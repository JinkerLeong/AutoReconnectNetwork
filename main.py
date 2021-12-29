#!/usr/bin/python3

import sys, time, configModule.configManager as configManager, network
from helper import print

print("load config from /etc/AutoReconnectNetwork/config.json")
config = configManager.loadConfig("/etc/AutoReconnectNetwork/config.json")

def checkArgv():
    for a in sys.argv:
        if a == "-t":
            config.startAfter = 0

if __name__ == "__main__":
    checkArgv()
    print("====================")
    print("[Config]")
    configManager.printConfig()
    print("====================")
    print(f"Starting script after {config.startAfter} seconds:")
    time.sleep(config.startAfter)
    print("Now runing script...")
    while True:
        print("Check networking...")
        if network.checkNetworkPass():
            print("Networking normal..")
        else:
            print("Networking no access, trying restart networking..")
            network.restartNetworking()
            print("Networking restart done...")
        network.restartUsbDevices()
        print(f"Wait {config.waitToCheck} seconds to check again...")
        time.sleep(config.waitToCheck)