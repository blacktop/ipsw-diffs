## mod_session_dbd.so

> `/usr/libexec/apache2/mod_session_dbd.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x1e20
+880.0.0.0.0
+  __TEXT.__text: 0x1b6c
   __TEXT.__auth_stubs: 0x1d0
   __TEXT.__cstring: 0x756
   __TEXT.__unwind_info: 0x68

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 8784EF2A-52B3-3547-98EB-E1422FB08101
+  UUID: 533A80A4-BE9F-31D2-B576-071BAD90CC90
   Functions: 16
   Symbols:   50
   CStrings:  42
Functions:
~ _create_session_dbd_dir_config : 160 -> 156
~ _merge_session_dbd_dir_config : 1080 -> 956
~ _set_dbd_peruser : 64 -> 60
~ _set_dbd_cookie_remove : 64 -> 60
~ _set_cookie_name : 212 -> 192
~ _set_cookie_name2 : 212 -> 192
~ _check_string : 132 -> 120
~ _session_dbd_load : 1036 -> 868
~ _session_dbd_save : 1048 -> 920
~ _dbd_load : 1020 -> 960
~ _dbd_init : 664 -> 616
~ _dbd_save : 1296 -> 1228
~ _dbd_remove : 496 -> 464
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/session/mod_session_dbd.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/session/mod_session_dbd.c"

```
