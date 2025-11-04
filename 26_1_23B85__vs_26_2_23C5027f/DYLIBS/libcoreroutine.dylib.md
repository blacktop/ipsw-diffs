## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-1069.0.4.0.0
-  __TEXT.__text: 0x613854
+1070.0.1.0.1
+  __TEXT.__text: 0x61650c
   __TEXT.__auth_stubs: 0x2190
-  __TEXT.__objc_methlist: 0x313b0
-  __TEXT.__const: 0x4968
+  __TEXT.__objc_methlist: 0x315c0
+  __TEXT.__const: 0x49b0
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__swift5_typeref: 0x1d3
-  __TEXT.__oslogstring: 0x77b5e
-  __TEXT.__cstring: 0x45bea
+  __TEXT.__oslogstring: 0x7843e
+  __TEXT.__cstring: 0x45fec
   __TEXT.__swift5_capture: 0x9c
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c

   __TEXT.__swift5_reflstr: 0x14
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x28b58
+  __TEXT.__gcc_except_tab: 0x28e9c
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0xdda0
+  __TEXT.__unwind_info: 0xdde0
   __TEXT.__eh_frame: 0x390
-  __TEXT.__objc_classname: 0x58ba
-  __TEXT.__objc_methname: 0x926bb
-  __TEXT.__objc_methtype: 0xd0c0
-  __TEXT.__objc_stubs: 0x562e0
-  __DATA_CONST.__got: 0x3148
-  __DATA_CONST.__const: 0xf650
-  __DATA_CONST.__objc_classlist: 0x1540
+  __TEXT.__objc_classname: 0x58d0
+  __TEXT.__objc_methname: 0x9336f
+  __TEXT.__objc_methtype: 0xd148
+  __TEXT.__objc_stubs: 0x568e0
+  __DATA_CONST.__got: 0x3150
+  __DATA_CONST.__const: 0xf6c0
+  __DATA_CONST.__objc_classlist: 0x1548
   __DATA_CONST.__objc_catlist: 0x3a8
   __DATA_CONST.__objc_protolist: 0x358
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x196a0
+  __DATA_CONST.__objc_selrefs: 0x19820
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x1190
   __DATA_CONST.__objc_arraydata: 0x2b88
   __AUTH_CONST.__auth_got: 0x10d8
-  __AUTH_CONST.__const: 0x32a0
-  __AUTH_CONST.__cfstring: 0x28cc0
-  __AUTH_CONST.__objc_const: 0x50c58
+  __AUTH_CONST.__const: 0x32e0
+  __AUTH_CONST.__cfstring: 0x29100
+  __AUTH_CONST.__objc_const: 0x510a8
   __AUTH_CONST.__objc_intobj: 0x48c0
   __AUTH_CONST.__objc_arrayobj: 0xf00
   __AUTH_CONST.__objc_doubleobj: 0xb10
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x20c8
-  __DATA.__objc_ivar: 0x2594
-  __DATA.__data: 0x2cd0
+  __AUTH.__objc_data: 0x2118
+  __DATA.__objc_ivar: 0x25e0
+  __DATA.__data: 0x2cd8
   __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_ivar: 0x117c
   __DATA_DIRTY.__objc_data: 0xb470

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A9955549-42A8-3DE3-BF68-1F5B9ECA8FA2
-  Functions: 20283
-  Symbols:   65459
-  CStrings:  40425
+  UUID: 96FBC755-0F3B-387C-BCAA-EF315B1BB3A7
+  Functions: 20331
+  Symbols:   65640
+  CStrings:  40613
 
