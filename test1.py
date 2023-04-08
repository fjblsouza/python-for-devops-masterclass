#!/usr/bin/env python

import os, platform, subprocess, socket, psutil, cpuinfo, logging
logging.basicConfig(filename = 'example.log', format = '‘%(asctime)s %(message)s' , level = logging.DEBUG)

#command = "cat /proc/cpuinfo"
#print(subprocess.check_output(ncpu, shell=True).strip())

kb = float(1024)
mb = float(kb ** 2)
gb = float(kb ** 3)

memTotal = int(psutil.virtual_memory()[0]/gb)
memFree = int(psutil.virtual_memory()[1]/gb)
memUsed = int(psutil.virtual_memory()[3]/gb)
memPercent = int(memUsed/memTotal*100)
storageTotal = int(psutil.disk_usage('/')[0]/gb)
storageUsed = int(psutil.disk_usage('/')[1]/gb)
storageFree = int(psutil.disk_usage('/')[2]/gb)
storagePercent = int(storageUsed/storageTotal*100)
info = cpuinfo.get_cpu_info()['brand_raw']

def load_avg():
    logging.debug('---------- Load CPU Average 1min ----------')
    logging.debug(round(os.getloadavg()[0],2))
    logging.debug('---------- Load CPU Average 5min ----------')
    logging.debug(round(os.getloadavg()[1],2))
    logging.debug('---------- Load CPU Average 15min----------')
    logging.debug(round(os.getloadavg()[2],2))

def system():
    core = os.cpu_count()
    host = socket.gethostname()
    #logging.debug('---------- System Info ----------')
    logging.debug('---------- Hostname ----------')
    logging.debug(host)
    logging.debug('---------- System----------')
    logging.debug((platform.system(),platform.machine()))
    #logging.debug('---------- System ----------')
    #logging.debug(platform.machine())
    logging.debug('---------- Kernel ----------')
    logging.debug(platform.release())
    print('Compiler     :', platform.python_compiler())
    print('CPU          :',info, core,"(Core)")
    print("Memory       :", memTotal,"GiB")
    print("Disk         :", storageTotal,"GiB")

def cpu():
    print()
    print('---------- CPU ----------')
    print()
    print("CPU Usage: ",cpuUsage,"GiB")

def memory():
    print()
    print('---------- RAM usage ----------')
    print()
    print("RAM Used: ",memUsed,"GiB /",memTotal,"GiB","(",memPercent,"%",")")
    print()
    print('---------- Disk usage ----------')
    print()
    print("Disk Used: ",storageUsed,"GiB /",storageTotal,"GiB","(",storagePercent,"%",")")
    cmd = "df -Th"
    # returns output
    returned_value = subprocess.call(cmd, shell=True)
    print()

def main():
    #service()
    system()
    load_avg()
    memory()
main()





