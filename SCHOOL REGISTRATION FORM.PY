from tkinter import *
root=Tk()

def getvals():
    print("Accepted")

root.geometry("400x200")
Label (root, text= "School Registration Form" , font="calibri 12 bold").grid (row =0, column=4)
name=Label(root, text="name")
Admission=Label(root,text="Admission")
Phone=Label(root, text="Phone")
Email=Label(root,text="Email")
Studyyear=Label(root,text="Studyyear")
Course=Label(root,text="Course")

name.grid(row=1 , column=2)
Admission.grid(row=2 , column=2)
Phone.grid(row=3 , column=2)
Email.grid(row= 4, column=2)
Studyyear.grid(row=5 , column=2)
Course.grid(row= 6, column=2)
namevalue=StringVar
Admissionvalue=StringVar
PhoneValue=StringVar
Emailvalue=StringVar
Studyyearvalue=StringVar
Coursevalue=StringVar
checkvalue=IntVar

nameentry=Entry( root, textvariable=namevalue)
Admissionentry=Entry(root, textvariable=Admissionvalue)
Phoneentry=Entry(root,textvariable=PhoneValue)
Emailentry=Entry(root,textvariable=Emailvalue)
Studyyearentry=Entry(root,textvariable=Studyyearvalue)
Courseentry=Entry(root,textvariable=Coursevalue)

nameentry.grid(row=1, column =3)
Admissionentry.grid(row=2,column=3)
Phoneentry.grid(row=3,column=3)
Emailentry.grid(row=4,column=3)
Studyyearentry.grid(row=5,column=3)
Courseentry.grid(row=6,column=3)


checkbtn=Checkbutton(text="remember me?",variable=checkvalue)
checkbtn.grid(row=7,column=3)

Button(text="Submit",command=getvals).grid(row=8, column=3)



root.mainloop()  