import tkinter

__author__ = 'hp'
from tkinter import *
from tkinter import ttk
import pandas as pd
import tkinter.messagebox as meassage_box
import functions

#main window of the software with resolution
mainwindow=tkinter.Tk()
mainwindow.wm_attributes("-fullscreen",True)
# this is x not a multiplication *
#mainwindow.geometry("500x500")


# data-frame + states,year,cause,age-groups list
df = pd.read_csv("data.csv")
STATES = sorted(list(set(df["STATE/UT"])))
YEAR = sorted(list(set(df["Year"])))
CAUSE = sorted(list(set(df["CAUSE"])))
AGE = sorted(list(set(df.columns[3:16])))


# buttion for quit the button
Button_for_quit_the_window=tkinter.Button(mainwindow,text="quit" ,command=lambda: quitbutton(),height=2,width=20,bg='red')


#quit button exit function
def quitbutton():
    box=meassage_box.askquestion('Exit Application','Are you sure to exit the window',icon='warning')
    if box == 'yes':
        mainwindow.destroy()


# quit application function

#left side first frame
frame_left=tkinter.Frame(mainwindow,highlightbackground="green", highlightcolor="green", highlightthickness=1,bg="silver",height=500,width=500, borderwidth = 1)
frame_left.pack(side=LEFT)
frame_left.place(x=100,y=100)
#farmelabel
frame_label1=tkinter.Label(frame_left,text="One State graph",padx=10,bg="silver",fg="red",font = "Helvetica 16 bold italic")
frame_label1.pack(padx=10,pady=10)




#window text label of main screen
main_label=tkinter.Label(mainwindow,text="Sucide Graph Generating Software", padx=20,font = "Helvetica 16 bold italic")
main_label.pack()


######################  one state graph  ############################################

#sate variable
state_list_1=StringVar(frame_left)
state_list_1.set(STATES[0]) #default value

#cause variable
cause_list_1=StringVar(frame_left)
cause_list_1.set(CAUSE[0]) #default value


#year variable
year_list_1=StringVar(frame_left)
year_list_1.set(YEAR[0]) #default value



#state label

#dropdown list for states
drop_down_list_for_states_1=ttk.OptionMenu(frame_left,state_list_1,*STATES)

#dropdown list for cause
drop_down_list_for_cause_1=ttk.OptionMenu(frame_left,cause_list_1,*CAUSE)

#dropdownlist for years

drop_down_list_for_year_1=ttk.OptionMenu(frame_left,year_list_1,*YEAR)
Result = ttk.Entry(frame_left)



# adding a dropdow list into the frame
drop_down_list_for_states_1.pack(padx=10,pady=10)


drop_down_list_for_cause_1.pack(padx=10,pady=10)


drop_down_list_for_year_1.pack(padx=10,pady=10)




#button for grapg generating in left frame
button_for_graph_1=tkinter.Button(frame_left,text='garph generating',command=lambda: functions.one_sate_graph(state_list_1.get(),cause_list_1.get(),int(year_list_1.get())),height=2,width=20,bg='red')
button_for_graph_1.pack(padx=10,pady=10)

########################## Difference between two year in one state graph ####################################################################


#second frame
second_frame=tkinter.Frame(mainwindow,highlightbackground="blue", highlightcolor="blue", highlightthickness=1,bg="silver",height=500,width=500,bd=2)
second_frame.pack(side=LEFT)
second_frame.place(x=100,y=400)
#farmelabel
frame_label2=tkinter.Label(second_frame,text="Difference between two Years in one State graph",padx=10,bg="silver",fg="red",font = "Helvetica 16 bold italic")
frame_label2.pack(padx=10,pady=10)



state_list_2=StringVar(second_frame)
state_list_2.set(STATES[0]) #default value

#cause variable
cause_list2_2=StringVar(second_frame)
cause_list2_2.set(CAUSE[0]) #default value


