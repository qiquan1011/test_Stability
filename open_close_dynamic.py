import textwrap
import time
import traceback
from pprint import pprint

import psutil
from pywinauto import mouse, Application

from get_handle import handle
def openAndclose_holters_and_Abp():
    '''
    实现主程序不断启用/关闭动态心态以及动态血压子程序
    :return:
    '''
    try:
        num=0
        ggh_handle=handle().Process_exists()
        ggh_handle.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
        for i in range(10):
            num=num+1
            print(num)
            mouse.move(coords=(1146,110))
            mouse.click(button="left",coords=(1146,110))
        #ggh_handle.print_control_identifiers()
            a=ggh_handle.child_window(title="动态心电", auto_id="DiagHolterEcg", control_type="Pane").child_window(title="行 1", control_type="Custom")
            a.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
            a.double_click_input(button='left')
            time.sleep(2)
            pids=psutil.pids()
            for pid in pids:
                try:
                    proc=psutil.Process(pid)
                except Exception as e:
                    print(e)
                if str(proc.name())=="NL.CardioCareDoctor.Container.WPF4.exe":
                    you_diag_name_app = Application(backend="uia").connect(path=r"D:/NLEMR/aECG-One/NL.CardioCareDoctor.Container.WPF4.exe")
                    handel=you_diag_name_app.window(title="诊断程序", control_type="Window")
                    handel.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
            #handel.print_control_identifiers()
                    c=handel.child_window(auto_id="PART_CloseBtn", control_type="Button")
                    c.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
                    c.click()
            mouse.move(coords=(1774,114))
            mouse.click(button="left",coords=(1774,114))
            b=ggh_handle.child_window(title="动态血压", auto_id="DiagAbp", control_type="Pane").child_window(title="行 1", control_type="Custom")
            b.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
            b.double_click_input(button='left')
            time.sleep(1)
            pids=psutil.pids()
            for pid in pids:
                try:
                    proc=psutil.Process(pid)
                except Exception as e:
                    print(e)

                if str(proc.name())=="NLC.ABPCare.Client.exe":
                    you_abp_name_app = Application(backend="uia").connect(path=r"D:/NLEMR/aECG-One/NLC.ABPCare.Client.exe")

                    handel_1=you_abp_name_app.window(title="心电及电生理网络系统软件", control_type="Window")
                    handel_1.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
            #handel_1.print_control_identifiers()
                    d=handel_1.child_window(auto_id="btnBack")
                    d.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
                    d.click_input(button="left")
    except :
        print(traceback.format_exc())
    finally:
        print("连接超时，请稍后再试！！！")

if __name__=="__main__":
    openAndclose_holters_and_Abp()
