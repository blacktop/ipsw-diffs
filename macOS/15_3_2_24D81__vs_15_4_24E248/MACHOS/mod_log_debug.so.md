## mod_log_debug.so

> `/usr/libexec/apache2/mod_log_debug.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x1754
+880.0.0.0.0
+  __TEXT.__text: 0x15b4
   __TEXT.__auth_stubs: 0x1a0
   __TEXT.__cstring: 0x29b
-  __TEXT.__unwind_info: 0x50
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0xd0
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0xc0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 865F60B4-C5E3-3680-AD92-1C2F2DF46ADB
+  UUID: 202696D8-E236-3923-83DD-D54B90D4C493
   Functions: 18
   Symbols:   49
   CStrings:  28
Functions:
~ _log_debug_create_dconf : 64 -> 60
~ _log_debug_merge_dconf : 220 -> 192
~ _cmd_log_message : 1236 -> 1108
~ _do_debug_log : 3204 -> 2948
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/loggers/mod_log_debug.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/loggers/mod_log_debug.c"

```
