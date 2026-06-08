## arkitd

> `/usr/libexec/arkitd`

```diff

-746.100.4.0.0
-  __TEXT.__text: 0xed0
-  __TEXT.__auth_stubs: 0x330
+779.0.0.0.5
+  __TEXT.__text: 0xdd0
+  __TEXT.__auth_stubs: 0x350
   __TEXT.__objc_stubs: 0x2a0
-  __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0xf4
+  __TEXT.__const: 0x6a
+  __TEXT.__gcc_except_tab: 0x78
   __TEXT.__cstring: 0x100
   __TEXT.__oslogstring: 0x1a5
   __TEXT.__objc_methname: 0x1aa
   __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0x1a8
-  __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0x140
   __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__got: 0x70
   __DATA.__objc_selrefs: 0xa8
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore
   - /System/Library/PrivateFrameworks/ARKitDaemon.framework/ARKitDaemon
+  - /System/Library/SubFrameworks/ARKitCore.framework/ARKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B31A418E-4665-321A-9A8C-94F47A08942A
-  Functions: 20
-  Symbols:   74
+  UUID: B9945E73-23C1-368B-BF2D-786C0B58BA96
+  Functions: 21
+  Symbols:   75
   CStrings:  50
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x25
+ _objc_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_autoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19

```
