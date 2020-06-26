f=open("binary file.txt","w")
f.write("I Love letsupgrade")
f.close()
f=open("binary file.txt","r")
print(f.read())
f.close()
f=open("binary file.txt","a")
f.write("\n\nWe All love to learn python with UL")
f.close()
f=open("binary file.txt","r")
print(f.read())
f.close()



