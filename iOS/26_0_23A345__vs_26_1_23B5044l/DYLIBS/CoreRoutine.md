## CoreRoutine

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine`

```diff

-1062.0.1.0.1
-  __TEXT.__text: 0x63bd4
+1067.0.2.0.0
+  __TEXT.__text: 0x640d4
   __TEXT.__auth_stubs: 0x6a0
   __TEXT.__objc_methlist: 0x7d84
   __TEXT.__const: 0x2c8
   __TEXT.__oslogstring: 0x331f
   __TEXT.__cstring: 0x644c
-  __TEXT.__gcc_except_tab: 0x36c
+  __TEXT.__gcc_except_tab: 0x368
   __TEXT.__unwind_info: 0x1e08
   __TEXT.__objc_classname: 0xf9a
   __TEXT.__objc_methname: 0xed3c

   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FA387974-67CB-3F05-9E8C-479A666683CA
+  UUID: 94C97671-A0B5-3B8D-837E-6636574234A6
   Functions: 2806
   Symbols:   8762
   CStrings:  4427
Functions:
~ -[RTRoutineManager initWithRestorationIdentifier:targertUserSession:] : 1096 -> 1120
~ -[RTRoutineManager _launchTaskWithSelector:remainingAttempts:proxyErrorHandler:taskBlock:] : 436 -> 456
~ ___90-[RTRoutineManager _launchTaskWithSelector:remainingAttempts:proxyErrorHandler:taskBlock:]_block_invoke : 548 -> 572
~ -[RTRoutineManager _proxyForServicingSelector:asynchronous:withErrorHandler:] : 836 -> 856
~ -[RTRoutineManager fetchTripSegmentsWithOptions:handler:] : 548 -> 568
~ -[RTRoutineManager fetchLocationsCountForTripSegmentWithOptions:handler:] : 548 -> 568
~ -[RTRoutineManager fetchLocationsForTripSegmentWithOptions:handler:] : 548 -> 568
~ -[RTRoutineManager deleteTripSegmentWithUUID:handler:] : 548 -> 568
~ -[RTRoutineManager fetchTripSegmentMetadataWithOptions:handler:] : 548 -> 568
~ -[RTRoutineManager fetchVehiclesWithOptions:handler:] : 548 -> 568
~ -[RTRoutineManager fetchLearnedRoutesWithOptions:handler:] : 548 -> 568
~ -[RTRoutineManager fetchTripClusterMetadataWithOptions:handler:] : 548 -> 568
~ -[RTRoutineManager purgeTripClusterTable:handler:] : 548 -> 568
~ -[RTRoutineManager purgeTripClusterWithClusterID:handler:] : 548 -> 568
~ ___59-[RTRoutineManager enumerateObjectsWithOptions:usingBlock:]_block_invoke : 1480 -> 1540
~ -[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:] : 1880 -> 1976
~ -[RTRoutineManager addElevations:handler:] : 384 -> 404
~ ___42-[RTRoutineManager addElevations:handler:]_block_invoke : 164 -> 184
~ -[RTRoutineManager fetchElevationsWithOptions:reply:] : 384 -> 404
~ ___53-[RTRoutineManager fetchElevationsWithOptions:reply:]_block_invoke : 168 -> 188
~ ___53-[RTRoutineManager fetchElevationsWithOptions:reply:]_block_invoke_3 : 140 -> 160
~ -[RTRoutineManager enumerateElevationsWithOptions:reply:] : 664 -> 684
~ ___58-[RTRoutineManager _enumerateElevationsWithOptions:reply:]_block_invoke.564 : 900 -> 920
~ -[RTRoutineManager fetchBackgroundInertialOdometrySamplesWithOptions:handler:] : 384 -> 404
~ ___78-[RTRoutineManager fetchBackgroundInertialOdometrySamplesWithOptions:handler:]_block_invoke_3 : 136 -> 156
~ -[RTRoutineManager addBackgroundInertialOdometrySamples:handler:] : 448 -> 468
~ ___65-[RTRoutineManager addBackgroundInertialOdometrySamples:handler:]_block_invoke_3 : 132 -> 152
~ -[RTRoutineManager submitUserCurationForDate:newLabel:handler:] : 556 -> 576
~ ___63-[RTRoutineManager submitUserCurationForDate:newLabel:handler:]_block_invoke_3 : 252 -> 272
~ -[RTRoutineManager submitUserCurationForVisitDateRange:newLabel:handler:] : 556 -> 576
~ ___73-[RTRoutineManager submitUserCurationForVisitDateRange:newLabel:handler:]_block_invoke_3 : 252 -> 272
~ -[RTRoutineManager correctLabelForCurrentPlace:date:newLabel:handler:] : 344 -> 364
~ -[RTRoutineManager correctLabelForVisitWithIdentifier:entryDate:originalLabel:newLabel:handler:] : 624 -> 644
~ ___96-[RTRoutineManager correctLabelForVisitWithIdentifier:entryDate:originalLabel:newLabel:handler:]_block_invoke_3 : 252 -> 272
~ -[RTRoutineManagerRegistrantPeopleDiscovery onDensityUpdate:error:] : 436 -> 456
~ ___44+[RTInferredMapItem dedupeInferredMapItems:]_block_invoke_2 : 300 -> 320
~ -[RTRoutineManagerRegistrantScenarioTrigger onScenarioTriggers:error:] : 748 -> 768
~ -[RTTripSegmentMetadataFetchOptions initWithDateInterval:fetchRoadClass:fetchFormOfWay:fetchLocationType:fetchPreferredNames:] : 436 -> 456
~ _log_analytics_submission : 500 -> 520
~ +[RTSignalGeneratorOptions getVisitsFromVisitsDescriptionData:] : 480 -> 500
~ ___63+[RTSignalGeneratorOptions getVisitsFromVisitsDescriptionData:]_block_invoke_2 : 612 -> 652
~ -[RTTripSegmentFormOfWay initWithDateInterval:distanceInterval:geoFormOfWay:] : 464 -> 484
~ -[RTPredictedContextResult predictedSequencesAfterContext:] : 1420 -> 1456
~ ___59-[RTPredictedContextResult predictedSequencesAfterContext:]_block_invoke : 288 -> 308
~ -[RTPredictedContextResult generateSequencesFromDate:toDate:] : 1224 -> 1244
~ -[RTElevation initWithElevation:dateInterval:elevationUncertainty:estimationStatus:] : 424 -> 444
~ -[RTEventAgentHelper initWithRestorationIdentifier:] : 600 -> 620
~ ___52-[RTEventAgentHelper initWithRestorationIdentifier:]_block_invoke : 192 -> 212
~ +[RTPredictedContext maskForSources:] : 624 -> 664
~ -[RTTripClusterWaypointEnumerationContext initWithEnumerationOptions:offset:] : 356 -> 376
~ -[RTTripSegmentRoadClass initWithDateInterval:distanceInterval:geoRoadClass:] : 464 -> 484
~ -[RTTripSegmentLocationType initWithDateInterval:distanceInterval:locationType:] : 404 -> 424
~ -[RTTripClusterRouteEnumerationContext initWithEnumerationOptions:offset:] : 356 -> 376
~ +[RTLocationDownsampler downsampleLocations:errorFunction:errorThreshold:outputSize:] : 412 -> 432
~ -[RTLocationsForTripSegmentFetchOptions initWithDateInterval:preferredDownsamplingLevel:boundingBoxLocation:batchSize:offset:] : 440 -> 460

```
