import datetime
import os.path
import time
import psutil
from pywinauto import Application
from get_handle import handle


def openAndclose_holters_and_Abp():
    '''
    实现主程序不断启用/关闭动态心态以及动态血压子程序
    :return:
    '''
    global hotel_handel, proc, abp_handel
    you_diag_name_app = None
    you_abp_name_app = None
    ggh_handle = handle().Process_exists()
    #ggh_handle.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
    num = 0
    screen_path = "D:\\pythonProject\\pythonProject\\test_Stability\\testScreen\\"
    if os.path.exists(screen_path) is False:
        os.mkdir(screen_path)
    while True:
        num += 1
        try:
            DiagHolterEcg = ggh_handle.child_window(
                title="动态心电", auto_id="lblItemName", control_type="Text")
            #DiagHolterEcg.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
            DiagHolterEcg.click_input()
        except:
            save_path = screen_path + "第" + str(num)+"次点击动态心电tab页.png"
            ggh_handle.capture_as_image().save(save_path)
        # ggh_handle.print_control_identifiers()
        try:
            a = ggh_handle.child_window(title="动态心电", auto_id="DiagHolterEcg", control_type="Pane").child_window(
                title="行 1", control_type="Custom")
            #a.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
            a.double_click_input(button='left')
        except:
            report_path = screen_path+"第" + str(num)+"次点动列表报告.png"
            ggh_handle.capture_as_image().save(report_path)
        time.sleep(2)
        pids = psutil.pids()

        for pid in pids:
            try:
                proc = psutil.Process(pid)
            except Exception as e:
                print(e)
            if str(proc.name()) == "NL.CardioCareDoctor.Container.WPF4.exe":
                try:
                    you_diag_name_app = Application(backend="uia").connect(
                        path=r"D:/NLEMR/aECG-One/NL.CardioCareDoctor.Container.WPF4.exe")
                    hotel_handel = you_diag_name_app.window(
                        title="诊断程序", control_type="Window")
                    hotel_handel.wait(wait_for="exists enabled ",
                                      timeout=3, retry_interval=3)
                except:
                    holtel_path = screen_path+"第" + str(num)+"次连接不上动态心电程序.png"
                    ggh_handle.capture_as_image().save(holtel_path)
            # handel.print_control_identifiers()
                try:
                    c = hotel_handel.child_window(
                        auto_id="PART_CloseBtn", control_type="Button")
                    c.click()
                except:
                    holtel_close_path = screen_path + \
                        "第" + str(num)+"次关闭动态心电失败.png"
                    ggh_handle.capture_as_image().save(holtel_close_path)
        if you_diag_name_app is None:
            fail_path = screen_path+"第" + str(num)+"次打开报告失败.png"
            ggh_handle.capture_as_image().save(fail_path)

        try:
            DiagnoseSelectorControl = ggh_handle.child_window(
                title="动态血压", auto_id="lblItemName", control_type="Text")
            #DiagnoseSelectorControl.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
            DiagnoseSelectorControl.click_input()
        except:
            abp_tab_path = screen_path+"第" + str(num)+"次点击动态血压tab页.png"
            ggh_handle.capture_as_image().save(abp_tab_path)
        try:
            b = ggh_handle.child_window(title="动态血压", auto_id="DiagAbp", control_type="Pane").child_window(
                title="行 1", control_type="Custom")
        #b.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
            b.double_click_input(button='left')
        except:
            abp_report_path = screen_path+"第" + str(num)+"次点击血压列表数据.png"
            ggh_handle.capture_as_image().save(abp_report_path)
        time.sleep(1)
        pids = psutil.pids()
        for pid in pids:
            try:
                proc = psutil.Process(pid)
            except Exception as e:
                print(e)
            if str(proc.name()) == "NLC.ABPCare.Client.exe":
                try:
                    you_abp_name_app = Application(backend="uia").connect(
                        path=r"D:/NLEMR/aECG-One/Diagnosis/AbpCare/NLC.ABPCare.Client.exe")
                    abp_handel = you_abp_name_app.window(
                        title="心电及电生理网络系统软件", control_type="Window")
                    abp_handel.wait(wait_for="exists enabled ",
                                    timeout=3, retry_interval=3)
                except:
                    abp_path = screen_path+"第" + str(num)+"次连接不上血压程序.png"
                    ggh_handle.capture_as_image().save(abp_path)
            # handel_1.print_control_identifiers()
                try:
                    d = abp_handel.child_window(auto_id="btnBack")
                    d.click_input(button="left")
                except:
                    return_path = screen_path+"第" + str(num)+"次关闭血压程序失败.png"
                    ggh_handle.capture_as_image().save(return_path)
        if you_abp_name_app is None:
            abp_file_path = screen_path+"第" + str(num)+"次血压报告打开失败.png"
            ggh_handle.capture_as_image().save(abp_file_path)


if __name__ == "__main__":
    openAndclose_holters_and_Abp()
