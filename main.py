
def aws():
	import os
	import time
	os.system("clear")
	os.system("tput smso 5")
	os.system("tput setaf 3")
	print("\n\n\t\t\t  WELCOME TO THE AWS MENU  ")
	os.system("tput sgr 0 ")
	while True:
	
		os.system("tput setaf 4")
		#os.system("tput smul 4")
		print("""
		\n
		Press 1 : To configure AWS
		Press 2 : To create a key-pair
		Press 3 : To create a security-group
		Press 4 : To launch an instance
		Press 5 : To start an instance
		Press 6 : To stop an instance
		Press 7 : To create an EBS volume of 1 GB.
		Press 8 : To create an S3 bucket
		Press 9 : To upload an image in bucket
		Press 10 : To create Cloudfront Distribution
		press 11 : To create Snapshot
		press 12 : TO back main menu
		press 13 : Close the program
	
		""")
		os.system("tput sgr0")
		os.system("tput bold 4")
		os.system("tput setaf 4")
		ch = input("Enter your choice : ")

		#print("\nYour choice is {}".format(ch))
	
		if int(ch) == 1:
		    os.system("tput sgr0")
		    os.system("tput setaf 3")
		    os.system("tput bold 3")
		    os.system('aws configure')
    
		elif int(ch) ==2:
		    os.system("tput sgr0")
		    os.system("tput setaf 13")
		    os.system("tput bold 13")
		    keyname = input("\nEnter the keyname :- ")
		    os.system('aws ec2 create-key-pair --key-name {}'.format(keyname))
    
		elif int(ch) ==3:
		    os.system("tput sgr0")
		    os.system("tput setaf 11")
		    os.system("tput bold 11")	    
		    description = input("\nEnter The Description :-")
		    group_name = input("\nEnter The Group Name :-")
		    os.system('aws ec2 create-security-group --description {} --group-name {}'.format(description, group_name ))
   
		elif int(ch) ==4:
		    os.system("tput sgr0")
		    os.system("tput setaf 10")
		    os.system("tput bold 10")
		    imageid =input("\nEnter the image id :- ")
		    securityid = input("\nEnter the security group id :-")
		    keyname = input("\nEnter the keyname :-")
		    os.system('aws ec2 run-instances --image-id {} --instance-type t2.micro --security-group-ids {} --key-name {}'.format(imageid, securityid ,keyname))


		elif int(ch) ==5:
		    os.system("tput sgr0")
		    os.system("tput setaf 9")
		    os.system("tput bold 9")
		    instanceid = input("\nEnter your instance-id :-")
		    os.system('aws ec2 start-instances --instance-ids {}'.format(instanceid))
   

		elif int(ch) ==6:
		    os.system("tput sgr0")
		    os.system("tput setaf 11")
		    os.system("tput bold 11")
		    instanceid = input("\nEnter your instance-id :-")
		    os.system('aws ec2 stop-instances --instance-ids {}'.format(instanceid))

		elif int(ch) ==7:
		    print("Select the Availabilty Zones ")
		    print("""
		        \n
		        Press 1 : ap-south-1a
		        Press 2 : ap-south-1b
		        Press 3 : ap-south-1c
		        """)
		    s = input("\nSelect Availability Zone :-")
		    if int(s) == 1:
		        az = "ap-south-1a"
		        os.system("aws ec2 create-volume --volume-type gp2 --size 1 --availability-zone ap-south-1a")
		    elif int(s) == 2:
		        az = "ap-south-1b"
		        os.system("aws ec2 create-volume --volume-type gp2 --size 1 --availability-zone ap-south-1b")

		    elif int(s) == 3:
		        az = "ap-south-1c"
		        os.system("aws ec2 create-volume --volume-type gp2 --size 1 --availability-zone ap-south-1c")


		elif int(ch) ==8:
		    os.system("tput sgr0")
		    os.system("tput setaf 13")
		    os.system("tput bold 13")
		    bname = input("\nEnter the bucket name :-")
		    region = input("\nEnter the region :-")
		    os.system('aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint=ap-south-1'.format(bname, region))
	
		elif int(ch) ==9:
		    os.system("tput sgr0")
		    os.system("tput setaf 14")
		    os.system("tput bold 14")
		    bname = input("\nEnter your bucket name :-")
		    location = input("\nEnter the loaction of image :-")
		    iname = input("\nEnter image name :-")
		    os.system('aws s3api put-object --bucket {} --body {} --key {}'.format(bname, location, iname))

		elif int(ch) ==10:
		    os.system("tput sgr0")
		    os.system("tput setaf 11")
		    os.system("tput bold 11")
		    domain_name = input("\nEnter the Domain name :-")
		    iname = input("\nEnter the image name :-")
		    os.system('aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object {}'.format(domain_name,iname))

		elif int(ch) ==11:
		    vd =input("Enter the volume id :- ")
		    desc =input("Enter the description :- ")
		    os.system("aws ec2 create-snapshot --volume-id {} --description {}".format(vd,desc))

		elif int(ch) ==12:
		    break

		elif int(ch) ==13:
		    print("BYE BYE ...")
		    time.sleep(2)
		    exit()

		else :
		    os.system("tput setaf 9")
		    print("\n\tIt is not in the menu")
		    os.system("tput setaf 5")
		    print("\n\t Renter Your Choice")
		    os.system("tput setaf 7")



