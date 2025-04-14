## KnowledgeMonitor

> `/System/Library/PrivateFrameworks/KnowledgeMonitor.framework/KnowledgeMonitor`

```diff

-458.5.0.1.0
-  __TEXT.__text: 0x2cec4
-  __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0x2f6c
-  __TEXT.__const: 0x228
+458.7.0.0.0
+  __TEXT.__text: 0x2d538
+  __TEXT.__auth_stubs: 0xc00
+  __TEXT.__objc_methlist: 0x2fac
+  __TEXT.__const: 0x230
   __TEXT.__gcc_except_tab: 0x810
-  __TEXT.__cstring: 0x2c62
-  __TEXT.__oslogstring: 0x26ca
+  __TEXT.__cstring: 0x2c8e
+  __TEXT.__oslogstring: 0x2859
   __TEXT.__dlopen_cstrs: 0x49
-  __TEXT.__unwind_info: 0xc00
+  __TEXT.__unwind_info: 0xc18
   __TEXT.__objc_classname: 0x5dc
-  __TEXT.__objc_methname: 0x865e
+  __TEXT.__objc_methname: 0x86e6
   __TEXT.__objc_methtype: 0xcba
-  __TEXT.__objc_stubs: 0x6b20
+  __TEXT.__objc_stubs: 0x6bc0
   __DATA_CONST.__got: 0x600
   __DATA_CONST.__const: 0x900
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22c0
+  __DATA_CONST.__objc_selrefs: 0x22e8
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__auth_got: 0x600
+  __AUTH_CONST.__auth_got: 0x610
   __AUTH_CONST.__const: 0x3e0
   __AUTH_CONST.__cfstring: 0x1f40
   __AUTH_CONST.__objc_const: 0x4aa0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1173
-  Symbols:   1659
-  CStrings:  2204
+  Functions: 1183
+  Symbols:   1671
+  CStrings:  2220
 
Symbols:
+ ___error
+ _sysctlbyname
CStrings:
+ "%@: Shutdown date is in the future"
+ "%@: bootDate: %@"
+ "%@: shutdownDate is: %@"
+ "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBacklightMonitor.m:175"
+ "Elapsed PMU RTC ticks in USecs since shutdown: %{public}@"
+ "SpringBoard shutdown date: %{public}@"
+ "Unable to get kern.monotonicclock_usecs: %{errno}d"
+ "Unable to get kern.shutdowntime: %{errno}d"
+ "Using shutdown date from SpringBoard: %{public}@"
+ "Using shutdown date from kern.shutdowntime: %{public}@"
+ "_shutdownDateFromSpringBoard"
+ "_shutdownDateFromSysctl"
+ "donateRetroactiveShutdownBacklightOffEvent"
+ "handleShutdownNotification"
+ "kern.monotonicclock_usecs"
+ "kern.monotonicclock_usecs[0] must be non-zero"
+ "kern.shutdowntime"
+ "kern.shutdowntime must be non-zero"
+ "shutdownDate"
- "%@: SBLastKnownShutdownDate is: %@"
- "%@: bootTime: %@"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBacklightMonitor.m:262"

```
