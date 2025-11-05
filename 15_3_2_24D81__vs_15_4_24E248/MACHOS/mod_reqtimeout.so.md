## mod_reqtimeout.so

> `/usr/libexec/apache2/mod_reqtimeout.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x1f88
+880.0.0.0.0
+  __TEXT.__text: 0x1cc4
   __TEXT.__auth_stubs: 0x1e0
   __TEXT.__cstring: 0x2ce
-  __TEXT.__unwind_info: 0x60
+  __TEXT.__unwind_info: 0x70
   __DATA_CONST.__auth_got: 0xf0
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 4E1D09C5-818B-3E76-A0F4-C61B0708C066
+  UUID: 08145900-E304-3DBE-A05F-D399241B6D8B
   Functions: 15
   Symbols:   52
   CStrings:  20
Functions:
~ _reqtimeout_create_srv_config : 192 -> 188
~ _reqtimeout_merge_srv_config : 952 -> 892
~ _set_reqtimeouts : 328 -> 300
~ _set_reqtimeout_param : 812 -> 692
~ _parse_int : 244 -> 224
~ _reqtimeout_filter : 2704 -> 2436
~ _reqtimeout_eor : 148 -> 136
~ _reqtimeout_init : 512 -> 476
~ _reqtimeout_before_header : 300 -> 280
~ _reqtimeout_before_body : 324 -> 304
~ _check_time_left : 200 -> 184
~ _extend_timeout : 220 -> 200
~ _have_lf_or_eos : 336 -> 296
~ _brigade_append : 556 -> 512
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_reqtimeout.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_reqtimeout.c"

```
