## CoreRoutine

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine`

```diff

-1071.0.1.0.0
-  __TEXT.__text: 0x64338
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x7db4
+1072.0.5.0.1
+  __TEXT.__text: 0x697a8
+  __TEXT.__auth_stubs: 0x630
+  __TEXT.__objc_methlist: 0x80a0
   __TEXT.__const: 0x2c8
-  __TEXT.__oslogstring: 0x3342
-  __TEXT.__cstring: 0x652f
-  __TEXT.__gcc_except_tab: 0x368
-  __TEXT.__unwind_info: 0x1e08
-  __TEXT.__objc_classname: 0xf9a
-  __TEXT.__objc_methname: 0xef35
-  __TEXT.__objc_methtype: 0x26db
-  __TEXT.__objc_stubs: 0x7500
-  __DATA_CONST.__got: 0x4a0
+  __TEXT.__oslogstring: 0x34c8
+  __TEXT.__cstring: 0x6716
+  __TEXT.__gcc_except_tab: 0x340
+  __TEXT.__unwind_info: 0x2030
+  __TEXT.__objc_classname: 0xffb
+  __TEXT.__objc_methname: 0xf455
+  __TEXT.__objc_methtype: 0x2786
+  __TEXT.__objc_stubs: 0x77c0
+  __DATA_CONST.__got: 0x4b8
   __DATA_CONST.__const: 0x1290
-  __DATA_CONST.__objc_classlist: 0x458
+  __DATA_CONST.__objc_classlist: 0x478
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2868
+  __DATA_CONST.__objc_selrefs: 0x2938
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x428
+  __DATA_CONST.__objc_superrefs: 0x440
   __DATA_CONST.__objc_arraydata: 0x98
-  __AUTH_CONST.__auth_got: 0x358
-  __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x5a00
-  __AUTH_CONST.__objc_const: 0xe2c0
+  __AUTH_CONST.__auth_got: 0x328
+  __AUTH_CONST.__const: 0x3c0
+  __AUTH_CONST.__cfstring: 0x5b60
+  __AUTH_CONST.__objc_const: 0xe7c0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x14a0
-  __DATA.__objc_ivar: 0x818
+  __AUTH.__objc_data: 0x1590
+  __DATA.__objc_ivar: 0x83c
   __DATA.__data: 0x308
   __DATA_DIRTY.__objc_ivar: 0x130
-  __DATA_DIRTY.__objc_data: 0x16d0
+  __DATA_DIRTY.__objc_data: 0x1720
   __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7894D15D-8C50-3DB8-9E14-34EA307D2D86
-  Functions: 2810
-  Symbols:   8775
-  CStrings:  4445
+  UUID: 7B8ADE16-8F87-3D76-94A3-75208D8B1230
+  Functions: 2874
+  Symbols:   8966
+  CStrings:  4529
 
