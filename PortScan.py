import socket #Import Socket Library
import threading #Import Multithreading to allow for faster scan speeds

def scan_port(host, port, timeout):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        if result == 0:
            print("Port {} is open on host {}".format(port, host))
            service_name = socket.getservbyport(port)
            if service_name:
                print("Service running on port {}: {}".format(port, service_name))
            else:
                print("Service running on port {}: Unknown".format(port))
        sock.close()
    except:
        print("An error occurred while scanning host {} on port {}".format(host, port))
#Main function of program
def main():
    while True:
        host = input("Enter a host to scan: ")
        port_range = input("Enter a range of ports to scan (ex: 1-65535): ")
        scan_type = input("Enter type of scan (stealthy/normal): ")
        ports = [int(x) for x in port_range.split("-")]
        start_port, end_port = ports[0], ports[-1]
        timeout = 0.1 # default timeout value
        thread_count = 10 # default thread count
        if scan_type == 'stealthy':
            timeout = 2 # increase timeout value for stealthy scan
            thread_count = 5 # reduce thread count for stealthy scan
        threads = []
        for port in range(start_port, end_port + 1):
            thread = threading.Thread(target=scan_port, args=(host, port, timeout))
            threads.append(thread)
            if len(threads) == thread_count:
                for t in threads:
                    t.start()
                for t in threads:
                    t.join()
                threads = []

#Init call start of program
if __name__ == '__main__':
    main()
