import sys
########## Display ####################################
Option=[("S","Split file")]
if len(sys.argv)==1 or sys.argv[1].lower()=="help":
	print "Usage:",sys.argv[0],"file_name","[Option]"
	print "Option:"
	for (option,description) in Option:
		print "\t"+option+"\t\t"+description  
	exit()
#######################################################
lib=[("PNG","89504e470d0a1a0a","49454e44ae426082","png"),
("RAR","526172211a0700","rar"),
("JPG","ffd8ffe0","ffd9","jpg"),
("PDF","25504446","2525454f46","pdf"),
("ZIP","504b0304","zip"),
("JAR","504b0304140008000800","jar"),
("PKZIP1","504b0506","zip"),
("PKZIP2","504b0708","zip"),
("GZIP","1f8b08","gz"),
("7Zip","377abcaf271c","7z"),
("Microsof Office","504b030414000600","504b0506","docx")]
try:
	f=open(sys.argv[1],"rb").read().encode("hex")
except IOError:
	print "File not found !!!"
	exit()
print "[+]File detected:"
for i in range(0,len(lib)):
	a=f.count(lib[i][1])
	if a!=0:
		print "   [-]"+lib[i][0]+": ",a,
		##### Check image Exif #########
		if (lib[i][0]=="PNG" or lib[i][0]=="JPG") and f.count("45786966")!=0:
			print "Exif("+str(f.count("45786966"))+")"
		else:
			print 
		################################
if len(sys.argv)>2:
	try:
		if(len(sys.argv[2])):
			if sys.argv[2].lower()=="s":
				for i in range(0,len(lib)):
					if(sys.argv[3].lower()==lib[i][0].lower()):
						type_file=lib[i][0]
						signal_file=lib[i][1]
						position=i
						break
				try:
					b=f.split(signal_file)
				except NameError:
					print "signal_file not found in library. Sorry !!!"
					exit()
				print "[+]Slpitting file:"
				######### File has trailer (Footer)#####
				if len(lib[position])>3:
					for i in range(1,len(b)):
						try:
							filename=type_file+"("+str(i)+")."+lib[position][3]
							print "\t[-]"+filename,
							filename=open(filename,"wb")
							filename.write((signal_file+b[i][0:b[i].index(lib[position][2])]+lib[position][2]).decode("hex"))
							filename.close()
						except TypeError:
							continue
				############################################
				######### File hasnt trailer (Footer) ######
				else:
					for i in range(1,len(b)):
						try:
							filename=type_file+"("+str(i)+")."+lib[position][2]
							print "\t[-]"+filename,
							filename=open(filename,"wb")
							filename.write(signal_file.decode("hex")+b[i].decode("hex"))
							filename.close()
						except TypeError:
							continue
				print "Done"
				#############################################3
			else:
				print "Usage:",sys.argv[0],"help ---> for details"

	except IndexError:
		print "Usage:",sys.argv[0],"help ---> for details"