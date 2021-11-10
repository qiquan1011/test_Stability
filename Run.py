import multiprocessing
import threading
import time

from get_cpu_merry import cpu_men_main
from open_close_dynamic import openAndclose_holters_and_Abp

def main():
    # 使用进程分别进行业务操作和CPU内存的获取
    openAndclose= multiprocessing.Process(target=openAndclose_holters_and_Abp)
    openAndclose.start()

    time.sleep(2)

    cpuAndmen=multiprocessing.Process(target=cpu_men_main)
    cpuAndmen.start()

if __name__=="__main__":
    main()