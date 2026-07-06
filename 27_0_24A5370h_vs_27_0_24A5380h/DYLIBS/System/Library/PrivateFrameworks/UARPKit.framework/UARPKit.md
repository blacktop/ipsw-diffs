## UARPKit

> `/System/Library/PrivateFrameworks/UARPKit.framework/UARPKit`

```diff

-  __TEXT.__text: 0x14184
+  __TEXT.__text: 0x14334
   __TEXT.__objc_methlist: 0x14d8
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0x1dea
   __TEXT.__gcc_except_tab: 0x3bc
-  __TEXT.__oslogstring: 0x742
-  __TEXT.__unwind_info: 0x418
+  __TEXT.__oslogstring: 0x8a3
+  __TEXT.__unwind_info: 0x420
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__got: 0xd8
   __AUTH_CONST.__cfstring: 0xb40
-  __AUTH_CONST.__objc_const: 0x1ea8
+  __AUTH_CONST.__objc_const: 0x1e88
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x190
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x18c
   __DATA.__data: 0x2a0
+  __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 512
-  Symbols:   1651
-  CStrings:  330
+  Functions: 516
+  Symbols:   1657
+  CStrings:  339
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__cstring : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Symbols:
+ -[UARPDevice handleDeviceUnresponsive]
+ GCC_except_table35
+ _objc_msgSend$handleDeviceUnresponsive
- -[UARPDevice deactivate]
- GCC_except_table36
- _OBJC_IVAR_$_UARPDevice._deactivated
- _objc_msgSend$deactivate
- _objc_msgSend$suspend
CStrings:
+ "%s: Not available %@"
+ "%s: device (and transport) are now unavailable %@"
+ "%s: device already unavailable %@"
+ "%s: device not available %@"
+ "%s: device not available ?? %@"
+ "%s: device not available, cannot plumb transport %@"
+ "%s: device not available, cannot plumb transporte %@"
+ "%s: transport already available %@"
+ "%s: transport already unavailable %@"
+ "%s: transport not available %@"
- "%s: DEACTIVATED %@"

```
