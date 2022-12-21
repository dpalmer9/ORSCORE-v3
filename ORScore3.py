# Module Import - Base
import os
import sys
import time
from tkinter import *
import tkinter.filedialog
from tkinter import filedialog

# Module Import - Secondary
import pandas as pd
import numpy as np
import keyboard
# import imp

# Find Current Directory
current_dir = os.getcwd()

folder_symbol = '/'
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
sys.path.insert(0, exp_dir)
sys.path.insert(0, protocol_dir)

# Get List of Active Experiments
active_exp = list()
print(exp_dir)
for file in os.listdir(exp_dir):
    if file.endswith(".ini"):
        active_exp.append(file)

active_exp = [exp_names.replace(".ini", "") for exp_names in active_exp]

# Get List of Available Protocols
active_prot = list()
for prot in os.listdir(protocol_dir):
    if prot.endswith(".py"):
        active_prot.append(prot)

Active_Prot = [prot_file.replace(".py", "") for prot_file in active_prot]


# Establish Main Window
top = Tk()  # Establish Top/Primary Window

# icon = current_dir + folder_symbol + "Mouse_Icon.ico"

# top.iconbitmap(icon)

# Experiment Command Run Function


def experiment_command_run():
    # Acquire filename
    exp_select_list_pos = curr_exp_list.curselection()
    exp_selected_name = curr_exp_list.get(exp_select_list_pos[0])
    exp_selected_filename = exp_selected_name + ".py"
    exp_filepath = exp_dir + folder_symbol + exp_selected_filename
    exp_loaded_file = open(exp_filepath, "r")
    exp_loaded_script_list = exp_loaded_file.readlines()
    exp_protocol_name = str(exp_loaded_script_list[1])
    exp_protocol_name = [exp_protocol_name.strip("\n")]
    exp_protocol_name = str(exp_protocol_name[0])
    exp_protocol_name = [exp_protocol_name.strip("Protocol = ")]
    exp_protocol_name = str(exp_protocol_name[0])

    data_filepath = data_dir + folder_symbol + exp_selected_name + folder_symbol + exp_selected_name + "_Raw.csv"
    protocol_filepath = protocol_dir + folder_symbol + exp_selected_name + ".ORp"
    import_command = "%s = imp.load_source('%s', r'%s%sProtocols%s%s.ORp')" % (exp_protocol_name, exp_protocol_name,
                                                                               current_dir,folder_symbol, folder_symbol,
                                                                               exp_protocol_name)
    trial_thread_code = "run_thread = Thread(target = "
    trial_setup_code = ".Trial_Setup(Curr_Exp=exp_filepath, Curr_Raw_Data=data_filepath))"
    run_trial_setup = trial_thread_code + exp_protocol_name + trial_setup_code
    run_trial_code2 = "run_thread.start()"
    top.destroy()
    exec(import_command)
    exec(run_trial_setup)
    exec(run_trial_code2)

# Experiment Delete Function


def experiment_command_delete():
    exp_select_list_pos = curr_exp_list.curselection()
    exp_selected_name = curr_exp_list.get(exp_select_list_pos[0])
    global exp_dir
    file_path = exp_dir + folder_symbol + exp_selected_name + ".py"
    os.remove(file_path)
    curr_exp_list.delete(0, END)
    active_exp = list()
    for experiments in os.listdir(exp_dir):
        if file.endswith(".ini"):
            active_exp.append(experiments)

    active_exp = [exp_names.strip(".ini") for exp_names in active_exp]
    for experiments in active_exp:
        curr_exp_list.insert(END, experiments)

# Experiment Create Function


