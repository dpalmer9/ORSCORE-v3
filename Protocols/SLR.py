## Module Import ##
import os
import time
import tkinter  ## Import Tkinter Modules
import msvcrt
from msvcrt import getch
from tkinter import *  ## Access Tkinter modules without calling to Tkinter
import tkinter.filedialog
from tkinter import filedialog
import csv
import threading
import imp
import pandas as pd
import numpy as np

#############################################################################################################
## Find Current Directory ##
current_dir = os.getcwd()

exp_folder = "\\Experiments"
data_folder = "\\Data"
protocol_folder = "\\Protocols"

current_dir.replace("\\Protocols","")
experiment_dir = current_dir + exp_folder
data_dir = current_dir + data_folder

icon = current_dir + "\\" + "Mouse_Icon.ico"
## SOR Variable List - Create ##
Conditions_List = list()
Condition_CSV_Create = 0
ObjectPairs_List = list()
Left_Keybind = "a"
Middle_Keybind = "j"
Right_Keybind = "l"
Key_Setting = "1"

## SOR - Create Experiment Function ##
def Create_Experiment():
    ## SOR Create Conditions ##
    def SOR_Create_Condition():
        condition_window = Toplevel()
        global icon
        condition_window.iconbitmap(icon)

        ## SOR Add Condition ##

        def condition_add():
            condition = condition_input.get()
            Conditions_List.append(condition)
            condition_list.insert(END, condition)
            condition_input.delete(0,END)

        ## SOR Remove Condition ##
        def condition_remove():
            condition = condition_list.curselection()
            condition_name = condition_list.get(condition[0])
            condition_pos = Conditions_List.index(condition_name)
            Conditions_List.remove(Conditions_List[condition_pos])
            condition_list.delete(condition[0])

        ## SOR Done ##
        def condition_done():
            global Condition_CSV_Create
            Condition_CSV_Create = int(condition_csv_create_var.get())
            condition_window.destroy()

        ## SLR Condition CSV ##
        def condition_csv_func():
            current_check_value = int(condition_csv_create_var.get())
            if current_check_value == 0:
                condition_list.config(state=NORMAL)
                condition_input.config(state=NORMAL)
                condition_add_button.config(state=NORMAL)
                condition_remove_button.config(state=NORMAL)
            if current_check_value == 1:
                condition_list.config(state='disabled')
                condition_input.config(state='disabled')
                condition_add_button.config(state='disabled')
                condition_remove_button.config(state='disabled')

            ## Window Setup##

        condition_title = Label(condition_window, text="Condition List")
        condition_title.grid(row=1, column=2)

        condition_list = Listbox(condition_window, selectmode=BROWSE)
        for condition in Conditions_List:
            condition_list.insert(END, condition)
        condition_list.grid(row=2, column=2)

        condition_input = Entry(condition_window)
        condition_input.grid(row=3, column=2)

        condition_csv_create_var = IntVar()
        condition_create_checkbox = Checkbutton(condition_window, text="Create CSV for Blind Conditions", variable=condition_csv_create_var, onvalue=1, offvalue=0, command=condition_csv_func)
        condition_create_checkbox.grid(row=4,column=2)

        condition_add_button = Button(condition_window, text="Add", command=condition_add)
        condition_add_button.grid(row=5, column=1)

        condition_remove_button = Button(condition_window, text="Remove", command=condition_remove)
        condition_remove_button.grid(row=5, column=3)

        condition_done_button = Button(condition_window, text="Done", command=condition_done)
        condition_done_button.grid(row=6, column=2)

        condition_window.focus_force()
        condition_window.mainloop()
        return

    ## SOR Object Pairs ##
    def SOR_ObjectPairs():
        objectpair_window = Toplevel()
        global icon
        objectpair_window.iconbitmap(icon)

        ## Add Object Pair ##
        def objectpair_add():
            object1 = objectpair_object1.get()
            objectpair_list.insert(END, object1)
            ObjectPairs_List.append(object1)
            objectpair_object1.delete(0,END)

        ## Remove Object Pair ##
        def objectpair_remove():
            removeset = objectpair_list.curselection()
            objectpair_identity_name = objectpair_list.get(removeset[0])
            objectpair_location = ObjectPairs_List.index(objectpair_identity_name)
            ObjectPairs_List.remove(ObjectPairs_List[objectpair_location])
            objectpair_list.delete(removeset[0])

        ## Done ##
        def objectpair_done():
            objectpair_window.destroy()

        ## Window Configuration ##

        objectpair_title = Label(objectpair_window, text="Object List")
        objectpair_title.grid(row=1, column=2)

        objectpair_list = Listbox(objectpair_window, selectmode=BROWSE)
        for pair in ObjectPairs_List:
            objectpair_list.insert(END, pair)
        objectpair_list.grid(row=2, column=2)

        objectpair_object1_label = Label(objectpair_window, text="Object")
        objectpair_object1_label.grid(row=3, column=2)

        objectpair_object1 = Entry(objectpair_window)
        objectpair_object1.grid(row=4, column=2)

        objectpair_add_button = Button(objectpair_window, text="Add", command=objectpair_add)
        objectpair_add_button.grid(row=5, column=2)

        objectpair_remove_button = Button(objectpair_window, text="Remove", command=objectpair_remove)
        objectpair_remove_button.grid(row=6, column=2)

        objectpair_done_button = Button(objectpair_window, text="Done", command=objectpair_done)
        objectpair_done_button.grid(row=7, column=2)

        objectpair_window.focus_force()
        objectpair_window.mainloop()

    ## Keybinding Menu ##
    def SOR_Keybind():
        top_keybind = Toplevel()
        global icon
        top_keybind.iconbitmap(icon)

        key_bind_right_string = StringVar()
        key_bind_right_string.set("l")

        key_bind_left_string = StringVar()
        key_bind_left_string.set("a")

        key_bind_middle_string = StringVar()
        key_bind_middle_string.set("j")

        ## Functions ##
        def keybind_done():
            nonlocal Key_Setting
            Key_Setting = key_func.get()
            top_keybind.destroy()

        def keybind_func_left():
            def key_press(event):
                global Left_Keybind
                key = event.char
                Left_Keybind = str(key)
                key_bind_left_string.set(Left_Keybind)
                top_keybind_left.destroy()
                return

            top_keybind_left = Toplevel()
            top_keybind_label = Label(top_keybind_left, text="Bind Left Key")
            top_keybind_label.grid(row=1, column=1)
            top_keybind_left.bind('<Key>', key_press)
            top_keybind_left.focus_force()
            top_keybind_left.mainloop()

        def keybind_func_middle():
            def key_press(event):
                global Middle_Keybind
                key = event.char
                Middle_Keybind = str(key)
                key_bind_middle_string.set(Middle_Keybind)
                top_keybind_middle.destroy()
                return

            top_keybind_middle = Toplevel()
            top_keybind_label = Label(top_keybind_middle, text="Bind Middle Key")
            top_keybind_label.grid(row=1, column=1)
            top_keybind_middle.bind('<Key>', key_press)
            top_keybind_middle.focus_force()
            top_keybind_middle.mainloop()
        def keybind_func_right():
            def key_press(event):
                global Right_Keybind
                key = event.char
                Right_Keybind = str(key)
                key_bind_right_string.set(Right_Keybind)
                top_keybind_right.destroy()
                return

            top_keybind_right = Toplevel()
            top_keybind_label = Label(top_keybind_right, text="Bind Right Key")
            top_keybind_label.grid(row=1, column=1)
            top_keybind_right.bind('<Key>', key_press)
            top_keybind_right.focus_force()
            top_keybind_right.mainloop()

        ## Window Configuration ##
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

        keybind_middle_label = Label(top_keybind, text="Middle Object Key")
        keybind_middle_label.grid(row=6, column=1)

        keybind_middle = Label(top_keybind, textvariable=key_bind_middle_string)
        keybind_middle.grid(row=6,column=2)

        keybind_middle_bind_button = Button(top_keybind, text="Bind", command=keybind_func_middle)
        keybind_middle_bind_button.grid(row=6,column=3)


        keybind_right_label = Label(top_keybind, text="Right Object Key")
        keybind_right_label.grid(row=7, column=1)

        keybind_right = Label(top_keybind, textvariable=key_bind_right_string)
        keybind_right.grid(row=7, column=2)

        keybind_right_bind_button = Button(top_keybind, text="Bind", command= keybind_func_right)
        keybind_right_bind_button.grid(row=7, column=3)

        keybind_done_button = Button(top_keybind, text="Done", command=keybind_done)
        keybind_done_button.grid(row=8, column=2)

        top_keybind.focus_force()
        top_keybind.mainloop()


    ## Finish: Save Function ##
    def SOR_Finish():
        nonlocal Key_Setting
        global Condition_CSV_Create
        exp_filename = SOR_ID_Prompt.get() + ".ORe"
        data_raw_filename = SOR_ID_Prompt.get() + "_Raw.csv"
        data_raw_filepath = data_dir + "\\" + data_raw_filename


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
        data_samp_Summary_file.write("'Date','Time','Animal_ID','Condition','Left_Object','Middle_Object','Right_Object','Left_Explore_Total','Middle_Explore_Total','Right_Explore_Total','Total_Exploration','Object_Preference'")
        data_samp_Summary_file.close()

        data_Choice_Summary_filename = SOR_ID_Prompt.get() + "_Choice_Summary.csv"
        data_Choice_Summary_filepath = data_file_dir + "\\" + data_Choice_Summary_filename
        data_Choice_Summary_file = open(data_Choice_Summary_filepath, "w")
        data_Choice_Summary_file.write("'Date','Time','Animal_ID','Condition','Left_Object','Right_Object','Novel_Side','Delay','Novel_Explore_Total','Familiar_Explore_Total','Total_Exploration','Discrimination_Ratio', '%d_Novel_Explore', '%d_Familiar_Explore','%d_Discrimination_Ratio'" % (int(SOR_Additional_Measure_Prompt.get()),int(SOR_Additional_Measure_Prompt.get()),int(SOR_Additional_Measure_Prompt.get())))
        data_Choice_Summary_file.close()



        exp_file = open(exp_filepath, "w")
        exp_file.write("#Protocol Details#")
        exp_file.write("\n")
        exp_file.write("Protocol = SLR")
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
        if SOR_Additional_Measure_Prompt.get() != "":
            exp_file.write("Additional_Measure = %d" % (int(SOR_Additional_Measure_Prompt.get())))
        if SOR_Additional_Measure_Prompt.get() == "":
            exp_file.write("Additional_Measure = 0")
        exp_file.write("\n")
        exp_file.write("\n")
        exp_file.write("#Conditions#")
        exp_file.write("\n")
        exp_file.write("Create_CSV = %d" % (Condition_CSV_Create))
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
        exp_file.write("Middle_Keybind = '%s'" % Middle_Keybind)
        exp_file.write("\n")
        exp_file.write("Right_Keybind = '%s'" % Right_Keybind)
        exp_file.write("\n")


        exp_file.close()

        if Condition_CSV_Create == 1:
            condition_csv_filepath = data_file_dir + "\\" + "Conditions.csv"
            condition_csv_file = open(condition_csv_filepath, "w")
            condition_csv_file.write("[Conditions]")
            condition_csv_file.write("\n")
            condition_csv_file.write("AnimalID,Trial#,NovelSide(Left or Right/NA if not known)")
            condition_csv_file.close()

        top_SOR.destroy()

    ## Window Parameters - Create ##
    top_SOR = Toplevel()  # Establish Top/Primary Window
    global icon
    top_SOR.iconbitmap(icon)

    SOR_Title = Label(top_SOR, text="SLR Experiment Creator")
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
            self.Condition_Csv = int()
            self.Conditions = list()
            self.Object_List = list()
            self.Keypress_Setup = int()
            self.Left_Keybind = str()
            self.Middle_Keybind = str()
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

            self.current_condition_csv = str(self.experiment_file_contents[12])
            self.current_condition_csv = self.current_condition_csv.strip("Create_CSV = ")
            self.Condition_Csv = self.current_condition_csv
            self.Condition_Csv = int(self.Condition_Csv)

            self.current_conditions_list = str(self.experiment_file_contents[13])
            self.current_conditions_list = self.current_conditions_list.strip("Conditions = [")
            self.current_conditions_list = self.current_conditions_list.strip("]")
            self.current_conditions_list = self.current_conditions_list.split(",")
            for condition in range(len(self.current_conditions_list)):
                self.current_conditions_list[condition] = self.current_conditions_list[condition].strip(" ")
                self.current_conditions_list[condition] = self.current_conditions_list[condition].strip("'")
            self.Conditions = self.current_conditions_list

            self.current_object_list = str(self.experiment_file_contents[16])
            self.current_object_list = self.current_object_list.strip("Object_List = [")
            self.current_object_list = self.current_object_list.strip("]")
            self.current_object_list = self.current_object_list.split(",")
            for objects in range(len(self.current_object_list)):
                self.current_object_list[objects] = self.current_object_list[objects].strip(" ")
                self.current_object_list[objects] = self.current_object_list[objects].strip("'")

            self.Object_List = self.current_object_list

            self.current_key_setting = str(self.experiment_file_contents[19])
            self.current_key_setting = self.current_key_setting.strip("Keypress_Setup = ")
            self.Keypress_Setup = self.current_key_setting
            self.Keypress_Setup = self.Keypress_Setup.strip("'")
            self.Keypress_Setup = int(self.Keypress_Setup)

            self.current_key_bind_left = str(self.experiment_file_contents[20])
            self.current_key_bind_left = self.current_key_bind_left.strip("Left_Keybind = ")
            self.Left_Keybind = self.current_key_bind_left
            self.Left_Keybind = self.Left_Keybind.strip("'")

            self.current_key_bind_middle = str(self.experiment_file_contents[21])
            self.current_key_bind_middle = self.current_key_bind_middle.strip("Middle_Keybind = ")
            self.Middle_Keybind = self.current_key_bind_middle
            self.Middle_Keybind = self.Middle_Keybind.strip("'")

            self.current_key_bind_right = str(self.experiment_file_contents[22])
            self.current_key_bind_right = self.current_key_bind_right.strip("Right_Keybind = ")
            self.Right_Keybind = self.current_key_bind_right
            self.Right_Keybind = self.Right_Keybind.strip("'")

            if self.Condition_Csv == 1:
                self.current_dir = os.getcwd()
                self.current_dir = self.current_dir.replace("\\Protocols","")
                self.data_dir = self.current_dir + "\\" + "Data" + "\\" + self.Experiment_ID
                self.condition_filepath = self.data_dir + "\\" + "Conditions.csv"
                self.Condition_Csv_File = open(self.condition_filepath, "r")
                self.Conditions_read = self.Condition_Csv_File.readlines()
                self.Conditions_read = [a.replace("\n","") for a in self.Conditions_read]
                self.Conditions_title = self.Conditions_read[1].split(',')
                self.Conditions_data = self.Conditions_read[2:]
                self.Conditions_data = [list(a.split(',')) for a in self.Conditions_data]
                self.Conditions_table = pd.DataFrame(self.Conditions_data, columns=self.Conditions_title)
                self.Conditions_ID = self.Conditions_table['AnimalID'].tolist()
                self.Conditions_ID = list(set(self.Conditions_ID))
                self.Conditions_TrialNum = self.Conditions_table['Trial#'].tolist()
                self.Conditions_TrialNum = list(set(self.Conditions_TrialNum))

            self.Trial_Setup_GUI()

        def Trial_Setup_GUI(self):
            self.top_run = Tk()
            global icon
            self.top_run.iconbitmap(icon)

            self.run_title = Label(self.top_run, text="Trial Setup")
            self.run_title.grid(row=1, column=2)

            self.run_ID_label = Label(self.top_run, text="Rat ID: ")
            self.run_ID_label.grid(row=2, column=1)

            if self.Condition_Csv == 0:
                self.run_ID_prompt = Entry(self.top_run)
                self.run_ID_prompt.grid(row=2, column=3)
            if self.Condition_Csv == 1:
                self.run_ID_prompt = Listbox(self.top_run, selectmode=SINGLE,height=5,exportselection=FALSE)
                self.run_ID_prompt.grid(row=2,column=3)
                for id in self.Conditions_ID:
                    self.run_ID_prompt.insert(END,id)
            if self.Condition_Csv == 0:
                self.run_Drug_label = Label(self.top_run, text="Condition: ")
            if self.Condition_Csv == 1:
                self.run_Drug_label = Label(self.top_run, text="Trial#: ")
            self.run_Drug_label.grid(row=3, column=2)

            self.run_Drug_List = Listbox(self.top_run, selectmode=SINGLE, height=4, exportselection=FALSE)
            self.run_Drug_List.grid(row=4, column=2)
            if self.Condition_Csv == 0:
                for condition in self.Conditions:
                    self.run_Drug_List.insert(END, condition)
            if self.Condition_Csv == 1:
                for trial in self.Conditions_TrialNum:
                    self.run_Drug_List.insert(END, trial)

            self.run_object_label = Label(self.top_run, text="Objects")
            self.run_object_label.grid(row=5, column=2)

            self.run_objectleft_label = Label(self.top_run, text="Left Object")
            self.run_objectleft_label.grid(row=6, column=1)

            self.run_objectleft_list = Listbox(self.top_run, selectmode=SINGLE, height=4, exportselection=FALSE)
            self.run_objectleft_list.grid(row=7, column=1)
            for object in self.Object_List:
                self.run_objectleft_list.insert(END, object)

            self.run_objectmid_label = Label(self.top_run, text="Middle Object")
            self.run_objectmid_label.grid(row=6, column=2)

            self.run_objectmid_list = Listbox(self.top_run, selectmode=SINGLE, height=4, exportselection=FALSE)
            self.run_objectmid_list.grid(row=7, column=2)
            for object in self.Object_List:
                self.run_objectmid_list.insert(END, object)

            self.run_objectright_label = Label(self.top_run, text="Right Object")
            self.run_objectright_label.grid(row=6, column=3)

            self.run_objectright_list = Listbox(self.top_run, selectmode=SINGLE, height=4, exportselection=FALSE)
            self.run_objectright_list.grid(row=7, column=3)
            for object in self.Object_List:
                self.run_objectright_list.insert(END, object)


            if self.Condition_Csv == 0:
                self.run_novel_label = Label(self.top_run, text="Novel Side")
                self.run_novel_label.grid(row=8, column=2)

                self.run_novel_side = IntVar()

                self.run_novel_left = Radiobutton(self.top_run, text="Left", variable=self.run_novel_side, value=1,
                                                  command=self.setnovel1)
                self.run_novel_left.grid(row=9, column=1)

                self.run_novel_right = Radiobutton(self.top_run, text="Right", variable=self.run_novel_side, value=2,
                                                   command=self.setnovel2)
                self.run_novel_right.grid(row=9, column=3)

                self.run_slr_label = Label(self.top_run, text = "SLR Trial Type")
                self.run_slr_label.grid(row=10,column=2)

                self.run_slr_type = IntVar()
                self.run_slr_d = Radiobutton(self.top_run, text="d-SLR", variable=self.run_slr_d_func, value=1, command=self.run_slr_d_func)
                self.run_slr_d.grid(row=11,column=1)

                self.run_slr_s = Radiobutton(self.top_run, text="s-SLR", variable=self.run_slr_s_func, value=2, command=self.run_slr_s_func)
                self.run_slr_s.grid(row=11,column=3)


            self.run_phase_choice = IntVar()

            self.run_phase_sample_only = Radiobutton(self.top_run, text="Sample", variable=self.run_phase_choice,
                                                     value=1, command=self.setphase1)
            self.run_phase_sample_only.grid(row=12, column=2)

            self.run_phase_choice_only = Radiobutton(self.top_run, text="Choice", variable=self.run_phase_choice,
                                                     value=2, command=self.setphase2)
            self.run_phase_choice_only.grid(row=13, column=2)

            self.run_phase_choice_both = Radiobutton(self.top_run, text="Sample/Choice", variable=self.run_phase_choice,
                                                     value=3, command=self.setphase3)
            self.run_phase_choice_both.grid(row=14, column=2)

            self.run_start_trial_button = Button(self.top_run, text="Start Trial", command=self.run_start_trial)
            self.run_start_trial_button.grid(row=15, column=2)

            self.run_start_trial_button = Button(self.top_run, text="Cancel", command=self.run_cancel_trial)
            self.run_start_trial_button.grid(row=16, column=2)

            self.run_trial_parameter_frame = LabelFrame(self.top_run, text="Trial Parameters")
            self.run_trial_parameter_frame.grid(row=16, column=2)

            self.parameter_frame_task = Label(self.run_trial_parameter_frame, text="Experiment Type: SLRv10")
            self.parameter_frame_task.grid(row=17, column=1)

            self.parameter_frame_sample = Label(self.run_trial_parameter_frame,
                                                text="Sample: Max = %i , Cutoff = %i " % (
                                                    self.Sample_Max, self.Sample_Cut))
            self.parameter_frame_sample.grid(row=18, column=1)

            self.parameter_frame_choice = Label(self.run_trial_parameter_frame,
                                                text="Choice: Max = %i, Cutoff = %i" % (
                                                    self.Choice_Max, self.Choice_Cut))
            self.parameter_frame_choice.grid(row=19, column=1)

            self.top_run.mainloop()

        def run_start_trial(self):
            nonlocal trial_import_data

            self.trial_import_data = list()
            if self.Condition_Csv == 1:
                self.trial_raw_ID_position = self.run_ID_prompt.curselection()
                self.trial_num_position = self.run_Drug_List.curselection()
                self.trial_raw_ID = str(self.run_ID_prompt.get(self.trial_raw_ID_position[0]))
                self.trial_num = str(self.run_Drug_List.get(self.trial_num_position[0]))
                self.trial_raw_condition = "NA"
                self.trial_novel = self.Conditions_table.loc[(self.Conditions_table['AnimalID'] == self.trial_raw_ID) & (self.Conditions_table['Trial#'] == self.trial_num), 'NovelSide(Left or Right/NA if not known)'].to_string(index=False)
                self.SLR_Trial_Type = "NA"

            self.trial_import_data.append(self.Experiment_ID)

            if self.Condition_Csv == 0:
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

            if self.Condition_Csv == 0:
                self.trial_raw_condition = str()
                self.trial_raw_condition_position = self.run_Drug_List.curselection()
                self.trial_raw_condition = self.run_Drug_List.get(self.trial_raw_condition_position[0])

            self.trial_import_data.append(self.trial_raw_condition)

            self.trial_raw_left = str()
            self.trial_raw_left_position = self.run_objectleft_list.curselection()
            self.trial_raw_left = self.run_objectleft_list.get(self.trial_raw_left_position[0])
            self.trial_import_data.append(self.trial_raw_left)

            self.trial_raw_mid = str()
            self.trial_raw_mid_position = self.run_objectmid_list.curselection()
            self.trial_raw_mid = self.run_objectmid_list.get(self.trial_raw_mid_position[0])
            self.trial_import_data.append(self.trial_raw_mid)

            self.trial_raw_right = str()
            self.trial_raw_right_position = self.run_objectright_list.curselection()
            self.trial_raw_right = self.run_objectright_list.get(self.trial_raw_right_position[0])
            self.trial_import_data.append(self.trial_raw_right)

            self.trial_import_data.append(self.Left_Keybind)

            self.trial_import_data.append(self.Middle_Keybind)

            self.trial_import_data.append(self.Right_Keybind)

            self.trial_import_data.append(self.Keypress_Setup)

            self.trial_import_data.append(self.Sample_Cut)

            self.trial_import_data.append(self.Sample_Max)

            self.trial_import_data.append(self.Choice_Cut)

            self.trial_import_data.append(self.Choice_Max)

            self.trial_import_data.append(self.Additional_Measure)

            if self.Condition_Csv == 0:
                self.run_slr_type_choice = self.run_slr_type.get()
                if self.run_slr_type_choice == 1:
                    self.SLR_Trial_Type = "d-SLR"
                if self.run_slr_type_choice == 2:
                    self.SLR_Trial_Type = "s-SLR"

            if self.Condition_Csv == 0:
                self.trial_novel_side = self.run_novel_side.get()
                if self.trial_novel_side == 1:
                    self.trial_novel = "Left"
                if self.trial_novel_side == 2:
                    self.trial_novel = "Right"

            self.trial_import_data.append(self.trial_novel)
            self.trial_import_data.append(self.SLR_Trial_Type)
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
        def run_slr_d_func(self):
            self.run_slr_type.set(1)
        def run_slr_s_func(self):
            self.run_slr_type.set(2)

    class Active_Trial():

        def __init__(self, trial_data):
            self.trial_data = trial_data
            self.trial_expid = str(self.trial_data[0])
            self.trial_anid = str(self.trial_data[1])
            self.trial_phase = str(self.trial_data[2])
            self.trial_condition = str(self.trial_data[3])
            self.trial_objleft = str(self.trial_data[4])
            self.trial_objmiddle = str(self.trial_data[5])
            self.trial_objright = str(self.trial_data[6])
            self.Left_Keybind = str(self.trial_data[7])
            self.Middle_Keybind = str(self.trial_data[8])
            self.Right_Keybind = str(self.trial_data[9])
            self.Keypress_Setup = int(self.trial_data[10])
            self.Sample_Cut = int(self.trial_data[11])
            self.Sample_Max = int(self.trial_data[12])
            self.Choice_Cut = int(self.trial_data[13])
            self.Choice_Max = int(self.trial_data[14])
            self.Additional_Measure = int(self.trial_data[15])
            self.Novel_Side = str(self.trial_data[16])
            self.SLR_Trial_Type = str(self.trial_data[17])
            self.trial_parameter_reset()
            self.run_window()

        def trial_parameter_reset(self):
            self.left_explore_total = 0
            self.right_explore_total = 0
            self.middle_explore_total = 0

            self.active_left_score = 0
            self.active_right_score = 0
            self.active_middle_score = 0
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

            self.additional_left = 0
            self.additional_right = 0

            self.trial_active = False
            self.bout_active = False

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

                self.bout_explore = "Neither"
                self.trial_record = str()

                self.left_explore_total = 0
                self.right_explore_total = 0
                self.middle_explore_total = 0

                self.active_left_score = 0
                self.active_right_score = 0
                self.active_middle_score = 0
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

                self.additional_left = 0
                self.additional_right = 0

                self.trial_active = False
                self.bout_active = False

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
                        self.bout_end = time.time()
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
                    if (self.pressed_key == self.Middle_Keybind) and (self.bout_active == False) and (
                                self.bout_explore == "Neither") and (
                                self.trial_active == True) and ((self.trial_phase == "Sample") or (self.trial_phase == "Both")):
                        self.bout_count = self.bout_count + 1
                        self.bout_start = time.time() - self.pause_length
                        self.bout_start_time = self.bout_start - self.start_time
                        self.bout_explore = "Middle"
                        self.bout_active = True
                        self.frame_middle_explore_status.configure(bg='green')
                        self.middle_explore_status.configure(bg='green')
                        self.pressed_key = ""
                    if (self.pressed_key == self.Middle_Keybind) and (self.bout_active == True) and (
                                self.bout_explore == "Middle") and (
                                self.trial_active == True) and ((self.trial_phase == "Sample") or (self.trial_phase == "Both")):
                        self.bout_end = time.time() - self.pause_length
                        self.bout_length = self.bout_end - self.bout_start
                        self.middle_explore_total = self.middle_explore_total + self.bout_length
                        self.bout_details = "%f, %f, %s, %f" % (
                            self.bout_count, self.bout_start_time, self.bout_explore, self.bout_length)
                        if not self.trial_record:
                            self.trial_record = "\n" + "%s, %s, %s" % (self.trial_anid, self.start_date, self.trial_condition) + "\n" + self.bout_details
                        else:
                            self.trial_record = self.trial_record + "\n" + self.bout_details
                        self.bout_active = False
                        self.bout_explore = "Neither"
                        self.frame_middle_explore_status.configure(bg='white')
                        self.middle_explore_status.configure(bg='white')
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
                    if (self.pressed_key == self.Middle_Keybind) and (self.bout_active == False) and (
                                self.bout_explore == "Neither") and (
                                self.trial_active == True) and ((self.trial_phase == "Sample") or (self.trial_phase == "Both")):
                        self.bout_count = self.bout_count + 1
                        self.bout_start = time.time() - self.pause_length
                        self.bout_start_time = self.bout_start - self.start_time
                        self.bout_explore = "Middle"
                        self.frame_middle_explore_status.configure(bg='green')
                        self.middle_explore_status.configure(bg='green')
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
                if (self.pressed_key == self.Middle_Keybind) and (self.bout_active == True) and (
                            self.bout_explore == "Middle") and (self.trial_active == True) and ((self.trial_phase == "Sample") or (self.trial_phase == "Both")):
                    self.bout_end = time.time() - self.pause_length
                    self.bout_length = self.bout_end - self.bout_start
                    self.middle_explore_total = self.middle_explore_total + self.bout_length
                    self.bout_details = "%f, %f, %s, %f" % (
                        self.bout_count, self.bout_start_time, self.bout_explore, self.bout_length)
                    if not self.trial_record:
                        self.trial_record = "\n" + "%s, %s, %s" % (str(self.trial_anid), str(self.start_date),
                                                             str(self.trial_condition)) + "\n" + self.bout_details
                    else:
                        self.trial_record = self.trial_record + "\n" + self.bout_details
                    self.bout_active = False
                    self.bout_explore = "Neither"
                    self.frame_middle_explore_status.configure(bg='white')
                    self.middle_explore_status.configure(bg='white')
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
            self.middle_explore_length_string = StringVar()
            self.middle_explore_length_string.set(self.active_middle_score)
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
            if self.trial_phase != "Choice":
                self.trial_status_var_middle_label = Label(self.trial_window, text="Middle Explore")
                self.trial_status_var_middle_label.grid(row=3, column=4)
            self.trial_status_var_right_label = Label(self.trial_window, text="Right Explore")
            self.trial_status_var_right_label.grid(row=3, column=5)
            self.trial_status_total_elapsed = Label(self.trial_window, textvariable=self.time_elapsed_string)
            self.trial_status_total_elapsed.grid(row=4, column=1)
            self.trial_status_total_remaining = Label(self.trial_window, textvariable=self.time_remaining_string)
            self.trial_status_total_remaining.grid(row=4, column=2)
            self.trial_status_left_elapsed = Label(self.trial_window, textvariable=self.left_explore_length_string)
            self.trial_status_left_elapsed.grid(row=4, column=3)
            if self.trial_phase != "Choice":
                self.trial_status_middle_elapsed = Label(self.trial_window, textvariable=self.middle_explore_length_string)
                self.trial_status_middle_elapsed.grid(row=4, column=4)
            self.trial_status_right_elapsed = Label(self.trial_window, textvariable=self.right_explore_length_string)
            self.trial_status_right_elapsed.grid(row=4, column=5)

            ## Object Exploration Status ##
            self.frame_left_explore_status = LabelFrame(self.trial_window, bg='white')
            self.frame_left_explore_status.grid(row=5, column=2)
            self.left_explore_status = Label(self.frame_left_explore_status, text="Left Object")
            self.left_explore_status.pack()

            if self.trial_phase != "Choice":
                self.frame_middle_explore_status = LabelFrame(self.trial_window, bg='white')
                self.frame_middle_explore_status.grid(row=5, column=3)
                self.middle_explore_status = Label(self.frame_middle_explore_status, text="Middle Object")
                self.middle_explore_status.pack()

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
            if (self.trial_active == True) and (self.bout_active == True) and (self.bout_explore == "Middle"):
                self.middle_scoring = (time.time() - self.bout_start)
                self.active_middle_score = self.middle_explore_total + ((time.time() - self.pause_length) - self.bout_start)
            if (self.trial_active == True) and (self.bout_active == True) and (self.bout_explore == "Right"):
                self.right_scoring = (time.time() - self.bout_start)
                self.active_right_score = self.right_explore_total + ((time.time() - self.pause_length) - self.bout_start)

            if (self.time_elapsed >= self.Additional_Measure) and (self.Additional_Measure != 0):
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
                self.Additional_Measure = 0
            if ((self.time_elapsed >= self.Sample_Max) and ((self.trial_phase == "Sample") or (self.trial_phase == "Both"))) or (
                        (self.time_elapsed >= self.Choice_Max) and (self.trial_phase == "Choice")):
                self.trial_finish()
            if (((self.active_left_score + self.active_right_score + self.active_middle_score) >= self.Sample_Cut) and (
                    (self.trial_phase == "Sample") or (self.trial_phase == "Both"))) or (
                        ((self.active_left_score + self.active_right_score + self.active_middle_score) >= self.Choice_Cut) and (
                                self.trial_phase == "Choice")):
                self.trial_finish()
            self.time_elapsed_string.set(round(self.time_elapsed, 2))
            self.time_remaining_string.set(round(self.time_remaining, 2))
            self.left_explore_length_string.set(round(self.active_left_score, 2))
            self.middle_explore_length_string.set(round(self.active_middle_score, 2))
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

                self.total_explore = self.left_explore_total + self.right_explore_total + self.middle_explore_total
                if self.total_explore > 0:
                    self.Discrimination_Ratio = (self.left_explore_total) / (self.total_explore)
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
                self.active_sum.write(self.trial_objleft)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_objmiddle)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_objright)
                self.active_sum.write(",")
                self.active_sum.write(str(self.left_explore_total))
                self.active_sum.write(",")
                self.active_sum.write(str(self.middle_explore_total))
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
                if self.Novel_Side == "NA":
                    self.novel_explore = self.left_explore_total
                    self.familiar_explore = self.right_explore_total
                    self.Discrimination_Ratio = (self.left_explore_total - self.right_explore_total) / (
                    self.total_explore)

                self.active_sum = open(self.sum_file, 'a')
                self.active_sum.write("\n")
                self.active_sum.write(self.start_date)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_anid)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_condition)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_objleft)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_objright)
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
