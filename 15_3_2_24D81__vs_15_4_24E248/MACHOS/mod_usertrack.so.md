## mod_usertrack.so

> `/usr/libexec/apache2/mod_usertrack.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x11d0
+880.0.0.0.0
+  __TEXT.__text: 0xffc
   __TEXT.__auth_stubs: 0x1c0
   __TEXT.__cstring: 0x51c
-  __TEXT.__unwind_info: 0x48
+  __TEXT.__unwind_info: 0x58
   __DATA_CONST.__auth_got: 0xe0
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__const: 0x168

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 900CAFC8-B9BE-344E-9392-63CD471B7710
+  UUID: CC07BB84-7166-3AE6-87F9-E88779A80315
   Functions: 11
   Symbols:   45
   CStrings:  67
Functions:
~ _make_cookie_log_state : 68 -> 64
~ _set_and_comp_regexp : 508 -> 452
~ _set_cookie_exp : 904 -> 792
~ _set_cookie_domain : 204 -> 184
~ _set_cookie_style : 336 -> 296
~ _set_cookie_name : 228 -> 212
~ _set_samesite_value : 244 -> 220
~ _spot_cookie : 676 -> 584
~ _make_cookie : 1200 -> 1096
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/metadata/mod_usertrack.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/metadata/mod_usertrack.c"

```
