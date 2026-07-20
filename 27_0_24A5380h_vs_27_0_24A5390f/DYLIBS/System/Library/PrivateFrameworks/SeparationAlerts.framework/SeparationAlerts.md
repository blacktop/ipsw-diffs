## SeparationAlerts

> `/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-107.0.25.0.0
-  __TEXT.__text: 0x3c5c0
-  __TEXT.__objc_methlist: 0x47fc
+107.0.26.0.0
+  __TEXT.__text: 0x3c784
+  __TEXT.__objc_methlist: 0x482c
   __TEXT.__const: 0x188
-  __TEXT.__oslogstring: 0xa3ef
-  __TEXT.__cstring: 0x2030
+  __TEXT.__oslogstring: 0xa418
+  __TEXT.__cstring: 0x2055
   __TEXT.__gcc_except_tab: 0x2e4
   __TEXT.__unwind_info: 0xa78
   __TEXT.__objc_stubs: 0x0

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x498
+  __DATA_CONST.__const: 0x4a0
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2760
+  __DATA_CONST.__objc_selrefs: 0x2788
   __DATA_CONST.__objc_superrefs: 0x138
-  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__got: 0x400
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x2d20
-  __AUTH_CONST.__objc_const: 0x70f0
+  __AUTH_CONST.__cfstring: 0x2d60
+  __AUTH_CONST.__objc_const: 0x7180
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x2d0
+  __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x5a4
+  __DATA.__objc_ivar: 0x5b0
   __DATA.__data: 0xe40
-  __DATA.__bss: 0x30
-  __DATA_DIRTY.__objc_data: 0xaf0
-  __DATA_DIRTY.__bss: 0x18
+  __DATA.__bss: 0x20
+  __DATA_DIRTY.__objc_data: 0xd70
+  __DATA_DIRTY.__bss: 0x28
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1335
-  Symbols:   3622
-  CStrings:  779
+  Functions: 1339
+  Symbols:   3635
+  CStrings:  781
 
Symbols:
+ -[SASuppressionManager minHistoricalFamiliarity]
+ -[SASuppressionManager setMinHistoricalFamiliarity:]
+ -[SASuppressionResult initWithFamiliarLocation:shortReunionTime:personalVehicle:vehicularMotion:bookendedTravelBTHint:insufficientScanAirTimeWhileTraveling:insufficientScanAirTimeForLBAndBookended:numSafeLocations:recentFamiliarity:historicalFamiliarity:distanceFromHome:predictedLocationReturnTime:contextProbability:minPredictedReunionProbability:minHistoricalFamiliarity:]
+ -[SASuppressionResult minHistoricalFamiliarity]
+ -[SASuppressionResult minPredictedReunionProbability]
+ _OBJC_IVAR_$_SASuppressionManager._minHistoricalFamiliarity
+ _OBJC_IVAR_$_SASuppressionResult._minHistoricalFamiliarity
+ _OBJC_IVAR_$_SASuppressionResult._minPredictedReunionProbability
+ _SATrialFactorMinHistoricalFamiliarity
+ _objc_msgSend$initWithFamiliarLocation:shortReunionTime:personalVehicle:vehicularMotion:bookendedTravelBTHint:insufficientScanAirTimeWhileTraveling:insufficientScanAirTimeForLBAndBookended:numSafeLocations:recentFamiliarity:historicalFamiliarity:distanceFromHome:predictedLocationReturnTime:contextProbability:minPredictedReunionProbability:minHistoricalFamiliarity:
+ _objc_msgSend$localeWithLocaleIdentifier:
+ _objc_msgSend$minHistoricalFamiliarity
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$setMinHistoricalFamiliarity:
- -[SASuppressionResult initWithFamiliarLocation:shortReunionTime:personalVehicle:vehicularMotion:bookendedTravelBTHint:insufficientScanAirTimeWhileTraveling:insufficientScanAirTimeForLBAndBookended:numSafeLocations:recentFamiliarity:historicalFamiliarity:distanceFromHome:predictedLocationReturnTime:contextProbability:]
- _objc_msgSend$initWithFamiliarLocation:shortReunionTime:personalVehicle:vehicularMotion:bookendedTravelBTHint:insufficientScanAirTimeWhileTraveling:insufficientScanAirTimeForLBAndBookended:numSafeLocations:recentFamiliarity:historicalFamiliarity:distanceFromHome:predictedLocationReturnTime:contextProbability:
CStrings:
+ "en_US_POSIX"
+ "minHistoricalFamiliarity"
+ "u"
+ "{\"msg%{public}.0s\":\"#SASuppressionManager received Trial config update\", \"namespace\":\"%{public}@\", \"configKeys\":%{public}lu, \"familiarLocationPolicy\":%{public}hhd, \"shortReunionTimePolicy\":%{public}hhd, \"personalVehiclePolicy\":%{public}hhd, \"vehicularMotionPolicy\":%{public}hhd, \"bookendedTravelBTHintPolicy\":%{public}hhd, \"insufficientScanWhileTravelingPolicy\":%{public}hhd, \"insufficientScanLBAndBookendedPolicy\":%{public}hhd, \"zeroSafeLocationsOverride\":%{public}hhd, \"maxDistanceFromHomeForFamiliar\":\"%{public}f\", \"maxPredictedReunionTime\":\"%{public}f\", \"minPredictedReunionProbability\":\"%{public}f\", \"minScanAirTimeWhileTravelingForAlert\":\"%{public}f\", \"minScanAirTimeForLBAndBookendedAlert\":\"%{public}f\", \"minHistoricalFamiliarity\":\"%{public}f\"}"
- "e"
- "{\"msg%{public}.0s\":\"#SASuppressionManager received Trial config update\", \"namespace\":\"%{public}@\", \"configKeys\":%{public}lu, \"familiarLocationPolicy\":%{public}hhd, \"shortReunionTimePolicy\":%{public}hhd, \"personalVehiclePolicy\":%{public}hhd, \"vehicularMotionPolicy\":%{public}hhd, \"bookendedTravelBTHintPolicy\":%{public}hhd, \"insufficientScanWhileTravelingPolicy\":%{public}hhd, \"insufficientScanLBAndBookendedPolicy\":%{public}hhd, \"zeroSafeLocationsOverride\":%{public}hhd, \"maxDistanceFromHomeForFamiliar\":\"%{public}f\", \"maxPredictedReunionTime\":\"%{public}f\", \"minPredictedReunionProbability\":\"%{public}f\", \"minScanAirTimeWhileTravelingForAlert\":\"%{public}f\", \"minScanAirTimeForLBAndBookendedAlert\":\"%{public}f\"}"
```
