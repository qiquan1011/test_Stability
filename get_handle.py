import os
import time
import traceback

import psutil as psutil
from pywinauto import Application, ElementNotFoundError


class handle():
    def __init__(self):
        self.name="Galaxy.Gemini.Shell.exe"
        self.name_path=r"D:/NLEMR/aECG-One"
        self.start_cmd= 'd: & cd ' + self.name_path + ' & start '+self.name
        self.close_cmd='d: & cd ' + self.name_path + ' & taskkill /f /t /im '+self.name
        self.you_path_id=None
        self.process_lst = []
        self.screen_path = "D:\\pythonProject\\pythonProject\\test_Stability\\testScreen\\"
        os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})
    def Process_exists(self):
        '''
        判断进程是否存在，存在就返回pid，不存在，启动程序，获取pid，返回pid
        :return: pid
        '''

        global ggh_main_handle, ggh_main_handle, proc
        pids=psutil.pids()
        for pid in pids:
            try:
                proc=psutil.Process(pid)
            except Exception as e:
                print(e)
            if str(proc.name())==self.name:
                self.you_path_id=pid
                #os.system(self.close_cmd)
                #os.system(self.start_cmd)
                #ggh_app_handle=self.get_window_authority()
                you_name_app = Application(backend="uia").connect(path=r"D:/NLEMR/aECG-One/Galaxy.Gemini.Shell.exe")

                try:
                    ggh_main_handle=you_name_app.window(title="心电医生工作站", auto_id="ShellView", control_type="Window")
                    ggh_main_handle.wait(wait_for="exists enabled ",timeout=10,retry_interval=3)
                except:
                    print("无法获取句柄，可能是登录失败，请检查！！！！")
                #ggh_main_handle.print_control_identifiers()#遍历打印控件，平常不使用
                return ggh_main_handle

        if self.you_path_id==None:
            os.system(self.start_cmd)

            Ggh_handle=self.get_window_authority()
            time.sleep(2)
            try:
                ggh_main_handle=Ggh_handle.window(title="心电医生工作站", auto_id="ShellView", control_type="Window")
                ggh_main_handle.wait(wait_for="exists enabled ",timeout=10,retry_interval=3)
            except:
                print("无法获取句柄，可能是登录失败，请检查！！！！")
            #ggh_main_handle.print_control_identifiers()

            return ggh_main_handle


    def get_window_authority(self):
        '''
        根据pid，连接登录窗口，进行登录，获取主程序窗口
        :return: 主程序窗口
        '''
        global you_name_app, ggh_handle
        try:
            you_name_app = Application(backend="uia").connect(path=r"D:/NLEMR/aECG-One/Galaxy.Gemini.Shell.exe")
            ggh_handle=you_name_app.window(auto_id="Login")
            ggh_handle.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
        except:
            print("无法获取句柄，可能应用启动失败，请前往查看！！！")

        try:
            username = ggh_handle.child_window(auto_id="CboUserName")
            username.type_keys("qdrsh")
        except:
            username_path=self.screen_path+"输入用户名失败.png"
            ggh_handle.capture_as_image().save(username_path)
        try:
            password = ggh_handle.child_window(auto_id="TxtPwd")
            password.type_keys("123456")
        except:
            password_path=self.screen_path+"密码输入失败.png"
            ggh_handle.capture_as_image().save(password_path)
        try:
            BtnLogin = ggh_handle.child_window(auto_id="BtnLogin")
            BtnLogin.click()
        except:
            BtnLogin_path=self.screen_path+"登录失败.png"
            ggh_handle.capture_as_image().save(BtnLogin_path)

        return you_name_app





if __name__=="__main__":
    handle().Process_exists()