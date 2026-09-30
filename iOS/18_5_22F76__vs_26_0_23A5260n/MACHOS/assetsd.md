## assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

```diff

-760.6.150.0.0
-  __TEXT.__text: 0x165c8
-  __TEXT.__auth_stubs: 0xb80
-  __TEXT.__objc_stubs: 0x4180
-  __TEXT.__objc_methlist: 0xcd4
-  __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__const: 0xf0
-  __TEXT.__gcc_except_tab: 0x590
-  __TEXT.__objc_classname: 0x5ff
-  __TEXT.__objc_methname: 0x4c61
-  __TEXT.__objc_methtype: 0x8b0
-  __TEXT.__oslogstring: 0x3bc1
-  __TEXT.__cstring: 0x142b
-  __TEXT.__unwind_info: 0x4e0
-  __DATA_CONST.__auth_got: 0x5d0
-  __DATA_CONST.__got: 0x700
-  __DATA_CONST.__const: 0xd00
-  __DATA_CONST.__cfstring: 0xa20
-  __DATA_CONST.__objc_classlist: 0x138
+800.14.111.0.0
+  __TEXT.__text: 0x1721c
+  __TEXT.__auth_stubs: 0xae0
+  __TEXT.__objc_stubs: 0x43a0
+  __TEXT.__objc_methlist: 0xcfc
+  __TEXT.__dlopen_cstrs: 0x11b
+  __TEXT.__const: 0x100
+  __TEXT.__gcc_except_tab: 0x5b0
+  __TEXT.__objc_classname: 0x5da
+  __TEXT.__objc_methname: 0x4ee4
+  __TEXT.__objc_methtype: 0x8ba
+  __TEXT.__oslogstring: 0x3b83
+  __TEXT.__cstring: 0x165e
+  __TEXT.__unwind_info: 0x520
+  __DATA_CONST.__auth_got: 0x580
+  __DATA_CONST.__got: 0x6a0
+  __DATA_CONST.__const: 0xe40
+  __DATA_CONST.__cfstring: 0xaa0
+  __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x2798
-  __DATA.__objc_selrefs: 0x1230
-  __DATA.__objc_ivar: 0x6c
-  __DATA.__objc_data: 0xc30
+  __DATA.__objc_const: 0x2710
+  __DATA.__objc_selrefs: 0x12b8
+  __DATA.__objc_ivar: 0x74
+  __DATA.__objc_data: 0xbe0
   __DATA.__data: 0x300
-  __DATA.__bss: 0x38
+  __DATA.__bss: 0x48
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 9916EFF1-7530-39A2-B241-4B8F16D7C87B
-  Functions: 323
-  Symbols:   421
-  CStrings:  1204
+  UUID: 1AB5F367-C0B1-37FB-9487-771F2DFDEDA9
+  Functions: 335
+  Symbols:   399
+  CStrings:  1244
 
Symbols:
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskProgressMetrics
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_CLASS_$_BGSystemTaskThroughputMetrics
+ _PLLibraryServicesOperationNamePrefetchSensitiveContentAnalysisPolicy
+ _PLStringFromModelMigrationActionResultShort
+ _qos_class_self
- _OBJC_CLASS_$_PLAssetAnalysisState
- _OBJC_CLASS_$_PLBackgroundJobLockedResourceWorker
- _OBJC_CLASS_$_PLSpotlightProgressManager
- _PLAssetAnalysisGetLog
- _PLLibraryServicesOperationNameCrashRecoveryRepairInterruptedLockedResourceTransfer
- _PLLibraryServicesOperationNameCrashRecoveryResetSearchIndex
- _PLSearchIndexGetLog
- _PLSearchIndexPauseReasonCloseSearchIndex
- _PLTransactionScopeLockedResources
- _PLTransactionScopeSearchIndex
- _XPC_ACTIVITY_CHECK_IN
- _XPC_ACTIVITY_GRACE_PERIOD
- _XPC_ACTIVITY_GROUP_CONCURRENCY_LIMIT
- _XPC_ACTIVITY_GROUP_NAME
- _XPC_ACTIVITY_INTERVAL_1_HOUR
- _XPC_ACTIVITY_PRIORITY
- _XPC_ACTIVITY_PRIORITY_MAINTENANCE
- _XPC_ACTIVITY_REPEATING
- _XPC_ACTIVITY_REQUIRE_SCREEN_SLEEP
- _xpc_activity_copy_identifier
- _xpc_activity_get_state
- _xpc_activity_register
- _xpc_activity_set_state
- _xpc_activity_should_defer
- _xpc_dictionary_create
- _xpc_dictionary_set_bool
- _xpc_dictionary_set_int64
- _xpc_dictionary_set_string
- _xpc_dictionary_set_uint64
CStrings:
+ "%@.%@"
+ "'%@' completed progress: %lld/%lld"
+ "'%@': %@, Can't register throughput tracking"
+ "'%@': '%@', can't report progress metrics"
+ "+[PLLibraryRepairSupportRegistration registerTaskHandler:description:executionWithProgressBlock:]_block_invoke_3"
+ "-[PLBackgroundMigrationActivity _submitProgresssMetricsForCategory:completedCount:totalCount:]"
+ "@\"BGSystemTask\""
+ "A background migration task with identifier %@ is already submitted"
+ "Background migration finished, result: %@"
+ "Class getSCSensitivityAnalysisClass(void)_block_invoke"
+ "Couldn't deregister metrics for '%@': %@"
+ "Defer maintenance tasks operations on %tu libraries: %@"
+ "Error prefetching sensitive content analysis policy: %@"
+ "Expiring background migration"
+ "Failed to expire background migration task. Error: %@"
+ "Failed to expire maintenance task. Error: %@"
+ "Failed to perform background migration tasks. Error: %@"
+ "Failed to register background migration task for library URL %@"
+ "Failed to submit task request for background migration with identifier %@. Error: %@"
+ "Finished task '%@' work, from: %@, to: %@, itemCount: %lu"
+ "Initial sync of shared albums after rebuild: %d D2D: %d"
+ "Maintenance task: history count: %llu, asset count: %llu in library URL: %@"
+ "SCSensitivityAnalysis"
+ "SpotlightDaemonClient: Aborting request to reindex all searchable items since pathManager is unexpectedly nil"
+ "SpotlightDaemonClient: Aborting unexpected request to reindex all searchable items with invalid bundleID: %{public}@"
+ "SpotlightDaemonClient: Auto bug capture completed with result: %@"
+ "SpotlightDaemonClient: Failed to update feature availability after Spotlight reindex request, error: %@"
+ "SpotlightDaemonClient: in reindexAllItemsForBundleID, dropping search index in availability computer"
+ "Submitting task request for background migration with identifier %@"
+ "TB,V_shouldDefer"
+ "[sync.spotlightReceiver] supported bundle ids: %{public}@"
+ "_progressReportQueue"
+ "_reportProgressForTask:repairTaskName:started:stopped:itemCount:"
+ "_shouldDefer"
+ "_shouldDeferTaskIfRequiredForClassName:"
+ "_submitProgresssMetricsForCategory:completedCount:totalCount:"
+ "_task"
+ "_taskRequestForBackgroundMigrationWithIdentifier:"
+ "addItemCount:"
+ "backgroundSystemTasksConcurrencyGroupName"
+ "backgroundSystemTasksConcurrencyLimit"
+ "com.apple.photos.migration_activity_report"
+ "com.apple.photos.periodicmaintenance.progressreport"
+ "deregisterTaskWithIdentifier:"
+ "deregisterThroughputTrackingFor:withEndTime:error:"
+ "fetchApproximateChangeCountWithPathManager:error:"
+ "generic"
+ "initWithIdentifier:"
+ "initWithIdentifier:qos:workloadCategory:expectedMetricValue:"
+ "initWithIdentifier:qos:workloadCategory:expectedMetricValue:itemsCompleted:totalItemCount:"
+ "initWithLibraryBundle:task:description:"
+ "initWithSourceManagedObjectContext:concurrent:readOnly:"
+ "initWithTask:description:"
+ "migrateBackgroundActionsWithPhotoLibraryBundle:logger:error:reportProgressUsingBlock:continuationHandler:"
+ "numberWithLongLong:"
+ "numberWithUnsignedInt:"
+ "pollForAlbumListUpdatesWithRefreshResetSync:"
+ "prefetchSensitiveContentPolicy:"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "registerTaskHandler:description:executionWithProgressBlock:"
+ "registerThroughputTrackingFor:withStartTime:error:"
+ "reportProgressMetrics:error:"
+ "runCuratedLibraryPeriodicMaintenanceTasksWithProgressReportBlock:"
+ "runPeriodicMaintenanceTasks:withTransaction:progressReportBlock:"
+ "runPeriodicMaintenanceWithProgressReportBlock:"
+ "setExpirationHandler:"
+ "setGroupConcurrencyLimit:"
+ "setGroupName:"
+ "setPriority:"
+ "setRequiresUserInactivity:"
+ "setShouldDefer:"
+ "setTaskCompleted"
+ "setTaskExpiredWithRetryAfter:error:"
+ "setTrySchedulingBefore:"
+ "sharedScheduler"
+ "shouldDefer"
+ "softlink:r:path:/System/Library/Frameworks/SensitiveContentAnalysis.framework/SensitiveContentAnalysis"
+ "submitTaskRequest:error:"
+ "taskRequestForIdentifier:"
+ "v16@?0@\"BGSystemTask\"8"
+ "v24@?0@\"PLLibraryRepairSupport\"8@?<v@?@\"NSDate\"@\"NSDate\"@\"NSString\"Q>16"
+ "v32@?0q8q16@\"NSString\"24"
+ "v40@0:8@16q24q32"
+ "v40@?0@\"NSDate\"8@\"NSDate\"16@\"NSString\"24Q32"
+ "v56@0:8@16@24@32@40Q48"
+ "void *SensitiveContentAnalysisLibrary(void)"
- "@\"NSObject<OS_xpc_object>\""
- "Auto bug capture completed with result: %@"
- "Defer maintenance tasks operations on libraries: %@"
- "Done background migrating: %@"
- "Error cleaning up invalid ignoreUntilDate values: %@"
- "Failed to perform background migration tasks. Setting activity to DEFER. Error: %@"
- "Failed to reset search index due to nil search index manager"
- "Failed to update feature availability after Spotlight reindex request, error: %@"
- "Forcing repair of interrupted locked resource job"
- "Forcing search reindex because of outstanding transactions"
- "Ignoring requested force search reindex because isSearchIndexingEnabled is NO."
- "Initial sync of shared albums after rebuild"
- "PLAnalysisStateCleanupMaintenanceTask"
- "SpotlightDaemonClient: Aborting unexpected request to reindex all searchable items"
- "SpotlightDaemonClient: Aborting unexpected request to reindex all searchable items for bundleID: %@"
- "SpotlightDaemonClient: Aborting unexpected request to reindex searchable items for bundleID: %@, identifiers: %@"
- "SpotlightDaemonClient: Failed to record request to reindex all searchable items for Core Spotlight"
- "SpotlightDaemonClient: Failed to record request to reindex searchable item identifiers for Core Spotlight: %@"
- "SpotlightDaemonClient: Received request to reindex all searchable items for Core Spotlight for bundleID: %@"
- "SpotlightDaemonClient: Received request to reindex searchable items for Core Spotlight: %@ for bundleID: %@"
- "SpotlightDaemonClient: Recorded request to reindex all searchable items for Core Spotlight"
- "SpotlightDaemonClient: Recorded request to reindex searchable item identifiers for Core Spotlight: %@"
- "[sync.spotlightReceiver] supported bundle ids"
- "_criteriaForBackgroundMigration"
- "_deferActivityIfRequiredForClassName:"
- "_updateXPCActivityProperties:"
- "_xpcActivity"
- "addSearchableItemIdentifiers:forOperationType:forPhotoLibraryPathManager:"
- "cleanupInvalidIgnoreUntilDatesInLibraryAtURL:error:"
- "com.apple.assetsd.backgroundmigrations"
- "dropSearchIndexWithCompletion:"
- "fetchApproximateHistoryRecordCountInLibrary:error:"
- "initWithActivity:description:"
- "initWithLibraryBundle:xpcActivity:description:"
- "initWithSourceManagedObjectContext:concurrent:"
- "isSearchIndexingEnabled"
- "migrateBackgroundActionsWithPhotoLibraryBundle:logger:error:continuationHandler:"
- "pollForAlbumListUpdates"
- "recoverFromInterruptedJobWithLibrary:"
- "registerXPCActivityHandler:description:executionBlock:"
- "removeAnalysisRecordsWithNoAssetOrUUIDUseMaintenanceMode:library:"
- "runCuratedLibraryPeriodicMaintenanceTasks"
- "runPeriodicMaintenance"
- "runPeriodicMaintenanceTasks:withTransaction:"
- "searchIndexManager"
- "setSpotlightIndexNeedsReindexing:forPhotoLibraryPathManager:"
- "shouldDisablePhotosLegacySearchDonation"
- "stopObservingSystemLibraryChanges"
- "unpauseIndexingWithReason:"
- "v40@0:8r*16@24@?32"

```
