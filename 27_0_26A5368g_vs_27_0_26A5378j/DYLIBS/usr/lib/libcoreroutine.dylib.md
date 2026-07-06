## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-  __TEXT.__text: 0x67f0f8
-  __TEXT.__objc_methlist: 0x31ad8
+  __TEXT.__text: 0x684c28
+  __TEXT.__objc_methlist: 0x31df8
   __TEXT.__const: 0x45e8
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__swift5_typeref: 0x18a
-  __TEXT.__oslogstring: 0x7cec9
-  __TEXT.__cstring: 0x44c12
+  __TEXT.__oslogstring: 0x7dc59
+  __TEXT.__cstring: 0x4516c
   __TEXT.__swift5_capture: 0x7c
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x20

   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x27768
+  __TEXT.__gcc_except_tab: 0x27848
   __TEXT.__ustring: 0x3e
-  __TEXT.__unwind_info: 0xdd10
+  __TEXT.__unwind_info: 0xdd78
   __TEXT.__eh_frame: 0x3a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x34d0
-  __DATA_CONST.__objc_classlist: 0x15e0
+  __DATA_CONST.__const: 0x34f0
+  __DATA_CONST.__objc_classlist: 0x15f0
   __DATA_CONST.__objc_catlist: 0x3c0
   __DATA_CONST.__objc_protolist: 0x330
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x193c0
+  __DATA_CONST.__objc_selrefs: 0x19588
   __DATA_CONST.__objc_protorefs: 0x128
-  __DATA_CONST.__objc_superrefs: 0x11b8
+  __DATA_CONST.__objc_superrefs: 0x11c8
   __DATA_CONST.__objc_arraydata: 0x2d28
-  __DATA_CONST.__got: 0x2ef0
-  __AUTH_CONST.__const: 0xf370
-  __AUTH_CONST.__cfstring: 0x277c0
-  __AUTH_CONST.__objc_const: 0x53328
+  __DATA_CONST.__got: 0x2f30
+  __AUTH_CONST.__const: 0xf450
+  __AUTH_CONST.__cfstring: 0x27b80
+  __AUTH_CONST.__objc_const: 0x539b8
   __AUTH_CONST.__objc_intobj: 0x4800
   __AUTH_CONST.__objc_arrayobj: 0xeb8
-  __AUTH_CONST.__objc_doubleobj: 0xbc0
+  __AUTH_CONST.__objc_doubleobj: 0xbe0
   __AUTH_CONST.__objc_dictobj: 0x320
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0xde0
-  __AUTH.__objc_data: 0x2818
+  __AUTH.__objc_data: 0x2598
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x2778
-  __DATA.__data: 0x2a90
-  __DATA.__bss: 0x60
-  __DATA_DIRTY.__objc_ivar: 0x1130
-  __DATA_DIRTY.__objc_data: 0xb310
+  __DATA.__objc_ivar: 0x27e8
+  __DATA.__data: 0x2a98
+  __DATA.__bss: 0x58
+  __DATA_DIRTY.__objc_ivar: 0x1138
+  __DATA_DIRTY.__objc_data: 0xb630
   __DATA_DIRTY.__data: 0x5a8
