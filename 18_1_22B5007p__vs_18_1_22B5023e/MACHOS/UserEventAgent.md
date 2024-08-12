## UserEventAgent

> `/usr/libexec/UserEventAgent`

```diff

-335.0.0.0.0
-  __TEXT.__text: 0x23d8
-  __TEXT.__auth_stubs: 0x620
+336.0.0.0.0
+  __TEXT.__text: 0x23a0
+  __TEXT.__auth_stubs: 0x650
   __TEXT.__objc_stubs: 0xe0
   __TEXT.__const: 0xa8
+  __TEXT.__gcc_except_tab: 0x48
   __TEXT.__cstring: 0x1e9
   __TEXT.__oslogstring: 0x681
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x5d
-  __TEXT.__unwind_info: 0xd8
-  __DATA_CONST.__auth_got: 0x318
+  __TEXT.__unwind_info: 0xe0
+  __DATA_CONST.__auth_got: 0x338
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x100
   __DATA_CONST.__cfstring: 0x20

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 49
-  Symbols:   124
+  Functions: 45
+  Symbols:   128
   CStrings:  67
 
Symbols:
+ _CFLocaleCopyCurrent
+ __Unwind_Resume
+ ___objc_personality_v0
+ ___snprintf_chk
+ _objc_release_x22
+ _objc_release_x23
+ _objc_terminate
- _objc_release_x24
- _objc_release_x28
- _snprintf

```
