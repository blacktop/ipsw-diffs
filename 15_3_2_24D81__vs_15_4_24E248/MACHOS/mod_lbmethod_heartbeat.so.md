## mod_lbmethod_heartbeat.so

> `/usr/libexec/apache2/mod_lbmethod_heartbeat.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x14e0
+880.0.0.0.0
+  __TEXT.__text: 0x1320
   __TEXT.__auth_stubs: 0x290
   __TEXT.__cstring: 0x29c
-  __TEXT.__unwind_info: 0x64
+  __TEXT.__unwind_info: 0x70
   __DATA_CONST.__auth_got: 0x148
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 36A8F978-6587-3E35-90E7-346CDC05F6DF
+  UUID: BE3DBAB5-A775-36BB-9DC3-137D988C55AE
   Functions: 13
   Symbols:   63
   CStrings:  26
Functions:
~ _lb_hb_create_config : 84 -> 80
~ _lb_hb_merge_config : 172 -> 152
~ _register_hooks : 112 -> 120
~ _cmd_lb_hb_storage : 176 -> 156
~ _lb_hb_init : 664 -> 628
~ _find_best_hb : 1988 -> 1828
~ _read_heartbeats : 152 -> 144
~ _readfile_heartbeats : 1232 -> 1080
~ _hm_read : 388 -> 348
~ _argstr_to_table : 236 -> 220
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/balancers/mod_lbmethod_heartbeat.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/balancers/mod_lbmethod_heartbeat.c"

```
