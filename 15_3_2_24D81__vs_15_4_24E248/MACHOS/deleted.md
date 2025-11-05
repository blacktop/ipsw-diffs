## deleted

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted`

```diff

-742.80.2.0.0
-  __TEXT.__text: 0x46158
-  __TEXT.__auth_stubs: 0xd50
+747.100.15.0.0
+  __TEXT.__text: 0x463a4
+  __TEXT.__auth_stubs: 0xd70
   __TEXT.__objc_stubs: 0x4f60
-  __TEXT.__objc_methlist: 0x1f24
+  __TEXT.__objc_methlist: 0x23c4
   __TEXT.__const: 0x190
-  __TEXT.__gcc_except_tab: 0x1ce0
-  __TEXT.__objc_methname: 0x57ee
-  __TEXT.__cstring: 0x2d0a
-  __TEXT.__oslogstring: 0x598e
-  __TEXT.__objc_classname: 0x366
-  __TEXT.__objc_methtype: 0xcd2
-  __TEXT.__unwind_info: 0xb30
-  __DATA_CONST.__auth_got: 0x6b8
+  __TEXT.__gcc_except_tab: 0x1d1c
+  __TEXT.__objc_methname: 0x583c
+  __TEXT.__cstring: 0x2d4f
+  __TEXT.__oslogstring: 0x59e4
+  __TEXT.__objc_classname: 0x387
+  __TEXT.__objc_methtype: 0xcd5
+  __TEXT.__unwind_info: 0xb38
+  __DATA_CONST.__auth_got: 0x6c8
   __DATA_CONST.__got: 0x250
   __DATA_CONST.__const: 0x1a78
-  __DATA_CONST.__cfstring: 0x2b60
+  __DATA_CONST.__cfstring: 0x2b80
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x2d8
   __DATA_CONST.__objc_dictobj: 0x280
   __DATA_CONST.__objc_arrayobj: 0x180
   __DATA_CONST.__objc_intobj: 0x120
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x3f20
-  __DATA.__objc_selrefs: 0x1710
+  __DATA.__objc_const: 0x36d8
+  __DATA.__objc_selrefs: 0x17c8
   __DATA.__objc_ivar: 0x26c
   __DATA.__objc_data: 0x910
-  __DATA.__data: 0x488
-  __DATA.__bss: 0x168
+  __DATA.__data: 0x4e8
+  __DATA.__bss: 0x178
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 25C53958-7059-3145-9985-EE76CD3BF8A8
-  Functions: 1005
-  Symbols:   2558
-  CStrings:  2565
+  UUID: 4C03A03D-A79C-3FEA-ABA0-826D863943D3
+  Functions: 1007
+  Symbols:   2569
+  CStrings:  2572
 
