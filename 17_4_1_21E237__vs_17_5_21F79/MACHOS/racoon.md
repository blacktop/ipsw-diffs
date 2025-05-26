## racoon

> `/usr/sbin/racoon`

```diff

-337.0.0.0.0
-  __TEXT.__text: 0x71464
+1125.0.0.0.0
+  __TEXT.__text: 0x714f4
   __TEXT.__auth_stubs: 0x1060
-  __TEXT.__oslogstring: 0xc434
+  __TEXT.__oslogstring: 0xc46a
   __TEXT.__cstring: 0x56ef
   __TEXT.__const: 0x706e
-  __TEXT.__unwind_info: 0xf48
+  __TEXT.__unwind_info: 0xf4c
   __DATA_CONST.__auth_got: 0x830
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libipsec.A.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libresolv.9.dylib
-  Functions: 2766
+  Functions: 2768
   Symbols:   302
-  CStrings:  2212
+  CStrings:  2213
 
CStrings:
+ "remote public key length (%zu) != prime length (%zu)\n"

```
