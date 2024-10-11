import socket
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from ipaddress import ip_address


def gui():
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    label = QLabel('GUI')

    label1 = QLabel("IP Address")

    label2 = QLabel("Ports")
    layout.addWidget(label)
    layout.addWidget(label1)
    layout.addWidget(label2)

    label.show()
    label1.show()
    label2.show()
    window.setLayout(layout)
    window.show()
    app.exec()






def scanner(ip,port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect(ip,port)
        print(f"Port {port} is open")
    except:
        None

def main():
    gui()


if __name__ == "__main__":
    main()