## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-4257.40.63.0.1
-  __TEXT.__text: 0x312420
+4257.40.69.0.0
+  __TEXT.__text: 0x313a24
   __TEXT.__auth_stubs: 0x1b40
-  __TEXT.__objc_methlist: 0x1a33c
+  __TEXT.__objc_methlist: 0x1a42c
   __TEXT.__const: 0x500
-  __TEXT.__cstring: 0x7d737
-  __TEXT.__oslogstring: 0x3c2d4
-  __TEXT.__gcc_except_tab: 0x1a688
+  __TEXT.__cstring: 0x7d9de
+  __TEXT.__oslogstring: 0x3c34c
+  __TEXT.__gcc_except_tab: 0x1a68c
   __TEXT.__ustring: 0x88
-  __TEXT.__unwind_info: 0xa020
-  __TEXT.__objc_classname: 0x2b0f
-  __TEXT.__objc_methname: 0x44819
-  __TEXT.__objc_methtype: 0x905f
-  __TEXT.__objc_stubs: 0x2f2c0
+  __TEXT.__unwind_info: 0xa068
+  __TEXT.__objc_classname: 0x2b47
+  __TEXT.__objc_methname: 0x449db
+  __TEXT.__objc_methtype: 0x90b4
+  __TEXT.__objc_stubs: 0x2f480
   __DATA_CONST.__got: 0x1718
-  __DATA_CONST.__const: 0x95f0
-  __DATA_CONST.__objc_classlist: 0xa70
+  __DATA_CONST.__const: 0x9640
+  __DATA_CONST.__objc_classlist: 0xa80
   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x288
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe750
+  __DATA_CONST.__objc_selrefs: 0xe7c0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x930
-  __DATA_CONST.__objc_arraydata: 0xe58
+  __DATA_CONST.__objc_superrefs: 0x940
+  __DATA_CONST.__objc_arraydata: 0xe60
   __AUTH_CONST.__auth_got: 0xdb0
-  __AUTH_CONST.__const: 0x2ba0
-  __AUTH_CONST.__cfstring: 0x22a40
-  __AUTH_CONST.__objc_const: 0x3d458
-  __AUTH_CONST.__objc_intobj: 0xbb8
-  __AUTH_CONST.__objc_arrayobj: 0x210
+  __AUTH_CONST.__const: 0x2c00
+  __AUTH_CONST.__cfstring: 0x22b80
+  __AUTH_CONST.__objc_const: 0x3d590
+  __AUTH_CONST.__objc_intobj: 0xbd0
+  __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x50
-  __AUTH.__objc_data: 0x2828
+  __AUTH.__objc_data: 0x28c8
   __AUTH.__data: 0x18
   __DATA.__objc_ivar: 0x1fb8
   __DATA.__data: 0x2740

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E06C61C0-6CF1-305C-8B16-9AE68075F220
-  Functions: 13620
-  Symbols:   44348
-  CStrings:  23327
+  UUID: DFF412C4-014C-333A-B172-0E930B9363DE
+  Functions: 13643
+  Symbols:   44425
+  CStrings:  23356
 
