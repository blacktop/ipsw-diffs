## mod_auth_form.so

> `/usr/libexec/apache2/mod_auth_form.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x5574
+880.0.0.0.0
+  __TEXT.__text: 0x4cbc
   __TEXT.__auth_stubs: 0x290
   __TEXT.__cstring: 0xf4d
-  __TEXT.__unwind_info: 0x70
+  __TEXT.__unwind_info: 0x80
   __DATA_CONST.__auth_got: 0x148
   __DATA_CONST.__const: 0x280
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: DF57AF3D-C86D-3E4A-A2D4-69C246B04744
+  UUID: E08741A4-75FA-3D78-83C2-C64E7488A05B
   Functions: 34
   Symbols:   82
   CStrings:  91
Functions:
~ _merge_auth_form_dir_config : 2148 -> 1904
~ _add_authn_provider : 404 -> 364
~ _set_cookie_form_username : 88 -> 84
~ _set_cookie_form_password : 88 -> 84
~ _set_cookie_form_location : 88 -> 84
~ _set_cookie_form_method : 88 -> 84
~ _set_cookie_form_mimetype : 88 -> 84
~ _set_cookie_form_body : 88 -> 84
~ _set_cookie_form_size : 188 -> 160
~ _set_login_required_location : 260 -> 240
~ _set_login_success_location : 260 -> 240
~ _set_logout_location : 260 -> 240
~ _set_site_passphrase : 64 -> 60
~ _set_authoritative : 64 -> 60
~ _set_fake_basic_auth : 64 -> 60
~ _set_disable_no_store : 64 -> 60
~ _check_string : 204 -> 172
~ _authenticate_form_post_config : 660 -> 564
~ _authenticate_form_authn : 2324 -> 2008
~ _authenticate_form_login_handler : 1056 -> 956
~ _authenticate_form_logout_handler : 456 -> 412
~ _authenticate_form_redirect_handler : 1372 -> 1240
~ _hook_note_cookie_auth_failure : 100 -> 92
~ _get_notes_auth : 1788 -> 1604
~ _get_session_auth : 1612 -> 1456
~ _check_site : 248 -> 212
~ _fake_basic_authentication : 296 -> 276
~ _check_authn : 1052 -> 956
~ _get_form_auth : 4772 -> 4264
~ _set_session_auth : 480 -> 460
~ _note_cookie_auth_failure : 152 -> 132
~ _set_notes_auth : 524 -> 472
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_auth_form.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_auth_form.c"

```
