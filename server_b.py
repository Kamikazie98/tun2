import socket
from scapy.all import IP, TCP, send

def receive_and_forward(listen_ip, listen_port, xray_ip, xray_port):
    """
    Receives OSPF packets, extracts the original TCP packets, and forwards them
    to the Xray core.
    """
    # Create a raw socket to listen for incoming OSPF packets
    with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_OSPF) as s:
        s.bind((listen_ip, listen_port))

        print(f"[*] Listening for OSPF packets on {listen_ip}:{listen_port}...")

        while True:
            # Receive an OSPF packet
            packet, addr = s.recvfrom(65535)

            # Extract the original TCP packet from the OSPF payload
            ip_packet = IP(packet)

            # Check if the packet contains a TCP layer
            if TCP in ip_packet:
                tcp_packet = ip_packet[TCP]

                # Forward the TCP packet to the Xray core
                send(IP(dst=xray_ip)/tcp_packet, verbose=0)
                print(f"[*] Forwarded TCP packet to {xray_ip}:{xray_port}")

if __name__ == '__main__':
    # Configuration for Server B
    LISTEN_IP = '127.0.0.1'  # IP address to listen on
    LISTEN_PORT = 5000  # Port to listen for OSPF packets
    XRAY_IP = '127.0.0.1'  # IP address of the Xray core
    XRAY_PORT = 1080  # Port of the Xray core

    receive_and_forward(LISTEN_IP, LISTEN_PORT, XRAY_IP, XRAY_PORT)
