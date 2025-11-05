## mod_proxy_ftp.so

> `/usr/libexec/apache2/mod_proxy_ftp.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xbbdc
+880.0.0.0.0
+  __TEXT.__text: 0xabf0
   __TEXT.__auth_stubs: 0x610
   __TEXT.__cstring: 0xeb9
-  __TEXT.__unwind_info: 0x78
+  __TEXT.__unwind_info: 0x88
   __DATA_CONST.__auth_got: 0x308
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 7A343F19-6213-3631-B0EE-E8F3CB24D78A
+  UUID: 70AA4C5D-1F31-3514-9552-C6529A2ACADC
   Functions: 23
   Symbols:   126
   CStrings:  146
Functions:
~ _create_proxy_ftp_dir_config : 92 -> 88
~ _merge_proxy_ftp_dir_config : 432 -> 380
~ _ap_proxy_ftp_register_hook : 228 -> 220
~ _set_ftp_list_on_wildcard : 64 -> 60
~ _set_ftp_escape_wildcards : 64 -> 60
~ _set_ftp_directory_charset : 52 -> 48
~ _proxy_ftp_handler : 29516 -> 27228
~ _proxy_ftp_canon : 2588 -> 2288
~ _proxy_send_dir_filter : 6304 -> 5760
~ _ftp_check_string : 332 -> 284
~ _decodeenc : 344 -> 308
~ _proxy_ftp_command : 3372 -> 3060
~ _ftp_unauthorized : 1120 -> 1028
~ _ftp_escape_globbingchars : 292 -> 268
~ _parse_epsv_reply : 384 -> 332
~ _ftp_check_globbingchars : 204 -> 176
~ _ftp_set_TYPE : 336 -> 312
~ _ftp_get_PWD : 228 -> 200
~ _ftp_getrc_msg : 1152 -> 1016
~ _ftp_string_read : 764 -> 676
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_ftp.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_ftp.c"

```
