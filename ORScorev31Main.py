# Module Import
import os
from tkinter import *
import sys


# Find Current Directory
current_dir = os.getcwd()

exp_folder = "\\Experiments"
data_folder = "\\Data"
protocol_folder = "\\Protocols"

exp_dir = current_dir + exp_folder
protocol_dir = current_dir + protocol_folder
data_dir = current_dir + data_folder
sys.path.insert(0, exp_dir)
sys.path.insert(0, protocol_dir)
# Get List of Active Experiments
Active_Exp = list()
for file in os.listdir(exp_dir):
    if file.endswith(".ORe"):
        Active_Exp.append(file)

Active_Exp = [exp_names.strip(".ORe") for exp_names in Active_Exp]

# Get List of Available Protocols
Active_Prot = list()
for prot in os.listdir(protocol_dir):
    if prot.endswith(".py"):
        Active_Prot.append(prot)

Active_Prot = [prot_file.strip(".py") for prot_file in Active_Prot]


# Establish Main Window
top = Tk()  # Establish Top/Primary Window
icon = current_dir + "\\" + "Mouse_Icon.ico"
top.iconbitmap(icon)

# Experiment Command Run Function


def experiment_command_run():

    # Acquire filename
    exp_select_list_pos = curr_exp_list.curselection()
    exp_selected_name = curr_exp_list.get(exp_select_list_pos[0])
    exp_selected_filename = exp_selected_name + ".ORe"
    exp_filepath = exp_dir + "\\" + exp_selected_filename
    exp_loaded_file = open(exp_filepath, "r")
    exp_loaded_script_list = exp_loaded_file.readlines()
    exp_protocol_name = str(exp_loaded_script_list[1])
    exp_protocol_name = [exp_protocol_name.strip("\n")]
    exp_protocol_name = str(exp_protocol_name[0])
    exp_protocol_name = [exp_protocol_name.strip("Protocol = ")]
    exp_protocol_name = str(exp_protocol_name[0])

    data_filepath = data_dir + "\\" + exp_selected_name + "\\" + exp_selected_name + "_Raw.csv"
    top.destroy()
    if exp_protocol_name == "MSO":
        from Protocols.MSO import Trial_Setup
        Trial_Setup(Curr_Exp=exp_filepath, Curr_Raw_Data=data_filepath)
    if exp_protocol_name == "SLR":
        from Protocols.SLR import Trial_Setup
        Trial_Setup(Curr_Exp=exp_filepath, Curr_Raw_Data=data_filepath)
    if exp_protocol_name == "SOR":
        from Protocols.SOR import Trial_Setup
        Trial_Setup(Curr_Exp=exp_filepath, Curr_Raw_Data=data_filepath)



# Experiment Delete Function

def experiment_command_delete():
    exp_select_list_pos = curr_exp_list.curselection()
    exp_selected_name = curr_exp_list.get(exp_select_list_pos[0])
    global exp_dir
    file_path = exp_dir + "\\" + exp_selected_name + ".ORe"
    os.remove(file_path)
    curr_exp_list.delete(0, END)
    active_exp = list()
    for files in os.listdir(exp_dir):
        if files.endswith(".ORe"):
            active_exp.append(file)

    active_exp = [exp_names.strip(".ORe") for exp_names in active_exp]
    for experiments in active_exp:
        curr_exp_list.insert(END, experiments)

# Experiment Create Function


def experiment_command_create():
    create_window = Toplevel()
    global icon
    create_window.iconbitmap(icon)

    # Create Command Function
    def create_command():
        prot_name_pos = protocol_list.curselection()
        prot_name = protocol_list.get(prot_name_pos[0])
        if prot_name == "MSO":
            from Protocols.MSO import Create_Experiment
            Create_Experiment()
        if prot_name == "SLR":
            from Protocols.SLR import Create_Experiment
            Create_Experiment()
        if prot_name == "SOR":
            from Protocols.SOR import Create_Experiment
            Create_Experiment()

    # Create Cancel Function
    def create_cancel():
        create_window.destroy()
        curr_exp_list.delete(0, END)
        active_exp = list()
        for files in os.listdir(exp_dir):
            if files.endswith(".ORe"):
                active_exp.append(files)

        active_exp = [exp_names.strip(".ORe") for exp_names in active_exp]
        for experiments in active_exp:
            curr_exp_list.insert(END, experiments)

    # Create Window Properties/Widgets

    protocol_list = Listbox(create_window, selectmode=BROWSE)
    for protocol in Active_Prot:
        protocol_list.insert(END, protocol)
    protocol_list.grid(row=1, column=1)
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
for exp in Active_Exp:
    curr_exp_list.insert(END, exp)
curr_exp_list.grid(row=4, column=2, sticky=(N, W, E, S))
curr_exp_scroll = Scrollbar(top, orient=VERTICAL,command=curr_exp_list.yview)
curr_exp_scroll.grid(row=4, column=3, sticky=(N, S))
curr_exp_list.configure(yscrollcommand=curr_exp_scroll.set)

select_exp = Button(top, text="Run Experiment", command=experiment_command_run)
select_exp.grid(row=5, column=2)

delete_exp = Button(top, text="Delete Experiment", command=experiment_command_delete)
delete_exp.grid(row=6, column=2)

create_exp = Button(top, text="Create New Experiment", command=experiment_command_create)
create_exp.grid(row=7, column=2)

# Run Window Command
top.mainloop()  # Run Main Window on Loop (Start)
