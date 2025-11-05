## mod_socache_dbm.so

> `/usr/libexec/apache2/mod_socache_dbm.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x1ea4
+880.0.0.0.0
+  __TEXT.__text: 0x1c64
   __TEXT.__auth_stubs: 0x1e0
   __TEXT.__cstring: 0x544
-  __TEXT.__unwind_info: 0x48
+  __TEXT.__unwind_info: 0x58
   __DATA_CONST.__auth_got: 0xf0
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 6C3BDF34-5DED-311A-BC24-1224FF775AD0
+  UUID: B56FCAA8-F9D7-368D-B499-85A69022BE92
   Functions: 12
   Symbols:   45
   CStrings:  33
Functions:
~ _socache_dbm_create : 272 -> 248
~ _socache_dbm_init : 936 -> 836
~ _socache_dbm_store : 1128 -> 1084
~ _socache_dbm_retrieve : 680 -> 624
~ _socache_dbm_remove : 344 -> 316
~ _socache_dbm_status : 736 -> 668
~ _socache_dbm_iterate : 1284 -> 1200
~ _try_chown : 356 -> 320
~ _socache_dbm_expire : 1536 -> 1412
~ _ap_rputs : 212 -> 200
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/cache/mod_socache_dbm.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/cache/mod_socache_dbm.c"

```
