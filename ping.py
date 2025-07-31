import os
ip_list=input()
ip_input=ip_list.split(",")
def ping_ip(ip):
    if not ip:
          print("no it isnot be specified")
          return 
    response=os.system(f"ping -n 1 {ip}>nul")
    if response==0:print(f"{ip} is up✔️")
    else:print("Down")
for ip in ip_input: 
    ping_ip(ip)