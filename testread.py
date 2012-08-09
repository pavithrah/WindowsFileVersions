import os, os.path
import re
import sys


linenew = ["os,sp,arch,file,minver,fixver,dir,bulletin,kb"]
#newlines= ["os","sp","arch","file","minver","fixver","dir","bulletin","kb"]
newlines=[]
newline=["","","","","","","","",""]
print "os,sp,arch,file,minver,fixver,dir,bulletin,kb"

f_read = open('hotfix_list.txt', 'r')
if f_read != None:
    lines = f_read.readlines();
    for line in lines:
        if line == None:
            continue;
        line.replace("\n", "")
        ind = line.find("hotfix_is_vulnerable(")
        if ind != -1:
            line = line[ind+21:]

        ind1 = line.find("hotfix_is_vulnerable (")
        if ind1 != -1:
            line = line[ind1+22:]

        line = line.replace(")", "")
        line = line.replace("|", "")
        line = line.replace('"', "")
        line = line.replace(' ', "")
        line = line.replace('\n', "")
        
        line = line.split(",")
        for item in line:
            if item.startswith("os:"):
                newline[0] = item[item.find("os:")+3:]
            elif item.startswith("sp:"):
                newline[1] = item[item.find("sp:")+3:]
            elif item.startswith("arch:"):
                newline[2] = item[item.find("arch:")+5:]
            elif item.startswith("file:"):
                newline[3] = item[item.find("file:")+5:]
            elif item.startswith("min_version:"):
                newline[4] = item[item.find("min_version:")+12:]
            elif item.startswith("version:"):
                newline[5] = item[item.find("version:")+8:]
            elif item.startswith("dir:"):
                newline[6] = item[item.find("dir:")+4:]
            elif item.startswith("bulletin:"):
                newline[7] = item[item.find("bulletin:")+9:]
            elif item.startswith("kb:"):
                newline[8] = item[item.find("kb:")+3:]
            ##elif item.startswith("path:"):
             ##   newline[6] = item[5] + item[item.find("path:")+5:]
            else:
                continue                

        #print newline  
        #newlines.append(newline)        
        print "%s,%s,%s,%s,%s,%s,%s,%s,%s" %(newline[0],newline[1],newline[2],newline[3],newline[4],newline[5],newline[6],newline[7],newline[8])
        
f_read.close()
    


