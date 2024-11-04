## libBasebandManagerDAL.dylib

> `/usr/lib/libBasebandManagerDAL.dylib`

```diff

-1209.0.0.0.0
-  __TEXT.__text: 0x118fb4
+1211.0.0.0.0
+  __TEXT.__text: 0x119c6c
   __TEXT.__auth_stubs: 0x2340
   __TEXT.__init_offsets: 0xb4
   __TEXT.__objc_methlist: 0x140
   __TEXT.__const: 0x64d7
-  __TEXT.__gcc_except_tab: 0x1a2b4
-  __TEXT.__oslogstring: 0x5200
-  __TEXT.__cstring: 0x2f56
-  __TEXT.__unwind_info: 0x5208
+  __TEXT.__gcc_except_tab: 0x1a4b4
+  __TEXT.__oslogstring: 0x52fa
+  __TEXT.__cstring: 0x2f7c
+  __TEXT.__unwind_info: 0x5258
   __TEXT.__objc_classname: 0x68
   __TEXT.__objc_methname: 0x626
   __TEXT.__objc_methtype: 0x1389
   __TEXT.__objc_stubs: 0x500
-  __DATA_CONST.__got: 0x1148
-  __DATA_CONST.__const: 0xf10
+  __DATA_CONST.__got: 0x1150
+  __DATA_CONST.__const: 0xf38
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH_CONST.__objc_const: 0x658
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x1c
-  __DATA.__data: 0x7c0
-  __DATA.__common: 0x40
+  __DATA.__data: 0x740
+  __DATA.__common: 0x28
   __DATA.__bss: 0x1d8
+  __DATA_DIRTY.__data: 0x80
+  __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3061
-  Symbols:   4448
-  CStrings:  1164
+  Functions: 3067
+  Symbols:   4456
+  CStrings:  1170
 
Symbols:
+ __ZN13HealthEventDB21updateCommCenterStatsEN3xpc4dictE
+ __ZN3abm28kKeyStatsBootFirstBootUpTimeE
+ __ZN3abm33kKeyCommCenterStatsLastLaunchTimeE
+ __ZN3abm34kKeyCommCenterStatsFirstLaunchTimeE
+ __ZN3sys20isBootSessionChangedEv
+ __ZN3sys21updateBootSessionUUIDEv
- __ZN3abm29kKeyCommCenterStatsLastUpTimeE
CStrings:
+ "#I AP reboot detected; resetting CommCenter and baseband stats"
+ "#I Resetting baseband boot stats"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1211"
+ "AppleBasebandServices_Manager-1211"
+ "Baseband boot stats not found"
+ "Failed to create xpc dictionary to reset Baseband stats"
+ "Failed to create xpc dictionary to reset CommCenter stats"
+ "Failed to update session id"
+ "KeyCommCenterStatsFirstLaunchTime"
+ "KeyCommCenterStatsLastLaunchTime"
- "AppleBasebandManager-AppleBasebandServices_Manager-1209"
- "AppleBasebandServices_Manager-1209"
- "BB stats is empty"
- "KeyCommCenterStatsLastUpTime"

```
