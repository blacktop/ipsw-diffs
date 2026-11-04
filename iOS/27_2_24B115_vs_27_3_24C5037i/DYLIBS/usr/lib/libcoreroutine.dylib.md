## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-1123.0.3.0.0
-  __TEXT.__text: 0x6bbe7c
-  __TEXT.__objc_methlist: 0x35370
-  __TEXT.__const: 0x4cd8
+1123.0.6.0.0
+  __TEXT.__text: 0x6c3370
+  __TEXT.__objc_methlist: 0x35670
+  __TEXT.__const: 0x4d08
   __TEXT.__dlopen_cstrs: 0x1d2
-  __TEXT.__swift5_typeref: 0x457
-  __TEXT.__swift5_capture: 0x144
+  __TEXT.__swift5_typeref: 0x477
+  __TEXT.__swift5_capture: 0x14c
   __TEXT.__constg_swiftt: 0x12c
   __TEXT.__swift5_fieldmd: 0x48
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__oslogstring: 0x8aec3
-  __TEXT.__cstring: 0x4b1f0
+  __TEXT.__oslogstring: 0x8b936
+  __TEXT.__cstring: 0x4b6f0
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x40
   __TEXT.__swift_as_cont: 0x60
   __TEXT.__swift5_reflstr: 0x14
-  __TEXT.__gcc_except_tab: 0x2f664
+  __TEXT.__gcc_except_tab: 0x2f974
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x11c10
-  __TEXT.__eh_frame: 0x7c8
+  __TEXT.__unwind_info: 0x11d68
+  __TEXT.__eh_frame: 0x7d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x10778
-  __DATA_CONST.__objc_classlist: 0x16a8
-  __DATA_CONST.__objc_catlist: 0x3f0
+  __DATA_CONST.__const: 0x10810
+  __DATA_CONST.__objc_classlist: 0x16d0
+  __DATA_CONST.__objc_catlist: 0x3f8
   __DATA_CONST.__objc_protolist: 0x388
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b748
+  __DATA_CONST.__objc_selrefs: 0x1b8e0
   __DATA_CONST.__objc_protorefs: 0x138
-  __DATA_CONST.__objc_superrefs: 0x1298
+  __DATA_CONST.__objc_superrefs: 0x12b0
   __DATA_CONST.__objc_arraydata: 0x2dd8
-  __DATA_CONST.__got: 0x3558
-  __AUTH_CONST.__const: 0x38d8
-  __AUTH_CONST.__cfstring: 0x2c5c0
-  __AUTH_CONST.__objc_const: 0x57110
-  __AUTH_CONST.__objc_intobj: 0x4c08
+  __DATA_CONST.__got: 0x3598
+  __AUTH_CONST.__const: 0x3918
+  __AUTH_CONST.__cfstring: 0x2c7a0
+  __AUTH_CONST.__objc_const: 0x576f8
+  __AUTH_CONST.__objc_intobj: 0x4c38
   __AUTH_CONST.__objc_arrayobj: 0xfc0
   __AUTH_CONST.__objc_doubleobj: 0xbe0
   __AUTH_CONST.__objc_dictobj: 0x2a8
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1328
-  __AUTH.__objc_data: 0x1a40
+  __AUTH_CONST.__auth_got: 0x1320
+  __AUTH.__objc_data: 0x1bd0
   __AUTH.__data: 0x30
-  __DATA.__objc_ivar: 0x292c
-  __DATA.__data: 0x2e28
-  __DATA_DIRTY.__objc_ivar: 0x12a8
+  __DATA.__objc_ivar: 0x2950
+  __DATA.__data: 0x2e48
+  __DATA.__common: 0x8
+  __DATA_DIRTY.__objc_ivar: 0x12b0
   __DATA_DIRTY.__objc_data: 0xc9e0
-  __DATA_DIRTY.__data: 0x800
+  __DATA_DIRTY.__data: 0x7f0
   __DATA_DIRTY.__bss: 0x2a8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 22197
-  Symbols:   34184
-  CStrings:  16512
+  Functions: 22285
+  Symbols:   34322
+  CStrings:  16577
 
