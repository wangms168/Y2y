import configparser
import os
import re
import tkinter as tk
import tkinter.filedialog
from tkinter import ttk, messagebox
import windnd

import pandas as pd

import convert
import yg_fl
import jjr_fl
import sb_fl
import gjj_fl

ZDR_bm = ''  # 制单人编码
YYB_bm = ''  # 营业部编码
JBB_bm = ''  # 基本部门编码
in_xlFile = ''  # 工资、社保excel文件


def r_cfg():
    global ZDR_bm, YYB_bm, JBB_bm
    # parent_dir = os.path.dirname(os.path.abspath(__file__))

    cfg = configparser.ConfigParser()
    # cfg.read(parent_dir + 'docs\\config.cfg')
    cfg.read('docs\\config.cfg')
    ZDR_bm = cfg.get('DEFAULT', 'zdr_bm')
    YYB_bm = cfg.get('DEFAULT', 'yyb_bm')
    JBB_bm = cfg.get('DEFAULT', 'jbb_bm')


def w_cfg(ent1, ent2, ent3):
    global ZDR_bm, YYB_bm, JBB_bm
    if not (ent1.get() and ent2.get() and ent3.get()):
        messagebox.showinfo(title='提示', message='配置字段不全！')
    else:
        cfg = configparser.ConfigParser()
        cfg.set('DEFAULT', 'zdr_bm', ent1.get())
        cfg.set('DEFAULT', 'yyb_bm', ent2.get())
        cfg.set('DEFAULT', 'jbb_bm', ent3.get())
        with open('docs\\config.cfg', 'w+') as f:
            cfg.write(f)

        ZDR_bm = ent1.get()
        YYB_bm = ent2.get()
        JBB_bm = ent3.get()
        messagebox.showinfo(title='提示', message='配置文件更新了！')


def check():
    global ZDR_bm, YYB_bm, JBB_bm, in_xlFile
    if in_xlFile == '':
        messagebox.showinfo(title='提示', message='没有选择文件！')
        return 1
    elif not (os.path.splitext(in_xlFile)[1] == '.xls' or os.path.splitext(in_xlFile)[1] == '.xlsx'):
        messagebox.showinfo(title='提示', message='非excel文件！')
        return 1
    if not (ZDR_bm and YYB_bm and JBB_bm):
        messagebox.showinfo(title='提示', message='配置字段变量不全！')
        return 1


