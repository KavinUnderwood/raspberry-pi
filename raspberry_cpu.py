# Copyright (C) 2017 wanghaojie                                         *
# All rights reserved                                                        *
#                                                                            *
# @author  :   rooster                                                         *
# @date    :   2017-10-13                                                    *                                                               *
import os
# 主要是利用原本的资源及驱动获取数据
# CPU温度、使用率
# 内存容量、使用容量、剩余容量
# 磁盘容量、占有控件、占有率
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))
                                                          
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])
                            
def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))

                                             
def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            return(line.split()[1:5])


# CPU 信息
CPU_temp = getCPUtemperature()
CPU_usage = getCPUuse()

# RAM 信息
RAM_stats = getRAMinfo()
RAM_total = round(int(RAM_stats[0]) / 1000,1)
RAM_used = round(int(RAM_stats[1]) / 1000,1)
RAM_free = round(int(RAM_stats[2]) / 1000,1)

# Disk 信息
DISK_stats = getDiskSpace()
DISK_total = DISK_stats[0]
DISK_used = DISK_stats[1]
DISK_perc = DISK_stats[3]

if __name__ == '__main__':
    print('')
    print('CPU Temperature = '+CPU_temp+'*C')
    print('CPU Use = '+CPU_usage+'%')
    print('')
    print('RAM Total = '+str(RAM_total)+' MB')
    print('RAM Used = '+str(RAM_used)+' MB')
    print('RAM Free = '+str(RAM_free)+' MB')
    print('')
    print('DISK Total Space = '+str(DISK_total)+'B')
    print('DISK Used Space = '+str(DISK_used)+'B')
    print('DISK Used Percentage = '+str(DISK_perc))
