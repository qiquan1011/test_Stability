import time

import psutil

process_lst=[]
def getProcess(name):
    all_pids  = psutil.pids()
    for pid in all_pids:
        try:
            p = psutil.Process(pid)
        except Exception as e:
            print(e)
        #print(p)
        if str(p.name()) == name:
            t = time.localtime()
            cm_time = '%d:%d:%d' % (t.tm_hour, t.tm_min, t.tm_sec)
            memory=p.memory_percent()
            cpu_1=p.cpu_percent(None)
            time.sleep(1)
            cpu=p.cpu_percent(None)
            print(cpu)



    return cm_time,memory,cpu
'''            
process_lst2=getProcess("Galaxy.Gemini.Shell.exe")
    # 获取内存利用率：
for process_instance in process_lst2:
    print("内存使用率：",process_instance.memory_percent())

    # 获取cpu利用率：
for process_instance in process_lst2:

    print(process_instance.cpu_percent(interval=1))

#time.sleep(2)
#for process_instance in process_lst2:
    print(process_instance.cpu_percent(None))
'''

if __name__=="__main__":
    while True:
        getProcess("Galaxy.Gemini.Shell.exe")