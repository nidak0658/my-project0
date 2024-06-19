import pcapy
import dpkt

def print_ethernet_packet(pkt):
    eth = dpkt.ethernet.Ethernet(pkt)
    print("Ethernet Packet:")
    print(f"Source MAC: {':'.join('%02x' % b for b in eth.src)}")
    print(f"Destination MAC: {':'.join('%02x' % b for b in eth.dst)}")
    print(f"Ethernet Type: {eth.type}")
    print()

def print_ip_packet(pkt):
    ip = dpkt.ip.IP(pkt)
    print("IP Packet:")
    print(f"Source IP: {pcapy.util.inet_ntoa(ip.src)}")
    print(f"Destination IP: {pcapy.util.inet_ntoa(ip.dst)}")
    print(f"TTL: {ip.ttl}")
    print(f"Protocol: {ip.p}")
    print()

def print_tcp_packet(pkt):
    tcp = dpkt.tcp.TCP(pkt)
    print("TCP Packet:")
    print(f"Source Port: {tcp.sport}")
    print(f"Destination Port: {tcp.dport}")
    print(f"Sequence Number: {tcp.seq}")
    print(f"Acknowledgment Number: {tcp.ack}")
    print()

def packet_handler(header, data):
    print(f"Captured Packet Length: {header.getlen()}")
    print("Hexdump of Packet Data:")
    print(':'.join("{:02x}".format(ord(c)) for c in data))
    print()

    try:
        eth = dpkt.ethernet.Ethernet(data)
        print_ethernet_packet(data)
        
        if isinstance(eth.data, dpkt.ip.IP):
            print_ip_packet(eth.data.data)
            if isinstance(eth.data.data, dpkt.tcp.TCP):
                print_tcp_packet(eth.data.data.data)
    except Exception as e:
        print(f"Exception: {e}")

def start_sniffer(interface, packet_count):
    cap = pcapy.open_live(interface, 65536, True, 100)
    print(f"Listening on {interface}...")

    # Set a callback function to receive packets
    cap.loop(packet_count, packet_handler)

if __name__ == "__main__":
    interface = "eth0"  # Change this to your network interface name
    packet_count = 10   # Number of packets to capture

    start_sniffer(interface, packet_count)
