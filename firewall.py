# In this program, you have been provided with a file containging IP addresses.
# Your task is to complete two functions below, firewall and read_ips.
# reasd_ips function reads IPs fropm the file provided, ips. txt line by line and
# returns a list of all the IPs. Thos IPs are then passed one by one to function
# firewall, which has to make a decision to either block the IP or let it pass.
# The rule is to block the IP if the third octet of
# IP address is between 50 and 100 inclusive. Else let the IP pass.
# ex. 213.207.52.20 -> blocked
# ex 212.58.102.205 -> pass

def firewall(ip):
    temp_ip = []
    temp_ip = ip.split(".") 
    if (int(temp_ip[2]) >= 50 and int(temp_ip[2]) <= 100):
        #print(ip, " -> ",  "Blocked")
        return "Blocked"
    else:
        #print(temp_ip, " ->  Pass")
        return "Pass"

def read_ips(f):
    ips = []
    for val in f:
        ips.append(f.readline())
    return ips

if __name__ == '__main__':
    f = open(".\ips.txt", "r")
    ips = read_ips(f)
    for ip in ips:
        print('{:20} -> {}'.format(ip, firewall(ip)))