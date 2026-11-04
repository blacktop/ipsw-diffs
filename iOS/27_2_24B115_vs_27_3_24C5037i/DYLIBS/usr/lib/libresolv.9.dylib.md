## libresolv.9.dylib

> `/usr/lib/libresolv.9.dylib`

```diff

-99.0.0.0.0
-  __TEXT.__text: 0x188d8
+101.0.0.0.0
+  __TEXT.__text: 0x188f0
   __TEXT.__const: 0x3fa
-  __TEXT.__cstring: 0x21c7
-  __TEXT.__unwind_info: 0x420
+  __TEXT.__cstring: 0x21fd
+  __TEXT.__unwind_info: 0x428
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xac8
   __DATA_CONST.__got: 0x0

   __DATA_DIRTY.__data: 0xa0
   __DATA_DIRTY.__bss: 0x10
   - /usr/lib/libSystem.B.dylib
-  Functions: 244
+  Functions: 245
   Symbols:   423
-  CStrings:  602
+  CStrings:  605
 
Functions:
~ _res_build : 1632 -> 1612
CStrings:
+ "consumed < sizeof(res->defdname)"
+ "res_build"
+ "res_init.c"
```
