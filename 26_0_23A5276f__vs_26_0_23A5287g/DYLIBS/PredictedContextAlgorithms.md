## PredictedContextAlgorithms

> `/System/Library/PrivateFrameworks/PredictedContextAlgorithms.framework/PredictedContextAlgorithms`

```diff

-26.0.0.0.0
-  __TEXT.__text: 0x89d8c
-  __TEXT.__auth_stubs: 0x1070
-  __TEXT.__objc_methlist: 0x68fc
+27.0.0.0.0
+  __TEXT.__text: 0x8aac4
+  __TEXT.__auth_stubs: 0x1090
+  __TEXT.__objc_methlist: 0x6a0c
   __TEXT.__const: 0xb64
-  __TEXT.__cstring: 0x31b2
-  __TEXT.__oslogstring: 0x58a9
+  __TEXT.__cstring: 0x3301
+  __TEXT.__oslogstring: 0x5b90
   __TEXT.__swift5_typeref: 0x2d0
   __TEXT.__swift5_reflstr: 0x14d
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__constg_swiftt: 0x4a0
   __TEXT.__swift5_fieldmd: 0x250
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_capture: 0x90
+  __TEXT.__swift5_capture: 0xa0
   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_types: 0x20
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x20
-  __TEXT.__gcc_except_tab: 0xe08
+  __TEXT.__gcc_except_tab: 0xe58
   __TEXT.__ustring: 0xbe
-  __TEXT.__unwind_info: 0x18b0
-  __TEXT.__eh_frame: 0x5d8
-  __TEXT.__objc_classname: 0x921
-  __TEXT.__objc_methname: 0xce1b
-  __TEXT.__objc_methtype: 0x16b1
-  __TEXT.__objc_stubs: 0x8620
+  __TEXT.__unwind_info: 0x18e8
+  __TEXT.__eh_frame: 0x600
+  __TEXT.__objc_classname: 0x923
+  __TEXT.__objc_methname: 0xd171
+  __TEXT.__objc_methtype: 0x16e6
+  __TEXT.__objc_stubs: 0x8880
   __DATA_CONST.__got: 0x688
-  __DATA_CONST.__const: 0xb20
+  __DATA_CONST.__const: 0xb48
   __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2dc0
+  __DATA_CONST.__objc_selrefs: 0x2e60
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x298
-  __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x850
-  __AUTH_CONST.__const: 0x7c8
-  __AUTH_CONST.__cfstring: 0x40c0
-  __AUTH_CONST.__objc_const: 0xaa48
+  __DATA_CONST.__objc_arraydata: 0xf0
+  __AUTH_CONST.__auth_got: 0x860
+  __AUTH_CONST.__const: 0x810
+  __AUTH_CONST.__cfstring: 0x4260
+  __AUTH_CONST.__objc_const: 0xabe8
   __AUTH_CONST.__objc_doubleobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__objc_intobj: 0xd8
+  __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0xb28
   __AUTH.__data: 0x1b0
-  __DATA.__objc_ivar: 0x708
+  __DATA.__objc_ivar: 0x728
   __DATA.__data: 0x258
   __DATA.__bss: 0x4a0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1b30
   __DATA_DIRTY.__data: 0x4b0
   __DATA_DIRTY.__common: 0x38
-  __DATA_DIRTY.__bss: 0x5c0
+  __DATA_DIRTY.__bss: 0x5d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CreateMLComponents.framework/CreateMLComponents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 644B9671-9AAC-31CA-AC1A-95462FA92D15
-  Functions: 2783
-  Symbols:   9002
-  CStrings:  3957
+  UUID: 983F9CC9-B615-3E7B-A9F5-F73DB98D3FF5
+  Functions: 2809
+  Symbols:   9087
+  CStrings:  4028
 
Symbols:
+ +[PCEmbedding indoorOutdoorCategoryActivityTypes]
+ +[PCNeuralNetworkUtilities applySinCosTransform:timeZone:]
+ -[PCEventBundle setWorkoutSessionLocationType:]
+ -[PCEventBundle setWorkoutSwimmingLocationType:]
+ -[PCEventBundle workoutSessionLocationType]
+ -[PCEventBundle workoutSwimmingLocationType]
+ -[PCEventWorkout setWorkoutSessionLocationType:]
+ -[PCEventWorkout setWorkoutSwimmingLocationType:]
+ -[PCEventWorkout workoutSessionLocationType]
+ -[PCEventWorkout workoutSwimmingLocationType]
+ -[PCPInputSignals currentTimeZoneAbbreviation]
+ -[PCPInputSignals hasCurrentTimeZoneAbbreviation]
+ -[PCPInputSignals setCurrentTimeZoneAbbreviation:]
+ -[PCPPredictedContextWorkout StringAsWorkoutLocationType:]
+ -[PCPPredictedContextWorkout hasWorkoutLocationType]
+ -[PCPPredictedContextWorkout setHasWorkoutLocationType:]
+ -[PCPPredictedContextWorkout setWorkoutLocationType:]
+ -[PCPPredictedContextWorkout workoutLocationTypeAsString:]
+ -[PCPPredictedContextWorkout workoutLocationType]
+ -[PCVisitHistoryPredictor candidateTimeZone]
+ -[PCVisitHistoryPredictor computeWithHistory:transitions:locationsOfInterest:homekitHomes:atTime:inTimeZone:withError:]
+ -[PCVisitHistoryPredictor setCandidateTimeZone:]
+ -[PCVisitHistoryPredictor setTimeZone:]
+ -[PCVisitHistoryPredictor timeZone]
+ -[PCWorkoutPredictionAlgorithm _updateActivityInfoForPrediction:fromActivityType:]
+ OBJC_IVAR_$_PCPInputSignals._currentTimeZoneAbbreviation
+ OBJC_IVAR_$_PCPPredictedContextWorkout._workoutLocationType
+ _$sIeAgH_ytIeAgHr_TRTA.88
+ _$sIeAgH_ytIeAgHr_TRTA.88TQ0_
+ _$sIeAgH_ytIeAgHr_TRTA.88Tu
+ _$sIeghH_IeAgH_TRTA.83
+ _$sIeghH_IeAgH_TRTA.83TQ0_
+ _$sIeghH_IeAgH_TRTA.83Tu
+ _$sSS11utf8CStrings15ContiguousArrayVys4Int8VGvg
+ _$sScTss5NeverORs_rlE4name8priority9operationScTyxABGSSSg_ScPSgxyYaYAcntcfCyt_Tt2gq5
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TA.70
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TA.70TQ0_
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TA.70Tu
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_IVAR_$_PCEventBundle._workoutSessionLocationType
+ _OBJC_IVAR_$_PCEventBundle._workoutSwimmingLocationType
+ _OBJC_IVAR_$_PCEventWorkout._workoutSessionLocationType
+ _OBJC_IVAR_$_PCEventWorkout._workoutSwimmingLocationType
+ _OBJC_IVAR_$_PCVisitHistoryPredictor._candidateTimeZone
+ _OBJC_IVAR_$_PCVisitHistoryPredictor._timeZone
+ ___119-[PCVisitHistoryPredictor computeWithHistory:transitions:locationsOfInterest:homekitHomes:atTime:inTimeZone:withError:]_block_invoke
+ ___49+[PCEmbedding indoorOutdoorCategoryActivityTypes]_block_invoke
+ ___block_literal_global.183
+ _objc_msgSend$_updateActivityInfoForPrediction:fromActivityType:
+ _objc_msgSend$abbreviation
+ _objc_msgSend$applySinCosTransform:timeZone:
+ _objc_msgSend$candidateTimeZone
+ _objc_msgSend$computeWithHistory:transitions:locationsOfInterest:homekitHomes:atTime:inTimeZone:withError:
+ _objc_msgSend$currentTimeZoneAbbreviation
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hasSessionLocationType
+ _objc_msgSend$hasSwimmingLocationType
+ _objc_msgSend$indoorOutdoorCategoryActivityTypes
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$sessionLocationType
+ _objc_msgSend$setCandidateTimeZone:
+ _objc_msgSend$setCurrentTimeZoneAbbreviation:
+ _objc_msgSend$setWorkoutLocationType:
+ _objc_msgSend$setWorkoutSessionLocationType:
+ _objc_msgSend$setWorkoutSwimmingLocationType:
+ _objc_msgSend$swimmingLocationType
+ _objc_msgSend$workoutLocationType
+ _objc_msgSend$workoutSessionLocationType
+ _objc_msgSend$workoutSwimmingLocationType
+ _swift_retain
- +[PCNeuralNetworkUtilities applySinCosTransform:]
- -[PCVisitHistoryPredictor computeWithHistory:transitions:locationsOfInterest:homekitHomes:atTime:withError:]
- _$sIeAgH_ytIeAgHr_TRTA.83
- _$sIeAgH_ytIeAgHr_TRTA.83TQ0_
- _$sIeAgH_ytIeAgHr_TRTA.83Tu
- _$sIeghH_IeAgH_TRTA.78
- _$sIeghH_IeAgH_TRTA.78TQ0_
- _$sIeghH_IeAgH_TRTA.78Tu
- _$sScTss5NeverORs_rlE8priority9operationScTyxABGScPSg_xyYaYAcntcfCyt_Tt1gq5
- ___108-[PCVisitHistoryPredictor computeWithHistory:transitions:locationsOfInterest:homekitHomes:atTime:withError:]_block_invoke
- ___block_literal_global.187
- _objc_msgSend$applySinCosTransform:
- _objc_msgSend$computeWithHistory:transitions:locationsOfInterest:homekitHomes:atTime:withError:
CStrings:
+ "\r"
+ " ("
+ "<%@ bundleIdentifier:%@, suggestionID:%@, startDate:%@, endDate:%@, creationDate:%@, interfaceType:%lu, activityType:%@, bundleSubType:%lu, bundleSuperType:%lu, time:%@, eventCount:%lu, placeType:%d, placeUserType:%d, poiCategory:%@, workoutSessionLocationType:%d, workoutSwimmingLocationType:%d>"
+ "<%@ workoutType:%@, sourceBundleIdentifier:%@, hkObjectIdentifier:%@, workoutSessionLocationType:%d, workoutSwimmingLocationType:%d>"
+ "Before deduping: Cluster %@: activityType='%@' (length=%lu)"
+ "Checking if '%@' is already predicted in %lu existing predictions"
+ "Comparing with existing prediction: workoutType=%llu, locationType=%d (looking for workoutType=%llu, locationType=%d)"
+ "Converted '%@' to workout type %llu"
+ "Created prediction for activity type: %@, total predictions now: %lu"
+ "Extracted base='%@', location=%d from '%@'"
+ "Indoor "
+ "Indoor %@"
+ "No input time zone - defaulting to PST for training"
+ "No trained time zone - defaulting to PST for prediction"
+ "Open Water "
+ "Open Water %@"
+ "Outdoor "
+ "Outdoor %@"
+ "Pool "
+ "Pool %@"
+ "Prediction time zone: %@"
+ "Selected cluster %@, workoutType: %@ , probability: %.4f"
+ "StringAsWorkoutLocationType:"
+ "T@\"NSString\",&,N,V_currentTimeZoneAbbreviation"
+ "T@\"NSTimeZone\",&,N,V_candidateTimeZone"
+ "Ti,N,V_workoutLocationType"
+ "Ti,N,V_workoutSessionLocationType"
+ "Ti,N,V_workoutSwimmingLocationType"
+ "Training time zone: %@"
+ "Updated activity type from '%@' to '%@'"
+ "Updated base activity type to '%@'"
+ "Workout %@ (workoutType=%llu, locationType=%d) is already predicted, skipping"
+ "Workout '%@' is NOT already predicted"
+ "WorkoutPrediction: Created Workout eventID, %@, workoutType, %@, sourceBundleIdentifier, %@, workoutLocationStart, %{sensitive}@, hkObjectIdentifier, %@, workoutSessionLocationType, %d, workoutSwimmingLocationType, %d"
+ "_candidateTimeZone"
+ "_currentTimeZoneAbbreviation"
+ "_updateActivityInfoForPrediction:fromActivityType:"
+ "_workoutLocationType"
+ "_workoutSessionLocationType"
+ "_workoutSwimmingLocationType"
+ "abbreviation"
+ "applySinCosTransform:timeZone:"
+ "candidateTimeZone"
+ "computeWithHistory:transitions:locationsOfInterest:homekitHomes:atTime:inTimeZone:withError:"
+ "currentTimeZoneAbbreviation"
+ "hasCurrentTimeZoneAbbreviation"
+ "hasPrefix:"
+ "hasWorkoutLocationType"
+ "indoorOutdoorCategoryActivityTypes"
+ "rangeOfString:"
+ "setCandidateTimeZone:"
+ "setCurrentTimeZoneAbbreviation:"
+ "setHasWorkoutLocationType:"
+ "setWorkoutLocationType:"
+ "setWorkoutSessionLocationType:"
+ "setWorkoutSwimmingLocationType:"
+ "timeZone decoded as %@"
+ "timeZone decoded as empty"
+ "v72@0:8@16@24@32@40d48@56^@64"
+ "workoutActivityType: %llu, workoutLocationType: %d, probability: %.2f, sourceBundleIdentifier: %@, entry time: %.2f, exit time: %.2f, sources: %@"
+ "workoutLocationType"
+ "workoutLocationTypeAsString:"
+ "workoutSessionLocationType"
+ "workoutSwimmingLocationType"
+ "{?=\"workoutActivityType\"b1\"workoutLocationType\"b1}"
- "\v"
- "<%@ bundleIdentifier:%@, suggestionID:%@, startDate:%@, endDate:%@, creationDate:%@, interfaceType:%lu, activityType:%@, bundleSubType:%lu, bundleSuperType:%lu, time:%@, eventCount:%lu, placeType:%d, placeUserType:%d, poiCategory:%@>"
- "<%@ workoutType:%@, sourceBundleIdentifier:%@, hkObjectIdentifier:%@>"
- "Created prediction for activity type: %@"
- "Selected cluster %@, workoutType: %@ (%llu), probability: %.4f"
- "WorkoutPrediction: Created Workout eventID, %@, workoutType, %@, sourceBundleIdentifier, %@, workoutLocationStart, %{sensitive}@, hkObjectIdentifier, %@"
- "WorkoutPrediction: Workout %llu is already predicted, skipping"
- "applySinCosTransform:"
- "computeWithHistory:transitions:locationsOfInterest:homekitHomes:atTime:withError:"
- "workoutActivityType: %llu, probability: %.2f, sourceBundleIdentifier: %@, entry time: %.2f, exit time: %.2f, sources: %@"
- "{?=\"workoutActivityType\"b1}"

```
