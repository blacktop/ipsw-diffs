## CoreRoutine

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine`

```diff

-1057.0.0.0.0
-  __TEXT.__text: 0x62c24
-  __TEXT.__auth_stubs: 0x670
+1061.0.0.0.0
+  __TEXT.__text: 0x63bd4
+  __TEXT.__auth_stubs: 0x6a0
   __TEXT.__objc_methlist: 0x7d84
-  __TEXT.__const: 0x2b8
-  __TEXT.__oslogstring: 0x31cf
+  __TEXT.__const: 0x2c8
+  __TEXT.__oslogstring: 0x331f
   __TEXT.__cstring: 0x644c
   __TEXT.__gcc_except_tab: 0x36c
-  __TEXT.__unwind_info: 0x1e28
+  __TEXT.__unwind_info: 0x1e08
   __TEXT.__objc_classname: 0xf9a
   __TEXT.__objc_methname: 0xed3c
   __TEXT.__objc_methtype: 0x26d3
   __TEXT.__objc_stubs: 0x74c0
   __DATA_CONST.__got: 0x4a0
-  __DATA_CONST.__const: 0x11a0
+  __DATA_CONST.__const: 0x1290
   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x428
   __DATA_CONST.__objc_arraydata: 0x98
-  __AUTH_CONST.__auth_got: 0x348
+  __AUTH_CONST.__auth_got: 0x360
   __AUTH_CONST.__const: 0x3a0
   __AUTH_CONST.__cfstring: 0x5980
   __AUTH_CONST.__objc_const: 0xe210

   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3BBFAC0A-4DDE-3F65-8B6E-2ABBF2CBCD03
+  UUID: AAF90731-372F-3391-898C-05907F07B17E
   Functions: 2806
-  Symbols:   8753
-  CStrings:  4418
+  Symbols:   8762
+  CStrings:  4427
 
