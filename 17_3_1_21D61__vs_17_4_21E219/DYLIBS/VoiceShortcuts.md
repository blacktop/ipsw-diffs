## VoiceShortcuts

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts`

```diff

-2302.0.5.0.0
-  __TEXT.__text: 0xdb3c4
-  __TEXT.__auth_stubs: 0x25a0
-  __TEXT.__objc_methlist: 0x4ccc
-  __TEXT.__const: 0x28f8
-  __TEXT.__cstring: 0xfdf5
-  __TEXT.__swift5_typeref: 0x1aad
-  __TEXT.__swift5_fieldmd: 0xdcc
-  __TEXT.__constg_swiftt: 0x1460
+2510.5.1.0.0
+  __TEXT.__text: 0xe065c
+  __TEXT.__auth_stubs: 0x2520
+  __TEXT.__objc_methlist: 0x4ebc
+  __TEXT.__const: 0x29f8
+  __TEXT.__cstring: 0x10825
+  __TEXT.__swift5_typeref: 0x1b11
+  __TEXT.__swift5_fieldmd: 0xe1c
+  __TEXT.__constg_swiftt: 0x14c8
   __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_reflstr: 0xd16
+  __TEXT.__swift5_reflstr: 0xd96
   __TEXT.__swift5_assocty: 0x378
   __TEXT.__swift5_protos: 0x3c
-  __TEXT.__swift5_proto: 0x23c
-  __TEXT.__swift5_types: 0x104
-  __TEXT.__swift5_capture: 0x590
+  __TEXT.__swift5_proto: 0x248
+  __TEXT.__swift5_types: 0x10c
+  __TEXT.__swift5_capture: 0x4c8
   __TEXT.__swift5_mpenum: 0x60
-  __TEXT.__gcc_except_tab: 0xe50
-  __TEXT.__oslogstring: 0xd24a
-  __TEXT.__dlopen_cstrs: 0x30f
+  __TEXT.__gcc_except_tab: 0xdf8
+  __TEXT.__oslogstring: 0xdbc0
+  __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0x44
-  __TEXT.__unwind_info: 0x3a7c
-  __TEXT.__eh_frame: 0x5410
-  __TEXT.__objc_classname: 0xd05
-  __TEXT.__objc_methname: 0x14e56
-  __TEXT.__objc_methtype: 0x4628
-  __TEXT.__objc_stubs: 0xf500
-  __DATA_CONST.__got: 0x730
-  __DATA_CONST.__const: 0x28c8
-  __DATA_CONST.__objc_classlist: 0x288
+  __TEXT.__unwind_info: 0x3984
+  __TEXT.__eh_frame: 0x52e8
+  __TEXT.__objc_classname: 0xd4a
+  __TEXT.__objc_methname: 0x159aa
+  __TEXT.__objc_methtype: 0x47b2
+  __TEXT.__objc_stubs: 0xff40
+  __DATA_CONST.__got: 0x778
+  __DATA_CONST.__const: 0x28f0
+  __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x160
-  __DATA_CONST.__objc_protolist: 0x248
+  __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9ce0
-  __DATA_CONST.__objc_selrefs: 0x47c0
+  __DATA_CONST.__objc_const: 0x9f18
+  __DATA_CONST.__objc_selrefs: 0x4a90
+  __DATA_CONST.__objc_protorefs: 0x88
+  __DATA_CONST.__objc_classrefs: 0xdc0
+  __DATA_CONST.__objc_superrefs: 0x1c8
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__const: 0x3738
-  __AUTH_CONST.__auth_ptr: 0x98
-  __AUTH_CONST.__objc_const: 0x2600
-  __AUTH_CONST.__cfstring: 0x4100
+  __AUTH_CONST.__const: 0x36e0
+  __AUTH_CONST.__auth_ptr: 0xa0
+  __AUTH_CONST.__objc_const: 0x2690
+  __AUTH_CONST.__cfstring: 0x4060
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x12e0
-  __AUTH.__objc_data: 0xdb8
-  __AUTH.__data: 0x888
-  __DATA.__objc_protorefs: 0x88
-  __DATA.__objc_classrefs: 0xd18
-  __DATA.__objc_superrefs: 0x1c8
-  __DATA.__objc_ivar: 0x45c
+  __AUTH_CONST.__auth_got: 0x12a0
+  __AUTH.__objc_data: 0xeb8
+  __AUTH.__data: 0x8b0
+  __DATA.__objc_ivar: 0x468
   __DATA.__objc_data: 0x90
-  __DATA.__data: 0x2ff8
-  __DATA.__bss: 0x33a0
+  __DATA.__data: 0x2fb8
+  __DATA.__bss: 0x34e0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xf68
-  __DATA_DIRTY.__data: 0x530
-  __DATA_DIRTY.__bss: 0x710
+  __DATA_DIRTY.__data: 0x558
+  __DATA_DIRTY.__bss: 0x738
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4355
-  Symbols:   9221
-  CStrings:  5737
+  Functions: 4400
+  Symbols:   9435
+  CStrings:  5915
 
