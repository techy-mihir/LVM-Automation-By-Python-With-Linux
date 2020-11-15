import os
os.system("clear")
while True:
	os.system("clear")
	os.system("tput setaf 3")
	print("\t\t\t\t========================================================")
	print("\t\t\t\t\tHeyy Welcome to my Automation LVM tool")
	print("\t\t\t\t========================================================")
	os.system("tput setaf 7")
	print("""
	Press 1:Show avialable device
	Press 2:Create pv(Pysical volumee)
	Press 3:Create VG(Volume group)
	Press 4:Create LV
	Press 5:Extend LV
	Press 6:Show all pv,vg,lv
	Press 7:Mounted LV's
	Press 8:Exit
	""")
	op=input("Enter the choice:")
	if op == "1":
		os.system("fdisk -l")
		input()
	elif op == "2":
		p=int(input("Enter the how many disk you want contribute?"))
		for i in range(p):
			dv=input(f"Enter the {i+1} disk name :")
			os.system(f"pvcreate {dv}")
			print("pv created successfully")
		input()
	elif op == "3":
		vg=input("Enter the new vg name :")
		pv=int(input("Enter the how many pv you want contribute in vg?"))
		v=[]
		s=" "
		for i in range(pv):
			v1=input(f"Enter the {i+1} pv name")
			v.append(v1)
		os.system(f"vgcreate {vg} {s.join(v)}")
		input()
	elif op =="4":
		pr=input("Enter the size of for partion(ex:3G or 5G):")
		pn=input("Enter the name of partion for creation:")
		pg=input("Enter the vg name:")
		os.system(f"lvcreate --size {pr} --name {pn} {pg}")	
		print("",end="\n\n")
		os.system(f"mkfs.ext4 /dev/{pg}/{pn}")
		mu=input("Enter the of folder for mount:")
		os.system(f"mkdir /{mu}")
		os.system(f"mount /dev/{pg}/{pn} /{mu}")
		os.system("tput setaf 2")# 2 for green
		print("===>Succesfully created partion<===")
		os.system("tput setaf 7")
		input()
	elif op == "5":
		pr=input("Enter the size of for extend(ex:3G or 5G):")
		pn=input("Enter the name of partion :")
		pg=input("Enter the vg name:")
		os.system(f"lvextend --size +{pr} /dev/{pg}/{pn}")
		os.system(f"resize2fs /dev/{pg}/{pn}")
		input()
	elif op =="6":
		print("""
		Press 1:Show pv	
		Press 2:Show vg
		press 3:Show lv
		Press 4: Exit
		""")
		while True:
			c=input("Enter your choice :")
			if c=="1":
				os.system("pvdisplay")
			elif c=="2":
				os.system("vgdisplay")
			elif c=="3":
				os.system("lvdisplay")
			elif c=="4":
				break
			else:
				print("Not supported.. choice")
		input()
	elif op == "7":
		os.system("df -h")
		input()
	elif op == "8":
		break
		input()
	else:
		print("Choice not supported.....")
		input()

	
		

	
	

