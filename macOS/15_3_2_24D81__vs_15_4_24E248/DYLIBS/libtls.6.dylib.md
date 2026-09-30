## libtls.6.dylib

> `/usr/lib/libtls.6.dylib`

```diff

-106.0.0.0.0
-  __TEXT.__text: 0x2070
+107.0.0.0.0
+  __TEXT.__text: 0x2050
   __TEXT.__auth_stubs: 0x590
-  __TEXT.__cstring: 0x518
+  __TEXT.__cstring: 0x516
   __TEXT.__const: 0x10
-  __TEXT.__unwind_info: 0xf8
+  __TEXT.__unwind_info: 0xf0
   __DATA_CONST.__got: 0x10
   __AUTH_CONST.__auth_got: 0x2c8
   __DATA.__bss: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.35.dylib
   - /usr/lib/libssl.35.dylib
-  UUID: EEE57B52-4BFC-3E15-9DAE-9BB062A7FDCB
-  Functions: 53
+  UUID: 628BDDB2-9C32-304D-8DDD-C73DC9C9C6CD
+  Functions: 52
   Symbols:   145
-  CStrings:  65
+  CStrings:  64
 
Functions:
~ _tls_ssl_error : 256 -> 264
- sub_260b089ec
~ _tls_connect_servername : 424 -> 412
CStrings:
- " "

```
