#created by Amit Khurana
import os
import random
print("Enter the full address of location from where you want to host the server")
loc = input()
os.chdir(loc)
r = random.randint(10000,20000)
print("Your server has been started .... Write your Ip Address:{}".format(r) + " in your browser's url")
os.system("python -m http.server {}".format(r))
print("Your server has been started")


