## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-4257.2.1.0.0
-  __TEXT.__text: 0x30e5fc
-  __TEXT.__auth_stubs: 0x1ac0
-  __TEXT.__objc_methlist: 0x1a034
+4257.40.32.502.1
+  __TEXT.__text: 0x31012c
+  __TEXT.__auth_stubs: 0x1b40
+  __TEXT.__objc_methlist: 0x1a18c
   __TEXT.__const: 0x500
-  __TEXT.__cstring: 0x7d217
-  __TEXT.__oslogstring: 0x3bf5b
-  __TEXT.__gcc_except_tab: 0x1a3ac
+  __TEXT.__cstring: 0x7d4f9
+  __TEXT.__oslogstring: 0x3c0f3
+  __TEXT.__gcc_except_tab: 0x1a464
   __TEXT.__ustring: 0x88
-  __TEXT.__unwind_info: 0x9f08
-  __TEXT.__objc_classname: 0x2a9d
-  __TEXT.__objc_methname: 0x441c0
-  __TEXT.__objc_methtype: 0x8fc6
-  __TEXT.__objc_stubs: 0x2ee60
-  __DATA_CONST.__got: 0x16f8
+  __TEXT.__unwind_info: 0x9f50
+  __TEXT.__objc_classname: 0x2acb
+  __TEXT.__objc_methname: 0x444b0
+  __TEXT.__objc_methtype: 0x900f
+  __TEXT.__objc_stubs: 0x2f0c0
+  __DATA_CONST.__got: 0x1720
   __DATA_CONST.__const: 0x95c8
-  __DATA_CONST.__objc_classlist: 0xa50
+  __DATA_CONST.__objc_classlist: 0xa60
   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x288
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe600
+  __DATA_CONST.__objc_selrefs: 0xe6a0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x910
+  __DATA_CONST.__objc_superrefs: 0x920
   __DATA_CONST.__objc_arraydata: 0xe40
-  __AUTH_CONST.__auth_got: 0xd70
-  __AUTH_CONST.__const: 0x2b80
-  __AUTH_CONST.__cfstring: 0x228c0
-  __AUTH_CONST.__objc_const: 0x3cfa0
+  __AUTH_CONST.__auth_got: 0xdb0
+  __AUTH_CONST.__const: 0x2b60
+  __AUTH_CONST.__cfstring: 0x22960
+  __AUTH_CONST.__objc_const: 0x3d220
   __AUTH_CONST.__objc_intobj: 0xba0
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x50
-  __AUTH.__objc_data: 0x2800
+  __AUTH.__objc_data: 0x28a0
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x1f84
+  __DATA.__objc_ivar: 0x1fa4
   __DATA.__data: 0x2740
   __DATA.__bss: 0x208
   __DATA_DIRTY.__objc_data: 0x3f20
   __DATA_DIRTY.__data: 0xd0
-  __DATA_DIRTY.__bss: 0x408
+  __DATA_DIRTY.__bss: 0x3f8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0D585642-3C46-37C6-A6F2-5BB3E18593E4
-  Functions: 13546
-  Symbols:   44091
-  CStrings:  27637
+  UUID: E66D3460-3419-33B8-A91A-2353426B8254
+  Functions: 13580
+  Symbols:   44215
+  CStrings:  27701
 
