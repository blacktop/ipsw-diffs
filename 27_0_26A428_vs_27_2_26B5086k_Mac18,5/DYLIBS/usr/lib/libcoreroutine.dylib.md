## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-1122.0.0.0.0
-  __TEXT.__text: 0x681dd8
-  __TEXT.__objc_methlist: 0x32010
-  __TEXT.__const: 0x45e8
+1123.0.0.0.0
+  __TEXT.__text: 0x683530
+  __TEXT.__objc_methlist: 0x320c8
+  __TEXT.__const: 0x45f8
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__swift5_typeref: 0x18a
-  __TEXT.__oslogstring: 0x7e1ad
-  __TEXT.__cstring: 0x45a29
+  __TEXT.__oslogstring: 0x7e511
+  __TEXT.__cstring: 0x45b19
   __TEXT.__swift5_capture: 0x7c
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x20

   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x27de0
+  __TEXT.__gcc_except_tab: 0x27ed4
   __TEXT.__ustring: 0x3e
-  __TEXT.__unwind_info: 0x104a0
+  __TEXT.__unwind_info: 0x104c8
   __TEXT.__eh_frame: 0x3a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3510
+  __DATA_CONST.__const: 0x3518
   __DATA_CONST.__objc_classlist: 0x15f0
   __DATA_CONST.__objc_catlist: 0x3c0
   __DATA_CONST.__objc_protolist: 0x330
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19688
+  __DATA_CONST.__objc_selrefs: 0x196e8
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x11d0
   __DATA_CONST.__objc_arraydata: 0x2ca8
   __DATA_CONST.__got: 0x2f40
-  __AUTH_CONST.__const: 0xf540
-  __AUTH_CONST.__cfstring: 0x286c0
-  __AUTH_CONST.__objc_const: 0x53ae8
+  __AUTH_CONST.__const: 0xf580
+  __AUTH_CONST.__cfstring: 0x286e0
+  __AUTH_CONST.__objc_const: 0x53bd8
   __AUTH_CONST.__objc_intobj: 0x4860
   __AUTH_CONST.__objc_arrayobj: 0xeb8
   __AUTH_CONST.__objc_doubleobj: 0xbe0
   __AUTH_CONST.__objc_dictobj: 0x280
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0xde0
-  __AUTH.__objc_data: 0x25e8
-  __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x27f8
-  __DATA.__data: 0x2aa0
+  __AUTH.__objc_data: 0x1a88
+  __DATA.__objc_ivar: 0x280c
+  __DATA.__data: 0x2a38
   __DATA_DIRTY.__objc_ivar: 0x113c
-  __DATA_DIRTY.__objc_data: 0xb5e0
-  __DATA_DIRTY.__data: 0x5a8
+  __DATA_DIRTY.__objc_data: 0xc140
+  __DATA_DIRTY.__data: 0x638
   __DATA_DIRTY.__bss: 0x1b0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 20822
-  Symbols:   43210
-  CStrings:  15136
+  Functions: 20842
+  Symbols:   43242
+  CStrings:  15147
 
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
+ OBJC_IVAR_$_RTTripClusterProcessorOptions._walkingArrivalMaxHorizontalAccuracy_m
+ OBJC_IVAR_$_RTTripClusterProcessorOptions._walkingArrivalRadius_m
+ OBJC_IVAR_$_RTTripClusterProcessorOptions._walkingArrivalRequiredConsecutiveFixes
+ OBJC_IVAR_$_RTTripClusterWalkAndBikeTripStats._options
+ OBJC_IVAR_$_RTTripClusterWalkAndBikeTripStats._tripSegmentManager
+ _RTApplicationManagerBundleIdMapsIntents
+ __74-[RTTripClusterWalkAndBikeTripStats _activeWalkingDurationForTripSegment:]_block_invoke
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
