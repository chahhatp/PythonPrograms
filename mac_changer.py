#!/usr/bin/env python
import subprocess
import optparse

# interface =  input("Interface -> ")
# new_mac = input("New MAC -> ")


def get_args():

    parser = optparse.OptionParser()
    parser.add_option("--i", "--interface", dest="interface", help="Interface to change its Mac")
    parser.add_option("--m", "--mac", dest="new_mac", help="Mac addresss")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please give interface")
    elif not options.new_mac:
        parser.error("please give mac_address")
    return options

    


# interface = options.interface
# new_mac = options.new_mac

def change_mac(interface, new_mac):
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])



options = get_args()

change_mac(options.interface, options.new_mac)



# subprocess.call("sudo ifconfig " + interface + " down", shell=True)
# subprocess.call("sudo ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("sudo ifconfig " + interface + " up", shell=True)

# subprocess.call(["sudo", "ifconfig", interface, "down"])
# subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
# subprocess.call(["sudo", "ifconfig", interface, "up"])





