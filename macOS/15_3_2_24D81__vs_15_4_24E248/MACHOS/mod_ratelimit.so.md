## mod_ratelimit.so

> `/usr/libexec/apache2/mod_ratelimit.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x1ff4
+880.0.0.0.0
+  __TEXT.__text: 0x1dfc
   __TEXT.__auth_stubs: 0x100
   __TEXT.__cstring: 0x1d6
-  __TEXT.__unwind_info: 0x5c
+  __TEXT.__unwind_info: 0x68
   __DATA_CONST.__auth_got: 0x80
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__const: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 03E05363-5531-3B30-9A29-AD38DEBC1C0F
+  UUID: 99C21F1D-0F91-3684-B44B-7E8A66D0E7EA
   Functions: 5
   Symbols:   31
   CStrings:  12
Functions:
~ _rate_limit_filter : 7728 -> 7224
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_ratelimit.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_ratelimit.c"

```
