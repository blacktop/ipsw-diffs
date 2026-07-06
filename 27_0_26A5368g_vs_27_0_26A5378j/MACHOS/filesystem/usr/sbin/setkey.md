## setkey

> `/usr/sbin/setkey`

```diff

-  __TEXT.__text: 0x8a04
+  __TEXT.__text: 0x8a30
   __TEXT.__auth_stubs: 0x480
-  __TEXT.__cstring: 0xfc6
+  __TEXT.__cstring: 0xfe4
   __TEXT.__const: 0x3136
   __TEXT.__unwind_info: 0x1c8
   __DATA_CONST.__const: 0x460

   __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__data: 0x14
-  __DATA.__bss: 0x998
+  __DATA.__bss: 0x9a0
   __DATA.__common: 0x898
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libipsec.A.dylib
-  Functions: 134
+  Functions: 135
   Symbols:   83
-  CStrings:  240
+  CStrings:  241
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
CStrings:
+ "bad length in yy_scan_bytes()"

```
