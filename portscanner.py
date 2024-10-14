import socket
import time
from xmlrpc.client import Boolean

from PyQt5.QtWidgets import *
from ipaddress import ip_address
import sys

def scanner(ip,port):
    result = None
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect(ip,port)
        print(f"Port {port} is open")
        result = True
        return result
    except:
        result = False
        return result

def check_ip(addr):
    try:
        socket.inet_aton(addr)
        return True
    except socket.error:
        return False


class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        self.app = QApplication([])
        self.app.setStyle('Fusion')
        title = "Port scanner"
        self.setWindowTitle(title)
        self.window = QWidget()
        self.layout = QVBoxLayout()


        self.ip_address = QLabel("IP Address")
        self.ip_address_field = QLineEdit()
        self.ports = QLabel("Ports")
        self.ports_field = QLineEdit()

        self.submit_button = QPushButton("submit")
        self.submit_button.clicked.connect(self.test)

        self.output_ipv4 = QLabel()
        self.output = QLabel()


        self.layout.addWidget(self.ip_address)
        self.layout.addWidget(self.ip_address_field)
        self.layout.addWidget(self.ports)
        self.layout.addWidget(self.ports_field)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.output_ipv4)
        self.layout.addWidget(self.output)

        self.ip_address.show()
        self.ports.show()


        self.window.setLayout(self.layout)
        self.window.show()
        self.app.exec()

    def test(self):  # <- With "self"
        print("Test")
        ip = self.get_ipv4_address()
        print(self.ports_field.text())
        ports_input = self.ports_field.text()
        des_ports_input = ports_input.split(",")
        output_ports = ""
        print(des_ports_input)
        for i in des_ports_input:
            scan_string = ("Scanning ip {ip} and port {p} ".format(ip=ip,p=i))
            self.output.setText(scan_string)
            output_text = ""
            result = scanner(ip,i)
            if result is False:
               print("IP and port {port} aren't available".format(port=i))
               output_text = "IP and port {port} aren't available".format(port=i)
               output_ports = output_ports+output_text
            else:
                output_string = "Port {port} open at ip {ip]"
                output_ports = output_ports+output_string
            self.output.setText(output_ports)

    def get_ipv4_address(self):
        ip = self.ip_address_field.text()
        isip = check_ip(ip)
        print(isip)
        if isip is False:
            self.output_ipv4.setText("No IPv4")
        else:
            self.output_ipv4.setText("IPv4 address")
        return ip


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