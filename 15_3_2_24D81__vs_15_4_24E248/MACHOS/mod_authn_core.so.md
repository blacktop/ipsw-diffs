## mod_authn_core.so

> `/usr/libexec/apache2/mod_authn_core.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xe90
+880.0.0.0.0
+  __TEXT.__text: 0xd28
   __TEXT.__auth_stubs: 0x180
   __TEXT.__cstring: 0x3b0
-  __TEXT.__unwind_info: 0x54
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0xc0
   __DATA_CONST.__const: 0xc0
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: EBEF9FA8-D6C7-3E74-8BA2-2ECE4DED3BA5
+  UUID: 45CBEF70-EC07-3927-807D-C1FCB9D4A4BF
   Functions: 13
   Symbols:   41
   CStrings:  25
Functions:
~ _create_authn_core_dir_config : 72 -> 68
~ _merge_authn_core_dir_config : 256 -> 228
~ _register_hooks : 176 -> 168
~ _set_authtype : 284 -> 260
~ _set_authname : 272 -> 248
~ _authaliassection : 1088 -> 976
~ _authn_alias_check_password : 288 -> 252
~ _authn_alias_get_realm_hash : 296 -> 260
~ _authn_ap_auth_type : 352 -> 316
~ _authn_ap_auth_name : 308 -> 280
~ _authenticate_no_user : 228 -> 204
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authn_core.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authn_core.c"

```
