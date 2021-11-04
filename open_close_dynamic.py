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
        path="D:\\pythonProject\\pythonProject\\test_Stability\\testScreen\\"
        try:
            DiagHolterEcg=ggh_handle.child_window(title="动态心电", auto_id="lblItemName", control_type="Text")
            #DiagHolterEcg.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
            DiagHolterEcg.click_input()
        except:
            save_path=path+ "第"+ str(num)+"次点击动态心电tab页.png"
            ggh_handle.capture_as_image().save(save_path)
        #ggh_handle.print_control_identifiers()
        try:
            a=ggh_handle.child_window(title="动态心电", auto_id="DiagHolterEcg", control_type="Pane").child_window(title="行 1", control_type="Custom")
            #a.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
            a.double_click_input(button='left')
        except:
            report_path=path+"第"+ str(num)+"次点动列表报告.png"
            ggh_handle.capture_as_image().save(report_path)
        time.sleep(2)
        pids=psutil.pids()

        for pid in pids:
            try:
                proc = psutil.Process(pid)
            except Exception as e:
                print(e)
            if str(proc.name())=="NL.CardioCareDoctor.Container.WPF4.exe":
                try:
                    you_diag_name_app = Application(backend="uia").connect(path=r"D:/NLEMR/aECG-One/NL.CardioCareDoctor.Container.WPF4.exe")
                    handel = you_diag_name_app.window(title="诊断程序", control_type="Window")
                    handel.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
                except:
                    holtel_path=path+"第"+ str(num)+"次连接不上动态心电程序.png"
                    handel.capture_as_image().save(holtel_path)
            #handel.print_control_identifiers()
                try:
                    c=handel.child_window(auto_id="PART_CloseBtn", control_type="Button")
                    c.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
                    c.click()
                except:
                    holtel_close_path=path+"第"+ str(num)+"次关闭动态心电失败.png"
                    handel.capture_as_image().save(holtel_close_path)
        if you_diag_name_app is None:
            fail_path=path+"第"+ str(num)+"次打开报告失败.png"
            ggh_handle.capture_as_image().save(fail_path)

        try:
            DiagnoseSelectorControl=ggh_handle.child_window(title="动态血压", auto_id="lblItemName", control_type="Text")
            #DiagnoseSelectorControl.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
            DiagnoseSelectorControl.click_input()
        except:
            abp_tab_path=path+"第"+ str(num)+"次点击动态血压tab页.png"
            ggh_handle.capture_as_image().save(abp_tab_path)
        try:
            b=ggh_handle.child_window(title="动态血压", auto_id="DiagAbp", control_type="Pane").child_window(title="行 1", control_type="Custom")
        #b.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
            b.double_click_input(button='left')
        except:
            abp_report_path=path+"第"+ str(num)+"次点击血压列表数据.png"
            ggh_handle.capture_as_image().save(abp_report_path)
        time.sleep(1)
        pids=psutil.pids()
        for pid in pids:
            try:
                proc=psutil.Process(pid)
            except Exception as e:
                print(e)
            if str(proc.name())=="NLC.ABPCare.Client.exe":
                try:
                    you_abp_name_app = Application(backend="uia").connect(path=r"D:/NLEMR/aECG-One/NLC.ABPCare.Client.exe")
                    handel_1 = you_abp_name_app.window(title="心电及电生理网络系统软件", control_type="Window")
                    handel_1.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
                except:
                    abp_path=path+"第"+ str(num)+"次连接不上血压程序.png"
                    handel_1.capture_as_image().save(abp_path)
            #handel_1.print_control_identifiers()
                try:
                    d=handel_1.child_window(auto_id="btnBack")
                    d.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
                    d.click_input(button="left")
                except:
                    return_path=path+"第"+ str(num)+"次关闭血压程序失败.png"
                    handel_1.capture_as_image().save(return_path)
        if you_abp_name_app is None:
                abp_file_path=path+"第"+ str(num)+"次血压报告打开失败.png"
                ggh_handle.capture_as_image().save(abp_file_path)


        endtime=datetime.datetime.now()
        times=endtime-starttime
        if times.seconds > 5:
            break

if __name__=="__main__":
    openAndclose_holters_and_Abp()
