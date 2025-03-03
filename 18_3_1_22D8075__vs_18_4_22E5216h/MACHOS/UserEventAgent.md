## UserEventAgent

> `/usr/libexec/UserEventAgent`

```diff

-340.0.0.0.0
-  __TEXT.__text: 0x23d8
+342.100.1.0.0
+  __TEXT.__text: 0x23cc
   __TEXT.__auth_stubs: 0x620
   __TEXT.__objc_stubs: 0xe0
-  __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x1e9
-  __TEXT.__oslogstring: 0x681
+  __TEXT.__const: 0xb0
+  __TEXT.__cstring: 0x1e5
+  __TEXT.__oslogstring: 0x67f
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x5d
   __TEXT.__unwind_info: 0xd8
   __DATA_CONST.__auth_got: 0x318
-  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x100
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 49
+  Functions: 51
   Symbols:   124
-  CStrings:  67
+  CStrings:  65
 
Symbols:
+ _objc_release_x21
+ _objc_release_x26
- _objc_release_x24
- _objc_release_x28
CStrings:
+ "assertion failure: \"descriptor == ((void*)0)\" -> %llu"
+ "assertion failure: \"sys->callback\" -> %llu"
+ "assertion failure: \"sys->name\" -> %llu"
+ "assertion failure: \"sys->publisher != ((void*)0)\" -> %llu"
+ "assertion failure: \"sys->queue\" -> %llu"
- "assertion failure: \"descriptor == ((void *)0)\" -> %lld"
- "assertion failure: \"sys->callback\" -> %lld"
- "assertion failure: \"sys->name\" -> %lld"
- "assertion failure: \"sys->publisher != ((void *)0)\" -> %lld"
- "assertion failure: \"sys->queue\" -> %lld"
- "d"
- "r"

```
