## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-4479.120.7.0.1
-  __TEXT.__text: 0x321bac
-  __TEXT.__auth_stubs: 0x1a90
-  __TEXT.__objc_methlist: 0x1aa7c
-  __TEXT.__const: 0x4e0
-  __TEXT.__cstring: 0x7e0ad
-  __TEXT.__oslogstring: 0x3b864
-  __TEXT.__gcc_except_tab: 0x19f98
+4479.120.19.0.0
+  __TEXT.__text: 0x324de8
+  __TEXT.__auth_stubs: 0x1a80
+  __TEXT.__objc_methlist: 0x1abbc
+  __TEXT.__const: 0x510
+  __TEXT.__cstring: 0x7ee61
+  __TEXT.__oslogstring: 0x3b991
+  __TEXT.__gcc_except_tab: 0x1a150
   __TEXT.__ustring: 0x36
-  __TEXT.__unwind_info: 0xa7e8
-  __TEXT.__objc_classname: 0x2ae4
-  __TEXT.__objc_methname: 0x45c09
-  __TEXT.__objc_methtype: 0x94d2
-  __TEXT.__objc_stubs: 0x2fca0
-  __DATA_CONST.__got: 0x1728
-  __DATA_CONST.__const: 0x9500
-  __DATA_CONST.__objc_classlist: 0xa58
+  __TEXT.__unwind_info: 0xa870
+  __TEXT.__objc_classname: 0x2b45
+  __TEXT.__objc_methname: 0x45e1e
+  __TEXT.__objc_methtype: 0x9570
+  __TEXT.__objc_stubs: 0x2fe00
+  __DATA_CONST.__got: 0x1730
+  __DATA_CONST.__const: 0x96e8
+  __DATA_CONST.__objc_classlist: 0xa68
   __DATA_CONST.__objc_catlist: 0xd8
-  __DATA_CONST.__objc_protolist: 0x298
+  __DATA_CONST.__objc_protolist: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xeb08
+  __DATA_CONST.__objc_selrefs: 0xeb78
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x910
+  __DATA_CONST.__objc_superrefs: 0x918
   __DATA_CONST.__objc_arraydata: 0xea0
-  __AUTH_CONST.__auth_got: 0xd58
-  __AUTH_CONST.__const: 0x2bd0
-  __AUTH_CONST.__cfstring: 0x22a20
-  __AUTH_CONST.__objc_const: 0x3d8f8
+  __AUTH_CONST.__auth_got: 0xd50
+  __AUTH_CONST.__const: 0x2bb0
+  __AUTH_CONST.__cfstring: 0x22d20
+  __AUTH_CONST.__objc_const: 0x3e1c8
   __AUTH_CONST.__objc_intobj: 0xbe8
   __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x50
-  __AUTH.__objc_data: 0x2698
+  __AUTH.__objc_data: 0x2788
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x1f48
-  __DATA.__data: 0x2800
+  __DATA.__objc_ivar: 0x1f54
+  __DATA.__data: 0x2860
   __DATA.__bss: 0x210
-  __DATA_DIRTY.__objc_data: 0x40d8
+  __DATA_DIRTY.__objc_data: 0x4088
   __DATA_DIRTY.__data: 0xd0
   __DATA_DIRTY.__bss: 0x408
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 1FD3A183-9AB1-3323-82A2-4F936CFAF1FF
-  Functions: 13779
-  Symbols:   45379
-  CStrings:  27858
+  UUID: 83EC03EA-0C48-3EE2-A52C-BA526517E793
+  Functions: 13813
+  Symbols:   45500
+  CStrings:  27972
 
