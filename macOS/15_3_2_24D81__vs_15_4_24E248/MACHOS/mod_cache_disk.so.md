## mod_cache_disk.so

> `/usr/libexec/apache2/mod_cache_disk.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x8a98
+880.0.0.0.0
+  __TEXT.__text: 0x800c
   __TEXT.__auth_stubs: 0x340
   __TEXT.__cstring: 0xcfa
-  __TEXT.__unwind_info: 0x74
+  __TEXT.__unwind_info: 0x80
   __DATA_CONST.__auth_got: 0x1a0
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: F3AB794E-BAA2-3106-87B3-1B09F3C0B4C7
+  UUID: E3D1EAE0-DC1F-31C5-9C41-5F97A8DE6E35
   Functions: 38
   Symbols:   99
   CStrings:  76
Functions:
~ _create_dir_config : 128 -> 124
~ _merge_dir_config : 824 -> 672
~ _create_config : 108 -> 104
~ _set_cache_root : 120 -> 104
~ _set_cache_dirlevels : 200 -> 184
~ _set_cache_dirlength : 200 -> 184
~ _set_cache_minfs : 160 -> 140
~ _set_cache_maxfs : 164 -> 144
~ _set_cache_readsize : 164 -> 144
~ _set_cache_readtime : 180 -> 160
~ _remove_entity : 100 -> 96
~ _store_headers : 252 -> 220
~ _store_body : 6152 -> 5632
~ _recall_headers : 3080 -> 2856
~ _recall_body : 124 -> 112
~ _create_entity : 3428 -> 3196
~ _open_entity : 4896 -> 4592
~ _remove_url : 5036 -> 4620
~ _commit_entity : 2204 -> 1980
~ _invalidate_entity : 136 -> 128
~ _close_disk_cache_fd : 128 -> 112
~ _read_table : 660 -> 588
~ _data_file : 280 -> 264
~ _header_file : 280 -> 264
~ _file_cache_temp_cleanup : 120 -> 108
~ _read_array : 564 -> 512
~ _regen_key : 448 -> 436
~ _file_cache_recall_mydata : 404 -> 380
~ _write_headers : 2832 -> 2744
~ _file_cache_el_final : 312 -> 276
~ _mkdir_structure : 236 -> 216
~ _tokens_to_array : 156 -> 144
~ _store_array : 348 -> 332
~ _store_table : 512 -> 488
~ _safe_file_rename : 260 -> 240
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/cache/mod_cache_disk.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/cache/mod_cache_disk.c"

```
