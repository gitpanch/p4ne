

import re
import glob
from ipaddress import IPv4Interface

def classify(s):


    m = re.match("^ ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", s)
    if m:
        return {"ip":IPv4Interface(str(m.group(1)) + "/" + str(m.group(2)))}

    m = re.match("^interface (.+)", s)
    if m:
        return {"int":m.group(1)}

    m = re.match("^hostname (.+)", s)
    if m:
        return {"host":m.group(1)}

    return ("UNCLASSIFIED",)

ip_addresses = []
interfaces = []
hosts = []

for current_file_name in glob.glob("C:\\Users\\Pancho\\Google Диск\\Обучение\\python\\my\\p4ne\\Lab1.5\\config_files\\*.txt"):
    with open(current_file_name) as f:
        for current_line in f:
            c = classify(current_line)
            if "ip" in c:
                ip_addresses.append(c)
            if "int" in c:
                interfaces.append(c)
            if "host" in c:
                hosts.append(c)

print(ip_addresses)
print(interfaces)
print(hosts)
