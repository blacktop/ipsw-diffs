## mod_cgi.so

> `/usr/libexec/apache2/mod_cgi.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x4568
+880.0.0.0.0
+  __TEXT.__text: 0x3f4c
   __TEXT.__auth_stubs: 0x530
   __TEXT.__cstring: 0x8e4
-  __TEXT.__unwind_info: 0x88
+  __TEXT.__unwind_info: 0x98
   __DATA_CONST.__auth_got: 0x298
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 03740BC9-7BE2-3455-A452-7DB6EACEC07C
+  UUID: 6F744A8F-D2EA-37B6-8C78-AD1C4814DAF2
   Functions: 29
   Symbols:   127
   CStrings:  82
Functions:
~ _create_cgi_dirconf : 64 -> 60
~ _create_cgi_config : 108 -> 104
~ _merge_cgi_config : 100 -> 84
~ _set_scriptlog : 196 -> 180
~ _set_scriptlog_length : 120 -> 100
~ _set_scriptlog_buffer : 128 -> 108
~ _set_script_timeout : 116 -> 104
~ _cgi_handler : 1984 -> 1812
~ _cgi_post_config : 120 -> 112
~ _cgi_optfns_retrieve : 196 -> 172
~ _is_scriptaliased : 128 -> 116
~ _log_scripterror : 840 -> 760
~ _run_cgi_child : 1308 -> 1160
~ _cgi_handle_request : 824 -> 720
~ _cgi_bucket_create : 812 -> 784
~ _cgi_handle_response : 1168 -> 1028
~ _cgi_child_errfn : 140 -> 136
~ _cgi_bucket_read : 864 -> 780
~ _cgi_read_stdout : 488 -> 460
~ _log_script_err : 384 -> 348
~ _log_script : 1684 -> 1516
~ _discard_script_output : 316 -> 304
~ _default_build_command : 604 -> 540
~ _cgi_handle_exec : 2892 -> 2680
~ _include_cmd : 716 -> 672
~ _include_cgi : 692 -> 628
~ _add_ssi_vars : 444 -> 404
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/generators/cgi_common.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/generators/mod_cgi.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/generators/cgi_common.h"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/generators/mod_cgi.c"

```
