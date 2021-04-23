

import glob

ips = set()

for file_name in glob.glob("C:\\Users\\Pancho\\Google Диск\\Обучение\\python\\my\\p4ne\\Lab1.5\\config_files\\*.txt"):
    with open(file_name) as f:
        for line in f:
            if line.find("ip address") is 1:
                ips.add(line.replace("ip address", ""), s)

for i in ips:
    print(i)
