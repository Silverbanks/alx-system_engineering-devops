0x13. Firewall

fire_wall

A firewall is a network security device that monitors incoming and outgoing network traffic and permits or blocks data packets based on a set of security rules. Its purpose is to establish a barrier between your internal network (LAN) and incoming traffic from external sources (such as the internet) in order to block malicious traffic like viruses and hackers.

The UFW On Linux Distro
Uncomplicated Firewall

The Uncomplicated firewall (UFW) in my ubuntu 22.04 LTS comes preinstalled but disabled, i only needed to enable it to get going. However lets take note of the following:

Once UFW is enabled you have to set the rules on that terminal session especially when you're connecting via ssh cause by default ufw blocks all connection to port 22.
UFW doesn't have a native port forwarding command, you need to do it via its /etc/ufw/before.rules file
You also need to enable port forwarding by uncommenting the net.ipv4.ip_forward=1 line in /etc/sysctl.conf

