#!/usr/bin/python3

import subprocess
import argparse
import os
import glob

subprocess.call(["yum install autofs -y"])

#add a check to see if autofs is already installed

#watch /etc for new files instead of removing all auto.* files

parser = argparse.ArgumentParser()
parser.add_argument('--install', help='Install autofs and start the setup',action="store_true")
parser.add_argument('--revert', help='Revert the complete installation and remove /etc/auto.* files',action="store_true")
args = parser.parse_args()

if args.install:

   mount_name = input("Mount name: ")
   ip = input("CIFS IP: ")
   remote_path = input("Remote share: ")
   local_path = input("Local path: ")
   ad_username = input("AD username: ")
   ad_password = input("AD password: ")
   user_id = input("User ID: ")

   f = open("auto." + mount_name ,'w')
   f.write(mount_name + " -fstype=cifs,username=" + ad_username + ",password=" + ad_password + ",uid=" + user_id + " ://" + ip + remote_path)
   f.close()

   f = open('auto.master','a')
   f.write(local_path + " /etc/auto." + mount_name + " --timeout 60")
   f.close()

if args.revert:
   print("Removing autofs package and deleting all auto.* files in /etc")
   subrpocess.call(["yum remove autofs -y"])
   for auto in glob.glob("/etc/auto.*"):
   os.remove(auto)

else:
   print("Installation and setup failed, please try again manually or use --revert to remove anything that was setup")

