## mod_auth_digest.so

> `/usr/libexec/apache2/mod_auth_digest.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x6ea8
+880.0.0.0.0
+  __TEXT.__text: 0x6520
   __TEXT.__auth_stubs: 0x4b0
   __TEXT.__cstring: 0x1030
-  __TEXT.__unwind_info: 0x70
+  __TEXT.__unwind_info: 0x80
   __DATA_CONST.__auth_got: 0x258
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x1b0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: FFB8081B-DC06-330A-A053-6F6D9CB97F53
+  UUID: 94930937-B04B-3B10-BF47-CB87975028D5
   Functions: 38
   Symbols:   131
   CStrings:  124
Functions:
~ _create_digest_dir_config : 224 -> 208
~ _set_realm : 152 -> 148
~ _add_authn_provider : 404 -> 364
~ _set_qop : 300 -> 272
~ _set_nonce_lifetime : 232 -> 220
~ _set_algorithm : 196 -> 180
~ _set_uri_list : 260 -> 248
~ _set_shmem_size : 1012 -> 928
~ _pre_init : 844 -> 780
~ _initialize_module : 128 -> 116
~ _initialize_child : 328 -> 296
~ _parse_hdr_and_update_nc : 328 -> 304
~ _authenticate_digest_user : 5216 -> 4800
~ _add_auth_info : 1720 -> 1512
~ _hook_note_digest_auth_failure : 280 -> 256
~ _initialize_tables : 1184 -> 1096
~ _log_error_and_cleanup : 188 -> 168
~ _rmm_malloc : 108 -> 96
~ _cleanup_tables : 684 -> 620
~ _get_digest_rec : 2240 -> 1948
~ _get_client : 2204 -> 2008
~ _note_digest_auth_failure : 1224 -> 1076
~ _copy_uri_components : 588 -> 508
~ _get_hash : 560 -> 496
~ _check_nc : 936 -> 860
~ _check_nonce : 2876 -> 2692
~ _gen_client : 384 -> 344
~ _ltox : 112 -> 104
~ _gen_nonce : 224 -> 204
~ _add_client : 1432 -> 1360
~ _gc : 536 -> 468
~ _rmm_free : 68 -> 64
~ _gen_nonce_hash : 268 -> 256
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_auth_digest.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_auth_digest.c"

```
