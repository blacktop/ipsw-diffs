## mod_watchdog.so

> `/usr/libexec/apache2/mod_watchdog.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x3488
+880.0.0.0.0
+  __TEXT.__text: 0x3074
   __TEXT.__auth_stubs: 0x2d0
   __TEXT.__cstring: 0x4f2
-  __TEXT.__unwind_info: 0x84
+  __TEXT.__unwind_info: 0x90
   __DATA_CONST.__auth_got: 0x168
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 81AD5855-A5EA-34B0-B8B5-FF4331F283A6
+  UUID: A1A1DF13-8C69-3CC1-88AC-9FFFF1482C13
   Functions: 23
   Symbols:   76
   CStrings:  39
Functions:
~ _wd_register_hooks : 304 -> 292
~ _ap_hook_watchdog_need : 264 -> 248
~ _ap_run_watchdog_need : 240 -> 220
~ _ap_hook_watchdog_init : 272 -> 256
~ _ap_run_watchdog_init : 264 -> 236
~ _ap_hook_watchdog_exit : 272 -> 256
~ _ap_run_watchdog_exit : 264 -> 236
~ _ap_hook_watchdog_step : 272 -> 256
~ _ap_run_watchdog_step : 264 -> 236
~ _wd_cmd_watchdog_int : 244 -> 220
~ _wd_pre_config_hook : 360 -> 320
~ _wd_post_config_hook : 4892 -> 4636
~ _wd_child_init_hook : 1312 -> 1220
~ _ap_watchdog_get_instance : 408 -> 360
~ _ap_watchdog_register_callback : 316 -> 296
~ _ap_watchdog_set_callback_interval : 196 -> 172
~ _wd_startup : 276 -> 252
~ _wd_worker : 2688 -> 2388
~ _wd_worker_cleanup : 280 -> 244
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/core/mod_watchdog.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/core/mod_watchdog.c"

```
