## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/FileProvider`

```diff

-1703.80.16.0.0
-  __TEXT.__text: 0x11b274
-  __TEXT.__auth_stubs: 0x19d0
-  __TEXT.__objc_methlist: 0xb840
-  __TEXT.__const: 0x3b0
-  __TEXT.__gcc_except_tab: 0x778c
-  __TEXT.__cstring: 0x13247
-  __TEXT.__oslogstring: 0xc8cc
+1835.102.2.0.0
+  __TEXT.__text: 0x11de14
+  __TEXT.__auth_stubs: 0x19f0
+  __TEXT.__objc_methlist: 0xba38
+  __TEXT.__const: 0x3a0
+  __TEXT.__gcc_except_tab: 0x7270
+  __TEXT.__cstring: 0x13104
+  __TEXT.__oslogstring: 0xd05d
   __TEXT.__dlopen_cstrs: 0x7ed
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x4e7c
-  __TEXT.__objc_classname: 0x1e1e
-  __TEXT.__objc_methname: 0x20af6
-  __TEXT.__objc_methtype: 0x5bae
-  __TEXT.__objc_stubs: 0x129a0
-  __DATA_CONST.__got: 0x4b0
-  __DATA_CONST.__const: 0x5c78
-  __DATA_CONST.__objc_classlist: 0x638
-  __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x278
+  __TEXT.__unwind_info: 0x4e80
+  __TEXT.__objc_classname: 0x1e49
+  __TEXT.__objc_methname: 0x21560
+  __TEXT.__objc_methtype: 0x5db7
+  __TEXT.__objc_stubs: 0x12e40
+  __DATA_CONST.__got: 0x4b8
+  __DATA_CONST.__const: 0x5e68
+  __DATA_CONST.__objc_classlist: 0x640
+  __DATA_CONST.__objc_catlist: 0x88
+  __DATA_CONST.__objc_protolist: 0x280
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1fdd0
-  __DATA_CONST.__objc_selrefs: 0x6318
-  __DATA_CONST.__objc_arraydata: 0xa98
-  __AUTH_CONST.__objc_const: 0x5590
-  __AUTH_CONST.__cfstring: 0xfa60
-  __AUTH_CONST.__const: 0x1920
-  __AUTH_CONST.__objc_arrayobj: 0x168
+  __DATA_CONST.__objc_const: 0x20478
+  __DATA_CONST.__objc_selrefs: 0x64a0
+  __DATA_CONST.__objc_protorefs: 0x128
+  __DATA_CONST.__objc_classrefs: 0x798
+  __DATA_CONST.__objc_superrefs: 0x500
+  __DATA_CONST.__objc_arraydata: 0xa90
+  __AUTH_CONST.__objc_const: 0x5660
+  __AUTH_CONST.__cfstring: 0xfca0
+  __AUTH_CONST.__const: 0x1960
   __AUTH_CONST.__auth_ptr: 0x30
   __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH_CONST.__auth_got: 0xcf8
-  __AUTH.__objc_data: 0x190
+  __AUTH_CONST.__objc_arrayobj: 0x150
+  __AUTH_CONST.__auth_got: 0xd08
+  __AUTH.__objc_data: 0x1e0
   __AUTH.__data: 0x10
-  __DATA.__objc_protorefs: 0x128
-  __DATA.__objc_classrefs: 0x788
-  __DATA.__objc_superrefs: 0x4f8
-  __DATA.__objc_ivar: 0xf30
-  __DATA.__data: 0x21c8
-  __DATA.__bss: 0x300
+  __DATA.__objc_ivar: 0xf40
+  __DATA.__data: 0x2240
+  __DATA.__bss: 0x308
   __DATA_DIRTY.__objc_data: 0x3ca0
   __DATA_DIRTY.__data: 0x2c0
-  __DATA_DIRTY.__bss: 0x3d0
+  __DATA_DIRTY.__bss: 0x3d8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6816
-  Symbols:   21636
-  CStrings:  9408
+  Functions: 6798
+  Symbols:   21656
+  CStrings:  9533
 
Symbols:
+ +[FPDaemonConnection runningInSyncBubble]
+ +[FPProviderDomain _generateDomainIDFromDSID:]
+ +[FPProviderDomain _generateDomainIDFromDSID:].cold.1
+ +[FPProviderDomain _generateDomainIDFromDSID:].cold.2
+ +[FPProviderDomain cachedProviderDomainWithID:cachePolicy:error:]
+ +[FPProviderDomain fetchProviderDomainForItem:cachePolicy:completionHandler:]
+ +[FPProviderDomain mainICloudDriveDomainID]
+ +[FPProviderDomain projectedFPFSMainICloudDriveDomainID]
+ +[FPProviderDomain providerDomainForItem:cachePolicy:error:]
+ +[FPProviderDomain providerDomainWithID:cachePolicy:completionHandler:]
+ +[FPProviderDomain providerDomainWithID:cachePolicy:error:]
+ +[FPProviderDomain rootURLForProviderDomainID:cachePolicy:error:]
+ +[FPReachabilityMonitor getReachabilityFlagsByCheckingNetwork]
+ +[FPXPCLogDelegate setupWithLog:forConnection:]
+ +[NSFileProviderManager addDomain:forProviderIdentifier:byImportingDirectoryAtURL:userAllowedDBDrop:knownFolders:completionHandler:]
+ +[NSFileProviderManager addDomain:forProviderIdentifier:byImportingDirectoryAtURL:userAllowedDBDrop:knownFolders:synchronous:completionHandler:]
+ +[NSFileProviderManager addDomain:userAllowedDBDrop:completionHandler:]
+ +[NSFileProviderManager checkLocationEligibilityForDomain:unsupportedReason:error:]
+ +[NSURL(FPAdditions) fp_backupManifestDirectory]
+ +[NSURL(FPAdditions) fp_lmdURL]
+ -[FPDaemonConnection restoreUserURL:cleanupOnSuccess:completionHandler:]
+ -[FPDaemonConnection runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:completionHandler:]
+ -[FPExtensionCollection updateRootItem:].cold.2
+ -[FPExtensionCollection updateRootItem:].cold.3
+ -[FPExtensionEnumerationSettings enumeratedURL]
+ -[FPExtensionEnumerationSettings nullableEnumeratedItemID]
+ -[FPExtensionEnumerationSettings setEnumeratedURL:]
+ -[FPExtensionEnumerationSettings setNullableEnumeratedItemID:]
+ -[FPItem _evaluateTypes:]
+ -[FPItem itemIsSupportedSearchScopeWithCachePolicy:completionHandler:]
+ -[FPItemManager _fetchURLForItemID:creatingPlaceholderIfMissing:completionHandlerWithInfo:]
+ -[FPItemManager appLibraryCollectionForProviderDomainID:]
+ -[FPItemManager eligibleActionsForItems:domainCachePolicy:]
+ -[FPItemManager eligibleActionsForItems:domainCachePolicy:].cold.1
+ -[FPItemManager newCollectionWithItemAtURL:error:]
+ -[FPItemManager newCollectionWithItemAtURL:skipValidation:error:]
+ -[FPProviderDomain reconnectAndReimportDomainWithCompletionHandler:]
+ -[FPProviderDomain setStorageURLsAreInTransientState:]
+ -[FPProviderDomain storageURLsAreInTransientState]
+ -[FPXConnectionHandler init]
+ -[FPXConnectionHandler invalidateCurrentContext:]
+ -[FPXExtensionContext bulkEvictItemsWithItemIDs:completionHandler:].cold.1
+ -[FPXExtensionContext deleteItemWithID:baseVersion:options:request:completionHandler:].cold.1
+ -[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:].cold.1
+ -[FPXExtensionContext deleteSearchableItemsWithSpotlightDomainIdentifiers:domainIdentifier:completionHandler:].cold.2
+ -[FPXExtensionContext didChangeItemID:completionHandler:].cold.1
+ -[FPXExtensionContext disconnectDomainID:options:completionHandler:].cold.1
+ -[FPXExtensionContext evictItemAtURL:completionHandler:].cold.1
+ -[FPXExtensionContext fetchHierarchyForItemID:recursively:ignoreAlternateContentURL:reply:]
+ -[FPXExtensionContext fetchItemID:reply:].cold.1
+ -[FPXExtensionContext fetchPublishingURLForItemID:completionHandler:].cold.1
+ -[FPXExtensionContext fetchServicesForItemID:allowRestrictedSources:completionHandler:].cold.1
+ -[FPXExtensionContext identifierForItemAtURL:completionHandler:].cold.1
+ -[FPXExtensionContext itemChangedAtURL:completionHandler:].cold.1
+ -[FPXExtensionContext itemForItemID:request:completionHandler:].cold.1
+ -[FPXExtensionContext itemForURL:completionHandler:].cold.2
+ -[FPXExtensionContext listRemoteVersionsWithSettings:observer:request:completionHandler:].cold.1
+ -[FPXExtensionContext removeTrashedItemsOlderThanDate:domainIdentifier:completionHandler:].cold.1
+ -[FPXExtensionContext wakeForSessionIdentifier:completionHandler:].cold.1
+ -[FPXPCLogDelegate .cxx_destruct]
+ -[FPXPCLogDelegate connection:handleInvocation:isReply:]
+ -[NSFileProviderDomain initWithDisplayName:userInfo:volumeURL:]
+ -[NSFileProviderDomain initWithIdentifier:displayName:userInfo:volumeURL:]
+ -[NSFileProviderDomain initWithIdentifier:displayName:userInfo:volumeURL:pathRelativeToDocumentStorage:hidden:replicated:]
+ -[NSFileProviderManager addDomain:userAllowedDBDrop:completionHandler:]
+ -[NSFileProviderManager stateDirectoryURLWithError:]
+ -[NSURL(FPAdditions) fp_fpfsProviderDomainID:]
+ -[NSURL(FPAdditions) fp_fpfsProviderDomainID:error:]
+ -[NSURL(FPAdditions) fp_uniqueTempFolderWithError:]
+ -[NSURL(FPAdditions) fp_volumeUUID].cold.1
+ -[NSUUID(FPAddtions) fp_UUIDWithObfuscation:]
+ -[NSUUID(FPAddtions) fp_UUID]
+ -[NSXPCConnection(FPAdditions) fp_annotateInvocation:withLogSection:]
+ -[NSXPCConnection(FPAdditions) fp_annotateInvocation:withLogSection:].cold.1
+ -[NSXPCConnection(FPAdditions) fp_userInfo]
+ -[NSXPCConnection(FPAdditions) fp_userInfo].cold.1
+ -[NSXPCConnection(FPXPCSanitizer) fp_annotateWithXPCSanitizer:]
+ GCC_except_table102
+ GCC_except_table104
+ GCC_except_table80
+ _ACAccountTypeIdentifierAppleAccount
+ _APFSVolumeGetVEKState
+ _FPDiagnosticAttributeKeyDBFPUnappliedFields
+ _FPDiagnosticAttributeKeyDBFSUnappliedFields
+ _FPDomainUnavailableErrorWithUnderlyingError
+ _FPExecutableNameForProcessIdentifier.onceToken
+ _FPExecutableNameForProcessIdentifier.pidResolutionAllowed
+ _FPFileIsAlreadyPausedError
+ _FPFileNotPausedError
+ _FPIsFPCKXPCServiceEnabled
+ _FPIsFPCKXPCServiceEnabled.featureEnabledByDefault
+ _FPIsFPCKXPCServiceEnabled.onceToken
+ _FPPauseSyncForFileAtURLWithBehavior
+ _FPPopLogSectionForBlock
+ _FPResumeSyncForFileAtURLWithBehavior
+ _FPVolumeFPFSSupported
+ _NSFileProviderErrorCategoryKey
+ _NSFileProviderErrorPostponeUpload
+ _OBJC_CLASS_$_FPXPCLogDelegate
+ _OBJC_CLASS_$_NSFileVersion
+ _OBJC_IVAR_$_FPExtensionEnumerationSettings._enumeratedURL
+ _OBJC_IVAR_$_FPProviderDomain._storageURLsAreInTransientState
+ _OBJC_IVAR_$_FPXConnectionHandler._activeConnections
+ _OBJC_IVAR_$_FPXPCLogDelegate._log
+ _OBJC_METACLASS_$_FPXPCLogDelegate
+ _SCNetworkReachabilityCreateWithAddress
+ _SCNetworkReachabilityGetFlags
+ __OBJC_$_CATEGORY_NSUUID_$_FPAddtions
+ __OBJC_$_CATEGORY_NSXPCConnection_$_FPXPCSanitizer
+ __OBJC_$_CLASS_METHODS_FPXPCLogDelegate
+ __OBJC_$_CLASS_METHODS_NSFileProviderManager(MaterializedSet|PendingSet|Import|ImportPrivate|Barrier|Stabilization|Eviction|Attribution|ForceIngestion|Disconnection|TestingModeInteractive|GlobalProgress|NSFileProviderService|Materialize|MaterializePrivate|Diagnostics)
+ __OBJC_$_INSTANCE_METHODS_FPXPCLogDelegate
+ __OBJC_$_INSTANCE_METHODS_NSFileProviderManager(MaterializedSet|PendingSet|Import|ImportPrivate|Barrier|Stabilization|Eviction|Attribution|ForceIngestion|Disconnection|TestingModeInteractive|GlobalProgress|NSFileProviderService|Materialize|MaterializePrivate|Diagnostics)
+ __OBJC_$_INSTANCE_METHODS_NSUUID(FPAddtions)
+ __OBJC_$_INSTANCE_METHODS_NSXPCConnection(FPXPCSanitizer|Sanitization|FPAdditions)
+ __OBJC_$_INSTANCE_VARIABLES_FPXPCLogDelegate
+ __OBJC_$_PROP_LIST_FPXPCLogDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCConnectionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCConnectionDelegate
+ __OBJC_$_PROTOCOL_REFS_NSXPCConnectionDelegate
+ __OBJC_CLASS_PROTOCOLS_$_FPXPCLogDelegate
+ __OBJC_CLASS_RO_$_FPXPCLogDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSXPCConnectionDelegate
+ __OBJC_METACLASS_RO_$_FPXPCLogDelegate
+ __OBJC_PROTOCOL_$_NSXPCConnectionDelegate
+ ___101-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:reply:]_block_invoke.526
+ ___101-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:reply:]_block_invoke_2.530
+ ___103-[FPXExtensionContext modifyItem:baseVersion:changedFields:contents:options:request:completionHandler:]_block_invoke.277
+ ___107-[NSFileProviderExtension(CreateItem) createItemBasedOnTemplate:fields:contents:options:completionHandler:]_block_invoke.341
+ ___107-[NSFileProviderExtension(CreateItem) createItemBasedOnTemplate:fields:contents:options:completionHandler:]_block_invoke.348
+ ___110-[FPXExtensionContext URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.325
+ ___110-[FPXExtensionContext URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.325.cold.1
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.513
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.513.cold.1
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.513.cold.2
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.513.cold.3
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.513.cold.4
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.513.cold.5
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.513.cold.6
+ ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.517
+ ___137-[FPXExtensionContext fetchContentsForItemWithID:version:request:estimatedItemSize:isSymlink:extent:alignment:options:completionHandler:]_block_invoke.253
+ ___137-[FPXExtensionContext fetchContentsForItemWithID:version:request:estimatedItemSize:isSymlink:extent:alignment:options:completionHandler:]_block_invoke_2.261
+ ___144+[NSFileProviderManager addDomain:forProviderIdentifier:byImportingDirectoryAtURL:userAllowedDBDrop:knownFolders:synchronous:completionHandler:]_block_invoke
+ ___155-[FPXExtensionContext fetchContentsForItemWithID:version:usingExistingContentsAtURL:existingVersion:request:estimatedItemSize:isSymlink:completionHandler:]_block_invoke.270
+ ___155-[FPXExtensionContext fetchContentsForItemWithID:version:usingExistingContentsAtURL:existingVersion:request:estimatedItemSize:isSymlink:completionHandler:]_block_invoke.271
+ ___34-[FPItemCollection startObserving]_block_invoke.135.cold.1
+ ___34-[FPItemCollection startObserving]_block_invoke.136
+ ___40-[FPItemCollection _flushPendingUpdates]_block_invoke.187
+ ___40-[FPItemCollection _flushPendingUpdates]_block_invoke.187.cold.1
+ ___41+[FPDaemonConnection runningInSyncBubble]_block_invoke
+ ___43+[FPItemCollection resumeVendorEnumeration]_block_invoke.220
+ ___44-[FPItemCollection sendIndexPathBasedDiffs:]_block_invoke.207
+ ___44-[FPItemCollection sendIndexPathBasedDiffs:]_block_invoke.207.cold.1
+ ___47-[FPXConnectionHandler shouldAcceptConnection:]_block_invoke.2
+ ___47-[FPXConnectionHandler shouldAcceptConnection:]_block_invoke.2.cold.1
+ ___49-[FPXEnumerator currentSyncAnchorWithCompletion:]_block_invoke.175
+ ___50-[NSFileProviderManager _signalPendingEnumerators]_block_invoke.169
+ ___52-[FPXExtensionContext itemForURL:completionHandler:]_block_invoke.320
+ ___52-[NSFileProviderManager stateDirectoryURLWithError:]_block_invoke
+ ___52-[NSFileProviderManager stateDirectoryURLWithError:]_block_invoke_2
+ ___52-[NSFileProviderManager stateDirectoryURLWithError:]_block_invoke_2.cold.1
+ ___55-[FPExtensionCollection _startMonitoringDSCopyProgress]_block_invoke.33
+ ___55-[FPExtensionCollection _startMonitoringDSCopyProgress]_block_invoke.35
+ ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.329
+ ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.333
+ ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.334
+ ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.334.cold.1
+ ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.335
+ ___59+[FPProviderDomain providerDomainWithID:cachePolicy:error:]_block_invoke
+ ___63-[FPXExtensionContext preflightTrashItemIDs:completionHandler:]_block_invoke.301
+ ___64-[FPXEnumerator enumerateItemsFromPage:suggestedPageSize:reply:]_block_invoke.178
+ ___64-[FPXEnumerator enumerateItemsFromPage:suggestedPageSize:reply:]_block_invoke.178.cold.1
+ ___64-[FPXEnumerator enumerateItemsFromPage:suggestedPageSize:reply:]_block_invoke.186
+ ___65-[FPXExtensionContext providePlaceholderAtURL:completionHandler:]_block_invoke.307
+ ___65-[FPXExtensionContext waitForStabilizationWithCompletionHandler:]_block_invoke.599
+ ___66+[FPItemToURLResourcesConverter dictionaryFromItem:requestedKeys:]_block_invoke.361
+ ___66-[FPXExtensionContext fetchTrashIdentifiersWithCompletionHandler:]_block_invoke.586
+ ___66-[FPXExtensionContext wakeForSessionIdentifier:completionHandler:]_block_invoke.546
+ ___66-[FPXExtensionContext wakeForSessionIdentifier:completionHandler:]_block_invoke.546.cold.1
+ ___67-[FPPendingSetEnumerator enumerateItemsForObserver:startingAtPage:]_block_invoke.436
+ ___67-[FPXExtensionContext bulkEvictItemsWithItemIDs:completionHandler:]_block_invoke.549
+ ___68-[FPProviderDomain reconnectAndReimportDomainWithCompletionHandler:]_block_invoke
+ ___68-[FPXEnumerator enumerateChangesFromToken:suggestedBatchSize:reply:]_block_invoke.192
+ ___68-[FPXExtensionContext preflightReparentItemIDs:underParentID:reply:]_block_invoke.482
+ ___69-[FPPendingSetEnumerator enumerateChangesForObserver:fromSyncAnchor:]_block_invoke.440
+ ___69-[FPPendingSetEnumerator enumerateChangesForObserver:fromSyncAnchor:]_block_invoke_2.443
+ ___69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.501
+ ___69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.501.cold.1
+ ___69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.507
+ ___69-[NSXPCConnection(FPAdditions) fp_annotateInvocation:withLogSection:]_block_invoke
+ ___70-[FPItem itemIsSupportedSearchScopeWithCachePolicy:completionHandler:]_block_invoke
+ ___78-[FPXExtensionContext attemptRecoveryFromError:optionIndex:completionHandler:]_block_invoke.552
+ ___80-[FPXExtensionContext fetchAlternateContentsURLWrapperForURL:completionHandler:]_block_invoke.cold.1
+ ___80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.191
+ ___80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.191.cold.1
+ ___80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.191.cold.2
+ ___83+[NSFileProviderManager checkLocationEligibilityForDomain:unsupportedReason:error:]_block_invoke
+ ___87-[FPXExtensionContext fetchServicesForItemID:allowRestrictedSources:completionHandler:]_block_invoke.465
+ ___91-[FPItemManager _fetchURLForItemID:creatingPlaceholderIfMissing:completionHandlerWithInfo:]_block_invoke
+ ___91-[FPXExtensionContext fetchHierarchyForItemID:recursively:ignoreAlternateContentURL:reply:]_block_invoke
+ ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.397
+ ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.397.cold.1
+ ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.410.cold.1
+ ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.412
+ ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.415
+ ___94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.309
+ ___95-[FPXExtensionContext fetchAndStartEnumeratingWithSettings:observer:request:completionHandler:]_block_invoke.441
+ ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.347
+ ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.366
+ ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.366.cold.1
+ ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.371
+ ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke_2.370
+ ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke_2.370.cold.1
+ ___98-[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:]_block_invoke.140
+ ___98-[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:]_block_invoke.140.cold.1
+ ___98-[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:]_block_invoke.140.cold.2
+ ___FILEPROVIDER_BAD_ITEM_MISSING_CONTENTTYPE__
+ ___FILEPROVIDER_BAD_ITEM_MISSING_FILENAME__
+ ___FILEPROVIDER_BAD_ITEM_MISSING_IDENTIFIER__
+ ___FILEPROVIDER_BAD_ITEM_MISSING_ITEMVERSION__
+ ___FILEPROVIDER_BAD_ITEM_MISSING_PROVIDER__
+ ___FPCrossDeviceItemIDForItemID_block_invoke.71
+ ___FPExecutableNameForProcessIdentifier_block_invoke
+ ___FPFetchLatestVersionForFileAtURL_block_invoke.cold.1
+ ___FPFetchLatestVersionForFileAtURL_block_invoke.cold.2
+ ___FPFetchLatestVersionForFileAtURL_block_invoke.cold.3
+ ___FPIsFPCKXPCServiceEnabled_block_invoke
+ ___FPItemIDFromCrossDeviceItemID_block_invoke.97
+ ___FPItemURLForCrossDeviceItemID_block_invoke.79
+ ___FPItemURLForCrossDeviceItemID_block_invoke.79.cold.1
+ ___FPItemURLForCrossDeviceItemID_block_invoke.84
+ ___FPItemURLForCrossDeviceItemID_block_invoke.84.cold.1
+ ___FPItemURLForCrossDeviceItemID_block_invoke.85
+ ___FPPauseSyncForFileAtURLWithBehavior_block_invoke
+ ___FPResumeSyncForFileAtURLWithBehavior_block_invoke
+ ___block_descriptor_40_e8_32bs_e30_v24?0"NSString"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e30_v28?0"NSURL"8B16"NSError"20ls32l8
+ ___block_descriptor_48_e8_32bs40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32bs_e204_i16?0^{fpfs_fileattrs={fpfs_item_handle=QQII*iI}{fpfs_metadata=ib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1Sq{timespec=qq}{timespec=qq}{timespec=qq}Q{fpfs_tag_data=^vQi}(?=II)QQq*q*^{fpfs_xattr}II*BB*Qii}*Q[0c]}8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e30_v28?0"NSURL"8B16"NSError"20ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e57_v32?0"NSString"8"FPSandboxingURLWrapper"16"NSError"24ls40l8s32l8
+ ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_56_e8_32r40r48r_e23_v28?0B8Q12"NSError"20lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40bs48r_e27_v24?0"NSURL"8"NSError"16ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e44_v24?0"FPSandboxingURLWrapper"8"NSError"16ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40s48bs_e30_v24?0"FPItemID"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e42_v24?0"<NSFileProviderItem>"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e5_v8?0ls32l8r48l8s40l8r56l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e5_v8?0ls32l8s40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40bs48r_e22_v16?0"NSInvocation"8ls32l8r48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s40l8s56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs_e75_v48?0"NSArray"8"NSData"16"NSData"24"FPExtensionResponse"32"NSError"40ls32l8s48l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e42_v24?0"<NSFileProviderItem>"8"NSError"16ls32l8s64l8s40l8s48l8s56l8
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e29_v24?0"NSArray"8"NSError"16ls32l8s64l8s40l8s48l8s56l8
+ ___block_literal_global.110
+ ___block_literal_global.144
+ ___block_literal_global.152
+ ___block_literal_global.157
+ ___block_literal_global.172
+ ___block_literal_global.174
+ ___block_literal_global.183
+ ___block_literal_global.202
+ ___block_literal_global.203
+ ___block_literal_global.216
+ ___block_literal_global.224
+ ___block_literal_global.228
+ ___block_literal_global.233
+ ___block_literal_global.252
+ ___block_literal_global.258
+ ___block_literal_global.264
+ ___block_literal_global.276
+ ___block_literal_global.279
+ ___block_literal_global.282
+ ___block_literal_global.316
+ ___block_literal_global.326
+ ___block_literal_global.334
+ ___block_literal_global.350
+ ___block_literal_global.359
+ ___block_literal_global.366
+ ___block_literal_global.409
+ ___block_literal_global.41
+ ___block_literal_global.415
+ ___block_literal_global.417
+ ___block_literal_global.427
+ ___block_literal_global.433
+ ___block_literal_global.444
+ ___block_literal_global.445
+ ___block_literal_global.468
+ ___block_literal_global.506
+ ___block_literal_global.519
+ ___block_literal_global.57
+ ___block_literal_global.597
+ ___block_literal_global.627
+ ___block_literal_global.73
+ ___block_literal_global.76
+ ___block_literal_global.82
+ __allowEbihilDiskImages
+ __unnamed_array_storage.285
+ _cachedDirectoriesWithSecurityScope
+ _fpfs_eviction_urgency
+ _fpfs_fset_pause_sync_bundleID
+ _fpfs_fset_resuming_sync_with_drop_local_changes
+ _fpfs_funset_pause_sync_bundleID
+ _fpfs_funset_resuming_sync_with_drop_local_changes
+ _fpfs_get_dirstat
+ _fpfs_get_is_sync_paused
+ _fpfs_get_is_sync_resuming_with_drop_local_changes
+ _fpfs_get_purgeable_info
+ _fpfs_get_purgeable_info.cold.1
+ _fpfs_set_evictable.cold.1
+ _fpfs_set_purgeable_non_evictable
+ _fpfs_setup_log_for_invocation
+ _fpfs_t_is_evictable
+ _kFileProviderLogSectionKey
+ _kInPauseResumeEntitlement
+ _kPoisonedUUID
+ _objc_moveWeak
+ _objc_msgSend$_evaluateTypes:
+ _objc_msgSend$_fetchURLForItemID:creatingPlaceholderIfMissing:completionHandlerWithInfo:
+ _objc_msgSend$_generateDomainIDFromDSID:
+ _objc_msgSend$_initWithFileURL:library:clientID:name:contentsURL:isBackup:revision:
+ _objc_msgSend$aa_personID
+ _objc_msgSend$accountTypeWithAccountTypeIdentifier:
+ _objc_msgSend$accountsWithAccountType:
+ _objc_msgSend$addDomain:forProviderIdentifier:byImportingDirectoryAtURL:nonWrappedURL:userAllowedDBDrop:knownFolders:completionHandler:
+ _objc_msgSend$addDomain:forProviderIdentifier:byImportingDirectoryAtURL:userAllowedDBDrop:knownFolders:completionHandler:
+ _objc_msgSend$addDomain:forProviderIdentifier:byImportingDirectoryAtURL:userAllowedDBDrop:knownFolders:synchronous:completionHandler:
+ _objc_msgSend$addDomain:userAllowedDBDrop:completionHandler:
+ _objc_msgSend$additionWithName:inNameSpace:error:
+ _objc_msgSend$appLibraryCollectionForProviderDomainID:
+ _objc_msgSend$bundleRecordForAuditToken:error:
+ _objc_msgSend$cachedProviderDomainWithID:cachePolicy:error:
+ _objc_msgSend$checkLocationEligibilityForDomain:completionHandler:
+ _objc_msgSend$currentUser
+ _objc_msgSend$eligibleActionsForItems:domainCachePolicy:
+ _objc_msgSend$enumeratedURL
+ _objc_msgSend$fetchHierarchyForItemID:recursively:ignoreAlternateContentURL:reply:
+ _objc_msgSend$fetchLatestVersionForItemAtURL:bundleID:completionHandler:
+ _objc_msgSend$fetchProviderDomainForItem:cachePolicy:completionHandler:
+ _objc_msgSend$fp_UUID
+ _objc_msgSend$fp_UUIDWithObfuscation:
+ _objc_msgSend$fp_annotateInvocation:withLogSection:
+ _objc_msgSend$fp_annotateWithXPCSanitizer:
+ _objc_msgSend$fp_fpfsProviderDomainID:
+ _objc_msgSend$fp_fpfsProviderDomainID:error:
+ _objc_msgSend$fp_lmdURL
+ _objc_msgSend$fp_supportDirectory
+ _objc_msgSend$fp_userInfo
+ _objc_msgSend$getReachabilityFlagsByCheckingNetwork
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithIdentifier:displayName:userInfo:volumeURL:pathRelativeToDocumentStorage:hidden:replicated:
+ _objc_msgSend$invalidateCurrentContext:
+ _objc_msgSend$isSharedIPad
+ _objc_msgSend$itemIsSupportedSearchScopeWithCachePolicy:completionHandler:
+ _objc_msgSend$listPausedURLsWithBundleID:completionHandler:
+ _objc_msgSend$newCollectionWithItemAtURL:skipValidation:error:
+ _objc_msgSend$nullableEnumeratedItemID
+ _objc_msgSend$pauseSyncForItemAtURL:behavior:bundleID:completionHandler:
+ _objc_msgSend$persistentIdentifier
+ _objc_msgSend$providerDomainForItem:cachePolicy:error:
+ _objc_msgSend$providerDomainWithID:cachePolicy:completionHandler:
+ _objc_msgSend$providerDomainWithID:cachePolicy:error:
+ _objc_msgSend$restoreUserURL:cleanupOnSuccess:completionHandler:
+ _objc_msgSend$resumeSyncForItemAtURL:behavior:bundleID:completionHandler:
+ _objc_msgSend$runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:completionHandler:
+ _objc_msgSend$runningInSyncBubble
+ _objc_msgSend$setEnumeratedURL:
+ _objc_msgSend$setNullableEnumeratedItemID:
+ _objc_msgSend$setRequireSandboxAccess:
+ _objc_msgSend$setupWithLog:forConnection:
+ _objc_msgSend$stateDirectoryWithCompletionHandler:
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_msgSend$temporaryDirectoryURLWithError:
+ _objc_msgSend$unsignedLongValue
+ _objc_msgSend$versionOfItemAtURL:forPersistentIdentifier:
+ _runningInSyncBubble.onceToken
+ _runningInSyncBubble.res
+ _stateURLByDomain
+ _strcasecmp
- +[NSFileProviderManager addDomain:forProviderIdentifier:byImportingDirectoryAtURL:knownFolders:completionHandler:]
- +[NSFileProviderManager addDomain:forProviderIdentifier:byImportingDirectoryAtURL:knownFolders:synchronous:completionHandler:]
- +[NSFileProviderManager checkLocationEligibilityForDomain:error:]
- +[NSFileProviderManager checkLocationEligibilityForDomain:error:].cold.1
- +[NSURL(FPAdditions) fp_uniqueTempFolderWithError:]
- -[FPItem _evaluateTypes]
- -[FPItem itemIsSupportedSearchScopeAllowingCache:completionHandler:]
- -[FPItemManager eligibleActionsForItems:allowCachedDomain:]
- -[FPItemManager eligibleActionsForItems:allowCachedDomain:].cold.1
- -[FPXConnectionHandler invalidateCurrentContext]
- -[FPXEnumerator currentSyncAnchorWithCompletion:].cold.1
- -[FPXEnumerator enumerateChangesFromToken:suggestedBatchSize:reply:].cold.1
- -[FPXEnumerator enumerateItemsFromPage:suggestedPageSize:reply:].cold.1
- -[FPXExtensionContext _test_callFileProviderManagerAPIs:].cold.1
- -[FPXExtensionContext bulkItemChanges:changedFields:completionHandler:].cold.2
- -[FPXExtensionContext dropDomainWithCompletionHandler:].cold.1
- -[FPXExtensionContext dropIndexForDomain:completionHandler:].cold.6
- -[FPXExtensionContext dumpIndexStateForDomain:toFileHandler:completionHandler:].cold.3
- -[FPXExtensionContext dumpInternalStateToTermDumper:domainIdentifier:completionHandler:].cold.1
- -[FPXExtensionContext fetchAndStartEnumeratingWithSettings:observer:request:completionHandler:].cold.1
- -[FPXExtensionContext fetchCustomPushTopicsWithCompletionHandler:].cold.1
- -[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:reply:].cold.1
- -[FPXExtensionContext fetchHierarchyForItemID:recursively:reply:]
- -[FPXExtensionContext fetchOperationServiceEndpoint:].cold.1
- -[FPXExtensionContext fetchOperationServiceEndpoint:].cold.2
- -[FPXExtensionContext fetchTrashIdentifiersWithCompletionHandler:].cold.1
- -[FPXExtensionContext fetchVendorEndpoint:].cold.1
- -[FPXExtensionContext fetchVendorEndpoint:].cold.2
- -[FPXExtensionContext forceUpdateBlockedProcessNamesFromDomain:completionHandler:].cold.1
- -[FPXExtensionContext importDidFinishWithCompletionHandler:].cold.1
- -[FPXExtensionContext indexOneBatchInDomain:completionHandler:].cold.8
- -[FPXExtensionContext preflightTrashItemIDs:completionHandler:].cold.1
- -[FPXExtensionContext providePlaceholderAtURL:completionHandler:].cold.1
- -[FPXExtensionContext signalEnumeratorForMaterializedItemsWithCompletionHandler:].cold.1
- -[FPXExtensionContext signalEnumeratorForPendingItemsWithCompletionHandler:].cold.1
- -[FPXExtensionContext singleItemChange:changedFields:bounce:completionHandler:].cold.1
- -[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:].cold.1
- -[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:].cold.1
- -[FPXExtensionContext trashItemAtURL:completionHandler:].cold.1
- -[FPXExtensionContext updateIgnoreStateOfItemWithIdentifiers:ignoreState:completionHandler:].cold.1
- -[FPXExtensionContext updateIgnoreStateOfItemWithIdentifiers:ignoreState:completionHandler:].cold.2
- -[FPXExtensionContext userInteractionErrorsForPerformingAction:sourceItems:destinationItem:fpProviderDomainId:sourceItemKeysAllowList:destinationItemKeysAllowList:completionHandler:].cold.1
- -[FPXExtensionContext valuesForAttributes:forItemID:completionHandler:].cold.1
- -[FPXExtensionContext waitForStabilizationWithCompletionHandler:].cold.1
- -[FPXExtensionContext wakeForPushWithCompletionHandler:].cold.2
- -[NSFileProviderDomain initWithIdentifier:displayName:volumeURL:]
- -[NSFileProviderDomain initWithIdentifier:displayName:volumeURL:pathRelativeToDocumentStorage:hidden:replicated:]
- -[NSFileProviderManager(Download) requestDownloadForItemWithIdentifier:requestedRange:completionHandler:]
- -[NSXPCConnection(FPAdditions) fp_bundleURL]
- GCC_except_table100
- GCC_except_table130
- GCC_except_table141
- GCC_except_table149
- GCC_except_table152
- GCC_except_table194
- GCC_except_table202
- GCC_except_table230
- GCC_except_table235
- GCC_except_table238
- GCC_except_table241
- GCC_except_table244
- GCC_except_table253
- GCC_except_table256
- GCC_except_table66
- GCC_except_table74
- _FPFSD2DRestorePluginIsEnabled
- _FPFSD2DRestorePluginIsEnabled.enabled
- _FPFSD2DRestorePluginIsEnabled.onceToken
- _FPFeatureFlagD2DMigrationIsEnabled
- _MGCopyAnswer
- _NSFileProviderErrorApplicationExtensionNotFound
- _NSFileProviderErrorProviderDomainNotFound
- _NSFileProviderErrorProviderDomainTemporarilyUnavailable
- _OUTLINED_FUNCTION_38
- _OUTLINED_FUNCTION_39
- _OUTLINED_FUNCTION_40
- _OUTLINED_FUNCTION_41
- _OUTLINED_FUNCTION_42
- _OUTLINED_FUNCTION_43
- _OUTLINED_FUNCTION_44
- _OUTLINED_FUNCTION_45
- _OUTLINED_FUNCTION_46
- _OUTLINED_FUNCTION_47
- _OUTLINED_FUNCTION_48
- _OUTLINED_FUNCTION_49
- _OUTLINED_FUNCTION_50
- __CFBundleCopyBundleURLForExecutableURL
- __OBJC_$_CATEGORY_NSXPCConnection_$_Sanitization
- __OBJC_$_CLASS_METHODS_NSFileProviderManager(MaterializedSet|PendingSet|Import|ImportPrivate|Download|Barrier|Stabilization|Eviction|Attribution|ForceIngestion|Disconnection|TestingModeInteractive|GlobalProgress|NSFileProviderService|Materialize|MaterializePrivate|Diagnostics)
- __OBJC_$_INSTANCE_METHODS_NSFileProviderManager(MaterializedSet|PendingSet|Import|ImportPrivate|Download|Barrier|Stabilization|Eviction|Attribution|ForceIngestion|Disconnection|TestingModeInteractive|GlobalProgress|NSFileProviderService|Materialize|MaterializePrivate|Diagnostics)
- __OBJC_$_INSTANCE_METHODS_NSXPCConnection(Sanitization|FPAdditions)
- ___101-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:reply:]_block_invoke.524
- ___101-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:reply:]_block_invoke_2.528
- ___103-[FPXExtensionContext modifyItem:baseVersion:changedFields:contents:options:request:completionHandler:]_block_invoke.274
- ___105-[NSFileProviderManager(Download) requestDownloadForItemWithIdentifier:requestedRange:completionHandler:]_block_invoke
- ___105-[NSFileProviderManager(Download) requestDownloadForItemWithIdentifier:requestedRange:completionHandler:]_block_invoke_2
- ___107-[NSFileProviderExtension(CreateItem) createItemBasedOnTemplate:fields:contents:options:completionHandler:]_block_invoke.336
- ___107-[NSFileProviderExtension(CreateItem) createItemBasedOnTemplate:fields:contents:options:completionHandler:]_block_invoke.343
- ___109-[FPXExtensionContext performActionWithIdentifier:onItemsWithIdentifiers:domainIdentifier:completionHandler:]_block_invoke.cold.3
- ___109-[FPXExtensionContext performActionWithIdentifier:onItemsWithIdentifiers:domainIdentifier:completionHandler:]_block_invoke_2.cold.1
- ___110-[FPXExtensionContext URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.322
- ___110-[FPXExtensionContext URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.322.cold.1
- ___110-[FPXExtensionContext URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.322.cold.2
- ___110-[FPXExtensionContext URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.322.cold.3
- ___110-[FPXExtensionContext URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.cold.2
- ___110-[FPXExtensionContext deleteSearchableItemsWithSpotlightDomainIdentifiers:domainIdentifier:completionHandler:]_block_invoke_2.cold.1
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.511
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.511.cold.1
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.511.cold.2
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.511.cold.3
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.511.cold.4
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.511.cold.5
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.511.cold.6
- ___120-[FPXExtensionContext _createItemBasedOnTemplate:fields:contents:options:request:bounce:bounceNumber:completionHandler:]_block_invoke.515
- ___126+[NSFileProviderManager addDomain:forProviderIdentifier:byImportingDirectoryAtURL:knownFolders:synchronous:completionHandler:]_block_invoke
- ___137-[FPXExtensionContext fetchContentsForItemWithID:version:request:estimatedItemSize:isSymlink:extent:alignment:options:completionHandler:]_block_invoke.250
- ___137-[FPXExtensionContext fetchContentsForItemWithID:version:request:estimatedItemSize:isSymlink:extent:alignment:options:completionHandler:]_block_invoke_2.258
- ___155-[FPXExtensionContext fetchContentsForItemWithID:version:usingExistingContentsAtURL:existingVersion:request:estimatedItemSize:isSymlink:completionHandler:]_block_invoke.267
- ___155-[FPXExtensionContext fetchContentsForItemWithID:version:usingExistingContentsAtURL:existingVersion:request:estimatedItemSize:isSymlink:completionHandler:]_block_invoke.268
- ___34-[FPItemCollection startObserving]_block_invoke.134
- ___34-[FPItemCollection startObserving]_block_invoke.134.cold.1
- ___40-[FPItemCollection _flushPendingUpdates]_block_invoke.186
- ___40-[FPItemCollection _flushPendingUpdates]_block_invoke.186.cold.1
- ___43+[FPItemCollection resumeVendorEnumeration]_block_invoke.219
- ___44-[FPItemCollection sendIndexPathBasedDiffs:]_block_invoke.206
- ___44-[FPItemCollection sendIndexPathBasedDiffs:]_block_invoke.206.cold.1
- ___47+[FPProviderDomain providerDomainWithID:error:]_block_invoke
- ___47-[FPXConnectionHandler shouldAcceptConnection:]_block_invoke.4
- ___47-[FPXConnectionHandler shouldAcceptConnection:]_block_invoke.4.cold.1
- ___49-[FPXEnumerator currentSyncAnchorWithCompletion:]_block_invoke.174
- ___49-[FPXEnumerator currentSyncAnchorWithCompletion:]_block_invoke.174.cold.1
- ___49-[FPXEnumerator currentSyncAnchorWithCompletion:]_block_invoke.cold.2
- ___49-[FPXEnumerator currentSyncAnchorWithCompletion:]_block_invoke.cold.3
- ___50-[NSFileProviderManager _signalPendingEnumerators]_block_invoke.167
- ___52-[FPXExtensionContext itemForURL:completionHandler:]_block_invoke.317
- ___52-[FPXExtensionContext itemForURL:completionHandler:]_block_invoke.cold.1
- ___52-[FPXExtensionContext itemForURL:completionHandler:]_block_invoke.cold.2
- ___55-[FPExtensionCollection _startMonitoringDSCopyProgress]_block_invoke.32
- ___55-[FPExtensionCollection _startMonitoringDSCopyProgress]_block_invoke.34
- ___55-[FPXExtensionContext dropDomainWithCompletionHandler:]_block_invoke.cold.1
- ___56-[FPXExtensionContext evictItemAtURL:completionHandler:]_block_invoke.cold.1
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.326
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.330
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.330.cold.1
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.331
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.331.cold.1
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.331.cold.2
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.332
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke.cold.1
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke_3.cold.2
- ___56-[FPXExtensionContext trashItemAtURL:completionHandler:]_block_invoke_3.cold.3
- ___57-[FPXExtensionContext _test_callFileProviderManagerAPIs:]_block_invoke.cold.1
- ___58-[FPXExtensionContext itemChangedAtURL:completionHandler:]_block_invoke.cold.2
- ___60-[FPXExtensionContext dropIndexForDomain:completionHandler:]_block_invoke.cold.1
- ___62-[FPExtensionDataSource _updateItemsWithUpdatesCount:section:]_block_invoke_2.cold.5
- ___63-[FPXExtensionContext preflightTrashItemIDs:completionHandler:]_block_invoke.298
- ___63-[FPXExtensionContext preflightTrashItemIDs:completionHandler:]_block_invoke_2.cold.1
- ___64-[FPXEnumerator enumerateItemsFromPage:suggestedPageSize:reply:]_block_invoke.177
- ___64-[FPXEnumerator enumerateItemsFromPage:suggestedPageSize:reply:]_block_invoke.177.cold.1
- ___64-[FPXEnumerator enumerateItemsFromPage:suggestedPageSize:reply:]_block_invoke.185
- ___64-[FPXExtensionContext identifierForItemAtURL:completionHandler:]_block_invoke.cold.2
- ___64-[FPXExtensionContext identifierForItemAtURL:completionHandler:]_block_invoke.cold.3
- ___65-[FPXExtensionContext fetchHierarchyForItemID:recursively:reply:]_block_invoke
- ___65-[FPXExtensionContext providePlaceholderAtURL:completionHandler:]_block_invoke.304
- ___65-[FPXExtensionContext providePlaceholderAtURL:completionHandler:]_block_invoke.cold.1
- ___65-[FPXExtensionContext waitForStabilizationWithCompletionHandler:]_block_invoke.597
- ___65-[FPXExtensionContext waitForStabilizationWithCompletionHandler:]_block_invoke.597.cold.1
- ___65-[FPXExtensionContext waitForStabilizationWithCompletionHandler:]_block_invoke.cold.1
- ___66+[FPItemToURLResourcesConverter dictionaryFromItem:requestedKeys:]_block_invoke.359
- ___66-[FPXExtensionContext fetchCustomPushTopicsWithCompletionHandler:]_block_invoke.cold.1
- ___66-[FPXExtensionContext fetchCustomPushTopicsWithCompletionHandler:]_block_invoke.cold.2
- ___66-[FPXExtensionContext fetchTrashIdentifiersWithCompletionHandler:]_block_invoke.584
- ___66-[FPXExtensionContext fetchTrashIdentifiersWithCompletionHandler:]_block_invoke.cold.1
- ___66-[FPXExtensionContext wakeForSessionIdentifier:completionHandler:]_block_invoke.544
- ___66-[FPXExtensionContext wakeForSessionIdentifier:completionHandler:]_block_invoke.544.cold.1
- ___66-[FPXExtensionContext wakeForSessionIdentifier:completionHandler:]_block_invoke.cold.1
- ___67-[FPPendingSetEnumerator enumerateItemsForObserver:startingAtPage:]_block_invoke.429
- ___67-[FPXExtensionContext bulkEvictItemsWithItemIDs:completionHandler:]_block_invoke.545
- ___67-[FPXExtensionContext bulkEvictItemsWithItemIDs:completionHandler:]_block_invoke.547.cold.1
- ___67-[FPXExtensionContext bulkEvictItemsWithItemIDs:completionHandler:]_block_invoke.cold.1
- ___68-[FPItem itemIsSupportedSearchScopeAllowingCache:completionHandler:]_block_invoke
- ___68-[FPXEnumerator enumerateChangesFromToken:suggestedBatchSize:reply:]_block_invoke.191
- ___68-[FPXExtensionContext disconnectDomainID:options:completionHandler:]_block_invoke.cold.2
- ___68-[FPXExtensionContext disconnectDomainID:options:completionHandler:]_block_invoke_2.cold.1
- ___68-[FPXExtensionContext disconnectDomainID:options:completionHandler:]_block_invoke_3.cold.1
- ___68-[FPXExtensionContext preflightReparentItemIDs:underParentID:reply:]_block_invoke.480
- ___68-[FPXExtensionContext preflightReparentItemIDs:underParentID:reply:]_block_invoke_3.cold.1
- ___69-[FPPendingSetEnumerator enumerateChangesForObserver:fromSyncAnchor:]_block_invoke.433
- ___69-[FPPendingSetEnumerator enumerateChangesForObserver:fromSyncAnchor:]_block_invoke_2.436
- ___69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.499
- ___69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.499.cold.1
- ___69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke.505
- ___69-[FPXExtensionContext deleteItemsWithIDs:baseVersions:options:reply:]_block_invoke_2.cold.2
- ___69-[FPXExtensionContext fetchPublishingURLForItemID:completionHandler:]_block_invoke.cold.2
- ___71+[FPProviderDomain providerDomainWithID:allowCached:completionHandler:]_block_invoke
- ___71-[FPXExtensionContext valuesForAttributes:forItemID:completionHandler:]_block_invoke_2.cold.1
- ___71-[FPXExtensionContext valuesForAttributes:forItemID:completionHandler:]_block_invoke_2.cold.2
- ___71-[FPXExtensionContext valuesForAttributes:forItemID:completionHandler:]_block_invoke_2.cold.3
- ___78-[FPXExtensionContext attemptRecoveryFromError:optionIndex:completionHandler:]_block_invoke.550
- ___78-[FPXExtensionContext attemptRecoveryFromError:optionIndex:completionHandler:]_block_invoke.550.cold.1
- ___78-[FPXExtensionContext attemptRecoveryFromError:optionIndex:completionHandler:]_block_invoke.cold.1
- ___79-[FPXExtensionContext singleItemChange:changedFields:bounce:completionHandler:]_block_invoke.cold.1
- ___79-[FPXExtensionContext singleItemChange:changedFields:bounce:completionHandler:]_block_invoke_2.cold.1
- ___80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.188
- ___80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.188.cold.1
- ___80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.188.cold.2
- ___80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.188.cold.3
- ___80-[FPXExtensionContext startProvidingItemAtURL:readingOptions:completionHandler:]_block_invoke.cold.2
- ___82-[FPXExtensionContext forceUpdateBlockedProcessNamesFromDomain:completionHandler:]_block_invoke.cold.1
- ___87-[FPXExtensionContext fetchServicesForItemID:allowRestrictedSources:completionHandler:]_block_invoke.463
- ___87-[FPXExtensionContext fetchServicesForItemID:allowRestrictedSources:completionHandler:]_block_invoke_2.cold.1
- ___88-[FPXExtensionContext dumpInternalStateToTermDumper:domainIdentifier:completionHandler:]_block_invoke_3.cold.1
- ___89-[FPXExtensionContext listRemoteVersionsWithSettings:observer:request:completionHandler:]_block_invoke.cold.5
- ___89-[FPXExtensionContext listRemoteVersionsWithSettings:observer:request:completionHandler:]_block_invoke.cold.6
- ___89-[FPXExtensionContext listRemoteVersionsWithSettings:observer:request:completionHandler:]_block_invoke.cold.7
- ___93-[FPXExtensionContext movingItemAtURL:requiresProvidingWithDestinationURL:completionHandler:]_block_invoke.cold.1
- ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.395
- ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.395.cold.1
- ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.408
- ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.408.cold.1
- ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.413
- ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.413.cold.1
- ___93-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]_block_invoke.cold.4
- ___94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.306
- ___94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke.cold.2
- ___94-[FPXExtensionContext didUpdateAlternateContentsDocumentForDocumentWithURL:completionHandler:]_block_invoke_2.cold.5
- ___95-[FPXExtensionContext fetchAndStartEnumeratingWithSettings:observer:request:completionHandler:]_block_invoke.439
- ___95-[FPXExtensionContext fetchAndStartEnumeratingWithSettings:observer:request:completionHandler:]_block_invoke.cold.4
- ___95-[FPXExtensionContext fetchAndStartEnumeratingWithSettings:observer:request:completionHandler:]_block_invoke_2.cold.1
- ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.344
- ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.363
- ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.363.cold.1
- ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.365
- ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.368.cold.1
- ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke.cold.3
- ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke_2.367
- ___97-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]_block_invoke_2.367.cold.1
- ___98-[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:]_block_invoke.138
- ___98-[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:]_block_invoke.138.cold.1
- ___98-[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:]_block_invoke.138.cold.2
- ___FPCrossDeviceItemIDForItemID_block_invoke.67
- ___FPFSD2DRestorePluginIsEnabled_block_invoke
- ___FPFetchLatestVersionForFileAtURL_block_invoke_2
- ___FPGetPausedFilesList_block_invoke_2
- ___FPItemIDFromCrossDeviceItemID_block_invoke.93
- ___FPItemURLForCrossDeviceItemID_block_invoke.75
- ___FPItemURLForCrossDeviceItemID_block_invoke.75.cold.1
- ___FPItemURLForCrossDeviceItemID_block_invoke.80
- ___FPItemURLForCrossDeviceItemID_block_invoke.80.cold.1
- ___FPItemURLForCrossDeviceItemID_block_invoke.81
- ___FPPauseSyncForFileAtURL_block_invoke
- ___FPPauseSyncForFileAtURL_block_invoke_2
- ___FPResumeSyncForFileAtURLWithOptions_block_invoke
- ___FPResumeSyncForFileAtURLWithOptions_block_invoke_2
- ___block_descriptor_48_e8_32bs_e199_i16?0^{fpfs_fileattrs={fpfs_item_handle=QQII*iI}{fpfs_metadata=ib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1Sq{timespec=qq}{timespec=qq}{timespec=qq}Q{fpfs_tag_data=^vQi}(?=II)QQq*q*^{fpfs_xattr}II*BB*ii}*Q[0c]}8ls32l8
- ___block_descriptor_48_e8_32s40bs_e35_v24?0"NSFileVersion"8"NSError"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs48r_e27_v24?0"NSURL"8"NSError"16ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e42_v24?0"<NSFileProviderItem>"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40bs48r56r_e5_v8?0ls32l8r48l8r56l8s40l8
- ___block_descriptor_64_e8_32s40bs_e56_v16?0"<FPDDomainServicing><FPXPCAutomaticErrorProxy>"8ls32l8s40l8
- ___block_descriptor_72_e8_32s40s48bs_e75_v48?0"NSArray"8"NSData"16"NSData"24"FPExtensionResponse"32"NSError"40ls48l8s32l8s40l8
- ___block_descriptor_73_e8_32s40s48s56s64bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s64l8s48l8s56l8
- ___block_literal_global.142
- ___block_literal_global.151
- ___block_literal_global.156
- ___block_literal_global.171
- ___block_literal_global.173
- ___block_literal_global.180
- ___block_literal_global.200
- ___block_literal_global.215
- ___block_literal_global.223
- ___block_literal_global.227
- ___block_literal_global.231
- ___block_literal_global.251
- ___block_literal_global.255
- ___block_literal_global.26
- ___block_literal_global.261
- ___block_literal_global.274
- ___block_literal_global.277
- ___block_literal_global.280
- ___block_literal_global.315
- ___block_literal_global.325
- ___block_literal_global.333
- ___block_literal_global.345
- ___block_literal_global.347
- ___block_literal_global.354
- ___block_literal_global.402
- ___block_literal_global.408
- ___block_literal_global.410
- ___block_literal_global.421
- ___block_literal_global.426
- ___block_literal_global.43
- ___block_literal_global.431
- ___block_literal_global.435
- ___block_literal_global.466
- ___block_literal_global.518
- ___block_literal_global.595
- ___block_literal_global.620
- ___block_literal_global.71
- __unnamed_array_storage.284
- _fpfs_is_evictable
- _kCiconiaEntitlement
- _kInPlaceCollaborationEntitlement
- _objc_msgSend$FPFetchLatestVersionForFileAtURL:completionHandler:
- _objc_msgSend$FPGetPausedFilesList:completionHandler:
- _objc_msgSend$FPPauseSyncForFileAtURL:timeout:options:completionHandler:
- _objc_msgSend$FPResumeSyncForFileAtURL:resumeOptions:completionHandler:
- _objc_msgSend$_evaluateTypes
- _objc_msgSend$addDomain:forProviderIdentifier:byImportingDirectoryAtURL:knownFolders:completionHandler:
- _objc_msgSend$addDomain:forProviderIdentifier:byImportingDirectoryAtURL:knownFolders:synchronous:completionHandler:
- _objc_msgSend$addDomain:forProviderIdentifier:byImportingDirectoryAtURL:nonWrappedURL:knownFolders:completionHandler:
- _objc_msgSend$bundleProxyForURL:
- _objc_msgSend$eligibleActionsForItems:allowCachedDomain:
- _objc_msgSend$fetchHierarchyForItemID:recursively:reply:
- _objc_msgSend$fetchProviderDomainForItem:allowCached:completionHandler:
- _objc_msgSend$fp_bundleURL
- _objc_msgSend$initWithIdentifier:displayName:volumeURL:pathRelativeToDocumentStorage:hidden:replicated:
- _objc_msgSend$invalidateCurrentContext
- _objc_msgSend$itemIsSupportedSearchScopeAllowingCache:completionHandler:
- _objc_msgSend$providerDomainForItem:error:
- _objc_msgSend$providerDomainWithID:allowCached:completionHandler:
- _objc_msgSend$providerDomainWithID:allowCached:error:
- _objc_msgSend$providerDomainWithID:error:
- _objc_msgSend$restoreUserURL:completionHandler:
- _objc_retain_x11
- _temporaryDirectoriesWithSecurityScope
CStrings:
+ "\x01$\x12\x15"
+ " cap:%c%c%c%c%c%c%c%c"
+ "%@...%@"
+ "%s Too many arguments supplied for databasesBackupsPath."
+ "(unavailable)"
+ ",changing"
+ ",forbiddenMDM"
+ "-[FPDaemonConnection runFPCKForDomainWithID:databasesBackupsPath:options:reason:completionHandler:]"
+ "-[FPXExtensionContext fetchHierarchyForItemID:recursively:ignoreAlternateContentURL:reply:]"
+ "-[FPXExtensionContext fetchHierarchyForItemID:recursively:ignoreAlternateContentURL:reply:]_block_invoke"
+ "-[NSXPCConnection(FPAdditions) fp_userInfo]"
+ ".CloudDocs"
+ "/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/NSXPCConnection+FPAdditions.m"
+ "00000000-0000-0000-0000-000000000000"
+ "1835.102.2"
+ "<%@ name:'%@' device:'%@' owner:'%@' size:%llu mtime:%@ thumbnail:%d etag:%@ url:'%@'"
+ "<%@:%p id:\"%@\" name:\"%@\" urls(%d%s):%@ db:%@%@ state:%s%s%s%s%s%s%s features:%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s>"
+ "<unresolved>"
+ "@\"<NSSecureCoding>\"40@0:8@\"NSXPCConnection\"16@\"NSXPCCoder\"24@32"
+ "@28@0:8B16^@20"
+ "@40@0:8@16Q24^@32"
+ "@64@0:8@16@24@32@40@48B56B60"
+ "B40@0:8@16^Q24^@32"
+ "Couldn't get purgeable flags, errno %{errno}d"
+ "DISCONNECTION_REASON_FORBIDDEN_MDM"
+ "FPAddtions"
+ "FPCKService"
+ "FPLogSection"
+ "FPXPCLogDelegate"
+ "FPXPCSanitizerKey"
+ "Invalid evictability parameters: %d / 0x%llx on %s ino:%llu"
+ "NSFileProviderErrorCategoryKey"
+ "NSXPCConnection userInfo is wrong type: %@"
+ "NSXPCConnectionDelegate"
+ "Provider %@ returned invalid item %@ of class %@ with identifier %@, missing contentType. Break on %s to debug this."
+ "Provider %@ returned invalid item %@ of class %@ with identifier %@, missing filename. Break on %s to debug this."
+ "Provider %@ returned invalid item %@ of class %@ with identifier %@, missing identifier. Break on %s to debug this."
+ "Provider %@ returned invalid item %@ of class %@ with identifier %@, missing itemVersion. Break on %s to debug this."
+ "Provider %@ returned invalid item %@ of class %@ with identifier %@, missing provider. Break on %s to debug this."
+ "T@\"FPItemID\",C,D,N"
+ "T@\"FPItemID\",C,N"
+ "T@\"NSArray\",?,R,C"
+ "T@\"NSData\",?,R,C,N"
+ "T@\"NSData\",?,R,N"
+ "T@\"NSDate\",?,R,C,N"
+ "T@\"NSDictionary\",?,R,N"
+ "T@\"NSError\",?,R,C,N"
+ "T@\"NSFileProviderItemVersion\",?,R,N"
+ "T@\"NSNumber\",?,R,C"
+ "T@\"NSNumber\",?,R,C,GisDownloadRequested"
+ "T@\"NSNumber\",?,R,C,N"
+ "T@\"NSPersonNameComponents\",?,R,N"
+ "T@\"NSSet\",?,R"
+ "T@\"NSSet\",?,R,C"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"NSString\",?,R,C,N,VtypeIdentifier"
+ "T@\"NSString\",?,R,N"
+ "T@\"NSURL\",?,R,C"
+ "T@\"NSURL\",C,N,V_enumeratedURL"
+ "T@\"UTType\",?,R,C,N"
+ "T@\"UTType\",?,R,C,N,VcontentType"
+ "TB,?,GisSyncRoot"
+ "TB,?,R"
+ "TB,?,R,Gfp_isUbiquitous"
+ "TB,?,R,GisHidden"
+ "TB,?,R,N,Gfp_isAddedByCurrentUser"
+ "TB,?,R,N,Gfp_isLastModifiedByCurrentUser"
+ "TB,?,R,N,GisDownloaded"
+ "TB,?,R,N,GisDownloading"
+ "TB,?,R,N,GisExcludedFromSync"
+ "TB,?,R,N,GisMostRecentVersionDownloaded"
+ "TB,?,R,N,GisShared"
+ "TB,?,R,N,GisSharedByCurrentUser"
+ "TB,?,R,N,GisTopLevelSharedItem"
+ "TB,?,R,N,GisTrashed"
+ "TB,?,R,N,GisUploaded"
+ "TB,?,R,N,GisUploading"
+ "TB,N,V_storageURLsAreInTransientState"
+ "TQ,?,R,N"
+ "TQ,?,R,N,Vcapabilities"
+ "Tq,?,R,N"
+ "T{NSFileProviderTypeAndCreator=II},?,R,N"
+ "[CRIT] Provider %{public}@ returned invalid item %@ of class %{public}@ with identifier %{public}@, missing contentType. Break on %{public}s to debug this."
+ "[CRIT] Provider %{public}@ returned invalid item %@ of class %{public}@ with identifier %{public}@, missing filename. Break on %{public}s to debug this."
+ "[CRIT] Provider %{public}@ returned invalid item %@ of class %{public}@ with identifier %{public}@, missing identifier. Break on %{public}s to debug this."
+ "[CRIT] Provider %{public}@ returned invalid item %@ of class %{public}@ with identifier %{public}@, missing itemVersion. Break on %{public}s to debug this."
+ "[CRIT] Provider %{public}@ returned invalid item %@ of class %{public}@ with identifier %{public}@, missing provider. Break on %{public}s to debug this."
+ "[CRIT] [helena] %@ has existing context, so we have gotten two calls to create a connection (connection count is %d)"
+ "[DEBUG] %@ learned enumerated item identifier"
+ "[DEBUG] Do not migrate to FPFS user default is configured."
+ "[DEBUG] Enumerated URL changed, resetting %@"
+ "[DEBUG] Generating domainID for %@"
+ "[DEBUG] caching state URL (daemon) %@ for domain %@"
+ "[DEBUG] fetching more changes [moreChanges: %d, concurrentChanges: %d, shouldUpdate: %d]"
+ "[DEBUG] ipc: %@ %s %@"
+ "[DEBUG] ipc: %@ %s %@ fields=%x options=%x contentURL=%@"
+ "[DEBUG] ipc: %@ %s %@, %@"
+ "[DEBUG] ipc: %@ %s %@, %@, %@"
+ "[DEBUG] ipc: %@ %s %@, %ld"
+ "[DEBUG] ipc: %@ %s %@, %lu"
+ "[DEBUG] ipc: %@ %s %@, %{bool}d"
+ "[DEBUG] ipc: %@ %s %@, %{bool}d, %{bool}d"
+ "[DEBUG] ipc: %@ %s %@, 0x%lx"
+ "[DEBUG] ipc: %@ %s %@, estimated size=%lld"
+ "[DEBUG] ipc: %@ %s %@, estimated size=%lld, symlink=%{bool}d"
+ "[DEBUG] ipc: %@ %s %@: %@"
+ "[DEBUG] ipc: %@ %s %d"
+ "[DEBUG] ┏%llx flushing pending updates for %@, generation %d"
+ "[DEBUG] ┳%llx ipc to %@ without reply"
+ "[DEBUG] ┳%llx ipc: %@, reply of %s "
+ "[DEBUG] ┳%llx ipc: %@, reply of %s %@"
+ "[DEBUG] ┳%llx ipc: %@, reply of %s %@, %@"
+ "[DEBUG] ┳%llx ipc: %@, reply of %s %@, %@, %@"
+ "[DEBUG] ┳%llx ipc: %@, reply of %s %@, %@, %@, %@, %lu, %@"
+ "[DEBUG] ┳%llx ipc: %@, reply of %s %@, %@, %@, %lu, %@"
+ "[DEBUG] ┳%llx ipc: %@, reply of %s %@, 0x%lx, %{bool}d, %@, %@"
+ "[DEBUG] ┳%llx ipc: %@, reply of %s %@, 0x%x, %{bool}d, %@, %@"
+ "[DEBUG] ┳%llx ipc: %@, reply of %s %{bool}d, %@"
+ "[DEBUG] ┳%llx ipc: %@[%d]: -[%{public}@ %{public}@] @ QoS %u"
+ "[ERROR] Couldn't find addition with name %@ - %@"
+ "[ERROR] Couldn't get storage after received version - %@"
+ "[ERROR] Couldn't look up file version by persistent identifier"
+ "[ERROR] Failed opening URL: %d"
+ "[ERROR] Unable to get file system attributes for volume path %{public}@: %{public}s"
+ "[INFO] Non-eligible device %{public}s [%d]: APFSIOC_GET_DEV_INFO error %{errno}d"
+ "[INFO] Non-eligible device %{public}s [%d]: R/O volume"
+ "[INFO] Non-eligible device %{public}s [%d]: disk images are excluded"
+ "[INFO] Non-eligible device %{public}s [%d]: non-apfs"
+ "[INFO] Non-eligible device %{public}s [%d]: non-local"
+ "[INFO] Non-eligible device %{public}s [%d]: unencrypted"
+ "[INFO] [helena] accepting connection %@"
+ "[INFO] [helena] call to beginRequest from connection %@"
+ "[INFO] [helena] connection %p was invalidated, %d left"
+ "[INFO] [helena] last connection %p was invalidated, tearing down"
+ "[NOTICE] shared iPad: extension is running in the sync bubble for euid %u"
+ "__FILEPROVIDER_BAD_ITEM_MISSING_CONTENTTYPE__"
+ "__FILEPROVIDER_BAD_ITEM_MISSING_FILENAME__"
+ "__FILEPROVIDER_BAD_ITEM_MISSING_IDENTIFIER__"
+ "__FILEPROVIDER_BAD_ITEM_MISSING_ITEMVERSION__"
+ "__FILEPROVIDER_BAD_ITEM_MISSING_PROVIDER__"
+ "_activeConnections"
+ "_enumeratedURL"
+ "_evaluateTypes:"
+ "_fetchURLForItemID:creatingPlaceholderIfMissing:completionHandlerWithInfo:"
+ "_generateDomainIDFromDSID:"
+ "_initWithFileURL:library:clientID:name:contentsURL:isBackup:revision:"
+ "_storageURLsAreInTransientState"
+ "aa_personID"
+ "accommodatePresentedItemEvictionWithCompletionHandler:"
+ "accountTypeWithAccountTypeIdentifier:"
+ "accountsWithAccountType:"
+ "addDomain:forProviderIdentifier:byImportingDirectoryAtURL:nonWrappedURL:userAllowedDBDrop:knownFolders:completionHandler:"
+ "addDomain:forProviderIdentifier:byImportingDirectoryAtURL:userAllowedDBDrop:knownFolders:completionHandler:"
+ "addDomain:forProviderIdentifier:byImportingDirectoryAtURL:userAllowedDBDrop:knownFolders:synchronous:completionHandler:"
+ "addDomain:userAllowedDBDrop:completionHandler:"
+ "additionWithName:inNameSpace:error:"
+ "allow-dmg"
+ "apfs"
+ "appLibraryCollectionForProviderDomainID:"
+ "backup"
+ "bundleRecordForAuditToken:error:"
+ "cachedProviderDomainWithID:cachePolicy:error:"
+ "checkLocationEligibilityForDomain:completionHandler:"
+ "checkLocationEligibilityForDomain:unsupportedReason:error:"
+ "com.apple.file-provider-resuming-sync-drop-local-changes#PX"
+ "com.apple.file-provider-sync_paused_bundle_id#PX"
+ "com.apple.fileprovider.pause-resume"
+ "com.apple.fileproviderd.FPCKService"
+ "com.apple.ubd.prsid"
+ "connection:handleInvocation:isReply:"
+ "currentUser"
+ "db_fp_unapplied_fields"
+ "db_fs_unapplied_fields"
+ "eligibleActionsForItems:domainCachePolicy:"
+ "enumeratedURL"
+ "fetchHierarchyForItemID:recursively:ignoreAlternateContentURL:reply:"
+ "fetchLatestVersionForItemAtURL:bundleID:completionHandler:"
+ "fetchProviderDomainForItem:cachePolicy:completionHandler:"
+ "fp_UUID"
+ "fp_UUIDWithObfuscation:"
+ "fp_annotateInvocation:withLogSection:"
+ "fp_annotateWithXPCSanitizer:"
+ "fp_backupManifestDirectory"
+ "fp_fpfsProviderDomainID:"
+ "fp_fpfsProviderDomainID:error:"
+ "fp_lmdURL"
+ "fp_userInfo"
+ "getReachabilityFlagsByCheckingNetwork"
+ "i16@?0^{fpfs_fileattrs={fpfs_item_handle=QQII*iI}{fpfs_metadata=ib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1Sq{timespec=qq}{timespec=qq}{timespec=qq}Q{fpfs_tag_data=^vQi}(?=II)QQq*q*^{fpfs_xattr}II*BB*Qii}*Q[0c]}8"
+ "initWithDisplayName:userInfo:volumeURL:"
+ "initWithIdentifier:displayName:userInfo:volumeURL:"
+ "initWithIdentifier:displayName:userInfo:volumeURL:pathRelativeToDocumentStorage:hidden:replicated:"
+ "invalidateCurrentContext:"
+ "isSharedIPad"
+ "itemIsSupportedSearchScopeWithCachePolicy:completionHandler:"
+ "listPausedURLsWithBundleID:completionHandler:"
+ "mainICloudDriveDomainID"
+ "newCollectionWithItemAtURL:error:"
+ "newCollectionWithItemAtURL:skipValidation:error:"
+ "nullableEnumeratedItemID"
+ "pauseSyncForItemAtURL:behavior:bundleID:completionHandler:"
+ "process-info-pidinfo"
+ "projectedFPFSMainICloudDriveDomainID"
+ "providerDomainForItem:cachePolicy:error:"
+ "providerDomainWithID:cachePolicy:completionHandler:"
+ "providerDomainWithID:cachePolicy:error:"
+ "reconnectAndReimportDomainWithCompletionHandler:"
+ "replacementObjectForXPCConnection:encoder:object:"
+ "restoreUserURL:cleanupOnSuccess:completionHandler:"
+ "resumeSyncForItemAtURL:behavior:bundleID:completionHandler:"
+ "rootURLForProviderDomainID:cachePolicy:error:"
+ "runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:completionHandler:"
+ "runningInSyncBubble"
+ "setEnumeratedURL:"
+ "setNullableEnumeratedItemID:"
+ "setStorageURLsAreInTransientState:"
+ "setupWithLog:forConnection:"
+ "stateDirectoryURLWithError:"
+ "stateDirectoryWithCompletionHandler:"
+ "storageURLsAreInTransientState"
+ "stringWithCString:encoding:"
+ "unsignedLongValue"
+ "url:%@ s:%@, al:%@"
+ "v24@0:8^v16"
+ "v28@?0@\"NSURL\"8B16@\"NSError\"20"
+ "v28@?0B8Q12@\"NSError\"20"
+ "v32@0:8@\"NSURL\"16@?<v@?BQ@\"NSError\">24"
+ "v32@?0@\"NSString\"8@\"FPSandboxingURLWrapper\"16@\"NSError\"24"
+ "v36@0:8@\"NSURL\"16B24@?<v@?B@\"NSError\">28"
+ "v36@0:8@\"NSXPCConnection\"16@\"NSInvocation\"24B32"
+ "v40@0:8@\"FPItemID\"16B24B28@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"NSURL\"16@\"NSString\"24@?<v@?@\"NSString\"@\"FPSandboxingURLWrapper\"@\"NSError\">32"
+ "v48@0:8@\"NSURL\"16Q24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@16Q24@32@?40"
+ "v60@0:8@16@24@32B40@44@?52"
+ "v64@0:8@16@24@32B40@44B52@?56"
+ "v68@0:8@\"NSFileProviderDomain\"16@\"NSString\"24@\"FPSandboxingURLWrapper\"32@\"NSURL\"40B48@\"NSArray\"52@?<v@?@\"NSString\"@\"NSError\">60"
+ "v68@0:8@16@24@32@40B48@52@?60"
+ "v72@0:8@\"NSString\"16@\"NSURL\"24@\"NSURL\"32Q40Q48Q56@?<v@?@\"NSString\"@\"FPCKStats\"@\"NSDictionary\"@\"NSError\">64"
+ "v72@0:8@16@24@32Q40Q48Q56@?64"
+ "versionOfItemAtURL:forPersistentIdentifier:"
- "\x01$\x13\x14"
- " cap:%c%c%c%c%c"
- "%@ has existing context, so there are two extension requests running concurrently"
- "-[FPXConnectionHandler makeNewContext]"
- "-[FPXEnumerator currentSyncAnchorWithCompletion:]"
- "-[FPXEnumerator enumerateChangesFromToken:suggestedBatchSize:reply:]"
- "-[FPXEnumerator enumerateItemsFromPage:suggestedPageSize:reply:]"
- "-[FPXExtensionContext _test_callFileProviderManagerAPIs:]"
- "-[FPXExtensionContext dropDomainWithCompletionHandler:]"
- "-[FPXExtensionContext dumpInternalStateToTermDumper:domainIdentifier:completionHandler:]"
- "-[FPXExtensionContext fetchAndStartEnumeratingWithSettings:observer:request:completionHandler:]"
- "-[FPXExtensionContext fetchCustomPushTopicsWithCompletionHandler:]"
- "-[FPXExtensionContext fetchDefaultContainerForBundleIdentifier:defaultName:inDomainIdentifier:reply:]"
- "-[FPXExtensionContext fetchHierarchyForItemID:recursively:reply:]"
- "-[FPXExtensionContext fetchHierarchyForItemID:recursively:reply:]_block_invoke"
- "-[FPXExtensionContext fetchTrashIdentifiersWithCompletionHandler:]"
- "-[FPXExtensionContext forceUpdateBlockedProcessNamesFromDomain:completionHandler:]"
- "-[FPXExtensionContext importDidFinishWithCompletionHandler:]"
- "-[FPXExtensionContext preflightTrashItemIDs:completionHandler:]"
- "-[FPXExtensionContext providePlaceholderAtURL:completionHandler:]"
- "-[FPXExtensionContext signalEnumeratorForMaterializedItemsWithCompletionHandler:]"
- "-[FPXExtensionContext signalEnumeratorForPendingItemsWithCompletionHandler:]"
- "-[FPXExtensionContext singleItemChange:changedFields:bounce:completionHandler:]"
- "-[FPXExtensionContext startOperation:toFetchThumbnailsForItemIdentifiers:size:completionHandler:]"
- "-[FPXExtensionContext startOperation:toFetchThumbnailsWithDictionary:size:completionHandler:]"
- "-[FPXExtensionContext trashItemAtURL:completionHandler:]"
- "-[FPXExtensionContext valuesForAttributes:forItemID:completionHandler:]"
- "-[FPXExtensionContext waitForStabilizationWithCompletionHandler:]"
- "/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/FPXConnectionHandler.m"
- "1703.80.16"
- "<%@ name:'%@' device:'%@' owner:'%@' size:%llu mtime:%@ etag:%@ url:'%@'"
- "<%@:%p id:\"%@\" name:\"%@\" urls(%d):%@ db:%@%@ state:%s%s%s%s%s%s%s features:%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s>"
- "@56@0:8@16@24@32@40B48B52"
- "D2D-restore-plugin"
- "D2DMigration"
- "DeviceClassNumber"
- "FPFS_Return"
- "Provider %@ returned invalid item %@ of class %@ with identifier %@: one of the required properties is missing or empty: %@. Break on %s to debug this."
- "T@\"FPItemID\",C,N,V_enumeratedItemID"
- "T@\"NSData\",R,C,N"
- "T@\"NSDate\",R,C,N"
- "T@\"NSError\",R,C,N"
- "T@\"NSNumber\",R,C"
- "T@\"NSNumber\",R,C,GisDownloadRequested"
- "T@\"NSNumber\",R,C,N"
- "T@\"NSSet\",R,C"
- "T@\"NSString\",R,C,N,VtypeIdentifier"
- "T@\"UTType\",R,C,N"
- "T@\"UTType\",R,C,N,VcontentType"
- "TB,GisSyncRoot"
- "TB,R,Gfp_isUbiquitous"
- "TB,R,GisHidden"
- "TB,R,N,Gfp_isLastModifiedByCurrentUser"
- "TB,R,N,GisDownloaded"
- "TB,R,N,GisDownloading"
- "TB,R,N,GisExcludedFromSync"
- "TB,R,N,GisMostRecentVersionDownloaded"
- "TB,R,N,GisShared"
- "TB,R,N,GisSharedByCurrentUser"
- "TB,R,N,GisTopLevelSharedItem"
- "TB,R,N,GisTrashed"
- "TB,R,N,GisUploaded"
- "TB,R,N,GisUploading"
- "TQ,R,N,Vcapabilities"
- "T{NSFileProviderTypeAndCreator=II},R,N"
- "[CRIT] Provider %{public}@ returned invalid item %@ of class %{public}@ with identifier %{public}@: one of the required properties is missing or empty: %{public}@. Break on %{public}s to debug this."
- "[DEBUG] fetching more changes"
- "[DEBUG] ipc: %@, reply of %s %@"
- "[DEBUG] ipc: %@, reply of %s %@, %@"
- "[DEBUG] ipc: %@, reply of %s %@, %@, %@"
- "[DEBUG] ipc: %@, reply of %s %@, %@, %@, %@, %lu, %@"
- "[DEBUG] ipc: %@, reply of %s %@, %@, %@, %lu, %@"
- "[DEBUG] ipc: %@, reply of %s %@, 0x%lx, %{bool}d, %@, %@"
- "[DEBUG] ipc: %@, reply of %s %@, 0x%x, %{bool}d, %@, %@"
- "[DEBUG] ipc: %@, reply of %s %{bool}d, %@"
- "[DEBUG] no last boot timestamp saved in the defaults, we can't check if the device has rebooted"
- "[DEBUG] ┏%llx flushing pending updates for %@"
- "[DEBUG] ┏%llx ipc: %@ %s "
- "[DEBUG] ┏%llx ipc: %@ %s %@"
- "[DEBUG] ┏%llx ipc: %@ %s %@ fields=%x options=%x contentURL=%@"
- "[DEBUG] ┏%llx ipc: %@ %s %@, %@"
- "[DEBUG] ┏%llx ipc: %@ %s %@, %@, %@"
- "[DEBUG] ┏%llx ipc: %@ %s %@, %ld"
- "[DEBUG] ┏%llx ipc: %@ %s %@, %lu"
- "[DEBUG] ┏%llx ipc: %@ %s %@, %{bool}d"
- "[DEBUG] ┏%llx ipc: %@ %s %@, %{bool}d, %{bool}d"
- "[DEBUG] ┏%llx ipc: %@ %s %@, 0x%lx"
- "[DEBUG] ┏%llx ipc: %@ %s %@, estimated size=%lld"
- "[DEBUG] ┏%llx ipc: %@ %s %@, estimated size=%lld, symlink=%{bool}d"
- "[DEBUG] ┏%llx ipc: %@ %s %@: %@"
- "[DEBUG] ┏%llx ipc: %@ %s %d"
- "[ERROR] can't check location %@ eligibility. Not supported"
- "[INFO] accepting connection %@"
- "__FILEPROVIDER_BAD_ITEM__"
- "_evaluateTypes"
- "addDomain:forProviderIdentifier:byImportingDirectoryAtURL:knownFolders:completionHandler:"
- "addDomain:forProviderIdentifier:byImportingDirectoryAtURL:knownFolders:synchronous:completionHandler:"
- "addDomain:forProviderIdentifier:byImportingDirectoryAtURL:nonWrappedURL:knownFolders:completionHandler:"
- "bundleProxyForURL:"
- "checkLocationEligibilityForDomain:error:"
- "com.apple.fileprovider.ciconia"
- "com.apple.internal.fileprovider.in-place-collaboration"
- "eligibleActionsForItems:allowCachedDomain:"
- "fetchHierarchyForItemID:recursively:reply:"
- "fp_bundleURL"
- "i16@?0^{fpfs_fileattrs={fpfs_item_handle=QQII*iI}{fpfs_metadata=ib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1Sq{timespec=qq}{timespec=qq}{timespec=qq}Q{fpfs_tag_data=^vQi}(?=II)QQq*q*^{fpfs_xattr}II*BB*ii}*Q[0c]}8"
- "iCloudDrive"
- "initWithIdentifier:displayName:volumeURL:"
- "initWithIdentifier:displayName:volumeURL:pathRelativeToDocumentStorage:hidden:replicated:"
- "invalidateCurrentContext"
- "itemIsSupportedSearchScopeAllowingCache:completionHandler:"
- "kern.boottime"
- "provider"
- "v24@?0@\"NSFileVersion\"8@\"NSError\"16"
- "v36@0:8@\"FPItemID\"16B24@?<v@?@\"NSArray\"@\"NSError\">28"
- "v56@0:8@\"NSString\"16@\"NSDictionary\"24Q32Q40@?<v@?@\"NSString\"@\"FPCKStats\"@\"NSDictionary\"@\"NSError\">48"
- "v60@0:8@16@24@32@40B48@?52"
- "v64@0:8@\"NSFileProviderDomain\"16@\"NSString\"24@\"FPSandboxingURLWrapper\"32@\"NSURL\"40@\"NSArray\"48@?<v@?@\"NSString\"@\"NSError\">56"

```
