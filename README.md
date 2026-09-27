# HARDWARE-LAB-2
#PS C:\WINDOWS\system32> python --version
Python 3.13.15
PS C:\WINDOWS\system32> Get-CimInstance Win32_Processor | Select-Object Name,NumberOfCores,NumberOfLogicalProcessors

Name                           NumberOfCores NumberOfLogicalProcessors
----                           ------------- -------------------------
Intel(R) Core(TM) Ultra 7 155U            12                        14


PS C:\WINDOWS\system32> Get-CimInstance Win32_ComputerSystem | Select-Object TotalPhysicalMemory

TotalPhysicalMemory
-------------------
        16668938240


PS C:\WINDOWS\system32> Get-PhysicalDisk | Select-Object FriendlyName,MediaType,Size

FriendlyName          MediaType          Size
------------          ---------          ----
UMIS RPETJ1T24MKP2QDQ SSD       1024209543168
