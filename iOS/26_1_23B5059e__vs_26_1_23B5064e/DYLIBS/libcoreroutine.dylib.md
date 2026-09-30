## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-1069.0.1.0.0
-  __TEXT.__text: 0x614ff0
+1069.0.2.0.0
+  __TEXT.__text: 0x6134cc
   __TEXT.__auth_stubs: 0x2190
-  __TEXT.__objc_methlist: 0x31510
-  __TEXT.__const: 0x4928
+  __TEXT.__objc_methlist: 0x313a0
+  __TEXT.__const: 0x48e8
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__swift5_typeref: 0x1d3
-  __TEXT.__oslogstring: 0x78185
-  __TEXT.__cstring: 0x45fcb
+  __TEXT.__oslogstring: 0x77b5e
+  __TEXT.__cstring: 0x45bea
   __TEXT.__swift5_capture: 0x9c
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c

   __TEXT.__swift5_reflstr: 0x14
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x28d74
+  __TEXT.__gcc_except_tab: 0x28b58
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0xddc8
+  __TEXT.__unwind_info: 0xdd98
   __TEXT.__eh_frame: 0x390
-  __TEXT.__objc_classname: 0x58cf
-  __TEXT.__objc_methname: 0x92fc9
-  __TEXT.__objc_methtype: 0xd0eb
-  __TEXT.__objc_stubs: 0x566c0
-  __DATA_CONST.__got: 0x3150
-  __DATA_CONST.__const: 0xf6c0
-  __DATA_CONST.__objc_classlist: 0x1548
+  __TEXT.__objc_classname: 0x58ba
+  __TEXT.__objc_methname: 0x9267c
+  __TEXT.__objc_methtype: 0xd0b5
+  __TEXT.__objc_stubs: 0x562c0
+  __DATA_CONST.__got: 0x3148
+  __DATA_CONST.__const: 0xf650
+  __DATA_CONST.__objc_classlist: 0x1540
   __DATA_CONST.__objc_catlist: 0x3a8
   __DATA_CONST.__objc_protolist: 0x358
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19788
+  __DATA_CONST.__objc_selrefs: 0x19698
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x1190
   __DATA_CONST.__objc_arraydata: 0x2b88
   __AUTH_CONST.__auth_got: 0x10d8
-  __AUTH_CONST.__const: 0x32e0
-  __AUTH_CONST.__cfstring: 0x290a0
-  __AUTH_CONST.__objc_const: 0x50fb8
+  __AUTH_CONST.__const: 0x32a0
+  __AUTH_CONST.__cfstring: 0x28cc0
+  __AUTH_CONST.__objc_const: 0x50c58
   __AUTH_CONST.__objc_intobj: 0x48c0
   __AUTH_CONST.__objc_arrayobj: 0xf00
-  __AUTH_CONST.__objc_doubleobj: 0xb00
+  __AUTH_CONST.__objc_doubleobj: 0xb10
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x2118
-  __DATA.__objc_ivar: 0x25e0
-  __DATA.__data: 0x2cc8
+  __AUTH.__objc_data: 0x20c8
+  __DATA.__objc_ivar: 0x2594
+  __DATA.__data: 0x2cc0
   __DATA.__bss: 0x70
-  __DATA_DIRTY.__objc_ivar: 0x116c
+  __DATA_DIRTY.__objc_ivar: 0x117c
   __DATA_DIRTY.__objc_data: 0xb470
   __DATA_DIRTY.__data: 0x5c8
   __DATA_DIRTY.__bss: 0x200

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 366DC65F-9B67-31E9-8E46-3F649D28FFE8
-  Functions: 20319
-  Symbols:   65598
-  CStrings:  40571
+  UUID: 388FFF1B-66CB-3745-B894-5606D00904C4
+  Functions: 20282
+  Symbols:   65456
+  CStrings:  40424
 
