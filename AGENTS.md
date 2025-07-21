# OSPF Tunnel Project

This file documents the development of the OSPF Tunnel project.

## Project Overview

The goal of this project is to create a tool that can bypass network restrictions by tunneling TCP traffic through OSPF packets. The project consists of two main components: Server A, which encapsulates TCP traffic into OSPF packets, and Server B, which de-encapsulates the traffic and forwards it to its destination.

## Development Steps

1.  **`README.md` Creation**: I started by creating a `README.md` file to provide a clear and concise overview of the project. This file explains the purpose of the tool, how it works, and includes a disclaimer about its use.

2.  **Server A Development**: I created the `server_a.py` script, which is responsible for capturing raw TCP packets and encapsulating them into OSPF packets. I used the `scapy` library to handle packet manipulation, which simplifies the process of creating and sending custom packets.

3.  **Server B Development**: Next, I developed the `server_b.py` script. This server listens for incoming OSPF packets, extracts the original TCP data, and forwards it to the Xray core. This script also uses `scapy` to parse the incoming packets and extract the required information.

4.  **Main Execution Script**: To make the tool easy to use, I created a `main.py` script that serves as the entry point for running both servers. It uses the `argparse` library to provide a simple command-line interface, allowing the user to start either Server A or Server B with a single command.

5.  **Final Review**: After creating all the necessary files, I will conduct a final review to ensure that the code is clean, well-documented, and functions as expected. I will also verify that the `README.md` provides clear instructions for setting up and using the tool.

## Technologies Used

-   **Python**: The core programming language for the project.
-   **Scapy**: A powerful Python library for packet manipulation, used for creating and parsing OSPF and TCP packets.
-   **socket**: A standard Python library for low-level network I/O.
-   **argparse**: A standard Python library for parsing command-line arguments.
