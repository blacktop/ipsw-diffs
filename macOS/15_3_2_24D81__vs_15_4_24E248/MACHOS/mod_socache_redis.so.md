## mod_socache_redis.so

> `/usr/libexec/apache2/mod_socache_redis.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x2c4
+880.0.0.0.0
+  __TEXT.__text: 0x290
   __TEXT.__auth_stubs: 0x30
   __TEXT.__cstring: 0x166
-  __TEXT.__unwind_info: 0x54
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0x18
   __DATA_CONST.__const: 0x78
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 9424D433-6D7C-382E-AB40-753B34904B49
+  UUID: B09EBFD7-57F8-3895-B135-803FE35D77E4
   Functions: 4
   Symbols:   9
   CStrings:  8
Functions:
~ _create_server_config : 92 -> 88
~ _socache_rd_set_ttl : 300 -> 276
~ _socache_rd_set_rwto : 300 -> 276
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/cache/mod_socache_redis.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/cache/mod_socache_redis.c"

```
