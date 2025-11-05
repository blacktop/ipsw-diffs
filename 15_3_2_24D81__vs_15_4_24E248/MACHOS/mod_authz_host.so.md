## mod_authz_host.so

> `/usr/libexec/apache2/mod_authz_host.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x12c0
+880.0.0.0.0
+  __TEXT.__text: 0x1120
   __TEXT.__auth_stubs: 0x180
   __TEXT.__cstring: 0x35e
-  __TEXT.__unwind_info: 0x60
+  __TEXT.__unwind_info: 0x70
   __DATA_CONST.__auth_got: 0xc0
   __DATA_CONST.__const: 0x40
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 2CD4EA16-075D-3772-8196-1966783EE3A9
+  UUID: 871590F0-5813-33DE-A738-577FFF15EDE3
   Functions: 10
   Symbols:   42
   CStrings:  24
Functions:
~ _ip_check_authorization : 156 -> 136
~ _ip_parse_config : 820 -> 720
~ _host_check_authorization : 908 -> 848
~ _host_parse_config : 252 -> 232
~ _in_domain : 292 -> 260
~ _forward_dns_check_authorization : 1672 -> 1512
~ _local_check_authorization : 176 -> 152
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authz_host.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authz_host.c"

```
