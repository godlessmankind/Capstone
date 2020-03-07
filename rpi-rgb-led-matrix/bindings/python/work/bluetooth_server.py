import bluetooth


class bt_server():

    def __init__(self):

        self.server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.server_sock.bind(("", bluetooth.PORT_ANY))
        self.server_sock.listen(1)

        self.port = self.server_sock.getsockname()[1]

        self.uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

        bluetooth.advertise_service(self.server_sock, "SampleServer", service_id=self.uuid,
                                    service_classes=[self.uuid, bluetooth.SERIAL_PORT_CLASS],
                                    profiles=[bluetooth.SERIAL_PORT_PROFILE],
                                    # protocols=[bluetooth.OBEX_UUID]
                                    )
        self.connect_to_device()


    def connect_to_device(self):
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
                
                print(type(data))

                return data

        except OSError:
            pass

        print("Disconnected.")

        self.client_sock.close()
        self.server_sock.close()
        print("All done.")

