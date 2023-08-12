from collections import defaultdict
import subprocess
import ipaddress
import sys
max_hops=1
hop_limit=30
ip_address=sys.argv[1]
destination=""
address_found=defaultdict(lambda : [])
time=-1
while(True):
    command=f"ping -m {max_hops} {ip_address} -t 1"
    for i in range(3):
        out=subprocess.run(command, shell=True, capture_output=True)
        output=out.stdout.decode().split("\n")
        try:
            if(destination==""):
                destination=output[0].split(" ")[2][1:-2]
            current=output[1].split(" ")[3][:-1]
            command2=f"ping -c 1 {current}"
            out2=subprocesses.run(command2,shell=True,capture_output=True)
            output2=out2.stdout.decode().split("\n")
            time= output2[-1].split("\ ")[4]
            address_found[current].append(time)
        except:
            address_found["*"].append(-1)
    if address_found[0][0]=="*":
        print(f"{max_hops}: *")
    else:
        s=""
        for time in address_found[0][1]:
            s+=f"{time} "
        print(f"{max_hops}: {address_found[0][0]} " + s)
    for i in range(1,len(address_found)):
        if address_found[i][0]=="*":
            print(f"{max_hops}: *")        
        else:
            s=""
            for time in address_found[i][1]:
                s+=f"{time} "
            print(f"   {address_found[i][0]} " + s)
    if(current==destination):
        break
    max_hops+=1
    if(max_hops>hop_limit):
        break

# import subprocess
# import ipaddress
# import sys
# max_hops=1
# hop_limit=30
# ip_address=sys.argv[1]
# destination=""
# while(True):
#     command=f"ping -m {max_hops} {ip_address} -t 1"
#     out=subprocess.run(command, shell=True, capture_output=True)
#     output=out.stdout.decode().split("\n")
#     try:
#         if(destination==""):
#             destination=output[0].split(" ")[2][1:-2]
#         current=output[1].split(" ")[3][:-1]
#         # ipaddress.ip_address(current)
#         print(f"{max_hops}: {current}")
#         if(current==destination):
#             break
#     except:
#         print(f"{max_hops}: *")
#     max_hops+=1
#     if(max_hops>hop_limit):
#         break
