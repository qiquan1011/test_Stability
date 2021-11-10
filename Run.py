import multiprocessing
import threading
import time

from get_cpu_merry import cpu_men_main
from open_close_dynamic import openAndclose_holters_and_Abp
def main():

    t1= multiprocessing.Process(target=openAndclose_holters_and_Abp)
    t1.start()
    time.sleep(2)
    t2=multiprocessing.Process(target=cpu_men_main)
    t2.start()

if __name__=="__main__":
    main()