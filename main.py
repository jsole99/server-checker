import re

print("JDS Service Checker 1.0 Running...")
print("Please select an option:")
print("1. Check Server Status")
print("2. Add New Server")
print("3. Remove Server")
print("4. Exit")
menuSelection = input("Selection: ")

if menuSelection == "1":
    serverIP = input("Enter Server IP or DNS: ")
    print("Checking status of " + serverIP + "...")
    #check if the input follows an ip strucutre
    x = re.search(r"([\d]+\.[\d]+\.[\d]+\.[\d+]+)", serverIP)
    print(x)
    #check if the input follows a dns structure
    #if the input is neither an IP nor DNS - throw error
    #else we will start to check the status of the server


if menuSelection == "2":
    newServerIP = input("IP Address of New Server: ")

if menuSelection == "3":
    print("Feature not implemented yet.")
    skip = input("Press Enter to Continue...")
    # first print list of servers denoted by number, ip, dns if applicable, ask for server number