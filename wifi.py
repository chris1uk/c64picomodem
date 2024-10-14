import network
import ujson

class wifi():
    file_name = 'settings.json'
    settings ={"ssid":"new","password":"password"}
    nic = network.WLAN(network.STA_IF)
    nic.active(True)

    def wifi_connect(self):
        self.nic.connect(self.settings["ssid"],self.settings["password"])

    def wifi_status(self):
        status = self.nic.status()
        if status == 0: return "no connection and no activity"
        if status == 1: return "connecting in progress"
        if status == -3: return "failed due to incorrect password"
        if status == -2: return "failed because no access point replied"
        if status == -1: return "failed due to other problems"
        if status == 3: return "connection successful"

    def wifi_scan(self):
        ssid = []
        networks =  (self.nic.scan())
        for item in networks:
            ssid.append(item[0].decode("utf-8"))
        return ssid

    def save(self):
        settings_json = ujson.dumps(self.settings)
        try:
            f = open(self.file_name,'w')
            f.write(settings_json)
            f.close()
            return True
        except:
            return False

    def load(self):
        try:
            f = open(self.file_name,'r')
            settings_string=f.read()
            f.close()
            self.settings = ujson.loads(settings_string)
            return True
        except:
            return False

    def wifi_info(self):
        retstr = ""
        if self.wifi_status() == "connection successful":
            retstr+="\nWelcome to my NOT\n hayes compatible wifi modem\n\n"
            retstr+="\nWifi is connected :)\n\n"
            retstr+="SSID: "+self.nic.config('ssid')+"\n"
            retstr+="CHANNEL: "+str(self.nic.config('channel'))+"\n"
            retstr+="TX POWER: "+str(self.nic.config('txpower'))+"\n"
        else:
            retstr = self.wifi_status()
        return retstr