Symbols:
+ +[BRCSharedServerChangeState supportsSecureCoding]
+ +[BRCSystemResourcesManager _fetchBundleIDsFromAppRegisteredNotificationWithXPCEvent:]
+ +[BRCSystemResourcesManager _fetchBundleIDsFromAppRegisteredNotificationWithXPCEvent:].cold.1
+ +[BRCSystemResourcesManager _fetchBundleIDsFromAppRegisteredNotificationWithXPCEvent:].cold.2
+ +[BRCSystemResourcesManager _fetchBundleIDsFromAppRegisteredNotificationWithXPCEvent:].cold.3
+ +[BRCSystemResourcesManager _fetchBundleIDsFromAppRegisteredNotificationWithXPCEvent:].cold.4
+ -[BRCClientZone(BRCZoneReset) _finishedReset:signpostTracker:completionHandler:]
+ -[BRCCloudDocsAppsMonitor _refetchPendingApps]
+ -[BRCCloudDocsAppsMonitor _updateMappingsAndNotifyObservers:appIDsByAppLibraryID:markInitialFetch:]
+ -[BRCCloudDocsAppsMonitor appListDidUpdateForBundleIDs:]
+ -[BRCCloudDocsAppsMonitor appListDidUpdateForBundleIDs:].cold.1
+ -[BRCPQLConnection fetchWithExpectedIndex:sql:]
+ -[BRCPQLConnection fetchWithExpectedIndex:sql:].cold.1
+ -[BRCPeriodicSyncInvestigation completeInvestigation]
+ -[BRCPeriodicSyncInvestigation completeInvestigation].cold.1
+ -[BRCPeriodicSyncInvestigation completeInvestigation].cold.2
+ -[BRCServerZone _shouldSendNotification]
+ -[BRCServerZone _shouldSendNotification].cold.1
+ -[BRCServerZone plist].cold.1
+ -[BRCSharedServerChangeState copyWithZone:]
+ -[BRCSharedServerChangeState descriptionWithContext:]
+ -[BRCSharedServerChangeState encodeWithCoder:]
+ -[BRCSharedServerChangeState everCaughtUp]
+ -[BRCSharedServerChangeState forgetChangeTokens]
+ -[BRCSharedServerChangeState initWithCoder:]
+ -[BRCSharedServerChangeState initWithServerSyncState:]
+ -[BRCSharedServerChangeState newlyCreatedDuringInitialSync]
+ -[BRCSharedServerChangeState setEverCaughtUp:]
+ -[BRCSharedServerChangeState setNewlyCreatedDuringInitialSync:]
+ -[BRCSharedServerChangeState updateWithServerChangeToken:clientRequestID:caughtUp:]
+ -[BRCSignpostTracker .cxx_destruct]
+ -[BRCSignpostTracker _startSignpostEvent]
+ -[BRCSignpostTracker dealloc]
+ -[BRCSignpostTracker dealloc].cold.1
+ -[BRCSignpostTracker endSignpostEvent]
+ -[BRCSignpostTracker initWithLabel:]
+ -[BRCSystemResourcesManager _handleAppsMonitorXPCEvent:]
+ -[BRCSystemResourcesManager _handleAppsMonitorXPCEvent:].cold.1
+ -[BRCUserDefaults signpostEnabled]
+ -[BRCUserDefaults supportsIncrementalAppsMonitoring]
+ GCC_except_table572
+ _BREntitledContainerIdentifiersForPropertyList
+ _OBJC_CLASS_$_BRCSharedServerChangeState
+ _OBJC_CLASS_$_BRCSignpostTracker
+ _OBJC_IVAR_$_BRCCloudDocsAppsMonitor._incrementalRefetchPacer
+ _OBJC_IVAR_$_BRCCloudDocsAppsMonitor._pendingBundleIDsToRefetch
+ _OBJC_IVAR_$_BRCSharedServerChangeState._everCaughtUp
+ _OBJC_IVAR_$_BRCSharedServerChangeState._newlyCreatedDuringInitialSync
+ _OBJC_IVAR_$_BRCSignpostTracker._ended
+ _OBJC_IVAR_$_BRCSignpostTracker._label
+ _OBJC_IVAR_$_BRCSignpostTracker._log
+ _OBJC_IVAR_$_BRCSignpostTracker._sid
+ _OBJC_METACLASS_$_BRCSharedServerChangeState
+ _OBJC_METACLASS_$_BRCSignpostTracker
+ __OBJC_$_CLASS_METHODS_BRCSharedServerChangeState
+ __OBJC_$_INSTANCE_METHODS_BRCSharedServerChangeState
+ __OBJC_$_INSTANCE_METHODS_BRCSignpostTracker
+ __OBJC_$_INSTANCE_VARIABLES_BRCSharedServerChangeState
+ __OBJC_$_INSTANCE_VARIABLES_BRCSignpostTracker
+ __OBJC_$_PROP_LIST_BRCSharedServerChangeState
+ __OBJC_CLASS_RO_$_BRCSharedServerChangeState
+ __OBJC_CLASS_RO_$_BRCSignpostTracker
+ __OBJC_METACLASS_RO_$_BRCSharedServerChangeState
+ __OBJC_METACLASS_RO_$_BRCSignpostTracker
+ ___120-[BRCAccountSession _recoverContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:]_block_invoke.222
+ ___148-[BRCServerZone didSyncDownRequestID:serverChangeToken:editedRecords:deletedRecordIDs:deletedShareRecordIDs:allocRankZones:caughtUp:pendingChanges:]_block_invoke.255
+ ___26-[BRCAccountSession close]_block_invoke.299
+ ___31-[BRCCloudDocsAppsMonitor init]_block_invoke_2
+ ___37-[BRCAccountSession destroyLocalData]_block_invoke.321
+ ___37-[BRCAccountSession destroyLocalData]_block_invoke.321.cold.1
+ ___39-[BRCCloudDocsAppsMonitor addObserver:]_block_invoke_2
+ ___39-[BRCServerZone collectTombstoneRanks:]_block_invoke.269
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.266
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.270
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.283
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.269
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.269.cold.1
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.271
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.271.cold.1
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_3.275
+ ___43-[BRCAccountSession _reportBasehashSalting]_block_invoke.204
+ ___43-[BRCAccountSession _reportBasehashSalting]_block_invoke.204.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.323
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.323.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.323.cold.2
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.323.cold.3
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.323.cold.4
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.330.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.333
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.355
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.355.cold.1
+ ___46-[BRCCloudDocsAppsMonitor _refetchPendingApps]_block_invoke
+ ___49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.517
+ ___50-[BRCServerZone _updateParticipantsTableForShare:]_block_invoke.186
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.245
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.245.cold.1
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.245.cold.2
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.245.cold.3
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.245.cold.4
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.249
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.259
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.259.cold.1
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.259.cold.2
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.259.cold.3
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.259.cold.4
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.263
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.246
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.253
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.253.cold.1
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.253.cold.2
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.253.cold.3
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.253.cold.4
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.260
+ ___56-[BRCCloudDocsAppsMonitor appListDidUpdateForBundleIDs:]_block_invoke
+ ___57-[BRCNotificationManager hasWatcherMatchingGlobalItemID:]_block_invoke
+ ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.368
+ ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.369
+ ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.136
+ ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.136.cold.1
+ ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.136.cold.2
+ ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.143
+ ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.148
+ ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.148.cold.1
+ ___66-[BRCAccountSession setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke.385
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.78
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.78.cold.1
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.80
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.80.cold.1
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.81
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.81.cold.1
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.85
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.85.cold.1
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.85.cold.2
+ ___68-[BRCAccountSession(BRCZoneMigration) scheduleZoneMovesToCloudDocs:]_block_invoke.83
+ ___68-[BRCAccountSession(BRCZoneMigration) scheduleZoneMovesToCloudDocs:]_block_invoke_2.84
+ ___75+[NSString(BRCPathAdditions) br_currentMobileDocumentsDirWithRefreshCache:]_block_invoke.15
+ ___75+[NSString(BRCPathAdditions) br_currentMobileDocumentsDirWithRefreshCache:]_block_invoke.15.cold.1
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.738
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.742
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.740
+ ___80-[BRCClientZone(BRCZoneReset) _finishedReset:signpostTracker:completionHandler:]_block_invoke
+ ___80-[BRCClientZone(BRCZoneReset) _finishedReset:signpostTracker:completionHandler:]_block_invoke.46
+ ___80-[BRCClientZone(BRCZoneReset) _finishedReset:signpostTracker:completionHandler:]_block_invoke_2
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.361
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.361.cold.1
+ ___84-[BRCApplyScheduler _recoverAndReportMissingJobsWithCompletion:report:recoveryTask:]_block_invoke.146
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.100
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.100.cold.1
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.100.cold.2
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.101
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.101.cold.1
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.103
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.96
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.96.cold.1
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.96.cold.2
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.97
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.97.cold.1
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.97.cold.2
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.98
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.98.cold.1
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.98.cold.2
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.99
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.99.cold.1
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.99.cold.2
+ ___86+[BRCSystemResourcesManager _fetchBundleIDsFromAppRegisteredNotificationWithXPCEvent:]_block_invoke
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.670
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.670.cold.1
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.674.cold.1
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.674.cold.2
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.676
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.677
+ ___99-[BRCCloudDocsAppsMonitor _updateMappingsAndNotifyObservers:appIDsByAppLibraryID:markInitialFetch:]_block_invoke
+ ___99-[BRCCloudDocsAppsMonitor _updateMappingsAndNotifyObservers:appIDsByAppLibraryID:markInitialFetch:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e36_B24?0Q8"NSObject<OS_xpc_object>"16ls32l8
+ ___block_literal_global.193
+ ___block_literal_global.194
+ ___block_literal_global.240
+ ___block_literal_global.255
+ ___block_literal_global.262
+ ___block_literal_global.301
+ ___block_literal_global.308
+ ___block_literal_global.320
+ ___block_literal_global.332
+ ___block_literal_global.366
+ ___block_literal_global.763
+ ___block_literal_global.945
+ __os_signpost_emit_with_name_impl
+ __xpc_type_array
+ __xpc_type_dictionary
+ __xpc_type_string
+ _brc_signpost_log
+ _objc_msgSend$_fetchBundleIDsFromAppRegisteredNotificationWithXPCEvent:
+ _objc_msgSend$_finishedReset:signpostTracker:completionHandler:
+ _objc_msgSend$_handleAppsMonitorXPCEvent:
+ _objc_msgSend$_refetchPendingApps
+ _objc_msgSend$_shouldSendNotification
+ _objc_msgSend$_startSignpostEvent
+ _objc_msgSend$_updateMappingsAndNotifyObservers:appIDsByAppLibraryID:markInitialFetch:
+ _objc_msgSend$allowsAccessRequests
+ _objc_msgSend$appListDidUpdateForBundleIDs:
+ _objc_msgSend$bundleRecordWithBundleIdentifier:allowPlaceholder:error:
+ _objc_msgSend$cachesDirForCurrentPersona
+ _objc_msgSend$completeInvestigation
+ _objc_msgSend$endSignpostEvent
+ _objc_msgSend$everCaughtUp
+ _objc_msgSend$fetchWithExpectedIndex:sql:
+ _objc_msgSend$initWithCString:encoding:
+ _objc_msgSend$initWithLabel:
+ _objc_msgSend$newlyCreatedDuringInitialSync
+ _objc_msgSend$setEverCaughtUp:
+ _objc_msgSend$setNewlyCreatedDuringInitialSync:
+ _objc_msgSend$signpostEnabled
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$supportsIncrementalAppsMonitoring
+ _os_signpost_enabled
+ _os_signpost_id_generate
+ _xpc_array_apply
+ _xpc_dictionary_get_value
+ _xpc_string_get_string_ptr
- +[BRCSharingUtil openApplicationForURL:completionHandler:]
- +[NSString(BRCPathAdditions) brc_currentCachesDir].cold.1
- -[BRCClientZone(BRCZoneReset) _finishedReset:completionHandler:]
- -[BRCPeriodicSyncInvestigation completeInvestigationIfNecessary].cold.1
- -[BRCPeriodicSyncInvestigation completeInvestigationIfNecessary].cold.2
- GCC_except_table118
- GCC_except_table570
- ___120-[BRCAccountSession _recoverContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:]_block_invoke.219
- ___126-[BRCUserNotificationRequestAccessApprovedRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.193
- ___126-[BRCUserNotificationRequestAccessApprovedRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.193.cold.1
- ___126-[BRCUserNotificationRequestAccessApprovedRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.194
- ___148-[BRCServerZone didSyncDownRequestID:serverChangeToken:editedRecords:deletedRecordIDs:deletedShareRecordIDs:allocRankZones:caughtUp:pendingChanges:]_block_invoke.248
- ___26-[BRCAccountSession close]_block_invoke.296
- ___37-[BRCAccountSession destroyLocalData]_block_invoke.318
- ___37-[BRCAccountSession destroyLocalData]_block_invoke.318.cold.1
- ___39-[BRCCloudDocsAppsMonitor _refetchApps]_block_invoke.17
- ___39-[BRCCloudDocsAppsMonitor _refetchApps]_block_invoke_2
- ___39-[BRCCloudDocsAppsMonitor addObserver:]_block_invoke.19
- ___39-[BRCServerZone collectTombstoneRanks:]_block_invoke.262
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.263
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.264
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.280
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.266
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.266.cold.1
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.268
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.268.cold.1
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_3.272
- ___43-[BRCAccountSession _reportBasehashSalting]_block_invoke.201
- ___43-[BRCAccountSession _reportBasehashSalting]_block_invoke.201.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.320
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.320.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.320.cold.2
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.320.cold.3
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.320.cold.4
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.327
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.327.cold.1
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.352
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.352.cold.1
- ___49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.514
- ___50+[NSString(BRCPathAdditions) brc_currentCachesDir]_block_invoke
- ___50-[BRCServerZone _updateParticipantsTableForShare:]_block_invoke.179
- ___50-[BRCSystemResourcesManager _initAppListObservers]_block_invoke.cold.1
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.242
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.242.cold.1
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.242.cold.2
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.242.cold.3
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.242.cold.4
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.246
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.256
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.256.cold.1
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.256.cold.2
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.256.cold.3
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.256.cold.4
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.260
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.243
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.250
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.250.cold.1
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.250.cold.2
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.250.cold.3
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.250.cold.4
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.257
- ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.365
- ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.366
- ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.145
- ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.145.cold.1
- ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.145.cold.2
- ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.152
- ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.157
- ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.157.cold.1
- ___64-[BRCClientZone(BRCZoneReset) _finishedReset:completionHandler:]_block_invoke
- ___64-[BRCClientZone(BRCZoneReset) _finishedReset:completionHandler:]_block_invoke.45
- ___64-[BRCClientZone(BRCZoneReset) _finishedReset:completionHandler:]_block_invoke_2
- ___66-[BRCAccountSession setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke.382
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.87
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.87.cold.1
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.89
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.89.cold.1
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.90
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.90.cold.1
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.94
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.94.cold.1
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.94.cold.2
- ___68-[BRCAccountSession(BRCZoneMigration) scheduleZoneMovesToCloudDocs:]_block_invoke.81
- ___68-[BRCAccountSession(BRCZoneMigration) scheduleZoneMovesToCloudDocs:]_block_invoke_2.82
- ___75+[NSString(BRCPathAdditions) br_currentMobileDocumentsDirWithRefreshCache:]_block_invoke.23
- ___75+[NSString(BRCPathAdditions) br_currentMobileDocumentsDirWithRefreshCache:]_block_invoke.23.cold.1
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.735
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.739
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.737
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.358
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.358.cold.1
- ___84-[BRCApplyScheduler _recoverAndReportMissingJobsWithCompletion:report:recoveryTask:]_block_invoke.145
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.105
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.105.cold.1
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.105.cold.2
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.106
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.106.cold.1
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.106.cold.2
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.107
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.107.cold.1
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.107.cold.2
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.108
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.108.cold.1
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.108.cold.2
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.109
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.109.cold.1
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.109.cold.2
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.110
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.110.cold.1
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.112
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.667
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.667.cold.1
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.668
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.671.cold.1
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.671.cold.2
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.673
- ___block_descriptor_64_e8_32s40s48s56bs_e27_v24?0"NSURL"8"NSError"16ls32l8s56l8s40l8s48l8
- ___block_literal_global.196
- ___block_literal_global.245
- ___block_literal_global.246
- ___block_literal_global.252
- ___block_literal_global.259
- ___block_literal_global.298
- ___block_literal_global.317
- ___block_literal_global.329
- ___block_literal_global.363
- ___block_literal_global.760
- ___block_literal_global.942
- _brc_currentCachesDir.once
- _brc_currentCachesDir.pathByPersonaID
- _objc_msgSend$_finishedReset:completionHandler:
- _objc_msgSend$br_pathRelativeToDirectory:
- _objc_msgSend$openApplicationForURL:completionHandler:
- _objc_msgSend$showJoinDialogForDocumentName:url:ownerDisplayName:ckContainer:isPublicShare:reply:
CStrings:
+ "+[BRCSystemResourcesManager _fetchBundleIDsFromAppRegisteredNotificationWithXPCEvent:]"
+ ", ever-caught-up:%@"
+ ", newly-created-during-initial-sync:%@"
+ "-[BRCClientZone(BRCZoneReset) _finishedReset:signpostTracker:completionHandler:]"
+ "-[BRCClientZone(BRCZoneReset) _finishedReset:signpostTracker:completionHandler:]_block_invoke_2"
+ "-[BRCCloudDocsAppsMonitor _refetchPendingApps]"
+ "-[BRCCloudDocsAppsMonitor appListDidUpdateForBundleIDs:]"
+ "-[BRCPQLConnection fetchWithExpectedIndex:sql:]"
+ "-[BRCPeriodicSyncInvestigation completeInvestigation]"
+ "-[BRCServerZone _shouldSendNotification]"
+ "-[BRCServerZone plist]"
+ "-[BRCSignpostTracker dealloc]"
+ "-[BRCSystemResourcesManager _handleAppsMonitorXPCEvent:]"
+ "@\"BRCSharedServerChangeState\""
+ "@\"NSObject<OS_os_log>\""
+ "ApplyJobs"
+ "B24@?0Q8@\"NSObject<OS_xpc_object>\"16"
+ "BRCSharedServerChangeState"
+ "BRCSignpostTracker"
+ "INSERT INTO client_pkg_upload_items (item_rowid, rel_path, item_type, asset_rank, file_id, quarantine_info, xattr_signature, mtime, signature_or_link, generation, size, mode) VALUES (%llu, %@, %u, %llu, %llu, %@, %@, %llu, %@, %@, %llu, %u)"
+ "SELECT ci1.rowid, ci1.zone_rowid, ci1.item_id, ci1.item_creator_id, ci1.item_sharing_options, ci1.item_side_car_ckinfo, ci1.item_parent_zone_rowid, ci1.item_localsyncupstate, ci1.item_local_diffs, ci1.item_notifs_rank, ci1.app_library_rowid, ci1.item_min_supported_os_rowid, ci1.item_user_visible, ci1.item_stat_ckinfo, ci1.item_state, ci1.item_type, ci1.item_mode, ci1.item_birthtime, ci1.item_lastusedtime, ci1.item_favoriterank,ci1.item_parent_id, ci1.item_filename, ci1.item_hidden_ext, ci1.item_finder_tags, ci1.item_xattr_signature, ci1.item_trash_put_back_path, ci1.item_trash_put_back_parent_id, ci1.item_alias_target, ci1.item_creator, ci1.item_processing_stamp, ci1.item_bouncedname, ci1.item_scope, ci1.item_local_change_count, ci1.item_old_version_identifier, ci1.fp_creation_item_identifier, ci1.version_name, ci1.version_ckinfo, ci1.version_mtime, ci1.version_size, ci1.version_thumb_size, ci1.version_thumb_signature, ci1.version_content_signature, ci1.version_xattr_signature, ci1.version_edited_since_shared, ci1.version_device, ci1.version_conflict_loser_etags, ci1.version_quarantine_info, ci1.version_uploaded_assets, ci1.version_upload_error, ci1.version_old_zone_item_id, ci1.version_old_zone_rowid, ci1.version_local_change_count, ci1.version_old_version_identifier, ci1.item_live_conflict_loser_etags, ci1.item_file_id, ci1.item_generation FROM client_items AS ci1                             LEFT JOIN client_items AS ci2                             ON ci2.version_old_zone_item_id = ci1.item_id AND ci2.version_old_zone_rowid = ci1.zone_rowid                             WHERE ci2.version_old_zone_rowid IS NULL                               AND ci2.version_old_zone_item_id IS NULL                               AND ci1.item_state = -3                               AND ci1.item_localsyncupstate != 0                               AND ci1.item_type IN (0, 9, 10)"
+ "SELECT item_rowid, rel_path, item_type, asset_rank, file_id, quarantine_info, xattr_signature, mtime, signature_or_link, generation, size, mode  FROM client_pkg_upload_items  ORDER BY item_rowid, rel_path"
+ "SELECT item_rowid, rel_path, item_type, asset_rank, file_id, quarantine_info, xattr_signature, mtime, signature_or_link, generation, size, mode FROM client_pkg_upload_items WHERE item_rowid = %llu ORDER BY asset_rank"
+ "SELECT item_rowid, rel_path, item_type, asset_rank, file_id, quarantine_info, xattr_signature, mtime, signature_or_link, generation, size, mode FROM client_pkg_upload_items WHERE item_rowid = %llu ORDER BY rel_path"
+ "T@\"BRCSharedServerChangeState\",&,V_sharedDatabaseChangeState"
+ "TB,N,V_everCaughtUp"
+ "TB,N,V_newlyCreatedDuringInitialSync"
+ "UPDATE client_items SET item_min_supported_os_rowid = NULL  WHERE item_localsyncupstate = 4 AND item_localsyncupstate != 0"
+ "UserInfo"
+ "ZoneReset"
+ "[CRIT] API MISUSE: you need to provide an index%@"
+ "[CRIT] Assertion failed: _ended%@"
+ "[CRIT] Assertion failed: li%@"
+ "[CRIT] UNREACHABLE: shared zone should have share server state%@"
+ "[DEBUG] No bundleRecord found for bundle identifier %@ - treating as uninstalled app%@"
+ "[DEBUG] app list updated for bundle IDs: %@%@"
+ "[DEBUG] ┏%llx refetching specific apps: %@%@"
+ "[ERROR] UserInfo field is not a dictionary%@"
+ "[ERROR] UserInfo has no bundleIDs field%@"
+ "[ERROR] bundleIDs field is not an array%@"
+ "[ERROR] xpcEvent has no UserInfo field%@"
+ "_ended"
+ "_everCaughtUp"
+ "_fetchBundleIDsFromAppRegisteredNotificationWithXPCEvent:"
+ "_finishedReset:signpostTracker:completionHandler:"
+ "_handleAppsMonitorXPCEvent:"
+ "_incrementalRefetchPacer"
+ "_log"
+ "_newlyCreatedDuringInitialSync"
+ "_pendingBundleIDsToRefetch"
+ "_refetchPendingApps"
+ "_shouldSendNotification"
+ "_sid"
+ "_startSignpostEvent"
+ "_updateMappingsAndNotifyObservers:appIDsByAppLibraryID:markInitialFetch:"
+ "allowsAccessRequests"
+ "appListDidUpdateForBundleIDs:"
+ "apps-incremental-refetch-pacer"
+ "bird.supports-incremental-apps-monitoring"
+ "bundleIDs"
+ "bundleRecordWithBundleIdentifier:allowPlaceholder:error:"
+ "cachesDirForCurrentPersona"
+ "client_items/item_filename_path;client_items/item_parent_id__item_bouncedname"
+ "client_items/sync_state_job_recovery;client_items/version_old_zone_rowid"
+ "completeInvestigation"
+ "endSignpostEvent"
+ "everCaughtUp"
+ "fetchWithExpectedIndex:sql:"
+ "initWithCString:encoding:"
+ "initWithLabel:"
+ "newlyCreatedDuringInitialSync"
+ "rdar://157468592"
+ "rdar://157727651"
+ "setEverCaughtUp:"
+ "setNewlyCreatedDuringInitialSync:"
+ "signpost.enabled"
+ "signpostEnabled"
+ "stringWithString:"
+ "supportsIncrementalAppsMonitoring"
+ "v24@0:8@\"NSArray\"16"
- "+[NSString(BRCPathAdditions) brc_currentCachesDir]"
- "-[BRCClientZone(BRCZoneReset) _finishedReset:completionHandler:]"
- "-[BRCClientZone(BRCZoneReset) _finishedReset:completionHandler:]_block_invoke_2"
- "-[BRCPeriodicSyncInvestigation completeInvestigationIfNecessary]"
- "-[BRCSystemResourcesManager _initAppListObservers]_block_invoke"
- "Direct tombstones should not be created on iOS"
- "INSERT INTO client_pkg_upload_items (item_rowid, rel_path, item_type, asset_rank, file_id, quarantine_info, xattr_signature, mtime, generation, size, mode) VALUES (%llu, %@, %u, %llu, %llu, %@, %@, %llu, %@, %llu, %u)"
- "Library/Caches/com.apple.bird"
- "SELECT ci1.rowid, ci1.zone_rowid, ci1.item_id, ci1.item_creator_id, ci1.item_sharing_options, ci1.item_side_car_ckinfo, ci1.item_parent_zone_rowid, ci1.item_localsyncupstate, ci1.item_local_diffs, ci1.item_notifs_rank, ci1.app_library_rowid, ci1.item_min_supported_os_rowid, ci1.item_user_visible, ci1.item_stat_ckinfo, ci1.item_state, ci1.item_type, ci1.item_mode, ci1.item_birthtime, ci1.item_lastusedtime, ci1.item_favoriterank,ci1.item_parent_id, ci1.item_filename, ci1.item_hidden_ext, ci1.item_finder_tags, ci1.item_xattr_signature, ci1.item_trash_put_back_path, ci1.item_trash_put_back_parent_id, ci1.item_alias_target, ci1.item_creator, ci1.item_processing_stamp, ci1.item_bouncedname, ci1.item_scope, ci1.item_local_change_count, ci1.item_old_version_identifier, ci1.fp_creation_item_identifier, ci1.version_name, ci1.version_ckinfo, ci1.version_mtime, ci1.version_size, ci1.version_thumb_size, ci1.version_thumb_signature, ci1.version_content_signature, ci1.version_xattr_signature, ci1.version_edited_since_shared, ci1.version_device, ci1.version_conflict_loser_etags, ci1.version_quarantine_info, ci1.version_uploaded_assets, ci1.version_upload_error, ci1.version_old_zone_item_id, ci1.version_old_zone_rowid, ci1.version_local_change_count, ci1.version_old_version_identifier, ci1.item_live_conflict_loser_etags, ci1.item_file_id, ci1.item_generation FROM client_items AS ci1                             LEFT JOIN client_items AS ci2                             ON ci2.version_old_zone_item_id = ci1.item_id AND ci2.version_old_zone_rowid = ci1.zone_rowid                             WHERE ci2.version_old_zone_rowid IS NULL                               AND ci2.version_old_zone_item_id IS NULL                               AND ci1.item_state = -3                               AND ci1.item_type IN (0, 9, 10)"
- "SELECT item_rowid, rel_path, item_type, asset_rank, file_id, quarantine_info, xattr_signature, mtime, generation, size, mode  FROM client_pkg_upload_items  ORDER BY item_rowid, rel_path"
- "SELECT item_rowid, rel_path, item_type, asset_rank, file_id, quarantine_info, xattr_signature, mtime, generation, size, mode FROM client_pkg_upload_items WHERE item_rowid = %llu ORDER BY asset_rank"
- "SELECT item_rowid, rel_path, item_type, asset_rank, file_id, quarantine_info, xattr_signature, mtime, generation, size, mode FROM client_pkg_upload_items WHERE item_rowid = %llu ORDER BY rel_path"
- "T@\"BRCServerChangeState\",&,V_sharedDatabaseChangeState"
- "UPDATE client_items SET item_min_supported_os_rowid = NULL"
- "We received a delete request for a document scope item, which shouldn't occur in iOS."
- "[DEBUG] Error while displaying dialog %@%@"
- "[DEBUG] Got an error while openning app for URL %@ - %@%@"
- "[WARNING] No path for Caches directory%@"
- "_finishedReset:completionHandler:"
- "br_pathRelativeToDirectory:"
- "openApplicationForURL:completionHandler:"
- "rdar://151131525"
- "unexpected deletion"

```
