## mod_log_forensic.so

> `/usr/libexec/apache2/mod_log_forensic.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xcb8
+880.0.0.0.0
+  __TEXT.__text: 0xbd4
   __TEXT.__auth_stubs: 0x180
   __TEXT.__cstring: 0x1b4
   __TEXT.__const: 0x200
-  __TEXT.__unwind_info: 0x60
+  __TEXT.__unwind_info: 0x70
   __DATA_CONST.__auth_got: 0xc0
   __DATA_CONST.__const: 0x60
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: F3AF4ADE-7A32-32DA-B4E0-B937D43CDD48
+  UUID: C51ACB52-8CD4-3E02-BAA5-F1AE673FDF83
   Functions: 12
   Symbols:   41
   CStrings:  16
Functions:
~ _merge_forensic_log_scfg : 188 -> 172
~ _set_forensic_log : 76 -> 72
~ _log_init : 140 -> 124
~ _log_before : 868 -> 820
~ _log_after : 344 -> 308
~ _open_log : 608 -> 552
~ _count_headers : 108 -> 104
~ _count_string : 144 -> 128
~ _log_escape : 380 -> 352
~ _log_headers : 168 -> 164
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/loggers/mod_log_forensic.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/loggers/mod_log_forensic.c"

```