Symbols:
+ +[WFConfiguredSystemActionProvider sharedProvider]
+ -[VCCKShortcutSyncCoordinator isUsingToprakSyncEngine]
+ -[VCCKShortcutSyncCoordinator updateCurrentSyncService]
+ -[VCCKShortcutSyncService fetchChangesOptions]
+ -[VCCKShortcutSyncService handleSavedLibraryRecord:]
+ -[VCCKShortcutSyncService handleSendLibraryConflictWithClientRecord:serverRecord:ancestorRecord:]
+ -[VCCKShortcutSyncService libraryRecordForRecordID:]
+ -[VCCKShortcutSyncService recordToSaveForRecordID:]
+ -[VCCKShortcutSyncService sendChangesOptions]
+ -[VCCKShortcutSyncService syncEngine:handleEvent:]
+ -[VCCKShortcutSyncService syncEngine:nextRecordZoneChangeBatchForContext:]
+ -[VCCKShortcutSyncService syncEngineDidDeleteRecordWithID:]
+ -[VCCKShortcutSyncService syncEngineDidDeleteRecordZoneWithID:]
+ -[VCCKShortcutSyncService syncEngineDidFetchRecord:]
+ -[VCCKShortcutSyncService syncEngineDidSaveRecord:]
+ -[VCCKShortcutSyncService syncEngineDidSaveRecordZone:]
+ -[VCCKShortcutSyncService syncEngineDidUpdateMetadata:]
+ -[VCCKShortcutSyncService syncEngineFailedToDeleteRecordWithID:error:]
+ -[VCCKShortcutSyncService syncEngineFailedToDeleteRecordZoneWithID:error:]
+ -[VCCKShortcutSyncService syncEngineFailedToSaveRecord:error:]
+ -[VCCKShortcutSyncService syncEngineFailedToSaveRecordZone:error:]
+ -[VCCKShortcutSyncService syncEngineRecordWithIDWasDeleted:recordType:]
+ -[VCCKShortcutSyncService syncEngineZoneWithIDChanged:]
+ -[VCCKShortcutSyncService syncEngineZoneWithIDWasDeleted:]
+ -[VCCKShortcutSyncService syncEngineZoneWithIDWasPurged:]
+ -[VCVoiceShortcutManager coherenceEnabledWithCompletion:]
+ -[VCVoiceShortcutManager coherenceMigrationEnabledWithCompletion:]
+ -[VCVoiceShortcutManager setCoherenceMigrationStatus:completion:]
+ -[VCVoiceShortcutManager toprakEngineEnabledWithCompletion:]
+ -[VCVoiceShortcutManagerAccessWrapper coherenceEnabledWithCompletion:]
+ -[VCVoiceShortcutManagerAccessWrapper coherenceMigrationEnabledWithCompletion:]
+ -[VCVoiceShortcutManagerAccessWrapper setCoherenceMigrationStatus:completion:]
+ -[VCVoiceShortcutManagerAccessWrapper toprakEngineEnabledWithCompletion:]
+ -[WFConfiguredSystemActionMigrator .cxx_destruct]
+ -[WFConfiguredSystemActionMigrator actionProvider]
+ -[WFConfiguredSystemActionMigrator databaseDeboucer]
+ -[WFConfiguredSystemActionMigrator databaseDidChange:modified:inserted:removed:]
+ -[WFConfiguredSystemActionMigrator databaseProvider]
+ -[WFConfiguredSystemActionMigrator database]
+ -[WFConfiguredSystemActionMigrator handleDatabaseChangeWithDelay]
+ -[WFConfiguredSystemActionMigrator initWithDatabaseProvider:actionProvider:]
+ -[WFConfiguredSystemActionMigrator isConfiguredSystemActionValid:]
+ -[WFConfiguredSystemActionMigrator queue]
+ -[WFConfiguredSystemActionMigrator setDatabase:]
+ -[WFConfiguredSystemActionMigrator setDatabaseDeboucer:]
+ -[WFConfiguredSystemActionMigrator startMonitoring]
+ -[WFConfiguredSystemActionMigrator stopMonitoring]
+ -[WFConfiguredSystemActionMigrator updateActionsIfNeededWithReason:]
+ -[WFConfiguredSystemActionMigrator updateConfiguredSystemActionOfType:]
+ -[WFConfiguredSystemActionMigrator updatedConfiguredSystemActionFrom:]
+ -[WFConfiguredSystemActionProvider availableActionTypes]
+ -[WFConfiguredSystemActionProvider configuredStaccatoActionFromTemplate:valuesByParameterKey:error:]
+ -[WFConfiguredSystemActionProvider configuredSystemActionForActionType:]
+ -[WFConfiguredSystemActionProvider defaultSystemActionForActionType:]
+ -[WFConfiguredSystemActionProvider linkActionWithStaccatoIdentifier:]
+ -[WFConfiguredSystemActionProvider saveUpdatedAction:forActionType:]
+ -[WFContextualActionSpotlightSyncService appShortcutBatchSize]
+ -[WFContextualActionSpotlightSyncService cellularSettingsUpdated]
+ -[WFContextualActionSpotlightSyncService queue_v2GetAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]
+ GCC_except_table101
+ GCC_except_table1011
+ GCC_except_table102
+ GCC_except_table1164
+ GCC_except_table1199
+ GCC_except_table1205
+ GCC_except_table1236
+ GCC_except_table1356
+ GCC_except_table1368
+ GCC_except_table139
+ GCC_except_table1449
+ GCC_except_table1455
+ GCC_except_table1457
+ GCC_except_table1460
+ GCC_except_table1461
+ GCC_except_table1466
+ GCC_except_table1475
+ GCC_except_table1651
+ GCC_except_table1663
+ GCC_except_table1669
+ GCC_except_table1670
+ GCC_except_table1678
+ GCC_except_table1680
+ GCC_except_table1682
+ GCC_except_table1684
+ GCC_except_table1687
+ GCC_except_table1688
+ GCC_except_table1700
+ GCC_except_table1739
+ GCC_except_table1746
+ GCC_except_table1757
+ GCC_except_table1764
+ GCC_except_table1802
+ GCC_except_table1806
+ GCC_except_table1824
+ GCC_except_table1828
+ GCC_except_table1842
+ GCC_except_table1854
+ GCC_except_table1857
+ GCC_except_table1870
+ GCC_except_table196
+ GCC_except_table1977
+ GCC_except_table1978
+ GCC_except_table1989
+ GCC_except_table1991
+ GCC_except_table201
+ GCC_except_table2024
+ GCC_except_table203
+ GCC_except_table206
+ GCC_except_table289
+ GCC_except_table373
+ GCC_except_table387
+ GCC_except_table402
+ GCC_except_table426
+ GCC_except_table448
+ GCC_except_table475
+ GCC_except_table491
+ GCC_except_table537
+ GCC_except_table563
+ GCC_except_table570
+ GCC_except_table579
+ GCC_except_table583
+ GCC_except_table585
+ GCC_except_table638
+ GCC_except_table731
+ GCC_except_table732
+ GCC_except_table747
+ GCC_except_table758
+ GCC_except_table96
+ _OBJC_CLASS_$_CKSyncEngineFetchChangesOptions
+ _OBJC_CLASS_$_CKSyncEngineFetchChangesScope
+ _OBJC_CLASS_$_CKSyncEngineFetchedDatabaseChangesEvent
+ _OBJC_CLASS_$_CKSyncEngineFetchedRecordZoneChangesEvent
+ _OBJC_CLASS_$_CKSyncEnginePendingRecordZoneChange
+ _OBJC_CLASS_$_CKSyncEnginePendingZoneSave
+ _OBJC_CLASS_$_CKSyncEngineRecordZoneChangeBatch
+ _OBJC_CLASS_$_CKSyncEngineSendChangesOptions
+ _OBJC_CLASS_$_CKSyncEngineSendChangesScope
+ _OBJC_CLASS_$_CKSyncEngineSentDatabaseChangesEvent
+ _OBJC_CLASS_$_CKSyncEngineSentRecordZoneChangesEvent
+ _OBJC_CLASS_$_CKSyncEngineStateSerialization
+ _OBJC_CLASS_$_CKSyncEngineStateUpdateEvent
+ _OBJC_CLASS_$_WFAppShortcutDataSource
+ _OBJC_CLASS_$_WFCloudKitLibrary
+ _OBJC_CLASS_$_WFConfiguredActionButtonIntentAction
+ _OBJC_CLASS_$_WFConfiguredSystemAction
+ _OBJC_CLASS_$_WFConfiguredSystemActionMigrator
+ _OBJC_CLASS_$_WFConfiguredSystemActionProvider
+ _OBJC_CLASS_$_WFConfiguredSystemNothingAction
+ _OBJC_CLASS_$_WFConfiguredSystemWorkflowAction
+ _OBJC_CLASS_$_WFExecutableAppShortcut
+ _OBJC_CLASS_$__TtC14VoiceShortcuts26VCCKLibrarySyncCoordinator
+ _OBJC_IVAR_$_VCCKShortcutSyncService._fetchChangesOptions
+ _OBJC_IVAR_$_VCCKShortcutSyncService._sendChangesOptions
+ _OBJC_IVAR_$_WFConfiguredSystemActionMigrator._actionProvider
+ _OBJC_IVAR_$_WFConfiguredSystemActionMigrator._database
+ _OBJC_IVAR_$_WFConfiguredSystemActionMigrator._databaseDeboucer
+ _OBJC_IVAR_$_WFConfiguredSystemActionMigrator._databaseProvider
+ _OBJC_IVAR_$_WFConfiguredSystemActionMigrator._queue
+ _OBJC_METACLASS_$_WFConfiguredSystemActionMigrator
+ _OBJC_METACLASS_$_WFConfiguredSystemActionProvider
+ _OBJC_METACLASS_$__TtC14VoiceShortcuts26VCCKLibrarySyncCoordinator
+ _WFDeviceCapabilityActionButton
+ _WFLogCategoryGeneral
+ _WFShortcutsSyncTriggerChangeZone
+ _WFShortcutsSyncTriggerDeleteRecord
+ _WFShortcutsSyncTriggerDeleteZone
+ _WFShortcutsSyncTriggerFetchRecord
+ _WFShortcutsSyncTriggerPurgeZone
+ _WFShortcutsSyncTriggerSaveRecord
+ _WFShortcutsSyncTriggerSaveZone
+ _WFSpotlightResultRunnableLNPropertyIdentifier
+ _WFStaccatoActionIdentifierSilentMode
+ _WFSystemActionTypeActionButton
+ __DATA__TtC14VoiceShortcuts26VCCKLibrarySyncCoordinator
+ __METACLASS_DATA__TtC14VoiceShortcuts26VCCKLibrarySyncCoordinator
+ __OBJC_$_CLASS_METHODS_WFConfiguredSystemActionProvider
+ __OBJC_$_CLASS_METHODS__TtC14VoiceShortcuts26VCCKLibrarySyncCoordinator
+ __OBJC_$_INSTANCE_METHODS_WFConfiguredSystemActionMigrator
+ __OBJC_$_INSTANCE_METHODS_WFConfiguredSystemActionProvider
+ __OBJC_$_INSTANCE_METHODS__TtC14VoiceShortcuts26VCCKLibrarySyncCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_WFConfiguredSystemActionMigrator
+ __OBJC_$_PROP_LIST_WFConfiguredSystemActionMigrator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CKSyncEngineDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CKSyncEngineDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CKSyncEngineDelegate
+ __OBJC_$_PROTOCOL_REFS_CKSyncEngineDelegate
+ __OBJC_CLASS_PROTOCOLS_$_WFConfiguredSystemActionMigrator
+ __OBJC_CLASS_RO_$_WFConfiguredSystemActionMigrator
+ __OBJC_CLASS_RO_$_WFConfiguredSystemActionProvider
+ __OBJC_LABEL_PROTOCOL_$_CKSyncEngineDelegate
+ __OBJC_METACLASS_RO_$_WFConfiguredSystemActionMigrator
+ __OBJC_METACLASS_RO_$_WFConfiguredSystemActionProvider
+ __OBJC_PROTOCOL_$_CKSyncEngineDelegate
+ ___103-[VCVoiceShortcutManager updateVoiceShortcutWithIdentifier:phrase:shortcut:accessSpecifier:completion:]_block_invoke.236
+ ___105-[VCVoiceShortcutManager getSleepActionSuggestionsForAllAppsFilteringBySleep:accessSpecifier:completion:]_block_invoke.284
+ ___105-[WFContextualActionSpotlightSyncService reindexSearchableItems:appShortcutBundleIdentifiers:completion:]_block_invoke.199
+ ___105-[WFContextualActionSpotlightSyncService reindexSearchableItems:appShortcutBundleIdentifiers:completion:]_block_invoke_2.201
+ ___105-[WFContextualActionSpotlightSyncService reindexSearchableItems:appShortcutBundleIdentifiers:completion:]_block_invoke_2.234
+ ___112-[WFWalletTransactionProvider observeForUpdatesWithInitialTransactionIfNeeded:transactionIdentifier:completion:]_block_invoke.198
+ ___113-[WFTriggerEventQueue notificationManager:receivedConfirmationToRunTriggerWithIdentifier:pendingTriggerEventIDs:]_block_invoke.203
+ ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.276
+ ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.277
+ ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.280
+ ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.281
+ ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.282
+ ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.286
+ ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.291
+ ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.292
+ ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.293
+ ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke_2.287
+ ___120-[WFContextualActionSpotlightSyncService queue_v2GetAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke
+ ___120-[WFContextualActionSpotlightSyncService queue_v2GetAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.297
+ ___120-[WFContextualActionSpotlightSyncService queue_v2GetAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.298
+ ___120-[WFContextualActionSpotlightSyncService queue_v2GetAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.300
+ ___120-[WFContextualActionSpotlightSyncService queue_v2GetAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.302
+ ___120-[WFContextualActionSpotlightSyncService queue_v2GetAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.303
+ ___120-[WFContextualActionSpotlightSyncService queue_v2GetAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.304
+ ___120-[WFContextualActionSpotlightSyncService queue_v2GetAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke_2
+ ___123-[VCVoiceShortcutManager getLinkActionWithAppBundleIdentifier:appIntentIdentifier:expandingParameterName:limit:completion:]_block_invoke.376
+ ___123-[VCVoiceShortcutManager getLinkActionWithAppBundleIdentifier:appIntentIdentifier:expandingParameterName:limit:completion:]_block_invoke.380
+ ___123-[VCVoiceShortcutManager getLinkActionWithAppBundleIdentifier:appIntentIdentifier:expandingParameterName:limit:completion:]_block_invoke.381
+ ___125-[VCVoiceShortcutManager getSleepActionSuggestionsForAppWithBundleIdentifier:shouldFilterBySleep:accessSpecifier:completion:]_block_invoke.277
+ ___146-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:batchSize:fetcher:completionBlock:]_block_invoke.236
+ ___146-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:batchSize:fetcher:completionBlock:]_block_invoke.238
+ ___146-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:batchSize:fetcher:completionBlock:]_block_invoke.252
+ ___146-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:batchSize:fetcher:completionBlock:]_block_invoke.254
+ ___146-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:batchSize:fetcher:completionBlock:]_block_invoke.256
+ ___146-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:batchSize:fetcher:completionBlock:]_block_invoke_2.253
+ ___146-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:batchSize:fetcher:completionBlock:]_block_invoke_2.255
+ ___146-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:batchSize:fetcher:completionBlock:]_block_invoke_2.257
+ ___159-[WFTriggerUserNotificationManager _postNotificationOfType:forTrigger:workflowReference:removeDeliveredNotifications:pendingTriggerEventIDs:actionIcons:error:]_block_invoke.213
+ ___37-[WFTopHitsAppShortcutsUpdater start]_block_invoke.163
+ ___42-[VCSpotlightSyncOperation saveLocalState]_block_invoke.166
+ ___42-[VCSpotlightSyncOperation saveLocalState]_block_invoke_2.167
+ ___48-[WFBiomeListener queue_handleEvent:forTrigger:]_block_invoke.185
+ ___50+[WFConfiguredSystemActionProvider sharedProvider]_block_invoke
+ ___50-[VCXPCServer listener:shouldAcceptNewConnection:]_block_invoke.170
+ ___50-[WFConfiguredSystemActionMigrator stopMonitoring]_block_invoke
+ ___51-[VCCKShortcutSyncService recordToSaveForRecordID:]_block_invoke
+ ___51-[VCCKShortcutSyncService syncEngineDidSaveRecord:]_block_invoke
+ ___51-[WFConfiguredSystemActionMigrator startMonitoring]_block_invoke
+ ___52-[VCCKShortcutSyncService syncEngineDidFetchRecord:]_block_invoke
+ ___53-[VCCKShortcutSyncService handleFetchedFolderRecord:]_block_invoke.250
+ ___55-[VCCKShortcutSyncCoordinator updateCurrentSyncService]_block_invoke
+ ___55-[VCCKShortcutSyncService handleFetchedWorkflowRecord:]_block_invoke.234
+ ___55-[VCCKShortcutSyncService handleFetchedWorkflowRecord:]_block_invoke.238
+ ___55-[VCCKShortcutSyncService handleFetchedWorkflowRecord:]_block_invoke.243
+ ___55-[VCCKShortcutSyncService syncEngineDidUpdateMetadata:]_block_invoke
+ ___55-[VCCKShortcutSyncService syncEngineDidUpdateMetadata:]_block_invoke_2
+ ___56-[WFBiomeListener registerConfiguredTrigger:completion:]_block_invoke.159
+ ___56-[WFBiomeListener registerConfiguredTrigger:completion:]_block_invoke.160
+ ___56-[WFBiomeListener registerConfiguredTrigger:completion:]_block_invoke.166
+ ___56-[WFBiomeListener registerConfiguredTrigger:completion:]_block_invoke.167
+ ___58+[VCIntentDefinitionSyncState applicationsJSONTransformer]_block_invoke.104
+ ___59-[VCCKShortcutSyncService syncEngineDidDeleteRecordWithID:]_block_invoke
+ ___62-[VCCKShortcutSyncService syncEngineFailedToSaveRecord:error:]_block_invoke
+ ___63-[WFTriggerNotificationScheduler registerWithDatabaseProvider:]_block_invoke.156
+ ___64-[WFWorkflowStatusPresenter listener:shouldAcceptNewConnection:]_block_invoke.151
+ ___64-[WFWorkflowStatusPresenter listener:shouldAcceptNewConnection:]_block_invoke.152
+ ___64-[WFWorkflowStatusPresenter listener:shouldAcceptNewConnection:]_block_invoke.153
+ ___65-[VCCKShortcutSyncCoordinator updateAccountStatusAndUserRecordID]_block_invoke.186
+ ___66-[WFCoreDuetListener handleCallbackForTriggerWithIdentifier:info:]_block_invoke.193
+ ___66-[WFDialogPresentationManager listener:shouldAcceptNewConnection:]_block_invoke.189
+ ___66-[WFDialogPresentationManager listener:shouldAcceptNewConnection:]_block_invoke.190
+ ___66-[WFDialogPresentationManager listener:shouldAcceptNewConnection:]_block_invoke.191
+ ___66-[WFTriggerNotificationScheduler registerConfiguredTrigger:delay:]_block_invoke.158
+ ___66-[WFTriggerNotificationScheduler registerConfiguredTrigger:delay:]_block_invoke.160
+ ___66-[WFTriggerNotificationScheduler registerConfiguredTrigger:delay:]_block_invoke.162
+ ___67-[VCSpotlightSyncService syncWithModifiedObjects:inserted:removed:]_block_invoke.174
+ ___68-[WFUserNotificationManager removeStaleNotificationsWithCompletion:]_block_invoke.155
+ ___69-[WFTriggerRegistrar getConfiguredTriggerDescriptionsWithCompletion:]_block_invoke.189
+ ___71-[VCCKShortcutSyncService syncEngineRecordWithIDWasDeleted:recordType:]_block_invoke
+ ___72-[WFSpringBoardRemoteAlertPresenter listener:shouldAcceptNewConnection:]_block_invoke.168
+ ___73-[WFTopHitsAppShortcutsUpdater registerForUpcomingMediaSuggestionChanged]_block_invoke.192
+ ___74-[VCCKShortcutSyncService initWithContainer:database:applicationObserver:]_block_invoke
+ ___74-[VCCKShortcutSyncService syncEngine:nextRecordZoneChangeBatchForContext:]_block_invoke
+ ___75-[WFTriggerNotificationScheduler updateTriggerNotificationLevels:database:]_block_invoke.172
+ ___76-[WFOnScreenContentManager getOnScreenContentWithOptions:completionHandler:]_block_invoke.143
+ ___78-[VCCKShortcutSyncCoordinator observeValueForKeyPath:ofObject:change:context:]_block_invoke.198
+ ___78-[VCCKShortcutSyncCoordinator observeValueForKeyPath:ofObject:change:context:]_block_invoke_2
+ ___78-[WFTriggerNotificationScheduler postBackgroundRunningNotificationForTrigger:]_block_invoke.168
+ ___78-[WFTriggerNotificationScheduler postBackgroundRunningNotificationForTrigger:]_block_invoke.170
+ ___79-[WFTriggerEventQueue enqueueTriggerWithIdentifier:eventInfo:force:completion:]_block_invoke.170
+ ___82-[WFDialogPresentationManager showDialogRequest:runningContext:completionHandler:]_block_invoke.176
+ ___84-[VCVoiceShortcutManagerAccessWrapper getRecentsCallWithTelephony:limit:completion:]_block_invoke.248
+ ___84-[WFDialogPresentationManager postNotificationWithRequest:presentationMode:context:]_block_invoke.187
+ ___92-[VCVoiceShortcutManagerAccessWrapper fetchAllValueSectionsForStaccatoParameter:completion:]_block_invoke.323
+ ___92-[WFTriggerBootManager registerForInitialBootXPCActivityWithUserNotificationCenterIfNeeded:]_block_invoke.160
+ ___92-[WFTriggerBootManager registerForInitialBootXPCActivityWithUserNotificationCenterIfNeeded:]_block_invoke.162
+ ___92-[WFTriggerBootManager registerForInitialBootXPCActivityWithUserNotificationCenterIfNeeded:]_block_invoke.164
+ ___92-[WFWalletTransactionProvider fetchRemoteTransactionWithIdentifier:passUniqueID:completion:]_block_invoke.192
+ ___92-[WFWalletTransactionProvider fetchRemoteTransactionWithIdentifier:passUniqueID:completion:]_block_invoke_2.193
+ ___96-[VCCKShortcutSyncService mergeLocalOrderingChangesWithRemoteOrderingChangesFromOrderingRecord:]_block_invoke.217
+ ___96-[VCCKShortcutSyncService mergeLocalOrderingChangesWithRemoteOrderingChangesFromOrderingRecord:]_block_invoke.218
+ ___97-[VCCKShortcutSyncService handleSendLibraryConflictWithClientRecord:serverRecord:ancestorRecord:]_block_invoke
+ ___97-[WFRemoteQuarantinePolicyManager(XPCActivity) scheduleRegularPolicyUpdatesWithDatabaseProvider:]_block_invoke.145
+ ___98+[WFTriggerBootManager registerForNotificationRemovalWithUserNotificationCenter:scheduleIfNeeded:]_block_invoke.172
+ ___98+[WFTriggerBootManager registerForNotificationRemovalWithUserNotificationCenter:scheduleIfNeeded:]_block_invoke.174
+ ___98+[WFTriggerBootManager registerForNotificationRemovalWithUserNotificationCenter:scheduleIfNeeded:]_block_invoke.176
+ ___Block_byref_object_copy_.1183
+ ___Block_byref_object_copy_.3518
+ ___Block_byref_object_copy_.3731
+ ___Block_byref_object_copy_.3936
+ ___Block_byref_object_copy_.4704
+ ___Block_byref_object_copy_.4915
+ ___Block_byref_object_copy_.5959
+ ___Block_byref_object_copy_.6202
+ ___Block_byref_object_copy_.6319
+ ___Block_byref_object_copy_.6460
+ ___Block_byref_object_copy_.6552
+ ___Block_byref_object_copy_.752
+ ___Block_byref_object_dispose_.1184
+ ___Block_byref_object_dispose_.3519
+ ___Block_byref_object_dispose_.3732
+ ___Block_byref_object_dispose_.3937
+ ___Block_byref_object_dispose_.4705
+ ___Block_byref_object_dispose_.4916
+ ___Block_byref_object_dispose_.5960
+ ___Block_byref_object_dispose_.6203
+ ___Block_byref_object_dispose_.6320
+ ___Block_byref_object_dispose_.6461
+ ___Block_byref_object_dispose_.6553
+ ___Block_byref_object_dispose_.753
+ ___block_descriptor_40_e8_32s_e46_"NSString"16?0"WFDatabaseObjectDescriptor"8ls32l8
+ ___block_descriptor_40_e8_32s_e56_"WFContextualAction"24?0"WFExecutableAppShortcut"8Q16ls32l8
+ ___block_descriptor_48_e8_32s40s_e30_"CKRecord"16?0"CKRecordID"8ls32l8s40l8
+ ___block_literal_global.1051
+ ___block_literal_global.109
+ ___block_literal_global.1202
+ ___block_literal_global.1400
+ ___block_literal_global.152
+ ___block_literal_global.158
+ ___block_literal_global.168
+ ___block_literal_global.1710
+ ___block_literal_global.173
+ ___block_literal_global.175
+ ___block_literal_global.175.7492
+ ___block_literal_global.177
+ ___block_literal_global.182
+ ___block_literal_global.1825
+ ___block_literal_global.186
+ ___block_literal_global.186.3620
+ ___block_literal_global.194
+ ___block_literal_global.198
+ ___block_literal_global.200
+ ___block_literal_global.200.5924
+ ___block_literal_global.220
+ ___block_literal_global.225
+ ___block_literal_global.241.5681
+ ___block_literal_global.244
+ ___block_literal_global.245
+ ___block_literal_global.2462
+ ___block_literal_global.255
+ ___block_literal_global.255.2392
+ ___block_literal_global.259
+ ___block_literal_global.262
+ ___block_literal_global.269
+ ___block_literal_global.270
+ ___block_literal_global.272
+ ___block_literal_global.2910
+ ___block_literal_global.292
+ ___block_literal_global.298
+ ___block_literal_global.3123
+ ___block_literal_global.313
+ ___block_literal_global.328
+ ___block_literal_global.343
+ ___block_literal_global.3615
+ ___block_literal_global.363
+ ___block_literal_global.365
+ ___block_literal_global.3745
+ ___block_literal_global.390
+ ___block_literal_global.3982
+ ___block_literal_global.4319
+ ___block_literal_global.4985
+ ___block_literal_global.5221
+ ___block_literal_global.550
+ ___block_literal_global.5747
+ ___block_literal_global.5972
+ ___block_literal_global.602
+ ___block_literal_global.6201
+ ___block_literal_global.6343
+ ___block_literal_global.6545
+ ___block_literal_global.658
+ ___block_literal_global.6786
+ ___block_literal_global.7024
+ ___block_literal_global.7508
+ ___block_literal_global.754
+ ___block_literal_global.7579
+ ___block_literal_global.79
+ __unnamed_array_storage.5689
+ _associated conformance 14VoiceShortcuts31VCCKLibrarySyncCoordinatorError33_7E1F78BDEE9DB7EA345475730192702BLLOSHAASQ
+ _block_descriptor.22
+ _objc_msgSend$actionProvider
+ _objc_msgSend$addPendingDatabaseChanges:
+ _objc_msgSend$addPendingRecordZoneChanges:
+ _objc_msgSend$appShortcutBatchSize
+ _objc_msgSend$availableActionTypes
+ _objc_msgSend$coherenceEnabled
+ _objc_msgSend$coherenceEnabledWithCompletion:
+ _objc_msgSend$coherenceMigrationEnabled
+ _objc_msgSend$coherenceMigrationEnabledWithCompletion:
+ _objc_msgSend$configuredStaccatoActionFromTemplate:valuesByParameterKey:error:
+ _objc_msgSend$configuredSystemActionForActionType:
+ _objc_msgSend$containsRecordID:
+ _objc_msgSend$dataFileRepresentation
+ _objc_msgSend$databaseDeboucer
+ _objc_msgSend$defaultSystemActionForActionType:
+ _objc_msgSend$deletedRecordIDs
+ _objc_msgSend$deletedZoneIDs
+ _objc_msgSend$deletions
+ _objc_msgSend$failedRecordDeletes
+ _objc_msgSend$failedRecordSaves
+ _objc_msgSend$failedZoneDeletes
+ _objc_msgSend$failedZoneSaves
+ _objc_msgSend$fetchAppShortcutsForBundleIdentifiers:localeIdentifier:error:
+ _objc_msgSend$fetchChangesOptions
+ _objc_msgSend$fetchChangesWithOptions:completionHandler:
+ _objc_msgSend$handleFetchedLibraryRecord:database:error:
+ _objc_msgSend$handleSavedLibraryRecord:
+ _objc_msgSend$handleSavedLibraryRecord:database:error:
+ _objc_msgSend$handleSendLibraryConflictWithClientRecord:serverRecord:ancestorRecord:
+ _objc_msgSend$handleServerRecordChangedErrorForRecord:database:error:
+ _objc_msgSend$handleUnknownItemErrorForRecord:database:error:
+ _objc_msgSend$id
+ _objc_msgSend$initWithAppShortcutsDenyListEnvironment:environment:
+ _objc_msgSend$initWithDatabase:stateSerialization:delegate:
+ _objc_msgSend$initWithDeprecatedData:
+ _objc_msgSend$initWithExecutableAppShortcut:index:
+ _objc_msgSend$initWithIntent:named:previewIcon:appShortcutIdentifier:templateParameterValues:contextualParameters:shortcutsMetadata:
+ _objc_msgSend$initWithLibraryRecord:zoneID:
+ _objc_msgSend$initWithPendingChanges:recordProvider:
+ _objc_msgSend$initWithRecordID:type:
+ _objc_msgSend$initWithScope:
+ _objc_msgSend$initWithWorkflow:shortcutsMetadata:
+ _objc_msgSend$initWithZone:
+ _objc_msgSend$initWithZoneIDs:
+ _objc_msgSend$isConfiguredSystemActionValid:
+ _objc_msgSend$isLibraryRecordID:
+ _objc_msgSend$isTopHitEligible
+ _objc_msgSend$legacySpotlightDomainIdentifier
+ _objc_msgSend$libraryIdentifierFromRecordID:error:
+ _objc_msgSend$libraryRecordForRecordID:
+ _objc_msgSend$lnPropertyIdentifier
+ _objc_msgSend$modifications
+ _objc_msgSend$options
+ _objc_msgSend$pendingRecordZoneChanges
+ _objc_msgSend$queue_v2GetAppShortcutContextualActionsForBundleIdentifiers:completionHandler:
+ _objc_msgSend$reason
+ _objc_msgSend$recordIDWithZoneID:libraryIdentifier:
+ _objc_msgSend$recordToSaveForRecordID:
+ _objc_msgSend$recordZone
+ _objc_msgSend$removeObjectObserver:
+ _objc_msgSend$removePendingRecordZoneChanges:
+ _objc_msgSend$runEventsCount
+ _objc_msgSend$saveSyncEventWithDate:trigger:success:errorDescription:
+ _objc_msgSend$saveUpdatedAction:forActionType:
+ _objc_msgSend$savedRecords
+ _objc_msgSend$savedZones
+ _objc_msgSend$scope
+ _objc_msgSend$sendChangesOptions
+ _objc_msgSend$sendChangesWithOptions:completionHandler:
+ _objc_msgSend$setCoherenceMigrationEnabled:
+ _objc_msgSend$setCoherenceMigrationStatus:completion:
+ _objc_msgSend$setDatabase:
+ _objc_msgSend$setDatabaseDeboucer:
+ _objc_msgSend$setPlayCount:
+ _objc_msgSend$shortcutsMetadata
+ _objc_msgSend$spotlightIconWithParameterIdentifier:
+ _objc_msgSend$stateSerialization
+ _objc_msgSend$syncEngineDidDeleteRecordWithID:
+ _objc_msgSend$syncEngineDidDeleteRecordZoneWithID:
+ _objc_msgSend$syncEngineDidFetchRecord:
+ _objc_msgSend$syncEngineDidSaveRecord:
+ _objc_msgSend$syncEngineDidSaveRecordZone:
+ _objc_msgSend$syncEngineDidUpdateMetadata:
+ _objc_msgSend$syncEngineFailedToDeleteRecordWithID:error:
+ _objc_msgSend$syncEngineFailedToDeleteRecordZoneWithID:error:
+ _objc_msgSend$syncEngineFailedToSaveRecord:error:
+ _objc_msgSend$syncEngineFailedToSaveRecordZone:error:
+ _objc_msgSend$syncEngineRecordWithIDWasDeleted:recordType:
+ _objc_msgSend$syncEngineZoneWithIDChanged:
+ _objc_msgSend$syncEngineZoneWithIDWasDeleted:
+ _objc_msgSend$syncEngineZoneWithIDWasPurged:
+ _objc_msgSend$toprakCoherenceEnabled
+ _objc_msgSend$toprakEngineEnabled
+ _objc_msgSend$toprakEngineEnabledWithCompletion:
+ _objc_msgSend$updateActionsIfNeededWithReason:
+ _objc_msgSend$updateConfiguredSystemActionOfType:
+ _objc_msgSend$updateCurrentSyncService
+ _objc_msgSend$updatedConfiguredSystemActionFrom:
+ _objc_msgSend$useNewDataSource
+ _objc_msgSend$wf_securelyArchivedDataWithRootObject:
+ _objectdestroy.55Tm
+ _sharedProvider.onceToken.932
+ _sharedProvider.sharedProvider
+ _symbolic G0R1_
+ _symbolic G1R1_
+ _symbolic G2R1_
+ _symbolic G3R1_
+ _symbolic So17WFCloudKitLibraryC
+ _symbolic So32WFConfiguredSystemActionMigratorC
+ _symbolic _____ 14VoiceShortcuts26VCCKLibrarySyncCoordinatorC
+ _symbolic _____ 14VoiceShortcuts31VCCKLibrarySyncCoordinatorError33_7E1F78BDEE9DB7EA345475730192702BLLO
- +[WFCellularSettings defaultSettings]
- -[VCCKShortcutSyncCoordinator isUsingSync2]
- -[VCCKShortcutSyncCoordinator updateCurrentSyncServiceIfNeeded]
- -[VCCKShortcutSyncService syncEngine:didDeleteRecordWithID:]
- -[VCCKShortcutSyncService syncEngine:didDeleteRecordZoneWithID:]
- -[VCCKShortcutSyncService syncEngine:didFetchRecord:]
- -[VCCKShortcutSyncService syncEngine:didSaveRecord:]
- -[VCCKShortcutSyncService syncEngine:didSaveRecordZone:]
- -[VCCKShortcutSyncService syncEngine:didUpdateMetadata:]
- -[VCCKShortcutSyncService syncEngine:failedToDeleteRecordWithID:error:]
- -[VCCKShortcutSyncService syncEngine:failedToDeleteRecordZoneWithID:error:]
- -[VCCKShortcutSyncService syncEngine:failedToSaveRecord:error:]
- -[VCCKShortcutSyncService syncEngine:failedToSaveRecordZone:error:]
- -[VCCKShortcutSyncService syncEngine:recordToSaveForRecordID:]
- -[VCCKShortcutSyncService syncEngine:recordWithIDWasDeleted:recordType:]
- -[VCCKShortcutSyncService syncEngine:zoneWithIDChanged:]
- -[VCCKShortcutSyncService syncEngine:zoneWithIDWasDeleted:]
- -[VCCKShortcutSyncService syncEngine:zoneWithIDWasPurged:]
- -[VCPBWorkflow hasSmartPromptPerWorkflowStateData]
- -[VCPBWorkflow setSmartPromptPerWorkflowStateData:]
- -[VCPBWorkflow smartPromptPerWorkflowStateData]
- -[WFCellularSettings cellularDataEnabledWithError:]
- -[WFCellularSettings connection]
- -[WFCellularSettings dealloc]
- -[WFCellularSettings init]
- -[WFContextualActionSpotlightSyncService autoShortcutsProvider]
- GCC_except_table1126
- GCC_except_table1161
- GCC_except_table1167
- GCC_except_table1198
- GCC_except_table1318
- GCC_except_table1330
- GCC_except_table135
- GCC_except_table1407
- GCC_except_table1413
- GCC_except_table1415
- GCC_except_table1418
- GCC_except_table1419
- GCC_except_table1424
- GCC_except_table1433
- GCC_except_table1570
- GCC_except_table1581
- GCC_except_table1599
- GCC_except_table1611
- GCC_except_table1617
- GCC_except_table1618
- GCC_except_table1626
- GCC_except_table1628
- GCC_except_table1630
- GCC_except_table1634
- GCC_except_table1635
- GCC_except_table1636
- GCC_except_table1648
- GCC_except_table1693
- GCC_except_table1704
- GCC_except_table1711
- GCC_except_table1749
- GCC_except_table1753
- GCC_except_table1771
- GCC_except_table1775
- GCC_except_table1789
- GCC_except_table1801
- GCC_except_table1804
- GCC_except_table1817
- GCC_except_table1893
- GCC_except_table1898
- GCC_except_table192
- GCC_except_table1935
- GCC_except_table1936
- GCC_except_table1947
- GCC_except_table1949
- GCC_except_table197
- GCC_except_table1982
- GCC_except_table199
- GCC_except_table202
- GCC_except_table285
- GCC_except_table369
- GCC_except_table383
- GCC_except_table398
- GCC_except_table422
- GCC_except_table444
- GCC_except_table463
- GCC_except_table479
- GCC_except_table506
- GCC_except_table544
- GCC_except_table551
- GCC_except_table560
- GCC_except_table564
- GCC_except_table566
- GCC_except_table616
- GCC_except_table709
- GCC_except_table710
- GCC_except_table725
- GCC_except_table736
- GCC_except_table92
- GCC_except_table97
- GCC_except_table98
- GCC_except_table992
- _CFRetain
- _CoreTelephonyLibrary
- _CoreTelephonyLibraryCore.frameworkLibrary
- _NSMachErrorDomain
- _NSPOSIXErrorDomain
- _OBJC_CLASS_$_WFActionButtonConfigurationEvent
- _OBJC_CLASS_$_WFConfiguredStaccatoIntentAction
- _OBJC_IVAR_$_VCPBWorkflow._hasSmartPromptPerWorkflowStateData
- _OBJC_IVAR_$_VCPBWorkflow._smartPromptPerWorkflowStateData
- _OBJC_IVAR_$_WFCellularSettings._connection
- _OBJC_IVAR_$_WFContextualActionSpotlightSyncService._autoShortcutsProvider
- _OBJC_METACLASS_$_WFCellularSettings
- _WFCellularSettingsErrorDomain
- _WFCoreTelephonyConnectionCallbackStub
- _WFSetSilentModeActionIdentifier
- __OBJC_$_CLASS_METHODS_WFCellularSettings
- __OBJC_$_INSTANCE_METHODS_WFCellularSettings
- __OBJC_$_INSTANCE_VARIABLES_WFCellularSettings
- __OBJC_$_PROP_LIST_WFCellularSettings
- __OBJC_CLASS_RO_$_WFCellularSettings
- __OBJC_METACLASS_RO_$_WFCellularSettings
- ___103-[VCVoiceShortcutManager updateVoiceShortcutWithIdentifier:phrase:shortcut:accessSpecifier:completion:]_block_invoke.233
- ___105-[VCVoiceShortcutManager getSleepActionSuggestionsForAllAppsFilteringBySleep:accessSpecifier:completion:]_block_invoke.281
- ___105-[WFContextualActionSpotlightSyncService reindexSearchableItems:appShortcutBundleIdentifiers:completion:]_block_invoke.193
- ___105-[WFContextualActionSpotlightSyncService reindexSearchableItems:appShortcutBundleIdentifiers:completion:]_block_invoke_2.195
- ___105-[WFContextualActionSpotlightSyncService reindexSearchableItems:appShortcutBundleIdentifiers:completion:]_block_invoke_2.228
- ___112-[WFWalletTransactionProvider observeForUpdatesWithInitialTransactionIfNeeded:transactionIdentifier:completion:]_block_invoke.195
- ___113-[WFTriggerEventQueue notificationManager:receivedConfirmationToRunTriggerWithIdentifier:pendingTriggerEventIDs:]_block_invoke.200
- ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.268
- ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.269
- ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.270
- ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.272
- ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.273
- ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.274
- ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.275
- ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.284
- ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.285
- ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke_2.279
- ___123-[VCVoiceShortcutManager getLinkActionWithAppBundleIdentifier:appIntentIdentifier:expandingParameterName:limit:completion:]_block_invoke.373
- ___123-[VCVoiceShortcutManager getLinkActionWithAppBundleIdentifier:appIntentIdentifier:expandingParameterName:limit:completion:]_block_invoke.377
- ___123-[VCVoiceShortcutManager getLinkActionWithAppBundleIdentifier:appIntentIdentifier:expandingParameterName:limit:completion:]_block_invoke.378
- ___125-[VCVoiceShortcutManager getSleepActionSuggestionsForAppWithBundleIdentifier:shouldFilterBySleep:accessSpecifier:completion:]_block_invoke.274
- ___146-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:batchSize:fetcher:completionBlock:]_block_invoke.230
- ___146-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:batchSize:fetcher:completionBlock:]_block_invoke.232
- ___146-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:batchSize:fetcher:completionBlock:]_block_invoke.246
- ___146-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:batchSize:fetcher:completionBlock:]_block_invoke.248
- ___146-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:batchSize:fetcher:completionBlock:]_block_invoke.250
- ___146-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:batchSize:fetcher:completionBlock:]_block_invoke_2.247
- ___146-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:batchSize:fetcher:completionBlock:]_block_invoke_2.249
- ___146-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:batchSize:fetcher:completionBlock:]_block_invoke_2.251
- ___159-[WFTriggerUserNotificationManager _postNotificationOfType:forTrigger:workflowReference:removeDeliveredNotifications:pendingTriggerEventIDs:actionIcons:error:]_block_invoke.210
- ___37+[WFCellularSettings defaultSettings]_block_invoke
- ___37-[WFTopHitsAppShortcutsUpdater start]_block_invoke.157
- ___42-[VCSpotlightSyncOperation saveLocalState]_block_invoke.163
- ___42-[VCSpotlightSyncOperation saveLocalState]_block_invoke_2.164
- ___48-[WFBiomeListener queue_handleEvent:forTrigger:]_block_invoke.182
- ___50-[VCXPCServer listener:shouldAcceptNewConnection:]_block_invoke.167
- ___52-[VCCKShortcutSyncService syncEngine:didSaveRecord:]_block_invoke
- ___53-[VCCKShortcutSyncService handleFetchedFolderRecord:]_block_invoke.226
- ___53-[VCCKShortcutSyncService syncEngine:didFetchRecord:]_block_invoke
- ___55-[VCCKShortcutSyncService handleFetchedWorkflowRecord:]_block_invoke.210
- ___55-[VCCKShortcutSyncService handleFetchedWorkflowRecord:]_block_invoke.214
- ___55-[VCCKShortcutSyncService handleFetchedWorkflowRecord:]_block_invoke.219
- ___56-[VCCKShortcutSyncService syncEngine:didUpdateMetadata:]_block_invoke
- ___56-[VCCKShortcutSyncService syncEngine:didUpdateMetadata:]_block_invoke_2
- ___56-[WFBiomeListener registerConfiguredTrigger:completion:]_block_invoke.154
- ___56-[WFBiomeListener registerConfiguredTrigger:completion:]_block_invoke.156
- ___56-[WFBiomeListener registerConfiguredTrigger:completion:]_block_invoke.163
- ___56-[WFBiomeListener registerConfiguredTrigger:completion:]_block_invoke.164
- ___58+[VCIntentDefinitionSyncState applicationsJSONTransformer]_block_invoke.103
- ___60-[VCCKShortcutSyncService syncEngine:didDeleteRecordWithID:]_block_invoke
- ___62-[VCCKShortcutSyncService syncEngine:recordToSaveForRecordID:]_block_invoke
- ___63-[VCCKShortcutSyncCoordinator updateCurrentSyncServiceIfNeeded]_block_invoke
- ___63-[VCCKShortcutSyncService syncEngine:failedToSaveRecord:error:]_block_invoke
- ___63-[WFTriggerNotificationScheduler registerWithDatabaseProvider:]_block_invoke.153
- ___64-[WFWorkflowStatusPresenter listener:shouldAcceptNewConnection:]_block_invoke.148
- ___64-[WFWorkflowStatusPresenter listener:shouldAcceptNewConnection:]_block_invoke.149
- ___64-[WFWorkflowStatusPresenter listener:shouldAcceptNewConnection:]_block_invoke.150
- ___65-[VCCKShortcutSyncCoordinator updateAccountStatusAndUserRecordID]_block_invoke.183
- ___66-[WFCoreDuetListener handleCallbackForTriggerWithIdentifier:info:]_block_invoke.190
- ___66-[WFDialogPresentationManager listener:shouldAcceptNewConnection:]_block_invoke.186
- ___66-[WFDialogPresentationManager listener:shouldAcceptNewConnection:]_block_invoke.187
- ___66-[WFDialogPresentationManager listener:shouldAcceptNewConnection:]_block_invoke.188
- ___66-[WFTriggerNotificationScheduler registerConfiguredTrigger:delay:]_block_invoke.155
- ___66-[WFTriggerNotificationScheduler registerConfiguredTrigger:delay:]_block_invoke.157
- ___66-[WFTriggerNotificationScheduler registerConfiguredTrigger:delay:]_block_invoke.159
- ___67-[VCSpotlightSyncService syncWithModifiedObjects:inserted:removed:]_block_invoke.171
- ___68-[WFUserNotificationManager removeStaleNotificationsWithCompletion:]_block_invoke.152
- ___69-[WFTriggerRegistrar getConfiguredTriggerDescriptionsWithCompletion:]_block_invoke.186
- ___72-[VCCKShortcutSyncService syncEngine:recordWithIDWasDeleted:recordType:]_block_invoke
- ___72-[WFSpringBoardRemoteAlertPresenter listener:shouldAcceptNewConnection:]_block_invoke.165
- ___73-[WFTopHitsAppShortcutsUpdater registerForUpcomingMediaSuggestionChanged]_block_invoke_2
- ___75-[WFTriggerNotificationScheduler updateTriggerNotificationLevels:database:]_block_invoke.169
- ___76-[WFOnScreenContentManager getOnScreenContentWithOptions:completionHandler:]_block_invoke.140
- ___78-[VCCKShortcutSyncCoordinator observeValueForKeyPath:ofObject:change:context:]_block_invoke.195
- ___78-[WFTriggerNotificationScheduler postBackgroundRunningNotificationForTrigger:]_block_invoke.165
- ___78-[WFTriggerNotificationScheduler postBackgroundRunningNotificationForTrigger:]_block_invoke.167
- ___79-[WFTriggerEventQueue enqueueTriggerWithIdentifier:eventInfo:force:completion:]_block_invoke.167
- ___82-[WFDialogPresentationManager showDialogRequest:runningContext:completionHandler:]_block_invoke.173
- ___84-[VCVoiceShortcutManagerAccessWrapper getRecentsCallWithTelephony:limit:completion:]_block_invoke.245
- ___84-[WFDialogPresentationManager postNotificationWithRequest:presentationMode:context:]_block_invoke.184
- ___92-[VCVoiceShortcutManagerAccessWrapper fetchAllValueSectionsForStaccatoParameter:completion:]_block_invoke.320
- ___92-[WFTriggerBootManager registerForInitialBootXPCActivityWithUserNotificationCenterIfNeeded:]_block_invoke.157
- ___92-[WFTriggerBootManager registerForInitialBootXPCActivityWithUserNotificationCenterIfNeeded:]_block_invoke.159
- ___92-[WFTriggerBootManager registerForInitialBootXPCActivityWithUserNotificationCenterIfNeeded:]_block_invoke.161
- ___92-[WFWalletTransactionProvider fetchRemoteTransactionWithIdentifier:passUniqueID:completion:]_block_invoke.189
- ___92-[WFWalletTransactionProvider fetchRemoteTransactionWithIdentifier:passUniqueID:completion:]_block_invoke_2.190
- ___96-[VCCKShortcutSyncService mergeLocalOrderingChangesWithRemoteOrderingChangesFromOrderingRecord:]_block_invoke.193
- ___96-[VCCKShortcutSyncService mergeLocalOrderingChangesWithRemoteOrderingChangesFromOrderingRecord:]_block_invoke.194
- ___97-[WFRemoteQuarantinePolicyManager(XPCActivity) scheduleRegularPolicyUpdatesWithDatabaseProvider:]_block_invoke.142
- ___98+[WFTriggerBootManager registerForNotificationRemovalWithUserNotificationCenter:scheduleIfNeeded:]_block_invoke.169
- ___98+[WFTriggerBootManager registerForNotificationRemovalWithUserNotificationCenter:scheduleIfNeeded:]_block_invoke.171
- ___98+[WFTriggerBootManager registerForNotificationRemovalWithUserNotificationCenter:scheduleIfNeeded:]_block_invoke.173
- ___Block_byref_object_copy_.1133
- ___Block_byref_object_copy_.3367
- ___Block_byref_object_copy_.3585
- ___Block_byref_object_copy_.3809
- ___Block_byref_object_copy_.4580
- ___Block_byref_object_copy_.4803
- ___Block_byref_object_copy_.5815
- ___Block_byref_object_copy_.6054
- ___Block_byref_object_copy_.6170
- ___Block_byref_object_copy_.6310
- ___Block_byref_object_copy_.6402
- ___Block_byref_object_copy_.744
- ___Block_byref_object_dispose_.1134
- ___Block_byref_object_dispose_.3368
- ___Block_byref_object_dispose_.3586
- ___Block_byref_object_dispose_.3810
- ___Block_byref_object_dispose_.4581
- ___Block_byref_object_dispose_.4804
- ___Block_byref_object_dispose_.5816
- ___Block_byref_object_dispose_.6055
- ___Block_byref_object_dispose_.6171
- ___Block_byref_object_dispose_.6311
- ___Block_byref_object_dispose_.6403
- ___Block_byref_object_dispose_.745
- ___CoreTelephonyLibraryCore_block_invoke
- ___block_descriptor_48_e8_32s40r_e40_v24?0"WFDatabaseObjectDescriptor"8^B16ls32l8r40l8
- ___block_literal_global.108
- ___block_literal_global.1147
- ___block_literal_global.1343
- ___block_literal_global.149
- ___block_literal_global.155
- ___block_literal_global.1645
- ___block_literal_global.165
- ___block_literal_global.170
- ___block_literal_global.172
- ___block_literal_global.172.7384
- ___block_literal_global.174
- ___block_literal_global.1763
- ___block_literal_global.179
- ___block_literal_global.183
- ___block_literal_global.183.3474
- ___block_literal_global.190
- ___block_literal_global.193
- ___block_literal_global.195
- ___block_literal_global.217
- ___block_literal_global.222
- ___block_literal_global.235
- ___block_literal_global.2376
- ___block_literal_global.238
- ___block_literal_global.239
- ___block_literal_global.252
- ___block_literal_global.252.2309
- ___block_literal_global.256
- ___block_literal_global.256.5520
- ___block_literal_global.261
- ___block_literal_global.264
- ___block_literal_global.267
- ___block_literal_global.283
- ___block_literal_global.2837
- ___block_literal_global.295
- ___block_literal_global.295.5468
- ___block_literal_global.2975
- ___block_literal_global.324
- ___block_literal_global.339
- ___block_literal_global.3469
- ___block_literal_global.360
- ___block_literal_global.3603
- ___block_literal_global.362
- ___block_literal_global.3855
- ___block_literal_global.387
- ___block_literal_global.4066
- ___block_literal_global.4866
- ___block_literal_global.5099
- ___block_literal_global.545
- ___block_literal_global.5604
- ___block_literal_global.575
- ___block_literal_global.5828
- ___block_literal_global.6053
- ___block_literal_global.6194
- ___block_literal_global.6395
- ___block_literal_global.648
- ___block_literal_global.6639
- ___block_literal_global.6877
- ___block_literal_global.6997
- ___block_literal_global.7400
- ___block_literal_global.746
- ___block_literal_global.7472
- ___block_literal_global.80
- ___block_literal_global.989
- ___get_CTServerConnectionCreateWithIdentifierSymbolLoc_block_invoke
- ___get_CTServerConnectionGetCellularDataIsEnabledSymbolLoc_block_invoke
- __unnamed_array_storage.5548
- _audit_stringCoreTelephony
- _block_descriptor.19
- _defaultSettings.onceToken
- _defaultSettings.settings
- _get_CTServerConnectionCreateWithIdentifierSymbolLoc.ptr
- _get_CTServerConnectionGetCellularDataIsEnabledSymbolLoc.ptr
- _objc_msgSend$addRecordZonesToSave:recordZoneIDsToDelete:
- _objc_msgSend$associatedBundleIdentifier
- _objc_msgSend$autoShortcutsProvider
- _objc_msgSend$configuredStaccatoActionFromTemplate:valuesByParameterKey:completion:
- _objc_msgSend$connection
- _objc_msgSend$contextualActionIcon
- _objc_msgSend$fetchChangesForZoneIDs:completionHandler:
- _objc_msgSend$initWithDatabase:dataSource:metadata:
- _objc_msgSend$initWithIntent:sectionIdentifier:named:appShortcutIdentifier:systemImageName:templateParameterValues:contextualParameters:shortcutsMetadata:
- _objc_msgSend$modifyPendingChangesInZoneIDs:completionHandler:
- _objc_msgSend$sectionIdentifier
- _objc_msgSend$setBundleIdentifier:
- _objc_msgSend$setIntentIdentifier:
- _objc_msgSend$setSectionIdentifier:
- _objc_msgSend$setSuccess:
- _objc_msgSend$spotlightDomainIdentifier
- _objc_msgSend$syncV2Enabled
- _objc_msgSend$updateCurrentSyncServiceIfNeeded
- _objectdestroy.58Tm
- _objectdestroy.67Tm
- _symbolic _____ 11WorkflowKit07WFCloudB7LibraryC
CStrings:
+ "\a"
+ "%s App Shortcut %@ is disabled"
+ "%s App Shortcuts preferences updated, triggering re-index for %@"
+ "%s Application moved into foreground, migrating to Coherence-backed library"
+ "%s Application moved into foreground, updating account status"
+ "%s Cellular settings updated, triggering toggle sync"
+ "%s Coherence feature flag enabled: %i, library migration enabled: %i"
+ "%s Completed updating system action type: %@, success: %i"
+ "%s Constructing library CKRecord for recordID: %{public}@"
+ "%s Current action for system action type: %@ needs updating: %@"
+ "%s Database changed, checking for App Shortcuts preferences"
+ "%s Database update doesn't contain App Shortcut preferences"
+ "%s Detected system action source change due to: %@, migrating actions if necessary"
+ "%s Failed to construct configured action with template: %@."
+ "%s Failed to fetch current workflow state due to: %@"
+ "%s Failed to fetch library record with error: %{public}@"
+ "%s Failed to fetch server record for library"
+ "%s Failed to find link action for default action identifier: %@"
+ "%s Failed to get identifier from library CKRecord with CKRecordID %{public}@"
+ "%s Failed to handle CKErrorServerRecordChanged error for library"
+ "%s Failed to handle fetched library record: %{public}@"
+ "%s Failed to handle unknown item error for library record: %{public}@"
+ "%s Failed to load WFLibraryRecord from descriptor: %{public}@, descriptor = %@"
+ "%s Failed to read configured action for type: %@ due to: %@"
+ "%s Failed to save library record: %{public}@"
+ "%s Failed to start monitoring due to: %@"
+ "%s Failed to unarchive state serialization: %@"
+ "%s Forwarding database change notification."
+ "%s Handling CKErrorServerRecordChanged error for sent library, clientRecord.recordChangeTag = %{public}@, serverRecord.recordChangeTag = %{public}@, ancestorRecord.recordChangeTag = %{public}@"
+ "%s Handling fetched library record: %@"
+ "%s Handling saved library record: %{public}@"
+ "%s Library changed in the database; adding record id to save"
+ "%s Migrating from old sync engine metadata blob to new sync engine state serialization"
+ "%s Not resuming queue due to missing trigger id"
+ "%s Received database change for library but the sync hashes remain the same, skipping sync up"
+ "%s Received media suggestion update for %@, triggering update"
+ "%s Received valid database change notification."
+ "%s Returning library CKRecord: %{public}@"
+ "%s Shortcuts/toprak_syncengine feature flag disabled, using legacy sync service"
+ "%s Shortcuts/toprak_syncengine feature flag enabled, using Toprak sync service"
+ "%s Started monitoring for changes for system actions."
+ "%s Successfully handled server record change for library"
+ "%s Successfuly saved updated action %@ of type %@."
+ "%s Sync engine failed to save CKRecord: error domain = %{public}@, code = %{public}ld, error = %{public}@, record = %@, partial errors = %{public}@"
+ "%s Sync engine metadata is empty, initializing configuration with nil state serialization"
+ "%s Unable to find default action for action button."
+ "%s Unable to save updated action %@ of type %@ due to: %@"
+ "%s Updated action for system action type: %@ is: %@"
+ "-[VCCKShortcutSyncCoordinator observeValueForKeyPath:ofObject:change:context:]_block_invoke"
+ "-[VCCKShortcutSyncCoordinator observeValueForKeyPath:ofObject:change:context:]_block_invoke_2"
+ "-[VCCKShortcutSyncCoordinator updateCurrentSyncService]"
+ "-[VCCKShortcutSyncService handleSavedLibraryRecord:]"
+ "-[VCCKShortcutSyncService handleSendLibraryConflictWithClientRecord:serverRecord:ancestorRecord:]"
+ "-[VCCKShortcutSyncService handleSendLibraryConflictWithClientRecord:serverRecord:ancestorRecord:]_block_invoke"
+ "-[VCCKShortcutSyncService libraryRecordForRecordID:]"
+ "-[VCCKShortcutSyncService recordToSaveForRecordID:]_block_invoke"
+ "-[VCCKShortcutSyncService syncEngineDidDeleteRecordWithID:]_block_invoke"
+ "-[VCCKShortcutSyncService syncEngineDidDeleteRecordZoneWithID:]"
+ "-[VCCKShortcutSyncService syncEngineDidFetchRecord:]_block_invoke"
+ "-[VCCKShortcutSyncService syncEngineDidSaveRecord:]_block_invoke"
+ "-[VCCKShortcutSyncService syncEngineDidSaveRecordZone:]"
+ "-[VCCKShortcutSyncService syncEngineDidUpdateMetadata:]"
+ "-[VCCKShortcutSyncService syncEngineFailedToDeleteRecordWithID:error:]"
+ "-[VCCKShortcutSyncService syncEngineFailedToDeleteRecordZoneWithID:error:]"
+ "-[VCCKShortcutSyncService syncEngineFailedToSaveRecord:error:]_block_invoke"
+ "-[VCCKShortcutSyncService syncEngineFailedToSaveRecordZone:error:]"
+ "-[VCCKShortcutSyncService syncEngineRecordWithIDWasDeleted:recordType:]_block_invoke"
+ "-[VCCKShortcutSyncService syncEngineZoneWithIDChanged:]"
+ "-[VCCKShortcutSyncService syncEngineZoneWithIDWasDeleted:]"
+ "-[VCCKShortcutSyncService syncEngineZoneWithIDWasPurged:]"
+ "-[WFConfiguredSystemActionMigrator databaseDidChange:modified:inserted:removed:]"
+ "-[WFConfiguredSystemActionMigrator handleDatabaseChangeWithDelay]"
+ "-[WFConfiguredSystemActionMigrator startMonitoring]_block_invoke"
+ "-[WFConfiguredSystemActionMigrator updateActionsIfNeededWithReason:]"
+ "-[WFConfiguredSystemActionMigrator updateConfiguredSystemActionOfType:]"
+ "-[WFConfiguredSystemActionMigrator updatedConfiguredSystemActionFrom:]"
+ "-[WFConfiguredSystemActionProvider configuredStaccatoActionFromTemplate:valuesByParameterKey:error:]"
+ "-[WFConfiguredSystemActionProvider configuredSystemActionForActionType:]"
+ "-[WFConfiguredSystemActionProvider defaultSystemActionForActionType:]"
+ "-[WFConfiguredSystemActionProvider saveUpdatedAction:forActionType:]"
+ "-[WFContextualActionSpotlightSyncService cellularSettingsUpdated]"
+ "-[WFContextualActionSpotlightSyncService queue_v2GetAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]"
+ "-[WFContextualActionSpotlightSyncService queue_v2GetAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke"
+ "-[WFContextualActionSpotlightSyncService queue_v2GetAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke_2"
+ "-[WFTopHitsAppShortcutsUpdater registerForUpcomingMediaSuggestionChanged]_block_invoke"
+ "@\"CKRecord\"16@?0@\"CKRecordID\"8"
+ "@\"CKSyncEngineFetchChangesOptions\""
+ "@\"CKSyncEngineFetchChangesOptions\"32@0:8@\"CKSyncEngine\"16@\"CKSyncEngineFetchChangesContext\"24"
+ "@\"CKSyncEngineRecordZoneChangeBatch\"32@0:8@\"CKSyncEngine\"16@\"CKSyncEngineSendChangesContext\"24"
+ "@\"CKSyncEngineSendChangesOptions\""
+ "@\"NSString\"16@?0@\"WFDatabaseObjectDescriptor\"8"
+ "@\"WFConfiguredSystemActionProvider\""
+ "@\"WFContextualAction\"24@?0@\"WFExecutableAppShortcut\"8Q16"
+ "An error occurred while running %@. (%@, %i)"
+ "B\x15\x12"
+ "CKSyncEngineDelegate"
+ "DatabaseChanged"
+ "Failed to handle saved library because database record is invalid"
+ "Failed to handle saved library because trying to save library record failed"
+ "Failed to handle unknown item error for library because database record is invalid"
+ "Failed to handle unknown item error for library because trying to save library record failed"
+ "Failed to merge libraries because database record is invalid"
+ "Failed to merge libraries because other library is malformed"
+ "Failed to merge libraries because trying to save library record failed"
+ "Insufficient space allocated to copy string contents"
+ "SBSystemActionConfiguredActionArchive"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"CKSyncEngineFetchChangesOptions\",R,N,V_fetchChangesOptions"
+ "T@\"CKSyncEngineSendChangesOptions\",R,N,V_sendChangesOptions"
+ "T@\"NSData\",?,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"WFConfiguredSystemActionProvider\",R,N,V_actionProvider"
+ "T@\"WFDatabase\",&,N,V_database"
+ "T@\"WFDebouncer\",&,N,V_databaseDeboucer"
+ "TB,R,N,GisUsingToprakSyncEngine"
+ "Unable to construct the default action"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "WFConfiguredSystemActionMigrator"
+ "WFConfiguredSystemActionProvider"
+ "_TtC14VoiceShortcuts26VCCKLibrarySyncCoordinator"
+ "_actionProvider"
+ "_databaseDeboucer"
+ "_fetchChangesOptions"
+ "_sendChangesOptions"
+ "actionProvider"
+ "addPendingDatabaseChanges:"
+ "addPendingRecordZoneChanges:"
+ "appShortcutBatchSize"
+ "applicationWillLaunchInForegroundForRunningContext:isLastAction:"
+ "availableActionTypes"
+ "cellularSettingsUpdated"
+ "coherenceEnabled"
+ "coherenceEnabledWithCompletion:"
+ "coherenceMigrationEnabled"
+ "coherenceMigrationEnabledWithCompletion:"
+ "com.apple.shortcuts.WFConfiguredSystemActionMigrator"
+ "com.apple.springboard"
+ "configuredStaccatoActionFromTemplate:valuesByParameterKey:error:"
+ "configuredSystemActionForActionType:"
+ "containsRecordID:"
+ "dataFileRepresentation"
+ "databaseDeboucer"
+ "defaultSystemActionForActionType:"
+ "deletedRecordIDs"
+ "deletedZoneIDs"
+ "deletions"
+ "failedRecordDeletes"
+ "failedRecordSaves"
+ "failedZoneDeletes"
+ "failedZoneSaves"
+ "fetchAppShortcutsForBundleIdentifiers:localeIdentifier:error:"
+ "fetchChangesOptions"
+ "fetchChangesWithOptions:completionHandler:"
+ "handleDatabaseChangeWithDelay"
+ "handleFetchedLibraryRecord:database:error:"
+ "handleSavedLibraryRecord:"
+ "handleSavedLibraryRecord:database:error:"
+ "handleSendLibraryConflictWithClientRecord:serverRecord:ancestorRecord:"
+ "handleServerRecordChangedErrorForRecord:database:error:"
+ "handleUnknownItemErrorForRecord:database:error:"
+ "id"
+ "initWithAppShortcutsDenyListEnvironment:environment:"
+ "initWithDatabase:stateSerialization:delegate:"
+ "initWithDatabaseProvider:actionProvider:"
+ "initWithDeprecatedData:"
+ "initWithExecutableAppShortcut:index:"
+ "initWithIdentifier:version:data:syncHash:"
+ "initWithIntent:named:previewIcon:appShortcutIdentifier:templateParameterValues:contextualParameters:shortcutsMetadata:"
+ "initWithLibraryRecord:zoneID:"
+ "initWithPendingChanges:recordProvider:"
+ "initWithRecordID:type:"
+ "initWithScope:"
+ "initWithWorkflow:shortcutsMetadata:"
+ "initWithZone:"
+ "initWithZoneIDs:"
+ "invalid Collection: less than 'count' elements in collection"
+ "isConfiguredSystemActionValid:"
+ "isLibraryRecordID:"
+ "isTopHitEligible"
+ "isUsingToprakSyncEngine"
+ "legacySpotlightDomainIdentifier"
+ "libraryIdentifierFromRecordID:error:"
+ "libraryIdentifierWithError:"
+ "libraryRecordForRecordID:"
+ "lnPropertyIdentifier"
+ "modifications"
+ "options"
+ "pendingRecordZoneChanges"
+ "queue_v2GetAppShortcutContextualActionsForBundleIdentifiers:completionHandler:"
+ "recordIDWithZoneID:libraryIdentifier:"
+ "recordToSaveForRecordID:"
+ "recordZone"
+ "removePendingRecordZoneChanges:"
+ "runEventsCount"
+ "saveSyncEventWithDate:trigger:success:errorDescription:"
+ "saveUpdatedAction:forActionType:"
+ "savedRecords"
+ "savedZones"
+ "scope"
+ "sendChangesOptions"
+ "sendChangesWithOptions:completionHandler:"
+ "setCoherenceMigrationEnabled:"
+ "setCoherenceMigrationStatus:completion:"
+ "setDatabase:"
+ "setDatabaseDeboucer:"
+ "setPlayCount:"
+ "shortcutsMetadata"
+ "spotlightIconWithParameterIdentifier:"
+ "spotlight_thumbnail_urls"
+ "startMonitoring"
+ "stateSerialization"
+ "stopMonitoring"
+ "syncEngine:handleEvent:"
+ "syncEngine:nextFetchChangesOptionsForContext:"
+ "syncEngine:nextRecordZoneChangeBatchForContext:"
+ "syncEngineDidDeleteRecordWithID:"
+ "syncEngineDidDeleteRecordZoneWithID:"
+ "syncEngineDidFetchRecord:"
+ "syncEngineDidSaveRecord:"
+ "syncEngineDidSaveRecordZone:"
+ "syncEngineDidUpdateMetadata:"
+ "syncEngineFailedToDeleteRecordWithID:error:"
+ "syncEngineFailedToDeleteRecordZoneWithID:error:"
+ "syncEngineFailedToSaveRecord:error:"
+ "syncEngineFailedToSaveRecordZone:error:"
+ "syncEngineRecordWithIDWasDeleted:recordType:"
+ "syncEngineZoneWithIDChanged:"
+ "syncEngineZoneWithIDWasDeleted:"
+ "syncEngineZoneWithIDWasPurged:"
+ "systemActionMigrator"
+ "toprakCoherenceEnabled"
+ "toprakEngineEnabled"
+ "toprakEngineEnabledWithCompletion:"
+ "updateActionsIfNeededWithReason:"
+ "updateConfiguredSystemActionOfType:"
+ "updateCurrentSyncService"
+ "updatedConfiguredSystemActionFrom:"
+ "useNewDataSource"
+ "usingToprakSyncEngine"
+ "v28@0:8B16@?<v@?@\"NSError\">20"
+ "v32@0:8@\"CKSyncEngine\"16@\"CKSyncEngineEvent\"24"
+ "v32@0:8@\"WFWorkflowRunningContext\"16@\"NSNumber\"24"
+ "wf_securelyArchivedDataWithRootObject:"
- "%s Application moved into foreground, updating account status if needed"
- "%s Auto Shortcuts preferences updated, triggering re-index"
- "%s Changes were requested while the app is foreground, syncing them up immediately"
- "%s Database changed, checking for Auto Shortcuts preferences"
- "%s Failed to construct configured action with action: %@."
- "%s Shortcuts/sync_v2 feature flag disabled, using Sync 1"
- "%s Shortcuts/sync_v2 feature flag enabled, using Toprak"
- "%s Sync engine failed to save CKRecord: error domain = %{public}@, code = %{public}ld, error = %{public}@, record = %@"
- "%s Unable to find default action with identifier: %@."
- "-[VCCKShortcutSyncCoordinator updateCurrentSyncServiceIfNeeded]"
- "-[VCCKShortcutSyncService syncEngine:didDeleteRecordWithID:]_block_invoke"
- "-[VCCKShortcutSyncService syncEngine:didDeleteRecordZoneWithID:]"
- "-[VCCKShortcutSyncService syncEngine:didFetchRecord:]_block_invoke"
- "-[VCCKShortcutSyncService syncEngine:didSaveRecord:]_block_invoke"
- "-[VCCKShortcutSyncService syncEngine:didSaveRecordZone:]"
- "-[VCCKShortcutSyncService syncEngine:didUpdateMetadata:]"
- "-[VCCKShortcutSyncService syncEngine:failedToDeleteRecordWithID:error:]"
- "-[VCCKShortcutSyncService syncEngine:failedToDeleteRecordZoneWithID:error:]"
- "-[VCCKShortcutSyncService syncEngine:failedToSaveRecord:error:]_block_invoke"
- "-[VCCKShortcutSyncService syncEngine:failedToSaveRecordZone:error:]"
- "-[VCCKShortcutSyncService syncEngine:recordToSaveForRecordID:]_block_invoke"
- "-[VCCKShortcutSyncService syncEngine:recordWithIDWasDeleted:recordType:]_block_invoke"
- "-[VCCKShortcutSyncService syncEngine:zoneWithIDChanged:]"
- "-[VCCKShortcutSyncService syncEngine:zoneWithIDWasDeleted:]"
- "-[VCCKShortcutSyncService syncEngine:zoneWithIDWasPurged:]"
- "@\"LNAutoShortcutsProvider\""
- "Action template with identifier (%@) does not resolve to valid configured staccato action"
- "An error occurred while running %@"
- "An unknown error occurred while running your shortcut. (%@, %i)"
- "B\x15\x12\x11"
- "CTError"
- "CTError WF_CTServerConnectionGetCellularDataIsEnabled(CTServerConnectionRef, Boolean *)"
- "CTErrorDomain"
- "CTServerConnectionRef WF_CTServerConnectionCreateWithIdentifier(CFAllocatorRef, CFStringRef, CTServerConnectionCallback, _CTServerConnectionContext *)"
- "Default action template with identifier (%@) does not resolve to valid configured staccato action"
- "T@\"LNAutoShortcutsProvider\",R,N,V_autoShortcutsProvider"
- "T@\"NSData\",&,N,V_smartPromptPerWorkflowStateData"
- "T@\"NSData\",C,N"
- "TB,R,N,GisUsingSync2"
- "TB,R,N,V_hasSmartPromptPerWorkflowStateData"
- "T^{__CTServerConnection=},R,N,V_connection"
- "View the shortcut for more details. (%@, %i)"
- "VoiceShortcuts/ToprakEngine.swift"
- "WFCellularSettings"
- "WFCellularSettings.m"
- "WFCellularSettingsErrorDomain"
- "_CTServerConnectionCreateWithIdentifier"
- "_CTServerConnectionGetCellularDataIsEnabled"
- "_autoShortcutsProvider"
- "_connection"
- "_hasSmartPromptPerWorkflowStateData"
- "_smartPromptPerWorkflowStateData"
- "addRecordZonesToSave:recordZoneIDsToDelete:"
- "associatedBundleIdentifier"
- "autoShortcutsProvider"
- "com.apple.VoiceShortcuts.library.indexed"
- "connection"
- "contextualActionIcon"
- "hasSmartPromptPerWorkflowStateData"
- "initWithIntent:sectionIdentifier:named:appShortcutIdentifier:systemImageName:templateParameterValues:contextualParameters:shortcutsMetadata:"
- "isUsingSync2"
- "setBundleIdentifier:"
- "setIntentIdentifier:"
- "setSectionIdentifier:"
- "setSmartPromptPerWorkflowStateData:"
- "setSuccess:"
- "smartPromptPerWorkflowStateData"
- "softlink:r:path:/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony"
- "spotlightDomainIdentifier"
- "spotlight_view"
- "syncV2Enabled"
- "updateCurrentSyncServiceIfNeeded"
- "usingSync2"
- "v24@?0@\"WFDatabaseObjectDescriptor\"8^B16"
- "void *CoreTelephonyLibrary(void)"

```