def linux():

	import os
	import time
	os.system("clear")
	os.system("tput smso 5")
	os.system("tput bold 4")
	os.system("tput setaf 4")
	print("\n\n\t\t\t  WELCOME TO THE LINUX & PARTITION MENU  ")
	os.system("tput sgr 0 ")
		
	while True:

		os.system("tput setaf 3")
		print("\n1.Press 1 : Run Linux Command")
		print("2.Press 2 : Create Partition")
		print("3.Press 3 : Create LVM")
		print("4.Press 4 : Check mounted disk")
		print("5.Press 5 : Volume Group List")
		print("6.Press 6 : Yum Configure")
		print("7.Press 7 : Back to main menu")
		print("8.Press 8 : Close the program")

		os.system("tput setaf 5")
		a=input("\nEnter your choice -  ")

		if a=="1":
			while True:
				os.system("tput setaf 6")
				command=input("\nInput the command :- ")
				os.system("tput setaf 7")
				os.system(command)
				os.system("tput setaf 2")
				#command=input("\nDo you want to run more command Y/N:- ")
				if (command=="exit"): #or (z=="Exit") or (z=="EXIT") or (z=="Y")or(z=="y"):
					break
				#elif (z=="no") or (z=="NO") or (z=="N") or (z=="n"):
				#
				#	break
										
			
		


		elif a=="2":
			os.system("tput setaf 7")
			os.system("fdisk -l")
			os.system("tput setaf 3")
			b=input("\tEnter disk name:-")
			os.system("fdisk {}".format(b))
			time.sleep(2)
		
			os.system("tput setaf 3")
			print("\n\nFormatting the Partition")
			os.system("mkfs.ext4 {}".format(b))
			os.system("tput setaf 2")
			print("Successfully Formatted")
			time.sleep(2)

			os.system("tput setaf 3")	
			d=input("\n\n Make Directory for mounting:-")
			os.system("mkdir /{}".format(d))
			os.system("tput setaf 2")
			print("Directory successfully Created")
			time.sleep(2)
		
			os.system("\n\nfdisk -l")
			os.system("tput setaf 3")
			m=input("\t Mount The Directory, Please enter the disk name ")
			os.system("mount {} {} ".format(m,d))
			os.system("tput setaf 2")
			print("successfully Mounted")
			time.sleep(2)

		elif a=="3":
			os.system("\n\nfdisk -l")
			os.system("tput setaf 3")
			print("Enter the both disks name :-")
			i=input("pvcreate ")
			j=input("pvcreate ")
			os.system("pvcreate {} {}".format(i,j))
			os.system("tput setaf 2")
			print("Successfully pv created")
			time.sleep(2)
			
			os.system("tput setaf 3")
			print("\n\nCreate volume group")
			l=input("Give me group name :-")
			os.system("vgcreate {} {} {}".format(l,i,j))
			os.system("tput setaf 2")
			print("Successfully volume group created")
			time.sleep(2)
				
			os.system("tput setaf 3")
			print("\n\nSet the Size of lv")
			n=input("Size(in GB) -  ")
			o=input("Set Name -")
			os.system("lvcreate --size {}GB --name {} {}".format(n,o,l))
			os.system("tput setaf 2")
			print("Successfully lv created")
			time.sleep(2)
			
			os.system("tput setaf 3")		
			print("\n\nFormat the lv")
			os.system("mkfs.ext4 /dev/{}/{}".format(l,o))
			os.system("tput setaf 2")
			print("Successfully Formatted")
			time.sleep(2)

			print("\n\nBefore the mounting please create Directory")
			p=input("mkdir ")
			os.system("mkdir {}".format(p))
			os.system("tput setaf 2")
			print("Directory created")
			time.sleep(2)

			print("\n\nMount your Directory")
			os.system("mount /dev/{}/{} /{}".format(l,o,p))
			os.system("tput setaf 2")
			print("Successfully Mounted please check with df -h command ")
			print("\n Back to the menu")
			os.system("tput setaf 7")

		elif a=="4":
			os.system("df -h")

		elif a=="5":
			os.system("vgdisplay")

		elif a=="6":
			os.system("yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")

		elif a=="7":
			break

		elif a=="8":
			os.system("tput setaf 7")
			print("BYE BYE..")
			time.sleep(2)
			exit()

		else:
			input("You have entered wrong keyword")
			continue
			


	
								
		
		
		





