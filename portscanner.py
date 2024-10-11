import socket
import time
from PyQt5.QtWidgets import *
from ipaddress import ip_address

def submit():
    print("pressed")

def gui():
    app = QApplication([])
    app.setStyle('Fusion')
    window = QWidget()
    layout = QVBoxLayout()
    gui = QLabel('GUI')

    ip_address = QLabel("IP Address")
    ip_address_field = QLineEdit()
    ports = QLabel("Ports")
    ports_field = QLineEdit()

    submit_button = QPushButton("submit")
    submit_button.clicked.connect(submit)

    layout.addWidget(gui)
    layout.addWidget(ip_address)
    layout.addWidget(ip_address_field)
    layout.addWidget(ports)
    layout.addWidget(ports_field)
    layout.addWidget(submit_button)

    gui.show()
    ip_address.show()
    ports.show()


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