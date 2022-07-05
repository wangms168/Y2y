from time import sleep
import tkinter as tk
root= tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - 300
y_coordinate = (screen_height / 2) - 300
root.geometry("400x200+%d+%d" % (x_coordinate, y_coordinate))
var=tk.StringVar()
var.set('hello')

def test():
    sleep(1)
    print("最后输出")

def com():
    label.configure(background='red' )
    var.set('被点击了')
    # print( '账号: ' ,e1.get())
    # print( '密码: ' ,e2.get())
    tt.delete('1.0', tk.END)
    tt.insert('insert', '账号: '+e1.get()+'\n'+'密码: '+e2.get()+'\n')
    tt.update()

    n=1
    while n<=10:
        sleep(1)
        tt.delete('1.0', tk.END)
        tt.insert('insert', '变化:'+str(n))
        tt.update()
        n+=1

    test()

label=tk.Label(root, textvariable=var ,width=10 ,height=2 ,bg='gray')
tt=tk.Text( root, width=45 , height= 10)
button= tk.Button(root ,
    text= '按钮',
    #按钮上的文本
    width=5,
    #按钮宽度
    height=1,
    #按钮高度
    command=com #按钮执行 的命令
)
e1= tk.Entry(root, show='') #明文
e2= tk.Entry(root, show='*') #密文
# e1.insert(1,'fd')
tt.insert( 'insert', '你是猪吗\n')
tt.insert( 'current', '我是猪\n')
tt.insert( 'end','123\n')
# tt.delete('1.0',tk.END) #删除文本框所有内容
label.pack(side= 'left')
button.pack(side='right' )
e1.pack() 
e2.pack()
tt.pack()

tk.mainloop()