def web():

	from os import system
	import subprocess as sp
	from time import sleep
	system("clear")
	os.system("tput smso 5")
	os.system("tput bold 4")
	os.system("tput setaf 4")
	print("\t\t WELCOME TO THE WEB SERVER CONFIGURATION MENU\n")
	
	while True :
	   
	    os.system("tput sgr0")
	    system("tput setaf 6")
	    print("\n\n1. Press 1 to install Apache Web Server Software")
	    print("2. Press 2 To Create Web Pages")
	    print("3. Press 3 To Start Services")
	    print("4. Press 4 To Stop Services")
	    print("5. Press 5 TO Back Main Menu")
	    print("6. Press 6 Close The Program")

	    system("tput setaf 3")
	    ch = int(input("\nEnter your choice : "))

	    if ch==1 : 
	        x = sp.getstatusoutput("rpm -q httpd")
	        if x[0] != 0 :
	            system("yum install httpd")
	            sleep(2)
	        else : 
	            system("tput setaf 2")
	            print("\nAlready installed ")
	            sleep(2)

	    elif ch==2 :
	        system("tput setaf 3")
	        page = input("\nEnter name of html page (with.html extension) : ")
	        system(f"vim /var/www/html/{page}")
	        system("tput setaf 2")
	        print("\nWeb Page created successfully")
	        sleep(2)

	    elif ch==3 :
	        system("tput setaf 2")
	        system("systemctl start httpd")
	        print("\nYour service has been started")
	        sleep(2)

	    elif ch==4 :
	        system("tput setaf 2")
	        system("systemctl stop httpd")
	        print("\nYour service has been stopped")
	        sleep(2)

	    elif ch==5 :
	        break

	    elif ch==6 :
	     	system("tput setaf 3")
	     	print("BYE BYE....🙏")
	     	system("tput sgr0")
	     	exit()
	     	
	        

	    else :
	        system("tput setaf 1")
	        print("\nWrong Choice\nTry again")
	        sleep(2)



def hadoop():

	from os import system 
	from time import sleep
	system("clear")
	os.system("tput smso 5")
	os.system("tput bold 5")
	os.system("tput setaf 5")
	print("\t\t WELCOME TO MY MENU\n")

	while True :    
	    #system("clear")
	    #system("tput setaf 3")
	    #print("----------------------".center(80))
	    #print("!!Welcome to My Menu!!".center(80))
	    #print("----------------------".center(80))

