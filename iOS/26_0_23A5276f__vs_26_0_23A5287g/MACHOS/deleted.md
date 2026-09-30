## deleted

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted`

```diff

-804.0.0.0.1
-  __TEXT.__text: 0x42a64
+806.0.0.0.1
+  __TEXT.__text: 0x42b00
   __TEXT.__auth_stubs: 0xea0
   __TEXT.__objc_stubs: 0x5080
   __TEXT.__objc_methlist: 0x24c4
   __TEXT.__const: 0x178
-  __TEXT.__gcc_except_tab: 0x1f88
+  __TEXT.__gcc_except_tab: 0x1f64
   __TEXT.__objc_methname: 0x5b33
-  __TEXT.__cstring: 0x32f3
-  __TEXT.__oslogstring: 0x6116
+  __TEXT.__cstring: 0x3318
+  __TEXT.__oslogstring: 0x616e
   __TEXT.__objc_classname: 0x392
   __TEXT.__objc_methtype: 0xcb6
-  __TEXT.__unwind_info: 0xaf0
+  __TEXT.__unwind_info: 0xb30
   __DATA_CONST.__auth_got: 0x760
   __DATA_CONST.__got: 0x218
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x18a0
-  __DATA_CONST.__cfstring: 0x3080
+  __DATA_CONST.__cfstring: 0x30a0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E868DC91-F5C6-32F9-88FC-0F645D81DEB0
+  UUID: E755B14C-6E8F-3ED4-85A2-CC33ACD9B3CF
   Functions: 953
   Symbols:   2563
-  CStrings:  2694
+  CStrings:  2698
 
Symbols:
+ __33-[CacheDelete clientCancelPurge:]_block_invoke.550
+ __34-[CacheDelete clientSetState:key:]_block_invoke.660
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.342
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.358
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.359
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.360
+ __37-[CacheDelete purge:volume:callback:]_block_invoke_2.361
+ __38-[CacheDelete clientPurge:replyBlock:]_block_invoke.544
+ __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.437
+ __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.438
+ __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.407
+ __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.414
+ __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.425
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.513
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.514
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.515
+ __57-[CacheDelete clientPerformPeriodicsWithInfo:completion:]_block_invoke.561
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.426
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.427
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.432
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.434
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.428
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.433
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.435
+ __block_literal_global.1004
+ __block_literal_global.1017
+ __block_literal_global.1019
+ __block_literal_global.1021
+ __block_literal_global.1025
+ __block_literal_global.1031
+ __block_literal_global.1035
+ __block_literal_global.1039
+ __block_literal_global.971
+ __block_literal_global.975
+ __block_literal_global.982
+ __main_block_invoke.1002
+ __main_block_invoke.1008
+ __main_block_invoke.1009
+ __main_block_invoke.1023
+ __main_block_invoke.972
+ __main_block_invoke.980
+ __main_block_invoke_2.1006
+ __main_block_invoke_2.1012
+ __main_block_invoke_2.1027
+ __main_block_invoke_3.1007
+ __main_block_invoke_3.1015
+ __siginfo_handler_block_invoke.1032
+ __siginfo_handler_block_invoke.1036
- __33-[CacheDelete clientCancelPurge:]_block_invoke.547
- __34-[CacheDelete clientSetState:key:]_block_invoke.657
- __37-[CacheDelete purge:volume:callback:]_block_invoke.345
- __37-[CacheDelete purge:volume:callback:]_block_invoke.361
- __37-[CacheDelete purge:volume:callback:]_block_invoke.362
- __37-[CacheDelete purge:volume:callback:]_block_invoke.363
- __37-[CacheDelete purge:volume:callback:]_block_invoke_2.364
- __38-[CacheDelete clientPurge:replyBlock:]_block_invoke.541
- __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.440
- __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.441
- __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.410
- __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.417
- __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.428
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.508
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.509
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.510
- __57-[CacheDelete clientPerformPeriodicsWithInfo:completion:]_block_invoke.558
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.429
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.430
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.435
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.437
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.431
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.436
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.438
- __block_literal_global.1001
- __block_literal_global.1008
- __block_literal_global.1016
- __block_literal_global.1018
- __block_literal_global.1022
- __block_literal_global.1028
- __block_literal_global.1032
- __block_literal_global.1036
- __block_literal_global.968
- __block_literal_global.972
- __block_literal_global.976
- __main_block_invoke.1005
- __main_block_invoke.1006
- __main_block_invoke.1020
- __main_block_invoke.969
- __main_block_invoke.977
- __main_block_invoke.999
- __main_block_invoke_2.1003
- __main_block_invoke_2.1009
- __main_block_invoke_2.1024
- __main_block_invoke_3.1004
- __main_block_invoke_3.1012
- __siginfo_handler_block_invoke.1029
- __siginfo_handler_block_invoke.1033
CStrings:
+ "%d cache_delete purge satisfied the request amountPurged %lld requested %lld"
+ "CACHE_DELETE_DO_NOT_UPDATE_PURGEABLE"
+ "Disabling Entitled IOPolicy"
+ "Enabling Entitled IOPolicy"
- "%d cache_delete purge satisfied the request"

```
