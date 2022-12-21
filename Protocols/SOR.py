## Module Import ##
import os
import time
from tkinter import *  # Access Tkinter modules without calling to Tkinter
import csv
import configparser
import sys

import keyboard
import pandas as pd

# Class - Experiment Configuration

class ExperimentConfigure:
    def __init__(self):
        self.curr_dir = os.getcwd()
        if sys.platform == 'linux' or sys.platform == 'darwin':
            self.folder_symbol = '/'
        elif sys.platform == 'win32':
            self.folder_symbol = '\\'
        self.experiment_folder = self.curr_dir + self.folder_symbol + 'Experiments' + self.folder_symbol
        # Initialize ConfigParser object
        self.experiment_config = configparser.ConfigParser()

        # Initialize parameters
        self.condition_list = list()
        self.object_list = list()
        self.key_dict = dict()

        # String Var for input fields
        self.experiment_id_string_var = StringVar()
        self.sample_cutoff_string_var = StringVar()
        self.sample_max_string_var = StringVar()
        self.choice_cutoff_string_var = StringVar()
        self.choice_max_string_var = StringVar()
        self.additonal_measure_string_var = StringVar()

        # Construct Primary GUI
        self.construct_gui()

    def construct_gui(self):
        # GUI
        toplevel = Toplevel()
        icon_path = current_dir + "\\" + "Mouse_Icon.ico"
        toplevel.iconbitmap(icon_path)

        window_title = Label(toplevel, text="SOR Experiment Creator")
        window_title.grid(row=1, column=2)

        id_label = Label(toplevel, text="Experiment ID: ")
        id_label.grid(row=2, column=1)

        id_prompt = Entry(toplevel, textvariable=self.experiment_id_string_var)
        id_prompt.grid(row=2, column=2)

        sample_cutoff_label = Label(toplevel, text="Sample Exploration Cutoff (sec): ")
        sample_cutoff_label.grid(row=3, column=1)

        sample_cutoff_entry = Entry(toplevel, width=4, textvariable=self.sample_cutoff_string_var)
        sample_cutoff_entry.grid(row=3, column=2)

        sample_max_label = Label(toplevel, text="Sample Exploration Maximum (sec): ")
        sample_max_label.grid(row=4, column=1)

        sample_max_entry = Entry(toplevel, width=4, textvariable=self.sample_max_string_var)
        sample_max_entry.grid(row=4, column=2)

        choice_cutoff_label = Label(toplevel, text="Choice Exploration Cutoff (sec): ")
        choice_cutoff_label.grid(row=5, column=1)

        choice_cutoff_entry = Entry(toplevel, width=4, textvariable=self.choice_cutoff_string_var)
        choice_cutoff_entry.grid(row=5, column=2)

        choice_max_label = Label(toplevel, text="Choice Exploration Maximum (sec): ")
        choice_max_label.grid(row=6, column=1)

        choice_max_entry = Entry(toplevel, width=4, textvariable=self.choice_max_string_var)
        choice_max_entry.grid(row=6, column=2)

        choice_add_time_label = Label(toplevel, text="Additional Choice Measure Time (sec): ")
        choice_add_time_label.grid(row=7, column=1)

        choice_add_time_entry = Entry(toplevel, width=4, textvariable=self.additonal_measure_string_var)
        choice_add_time_entry.grid(row=7, column=2)

        condition_button = Button(toplevel, text="Conditions", command=self.condition_gui)
        condition_button.grid(row=8, column=2)

        object_list_button = Button(toplevel, text="Object List", command=self.object_pair_gui)
        object_list_button.grid(row=9, column=2)

        keybinding_button = Button(toplevel, text="Key Bindings", command=self.keybinding_gui)
        keybinding_button.grid(row=10, column=2)

        save_close_button = Button(toplevel, text="Save and Close",
                                   command=lambda: self.save_close_experiment(toplevel))
        save_close_button.grid(row=11, column=2)

        # Run Window Command
        toplevel.mainloop()

    def condition_gui(self):
        condition_window = Toplevel()
        icon_path = current_dir + "\\" + "Mouse_Icon.ico"
        condition_window.iconbitmap(icon_path)

        condition_title = Label(condition_window, text="Condition List")
        condition_title.grid(row=1, column=2)

        condition_listbox = Listbox(condition_window, selectmode=BROWSE)
        for condition in self.condition_list:
            condition_listbox.insert(END, condition)
        condition_listbox.grid(row=2, column=2)

        condition_input = Entry(condition_window)
        condition_input.grid(row=3, column=2)

        def condition_add():
            new_condition = condition_input.get()
            condition_listbox.insert(END, new_condition)
            self.condition_list.append(new_condition)
            condition_input.delete(0, END)

        def condition_remove():
            condition_sel = condition_listbox.curselection()
            condition_name = condition_listbox.get(condition_sel[0])
            self.condition_list.remove(condition_name)
            condition_listbox.delete(condition_sel)

        # SOR Done
        def condition_done():
            condition_window.destroy()
            self.experiment_config['Condition Parameters'] = {}
            self.experiment_config['Condition Parameters']['conditions'] = ','.join(self.condition_list)

        condition_add_button = Button(condition_window, text="Add", command=condition_add)
        condition_add_button.grid(row=4, column=1)

        condition_remove_button = Button(condition_window, text="Remove", command=condition_remove)
        condition_remove_button.grid(row=4, column=3)

        condition_done_button = Button(condition_window, text="Done", command=condition_done)
        condition_done_button.grid(row=5, column=2)

        condition_window.focus_force()
        condition_window.mainloop()

    def object_pair_gui(self):
        object_pair_window = Toplevel()
        icon_path = current_dir + "\\" + "Mouse_Icon.ico"
        object_pair_window.iconbitmap(icon_path)

        # Add Object Pair
        def object_pair_add():
            object1 = object_pair_entry.get()
            object_pair_listbox.insert(END, object1)
            self.object_list.append(object1)
            object_pair_entry.delete(0, END)

        # Remove Object Pair
        def object_pair_remove():
            remove_set = object_pair_listbox.curselection()
            object_pair_identity_name = object_pair_listbox.get(remove_set[0])
            object_pair_listbox.delete(object_pair_identity_name)
            self.object_list.remove(remove_set)

        # Done
        def object_pair_done():
            object_pair_window.destroy()
            self.experiment_config['Object List'] = {}
            self.experiment_config['Object List']['objects'] = ','.join(self.object_list)

        # Window Configuration

        object_pair_title = Label(object_pair_window, text="Object List")
        object_pair_title.grid(row=1, column=2)

        object_pair_listbox = Listbox(object_pair_window, selectmode=BROWSE)
        for pair in self.object_list:
            object_pair_listbox.insert(END, pair)
        object_pair_listbox.grid(row=2, column=2)

        object_pair_object1_label = Label(object_pair_window, text="Object")
        object_pair_object1_label.grid(row=3, column=2)

        object_pair_entry = Entry(object_pair_window)
        object_pair_entry.grid(row=4, column=2)

        object_pair_add_button = Button(object_pair_window, text="Add", command=object_pair_add)
        object_pair_add_button.grid(row=5, column=2)

        object_pair_remove_button = Button(object_pair_window, text="Remove", command=object_pair_remove)
        object_pair_remove_button.grid(row=6, column=2)

        object_pair_done_button = Button(object_pair_window, text="Done", command=object_pair_done)
        object_pair_done_button.grid(row=7, column=2)

        object_pair_window.focus_force()
        object_pair_window.mainloop()

    def keybinding_gui(self):
        top_keybind = Toplevel()
        icon_path = current_dir + "\\" + "Mouse_Icon.ico"
        top_keybind.iconbitmap(icon_path)

        key_bind_right_string = StringVar()
        key_bind_right_string.set("l")

        key_bind_left_string = StringVar()
        key_bind_left_string.set("a")

        def keybind_done():
            self.key_dict['mode'] = key_func.get()
            self.experiment_config['Key Bindings'] = self.key_dict
            top_keybind.destroy()

        def keybind_func_left():
            left_key = keyboard.read_key()
            self.key_dict['left'] = left_key
            key_bind_left_string.set(left_key)

        def keybind_func_right():
            right_key = keyboard.read_key()
            self.key_dict['right'] = right_key
            key_bind_right_string.set(right_key)

        keybind_label = Label(top_keybind, text="Keybinding")
        keybind_label.grid(row=1, column=1)

        keybind_radio_label = Label(top_keybind, text="Key Function")
        keybind_radio_label.grid(row=2, column=1)

        key_func = IntVar()

        keybind_radio_double = Radiobutton(top_keybind, text="Press to start,"
                                                             "Press to Release", variable=key_func, value=1)
        keybind_radio_double.grid(row=3, column=1)
        keybind_radio_double.select()

        keybind_radio_hold = Radiobutton(top_keybind, text="Hold to record", variable=key_func, value=2)
        keybind_radio_hold.grid(row=4, column=1)

        keybind_left_label = Label(top_keybind, text="Left Object Key")
        keybind_left_label.grid(row=5, column=1)

        keybind_left = Label(top_keybind, textvariable=key_bind_left_string)
        keybind_left.grid(row=5, column=2)

        keybind_left_bind_button = Button(top_keybind, text="Bind", command=keybind_func_left)
        keybind_left_bind_button.grid(row=5, column=3)

        keybind_right_label = Label(top_keybind, text="Right Object Key")
        keybind_right_label.grid(row=6, column=1)

        keybind_right = Label(top_keybind, textvariable=key_bind_right_string)
        keybind_right.grid(row=6, column=2)

        keybind_right_bind_button = Button(top_keybind, text="Bind", command=keybind_func_right)
        keybind_right_bind_button.grid(row=6, column=3)

        keybind_done_button = Button(top_keybind, text="Done", command=keybind_done)
        keybind_done_button.grid(row=7, column=2)

        top_keybind.focus_force()
        top_keybind.mainloop()

    def save_close_experiment(self,tk_level):
        self.experiment_config['Experiment Details'] = {}
        self.experiment_config['Experiment Details']['experiment_name'] = self.experiment_id_string_var.get()

        self.experiment_config['Time Parameters'] = {}
        self.experiment_config['Time Parameters']['sample_cutoff'] = self.sample_cutoff_string_var.get()
        self.experiment_config['Time Parameters']['sample_max'] = self.sample_max_string_var.get()
        self.experiment_config['Time Parameters']['choice_cutoff'] = self.choice_cutoff_string_var.get()
        self.experiment_config['Time Parameters']['choice_max'] = self.choice_max_string_var.get()
        self.experiment_config['Time Parameters']['additional_time'] = self.additonal_measure_string_var.get()

        config_filepath = self.experiment_folder + self.experiment_id_string_var.get() + '.ini'

        with open(config_filepath, 'w') as config_file:
            self.experiment_config.write(config_file)

        # Data files
        data_folderpath = self.curr_dir + self.folder_symbol + 'Data' + self.folder_symbol + \
                          self.experiment_id_string_var.get() + self.folder_symbol
        sample_bout_filepath = data_folderpath + self.experiment_id_string_var.get() + '_Sample_Bout.csv'
        sample_summary_filepath = data_folderpath + self.experiment_id_string_var.get() + '_Sample_Summary.csv'
        choice_bout_filepath = data_folderpath + self.experiment_id_string_var.get() + '_Choice_Bout.csv'
        choice_summary_filepath = data_folderpath + self.experiment_id_string_var.get() + '_Choice_Summary.csv'

        bout_pd = pd.DataFrame(columns=['Bout#', 'Bout_Start_Time', 'Bout_Side', 'Bout_Duration'])
        sample_pd = pd.DataFrame(columns=['Date', 'Time', 'Animal_ID', 'Condition', 'Left_Object','Right_Object',
                                          'Left_Explore_Total', 'Right_Explore_Total', 'Total_Exploration',
                                          'Discrimination_Ratio'])
        choice_pd = pd.DataFrame(columns=['Date','Time', 'Animal_ID', 'Condition', 'Left_Object', 'Right_Object',
                                          'Novel_Side', 'Delay', 'Novel_Explore_Total', 'Familiar_Explore_Total',
                                          'Total_Exploration', 'Discrimination_Ratio', '%d_Novel_Explore',
                                          '%d_Familiar_Explore', '%d_Discrimination_Ratio'])

        bout_pd.to_csv(sample_bout_filepath, index=False)
        bout_pd.to_csv(choice_bout_filepath, index=False)
        sample_pd.to_csv(sample_summary_filepath, index=False)
        choice_pd.to_csv(choice_summary_filepath, index=False)

        tk_level.destroy()




