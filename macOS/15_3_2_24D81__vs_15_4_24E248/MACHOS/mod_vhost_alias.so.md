## mod_vhost_alias.so

> `/usr/libexec/apache2/mod_vhost_alias.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x1064
+880.0.0.0.0
+  __TEXT.__text: 0xf20
   __TEXT.__auth_stubs: 0x120
   __TEXT.__cstring: 0x217
-  __TEXT.__unwind_info: 0x54
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0x90
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 437BB772-2EA4-3036-8E38-27165D642280
+  UUID: 5454B37E-2F0D-38ED-8257-07B1B0A35B4D
   Functions: 7
   Symbols:   34
   CStrings:  20
Functions:
~ _mva_merge_server_config : 292 -> 268
~ _vhost_alias_set : 988 -> 900
~ _mva_translate : 612 -> 564
~ _vhost_alias_interpolate : 1912 -> 1760
~ _vhost_alias_checkspace : 216 -> 204
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/mappers/mod_vhost_alias.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/mappers/mod_vhost_alias.c"

```
