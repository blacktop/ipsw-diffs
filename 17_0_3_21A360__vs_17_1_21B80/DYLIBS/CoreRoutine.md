## CoreRoutine

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine`

```diff

-891.0.1.0.0
-  __TEXT.__text: 0x3803c
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__objc_methlist: 0x42bc
+893.0.5.0.2
+  __TEXT.__text: 0x39494
+  __TEXT.__auth_stubs: 0x670
+  __TEXT.__objc_methlist: 0x42fc
   __TEXT.__const: 0x188
-  __TEXT.__oslogstring: 0x2060
-  __TEXT.__cstring: 0x36b9
-  __TEXT.__gcc_except_tab: 0x184
-  __TEXT.__unwind_info: 0x1018
-  __TEXT.__objc_classname: 0x7fa
-  __TEXT.__objc_methname: 0x8966
-  __TEXT.__objc_methtype: 0x1a00
-  __TEXT.__objc_stubs: 0x4aa0
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0xa88
-  __DATA_CONST.__objc_classlist: 0x270
+  __TEXT.__oslogstring: 0x2187
+  __TEXT.__cstring: 0x3899
+  __TEXT.__gcc_except_tab: 0x280
+  __TEXT.__unwind_info: 0x1044
+  __TEXT.__objc_classname: 0x809
+  __TEXT.__objc_methname: 0x8ae8
+  __TEXT.__objc_methtype: 0x1a11
+  __TEXT.__objc_stubs: 0x4c80
+  __DATA_CONST.__got: 0x50
+  __DATA_CONST.__const: 0xb20
+  __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6008
-  __DATA_CONST.__objc_selrefs: 0x1a18
-  __AUTH_CONST.__cfstring: 0x3180
-  __AUTH_CONST.__objc_const: 0x28e8
-  __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__objc_const: 0x6050
+  __DATA_CONST.__objc_selrefs: 0x1a98
+  __DATA_CONST.__objc_arraydata: 0x90
+  __AUTH_CONST.__cfstring: 0x33e0
+  __AUTH_CONST.__objc_const: 0x2930
+  __AUTH_CONST.__const: 0x380
+  __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x310
-  __AUTH.__objc_data: 0x550
+  __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__auth_got: 0x348
+  __AUTH.__objc_data: 0x5a0
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x290
-  __DATA.__objc_superrefs: 0x240
+  __DATA.__objc_classrefs: 0x2a8
+  __DATA.__objc_superrefs: 0x248
   __DATA.__objc_ivar: 0x478
-  __DATA.__data: 0x2a0
+  __DATA.__data: 0x2c0
   __DATA_DIRTY.__objc_ivar: 0x98
   __DATA_DIRTY.__objc_data: 0x1310
   __DATA_DIRTY.__data: 0x30

   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1587
-  Symbols:   5061
-  CStrings:  2309
+  Functions: 1599
+  Symbols:   5130
+  CStrings:  2355
 
