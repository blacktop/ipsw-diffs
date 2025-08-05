## IOKit

> `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

```diff

-100222.0.1.0.0
-  __TEXT.__text: 0xa4fc4
+100222.0.4.0.0
+  __TEXT.__text: 0xa4fb0
   __TEXT.__auth_stubs: 0x2120
   __TEXT.__objc_methlist: 0x150
   __TEXT.__const: 0x104cc
-  __TEXT.__oslogstring: 0x52bd
-  __TEXT.__cstring: 0xbb21
-  __TEXT.__unwind_info: 0x2158
+  __TEXT.__oslogstring: 0x5280
+  __TEXT.__cstring: 0xbbb0
+  __TEXT.__unwind_info: 0x2168
   __TEXT.__objc_classname: 0x58
   __TEXT.__objc_methname: 0xa3
   __TEXT.__objc_methtype: 0x19bc

   __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x590
-  __DATA.__bss: 0x4a8
+  __DATA.__bss: 0x4b0
   __DATA.__common: 0x100
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0xe8
-  __DATA_DIRTY.__bss: 0x260
+  __DATA_DIRTY.__bss: 0x258
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 65E313E6-01A0-381C-80D2-7F15E71723F7
-  Functions: 3460
-  Symbols:   6653
-  CStrings:  3489
+  UUID: 16861014-5B07-34CA-BB08-28A0E69D150D
+  Functions: 3461
+  Symbols:   6647
+  CStrings:  3491
 
Symbols:
+ __MergedGlobals.68
+ ___IOHIDUserDeviceSetupAsyncSupport.cold.3
+ ___IOHIDUserDeviceSetupAsyncSupport.cold.4
+ ___IOHIDUserDeviceSetupAsyncSupport.cold.5
- _IOHIDUserDeviceScheduleWithRunLoop.cold.1
- _IOHIDUserDeviceSetDispatchQueue.cold.1
- _IOHIDUserDeviceSetDispatchQueue.cold.2
- __MergedGlobals.65
CStrings:
+ "OSKEXT_BUILD_DATE 18:09:24 Jul 25 2025"
+ "assertion failure: CFMachPortCreateWithPort"
+ "assertion failure: IOConnectMapMemory:0x%x"
+ "assertion failure: IODataQueueAllocateNotificationPort"
+ "assertion failure: IONotificationPortCreate"
- "0x%llx: IOConnectMapMemory:0x%x"
- "OSKEXT_BUILD_DATE 20:04:56 Jul 11 2025"
- "assertion failure: \"__IOHIDUserDeviceSetupAsyncSupport(device)\" -> %llu"

```
