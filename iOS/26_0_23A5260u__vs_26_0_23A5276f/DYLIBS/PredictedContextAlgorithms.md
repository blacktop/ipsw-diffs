## PredictedContextAlgorithms

> `/System/Library/PrivateFrameworks/PredictedContextAlgorithms.framework/PredictedContextAlgorithms`

```diff

-24.0.0.0.0
-  __TEXT.__text: 0x88e24
-  __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_methlist: 0x6724
-  __TEXT.__const: 0xa64
-  __TEXT.__cstring: 0x30e6
-  __TEXT.__oslogstring: 0x58f1
-  __TEXT.__swift5_typeref: 0x320
-  __TEXT.__constg_swiftt: 0x454
-  __TEXT.__swift5_reflstr: 0x114
-  __TEXT.__swift5_fieldmd: 0x238
-  __TEXT.__swift5_capture: 0xa4
-  __TEXT.__swift5_proto: 0x3c
-  __TEXT.__swift5_types: 0x1c
+26.0.0.0.0
+  __TEXT.__text: 0x89d8c
+  __TEXT.__auth_stubs: 0x1070
+  __TEXT.__objc_methlist: 0x68fc
+  __TEXT.__const: 0xb64
+  __TEXT.__cstring: 0x31b2
+  __TEXT.__oslogstring: 0x58a9
+  __TEXT.__swift5_typeref: 0x2d0
+  __TEXT.__swift5_reflstr: 0x14d
+  __TEXT.__swift5_assocty: 0x30
+  __TEXT.__constg_swiftt: 0x4a0
+  __TEXT.__swift5_fieldmd: 0x250
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_capture: 0x90
+  __TEXT.__swift5_proto: 0x4c
+  __TEXT.__swift5_types: 0x20
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x20
-  __TEXT.__gcc_except_tab: 0xd88
+  __TEXT.__gcc_except_tab: 0xe08
   __TEXT.__ustring: 0xbe
-  __TEXT.__unwind_info: 0x1840
+  __TEXT.__unwind_info: 0x18b0
   __TEXT.__eh_frame: 0x5d8
-  __TEXT.__objc_classname: 0x905
-  __TEXT.__objc_methname: 0xc8af
-  __TEXT.__objc_methtype: 0x1649
-  __TEXT.__objc_stubs: 0x8420
-  __DATA_CONST.__got: 0x6b0
-  __DATA_CONST.__const: 0xb00
-  __DATA_CONST.__objc_classlist: 0x368
+  __TEXT.__objc_classname: 0x921
+  __TEXT.__objc_methname: 0xce1b
+  __TEXT.__objc_methtype: 0x16b1
+  __TEXT.__objc_stubs: 0x8620
+  __DATA_CONST.__got: 0x688
+  __DATA_CONST.__const: 0xb20
+  __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2cc8
+  __DATA_CONST.__objc_selrefs: 0x2dc0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x290
+  __DATA_CONST.__objc_superrefs: 0x298
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x880
-  __AUTH_CONST.__const: 0x720
-  __AUTH_CONST.__cfstring: 0x4000
-  __AUTH_CONST.__objc_const: 0xa730
+  __AUTH_CONST.__auth_got: 0x850
+  __AUTH_CONST.__const: 0x7c8
+  __AUTH_CONST.__cfstring: 0x40c0
+  __AUTH_CONST.__objc_const: 0xaa48
   __AUTH_CONST.__objc_doubleobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH.__objc_data: 0xa98
+  __AUTH.__objc_data: 0xb28
   __AUTH.__data: 0x1b0
-  __DATA.__objc_ivar: 0x6dc
-  __DATA.__data: 0x260
-  __DATA.__bss: 0x2a0
+  __DATA.__objc_ivar: 0x708
+  __DATA.__data: 0x258
+  __DATA.__bss: 0x4a0
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1b30
-  __DATA_DIRTY.__data: 0x4e8
+  __DATA_DIRTY.__data: 0x4b0
   __DATA_DIRTY.__common: 0x38
   __DATA_DIRTY.__bss: 0x5c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7A3DDA2F-22C5-3D6F-9015-3C29FD1116EA
-  Functions: 2714
-  Symbols:   8825
-  CStrings:  3884
+  UUID: 644B9671-9AAC-31CA-AC1A-95462FA92D15
+  Functions: 2783
+  Symbols:   9002
+  CStrings:  3957
 
Symbols:
+ +[PCEmbeddingDistanceCalculator calculateValidMean:]
+ -[PCAlgorithms currentComputeDate]
+ -[PCAlgorithms interruptComputeWithError:]
+ -[PCAlgorithms lastComputeDate]
+ -[PCAlgorithms setCurrentComputeDate:]
+ -[PCAlgorithms setLastComputeDate:]
+ -[PCPComputeInterruptRequest copyTo:]
+ -[PCPComputeInterruptRequest copyWithZone:]
+ -[PCPComputeInterruptRequest description]
+ -[PCPComputeInterruptRequest dictionaryRepresentation]
+ -[PCPComputeInterruptRequest hash]
+ -[PCPComputeInterruptRequest isEqual:]
+ -[PCPComputeInterruptRequest mergeFrom:]
+ -[PCPComputeInterruptRequest readFrom:]
+ -[PCPComputeInterruptRequest writeTo:]
+ -[PCPComputeRequest StringAsCompletionStatus:]
+ -[PCPComputeRequest completionStatusAsString:]
+ -[PCPComputeRequest completionStatus]
+ -[PCPComputeRequest hasCompletionStatus]
+ -[PCPComputeRequest hasReceivedInterruptRequest]
+ -[PCPComputeRequest receivedInterruptRequest]
+ -[PCPComputeRequest setCompletionStatus:]
+ -[PCPComputeRequest setHasCompletionStatus:]
+ -[PCPComputeRequest setHasReceivedInterruptRequest:]
+ -[PCPComputeRequest setReceivedInterruptRequest:]
+ -[PCPInteractionRecord hasInterruptRequest]
+ -[PCPInteractionRecord interruptRequest]
+ -[PCPInteractionRecord setInterruptRequest:]
+ -[PCVisitHistoryPredictor candidateLoiToHomeMap]
+ -[PCVisitHistoryPredictor candidateLoiToLocationMap]
+ -[PCVisitHistoryPredictor candidateLoiToWorkMap]
+ -[PCVisitHistoryPredictor candidateModel]
+ -[PCVisitHistoryPredictor candidateVisitIndicies]
+ -[PCVisitHistoryPredictor computeWithHistory:transitions:locationsOfInterest:homekitHomes:atTime:withError:]
+ -[PCVisitHistoryPredictor interruptTraining]
+ -[PCVisitHistoryPredictor setCandidateLoiToHomeMap:]
+ -[PCVisitHistoryPredictor setCandidateLoiToLocationMap:]
+ -[PCVisitHistoryPredictor setCandidateLoiToWorkMap:]
+ -[PCVisitHistoryPredictor setCandidateModel:]
+ -[PCVisitHistoryPredictor setCandidateVisitIndicies:]
+ -[PCVisitHistoryPredictor storeHomeLoisTo:workLoisTo:from:withVisitIndices:]
+ -[PCWorkoutPredictionAlgorithm calculateScoreFromFeatures:identifier:]
+ OBJC_IVAR_$_PCPComputeRequest._completionStatus
+ OBJC_IVAR_$_PCPComputeRequest._has
+ OBJC_IVAR_$_PCPComputeRequest._receivedInterruptRequest
+ OBJC_IVAR_$_PCPInteractionRecord._interruptRequest
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC10CodingKeys33_5E3324A45488CAD9EFDF1E72CC9262A7LLO8rawValueAFSgSS_tcfCTf4nd_n
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC10CodingKeys33_5E3324A45488CAD9EFDF1E72CC9262A7LLO8rawValueAFSgSS_tcfCTv_r
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC10CodingKeys33_5E3324A45488CAD9EFDF1E72CC9262A7LLOSYAAMA
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC10CodingKeys33_5E3324A45488CAD9EFDF1E72CC9262A7LLOSYAAMc
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC10CodingKeys33_5E3324A45488CAD9EFDF1E72CC9262A7LLOSYAAMcMK
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC10CodingKeys33_5E3324A45488CAD9EFDF1E72CC9262A7LLOSYAASY8rawValue03RawQ0QzvgTW
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC10CodingKeys33_5E3324A45488CAD9EFDF1E72CC9262A7LLOSYAASY8rawValuexSg03RawQ0Qz_tcfCTW
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC16trainFromTensors8datasetX0J1Y9timestepsAA0aB18TrainingResultCodeOSaySaySfGG_AJSitF
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC16trainFromTensors8datasetX0J1Y9timestepsAA0aB18TrainingResultCodeOSaySaySfGG_AJSitF14NeuralNetworks10SequentialVyANyANyANyAL6Conv1DVAL4ReLUVGAL7FlattenVGAL5DenseVGAL7ReshapeVGyXEfU_
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC16trainFromTensors8datasetX0J1Y9timestepsAA0aB18TrainingResultCodeOSaySaySfGG_AJSitF14NeuralNetworks10SequentialVyANyANyANyAL6Conv1DVAL4ReLUVGAL7FlattenVGAL5DenseVGAL7ReshapeVGyXEfU_TA
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC16trainFromTensors8datasetX0J1Y9timestepsAA0aB18TrainingResultCodeOSaySaySfGG_AJSitF14NeuralNetworks6TensorVAL10SequentialVyAPyAPyAPyAL6Conv1DVAL4ReLUVGAL7FlattenVGAL5DenseVGAL7ReshapeVGXEfU0_
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC16trainFromTensors8datasetX0J1Y9timestepsAA0aB18TrainingResultCodeOSaySaySfGG_AJSitF14NeuralNetworks6TensorVAL10SequentialVyAPyAPyAPyAL6Conv1DVAL4ReLUVGAL7FlattenVGAL5DenseVGAL7ReshapeVGXEfU0_TA
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC16trainFromTensors8datasetX0J1Y9timestepsAA0aB18TrainingResultCodeOSaySaySfGG_AJSitFTj
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC16trainFromTensors8datasetX0J1Y9timestepsAA0aB18TrainingResultCodeOSaySaySfGG_AJSitFTo
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC16trainFromTensors8datasetX0J1Y9timestepsAA0aB18TrainingResultCodeOSaySaySfGG_AJSitFTq
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC16trainFromTensors8datasetX0J1Y9timestepsAA0aB18TrainingResultCodeOSaySaySfGG_AJSitFTv0_r
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC16trainFromTensors8datasetX0J1Y9timestepsAA0aB18TrainingResultCodeOSaySaySfGG_AJSitFTv_r
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC17interruptTrainingyyF
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC17interruptTrainingyyFTj
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC17interruptTrainingyyFTm
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC17interruptTrainingyyFTo
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC17interruptTrainingyyFTq
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC17predictFromTensor8xPredict01xJ6Matrix9timestepsSaySaySaySfGGGAJ_AISitFTf4dnnn_n
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC18predictFromDataset33_5E3324A45488CAD9EFDF1E72CC9262A7LL13featureMatrixSay14NeuralNetworks6TensorVGAA014DataSetFeatureR0C_tF
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC18predictFromDataset33_5E3324A45488CAD9EFDF1E72CC9262A7LL13featureMatrixSay14NeuralNetworks6TensorVGAA014DataSetFeatureR0C_tFTv0_r
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC18predictFromDataset33_5E3324A45488CAD9EFDF1E72CC9262A7LL13featureMatrixSay14NeuralNetworks6TensorVGAA014DataSetFeatureR0C_tFTv_r
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC22clearTrainingInterrupt33_5E3324A45488CAD9EFDF1E72CC9262A7LLyyF
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC23shouldInterruptTrainingSbvM
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC23shouldInterruptTrainingSbvM.resume.0
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC23shouldInterruptTrainingSbvMTj
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC23shouldInterruptTrainingSbvMTq
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC23shouldInterruptTrainingSbvg
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC23shouldInterruptTrainingSbvgTj
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC23shouldInterruptTrainingSbvgTq
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC23shouldInterruptTrainingSbvpACTK
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC23shouldInterruptTrainingSbvpACTk
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC23shouldInterruptTrainingSbvpMV
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC23shouldInterruptTrainingSbvpWvd
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC23shouldInterruptTrainingSbvs
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC23shouldInterruptTrainingSbvsTj
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC23shouldInterruptTrainingSbvsTq
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC4lockSo6NSLockCvM
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC4lockSo6NSLockCvM.resume.0
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC4lockSo6NSLockCvMTj
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC4lockSo6NSLockCvMTq
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC4lockSo6NSLockCvg
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC4lockSo6NSLockCvgTj
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC4lockSo6NSLockCvgTq
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC4lockSo6NSLockCvpACTK
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC4lockSo6NSLockCvpACTk
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC4lockSo6NSLockCvpMV
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC4lockSo6NSLockCvpWvd
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC4lockSo6NSLockCvs
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC4lockSo6NSLockCvsTj
+ _$s28PCNeuralNetworkSupportBridge0A8NetModelC4lockSo6NSLockCvsTq
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeO8rawValueACSgSi_tcfC
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeO8rawValueSivg
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeO8rawValueSivpMV
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeOACSQAAWL
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeOACSQAAWl
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeOMB
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeOMa
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeOMf
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeOMn
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeON
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeOSHAAMc
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeOSHAAMcMK
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeOSHAASH13_rawHashValue4seedS2i_tFTW
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeOSHAASH4hash4intoys6HasherVz_tFTW
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeOSHAASH9hashValueSivgTW
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeOSHAASQWb
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeOSQAAMc
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeOSQAAMcMK
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeOSQAASQ2eeoiySbx_xtFZTW
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeOSYAAMA
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeOSYAAMc
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeOSYAAMcMK
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeOSYAASY8rawValue03RawI0QzvgTW
+ _$s28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeOSYAASY8rawValuexSg03RawI0Qz_tcfCTW
+ _$s8RawValueSYTl
+ _$sIeAgH_ytIeAgHr_TRTA.83
+ _$sIeAgH_ytIeAgHr_TRTA.83TQ0_
+ _$sIeAgH_ytIeAgHr_TRTA.83Tu
+ _$sIeghH_IeAgH_TRTA.78
+ _$sIeghH_IeAgH_TRTA.78TQ0_
+ _$sIeghH_IeAgH_TRTA.78Tu
+ _$sSY8rawValue03RawB0QzvgTq
+ _$sSY8rawValuexSg03RawB0Qz_tcfCTq
+ _$sSYMp
+ _$sSYsSHRzSH8RawValueSYRpzrlE04hashB0Sivg28PCNeuralNetworkSupportBridge0D8NetModelC10CodingKeys33_5E3324A45488CAD9EFDF1E72CC9262A7LLO_Tg5
+ _$sSYsSHRzSH8RawValueSYRpzrlE08_rawHashB04seedS2i_tF28PCNeuralNetworkSupportBridge0F8NetModelC10CodingKeys33_5E3324A45488CAD9EFDF1E72CC9262A7LLO_Tg5
+ _$ss21_findStringSwitchCase5cases6stringSiSays06StaticB0VG_SStF
+ _$ss2eeoiySbx_xtSYRzSQ8RawValueRpzlF28PCNeuralNetworkSupportBridge0D8NetModelC10CodingKeys33_5E3324A45488CAD9EFDF1E72CC9262A7LLO_Tg5
+ _OBJC_CLASS_$_NSLock
+ _OBJC_CLASS_$_PCPComputeInterruptRequest
+ _OBJC_IVAR_$_PCAlgorithms._currentComputeDate
+ _OBJC_IVAR_$_PCAlgorithms._lastComputeDate
+ _OBJC_IVAR_$_PCVisitHistoryPredictor._candidateLoiToHomeMap
+ _OBJC_IVAR_$_PCVisitHistoryPredictor._candidateLoiToLocationMap
+ _OBJC_IVAR_$_PCVisitHistoryPredictor._candidateLoiToWorkMap
+ _OBJC_IVAR_$_PCVisitHistoryPredictor._candidateModel
+ _OBJC_IVAR_$_PCVisitHistoryPredictor._candidateVisitIndicies
+ _OBJC_METACLASS_$_PCPComputeInterruptRequest
+ _PCPComputeInterruptRequestReadFrom
+ __OBJC_$_INSTANCE_METHODS_PCPComputeInterruptRequest
+ __OBJC_CLASS_PROTOCOLS_$_PCPComputeInterruptRequest
+ __OBJC_CLASS_RO_$_PCPComputeInterruptRequest
+ __OBJC_METACLASS_RO_$_PCPComputeInterruptRequest
+ ___108-[PCVisitHistoryPredictor computeWithHistory:transitions:locationsOfInterest:homekitHomes:atTime:withError:]_block_invoke
+ _associated conformance 28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeOSHAASQ
+ _objc_msgSend$calculateScoreFromFeatures:identifier:
+ _objc_msgSend$calculateValidMean:
+ _objc_msgSend$candidateLoiToHomeMap
+ _objc_msgSend$candidateLoiToLocationMap
+ _objc_msgSend$candidateLoiToWorkMap
+ _objc_msgSend$candidateModel
+ _objc_msgSend$candidateVisitIndicies
+ _objc_msgSend$computeWithHistory:transitions:locationsOfInterest:homekitHomes:atTime:withError:
+ _objc_msgSend$currentComputeDate
+ _objc_msgSend$interruptTraining
+ _objc_msgSend$lastComputeDate
+ _objc_msgSend$setCandidateLoiToHomeMap:
+ _objc_msgSend$setCandidateLoiToLocationMap:
+ _objc_msgSend$setCandidateLoiToWorkMap:
+ _objc_msgSend$setCandidateModel:
+ _objc_msgSend$setCandidateVisitIndicies:
+ _objc_msgSend$setCurrentComputeDate:
+ _objc_msgSend$setInterruptRequest:
+ _objc_msgSend$setLastComputeDate:
+ _objc_msgSend$storeHomeLoisTo:workLoisTo:from:withVisitIndices:
+ _objectdestroy.56Tm
+ _symbolic $sSY
+ _symbolic SS
+ _symbolic So6NSLockC
+ _symbolic _____ 28PCNeuralNetworkSupportBridge0aB18TrainingResultCodeO
- -[PCVisitHistoryPredictor computeWithHistory:transitions:locationsOfInterest:homekitHomes:atTime:]
- -[PCVisitHistoryPredictor storeHomeLoisTo:workLoisTo:from:]
- -[PCWorkoutPredictionAlgorithm _calculateMeanProbabilities:]
- -[PCWorkoutPredictionAlgorithm calculateScoreFromFeatures:]
- _$s14NeuralNetworks10DataSampleV8features6labelsACyxq_Gx_q_tcfC
- _$s14NeuralNetworks10DataSampleVMn
- _$s14NeuralNetworks10DataSampleVyAA6TensorVAEGACyxq_GAA0cD8ProtocolAAWL
- _$s14NeuralNetworks10DataSampleVyAA6TensorVAEGACyxq_GAA10CollatableA2aHRzAaHR_rlWL
- _$s14NeuralNetworks10DataSampleVyAA6TensorVAEGACyxq_GAA10CollatableA2aHRzAaHR_rlWl
- _$s14NeuralNetworks10DataSampleVyAA6TensorVAEGMD
- _$s14NeuralNetworks10DataSampleVyxq_GAA0cD8ProtocolAAMc
- _$s14NeuralNetworks10DataSampleVyxq_GAA10CollatableA2aERzAaER_rlMc
- _$s14NeuralNetworks10ScalarTypeO7float32yA2CmFWC
- _$s14NeuralNetworks17SequentialSamplerCAA0D0AAWP
- _$s14NeuralNetworks17SequentialSamplerCACycfc
- _$s14NeuralNetworks17SequentialSamplerCMa
- _$s14NeuralNetworks6TensorV4ones10scalarType2onAcA0C5ShapeV_AA06ScalarF0OAA13ComputeDeviceVSgtcfC
- _$s14NeuralNetworks6TensorV8stacking9alongAxis10scalarTypeACSayACG_SiAA06ScalarH0OSgtcfC
- _$s14NeuralNetworks6TensorVAA10CollatableAAWP
- _$s14NeuralNetworks6TensorV_2onACSi_AA13ComputeDeviceVSgtcfC
- _$s14NeuralNetworks7DatasetV12PrefetchModeO6serialyAEyxq__GAGmSTRzAA10CollatableR_AA18DataSampleProtocolR_r0_lFWC
- _$s14NeuralNetworks7DatasetV12PrefetchModeOMn
- _$s14NeuralNetworks7DatasetV12PrefetchModeOySaySaySaySfGGGAA10DataSampleVyAA6TensorVALG_GMD
- _$s14NeuralNetworks7DatasetV7samples9batchSize0E7Sampler21dropsLastPartialBatch12prefetchMode9transformACyxq_Gx_SiAA0G0_pSgSbAC08PrefetchM0Oyxq__Gq_7ElementQzctcfC
- _$s14NeuralNetworks7DatasetVMn
- _$s14NeuralNetworks7DatasetVySaySaySaySfGGGAA10DataSampleVyAA6TensorVAJGGMD
- _$s28PCNeuralNetworkSupportBridge0A8NetModelC10CodingKeys33_5E3324A45488CAD9EFDF1E72CC9262A7LLO11stringValueAFSgSS_tcfCTf4nd_n
- _$s28PCNeuralNetworkSupportBridge0A8NetModelC16trainFromTensors8datasetX0J1Y9timestepsySaySaySfGG_AHSitF
- _$s28PCNeuralNetworkSupportBridge0A8NetModelC16trainFromTensors8datasetX0J1Y9timestepsySaySaySfGG_AHSitF14NeuralNetworks10SequentialVyALyALyALyAJ6Conv1DVAJ4ReLUVGAJ7FlattenVGAJ5DenseVGAJ7ReshapeVGyXEfU_
- _$s28PCNeuralNetworkSupportBridge0A8NetModelC16trainFromTensors8datasetX0J1Y9timestepsySaySaySfGG_AHSitF14NeuralNetworks10SequentialVyALyALyALyAJ6Conv1DVAJ4ReLUVGAJ7FlattenVGAJ5DenseVGAJ7ReshapeVGyXEfU_TA
- _$s28PCNeuralNetworkSupportBridge0A8NetModelC16trainFromTensors8datasetX0J1Y9timestepsySaySaySfGG_AHSitF14NeuralNetworks6TensorVAJ10SequentialVyANyANyANyAJ6Conv1DVAJ4ReLUVGAJ7FlattenVGAJ5DenseVGAJ7ReshapeVGXEfU0_
- _$s28PCNeuralNetworkSupportBridge0A8NetModelC16trainFromTensors8datasetX0J1Y9timestepsySaySaySfGG_AHSitF14NeuralNetworks6TensorVAJ10SequentialVyANyANyANyAJ6Conv1DVAJ4ReLUVGAJ7FlattenVGAJ5DenseVGAJ7ReshapeVGXEfU0_TA
- _$s28PCNeuralNetworkSupportBridge0A8NetModelC16trainFromTensors8datasetX0J1Y9timestepsySaySaySfGG_AHSitFTj
- _$s28PCNeuralNetworkSupportBridge0A8NetModelC16trainFromTensors8datasetX0J1Y9timestepsySaySaySfGG_AHSitFTo
- _$s28PCNeuralNetworkSupportBridge0A8NetModelC16trainFromTensors8datasetX0J1Y9timestepsySaySaySfGG_AHSitFTq
- _$s28PCNeuralNetworkSupportBridge0A8NetModelC16trainFromTensors8datasetX0J1Y9timestepsySaySaySfGG_AHSitFTv0_r
- _$s28PCNeuralNetworkSupportBridge0A8NetModelC16trainFromTensors8datasetX0J1Y9timestepsySaySaySfGG_AHSitFTv_r
- _$s28PCNeuralNetworkSupportBridge0A8NetModelC18predictFromDataset33_5E3324A45488CAD9EFDF1E72CC9262A7LL7dataset13featureMatrixSay14NeuralNetworks6TensorVGAH0I0VySaySaySaySfGGGAH10DataSampleVyA2JGG_AA0w10SetFeatureS0CtF
- _$s28PCNeuralNetworkSupportBridge0A8NetModelC18predictFromDataset33_5E3324A45488CAD9EFDF1E72CC9262A7LL7dataset13featureMatrixSay14NeuralNetworks6TensorVGAH0I0VySaySaySaySfGGGAH10DataSampleVyA2JGG_AA0w10SetFeatureS0CtFTv0_r
- _$s28PCNeuralNetworkSupportBridge0A8NetModelC18predictFromDataset33_5E3324A45488CAD9EFDF1E72CC9262A7LL7dataset13featureMatrixSay14NeuralNetworks6TensorVGAH0I0VySaySaySaySfGGGAH10DataSampleVyA2JGG_AA0w10SetFeatureS0CtFTv_r
- _$s28PCNeuralNetworkSupportBridge0A8NetModelC21predDatasetFromTensor33_5E3324A45488CAD9EFDF1E72CC9262A7LL6tensor14NeuralNetworks0H0VySaySaySaySfGGGAG10DataSampleVyAG0J0VAPGGAL_tF
- _$s28PCNeuralNetworkSupportBridge0A8NetModelC21predDatasetFromTensor33_5E3324A45488CAD9EFDF1E72CC9262A7LL6tensor14NeuralNetworks0H0VySaySaySaySfGGGAG10DataSampleVyAG0J0VAPGGAL_tFAqKcfU_
- _$s28PCNeuralNetworkSupportBridge0A8NetModelC21predDatasetFromTensor33_5E3324A45488CAD9EFDF1E72CC9262A7LL6tensor14NeuralNetworks0H0VySaySaySaySfGGGAG10DataSampleVyAG0J0VAPGGAL_tFAqKcfU_TA
- _$s28PCNeuralNetworkSupportBridge15NeuralNetConfigC10CodingKeys33_5E3324A45488CAD9EFDF1E72CC9262A7LLOSHAASH13_rawHashValue4seedS2i_tFTWTm
- _$s28PCNeuralNetworkSupportBridge15NeuralNetConfigC10CodingKeys33_5E3324A45488CAD9EFDF1E72CC9262A7LLOSHAASH9hashValueSivgTWTm
- _$sIeAgH_ytIeAgHr_TRTA.82
- _$sIeAgH_ytIeAgHr_TRTA.82TQ0_
- _$sIeAgH_ytIeAgHr_TRTA.82Tu
- _$sIeghH_IeAgH_TRTA.77
- _$sIeghH_IeAgH_TRTA.77TQ0_
- _$sIeghH_IeAgH_TRTA.77Tu
- _$sSaySaySaySfGGGMD
- _$sSaySaySaySfGGGSayxGSTsWL
- _$ss10ArraySliceVMn
- _$ss10ArraySliceVySfGAByxGSlsWL
- _$ss10ArraySliceVySfGMD
- _$ss10ArraySliceVyxGSlsMc
- ___98-[PCVisitHistoryPredictor computeWithHistory:transitions:locationsOfInterest:homekitHomes:atTime:]_block_invoke
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_PCNeuralNetworkSupportBridge
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_PCNeuralNetworkSupportBridge
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_PCNeuralNetworkSupportBridge
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_PCNeuralNetworkSupportBridge
- _objc_msgSend$_calculateMeanProbabilities:
- _objc_msgSend$calculateScoreFromFeatures:
- _objc_msgSend$computeWithHistory:transitions:locationsOfInterest:homekitHomes:atTime:
- _objc_msgSend$storeHomeLoisTo:workLoisTo:from:
- _objectdestroy.55Tm
- _symbolic SaySaySaySfGGG
- _symbolic _____ySaySaySaySfGGG_____y_____AFGG 14NeuralNetworks7DatasetV AA10DataSampleV AA6TensorV
- _symbolic _____ySaySaySaySfGGG_____y_____AFG_G 14NeuralNetworks7DatasetV12PrefetchModeO AA10DataSampleV AA6TensorV
- _symbolic _____ySfG s10ArraySliceV
- _symbolic _____y_____ABG 14NeuralNetworks10DataSampleV AA6TensorV
CStrings:
+ "\v"
+ "#warning: found invalid value in array (%.3f)"
+ "@\"NSNumber\""
+ "@\"PCPComputeInterruptRequest\""
+ "B24@0:8^@16"
+ "Cluster %@ (%@), mapped probability,%.4f, location,%@"
+ "Cluster %@: Could not compute mean probability (numWorkouts=%lu)"
+ "Cluster %@: workoutType=%@, meanProbability=%.3f, meanScore=%.3f, numWorkouts=%lu"
+ "InterruptRequest"
+ "Interrupted"
+ "Interrupting training"
+ "LastTrainingDateCFAbsTime"
+ "LogisticRegression,%@,output,%.3f,logit,%.3f,FeaturesRawAndWeighted,combinedPlaceType,%.3f,%.3f,placeName,%.3f,%.3f,geographicalProximity,%.3f,%.3f,timeOfDay,%.3f,%.3f,dayOfWeek,%.3f,%.3f,isWeekend,%.3f,%.3f,timeOfDayCircularStd,%.3f,%.3f,latLongCircularStd,%.3f,%.3f"
+ "PCPComputeInterruptRequest"
+ "StringAsCompletionStatus:"
+ "T@\"NSMutableDictionary\",&,N,V_candidateLoiToHomeMap"
+ "T@\"NSMutableDictionary\",&,N,V_candidateLoiToLocationMap"
+ "T@\"NSMutableDictionary\",&,N,V_candidateLoiToWorkMap"
+ "T@\"NSMutableDictionary\",&,N,V_candidateVisitIndicies"
+ "T@\"NSNumber\",&,V_currentComputeDate"
+ "T@\"NSNumber\",&,V_lastComputeDate"
+ "T@\"PCPComputeInterruptRequest\",&,N,V_interruptRequest"
+ "T@\"_TtC28PCNeuralNetworkSupportBridge16PCNeuralNetModel\",&,N,V_candidateModel"
+ "TB,N,V_receivedInterruptRequest"
+ "Ti,N,V_completionStatus"
+ "_candidateLoiToHomeMap"
+ "_candidateLoiToLocationMap"
+ "_candidateLoiToWorkMap"
+ "_candidateModel"
+ "_candidateVisitIndicies"
+ "_completionStatus"
+ "_currentComputeDate"
+ "_interruptRequest"
+ "_lastComputeDate"
+ "_receivedInterruptRequest"
+ "age of model is greater than %d days, deferral will not be honored"
+ "applyAlgorithmState: decodeDoubleForKey:kLastTrainingDateCFAbsTime failed with exception %@"
+ "calculateScoreFromFeatures:identifier:"
+ "calculateValidMean:"
+ "candidateLoiToHomeMap"
+ "candidateLoiToLocationMap"
+ "candidateLoiToWorkMap"
+ "candidateModel"
+ "candidateVisitIndicies"
+ "clearing training interrupt flag"
+ "completionStatus"
+ "completionStatusAsString:"
+ "computeWithHistory:transitions:locationsOfInterest:homekitHomes:atTime:withError:"
+ "currentComputeDate"
+ "deferral request ignored due to model age"
+ "hasCompletionStatus"
+ "hasInterruptRequest"
+ "hasReceivedInterruptRequest"
+ "interrupt training request received"
+ "interruptComputeWithError:"
+ "interruptRequest"
+ "interruptTraining"
+ "lastComputeDate"
+ "lock"
+ "missing information on age of model, deferral will be honored"
+ "q40@0:8@16@24q32"
+ "receivedInterruptRequest"
+ "setCandidateLoiToHomeMap:"
+ "setCandidateLoiToLocationMap:"
+ "setCandidateLoiToWorkMap:"
+ "setCandidateModel:"
+ "setCandidateVisitIndicies:"
+ "setCompletionStatus:"
+ "setCurrentComputeDate:"
+ "setHasCompletionStatus:"
+ "setHasReceivedInterruptRequest:"
+ "setInterruptRequest:"
+ "setLastComputeDate:"
+ "setReceivedInterruptRequest:"
+ "setting training interrupt flag"
+ "shouldInterruptTraining"
+ "storeHomeLoisTo:workLoisTo:from:withVisitIndices:"
+ "training interrupted at epoch %ld"
+ "unlock"
+ "v48@0:8@16@24@32@40"
+ "{?=\"completionStatus\"b1\"receivedInterruptRequest\"b1}"
- "Cluster %@ below threshold (%.4f < %.4f) at %@ location"
- "Cluster %@ has %lu workouts with calculated probabilities"
- "Cluster %@ passes threshold (%.4f >= %.4f) at %@ location"
- "Cluster %@, mean probability: %.6f from %d valid probabilities"
- "Encountered null cluster UUID in probability map"
- "Found %lu clusters above threshold of %.4f"
- "Invalid probability value in cluster %@"
- "Logistic Regression Probability Breakdown: CombinedPlaceType=%.4f (weight=%.4f, contrib=%.4f), PlaceName=%.4f (weight=%.4f, contrib=%.4f), GeoProximity=%.4f (weight=%.4f, contrib=%.4f), TimeOfDay=%.4f (weight=%.4f, contrib=%.4f), DayOfWeek=%.4f (weight=%.4f, contrib=%.4f), IsWeekend=%.4f (weight=%.4f, contrib=%.4f), TimeOfDayCircStd=%.4f (weight=%.4f, contrib=%.4f), LatLongCircStd=%.4f (weight=%.4f, contrib=%.4f), Intercept=%.4f, DotProduct=%.4f, Probability=%.9f"
- "No probabilities found for cluster %@"
- "No valid probabilities for cluster %@"
- "Workout %@, cluster %@, raw score: %.6f, adjusted probability: %.6f"
- "_calculateMeanProbabilities:"
- "calculateScoreFromFeatures:"
- "computeWithHistory:transitions:locationsOfInterest:homekitHomes:atTime:"
- "non-home/work"
- "storeHomeLoisTo:workLoisTo:from:"
- "v40@0:8@16@24q32"
- "v56@0:8@16@24@32@40d48"

```
