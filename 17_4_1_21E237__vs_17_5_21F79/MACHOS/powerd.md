## powerd

> `/System/Library/CoreServices/powerd.bundle/powerd`

```diff

-1630.100.21.0.0
-  __TEXT.__text: 0x5f694
+1630.120.8.0.0
+  __TEXT.__text: 0x609a0
   __TEXT.__auth_stubs: 0x1a80
   __TEXT.__objc_stubs: 0x42a0
   __TEXT.__objc_methlist: 0x1b28
   __TEXT.__const: 0x2b0
-  __TEXT.__cstring: 0x5be0
-  __TEXT.__objc_methname: 0x4894
-  __TEXT.__oslogstring: 0xa0a1
+  __TEXT.__cstring: 0x5c6d
+  __TEXT.__objc_methname: 0x48a0
+  __TEXT.__oslogstring: 0xa3c2
   __TEXT.__objc_classname: 0x2c8
   __TEXT.__objc_methtype: 0x768
   __TEXT.__gcc_except_tab: 0x3bc
   __TEXT.__dlopen_cstrs: 0x256
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x1070
+  __TEXT.__unwind_info: 0x108c
   __DATA_CONST.__auth_got: 0xd50
   __DATA_CONST.__got: 0x210
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x2320
-  __DATA_CONST.__cfstring: 0x6360
+  __DATA_CONST.__const: 0x2340
+  __DATA_CONST.__cfstring: 0x6460
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_data: 0x550
   __DATA.__data: 0x9bc
   __DATA.__common: 0x1120
-  __DATA.__bss: 0xa98
+  __DATA.__bss: 0xae8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3E043852-E92F-3CB0-B35F-E915A5C002D0
-  Functions: 2097
+  UUID: 89D7520F-F47F-35C8-9C6B-06B462D1274B
+  Functions: 2119
   Symbols:   541
-  CStrings:  3888
+  CStrings:  3924
 
CStrings:
+ "Changing NCCP from %d -> %d (freeze), cycle count change(%d->%d). NCC:%d DesignCap:%d\n"
+ "Changing NCCP from %d -> %d (reset), cycle count change(%d->%d). NCC:%d DesignCap:%d\n"
+ "Device class: %@"
+ "Failed to find device class"
+ "Failed to read qmax"
+ "K/Q:%d/%d [ENTER]"
+ "K/Q:%d/%d [EXIT]"
+ "K/Q:%d/%d [EXIT] timeNow: (%llu) timeStored: (%llu) timediff: (%llu)"
+ "K/Q:%d/%d [UPDATE]"
+ "K/Q:%d/%d [UPDATE] kioskQmax: %d kioskQmaxTime: %llu"
+ "K/Q:%d/%d [UPDATE] timeNow: (%llu) timeStored: (%llu) timediff: (%llu)"
+ "No previous Qmax state found, storing first Good Qmax update"
+ "Watch"
+ "[ENTER] kiosk mode: %d flags: 0x%x K/Q:%d/%d qmax:%d currentTime:%llu"
+ "[EXIT] kiosk mode: %d flags: 0x%x K/Q:%d/%d"
+ "batteryCapacityMonitor"
+ "batteryHealthServiceBCDC support: %d"
+ "couldn't find battery data"
+ "couldn't find lifetime data"
+ "iPhone"
+ "kiosk mode dict missing"
+ "kiosk mode value missing"
+ "lastBadQmax"
+ "lastBadQmaxTimeStamp"
+ "lastGoodQmax"
+ "lastGoodQmaxTimeStamp"
+ "lastKioskQmax"
+ "lastKioskQmaxTimeStamp"
+ "setYearForWeekOfYear:"
- "setYear:"

```
