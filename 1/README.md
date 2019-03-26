## ECE-303 Project-1 TCP Port Scanner
### Jing Jiang

<hr />

This is the instruction for the first project assigment of ECE 303 Comm Nets Spring 2019.
The goal is to develop a program that will scan a port range on a specific set of target hosts and will
return the open ports. In addition, if a protocol’s default port lies within the port range, list the name of
the protocol.

How to run the program:
```
python port_scanner_JingJiang.py hostname [-p starting_port ending_port]
```
the starting and ending ports can also be separated by a colon ":":
```
[-p starting_port:ending_port]
```

If the -p argument is not specified. The program will use 20 as starting port and 1025 as ending port.