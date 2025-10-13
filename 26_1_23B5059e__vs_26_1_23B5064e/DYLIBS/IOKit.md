## IOKit

> `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

```diff

-100222.40.3.0.0
-  __TEXT.__text: 0xa5040
+100222.40.4.0.0
+  __TEXT.__text: 0xa50c4
   __TEXT.__auth_stubs: 0x2120
   __TEXT.__objc_methlist: 0x150
   __TEXT.__const: 0x104cc
-  __TEXT.__oslogstring: 0x5280
+  __TEXT.__oslogstring: 0x52b0
   __TEXT.__cstring: 0xbbb0
   __TEXT.__unwind_info: 0x2170
   __TEXT.__objc_classname: 0x58

   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 7F5E5104-05F2-326D-AC11-29B662F86C3A
-  Functions: 3461
-  Symbols:   6651
-  CStrings:  3491
+  UUID: 8D65943A-6673-3BF3-9BF9-F281F0A6E6C2
+  Functions: 3462
+  Symbols:   6655
+  CStrings:  3492
 
Symbols:
+ _IOCreatePlugInInterfaceForService.cold.27
+ _IOCreatePlugInInterfaceForService.cold.28
Functions:
~ _IOCreatePlugInInterfaceForService : 2720 -> 2748
~ _IOCreatePlugInInterfaceForService.cold.11 : 68 -> 104
~ _IOCreatePlugInInterfaceForService.cold.13 : 104 -> 68
+ _IOCreatePlugInInterfaceForService.cold.23
CStrings:
+ "OSKEXT_BUILD_DATE 21:49:24 Oct  5 2025"
+ "io_service_t has invalid IOCFPlugInTypes for %@"
- "OSKEXT_BUILD_DATE 21:33:17 Sep 28 2025"

```