Symbols:
+ +[RTPOIHarvestUtilities harvestCuration:mapItem:visitLocations:poiHarvester:error:]
+ -[CLPPoiHarvest(RTExtensions) initWithMapItem:accessPoints:locations:motionActivities:triggerType:]
+ -[CLPPoiTriggerEvent(RTExtensions) initWithMapItem:triggerType:date:]
+ -[RTPOIHarvester _augmentedLocationsForAccessPoints:metrics:error:]
+ -[RTPOIHarvester _fingerprintAccessPointsForSettledState:withinInterval:metrics:error:]
+ -[RTPOIHarvester _fingerprintAccessPointsWithinInterval:harvestType:metrics:error:]
+ -[RTPOIHarvester _harvestPOI:mapItemSource:accessPointArrays:referenceLocations:harvestType:metrics:error:]
+ -[RTPOIHarvester _motionActivitiesWithinInterval:error:]
+ -[RTPOIHarvester _poiHarvestForAccessPoints:mapItem:referenceLocations:harvestType:metrics:]
+ -[RTPOIHarvester harvestPOI:mapItemSource:visitLocations:visitEntryDate:visitExitDate:harvestType:error:]
+ -[RTPOIHarvesterMetrics fingerprintErrorCount]
+ -[RTPOIHarvesterMetrics harvestCreationCount]
+ -[RTPOIHarvesterMetrics harvestSubmissionCount]
+ -[RTPOIHarvesterMetrics harvestSubmissionErrorCount]
+ -[RTPOIHarvesterMetrics harvestType]
+ -[RTPOIHarvesterMetrics mapItemCopyErrorCount]
+ -[RTPOIHarvesterMetrics referenceLocationsCount]
+ -[RTPOIHarvesterMetrics setFingerprintErrorCount:]
+ -[RTPOIHarvesterMetrics setHarvestCreationCount:]
+ -[RTPOIHarvesterMetrics setHarvestSubmissionCount:]
+ -[RTPOIHarvesterMetrics setHarvestSubmissionErrorCount:]
+ -[RTPOIHarvesterMetrics setHarvestType:]
+ -[RTPOIHarvesterMetrics setMapItemCopyErrorCount:]
+ -[RTPOIHarvesterMetrics setReferenceLocationsCount:]
+ -[RTPOIHarvesterMetrics setSettledFingerprintCountWithTimeWindowFallback:]
+ -[RTPOIHarvesterMetrics setSettledFingerprintCountWithoutTimeWindowFallback:]
+ -[RTPOIHarvesterMetrics setTotalAccessPointCount:]
+ -[RTPOIHarvesterMetrics setTotalAccessPointErrorCount:]
+ -[RTPOIHarvesterMetrics setTotalEstimatedFingerprintLocationsCount:]
+ -[RTPOIHarvesterMetrics setTotalEstimatedFingerprintLocationsErrorCount:]
+ -[RTPOIHarvesterMetrics setTotalFetchedFingerprintLocationsCount:]
+ -[RTPOIHarvesterMetrics setTotalFetchedFingerprintLocationsErrorCount:]
+ -[RTPOIHarvesterMetrics setTotalMotionActivitiesCount:]
+ -[RTPOIHarvesterMetrics setTotalMotionActivitiesErrorCount:]
+ -[RTPOIHarvesterMetrics setUnsettledFingerprintCountWithTimeWindowFallback:]
+ -[RTPOIHarvesterMetrics setUnsettledFingerprintCountWithoutTimeWindowFallback:]
+ -[RTPOIHarvesterMetrics settledFingerprintCountWithTimeWindowFallback]
+ -[RTPOIHarvesterMetrics settledFingerprintCountWithoutTimeWindowFallback]
+ -[RTPOIHarvesterMetrics submit]
+ -[RTPOIHarvesterMetrics totalAccessPointCount]
+ -[RTPOIHarvesterMetrics totalAccessPointErrorCount]
+ -[RTPOIHarvesterMetrics totalEstimatedFingerprintLocationsCount]
+ -[RTPOIHarvesterMetrics totalEstimatedFingerprintLocationsErrorCount]
+ -[RTPOIHarvesterMetrics totalFetchedFingerprintLocationsCount]
+ -[RTPOIHarvesterMetrics totalFetchedFingerprintLocationsErrorCount]
+ -[RTPOIHarvesterMetrics totalMotionActivitiesCount]
+ -[RTPOIHarvesterMetrics totalMotionActivitiesErrorCount]
+ -[RTPOIHarvesterMetrics unsettledFingerprintCountWithTimeWindowFallback]
+ -[RTPOIHarvesterMetrics unsettledFingerprintCountWithoutTimeWindowFallback]
+ _OBJC_CLASS_$_RTPOIHarvesterMetrics
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._fingerprintErrorCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._harvestCreationCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._harvestSubmissionCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._harvestSubmissionErrorCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._harvestType
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._mapItemCopyErrorCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._referenceLocationsCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._settledFingerprintCountWithTimeWindowFallback
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._settledFingerprintCountWithoutTimeWindowFallback
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalAccessPointCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalAccessPointErrorCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalEstimatedFingerprintLocationsCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalEstimatedFingerprintLocationsErrorCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalFetchedFingerprintLocationsCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalFetchedFingerprintLocationsErrorCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalMotionActivitiesCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalMotionActivitiesErrorCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._unsettledFingerprintCountWithTimeWindowFallback
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._unsettledFingerprintCountWithoutTimeWindowFallback
+ _OBJC_METACLASS_$_RTPOIHarvesterMetrics
+ _RTAnalyticsEventBluePOIHarvest
+ __OBJC_$_INSTANCE_METHODS_RTPOIHarvesterMetrics
+ __OBJC_$_INSTANCE_VARIABLES_RTPOIHarvesterMetrics
+ __OBJC_$_PROP_LIST_RTPOIHarvesterMetrics
+ __OBJC_CLASS_RO_$_RTPOIHarvesterMetrics
+ __OBJC_METACLASS_RO_$_RTPOIHarvesterMetrics
+ ___105-[RTPOIHarvester harvestPOI:mapItemSource:visitLocations:visitEntryDate:visitExitDate:harvestType:error:]_block_invoke
+ ___121+[RTPOIHarvestUtilities fingerprintsBetweenStartDate:endDate:isTimeWindowFallback:settledState:fingerprintManager:error:]_block_invoke.6
+ ___31-[RTPOIHarvesterMetrics submit]_block_invoke
+ ___31-[RTPOIHarvesterMetrics submit]_block_invoke.184
+ ___39-[RTBluePOITileManager _validateTiles:]_block_invoke.159
+ ___42-[RTBluePOITileManager _validateMetadata:]_block_invoke.170
+ ___56-[RTPOIHarvester _motionActivitiesWithinInterval:error:]_block_invoke
+ ___57-[RTBluePOITileManager _fetchBluePOIMetadataWithHandler:]_block_invoke.178
+ ___57-[RTBluePOITileManager _fetchBluePOIMetadataWithHandler:]_block_invoke.181
+ ___57-[RTBluePOITileManager _fetchBluePOIMetadataWithHandler:]_block_invoke_2.180
+ ___61-[RTBluePOITileManager _fetchPOICategoryDenyListWithHandler:]_block_invoke.176
+ ___67-[RTPOIHarvester _augmentedLocationsForAccessPoints:metrics:error:]_block_invoke
+ ___69-[RTBluePOITileManager _performPurgeOfType:referenceDate:completion:]_block_invoke.154
+ ___90+[RTPOIHarvestUtilities locationsForAccessPoints:harvestParameters:locationManager:error:]_block_invoke
+ ___92-[RTPOIHarvester _poiHarvestForAccessPoints:mapItem:referenceLocations:harvestType:metrics:]_block_invoke
+ ___block_descriptor_32_e35_q24?0"RTLocation"8"RTLocation"16l
+ ___block_descriptor_32_e49_q24?0"RTWiFiAccessPoint"8"RTWiFiAccessPoint"16l
+ ___block_descriptor_56_e8_32s40w_e19_"NSDictionary"8?0lw40l8s32l8
+ ___block_literal_global.295
+ ___block_literal_global.407
+ ___block_literal_global.42
+ ___block_literal_global.59
+ _kRTMaxErrorsWorkoutDistanceMatrix
+ _objc_msgSend$_augmentedLocationsForAccessPoints:metrics:error:
+ _objc_msgSend$_fingerprintAccessPointsForSettledState:withinInterval:metrics:error:
+ _objc_msgSend$_fingerprintAccessPointsWithinInterval:harvestType:metrics:error:
+ _objc_msgSend$_harvestPOI:mapItemSource:accessPointArrays:referenceLocations:harvestType:metrics:error:
+ _objc_msgSend$_motionActivitiesWithinInterval:error:
+ _objc_msgSend$_poiHarvestForAccessPoints:mapItem:referenceLocations:harvestType:metrics:
+ _objc_msgSend$accessPointsCount
+ _objc_msgSend$featureToHashedApMappingDataURL
+ _objc_msgSend$fingerprintErrorCount
+ _objc_msgSend$harvestCreationCount
+ _objc_msgSend$harvestCuration:mapItem:visitLocations:poiHarvester:error:
+ _objc_msgSend$harvestPOI:mapItemSource:visitLocations:visitEntryDate:visitExitDate:harvestType:error:
+ _objc_msgSend$harvestSubmissionCount
+ _objc_msgSend$harvestSubmissionErrorCount
+ _objc_msgSend$harvestType
+ _objc_msgSend$hashedApToModelMappingDataURL
+ _objc_msgSend$initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashedApToModelMappingDataURL:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:
+ _objc_msgSend$initWithIdentifier:featureToHashedApMapping:featureToHashedApMappingDataURL:url:
+ _objc_msgSend$initWithMapItem:accessPoints:locations:motionActivities:triggerType:
+ _objc_msgSend$initWithMapItem:triggerType:date:
+ _objc_msgSend$locationsCount
+ _objc_msgSend$mapItemCopyErrorCount
+ _objc_msgSend$referenceLocationsCount
+ _objc_msgSend$setFeatureToHashedApMappingDataURL:
+ _objc_msgSend$setFingerprintErrorCount:
+ _objc_msgSend$setHarvestCreationCount:
+ _objc_msgSend$setHarvestSubmissionCount:
+ _objc_msgSend$setHarvestSubmissionErrorCount:
+ _objc_msgSend$setHarvestType:
+ _objc_msgSend$setHashedApToModelMappingDataURL:
+ _objc_msgSend$setMapItemCopyErrorCount:
+ _objc_msgSend$setReferenceLocationsCount:
+ _objc_msgSend$setSettledFingerprintCountWithTimeWindowFallback:
+ _objc_msgSend$setSettledFingerprintCountWithoutTimeWindowFallback:
+ _objc_msgSend$setTotalAccessPointCount:
+ _objc_msgSend$setTotalAccessPointErrorCount:
+ _objc_msgSend$setTotalEstimatedFingerprintLocationsCount:
+ _objc_msgSend$setTotalEstimatedFingerprintLocationsErrorCount:
+ _objc_msgSend$setTotalFetchedFingerprintLocationsCount:
+ _objc_msgSend$setTotalFetchedFingerprintLocationsErrorCount:
+ _objc_msgSend$setTotalMotionActivitiesCount:
+ _objc_msgSend$setTotalMotionActivitiesErrorCount:
+ _objc_msgSend$setUnsettledFingerprintCountWithTimeWindowFallback:
+ _objc_msgSend$setUnsettledFingerprintCountWithoutTimeWindowFallback:
+ _objc_msgSend$settledFingerprintCountWithTimeWindowFallback
+ _objc_msgSend$settledFingerprintCountWithoutTimeWindowFallback
+ _objc_msgSend$totalAccessPointCount
+ _objc_msgSend$totalAccessPointErrorCount
+ _objc_msgSend$totalEstimatedFingerprintLocationsCount
+ _objc_msgSend$totalEstimatedFingerprintLocationsErrorCount
+ _objc_msgSend$totalFetchedFingerprintLocationsCount
+ _objc_msgSend$totalFetchedFingerprintLocationsErrorCount
+ _objc_msgSend$totalMotionActivitiesCount
+ _objc_msgSend$totalMotionActivitiesErrorCount
+ _objc_msgSend$unsettledFingerprintCountWithTimeWindowFallback
+ _objc_msgSend$unsettledFingerprintCountWithoutTimeWindowFallback
- +[RTPOIHarvestUtilities harvestCuration:mapItem:referenceLocations:poiHarvester:error:]
- -[CLPPoiHarvest(RTExtensions) initWithMapItem:accessPoints:locations:motionActivities:]
- -[CLPPoiTriggerEvent(RTExtensions) initWithMapItem:date:]
- -[RTPOIHarvester _motionActivitiesFrom:to:error:]
- -[RTPOIHarvester _poiHarvestForFingerprint:mapItem:referenceLocations:endDate:error:]
- -[RTPOIHarvester harvestPOI:mapItemSource:referenceLocations:startDate:endDate:harvestType:error:]
- ___121+[RTPOIHarvestUtilities fingerprintsBetweenStartDate:endDate:isTimeWindowFallback:settledState:fingerprintManager:error:]_block_invoke.5
- ___39-[RTBluePOITileManager _validateTiles:]_block_invoke.153
- ___42-[RTBluePOITileManager _validateMetadata:]_block_invoke.164
- ___49-[RTPOIHarvester _motionActivitiesFrom:to:error:]_block_invoke
- ___57-[RTBluePOITileManager _fetchBluePOIMetadataWithHandler:]_block_invoke.172
- ___57-[RTBluePOITileManager _fetchBluePOIMetadataWithHandler:]_block_invoke.175
- ___57-[RTBluePOITileManager _fetchBluePOIMetadataWithHandler:]_block_invoke_2.174
- ___61-[RTBluePOITileManager _fetchPOICategoryDenyListWithHandler:]_block_invoke.170
- ___69-[RTBluePOITileManager _performPurgeOfType:referenceDate:completion:]_block_invoke.145
- ___98-[RTPOIHarvester harvestPOI:mapItemSource:referenceLocations:startDate:endDate:harvestType:error:]_block_invoke
- ___block_literal_global.401
- ___block_literal_global.49
- _objc_msgSend$_motionActivitiesFrom:to:error:
- _objc_msgSend$_poiHarvestForFingerprint:mapItem:referenceLocations:endDate:error:
- _objc_msgSend$harvestCuration:mapItem:referenceLocations:poiHarvester:error:
- _objc_msgSend$harvestPOI:mapItemSource:referenceLocations:startDate:endDate:harvestType:error:
- _objc_msgSend$initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:
- _objc_msgSend$initWithIdentifier:featureToHashedApMapping:url:
- _objc_msgSend$initWithMapItem:accessPoints:locations:motionActivities:
- _objc_msgSend$initWithMapItem:date:
CStrings:
+ "%@, %@, max error count reached, %lu, exiting loops early to prevent memory issues"
+ "%@, no places were inferred, created a placeInference object with reference location only, %@"
+ "%@, remove model metadata from disk, metadata, %{sensitive}@, error, %@"
+ "%@, remove tile metadata from disk, metadata, %{sensitive}@, error, %@"
+ "%K <= %f"
+ "%K > %@ && %K < %@"
+ "%{public}@, %{public}@, %lu %s fingerprints with access points found between %{private}@, fallback time window, %{public}d, error, %{public}@"
+ "%{public}@, %{public}@, Canceling harvest after error fetching fingerprints, %{public}@, between start date, %{private}@, end date, %{private}@, harvest type, %{public}@"
+ "%{public}@, %{public}@, Canceling harvest because visit start date, %{private}@, comes after end date, %{private}@, for harvest type, %{public}@, error, %{public}@"
+ "%{public}@, %{public}@, Failed to copy map item, %{sensitive}@, exiting early"
+ "%{public}@, %{public}@, Fetched %lu locations for access points, %{sensitive}@, harvest params, %{public}@, error, %{public}@"
+ "%{public}@, %{public}@, Fetched %lu motion states between %{private}@, error, %{public}@"
+ "%{public}@, %{public}@, Fetched access points for fingerprint, %{sensitive}@, end date, %{private}@, error, %{public}@"
+ "%{public}@, %{public}@, No valid map item provided, exiting early"
+ "%{public}@, %{public}@, Settled fingerprints with access points, count, %lu, between %{private}@"
+ "%{public}@, %{public}@, Unsettled fingerprints with access points, count, %lu, between %{private}@"
+ "%{public}@, %{public}@, submitting metrics, %@"
+ "+[RTPOIHarvestUtilities harvestCuration:mapItem:visitLocations:poiHarvester:error:]"
+ ".mlmodelc"
+ "20:38:24"
+ "@36@0:8@16i24@28"
+ "@48@0:8@16^Q24@32^@40"
+ "@48@0:8Q16@24@32^@40"
+ "@52@0:8@16@24@32@40i48"
+ "@56@0:8@16@24@32Q40@48"
+ "B72@0:8@16Q24@32@40Q48@56^@64"
+ "CoreRoutine.BluePOIHarvest"
+ "HarvestType_VisitUnsettled"
+ "Harvested user curation of map item, %{sensitive}@, locations, %{sensitive}@, start, %@, end, %@, error, %{public}@"
+ "Harvested visit to map item, %{sensitive}@, source, %lu, location, %{sensitive}@, start, %@, end, %@, harvest type, %{public}lu, error, %{public}@"
+ "Invalid parameter not satisfying: dateInterval != nil"
+ "Invalid parameter not satisfying: harvestParameters"
+ "Invalid parameter not satisfying: harvestType != RTHarvestTypeUnknown"
+ "Invalid parameter not satisfying: harvestTypeInOut != nil"
+ "Invalid parameter not satisfying: metrics != nil"
+ "Invalid parameter not satisfying: settledState == RTScenarioTriggerSettledStateSettled || settledState == RTScenarioTriggerSettledStateUnsettled"
+ "Oct 30 2025"
+ "RTPOIHarvesterMetrics"
+ "Received %lu locations for %lu access points; filled in gaps and now have %lu locations"
+ "Submitted POI harvest success, %{public}s, access point count, %lu, location count, %lu, triggerType, %{public}d, harvestType, %{public}@, error, %{public}@"
+ "TQ,N,V_fingerprintErrorCount"
+ "TQ,N,V_harvestCreationCount"
+ "TQ,N,V_harvestSubmissionCount"
+ "TQ,N,V_harvestSubmissionErrorCount"
+ "TQ,N,V_harvestType"
+ "TQ,N,V_mapItemCopyErrorCount"
+ "TQ,N,V_referenceLocationsCount"
+ "TQ,N,V_settledFingerprintCountWithTimeWindowFallback"
+ "TQ,N,V_settledFingerprintCountWithoutTimeWindowFallback"
+ "TQ,N,V_totalAccessPointCount"
+ "TQ,N,V_totalAccessPointErrorCount"
+ "TQ,N,V_totalEstimatedFingerprintLocationsCount"
+ "TQ,N,V_totalEstimatedFingerprintLocationsErrorCount"
+ "TQ,N,V_totalFetchedFingerprintLocationsCount"
+ "TQ,N,V_totalFetchedFingerprintLocationsErrorCount"
+ "TQ,N,V_totalMotionActivitiesCount"
+ "TQ,N,V_totalMotionActivitiesErrorCount"
+ "TQ,N,V_unsettledFingerprintCountWithTimeWindowFallback"
+ "TQ,N,V_unsettledFingerprintCountWithoutTimeWindowFallback"
+ "Timeout waiting for estimated locations for %lu access points; giving up after %lu locations"
+ "_augmentedLocationsForAccessPoints:metrics:error:"
+ "_fingerprintAccessPointsForSettledState:withinInterval:metrics:error:"
+ "_fingerprintAccessPointsWithinInterval:harvestType:metrics:error:"
+ "_fingerprintErrorCount"
+ "_harvestCreationCount"
+ "_harvestPOI:mapItemSource:accessPointArrays:referenceLocations:harvestType:metrics:error:"
+ "_harvestSubmissionCount"
+ "_harvestSubmissionErrorCount"
+ "_harvestType"
+ "_mapItemCopyErrorCount"
+ "_motionActivitiesWithinInterval:error:"
+ "_poiHarvestForAccessPoints:mapItem:referenceLocations:harvestType:metrics:"
+ "_referenceLocationsCount"
+ "_settledFingerprintCountWithTimeWindowFallback"
+ "_settledFingerprintCountWithoutTimeWindowFallback"
+ "_totalAccessPointCount"
+ "_totalAccessPointErrorCount"
+ "_totalEstimatedFingerprintLocationsCount"
+ "_totalEstimatedFingerprintLocationsErrorCount"
+ "_totalFetchedFingerprintLocationsCount"
+ "_totalFetchedFingerprintLocationsErrorCount"
+ "_totalMotionActivitiesCount"
+ "_totalMotionActivitiesErrorCount"
+ "_unsettledFingerprintCountWithTimeWindowFallback"
+ "_unsettledFingerprintCountWithoutTimeWindowFallback"
+ "accessPointsCount"
+ "bin"
+ "dateInterval != nil"
+ "featureToHashedApMappingDataURL"
+ "fingerprintErrorCount"
+ "harvestCreationCount"
+ "harvestCuration:mapItem:visitLocations:poiHarvester:error:"
+ "harvestPOI:mapItemSource:visitLocations:visitEntryDate:visitExitDate:harvestType:error:"
+ "harvestSubmissionCount"
+ "harvestSubmissionErrorCount"
+ "harvestType"
+ "harvestTypeInOut != nil"
+ "harvested %lu visits, mapItem, %{sensitive}@, success, %{public}@, error, %{public}@"
+ "hashedApToModelMappingDataURL"
+ "initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashedApToModelMappingDataURL:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:"
+ "initWithIdentifier:featureToHashedApMapping:featureToHashedApMappingDataURL:url:"
+ "initWithMapItem:accessPoints:locations:motionActivities:triggerType:"
+ "initWithMapItem:triggerType:date:"
+ "mapItemCopyErrorCount"
+ "metrics != nil"
+ "q24@?0@\"RTLocation\"8@\"RTLocation\"16"
+ "q24@?0@\"RTWiFiAccessPoint\"8@\"RTWiFiAccessPoint\"16"
+ "referenceLocationsCount"
+ "setFeatureToHashedApMappingDataURL:"
+ "setFingerprintErrorCount:"
+ "setHarvestCreationCount:"
+ "setHarvestSubmissionCount:"
+ "setHarvestSubmissionErrorCount:"
+ "setHarvestType:"
+ "setHashedApToModelMappingDataURL:"
+ "setMapItemCopyErrorCount:"
+ "setReferenceLocationsCount:"
+ "setSettledFingerprintCountWithTimeWindowFallback:"
+ "setSettledFingerprintCountWithoutTimeWindowFallback:"
+ "setTotalAccessPointCount:"
+ "setTotalAccessPointErrorCount:"
+ "setTotalEstimatedFingerprintLocationsCount:"
+ "setTotalEstimatedFingerprintLocationsErrorCount:"
+ "setTotalFetchedFingerprintLocationsCount:"
+ "setTotalFetchedFingerprintLocationsErrorCount:"
+ "setTotalMotionActivitiesCount:"
+ "setTotalMotionActivitiesErrorCount:"
+ "setUnsettledFingerprintCountWithTimeWindowFallback:"
+ "setUnsettledFingerprintCountWithoutTimeWindowFallback:"
+ "settled"
+ "settledFingerprintCountWithTimeWindowFallback"
+ "settledFingerprintCountWithoutTimeWindowFallback"
+ "totalAccessPointCount"
+ "totalAccessPointErrorCount"
+ "totalErrorCount"
+ "totalEstimatedFingerprintLocationsCount"
+ "totalEstimatedFingerprintLocationsErrorCount"
+ "totalFetchedFingerprintLocationsCount"
+ "totalFetchedFingerprintLocationsErrorCount"
+ "totalFingerprintCount"
+ "totalLocationCount"
+ "totalMotionActivitiesCount"
+ "totalMotionActivitiesErrorCount"
+ "totalSettledFingerprintCount"
+ "totalUnsettledFingerprintCount"
+ "unsettledFingerprintCountWithTimeWindowFallback"
+ "unsettledFingerprintCountWithoutTimeWindowFallback"
- "%@, %@, Failed to copy map item, %@, exiting early"
- "%@, %@, No fingerprints found between start date, %@, and end date, %@, POI data will not be harvested"
- "%@, %@, No valid map item provided, exiting early"
- "+[RTPOIHarvestUtilities harvestCuration:mapItem:referenceLocations:poiHarvester:error:]"
- "23:43:40"
- "Oct 22 2025"
- "_motionActivitiesFrom:to:error:"
- "_poiHarvestForFingerprint:mapItem:referenceLocations:endDate:error:"
- "harvestCuration:mapItem:referenceLocations:poiHarvester:error:"
- "harvestPOI:mapItemSource:referenceLocations:startDate:endDate:harvestType:error:"
- "harvested %lu visits, mapItem, %{sensitive}@, success, %@, error %@"
- "harvested fingerprint, %@, poiHarvest, %@, triggerType, %d, harvestType, %@, error, %@"
- "initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:"
- "initWithIdentifier:featureToHashedApMapping:url:"
- "initWithMapItem:accessPoints:locations:motionActivities:"
- "initWithMapItem:date:"

```
