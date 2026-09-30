## mod_imagemap.so

> `/usr/libexec/apache2/mod_imagemap.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x2988
+880.0.0.0.0
+  __TEXT.__text: 0x24a4
   __TEXT.__auth_stubs: 0x1d0
   __TEXT.__cstring: 0x421
-  __TEXT.__unwind_info: 0x78
+  __TEXT.__unwind_info: 0x88
   __DATA_CONST.__auth_got: 0xe8
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: F829F5E4-5228-3852-8212-E93C6AF732DC
+  UUID: 5F638064-F804-34E8-9665-2A028213548D
   Functions: 21
   Symbols:   55
   CStrings:  51
Functions:
~ _create_imap_dir_config : 84 -> 80
~ _merge_imap_dir_configs : 292 -> 256
~ _imap_handler : 160 -> 136
~ _imap_handler_internal : 3324 -> 2852
~ _imap_url : 1752 -> 1492
~ _get_x_coord : 276 -> 240
~ _get_y_coord : 304 -> 264
~ _menu_header : 264 -> 256
~ _menu_blank : 200 -> 176
~ _menu_comment : 292 -> 252
~ _read_quoted : 280 -> 256
~ _menu_default : 488 -> 448
~ _menu_directive : 488 -> 448
~ _pointinpoly : 948 -> 840
~ _imap_reply : 220 -> 188
~ _pointincircle : 236 -> 232
~ _pointinrect : 428 -> 404
~ _is_closer : 268 -> 244
~ _ap_rputs : 212 -> 200
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/mappers/mod_imagemap.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/mappers/mod_imagemap.c"

```
