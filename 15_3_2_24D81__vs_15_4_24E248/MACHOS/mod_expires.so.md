## mod_expires.so

> `/usr/libexec/apache2/mod_expires.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xfa0
+880.0.0.0.0
+  __TEXT.__text: 0xe24
   __TEXT.__auth_stubs: 0x1a0
   __TEXT.__cstring: 0x2bd
-  __TEXT.__unwind_info: 0x54
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0xd0
   __DATA_CONST.__const: 0xa0
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 69A93811-F906-3CF3-88CF-64A1D614C25C
+  UUID: BC7CFC68-63F0-35A8-B66C-5BA671C0931E
   Functions: 10
   Symbols:   38
   CStrings:  35
Functions:
~ _create_dir_expires_config : 120 -> 116
~ _merge_expires_dir_configs : 276 -> 252
~ _set_expiresactive : 84 -> 72
~ _set_expiresbytype : 360 -> 328
~ _set_expiresdefault : 196 -> 180
~ _check_code : 1176 -> 1040
~ _expires_filter : 800 -> 716
~ _expires_insert_filter : 256 -> 220
~ _set_expiration_fields : 600 -> 564
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/metadata/mod_expires.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/metadata/mod_expires.c"

```
