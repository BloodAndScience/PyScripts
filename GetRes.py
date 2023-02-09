import os
 
 
Direc = "./res"
 
files = os.listdir(Direc)
files = [f for f in files if os.path.isfile(Direc+'/'+f)] #Filtering only the files.

for f in files:

    print("## "+ f +"\n")
    print(" ")
    print("!["+f+"]("+"./res/"+f+")"+"\n")
    print(" ")

#print(*files, sep="\n")
