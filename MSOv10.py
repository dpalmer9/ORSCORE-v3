## Module Import ##
import os
import time
import tkinter  ## Import Tkinter Modules
import msvcrt
from msvcrt import getch
from tkinter import *  ## Access Tkinter modules without calling to Tkinter
import csv
import threading
import imp

#############################################################################################################
## Find Current Directory ##
current_dir = os.getcwd()

exp_folder = "\\Experiments"
data_folder = "\\Data"
protocol_folder = "\\Protocols"

current_dir.replace("\\Protocols","")
experiment_dir = current_dir + exp_folder
data_dir = current_dir + data_folder

## SOR Variable List - Create ##
Conditions_List = list()
ObjectPairs_List = list()
Keybind_1 = "F"
Keybind_2 = "J"
Keybind_3 = "K"
Keybind_4 = "L"
Keybind_5 = ";"
Numkey_Setting = 1
Key_Setting = 1

## SOR - Create Experiment Function ##
def Create_Experiment():
    ## SOR Create Conditions ##
    def SOR_Create_Condition():
        condition_window = Toplevel()

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
            condition_window.destroy()

            ## Window Setup##

        condition_title = Label(condition_window, text="Condition List")
        condition_title.grid(row=1, column=2)

        condition_list = Listbox(condition_window, selectmode=BROWSE)
        for condition in Conditions_List:
            condition_list.insert(END, condition)
        condition_list.grid(row=2, column=2)

        condition_input = Entry(condition_window)
        condition_input.grid(row=3, column=2)

        condition_add_button = Button(condition_window, text="Add", command=condition_add)
        condition_add_button.grid(row=4, column=1)

        condition_remove_button = Button(condition_window, text="Remove", command=condition_remove)
        condition_remove_button.grid(row=4, column=3)

        condition_done_button = Button(condition_window, text="Done", command=condition_done)
        condition_done_button.grid(row=5, column=2)

        condition_window.focus_force()
        condition_window.mainloop()
        return

    ## SOR Object Pairs ##
    def SOR_ObjectPairs():
        objectpair_window = Toplevel()

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


        key_bind_1_string = StringVar()
        key_bind_1_string.set("f")

        key_bind_2_string = StringVar()
        key_bind_2_string.set("j")

        key_bind_3_string = StringVar()
        key_bind_3_string.set("k")

        key_bind_4_string = StringVar()
        key_bind_4_string.set("l")

        key_bind_5_string = StringVar()
        key_bind_5_string.set(";")

        ## Functions ##
        def keybind_done():
            global Key_Setting
            global Numkey_Setting
            Numkey_Setting = num_key_setting.get()
            Key_Setting = key_func.get()
            top_keybind.destroy()

        def keybind_func_1():
            def key_press(event):
                global Keybind_1
                key = event.char
                Keybind_1 = str(key)
                key_bind_1_string.set(Keybind_1)
                top_keybind_1.destroy()
                return

            top_keybind_1 = Toplevel()
            top_keybind_label = Label(top_keybind_1, text="Bind Object 1 Key")
            top_keybind_label.grid(row=1, column=1)
            top_keybind_1.bind('<Key>', key_press)
            top_keybind_1.focus_force()
            top_keybind_1.mainloop()
            
        def keybind_func_2():
            def key_press(event):
                global Keybind_2
                key = event.char
                Keybind_2 = str(key)
                key_bind_2_string.set(Keybind_2)
                top_keybind_2.destroy()
                return

            top_keybind_2 = Toplevel()
            top_keybind_label = Label(top_keybind_2, text="Bind Object 2 Key")
            top_keybind_label.grid(row=1, column=1)
            top_keybind_2.bind('<Key>', key_press)
            top_keybind_2.focus_force()
            top_keybind_2.mainloop()
            
        def keybind_func_3():
            def key_press(event):
                global Keybind_3
                key = event.char
                Keybind_3 = str(key)
                key_bind_3_string.set(Keybind_3)
                top_keybind_3.destroy()
                return

            top_keybind_3 = Toplevel()
            top_keybind_label = Label(top_keybind_3, text="Bind Object 3 Key")
            top_keybind_label.grid(row=1, column=1)
            top_keybind_3.bind('<Key>', key_press)
            top_keybind_3.focus_force()
            top_keybind_3.mainloop()
            
        def keybind_func_4():
            def key_press(event):
                global Keybind_4
                key = event.char
                Keybind_4 = str(key)
                key_bind_4_string.set(Keybind_4)
                top_keybind_4.destroy()
                return

            top_keybind_4 = Toplevel()
            top_keybind_label = Label(top_keybind_4, text="Bind Object 4 Key")
            top_keybind_label.grid(row=1, column=1)
            top_keybind_4.bind('<Key>', key_press)
            top_keybind_4.focus_force()
            top_keybind_4.mainloop()
            
        def keybind_func_5():
            def key_press(event):
                global Keybind_5
                key = event.char
                Keybind_5 = str(key)
                key_bind_5_string.set(Keybind_5)
                top_keybind_5.destroy()
                return

            top_keybind_5 = Toplevel()
            top_keybind_label = Label(top_keybind_5, text="Bind Object 5 Key")
            top_keybind_label.grid(row=1, column=1)
            top_keybind_5.bind('<Key>', key_press)
            top_keybind_5.focus_force()
            top_keybind_5.mainloop()

        def keybind_2select():
            global Keybind_2
            global Keybind_3
            global Keybind_4
            global Keybind_1
            global Keybind_5
            keybind_2_bind_button.config(state=DISABLED)
            keybind_3_bind_button.config(state=DISABLED)
            keybind_4_bind_button.config(state=DISABLED)
            key_bind_2_string.set("")
            key_bind_3_string.set("")
            key_bind_4_string.set("")
            key_bind_1_string.set('a')
            key_bind_5_string.set('l')
            Keybind_2 = ""
            Keybind_3 = ""
            Keybind_4 = ""
            Keybind_1 = "a"
            Keybind_5 = "l"
            keybind_string_obj1.set("Normal Explore Key")
            keybind_string_obj5.set("Odd Explore Key")
            keybind_string_obj2.set("")
            keybind_string_obj3.set("")
            keybind_string_obj4.set("")

        def keybind_5select():
            global Keybind_2
            global Keybind_3
            global Keybind_4
            global Keybind_1
            global Keybind_5
            keybind_2_bind_button.config(state="normal")
            keybind_3_bind_button.config(state="normal")
            keybind_4_bind_button.config(state="normal")
            key_bind_2_string.set("j")
            key_bind_3_string.set("k")
            key_bind_4_string.set("l")
            key_bind_1_string.set('f')
            key_bind_5_string.set(';')
            Keybind_1 = "f"
            Keybind_2 = "j"
            Keybind_3 = "k"
            Keybind_4 = "l"
            Keybind_5 = ";"
            keybind_string_obj1.set("Object 1 Key")
            keybind_string_obj2.set("Object 2 Key")
            keybind_string_obj3.set("Object 3 Key")
            keybind_string_obj4.set("Object 4 Key")
            keybind_string_obj5.set("Object 5 Key")





        ## Window Configuration ##
        keybind_string_obj1 = StringVar()
        keybind_string_obj1.set("Object 1 Key")
        keybind_string_obj2 = StringVar()
        keybind_string_obj2.set("Object 2 Key")
        keybind_string_obj3 = StringVar()
        keybind_string_obj3.set("Object 3 Key")
        keybind_string_obj4 = StringVar()
        keybind_string_obj4.set("Object 4 Key")
        keybind_string_obj5 = StringVar()
        keybind_string_obj5.set("Object 5 Key")

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

        num_key_setting = IntVar()

        keybind_radio_5keys = Radiobutton(top_keybind, text="5 Scoring Keys", variable=num_key_setting, value=1,command=keybind_5select)
        keybind_radio_5keys.grid(row=5,column=1)

        keybind_radio_2keys = Radiobutton(top_keybind, text="2 Scoring Keys", variable=num_key_setting,value=2,command=keybind_2select)
        keybind_radio_2keys.grid(row=6,column=1)

        keybind_1_label = Label(top_keybind, textvariable=keybind_string_obj1)
        keybind_1_label.grid(row=7, column=1)

        keybind_1 = Label(top_keybind, textvariable=key_bind_1_string)
        keybind_1.grid(row=7, column=2)

        keybind_1_bind_button = Button(top_keybind, text="Bind", command=keybind_func_1)
        keybind_1_bind_button.grid(row=7, column=3)

        keybind_2_label = Label(top_keybind, textvariable=keybind_string_obj2)
        keybind_2_label.grid(row=8, column=1)

        keybind_2 = Label(top_keybind, textvariable=key_bind_2_string)
        keybind_2.grid(row=8, column=2)

        keybind_2_bind_button = Button(top_keybind, text="Bind", command=keybind_func_2)
        keybind_2_bind_button.grid(row=8, column=3)
        
        keybind_3_label = Label(top_keybind, textvariable=keybind_string_obj3)
        keybind_3_label.grid(row=9, column=1)

        keybind_3 = Label(top_keybind, textvariable=key_bind_3_string)
        keybind_3.grid(row=9, column=2)

        keybind_3_bind_button = Button(top_keybind, text="Bind", command=keybind_func_3)
        keybind_3_bind_button.grid(row=9, column=3)
        
        keybind_4_label = Label(top_keybind, textvariable=keybind_string_obj4)
        keybind_4_label.grid(row=10, column=1)

        keybind_4 = Label(top_keybind, textvariable=key_bind_4_string)
        keybind_4.grid(row=10, column=2)

        keybind_4_bind_button = Button(top_keybind, text="Bind", command=keybind_func_4)
        keybind_4_bind_button.grid(row=10, column=3)
        
        keybind_5_label = Label(top_keybind, textvariable=keybind_string_obj5)
        keybind_5_label.grid(row=11, column=1)

        keybind_5 = Label(top_keybind, textvariable=key_bind_5_string)
        keybind_5.grid(row=11, column=2)

        keybind_5_bind_button = Button(top_keybind, text="Bind", command=keybind_func_5)
        keybind_5_bind_button.grid(row=11, column=3)


        keybind_done_button = Button(top_keybind, text="Done", command=keybind_done)
        keybind_done_button.grid(row=12, column=2)

        top_keybind.focus_force()
        top_keybind.mainloop()


    ## Finish: Save Function ##
    def SOR_Finish():
        global Key_Setting
        global Numkey_Setting
        exp_filename = SOR_ID_Prompt.get() + ".ORe"
        data_raw_filename = SOR_ID_Prompt.get() + "_Raw.csv"
        data_raw_filepath = data_dir + "\\" + data_raw_filename


        exp_filepath = experiment_dir + "\\" + exp_filename
        data_file_dir = data_dir + "\\" + SOR_ID_Prompt.get()
        os.makedirs(data_file_dir)

        data_samp_bout_filename = SOR_ID_Prompt.get() + "_Bout.csv"
        data_samp_bout_filepath = data_file_dir + "\\" + data_samp_bout_filename
        data_samp_bout_file = open(data_samp_bout_filepath, "w")
        data_samp_bout_file.write("'Bout#','Bout_Start_Time','Object_Explored','Bout_Duration'")
        data_samp_bout_file.close()


        data_samp_Summary_filename = SOR_ID_Prompt.get() + "_Summary.csv"
        data_samp_Summary_filepath = data_file_dir + "\\" + data_samp_Summary_filename
        data_samp_Summary_file = open(data_samp_Summary_filepath, "w")
        if Numkey_Setting == 1:
            data_samp_Summary_file.write(
                "'Start_Date','Time','Animal_ID','Condition','Modality','Object_Set_A','Object_Set_B','Odd_Object', 'Odd_Object_Position', 'Object_1_Explore', 'Object_2_Explore', 'Object_3_Explore', 'Object_4_Explore', 'Object_5_Explore','Total_Explore', 'Oddity_Ratio'")
        if Numkey_Setting == 2:
            data_samp_Summary_file.write(
                "'Start_Date','Time','Animal_ID','Condition','Modality','Object_Set_A','Object_Set_B','Odd_Object', 'Odd_Object_Position', 'Normal_Explore', 'Odd_Explore','Total_Explore', 'Oddity_Ratio'")

        data_samp_Summary_file.close()




        exp_file = open(exp_filepath, "w")
        exp_file.write("#Protocol Details#")
        exp_file.write("\n")
        exp_file.write("Protocol = MSOv10")
        exp_file.write("\n")
        exp_file.write("Experiment_ID = '%s'" % (SOR_ID_Prompt.get()))
        exp_file.write("\n")
        exp_file.write("\n")
        exp_file.write("#Protocol Timepoints#")
        exp_file.write("\n")
        exp_file.write("Explore_Cut = %d" % (int(SOR_Sample_Cutoff_Prompt.get())))
        exp_file.write("\n")
        exp_file.write("Explore_Max = %d" % (int(SOR_Sample_Max_Prompt.get())))
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
        exp_file.write("Numkey_Setup = %d" % (int(Numkey_Setting)))
        exp_file.write("\n")
        exp_file.write("Keybind_1 = '%s'" % Keybind_1)
        exp_file.write("\n")
        exp_file.write("Keybind_2 = '%s'" % Keybind_2)
        exp_file.write("\n")
        exp_file.write("Keybind_3 = '%s'" % Keybind_3)
        exp_file.write("\n")
        exp_file.write("Keybind_4 = '%s'" % Keybind_4)
        exp_file.write("\n")
        exp_file.write("Keybind_5 = '%s'" % Keybind_5)
        exp_file.write("\n")


        exp_file.close()
        top_SOR.destroy()

    ## Window Parameters - Create ##
    top_SOR = Toplevel()  # Establish Top/Primary Window

    SOR_Title = Label(top_SOR, text="MSO Experiment Creator")
    SOR_Title.grid(row=1, column=2)

    SOR_ID_Label = Label(top_SOR, text="Experiment ID: ")
    SOR_ID_Label.grid(row=2, column=1)

    SOR_ID_Prompt = Entry(top_SOR)
    SOR_ID_Prompt.grid(row=2, column=3)

    SOR_Sample_Cutoff_Label = Label(top_SOR, text="Exploration Cutoff (sec): ")
    SOR_Sample_Cutoff_Label.grid(row=3, column=1)

    SOR_Sample_Cutoff_Prompt = Entry(top_SOR, width=4)
    SOR_Sample_Cutoff_Prompt.grid(row=3, column=3)

    SOR_Sample_Max_Label = Label(top_SOR, text="Exploration Maximum (sec): ")
    SOR_Sample_Max_Label.grid(row=4, column=1)

    SOR_Sample_Max_Prompt = Entry(top_SOR, width=4)
    SOR_Sample_Max_Prompt.grid(row=4, column=3)

    SOR_Condition_Button = Button(top_SOR, text="Conditions", command=SOR_Create_Condition)
    SOR_Condition_Button.grid(row=5, column=2)

    SOR_ObjectPairs_Button = Button(top_SOR, text="Object List", command=SOR_ObjectPairs)
    SOR_ObjectPairs_Button.grid(row=6, column=2)

    SOR_KeyBinding_Button = Button(top_SOR, text="Key Bindings", command=SOR_Keybind)
    SOR_KeyBinding_Button.grid(row=7, column=2)

    SOR_Finish_Button = Button(top_SOR, text="Finished", command=SOR_Finish)
    SOR_Finish_Button.grid(row=8, column=2)

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
            self.Explore_Cut = int()
            self.Explore_Max = int()
            self.Conditions = list()
            self.Object_List = list()
            self.Keypress_Setup = int()
            self.Numkey_Setup = int()
            self.Keybind_1 = str()
            self.Keybind_2 = str()
            self.Keybind_3 = str()
            self.Keybind_4 = str()
            self.Keybind_5 = str()
            self.var_define()

        def var_define(self):
            self.current_exp_title = str(self.experiment_file_contents[2])
            self.current_exp_title = self.current_exp_title.strip("Experiment_ID = ")
            self.current_exp_title = self.current_exp_title.strip("'")
            self.Experiment_ID = self.current_exp_title

            self.current_samp_cut = str(self.experiment_file_contents[5])
            self.current_samp_cut = self.current_samp_cut.strip("Explore_Cut = ")
            self.Explore_Cut = self.current_samp_cut
            self.Explore_Cut = int(self.Explore_Cut)

            self.current_samp_max = str(self.experiment_file_contents[6])
            self.current_samp_max = self.current_samp_max.strip("Explore_Max = ")
            self.Explore_Max = self.current_samp_max
            self.Explore_Max = int(self.Explore_Max)



            self.current_conditions_list = str(self.experiment_file_contents[9])
            self.current_conditions_list = self.current_conditions_list.strip("Conditions = [")
            self.current_conditions_list = self.current_conditions_list.strip("]")
            self.current_conditions_list = self.current_conditions_list.split(",")
            for condition in range(len(self.current_conditions_list)):
                self.current_conditions_list[condition] = self.current_conditions_list[condition].strip(" ")
                self.current_conditions_list[condition] = self.current_conditions_list[condition].strip("'")
            self.Conditions = self.current_conditions_list

            self.current_object_list = str(self.experiment_file_contents[12])
            self.current_object_list = self.current_object_list.strip("Object_List = [")
            self.current_object_list = self.current_object_list.strip("]")
            self.current_object_list = self.current_object_list.split(",")
            for objects in range(len(self.current_object_list)):
                self.current_object_list[objects] = self.current_object_list[objects].strip(" ")
                self.current_object_list[objects] = self.current_object_list[objects].strip("'")

            self.Object_List = self.current_object_list

            self.current_key_setting = str(self.experiment_file_contents[15])
            self.current_key_setting = self.current_key_setting.strip("Keypress_Setup = ")
            self.Keypress_Setup = self.current_key_setting
            self.Keypress_Setup = self.Keypress_Setup.strip("'")
            self.Keypress_Setup = int(self.Keypress_Setup)

            self.current_numkey_setting = str(self.experiment_file_contents[16])
            self.current_numkey_setting = self.current_numkey_setting.strip("Numkey_Setup = ")
            self.Numkey_Setup = self.current_numkey_setting
            self.Numkey_Setup = self.Numkey_Setup.strip("'")
            self.Numkey_Setup = int(self.Numkey_Setup)

            self.current_key_bind_1 = str(self.experiment_file_contents[17])
            self.current_key_bind_1 = self.current_key_bind_1.strip("Keybind_1 = ")
            self.Keybind_1 = self.current_key_bind_1
            self.Keybind_1 = self.Keybind_1.strip("'")
            
            self.current_key_bind_2 = str(self.experiment_file_contents[18])
            self.current_key_bind_2 = self.current_key_bind_2.strip("Keybind_2 = ")
            self.Keybind_2 = self.current_key_bind_2
            self.Keybind_2 = self.Keybind_2.strip("'")
            
            self.current_key_bind_3 = str(self.experiment_file_contents[19])
            self.current_key_bind_3 = self.current_key_bind_3.strip("Keybind_3 = ")
            self.Keybind_3 = self.current_key_bind_3
            self.Keybind_3 = self.Keybind_3.strip("'")
            
            self.current_key_bind_4 = str(self.experiment_file_contents[20])
            self.current_key_bind_4 = self.current_key_bind_4.strip("Keybind_4 = ")
            self.Keybind_4 = self.current_key_bind_4
            self.Keybind_4 = self.Keybind_4.strip("'")
            
            self.current_key_bind_5 = str(self.experiment_file_contents[21])
            self.current_key_bind_5 = self.current_key_bind_5.strip("Keybind_5 = ")
            self.Keybind_5 = self.current_key_bind_5
            self.Keybind_5 = self.Keybind_5.strip("'")


            self.Trial_Setup_GUI()

        def Trial_Setup_GUI(self):
            self.top_run = Tk()
            global current_dir
            self.top_run.iconbitmap

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

            self.run_objectpair1_label = Label(self.top_run, text="Pair 1")
            self.run_objectpair1_label.grid(row=6, column=1)

            self.run_objectpair1_list = Listbox(self.top_run, selectmode=SINGLE, height=4, exportselection=FALSE)
            self.run_objectpair1_list.grid(row=7, column=1)
            for object in self.Object_List:
                self.run_objectpair1_list.insert(END, object)

            self.run_objectpair2_label = Label(self.top_run, text="Pair 2")
            self.run_objectpair2_label.grid(row=6, column=2)

            self.run_objectpair2_list = Listbox(self.top_run, selectmode=SINGLE, height=4, exportselection=FALSE)
            self.run_objectpair2_list.grid(row=7, column=2)
            for object in self.Object_List:
                self.run_objectpair2_list.insert(END, object)

            self.run_objectodd_label = Label(self.top_run, text="Odd Object")
            self.run_objectodd_label.grid(row=6, column=3)

            self.run_objectodd_list = Listbox(self.top_run, selectmode=SINGLE, height=4, exportselection=FALSE)
            self.run_objectodd_list.grid(row=7, column=3)
            for object in self.Object_List:
                self.run_objectodd_list.insert(END, object)
            self.run_novel_label = Label(self.top_run, text="MSO Trial Type")
            self.run_novel_label.grid(row=8, column=2)

            self.run_mso_type = IntVar()

            self.run_mso_tactile = Radiobutton(self.top_run, text="Tactile", variable=self.run_mso_type, value=1,
                                               command=self.msotactile)
            self.run_mso_tactile.grid(row=9, column=1)

            self.run_mso_visual = Radiobutton(self.top_run, text="Visual", variable=self.run_mso_type, value=2,
                                              command=self.msovisual)
            self.run_mso_visual.grid(row=9, column=2)

            self.run_mso_multi = Radiobutton(self.top_run, text="Multimodal", variable=self.run_mso_type, value=3,
                                             command=self.msomulti)
            self.run_mso_multi.grid(row=10, column=1)

            self.run_mso_olfactory = Radiobutton(self.top_run, text="Olfactory", variable=self.run_mso_type, value=4,
                                                 command=self.msoolf)
            self.run_mso_olfactory.grid(row=9, column=3)

            self.run_odd_object_posotion_label = Label(self.top_run, text="Odd Object Position")
            self.run_odd_object_posotion_label.grid(row=11, column=2)
            self.run_odd_object_position_list = Spinbox(self.top_run, from_=1, to=5)
            self.run_odd_object_position_list.grid(row=12, column=2)

            self.run_start_trial_button = Button(self.top_run, text="Start Trial", command=self.run_start_trial)
            self.run_start_trial_button.grid(row=13, column=2)

            self.run_start_trial_button = Button(self.top_run, text="Cancel", command=self.run_cancel_trial)
            self.run_start_trial_button.grid(row=14, column=2)

            self.run_trial_parameter_frame = LabelFrame(self.top_run, text="Trial Parameters")
            self.run_trial_parameter_frame.grid(row=15, column=2)

            self.parameter_frame_task = Label(self.run_trial_parameter_frame, text="Experiment Type: SORv11")
            self.parameter_frame_task.grid(row=16, column=1)

            self.parameter_frame_sample = Label(self.run_trial_parameter_frame,
                                                text="Max = %i , Cutoff = %i " % (
                                                    self.Explore_Max, self.Explore_Cut))
            self.parameter_frame_sample.grid(row=17, column=1)

            self.top_run.mainloop()

        def run_start_trial(self):
            nonlocal trial_import_data

            if self.Numkey_Setup == 2:
                self.Keybind_2 = ""
                self.Keybind_3 = ""
                self.Keybind_4 = ""

            self.trial_import_data = list()

            self.trial_import_data.append(self.Experiment_ID)

            self.trial_raw_ID = self.run_ID_prompt.get()
            self.trial_import_data.append(self.trial_raw_ID)

            self.run_modality_value = self.run_mso_type.get()
            if self.run_modality_value == 1:
                self.trial_raw_phase = "Tactile"
            elif self.run_modality_value == 2:
                self.trial_raw_phase = "Visual"
            elif self.run_modality_value == 3:
                self.trial_raw_phase = "Multimodal"
            elif self.run_modality_value == 4:
                self.trial_raw_phase == "Olfactory"
            self.trial_import_data.append(self.trial_raw_phase)

            self.trial_raw_condition = str()
            self.trial_raw_condition_position = self.run_Drug_List.curselection()
            self.trial_raw_condition = self.run_Drug_List.get(self.trial_raw_condition_position[0])
            self.trial_import_data.append(self.trial_raw_condition)

            self.trial_raw_obj1 = str()
            self.trial_raw_obj1_position = self.run_objectpair1_list.curselection()
            self.trial_raw_obj1 = self.run_objectpair1_list.get(self.trial_raw_obj1_position[0])
            self.trial_import_data.append(self.trial_raw_obj1)

            self.trial_raw_obj2 = str()
            self.trial_raw_obj2_position = self.run_objectpair2_list.curselection()
            self.trial_raw_obj2 = self.run_objectpair2_list.get(self.trial_raw_obj2_position[0])
            self.trial_import_data.append(self.trial_raw_obj2)

            self.trial_raw_odd = str()
            self.trial_raw_odd_position = self.run_objectodd_list.curselection()
            self.trial_raw_odd = self.run_objectodd_list.get(self.trial_raw_odd_position[0])
            self.trial_import_data.append(self.trial_raw_odd)

            self.trial_import_data.append(self.Keybind_1)

            self.trial_import_data.append(self.Keybind_2)

            self.trial_import_data.append(self.Keybind_3)

            self.trial_import_data.append(self.Keybind_4)

            self.trial_import_data.append(self.Keybind_5)

            self.trial_import_data.append(self.Keypress_Setup)

            self.trial_import_data.append(self.Numkey_Setup)

            self.trial_import_data.append(self.Explore_Cut)

            self.trial_import_data.append(self.Explore_Max)

            self.trial_import_data.append(int(self.run_odd_object_position_list.get()))


            trial_import_data = self.trial_import_data
            self.top_run.destroy()
            return self.trial_import_data

        def run_cancel_trial(self):
            self.top_run.destroy()

        def msotactile(self):
            self.run_mso_type.set(1)
        def msovisual(self):
            self.run_mso_type.set(2)
        def msomulti(self):
            self.run_mso_type.set(3)

    class Active_Trial():

        def __init__(self, trial_data):
            self.trial_data = trial_data
            self.trial_expid = str(self.trial_data[0])
            self.trial_anid = str(self.trial_data[1])
            self.trial_mode = str(self.trial_data[2])
            self.trial_condition = str(self.trial_data[3])
            self.trial_obj1 = str(self.trial_data[4])
            self.trial_obj2 = str(self.trial_data[5])
            self.trial_objodd = str(self.trial_data[6])
            self.Keybind_1 = str(self.trial_data[7])
            self.Keybind_2 = str(self.trial_data[8])
            self.Keybind_3 = str(self.trial_data[9])
            self.Keybind_4 = str(self.trial_data[10])
            self.Keybind_5 = str(self.trial_data[11])
            self.Keypress_Setup = int(self.trial_data[12])
            self.Numkey_Setup = int(self.trial_data[13])
            self.Explore_Cut = int(self.trial_data[14])
            self.Explore_Max = int(self.trial_data[15])
            self.Odd_Position = int(self.trial_data[16])
            self.trial_parameter_reset()
            self.run_window()

        def trial_parameter_reset(self):
            self.explore_1_total = 0
            self.explore_2_total = 0
            self.explore_3_total = 0
            self.explore_4_total = 0
            self.explore_5_total = 0
            self.active_explore_1 = 0
            self.active_explore_2 = 0
            self.active_explore_3 = 0
            self.active_explore_4 = 0
            self.active_explore_5 = 0

            self.normal_explore_total = 0
            self.odd_explore_total = 0
            self.active_explore_normal = 0
            self.active_explore_odd = 0

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

            self.bout_explore = "Neither"

            self.trial_record = str()

            self.current_dir = os.getcwd()

        def run_window(self):
            self.trial_window = Tk()

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

                self.explore_1_total = 0
                self.explore_2_total = 0
                self.explore_3_total = 0
                self.explore_4_total = 0
                self.explore_5_total = 0
                self.active_explore_1 = 0
                self.active_explore_2 = 0
                self.active_explore_3 = 0
                self.active_explore_4 = 0
                self.active_explore_5 = 0

                self.normal_explore_total = 0
                self.odd_explore_total = 0
                self.active_explore_normal = 0
                self.active_explore_odd = 0

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

                self.bout_explore = "Neither"

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
                if self.Numkey_Setup == 1:
                    if self.Keypress_Setup == 1:
                        if (self.pressed_key == self.Keybind_1) and (self.bout_active == False) and (
                                    self.bout_explore == "Neither") and (
                                    self.trial_active == True):
                            self.bout_count = self.bout_count + 1
                            self.bout_start = time.time()
                            self.bout_start_time = self.bout_start - self.start_time
                            self.bout_explore = "1"
                            self.bout_active = True
                            self.frame_1_explore_status.configure(bg='green')
                            self.label_1_explore_status.configure(bg='green')
                            self.pressed_key = ""
                        if (self.pressed_key == self.Keybind_1) and (self.bout_active == True) and (
                                    self.bout_explore == "1") and (
                                    self.trial_active == True):
                            self.bout_end = time.time()
                            self.bout_length = self.bout_end - self.bout_start
                            self.explore_1_total = self.explore_1_total + self.bout_length
                            self.bout_details = "%f, %f, %s, %f" % (
                                self.bout_count, self.bout_start_time, self.bout_explore, self.bout_length)
                            if not self.trial_record:
                                self.trial_record = "\n" + "%s, %s, %s, %s" % (
                                self.trial_anid, self.start_date, self.trial_condition, self.trial_mode) + "\n" + self.bout_details
                            else:
                                self.trial_record = self.trial_record + "\n" + self.bout_details
                            self.bout_active = False
                            self.bout_explore = "Neither"
                            self.frame_1_explore_status.configure(bg='white')
                            self.label_1_explore_status.configure(bg='white')
                            self.pressed_key = ""

                        if (self.pressed_key == self.Keybind_2) and (self.bout_active == False) and (
                                    self.bout_explore == "Neither") and (
                                    self.trial_active == True):
                            self.bout_count = self.bout_count + 1
                            self.bout_start = time.time()
                            self.bout_start_time = self.bout_start - self.start_time
                            self.bout_explore = "2"
                            self.bout_active = True
                            self.frame_2_explore_status.configure(bg='green')
                            self.label_2_explore_status.configure(bg='green')
                            self.pressed_key = ""
                        if (self.pressed_key == self.Keybind_2) and (self.bout_active == True) and (
                                    self.bout_explore == "2") and (
                                    self.trial_active == True):
                            self.bout_end = time.time()
                            self.bout_length = self.bout_end - self.bout_start
                            self.explore_2_total = self.explore_2_total + self.bout_length
                            self.bout_details = "%f, %f, %s, %f" % (
                                self.bout_count, self.bout_start_time, self.bout_explore, self.bout_length)
                            if not self.trial_record:
                                self.trial_record = "\n" + "%s, %s, %s, %s" % (
                                self.trial_anid, self.start_date, self.trial_condition, self.trial_mode) + "\n" + self.bout_details
                            else:
                                self.trial_record = self.trial_record + "\n" + self.bout_details
                            self.bout_active = False
                            self.bout_explore = "Neither"
                            self.frame_2_explore_status.configure(bg='white')
                            self.label_2_explore_status.configure(bg='white')
                            self.pressed_key = ""
                            
                        if (self.pressed_key == self.Keybind_3) and (self.bout_active == False) and (
                                    self.bout_explore == "Neither") and (
                                    self.trial_active == True):
                            self.bout_count = self.bout_count + 1
                            self.bout_start = time.time()
                            self.bout_start_time = self.bout_start - self.start_time
                            self.bout_explore = "3"
                            self.bout_active = True
                            self.frame_3_explore_status.configure(bg='green')
                            self.label_3_explore_status.configure(bg='green')
                            self.pressed_key = ""
                        if (self.pressed_key == self.Keybind_3) and (self.bout_active == True) and (
                                    self.bout_explore == "3") and (
                                    self.trial_active == True):
                            self.bout_end = time.time()
                            self.bout_length = self.bout_end - self.bout_start
                            self.explore_3_total = self.explore_3_total + self.bout_length
                            self.bout_details = "%f, %f, %s, %f" % (
                                self.bout_count, self.bout_start_time, self.bout_explore, self.bout_length)
                            if not self.trial_record:
                                self.trial_record = "\n" + "%s, %s, %s, %s" % (
                                self.trial_anid, self.start_date, self.trial_condition, self.trial_mode) + "\n" + self.bout_details
                            else:
                                self.trial_record = self.trial_record + "\n" + self.bout_details
                            self.bout_active = False
                            self.bout_explore = "Neither"
                            self.frame_3_explore_status.configure(bg='white')
                            self.label_3_explore_status.configure(bg='white')
                            self.pressed_key = ""
                        
                        if (self.pressed_key == self.Keybind_4) and (self.bout_active == False) and (
                                    self.bout_explore == "Neither") and (
                                    self.trial_active == True):
                            self.bout_count = self.bout_count + 1
                            self.bout_start = time.time()
                            self.bout_start_time = self.bout_start - self.start_time
                            self.bout_explore = "4"
                            self.bout_active = True
                            self.frame_4_explore_status.configure(bg='green')
                            self.label_4_explore_status.configure(bg='green')
                            self.pressed_key = ""
                        if (self.pressed_key == self.Keybind_4) and (self.bout_active == True) and (
                                    self.bout_explore == "4") and (
                                    self.trial_active == True):
                            self.bout_end = time.time()
                            self.bout_length = self.bout_end - self.bout_start
                            self.explore_4_total = self.explore_4_total + self.bout_length
                            self.bout_details = "%f, %f, %s, %f" % (
                                self.bout_count, self.bout_start_time, self.bout_explore, self.bout_length)
                            if not self.trial_record:
                                self.trial_record = "\n" + "%s, %s, %s, %s" % (
                                self.trial_anid, self.start_date, self.trial_condition, self.trial_mode) + "\n" + self.bout_details
                            else:
                                self.trial_record = self.trial_record + "\n" + self.bout_details
                            self.bout_active = False
                            self.bout_explore = "Neither"
                            self.frame_4_explore_status.configure(bg='white')
                            self.label_4_explore_status.configure(bg='white')
                            self.pressed_key = ""
                            
                        if (self.pressed_key == self.Keybind_5) and (self.bout_active == False) and (
                                    self.bout_explore == "Neither") and (
                                    self.trial_active == True):
                            self.bout_count = self.bout_count + 1
                            self.bout_start = time.time()
                            self.bout_start_time = self.bout_start - self.start_time
                            self.bout_explore = "5"
                            self.bout_active = True
                            self.frame_5_explore_status.configure(bg='green')
                            self.label_5_explore_status.configure(bg='green')
                            self.pressed_key = ""
                        if (self.pressed_key == self.Keybind_5) and (self.bout_active == True) and (
                                    self.bout_explore == "5") and (
                                    self.trial_active == True):
                            self.bout_end = time.time()
                            self.bout_length = self.bout_end - self.bout_start
                            self.explore_5_total = self.explore_5_total + self.bout_length
                            self.bout_details = "%f, %f, %s, %f" % (
                                self.bout_count, self.bout_start_time, self.bout_explore, self.bout_length)
                            if not self.trial_record:
                                self.trial_record = "\n" + "%s, %s, %s, %s" % (
                                self.trial_anid, self.start_date, self.trial_condition, self.trial_mode) + "\n" + self.bout_details
                            else:
                                self.trial_record = self.trial_record + "\n" + self.bout_details
                            self.bout_active = False
                            self.bout_explore = "Neither"
                            self.frame_5_explore_status.configure(bg='white')
                            self.label_5_explore_status.configure(bg='white')
                            self.pressed_key = ""

                    if self.Keypress_Setup == 2:
                        if (self.pressed_key == self.Keybind_1) and (self.bout_active == False) and (
                                    self.bout_explore == "Neither") and (
                                    self.trial_active == True):
                            self.bout_count = self.bout_count + 1
                            self.bout_start = time.time()
                            self.bout_start_time = self.bout_start - self.start_time
                            self.bout_explore = "1"
                            self.bout_active = True
                            self.frame_1_explore_status.configure(bg='green')
                            self.label_1_explore_status.configure(bg='green')
                            self.pressed_key = ""
                        if (self.pressed_key == self.Keybind_2) and (self.bout_active == False) and (
                                    self.bout_explore == "Neither") and (
                                    self.trial_active == True):
                            self.bout_count = self.bout_count + 1
                            self.bout_start = time.time()
                            self.bout_start_time = self.bout_start - self.start_time
                            self.bout_explore = "2"
                            self.bout_active = True
                            self.frame_2_explore_status.configure(bg='green')
                            self.label_2_explore_status.configure(bg='green')
                            self.pressed_key = ""
                        if (self.pressed_key == self.Keybind_3) and (self.bout_active == False) and (
                                    self.bout_explore == "Neither") and (
                                    self.trial_active == True):
                            self.bout_count = self.bout_count + 1
                            self.bout_start = time.time()
                            self.bout_start_time = self.bout_start - self.start_time
                            self.bout_explore = "3"
                            self.bout_active = True
                            self.frame_3_explore_status.configure(bg='green')
                            self.label_3_explore_status.configure(bg='green')
                            self.pressed_key = ""
                        if (self.pressed_key == self.Keybind_4) and (self.bout_active == False) and (
                                    self.bout_explore == "Neither") and (
                                    self.trial_active == True):
                            self.bout_count = self.bout_count + 1
                            self.bout_start = time.time()
                            self.bout_start_time = self.bout_start - self.start_time
                            self.bout_explore = "4"
                            self.bout_active = True
                            self.frame_4_explore_status.configure(bg='green')
                            self.label_4_explore_status.configure(bg='green')
                            self.pressed_key = ""
                        if (self.pressed_key == self.Keybind_5) and (self.bout_active == False) and (
                                    self.bout_explore == "Neither") and (
                                    self.trial_active == True):
                            self.bout_count = self.bout_count + 1
                            self.bout_start = time.time()
                            self.bout_start_time = self.bout_start - self.start_time
                            self.bout_explore = "5"
                            self.bout_active = True
                            self.frame_5_explore_status.configure(bg='green')
                            self.label_5_explore_status.configure(bg='green')
                            self.pressed_key = ""
                if self.Numkey_Setup == 2:
                    if self.Keypress_Setup == 1:
                        if (self.pressed_key == self.Keybind_1) and (self.bout_active == False) and (
                                    self.bout_explore == "Neither") and (
                                    self.trial_active == True):
                            self.bout_count = self.bout_count + 1
                            self.bout_start = time.time()
                            self.bout_start_time = self.bout_start - self.start_time
                            self.bout_explore = "Normal"
                            self.bout_active = True
                            self.frame_normal_explore_status.configure(bg='green')
                            self.normal_explore_status.configure(bg='green')
                            self.pressed_key = ""
                        if (self.pressed_key == self.Keybind_1) and (self.bout_active == True) and (
                                    self.bout_explore == "Normal") and (
                                    self.trial_active == True):
                            self.bout_end = time.time()
                            self.bout_length = self.bout_end - self.bout_start
                            self.normal_explore_total = self.normal_explore_total + self.bout_length
                            self.bout_details = "%f, %f, %s, %f" % (
                                self.bout_count, self.bout_start_time, self.bout_explore, self.bout_length)
                            if not self.trial_record:
                                self.trial_record = "\n" + "%s, %s, %s, %s" % (
                                self.trial_anid, self.start_date, self.trial_condition, self.trial_mode) + "\n" + self.bout_details
                            else:
                                self.trial_record = self.trial_record + "\n" + self.bout_details
                            self.bout_active = False
                            self.bout_explore = "Neither"
                            self.frame_normal_explore_status.configure(bg='white')
                            self.normal_explore_status.configure(bg='white')
                            self.pressed_key = ""
                            
                        if (self.pressed_key == self.Keybind_5) and (self.bout_active == False) and (
                                    self.bout_explore == "Neither") and (
                                    self.trial_active == True):
                            self.bout_count = self.bout_count + 1
                            self.bout_start = time.time()
                            self.bout_start_time = self.bout_start - self.start_time
                            self.bout_explore = "Odd"
                            self.bout_active = True
                            self.frame_odd_explore_status.configure(bg='green')
                            self.odd_explore_status.configure(bg='green')
                            self.pressed_key = ""
                        if (self.pressed_key == self.Keybind_5) and (self.bout_active == True) and (
                                    self.bout_explore == "Odd") and (
                                    self.trial_active == True):
                            self.bout_end = time.time()
                            self.bout_length = self.bout_end - self.bout_start
                            self.odd_explore_total = self.odd_explore_total + self.bout_length
                            self.bout_details = "%f, %f, %s, %f" % (
                                self.bout_count, self.bout_start_time, self.bout_explore, self.bout_length)
                            if not self.trial_record:
                                self.trial_record = "\n" + "%s, %s, %s, %s" % (
                                self.trial_anid, self.start_date, self.trial_condition, self.trial_mode) + "\n" + self.bout_details
                            else:
                                self.trial_record = self.trial_record + "\n" + self.bout_details
                            self.bout_active = False
                            self.bout_explore = "Neither"
                            self.frame_odd_explore_status.configure(bg='white')
                            self.odd_explore_status.configure(bg='white')
                            self.pressed_key = ""

                    if self.Keypress_Setup == 2:
                        if (self.pressed_key == self.Keybind_1) and (self.bout_active == False) and (
                                    self.bout_explore == "Neither") and (
                                    self.trial_active == True):
                            self.bout_count = self.bout_count + 1
                            self.bout_start = time.time()
                            self.bout_start_time = self.bout_start - self.start_time
                            self.bout_explore = "Normal"
                            self.frame_normal_explore_status.configure(bg='green')
                            self.normal_explore_status.configure(bg='green')
                            self.bout_active = True
                        if (self.pressed_key == self.Keybind_5) and (self.bout_active == False) and (
                                    self.bout_explore == "Neither") and (
                                    self.trial_active == True):
                            self.bout_count = self.bout_count + 1
                            self.bout_start = time.time()
                            self.bout_start_time = self.bout_start - self.start_time
                            self.bout_explore = "Odd"
                            self.frame_odd_explore_status.configure(bg='green')
                            self.odd_explore_status_explore_status.configure(bg='green')
                            self.bout_active = True
                            self.pressed_key = ""


            def object_score_release(event):
                if self.Numkey_Setup == 1:
                    if (self.pressed_key == self.Keybind_1) and (self.bout_active == True) and (
                                self.bout_explore == "1") and (
                                self.trial_active == True):
                        self.bout_end = time.time()
                        self.bout_length = self.bout_end - self.bout_start
                        self.explore_1_total = self.explore_1_total + self.bout_length
                        self.bout_details = "%f, %f, %s, %f" % (
                        self.bout_count, self.bout_start_time, self.bout_explore, self.bout_length)
                        if not self.trial_record:
                            self.trial_record = "\n" + "%s, %s, %s, %s" % (
                                self.trial_anid, self.start_date, self.trial_condition,
                                self.trial_mode) + "\n" + self.bout_details
                        else:
                            self.trial_record = self.trial_record + "\n" + self.bout_details
                        self.bout_active = False
                        self.bout_explore = "Neither"
                        self.frame_1_explore_status.configure(bg='white')
                        self.label_1_explore_status.configure(bg='white')
                        self.pressed_key = ""
                    if (self.pressed_key == self.Keybind_2) and (self.bout_active == True) and (
                                self.bout_explore == "2") and (
                                self.trial_active == True):
                        self.bout_end = time.time()
                        self.bout_length = self.bout_end - self.bout_start
                        self.explore_2_total = self.explore_2_total + self.bout_length
                        self.bout_details = "%f, %f, %s, %f" % (
                        self.bout_count, self.bout_start_time, self.bout_explore, self.bout_length)
                        if not self.trial_record:
                            self.trial_record = "\n" + "%s, %s, %s, %s" % (
                                self.trial_anid, self.start_date, self.trial_condition,
                                self.trial_mode) + "\n" + self.bout_details
                        else:
                            self.trial_record = self.trial_record + "\n" + self.bout_details
                        self.bout_active = False
                        self.bout_explore = "Neither"
                        self.frame_2_explore_status.configure(bg='white')
                        self.label_2_explore_status.configure(bg='white')
                        self.pressed_key = ""
                    if (self.pressed_key == self.Keybind_3) and (self.bout_active == True) and (
                                self.bout_explore == "3") and (
                                self.trial_active == True):
                        self.bout_end = time.time()
                        self.bout_length = self.bout_end - self.bout_start
                        self.explore_3_total = self.explore_3_total + self.bout_length
                        self.bout_details = "%f, %f, %s, %f" % (
                        self.bout_count, self.bout_start_time, self.bout_explore, self.bout_length)
                        if not self.trial_record:
                            self.trial_record = "\n" + "%s, %s, %s, %s" % (
                                self.trial_anid, self.start_date, self.trial_condition,
                                self.trial_mode) + "\n" + self.bout_details
                        else:
                            self.trial_record = self.trial_record + "\n" + self.bout_details
                        self.bout_active = False
                        self.bout_explore = "Neither"
                        self.frame_3_explore_status.configure(bg='white')
                        self.label_3_explore_status.configure(bg='white')
                        self.pressed_key = ""
                    if (self.pressed_key == self.Keybind_4) and (self.bout_active == True) and (
                                self.bout_explore == "4") and (
                                self.trial_active == True):
                        self.bout_end = time.time()
                        self.bout_length = self.bout_end - self.bout_start
                        self.explore_4_total = self.explore_4_total + self.bout_length
                        self.bout_details = "%f, %f, %s, %f" % (
                        self.bout_count, self.bout_start_time, self.bout_explore, self.bout_length)
                        if not self.trial_record:
                            self.trial_record = "\n" + "%s, %s, %s, %s" % (
                                self.trial_anid, self.start_date, self.trial_condition,
                                self.trial_mode) + "\n" + self.bout_details
                        else:
                            self.trial_record = self.trial_record + "\n" + self.bout_details
                        self.bout_active = False
                        self.bout_explore = "Neither"
                        self.frame_4_explore_status.configure(bg='white')
                        self.label_4_explore_status.configure(bg='white')
                        self.pressed_key = ""
                    if (self.pressed_key == self.Keybind_5) and (self.bout_active == True) and (
                                self.bout_explore == "5") and (
                                self.trial_active == True):
                        self.bout_end = time.time()
                        self.bout_length = self.bout_end - self.bout_start
                        self.explore_5_total = self.explore_5_total + self.bout_length
                        self.bout_details = "%f, %f, %s, %f" % (
                        self.bout_count, self.bout_start_time, self.bout_explore, self.bout_length)
                        if not self.trial_record:
                            self.trial_record = "\n" + "%s, %s, %s, %s" % (
                                self.trial_anid, self.start_date, self.trial_condition,
                                self.trial_mode) + "\n" + self.bout_details
                        else:
                            self.trial_record = self.trial_record + "\n" + self.bout_details
                        self.bout_active = False
                        self.bout_explore = "Neither"
                        self.frame_5_explore_status.configure(bg='white')
                        self.label_5_explore_status.configure(bg='white')
                        self.pressed_key = ""
                if self.Numkey_Setup == 2:
                    if (self.pressed_key == self.Keybind_1) and (self.bout_active == True) and (
                                self.bout_explore == "Normal") and (
                                self.trial_active == True):
                        self.bout_end = time.time()
                        self.bout_length = self.bout_end - self.bout_start
                        self.normal_explore_total = self.normal_explore_total + self.bout_length
                        self.bout_details = "%f, %f, %s, %f" % (
                            self.bout_count, self.bout_start_time, self.bout_explore, self.bout_length)
                        if not self.trial_record:
                            self.trial_record = "\n" + "%s, %s, %s, %s" % (
                                self.trial_anid, self.start_date, self.trial_condition,
                                self.trial_mode) + "\n" + self.bout_details
                        else:
                            self.trial_record = self.trial_record + "\n" + self.bout_details
                        self.bout_active = False
                        self.bout_explore = "Neither"
                        self.frame_normal_explore_status.configure(bg='white')
                        self.normal_explore_status.configure(bg='white')
                        self.pressed_key = ""
                    if (self.pressed_key == self.Keybind_5) and (self.bout_active == True) and (
                                self.bout_explore == "Odd") and (
                                self.trial_active == True):
                        self.bout_end = time.time()
                        self.bout_length = self.bout_end - self.bout_start
                        self.odd_explore_total = self.odd_explore_total + self.bout_length
                        self.bout_details = "%f, %f, %s, %f" % (
                            self.bout_count, self.bout_start_time, self.bout_explore, self.bout_length)
                        if not self.trial_record:
                            self.trial_record = "\n" + "%s, %s, %s, %s" % (
                                self.trial_anid, self.start_date, self.trial_condition,
                                self.trial_mode) + "\n" + self.bout_details
                        else:
                            self.trial_record = self.trial_record + "\n" + self.bout_details
                        self.bout_active = False
                        self.bout_explore = "Neither"
                        self.frame_odd_explore_status.configure(bg='white')
                        self.odd_explore_status.configure(bg='white')
                        self.pressed_key = ""

            ## Trial Menu Window ##

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
            if self.Numkey_Setup == 1:
                self.trial_status_var_1_label = Label(self.trial_window, text = "Obj 1 Explore")
                self.trial_status_var_1_label.grid(row=5,column=1)
                
                self.trial_status_var_2_label = Label(self.trial_window, text = "Obj 2 Explore")
                self.trial_status_var_2_label.grid(row=5,column=2)
                
                self.trial_status_var_3_label = Label(self.trial_window, text = "Obj 3 Explore")
                self.trial_status_var_3_label.grid(row=5,column=3)
                
                self.trial_status_var_4_label = Label(self.trial_window, text = "Obj 4 Explore")
                self.trial_status_var_4_label.grid(row=5,column=4)
                
                self.trial_status_var_5_label = Label(self.trial_window, text = "Obj 5 Explore")
                self.trial_status_var_5_label.grid(row=5,column=5)
            if self.Numkey_Setup == 2:
                self.trial_status_var_left_label = Label(self.trial_window, text="Normal Explore")
                self.trial_status_var_left_label.grid(row=3, column=3)
                self.trial_status_var_right_label = Label(self.trial_window, text="Odd Explore")
                self.trial_status_var_right_label.grid(row=3, column=4)
                
            self.trial_status_total_elapsed = Label(self.trial_window, textvariable=self.time_elapsed_string)
            self.trial_status_total_elapsed.grid(row=4, column=1)
            self.trial_status_total_remaining = Label(self.trial_window, textvariable=self.time_remaining_string)
            self.trial_status_total_remaining.grid(row=4, column=2)
            if self.Numkey_Setup == 1:
                self.object_1_explore_length_string = IntVar()
                self.object_2_explore_length_string = IntVar()
                self.object_3_explore_length_string = IntVar()
                self.object_4_explore_length_string = IntVar()
                self.object_5_explore_length_string = IntVar()
                self.trial_status_1_elapsed = Label(self.trial_window, textvariable = self.object_1_explore_length_string)
                self.trial_status_1_elapsed.grid(row=6,column=1)
                self.trial_status_2_elapsed = Label(self.trial_window, textvariable = self.object_2_explore_length_string)
                self.trial_status_2_elapsed.grid(row=6,column=2)
                self.trial_status_3_elapsed = Label(self.trial_window, textvariable = self.object_3_explore_length_string)
                self.trial_status_3_elapsed.grid(row=6,column=3)
                self.trial_status_4_elapsed = Label(self.trial_window, textvariable = self.object_4_explore_length_string)
                self.trial_status_4_elapsed.grid(row=6,column=4)
                self.trial_status_5_elapsed = Label(self.trial_window, textvariable = self.object_5_explore_length_string)
                self.trial_status_5_elapsed.grid(row=6,column=5)
            if self.Numkey_Setup == 2:
                self.object_normal_length_string = IntVar()
                self.object_odd_length_string = IntVar()
                self.trial_status_left_elapsed = Label(self.trial_window, textvariable=self.object_normal_length_string)
                self.trial_status_left_elapsed.grid(row=4, column=3)
                self.trial_status_right_elapsed = Label(self.trial_window,
                                                        textvariable=self.object_odd_length_string)
                self.trial_status_right_elapsed.grid(row=4, column=4)

            ## Object Exploration Status ##
            if self.Numkey_Setup == 1:
                self.frame_1_explore_status = LabelFrame(self.trial_window, bg='white')
                self.frame_1_explore_status.grid(row=7, column=1)
                self.label_1_explore_status = Label(self.frame_1_explore_status, text="Object 1")
                self.label_1_explore_status.pack()
                
                self.frame_2_explore_status = LabelFrame(self.trial_window, bg='white')
                self.frame_2_explore_status.grid(row=7, column=2)
                self.label_2_explore_status = Label(self.frame_2_explore_status, text="Object 2")
                self.label_2_explore_status.pack()
                
                self.frame_3_explore_status = LabelFrame(self.trial_window, bg='white')
                self.frame_3_explore_status.grid(row=7, column=3)
                self.label_3_explore_status = Label(self.frame_3_explore_status, text="Object 3")
                self.label_3_explore_status.pack()
                
                self.frame_4_explore_status = LabelFrame(self.trial_window, bg='white')
                self.frame_4_explore_status.grid(row=7, column=4)
                self.label_4_explore_status = Label(self.frame_4_explore_status, text="Object 4")
                self.label_4_explore_status.pack()
                
                self.frame_5_explore_status = LabelFrame(self.trial_window, bg='white')
                self.frame_5_explore_status.grid(row=7, column=5)
                self.label_5_explore_status = Label(self.frame_5_explore_status, text="Object 5")
                self.label_5_explore_status.pack()
                
                
            if self.Numkey_Setup == 2:
                self.frame_normal_explore_status = LabelFrame(self.trial_window, bg='white')
                self.frame_normal_explore_status.grid(row=5, column=1)
                self.normal_explore_status = Label(self.frame_normal_explore_status, text="Normal Objects")
                self.normal_explore_status.pack()

                self.frame_odd_explore_status = LabelFrame(self.trial_window, bg='white')
                self.frame_odd_explore_status.grid(row=5, column=4)
                self.odd_explore_status = Label(self.frame_odd_explore_status, text="Odd Object")
                self.odd_explore_status.pack()


            self.trial_window.bind("<Key>", object_score_measures)
            if (self.Keypress_Setup == 2):
                self.trial_window.bind("<KeyRelease>", object_score_release)

            self.trial_window.update()
            self.time_update()
            self.trial_window.mainloop()

        def time_update(self):
            if self.start_time == 0:
                self.time_elapsed = 0
                self.time_remaining = 0
            if (self.start_time != 0) and (self.trial_active == True):
                self.time_elapsed = time.time() - self.start_time
                self.time_remaining = self.Explore_Max - self.time_elapsed
            if (self.start_time != 0) and (self.trial_active == False):
                self.time_elapsed = self.time_elapsed
                self.time_remaining = self.time_remaining
                
            if self.Numkey_Setup == 2:
                if (self.trial_active == True) and (self.bout_active == True) and (self.bout_explore == "Normal"):
                    self.normal_scoring = (time.time() - self.bout_start)
                    self.active_explore_normal = self.normal_explore_total + self.normal_scoring
                if (self.trial_active == True) and (self.bout_active == True) and (self.bout_explore == "Odd"):
                    self.odd_scoring = (time.time() - self.bout_start)
                    self.active_explore_odd = self.odd_explore_total + self.odd_scoring
                self.active_total_explore = self.active_explore_normal + self.active_explore_odd
            if self.Numkey_Setup == 1:
                if (self.trial_active == True) and (self.bout_active == True) and (self.bout_explore == "1"):
                    self.scoring_1 = (time.time() - self.bout_start)
                    self.active_explore_1 = self.explore_1_total + self.scoring_1
                if (self.trial_active == True) and (self.bout_active == True) and (self.bout_explore == "2"):
                    self.scoring_2 = (time.time() - self.bout_start)
                    self.active_explore_2 = self.explore_2_total + self.scoring_2
                if (self.trial_active == True) and (self.bout_active == True) and (self.bout_explore == "3"):
                    self.scoring_3 = (time.time() - self.bout_start)
                    self.active_explore_3 = self.explore_3_total + self.scoring_3
                if (self.trial_active == True) and (self.bout_active == True) and (self.bout_explore == "4"):
                    self.scoring_4 = (time.time() - self.bout_start)
                    self.active_explore_4 = self.explore_4_total + self.scoring_4
                if (self.trial_active == True) and (self.bout_active == True) and (self.bout_explore == "5"):
                    self.scoring_5 = (time.time() - self.bout_start)
                    self.active_explore_5 = self.explore_5_total + self.scoring_5
                self.active_total_explore = self.active_explore_1 + self.active_explore_2 + self.active_explore_3 + self.active_explore_4 + self.active_explore_5

            if self.time_elapsed > self.Explore_Max:
                self.trial_finish()
            if self.active_total_explore >= self.Explore_Cut:
                self.trial_finish()
            self.time_elapsed_string.set(round(self.time_elapsed, 2))
            self.time_remaining_string.set(round(self.time_remaining, 2))
            if self.Numkey_Setup == 1:
                self.object_1_explore_length_string.set(round(self.active_explore_1,2))
                self.object_2_explore_length_string.set(round(self.active_explore_2,2))
                self.object_3_explore_length_string.set(round(self.active_explore_3,2))
                self.object_4_explore_length_string.set(round(self.active_explore_4,2))
                self.object_5_explore_length_string.set(round(self.active_explore_5,2))
            if self.Numkey_Setup == 2:
                self.object_normal_length_string.set(round(self.active_explore_normal,2))
                self.object_odd_length_string.set(round(self.active_explore_odd,2))

            self.trial_window.after(10, self.time_update)

        def trial_finish(self):
            self.current_dir = os.getcwd()

            self.exp_folder = "\\Experiments"
            self.data_folder = "\\Data"
            self.protocol_folder = "\\Protocols"

            self.current_dir.replace("\\Protocols", "")
            self.experiment_dir = self.current_dir + self.exp_folder
            self.data_dir = self.current_dir + self.data_folder
            self.bout_file = self.data_dir + "\\" + self.trial_expid + "\\" + self.trial_expid + "_Bout.csv"
            self.sum_file = self.data_dir + "\\" + self.trial_expid + "\\" + self.trial_expid + "_Summary.csv"

            if self.Numkey_Setup == 1:
                self.active_bout = open(self.bout_file, 'a')
                self.active_bout.write(self.trial_record)
                self.active_bout.close()

                self.total_explore = self.explore_1_total + self.explore_2_total + self.explore_3_total + self.explore_4_total + self.explore_5_total
                if self.Odd_Position == 1:
                    self.Oddity_Ratio = (self.explore_1_total) / (self.total_explore)
                if self.Odd_Position == 2:
                    self.Oddity_Ratio = (self.explore_2_total) / (self.total_explore)
                if self.Odd_Position == 3:
                    self.Oddity_Ratio = (self.explore_3_total) / (self.total_explore)
                if self.Odd_Position == 4:
                    self.Oddity_Ratio = (self.explore_4_total) / (self.total_explore)
                if self.Odd_Position == 5:
                    self.Oddity_Ratio = (self.explore_5_total) / (self.total_explore)


                self.active_sum = open(self.sum_file, 'a')
                self.active_sum.write("\n")
                self.active_sum.write(self.start_date)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_anid)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_condition)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_mode)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_obj1)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_obj2)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_objodd)
                self.active_sum.write(",")
                self.active_sum.write(str(self.Odd_Position))
                self.active_sum.write(",")
                self.active_sum.write(str(self.explore_1_total))
                self.active_sum.write(",")
                self.active_sum.write(str(self.explore_2_total))
                self.active_sum.write(",")
                self.active_sum.write(str(self.explore_3_total))
                self.active_sum.write(",")
                self.active_sum.write(str(self.explore_4_total))
                self.active_sum.write(",")
                self.active_sum.write(str(self.explore_5_total))
                self.active_sum.write(",")
                self.active_sum.write(str(self.total_explore))
                self.active_sum.write(",")
                self.active_sum.write(str(self.Oddity_Ratio))

                self.active_sum.close()

            if self.Numkey_Setup == 2:
                self.active_bout = open(self.bout_file, 'a')
                self.active_bout.write(self.trial_record)
                self.active_bout.close()

                self.total_explore = self.normal_explore_total + self.odd_explore_total
                self.Oddity_Ratio = (self.odd_explore_total) / (self.total_explore)



                self.active_sum = open(self.sum_file, 'a')
                self.active_sum.write("\n")
                self.active_sum.write(self.start_date)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_anid)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_condition)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_mode)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_obj1)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_obj2)
                self.active_sum.write(",")
                self.active_sum.write(self.trial_objodd)
                self.active_sum.write(",")
                self.active_sum.write(str(self.Odd_Position))
                self.active_sum.write(",")
                self.active_sum.write(str(self.normal_explore_total))
                self.active_sum.write(",")
                self.active_sum.write(str(self.odd_explore_total))
                self.active_sum.write(",")
                self.active_sum.write(str(self.total_explore))
                self.active_sum.write(",")
                self.active_sum.write(str(self.Oddity_Ratio))

                self.active_sum.close()

            self.trial_window.destroy()

    test = Trial_Create(Curr_Exp=Curr_Exp)
    while True:
        if isinstance(trial_import_data, list):
            Active_Trial(trial_data=trial_import_data)
            break
        else:
            pass
