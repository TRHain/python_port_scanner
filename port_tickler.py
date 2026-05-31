import socket

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(.5)
            return s.connect_ex((ip, port)) == 0
    except Exception:
        return False


ip = "127.0.0.1"
open_ports = []

for port in range(20, 1025):

    # Print progress every 50 ports
    if port % 50 == 0:
        print(f"Scanned through port {port}...")

    if scan_port(ip, port):
        print(f"Port {port} OPEN")
        open_ports.append(port)

# Final results
print("\nScan complete.")

if open_ports:
    print("Open ports found:")
    for port in open_ports:
        print(port)
else:
    print("No open ports found.")