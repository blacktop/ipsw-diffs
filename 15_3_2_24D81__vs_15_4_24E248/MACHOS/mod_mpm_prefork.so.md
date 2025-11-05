## mod_mpm_prefork.so

> `/usr/libexec/apache2/mod_mpm_prefork.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x50dc
+880.0.0.0.0
+  __TEXT.__text: 0x4bb4
   __TEXT.__auth_stubs: 0x5c0
   __TEXT.__cstring: 0xe6b
-  __TEXT.__unwind_info: 0x84
+  __TEXT.__unwind_info: 0x90
   __DATA_CONST.__auth_got: 0x2e0
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x218

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 7A121E73-1573-3AF5-96B5-AA0CE825A07C
+  UUID: 5CFB255F-C28C-3C0B-A8E0-B7344C620602
   Functions: 25
   Symbols:   153
   CStrings:  84
Functions:
~ _set_daemons_to_start : 120 -> 108
~ _set_min_free_servers : 120 -> 108
~ _set_max_free_servers : 120 -> 108
~ _set_max_clients : 596 -> 544
~ _set_server_limit : 120 -> 108
~ _prefork_open_logs : 2976 -> 2796
~ _prefork_pre_config : 808 -> 724
~ _prefork_check_config : 2372 -> 2248
~ _prefork_run : 4920 -> 4644
~ _prefork_query : 384 -> 380
~ _make_child : 636 -> 588
~ _startup_children : 232 -> 208
~ _perform_idle_server_maintenance : 1576 -> 1468
~ _prefork_note_child_started : 156 -> 152
~ _child_main : 3212 -> 2964
~ _clean_child_exit : 216 -> 192
~ _accept_mutex_on : 740 -> 692
~ _accept_mutex_off : 740 -> 692
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/server/mpm/prefork/prefork.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/server/mpm/prefork/prefork.c"

```
