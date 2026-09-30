## CoreRoutine

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/Versions/A/CoreRoutine`

```diff

-986.0.1.0.0
-  __TEXT.__text: 0x406a0
+990.0.10.0.0
+  __TEXT.__text: 0x41450
   __TEXT.__auth_stubs: 0x490
-  __TEXT.__objc_methlist: 0x444c
+  __TEXT.__objc_methlist: 0x4a38
   __TEXT.__const: 0x230
   __TEXT.__oslogstring: 0x239f
-  __TEXT.__cstring: 0x3dab
+  __TEXT.__cstring: 0x3e65
   __TEXT.__gcc_except_tab: 0x364
-  __TEXT.__unwind_info: 0x1238
+  __TEXT.__unwind_info: 0x1270
   __TEXT.__objc_classname: 0x87a
-  __TEXT.__objc_methname: 0x90c8
-  __TEXT.__objc_methtype: 0x1c11
-  __TEXT.__objc_stubs: 0x4f80
+  __TEXT.__objc_methname: 0x91d0
+  __TEXT.__objc_methtype: 0x1c4b
+  __TEXT.__objc_stubs: 0x5040
   __DATA_CONST.__got: 0x300
-  __DATA_CONST.__const: 0x420
+  __DATA_CONST.__const: 0x438
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b90
+  __DATA_CONST.__objc_selrefs: 0x1c40
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x250
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__auth_got: 0x258
-  __AUTH_CONST.__const: 0xe10
-  __AUTH_CONST.__cfstring: 0x3740
-  __AUTH_CONST.__objc_const: 0x8a50
+  __AUTH_CONST.__const: 0xe40
+  __AUTH_CONST.__cfstring: 0x3800
+  __AUTH_CONST.__objc_const: 0x7fd0
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50

   - /System/Library/PrivateFrameworks/GeoServices.framework/Versions/A/GeoServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D677FA7E-2132-3A0F-91B3-A1954ECE97DE
-  Functions: 1667
-  Symbols:   3633
-  CStrings:  2840
+  UUID: 703BA8CA-95D0-3677-8CEF-963DF0C4CCEE
+  Functions: 1679
+  Symbols:   3655
+  CStrings:  2862
 
