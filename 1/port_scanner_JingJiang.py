# ECE-303 Project-1 TCP Port Scanner
# Jing Jiang

import sys
import socket
from datetime import datetime

if __name__ == '__main__':
    # Parse the arguments
    if len(sys.argv) == 2:
        target = sys.argv[1]
        # default range of scan if no -p input found
        start = 20
        end = 1025
    elif len(sys.argv) == 5 and sys.argv[2]=='-p':
        target = sys.argv[1]
        try:
            start = int(sys.argv[3])
            end = int(sys.argv[4])
        except:
            print("Enter correct numbers in correct format.")
            sys.exit()
    elif len(sys.argv) == 4 and sys.argv[2]=='-p':
        target = sys.argv[1]
        try:
            portNums = sys.argv[3].split(':')
            start = int(portNums[0])
            end = int(portNums[1])
        except:
            print("Enter correct numbers in correct format.")
            sys.exit()
    else:
        print("Wrong Arguments.\nFormat: python port_scanner_JingJiang.py hostname [-p start end].")
        sys.exit()

    # get host
    try:
        targetIP = socket.gethostbyname(target)
        if start == 20 and end == 1025:
            isDefaultPortNum = "\n(No input for port range. Use default number start = 20, end = 1025.)"
        else:
            isDefaultPortNum = ""
        if end < start:    # detect if start port is larger than end port, if yes, swap
            print("ending port larger than starting port. Do swapping.")
            temp = start
            start = end
            end = temp
        print ('Starting scan on host', targetIP, ', from', start, 'to', end, isDefaultPortNum)
    except:
        print("Not found. Ending the program.")
        sys.exit()
    
    t1 = datetime.now()
    # scan for reserved ports
    for i in range(start, end+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((targetIP, i))

        if result == 0:
            try:
                ptcl = socket.getservbyport(i)
            except:
                ptcl = "Protocol Name Not Identified"
            print ('Port ', i, ': OPEN, Name: ', ptcl)
        s.close()

    # output the total time elapsed
    t2 = datetime.now()
    timeElapsed = t2 - t1
    print ('Scanning Completed in: ', timeElapsed)
