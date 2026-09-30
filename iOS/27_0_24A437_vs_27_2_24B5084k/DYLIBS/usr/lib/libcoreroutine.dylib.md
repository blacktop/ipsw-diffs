## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-1122.0.0.0.0
-  __TEXT.__text: 0x6b0a88
-  __TEXT.__objc_methlist: 0x34e30
-  __TEXT.__const: 0x4bd8
+1123.0.0.0.0
+  __TEXT.__text: 0x6b1fb4
+  __TEXT.__objc_methlist: 0x34ee8
+  __TEXT.__const: 0x4be8
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__swift5_typeref: 0x41b
-  __TEXT.__oslogstring: 0x89da2
-  __TEXT.__cstring: 0x4aed2
+  __TEXT.__oslogstring: 0x8a106
+  __TEXT.__cstring: 0x4afc2
   __TEXT.__swift5_capture: 0xdc
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x38

   __TEXT.__swift5_reflstr: 0x14
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_types: 0x8
-  __TEXT.__gcc_except_tab: 0x2effc
+  __TEXT.__gcc_except_tab: 0x2f0f0
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x119d8
+  __TEXT.__unwind_info: 0x11a00
   __TEXT.__eh_frame: 0x6d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x10680
+  __DATA_CONST.__const: 0x10688
   __DATA_CONST.__objc_classlist: 0x1688
   __DATA_CONST.__objc_catlist: 0x3f0
   __DATA_CONST.__objc_protolist: 0x370
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b4a8
+  __DATA_CONST.__objc_selrefs: 0x1b508
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x1280
   __DATA_CONST.__objc_arraydata: 0x2dd8
   __DATA_CONST.__got: 0x3518
-  __AUTH_CONST.__const: 0x3738
-  __AUTH_CONST.__cfstring: 0x2c340
-  __AUTH_CONST.__objc_const: 0x56920
+  __AUTH_CONST.__const: 0x3778
+  __AUTH_CONST.__cfstring: 0x2c360
+  __AUTH_CONST.__objc_const: 0x56a10
   __AUTH_CONST.__objc_intobj: 0x4c08
   __AUTH_CONST.__objc_arrayobj: 0xfc0
   __AUTH_CONST.__objc_doubleobj: 0xbe0

   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x12f0
   __AUTH.__objc_data: 0x1b20
-  __DATA.__objc_ivar: 0x28ec
+  __DATA.__objc_ivar: 0x2900
   __DATA.__data: 0x2dd0
   __DATA_DIRTY.__objc_ivar: 0x1274
   __DATA_DIRTY.__objc_data: 0xc760

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 22022
-  Symbols:   45816
-  CStrings:  16419
+  Functions: 22042
+  Symbols:   45847
+  CStrings:  16430
 
