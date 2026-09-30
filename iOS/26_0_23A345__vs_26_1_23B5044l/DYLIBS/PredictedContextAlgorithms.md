## PredictedContextAlgorithms

> `/System/Library/PrivateFrameworks/PredictedContextAlgorithms.framework/PredictedContextAlgorithms`

```diff

-31.0.0.0.0
-  __TEXT.__text: 0x8c984
+33.0.0.0.0
+  __TEXT.__text: 0x8c2f4
   __TEXT.__auth_stubs: 0x1090
   __TEXT.__objc_methlist: 0x6abc
   __TEXT.__const: 0xbe4
-  __TEXT.__cstring: 0x3320
-  __TEXT.__oslogstring: 0x6080
+  __TEXT.__cstring: 0x3330
+  __TEXT.__oslogstring: 0x6090
   __TEXT.__swift5_typeref: 0x2d0
   __TEXT.__swift5_reflstr: 0x14d
   __TEXT.__swift5_assocty: 0x30

   __TEXT.__swift_as_ret: 0x20
   __TEXT.__gcc_except_tab: 0xed8
   __TEXT.__ustring: 0xbe
-  __TEXT.__unwind_info: 0x1918
+  __TEXT.__unwind_info: 0x1910
   __TEXT.__eh_frame: 0x600
   __TEXT.__objc_classname: 0x925
   __TEXT.__objc_methname: 0xd3b0
   __TEXT.__objc_methtype: 0x173f
-  __TEXT.__objc_stubs: 0x8a20
+  __TEXT.__objc_stubs: 0x89e0
   __DATA_CONST.__got: 0x688
   __DATA_CONST.__const: 0xb68
   __DATA_CONST.__objc_classlist: 0x370

   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0x860
   __AUTH_CONST.__const: 0x830
-  __AUTH_CONST.__cfstring: 0x4220
+  __AUTH_CONST.__cfstring: 0x4240
   __AUTH_CONST.__objc_const: 0xac88
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x78

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AA32A0AA-EED6-37E1-AD32-A642CBB28F44
-  Functions: 2828
-  Symbols:   9142
-  CStrings:  4056
+  UUID: FEEE630A-8C2C-37CB-894D-C8A319F57E0E
+  Functions: 2827
+  Symbols:   9140
+  CStrings:  4058
 
Symbols:
- _objc_msgSend$isDominantPlaceForVisits:startDate:endDate:
- _objc_msgSend$predicateWithStartDate:endDate:distanceThreshold:
Functions:
+ sub_1cf3b4284
- sub_1cdfb13d4
- sub_1cdfb1578
~ -[PCWorkoutPredictionAlgorithm generateWorkoutPredictionsFromProbabilities:atTime:embeddings:clusters:] : 4008 -> 2852
~ -[PCWorkoutAnnotationManager getContextEventsForBaseEvents:events:] : 528 -> 432
~ -[PCWorkoutAnnotationManager annotateEventBundle:withContextEvents:andBaseEventReference:] : 664 -> 572
CStrings:
+ "Capping outdoor walk probability to %{public}.2f from %{public}f"
+ "Outdoor Walking"
- "Capping outdoor walk probability to 0.89 from %f"

```
