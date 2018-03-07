from Tkinter import *
root=Tk()
root.title('python calc')
e=Entry(root,width=30,font="Arial 30 bold",bd=20,bg='light blue',justify='right')
e.grid(row=0,column=0,columnspan=6)
def add_entry(x):
    e.insert(16,x)
def clearall():
    txt=e.get()[:-1]
    
    e.delete(0,END)
    e.insert(0,txt)
def result(y):
    e.delete(0,END)
    e.insert(16,y)
    
Button(root,text='7',width=10,height=5,bg='pink',bd=10,font="Arial 9 bold",command=lambda:add_entry('7')).grid(row=1,column=0,sticky=E+W+N+S)
Button(root,text='8',width=10,height=5,bg='pink',bd=10,font="Arial 9 bold",command=lambda:add_entry('8')).grid(row=1,column=1,sticky=E+W+N+S)
Button(root,text='9',width=10,height=5,bg='pink',bd=10,font="Arial 9 bold",command=lambda:add_entry('9')).grid(row=1,column=2,sticky=E+W+N+S)
Button(root,text='+',width=10,height=5,bg='pink',bd=10,font="Arial 9 bold",command=lambda:add_entry('+')).grid(row=1,column=3,sticky=E+W+N+S)
Button(root,text='*',width=10,height=5,bg='pink',bd=10,font="Arial 9 bold",command=lambda:add_entry('*')).grid(row=1,column=4,sticky=E+W+N+S)
Button(root,text='(',width=10,height=5,bg='pink',bd=10,font="Arial 9 bold",command=lambda:add_entry('(')).grid(row=1,column=5,sticky=E+W+N+S)



Button(root,text='4',width=10,height=5,bg='pink',bd=10,font="Arial 9 bold",command=lambda:add_entry('4')).grid(row=2,column=0,sticky=E+W+N+S)
Button(root,text='5',width=10,height=5,bg='pink',bd=10,font="Arial 9 bold",command=lambda:add_entry('5')).grid(row=2,column=1,sticky=E+W+N+S)
Button(root,text='6',width=10,height=5,bg='pink',bd=10,font="Arial 9 bold",command=lambda:add_entry('6')).grid(row=2,column=2,sticky=E+W+N+S)
Button(root,text='-',width=10,height=5,bg='pink',bd=10,font="Arial 9 bold",command=lambda:add_entry('-')).grid(row=2,column=3,sticky=E+W+N+S)
Button(root,text=')',width=10,height=5,bg='pink',bd=10,font="Arial 9 bold",command=lambda:add_entry(')')).grid(row=2,column=5,sticky=E+W+N+S)
Button(root,text='/',width=10,height=5,bg='pink',bd=10,font="Arial 9 bold",command=lambda:add_entry('/')).grid(row=2,column=4,sticky=E+W+N+S)

Button(root,text='1',width=10,height=5,bg='pink',bd=10,font="Arial 9 bold",command=lambda:add_entry('1')).grid(row=3,column=0,sticky=E+W+N+S)
Button(root,text='2',width=10,height=5,bg='pink',bd=10,font="Arial 9 bold",command=lambda:add_entry('2')).grid(row=3,column=1,sticky=E+W+N+S)
Button(root,text='3',width=10,height=5,bg='pink',bd=10,font="Arial 9 bold",command=lambda:add_entry('3')).grid(row=3,column=2,sticky=E+W+N+S)
Button(root,text='=',width=10,height=5,bg='pink',bd=10,font="Arial 9 bold",command=lambda:result(eval(e.get()))).grid(row=3,column=3,sticky=E+W+N+S)
Button(root,text='.',width=10,height=5,bg='pink',bd=10,font="Arial 9 bold",command=lambda:add_entry('.')).grid(row=3,column=4,sticky=E+W+N+S)
Button(root,text='c',width=10,height=5,bg='pink',bd=10,font="Arial 9 bold",command=lambda:clearall()).grid(row=3,column=5,sticky=E+W+N+S)



root.mainloop()
