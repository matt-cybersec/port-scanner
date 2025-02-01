import socket

def scan_ports(target, ports):
    print(f"\nScanning {target}...\n")
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Timeout for connection attempt

        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is CLOSED")
        sock.close()

if __name__ == "__main__":
    target = input("Enter target IP or domain: ")
    ports = [21, 22, 23, 25, 53, 80, 443, 3306, 8080]  # Common ports
    scan_ports(target, ports)
