## mod_socache_memcache.so

> `/usr/libexec/apache2/mod_socache_memcache.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x15d0
+880.0.0.0.0
+  __TEXT.__text: 0x1478
   __TEXT.__auth_stubs: 0x180
   __TEXT.__cstring: 0x6fb
-  __TEXT.__unwind_info: 0x68
+  __TEXT.__unwind_info: 0x78
   __DATA_CONST.__auth_got: 0xc0
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0xa0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: A42E1232-09F2-3864-BA51-4FD15445E11C
+  UUID: 62234347-7451-39B1-AC60-1AC118D2676D
   Functions: 13
   Symbols:   41
   CStrings:  40
Functions:
~ _create_server_config : 80 -> 76
~ _socache_mc_set_ttl : 300 -> 276
~ _socache_mc_create : 168 -> 152
~ _socache_mc_init : 1368 -> 1296
~ _socache_mc_store : 496 -> 448
~ _socache_mc_retrieve : 608 -> 564
~ _socache_mc_remove : 684 -> 632
~ _socache_mc_status : 1368 -> 1300
~ _socache_mc_id2key : 168 -> 164
~ _ap_rputs : 212 -> 200
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/cache/mod_socache_memcache.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/cache/mod_socache_memcache.c"

```
