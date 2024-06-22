# Form implementation generated from reading ui file 'save-window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import subprocess, os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(412, 184)
        Form.setMinimumSize(QtCore.QSize(100, 100))
        Form.setStyleSheet("background-color: gray;")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(240, 140, 158, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.saveButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.noButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.noButton.setObjectName("noButton")
        self.horizontalLayout.addWidget(self.noButton)
        self.commitMessage = QtWidgets.QTextEdit(parent=Form)
        self.commitMessage.setGeometry(QtCore.QRect(30, 30, 361, 101))
        self.commitMessage.setStyleSheet("background-color: white")
        self.commitMessage.setObjectName("commitMessage")
        self.saveButton.clicked.connect(lambda: self.save(self.commitMessage.toPlainText()))
        self.noButton.clicked.connect(self.close)

        self.retranslateUi(Form)
        self.noButton.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def save(self, commitMessage):
        print(commitMessage)
        directoryPath = r'.\Bulaloi-App-Development-Experiment/next-app'
        fullPath = os.path.join(directoryPath)
        print(fullPath)
        command = subprocess.run(['cd', fullPath , '&&', 'git', 'add', '.', '&&', 'git', 'commit', '-m', f'"{commitMessage}"', '&&', 'git', 'push', 'origin', 'main'], shell=True, capture_output=True, text=True)
        print(command.stdout)
        print(command.returncode)
        print(command.stderr)

    def close(self):
        Form.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.saveButton.setText(_translate("Form", "Save"))
        self.noButton.setText(_translate("Form", "No"))
        self.commitMessage.setPlaceholderText(_translate("Form", "Commit message..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