Symbols:
+ ___42-[RTRoutineManager addElevations:handler:]_block_invoke.562
+ ___50-[RTRoutineManager fetchAuthorizedLocationStatus:]_block_invoke.517
+ ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.519
+ ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.520
+ ___53-[RTRoutineManager fetchElevationsWithOptions:reply:]_block_invoke.563
+ ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke.491
+ ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke_2.492
+ ___57-[RTRoutineManager fetchStoredVisitsWithOptions:handler:]_block_invoke.477
+ ___58-[RTRoutineManager _enumerateElevationsWithOptions:reply:]_block_invoke.564
+ ___58-[RTRoutineManager _enumerateElevationsWithOptions:reply:]_block_invoke.567
+ ___62-[RTRoutineManager startMonitoringForPeopleDiscovery:handler:]_block_invoke.553
+ ___62-[RTRoutineManager stopMonitoringPredictedContextWithHandler:]_block_invoke.486
+ ___62-[RTRoutineManager stopMonitoringPredictedContextWithHandler:]_block_invoke_2.487
+ ___63-[RTRoutineManager fetchLocationsOfInterestOfType:withHandler:]_block_invoke.495
+ ___63-[RTRoutineManager submitUserCurationForDate:newLabel:handler:]_block_invoke.570
+ ___64-[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]_block_invoke.554
+ ___64-[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]_block_invoke.555
+ ___65-[RTRoutineManager addBackgroundInertialOdometrySamples:handler:]_block_invoke.569
+ ___68-[RTRoutineManager fetchPeopleCountEventsHistory:completionHandler:]_block_invoke.559
+ ___70-[RTRoutineManager fetchLocationOfInterestWithIdentifier:withHandler:]_block_invoke.493
+ ___71-[RTRoutineManager fetchContactScoresFromContactIDs:completionHandler:]_block_invoke.561
+ ___72-[RTRoutineManager fetchProximityHistoryFromEventIDs:completionHandler:]_block_invoke.558
+ ___73-[RTRoutineManager fetchLocationsOfInterestVisitedSinceDate:withHandler:]_block_invoke.499
+ ___73-[RTRoutineManager submitUserCurationForVisitDateRange:newLabel:handler:]_block_invoke.571
+ ___78-[RTRoutineManager fetchBackgroundInertialOdometrySamplesWithOptions:handler:]_block_invoke.568
+ ___81-[RTRoutineManager fetchProximityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.557
+ ___81-[RTRoutineManager startMonitoringPredictedContextWithOptions:completionHandler:]_block_invoke.484
+ ___81-[RTRoutineManager startMonitoringPredictedContextWithOptions:completionHandler:]_block_invoke_2.485
+ ___85-[RTRoutineManager fetchPeopleDensityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.560
+ ___88-[RTRoutineManager fetchLocationsOfInterestVisitedBetweenStartDate:endDate:withHandler:]_block_invoke.503
+ ___96-[RTRoutineManager correctLabelForVisitWithIdentifier:entryDate:originalLabel:newLabel:handler:]_block_invoke.572
+ ___Block_byref_object_copy_.565
+ ___Block_byref_object_dispose_.566
+ ___block_descriptor_49_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e42_v24?0"RTLocationOfInterest"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e48_v24?0"RTAuthorizedLocationStatus"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40bs_e8_v16?08ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e28_v16?0"<RTDaemonProtocol>"8ls32l8s40l8s48l8
+ ___block_literal_global.490
+ ___block_literal_global.548
+ ___block_literal_global.550
+ ___block_literal_global.552
+ __os_signpost_emit_with_name_impl
+ _os_signpost_enabled
+ _os_signpost_id_generate
- ___42-[RTRoutineManager addElevations:handler:]_block_invoke.556
- ___50-[RTRoutineManager fetchAuthorizedLocationStatus:]_block_invoke_4
- ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.513
- ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.514
- ___53-[RTRoutineManager fetchElevationsWithOptions:reply:]_block_invoke.557
- ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke.490
- ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke_2.491
- ___57-[RTRoutineManager fetchStoredVisitsWithOptions:handler:]_block_invoke_4
- ___58-[RTRoutineManager _enumerateElevationsWithOptions:reply:]_block_invoke.558
- ___58-[RTRoutineManager _enumerateElevationsWithOptions:reply:]_block_invoke.561
- ___62-[RTRoutineManager startMonitoringForPeopleDiscovery:handler:]_block_invoke.547
- ___62-[RTRoutineManager stopMonitoringPredictedContextWithHandler:]_block_invoke.485
- ___62-[RTRoutineManager stopMonitoringPredictedContextWithHandler:]_block_invoke_2.486
- ___63-[RTRoutineManager fetchLocationsOfInterestOfType:withHandler:]_block_invoke_4
- ___63-[RTRoutineManager submitUserCurationForDate:newLabel:handler:]_block_invoke.564
- ___64-[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]_block_invoke.548
- ___64-[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]_block_invoke.549
- ___65-[RTRoutineManager addBackgroundInertialOdometrySamples:handler:]_block_invoke.563
- ___68-[RTRoutineManager fetchPeopleCountEventsHistory:completionHandler:]_block_invoke.553
- ___70-[RTRoutineManager fetchLocationOfInterestWithIdentifier:withHandler:]_block_invoke_4
- ___71-[RTRoutineManager fetchContactScoresFromContactIDs:completionHandler:]_block_invoke.555
- ___72-[RTRoutineManager fetchProximityHistoryFromEventIDs:completionHandler:]_block_invoke.552
- ___73-[RTRoutineManager fetchLocationsOfInterestVisitedSinceDate:withHandler:]_block_invoke_4
- ___73-[RTRoutineManager submitUserCurationForVisitDateRange:newLabel:handler:]_block_invoke.565
- ___78-[RTRoutineManager fetchBackgroundInertialOdometrySamplesWithOptions:handler:]_block_invoke.562
- ___81-[RTRoutineManager fetchProximityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.551
- ___81-[RTRoutineManager startMonitoringPredictedContextWithOptions:completionHandler:]_block_invoke.483
- ___81-[RTRoutineManager startMonitoringPredictedContextWithOptions:completionHandler:]_block_invoke_2.484
- ___85-[RTRoutineManager fetchPeopleDensityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.554
- ___88-[RTRoutineManager fetchLocationsOfInterestVisitedBetweenStartDate:endDate:withHandler:]_block_invoke_4
- ___96-[RTRoutineManager correctLabelForVisitWithIdentifier:entryDate:originalLabel:newLabel:handler:]_block_invoke.566
- ___Block_byref_object_copy_.559
- ___Block_byref_object_dispose_.560
- ___block_descriptor_48_e8_32s40bs_e48_v24?0"RTAuthorizedLocationStatus"8"NSError"16ls32l8s40l8
- ___block_literal_global.489
- ___block_literal_global.516
- ___block_literal_global.518
- ___block_literal_global.520
Functions:
~ -[RTRoutineManager fetchRoutineStateWithHandler:] : 424 -> 572
~ ___49-[RTRoutineManager fetchRoutineStateWithHandler:]_block_invoke : 220 -> 344
~ ___49-[RTRoutineManager fetchRoutineStateWithHandler:]_block_invoke.441 : 144 -> 152
~ ___49-[RTRoutineManager fetchRoutineStateWithHandler:]_block_invoke_2 : 176 -> 180
~ ___49-[RTRoutineManager fetchRoutineStateWithHandler:]_block_invoke_3 : 40 -> 188
~ -[RTRoutineManager fetchStoredVisitsWithOptions:handler:] : 292 -> 448
~ ___57-[RTRoutineManager fetchStoredVisitsWithOptions:handler:]_block_invoke : 32 -> 256
~ ___57-[RTRoutineManager fetchStoredVisitsWithOptions:handler:]_block_invoke_2 -> ___57-[RTRoutineManager fetchStoredVisitsWithOptions:handler:]_block_invoke.477 : 152 -> 156
~ ___57-[RTRoutineManager fetchStoredVisitsWithOptions:handler:]_block_invoke_3 -> ___57-[RTRoutineManager fetchStoredVisitsWithOptions:handler:]_block_invoke_2 : 232 -> 236
~ ___57-[RTRoutineManager fetchStoredVisitsWithOptions:handler:]_block_invoke_4 -> ___57-[RTRoutineManager fetchStoredVisitsWithOptions:handler:]_block_invoke_3 : 24 -> 236
~ -[RTRoutineManager fetchLocationOfInterestWithIdentifier:withHandler:] : 468 -> 612
~ ___70-[RTRoutineManager fetchLocationOfInterestWithIdentifier:withHandler:]_block_invoke : 24 -> 252
~ ___70-[RTRoutineManager fetchLocationOfInterestWithIdentifier:withHandler:]_block_invoke_2 -> ___70-[RTRoutineManager fetchLocationOfInterestWithIdentifier:withHandler:]_block_invoke.493 : 152 -> 156
~ ___70-[RTRoutineManager fetchLocationOfInterestWithIdentifier:withHandler:]_block_invoke_3 -> ___70-[RTRoutineManager fetchLocationOfInterestWithIdentifier:withHandler:]_block_invoke_2 : 232 -> 236
~ ___70-[RTRoutineManager fetchLocationOfInterestWithIdentifier:withHandler:]_block_invoke_4 -> ___70-[RTRoutineManager fetchLocationOfInterestWithIdentifier:withHandler:]_block_invoke_3 : 24 -> 236
~ -[RTRoutineManager fetchLocationsOfInterestOfType:withHandler:] : 440 -> 584
~ ___63-[RTRoutineManager fetchLocationsOfInterestOfType:withHandler:]_block_invoke : 24 -> 252
~ ___63-[RTRoutineManager fetchLocationsOfInterestOfType:withHandler:]_block_invoke_2 -> ___63-[RTRoutineManager fetchLocationsOfInterestOfType:withHandler:]_block_invoke.495 : 152 -> 156
~ ___63-[RTRoutineManager fetchLocationsOfInterestOfType:withHandler:]_block_invoke_3 -> ___63-[RTRoutineManager fetchLocationsOfInterestOfType:withHandler:]_block_invoke_2 : 232 -> 236
~ ___63-[RTRoutineManager fetchLocationsOfInterestOfType:withHandler:]_block_invoke_4 -> ___63-[RTRoutineManager fetchLocationsOfInterestOfType:withHandler:]_block_invoke_3 : 24 -> 236
~ -[RTRoutineManager fetchLocationsOfInterestVisitedSinceDate:withHandler:] : 524 -> 672
~ ___73-[RTRoutineManager fetchLocationsOfInterestVisitedSinceDate:withHandler:]_block_invoke : 24 -> 252
~ ___73-[RTRoutineManager fetchLocationsOfInterestVisitedSinceDate:withHandler:]_block_invoke_2 -> ___73-[RTRoutineManager fetchLocationsOfInterestVisitedSinceDate:withHandler:]_block_invoke.499 : 204 -> 212
~ ___73-[RTRoutineManager fetchLocationsOfInterestVisitedSinceDate:withHandler:]_block_invoke_3 -> ___73-[RTRoutineManager fetchLocationsOfInterestVisitedSinceDate:withHandler:]_block_invoke_2 : 232 -> 236
~ ___73-[RTRoutineManager fetchLocationsOfInterestVisitedSinceDate:withHandler:]_block_invoke_4 -> ___73-[RTRoutineManager fetchLocationsOfInterestVisitedSinceDate:withHandler:]_block_invoke_3 : 24 -> 236
~ -[RTRoutineManager fetchLocationsOfInterestVisitedBetweenStartDate:endDate:withHandler:] : 604 -> 760
~ ___88-[RTRoutineManager fetchLocationsOfInterestVisitedBetweenStartDate:endDate:withHandler:]_block_invoke : 24 -> 252
~ ___88-[RTRoutineManager fetchLocationsOfInterestVisitedBetweenStartDate:endDate:withHandler:]_block_invoke_2 -> ___88-[RTRoutineManager fetchLocationsOfInterestVisitedBetweenStartDate:endDate:withHandler:]_block_invoke.503 : 164 -> 172
~ ___88-[RTRoutineManager fetchLocationsOfInterestVisitedBetweenStartDate:endDate:withHandler:]_block_invoke_3 -> ___88-[RTRoutineManager fetchLocationsOfInterestVisitedBetweenStartDate:endDate:withHandler:]_block_invoke_2 : 232 -> 236
~ ___88-[RTRoutineManager fetchLocationsOfInterestVisitedBetweenStartDate:endDate:withHandler:]_block_invoke_4 -> ___88-[RTRoutineManager fetchLocationsOfInterestVisitedBetweenStartDate:endDate:withHandler:]_block_invoke_3 : 24 -> 236
~ -[RTRoutineManager fetchAuthorizedLocationStatus:] : 424 -> 572
~ ___50-[RTRoutineManager fetchAuthorizedLocationStatus:]_block_invoke : 32 -> 256
~ ___50-[RTRoutineManager fetchAuthorizedLocationStatus:]_block_invoke_2 -> ___50-[RTRoutineManager fetchAuthorizedLocationStatus:]_block_invoke.517 : 144 -> 152
~ ___50-[RTRoutineManager fetchAuthorizedLocationStatus:]_block_invoke_3 -> ___50-[RTRoutineManager fetchAuthorizedLocationStatus:]_block_invoke_2 : 232 -> 236
~ ___50-[RTRoutineManager fetchAuthorizedLocationStatus:]_block_invoke_4 -> ___50-[RTRoutineManager fetchAuthorizedLocationStatus:]_block_invoke_3 : 32 -> 240
CStrings:
+ " enableTelemetry=YES "
+ " enableTelemetry=YES {error:%{public,signpost.telemetry:number1}ld}"
+ "fetchAuthorizedLocationStatus"
+ "fetchLocationOfInterestWithIdentifier"
+ "fetchLocationsOfInterestOfType"
+ "fetchLocationsOfInterestVisitedBetweenStartDate"
+ "fetchLocationsOfInterestVisitedSinceDate"
+ "fetchRoutineStateWithHandler"
+ "fetchStoredVisitsWithOptions"

```
