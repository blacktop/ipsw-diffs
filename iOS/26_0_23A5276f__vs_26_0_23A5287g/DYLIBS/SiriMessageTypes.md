## SiriMessageTypes

> `/System/Library/PrivateFrameworks/SiriMessageTypes.framework/SiriMessageTypes`

```diff

-3500.61.2.0.0
-  __TEXT.__text: 0x1281d8
+3500.66.1.0.0
+  __TEXT.__text: 0x129008
   __TEXT.__auth_stubs: 0x1260
-  __TEXT.__objc_methlist: 0x2110
+  __TEXT.__objc_methlist: 0x2380
   __TEXT.__const: 0x1b748
-  __TEXT.__cstring: 0x77f2
+  __TEXT.__cstring: 0x7a0e
   __TEXT.__oslogstring: 0x13ec
   __TEXT.__swift5_typeref: 0x5017
   __TEXT.__constg_swiftt: 0x8b7c

   __TEXT.__swift5_protos: 0x3c
   __TEXT.__swift5_mpenum: 0x9c
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x8570
+  __TEXT.__unwind_info: 0x8648
   __TEXT.__eh_frame: 0x8940
-  __TEXT.__objc_classname: 0x2f7
-  __TEXT.__objc_methname: 0x2607
-  __TEXT.__objc_methtype: 0x746
-  __TEXT.__objc_stubs: 0x1600
-  __DATA_CONST.__got: 0x4f8
-  __DATA_CONST.__const: 0xf80
-  __DATA_CONST.__objc_classlist: 0x598
-  __DATA_CONST.__objc_protolist: 0x58
+  __TEXT.__objc_classname: 0x379
+  __TEXT.__objc_methname: 0x2996
+  __TEXT.__objc_methtype: 0x85b
+  __TEXT.__objc_stubs: 0x1880
+  __DATA_CONST.__got: 0x508
+  __DATA_CONST.__const: 0x1028
+  __DATA_CONST.__objc_classlist: 0x5a8
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x810
+  __DATA_CONST.__objc_selrefs: 0x8c0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x70
-  __DATA_CONST.__objc_arraydata: 0x60
+  __DATA_CONST.__objc_superrefs: 0x80
+  __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__auth_got: 0x938
-  __AUTH_CONST.__const: 0xcec0
-  __AUTH_CONST.__cfstring: 0xac0
-  __AUTH_CONST.__objc_const: 0x89b0
-  __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x2360
+  __AUTH_CONST.__const: 0xcee0
+  __AUTH_CONST.__cfstring: 0xc60
+  __AUTH_CONST.__objc_const: 0x8e98
+  __AUTH_CONST.__objc_intobj: 0xd8
+  __AUTH_CONST.__objc_dictobj: 0x78
+  __AUTH.__objc_data: 0x2400
   __AUTH.__data: 0x2a40
-  __DATA.__objc_ivar: 0x24c
-  __DATA.__data: 0x3538
-  __DATA.__bss: 0x246b0
+  __DATA.__objc_ivar: 0x294
+  __DATA.__data: 0x3598
+  __DATA.__bss: 0x246c0
   __DATA.__common: 0x1b8
   __DATA_DIRTY.__objc_data: 0xbc40
   __DATA_DIRTY.__data: 0x5f00

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A1F82930-EC0C-3681-8DD2-176DFCC27C55
-  Functions: 13668
-  Symbols:   8266
-  CStrings:  1493
+  UUID: 16FB3D00-A3D7-31F2-8DE5-4C7B3108929F
+  Functions: 13715
+  Symbols:   8423
+  CStrings:  1561
 
Symbols:
+ +[SMTSpeechDetectionUpdate newWithBuilder:]
+ +[SMTSpeechDetectionUpdate supportsSecureCoding]
+ -[SMTSiriIntendedInfo neuralCombinerScore]
+ -[SMTSiriIntendedInfo neuralCombinerThreshold]
+ -[SMTSpeechDetectionUpdate .cxx_destruct]
+ -[SMTSpeechDetectionUpdate _descriptionWithIndent:]
+ -[SMTSpeechDetectionUpdate copyWithZone:]
+ -[SMTSpeechDetectionUpdate description]
+ -[SMTSpeechDetectionUpdate encodeWithCoder:]
+ -[SMTSpeechDetectionUpdate hash]
+ -[SMTSpeechDetectionUpdate initWithBuilder:]
+ -[SMTSpeechDetectionUpdate initWithCoder:]
+ -[SMTSpeechDetectionUpdate init]
+ -[SMTSpeechDetectionUpdate isEqual:]
+ -[SMTSpeechDetectionUpdate lastTRPCandidateId]
+ -[SMTSpeechDetectionUpdate processedAudioDurationMs]
+ -[SMTSpeechDetectionUpdate speechDetected]
+ -[SMTSpeechDetectionUpdate trailingSilenceDurationMs]
+ -[SMTSpeechDetectionUpdate wordCount]
+ -[SMTSpeechDetectionUpdate(SMTSpeechDetectionUpdateMutability) mutatedCopyWithMutator:]
+ -[SMTTCUPackage neuralCombinerMitigationDecision]
+ -[_SMTSiriIntendedInfoMutation getNeuralCombinerScore]
+ -[_SMTSiriIntendedInfoMutation getNeuralCombinerThreshold]
+ -[_SMTSiriIntendedInfoMutation setNeuralCombinerScore:]
+ -[_SMTSiriIntendedInfoMutation setNeuralCombinerThreshold:]
+ -[_SMTSpeechDetectionUpdateMutation .cxx_destruct]
+ -[_SMTSpeechDetectionUpdateMutation getLastTRPCandidateId]
+ -[_SMTSpeechDetectionUpdateMutation getProcessedAudioDurationMs]
+ -[_SMTSpeechDetectionUpdateMutation getSpeechDetected]
+ -[_SMTSpeechDetectionUpdateMutation getTrailingSilenceDurationMs]
+ -[_SMTSpeechDetectionUpdateMutation getWordCount]
+ -[_SMTSpeechDetectionUpdateMutation initWithBase:]
+ -[_SMTSpeechDetectionUpdateMutation isDirty]
+ -[_SMTSpeechDetectionUpdateMutation setLastTRPCandidateId:]
+ -[_SMTSpeechDetectionUpdateMutation setProcessedAudioDurationMs:]
+ -[_SMTSpeechDetectionUpdateMutation setSpeechDetected:]
+ -[_SMTSpeechDetectionUpdateMutation setTrailingSilenceDurationMs:]
+ -[_SMTSpeechDetectionUpdateMutation setWordCount:]
+ -[_SMTTCUPackageMutation getNeuralCombinerMitigationDecision]
+ -[_SMTTCUPackageMutation setNeuralCombinerMitigationDecision:]
+ _OBJC_CLASS_$_SMTSpeechDetectionUpdate
+ _OBJC_CLASS_$__SMTSpeechDetectionUpdateMutation
+ _OBJC_IVAR_$_SMTSiriIntendedInfo._neuralCombinerScore
+ _OBJC_IVAR_$_SMTSiriIntendedInfo._neuralCombinerThreshold
+ _OBJC_IVAR_$_SMTSpeechDetectionUpdate._lastTRPCandidateId
+ _OBJC_IVAR_$_SMTSpeechDetectionUpdate._processedAudioDurationMs
+ _OBJC_IVAR_$_SMTSpeechDetectionUpdate._speechDetected
+ _OBJC_IVAR_$_SMTSpeechDetectionUpdate._trailingSilenceDurationMs
+ _OBJC_IVAR_$_SMTSpeechDetectionUpdate._wordCount
+ _OBJC_IVAR_$_SMTTCUPackage._neuralCombinerMitigationDecision
+ _OBJC_IVAR_$__SMTSiriIntendedInfoMutation._neuralCombinerScore
+ _OBJC_IVAR_$__SMTSiriIntendedInfoMutation._neuralCombinerThreshold
+ _OBJC_IVAR_$__SMTSpeechDetectionUpdateMutation._base
+ _OBJC_IVAR_$__SMTSpeechDetectionUpdateMutation._lastTRPCandidateId
+ _OBJC_IVAR_$__SMTSpeechDetectionUpdateMutation._mutationFlags
+ _OBJC_IVAR_$__SMTSpeechDetectionUpdateMutation._processedAudioDurationMs
+ _OBJC_IVAR_$__SMTSpeechDetectionUpdateMutation._speechDetected
+ _OBJC_IVAR_$__SMTSpeechDetectionUpdateMutation._trailingSilenceDurationMs
+ _OBJC_IVAR_$__SMTSpeechDetectionUpdateMutation._wordCount
+ _OBJC_IVAR_$__SMTTCUPackageMutation._neuralCombinerMitigationDecision
+ _OBJC_METACLASS_$_SMTSpeechDetectionUpdate
+ _OBJC_METACLASS_$__SMTSpeechDetectionUpdateMutation
+ _SMTNeuralCombinerMitigationDecisionGetFromName
+ _SMTNeuralCombinerMitigationDecisionGetFromName.map
+ _SMTNeuralCombinerMitigationDecisionGetFromName.onceToken
+ _SMTNeuralCombinerMitigationDecisionGetIsValid
+ _SMTNeuralCombinerMitigationDecisionGetIsValidAndSpecified
+ _SMTNeuralCombinerMitigationDecisionGetName
+ _SMTSpeechDetectionUpdateKey
+ __OBJC_$_CLASS_METHODS_SMTSpeechDetectionUpdate
+ __OBJC_$_CLASS_PROP_LIST_SMTSpeechDetectionUpdate
+ __OBJC_$_INSTANCE_METHODS_SMTSpeechDetectionUpdate(SMTSpeechDetectionUpdateMutability)
+ __OBJC_$_INSTANCE_METHODS__SMTSpeechDetectionUpdateMutation
+ __OBJC_$_INSTANCE_VARIABLES_SMTSpeechDetectionUpdate
+ __OBJC_$_INSTANCE_VARIABLES__SMTSpeechDetectionUpdateMutation
+ __OBJC_$_PROP_LIST_SMTSpeechDetectionUpdate
+ __OBJC_$_PROP_LIST__SMTSpeechDetectionUpdateMutation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SMTSpeechDetectionUpdateMutating
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SMTSpeechDetectionUpdateMutating
+ __OBJC_$_PROTOCOL_REFS_SMTSpeechDetectionUpdateMutating
+ __OBJC_CLASS_PROTOCOLS_$_SMTSpeechDetectionUpdate
+ __OBJC_CLASS_PROTOCOLS_$__SMTSpeechDetectionUpdateMutation
+ __OBJC_CLASS_RO_$_SMTSpeechDetectionUpdate
+ __OBJC_CLASS_RO_$__SMTSpeechDetectionUpdateMutation
+ __OBJC_LABEL_PROTOCOL_$_SMTSpeechDetectionUpdateMutating
+ __OBJC_METACLASS_RO_$_SMTSpeechDetectionUpdate
+ __OBJC_METACLASS_RO_$__SMTSpeechDetectionUpdateMutation
+ __OBJC_PROTOCOL_$_SMTSpeechDetectionUpdateMutating
+ ___37-[SMTSiriIntendedInfo initWithCoder:]_block_invoke
+ ___42-[SMTSpeechDetectionUpdate initWithCoder:]_block_invoke
+ ___SMTNeuralCombinerMitigationDecisionGetFromName_block_invoke
+ ___block_descriptor_65_e8_32s_e44_v16?0"<SMTSpeechDetectionUpdateMutating>"8ls32l8
+ ___block_descriptor_88_e8_32s_e39_v16?0"<SMTSiriIntendedInfoMutating>"8ls32l8
+ ___block_literal_global.128
+ ___block_literal_global.208
+ ___block_literal_global.628
+ ___block_literal_global.983
+ _objc_msgSend$getNeuralCombinerMitigationDecision
+ _objc_msgSend$getNeuralCombinerScore
+ _objc_msgSend$getNeuralCombinerThreshold
+ _objc_msgSend$getProcessedAudioDurationMs
+ _objc_msgSend$getSpeechDetected
+ _objc_msgSend$getTrailingSilenceDurationMs
+ _objc_msgSend$getWordCount
+ _objc_msgSend$neuralCombinerMitigationDecision
+ _objc_msgSend$neuralCombinerScore
+ _objc_msgSend$neuralCombinerThreshold
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$processedAudioDurationMs
+ _objc_msgSend$setNeuralCombinerScore:
+ _objc_msgSend$setNeuralCombinerThreshold:
+ _objc_msgSend$setProcessedAudioDurationMs:
+ _objc_msgSend$setSpeechDetected:
+ _objc_msgSend$setTrailingSilenceDurationMs:
+ _objc_msgSend$setWordCount:
+ _objc_msgSend$speechDetected
+ _objc_msgSend$trailingSilenceDurationMs
+ _objc_msgSend$wordCount
- ___block_literal_global.186
- ___block_literal_global.494
- ___block_literal_global.845
- _objc_msgSend$initWithOdldScore:aftmScore:spkrIdScore:lrnnScore:checkerScore:invocationType:lrnnThreshold:lrnnScale:lrnnOffset:conversationalOdldScore:spkrIdThreshold:
CStrings:
+ "%@ {odldScore = %f, aftmScore = %f, spkrIdScore = %f, lrnnScore = %f, checkerScore = %f, invocationType = %@, lrnnThreshold = %f, lrnnScale = %f, lrnnOffset = %f, gazeSignalPresent = %u, conversationalOdldScore = %f, spkrIdThreshold = %f, neuralCombinerScore = %f, ncThreshold = %f }"
+ "%@ {speechDetected = %u, lastTRPCandidateId = %@, processedAudioDurationMs = %ldtrailingSilenceDurationMs = %ld, wordCount = %ld}"
+ "%@ {tcuId = %@, requestId = %@, tcuState = %@, speechEvent = %lld, voiceTriggerPhraseType = %@, siriIntendedInfo = %@, prevTCUIds = %@, startAudioTimeStampInMs = %f, endAudioTimeStampInMs = %f, speechPackage = %@, neuralCombinerMitigationDecision = %@}"
+ ">, <hasSufficientAudioProcessed:"
+ "@\"SMTSpeechDetectionUpdate\""
+ "SMTSiriIntendedInfo::neuralCombinerScore"
+ "SMTSiriIntendedInfo::neuralCombinerThreshold"
+ "SMTSpeechDetectionUpdate"
+ "SMTSpeechDetectionUpdateMutability"
+ "SMTSpeechDetectionUpdateMutating"
+ "TB,R,N,V_speechDetected"
+ "TQ,R,N,V_wordCount"
+ "Tf,R,N,V_neuralCombinerScore"
+ "Tf,R,N,V_neuralCombinerThreshold"
+ "Tq,R,N,V_neuralCombinerMitigationDecision"
+ "Tq,R,N,V_processedAudioDurationMs"
+ "Tq,R,N,V_trailingSilenceDurationMs"
+ "_SMTSpeechDetectionUpdateMutation"
+ "_neuralCombinerMitigationDecision"
+ "_neuralCombinerScore"
+ "_neuralCombinerThreshold"
+ "_processedAudioDurationMs"
+ "_speechDetected"
+ "_trailingSilenceDurationMs"
+ "_wordCount"
+ "getNeuralCombinerMitigationDecision"
+ "getNeuralCombinerScore"
+ "getNeuralCombinerThreshold"
+ "getProcessedAudioDurationMs"
+ "getSpeechDetected"
+ "getTrailingSilenceDurationMs"
+ "getWordCount"
+ "may_be_mitigated"
+ "neuralCombinerMitigationDecision"
+ "neuralCombinerScore"
+ "neuralCombinerThreshold"
+ "numberWithUnsignedInteger:"
+ "processedAudioDurationMs"
+ "selected"
+ "setNeuralCombinerMitigationDecision:"
+ "setNeuralCombinerScore:"
+ "setNeuralCombinerThreshold:"
+ "setProcessedAudioDurationMs:"
+ "setSpeechDetected:"
+ "setTrailingSilenceDurationMs:"
+ "setWordCount:"
+ "speechDetected"
+ "trailingSilenceDurationMs"
+ "v16@?0@\"<SMTSpeechDetectionUpdateMutating>\"8"
+ "wordCount"
+ "{_mutationFlags=\"isDirty\"b1\"hasOdldScore\"b1\"hasAftmScore\"b1\"hasSpkrIdScore\"b1\"hasLrnnScore\"b1\"hasCheckerScore\"b1\"hasInvocationType\"b1\"hasLrnnThreshold\"b1\"hasLrnnScale\"b1\"hasLrnnOffset\"b1\"hasIsGazeSignalPresent\"b1\"hasConversationalOdldScore\"b1\"hasSpkrIdThreshold\"b1\"hasNeuralCombinerScore\"b1\"hasNeuralCombinerThreshold\"b1}"
+ "{_mutationFlags=\"isDirty\"b1\"hasSpeechDetected\"b1\"hasLastTRPCandidateId\"b1\"hasProcessedAudioDurationMs\"b1\"hasTrailingSilenceDurationMs\"b1\"hasWordCount\"b1}"
+ "{_mutationFlags=\"isDirty\"b1\"hasTcuId\"b1\"hasRequestId\"b1\"hasTcuState\"b1\"hasSpeechEvent\"b1\"hasVoiceTriggerPhraseType\"b1\"hasSiriIntendedInfo\"b1\"hasPrevTCUIds\"b1\"hasStartAudioTimeStampInMs\"b1\"hasEndAudioTimeStampInMs\"b1\"hasSpeechPackage\"b1\"hasNeuralCombinerMitigationDecision\"b1}"
- "%@ {odldScore = %f, aftmScore = %f, spkrIdScore = %f, lrnnScore = %f, checkerScore = %f, invocationType = %@, lrnnThreshold = %f, lrnnScale = %f, lrnnOffset = %f, gazeSignalPresent = %u, conversationalOdldScore = %f, spkrIdThreshold = %f}"
- "%@ {tcuId = %@, requestId = %@, tcuState = %@, speechEvent = %lld, voiceTriggerPhraseType = %@, siriIntendedInfo = %@, prevTCUIds = %@, startAudioTimeStampInMs = %f, endAudioTimeStampInMs = %f, speechPackage = %@}"
- ">, <hasSuffienctAudioProcessed:"
- "a"
- "{_mutationFlags=\"isDirty\"b1\"hasOdldScore\"b1\"hasAftmScore\"b1\"hasSpkrIdScore\"b1\"hasLrnnScore\"b1\"hasCheckerScore\"b1\"hasInvocationType\"b1\"hasLrnnThreshold\"b1\"hasLrnnScale\"b1\"hasLrnnOffset\"b1\"hasIsGazeSignalPresent\"b1\"hasConversationalOdldScore\"b1\"hasSpkrIdThreshold\"b1}"
- "{_mutationFlags=\"isDirty\"b1\"hasTcuId\"b1\"hasRequestId\"b1\"hasTcuState\"b1\"hasSpeechEvent\"b1\"hasVoiceTriggerPhraseType\"b1\"hasSiriIntendedInfo\"b1\"hasPrevTCUIds\"b1\"hasStartAudioTimeStampInMs\"b1\"hasEndAudioTimeStampInMs\"b1\"hasSpeechPackage\"b1}"

```
