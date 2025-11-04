## libindus.dylib

> `/usr/lib/libindus.dylib`

```diff

-95.0.1.0.0
-  __TEXT.__text: 0x13e538
+95.0.2.0.0
+  __TEXT.__text: 0x13e610
   __TEXT.__auth_stubs: 0x860
   __TEXT.__const: 0x4c80
   __TEXT.__gcc_except_tab: 0x4bf8
-  __TEXT.__cstring: 0x26ccd
+  __TEXT.__cstring: 0x26d41
   __TEXT.__oslogstring: 0xb
   __TEXT.__unwind_info: 0x1c88
   __DATA_CONST.__got: 0xb0

   __AUTH_CONST.__cfstring: 0x20
   __AUTH.__data: 0x3f8
   __DATA.__data: 0x28698
-  __DATA.__common: 0x680b1
-  __DATA.__bss: 0x83d0
+  __DATA.__common: 0x680c1
+  __DATA.__bss: 0x83e0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 894A30F0-1742-3DC7-BC91-3AECA067B235
+  UUID: 444B6CE1-B9B9-3813-A630-26ACB8936589
   Functions: 1752
-  Symbols:   5264
-  CStrings:  4011
+  Symbols:   5266
+  CStrings:  4014
 
Symbols:
+ __ZL18g_ReportingFTAData.10
+ __ZL18g_ReportingFTAData.11
+ __ZL18g_ReportingFTAData.12
+ ___block_descriptor_tmp.73
- __ZL18g_ReportingFTAData.4
- __ZL18g_ReportingFTAData.5
Functions:
~ __Z27Hal_ProcessFTAAnalyticsDataPht : 1052 -> 1152
~ __Z26Hal_ReportFTAAnalyticsDatav : 604 -> 620
~ ____Z26Hal_ReportFTAAnalyticsDatav_block_invoke : 504 -> 604
CStrings:
+ "%10u %s%c %s: FTA-CA,METTickMs,%u,SleepTimeSec,%8.19lf,TimeErrUSec,%10.15lf, WorstVTErrUSec,%10.15lf\n"
+ "%10u %s%c %s: FTA-Evnt, METtick,%u, SleepTimeSec,%10.10lf, FTA-TimeErrUSec,%10.15lf, VirtualTimeErrUSec,%10.15lf\n"
+ "Oct 21 2025"
+ "TAoneway"
+ "VirtualTimeErrAtWorstFTAUSec"
+ "VirtualTimeWorstErrUSec"
- "%10u %s%c %s: FTA-CA,METTickMs,%u,SleepTimeSec,%8.19lf,TimeErrUSec,%10.15lf\n"
- "%10u %s%c %s: FTA-Evnt, METtick,%u, SleepTimeSec,%10.10lf, FTA-TimeErrUSec,%10.15lf\n"
- "Oct 10 2025"

```
