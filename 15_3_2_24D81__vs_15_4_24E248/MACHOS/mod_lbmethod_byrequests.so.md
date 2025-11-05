## mod_lbmethod_byrequests.so

> `/usr/libexec/apache2/mod_lbmethod_byrequests.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x354
+880.0.0.0.0
+  __TEXT.__text: 0x31c
   __TEXT.__auth_stubs: 0x50
   __TEXT.__cstring: 0x123
-  __TEXT.__unwind_info: 0x60
+  __TEXT.__unwind_info: 0x70
   __DATA_CONST.__auth_got: 0x28
   __DATA_CONST.__const: 0x30
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 775E7A05-39EB-393A-9E12-5DA47615B793
+  UUID: 1F0B720B-8B01-3E91-BDD0-729040338827
   Functions: 6
   Symbols:   14
   CStrings:  6
Functions:
~ _register_hook : 108 -> 116
~ _lbmethod_byrequests_post_config : 268 -> 236
~ _find_best_byrequests : 144 -> 128
~ _reset : 136 -> 132
~ _is_best_byrequests : 172 -> 160
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/balancers/mod_lbmethod_byrequests.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/balancers/mod_lbmethod_byrequests.c"

```
