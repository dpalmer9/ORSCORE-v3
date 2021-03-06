## Module Import ##
import os
import time
from tkinter import *  ## Access Tkinter modules without calling to Tkinter
import tkinter.filedialog
from tkinter import filedialog
from threading import Thread
import imp
import sys
import pandas as pd
import numpy as np
import pygame





## Find Current Directory ##
current_dir = os.getcwd()

if sys.platform == 'linux' or sys.platform == 'darwin':
    folder_symbol = '/'
elif sys.platform == 'win32':
    folder_symbol = '\\'
    
exp_folder = folder_symbol + 'Experiments'
data_folder = folder_symbol + 'Data'
protocol_folder = folder_symbol + 'Protocols'

exp_dir = current_dir + exp_folder
protocol_dir = current_dir + protocol_folder
data_dir = current_dir + data_folder
sys.path.insert(0,exp_dir)
sys.path.insert(0,protocol_dir)
## Get List of Active Experiments ##
Active_Exp = list()
for file in os.listdir(exp_dir):
    if file.endswith(".ORe"):
        Active_Exp.append(file)

Active_Exp = [exp_names.replace(".ORe","") for exp_names in Active_Exp]

## Get List of Available Protocols ##
Active_Prot = list()
for prot in os.listdir(protocol_dir):
    if prot.endswith(".ORp"):
        Active_Prot.append(prot)

Active_Prot = [prot_file.replace(".ORp","") for prot_file in Active_Prot]


## Establish Main Window ##
top = Tk() # Establish Top/Primary Window
#icon = current_dir + folder_symbol + "Mouse_Icon.ico"
#top.iconbitmap(icon)

## Experiment Command Run Function ##
def Experiment_Command_Run():
    ## Acquire filename ##
    exp_select_list_pos = Curr_Exp_List.curselection()
    exp_selected_name = Curr_Exp_List.get(exp_select_list_pos[0])
    exp_selected_filename = exp_selected_name + ".ORe"
    exp_filepath = exp_dir + folder_symbol + exp_selected_filename
    exp_loaded_file = open(exp_filepath,"r")
    exp_loaded_script_list = exp_loaded_file.readlines()
    exp_protocol_name = str(exp_loaded_script_list[1])
    exp_protocol_name = [exp_protocol_name.strip("\n")]
    exp_protocol_name = str(exp_protocol_name[0])
    exp_protocol_name = [exp_protocol_name.strip("Protocol = ")]
    exp_protocol_name = str(exp_protocol_name[0])

    data_filepath = data_dir + folder_symbol + exp_selected_name + folder_symbol + exp_selected_name + "_Raw.csv"
    protocol_filepath = protocol_dir + folder_symbol + exp_selected_name + ".ORp"
    import_command = "%s = imp.load_source('%s', r'%s%sProtocols%s%s.ORp')" % (exp_protocol_name, exp_protocol_name, current_dir,folder_symbol, folder_symbol, exp_protocol_name)
    trial_thread_code = "run_thread = Thread(target = "
    trial_setup_code = ".Trial_Setup(Curr_Exp=exp_filepath, Curr_Raw_Data=data_filepath))"
    run_trial_setup = trial_thread_code + exp_protocol_name + trial_setup_code
    run_trial_code2 = "run_thread.start()"
    top.destroy()
    exec(import_command)
    exec(run_trial_setup)
    exec(run_trial_code2)



## Experiment Delete Function ##
def Experiment_Command_Delete():
    exp_select_list_pos = Curr_Exp_List.curselection()
    exp_selected_name = Curr_Exp_List.get(exp_select_list_pos[0])
    global exp_dir
    file_path = exp_dir + folder_symbol + exp_selected_name + ".ORe"
    os.remove(file_path)
    Curr_Exp_List.delete(0, END)
    Active_Exp = list()
    for file in os.listdir(exp_dir):
        if file.endswith(".ORe"):
            Active_Exp.append(file)

    Active_Exp = [exp_names.strip(".ORe") for exp_names in Active_Exp]
    for exp in Active_Exp:
        Curr_Exp_List.insert(END, exp)

## Experiment Create Function ##
def Experiment_Command_Create():
    create_window = Toplevel()
    #global icon
    #create_window.iconbitmap(icon)



    ## Create Command Function ##
    def Create_Command():
        prot_name_pos = Protocol_List.curselection()
        prot_name = Protocol_List.get(prot_name_pos[0])
        protocol_file = prot_name + ".ORp"
        global protocol_dir
        file_location = protocol_dir
        file_path = file_location + folder_symbol + protocol_file
        import_command = "%s = imp.load_source('%s', r'%s')" % (prot_name, prot_name, file_path)
        run_setup_command = prot_name + ".Create_Experiment()"
        exec(import_command)
        exec(run_setup_command)


    ## Create Cancel Function ##
    def Create_Cancel():
        create_window.destroy()
        Curr_Exp_List.delete(0, END)
        Active_Exp = list()
        for file in os.listdir(exp_dir):
            if file.endswith(".ORe"):
                Active_Exp.append(file)

        Active_Exp = [exp_names.strip(".ORe") for exp_names in Active_Exp]
        for exp in Active_Exp:
            Curr_Exp_List.insert(END, exp)

    ## Create Window Properties/Widgets ##


    Protocol_List = Listbox(create_window,selectmode=BROWSE)
    for protocol in Active_Prot:
        Protocol_List.insert(END,protocol)
    Protocol_List.grid(row=1, column=1,sticky=(N,W,E,S))
    Protocol_Scroll = Scrollbar(create_window, orient=VERTICAL,command=Protocol_List.yview)
    Protocol_Scroll.grid(row=1,column=2,sticky=(N,S))
    Protocol_Select = Button(create_window, text="Select Protocol", command=Create_Command)
    Protocol_Select.grid(row=2, column=1)

    Protocol_Cancel = Button(create_window, text="Done", command=Create_Cancel)
    Protocol_Cancel.grid(row=3, column=1)
    create_window.mainloop()
    return

## GUI Properties ##
title = Label(top, text="OR Score3") # Establish title as main label
title.grid(row=1, column=2)
author = Label(top, text="Created by: Daniel Palmer, PhD")
author.grid(row=2, column=2)

Curr_Version = Label(top, text="Current Version: 1.10")
Curr_Version.grid(row=3, column=2)



Curr_Exp_List = Listbox(top, selectmode=BROWSE) # Create listbox of active experiments
for exp in Active_Exp:
    Curr_Exp_List.insert(END, exp)
Curr_Exp_List.grid(row=4, column=2,sticky=(N,W,E,S))
Curr_Exp_Scroll = Scrollbar(top, orient=VERTICAL,command=Curr_Exp_List.yview)
Curr_Exp_Scroll.grid(row=4, column=3,sticky=(N,S))
Curr_Exp_List.configure(yscrollcommand=Curr_Exp_Scroll.set)



Select_Exp = Button(top, text="Run Experiment", command=Experiment_Command_Run)
Select_Exp.grid(row=5, column=2)

Delete_Exp = Button(top, text="Delete Experiment",command=Experiment_Command_Delete)
Delete_Exp.grid(row=6, column=2)

Create_Exp = Button(top, text = "Create New Experiment", command=Experiment_Command_Create)
Create_Exp.grid(row=7,column=2)

## Run Window Command ##
top.mainloop() # Run Main Window on Loop (Start)
