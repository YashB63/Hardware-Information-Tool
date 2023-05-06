import platform
import psutil
import cpuinfo
import wmi



print(f"Architecture: {platform.architecture()}")
print(f"Network Name: {platform.node()}")
print(f"Operating system: {platform.platform()}")
print(f"Processor: {platform.processor()}")


cpu_info = cpuinfo.get_cpu_info()
print(f"Full Cpu name: {cpu_info['brand_raw']}")
#-----------------------Actual Clock Speed------------------------
print(f"Full Cpu name: {cpu_info['hz_actual_friendly']}")

#-----------------------Advertised Clock Speed--------------------
print(f"Full Cpu name: {cpu_info['hz_advertised_friendly']}")

#----------------RAM Info---------------------
print(f"Total RAM: {psutil.virtual_memory().total / 1024 / 1024 / 1024:.2f} GB")

pc = wmi.WMI()

os_info = pc.Win32_OperatingSystem()[0]
print(os_info)
print(pc.Win32_Processor()[0])
#--------------------GPU Info------------------------
print(pc.Win32_VideoController()[0])