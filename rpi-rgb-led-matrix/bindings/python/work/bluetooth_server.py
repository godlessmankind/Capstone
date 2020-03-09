#!~/capstone/venv_capstone/bin/python
import bluetooth
import subprocess
import os


class bt_server:


    def __init__(self):


        if __name__ == '__main__':
            self.__correct_folder()

        self.server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.server_sock.bind(("", bluetooth.PORT_ANY))
        self.server_sock.listen(1)

        self.port = self.server_sock.getsockname()[1]

        self.uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

        # try:
        bluetooth.advertise_service(self.server_sock, "SampleServer", service_id=self.uuid,
                                    service_classes=[self.uuid, bluetooth.SERIAL_PORT_CLASS],
                                    profiles=[bluetooth.SERIAL_PORT_PROFILE],
                                    # protocols=[bluetooth.OBEX_UUID]
                                    )
        # except bluetooth.btcommon.BluetoothError:
        #     subprocess.call(['sudo', 'hciconfig', 'hciX piscan'])
        #     print("Bluetooth server is ready to accept clients")

        #     bluetooth.advertise_service(self.server_sock, "SampleServer", service_id=self.uuid,
        #                     service_classes=[self.uuid, bluetooth.SERIAL_PORT_CLASS],
        #                     profiles=[bluetooth.SERIAL_PORT_PROFILE],
        #                     # protocols=[bluetooth.OBEX_UUID]
        #                     )

        self.__connect_to_device()


    def __connect_to_device(self):
        print("Waiting for connection on RFCOMM channel", self.port)

        self.client_sock, client_info = self.server_sock.accept()
        print("Accepted connection from", client_info)


    def recive_data(self):
        try:
            while True:
                recv_data = self.client_sock.recv(1024)
                if not recv_data:
                    break
                data = recv_data.decode('utf-8')
                print("Received", data)

                return data

        except OSError:
            pass

        print("Disconnected.")

        self.client_sock.close()
        self.server_sock.close()
        print("All done.")


    def __correct_folder(self):
        PRJ_FLDR = os.path.dirname(os.path.realpath(__file__))
        if os.getcwd() != PRJ_FLDR:
            os.chdir(PRJ_FLDR)


def main():
    bt = bt_server()
    bt.recive_data

if __name__ == '__main__':
    main()