# Find Current Directory
current_dir = os.getcwd()

exp_folder = "\\Experiments"
data_folder = "\\Data"
protocol_folder = "\\Protocols"

current_dir.replace("\\Protocols", "")
experiment_dir = current_dir + exp_folder
data_dir = current_dir + data_folder

# SOR Variable List - Create
conditions_list = list()
object_pairs_list = list()
left_keybind = "a"
right_keybind = "l"
key_setting = "1"

# SOR - Create Experiment Function


def create_experiment():

    # Keybinding Menu
    ## Finish: Save Function ##
    def SOR_Finish():
        nonlocal Key_Setting
        exp_filename = SOR_ID_Prompt.get() + ".ORe"
        data_raw_filename = SOR_ID_Prompt.get() + "_Raw.csv"
        data_raw_filepath = data_dir + "\\" + data_raw_filename

        if len(SOR_Additional_Measure_Prompt.get()) == 0:
            SOR_Additional_Time = 0
        else:
            SOR_Additional_Time = int(SOR_Additional_Measure_Prompt.get())


        exp_filepath = experiment_dir + "\\" + exp_filename
        data_file_dir = data_dir + "\\" + SOR_ID_Prompt.get()
        os.makedirs(data_file_dir)

        data_samp_bout_filename = SOR_ID_Prompt.get() + "_Samp_Bout.csv"
        data_samp_bout_filepath = data_file_dir + "\\" + data_samp_bout_filename
        data_samp_bout_file = open(data_samp_bout_filepath, "w")
        data_samp_bout_file.write("'Bout#','Bout_Start_Time','Bout_Side','Bout_Duration'")
        data_samp_bout_file.close()
        
        data_Choice_bout_filename = SOR_ID_Prompt.get() + "_Choice_Bout.csv"
        data_Choice_bout_filepath = data_file_dir + "\\" + data_Choice_bout_filename
        data_Choice_bout_file = open(data_Choice_bout_filepath, "w")
        data_Choice_bout_file.write("'Bout#','Bout_Start_Time','Bout_Side','Bout_Duration'")
        data_Choice_bout_file.close()

        data_samp_Summary_filename = SOR_ID_Prompt.get() + "_Samp_Summary.csv"
        data_samp_Summary_filepath = data_file_dir + "\\" + data_samp_Summary_filename
        data_samp_Summary_file = open(data_samp_Summary_filepath, "w")
        data_samp_Summary_file.write("'Date','Time','Animal_ID','Condition','Left_Object','Right_Object','Left_Explore_Total','Right_Explore_Total','Total_Exploration','Discrimination_Ratio'")
        data_samp_Summary_file.close()

        data_Choice_Summary_filename = SOR_ID_Prompt.get() + "_Choice_Summary.csv"
        data_Choice_Summary_filepath = data_file_dir + "\\" + data_Choice_Summary_filename
        data_Choice_Summary_file = open(data_Choice_Summary_filepath, "w")
        data_Choice_Summary_file.write("'Date','Time','Animal_ID','Condition','Left_Object','Right_Object','Novel_Side','Delay','Novel_Explore_Total','Familiar_Explore_Total','Total_Exploration','Discrimination_Ratio', '%d_Novel_Explore', '%d_Familiar_Explore','%d_Discrimination_Ratio'" % (SOR_Additional_Time,SOR_Additional_Time,SOR_Additional_Time))
        data_Choice_Summary_file.close()



        exp_file = open(exp_filepath, "w")
        exp_file.write("#Protocol Details#")
        exp_file.write("\n")
        exp_file.write("Protocol = SORv15")
        exp_file.write("\n")
        exp_file.write("Experiment_ID = '%s'" % (SOR_ID_Prompt.get()))
        exp_file.write("\n")
        exp_file.write("\n")
        exp_file.write("#Protocol Timepoints#")
        exp_file.write("\n")
        exp_file.write("Sample_Cut = %d" % (int(SOR_Sample_Cutoff_Prompt.get())))
        exp_file.write("\n")
        exp_file.write("Sample_Max = %d" % (int(SOR_Sample_Max_Prompt.get())))
        exp_file.write("\n")
        exp_file.write("Choice_Cut = %d" % (int(SOR_Choice_Cutoff_Prompt.get())))
        exp_file.write("\n")
        exp_file.write("Choice_Max = %d" % (int(SOR_Choice_Max_Prompt.get())))
        exp_file.write("\n")
        if len(SOR_Additional_Measure_Prompt.get()) != 0:
            exp_file.write("Additional_Measure = %d" % (int(SOR_Additional_Measure_Prompt.get())))
        if len(SOR_Additional_Measure_Prompt.get()) == 0:
            exp_file.write("Additional_Measure = 0")
        exp_file.write("\n")
        exp_file.write("\n")
        exp_file.write("#Conditions#")
        exp_file.write("\n")
        exp_file.write("Conditions = %s" % Conditions_List)
        exp_file.write("\n")
        exp_file.write("\n")
        exp_file.write("#Objects#")
        exp_file.write("\n")
        exp_file.write("Object_List = %s" % ObjectPairs_List)
        exp_file.write("\n")
        exp_file.write("\n")
        exp_file.write("#Keyboard#")
        exp_file.write("\n")
        exp_file.write("Keypress_Setup = %d" % (int(Key_Setting)))
        exp_file.write("\n")
        exp_file.write("Left_Keybind = '%s'" % Left_Keybind)
        exp_file.write("\n")
        exp_file.write("Right_Keybind = '%s'" % Right_Keybind)
        exp_file.write("\n")

        exp_file.close()
        top_SOR.destroy()

    ## Window Parameters - Create ##
    top_SOR = Toplevel()  # Establish Top/Primary Window
    global icon
    top_SOR.iconbitmap(icon)

    SOR_Title = Label(top_SOR, text="SOR Experiment Creator")
    SOR_Title.grid(row=1, column=2)

    SOR_ID_Label = Label(top_SOR, text="Experiment ID: ")
    SOR_ID_Label.grid(row=2, column=1)

    SOR_ID_Prompt = Entry(top_SOR)
    SOR_ID_Prompt.grid(row=2, column=3)

    SOR_Sample_Cutoff_Label = Label(top_SOR, text="Sample Exploration Cutoff (sec): ")
    SOR_Sample_Cutoff_Label.grid(row=3, column=1)

    SOR_Sample_Cutoff_Prompt = Entry(top_SOR, width=4)
    SOR_Sample_Cutoff_Prompt.grid(row=3, column=3)

    SOR_Sample_Max_Label = Label(top_SOR, text="Sample Exploration Maximum (sec): ")
    SOR_Sample_Max_Label.grid(row=4, column=1)

    SOR_Sample_Max_Prompt = Entry(top_SOR, width=4)
    SOR_Sample_Max_Prompt.grid(row=4, column=3)

    SOR_Choice_Cutoff_Label = Label(top_SOR, text="Choice Exploration Cutoff (sec): ")
    SOR_Choice_Cutoff_Label.grid(row=5, column=1)

    SOR_Choice_Cutoff_Prompt = Entry(top_SOR, width=4)
    SOR_Choice_Cutoff_Prompt.grid(row=5, column=3)

    SOR_Choice_Max_Label = Label(top_SOR, text="Choice Exploration Maximum (sec): ")
    SOR_Choice_Max_Label.grid(row=6, column=1)

    SOR_Choice_Max_Prompt = Entry(top_SOR, width=4)
    SOR_Choice_Max_Prompt.grid(row=6, column=3)

    SOR_Additional_Measure_Label = Label(top_SOR, text="Additional Measure Time (sec): ")
    SOR_Additional_Measure_Label.grid(row=7, column=1)

    SOR_Additional_Measure_Prompt = Entry(top_SOR, width=4)
    SOR_Additional_Measure_Prompt.grid(row=7,column=2)

    SOR_Condition_Button = Button(top_SOR, text="Conditions", command=SOR_Create_Condition)
    SOR_Condition_Button.grid(row=8, column=2)

    SOR_ObjectPairs_Button = Button(top_SOR, text="Object List", command=SOR_ObjectPairs)
    SOR_ObjectPairs_Button.grid(row=9, column=2)

    SOR_KeyBinding_Button = Button(top_SOR, text="Key Bindings", command=SOR_Keybind)
    SOR_KeyBinding_Button.grid(row=10, column=2)

    SOR_Finish_Button = Button(top_SOR, text="Finished", command=SOR_Finish)
    SOR_Finish_Button.grid(row=111, column=2)

    Key_Setting = 1

    ## Run Window Command ##
    top_SOR.mainloop()  # Run Main Window on Loop (Start)

    return

