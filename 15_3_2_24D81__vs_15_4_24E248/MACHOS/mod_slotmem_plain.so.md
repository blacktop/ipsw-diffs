## mod_slotmem_plain.so

> `/usr/libexec/apache2/mod_slotmem_plain.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xbbc
+880.0.0.0.0
+  __TEXT.__text: 0xa90
   __TEXT.__auth_stubs: 0x90
   __TEXT.__cstring: 0xc0
-  __TEXT.__unwind_info: 0x78
+  __TEXT.__unwind_info: 0x88
   __DATA_CONST.__auth_got: 0x48
   __DATA_CONST.__const: 0x68
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 25A95C21-DA8D-3296-A83B-44A53C8DE6DC
+  UUID: 43B98CAE-7638-3B86-BFE3-0A90AEAD5F98
   Functions: 14
   Symbols:   27
   CStrings:  6
Functions:
~ _ap_slotmem_plain_register_hook : 108 -> 116
~ _slotmem_do : 348 -> 300
~ _slotmem_create : 632 -> 572
~ _slotmem_attach : 300 -> 268
~ _slotmem_dptr : 188 -> 168
~ _slotmem_get : 308 -> 272
~ _slotmem_put : 308 -> 272
~ _slotmem_num_free_slots : 156 -> 136
~ _slotmem_grab : 244 -> 220
~ _slotmem_release : 184 -> 164
~ _slotmem_fgrab : 140 -> 128
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/slotmem/mod_slotmem_plain.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/slotmem/mod_slotmem_plain.c"

```
