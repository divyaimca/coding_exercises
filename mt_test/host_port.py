import socket
import multiprocessing as mp
from multiprocessing import Pool
import time
import os


#ncpus=int(os.getenv('NUM_PROCS'))
pool = mp.Pool(processes=4)

jobs = []




def host_port_check(host,port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        status = sock.connect_ex((host, port))
        sock.close()
    except Exception as err:
        print(err)

    if status == 0:
        return "Success : Port is open"
    else:
        return "Unsuccessfull : Port not listening"



if __name__ == "__main__":
    file1 = input("Enter the file name :")
    t1 = time.time()
    try:
        with open(file1,"r") as f:
            for line in f:
                h = line.split()[0]
                p = int(line.split()[1])
                #print(host_port_check(h,p))
                jobs.append(pool.apply_async(host_port_check, (h,p)))
        
        for job in jobs:
            job.get()

        pool.close()
        pool.join()
    except Exception as err:
        print(err)
    
    


    print(f"Total time : {time.time() - t1}")

    # p = int(input("Enter the port number :"))
    # print(host_port_check(h,p))

    # a = "192.168.0.186"
    # p = 22
    
    # with open("host","w+") as f:
    #     for i in range(1000):
    #         f.write(f"{a} {p}\n")

