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
Left_Keybind = "A"
Right_Keybind = "L"
Key_Setting = "1"

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

        key_bind_right_string = StringVar()
        key_bind_right_string.set("l")

        key_bind_left_string = StringVar()
        key_bind_left_string.set("a")

        ## Functions ##
        def keybind_done():
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


        keybind_right_label = Label(top_keybind, text="Right Object Key")
        keybind_right_label.grid(row=6, column=1)

        keybind_right = Label(top_keybind, textvariable=key_bind_right_string)
        keybind_right.grid(row=6, column=2)

        keybind_right_bind_button = Button(top_keybind, text="Bind", command= keybind_func_right)
        keybind_right_bind_button.grid(row=6, column=3)

        keybind_done_button = Button(top_keybind, text="Done", command=keybind_done)
        keybind_done_button.grid(row=7, column=2)

        top_keybind.focus_force()
        top_keybind.mainloop()


    ## Finish: Save Function ##
    def SOR_Finish():
        exp_filename = SOR_ID_Prompt.get() + ".ORe"
        data_raw_filename = SOR_ID_Prompt.get() + "_Raw.csv"
        data_raw_filepath = data_dir + "\\" + data_raw_filename


        exp_filepath = experiment_dir + "\\" + exp_filename
        data_file_dir = data_dir + "\\" + SOR_ID_Prompt.get()
        os.makedirs(data_file_dir)

        data_raw_filename = SOR_ID_Prompt.get() + "_Raw.csv"
        data_raw_filepath = data_file_dir + "\\" + data_raw_filename
        data_raw_file = open(data_raw_filepath, "w")
        data_raw_file.write("'Bout#','Bout_Start_Time','Bout_Side','Bout_Duration'")
        data_raw_file.close()

        exp_file = open(exp_filepath, "w")
        exp_file.write("#Protocol Details#")
        exp_file.write("\n")
        exp_file.write("Protocol = SOR_Trial")
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
    top_SOR = tkinter.Tk()  # Establish Top/Primary Window

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

    SOR_Condition_Button = Button(top_SOR, text="Conditions", command=SOR_Create_Condition)
    SOR_Condition_Button.grid(row=7, column=2)

    SOR_ObjectPairs_Button = Button(top_SOR, text="Object List", command=SOR_ObjectPairs)
    SOR_ObjectPairs_Button.grid(row=8, column=2)

    SOR_KeyBinding_Button = Button(top_SOR, text="Key Bindings", command=SOR_Keybind)
    SOR_KeyBinding_Button.grid(row=9, column=2)

    SOR_Finish_Button = Button(top_SOR, text="Finished", command=SOR_Finish)
    SOR_Finish_Button.grid(row=10, column=2)

    ## Run Window Command ##
    top_SOR.mainloop()  # Run Main Window on Loop (Start)

    return

#####################################################################################################
