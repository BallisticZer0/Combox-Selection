# Demonstrating the use of Combobox and tkinter buttons
  
import tkinter as tk 
from tkinter import ttk 
  
# Creating tkinter window 
root = tk.Tk() 
root.title("Dental Milling Machines")
root.geometry("1000x900") 
frame = tk.Frame(root)


# label for the selection menu 
ttk.Label(root, text = "Dental Milling Machines",  
          background = 'green', foreground ="white",  
          font = ("Times New Roman", 15)).grid(row = 0, column = 10) 
  
# label to the left of the selection window
ttk.Label(root, text = "Choose a number :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 
  
# Combobox creation or selection window 
n = tk.StringVar() 
numbers = ttk.Combobox(root, width = 27, textvariable = n)


  
# Adding combobox drop down list 
numbers['values'] = (' 1',  
                          ' 2', 
                          ' 3', 
                          ' 4', 
                          ' 5') 
  
numbers.grid(column = 10, row = 5)
numbers.current()

def Cnum():# current number in the box, It's in a function because it wont run correctly with it being printed directly into the "command" section
    print(numbers.current()+1)

# The button that says Go and prints the number in the selection box
button = tk.Button(root,
                    text=" Go ",fg="brown",command=Cnum,font = ("Times New Roman", 15)).grid(row = 5, column = 20)#giving the command to reference the Var "Number1" which is 


# This loops the program so the user can keep putting in numbers and pressing Go   
root.mainloop() 
