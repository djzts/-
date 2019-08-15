#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter
from tkinter import *
from tkinter import ttk
import numpy as np
import os

root = Tk()
root.geometry("350x330")
root.title('投资项目评估作业生成系统(学生版)v2.0')

frame1 = Frame(root)
frame2 = Frame(root)


Label(root,text='投资项目评估作业生成系统',fg = "Black",font = "楷体 16 bold").grid(row=0,column=0,columnspan=2,sticky=W+E+N+S, padx=20, pady=5)

Label(root,text=' ').grid(columnspan=2)

Label(root,text='学号 :').grid(row=2,column=0) # 对Label内容进行 表格式 布局
Label(root,text='姓名 :').grid(row=3,column=0)
Label(root,text='课程类型 :').grid(row=4,column=0)
Label(root,text='随机码:').grid(row=5,column=0)




v1=StringVar()    # 设置变量 .
v2=StringVar()
v3=StringVar()

v4=StringVar()

e1 = Entry(root,textvariable=v1)            # 用于储存 输入的内容
#e2 = Entry(root,textvariable=v2,show='$')
e2 = Entry(root,textvariable=v2)
com3 = ttk.Combobox(root, textvariable=v3,width=5)
com3["value"] = ("校选", "限选")
com3.current(0)
e4 = Entry(root,width=3,textvariable=v4)


e1.grid(sticky="W",row=2,column=1,padx=10,pady=5)      # 进行表格式布局 .
e2.grid(sticky="W",row=3,column=1,padx=10,pady=5)
com3.grid(sticky="W",row=4,column=1,padx=10,pady=5)
e4.grid(sticky="W",row=5,column=1,padx=10,pady=5)

