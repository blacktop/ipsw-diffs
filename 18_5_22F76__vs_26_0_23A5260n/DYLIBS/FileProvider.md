## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/FileProvider`

```diff

-2882.120.74.0.0
-  __TEXT.__text: 0x12b1c8
-  __TEXT.__auth_stubs: 0x1ce0
-  __TEXT.__objc_methlist: 0xdf6c
-  __TEXT.__const: 0x85e
-  __TEXT.__gcc_except_tab: 0x9f64
-  __TEXT.__cstring: 0x14132
-  __TEXT.__oslogstring: 0xd86e
-  __TEXT.__dlopen_cstrs: 0x79e
+3762.0.0.0.0
+  __TEXT.__text: 0x130848
+  __TEXT.__auth_stubs: 0x1d10
+  __TEXT.__objc_methlist: 0xe4f4
+  __TEXT.__const: 0x87e
+  __TEXT.__gcc_except_tab: 0xa1b0
+  __TEXT.__cstring: 0x147e2
+  __TEXT.__oslogstring: 0xdc26
+  __TEXT.__dlopen_cstrs: 0x79f
   __TEXT.__ustring: 0x21e
   __TEXT.__swift5_typeref: 0xb4
   __TEXT.__constg_swiftt: 0x60

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0x5490
+  __TEXT.__unwind_info: 0x5638
   __TEXT.__eh_frame: 0xa0
-  __TEXT.__objc_classname: 0x1ef9
-  __TEXT.__objc_methname: 0x23051
-  __TEXT.__objc_methtype: 0x6572
-  __TEXT.__objc_stubs: 0x138a0
-  __DATA_CONST.__got: 0xab0
-  __DATA_CONST.__const: 0x5ff8
-  __DATA_CONST.__objc_classlist: 0x650
+  __TEXT.__objc_classname: 0x2045
+  __TEXT.__objc_methname: 0x23b91
+  __TEXT.__objc_methtype: 0x6811
+  __TEXT.__objc_stubs: 0x13d40
+  __DATA_CONST.__got: 0xa90
+  __DATA_CONST.__const: 0x6088
+  __DATA_CONST.__objc_classlist: 0x690
   __DATA_CONST.__objc_catlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x278
+  __DATA_CONST.__objc_protolist: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b60
-  __DATA_CONST.__objc_protorefs: 0x140
-  __DATA_CONST.__objc_superrefs: 0x518
-  __DATA_CONST.__objc_arraydata: 0xaa0
-  __AUTH_CONST.__auth_got: 0xe80
-  __AUTH_CONST.__const: 0x1b48
-  __AUTH_CONST.__cfstring: 0x10d00
-  __AUTH_CONST.__objc_const: 0x22ea0
+  __DATA_CONST.__objc_selrefs: 0x6d08
+  __DATA_CONST.__objc_protorefs: 0x158
+  __DATA_CONST.__objc_superrefs: 0x550
+  __DATA_CONST.__objc_arraydata: 0xab0
+  __AUTH_CONST.__auth_got: 0xe98
+  __AUTH_CONST.__const: 0x1c08
+  __AUTH_CONST.__cfstring: 0x11080
+  __AUTH_CONST.__objc_const: 0x24740
   __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH_CONST.__objc_arrayobj: 0x180
-  __AUTH.__objc_data: 0x2d0
+  __AUTH_CONST.__objc_arrayobj: 0x198
+  __AUTH.__objc_data: 0x500
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0xfd4
-  __DATA.__data: 0x1ee8
-  __DATA.__bss: 0xa30
+  __DATA.__objc_ivar: 0x1080
+  __DATA.__data: 0x20c0
+  __DATA.__bss: 0xac0
   __DATA.__common: 0x39
-  __DATA_DIRTY.__objc_data: 0x3c50
+  __DATA_DIRTY.__objc_data: 0x3ca0
   __DATA_DIRTY.__data: 0x2c1
-  __DATA_DIRTY.__bss: 0x378
+  __DATA_DIRTY.__bss: 0x380
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 13213DA6-85D8-3DDB-8322-E62BA15DC98F
-  Functions: 7022
-  Symbols:   22863
-  CStrings:  12036
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  UUID: C63BC528-62FB-31D8-BFA5-70C398DA37B7
+  Functions: 7169
+  Symbols:   23362
+  CStrings:  12248
 
Symbols:
+ +[FPSearchOnServerEnumerator enumeratorForQuery:providerDomainID:completionHandler:]
+ +[FPSearchOnServerRequestDescriptor supportsSecureCoding]
+ +[FPSearchOnServerResult supportsSecureCoding]
+ +[NSURL(FPAdditions) fp_additionalContainerPathsForBookmarks]
+ +[NSURL(FPAdditions) fp_additionalContainerPathsForBookmarks].cold.1
+ +[NSURL(FPAdditions) fp_uncachedContainerURLForSecurityApplicationGroupIdentifier:forPrimaryPersona:]
+ +[NSURL(FPAdditions) fp_uncachedContainerURLForSecurityApplicationGroupIdentifier:forPrimaryPersona:].cold.1
+ -[FPAppMetadata initWithBundleID:displayName:documentsURL:providerDomainID:isManaged:]
+ -[FPDaemonConnection checkErrorAgainstDiagnosticsJson:inputError:errorDirection:jobCode:underlying:completionHandler:]
+ -[FPDaemonConnection enumerateSearchResultForRequest:providerDomainID:completionHandler:]
+ -[FPDaemonConnection pauseIndexingFor:completionHandler:]
+ -[FPDaemonConnection resumeIndexingFor:completionHandler:]
+ -[FPDaemonConnection runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:contentBarrier:completionHandler:]
+ -[FPDaemonConnection setIndexingEnabled:forDomainIdentifier:providerIdentifier:completionHandler:]
+ -[FPItem isSyncPaused]
+ -[FPItem overrideFields:ofItem:].cold.64
+ -[FPItem overrideFields:ofItem:].cold.65
+ -[FPItem overrideFields:ofItem:].cold.66
+ -[FPItem providerParentItemID]
+ -[FPItem providerParentItemIdentifier]
+ -[FPItem setSupportsUploadWithFailOnConflict:]
+ -[FPItem setSyncPaused:]
+ -[FPItem supportsUploadWithFailOnConflict]
+ -[FPNSFileProviderItemHelper fp_supportedSyncControls]
+ -[FPNotifyCacheDelegate cache:willEvictObject:]
+ -[FPProviderDomain setSupportsSearchOnServer:]
+ -[FPProviderDomain supportsSearchOnServer]
+ -[FPSearchOnServerEnumerator .cxx_destruct]
+ -[FPSearchOnServerEnumerator cancelOnQueue]
+ -[FPSearchOnServerEnumerator cancelOnQueue].cold.1
+ -[FPSearchOnServerEnumerator cancel]
+ -[FPSearchOnServerEnumerator checkFinished]
+ -[FPSearchOnServerEnumerator checkFinished].cold.1
+ -[FPSearchOnServerEnumerator finishProviderDomainID:]
+ -[FPSearchOnServerEnumerator getNextResultSynchronouslyWithCompletionHandler:]
+ -[FPSearchOnServerEnumerator getNextResultSynchronouslyWithCompletionHandler:].cold.1
+ -[FPSearchOnServerEnumerator initWithQuery:domainIDs:]
+ -[FPSearchOnServerEnumerator nextResultsWithCompletionHandler:]
+ -[FPSearchOnServerEnumerator requestResultsFromEnumerator:providerDomainID:atPage:]
+ -[FPSearchOnServerEnumerator signalGroup]
+ -[FPSearchOnServerRequestDescriptor .cxx_destruct]
+ -[FPSearchOnServerRequestDescriptor encodeWithCoder:]
+ -[FPSearchOnServerRequestDescriptor initWithCoder:]
+ -[FPSearchOnServerRequestDescriptor initWithQuery:maxNumberOfResults:]
+ -[FPSearchOnServerRequestDescriptor maxNumberOfResults]
+ -[FPSearchOnServerRequestDescriptor query]
+ -[FPSearchOnServerResult .cxx_destruct]
+ -[FPSearchOnServerResult contentModificationDate]
+ -[FPSearchOnServerResult contentType]
+ -[FPSearchOnServerResult creationDate]
+ -[FPSearchOnServerResult description]
+ -[FPSearchOnServerResult documentSize]
+ -[FPSearchOnServerResult encodeWithCoder:]
+ -[FPSearchOnServerResult filename]
+ -[FPSearchOnServerResult initWithCoder:]
+ -[FPSearchOnServerResult initWithCoder:].cold.1
+ -[FPSearchOnServerResult initWithCoder:].cold.2
+ -[FPSearchOnServerResult initWithCoder:].cold.3
+ -[FPSearchOnServerResult initWithCoder:].cold.4
+ -[FPSearchOnServerResult initWithCoder:].cold.5
+ -[FPSearchOnServerResult itemIdentifier]
+ -[FPSearchOnServerResult lastUsedDate]
+ -[FPSearchOnServerResult rankingHint]
+ -[FPSearchOnServerResult toSearchableItem]
+ -[FPSearchOnServerResult(Internal) initWithFilename:creationDate:contentModificationDate:lastUsedDate:contentType:documentSize:itemIdentifier:providerID:domainIdentifier:]
+ -[FPSpotlightIndexOneBatchOperation searchableItems]
+ -[FPSpotlightIndexOneBatchOperation setSearchableItems:]
+ -[FPSpotlightIndexer pause]
+ -[FPSpotlightIndexer resume]
+ -[FPXExtensionContext enumerateSearchResultForRequest:completionHandler:]
+ -[FPXExtensionContext enumerateSearchResultForRequest:completionHandler:].cold.1
+ -[FPXExtensionContext searchEnumeratorWasInvalidated:]
+ -[FPXPCAutomaticErrorProxy forwardInvocation:].cold.1
+ -[FPXPCAutomaticErrorProxy generateSignposts]
+ -[FPXPCAutomaticErrorProxy setGenerateSignposts:]
+ -[FPXSearchEnumerator .cxx_destruct]
+ -[FPXSearchEnumerator _invalidateSync]
+ -[FPXSearchEnumerator _invalidateSync].cold.1
+ -[FPXSearchEnumerator dealloc]
+ -[FPXSearchEnumerator dealloc].cold.1
+ -[FPXSearchEnumerator enumerateSearchResultsForObserver:startingAtPage:]
+ -[FPXSearchEnumerator initWithDomainContext:vendorEnumerator:queue:maxNumberOfResults:]
+ -[FPXSearchEnumerator invalidateVendorEnumeration]
+ -[FPXSearchEnumerator invalidate]
+ -[FPXSearchEnumeratorObserver .cxx_destruct]
+ -[FPXSearchEnumeratorObserver didEnumerateSearchResults:]
+ -[FPXSearchEnumeratorObserver finishEnumeratingUpToPage:]
+ -[FPXSearchEnumeratorObserver finishEnumeratingWithError:]
+ -[FPXSearchEnumeratorObserver initWithMaxNumberOfResults:completionHandler:]
+ -[FPXSearchEnumeratorObserver maxNumberOfResults]
+ -[FPXWrappedSearchEnumeratorObserver .cxx_destruct]
+ -[FPXWrappedSearchEnumeratorObserver didEnumerateSearchResults:]
+ -[FPXWrappedSearchEnumeratorObserver finishEnumeratingUpToPage:]
+ -[FPXWrappedSearchEnumeratorObserver finishEnumeratingWithError:]
+ -[FPXWrappedSearchEnumeratorObserver initWithTarget:maxNumberOfResults:providerID:domainIdentifier:]
+ -[FPXWrappedSearchEnumeratorObserver maxNumberOfResults]
+ -[FPXWrappedSearchEnumeratorObserver setMaxNumberOfResults:]
+ -[NSFileProviderDomain setSupportsStringSearchRequest:]
+ -[NSFileProviderDomain supportsStringSearchRequest]
+ -[NSFileProviderRequest continuationToken]
+ -[NSFileProviderStringSearchRequest .cxx_destruct]
+ -[NSFileProviderStringSearchRequest initWithQuery:]
+ -[NSFileProviderStringSearchRequest query]
+ -[NSURL(CopyFile) fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:ignoreVFSSkipMtime:completion:]
+ -[NSURL(CopyFile) fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:shouldCopyAppleDouble:ignoreVFSSkipMtime:completion:]
+ -[NSURL(FPAdditions) fp_matchesApplicationDataOrGroupContainerURL:]
+ -[NSURL(FPAdditions) fp_matchesFileProviderHeuristics:options:]
+ -[NSURL(FPAdditions) fp_matchesFileProviderHeuristics:options:].cold.1
+ -[NSURL(FPAdditions) fp_matchesOtherBookmarkContainersURL:]
+ GCC_except_table108
+ GCC_except_table165
+ GCC_except_table166
+ GCC_except_table173
+ GCC_except_table174
+ GCC_except_table179
+ GCC_except_table186
+ GCC_except_table189
+ GCC_except_table194
+ GCC_except_table195
+ GCC_except_table206
+ GCC_except_table207
+ GCC_except_table210
+ GCC_except_table228
+ GCC_except_table229
+ GCC_except_table235
+ GCC_except_table238
+ GCC_except_table243
+ GCC_except_table249
+ GCC_except_table254
+ GCC_except_table255
+ GCC_except_table259
+ GCC_except_table260
+ GCC_except_table264
+ GCC_except_table267
+ GCC_except_table272
+ GCC_except_table297
+ GCC_except_table298
+ GCC_except_table299
+ GCC_except_table350
+ GCC_except_table368
+ GCC_except_table377
+ GCC_except_table392
+ GCC_except_table429
+ GCC_except_table431
+ GCC_except_table77
+ GCC_except_table79
+ _FPExpensiveRequestWithContinuationTokenError
+ _FPFeatureFlagBGSTImprovementsIsEnabled
+ _FPFeatureFlagIndexAllRemoteItemsIsEnabled
+ _FPFeatureFlagResolverIsEnabled
+ _FPFetchLatestRemoteVersionOfItemAtURL
+ _FPFilePausedWithNoFilePresenter
+ _FPIsFileIndexerEnabled
+ _FPIsFileIndexerEnabled.enabled
+ _FPIsFileIndexerEnabled.once_token
+ _FPPauseSyncForItemAtURL
+ _FPPerformWithDefaultPersona.cold.1
+ _FPResumeSyncForItemAtURLWithBehavior
+ _FPUnrevivableItemError
+ _FPUploadAndReturnLocalVersionOfUbiquitousItemAtURLWithConflictResolutionPolicy
+ _FPUploadLocalVersionOfUbiquitousItemAtURLWithConflictResolutionPolicy
+ _FPXSearchEnumeratorObserverXPCInterface
+ _FPXSearchEnumeratorObserverXPCInterface.cold.1
+ _FPXSearchEnumeratorObserverXPCInterface.interface
+ _FPXSearchEnumeratorObserverXPCInterface.once
+ _FPXSearchEnumeratorXPCInterface
+ _FPXSearchEnumeratorXPCInterface.cold.1
+ _FPXSearchEnumeratorXPCInterface.interface
+ _FPXSearchEnumeratorXPCInterface.once
+ _NSFileProviderErrorExpensiveRequest
+ _NSFileProviderErrorExpensiveRequestContinuationTokenKey
+ _NSFileProviderErrorExpensiveRequestIsRecursiveKey
+ _NSFileProviderErrorRecoveryLocationItemIdentifierKey
+ _NSFileProviderErrorRetryAfterKey
+ _NSFileProviderErrorUnrevivableItem
+ _NSURLUbiquitousItemIsSyncPausedKey
+ _NSURLUbiquitousItemSupportedSyncControlsKey
+ _OBJC_CLASS_$_FPNotifyCacheDelegate
+ _OBJC_CLASS_$_FPSearchOnServerEnumerator
+ _OBJC_CLASS_$_FPSearchOnServerRequestDescriptor
+ _OBJC_CLASS_$_FPSearchOnServerResult
+ _OBJC_CLASS_$_FPXSearchEnumerator
+ _OBJC_CLASS_$_FPXSearchEnumeratorObserver
+ _OBJC_CLASS_$_FPXWrappedSearchEnumeratorObserver
+ _OBJC_CLASS_$_NSFileProviderStringSearchRequest
+ _OBJC_IVAR_$_FPItem._supportsUploadWithFailOnConflict
+ _OBJC_IVAR_$_FPItem._syncPaused
+ _OBJC_IVAR_$_FPProviderDomain._supportsSearchOnServer
+ _OBJC_IVAR_$_FPSearchOnServerEnumerator._extensionLifetimeExtenders
+ _OBJC_IVAR_$_FPSearchOnServerEnumerator._finished
+ _OBJC_IVAR_$_FPSearchOnServerEnumerator._inflightRequests
+ _OBJC_IVAR_$_FPSearchOnServerEnumerator._initialRequests
+ _OBJC_IVAR_$_FPSearchOnServerEnumerator._nextPages
+ _OBJC_IVAR_$_FPSearchOnServerEnumerator._prefetchedResults
+ _OBJC_IVAR_$_FPSearchOnServerEnumerator._query
+ _OBJC_IVAR_$_FPSearchOnServerEnumerator._queue
+ _OBJC_IVAR_$_FPSearchOnServerEnumerator._waitGroup
+ _OBJC_IVAR_$_FPSearchOnServerRequestDescriptor._maxNumberOfResults
+ _OBJC_IVAR_$_FPSearchOnServerRequestDescriptor._query
+ _OBJC_IVAR_$_FPSearchOnServerResult._contentModificationDate
+ _OBJC_IVAR_$_FPSearchOnServerResult._contentType
+ _OBJC_IVAR_$_FPSearchOnServerResult._creationDate
+ _OBJC_IVAR_$_FPSearchOnServerResult._documentSize
+ _OBJC_IVAR_$_FPSearchOnServerResult._domainIdentifier
+ _OBJC_IVAR_$_FPSearchOnServerResult._filename
+ _OBJC_IVAR_$_FPSearchOnServerResult._itemIdentifier
+ _OBJC_IVAR_$_FPSearchOnServerResult._lastUsedDate
+ _OBJC_IVAR_$_FPSearchOnServerResult._providerID
+ _OBJC_IVAR_$_FPSearchOnServerResult._rankingHint
+ _OBJC_IVAR_$_FPSpotlightIndexOneBatchOperation._searchableItems
+ _OBJC_IVAR_$_FPSpotlightIndexer._paused
+ _OBJC_IVAR_$_FPSpotlightIndexer._pausedStateSemaphore
+ _OBJC_IVAR_$_FPXExtensionContext._runningSearchEnumerators
+ _OBJC_IVAR_$_FPXPCAutomaticErrorProxy._generateSignposts
+ _OBJC_IVAR_$_FPXSearchEnumerator._domainContext
+ _OBJC_IVAR_$_FPXSearchEnumerator._maxNumberOfResults
+ _OBJC_IVAR_$_FPXSearchEnumerator._queue
+ _OBJC_IVAR_$_FPXSearchEnumerator._vendorEnumerator
+ _OBJC_IVAR_$_FPXSearchEnumeratorObserver._completionHandler
+ _OBJC_IVAR_$_FPXSearchEnumeratorObserver._maxNumberOfResults
+ _OBJC_IVAR_$_FPXSearchEnumeratorObserver._resultsBuffer
+ _OBJC_IVAR_$_FPXWrappedSearchEnumeratorObserver._domainIdentifier
+ _OBJC_IVAR_$_FPXWrappedSearchEnumeratorObserver._maxNumberOfResults
+ _OBJC_IVAR_$_FPXWrappedSearchEnumeratorObserver._providerIdentifier
+ _OBJC_IVAR_$_FPXWrappedSearchEnumeratorObserver._target
+ _OBJC_IVAR_$_NSFileProviderDomain._supportsStringSearchRequest
+ _OBJC_IVAR_$_NSFileProviderRequest._continuationToken
+ _OBJC_IVAR_$_NSFileProviderStringSearchRequest._query
+ _OBJC_METACLASS_$_FPNotifyCacheDelegate
+ _OBJC_METACLASS_$_FPSearchOnServerEnumerator
+ _OBJC_METACLASS_$_FPSearchOnServerRequestDescriptor
+ _OBJC_METACLASS_$_FPSearchOnServerResult
+ _OBJC_METACLASS_$_FPXSearchEnumerator
+ _OBJC_METACLASS_$_FPXSearchEnumeratorObserver
+ _OBJC_METACLASS_$_FPXWrappedSearchEnumeratorObserver
+ _OBJC_METACLASS_$_NSFileProviderStringSearchRequest
+ __OBJC_$_CLASS_METHODS_FPSearchOnServerEnumerator
+ __OBJC_$_CLASS_METHODS_FPSearchOnServerRequestDescriptor
+ __OBJC_$_CLASS_METHODS_FPSearchOnServerResult
+ __OBJC_$_CLASS_PROP_LIST_FPSearchOnServerRequestDescriptor
+ __OBJC_$_CLASS_PROP_LIST_FPSearchOnServerResult
+ __OBJC_$_INSTANCE_METHODS_FPNotifyCacheDelegate
+ __OBJC_$_INSTANCE_METHODS_FPSearchOnServerEnumerator
+ __OBJC_$_INSTANCE_METHODS_FPSearchOnServerRequestDescriptor
+ __OBJC_$_INSTANCE_METHODS_FPSearchOnServerResult(Internal)
+ __OBJC_$_INSTANCE_METHODS_FPXSearchEnumerator
+ __OBJC_$_INSTANCE_METHODS_FPXSearchEnumeratorObserver
+ __OBJC_$_INSTANCE_METHODS_FPXWrappedSearchEnumeratorObserver
+ __OBJC_$_INSTANCE_METHODS_NSFileProviderStringSearchRequest
+ __OBJC_$_INSTANCE_VARIABLES_FPSearchOnServerEnumerator
+ __OBJC_$_INSTANCE_VARIABLES_FPSearchOnServerRequestDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_FPSearchOnServerResult
+ __OBJC_$_INSTANCE_VARIABLES_FPXSearchEnumerator
+ __OBJC_$_INSTANCE_VARIABLES_FPXSearchEnumeratorObserver
+ __OBJC_$_INSTANCE_VARIABLES_FPXWrappedSearchEnumeratorObserver
+ __OBJC_$_INSTANCE_VARIABLES_NSFileProviderStringSearchRequest
+ __OBJC_$_PROP_LIST_FPNotifyCacheDelegate
+ __OBJC_$_PROP_LIST_FPSearchOnServerRequestDescriptor
+ __OBJC_$_PROP_LIST_FPSearchOnServerResult
+ __OBJC_$_PROP_LIST_FPXPCAutomaticErrorProxy.105
+ __OBJC_$_PROP_LIST_FPXSearchEnumerator
+ __OBJC_$_PROP_LIST_FPXSearchEnumeratorObserver
+ __OBJC_$_PROP_LIST_FPXWrappedSearchEnumeratorObserver
+ __OBJC_$_PROP_LIST_NSFileProviderSearchEnumerationObserver
+ __OBJC_$_PROP_LIST_NSFileProviderSearchResult
+ __OBJC_$_PROP_LIST_NSFileProviderStringSearchRequest
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FPXSearchEnumerator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FPXSearchEnumeratorObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSFileProviderSearchEnumerationObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSFileProviderSearchResult
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSFileProviderSearching_Legacy
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSCacheDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FPXSearchEnumerator
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FPXSearchEnumeratorObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCacheDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSFileProviderSearchEnumerationObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSFileProviderSearchResult
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSFileProviderSearching_Legacy
+ __OBJC_$_PROTOCOL_REFS_FPXSearchEnumerator
+ __OBJC_$_PROTOCOL_REFS_FPXSearchEnumeratorObserver
+ __OBJC_$_PROTOCOL_REFS_NSCacheDelegate
+ __OBJC_$_PROTOCOL_REFS_NSFileProviderSearchEnumerationObserver
+ __OBJC_$_PROTOCOL_REFS_NSFileProviderSearching_Legacy
+ __OBJC_CLASS_PROTOCOLS_$_FPNotifyCacheDelegate
+ __OBJC_CLASS_PROTOCOLS_$_FPSearchOnServerRequestDescriptor
+ __OBJC_CLASS_PROTOCOLS_$_FPSearchOnServerResult
+ __OBJC_CLASS_PROTOCOLS_$_FPXSearchEnumerator
+ __OBJC_CLASS_PROTOCOLS_$_FPXSearchEnumeratorObserver
+ __OBJC_CLASS_PROTOCOLS_$_FPXWrappedSearchEnumeratorObserver
+ __OBJC_CLASS_RO_$_FPNotifyCacheDelegate
+ __OBJC_CLASS_RO_$_FPSearchOnServerEnumerator
+ __OBJC_CLASS_RO_$_FPSearchOnServerRequestDescriptor
+ __OBJC_CLASS_RO_$_FPSearchOnServerResult
+ __OBJC_CLASS_RO_$_FPXSearchEnumerator
+ __OBJC_CLASS_RO_$_FPXSearchEnumeratorObserver
+ __OBJC_CLASS_RO_$_FPXWrappedSearchEnumeratorObserver
+ __OBJC_CLASS_RO_$_NSFileProviderStringSearchRequest
+ __OBJC_LABEL_PROTOCOL_$_FPXSearchEnumerator
+ __OBJC_LABEL_PROTOCOL_$_FPXSearchEnumeratorObserver
+ __OBJC_LABEL_PROTOCOL_$_NSCacheDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSFileProviderSearchEnumerationObserver
+ __OBJC_LABEL_PROTOCOL_$_NSFileProviderSearchResult
+ __OBJC_LABEL_PROTOCOL_$_NSFileProviderSearching_Legacy
+ __OBJC_METACLASS_RO_$_FPNotifyCacheDelegate
+ __OBJC_METACLASS_RO_$_FPSearchOnServerEnumerator
+ __OBJC_METACLASS_RO_$_FPSearchOnServerRequestDescriptor
+ __OBJC_METACLASS_RO_$_FPSearchOnServerResult
+ __OBJC_METACLASS_RO_$_FPXSearchEnumerator
+ __OBJC_METACLASS_RO_$_FPXSearchEnumeratorObserver
+ __OBJC_METACLASS_RO_$_FPXWrappedSearchEnumeratorObserver
+ __OBJC_METACLASS_RO_$_NSFileProviderStringSearchRequest
+ __OBJC_PROTOCOL_$_FPXSearchEnumerator
+ __OBJC_PROTOCOL_$_FPXSearchEnumeratorObserver
+ __OBJC_PROTOCOL_$_NSCacheDelegate
+ __OBJC_PROTOCOL_$_NSFileProviderSearchEnumerationObserver
+ __OBJC_PROTOCOL_$_NSFileProviderSearchResult
+ __OBJC_PROTOCOL_$_NSFileProviderSearching_Legacy
+ __OBJC_PROTOCOL_REFERENCE_$_FPXSearchEnumerator
+ __OBJC_PROTOCOL_REFERENCE_$_FPXSearchEnumeratorObserver
+ __OBJC_PROTOCOL_REFERENCE_$_NSFileProviderSearching_Legacy
+ ___100-[FPSpotlightIndexer _indexOneBatchFromAnchor:toAnchor:updatedItems:deletedItems:completionHandler:]_block_invoke.90
+ ___100-[FPSpotlightIndexer _indexOneBatchFromAnchor:toAnchor:updatedItems:deletedItems:completionHandler:]_block_invoke.90.cold.1
+ ___107-[NSFileProviderExtension(CreateItem) createItemBasedOnTemplate:fields:contents:options:completionHandler:]_block_invoke.346
+ ___107-[NSFileProviderExtension(CreateItem) createItemBasedOnTemplate:fields:contents:options:completionHandler:]_block_invoke.353
+ ___129-[NSURL(CopyFile) fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:shouldCopyAppleDouble:ignoreVFSSkipMtime:completion:]_block_invoke
+ ___129-[NSURL(CopyFile) fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:shouldCopyAppleDouble:ignoreVFSSkipMtime:completion:]_block_invoke.cold.1
+ ___27-[FPSpotlightIndexer pause]_block_invoke
+ ___27-[FPSpotlightIndexer pause]_block_invoke.97
+ ___27-[FPSpotlightIndexer pause]_block_invoke.cold.1
+ ___27-[FPSpotlightIndexer pause]_block_invoke.cold.2
+ ___27-[FPSpotlightIndexer pause]_block_invoke.cold.3
+ ___28-[FPSpotlightIndexer resume]_block_invoke
+ ___28-[FPSpotlightIndexer resume]_block_invoke.cold.1
+ ___28-[FPSpotlightIndexer resume]_block_invoke.cold.2
+ ___33-[FPXSearchEnumerator invalidate]_block_invoke
+ ___36-[FPSearchOnServerEnumerator cancel]_block_invoke
+ ___46-[FPXPCAutomaticErrorProxy forwardInvocation:]_block_invoke.16
+ ___46-[FPXPCAutomaticErrorProxy forwardInvocation:]_block_invoke.16.cold.1
+ ___46-[FPXPCAutomaticErrorProxy forwardInvocation:]_block_invoke.18
+ ___46-[FPXPCAutomaticErrorProxy forwardInvocation:]_block_invoke.18.cold.1
+ ___47-[FPProviderMonitor addObserver:forProviderID:]_block_invoke.79
+ ___54-[FPSearchOnServerEnumerator initWithQuery:domainIDs:]_block_invoke
+ ___54-[FPSearchOnServerEnumerator initWithQuery:domainIDs:]_block_invoke_2
+ ___54-[FPSearchOnServerEnumerator initWithQuery:domainIDs:]_block_invoke_3
+ ___54-[FPSearchOnServerEnumerator initWithQuery:domainIDs:]_block_invoke_3.cold.1
+ ___54-[FPXExtensionContext searchEnumeratorWasInvalidated:]_block_invoke
+ ___58-[FPSpotlightIndexer _indexOneBatchWithCompletionHandler:]_block_invoke.84
+ ___61+[NSURL(FPAdditions) fp_additionalContainerPathsForBookmarks]_block_invoke
+ ___63-[FPSearchOnServerEnumerator nextResultsWithCompletionHandler:]_block_invoke
+ ___63-[FPSearchOnServerEnumerator nextResultsWithCompletionHandler:]_block_invoke_2
+ ___63-[FPSearchOnServerEnumerator nextResultsWithCompletionHandler:]_block_invoke_2.cold.1
+ ___64-[FPXWrappedSearchEnumeratorObserver didEnumerateSearchResults:]_block_invoke
+ ___66+[FPItemToURLResourcesConverter dictionaryFromItem:requestedKeys:]_block_invoke.377
+ ___73-[FPXExtensionContext enumerateSearchResultForRequest:completionHandler:]_block_invoke
+ ___83-[FPSearchOnServerEnumerator requestResultsFromEnumerator:providerDomainID:atPage:]_block_invoke
+ ___83-[FPSearchOnServerEnumerator requestResultsFromEnumerator:providerDomainID:atPage:]_block_invoke_2
+ ___83-[FPSearchOnServerEnumerator requestResultsFromEnumerator:providerDomainID:atPage:]_block_invoke_3
+ ___FILEPROVIDER_SEARCH_OBSERVER_TOO_MANY_ITEMS__
+ ___FPCrossDeviceItemIDForItemID_block_invoke.76
+ ___FPFetchLatestRemoteVersionOfItemAtURL_block_invoke
+ ___FPIsFileIndexerEnabled_block_invoke
+ ___FPItemIDFromCrossDeviceItemID_block_invoke.102
+ ___FPItemURLForCrossDeviceItemID_block_invoke.84
+ ___FPItemURLForCrossDeviceItemID_block_invoke.84.cold.1
+ ___FPItemURLForCrossDeviceItemID_block_invoke.89
+ ___FPItemURLForCrossDeviceItemID_block_invoke.89.cold.1
+ ___FPItemURLForCrossDeviceItemID_block_invoke.90
+ ___FPResumeSyncForItemAtURLWithBehavior_block_invoke
+ ___FPUploadAndReturnLocalVersionOfUbiquitousItemAtURLWithConflictResolutionPolicy_block_invoke
+ ___FPUploadLocalVersionOfUbiquitousItemAtURLWithConflictResolutionPolicy_block_invoke
+ ___FPXSearchEnumeratorObserverXPCInterface_block_invoke
+ ___FPXSearchEnumeratorXPCInterface_block_invoke
+ ___block_descriptor_243_e8_32s40s48s56s64bs72r_e5_v8?0ls32l8s40l8s48l8r72l8s56l8s64l8
+ ___block_descriptor_40_e8_32bs_e35_v24?0"NSFileVersion"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e38_16?0"<NSFileProviderSearchResult>"8ls32l8
+ ___block_descriptor_48_e8_32bs40r_e17_v16?0"NSError"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e35_v24?0"NSFileVersion"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e70_v32?0"<FPXSearchEnumerator>"8"<FPDLifetimeServicing>"16"NSError"24ls32l8s40l8
+ ___block_descriptor_52_e8_32bs_e205_i16?0^{fpfs_fileattrs={fpfs_item_handle=QQII*iI}{fpfs_metadata=ib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1Sq{timespec=qq}{timespec=qq}{timespec=qq}Q{fpfs_tag_data=^vQi}(?=II)QQq*q*^{fpfs_xattr}II*BB*QICii}Q[0c]}8ls32l8
+ ___block_descriptor_56_e8_32bs40w48w_e20_v24?08"NSError"16lw40l8s32l8w48l8
+ ___block_descriptor_56_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e40_v32?0"NSArray"8"NSData"16"NSError"24ls32l8s40l8s48l8
+ ___block_descriptor_87_e8_32s40s48s56s_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_99_e8_32s40s48s56bs64r72w_e22_v16?0"NSInvocation"8ls32l8s40l8w72l8s56l8s48l8r64l8
+ ___block_literal_global.10
+ ___block_literal_global.105
+ ___block_literal_global.121
+ ___block_literal_global.125
+ ___block_literal_global.135
+ ___block_literal_global.156
+ ___block_literal_global.16
+ ___block_literal_global.184
+ ___block_literal_global.193
+ ___block_literal_global.255
+ ___block_literal_global.285
+ ___block_literal_global.287
+ ___block_literal_global.289
+ ___block_literal_global.292
+ ___block_literal_global.295
+ ___block_literal_global.310
+ ___block_literal_global.33
+ ___block_literal_global.34
+ ___block_literal_global.375
+ ___block_literal_global.42
+ ___block_literal_global.426
+ ___block_literal_global.435
+ ___block_literal_global.50
+ ___block_literal_global.52
+ ___block_literal_global.579
+ ___block_literal_global.581
+ ___block_literal_global.67
+ ___block_literal_global.80
+ ___block_literal_global.85
+ ___fpfs_supports_bgst_improvements_block_invoke
+ ___fpfs_supports_indexAllRemoteItems_block_invoke
+ ___fpfs_supports_local_storage_less_block_invoke
+ ___telemetry_default_log_block_invoke
+ __fpfs_fgethandle
+ __fpfs_is_meaningful_item
+ __fset_dataless_cmpfs_xattr.cold.1
+ __fset_dataless_cmpfs_xattr_only.cold.1
+ __os_signpost_emit_with_name_impl
+ __supportedSyncControlsForVendorItem
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_FileProvider
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_FileProvider
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_FileProvider
+ _forwardInvocation:.internal_build
+ _forwardInvocation:.once_token
+ _fp_additionalContainerPathsForBookmarks.additionalContainerPathsForBookmarks
+ _fp_additionalContainerPathsForBookmarks.onceToken
+ _fpfs_fgethandle_nocheck
+ _fpfs_fileattrs_with_path
+ _fpfs_ignore_thread_skip_mtime_iopolicy
+ _fpfs_ignore_thread_skip_mtime_iopolicy.cold.1
+ _fpfs_ignore_thread_skip_mtime_iopolicy.cold.2
+ _fpfs_is_seed_build.is_seed_build
+ _fpfs_parse_cmpfs_xattr.cold.1
+ _fpfs_purge_single_file
+ _fpfs_purge_single_file.cold.1
+ _fpfs_restore_thread_skip_mtime_iopolicy
+ _fpfs_restore_thread_skip_mtime_iopolicy.cold.1
+ _fpfs_supports_bgst_improvements
+ _fpfs_supports_bgst_improvements.cold.1
+ _fpfs_supports_bgst_improvements.feature_enabled
+ _fpfs_supports_bgst_improvements.once_token
+ _fpfs_supports_indexAllRemoteItems
+ _fpfs_supports_indexAllRemoteItems.cold.1
+ _fpfs_supports_indexAllRemoteItems.feature_enabled
+ _fpfs_supports_indexAllRemoteItems.once_token
+ _fpfs_supports_local_storage_less
+ _fpfs_supports_local_storage_less.cold.1
+ _fpfs_supports_local_storage_less.feature_enabled
+ _fpfs_supports_local_storage_less.once_token
+ _gatherDefaultPersona
+ _isProviderIDForeground:.cacheDelegate
+ _kFileProviderSearchOnServerEntitlement
+ _objc_msgSend$_invalidateSync
+ _objc_msgSend$_setError
+ _objc_msgSend$addBarrierBlock:
+ _objc_msgSend$cancelOnQueue
+ _objc_msgSend$checkErrorAgainstDiagnosticsJson:inputError:errorDirection:jobCode:underlying:completionHandler:
+ _objc_msgSend$checkFinished
+ _objc_msgSend$currentVersionOfItemAtURL:
+ _objc_msgSend$didEnumerateSearchResults:
+ _objc_msgSend$enumerateSearchResultForRequest:providerDomainID:completionHandler:
+ _objc_msgSend$enumerateSearchResultsForObserver:startingAtPage:
+ _objc_msgSend$enumeratorForQuery:providerDomainID:completionHandler:
+ _objc_msgSend$finishProviderDomainID:
+ _objc_msgSend$fp_additionalContainerPathsForBookmarks
+ _objc_msgSend$fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:ignoreVFSSkipMtime:completion:
+ _objc_msgSend$fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:shouldCopyAppleDouble:ignoreVFSSkipMtime:completion:
+ _objc_msgSend$fp_matchesApplicationDataOrGroupContainerURL:
+ _objc_msgSend$fp_matchesFileProviderHeuristics:options:
+ _objc_msgSend$fp_matchesOtherBookmarkContainersURL:
+ _objc_msgSend$fp_uncachedContainerURLForSecurityApplicationGroupIdentifier:forPrimaryPersona:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$getNextResultSynchronouslyWithCompletionHandler:
+ _objc_msgSend$hasError
+ _objc_msgSend$initWithFilename:creationDate:contentModificationDate:lastUsedDate:contentType:documentSize:itemIdentifier:providerID:domainIdentifier:
+ _objc_msgSend$initWithMaxNumberOfResults:completionHandler:
+ _objc_msgSend$initWithQuery:maxNumberOfResults:
+ _objc_msgSend$initWithTarget:maxNumberOfResults:providerID:domainIdentifier:
+ _objc_msgSend$isSyncPaused
+ _objc_msgSend$listAllPersonaWithAttributes
+ _objc_msgSend$nextResultsWithCompletionHandler:
+ _objc_msgSend$parentFormerItemID
+ _objc_msgSend$pauseIndexingFor:completionHandler:
+ _objc_msgSend$position
+ _objc_msgSend$providerParentItemID
+ _objc_msgSend$requestResultsFromEnumerator:providerDomainID:atPage:
+ _objc_msgSend$resumeIndexingFor:completionHandler:
+ _objc_msgSend$runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:contentBarrier:completionHandler:
+ _objc_msgSend$searchEnumeratorWasInvalidated:
+ _objc_msgSend$searchableItems
+ _objc_msgSend$setGenerateSignposts:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setSearchableItems:
+ _objc_msgSend$setSupportsStringSearchRequest:
+ _objc_msgSend$signalGroup
+ _objc_msgSend$supportsStringSearchRequest
+ _objc_msgSend$supportsUploadWithFailOnConflict
+ _objc_msgSend$uploadLocalVersionOfItemAtURL:bundleID:conflictResolutionPolicy:completionHandler:
+ _openat_s
+ _os_signpost_enabled
+ _os_signpost_id_generate
+ _pthread_main_np
+ _telemetry_default_log
+ _telemetry_default_log.cold.1
+ _telemetry_default_log.logger
+ _telemetry_default_log.once
- +[NSURL(FPAdditions) fp_uncachedContainerURLForSecurityApplicationGroupIdentifier:].cold.1
- -[FPDaemonConnection checkErrorAgainstDiagnosticsJson:inputError:errorDirection:jobCode:completionHandler:]
- -[FPItemManager collectionForFolderItem:].cold.1
- -[FPProviderDomain iCloudAccountIdentifier]
- -[FPProviderDomain isFPFSiCloudDriveProvider]
- -[GSAddition(FPVersions) shouldBeForwardedToFileProvider]
- -[GSAddition(FPVersions) shouldBeForwardedToFileProvider].cold.1
- -[NSString(FPAdditions) fp_isLegacyCloudDocsIdentifier]
- -[NSURL(CopyFile) fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:completion:]
- -[NSURL(CopyFile) fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:shouldCopyAppleDouble:completion:]
- -[NSURL(FPAdditions) fp_matchesFileProviderHeuristics:].cold.1
- -[NSURL(FPConflictWinner) shouldBeForwardedToFileProvider]
- -[NSURL(FPConflictWinner) shouldBeForwardedToFileProvider].cold.1
- GCC_except_table163
- GCC_except_table164
- GCC_except_table167
- GCC_except_table172
- GCC_except_table175
- GCC_except_table180
- GCC_except_table183
- GCC_except_table184
- GCC_except_table188
- GCC_except_table193
- GCC_except_table202
- GCC_except_table203
- GCC_except_table208
- GCC_except_table213
- GCC_except_table214
- GCC_except_table230
- GCC_except_table231
- GCC_except_table237
- GCC_except_table242
- GCC_except_table248
- GCC_except_table251
- GCC_except_table256
- GCC_except_table257
- GCC_except_table262
- GCC_except_table263
- GCC_except_table268
- GCC_except_table293
- GCC_except_table294
- GCC_except_table295
- GCC_except_table346
- GCC_except_table364
- GCC_except_table373
- GCC_except_table388
- GCC_except_table425
- GCC_except_table427
- GCC_except_table80
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _CloudDocsLibrary
- _CloudDocsLibrary.cold.1
- _CloudDocsLibraryCore.frameworkLibrary
- _FPIsSpaceAttributionEnabledAndUsedByStorageUI
- _OBJC_CLASS_$_UMUserPersonaAttributes
- _SANDBOX_CHECK_ALLOW_APPROVAL
- _SANDBOX_CHECK_CANONICAL
- _SANDBOX_CHECK_NO_APPROVAL
- _SANDBOX_CHECK_POSIX_READABLE
- _StorageManagementFeatureFlagStorageUIV2IsEnabled
- __OBJC_$_PROP_LIST_FPXPCAutomaticErrorProxy.94
- __OBJC_$_PROP_LIST__SWFileProviderItem
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__SWFileProviderItem
- __OBJC_$_PROTOCOL_METHOD_TYPES__SWFileProviderItem
- __OBJC_$_PROTOCOL_REFS__SWFileProviderItem
- __OBJC_LABEL_PROTOCOL_$__SWFileProviderItem
- __OBJC_PROTOCOL_$__SWFileProviderItem
- ___100-[FPSpotlightIndexer _indexOneBatchFromAnchor:toAnchor:updatedItems:deletedItems:completionHandler:]_block_invoke.87
- ___107-[NSFileProviderExtension(CreateItem) createItemBasedOnTemplate:fields:contents:options:completionHandler:]_block_invoke.337
- ___107-[NSFileProviderExtension(CreateItem) createItemBasedOnTemplate:fields:contents:options:completionHandler:]_block_invoke.344
- ___110-[NSURL(CopyFile) fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:shouldCopyAppleDouble:completion:]_block_invoke
- ___110-[NSURL(CopyFile) fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:shouldCopyAppleDouble:completion:]_block_invoke.cold.1
- ___45-[NSURL(FPFSHelpers) fp_isDatalessWithError:]_block_invoke
- ___46-[FPXPCAutomaticErrorProxy forwardInvocation:]_block_invoke.12
- ___46-[FPXPCAutomaticErrorProxy forwardInvocation:]_block_invoke.12.cold.1
- ___46-[FPXPCAutomaticErrorProxy forwardInvocation:]_block_invoke.cold.1
- ___47-[FPProviderMonitor addObserver:forProviderID:]_block_invoke.30
- ___58-[FPSpotlightIndexer _indexOneBatchWithCompletionHandler:]_block_invoke.81
- ___66+[FPItemToURLResourcesConverter dictionaryFromItem:requestedKeys:]_block_invoke.364
- ___CloudDocsLibraryCore_block_invoke
- ___FPCrossDeviceItemIDForItemID_block_invoke.72
- ___FPItemIDFromCrossDeviceItemID_block_invoke.98
- ___FPItemURLForCrossDeviceItemID_block_invoke.80
- ___FPItemURLForCrossDeviceItemID_block_invoke.80.cold.1
- ___FPItemURLForCrossDeviceItemID_block_invoke.85
- ___FPItemURLForCrossDeviceItemID_block_invoke.85.cold.1
- ___FPItemURLForCrossDeviceItemID_block_invoke.86
- ___block_descriptor_242_e8_32s40s48s56s64bs72r_e5_v8?0ls32l8s40l8s48l8r72l8s56l8s64l8
- ___block_descriptor_48_e8_32bs40w_e20_v24?08"NSError"16lw40l8s32l8
- ___block_descriptor_48_e8_32s40r_e5_i8?0ls32l8r40l8
- ___block_descriptor_52_e8_32bs_e206_i16?0^{fpfs_fileattrs={fpfs_item_handle=QQII*iI}{fpfs_metadata=ib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1Sq{timespec=qq}{timespec=qq}{timespec=qq}Q{fpfs_tag_data=^vQi}(?=II)QQq*q*^{fpfs_xattr}II*BB*QICii}*Q[0c]}8ls32l8
- ___block_descriptor_56_e5_i8?0l
- ___block_descriptor_60_e8_32r_e5_i8?0lr32l8
- ___block_descriptor_69_e8_32s40s48s_e17_v16?0"NSError"8ls32l8s40l8s48l8
- ___block_descriptor_84_e5_i8?0l
- ___block_descriptor_89_e8_32s40s48s56bs64r72w_e22_v16?0"NSInvocation"8ls32l8s40l8w72l8s56l8s48l8r64l8
- ___block_literal_global.13
- ___block_literal_global.159
- ___block_literal_global.164
- ___block_literal_global.199
- ___block_literal_global.247
- ___block_literal_global.249
- ___block_literal_global.276
- ___block_literal_global.279
- ___block_literal_global.282
- ___block_literal_global.283
- ___block_literal_global.306
- ___block_literal_global.35
- ___block_literal_global.36
- ___block_literal_global.395
- ___block_literal_global.404
- ___block_literal_global.44
- ___block_literal_global.468
- ___block_literal_global.47
- ___block_literal_global.547
- ___block_literal_global.549
- ___cachedFrameworkOverridingObjects_block_invoke.cold.2
- ___fpfs_lp_sandbox_check_block_invoke
- ___fpfs_lp_sandbox_check_by_audit_token_block_invoke
- ___fpfs_lp_sandbox_extension_issue_file_block_invoke
- ___fpfs_supports_long_paths_block_invoke
- ___fpfs_supports_speculative_set_block_invoke
- ___fpfs_t_is_evictable_at_block_invoke
- __get_current_user_uuid
- __get_current_user_uuid.cold.1
- __openbyid_longpaths
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_FileProvider
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_FileProvider
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_FileProvider
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_FileProvider
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_FileProvider
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_FileProvider
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_FileProvider
- _audit_stringCloudDocs
- _faccessat
- _fpfs_evict.cold.5
- _fpfs_lp_faccessat
- _fpfs_lp_fsctl
- _fpfs_lp_fstatat
- _fpfs_lp_mkdirat
- _fpfs_lp_openat
- _fpfs_lp_sandbox_check
- _fpfs_lp_sandbox_check_by_audit_token
- _fpfs_lp_sandbox_extension_issue_file
- _fpfs_lp_unlinkat
- _fpfs_supports_long_paths
- _fpfs_supports_long_paths.cold.1
- _fpfs_supports_long_paths.feature_enabled
- _fpfs_supports_long_paths.once_token
- _fpfs_supports_speculative_set.cold.1
- _fpfs_supports_speculative_set.feature_enabled
- _fpfs_supports_speculative_set.once_token
- _fpfs_t_is_evictable_at
- _objc_msgSend$br_lastEditorDeviceName
- _objc_msgSend$br_lastEditorNameComponents
- _objc_msgSend$br_markResolvedWithError:
- _objc_msgSend$checkErrorAgainstDiagnosticsJson:inputError:errorDirection:jobCode:completionHandler:
- _objc_msgSend$fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:completion:
- _objc_msgSend$fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:shouldCopyAppleDouble:completion:
- _objc_msgSend$isFPFSiCloudDriveProvider
- _objc_msgSend$personaAttributesForPersonaType:
- _objc_msgSend$shouldBeForwardedToFileProvider
CStrings:
+ "\t"
+ "      change token: %s\n"
+ "      description: %@\n"
+ "      operation: %s\n"
+ " paused"
+ ",searchLegacy"
+ ",searchOnServer"
+ "-[FPSpotlightIndexer _indexOneBatchFromAnchor:toAnchor:updatedItems:deletedItems:completionHandler:]_block_invoke"
+ "-[FPXExtensionContext enumerateSearchResultForRequest:completionHandler:]"
+ "-[FPXExtensionContext enumerateSearchResultForRequest:completionHandler:]_block_invoke"
+ "-[FPXSearchEnumerator _invalidateSync]"
+ "-[FPXSearchEnumerator dealloc]"
+ "/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/search-on-server/FPXSearchEnumeratorObserver.m"
+ "3762"
+ "<%@: %p, %@ id=%@ vid=%@ (%@%@%@%@%@%@%@%@%@%@%@%@)%@%@>"
+ "<%@: itemIdentifier:%@, filename: %@>"
+ "<%@:%@ %p %@%@%@ [%lu ops]>"
+ "<%@:%p id:\"%@\" name:\"%@\" urls(%d%s):%@ db:%@%@ state:%s%s%s%s%s%s%s%s features:%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%@%@>"
+ "@\"<NSFileProviderSearchEnumerationObserver>\""
+ "@\"<NSFileProviderSearchEnumerator>\""
+ "@\"<NSFileProviderSearchEnumerator>\"24@0:8@\"NSFileProviderStringSearchRequest\"16"
+ "@16@?0@\"<NSFileProviderSearchResult>\"8"
+ "@32@0:8@16q24"
+ "@32@0:8q16@?24"
+ "@48@0:8@16q24@32@40"
+ "@60@0:8@16@24Q32B40B44B48@?52"
+ "@88@0:8@16@24@32@40@48@56@64@72@80"
+ "B28@0:8I16Q20"
+ "Caches"
+ "ClientXPC"
+ "FPNotifyCacheDelegate"
+ "FPSearchOnServerEnumerator"
+ "FPSearchOnServerRequestDescriptor"
+ "FPSearchOnServerResult"
+ "FPSearchOnServerResult.m"
+ "FPXSearchEnumerator"
+ "FPXSearchEnumeratorObserver"
+ "FPXWrappedSearchEnumeratorObserver"
+ "FileIndexer"
+ "FilePausedWithNoFilePresenter"
+ "IndexerDaemon"
+ "Internal"
+ "Library"
+ "Library/Mail"
+ "Library/SMS/Attachments"
+ "LocalStorageLess"
+ "NSCacheDelegate"
+ "NSFileProviderErrorExpensiveRequestContinuationTokenKey"
+ "NSFileProviderErrorExpensiveRequestIsRecursiveKey"
+ "NSFileProviderErrorRecoveryLocationItemIdentifierKey"
+ "NSFileProviderErrorRetryAfterKey"
+ "NSFileProviderSearchEnumerationObserver"
+ "NSFileProviderSearchResult"
+ "NSFileProviderSearching_Legacy"
+ "NSFileProviderStringSearchRequest"
+ "Resolver"
+ "Search enumerator attempted to return more than %lu items in one page/batch. Use the -maxNumberOfResults method to determine a reasonable number of items per page. Break on %s to debug this."
+ "SupportsStringSearchRequest"
+ "T@\"NSArray\",&,N,V_searchableItems"
+ "T@\"NSData\",R,N,V_continuationToken"
+ "T@\"NSDate\",R,C,N"
+ "T@\"NSDate\",R,C,N,V_contentModificationDate"
+ "T@\"NSDate\",R,C,N,V_creationDate"
+ "T@\"NSDate\",R,C,N,V_lastUsedDate"
+ "T@\"NSNumber\",R,C,N"
+ "T@\"NSNumber\",R,C,N,V_documentSize"
+ "T@\"NSString\",R,N,V_query"
+ "T@\"UTType\",R,C,N"
+ "T@\"UTType\",R,C,N,V_contentType"
+ "TB,N,GisSyncPaused,V_syncPaused"
+ "TB,N,V_generateSignposts"
+ "TB,N,V_supportsSearchOnServer"
+ "TB,N,V_supportsUploadWithFailOnConflict"
+ "TB,V_supportsStringSearchRequest"
+ "Td,R,N,V_rankingHint"
+ "Tq,N,V_maxNumberOfResults"
+ "Tq,R,N,V_maxNumberOfResults"
+ "[DEBUG] %@: already paused"
+ "[DEBUG] %@: pausing"
+ "[DEBUG] %@: resuming"
+ "[DEBUG] Illegal state - caller said there were prefetched results, but there were not"
+ "[DEBUG] 🆘 Finished searching all domains"
+ "[DEBUG] 🆘 cancel called multiple times"
+ "[DEBUG] 🆘 expecting prefetched results, or all domains finished"
+ "[ERROR] Failed finding the default persona"
+ "[ERROR] Unable to disable IOPOL_TYPE_VFS_SKIP_MTIME_UPDATE for the thread"
+ "[ERROR] Unable to get IOPOL_TYPE_VFS_SKIP_MTIME_UPDATE for the thread"
+ "[ERROR] Unable to restore IOPOL_TYPE_VFS_SKIP_MTIME_UPDATE for the thread"
+ "[ERROR] can't get home dir path size %{errno}d"
+ "[ERROR] enumerator for query returned nil enumerator, %@"
+ "[ERROR] 🆘 Couldn't decode domainIdentifier in search result"
+ "[ERROR] 🆘 Couldn't decode filename in search result"
+ "[ERROR] 🆘 Couldn't decode itemIdentifier in search result"
+ "[ERROR] 🆘 Couldn't decode providerID in search result"
+ "__FILEPROVIDER_SEARCH_OBSERVER_TOO_MANY_ITEMS__"
+ "_completionHandler"
+ "_continuationToken"
+ "_extensionLifetimeExtenders"
+ "_generateSignposts"
+ "_inflightRequests"
+ "_initialRequests"
+ "_invalidateSync"
+ "_maxNumberOfResults"
+ "_nextPages"
+ "_paused"
+ "_pausedStateSemaphore"
+ "_prefetchedResults"
+ "_query"
+ "_rankingHint"
+ "_resultsBuffer"
+ "_runningSearchEnumerators"
+ "_searchableItems"
+ "_setError"
+ "_supportsSearchOnServer"
+ "_supportsStringSearchRequest"
+ "_supportsUploadWithFailOnConflict"
+ "_syncPaused"
+ "_waitGroup"
+ "addBarrierBlock:"
+ "behavior"
+ "bgstImprovements"
+ "cache:willEvictObject:"
+ "cancelOnQueue"
+ "checkErrorAgainstDiagnosticsJson:inputError:errorDirection:jobCode:underlying:completionHandler:"
+ "checkFinished"
+ "com.apple.FileIndexer"
+ "com.apple.fileindexerd.%sDevelopment"
+ "com.apple.fileprovider.before-bounce#PX"
+ "com.apple.fileproviderd.debug.enable-resolver"
+ "com.apple.private.fileprovider.search-on-server"
+ "continuationToken"
+ "currentVersionOfItemAtURL:"
+ "didEnumerateSearchResults:"
+ "enableTelemetry=YES rc=%{public,signpost.telemetry:number1,name=rc}d mainThread=%{public,signpost.telemetry:number2,name=isMainThread}d"
+ "enumerateSearchResultForRequest:completionHandler:"
+ "enumerateSearchResultForRequest:providerDomainID:completionHandler:"
+ "enumerateSearchResultsForObserver:startingAtPage:"
+ "enumeratorForQuery:providerDomainID:completionHandler:"
+ "finishProviderDomainID:"
+ "fp_additionalContainerPathsForBookmarks"
+ "fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:ignoreVFSSkipMtime:completion:"
+ "fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:shouldCopyAppleDouble:ignoreVFSSkipMtime:completion:"
+ "fp_matchesApplicationDataOrGroupContainerURL:"
+ "fp_matchesFileProviderHeuristics:options:"
+ "fp_matchesOtherBookmarkContainersURL:"
+ "fp_supportedSyncControls"
+ "fp_uncachedContainerURLForSecurityApplicationGroupIdentifier:forPrimaryPersona:"
+ "generateSignposts"
+ "getBytes:range:"
+ "getNextResultSynchronouslyWithCompletionHandler:"
+ "hasError"
+ "i16@?0^{fpfs_fileattrs={fpfs_item_handle=QQII*iI}{fpfs_metadata=ib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1Sq{timespec=qq}{timespec=qq}{timespec=qq}Q{fpfs_tag_data=^vQi}(?=II)QQq*q*^{fpfs_xattr}II*BB*QICii}Q[0c]}8"
+ "indexAllRemoteItems"
+ "initWithBundleID:displayName:documentsURL:providerDomainID:isManaged:"
+ "initWithDomainContext:vendorEnumerator:queue:maxNumberOfResults:"
+ "initWithFilename:creationDate:contentModificationDate:lastUsedDate:contentType:documentSize:itemIdentifier:providerID:domainIdentifier:"
+ "initWithMaxNumberOfResults:completionHandler:"
+ "initWithQuery:"
+ "initWithQuery:domainIDs:"
+ "initWithQuery:maxNumberOfResults:"
+ "initWithTarget:maxNumberOfResults:providerID:domainIdentifier:"
+ "isSyncPaused"
+ "kMDItemLogicalSize"
+ "listAllPersonaWithAttributes"
+ "maxNumberOfResults"
+ "nextResultsWithCompletionHandler:"
+ "pauseIndexingFor:completionHandler:"
+ "position"
+ "providerParentItemID"
+ "providerParentItemIdentifier"
+ "query"
+ "query=%{public,signpost.telemetry:string1,name=selector}s"
+ "rankingHint"
+ "requestResultsFromEnumerator:providerDomainID:atPage:"
+ "resumeIndexingFor:completionHandler:"
+ "runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:contentBarrier:completionHandler:"
+ "searchEnumeratorForStringSearchRequest:"
+ "searchEnumeratorWasInvalidated:"
+ "searchableItems"
+ "setGenerateSignposts:"
+ "setMaxNumberOfResults:"
+ "setPosition:"
+ "setSearchableItems:"
+ "setSupportsSearchOnServer:"
+ "setSupportsStringSearchRequest:"
+ "setSupportsUploadWithFailOnConflict:"
+ "setSyncPaused:"
+ "signalGroup"
+ "strongIndexOperation"
+ "supportsSearchOnServer"
+ "supportsStringSearchRequest"
+ "supportsUploadWithFailOnConflict"
+ "syncPaused"
+ "telemetry"
+ "uploadLocalVersionOfItemAtURL:bundleID:conflictResolutionPolicy:completionHandler:"
+ "v24@?0@\"NSFileVersion\"8@\"NSError\"16"
+ "v32@0:8@\"<NSFileProviderSearchEnumerationObserver>\"16@\"NSData\"24"
+ "v32@0:8@\"FPSearchOnServerRequestDescriptor\"16@?<v@?@\"<FPXSearchEnumerator>\"@\"NSError\">24"
+ "v32@0:8@\"NSCache\"16@24"
+ "v32@?0@\"<FPXSearchEnumerator>\"8@\"<FPDLifetimeServicing>\"16@\"NSError\"24"
+ "v32@?0@\"NSArray\"8@\"NSData\"16@\"NSError\"24"
+ "v40@0:8@\"FPSearchOnServerRequestDescriptor\"16@\"NSString\"24@?<v@?@\"<FPXSearchEnumerator>\"@\"<FPDLifetimeServicing>\"@\"NSError\">32"
+ "v48@0:8@\"NSURL\"16@\"NSString\"24q32@?<v@?@\"NSError\">40"
+ "v64@0:8@\"NSString\"16@\"NSError\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@?<v@?@\"NSString\"@\"NSError\">56"
+ "v80@0:8@\"NSString\"16@\"NSURL\"24@\"NSURL\"32Q40Q48Q56q64@?<v@?@\"NSString\"@\"FPCKStats\"@\"NSDictionary\"@\"NSError\">72"
+ "v80@0:8@16@24@32Q40Q48Q56q64@?72"
+ "\xb1"
+ "\xf0R"
- "    change token: %s\n"
- "    operation: %s\n"
- "2882.120.74"
- "<%@: %p, %@ id=%@ vid=%@ (%@%@%@%@%@%@%@%@%@%@%@)%@%@>"
- "<%@:%@ %p %@%@ [%lu ops]>"
- "<%@:%p id:\"%@\" name:\"%@\" urls(%d%s):%@ db:%@%@ state:%s%s%s%s%s%s%s%s features:%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%@%@>"
- "@52@0:8@16@24Q32B40@?44"
- "GSAddition+FPVersions.m"
- "LongPaths"
- "SpeculativeSet"
- "StorageUIV2"
- "[DEBUG] Ignoring new world icloud drive override when fpfs is not enabled"
- "[ERROR] Failed to dlopen CloudDocs Private Framework, process will most likely crash!"
- "_SWFileProviderItem"
- "br_lastEditorDeviceName"
- "br_lastEditorNameComponents"
- "br_markResolvedWithError:"
- "checkErrorAgainstDiagnosticsJson:inputError:errorDirection:jobCode:completionHandler:"
- "clouddocs"
- "clouddocsmanaged"
- "com.apple.fileprovider.before-bounce#P"
- "com.apple.icloud.drive.fileprovider.override"
- "fgetattrlist (LP) failed (%s)"
- "fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:completion:"
- "fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:shouldCopyAppleDouble:completion:"
- "fp_isLegacyCloudDocsIdentifier"
- "fpfs_fsgetpath failed (%s)"
- "i16@?0^{fpfs_fileattrs={fpfs_item_handle=QQII*iI}{fpfs_metadata=ib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1Sq{timespec=qq}{timespec=qq}{timespec=qq}Q{fpfs_tag_data=^vQi}(?=II)QQq*q*^{fpfs_xattr}II*BB*QICii}*Q[0c]}8"
- "iCloudAccountIdentifier"
- "isFPFSiCloudDriveProvider"
- "personaAttributesForPersonaType:"
- "shouldBeForwardedToFileProvider"
- "softlink:r:path:/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs"
- "v56@0:8@\"NSString\"16@\"NSError\"24@\"NSNumber\"32@\"NSNumber\"40@?<v@?@\"NSString\"@\"NSError\">48"
- "v72@0:8@\"NSString\"16@\"NSURL\"24@\"NSURL\"32Q40Q48Q56@?<v@?@\"NSString\"@\"FPCKStats\"@\"NSDictionary\"@\"NSError\">64"
- "void *CloudDocsLibrary(void)"
- "\xa1"
- "\xf02"

```
