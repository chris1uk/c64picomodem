import socket
class bbs_socket():
    connected = False

    def conn(self,host,port):
        try:
            addr_info = socket.getaddrinfo(host, int(port))
            addr = addr_info[0][-1]
            self.client_socket = socket.socket()
            self.client_socket.connect(addr)
            self.client_socket.settimeout(0)
            self.connected = True
            return True

        except:
            return False

    def read_data(self):
        try:
            data = self.client_socket.recv(256)
            return data
        except:
            return None

    def send_data(self,data):
        try:
            self.client_socket.send(data)
            return True
        except:
            return False

    def close_socket(self):
         self.client_socket.close()
         self.connected = False
