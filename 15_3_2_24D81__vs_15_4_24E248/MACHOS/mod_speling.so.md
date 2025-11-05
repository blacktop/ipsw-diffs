## mod_speling.so

> `/usr/libexec/apache2/mod_speling.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x1778
+880.0.0.0.0
+  __TEXT.__text: 0x1574
   __TEXT.__auth_stubs: 0x1e0
   __TEXT.__cstring: 0x440
-  __TEXT.__unwind_info: 0x5c
+  __TEXT.__unwind_info: 0x68
   __DATA_CONST.__auth_got: 0xf0
   __DATA_CONST.__const: 0xa0
   __DATA.__data: 0xa8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 9EBE34EB-FC4C-372D-BB77-78B4B01C0A72
+  UUID: FFFCE870-0532-30C8-B082-D0817B21351D
   Functions: 7
   Symbols:   41
   CStrings:  37
Functions:
~ _mkconfig : 92 -> 88
~ _check_speling : 5128 -> 4708
~ _spdist : 592 -> 500
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/mappers/mod_speling.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/mappers/mod_speling.c"

```
