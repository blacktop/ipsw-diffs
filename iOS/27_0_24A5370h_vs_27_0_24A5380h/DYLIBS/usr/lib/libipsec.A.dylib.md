## libipsec.A.dylib

> `/usr/lib/libipsec.A.dylib`

```diff

-  __TEXT.__text: 0x28f0
-  __TEXT.__cstring: 0x5c3
+  __TEXT.__text: 0x2924
+  __TEXT.__cstring: 0x5e1
   __TEXT.__const: 0xb0a
   __TEXT.__unwind_info: 0xe8
   __TEXT.__auth_stubs: 0x0

   __DATA.__common: 0x48
   __DATA.__bss: 0x90
   - /usr/lib/libSystem.B.dylib
-  Functions: 57
-  Symbols:   163
-  CStrings:  74
+  Functions: 58
+  Symbols:   165
+  CStrings:  75
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ ___libipseclex : 2620 -> 2648
~ ___libipsec_create_buffer : 132 -> 128
~ ___libipsec_scan_buffer : 152 -> 144
~ ___libipsec_scan_bytes : 128 -> 140
CStrings:
+ "bad length in yy_scan_bytes()"

```
