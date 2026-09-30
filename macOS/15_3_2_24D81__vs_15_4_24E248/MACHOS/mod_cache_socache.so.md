## mod_cache_socache.so

> `/usr/libexec/apache2/mod_cache_socache.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x84c8
+880.0.0.0.0
+  __TEXT.__text: 0x7b00
   __TEXT.__auth_stubs: 0x350
   __TEXT.__cstring: 0x10c7
-  __TEXT.__unwind_info: 0x80
+  __TEXT.__unwind_info: 0x90
   __DATA_CONST.__auth_got: 0x1a8
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__const: 0x168

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 58DE786B-A7A4-3631-B0F2-A4CC4FA76BCF
+  UUID: 23D57AB5-A283-3E95-B7EB-5CAB51829A37
   Functions: 37
   Symbols:   98
   CStrings:  86
Functions:
~ _create_dir_config : 152 -> 148
~ _merge_dir_config : 1000 -> 816
~ _create_config : 64 -> 60
~ _merge_config : 108 -> 92
~ _cache_socache_register_hook : 188 -> 192
~ _set_cache_socache : 356 -> 328
~ _set_cache_maxtime : 184 -> 164
~ _set_cache_mintime : 184 -> 164
~ _set_cache_max : 188 -> 168
~ _set_cache_readsize : 164 -> 144
~ _set_cache_readtime : 180 -> 160
~ _socache_precfg : 256 -> 224
~ _socache_post_config : 904 -> 844
~ _socache_child_init : 276 -> 240
~ _store_headers : 3436 -> 3224
~ _store_body : 4776 -> 4376
~ _recall_body : 292 -> 276
~ _create_entity : 5072 -> 4696
~ _open_entity : 8516 -> 8048
~ _remove_url : 676 -> 624
~ _commit_entity : 2304 -> 2168
~ _tokens_to_array : 156 -> 144
~ _store_array : 476 -> 440
~ _regen_key : 452 -> 440
~ _store_table : 672 -> 620
~ _read_array : 432 -> 404
~ _read_table : 932 -> 844
~ _sobj_body_pre_cleanup : 68 -> 64
~ _socache_status_register : 96 -> 92
~ _socache_status_hook : 768 -> 664
~ _ap_rputs : 212 -> 200
~ _remove_lock : 88 -> 80
~ _destroy_cache : 184 -> 160
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/cache/mod_cache_socache.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/cache/mod_cache_socache.c"

```
