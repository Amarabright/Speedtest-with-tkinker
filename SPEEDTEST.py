from tkinter import *
from tkinter import messagebox 
from tkinter import ttk
import speedtest
st=speedtest.Speedtest()
root = Tk()  
root.title('SPEED TEST')
root.geometry('420x250+250+150')
root.config(background='#5902EC')
label=ttk.Label(root,text='SPEED TEST')
label.grid(row=0,column=1,padx=3,pady=5,sticky='snew')
test=ttk.Button(root,text='TEST SPEED')
test.grid(row=1,column=0,columnspan=2,padx=3,pady=3)

# to move and resize the label with respect to application window size
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)


#functionality
def spt():
    servernames=[]
    st.get_servers(servernames)
    messagebox.showinfo(title='SPEED TEST',message='Download Speed : {}MBPS\nUpload Speed : {} MBPS\nPing : {}'.format(st.download()/(1024*1024),st.upload()/(1024*1024),st.results.ping))
test.config(command=spt)

#styling

style=ttk.Style()
style.theme_use('clam')
style.configure('TLabel',background='#5902EC',foreground='#FF1818',font=('Arial',30))
style.configure('TButton',background='#ECECEC',font=('Arial',20))
style.map('TButton',background=[('pressed','#FF1818')])   




root.mainloop()  