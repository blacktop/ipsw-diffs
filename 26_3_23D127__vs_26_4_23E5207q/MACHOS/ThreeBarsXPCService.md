## ThreeBarsXPCService

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/XPCServices/ThreeBarsXPCService.xpc/ThreeBarsXPCService`

```diff

-1035.6.0.0.0
-  __TEXT.__text: 0xbb0
-  __TEXT.__auth_stubs: 0x1b0
+1041.19.2.0.0
+  __TEXT.__text: 0x1460
+  __TEXT.__auth_stubs: 0x230
   __TEXT.__objc_stubs: 0x320
   __TEXT.__objc_methlist: 0x288
   __TEXT.__objc_classname: 0x80
   __TEXT.__objc_methname: 0x56c
   __TEXT.__objc_methtype: 0x232
-  __TEXT.__cstring: 0x495
-  __TEXT.__const: 0x8
-  __TEXT.__unwind_info: 0x98
-  __DATA_CONST.__auth_got: 0xe0
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0xc0
+  __TEXT.__cstring: 0x516
+  __TEXT.__const: 0x10
+  __TEXT.__gcc_except_tab: 0x74
+  __TEXT.__dlopen_cstrs: 0xa4
+  __TEXT.__unwind_info: 0xe8
+  __DATA_CONST.__auth_got: 0x128
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__const: 0x118
   __DATA_CONST.__cfstring: 0x1e0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28

   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x1e0
+  __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 75B76DF0-D16F-3E32-A957-E84EE98CB3ED
-  Functions: 21
-  Symbols:   56
-  CStrings:  152
+  UUID: AEE70BAB-10D3-3584-9E22-464A7812D156
+  Functions: 36
+  Symbols:   60
+  CStrings:  160
 
Symbols:
+ __Block_object_dispose
+ __Unwind_Resume
+ ___objc_personality_v0
+ __sl_dlopen
+ _abort_report_np
+ _free
+ _objc_autorelease
+ _objc_autoreleaseReturnValue
+ _objc_getClass
+ _objc_release_x27
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x22
+ _objc_retain_x24
+ _objc_retain_x25
- _OBJC_CLASS_$_TBTileFetchRequest
- _OBJC_CLASS_$_TBTileFetchRequestDescriptor
- _OBJC_CLASS_$_TBTileItemDescriptor
- _OBJC_CLASS_$_WiFi3BarsNetwork
- _OBJC_CLASS_$_WiFi3BarsSource
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
- _objc_retain_x21
- _objc_retain_x23
- _objc_retain_x3
CStrings:
+ "%s"
+ "TBTileFetchRequest"
+ "TBTileFetchRequestDescriptor"
+ "TBTileItemDescriptor"
+ "Unable to find class %s"
+ "WiFi3BarsNetwork"
+ "WiFi3BarsSource"
+ "softlink:r:path:/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy"

```