# Menu options
	    system("tput sgr0")
	    system("tput smul 6")
	    system("tput setaf 6")
	    print("1. Press 1 to work locally")
	    print("2. Press 2 to work remotely")
	    print("3. Press 3 to back main menu")
	    print("4. Press 4 to exit")
	    system("tput sgr0")
	    system("tput setaf 5")
	    ch = int(input("\nEnter your choice : "))
	    system("tput setaf 6")

	    if ch==2 :
	        system("tput setaf 5")
	        ip = input("Enter IP address of remote system : ")
	        system("tput setaf 7")
	        system(f"ssh {ip}")
        
	    elif ch==1 :
	        while True :
	            system("clear")
	            #system("tput setaf 3")
	            system("tput smso 5")
	            system("tput bold 5")
	            system("tput setaf 5")
	            print("\t\t------Hadoop Menu------")
	            system("tput sgr0")
	            system("tput setaf 6")
	            print("\n1. Press 1 to setup NameNode")
	            print("2. Press 2 to setup DataNode")
	            print("3. Press 3 to return to main menu")
	            print("4. Press 4 to Exit the program")
	            system("tput sgr0")
	            system("tput setaf 3")
	            hdp = int(input("\nEnter your choice : "))
	            system("tput setaf 6")

	            if hdp==1 : 
	                while True :
	                    system("clear")
	                    #system("tput setaf 3")
	                    system("tput smso 5")
	                    system("tput bold 5")
	                    system("tput setaf 5")
	
	                    print("------NameNode Menu------\n")
	                    system("tput sgr0")
	                    system("tput setaf 6")
	                    print("1.  Press 1 to open hdfs-site.xml file")
	                    print("2.  Press 2 to open core-site.xml file")
	                    print("3.  Press 3 to start services of NameNode")
	                    print("4.  Press 4 to stop NameNode")
	                    print("5.  Press 5 to check report")
	                    print("6.  Press 6 to upload an empty file")
	                    print("7.  Press 7 to create and upload a file")
	                    print("8.  Press 8 to remove a file")
	                    print("9.  Press 9 to read a file")
	                    print("10. Press 10 to see all files")
	                    print("11. Press 11 to save file to local system")
	                    print("12. Press 12 to start safemode")
	                    print("13. Press 13 to stop safemode")
	                    print("14. Press 14 to go back to menu")
	                    print("15. Press 15 to Exit the program")
	                    system("tput setaf 5")
	                    ch = int(input("\nEnter your choice : "))
	                    if ch==1 : 
	                        system("tput setaf 4")
	                        dirNN = input("Create folder for NameNode : ")
	                        system(f"mkdir {dirNN}")
	                        system("tput setaf 3")
	                        print("Opening hdfs-site.xml file...")
	                        sleep(1)
	                        system("vim /etc/hadoop/hdfs-site.xml")
	                        system("tput setaf 2")
	                        print("hdfs-site.xml file successfully modified")
	                        system("hadoop namenode -format")
	                        sleep(2)
	                    elif ch==2 :
	                        system("vim /etc/hadoop/core-site.xml")
	                        system("tput setaf 2")
	                        print("core-site.xml file successfully modified")
	                        sleep(2)
	                    elif ch==3 :
	                        system("tput setaf 3")
	                        system("hadoop-daemon.sh start namenode")
	                        system("tput setaf 2")
	                        system("jps")
	                        print("Namenode started successfully :-)")
	                        sleep(2)
	                    elif ch == 4 :
	                        system("tput setaf 2")
	                        system("hadoop-daemon.sh stop namenode")
	                        sleep(2)
	                    elif ch==5 :
	                        system("tput setaf 2")
	                        system("hadoop dfsadmin -report")
	                        input("...")
	                    elif ch==6 :
	                        system("tput setaf 5")
	                        fname = input("File name : ")
	                        system(f"hadoop fs -touchz /{fname}")
	                        system("tput setaf 2")
	                        print("File ceated successfully")
	                        input("...")
	                    elif ch==7 :
	                        system("tput setaf 5")
	                        fname = input("File name : ")
	                        print("Write in file :")
	                        system("tput setaf 7")
	                        system(f"cat > {fname}")
	                        system(f"hadoop fs -put {fname} /")
	                        system("tput setaf 2")
	                        print("File uploaded successfully")
	                        input("...")
	                    elif ch==8 :
	                        system("tput setaf 5")
	                        fname = input("File name : ")
	                        system("tput setaf 1")
	                        system(f"hadoop fs -rm /{fname}")
	                        input("...")
	                    elif ch==9 : 
	                        system("tput setaf 5")
	                        fname = input("File name : ")
	                        system("tput setaf 7")
	                        system(f"hadoop fs -cat /{fname}")
	                        input("...")
	                    elif ch==10 :
	                        system("tput setaf 4")
	                        system("hadoop fs -ls /")
	                        input("...")
	                    elif ch==11 :
	                        system("tput setaf 4")
	                        src = input("Enter the name of file you want to copy : ")
	                        dest = input("Enter location where you want to save the file : ")
	                        system(f"hadoop fs -copyToLocal /{src} {dest}")
	                        system("tput setaf 2")
	                        print("File copied successfully")
	                        sleep(2)
	                    elif ch==12 :
	                        system("tput setaf 2")
	                        system("hadoop dfsadmin -safemode get")
	                    elif ch==13 :
	                        system("tput setaf 2")
	                        system("hadoop dfsadmin -safemode leave")
	                    elif ch==14 :
	                        break
	                    elif ch==15 :
	                        system("tput setaf 3")
	                        print("Bye...")
	                        system("tput setaf 7")
	                        exit()
	                    else :
	                        system("tput setaf 1")
	                        print("Wrong choice/n")
	                        #input("...")
	                        sleep(2)

	            elif hdp==2 : 
	                while True :
	                    system("clear")
	                    system("tput sgr0")
	                    system("tput setaf 3")
	                    print("------DataNode Menu------\n")
	                    system("tput setaf 6")
	                    print("1.  Press 1 to open hdfs-site.xml file")
	                    print("2.  Press 2 to open core-site.xml file")
	                    print("3.  Press 3 to start services of DataNode")
	                    print("4.  Press 4 to stop DataNode")
	                    print("5.  Press 5 to check report")
	                    print("6.  Press 6 to upload an empty file")
	                    print("7.  Press 7 to create and upload a file")
	                    print("8.  Press 8 to remove a file")
	                    print("9.  Press 9 to read a file")
	                    print("10. Press 10 to see all files")
	                    print("11. Press 11 to go back to Main menu")
	                    print("12. Press 12 to Exit the program\n")
	                    system("tput setaf 5")
	                    ch = int(input("Enter your choice : "))
	                    if ch==1 : 
	                        system("tput setaf 5")
	                        dirDN = input("Create folder for DataNode : ")
	                        system(f"mkdir {dirDN}")
	                        system("tput setaf 3")
	                        print("Opening hdfs-site.xml file...")
	                        sleep(1)
	                        system("vim /etc/hadoop/hdfs-site.xml")
	                        system("tput setaf 2")
	                        print("hdfs-site.xml file successfully modified")
	                        sleep(2)
	                    elif ch==2 :
	                        system("vim /etc/hadoop/core-site.xml")
	                        system("tput setaf 2")
	                        print("core-site.xml file successfully modified")
	                        sleep(2)
	                    elif ch==3 :
	                        system("tput setaf 3")
	                        system("hadoop-daemon.sh start datanode")
	                        system("tput setaf 2")
	                        system("jps")
	                        print("DataNode started successfully :-)")
	                        sleep(2)
	                    elif ch == 4 :
	                        system("tput setaf 2")
	                        system("hadoop-daemon.sh stop datanode")
	                        sleep(2)
	                    elif ch==5 :
	                        system("tput setaf 2")
	                        system("hadoop dfsadmin -report")
	                        input("...")
	                    elif ch==6 :
	                        system("tput setaf 5")
	                        fname = input("File name : ")
	                        system(f"hadoop fs -touchz /{fname}")
	                        system("tput setaf 2")
	                        print("File ceated successfully")
	                        input("...")
	                    elif ch==7 :
	                        system("tput setaf 5")
	                        fname = input("File name : ")
	                        print("Write in file :")
	                        system("tput setaf 7")
	                        system(f"cat > {fname}")
	                        system(f"hadoop fs -put {fname} /")
	                        system("tput setaf 2")
	                        print("File uploaded successfully")
	                        input("...")
	                    elif ch==8 :
	                        system("tput setaf 5")
	                        fname = input("File name : ")
	                        system("tput setaf 1")
	                        system(f"hadoop fs -rm /{fname}")
	                        input("...")
	                    elif ch==9 : 
	                        system("tput setaf 5")
	                        fname = input("File name : ")
	                        system("tput setaf 4")
	                        system(f"hadoop fs -cat /{fname}")
	                        input("...")
	                    elif ch==10 :
	                        system("tput setaf 4")
	                        system("hadoop fs -ls /")
	                        input("...")
	                    elif ch==11 :
	                        break
	                    elif ch==12 :
	                        system("tput setaf 3")
	                        print("Bye...")
	                        system("tput setaf 7")
	                        exit()
	                    else :
	                        system("tput setaf 1")
	                        print("!!Wrong choice!!\nTry again")
	                        sleep(2)
	            elif hdp==3 :
	                break
	            elif hdp==4 :
	                system("tput setaf 3")
	                print("Bye...")
	                system("tput setaf 7")
	                exit()
	            else :
	                system("tput setaf 1")
	                print("!!Wrong choice!!\nTry again")
	                sleep(2)
	    elif ch ==3:
	        break
	    elif ch == 4:
	        system("tput setaf 3")
	        print("Bye...")
	        system("tput setaf 7")
	        exit()
    
	    else :
	        system("tput setaf 1")
	        print("!!!! Wrong Choice !!!!\n Try again :-)")
	        system("tput setaf 6")
	        input("...")