Symbols:
+ +[BRCPQLInjectionDomainSyncState _getPQLInjectionWithDesiredSyncStates:]
+ +[BRCPQLInjectionJobStates _getPQLInjectionFromJobStates:]
+ +[BRCPQLInjectionJobStates _getPQLInjectionFromJobStates:].cold.1
+ -[BRCAccountSession performAsyncOnClientReadDatabaseWorkloop:]
+ -[BRCAppLibrary _bundleIDsDescription]
+ -[BRCClientDatabaseFacade getSyncState:ignoredZones:error:]
+ -[BRCClientDatabaseFacade item:hasSyncUpJobState:]
+ -[BRCCloudDocsAppsMonitor _dumpAppIDsByAppLibraryIDToContext:]
+ -[BRCCloudDocsAppsMonitor _dumpCloudDocsAppLibrariesByAppIDToContext:]
+ -[BRCGlobalProgress _isSyncUpSuspendedForDocument:]
+ -[BRCPQLInjectionDomainSyncState initWithDesiredSyncStates:]
+ -[BRCPQLInjectionJobStates initWithJobStates:]
+ -[NSError(BRCAdditions) brc_obfuscate]
+ GCC_except_table172
+ GCC_except_table180
+ GCC_except_table215
+ GCC_except_table222
+ GCC_except_table235
+ GCC_except_table246
+ GCC_except_table254
+ GCC_except_table271
+ GCC_except_table295
+ GCC_except_table332
+ GCC_except_table449
+ _OBJC_CLASS_$_BRCPQLInjectionDomainSyncState
+ _OBJC_CLASS_$_BRCPQLInjectionJobStates
+ _OBJC_METACLASS_$_BRCPQLInjectionDomainSyncState
+ _OBJC_METACLASS_$_BRCPQLInjectionJobStates
+ __OBJC_$_CLASS_METHODS_BRCPQLInjectionDomainSyncState
+ __OBJC_$_CLASS_METHODS_BRCPQLInjectionJobStates
+ __OBJC_$_INSTANCE_METHODS_BRCPQLInjectionDomainSyncState
+ __OBJC_$_INSTANCE_METHODS_BRCPQLInjectionJobStates
+ __OBJC_CLASS_RO_$_BRCPQLInjectionDomainSyncState
+ __OBJC_CLASS_RO_$_BRCPQLInjectionJobStates
+ __OBJC_METACLASS_RO_$_BRCPQLInjectionDomainSyncState
+ __OBJC_METACLASS_RO_$_BRCPQLInjectionJobStates
+ ___109-[BRCXPCRegularIPCsClient startOperation:toProcessSubitemsWithItemID:maxSubsharesFailures:processType:reply:]_block_invoke.646
+ ___113-[BRCAccountSession(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke.352
+ ___113-[BRCAccountSession(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke_2.353
+ ___234-[BRCAppLibrary itemsEnumeratorWithRankMin:rankMax:namePrefix:withDeadItems:shouldIncludeFolders:shouldIncludeOnlyFolders:shouldIncludeDocumentsScope:shouldIncludeDataScope:shouldIncludeExternalScope:shouldIncludeTrashScope:count:db:]_block_invoke.143
+ ___38-[BRCAppLibrary _bundleIDsDescription]_block_invoke
+ ___48-[BRCAppLibrary resumeQueryBasedSyncIfNecessary]_block_invoke.149
+ ___52-[BRCAppLibrary waitForRootIngestionWithCompletion:]_block_invoke.178
+ ___53-[BRCXPCRegularIPCsClient currentNotifRankWithReply:]_block_invoke.502
+ ___54-[BRCAccountSession(BRCDatabaseManager) _startWatcher]_block_invoke.44
+ ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.717
+ ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.721
+ ___56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.668
+ ___56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.668.cold.1
+ ___58-[BRCAppLibrary flushAndForceIngestRootAndDocumentsFolder]_block_invoke.177
+ ___58-[BRCAppLibrary flushAndForceIngestRootAndDocumentsFolder]_block_invoke.177.cold.1
+ ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.464
+ ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.464.cold.1
+ ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.471
+ ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.473
+ ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.614
+ ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.614.cold.1
+ ___62-[BRCAccountSession performAsyncOnClientReadDatabaseWorkloop:]_block_invoke
+ ___62-[BRCCloudDocsAppsMonitor _dumpAppIDsByAppLibraryIDToContext:]_block_invoke
+ ___62-[BRCCloudDocsAppsMonitor _dumpAppIDsByAppLibraryIDToContext:]_block_invoke_2
+ ___62-[BRCCloudDocsAppsMonitor _dumpAppIDsByAppLibraryIDToContext:]_block_invoke_3
+ ___62-[BRCXPCRegularIPCsClient copyCurrentUserIdentifierWithReply:]_block_invoke.609
+ ___65-[BRCXPCRegularIPCsClient _handleAcceptingCKShareMetadata:reply:]_block_invoke.666
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.662
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.662.cold.1
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.662.cold.2
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.663
+ ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.616
+ ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.617
+ ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.619
+ ___70-[BRCAccountSession(BRCDatabaseManager) _registerObfuscationFunction:]_block_invoke_4
+ ___70-[BRCAccountSession(BRCDatabaseManager) _registerObfuscationFunction:]_block_invoke_5
+ ___70-[BRCCloudDocsAppsMonitor _dumpCloudDocsAppLibrariesByAppIDToContext:]_block_invoke
+ ___70-[BRCCloudDocsAppsMonitor _dumpCloudDocsAppLibrariesByAppIDToContext:]_block_invoke_2
+ ___70-[BRCCloudDocsAppsMonitor _dumpCloudDocsAppLibrariesByAppIDToContext:]_block_invoke_3
+ ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.650
+ ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.652
+ ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.652.cold.1
+ ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.653
+ ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.653.cold.1
+ ___71-[BRCXPCRegularIPCsClient _t_extractMetadataForAllContainersWithReply:]_block_invoke.712
+ ___71-[BRCXPCRegularIPCsClient startOperation:toCopyShareURLForShare:reply:]_block_invoke.658
+ ___72-[BRCXPCRegularIPCsClient copyCurrentUserNameAndDisplayHandleWithReply:]_block_invoke.610
+ ___72-[BRCXPCRegularIPCsClient startOperation:toCopyAvailableQuotaWithReply:]_block_invoke.604
+ ___73-[BRCXPCRegularIPCsClient handleCloudKitShareMetadata:completionHandler:]_block_invoke.667
+ ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.579
+ ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.581
+ ___74+[BRCAccountSession(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke.77
+ ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.623
+ ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.625
+ ___75-[BRCAccountSession(BRCDatabaseManager) _registerDynamicDBFunctions:error:]_block_invoke.91
+ ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.620
+ ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.621
+ ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.612
+ ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.612.cold.1
+ ___76-[BRCXPCRegularIPCsClient startOperation:toCopySharingInfoWithItemID:reply:]_block_invoke.576
+ ___76-[BRCXPCRegularIPCsClient startOperation:toUploadAllFilesInContainer:reply:]_block_invoke.607
+ ___80-[BRCXPCRegularIPCsClient _startOperation:toCopySharingInfoWithLocalItem:reply:]_block_invoke.567
+ ___81-[BRCXPCRegularIPCsClient startOperation:toCopyParticipantTokenWithItemID:reply:]_block_invoke.642
+ ___81-[BRCXPCRegularIPCsClient startOperation:toCopySharingAccessTokenOfItemID:reply:]_block_invoke.578
+ ___81-[BRCXPCRegularIPCsClient startOperation:toPrepFolderForSharingWithItemID:reply:]_block_invoke.644
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.265
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.265.cold.1
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.273
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.277
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.277.cold.1
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.277.cold.2
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.504
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.504.cold.1
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.504.cold.2
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.504.cold.3
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.508
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.518
+ ___84-[BRCXPCRegularIPCsClient getEnhancedDrivePrivacyStatusForContainer:onServer:reply:]_block_invoke.704
+ ___84-[BRCXPCRegularIPCsClient getEnhancedDrivePrivacyStatusForContainer:onServer:reply:]_block_invoke.705
+ ___84-[BRCXPCRegularIPCsClient startOperation:toAcceptShareLink:skipAcceptDialogs:reply:]_block_invoke.648
+ ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.462
+ ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.463
+ ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.519
+ ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.521
+ ___88-[BRCXPCRegularIPCsClient startOperation:toCopySharingWebAuthTokenForContainerID:reply:]_block_invoke.583
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.586
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.587
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.588
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.589
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.590
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.598
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.600
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke_2.596
+ ___91-[BRCXPCRegularIPCsClient startOperation:toModifyRecordAccessWithItemID:allowAccess:reply:]_block_invoke.634
+ ___94-[BRCXPCRegularIPCsClient _doesAnyRecordExistInContainerMetadataRecordName:completionHandler:]_block_invoke.680
+ ___95-[BRCXPCRegularIPCsClient setEnhancedDrivePrivacyEnabled:forContainer:onServer:onClient:reply:]_block_invoke.693
+ ___95-[BRCXPCRegularIPCsClient setEnhancedDrivePrivacyEnabled:forContainer:onServer:onClient:reply:]_block_invoke.701
+ ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.405
+ ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.405.cold.1
+ ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.409
+ ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke_12
+ ___block_descriptor_40_e8_32s_e22_v24?0"NSString"8^B16ls32l8
+ ___block_descriptor_40_e8_32s_e32_v32?0"NSString"8"NSSet"16^B24ls32l8
+ ___block_descriptor_56_e8_32s40bs_e33_v16?0"BRCClientDatabaseFacade"8ls32l8s40l8
+ ___block_literal_global.180
+ ___block_literal_global.276
+ ___block_literal_global.351
+ ___block_literal_global.360
+ ___block_literal_global.368
+ ___block_literal_global.385
+ ___block_literal_global.390
+ ___block_literal_global.395
+ ___block_literal_global.411
+ ___block_literal_global.416
+ ___block_literal_global.421
+ ___block_literal_global.426
+ ___block_literal_global.431
+ ___block_literal_global.436
+ ___block_literal_global.441
+ ___block_literal_global.454
+ ___block_literal_global.459
+ ___block_literal_global.464
+ ___block_literal_global.469
+ ___block_literal_global.655
+ ___block_literal_global.677
+ ___block_literal_global.84
+ ___block_literal_global.947
+ __brc_sqlite3_result_archived_value
+ _objc_msgSend$_bundleIDsDescription
+ _objc_msgSend$_dumpAppIDsByAppLibraryIDToContext:
+ _objc_msgSend$_dumpCloudDocsAppLibrariesByAppIDToContext:
+ _objc_msgSend$_getPQLInjectionFromJobStates:
+ _objc_msgSend$_getPQLInjectionWithDesiredSyncStates:
+ _objc_msgSend$_isSyncUpSuspendedForDocument:
+ _objc_msgSend$br_obfuscateAliasTarget
+ _objc_msgSend$br_obfuscatedDotOrTildaSeparatedComponents
+ _objc_msgSend$brc_errorItemIneligibleFromSyncForInode:localizedDescription:
+ _objc_msgSend$brc_obfuscate
+ _objc_msgSend$getSyncState:ignoredZones:error:
+ _objc_msgSend$initWithDesiredSyncStates:
+ _objc_msgSend$initWithJobStates:
+ _objc_msgSend$item:hasSyncUpJobState:
+ _objc_msgSend$performAsyncOnClientReadDatabaseWorkloop:
- GCC_except_table126
- GCC_except_table131
- GCC_except_table135
- GCC_except_table144
- GCC_except_table174
- GCC_except_table178
- GCC_except_table182
- GCC_except_table186
- GCC_except_table220
- GCC_except_table238
- GCC_except_table244
- GCC_except_table273
- GCC_except_table294
- GCC_except_table330
- ___109-[BRCXPCRegularIPCsClient startOperation:toProcessSubitemsWithItemID:maxSubsharesFailures:processType:reply:]_block_invoke.652
- ___113-[BRCAccountSession(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke.354
- ___113-[BRCAccountSession(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke_2.355
- ___234-[BRCAppLibrary itemsEnumeratorWithRankMin:rankMax:namePrefix:withDeadItems:shouldIncludeFolders:shouldIncludeOnlyFolders:shouldIncludeDocumentsScope:shouldIncludeDataScope:shouldIncludeExternalScope:shouldIncludeTrashScope:count:db:]_block_invoke.142
- ___41-[BRCCloudDocsAppsMonitor dumpToContext:]_block_invoke
- ___41-[BRCCloudDocsAppsMonitor dumpToContext:]_block_invoke_2
- ___48-[BRCAppLibrary resumeQueryBasedSyncIfNecessary]_block_invoke.148
- ___52-[BRCAppLibrary waitForRootIngestionWithCompletion:]_block_invoke.177
- ___53-[BRCXPCRegularIPCsClient currentNotifRankWithReply:]_block_invoke.508
- ___54-[BRCAccountSession(BRCDatabaseManager) _startWatcher]_block_invoke_2
- ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.723
- ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.727
- ___56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.674
- ___56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.674.cold.1
- ___58-[BRCAppLibrary flushAndForceIngestRootAndDocumentsFolder]_block_invoke.175
- ___58-[BRCAppLibrary flushAndForceIngestRootAndDocumentsFolder]_block_invoke.175.cold.1
- ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.470
- ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.470.cold.1
- ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.477
- ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.479
- ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.620
- ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.620.cold.1
- ___62-[BRCXPCRegularIPCsClient copyCurrentUserIdentifierWithReply:]_block_invoke.615
- ___65-[BRCXPCRegularIPCsClient _handleAcceptingCKShareMetadata:reply:]_block_invoke.672
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.668
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.668.cold.1
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.668.cold.2
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.669
- ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.622
- ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.623
- ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.625
- ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.656
- ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.658
- ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.658.cold.1
- ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.659
- ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.659.cold.1
- ___71-[BRCXPCRegularIPCsClient _t_extractMetadataForAllContainersWithReply:]_block_invoke.718
- ___71-[BRCXPCRegularIPCsClient startOperation:toCopyShareURLForShare:reply:]_block_invoke.664
- ___72-[BRCXPCRegularIPCsClient copyCurrentUserNameAndDisplayHandleWithReply:]_block_invoke.616
- ___72-[BRCXPCRegularIPCsClient startOperation:toCopyAvailableQuotaWithReply:]_block_invoke.610
- ___73-[BRCXPCRegularIPCsClient handleCloudKitShareMetadata:completionHandler:]_block_invoke.673
- ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.585
- ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.587
- ___74+[BRCAccountSession(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke.79
- ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.629
- ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.631
- ___75-[BRCAccountSession(BRCDatabaseManager) _registerDynamicDBFunctions:error:]_block_invoke.93
- ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.626
- ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.627
- ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.618
- ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.618.cold.1
- ___76-[BRCXPCRegularIPCsClient startOperation:toCopySharingInfoWithItemID:reply:]_block_invoke.582
- ___76-[BRCXPCRegularIPCsClient startOperation:toUploadAllFilesInContainer:reply:]_block_invoke.613
- ___80-[BRCXPCRegularIPCsClient _startOperation:toCopySharingInfoWithLocalItem:reply:]_block_invoke.573
- ___81-[BRCXPCRegularIPCsClient startOperation:toCopyParticipantTokenWithItemID:reply:]_block_invoke.648
- ___81-[BRCXPCRegularIPCsClient startOperation:toCopySharingAccessTokenOfItemID:reply:]_block_invoke.584
- ___81-[BRCXPCRegularIPCsClient startOperation:toPrepFolderForSharingWithItemID:reply:]_block_invoke.650
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.269
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.269.cold.1
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.275
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.279
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.279.cold.1
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.279.cold.2
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.510
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.510.cold.1
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.510.cold.2
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.510.cold.3
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.514
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.524
- ___84-[BRCXPCRegularIPCsClient getEnhancedDrivePrivacyStatusForContainer:onServer:reply:]_block_invoke.710
- ___84-[BRCXPCRegularIPCsClient getEnhancedDrivePrivacyStatusForContainer:onServer:reply:]_block_invoke.711
- ___84-[BRCXPCRegularIPCsClient startOperation:toAcceptShareLink:skipAcceptDialogs:reply:]_block_invoke.654
- ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.468
- ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.469
- ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.525
- ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.527
- ___88-[BRCXPCRegularIPCsClient startOperation:toCopySharingWebAuthTokenForContainerID:reply:]_block_invoke.589
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.592
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.594
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.596
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.601
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.604
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.605
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.606
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke_2.602
- ___91-[BRCXPCRegularIPCsClient startOperation:toModifyRecordAccessWithItemID:allowAccess:reply:]_block_invoke.640
- ___94-[BRCXPCRegularIPCsClient _doesAnyRecordExistInContainerMetadataRecordName:completionHandler:]_block_invoke.686
- ___95-[BRCXPCRegularIPCsClient setEnhancedDrivePrivacyEnabled:forContainer:onServer:onClient:reply:]_block_invoke.699
- ___95-[BRCXPCRegularIPCsClient setEnhancedDrivePrivacyEnabled:forContainer:onServer:onClient:reply:]_block_invoke.707
- ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.397
- ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.397.cold.1
- ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.401
- ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_literal_global.130
- ___block_literal_global.179
- ___block_literal_global.278
- ___block_literal_global.353
- ___block_literal_global.362
- ___block_literal_global.370
- ___block_literal_global.387
- ___block_literal_global.403
- ___block_literal_global.413
- ___block_literal_global.418
- ___block_literal_global.423
- ___block_literal_global.428
- ___block_literal_global.433
- ___block_literal_global.438
- ___block_literal_global.451
- ___block_literal_global.456
- ___block_literal_global.661
- ___block_literal_global.683
- ___block_literal_global.86
- ___block_literal_global.91
- ___block_literal_global.946
- _objc_msgSend$brc_errorItemIneligibleFromSyncForInode:
CStrings:
+ "(%@ OR %@)"
+ "(item_localsyncupstate = 3 AND NOT EXISTS (SELECT 1 FROM client_uploads WHERE throttle_id = ci.rowid AND throttle_state IN (%d, %d, %d, %d, %d, %d)))"
+ "(item_localsyncupstate = 4 AND NOT EXISTS (SELECT 1 FROM client_sync_up WHERE throttle_id = ci.rowid AND throttle_state IN (%d, %d)))"
+ "+[BRCPQLInjectionJobStates _getPQLInjectionFromJobStates:]"
+ ", %@"
+ "-[BRCClientDatabaseFacade getSyncState:ignoredZones:error:]"
+ "AND throttle_state = %@"
+ "AND throttle_state IN (%@"
+ "B32@0:8@\"BRCLocalItem\"16@\"NSArray\"24"
+ "BRCPQLInjectionDomainSyncState"
+ "BRCPQLInjectionJobStates"
+ "OBFUSCATE_ALIAS_TARGET"
+ "OBFUSCATE_ERROR"
+ "Q40@0:8Q16@\"NSIndexSet\"24^@32"
+ "Q40@0:8Q16@24^@32"
+ "SELECT 1 FROM client_sync_up WHERE throttle_id = %llu %@"
+ "SELECT DISTINCT item_localsyncupstate, HEX(version_content_signature) IN ('013F', '1B3F') FROM client_items as ci WHERE item_localsyncupstate != 0       AND item_scope = 2       AND NOT item_id_is_documents(item_id)       AND NOT indexset_contains(%p, zone_rowid)       AND %@"
+ "UPDATE client_items SET item_localname = OBFUSCATE(rowid, item_localname), item_bouncedname = OBFUSCATE(rowid, item_bouncedname), item_filename = OBFUSCATE(rowid, item_filename), item_trash_put_back_path = OBFUSCATE_PATH(rowid, item_trash_put_back_path), version_name = OBFUSCATE(rowid, version_name), version_block_sync_until_bundle_id = NULL, version_upload_error = OBFUSCATE_ERROR(version_upload_error)"
+ "UPDATE client_uploads SET upload_error = OBFUSCATE_ERROR(upload_error)"
+ "UPDATE server_items SET item_filename = OBFUSCATE(rowid, item_filename), item_origname = OBFUSCATE(rowid, item_origname), item_trash_put_back_path = OBFUSCATE_PATH(rowid, item_trash_put_back_path), version_name = OBFUSCATE(rowid, version_name), item_alias_target = OBFUSCATE_ALIAS_TARGET(item_alias_target)"
+ "[CRIT] UNREACHABLE: jobStates is not expected to be empty%@"
+ "[CRIT] someone ripped the database from under our feet%@"
+ "[DEBUG] shared document %@ is read-only, do not sync%@"
+ "_bundleIDsDescription"
+ "_dumpAppIDsByAppLibraryIDToContext:"
+ "_dumpCloudDocsAppLibrariesByAppIDToContext:"
+ "_getPQLInjectionFromJobStates:"
+ "_getPQLInjectionWithDesiredSyncStates:"
+ "_isSyncUpSuspendedForDocument:"
+ "br_obfuscateAliasTarget"
+ "br_obfuscatedDotOrTildaSeparatedComponents"
+ "brc_errorItemIneligibleFromSyncForInode:localizedDescription:"
+ "brc_obfuscate"
+ "getSyncState:ignoredZones:error:"
+ "initWithDesiredSyncStates:"
+ "initWithJobStates:"
+ "item:hasSyncUpJobState:"
+ "performAsyncOnClientReadDatabaseWorkloop:"
- "(3)"
- "(3, 4)"
- "(4)"
- "SELECT DISTINCT item_localsyncupstate, HEX(version_content_signature) IN ('013F', '1B3F') FROM client_items WHERE item_localsyncupstate IN %@       AND item_localsyncupstate != 0       AND item_scope = 2       AND NOT item_id_is_documents(item_id)       AND NOT indexset_contains(%p, zone_rowid)"
- "UPDATE client_items SET item_localname = OBFUSCATE(rowid, item_localname), item_bouncedname = OBFUSCATE(rowid, item_bouncedname), item_filename = OBFUSCATE(rowid, item_filename), item_trash_put_back_path = OBFUSCATE_PATH(rowid, item_trash_put_back_path), version_name = OBFUSCATE(rowid, version_name), version_block_sync_until_bundle_id = NULL"
- "UPDATE server_items SET item_filename = OBFUSCATE(rowid, item_filename), item_origname = OBFUSCATE(rowid, item_origname), item_trash_put_back_path = OBFUSCATE_PATH(rowid, item_trash_put_back_path), version_name = OBFUSCATE(rowid, version_name)"
- "[DEBUG] shared document is read-only, do not sync%@"
- "brc_errorItemIneligibleFromSyncForInode:"
- "someone ripped the database from under our feet"

```
