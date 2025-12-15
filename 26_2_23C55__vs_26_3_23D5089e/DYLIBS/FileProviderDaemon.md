## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon`

```diff

-3882.60.27.0.0
-  __TEXT.__text: 0xa19e48
+3882.80.11.0.0
+  __TEXT.__text: 0xa19e74
   __TEXT.__auth_stubs: 0x5ce0
   __TEXT.__objc_methlist: 0x9cec
   __TEXT.__const: 0x29870
-  __TEXT.__cstring: 0x43c1d
+  __TEXT.__cstring: 0x43ccd
   __TEXT.__oslogstring: 0x1e832
-  __TEXT.__gcc_except_tab: 0xe92c
+  __TEXT.__gcc_except_tab: 0xe94c
   __TEXT.__ustring: 0x176e
   __TEXT.__dlopen_cstrs: 0xc3
   __TEXT.__constg_swiftt: 0x12d84

   __DATA_CONST.__objc_selrefs: 0x6230
   __DATA_CONST.__objc_protorefs: 0x188
   __DATA_CONST.__objc_superrefs: 0x288
-  __DATA_CONST.__objc_arraydata: 0xf0
+  __DATA_CONST.__objc_arraydata: 0x128
   __AUTH_CONST.__auth_got: 0x2e80
   __AUTH_CONST.__const: 0x44980
-  __AUTH_CONST.__cfstring: 0x7180
+  __AUTH_CONST.__cfstring: 0x7200
   __AUTH_CONST.__objc_const: 0x2c418
-  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH.__objc_data: 0x21d0

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A8DF6F23-2E33-337F-852B-2C7F2C433E00
+  UUID: B96FABA3-0EFF-3386-9249-3655EF89DA94
   Functions: 29611
   Symbols:   25594
-  CStrings:  13800
+  CStrings:  13808
 
Symbols:
+ ___100-[FPDXPCServicer _test_importItemsPendingScanningProviderProgressForDomainWithID:completionHandler:]_block_invoke.523
+ ___100-[FPDXPCServicer uploadLocalVersionOfItemAtURL:bundleID:conflictResolutionPolicy:completionHandler:]_block_invoke.584
+ ___100-[FPDXPCServicer uploadLocalVersionOfItemAtURL:bundleID:conflictResolutionPolicy:completionHandler:]_block_invoke.584.cold.1
+ ___106-[FPDXPCServicer createItemBasedOnTemplate:fields:urlWrapper:options:bounceOnCollision:completionHandler:]_block_invoke.221
+ ___106-[FPDXPCServicer createItemBasedOnTemplate:fields:urlWrapper:options:bounceOnCollision:completionHandler:]_block_invoke.221.cold.1
+ ___106-[FPDXPCServicer createItemBasedOnTemplate:fields:urlWrapper:options:bounceOnCollision:completionHandler:]_block_invoke.221.cold.2
+ ___109-[FPDXPCServicer evictItemAtURL:evenIfEnumeratingFP:andClearACLForConsumer:evictionReason:completionHandler:]_block_invoke.163
+ ___109-[FPDXPCServicer evictItemAtURL:evenIfEnumeratingFP:andClearACLForConsumer:evictionReason:completionHandler:]_block_invoke.163.cold.1
+ ___109-[FPDXPCServicer evictItemAtURL:evenIfEnumeratingFP:andClearACLForConsumer:evictionReason:completionHandler:]_block_invoke.163.cold.2
+ ___114-[FPDXPCServicer documentURLFromItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.216
+ ___120-[FPDXPCServicer startAccessingServiceWithName:itemID:domain:connection:enumerateEntitlementRequired:completionHandler:]_block_invoke.134
+ ___120-[FPDXPCServicer startAccessingServiceWithName:itemID:domain:connection:enumerateEntitlementRequired:completionHandler:]_block_invoke.134.cold.1
+ ___125-[FPDXPCServicer fetchFSItemsForItemIdentifiers:providerIdentifier:domainIdentifier:materializingIfNeeded:completionHandler:]_block_invoke.233
+ ___126-[FPDXPCServicer documentURLFromBookmarkableString:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.208
+ ___133-[FPDXPCServicer runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:contentBarrier:completionHandler:]_block_invoke.358
+ ___133-[FPDXPCServicer runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:contentBarrier:completionHandler:]_block_invoke.358.cold.1
+ ___133-[FPDXPCServicer runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:contentBarrier:completionHandler:]_block_invoke.361
+ ___139-[FPDXPCServicer addDomain:forProviderIdentifier:byImportingDirectoryAtURL:nonWrappedURL:userAllowedDBDrop:knownFolders:completionHandler:]_block_invoke.306
+ ___139-[FPDXPCServicer addDomain:forProviderIdentifier:byImportingDirectoryAtURL:nonWrappedURL:userAllowedDBDrop:knownFolders:completionHandler:]_block_invoke.307
+ ___139-[FPDXPCServicer addDomain:forProviderIdentifier:byImportingDirectoryAtURL:nonWrappedURL:userAllowedDBDrop:knownFolders:completionHandler:]_block_invoke.320
+ ___158-[FPDXPCServicer getURLForContainerWithItemID:inDataScopeDomainWithIdentifier:documentsScopeDomainIdentifier:documentsFolderItemIdentifier:completionHandler:]_block_invoke.266
+ ___158-[FPDXPCServicer getURLForContainerWithItemID:inDataScopeDomainWithIdentifier:documentsScopeDomainIdentifier:documentsFolderItemIdentifier:completionHandler:]_block_invoke.267
+ ___50-[FPDXPCServicer pinItemWithID:completionHandler:]_block_invoke.167
+ ___51-[FPDXPCServicer trashItemAtURL:completionHandler:]_block_invoke.235
+ ___52-[FPDXPCServicer unpinItemWithID:completionHandler:]_block_invoke.171
+ ___53-[FPDXPCServicer pauseIndexingFor:completionHandler:]_block_invoke.495
+ ___54-[FPDXPCServicer removeDomain:mode:completionHandler:]_block_invoke.323
+ ___54-[FPDXPCServicer removeDomain:mode:completionHandler:]_block_invoke.324
+ ___54-[FPDXPCServicer resumeIndexingFor:completionHandler:]_block_invoke.496
+ ___55-[FPDXPCServicer _test_getDBOptions:completionHandler:]_block_invoke.513
+ ___55-[FPDXPCServicer itemForURL:options:completionHandler:]_block_invoke.228
+ ___55-[FPDXPCServicer updateLastUsedDate:completionHandler:]_block_invoke.242
+ ___55-[FPDXPCServicer updateLastUsedDate:completionHandler:]_block_invoke.244
+ ___57-[FPDXPCServicer resolveConflictAtURL:completionHandler:]_block_invoke.303
+ ___57-[FPDXPCServicer stateForDomainWithID:completionHandler:]_block_invoke.356
+ ___58-[FPDXPCServicer clearDiagnosticsState:completionHandler:]_block_invoke.288
+ ___59-[FPDXPCServicer _test_purgerBarrierWithCompletionHandler:]_block_invoke.530
+ ___59-[FPDXPCServicer _test_purgerBarrierWithCompletionHandler:]_block_invoke.530.cold.1
+ ___59-[FPDXPCServicer appHasNonUploadedFiles:completionHandler:]_block_invoke.369
+ ___59-[FPDXPCServicer getSavedDiagnosticsFor:completionHandler:]_block_invoke.287
+ ___61-[FPDXPCServicer forceIngestionForItemIDs:completionHandler:]_block_invoke.217
+ ___62-[FPDXPCServicer fetchPathComponentsForURL:completionHandler:]_block_invoke.269
+ ___62-[FPDXPCServicer setPutBackInfoOnItemAtURL:completionHandler:]_block_invoke.238
+ ___62-[FPDXPCServicer startDownloadingItemAtURL:completionHandler:]_block_invoke.156
+ ___62-[FPDXPCServicer startDownloadingItemAtURL:completionHandler:]_block_invoke.160
+ ___63-[FPDXPCServicer fetchDaemonOperationIDsWithCompletionHandler:]_block_invoke.450
+ ___65-[FPDXPCServicer _test_resetDBQueryStatistics:completionHandler:]_block_invoke.525
+ ___66-[FPDXPCServicer importProgressForDomainWithID:completionHandler:]_block_invoke.354
+ ___66-[FPDXPCServicer putBackURLForTrashedItemAtURL:completionHandler:]_block_invoke.237
+ ___67-[FPDXPCServicer _test_disableDBQueryStatistics:completionHandler:]_block_invoke.524
+ ___67-[FPDXPCServicer dumpTelemetryTo:providerFilter:completionHandler:]_block_invoke.427
+ ___67-[FPDXPCServicer evictItemWithID:evictionReason:completionHandler:]_block_invoke.164
+ ___68-[FPDXPCServicer dumpDatabaseAt:fullDump:writeTo:completionHandler:]_block_invoke.364
+ ___68-[FPDXPCServicer scheduleActionOperationWithInfo:completionHandler:]_block_invoke.448
+ ___69-[FPDXPCServicer valuesForAttributes:forItemAtURL:completionHandler:]_block_invoke.245
+ ___70-[FPDXPCServicer _test_triggerDatabaseError:domain:completionHandler:]_block_invoke.529
+ ___70-[FPDXPCServicer copyDatabaseForFPCKStartingAtPath:completionHandler:]_block_invoke.441
+ ___70-[FPDXPCServicer forceLatestVersionOnDiskForItemID:completionHandler:]_block_invoke.220
+ ___71-[FPDXPCServicer dumpStateTo:providerFilter:options:completionHandler:]_block_invoke.410
+ ___73-[FPDXPCServicer _test_getDBQueryStatistics:queryPlan:completionHandler:]_block_invoke.526
+ ___73-[FPDXPCServicer waitForChangesOnItemsBelowItemWithID:completionHandler:]_block_invoke.444
+ ___74-[FPDXPCServicer removeAllDomainsForProviderIdentifier:completionHandler:]_block_invoke.325
+ ___74-[FPDXPCServicer removeAllDomainsForProviderIdentifier:completionHandler:]_block_invoke.325.cold.1
+ ___74-[FPDXPCServicer startAccessingServiceWithName:itemURL:completionHandler:]_block_invoke.461
+ ___75-[FPDXPCServicer removeDomainAndPreserveDataWithID:mode:completionHandler:]_block_invoke.321
+ ___75-[FPDXPCServicer removeDomainAndPreserveDataWithID:mode:completionHandler:]_block_invoke.322
+ ___76-[FPDXPCServicer fetchLatestVersionForItemAtURL:bundleID:completionHandler:]_block_invoke.574
+ ___76-[FPDXPCServicer pauseSyncForItemAtURL:behavior:bundleID:completionHandler:]_block_invoke.556
+ ___76-[FPDXPCServicer waitForStabilizationOfDomainWithID:mode:completionHandler:]_block_invoke.445
+ ___77-[FPDXPCServicer _performWithCheckedEnumerationAttributes:completionHandler:]_block_invoke.471
+ ___77-[FPDXPCServicer forceUpdateBlockedProcessNamesFromDomain:completionHandler:]_block_invoke.351
+ ___77-[FPDXPCServicer resumeSyncForItemAtURL:behavior:bundleID:completionHandler:]_block_invoke.568
+ ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.504
+ ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.504.cold.1
+ ___80-[FPDXPCServicer fetchProviderForShareURL:fallbackIdentifier:completionHandler:]_block_invoke.240
+ ___80-[FPDXPCServicer fetchProviderForShareURL:fallbackIdentifier:completionHandler:]_block_invoke.240.cold.1
+ ___80-[FPDXPCServicer fetchProviderForShareURL:fallbackIdentifier:completionHandler:]_block_invoke.240.cold.2
+ ___80-[FPDXPCServicer fetchProviderForShareURL:fallbackIdentifier:completionHandler:]_block_invoke.240.cold.3
+ ___80-[FPDXPCServicer fetchProviderForShareURL:fallbackIdentifier:completionHandler:]_block_invoke.240.cold.4
+ ___80-[FPDXPCServicer fetchProviderForShareURL:fallbackIdentifier:completionHandler:]_block_invoke.240.cold.5
+ ___80-[FPDXPCServicer getNumberOfNonMaterializedFilesInDomain:withCompletionHandler:]_block_invoke.587
+ ___80-[FPDXPCServicer getNumberOfNonMaterializedFilesInDomain:withCompletionHandler:]_block_invoke.587.cold.1
+ ___82-[FPDXPCServicer extendBookmarkForFileURL:toConsumerID:options:completionHandler:]_block_invoke.225
+ ___82-[FPDXPCServicer extendBookmarkForFileURL:toConsumerID:options:completionHandler:]_block_invoke.225.cold.1
+ ___82-[FPDXPCServicer extendBookmarkForFileURL:toConsumerID:options:completionHandler:]_block_invoke.225.cold.2
+ ___82-[FPDXPCServicer fetchAndStartEnumeratingWithSettings:observer:completionHandler:]_block_invoke.477
+ ___82-[FPDXPCServicer reimportItemsBelowItemWithID:markItemDataless:completionHandler:]_block_invoke.350
+ ___85-[FPDXPCServicer enumerateSearchResultForRequest:providerDomainID:completionHandler:]_block_invoke.466
+ ___86-[FPDXPCServicer setEnabled:forDomainIdentifier:providerIdentifier:completionHandler:]_block_invoke.347
+ ___88-[FPDXPCServicer listRemoteVersionsOfItemAtURL:includeCachedVersions:completionHandler:]_block_invoke.304
+ ___88-[FPDXPCServicer spotlightReindexAllItemsForBundleID:protectionClass:completionHandler:]_block_invoke.446
+ ___89-[FPDXPCServicer startProvidingItemAtURL:fromProviderID:forConsumerID:completionHandler:]_block_invoke.152
+ ___91-[FPDXPCServicer selectNewProviderDomain:knownFolders:skipReleasePrompt:completionHandler:]_block_invoke.172
+ ___91-[FPDXPCServicer setHiddenByUser:forDomainIdentifier:providerIdentifier:completionHandler:]_block_invoke.348
+ ___93-[FPDXPCServicer signalReindexCSIdentifiersByProviderDomainID:indexReason:completionHandler:]_block_invoke.497
+ ___93-[FPDXPCServicer signalReindexCSIdentifiersByProviderDomainID:indexReason:completionHandler:]_block_invoke.497.cold.1
+ ___93-[FPDXPCServicer signalReindexCSIdentifiersByProviderDomainID:indexReason:completionHandler:]_block_invoke.497.cold.2
+ ___94-[FPDXPCServicer setIndexingEnabled:forDomainIdentifier:providerIdentifier:completionHandler:]_block_invoke.349
+ ___95-[FPDXPCServicer triggerDiagnosticsFor:triggeringError:uiOnly:useDiagnostic:completionHandler:]_block_invoke.270
+ ___95-[FPDXPCServicer triggerDiagnosticsFor:triggeringError:uiOnly:useDiagnostic:completionHandler:]_block_invoke.271
+ ___95-[FPDXPCServicer triggerDiagnosticsFor:triggeringError:uiOnly:useDiagnostic:completionHandler:]_block_invoke.271.cold.1
+ ___95-[FPDXPCServicer triggerDiagnosticsFor:triggeringError:uiOnly:useDiagnostic:completionHandler:]_block_invoke.272
+ ___96-[FPDXPCServicer _test_importItemsPendingScanningDiskProgressForDomainWithID:completionHandler:]_block_invoke.520
+ ___98-[FPDXPCServicer _test_importItemsPendingReconciliationProgressForDomainWithID:completionHandler:]_block_invoke.517
+ ___98-[FPDXPCServicer spotlightReindexItemsWithIdentifiers:bundleID:protectionClass:completionHandler:]_block_invoke.447
+ ___99-[FPDXPCServicer startOperation:toFetchIconsForAppBundleIDs:requestedSize:scale:completionHandler:]_block_invoke.250
+ ___99-[FPDXPCServicer startOperation:toFetchIconsForAppBundleIDs:requestedSize:scale:completionHandler:]_block_invoke.250.cold.1
+ ___99-[FPDXPCServicer startOperation:toFetchIconsForAppBundleIDs:requestedSize:scale:completionHandler:]_block_invoke.265
+ ___99-[FPDXPCServicer startOperation:toFetchIconsForAppBundleIDs:requestedSize:scale:completionHandler:]_block_invoke.265.cold.1
+ ___block_descriptor_64_e8_32s40s48s56bs_e37_v24?0"<FPXEnumerator>"8"NSError"16ls32l8s40l8s56l8s48l8
+ ___block_literal_global.121
+ ___block_literal_global.162
+ ___block_literal_global.205
+ ___block_literal_global.327
+ ___block_literal_global.453
- ___100-[FPDXPCServicer _test_importItemsPendingScanningProviderProgressForDomainWithID:completionHandler:]_block_invoke.505
- ___100-[FPDXPCServicer uploadLocalVersionOfItemAtURL:bundleID:conflictResolutionPolicy:completionHandler:]_block_invoke.566
- ___100-[FPDXPCServicer uploadLocalVersionOfItemAtURL:bundleID:conflictResolutionPolicy:completionHandler:]_block_invoke.566.cold.1
- ___106-[FPDXPCServicer createItemBasedOnTemplate:fields:urlWrapper:options:bounceOnCollision:completionHandler:]_block_invoke.205
- ___106-[FPDXPCServicer createItemBasedOnTemplate:fields:urlWrapper:options:bounceOnCollision:completionHandler:]_block_invoke.205.cold.1
- ___106-[FPDXPCServicer createItemBasedOnTemplate:fields:urlWrapper:options:bounceOnCollision:completionHandler:]_block_invoke.205.cold.2
- ___109-[FPDXPCServicer evictItemAtURL:evenIfEnumeratingFP:andClearACLForConsumer:evictionReason:completionHandler:]_block_invoke.148
- ___109-[FPDXPCServicer evictItemAtURL:evenIfEnumeratingFP:andClearACLForConsumer:evictionReason:completionHandler:]_block_invoke.148.cold.1
- ___109-[FPDXPCServicer evictItemAtURL:evenIfEnumeratingFP:andClearACLForConsumer:evictionReason:completionHandler:]_block_invoke.148.cold.2
- ___114-[FPDXPCServicer documentURLFromItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.200
- ___120-[FPDXPCServicer startAccessingServiceWithName:itemID:domain:connection:enumerateEntitlementRequired:completionHandler:]_block_invoke.119
- ___120-[FPDXPCServicer startAccessingServiceWithName:itemID:domain:connection:enumerateEntitlementRequired:completionHandler:]_block_invoke.119.cold.1
- ___125-[FPDXPCServicer fetchFSItemsForItemIdentifiers:providerIdentifier:domainIdentifier:materializingIfNeeded:completionHandler:]_block_invoke.217
- ___126-[FPDXPCServicer documentURLFromBookmarkableString:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:completionHandler:]_block_invoke.192
- ___133-[FPDXPCServicer runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:contentBarrier:completionHandler:]_block_invoke.340
- ___133-[FPDXPCServicer runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:contentBarrier:completionHandler:]_block_invoke.340.cold.1
- ___133-[FPDXPCServicer runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:contentBarrier:completionHandler:]_block_invoke.343
- ___139-[FPDXPCServicer addDomain:forProviderIdentifier:byImportingDirectoryAtURL:nonWrappedURL:userAllowedDBDrop:knownFolders:completionHandler:]_block_invoke.288
- ___139-[FPDXPCServicer addDomain:forProviderIdentifier:byImportingDirectoryAtURL:nonWrappedURL:userAllowedDBDrop:knownFolders:completionHandler:]_block_invoke.289
- ___139-[FPDXPCServicer addDomain:forProviderIdentifier:byImportingDirectoryAtURL:nonWrappedURL:userAllowedDBDrop:knownFolders:completionHandler:]_block_invoke.302
- ___158-[FPDXPCServicer getURLForContainerWithItemID:inDataScopeDomainWithIdentifier:documentsScopeDomainIdentifier:documentsFolderItemIdentifier:completionHandler:]_block_invoke.250
- ___158-[FPDXPCServicer getURLForContainerWithItemID:inDataScopeDomainWithIdentifier:documentsScopeDomainIdentifier:documentsFolderItemIdentifier:completionHandler:]_block_invoke.251
- ___50-[FPDXPCServicer pinItemWithID:completionHandler:]_block_invoke.152
- ___51-[FPDXPCServicer trashItemAtURL:completionHandler:]_block_invoke.219
- ___52-[FPDXPCServicer unpinItemWithID:completionHandler:]_block_invoke.156
- ___53-[FPDXPCServicer pauseIndexingFor:completionHandler:]_block_invoke.477
- ___54-[FPDXPCServicer removeDomain:mode:completionHandler:]_block_invoke.305
- ___54-[FPDXPCServicer removeDomain:mode:completionHandler:]_block_invoke.306
- ___54-[FPDXPCServicer resumeIndexingFor:completionHandler:]_block_invoke.478
- ___55-[FPDXPCServicer _test_getDBOptions:completionHandler:]_block_invoke.495
- ___55-[FPDXPCServicer itemForURL:options:completionHandler:]_block_invoke.215
- ___55-[FPDXPCServicer updateLastUsedDate:completionHandler:]_block_invoke.226
- ___55-[FPDXPCServicer updateLastUsedDate:completionHandler:]_block_invoke.228
- ___57-[FPDXPCServicer resolveConflictAtURL:completionHandler:]_block_invoke.285
- ___57-[FPDXPCServicer stateForDomainWithID:completionHandler:]_block_invoke.338
- ___58-[FPDXPCServicer clearDiagnosticsState:completionHandler:]_block_invoke.270
- ___59-[FPDXPCServicer _test_purgerBarrierWithCompletionHandler:]_block_invoke.512
- ___59-[FPDXPCServicer _test_purgerBarrierWithCompletionHandler:]_block_invoke.512.cold.1
- ___59-[FPDXPCServicer appHasNonUploadedFiles:completionHandler:]_block_invoke.351
- ___59-[FPDXPCServicer getSavedDiagnosticsFor:completionHandler:]_block_invoke.269
- ___61-[FPDXPCServicer forceIngestionForItemIDs:completionHandler:]_block_invoke.201
- ___62-[FPDXPCServicer fetchPathComponentsForURL:completionHandler:]_block_invoke.253
- ___62-[FPDXPCServicer setPutBackInfoOnItemAtURL:completionHandler:]_block_invoke.222
- ___62-[FPDXPCServicer startDownloadingItemAtURL:completionHandler:]_block_invoke.141
- ___62-[FPDXPCServicer startDownloadingItemAtURL:completionHandler:]_block_invoke.145
- ___63-[FPDXPCServicer fetchDaemonOperationIDsWithCompletionHandler:]_block_invoke.432
- ___65-[FPDXPCServicer _test_resetDBQueryStatistics:completionHandler:]_block_invoke.507
- ___66-[FPDXPCServicer importProgressForDomainWithID:completionHandler:]_block_invoke.336
- ___66-[FPDXPCServicer putBackURLForTrashedItemAtURL:completionHandler:]_block_invoke.221
- ___67-[FPDXPCServicer _test_disableDBQueryStatistics:completionHandler:]_block_invoke.506
- ___67-[FPDXPCServicer dumpTelemetryTo:providerFilter:completionHandler:]_block_invoke.409
- ___67-[FPDXPCServicer evictItemWithID:evictionReason:completionHandler:]_block_invoke.149
- ___68-[FPDXPCServicer dumpDatabaseAt:fullDump:writeTo:completionHandler:]_block_invoke.346
- ___68-[FPDXPCServicer scheduleActionOperationWithInfo:completionHandler:]_block_invoke.430
- ___69-[FPDXPCServicer valuesForAttributes:forItemAtURL:completionHandler:]_block_invoke.229
- ___70-[FPDXPCServicer _test_triggerDatabaseError:domain:completionHandler:]_block_invoke.511
- ___70-[FPDXPCServicer copyDatabaseForFPCKStartingAtPath:completionHandler:]_block_invoke.423
- ___70-[FPDXPCServicer forceLatestVersionOnDiskForItemID:completionHandler:]_block_invoke.204
- ___71-[FPDXPCServicer dumpStateTo:providerFilter:options:completionHandler:]_block_invoke.392
- ___73-[FPDXPCServicer _test_getDBQueryStatistics:queryPlan:completionHandler:]_block_invoke.508
- ___73-[FPDXPCServicer waitForChangesOnItemsBelowItemWithID:completionHandler:]_block_invoke.426
- ___74-[FPDXPCServicer removeAllDomainsForProviderIdentifier:completionHandler:]_block_invoke.307
- ___74-[FPDXPCServicer removeAllDomainsForProviderIdentifier:completionHandler:]_block_invoke.307.cold.1
- ___74-[FPDXPCServicer startAccessingServiceWithName:itemURL:completionHandler:]_block_invoke.443
- ___75-[FPDXPCServicer removeDomainAndPreserveDataWithID:mode:completionHandler:]_block_invoke.303
- ___75-[FPDXPCServicer removeDomainAndPreserveDataWithID:mode:completionHandler:]_block_invoke.304
- ___76-[FPDXPCServicer fetchLatestVersionForItemAtURL:bundleID:completionHandler:]_block_invoke.556
- ___76-[FPDXPCServicer pauseSyncForItemAtURL:behavior:bundleID:completionHandler:]_block_invoke.538
- ___76-[FPDXPCServicer waitForStabilizationOfDomainWithID:mode:completionHandler:]_block_invoke.427
- ___77-[FPDXPCServicer _performWithCheckedEnumerationAttributes:completionHandler:]_block_invoke.453
- ___77-[FPDXPCServicer forceUpdateBlockedProcessNamesFromDomain:completionHandler:]_block_invoke.333
- ___77-[FPDXPCServicer resumeSyncForItemAtURL:behavior:bundleID:completionHandler:]_block_invoke.550
- ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.486
- ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.486.cold.1
- ___80-[FPDXPCServicer fetchProviderForShareURL:fallbackIdentifier:completionHandler:]_block_invoke.224
- ___80-[FPDXPCServicer fetchProviderForShareURL:fallbackIdentifier:completionHandler:]_block_invoke.224.cold.1
- ___80-[FPDXPCServicer fetchProviderForShareURL:fallbackIdentifier:completionHandler:]_block_invoke.224.cold.2
- ___80-[FPDXPCServicer fetchProviderForShareURL:fallbackIdentifier:completionHandler:]_block_invoke.224.cold.3
- ___80-[FPDXPCServicer fetchProviderForShareURL:fallbackIdentifier:completionHandler:]_block_invoke.224.cold.4
- ___80-[FPDXPCServicer fetchProviderForShareURL:fallbackIdentifier:completionHandler:]_block_invoke.224.cold.5
- ___80-[FPDXPCServicer getNumberOfNonMaterializedFilesInDomain:withCompletionHandler:]_block_invoke.569
- ___80-[FPDXPCServicer getNumberOfNonMaterializedFilesInDomain:withCompletionHandler:]_block_invoke.569.cold.1
- ___82-[FPDXPCServicer extendBookmarkForFileURL:toConsumerID:options:completionHandler:]_block_invoke.209
- ___82-[FPDXPCServicer extendBookmarkForFileURL:toConsumerID:options:completionHandler:]_block_invoke.209.cold.1
- ___82-[FPDXPCServicer extendBookmarkForFileURL:toConsumerID:options:completionHandler:]_block_invoke.209.cold.2
- ___82-[FPDXPCServicer fetchAndStartEnumeratingWithSettings:observer:completionHandler:]_block_invoke.462
- ___82-[FPDXPCServicer reimportItemsBelowItemWithID:markItemDataless:completionHandler:]_block_invoke.332
- ___85-[FPDXPCServicer enumerateSearchResultForRequest:providerDomainID:completionHandler:]_block_invoke.448
- ___86-[FPDXPCServicer setEnabled:forDomainIdentifier:providerIdentifier:completionHandler:]_block_invoke.329
- ___88-[FPDXPCServicer listRemoteVersionsOfItemAtURL:includeCachedVersions:completionHandler:]_block_invoke.286
- ___88-[FPDXPCServicer spotlightReindexAllItemsForBundleID:protectionClass:completionHandler:]_block_invoke.428
- ___89-[FPDXPCServicer startProvidingItemAtURL:fromProviderID:forConsumerID:completionHandler:]_block_invoke.137
- ___91-[FPDXPCServicer selectNewProviderDomain:knownFolders:skipReleasePrompt:completionHandler:]_block_invoke.157
- ___91-[FPDXPCServicer setHiddenByUser:forDomainIdentifier:providerIdentifier:completionHandler:]_block_invoke.330
- ___93-[FPDXPCServicer signalReindexCSIdentifiersByProviderDomainID:indexReason:completionHandler:]_block_invoke.479
- ___93-[FPDXPCServicer signalReindexCSIdentifiersByProviderDomainID:indexReason:completionHandler:]_block_invoke.479.cold.1
- ___93-[FPDXPCServicer signalReindexCSIdentifiersByProviderDomainID:indexReason:completionHandler:]_block_invoke.479.cold.2
- ___94-[FPDXPCServicer setIndexingEnabled:forDomainIdentifier:providerIdentifier:completionHandler:]_block_invoke.331
- ___95-[FPDXPCServicer triggerDiagnosticsFor:triggeringError:uiOnly:useDiagnostic:completionHandler:]_block_invoke.254
- ___95-[FPDXPCServicer triggerDiagnosticsFor:triggeringError:uiOnly:useDiagnostic:completionHandler:]_block_invoke.255
- ___95-[FPDXPCServicer triggerDiagnosticsFor:triggeringError:uiOnly:useDiagnostic:completionHandler:]_block_invoke.255.cold.1
- ___95-[FPDXPCServicer triggerDiagnosticsFor:triggeringError:uiOnly:useDiagnostic:completionHandler:]_block_invoke.256
- ___96-[FPDXPCServicer _test_importItemsPendingScanningDiskProgressForDomainWithID:completionHandler:]_block_invoke.502
- ___98-[FPDXPCServicer _test_importItemsPendingReconciliationProgressForDomainWithID:completionHandler:]_block_invoke.499
- ___98-[FPDXPCServicer spotlightReindexItemsWithIdentifiers:bundleID:protectionClass:completionHandler:]_block_invoke.429
- ___99-[FPDXPCServicer startOperation:toFetchIconsForAppBundleIDs:requestedSize:scale:completionHandler:]_block_invoke.234
- ___99-[FPDXPCServicer startOperation:toFetchIconsForAppBundleIDs:requestedSize:scale:completionHandler:]_block_invoke.234.cold.1
- ___99-[FPDXPCServicer startOperation:toFetchIconsForAppBundleIDs:requestedSize:scale:completionHandler:]_block_invoke.249
- ___99-[FPDXPCServicer startOperation:toFetchIconsForAppBundleIDs:requestedSize:scale:completionHandler:]_block_invoke.249.cold.1
- ___block_descriptor_56_e8_32s40s48bs_e37_v24?0"<FPXEnumerator>"8"NSError"16ls32l8s48l8s40l8
- ___block_literal_global.106
- ___block_literal_global.147
- ___block_literal_global.189
- ___block_literal_global.309
- ___block_literal_global.435
Functions:
~ -[FPDXPCServicer itemForURL:options:completionHandler:] : 1060 -> 952
~ ___55-[FPDXPCServicer itemForURL:options:completionHandler:]_block_invoke.215 -> ___55-[FPDXPCServicer itemForURL:options:completionHandler:]_block_invoke.228 : 368 -> 500
~ ___82-[FPDXPCServicer fetchAndStartEnumeratingWithSettings:observer:completionHandler:]_block_invoke : 1116 -> 1004
~ ___82-[FPDXPCServicer fetchAndStartEnumeratingWithSettings:observer:completionHandler:]_block_invoke_3 : 376 -> 508
CStrings:
+ "com.apple.DocumentManager.DockFolderViewService"
+ "com.apple.DocumentManagerUICore.RecentsAvocado"
+ "com.apple.DocumentManagerUICore.SaveToFiles"
+ "com.apple.DocumentManagerUICore.Service"
+ "com.apple.iCloudDriveCore.diagnostic"
- "com.apple.CloudDocsDaemon.diagnostic"

```