def docker():

	import os
	os.system("clear")
	os.system("tput smso 5")
	os.system("tput setaf 3")
	print("\n\n\t\t\t  WELCOME TO THE DOCKER MENU  ")
	os.system("tput sgr 0 ") 

	while True:
		os.system("tput setaf 4")
		#os.system("tput smul 4")
		print("""
		1.  press 1 for Search image on Dockerhub.
		2.  press 2 for Download Docker image.
		3.  press 3 for List of Docker image.
		4.  press 4 for List of Docker container.
		5.  Press 5 for Create container.
		6.  Press 6 for All exited container.
		7.  Press 7 for start container and attach container.
		8.  Press 8 for Remove container.
		9.  Press 9 for Remove images.
		10. press 10 for Back to main menu.
		11. press 11 for Exit.
		""")
		
		os.system("tput sgr0")
		os.system("tput bold")	
		os.system("tput setaf 5")
		x=input("\nEnter the number :- ")
		os.system("clear")
		if x=="1":
			os.system("tput sgr0")	
			os.system("tput setaf 6")
			img=input("\nEnter the image name:- ")
			os.system("docker search {}".format(img))
			os.system("tput sgr0")			
			os.system("tput bold")
			os.system("tput setaf 4")
			input("\n\t\t!!!!!!!!!!!Press enter:-!!!!!!!!!!!!!!")
			os.system("tput sgr0")


		
		elif x=="2":
			os.system("tput sgr0")	
			os.system("tput setaf 6")
			z=input("\nEnter the image name:- ")	
			os.system("docker pull {}:latest".format(z))					
			os.system("tput sgr0")			
			os.system("tput bold")
			os.system("tput setaf 4")
			input("\n\t\t!!!!!!!!!!!Press enter:-!!!!!!!!!!!!!!")
			os.system("tput sgr0")


		elif x=="3":
			os.system("tput sgr0")	
			os.system("docker images")
			os.system("tput sgr0")			
			os.system("tput bold")
			os.system("tput setaf 4")
			input("\n\t\t!!!!!!!!!!!Press enter:-!!!!!!!!!!!!!!")
			os.system("tput sgr0")


			

		elif x=="4":
			os.system("tput sgr0")	
			os.system("docker ps")
			os.system("tput sgr0")			
			os.system("tput bold")
			os.system("tput setaf 4")
			input("\n\t\t!!!!!!!!!!!Press enter:-!!!!!!!!!!!!!!")
			os.system("tput sgr0")


		elif x=="5":
			os.system("tput sgr0")	
			os.system("docker images")
			img=input("\nEnter the image name:- ")
			name=input("\nEnter container name:- ")	
			os.system("docker run -it --name {}  {}:latest".format(name,img))
			os.system("tput sgr0")			
			os.system("tput bold")
			os.system("tput setaf 4")
			input("\n\t\t!!!!!!!!!!!Press enter:-!!!!!!!!!!!!!!")
			os.system("tput sgr0")



		elif x=="6":
			os.system("tput sgr0")	
			os.system("docker ps -a")
			os.system("tput sgr0")
			os.system("tput bold")
			os.system("tput setaf 4")
			input("\n\t\t!!!!!!!!!!!Press enter:-!!!!!!!!!!!!!!")
			os.system("tput sgr0")

		

		elif x=="7":
			os.system("tput sgr0")	
			os.system("docker ps -a")
			i=input("\nEnter the contianer name:- ")
			os.system("docker start {}".format(i))
			os.system("docker attach {}".format(i))

		elif x=="8":
			while True:
				os.system("tput sgr0")	
				os.system("tput smul 3")
				os.system("tput setaf 3")
				print("\n1. press 1 for Remove one container.")
				print("2. press 2 for Remove all container.")
				print("3. press 3 for Back to main menu.")
				print("4. press 4 for Exit.")

				os.system("tput sgr0")	
				os.system("tput setaf 6")
				a=input("Enter your choice:- ")
				if a=="1":
					os.system("tput sgr0")	
					os.system("docker ps -a")
					os.system("tput setaf 5")
					x=input("\nEnter id or container name:- ")
					os.system("docker rm {}".format(x))
					os.system("docker ps -a")
					os.system("tput sgr0")
					os.system("tput bold")
					os.system("tput setaf 4")
					input("\n\t\t!!!!!!!!!!!Press enter:-!!!!!!!!!!!!!!")
					os.system("tput sgr0")
				
				elif a=="2":
					os.system("tput sgr0")	
					os.system("docker ps -a")
					os.system("docker rm `docker ps -a -q`")
					os.system("docker ps -a")
					os.system("tput sgr0")
					os.system("tput bold")
					os.system("tput setaf 4")
					input("\n\t\t!!!!!!!!!!!Press enter:-!!!!!!!!!!!!!!")
					os.system("tput sgr0")

				
				elif a=="3":
					break

				elif a=="4":
					exit()
				
				else:
					print("\n\t\t!!!!!!!Enter valid number!!!!!!!!!!!!!!")



		elif x=="9":
			os.system("tput sgr0")	
			os.system("docker images")
			img=input("\nEnter image name:- ")
			os.system("docker rmi -f {}".format(img))
			os.system("docker images")
			os.system("tput sgr0")			
			os.system("tput bold")
			os.system("tput setaf 4")
			input("\n\t\t!!!!!!!!!!!Press enter:-!!!!!!!!!!!!!!")
			os.system("tput sgr0")

			


		elif x=="10":
			break

		elif x=="11":
			exit()













