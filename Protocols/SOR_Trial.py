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

## Global Variables ##


    top_run = Toplevel()

    ## Import Experimental Data ##
    experiment_file = open(exp_filepath,"r")
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
        class Active_Trial_Window(threading.Thread):

            def __init__(self):
                threading.Thread.__init__(self)
                self.start()

            def callback(self):
                self.root.quit()

            def run(self):
                self.root = Tk()
                trial_record = str()
                trial_raw_ID = str()
                bout_explore = "Neither"

                left_explore_length = 0
                start_time = 0
                right_explore_length = 0
                time_elapsed = 0
                time_remaining = 0
                total_explore = 0
                bout_count = 0
                pause_start = 0
                pause_end = 0
                pause_length = 0

                trial_active = False
                bout_active = False

                trial_raw_ID = run_ID_prompt.get()
                run_phase_choice_value = run_phase_choice.get()
                if run_phase_choice_value != 2:
                    trial_raw_phase = "Sample"
                elif run_phase_choice_value == 2:
                    trial_raw_phase = "Choice"
                trial_raw_condition = str()
                trial_raw_condition_position = run_Drug_List.curselection()
                trial_raw_condition = run_Drug_List.get(trial_raw_condition_position[0])
                trial_raw_obj1 = str()
                trial_raw_obj1_position = run_objectsamp_list
                trial_raw_obj2 = str()

                def trial_menu_start():
                    trial_menu_pause_button.config(state="normal")
                    trial_menu_start_button.config(state=DISABLED)
                    trial_menu_restart_button.config(state="normal")
                    trial_menu_finish_button.config(state="normal")
                    trial_active = True

                    start_time = time.time()

                ## Finish Trial ##
                def trial_menu_finish():
                    return

                ## Cancel Trial ##
                def trial_menu_cancel():
                    self.root.destroy()

                ## Pause Trial ##
                def trial_menu_pause():
                    global trial_active
                    global pause_start
                    global bout_active

                    if bout_active == False:
                        trial_active = False
                        pause_start = time.time()
                        trial_menu_resume_button.config(state="normal")
                        trial_menu_pause_button.config(state=DISABLED)
                    if bout_active == True:
                        return

                ## Resume Trial ##
                def trial_menu_resume():
                    global trial_active
                    global pause_start
                    global pause_end
                    global pause_length

                    pause_end = time.time()
                    pause_length = pause_length(pause_end - pause_start)

                ## Restart Trial ##
                def trial_menu_restart():
                    global trial_active
                    global bout_active
                    global start_time
                    global bout_explore
                    global left_explore_length
                    global right_explore_length
                    global time_elapsed
                    global bout_count
                    global pause_start
                    global pause_end
                    global trial_record

                    bout_explore = "Neither"
                    trial_record = str()

                    left_explore_length = 0
                    start_time = 0
                    right_explore_length = 0
                    time_elapsed = 0
                    total_explore = 0
                    bout_count = 0
                    pause_start = 0
                    pause_end = 0
                    pause_length = 0

                    trial_active = False
                    bout_active = False

                    trial_menu_finish_button.config(state=DISABLED)
                    trial_menu_restart_button.config(state=DISABLED)
                    trial_menu_finish_button.config(state=DISABLED)
                    trial_menu_pause_button.config(state=DISABLED)
                    trial_menu_resume_button.config(state=DISABLED)
                    trial_menu_start_button.config(state="normal")

                    return

                ## Key Press Scoring ##
                def object_score_measures(event):
                    global Left_Keybind
                    global Right_Keybind
                    global right_explore_length
                    global left_explore_length
                    global time_elapsed
                    global time_remaining
                    global total_explore
                    global trial_active
                    global trial_record
                    global bout_explore
                    global bout_count
                    global bout_active

                    pressed_key = event.char
                    if (pressed_key == Left_Keybind) and (bout_active == False) and (bout_explore == "Neither") and (
                        trial_active == True):
                        bout_count = bout_count + 1
                        bout_start = time.time()
                        bout_start_time = bout_start - start_time
                        bout_explore = "Left"
                        bout_active = True
                        active_key = ""
                    if (pressed_key == Left_Keybind) and (bout_active == True) and (bout_explore == "Left") and (
                        trial_active == True):
                        bout_end = time.time()
                        bout_length = bout_end - bout_start
                        left_explore_length = left_explore_length + bout_length
                        bout_details = "%i, %i, %s, %i" % (bout_count, bout_start, bout_explore, bout_length)
                        trial_record = trial_record + "\n" + bout_details
                        bout_active = False
                        active_key = ""
                    if (pressed_key == Right_Keybind) and (bout_active == False) and (bout_explore == "Neither") and (
                        trial_active == True):
                        bout_count = bout_count + 1
                        bout_start = time.time()
                        bout_start_time = bout_start - start_time
                        bout_explore = "Right"
                        bout_active = True
                        active_key = ""
                    if (pressed_key == Right_Keybind) and (bout_active == True) and (bout_explore == "Right") and (
                        trial_active == True):
                        bout_end = time.time()
                        bout_length = bout_end - bout_start
                        left_explore_length = left_explore_length + bout_length
                        bout_details = "%i, %i, %s, %i" % (bout_count, bout_start, bout_explore, bout_length)
                        trial_record = trial_record + "\n" + bout_details
                        bout_active = False
                        active_key = ""

                ## Trial Menu Window ##

                self.left_explore_length_string = StringVar()
                self.left_explore_length_string.set(str(left_explore_length))
                self.right_explore_length_string = StringVar()
                self.right_explore_length_string.set(str(right_explore_length))
                self.time_elapsed_string = StringVar()
                self.time_elapsed_string.set(str(time_elapsed))
                self.time_remaining_string = StringVar()
                self.time_remaining_string.set(str(time_remaining))
                trial_menu_title = Label(self.root, text="Active Trial Menu")
                trial_menu_title.grid(row=1, column=1)

                trial_menu_start_button = Button(self.root, text="Start Trial", command=trial_menu_start)
                trial_menu_start_button.grid(row=1, column=2)

                trial_menu_finish_button = Button(self.root, text="Finish Trial", command=trial_menu_finish,
                                                  state=DISABLED)
                trial_menu_finish_button.grid(row=2, column=2)

                trial_menu_cancel_button = Button(self.root, text="Cancel Trial", command=trial_menu_cancel)
                trial_menu_cancel_button.grid(row=1, column=3)

                trial_menu_pause_button = Button(self.root, text="Pause", command=trial_menu_pause,
                                                 state=DISABLED)
                trial_menu_pause_button.grid(row=1, column=4)

                trial_menu_resume_button = Button(self.root, text="Resume", command=trial_menu_resume,
                                                  state=DISABLED)
                trial_menu_resume_button.grid(row=2, column=4)

                trial_menu_restart_button = Button(self.root, text="Restart", command=trial_menu_restart,
                                                   state=DISABLED)
                trial_menu_restart_button.grid(row=2, column=3)

                ## Trial Status Window ##
                trial_status_var_elapsed_label = Label(self.root, text="Time Elapsed")
                trial_status_var_elapsed_label.grid(row=3, column=1)
                trial_status_var_remaining_label = Label(self.root, text="Time Remaining")
                trial_status_var_remaining_label.grid(row=3, column=2)
                trial_status_var_left_label = Label(self.root, text="Left Explore")
                trial_status_var_left_label.grid(row=3, column=3)
                trial_status_var_right_label = Label(self.root, text="Right Explore")
                trial_status_var_right_label.grid(row=3, column=4)
                trial_status_total_elapsed = Label(self.root, textvariable=self.time_elapsed_string)
                trial_status_total_elapsed.grid(row=4, column=1)
                trial_status_total_remaining = Label(self.root, textvariable=self.time_remaining_string)
                trial_status_total_remaining.grid(row=4, column=2)
                trial_status_left_elapsed = Label(self.root, textvariable=self.left_explore_length_string)
                trial_status_left_elapsed.grid(row=4, column=3)
                trial_status_right_elapsed = Label(self.root, textvariable=self.right_explore_length_string)
                trial_status_right_elapsed.grid(row=4, column=4)

                self.root.bind("<Key>", object_score_measures)
                self.root.
                self.root.update_idletasks()
                self.root.mainloop()
        trial_window = Active_Trial_Window()
        top_run.destroy()








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