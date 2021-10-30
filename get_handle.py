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
        os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})
    def Process_exists(self):
        '''
        判断进程是否存在，存在就返回pid，不存在，启动程序，获取pid，返回pid
        :return: pid
        '''

        pids=psutil.pids()
        for pid in pids:
            proc=psutil.Process(pid)
            if str(proc.name())==self.name:
                os.system(self.close_cmd)
                os.system(self.start_cmd)
                ggh_app_handle=self.get_window_authority()
                #you_name_app = Application(backend="uia").connect(path=r"D:/NLEMR/aECG-One/Galaxy.Gemini.Shell.exe")
                ggh_main_handle=ggh_app_handle.window(title="心电医生工作站", auto_id="ShellView", control_type="Window")
                ggh_main_handle.wait(wait_for="exists enabled ",timeout=5,retry_interval=3)
                #ggh_main_handle.print_control_identifiers()#遍历打印控件，平常不使用
                return ggh_main_handle

        if self.you_path_id==None:
            os.system(self.start_cmd)

            Ggh_handle=self.get_window_authority()
            time.sleep(2)
            ggh_main_handle=Ggh_handle.top_window(name="心电医生工作站", auto_id="ShellView", control_type="Window")
            #ggh_main_handle.print_control_identifiers()

            return ggh_main_handle


    def get_window_authority(self):
        '''
        根据pid，连接登录窗口，进行登录，获取主程序窗口
        :return: 主程序窗口
        '''
        you_name_app = Application(backend="uia").connect(path=r"D:/NLEMR/aECG-One/Galaxy.Gemini.Shell.exe")

        ggh_handle=you_name_app.window(auto_id="Login")
        ggh_handle.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)

        username = ggh_handle.child_window(auto_id="CboUserName")
        username.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
        username.type_keys("qdrsh")

        password = ggh_handle.child_window(auto_id="TxtPwd")
        password.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
        password.type_keys("123456")

        BtnLogin = ggh_handle.child_window(auto_id="BtnLogin")
        BtnLogin.wait(wait_for="exists enabled ",timeout=3,retry_interval=3)
        BtnLogin.click()
        return you_name_app





if __name__=="__main__":
    handle().Process_exists()