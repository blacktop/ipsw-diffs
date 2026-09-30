## deleted

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted`

```diff

-742.80.2.0.0
-  __TEXT.__text: 0x3eb34
-  __TEXT.__auth_stubs: 0xe30
-  __TEXT.__objc_stubs: 0x4ea0
-  __TEXT.__objc_methlist: 0x1f54
+747.100.14.0.1
+  __TEXT.__text: 0x3f2b8
+  __TEXT.__auth_stubs: 0xe50
+  __TEXT.__objc_stubs: 0x4f20
+  __TEXT.__objc_methlist: 0x2464
   __TEXT.__const: 0x1a0
-  __TEXT.__gcc_except_tab: 0x1e28
-  __TEXT.__objc_methname: 0x5807
-  __TEXT.__cstring: 0x2d36
-  __TEXT.__oslogstring: 0x591f
-  __TEXT.__objc_classname: 0x371
-  __TEXT.__objc_methtype: 0xcb3
-  __TEXT.__unwind_info: 0xb40
-  __DATA_CONST.__auth_got: 0x728
+  __TEXT.__gcc_except_tab: 0x1e64
+  __TEXT.__objc_methname: 0x59e3
+  __TEXT.__cstring: 0x2dee
+  __TEXT.__oslogstring: 0x59f6
+  __TEXT.__objc_classname: 0x392
+  __TEXT.__objc_methtype: 0xcb6
+  __TEXT.__unwind_info: 0xb48
+  __DATA_CONST.__auth_got: 0x738
   __DATA_CONST.__got: 0x208
   __DATA_CONST.__const: 0x1878
-  __DATA_CONST.__cfstring: 0x2ba0
+  __DATA_CONST.__cfstring: 0x2c20
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x298
   __DATA_CONST.__objc_dictobj: 0x258
   __DATA_CONST.__objc_arrayobj: 0x180
   __DATA_CONST.__objc_intobj: 0x120
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x3fe0
-  __DATA.__objc_selrefs: 0x16e8
-  __DATA.__objc_ivar: 0x270
+  __DATA.__objc_const: 0x3830
+  __DATA.__objc_selrefs: 0x17d8
+  __DATA.__objc_ivar: 0x27c
   __DATA.__objc_data: 0x960
-  __DATA.__data: 0x490
-  __DATA.__bss: 0x188
+  __DATA.__data: 0x4f0
+  __DATA.__bss: 0x198
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 929
-  Symbols:   2498
-  CStrings:  2205
+  Functions: 938
+  Symbols:   2525
+  CStrings:  2229
 
