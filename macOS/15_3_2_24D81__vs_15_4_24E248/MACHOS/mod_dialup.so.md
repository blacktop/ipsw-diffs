## mod_dialup.so

> `/usr/libexec/apache2/mod_dialup.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xbd8
+880.0.0.0.0
+  __TEXT.__text: 0xaf0
   __TEXT.__auth_stubs: 0x1a0
   __TEXT.__cstring: 0x223
-  __TEXT.__unwind_info: 0x48
+  __TEXT.__unwind_info: 0x58
   __DATA_CONST.__auth_got: 0xd0
   __DATA_CONST.__const: 0xc0
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 38CB398D-D847-392A-878F-B73607F31FD5
+  UUID: AA945D8F-A4C4-30A1-A83F-9BFFD1E71F5B
   Functions: 6
   Symbols:   35
   CStrings:  14
Functions:
~ _dialup_dcfg_create : 68 -> 64
~ _cmd_modem_standard : 252 -> 220
~ _dialup_handler : 1100 -> 1012
~ _dialup_send_pulse : 1148 -> 1072
~ _dialup_callback : 396 -> 364
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/test/mod_dialup.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/test/mod_dialup.c"

```
