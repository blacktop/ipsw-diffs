## mod_macro.so

> `/usr/libexec/apache2/mod_macro.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x2778
+880.0.0.0.0
+  __TEXT.__text: 0x2390
   __TEXT.__auth_stubs: 0x1c0
   __TEXT.__cstring: 0x7c4
-  __TEXT.__unwind_info: 0x74
+  __TEXT.__unwind_info: 0x80
   __DATA_CONST.__auth_got: 0xe0
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 62FC1E60-93B5-3969-A3E0-B47B624786E7
+  UUID: A305BC24-3EAD-3597-A46B-654B9E227730
   Functions: 20
   Symbols:   55
   CStrings:  55
Functions:
~ _macro_section : 1300 -> 1200
~ _use_macro : 824 -> 768
~ _undef_macro : 296 -> 264
~ _warn_if_non_blank : 352 -> 312
~ _looks_like_an_argument : 64 -> 60
~ _get_arguments : 320 -> 292
~ _check_macro_arguments : 1072 -> 980
~ _get_lines_till_end_token : 1096 -> 960
~ _check_macro_contents : 696 -> 640
~ _process_content : 508 -> 468
~ _substitute_macro_args : 456 -> 392
~ _next_substitution : 332 -> 280
~ _substitute : 800 -> 704
~ _number_of_escapes : 156 -> 132
~ _check_macro_use_arguments : 328 -> 284
~ _make_array_config : 324 -> 308
~ _array_getch : 512 -> 460
~ _array_getstr : 448 -> 400
~ _array_close : 68 -> 64
~ _next_one : 152 -> 136
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/core/mod_macro.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/core/mod_macro.c"

```