Symbols:
+ +[RTMotionActivity motionActivityConfidenceFromString:]
+ +[RTMotionActivity motionActivityTypeFromString:]
+ -[RTHangsMetrics init]
+ -[RTHangsMetrics submitToCoreAnalytics:type:duration:]
+ -[RTSignalGeneratorOptions initWithVisitsDescriptionData:]
+ GCC_except_table0
+ GCC_except_table9
+ _AnalyticsSendEvent
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_RTHangsMetrics
+ _OBJC_METACLASS_$_RTHangsMetrics
+ _RTAnalyticsEventHangsMetrics
+ _RTLogFacilityMetric
+ __OBJC_$_INSTANCE_METHODS_RTHangsMetrics
+ __OBJC_CLASS_RO_$_RTHangsMetrics
+ __OBJC_METACLASS_RO_$_RTHangsMetrics
+ ___38-[RTRoutineManager stopLeechingVisits]_block_invoke.387
+ ___40-[RTRoutineManager stopMonitoringVisits]_block_invoke.386
+ ___42-[RTRoutineManager addElevations:handler:]_block_invoke.450
+ ___51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke.388
+ ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.416
+ ___53-[RTRoutineManager fetchElevationsWithOptions:reply:]_block_invoke.451
+ ___56+[RTSignalGeneratorOptions visitsDescriptionDataAtPath:]_block_invoke.74
+ ___56+[RTSignalGeneratorOptions visitsDescriptionDataAtPath:]_block_invoke.78
+ ___56+[RTSignalGeneratorOptions visitsDescriptionDataAtPath:]_block_invoke_2.79
+ ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke.392
+ ___63+[RTSignalGeneratorOptions getVisitsFromVisitsDescriptionData:]_block_invoke.93
+ ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.383
+ ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.384
+ ___68-[RTRoutineManager fetchPeopleCountEventsHistory:completionHandler:]_block_invoke.447
+ ___71-[RTRoutineManager fetchContactScoresFromContactIDs:completionHandler:]_block_invoke.449
+ ___72-[RTRoutineManager fetchProximityHistoryFromEventIDs:completionHandler:]_block_invoke.446
+ ___81-[RTRoutineManager fetchProximityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.445
+ ___85-[RTRoutineManager fetchPeopleDensityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.448
+ ____RTSemaphoreWait_block_invoke
+ ___block_descriptor_32_e31_q24?0"NSString"8"NSString"16l
+ ___block_descriptor_32_e35_B24?0"NSString"8"NSDictionary"16l
+ ___block_descriptor_56_e8_32r40r48r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40s48s_e15_v32?08Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56r_e15_v32?08Q16^B24ls32l8s40l8r56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56r_e29_v32?0"NSDictionary"8Q16^B24ls32l8s40l8r56l8s48l8
+ ___block_literal_global.394
+ ___block_literal_global.418
+ ___block_literal_global.420
+ ___block_literal_global.422
+ ___block_literal_global.424
+ ___block_literal_global.426
+ ___block_literal_global.428
+ ___block_literal_global.430
+ ___block_literal_global.432
+ ___block_literal_global.434
+ ___block_literal_global.436
+ ___block_literal_global.438
+ ___block_literal_global.440
+ ___block_literal_global.442
+ ___block_literal_global.444
+ ___block_literal_global.630
+ ___log_analytics_submission_block_invoke
+ ___stderrp
+ __unnamed_array_storage
+ __unnamed_array_storage.51
+ __unnamed_array_storage.53
+ __unnamed_array_storage.54
+ _dispatch_queue_get_label
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_time
+ _fputs
+ _kRTSignalGeneratorOptionsKeyMotionActivities
+ _log_analytics_submission
+ _objc_msgSend$_queue
+ _objc_msgSend$allKeys
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$componentsSeparatedByCharactersInSet:
+ _objc_msgSend$containsString:
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$initWithCString:encoding:
+ _objc_msgSend$motionActivityConfidenceFromString:
+ _objc_msgSend$motionActivityTypeFromString:
+ _objc_msgSend$now
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_msgSend$submitToCoreAnalytics:type:duration:
- GCC_except_table5
- ___38-[RTRoutineManager stopLeechingVisits]_block_invoke.384
- ___40-[RTRoutineManager stopMonitoringVisits]_block_invoke.383
- ___42-[RTRoutineManager addElevations:handler:]_block_invoke.447
- ___51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke.385
- ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.413
- ___53-[RTRoutineManager fetchElevationsWithOptions:reply:]_block_invoke.448
- ___56+[RTSignalGeneratorOptions visitsDescriptionDataAtPath:]_block_invoke.56
- ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke.389
- ___63+[RTSignalGeneratorOptions getVisitsFromVisitsDescriptionData:]_block_invoke.68
- ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.380
- ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.381
- ___68-[RTRoutineManager fetchPeopleCountEventsHistory:completionHandler:]_block_invoke.444
- ___71-[RTRoutineManager fetchContactScoresFromContactIDs:completionHandler:]_block_invoke.446
- ___72-[RTRoutineManager fetchProximityHistoryFromEventIDs:completionHandler:]_block_invoke.443
- ___81-[RTRoutineManager fetchProximityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.442
- ___85-[RTRoutineManager fetchPeopleDensityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.445
- ___block_descriptor_48_e8_32r40r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8
- ___block_descriptor_56_e8_32s40s48s_e15_v32?08Q16^B24ls32l8s40l8s48l8
- ___block_literal_global.388
- ___block_literal_global.415
- ___block_literal_global.417
- ___block_literal_global.419
- ___block_literal_global.421
- ___block_literal_global.423
- ___block_literal_global.425
- ___block_literal_global.427
- ___block_literal_global.429
- ___block_literal_global.431
- ___block_literal_global.433
- ___block_literal_global.435
- ___block_literal_global.437
- ___block_literal_global.439
- ___block_literal_global.441
CStrings:
+ "\n=== BEGIN analytics submission for event %@ ===\n"
+ "%@ : %@\n"
+ "%@ XPC Connection wasn't to use self.queue. (in %s:%d)"
+ "- "
+ "=== END analytics submission for event %@ ===\n"
+ "B24@?0@\"NSString\"8@\"NSDictionary\"16"
+ "Confidence"
+ "CoreRoutine.HangsMetrics"
+ "ERROR: adjusted start, %@, postdates adjusted end, %@"
+ "End"
+ "METRIC"
+ "Mode of Transportation"
+ "MotionActivities"
+ "RT"
+ "RTHangsMetrics"
+ "Semaphore wait timed out, we're hung!"
+ "Start"
+ "WeeklyActivities"
+ "XPC timeout error while waiting for stored locations, %@."
+ "allKeys"
+ "appendFormat:"
+ "characterSetWithCharactersInString:"
+ "com.apple.%@"
+ "componentsSeparatedByCharactersInSet:"
+ "containsString:"
+ "fetchLocationsHelperQueue"
+ "filteredArrayUsingPredicate:"
+ "hangDuration"
+ "hangType"
+ "hungObject"
+ "hungQueue"
+ "index %d (day), activity type %@, confidence %@, adjustedStart %@, adjustedEnd %@\n"
+ "initWithCString:encoding:"
+ "initWithVisitsDescriptionData:"
+ "motionActivityConfidenceFromString:"
+ "motionActivityTypeFromString:"
+ "now"
+ "predicateWithBlock:"
+ "q24@?0@\"NSString\"8@\"NSString\"16"
+ "received error while getting [SYNC] asynchronous proxy to enumerate stored locations, %@."
+ "semaphore wait timeout"
+ "sortedArrayUsingComparator:"
+ "stringWithCString:encoding:"
+ "submitToCoreAnalytics:type:duration:"
+ "v40@0:8@16q24d32"

```
