import datetime
import threading
import time

import psutil
import xlwt

process_lst=[]
def getProcess(name):
    num_cls=[]
    all_pids  = psutil.pids()
    for pid in all_pids:
        try:
            p = psutil.Process(pid)
        except Exception as e:
            print(e)
        #print(p)

        if str(p.name()) == name:
            #start_time=datetime.datetime.now()
            while True:
                t = time.localtime()
                cm_time = '%d:%d:%d' % (t.tm_hour, t.tm_min, t.tm_sec)
                memory=p.memory_percent()
                cpu_1=p.cpu_percent(None)
                time.sleep(1)
                cpu=p.cpu_percent(None)
                a=cm_time,memory,cpu
                num_cls.append(a)
    return num_cls






def get_cpu_and_memory():
    '''
将得到的内存使用率和CPU率使用率，写入表格，生成折线图
:return:
'''
excelpath =('D:\\user.xls')  #新建excel文件
workbook = xlwt.Workbook(encoding='utf-8')  #写入excel文件
sheet = workbook.add_sheet('Sheet1',cell_overwrite_ok=True)  #新增一个sheet工作表
headlist=[u'时间',u'内存使用率',u'cpu使用率']   #写入数据头
row=0
col=0
for head in headlist:
    sheet.write(row,col,head)
    col=col+1
num=getProcess("Galaxy.Gemini.Shell.exe")
for i in range(1,len(num)):
    for j in range(0,3):
        sheet.write(i,j,num[i-1][j])
workbook.save(excelpath) #保存



if __name__=="__main__":
        getProcess("Galaxy.Gemini.Shell.exe")

