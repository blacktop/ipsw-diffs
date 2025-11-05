## mod_session.so

> `/usr/libexec/apache2/mod_session.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x2bf8
+880.0.0.0.0
+  __TEXT.__text: 0x27b4
   __TEXT.__auth_stubs: 0x290
   __TEXT.__cstring: 0x68a
-  __TEXT.__unwind_info: 0x8c
+  __TEXT.__unwind_info: 0x98
   __DATA_CONST.__auth_got: 0x148
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__const: 0x140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: DCD4C011-F97B-3C45-B6D8-4D26E416A3B6
+  UUID: 4081BD99-DF47-3029-A9CF-CCFDA9E2E38C
   Functions: 34
   Symbols:   75
   CStrings:  40
Functions:
~ _ap_hook_session_load : 264 -> 248
~ _ap_run_session_load : 224 -> 204
~ _ap_hook_session_save : 272 -> 256
~ _ap_run_session_save : 236 -> 216
~ _ap_hook_session_encode : 272 -> 256
~ _ap_run_session_encode : 256 -> 228
~ _ap_hook_session_decode : 272 -> 256
~ _ap_run_session_decode : 256 -> 228
~ _create_session_dir_config : 140 -> 136
~ _merge_session_dir_config : 876 -> 784
~ _register_hooks : 448 -> 432
~ _set_session_enable : 64 -> 60
~ _set_session_maxage : 96 -> 80
~ _set_session_header : 64 -> 60
~ _set_session_env : 64 -> 60
~ _add_session_include : 100 -> 80
~ _add_session_exclude : 100 -> 80
~ _set_session_expiry_update : 168 -> 156
~ _session_output_filter : 484 -> 412
~ _session_fixups : 236 -> 204
~ _session_identity_encode : 304 -> 284
~ _session_identity_decode : 572 -> 476
~ _ap_session_get : 216 -> 172
~ _ap_session_set : 244 -> 200
~ _ap_session_load : 2752 -> 2524
~ _ap_session_save : 1284 -> 1168
~ _identity_count : 124 -> 120
~ _identity_concat : 204 -> 188
~ _session_included : 544 -> 476
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/session/mod_session.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/session/mod_session.c"

```