def show():
     #print("帐号 :%s" % e1.get())          # get 变量内容
     #print(com3.get())\
    try:
        if not os.path.exists('./作业/'):
            os.makedirs('./作业/')
    except OSError:
        print('Error: Creating directory. ' +  './作业/')


    text1=e1.get()     #学号
    text2=e2.get()   #姓名
    text3=e4.get()       #随机数
    text4=com3.get()  #课程类型

    studentnum=int(text1)
    studentname=str(text2)
    seeds = int(text3);
    Class_Type = str(text4);
    str_standard = "限选";

    randomseeds= seeds*studentnum;   # Initial set and initial distortion

    #Fixinvestment = 1e3;                     %固定资产投资 +-200
    Fixinvestment = np.round(1e3+200*np.sin(randomseeds),0);

    #Construction_year = 3;                   %建设期
    Construction_year = int(np.round(3+1*np.sin(randomseeds),0));

    #Ratioset = [0.5,0.3,0.2];                %每年投入比例
    if Construction_year == 2:
        y1=np.round(0.65+0.15*np.sin(randomseeds),2);
        Ratioset=np.array([y1,1-y1]);
    elif Construction_year == 3:
        y1=np.round(0.55+0.05*np.sin(randomseeds),2);
        y2=np.round(0.3+0.08*np.sin(randomseeds),2);
        Ratioset=np.sort(np.array([y1,y2,1-y1-y2]))[::-1];
    else:
        y1=np.round(0.55+0.05*np.sin(randomseeds),2);
        y2=np.round(0.18+0.04*np.sin(randomseeds),2);
        y3=np.round(0.11+0.03*np.sin(randomseeds),2);
        Ratioset=np.sort(np.array([y1,y2,y3,1-y1-y2-y3]))[::-1];

    #Capital_Base = 4e2;                      %资本金
    Capital_Base = np.round(Fixinvestment*(0.325+0.075*np.sin(randomseeds)));

    #Payment_Done_year = 5;                   %贷款还清年数
    Payment_Done_year = int(np.round(5 + 2*np.sin(randomseeds)));

    #Fixed_Borrow_Interest_Rate = 0.1;         %固定资产借款利息
    Fixed_Borrow_Interest_Rate = np.round(0.07 + 0.03*(np.sin(randomseeds)),3);

    #Floating_Capital_self_owned = 5e1;         %流动资金自有
    Floating_Capital_self_owned = np.round(75+25*np.sin(randomseeds));

    #Income = 5e2;                               %年收入
    Income = np.round(6+np.sin(randomseeds),2)*100;

    #Operation_tax = 0.08;                       %税金及其附加
    Operation_tax = np.round(0.075+0.015*np.sin(randomseeds),3);

    #OperationCost = 96;                         %运营期年经营成本
    OperationCost = np.round(96*(1+0.2*np.sin(randomseeds)));

    income_tax = 0.25                          #所得税

    #Yield_Expectation_rate = 0.1;                  %预期收益率
    Yield_Expectation_rate = np.round(0.07+0.03*np.sin(randomseeds),3)

    if Class_Type == str_standard:
        #Floating_Capital_borrow = 0;                %流动资金外借
        Floating_Capital_borrow = np.round(75+25*np.sin(randomseeds));

        #Operation_year = 12;                        %运营期
        Operation_year = int(np.round(12+3*np.sin(randomseeds)));

        #Operation_Cost_rate = 0;                    %经营成本增长率
        Operation_Cost_rate = np.round(0.045+0.015*np.sin(randomseeds),3);

        Residual_Fix_Assets = 0.05;                 #固定资产残值率

        #Fix_made_rate=round(0.95+0.05*sin(randomseeds),2);   %固定资产形成率
        Fix_made_rate=np.round(0.95+0.05*np.sin(randomseeds),3);

        Floating_Capital_Borrow_rate=np.round(0.055+0.015*np.sin(randomseeds),3);             #流动资金借款利率
    else:                                           # 非专业
        Floating_Capital_borrow = 0;                #流动资金外借

        #Operation_year = 12;                        #运营期
        Operation_year = int(np.round(8+4*np.sin(randomseeds)))

        Operation_Cost_rate = 0;                    #经营成本增长率

        Residual_Fix_Assets = 0.05;                 #固定资产残值率

        Fix_made_rate=1;                            #固定资产形成率

        Floating_Capital_Borrow_rate=0;             #流动资金借款利率

    filename = studentname+"_"+str(studentnum)+"_财务评价综合计算与分析" + ".xlsx";  #文件标题

    pathname = os.getcwd() + "/作业/" + filename
    ## Start!
    import xlsxwriter

    workbook = xlsxwriter.Workbook(pathname)
    worksheet = workbook.add_worksheet('建设期借款利息表')

    set=()
    for element in Ratioset:
        set=set+(np.round(element,2),)

    data=(Construction_year,Fixinvestment,Construction_year)+set+(Capital_Base,
      Fixed_Borrow_Interest_Rate*100,Payment_Done_year,Floating_Capital_self_owned,
      Operation_year,Income,Operation_tax*100,OperationCost,income_tax*100,Residual_Fix_Assets*100,
      Floating_Capital_Borrow_rate*100,Fix_made_rate*100,Operation_Cost_rate*100,Floating_Capital_borrow,Yield_Expectation_rate*100)

    if Construction_year == 2:
        txt = "某投资项目建设期%d年，固定资产投资%d万元。该投资分%d年投入，\n每年投入比例为%.3f,%.3f。用于固定资产投资的资本金为%d万元。\n资本金与贷款同比例投入。固定资产投资借款向A行借入，利率为%.1f%%。\n贷款（包括建设期利息）将于在项目运营后按年末等额还本付息方式在%d年内还清。\n不考虑无形和递延资产。流动资金全部为资本金，\n于运营期第一年投入共计%d万元，项目结束全部回收。\n本项目运营期%d年，每年营业收入为%d万元。\n营业税金及其附加按当年销售收入的%.1f%%计，运营期各年经营成本%d万元。\n所得税率%.1f%%，固定资产残值率为%.1f%%，按直线法计提折旧。\n流动资金借款利率为%.1f%%，固定资产形成率为%.1f%%，经营成本增长率为%.1f%%，\n流动资金借款为%d万元，预期收益率为%.1f%%." % data;
    elif Construction_year == 3:
        txt = "某投资项目建设期%d年，固定资产投资%d万元。该投资分%d年投入，\n每年投入比例为%.3f,%.3f,%.3f。用于固定资产投资的资本金为%d万元。\n资本金与贷款同比例投入。固定资产投资借款向A行借入，利率为%.1f%%。\n贷款（包括建设期利息）将于在项目运营后按年末等额还本付息方式在%d年内还清。\n不考虑无形和递延资产。流动资金全部为资本金，\n于运营期第一年投入共计%d万元，项目结束全部回收。\n本项目运营期%d年，每年营业收入为%d万元。\n营业税金及其附加按当年销售收入的%.1f%%计，运营期各年经营成本%d万元。\n所得税率%.1f%%，固定资产残值率为%.1f%%，按直线法计提折旧。\n流动资金借款利率为%.1f%%，固定资产形成率为%.1f%%，经营成本增长率为%.1f%%，\n流动资金借款为%d万元，预期收益率为%.1f%%." % data;
    else:
        txt = "某投资项目建设期%d年，固定资产投资%d万元。该投资分%d年投入，\n每年投入比例为%.3f,%.3f,%.3f,%.3f。用于固定资产投资的资本金为%d万元。\n资本金与贷款同比例投入。固定资产投资借款向A行借入，利率为%.1f%%。\n贷款（包括建设期利息）将于在项目运营后按年末等额还本付息方式在%d年内还清。\n不考虑无形和递延资产。流动资金全部为资本金，\n于运营期第一年投入共计%d万元，项目结束全部回收。\n本项目运营期%d年，每年营业收入为%d万元。\n营业税金及其附加按当年销售收入的%.1f%%计，运营期各年经营成本%d万元。\n所得税率%.1f%%，固定资产残值率为%.1f%%，按直线法计提折旧。\n流动资金借款利率为%.1f%%，固定资产形成率为%.1f%%，经营成本增长率为%.1f%%，\n流动资金借款为%d万元，预期收益率为%.1f%%." % data;

    merge_format = workbook.add_format({
        'bold':     True,
        'border':   6,
        'align':    'center',#水平居中
        'valign':   'vcenter',#垂直居中
        'fg_color': '#D7E4BC',#颜色填充
    })

    answer_format = workbook.add_format({
        'border':   1,
        'align':    'center',#水平居中
        'valign':   'vcenter',#垂直居中
        'fg_color': '#e6ffb3',#颜色填充
    })

    worksheet.merge_range('G2:O15', txt, merge_format)


    ## 基本输出 output
    bold = workbook.add_format({'bold':True})


    worksheet.write('A1', '建设期利息', bold)
    T1 = (
         ['固定资产投资额', ' '],
         ['资本金',   ' '],
         ['固定资产投资借款', ' ']
     )
    row = 1
    col = 0
    for item, item2 in (T1):
        worksheet.write(row, col,     item, bold)
        worksheet.write(row, col + 1, item2, answer_format)
        row += 1


    worksheet.write('A5', '建设投资比例', bold)

    row = 4
    col = 1
    for number in range(Construction_year):
         worksheet.write(row, col,' ', answer_format)
         col += 1


    #% 建设期借款利息表
    Name=(["年份","年初借款累计","本年借款支用","本年应计利息","年末借款累计"])

    row = 6
    col = 0
    for name in (Name):
         worksheet.write(row, col, name, bold)
         row += 1

    row = 6
    col = 1
    year_end_total = 0
    Table1=np.zeros((3,Construction_year))

    for year in range(int(Construction_year)):
        #1
        worksheet.write(row, col+year, year+1, bold)

        #2
        worksheet.write(row+1, col+year,' ',answer_format)

        #3
        worksheet.write(row+2, col+year,' ',answer_format)

        #4
        worksheet.write(row+3, col+year,' ',answer_format)

        #5
        worksheet.write(row+4, col+year,' ',answer_format)

    worksheet.write('F9','总计', bold)
    worksheet.write('F10',' ',answer_format)

    #%% 固定资产折旧
    T2 = (
         ['固定资产折旧（含建设期利息）', ' '],
         ['固定资产折旧（不含建设期利息）',   ' '],
         ['年末等额还本付息', ' ']
     )
    row = 12
    col = 0
    for item, item2 in (T2):
         worksheet.write(row, col,     item, bold)
         worksheet.write(row, col + 1, item2 ,answer_format)
         row += 1


    #%% 借款还本付息计划表
    Name2=(
          ["序号","项目"],
          ["1","固定资产借款"],
          ["1.1","期初借款余额"],
          [" ","当期借款支用"],
          [" ","本期应计利息"],
          ["1.2","当期还本付息"],
          [" ","其中:还本"],
          [" " ,"   付息"],
          ["1.3","期末借款余额"],
          ["2","流动资金借款"],
          ["2.1","期初借款余额"],
          ["2.2","当期还本付息"],
          [" ","其中:还本"],
          [" ","    付息"],
          ["2.3","期末借款余额"],
          ["3","合计"],
          ["3.1","年初借款余额"],
          ["3.2","当期还本付息"],
          [" ","其中:还本"],
          [" ","    付息"],
          ["3.3","期末借款余额"]
        );
    row = 16
    col = 0
    for item1, item2  in (Name2):
         worksheet.write(row, col,     item1, bold)
         worksheet.write(row, col + 1, item2, bold)
         row += 1

    ## 年份
    row = 16
    col = 2
    for year  in range(Construction_year+Operation_year):
        worksheet.write(row, col,  year+1, bold)
        col += 1

    ## 建设期还款计划
    Table2=np.zeros((17,Construction_year+Operation_year)) #17行数字需要填写
    row = 18
    col = 2
    for year in range(Construction_year):
        #1
        worksheet.write(row, col+year,' ',answer_format)

        #2
        worksheet.write(row+1, col+year,' ',answer_format)

        #3
        worksheet.write(row+2, col+year,' ',answer_format)

        #4-6
        for i in range(4,7,1):
            worksheet.write(row+i-1, col+year,' ',answer_format)

        #7
        worksheet.write(row+6, col+year,' ',answer_format)

        #8-12
        for i in range(8,13,1):
            worksheet.write(row+i, col+year,' ',answer_format)

        #13

        worksheet.write(row+14, col+year,' ',answer_format)

        #14-16
        for i in range(14,17,1):
            worksheet.write(row+i+1, col+year,' ',answer_format)

        #17
        worksheet.write(row+18, col+year,' ',answer_format)

    ## 还款期还款计划
    for year in range(Construction_year,Operation_year+Construction_year,1):
        #1
        worksheet.write(row, col+year,' ',answer_format)

        #2
        worksheet.write(row+1, col+year,' ',answer_format)

        #3
        worksheet.write(row+2, col+year,' ',answer_format)

        #4
        worksheet.write(row+3, col+year,' ',answer_format)

        #5
        worksheet.write(row+4, col+year,' ',answer_format)

        #6
        worksheet.write(row+5, col+year,' ',answer_format)

        #7
        worksheet.write(row+6, col+year,' ',answer_format)

        #8-12
        for i in range(8,13,1):
            worksheet.write(row+i, col+year,' ',answer_format)

        #13
        worksheet.write(row+14, col+year,' ',answer_format)

        #14-16
        for i in range(14,17,1):
            worksheet.write(row+i+1, col+year,' ',answer_format)

        #17
        worksheet.write(row+18, col+year,' ',answer_format)


    #  Sheet 2 项目投资现金流量表
    worksheet2 = workbook.add_worksheet('项目投资现金流量表')

    worksheet2.merge_range('B1:G1',"项目投资现金流量表   单位：万元", merge_format)

    Name3= ([
        "项目",
        "1 现金流入",
        "1.1 营业收入",
        "1.2 回收固定资产余值",
        "1.3 回收流动资金",
        "2 现金流出",
            "2.1 建设投资",
        "2.2 流动资金",
        "2.3 经营成本",
        "2.4 税金及附加",
        "3 所得税前净现金流量 (1-2)",
        "4 累计所得税前净现金流量",
        "3' 贴现后所得税前净现金流量",
        "4' 累计贴现所得税前净现金流量",
        "5 调整所得税",
        "6 所得税后净现金流量 (3-5)",
        "7 累计所得税后净现金流量",
        "6' 贴现后所得税后净现金流量 ",
        "7' 累计贴现所得税后净现金流量"
        ])

    #  表格项目
    row = 1
    col = 0
    for name in (Name3):
         worksheet2.write(row, col, name, bold)
         row += 1

    ## 年份
    row = 1
    col = 1
    for year  in range(Construction_year+Operation_year):
        worksheet2.write(row, col,  year, bold)
        col += 1

    # 资本金分配比例提前计算

    ## 表格内容
    Table3 = np.zeros((18,Construction_year+Operation_year)) #18行数字需要填写
    row = 2
    col = 1

    for year in range(Construction_year):
        #1-4
        for i in range(4):
            worksheet2.write(row+i, col+year,' ',answer_format)

        #5
        worksheet2.write(row+4, col+year,' ',answer_format)

        #6
        worksheet2.write(row+5, col+year,' ',answer_format)

        #7-9
        for i in range(7,10,1):
            worksheet2.write(row+i-1, col+year,' ',answer_format)

        #10
        worksheet2.write(row+9, col+year,' ',answer_format)

        #11
        worksheet2.write(row+10, col+year,' ',answer_format)

        #12
        worksheet2.write(row+11, col+year,' ',answer_format)

        #13
        worksheet2.write(row+12, col+year,' ',answer_format)

        #14
        worksheet2.write(row+13, col+year,' ',answer_format)

        #15
        worksheet2.write(row+14, col+year,' ',answer_format)

        #16
        worksheet2.write(row+15, col+year,' ',answer_format)

        #17
        worksheet2.write(row+16, col+year,' ',answer_format)

        #18
        worksheet2.write(row+17, col+year,' ',answer_format)


    #运营期 变量提前计算


    #运营期现金流量计划
    for year in range(Construction_year,Operation_year+Construction_year,1):
        #1
        worksheet2.write(row, col+year,' ',answer_format)

        #2
        worksheet2.write(row+1, col+year,' ',answer_format)

        #3
        worksheet2.write(row+2, col+year,' ',answer_format)

        #4
        worksheet2.write(row+3, col+year,' ',answer_format)

        #5
        worksheet2.write(row+4, col+year,' ',answer_format)

        #6
        worksheet2.write(row+5, col+year,' ',answer_format)

        #7
        worksheet2.write(row+6, col+year,' ',answer_format)

        #8
        worksheet2.write(row+7, col+year,' ',answer_format)

        #9
        worksheet2.write(row+8, col+year,' ',answer_format)

        #10
        worksheet2.write(row+9, col+year,' ',answer_format)

        #11
        worksheet2.write(row+10, col+year,' ',answer_format)

        #12
        worksheet2.write(row+11, col+year,' ',answer_format)

        #13
        worksheet2.write(row+12, col+year,' ',answer_format)

        #14
        worksheet2.write(row+13, col+year,' ',answer_format)

        #15
        worksheet2.write(row+14, col+year,' ',answer_format)

        #16
        worksheet2.write(row+15, col+year,' ',answer_format)

        #17
        worksheet2.write(row+16, col+year,' ',answer_format)

        #18
        worksheet2.write(row+17, col+year,' ',answer_format)



    #回收期提前计算
    Name_temp= (["税前静态回收期",' '],
            ["税后静态回收期",' '],
            ["税前动态回收期",' '],
            ["税后动态回收期",' '])

    #  表格项目
    row = 21
    col = 0
    for name, item in (Name_temp):
        worksheet2.write(row, col, name, bold)
        worksheet2.write(row, col + 1, item, answer_format)
        row += 1


    #内部收益率提前计算

    #内部收益率
    row = 26
    col = 0
    Name_temp_1= (["所得税前内部收益率", ' '],
                  ["所得税后内部收益率", ' ']
                  )

    for name, item in (Name_temp_1):
        worksheet2.write(row, col, name, bold)
        worksheet2.write(row, col + 1, item, answer_format)
        row += 1

    worksheet2.write('C27', "%")
    worksheet2.write('C28', "%")

    #  Sheet 3  项目资本金现金流量表
    worksheet3 = workbook.add_worksheet('项目资本金现金流量表')

    #  Sheet 4  利润表
    worksheet4 = workbook.add_worksheet('利润表')
    worksheet4.merge_range('B1:G1',"利润表   单位：万元", merge_format)

    Name4 = ([
        "项目",
        "1 营业收入",
        "2 税金及附加",
        "3 总成本费用",
        "4 补贴收入",
        "5 利润总额 (1-2-3+4)",
        "6 弥补以前年度亏损",
        "7 应纳所得税额 (5-6)",
        "8 所得税",
        "9 净利润 (7-8)",
        "10 应支付利息",
        "11 息税前利润 (EBIT)",
        "12 还本付息来源 (9+10+折旧)",
        ])

    #  表格项目
    row = 1
    col = 0
    for name in (Name4):
         worksheet4.write(row, col, name, bold)
         row += 1

    ## 年份
    row = 1
    col = 1
    for year  in range(Construction_year,Operation_year+Construction_year,1):
        worksheet4.write(row, col,  year, bold)
        col += 1

    Table4 = np.zeros((12,Operation_year))
    row = 2
    col = 1

    for year in range(Operation_year):
        #1
        worksheet4.write(row, col+year,' ',answer_format)

        #2
        worksheet4.write(row+1, col+year,' ',answer_format)

        #3
        worksheet4.write(row+2, col+year,' ',answer_format)

        #4
        worksheet4.write(row+3, col+year,' ',answer_format)

        #5 =1-2-3+4
        worksheet4.write(row+4, col+year,' ',answer_format)

        #6
        worksheet4.write(row+5, col+year,' ',answer_format)

        #7
        worksheet4.write(row+6, col+year,' ',answer_format)

        #8
        worksheet4.write(row+7, col+year,' ',answer_format)

        #9
        worksheet4.write(row+8, col+year,' ',answer_format)

        #10
        worksheet4.write(row+9, col+year,' ',answer_format)

        #11
        worksheet4.write(row+10, col+year,' ',answer_format)

        #12
        worksheet4.write(row+11, col+year,' ',answer_format)


    ## 重返 sheet 3 做表

    worksheet3.merge_range('B1:G1',"项目资本金现金流量表   单位：万元", merge_format)

    ## 项目
    Name5 = ([
        "项目",
        "1 现金流入",
        "1.1 营业收入",
        "1.2 补贴收入",
        "1.3 回收固定资产余值",
        "1.4 回收流动资金",
        "2 现金流出",
        "2.1 项目资本金",
        "2.2 借款本金偿还",
        "2.3 借款利息支付",
        "2.4 经营成本",
        "2.5 税金及附加",
        "3 所得税前净现金流量 (1-2)",
        "4 累计所得税前净现金流量",
        "3' 贴现后所得税前净现金流量",
        "4' 累计贴现所得税前净现金流量",
        "5 所得税",
        "6 所得税后净现金流量 (3-5)",
        "7 累计所得税后净现金流量",
        "6' 贴现后所得税后净现金流量 ",
        "7' 累计贴现所得税后净现金流量"
        ])

    row = 1
    col = 0
    for name in (Name5):
         worksheet3.write(row, col, name, bold)
         row += 1

    ## 年份
    row = 1
    col = 1
    for year  in range(Construction_year+Operation_year):
        worksheet3.write(row, col,  year, bold)
        col += 1

    #建立表格
    Table5=np.zeros((len(Name5)-1,Operation_year + Construction_year))

    # 项目资本金现金流量表变量提前计算

    Capital_Base_Investment = Capital_Base * Ratioset

    # 表格

    row = 2
    col = 1

    ## 建设期
    for year in range(Construction_year):
        #1-5
        for i in range(5):
            worksheet3.write(row+i, col+year,' ',answer_format)

        #6
        worksheet3.write(row+5, col+year,' ',answer_format)

        #7
        worksheet3.write(row+6, col+year,' ',answer_format)

        #8-11
        for i in range(7,11,1):
            worksheet3.write(row+i, col+year,' ',answer_format)

        #12
        worksheet3.write(row+11, col+year,' ',answer_format)

        #13
        worksheet3.write(row+12, col+year,' ',answer_format)

        #14
        worksheet3.write(row+13, col+year,' ',answer_format)

        #15
        worksheet3.write(row+14, col+year,' ',answer_format)

        #16
        worksheet3.write(row+15, col+year,' ',answer_format)

        #17
        worksheet3.write(row+16, col+year,' ',answer_format)

        #18
        worksheet3.write(row+17, col+year,' ',answer_format)

        #19
        worksheet3.write(row+18, col+year,' ',answer_format)

        #20
        worksheet3.write(row+19, col+year,' ',answer_format)


    ## 运营期

    for year in range(Construction_year,Operation_year+Construction_year,1):
        #1
        worksheet3.write(row, col+year,' ',answer_format)

        #2
        worksheet3.write(row+1, col+year,' ',answer_format)

        #3
        worksheet3.write(row+2, col+year,' ',answer_format)

        #4
        worksheet3.write(row+3, col+year,' ',answer_format)

        #5
        worksheet3.write(row+4, col+year,' ',answer_format)

        #6
        worksheet3.write(row+5, col+year,' ',answer_format)

        #7
        worksheet3.write(row+6, col+year,' ',answer_format)

        #8
        worksheet3.write(row+7, col+year,' ',answer_format)

        #9
        worksheet3.write(row+8, col+year,' ',answer_format)

        #10
        worksheet3.write(row+9, col+year,' ',answer_format)

        #11
        worksheet3.write(row+10, col+year,' ',answer_format)

        #12
        worksheet3.write(row+11, col+year,' ',answer_format)

        #13
        worksheet3.write(row+12, col+year,' ',answer_format)

        #14
        worksheet3.write(row+13, col+year,' ',answer_format)

        #15
        worksheet3.write(row+14, col+year,' ',answer_format)

        #16
        worksheet3.write(row+15, col+year,' ',answer_format)

        #17
        worksheet3.write(row+16, col+year,' ',answer_format)

        #18
        worksheet3.write(row+17, col+year,' ',answer_format)

        #19
        worksheet3.write(row+18, col+year,' ',answer_format)

        #20
        worksheet3.write(row+19, col+year,' ',answer_format)


    #回收期 提前计算

    Name_temp_2= (["税后静态回收期",' '],
            ["税后动态回收期",' '])

    #  表格项目
    row = 23
    col = 0
    for name, item in (Name_temp_2):
        worksheet3.write(row, col, name, bold)
        worksheet3.write(row, col + 1, item, answer_format)
        row += 1


    #内部收益率提前计算

    #内部收益率
    row = 26
    col = 0

    Name_temp_3= (["所得税前内部收益率", ' '],
                  ["所得税后内部收益率", ' ']
                  )

    for name, item in (Name_temp_3):
        worksheet3.write(row, col, name, bold)
        worksheet3.write(row, col + 1, item, answer_format)
        row += 1

    worksheet3.write('C27', '%')
    worksheet3.write('C28', '%')


    ## ROI and ROE
    row = 15
    col = 0

    Name_temp_4= (["总投资收益率 ROI", ' '],
                  ["总投资收益率 ROI , 不考虑利息", ' ']
                  )

    for name, item in (Name_temp_4):
        worksheet4.write(row, col, name, bold)
        worksheet4.write(row, col + 1, item, answer_format)
        row += 1

    worksheet4.write('C16', '%')
    worksheet4.write('C17', '%')

    row = 18
    col = 0

    worksheet4.write(row, col, "项目资本金净利润率 ROE", bold)
    worksheet4.write(row, col + 1, ' ',answer_format)

    worksheet4.write('C19', '%')

    ##   ICR and DSCR

    row = 20
    col = 0

    worksheet4.write(row, col, "利息备付率 ICR", bold)
    for i in range(Payment_Done_year):
        worksheet4.write(row, col + i + 1, ' ',answer_format)

    row = 22
    col = 0

    worksheet4.write(row, col, "偿债备付率 DSCR", bold)
    for i in range(Payment_Done_year):
        worksheet4.write(row, col + i + 1, ' ',answer_format)

    workbook.close()
    Label(root,text='作业已经生成,请在目录中查看',fg = "Red",font = "楷体 10").grid(row=8,column=0,columnspan=2,sticky=W+E+N+S, padx=20, pady=5)


Button(root,text='生成作业',width=10,command=show).grid(row=6,column=0,padx=10,pady=5)  # 设置 button 指定 宽度 , 并且 关联 函数 , 使用表格式布局 .
Button(root,text='退出',width=10,command=root.quit).grid(row=6,column=1,sticky=E,padx=10,pady=5)

Label(root,text='投资项目评估作业生成系统(学生版)v2.0\n 作者：Thomas\n 微博@士干土工',fg = "Black",font = "楷体").grid(row=7,column=0,columnspan=2,sticky=W+E+N+S, padx=20, pady=5)




mainloop()






# In[ ]:
