class UsbDevice(object):
        def __init__(self, usbD):
            self.name = usbD['name']
            self.ip = usbD['ip']
            self.netmask = usbD['netmask']

class config(object):
    def __init__(self, a,b,c,d,e):
        self.startAfter = int(a)
        self.waitToCheck = int(b)
        self.targetHost = c
        self.pingCount = d
        self.usbDevices:list[UsbDevice] = []
        for device in e:
            self.usbDevices.append(UsbDevice(device))