## deleted

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted`

```diff

-747.120.2.0.0
-  __TEXT.__text: 0x3f2b8
-  __TEXT.__auth_stubs: 0xe50
-  __TEXT.__objc_stubs: 0x4f20
-  __TEXT.__objc_methlist: 0x2464
-  __TEXT.__const: 0x1a0
-  __TEXT.__gcc_except_tab: 0x1e64
-  __TEXT.__objc_methname: 0x59e3
-  __TEXT.__cstring: 0x2dee
-  __TEXT.__oslogstring: 0x59f6
+795.0.0.502.1
+  __TEXT.__text: 0x424b8
+  __TEXT.__auth_stubs: 0xe90
+  __TEXT.__objc_stubs: 0x5060
+  __TEXT.__objc_methlist: 0x24c4
+  __TEXT.__const: 0x178
+  __TEXT.__gcc_except_tab: 0x1f88
+  __TEXT.__objc_methname: 0x5b64
+  __TEXT.__cstring: 0x32bf
+  __TEXT.__oslogstring: 0x5ffa
   __TEXT.__objc_classname: 0x392
-  __TEXT.__objc_methtype: 0xcb6
-  __TEXT.__unwind_info: 0xae0
-  __DATA_CONST.__auth_got: 0x738
-  __DATA_CONST.__got: 0x208
-  __DATA_CONST.__const: 0x1878
-  __DATA_CONST.__cfstring: 0x2c20
+  __TEXT.__objc_methtype: 0xccd
+  __TEXT.__unwind_info: 0xae8
+  __DATA_CONST.__auth_got: 0x758
+  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__const: 0x18a0
+  __DATA_CONST.__cfstring: 0x3040
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xc0
-  __DATA_CONST.__objc_arraydata: 0x298
-  __DATA_CONST.__objc_dictobj: 0x258
-  __DATA_CONST.__objc_arrayobj: 0x180
   __DATA_CONST.__objc_intobj: 0x120
+  __DATA_CONST.__objc_arraydata: 0x2e8
+  __DATA_CONST.__objc_dictobj: 0x280
+  __DATA_CONST.__objc_arrayobj: 0x198
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x3830
-  __DATA.__objc_selrefs: 0x17d8
-  __DATA.__objc_ivar: 0x27c
+  __DATA.__objc_const: 0x3860
+  __DATA.__objc_selrefs: 0x1828
+  __DATA.__objc_ivar: 0x280
   __DATA.__objc_data: 0x960
   __DATA.__data: 0x4f0
-  __DATA.__bss: 0x198
+  __DATA.__bss: 0x1a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0AA3E65F-4107-31F0-A1BD-9FA59ED56CC7
-  Functions: 938
-  Symbols:   2525
-  CStrings:  2568
+  UUID: C9C0A679-6DDB-3A52-845E-6277750EA037
+  Functions: 953
+  Symbols:   2559
+  CStrings:  2684
 
