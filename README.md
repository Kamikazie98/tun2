# OSPF Tunnel

This project provides a simple yet effective method for bypassing network restrictions by tunneling TCP traffic through OSPF packets. It is designed to be a proof-of-concept, so it may require additional enhancements for production use.

## How It Works

The core idea is to encapsulate standard TCP packets within OSPF packets, which are often less scrutinized by network filtering systems. This allows the TCP traffic to traverse restricted networks without being easily detected or blocked.

The project consists of two main components:

-   **Server A**: Captures raw TCP packets, wraps them in an OSPF header, and sends them to Server B.
-   **Server B**: Receives the OSPF packets, extracts the original TCP packets, and forwards them to a specified destination, such as an Xray core.

This approach effectively disguises the nature of the traffic, making it appear as legitimate OSPF routing updates.

## Features

-   **TCP Tunneling**: Encapsulates TCP traffic within OSPF packets to bypass network filters.
-   **Proof-of-Concept**: Demonstrates the viability of the tunneling technique.
-   **Lightweight**: Minimal dependencies and a straightforward implementation.

## Disclaimer

This tool is intended for educational and research purposes only. The developers are not responsible for any misuse or damage caused by this software.
