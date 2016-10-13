# -*- coding: utf-8 -*-

from time import strftime, gmtime

def writeMenuOnFile(filePath):
     with open(filePath, "a+") as file:
         file.write(strftime("%d.%m.%Y %H:%M:%S", gmtime()))
         file.write("\n")
         while True:
             food = raw_input("Insert food: ")
             price = raw_input("Insert price in EUR: ")
             file.write(food)
             file.write(": ")
             file.write(price)
             file.write("\n")
             another = raw_input("Would you like to enter new task? (yes/no): ")
             if another == "no":
                 break
         file.write("\n\n")

if __name__ == "__main__":
    writeMenuOnFile("menu.txt")
