

import glob

set_of_ip = set()

for current_file_name in glob.glob("C:\Users\Pancho\Google Диск\Обучение\python\my\p4ne\Lab1.5\config_files\*.txt"):
    with open(current_file_name) as f:
        for current_line in f:
            if current_line.find("ip address") == 1:
                set_of_ip.add(current_line.replace("ip address", "").strip())

for i in set_of_ip:
    print(i)
