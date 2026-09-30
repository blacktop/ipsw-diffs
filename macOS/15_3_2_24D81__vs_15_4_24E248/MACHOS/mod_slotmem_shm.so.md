## mod_slotmem_shm.so

> `/usr/libexec/apache2/mod_slotmem_shm.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x3484
+880.0.0.0.0
+  __TEXT.__text: 0x3068
   __TEXT.__auth_stubs: 0x1f0
   __TEXT.__cstring: 0x396
-  __TEXT.__unwind_info: 0x98
+  __TEXT.__unwind_info: 0xa8
   __DATA_CONST.__auth_got: 0xf8
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__const: 0x68

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: AB4B8298-4F1A-3D8F-916D-D8B0EDDEF947
+  UUID: 8AC986AF-738F-3EB0-8149-AF71E89B6C51
   Functions: 22
   Symbols:   60
   CStrings:  30
Functions:
~ _ap_slotmem_shm_register_hook : 160 -> 156
~ _post_config : 100 -> 104
~ _slotmem_doall : 336 -> 296
~ _slotmem_create : 3708 -> 3436
~ _slotmem_attach : 2072 -> 1964
~ _slotmem_dptr : 196 -> 176
~ _slotmem_get : 316 -> 280
~ _slotmem_put : 316 -> 280
~ _slotmem_num_free_slots : 220 -> 192
~ _slotmem_grab : 812 -> 756
~ _slotmem_release : 788 -> 728
~ _slotmem_fgrab : 732 -> 680
~ _slotmem_filenames : 532 -> 456
~ _restore_slotmem : 1632 -> 1508
~ _cleanup_slotmem : 204 -> 172
~ _store_slotmem : 1008 -> 916
~ _slotmem_clearinuse : 188 -> 168
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/slotmem/mod_slotmem_shm.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/slotmem/mod_slotmem_shm.c"

```
