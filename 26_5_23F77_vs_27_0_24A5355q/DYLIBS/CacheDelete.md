## CacheDelete

> `/System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete`

```diff

-819.120.2.0.0
-  __TEXT.__text: 0x37d28
-  __TEXT.__auth_stubs: 0xce0
-  __TEXT.__objc_methlist: 0x1724
+901.0.0.0.1
+  __TEXT.__text: 0x368bc
+  __TEXT.__objc_methlist: 0x1884
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__const: 0x1f0
-  __TEXT.__cstring: 0x2466
-  __TEXT.__oslogstring: 0x5dd7
-  __TEXT.__gcc_except_tab: 0xdec
-  __TEXT.__unwind_info: 0xb18
-  __TEXT.__objc_classname: 0x2a3
-  __TEXT.__objc_methname: 0x3a7d
-  __TEXT.__objc_methtype: 0xa5a
-  __TEXT.__objc_stubs: 0x35e0
-  __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__const: 0xd48
-  __DATA_CONST.__objc_classlist: 0x88
+  __TEXT.__const: 0x1f8
+  __TEXT.__gcc_except_tab: 0xd30
+  __TEXT.__cstring: 0x259c
+  __TEXT.__oslogstring: 0x6081
+  __TEXT.__unwind_info: 0xa70
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xe30
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1090
+  __DATA_CONST.__objc_selrefs: 0x1158
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x70
-  __DATA_CONST.__objc_arraydata: 0x1d0
-  __AUTH_CONST.__auth_got: 0x680
-  __AUTH_CONST.__const: 0x5a0
-  __AUTH_CONST.__cfstring: 0x2080
-  __AUTH_CONST.__objc_const: 0x2160
+  __DATA_CONST.__objc_superrefs: 0x78
+  __DATA_CONST.__objc_arraydata: 0x200
+  __DATA_CONST.__got: 0x1e8
+  __AUTH_CONST.__const: 0x600
+  __AUTH_CONST.__cfstring: 0x2180
+  __AUTH_CONST.__objc_const: 0x2388
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH_CONST.__objc_intobj: 0x1b0
-  __AUTH_CONST.__objc_dictobj: 0x320
+  __AUTH_CONST.__objc_intobj: 0x1c8
+  __AUTH_CONST.__objc_dictobj: 0x370
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x150
+  __AUTH_CONST.__auth_got: 0x6d8
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x170
   __DATA.__data: 0x4f8
   __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_ivar: 0x2c
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__data: 0xc
-  __DATA_DIRTY.__bss: 0x1b0
+  __DATA_DIRTY.__bss: 0x1c0
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6D9FA18D-1953-3590-9813-17C17EBF0305
-  Functions: 776
-  Symbols:   2591
-  CStrings:  1994
+  UUID: 3FA20360-7BFF-3951-898F-01CCF8CD34EA
+  Functions: 815
+  Symbols:   2729
+  CStrings:  1155
 
Symbols:
+ +[AppCache sortedCachesForInstalledAppsOnVolume:urgency:calculate:bytesNeeded:telemetry:]
+ -[CDPurgeablePathEnumerator .cxx_destruct]
+ -[CDPurgeablePathEnumerator _createItemDictionaryForPath:urgency:]
+ -[CDPurgeablePathEnumerator _getPathsForAppCache:]
+ -[CDPurgeablePathEnumerator _initializeIfNeeded]
+ -[CDPurgeablePathEnumerator _moveToNextValidAppCache]
+ -[CDPurgeablePathEnumerator appCaches]
+ -[CDPurgeablePathEnumerator currentAppCacheIndex]
+ -[CDPurgeablePathEnumerator currentCachePaths]
+ -[CDPurgeablePathEnumerator currentPathIndex]
+ -[CDPurgeablePathEnumerator hasBeenInitialized]
+ -[CDPurgeablePathEnumerator hasMore]
+ -[CDPurgeablePathEnumerator initWithVolume:urgency:]
+ -[CDPurgeablePathEnumerator nextBatch:error:]
+ -[CDPurgeablePathEnumerator reset]
+ -[CDPurgeablePathEnumerator restoreState:error:]
+ -[CDPurgeablePathEnumerator saveState]
+ -[CDPurgeablePathEnumerator setAppCaches:]
+ -[CDPurgeablePathEnumerator setCurrentAppCacheIndex:]
+ -[CDPurgeablePathEnumerator setCurrentCachePaths:]
+ -[CDPurgeablePathEnumerator setCurrentPathIndex:]
+ -[CDPurgeablePathEnumerator setHasBeenInitialized:]
+ -[CDPurgeablePathEnumerator setTelemetry:]
+ -[CDPurgeablePathEnumerator telemetry]
+ -[CDPurgeablePathEnumerator urgency]
+ -[CDPurgeablePathEnumerator volume]
+ -[CacheDeleteRemoteExtensionContext serviceCancelPurgeImmediate:]
+ -[CacheDeleteServiceListener serviceCancelPurgeImmediate:]
+ GCC_except_table104
+ GCC_except_table38
+ GCC_except_table4
+ GCC_except_table62
+ GCC_except_table82
+ GCC_except_table98
+ _CDGetPurgeSignpostLogHandle
+ _CFStringGetTypeID
+ _CacheDeleteCreatePurgeablePathEnumerator
+ _OBJC_CLASS_$_CDPurgeablePathEnumerator
+ _OBJC_IVAR_$_CDPurgeablePathEnumerator._appCaches
+ _OBJC_IVAR_$_CDPurgeablePathEnumerator._currentAppCacheIndex
+ _OBJC_IVAR_$_CDPurgeablePathEnumerator._currentCachePaths
+ _OBJC_IVAR_$_CDPurgeablePathEnumerator._currentPathIndex
+ _OBJC_IVAR_$_CDPurgeablePathEnumerator._hasBeenInitialized
+ _OBJC_IVAR_$_CDPurgeablePathEnumerator._telemetry
+ _OBJC_IVAR_$_CDPurgeablePathEnumerator._urgency
+ _OBJC_IVAR_$_CDPurgeablePathEnumerator._volume
+ _OBJC_METACLASS_$_CDPurgeablePathEnumerator
+ __OBJC_$_INSTANCE_METHODS_CDPurgeablePathEnumerator
+ __OBJC_$_INSTANCE_VARIABLES_CDPurgeablePathEnumerator
+ __OBJC_$_PROP_LIST_CDPurgeablePathEnumerator
+ __OBJC_CLASS_RO_$_CDPurgeablePathEnumerator
+ __OBJC_METACLASS_RO_$_CDPurgeablePathEnumerator
+ ___65-[CacheDeleteRemoteExtensionContext serviceCancelPurgeImmediate:]_block_invoke
+ ___65-[CacheDeleteRemoteExtensionContext serviceCancelPurgeImmediate:]_block_invoke_2
+ ___66-[CacheDeleteRemoteExtensionContext servicePurge:info:replyBlock:]_block_invoke.74
+ ___69-[CacheDeleteRemoteExtensionContext servicePeriodic:info:replyBlock:]_block_invoke.85
+ ___70-[CacheDeleteRemoteExtensionContext servicePurgeable:info:replyBlock:]_block_invoke.62
+ ___89+[AppCache sortedCachesForInstalledAppsOnVolume:urgency:calculate:bytesNeeded:telemetry:]_block_invoke
+ ___89+[AppCache sortedCachesForInstalledAppsOnVolume:urgency:calculate:bytesNeeded:telemetry:]_block_invoke.71
+ ___89+[AppCache sortedCachesForInstalledAppsOnVolume:urgency:calculate:bytesNeeded:telemetry:]_block_invoke_2
+ ___CDGetPurgeSignpostLogHandle_block_invoke
+ ___CacheDeleteCopyAvailableSpaceForVolume_block_invoke.123
+ ___CacheDeleteEnableReserveSpace_block_invoke.302
+ ___CacheDeletePauseReserveSpaceMonitoring_block_invoke.293
+ ___CacheDeleteRequestCacheableSpaceGuidance_block_invoke.205
+ ___CacheDeleteServiceRequest_block_invoke.236
+ ___CacheDeleteSetEntitledAndUnentitledReservation_block_invoke.311
+ ___CallBlockWithProxy_block_invoke.324
+ ____CacheDeleteCacheableForVolume_block_invoke.412
+ ____CacheDeleteEnumerateRemovedFiles_block_invoke.84
+ ____CacheDeleteEnumerateRemovedFiles_block_invoke.97
+ ____CacheDeletePurgeSpaceWithInfo_block_invoke.393
+ ____CacheDeleteRegisterLegacyCallbacks_block_invoke.367
+ ____CacheDeleteRegisterLegacyCallbacks_block_invoke.368
+ ____CacheDeleteRegister_block_invoke.330
+ ____CacheDeleteRegister_block_invoke.360
+ ____CacheDeleteRegister_block_invoke.363
+ ____CacheDeleteRegister_block_invoke_2.361
+ ____CacheDeleteSetCacheableForVolume_block_invoke.409
+ ___block_descriptor_32_e11_q24?0816l
+ ___block_descriptor_56_e8_32s40bs48r_e22_v16?0"NSDictionary"8lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e8_v16?0Q8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e37_v16?0"<CacheDeleteClientProtocol>"8ls32l8r56l8s40l8s48l8
+ ___block_descriptor_68_e8_32s40s48s56s_e28_B24?0"NSString"8"NSURL"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_77_e8_32s40s48s56s64s_e18_B16?0"AppCache"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_96_e8_32s40s48bs56bs64bs72bs80bs88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_literal_global.108
+ ___block_literal_global.110
+ ___block_literal_global.13
+ ___block_literal_global.141
+ ___block_literal_global.197
+ ___block_literal_global.227
+ ___block_literal_global.281
+ ___block_literal_global.283
+ ___block_literal_global.285
+ ___block_literal_global.295
+ ___block_literal_global.304
+ ___block_literal_global.313
+ ___block_literal_global.322
+ ___block_literal_global.324
+ ___block_literal_global.35
+ ___block_literal_global.355
+ ___block_literal_global.365
+ ___block_literal_global.39
+ ___block_literal_global.411
+ ___block_literal_global.51
+ ___block_literal_global.63
+ ___block_literal_global.65
+ ___block_literal_global.76
+ ___block_literal_global.82
+ ___block_literal_global.87
+ ___block_literal_global.96
+ ___parallel_delete_directories_block_invoke
+ __dispatch_queue_attr_concurrent
+ _closedir
+ _dispatch_apply
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_createItemDictionaryForPath:urgency:
+ _objc_msgSend$_getPathsForAppCache:
+ _objc_msgSend$_initializeIfNeeded
+ _objc_msgSend$_moveToNextValidAppCache
+ _objc_msgSend$appCacheWithRecords:identifier:groupIdentifiers:dataContainerURL:userManagedAssetsURL:personaUniqueString:isDataseparated:isPlaceholder:isPlugin:telemetry:
+ _objc_msgSend$appCaches
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$currentAppCacheIndex
+ _objc_msgSend$currentCachePaths
+ _objc_msgSend$currentPathIndex
+ _objc_msgSend$enumerateGroupCachesOnVolume:block:
+ _objc_msgSend$hasBeenInitialized
+ _objc_msgSend$hasMore
+ _objc_msgSend$initWithVolume:urgency:
+ _objc_msgSend$reset
+ _objc_msgSend$serviceCancelPurgeImmediate:
+ _objc_msgSend$setAppCaches:
+ _objc_msgSend$setCurrentAppCacheIndex:
+ _objc_msgSend$setCurrentCachePaths:
+ _objc_msgSend$setCurrentPathIndex:
+ _objc_msgSend$setHasBeenInitialized:
+ _objc_msgSend$setLastUsedTime:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$sortedCachesForInstalledAppsOnVolume:urgency:calculate:bytesNeeded:telemetry:
+ _objc_msgSend$substringToIndex:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_sync_enter
+ _objc_sync_exit
+ _opendir
+ _parallel_delete_directories
+ _readdir
+ _tokenStringForToken
- GCC_except_table57
- GCC_except_table77
- GCC_except_table93
- ___66-[CacheDeleteRemoteExtensionContext servicePurge:info:replyBlock:]_block_invoke.73
- ___69-[CacheDeleteRemoteExtensionContext servicePeriodic:info:replyBlock:]_block_invoke.82
- ___70-[CacheDeleteRemoteExtensionContext servicePurgeable:info:replyBlock:]_block_invoke.61
- ___CacheDeleteCopyAvailableSpaceForVolume_block_invoke.124
- ___CacheDeleteEnableReserveSpace_block_invoke.295
- ___CacheDeletePauseReserveSpaceMonitoring_block_invoke.286
- ___CacheDeleteRequestCacheableSpaceGuidance_block_invoke.201
- ___CacheDeleteServiceRequest_block_invoke.232
- ___CacheDeleteSetEntitledAndUnentitledReservation_block_invoke.304
- ___CallBlockWithProxy_block_invoke.313
- ____CacheDeleteCacheableForVolume_block_invoke.408
- ____CacheDeleteEnumerateRemovedFiles_block_invoke.85
- ____CacheDeleteEnumerateRemovedFiles_block_invoke.98
- ____CacheDeletePurgeSpaceWithInfo_block_invoke.389
- ____CacheDeleteRegisterLegacyCallbacks_block_invoke.360
- ____CacheDeleteRegisterLegacyCallbacks_block_invoke.361
- ____CacheDeleteRegister_block_invoke.323
- ____CacheDeleteRegister_block_invoke.346
- ____CacheDeleteRegister_block_invoke.356
- ____CacheDeleteRegister_block_invoke_2.354
- ____CacheDeleteSetCacheableForVolume_block_invoke.405
- ___block_descriptor_96_e8_32s40s48bs56bs64bs72bs80bs88bs_e5_v8?0ls32l8s48l8s56l8s64l8s72l8s80l8s88l8s40l8
- ___block_literal_global.130
- ___block_literal_global.193
- ___block_literal_global.223
- ___block_literal_global.274
- ___block_literal_global.276
- ___block_literal_global.278
- ___block_literal_global.288
- ___block_literal_global.290
- ___block_literal_global.306
- ___block_literal_global.315
- ___block_literal_global.317
- ___block_literal_global.348
- ___block_literal_global.358
- ___block_literal_global.36
- ___block_literal_global.407
- ___block_literal_global.52
- ___block_literal_global.64
- ___block_literal_global.81
- ___block_literal_global.93
- ___block_literal_global.97
- ___block_literal_global.99
- _objc_autorelease
CStrings:
+ "%@ CacheManagementAssetPurgeabilityScore within download completion grace period, not purgeable"
+ "%@ _CacheDeletePurgeSpaceWithInfo ENTRY, volume: %{public}@ %@"
+ "%@ _CacheDeletePurgeSpaceWithInfo purged: %{public}@ bytes from %{public}@"
+ "B24@?0@\"NSString\"8@\"NSURL\"16"
+ "CACHE_DELETE_CRITICAL_RELINQUISH_PURGE"
+ "CACHE_DELETE_FILE_TYPE"
+ "CACHE_DELETE_INODE"
+ "CACHE_DELETE_PATH"
+ "Critical relinquish itemized purgeable query: setting urgency=%d for framework cache lookup"
+ "Critical relinquish purgeable query: setting urgency=%d for framework cache lookup"
+ "Deletion complete: %.3f sec, %d dirs total"
+ "Failed to open directory: %s"
+ "Processing batch of %d directories"
+ "PurgeOperations"
+ "Skipping %@ - cache too small (%llu bytes < 1MB)"
+ "Skipping mountpoint at %s"
+ "[%@]"
+ "[no-token]"
+ "app_cache"
+ "cancelPurgeImmediate "
+ "clearDiscardedCaches parallel_delete_directories failed for %s"
+ "com.apple.Safari.WebApp"
+ "com.apple.cache_delete.parallel_delete"
+ "com.apple.cache_delete.purge"
+ "parallel_delete_directories: processing subdirectories in %s (batch size: %d)"
+ "q24@?0@8@16"
+ "serviceCancelPurgeImmediate"
+ "serviceCancelPurgeImmediate end"
+ "\xb1"
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"CDRecentInfo\""
- "@\"CacheDeleteServiceInfo\""
- "@\"CacheDeleteVolume\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSDictionary\"20@0:8i16"
- "@\"NSDictionary\"28@0:8@\"CacheDeleteVolume\"16i24"
- "@\"NSDictionary\"32@0:8@\"CacheDeleteVolume\"16i24B28"
- "@\"NSDictionary\"40@0:8@\"NSArray\"16i24B28@\"NSString\"32"
- "@\"NSExtensionContext\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableDictionary\"32@0:8@\"NSMutableDictionary\"16@\"NSDictionary\"24"
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSXPCListener\""
- "@\"NSXPCListenerEndpoint\""
- "@\"Protocol\""
- "@\"TestTelemetry\""
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{?=IdddddiBqqqqq[0c]}16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8i16B20"
- "@24@0:8r*16"
- "@28@0:8@16i24"
- "@28@0:8i16@20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16i24B28"
- "@32@0:8@?16@24"
- "@32@0:8r*16Q24"
- "@36@0:8@16@24B32"
- "@40@0:8:16@24@32"
- "@40@0:8@16i24B28@32"
- "@52@0:8@16@24@32@40B48"
- "@52@0:8@16i24d28@36@44"
- "@60@0:8@16@24@32@40@48i56"
- "@84@0:8@16@24@32@40@48@56B64B68B72@76"
- "@92@0:8@16@24@32@40@48@56@64B72B76B80@84"
- "@?"
- "@?16@0:8"
- "App"
- "AppCache"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B28@0:8@16i24"
- "B28@0:8d16i24"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "B32@0:8q16@24"
- "B36@0:8@16@24i32"
- "B56@0:8@16Q24Q32Q40Q48"
- "B56@0:8@16i24d28@36B44@48"
- "B64@0:8@16@24i32d36@44B52@56"
- "B72@0:8@16@24@32i40d44@52B60@64"
- "CDPurgeableResultCache"
- "CDRecentInfo"
- "CDRecentServiceInfo"
- "CDRecentServiceInfo:atUrgency:withTimestamp:nonPurgeableAmount:info:"
- "CDRecentVolumeInfo"
- "CDRecentVolumeInfo:"
- "CDRemoveEventsConsumer"
- "CacheDeleteAppInFocus"
- "CacheDeleteClientProtocol"
- "CacheDeleteHostExtensionContext"
- "CacheDeleteHostProtocol"
- "CacheDeleteListener"
- "CacheDeletePrivateClientProtocol"
- "CacheDeletePublicClientProtocol"
- "CacheDeleteRemoteExtensionContext"
- "CacheDeleteServiceInfo"
- "CacheDeleteServiceListener"
- "CacheDeleteServiceProtocol"
- "CacheDeleteVolume"
- "CacheManagementAdditions"
- "CacheManagementAsset"
- "FSEventsUUID"
- "I"
- "I16@0:8"
- "InFocus"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "NSXPCListenerDelegate"
- "OperationState"
- "Q"
- "Q16@0:8"
- "Q20@0:8B16"
- "Q24@0:8B16B20"
- "Q28@0:8B16B20B24"
- "RBSAssertionObserving"
- "RBSTerminationAssertionObserving"
- "T#,R"
- "T@\"CDRecentInfo\",&,N,V_recentPurgeableResults"
- "T@\"CacheDeleteServiceInfo\",R,N,V_serviceInfo"
- "T@\"CacheDeleteVolume\",&,N,V_cdVolume"
- "T@\"CacheDeleteVolume\",R,N,V_cdVol"
- "T@\"NSData\",&,N"
- "T@\"NSData\",&,N,V_metadata"
- "T@\"NSDate\",&,N,V_lastUsed"
- "T@\"NSDate\",&,V_timestamp"
- "T@\"NSDictionary\",&,N,V_serviceInfo"
- "T@\"NSDictionary\",&,N,V_thresholds"
- "T@\"NSDictionary\",R,N,V_thresholds"
- "T@\"NSExtensionContext\",R,N,V_extensionContext"
- "T@\"NSMutableArray\",&,N,V_removeFailures"
- "T@\"NSMutableArray\",&,N,V_terminationFailures"
- "T@\"NSMutableDictionary\",&,N,V_diagnostics"
- "T@\"NSMutableDictionary\",&,N,V_services"
- "T@\"NSMutableDictionary\",&,N,V_volumes"
- "T@\"NSMutableSet\",&,N,V_bundleIdentifiers"
- "T@\"NSMutableSet\",&,N,V_groupContainerIdentifiers"
- "T@\"NSMutableSet\",&,N,V_invalidVolumes"
- "T@\"NSMutableSet\",&,N,V_pushingServices"
- "T@\"NSMutableSet\",&,N,V_requiredEntitlements"
- "T@\"NSNumber\",&,N,V_lastKnownCacheSize"
- "T@\"NSNumber\",&,N,V_lastKnownFreespace"
- "T@\"NSNumber\",&,N,V_lastKnownGroupCacheSize"
- "T@\"NSNumber\",&,N,V_lastKnownTmpSize"
- "T@\"NSNumber\",&,N,V_version"
- "T@\"NSNumber\",&,V_freespace"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_consumer_q"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSObject<OS_dispatch_queue>\",R,V_q"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_completionSem"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_sem"
- "T@\"NSString\",&,N,V_bsdDisk"
- "T@\"NSString\",&,N,V_contentType"
- "T@\"NSString\",&,N,V_displayName"
- "T@\"NSString\",&,N,V_identifier"
- "T@\"NSString\",&,N,V_relativePath"
- "T@\"NSString\",&,N,V_serviceName"
- "T@\"NSString\",&,N,V_volume"
- "T@\"NSString\",&,V_absolutePath"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_bsdName"
- "T@\"NSString\",R,N,V_fsType"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSString\",R,N,V_mountPoint"
- "T@\"NSString\",R,N,V_personaUniqueString"
- "T@\"NSURL\",R,N,V_dataContainerURL"
- "T@\"NSURL\",R,N,V_userManagedAssetsURL"
- "T@\"NSXPCListener\",&,N,V_listener"
- "T@\"NSXPCListenerEndpoint\",R,V_endpoint"
- "T@\"Protocol\",&,N,V_protocol"
- "T@\"TestTelemetry\",&,N,V_telemetry"
- "T@,&,N,V_xObj"
- "T@?,C,N,V_callback"
- "T@?,C,N,V_cancel"
- "T@?,C,N,V_consumer"
- "T@?,C,N,V_notify"
- "T@?,C,N,V_periodic"
- "T@?,C,N,V_purge"
- "T@?,C,N,V_purgeable"
- "TB,N,V_isResumed"
- "TB,R"
- "TB,R,V_anonymous"
- "TB,R,V_isDataseparated"
- "TB,R,V_isPlaceholder"
- "TB,R,V_isPlugin"
- "TB,R,V_isRoot"
- "TB,R,V_legacyCallbacks"
- "TB,V_doNotQuery"
- "TB,V_hasSnapshot"
- "TB,V_historyDone"
- "TB,V_operationCancelled"
- "TI,R,V_assetVersion"
- "TI,R,V_block_size"
- "TQ,R"
- "TQ,R,V_initialFreespace"
- "TQ,V_files_deleted"
- "TQ,V_reserve"
- "TQ,V_since"
- "T^{__FSEventStream=},V_stream"
- "Td,V_consumed_date"
- "Td,V_download_completion_date"
- "Td,V_download_start_date"
- "Td,V_expiration_date"
- "Td,V_last_viewed_date"
- "Td,V_remove_threshold"
- "Td,V_termination_threshold"
- "Td,V_timestamp"
- "TestTelemetry"
- "Ti,R,V_dev"
- "Ti,V_operationRefcount"
- "Ti,V_priority"
- "Tq,N,V_volumeState"
- "Tq,R,D,N"
- "T{fsid=[2i]},V_fsid"
- "UIBackgroundModes"
- "URLByAppendingPathComponent:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{?=IdddddiBqqqqq[0c]}24@0:8^q16"
- "^{_NSZone=}16@0:8"
- "^{__FSEventStream=}"
- "^{__FSEventStream=}16@0:8"
- "_CacheDeletePurgeSpaceWithInfo ENTRY, volume: %{public}@ %@"
- "_CacheDeletePurgeSpaceWithInfo purged: %{public}@ bytes from %{public}@"
- "_absolutePath"
- "_anonymous"
- "_assetVersion"
- "_block_size"
- "_bsdDisk"
- "_bsdName"
- "_bundleIdentifiers"
- "_callback"
- "_cancel"
- "_cdVol"
- "_cdVolume"
- "_completionSem"
- "_consumed_date"
- "_consumer"
- "_consumer_q"
- "_contentType"
- "_createNewRecentVolumeInfo"
- "_createNewRecentVolumeInfoWithName:"
- "_dataContainerURL"
- "_dev"
- "_diagnostics"
- "_displayName"
- "_doNotQuery"
- "_download_completion_date"
- "_download_start_date"
- "_endpoint"
- "_expiration_date"
- "_extensionAuxiliaryHostProtocol"
- "_extensionAuxiliaryVendorProtocol"
- "_extensionContext"
- "_files_deleted"
- "_freespace"
- "_fsType"
- "_fsid"
- "_groupContainerIdentifiers"
- "_hasSnapshot"
- "_historyDone"
- "_identifier"
- "_initialFreespace"
- "_invalidVolumes"
- "_isDataseparated"
- "_isPlaceholder"
- "_isPlugin"
- "_isResumed"
- "_isRoot"
- "_lastKnownCacheSize"
- "_lastKnownFreespace"
- "_lastKnownGroupCacheSize"
- "_lastKnownTmpSize"
- "_lastUsed"
- "_last_viewed_date"
- "_legacyCallbacks"
- "_listener"
- "_metadata"
- "_mountPoint"
- "_notify"
- "_operationCancelled"
- "_operationRefcount"
- "_periodic"
- "_personaUniqueString"
- "_priority"
- "_protocol"
- "_purge"
- "_purgeable"
- "_pushingServices"
- "_q"
- "_queue"
- "_recentInfoAtUrgency:validateResults:"
- "_recentInfoForVolume:atUrgency:validateResults:"
- "_recentPurgeableResults"
- "_recentPurgeableTotals:validateResults:"
- "_relativePath"
- "_removeFailures"
- "_remove_threshold"
- "_requiredEntitlements"
- "_reserve"
- "_reserveForVolume"
- "_sem"
- "_serviceInfo"
- "_serviceName"
- "_services"
- "_since"
- "_stream"
- "_telemetry"
- "_terminationFailures"
- "_termination_threshold"
- "_thresholds"
- "_timestamp"
- "_userManagedAssetsURL"
- "_validateWithSharedCacheDeleteForService:"
- "_version"
- "_volume"
- "_volumeState"
- "_volumes"
- "_xObj"
- "_xpcConnection"
- "absolutePath"
- "absorbRecentInfo:"
- "acquireWithError:"
- "addBundleRecord:"
- "addBundleRecords:"
- "addDeletes:"
- "addEntriesFromDictionary:"
- "addIndex:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:"
- "addPointer:"
- "addRemoveFailure:"
- "addRequiredEntitlement:"
- "addTerminationFailure:"
- "allKeys"
- "allObjects"
- "allValues"
- "allocWithZone:"
- "amountAtUrgency:checkTimestamp:"
- "amountIsRational:freespace:effective_size:used:size:"
- "amountPurged"
- "anonymous"
- "anonymousListener"
- "appCacheWithRecords:identifier:groupIdentifiers:dataContainerURL:userManagedAssetsURL:personaUniqueString:cacheDeleteVolume:isDataseparated:isPlaceholder:isPlugin:telemetry:"
- "appCacheWithRecords:identifier:groupIdentifiers:dataContainerURL:userManagedAssetsURL:personaUniqueString:isDataseparated:isPlaceholder:isPlugin:telemetry:"
- "appendBytes:length:"
- "array"
- "arrayWithObject:"
- "arrayWithObjects:"
- "arrayWithObjects:count:"
- "assertion:didInvalidateWithError:"
- "assertionTargetProcessDidExit:"
- "assertionWillInvalidate:"
- "assetFromData:"
- "assetFromFile:withIdentifier:"
- "assetFromPath:withIdentifier:"
- "assetFromPath:withIdentifier:createIfAbsent:"
- "assetVersion"
- "assetWithRelativePath:identifier:expirationDate:contentType:metadata:priority:"
- "auditToken"
- "autorelease"
- "begin"
- "block_size"
- "boolValue"
- "bsdDisk"
- "bsdDiskForVolume:"
- "bsdName"
- "bundleID"
- "bundleIdentifier"
- "bundleIdentifiers"
- "bundleRecordWithBundleIdentifier:allowPlaceholder:error:"
- "bytes"
- "cStringUsingEncoding:"
- "cacheDeleteServiceListener:options:"
- "cachePath"
- "caches:purge:"
- "callback"
- "callback:"
- "cancel"
- "cancelled"
- "cdVol"
- "cdVolume"
- "class"
- "clearCaches:"
- "clientCancelPurge:"
- "clientCheckin:endpoint:info:reply:"
- "clientGetPendingStorageThreshold:replyBlock:"
- "clientGetState:replyBlock:"
- "clientPerformOperation:replyBlock:"
- "clientPerformServiceRequest:replyBlock:"
- "clientPurge:replyBlock:"
- "clientRegisterLowDiskFailure:failureType:isRoot:"
- "clientSetState:key:"
- "clientUnifiedPurgeableSpace:queryType:replyBlock:"
- "clientUpdatePurgeable:"
- "code"
- "commit"
- "compare:"
- "completeRequestReturningItems:completionHandler:"
- "completionSem"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "conformsToProtocol:"
- "consumeStream:forVolume:"
- "consumedDate"
- "consumed_date"
- "consumer"
- "consumer_q"
- "containingBundleRecord"
- "containsIndex:"
- "containsObject:"
- "containsPath:"
- "containsString:"
- "containsValueForKey:"
- "contentType"
- "copy"
- "copyInvalidsAtUrgency:currentlyPushing:"
- "copyInvalidsForVolume:atUrgency:"
- "copyPushingServices"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createFlattenedAsset:"
- "createVolumeWithMountPoint:"
- "createVolumeWithPath:"
- "currentConnection"
- "currentStateMatchingDescriptor:"
- "d"
- "d16@0:8"
- "dataContainerURL"
- "dataWithBytes:length:"
- "dataWithPropertyList:format:options:error:"
- "date"
- "dateByAddingTimeInterval:"
- "dateWithTimeIntervalSinceNow:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultManager"
- "deletes"
- "description"
- "descriptor"
- "dev"
- "diagnostics"
- "dictionary"
- "dictionaryByMerging:with:"
- "dictionaryWithCapacity:"
- "dictionaryWithObjects:forKeys:count:"
- "displayName"
- "distantFuture"
- "doNotQuery"
- "doubleValue"
- "downloadCompletionDate"
- "downloadStartDate"
- "download_completion_date"
- "download_start_date"
- "effective_size"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "end"
- "endpoint"
- "enumerateAppCachesOnVolume:options:telemetry:block:"
- "enumerateGroupCachesOnVolume:block:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateMatchesInString:options:range:usingBlock:"
- "enumerateWithContainerQuery:container_class:options:telemetry:block:"
- "error"
- "errorWithDomain:code:userInfo:"
- "eventBody"
- "expirationDate"
- "expiration_date"
- "extensionContext"
- "fetchAllowedClassesSet"
- "fetchVolumeWithPath:"
- "fileSystemRepresentation"
- "fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:"
- "fileURLWithPath:isDirectory:"
- "fileURLWithPathComponents:"
- "files_deleted"
- "firstMatchInString:options:range:"
- "floatValue"
- "freespace"
- "freespaceIsStale:"
- "fsType"
- "fsid"
- "fullPath"
- "getCString:maxLength:encoding:"
- "getUUIDBytes:"
- "groupContainerIdentifiers"
- "handleForPredicate:error:"
- "hasInvalids"
- "hasPrefix:"
- "hasSnapshot"
- "hasSnapshotForVolume:"
- "hash"
- "i16@0:8"
- "i20@0:8i16"
- "identifier"
- "indexOfObject:"
- "infoDictionary"
- "init"
- "initEmpty"
- "initWithAmount:atUrgency:withTimestamp:nonPurgeableAmount:info:"
- "initWithBundleRecords:identifier:groupIdentifiers:dataContainerURL:userManagedAssetsURL:personaUniqueString:cacheDeleteVolume:isDataseparated:isPlaceholder:isPlugin:telemetry:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithConsumer:identifier:"
- "initWithDictionary:"
- "initWithDomain:code:userInfo:"
- "initWithExplanation:"
- "initWithExtensionContext:"
- "initWithFlattenedAsset:"
- "initWithFormat:"
- "initWithInfo:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "initWithName:listener:protocol:exportedObj:isExtension:"
- "initWithName:options:"
- "initWithOptions:"
- "initWithPath:"
- "initWithPredicate:context:"
- "initWithRecentInfo:"
- "initWithRelativePath:identifier:expirationDate:contentType:metadata:priority:"
- "initWithServices:volumeName:"
- "initWithStartDate:endDate:maxEvents:lastN:reversed:"
- "initWithUUIDBytes:"
- "initWithUUIDString:"
- "initWithVolume:"
- "initWithVolumeInfo:"
- "initWithVolumes:"
- "initialFreespace"
- "intValue"
- "integerValue"
- "interfaceWithProtocol:"
- "invalidVolumes"
- "invalidate"
- "invalidateAllForgettingPushers:"
- "invalidateForVolume:"
- "isDataSeparatedPersona"
- "isDataseparated"
- "isEmpty"
- "isEqual:"
- "isEqualTo:"
- "isEqualToNumber:"
- "isEqualToString:"
- "isInvalidForVolume:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPlaceholder"
- "isPlugin"
- "isProxy"
- "isResumed"
- "isRoot"
- "isStale"
- "isStaleForVolume:"
- "isSystemPlaceholder"
- "keepUpToDate:"
- "lastKnownCacheSize"
- "lastKnownFreespace"
- "lastKnownGroupCacheSize"
- "lastKnownTmpSize"
- "lastObject"
- "lastPathComponent"
- "lastUsed"
- "lastViewedDate"
- "last_viewed_date"
- "launchReason"
- "legacyCallbacks"
- "length"
- "lengthOfBytesUsingEncoding:"
- "listAllPersonaWithAttributes"
- "listener"
- "listener:shouldAcceptNewConnection:"
- "log"
- "longLongValue"
- "maximumLengthOfBytesUsingEncoding:"
- "mayContainPurgeableAmount:forService:"
- "metadata"
- "mountPoint"
- "mountPointForUUID:"
- "moveCacheAside:"
- "mutableCopy"
- "name"
- "nonPurgeableAmount"
- "notify"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithLongLong:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKey:ofClass:"
- "objectForKeyedSubscript:"
- "operationCancelled"
- "operationRefcount"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "periodic"
- "personaUniqueString"
- "pointerAtIndex:"
- "predicateMatchingBundleIdentifier:"
- "priority"
- "processExists"
- "propertyListWithData:options:format:error:"
- "protocol"
- "publisherWithOptions:"
- "purge"
- "purgeabilityScoreAtUrgency:"
- "purgeable"
- "pushingServices"
- "q"
- "q16@0:8"
- "q20@0:8B16"
- "q24@0:8@\"CacheDeleteVolume\"16"
- "q24@0:8@16"
- "queryAppContainers:replyBlock:"
- "queue"
- "range"
- "rangeAtIndex:"
- "rangeOfString:"
- "recentInfoAtUrgency:"
- "recentInfoForVolume:atUrgency:"
- "recentInfoForVolume:atUrgency:validateResults:"
- "recentInfoForVolumes:"
- "recentInfoForVolumes:atUrgency:"
- "recentInfoForVolumes:atUrgency:validateResults:targetVolume:"
- "recentPurgeableResults"
- "recentPurgeableTotals:"
- "recentStateForVolume:"
- "recentinfo"
- "regularExpressionWithPattern:options:error:"
- "relativePath"
- "release"
- "removeAllObjects"
- "removeFailures"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removePointerAtIndex:"
- "removeServiceInfo:"
- "removeServiceInfo:forVolume:"
- "remove_threshold"
- "requiredEntitlements"
- "reserve"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "rootVolume"
- "self"
- "sem"
- "serialize"
- "serviceCallback:replyBlock:"
- "serviceCancelPurge:"
- "serviceInfo"
- "serviceInfoWithExtensionContext:"
- "serviceName"
- "serviceNotify:replyBlock:"
- "servicePeriodic:info:replyBlock:"
- "servicePing:"
- "servicePurge:info:replyBlock:"
- "servicePurgeable:info:replyBlock:"
- "services"
- "servicesForVolume:"
- "set"
- "setAbsolutePath:"
- "setBsdDisk:"
- "setBundleIdentifiers:"
- "setCallback:"
- "setCancel:"
- "setCdVolume:"
- "setCompletionSem:"
- "setConsumedDate:"
- "setConsumed_date:"
- "setConsumer:"
- "setConsumer_q:"
- "setContentType:"
- "setDelegate:"
- "setDiagnostics:"
- "setDisplayName:"
- "setDoNotQuery:"
- "setDownloadCompletionDate:"
- "setDownloadStartDate:"
- "setDownload_completion_date:"
- "setDownload_start_date:"
- "setExceptionCode:"
- "setExpirationDate:"
- "setExpiration_date:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFiles_deleted:"
- "setFreespace:"
- "setFsid:"
- "setGroupContainerIdentifiers:"
- "setHasSnapshot:"
- "setHistoryDone:"
- "setIdentifier:"
- "setInterruptionHandler:"
- "setInvalidVolumes:"
- "setInvalidationHandler:"
- "setIsResumed:"
- "setLastKnownCacheSize:"
- "setLastKnownFreespace:"
- "setLastKnownGroupCacheSize:"
- "setLastKnownTmpSize:"
- "setLastUsed:"
- "setLastUsedTime:"
- "setLastViewedDate:"
- "setLast_viewed_date:"
- "setListener:"
- "setMaximumTerminationResistance:"
- "setMetadata:"
- "setNotify:"
- "setNotifyCallback:"
- "setObject:atIndexedSubscript:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOperationCancelled:"
- "setOperationRefcount:"
- "setPeriodic:"
- "setPriority:"
- "setProtocol:"
- "setPurge:"
- "setPurgeable:"
- "setPurgeable:purge:cancel:periodic:notify:callback:entitlements:"
- "setPushingServices:"
- "setQueue:"
- "setRecentPurgeableResults:"
- "setRelativePath:"
- "setRemoteObjectInterface:"
- "setRemoveFailures:"
- "setRemove_threshold:"
- "setRequiredEntitlements:"
- "setReserve:"
- "setSem:"
- "setServiceInfo:"
- "setServiceName:"
- "setServices:"
- "setSince:"
- "setStream:"
- "setTelemetry:"
- "setTerminationFailures:"
- "setTermination_threshold:"
- "setThresholds:"
- "setThumbnailData:"
- "setTimestamp:"
- "setValues:"
- "setVersion:"
- "setVolume:"
- "setVolumeState:"
- "setVolumes:"
- "setWithArray:"
- "setWithObject:"
- "setWithObjects:"
- "setXObj:"
- "sharedManager"
- "sharedPurgeableResultsCache"
- "since"
- "sinkWithCompletion:receiveInput:"
- "size"
- "sizeCached:"
- "starting"
- "state"
- "stateForPath:"
- "stream"
- "stringByAppendingPathComponent:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringByStandardizingPath"
- "stringWithCString:encoding:"
- "stringWithFileSystemRepresentation:"
- "stringWithFileSystemRepresentation:length:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "subscribeToAppInFocusStreamBeginning:callback:"
- "substringFromIndex:"
- "substringWithRange:"
- "superclass"
- "supportsSecureCoding"
- "suspend"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "telemetry"
- "termAssertionObserver"
- "terminationFailures"
- "terminationResistance"
- "termination_threshold"
- "testTelemetryWithInfo:"
- "three_days_ago"
- "thresholds"
- "thresholdsForVolume:"
- "thumbnailData"
- "timeIntervalSinceDate:"
- "timeIntervalSinceReferenceDate"
- "tmp:purge:all:"
- "tmpPath"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "updateAmount:atUrgency:withTimestamp:nonPurgeableAmount:deductFromCurrentAmount:info:"
- "updateInfo:"
- "updateRecentState:forVolume:"
- "updateRecentVolumeInfo:"
- "updateServiceInfoAmount:forService:atUrgency:withTimestamp:nonPurgeableAmount:deductFromCurrentAmount:info:"
- "updateServiceInfoAmount:forService:onVolume:atUrgency:withTimestamp:nonPurgeableAmount:deductFromCurrentAmount:info:"
- "urgency"
- "used"
- "userManagedAssetsURL"
- "userPersonaUniqueString"
- "uuid"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"RBSAssertion\"16"
- "v24@0:8@\"RBSTerminationAssertion\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8Q16"
- "v24@0:8^{__FSEventStream=}16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v24@0:8{fsid=[2i]}16"
- "v32@0:8@\"NSDictionary\"16@\"NSString\"24"
- "v32@0:8@\"NSDictionary\"16@?<v@?>24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@\"NSString\"16@?<v@?@>24"
- "v32@0:8@\"NSString\"16i24B28"
- "v32@0:8@\"RBSAssertion\"16@\"NSError\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16i24B28"
- "v32@0:8^{__FSEventStream=}16@24"
- "v36@0:8@\"NSDictionary\"16i24@?<v@?@\"CDRecentInfo\">28"
- "v36@0:8@16i24@?28"
- "v36@0:8i16@\"NSDictionary\"20@?<v@?@\"NSDictionary\">28"
- "v36@0:8i16@20@?28"
- "v44@0:8@16i24@28@?36"
- "v48@0:8@\"NSString\"16@\"NSXPCListenerEndpoint\"24@\"NSDictionary\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v52@0:8@16Q24i32@36@?44"
- "v72@0:8@?16@?24@?32@?40@?48@?56@64"
- "validate"
- "validate:atUrgency:"
- "validateForVolume:andService:atUrgency:"
- "validateServiceInfo:atUrgency:"
- "validateVolumeAtPath:"
- "valueForEntitlement:"
- "version"
- "volume"
- "volumeServices"
- "volumeState"
- "volumeWithMountpoint:"
- "volumeWithPath:"
- "volumeWithUUID:"
- "volumes"
- "xObj"
- "zone"
- "{?=\"urgencies\"[4{?=\"timestamp\"d\"amount\"Q}]\"non_purgeable_amount\"Q\"data\"[0C]}"
- "{fsid=\"val\"[2i]}"
- "{fsid=[2i]}16@0:8"
- "\x91"

```