Symbols:
+ +[RTAuthorizationManager readCoreRoutineLocationClientState]
+ +[RTExtendedTimeToLiveGate refreshMFeatureVerdictWithProvider:previousVerdict:defaultsManager:]
+ +[RTPOIHarvestUtilities harvestVisit:targets:harvestType:poiHarvester:error:]
+ +[RTPOIHarvestUtilities shouldHarvestMapItemSource:harvestType:harvestMask:]
+ +[RTTripParkingMetrics(RTCoreDataTransformable) createWithManagedObject:]
+ +[RTTripParkingMetrics(RTCoreDataTransformable) createWithTripParkingMetricsMO:]
+ +[RTTripParkingMetricsCalculator circlingTimeForSortedLocations:destinationLatitude:destinationLongitude:radius_m:tripEndDate:]
+ +[RTTripParkingMetricsCalculator walkingTimeAfterLastDriveForSortedCommuteTrips:walkTimeDurationAfterDrive_sec:]
+ +[RTTripParkingMetricsMO managedObjectWithTripParkingMetrics:inManagedObjectContext:]
+ +[RTTripParkingMetricsMO(CoreDataProperties) fetchRequest]
+ +[RTTripParkingMetricsStore _predicateForCommuteID:]
+ -[RTAuthorizationManager _applyCoreRoutineLocationClientState:]
+ -[RTAuthorizationManager _readCoreRoutineLocationClientState]
+ -[RTAuthorizationManager coreRoutineEnabledVerified]
+ -[RTAuthorizationManager setCoreRoutineEnabledVerified:]
+ -[RTCheckInMetricsProvider runIsMultiDevice]
+ -[RTCheckInMetricsProvider setRunIsMultiDevice:]
+ -[RTDaemonClient fetchTripParkingMetricsWithOptions:reply:]
+ -[RTExtendedTimeToLiveGate initWithFeatureEnabled:trialManager:platform:defaultsManager:activityStatusProvider:]
+ -[RTLearnedLocationEngine _harvestVisits:places:finerGranularityInferredMapItems:]
+ -[RTPOIHarvestContext .cxx_destruct]
+ -[RTPOIHarvestContext accessPoints]
+ -[RTPOIHarvestContext fingerprintLocations]
+ -[RTPOIHarvestContext initWithAccessPoints:fingerprintLocations:motionActivities:]
+ -[RTPOIHarvestContext motionActivities]
+ -[RTPOIHarvestTarget .cxx_destruct]
+ -[RTPOIHarvestTarget initWithMapItem:source:]
+ -[RTPOIHarvestTarget mapItem]
+ -[RTPOIHarvestTarget source]
+ -[RTPOIHarvester _harvestContextForAccessPoints:metrics:]
+ -[RTPOIHarvester _harvestPOIs:accessPointArrays:referenceLocations:harvestType:metrics:error:]
+ -[RTPOIHarvester _poiHarvestWithContext:mapItem:referenceLocations:harvestType:]
+ -[RTPOIHarvester harvestPOIs:visitLocations:visitEntryDate:visitExitDate:harvestType:error:]
+ -[RTPersistenceMirroringManager _recomputeExportingAvailability]
+ -[RTPersistenceMirroringManager onExpiredRecordsRemoved:]
+ -[RTPurgeManager _longTermExtendedReferenceDate:]
+ -[RTTripClusterDataStoresContainer _refreshCloudSyncRetentionIntervals]
+ -[RTTripClusterDataStoresContainer initWithTripClusterStore:tripClusterCloudStore:tripClusterRouteStore:tripClusterRouteRoadTransitionsStore:tripClusterRecencyStore:tripClusterRecencyCloudStore:tripClusterScheduleStore:tripClusterScheduleCloudStore:tripSegmentRoadTransitionsStore:tripClusterWaypointStore:tripClusterWaypointCloudStore:tripClusterRouteSummaryStore:tripParkingMetricsStore:defaultsManager:bugCaptureManager:]
+ -[RTTripClusterDataStoresContainer isTripClusterChildDataEligibleForCloudPush:]
+ -[RTTripClusterDataStoresContainer isTripClusterEligibleForCloudPush:]
+ -[RTTripClusterDataStoresContainer isTripClusterRecencyEligibleForCloudPush:]
+ -[RTTripClusterDataStoresContainer tripParkingMetricsStore]
+ -[RTTripClusterManager _computeAndStoreTripParkingMetricsForDrivingSegment:sortedCommuteTrips:walkAndBikeTripStats:]
+ -[RTTripClusterManager fetchTripParkingMetricsWithOptions:handler:]
+ -[RTTripClusterManager isParkingMetricsEnabled]
+ -[RTTripClusterManager setIsParkingMetricsEnabled:]
+ -[RTTripParkingMetrics(RTCoreDataTransformable) managedObjectWithContext:]
+ -[RTTripParkingMetricsStore _deleteExpiredTripParkingMetricsPredating:handler:]
+ -[RTTripParkingMetricsStore _deleteTripParkingMetricsWithCommuteID:handler:]
+ -[RTTripParkingMetricsStore _fetchTripParkingMetricsWithContext:handler:]
+ -[RTTripParkingMetricsStore _fetchTripParkingMetricsWithOptions:handler:]
+ -[RTTripParkingMetricsStore _getAllStoredCommuteIDsWithHandler:]
+ -[RTTripParkingMetricsStore _purgeTripParkingMetricsWithHandler:]
+ -[RTTripParkingMetricsStore _storeTripParkingMetrics:handler:]
+ -[RTTripParkingMetricsStore deleteExpiredTripParkingMetricsPredating:handler:]
+ -[RTTripParkingMetricsStore deleteTripParkingMetricsWithCommuteID:]
+ -[RTTripParkingMetricsStore deleteTripParkingMetricsWithCommuteID:handler:]
+ -[RTTripParkingMetricsStore fetchRequestFromOptions:offset:error:]
+ -[RTTripParkingMetricsStore fetchRequestFromOptions:offset:error:inManagedObjectContext:]
+ -[RTTripParkingMetricsStore fetchRequestFromStoredTripParkingMetricsOptions:inManagedObjectContext:]
+ -[RTTripParkingMetricsStore fetchTripParkingMetricsWithContext:handler:]
+ -[RTTripParkingMetricsStore fetchTripParkingMetricsWithOptions:handler:]
+ -[RTTripParkingMetricsStore getAllStoredCommuteIDsWithHandler:]
+ -[RTTripParkingMetricsStore getAllStoredCommuteIDs]
+ -[RTTripParkingMetricsStore getTripParkingMetricsWithOptions:]
+ -[RTTripParkingMetricsStore initWithPersistenceManager:]
+ -[RTTripParkingMetricsStore purgeTripParkingMetricsWithHandler:]
+ -[RTTripParkingMetricsStore storeTripParkingMetrics:]
+ -[RTTripParkingMetricsStore storeTripParkingMetrics:handler:]
+ GCC_except_table200
+ GCC_except_table214
+ GCC_except_table218
+ GCC_except_table229
+ GCC_except_table232
+ GCC_except_table235
+ GCC_except_table250
+ GCC_except_table263
+ GCC_except_table268
+ GCC_except_table270
+ GCC_except_table273
+ GCC_except_table276
+ GCC_except_table280
+ GCC_except_table283
+ GCC_except_table285
+ GCC_except_table289
+ GCC_except_table308
+ GCC_except_table310
+ GCC_except_table312
+ GCC_except_table316
+ GCC_except_table319
+ GCC_except_table321
+ GCC_except_table323
+ GCC_except_table327
+ GCC_except_table331
+ GCC_except_table334
+ GCC_except_table336
+ _OBJC_CLASS_$_RTActionSuggestionActivityStatusProvider
+ _OBJC_CLASS_$_RTPOIHarvestContext
+ _OBJC_CLASS_$_RTPOIHarvestTarget
+ _OBJC_CLASS_$_RTTripParkingMetrics
+ _OBJC_CLASS_$_RTTripParkingMetricsCalculator
+ _OBJC_CLASS_$_RTTripParkingMetricsEnumerationContext
+ _OBJC_CLASS_$_RTTripParkingMetricsEnumerationOptions
+ _OBJC_CLASS_$_RTTripParkingMetricsMO
+ _OBJC_CLASS_$_RTTripParkingMetricsStore
+ _OBJC_IVAR_$_RTCheckInMetricsProvider._runIsMultiDevice
+ _OBJC_IVAR_$_RTPOIHarvestContext._accessPoints
+ _OBJC_IVAR_$_RTPOIHarvestContext._fingerprintLocations
+ _OBJC_IVAR_$_RTPOIHarvestContext._motionActivities
+ _OBJC_IVAR_$_RTPOIHarvestTarget._mapItem
+ _OBJC_IVAR_$_RTPOIHarvestTarget._source
+ _OBJC_IVAR_$_RTTripClusterDataStoresContainer._cloudSyncExpirationInterval
+ _OBJC_IVAR_$_RTTripClusterDataStoresContainer._cloudSyncShortExpirationInterval
+ _OBJC_IVAR_$_RTTripClusterDataStoresContainer._tripParkingMetricsStore
+ _OBJC_METACLASS_$_RTActionSuggestionActivityStatusProvider
+ _OBJC_METACLASS_$_RTPOIHarvestContext
+ _OBJC_METACLASS_$_RTPOIHarvestTarget
+ _OBJC_METACLASS_$_RTTripParkingMetricsCalculator
+ _OBJC_METACLASS_$_RTTripParkingMetricsMO
+ _OBJC_METACLASS_$_RTTripParkingMetricsStore
+ _RTPersistenceExpirationEnforcerDidRemoveExpiredRecordsNotificationName
+ __DATA_RTActionSuggestionActivityStatusProvider
+ __INSTANCE_METHODS_RTActionSuggestionActivityStatusProvider
+ __METACLASS_DATA_RTActionSuggestionActivityStatusProvider
+ __OBJC_$_CATEGORY_CLASS_METHODS_RTTripParkingMetrics_$_RTCoreDataTransformable
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_RTTripParkingMetrics_$_RTCoreDataTransformable
+ __OBJC_$_CATEGORY_RTTripParkingMetrics_$_RTCoreDataTransformable
+ __OBJC_$_CLASS_METHODS_RTTripParkingMetricsCalculator
+ __OBJC_$_CLASS_METHODS_RTTripParkingMetricsMO(CoreDataProperties)
+ __OBJC_$_CLASS_METHODS_RTTripParkingMetricsStore
+ __OBJC_$_INSTANCE_METHODS_RTPOIHarvestContext
+ __OBJC_$_INSTANCE_METHODS_RTPOIHarvestTarget
+ __OBJC_$_INSTANCE_METHODS_RTTripParkingMetricsStore
+ __OBJC_$_INSTANCE_VARIABLES_RTPOIHarvestContext
+ __OBJC_$_INSTANCE_VARIABLES_RTPOIHarvestTarget
+ __OBJC_$_PROP_LIST_RTPOIHarvestContext
+ __OBJC_$_PROP_LIST_RTPOIHarvestTarget
+ __OBJC_$_PROP_LIST_RTTripParkingMetrics_$_RTCoreDataTransformable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RTActionSuggestionActivityStatusProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RTActionSuggestionActivityStatusProviding
+ __OBJC_$_PROTOCOL_REFS_RTActionSuggestionActivityStatusProviding
+ __OBJC_CATEGORY_PROTOCOLS_$_RTTripParkingMetrics_$_RTCoreDataTransformable
+ __OBJC_CLASS_RO_$_RTPOIHarvestContext
+ __OBJC_CLASS_RO_$_RTPOIHarvestTarget
+ __OBJC_CLASS_RO_$_RTTripParkingMetricsCalculator
+ __OBJC_CLASS_RO_$_RTTripParkingMetricsMO
+ __OBJC_CLASS_RO_$_RTTripParkingMetricsStore
+ __OBJC_LABEL_PROTOCOL_$_RTActionSuggestionActivityStatusProviding
+ __OBJC_METACLASS_RO_$_RTPOIHarvestContext
+ __OBJC_METACLASS_RO_$_RTPOIHarvestTarget
+ __OBJC_METACLASS_RO_$_RTTripParkingMetricsCalculator
+ __OBJC_METACLASS_RO_$_RTTripParkingMetricsMO
+ __OBJC_METACLASS_RO_$_RTTripParkingMetricsStore
+ __OBJC_PROTOCOL_$_RTActionSuggestionActivityStatusProviding
+ __PROTOCOLS_RTActionSuggestionActivityStatusProvider
+ ___116-[RTTripClusterManager _computeAndStoreTripParkingMetricsForDrivingSegment:sortedCommuteTrips:walkAndBikeTripStats:]_block_invoke
+ ___116-[RTTripClusterManager _computeAndStoreTripParkingMetricsForDrivingSegment:sortedCommuteTrips:walkAndBikeTripStats:]_block_invoke_2
+ ___51-[RTTripParkingMetricsStore getAllStoredCommuteIDs]_block_invoke
+ ___53-[RTTripParkingMetricsStore storeTripParkingMetrics:]_block_invoke
+ ___57-[RTPOIHarvester _harvestContextForAccessPoints:metrics:]_block_invoke
+ ___57-[RTPersistenceMirroringManager onExpiredRecordsRemoved:]_block_invoke
+ ___61-[RTTripParkingMetricsStore storeTripParkingMetrics:handler:]_block_invoke
+ ___62-[RTTripParkingMetricsStore _storeTripParkingMetrics:handler:]_block_invoke
+ ___62-[RTTripParkingMetricsStore getTripParkingMetricsWithOptions:]_block_invoke
+ ___63-[RTTripParkingMetricsStore getAllStoredCommuteIDsWithHandler:]_block_invoke
+ ___64-[RTTripParkingMetricsStore _getAllStoredCommuteIDsWithHandler:]_block_invoke
+ ___64-[RTTripParkingMetricsStore _getAllStoredCommuteIDsWithHandler:]_block_invoke_2
+ ___64-[RTTripParkingMetricsStore purgeTripParkingMetricsWithHandler:]_block_invoke
+ ___67-[RTTripClusterManager fetchTripParkingMetricsWithOptions:handler:]_block_invoke
+ ___67-[RTTripParkingMetricsStore deleteTripParkingMetricsWithCommuteID:]_block_invoke
+ ___72-[RTTripParkingMetricsStore fetchTripParkingMetricsWithContext:handler:]_block_invoke
+ ___72-[RTTripParkingMetricsStore fetchTripParkingMetricsWithOptions:handler:]_block_invoke
+ ___73-[RTTripParkingMetricsStore _fetchTripParkingMetricsWithContext:handler:]_block_invoke
+ ___75-[RTTripParkingMetricsStore deleteTripParkingMetricsWithCommuteID:handler:]_block_invoke
+ ___76-[RTTripParkingMetricsStore _deleteTripParkingMetricsWithCommuteID:handler:]_block_invoke
+ ___78-[RTTripParkingMetricsStore deleteExpiredTripParkingMetricsPredating:handler:]_block_invoke
+ ___82-[RTLearnedLocationEngine _harvestVisits:places:finerGranularityInferredMapItems:]_block_invoke
+ ___92-[RTPOIHarvester harvestPOIs:visitLocations:visitEntryDate:visitExitDate:harvestType:error:]_block_invoke
+ ___95+[RTExtendedTimeToLiveGate refreshMFeatureVerdictWithProvider:previousVerdict:defaultsManager:]_block_invoke
+ ___block_descriptor_48_e8_32s_e54_B24?0"NSObject<OS_dispatch_semaphore>"8"NSString"16ls32l8
+ ___block_descriptor_49_e8_32s_e20_v24?0q8"NSError"16ls32l8
+ ___block_descriptor_68_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ _kRTTripParkingMetricsDefaultCirclingRadius_m
+ _kRTTripParkingMetricsUnknownDuration
+ _symbolic SS_ypt
+ _symbolic _____ 14libcoreroutine40RTActionSuggestionActivityStatusProviderC
+ _symbolic _____ So32RTActionSuggestionActivityStatusV
+ _symbolic _____So7NSErrorCSgIeyByy_ So32RTActionSuggestionActivityStatusV
+ _symbolic _____XDXMT 14libcoreroutine40RTActionSuggestionActivityStatusProviderC
+ _symbolic ___________pSgIegyg_ So32RTActionSuggestionActivityStatusV s5ErrorP
+ _symbolic _____ySSypG s18_DictionaryStorageC
- +[RTAuthorizationManager readCoreRoutineLocationClientEnabled]
- +[RTExtendedTimeToLiveGate refreshMFeatureVerdictWithProvider:defaultsManager:]
- +[RTPOIHarvestUtilities harvestVisits:mapItem:harvestType:poiHarvester:error:]
- -[RTBGSystemTaskScheduler setEnableHealthChecks:]
- -[RTExtendedTimeToLiveGate initWithFeatureEnabled:trialManager:platform:defaultsManager:featureStatusProvider:]
- -[RTLearnedLocationEngine _harvestVisits:places:]
- -[RTPOIHarvester _harvestPOI:mapItemSource:accessPointArrays:referenceLocations:harvestType:metrics:error:]
- -[RTPOIHarvester _poiHarvestForAccessPoints:mapItem:referenceLocations:harvestType:metrics:]
- -[RTTripClusterDataStoresContainer initWithTripClusterStore:tripClusterCloudStore:tripClusterRouteStore:tripClusterRouteRoadTransitionsStore:tripClusterRecencyStore:tripClusterRecencyCloudStore:tripClusterScheduleStore:tripClusterScheduleCloudStore:tripSegmentRoadTransitionsStore:tripClusterWaypointStore:tripClusterWaypointCloudStore:tripClusterRouteSummaryStore:defaultsManager:bugCaptureManager:]
- -[RTTripClusterDataStoresContainer shouldTripClusterBePurged:]
- -[RTTripClusterDataStoresContainer shouldTripClusterChildDataBePurged:]
- -[RTTripClusterDataStoresContainer shouldTripClusterRecencyBePurged:]
- GCC_except_table125
- GCC_except_table228
- GCC_except_table231
- GCC_except_table234
- GCC_except_table249
- GCC_except_table262
- GCC_except_table264
- GCC_except_table269
- GCC_except_table272
- GCC_except_table281
- GCC_except_table284
- GCC_except_table307
- GCC_except_table309
- GCC_except_table311
- GCC_except_table315
- GCC_except_table318
- GCC_except_table320
- GCC_except_table322
- GCC_except_table326
- GCC_except_table330
- GCC_except_table333
- GCC_except_table335
- _OBJC_CLASS_$_RTActionSuggestionFeatureStatusProvider
- _OBJC_METACLASS_$_RTActionSuggestionFeatureStatusProvider
- __DATA_RTActionSuggestionFeatureStatusProvider
- __INSTANCE_METHODS_RTActionSuggestionFeatureStatusProvider
- __METACLASS_DATA_RTActionSuggestionFeatureStatusProvider
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_RTActionSuggestionFeatureStatusProviding
- __OBJC_$_PROTOCOL_METHOD_TYPES_RTActionSuggestionFeatureStatusProviding
- __OBJC_$_PROTOCOL_REFS_RTActionSuggestionFeatureStatusProviding
- __OBJC_LABEL_PROTOCOL_$_RTActionSuggestionFeatureStatusProviding
- __OBJC_PROTOCOL_$_RTActionSuggestionFeatureStatusProviding
- __PROTOCOLS_RTActionSuggestionFeatureStatusProvider
- ___105-[RTPOIHarvester harvestPOI:mapItemSource:visitLocations:visitEntryDate:visitExitDate:harvestType:error:]_block_invoke
- ___49-[RTLearnedLocationEngine _harvestVisits:places:]_block_invoke
- ___79+[RTExtendedTimeToLiveGate refreshMFeatureVerdictWithProvider:defaultsManager:]_block_invoke
- ___92-[RTPOIHarvester _poiHarvestForAccessPoints:mapItem:referenceLocations:harvestType:metrics:]_block_invoke
- _symbolic _____ 14libcoreroutine39RTActionSuggestionFeatureStatusProviderC
- _symbolic _____ So36RTActionSuggestionFeatureStatusStateV
- _symbolic _____So7NSErrorCSgIeyByy_ So36RTActionSuggestionFeatureStatusStateV
- _symbolic ___________pSgIegyg_ So36RTActionSuggestionFeatureStatusStateV s5ErrorP
CStrings:
+ "%@, %@, CoreRoutine client read was indeterminate; retaining last confirmed value, %{public}@, term left unverified"
+ "%@, %@, CoreRoutine's location client state, %{public}@"
+ "%@, %@, CoreRoutine, %{public}@"
+ "%@, %@, Detected %lu orphaned relationships and %lu unexpected files; RBC to be invoked"
+ "%@, %@, Location Services, %{public}@"
+ "%@, %@, Location services enabled, %{public}@"
+ "%@, %@, cached auth state from defaults, Location Services, %{public}@, CoreRoutine, %{public}@, enabled, %{public}@"
+ "%@, %@, read results, Location Services, %{public}@, CoreRoutine client, %{public}@"
+ "%@, %@, refreshed after CLAppResetChangedNotification, enabled, %{public}@"
+ "%@, %@, refreshed after CLAuthorizationStatusChangedNotification, Location Services, %{public}@, CoreRoutine verified, %{public}@"
+ "%@, %@, supported, %{public}@, Location Services, %{public}@, CoreRoutine, %{public}@, verified, %{public}@, enabled, %{public}@"
+ "%@, account is not single-iPhone, submitting with the multi-device outcome bit"
+ "%@, device check failed, retrying on the failure back-off, error, %@"
+ "%@, encountered error during metadata reset request for %lu object IDs, error, %@"
+ "%@, expiration cutoff, %{public}@, place type inference cutoff, %{public}@"
+ "%@, exporting available, %{public}@"
+ "%@, failed to check for expired records, suspending export, error, %@"
+ "%@, harvested visit, %{sensitive}@, against %lu targets, success, %{public}@, error, %{public}@"
+ "%@, harvested visit, %{sensitive}@, primary mapItem, %{sensitive}@, finergranularity mapItem, %{sensitive}@, success, %{public}@, error, %{public}@"
+ "%@, managedObject, %@, is not supported by RTTripParkingMetrics+CoreDataReadable (in %s:%d)"
+ "%@, successfully submitted metadata reset request for %lu object IDs"
+ "%@, timed out waiting for %{public}@, error, %@"
+ "%@,%@,Error fetching all trip IDs: %@"
+ "%@,%@,Semaphore timeout fetching all trip IDs: %@"
+ "%@,%@,_isParkingMetricsEnabled,%{public}d,internalInstall,%{public}d,featureFlag,%{public}d"
+ "%@,%@,commuteID,%@,fetched count,%lu,error,%@"
+ "%@,%@,parking metrics are not enabled"
+ "%@,%@,purging entries expiring before,%@"
+ "%@,Error creating RTTripParkingMetrics from tripParkingMetricsMO"
+ "%@,Error deleting trip parking metrics for commuteID,%@,error,%@"
+ "%@,Error fetching locations for parking metrics,skipping,commuteID,%@,error,%@"
+ "%@,Error fetching trip parking metrics for commuteID,%@,error,%@"
+ "%@,Error purging expired trip parking metrics,%@"
+ "%@,Error storing trip parking metrics,%@"
+ "%@,Error storing trip parking metrics,commuteID,%@,error,%@"
+ "%@,Error storing trip parking metrics,error,%@"
+ "%@,Error,missing commuteID in options. This will fetch all trip parking metrics"
+ "%@,Negative walking time after last drive,walkTimeAfterDrive,%.1f,walkTimeBetweenDrives,%.1f"
+ "%@,Semaphore Error fetching trip parking metrics for commuteID,%@,error,%@"
+ "%@,Semaphore Error storing trip parking metrics,error,%@"
+ "%@,Semaphore error deleting trip parking metrics for commuteID,%@,error,%@"
+ "%@,Skipping cluster not eligible for cloud push: %@"
+ "%@,Skipping cluster update not eligible for cloud push: %@"
+ "%@,Skipping recency not eligible for cloud push: %@"
+ "%@,Skipping schedule not eligible for cloud push: %@"
+ "%@,Skipping schedule update not eligible for cloud push: %@"
+ "%@,Skipping waypoint cluster not eligible for cloud push: %@"
+ "%@,Stored trip parking metrics,commuteID,%@,timeID,%d,circlingTime,%f,walkingTime,%f"
+ "%@,cloud sync retention,useGatedRetention,%d,interval,%.0f,shortInterval,%.0f"
+ "%@:%@ no CoreRoutine location entity registered; cached routineEnabled=%{public}@ locally, will reconcile on next CLAppResetChangedNotification"
+ "%lu unexpected files detected"
+ "%lu unexpected files detected (%@)"
+ "%s: Failed to fetch Mulberry activity status, error, %@"
+ "%s: Mulberry activity status, %ld"
+ "%s: Unrecognized Mulberry activity status, %{public}s"
+ "%{public}@, %{public}@, Failed to copy map item, %{sensitive}@, skipping target"
+ "%{public}@, mFeature fetch failed, holding previous verdict, error, %{public}@"
+ "%{public}@, mFeature verdict unchanged, %{public}@"
+ "+[RTTripParkingMetrics(RTCoreDataTransformable) createWithManagedObject:]"
+ "-[RTTripClusterManager fetchTripParkingMetricsWithOptions:handler:]"
+ "-[RTTripParkingMetricsStore _deleteExpiredTripParkingMetricsPredating:handler:]"
+ "-[RTTripParkingMetricsStore _deleteTripParkingMetricsWithCommuteID:handler:]"
+ "-[RTTripParkingMetricsStore _fetchTripParkingMetricsWithContext:handler:]"
+ "-[RTTripParkingMetricsStore _fetchTripParkingMetricsWithOptions:handler:]"
+ "-[RTTripParkingMetricsStore _getAllStoredCommuteIDsWithHandler:]"
+ "-[RTTripParkingMetricsStore getAllStoredCommuteIDsWithHandler:]"
+ "-[RTTripParkingMetricsStore storeTripParkingMetrics:handler:]"
+ "AUTHORIZED"
+ "B24@?0@\"NSObject<OS_dispatch_semaphore>\"8@\"NSString\"16"
+ "CoreRoutine enabled, %{public}@"
+ "DENIED"
+ "INDETERMINATE"
+ "Invalid parameter not satisfying: lastPhysicalDrivingSegment"
+ "Invalid parameter not satisfying: tripParkingMetrics"
+ "Invalid parameter not satisfying: tripParkingMetrics (in %s:%d)"
+ "Invalid parameter not satisfying: tripParkingMetricsMO.commuteID"
+ "Location services enabled, %{public}@"
+ "Parking metrics are not enabled"
+ "RTAuthorizationManagerCoreRoutineClientStateOverride"
+ "RTDefaultsTripClusterCloudSyncUseExtendedRetention"
+ "RTDefaultsTripSegmentParkingMetricsEnabled"
+ "RTPersistenceExpirationEnforcerDidRemoveExpiredRecordsNotificationName"
+ "RTTripParkingMetricsMO"
+ "Submitted POI harvest success, %{public}s, map item source, %lu, access point count, %lu, location count, %lu, triggerType, %{public}d, harvestType, %{public}@, error, %{public}@"
+ "TimeToPark"
+ "UNKNOWN"
+ "Unrecognized Mulberry activity status"
+ "com.apple.CoreRoutine.RTActionSuggestionActivityStatusProvider"
+ "fetchActivityStatus(completion:)"
+ "remove expired records"
+ "remove learned place type inferences"
+ "remove unreferenced map items"
+ "remove unreferenced places"
+ "set routine enabled to %{public}@"
+ "update routine enabled to %{public}@"
- "%@, %@, CoreRoutine's location client enabled, %@"
- "%@, %@, CoreRoutine, %@"
- "%@, %@, Detected %lu orphaned relationships; RBC to be invoked"
- "%@, %@, Location Services, %@"
- "%@, %@, Location services enabled, %@"
- "%@, %@, cached auth state from defaults, Location Services, %@, CoreRoutine, %@, enabled, %@"
- "%@, %@, refreshed after CLAppResetChangedNotification, enabled, %@"
- "%@, %@, refreshed after CLAuthorizationStatusChangedNotification, Location Services, %@"
- "%@, %@, supported, %@, Location Services, %@, CoreRoutine, %@, enabled, %@"
- "%@, account has a device other than an iPhone, or the device fetch failed, skipping, error, %@"
- "%@, encountered error during metadata reset request with object IDs %@s, error, %@"
- "%@, successfully submitted metadata reset request for %lu object IDs, %@"
- "%@,Skipping purge-eligible cluster: %@"
- "%@,Skipping purge-eligible recency: %@"
- "%@,Skipping purge-eligible schedule: %@"
- "%@,Skipping purge-eligible waypoint cluster: %@"
- "%@:%@ no CoreRoutine location entity registered; cached routineEnabled=%@ locally, will reconcile on next CLAppResetChangedNotification"
- "%s: Failed to fetch Mulberry feature status, error, %@"
- "%s: Mulberry feature status, %ld"
- "%{public}@, %{public}@, Failed to copy map item, %{sensitive}@, exiting early"
- "%{public}@, mFeature indeterminate, holding previous verdict, error, %{public}@"
- "CoreRoutine enabled, %@"
- "Harvested visit to map item, %{sensitive}@, source, %lu, location, %{sensitive}@, start, %@, end, %@, harvest type, %{public}lu, error, %{public}@"
- "Location services enabled, %@"
- "Submitted POI harvest success, %{public}s, access point count, %lu, location count, %lu, triggerType, %{public}d, harvestType, %{public}@, error, %{public}@"
- "fetchFeatureStatus(completion:)"
- "harvested %lu visits, mapItem, %{sensitive}@, success, %{public}@, error, %{public}@"
- "set routine enabled to %@"
- "unexpected files detected (%@)"
- "update routine enabled to %@"
```