# in_xlFile，工资社保表电子版格式程序要求：“科目代码”行3个表都是固定在第3行；“人员编码及类别”列，员工、经纪人工资表都是固定在第2列；
# 社保表xm(姓名)列固定在第3列、“代垫”列固定在第2列。要求固定的行、列之后的行列可任意增减。
def check_gz(ent1, ent2, ent3, lb):  # 工资表初步检查
    global in_xlFile, kmdm_col, kmdm, p, lst
    xls = pd.ExcelFile(in_xlFile)

    # ------------------------------------------------------------------------------------------------------------------
    # 检查一：检查工资表文件是否存在“员工”工作表sheet。
    if not (lb in xls.sheet_names):
        messagebox.showinfo(title='提示', message='该文件中没有"' + lb + '"工资表sheet!')
        return

    in_df = pd.read_excel(in_xlFile, sheet_name=lb, index_col=2 - 1, skiprows=3 - 1)

    # ------------------------------------------------------------------------------------------------------------------
    # 检查二：检查指第4行内容类型type是否全部是str，以防其内容数据而非str型科目代码、真正科目代码行落到了小于第4行。
    if not all(type(x) is str for x in in_df.columns):
        print("\n【列标题】----------------------------------------\n", in_df.columns)  # 列标题
        messagebox.showinfo(title='提示', message='科目代码行可能不在第3行,列标题进入了数据区！')
        return

    # 剔除空行索引、'^Unnamed'列标题。
    # https://stackoverflow.com/questions/36519086/how-to-get-rid-of-unnamed-0-column-in-a-pandas-dataframe
    # in_df1 = in_df.loc[~pd.isnull(in_df.index), ~in_df.columns.str.match('Unnamed')]
    in_df = in_df.loc[in_df.index.notnull(), ~in_df.columns.str.contains('^Unnamed')]
    # 剔除空的行索引、列标题。 ~按位取反运算符，即取非'^Unnamed'列标题。
    print("\n【" + lb + "工资表pandas】----------------------------------------\n", in_df)
    print("\n【行索引】----------------------------------------\n", in_df.index)  # 行索引
    print("\n【列标题】----------------------------------------\n", in_df.columns)  # 列标题

    # ------------------------------------------------------------------------------------------------------------------
    # 检查三：检查列标题列表是否科目代码范围列表的子集。
    kmdm_col = in_df.columns
    if lb == "员工":
        kmdm = set(yg_fl.kmdm) | {'1001'}
    if lb == "经纪人":
        kmdm = set(jjr_fl.kmdm) | {'1001'}

    if not set(kmdm_col).issubset(kmdm):
        print("\n【列标题】----------------------------------------\n", kmdm_col)
        print("\n【科目代码范围】----------------------------------------\n", kmdm)
        print("\n【差集】----------------------------------------\n", set(kmdm_col) - kmdm)
        messagebox.showinfo(title='提示', message='科目代码行可能不在第3行！')
        return

    # ------------------------------------------------------------------------------------------------------------------
    # 检查四：检查行索引中是否含有':|A1|A2|A小计|B小计|D小计|L小计|合计'或':|合计'，以判断人员编码列是否第3列。
    if lb == "员工":
        p = re.compile(':|A1|A2|A小计|B小计|D小计|L小计|合计')
    if lb == "经纪人":
        p = re.compile(':|合计')

    if not [x for x in in_df.index if p.findall(x)]:  # 空列表list判断
        print("\n【行索引】----------------------------------------\n", in_df.index)  # 行索引
        messagebox.showinfo(title='提示', message='人员编码列可能不在第2列！')
        return

    # ------------------------------------------------------------------------------------------------------------------
    # 检查五：检查行索引中是否存在非法字段，如全角的冒号"："
    if not all(p.findall(x) for x in in_df.index):
        print("\n【行索引】----------------------------------------\n", in_df.index)  # 行索引
        messagebox.showinfo(title='提示', message='人员编码列存在非法字段！')
        return

    # ------------------------------------------------------------------------------------------------------------------
    # 检查六：检查行索引中是否含有'A小计|B小计|合计'或'合计'，已判断人员编码列是否第3列。
    if lb == "员工":
        lst = ['A小计', '合计']
    if lb == "经纪人":
        lst = ['合计']

    if not set(lst).issubset(set(in_df.index)):
        print("\n【行索引】----------------------------------------\n", in_df.index)  # 行索引
        messagebox.showinfo(title='提示', message=lb + '工资表人员编码列可能没有"'+'|'.join(lst)+'"！')
        return

    return in_df


