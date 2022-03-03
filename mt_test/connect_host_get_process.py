import subprocess
import time
import multiprocessing as mp
import smtplib
import _thread


user = "ubuntu"
hosts = []
for i in range(10):
    hosts.append("192.168.0.192")

command = "ps -ef  |grep -v \"grep\" |grep -i \"/usr/sbin/sshd\" > /dev/null && echo $(hostname)\" :sshd running\" || echo $(hostname)\" :sshd not running\""



response = []

now_time = time.time()

with open("result.txt","w+") as file1:
    for host in hosts:
        try:
            output = subprocess.check_output(["ssh","-q",f"{user}@{host}",command])
            resp = output.decode().strip()
            response.append(resp)
            file1.write(f"{resp}\n")
        except Exception as err:
            print(err)
print(f"Total time taken for running command in all host sequentially : {time.time() - now_time}")


print(response)



sender = "pdk@gmail.com"
receivers = "pdkgroup@gmail.com"
message = response


# try:
#     smtpObj = smtplib.SMTP("localhost")
#     smtpObj.sendmail(sender, receivers, message)
# except smtpException:
#     print("Not sent")


##Multiprocesssing
respn1 = []
def fun1(host,file2):
    print(f"Calling {host}")
    with open("result1.txt","w+") as file2:
        try:
            output = subprocess.check_output(["ssh","-q",f"{user}@{host}",command])
            resp = output.decode().strip()
            print(resp)
            respn1.append(resp)
            file2.write(f"{resp}\n")
        except Exception as err:
            print(err)


# jobs = []
# now_time = time.time()

# for host in hosts:
#     job = mp.Process(target=fun1, args=(host))
#     jobs.append(job)
#     job.start()
    

# print(respn1)


# print(f"Total time taken for running command in all hosts parallely : {time.time() - now_time}")

now_time = time.time()
threads = []

[threads.append(f"Thread-{x}") for x in range(1,11)]

print(threads)
for thread in threads:
    for host in hosts:
        _thread.start_new_thread( fun1, (host,))
        # job = mp.Process(target=fun1, args=(host))
        # jobs.append(job)
        # job.start()

print(f"Total time taken for running command in all hosts parallely : {time.time() - now_time}")