#####################################################################################################


## SOR Trial Setup ##
def Trial_Setup(Curr_Exp, Curr_Raw_Data):
    trial_import_data = str()
    class Trial_Create():
        def __init__(self, Curr_Exp):
            self.experiment_file = open(Curr_Exp, "r")
            self.experiment_file_contents = self.experiment_file.readlines()
            self.experiment_file_contents = [experiment_item.strip("\n") for experiment_item in
                                             self.experiment_file_contents]
            self.var_creation()

        def var_creation(self):
            self.Experiment_ID = str()
            self.Sample_Cut = int()
            self.Sample_Max = int()
            self.Choice_Cut = int()
            self.Choice_Max = int()
            self.Conditions = list()
            self.Object_List = list()
            self.Keypress_Setup = int()
            self.Left_Keybind = str()
            self.Right_Keybind = str()
            self.Delay = ""
            self.var_define()

        def var_define(self):
            self.current_exp_title = str(self.experiment_file_contents[2])
            self.current_exp_title = self.current_exp_title.strip("Experiment_ID = ")
            self.current_exp_title = self.current_exp_title.strip("'")
            self.Experiment_ID = self.current_exp_title

            self.current_samp_cut = str(self.experiment_file_contents[5])
            self.current_samp_cut = self.current_samp_cut.strip("Sample_Cut = ")
            self.Sample_Cut = self.current_samp_cut
            self.Sample_Cut = int(self.Sample_Cut)

            self.current_samp_max = str(self.experiment_file_contents[6])
            self.current_samp_max = self.current_samp_max.strip("Sample_Max = ")
            self.Sample_Max = self.current_samp_max
            self.Sample_Max = int(self.Sample_Max)

            self.current_choice_cut = str(self.experiment_file_contents[7])
            self.current_choice_cut = self.current_choice_cut.strip("Choice_Cut = ")
            self.Choice_Cut = self.current_choice_cut
            self.Choice_Cut = int(self.Choice_Cut)

            self.current_choice_max = str(self.experiment_file_contents[8])
            self.current_choice_max = self.current_choice_max.strip("Choice_Max = ")
            self.Choice_Max = self.current_choice_max
            self.Choice_Max = int(self.Choice_Max)

            self.additional_time = str(self.experiment_file_contents[9])
            self.additional_time = self.additional_time.strip("Additional_Measure = ")
            self.Additional_Measure = self.additional_time
            self.Additional_Measure = int(self.Additional_Measure)

            self.current_conditions_list = str(self.experiment_file_contents[12])
            self.current_conditions_list = self.current_conditions_list.strip("Conditions = [")
            self.current_conditions_list = self.current_conditions_list.strip("]")
            self.current_conditions_list = self.current_conditions_list.split(",")
            for condition in range(len(self.current_conditions_list)):
                self.current_conditions_list[condition] = self.current_conditions_list[condition].strip(" ")
                self.current_conditions_list[condition] = self.current_conditions_list[condition].strip("'")
            self.Conditions = self.current_conditions_list

            self.current_object_list = str(self.experiment_file_contents[15])
            self.current_object_list = self.current_object_list.strip("Object_List = [")
            self.current_object_list = self.current_object_list.strip("]")
            self.current_object_list = self.current_object_list.split(",")
            for objects in range(len(self.current_object_list)):
                self.current_object_list[objects] = self.current_object_list[objects].strip(" ")
                self.current_object_list[objects] = self.current_object_list[objects].strip("'")

            self.Object_List = self.current_object_list

            self.current_key_setting = str(self.experiment_file_contents[18])
            self.current_key_setting = self.current_key_setting.strip("Keypress_Setup = ")
            self.Keypress_Setup = self.current_key_setting
            self.Keypress_Setup = self.Keypress_Setup.strip("'")
            self.Keypress_Setup = int(self.Keypress_Setup)

            self.current_key_bind_left = str(self.experiment_file_contents[19])
            self.current_key_bind_left = self.current_key_bind_left.strip("Left_Keybind = ")
            self.Left_Keybind = self.current_key_bind_left
            self.Left_Keybind = self.Left_Keybind.strip("'")

            self.current_key_bind_right = str(self.experiment_file_contents[20])
            self.current_key_bind_right = self.current_key_bind_right.strip("Right_Keybind = ")
            self.Right_Keybind = self.current_key_bind_right
            self.Right_Keybind = self.Right_Keybind.strip("'")
            self.Trial_Setup_GUI()

        def Trial_Setup_GUI(self):
            self.top_run = Tk()
            global icon
            self.top_run.iconbitmap(icon)

            self.run_title = Label(self.top_run, text="Trial Setup")
            self.run_title.grid(row=1, column=2)

            self.run_ID_label = Label(self.top_run, text="Rat ID: ")
            self.run_ID_label.grid(row=2, column=1)

            self.run_ID_prompt = Entry(self.top_run)
            self.run_ID_prompt.grid(row=2, column=3)

            self.run_Drug_label = Label(self.top_run, text="Condition: ")
            self.run_Drug_label.grid(row=3, column=2)

            self.run_Drug_List = Listbox(self.top_run, selectmode=SINGLE, height=4, exportselection=FALSE)
            self.run_Drug_List.grid(row=4, column=2)
            for condition in self.Conditions:
                self.run_Drug_List.insert(END, condition)

            self.run_object_label = Label(self.top_run, text="Objects")
            self.run_object_label.grid(row=5, column=2)

            self.run_objectsamp_label = Label(self.top_run, text="Sample Object")
            self.run_objectsamp_label.grid(row=6, column=1)

            self.run_objectsamp_list = Listbox(self.top_run, selectmode=SINGLE, height=4, exportselection=FALSE)
            self.run_objectsamp_list.grid(row=7, column=1)
            for object in self.Object_List:
                self.run_objectsamp_list.insert(END, object)

            self.run_objectchoice_label = Label(self.top_run, text="Choice Object")
            self.run_objectchoice_label.grid(row=6, column=3)

            self.run_objectchoice_list = Listbox(self.top_run, selectmode=SINGLE, height=4, exportselection=FALSE)
            self.run_objectchoice_list.grid(row=7, column=3)
            for object in self.Object_List:
                self.run_objectchoice_list.insert(END, object)
            self.run_novel_label = Label(self.top_run, text="Novel Side")
            self.run_novel_label.grid(row=8, column=2)

            self.run_novel_side = IntVar()

            self.run_novel_left = Radiobutton(self.top_run, text="Left", variable=self.run_novel_side, value=1, command=self.setnovel1)
            self.run_novel_left.grid(row=9, column=1)

            self.run_novel_right = Radiobutton(self.top_run, text="Right", variable=self.run_novel_side, value=2, command=self.setnovel2)
            self.run_novel_right.grid(row=9, column=3)

            self.run_phase_choice = IntVar()

            self.run_phase_sample_only = Radiobutton(self.top_run, text="Sample", variable=self.run_phase_choice,
                                                     value=1, command=self.setphase1)
            self.run_phase_sample_only.grid(row=10, column=2)

            self.run_phase_choice_only = Radiobutton(self.top_run, text="Choice", variable=self.run_phase_choice,
                                                     value=2, command=self.setphase2)
            self.run_phase_choice_only.grid(row=11, column=2)

            self.run_phase_choice_both = Radiobutton(self.top_run, text="Sample/Choice", variable=self.run_phase_choice,
                                                     value=3, command=self.setphase3)
            self.run_phase_choice_both.grid(row=12, column=2)

            self.run_start_trial_button = Button(self.top_run, text="Start Trial", command=self.run_start_trial)
            self.run_start_trial_button.grid(row=13, column=2)

            self.run_start_trial_button = Button(self.top_run, text="Cancel", command=self.run_cancel_trial)
            self.run_start_trial_button.grid(row=14, column=2)

            self.run_trial_parameter_frame = LabelFrame(self.top_run, text="Trial Parameters")
            self.run_trial_parameter_frame.grid(row=15, column=2)

            self.parameter_frame_task = Label(self.run_trial_parameter_frame, text="Experiment Type: SORv11")
            self.parameter_frame_task.grid(row=16, column=1)

            self.parameter_frame_sample = Label(self.run_trial_parameter_frame,
                                                text="Sample: Max = %i , Cutoff = %i " % (
                                                    self.Sample_Max, self.Sample_Cut))
            self.parameter_frame_sample.grid(row=17, column=1)

            self.parameter_frame_choice = Label(self.run_trial_parameter_frame,
                                                text="Choice: Max = %i, Cutoff = %i" % (
                                                    self.Choice_Max, self.Choice_Cut))
            self.parameter_frame_choice.grid(row=18, column=1)

            self.top_run.mainloop()

        def run_start_trial(self):
            nonlocal trial_import_data

            self.trial_import_data = list()

            self.trial_import_data.append(self.Experiment_ID)

            self.trial_raw_ID = self.run_ID_prompt.get()
            self.trial_import_data.append(self.trial_raw_ID)

            self.run_phase_choice_value = self.run_phase_choice.get()
            if self.run_phase_choice_value == 1:
                self.trial_raw_phase = "Sample"
            if self.run_phase_choice_value == 2:
                self.trial_raw_phase = "Choice"
            if self.run_phase_choice_value == 3:
                self.trial_raw_phase = "Both"
            self.trial_import_data.append(self.trial_raw_phase)

            self.trial_raw_condition = str()
            self.trial_raw_condition_position = self.run_Drug_List.curselection()
            self.trial_raw_condition = self.run_Drug_List.get(self.trial_raw_condition_position[0])
            self.trial_import_data.append(self.trial_raw_condition)

            self.trial_raw_obj1 = str()
            self.trial_raw_obj1_position = self.run_objectsamp_list.curselection()
            self.trial_raw_obj1 = self.run_objectsamp_list.get(self.trial_raw_obj1_position[0])
            self.trial_import_data.append(self.trial_raw_obj1)

            self.trial_raw_obj2 = str()
            self.trial_raw_obj2_position = self.run_objectchoice_list.curselection()
            self.trial_raw_obj2 = self.run_objectchoice_list.get(self.trial_raw_obj2_position[0])
            self.trial_import_data.append(self.trial_raw_obj2)

            self.trial_import_data.append(self.Left_Keybind)

            self.trial_import_data.append(self.Right_Keybind)

            self.trial_import_data.append(self.Keypress_Setup)

            self.trial_import_data.append(self.Sample_Cut)

            self.trial_import_data.append(self.Sample_Max)

            self.trial_import_data.append(self.Choice_Cut)

            self.trial_import_data.append(self.Choice_Max)

            self.trial_import_data.append(self.Additional_Measure)

            self.trial_novel_side = self.run_novel_side.get()
            if self.trial_novel_side == 1:
                self.trial_novel = "Left"
            if self.trial_novel_side == 2:
                self.trial_novel = "Right"

            self.trial_import_data.append(self.trial_novel)
            trial_import_data = self.trial_import_data
            self.top_run.destroy()
            return self.trial_import_data

        def run_cancel_trial(self):
            self.top_run.destroy()
        def setphase1(self):
            self.run_phase_choice.set(1)
        def setphase2(self):
            self.run_phase_choice.set(2)
        def setphase3(self):
            self.run_phase_choice.set(3)
        def setnovel1(self):
            self.run_novel_side.set(1)
        def setnovel2(self):
            self.run_novel_side.set(2)

    class Active_Trial():

        def __init__(self, trial_data):
            self.trial_data = trial_data
            self.trial_expid = str(self.trial_data[0])
            self.trial_anid = str(self.trial_data[1])
            self.trial_phase = str(self.trial_data[2])
            self.trial_condition = str(self.trial_data[3])
            self.trial_obj1 = str(self.trial_data[4])
            self.trial_obj2 = str(self.trial_data[5])
            self.Left_Keybind = str(self.trial_data[6])
            self.Right_Keybind = str(self.trial_data[7])
            self.Keypress_Setup = int(self.trial_data[8])
            self.Sample_Cut = int(self.trial_data[9])
            self.Sample_Max = int(self.trial_data[10])
            self.Choice_Cut = int(self.trial_data[11])
            self.Choice_Max = int(self.trial_data[12])
            self.Additional_Measure = int(self.trial_data[13])
            self.Novel_Side = str(self.trial_data[14])
            self.trial_parameter_reset()
            self.run_window()

        def trial_parameter_reset(self):
            self.left_explore_total = 0
            self.right_explore_total = 0

            self.active_left_score = 0
            self.active_right_score = 0
            self.explore_total = 0

            self.time_elapsed = 0
            self.time_remaining = 0

            self.start_time = 0

            self.pause_start = 0
            self.pause_end = 0
            self.pause_length = 0

            self.bout_count = 0
            self.bout_start = 0
            self.bout_start_time = 0

            self.trial_active = False
            self.bout_active = False
            self.additional_calculated = False

            self.bout_explore = "Neither"
            self.pressed_key = ""

            self.trial_record = str()

            self.current_dir = os.getcwd()

        def run_window(self):
            self.trial_window = Tk()
            global icon
            self.trial_window.iconbitmap(icon)

            def trial_menu_start():
                self.trial_menu_pause_button.config(state="normal")
                self.trial_menu_start_button.config(state=DISABLED)
                self.trial_menu_restart_button.config(state="normal")
                self.trial_menu_finish_button.config(state="normal")

                self.trial_active = True

                self.start_time = time.time()
                self.start_date = time.strftime("%d %m %Y,%H:%M:%S")

            ## Finish Trial ##
            def trial_menu_finish():
                self.trial_finish()

            ## Cancel Trial ##
            def trial_menu_cancel():
                self.trial_window.destroy()

            ## Pause Trial ##
            def trial_menu_pause():

                if self.bout_active == False:
                    self.trial_active = False
                    self.pause_start = time.time()
                    self.trial_menu_resume_button.config(state="normal")
                    self.trial_menu_pause_button.config(state=DISABLED)
                if self.bout_active == True:
                    return

            ## Resume Trial ##
            def trial_menu_resume():
                self.pause_end = time.time()
                self.trial_active = True
                self.pause_length = self.pause_length + (self.pause_end - self.pause_start)
                self.trial_menu_resume_button.config(state=DISABLED)
                self.trial_menu_pause_button.config(state="normal")

            ## Restart Trial ##
            def trial_menu_restart():

                self.left_explore_total = 0
                self.right_explore_total = 0

                self.active_left_score = 0
                self.active_right_score = 0
                self.explore_total = 0

                self.time_elapsed = 0
                self.time_remaining = 0

                self.start_time = 0

                self.pause_start = 0
                self.pause_end = 0
                self.pause_length = 0

                self.bout_count = 0
                self.bout_start = 0
                self.bout_start_time = 0

                self.trial_active = False
                self.bout_active = False
                self.additional_calculated = False

                self.bout_explore = "Neither"
                self.pressed_key = ""

                self.trial_record = str()

                self.trial_menu_finish_button.config(state=DISABLED)
                self.trial_menu_restart_button.config(state=DISABLED)
                self.trial_menu_finish_button.config(state=DISABLED)
                self.trial_menu_pause_button.config(state=DISABLED)
                self.trial_menu_resume_button.config(state=DISABLED)
                self.trial_menu_start_button.config(state="normal")

                return

            ## Key Press Scoring ##


            def object_score_measures(event):
                self.pressed_key = event.char
                if self.Keypress_Setup == 1:
                    if (self.pressed_key == self.Left_Keybind) and (self.bout_active == False) and (
                                self.bout_explore == "Neither") and (
                                self.trial_active == True):
                        self.bout_count = self.bout_count + 1
                        self.bout_start = time.time() - self.pause_length
                        self.bout_start_time = self.bout_start - self.start_time
                        self.bout_explore = "Left"
                        self.bout_active = True
                        self.frame_left_explore_status.configure(bg='green')
                        self.left_explore_status.configure(bg='green')
                        self.pressed_key = ""
                    if (self.pressed_key == self.Left_Keybind) and (self.bout_active == True) and (
                                self.bout_explore == "Left") and (
                                self.trial_active == True):
                        self.bout_end = time.time() - self.pause_length
                        self.bout_length = self.bout_end - self.bout_start
                        self.left_explore_total = self.left_explore_total + self.bout_length
                        self.bout_details = "%f, %f, %s, %f" % (
                            self.bout_count, self.bout_start_time, self.bout_explore, self.bout_length)
                        if not self.trial_record:
                            self.trial_record = "\n" + "%s, %s, %s" % (self.trial_anid, self.start_date, self.trial_condition) + "\n" + self.bout_details
                        else:
                            self.trial_record = self.trial_record + "\n" + self.bout_details
                        self.bout_active = False
                        self.bout_explore = "Neither"
                        self.frame_left_explore_status.configure(bg='white')
                        self.left_explore_status.configure(bg='white')
                        self.pressed_key = ""
                    if (self.pressed_key == self.Right_Keybind) and (self.bout_active == False) and (
                                self.bout_explore == "Neither") and (
                                self.trial_active == True):
                        self.bout_count = self.bout_count + 1
                        self.bout_start = time.time() - self.pause_length
                        self.bout_start_time = self.bout_start - self.start_time - self.pause_length
                        self.bout_explore = "Right"
                        self.bout_active = True
                        self.frame_right_explore_status.configure(bg='green')
                        self.right_explore_status.configure(bg='green')
                        self.pressed_key = ""
                    if (self.pressed_key == self.Right_Keybind) and (self.bout_active == True) and (
                                self.bout_explore == "Right") and (
                                self.trial_active == True):
                        self.bout_end = time.time() - self.pause_length
                        self.bout_length = self.bout_end - self.bout_start
                        self.right_explore_total = self.right_explore_total + self.bout_length
                        self.bout_details = "%f, %f, %s, %f" % (
                            self.bout_count, self.bout_start_time, self.bout_explore, self.bout_length)
                        if not self.trial_record:
                            self.trial_record = "\n" + "%s, %s, %s" % (str(self.trial_anid), str(self.start_date),
                                                                 str(self.trial_condition)) + "\n" + self.bout_details
                        else:
                            self.trial_record = self.trial_record + "\n" + self.bout_details
                        self.bout_active = False
                        self.bout_explore = "Neither"
                        self.frame_right_explore_status.configure(bg='white')
                        self.right_explore_status.configure(bg='white')
                        self.pressed_key = ""
                if self.Keypress_Setup == 2:
                    if (self.pressed_key == self.Left_Keybind) and (self.bout_active == False) and (
                                self.bout_explore == "Neither") and (
                                self.trial_active == True):
                        self.bout_count = self.bout_count + 1
                        self.bout_start = time.time() - self.pause_length
                        self.bout_start_time = self.bout_start - self.start_time
                        self.bout_explore = "Left"
                        self.frame_left_explore_status.configure(bg='green')
                        self.left_explore_status.configure(bg='green')
                        self.bout_active = True
                    if (self.pressed_key == self.Right_Keybind) and (self.bout_active == False) and (
                                self.bout_explore == "Neither") and (
                                self.trial_active == True):
                        self.bout_count = self.bout_count + 1
                        self.bout_start = time.time() - self.pause_length
                        self.bout_start_time = self.bout_start - self.start_time
                        self.bout_explore = "Right"
                        self.frame_right_explore_status.configure(bg='green')
                        self.right_explore_status.configure(bg='green')
                        self.bout_active = True

            def object_score_release(event):
                if (self.pressed_key == self.Left_Keybind) and (self.bout_active == True) and (
                            self.bout_explore == "Left") and (self.trial_active == True):
                    self.bout_end = time.time() - self.pause_length
                    self.bout_length = self.bout_end - self.bout_start
                    self.left_explore_total = self.left_explore_total + self.bout_length
                    self.bout_details = "%f, %f, %s, %f" % (
                        self.bout_count, self.bout_start_time, self.bout_explore, self.bout_length)
                    if not self.trial_record:
                        self.trial_record = "\n" + "%s, %s, %s" % (str(self.trial_anid), str(self.start_date),
                                                             str(self.trial_condition)) + "\n" + self.bout_details
                    else:
                        self.trial_record = self.trial_record + "\n" + self.bout_details
                    self.bout_active = False
                    self.bout_explore = "Neither"
                    self.frame_left_explore_status.configure(bg='white')
                    self.left_explore_status.configure(bg='white')
                    self.pressed_key = ""
                if (self.pressed_key == self.Right_Keybind) and (self.bout_active == True) and (
                            self.bout_explore == "Right") and (self.trial_active == True):
                    self.bout_end = time.time() - self.pause_length
                    self.bout_length = self.bout_end - self.bout_start
                    self.right_explore_total = self.right_explore_total + self.bout_length
                    self.bout_details = "%f, %f, %s, %f" % (
                        self.bout_count, self.bout_start_time, self.bout_explore, self.bout_length)
                    if not self.trial_record:
                        self.trial_record = "\n" + "%s, %s, %s" % (str(self.trial_anid), str(self.start_date),
                                                             str(self.trial_condition)) + "\n" + self.bout_details
                    else:
                        self.trial_record = self.trial_record + "\n" + self.bout_details
                    self.bout_active = False
                    self.bout_explore = "Neither"
                    self.frame_right_explore_status.configure(bg='white')
                    self.right_explore_status.configure(bg='white')
                    self.pressed_key = ""

            def object_press_space(event):
                nonlocal trial_menu_pause
                nonlocal trial_menu_resume
                self.pressed_key == "<space>"
                if (self.pressed_key == "<space>") and (self.trial_active == True) and (self.time_elapsed > 0):
                    trial_menu_pause()
                    self.pressed_key = ""
                if (self.pressed_key == "<space>") and (self.trial_active == False) and (self.time_elapsed > 0):
                    trial_menu_resume()
                    self.pressed_key = ""

            ## Trial Menu Window ##

            self.left_explore_length_string = StringVar()
            self.left_explore_length_string.set(self.active_left_score)
            self.right_explore_length_string = StringVar()
            self.right_explore_length_string.set(str(self.active_right_score))
            self.time_elapsed_string = StringVar()
            self.time_elapsed_string.set(str(self.time_elapsed))
            self.time_remaining_string = StringVar()
            self.time_remaining_string.set(str(self.time_remaining))
            self.trial_menu_title = Label(self.trial_window, text="Active Trial Menu")
            self.trial_menu_title.grid(row=1, column=1)

            self.trial_menu_start_button = Button(self.trial_window, text="Start Trial", command=trial_menu_start)
            self.trial_menu_start_button.grid(row=1, column=2)

            self.trial_menu_finish_button = Button(self.trial_window, text="Finish Trial", command=trial_menu_finish,
                                                   state=DISABLED)
            self.trial_menu_finish_button.grid(row=2, column=2)

            self.trial_menu_cancel_button = Button(self.trial_window, text="Cancel Trial", command=trial_menu_cancel)
            self.trial_menu_cancel_button.grid(row=1, column=3)

            self.trial_menu_pause_button = Button(self.trial_window, text="Pause", command=trial_menu_pause,
                                                  state=DISABLED)
            self.trial_menu_pause_button.grid(row=1, column=4)

            self.trial_menu_resume_button = Button(self.trial_window, text="Resume", command=trial_menu_resume,
                                                   state=DISABLED)
            self.trial_menu_resume_button.grid(row=2, column=4)

            self.trial_menu_restart_button = Button(self.trial_window, text="Restart", command=trial_menu_restart,
                                                    state=DISABLED)
            self.trial_menu_restart_button.grid(row=2, column=3)

            ## Trial Status Window ##
            self.trial_status_var_elapsed_label = Label(self.trial_window, text="Time Elapsed")
            self.trial_status_var_elapsed_label.grid(row=3, column=1)
            self.trial_status_var_remaining_label = Label(self.trial_window, text="Time Remaining")
            self.trial_status_var_remaining_label.grid(row=3, column=2)
            self.trial_status_var_left_label = Label(self.trial_window, text="Left Explore")
            self.trial_status_var_left_label.grid(row=3, column=3)
            self.trial_status_var_right_label = Label(self.trial_window, text="Right Explore")
            self.trial_status_var_right_label.grid(row=3, column=4)
            self.trial_status_total_elapsed = Label(self.trial_window, textvariable=self.time_elapsed_string)
            self.trial_status_total_elapsed.grid(row=4, column=1)
            self.trial_status_total_remaining = Label(self.trial_window, textvariable=self.time_remaining_string)
            self.trial_status_total_remaining.grid(row=4, column=2)
            self.trial_status_left_elapsed = Label(self.trial_window, textvariable=self.left_explore_length_string)
            self.trial_status_left_elapsed.grid(row=4, column=3)
            self.trial_status_right_elapsed = Label(self.trial_window, textvariable=self.right_explore_length_string)
            self.trial_status_right_elapsed.grid(row=4, column=4)

            ## Object Exploration Status ##
            self.frame_left_explore_status = LabelFrame(self.trial_window, bg='white')
            self.frame_left_explore_status.grid(row=5, column=1)
            self.left_explore_status = Label(self.frame_left_explore_status, text="Left Object")
            self.left_explore_status.pack()

            self.frame_right_explore_status = LabelFrame(self.trial_window, bg='white')
            self.frame_right_explore_status.grid(row=5, column=4)
            self.right_explore_status = Label(self.frame_right_explore_status, text="Right Object")
            self.right_explore_status.pack()

            self.trial_window.bind("<Key>", object_score_measures)
            if (self.Keypress_Setup == 2):
                self.trial_window.bind("<KeyRelease>", object_score_release)
            self.trial_window.bind("<space>", object_press_space)

            self.trial_window.update()
            self.time_update()
            self.trial_window.mainloop()

        def time_update(self):
            if self.start_time == 0:
                self.time_elapsed = 0
            if (self.start_time != 0) and (self.trial_active == True):
                self.time_elapsed = time.time() - self.start_time - self.pause_length
            if (self.start_time != 0) and (self.trial_active == False):
                self.time_elapsed = self.time_elapsed
            if ((self.trial_phase == "Sample") or (self.trial_phase == "Both")) and (self.trial_active == True):
                self.time_remaining = self.Sample_Max - self.time_elapsed
            if (self.trial_phase == "Choice") and (self.trial_active == True):
                self.time_remaining = self.Choice_Max - self.time_elapsed
            if (self.trial_active == False):
                self.time_remaining = self.time_remaining
            if (self.trial_active == True) and (self.bout_active == True) and (self.bout_explore == "Left"):
                self.left_scoring = (time.time() - self.bout_start)
                self.active_left_score = self.left_explore_total + ((time.time() - self.pause_length) - self.bout_start)
            if (self.trial_active == True) and (self.bout_active == True) and (self.bout_explore == "Right"):
                self.right_scoring = (time.time() - self.bout_start)
                self.active_right_score = self.right_explore_total + ((time.time() - self.pause_length) - self.bout_start)
            if (self.time_elapsed >= self.Additional_Measure) and (self.Additional_Measure != 0) and (self.additional_calculated == False):
                self.additional_left = self.left_explore_total
                self.additional_right = self.right_explore_total
                if (self.Novel_Side == "Left"):
                    self.additional_novel = self.additional_left
                    self.additional_familiar = self.additional_right
                    if (self.additional_left == 0) and (self.additional_right > 0):
                        self.additional_discrim_ratio = 0
                    elif (self.additional_right == 0) and (self.additional_left > 0):
                        self.additional_discrim_ratio = 1
                    elif (self.additional_right == 0) and (self.additional_left == 0):
                        self.additional_discrim_ratio = 0
                    else:
                        self.additional_discrim_ratio = (self.additional_left - self.additional_right) / (self.additional_left + self.additional_right)
                elif (self.Novel_Side == "Right"):
                    self.additional_novel = self.additional_right
                    self.additional_familiar = self.additional_left
                    if (self.additional_left == 0) and (self.additional_right > 0):
                        self.additional_discrim_ratio = 1
                    elif (self.additional_right == 0) and (self.additional_left > 0):
                        self.additional_discrim_ratio = 0
                    elif (self.additional_right == 0) and (self.additional_left == 0):
                        self.additional_discrim_ratio = 0
                    else:
                        self.additional_discrim_ratio = (self.additional_right - self.additional_left) / (self.additional_left + self.additional_right)
                elif (self.Novel_Side == "NA"):
                    self.additional_novel = self.additional_left
                    self.additional_familiar = self.additional_right
                    if (self.additional_left == 0) and (self.additional_right > 0):
                        self.additional_discrim_ratio = 0
                    elif (self.additional_right == 0) and (self.additional_left > 0):
                        self.additional_discrim_ratio = 1
                    elif (self.additional_right == 0) and (self.additional_left == 0):
                        self.additional_discrim_ratio = 0
                    else:
                        self.additional_discrim_ratio = (self.additional_left - self.additional_right) / (self.additional_left + self.additional_right)
                self.additional_calculated = True
            if ((self.time_elapsed >= self.Sample_Max) and ((self.trial_phase == "Sample") or (self.trial_phase == "Both"))) or (
                        (self.time_elapsed >= self.Choice_Max) and (self.trial_phase == "Choice")):
                self.trial_finish()
            if (((self.active_left_score + self.active_right_score) >= self.Sample_Cut) and (
                    (self.trial_phase == "Sample") or (self.trial_phase == "Both"))) or (
                        ((self.active_left_score + self.active_right_score) >= self.Choice_Cut) and (
                                self.trial_phase == "Choice")):
                self.trial_finish()
            self.time_elapsed_string.set(round(self.time_elapsed, 2))
            self.time_remaining_string.set(round(self.time_remaining, 2))
            self.left_explore_length_string.set(round(self.active_left_score, 2))
            self.right_explore_length_string.set(round(self.active_right_score, 2))
            self.trial_window.after(10, self.time_update)


        def trial_finish(self):
            self.current_dir = os.getcwd()

            self.exp_folder = "\\Experiments"
            self.data_folder = "\\Data"
            self.protocol_folder = "\\Protocols"

            self.current_dir.replace("\\Protocols", "")
            self.experiment_dir = self.current_dir + self.exp_folder
            self.data_dir = self.current_dir + self.data_folder

            self.pressed_key = ""

            if (self.trial_phase == "Sample") or (self.trial_phase == "Choice"):
                self.Delay = "NA"

            if (self.trial_phase == "Sample") or (self.trial_phase == "Both"):
                self.bout_file = self.data_dir + "\\" + self.trial_expid + "\\" + self.trial_expid + "_Samp_Bout.csv"
                self.sum_file = self.data_dir + "\\" + self.trial_expid + "\\" + self.trial_expid + "_Samp_Summary.csv"
            if self.trial_phase == "Choice":
                self.bout_file = self.data_dir + "\\" + self.trial_expid + "\\" + self.trial_expid + "_Choice_Bout.csv"
                self.sum_file = self.data_dir + "\\" + self.trial_expid + "\\" + self.trial_expid + "_Choice_Summary.csv"
            if (self.trial_phase == "Sample") or (self.trial_phase == "Both"):
                self.active_bout = open(self.bout_file, 'a')
                self.active_bout.write(self.trial_record)
                self.active_bout.close()

                self.total_explore = self.left_explore_total + self.right_explore_total
                if (self.Novel_Side == "Left") and (self.total_explore > 0):
                    self.Discrimination_Ratio = (self.left_explore_total - self.right_explore_total) / (self.total_explore)
                if (self.Novel_Side == "Right") and (self.total_explore > 0):
                    self.Discrimination_Ratio = (self.right_explore_total - self.left_explore_total) / (self.total_explore)
                if (self.total_explore == 0):
                    self.Discrimination_Ratio = ""

                self.active_sum = open(self.sum_file, 'a')
                self.active_sum.write("\n")
                self.active_sum.write(self.start_date)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_anid)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_condition)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_obj1)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_obj2)
                self.active_sum.write(",")
                self.active_sum.write(str(self.left_explore_total))
                self.active_sum.write(",")
                self.active_sum.write(str(self.right_explore_total))
                self.active_sum.write(",")
                self.active_sum.write(str(self.total_explore))
                self.active_sum.write(",")
                self.active_sum.write(str(self.Discrimination_Ratio))


                self.active_sum.close()

            if self.trial_phase == "Choice":
                self.active_bout = open(self.bout_file, 'a')
                self.active_bout.write(self.trial_record)
                self.active_bout.close()

                self.total_explore = self.left_explore_total + self.right_explore_total
                if self.Novel_Side == "Left":
                    self.novel_explore = self.left_explore_total
                    self.familiar_explore = self.right_explore_total
                    self.Discrimination_Ratio = (self.left_explore_total - self.right_explore_total) / (
                    self.total_explore)
                if self.Novel_Side == "Right":
                    self.novel_explore = self.right_explore_total
                    self.familiar_explore = self.left_explore_total
                    self.Discrimination_Ratio = (self.right_explore_total - self.left_explore_total) / (
                    self.total_explore)

                self.active_sum = open(self.sum_file, 'a')
                self.active_sum.write("\n")
                self.active_sum.write(self.start_date)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_anid)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_condition)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_obj1)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_obj2)
                self.active_sum.write(",")
                self.active_sum.write(self.Novel_Side)
                self.active_sum.write(",")
                self.active_sum.write(str(self.Delay))
                self.active_sum.write(",")
                self.active_sum.write(str(self.novel_explore))
                self.active_sum.write(",")
                self.active_sum.write(str(self.familiar_explore))
                self.active_sum.write(",")
                self.active_sum.write(str(self.total_explore))
                self.active_sum.write(",")
                self.active_sum.write(str(self.Discrimination_Ratio))
                if (self.Additional_Measure > 0) and (self.Additional_Measure < self.time_elapsed):
                    self.active_sum.write(",")
                    self.active_sum.write(str(self.additional_novel))
                    self.active_sum.write(",")
                    self.active_sum.write(str(self.additional_familiar))
                    self.active_sum.write(",")
                    self.active_sum.write(str(self.additional_discrim_ratio))

                self.active_sum.close()

            if (self.trial_phase == "Sample") or (self.trial_phase == "Choice"):
                self.trial_window.destroy()
            if (self.trial_phase == "Both"):
                self.trial_window.destroy()
                self.trial_wait()

        def trial_wait(self):
            def trial_wait_start_choice():
                self.trial_phase = "Choice"
                self.Delay = self.trial_wait_time
                self.trial_wait_window.destroy()
                self.trial_parameter_reset()
                self.run_window()
            def trial_wait_cancel_choice():
                self.trial_wait_window.destroy()

            self.trial_wait_window = Tk()

            self.trial_wait_start = time.time()
            self.trial_wait_time = 0
            self.trial_wait_time_string = IntVar()
            self.trial_wait_time_string.set(0)

            self.trial_wait_title = Label(self.trial_wait_window, text="Delay Period")
            self.trial_wait_title.grid(row=1,column=1)

            self.trial_wait_time_display = Label(self.trial_wait_window, textvariable=self.trial_wait_time_string)
            self.trial_wait_time_display.grid(row=2,column=1)

            self.trial_wait_time_start = Button(self.trial_wait_window, text="Start Choice", command=trial_wait_start_choice)
            self.trial_wait_time_start.grid(row=3,column=1)

            self.trial_wait_time_cancel = Button(self.trial_wait_window,text="Cancel Choice", command=trial_wait_cancel_choice)
            self.trial_wait_time_cancel.grid(row=4,column=1)
            self.trial_wait_window.update_idletasks()
            self.trial_wait_window.update()
            self.trial_wait_update()
            self.trial_wait_window.mainloop()
        def trial_wait_update(self):
            self.trial_wait_time = time.time() - self.trial_wait_start
            self.trial_wait_time_string.set(round(self.trial_wait_time, 2))
            self.trial_wait_window.after(100, self.trial_wait_update)


    test = Trial_Create(Curr_Exp=Curr_Exp)
    while True:
        if isinstance(trial_import_data, list):
            Active_Trial(trial_data=trial_import_data)
            break
        else:
            pass