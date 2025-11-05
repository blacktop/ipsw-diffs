## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/Versions/A/FileProvider`

```diff

-2732.81.1.0.0
-  __TEXT.__text: 0x145cdc
-  __TEXT.__auth_stubs: 0x1ba0
-  __TEXT.__objc_methlist: 0xc0f0
-  __TEXT.__const: 0x5c0
-  __TEXT.__gcc_except_tab: 0xa0f8
-  __TEXT.__cstring: 0x14088
-  __TEXT.__oslogstring: 0xd541
-  __TEXT.__dlopen_cstrs: 0x709
+2882.101.2.0.0
+  __TEXT.__text: 0x149ec4
+  __TEXT.__auth_stubs: 0x1da0
+  __TEXT.__objc_methlist: 0xdf1c
+  __TEXT.__const: 0x84e
+  __TEXT.__gcc_except_tab: 0xa17c
+  __TEXT.__cstring: 0x14112
+  __TEXT.__oslogstring: 0xd7e2
+  __TEXT.__dlopen_cstrs: 0x6b9
   __TEXT.__ustring: 0x21e
-  __TEXT.__unwind_info: 0x53f0
-  __TEXT.__objc_classname: 0x1f56
-  __TEXT.__objc_methname: 0x22aeb
-  __TEXT.__objc_methtype: 0x636a
-  __TEXT.__objc_stubs: 0x13460
-  __DATA_CONST.__got: 0xaa0
-  __DATA_CONST.__const: 0x1658
-  __DATA_CONST.__objc_classlist: 0x660
+  __TEXT.__swift5_typeref: 0xb4
+  __TEXT.__constg_swiftt: 0x60
+  __TEXT.__swift5_reflstr: 0x45
+  __TEXT.__swift5_fieldmd: 0x44
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_assocty: 0x60
+  __TEXT.__swift5_proto: 0x1c
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__swift_as_entry: 0x4
+  __TEXT.__swift_as_ret: 0x4
+  __TEXT.__unwind_info: 0x56d8
+  __TEXT.__eh_frame: 0xa0
+  __TEXT.__objc_classname: 0x1f02
+  __TEXT.__objc_methname: 0x22ef0
+  __TEXT.__objc_methtype: 0x65de
+  __TEXT.__objc_stubs: 0x13680
+  __DATA_CONST.__got: 0xab8
+  __DATA_CONST.__const: 0x16c0
+  __DATA_CONST.__objc_classlist: 0x650
   __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x290
+  __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x67e0
-  __DATA_CONST.__objc_protorefs: 0x148
-  __DATA_CONST.__objc_superrefs: 0x520
-  __DATA_CONST.__objc_arraydata: 0xa98
-  __AUTH_CONST.__auth_got: 0xde0
-  __AUTH_CONST.__const: 0x6940
-  __AUTH_CONST.__cfstring: 0x10e20
-  __AUTH_CONST.__objc_const: 0x268c8
+  __DATA_CONST.__objc_selrefs: 0x6b00
+  __DATA_CONST.__objc_protorefs: 0x140
+  __DATA_CONST.__objc_superrefs: 0x518
+  __DATA_CONST.__objc_arraydata: 0xaa0
+  __AUTH_CONST.__auth_got: 0xee0
+  __AUTH_CONST.__const: 0x6a88
+  __AUTH_CONST.__cfstring: 0x10fe0
+  __AUTH_CONST.__objc_const: 0x22fa8
   __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH_CONST.__objc_arrayobj: 0x168
-  __AUTH.__objc_data: 0x1360
-  __DATA.__objc_ivar: 0xfcc
-  __DATA.__data: 0x2278
-  __DATA.__bss: 0x980
-  __DATA_DIRTY.__objc_data: 0x2c60
+  __AUTH_CONST.__objc_arrayobj: 0x180
+  __AUTH.__objc_data: 0x1310
+  __DATA.__objc_ivar: 0xfd8
+  __DATA.__data: 0x21b0
+  __DATA.__bss: 0xcb0
+  __DATA.__common: 0x2b
+  __DATA_DIRTY.__objc_data: 0x2c10
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: 89FB864F-DDFE-3DEF-840A-4518E0C2454F
-  Functions: 6863
-  Symbols:   15773
-  CStrings:  12024
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  UUID: ED29D2B8-E24C-3FB8-BD79-5990BACDC9D3
+  Functions: 7165
+  Symbols:   16100
+  CStrings:  12077
 
Symbols:
+ +[FPAppMetadata _isContainerIDPermitted:].cold.1
+ +[FPDaemonConnection connectionForUser:].cold.1
+ +[FPDaemonConnection runningInSyncBubble].cold.1
+ +[FPDaemonConnection sharedConnection].cold.1
+ +[FPDaemonOperationManager sharedInstance].cold.1
+ +[FPItemCollection initialize].cold.1
+ +[FPItemDecoration _decorationCache].cold.1
+ +[FPItemDecoration infoForItem:parentInfo:].cold.1
+ +[FPItemManager defaultManager].cold.1
+ +[FPItemToURLResourcesConverter dictionaryFromItem:requestedKeys:].cold.1
+ +[FPProgressManager defaultManager].cold.1
+ +[FPProviderDomain _t_forceReadCacheFromDisk]
+ +[FPProviderDomain _t_ignoreUpdateNotifications:]
+ +[FPProviderDomain _t_loadCacheOnHandlerAdding:]
+ +[FPProviderDomain allowedToReadCacheFromDisk]
+ +[FPProviderDomain endMonitoringProviderDomainChanges:].cold.1
+ +[FPProviderDomain fetchProviderDomainWithID:completionHandler:].cold.1
+ +[FPProviderDomain fetchProviderDomainWithID:completionHandler:].cold.2
+ +[FPProviderDomain hasProviderDomainAccess].cold.1
+ +[FPProviderDomain readCacheFromDisk:]
+ +[FPProviderDomain selectNewProviderDomain:knownFolders:skipReleasePrompt:completionHandler:]
+ +[FPProviderDomainChangesReceiver _sharedChangesReceiverInitIfNeeded:].cold.1
+ +[FPProviderDomainChangesReceiver allowedToReadCacheFromDisk]
+ +[FPProviderDomainChangesReceiver allowedToReadCacheFromDisk].cold.1
+ +[FPProviderDomainChangesReceiver readCacheFromDisk:]
+ +[FPProviderDomainChangesReceiver readCacheFromDisk:].cold.1
+ +[FPProviderDomainChangesReceiver readCacheFromDisk:].cold.2
+ +[FPReachabilityMonitor sharedReachabilityMonitor].cold.1
+ +[FPSandboxingURLWrapper wrapperWithSecurityScopedURL:].cold.1
+ +[FPSpotlightCollector processingQueue].cold.1
+ +[FPSpotlightIndexer setIndexerProperty:forKey:supportURL:].cold.1
+ +[FPStitchingManager sharedInstance].cold.1
+ +[FPTask exec:error:]
+ +[FPTask exec:stdoutString:stderrString:error:]
+ +[FPTask exec:stdoutString:stderrString:error:].cold.1
+ +[FPTask simulatorRoot]
+ +[FPThreadedCopier sharedCopier].cold.1
+ +[FPUserInfo mergeWithUserInfo:intoParentUserInfo:].cold.1
+ +[FPUserInfo mergeWithUserInfo:intoParentUserInfo:].cold.2
+ +[FPUserInfo mergeWithUserInfo:intoParentUserInfo:].cold.3
+ +[FPUserInfo mergeWithUserInfo:intoParentUserInfo:].cold.4
+ +[FPUserInfo mergeWithUserInfo:intoParentUserInfo:].cold.5
+ +[FPUserInfo mergeWithUserInfo:intoParentUserInfo:].cold.6
+ +[FPUserInfo mergeWithUserInfo:intoParentUserInfo:].cold.7
+ +[FPUserInfo mergeWithUserInfo:intoParentUserInfo:].cold.8
+ +[FPUserInfo unzipKeysWithZippedArray:].cold.1
+ +[FPUserInfo unzipValuesWithZippedArray:].cold.1
+ +[FPUserInfo zipWithArray1:array2:].cold.1
+ +[NSArray(FPFrameworkAdditions) fp_sortDescriptorByDisplayName].cold.1
+ +[NSArray(FPFrameworkAdditions) fp_sortDescriptorByDocumentSize].cold.1
+ +[NSArray(FPFrameworkAdditions) fp_sortDescriptorByLastUsedDate].cold.1
+ +[NSArray(FPFrameworkAdditions) fp_sortDescriptorByModifiedDateDescending].cold.1
+ +[NSError(FPAdditions) fp_initLocalizationStrings].cold.1
+ +[NSError(NSFileProviderError) fileProviderErrorForCollisionWithItem:].cold.1
+ +[NSError(NSFileProviderError) fileProviderErrorForNonExistentItemWithIdentifier:].cold.1
+ +[NSError(NSFileProviderError) fileProviderErrorForRejectedDeletionOfItem:].cold.1
+ +[NSFileProviderItemVersion beforeFirstSyncComponent].cold.1
+ +[NSFileProviderManager _registerNotificationsForProviderIdentifier:].cold.1
+ +[NSFileProviderManager addDomain:forProviderIdentifier:byImportingDirectoryAtURL:userAllowedDBDrop:knownFolders:synchronous:completionHandler:].cold.1
+ +[NSFileProviderManager getDomainsForProviderIdentifier:completionHandler:].cold.1
+ +[NSFileProviderManager getDomainsWithCompletionHandler:].cold.1
+ +[NSFileProviderManager getIdentifierForUserVisibleFileAtURL:completionHandler:].cold.1
+ +[NSFileProviderManager registerDomainServicer:forDomain:].cold.1
+ +[NSFileProviderManager registerRootURL:forDomain:].cold.1
+ +[NSFileProviderManager removeAllDomainsForProviderIdentifier:completionHandler:].cold.1
+ +[NSFileProviderManager removeDomain:forProviderIdentifier:completionHandler:].cold.1
+ +[NSFileProviderManager removeDomain:mode:completionHandler:].cold.1
+ +[NSFileProviderManager resolvableErrorCodes].cold.1
+ +[NSFileProviderManager writePlaceholderAtURL:withMetadata:error:].cold.1
+ +[NSFileProviderManager writePlaceholderAtURL:withMetadata:error:].cold.2
+ +[NSFileProviderManager writePlaceholderAtURL:withMetadata:error:].cold.3
+ +[NSFileProviderManager(Import) importDomain:fromDirectoryAtURL:completionHandler:].cold.1
+ +[NSFileProviderManager(ImportPrivate) importDomain:forProviderIdentifier:fromDirectoryAtURL:completionHandler:].cold.1
+ +[NSFileProviderManager(ImportPrivate) importDomain:forProviderIdentifier:fromDirectoryAtURL:knownFolders:completionHandler:].cold.1
+ +[NSString(FPAdditions) fp_wordTokenizer].cold.1
+ +[NSURL(FPAdditions) fp_personaSharedDirectoryPathForUserID:].cold.3
+ +[NSURL(FPAdditions) fp_secureTempDirectoryIgnoringPersona].cold.1
+ +[UTType(FPCaching) fp_cachedTypeWithIdentifier:alreadyAvailableType:].cold.1
+ +[_NSFileProviderEmptyItemVersion emptyVersion].cold.1
+ -[FPAccessControlManager _killBundle:completionHandler:].cold.1
+ -[FPActionOperation initWithItemsOfDifferentProviders:action:].cold.1
+ -[FPActionOperation tryRecoveringFromError:completion:].cold.3
+ -[FPActionOperationLocator asFPItem].cold.1
+ -[FPActionOperationLocator asURL].cold.1
+ -[FPAggregateProgress addChild:].cold.1
+ -[FPArchiveOperation initWithItems:destinationFolder:].cold.1
+ -[FPArchiveOperation initWithItems:destinationFolder:].cold.2
+ -[FPArchiveTemporaryFolder initWithURL:].cold.1
+ -[FPBlockRecoveryAttempter attemptRecoveryFromError:optionIndex:].cold.5
+ -[FPBlockRecoveryAttempter attemptRecoveryFromError:optionIndex:].cold.6
+ -[FPDaemonConnection checkErrorAgainstDiagnosticsJson:inputError:errorDirection:jobCode:completionHandler:]
+ -[FPDaemonConnection clearDiagnosticsState:completionHandler:]
+ -[FPDaemonConnection createItemBasedOnTemplate:fields:urlWrapper:options:bounceOnCollision:completionHandler:].cold.1
+ -[FPDaemonConnection forceIngestionForItemID:completionHandler:].cold.1
+ -[FPDaemonConnection forceIngestionForItemIDs:completionHandler:].cold.1
+ -[FPDaemonConnection forceLatestVersionOnDiskForItemID:completionHandler:].cold.1
+ -[FPDaemonConnection runFPCKForDomainWithID:databasesBackupsPath:options:reason:completionHandler:].cold.1
+ -[FPDaemonConnection updateLastUsedDateForFileURL:completionHandler:].cold.1
+ -[FPDaemonConnection validateDiagnosticsJson:completionHandler:]
+ -[FPDaemonConnection waitForStabilizationOfDomainWithID:mode:completionHandler:]
+ -[FPDownloadOperation actionMain].cold.1
+ -[FPExceptionToErrorProxy forwardInvocation:].cold.2
+ -[FPFileVersion registerThumbnailNotification].cold.1
+ -[FPGracePeriodTimer initWithAction:callbackQueue:delay:].cold.1
+ -[FPItem initWithProviderID:domainIdentifier:itemIdentifier:parentItemIdentifier:filename:contentType:].cold.1
+ -[FPItem initWithVendorItem:provider:domain:spotlightDomainIdentifier:extensionCapabilities:useFPFS:].cold.2
+ -[FPItem initWithVendorItem:provider:domain:spotlightDomainIdentifier:extensionCapabilities:useFPFS:].cold.3
+ -[FPItem isEvictedWithClone]
+ -[FPItem overrideFields:ofItem:].cold.63
+ -[FPItem setIsEvictedWithClone:]
+ -[FPItemCollection dataSource:wasInvalidatedWithError:].cold.1
+ -[FPItemCollection initWithPacing:].cold.1
+ -[FPItemID(FPFS) transformForMigratedCloudDocsProviderDomainIdentifier:].cold.1
+ -[FPItemManager _itemIsOfArchiveType:].cold.1
+ -[FPItemManager collectionForFolderItem:].cold.1
+ -[FPItemManager operationForAction:items:].cold.1
+ -[FPItemManager recursivelyExportItem:toURL:completionHandler:].cold.1
+ -[FPItemManager serverCollectionForFolderItem:].cold.1
+ -[FPListRemoteVersionsOperation initWithDocumentURL:].cold.1
+ -[FPModifyFavoritesOperation initWithItems:favoriteRanks:isUnfavorite:].cold.1
+ -[FPMoveOperation _preflightCheckProviderCanMoveWithErrors:].cold.1
+ -[FPMoveOperation _recoverFromCollisionError:withPolicy:].cold.2
+ -[FPMoveOperation actionMain].cold.1
+ -[FPMoveOperation runUserInteractionsPreflight:].cold.3
+ -[FPOperation _setRemoteCancellationHandler:].cold.1
+ -[FPOperation dealloc].cold.1
+ -[FPProgress initWithOperation:].cold.1
+ -[FPProviderDomain initWithProviderID:domain:].cold.1
+ -[FPProviderDomain isOnMainVolume]
+ -[FPProviderDomain setIsOnMainVolume:]
+ -[FPProviderDomainChangesReceiver _t_forceReadCacheFromDisk]
+ -[FPProviderDomainChangesReceiver _t_ignoreUpdateNotifications:]
+ -[FPProviderDomainChangesReceiver _t_loadCacheOnHandlerAdding:]
+ -[FPProviderDomainChangesReceiver ignoreUpdateNotifications]
+ -[FPProviderMonitor dealloc].cold.1
+ -[FPSearchQueryDataSource initWithQueryDescriptor:predicate:].cold.4
+ -[FPSearchQueryDataSource initWithQueryDescriptor:predicate:].cold.5
+ -[FPSetTagsOperation initWithItems:tagsLists:].cold.1
+ -[FPSpotlightCollector _createQueryForMountPoint:].cold.1
+ -[FPSpotlightCollector _start].cold.4
+ -[FPSpotlightCollector _start].cold.5
+ -[FPSpotlightCollector _start].cold.6
+ -[FPSpotlightFetchClientStateOperation _handleFetchedClientState:error:].cold.3
+ -[FPSpotlightIndexOneBatchOperation _markItemsForUpdate:index:completionHandler:]
+ -[FPStitchingSession transformItems:handler:].cold.1
+ -[FPTask execAsync].cold.2
+ -[FPTask exec].cold.2
+ -[FPTask exec].cold.3
+ -[FPTask newPreparedArgvArray]
+ -[FPUnarchiveOperation initWithItem:destinationFolder:].cold.1
+ -[FPUnarchiveOperation initWithItem:destinationFolder:].cold.2
+ -[FPUnarchiveOperation service:didReceiveArchivedItemsDescriptors:placeholderName:placeholderTypeIdentifier:].cold.1
+ -[FPUserInfo initWithKeys:values:].cold.1
+ -[FPVendorDefinedActionOperation initWithActionIdentifier:providerDomainID:itemIdentifiers:].cold.1
+ -[FPVendorDefinedActionOperation initWithActionIdentifier:providerDomainID:itemIdentifiers:].cold.2
+ -[FPXDomainContext itemFromVendorItem:].cold.1
+ -[FPXDomainContext itemFromVendorItem:].cold.2
+ -[FPXDomainContext updateCapabilities].cold.2
+ -[FPXExtensionContext additionalServiceSourcesForItemID:domain:extension:].cold.1
+ -[FPXExtensionContext domainContextForIdentifier:].cold.1
+ -[FPXExtensionContext domainContextForItemID:].cold.1
+ -[FPXObserver updateForProviderItem:].cold.2
+ -[FPXObserver verifyVendorToken:].cold.1
+ -[NSArray(FPFrameworkAdditions) fp_pickItemsFromArray:correspondingToIndexesOfItemsInArray:].cold.1
+ -[NSArray(_FPSpotlightQueryHelpers) _fp_filter:].cold.1
+ -[NSArray(_FPSpotlightQueryHelpers) _fp_map:].cold.1
+ -[NSFileProviderExtension extensionContext]
+ -[NSFileProviderExtension itemChanged:baseVersion:changedFields:contents:completionHandler:].cold.1
+ -[NSFileProviderExtension setExtensionContext:]
+ -[NSFileProviderExtension(CreateItem) createItemBasedOnTemplate:fields:contents:options:completionHandler:].cold.1
+ -[NSFileProviderExtension(CreateItem) createItemBasedOnTemplate:fields:contents:options:completionHandler:].cold.2
+ -[NSFileProviderItemVersion etagHash].cold.1
+ -[NSFileProviderItemVersion initWithMainContentVersion:equivalentContentVersions:mainMetadataVersion:equivalentMetadataVersions:lastEditorDeviceName:conflictResolved:].cold.1
+ -[NSFileProviderItemVersion initWithMainContentVersion:equivalentContentVersions:mainMetadataVersion:equivalentMetadataVersions:lastEditorDeviceName:conflictResolved:].cold.2
+ -[NSFileProviderManager _cacheProviderInfo].cold.5
+ -[NSFileProviderManager _failToSignalPendingChangesWithError:completionHandlersByItemID:].cold.1
+ -[NSFileProviderManager _initWithProviderIdentifier:groupName:domain:].cold.1
+ -[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:].cold.3
+ -[NSFileProviderManager getUserVisibleURLForItemIdentifier:completionHandler:].cold.1
+ -[NSFileProviderManager registerURLSessionTask:forItemWithIdentifier:completionHandler:].cold.1
+ -[NSFileProviderManager registerURLSessionTask:forItemWithIdentifier:completionHandler:].cold.2
+ -[NSFileProviderManager removeDomain:options:completionHandler:].cold.1
+ -[NSFileProviderManager removeDomain:options:preservedLocation:error:].cold.1
+ -[NSFileProviderManager stateDirectoryURLWithError:].cold.1
+ -[NSFileProviderManager temporaryDirectoryURLWithError:].cold.5
+ -[NSFileProviderManager(Diagnostics) requestDiagnosticCollectionForItemWithIdentifier:errorReason:completionHandler:]
+ -[NSFileProviderManager(PrivateDiagnostics) getDiagnosticAttributesForItems:completionHandler:]
+ -[NSFileProviderManager(Stabilization) waitForStabilizationWithMode:completionHandler:]
+ -[NSFileProviderSearchQuery(NSFileProviderSearch_Internal) csQueryScopes].cold.1
+ -[NSFileProviderSearchQuery(NSFileProviderSearch_Private) initWithSearchScopedToItemID:alternateItemID:].cold.1
+ -[NSString(FPAdditions) fp_enumerateTokensInRange:tokenizer:usingBlock:].cold.1
+ -[NSString(FPAdditions) fp_isCJKLanguageIdentifier].cold.1
+ -[NSString(FPAdditions) fp_prettyPathWithObfuscation:].cold.1
+ -[NSURL(FPFSHelpers) fp_moveUnderFolder:withNewName:coordinationOptions:allowBounce:allowCoordination:moveHandler:completionHandler:].cold.1
+ -[NSURL(FPFSHelpers) getMaxChildrenCount].cold.1
+ FPCacheForAnyDocumentRecentlyUsed.cold.1
+ FPDDaemonXPCInterface.cold.1
+ FPDaemonActionOperationClientXPCInterface.cold.1
+ FPDaemonActionOperationXPCInterface.cold.1
+ FPDataSourceBaseQueue.cold.1
+ FPExecutableNameForProcessIdentifier.cold.1
+ FPFSProviderIsDeniedForFPFS.cold.1
+ FPFSProviderIsForcedForFPFS.cold.1
+ FPFetchDatalessFileResolverUIDAtURL.cold.1
+ FPFetchDatalessFileResolverUIDAtURL.cold.2
+ FPFetchDatalessFileResolverUIDAtURL.cold.3
+ FPGetSharedDomainCachingPath.cold.1
+ FPGetSharedDomainCachingPath.cold.2
+ FPGetSharedDomainCachingPath.cold.3
+ FPGetSharedDomainCachingPath.cold.4
+ FPIgnoresForcedKeyChecks.cold.1
+ FPIsAnyDocumentRecentlyUsed.cold.1
+ FPItemPropertyNamesByURLResourceKey.cold.1
+ FPLocalizationBundle.cold.1
+ FPMatchingDictionaryKeys.cold.1
+ FPOSVersion.cold.1
+ FPPinningSupportedForItem.cold.1
+ FPSimulatorSupportInterface.cold.1
+ FPURLResourceKeysByItemPropertyNames.cold.1
+ FPXEnumeratorXPCInterface.cold.1
+ FPXOperationServiceXPCInterface.cold.1
+ FPXVendorXPCInterface.cold.1
+ GCC_except_table235
+ GCC_except_table285
+ GCC_except_table309
+ GCC_except_table310
+ GCC_except_table311
+ GCC_except_table313
+ GCC_except_table314
+ GCC_except_table325
+ GCC_except_table332
+ GCC_except_table333
+ GCC_except_table334
+ GCC_except_table344
+ GCC_except_table353
+ GCC_except_table354
+ GCC_except_table358
+ GCC_except_table360
+ GCC_except_table366
+ GCC_except_table376
+ GCC_except_table380
+ GCC_except_table384
+ GCC_except_table389
+ GCC_except_table391
+ GCC_except_table395
+ GCC_except_table401
+ GCC_except_table402
+ GCC_except_table408
+ GCC_except_table410
+ GCC_except_table422
+ GCC_except_table425
+ GCC_except_table444
+ GCC_except_table446
+ GCC_except_table448
+ GCC_except_table460
+ GCC_except_table461
+ GCC_except_table463
+ GCC_except_table467
+ GCC_except_table60
+ OBJC_IVAR_$_FPItem._isEvictedWithClone
+ OBJC_IVAR_$_FPProviderDomain._isOnMainVolume
+ OBJC_IVAR_$_FPProviderDomainChangesReceiver._dontLoadCacheFromDisk
+ OBJC_IVAR_$_FPProviderDomainChangesReceiver._ignoreUpdateNotifications
+ _CFDictionaryGetTypeID
+ _CFPreferencesGetAppBooleanValue
+ _CFPreferencesGetAppIntegerValue
+ _FPGetSharedDomainCachingPath
+ _FPItemAttributeValueFunction.cold.1
+ _FPItemAttributeValueFunction.cold.2
+ _FPPerformWithDefaultPersona
+ _FPPerformWithPersona.cold.1
+ _FPProviderNotFoundErrorForURLWithReason
+ _OBJC_CLASS_$_NSProcessInfo
+ __100-[FPXExtensionContext _singleItemChange:changedFields:bounce:bounceIndex:request:completionHandler:]_block_invoke.327
+ __103-[FPXExtensionContext modifyItem:baseVersion:changedFields:contents:options:request:completionHandler:]_block_invoke.316
+ __107-[NSFileProviderExtension(CreateItem) createItemBasedOnTemplate:fields:contents:options:completionHandler:]_block_invoke.349
+ __109-[FPXExtensionContext performActionWithIdentifier:onItemsWithIdentifiers:domainIdentifier:completionHandler:]_block_invoke.690
+ __109-[FPXExtensionContext signalNeedsReindexItemsWithIdentifiers:domainIdentifier:indexReason:completionHandler:]_block_invoke.349
+ __109-[FPXExtensionContext signalNeedsReindexItemsWithIdentifiers:domainIdentifier:indexReason:completionHandler:]_block_invoke.349.cold.1
+ __109-[FPXExtensionContext signalNeedsReindexItemsWithIdentifiers:domainIdentifier:indexReason:completionHandler:]_block_invoke.352
+ __110-[FPXExtensionContext URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.396
+ __110-[FPXExtensionContext URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.396.cold.1
+ __112-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:lookupOnly:reply:]_block_invoke.657
+ __112-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:lookupOnly:reply:]_block_invoke.663
+ __112-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:lookupOnly:reply:]_block_invoke.666
+ __112-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:lookupOnly:reply:]_block_invoke.672
+ __112-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:lookupOnly:reply:]_block_invoke.672.cold.1
+ __112-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:lookupOnly:reply:]_block_invoke.672.cold.2
+ __120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.639
+ __120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.639.cold.1
+ __120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.639.cold.2
+ __120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.639.cold.3
+ __120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.639.cold.4
+ __120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.639.cold.5
+ __120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.639.cold.6
+ __120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.643
+ __122-[FPXExtensionContext deleteSearchableItemsWithSpotlightDomainIdentifiers:domainIdentifier:indexReason:completionHandler:]_block_invoke.239
+ __137-[FPXExtensionContext fetchContentsForItemWithID:version:request:estimatedItemSize:isSymlink:extent:alignment:options:completionHandler:]_block_invoke.268
+ __137-[FPXExtensionContext fetchContentsForItemWithID:version:request:estimatedItemSize:isSymlink:extent:alignment:options:completionHandler:]_block_invoke.282
+ __137-[FPXExtensionContext fetchContentsForItemWithID:version:request:estimatedItemSize:isSymlink:extent:alignment:options:completionHandler:]_block_invoke.292
+ __137-[FPXExtensionContext fetchContentsForItemWithID:version:request:estimatedItemSize:isSymlink:extent:alignment:options:completionHandler:]_block_invoke.296
+ __155-[FPXExtensionContext fetchContentsForItemWithID:version:usingExistingContentsAtURL:existingVersion:request:estimatedItemSize:isSymlink:completionHandler:]_block_invoke.307
+ __155-[FPXExtensionContext fetchContentsForItemWithID:version:usingExistingContentsAtURL:existingVersion:request:estimatedItemSize:isSymlink:completionHandler:]_block_invoke.308
+ __30-[FPItem descriptionForFPCTL:]_block_invoke.1104
+ __32-[_CSSearchableItemAdapter tags]_block_invoke.137
+ __36-[NSFileProviderDomain setUserInfo:]_block_invoke.cold.1
+ __36-[NSFileProviderDomain setUserInfo:]_block_invoke.cold.2
+ __36-[NSFileProviderManager _connection]_block_invoke.167
+ __37+[FPXExtensionContext principalClass]_block_invoke.cold.1
+ __37+[FPXExtensionContext principalClass]_block_invoke.cold.2
+ __37-[FPListRemoteVersionsOperation main]_block_invoke.15
+ __37-[FPListRemoteVersionsOperation main]_block_invoke.8
+ __37-[FPListRemoteVersionsOperation main]_block_invoke.cold.1
+ __41-[FPSpotlightIndexOneBatchOperation main]_block_invoke.87
+ __41-[FPSpotlightIndexOneBatchOperation main]_block_invoke.94
+ __41-[FPSpotlightIndexOneBatchOperation main]_block_invoke.96
+ __41-[FPSpotlightIndexOneBatchOperation main]_block_invoke_2.97
+ __41-[FPSpotlightIndexOneBatchOperation main]_block_invoke_2.97.cold.1
+ __41-[FPSpotlightIndexOneBatchOperation main]_block_invoke_2.97.cold.2
+ __43-[NSFileProviderManager _cacheProviderInfo]_block_invoke.237
+ __44-[FPItemManager servicesForItemAtURL:error:]_block_invoke.261
+ __46-[FPMoveOperation _completedWithResult:error:]_block_invoke.cold.1
+ __47+[FPTask exec:stdoutString:stderrString:error:]_block_invoke.53
+ __47+[FPTask exec:stdoutString:stderrString:error:]_block_invoke.53.cold.1
+ __47+[FPTask exec:stdoutString:stderrString:error:]_block_invoke.54
+ __47+[FPTask exec:stdoutString:stderrString:error:]_block_invoke.cold.1
+ __50-[FPQueryCollection _enumerationSettingsPredicate]_block_invoke.cold.1
+ __50-[NSFileProviderManager _signalPendingEnumerators]_block_invoke.183
+ __50-[NSFileProviderSearchQuery(Predicates) predicate]_block_invoke.cold.1
+ __50-[NSFileProviderSearchQuery(Predicates) predicate]_block_invoke.cold.2
+ __51-[FPSearchCollection _enumerationSettingsPredicate]_block_invoke.cold.1
+ __52-[FPXExtensionContext itemForURL:completionHandler:]_block_invoke.389
+ __53-[FPProviderDomain domainStateWithCompletionHandler:]_block_invoke.357
+ __56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.410
+ __56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.411
+ __56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.411.cold.1
+ __56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.412
+ __56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.416
+ __56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke_2.cold.2
+ __58-[NSFileProviderSearchQuery(Predicates) filenamePredicate]_block_invoke.cold.3
+ __61+[FPProviderDomainChangesReceiver allowedToReadCacheFromDisk]_block_invoke.cold.1
+ __63-[FPXExtensionContext itemForItemID:request:completionHandler:]_block_invoke.378
+ __63-[FPXExtensionContext preflightTrashItemIDs:completionHandler:]_block_invoke.356
+ __63-[FPXExtensionContext preflightTrashItemIDs:completionHandler:]_block_invoke.360
+ __65-[FPXExtensionContext getKnownFolderLocations:completionHandler:]_block_invoke.755
+ __65-[FPXExtensionContext getKnownFolderLocations:completionHandler:]_block_invoke.755.cold.1
+ __65-[FPXExtensionContext providePlaceholderAtURL:completionHandler:]_block_invoke.367
+ __65-[FPXExtensionContext waitForStabilizationWithCompletionHandler:]_block_invoke.765
+ __66-[FPXExtensionContext wakeForSessionIdentifier:completionHandler:]_block_invoke.698
+ __66-[FPXExtensionContext wakeForSessionIdentifier:completionHandler:]_block_invoke.698.cold.1
+ __67-[FPPendingSetEnumerator enumerateItemsForObserver:startingAtPage:]_block_invoke.487
+ __67-[FPXExtensionContext bulkEvictItemsWithItemIDs:completionHandler:]_block_invoke.699
+ __67-[FPXExtensionContext bulkEvictItemsWithItemIDs:completionHandler:]_block_invoke.703
+ __68-[FPXEnumerator enumerateChangesFromToken:suggestedBatchSize:reply:]_block_invoke.cold.3
+ __68-[FPXExtensionContext disconnectDomainID:options:completionHandler:]_block_invoke.686
+ __68-[FPXExtensionContext preflightReparentItemIDs:underParentID:reply:]_block_invoke.602
+ __68-[FPXExtensionContext preflightReparentItemIDs:underParentID:reply:]_block_invoke.608
+ __69+[NSFileProviderManager _registerNotificationsForProviderIdentifier:]_block_invoke.165
+ __69-[FPPendingSetEnumerator enumerateChangesForObserver:fromSyncAnchor:]_block_invoke.493
+ __69-[FPPendingSetEnumerator enumerateChangesForObserver:fromSyncAnchor:]_block_invoke_2.496
+ __69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.620
+ __69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.620.cold.1
+ __69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.626
+ __69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.cold.3
+ __69-[FPXExtensionContext fetchPublishingURLForItemID:completionHandler:]_block_invoke.678
+ __69-[NSFileProviderSearchQuery(Predicates) allowedContentTypesPredicate]_block_invoke.cold.1
+ __70-[FPXExtensionContext _deleteIndexInDomainContexts:completionHandler:]_block_invoke.205
+ __71-[FPXExtensionContext bulkItemChanges:changedFields:completionHandler:]_block_invoke.338
+ __71-[FPXExtensionContext bulkItemChanges:changedFields:completionHandler:]_block_invoke.342
+ __71-[FPXExtensionContext valuesForAttributes:forItemID:completionHandler:]_block_invoke.526
+ __72-[FPXExtensionContext shouldConnectExternalDomainWithCompletionHandler:]_block_invoke.771
+ __73-[FPProviderDomainChangesReceiver updateProviderDomainsWithAttemptCount:]_block_invoke.52
+ __74-[FPXExtensionContext sendBlockedProcessNamesUpdateWithCompletionHandler:]_block_invoke.191
+ __78-[FPXExtensionContext attemptRecoveryFromError:optionIndex:completionHandler:]_block_invoke.706
+ __80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.210
+ __80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.210.cold.1
+ __80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.210.cold.2
+ __86-[FPXExtensionContext deleteItemWithID:baseVersion:options:request:completionHandler:]_block_invoke.629
+ __87-[FPXExtensionContext fetchServicesForItemID:allowRestrictedSources:completionHandler:]_block_invoke.573
+ __87-[FPXExtensionContext fetchServicesForItemID:allowRestrictedSources:completionHandler:]_block_invoke.579
+ __90-[FPXExtensionContext removeTrashedItemsOlderThanDate:domainIdentifier:completionHandler:]_block_invoke.242
+ __90-[FPXExtensionContext removeTrashedItemsOlderThanDate:domainIdentifier:completionHandler:]_block_invoke.242.cold.1
+ __93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.499
+ __93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.499.cold.1
+ __93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.512
+ __93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.512.cold.1
+ __93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.516
+ __93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.520
+ __93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.524
+ __93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.524.cold.1
+ __93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.525
+ __94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.373
+ __94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.373.cold.1
+ __94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.373.cold.2
+ __94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.373.cold.3
+ __94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.373.cold.4
+ __94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.374
+ __95-[FPXExtensionContext fetchAndStartEnumeratingWithSettings:observer:request:completionHandler:]_block_invoke.549
+ __95-[FPXExtensionContext fetchAndStartEnumeratingWithSettings:observer:request:completionHandler:]_block_invoke.552
+ __97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.440
+ __97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.459
+ __97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.459.cold.1
+ __97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.464
+ __97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.468
+ __97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.468.cold.1
+ __97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.469
+ __98-[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:]_block_invoke.150
+ __98-[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:]_block_invoke.150.cold.1
+ __98-[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:]_block_invoke.150.cold.2
+ __98-[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:]_block_invoke.150.cold.3
+ __98-[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:]_block_invoke.cold.2
+ __Block_copy
+ __Block_release
+ __FPCFCopyAttributeValuesForItem_block_invoke.31
+ __FPCFCopyAttributeValuesForItem_block_invoke.31.cold.1
+ __FPCrossDeviceItemIDForItemID_block_invoke.115
+ __FPCrossDeviceItemIDForItemID_block_invoke.119
+ __FPCrossDeviceItemIDForItemID_block_invoke.126
+ __FPCrossDeviceItemIDForItemID_block_invoke_2.121
+ __FPCrossDeviceItemIDForItemID_block_invoke_2.127
+ __FPEvictItemAtURL_block_invoke.44
+ __FPItemIDFromCrossDeviceItemID_block_invoke.172
+ __FPItemURLForCrossDeviceItemID_block_invoke.140
+ __FPItemURLForCrossDeviceItemID_block_invoke.140.cold.1
+ __FPItemURLForCrossDeviceItemID_block_invoke.147
+ __FPItemURLForCrossDeviceItemID_block_invoke.147.cold.1
+ __FPItemURLForCrossDeviceItemID_block_invoke.148
+ __FPItemURLForCrossDeviceItemID_block_invoke.166
+ __FPPerformWithPersona
+ __FPRegisterFileProvidersForUserAtURLs_block_invoke.23
+ __FPResolveSymlinkRecursive_block_invoke.179
+ __OBJC_$_CLASS_METHODS_NSFileProviderManager(MaterializedSet|PendingSet|Import|ImportPrivate|Barrier|Stabilization|Eviction|Attribution|ForceIngestion|Disconnection|TestingModeInteractive|GlobalProgress|NSFileProviderService|Materialize|MaterializePrivate|PrivateDiagnostics|KnownFolders|Diagnostics)
+ __OBJC_$_INSTANCE_METHODS_NSFileProviderManager(MaterializedSet|PendingSet|Import|ImportPrivate|Barrier|Stabilization|Eviction|Attribution|ForceIngestion|Disconnection|TestingModeInteractive|GlobalProgress|NSFileProviderService|Materialize|MaterializePrivate|PrivateDiagnostics|KnownFolders|Diagnostics)
+ ___117-[NSFileProviderManager(Diagnostics) requestDiagnosticCollectionForItemWithIdentifier:errorReason:completionHandler:]_block_invoke
+ ___117-[NSFileProviderManager(Diagnostics) requestDiagnosticCollectionForItemWithIdentifier:errorReason:completionHandler:]_block_invoke_2
+ ___37+[FPXExtensionContext principalClass]_block_invoke
+ ___47+[FPTask exec:stdoutString:stderrString:error:]_block_invoke
+ ___61+[FPProviderDomainChangesReceiver allowedToReadCacheFromDisk]_block_invoke
+ ___81-[FPSpotlightIndexOneBatchOperation _markItemsForUpdate:index:completionHandler:]_block_invoke
+ ___81-[FPSpotlightIndexOneBatchOperation _markItemsForUpdate:index:completionHandler:]_block_invoke_2
+ ___87-[NSFileProviderManager(Stabilization) waitForStabilizationWithMode:completionHandler:]_block_invoke
+ ___93+[FPProviderDomain selectNewProviderDomain:knownFolders:skipReleasePrompt:completionHandler:]_block_invoke
+ ___95-[NSFileProviderManager(PrivateDiagnostics) getDiagnosticAttributesForItems:completionHandler:]_block_invoke
+ ___95-[NSFileProviderManager(PrivateDiagnostics) getDiagnosticAttributesForItems:completionHandler:]_block_invoke_2
+ ___block_descriptor_280_e8_32bs_e40_i16?0^{fpfs_xattr=^{fpfs_xattr}*Q[0c]}8l
+ ___block_descriptor_32_e9_B16?0r*8l
+ ___block_descriptor_40_e8_32bs_e20_v24?08"NSError"16l
+ ___block_descriptor_40_e8_32bs_e44_v24?0"<FPDWakeupTransaction>"8"NSError"16l
+ ___block_descriptor_44_e8_32bs_e29_i16?0^{dirent=QQSSC[1024c]}8l
+ ___block_descriptor_44_e8_32bs_e8_i12?0i8l
+ ___block_descriptor_48_e8_32bs_e5_i8?0l
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSArray"8l
+ ___block_descriptor_48_e8_32s40s_e8_v12?0i8l
+ ___block_descriptor_48_e8_32s_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_52_e8_32bs_e206_i16?0^{fpfs_fileattrs={fpfs_item_handle=QQII*iI}{fpfs_metadata=ib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1Sq{timespec=qq}{timespec=qq}{timespec=qq}Q{fpfs_tag_data=^vQi}(?=II)QQq*q*^{fpfs_xattr}II*BB*QICii}*Q[0c]}8l
+ ___block_descriptor_56_e5_i8?0l
+ ___block_descriptor_56_e8_32s40bs_e56_v16?0"<FPDDomainServicing><FPXPCAutomaticErrorProxy>"8l
+ ___block_descriptor_56_e8_i12?0i8l
+ ___block_descriptor_60_e8_32bs_e8_i12?0i8l
+ ___block_descriptor_60_e8_32r_e5_i8?0l
+ ___block_descriptor_64_e8_32s40bs48r_e30_v24?0"FPItemID"8"NSError"16l
+ ___block_descriptor_64_e8_32s40bs48r_e52_v32?0"FPItem"8"FPExtensionResponse"16"NSError"24l
+ ___block_descriptor_64_e8_32s40s48bs_e19_v24?0"FPItem"8Q16l
+ ___block_descriptor_64_e8_32s40s48bs_e28_v24?0"FPItem"8"NSError"16l
+ ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0l
+ ___block_descriptor_84_e5_i8?0l
+ ___fpfs_evict_legacy_block_invoke.34
+ ___fpfs_recursive_prune_fault_block_invoke
+ ___fpfs_supports_download_lazily_v2_block_invoke
+ ___fpfs_t_is_evictable_at_block_invoke
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_memcpy9_8
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_0
+ ___swift_reflection_version
+ __block_literal_global.113
+ __block_literal_global.133
+ __block_literal_global.139
+ __block_literal_global.154
+ __block_literal_global.176
+ __block_literal_global.185
+ __block_literal_global.188
+ __block_literal_global.194
+ __block_literal_global.227
+ __block_literal_global.247
+ __block_literal_global.265
+ __block_literal_global.299
+ __block_literal_global.305
+ __block_literal_global.34
+ __block_literal_global.37
+ __block_literal_global.395
+ __block_literal_global.404
+ __block_literal_global.443
+ __block_literal_global.455
+ __block_literal_global.464
+ __block_literal_global.466
+ __block_literal_global.489
+ __block_literal_global.495
+ __block_literal_global.498
+ __block_literal_global.545
+ __block_literal_global.547
+ __block_literal_global.557
+ __block_literal_global.582
+ __block_literal_global.707
+ __block_literal_global.709
+ __block_literal_global.751
+ __fp_create_section.cold.1
+ __fpfs_supports_tap_to_feedback_block_invoke.cold.1
+ __fpfs_supports_tap_to_feedback_block_invoke.cold.2
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_FileProvider
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_FileProvider
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_FileProvider
+ __swift_FORCE_LOAD_$_swiftFileProvider
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_FileProvider
+ __swift_FORCE_LOAD_$_swiftIOKit
+ __swift_FORCE_LOAD_$_swiftIOKit_$_FileProvider
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_FileProvider
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_FileProvider
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_FileProvider
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_errno_$_FileProvider
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_math_$_FileProvider
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_signal_$_FileProvider
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_stdio_$_FileProvider
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swift_time_$_FileProvider
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftsys_time_$_FileProvider
+ __swift_FORCE_LOAD_$_swiftunistd
+ __swift_FORCE_LOAD_$_swiftunistd_$_FileProvider
+ _associated conformance So27NSFileProviderDomainVersionCSL04FileB0SQ
+ _associated conformance So37NSFileProviderVolumeUnsupportedReasonVs10SetAlgebraSCSQ
+ _associated conformance So37NSFileProviderVolumeUnsupportedReasonVs10SetAlgebraSCs25ExpressibleByArrayLiteral
+ _associated conformance So37NSFileProviderVolumeUnsupportedReasonVs9OptionSetSCSY
+ _associated conformance So37NSFileProviderVolumeUnsupportedReasonVs9OptionSetSCs0G7Algebra
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _container_copy_sandbox_token
+ _dataless_fault_header_convert_to_decmpfs_header
+ _dataless_fault_header_decode
+ _fpfs_eviction_properties
+ _fpfs_eviction_urgency_with_validation
+ _fpfs_fast_realpath
+ _fpfs_flock
+ _fpfs_get_purgable_flags
+ _fpfs_get_purgeable_non_evictable_urgency
+ _fpfs_lp_mkdirat
+ _fpfs_openbyid64_np
+ _fpfs_openparent
+ _fpfs_remove_content_dependent_xattrs
+ _fpfs_renameatx_np
+ _fpfs_set_support_long_paths_iopolicy
+ _fpfs_speculative_download_hierarchy_set
+ _fpfs_speculative_download_hierarchy_unset
+ _fpfs_supports_download_lazily_v2
+ _fpfs_t_is_evictable_at
+ _fpfs_update_purgency_during_restore
+ _get_current_user_uuid.cold.1
+ _kCFPreferencesAnyApplication
+ _kFPDefaultIOContext
+ _kFPDefaultIOContextForLocalStorage
+ _kFPDefaultIOContextForLocalStorage_block_invoke
+ _kFPDefaultIOContext_block_invoke_2
+ _kFPTaskErrorDomain
+ _kNSFileProviderUserInfoExperimentID
+ _notify_get_state
+ _notify_register_check
+ _objc_msgSend$_markItemsForUpdate:index:completionHandler:
+ _objc_msgSend$_t_forceReadCacheFromDisk
+ _objc_msgSend$_t_ignoreUpdateNotifications:
+ _objc_msgSend$_t_loadCacheOnHandlerAdding:
+ _objc_msgSend$allowedToReadCacheFromDisk
+ _objc_msgSend$checkErrorAgainstDiagnosticsJson:inputError:errorDirection:jobCode:completionHandler:
+ _objc_msgSend$clearDiagnosticsState:completionHandler:
+ _objc_msgSend$dataWithContentsOfFile:options:error:
+ _objc_msgSend$environment
+ _objc_msgSend$exec:stdoutString:stderrString:error:
+ _objc_msgSend$ignoreUpdateNotifications
+ _objc_msgSend$isEvictedWithClone
+ _objc_msgSend$newPreparedArgvArray
+ _objc_msgSend$processInfo
+ _objc_msgSend$readCacheFromDisk:
+ _objc_msgSend$requestDiagnosticCollectionForItemWithIdentifier:errorReason:completionHandler:
+ _objc_msgSend$selectNewProviderDomain:knownFolders:skipReleasePrompt:completionHandler:
+ _objc_msgSend$setContentPolicy:
+ _objc_msgSend$setEffectiveContentPolicy:
+ _objc_msgSend$setExtensionContext:
+ _objc_msgSend$setInheritedContentPolicy:
+ _objc_msgSend$slowFetchAttributes:protectionClass:bundleID:identifiers:completionHandler:
+ _objc_msgSend$validateDiagnosticsJson:completionHandler:
+ _objc_msgSend$waitForStabilizationOfDomainWithID:mode:completionHandler:
+ _objc_msgSend$waitForStabilizationWithMode:completionHandler:
+ _objc_msgSend$wakeUpForURLFixed:completionHandler:
+ _sandbox_extension_consume
+ _sandbox_extension_release
+ _statfs_ext
+ _swift_allocError
+ _swift_bridgeObjectRelease
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_release
+ _swift_retain
+ _swift_task_switch
+ _swift_willThrow
+ _symbolic $sSY
+ _symbolic $ss10SetAlgebraP
+ _symbolic $ss25ExpressibleByArrayLiteralP
+ _symbolic $ss9OptionSetP
+ _symbolic Sccyyt______pG s5ErrorP
+ _symbolic So21NSFileProviderManagerC
+ _symbolic Su
+ _symbolic _____ So21NSFileProviderManagerC04FileB0E17EligibilityResultO
+ _symbolic _____ So37NSFileProviderVolumeUnsupportedReasonV
+ _symbolic ______p s5ErrorP
+ _underlyingErrorForProviderNotFoundReason
+ allowedToReadCacheFromDisk.allowed
+ allowedToReadCacheFromDisk.onceToken
+ block_copy_helper.1
+ block_descriptor.3
+ block_destroy_helper.2
+ cachedFrameworkOverridingObjects.cold.1
+ fp_default_log.cold.1
+ fp_extension_log.cold.1
+ fp_shouldObfuscateFilenames.cold.1
+ fp_shouldObfuscateFilenames.delayInSec
+ fpfs_adopt_log.cold.1
+ fpfs_current_log.cold.1
+ fpfs_current_or_default_log.cold.1
+ fpfs_fset_is_shared.cold.1
+ fpfs_fset_is_shared_by_current_user.cold.1
+ fpfs_fset_owner_name.cold.1
+ fpfs_get_materialization_alignment.cold.1
+ fpfs_icd_package_extension_list_contains.cold.1
+ fpfs_icd_package_extension_list_init.cold.1
+ fpfs_is_internal_build.cold.1
+ fpfs_is_seed_build.cold.1
+ fpfs_materialize.cold.3
+ fpfs_pathpkg_check.cold.2
+ fpfs_supports_brm_sparse_files.cold.1
+ fpfs_supports_download_lazily_v2.cold.1
+ fpfs_supports_download_lazily_v2.feature_enabled
+ fpfs_supports_download_lazily_v2.once_token
+ fpfs_supports_lazy_recursive_deletion.cold.1
+ fpfs_supports_long_paths.cold.1
+ fpfs_supports_nx_for_testing.cold.1
+ fpfs_supports_partial_materialization.cold.1
+ fpfs_supports_pkg_dataless_escape_prevention.cold.1
+ fpfs_supports_sokoban.cold.1
+ fpfs_supports_speculative_set.cold.1
+ fpfs_supports_tap_to_feedback.cold.1
+ fpfs_xattr_flags_from_name.cold.1
+ frameworkOverridingModulesDirectoryURL.cold.1
+ fssync_default_log.cold.1
+ get_sd_reporter.cold.1
+ knownFolderLocationConcreteClasses.cold.1
+ principalClass.clazz
+ principalClass.onceToken
+ rewriteBeforeFirstSync.cold.2
- +[FPExtension_subsystem initForPlugInKit]
- +[FPExtension_subsystem sharedInstance]
- +[FPTask exec:stdoutString:stderrString:]
- +[FPXExtensionContext principalClass].cold.2
- +[FPXPlugInKitExtensionContext _extensionAuxiliaryHostProtocol]
- +[FPXPlugInKitExtensionContext _extensionAuxiliaryVendorProtocol]
- +[FPXPlugInKitExtensionContext principalClass]
- +[FPXPlugInKitExtensionContext setPrincipalClass:]
- +[NSFileProviderExtension _initializedByViewServices]
- -[FPDaemonConnection makeTopologicallySortedItemsOnDisk:completionHandler:]
- -[FPDaemonConnection makeTopologicallySortedItemsOnDisk:error:]
- -[FPExtension_subsystem beginUsing:withBundle:]
- -[FPExtension_subsystem endUsing:]
- -[FPXExtensionContext _setTransaction:]
- -[FPXPlugInKitExtensionContext .cxx_destruct]
- -[FPXPlugInKitExtensionContext initWithInputItems:listenerEndpoint:contextUUID:]
- -[NSFileProviderExtension beginRequestWithExtensionContext:]
- -[NSFileProviderManager(Diagnostics) getDiagnosticAttributesForItems:completionHandler:]
- FPIsCloudDocsWithFPFSEnabled.icdOnFPFSEnabled
- FPIsCloudDocsWithFPFSEnabled.onceToken
- FPIsFPCKXPCServiceEnabled.featureEnabledByDefault
- FPIsFPCKXPCServiceEnabled.onceToken
- FPPerformWithPersona.cold.2
- GCC_except_table231
- GCC_except_table234
- GCC_except_table293
- GCC_except_table294
- GCC_except_table324
- GCC_except_table329
- GCC_except_table330
- GCC_except_table331
- GCC_except_table342
- GCC_except_table349
- GCC_except_table350
- GCC_except_table355
- GCC_except_table361
- GCC_except_table367
- GCC_except_table372
- GCC_except_table377
- GCC_except_table378
- GCC_except_table383
- GCC_except_table388
- GCC_except_table390
- GCC_except_table398
- GCC_except_table399
- GCC_except_table404
- GCC_except_table406
- GCC_except_table413
- GCC_except_table419
- GCC_except_table438
- GCC_except_table440
- GCC_except_table441
- GCC_except_table454
- GCC_except_table456
- GCC_except_table457
- GCC_except_table462
- GCC_except_table87
- OBJC_IVAR_$_FPXPlugInKitExtensionContext._context
- _FPFeatureFlagHelenaIsEnabled
- _FPIsFPCKXPCServiceEnabled
- _FPStatVFS
- _OBJC_CLASS_$_FPExtension_subsystem
- _OBJC_CLASS_$_FPXPlugInKitExtensionContext
- _OBJC_CLASS_$_NSExtensionContext
- _OBJC_CLASS_$__NSExtensionContextVendor
- _OBJC_METACLASS_$_FPExtension_subsystem
- _OBJC_METACLASS_$_FPXPlugInKitExtensionContext
- _OBJC_METACLASS_$_NSExtensionContext
- _OUTLINED_FUNCTION_46
- _OUTLINED_FUNCTION_47
- _OUTLINED_FUNCTION_48
- _OUTLINED_FUNCTION_49
- __100-[FPXExtensionContext _singleItemChange:changedFields:bounce:bounceIndex:request:completionHandler:]_block_invoke.320
- __103-[FPXExtensionContext modifyItem:baseVersion:changedFields:contents:options:request:completionHandler:]_block_invoke.309
- __107-[NSFileProviderExtension(CreateItem) createItemBasedOnTemplate:fields:contents:options:completionHandler:]_block_invoke.353
- __109-[FPXExtensionContext performActionWithIdentifier:onItemsWithIdentifiers:domainIdentifier:completionHandler:]_block_invoke.676
- __109-[FPXExtensionContext signalNeedsReindexItemsWithIdentifiers:domainIdentifier:indexReason:completionHandler:]_block_invoke.342
- __109-[FPXExtensionContext signalNeedsReindexItemsWithIdentifiers:domainIdentifier:indexReason:completionHandler:]_block_invoke.342.cold.1
- __109-[FPXExtensionContext signalNeedsReindexItemsWithIdentifiers:domainIdentifier:indexReason:completionHandler:]_block_invoke.345
- __110-[FPXExtensionContext URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.389
- __110-[FPXExtensionContext URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.389.cold.1
- __112-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:lookupOnly:reply:]_block_invoke.643
- __112-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:lookupOnly:reply:]_block_invoke.649
- __112-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:lookupOnly:reply:]_block_invoke.652
- __112-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:lookupOnly:reply:]_block_invoke.658
- __112-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:lookupOnly:reply:]_block_invoke.658.cold.1
- __112-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:lookupOnly:reply:]_block_invoke.658.cold.2
- __120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.625
- __120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.625.cold.1
- __120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.625.cold.2
- __120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.625.cold.3
- __120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.625.cold.4
- __120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.625.cold.5
- __120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.625.cold.6
- __120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.629
- __122-[FPXExtensionContext deleteSearchableItemsWithSpotlightDomainIdentifiers:domainIdentifier:indexReason:completionHandler:]_block_invoke.232
- __137-[FPXExtensionContext fetchContentsForItemWithID:version:request:estimatedItemSize:isSymlink:extent:alignment:options:completionHandler:]_block_invoke.261
- __137-[FPXExtensionContext fetchContentsForItemWithID:version:request:estimatedItemSize:isSymlink:extent:alignment:options:completionHandler:]_block_invoke.275
- __137-[FPXExtensionContext fetchContentsForItemWithID:version:request:estimatedItemSize:isSymlink:extent:alignment:options:completionHandler:]_block_invoke.285
- __137-[FPXExtensionContext fetchContentsForItemWithID:version:request:estimatedItemSize:isSymlink:extent:alignment:options:completionHandler:]_block_invoke.289
- __155-[FPXExtensionContext fetchContentsForItemWithID:version:usingExistingContentsAtURL:existingVersion:request:estimatedItemSize:isSymlink:completionHandler:]_block_invoke.300
- __155-[FPXExtensionContext fetchContentsForItemWithID:version:usingExistingContentsAtURL:existingVersion:request:estimatedItemSize:isSymlink:completionHandler:]_block_invoke.301
- __30-[FPItem descriptionForFPCTL:]_block_invoke.1098
- __32-[_CSSearchableItemAdapter tags]_block_invoke.138
- __36-[NSFileProviderManager _connection]_block_invoke.162
- __37-[FPListRemoteVersionsOperation main]_block_invoke.14
- __41+[FPTask exec:stdoutString:stderrString:]_block_invoke.41
- __41+[FPTask exec:stdoutString:stderrString:]_block_invoke.41.cold.1
- __41+[FPTask exec:stdoutString:stderrString:]_block_invoke.42
- __41+[FPTask exec:stdoutString:stderrString:]_block_invoke.cold.1
- __41-[FPSpotlightIndexOneBatchOperation main]_block_invoke.75
- __41-[FPSpotlightIndexOneBatchOperation main]_block_invoke.81
- __41-[FPSpotlightIndexOneBatchOperation main]_block_invoke_2.82
- __41-[FPSpotlightIndexOneBatchOperation main]_block_invoke_2.82.cold.1
- __41-[FPSpotlightIndexOneBatchOperation main]_block_invoke_2.82.cold.2
- __43-[NSFileProviderManager _cacheProviderInfo]_block_invoke.232
- __44-[FPItemManager servicesForItemAtURL:error:]_block_invoke.256
- __50-[NSFileProviderManager _signalPendingEnumerators]_block_invoke.178
- __52-[FPXExtensionContext itemForURL:completionHandler:]_block_invoke.382
- __53-[FPProviderDomain domainStateWithCompletionHandler:]_block_invoke.354
- __56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.397
- __56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.403
- __56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.404.cold.1
- __56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.405
- __56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.406
- __63-[FPXExtensionContext itemForItemID:request:completionHandler:]_block_invoke.371
- __63-[FPXExtensionContext preflightTrashItemIDs:completionHandler:]_block_invoke.349
- __63-[FPXExtensionContext preflightTrashItemIDs:completionHandler:]_block_invoke.353
- __65-[FPXExtensionContext getKnownFolderLocations:completionHandler:]_block_invoke.744
- __65-[FPXExtensionContext getKnownFolderLocations:completionHandler:]_block_invoke.744.cold.1
- __65-[FPXExtensionContext providePlaceholderAtURL:completionHandler:]_block_invoke.360
- __65-[FPXExtensionContext waitForStabilizationWithCompletionHandler:]_block_invoke.754
- __66-[FPXExtensionContext wakeForSessionIdentifier:completionHandler:]_block_invoke.684
- __66-[FPXExtensionContext wakeForSessionIdentifier:completionHandler:]_block_invoke.684.cold.1
- __67-[FPPendingSetEnumerator enumerateItemsForObserver:startingAtPage:]_block_invoke.482
- __67-[FPXExtensionContext bulkEvictItemsWithItemIDs:completionHandler:]_block_invoke.685
- __67-[FPXExtensionContext bulkEvictItemsWithItemIDs:completionHandler:]_block_invoke.689
- __68-[FPXExtensionContext disconnectDomainID:options:completionHandler:]_block_invoke.672
- __68-[FPXExtensionContext preflightReparentItemIDs:underParentID:reply:]_block_invoke.588
- __68-[FPXExtensionContext preflightReparentItemIDs:underParentID:reply:]_block_invoke.594
- __69+[NSFileProviderManager _registerNotificationsForProviderIdentifier:]_block_invoke.160
- __69-[FPPendingSetEnumerator enumerateChangesForObserver:fromSyncAnchor:]_block_invoke.488
- __69-[FPPendingSetEnumerator enumerateChangesForObserver:fromSyncAnchor:]_block_invoke_2.491
- __69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.606
- __69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.606.cold.1
- __69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.612
- __69-[FPXExtensionContext fetchPublishingURLForItemID:completionHandler:]_block_invoke.664
- __70-[FPXExtensionContext _deleteIndexInDomainContexts:completionHandler:]_block_invoke.198
- __71-[FPXExtensionContext bulkItemChanges:changedFields:completionHandler:]_block_invoke.331
- __71-[FPXExtensionContext bulkItemChanges:changedFields:completionHandler:]_block_invoke.335
- __71-[FPXExtensionContext valuesForAttributes:forItemID:completionHandler:]_block_invoke.512
- __72-[FPXExtensionContext shouldConnectExternalDomainWithCompletionHandler:]_block_invoke.760
- __73-[FPProviderDomainChangesReceiver updateProviderDomainsWithAttemptCount:]_block_invoke.35
- __74-[FPXExtensionContext sendBlockedProcessNamesUpdateWithCompletionHandler:]_block_invoke.184
- __78-[FPXExtensionContext attemptRecoveryFromError:optionIndex:completionHandler:]_block_invoke.692
- __80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.203
- __80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.203.cold.1
- __80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.203.cold.2
- __80-[FPXPlugInKitExtensionContext initWithInputItems:listenerEndpoint:contextUUID:]_block_invoke.cold.1
- __86-[FPXExtensionContext deleteItemWithID:baseVersion:options:request:completionHandler:]_block_invoke.615
- __87-[FPXExtensionContext fetchServicesForItemID:allowRestrictedSources:completionHandler:]_block_invoke.559
- __87-[FPXExtensionContext fetchServicesForItemID:allowRestrictedSources:completionHandler:]_block_invoke.565
- __90-[FPXExtensionContext removeTrashedItemsOlderThanDate:domainIdentifier:completionHandler:]_block_invoke.235
- __90-[FPXExtensionContext removeTrashedItemsOlderThanDate:domainIdentifier:completionHandler:]_block_invoke.235.cold.1
- __93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.485
- __93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.485.cold.1
- __93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.498
- __93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.498.cold.1
- __93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.502
- __93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.506
- __93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.510
- __93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.510.cold.1
- __93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.511
- __94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.366
- __94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.366.cold.1
- __94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.366.cold.2
- __94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.366.cold.3
- __94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.366.cold.4
- __94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.367
- __95-[FPXExtensionContext fetchAndStartEnumeratingWithSettings:observer:request:completionHandler:]_block_invoke.535
- __95-[FPXExtensionContext fetchAndStartEnumeratingWithSettings:observer:request:completionHandler:]_block_invoke.538
- __97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.426
- __97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.445
- __97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.445.cold.1
- __97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.450
- __97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.454
- __97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.454.cold.1
- __97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.455
- __98-[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:]_block_invoke.145
- __98-[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:]_block_invoke.145.cold.1
- __98-[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:]_block_invoke.145.cold.2
- __98-[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:]_block_invoke.145.cold.3
- __FPCFCopyAttributeValuesForItem_block_invoke.28
- __FPCFCopyAttributeValuesForItem_block_invoke.28.cold.1
- __FPCrossDeviceItemIDForItemID_block_invoke.109
- __FPCrossDeviceItemIDForItemID_block_invoke.116
- __FPCrossDeviceItemIDForItemID_block_invoke.123
- __FPCrossDeviceItemIDForItemID_block_invoke_2.118
- __FPCrossDeviceItemIDForItemID_block_invoke_2.124
- __FPEvictItemAtURL_block_invoke.41
- __FPIsCloudDocsWithFPFSEnabled_block_invoke.cold.1
- __FPItemIDFromCrossDeviceItemID_block_invoke.169
- __FPItemURLForCrossDeviceItemID_block_invoke.137
- __FPItemURLForCrossDeviceItemID_block_invoke.137.cold.1
- __FPItemURLForCrossDeviceItemID_block_invoke.144
- __FPItemURLForCrossDeviceItemID_block_invoke.144.cold.1
- __FPItemURLForCrossDeviceItemID_block_invoke.145
- __FPItemURLForCrossDeviceItemID_block_invoke.160
- __FPRegisterFileProvidersForUserAtURLs_block_invoke.20
- __FPResolveSymlinkRecursive_block_invoke.176
- __FPXExtensionContextPrincipalClass
- __OBJC_$_CLASS_METHODS_FPExtension_subsystem
- __OBJC_$_CLASS_METHODS_FPXPlugInKitExtensionContext
- __OBJC_$_CLASS_METHODS_NSFileProviderManager(MaterializedSet|PendingSet|Import|ImportPrivate|Barrier|Stabilization|Eviction|Attribution|ForceIngestion|Disconnection|TestingModeInteractive|GlobalProgress|NSFileProviderService|Materialize|MaterializePrivate|Diagnostics|KnownFolders)
- __OBJC_$_CLASS_PROP_LIST_FPXPlugInKitExtensionContext
- __OBJC_$_INSTANCE_METHODS_FPExtension_subsystem
- __OBJC_$_INSTANCE_METHODS_FPXPlugInKitExtensionContext
- __OBJC_$_INSTANCE_METHODS_NSFileProviderManager(MaterializedSet|PendingSet|Import|ImportPrivate|Barrier|Stabilization|Eviction|Attribution|ForceIngestion|Disconnection|TestingModeInteractive|GlobalProgress|NSFileProviderService|Materialize|MaterializePrivate|Diagnostics|KnownFolders)
- __OBJC_$_INSTANCE_VARIABLES_FPXPlugInKitExtensionContext
- __OBJC_$_PROP_LIST_FPExtension_subsystem
- __OBJC_$_PROTOCOL_CLASS_METHODS_OPT_PKModularService
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSExtensionRequestHandling
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PKModularService
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSExtensionRequestHandling
- __OBJC_$_PROTOCOL_METHOD_TYPES_PKModularService
- __OBJC_$_PROTOCOL_REFS_NSExtensionRequestHandling
- __OBJC_$_PROTOCOL_REFS_PKModularService
- __OBJC_CLASS_PROTOCOLS_$_FPExtension_subsystem
- __OBJC_CLASS_PROTOCOLS_$_NSFileProviderExtension
- __OBJC_CLASS_RO_$_FPExtension_subsystem
- __OBJC_CLASS_RO_$_FPXPlugInKitExtensionContext
- __OBJC_LABEL_PROTOCOL_$_FPXHost
- __OBJC_LABEL_PROTOCOL_$_NSExtensionRequestHandling
- __OBJC_LABEL_PROTOCOL_$_PKModularService
- __OBJC_METACLASS_RO_$_FPExtension_subsystem
- __OBJC_METACLASS_RO_$_FPXPlugInKitExtensionContext
- __OBJC_PROTOCOL_$_FPXHost
- __OBJC_PROTOCOL_$_NSExtensionRequestHandling
- __OBJC_PROTOCOL_$_PKModularService
- __OBJC_PROTOCOL_REFERENCE_$_FPXHost
- ___37-[FPListRemoteVersionsOperation main]_block_invoke_3
- ___39+[FPExtension_subsystem sharedInstance]_block_invoke
- ___41+[FPTask exec:stdoutString:stderrString:]_block_invoke
- ___47-[FPExtension_subsystem beginUsing:withBundle:]_block_invoke
- ___63+[FPXPlugInKitExtensionContext _extensionAuxiliaryHostProtocol]_block_invoke
- ___63-[FPDaemonConnection makeTopologicallySortedItemsOnDisk:error:]_block_invoke
- ___65+[FPXPlugInKitExtensionContext _extensionAuxiliaryVendorProtocol]_block_invoke
- ___75+[FPProviderDomain selectNewProviderDomain:knownFolders:completionHandler:]_block_invoke
- ___80-[FPXPlugInKitExtensionContext initWithInputItems:listenerEndpoint:contextUUID:]_block_invoke
- ___82-[NSFileProviderManager(Stabilization) waitForStabilizationWithCompletionHandler:]_block_invoke
- ___88-[NSFileProviderManager(Diagnostics) getDiagnosticAttributesForItems:completionHandler:]_block_invoke
- ___88-[NSFileProviderManager(Diagnostics) getDiagnosticAttributesForItems:completionHandler:]_block_invoke_2
- ___FPIsCloudDocsWithFPFSEnabled_block_invoke
- ___FPIsFPCKXPCServiceEnabled_block_invoke
- ___block_descriptor_40_e8_32bs_e34_v24?0"NSError"8"NSDictionary"16l
- ___block_descriptor_40_e8_32bs_e44_v24?0"NSError"8"<FPDWakeupTransaction>"16l
- ___block_descriptor_48_e8_32r40r_e34_v24?0"NSError"8"NSDictionary"16l
- ___block_descriptor_48_e8_32s40bs_e19_v24?0"FPItem"8Q16l
- ___block_descriptor_48_e8_32s_e34_v24?0"NSError"8"NSDictionary"16l
- ___block_descriptor_48_e8_i12?0i8l
- ___block_descriptor_52_e8_32bs_e205_i16?0^{fpfs_fileattrs={fpfs_item_handle=QQII*iI}{fpfs_metadata=ib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1Sq{timespec=qq}{timespec=qq}{timespec=qq}Q{fpfs_tag_data=^vQi}(?=II)QQq*q*^{fpfs_xattr}II*BB*QIii}*Q[0c]}8l
- ___block_descriptor_56_e8_32s40bs48r_e30_v24?0"FPItemID"8"NSError"16l
- ___block_descriptor_56_e8_32s40bs48r_e52_v32?0"FPItem"8"FPExtensionResponse"16"NSError"24l
- ___block_descriptor_56_e8_32s40s48s_e8_v12?0i8l
- ___block_descriptor_56_e8_32s40s_e5_v8?0l
- ___copy_helper_block_8_32b
- ___copy_helper_block_8_32r
- ___destroy_helper_block_8_32b
- ___destroy_helper_block_8_32r
- ___fpfs_evict_legacy_block_invoke.29
- ___fpfs_supports_purge_reasons_block_invoke
- ___getbrc_notify_get_stateSymbolLoc_block_invoke
- ___getbrc_notify_register_checkSymbolLoc_block_invoke
- __block_descriptor_tmp.10
- __block_descriptor_tmp.14
- __block_descriptor_tmp.15
- __block_descriptor_tmp.16
- __block_descriptor_tmp.2
- __block_descriptor_tmp.4
- __block_descriptor_tmp.6
- __block_descriptor_tmp.7
- __block_literal_global.134
- __block_literal_global.140
- __block_literal_global.174
- __block_literal_global.183
- __block_literal_global.222
- __block_literal_global.236
- __block_literal_global.260
- __block_literal_global.294
- __block_literal_global.300
- __block_literal_global.384
- __block_literal_global.393
- __block_literal_global.429
- __block_literal_global.450
- __block_literal_global.456
- __block_literal_global.459
- __block_literal_global.461
- __block_literal_global.484
- __block_literal_global.490
- __block_literal_global.493
- __block_literal_global.535
- __block_literal_global.537
- __block_literal_global.543
- __block_literal_global.568
- __block_literal_global.699
- __block_literal_global.701
- __block_literal_global.739
- __block_literal_global.74
- __block_literal_global.78
- __brc_notify_get_state
- _brc_notify_get_state.cold.1
- _extensionAuxiliaryHostProtocol.interface
- _extensionAuxiliaryHostProtocol.onceToken
- _extensionAuxiliaryVendorProtocol.interface
- _extensionAuxiliaryVendorProtocol.onceToken
- _fmod
- _fpfs_eviction_urgency
- _fpfs_supports_purge_reasons
- _kInPauseResumeEntitlement
- _objc_msgSend$_auxiliaryConnection
- _objc_msgSend$_setRequestCleanUpBlock:
- _objc_msgSend$_startListening:
- _objc_msgSend$beginRequestWithExtensionContext:
- _objc_msgSend$bundleInfoDictionary
- _objc_msgSend$makeTopologicallySortedItemsOnDisk:completionHandler:
- _objc_msgSend$selectNewProviderDomain:knownFolders:completionHandler:
- _objc_msgSend$setPrincipalClass:
- _objc_msgSend$waitForStabilizationOfDomainWithID:completionHandler:
- beginUsing:withBundle:.onceToken
- fpfs_evict.cold.6
- fpfs_supports_purge_reasons.feature_enabled
- fpfs_supports_purge_reasons.once_token
- getbrc_notify_get_stateSymbolLoc.ptr
- getbrc_notify_register_checkSymbolLoc.ptr
- sharedInstance.__instance
CStrings:
+ "+[FPXExtensionContext principalClass]_block_invoke"
+ ".domainscache.plist"
+ "/.nofollow/"
+ "/.nofollow/%s"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/FPXDomainContext.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/FPXEnumerator.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/FPXExtensionContext.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/FPXFakeDefaultDomainExtension.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FileProvider/fileproviderd/action operation engine/FPActionOperationLocator.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/FPDaemonConnection.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/FPItem.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/FPTestingOperations.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/FPXPCSanitizer.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/NSFileProviderManager.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/NSURL+FPAdditions.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/NSXPCConnection+FPAdditions.m"
+ "2882.101.2"
+ "B16@?0r*8"
+ "B48@0:8@16^@24^@32^@40"
+ "Can't tell sandbox to register sync root change: %{errno}d"
+ "DLV2"
+ "FPRepeatDonation"
+ "FPTaskErrorDomain"
+ "Failed to spawn task"
+ "NSFileProviderUserInfoExperimentID"
+ "PreventUnindexOnEviction"
+ "PrivateDiagnostics"
+ "SIMULATOR_ROOT"
+ "Spotlight"
+ "T@\"FPXExtensionContext\",W,N,V_extensionContext"
+ "TB,N,V_isEvictedWithClone"
+ "TB,N,V_isOnMainVolume"
+ "Task finished with exit code %d"
+ "Task terminated due to signal %d"
+ "Vendor extension instance returned neither an item nor an error during trash operation of item %@"
+ "[DEBUG] Process is allowed to read domains cache"
+ "[DEBUG] Spawning FPTask with command '%@'"
+ "[DEBUG] ┳%llx continuing on %s at QoS %d"
+ "[ERROR] Failed getting sandbox extension: %d (handle: %lld)"
+ "[ERROR] Failed querying shared cache"
+ "[ERROR] Failed querying shared cache: %s"
+ "[ERROR] Failed reading domains cache: %{public}@"
+ "[ERROR] Failed to create container query"
+ "[ERROR] Failed unarchiving domains cache: %{public}@"
+ "[ERROR] failed to enable long paths i/o policy: %s"
+ "[ERROR] failed to get long paths i/o policy: %s"
+ "[ERROR] failed to list version from the provider with error: %@"
+ "[ERROR] failed to restore long paths i/o policy to %d: %s"
+ "[ERROR] waitpid() failed with errno %d, %s"
+ "[INFO] command terminated due to signal %d"
+ "[WARNING] Process is not allowed to read domains cache"
+ "_FPPerformWithPersona"
+ "_dontLoadCacheFromDisk"
+ "_ignoreUpdateNotifications"
+ "_isEvictedWithClone"
+ "_isOnMainVolume"
+ "_markItemsForUpdate:index:completionHandler:"
+ "_t_forceReadCacheFromDisk"
+ "_t_ignoreUpdateNotifications:"
+ "_t_loadCacheOnHandlerAdding:"
+ "_test_purgerBarrierWithCompletionHandler:"
+ "_test_triggerDatabaseError:domain:completionHandler:"
+ "allowedToReadCacheFromDisk"
+ "appGroup"
+ "checkErrorAgainstDiagnosticsJson:inputError:errorDirection:jobCode:completionHandler:"
+ "clearDiagnosticsState:completionHandler:"
+ "com.apple.fileprovider.log-sensitive-data-update-interval"
+ "com.apple.private.MobileContainerManager.lookup"
+ "dataWithContentsOfFile:options:error:"
+ "environment"
+ "exec:error:"
+ "exec:stdoutString:stderrString:error:"
+ "failed to remove content dpendent xattrs during eviction [%s]"
+ "failed to remove content dpendent xattrs during materialization [%s]"
+ "fpfs_metadata.m"
+ "group.com.apple.FileProvider.DomainCaching"
+ "i16@?0^{fpfs_fileattrs={fpfs_item_handle=QQII*iI}{fpfs_metadata=ib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1Sq{timespec=qq}{timespec=qq}{timespec=qq}Q{fpfs_tag_data=^vQi}(?=II)QQq*q*^{fpfs_xattr}II*BB*QICii}*Q[0c]}8"
+ "ignoreUpdateNotifications"
+ "isEvictedWithClone"
+ "isOnMainVolume"
+ "kMDItemFileItemID"
+ "newPreparedArgvArray"
+ "processInfo"
+ "r^*16@0:8"
+ "readCacheFromDisk:"
+ "requestDiagnosticCollectionForItemWithIdentifier:errorReason:completionHandler:"
+ "selectNewProviderDomain:knownFolders:skipReleasePrompt:completionHandler:"
+ "setExtensionContext:"
+ "setIsEvictedWithClone:"
+ "setIsOnMainVolume:"
+ "sim_mkdirAt:path:permissions:completionHandler:"
+ "sim_openAt:path:flags:permissions:completionHandler:"
+ "sim_openByID:device:oflag:completionHandler:"
+ "sim_renameAt:from:tofd:to:flags:completionHandler:"
+ "sim_requestProtocolVersion:completionHandler:"
+ "sim_unlinkAt:path:flag:recursive:completionHandler:"
+ "simulatorRoot"
+ "slowFetchAttributes:protectionClass:bundleID:identifiers:completionHandler:"
+ "stderr"
+ "stdout"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
+ "v24@?0@\"<FPDWakeupTransaction>\"8@\"NSError\"16"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"<FPDWakeupTransaction>\"@\"NSError\">24"
+ "v32@0:8Q16@?<v@?@\"NSError\">24"
+ "v32@0:8Q16@?<v@?Q@\"NSError\">24"
+ "v40@0:8@\"NSError\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSError\"24@?<v@?@\"NSError\">32"
+ "v40@0:8Q16i24i28@?32"
+ "v40@0:8Q16i24i28@?<v@?@\"NSFileHandle\"@\"NSError\">32"
+ "v44@0:8@\"NSString\"16Q24B32@?<v@?@\"NSError\">36"
+ "v48@0:8@\"NSFileHandle\"16@\"NSString\"24q32@?<v@?@\"NSError\">40"
+ "v52@0:8@\"NSFileHandle\"16@\"NSString\"24q32B40@?<v@?@\"NSError\">44"
+ "v52@0:8@16@24q32B40@?44"
+ "v56@0:8@\"NSFileHandle\"16@\"NSString\"24q32q40@?<v@?@\"NSFileHandle\"@\"NSError\">48"
+ "v56@0:8@\"NSString\"16@\"NSError\"24@\"NSNumber\"32@\"NSNumber\"40@?<v@?@\"NSString\"@\"NSError\">48"
+ "v56@0:8@16@24q32q40@?48"
+ "v64@0:8@\"NSFileHandle\"16@\"NSString\"24@\"NSFileHandle\"32@\"NSString\"40q48@?<v@?@\"NSError\">56"
+ "v64@0:8@16@24@32@40q48@?56"
+ "validateDiagnosticsJson:completionHandler:"
+ "waitForStabilizationOfDomainWithID:mode:completionHandler:"
+ "waitForStabilizationWithMode:completionHandler:"
+ "wakeUpForURLFixed:completionHandler:"
- "&"
- "+[FPXExtensionContext principalClass]"
- ".~"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/FPXDomainContext.m"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/FPXEnumerator.m"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/FPXExtensionContext.m"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/FPXFakeDefaultDomainExtension.m"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/FileProvider/fileproviderd/action operation engine/FPActionOperationLocator.m"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/FPDaemonConnection.m"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/FPItem.m"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/FPTestingOperations.m"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/FPXPCSanitizer.m"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/NSFileProviderManager.m"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/NSURL+FPAdditions.m"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/NSXPCConnection+FPAdditions.m"
- "2732.81.1"
- "@\"<PKModularService>\"16@0:8"
- "@\"<PKModularService>\"24@0:8@\"NSDictionary\"16"
- "APFSIOC_PURGE_SINGLE_FILE did not evict anything, assuming EBUSY"
- "Can't tell sandbox to register sync root change: %s"
- "D"
- "FPCKService"
- "FPExtension_subsystem"
- "FPExtension_subsystem.m"
- "FPPurgeReasonsSupport"
- "FPXHost"
- "FPXPlugInKitExtensionContext"
- "G"
- "Helena"
- "N"
- "NSExtensionPrincipalClass %@ could not be resolved to class!"
- "NSExtensionRequestHandling"
- "PKModularService"
- "Pinning"
- "R"
- "S"
- "T"
- "T#,&,N"
- "Unable to make empty file dataless: %{errno}d"
- "V"
- "W"
- "Z"
- "[DEBUG] Cleanup of extension context requested, but already deallocated"
- "[DEBUG] Do not migrate to FPFS user default is configured."
- "_auxiliaryConnection"
- "_extensionAuxiliaryHostProtocol"
- "_extensionAuxiliaryVendorProtocol"
- "_initializedByViewServices"
- "_setRequestCleanUpBlock:"
- "_setTransaction:"
- "_startListening:"
- "beginRequestWithExtensionContext:"
- "beginUsing:withBundle:"
- "brc_notify_get_state"
- "brc_notify_register_check"
- "bundleInfoDictionary"
- "com.apple.fileprovider.pause-resume"
- "com.apple.fileproviderd.FPCKService"
- "communicationsFailed:"
- "endUsing:"
- "exec:stdoutString:stderrString:"
- "extension context is of an invalid type of class (expected: %@, actual: %@)"
- "f"
- "fpfs_metadata.c"
- "gz"
- "i16@?0^{fpfs_fileattrs={fpfs_item_handle=QQII*iI}{fpfs_metadata=ib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1Sq{timespec=qq}{timespec=qq}{timespec=qq}Q{fpfs_tag_data=^vQi}(?=II)QQq*q*^{fpfs_xattr}II*BB*QIii}*Q[0c]}8"
- "initForPlugInKit"
- "initForPlugInKitWithOptions:"
- "initWithInputItems:listenerEndpoint:contextUUID:"
- "int _brc_notify_register_check(const char *, int *)"
- "makeTopologicallySortedItemsOnDisk:completionHandler:"
- "makeTopologicallySortedItemsOnDisk:error:"
- "setPrincipalClass:"
- "v24@0:8@\"<PKSubsystemServicePersonality>\"16"
- "v24@0:8@\"NSExtensionContext\"16"
- "v24@0:8@?<v@?@\"NSError\"@\"NSDictionary\">16"
- "v24@?0@\"NSError\"8@\"<FPDWakeupTransaction>\"16"
- "v24@?0@\"NSError\"8@\"NSDictionary\"16"
- "v32@0:8@\"<PKSubsystemServicePersonality>\"16@\"NSBundle\"24"
- "void _brc_notify_get_state(int, uint64_t *, const char *)"
- "xz"
- "~$"

```
