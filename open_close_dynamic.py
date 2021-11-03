import datetime
import time
import psutil
from pywinauto import  Application
from get_handle import handle

def openAndclose_holters_and_Abp():
    '''
    实现主程序不断启用/关闭动态心态以及动态血压子程序
    :return:
    '''
    you_diag_name_app=None
    you_abp_name_app=None
    ggh_handle=handle().Process_exists()
    ggh_handle.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
    starttime = datetime.datetime.now()
    num=0
    while True:
        num+=1
        path="D:\\pythonProject\\pythonProject\\test_Stability\\testScreen\\"+ str(num) + ".png"

        try:
            DiagHolterEcg=ggh_handle.child_window(title="动态心电", auto_id="lblItemName", control_type="Text")
            #DiagHolterEcg.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
            DiagHolterEcg.click_input()
        except:
            ggh_handle.capture_as_image().save(path)
        #ggh_handle.print_control_identifiers()
        try:
            a=ggh_handle.child_window(title="动态心电", auto_id="DiagHolterEcg", control_type="Pane").child_window(title="行 1", control_type="Custom")
            #a.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
            a.double_click_input(button='left')
        except:
            ggh_handle.capture_as_image().save(path)
        time.sleep(2)
        pids=psutil.pids()
        for pid in pids:
            try:
                proc=psutil.Process(pid)
                if you_diag_name_app is None:
                    ggh_handle.capture_as_image().save(path)
                if str(proc.name())=="NL.CardioCareDoctor.Container.WPF4.exe":
                    try:
                        you_diag_name_app = Application(backend="uia").connect(path=r"D:/NLEMR/aECG-One/NL.CardioCareDoctor.Container.WPF4.exe")
                        handel=you_diag_name_app.window(title="诊断程序", control_type="Window")
                        handel.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
                    except:
                        handel.capture_as_image().save(path)
            #handel.print_control_identifiers()
                    try:
                        c=handel.child_window(auto_id="PART_CloseBtn", control_type="Button")
                        c.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
                        c.click()
                    except:
                        handel.capture_as_image().save(path)
                else:
                    break
            except Exception as e:
                print(e)
        try:
            DiagnoseSelectorControl=ggh_handle.child_window(title="动态血压", auto_id="lblItemName", control_type="Text")
            #DiagnoseSelectorControl.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
            DiagnoseSelectorControl.click_input()
        except:
            ggh_handle.capture_as_image().save(path)
        try:
            b=ggh_handle.child_window(title="动态血压", auto_id="DiagAbp", control_type="Pane").child_window(title="行 1", control_type="Custom")
        #b.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
            b.double_click_input(button='left')
        except:
            ggh_handle.capture_as_image().save(path)
        time.sleep(1)
        pids=psutil.pids()
        for pid in pids:
            try:
                proc=psutil.Process(pid)
                if you_abp_name_app is None:
                    ggh_handle.capture_as_image().save(path)
                if str(proc.name())=="NLC.ABPCare.Client.exe":
                    try:
                        you_abp_name_app = Application(backend="uia").connect(path=r"D:/NLEMR/aECG-One/NLC.ABPCare.Client.exe")
                        handel_1=you_abp_name_app.window(title="心电及电生理网络系统软件", control_type="Window")
                        handel_1.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
                    except:
                        handel_1.capture_as_image().save(path)
            #handel_1.print_control_identifiers()
                    try:
                        d=handel_1.child_window(auto_id="btnBack")
                        d.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
                        d.click_input(button="left")
                    except:
                        handel_1.capture_as_image().save(path)
                else:
                    break
            except Exception as e:
                print(e)
        endtime=datetime.datetime.now()
        times=endtime-starttime
        if times.seconds > 10:
            break
if __name__=="__main__":
    openAndclose_holters_and_Abp()