Symbols:
+ -[CDPurgeOperationResult isIdlePurgeDisk]
+ -[CDPurgeOperationResult setIdlePurge:]
+ -[CacheDelete CheckPurgeableAndUpdateReserveSpace]
+ -[CacheDelete beginIdlePurgeActivityForVolume:]
+ -[CacheDelete checkAndReserveSpace:systemGrowthAmount:centralizedPurgeableFactor:pluginPurgeableFactor:maxReserveSpace:]
+ -[CacheDelete endIdlePurgeActivityForVolume:]
+ -[CacheDelete getReserveSpaceFromUpdateVolume:]
+ -[CacheDelete setEntitledReserve:unentitledReserve:]
+ GCC_except_table129
+ GCC_except_table139
+ GCC_except_table153
+ GCC_except_table49
+ GCC_except_table67
+ GCC_except_table75
+ GCC_except_table85
+ GCC_except_table91
+ GCC_except_table99
+ OBJC_IVAR_$_CDPurgeOperationResult._idlePurge
+ _XPC_ACTIVITY_ALLOW_BATTERY
+ _XPC_ACTIVITY_REQUIRE_SCREEN_SLEEP
+ __101-[CacheDeletePurgeOperation serviceRequest:volume:urgency:donation:info:optionalTestInfo:completion:]_block_invoke.132
+ __19-[CacheDelete init]_block_invoke.82
+ __30-[CacheDelete totalAvailable:]_block_invoke.313
+ __30-[CacheDelete totalAvailable:]_block_invoke.314
+ __30-[CacheDelete totalAvailable:]_block_invoke.317
+ __30-[CacheDelete totalAvailable:]_block_invoke.320
+ __30-[CacheDelete updateFollowup:]_block_invoke.185
+ __33-[CacheDelete clientCancelPurge:]_block_invoke.544
+ __34-[CacheDelete clientSetState:key:]_block_invoke.651
+ __36-[CacheDelete applicationExtensions]_block_invoke.232
+ __36-[CacheDelete applicationExtensions]_block_invoke.240
+ __36-[CacheDelete startPersistenceTimer]_block_invoke.221
+ __37-[CacheDelete checkNotificationState]_block_invoke.187
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.345
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.361
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.362
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.363
+ __37-[CacheDelete purge:volume:callback:]_block_invoke_2.364
+ __38-[CacheDelete clientPurge:replyBlock:]_block_invoke.538
+ __39-[CacheDelete handleVFSStreamXPCEvent:]_block_invoke.206
+ __40-[CacheDelete processLowDiskVolume:key:]_block_invoke.130
+ __40-[CacheDelete processLowDiskVolume:key:]_block_invoke.131
+ __40-[CacheDelete processLowDiskVolume:key:]_block_invoke.133
+ __40-[CacheDelete processLowDiskVolume:key:]_block_invoke_2.132
+ __41-[CacheDelete notifyFollowup:completion:]_block_invoke.178
+ __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.440
+ __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.441
+ __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.72
+ __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.77
+ __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.92
+ __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.93
+ __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.95
+ __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.96
+ __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.410
+ __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.417
+ __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.428
+ __47-[CacheDeleteAnalytics anonymizeAndFlush:name:]_block_invoke.222
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.505
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.506
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.507
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.508
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.509
+ __57-[CacheDelete clientPerformPeriodicsWithInfo:completion:]_block_invoke.555
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.429
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.430
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.435
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.437
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.431
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.436
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.438
+ __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.284
+ __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.286
+ __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.294
+ __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.298
+ ___34-[CacheDelete clientSetState:key:]_block_invoke_2
+ ___47-[CacheDelete beginIdlePurgeActivityForVolume:]_block_invoke
+ ___50-[CacheDelete CheckPurgeableAndUpdateReserveSpace]_block_invoke
+ ___50-[CacheDelete CheckPurgeableAndUpdateReserveSpace]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e8_v16?08ls32l8
+ ___block_descriptor_64_e8_32s40s48s_e22_v16?0"NSDictionary"8ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48r_e51_B24?0r*8^{?=BBqiIQQQ{timespec=qq}{timespec=qq}B}16ls32l8s40l8r48l8
+ ___block_descriptor_91_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ __block_literal_global.1006
+ __block_literal_global.1009
+ __block_literal_global.1012
+ __block_literal_global.1014
+ __block_literal_global.1016
+ __block_literal_global.1020
+ __block_literal_global.1026
+ __block_literal_global.1030
+ __block_literal_global.1034
+ __block_literal_global.171
+ __block_literal_global.189
+ __block_literal_global.199
+ __block_literal_global.259
+ __block_literal_global.279
+ __block_literal_global.316
+ __block_literal_global.319
+ __block_literal_global.90
+ __block_literal_global.966
+ __block_literal_global.970
+ __block_literal_global.974
+ __block_literal_global.977
+ __block_literal_global.999
+ __main_block_invoke.1003
+ __main_block_invoke.1004
+ __main_block_invoke.1018
+ __main_block_invoke.967
+ __main_block_invoke.975
+ __main_block_invoke.997
+ __main_block_invoke_2.1001
+ __main_block_invoke_2.1007
+ __main_block_invoke_2.1022
+ __main_block_invoke_3.1002
+ __main_block_invoke_3.1010
+ __os_feature_enabled_impl
+ __siginfo_handler_block_invoke.1027
+ __siginfo_handler_block_invoke.1031
+ _fallbackThresholds
+ _getReservedSizeFromUpdateVolume
+ _idleXPCActivityScheduled
+ _objc_msgSend$CheckPurgeableAndUpdateReserveSpace
+ _objc_msgSend$beginIdlePurgeActivityForVolume:
+ _objc_msgSend$checkAndReserveSpace:systemGrowthAmount:centralizedPurgeableFactor:pluginPurgeableFactor:maxReserveSpace:
+ _objc_msgSend$effective_size
+ _objc_msgSend$endIdlePurgeActivityForVolume:
+ _objc_msgSend$getReserveSpaceFromUpdateVolume:
+ _objc_msgSend$isIdlePurgeDisk
+ _objc_msgSend$setEntitledReserve:unentitledReserve:
+ _objc_msgSend$setIdlePurge:
+ _objc_msgSend$tmpPath
+ _setiopolicy_np
+ _xpc_bool_create
- GCC_except_table118
- GCC_except_table128
- GCC_except_table131
- GCC_except_table46
- GCC_except_table64
- GCC_except_table72
- GCC_except_table82
- GCC_except_table88
- GCC_except_table94
- __101-[CacheDeletePurgeOperation serviceRequest:volume:urgency:donation:info:optionalTestInfo:completion:]_block_invoke.123
- __19-[CacheDelete init]_block_invoke.65
- __30-[CacheDelete totalAvailable:]_block_invoke.286
- __30-[CacheDelete totalAvailable:]_block_invoke.287
- __30-[CacheDelete totalAvailable:]_block_invoke.290
- __30-[CacheDelete totalAvailable:]_block_invoke.293
- __30-[CacheDelete updateFollowup:]_block_invoke.164
- __33-[CacheDelete clientCancelPurge:]_block_invoke.450
- __36-[CacheDelete applicationExtensions]_block_invoke.206
- __36-[CacheDelete applicationExtensions]_block_invoke.214
- __36-[CacheDelete startPersistenceTimer]_block_invoke.195
- __37-[CacheDelete checkNotificationState]_block_invoke.168
- __37-[CacheDelete purge:volume:callback:]_block_invoke.326
- __37-[CacheDelete purge:volume:callback:]_block_invoke.327
- __37-[CacheDelete purge:volume:callback:]_block_invoke.328
- __38-[CacheDelete clientPurge:replyBlock:]_block_invoke.444
- __39-[CacheDelete handleVFSStreamXPCEvent:]_block_invoke.184
- __40-[CacheDelete processLowDiskVolume:key:]_block_invoke.109
- __40-[CacheDelete processLowDiskVolume:key:]_block_invoke.110
- __40-[CacheDelete processLowDiskVolume:key:]_block_invoke.112
- __40-[CacheDelete processLowDiskVolume:key:]_block_invoke_2.111
- __41-[CacheDelete notifyFollowup:completion:]_block_invoke.157
- __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.401
- __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.402
- __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.63
- __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.68
- __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.83
- __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.84
- __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.86
- __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.87
- __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.371
- __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.378
- __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.389
- __47-[CacheDeleteAnalytics anonymizeAndFlush:name:]_block_invoke.213
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.411
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.412
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.413
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.414
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.415
- __57-[CacheDelete clientPerformPeriodicsWithInfo:completion:]_block_invoke.461
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.390
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.391
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.396
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.398
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.392
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.397
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.399
- __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.258
- __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.267
- __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.271
- ___89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke_2
- ___block_descriptor_56_e8_32s40s_e22_v16?0"NSDictionary"8ls32l8s40l8
- ___block_descriptor_72_e8_32s40s48r_e50_B24?0r*8^{?=BBqiIQQQ{timespec=qq}{timespec=qq}}16ls32l8s40l8r48l8
- ___block_descriptor_81_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- __block_literal_global.150
- __block_literal_global.170
- __block_literal_global.177
- __block_literal_global.233
- __block_literal_global.253
- __block_literal_global.289
- __block_literal_global.292
- __block_literal_global.73
- __block_literal_global.853
- __block_literal_global.857
- __block_literal_global.861
- __block_literal_global.864
- __block_literal_global.894
- __block_literal_global.901
- __block_literal_global.904
- __block_literal_global.907
- __block_literal_global.909
- __block_literal_global.911
- __block_literal_global.915
- __block_literal_global.921
- __block_literal_global.925
- __block_literal_global.929
- __main_block_invoke.854
- __main_block_invoke.862
- __main_block_invoke.892
- __main_block_invoke.898
- __main_block_invoke.899
- __main_block_invoke.913
- __main_block_invoke_2.896
- __main_block_invoke_2.902
- __main_block_invoke_2.917
- __main_block_invoke_3.897
- __main_block_invoke_3.905
- __siginfo_handler_block_invoke.922
- __siginfo_handler_block_invoke.926
- _objc_retain_x6
CStrings:
+ " APFSIOC_GET_FREE_QUEUE_INFO: free_queue_bytes:%lld free_queue_tier2_bytes: %lld"
+ " checkAndReserveSpace %@"
+ " checkAndReserveSpace purgeable available %lld amount to reserve %lld"
+ " processLowDiskVolume: %@"
+ " triggering CheckPurgeableAndUpdateReserveSpace after purgeable"
+ " triggering CheckPurgeableAndUpdateReserveSpace from daily activity"
+ " tryFSPurge goal %@"
+ "\"r"
+ "%@ is not entitled to purge with kCacheDeleteUrgencySpecialCase or with CACHE_DELETE_RELEASE_SPACE_KEY"
+ "%d  pausing reservation monitoring %@"
+ "%d CheckPurgeableAndUpdateReserveSpace %@"
+ "%d CheckPurgeableAndUpdateReserveSpace %f %f %f"
+ "%d Purge Result: %@ "
+ "%d Starting purgeable with Info %@"
+ "%d _clientSetState "
+ "%d _clientSetState %@ "
+ "%d _clientSetState %f "
+ "%d checkAndReserveSpace  "
+ "%d checkAndReserveSpace amountToReserve: %lld systemGrowthAmount:%lld "
+ "%d clientSetState setting %@"
+ "%d purgeable ended with Info %@"
+ "%d tryFSPurge WARNING: Calculating goal (missing from info dict: %@)"
+ "Amount to reserve is too large %lld effectiveSize %lld"
+ "B24@?0r*8^{?=BBqiIQQQ{timespec=qq}{timespec=qq}B}16"
+ "Begin delayed idle low disk activity for volume %@"
+ "CACHE_DELETE_ENABLE_RESERVE_SPACE"
+ "CACHE_DELETE_ENTITLED_RESERVATION"
+ "CACHE_DELETE_ENTITLED_RESERVATION_ALLOCED"
+ "CACHE_DELETE_ENTITLED_RESERVATION_FREE"
+ "CACHE_DELETE_ENTITLED_RESERVATION_SECURED"
+ "CACHE_DELETE_EXPECTED_SYSTEM_GROWTH_AMOUNT"
+ "CACHE_DELETE_EXTRA_SHARED_FREE"
+ "CACHE_DELETE_FACTOR_FOR_CENTRALIZED_PURGEABLE"
+ "CACHE_DELETE_FACTOR_FOR_PLUGIN_PURGEABLE"
+ "CACHE_DELETE_FREESPACE_GOAL"
+ "CACHE_DELETE_MAX_RESERVE_SPACE_AMOUNT"
+ "CACHE_DELETE_RELEASE_SPACE"
+ "CACHE_DELETE_REPORTABLE_RESERVE_SPACE_AMOUNT"
+ "CACHE_DELETE_RESERVE_SPACE"
+ "CACHE_DELETE_RESERVE_SPACE_AMOUNT"
+ "CACHE_DELETE_RESERVE_SPACE_ENABLED"
+ "CACHE_DELETE_RESERVE_SPACE_FILESYSTEM_AMOUNT"
+ "CACHE_DELETE_RESERVE_SPACE_PAUSE_TIMESTAMP"
+ "CACHE_DELETE_SET_RESERVE_SPACE_ENTITLEMENT"
+ "CACHE_DELETE_SUR_THRESHOLD"
+ "CACHE_DELETE_UNENTITLED_CD_THRESHOLD"
+ "CACHE_DELETE_UNENTITLED_RESERVATION"
+ "CACHE_DELETE_UNENTITLED_RESERVATION_ALLOCED"
+ "CACHE_DELETE_UNENTITLED_RESERVATION_FREE"
+ "CACHE_DELETE_UNENTITLED_RESERVE_AMOUNT"
+ "CD_IDLE_PURGE_NOTIFY_DISK_EVENT"
+ "CheckPurgeableAndUpdateReserveSpace"
+ "Clearing delayed idle disk purge activity for volume %@"
+ "Connection interrupted for service %@ with no outstanding messages, tearing down"
+ "IdlePurgeDiskEvent"
+ "Purge: goal %@ freespace %llu"
+ "Returning without getting purgeable due to pending requests"
+ "Running idle purge activity %p"
+ "Setting entitled reservation to %lld and untitled to %lld"
+ "TB,N,GisIdlePurgeDisk,V_idlePurge"
+ "[%d] checkAndReserveSpace updateInfo: %@"
+ "_idlePurge"
+ "beginIdlePurgeActivityForVolume:"
+ "caught VQ_IDLE_PURGE_NOTIFY on \"%{public}@\""
+ "checkAndReserveSpace:systemGrowthAmount:centralizedPurgeableFactor:pluginPurgeableFactor:maxReserveSpace:"
+ "clientGetState Client is not entitled to get key: %@"
+ "com.apple.cache_delete.IdlePurge"
+ "dailyNumIdlePurgeDiskEvents"
+ "dailyNumIdlePurgeDiskPurges%s"
+ "dailyNumIdlePurgeDiskSuccess%s"
+ "effective_size"
+ "enablePreallocatedSpace"
+ "enablePreallocatedSpace is off "
+ "endIdlePurgeActivityForVolume:"
+ "getReserveSpaceFromUpdateVolume APFSIOC_ENTITLED_RESERVE failed for %@ : %s"
+ "getReserveSpaceFromUpdateVolume:"
+ "idlePurge"
+ "idlepurgediskPeriodS"
+ "idlepurgediskTimeS"
+ "idlepurgedisk_success"
+ "isIdlePurgeDisk"
+ "mainVolume: %{public}@, freespace:%lld initialfreespace:%lld"
+ "mainVolume: %{public}@, fstype: %{public}@ freespace:%lld "
+ "setEntitledReserve APFSIOC_ENTITLED_RESERVE failed for %@ : %s"
+ "setEntitledReserve:unentitledReserve:"
+ "setIdlePurge:"
+ "tmpPath"
+ "v56@0:8@16@24@32@40@48"
- "%@ is not entitled to purge with kCacheDeleteUrgencySpecialCase"
- "%d Purge Result: %@"
- "B24@?0r*8^{?=BBqiIQQQ{timespec=qq}{timespec=qq}}16"
- "clientGetState Client is not entitled to set key: %@"
- "mainVolume: %{public}@, fstype: %{public}@"
- "there is no entitlement required for key: %@"

```
