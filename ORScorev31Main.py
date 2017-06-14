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
data_dir = current_dir + data_folder
sys.path.insert(0,exp_dir)
sys.path.insert(0,protocol_dir)
## Get List of Active Experiments ##
Active_Exp = list()
for file in os.listdir(exp_dir):
    if file.endswith(".ORe"):
        Active_Exp.append(file)

Active_Exp = [exp_names.strip(".ORe") for exp_names in Active_Exp]

## Get List of Available Protocols ##
Active_Prot = list()
for prot in os.listdir(protocol_dir):
    if prot.endswith(".py"):
        Active_Prot.append(prot)

Active_Prot = [prot_file.strip(".py") for prot_file in Active_Prot]

## Experiment Command Run Function ##
def Experiment_Command_Run():
    ## Acquire filename ##
    exp_select_list_pos = Curr_Exp_List.curselection()
    exp_selected_name = Curr_Exp_List.get(exp_select_list_pos[0])
    exp_selected_filename = exp_selected_name + ".ORe"
    exp_filepath = exp_dir + "\\" + exp_selected_filename
    exp_loaded_file = open(exp_filepath,"r")
    exp_loaded_script_list = exp_loaded_file.readlines()
    exp_protocol_name = str(exp_loaded_script_list[1])
    exp_protocol_name = [exp_protocol_name.strip("\n")]
    exp_protocol_name = str(exp_protocol_name[0])
    exp_protocol_name = [exp_protocol_name.strip("Protocol = ")]
    exp_protocol_name = str(exp_protocol_name[0])

    data_filepath = data_dir + "\\" + exp_selected_name + "\\" + exp_selected_name + "_Raw.csv"
    import_command = "import %s" % (exp_protocol_name)
    trial_setup_code = ".Trial_Setup(Curr_Exp=exp_filepath, Curr_Raw_Data=data_filepath)"
    run_trial_setup = exp_protocol_name + trial_setup_code
    exec(import_command)
    exec(run_trial_setup)


    return


## Experiment Delete Function ##
def Experiment_Command_Delete(Exp_Select):
    return

## Experiment Create Function ##
def Experiment_Command_Create():
    create_window = Toplevel()


    ## Create Command Function ##
    def Create_Command():
        prot_name_pos = Protocol_List.curselection()
        prot_name = Protocol_List.get(prot_name_pos[0])
        protocol_file = prot_name + ".py"
        tempfile = "SORv1.py 1"
        file_location = protocol_dir
        file_path = file_location + "\\" + protocol_file
        import_command = "import %s" % (prot_name)
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
    Protocol_List.grid(row=1, column=1)
    Protocol_Select = Button(create_window, text="Select Protocol", command=Create_Command)
    Protocol_Select.grid(row=2, column=1)

    Protocol_Cancel = Button(create_window, text="Done", command=Create_Cancel)
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


Select_Exp = Button(top, text="Run Experiment", command=Experiment_Command_Run)
Select_Exp.grid(row=5, column=2)

Delete_Exp = Button(top, text="Delete Experiment",command=Experiment_Command_Delete)
Delete_Exp.grid(row=6, column=2)

Create_Exp = Button(top, text = "Create New Experiment", command=Experiment_Command_Create)
Create_Exp.grid(row=7,column=2)

## Run Window Command ##
top.mainloop() # Run Main Window on Loop (Start)