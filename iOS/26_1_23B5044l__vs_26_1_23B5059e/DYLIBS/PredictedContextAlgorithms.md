## PredictedContextAlgorithms

> `/System/Library/PrivateFrameworks/PredictedContextAlgorithms.framework/PredictedContextAlgorithms`

```diff

-33.0.0.0.0
-  __TEXT.__text: 0x8c2f4
-  __TEXT.__auth_stubs: 0x1090
-  __TEXT.__objc_methlist: 0x6abc
-  __TEXT.__const: 0xbe4
-  __TEXT.__cstring: 0x3330
-  __TEXT.__oslogstring: 0x6090
-  __TEXT.__swift5_typeref: 0x2d0
+36.0.0.0.0
+  __TEXT.__text: 0x8e628
+  __TEXT.__auth_stubs: 0x10a0
+  __TEXT.__objc_methlist: 0x6b44
+  __TEXT.__const: 0xbf4
+  __TEXT.__cstring: 0x3399
+  __TEXT.__oslogstring: 0x6a22
+  __TEXT.__swift5_typeref: 0x2e0
   __TEXT.__swift5_reflstr: 0x14d
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__constg_swiftt: 0x4a0
+  __TEXT.__constg_swiftt: 0x4a8
   __TEXT.__swift5_fieldmd: 0x250
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_capture: 0xa0

   __TEXT.__swift_as_ret: 0x20
   __TEXT.__gcc_except_tab: 0xed8
   __TEXT.__ustring: 0xbe
-  __TEXT.__unwind_info: 0x1910
-  __TEXT.__eh_frame: 0x600
-  __TEXT.__objc_classname: 0x925
-  __TEXT.__objc_methname: 0xd3b0
-  __TEXT.__objc_methtype: 0x173f
-  __TEXT.__objc_stubs: 0x89e0
-  __DATA_CONST.__got: 0x688
+  __TEXT.__unwind_info: 0x1940
+  __TEXT.__eh_frame: 0x628
+  __TEXT.__objc_classname: 0x93f
+  __TEXT.__objc_methname: 0xd64c
+  __TEXT.__objc_methtype: 0x17a4
+  __TEXT.__objc_stubs: 0x8b60
+  __DATA_CONST.__got: 0x690
   __DATA_CONST.__const: 0xb68
-  __DATA_CONST.__objc_classlist: 0x370
+  __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ec8
+  __DATA_CONST.__objc_selrefs: 0x2f28
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x298
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0x860
+  __AUTH_CONST.__auth_got: 0x868
   __AUTH_CONST.__const: 0x830
-  __AUTH_CONST.__cfstring: 0x4240
-  __AUTH_CONST.__objc_const: 0xac88
+  __AUTH_CONST.__cfstring: 0x4300
+  __AUTH_CONST.__objc_const: 0xad48
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x858
+  __AUTH.__objc_data: 0x8b0
   __AUTH.__data: 0x1b0
-  __DATA.__objc_ivar: 0x734
-  __DATA.__data: 0x258
+  __DATA.__objc_ivar: 0x738
+  __DATA.__data: 0x288
   __DATA.__bss: 0x4a0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1e00

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FEEE630A-8C2C-37CB-894D-C8A319F57E0E
-  Functions: 2827
-  Symbols:   9140
-  CStrings:  4058
+  UUID: D7D55C9E-79A0-3ED1-8B4F-D154D7BC4C86
+  Functions: 2841
+  Symbols:   9192
+  CStrings:  4125
 
Symbols:
+ +[PCGenericRoutinePredictor buildValidLoiIdentifiersFromHistory:forDayOfWeek:forHour:forMinute:atTime:inTimeZone:timeWindowHours:requireExactDayOfWeek:]
+ +[PCGenericRoutinePredictor filterCandidateVisitsByRoutine:withHistory:atTime:inTimeZone:]
+ +[PCGenericRoutinePredictor filterCandidateVisitsByRoutine:withHistory:atTime:inTimeZone:timeWindowHours:requireExactDayOfWeek:]
+ +[PCGenericRoutinePredictor shouldKeepCandidateVisit:withValidLoiIdentifiers:]
+ -[PCOutOfPatternLogic _requestRetrainIfNeededWithReason:]
+ -[PCOutOfPatternLogic isAwaitingRetrain]
+ -[PCOutOfPatternLogic isWaitingRetrain]
+ -[PCOutOfPatternLogic resetAwaitingRetrainWithCurrentLocation:inputSignals:]
+ -[PCOutOfPatternLogic setIsAwaitingRetrain:]
+ -[PCWorkoutPredictionAlgorithm _buildWorkoutTypeLocationMapping:]
+ -[PCWorkoutPredictionAlgorithm _hasUserWorkedOutForActivityType:nearCurrentVisit:workoutTypeLocationMap:]
+ -[PCWorkoutPredictionAlgorithm generateWorkoutPredictionsFromProbabilities:atTime:currentVisit:embeddings:clusters:]
+ _$s14NeuralNetworks13ComputeDeviceV7bnnsCPUACSgvgZ
+ _$s14NeuralNetworks6TensorV15withUnsafeBytesyxxSWKXEKlF
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC17predictFromTensor8xPredict01xJ6Matrix9timestepsSaySaySaySfGGGAJ_AISitFAJSWXEfU_
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC17predictFromTensor8xPredict01xJ6Matrix9timestepsSaySaySaySfGGGAJ_AISitFAJSWXEfU_TA
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC20getBNNSComputeDevice14NeuralNetworks07ComputeI0VyF
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC20getBNNSComputeDevice14NeuralNetworks07ComputeI0VyFTj
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC20getBNNSComputeDevice14NeuralNetworks07ComputeI0VyFTq
+ _$sSaySaySaySfGGGMD
+ _OBJC_CLASS_$_PCGenericRoutinePredictor
+ _OBJC_IVAR_$_PCOutOfPatternLogic._isAwaitingRetrain
+ _OBJC_METACLASS_$_PCGenericRoutinePredictor
+ _PCLogCategoryGenericRoutinePredictor
+ __OBJC_$_CLASS_METHODS_PCGenericRoutinePredictor
+ __OBJC_CLASS_RO_$_PCGenericRoutinePredictor
+ __OBJC_METACLASS_RO_$_PCGenericRoutinePredictor
+ ___block_literal_global.17
+ ___block_literal_global.20
+ _kLocationFilteringMaxDistanceMiles
+ _objc_msgSend$_buildWorkoutTypeLocationMapping:
+ _objc_msgSend$_hasUserWorkedOutForActivityType:nearCurrentVisit:workoutTypeLocationMap:
+ _objc_msgSend$_requestRetrainIfNeededWithReason:
+ _objc_msgSend$buildValidLoiIdentifiersFromHistory:forDayOfWeek:forHour:forMinute:atTime:inTimeZone:timeWindowHours:requireExactDayOfWeek:
+ _objc_msgSend$containsValueForKey:
+ _objc_msgSend$filterCandidateVisitsByRoutine:withHistory:atTime:inTimeZone:
+ _objc_msgSend$filterCandidateVisitsByRoutine:withHistory:atTime:inTimeZone:timeWindowHours:requireExactDayOfWeek:
+ _objc_msgSend$generateWorkoutPredictionsFromProbabilities:atTime:currentVisit:embeddings:clusters:
+ _objc_msgSend$isAwaitingRetrain
+ _objc_msgSend$isWaitingRetrain
+ _objc_msgSend$resetAwaitingRetrainWithCurrentLocation:inputSignals:
+ _objc_msgSend$setIsAwaitingRetrain:
+ _objc_msgSend$shouldKeepCandidateVisit:withValidLoiIdentifiers:
+ _symbolic SaySaySaySfGGG
- -[PCWorkoutPredictionAlgorithm generateWorkoutPredictionsFromProbabilities:atTime:embeddings:clusters:]
- _$s14NeuralNetworks6TensorV7scalars2asSayxGxm_tAA0C6ScalarRzlF
- _$sSa6append10contentsOfyqd__n_t7ElementQyd__RszSTRd__lFSaySaySfGG_SayAFGTg5
- ___block_literal_global.11
- _objc_msgSend$generateWorkoutPredictionsFromProbabilities:atTime:embeddings:clusters:
CStrings:
+ "@56@0:8@16d24@32@40@48"
+ "@76@0:8@16q24q32q40d48@56d64B72"
+ "Already awaiting retrain, not requesting again (reason: %@)"
+ "BNNS unavailable, falling back to CPU backend"
+ "Built workout type location mapping for %lu activity types"
+ "Found %@ workout with matching placeType: %@"
+ "Found %@ workout within %.1f miles: %.3f miles"
+ "GMT"
+ "GOOP detection"
+ "GenericRoutinePredictor"
+ "Missing model centroid, indicating no trained model"
+ "No current visit provided to generate predictions"
+ "No embeddings provided to _buildWorkoutTypeLocationMapping"
+ "No location context in current visit"
+ "No location data found for activity type: %@"
+ "No matching %@ workout locations found near this visit"
+ "PCGenericRoutinePredictor"
+ "PCGenericRoutinePredictor: Candidate visit missing LOI information, keeping visit for other predictors"
+ "PCGenericRoutinePredictor: Current time - Day of week: %ld, Hour: %ld, Minute: %ld"
+ "PCGenericRoutinePredictor: Failed to extract date components - aborting filtering"
+ "PCGenericRoutinePredictor: Filtering out visit with LOI ID %@ and probability %.3f - no routine pattern found for this day/time"
+ "PCGenericRoutinePredictor: Found %lu valid LOI identifiers for routine filtering"
+ "PCGenericRoutinePredictor: Invalid currentTimeCFAbsolute %f - aborting filtering"
+ "PCGenericRoutinePredictor: Invalid date components (dow=%ld, h=%ld, m=%ld) - aborting"
+ "PCGenericRoutinePredictor: Invalid timeWindowHours %f - using default"
+ "PCGenericRoutinePredictor: Large timeWindowHours %f - clamping to 12.0"
+ "PCGenericRoutinePredictor: No candidate visits to filter"
+ "PCGenericRoutinePredictor: No input time zone - defaulting to PST for routine filtering"
+ "PCGenericRoutinePredictor: No timezone available - using system timezone"
+ "PCGenericRoutinePredictor: No visit history available for routine filtering"
+ "PCGenericRoutinePredictor: PST timezone unavailable - falling back to GMT"
+ "PCGenericRoutinePredictor: Removed %lu visits that don't match routine patterns, %lu visits remaining"
+ "PCGenericRoutinePredictor: Routine filtering time zone: %@"
+ "PCGenericRoutinePredictor: Starting routine filtering with %lu candidate visits and %lu historical visits"
+ "PCGenericRoutinePredictor: currentTimeCFAbsolute %f outside reasonable bounds - aborting"
+ "Reset awaiting retrain state after successful retrain. New modelCentroid: %{sensitive}@"
+ "Reset awaiting retrain state while not waiting for a retrain, no-op"
+ "Setting awaiting retrain flag for %@"
+ "Suppressing history based predictors due to awaiting retrain"
+ "TB,N,V_isAwaitingRetrain"
+ "User has not done %@ workouts at current location, skipping cluster %@"
+ "Using BNNS backend"
+ "_buildWorkoutTypeLocationMapping:"
+ "_hasUserWorkedOutForActivityType:nearCurrentVisit:workoutTypeLocationMap:"
+ "_isAwaitingRetrain"
+ "_requestRetrainIfNeededWithReason:"
+ "buildValidLoiIdentifiersFromHistory:forDayOfWeek:forHour:forMinute:atTime:inTimeZone:timeWindowHours:requireExactDayOfWeek:"
+ "coder doesn't contain visit history config key - initializing with default config instead"
+ "containsValueForKey:"
+ "filterCandidateVisitsByRoutine:withHistory:atTime:inTimeZone:"
+ "filterCandidateVisitsByRoutine:withHistory:atTime:inTimeZone:timeWindowHours:requireExactDayOfWeek:"
+ "generateWorkoutPredictionsFromProbabilities:atTime:currentVisit:embeddings:clusters:"
+ "initial model training"
+ "isAwaitingRetrain"
+ "isWaitingRetrain"
+ "locations"
+ "placeTypes"
+ "resetAwaitingRetrainWithCurrentLocation:inputSignals:"
+ "setIsAwaitingRetrain:"
+ "shouldKeepCandidateVisit:withValidLoiIdentifiers:"
+ "v48@0:8@16@24d32@40"
+ "v60@0:8@16@24d32@40d48B56"
- "Missing model centroid, assign current location, %{sensitive}@"
- "generateWorkoutPredictionsFromProbabilities:atTime:embeddings:clusters:"

```
