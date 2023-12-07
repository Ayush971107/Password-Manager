# CS Project made by Ayush Roy 
# Redistribution of following code is allowed by the creators :)

# basic flow of the program:-
# get data
# Sign up done (yes) -> login window (pwd correct) -> Main window -> Add Password -> Generate Random
#				   |							 |				  -> Edit Password
#				   |							 |				  -> Copy Password
#				   |				   (pwd wrong) -> give error
#				(no) -> sign up process and exit
# update data and exit

# all libraries are pre-installed in python, no dependencies required
from tkinter import *
from tkinter import messagebox
from random import randint
import os


def changePwdInEntry(temp):
	toFind = clicked.get()
	i = 0
	while i < len(PWDS):
		if NAMES[i] == toFind:
			break
		i += 1
	pwdEntry.delete(0, END)
	pwdEntry.insert(0, PWDS[i])
def generateRandom():
	newPwdEntry2.delete(0, END)
	pwd = ""
	for i in range(0, 10):
		pwd += (chr(randint(65, 90)))
	newPwdEntry2.insert(0, pwd.strip(" "))

# edit password from MainWindow
def editPwd():
	i = 0
	while i < len(NAMES):
		if NAMES[i] == clicked.get():
			break
		i += 1
	PWDS[i] = pwdEntry.get()
	messagebox.showinfo("QuickSave", "Password edited succesfully.")

# gui to add password entry
def AddPasswordWindow():
	global root2, newPwdEntry1, newPwdEntry2
	root2 = Tk()
	root2.title("QuickSave")
	Label(root2, text="New account: ", font=("Arial", 15)).grid(row=0, column=0)
	Label(root2, text="New password: ", font=("Arial", 15)).grid(row=1, column=0)
	newPwdEntry1, newPwdEntry2 = Entry(root2, font=("Arial", 15)), Entry(root2, font=("Arial", 15))
	newPwdEntry1.grid(row=0, column=1)
	newPwdEntry2.grid(row=1, column=1)
	Button(root2, text="Add password", font=("Arial", 15), command=addPwd).grid(row=2, column=0)
	but = Button(root2, text="Generate Random", font=("Arial", 15), command=generateRandom)
	but.config(width=20)
	but.grid(row=2, column=1)
	root2.mainloop()
# add password details from addPwdWindow
def addPwd():
	NAMES.append(newPwdEntry1.get())
	PWDS.append(newPwdEntry2.get())
	root2.destroy()
	root1.destroy()
	MainWindow()

# main gui
def MainWindow():
	global root1, clicked, pwdEntry
	try: pwdCheck = NAMES[0] == LoginEntry1.get() and PWDS[0] == LoginEntry2.get()
	except: pwdCheck = True
	try: rootState = 'normal' == root.state()
	except: rootState = False
	if pwdCheck:
		if rootState:
			root.destroy()
		root1 = Tk()
		root1.title("QuickSave")
		root1.geometry("490x115")
		# the dropdown menu
		clicked = StringVar()
		clicked.set(NAMES[0])
		dropdown = OptionMenu(root1, clicked, *NAMES, command=changePwdInEntry)
		dropdown.config(width=35)
		dropdown.grid(row=0, column=0)
		# the entry where passwords show up
		pwdEntry = Entry(root1, font=("Arial", 15))
		pwdEntry.grid(row=0, column=1)
		changePwdInEntry(0)
		# two final buttons
		addPwdButton = Button(root1, text="Add Password", font=("Arial", 15), command=AddPasswordWindow)
		editPwdButton = Button(root1, text="Edit Password", font=("Arial", 15), command=editPwd)
		copyPwdButton = Button(root1, text="Copy Password", font=("Arial", 15), command=lambda: os.system("echo|set /p=" + pwdEntry.get() + "|clip"))
		addPwdButton.config(width=22)
		editPwdButton.config(width=20)
		copyPwdButton.config(width=30)
		addPwdButton.grid(row=1, column=0)
		editPwdButton.grid(row=1, column=1)
		copyPwdButton.grid(row=2, column=0, columnspan=2)
		root1.mainloop()
	else:
		messagebox.showerror("Error", "Wrong Password.")
		return

# login gui
def LoginWindow():
	global root, LoginEntry1, LoginEntry2
	root = Tk()
	root.title("QuickSave")
	root.geometry("350x140")
	Label(root, text="Signup-", font=("Arial", 15)).grid(row=0)
	LoginEntry1, LoginEntry2 = Entry(root, font=("Arial", 15)), Entry(root, font=("Arial", 15))
	loginButton = Button(root, text="Login", font=("Arial", 15), command=MainWindow)
	Label(root, text="Username: ", font=("Arial", 15)).grid(row=1)
	LoginEntry1.grid(row=1, column=1)
	Label(root, text="Password: ", font=("Arial", 15)).grid(row=2, column=0)
	LoginEntry2.grid(row=2, column=1)
	loginButton.place(relx=0.5, rely=0.8, anchor=CENTER)
	root.mainloop()

# sign up before using app
if os.path.isfile("data.txt") == False:
	print("Account name and password required. This is a signup process.")
	name = input("Account name: ").strip("\n")
	pwd = input("Account password: ").strip("\n")
	print("Enter account name and password next time while starting the app")
	open("data.txt", "w").writelines(name + "|" + pwd)
	exit()


# get all passwords from database(here it is a text file)
NAMES, PWDS = [], []
for line in open("data.txt", "r").readlines():
	temp = line.split("|")
	NAMES.append(temp[0].strip("\n"))
	PWDS.append(temp[1].strip("\n"))

LoginWindow()

# changes made to file if new password is added or edited
i = 0
lines = []
while i < len(NAMES):
	lines.append(NAMES[i] + "|" + PWDS[i] + "\n")
	i += 1
open("data.txt", "w").writelines(lines)