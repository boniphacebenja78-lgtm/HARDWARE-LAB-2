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


LENOVO 21L10007UE
813
Single-Core Score
2480
Multi-Core Score
Geekbench 7.0.0 for Windows AVX2Valid
Result Information
Upload Date	September 27 2026 04:02 PM
Views	1
System Information
System Information
Operating System	Microsoft Windows 11 Pro
Model	LENOVO 21L10007UE
Motherboard	LENOVO 21L10007UE
Power Plan	Balanced
CPU Information
Name	Intel Core Ultra 7 155U
Topology	1 Processor, 12 Cores, 14 Threads
Identifier	GenuineIntel Family 6 Model 170 Stepping 4
Base Frequency	1.70 GHz
Cluster 1	2 Cores
Cluster 2	10 Cores
Maximum Frequency	4788 MHz
Package	Socket 2049 FCBGA
Codename	Meteor Lake
L1 Instruction Cache	64.0 KB x 7
L1 Data Cache	48.0 KB x 7
L2 Cache	2.00 MB x 1
L3 Cache	12.0 MB x 1
Instruction Sets	sse2 sse3 pclmul fma3 sse41 aesni avx f16c avx2 shani vaes avx-vnni
Memory Information
Size	16.00 GB
Transfer Rate	3192 MT/s
Type	DDR5 SDRAM
Channels	2
Single-Core Performance
Single-Core Score	813	
File Compression
1054
150.0 MB/sec	
 
Navigation
853
4.70 routes/sec	
 
HTML5 Browser
718
8.97 pages/sec	
 
PDF Viewer
802
36.0 Mpixels/sec	
 
Photo Library
783
2.68 images/sec	
 
Clang
781
4.23 Klines/sec	
 
Text Processing
986
58.2 pages/sec	
 
Asset Compression
1019
22.6 MB/sec	
 
HDR
734
44.3 Mpixels/sec	
 
Photo Editor
926
17.0 images/sec	
 
Ray Tracer
626
176.0 Ksamples/sec	
 
Structure from Motion
947
17.1 Kpixels/sec	
 
Game Physics
638
25.8 FPS	
 
Video Encoder
579
21.1 FPS	
 
Audio Encoder
1122
1.56 Msamples/sec	
 
Video Player
688
72.8 FPS	
 
Multi-Core Performance
Multi-Core Score	2480	
File Compression
2418
344.1 MB/sec	
 
Photo Library
2521
8.64 images/sec	
 
Clang
2597
14.0 Klines/sec	
 
Text Processing
2821
166.4 pages/sec	
 
Asset Compression
3760
83.5 MB/sec	
 
HDR
2190
132.3 Mpixels/sec	
 
Photo Editor
1252
23.0 images/sec	
 
Ray Tracer
3109
873.2 Ksamples/sec	
 
