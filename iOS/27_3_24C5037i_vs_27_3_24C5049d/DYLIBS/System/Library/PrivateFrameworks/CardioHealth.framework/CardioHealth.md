## CardioHealth

> `/System/Library/PrivateFrameworks/CardioHealth.framework/CardioHealth`

```diff

-3188.0.7.0.1
-  __TEXT.__text: 0xd43c
-  __TEXT.__const: 0x564
-  __TEXT.__gcc_except_tab: 0x39c
+3188.0.11.0.0
+  __TEXT.__text: 0xd874
+  __TEXT.__const: 0x584
+  __TEXT.__gcc_except_tab: 0x3a4
   __TEXT.__cstring: 0xed
-  __TEXT.__oslogstring: 0x26ef
+  __TEXT.__oslogstring: 0x2783
   __TEXT.__unwind_info: 0x2d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libz.1.dylib
   Functions: 105
   Symbols:   88
-  CStrings:  97
+  CStrings:  98
 
Functions:
~ sub_25cdf1d4c -> sub_25dfe1d4c : 5996 -> 6432
~ __ZN17CHVO2MaxEstimator16feedWorkoutEventERKN12CardioHealth12WorkoutEventE : 6256 -> 6308
~ __ZN17CHVO2MaxEstimator18retrocomputeVO2MaxEdRKNSt3__16vectorI11VO2MaxInputNS0_9allocatorIS2_EEEERKNS1_I13VO2MaxSummaryNS3_IS8_EEEERKN12CardioHealth13CHBodyMetricsEddNSD_13CHWorkoutTypeENSD_23CHWorkoutSessionDetails4TypeER31VO2MaxRetrocomputeSessionResult : 1332 -> 1388
~ sub_25cdf7b98 -> sub_25dfe7db8 : 9200 -> 9572
~ sub_25cdf9f88 -> sub_25dfea31c : 1868 -> 2032
CStrings:
+ "VO2Max Step Test confident HR at or below resting: droppedPairs=%{public}d, confidentPairs=%{public}d, restingHR=%{private}.0f, hrMax=%{private}.0f"
```
