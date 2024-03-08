try:
    import tkinter as tk
    from tkinter import *
    from tkinter import filedialog
    import random
    import os
    import passfunctions

except ImportError:
    raise ImportError('function is not here')

def gui_input(prompt):

        root = tk.Toplevel()
    # this will contain the entered string, and will
    # still exist after the window is destroyed
        var = tk.StringVar()

    # create the dialog
        label = tk.Label(root, text=prompt)
        entry = tk.Entry(root, textvariable=var)
        label.pack(side="left", padx=(20, 0), pady=20)
        entry.pack(side="right", fill="x", padx=(0, 20), pady=20, expand=True)

    # Let the user press the return key to destroy the gui
        entry.bind("<Return>", lambda event: root.destroy())

    # this will wait until the window is destroyed
        root.wait_window()

    # after the window has been destroyed, we can't access
    # the entry widget, but we _can_ access the associated
    # variable
        value = var.get()
        return value

def generatesinglepass():
    
    displaypasswords.delete(1.0,  END)  #deletes any data that may be in tkinter Text widget from other functions
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789' #list of characters which can be used to generate password#list of characters which can be used to generate password#list of characters which can be used to generate password
    
    number = int('1')  # set number of passwords to be generat
    
    
    while True:
        try:
            length = int(gui_input("Please enter how long you would like each password to be (e.g. 20)" )) # prompts user for length of password
        except ValueError:
            print("Not a valid number") # prints error if user hasn't enteted a valid value, (e.g. 6)
            continue
        else:
            break

    print('\nhere are the generated password:')
    
    for pwd in range(number):
        password = ''
        for c in range(length):
            password += random.choice(chars)
        print(password)
    displaypasswords.insert(1.0 ,  password) #display single generated password in text tkinter widget

def generatepass():
    displaypasswords.delete(1.0,  END) #deletes any data that may be in tkinter Text widget from other functions
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789' #list of characters which can be used to generate password#list of characters which can be used to generate password

    while True:
            try:
                number = int(gui_input("Please enter the number of passwords you would like to generate (e.g. 2)" )) # prompts user for number of passwords
            except ValueError:
                print("Not a valid number")
                continue
            else:
                break

    while True:
            try:
                length = int(gui_input("Please enter how long you would like each password to be (e.g. 20)" )) # prompts user for length of passwords
            except ValueError:
                print("Not a valid number")
                continue
            else:
                break

    print('\nhere are the generated passwords:')
    savepass = filedialog.asksaveasfilename(initialdir="/home", title = "Enter save file name",filetypes = (("text files","*.txt"),("all files","*.*")))

    with open(savepass ,"w") as text_file:  #  open text file selected by user in pevious dialog to write  generated passwords to.
        for pwd in range(number):
            password = ''
            for c in range(length):
                password += random.choice(chars)
            print(password)

            text_file.writelines(password+"\n") # write passwords to generatepass.txt file
             
            displaypasswords.insert('end', password+"\n") #  display passwords in tkinter text widget
            
        displaypasswords.insert('end',  "\nPassword's have been outputted to text file")
        

def strength(): # password strength check function for single user entered password
        displaypasswords.delete(1.0,  END) #deletes any data that may be in tkinter Text widget from other functions
        password = gui_input("Please enter password you would like to check strength of" ) # prompts user to enter password

        def strongPassword(password):
            
            passfunctions.regexcompile(password) #   runs regex commands from passfunctions.py file to test password strength

        if passfunctions.regexcompile(password) == True:
            print("Strong Password")
            displaypasswords.insert('end',  "Password is strong")
        else:
            print("This is not a strong password")
            displaypasswords.insert('end',  "Password is not strong")
            
def multiplestrength(): # password strength check function  from selected text file containing passwords
        displaypasswords.delete(1.0,  END) #deletes any data that may be in tkinter Text widget from other functions
        
        def strong_password(password):  # the function name should be snake case
           passfunctions.regexcompile(password)

        textfile =  filedialog.askopenfilename(initialdir="/home", title = "Select text file containing passwords",filetypes = (("text files","*.txt"),("all files","*.*")))
        with open(textfile, mode="r", encoding="utf-8") as pass_file: # Open fle containing passwords to read
            if os.stat(textfile).st_size == 0:
                print("no password in file")
            else:
                savefile = filedialog.asksaveasfilename(initialdir="/home", title = "Enter save file name for pass strength results",filetypes = (("text files","*.txt"),("all files","*.*")))  # open file to save password strength results to which was select in previous dialog
                with open(savefile,  "w") as strength_file:
                        for line in pass_file.readlines():  # Read all lines one-by-one
                            print("\nPassword: {}".format(line.strip()), file=strength_file)  # Print the current password ("strip" removes the whitespace characters from string).
                            displaypasswords.insert('end',"\nPassword: {}".format(line.strip()))  # Print the current password ("strip" removes the whitespace characters from string).
                            if passfunctions.regexcompile(line):  # This statement is True if the "strong_password" function returns True
                                displaypasswords.insert('end',"\nStrong Password\n") 
                                print("Strong Password",  file=strength_file) 
                                continue  # Get the next element (line of file)
                            displaypasswords.insert('end', "\nThis is not a strong password\n")  # Else statement is not needed because the "if" contains a continue
                            print("This is not a strong password",  file=strength_file)
                
def quit():
    root.quit()

root = tk.Tk()
root.geometry("350x350")
root.wm_title("Password Tools")
maintitle = tk.Label(root, text = 'Password Tools', font = ('Comic Sans MS',18))
generatesingle = tk.Button(root, text="Generate Single Password", command=generatesinglepass)
generatemulti = tk.Button(root, text="Generate Multiple Password to Text File", command=generatepass)
checkstrength = tk.Button(root,  text = "Check Password Strength",   command=strength)
checkstrengthfromtext = tk.Button(root,  text = "Check Password Strength from Text File",   command=multiplestrength)
quit = tk.Button(root,  text = "Quit Program", command=quit)
outputlabel = tk.Label(root, text = "Output")
displaypasswords = Text(root)
maintitle.pack()
generatesingle.pack()
generatemulti.pack()
checkstrength.pack()
checkstrengthfromtext.pack()
quit.pack()
outputlabel.pack()
displaypasswords.pack() 
root.mainloop()
