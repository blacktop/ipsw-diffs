## mod_lbmethod_bybusyness.so

> `/usr/libexec/apache2/mod_lbmethod_bybusyness.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x3d0
+880.0.0.0.0
+  __TEXT.__text: 0x390
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
-  UUID: 962DA206-BE03-3BF0-9DF9-E62775B569F0
+  UUID: AD3ED387-DB4F-305C-B077-F252F709CC69
   Functions: 6
   Symbols:   14
   CStrings:  6
Functions:
~ _register_hook : 108 -> 116
~ _lbmethod_bybusyness_post_config : 268 -> 236
~ _find_best_bybusyness : 144 -> 128
~ _reset : 152 -> 148
~ _is_best_bybusyness : 280 -> 260
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/balancers/mod_lbmethod_bybusyness.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/balancers/mod_lbmethod_bybusyness.c"

```
