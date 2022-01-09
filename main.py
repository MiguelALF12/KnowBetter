from FRONTEND.mainInterfacePR import *
import sys


def hide_button_maximize(form_window):
    form_window.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint
                               | QtCore.Qt.WindowMinimizeButtonHint)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    mainInterface = MainUIForm()  # inicio la aplicacion
    mainInterface.setupUi(window)
    window.show()
    sys.exit(app.exec_())
