import socket
from scapy.all import IP, TCP, Raw, send

def capture_and_forward(listen_port, target_ip, target_port):
    """
    Captures TCP packets on a specified port, encapsulates them in OSPF,
    and forwards them to a target IP and port.
    """
    # Create a raw socket to listen for incoming packets
    with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP) as s:
        s.bind(('0.0.0.0', listen_port))

        print(f"[*] Listening for TCP packets on port {listen_port}...")

        while True:
            # Receive a TCP packet
            packet, addr = s.recvfrom(65535)

            # Encapsulate the TCP packet into an OSPF packet
            ospf_packet = IP(dst=target_ip, proto=89) / packet

            # Send the OSPF packet to Server B
            send(ospf_packet, verbose=0)
            print(f"[*] Sent encapsulated packet to {target_ip}:{target_port}")

if __name__ == '__main__':
    # Configuration for Server A
    LISTEN_PORT = 8080  # Port to capture TCP packets on
    TARGET_IP = '127.0.0.1'  # IP address of Server B
    TARGET_PORT = 5000  # Port to send OSPF packets to

    capture_and_forward(LISTEN_PORT, TARGET_IP, TARGET_PORT)