Symbols:
+ +[RTBusinessHours supportsSecureCoding]
+ +[RTDailyHours supportsSecureCoding]
+ +[RTLocalTimeInterval supportsSecureCoding]
+ -[RTBusinessHours .cxx_destruct]
+ -[RTBusinessHours copyWithZone:]
+ -[RTBusinessHours dailyHours]
+ -[RTBusinessHours description]
+ -[RTBusinessHours encodeWithCoder:]
+ -[RTBusinessHours hash]
+ -[RTBusinessHours hoursType]
+ -[RTBusinessHours initWithCoder:]
+ -[RTBusinessHours initWithHoursType:dailyHours:]
+ -[RTBusinessHours init]
+ -[RTBusinessHours isEqual:]
+ -[RTBusinessHours isEqualToBusinessHours:]
+ -[RTDailyHours .cxx_destruct]
+ -[RTDailyHours copyWithZone:]
+ -[RTDailyHours description]
+ -[RTDailyHours encodeWithCoder:]
+ -[RTDailyHours hash]
+ -[RTDailyHours initWithCoder:]
+ -[RTDailyHours initWithWeekday:timeIntervals:]
+ -[RTDailyHours init]
+ -[RTDailyHours isEqual:]
+ -[RTDailyHours isEqualToDailyHours:]
+ -[RTDailyHours timeIntervals]
+ -[RTDailyHours weekday]
+ -[RTLocalTimeInterval copyWithZone:]
+ -[RTLocalTimeInterval description]
+ -[RTLocalTimeInterval encodeWithCoder:]
+ -[RTLocalTimeInterval endTime]
+ -[RTLocalTimeInterval hash]
+ -[RTLocalTimeInterval initWithCoder:]
+ -[RTLocalTimeInterval initWithStartTime:endTime:]
+ -[RTLocalTimeInterval init]
+ -[RTLocalTimeInterval isEqual:]
+ -[RTLocalTimeInterval isEqualToLocalTimeInterval:]
+ -[RTLocalTimeInterval startTime]
+ -[RTMapItem businessHours]
+ -[RTMapItem initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:geoMapItemIdentifier:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:businessHours:]
+ -[RTRoutineManager generatedTripSegmentRegistrant]
+ -[RTRoutineManager initWithRestorationIdentifier:targetUserSession:]
+ -[RTRoutineManager onGeneratedTripSegment:withError:]
+ -[RTRoutineManager setGeneratedTripSegmentRegistrant:]
+ -[RTRoutineManager startMonitoringForGeneratedTripSegmentsWithCallback:]
+ -[RTRoutineManager stopMonitoringForGeneratedTripSegments]
+ -[RTRoutineManagerExportedObject onGeneratedTripSegment:withError:]
+ -[RTRoutineManagerRegistrantGeneratedTripSegments .cxx_destruct]
+ -[RTRoutineManagerRegistrantGeneratedTripSegments clientCallback]
+ -[RTRoutineManagerRegistrantGeneratedTripSegments isRegistered]
+ -[RTRoutineManagerRegistrantGeneratedTripSegments onGeneratedTripSegment:andError:]
+ -[RTRoutineManagerRegistrantGeneratedTripSegments setClientCallback:]
+ -[RTRoutineManagerRegistrantGeneratedTripSegments startMonitoringWithCallback:]
+ -[RTRoutineManagerRegistrantGeneratedTripSegments stopMonitoring]
+ GCC_except_table175
+ GCC_except_table176
+ GCC_except_table183
+ GCC_except_table583
+ _OBJC_CLASS_$_RTBusinessHours
+ _OBJC_CLASS_$_RTDailyHours
+ _OBJC_CLASS_$_RTLocalTimeInterval
+ _OBJC_CLASS_$_RTRoutineManagerRegistrantGeneratedTripSegments
+ _OBJC_IVAR_$_RTBusinessHours._dailyHours
+ _OBJC_IVAR_$_RTBusinessHours._hoursType
+ _OBJC_IVAR_$_RTDailyHours._timeIntervals
+ _OBJC_IVAR_$_RTDailyHours._weekday
+ _OBJC_IVAR_$_RTLocalTimeInterval._endTime
+ _OBJC_IVAR_$_RTLocalTimeInterval._startTime
+ _OBJC_IVAR_$_RTMapItem._businessHours
+ _OBJC_IVAR_$_RTRoutineManager._generatedTripSegmentRegistrant
+ _OBJC_IVAR_$_RTRoutineManagerRegistrantGeneratedTripSegments._clientCallback
+ _OBJC_METACLASS_$_RTBusinessHours
+ _OBJC_METACLASS_$_RTDailyHours
+ _OBJC_METACLASS_$_RTLocalTimeInterval
+ _OBJC_METACLASS_$_RTRoutineManagerRegistrantGeneratedTripSegments
+ __OBJC_$_CLASS_METHODS_RTBusinessHours
+ __OBJC_$_CLASS_METHODS_RTDailyHours
+ __OBJC_$_CLASS_METHODS_RTLocalTimeInterval
+ __OBJC_$_CLASS_PROP_LIST_RTBusinessHours
+ __OBJC_$_CLASS_PROP_LIST_RTDailyHours
+ __OBJC_$_CLASS_PROP_LIST_RTLocalTimeInterval
+ __OBJC_$_INSTANCE_METHODS_RTBusinessHours
+ __OBJC_$_INSTANCE_METHODS_RTDailyHours
+ __OBJC_$_INSTANCE_METHODS_RTLocalTimeInterval
+ __OBJC_$_INSTANCE_METHODS_RTRoutineManagerRegistrantGeneratedTripSegments
+ __OBJC_$_INSTANCE_VARIABLES_RTBusinessHours
+ __OBJC_$_INSTANCE_VARIABLES_RTDailyHours
+ __OBJC_$_INSTANCE_VARIABLES_RTLocalTimeInterval
+ __OBJC_$_INSTANCE_VARIABLES_RTRoutineManagerRegistrantGeneratedTripSegments
+ __OBJC_$_PROP_LIST_RTBusinessHours
+ __OBJC_$_PROP_LIST_RTDailyHours
+ __OBJC_$_PROP_LIST_RTLocalTimeInterval
+ __OBJC_$_PROP_LIST_RTRoutineManagerRegistrantGeneratedTripSegments
+ __OBJC_CLASS_PROTOCOLS_$_RTBusinessHours
+ __OBJC_CLASS_PROTOCOLS_$_RTDailyHours
+ __OBJC_CLASS_PROTOCOLS_$_RTLocalTimeInterval
+ __OBJC_CLASS_RO_$_RTBusinessHours
+ __OBJC_CLASS_RO_$_RTDailyHours
+ __OBJC_CLASS_RO_$_RTLocalTimeInterval
+ __OBJC_CLASS_RO_$_RTRoutineManagerRegistrantGeneratedTripSegments
+ __OBJC_METACLASS_RO_$_RTBusinessHours
+ __OBJC_METACLASS_RO_$_RTDailyHours
+ __OBJC_METACLASS_RO_$_RTLocalTimeInterval
+ __OBJC_METACLASS_RO_$_RTRoutineManagerRegistrantGeneratedTripSegments
+ ___37-[RTRoutineManager _createConnection]_block_invoke.418
+ ___38-[RTRoutineManager stopLeechingVisits]_block_invoke.478
+ ___38-[RTRoutineManager stopLeechingVisits]_block_invoke_2.479
+ ___40-[RTRoutineManager stopMonitoringVisits]_block_invoke.476
+ ___40-[RTRoutineManager stopMonitoringVisits]_block_invoke_2.477
+ ___42-[RTRoutineManager addElevations:handler:]_block_invoke.571
+ ___49-[RTRoutineManager fetchRoutineStateWithHandler:]_block_invoke.450
+ ___49-[RTRoutineManager stopMonitoringPlaceInferences]_block_invoke.484
+ ___49-[RTRoutineManager stopMonitoringPlaceInferences]_block_invoke_2.485
+ ___50-[RTRoutineManager fetchAuthorizedLocationStatus:]_block_invoke.526
+ ___51-[RTRoutineManager fetchRoutineEnabledWithHandler:]_block_invoke.448
+ ___51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke.480
+ ___51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke_2.481
+ ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.528
+ ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.529
+ ___53-[RTRoutineManager fetchElevationsWithOptions:reply:]_block_invoke.572
+ ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke.500
+ ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke_2.501
+ ___57-[RTRoutineManager fetchStoredVisitsWithOptions:handler:]_block_invoke.486
+ ___58-[RTRoutineManager _enumerateElevationsWithOptions:reply:]_block_invoke.573
+ ___58-[RTRoutineManager _enumerateElevationsWithOptions:reply:]_block_invoke.576
+ ___58-[RTRoutineManager stopMonitoringForGeneratedTripSegments]_block_invoke
+ ___58-[RTRoutineManager stopMonitoringForGeneratedTripSegments]_block_invoke.445
+ ___58-[RTRoutineManager stopMonitoringForGeneratedTripSegments]_block_invoke_2
+ ___58-[RTRoutineManager stopMonitoringForGeneratedTripSegments]_block_invoke_2.446
+ ___58-[RTRoutineManager stopMonitoringForGeneratedTripSegments]_block_invoke_3
+ ___58-[RTRoutineManager stopMonitoringRemoteStatusWithHandler:]_block_invoke.456
+ ___58-[RTRoutineManager stopMonitoringRemoteStatusWithHandler:]_block_invoke_2.457
+ ___59-[RTRoutineManager enumerateObjectsWithOptions:usingBlock:]_block_invoke.468
+ ___59-[RTRoutineManager startMonitoringRemoteStatusWithHandler:]_block_invoke.453
+ ___59-[RTRoutineManager startMonitoringRemoteStatusWithHandler:]_block_invoke_2.454
+ ___62-[RTRoutineManager startMonitoringForPeopleDiscovery:handler:]_block_invoke.562
+ ___62-[RTRoutineManager stopMonitoringPredictedContextWithHandler:]_block_invoke.495
+ ___62-[RTRoutineManager stopMonitoringPredictedContextWithHandler:]_block_invoke_2.496
+ ___63-[RTRoutineManager fetchLocationsOfInterestOfType:withHandler:]_block_invoke.504
+ ___63-[RTRoutineManager submitUserCurationForDate:newLabel:handler:]_block_invoke.579
+ ___64-[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]_block_invoke.563
+ ___64-[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]_block_invoke.564
+ ___65-[RTRoutineManager addBackgroundInertialOdometrySamples:handler:]_block_invoke.578
+ ___67-[RTRoutineManagerExportedObject onGeneratedTripSegment:withError:]_block_invoke
+ ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.473
+ ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.474
+ ___68-[RTRoutineManager fetchPeopleCountEventsHistory:completionHandler:]_block_invoke.568
+ ___70-[RTRoutineManager fetchLocationOfInterestWithIdentifier:withHandler:]_block_invoke.502
+ ___70-[RTRoutineManager startMonitoringPlaceInferencesWithOptions:handler:]_block_invoke.482
+ ___70-[RTRoutineManager startMonitoringPlaceInferencesWithOptions:handler:]_block_invoke_2.483
+ ___71-[RTRoutineManager fetchContactScoresFromContactIDs:completionHandler:]_block_invoke.570
+ ___72-[RTRoutineManager fetchProximityHistoryFromEventIDs:completionHandler:]_block_invoke.567
+ ___72-[RTRoutineManager startMonitoringForGeneratedTripSegmentsWithCallback:]_block_invoke
+ ___72-[RTRoutineManager startMonitoringForGeneratedTripSegmentsWithCallback:]_block_invoke_2
+ ___72-[RTRoutineManager startMonitoringForGeneratedTripSegmentsWithCallback:]_block_invoke_3
+ ___72-[RTRoutineManager startMonitoringForGeneratedTripSegmentsWithCallback:]_block_invoke_4
+ ___72-[RTRoutineManager startMonitoringForGeneratedTripSegmentsWithCallback:]_block_invoke_5
+ ___73-[RTRoutineManager fetchLocationsOfInterestVisitedSinceDate:withHandler:]_block_invoke.508
+ ___73-[RTRoutineManager submitUserCurationForVisitDateRange:newLabel:handler:]_block_invoke.580
+ ___77-[RTRoutineManager _proxyForServicingSelector:asynchronous:withErrorHandler:]_block_invoke.420
+ ___77-[RTRoutineManager _proxyForServicingSelector:asynchronous:withErrorHandler:]_block_invoke.421
+ ___78-[RTRoutineManager fetchBackgroundInertialOdometrySamplesWithOptions:handler:]_block_invoke.577
+ ___81-[RTRoutineManager fetchProximityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.566
+ ___81-[RTRoutineManager startMonitoringPredictedContextWithOptions:completionHandler:]_block_invoke.493
+ ___81-[RTRoutineManager startMonitoringPredictedContextWithOptions:completionHandler:]_block_invoke_2.494
+ ___85-[RTRoutineManager fetchPeopleDensityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.569
+ ___88-[RTRoutineManager fetchLocationsOfInterestVisitedBetweenStartDate:endDate:withHandler:]_block_invoke.512
+ ___96-[RTRoutineManager correctLabelForVisitWithIdentifier:entryDate:originalLabel:newLabel:handler:]_block_invoke.581
+ ___Block_byref_object_copy_.574
+ ___Block_byref_object_dispose_.575
+ ___block_literal_global.444
+ ___block_literal_global.499
+ ___block_literal_global.531
+ ___block_literal_global.533
+ ___block_literal_global.535
+ ___block_literal_global.537
+ ___block_literal_global.539
+ ___block_literal_global.541
+ ___block_literal_global.543
+ ___block_literal_global.545
+ ___block_literal_global.547
+ ___block_literal_global.549
+ ___block_literal_global.551
+ ___block_literal_global.553
+ ___block_literal_global.555
+ ___block_literal_global.557
+ ___block_literal_global.559
+ ___block_literal_global.561
+ _objc_msgSend$clientCallback
+ _objc_msgSend$dailyHours
+ _objc_msgSend$endTime
+ _objc_msgSend$generatedTripSegmentRegistrant
+ _objc_msgSend$hoursType
+ _objc_msgSend$initWithHoursType:dailyHours:
+ _objc_msgSend$initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:geoMapItemIdentifier:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:businessHours:
+ _objc_msgSend$initWithRestorationIdentifier:targetUserSession:
+ _objc_msgSend$initWithStartTime:endTime:
+ _objc_msgSend$initWithWeekday:timeIntervals:
+ _objc_msgSend$isEqualToBusinessHours:
+ _objc_msgSend$isEqualToDailyHours:
+ _objc_msgSend$isEqualToLocalTimeInterval:
+ _objc_msgSend$isRegistered
+ _objc_msgSend$onGeneratedTripSegment:andError:
+ _objc_msgSend$onGeneratedTripSegment:withError:
+ _objc_msgSend$setClientCallback:
+ _objc_msgSend$startMonitoringForGeneratedTripSegmentsWithCallback:
+ _objc_msgSend$startMonitoringForGeneratedTripSegmentsWithReply:
+ _objc_msgSend$startMonitoringWithCallback:
+ _objc_msgSend$startTime
+ _objc_msgSend$stopMonitoring
+ _objc_msgSend$stopMonitoringForGeneratedTripSegmentsWithReply:
+ _objc_msgSend$timeIntervals
- -[RTRoutineManager initWithRestorationIdentifier:targertUserSession:]
- GCC_except_table160
- GCC_except_table161
- GCC_except_table168
- GCC_except_table568
- ___37-[RTRoutineManager _createConnection]_block_invoke.413
- ___38-[RTRoutineManager stopLeechingVisits]_block_invoke.469
- ___38-[RTRoutineManager stopLeechingVisits]_block_invoke_2.470
- ___40-[RTRoutineManager stopMonitoringVisits]_block_invoke.467
- ___40-[RTRoutineManager stopMonitoringVisits]_block_invoke_2.468
- ___42-[RTRoutineManager addElevations:handler:]_block_invoke.562
- ___49-[RTRoutineManager fetchRoutineStateWithHandler:]_block_invoke.441
- ___49-[RTRoutineManager stopMonitoringPlaceInferences]_block_invoke.475
- ___49-[RTRoutineManager stopMonitoringPlaceInferences]_block_invoke_2.476
- ___50-[RTRoutineManager fetchAuthorizedLocationStatus:]_block_invoke.517
- ___51-[RTRoutineManager fetchRoutineEnabledWithHandler:]_block_invoke.439
- ___51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke.471
- ___51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke_2.472
- ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.519
- ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.520
- ___53-[RTRoutineManager fetchElevationsWithOptions:reply:]_block_invoke.563
- ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke.491
- ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke_2.492
- ___57-[RTRoutineManager fetchStoredVisitsWithOptions:handler:]_block_invoke.477
- ___58-[RTRoutineManager _enumerateElevationsWithOptions:reply:]_block_invoke.564
- ___58-[RTRoutineManager _enumerateElevationsWithOptions:reply:]_block_invoke.567
- ___58-[RTRoutineManager stopMonitoringRemoteStatusWithHandler:]_block_invoke.447
- ___58-[RTRoutineManager stopMonitoringRemoteStatusWithHandler:]_block_invoke_2.448
- ___59-[RTRoutineManager enumerateObjectsWithOptions:usingBlock:]_block_invoke.459
- ___59-[RTRoutineManager startMonitoringRemoteStatusWithHandler:]_block_invoke.444
- ___59-[RTRoutineManager startMonitoringRemoteStatusWithHandler:]_block_invoke_2.445
- ___62-[RTRoutineManager startMonitoringForPeopleDiscovery:handler:]_block_invoke.553
- ___62-[RTRoutineManager stopMonitoringPredictedContextWithHandler:]_block_invoke.486
- ___62-[RTRoutineManager stopMonitoringPredictedContextWithHandler:]_block_invoke_2.487
- ___63-[RTRoutineManager fetchLocationsOfInterestOfType:withHandler:]_block_invoke.495
- ___63-[RTRoutineManager submitUserCurationForDate:newLabel:handler:]_block_invoke.570
- ___64-[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]_block_invoke.554
- ___64-[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]_block_invoke.555
- ___65-[RTRoutineManager addBackgroundInertialOdometrySamples:handler:]_block_invoke.569
- ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.464
- ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.465
- ___68-[RTRoutineManager fetchPeopleCountEventsHistory:completionHandler:]_block_invoke.559
- ___70-[RTRoutineManager fetchLocationOfInterestWithIdentifier:withHandler:]_block_invoke.493
- ___70-[RTRoutineManager startMonitoringPlaceInferencesWithOptions:handler:]_block_invoke.473
- ___70-[RTRoutineManager startMonitoringPlaceInferencesWithOptions:handler:]_block_invoke_2.474
- ___71-[RTRoutineManager fetchContactScoresFromContactIDs:completionHandler:]_block_invoke.561
- ___72-[RTRoutineManager fetchProximityHistoryFromEventIDs:completionHandler:]_block_invoke.558
- ___73-[RTRoutineManager fetchLocationsOfInterestVisitedSinceDate:withHandler:]_block_invoke.499
- ___73-[RTRoutineManager submitUserCurationForVisitDateRange:newLabel:handler:]_block_invoke.571
- ___77-[RTRoutineManager _proxyForServicingSelector:asynchronous:withErrorHandler:]_block_invoke.415
- ___77-[RTRoutineManager _proxyForServicingSelector:asynchronous:withErrorHandler:]_block_invoke.416
- ___78-[RTRoutineManager fetchBackgroundInertialOdometrySamplesWithOptions:handler:]_block_invoke.568
- ___81-[RTRoutineManager fetchProximityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.557
- ___81-[RTRoutineManager startMonitoringPredictedContextWithOptions:completionHandler:]_block_invoke.484
- ___81-[RTRoutineManager startMonitoringPredictedContextWithOptions:completionHandler:]_block_invoke_2.485
- ___85-[RTRoutineManager fetchPeopleDensityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.560
- ___88-[RTRoutineManager fetchLocationsOfInterestVisitedBetweenStartDate:endDate:withHandler:]_block_invoke.503
- ___96-[RTRoutineManager correctLabelForVisitWithIdentifier:entryDate:originalLabel:newLabel:handler:]_block_invoke.572
- ___Block_byref_object_copy_.565
- ___Block_byref_object_dispose_.566
- ___block_literal_global.490
- ___block_literal_global.522
- ___block_literal_global.524
- ___block_literal_global.526
- ___block_literal_global.528
- ___block_literal_global.530
- ___block_literal_global.532
- ___block_literal_global.534
- ___block_literal_global.536
- ___block_literal_global.538
- ___block_literal_global.540
- ___block_literal_global.542
- ___block_literal_global.544
- ___block_literal_global.546
- ___block_literal_global.548
- ___block_literal_global.550
- ___block_literal_global.552
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:geoMapItemIdentifier:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:
- _objc_msgSend$initWithRestorationIdentifier:targertUserSession:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
CStrings:
+ "%@-%@: registered, %@, generatedTripSegment, %@, error, %@"
+ "-[RTBusinessHours initWithHoursType:dailyHours:]"
+ "-[RTDailyHours initWithWeekday:timeIntervals:]"
+ "-[RTRoutineManager startMonitoringForGeneratedTripSegmentsWithCallback:]"
+ "@\"RTRoutineManagerRegistrantGeneratedTripSegments\""
+ "@156@0:8@16@24@32@40@48@56Q64Q72Q80q88@96@104@112@120@128@136B144@148"
+ "@24@0:8@?16"
+ "Client is exceeding maximum call rate! Selector culprit: %@"
+ "Encountered error while stopping monitoring for generated trip segments, error, %@"
+ "Encountered error while stopping monitoring generated trip segments, error, %@"
+ "Invalid parameter not satisfying: callback (in %s:%d)"
+ "Invalid parameter not satisfying: dailyHours (in %s:%d)"
+ "Invalid parameter not satisfying: timeIntervals (in %s:%d)"
+ "Invalid parameter value for callback. Requires non-nil values."
+ "RTBusinessHours"
+ "RTBusinessHours: hoursType=%lu, dailyHours=%@"
+ "RTDailyHours"
+ "RTDailyHours: weekday=%lu, timeIntervals=%@"
+ "RTLocalTimeInterval"
+ "RTLocalTimeInterval: startTime=%.1f, endTime=%.1f"
+ "RTRoutineManagerRegistrantGeneratedTripSegments"
+ "T@\"NSArray\",R,C,N,V_businessHours"
+ "T@\"NSArray\",R,C,N,V_dailyHours"
+ "T@\"NSArray\",R,C,N,V_timeIntervals"
+ "T@\"RTRoutineManagerRegistrantGeneratedTripSegments\",&,N,V_generatedTripSegmentRegistrant"
+ "T@?,C,N,V_clientCallback"
+ "TB,R,N,GisRegistered"
+ "TQ,R,N,V_hoursType"
+ "TQ,R,N,V_weekday"
+ "Td,R,N,V_endTime"
+ "Td,R,N,V_startTime"
+ "_businessHours"
+ "_clientCallback"
+ "_dailyHours"
+ "_endTime"
+ "_generatedTripSegmentRegistrant"
+ "_hoursType"
+ "_startTime"
+ "_timeIntervals"
+ "_weekday"
+ "businessHours"
+ "clientCallback"
+ "dailyHours"
+ "endTime"
+ "generatedTripSegmentRegistrant"
+ "hoursType"
+ "identifier, %@, geoMapItemIdentifier, %@ (%@), name, \"%@\", category, %@, categoryMUID, %@, businessHours, %@, address, %@, location, %@, source, %@, map item place type, %@, muid, %lu, result provider ID: %ld, weight, %lf, creationDate, %@, extended attributes, %@, display language, %@, disputed, %@"
+ "initWithHoursType:dailyHours:"
+ "initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:geoMapItemIdentifier:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:businessHours:"
+ "initWithRestorationIdentifier:targetUserSession:"
+ "initWithStartTime:endTime:"
+ "initWithWeekday:timeIntervals:"
+ "isEqualToBusinessHours:"
+ "isEqualToDailyHours:"
+ "isEqualToLocalTimeInterval:"
+ "isRegistered"
+ "onGeneratedTripSegment:andError:"
+ "onGeneratedTripSegment:withError:"
+ "setClientCallback:"
+ "setGeneratedTripSegmentRegistrant:"
+ "startMonitoringForGeneratedTripSegmentsWithCallback:"
+ "startMonitoringForGeneratedTripSegmentsWithReply:"
+ "startMonitoringWithCallback:"
+ "startTime"
+ "stopMonitoring"
+ "stopMonitoringForGeneratedTripSegments"
+ "stopMonitoringForGeneratedTripSegmentsWithReply:"
+ "timeIntervals"
+ "v32@0:8@\"RTTripSegment\"16@\"NSError\"24"
- "Client is exceeding maximum call rate!"
- "identifier, %@, geoMapItemIdentifier, %@ (%@), name, \"%@\", category, %@, categoryMUID, %@, address, %@, location, %@, source, %@, map item place type, %@, muid, %lu, result provider ID: %ld, weight, %lf, creationDate, %@, extended attributes, %@, display language, %@, disputed, %@"
- "initWithRestorationIdentifier:targertUserSession:"

```
