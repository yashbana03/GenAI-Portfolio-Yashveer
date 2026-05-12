
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


with open("myfile2.txt", "a") as f:
    
    f.write("\nnew appeded lines ")