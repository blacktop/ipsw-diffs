## mod_session_cookie.so

> `/usr/libexec/apache2/mod_session_cookie.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xa88
+880.0.0.0.0
+  __TEXT.__text: 0x968
   __TEXT.__auth_stubs: 0x120
   __TEXT.__cstring: 0x20d
-  __TEXT.__unwind_info: 0x54
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0x90
   __DATA_CONST.__const: 0xa0
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 40451DAE-A924-359E-A14D-2836ED876722
+  UUID: CD444422-6CDD-32C3-A7B4-55A68C8A900F
   Functions: 9
   Symbols:   29
   CStrings:  12
Functions:
~ _create_session_cookie_dir_config : 84 -> 80
~ _merge_session_cookie_dir_config : 668 -> 592
~ _set_cookie_name : 212 -> 192
~ _set_cookie_name2 : 212 -> 192
~ _set_remove : 64 -> 60
~ _check_string : 204 -> 172
~ _session_cookie_load : 592 -> 528
~ _session_cookie_save : 548 -> 480
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/session/mod_session_cookie.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/session/mod_session_cookie.c"

```
