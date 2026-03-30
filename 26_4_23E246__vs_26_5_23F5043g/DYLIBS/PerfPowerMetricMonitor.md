## PerfPowerMetricMonitor

> `/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/PerfPowerMetricMonitor`

```diff

-3031.102.1.0.0
-  __TEXT.__text: 0x1a7c8
+3031.120.21.0.0
+  __TEXT.__text: 0x1b3d0
   __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x14b4
+  __TEXT.__objc_methlist: 0x1544
   __TEXT.__const: 0xf8
   __TEXT.__gcc_except_tab: 0x984
-  __TEXT.__cstring: 0xf2c
+  __TEXT.__cstring: 0x10cb
   __TEXT.__oslogstring: 0x1bae
   __TEXT.__ustring: 0x6c0
-  __TEXT.__unwind_info: 0x760
+  __TEXT.__unwind_info: 0x790
   __TEXT.__objc_classname: 0x185
-  __TEXT.__objc_methname: 0x3c70
+  __TEXT.__objc_methname: 0x3f66
   __TEXT.__objc_methtype: 0x66e
-  __TEXT.__objc_stubs: 0x3140
+  __TEXT.__objc_stubs: 0x32c0
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x678
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe40
+  __DATA_CONST.__objc_selrefs: 0xea0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x40
-  __DATA_CONST.__objc_arraydata: 0x240
+  __DATA_CONST.__objc_arraydata: 0x270
   __AUTH_CONST.__auth_got: 0x2e8
   __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__cfstring: 0x1340
-  __AUTH_CONST.__objc_const: 0x2128
+  __AUTH_CONST.__cfstring: 0x1400
+  __AUTH_CONST.__objc_const: 0x2248
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_ivar: 0x204
+  __DATA.__objc_ivar: 0x21c
   __DATA.__data: 0x300
   __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0x2d0

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3D4FB726-716A-3D82-A832-0CB7B63152F9
-  Functions: 597
-  Symbols:   2103
-  CStrings:  1270
+  UUID: 57D86611-E8D6-3E65-9BAC-B8EA83455696
+  Functions: 609
+  Symbols:   2145
+  CStrings:  1306
 
Symbols:
+ -[PPSProcessMetricCollection cpuEnergyWithVouchers]
+ -[PPSProcessMetricCollection cpuEnergyWithoutVouchers]
+ -[PPSProcessMetricCollection cpuSecondsWithVouchers]
+ -[PPSProcessMetricCollection cpuSecondsWithoutVouchers]
+ -[PPSProcessMetricCollection gpuEnergyWithVouchers]
+ -[PPSProcessMetricCollection gpuEnergyWithoutVouchers]
+ -[PPSProcessMetricCollection setCpuEnergyWithVouchers:]
+ -[PPSProcessMetricCollection setCpuEnergyWithoutVouchers:]
+ -[PPSProcessMetricCollection setCpuSecondsWithVouchers:]
+ -[PPSProcessMetricCollection setCpuSecondsWithoutVouchers:]
+ -[PPSProcessMetricCollection setGpuEnergyWithVouchers:]
+ -[PPSProcessMetricCollection setGpuEnergyWithoutVouchers:]
+ _OBJC_IVAR_$_PPSProcessMetricCollection._cpuEnergyWithVouchers
+ _OBJC_IVAR_$_PPSProcessMetricCollection._cpuEnergyWithoutVouchers
+ _OBJC_IVAR_$_PPSProcessMetricCollection._cpuSecondsWithVouchers
+ _OBJC_IVAR_$_PPSProcessMetricCollection._cpuSecondsWithoutVouchers
+ _OBJC_IVAR_$_PPSProcessMetricCollection._gpuEnergyWithVouchers
+ _OBJC_IVAR_$_PPSProcessMetricCollection._gpuEnergyWithoutVouchers
+ _objc_msgSend$cpuEnergyWithVouchers
+ _objc_msgSend$cpuEnergyWithoutVouchers
+ _objc_msgSend$cpuSecondsWithVouchers
+ _objc_msgSend$cpuSecondsWithoutVouchers
+ _objc_msgSend$gpuEnergyWithVouchers
+ _objc_msgSend$gpuEnergyWithoutVouchers
+ _objc_msgSend$setCpuEnergyWithVouchers:
+ _objc_msgSend$setCpuEnergyWithoutVouchers:
+ _objc_msgSend$setCpuSecondsWithVouchers:
+ _objc_msgSend$setCpuSecondsWithoutVouchers:
+ _objc_msgSend$setGpuEnergyWithVouchers:
+ _objc_msgSend$setGpuEnergyWithoutVouchers:
CStrings:
+ "Energy Cost        %8.3f     %@\nEnergy Overhead    %8.3f     %@\nCPU Cost           %8.3f     %@\nCPU Seconds        %8.3f s   %@\nCPU Seconds (without vouchers) %8.3f s   %@\nCPU Seconds (vouchers) %8.3f s   %@\nCPU Energy         %8.3f nJ  %@\nCPU Energy (without vouchers)  %8.3f nJ  %@\nCPU Energy (vouchers)  %8.3f nJ  %@\nGPU Cost           %8.3f     %@\nGPU Energy         %8.3f nJ  %@\nGPU Energy (without vouchers)  %8.3f nJ  %@\nGPU Energy (vouchers)  %8.3f nJ  %@\nDisplay Power      %8.3f     %@\nNetwork Cost       %8d     %@\nWiFi In            %8d B   %@\nWiFi Out           %8d B   %@\nCell In            %8d B   %@\nCell Out           %8d B   %@\nLocation Cost      %8.3f     %@\nOngoing Location   %8s     %@\nLocation Desired Accuracy %8.3f %@\nQOS Utility %8.3f s   %@\nQOS Background %8.3f s   %@\nQOS User Initiated %8.3f s   %@\nQOS User Interactive %8.3f s   %@\nQOS Default %8.3f s   %@\nQOS Maintenance %8.3f s   %@\nQOS Unspecified %8.3f s   %@\nApplication State               %@\n%29s"
+ "T@\"PPSMetricSample\",&,N,V_cpuEnergyWithVouchers"
+ "T@\"PPSMetricSample\",&,N,V_cpuEnergyWithoutVouchers"
+ "T@\"PPSMetricSample\",&,N,V_cpuSecondsWithVouchers"
+ "T@\"PPSMetricSample\",&,N,V_cpuSecondsWithoutVouchers"
+ "T@\"PPSMetricSample\",&,N,V_gpuEnergyWithVouchers"
+ "T@\"PPSMetricSample\",&,N,V_gpuEnergyWithoutVouchers"
+ "_cpuEnergyWithVouchers"
+ "_cpuEnergyWithoutVouchers"
+ "_cpuSecondsWithVouchers"
+ "_cpuSecondsWithoutVouchers"
+ "_gpuEnergyWithVouchers"
+ "_gpuEnergyWithoutVouchers"
+ "cpuEnergyWithVouchers"
+ "cpuEnergyWithoutVouchers"
+ "cpuSecondsWithVouchers"
+ "cpuSecondsWithoutVouchers"
+ "gpuEnergyWithVouchers"
+ "gpuEnergyWithoutVouchers"
+ "setCpuEnergyWithVouchers:"
+ "setCpuEnergyWithoutVouchers:"
+ "setCpuSecondsWithVouchers:"
+ "setCpuSecondsWithoutVouchers:"
+ "setGpuEnergyWithVouchers:"
+ "setGpuEnergyWithoutVouchers:"
- "Energy Cost        %8.3f     %@\nEnergy Overhead    %8.3f     %@\nCPU Cost           %8.3f     %@\nCPU Seconds        %8.3f s   %@\nCPU Energy         %8.3f nJ  %@\nGPU Cost           %8.3f     %@\nDisplay Power      %8.3f     %@\nNetwork Cost       %8d     %@\nWiFi In            %8d B   %@\nWiFi Out           %8d B   %@\nCell In            %8d B   %@\nCell Out           %8d B   %@\nLocation Cost      %8.3f     %@\nOngoing Location   %8s     %@\nLocation Desired Accuracy %8.3f %@\nQOS Utility %8.3f s   %@\nQOS Background %8.3f s   %@\nQOS User Initiated %8.3f s   %@\nQOS User Interactive %8.3f s   %@\nQOS Default %8.3f s   %@\nQOS Maintenance %8.3f s   %@\nQOS Unspecified %8.3f s   %@\nApplication State               %@\n%29s"

```
