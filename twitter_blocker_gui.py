from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap, QFont, QRegularExpressionValidator
from PySide6.QtCore import QTimer, QRegularExpression, QPoint, QObject, QThread, Signal
from PySide6.QtWidgets import QMessageBox
from twitter_blocker import Blocker, UserWrapper, UserSuspendedError
from PIL.ImageQt import ImageQt
from ui_main_window import Ui_MainWindow
from ui_account_settings_dialog import Ui_settings_dialog
import sys


class BlockerWorker(QObject):
    finished = Signal()
    progress = Signal(int)
    status_changed = Signal(str)

    def __init__(self, blocker, user_id, reason):
        super(BlockerWorker, self).__init__()
        self.blocker = blocker
        self.user_id = user_id
        self.reason = reason

    def _blocking(self, ids_to_block):
        self.status_changed.emit("Blocking users")
        for i in self.blocker.block_users(self.user_id, ids_to_block, self.reason):
            self.progress.emit(i)
            self.status_changed.emit(f"Blocked users: {i}")
        self.finished.emit()

    def continue_(self):
        self.status_changed.emit("Blocking users")
        for i in self.blocker.continue_blocking():
            self.progress.emit(i)
            self.status_changed.emit(f"Blocked users: {i}")
        self.finished.emit()

    def run(self):
        ids_to_block = []
        self.status_changed.emit("Retrieving followers")
        batch = 0
        for ids in self.blocker.get_follower_ids(self.user_id):
            batch += 1
            limit_remaining = self.blocker.api.rate_limit.resources.get('followers').get('/followers/ids').get('remaining')
            # TODO: Instead of just waiting, the program should start blocking what's there already
            if limit_remaining == 0:
                self.status_changed.emit("Retrieving followers (waiting for rate limit to end)")
            else:
                self.status_changed.emit("Retrieving followers")
            print(f"Batch {batch}")
            ids_to_block.extend(ids)

        self._blocking(ids_to_block)


