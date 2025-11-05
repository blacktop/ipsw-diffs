## UserEventAgent

> `/usr/libexec/UserEventAgent`

```diff

-340.0.0.0.0
-  __TEXT.__text: 0x252c
+342.100.1.0.0
+  __TEXT.__text: 0x2520
   __TEXT.__auth_stubs: 0x660
   __TEXT.__objc_stubs: 0xe0
-  __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x233
-  __TEXT.__oslogstring: 0x681
+  __TEXT.__const: 0xb0
+  __TEXT.__cstring: 0x22f
+  __TEXT.__oslogstring: 0x67f
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x5d
   __TEXT.__unwind_info: 0xd8
   __DATA_CONST.__auth_got: 0x338
-  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x100
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 32C8BF23-2570-3156-B63F-60B95C5F5C21
-  Functions: 49
+  UUID: C494C51F-0280-3BA8-AB0D-65835B0615A1
+  Functions: 51
   Symbols:   130
-  CStrings:  71
+  CStrings:  69
 
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
