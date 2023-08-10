import subprocess
import ipaddress
import sys
max_hops=1
hop_limit=30
ip_address=sys.argv[1]
destination=""
while(True):
    command=f"ping -m {max_hops} {ip_address} -t 1"
    out=subprocess.run(command, shell=True, capture_output=True)
    output=out.stdout.decode().split("\n")
    try:
        if(destination==""):
            destination=output[0].split(" ")[2][1:-2]
        current=output[1].split(" ")[3][:-1]
        # ipaddress.ip_address(current)
        print(f"{max_hops}: {current}")
        if(current==destination):
            break
    except:
        print(f"{max_hops}: *")
    max_hops+=1
    if(max_hops>hop_limit):
        break