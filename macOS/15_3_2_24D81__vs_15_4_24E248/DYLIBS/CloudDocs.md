## CloudDocs

> `/System/Library/PrivateFrameworks/CloudDocs.framework/Versions/A/CloudDocs`

```diff

-3097.81.2.0.0
-  __TEXT.__text: 0x9cb0c
-  __TEXT.__auth_stubs: 0x1370
-  __TEXT.__objc_methlist: 0x54b0
+3437.101.1.0.0
+  __TEXT.__text: 0x98148
+  __TEXT.__auth_stubs: 0x1330
+  __TEXT.__objc_methlist: 0x6b04
   __TEXT.__const: 0x1d8
-  __TEXT.__gcc_except_tab: 0x5214
-  __TEXT.__cstring: 0xaed4
-  __TEXT.__oslogstring: 0x95c8
+  __TEXT.__gcc_except_tab: 0x4ee4
+  __TEXT.__cstring: 0xb043
+  __TEXT.__oslogstring: 0x9350
   __TEXT.__dlopen_cstrs: 0x4c
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x2570
-  __TEXT.__objc_classname: 0xe4c
-  __TEXT.__objc_methname: 0x11273
-  __TEXT.__objc_methtype: 0x44d0
-  __TEXT.__objc_stubs: 0xb600
-  __DATA_CONST.__got: 0x8c0
+  __TEXT.__unwind_info: 0x27d8
+  __TEXT.__objc_classname: 0xe2e
+  __TEXT.__objc_methname: 0x11789
+  __TEXT.__objc_methtype: 0x44bc
+  __TEXT.__objc_stubs: 0xb1e0
+  __DATA_CONST.__got: 0x8b8
   __DATA_CONST.__const: 0xb00
-  __DATA_CONST.__objc_classlist: 0x2f8
-  __DATA_CONST.__objc_catlist: 0xe0
-  __DATA_CONST.__objc_protolist: 0x148
+  __DATA_CONST.__objc_classlist: 0x310
+  __DATA_CONST.__objc_catlist: 0xe8
+  __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3da8
-  __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x258
+  __DATA_CONST.__objc_selrefs: 0x4338
+  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_classrefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x268
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x9c8
-  __AUTH_CONST.__const: 0x3170
-  __AUTH_CONST.__cfstring: 0x5a00
-  __AUTH_CONST.__objc_const: 0x11278
+  __AUTH_CONST.__auth_got: 0x9a8
+  __AUTH_CONST.__const: 0x3000
+  __AUTH_CONST.__cfstring: 0x5a20
+  __AUTH_CONST.__objc_const: 0xe168
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__objc_intobj: 0x498
+  __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x18b0
-  __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0x644
-  __DATA.__data: 0x1098
-  __DATA.__bss: 0x568
+  __AUTH.__objc_data: 0x19a0
+  __AUTH.__data: 0x88
+  __DATA.__objc_ivar: 0x674
+  __DATA.__data: 0xeb0
+  __DATA.__bss: 0x598
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x500
-  __DATA_DIRTY.__data: 0x28
-  __DATA_DIRTY.__bss: 0xe8
+  __DATA_DIRTY.__data: 0x20
+  __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: CEFBDB95-CA27-316C-B8B0-7F251F64CE20
-  Functions: 3077
-  Symbols:   7819
-  CStrings:  6236
+  UUID: 6957CC2A-E6C5-34C4-A2F3-0BB361B37C4C
+  Functions: 3152
+  Symbols:   7857
+  CStrings:  6266
 
Symbols:
+ +[ACAccount(BRAdditions) br_getMigrationStatusForDSID:]
+ +[BRAccount _refreshCurrentLoggedInAccountForcingRefresh:personaID:error:].cold.4
+ +[BRAccount currentCachedLoggedInAccountWithError:].cold.1
+ +[BRAccount currentLoggedInAccountWithError:].cold.1
+ +[BRAccount refreshCurrentLoggedInAccountWithError:].cold.2
+ +[BRAccount refreshCurrentLoggedInAccount].cold.1
+ +[BRAccount(BRPrivate) startAccountTokenChangeObserverIfNeeded].cold.1
+ +[BRAccountDescriptor matchDomainWithAccountAndStampDomainIfNeeded:withAccounts:persistDomain:].cold.4
+ +[BRAccountDescriptor refreshCache:].cold.1
+ +[BRCloudDocsHelperProvider hasDaemonicParts].cold.1
+ +[BRCloudDocsHelperProvider isFPFSExtension]
+ +[BRCloudDocsHelperProvider isFPFSExtension].cold.1
+ +[BRContainer _sanitizedContainerFallbackNameForMangledID:].cold.1
+ +[BRContainer(BRFinderAdditions) containerInRepositoryURL:createIfMissing:error:].cold.1
+ +[BRContainer(BRInternalAdditions) postContainerListUpdateNotification].cold.3
+ +[BRContainerCache containerCacheForPersonaID:].cold.1
+ +[BRContainerCache hasDaemonicParts].cold.1
+ +[BRContainerCache isManagedProvider].cold.1
+ +[BRContainerCache isPersonalProvider].cold.1
+ +[BRDaemonConnection defaultConnectionForPersonaID:]
+ +[BRDaemonConnection defaultConnectionIfExistsForPersonaID:]
+ +[BRDaemonConnection secondaryConnectionForPersonaID:]
+ +[BRDaemonConnection secondaryConnectionIfExistsForPersonaID:]
+ +[BRFileProviderServicesFactory fetchItemServiceAsyncProxyForURL:handler:]
+ +[BRFrameworkContainerHelper sharedHelper].cold.1
+ +[BRMangledID _mangledIDStringFromZoneName:ownerName:validate:].cold.1
+ +[BRMangledID validateContainerID:].cold.1
+ +[BRMangledID validateOwnerName:].cold.3
+ +[BRNWPathMonitorWrapper usingCellular:]
+ +[BRPersonaUtils currentPersonaMatchesID:]
+ +[BRPosixOperationsWrapper checkMachLookupForService:]
+ +[BRReachabilityMonitor sharedReachabilityMonitor].cold.1
+ +[BRRemoteUserDefaults sharedDefaults].cold.1
+ +[BRRuntimeBehavior isInternalBuild].cold.1
+ +[BRRuntimeBehavior isSeedBuild].cold.1
+ +[BRScreenLockMonitor sharedScreenLockMonitor].cold.1
+ +[BRSpecialFolders _br_containerPathForDataSeparatedPersona]
+ +[BRSpecialFolders _br_containerPathForDataSeparatedPersona].cold.1
+ +[BRSpecialFolders applicationSupportDirForCurrentPersona]
+ +[BRSpecialFolders applicationSupportDirForCurrentPersona].cold.1
+ +[BRSpecialFolders homeDirForCurrentPersona]
+ +[BRSpecialFolders homeDirForCurrentPersona].cold.1
+ +[BRSpecialFolders homeDirForCurrentPersona].cold.2
+ +[BRSpecialFolders volumeUUIDForPersona:]
+ +[BRXPCAutomaticErrorProxy incrementConnectionRefCount:].cold.1
+ +[NSDate(BRAdditions) getLastMidnightDate]
+ +[NSError(BRAdditions) brc_errorCantRegisterBGSystemTask]
+ +[NSError(BRAdditions) brc_errorCellularStatusChanged]
+ +[NSError(BRAdditions) brc_errorNetworkUnreachableDueToCellularConstraint]
+ +[NSError(BRAdditions) brc_errorNetworkUnreachable]
+ +[NSError(BRAdditions) brc_errorShouldNotDownloadOverCellular]
+ +[NSError(BRAdditions) brc_errorUserCancelledDialog]
+ +[NSFileProviderManager(BRAdditions) br_getFPDomainsForProviderIdentifier:withError:]
+ +[NSFileProviderManager(BRAdditions) br_sharedProviderManagerWithDomainID:].cold.3
+ +[NSJSONSerialization(BRAdditions) _jsonifyObject:].cold.1
+ +[UMUserManager(BRAdditions) br_isInSyncBubble].cold.1
+ -[ACAccount(BRAdditions) br_volumeUUID]
+ -[ACAccountStore(BRAdditions) br_accountForPersona:].cold.1
+ -[BRAccount containerWithPendingChanges].cold.6
+ -[BRAccount iCloudDesktopSettingsChangedWithAttributes:error:].cold.4
+ -[BRAccount(BRPrivate) evictOldDocumentsWithHandler:].cold.4
+ -[BRAccount(BRPrivate) hasOptimizeStorageWithError:].cold.4
+ -[BRAccount(BRPrivate) setOptimizeStorageEnabled:error:].cold.4
+ -[BRContainer _replaceDataRepresentationWithData:].cold.1
+ -[BRContainer initWithMangledID:].cold.1
+ -[BRContainer(BRInternalAdditions) _accessDataRepresentation:inBlock:]
+ -[BRContainer(BRInternalAdditions) _accessPurgeableDataRepresentation:inBlock:]
+ -[BRContainer(BRInternalAdditions) _accessRebuiltPurgeableDataRepresentation:inBlock:]
+ -[BRContainer(BRInternalAdditions) accessDataRepresentationInBlock:].cold.1
+ -[BRContainerCache _accountWillChange].cold.5
+ -[BRDaemonConnection _setupAndResumeForPersonaID:]
+ -[BRDarwinNotifyReceiver .cxx_destruct]
+ -[BRDarwinNotifyReceiver dealloc]
+ -[BRDarwinNotifyReceiver initForEventName:withQueue:handler:]
+ -[BRDarwinNotifyReceiver initForEventName:withQueue:handler:].cold.1
+ -[BRDarwinNotifyReceiver invalidate]
+ -[BRDarwinNotifyReceiver lastState]
+ -[BRDarwinNotifySender .cxx_destruct]
+ -[BRDarwinNotifySender dealloc]
+ -[BRDarwinNotifySender initForEventName:]
+ -[BRDarwinNotifySender initForEventName:].cold.1
+ -[BRDarwinNotifySender initForEventName:].cold.2
+ -[BRDarwinNotifySender invalidate]
+ -[BRDarwinNotifySender lastState]
+ -[BRDarwinNotifySender notifyChangedState:]
+ -[BRDownloadProgressProxy _queryDidReceiveUpdate:].cold.4
+ -[BRItemCollectionGatherer _accountDidChangeNotificationBlock]
+ -[BRItemCollectionGatherer _accountDidChangeNotificationBlock].cold.1
+ -[BRItemCollectionGatherer _accountDidChangeNotificationBlock].cold.2
+ -[BRItemCollectionGatherer _accountDidChangeNotificationBlock].cold.3
+ -[BRItemCollectionGatherer _addDeletedItems:]
+ -[BRItemCollectionGatherer _addUpdatedItems:]
+ -[BRItemCollectionGatherer _getDeletedItems]
+ -[BRItemCollectionGatherer _getUpdatedItems]
+ -[BRItemCollectionGatherer _itemCollectionGathererSendUpdates]
+ -[BRItemCollectionGatherer _itemCollectionGathererSendUpdates].cold.1
+ -[BRItemCollectionGatherer _shouldFilterEvaluatedItem:collectionRootItem:]
+ -[BRItemCollectionGatherer _shouldFilterEvaluatedItem:collectionRootItem:].cold.1
+ -[BRItemCollectionGatherer _stopObeservingCollections]
+ -[BRItemCollectionGatherer _unboostApplibrariesIfNeeded].cold.1
+ -[BRItemCollectionGatherer test_getInvalidateQueue]
+ -[BRQuery _classifyItems:deletedItemIDs:].cold.1
+ -[BRQuery _classifyItems:deletedItemIDs:].cold.2
+ -[BRReachabilityMonitor _updateCellularNetworkStatusForObserver:isCellularNetwork:previousCellularStatus:]
+ -[BRReachabilityMonitor isCellularNetwork]
+ -[BRRemoteUserDefaults collectionGathererPacerMinFireInterval]
+ -[NSArray(BRAdditions) br_zipApplyWithArray:applyBlock:]
+ -[NSError(BRFPAdditions) _br_fileProviderErrorWithFallbackFileProviderErrorCode:]
+ -[NSError(BRFPAdditions) _br_getFileProviderDomainErrorCode:].cold.1
+ -[NSError(BRFPAdditions) _br_populateUserInfoDictWithDomain:code:].cold.1
+ -[NSError(BRFPAdditions) br_fileProviderErrorForDownloadFlow]
+ -[NSFileProviderDomain(BRAdditions) br_volumeUUID]
+ -[NSNumber(BRAdditions) br_round:]
+ -[NSNumber(BRAdditions) br_round:].cold.1
+ -[NSNumber(BRAdditions) br_round:].cold.2
+ -[NSURL(BRAdditions) br_isInTrash].cold.1
+ -[NSURL(BRServiceAdditions) _br_fetchItemServiceAsyncProxy:]
+ BRCXPCBRItemServiceProtocolInterface.cold.1
+ BRCXPCICDFileProviderClientSideCollaborationProtocolInterface.cold.1
+ BRCXPCInterface.cold.1
+ BRCXPCSharingOperationInterface.cold.1
+ BRCXPCTokenInterface.cold.1
+ BRCloudDocsCanBeEnabledForCurrentUser.cold.2
+ BRContainerIconCKAssetKeys.cold.1
+ BRCopyUbiquityContainerIdentifiersForCurrentProcess.cold.3
+ BRCurrentProcessHasAccessToCloudDocsGroupContainers.cold.1
+ BRCurrentProcessHasUbiquityContainer.cold.1
+ BRCurrentProcessIsContainerProxy.cold.1
+ BRCurrentProcessIsNotAppSandboxed.cold.1
+ BRCurrentProcessIsNotAppSandboxedAndHasContainers.cold.1
+ BRCurrentProcessIsOwningContainerWithID.cold.1
+ BRGetProcessMobileContainerForID.cold.2
+ BRPerformWithPersonaAndError.cold.4
+ BRRegisterInitialSyncHandlerForContainer.cold.1
+ BRStartCellularConstraintsNotificationsObserver.cold.1
+ BRStartCellularConstraintsNotificationsObserver.notifyRecevier
+ BRStartCellularConstraintsNotificationsObserver.onceToken
+ BRStartCellularConstraintsNotificationsObserver.queue
+ BRTrashExternalDocumentReference.cold.3
+ BRiCloudDesktopCanBeEnabledForDesktopFolder.cold.2
+ BRiCloudDesktopCanBeEnabledForDocumentsFolder.cold.2
+ GCC_except_table106
+ GCC_except_table112
+ GCC_except_table113
+ GCC_except_table126
+ GCC_except_table145
+ GCC_except_table148
+ GCC_except_table163
+ GCC_except_table17
+ GCC_except_table180
+ GCC_except_table186
+ GCC_except_table188
+ GCC_except_table196
+ GCC_except_table197
+ GCC_except_table201
+ GCC_except_table211
+ GCC_except_table215
+ GCC_except_table227
+ GCC_except_table240
+ GCC_except_table251
+ GCC_except_table252
+ GCC_except_table260
+ GCC_except_table268
+ GCC_except_table33
+ GCC_except_table42
+ GCC_except_table54
+ GCC_except_table55
+ GCC_except_table62
+ GCC_except_table69
+ GCC_except_table70
+ GCC_except_table75
+ GCC_except_table77
+ GCC_except_table85
+ GCC_except_table89
+ GCC_except_table90
+ GCC_except_table92
+ LBCopyUbiquityAccountToken.cold.1
+ OBJC_IVAR_$_BRDarwinNotifyReceiver._eventName
+ OBJC_IVAR_$_BRDarwinNotifyReceiver._lastState
+ OBJC_IVAR_$_BRDarwinNotifyReceiver._queue
+ OBJC_IVAR_$_BRDarwinNotifyReceiver._token
+ OBJC_IVAR_$_BRDarwinNotifySender._eventName
+ OBJC_IVAR_$_BRDarwinNotifySender._lastState
+ OBJC_IVAR_$_BRDarwinNotifySender._token
+ OBJC_IVAR_$_BRItemCollectionGatherer._addedItems
+ OBJC_IVAR_$_BRItemCollectionGatherer._deletedItems
+ OBJC_IVAR_$_BRItemCollectionGatherer._invalidateQueue
+ OBJC_IVAR_$_BRItemCollectionGatherer._invalidated
+ OBJC_IVAR_$_BRItemCollectionGatherer._notificationPacer
+ OBJC_IVAR_$_BRReachabilityMonitor._isCellularNetwork
+ OSVersion.cold.1
+ _BRCDatabaseBackupManagerFunction
+ _BRCDatabaseRestoreManagerFunction
+ _BRCellularConstraintChangedNotification
+ _BRCellularConstraintReachedKey
+ _BRContainerIconSupportedNames.cold.1
+ _BREntitlementFPFSExtension
+ _BRGenerateDatabaseBackupManager
+ _BRGenerateDatabaseRestoreManager
+ _BRMetadataUbiquitousItemFavoriteRankKey
+ _BROverrideUploadOnCellularConstraints
+ _BRStartCellularConstraintsNotificationsObserver
+ _OBJC_CLASS_$_BRDarwinNotifyReceiver
+ _OBJC_CLASS_$_BRDarwinNotifySender
+ _OBJC_CLASS_$_BRSpecialFolders
+ _OBJC_CLASS_$_FPProviderDomain
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_METACLASS_$_BRDarwinNotifyReceiver
+ _OBJC_METACLASS_$_BRDarwinNotifySender
+ _OBJC_METACLASS_$_BRSpecialFolders
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ __26-[BRQuery _setQueryState:]_block_invoke.96
+ __29-[BRReachabilityMonitor init]_block_invoke.8
+ __29-[BRReachabilityMonitor init]_block_invoke.cold.1
+ __29-[BRReachabilityMonitor init]_block_invoke.cold.2
+ __38-[BRQuery _processProgressUpdateBatch]_block_invoke.146
+ __40-[BRAccount containerWithPendingChanges]_block_invoke.46
+ __41+[BRSpecialFolders volumeUUIDForPersona:]_block_invoke.cold.1
+ __42-[BRUploadAllFilesForLogOutOperation main]_block_invoke.18
+ __42-[BRUploadAllFilesForLogOutOperation main]_block_invoke.18.cold.1
+ __42-[BRUploadAllFilesForLogOutOperation main]_block_invoke.21
+ __42-[BRUploadAllFilesForLogOutOperation main]_block_invoke.30
+ __42-[BRUploadAllFilesForLogOutOperation main]_block_invoke.30.cold.1
+ __42-[BRUploadAllFilesForLogOutOperation main]_block_invoke.31.cold.2
+ __45-[BRContainerCache initWithHelper:personaID:]_block_invoke.537
+ __45-[BRContainerCache initWithHelper:personaID:]_block_invoke.537.cold.1
+ __45-[BRContainerCache initWithHelper:personaID:]_block_invoke.543
+ __45-[BRContainerCache initWithHelper:personaID:]_block_invoke.543.cold.1
+ __46-[BRContainer(BRXcodeAdditions) currentStatus]_block_invoke.383
+ __46-[BRQuery itemCollectionGathererDidInvalidate]_block_invoke.164
+ __46-[BRQuery itemCollectionGathererDidInvalidate]_block_invoke.164.cold.1
+ __49-[BRContainer(BRXcodeAdditions) lastServerUpdate]_block_invoke.379
+ __50-[BRDaemonConnection _setupAndResumeForPersonaID:]_block_invoke.19
+ __52-[BRAccount(BRPrivate) hasOptimizeStorageWithError:]_block_invoke.92
+ __53-[BRAccount(BRPrivate) evictOldDocumentsWithHandler:]_block_invoke.103
+ __53-[BRAccount(BRPrivate) evictOldDocumentsWithHandler:]_block_invoke.105
+ __53-[BRQuery _handleRemovedItemsNotifications:userInfo:]_block_invoke.163
+ __53-[BRQuery _handleRemovedItemsNotifications:userInfo:]_block_invoke.163.cold.1
+ __54-[BRQuery _handleReplacedItemsNotifications:userInfo:]_block_invoke.157
+ __55-[BRItemCollectionGatherer _startWatchingAppLibraries:]_block_invoke.61
+ __55-[BRItemCollectionGatherer _startWatchingAppLibraries:]_block_invoke.61.cold.1
+ __55-[BRItemCollectionGatherer _startWatchingAppLibraries:]_block_invoke.63
+ __55-[BRItemCollectionGatherer _startWatchingAppLibraries:]_block_invoke.63.cold.1
+ __56-[BRAccount(BRPrivate) setOptimizeStorageEnabled:error:]_block_invoke.98
+ __57-[BRItemCollectionGatherer _invalidateAndNotifyDelegate:]_block_invoke_2.cold.1
+ __57-[BRItemCollectionGatherer collection:didEncounterError:]_block_invoke.80
+ __57-[BRItemCollectionGatherer collection:didEncounterError:]_block_invoke.80.cold.1
+ __61-[BRDarwinNotifyReceiver initForEventName:withQueue:handler:]_block_invoke.21
+ __61-[BRDarwinNotifyReceiver initForEventName:withQueue:handler:]_block_invoke.23
+ __61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke.22
+ __61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke.22.cold.1
+ __61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke.22.cold.2
+ __61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke.22.cold.3
+ __61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke.22.cold.4
+ __61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke.22.cold.5
+ __61-[NSURL(BRAdditions) br_containerIDIfIsDocumentsContainerURL]_block_invoke.65
+ __62-[BRAccount iCloudDesktopSettingsChangedWithAttributes:error:]_block_invoke.52
+ __65+[NSURL(BRAdditions) br_documentURLFromBookmarkableString:error:]_block_invoke.27
+ __66-[NSError(BRFPAdditions) _br_populateUserInfoDictWithDomain:code:]_block_invoke.111
+ __68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke.33
+ __68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke.36.cold.1
+ __68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke.36.cold.2
+ __68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke.37
+ __68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke.42
+ __68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke.44
+ __70+[BRContainer(BRInternalAdditions) forceRefreshContainers:completion:]_block_invoke.461
+ __70+[NSURL(BRAdditions) br_documentURLFromBookmarkableString:completion:]_block_invoke.24
+ __83-[BRContainer(BRFinderInternalAdditions) deleteAllContentsOnClientAndServer:error:]_block_invoke.420
+ __85+[NSFileProviderManager(BRAdditions) br_getFPDomainsForProviderIdentifier:withError:]_block_invoke_2.cold.1
+ __85+[NSFileProviderManager(BRAdditions) br_getFPDomainsForProviderIdentifier:withError:]_block_invoke_2.cold.2
+ __BRAddNetworkReachabilityObserverWithCallbackQueue_block_invoke.50
+ __BRAddNetworkReachabilityObserverWithCallbackQueue_block_invoke.52
+ __BRGetProcessMobileContainerForID_block_invoke.cold.2
+ __BRSharingBulkCopyShareID_block_invoke.134
+ __BRSharingCopyCurrentUserIdentifier_block_invoke.111
+ __BRSharingCopyCurrentUserIdentifier_block_invoke_2.112
+ __BRiWorkSharingSetSharingState_block_invoke.96
+ __OBJC_$_CATEGORY_CLASS_METHODS_ACAccount_$_BRAdditions
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSDate_$_BRAdditions
+ __OBJC_$_CATEGORY_NSDate_$_BRAdditions
+ __OBJC_$_CLASS_METHODS_BRSpecialFolders
+ __OBJC_$_INSTANCE_METHODS_BRDarwinNotifyReceiver
+ __OBJC_$_INSTANCE_METHODS_BRDarwinNotifySender
+ __OBJC_$_INSTANCE_VARIABLES_BRDarwinNotifyReceiver
+ __OBJC_$_INSTANCE_VARIABLES_BRDarwinNotifySender
+ __OBJC_$_PROP_LIST_BRDarwinNotifyReceiver
+ __OBJC_$_PROP_LIST_BRDarwinNotifySender
+ __OBJC_CLASS_RO_$_BRDarwinNotifyReceiver
+ __OBJC_CLASS_RO_$_BRDarwinNotifySender
+ __OBJC_CLASS_RO_$_BRSpecialFolders
+ __OBJC_METACLASS_RO_$_BRDarwinNotifyReceiver
+ __OBJC_METACLASS_RO_$_BRDarwinNotifySender
+ __OBJC_METACLASS_RO_$_BRSpecialFolders
+ ___25+[BRQueryItem initialize]_block_invoke_44
+ ___36-[BRDarwinNotifyReceiver invalidate]_block_invoke
+ ___41+[BRSpecialFolders volumeUUIDForPersona:]_block_invoke
+ ___41-[BRItemCollectionGatherer enableUpdates]_block_invoke
+ ___42-[BRItemCollectionGatherer disableUpdates]_block_invoke
+ ___42-[BRReachabilityMonitor isCellularNetwork]_block_invoke
+ ___44+[BRCloudDocsHelperProvider isFPFSExtension]_block_invoke
+ ___44+[BRSpecialFolders homeDirForCurrentPersona]_block_invoke
+ ___50-[BRDaemonConnection _setupAndResumeForPersonaID:]_block_invoke
+ ___50-[BRDaemonConnection _setupAndResumeForPersonaID:]_block_invoke_2
+ ___51-[BRItemCollectionGatherer initWithDelegate:query:]_block_invoke
+ ___52+[BRDaemonConnection defaultConnectionForPersonaID:]_block_invoke
+ ___54+[BRDaemonConnection secondaryConnectionForPersonaID:]_block_invoke
+ ___57-[BRItemCollectionGatherer _invalidateAndNotifyDelegate:]_block_invoke_2
+ ___58+[BRSpecialFolders applicationSupportDirForCurrentPersona]_block_invoke
+ ___60+[BRDaemonConnection defaultConnectionIfExistsForPersonaID:]_block_invoke
+ ___60+[BRSpecialFolders _br_containerPathForDataSeparatedPersona]_block_invoke
+ ___61-[BRDarwinNotifyReceiver initForEventName:withQueue:handler:]_block_invoke
+ ___62+[BRDaemonConnection secondaryConnectionIfExistsForPersonaID:]_block_invoke
+ ___62-[BRRemoteUserDefaults collectionGathererPacerMinFireInterval]_block_invoke
+ ___74+[BRFileProviderServicesFactory fetchItemServiceAsyncProxyForURL:handler:]_block_invoke
+ ___85+[NSFileProviderManager(BRAdditions) br_getFPDomainsForProviderIdentifier:withError:]_block_invoke
+ ___85+[NSFileProviderManager(BRAdditions) br_getFPDomainsForProviderIdentifier:withError:]_block_invoke_2
+ ___BROverrideUploadOnCellularConstraints_block_invoke
+ ___BRStartCellularConstraintsNotificationsObserver_block_invoke
+ ___BRStartCellularConstraintsNotificationsObserver_block_invoke_2
+ ___block_descriptor_32_e8_v16?0Q8l
+ ___block_descriptor_48_e8_32r_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32s40bs_e8_v12?0i8l
+ ___block_descriptor_48_e8_32s40w_e25_B24?08"NSDictionary"16l
+ ___block_descriptor_51_e8_32s40s_e5_v8?0l
+ ___block_descriptor_56_e8_32s40r48r_e29_v24?0"NSArray"8"NSError"16l
+ ___exp10
+ __block_literal_global.108
+ __block_literal_global.151
+ __block_literal_global.171
+ __block_literal_global.175
+ __block_literal_global.177
+ __block_literal_global.187
+ __block_literal_global.189
+ __block_literal_global.218
+ __block_literal_global.223
+ __block_literal_global.227
+ __block_literal_global.232
+ __block_literal_global.25
+ __block_literal_global.266
+ __block_literal_global.281
+ __block_literal_global.287
+ __block_literal_global.323
+ __block_literal_global.4
+ __block_literal_global.424
+ __block_literal_global.436
+ __block_literal_global.465
+ __block_literal_global.468
+ __block_literal_global.470
+ __block_literal_global.48
+ __block_literal_global.484
+ __block_literal_global.51
+ __block_literal_global.556
+ __block_literal_global.558
+ __block_literal_global.566
+ __block_literal_global.568
+ __block_literal_global.573
+ __block_literal_global.61
+ __block_literal_global.626
+ __block_literal_global.707
+ __block_literal_global.85
+ __brc_create_section.cold.1
+ _brc_create_simulate_crash_message.cold.1
+ _brc_log_is_internal_install.cold.1
+ _classBRCDatabaseBackupManager
+ _classBRCDatabaseRestoreManager
+ _dispatch_assert_queue_not$V2
+ _gDaemonDefaultConnectionsByPersonaID
+ _gDaemonSecondaryConnectionsByPersonaID
+ _getBRCDatabaseBackupManagerClass
+ _getBRCDatabaseRestoreManagerClass
+ _iCloudDriveCoreLibrary
+ _initBRCDatabaseBackupManager
+ _initBRCDatabaseRestoreManager
+ _log10
+ _nw_path_uses_interface_type
+ _objc_msgSend$_accessDataRepresentation:inBlock:
+ _objc_msgSend$_accessPurgeableDataRepresentation:inBlock:
+ _objc_msgSend$_accessRebuiltPurgeableDataRepresentation:inBlock:
+ _objc_msgSend$_accountDidChangeNotificationBlock
+ _objc_msgSend$_addDeletedItems:
+ _objc_msgSend$_addUpdatedItems:
+ _objc_msgSend$_br_fetchItemServiceAsyncProxy:
+ _objc_msgSend$_br_fileProviderErrorWithFallbackFileProviderErrorCode:
+ _objc_msgSend$_getDeletedItems
+ _objc_msgSend$_getUpdatedItems
+ _objc_msgSend$_itemCollectionGathererSendUpdates
+ _objc_msgSend$_setupAndResumeForPersonaID:
+ _objc_msgSend$_shouldFilterEvaluatedItem:collectionRootItem:
+ _objc_msgSend$_stopObeservingCollections
+ _objc_msgSend$_stopObservingAccountTokenDidChangeNotification
+ _objc_msgSend$_updateCellularNetworkStatusForObserver:isCellularNetwork:previousCellularStatus:
+ _objc_msgSend$applicationSupportDirForCurrentPersona
+ _objc_msgSend$br_fileProviderError
+ _objc_msgSend$br_getFPDomainsForProviderIdentifier:withError:
+ _objc_msgSend$br_volumeUUID
+ _objc_msgSend$checkMachLookupForService:
+ _objc_msgSend$collectionGathererPacerMinFireInterval
+ _objc_msgSend$components:fromDate:
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$dateFromComponents:
+ _objc_msgSend$defaultConnectionForPersonaID:
+ _objc_msgSend$defaultConnectionIfExistsForPersonaID:
+ _objc_msgSend$favoriteRank
+ _objc_msgSend$fetchItemServiceAsyncProxyForURL:handler:
+ _objc_msgSend$fp_volumeUUID
+ _objc_msgSend$homeDirForCurrentPersona
+ _objc_msgSend$initForEventName:withQueue:handler:
+ _objc_msgSend$initWithUserURL:
+ _objc_msgSend$initWithUserURL:outputUserURL:
+ _objc_msgSend$isFPFSExtension
+ _objc_msgSend$lookupCollectionGathererPacerMinFireInterval:
+ _objc_msgSend$objCType
+ _objc_msgSend$overrideUploadOnCellularConstraintsWithReply:
+ _objc_msgSend$providerDomainWithID:cachePolicy:error:
+ _objc_msgSend$reachabilityMonitor:didChangeCellularNetworkTo:
+ _objc_msgSend$secondaryConnectionForPersonaID:
+ _objc_msgSend$secondaryConnectionIfExistsForPersonaID:
+ _objc_msgSend$setHour:
+ _objc_msgSend$setMinute:
+ _objc_msgSend$setNanosecond:
+ _objc_msgSend$setSecond:
+ _objc_msgSend$storageURLs
+ _objc_msgSend$usingCellular:
+ _objc_msgSend$validateConnectionExtensionInfoForPersonaID:
+ _objc_msgSend$volumeUUIDForPersona:
+ applicationSupportDirForCurrentPersona.once
+ applicationSupportDirForCurrentPersona.pathByPersonaID
+ brc_default_log.cold.3
+ brc_monotonic_time_diff_to_interval.cold.1
+ brc_notifications_log.cold.3
+ brc_trace_log.cold.3
+ fileProgressSubscribeQueue.cold.1
+ getSharingServiceInterface.cold.1
+ homeDirForCurrentPersona.once
+ homeDirForCurrentPersona.pathByPersonaID
+ iCloudDriveCoreLibrary.cold.1
+ iCloudDriveCoreLibrary.frameworkLibrary
+ initBRCDatabaseBackupManager.cold.1
+ initBRCDatabaseRestoreManager.cold.1
+ isFPFSExtension.isFPFSExtension
+ isFPFSExtension.once
- +[BRDaemonConnection defaultConnectionForKey:initializer:]
- +[BRDaemonConnection defaultConnectionIfExistsForKey:]
- +[BRDaemonConnection secondaryConnectionForKey:initializer:]
- +[BRDaemonConnection secondaryConnectionIfExistsForKey:]
- +[BRFileProviderServicesFactory fetchItemServiceSyncProxyForURL:handler:]
- +[BRQueryItem askDaemonQueryItemForURL:andFakeFSEvent:error:].cold.2
- +[NSString(BRPathAdditions) _br_containerPathForDataSeparatedPersona]
- +[NSString(BRPathAdditions) _br_containerPathForDataSeparatedPersona].cold.1
- +[NSString(BRPathAdditions) br_currentHomeDir]
- +[NSString(BRPathAdditions) br_currentHomeDir].cold.1
- +[NSString(BRPathAdditions) br_supportDirForPersona:dataSeparated:]
- -[BRAccount(BRPrivate) getEvictableSpace:error:].cold.1
- -[BRAccount(BRPrivate) getEvictableSpace:error:].cold.2
- -[BRAccount(BRPrivate) getEvictableSpace:error:].cold.3
- -[BRDaemonConnection _setupAndResumeForKey:]
- -[BRDaemonConnection newFPFSSyncProxy].cold.2
- -[BRDaemonConnection newLegacySyncProxy].cold.2
- -[BRDbRowObjectID isFpfsItem]
- -[BRFileObjectID isAppLibraryDocumentsFolder].cold.1
- -[BRFileObjectID isAppLibraryRoot].cold.1
- -[BRItemCollectionGatherer collection:didUpdateItems:replaceItemsByFormerID:deleteItemsWithIDs:].cold.2
- -[BROperation remoteFPFSObject].cold.1
- -[BRQuery _setQueryState:].cold.1
- -[BRQueryItem _isFPFSItem]
- -[BRQueryItem initWithCoder:].cold.3
- -[BRShareOperation remoteFPFSObject].cold.1
- -[BRWaitForFPFSMigrationOperation main].cold.2
- -[NSError(BRFPAdditions) br_fileProviderErrorWithFPFS:]
- -[NSFileManager(BRAdditions) br_movePromisedItemAtURL:toURL:error:].cold.1
- -[NSFileManager(BRAdditions) br_movePromisedItemAtURL:toURL:error:].cold.2
- -[NSFileManager(BRAdditions) br_movePromisedItemAtURL:toURL:error:].cold.3
- -[NSFileManager(BRAdditions) br_movePromisedItemAtURL:toURL:error:].cold.4
- -[NSFileManager(BRAdditions) br_movePromisedItemAtURL:toURL:error:].cold.5
- -[NSFileManager(BRAdditions) br_movePromisedItemAtURL:toURL:error:].cold.6
- -[NSFileManager(BRAdditions) br_movePromisedItemAtURL:toURL:error:].cold.7
- -[NSFileManager(BRAdditions) br_movePromisedItemAtURL:toURL:error:].cold.8
- -[NSFileManager(BRAdditions) br_putBackTrashedItemAtURL:resultingURL:error:].cold.1
- -[NSFileManager(BRAdditions) br_putBackURLForTrashedItemAtURL:error:].cold.1
- -[NSFileManager(BRAdditions) br_putBackURLForTrashedItemAtURL:error:].cold.2
- -[NSFileManager(TempFilesAdditions) brc_createTemporaryFdInDirectory:withTemplate:error:]
- -[NSString(BRPathAdditions) br_realpath].cold.1
- -[NSURL(BRAdditions) _br_isParentOfURL:strictly:ignoreHomeDirectoryCheck:].cold.1
- -[NSURL(BRAdditions) br_addPhysicalProperty]
- -[NSURL(BRServiceAdditions) _br_fetchItemServiceSyncProxy:]
- -[_BRContainerItem initWithQueryItem:container:zoneRowID:].cold.1
- BRFetchCollaborationIdentifierForItemAtURL.cold.2
- BRFetchCollaborationIdentifierForItemWithIdentifier.cold.2
- BRSetMigrationStatusForDSIDInPref.cold.2
- GCC_except_table101
- GCC_except_table104
- GCC_except_table110
- GCC_except_table117
- GCC_except_table118
- GCC_except_table128
- GCC_except_table142
- GCC_except_table147
- GCC_except_table149
- GCC_except_table15
- GCC_except_table153
- GCC_except_table158
- GCC_except_table160
- GCC_except_table165
- GCC_except_table166
- GCC_except_table169
- GCC_except_table178
- GCC_except_table183
- GCC_except_table193
- GCC_except_table194
- GCC_except_table198
- GCC_except_table203
- GCC_except_table208
- GCC_except_table212
- GCC_except_table225
- GCC_except_table29
- GCC_except_table51
- GCC_except_table71
- GCC_except_table87
- GCC_except_table96
- OBJC_IVAR_$_BRQuery._isFPFSMode
- _BRIsFPFSEnabled
- _BRWhatsAppContainerID
- _CKRecordZoneIDFunction
- _FPIsCloudDocsWithFPFSEnabled
- _GSAdditionCreationNameKey
- _GSAdditionCreationNameSpaceKey
- _GSAdditionCreationUserInfoKey
- _GSUbiquitousConflictsNameSpace
- _NSFileProviderItemCapabilitiesAllowsRecursiveDownloading
- _NSKeyedArchiveRootObjectKey
- __117+[NSURL(BRAdditions) _br_bookmarkableStringForURL:remoteOpeningAppWithBundleID:onlyAllowItemKnowByServer:completion:]_block_invoke.14
- __24-[BRQuery enableUpdates]_block_invoke.cold.2
- __25-[BRQuery disableUpdates]_block_invoke.cold.2
- __26-[BRQuery _setQueryState:]_block_invoke.97
- __38-[BRQuery _processProgressUpdateBatch]_block_invoke.144
- __40-[BRAccount containerWithPendingChanges]_block_invoke.34
- __40-[BRListNonLocalVersionsOperation start]_block_invoke.94
- __40-[BRListNonLocalVersionsOperation start]_block_invoke.94.cold.1
- __40-[BRListNonLocalVersionsOperation start]_block_invoke.94.cold.2
- __40-[BRListNonLocalVersionsOperation start]_block_invoke.95
- __40-[BRListNonLocalVersionsOperation start]_block_invoke.95.cold.1
- __40-[BRListNonLocalVersionsOperation start]_block_invoke.96
- __40-[BRListNonLocalVersionsOperation start]_block_invoke.cold.1
- __40-[BRSharingCopyShortTokenOperation main]_block_invoke.333
- __42-[BRUploadAllFilesForLogOutOperation main]_block_invoke.20
- __42-[BRUploadAllFilesForLogOutOperation main]_block_invoke.20.cold.1
- __42-[BRUploadAllFilesForLogOutOperation main]_block_invoke.22
- __42-[BRUploadAllFilesForLogOutOperation main]_block_invoke.32.cold.2
- __42-[BRUploadAllFilesForLogOutOperation main]_block_invoke.33
- __42-[BRUploadAllFilesForLogOutOperation main]_block_invoke.33.cold.1
- __44-[BRDaemonConnection _setupAndResumeForKey:]_block_invoke.19
- __45-[BRContainerCache initWithHelper:personaID:]_block_invoke.532
- __45-[BRContainerCache initWithHelper:personaID:]_block_invoke.532.cold.1
- __45-[BRContainerCache initWithHelper:personaID:]_block_invoke.533
- __45-[BRContainerCache initWithHelper:personaID:]_block_invoke.538.cold.1
- __46-[BRContainer(BRXcodeAdditions) currentStatus]_block_invoke.381
- __46-[BRQuery itemCollectionGathererDidInvalidate]_block_invoke.162
- __46-[BRQuery itemCollectionGathererDidInvalidate]_block_invoke.162.cold.1
- __48-[BRAccount(BRPrivate) getEvictableSpace:error:]_block_invoke.93
- __49-[BRContainer(BRXcodeAdditions) lastServerUpdate]_block_invoke.377
- __52-[BRAccount(BRPrivate) hasOptimizeStorageWithError:]_block_invoke.80
- __53-[BRAccount(BRPrivate) evictOldDocumentsWithHandler:]_block_invoke.101
- __53-[BRAccount(BRPrivate) evictOldDocumentsWithHandler:]_block_invoke.99
- __53-[BRItemCollectionGatherer _addItemCollectionOnItem:]_block_invoke.cold.1
- __53-[BRQuery _handleRemovedItemsNotifications:userInfo:]_block_invoke.161
- __53-[BRQuery _handleRemovedItemsNotifications:userInfo:]_block_invoke.161.cold.1
- __54-[BRQuery _handleReplacedItemsNotifications:userInfo:]_block_invoke.155
- __55-[BRItemCollectionGatherer _startWatchingAppLibraries:]_block_invoke.58
- __55-[BRItemCollectionGatherer _startWatchingAppLibraries:]_block_invoke.58.cold.1
- __55-[BRItemCollectionGatherer _startWatchingAppLibraries:]_block_invoke.60
- __55-[BRItemCollectionGatherer _startWatchingAppLibraries:]_block_invoke.60.cold.1
- __56+[NSFileCoordinator(BRAdditions) br_boostFilePresenter:]_block_invoke.1
- __56-[BRAccount(BRPrivate) setOptimizeStorageEnabled:error:]_block_invoke.88
- __56-[NSURL(BRAdditions) br_creatorNameComponentsWithError:]_block_invoke.88
- __57-[BRItemCollectionGatherer _invalidateAndNotifyDelegate:]_block_invoke.cold.1
- __57-[BRItemCollectionGatherer collection:didEncounterError:]_block_invoke.77
- __57-[BRItemCollectionGatherer collection:didEncounterError:]_block_invoke.77.cold.1
- __61+[BRQueryItem askDaemonQueryItemForURL:andFakeFSEvent:error:]_block_invoke.694
- __61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke.21
- __61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke.21.cold.1
- __61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke.21.cold.2
- __61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke.21.cold.3
- __61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke.21.cold.4
- __61-[NSURL(BRAdditions) br_containerIDIfIsDocumentsContainerURL]_block_invoke.64
- __62-[BRAccount iCloudDesktopSettingsChangedWithAttributes:error:]_block_invoke.40
- __63-[NSFileProviderManager(BRAdditions) br_getFPDomainsWithError:]_block_invoke_2.cold.1
- __63-[NSFileProviderManager(BRAdditions) br_getFPDomainsWithError:]_block_invoke_2.cold.2
- __65+[NSURL(BRAdditions) br_documentURLFromBookmarkableString:error:]_block_invoke.26
- __66-[NSError(BRFPAdditions) _br_populateUserInfoDictWithDomain:code:]_block_invoke.105
- __67-[NSFileManager(BRAdditions) br_movePromisedItemAtURL:toURL:error:]_block_invoke.14
- __67-[NSFileManager(BRAdditions) br_movePromisedItemAtURL:toURL:error:]_block_invoke.14.cold.1
- __67-[NSFileManager(BRAdditions) br_movePromisedItemAtURL:toURL:error:]_block_invoke.14.cold.2
- __67-[NSFileManager(BRAdditions) br_trashItemAtURL:resultingURL:error:]_block_invoke.36
- __68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke.32
- __68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke.35
- __68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke.35.cold.1
- __68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke.35.cold.2
- __68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke.39
- __68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke.43
- __70+[BRContainer(BRInternalAdditions) forceRefreshContainers:completion:]_block_invoke.459
- __75-[BRFrameworkContainerHelper br_capabilityToMoveFromURL:toNewParent:error:]_block_invoke.639
- __76-[BRItemCollectionGatherer _startObservingAccountTokenDidChangeNotification]_block_invoke.cold.1
- __76-[BRItemCollectionGatherer _startObservingAccountTokenDidChangeNotification]_block_invoke.cold.2
- __76-[BRItemCollectionGatherer _startObservingAccountTokenDidChangeNotification]_block_invoke.cold.3
- __76-[BRItemCollectionGatherer _startObservingAccountTokenDidChangeNotification]_block_invoke.cold.4
- __83-[BRContainer(BRFinderInternalAdditions) deleteAllContentsOnClientAndServer:error:]_block_invoke.418
- __86-[NSURL(BRAdditions_Private) _br_getAttributeValue:withSecondaryConnection:withError:]_block_invoke.187
- __BRAddNetworkReachabilityObserverWithCallbackQueue_block_invoke.57
- __BRAddNetworkReachabilityObserverWithCallbackQueue_block_invoke.59
- __BRCXPCBRItemServiceProtocolInterface_block_invoke.cold.1
- __BRCXPCICDFileProviderClientSideCollaborationProtocolInterface_block_invoke.cold.1
- __BRGetAttributeValuesForItem_block_invoke.43
- __BRGetURLForPublishedItemWithOptions_block_invoke.23
- __BRSharingBulkCopyShareID_block_invoke.158
- __BRSharingBulkCopyShareID_block_invoke.160
- __BRSharingBulkCopyShareID_block_invoke_2.161
- __BRSynchronousEvictItemAtURLWithOptions_block_invoke.29
- __BRiWorkSharingGetBadgingSharingState_block_invoke.120
- __BRiWorkSharingGetFullSharingInfo_block_invoke.134
- __BRiWorkSharingGetFullSharingInfo_block_invoke_2.135
- __BRiWorkSharingGetFullSharingInfo_block_invoke_3.136
- __BRiWorkSharingGetNeedsMigrateAtURL_block_invoke.126
- __BRiWorkSharingSetSharingState_block_invoke.109
- __BRiWorkSharingSetSharingState_block_invoke.111
- __BRiWorkSharingSetSharingState_block_invoke.115
- __BRiWorkSharingSetSharingState_block_invoke.116
- __BRiWorkSharingSetSharingState_block_invoke_2.112
- __CFURLCopyPromiseURLOfLogicalURL
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BRFileProviderExtensionBackChannel
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BRItemNotificationSendingLegacy
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BRNonLocalVersionSending
- __OBJC_$_PROTOCOL_METHOD_TYPES_BRFileProviderExtensionBackChannel
- __OBJC_$_PROTOCOL_METHOD_TYPES_BRItemNotificationSendingLegacy
- __OBJC_$_PROTOCOL_METHOD_TYPES_BRNonLocalVersionSending
- __OBJC_$_PROTOCOL_REFS_BRFileProviderExtensionBackChannel
- __OBJC_$_PROTOCOL_REFS_BRItemNotificationSendingLegacy
- __OBJC_$_PROTOCOL_REFS_BRNonLocalVersionSending
- __OBJC_LABEL_PROTOCOL_$_BRFileProviderExtensionBackChannel
- __OBJC_LABEL_PROTOCOL_$_BRItemNotificationSendingLegacy
- __OBJC_LABEL_PROTOCOL_$_BRNonLocalVersionSending
- __OBJC_PROTOCOL_$_BRFileProviderExtensionBackChannel
- __OBJC_PROTOCOL_$_BRItemNotificationSendingLegacy
- __OBJC_PROTOCOL_$_BRNonLocalVersionSending
- __OBJC_PROTOCOL_REFERENCE_$_BRFileProviderExtensionBackChannel
- __OBJC_PROTOCOL_REFERENCE_$_BRGetPausedFileListProtocol
- __OBJC_PROTOCOL_REFERENCE_$_BRItemNotificationSendingLegacy
- __OBJC_PROTOCOL_REFERENCE_$_BRNonLocalVersionReceiving
- __OBJC_PROTOCOL_REFERENCE_$_BRNonLocalVersionSending
- __OBJC_PROTOCOL_REFERENCE_$_BRShareOperationLegacyProtocol
- ___28-[BREvictItemOperation main]_block_invoke
- ___29-[BRReachabilityMonitor init]_block_invoke_2
- ___33-[BROperation remoteLegacyObject]_block_invoke
- ___39+[BRDaemonConnection defaultConnection]_block_invoke
- ___39-[BRShareCopyAccessTokenOperation main]_block_invoke_2
- ___40-[BRListNonLocalVersionsOperation start]_block_invoke
- ___41+[BRDaemonConnection secondaryConnection]_block_invoke
- ___44-[BRDaemonConnection _setupAndResumeForKey:]_block_invoke
- ___44-[BRDaemonConnection _setupAndResumeForKey:]_block_invoke_2
- ___45-[NSURL(BRAdditions) br_setAccessTime:error:]_block_invoke
- ___46+[NSString(BRPathAdditions) br_currentHomeDir]_block_invoke
- ___48-[BRAccount(BRPrivate) getEvictableSpace:error:]_block_invoke
- ___54+[BRDaemonConnection defaultConnectionIfExistsForKey:]_block_invoke
- ___56+[BRDaemonConnection secondaryConnectionIfExistsForKey:]_block_invoke
- ___57-[GSAddition(BRConflictLosers) br_markResolvedWithError:]_block_invoke
- ___58+[BRDaemonConnection defaultConnectionForKey:initializer:]_block_invoke
- ___60+[BRDaemonConnection secondaryConnectionForKey:initializer:]_block_invoke
- ___61+[BRQueryItem askDaemonQueryItemForURL:andFakeFSEvent:error:]_block_invoke
- ___63-[NSFileProviderManager(BRAdditions) br_getFPDomainsWithError:]_block_invoke
- ___63-[NSFileProviderManager(BRAdditions) br_getFPDomainsWithError:]_block_invoke_2
- ___67+[NSString(BRPathAdditions) br_supportDirForPersona:dataSeparated:]_block_invoke
- ___67-[NSFileManager(BRAdditions) br_movePromisedItemAtURL:toURL:error:]_block_invoke
- ___69+[NSString(BRPathAdditions) _br_containerPathForDataSeparatedPersona]_block_invoke
- ___70+[NSURL(BRAdditions) br_documentURLFromBookmarkableString:completion:]_block_invoke_2
- ___73+[BRFileProviderServicesFactory fetchItemServiceSyncProxyForURL:handler:]_block_invoke
- ___80+[NSURL(BRAdditions) br_containerIDsWithExternalReferencesTo:completionHandler:]_block_invoke
- ___91-[NSURL(BRConflictWinner) br_addFakeConflictLoserFromItemAtURL:lastEditorDeviceName:error:]_block_invoke
- ___BRFetchCollaborationIdentifierForItemAtURL_block_invoke
- ___BRFetchCollaborationIdentifierForItemAtURL_block_invoke_2
- ___BRLSOpenFileAtURL_block_invoke
- ___BRPrepareDocumentForForcedConflict_block_invoke
- ___BRRemoveItemAtURL_block_invoke
- ___BRSharingBulkCopyShareID_block_invoke_3
- ___BRSharingBulkCopyShareID_block_invoke_4
- ___BRSharingCopyCurrentUserIdentifier_block_invoke_3
- ___BRSharingCopyCurrentUserIdentifier_block_invoke_4
- ___BRSynchronousEvictItemAtURLWithOptions_block_invoke
- ___BRiWorkSharingGetFullSharingInfo_block_invoke_4
- ___block_descriptor_32_e25_"BRDaemonConnection"8?0l
- ___block_descriptor_40_e8_32s_e20_v20?0S8"NSError"12l
- ___block_descriptor_40_e8_32s_e20_v20?0i8"NSError"12l
- ___block_descriptor_40_e8_32s_e20_v24?0Q8"NSError"16l
- ___block_descriptor_40_e8_32s_e27_v24?0"NSURL"8"NSError"16l
- ___block_descriptor_40_e8_32s_e33_v24?0"BRQueryItem"8"NSError"16l
- ___block_descriptor_40_e8_32s_e41_v24?0"NSMutableDictionary"8"NSError"16l
- ___block_descriptor_40_e8_32s_e44_v24?0"NSPersonNameComponents"8"NSError"16l
- ___block_descriptor_48_e8_32s40r_e29_v24?0"NSArray"8"NSError"16l
- ___block_descriptor_48_e8_32s40s_e18_B16?0"NSString"8l
- ___block_descriptor_48_e8_32s40s_e58_v32?0"<BRNonLocalVersionSending>"8"NSURL"16"NSError"24l
- ___block_descriptor_56_e8_32s40r48r_e32_v24?0"GSAddition"8"NSError"16l
- ___block_descriptor_56_e8_32s40s48s_e17_"NSError"12?0i8l
- ___block_descriptor_56_e8_32s40s48s_e25_B24?08"NSDictionary"16l
- ___block_descriptor_64_e8_32bs_e17_v16?0"NSError"8l
- __block_literal_global.188
- __block_literal_global.199
- __block_literal_global.203
- __block_literal_global.205
- __block_literal_global.215
- __block_literal_global.225
- __block_literal_global.23
- __block_literal_global.230
- __block_literal_global.24
- __block_literal_global.279
- __block_literal_global.298
- __block_literal_global.304
- __block_literal_global.321
- __block_literal_global.39
- __block_literal_global.463
- __block_literal_global.466
- __block_literal_global.47
- __block_literal_global.538
- __block_literal_global.550
- __block_literal_global.551
- __block_literal_global.553
- __block_literal_global.561
- __block_literal_global.563
- __block_literal_global.571
- __block_literal_global.584
- __block_literal_global.598
- __block_literal_global.60
- __block_literal_global.627
- __block_literal_global.711
- __block_literal_global.73
- __block_literal_global.79
- __block_literal_global.87
- __block_literal_global.92
- __block_literal_global.98
- __mkstempWrapper
- __reportPosixWriteError
- _brc_xattr_get_fs_string
- _classCKRecordZoneID
- _fsctl
- _gBRActiveQueries
- _gBRActiveQueriesMutex
- _gDaemonDefaultConnectionsByKey
- _gDaemonSecondaryConnectionsByKey
- _getCKRecordZoneIDClass
- _initCKRecordZoneID
- _objc_msgSend$URLForDirectory:inDomain:appropriateForURL:create:error:
- _objc_msgSend$__itemAtURL:didGainVersionWithClientID:name:purposeID:
- _objc_msgSend$__itemAtURL:didResolveConflictVersionWithClientID:name:purposeID:
- _objc_msgSend$_br_fetchItemServiceSyncProxy:
- _objc_msgSend$_br_markResolvedWithError:
- _objc_msgSend$_isFPFSItem
- _objc_msgSend$_setVersionStoreForDocumentAtURL:error:
- _objc_msgSend$_setupAndResumeForKey:
- _objc_msgSend$boostFilePresenterAtURL:reply:
- _objc_msgSend$br_addPhysicalProperty
- _objc_msgSend$br_capabilityToMoveToURL:error:
- _objc_msgSend$br_currentHomeDir
- _objc_msgSend$br_fileProviderErrorWithFPFS:
- _objc_msgSend$br_movePromisedItemAtURL:toURL:error:
- _objc_msgSend$br_putBackURLForTrashedItemAtURL:error:
- _objc_msgSend$br_setPutBackInfoOnItemAtURL:
- _objc_msgSend$br_supportDirForPersona:dataSeparated:
- _objc_msgSend$br_underlyingPOSIXError
- _objc_msgSend$capabilityWhenTryingToReparentItemAtURL:toNewParent:reply:
- _objc_msgSend$checkinAskClientIfUsingUbiquity:
- _objc_msgSend$contentsOfDirectoryAtPath:error:
- _objc_msgSend$copyBulkShareIDsAtURLs:reply:
- _objc_msgSend$copyCollaborationIdentifierForItemAtURL:reply:
- _objc_msgSend$copyItemAtURL:toURL:error:
- _objc_msgSend$createAdditionStagedAtURL:creationInfo:completionHandler:
- _objc_msgSend$createSharingInfoForURL:reply:
- _objc_msgSend$defaultConnectionForKey:initializer:
- _objc_msgSend$defaultConnectionIfExistsForKey:
- _objc_msgSend$documentURL
- _objc_msgSend$evictAllFilesInGroup:
- _objc_msgSend$evictItemAtURL:options:reply:
- _objc_msgSend$fetchItemServiceSyncProxyForURL:handler:
- _objc_msgSend$fileObjectIDForURL:allocateDocID:error:
- _objc_msgSend$forceConflictForURL:bookmarkData:forcedEtag:reply:
- _objc_msgSend$getAttributeValues:forItemAtURL:reply:
- _objc_msgSend$getBackReferencingContainerIDsForURLs:reply:
- _objc_msgSend$getBookmarkDataForURL:onlyAllowItemKnowByServer:allowAccessByBundleID:reply:
- _objc_msgSend$getCreatorNameComponentsForURL:reply:
- _objc_msgSend$getEvictableSpaceWithReply:
- _objc_msgSend$getNonLocalVersionSenderWithReceiver:documentURL:includeCachedVersions:reply:
- _objc_msgSend$getPublishedURLForItemAtURL:forStreaming:requestedTTL:reply:
- _objc_msgSend$getQueryItemForURL:reply:
- _objc_msgSend$getiWorkNeedsShareMigrateAtURL:reply:
- _objc_msgSend$getiWorkPublishingBadgingStatusAtURL:reply:
- _objc_msgSend$getiWorkPublishingInfoAtURL:reply:
- _objc_msgSend$initForReadingFromData:error:
- _objc_msgSend$initWithURL:objid:kind:
- _objc_msgSend$invalidateAndDontNotifyDelegate
- _objc_msgSend$isEvictable
- _objc_msgSend$isFpfsItem
- _objc_msgSend$isTopLevel
- _objc_msgSend$listNonLocalVersionsWithReply:
- _objc_msgSend$moveBRSecurityBookmarkAtURL:toURL:reply:
- _objc_msgSend$openFileAtURL:appURL:reply:
- _objc_msgSend$options
- _objc_msgSend$overwriteAccessTimeForItemAtURL:atime:reply:
- _objc_msgSend$prepareAdditionCreationWithItemAtURL:byMoving:creationInfo:error:
- _objc_msgSend$removeItemFromDisk:reply:
- _objc_msgSend$resolveConflictWithName:atURL:reply:
- _objc_msgSend$secondaryConnectionForKey:initializer:
- _objc_msgSend$secondaryConnectionIfExistsForKey:
- _objc_msgSend$setBatchingChanges:
- _objc_msgSend$setBatchingDelay:
- _objc_msgSend$setFromURL:
- _objc_msgSend$setNameSpace:error:
- _objc_msgSend$setOptions:error:
- _objc_msgSend$setQueries:
- _objc_msgSend$setiWorkPublishingInfoAtURL:publish:readonly:reply:
- _objc_msgSend$startDownloadItemsAtURLs:options:reply:
- _objc_msgSend$startOperation:toCopyParticipantTokenAtURL:reply:
- _objc_msgSend$startOperation:toCopySharingAccessToken:reply:
- _objc_msgSend$startOperation:toCopySharingInfoAtURL:reply:
- _objc_msgSend$startOperation:toCopyShortTokenAtURL:reply:
- _objc_msgSend$startOperation:toEvictItemAtURL:reply:
- _objc_msgSend$startOperation:toModifyRecordAccessAtURL:allowAccess:reply:
- _objc_msgSend$startOperation:toPrepFolderForSharingAt:reply:
- _objc_msgSend$startOperation:toProcessSubitemsAtURL:maxSubsharesFailures:processType:reply:
- _objc_msgSend$storage
- _objc_msgSend$thumbnailChangedForItemAtURL:reply:
- _objc_msgSend$trashItemAtURL:reply:
- _objc_msgSend$updateItemFromURL:reply:
- _objc_msgSend$watchUbiquitousScopes:bundleID:predicate:
- _objc_msgSend$writeToURL:options:error:
- _pthread_rwlock_rdlock
- _pthread_rwlock_unlock
- _pthread_rwlock_wrlock
- _renamex_np
- _unlink
- br_currentHomeDir.once
- br_currentHomeDir.pathByPersonaID
- br_sharedProviderManagerWithDomainID:.defaultSharedProvider
- br_supportDirForPersona:dataSeparated:.once
- br_supportDirForPersona:dataSeparated:.pathByPersonaID
- getEvictableSpace:error:.__personaOnceToken
- getEvictableSpace:error:.__personalPersona
CStrings:
+ "+[BRAccount currentCachedLoggedInAccountWithError:]"
+ "+[BRAccount currentLoggedInAccountWithError:]"
+ "+[BRAccount refreshCurrentLoggedInAccount]"
+ "+[BRContainer(BRInternalAdditions) containerForMangledID:]"
+ "+[BRSpecialFolders _br_containerPathForDataSeparatedPersona]"
+ "+[BRSpecialFolders applicationSupportDirForCurrentPersona]"
+ "+[BRSpecialFolders homeDirForCurrentPersona]"
+ "+[BRSpecialFolders volumeUUIDForPersona:]_block_invoke"
+ "+[NSFileProviderManager(BRAdditions) br_getFPDomainsForProviderIdentifier:withError:]"
+ "+[NSFileProviderManager(BRAdditions) br_getFPDomainsForProviderIdentifier:withError:]_block_invoke"
+ "+[NSFileProviderManager(BRAdditions) br_getFPDomainsForProviderIdentifier:withError:]_block_invoke_2"
+ "-[BRDarwinNotifyReceiver initForEventName:withQueue:handler:]"
+ "-[BRDarwinNotifySender initForEventName:]"
+ "-[BRItemCollectionGatherer _accountDidChangeNotificationBlock]"
+ "-[BRItemCollectionGatherer _invalidateAndNotifyDelegate:]_block_invoke_2"
+ "-[BRItemCollectionGatherer _itemCollectionGathererSendUpdates]"
+ "-[BRItemCollectionGatherer _shouldFilterEvaluatedItem:collectionRootItem:]"
+ "-[BRReachabilityMonitor init]_block_invoke"
+ "-[NSFileProviderDomain(BRAdditions) br_volumeUUID]"
+ "-[NSNumber(BRAdditions) br_round:]"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/CloudDocs/framework/BRContainer.m"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/CloudDocs/framework/BRDeviceToDevice.m"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/CloudDocs/framework/SpotlightIndex_SoftLinking.m"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/CloudDocs/framework/foundation/BRScreenLockMonitor.m"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/CloudDocs/framework/operations/BRShareOperations.m"
+ "/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore"
+ "3437.101.1"
+ "@\"NSProgress\"52@0:8@\"NSString\"16@\"NSSecurityScopedURLWrapper\"24@\"NSFileProviderItemVersion\"32B40@?<v@?@\"NSFileProviderItemVersion\"@\"NSError\">44"
+ "@24@0:8q16"
+ "@52@0:8@16@24@32B40@?44"
+ "BRCDatabaseBackupManager"
+ "BRCDatabaseRestoreManager"
+ "BRCellularConstraintChangedNotification"
+ "BRCellularConstraintReached"
+ "BRDarwinNotifyReceiver"
+ "BRDarwinNotifySender"
+ "BRDeviceToDevice.m"
+ "BRMetadataUbiquitousItemFavoriteRankKey"
+ "BRSpecialFolders"
+ "Can't open iCloudDriveCore"
+ "Document shouldn't be downloaded over cellular"
+ "Td,R,N"
+ "User cancelled dialog"
+ "[CRIT] UNREACHABLE: BRFetchCollaborationIdentifierForItemAtURL should not run when FPFS enabled%@"
+ "[CRIT] UNREACHABLE: Can't get account volume UUID%@"
+ "[CRIT] UNREACHABLE: Can't get current cached logged in account from the daemon%@"
+ "[CRIT] UNREACHABLE: Can't get current logged in account from the daemon%@"
+ "[CRIT] UNREACHABLE: Can't get domain volume UUID%@"
+ "[CRIT] UNREACHABLE: Can't refresh current logged in account from the daemon%@"
+ "[CRIT] UNREACHABLE: Expecting normal number. Got %@%@"
+ "[CRIT] UNREACHABLE: Failed registering check%@"
+ "[CRIT] UNREACHABLE: Failed to adopt persona for notification %s due to %@%@"
+ "[CRIT] UNREACHABLE: Failed to adopt persona for volumeUUIDForPersona%@"
+ "[CRIT] UNREACHABLE: Invalid Arguments%@"
+ "[CRIT] UNREACHABLE: failed to get app library name for url %@%@"
+ "[CRIT] UNREACHABLE: failed to get container URL for %@%@"
+ "[CRIT] UNREACHABLE: failed to parse the given data to a plist. error: %@%@"
+ "[CRIT] UNREACHABLE: significantDigits must be positive integer value. Got %u%@"
+ "[DEBUG] %@ - Failed getting provider domain: %@%@"
+ "[DEBUG] BRItemCollectionGatherer - appLibrary %@ with url %@ retries left %d%@"
+ "[DEBUG] Found plistURL: %@ for mangledID: %@%@"
+ "[DEBUG] Got cellular network %s%@"
+ "[DEBUG] Got network updated status %u%@"
+ "[DEBUG] Matched account %@ (vid=%@) and domain %@ (vid=%@) volume IDs match%@"
+ "[DEBUG] recalculating purgeable data for %@%@"
+ "[DEBUG] ┏%llx Replace data for container %@. Use purgeable data [%s].%@"
+ "[WARNING] Can't open iCloudDriveCore : %s%@"
+ "[WARNING] Matched account %@ (vid=%@) and domain %@ (vid=%@) volume IDs DO NOT match%@"
+ "_accessDataRepresentation:inBlock:"
+ "_accessPurgeableDataRepresentation:inBlock:"
+ "_accessRebuiltPurgeableDataRepresentation:inBlock:"
+ "_accountDidChangeNotificationBlock"
+ "_addDeletedItems:"
+ "_addUpdatedItems:"
+ "_addedItems"
+ "_br_fetchItemServiceAsyncProxy:"
+ "_br_fileProviderErrorWithFallbackFileProviderErrorCode:"
+ "_deletedItems"
+ "_eventName"
+ "_getDeletedItems"
+ "_getUpdatedItems"
+ "_invalidateQueue"
+ "_invalidated"
+ "_isCellularNetwork"
+ "_itemCollectionGathererSendUpdates"
+ "_lastState"
+ "_notificationPacer"
+ "_setupAndResumeForPersonaID:"
+ "_shouldFilterEvaluatedItem:collectionRootItem:"
+ "_stopObeservingCollections"
+ "_token"
+ "_updateCellularNetworkStatusForObserver:isCellularNetwork:previousCellularStatus:"
+ "applicationSupportDirForCurrentPersona"
+ "br_fileProviderErrorForDownloadFlow"
+ "br_getFPDomainsForProviderIdentifier:withError:"
+ "br_getMigrationStatusForDSID:"
+ "br_round:"
+ "br_volumeUUID"
+ "br_zipApplyWithArray:applyBlock:"
+ "brc_errorCantRegisterBGSystemTask"
+ "brc_errorCellularStatusChanged"
+ "brc_errorNetworkUnreachable"
+ "brc_errorNetworkUnreachableDueToCellularConstraint"
+ "brc_errorShouldNotDownloadOverCellular"
+ "brc_errorUserCancelledDialog"
+ "c24@0:8@16"
+ "cellular-constraints-listener"
+ "checkMachLookupForService:"
+ "classBRCDatabaseBackupManager"
+ "classBRCDatabaseRestoreManager"
+ "collection-gatherer"
+ "collection-gatherer-pacer-min-fire-interval"
+ "collectionGathererPacerMinFireInterval"
+ "com.apple.br.item-collection-gatherer.invalidate"
+ "com.apple.clouddocs.internal.fpfs-extension"
+ "components:fromDate:"
+ "currentCalendar"
+ "currentPersonaMatchesID:"
+ "dateFromComponents:"
+ "defaultConnectionForPersonaID:"
+ "defaultConnectionIfExistsForPersonaID:"
+ "dropSpotlightIndexWithReply:"
+ "fetchItemServiceAsyncProxyForURL:handler:"
+ "fp_volumeUUID"
+ "getAvailableBytesForUploadOverCellularWithReply:"
+ "getEnhancedDrivePrivacyStatusForContainer:onServer:reply:"
+ "getLastMidnightDate"
+ "homeDirForCurrentPersona"
+ "iCloudDriveCoreLibrary"
+ "initBRCDatabaseBackupManager"
+ "initBRCDatabaseRestoreManager"
+ "initForEventName:"
+ "initForEventName:withQueue:handler:"
+ "initWithUserURL:"
+ "initWithUserURL:outputUserURL:"
+ "isCellularNetwork"
+ "isFPFSExtension"
+ "lastState"
+ "lookupCollectionGathererPacerMinFireInterval:"
+ "notifyChangedState:"
+ "objCType"
+ "overrideUploadOnCellularConstraintsWithReply:"
+ "providerDomainWithID:cachePolicy:error:"
+ "reachabilityMonitor:didChangeCellularNetworkTo:"
+ "secondaryConnectionForPersonaID:"
+ "secondaryConnectionIfExistsForPersonaID:"
+ "setEnhancedDrivePrivacySupported:forContainer:reply:"
+ "setHour:"
+ "setMinute:"
+ "setNanosecond:"
+ "setSecond:"
+ "storageURLs"
+ "test_getInvalidateQueue"
+ "unlimitedUpdatesOverCellularWithEnablementStatus:reply:"
+ "unreachable: BRFetchCollaborationIdentifierForItemAtURL should not run when FPFS enabled"
+ "unreachable: Can't get current cached logged in account from the daemon"
+ "unreachable: Can't get current logged in account from the daemon"
+ "unreachable: Can't refresh current logged in account from the daemon"
+ "uploadItemIdentifier:withContents:baseVersion:basedOnOriginalVersion:reply:"
+ "usingCellular:"
+ "v16@?0Q8"
+ "v32@0:8@16B24B28"
+ "v36@0:8@\"NSString\"16B24@?<v@?B@\"NSError\">28"
+ "v36@0:8B16@\"NSString\"20@?<v@?@\"NSError\">28"
+ "v36@0:8B16@20@?28"
+ "validateConnectionDomainWithDomainIdentifier:databaseID:reply:"
+ "validateConnectionExtensionInfoForPersonaID:"
+ "volumeUUIDForPersona:"
- "%@ is reachable."
- "%K = %@ OR %K.URLByDeletingLastPathComponent.path = %@"
- "%K = %@ OR %K.path = %@"
- "+[NSString(BRPathAdditions) _br_containerPathForDataSeparatedPersona]"
- "+[NSString(BRPathAdditions) br_currentHomeDir]"
- "+[NSString(BRPathAdditions) br_supportDirForPersona:dataSeparated:]"
- "-[BRFileObjectID isAppLibraryDocumentsFolder]"
- "-[BRFileObjectID isAppLibraryRoot]"
- "-[BRItemCollectionGatherer _addItemCollectionOnItem:]_block_invoke"
- "-[BRItemCollectionGatherer _invalidateAndNotifyDelegate:]_block_invoke"
- "-[BRItemCollectionGatherer _startObservingAccountTokenDidChangeNotification]_block_invoke"
- "-[BRListNonLocalVersionsOperation start]_block_invoke"
- "-[BROperation remoteFPFSObject]"
- "-[BRShareOperation remoteFPFSObject]"
- "-[NSFileManager(BRAdditions) br_movePromisedItemAtURL:toURL:error:]_block_invoke"
- "-[NSFileManager(BRAdditions) br_putBackTrashedItemAtURL:resultingURL:error:]"
- "-[NSFileManager(TempFilesAdditions) brc_createTemporaryFdInDirectory:withTemplate:error:]"
- "-[NSFileProviderManager(BRAdditions) br_getFPDomainsWithError:]"
- "-[NSFileProviderManager(BRAdditions) br_getFPDomainsWithError:]_block_invoke"
- "-[NSFileProviderManager(BRAdditions) br_getFPDomainsWithError:]_block_invoke_2"
- "-[NSString(BRPathAdditions) br_realpath]"
- "-[_BRContainerItem initWithQueryItem:container:zoneRowID:]"
- ".~"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/CloudDocs/framework/BRContainer.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/CloudDocs/framework/SpotlightIndex_SoftLinking.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/CloudDocs/framework/foundation/BRScreenLockMonitor.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/CloudDocs/framework/operations/BRShareOperations.m"
- "3097.81.2"
- "57T9237FN3.net.whatsapp.WhatsApp"
- "@\"BRDaemonConnection\"8@?0"
- "@\"NSProgress\"48@0:8@\"NSString\"16@\"NSSecurityScopedURLWrapper\"24@\"NSFileProviderItemVersion\"32@?<v@?@\"NSFileProviderItemVersion\"@\"NSError\">40"
- "@48@0:8@16@24@32@?40"
- "BRCXPCBRItemServiceProtocolInterface_block_invoke"
- "BRCXPCICDFileProviderClientSideCollaborationProtocolInterface_block_invoke"
- "BRFileProviderExtensionBackChannel"
- "BRItemNotificationSendingLegacy"
- "BRNonLocalVersionSending"
- "BRiWorkSharingSetSharingState_block_invoke"
- "CKRecordZoneID"
- "The move between those locations is invalid"
- "URLForDirectory:inDomain:appropriateForURL:create:error:"
- "Unable to make write promise at '%@'"
- "Unable to open fault at '%@'"
- "Unable to transfer doc-id from '%@' to '%@'"
- "Z"
- "[CRIT] Asking for FPFS object when FPFS isn't enabled%@"
- "[CRIT] Assertion failed: !FPIsCloudDocsWithFPFSEnabled()%@"
- "[CRIT] Assertion failed: FPIsCloudDocsWithFPFSEnabled()%@"
- "[CRIT] Assertion failed: capability & BRMoveCapabilityMaskAllow%@"
- "[CRIT] Assertion failed: error != nil%@"
- "[CRIT] Assertion failed: gBRActiveQueriesSet.count == gBRActiveQueries%@"
- "[CRIT] Assertion failed: isFpfs || self.isDead%@"
- "[CRIT] Assertion failed: zoneRowID%@"
- "[CRIT] UNREACHABLE: Can't use the fpfs sync proxy when fpfs isn't enabled%@"
- "[CRIT] UNREACHABLE: Failed to adopt persona for notification %s%@"
- "[CRIT] UNREACHABLE: IsAppLibraryRoot called on non-fpfs code%@"
- "[CRIT] UNREACHABLE: Using client side collaboration service protocol from legacy%@"
- "[CRIT] UNREACHABLE: Using item service protocol from legacy%@"
- "[CRIT] UNREACHABLE: isAppLibraryDocumentsFolder called on non-fpfs code%@"
- "[DEBUG] %@: resuming receiver%@"
- "[DEBUG] %@: suspending receiver%@"
- "[DEBUG] BRItemCollectionGatherer - appLibrary %@ with url %@%@"
- "[DEBUG] Preventing returning the put back info path when parented by .Trash: %@%@"
- "[DEBUG] We are in Legacy, no need to wait for migration%@"
- "[DEBUG] failed to write xattr:  %{errno}d%@"
- "[DEBUG] failed to writeToURL: %@%@"
- "[DEBUG] group activity sharing item at %@%@"
- "[DEBUG] moving %@ to %@%@"
- "[DEBUG] not implemented: fallback to itemID %@%@"
- "[DEBUG] realpath(%@) failed %{errno}d%@"
- "[DEBUG] ┏%llx Replace data for container %@%@"
- "[DEBUG] ┏%llx moving from: %@\n       to:   %@\n%@"
- "[DEBUG] ┏%llx restoring trashed item %@%@"
- "[DEBUG] ┳%llx getting container failed: %@%@"
- "[ERROR] %@ does not seem to be reachable%@"
- "[ERROR] %@: %s(%d)%@"
- "[ERROR] Can't create temporary directory%@"
- "[ERROR] Failed to copy properties of URL: %@%@"
- "[ERROR] can't create predicate for %@: %@%@"
- "[ERROR] can't get create predicate for %@: %@%@"
- "[ERROR] copyItem failed: %@%@"
- "[ERROR] couldn't enumerate %@%@"
- "[ERROR] couldn't find putback url: %@%@"
- "[ERROR] failed getting a sender for '%@' - %@%@"
- "[ERROR] failed receiving versions for '%@' - %@%@"
- "[ERROR] failed setting the version store for '%@' - %@%@"
- "[ERROR] no file name in fault at %@%@"
- "[ERROR] writeToURL failed: %@%@"
- "[WARNING] Attempting rename by copy, since rename(%s, %s) failed with %@.%@"
- "__itemAtURL:didGainVersionWithClientID:name:purposeID:"
- "__itemAtURL:didResolveConflictVersionWithClientID:name:purposeID:"
- "_br_fetchItemServiceSyncProxy:"
- "_isFPFSItem"
- "_isFPFSMode"
- "_reportPosixWriteError"
- "_setupAndResumeForKey:"
- "br_addPhysicalProperty"
- "br_currentHomeDir"
- "br_fileProviderErrorWithFPFS:"
- "br_supportDirForPersona:dataSeparated:"
- "brc_createTemporaryFdInDirectory:withTemplate:error:"
- "broken FPFS proxy"
- "com.apple.icloud.itemName"
- "contentsOfDirectoryAtPath:error:"
- "copyItemAtURL:toURL:error:"
- "createAdditionStagedAtURL:creationInfo:completionHandler:"
- "defaultConnectionForKey:initializer:"
- "defaultConnectionIfExistsForKey:"
- "documentURL"
- "fakeloser_"
- "fetchItemServiceSyncProxyForURL:handler:"
- "gz"
- "i40@0:8@16@24^@32"
- "initForReadingFromData:error:"
- "invalidateExtension"
- "listNonLocalVersionsWithReply:"
- "options"
- "predicateForChildrenOfURL"
- "predicateForURL"
- "prepareAdditionCreationWithItemAtURL:byMoving:creationInfo:error:"
- "sb-"
- "secondaryConnectionForKey:initializer:"
- "secondaryConnectionIfExistsForKey:"
- "setNameSpace:error:"
- "setOptions:error:"
- "storage"
- "syncedChangeTag"
- "uploadItemIdentifier:withContents:baseVersion:reply:"
- "v24@?0@\"BRQueryItem\"8@\"NSError\"16"
- "v24@?0@\"GSAddition\"8@\"NSError\"16"
- "v24@?0Q8@\"NSError\"16"
- "v32@?0@\"<BRNonLocalVersionSending>\"8@\"NSURL\"16@\"NSError\"24"
- "v36@0:8@\"NSURL\"16S24@?<v@?@\"NSError\">28"
- "v36@0:8@16S24@?28"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"<BRFileProviderExtensionBackChannel>\"32@?<v@?@\"NSError\">40"
- "validateConnectionDomainWithDomainIdentifier:databaseID:backChannel:reply:"
- "writeToURL:options:error:"
- "xz"
- "~$"

```
