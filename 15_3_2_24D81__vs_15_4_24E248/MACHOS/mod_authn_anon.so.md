## mod_authn_anon.so

> `/usr/libexec/apache2/mod_authn_anon.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x7e4
+880.0.0.0.0
+  __TEXT.__text: 0x6f0
   __TEXT.__auth_stubs: 0x70
   __TEXT.__cstring: 0x1a8
-  __TEXT.__unwind_info: 0x48
+  __TEXT.__unwind_info: 0x58
   __DATA_CONST.__auth_got: 0x38
   __DATA_CONST.__const: 0x100
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: BFFBC33C-AD15-3665-8253-6405AAA801B1
+  UUID: 9C86EB43-8576-3408-A035-B72007AC6A5E
   Functions: 4
   Symbols:   15
   CStrings:  15
Functions:
~ _anon_set_string_slots : 256 -> 228
~ _check_anonymous : 1576 -> 1360
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authn_anon.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authn_anon.c"

```
