#import librarys
import os
from simple_term_menu import TerminalMenu
import time

#Function mounted
def mountDisk():
    os.system(f"sudo mkdir -p /run/media/maury/{disk_select[2]}")
    os.system(f"sudo mount -t {disk_select[1]} /dev/{disk_select[0]} /run/media/maury/{disk_select[2]}")

def main():
#Function mounted
    def mountDisk():
        os.system(f"sudo mkdir -p /run/media/maury/{disk_select[2]}")
        os.system(f"sudo mount -t {disk_select[1]} /dev/{disk_select[0]} /run/media/maury/{disk_select[2]}")

#Function dismounted 
    def dismountDisk():
        os.system(f"sudo umount /run/media/maury/{disk_select[2]}")
        os.system(f"sudo rm -rf /run/media/maury/{disk_select[2]}")

    #Clear display and view banner,options
    os.system("clear && cat ./banner")
    print("[+]mounted   [-]umounted \n")
    #List disk
    disks = os.popen("lsblk -f -l | grep -E 'sdb|sdb[0-9]|sdc|sdc[0-9]' | awk '{var=\"\";if ($8 != \"\") var=\"+\"; else var=\"-\" ; print \"[\"var\"]\"$4,\"-\",$1,\"-\",$2}' ").read().strip().split("\n")
    disks_available = os.popen("lsblk -f -l | grep -E 'sdb|sdb[0-9]|sdc|sdc[0-9]' | awk '{print $1,$2,$4,$8}' ").read().split("\n") 
    disks.append("Exit")
    try:
        terminal_menu = TerminalMenu(disks)
        index = terminal_menu.show()
        if ( index == len(disks)-1 ):
            os.system("clear")
            exit()
        disk_select=disks_available[index]
        disk_select=disk_select.split(" ")
        if ( disk_select[3] == "" ):
            mountDisk()
            print("> Just a minute!") 
            time.sleep(0.5)
            print(f">> {disk_select[2]} is mounted!!!")
            time.sleep(1.5)
        else:
            dismountDisk()
            print("> Just a minute!")
            time.sleep(0.5)
            print(">> It is safe \n   to disconnect the storage drive...")
            time.sleep(1.5)
 
        time.sleep(3)
    except AssertionError as e:
        #Exception for no found disks
        os.system("clear")
        print("No valid disks availables found.")
        exit()
 
while True:
    if __name__ == "__main__":
        main()