def experiment_command_create():
    create_window = Toplevel()
    # global icon
    # create_window.iconbitmap(icon)
    # Create Command Function

    def create_command():
        prot_name_pos = protocol_list.curselection()
        prot_name = protocol_list.get(prot_name_pos[0])
        protocol_file = prot_name + ".py"
        global protocol_dir
        file_location = protocol_dir
        file_path = file_location + folder_symbol + protocol_file
        if prot_name == 'SOR':
            from Protocols.SOR import ExperimentConfigure
            ExperimentConfigure()
        # import_command = "%s = imp.load_source('%s', r'%s')" % (prot_name, prot_name, file_path)
        # run_setup_command = prot_name + ".Create_Experiment()"
        # exec(import_command)
        # exec(run_setup_command)

    # Create Cancel Function

    def create_cancel():
        create_window.destroy()
        curr_exp_list.delete(0, END)
        active_exp = list()
        for experiments in os.listdir(exp_dir):
            if experiments.endswith(".ini"):
                active_exp.append(file)

        active_exp = [exp_names.strip(".ini") for exp_names in active_exp]
        for experiments in active_exp:
            curr_exp_list.insert(END, experiments)

    # Create Window Properties/Widgets

    protocol_list = Listbox(create_window,selectmode=BROWSE)
    for protocol in Active_Prot:
        protocol_list.insert(END,protocol)
    protocol_list.grid(row=1, column=1,sticky=(N, W, E, S))
    protocol_scroll = Scrollbar(create_window, orient=VERTICAL,command=protocol_list.yview)
    protocol_scroll.grid(row=1, column=2,sticky=(N, S))
    protocol_select = Button(create_window, text="Select Protocol", command=create_command)
    protocol_select.grid(row=2, column=1)

    protocol_cancel = Button(create_window, text="Done", command=create_cancel)
    protocol_cancel.grid(row=3, column=1)
    create_window.mainloop()
    return

# GUI Properties


title = Label(top, text="OR Score3")  # Establish title as main label
title.grid(row=1, column=2)
author = Label(top, text="Created by: Daniel Palmer, PhD")
author.grid(row=2, column=2)

curr_version = Label(top, text="Current Version: 1.10")
curr_version.grid(row=3, column=2)

curr_exp_list = Listbox(top, selectmode=BROWSE)  # Create listbox of active experiments
for experiment in active_exp:
    curr_exp_list.insert(END, experiment)
curr_exp_list.grid(row=4, column=2, sticky=(N, W, E, S))
curr_exp_scroll = Scrollbar(top, orient=VERTICAL,command=curr_exp_list.yview)
curr_exp_scroll.grid(row=4, column=3, sticky=(N, S))
curr_exp_list.configure(yscrollcommand=curr_exp_scroll.set)

select_exp = Button(top, text="Run Experiment", command=experiment_command_run)
select_exp.grid(row=5, column=2)

delete_exp = Button(top, text="Delete Experiment",command=experiment_command_delete)
delete_exp.grid(row=6, column=2)

create_exp = Button(top, text = "Create New Experiment", command=experiment_command_create)
create_exp.grid(row=7,column=2)

# Run Window Command
top.mainloop()  # Run Main Window on Loop (Start)


class MainWindow:
    def __init__(self):

        # Initialize Variables
        self.current_dir = ''
        self.exp_folder = ''
        self.data_folder = ''
        self.protocol_folder = ''
        self.find_folders()

        # Initialize Lists
        self.experiment_list = list()
        self.find_experiments()

        # Generate GUI
        self.top = Tk()

        # Generate Titles

        self.title_label = Label(self.top, text="ORScore 3")
        self.title_label.grid(row=1, column=2)

        self.author_label = Label(self.top, text="Created by: Daniel Palmer, PhD")
        self.author_label.grid(row=2, column=2)

        self.version_label = Label(self.top, text='Version: 3.0.0')
        self.version_label.grid(row=3, column=2)
        #
        return

    def find_folders(self):
        self.current_dir = os.getcwd()

        folder_symbol = '/'
        if sys.platform == 'linux' or sys.platform == 'darwin':
            folder_symbol = '/'
        elif sys.platform == 'win32':
            folder_symbol = '\\'
        self.exp_folder = self.current_dir + folder_symbol + 'Experiments'
        if not os.path.isdir(self.exp_folder):
            os.mkdir(self.exp_folder)
        self.data_folder = self.current_dir + folder_symbol + 'Data'
        if not os.path.isdir(self.data_folder):
            os.mkdir(self.data_folder)
        self.protocol_folder = self.current_dir + folder_symbol + 'Protocols'
        if not os.path.isdir(self.protocol_folder):
            os.mkdir(self.protocol_folder)
        return
    def find_experiments(self):
        exp_dir_list = os.listdir(self.exp_folder)
        for experiment in self.exp_folder:
            if experiment.endswith('.cfg'):
                self.experiment_list.append(file)