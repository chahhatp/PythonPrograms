#!/usr/bin/env python
import subprocess
import optparse
import re
import string
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

#change_mac(options.interface, options.new_mac)



# subprocess.call("sudo ifconfig " + interface + " down", shell=True)
# subprocess.call("sudo ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("sudo ifconfig " + interface + " up", shell=True)

# subprocess.call(["sudo", "ifconfig", interface, "down"])
# subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
# subprocess.call(["sudo", "ifconfig", interface, "up"])

def return_mac_address(interface):
    return_value_of_ifconfig = str(subprocess.check_output(["ifconfig", interface]))

    mac_return = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", return_value_of_ifconfig)
    if mac_return:
        return mac_return.group(0)
    else:
        print("Cannot get the mac address")



current_mac = return_mac_address(options.interface)

print("Current Mac is "+ str(current_mac))

change_mac(options.interface, options.new_mac)
current_mac2 = return_mac_address(options.interface)


if current_mac2.lower() == options.new_mac.lower():
    print("Mac changed to " + current_mac2)
else:
    print("Mac Changed")









