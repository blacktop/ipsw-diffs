## SpeechDetector

> `/System/Library/PrivateFrameworks/SpeechDetector.framework/SpeechDetector`

```diff

-3525.5.8.0.0
-  __TEXT.__text: 0x1d30
-  __TEXT.__auth_stubs: 0x2b0
+3600.64.114.1.5
+  __TEXT.__text: 0x1a2c
   __TEXT.__objc_methlist: 0x484
-  __TEXT.__const: 0x84
-  __TEXT.__cstring: 0x535
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x541
   __TEXT.__oslogstring: 0x20c
-  __TEXT.__unwind_info: 0x130
-  __TEXT.__objc_classname: 0xb3
-  __TEXT.__objc_methname: 0xee5
-  __TEXT.__objc_methtype: 0x341
-  __TEXT.__objc_stubs: 0x8a0
-  __DATA_CONST.__got: 0xb8
+  __TEXT.__unwind_info: 0xf8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_selrefs: 0x3d0
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x220
-  __AUTH_CONST.__auth_got: 0x160
+  __DATA_CONST.__got: 0xb8
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x880
   __AUTH_CONST.__objc_const: 0x910
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x68
   __DATA.__data: 0x258

   - /System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ED8C7564-F6CC-310A-AFE9-9D87F38D708F
+  UUID: 08FF80D1-BF28-341A-92B1-C283C1A314F8
   Functions: 61
-  Symbols:   370
-  CStrings:  388
+  Symbols:   373
+  CStrings:  156
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- _objc_retainAutoreleasedReturnValue
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<LipMovementVADDelegate>\""
- "@\"<OSDAnalyzerAssetLocker>\""
- "@\"<OSDAnalyzerDelegate>\""
- "@\"EARCaesuraSilencePosteriorGenerator\""
- "@\"MLModel\""
- "@\"MLPredictionOptions\""
- "@\"NSArray\""
- "@\"NSDictionary\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"OSDFeatures\""
- "@\"SDLipMovementVAD\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16Q24"
- "@40@0:8:16@24@32"
- "@48@0:8d16d24d32d40"
- "@56@0:8d16d24d32d40Q48"
- "@64@0:8@16Q24@32@40@48@56"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B40@0:8@16Q24@32"
- "EARCaesuraSilencePosteriorGeneratorDelegate"
- "LipMovementData"
- "LipMovementVADDelegate"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "OSDAnalyzer"
- "OSDFeatures"
- "Q16@0:8"
- "SDLipMovementVAD"
- "T#,R"
- "T@\"<LipMovementVADDelegate>\",W,N,V_delegate"
- "T@\"<OSDAnalyzerAssetLocker>\",&,N,V_osdAnalyzerAssetLocker"
- "T@\"<OSDAnalyzerDelegate>\",W,N,V_delegate"
- "T@\"EARCaesuraSilencePosteriorGenerator\",&,N,V_caesuraSPG"
- "T@\"NSArray\",R,N,V_blendshapes"
- "T@\"NSDictionary\",&,N,V_osdContext"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_lipMovementQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"OSDFeatures\",&,N,V_osdFeatures"
- "T@\"SDLipMovementVAD\",&,N,V_lipMovementVAD"
- "TB,N,V_endOfSpeechDetected"
- "TB,N,V_startOfSpeechDetected"
- "TB,R"
- "TQ,R"
- "TQ,R,N,V_absMachTime"
- "TQ,R,N,V_inferenceTime"
- "Td,R,N,V_processedAudioMs"
- "Td,R,N,V_silenceDurationMs"
- "Td,R,N,V_silenceFramesCountMs"
- "Td,R,N,V_silenceProbability"
- "Td,R,N,V_visualSpeechProbability"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_absMachTime"
- "_blendshapeLocationToIndexMap"
- "_blendshapes"
- "_caesuraSPG"
- "_configFile"
- "_delegate"
- "_endOfSpeechDetected"
- "_framesToNextPrediction"
- "_inferenceTime"
- "_lipMovementDataArray"
- "_lipMovementQueue"
- "_lipMovementVAD"
- "_lipMovementVADModel"
- "_numConsecutiveNonSilenceFrames"
- "_options"
- "_osdAnalyzerAssetLocker"
- "_osdContext"
- "_osdFeatures"
- "_processedAudioMs"
- "_queue"
- "_setupCaesuraSPGWithConfigFile:sampleRate:osdAnalyzerAssetLocker:"
- "_setupOEPAssetManagerWithOSDAnalyzerAssetLocker:"
- "_silenceDurationMs"
- "_silenceFramesCountMs"
- "_silenceProbability"
- "_startOfSpeechDetected"
- "_visualSpeechProbability"
- "absMachTime"
- "addAudio:numSamples:"
- "addFaceTrackingData:atMachAbsTime:"
- "addObject:"
- "appendFormat:"
- "arrayWithObjects:count:"
- "autorelease"
- "blendshapes"
- "bytes"
- "caesuraSPG"
- "class"
- "clientSilenceFeaturesAvailable:"
- "conformsToProtocol:"
- "copy"
- "copyWithZone:"
- "count"
- "d"
- "d16@0:8"
- "debugDescription"
- "decodeDoubleForKey:"
- "decodeObjectOfClass:forKey:"
- "delegate"
- "description"
- "dictionary"
- "didUpdateVisualSpeechProbability:from:to:"
- "encodeDouble:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endAudio"
- "endOfSpeechDetected"
- "enumerateObjectsUsingBlock:"
- "featureValueForName:"
- "fileURLWithPath:"
- "firstObject"
- "floatValue"
- "getCurrentOSDFeatures"
- "getFrameDurationMs"
- "hash"
- "inferenceTime"
- "init"
- "initWithBlendshape:andTime:"
- "initWithCoder:"
- "initWithConfigFile:sampleRate:context:queue:delegate:osdAnalyzerAssetLocker:"
- "initWithConfigFile:samplingRate:queue:"
- "initWithDictionary:error:"
- "initWithModelFile:"
- "initWithShape:dataType:error:"
- "initWithSilenceFramesCountMs:silenceProbability:silenceDurationMs:processedAudioMs:"
- "initWithSilenceFramesCountMs:silenceProbability:silenceDurationMs:processedAudioMs:inferenceTime:"
- "intValue"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lastObject"
- "length"
- "lipMovementQueue"
- "lipMovementVAD"
- "localeWithLocaleIdentifier:"
- "localizedDescription"
- "modelWithContentsOfURL:configuration:error:"
- "multiArrayValue"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "osdAnalyzer:didDetectEndOfSpeechAt:"
- "osdAnalyzer:didDetectStartOfSpeechAt:"
- "osdAnalyzer:didUpdateOSDFeatures:"
- "osdAnalyzer:didUpdateVisualSpeechProbability:from:to:"
- "osdAnalyzerAssetLocker"
- "osdContext"
- "osdFeatures"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "predictionFromFeatures:options:error:"
- "processedAudioMs"
- "q16@0:8"
- "queue"
- "release"
- "removeAllObjects"
- "removeObjectAtIndex:"
- "reset"
- "resetTimer"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "runModel"
- "self"
- "setCaesuraSPG:"
- "setComputeUnits:"
- "setDateFormat:"
- "setDelegate:"
- "setEndOfSpeechDetected:"
- "setLipMovementQueue:"
- "setLipMovementVAD:"
- "setLocale:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOsdAnalyzerAssetLocker:"
- "setOsdContext:"
- "setOsdFeatures:"
- "setQueue:"
- "setStartOfSpeechDetected:"
- "setupBlendshapeIndexArray"
- "setupLipMovementVADWithModelPath:"
- "silenceDurationEstimateAvailable:numEstimates:clientProcessedAudioMs:"
- "silenceDurationMs"
- "silenceFramesCountMs"
- "silencePosteriorGeneratorProcessorIsFinished:"
- "silenceProbability"
- "startOfSpeechDetected"
- "string"
- "superclass"
- "supportsSecureCoding"
- "unsignedLongLongValue"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"EARCaesuraSilencePosteriorGenerator\"16"
- "v24@0:8@\"EARClientSilenceFeatures\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v32@0:8@16Q24"
- "v36@0:8^f16Q24f32"
- "v40@0:8d16Q24Q32"
- "visualSpeechProbability"
- "zone"

```