def check_sb(ent1, ent2, ent3):  # 社保表初步检查
    global in_xlFile
    xls = pd.ExcelFile(in_xlFile)

    # ------------------------------------------------------------------------------------------------------------------
    # 检查一：检查工资表文件是否存在“社保”工作表sheet。
    if not ('社保' in xls.sheet_names):
        messagebox.showinfo(title='提示', message='检查一：该文件中没有“社保”表sheet!')
        return

    in_df = pd.read_excel(in_xlFile, sheet_name="社保", index_col=3 - 1, skiprows=3 - 1)

    # ------------------------------------------------------------------------------------------------------------------
    # 检查二：检查指第4行内容类型type是否全部是str，以防其内容数据而非str型科目代码、真正科目代码行落到了小于第4行。
    if not all(type(x) is str for x in in_df.columns):
        print("\n【列标题】----------------------------------------\n", in_df.columns)  # 列标题
        messagebox.showinfo(title='提示', message='检查二：科目代码行可能不在第3行,列标题进入了数据区！')
        return

    # 剔除空行索引、'^Unnamed'列标题。
    in_df = in_df.loc[in_df.index.notnull(), ~in_df.columns.str.contains('^Unnamed')]
    print("\n【社保表-df】----------------------------------------\n", in_df)
    print("\n【社保表-行索引】----------------------------------------\n", in_df.index)  # 行索引
    print("\n【社保表-列标题】----------------------------------------\n", in_df.columns)  # 列标题

    # ------------------------------------------------------------------------------------------------------------------
    # 检查三：检查列标题列表是否科目代码范围列表的子集。
    kmdm_col = in_df.columns
    kmdm_1 = sb_fl.case_1.keys()  # 字典dict键key列表
    kmdm_2 = sb_fl.case_2.keys()
    kmdm_3 = gjj_fl.case.keys()
    kmdm_4 = ['1001', '代垫', '660110', '660110个人']
    kmdm = set(kmdm_1) | set(kmdm_2) | set(kmdm_3) | set(kmdm_4)
    if not set(kmdm_col).issubset(kmdm):
        print("\n【列标题】----------------------------------------\n", kmdm_col)
        print("\n【科目代码范围】----------------------------------------\n", kmdm)
        print("\n【差集】----------------------------------------\n", set(kmdm_col) - kmdm)
        messagebox.showinfo(title='提示', message='检查三：科目代码行可能不在第3行！')
        return

    # ------------------------------------------------------------------------------------------------------------------
    # 检查四：检查列标题列表是否包含['1001', '代垫', '660110', '660110个人']。
    if not set(kmdm_4).issubset(set(kmdm_col)):
        print("\n【列标题】----------------------------------------\n", kmdm_col)
        messagebox.showinfo(title='提示', message="检查四：科目代码行可能不包含['1001', '代垫', '660110', '660110个人']！")
        return

    # ------------------------------------------------------------------------------------------------------------------
    # 检查五：检查行索引中是否含有'本分小计|应收小计|成本数据|实付数据'，已判断人员编码列是否第3列。
    p = re.compile('本分小计|应收小计|成本数据|实付数据')
    if not set(kmdm_col).issubset(kmdm) and [x for x in in_df.index if p.findall(x)]:
        print("\n【列标题】----------------------------------------\n", kmdm_col)
        print("\n【科目代码范围】----------------------------------------\n", kmdm)
        print("\n【差集】----------------------------------------\n", set(kmdm_col) - kmdm)
        messagebox.showinfo(title='提示', message='检查四：人员姓名列可能不在第3列！')
        return

    # ------------------------------------------------------------------------------------------------------------------
    # 检查六：检测行索引in_df.index.name=="xm"
    if not in_df.index.name == "xm":
        print("\n【行索引name】----------------------------------------\n", in_df.index.name)
        messagebox.showinfo(title='提示', message='检查六：行索引name不是“xm”！')
        return

    # ==================================================================================================================
    # 准备代垫dd_df，其含应收应付及代垫总部，sf_df应收应付，dz_df代垫总部
    dd_df = pd.read_excel(in_xlFile, sheet_name="社保", index_col=2 - 1, skiprows=3 - 1)
    dd_df = dd_df.loc[dd_df.index.notnull(), ~dd_df.columns.str.contains('^Unnamed')]
    print("\n【dd_df】----------------------------------------\n", dd_df)

    # ------------------------------------------------------------------------------------------------------------------
    # dd_df检查一：备注列中的一些实例备注不要删干净了
    if not (dd_df.index.size > 0):
        messagebox.showinfo(title='提示', message='dd_df检查一：代垫dd_df备注列中的一些实例备注不要删干净了，留点吧！')
        return

    # 准备应收应付sf_df
    # https://stackoverflow.com/questions/11350770/select-by-partial-string-from-a-pandas-dataframe
    sf_df = dd_df.loc[
        dd_df.index.str.contains("应收|应付"), ~dd_df.columns.str.contains('^Unnamed')]  # 这个不能代替上面一句，只能在上一句基础上进行筛选。
    print("\n【应收付sf_df】----------------------------------------\n", sf_df)

    # 准备代垫总部dz_df
    dz_df = dd_df.loc[
        dd_df.index.str.contains("代垫总部"), ~dd_df.columns.str.contains('^Unnamed')]  # 这个不能代替上面一句，只能在notnull基础上进行筛选。
    print("\n【代垫总部dz_df】----------------------------------------\n", dz_df)

    # ------------------------------------------------------------------------------------------------------------------
    # dd_df检查二：检查行索引是否全是str，以此判断代垫内容列是否在18列
    if not all(type(x) is str for x in dd_df.index):
        messagebox.showinfo(title='提示', message='dd_df检查二：检查行索引是否全是str、判断代垫列可能不在第18列！')
        return

    # ------------------------------------------------------------------------------------------------------------------
    # dd_df检查三：检查行索引是否含有”应收|实付“，以此判断代垫内容列是否在28列
    p_dd = re.compile('应收|应付|代垫总部')
    if not [x for x in dd_df.index if p_dd.findall(x)]:
        print("\n【代垫-行索引】----------------------------------------\n", dd_df.index)
        messagebox.showinfo(title='提示', message='代垫df检查三：检查行索引是否含有”应收|实付|代垫总部“、判断代垫列可能不在第2列！')
        return

    return in_df, sf_df, dz_df


