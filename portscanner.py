import socket
import time
from xmlrpc.client import Boolean

from PyQt5.QtWidgets import *
from ipaddress import ip_address, IPv4Address
import sys

class Window(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
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

        self.set_layout()

        self.ip_address.show()
        self.ports.show()


        self.window.setLayout(self.layout)
        self.window.show()
        self.app.exec()

    def set_layout(self):
        self.layout.addWidget(self.ip_address)
        self.layout.addWidget(self.ip_address_field)
        self.layout.addWidget(self.ports)
        self.layout.addWidget(self.ports_field)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.output_ipv4)
        self.layout.addWidget(self.output)

    def scanner(self,ip, port):

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                s.connect((ip, int(port)))
                s.sendall(b"Hello, world")
                data = s.recv(1024)

                print(f"Received {data!r}")
                return data
        except Exception as e:
            print(e)
            return e

    def validIPAddress(self,IP: str) -> str:
        try:
            return "IPv4" if type(ip_address(IP)) is IPv4Address else "IPv6"
        except ValueError:
            return False

    def test(self):  # <- With "self"
        print("Test")
        ip = self.get_ip_address()
        self.get_scanning_for_ip_and_ports(ip)

    def get_scanning_for_ip_and_ports(self, ip):
        print(self.ports_field.text())
        ports_input = self.ports_field.text()
        des_ports_input = ports_input.split(",")
        output_ports = ""
        print(des_ports_input)
        for i in des_ports_input:
            scan_string = ("Scanning ip {ip} and port {p} ".format(ip=ip, p=i))
            self.output.setText(scan_string)
            output_text = ""
            result = self.scanner(ip, i)
            if result is False:
                print("IP and port {port} aren't available".format(port=i))
                output_text = "IP and port {port} aren't available".format(port=i)
                output_ports = output_ports + output_text + "\n"
            else:
                print("{0} is open".format(i))
                output_string = "{0} is open".format(i)
                output_ports = output_ports + output_string + "\n"
            self.output.setText(output_ports)

    def get_ip_address(self):
        ip = self.ip_address_field.text()
        check_if_ip =self. validIPAddress(ip)
        print(check_if_ip)
        if check_if_ip is False:
            self.output_ipv4.setText("No IPv4 or IPv6 address")
        else:
            self.check_ip_version(check_if_ip)

        return ip

    def check_ip_version(self, check_if_ip):
        if check_if_ip == "IPv4":
            self.output_ipv4.setText("Ipv4 address")
        elif check_if_ip == "IPv6":
            self.output_ipv4.setText("IPv6 address")
        else:
            self.output_ipv4.setText("IPv4 or IPv6 address")


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