import os
import time
import getpass
#w=input("Press ENTER to Enter Your Password")
for w in "pass":
	os.system("tput bold")
	os.system("tput setaf 5")
	password=getpass.getpass("\tEnter your Password -")
	if password == "Arth@2020":
		time.sleep(2)
		print("------------")
		print("Have a good journey")
		print("------------")
	else:	
		os.system("tput setaf 9")
		print("You have entered wrong password please renter your password")
		os.system("tput sgr0")
		continue
	while True:
		os.system("clear")
		os.system("tput bold 5")
		os.system("tput smso 5")
		os.system("tput setaf 5")
		print("\n\t\t\t1.🌥  Amazon Web Service")
		os.system("tput sgr0")
		os.system("tput bold 0")
		os.system("tput smso 0")
		os.system("tput setaf 0")
		print("\t\t\t2.🐳 Docker") #docker
		os.system("tput sgr0")
		os.system("tput bold 2")
		os.system("tput smso 2")
		os.system("tput setaf 2")
		print("\t\t\t3.🎩 Linux & Partitions")
		os.system("tput sgr0")
		os.system("tput bold 3")
		os.system("tput smso 3")
		os.system("tput setaf 3")
		print("\t\t\t4.🌐 Web Configuration")
		os.system("tput sgr0")
		os.system("tput bold 6")	
		os.system("tput smso 6")
		os.system("tput setaf 6")
		print("\t\t\t5.🐘 Hadoop Configuration")
		os.system("tput sgr0")
		os.system("tput bold 9")
		os.system("tput smso 9")
		os.system("tput setaf 9")
		print("\t\t\t6.🏃 exit")
		
		os.system("tput sgr0")
		os.system("tput bold ")
		os.system("tput setaf 27")
		i=input("\nEnter Your Requirements:- ")
		os.system("tput sgr0 ")
		
		
		if int(i)==1:
			aws()
		elif i=="2":
			docker() 
		elif i=="3":
			linux()
		elif i=="4":
			web()
		elif i=="5":
			hadoop()
		elif i=="6":
			exit()
		else:
			os.system("tput sgr0")
			os.system("tput bold")
			os.system("tput setaf 9")
			print('\n\n\t\t\tPlease Enter Valid Number')
			input("\n\t\t\tPress ENTER to get the menu")

