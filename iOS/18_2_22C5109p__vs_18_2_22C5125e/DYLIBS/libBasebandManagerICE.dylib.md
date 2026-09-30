## libBasebandManagerICE.dylib

> `/usr/lib/libBasebandManagerICE.dylib`

```diff

-1209.0.0.0.0
-  __TEXT.__text: 0x1f9280
+1211.0.0.0.0
+  __TEXT.__text: 0x1f9eec
   __TEXT.__auth_stubs: 0x3240
   __TEXT.__init_offsets: 0x138
   __TEXT.__objc_methlist: 0x270
   __TEXT.__const: 0xcbd7
-  __TEXT.__gcc_except_tab: 0x30e14
-  __TEXT.__oslogstring: 0xab79
-  __TEXT.__cstring: 0x6ccf
-  __TEXT.__unwind_info: 0x93d8
+  __TEXT.__gcc_except_tab: 0x31010
+  __TEXT.__oslogstring: 0xac73
+  __TEXT.__cstring: 0x6cf5
+  __TEXT.__unwind_info: 0x9420
   __TEXT.__objc_classname: 0x109
   __TEXT.__objc_methname: 0x1187
   __TEXT.__objc_methtype: 0x1853
   __TEXT.__objc_stubs: 0xfa0
   __DATA_CONST.__got: 0x2098
-  __DATA_CONST.__const: 0x1aa8
+  __DATA_CONST.__const: 0x1ad0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x40
-  __DATA.__data: 0x658
+  __DATA.__data: 0x600
   __DATA.__common: 0x29
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x4a8
+  __DATA_DIRTY.__data: 0x500
   __DATA_DIRTY.__common: 0xb8
-  __DATA_DIRTY.__bss: 0x230
+  __DATA_DIRTY.__bss: 0x22a
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 5735
-  Symbols:   8212
-  CStrings:  2399
+  Functions: 5740
+  Symbols:   8218
+  CStrings:  2405
 
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
