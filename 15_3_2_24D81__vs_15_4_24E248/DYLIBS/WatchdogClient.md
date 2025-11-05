## WatchdogClient

> `/System/Library/PrivateFrameworks/WatchdogClient.framework/Versions/A/WatchdogClient`

```diff

-277.80.2.0.0
-  __TEXT.__text: 0xfb8
+299.100.5.0.0
+  __TEXT.__text: 0x128c
   __TEXT.__auth_stubs: 0x230
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x109
+  __TEXT.__cstring: 0x133
   __TEXT.__unwind_info: 0x98
-  __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0x40
+  __DATA_CONST.__got: 0x28
+  __DATA_CONST.__const: 0x60
   __AUTH_CONST.__auth_got: 0x118
   __AUTH_CONST.__const: 0x48
-  __DATA_DIRTY.__bss: 0x290
+  __DATA_DIRTY.__bss: 0x388
   - /usr/lib/libSystem.B.dylib
-  UUID: 4850B029-4065-3134-B72E-50EBF3644007
-  Functions: 19
-  Symbols:   97
-  CStrings:  9
+  UUID: B10AB75B-5858-356D-A9A7-5FE36C19382B
+  Functions: 22
+  Symbols:   107
+  CStrings:  10
 
Symbols:
+ ___chkstk_darwin
+ ___wd_kickoff_ping_block_invoke_3
+ __block_descriptor_tmp.7
+ __block_descriptor_tmp.8
+ _wd_endpoint_add_work_processor_block
+ wd_endpoint_add_work_processor_block.cold.1
+ wd_endpoint_add_work_processor_block.cold.2
+ wd_endpoint_add_work_processor_block.cold.3
+ wd_endpoint_add_work_processor_block.cold.4
+ wd_endpoint_add_work_processor_block.cold.5
+ wd_endpoint_add_work_processor_block.cold.6
- __block_descriptor_tmp.6
Functions:
~ __WDOGClient_PollIsAlive : 916 -> 1148
~ _wd_kickoff_ping : 436 -> 596
~ _wd_endpoint_add_queue : 160 -> 168
~ _wd_endpoint_add_work_processor : 196 -> 204
+ _wd_endpoint_add_work_processor_block
~ _wd_endpoint_activate : 376 -> 380
~ _wd_endpoint_begin_watchdog_monitoring_for_service : 308 -> 312
~ _wd_endpoint_disable_monitoring_for_service : 208 -> 212
+ ___wd_kickoff_ping_block_invoke_3
~ __WDOGClient_ReplyIsAlive : 392 -> 388
CStrings:
+ "unresponsive work processor block(s): %s "

```
