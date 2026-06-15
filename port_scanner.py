import socket
from datetime import datetime as dt
import sys

def main():
    # Check if arguments are passed via command line
    if len(sys.argv) > 1:
        if len(sys.argv) == 4:
            target_arg = sys.argv[1]
            try:
                start_port = int(sys.argv[2])
                end_port = int(sys.argv[3])
            except ValueError:
                print("Error: Port range arguments must be integers.")
                sys.exit(1)
        else:
            print("Usage: python port_scanner.py <target> <start_port> <end_port>")
            sys.exit(1)
    else:
        # Prompt for inputs interactively
        try:
            target_arg = input("Enter target hostname or IP to scan: ").strip()
            if not target_arg:
                print("Error: Hostname/IP cannot be empty.")
                sys.exit(1)

            start_port = int(input("Enter starting port: ").strip())
            end_port = int(input("Enter ending port: ").strip())
        except ValueError:
            print("Error: Port numbers must be integers.")
            sys.exit(1)
        except KeyboardInterrupt:
            print("\nExiting program.")
            sys.exit(0)

    # Validate and resolve target (supports both IPv4 and IPv6)
    try:
        addr_info = socket.getaddrinfo(target_arg, None)
        targets = []
        seen_ips = set()
        for item in addr_info:
            family = item[0]
            sockaddr = item[4]
            ip = sockaddr[0]
            if ip not in seen_ips:
                seen_ips.add(ip)
                targets.append((ip, family))
    except socket.gaierror:
        print(f"Error: Hostname could not be resolved: {target_arg}")
        sys.exit(1)

    # Validate port range
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Error: Invalid port range. Must be between 1 and 65535, with start port <= end port.")
        sys.exit(1)

    print("-" * 50)
    print(f"Scanning target: {target_arg} ({', '.join(ip for ip, _ in targets)})")
    print(f"Scanning ports: {start_port} to {end_port}")
    time1 = dt.now()
    print("Start Time: " + str(time1))
    print("-" * 50)

    open_ports = []

    try:
        for port in range(start_port, end_port + 1):
            is_open = False
            print(f"Scanning port {port}...")
            for ip, family in targets:
                try:
                    with socket.socket(family, socket.SOCK_STREAM) as s:
                        s.settimeout(0.9)
                        if family == socket.AF_INET6:
                            addr = (ip, port, 0, 0)
                        else:
                            addr = (ip, port)
                        result = s.connect_ex(addr)
                        if result == 0:
                            is_open = True
                            break
                except socket.error:
                    continue
            
            if is_open:
                print(f"[+] Port {port} is open")
                open_ports.append(port)
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit(0)
    except socket.error:
        print("Error: Couldn't connect to server.")
        sys.exit(1)

    time2 = dt.now()

    print("-" * 50)
    if not open_ports:
        print("No open ports found.")
    else:
        print(f"Open ports found: {', '.join(map(str, open_ports))}")

    print("Scanning completed in:", time2 - time1)
    print("-" * 50)

if __name__ == "__main__":
    main()
