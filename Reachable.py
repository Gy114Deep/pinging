import subprocess
import platform
def check_ip(ip):   # for Window ping command is'-n',for mac/linux '-c'
    ip_ping="-n" if platform.system().lower()=="windows" else "-c"
    result=subprocess.run(["ping",ip_ping,"1",ip],timeout=3,text=True,capture_output=True)
    if result.returncode==0:
        return "reachable"
    else: return "unreachable"
# print(check_ip("8.8.8.8"))    or
ip_input=input("Your ip address is - ").split(",")
for ip in ip_input:
    print(check_ip(ip))
