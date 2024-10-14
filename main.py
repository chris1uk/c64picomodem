import bbs_socket
import time
import wifi
class hayes_modem():
    bbs = bbs_socket.bbs_socket()
    wifi=wifi.wifi()
    Hook = True #start phone on hook
    Echo =   True #start with echo on
    Busy = False
    connected = False
    Command_mode = False
    response = []

    def ok(self):
        self.response.append("OK\n")

    def close_connection(self):
        if self.connected== True:
            self.Busy=False
            self.connected = False
            self.bbs.close_socket()
            self.response.append("\nConnection Closed\n")

    def process_command(self,cmd):
        cmd = cmd.replace(" ", "") #cmd = cmd.upper().replace(" ", "")
        self.response = []
        cmd = cmd.strip()
        cmd = cmd.split(";")
        if self.Busy == False:
            for item in cmd:
                if item[:4].upper() == "ATDT":#if item.split(" ")[0] == "ATDT":
                    if len(item) >4:
                        addr = item[4:]#item.split(" ")
                        addr = addr.split(":")#addr[1].split(":")
                        if len(addr) ==2:
                            host = addr[0]
                            port = addr[1]
                            if self.bbs.conn(host,port):
                                #print (self.bbs.read_data())
                                self.Busy = True
                                self.connected = True
                                #self.response.append("RING\n")
                                self.response.append("CONNECT 2400\n")
                            else:
                                #failed
                                self.response.append("NO CARRIER\n")
                    else:
                        if self.connected == True:
                            self.Busy = True
                        self.ok()
                elif item.upper() == "ATE0":
                    self.Echo = False
                    self.ok()
                elif item[:3].upper() == "ATM":
                    #self.Echo = False
                    self.ok()
                elif item[:3].upper() == "ATV":
                    #self.Echo = False
                    self.ok()

                elif item.upper() == "ATE1":
                    self.Echo = True
                    self.ok()
                elif item.upper() =="HELP":
                    retstr="\n\n"
                    retstr+= "ATDT - dial\n"
                    retstr+= "ATE0 - Echo off\n"
                    retstr+= "ATE1 - Echo on\n"
                    retstr+= "ATM? - not implemented but\n responds okay\n"
                    retstr+= "ATV? - not implemented but\n responds okay\n"
                    retstr+= "ATH - hang up\n"
                    retstr+= "SSID - set ssid\n"
                    retstr+= "PASSWD - set password\n"
                    retstr+= "SAVE - save settings\n"
                    retstr+= "CONNECT - connect wifi\n"
                    retstr+= "ATI - show wifi connectin information\n"
                    retstr+="+++ - command mode\n\n"
                    self.response = retstr
                elif item.upper() == "ATI":
                    self.response = self.wifi.wifi_info()+"\n"
                    if not self.response:
                        self.response = "No response try again!\n"
                elif item[:4].upper() == "SSID":
                    self.wifi.settings["ssid"] = item[4:]
                    self.response = "SSID set make sure to\n SAVE setting and CONNECT\n\n"
                elif item[:6].upper() == "PASSWD":
                    self.wifi.settings["password"] = item[6:]
                    self.response = "PASSWD  set make sure to\n SAVE setting and CONNECT\n\n"
                elif item[:4].upper() == "SAVE":
                    self.wifi.save()
                    self.response = "Settings saved now CONNECT\n\n"
                elif item[:7].upper() == "CONNECT":
                    self.wifi.wifi_connect()
                    self.response = "Check connection status with ATI\n\n"
                elif item =="+++":
                    pass
                elif item.upper() == "ATH":
                    self.close_connection()
                    if self.connected== True:
                        self.Busy=False
                        self.connected = False
                        self.bbs.close_socket()
                        self.response.append("Connection Closed\n")
                else:
                    self.response.append("ERROR\n")
        for item in cmd:
            if item == "+++" and self.Busy == True:
                self.Busy = False;
                self.response.append("\nCommand mode enabled,use ATDT to continue session\n")
        return self.response
