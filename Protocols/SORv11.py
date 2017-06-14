## Module Import ##
import os
import time
import tkinter  ## Import Tkinter Modules
import pygame
from msvcrt import getch
from tkinter import *  ## Access Tkinter modules without calling to Tkinter

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

        objectpair_window.mainloop()

    ## Keybinding Menu ##
    def SOR_Keybind():
        top_keybind = Toplevel()

        ## Keybind Done Command ##
        def keybind_done():
            Key_Setting = key_func.get()
            Left_Keybind = keybind_left.get()
            Right_Keybind = keybind_right.get()
            top_keybind.destroy()

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

        keybind_left = Entry(top_keybind, width=1, selectborderwidth=5)
        keybind_left.insert(END, Left_Keybind)
        keybind_left.grid(row=5, column=2)

        keybind_right_label = Label(top_keybind, text="Right Object Key")
        keybind_right_label.grid(row=6, column=1)

        keybind_right = Entry(top_keybind, width=1, selectborderwidth=5)
        keybind_right.insert(END, Right_Keybind)
        keybind_right.grid(row=6, column=2)

        keybind_done_button = Button(top_keybind, text="Done", command=keybind_done)
        keybind_done_button.grid(row=7, column=2)

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
        exp_file.write("Protocol = SORv11")
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

