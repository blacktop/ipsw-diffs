## SyncedDefaults

> `/System/Library/PrivateFrameworks/SyncedDefaults.framework/Versions/A/SyncedDefaults`

```diff

-2230.13.0.0.0
-  __TEXT.__text: 0xf54c
-  __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0x8f0
-  __TEXT.__const: 0x1d6
-  __TEXT.__cstring: 0xd32
-  __TEXT.__oslogstring: 0x1b91
-  __TEXT.__gcc_except_tab: 0x898
-  __TEXT.__swift5_typeref: 0x36
+2250.21.0.0.0
+  __TEXT.__text: 0x11f18
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__objc_methlist: 0xb68
+  __TEXT.__const: 0x1fa
+  __TEXT.__cstring: 0xe62
+  __TEXT.__oslogstring: 0x1eb1
+  __TEXT.__gcc_except_tab: 0x964
+  __TEXT.__swift5_typeref: 0x46
+  __TEXT.__swift_as_entry: 0x4
+  __TEXT.__swift_as_ret: 0x4
   __TEXT.__constg_swiftt: 0x44
   __TEXT.__swift5_reflstr: 0x5e
   __TEXT.__swift5_fieldmd: 0x68
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x550
+  __TEXT.__unwind_info: 0x660
   __TEXT.__eh_frame: 0xd8
-  __TEXT.__objc_classname: 0xe1
-  __TEXT.__objc_methname: 0x1b81
-  __TEXT.__objc_methtype: 0x6d5
-  __TEXT.__objc_stubs: 0x1540
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x158
+  __TEXT.__objc_classname: 0xfc
+  __TEXT.__objc_methname: 0x214b
+  __TEXT.__objc_methtype: 0x86d
+  __TEXT.__objc_stubs: 0x18e0
+  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__const: 0x180
   __DATA_CONST.__objc_classlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d8
+  __DATA_CONST.__objc_selrefs: 0x818
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x380
-  __AUTH_CONST.__const: 0x910
-  __AUTH_CONST.__cfstring: 0xa00
-  __AUTH_CONST.__objc_const: 0xb60
+  __AUTH_CONST.__auth_got: 0x388
+  __AUTH_CONST.__const: 0xc48
+  __AUTH_CONST.__cfstring: 0xb20
+  __AUTH_CONST.__objc_const: 0xa98
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x54
-  __DATA.__data: 0x238
+  __DATA.__objc_ivar: 0x64
+  __DATA.__data: 0x298
   __DATA.__bss: 0x320
-  __DATA.__common: 0x40
+  __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 56A5A943-D5D3-39BA-951B-6A82D6A92829
-  Functions: 453
-  Symbols:   986
-  CStrings:  661
+  UUID: E7E46FA3-4765-3CE4-B254-486A915ED7B3
+  Functions: 539
+  Symbols:   1146
+  CStrings:  764
 
Symbols:
+ +[SYDClientToDaemonConnection clientProtocolInterface].cold.1
+ +[SYDClientToDaemonConnection connectionUsingTestServer:]
+ +[SYDClientToDaemonConnection connection]
+ +[SYDClientToDaemonConnection daemonProtocolInterface].cold.1
+ +[SYDClientToDaemonConnection disgustingUglyHardcodedKnownStoreIdentifierForApplicationIdentifier:].cold.1
+ +[SYDClientToDaemonConnection removeUnitTestSyncManagers]
+ +[SYDClientToDaemonConnection setUseTestServerByDefault:]
+ +[SYDClientToDaemonConnection useTestServerByDefault]
+ -[SYDClientToDaemonConnection ___We_looked_everywhere_but_we_cant_find_your_store_identifier___].cold.1
+ -[SYDClientToDaemonConnection ___You_exceeded_the_quota_limit_for_NSUbiquitousKeyValueStore___].cold.1
+ -[SYDClientToDaemonConnection ___You_think_you_can_just_XPC_into_any_process_all_willy_nilly_well_think_again___].cold.1
+ -[SYDClientToDaemonConnection ___Your_store_identifier_is_empty___].cold.1
+ -[SYDClientToDaemonConnection _cachedObjectForKey:]
+ -[SYDClientToDaemonConnection _daemonWithOptions:retries:errorHandler:daemonHandler:]
+ -[SYDClientToDaemonConnection _synchronize:]
+ -[SYDClientToDaemonConnection containerIDFromDaemonWithError:]
+ -[SYDClientToDaemonConnection daemonWithOptions:errorHandler:daemonHandler:]
+ -[SYDClientToDaemonConnection delegate]
+ -[SYDClientToDaemonConnection deleteDataFromDisk]
+ -[SYDClientToDaemonConnection deleteDataFromDisk].cold.1
+ -[SYDClientToDaemonConnection deleteDataFromDisk].cold.2
+ -[SYDClientToDaemonConnection exit:]
+ -[SYDClientToDaemonConnection initWithStoreConfiguration:].cold.1
+ -[SYDClientToDaemonConnection isUIFrameworkLinkedInDaemon]
+ -[SYDClientToDaemonConnection personaUniqueString]
+ -[SYDClientToDaemonConnection postFakeAccountChangeNotificationWithCompletionHandler:]
+ -[SYDClientToDaemonConnection postFakeSyncManagerChangeNotificationWithCompletionHandler:]
+ -[SYDClientToDaemonConnection setDelegate:]
+ -[SYDClientToDaemonConnection setFakeError:forNextCloudKitRequestOfClassName:inStoreWithConfiguration:]
+ -[SYDClientToDaemonConnection setUseTestServer:]
+ -[SYDClientToDaemonConnection useTestServer]
+ -[SYDRemotePreferencesSource initWithApplicationID:storeID:shared:additionalSource:containerPath:storeType:].cold.1
+ -[SYDStoreConfiguration entitlementOverrides]
+ -[SYDStoreConfiguration initWithStoreID:].cold.1
+ -[SYDStoreConfiguration setEntitlementOverrides:]
+ -[SYDStoreID containerID]
+ -[SYDStoreID initWithIdentifier:type:].cold.1
+ -[SYDStoreID setContainerID:]
+ GCC_except_table109
+ GCC_except_table112
+ GCC_except_table119
+ GCC_except_table129
+ GCC_except_table133
+ GCC_except_table139
+ GCC_except_table141
+ GCC_except_table142
+ GCC_except_table163
+ GCC_except_table172
+ GCC_except_table177
+ GCC_except_table180
+ GCC_except_table183
+ GCC_except_table186
+ GCC_except_table189
+ GCC_except_table193
+ GCC_except_table199
+ GCC_except_table211
+ GCC_except_table213
+ GCC_except_table215
+ GCC_except_table276
+ GCC_except_table287
+ GCC_except_table36
+ GCC_except_table44
+ GCC_except_table62
+ GCC_except_table70
+ GCC_except_table74
+ GCC_except_table81
+ GCC_except_table91
+ OBJC_IVAR_$_SYDClientToDaemonConnection._delegate
+ OBJC_IVAR_$_SYDClientToDaemonConnection._useTestServer
+ OBJC_IVAR_$_SYDStoreConfiguration._entitlementOverrides
+ OBJC_IVAR_$_SYDStoreID._containerID
+ SYDErrorUserInfoClasses.cold.1
+ SYDGetAccessorSignpostsLog.cold.1
+ SYDGetAccountsLog.cold.1
+ SYDGetAnalyticsLog.cold.1
+ SYDGetCloudKitLog.cold.1
+ SYDGetConnectionLog.cold.1
+ SYDGetCoreDataLog.cold.1
+ SYDGetMigrationLog.cold.1
+ SYDGetMiscLog.cold.1
+ SYDGetSyncSignpostsLog.cold.1
+ SYDGetTCCLog.cold.1
+ _CKErrorUserInfoClasses
+ _OBJC_CLASS_$_CKContainerID
+ _OUTLINED_FUNCTION_16
+ _SYDContainerID
+ __103-[SYDClientToDaemonConnection setFakeError:forNextCloudKitRequestOfClassName:inStoreWithConfiguration:]_block_invoke.280
+ __103-[SYDClientToDaemonConnection setFakeError:forNextCloudKitRequestOfClassName:inStoreWithConfiguration:]_block_invoke.cold.1
+ __105+[SYDClientToDaemonConnection synchronizeStoresWithIdentifiers:type:testConfiguration:completionHandler:]_block_invoke.214
+ __105+[SYDClientToDaemonConnection synchronizeStoresWithIdentifiers:type:testConfiguration:completionHandler:]_block_invoke.214.cold.1
+ __105+[SYDClientToDaemonConnection synchronizeStoresWithIdentifiers:type:testConfiguration:completionHandler:]_block_invoke.215
+ __105+[SYDClientToDaemonConnection synchronizeStoresWithIdentifiers:type:testConfiguration:completionHandler:]_block_invoke.216
+ __44-[SYDClientToDaemonConnection _synchronize:]_block_invoke.194
+ __44-[SYDClientToDaemonConnection _synchronize:]_block_invoke.cold.1
+ __44-[SYDClientToDaemonConnection _synchronize:]_block_invoke.cold.2
+ __44-[SYDClientToDaemonConnection _synchronize:]_block_invoke.cold.3
+ __44-[SYDClientToDaemonConnection xpcConnection]_block_invoke.390
+ __47+[SYDClientToDaemonConnection newXPCConnection]_block_invoke.236
+ __47+[SYDClientToDaemonConnection newXPCConnection]_block_invoke.236.cold.1
+ __50-[SYDClientToDaemonConnection objectForKey:error:]_block_invoke.152
+ __50-[SYDClientToDaemonConnection objectForKey:error:]_block_invoke.152.cold.1
+ __50-[SYDClientToDaemonConnection objectForKey:error:]_block_invoke.152.cold.2
+ __50-[SYDClientToDaemonConnection objectForKey:error:]_block_invoke.160
+ __50-[SYDClientToDaemonConnection objectForKey:error:]_block_invoke_2.164
+ __50-[SYDClientToDaemonConnection personaUniqueString]_block_invoke.285
+ __50-[SYDClientToDaemonConnection personaUniqueString]_block_invoke.cold.1
+ __54+[SYDClientToDaemonConnection daemonProtocolInterface]_block_invoke.378
+ __54-[SYDClientToDaemonConnection setObject:forKey:error:]_block_invoke.143
+ __57+[SYDClientToDaemonConnection removeUnitTestSyncManagers]_block_invoke.300
+ __57+[SYDClientToDaemonConnection removeUnitTestSyncManagers]_block_invoke.300.cold.1
+ __57+[SYDClientToDaemonConnection removeUnitTestSyncManagers]_block_invoke.cold.1
+ __58-[SYDClientToDaemonConnection isUIFrameworkLinkedInDaemon]_block_invoke.293
+ __58-[SYDClientToDaemonConnection isUIFrameworkLinkedInDaemon]_block_invoke.cold.1
+ __61-[SYDClientToDaemonConnection applicationWillEnterForeground]_block_invoke.254
+ __61-[SYDClientToDaemonConnection applicationWillEnterForeground]_block_invoke.254.cold.1
+ __62-[SYDClientToDaemonConnection containerIDFromDaemonWithError:]_block_invoke.294
+ __62-[SYDClientToDaemonConnection containerIDFromDaemonWithError:]_block_invoke.cold.1
+ __62-[SYDClientToDaemonConnection registerForSynchronizedDefaults]_block_invoke.242
+ __62-[SYDClientToDaemonConnection registerForSynchronizedDefaults]_block_invoke_2.cold.1
+ __62-[SYDClientToDaemonConnection registerForSynchronizedDefaults]_block_invoke_2.cold.2
+ __68-[SYDClientToDaemonConnection synchronizationWithCompletionHandler:]_block_invoke.205
+ __68-[SYDClientToDaemonConnection synchronizationWithCompletionHandler:]_block_invoke.207
+ __74+[SYDClientToDaemonConnection processAccountChangesWithCompletionHandler:]_block_invoke.275
+ __74+[SYDClientToDaemonConnection processAccountChangesWithCompletionHandler:]_block_invoke.275.cold.1
+ __74+[SYDClientToDaemonConnection processAccountChangesWithCompletionHandler:]_block_invoke.275.cold.2
+ __75-[SYDClientToDaemonConnection performOpportunisticAppLaunchSyncIfNecessary]_block_invoke.cold.2
+ __79+[SYDClientToDaemonConnection isCloudSyncUserDefaultEnabledForStoreIdentifier:]_block_invoke.221
+ __85-[SYDClientToDaemonConnection _daemonWithOptions:retries:errorHandler:daemonHandler:]_block_invoke_2.cold.1
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SYDTestDaemonProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SYDTestDaemonProtocol
+ __OBJC_$_PROTOCOL_REFS_SYDDaemonProtocol
+ __OBJC_LABEL_PROTOCOL_$_SYDTestDaemonProtocol
+ __OBJC_PROTOCOL_$_SYDTestDaemonProtocol
+ ___103-[SYDClientToDaemonConnection setFakeError:forNextCloudKitRequestOfClassName:inStoreWithConfiguration:]_block_invoke
+ ___36-[SYDClientToDaemonConnection exit:]_block_invoke
+ ___36-[SYDClientToDaemonConnection exit:]_block_invoke_2
+ ___42-[SYDClientToDaemonConnection changeToken]_block_invoke_3
+ ___44-[SYDClientToDaemonConnection _synchronize:]_block_invoke
+ ___44-[SYDClientToDaemonConnection _synchronize:]_block_invoke_2
+ ___44-[SYDClientToDaemonConnection _synchronize:]_block_invoke_3
+ ___46-[SYDClientToDaemonConnection setChangeToken:]_block_invoke_3
+ ___49-[SYDClientToDaemonConnection deleteDataFromDisk]_block_invoke
+ ___49-[SYDClientToDaemonConnection deleteDataFromDisk]_block_invoke_2
+ ___49-[SYDClientToDaemonConnection deleteDataFromDisk]_block_invoke_3
+ ___50-[SYDClientToDaemonConnection objectForKey:error:]_block_invoke_4
+ ___50-[SYDClientToDaemonConnection personaUniqueString]_block_invoke
+ ___50-[SYDClientToDaemonConnection personaUniqueString]_block_invoke_2
+ ___54-[SYDClientToDaemonConnection setObject:forKey:error:]_block_invoke_4
+ ___56-[SYDClientToDaemonConnection removeObjectForKey:error:]_block_invoke_4
+ ___57+[SYDClientToDaemonConnection removeUnitTestSyncManagers]_block_invoke
+ ___58-[SYDClientToDaemonConnection isUIFrameworkLinkedInDaemon]_block_invoke
+ ___58-[SYDClientToDaemonConnection isUIFrameworkLinkedInDaemon]_block_invoke_2
+ ___62-[SYDClientToDaemonConnection containerIDFromDaemonWithError:]_block_invoke
+ ___62-[SYDClientToDaemonConnection containerIDFromDaemonWithError:]_block_invoke_2
+ ___62-[SYDClientToDaemonConnection registerForSynchronizedDefaults]_block_invoke_2
+ ___65-[SYDClientToDaemonConnection dictionaryRepresentationWithError:]_block_invoke_3
+ ___85-[SYDClientToDaemonConnection _daemonWithOptions:retries:errorHandler:daemonHandler:]_block_invoke
+ ___85-[SYDClientToDaemonConnection _daemonWithOptions:retries:errorHandler:daemonHandler:]_block_invoke_2
+ ___86-[SYDClientToDaemonConnection postFakeAccountChangeNotificationWithCompletionHandler:]_block_invoke
+ ___86-[SYDClientToDaemonConnection postFakeAccountChangeNotificationWithCompletionHandler:]_block_invoke_2
+ ___90-[SYDClientToDaemonConnection postFakeSyncManagerChangeNotificationWithCompletionHandler:]_block_invoke
+ ___90-[SYDClientToDaemonConnection postFakeSyncManagerChangeNotificationWithCompletionHandler:]_block_invoke_2
+ ___block_descriptor_40_e17_B16?0"NSError"8l
+ ___block_descriptor_40_e8_32bs_e29_v16?0"<SYDDaemonProtocol>"8l
+ ___block_descriptor_40_e8_32r_e18_v16?0"NSString"8l
+ ___block_descriptor_40_e8_32r_e23_v16?0"CKContainerID"8l
+ ___block_descriptor_40_e8_32r_e29_v16?0"<SYDDaemonProtocol>"8l
+ ___block_descriptor_40_e8_32s_e29_v16?0"<SYDDaemonProtocol>"8l
+ ___block_descriptor_48_e8_32s40bs_e29_v16?0"<SYDDaemonProtocol>"8l
+ ___block_descriptor_48_e8_32s40r_e29_v16?0"<SYDDaemonProtocol>"8l
+ ___block_descriptor_56_e8_32s40r48r_e29_v16?0"<SYDDaemonProtocol>"8l
+ ___block_descriptor_56_e8_32s40s48r_e29_v16?0"<SYDDaemonProtocol>"8l
+ ___block_descriptor_56_e8_32s40s48s_e29_v16?0"<SYDDaemonProtocol>"8l
+ ___block_descriptor_57_e8_32s40r48r_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48r56r_e29_v16?0"<SYDDaemonProtocol>"8l
+ ___block_descriptor_64_e8_32s40s48s56r_e29_v16?0"<SYDDaemonProtocol>"8l
+ ___block_descriptor_80_e8_32bs40bs48bs56w_e17_v16?0"NSError"8l
+ ___copy_helper_block_e8_32b40b48b56w
+ ___copy_helper_block_e8_32s40r
+ ___destroy_helper_block_e8_32s40r
+ ___destroy_helper_block_e8_32s40s48s56w
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_literal_global.178
+ __block_literal_global.220
+ __block_literal_global.226
+ __block_literal_global.238
+ __block_literal_global.241
+ __block_literal_global.244
+ __block_literal_global.265
+ __block_literal_global.267
+ __block_literal_global.270
+ __block_literal_global.272
+ __block_literal_global.279
+ __block_literal_global.284
+ __block_literal_global.292
+ __block_literal_global.299
+ __block_literal_global.302
+ __block_literal_global.304
+ __block_literal_global.383
+ __block_literal_global.389
+ _block_copy_helper
+ _block_destroy_helper
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_msgSend$_daemonWithOptions:retries:errorHandler:daemonHandler:
+ _objc_msgSend$_synchronize:
+ _objc_msgSend$boolValue
+ _objc_msgSend$connection
+ _objc_msgSend$connection:didRemoveObjectForKey:
+ _objc_msgSend$connection:didSetObject:forKey:
+ _objc_msgSend$connection:didSynchronize:error:
+ _objc_msgSend$connection:willGetObjectForKey:
+ _objc_msgSend$connection:willRemoveObjectForKey:
+ _objc_msgSend$connection:willSetObject:forKey:
+ _objc_msgSend$connectionStoreWillChange:
+ _objc_msgSend$connectionUsingTestServer:
+ _objc_msgSend$connectionWillGetDictionaryRepresentation:
+ _objc_msgSend$connectionWillSynchronize:
+ _objc_msgSend$containerID
+ _objc_msgSend$containerIDWithConfiguration:reply:
+ _objc_msgSend$daemonWithOptions:errorHandler:daemonHandler:
+ _objc_msgSend$decodeObjectOfClasses:forKey:
+ _objc_msgSend$delegate
+ _objc_msgSend$deleteDataFromDiskForStoreWithConfiguration:reply:
+ _objc_msgSend$entitlementOverrides
+ _objc_msgSend$exit
+ _objc_msgSend$initWithContainerIdentifier:environment:
+ _objc_msgSend$initWithServiceName:options:
+ _objc_msgSend$isUIFrameworkLinkedInDaemonWithReply:
+ _objc_msgSend$personaUniqueStringWithReply:
+ _objc_msgSend$postFakeAccountChangeNotificationWithCompletionHandler:
+ _objc_msgSend$postFakeSyncManagerChangeNotificationForStoreWithConfiguration:completionHandler:
+ _objc_msgSend$removeUnitTestSyncManagersWithReply:
+ _objc_msgSend$setContainerID:
+ _objc_msgSend$setEntitlementOverrides:
+ _objc_msgSend$setFakeError:forNextCloudKitRequestOfClassName:inStoreWithConfiguration:
+ _objc_msgSend$shouldSyncOnFirstInitializationOverride
+ _objc_msgSend$useTestServer
+ _objc_msgSend$useTestServerByDefault
+ _objc_opt_respondsToSelector
+ _sUseTestServerByDefault
+ _symbolic Sccyyt______pG s5ErrorP
- +[SYDClientToDaemonConnection machServiceNameUsingTestServer:]
- +[SYDClientToDaemonConnection machServiceName]
- -[SYDClientToDaemonConnection asyncDaemonWithErrorHandler:]
- -[SYDClientToDaemonConnection machServiceName]
- -[SYDClientToDaemonConnection setStoreConfiguration:]
- -[SYDClientToDaemonConnection synchronousDaemonWithErrorHandler:]
- GCC_except_table110
- GCC_except_table113
- GCC_except_table117
- GCC_except_table126
- GCC_except_table147
- GCC_except_table156
- GCC_except_table166
- GCC_except_table168
- GCC_except_table169
- GCC_except_table171
- GCC_except_table222
- GCC_except_table235
- GCC_except_table35
- GCC_except_table42
- GCC_except_table58
- GCC_except_table63
- GCC_except_table66
- GCC_except_table71
- GCC_except_table72
- GCC_except_table83
- GCC_except_table99
- __105+[SYDClientToDaemonConnection synchronizeStoresWithIdentifiers:type:testConfiguration:completionHandler:]_block_invoke.186
- __105+[SYDClientToDaemonConnection synchronizeStoresWithIdentifiers:type:testConfiguration:completionHandler:]_block_invoke.186.cold.1
- __105+[SYDClientToDaemonConnection synchronizeStoresWithIdentifiers:type:testConfiguration:completionHandler:]_block_invoke.187
- __105+[SYDClientToDaemonConnection synchronizeStoresWithIdentifiers:type:testConfiguration:completionHandler:]_block_invoke.188
- __44-[SYDClientToDaemonConnection xpcConnection]_block_invoke.301
- __47+[SYDClientToDaemonConnection newXPCConnection]_block_invoke.205
- __47+[SYDClientToDaemonConnection newXPCConnection]_block_invoke.205.cold.1
- __49-[SYDClientToDaemonConnection synchronizeForced:]_block_invoke.173
- __49-[SYDClientToDaemonConnection synchronizeForced:]_block_invoke.cold.1
- __49-[SYDClientToDaemonConnection synchronizeForced:]_block_invoke.cold.2
- __49-[SYDClientToDaemonConnection synchronizeForced:]_block_invoke.cold.3
- __50-[SYDClientToDaemonConnection objectForKey:error:]_block_invoke.139
- __50-[SYDClientToDaemonConnection objectForKey:error:]_block_invoke.139.cold.1
- __50-[SYDClientToDaemonConnection objectForKey:error:]_block_invoke.139.cold.2
- __50-[SYDClientToDaemonConnection objectForKey:error:]_block_invoke.143
- __50-[SYDClientToDaemonConnection objectForKey:error:]_block_invoke_2.147
- __54+[SYDClientToDaemonConnection daemonProtocolInterface]_block_invoke.289
- __54-[SYDClientToDaemonConnection setObject:forKey:error:]_block_invoke.136
- __59-[SYDClientToDaemonConnection asyncDaemonWithErrorHandler:]_block_invoke.cold.1
- __61-[SYDClientToDaemonConnection applicationWillEnterForeground]_block_invoke.221
- __61-[SYDClientToDaemonConnection applicationWillEnterForeground]_block_invoke.221.cold.1
- __62-[SYDClientToDaemonConnection registerForSynchronizedDefaults]_block_invoke.211
- __62-[SYDClientToDaemonConnection registerForSynchronizedDefaults]_block_invoke.211.cold.1
- __62-[SYDClientToDaemonConnection registerForSynchronizedDefaults]_block_invoke.211.cold.2
- __65-[SYDClientToDaemonConnection synchronousDaemonWithErrorHandler:]_block_invoke.cold.1
- __68-[SYDClientToDaemonConnection synchronizationWithCompletionHandler:]_block_invoke.180
- __74+[SYDClientToDaemonConnection processAccountChangesWithCompletionHandler:]_block_invoke.238
- __74+[SYDClientToDaemonConnection processAccountChangesWithCompletionHandler:]_block_invoke.238.cold.1
- __74+[SYDClientToDaemonConnection processAccountChangesWithCompletionHandler:]_block_invoke.238.cold.2
- __79+[SYDClientToDaemonConnection isCloudSyncUserDefaultEnabledForStoreIdentifier:]_block_invoke.193
- ___49-[SYDClientToDaemonConnection synchronizeForced:]_block_invoke
- ___49-[SYDClientToDaemonConnection synchronizeForced:]_block_invoke_2
- ___59-[SYDClientToDaemonConnection asyncDaemonWithErrorHandler:]_block_invoke
- ___65-[SYDClientToDaemonConnection synchronousDaemonWithErrorHandler:]_block_invoke
- ___block_descriptor_56_e8_32s40r48r_e5_v8?0l
- __block_literal_global.175
- __block_literal_global.192
- __block_literal_global.198
- __block_literal_global.204
- __block_literal_global.207
- __block_literal_global.210
- __block_literal_global.213
- __block_literal_global.230
- __block_literal_global.232
- __block_literal_global.237
- __block_literal_global.240
- __block_literal_global.294
- __block_literal_global.300
- _objc_msgSend$asyncDaemonWithErrorHandler:
- _objc_msgSend$machServiceName
- _objc_msgSend$machServiceNameUsingTestServer:
- _objc_msgSend$synchronize
- _objc_msgSend$synchronizeForced:
- _objc_msgSend$synchronousDaemonWithErrorHandler:
- _swift_arrayDestroy
- _swift_bridgeObjectRetain
CStrings:
+ " containerID=%@"
+ " entitlementOverrides=%@"
+ "'"
+ "@\"<SYDClientToDaemonConnectionDelegate>\""
+ "@\"CKContainerID\""
+ "@\"NSDictionary\""
+ "B16@?0@\"NSError\"8"
+ "C20@0:8B16"
+ "Deleting data from disk for %@"
+ "Error obtaining %{public}@ remote object proxy: %@"
+ "Error obtaining synchronous remote object proxy to fetch if a UI framework is linked: %@"
+ "Error obtaining synchronous remote object proxy to fetch persona unique string: %@"
+ "Error obtaining synchronous remote object proxy to fetch value for containerID: %@"
+ "Failed to set fake CloudKit request error with error: %@"
+ "Finished deleting data from disk"
+ "Not syncing on first initialization because we're in the tests"
+ "Removed unit test sync managers"
+ "Removing unit test sync managers"
+ "Retrying XPC message on interruption"
+ "SYDTestDaemonProtocol"
+ "T@\"<SYDClientToDaemonConnectionDelegate>\",W,V_delegate"
+ "T@\"CKContainerID\",C,N"
+ "T@\"NSDictionary\",C,N,V_entitlementOverrides"
+ "T@\"SYDStoreConfiguration\",R,N,V_storeConfiguration"
+ "TB,N,V_useTestServer"
+ "Telling daemon to exit"
+ "Telling daemon to post fake account change notification"
+ "Telling daemon to post fake sync manager change notification"
+ "Telling daemon to set fake CloudKit request error"
+ "Using test server service name"
+ "_cachedObjectForKey:"
+ "_containerID"
+ "_daemonWithOptions:retries:errorHandler:daemonHandler:"
+ "_delegate"
+ "_entitlementOverrides"
+ "_synchronize:"
+ "_useTestServer"
+ "asynchronous"
+ "boolValue"
+ "com.apple.CloudKeyValuesTestingService"
+ "com.apple.KeyValueService"
+ "com.apple.KeyValueService.Encrypted"
+ "com.apple.KeyValueService.EndToEndEncrypted"
+ "com.apple.KeyValueService.EndToEndEncrypted.AllPlatforms"
+ "connection"
+ "connection:didRemoveObjectForKey:"
+ "connection:didSetObject:forKey:"
+ "connection:didSynchronize:error:"
+ "connection:willGetObjectForKey:"
+ "connection:willRemoveObjectForKey:"
+ "connection:willSetObject:forKey:"
+ "connectionStoreWillChange:"
+ "connectionUsingTestServer:"
+ "connectionWillGetDictionaryRepresentation:"
+ "connectionWillSynchronize:"
+ "container"
+ "containerID"
+ "containerIDFromDaemonWithError:"
+ "containerIDWithConfiguration:reply:"
+ "daemonWithOptions:errorHandler:daemonHandler:"
+ "decodeObjectOfClasses:forKey:"
+ "delegate"
+ "deleteDataFromDisk"
+ "deleteDataFromDiskForStoreWithConfiguration:reply:"
+ "e"
+ "entitlementOverrides"
+ "exit"
+ "exit:"
+ "initWithContainerIdentifier:environment:"
+ "initWithServiceName:options:"
+ "isUIFrameworkLinkedInDaemon"
+ "isUIFrameworkLinkedInDaemonWithReply:"
+ "kvs/exit"
+ "kvs/post-fake-account-change"
+ "kvs/post-fake-sync-manager-change"
+ "kvs/set-fake-cloudkit-error"
+ "personaUniqueStringWithReply:"
+ "postFakeAccountChangeNotificationWithCompletionHandler:"
+ "postFakeAccountChangeNotificationWithPreviousID:currentID:completionHandler:"
+ "postFakeSyncManagerChangeNotificationForStoreWithConfiguration:completionHandler:"
+ "postFakeSyncManagerChangeNotificationWithCompletionHandler:"
+ "removeUnitTestSyncManagers"
+ "removeUnitTestSyncManagersWithReply:"
+ "setContainerID:"
+ "setDelegate:"
+ "setEntitlementOverrides:"
+ "setFakeError:forNextCloudKitRequestOfClassName:inStoreWithConfiguration:"
+ "setUseTestServer:"
+ "setUseTestServerByDefault:"
+ "synchronous"
+ "useTestServer"
+ "useTestServerByDefault"
+ "v16@?0@\"<SYDDaemonProtocol>\"8"
+ "v16@?0@\"CKContainerID\"8"
+ "v16@?0@\"NSString\"8"
+ "v24@0:8@?<v@?>16"
+ "v24@0:8@?<v@?@\"NSString\">16"
+ "v24@0:8@?<v@?B>16"
+ "v32@0:8@\"SYDStoreConfiguration\"16@?<v@?>24"
+ "v32@0:8@\"SYDStoreConfiguration\"16@?<v@?@\"CKContainerID\">24"
+ "v40@0:8@\"NSError\"16@\"NSString\"24@\"SYDStoreConfiguration\"32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@16@24@32"
+ "v40@0:8q16@?24@?32"
+ "v48@0:8q16Q24@?32@?40"
- "@24@0:8@?16"
- "Error obtaining asynchronous remote object proxy: %@"
- "Error obtaining synchronous remote object proxy: %@"
- "Expected non-nil XPC connection"
- "Expected non-nil XPC connection queue"
- "T@\"SYDStoreConfiguration\",&,N,V_storeConfiguration"
- "asyncDaemonWithErrorHandler:"
- "machServiceName"
- "machServiceNameUsingTestServer:"
- "setStoreConfiguration:"
- "synchronousDaemonWithErrorHandler:"

```
