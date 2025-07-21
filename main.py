import argparse
import subprocess
import sys

def main():
    """
    Main function to run Server A and Server B.
    """
    parser = argparse.ArgumentParser(description='OSPF Tunnel')
    parser.add_argument('server', choices=['a', 'b'], help='Server to run (a or b)')
    args = parser.parse_args()

    if args.server == 'a':
        print("[*] Starting Server A...")
        try:
            subprocess.run([sys.executable, 'server_a.py'])
        except FileNotFoundError:
            print("[!] Error: server_a.py not found. Make sure it's in the same directory.")
    elif args.server == 'b':
        print("[*] Starting Server B...")
        try:
            subprocess.run([sys.executable, 'server_b.py'])
        except FileNotFoundError:
            print("[!] Error: server_b.py not found. Make sure it's in the same directory.")

if __name__ == '__main__':
    main()