Symbols:
+ +[CacheDeleteListener(Daemon) daemonPrivateListenerWithExportedObject:]
+ -[CacheDelete clientGetPendingStorageThreshold:replyBlock:]
+ -[CacheDelete pendingStorageLevels]
+ -[CacheDelete pendingStorageThresholds]
+ -[CacheDelete privateListener]
+ -[CacheDelete setPendingStorageLevels:]
+ -[CacheDelete setPendingStorageThresholds:]
+ -[CacheDelete setPrivateListener:]
+ -[CacheDelete shouldUpdatePurgeable:]
+ -[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]
+ GCC_except_table118
+ GCC_except_table128
+ GCC_except_table131
+ GCC_except_table142
+ GCC_except_table18
+ GCC_except_table25
+ GCC_except_table29
+ GCC_except_table36
+ GCC_except_table72
+ GCC_except_table82
+ GCC_except_table88
+ GCC_except_table94
+ OBJC_IVAR_$_CacheDelete._pendingStorageLevels
+ OBJC_IVAR_$_CacheDelete._pendingStorageThresholds
+ OBJC_IVAR_$_CacheDelete._privateListener
+ __101-[CacheDeletePurgeOperation serviceRequest:volume:urgency:donation:info:optionalTestInfo:completion:]_block_invoke.123
+ __30-[CacheDelete totalAvailable:]_block_invoke.286
+ __30-[CacheDelete totalAvailable:]_block_invoke.287
+ __30-[CacheDelete totalAvailable:]_block_invoke.290
+ __30-[CacheDelete totalAvailable:]_block_invoke.293
+ __33-[CacheDelete clientCancelPurge:]_block_invoke.450
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.326
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.327
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.328
+ __38-[CacheDelete clientPurge:replyBlock:]_block_invoke.444
+ __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.401
+ __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.402
+ __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.63
+ __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.68
+ __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.83
+ __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.86
+ __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.87
+ __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.371
+ __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.389
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.411
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.412
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.413
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.414
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.415
+ __57-[CacheDelete clientPerformPeriodicsWithInfo:completion:]_block_invoke.461
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.390
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.391
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.396
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.398
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.392
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.397
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.399
+ __73-[CDDaemonPurgeableResultCache updateRecentInfoForServiceID:volume:info:]_block_invoke.60
+ __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.258
+ __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.267
+ __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.271
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CacheDeletePrivateClientProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CacheDeletePrivateClientProtocol
+ __OBJC_$_PROTOCOL_REFS_CacheDeletePrivateClientProtocol
+ __OBJC_LABEL_PROTOCOL_$_CacheDeletePrivateClientProtocol
+ __OBJC_PROTOCOL_$_CacheDeletePrivateClientProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_CacheDeletePrivateClientProtocol
+ ___37-[CacheDelete shouldUpdatePurgeable:]_block_invoke
+ ___37-[CacheDelete shouldUpdatePurgeable:]_block_invoke_2
+ ___89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke
+ ___89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke_2
+ ___block_descriptor_33_e18_B16?0"AppCache"8l
+ ___block_descriptor_33_e28_B24?0"NSString"8"NSURL"16l
+ __block_literal_global.233
+ __block_literal_global.253
+ __block_literal_global.289
+ __block_literal_global.292
+ __block_literal_global.62
+ __block_literal_global.853
+ __block_literal_global.857
+ __block_literal_global.861
+ __block_literal_global.864
+ __block_literal_global.894
+ __block_literal_global.901
+ __block_literal_global.904
+ __block_literal_global.907
+ __block_literal_global.909
+ __block_literal_global.911
+ __block_literal_global.915
+ __block_literal_global.921
+ __block_literal_global.925
+ __block_literal_global.929
+ __main_block_invoke.854
+ __main_block_invoke.892
+ __main_block_invoke.898
+ __main_block_invoke.899
+ __main_block_invoke.913
+ __main_block_invoke_2.896
+ __main_block_invoke_2.902
+ __main_block_invoke_2.917
+ __main_block_invoke_3.897
+ __main_block_invoke_3.905
+ __siginfo_handler_block_invoke.922
+ __siginfo_handler_block_invoke.926
+ _isSpecialAPFSVolume
+ _objc_msgSend$appCacheWithRecords:identifier:groupIdentifiers:dataContainerURL:userManagedAssetsURL:personaUniqueString:isDataseparated:isPlaceholder:isPlugin:telemetry:
+ _objc_msgSend$bundleIdentifiers
+ _objc_msgSend$daemonPrivateListenerWithExportedObject:
+ _objc_msgSend$pendingStorageLevels
+ _objc_msgSend$pendingStorageThresholds
+ _objc_msgSend$privateListener
+ _objc_msgSend$updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:
+ _volumeSupportsEAPFS
- -[CDDaemonPurgeableResultCache shouldUpdatePurgeable:]
- -[CacheDelete updateRecentResultsForVolumes:withInfo:qos:receiveResults:]
- GCC_except_table114
- GCC_except_table124
- GCC_except_table127
- GCC_except_table17
- GCC_except_table19
- GCC_except_table23
- GCC_except_table28
- GCC_except_table39
- GCC_except_table41
- GCC_except_table79
- GCC_except_table84
- GCC_except_table90
- __101-[CacheDeletePurgeOperation serviceRequest:volume:urgency:donation:info:optionalTestInfo:completion:]_block_invoke.121
- __30-[CacheDelete totalAvailable:]_block_invoke.278
- __30-[CacheDelete totalAvailable:]_block_invoke.279
- __30-[CacheDelete totalAvailable:]_block_invoke.282
- __33-[CacheDelete clientCancelPurge:]_block_invoke.439
- __37-[CacheDelete purge:volume:callback:]_block_invoke.315
- __37-[CacheDelete purge:volume:callback:]_block_invoke.316
- __37-[CacheDelete purge:volume:callback:]_block_invoke.317
- __38-[CacheDelete clientPurge:replyBlock:]_block_invoke.433
- __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.390
- __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.391
- __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.66
- __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.81
- __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.82
- __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.85
- __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.360
- __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.367
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.400
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.401
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.402
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.403
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.404
- __57-[CacheDelete clientPerformPeriodicsWithInfo:completion:]_block_invoke.450
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.379
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.380
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.385
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.387
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.381
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.386
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.388
- __73-[CDDaemonPurgeableResultCache updateRecentInfoForServiceID:volume:info:]_block_invoke.79
- __73-[CacheDelete updateRecentResultsForVolumes:withInfo:qos:receiveResults:]_block_invoke.247
- __73-[CacheDelete updateRecentResultsForVolumes:withInfo:qos:receiveResults:]_block_invoke.256
- __73-[CacheDelete updateRecentResultsForVolumes:withInfo:qos:receiveResults:]_block_invoke.260
- ___54-[CDDaemonPurgeableResultCache shouldUpdatePurgeable:]_block_invoke
- ___54-[CDDaemonPurgeableResultCache shouldUpdatePurgeable:]_block_invoke_2
- ___73-[CacheDelete updateRecentResultsForVolumes:withInfo:qos:receiveResults:]_block_invoke
- ___73-[CacheDelete updateRecentResultsForVolumes:withInfo:qos:receiveResults:]_block_invoke_2
- ___block_descriptor_32_e18_B16?0"AppCache"8l
- ___block_descriptor_32_e28_B24?0"NSString"8"NSURL"16l
- __block_literal_global.242
- __block_literal_global.281
- __block_literal_global.41
- __block_literal_global.81
- __block_literal_global.817
- __block_literal_global.821
- __block_literal_global.825
- __block_literal_global.828
- __block_literal_global.83
- __block_literal_global.85
- __block_literal_global.858
- __block_literal_global.865
- __block_literal_global.868
- __block_literal_global.871
- __block_literal_global.873
- __block_literal_global.875
- __block_literal_global.879
- __block_literal_global.885
- __block_literal_global.889
- __block_literal_global.893
- __main_block_invoke.818
- __main_block_invoke.826
- __main_block_invoke.856
- __main_block_invoke.863
- __main_block_invoke.877
- __main_block_invoke_2.860
- __main_block_invoke_2.866
- __main_block_invoke_2.881
- __main_block_invoke_3.861
- __main_block_invoke_3.869
- __siginfo_handler_block_invoke.886
- __siginfo_handler_block_invoke.890
- _objc_msgSend$appCacheWithRecords:identifier:dataContainerURL:userManagedAssetsURL:personaUniqueString:isDataseparated:isPlaceholder:isPlugin:telemetry:
- _objc_msgSend$bundleRecords
- _objc_msgSend$updateRecentResultsForVolumes:withInfo:qos:receiveResults:
CStrings:
+ "\x1f\x06\x15"
+ "%d deleted clientGetPendingStorageThreshold with: %@"
+ "%d totalAvailable shouldUpdatePurgeable"
+ "CACHE_DELETE_RESULTS"
+ "CacheDeletePrivateClientProtocol"
+ "Evaluating low disk notification"
+ "Sending notification for volume: %@ in persistent very low disk state"
+ "T@\"CacheDeleteListener\",&,N,V_privateListener"
+ "T@\"NSMutableDictionary\",&,N,V_pendingStorageLevels"
+ "T@\"NSMutableDictionary\",&,N,V_pendingStorageThresholds"
+ "_pendingStorageLevels"
+ "_pendingStorageThresholds"
+ "_privateListener"
+ "appCacheWithRecords:identifier:groupIdentifiers:dataContainerURL:userManagedAssetsURL:personaUniqueString:isDataseparated:isPlaceholder:isPlugin:telemetry:"
+ "bundleIdentifiers"
+ "clientGetPendingStorageThreshold:replyBlock:"
+ "com.apple.cache_delete.private"
+ "com.apple.cache_delete.purge_fsevents"
+ "daemonPrivateListenerWithExportedObject:"
+ "missing or invalid key: %@"
+ "pendingStorageLevels"
+ "pendingStorageThresholds"
+ "privateListener"
+ "return after updating fsPurgeable"
+ "setPendingStorageLevels:"
+ "setPendingStorageThresholds:"
+ "setPrivateListener:"
+ "totalAvailable fspurgeable operationResult is %@"
+ "updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:"
+ "v48@0:8@16B24@28I36@?40"
+ "volume path %@ does not currently have a pending storage threshold"
- "\x1f\x05\x13"
- "Sent low disk notification"
- "appCacheWithRecords:identifier:dataContainerURL:userManagedAssetsURL:personaUniqueString:isDataseparated:isPlaceholder:isPlugin:telemetry:"
- "bundleRecords"
- "emitRecentInfo shouldUpdatePurgeable"
- "updateRecentResultsForVolumes:withInfo:qos:receiveResults:"
- "v44@0:8@16@24I32@?36"

```