## SOR Trial Setup ##
def Trial_Setup(Curr_Exp, Curr_Raw_Data):
    top_run = Toplevel()

    ## Import Experimental Data ##
    experiment_file = open(Curr_Exp,"r")
    experiment_file_contents = experiment_file.readlines()
    experiment_file_contents = [experiment_item.strip("\n") for experiment_item in experiment_file_contents]

    Experiment_ID = str()
    Sample_Cut = int()
    Sample_Max = int()
    Choice_Cut = int()
    Choice_Max = int()
    Conditions = list()
    Object_List = list()
    Keypress_Setup = int()
    Left_Keybind = str()
    Right_Keybind = str()

    current_exp_title = str(experiment_file_contents[2])
    current_exp_title = current_exp_title.strip("Current_Exp = ")
    Experiment_ID = current_exp_title

    current_samp_cut = str(experiment_file_contents[5])
    current_samp_cut = current_samp_cut.strip("Sample_Cut = ")
    Sample_Cut = current_samp_cut
    Sample_Cut = int(Sample_Cut)

    current_samp_max = str(experiment_file_contents[6])
    current_samp_max = current_samp_max.strip("Sample_Max = ")
    Sample_Max = current_samp_max
    Sample_Max = int(Sample_Max)

    current_choice_cut = str(experiment_file_contents[7])
    current_choice_cut = current_choice_cut.strip("Choice_Cut = ")
    Choice_Cut = current_choice_cut
    Choice_Cut = int(Choice_Cut)

    current_choice_max = str(experiment_file_contents[8])
    current_choice_max = current_choice_max.strip("Choice_Max = ")
    Choice_Max = current_choice_max
    Choice_Max = int(Choice_Max)

    current_conditions_list = str(experiment_file_contents[11])
    current_conditions_list = current_conditions_list.strip("Conditions = ")
    current_conditions_list = current_conditions_list.strip("[")
    current_conditions_list = current_conditions_list.strip("]")
    current_conditions_list = current_conditions_list.strip(" '")
    current_conditions_list = current_conditions_list.strip("'")
    current_conditions_list = current_conditions_list.split(",")
    Conditions = current_conditions_list

    current_object_list = str(experiment_file_contents[14])
    current_object_list = current_object_list.strip("Object_List = ")
    current_object_list = current_object_list.strip("[")
    current_object_list = current_object_list.strip("]")
    current_object_list = current_object_list.strip(" '")
    current_object_list = current_object_list.strip("'")
    current_object_list = current_object_list.split(",")

    Object_List = current_object_list

    current_key_setting = str(experiment_file_contents[17])
    current_key_setting = current_key_setting.strip("Keypress_Setup = ")
    Keypress_Setup = current_key_setting
    Keypress_Setup = Keypress_Setup.strip("'")
    Keypress_Setup = int(Keypress_Setup)

    current_key_bind_left = str(experiment_file_contents[18])
    current_key_bind_left = current_key_bind_left.strip("Left_Keybind = ")
    Left_Keybind = current_key_bind_left
    Left_Keybind = Left_Keybind.strip("'")

    current_key_bind_right = str(experiment_file_contents[19])
    current_key_bind_right = current_key_bind_right.strip("Right_Keybind = ")
    Right_Keybind = current_key_bind_right
    Right_Keybind = Right_Keybind.strip("'")


    ## Start Trial ##
    def run_start_trial():
        top_run.destroy()
        top_trial_menu = Toplevel()
        top_trial_status = Toplevel()
        trial_active = FALSE
        trial_record = str()
        start_time = time.time()
        left_explore_length = 0
        left_explore_length_string = StringVar()
        left_explore_length_string.set(left_explore_length)
        right_explore_length = 0
        right_explore_length_string = StringVar()
        right_explore_length_string.set(right_explore_length)
        time_elapsed = 0
        time_elapsed_string = StringVar()
        time_elapsed_string.set(time_elapsed)
        trial_active = False


        if run_phase_choice != 2:
            curr_phase = "Sample"
            trial_length = Sample_Max
        elif run_phase_choice == 2:
            curr_phase = "Choice"
            trial_length = Choice_Max
        time_remaining = trial_length - time_elapsed
        time_remaining_string = StringVar()
        time_remaining_string.set(time_remaining)
        active_data_file = open(Curr_Raw_Data,"r+")




        ### Trial Menu Functions ###
        ## Start Trial ##
        def trial_menu_start():
            trial_raw_date = time.ctime()
            trial_raw_phase = str()
            if run_phase_choice != 2:
                trial_raw_phase = "Sample"
            elif run_phase_choice == 2:
                trial_raw_phase = "Choice"
            trial_raw_ID = str()
            trial_raw_ID = run_ID_prompt.get()
            trial_raw_condition = str()
            trial_raw_condition_position = run_Drug_List.curselection()
            trial_raw_condition = run_Drug_List.get(trial_raw_condition_position[0])
            trial_raw_obj1 = str()
            trial_raw_obj1_position = run_objectsamp_list
            trial_raw_obj2 = str()
            start_time = time.time()
            bout_count = 0
            trial_active = True



            trial_raw_data_description = "'%s','%s','%s','%s','%s','%s'" % (trial_raw_date,trial_raw_phase,trial_raw_ID,trial_raw_condition,trial_raw_obj1,trial_raw_obj2)
            trial_menu_start_button.config(state= DISABLED)
            trial_menu_finish_button.config(state="normal")
            trial_menu_pause_button.config(state="normal")
            trial_menu_restart_button.config(state="normal")
            return

        ## Finish Trial ##
        def trial_menu_finish():
            return

        ## Cancel Trial ##
        def trial_menu_cancel():
            trial_active = False
            top_trial_status.destroy()
            top_trial_menu.destroy()
            return

        ## Pause Trial ##
        def trial_menu_pause():
            trial_active = False
            pause_start_time = time.time()
            trial_menu_resume_button.config(state="normal")
            trial_menu_pause_button.config(state=DISABLED)

            return

        ## Resume Trial ##
        def trial_menu_resume():
            pause_end_time = time.time()
            trial_menu_pause_button.config(state="normal")
            trial_menu_resume_button.config(state=DISABLED)
            return

        ## Restart Trial ##
        def trial_menu_restart():
            trial_active = False
            trial_record = ""
            trial_menu_start_button.config(state="normal")
            trial_menu_restart_button.config(state=DISABLED)
            trial_menu_pause_button.config(state=DISABLED)
            trial_menu_finish_button.config(state=DISABLED)
            left_explore_length = 0
            left_explore_length_string = StringVar()
            left_explore_length_string.set(left_explore_length)
            right_explore_length = 0
            right_explore_length_string = StringVar()
            right_explore_length_string.set(right_explore_length)
            time_elapsed = 0
            time_elapsed_string = StringVar()
            time_elapsed_string.set(time_elapsed)
            time_remaining = trial_length - time_elapsed
            time_remaining_string = StringVar()
            time_remaining_string.set(time_remaining)
            return

        ## Key Press Scoring ##
        while trial_active == True:
            active_key = getch()
            time_elapsed = time.time() - start_time
            time_elapsed_string.set(time_elapsed)
            time_remaining = trial_length - time_elapsed
            time_remaining_string.set(time_remaining)
            left_explore_length_string.set(left_explore_length)
            right_explore_length_string.set(right_explore_length)
            if (time.time() - start_time) < trial_length:
                if Keypress_Setup == 1:
                    if active_key == Left_Keybind and bout_active == 0:
                        bout_count = bout_count + 1
                        bout_start = time.time()
                        bout_start_time = bout_start - start_time
                        bout_explore = "Left"
                        bout_active = 1
                        active_key = ""
                    elif active_key == Left_Keybind and bout_active == 1 and bout_explore == "Left":
                        bout_end = time.time()
                        bout_length = bout_end - bout_start
                        left_explore_length = left_explore_length + bout_length
                        bout_details = "%i, %i, %s, %i" % (bout_count, bout_start, bout_explore, bout_length)
                        trial_record = trial_record + "\n" + bout_details
                        bout_active = 0
                        active_key = ""
                    elif active_key == Right_Keybind and bout_active == 0:
                        bout_count = bout_count + 1
                        bout_start = time.time()
                        bout_start_time = bout_start - start_time
                        bout_explore = "Right"
                        bout_active = 1
                        active_key = ""
                    elif active_key == Right_Keybind and bout_active == 1 and bout_explore == Right_Keybind:
                        bout_end = time.time()
                        bout_length = bout_end - bout_start
                        right_explore_length = right_explore_length + bout_length
                        bout_details = "%i, %i, %s, %i" % (bout_count, bout_start, bout_explore, bout_length)
                        trial_record = trial_record + "\n" + bout_details
                        bout_active = 0
                        active_key = ""
            elif (time.time() - start_time) > trial_length:
                trial_active = False
                top_trial_menu.destroy()
                top_trial_status.destroy()


        ## Trial Menu Window ##
        trial_menu_title = Label(top_trial_menu, text="Active Trial Menu: %s Phase" % (curr_phase))
        trial_menu_title.grid(row=1,column=1)

        trial_menu_start_button = Button(top_trial_menu, text="Start Trial", command=trial_menu_start)
        trial_menu_start_button.grid(row=2,column=1)

        trial_menu_finish_button = Button(top_trial_menu, text="Finish Trial", command=trial_menu_finish, state=DISABLED)
        trial_menu_finish_button.grid(row=3,column=1)

        trial_menu_cancel_button = Button(top_trial_menu, text="Cancel Trial", command=trial_menu_cancel)
        trial_menu_cancel_button.grid(row=4,column=1)

        trial_menu_pause_button = Button(top_trial_menu, text="Pause",command=trial_menu_pause, state=DISABLED)
        trial_menu_pause_button.grid(row=6,column=1)

        trial_menu_resume_button = Button(top_trial_menu, text="Resume", command=trial_menu_resume, state=DISABLED)
        trial_menu_resume_button.grid(row=7, column=1)

        trial_menu_restart_button = Button(top_trial_menu, text="Restart",command=trial_menu_restart,state=DISABLED)
        trial_menu_restart_button.grid(row=8,column=1)

        ## Trial Status Window ##
        trial_status_var_elapsed_label = Label(top_trial_status, text = "Time Elapsed")
        trial_status_var_elapsed_label.grid(row=1,column=1)
        trial_status_var_remaining_label = Label(top_trial_status, text="Time Remaining")
        trial_status_var_remaining_label.grid(row=1,column=2)
        trial_status_var_left_label = Label(top_trial_status,text="Left Explore")
        trial_status_var_left_label.grid(row=1, column=3)
        trial_status_var_right_label = Label(top_trial_status, text="Right Explore")
        trial_status_var_right_label.grid(row=1, column=4)
        trial_status_total_elapsed = Label(top_trial_status, textvariable=time_elapsed_string)
        trial_status_total_elapsed.grid(row=2,column=1)
        trial_status_total_remaining = Label(top_trial_status, textvariable=time_remaining_string)
        trial_status_total_remaining.grid(row=2,column=2)
        trial_status_left_elapsed = Label(top_trial_status, textvariable=left_explore_length_string)
        trial_status_left_elapsed.grid(row=2,column=3)
        trial_status_right_elapsed = Label(top_trial_status, textvariable=right_explore_length_string)
        trial_status_right_elapsed.grid(row=2,column=4)

        top_trial_status.update_idletasks()
        top_trial_menu.mainloop()
        top_trial_status.mainloop()







    ## Cancel Trial ##
    def run_cancel_trial():
        top_run.destroy()

    ## Window Specs ##
    run_title = Label(top_run, text="Trial Setup")
    run_title.grid(row=1, column=2)

    run_ID_label = Label(top_run, text="Rat ID: ")
    run_ID_label.grid(row=2, column=1)

    run_ID_prompt = Entry(top_run)
    run_ID_prompt.grid(row=2, column=3)

    run_Drug_label = Label(top_run, text="Drug Condition: ")
    run_Drug_label.grid(row=3, column=2)

    run_Drug_List = Listbox(top_run, selectmode=SINGLE, height=4, exportselection=FALSE)
    run_Drug_List.grid(row=4, column=2)
    for condition in Conditions:
        run_Drug_List.insert(END,condition)

    run_object_label = Label(top_run, text="Objects")
    run_object_label.grid(row=5, column=2)

    run_objectsamp_label = Label(top_run, text = "Sample Object")
    run_objectsamp_label.grid(row=6,column=1)

    run_objectsamp_list = Listbox(top_run, selectmode=SINGLE, height=4, exportselection=FALSE)
    run_objectsamp_list.grid(row=7,column=1)
    for object in Object_List:
        run_objectsamp_list.insert(END,object)

    run_objectchoice_label = Label(top_run, text = "Choice Object")
    run_objectchoice_label.grid(row=6,column=3)

    run_objectchoice_list = Listbox(top_run, selectmode=SINGLE ,height=4,exportselection=FALSE)
    run_objectchoice_list.grid(row=7, column=3)
    for object in Object_List:
        run_objectchoice_list.insert(END,object)

    run_phase_choice = IntVar()

    run_phase_sample_only = Radiobutton(top_run, text = "Sample", variable = run_phase_choice, value=1)
    run_phase_sample_only.grid(row=8,column=2)

    run_phase_choice_only = Radiobutton(top_run, text = "Choice", variable = run_phase_choice, value=2)
    run_phase_choice_only.grid(row=9, column=2)

    run_phase_choice_both = Radiobutton(top_run, text = "Sample/Choice", variable = run_phase_choice, value=3)
    run_phase_choice_both.grid(row=10, column=2)

    run_start_trial_button = Button(top_run, text="Start Trial",command=run_start_trial)
    run_start_trial_button.grid(row=11,column=2)

    run_start_trial_button = Button(top_run, text = "Cancel", command=run_cancel_trial)
    run_start_trial_button.grid(row=12,column=2)

    run_trial_parameter_frame = LabelFrame(top_run, text="Trial Parameters")
    run_trial_parameter_frame.grid(row=13,column=2)

    parameter_frame_task = Label(run_trial_parameter_frame, text="Experiment Type: SORv11")
    parameter_frame_task.grid(row=14,column=1)

    parameter_frame_sample = Label(run_trial_parameter_frame, text="Sample: Max = %i , Cutoff = %i " % (Sample_Max,Sample_Cut) )
    parameter_frame_sample.grid(row=15,column=1)

    parameter_frame_choice = Label(run_trial_parameter_frame, text="Choice: Max = %i, Cutoff = %i" % (Choice_Max, Choice_Cut))
    parameter_frame_choice.grid(row=16,column=1)

    top_run.mainloop()