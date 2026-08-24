## PredictedContextAlgorithms

> `/System/Library/PrivateFrameworks/PredictedContextAlgorithms.framework/Versions/A/PredictedContextAlgorithms`

```diff

-46.0.0.0.0
-  __TEXT.__text: 0x9f62c
-  __TEXT.__objc_methlist: 0x6de4
+46.0.1.0.0
+  __TEXT.__text: 0x9f90c
+  __TEXT.__objc_methlist: 0x6dec
   __TEXT.__const: 0xcd8
-  __TEXT.__cstring: 0x32a6
-  __TEXT.__oslogstring: 0x6c6c
+  __TEXT.__cstring: 0x32a2
+  __TEXT.__oslogstring: 0x6d23
   __TEXT.__swift5_typeref: 0x2ec
   __TEXT.__swift5_capture: 0xe0
   __TEXT.__swift5_reflstr: 0x14d

   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x2fb0
+  __DATA_CONST.__objc_selrefs: 0x2fb8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__got: 0x678
   __AUTH_CONST.__const: 0xbc8
-  __AUTH_CONST.__cfstring: 0x43c0
+  __AUTH_CONST.__cfstring: 0x4400
   __AUTH_CONST.__objc_const: 0xb0e8
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x180

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2933
-  Symbols:   6512
-  CStrings:  1080
+  Functions: 2934
+  Symbols:   6514
+  CStrings:  1082
 
Symbols:
+ -[PCWorkoutPredictionAlgorithm _locationMatchesRecord:visitPlaceType:visitLat:visitLon:]
+ -[PCWorkoutPredictionAlgorithm _passesLocDowLocTimeGateForActivityType:currentVisit:workoutTypeLocationMap:]
+ _objc_msgSend$_locationMatchesRecord:visitPlaceType:visitLat:visitLon:
+ _objc_msgSend$_passesLocDowLocTimeGateForActivityType:currentVisit:workoutTypeLocationMap:
- -[PCWorkoutPredictionAlgorithm _hasUserWorkedOutForActivityType:nearCurrentVisit:workoutTypeLocationMap:]
- _objc_msgSend$_hasUserWorkedOutForActivityType:nearCurrentVisit:workoutTypeLocationMap:
CStrings:
+ "dow"
+ "hour"
+ "lat"
+ "locDoW_locTime gate FAIL for %{public}@: locDow=%{public}d, locTime=%{public}d (n=%{public}lu, vDow=%{public}ld, vHour=%{public}.2f)"
+ "locDoW_locTime gate PASS for %{public}@ (vDow=%{public}ld, vHour=%{public}.2f)"
+ "locDoW_locTime gate rejected %{public}@ at this visit, skipping cluster %{public}@"
+ "locDoW_locTime gate: no prior %{public}@ workouts"
+ "locDoW_locTime gate: visit missing dow/hour, rejecting %{public}@"
+ "locDoW_locTime gate: visit missing location/time context for %{public}@"
+ "lon"
- "Found %@ workout with matching placeType: %@"
- "Found %@ workout within %.1f miles: %.3f miles"
- "No location context in current visit"
- "No location data found for activity type: %@"
- "No matching %@ workout locations found near this visit"
- "User has not done %@ workouts at current location, skipping cluster %@"
- "locations"
- "placeTypes"
```
