## mod_file_cache.so

> `/usr/libexec/apache2/mod_file_cache.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xd98
+880.0.0.0.0
+  __TEXT.__text: 0xcc8
   __TEXT.__auth_stubs: 0x230
   __TEXT.__cstring: 0x251
-  __TEXT.__unwind_info: 0x60
+  __TEXT.__unwind_info: 0x70
   __DATA_CONST.__auth_got: 0x118
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x78

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 5373BB50-5EBE-363A-9E5E-65B9FD7558FB
+  UUID: 9F968255-E063-3883-9D11-7BF1039166EB
   Functions: 10
   Symbols:   48
   CStrings:  15
Functions:
~ _cache_the_file : 1488 -> 1424
~ _file_cache_handler : 624 -> 556
~ _file_cache_xlat : 308 -> 276
~ _mmap_handler : 404 -> 380
~ _sendfile_handler : 280 -> 260
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/cache/mod_file_cache.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/cache/mod_file_cache.c"

```
