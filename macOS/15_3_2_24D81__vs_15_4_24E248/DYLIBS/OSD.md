## OSD

> `/System/Library/PrivateFrameworks/OSD.framework/Versions/A/OSD`

```diff

 43.0.0.0.0
   __TEXT.__text: 0x6b8
   __TEXT.__auth_stubs: 0x100
-  __TEXT.__objc_methlist: 0x98
+  __TEXT.__objc_methlist: 0xe8
   __TEXT.__const: 0x8
   __TEXT.__gcc_except_tab: 0x2c
   __TEXT.__cstring: 0x5a
-  __TEXT.__unwind_info: 0xa0
+  __TEXT.__unwind_info: 0xa8
   __TEXT.__objc_classname: 0x21
   __TEXT.__objc_methname: 0x285
   __TEXT.__objc_methtype: 0xfd

   __AUTH_CONST.__auth_got: 0x90
   __AUTH_CONST.__const: 0x70
   __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__objc_const: 0x1e0
+  __AUTH_CONST.__objc_const: 0x148
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0x60
   __DATA.__bss: 0x10

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CA1D3CC0-DFC5-3837-879D-27F653047AA8
-  Functions: 16
-  Symbols:   82
+  UUID: E3BD3DB3-9FBC-38A8-97AA-083ED15D1507
+  Functions: 17
+  Symbols:   83
   CStrings:  41
 
Symbols:
+ +[OSDManager sharedManager].cold.1
Functions:
~ +[OSDManager sharedManager] : 84 -> 68
~ -[OSDManager remoteObjectProxy] : 504 -> 500

```
