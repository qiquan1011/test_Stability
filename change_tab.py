import multiprocessing
import threading
import traceback

from pywinauto import mouse
import string
import xlwt

import get_cpu_merry
from get_handle import handle
def tab_change():
    '''
    根据坐标位置，点击tab页，并同时获取cpu使用率和内存使用率
    :return: 内存使用率和CPU使用率
    '''
    try:
        ggh_handle=handle().Process_exists()
        ggh_handle.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
        cls=[(1774,114),(1146,110),(593,103)]
        b=20
        num_cls=[]
        while b>=10:
            b=b-1
            for i in cls:
                mouse.move(coords=i)
                mouse.click(button="left",coords=i)
                num=get_cpu_merry.getProcess("Galaxy.Gemini.Shell.exe")
                num_cls.append(num)
    except:
        print(traceback.format_exc())
    finally:
        print("请求超时，请稍后再试！")

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
    num_cls_cls=tab_change()
    for i in range(1,len(num_cls_cls)):
        for j in range(0,3):
            sheet.write(i,j,num_cls_cls[i-1][j])

    workbook.save(excelpath) #保存



if __name__=="__main__":

     get_cpu_and_memory()


