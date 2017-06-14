## Module Import ##
import tkinter ## Import Tkinter Modules
from tkinter import * ## Access Tkinter modules without calling to Tkinter
import os


## Find Current Directory ##
current_dir = os.getcwd()

exp_folder = "\\Experiments"
data_folder = "\\Data"
protocol_folder = "\\Protocols"

exp_dir = current_dir + exp_folder
protocol_dir = current_dir + protocol_folder
sys.path.insert(0,exp_dir)
sys.path.insert(0,protocol_dir)
## Get List of Active Experiments ##
Active_Exp = list()
for file in os.listdir(exp_dir):
    if file.endswith(".ORe"):
        Active_Exp.append(file)

for exp_file in Active_Exp:
    exp_file.replace(".ORe", "")

## Get List of Available Protocols ##
Active_Prot = list()
for prot in os.listdir(protocol_dir):
    if prot.endswith(".ORp"):
        Active_Prot.append(prot)

for prot_file in Active_Prot:
    prot_file.replace(".ORp", "")
## Experiment Command Run Function ##
def Experiment_Command_Run():
    top.destroy()
    top_run = Toplevel()
    config_file_path = exp_dir + "\\"
    config_file = open(config_file_path, "r")
    ## Import Specs ##



    ## Window Specs ##
    run_title = Label(top_run, text="Trial Setup")
    run_title.grid(row=1, column=2)

    run_ID_label = Label(top_run, text="Rat ID: ")
    run_ID_label.grid(row=2, column=1)

    run_ID_prompt = Entry(top_run)
    run_ID_prompt.grid(row=2, column=3)

    run_Drug_label = Label(top_run, text="Drug Condition: ")
    run_Drug_label.grid(row=3, column=1)

    run_Drug_List = Listbox(top_run, selectmode=BROWSE)

    return


## Experiment Delete Function ##
def Experiment_Command_Delete(Exp_Select):
    return

## Experiment Create Function ##
def Experiment_Command_Create(ExpSelected):
    create_window = Toplevel()

    ## Create Command Function ##
    def Create_Command():
        protocol_file = "SORv1" + ".ORp" + " 1"
        tempfile = "SORv1.py 1"
        file_location = protocol_dir
        file_path = file_location + "\\" + tempfile
        from SORv11 import SOR_Create_Experiment


    ## Create Cancel Function ##
    def Create_Cancel():
        create_window.destroy()

    ## Create Window Properties/Widgets ##

    Protocol_Scroll = Scrollbar(create_window)
    Protocol_Scroll.grid(row=1,column=2)

    Protocol_List = Listbox(create_window,selectmode=BROWSE,yscrollcommand=Protocol_Scroll)
    for protocol in Active_Prot:
        Protocol_List.insert(END.protocol)
    Protocol_List.grid(row=1, column=1)
    Protocol_Select = Button(create_window, text="Select Protocol", command=Create_Command)
    Protocol_Select.grid(row=2, column=1)

    Protocol_Cancel = Button(create_window, text="Cancel", command=Create_Cancel)
    Protocol_Cancel.grid(row=3, column=1)
    create_window.mainloop()
    return
## Establish Main Window ##
top = tkinter.Tk() # Establish Top/Primary Window
title = Label(top, text="OR Score 2") # Establish title as main label
title.grid(row=1, column=2)
author = Label(top, text="Created by: Daniel Palmer, PhD")
author.grid(row=2, column=2)

Curr_Version = Label(top, text="Current Version: 2.00")
Curr_Version.grid(row=3, column=2)

Curr_Exp_Scroll = Scrollbar(top)
Curr_Exp_Scroll.grid(row=4, column=2)

Curr_Exp_List = Listbox(top, selectmode=BROWSE, yscrollcommand=Curr_Exp_Scroll.set) # Create listbox of active experiments
for exp in Active_Exp:
    Curr_Exp_List.insert(END, exp)
Curr_Exp_List.grid(row=4, column=2)
Curr_Exp_Scroll.config(command=Curr_Exp_List.yview)


Select_Exp = Button(top, text="Run Experiment", command=Experiment_Command_Run())
Select_Exp.grid(row=5, column=2)

Delete_Exp = Button(top, text="Delete Experiment",command=Experiment_Command_Delete)
Delete_Exp.grid(row=6, column=2)

Create_Exp = Button(top, text = "Create New Experiment", command=Experiment_Command_Create)
Create_Exp.grid(row=7,column=2)

## Run Window Command ##
top.mainloop() # Run Main Window on Loop (Start)