Symbols:
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newSyncEngineV1StatusEventWithValue:]
+ +[BRCAccountSession(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:dbCreationDate:options:error:]
+ +[BRCAccountSession(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:dbCreationDate:options:error:].cold.1
+ +[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:skipControlFiles:dbCreationDate:options:]
+ +[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:skipControlFiles:dbCreationDate:options:].cold.1
+ +[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:options:error:]
+ +[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:options:error:].cold.1
+ +[BRCSyncEngineMigrationTelemetryManager _calculateSyncStatusWithDBFacade:zoneAppRetriever:]
+ +[BRCSyncEngineMigrationTelemetryManager _calculateSyncStatusWithDBFacade:zoneAppRetriever:].cold.1
+ +[BRCSyncEngineMigrationTelemetryManager _describeSyncStatus:]
+ +[BRCSyncEngineMigrationTelemetryManager collectSyncEngineTelemetryIfNeededWithSessionContext:osWasUpgraded:]
+ +[BRCSyncEngineMigrationTelemetryManager syncStatusDescriptionWithDBFacade:zoneAppRetriever:]
+ -[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:initialVersion:lastCurrentVersion:options:error:]
+ -[BRCAccountSession(BRCDatabaseManager) openDBForNewDomain:options:withError:]
+ -[BRCAccountsManager _sendTapToRadarForDomainMatchingError:forDomains:]
+ -[BRCClientDatabaseFacade getSyncStatusBitMask]
+ -[BRCLocalItem markLatestSyncRequestFailedInZone:shouldBackoff:]
+ -[BRCLocalItem markLatestSyncRequestFailedInZone:shouldBackoff:].cold.1
+ -[BRCPackageManifestWriter stagePackageWithReader:package:xattrsPackage:stageItemURL:existingContentsURL:recordName:isDocumentModifiedByOtherUser:].cold.9
+ -[BRCSQLNamedThrottleManager .cxx_destruct]
+ -[BRCSQLNamedThrottleManager cleanNamedThrottleTable]
+ -[BRCSQLNamedThrottleManager cleanNamedThrottleTable].cold.1
+ -[BRCSQLNamedThrottleManager cleanNamedThrottleTable].cold.2
+ -[BRCSQLNamedThrottleManager dumpToContext:]
+ -[BRCSQLNamedThrottleManager initWithDB:]
+ -[BRCSQLNamedThrottleManager throttle:subCategory:withRules:onQueue:block:]
+ -[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:]
+ -[BRCUserDefaults limitPackageItemPathsUnderPackageRootInPackageReader]
+ -[BRCUserDefaults shouldSendSyncEngineTelemetry]
+ -[BRCUserDefaultsNamedThrottleManager .cxx_destruct]
+ -[BRCUserDefaultsNamedThrottleManager _getMaxLastRunForThrottle:fromData:]
+ -[BRCUserDefaultsNamedThrottleManager _getRecordForThrottle:subCategory:fromData:]
+ -[BRCUserDefaultsNamedThrottleManager _getThrottleData]
+ -[BRCUserDefaultsNamedThrottleManager _keyForThrottle:subCategory:]
+ -[BRCUserDefaultsNamedThrottleManager _saveRecord:forThrottle:subCategory:inData:]
+ -[BRCUserDefaultsNamedThrottleManager _saveThrottleData:]
+ -[BRCUserDefaultsNamedThrottleManager _updateMaxLastRun:forThrottle:inData:]
+ -[BRCUserDefaultsNamedThrottleManager cleanNamedThrottleTable]
+ -[BRCUserDefaultsNamedThrottleManager dumpToContext:]
+ -[BRCUserDefaultsNamedThrottleManager initWithUserDefaults:]
+ -[BRCUserDefaultsNamedThrottleManager throttle:subCategory:withRules:onQueue:block:]
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) copyStructureRecordIDForItemIdentifier:reply:]
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) getStructureRecordIDsForFPItems:reply:]
+ GCC_except_table178
+ GCC_except_table575
+ _OBJC_CLASS_$_BRCSQLNamedThrottleManager
+ _OBJC_CLASS_$_BRCSyncEngineMigrationTelemetryManager
+ _OBJC_CLASS_$_BRCUserDefaultsNamedThrottleManager
+ _OBJC_IVAR_$_BRCSQLNamedThrottleManager._currentOSVersion
+ _OBJC_IVAR_$_BRCSQLNamedThrottleManager._db
+ _OBJC_IVAR_$_BRCUserDefaultsNamedThrottleManager._currentOSVersion
+ _OBJC_IVAR_$_BRCUserDefaultsNamedThrottleManager._serialQueue
+ _OBJC_IVAR_$_BRCUserDefaultsNamedThrottleManager._userDefaults
+ _OBJC_METACLASS_$_BRCSQLNamedThrottleManager
+ _OBJC_METACLASS_$_BRCSyncEngineMigrationTelemetryManager
+ _OBJC_METACLASS_$_BRCUserDefaultsNamedThrottleManager
+ __OBJC_$_CLASS_METHODS_BRCSyncEngineMigrationTelemetryManager
+ __OBJC_$_INSTANCE_METHODS_BRCSQLNamedThrottleManager
+ __OBJC_$_INSTANCE_METHODS_BRCUserDefaultsNamedThrottleManager
+ __OBJC_$_INSTANCE_VARIABLES_BRCSQLNamedThrottleManager
+ __OBJC_$_INSTANCE_VARIABLES_BRCUserDefaultsNamedThrottleManager
+ __OBJC_$_PROP_LIST_BRCSQLNamedThrottleManager
+ __OBJC_$_PROP_LIST_BRCUserDefaultsNamedThrottleManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BRCNamedThrottling
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BRCNamedThrottling
+ __OBJC_$_PROTOCOL_REFS_BRCNamedThrottling
+ __OBJC_CLASS_PROTOCOLS_$_BRCSQLNamedThrottleManager
+ __OBJC_CLASS_PROTOCOLS_$_BRCUserDefaultsNamedThrottleManager
+ __OBJC_CLASS_RO_$_BRCSQLNamedThrottleManager
+ __OBJC_CLASS_RO_$_BRCSyncEngineMigrationTelemetryManager
+ __OBJC_CLASS_RO_$_BRCUserDefaultsNamedThrottleManager
+ __OBJC_LABEL_PROTOCOL_$_BRCNamedThrottling
+ __OBJC_METACLASS_RO_$_BRCSQLNamedThrottleManager
+ __OBJC_METACLASS_RO_$_BRCSyncEngineMigrationTelemetryManager
+ __OBJC_METACLASS_RO_$_BRCUserDefaultsNamedThrottleManager
+ __OBJC_PROTOCOL_$_BRCNamedThrottling
+ ___104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke.182
+ ___104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke.182.cold.1
+ ___109+[BRCSyncEngineMigrationTelemetryManager collectSyncEngineTelemetryIfNeededWithSessionContext:osWasUpgraded:]_block_invoke
+ ___125-[BRCXPCRegularIPCsClient(FPFSAdditions) uploadItemIdentifier:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.213
+ ___132-[BRCAccountSession _recoverNamespaceAndContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:]_block_invoke.285
+ ___173+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:options:error:]_block_invoke
+ ___173+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:options:error:]_block_invoke.cold.1
+ ___23-[BRCDaemon selfCheck:]_block_invoke.107
+ ___26-[BRCAccountSession close]_block_invoke.368
+ ___37-[BRCAccountSession destroyLocalData]_block_invoke.391
+ ___37-[BRCAccountSession destroyLocalData]_block_invoke.391.cold.1
+ ___40-[BRCDaemon networkReachabilityChanged:]_block_invoke.115
+ ___40-[BRCDaemon networkReachabilityChanged:]_block_invoke.115.cold.1
+ ___40-[BRCDaemon networkReachabilityChanged:]_block_invoke.119
+ ___40-[BRCDaemon networkReachabilityChanged:]_block_invoke_2.120
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.330
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.334
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.334.cold.1
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.347
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.332
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.332.cold.1
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.332.cold.2
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.338
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_3.342
+ ___43-[BRCAccountSession _reportBasehashSalting]_block_invoke.267
+ ___43-[BRCAccountSession _reportBasehashSalting]_block_invoke.267.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.393
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.393.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.393.cold.2
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.393.cold.3
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.393.cold.4
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.400
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.400.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.403
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.425
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.425.cold.1
+ ___47-[BRCAccountsManager waitUntilDeviceIsUnlocked]_block_invoke.89
+ ___48-[BRCAccountSession openWithError:pushWorkloop:]_block_invoke.235
+ ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke.93
+ ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke.93.cold.1
+ ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke_2.99
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.308
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.308.cold.1
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.308.cold.2
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.308.cold.3
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.308.cold.4
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.312
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.322
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.322.cold.1
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.322.cold.2
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.322.cold.3
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.322.cold.4
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.326
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.309
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.316
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.316.cold.1
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.316.cold.2
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.316.cold.3
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.316.cold.4
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.323
+ ___53-[BRCAccountSession _pcsChainAllItemsWithSystemTask:]_block_invoke.238
+ ___54-[BRCContainerScheduler _updatePushTopicsRegistration]_block_invoke.266
+ ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.439
+ ___61-[BRCAccountSession _saltPartiallySaltedItemsWithSystemTask:]_block_invoke.252
+ ___61-[BRCAccountSession _saltPartiallySaltedItemsWithSystemTask:]_block_invoke.255
+ ___62-[BRCUserDefaultsNamedThrottleManager cleanNamedThrottleTable]_block_invoke
+ ___62-[BRCUserDefaultsNamedThrottleManager cleanNamedThrottleTable]_block_invoke.cold.1
+ ___62-[BRCUserDefaultsNamedThrottleManager cleanNamedThrottleTable]_block_invoke.cold.2
+ ___65-[BRCAccountsManager updateAccountDisplayName:completionHandler:]_block_invoke.82
+ ___66-[BRCAccountSession setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke.455
+ ___72-[BRCXPCRegularIPCsClient(FPFSAdditions) waitForStabilizationWithReply:]_block_invoke.211
+ ___73-[BRCXPCRegularIPCsClient(FPFSAdditions) getCKRecordIDsForFPItems:reply:]_block_invoke.215
+ ___75-[BRCSQLNamedThrottleManager throttle:subCategory:withRules:onQueue:block:]_block_invoke
+ ___75-[BRCSQLNamedThrottleManager throttle:subCategory:withRules:onQueue:block:]_block_invoke.22
+ ___75-[BRCSQLNamedThrottleManager throttle:subCategory:withRules:onQueue:block:]_block_invoke_2
+ ___75-[BRCSQLNamedThrottleManager throttle:subCategory:withRules:onQueue:block:]_block_invoke_3
+ ___75-[BRCXPCRegularIPCsClient(FPFSAdditions) getFPItemIDsForCKRecordIDs:reply:]_block_invoke.217
+ ___78-[BRCAccountSession(BRCDatabaseManager) openDBForNewDomain:options:withError:]_block_invoke
+ ___78-[BRCAccountSession(BRCDatabaseManager) openDBForNewDomain:options:withError:]_block_invoke_2
+ ___79-[BRCBGSystemTaskManager submitBGSystemTaskWithIdentifier:configuration:block:]_block_invoke.26
+ ___79-[BRCBGSystemTaskManager submitBGSystemTaskWithIdentifier:configuration:block:]_block_invoke.26.cold.1
+ ___79-[BRCBGSystemTaskManager submitBGSystemTaskWithIdentifier:configuration:block:]_block_invoke.26.cold.2
+ ___80-[BRCXPCRegularIPCsClient(FPFSAdditions) getStructureRecordIDsForFPItems:reply:]_block_invoke
+ ___80-[BRCXPCRegularIPCsClient(FPFSAdditions) getStructureRecordIDsForFPItems:reply:]_block_invoke.216
+ ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.72
+ ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.73
+ ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.73.cold.1
+ ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.74
+ ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.75
+ ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.76
+ ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.76.cold.1
+ ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.77
+ ___82-[BRCAccountsManager _scheduleExistingFileProviderDomainsMaintenanceWithAccounts:]_block_invoke.78
+ ___83-[BRCAccountSession locateItemWithIdentifier:zoneName:ownerName:completionHandler:]_block_invoke.490
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.431
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.431.cold.1
+ ___84-[BRCUserDefaultsNamedThrottleManager throttle:subCategory:withRules:onQueue:block:]_block_invoke
+ ___84-[BRCUserDefaultsNamedThrottleManager throttle:subCategory:withRules:onQueue:block:]_block_invoke.43
+ ___84-[BRCUserDefaultsNamedThrottleManager throttle:subCategory:withRules:onQueue:block:]_block_invoke_2
+ ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerSaltingKeysAtItemIdentifier:reply:]_block_invoke.198
+ ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerSaltingKeysAtItemIdentifier:reply:]_block_invoke.204
+ ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) copyStructureRecordIDForItemIdentifier:reply:]_block_invoke
+ ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) copyStructureRecordIDForItemIdentifier:reply:]_block_invoke.177
+ ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) checkIfItemIsShareableWithItemIdentifier:reply:]_block_invoke.178
+ ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) startOperation:toWaitForFPFSMigrationWithReply:]_block_invoke.185
+ ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getCreatorNameComponentsForItemIdentifier:reply:]_block_invoke.179
+ ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerContentSignatureAtItemIdentifier:reply:]_block_invoke.206
+ ___92+[BRCSyncEngineMigrationTelemetryManager _calculateSyncStatusWithDBFacade:zoneAppRetriever:]_block_invoke
+ ___97-[BRCXPCRegularIPCsClient(FPFSAdditions) getClientSaltingVerificationKeysAtItemIdentifier:reply:]_block_invoke.190
+ ___99-[BRCAccountSession learnNewItemIdentifier:forItemIdentifier:zoneName:ownerName:completionHandler:]_block_invoke.488
+ ___block_descriptor_40_e8_32r_e23_B16?0"BRCClientZone"8lr32l8
+ ___block_descriptor_48_e8_32s40r_e42_v16?0"BRCReadWriteClientDatabaseFacade"8lr40l8s32l8
+ ___block_literal_global.103
+ ___block_literal_global.1052
+ ___block_literal_global.111
+ ___block_literal_global.118
+ ___block_literal_global.123
+ ___block_literal_global.125
+ ___block_literal_global.184
+ ___block_literal_global.217
+ ___block_literal_global.219
+ ___block_literal_global.248
+ ___block_literal_global.253
+ ___block_literal_global.303
+ ___block_literal_global.311
+ ___block_literal_global.318
+ ___block_literal_global.325
+ ___block_literal_global.370
+ ___block_literal_global.378
+ ___block_literal_global.402
+ ___block_literal_global.69
+ ___block_literal_global.95
+ __structureRecordIDForItem
+ __structureRecordIDForItem.cold.1
+ __structureRecordIDForItem.cold.2
+ _br_sync_status_flags_entries
+ _objc_msgSend$_calculateSyncStatusWithDBFacade:zoneAppRetriever:
+ _objc_msgSend$_checkIntegrity:serverTruth:session:skipControlFiles:dbCreationDate:options:error:
+ _objc_msgSend$_describeSyncStatus:
+ _objc_msgSend$_getMaxLastRunForThrottle:fromData:
+ _objc_msgSend$_getRecordForThrottle:subCategory:fromData:
+ _objc_msgSend$_getThrottleData
+ _objc_msgSend$_keyForThrottle:subCategory:
+ _objc_msgSend$_registerLastBootIfNeeded:table:skipControlFiles:dbCreationDate:options:
+ _objc_msgSend$_saveRecord:forThrottle:subCategory:inData:
+ _objc_msgSend$_saveThrottleData:
+ _objc_msgSend$_sendTapToRadarForDomainMatchingError:forDomains:
+ _objc_msgSend$_updateMaxLastRun:forThrottle:inData:
+ _objc_msgSend$brc_addPartialError:forFileProviderItemIdentifier:toError:
+ _objc_msgSend$cleanNamedThrottleTable
+ _objc_msgSend$collectSyncEngineTelemetryIfNeededWithSessionContext:osWasUpgraded:
+ _objc_msgSend$dictionaryForKey:
+ _objc_msgSend$getSyncStatusBitMask
+ _objc_msgSend$initWithUserDefaults:
+ _objc_msgSend$limitPackageItemPathsUnderPackageRootInPackageReader
+ _objc_msgSend$markLatestSyncRequestFailedInZone:shouldBackoff:
+ _objc_msgSend$matchDomainWithAccountAndStampDomainIfNeeded:withAccounts:persistDomain:error:
+ _objc_msgSend$newSyncEngineV1StatusEventWithValue:
+ _objc_msgSend$openAndValidateDatabase:serverTruth:initialVersion:lastCurrentVersion:options:error:
+ _objc_msgSend$openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:options:error:
+ _objc_msgSend$openDBForNewDomain:options:withError:
+ _objc_msgSend$shouldSendSyncEngineTelemetry
+ _objc_msgSend$syncStatusDescriptionWithDBFacade:zoneAppRetriever:
- +[BRCAccountSession(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:dbCreationDate:deviceIDChanged:error:]
- +[BRCAccountSession(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:dbCreationDate:deviceIDChanged:error:].cold.1
- +[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:skipControlFiles:dbCreationDate:deviceIDChanged:]
- +[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:skipControlFiles:dbCreationDate:deviceIDChanged:].cold.1
- +[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:deviceIDChanged:error:]
- +[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:deviceIDChanged:error:].cold.1
- -[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:initialVersion:lastCurrentVersion:deviceIDChanged:error:]
- -[BRCAccountSession(BRCDatabaseManager) openDBForNewDomain:deviceIDChanged:withError:]
- -[BRCBGSystemTaskManager _cancelSyncTasks:scheduler:]
- -[BRCBGSystemTaskManager garbageCollectAllDanglingSyncTasks]
- -[BRCBGSystemTaskManager garbageCollectAllDanglingSyncTasks].cold.1
- -[BRCLocalItem markLatestSyncRequestFailedInZone:]
- -[BRCLocalItem markLatestSyncRequestFailedInZone:].cold.1
- -[BRCNamedThrottleManager .cxx_destruct]
- -[BRCNamedThrottleManager cleanNamedThrottleTable:]
- -[BRCNamedThrottleManager cleanNamedThrottleTable:].cold.1
- -[BRCNamedThrottleManager cleanNamedThrottleTable:].cold.2
- -[BRCNamedThrottleManager dumpToContext:]
- -[BRCNamedThrottleManager initWithDB:]
- -[BRCNamedThrottleManager throttle:subCategory:withRules:onQueue:block:]
- -[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:additionalDevices:triggerRootCause:]
- GCC_except_table180
- GCC_except_table76
- _OBJC_CLASS_$_BRCNamedThrottleManager
- _OBJC_CLASS_$__DASScheduler
- _OBJC_IVAR_$_BRCNamedThrottleManager._currentOSVersion
- _OBJC_IVAR_$_BRCNamedThrottleManager._db
- _OBJC_METACLASS_$_BRCNamedThrottleManager
- __OBJC_$_INSTANCE_METHODS_BRCNamedThrottleManager
- __OBJC_$_INSTANCE_VARIABLES_BRCNamedThrottleManager
- __OBJC_CLASS_RO_$_BRCNamedThrottleManager
- __OBJC_METACLASS_RO_$_BRCNamedThrottleManager
- ___104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke.181
- ___104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke.181.cold.1
- ___125-[BRCXPCRegularIPCsClient(FPFSAdditions) uploadItemIdentifier:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.212
- ___132-[BRCAccountSession _recoverNamespaceAndContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:]_block_invoke.284
- ___181+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:deviceIDChanged:error:]_block_invoke
- ___181+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:deviceIDChanged:error:]_block_invoke.cold.1
- ___23-[BRCDaemon selfCheck:]_block_invoke.108
- ___26-[BRCAccountSession close]_block_invoke.367
- ___37-[BRCAccountSession destroyLocalData]_block_invoke.390
- ___37-[BRCAccountSession destroyLocalData]_block_invoke.390.cold.1
- ___40-[BRCDaemon networkReachabilityChanged:]_block_invoke.116
- ___40-[BRCDaemon networkReachabilityChanged:]_block_invoke.116.cold.1
- ___40-[BRCDaemon networkReachabilityChanged:]_block_invoke.120
- ___40-[BRCDaemon networkReachabilityChanged:]_block_invoke_2.121
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.328
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.332
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.333.cold.1
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.346
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.331
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.331.cold.1
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.331.cold.2
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.337
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_3.341
- ___43-[BRCAccountSession _reportBasehashSalting]_block_invoke.266
- ___43-[BRCAccountSession _reportBasehashSalting]_block_invoke.266.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.392
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.392.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.392.cold.2
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.392.cold.3
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.392.cold.4
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.399
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.399.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.402
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.424
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.424.cold.1
- ___47-[BRCAccountsManager waitUntilDeviceIsUnlocked]_block_invoke.77
- ___48-[BRCAccountSession openWithError:pushWorkloop:]_block_invoke.234
- ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke.94
- ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke.94.cold.1
- ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke_2.100
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.307
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.307.cold.1
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.307.cold.2
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.307.cold.3
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.307.cold.4
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.311
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.321
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.321.cold.1
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.321.cold.2
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.321.cold.3
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.321.cold.4
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.325
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.308
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.315
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.315.cold.1
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.315.cold.2
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.315.cold.3
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.315.cold.4
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.322
- ___53-[BRCAccountSession _pcsChainAllItemsWithSystemTask:]_block_invoke.237
- ___53-[BRCBGSystemTaskManager _cancelSyncTasks:scheduler:]_block_invoke
- ___53-[BRCBGSystemTaskManager _cancelSyncTasks:scheduler:]_block_invoke_2
- ___54-[BRCContainerScheduler _updatePushTopicsRegistration]_block_invoke.262
- ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.437
- ___61-[BRCAccountSession _saltPartiallySaltedItemsWithSystemTask:]_block_invoke.251
- ___61-[BRCAccountSession _saltPartiallySaltedItemsWithSystemTask:]_block_invoke.254
- ___65-[BRCAccountsManager updateAccountDisplayName:completionHandler:]_block_invoke.70
- ___66-[BRCAccountSession setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke.454
- ___72-[BRCNamedThrottleManager throttle:subCategory:withRules:onQueue:block:]_block_invoke
- ___72-[BRCNamedThrottleManager throttle:subCategory:withRules:onQueue:block:]_block_invoke.22
- ___72-[BRCNamedThrottleManager throttle:subCategory:withRules:onQueue:block:]_block_invoke_2
- ___72-[BRCNamedThrottleManager throttle:subCategory:withRules:onQueue:block:]_block_invoke_3
- ___72-[BRCXPCRegularIPCsClient(FPFSAdditions) waitForStabilizationWithReply:]_block_invoke.210
- ___73-[BRCXPCRegularIPCsClient(FPFSAdditions) getCKRecordIDsForFPItems:reply:]_block_invoke.214
- ___75-[BRCXPCRegularIPCsClient(FPFSAdditions) getFPItemIDsForCKRecordIDs:reply:]_block_invoke.215
- ___79-[BRCBGSystemTaskManager submitBGSystemTaskWithIdentifier:configuration:block:]_block_invoke.33
- ___79-[BRCBGSystemTaskManager submitBGSystemTaskWithIdentifier:configuration:block:]_block_invoke.33.cold.1
- ___79-[BRCBGSystemTaskManager submitBGSystemTaskWithIdentifier:configuration:block:]_block_invoke.33.cold.2
- ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.60
- ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.61
- ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.61.cold.1
- ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.62
- ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.63
- ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.64
- ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.64.cold.1
- ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.65
- ___82-[BRCAccountsManager _scheduleExistingFileProviderDomainsMaintenanceWithAccounts:]_block_invoke.66
- ___83-[BRCAccountSession locateItemWithIdentifier:zoneName:ownerName:completionHandler:]_block_invoke.489
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.430
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.430.cold.1
- ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerSaltingKeysAtItemIdentifier:reply:]_block_invoke.197
- ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerSaltingKeysAtItemIdentifier:reply:]_block_invoke.203
- ___86-[BRCAccountSession(BRCDatabaseManager) openDBForNewDomain:deviceIDChanged:withError:]_block_invoke
- ___86-[BRCAccountSession(BRCDatabaseManager) openDBForNewDomain:deviceIDChanged:withError:]_block_invoke_2
- ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) checkIfItemIsShareableWithItemIdentifier:reply:]_block_invoke.177
- ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) startOperation:toWaitForFPFSMigrationWithReply:]_block_invoke.184
- ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getCreatorNameComponentsForItemIdentifier:reply:]_block_invoke.178
- ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerContentSignatureAtItemIdentifier:reply:]_block_invoke.204
- ___97-[BRCXPCRegularIPCsClient(FPFSAdditions) getClientSaltingVerificationKeysAtItemIdentifier:reply:]_block_invoke.189
- ___99-[BRCAccountSession learnNewItemIdentifier:forItemIdentifier:zoneName:ownerName:completionHandler:]_block_invoke.487
- ___block_descriptor_48_e8_32s40s_e8_v12?0B8ls32l8s40l8
- ___block_literal_global.104
- ___block_literal_global.1051
- ___block_literal_global.112
- ___block_literal_global.126
- ___block_literal_global.183
- ___block_literal_global.203
- ___block_literal_global.205
- ___block_literal_global.244
- ___block_literal_global.249
- ___block_literal_global.27
- ___block_literal_global.302
- ___block_literal_global.310
- ___block_literal_global.317
- ___block_literal_global.324
- ___block_literal_global.369
- ___block_literal_global.377
- ___block_literal_global.389
- ___block_literal_global.401
- ___block_literal_global.435
- ___block_literal_global.57
- ___block_literal_global.80
- ___block_literal_global.85
- ___block_literal_global.87
- _objc_msgSend$_cancelSyncTasks:scheduler:
- _objc_msgSend$_checkIntegrity:serverTruth:session:skipControlFiles:dbCreationDate:deviceIDChanged:error:
- _objc_msgSend$_registerLastBootIfNeeded:table:skipControlFiles:dbCreationDate:deviceIDChanged:
- _objc_msgSend$cancelTaskRequestWithIdentifier:
- _objc_msgSend$cleanNamedThrottleTable:
- _objc_msgSend$garbageCollectAllDanglingSyncTasks
- _objc_msgSend$markLatestSyncRequestFailedInZone:
- _objc_msgSend$matchDomainWithAccountAndStampDomainIfNeeded:withAccounts:persistDomain:
- _objc_msgSend$openAndValidateDatabase:serverTruth:initialVersion:lastCurrentVersion:deviceIDChanged:error:
- _objc_msgSend$openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:deviceIDChanged:error:
- _objc_msgSend$openDBForNewDomain:deviceIDChanged:withError:
- _objc_msgSend$runningActivities
- _objc_msgSend$scheduler
- _objc_msgSend$submitTaskRequestWithIdentifier:descriptor:completionHandler:
- _objc_msgSend$submittedActivities
- _objc_msgSend$unregisterSystemTaskWithIdentifier:completionHandler:
- _xpc_dictionary_create
CStrings:
+ "+ sync status:           %@"
+ "+[BRCAccountSession(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:dbCreationDate:options:error:]"
+ "+[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:skipControlFiles:dbCreationDate:options:]"
+ "+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:options:error:]"
+ "+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:options:error:]_block_invoke"
+ "+[BRCSyncEngineMigrationTelemetryManager _calculateSyncStatusWithDBFacade:zoneAppRetriever:]"
+ "+[BRCSyncEngineMigrationTelemetryManager _calculateSyncStatusWithDBFacade:zoneAppRetriever:]_block_invoke"
+ "-[BRCAccountSession(BRCDatabaseManager) openDBForNewDomain:options:withError:]"
+ "-[BRCAccountsManager _sendTapToRadarForDomainMatchingError:forDomains:]"
+ "-[BRCLocalItem markLatestSyncRequestFailedInZone:shouldBackoff:]"
+ "-[BRCSQLNamedThrottleManager cleanNamedThrottleTable]"
+ "-[BRCSQLNamedThrottleManager throttle:subCategory:withRules:onQueue:block:]_block_invoke"
+ "-[BRCUserDefaultsNamedThrottleManager cleanNamedThrottleTable]_block_invoke"
+ "-[BRCUserDefaultsNamedThrottleManager throttle:subCategory:withRules:onQueue:block:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) copyStructureRecordIDForItemIdentifier:reply:]"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) copyStructureRecordIDForItemIdentifier:reply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) getStructureRecordIDsForFPItems:reply:]"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) getStructureRecordIDsForFPItems:reply:]_block_invoke"
+ "@\"<BRCNamedThrottling>\""
+ "@\"<BRCNamedThrottling>\"16@0:8"
+ "@\"NSUserDefaults\""
+ "B36@0:8B16^Q20^@28"
+ "B60@0:8@16B24^I28^I36^Q44^@52"
+ "B64@0:8@16B24@28B36^@40^Q48^@56"
+ "B88@0:8@16B24@28@36B44^I48^I56^@64^Q72^@80"
+ "BRCNamedThrottling"
+ "BRCSQLNamedThrottleManager"
+ "BRCSyncEngineMigrationTelemetryManager"
+ "BRCUserDefaultsNamedThrottleManager"
+ "During domain maintenance we encountered an unexpected state"
+ "Failure during domain maintenance on load time"
+ "SELECT 1 FROM client_items AS ci WHERE item_processing_stamp IS NOT NULL and version_old_zone_item_id IS NULL AND item_state == 1 AND %@ != (SELECT cz.zone_owner FROM client_zones AS cz WHERE cz.rowid = ci.zone_rowid) LIMIT 1"
+ "SELECT 1 FROM client_items AS ci WHERE item_processing_stamp IS NOT NULL and version_old_zone_rowid IS NOT NULL AND %@ != (SELECT cz.zone_owner FROM client_zones AS cz WHERE cz.rowid = ci.zone_rowid) LIMIT 1"
+ "SELECT 1 FROM client_items WHERE item_localsyncupstate != 0 AND item_localsyncupstate == 3 LIMIT 1"
+ "SELECT 1 FROM client_items WHERE item_localsyncupstate != 0 AND item_localsyncupstate == 4 AND NOT item_id_is_documents(item_id) LIMIT 1"
+ "SELECT 1 FROM client_items WHERE item_localsyncupstate != 0 AND item_localsyncupstate == 8 LIMIT 1"
+ "SELECT 1 FROM client_items WHERE item_processing_stamp IS NOT NULL and version_old_zone_item_id IS NULL AND item_state == 1 LIMIT 1"
+ "SELECT 1 FROM client_items WHERE item_processing_stamp IS NOT NULL and version_old_zone_rowid IS NOT NULL LIMIT 1"
+ "SELECT COUNT(*) FROM client_items WHERE item_localsyncupstate != 0 AND NOT item_id_is_documents(item_id)"
+ "SELECT COUNT(*) FROM client_items WHERE item_localsyncupstate != 0 AND item_localsyncupstate == 4 AND item_state = 1 AND NOT item_id_is_documents(item_id) LIMIT 1"
+ "SELECT COUNT(*) FROM client_items WHERE item_localsyncupstate != 0 AND item_localsyncupstate == 4 AND version_old_zone_rowid IS NOT NULL AND NOT item_id_is_documents(item_id) LIMIT 1"
+ "SELECT DISTINCT throttle_state FROM client_sync_up AS su INNER JOIN client_items AS li ON su.throttle_id = li.rowid  AND su.throttle_state != 0 AND NOT item_id_is_documents(li.item_id)"
+ "SELECT DISTINCT throttle_state FROM client_uploads"
+ "SYNC_ENGINE_V1_STATUS"
+ "T@\"<BRCNamedThrottling>\",R,N"
+ "[DEBUG] Calculated sync status bit mask: %@%@"
+ "[DEBUG] Cleaning named throttler from user defaults%@"
+ "[DEBUG] Cleared %lu throttle history records from user defaults%@"
+ "[ERROR] === DOMAIN VOLUME UUID ERROR - DIAGNOSTIC REPORT ===%@"
+ "[ERROR] === END DIAGNOSTIC REPORT ===%@"
+ "[ERROR] Domain User Info: %@%@"
+ "[ERROR] Domain: %@%@"
+ "[ERROR] Error: %@%@"
+ "[ERROR] Package manifest item path escapes stage directory: %@%@"
+ "[WARNING] Found resetting zone: %@%@"
+ "_calculateSyncStatusWithDBFacade:zoneAppRetriever:"
+ "_checkIntegrity:serverTruth:session:skipControlFiles:dbCreationDate:options:error:"
+ "_describeSyncStatus:"
+ "_getMaxLastRunForThrottle:fromData:"
+ "_getRecordForThrottle:subCategory:fromData:"
+ "_getThrottleData"
+ "_keyForThrottle:subCategory:"
+ "_registerLastBootIfNeeded:table:skipControlFiles:dbCreationDate:options:"
+ "_saveRecord:forThrottle:subCategory:inData:"
+ "_saveThrottleData:"
+ "_sendTapToRadarForDomainMatchingError:forDomains:"
+ "_serialQueue"
+ "_structureRecordIDForItem"
+ "_updateMaxLastRun:forThrottle:inData:"
+ "account-session.should-send-sync-engine-telemetry"
+ "allowSameBuild"
+ "bird.limit-pkg-item-paths-in-pkg-reader"
+ "brc_addPartialError:forFileProviderItemIdentifier:toError:"
+ "cleanNamedThrottleTable"
+ "collectSyncEngineTelemetryIfNeededWithSessionContext:osWasUpgraded:"
+ "com.apple.clouddocs.namedThrottle.data"
+ "com.apple.clouddocs.userdefaults-throttle"
+ "copyStructureRecordIDForItemIdentifier:reply:"
+ "crossZoneMoveNeedsSyncUp"
+ "crossZoneMoveNeedsSyncUpMoreThan100"
+ "crossZoneMoveNeedsSyncUpMoreThan1000"
+ "crossZoneMoveNeedsSyncUpMoreThan10000"
+ "dictionaryForKey:"
+ "expiration"
+ "failed maintaining domains"
+ "getStructureRecordIDsForFPItems:reply:"
+ "getSyncStatusBitMask"
+ "initWithUserDefaults:"
+ "itemsNeedSyncUp"
+ "itemsNeedUpload"
+ "lastRun"
+ "limitPackageItemPathsUnderPackageRootInPackageReader"
+ "markLatestSyncRequestFailedInZone:shouldBackoff:"
+ "matchDomainWithAccountAndStampDomainIfNeeded:withAccounts:persistDomain:error:"
+ "maxLastRuns"
+ "newSyncEngineV1StatusEventWithValue:"
+ "nonIdleItems"
+ "nonIdleItemsMoreThan100"
+ "nonIdleItemsMoreThan1000"
+ "nonIdleItemsMoreThan10000"
+ "openAndValidateDatabase:serverTruth:initialVersion:lastCurrentVersion:options:error:"
+ "openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:options:error:"
+ "openDBForNewDomain:options:withError:"
+ "osVersion"
+ "recursiveCrossZoneMoveInFlight"
+ "recursiveDeleteInFlight"
+ "recursiveOpInSharedToMeZone"
+ "requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:"
+ "shouldSendSyncEngineTelemetry"
+ "syncStatusDescriptionWithDBFacade:zoneAppRetriever:"
+ "syncUpSuspendedForError"
+ "syncUpSuspendedForIneligible"
+ "tombstoneNeedsSyncUp"
+ "tombstoneNeedsSyncUpMoreThan100"
+ "tombstoneNeedsSyncUpMoreThan1000"
+ "tombstoneNeedsSyncUpMoreThan10000"
+ "tooDeepHierarchy"
+ "uploadSuspendedForDataProtectionClass"
+ "uploadSuspendedForFailure"
+ "uploadSuspendedForNoNetwork"
+ "uploadSuspendedForQuota"
+ "uploadSuspendedForSize"
+ "uploadSuspendedForVerifyTerms"
+ "v24@0:8@\"BRCDumpContext\"16"
+ "v40@0:8q16@24@32"
+ "v52@0:8@16@24B32^@36^Q44"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@\"NSObject<OS_dispatch_queue>\"40@?<v@?@\"NSError\">48"
+ "zoneResetInFlight"
- "+[BRCAccountSession(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:dbCreationDate:deviceIDChanged:error:]"
- "+[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:skipControlFiles:dbCreationDate:deviceIDChanged:]"
- "+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:deviceIDChanged:error:]"
- "+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:deviceIDChanged:error:]_block_invoke"
- "-[BRCAccountSession(BRCDatabaseManager) openDBForNewDomain:deviceIDChanged:withError:]"
- "-[BRCBGSystemTaskManager _cancelSyncTasks:scheduler:]"
- "-[BRCBGSystemTaskManager garbageCollectAllDanglingSyncTasks]"
- "-[BRCLocalItem markLatestSyncRequestFailedInZone:]"
- "-[BRCNamedThrottleManager cleanNamedThrottleTable:]"
- "-[BRCNamedThrottleManager throttle:subCategory:withRules:onQueue:block:]_block_invoke"
- "@\"BRCNamedThrottleManager\""
- "@\"BRCNamedThrottleManager\"16@0:8"
- "B36@0:8B16^B20^@28"
- "B60@0:8@16B24^I28^I36^B44^@52"
- "B64@0:8@16B24@28B36^@40^B48^@56"
- "B88@0:8@16B24@28@36B44^I48^I56^@64^B72^@80"
- "BRCNamedThrottleManager"
- "T@\"BRCNamedThrottleManager\",R,N"
- "[DEBUG] Going to list all the submitted tasks from DAS and unregister old tasks from last bird run%@"
- "[DEBUG] Unregistering task with ID: %@%@"
- "_cancelSyncTasks:scheduler:"
- "_checkIntegrity:serverTruth:session:skipControlFiles:dbCreationDate:deviceIDChanged:error:"
- "_registerLastBootIfNeeded:table:skipControlFiles:dbCreationDate:deviceIDChanged:"
- "cancelTaskRequestWithIdentifier:"
- "cleanNamedThrottleTable:"
- "com.apple.bird.bgst."
- "garbageCollectAllDanglingSyncTasks"
- "markLatestSyncRequestFailedInZone:"
- "matchDomainWithAccountAndStampDomainIfNeeded:withAccounts:persistDomain:"
- "openAndValidateDatabase:serverTruth:initialVersion:lastCurrentVersion:deviceIDChanged:error:"
- "openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:deviceIDChanged:error:"
- "openDBForNewDomain:deviceIDChanged:withError:"
- "requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:additionalDevices:triggerRootCause:"
- "runningActivities"
- "submitTaskRequestWithIdentifier:descriptor:completionHandler:"
- "submittedActivities"
- "unregisterSystemTaskWithIdentifier:completionHandler:"
- "v52@0:8@16@24B32^@36^B44"

```
