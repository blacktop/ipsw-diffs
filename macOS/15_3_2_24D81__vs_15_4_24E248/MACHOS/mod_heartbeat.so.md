## mod_heartbeat.so

> `/usr/libexec/apache2/mod_heartbeat.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x8ec
+880.0.0.0.0
+  __TEXT.__text: 0x80c
   __TEXT.__auth_stubs: 0x120
   __TEXT.__cstring: 0x25c
-  __TEXT.__unwind_info: 0x58
+  __TEXT.__unwind_info: 0x68
   __DATA_CONST.__auth_got: 0x90
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 5E88BA4B-1B4F-3A3C-A55E-187ABD70B0D7
+  UUID: 0EE5B985-1E79-3478-BBAC-AF5B6B5EC3DB
   Functions: 8
   Symbols:   31
   CStrings:  13
Functions:
~ _hb_create_config : 72 -> 68
~ _cmd_hb_address : 444 -> 380
~ _hb_watchdog_need : 176 -> 148
~ _hb_watchdog_init : 108 -> 104
~ _hb_watchdog_step : 160 -> 140
~ _hb_monitor : 1112 -> 1008
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/cluster/mod_heartbeat.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/cluster/mod_heartbeat.c"

```
