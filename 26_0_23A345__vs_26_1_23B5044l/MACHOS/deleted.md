## deleted

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted`

```diff

-811.0.0.0.0
-  __TEXT.__text: 0x42db8
+815.0.0.0.0
+  __TEXT.__text: 0x42e54
   __TEXT.__auth_stubs: 0xea0
   __TEXT.__objc_stubs: 0x50a0
   __TEXT.__objc_methlist: 0x24c4

   __TEXT.__gcc_except_tab: 0x1f64
   __TEXT.__objc_methname: 0x5b4a
   __TEXT.__cstring: 0x3362
-  __TEXT.__oslogstring: 0x618a
+  __TEXT.__oslogstring: 0x61b2
   __TEXT.__objc_classname: 0x392
   __TEXT.__objc_methtype: 0xcb6
   __TEXT.__unwind_info: 0xb30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3460CBE5-B18C-382D-BCF5-2808DFDB161B
+  UUID: 1B5F2E30-D4B0-3BE2-BF9A-811259308893
   Functions: 953
   Symbols:   2564
-  CStrings:  2705
+  CStrings:  2706
 
Symbols:
+ __30-[CacheDelete totalAvailable:]_block_invoke.316
+ __30-[CacheDelete totalAvailable:]_block_invoke.323
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.345
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.361
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.362
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.363
+ __37-[CacheDelete purge:volume:callback:]_block_invoke_2.364
+ __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.440
+ __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.441
+ __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.410
+ __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.417
+ __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.428
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.429
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.430
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.435
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.437
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.431
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.436
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.438
+ __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.287
+ __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.289
+ __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.297
+ __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.301
+ ___block_descriptor_92_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ __block_literal_global.282
+ __block_literal_global.322
- __30-[CacheDelete totalAvailable:]_block_invoke.313
- __30-[CacheDelete totalAvailable:]_block_invoke.314
- __37-[CacheDelete purge:volume:callback:]_block_invoke.342
- __37-[CacheDelete purge:volume:callback:]_block_invoke.358
- __37-[CacheDelete purge:volume:callback:]_block_invoke.359
- __37-[CacheDelete purge:volume:callback:]_block_invoke.360
- __37-[CacheDelete purge:volume:callback:]_block_invoke_2.361
- __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.437
- __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.438
- __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.407
- __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.414
- __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.425
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.426
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.427
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.432
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.434
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.428
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.433
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.435
- __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.284
- __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.286
- __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.294
- __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.298
- ___block_descriptor_91_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- __block_literal_global.279
- __block_literal_global.316
Functions:
~ -[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:] : 1264 -> 1300
~ __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.284 -> __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.287 : 688 -> 696
~ -[CacheDelete processPurgeNotification:forService:info:group:force:] : 2820 -> 2668
~ ___45-[CacheDelete _notifyRecipients:value:force:]_block_invoke_2 : 1104 -> 1128
~ ___50-[CacheDelete CheckPurgeableAndUpdateReserveSpace]_block_invoke_2 : 724 -> 964
CStrings:
+ "%d CheckPurgeableAndUpdateReserveSpace "

```
