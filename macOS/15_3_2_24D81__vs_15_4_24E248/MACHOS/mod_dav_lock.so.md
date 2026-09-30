## mod_dav_lock.so

> `/usr/libexec/apache2/mod_dav_lock.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x27a0
+880.0.0.0.0
+  __TEXT.__text: 0x245c
   __TEXT.__auth_stubs: 0x1e0
   __TEXT.__cstring: 0x3ba
   __TEXT.__const: 0xd5
-  __TEXT.__unwind_info: 0x6c
+  __TEXT.__unwind_info: 0x78
   __DATA_CONST.__auth_got: 0xf0
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0xd0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 008326FB-729C-3D5E-AEDB-47F39AA3E3A9
+  UUID: EE9184A9-7353-35D1-970A-61D6D1FBB558
   Functions: 28
   Symbols:   62
   CStrings:  18
Functions:
~ _dav_lock_merge_dir_config : 160 -> 144
~ _dav_lock_cmd_davlockdb : 160 -> 148
~ _dav_generic_parse_locktoken : 240 -> 228
~ _dav_generic_format_locktoken : 148 -> 144
~ _dav_generic_open_lockdb : 308 -> 292
~ _dav_generic_close_lockdb : 92 -> 84
~ _dav_generic_create_lock : 156 -> 152
~ _dav_generic_get_locks : 812 -> 748
~ _dav_generic_find_lock : 864 -> 792
~ _dav_generic_has_locks : 220 -> 200
~ _dav_generic_append_locks : 812 -> 756
~ _dav_generic_remove_lock : 600 -> 504
~ _dav_generic_refresh_locks : 972 -> 872
~ _dav_generic_really_open_lockdb : 288 -> 256
~ _dav_generic_dbm_new_error : 280 -> 260
~ _dav_generic_build_key : 204 -> 196
~ _dav_generic_alloc_lock : 204 -> 196
~ _dav_generic_load_lock_record : 1396 -> 1288
~ _dav_generic_resolve : 328 -> 292
~ _dav_generic_lock_expired : 96 -> 88
~ _dav_generic_save_lock_record : 1364 -> 1248
~ _dav_generic_do_refresh : 160 -> 140
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/dav/lock/mod_dav_lock.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/dav/lock/mod_dav_lock.c"

```
