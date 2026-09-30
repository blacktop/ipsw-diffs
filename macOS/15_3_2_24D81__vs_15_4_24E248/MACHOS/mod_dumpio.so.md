## mod_dumpio.so

> `/usr/libexec/apache2/mod_dumpio.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x1970
+880.0.0.0.0
+  __TEXT.__text: 0x1780
   __TEXT.__auth_stubs: 0xa0
   __TEXT.__cstring: 0x21d
-  __TEXT.__unwind_info: 0x64
+  __TEXT.__unwind_info: 0x70
   __DATA_CONST.__auth_got: 0x50
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x78

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 4CF196AD-A35A-35A1-BE9F-46897454BECC
+  UUID: 81CB3251-02F2-3AC0-8BE8-9EA3A58CEBAA
   Functions: 8
   Symbols:   21
   CStrings:  25
Functions:
~ _dumpio_enable_input : 76 -> 72
~ _dumpio_enable_output : 76 -> 72
~ _dumpio_output_filter : 988 -> 908
~ _dumpio_input_filter : 1932 -> 1780
~ _dumpio_pre_conn : 744 -> 672
~ _dumpit : 2464 -> 2280
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/debugging/mod_dumpio.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/debugging/mod_dumpio.c"

```