Symbols:
+ -[RTLocation initWithFirstJSONDictionary:]
+ -[RTLocation outputToDictionaryReadableDate:]
+ -[RTLocation outputToFirstJSONDictionary]
+ -[RTMapItem outputToDictionary]
+ -[RTRoutineManager fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:]
+ -[RTWiFiAccessPoint initWithDictionary:]
+ -[RTWiFiAccessPoint initWithFirstJSONDictionary:]
+ -[RTWiFiAccessPoint outputToDictionary]
+ -[RTWiFiAccessPoint outputToFirstJSONDictionary]
+ __37-[RTRoutineManager _createConnection]_block_invoke.345
+ __37-[RTRoutineManager _createConnection]_block_invoke.346
+ __38-[RTRoutineManager stopLeechingVisits]_block_invoke.438
+ __38-[RTRoutineManager stopLeechingVisits]_block_invoke_2.439
+ __40-[RTRoutineManager stopMonitoringVisits]_block_invoke.434
+ __40-[RTRoutineManager stopMonitoringVisits]_block_invoke_2.435
+ __42-[RTRoutineManager addElevations:handler:]_block_invoke.548
+ __49-[RTRoutineManager fetchRoutineStateWithHandler:]_block_invoke.391
+ __49-[RTRoutineManager stopMonitoringPlaceInferences]_block_invoke.446
+ __49-[RTRoutineManager stopMonitoringPlaceInferences]_block_invoke_2.447
+ __51-[RTRoutineManager fetchRoutineEnabledWithHandler:]_block_invoke.385
+ __51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke.440
+ __51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke_2.441
+ __53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.512
+ __53-[RTRoutineManager fetchElevationsWithOptions:reply:]_block_invoke.549
+ __56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke.471
+ __56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke_2.472
+ __59-[RTRoutineManager enumerateObjectsWithOptions:usingBlock:]_block_invoke.409
+ __65-[RTRoutineManager addBackgroundInertialOdometrySamples:handler:]_block_invoke.551
+ __68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.420
+ __68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.423
+ __69-[RTRoutineManager fetchTransitionsBetweenStartDate:endDate:handler:]_block_invoke.371
+ __69-[RTRoutineManager startMonitoringScenarioTriggerOfType:withHandler:]_block_invoke.463
+ __69-[RTRoutineManager startMonitoringScenarioTriggerOfType:withHandler:]_block_invoke_2.464
+ __70-[RTRoutineManager startMonitoringPlaceInferencesWithOptions:handler:]_block_invoke.442
+ __70-[RTRoutineManager startMonitoringPlaceInferencesWithOptions:handler:]_block_invoke_2.443
+ __78-[RTRoutineManager fetchBackgroundInertialOdometrySamplesWithOptions:handler:]_block_invoke.550
+ ___84-[RTRoutineManager fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:]_block_invoke
+ ___84-[RTRoutineManager fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:]_block_invoke_2
+ ___84-[RTRoutineManager fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:]_block_invoke_3
+ ___block_descriptor_40_e8_32bs_e39_v24?0"RTInferredMapItem"8"NSError"16l
+ __block_literal_global.470
+ __block_literal_global.474
+ __block_literal_global.514
+ __block_literal_global.516
+ __block_literal_global.525
+ __block_literal_global.539
+ __block_literal_global.541
+ __block_literal_global.543
+ __block_literal_global.545
+ __block_literal_global.547
+ __block_literal_global.761
+ _kRTLocationFirstJSONKeyHorizontalUncertainty
+ _kRTLocationFirstJSONKeyLatitude
+ _kRTLocationFirstJSONKeyLongitude
+ _objc_msgSend$fetchFinerGranularityInferredMapItemWithVisitIdentifier:reply:
+ _objc_msgSend$getFormattedDateString
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$outputToDictionary
+ _objc_msgSend$outputToDictionaryReadableDate:
+ _objc_msgSend$setValue:forKey:
- __37-[RTRoutineManager _createConnection]_block_invoke.341
- __37-[RTRoutineManager _createConnection]_block_invoke.342
- __38-[RTRoutineManager stopLeechingVisits]_block_invoke.434
- __38-[RTRoutineManager stopLeechingVisits]_block_invoke_2.435
- __40-[RTRoutineManager stopMonitoringVisits]_block_invoke.430
- __40-[RTRoutineManager stopMonitoringVisits]_block_invoke_2.431
- __42-[RTRoutineManager addElevations:handler:]_block_invoke.538
- __49-[RTRoutineManager fetchRoutineStateWithHandler:]_block_invoke.387
- __49-[RTRoutineManager stopMonitoringPlaceInferences]_block_invoke.442
- __49-[RTRoutineManager stopMonitoringPlaceInferences]_block_invoke_2.443
- __51-[RTRoutineManager fetchRoutineEnabledWithHandler:]_block_invoke.381
- __51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke.436
- __51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke_2.437
- __53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.502
- __53-[RTRoutineManager fetchElevationsWithOptions:reply:]_block_invoke.539
- __56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke.461
- __56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke_2.462
- __59-[RTRoutineManager enumerateObjectsWithOptions:usingBlock:]_block_invoke.405
- __65-[RTRoutineManager addBackgroundInertialOdometrySamples:handler:]_block_invoke.541
- __68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.412
- __68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.419
- __69-[RTRoutineManager fetchTransitionsBetweenStartDate:endDate:handler:]_block_invoke.367
- __69-[RTRoutineManager startMonitoringScenarioTriggerOfType:withHandler:]_block_invoke.453
- __69-[RTRoutineManager startMonitoringScenarioTriggerOfType:withHandler:]_block_invoke_2.454
- __70-[RTRoutineManager startMonitoringPlaceInferencesWithOptions:handler:]_block_invoke.438
- __70-[RTRoutineManager startMonitoringPlaceInferencesWithOptions:handler:]_block_invoke_2.439
- __78-[RTRoutineManager fetchBackgroundInertialOdometrySamplesWithOptions:handler:]_block_invoke.540
- __block_literal_global.460
- __block_literal_global.464
- __block_literal_global.504
- __block_literal_global.506
- __block_literal_global.509
- __block_literal_global.511
- __block_literal_global.513
- __block_literal_global.515
- __block_literal_global.517
- __block_literal_global.535
- __block_literal_global.750
CStrings:
+ "-[RTRoutineManager fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:]"
+ "ch"
+ "dateAsString"
+ "fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:"
+ "fetchFinerGranularityInferredMapItemWithVisitIdentifier:reply:"
+ "initWithDomain:code:userInfo:"
+ "initWithFirstJSONDictionary:"
+ "lat"
+ "lng"
+ "macid"
+ "outputToDictionaryReadableDate:"
+ "outputToFirstJSONDictionary"
+ "requires a non-nil identifier."
+ "setValue:forKey:"
+ "v24@?0@\"RTInferredMapItem\"8@\"NSError\"16"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"RTInferredMapItem\"@\"NSError\">24"

```
