## CoreRoutine

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine`

```diff

-895.0.11.0.2
-  __TEXT.__text: 0x3aee0
-  __TEXT.__auth_stubs: 0x620
-  __TEXT.__objc_methlist: 0x442c
+896.0.1.0.1
+  __TEXT.__text: 0x3baf4
+  __TEXT.__auth_stubs: 0x680
+  __TEXT.__objc_methlist: 0x4454
   __TEXT.__const: 0x190
-  __TEXT.__oslogstring: 0x212b
-  __TEXT.__cstring: 0x39d2
-  __TEXT.__gcc_except_tab: 0x1b8
-  __TEXT.__unwind_info: 0x108c
-  __TEXT.__objc_classname: 0x815
-  __TEXT.__objc_methname: 0x8e98
-  __TEXT.__objc_methtype: 0x1ad5
-  __TEXT.__objc_stubs: 0x4ec0
+  __TEXT.__oslogstring: 0x21e2
+  __TEXT.__cstring: 0x3b0f
+  __TEXT.__gcc_except_tab: 0x280
+  __TEXT.__unwind_info: 0x10a4
+  __TEXT.__objc_classname: 0x824
+  __TEXT.__objc_methname: 0x8fee
+  __TEXT.__objc_methtype: 0x1ae6
+  __TEXT.__objc_stubs: 0x5080
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0xb28
-  __DATA_CONST.__objc_classlist: 0x278
+  __DATA_CONST.__const: 0xb68
+  __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6180
-  __DATA_CONST.__objc_selrefs: 0x1b48
+  __DATA_CONST.__objc_const: 0x61c8
+  __DATA_CONST.__objc_selrefs: 0x1bc0
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__cfstring: 0x36e0
-  __AUTH_CONST.__objc_const: 0x29b8
-  __AUTH_CONST.__const: 0x340
+  __AUTH_CONST.__cfstring: 0x3860
+  __AUTH_CONST.__objc_const: 0x2a00
+  __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x320
-  __AUTH.__objc_data: 0x5a0
+  __AUTH_CONST.__auth_got: 0x350
+  __AUTH.__objc_data: 0x5f0
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x2b0
-  __DATA.__objc_superrefs: 0x248
+  __DATA.__objc_classrefs: 0x2c8
+  __DATA.__objc_superrefs: 0x250
   __DATA.__objc_ivar: 0x490
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
-  Functions: 1623
-  Symbols:   5200
-  CStrings:  2404
+  Functions: 1629
+  Symbols:   5245
+  CStrings:  2439
 