-  __DATA_DIRTY.__bss: 0x188
+  __DATA_DIRTY.__bss: 0x190
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 20683
-  Symbols:   45108
-  CStrings:  20002
+  Functions: 20757
+  Symbols:   45262
+  CStrings:  20114
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ +[RTFloorTransitionExtractor extractFloorTransitionFeatures:startIndex:labeledSimplifiedData:clusterResult:visitUUID:analyticsMetrics:]
+ +[RTFloorTransitionExtractor extractTransitionsFromElevationData:]
+ -[RTAltimeterFloorMapDataManager createFloorMapForLOI:learnedLocationStore:visitManager:reply:]
+ -[RTAltimeterFloorMapDataManager createFloorMapForVisit:rawAltimeterDataManager:locationManager:learnedLocationStore:reply:]
+ -[RTAltimeterFloorMapDataManager createLOIFloorMapFromVisits:learnedLocationStore:visitManager:reply:]
+ -[RTAltimeterFloorMapDataManager initWithAltimeterFloorMapDataStore:defaultsManager:learnedLocationStore:visitStore:]
+ -[RTAltimeterFloorMapDataManager setVisitStore:]
+ -[RTAltimeterFloorMapDataManager visitStore]
+ -[RTClientListenerInternal altimeterFloorMapDataManager]
+ -[RTClientListenerInternal initWithAccountManager:assetManager:authorizationManager:bluePOITileManager:buildingPolygonManager:dataIntegrityManager:deviceLocationPredictor:diagnostics:eventAgentManager:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:platform:pointOfInterestSampler:predictedContextManager:purgeManager:safetyCacheStore:scenarioTriggerManager:userCurationManager:vehicleLocationProvider:visitManager:tripSegmentManager:workoutRouteManager:workoutScheduler:rawAltimeterDataManager:altimeterFloorMapDataManager:]
+ -[RTClientListenerInternal setAltimeterFloorMapDataManager:]
+ -[RTClusterLearnedRouteMetrics localCloudReconciliationMetrics]
+ -[RTClusterLearnedRouteMetrics prepareLocalCloudReconciliationMetrics]
+ -[RTClusterLearnedRouteMetrics setLocalCloudReconciliationMetrics:]
+ -[RTDaemonClientInternal altimeterFloorMapDataManager]
+ -[RTDaemonClientInternal createFloorMapForLOI:reply:]
+ -[RTDaemonClientInternal createFloorMapForVisit:reply:]
+ -[RTDaemonClientInternal fetchTransactionDiagnosticsSampledWithReply:]
+ -[RTDaemonClientInternal initWithQueue:accountManager:assetManager:authorizationManager:bluePOITileManager:buildingPolygonManager:dataIntegrityManager:deviceLocationPredictor:diagnostics:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:pointOfInterestSampler:predictedContextManager:purgeManager:safetyCacheStore:scenarioTriggerManager:userCurationManager:vehicleLocationProvider:visitManager:tripSegmentManager:workoutRouteManager:workoutScheduler:rawAltimeterDataManager:altimeterFloorMapDataManager:]
+ -[RTDaemonClientInternal setAltimeterFloorMapDataManager:]
+ -[RTDaemonClientInternal setTransactionDiagnosticsSampled:reply:]
+ -[RTDiagnostics fetchTransactionDiagnosticsSampled]
+ -[RTDiagnostics setTransactionDiagnosticsSampled:]
+ -[RTFloorTransitionExtractor _advanceBufferWithSample:]
+ -[RTFloorTransitionExtractor _calculateAndStoreLevelWindowIfReady:]
+ -[RTFloorTransitionExtractor _computeBufferStatistics:elevationVariance:stepAverage:weightedTime:]
+ -[RTFloorTransitionExtractor _endTransitionWithBufferMean:elevationVariance:stepAverage:weightedTime:]
+ -[RTFloorTransitionExtractor _extractFloorTransitionFeatures:startIndex:labeledSimplifiedData:clusterResult:visitUUID:analyticsMetrics:]
+ -[RTFloorTransitionExtractor _extractTransitionsFromElevationDataWithStartIndex:startIndex:]
+ -[RTFloorTransitionExtractor _initializeBufferWithSample:]
+ -[RTFloorTransitionExtractor _processNewSample:]
+ -[RTFloorTransitionExtractor _seedLevelWindowAnchorFromCurrentBuffer]
+ -[RTFloorTransitionExtractor levelWindowAnchorTime]
+ -[RTFloorTransitionExtractor setLevelWindowAnchorTime:]
+ -[RTFloorTransitionExtractor setSettleCandidateTime:]
+ -[RTFloorTransitionExtractor setTransitionEndElevationVariance:]
+ -[RTFloorTransitionExtractor setTransitionStartElevationVariance:]
+ -[RTFloorTransitionExtractor settleCandidateTime]
+ -[RTFloorTransitionExtractor transitionEndElevationVariance]
+ -[RTFloorTransitionExtractor transitionStartElevationVariance]
+ -[RTInferredMapItemFuser fusedInferredMapItemsUsingCandidates:referenceLocation:snapToBestKnownPlace:snapToBestAoi:includeNonWinningCandidates:unfilteredBluePOICandidates:error:]
+ -[RTLearnedFloorMap createClusteredFloorMapDataFromVisits:withDataManager:]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics .cxx_destruct]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics bootstrapFromCloudTriggered]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics clusterSyncCompletenessRatio]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics deviceOwnedClusterRatio]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics initForDefaultMetric]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics init]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics numDeviceOwnedClustersNotInCloudAfterSync]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics numDeviceOwnedClusters]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics numTraversalCountMismatches]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics postLearningSyncDurationMs]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics preLearningSyncDurationMs]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics setBootstrapFromCloudTriggered:]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics setClusterSyncCompletenessRatio:]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics setDeviceOwnedClusterRatio:]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics setNumDeviceOwnedClusters:]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics setNumDeviceOwnedClustersNotInCloudAfterSync:]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics setNumTraversalCountMismatches:]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics setPostLearningSyncDurationMs:]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics setPreLearningSyncDurationMs:]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics setSyncErrorCount:]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics setSyncSkippedDueToDeferral:]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics setToCloud:]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics setToLocal:]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics syncErrorCount]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics syncSkippedDueToDeferral]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics toCloud]
+ -[RTLearnedRouteLocalCloudReconciliationMetrics toLocal]
+ -[RTLearnedRouteSyncDirectionMetrics initForDefaultMetric]
+ -[RTLearnedRouteSyncDirectionMetrics init]
+ -[RTLearnedRouteSyncDirectionMetrics numClustersStored]
+ -[RTLearnedRouteSyncDirectionMetrics numClustersUpdated]
+ -[RTLearnedRouteSyncDirectionMetrics numRecenciesStored]
+ -[RTLearnedRouteSyncDirectionMetrics numSchedulesStored]
+ -[RTLearnedRouteSyncDirectionMetrics numWaypointClustersStored]
+ -[RTLearnedRouteSyncDirectionMetrics setNumClustersStored:]
+ -[RTLearnedRouteSyncDirectionMetrics setNumClustersUpdated:]
+ -[RTLearnedRouteSyncDirectionMetrics setNumRecenciesStored:]
+ -[RTLearnedRouteSyncDirectionMetrics setNumSchedulesStored:]
+ -[RTLearnedRouteSyncDirectionMetrics setNumWaypointClustersStored:]
+ -[RTTripClusterDataStoresContainer computePostSyncMetrics]
+ -[RTTripClusterDataStoresContainer reconciliationMetrics]
+ -[RTTripClusterDataStoresContainer resetReconciliationMetrics]
+ -[RTTripClusterManager _submitReconciliationMetrics]
+ OBJC_IVAR_$_RTClusterLearnedRouteMetrics._localCloudReconciliationMetrics
+ OBJC_IVAR_$_RTDaemonClientInternal._altimeterFloorMapDataManager
+ OBJC_IVAR_$_RTFloorTransitionExtractor._buffer
+ OBJC_IVAR_$_RTFloorTransitionExtractor._bufferCount
+ OBJC_IVAR_$_RTFloorTransitionExtractor._bufferEndTime
+ OBJC_IVAR_$_RTFloorTransitionExtractor._bufferTailIdx
+ OBJC_IVAR_$_RTFloorTransitionExtractor._bufferTotalWeight
+ OBJC_IVAR_$_RTFloorTransitionExtractor._bufferWeightedEleSum
+ OBJC_IVAR_$_RTFloorTransitionExtractor._bufferWeightedEleVarSum
+ OBJC_IVAR_$_RTFloorTransitionExtractor._bufferWeightedStepSum
+ OBJC_IVAR_$_RTFloorTransitionExtractor._bufferWeightedTimeSum
+ OBJC_IVAR_$_RTFloorTransitionExtractor._levelWindowAnchorTime
+ OBJC_IVAR_$_RTFloorTransitionExtractor._settleCandidateTime
+ OBJC_IVAR_$_RTFloorTransitionExtractor._transitionEndElevationVariance
+ OBJC_IVAR_$_RTFloorTransitionExtractor._transitionStartElevationVariance
+ OBJC_IVAR_$_RTLearnedRouteLocalCloudReconciliationMetrics._bootstrapFromCloudTriggered
+ OBJC_IVAR_$_RTLearnedRouteLocalCloudReconciliationMetrics._clusterSyncCompletenessRatio
+ OBJC_IVAR_$_RTLearnedRouteLocalCloudReconciliationMetrics._deviceOwnedClusterRatio
+ OBJC_IVAR_$_RTLearnedRouteLocalCloudReconciliationMetrics._numDeviceOwnedClusters
+ OBJC_IVAR_$_RTLearnedRouteLocalCloudReconciliationMetrics._numDeviceOwnedClustersNotInCloudAfterSync
+ OBJC_IVAR_$_RTLearnedRouteLocalCloudReconciliationMetrics._numTraversalCountMismatches
+ OBJC_IVAR_$_RTLearnedRouteLocalCloudReconciliationMetrics._postLearningSyncDurationMs
+ OBJC_IVAR_$_RTLearnedRouteLocalCloudReconciliationMetrics._preLearningSyncDurationMs
+ OBJC_IVAR_$_RTLearnedRouteLocalCloudReconciliationMetrics._syncErrorCount
+ OBJC_IVAR_$_RTLearnedRouteLocalCloudReconciliationMetrics._syncSkippedDueToDeferral
+ OBJC_IVAR_$_RTLearnedRouteLocalCloudReconciliationMetrics._toCloud
+ OBJC_IVAR_$_RTLearnedRouteLocalCloudReconciliationMetrics._toLocal
+ OBJC_IVAR_$_RTLearnedRouteSyncDirectionMetrics._numClustersStored
+ OBJC_IVAR_$_RTLearnedRouteSyncDirectionMetrics._numClustersUpdated
+ OBJC_IVAR_$_RTLearnedRouteSyncDirectionMetrics._numRecenciesStored
+ OBJC_IVAR_$_RTLearnedRouteSyncDirectionMetrics._numSchedulesStored
+ OBJC_IVAR_$_RTLearnedRouteSyncDirectionMetrics._numWaypointClustersStored
+ OBJC_IVAR_$_RTTripClusterDataStoresContainer._reconciliationMetrics
+ _NSFileTypeDirectory
+ _OBJC_CLASS_$_RTLearnedRouteLocalCloudReconciliationMetrics
+ _OBJC_CLASS_$_RTLearnedRouteSyncDirectionMetrics
+ _OBJC_METACLASS_$_RTLearnedRouteLocalCloudReconciliationMetrics
+ _OBJC_METACLASS_$_RTLearnedRouteSyncDirectionMetrics
+ _RTAnalyticsEventRTTripClusterLearnedRouteLocalCloudReconciliation
+ __102-[RTAltimeterFloorMapDataManager createLOIFloorMapFromVisits:learnedLocationStore:visitManager:reply:]_block_invoke
+ __124-[RTAltimeterFloorMapDataManager createFloorMapForVisit:rawAltimeterDataManager:locationManager:learnedLocationStore:reply:]_block_invoke
+ __178-[RTInferredMapItemFuser fusedInferredMapItemsUsingCandidates:referenceLocation:snapToBestKnownPlace:snapToBestAoi:includeNonWinningCandidates:unfilteredBluePOICandidates:error:]_block_invoke
+ __54-[RTClusterLearnedRouteMetrics submitToCoreAnalytics:]_block_invoke_2
+ __OBJC_$_CLASS_METHODS_RTFloorTransitionExtractor
+ __OBJC_$_INSTANCE_METHODS_RTLearnedRouteLocalCloudReconciliationMetrics
+ __OBJC_$_INSTANCE_METHODS_RTLearnedRouteSyncDirectionMetrics
+ __OBJC_$_INSTANCE_VARIABLES_RTLearnedRouteLocalCloudReconciliationMetrics
+ __OBJC_$_INSTANCE_VARIABLES_RTLearnedRouteSyncDirectionMetrics
+ __OBJC_$_PROP_LIST_RTLearnedRouteLocalCloudReconciliationMetrics
+ __OBJC_$_PROP_LIST_RTLearnedRouteSyncDirectionMetrics
+ __OBJC_CLASS_RO_$_RTLearnedRouteLocalCloudReconciliationMetrics
+ __OBJC_CLASS_RO_$_RTLearnedRouteSyncDirectionMetrics
+ __OBJC_METACLASS_RO_$_RTLearnedRouteLocalCloudReconciliationMetrics
+ __OBJC_METACLASS_RO_$_RTLearnedRouteSyncDirectionMetrics
+ ___102-[RTAltimeterFloorMapDataManager createLOIFloorMapFromVisits:learnedLocationStore:visitManager:reply:]_block_invoke
+ ___124-[RTAltimeterFloorMapDataManager createFloorMapForVisit:rawAltimeterDataManager:locationManager:learnedLocationStore:reply:]_block_invoke
+ ___178-[RTInferredMapItemFuser fusedInferredMapItemsUsingCandidates:referenceLocation:snapToBestKnownPlace:snapToBestAoi:includeNonWinningCandidates:unfilteredBluePOICandidates:error:]_block_invoke
+ ___178-[RTInferredMapItemFuser fusedInferredMapItemsUsingCandidates:referenceLocation:snapToBestKnownPlace:snapToBestAoi:includeNonWinningCandidates:unfilteredBluePOICandidates:error:]_block_invoke_2
+ ___50-[RTDiagnostics setTransactionDiagnosticsSampled:]_block_invoke
+ ___51-[RTDiagnostics fetchTransactionDiagnosticsSampled]_block_invoke
+ ___65-[RTDaemonClientInternal setTransactionDiagnosticsSampled:reply:]_block_invoke
+ ___70-[RTDaemonClientInternal fetchTransactionDiagnosticsSampledWithReply:]_block_invoke
+ ___block_descriptor_33_e5_v8?0l
+ ___block_descriptor_49_e8_32bs_e5_v8?0l
+ ___block_descriptor_56_e8_32s40r48r_e32_v28?0"NSArray"8B16"NSError"20l
+ ___block_descriptor_64_e8_32s40s48s56r_e17_v16?0"NSError"8l
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e17_v16?0"NSError"8l
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e36_v24?0"RTLearnedVisit"8"NSError"16l
+ _objc_msgSend$_advanceBufferWithSample:
+ _objc_msgSend$_calculateAndStoreLevelWindowIfReady:
+ _objc_msgSend$_computeBufferStatistics:elevationVariance:stepAverage:weightedTime:
+ _objc_msgSend$_endTransitionWithBufferMean:elevationVariance:stepAverage:weightedTime:
+ _objc_msgSend$_extractFloorTransitionFeatures:startIndex:labeledSimplifiedData:clusterResult:visitUUID:analyticsMetrics:
+ _objc_msgSend$_extractTransitionsFromElevationDataWithStartIndex:startIndex:
+ _objc_msgSend$_initializeBufferWithSample:
+ _objc_msgSend$_processNewSample:
+ _objc_msgSend$_seedLevelWindowAnchorFromCurrentBuffer
+ _objc_msgSend$_submitReconciliationMetrics
+ _objc_msgSend$bootstrapFromCloudTriggered
+ _objc_msgSend$clusterSyncCompletenessRatio
+ _objc_msgSend$computePostSyncMetrics
+ _objc_msgSend$createClusteredFloorMapDataFromVisits:withDataManager:
+ _objc_msgSend$createFloorMapForLOI:learnedLocationStore:visitManager:reply:
+ _objc_msgSend$createFloorMapForVisit:rawAltimeterDataManager:locationManager:learnedLocationStore:reply:
+ _objc_msgSend$createLOIFloorMapFromVisits:learnedLocationStore:visitManager:reply:
+ _objc_msgSend$deviceOwnedClusterRatio
+ _objc_msgSend$disableDistancePriorForHighDensity
+ _objc_msgSend$distancePriorWeight
+ _objc_msgSend$fetchTransactionDiagnosticsSampled
+ _objc_msgSend$fileAttributes
+ _objc_msgSend$fileType
+ _objc_msgSend$fusedInferredMapItemsUsingCandidates:referenceLocation:snapToBestKnownPlace:snapToBestAoi:includeNonWinningCandidates:unfilteredBluePOICandidates:error:
+ _objc_msgSend$initWithAccountManager:assetManager:authorizationManager:bluePOITileManager:buildingPolygonManager:dataIntegrityManager:deviceLocationPredictor:diagnostics:eventAgentManager:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:platform:pointOfInterestSampler:predictedContextManager:purgeManager:safetyCacheStore:scenarioTriggerManager:userCurationManager:vehicleLocationProvider:visitManager:tripSegmentManager:workoutRouteManager:workoutScheduler:rawAltimeterDataManager:altimeterFloorMapDataManager:
+ _objc_msgSend$initWithAltimeterFloorMapDataStore:defaultsManager:learnedLocationStore:visitStore:
+ _objc_msgSend$initWithIdentifier:apToModelMapping:date:disableDistancePriorForHighDensity:distancePriorWeight:distancePriors:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashedApToModelMappingDataURL:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:
+ _objc_msgSend$initWithQueue:accountManager:assetManager:authorizationManager:bluePOITileManager:buildingPolygonManager:dataIntegrityManager:deviceLocationPredictor:diagnostics:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:pointOfInterestSampler:predictedContextManager:purgeManager:safetyCacheStore:scenarioTriggerManager:userCurationManager:vehicleLocationProvider:visitManager:tripSegmentManager:workoutRouteManager:workoutScheduler:rawAltimeterDataManager:altimeterFloorMapDataManager:
+ _objc_msgSend$isRbcAllowed
+ _objc_msgSend$isTransactionDiagnosticsSampled
+ _objc_msgSend$numClustersStored
+ _objc_msgSend$numClustersUpdated
+ _objc_msgSend$numDeviceOwnedClusters
+ _objc_msgSend$numDeviceOwnedClustersNotInCloudAfterSync
+ _objc_msgSend$numRecenciesStored
+ _objc_msgSend$numSchedulesStored
+ _objc_msgSend$numTraversalCountMismatches
+ _objc_msgSend$numWaypointClustersStored
+ _objc_msgSend$postLearningSyncDurationMs
+ _objc_msgSend$preLearningSyncDurationMs
+ _objc_msgSend$prepareLocalCloudReconciliationMetrics
+ _objc_msgSend$reconciliationMetrics
+ _objc_msgSend$resetReconciliationMetrics
+ _objc_msgSend$setBootstrapFromCloudTriggered:
+ _objc_msgSend$setClusterSyncCompletenessRatio:
+ _objc_msgSend$setDeviceOwnedClusterRatio:
+ _objc_msgSend$setDisableDistancePriorForHighDensity:
+ _objc_msgSend$setDistancePriorWeight:
+ _objc_msgSend$setLocalCloudReconciliationMetrics:
+ _objc_msgSend$setNumClustersStored:
+ _objc_msgSend$setNumClustersUpdated:
+ _objc_msgSend$setNumDeviceOwnedClusters:
+ _objc_msgSend$setNumDeviceOwnedClustersNotInCloudAfterSync:
+ _objc_msgSend$setNumRecenciesStored:
+ _objc_msgSend$setNumSchedulesStored:
+ _objc_msgSend$setNumTraversalCountMismatches:
+ _objc_msgSend$setNumWaypointClustersStored:
+ _objc_msgSend$setPostLearningSyncDurationMs:
+ _objc_msgSend$setPreLearningSyncDurationMs:
+ _objc_msgSend$setSyncErrorCount:
+ _objc_msgSend$setSyncSkippedDueToDeferral:
+ _objc_msgSend$setTransactionDiagnosticsSampled:
+ _objc_msgSend$syncErrorCount
+ _objc_msgSend$syncSkippedDueToDeferral
+ _objc_msgSend$toCloud
+ _objc_msgSend$toLocal
+ _objc_msgSend$validateCacheDirectoryFileExtensionsWithSampleFilenames:error:
- -[RTAltimeterFloorMapDataManager initWithAltimeterFloorMapDataStore:defaultsManager:learnedLocationStore:]
- -[RTClientListenerInternal initWithAccountManager:assetManager:authorizationManager:bluePOITileManager:buildingPolygonManager:dataIntegrityManager:deviceLocationPredictor:diagnostics:eventAgentManager:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:platform:pointOfInterestSampler:predictedContextManager:purgeManager:safetyCacheStore:scenarioTriggerManager:userCurationManager:vehicleLocationProvider:visitManager:tripSegmentManager:workoutRouteManager:workoutScheduler:rawAltimeterDataManager:]
- -[RTDaemonClientInternal initWithQueue:accountManager:assetManager:authorizationManager:bluePOITileManager:buildingPolygonManager:dataIntegrityManager:deviceLocationPredictor:diagnostics:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:pointOfInterestSampler:predictedContextManager:purgeManager:safetyCacheStore:scenarioTriggerManager:userCurationManager:vehicleLocationProvider:visitManager:tripSegmentManager:workoutRouteManager:workoutScheduler:rawAltimeterDataManager:]
- -[RTFloorTransitionExtractor _accumulateLevelTime:]
- -[RTFloorTransitionExtractor _calculateAndStoreLevelWindow:]
- -[RTFloorTransitionExtractor _calculateEvent:atIndex:]
- -[RTFloorTransitionExtractor _endEdgeDetection:]
- -[RTFloorTransitionExtractor _endTransition:]
- -[RTFloorTransitionExtractor _updateTransition:]
- -[RTFloorTransitionExtractor elevationData]
- -[RTFloorTransitionExtractor extractFloorTransitionFeatures:startIndex:labeledSimplifiedData:clusterResult:visitUUID:analyticsMetrics:]
- -[RTFloorTransitionExtractor extractTransitionsFromElevationData:]
- -[RTFloorTransitionExtractor extractTransitionsFromElevationDataWithStartIndex:startIndex:]
- -[RTFloorTransitionExtractor processElevationChangeEvent:]
- -[RTFloorTransitionExtractor setElevationData:]
- -[RTFloorTransitionExtractor setStableElevationDuration:]
- -[RTFloorTransitionExtractor setTransitionEndUncertainty:]
- -[RTFloorTransitionExtractor setTransitionStartUncertainty:]
- -[RTFloorTransitionExtractor stableElevationDuration]
- -[RTFloorTransitionExtractor transitionEndUncertainty]
- -[RTFloorTransitionExtractor transitionStartUncertainty]
- -[RTInferredMapItemFuser fusedInferredMapItemsUsingCandidates:referenceLocation:snapToBestKnownPlace:snapToBestAoi:unfilteredBluePOICandidates:error:]
- -[RTLearnedFloorMap _createClusteredFloorMapDataFromVisits:withDataManager:]
- -[RTVisitPipelineModuleAltitudeEstimator rawAltimeterData]
- -[RTVisitPipelineModuleAltitudeEstimator setRawAltimeterData:]
- OBJC_IVAR_$_RTFloorTransitionExtractor._elevationData
- OBJC_IVAR_$_RTFloorTransitionExtractor._stableElevationDuration
- OBJC_IVAR_$_RTFloorTransitionExtractor._transitionEndUncertainty
- OBJC_IVAR_$_RTFloorTransitionExtractor._transitionStartUncertainty
- OBJC_IVAR_$_RTVisitPipelineModuleAltitudeEstimator._rawAltimeterData
- __150-[RTInferredMapItemFuser fusedInferredMapItemsUsingCandidates:referenceLocation:snapToBestKnownPlace:snapToBestAoi:unfilteredBluePOICandidates:error:]_block_invoke
- ___150-[RTInferredMapItemFuser fusedInferredMapItemsUsingCandidates:referenceLocation:snapToBestKnownPlace:snapToBestAoi:unfilteredBluePOICandidates:error:]_block_invoke
- ___150-[RTInferredMapItemFuser fusedInferredMapItemsUsingCandidates:referenceLocation:snapToBestKnownPlace:snapToBestAoi:unfilteredBluePOICandidates:error:]_block_invoke_2
- ___block_descriptor_56_e8_32s40s48r_e32_v28?0"NSArray"8B16"NSError"20l
- _objc_msgSend$_accumulateLevelTime:
- _objc_msgSend$_calculateAndStoreLevelWindow:
- _objc_msgSend$_calculateEvent:atIndex:
- _objc_msgSend$_createClusteredFloorMapDataFromVisits:withDataManager:
- _objc_msgSend$_deleteDefaultsForIdentifier:
- _objc_msgSend$_endEdgeDetection:
- _objc_msgSend$_endTransition:
- _objc_msgSend$_updateTransition:
- _objc_msgSend$currentState
- _objc_msgSend$detectedTransitions
- _objc_msgSend$elevationData
- _objc_msgSend$extractTransitionsFromElevationDataWithStartIndex:startIndex:
- _objc_msgSend$fusedInferredMapItemsUsingCandidates:referenceLocation:snapToBestKnownPlace:snapToBestAoi:unfilteredBluePOICandidates:error:
- _objc_msgSend$initWithAccountManager:assetManager:authorizationManager:bluePOITileManager:buildingPolygonManager:dataIntegrityManager:deviceLocationPredictor:diagnostics:eventAgentManager:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:platform:pointOfInterestSampler:predictedContextManager:purgeManager:safetyCacheStore:scenarioTriggerManager:userCurationManager:vehicleLocationProvider:visitManager:tripSegmentManager:workoutRouteManager:workoutScheduler:rawAltimeterDataManager:
- _objc_msgSend$initWithAltimeterFloorMapDataStore:defaultsManager:learnedLocationStore:
- _objc_msgSend$initWithIdentifier:apToModelMapping:date:distancePriors:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashedApToModelMappingDataURL:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:
- _objc_msgSend$initWithIdentifier:bugCaptureManager:defaultsManager:diagnostics:persistenceManager:timerManager:
- _objc_msgSend$initWithQueue:accountManager:assetManager:authorizationManager:bluePOITileManager:buildingPolygonManager:dataIntegrityManager:deviceLocationPredictor:diagnostics:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:pointOfInterestSampler:predictedContextManager:purgeManager:safetyCacheStore:scenarioTriggerManager:userCurationManager:vehicleLocationProvider:visitManager:tripSegmentManager:workoutRouteManager:workoutScheduler:rawAltimeterDataManager:
- _objc_msgSend$processElevationChangeEvent:
- _objc_msgSend$setCurrentState:
- _objc_msgSend$setDetectedTransitions:
- _objc_msgSend$setElevationData:
- _objc_msgSend$setStableElevationDuration:
- _objc_msgSend$setTransitionEndElevation:
- _objc_msgSend$setTransitionEndStepCount:
- _objc_msgSend$setTransitionEndTime:
- _objc_msgSend$setTransitionEndUncertainty:
- _objc_msgSend$setTransitionStartElevation:
- _objc_msgSend$setTransitionStartStepCount:
- _objc_msgSend$setTransitionStartTime:
- _objc_msgSend$setTransitionStartUncertainty:
- _objc_msgSend$stableElevationDuration
- _objc_msgSend$transitionEndElevation
- _objc_msgSend$transitionEndStepCount
- _objc_msgSend$transitionEndTime
- _objc_msgSend$transitionEndUncertainty
- _objc_msgSend$transitionStartElevation
- _objc_msgSend$transitionStartStepCount
- _objc_msgSend$transitionStartTime
- _objc_msgSend$transitionStartUncertainty
CStrings:
+ "#altimeter,_fetchRawAltimeterDataFromStartTime,isContinue,%d,altimeterData,%lu"
+ "#altimeter,_fetchRawAltimeterDataFromStartTime,timeout,%@"
+ "#altimeter,advanceBufferWithSample,buffer overflow,count,%lu,visitUUID,%{private}@"
+ "#altimeter,calculateAndStoreLevelWindow,startWeightedTime,%.3f,endWeightedTime,%.3f,deltaH,%.3f,visitUUID,%{private}@"
+ "#altimeter,calculateAndStoreLevelWindowIfReady,no post-incorporation buffer stats,visitUUID,%{private}@"
+ "#altimeter,calculateAndStoreTransitionFeatures,isLevelWindow,%d,startTime,%.3f,endTime,%.3f,altitudeChange,%.3f,uncertainty,%.3f,duration,%.1f,stepCountChange,%.2f,visitUUID,%{private}@"
+ "#altimeter,createFloorTransitionModelEntriesFromLabeledData,values exceed int16_t,startFloorIdx,%lu,endFloorIdx,%lu,occurrenceCount,%lu,visitUUID,%{private}@"
+ "#altimeter,createGroupedAltimeterData,no positive-duration samples in time range (invalid or missing timestamps),startTime,%{private}@,endTime,%{private}@,visitUUID,%{private}@"
+ "#altimeter,createGroupedAltimeterData,pointCount,%lu,mean,%.2f,uncertainty,%.2f,visitUUID,%{private}@"
+ "#altimeter,endTransition,t_candidate,%.3f,t_end,%.3f,sustained,%.1f,visitUUID,%{private}@"
+ "#altimeter,enumerate visit elevation profile,timestamp,%f,altitude,%f,uncertainty,%f,sampleDuration,%f,visitUUID,%{private}@"
+ "#altimeter,processEventInLevelState,unexpected missing buffer stats,bufferCount,%lu,visitUUID,%{private}@"
+ "#altimeter,processEventInTransitioningState,no post-incorporation buffer stats,visitUUID,%{private}@"
+ "#altimeter,processEventInTransitioningState,unexpected missing buffer stats,bufferCount,%lu,visitUUID,%{private}@"
+ "#altimeter,processNewSample,state,%lu,H_t,%.3f,H_bar_pre,%.3f,sampleEnd,%.3f,sampleDuration,%.3f,visitUUID,%{private}@"
+ "#altimeter,processNewSample,unexpected data gap,gapSize,%.1f,visitUUID,%{private}@"
+ "#altimeter,reset state machine"
+ "#altimeter,seedLevelWindowAnchor,no buffer stats from initialized buffer,visitUUID,%{private}@"
+ "#altimeter,settle candidate marked,t_candidate,%.3f,H_t,%.3f,H_bar_pre,%.3f,visitUUID,%{private}@"
+ "#altimeter,settle candidate reset,H_t,%.3f,H_bar_pre,%.3f,visitUUID,%{private}@"
+ "#altimeter,startEdgeDetection,t_i,%.3f,H_i,%.3f,startSteps,%.2f,visitUUID,%{private}@"
+ "#altimeter,startEdgeDetection,unexpected missing buffer stats,visitUUID,%{private}@"
+ "#altimeter,startTransition,H_t,%.3f,H_bar_pre,%.3f,sampleEnd,%.3f,visitUUID,%{private}@"
+ "%@, %@, Cache file count exceeded scan cap (%lu) at %@; stopping scan"
+ "%@, %@, Found unexpected files (sampled first %lu)"
+ "%@, %@, Skipping cache file-extension check (not internal install)"
+ "%@, fetched transaction diagnostics sampled: %@"
+ "%@, set transaction diagnostics sampled to %@"
+ "%@, skipping append of non-winning candidates"
+ "%@,computePostSyncMetrics: local store is empty, skipping per-cluster checks"
+ "%@,computePostSyncMetrics: ratio=%.2f deviceOwned=%d notInCloud=%d traversalCountMismatches=%d deviceOwnedRatio=%.2f"
+ "%@:%@,Local cloud reconciliation metrics collection"
+ "-[RTAltimeterFloorMapDataManager createFloorMapForLOI:learnedLocationStore:visitManager:reply:]"
+ "-[RTAltimeterFloorMapDataManager createFloorMapForVisit:rawAltimeterDataManager:locationManager:learnedLocationStore:reply:]"
+ "-[RTAltimeterFloorMapDataManager createLOIFloorMapFromVisits:learnedLocationStore:visitManager:reply:]"
+ "-[RTDaemonClientInternal createFloorMapForLOI:reply:]"
+ "-[RTDaemonClientInternal createFloorMapForVisit:reply:]"
+ "08:44:53"
+ "AltimeterFloorMapDataManager is nil"
+ "BootstrapFromCloudTriggered"
+ "ClusterSyncCompletenessRatio"
+ "DeviceOwnedClusterRatio"
+ "Failed to create LOI floor map data object"
+ "Failed to create altitude estimator"
+ "Failed to create clustered floor map"
+ "Floor map result missing floorMapArray"
+ "Invalid parameter not satisfying: altimeterFloorMapDataManager"
+ "Invalid parameter not satisfying: loiUUID (in %s:%d)"
+ "Invalid visit properties"
+ "Invalid visit time bounds"
+ "Jun 27 2026"
+ "No learned visits found in date interval"
+ "NumClustersStoredToCloud"
+ "NumClustersStoredToLocal"
+ "NumClustersUpdatedInCloud"
+ "NumClustersUpdatedInLocal"
+ "NumDeviceOwnedClusters"
+ "NumDeviceOwnedClustersNotInCloudAfterSync"
+ "NumRecenciesStoredToCloud"
+ "NumRecenciesStoredToLocal"
+ "NumSchedulesStoredToCloud"
+ "NumSchedulesStoredToLocal"
+ "NumTraversalCountMismatches"
+ "NumWaypointClustersStoredToCloud"
+ "NumWaypointClustersStoredToLocal"
+ "PostLearningSyncDurationMs"
+ "PreLearningSyncDurationMs"
+ "R"
+ "RTAltimeterFloorMapDataManager successfully initialized."
+ "RTTransactionManager shared instance not set, cannot fetch sampling state"
+ "RTTransactionManager shared instance not set, cannot override sampling"
+ "Skipping data integrity validation registration (not internal install)"
+ "Skipping routined IPS log check (RBC not allowed)"
+ "SyncErrorCount"
+ "SyncSkippedDueToDeferral"
+ "Transaction diagnostics sampling override set to %@"
+ "createFloorMapForLOI, loiUUID,%{public}@"
+ "createFloorMapForVisit, failed to create RTVisitPipelineModuleAltitudeEstimator"
+ "createFloorMapForVisit, invalid visit: entry,%{public}@, exit,%{public}@, identifier,%{public}@"
+ "createFloorMapForVisit, learnedLocationStore store failed: %{public}@"
+ "createFloorMapForVisit, rawAltimeterDataManager is nil"
+ "createFloorMapForVisit, reply, visit identifier,%{public}@, updated visit,%{public}@, latency,%.2f"
+ "createFloorMapForVisit, stored learned visit, identifier,%{public}@"
+ "createFloorMapForVisit, validation FAILED — no RTLearnedVisit found for identifier,%{public}@"
+ "createFloorMapForVisit, validation OK — RTLearnedVisit found: identifier,%{public}@, entry,%{public}@, exit,%{public}@"
+ "createFloorMapForVisit, validation fetch failed: %{public}@"
+ "createFloorMapForVisit, visit identifier,%{public}@, entry,%{public}@, exit,%{public}@"
+ "createLOIFloorMapFromVisits, RTVisitMO entries purged"
+ "createLOIFloorMapFromVisits, failed to create RTAltimeterFloorMapData for LOI: %{public}@"
+ "createLOIFloorMapFromVisits, failed to create clustered floor map for LOI: %{public}@"
+ "createLOIFloorMapFromVisits, failed to store LOI floor map: %{public}@, error: %{public}@"
+ "createLOIFloorMapFromVisits, fetch failed: %{public}@"
+ "createLOIFloorMapFromVisits, fetched %{public}lu learned visit(s) for clustering"
+ "createLOIFloorMapFromVisits, fetching learned visits in interval %{public}@ — %{public}@"
+ "createLOIFloorMapFromVisits, floor map result missing floorMapArray for LOI: %{public}@"
+ "createLOIFloorMapFromVisits, invalid visit time bounds for LOI: %{public}@"
+ "createLOIFloorMapFromVisits, loiUUID,%{public}@"
+ "createLOIFloorMapFromVisits, no learned visits found — ensure createFloorMapForVisit ran first"
+ "createLOIFloorMapFromVisits, success, loiUUID,%{public}@, latency,%.2f"
+ "createLOIFloorMapFromVisits, visit purge failed: %{public}@"
+ "createLOIFloorMapFromVisits,,%d,learned visit,%{public}@"
+ "currentLOIUUID"
+ "r"
+ "rawAltimeterDataManager is nil"
+ "routined.LearnedRoutesLocalCloudReconciliation"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x93"
- "#altimeter,_fetchRawAltimeterDataFromStartTime,isContinue,%d,_rawAltimeterData,%lu,altimeterData,%lu"
- "#altimeter,calculateAndStoreLevelWindow,missing window start data,visitUUID,%{private}@"
- "#altimeter,calculateAndStoreLevelWindow,stored level window,startTime,%.3f,endTime,%.3f,deltaH,%.3f,visitUUID,%{private}@"
- "#altimeter,calculateAndStoreTransitionFeatures,added transition,startTime,%.3f,endTime,%.3f,altitudeChange,%.3f,uncertainty,%.3f,duration,%.1f,stepCountChange,%d,visitUUID,%{private}@"
- "#altimeter,createFloorTransitionModelEntriesFromLabeledData,missing or mismatched cluster uncertainties,centers,%lu,uncertainties,%lu,visitUUID,%{private}@"
- "#altimeter,createGroupedAltimeterData,pointCount,%d,mean,%.2f,uncertainty,%.2f,visitUUID,%{private}@"
- "#altimeter,endEdgeDetection,fallback to event data,time,%.3f,altitude,%.3f,visitUUID,%{private}@"
- "#altimeter,endEdgeDetection,using stored transition end,time,%.3f,altitude,%.3f,visitUUID,%{private}@"
- "#altimeter,endTransition,stableDuration,%.1f,transitionStartTime,%.3f,eventTimestamp,%.3f,visitUUID,%{private}@"
- "#altimeter,enumerate visit elevation profile,timestamp,%f,altitude,%f,uncertainty,%f,visitUUID,%{private}@"
- "#altimeter,processElevationChangeEvent,state,%lu,deltaH,%.3f,deltaT,%.1f,altitude,%.3f,visitUUID,%{private}@"
- "#altimeter,reset state machine,visitUUID,%{private}@"
- "#altimeter,startEdgeDetection,transition start,time,%.3f,altitude,%.3f,visitUUID,%{private}@"
- "#altimeter,startTransition,deltaH,%.3f,altitude,%.3f,timestamp,%.3f,visitUUID,%{private}@"
- "#altimeter,startTransition,determined start,time,%.3f,altitude,%.3f,visitUUID,%{private}@"
- "#altimeter,updateTransition,resetting stable duration,deltaH,%.3f,altitude,%.3f,visitUUID,%{private}@"
- "$!"
- "%@, %@, Found %lu files with unexpected extensions"
- "09:08:57"
- "Invalid parameter not satisfying: address.mergedThoroughfare.length > 0"
- "Jun 12 2026"
- "Skipping IPS log check on customer install"
- "b"
- "\x94"

```