def convert_yg(ent1, ent2, ent3):
    os.system('cls')  # 清屏命令os.system('cls')
    global ZDR_bm, YYB_bm, JBB_bm
    if check():
        return
    # 获取初始化信息
    ZDR_bm = ent1.get()
    YYB_bm = ent2.get()
    JBB_bm = ent3.get()
    if len(JBB_bm) == 4:
        JBB_bm = YYB_bm + JBB_bm

    re = check_gz(ent1, ent2, ent3, "员工")
    if not (re is not None):  # if not re: 或 if re:  这样写不行！
        print("员工工资表检测到问题，推出！")
        return
    else:
        in_df = re
        # ==================================================================================================================
        # 各项检查完后，最后进行转换和分录生成：
        convert.convert_yg(ZDR_bm, YYB_bm, JBB_bm, in_df)
        messagebox.showinfo(title='提示', message='已转换完毕!，接下来请在用友中导入凭证。')


def convert_jjr(ent1, ent2, ent3):
    os.system('cls')  # 清屏命令os.system('cls')
    global ZDR_bm, YYB_bm, JBB_bm
    if check():
        return
    # 获取初始化信息
    ZDR_bm = ent1.get()
    YYB_bm = ent2.get()
    JBB_bm = ent3.get()
    if len(JBB_bm) == 4:
        JBB_bm = YYB_bm + JBB_bm

    re = check_gz(ent1, ent2, ent3, "经纪人")
    if not (re is not None):
        print("员工工资表检测到问题，推出！")
        return
    else:
        in_df = re
        # ==================================================================================================================
        # 各项检查完后，最后进行转换和分录生成：
        convert.convert_jjr(ZDR_bm, YYB_bm, JBB_bm, in_df)
        messagebox.showinfo(title='提示', message='已转换完毕!，接下来请在用友中导入凭证。')


def convert_sb(ent1, ent2, ent3):
    os.system('cls')  # 清屏命令os.system('cls')
    global ZDR_bm, YYB_bm, JBB_bm
    if check():
        return
    # 获取初始化信息
    ZDR_bm = ent1.get()
    YYB_bm = ent2.get()
    JBB_bm = ent3.get()
    if len(JBB_bm) == 4:
        JBB_bm = YYB_bm + JBB_bm

    re = check_sb(ent1, ent2, ent3)
    if not (re is not None):
        print("员工工资表检测到问题，推出！")
        return
    else:
        in_df, sf_df, dz_df = re
        # ==================================================================================================================
        # 各项检查完后，最后进行转换和分录生成：
        convert.convert_sb(ZDR_bm, YYB_bm, JBB_bm, in_df, sf_df, dz_df)
        messagebox.showinfo(title='提示', message='已转换完毕!，接下来请在用友中导入凭证。')


def convert_gjj(ent1, ent2, ent3):
    os.system('cls')  # 清屏命令os.system('cls')
    global ZDR_bm, YYB_bm, JBB_bm
    if check():
        return
    # 获取初始化信息
    ZDR_bm = ent1.get()
    YYB_bm = ent2.get()
    JBB_bm = ent3.get()
    if len(JBB_bm) == 4:
        JBB_bm = YYB_bm + JBB_bm

    re = check_sb(ent1, ent2, ent3)
    if not (re is not None):
        print("员工工资表检测到问题，推出！")
        return
    else:
        in_df, sf_df, dz_df = re
        # ==================================================================================================================
        # 各项检查完后，最后进行转换和分录生成：
        convert.convert_gjj(ZDR_bm, YYB_bm, JBB_bm, in_df, sf_df, dz_df)
        messagebox.showinfo(title='提示', message='已转换完毕!，接下来请在用友中导入凭证。')


