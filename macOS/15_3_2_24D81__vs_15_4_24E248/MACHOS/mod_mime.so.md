## mod_mime.so

> `/usr/libexec/apache2/mod_mime.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x2d0c
+880.0.0.0.0
+  __TEXT.__text: 0x2834
   __TEXT.__auth_stubs: 0x270
   __TEXT.__cstring: 0x845
-  __TEXT.__unwind_info: 0x68
+  __TEXT.__unwind_info: 0x78
   __DATA_CONST.__auth_got: 0x138
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 27C2B682-2F92-31E0-9DDF-39ED31991F7F
+  UUID: 1FD39126-16A3-324E-93B3-23F6652463FA
   Functions: 18
   Symbols:   65
   CStrings:  63
Functions:
~ _create_mime_dir_config : 104 -> 100
~ _merge_mime_dir_configs : 628 -> 536
~ _overlay_extension_mappings : 412 -> 344
~ _remove_items : 316 -> 276
~ _add_extension_info : 392 -> 356
~ _multiviews_match : 640 -> 540
~ _remove_extension_info : 224 -> 208
~ _mime_post_config : 796 -> 728
~ _find_ct : 3156 -> 2724
~ _analyze_ct : 3664 -> 3376
~ _zap_sp : 220 -> 196
~ _is_token : 160 -> 144
~ _zap_sp_and_dup : 296 -> 280
~ _is_qtext : 156 -> 140
~ _is_quoted_pair : 132 -> 108
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/http/mod_mime.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/http/mod_mime.c"

```
