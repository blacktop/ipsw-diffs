## arkitd

> `/usr/libexec/arkitd`

```diff

-631.5.7.0.0
-  __TEXT.__text: 0xcdc
-  __TEXT.__auth_stubs: 0x320
+631.6.0.0.0
+  __TEXT.__text: 0xe3c
+  __TEXT.__auth_stubs: 0x330
   __TEXT.__objc_stubs: 0x2a0
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x10c
+  __TEXT.__gcc_except_tab: 0x110
   __TEXT.__cstring: 0xe5
-  __TEXT.__oslogstring: 0x115
+  __TEXT.__oslogstring: 0x1a5
   __TEXT.__objc_methname: 0x1aa
-  __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0x1a0
+  __TEXT.__unwind_info: 0xa8
+  __DATA_CONST.__auth_got: 0x1a8
   __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__const: 0x140
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x60

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_selrefs: 0xa8
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x40
+  __DATA.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore
   - /System/Library/PrivateFrameworks/ARKitDaemon.framework/ARKitDaemon
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 14
-  Symbols:   73
-  CStrings:  41
+  Functions: 15
+  Symbols:   74
+  CStrings:  44
 
Symbols:
+ _objc_retain_x20
+ _os_variant_has_internal_content
- _objc_retain_x25
CStrings:
+ "Error: Exiting unexpectedly"
+ "Error: Failed to setup sandbox library directory with error: %@"
+ "Error: Failed to setup sandbox temporary directory!"

```
