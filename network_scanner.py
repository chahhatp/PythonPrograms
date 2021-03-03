#code needs root privilages

#Way 1
# import scapy.all as scapy

# def scan(ip):
#     scapy.arping(ip)

# scan("172.20.10.1/24")

import scapy.all as scapy
import optparse

def scan(ip):
    #sets the ip address
    arp_request = scapy.ARP()
    arp_request.pdst = ip
    #scapy.ls(scapy.ARP())
    #print(arp_request.summary())


    #sets the broadcast address
    broadcast = scapy.Ether()
    #scapy.ls(scapy.Ether())
    broadcast.dst = "ff:ff:ff:ff:ff:ff"
    #print(broadcast.summary())
    
    #combining the two
    arp_request_broadcast = broadcast/arp_request
    #print(arp_request_broadcast.summary())

    #can use show() for more details
    #arp_request_broadcast.show()
    
    #send recieve the value srp(), returns 2 values
    answered_list =  scapy.srp(arp_request_broadcast, timeout=10, verbose=False)[0]
    #print(answered_list.summary())
    
    


    
    clients_list=[]
    for element in answered_list:
        clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(clients_dict)
       
  

    return clients_list
        
def print_result(result_list):
    print("IP\t\t||\tMAC Address\n =====================================")
    for client in result_list:
        print(client["ip"]+"\t\t"+client["mac"])

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("--t", "--target", dest="target_ip", help="Please enter the target ip ")
    (options, arguments)=parser.parse_args()
    if not options.target_ip:
        parser.error("enter the ip")
    return options

   


options = get_args()
scan_result = scan(options.target_ip)
print_result(scan_result)
