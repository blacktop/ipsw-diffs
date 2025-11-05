## mod_logio.so

> `/usr/libexec/apache2/mod_logio.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x928
+880.0.0.0.0
+  __TEXT.__text: 0x89c
   __TEXT.__auth_stubs: 0x120
   __TEXT.__cstring: 0x155
   __TEXT.__const: 0x20
-  __TEXT.__unwind_info: 0x6c
+  __TEXT.__unwind_info: 0x78
   __DATA_CONST.__auth_got: 0x90
   __DATA_CONST.__const: 0x50
   __DATA.__data: 0x80

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 4D9C2EDB-C513-3B06-A492-A1E0806FFC6E
+  UUID: C5D42AFA-10F8-3AC9-910C-F77FA2C1E6C8
   Functions: 16
   Symbols:   39
   CStrings:  14
Functions:
~ _create_logio_dirconf : 64 -> 60
~ _register_hooks : 424 -> 412
~ _logio_track_ttfb : 68 -> 64
~ _logio_pre_config : 268 -> 260
~ _logio_transaction : 100 -> 96
~ _logio_in_filter : 204 -> 196
~ _logio_insert_filter : 124 -> 108
~ _logio_ttfb_filter : 292 -> 252
~ _ap_logio_add_bytes_out : 72 -> 68
~ _ap_logio_add_bytes_in : 72 -> 68
~ _ap_logio_get_last_bytes : 56 -> 52
~ _log_bytes_in : 92 -> 88
~ _log_bytes_out : 92 -> 88
~ _log_bytes_combined : 104 -> 100
~ _log_ttfb : 176 -> 156
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/loggers/mod_logio.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/loggers/mod_logio.c"

```