Symbols:
+ +[RTPOIHarvestUtilities harvestCuration:mapItem:referenceLocations:poiHarvester:error:]
+ -[CLPPoiHarvest(RTExtensions) initWithMapItem:accessPoints:locations:motionActivities:]
+ -[CLPPoiTriggerEvent(RTExtensions) initWithMapItem:date:]
+ -[NSError(RTExtensions) hasAOIInferenceError]
+ -[NSError(RTExtensions) hasStorageFullError]
+ -[RTBluePOIMonitor aoiRefreshBackoffInterval]
+ -[RTBluePOIMonitor distanceToRefreshAOI]
+ -[RTBluePOIMonitor lastAOIRefreshResult]
+ -[RTBluePOIMonitor nextAOIRefreshDate]
+ -[RTBluePOIMonitor setAoiRefreshBackoffInterval:]
+ -[RTBluePOIMonitor setDistanceToRefreshAOI:]
+ -[RTBluePOIMonitor setLastAOIRefreshResult:]
+ -[RTBluePOIMonitor setNextAOIRefreshDate:]
+ -[RTBluePOIMonitor shouldRefreshAOIAtLocation:]
+ -[RTMapServiceManager inferLocalBluePOIWithReferenceLocation:locations:accessPoints:bluePOITile:signalEnv:refreshAOI:handler:]
+ -[RTPOIHarvester _motionActivitiesFrom:to:error:]
+ -[RTPOIHarvester _poiHarvestForFingerprint:mapItem:referenceLocations:endDate:error:]
+ -[RTPOIHarvester harvestPOI:mapItemSource:referenceLocations:startDate:endDate:harvestType:error:]
+ ___121+[RTPOIHarvestUtilities fingerprintsBetweenStartDate:endDate:isTimeWindowFallback:settledState:fingerprintManager:error:]_block_invoke.5
+ ___126-[RTMapServiceManager inferLocalBluePOIWithReferenceLocation:locations:accessPoints:bluePOITile:signalEnv:refreshAOI:handler:]_block_invoke
+ ___126-[RTMapServiceManager inferLocalBluePOIWithReferenceLocation:locations:accessPoints:bluePOITile:signalEnv:refreshAOI:handler:]_block_invoke_2
+ ___131-[RTBluePOIMonitor _fetchLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:skipAggregation:collectMetrics:error:]_block_invoke.95
+ ___133-[RTBluePOIMonitor localBluePOIResultForReferenceLocation:locations:accessPoints:signalEnv:tileRequestPriority:collectMetrics:error:]_block_invoke.61
+ ___49-[RTPOIHarvester _motionActivitiesFrom:to:error:]_block_invoke
+ ___98-[RTPOIHarvester harvestPOI:mapItemSource:referenceLocations:startDate:endDate:harvestType:error:]_block_invoke
+ ___block_descriptor_93_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s72l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.1253
+ ___block_literal_global.49
+ _objc_msgSend$_motionActivitiesFrom:to:error:
+ _objc_msgSend$_poiHarvestForFingerprint:mapItem:referenceLocations:endDate:error:
+ _objc_msgSend$aoiRefreshBackoffInterval
+ _objc_msgSend$distanceToNearestAOILowerBound
+ _objc_msgSend$distanceToRefreshAOI
+ _objc_msgSend$harvestCuration:mapItem:referenceLocations:poiHarvester:error:
+ _objc_msgSend$harvestPOI:mapItemSource:referenceLocations:startDate:endDate:harvestType:error:
+ _objc_msgSend$hasAOIInferenceError
+ _objc_msgSend$hasStorageFullError
+ _objc_msgSend$inferLocalBluePOIWithReferenceLocation:locations:accessPoints:bluePOITile:signalEnv:refreshAOI:handler:
+ _objc_msgSend$initWithMapItem:accessPoints:locations:motionActivities:
+ _objc_msgSend$initWithMapItem:date:
+ _objc_msgSend$initWithPOIConfidences:aoiConfidences:distanceToNearestAOILowerBound:referenceLocation:queryTime:
+ _objc_msgSend$lastAOIRefreshResult
+ _objc_msgSend$nextAOIRefreshDate
+ _objc_msgSend$setAoiRefreshBackoffInterval:
+ _objc_msgSend$setDistanceToRefreshAOI:
+ _objc_msgSend$setLastAOIRefreshResult:
+ _objc_msgSend$setNextAOIRefreshDate:
+ _objc_msgSend$shouldRefreshAOIAtLocation:
- +[RTPOIHarvestUtilities harvestCuration:mapItem:visitLocations:poiHarvester:error:]
- -[CLPPoiHarvest(RTExtensions) initWithMapItem:accessPoints:locations:motionActivities:triggerType:]
- -[CLPPoiTriggerEvent(RTExtensions) initWithMapItem:triggerType:date:]
- -[RTMapServiceManager inferLocalBluePOIWithReferenceLocation:locations:accessPoints:bluePOITile:signalEnv:handler:]
- -[RTPOIHarvester _augmentedLocationsForAccessPoints:metrics:error:]
- -[RTPOIHarvester _fingerprintAccessPointsForSettledState:withinInterval:metrics:error:]
- -[RTPOIHarvester _fingerprintAccessPointsWithinInterval:harvestType:metrics:error:]
- -[RTPOIHarvester _harvestPOI:mapItemSource:accessPointArrays:referenceLocations:harvestType:metrics:error:]
- -[RTPOIHarvester _motionActivitiesWithinInterval:error:]
- -[RTPOIHarvester _poiHarvestForAccessPoints:mapItem:referenceLocations:harvestType:metrics:]
- -[RTPOIHarvester harvestPOI:mapItemSource:visitLocations:visitEntryDate:visitExitDate:harvestType:error:]
- -[RTPOIHarvesterMetrics fingerprintErrorCount]
- -[RTPOIHarvesterMetrics harvestCreationCount]
- -[RTPOIHarvesterMetrics harvestSubmissionCount]
- -[RTPOIHarvesterMetrics harvestSubmissionErrorCount]
- -[RTPOIHarvesterMetrics harvestType]
- -[RTPOIHarvesterMetrics mapItemCopyErrorCount]
- -[RTPOIHarvesterMetrics referenceLocationsCount]
- -[RTPOIHarvesterMetrics setFingerprintErrorCount:]
- -[RTPOIHarvesterMetrics setHarvestCreationCount:]
- -[RTPOIHarvesterMetrics setHarvestSubmissionCount:]
- -[RTPOIHarvesterMetrics setHarvestSubmissionErrorCount:]
- -[RTPOIHarvesterMetrics setHarvestType:]
- -[RTPOIHarvesterMetrics setMapItemCopyErrorCount:]
- -[RTPOIHarvesterMetrics setReferenceLocationsCount:]
- -[RTPOIHarvesterMetrics setSettledFingerprintCountWithTimeWindowFallback:]
- -[RTPOIHarvesterMetrics setSettledFingerprintCountWithoutTimeWindowFallback:]
- -[RTPOIHarvesterMetrics setTotalAccessPointCount:]
- -[RTPOIHarvesterMetrics setTotalAccessPointErrorCount:]
- -[RTPOIHarvesterMetrics setTotalEstimatedFingerprintLocationsCount:]
- -[RTPOIHarvesterMetrics setTotalEstimatedFingerprintLocationsErrorCount:]
- -[RTPOIHarvesterMetrics setTotalFetchedFingerprintLocationsCount:]
- -[RTPOIHarvesterMetrics setTotalFetchedFingerprintLocationsErrorCount:]
- -[RTPOIHarvesterMetrics setTotalMotionActivitiesCount:]
- -[RTPOIHarvesterMetrics setTotalMotionActivitiesErrorCount:]
- -[RTPOIHarvesterMetrics setUnsettledFingerprintCountWithTimeWindowFallback:]
- -[RTPOIHarvesterMetrics setUnsettledFingerprintCountWithoutTimeWindowFallback:]
- -[RTPOIHarvesterMetrics settledFingerprintCountWithTimeWindowFallback]
- -[RTPOIHarvesterMetrics settledFingerprintCountWithoutTimeWindowFallback]
- -[RTPOIHarvesterMetrics submit]
- -[RTPOIHarvesterMetrics totalAccessPointCount]
- -[RTPOIHarvesterMetrics totalAccessPointErrorCount]
- -[RTPOIHarvesterMetrics totalEstimatedFingerprintLocationsCount]
- -[RTPOIHarvesterMetrics totalEstimatedFingerprintLocationsErrorCount]
- -[RTPOIHarvesterMetrics totalFetchedFingerprintLocationsCount]
- -[RTPOIHarvesterMetrics totalFetchedFingerprintLocationsErrorCount]
- -[RTPOIHarvesterMetrics totalMotionActivitiesCount]
- -[RTPOIHarvesterMetrics totalMotionActivitiesErrorCount]
- -[RTPOIHarvesterMetrics unsettledFingerprintCountWithTimeWindowFallback]
- -[RTPOIHarvesterMetrics unsettledFingerprintCountWithoutTimeWindowFallback]
- _OBJC_CLASS_$_RTPOIHarvesterMetrics
- _OBJC_IVAR_$_RTPOIHarvesterMetrics._fingerprintErrorCount
- _OBJC_IVAR_$_RTPOIHarvesterMetrics._harvestCreationCount
- _OBJC_IVAR_$_RTPOIHarvesterMetrics._harvestSubmissionCount
- _OBJC_IVAR_$_RTPOIHarvesterMetrics._harvestSubmissionErrorCount
- _OBJC_IVAR_$_RTPOIHarvesterMetrics._harvestType
- _OBJC_IVAR_$_RTPOIHarvesterMetrics._mapItemCopyErrorCount
- _OBJC_IVAR_$_RTPOIHarvesterMetrics._referenceLocationsCount
- _OBJC_IVAR_$_RTPOIHarvesterMetrics._settledFingerprintCountWithTimeWindowFallback
- _OBJC_IVAR_$_RTPOIHarvesterMetrics._settledFingerprintCountWithoutTimeWindowFallback
- _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalAccessPointCount
- _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalAccessPointErrorCount
- _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalEstimatedFingerprintLocationsCount
- _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalEstimatedFingerprintLocationsErrorCount
- _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalFetchedFingerprintLocationsCount
- _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalFetchedFingerprintLocationsErrorCount
- _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalMotionActivitiesCount
- _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalMotionActivitiesErrorCount
- _OBJC_IVAR_$_RTPOIHarvesterMetrics._unsettledFingerprintCountWithTimeWindowFallback
- _OBJC_IVAR_$_RTPOIHarvesterMetrics._unsettledFingerprintCountWithoutTimeWindowFallback
- _OBJC_METACLASS_$_RTPOIHarvesterMetrics
- _RTAnalyticsEventBluePOIHarvest
- __OBJC_$_INSTANCE_METHODS_RTPOIHarvesterMetrics
- __OBJC_$_INSTANCE_VARIABLES_RTPOIHarvesterMetrics
- __OBJC_$_PROP_LIST_RTPOIHarvesterMetrics
- __OBJC_CLASS_RO_$_RTPOIHarvesterMetrics
- __OBJC_METACLASS_RO_$_RTPOIHarvesterMetrics
- ___105-[RTPOIHarvester harvestPOI:mapItemSource:visitLocations:visitEntryDate:visitExitDate:harvestType:error:]_block_invoke
- ___115-[RTMapServiceManager inferLocalBluePOIWithReferenceLocation:locations:accessPoints:bluePOITile:signalEnv:handler:]_block_invoke
- ___115-[RTMapServiceManager inferLocalBluePOIWithReferenceLocation:locations:accessPoints:bluePOITile:signalEnv:handler:]_block_invoke_2
- ___121+[RTPOIHarvestUtilities fingerprintsBetweenStartDate:endDate:isTimeWindowFallback:settledState:fingerprintManager:error:]_block_invoke.6
- ___131-[RTBluePOIMonitor _fetchLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:skipAggregation:collectMetrics:error:]_block_invoke.93
- ___133-[RTBluePOIMonitor localBluePOIResultForReferenceLocation:locations:accessPoints:signalEnv:tileRequestPriority:collectMetrics:error:]_block_invoke.55
- ___31-[RTPOIHarvesterMetrics submit]_block_invoke
- ___31-[RTPOIHarvesterMetrics submit]_block_invoke.184
- ___56-[RTPOIHarvester _motionActivitiesWithinInterval:error:]_block_invoke
- ___67-[RTPOIHarvester _augmentedLocationsForAccessPoints:metrics:error:]_block_invoke
- ___90+[RTPOIHarvestUtilities locationsForAccessPoints:harvestParameters:locationManager:error:]_block_invoke
- ___92-[RTPOIHarvester _poiHarvestForAccessPoints:mapItem:referenceLocations:harvestType:metrics:]_block_invoke
- ___block_descriptor_32_e35_q24?0"RTLocation"8"RTLocation"16l
- ___block_descriptor_32_e49_q24?0"RTWiFiAccessPoint"8"RTWiFiAccessPoint"16l
- ___block_descriptor_56_e8_32s40w_e19_"NSDictionary"8?0lw40l8s32l8
- ___block_descriptor_92_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s72l8s40l8s48l8s56l8s64l8
- ___block_literal_global.1251
- ___block_literal_global.212
- ___block_literal_global.295
- ___block_literal_global.42
- ___block_literal_global.59
- ___block_literal_global.92
- _objc_msgSend$_augmentedLocationsForAccessPoints:metrics:error:
- _objc_msgSend$_fingerprintAccessPointsForSettledState:withinInterval:metrics:error:
- _objc_msgSend$_fingerprintAccessPointsWithinInterval:harvestType:metrics:error:
- _objc_msgSend$_harvestPOI:mapItemSource:accessPointArrays:referenceLocations:harvestType:metrics:error:
- _objc_msgSend$_motionActivitiesWithinInterval:error:
- _objc_msgSend$_poiHarvestForAccessPoints:mapItem:referenceLocations:harvestType:metrics:
- _objc_msgSend$accessPointsCount
- _objc_msgSend$fingerprintErrorCount
- _objc_msgSend$harvestCreationCount
- _objc_msgSend$harvestCuration:mapItem:visitLocations:poiHarvester:error:
- _objc_msgSend$harvestPOI:mapItemSource:visitLocations:visitEntryDate:visitExitDate:harvestType:error:
- _objc_msgSend$harvestSubmissionCount
- _objc_msgSend$harvestSubmissionErrorCount
- _objc_msgSend$harvestType
- _objc_msgSend$inferLocalBluePOIWithReferenceLocation:locations:accessPoints:bluePOITile:signalEnv:handler:
- _objc_msgSend$initWithMapItem:accessPoints:locations:motionActivities:triggerType:
- _objc_msgSend$initWithMapItem:triggerType:date:
- _objc_msgSend$initWithPOIConfidences:aoiConfidences:referenceLocation:queryTime:
- _objc_msgSend$locationsCount
- _objc_msgSend$mapItemCopyErrorCount
- _objc_msgSend$referenceLocationsCount
- _objc_msgSend$setFingerprintErrorCount:
- _objc_msgSend$setHarvestCreationCount:
- _objc_msgSend$setHarvestSubmissionCount:
- _objc_msgSend$setHarvestSubmissionErrorCount:
- _objc_msgSend$setHarvestType:
- _objc_msgSend$setMapItemCopyErrorCount:
- _objc_msgSend$setReferenceLocationsCount:
- _objc_msgSend$setSettledFingerprintCountWithTimeWindowFallback:
- _objc_msgSend$setSettledFingerprintCountWithoutTimeWindowFallback:
- _objc_msgSend$setTotalAccessPointCount:
- _objc_msgSend$setTotalAccessPointErrorCount:
- _objc_msgSend$setTotalEstimatedFingerprintLocationsCount:
- _objc_msgSend$setTotalEstimatedFingerprintLocationsErrorCount:
- _objc_msgSend$setTotalFetchedFingerprintLocationsCount:
- _objc_msgSend$setTotalFetchedFingerprintLocationsErrorCount:
- _objc_msgSend$setTotalMotionActivitiesCount:
- _objc_msgSend$setTotalMotionActivitiesErrorCount:
- _objc_msgSend$setUnsettledFingerprintCountWithTimeWindowFallback:
- _objc_msgSend$setUnsettledFingerprintCountWithoutTimeWindowFallback:
- _objc_msgSend$settledFingerprintCountWithTimeWindowFallback
- _objc_msgSend$settledFingerprintCountWithoutTimeWindowFallback
- _objc_msgSend$totalAccessPointCount
- _objc_msgSend$totalAccessPointErrorCount
- _objc_msgSend$totalEstimatedFingerprintLocationsCount
- _objc_msgSend$totalEstimatedFingerprintLocationsErrorCount
- _objc_msgSend$totalFetchedFingerprintLocationsCount
- _objc_msgSend$totalFetchedFingerprintLocationsErrorCount
- _objc_msgSend$totalMotionActivitiesCount
- _objc_msgSend$totalMotionActivitiesErrorCount
- _objc_msgSend$unsettledFingerprintCountWithTimeWindowFallback
- _objc_msgSend$unsettledFingerprintCountWithoutTimeWindowFallback
CStrings:
+ "%@, %@, Failed to copy map item, %@, exiting early"
+ "%@, %@, No fingerprints found between start date, %@, and end date, %@, POI data will not be harvested"
+ "%@, %@, No valid map item provided, exiting early"
+ "%@, %@, nextAOIRefreshDate, %@, updatedLocationDate, %@, lastAOIRefreshLocation, %{sensitive}@, updatedLocation, %{sensitive}@, distanceWithUncertainty, %f, distanceToRefreshAOI, %f"
+ "%@, NO, nextAOIRefreshDate, %@, updatedLocationDate, %@"
+ "%@, YES, nextAOIRefreshDate, %@, updatedLocationDate, %@, lastAOIRefreshLocation, %{sensitive}@"
+ "%@, resetting nextAOIRefreshDate, %@, updatedLocationDate, %@"
+ "+[RTPOIHarvestUtilities harvestCuration:mapItem:referenceLocations:poiHarvester:error:]"
+ "03:22:39"
+ "NSPOSIXErrorDomain"
+ "Oct  6 2025"
+ "T@\"NSDate\",&,N,V_nextAOIRefreshDate"
+ "T@\"RTLocalBluePOIResult\",&,N,V_lastAOIRefreshResult"
+ "Td,N,V_aoiRefreshBackoffInterval"
+ "Td,N,V_distanceToRefreshAOI"
+ "_aoiRefreshBackoffInterval"
+ "_bestIconForPlaceCardHeaderDisplay:allowSmaller:"
+ "_distanceToRefreshAOI"
+ "_lastAOIRefreshResult"
+ "_motionActivitiesFrom:to:error:"
+ "_nextAOIRefreshDate"
+ "_poiHarvestForFingerprint:mapItem:referenceLocations:endDate:error:"
+ "aoiRefreshBackoffInterval"
+ "distanceToNearestAOILowerBound"
+ "distanceToRefreshAOI"
+ "harvestCuration:mapItem:referenceLocations:poiHarvester:error:"
+ "harvestPOI:mapItemSource:referenceLocations:startDate:endDate:harvestType:error:"
+ "harvested %lu visits, mapItem, %{sensitive}@, success, %@, error %@"
+ "harvested fingerprint, %@, poiHarvest, %@, triggerType, %d, harvestType, %@, error, %@"
+ "hasAOIInferenceError"
+ "hasStorageFullError"
+ "inferLocalBluePOIWithReferenceLocation:locations:accessPoints:bluePOITile:signalEnv:refreshAOI:handler:"
+ "initWithMapItem:accessPoints:locations:motionActivities:"
+ "initWithMapItem:date:"
+ "initWithPOIConfidences:aoiConfidences:distanceToNearestAOILowerBound:referenceLocation:queryTime:"
+ "lastAOIRefreshResult"
+ "nextAOIRefreshDate"
+ "service:account:inviteDroppedForSessionID:fromID:error:"
+ "setAoiRefreshBackoffInterval:"
+ "setDistanceToRefreshAOI:"
+ "setLastAOIRefreshResult:"
+ "setNextAOIRefreshDate:"
+ "shouldRefreshAOIAtLocation:"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48"
+ "v64@0:8@\"RTLocation\"16@\"NSArray\"24@\"NSArray\"32@\"RTBluePOITile\"40i48B52@?<v@?@\"RTLocalBluePOIResult\"@\"NSError\">56"
+ "v64@0:8@16@24@32@40i48B52@?56"
- "%K <= %f"
- "%K > %@ && %K < %@"
- "%{public}@, %{public}@, %lu %s fingerprints with access points found between %{private}@, fallback time window, %{public}d, error, %{public}@"
- "%{public}@, %{public}@, Canceling harvest after error fetching fingerprints, %{public}@, between start date, %{private}@, end date, %{private}@, harvest type, %{public}@"
- "%{public}@, %{public}@, Canceling harvest because visit start date, %{private}@, comes after end date, %{private}@, for harvest type, %{public}@, error, %{public}@"
- "%{public}@, %{public}@, Failed to copy map item, %{sensitive}@, exiting early"
- "%{public}@, %{public}@, Fetched %lu locations for access points, %{sensitive}@, harvest params, %{public}@, error, %{public}@"
- "%{public}@, %{public}@, Fetched %lu motion states between %{private}@, error, %{public}@"
- "%{public}@, %{public}@, Fetched access points for fingerprint, %{sensitive}@, end date, %{private}@, error, %{public}@"
- "%{public}@, %{public}@, No fingerprints with access points found between %{private}@, POI data will not be harvested"
- "%{public}@, %{public}@, No settled fingerprints with access points found, retrying with unsettled"
- "%{public}@, %{public}@, No valid map item provided, exiting early"
- "%{public}@, %{public}@, submitting metrics, %@"
- "+[RTPOIHarvestUtilities harvestCuration:mapItem:visitLocations:poiHarvester:error:]"
- "00:11:39"
- "@36@0:8@16i24@28"
- "@48@0:8@16^Q24@32^@40"
- "@48@0:8Q16@24@32^@40"
- "@52@0:8@16@24@32@40i48"
- "@56@0:8@16@24@32Q40@48"
- "B72@0:8@16Q24@32@40Q48@56^@64"
- "CoreRoutine.BluePOIHarvest"
- "HarvestType_VisitUnsettled"
- "Harvested user curation of map item, %{sensitive}@, locations, %{sensitive}@, start, %@, end, %@, error, %{public}@"
- "Harvested visit to map item, %{sensitive}@, source, %lu, location, %{sensitive}@, start, %@, end, %@, harvest type, %{public}lu, error, %{public}@"
- "Invalid parameter not satisfying: dateInterval != nil"
- "Invalid parameter not satisfying: harvestParameters"
- "Invalid parameter not satisfying: harvestType != RTHarvestTypeUnknown"
- "Invalid parameter not satisfying: harvestTypeInOut != nil"
- "Invalid parameter not satisfying: metrics != nil"
- "Invalid parameter not satisfying: settledState == RTScenarioTriggerSettledStateSettled || settledState == RTScenarioTriggerSettledStateUnsettled"
- "RTPOIHarvesterMetrics"
- "Received %lu locations for %lu access points; filled in gaps and now have %lu locations"
- "Sep 29 2025"
- "Submitted POI harvest success, %{public}s, access point count, %lu, location count, %lu, triggerType, %{public}d, harvestType, %{public}@, error, %{public}@"
- "TQ,N,V_fingerprintErrorCount"
- "TQ,N,V_harvestCreationCount"
- "TQ,N,V_harvestSubmissionCount"
- "TQ,N,V_harvestSubmissionErrorCount"
- "TQ,N,V_harvestType"
- "TQ,N,V_mapItemCopyErrorCount"
- "TQ,N,V_referenceLocationsCount"
- "TQ,N,V_settledFingerprintCountWithTimeWindowFallback"
- "TQ,N,V_settledFingerprintCountWithoutTimeWindowFallback"
- "TQ,N,V_totalAccessPointCount"
- "TQ,N,V_totalAccessPointErrorCount"
- "TQ,N,V_totalEstimatedFingerprintLocationsCount"
- "TQ,N,V_totalEstimatedFingerprintLocationsErrorCount"
- "TQ,N,V_totalFetchedFingerprintLocationsCount"
- "TQ,N,V_totalFetchedFingerprintLocationsErrorCount"
- "TQ,N,V_totalMotionActivitiesCount"
- "TQ,N,V_totalMotionActivitiesErrorCount"
- "TQ,N,V_unsettledFingerprintCountWithTimeWindowFallback"
- "TQ,N,V_unsettledFingerprintCountWithoutTimeWindowFallback"
- "Timeout waiting for estimated locations for %lu access points; giving up after %lu locations"
- "_augmentedLocationsForAccessPoints:metrics:error:"
- "_fingerprintAccessPointsForSettledState:withinInterval:metrics:error:"
- "_fingerprintAccessPointsWithinInterval:harvestType:metrics:error:"
- "_fingerprintErrorCount"
- "_harvestCreationCount"
- "_harvestPOI:mapItemSource:accessPointArrays:referenceLocations:harvestType:metrics:error:"
- "_harvestSubmissionCount"
- "_harvestSubmissionErrorCount"
- "_harvestType"
- "_mapItemCopyErrorCount"
- "_motionActivitiesWithinInterval:error:"
- "_poiHarvestForAccessPoints:mapItem:referenceLocations:harvestType:metrics:"
- "_referenceLocationsCount"
- "_settledFingerprintCountWithTimeWindowFallback"
- "_settledFingerprintCountWithoutTimeWindowFallback"
- "_totalAccessPointCount"
- "_totalAccessPointErrorCount"
- "_totalEstimatedFingerprintLocationsCount"
- "_totalEstimatedFingerprintLocationsErrorCount"
- "_totalFetchedFingerprintLocationsCount"
- "_totalFetchedFingerprintLocationsErrorCount"
- "_totalMotionActivitiesCount"
- "_totalMotionActivitiesErrorCount"
- "_unsettledFingerprintCountWithTimeWindowFallback"
- "_unsettledFingerprintCountWithoutTimeWindowFallback"
- "accessPointsCount"
- "dateInterval != nil"
- "fingerprintErrorCount"
- "harvestCreationCount"
- "harvestCuration:mapItem:visitLocations:poiHarvester:error:"
- "harvestPOI:mapItemSource:visitLocations:visitEntryDate:visitExitDate:harvestType:error:"
- "harvestSubmissionCount"
- "harvestSubmissionErrorCount"
- "harvestType"
- "harvestTypeInOut != nil"
- "harvested %lu visits, mapItem, %{sensitive}@, success, %{public}@, error, %{public}@"
- "inferLocalBluePOIWithReferenceLocation:locations:accessPoints:bluePOITile:signalEnv:handler:"
- "initWithMapItem:accessPoints:locations:motionActivities:triggerType:"
- "initWithMapItem:triggerType:date:"
- "initWithPOIConfidences:aoiConfidences:referenceLocation:queryTime:"
- "mapItemCopyErrorCount"
- "metrics != nil"
- "q24@?0@\"RTLocation\"8@\"RTLocation\"16"
- "q24@?0@\"RTWiFiAccessPoint\"8@\"RTWiFiAccessPoint\"16"
- "referenceLocationsCount"
- "setFingerprintErrorCount:"
- "setHarvestCreationCount:"
- "setHarvestSubmissionCount:"
- "setHarvestSubmissionErrorCount:"
- "setHarvestType:"
- "setMapItemCopyErrorCount:"
- "setReferenceLocationsCount:"
- "setSettledFingerprintCountWithTimeWindowFallback:"
- "setSettledFingerprintCountWithoutTimeWindowFallback:"
- "setTotalAccessPointCount:"
- "setTotalAccessPointErrorCount:"
- "setTotalEstimatedFingerprintLocationsCount:"
- "setTotalEstimatedFingerprintLocationsErrorCount:"
- "setTotalFetchedFingerprintLocationsCount:"
- "setTotalFetchedFingerprintLocationsErrorCount:"
- "setTotalMotionActivitiesCount:"
- "setTotalMotionActivitiesErrorCount:"
- "setUnsettledFingerprintCountWithTimeWindowFallback:"
- "setUnsettledFingerprintCountWithoutTimeWindowFallback:"
- "settled"
- "settledFingerprintCountWithTimeWindowFallback"
- "settledFingerprintCountWithoutTimeWindowFallback"
- "totalAccessPointCount"
- "totalAccessPointErrorCount"
- "totalErrorCount"
- "totalEstimatedFingerprintLocationsCount"
- "totalEstimatedFingerprintLocationsErrorCount"
- "totalFetchedFingerprintLocationsCount"
- "totalFetchedFingerprintLocationsErrorCount"
- "totalFingerprintCount"
- "totalLocationCount"
- "totalMotionActivitiesCount"
- "totalMotionActivitiesErrorCount"
- "totalSettledFingerprintCount"
- "totalUnsettledFingerprintCount"
- "unsettledFingerprintCountWithTimeWindowFallback"
- "unsettledFingerprintCountWithoutTimeWindowFallback"
- "v60@0:8@\"RTLocation\"16@\"NSArray\"24@\"NSArray\"32@\"RTBluePOITile\"40i48@?<v@?@\"RTLocalBluePOIResult\"@\"NSError\">52"
- "v60@0:8@16@24@32@40i48@?52"

```
