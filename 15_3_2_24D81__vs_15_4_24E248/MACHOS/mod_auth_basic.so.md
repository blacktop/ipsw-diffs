## mod_auth_basic.so

> `/usr/libexec/apache2/mod_auth_basic.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x2024
+880.0.0.0.0
+  __TEXT.__text: 0x1d68
   __TEXT.__auth_stubs: 0x180
   __TEXT.__cstring: 0x6a8
-  __TEXT.__unwind_info: 0x60
+  __TEXT.__unwind_info: 0x70
   __DATA_CONST.__auth_got: 0xc0
   __DATA_CONST.__const: 0xc8
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 337145DF-0170-32EE-843B-30F28D3CA20B
+  UUID: EFC22965-1C50-30C2-A459-C8B97A1893A8
   Functions: 12
   Symbols:   38
   CStrings:  42
Functions:
~ _merge_auth_basic_dir_config : 784 -> 652
~ _add_authn_provider : 404 -> 364
~ _set_authoritative : 72 -> 68
~ _add_basic_fake : 556 -> 512
~ _set_use_digest_algorithm : 208 -> 188
~ _authenticate_basic_user : 1728 -> 1576
~ _authenticate_basic_fake : 3420 -> 3180
~ _hook_note_basic_auth_failure : 100 -> 92
~ _get_basic_auth : 528 -> 480
~ _note_basic_auth_failure : 180 -> 168
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_auth_basic.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_auth_basic.c"

```
