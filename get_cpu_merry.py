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
                t = time.localtime()
                cm_time = '%d:%d:%d' % (t.tm_hour, t.tm_min, t.tm_sec)
                memory=p.memory_percent()
                cpu_1=p.cpu_percent(None)
                time.sleep(5)
                cpu=p.cpu_percent(None)
                a=cm_time,memory,cpu
                num_cls.append(a)
                return cm_time,memory,cpu

def cpu_men_main():
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    fname=now + r"-report.csv"
    file_path="D:\\pythonProject\\pythonProject\\test_Stability\\Cpu_Men\\"
    cpu_men_parh=file_path +fname
    print(cpu_men_parh)
    with open("%s" % cpu_men_parh,"w") as f:
        title_str= "Time,Men,Cpu"
        f.write(title_str + "\n")
        while True:
            info=getProcess("Galaxy.Gemini.Shell.exe")
            tmp_str= "%4s,%5s,%4s" % (info[0],info[1],info[2])
            f.write(tmp_str + "\n")





if __name__=="__main__":
        cpu_men_main()

