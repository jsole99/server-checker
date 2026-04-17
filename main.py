import re
import os

## need to get menu function working
def menu():
    menu_list = ["Check Server Status", "Add New Server", "Remove Server", "Exit"]
    # iterates menu
    for i in menu_list:
        print(str(menu_list.index(i) + 1) + ". " + i)



def menuSelectionLogic():
    menuValue = input("Selection: ")
    #returns data captures and stored in menuSelection
    match int(menuValue):
        case 1:
            print("Menu Option 1 Selected")
            selection = 1
        case 2:
            print("Menu Option 2 Selected")
            selection = 2
        case 3:
            print("Menu Option 3 Selected")
            selection = 3
        case 4:
            selection = 0
    return selection

def main():
    running = 1
    while running != 0:
        print("JDS Service Checker 1.0 Running...")
        menu()
        running = menuSelectionLogic()
    return 0


if __name__ == "__main__":
    main()
    exit()





#  if menuSelection == "1":
#         # Can probably break this out into it's own function after completed
#         x = None
#         while x is None:
#             serverIP = input("Enter Server IP or Domain: ")
#             print("Checking status of " + serverIP + "...")
#             #check if the input follows an ip strucutre
#             x = re.search(r"([\d]+\.[\d]+\.[\d]+\.[\d+]+)", serverIP)
#                 # check if the user does NOT input a valid IP address
#             if x == None:
#                 print("not a valid ip")
#             # need to re-load logic at this point
#         # start to scan IP
#         else:
#             print(os.system("ping " + serverIP))
            
            

        
#         #check if the input follows a dns structure
#         #if the input is neither an IP nor DNS - throw error
#         #else we will start to check the status of the server


#     if menuSelection == "2":
#         newServerIP = input("IP Address of New Server: ")
#         #validate ip address

#     if menuSelection == "3":
#         print("Feature not implemented yet.")
#         skip = input("Press Enter to Continue...")
#         # first print list of servers denoted by number, ip, dns if applicable, ask for server number
