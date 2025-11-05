## mod_heartmonitor.so

> `/usr/libexec/apache2/mod_heartmonitor.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x3604
+880.0.0.0.0
+  __TEXT.__text: 0x3284
   __TEXT.__auth_stubs: 0x430
   __TEXT.__cstring: 0x8ae
-  __TEXT.__unwind_info: 0x60
+  __TEXT.__unwind_info: 0x70
   __DATA_CONST.__auth_got: 0x218
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 7AA6B7DD-363F-3858-9CDA-35316D699AA4
+  UUID: 267E7C4D-6CAA-312D-B93C-DEC13DE398EC
   Functions: 23
   Symbols:   98
   CStrings:  68
Functions:
~ _hm_create_config : 192 -> 180
~ _cmd_hm_listen : 444 -> 380
~ _cmd_hm_storage : 176 -> 156
~ _cmd_hm_maxworkers : 180 -> 156
~ _hm_post_config : 1600 -> 1524
~ _hm_handler : 656 -> 628
~ _hm_watchdog_callback : 1676 -> 1568
~ _hm_listen : 1080 -> 1032
~ _hm_update_stats : 104 -> 96
~ _hm_recv : 528 -> 492
~ _hm_slotmem_update_stats : 288 -> 264
~ _hm_file_update_stats : 1316 -> 1240
~ _hm_slotmem_remove_stat : 164 -> 156
~ _hm_slotmem_update_stat : 380 -> 368
~ _hm_readid : 148 -> 128
~ _hm_update : 180 -> 160
~ _hm_processmsg : 1028 -> 964
~ _qs_to_table : 280 -> 256
~ _hm_get_server : 204 -> 196
~ _hm_update_stat : 112 -> 104
~ _ap_rputs : 212 -> 200
~ _hm_file_update_stat : 2768 -> 2572
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/cluster/mod_heartmonitor.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/cluster/mod_heartmonitor.c"

```
