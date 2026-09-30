## libBasebandManager.dylib

> `/usr/lib/libBasebandManager.dylib`

```diff

-1209.0.0.0.0
-  __TEXT.__text: 0x201230
+1211.0.0.0.0
+  __TEXT.__text: 0x201eac
   __TEXT.__auth_stubs: 0x3230
   __TEXT.__init_offsets: 0x134
   __TEXT.__objc_methlist: 0x270
-  __TEXT.__gcc_except_tab: 0x314a8
+  __TEXT.__gcc_except_tab: 0x316a4
   __TEXT.__const: 0xcc6b
-  __TEXT.__cstring: 0x6f40
-  __TEXT.__oslogstring: 0xad0c
-  __TEXT.__unwind_info: 0x94a8
+  __TEXT.__cstring: 0x6f66
+  __TEXT.__oslogstring: 0xae06
+  __TEXT.__unwind_info: 0x94f0
   __TEXT.__objc_classname: 0x109
   __TEXT.__objc_methname: 0x1187
   __TEXT.__objc_methtype: 0x1853
   __TEXT.__objc_stubs: 0xfa0
   __DATA_CONST.__got: 0x2078
-  __DATA_CONST.__const: 0x1df0
+  __DATA_CONST.__const: 0x1e18
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x40
-  __DATA.__data: 0x5f0
+  __DATA.__data: 0x5e8
   __DATA.__bss: 0x4c8
   __DATA.__common: 0x21
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x548
+  __DATA_DIRTY.__data: 0x550
   __DATA_DIRTY.__bss: 0x21a
   __DATA_DIRTY.__common: 0xc8
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 5792
-  Symbols:   8279
-  CStrings:  2455
+  Functions: 5797
+  Symbols:   8285
+  CStrings:  2461
 
Symbols:
+ __ZN13HealthEventDB21updateCommCenterStatsEN3xpc4dictE
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
