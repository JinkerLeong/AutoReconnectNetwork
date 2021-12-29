import json
from configModule.myconfig import *
from sys import stdout
from helper import print

CONFIG_PATH = "/etc/AutoReconnectNetwork/config.json"

def jsonToConfig(d):
    return config(d['startAfter'],d['waitToCheck'],d['targetHost'], d['pingCount'], d['usbDevices'])

def loadConfig()->config:
    print("load config from /etc/AutoReconnectNetwork/config.json")
    with open(CONFIG_PATH) as f:
        return jsonToConfig(json.load(f))

globalConfig:config = loadConfig()

def getConfig()->config:
    return globalConfig

def printConfig():
    print("=========================")
    print("[Config]")
    print(f"Start after seconds: {globalConfig.startAfter}")
    print(f"Wait to check seconds: {globalConfig.waitToCheck}")
    print(f"Target host: {globalConfig.targetHost}")
    print(f"Ping count: {globalConfig.pingCount}")
    num = 0
    for device in globalConfig.usbDevices:
        num = num + 1
        print(f"Usb device#{num}: {device.name}, {device.ip}, {device.netmask}")
    print("=========================")
    stdout.flush()