## mod_lbmethod_bytraffic.so

> `/usr/libexec/apache2/mod_lbmethod_bytraffic.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x338
+880.0.0.0.0
+  __TEXT.__text: 0x304
   __TEXT.__auth_stubs: 0x50
   __TEXT.__cstring: 0x120
-  __TEXT.__unwind_info: 0x60
+  __TEXT.__unwind_info: 0x70
   __DATA_CONST.__auth_got: 0x28
   __DATA_CONST.__const: 0x30
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: A7FF32B6-0EAF-3EE2-927D-DFCF45A46228
+  UUID: BC355B35-AD68-35B4-BC1B-197F9EC09777
   Functions: 6
   Symbols:   14
   CStrings:  6
Functions:
~ _register_hook : 108 -> 116
~ _lbmethod_bytraffic_post_config : 268 -> 236
~ _find_best_bytraffic : 84 -> 80
~ _reset : 152 -> 148
~ _is_best_bytraffic : 188 -> 168
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/balancers/mod_lbmethod_bytraffic.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/balancers/mod_lbmethod_bytraffic.c"

```
