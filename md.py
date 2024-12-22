import os
import time

#Function mounted
def mountDisk():
    os.system(f"sudo mkdir -p /run/media/maury/{diskSelected[2]}")
    os.system(f"sudo mount -t {diskSelected[1]} /dev/{diskSelected[0]} /run/media/maury/{diskSelected[2]}")

#Function dismounted 
def dismountDisk():
    os.system(f"sudo umount /run/media/maury/{diskSelected[2]}")
    os.system(f"sudo rm -rf /run/media/maury/{diskSelected[2]}")

while True:
#Query disks availables
    os.system("clear")
    os.system("cat ./banner")
    disks_available = os.popen("lsblk -f -l | grep 'sdb' | awk '{print $1,$2,$4,$8}' ").read()
    disks_available_aux = os.popen("lsblk -f -l | grep 'sdb' | awk '{if ($8 != \"\") $8=\"yes \"; else $8=\"no  \" ; print $8,$2,$4}' ").read() 
    
    disks_available=disks_available.split("\n")
    disks_available_aux=disks_available_aux.split("\n")
#Remove line empty
    disks_available.remove('')
    disks_available_aux.remove('') 
#List all disks availables
    i=1
    print("id: mnt  type label")
    print("-------------------")
    for disk in disks_available_aux:
        print(f"{i}   {disk}")
        i=i+1

#Read index of list
    optionList=input(">> ")
    if (optionList=="0"):
        exit()
    elif (optionList!=""):
#Separate items from the selected disk
        diskSelected=disks_available[int(optionList)-1].split(" ")

#Query of Disk is mount or dismount
        if ( diskSelected[3] == "" ):
            mountDisk()
            print(f"{diskSelected[2]} is mounted")
            time.sleep(3)
        else:
            dismountDisk()
            print(f"{diskSelected[2]} is dismounted")
            time.sleep(3)
    else:
        pass
 
