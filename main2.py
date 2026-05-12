
import os


###
#f = open("myfile.txt", "rb")
#if not os.path.exists("myfile2.txt"):
 #g = open("myfile2.txt", "x")
 
 
 
#print(f.read())
#f.close()###


#f = open ( "myfile2.txt", "w")
#f.write("This is my file")
#f.close()



#f = open ( "myfile2.txt", "a")
#f.write("This is my file")
#f.close()


#with open("myfile2.txt", "a") as f:
    
#    f.write("\nnew appeded lines ")


#f = open("myfile2.txt", "r")
#while True:
#    line = f.readline()
#    if not line :
#        break 
#    print(line)
#f.close()

#f = open ("marks.txt", "r")
#i = 0 
#while True :
#    i +=1
#    line = f.readline()  
#    if not line :
#        break
#    
#    m1 = int(line.split(",")[0])         
#    
#    m2 =int(line.split(",")[1])   
#     
#    m3 = int(line.split(",")[2])  
#    
#    
#    print(f"Marks of student {i} are {m1*5}")
#    print(f"Marks of student {i} are  {m2}")
#    print(f"Marks of student {i} are  {m3}")
#    print(line)
#f.close()
    
    
#f = open("marks2.txt", "w")
#lines =  ["10,20,30\n", "40,50,60\n", "70,80,90\n"]
#f.writelines(lines)
#f.close()
#

f = open("marks2.txt", "w")
lines = ["10,30", "40,50,60", "70,80,90"]

for i in lines:
    f.write(i + "\n")
f.close()