def askopenfilename(obj):
    global in_xlFile
    # 打开一个文件选择框
    in_xlFile = tk.filedialog.askopenfilename()
    if in_xlFile != '':
        obj.delete(0, "end")
        obj.insert("end", in_xlFile + '\n')
    else:
        obj.delete(0, "end")
        obj.insert("end", "您没有选择任何文件")


# def newwindow(obj):
#     toplevel = tk.Toplevel(obj)
#     Demo2(toplevel)


# class Demo2:
#     # https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
#     def __init__(self, master):
#         self.master = master
#         self.master.geometry("250x100+300+200")
#         self.frame = tk.Frame(self.master)
#         self.frame.pack()
#         self.lb1 = ttk.Label(self.frame, text='预留以后用窗口')
#         self.lb1.grid(row=0, column=0, padx=5, pady=5)
#         self.qButton = ttk.Button(self.frame, text='Quit', command=self.master.destroy)
#         self.qButton.grid(row=1, column=0, padx=5, pady=5)


def main():
    def call_w_cfg():
        w_cfg(ent1, ent2, ent3)

    def call_askopenfilename():
        askopenfilename(ent4)

    def call_yg():
        convert_yg(ent1, ent2, ent3)

    def call_jjr():
        convert_jjr(ent1, ent2, ent3)

    def call_sb():
        convert_sb(ent1, ent2, ent3)

    def call_gjj():
        convert_gjj(ent1, ent2, ent3)

    mainwin = tk.Tk()
    mainwin.title("转换成导入凭证的excel表")
    screen_width = mainwin.winfo_screenwidth()
    screen_height = mainwin.winfo_screenheight()
    x_coordinate = (screen_width / 2) - 300
    y_coordinate = (screen_height / 2) - 300
    mainwin.geometry("+%d+%d" % (x_coordinate, y_coordinate))
    mainframe = tk.Frame(mainwin, bg="red")
    mainframe.pack(fill="both", expand=True, padx=25)

    # mainwin.configure(background='#f7f7f7')
    style = ttk.Style()
    style.configure('TLabel', font=('Arial', 9))  # , background='#f7f7f7'
    style.configure('Header.TLabel', font=('Arial', 18, 'bold'))
    style.configure('Text.TButton', font=('Arial', 11,))

    # 创建widget
    ##=======================================================================================    
    frm1 = tk.Frame(mainframe)  # , bg='blue'
    #   .grid_columnconfigure的作用在横向拉扯窗口时可以看出
    frm1.grid_columnconfigure(0, weight=1)
    frm1.grid_columnconfigure(1, weight=1)
    frm1.pack(fill="x")

    logo = tk.PhotoImage(file='docs\\python_logo.gif')
    lbl1 = ttk.Label(frm1, image=logo)
    lbl1.grid(row=0, column=0, rowspan=2, padx=5)

    lbl2 = ttk.Label(frm1, text='Convert App', style='Header.TLabel')
    lbl2.grid(row=0, column=1, padx=5)

    text = '''第一步、请按下面"Select"按钮选择或将即将处理的工资社保excel文件拖至有提示的方框；\
              第二步、请分别按“员工工资”、"经纪人工资"、“社保”、"公积金"按钮，对应转换生成用友导入凭证的excel文件。'''
    lbl3 = ttk.Label(frm1, wraplength=270, text=text)
    lbl3.grid(row=1, column=1, padx=5)

    spr1 = ttk.Separator(frm1, orient=tk.HORIZONTAL)
    spr1.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    ##=======================================================================================    
    frm2 = tk.Frame(mainframe)
    frm2.grid_columnconfigure(0, weight=1)
    frm2.grid_columnconfigure(1, weight=1)
    frm2.grid_columnconfigure(2, weight=1)
    frm2.grid_columnconfigure(3, weight=1)
    frm2.grid_columnconfigure(4, weight=1)
    frm2.grid_columnconfigure(5, weight=1)
    frm2.grid_columnconfigure(6, weight=1)
    frm2.pack(fill="x")
    
    lbl4 = ttk.Label(frm2, text="制单人编码")
    lbl4.grid(row=0, column=0, padx=5)

    ent1 = ttk.Entry(frm2, width=5)
    ent1.insert(0, ZDR_bm)
    ent1.grid(row=0, column=1, padx=5)

    lbl5 = ttk.Label(frm2, text="营业部编码")
    lbl5.grid(row=0, column=2, padx=5)

    ent2 = ttk.Entry(frm2, width=5)
    ent2.insert(0, YYB_bm)
    ent2.grid(row=0, column=3, padx=5)

    lbl6 = ttk.Label(frm2, text="基本部门编码")
    lbl6.grid(row=0, column=4, padx=5)

    ent3 = ttk.Entry(frm2, width=9)
    ent3.insert(0, JBB_bm)
    ent3.grid(row=0, column=5, padx=5)

    btn1 = ttk.Button(frm2, width=3, text="Ok", command=call_w_cfg)
    btn1.grid(row=0, column=6, padx=5)

    spr2 = ttk.Separator(frm2, orient=tk.HORIZONTAL)
    spr2.grid(row=1, column=0, columnspan=7, padx=5, pady=5, sticky="ew")

    ##=======================================================================================    
    frm3 = tk.Frame(mainframe)
    frm3.grid_columnconfigure(0, weight=1)
    frm3.grid_columnconfigure(1, weight=1)
    frm3.grid_columnconfigure(2, weight=1)
    frm3.grid_columnconfigure(3, weight=1)
    frm3.grid_columnconfigure(4, weight=1)
    frm3.grid_columnconfigure(5, weight=1)
    frm3.pack(fill="x")

    btn2 = ttk.Button(frm3, text="Select", style='Text.TButton', command=call_askopenfilename)
    btn2.grid(row=0, column=0, columnspan=2, padx=5, sticky='w')

    ent4 = ttk.Entry(frm3, width=55)
    ent4.insert(0, "或将所需的excel文件拖放到这里")
    ent4.grid(row=0, column=2, columnspan=4, ipady=1, padx=5, sticky="ew")

    # windnd 插件，监听文件被拖拽进来
    def func(ls):
        ent4.delete(0, "end")
        for i in ls:
            global in_xlFile
            in_xlFile = i.decode("gbk")
            ent4.insert("end", i.decode("gbk") + '\n')

    # windows 挂钩
    windnd.hook_dropfiles(ent4.winfo_id(), func)

    spr3 = ttk.Separator(frm3, orient=tk.HORIZONTAL)
    spr3.grid(row=1, column=0, columnspan=6, padx=5, pady=5, sticky="ew")


    ##=======================================================================================    
    frm4 = tk.Frame(mainframe)
    frm4.grid_columnconfigure(0, weight=1)
    frm4.grid_columnconfigure(1, weight=1)
    frm4.grid_columnconfigure(2, weight=1)
    frm4.grid_columnconfigure(3, weight=1)
    frm4.pack(fill="x")

    btn3 = ttk.Button(frm4, text="开始转换", style='Text.TButton', command=call_yg)
    btn3.grid(row=0, column=0, padx=5, sticky='w')

    btn4 = ttk.Button(frm4, text="经纪人工资",
                      style='Text.TButton', command=call_jjr)
    btn4.grid(row=0, column=1, padx=5)

    btn5 = ttk.Button(frm4, text="  社保  ",
                      style='Text.TButton', command=call_sb)
    btn5.grid(row=0, column=2, padx=5)

    btn6 = ttk.Button(frm4, text=" 公积金 ", style='Text.TButton', command=call_gjj)
    btn6.grid(row=0, column=3, padx=5, sticky='e')

    spr4 = ttk.Separator(frm4, orient=tk.HORIZONTAL)
    spr4.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

    ##=======================================================================================    
    frm5 = tk.Frame(mainframe)
    frm5.grid_columnconfigure(0, weight=1)
    frm5.pack(fill="x")

    txt_msg = tk.Text(frm5, width=70, height=4, font=('Arial', 9))
    txt_msg.insert(1.0, "Msg Output： ")
    txt_msg.insert("end", "hello，程序启动正常！")
    txt_msg.grid(row=0, column=0, padx=5, sticky="ew")

    spr5 = ttk.Separator(frm5, orient=tk.HORIZONTAL)
    spr5.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

    btn7 = ttk.Button(frm5, text="Exit", width=6, style='Text.TButton', command=mainwin.destroy, )
    btn7.grid(row=2, padx=5, pady=5, sticky='e')


    # 窗口布局Layout management

    # tart the application mainloop
    tk.mainloop()


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    r_cfg()
    main()
