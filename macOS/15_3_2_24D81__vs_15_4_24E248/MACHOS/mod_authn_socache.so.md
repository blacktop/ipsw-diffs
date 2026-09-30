## mod_authn_socache.so

> `/usr/libexec/apache2/mod_authn_socache.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x2a0c
+880.0.0.0.0
+  __TEXT.__text: 0x2714
   __TEXT.__auth_stubs: 0x240
   __TEXT.__cstring: 0x640
-  __TEXT.__unwind_info: 0x5c
+  __TEXT.__unwind_info: 0x68
   __DATA_CONST.__auth_got: 0x120
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x100

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: C4FFF0D2-AEFE-3F1D-A23C-8E7BC7E2FE04
+  UUID: 9404AED5-55B4-343B-8211-F8A6FC7D2EB7
   Functions: 16
   Symbols:   63
   CStrings:  39
Functions:
~ _authn_cache_dircfg_create : 100 -> 96
~ _authn_cache_dircfg_merge : 240 -> 212
~ _register_hooks : 244 -> 240
~ _authn_cache_socache : 424 -> 388
~ _authn_cache_enable : 72 -> 68
~ _authn_cache_setprovider : 152 -> 140
~ _authn_cache_timeout : 108 -> 88
~ _ap_authn_cache_store : 2616 -> 2452
~ _authn_cache_precfg : 292 -> 260
~ _authn_cache_post_config : 884 -> 844
~ _authn_cache_child_init : 276 -> 240
~ _check_password : 2364 -> 2192
~ _get_realm_hash : 2336 -> 2172
~ _construct_key : 464 -> 436
~ _remove_lock : 88 -> 80
~ _destroy_cache : 104 -> 96
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authn_socache.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authn_socache.c"

```
