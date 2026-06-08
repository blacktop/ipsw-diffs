## assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

```diff

-852.0.102.0.0
-  __TEXT.__text: 0x18728
-  __TEXT.__auth_stubs: 0xa90
-  __TEXT.__objc_stubs: 0x4540
-  __TEXT.__objc_methlist: 0xd2c
+910.14.107.0.0
+  __TEXT.__text: 0x17f4c
+  __TEXT.__auth_stubs: 0xb20
+  __TEXT.__objc_stubs: 0x49c0
+  __TEXT.__objc_methlist: 0xdc4
   __TEXT.__dlopen_cstrs: 0x11b
-  __TEXT.__const: 0x100
-  __TEXT.__gcc_except_tab: 0x584
-  __TEXT.__objc_classname: 0x630
-  __TEXT.__objc_methname: 0x510c
-  __TEXT.__objc_methtype: 0x8ba
-  __TEXT.__oslogstring: 0x3c27
-  __TEXT.__cstring: 0x171c
-  __TEXT.__unwind_info: 0x510
-  __DATA_CONST.__auth_got: 0x558
-  __DATA_CONST.__got: 0x6c8
-  __DATA_CONST.__const: 0xea0
-  __DATA_CONST.__cfstring: 0xac0
-  __DATA_CONST.__objc_classlist: 0x140
+  __TEXT.__const: 0x110
+  __TEXT.__gcc_except_tab: 0x554
+  __TEXT.__objc_classname: 0x6bb
+  __TEXT.__objc_methname: 0x5494
+  __TEXT.__objc_methtype: 0x906
+  __TEXT.__oslogstring: 0x3f73
+  __TEXT.__cstring: 0x174a
+  __TEXT.__unwind_info: 0x538
+  __DATA_CONST.__const: 0xf10
+  __DATA_CONST.__cfstring: 0xb20
+  __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x28f0
-  __DATA.__objc_selrefs: 0x1320
-  __DATA.__objc_ivar: 0x74
-  __DATA.__objc_data: 0xc80
+  __DATA_CONST.__auth_got: 0x5a0
+  __DATA_CONST.__got: 0x6f8
+  __DATA.__objc_const: 0x2c98
+  __DATA.__objc_selrefs: 0x1440
+  __DATA.__objc_ivar: 0x7c
+  __DATA.__objc_data: 0xdc0
   __DATA.__data: 0x300
-  __DATA.__bss: 0x48
+  __DATA.__bss: 0x58
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 59A52D3A-B8A6-31DC-A3AC-8E34B7C8268D
-  Functions: 341
-  Symbols:   399
-  CStrings:  1265
+  UUID: C71C9FDA-F485-3533-9237-A49E801E4E97
+  Functions: 354
+  Symbols:   414
+  CStrings:  1331
 
Symbols:
+ _OBJC_CLASS_$_PLCollectionShare
+ _OBJC_CLASS_$_PLDeviceRestoreMigrationSupport
+ _OBJC_CLASS_$_PLPositionalTableOptimizer
+ _OBJC_CLASS_$_PLSearchStore
+ _PLCoreAnalyticsLibrarySummaryLibraryIDKey
+ _PLIsErrorFileNotFound
+ _PLLibraryServicesOperationNameCrashRecoveryThumbnailOptimization
+ _PLPlatformCollectionShareMigrationSupported
+ _PLSearchLeoFeatureAvailabilityEnabled
+ _PLStringFromCoreAnalyticsLibraryID
+ _PLTransactionScopeTableThumbnailOptimization
+ _dispatch_apply
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x7
+ _objc_retain_x8
+ _xpc_connection_cancel
- _CFRetain
- _OBJC_CLASS_$_PLLibraryContentsEnumerator
- _PLCreateShortLivedSyndicationPhotoLibrary
- _xpc_dictionary_get_bool
CStrings:
+ "%K == %d"
+ "%{public}@ CVT root directory does not exist, nothing to clean up"
+ "%{public}@ CVT root path is nil, skipping orphaned CVT cleanup"
+ "%{public}@ Failed to enumerate CVT root directory: %@"
+ "%{public}@ Failed to fetch asset UUIDs for orphaned CVT cleanup: %@"
+ "%{public}@ Failed to remove orphaned CVT directory %{public}@: %@"
+ "%{public}@ Orphaned CVT cleanup complete: removed %ld directories"
+ "%{public}@ Removed orphaned CVT directory for asset %{public}@"
+ "%{public}@ Scanning for orphaned CVT directories (%tu assets in database)"
+ "@\"NSObject<OS_xpc_object>\""
+ "AB"
+ "B28@0:8@\"PLXPCTransaction\"16B24"
+ "B28@0:8@16B24"
+ "Error recovering table thumbnails after optimization crash: %@"
+ "Failed to create search store: %@"
+ "Failed to get Leo statistics: %@"
+ "Migration failed for non-well-known library"
+ "Migration failed for non-well-known library, deactivating: %@"
+ "PLCleanupOrphanedCVTFilesMaintenanceTask"
+ "PLCollectionShareMigrationMaintenanceTask"
+ "PLReportSearchIndexStatisticsMaintenanceTask"
+ "PLSearchIndexMaintenanceTask"
+ "PLThumbnailTableMonitoringMaintenanceTask"
+ "Reported Leo statistics"
+ "Thumbnail table optimization already marked, re-signaling worker"
+ "Thumbnail table optimization needed: %d, fragmentation=%.1f%%, ordering=%.1f%%, tailSpace=%lu"
+ "_dataMigratorDone"
+ "_enqueueThumbnailOptimizationRecoveryOperationWithLSM:library:serverTransaction:"
+ "_listener"
+ "_shouldRunNow"
+ "collectionShareMigrator"
+ "com.apple.assetsd.background-migration.bgst-submission"
+ "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
+ "coreAnalyticsLibraryID"
+ "cplManagerMaintenanceTaskLastRunDate"
+ "entryCapacity"
+ "executeFetchRequest:error:"
+ "fastThumbPersistenceManagers"
+ "fetchRequest"
+ "fireExpiringSoonNotificationIfNeededWithPhotoLibrary:forceNotification:"
+ "fragmentationMetricsForPhotoLibrary:entryCapacity:"
+ "fragmentationPercentage"
+ "initWithPhotoLibrary:index:writeable:error:"
+ "integerValue"
+ "isAppPhotoLibrary"
+ "isCPLSyncablePhotoLibrary"
+ "isDataMigrationInProgress"
+ "isSearchIndexingEnabled"
+ "isSuccess"
+ "kind"
+ "lastPathComponent"
+ "leoStatistics"
+ "libraryStatsCloudKitKey"
+ "libraryStatsCoreAnalyticsKey"
+ "libraryStatsWithCPLManager:photoLibrary:error:"
+ "maskForOptimizeTableThumbs"
+ "migrateAllPendingCollectionSharesWithCompletionHandler:"
+ "orderednessMetricsForPhotoLibrary:entryCapacity:samplingRatio:"
+ "orderingScore"
+ "performIndexMaintenance"
+ "recoverAfterCrashDuringSwapWithTables:photoLibrary:error:"
+ "reportStatisticsDictionary"
+ "result"
+ "runSilentMigrationValidatorWithProgress:force:completionHandler:"
+ "runTaskWithTransaction:force:"
+ "setCplManagerMaintenanceTaskLastRunDate:"
+ "setPrimaryDomain:"
+ "setPurpose:"
+ "setThumbnailTablesNeedOptimization:"
+ "signalBackgroundProcessingNeededOnBundle:"
+ "starting library stats reporting during periodic maintenance for %@"
+ "tailSpace"
+ "thumbnailTablesNeedOptimization"
+ "v16@?0Q8"
+ "valueForKeyPath:"
- "-[PLCPLManagerMaintenanceTask _reportLibraryStatsWithCPLManager:]"
- "Library statistics logging: starting asset enumeration..."
- "PLSearchRemoveUnusedGroupsMaintenanceTask"
- "cameraRollVisibilityChange"
- "configureEnumeratorForHyperionLocalResourcesLogging:cloudPhotoLibraryEnabled:dataForCA:dataForCK:"
- "configureEnumeratorForLibrarySizeLogging:cloudPhotoLibraryEnabled:dataForCA:dataForCK:"
- "configureEnumeratorForLibrarySummaryForLibraryEnumerator:withSyndicationLibraryEnumerator:cloudPhotoLibraryEnabled:dataForCA:libraryServicesManager:"
- "initWithSourceManagedObjectContext:concurrent:readOnly:"
- "processObjectsWithError:"
- "removeUnusedGroupsFromPSI"
- "starting library stats reporting during periodic maintenance"
- "sync:identifyingBlock:library:"

```