class AccountSettingsDialog(QtWidgets.QDialog, Ui_settings_dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, blocker):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.current_target_user: UserWrapper = None

        self.blocker = blocker
        if self.blocker.authenticated_user:
            self.fill_account_data()

        self.target_user_profile_pic_label.setScaledContents(True)
        self.target_user_screen_name_input.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Z0-9_-]+")))
        self.timer = QTimer()
        self.timer.setSingleShot(True)

        self.progress_bar.hide()
        self.status_label.hide()
        self.continue_blocking_button.hide()
        self.continue_last_block_run()
        self._init_events()
        self.show()

    def _init_events(self):
        self.timer.timeout.connect(self.set_target_user_data)
        self.target_user_screen_name_input.textEdited.connect(lambda: (
            self.timer.start(2000),
            self.target_user_screen_name_input.setStyleSheet("")
        ))
        self.block_user_button.clicked.connect(self.start_blocking)
        self.action_account.triggered.connect(self.show_account_settings_dialog)
        self.continue_blocking_button.clicked.connect(self.continue_blocking)

    def fill_account_data(self):
        image = ImageQt(self.blocker.authenticated_user.profile_pic)
        # it's weird but without the copy() the program crashes sometimes
        self.user_profile_pic_label.setPixmap(QPixmap.fromImage(image).copy())
        self.user_profile_pic_label.setScaledContents(True)
        self.user_screen_name_label.setText(f"@{self.blocker.authenticated_user.screen_name}")
        self.user_display_name_label.setText(self.blocker.authenticated_user.display_name)
        self.user_block_count_label.setText(f"{self.blocker.get_block_count()} blocks")

    def show_account_settings_dialog(self):
        settings_dialog = AccountSettingsDialog(self)
        account_data = self.blocker.get_account_settings()
        settings_dialog.consumer_key_edit.setText(account_data['consumer_key']),
        settings_dialog.consumer_secret_edit.setText(account_data['consumer_secret']),
        settings_dialog.access_token_key_edit.setText(account_data['access_token_key']),
        settings_dialog.access_token_secret_edit.setText(account_data['access_token_secret'])
        settings_dialog.accepted.connect(lambda x=settings_dialog: self.save_account_data(x))
        settings_dialog.exec()

    def save_account_data(self, dialog):
        self.blocker.save_account_settings(
            dialog.consumer_key_edit.text(),
            dialog.consumer_secret_edit.text(),
            dialog.access_token_key_edit.text(),
            dialog.access_token_secret_edit.text()
        )
        self.blocker.authenticate()
        if self.blocker.authenticated_user:
            self.fill_account_data()

    def set_target_user_data(self):
        def clear():
            self.target_user_screen_name_input.setStyleSheet("")
            self.target_user_profile_pic_label.clear()
            self.target_user_display_name_label.setText("")
            self.target_user_stats_label.setText("")
            self.target_user_description_label.setText("")
            self.current_target_user = None
            self.progress_bar.setValue(0)

        screen_name = self.target_user_screen_name_input.text()

        if not screen_name:
            clear()
        else:
            error = "The user does not exist."
            try:
                user = self.blocker.get_user(screen_name)
            except UserSuspendedError as e:
                print(e.message)
                user = None
                error = "The user has been suspended."

            if not user:
                QtWidgets.QToolTip.showText(self.target_user_screen_name_input.mapToGlobal(
                    QPoint(0, self.target_user_screen_name_input.height()/2)), error)
                clear()
                self.target_user_screen_name_input.setStyleSheet("QLineEdit { background: salmon; }")
                return

            self.current_target_user = user
            self.fill_target_user_data()

    def fill_target_user_data(self):
        self.target_user_profile_pic_label.setPixmap(QPixmap.fromImage(ImageQt(self.current_target_user.profile_pic).copy()))
        self.target_user_display_name_label.setText(self.current_target_user.display_name)
        self.target_user_stats_label.setText(f"{self.current_target_user.follower_count} Followers")
        self.target_user_description_label.setText(self.current_target_user.description)

    def continue_blocking(self):
        self.start_blocking(True)

    def start_blocking(self, continue_blocking=False):
        if not self.current_target_user:
            return

        self.progress_bar.setMaximum(self.current_target_user.follower_count)
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = BlockerWorker(self.blocker, self.current_target_user.twitter_id, self.block_reason_input.text())
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        if continue_blocking:
            self.thread.started.connect(self.worker.continue_)
        else:
            self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(lambda x: self.progress_bar.setValue(x))
        self.worker.status_changed.connect(lambda x: self.status_label.setText(x))
        # Final resets
        self.thread.finished.connect(
            lambda: (
                self.enable_ui(True),
                self.progress_bar.setValue(self.progress_bar.maximum()),
                QMessageBox.about(self, "Done", "Finished blocking everyone"),
                self.user_block_count_label.setText(f"{self.blocker.get_block_count()} blocks")
            )
        )
        self.thread.start()
        self.enable_ui(False)


    def enable_ui(self, enabled=True):
        self.target_user_screen_name_input.setEnabled(enabled)
        self.block_reason_input.setEnabled(enabled)
        self.block_user_button.setEnabled(enabled)
        self.continue_blocking_button.setEnabled(enabled)
        self.menubar.setEnabled(enabled)
        if enabled:
            self.block_user_button.show()
            self.block_reason_input.show()
            self.progress_bar.hide()
            self.status_label.hide()
        else:
            self.block_user_button.hide()
            self.continue_blocking_button.hide()
            self.block_reason_input.hide()
            self.progress_bar.show()
            self.status_label.show()

    def continue_last_block_run(self):
        remaining_blocks, reason = self.blocker.get_last_run_info()
        if remaining_blocks is not None and remaining_blocks > 0:
            user_id = self.blocker.get_last_run_target_id()
            self.current_target_user = self.blocker.get_user(user_id=user_id)
            self.target_user_screen_name_input.setText(self.current_target_user.display_name)
            self.target_user_screen_name_input.setEnabled(False)
            self.block_reason_input.setText(reason)
            self.block_reason_input.setEnabled(False)
            self.fill_target_user_data()
            self.block_user_button.hide()
            self.continue_blocking_button.show()


with Blocker() as b:
    app = QtWidgets.QApplication(sys.argv)
    # TODO make emojis show correctly again
    # Used to add the font to enable emojis in twitter profiles an names but it messes up
    # everything in Qt6/PySide6
    #app.font()
    #QFont.insertSubstitution(app.font().family(), "Noto Color Emoji")
    window = MainWindow(b)
    app.exec()
