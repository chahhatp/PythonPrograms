import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range")
    options = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    #arp_request.show() 
    #arp_request.pdst=ip
    #print(arp_request.summary())    
    #scapy.ls(scapy.ARP())           #listing the contents        
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")    #Ethernet Object #ff:ff:ff:ff:ff:ff --> default broadcast 
    #scapy.ls(scapy.Ether())
    #broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    #print(arp_request_broadcast.summary())
    #arp_request_broadcast.show()
    #answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1)
    answered_list= scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac":element[1].hwsrc}
        clients_list.append(client_dict)
        #print(element[1].psrc + "\t\t" + element[1].hwsrc)
        #print(element[1].show())
        #print(element[1].hwsrc)
    return clients_list

def print_result(result_list):    
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for client  in result_list:
        print(client)

options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)