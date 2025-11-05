## mod_deflate.so

> `/usr/libexec/apache2/mod_deflate.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x8f24
+880.0.0.0.0
+  __TEXT.__text: 0x848c
   __TEXT.__auth_stubs: 0x330
   __TEXT.__cstring: 0xedb
   __TEXT.__const: 0x14
-  __TEXT.__unwind_info: 0x74
+  __TEXT.__unwind_info: 0x80
   __DATA_CONST.__auth_got: 0x198
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x190

   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
   - /usr/lib/libz.1.dylib
-  UUID: EE8DB57A-73D1-32C7-9839-BD867A6E9190
+  UUID: 0C9BE80A-2A43-3602-A0B2-F968C2DB353E
   Functions: 26
   Symbols:   85
   CStrings:  106
Functions:
~ _deflate_set_note : 324 -> 288
~ _deflate_set_window_size : 180 -> 168
~ _deflate_set_buffer_size : 152 -> 140
~ _deflate_set_memlevel : 172 -> 160
~ _deflate_set_compressionlevel : 172 -> 160
~ _deflate_set_inflate_limit : 188 -> 156
~ _deflate_set_inflate_ratio_limit : 128 -> 120
~ _deflate_set_inflate_ratio_burst : 128 -> 120
~ _deflate_set_etag : 252 -> 224
~ _deflate_out_filter : 14888 -> 13708
~ _inflate_out_filter : 8492 -> 8000
~ _deflate_in_filter : 7200 -> 6792
~ _have_ssl_compression : 180 -> 156
~ _deflate_ctx_cleanup : 88 -> 76
~ _deflate_check_etag : 552 -> 500
~ _flush_libz_buffer : 336 -> 292
~ _consume_buffer : 260 -> 248
~ _check_gzip : 972 -> 784
~ _consume_zlib_flags : 1192 -> 1072
~ _check_ratio : 188 -> 168
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_deflate.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_deflate.c"

```