Symbols:
+ -[NSArray(RTExtensions) shuffle]
+ -[RTHangsMetrics init]
+ -[RTHangsMetrics submitToCoreAnalytics:type:duration:]
+ _AnalyticsSendEvent
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_RTHangsMetrics
+ _OBJC_METACLASS_$_RTHangsMetrics
+ _RTAnalyticsEventHangsMetrics
+ _RTLogFacilityMetric
+ __OBJC_$_INSTANCE_METHODS_RTHangsMetrics
+ __OBJC_CLASS_RO_$_RTHangsMetrics
+ __OBJC_METACLASS_RO_$_RTHangsMetrics
+ ___38-[RTRoutineManager stopLeechingVisits]_block_invoke.391
+ ___40-[RTRoutineManager stopMonitoringVisits]_block_invoke.390
+ ___42-[RTRoutineManager addElevations:handler:]_block_invoke.455
+ ___51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke.392
+ ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.421
+ ___53-[RTRoutineManager fetchElevationsWithOptions:reply:]_block_invoke.456
+ ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke.396
+ ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.387
+ ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.388
+ ___68-[RTRoutineManager fetchPeopleCountEventsHistory:completionHandler:]_block_invoke.452
+ ___71-[RTRoutineManager fetchContactScoresFromContactIDs:completionHandler:]_block_invoke.454
+ ___72-[RTRoutineManager fetchProximityHistoryFromEventIDs:completionHandler:]_block_invoke.451
+ ___81-[RTRoutineManager fetchProximityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.450
+ ___85-[RTRoutineManager fetchPeopleDensityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.453
+ ____RTSemaphoreWait_block_invoke
+ ___block_descriptor_32_e31_q24?0"NSString"8"NSString"16l
+ ___block_descriptor_32_e35_B24?0"NSString"8"NSDictionary"16l
+ ___block_descriptor_56_e8_32r40r48r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8r48l8
+ ___block_literal_global.398
+ ___block_literal_global.423
+ ___block_literal_global.425
+ ___block_literal_global.427
+ ___block_literal_global.429
+ ___block_literal_global.431
+ ___block_literal_global.433
+ ___block_literal_global.435
+ ___block_literal_global.437
+ ___block_literal_global.439
+ ___block_literal_global.441
+ ___block_literal_global.443
+ ___block_literal_global.445
+ ___block_literal_global.447
+ ___block_literal_global.449
+ ___block_literal_global.635
+ ___log_analytics_submission_block_invoke
+ _dispatch_queue_get_label
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_time
+ _log_analytics_submission
+ _objc_msgSend$_queue
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$componentsSeparatedByCharactersInSet:
+ _objc_msgSend$containsString:
+ _objc_msgSend$exchangeObjectAtIndex:withObjectAtIndex:
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$initWithCString:encoding:
+ _objc_msgSend$now
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_msgSend$submitToCoreAnalytics:type:duration:
- ___38-[RTRoutineManager stopLeechingVisits]_block_invoke.388
- ___40-[RTRoutineManager stopMonitoringVisits]_block_invoke.387
- ___42-[RTRoutineManager addElevations:handler:]_block_invoke.452
- ___51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke.389
- ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.418
- ___53-[RTRoutineManager fetchElevationsWithOptions:reply:]_block_invoke.453
- ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke.393
- ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.384
- ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.385
- ___68-[RTRoutineManager fetchPeopleCountEventsHistory:completionHandler:]_block_invoke.449
- ___71-[RTRoutineManager fetchContactScoresFromContactIDs:completionHandler:]_block_invoke.451
- ___72-[RTRoutineManager fetchProximityHistoryFromEventIDs:completionHandler:]_block_invoke.448
- ___81-[RTRoutineManager fetchProximityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.447
- ___85-[RTRoutineManager fetchPeopleDensityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.450
- ___block_descriptor_48_e8_32r40r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8
- ___block_literal_global.392
- ___block_literal_global.420
- ___block_literal_global.422
- ___block_literal_global.424
- ___block_literal_global.426
- ___block_literal_global.428
- ___block_literal_global.430
- ___block_literal_global.432
- ___block_literal_global.434
- ___block_literal_global.436
- ___block_literal_global.438
- ___block_literal_global.440
- ___block_literal_global.442
- ___block_literal_global.444
- ___block_literal_global.446
CStrings:
+ "\n=== BEGIN analytics submission for event %@ ===\n"
+ "%@ : %@\n"
+ "%@ XPC Connection wasn't to use self.queue. (in %s:%d)"
+ "- "
+ "=== END analytics submission for event %@ ===\n"
+ "B24@?0@\"NSString\"8@\"NSDictionary\"16"
+ "CoreRoutine.HangsMetrics"
+ "METRIC"
+ "RT"
+ "RTHangsMetrics"
+ "Semaphore wait timed out, we're hung!"
+ "XPC timeout error while waiting for stored locations, %@."
+ "appendFormat:"
+ "arrayWithArray:"
+ "characterSetWithCharactersInString:"
+ "com.apple.%@"
+ "componentsSeparatedByCharactersInSet:"
+ "containsString:"
+ "exchangeObjectAtIndex:withObjectAtIndex:"
+ "fetchLocationsHelperQueue"
+ "filteredArrayUsingPredicate:"
+ "hangDuration"
+ "hangType"
+ "hungObject"
+ "hungQueue"
+ "initWithCString:encoding:"
+ "now"
+ "predicateWithBlock:"
+ "q24@?0@\"NSString\"8@\"NSString\"16"
+ "received error while getting asynchronous proxy to enumerate stored locations, %@."
+ "semaphore wait timeout"
+ "shuffle"
+ "sortedArrayUsingComparator:"
+ "stringWithCString:encoding:"
+ "submitToCoreAnalytics:type:duration:"
+ "v40@0:8@16q24d32"
- "Invalid parameter not satisfying: geoAddressObject"

```