#year first variable
year_list_2=StringVar(second_frame)
year_list_2.set(YEAR[0]) #default value

#year first variable
year_list2_2=StringVar(second_frame)
year_list2_2.set(YEAR[0]) #default value






#state label

#dropdown list for states
drop_down_list_for_states_2=ttk.OptionMenu(second_frame,state_list_2,*STATES)

#dropdown list for cause
drop_down_list_for_cause_2=ttk.OptionMenu(second_frame,cause_list2_2,*CAUSE)

#dropdownlist for years first

drop_down_list_for_year_2=ttk.OptionMenu(second_frame,year_list_2,*YEAR)

#dropdownlist for years two

drop_down_list_for_year2_2=ttk.OptionMenu(second_frame,year_list2_2,*YEAR)

#dropdown list for age


Result = ttk.Entry(second_frame)


# adding a dropdow list into the frame
drop_down_list_for_states_2.pack(padx=10,pady=10)


drop_down_list_for_cause_2.pack(padx=10,pady=10)


drop_down_list_for_year_2.pack(padx=10,pady=10)

drop_down_list_for_year2_2.pack(padx=10,pady=10)



#button for graph generating in left frame
button_for_graph_2=tkinter.Button(second_frame,text='garph generating',command=lambda: functions.two_years_difference_graph(state_list_2.get(),cause_list2_2.get(),int(year_list_2.get()),int(year_list2_2.get())),height=2,width=20,bg='red')
button_for_graph_2.pack(padx=10,pady=10)


########################## Difference between two states in one year state graph ####################################################################


#third frame
third_frame=tkinter.Frame(mainwindow,highlightbackground="blue", highlightcolor="blue", highlightthickness=1,bg="silver",height=500,width=500,bd=2)
third_frame.pack(side=RIGHT)
third_frame.place(x=400,y=100)
#farmelabel
frame_label3=tkinter.Label(third_frame,text="Difference between two States in one year graph",padx=10,bg="silver",fg="red",font = "Helvetica 16 bold italic")
frame_label3.pack(padx=10,pady=10)



state_list_3=StringVar(third_frame)
state_list_3.set(STATES[0]) #default value

state_list2_3=StringVar(third_frame)
state_list2_3.set(STATES[0]) #default value

#cause variable
cause_list_3=StringVar(third_frame)
cause_list_3.set(CAUSE[0]) #default value


#year first variable
year_list_3=StringVar(third_frame)
year_list_3.set(YEAR[0]) #default value








#state label

#dropdown list for states
drop_down_list_for_states_3=ttk.OptionMenu(third_frame,state_list_3,*STATES)


drop_down_list_for_state2_3=ttk.OptionMenu(third_frame,state_list2_3,*STATES)

#dropdown list for cause
drop_down_list_for_cause_3=ttk.OptionMenu(third_frame,cause_list_3,*CAUSE)

#dropdownlist for years first

drop_down_list_for_year_3=ttk.OptionMenu(third_frame,year_list_3,*YEAR)




#dropdown list for age


Result = ttk.Entry(third_frame)


#button adding and placing inside the window
Button_for_quit_the_window.pack() # add a button to the window
Button_for_quit_the_window.place(x=650,y=750) # to set the x and y axis dimentions in mainwindow

# adding a dropdow list into the frame
drop_down_list_for_states_3.pack(padx=10,pady=10)

drop_down_list_for_state2_3.pack(padx=10,pady=10)

drop_down_list_for_cause_3.pack(padx=10,pady=10)


drop_down_list_for_year_3.pack(padx=10,pady=10)





#button for graph generating in right frame
button_for_graph_3=tkinter.Button(third_frame,text='garph generating',command=lambda: functions.two_states_difference_graph(state_list_3.get(),state_list2_3.get(),cause_list_3.get(),int(year_list_3.get())),height=2,width=20,bg='red')
button_for_graph_3.pack(padx=10,pady=10)





#mainwindow loop in tkinter
mainwindow.mainloop()
