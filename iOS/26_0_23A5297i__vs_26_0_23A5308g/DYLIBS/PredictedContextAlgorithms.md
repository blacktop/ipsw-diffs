## PredictedContextAlgorithms

> `/System/Library/PrivateFrameworks/PredictedContextAlgorithms.framework/PredictedContextAlgorithms`

```diff

-29.0.0.0.0
-  __TEXT.__text: 0x8ad8c
+31.0.0.0.0
+  __TEXT.__text: 0x8c8f0
   __TEXT.__auth_stubs: 0x1090
-  __TEXT.__objc_methlist: 0x6a34
-  __TEXT.__const: 0xbd4
-  __TEXT.__cstring: 0x32db
-  __TEXT.__oslogstring: 0x5d17
+  __TEXT.__objc_methlist: 0x6abc
+  __TEXT.__const: 0xbe4
+  __TEXT.__cstring: 0x3320
+  __TEXT.__oslogstring: 0x6080
   __TEXT.__swift5_typeref: 0x2d0
   __TEXT.__swift5_reflstr: 0x14d
   __TEXT.__swift5_assocty: 0x30

   __TEXT.__swift5_types: 0x20
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x20
-  __TEXT.__gcc_except_tab: 0xe58
+  __TEXT.__gcc_except_tab: 0xed8
   __TEXT.__ustring: 0xbe
-  __TEXT.__unwind_info: 0x18e8
+  __TEXT.__unwind_info: 0x1918
   __TEXT.__eh_frame: 0x600
-  __TEXT.__objc_classname: 0x923
-  __TEXT.__objc_methname: 0xd171
-  __TEXT.__objc_methtype: 0x16e6
-  __TEXT.__objc_stubs: 0x8880
+  __TEXT.__objc_classname: 0x925
+  __TEXT.__objc_methname: 0xd3b0
+  __TEXT.__objc_methtype: 0x173f
+  __TEXT.__objc_stubs: 0x8a20
   __DATA_CONST.__got: 0x688
-  __DATA_CONST.__const: 0xb48
+  __DATA_CONST.__const: 0xb68
   __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e60
+  __DATA_CONST.__objc_selrefs: 0x2ec8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x298
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0x860
-  __AUTH_CONST.__const: 0x810
-  __AUTH_CONST.__cfstring: 0x4200
-  __AUTH_CONST.__objc_const: 0xac28
-  __AUTH_CONST.__objc_doubleobj: 0x190
+  __AUTH_CONST.__const: 0x830
+  __AUTH_CONST.__cfstring: 0x4220
+  __AUTH_CONST.__objc_const: 0xac88
+  __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__objc_intobj: 0xd8
+  __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0xb28
+  __AUTH.__objc_data: 0x858
   __AUTH.__data: 0x1b0
-  __DATA.__objc_ivar: 0x72c
+  __DATA.__objc_ivar: 0x734
   __DATA.__data: 0x258
   __DATA.__bss: 0x4a0
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x1b30
+  __DATA_DIRTY.__objc_data: 0x1e00
   __DATA_DIRTY.__data: 0x4b0
   __DATA_DIRTY.__common: 0x38
   __DATA_DIRTY.__bss: 0x5d0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1E0ADE0E-4EC1-34BE-8FD5-719403FD000F
-  Functions: 2813
-  Symbols:   9094
-  CStrings:  4015
+  UUID: 40BEA900-3C0E-305E-A654-9CC60EF983EC
+  Functions: 2828
+  Symbols:   9142
+  CStrings:  4056
 
Symbols:
+ +[PCEmbedding secondsFromTimeOfDay:toTimeOfDay:]
+ +[PCLocationUtils currentLocationWithLocationHistory:visitHistory:currentTime:]
+ +[PCLocationUtils isLocation:withinThreshold:]
+ +[PCNeuralNetworkUtilities buildMutableArrayCopyOfSwiftBridgedArray:]
+ +[PCNeuralNetworkUtilities calculateVisitValues:endTime:probs:thresholdStartTime:loi:probabilityCalculationMode:probabilityPercentile:startIdx:]
+ +[PCNeuralNetworkUtilities generateClustersAndRemoveBias:calcMode:currentTime:loiIdx:percentile:predSample:predictionArray:timestepSizeMinutes:]
+ +[PCNeuralNetworkUtilities removeBiasFromCluster:percentile:prediction:startIdx:]
+ +[PCNeuralNetworkUtilities removeBiasesWith:loiIdx:mutablePreds:]
+ +[PCScheduledTravelPredictor estimateTravelTimeForCurrentLocation:destination:]
+ +[PCScheduledTravelPredictor predictWithScheduledTravelWithActiveNav:previousNav:visitHistory:locationHistory:atTime:results:]
+ -[PCEmbedding timeOfDay]
+ -[PCWorkoutPredictionAlgorithm _createDateIntervalStartingAt:probability:embeddings:]
+ -[PCWorkoutPredictionAlgorithm _createSourcesFromEmbeddings:]
+ -[PCWorkoutPredictionAlgorithm _subselectEmbeddings:fromCluster:]
+ -[PredictionCluster setVisitEndIdx:]
+ -[PredictionCluster setVisitStartIdx:]
+ -[PredictionCluster visitEndIdx]
+ -[PredictionCluster visitStartIdx]
+ _OBJC_IVAR_$_PredictionCluster._visitEndIdx
+ _OBJC_IVAR_$_PredictionCluster._visitStartIdx
+ ___126+[PCScheduledTravelPredictor predictWithScheduledTravelWithActiveNav:previousNav:visitHistory:locationHistory:atTime:results:]_block_invoke
+ ___126+[PCScheduledTravelPredictor predictWithScheduledTravelWithActiveNav:previousNav:visitHistory:locationHistory:atTime:results:]_block_invoke_2
+ ___126+[PCScheduledTravelPredictor predictWithScheduledTravelWithActiveNav:previousNav:visitHistory:locationHistory:atTime:results:]_block_invoke_3
+ ___126+[PCScheduledTravelPredictor predictWithScheduledTravelWithActiveNav:previousNav:visitHistory:locationHistory:atTime:results:]_block_invoke_4
+ ___79+[PCLocationUtils currentLocationWithLocationHistory:visitHistory:currentTime:]_block_invoke
+ ___85-[PCWorkoutPredictionAlgorithm _createDateIntervalStartingAt:probability:embeddings:]_block_invoke
+ ___block_descriptor_32_e37_q24?0"PCEmbedding"8"PCEmbedding"16l
+ ___block_literal_global.12
+ ___block_literal_global.15
+ ___block_literal_global.197
+ ___block_literal_global.9
+ _objc_msgSend$_createDateIntervalStartingAt:probability:embeddings:
+ _objc_msgSend$_createSourcesFromEmbeddings:
+ _objc_msgSend$_subselectEmbeddings:fromCluster:
+ _objc_msgSend$buildMutableArrayCopyOfSwiftBridgedArray:
+ _objc_msgSend$calculateVisitValues:endTime:probs:thresholdStartTime:loi:probabilityCalculationMode:probabilityPercentile:startIdx:
+ _objc_msgSend$currentLocationWithLocationHistory:visitHistory:currentTime:
+ _objc_msgSend$estimateTravelTimeForCurrentLocation:destination:
+ _objc_msgSend$generateClustersAndRemoveBias:calcMode:currentTime:loiIdx:percentile:predSample:predictionArray:timestepSizeMinutes:
+ _objc_msgSend$predictWithScheduledTravelWithActiveNav:previousNav:visitHistory:locationHistory:atTime:results:
+ _objc_msgSend$removeBiasFromCluster:percentile:prediction:startIdx:
+ _objc_msgSend$removeBiasesWith:loiIdx:mutablePreds:
+ _objc_msgSend$second
+ _objc_msgSend$secondsFromTimeOfDay:toTimeOfDay:
+ _objc_msgSend$setVisitEndIdx:
+ _objc_msgSend$setVisitStartIdx:
+ _objc_msgSend$timeOfDay
+ _objc_msgSend$visitEndIdx
+ _objc_msgSend$visitStartIdx
- +[PCMapsViewedPlacesPredictor isLocation:withinThreshold:]
- +[PCNeuralNetworkUtilities calculateVisitValues:endTime:probs:thresholdStartTime:loi:probabilityCalculationMode:probabilityPercentile:]
- +[PCScheduledTravelPredictor estimateTravelTimeForOrigin:destination:]
- +[PCScheduledTravelPredictor isLocation:withinThreshold:]
- +[PCScheduledTravelPredictor predictWithScheduledTravelWithActiveNav:previousNav:history:atTime:results:]
- -[PCWorkoutPredictionAlgorithm _createDateIntervalStartingAt:]
- -[PCWorkoutPredictionAlgorithm _createSourcesFromCluster:embeddings:]
- ___105+[PCScheduledTravelPredictor predictWithScheduledTravelWithActiveNav:previousNav:history:atTime:results:]_block_invoke
- ___105+[PCScheduledTravelPredictor predictWithScheduledTravelWithActiveNav:previousNav:history:atTime:results:]_block_invoke_2
- ___105+[PCScheduledTravelPredictor predictWithScheduledTravelWithActiveNav:previousNav:history:atTime:results:]_block_invoke_3
- ___105+[PCScheduledTravelPredictor predictWithScheduledTravelWithActiveNav:previousNav:history:atTime:results:]_block_invoke_4
- ___block_literal_global.183
- _objc_msgSend$_createDateIntervalStartingAt:
- _objc_msgSend$_createSourcesFromCluster:embeddings:
- _objc_msgSend$calculateVisitValues:endTime:probs:thresholdStartTime:loi:probabilityCalculationMode:probabilityPercentile:
- _objc_msgSend$estimateTravelTimeForOrigin:destination:
- _objc_msgSend$predictWithScheduledTravelWithActiveNav:previousNav:history:atTime:results:
CStrings:
+ "!"
+ "%@"
+ "%@ - no valid location found from visit or location history"
+ "%s, current location is unknown!, use origin location as a fallback"
+ "+[PCScheduledTravelPredictor predictWithScheduledTravelWithActiveNav:previousNav:visitHistory:locationHistory:atTime:results:]"
+ "@40@0:8@16d24@32"
+ "@40@0:8@16f24@28i36"
+ "@60@0:8d16f24@28f36i40q44f52i56"
+ "@68@0:8f16q20d28i36f40@44@52d60"
+ "@min.self"
+ "Scheduling: High-probability prediction, but no embeddings found in prediction period (startTime=%{public}.1f)"
+ "Scheduling: Updated high-confidence prediction. currentStartTime=%{public}.1f,updatedStartTime=%{public}.1f,secondsUntilWorkout=%{public}.1f"
+ "Ti,V_visitEndIdx"
+ "Ti,V_visitStartIdx"
+ "[%@] current location from active visit, lat: %{sensitive}.5f, lon: %{sensitive}.5f, current time: %f"
+ "[%@] current location from location history, lat: %{sensitive}.5f, lon: %{sensitive}.5f, current time: %f"
+ "[secondsFromTimeOfDay] Invalid Parameters: %@, %@"
+ "_createDateIntervalStartingAt:probability:embeddings:"
+ "_createSourcesFromEmbeddings:"
+ "_subselectEmbeddings:fromCluster:"
+ "_visitEndIdx"
+ "_visitStartIdx"
+ "bias detected in cluster, rerunning clustering with bias removed"
+ "bias diff from max probability: %f"
+ "bias in cluster: %@"
+ "biases"
+ "buildMutableArrayCopyOfSwiftBridgedArray:"
+ "calculateVisitValues:endTime:probs:thresholdStartTime:loi:probabilityCalculationMode:probabilityPercentile:startIdx:"
+ "currentLocationWithLocationHistory:visitHistory:currentTime:"
+ "estimateTravelTimeForCurrentLocation:destination:"
+ "generateClustersAndRemoveBias:calcMode:currentTime:loiIdx:percentile:predSample:predictionArray:timestepSizeMinutes:"
+ "pred probs:"
+ "predictWithScheduledTravelWithActiveNav:previousNav:visitHistory:locationHistory:atTime:results:"
+ "prediction probabilities after restoration"
+ "q24@?0@\"PCEmbedding\"8@\"PCEmbedding\"16"
+ "removeBiasFromCluster:percentile:prediction:startIdx:"
+ "removeBiasesWith:loiIdx:mutablePreds:"
+ "restoring biases from index %d to %d"
+ "second"
+ "secondsFromTimeOfDay:toTimeOfDay:"
+ "setVisitEndIdx:"
+ "setVisitStartIdx:"
+ "subarray: %@"
+ "timeOfDay"
+ "v36@0:8@16i24@28"
+ "visitEndIdx"
+ "visitStartIdx"
- "+[PCScheduledTravelPredictor predictWithScheduledTravelWithActiveNav:previousNav:history:atTime:results:]"
- "@56@0:8d16f24@28f36i40q44f52"
- "_createDateIntervalStartingAt:"
- "_createSourcesFromCluster:embeddings:"
- "calculateVisitValues:endTime:probs:thresholdStartTime:loi:probabilityCalculationMode:probabilityPercentile:"
- "estimateTravelTimeForOrigin:destination:"
- "predictWithScheduledTravelWithActiveNav:previousNav:history:atTime:results:"

```
