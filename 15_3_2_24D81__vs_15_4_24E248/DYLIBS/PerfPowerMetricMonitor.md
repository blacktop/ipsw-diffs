## PerfPowerMetricMonitor

> `/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/Versions/A/PerfPowerMetricMonitor`

```diff

-2308.80.23.0.0
-  __TEXT.__text: 0xf644
+2423.100.232.0.0
+  __TEXT.__text: 0xfcfc
   __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0xc74
+  __TEXT.__objc_methlist: 0xf0c
   __TEXT.__const: 0xb8
   __TEXT.__gcc_except_tab: 0x6ac
-  __TEXT.__cstring: 0xe21
+  __TEXT.__cstring: 0xe63
   __TEXT.__oslogstring: 0x92f
-  __TEXT.__ustring: 0x5c6
-  __TEXT.__unwind_info: 0x3c8
-  __TEXT.__objc_classname: 0x126
-  __TEXT.__objc_methname: 0x27d0
+  __TEXT.__ustring: 0x6c0
+  __TEXT.__unwind_info: 0x3d8
+  __TEXT.__objc_classname: 0x127
+  __TEXT.__objc_methname: 0x2900
   __TEXT.__objc_methtype: 0x596
-  __TEXT.__objc_stubs: 0x1f00
+  __TEXT.__objc_stubs: 0x2000
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0x118
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x918
+  __DATA_CONST.__objc_selrefs: 0x9f0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0x190
+  __DATA_CONST.__objc_arraydata: 0x1b0
   __AUTH_CONST.__auth_got: 0x1d0
   __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0xb80
-  __AUTH_CONST.__objc_const: 0x1b90
+  __AUTH_CONST.__cfstring: 0xbe0
+  __AUTH_CONST.__objc_const: 0x18b0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x158
+  __DATA.__objc_ivar: 0x16c
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/AssertionServices.framework/Versions/A/AssertionServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8364BE3A-45C5-3F58-81E3-8B75A06763DF
-  Functions: 400
-  Symbols:   1009
-  CStrings:  847
+  UUID: 3D879CB5-7F9A-3179-AA1D-2A8EA026CF38
+  Functions: 413
+  Symbols:   1034
+  CStrings:  869
 
Symbols:
+ +[PPSMetricCollection _metricSamplePropertyKeys].cold.1
+ +[PPSMetricCollection allPropertyKeys].cold.1
+ +[PPSMetricMonitorService sharedInstance].cold.1
+ +[PPSProcessMetricCollection _metricSamplePropertyKeys].cold.1
+ -[PPSMetricCollection brightness]
+ -[PPSMetricCollection displayAZL]
+ -[PPSMetricCollection edrHeadroom]
+ -[PPSMetricCollection scanoutFPS]
+ -[PPSMetricCollection setBrightness:]
+ -[PPSMetricCollection setDisplayAZL:]
+ -[PPSMetricCollection setEdrHeadroom:]
+ -[PPSMetricCollection setScanoutFPS:]
+ -[PPSProcessMetricCollection cpuEnergy]
+ -[PPSProcessMetricCollection setCpuEnergy:]
+ GCC_except_table71
+ GCC_except_table77
+ OBJC_IVAR_$_PPSMetricCollection._brightness
+ OBJC_IVAR_$_PPSMetricCollection._displayAZL
+ OBJC_IVAR_$_PPSMetricCollection._edrHeadroom
+ OBJC_IVAR_$_PPSMetricCollection._scanoutFPS
+ OBJC_IVAR_$_PPSProcessMetricCollection._cpuEnergy
+ PPSMetricMonitorLogHandleForCategory.cold.1
+ PPSTimeStringFromDate.cold.1
+ _objc_msgSend$brightness
+ _objc_msgSend$displayAZL
+ _objc_msgSend$edrHeadroom
+ _objc_msgSend$scanoutFPS
+ _objc_msgSend$setBrightness:
+ _objc_msgSend$setDisplayAZL:
+ _objc_msgSend$setEdrHeadroom:
+ _objc_msgSend$setScanoutFPS:
- GCC_except_table70
- GCC_except_table75
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
CStrings:
+ "Energy Cost        %8.3f     %@\nEnergy Overhead    %8.3f     %@\nCPU Cost           %8.3f     %@\nCPU Seconds        %8.3f s   %@\nCPU Energy         %8.3f nJ  %@\nGPU Cost           %8.3f     %@\nNetwork Cost       %8d     %@\nWiFi In            %8d B   %@\nWiFi Out           %8d B   %@\nCell In            %8d B   %@\nCell Out           %8d B   %@\nLocation Cost      %8.3f     %@\nOngoing Location   %8s     %@\nApplication State               %@\n%29s"
+ "T@\"PPSMetricSample\",&,N,V_brightness"
+ "T@\"PPSMetricSample\",&,N,V_displayAZL"
+ "T@\"PPSMetricSample\",&,N,V_edrHeadroom"
+ "T@\"PPSMetricSample\",&,N,V_scanoutFPS"
+ "_brightness"
+ "_displayAZL"
+ "_edrHeadroom"
+ "_scanoutFPS"
+ "brightness"
+ "displayAZL"
+ "edrHeadroom"
+ "scanoutFPS"
+ "setBrightness:"
+ "setDisplayAZL:"
+ "setEdrHeadroom:"
+ "setScanoutFPS:"
- "Energy Cost        %8.3f     %@\nEnergy Overhead    %8.3f     %@\nCPU Cost           %8.3f     %@\nCPU Seconds        %8.3f s   %@\nGPU Cost           %8.3f     %@\nNetwork Cost       %8d     %@\nWiFi In            %8d B   %@\nWiFi Out           %8d B   %@\nCell In            %8d B   %@\nCell Out           %8d B   %@\nLocation Cost      %8.3f     %@\nOngoing Location   %8s     %@\nApplication State               %@\n%29s"

```