Symbols:
+ +[CacheDeleteListener(Daemon) daemonPrivateListenerWithExportedObject:]
+ -[CacheDelete shouldUpdatePurgeable:]
+ -[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]
+ GCC_except_table100
+ GCC_except_table111
+ GCC_except_table141
+ GCC_except_table157
+ GCC_except_table160
+ GCC_except_table171
+ GCC_except_table18
+ GCC_except_table24
+ GCC_except_table34
+ GCC_except_table36
+ GCC_except_table40
+ GCC_except_table42
+ GCC_except_table77
+ GCC_except_table92
+ __101-[CacheDeletePurgeOperation serviceRequest:volume:urgency:donation:info:optionalTestInfo:completion:]_block_invoke.126
+ __101-[CacheDeletePurgeOperation serviceRequest:volume:urgency:donation:info:optionalTestInfo:completion:]_block_invoke.129
+ __30-[CacheDelete totalAvailable:]_block_invoke.279
+ __30-[CacheDelete totalAvailable:]_block_invoke.280
+ __30-[CacheDelete totalAvailable:]_block_invoke.283
+ __30-[CacheDelete totalAvailable:]_block_invoke.286
+ __33-[CacheDelete clientCancelPurge:]_block_invoke.461
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.321
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.322
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.323
+ __38-[CacheDelete clientPurge:replyBlock:]_block_invoke.451
+ __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.407
+ __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.408
+ __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.66
+ __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.71
+ __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.86
+ __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.89
+ __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.90
+ __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.369
+ __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.389
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.417
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.418
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.419
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.420
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.421
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.422
+ __49-[CacheDelete clientPerformOperation:replyBlock:]_block_invoke.539
+ __57-[CacheDelete clientPerformPeriodicsWithInfo:completion:]_block_invoke.472
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.394
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.395
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.402
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.404
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.396
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.403
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.405
+ __73-[CDDaemonPurgeableResultCache updateRecentInfoForServiceID:volume:info:]_block_invoke.60
+ __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.251
+ __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.262
+ __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.263
+ __OBJC_$_PROTOCOL_REFS_CacheDeletePrivateClientProtocol
+ __OBJC_LABEL_PROTOCOL_$_CacheDeletePrivateClientProtocol
+ __OBJC_PROTOCOL_$_CacheDeletePrivateClientProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_CacheDeletePrivateClientProtocol
+ ___37-[CacheDelete shouldUpdatePurgeable:]_block_invoke
+ ___37-[CacheDelete shouldUpdatePurgeable:]_block_invoke_2
+ ___89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke
+ ___89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke_2
+ ___DADiskDisappearedCallback_block_invoke.952
+ ___DADiskDisappearedCallback_block_invoke.953
+ ___block_descriptor_33_e18_B16?0"AppCache"8l
+ ___block_descriptor_33_e28_B24?0"NSString"8"NSURL"16l
+ __block_literal_global.224
+ __block_literal_global.246
+ __block_literal_global.282
+ __block_literal_global.285
+ __block_literal_global.62
+ __block_literal_global.859
+ __block_literal_global.863
+ __block_literal_global.866
+ __block_literal_global.896
+ __block_literal_global.902
+ __block_literal_global.905
+ __block_literal_global.922
+ __block_literal_global.928
+ __block_literal_global.931
+ __block_literal_global.934
+ __block_literal_global.938
+ __block_literal_global.950
+ __block_literal_global.958
+ __block_literal_global.962
+ __block_literal_global.966
+ __main_block_invoke.856
+ __main_block_invoke.864
+ __main_block_invoke.894
+ __main_block_invoke.920
+ __main_block_invoke.936
+ __main_block_invoke_2.898
+ __main_block_invoke_2.923
+ __main_block_invoke_2.940
+ __main_block_invoke_3.899
+ __main_block_invoke_3.926
+ __main_block_invoke_4.929
+ __main_block_invoke_5.932
+ __siginfo_handler_block_invoke.959
+ __siginfo_handler_block_invoke.963
+ _isSpecialAPFSVolume
+ _objc_msgSend$appCacheWithRecords:identifier:groupIdentifiers:dataContainerURL:userManagedAssetsURL:personaUniqueString:isDataseparated:isPlaceholder:isPlugin:telemetry:
+ _objc_msgSend$bundleIdentifiers
+ _objc_msgSend$updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:
+ _volumeSupportsEAPFS
- -[CDDaemonPurgeableResultCache shouldUpdatePurgeable:]
- -[CacheDelete updateRecentResultsForVolumes:withInfo:qos:receiveResults:]
- GCC_except_table107
- GCC_except_table137
- GCC_except_table153
- GCC_except_table156
- GCC_except_table17
- GCC_except_table22
- GCC_except_table32
- GCC_except_table39
- GCC_except_table41
- GCC_except_table43
- GCC_except_table89
- GCC_except_table96
- __101-[CacheDeletePurgeOperation serviceRequest:volume:urgency:donation:info:optionalTestInfo:completion:]_block_invoke.124
- __101-[CacheDeletePurgeOperation serviceRequest:volume:urgency:donation:info:optionalTestInfo:completion:]_block_invoke.127
- __30-[CacheDelete totalAvailable:]_block_invoke.269
- __30-[CacheDelete totalAvailable:]_block_invoke.270
- __30-[CacheDelete totalAvailable:]_block_invoke.273
- __33-[CacheDelete clientCancelPurge:]_block_invoke.448
- __37-[CacheDelete purge:volume:callback:]_block_invoke.308
- __37-[CacheDelete purge:volume:callback:]_block_invoke.309
- __37-[CacheDelete purge:volume:callback:]_block_invoke.310
- __38-[CacheDelete clientPurge:replyBlock:]_block_invoke.438
- __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.394
- __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.395
- __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.69
- __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.84
- __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.85
- __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.88
- __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.356
- __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.363
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.404
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.405
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.406
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.407
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.408
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.409
- __49-[CacheDelete clientPerformOperation:replyBlock:]_block_invoke.526
- __57-[CacheDelete clientPerformPeriodicsWithInfo:completion:]_block_invoke.459
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.381
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.382
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.389
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.391
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.383
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.390
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.392
- __73-[CDDaemonPurgeableResultCache updateRecentInfoForServiceID:volume:info:]_block_invoke.79
- __73-[CacheDelete updateRecentResultsForVolumes:withInfo:qos:receiveResults:]_block_invoke.238
- __73-[CacheDelete updateRecentResultsForVolumes:withInfo:qos:receiveResults:]_block_invoke.249
- __73-[CacheDelete updateRecentResultsForVolumes:withInfo:qos:receiveResults:]_block_invoke.250
- ___54-[CDDaemonPurgeableResultCache shouldUpdatePurgeable:]_block_invoke
- ___54-[CDDaemonPurgeableResultCache shouldUpdatePurgeable:]_block_invoke_2
- ___73-[CacheDelete updateRecentResultsForVolumes:withInfo:qos:receiveResults:]_block_invoke
- ___73-[CacheDelete updateRecentResultsForVolumes:withInfo:qos:receiveResults:]_block_invoke_2
- ___DADiskDisappearedCallback_block_invoke.939
- ___DADiskDisappearedCallback_block_invoke.940
- ___block_descriptor_32_e18_B16?0"AppCache"8l
- ___block_descriptor_32_e28_B24?0"NSString"8"NSURL"16l
- __block_literal_global.233
- __block_literal_global.272
- __block_literal_global.41
- __block_literal_global.76
- __block_literal_global.78
- __block_literal_global.81
- __block_literal_global.840
- __block_literal_global.846
- __block_literal_global.850
- __block_literal_global.883
- __block_literal_global.889
- __block_literal_global.892
- __block_literal_global.909
- __block_literal_global.912
- __block_literal_global.915
- __block_literal_global.918
- __block_literal_global.921
- __block_literal_global.937
- __block_literal_global.945
- __block_literal_global.949
- __block_literal_global.953
- __main_block_invoke.843
- __main_block_invoke.851
- __main_block_invoke.881
- __main_block_invoke.907
- __main_block_invoke.923
- __main_block_invoke_2.885
- __main_block_invoke_2.910
- __main_block_invoke_2.927
- __main_block_invoke_3.886
- __main_block_invoke_3.913
- __main_block_invoke_4.916
- __main_block_invoke_5.919
- __siginfo_handler_block_invoke.946
- __siginfo_handler_block_invoke.950
- _objc_msgSend$appCacheWithRecords:identifier:dataContainerURL:userManagedAssetsURL:personaUniqueString:isDataseparated:isPlaceholder:isPlugin:telemetry:
- _objc_msgSend$bundleRecords
- _objc_msgSend$updateRecentResultsForVolumes:withInfo:qos:receiveResults:
CStrings:
+ "%d totalAvailable shouldUpdatePurgeable"
+ "CacheDeletePrivateClientProtocol"
+ "appCacheWithRecords:identifier:groupIdentifiers:dataContainerURL:userManagedAssetsURL:personaUniqueString:isDataseparated:isPlaceholder:isPlugin:telemetry:"
+ "bundleIdentifiers"
+ "com.apple.cache_delete.private"
+ "com.apple.cache_delete.purge_fsevents"
+ "daemonPrivateListenerWithExportedObject:"
+ "return after updating fsPurgeable"
+ "totalAvailable fspurgeable operationResult is %@"
+ "updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:"
+ "v48@0:8@16B24@28I36@?40"
- "appCacheWithRecords:identifier:dataContainerURL:userManagedAssetsURL:personaUniqueString:isDataseparated:isPlaceholder:isPlugin:telemetry:"
- "bundleRecords"
- "emitRecentInfo shouldUpdatePurgeable"
- "updateRecentResultsForVolumes:withInfo:qos:receiveResults:"
- "v44@0:8@16@24I32@?36"

```
