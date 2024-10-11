import socket
import time
from PyQt5.QtWidgets import *
from ipaddress import ip_address
import sys




class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        self.app = QApplication([])
        self.app.setStyle('Fusion')

        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.gui = QLabel('GUI')

        self.ip_address = QLabel("IP Address")
        self.ip_address_field = QLineEdit()
        self.ports = QLabel("Ports")
        self.ports_field = QLineEdit()

        self.submit_button = QPushButton("submit")
        self.submit_button.clicked.connect(self.input)

        self.layout.addWidget(self.gui)
        self.layout.addWidget(self.ip_address)
        self.layout.addWidget(self.ip_address_field)
        self.layout.addWidget(self.ports)
        self.layout.addWidget(self.ports_field)
        self.layout.addWidget(self.submit_button)

        self.gui.show()
        self.ip_address.show()
        self.ports.show()


        self.window.setLayout(self.layout)
        self.window.show()
        self.app.exec()

    def input(self,ip_address, ports):
        print("pressed")
        print(self.ip_address)
        print(self.ports)




def scanner(ip,port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect(ip,port)
        print(f"Port {port} is open")
    except:
        None

def main():
    # create pyqt5 app
    app = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()

    # showing the window
    window.show()

    # start the app
    sys.exit(app.exec())


if __name__ == "__main__":
    main()