Symbols:
+ -[RTTripClusterManager _donationPlaceConfidenceForLocationOfInterest:]
+ -[RTTripClusterManager _nearestLocationOfInterest:toLocation:withinDistance:]
+ -[RTTripClusterProcessorOptions setWalkingArrivalMaxHorizontalAccuracy_m:]
+ -[RTTripClusterProcessorOptions setWalkingArrivalRadius_m:]
+ -[RTTripClusterProcessorOptions setWalkingArrivalRequiredConsecutiveFixes:]
+ -[RTTripClusterProcessorOptions walkingArrivalMaxHorizontalAccuracy_m]
+ -[RTTripClusterProcessorOptions walkingArrivalRadius_m]
+ -[RTTripClusterProcessorOptions walkingArrivalRequiredConsecutiveFixes]
+ -[RTTripClusterWalkAndBikeTripStats .cxx_destruct]
+ -[RTTripClusterWalkAndBikeTripStats _activeWalkingDurationForSortedLocations:destinationLatitude:destinationLongitude:segmentStartDate:wallClockDuration:]
+ -[RTTripClusterWalkAndBikeTripStats _activeWalkingDurationForTripSegment:]
+ -[RTTripClusterWalkAndBikeTripStats initWithTripSegmentManager:options:]
+ -[RTTripClusterWalkAndBikeTripStats options]
+ -[RTTripClusterWalkAndBikeTripStats setOptions:]
+ -[RTTripClusterWalkAndBikeTripStats setTripSegmentManager:]
+ -[RTTripClusterWalkAndBikeTripStats tripSegmentManager]
+ -[RTTripClusterWalkAndBikeTripStats updateWalkAndBikeStats:isTripSegmentBeforeDriving:isTerminalTripSegment:]
+ _OBJC_IVAR_$_RTTripClusterProcessorOptions._walkingArrivalMaxHorizontalAccuracy_m
+ _OBJC_IVAR_$_RTTripClusterProcessorOptions._walkingArrivalRadius_m
+ _OBJC_IVAR_$_RTTripClusterProcessorOptions._walkingArrivalRequiredConsecutiveFixes
+ _OBJC_IVAR_$_RTTripClusterWalkAndBikeTripStats._options
+ _OBJC_IVAR_$_RTTripClusterWalkAndBikeTripStats._tripSegmentManager
+ _RTApplicationManagerBundleIdMapsIntents
+ ___74-[RTTripClusterWalkAndBikeTripStats _activeWalkingDurationForTripSegment:]_block_invoke
+ _objc_msgSend$_activeWalkingDurationForSortedLocations:destinationLatitude:destinationLongitude:segmentStartDate:wallClockDuration:
+ _objc_msgSend$_activeWalkingDurationForTripSegment:
+ _objc_msgSend$_donationPlaceConfidenceForLocationOfInterest:
+ _objc_msgSend$_nearestLocationOfInterest:toLocation:withinDistance:
+ _objc_msgSend$initWithTripSegment:preferredDownsamplingLevel:
+ _objc_msgSend$initWithTripSegmentManager:options:
+ _objc_msgSend$updateWalkAndBikeStats:isTripSegmentBeforeDriving:isTerminalTripSegment:
+ _objc_msgSend$walkingArrivalMaxHorizontalAccuracy_m
+ _objc_msgSend$walkingArrivalRadius_m
+ _objc_msgSend$walkingArrivalRequiredConsecutiveFixes
- -[RTTripClusterWalkAndBikeTripStats init]
- -[RTTripClusterWalkAndBikeTripStats updateWalkAndBikeStats:isTripSegmentBeforeDriving:]
- _objc_msgSend$updateWalkAndBikeStats:isTripSegmentBeforeDriving:
CStrings:
+ "%@,Error computing distance to destination,%@"
+ "%@,_activeWalkingDurationForSortedLocations,arrival not confirmed,falling back to wall-clock duration,%.1f"
+ "%@,_activeWalkingDurationForSortedLocations,implausible active duration,%.1f,falling back to wall-clock duration,%.1f"
+ "%@,_activeWalkingDurationForSortedLocations,leg never left arrival radius,maxDistance,%.1f,falling back to wall-clock duration,%.1f"
+ "%@,_activeWalkingDurationForTripSegment,tripID,%@,no location data,fetchError,%@,semaError,%@,falling back to wall-clock duration,%.1f"
+ "%@,_activeWalkingDurationForTripSegment,tripID,%@,tripDistance,%.1f,wallClockDuration,%.1f,activeWalkingDuration,%.1f"
+ "%@:%@, found location of interest for location %@ with name '%@', place confidence, %.3f, derived from %lu visits"
+ "%@:%@, location of interest, %@, has no visits, donating place confidence, %.3f"
+ "%@:%@, location of interest, %@, has out of range place confidence, %.3f, clamping"
+ "-[RTTripClusterWalkAndBikeTripStats _activeWalkingDurationForTripSegment:]"
+ "-[RTTripClusterWalkAndBikeTripStats updateWalkAndBikeStats:isTripSegmentBeforeDriving:isTerminalTripSegment:]"
+ "<%@: %p, downsampleFactor,%ld,windowSize,%ld,maxLocationPerTrip,%ld,maxProcessedTripSegments,%ld,useMaxProcessedTripSegments,%@,purgeClustersDataBase,%@,distBetweenTrips_km,%.2f,distanceThreshold_m,%.2f,unreachableDistance_m,%.2f,clusterLifeTimeThreshold_d,%ld,lengthDeviationThreshold_m,%.2f,locationThresholdRadius_m,%.2f,distAccuracyThreshold_m,%.2f,writeTripSegmentsToFile,%@,enableClusterProcessing,%@,saveToHTML,%@,clusterProcessorMode,%ld,learnedRoutesCurrentLocationSPIEnabled,%@,maxCleanUpOperationsCountPerRun,%ld,maxRouteRehydrationsCountPerRun,%ld,maxDeletionAttemptsForClusterData,%ld,rehydrateRouteLocationsFromWaypoints,%@,cleanUpClusterWithDuplicateWaypoints,%@,cleanUpOrphanedLocalStoreEntries,%@,walkingArrivalRadius_m,%.2f,walkingArrivalMaxHorizontalAccuracy_m,%.2f,walkingArrivalRequiredConsecutiveFixes,%ld>"
+ "com.apple.Maps.MapsIntents"
+ "\x92"
- "%@:%@, found location of interest for location %@ with name '%@'"
- "-[RTTripClusterWalkAndBikeTripStats updateWalkAndBikeStats:isTripSegmentBeforeDriving:]"
- "<%@: %p, downsampleFactor,%ld,windowSize,%ld,maxLocationPerTrip,%ld,maxProcessedTripSegments,%ld,useMaxProcessedTripSegments,%@,purgeClustersDataBase,%@,distBetweenTrips_km,%.2f,distanceThreshold_m,%.2f,unreachableDistance_m,%.2f,clusterLifeTimeThreshold_d,%ld,lengthDeviationThreshold_m,%.2f,locationThresholdRadius_m,%.2f,distAccuracyThreshold_m,%.2f,writeTripSegmentsToFile,%@,enableClusterProcessing,%@,saveToHTML,%@,clusterProcessorMode,%ld,learnedRoutesCurrentLocationSPIEnabled,%@,maxCleanUpOperationsCountPerRun,%ld,maxRouteRehydrationsCountPerRun,%ld,maxDeletionAttemptsForClusterData,%ld,rehydrateRouteLocationsFromWaypoints,%@,cleanUpClusterWithDuplicateWaypoints,%@,cleanUpOrphanedLocalStoreEntries,%@>"
```
