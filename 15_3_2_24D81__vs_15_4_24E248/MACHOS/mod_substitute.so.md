## mod_substitute.so

> `/usr/libexec/apache2/mod_substitute.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x45e4
+880.0.0.0.0
+  __TEXT.__text: 0x406c
   __TEXT.__auth_stubs: 0x240
   __TEXT.__cstring: 0x361
   __TEXT.__const: 0xb
-  __TEXT.__unwind_info: 0x50
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0x120
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0xa0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: E1C05A95-8EB7-31A9-B2E9-DD3EC1E77F8D
+  UUID: D25BEB2C-5B41-3305-ACD8-40DF230A48DD
   Functions: 7
   Symbols:   49
   CStrings:  25
Functions:
~ _create_substitute_dcfg : 116 -> 112
~ _merge_substitute_dcfg : 348 -> 320
~ _set_pattern : 1332 -> 1120
~ _set_max_line_length : 588 -> 488
~ _substitute_filter : 3304 -> 3100
~ _do_pattmatch : 12136 -> 11284
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_substitute.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_substitute.c"

```
