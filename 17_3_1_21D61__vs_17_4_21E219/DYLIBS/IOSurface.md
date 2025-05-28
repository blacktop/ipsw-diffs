## IOSurface

> `/System/Library/Frameworks/IOSurface.framework/IOSurface`

```diff

-352.10.2.0.0
-  __TEXT.__text: 0x108a4
-  __TEXT.__auth_stubs: 0xcc0
+352.41.7.0.0
+  __TEXT.__text: 0x106b8
+  __TEXT.__auth_stubs: 0xcd0
   __TEXT.__objc_methlist: 0x780
-  __TEXT.__cstring: 0x2706
-  __TEXT.__const: 0x1b
-  __TEXT.__oslogstring: 0x2f8
+  __TEXT.__cstring: 0x2718
+  __TEXT.__const: 0x50
+  __TEXT.__oslogstring: 0x3d9
   __TEXT.__gcc_except_tab: 0x6c
-  __TEXT.__unwind_info: 0x41c
+  __TEXT.__unwind_info: 0x424
   __TEXT.__objc_classname: 0x13e
   __TEXT.__objc_methname: 0x1077
   __TEXT.__objc_methtype: 0x54d
   __TEXT.__objc_stubs: 0xb60
   __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x978
+  __DATA_CONST.__const: 0x9a0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xb50
+  __DATA_CONST.__objc_const: 0xab0
   __DATA_CONST.__objc_selrefs: 0x530
-  __AUTH_CONST.__cfstring: 0x1d60
+  __DATA_CONST.__objc_classrefs: 0x90
+  __DATA_CONST.__objc_superrefs: 0x50
+  __AUTH_CONST.__cfstring: 0x1d80
   __AUTH_CONST.__objc_const: 0x3f0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x198
-  __AUTH_CONST.__auth_got: 0x670
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_classrefs: 0x90
-  __DATA.__objc_superrefs: 0x50
+  __AUTH_CONST.__auth_got: 0x678
+  __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x74
-  __DATA.__data: 0x208
+  __DATA.__data: 0x218
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x138
-  __DATA_DIRTY.__objc_data: 0x190
-  __DATA_DIRTY.__data: 0x180
+  __DATA_DIRTY.__objc_data: 0x1e0
+  __DATA_DIRTY.__data: 0x170
   __DATA_DIRTY.__bss: 0x8c
-  __DATA_DIRTY.__common: 0x18
+  __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 561
-  Symbols:   1622
-  CStrings:  685
+  Functions: 564
+  Symbols:   1623
+  CStrings:  689
 
Symbols:
+ _IOServiceGetMatchingServices
+ _IOSurfaceClientDisallowForever
+ _IOSurfaceClientDisallowForever.cold.1
+ _IOSurfaceDisallowForever
+ ____ioSurfaceConnectInternal_block_invoke
+ ____ioSurfaceConnectInternal_block_invoke.cold.1
+ ____ioSurfaceConnectInternal_block_invoke.cold.2
+ ____ioSurfaceConnectInternal_block_invoke.cold.3
+ ____ioSurfaceConnectInternal_block_invoke.cold.4
+ ___block_descriptor_33_e5_v8?0l
+ __ioSurfaceConnectInternal
+ __ioSurfaceConnectInternal.once
+ __iosServiceReturn
+ __os_log_impl
+ _kIOSurfaceHostOnly
- _IOServiceGetMatchingService
- __ioSurfaceClientRelease
- __ioSurfaceConnect.once
- __iosConnectInitalize
- __iosConnectInitalize.cold.1
- __iosConnectInitalize.cold.2
- __iosConnectInitalize.cold.3
- __iosConnectInitalize.cold.4
CStrings:
+ "@40@0:8r^{?=QIIIIIIIIQQCCCCIQQQQQQQ}16r^{?=QQQQIII}24@32"
+ "IOSurface.framework API explicitly disallowed."
+ "IOSurface.framework not allowed to iterate kernel services (%08x).  API disallowed."
+ "IOSurfaceDisallowForever() invoked too late, connection to IOSurface.kext already established"
+ "IOSurfaceHostOnly"
+ "{?=\"clientAddress\"Q\"surfaceID\"I\"pixelFormat\"I\"retainCount\"I\"yCbCrMatrix\"I\"cacheMode\"I\"mapCacheAttribute\"I\"purgeableState\"I\"purgeableStateAPI\"I\"allocOffset\"Q\"allocSize\"Q\"isGlobal\"C\"isAllocated\"C\"isWired\"C\"pad\"C\"parentSurfaceID\"I\"detachModeCode\"Q\"initDetachModeCodeTime\"Q\"protectionOptions\"Q\"residentSize\"Q\"dirtySize\"Q\"traceID\"Q\"memDescID\"Q}"
+ "{?=\"offset\"Q\"width\"Q\"height\"Q\"bytesPerRow\"Q\"bytesPerElement\"I\"elementWidth\"I\"elementHeight\"I}"
- "@40@0:8r^{?=QIIIIIIIIIICCCCIQQQIIQQ}16r^{?=IIIIIII}24@32"
- "{?=\"clientAddress\"Q\"surfaceID\"I\"pixelFormat\"I\"retainCount\"I\"yCbCrMatrix\"I\"cacheMode\"I\"mapCacheAttribute\"I\"purgeableState\"I\"purgeableStateAPI\"I\"allocOffset\"I\"allocSize\"I\"isGlobal\"C\"isAllocated\"C\"isWired\"C\"pad\"C\"parentSurfaceID\"I\"detachModeCode\"Q\"initDetachModeCodeTime\"Q\"protectionOptions\"Q\"residentSize\"I\"dirtySize\"I\"traceID\"Q\"memDescID\"Q}"
- "{?=\"offset\"I\"width\"I\"height\"I\"bytesPerRow\"I\"bytesPerElement\"I\"elementWidth\"I\"elementHeight\"I}"

```
