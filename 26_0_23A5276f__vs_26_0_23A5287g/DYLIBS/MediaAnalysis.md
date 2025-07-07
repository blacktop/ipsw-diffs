## MediaAnalysis

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis`

```diff

-345.64.1.0.0
-  __TEXT.__text: 0x45c194
-  __TEXT.__auth_stubs: 0x3f70
-  __TEXT.__objc_methlist: 0x1cd68
+345.67.3.0.0
+  __TEXT.__text: 0x458b8c
+  __TEXT.__auth_stubs: 0x3f90
+  __TEXT.__objc_methlist: 0x1cd10
   __TEXT.__const: 0x14b28
-  __TEXT.__gcc_except_tab: 0x59a28
-  __TEXT.__cstring: 0x20578
-  __TEXT.__oslogstring: 0x292cb
+  __TEXT.__gcc_except_tab: 0x592a8
+  __TEXT.__cstring: 0x20518
+  __TEXT.__oslogstring: 0x28ccb
   __TEXT.__dlopen_cstrs: 0x4b8
   __TEXT.__ustring: 0x40
-  __TEXT.__swift5_typeref: 0x39e
+  __TEXT.__swift5_typeref: 0x3a8
   __TEXT.__swift5_reflstr: 0xf1
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__constg_swiftt: 0x2a0

   __TEXT.__swift5_fieldmd: 0x100
   __TEXT.__swift5_proto: 0x2c
   __TEXT.__swift5_types: 0x28
-  __TEXT.__swift5_capture: 0xc8
+  __TEXT.__swift5_capture: 0xd8
   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x30
-  __TEXT.__unwind_info: 0x112d0
-  __TEXT.__eh_frame: 0x8b8
+  __TEXT.__unwind_info: 0x11270
+  __TEXT.__eh_frame: 0x940
   __TEXT.__objc_classname: 0x4366
-  __TEXT.__objc_methname: 0x3cc62
-  __TEXT.__objc_methtype: 0xcd0c
-  __TEXT.__objc_stubs: 0x294e0
-  __DATA_CONST.__got: 0x1cc0
-  __DATA_CONST.__const: 0x6688
+  __TEXT.__objc_methname: 0x3ca14
+  __TEXT.__objc_methtype: 0xcd83
+  __TEXT.__objc_stubs: 0x29280
+  __DATA_CONST.__got: 0x1cb8
+  __DATA_CONST.__const: 0x6660
   __DATA_CONST.__objc_classlist: 0x1278
   __DATA_CONST.__objc_catlist: 0x1b8
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc9b8
+  __DATA_CONST.__objc_selrefs: 0xc928
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xec8
-  __DATA_CONST.__objc_arraydata: 0x1230
-  __AUTH_CONST.__auth_got: 0x1fd0
-  __AUTH_CONST.__const: 0x5b60
-  __AUTH_CONST.__cfstring: 0x178e0
-  __AUTH_CONST.__objc_const: 0x381c0
+  __DATA_CONST.__objc_arraydata: 0x11f0
+  __AUTH_CONST.__auth_got: 0x1fe0
+  __AUTH_CONST.__const: 0x5aa8
+  __AUTH_CONST.__cfstring: 0x177c0
+  __AUTH_CONST.__objc_const: 0x38200
   __AUTH_CONST.__objc_floatobj: 0x290
   __AUTH_CONST.__objc_doubleobj: 0x460
-  __AUTH_CONST.__objc_intobj: 0x2ee0
-  __AUTH_CONST.__objc_arrayobj: 0xca8
+  __AUTH_CONST.__objc_intobj: 0x2ec8
+  __AUTH_CONST.__objc_arrayobj: 0xc30
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH.__objc_data: 0x1da0
   __AUTH.__data: 0x1d8
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x9d0
-  __DATA.__objc_ivar: 0x3268
-  __DATA.__data: 0x1ba8
-  __DATA.__bss: 0xec9
+  __DATA.__objc_ivar: 0x3270
+  __DATA.__data: 0x1b88
+  __DATA.__bss: 0xea9
   __DATA.__common: 0x3c1
   __DATA_DIRTY.__objc_data: 0x9d40
   __DATA_DIRTY.__data: 0x160
-  __DATA_DIRTY.__bss: 0x8b0
+  __DATA_DIRTY.__bss: 0x890
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
-  - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CA385050-B681-3F46-810E-D063FF72F3FB
-  Functions: 16738
-  Symbols:   56744
-  CStrings:  21913
+  UUID: CB1DE6EF-A06F-3E17-9574-5E7DA3FBF346
+  Functions: 16719
+  Symbols:   56657
+  CStrings:  21837
 
Symbols:
+ +[MADVectorDatabase _vectorDatabaseMetric]
+ +[MADVideoSessionPixelBufferAsset assetWithPixelBuffer:frameProperties:]
+ -[MADPersonalizedEmbeddingTask processGenerativePlaygroundsOutput:resource:imageSegment:personalizationIndex:embeddingResult:hiddenLayerResult:pooledEmbeddingResult:]
+ -[MADPersonalizedEmbeddingTask processSegments:resource:keyImageSegment:personalizationIndex:textEncoderInputs:]
+ -[MADProcessingGraph addInput:error:]
+ -[MADProcessingGraph hasProcessingFailure]
+ -[MADProcessingNode hasFailure]
+ -[MADServiceVideoSafetyProcessingTask performQRCodeDetectionsForVideoURL:]
+ -[MADUserSafetyImageQRCodeDetector sensitivityFromQRCodeForPixelBuffer:orientation:signpostPayload:]
+ -[MADUserSafetyVideoQRCodeDetector sensitivityFromQRCodeForVideoURL:request:signpostPayload:progressHandler:]
+ -[MADVideoSessionPixelBufferAsset initWithPixelBuffer:orientation:regionOfInterest:timestamp:]
+ -[MADVideoSessionPixelBufferAsset loadPixelBuffer:orientation:regionOfInterest:]
+ -[MADVideoSessionSafetyClassificationTask scalePixelBuffer:output:regionOfInterest:width:height:format:]
+ -[VCPFaceProcessingVersionManager resetAnalysisStateWithError:]
+ -[VCPMADImageSafetyClassificationTask performQRCodeForPixelBuffer:orientation:detections:results:]
+ _OBJC_IVAR_$_MADProcessingNode._isFailed
+ _OBJC_IVAR_$_MADVideoSessionPixelBufferAsset._regionOfInterest
+ ___109-[MADUserSafetyVideoQRCodeDetector sensitivityFromQRCodeForVideoURL:request:signpostPayload:progressHandler:]_block_invoke
+ ___112-[MADPersonalizedEmbeddingTask processSegments:resource:keyImageSegment:personalizationIndex:textEncoderInputs:]_block_invoke
+ ___112-[MADPersonalizedEmbeddingTask processSegments:resource:keyImageSegment:personalizationIndex:textEncoderInputs:]_block_invoke.498
+ ___166-[MADPersonalizedEmbeddingTask processGenerativePlaygroundsOutput:resource:imageSegment:personalizationIndex:embeddingResult:hiddenLayerResult:pooledEmbeddingResult:]_block_invoke
+ ___63-[VCPFaceProcessingVersionManager resetAnalysisStateWithError:]_block_invoke
+ ___block_literal_global.500
+ ___block_literal_global.504
+ ___block_literal_global.512
+ _objc_msgSend$_vectorDatabaseMetric
+ _objc_msgSend$addInput:error:
+ _objc_msgSend$hasFailure
+ _objc_msgSend$hasProcessingFailure
+ _objc_msgSend$initWithPixelBuffer:orientation:regionOfInterest:timestamp:
+ _objc_msgSend$loadPixelBuffer:orientation:regionOfInterest:
+ _objc_msgSend$performQRCodeDetectionsForVideoURL:
+ _objc_msgSend$performQRCodeForPixelBuffer:orientation:detections:results:
+ _objc_msgSend$processGenerativePlaygroundsOutput:resource:imageSegment:personalizationIndex:embeddingResult:hiddenLayerResult:pooledEmbeddingResult:
+ _objc_msgSend$processSegments:resource:keyImageSegment:personalizationIndex:textEncoderInputs:
+ _objc_msgSend$resetAnalysisStateWithError:
+ _objc_msgSend$resetStateForMediaProcessingTaskID:assetIdentifiers:resetOptions:error:
+ _objc_msgSend$scalePixelBuffer:output:regionOfInterest:width:height:format:
+ _objc_msgSend$sensitivityFromQRCodeForPixelBuffer:orientation:signpostPayload:
+ _objc_msgSend$sensitivityFromQRCodeForVideoURL:request:signpostPayload:progressHandler:
+ _swift_bridgeObjectRetain_n
+ _symbolic _____ySsG s23_ContiguousArrayStorageC
- +[MADManagedBackgroundActivitySchedule _isMACDEnabled]
- +[MADManagedBackgroundActivitySchedule _isMACDEnabled].cold.1
- +[MADManagedBackgroundAnalysisProgressHistory(Utilities) shouldUseCDProgressHistory]
- +[MADManagedBackgroundAnalysisProgressHistory(Utilities) shouldUseCDProgressHistory].cold.1
- +[MADManagedChangeToken(Utilities) shouldUseCDChangeToken]
- +[MADManagedChangeToken(Utilities) shouldUseCDChangeToken].cold.1
- +[MADManagedKeyValueStore(Utilities) _isMACDEnabledForKeyValueStore]
- +[MADManagedKeyValueStore(Utilities) _isMACDEnabledForKeyValueStore].cold.1
- +[MADManagedMomentsScheduledAsset(Utilities) shouldUseCDMomentsScheduledAsset]
- +[MADManagedMomentsScheduledAsset(Utilities) shouldUseCDMomentsScheduledAsset].cold.1
- +[MADManagedPhotosAsset(Utilities) _isMACDEnabled]
- +[MADManagedPhotosAsset(Utilities) _isMACDEnabled].cold.1
- +[MADManagedProcessingStatus(Utilities) _isMACDEnabledForProcessingStatus]
- +[MADManagedProcessingStatus(Utilities) _isMACDEnabledForProcessingStatus].cold.1
- +[MADVideoSessionPixelBufferAsset assetWithPixelBuffer:orientation:timestamp:]
- +[VCPFaceProcessingVersionManager resetLevelDescription:]
- -[MADPersonalizedEmbeddingTask processEntitySegment:tokenEmbeddingType:textEncoderInput:ageType:]
- -[MADPersonalizedEmbeddingTask processFaceprintSegment:resource:textEncoderInput:faceObservation:]
- -[MADPersonalizedEmbeddingTask processGenerativePlaygroundsOutput:resource:entitySegment:imageSegment:faceObservation:personalizationIndex:embeddingResult:hiddenLayerResult:pooledEmbeddingResult:]
- -[MADPersonalizedEmbeddingTask processImageSegment:resource:textEncoderInput:faceObservation:ageType:]
- -[MADPersonalizedEmbeddingTask processSegments:resource:keyEntitySegment:keyImageSegment:faceObservation:personalizationIndex:textEncoderInputs:]
- -[MADProcessingGraph processInput:error:]
- -[MADServiceVideoSafetyProcessingTask performQRCodeDetections]
- -[MADUserSafetyImageQRCodeDetector sensitivityFromQRCodeInImage:signpostPayload:]
- -[MADUserSafetyVideoQRCodeDetector sensitivityFromQRCodeInVideo:request:signpostPayload:progressHandler:cancelBlock:]
- -[MADVideoSessionPixelBufferAsset initWithPixelBuffer:orientation:timestamp:]
- -[MADVideoSessionPixelBufferAsset loadPixelBuffer:orientation:]
- -[MADVideoSessionSafetyClassificationTask scalePixelBuffer:output:width:height:format:]
- -[VCPFaceProcessingVersionManager resetAnalysisDataWithResetLevel:error:]
- -[VCPMADImageSafetyClassificationTask performQRCodeDetections:results:]
- _OBJC_CLASS_$_VUWGalleryPersonalizationOptions
- ___117-[MADUserSafetyVideoQRCodeDetector sensitivityFromQRCodeInVideo:request:signpostPayload:progressHandler:cancelBlock:]_block_invoke
- ___145-[MADPersonalizedEmbeddingTask processSegments:resource:keyEntitySegment:keyImageSegment:faceObservation:personalizationIndex:textEncoderInputs:]_block_invoke
- ___145-[MADPersonalizedEmbeddingTask processSegments:resource:keyEntitySegment:keyImageSegment:faceObservation:personalizationIndex:textEncoderInputs:]_block_invoke.522
- ___196-[MADPersonalizedEmbeddingTask processGenerativePlaygroundsOutput:resource:entitySegment:imageSegment:faceObservation:personalizationIndex:embeddingResult:hiddenLayerResult:pooledEmbeddingResult:]_block_invoke
- ___50+[MADManagedPhotosAsset(Utilities) _isMACDEnabled]_block_invoke
- ___54+[MADManagedBackgroundActivitySchedule _isMACDEnabled]_block_invoke
- ___58+[MADManagedChangeToken(Utilities) shouldUseCDChangeToken]_block_invoke
- ___68+[MADManagedKeyValueStore(Utilities) _isMACDEnabledForKeyValueStore]_block_invoke
- ___73-[VCPFaceProcessingVersionManager resetAnalysisDataWithResetLevel:error:]_block_invoke
- ___73-[VCPFaceProcessingVersionManager resetAnalysisDataWithResetLevel:error:]_block_invoke_2
- ___74+[MADManagedProcessingStatus(Utilities) _isMACDEnabledForProcessingStatus]_block_invoke
- ___78+[MADManagedMomentsScheduledAsset(Utilities) shouldUseCDMomentsScheduledAsset]_block_invoke
- ___84+[MADManagedBackgroundAnalysisProgressHistory(Utilities) shouldUseCDProgressHistory]_block_invoke
- ___block_descriptor_64_ea8_32s40s48r_e20_v20?0B8"NSError"12lr48l8s32l8s40l8
- ___block_literal_global.524
- ___block_literal_global.528
- __isMACDEnabled.isEnabled
- __isMACDEnabled.once
- __isMACDEnabledForKeyValueStore.isEnabled
- __isMACDEnabledForKeyValueStore.once
- __isMACDEnabledForProcessingStatus.isEnabled
- __isMACDEnabledForProcessingStatus.once
- _objc_msgSend$_isMACDEnabled
- _objc_msgSend$_isMACDEnabledForKeyValueStore
- _objc_msgSend$_isMACDEnabledForProcessingStatus
- _objc_msgSend$entityGallery
- _objc_msgSend$entityUUID
- _objc_msgSend$faceObservationWithRequestRevision:boundingBox:faceprint:
- _objc_msgSend$faceTorsoprint
- _objc_msgSend$initWithPixelBuffer:orientation:timestamp:
- _objc_msgSend$originatingRequestSpecifier
- _objc_msgSend$performQRCodeDetections
- _objc_msgSend$performQRCodeDetections:results:
- _objc_msgSend$personalizationOptions
- _objc_msgSend$personalizeEmbeddingLayer:index:observation:type:options:error:
- _objc_msgSend$personalizeEmbeddingLayer:index:tag:client:type:options:error:
- _objc_msgSend$processEntitySegment:tokenEmbeddingType:textEncoderInput:ageType:
- _objc_msgSend$processFaceprintSegment:resource:textEncoderInput:faceObservation:
- _objc_msgSend$processGenerativePlaygroundsOutput:resource:entitySegment:imageSegment:faceObservation:personalizationIndex:embeddingResult:hiddenLayerResult:pooledEmbeddingResult:
- _objc_msgSend$processImageSegment:resource:textEncoderInput:faceObservation:ageType:
- _objc_msgSend$processSegments:resource:keyEntitySegment:keyImageSegment:faceObservation:personalizationIndex:textEncoderInputs:
- _objc_msgSend$rangeValue
- _objc_msgSend$resetAnalysisDataWithResetLevel:error:
- _objc_msgSend$resetFaceAnalysisWithResetLevel:completionHandler:
- _objc_msgSend$seed
- _objc_msgSend$sensitivityFromQRCodeInImage:signpostPayload:
- _objc_msgSend$sensitivityFromQRCodeInVideo:request:signpostPayload:progressHandler:cancelBlock:
- _objc_msgSend$setEmbedding:
- _objc_msgSend$setSeed:
- _objc_msgSend$shouldUseCDChangeToken
- _objc_msgSend$shouldUseCDMomentsScheduledAsset
- _objc_msgSend$shouldUseCDProgressHistory
- _objc_msgSend$targetBounds
- _objc_msgSend$tokenEmbeddingType
- _objc_msgSend$tokenEmbeddingsForObservation:type:error:
- _objc_msgSend$tokenEmbeddingsForTag:client:type:error:
- _os_eligibility_get_domain_answer
- _shouldUseCDChangeToken.once
- _shouldUseCDChangeToken.shouldUseCDChangeToken
- _shouldUseCDMomentsScheduledAsset.once
- _shouldUseCDMomentsScheduledAsset.shouldUseCDMomentsScheduledAsset
- _shouldUseCDProgressHistory.once
- _shouldUseCDProgressHistory.shouldUseCDProgressHistory
CStrings:
+ "%@ (%p) Failed to process input"
+ "%@ (%p) child failed to process input: %@"
+ "%@ Failed to add input to queue (%@)"
+ "%@ Processing graph had failure"
+ "@36@0:8^{__CVBuffer=}16I24@28"
+ "@84@0:8^{__CVBuffer=}16I24{CGRect={CGPoint=dd}{CGSize=dd}}28{?=qiIq}60"
+ "Face detection not supported"
+ "Failed to load bridge model: %@"
+ "Inconsistent number of video samples after update"
+ "Processing canceled"
+ "Processing failed"
+ "Processing previously failed"
+ "Q44@0:8^{__CVBuffer=}16I24Q28@36"
+ "[FaceVersion] Dropping %@"
+ "[FaceVersion] Failed to remove %@ - %@"
+ "[FaceVersion] Failed to reset Face Analysis data for PhotoLibrary %@"
+ "[FaceVersion] Failed to reset processing state in Photos Library - %@"
+ "[FaceVersion] Failed to update version state - %@"
+ "[FaceVersion] No persistentURL to update version state - %@"
+ "[FaceVersion] Reset processing state in Photos Library"
+ "[FaceVersion] Resetting processing state ... (%@)"
+ "[MADProcessingGraph] Error sending input to queue: %@"
+ "[MADProcessingGraph] processing had failed"
+ "_isFailed"
+ "_vectorDatabaseMetric"
+ "addInput:error:"
+ "assetWithPixelBuffer:frameProperties:"
+ "com.apple.mediaanalysisd.BackupRunSession"
+ "com.apple.mediaanalysisd.FullClusterAnalysisRunSession"
+ "com.apple.mediaanalysisd.MaintenanceRunSession"
+ "com.apple.mediaanalysisd.TelemetryRunSession"
+ "hasFailure"
+ "hasProcessingFailure"
+ "i40@0:8^^{__CVBuffer}16^I24^{CGRect={CGPoint=dd}{CGSize=dd}}32"
+ "i56@0:8@16@24^@32^Q40@48"
+ "i72@0:8@16@24@32Q40^@48^@56^@64"
+ "i76@0:8^{__CVBuffer=}16^^{__CVBuffer}24{CGRect={CGPoint=dd}{CGSize=dd}}32i64i68I72"
+ "initWithPixelBuffer:orientation:regionOfInterest:timestamp:"
+ "loadPixelBuffer:orientation:regionOfInterest:"
+ "performQRCodeDetectionsForVideoURL:"
+ "performQRCodeForPixelBuffer:orientation:detections:results:"
+ "processGenerativePlaygroundsOutput:resource:imageSegment:personalizationIndex:embeddingResult:hiddenLayerResult:pooledEmbeddingResult:"
+ "processSegments:resource:keyImageSegment:personalizationIndex:textEncoderInputs:"
+ "resetAnalysisStateWithError:"
+ "resetStateForMediaProcessingTaskID:assetIdentifiers:resetOptions:error:"
+ "scalePixelBuffer:output:regionOfInterest:width:height:format:"
+ "sensitivityFromQRCodeForPixelBuffer:orientation:signpostPayload:"
+ "sensitivityFromQRCodeForVideoURL:request:signpostPayload:progressHandler:"
- "%@ (%p) child failed to process input"
- "%@ (%p) failed to process input"
- "%@ CoreData for BackgroundAnalysisProgressHistory"
- "%@ CoreData for ChangeToken"
- "%@ CoreData for MomentsScheduledAsset"
- "%@ processing failed (%@)"
- "@52@0:8^{__CVBuffer=}16I24{?=qiIq}28"
- "@56@0:8@16@24@32@?40@?48"
- "Associated torso: %@"
- "Configuration does not support faceprint inputs"
- "Description and face image input not supported"
- "Description requires entity input"
- "Embedding personalization failed (%@)"
- "Embedding personalization failed - %@"
- "Entity and face image input not supported"
- "Entity should not be the first segment"
- "Face count: %d"
- "Face printing produced no observations"
- "Faceprints not supported with other personalizations"
- "Failed to configure face attributes (%@)"
- "Failed to configure face printing (%@)"
- "Failed to configure torso detection (%@)"
- "Failed to configure torso printing (%@)"
- "Failed to create VUWGallery"
- "Failed to fetch Photos face (%@)"
- "Failed to fetch Photos person (%@)"
- "Failed to generate face-torso representation (%@) %@ (faceprint: %@valid - torsoprint: %@valid)"
- "Failed to perform additional requests - %@"
- "Failed to resolve entity %@ (%@)"
- "Failed to resolve entity (%@)"
- "Generated face-torso representation (%@) %@ (faceprint: %@valid - torsoprint: %@valid)"
- "Largest face: %@"
- "MACD is %@ for Asset and Result tables"
- "MACD is %@ for BackgroundActivitySchedule tables"
- "MACD is %@ for KeyValueStore"
- "MACD is %@ for ProcessingStatus"
- "MACDActivityScheduleEnabled"
- "MACDAssetResultEnabled"
- "MACDChangeToken"
- "MACDKeyValueStore"
- "MACDMomentsScheduledAsset"
- "MACDProcessingStatus"
- "MACDProgressHistory"
- "Multiple entity UUIDs not supported"
- "Multiple faceprints not supported"
- "No face detected, falling back to non-personalized embedding"
- "No identity source provided; generating non-personalized text embedding"
- "Personalization bounds: %@"
- "Personalization index: %d"
- "Personalization seed: %@"
- "Processing entity input (%@)"
- "Processing faceprint input (%@)"
- "Providing personalization with face-torso print - %@"
- "Reset faceAdjustmentVersion"
- "Reset for Forward Compatible version bump (asset.faceAdjustmentVersion + facecrops)"
- "Reset none"
- "VNCreateFaceprintRequest"
- "VUWGallery_personalizeEmbeddingLayerEntity"
- "VUWGallery_personalizeEmbeddingLayerImage"
- "VUWGallery_tokenEmbeddingsForObservation"
- "Will not use"
- "Will use"
- "[%@] image loading failed"
- "[FaceModelBump] Dropping %@"
- "[FaceModelBump] Failed to remove %@ - %@"
- "[FaceModelBump] Failed to reset Face Analysis data for PhotoLibrary %@"
- "[FaceModelBump] Failed to update version state - %@"
- "[FaceModelBump] No persistentURL to update version state - %@"
- "[FaceModelBump] Resetting face data ... (%@)"
- "[MADProcessingGraph] ERROR: %@"
- "_isMACDEnabled"
- "_isMACDEnabledForKeyValueStore"
- "_isMACDEnabledForProcessingStatus"
- "assetWithPixelBuffer:orientation:timestamp:"
- "clip_tokens"
- "entityUUID"
- "faceObservationWithRequestRevision:boundingBox:faceprint:"
- "faceTorsoprint"
- "i32@0:8q16^@24"
- "i48@0:8@16@24^@32^@40"
- "i48@0:8@16q24^@32^S40"
- "i56@0:8@16@24^@32^@40^S48"
- "i72@0:8@16@24^@32^@40^@48^Q56@64"
- "i88@0:8@16@24@32@40@48Q56^@64^@72^@80"
- "in"
- "initWithPixelBuffer:orientation:timestamp:"
- "linear_1"
- "originatingRequestSpecifier"
- "os_eligibility_get_domain_answer failed with errno %d: %s"
- "performQRCodeDetections"
- "performQRCodeDetections:results:"
- "personalizationOptions"
- "personalizeEmbeddingLayer:index:observation:type:options:error:"
- "personalizeEmbeddingLayer:index:tag:client:type:options:error:"
- "processEntitySegment:tokenEmbeddingType:textEncoderInput:ageType:"
- "processFaceprintSegment:resource:textEncoderInput:faceObservation:"
- "processGenerativePlaygroundsOutput:resource:entitySegment:imageSegment:faceObservation:personalizationIndex:embeddingResult:hiddenLayerResult:pooledEmbeddingResult:"
- "processImageSegment:resource:textEncoderInput:faceObservation:ageType:"
- "processSegments:resource:keyEntitySegment:keyImageSegment:faceObservation:personalizationIndex:textEncoderInputs:"
- "rangeValue"
- "resetAnalysisDataWithResetLevel:error:"
- "resetFaceAnalysisWithResetLevel:completionHandler:"
- "resetLevelDescription:"
- "seed"
- "sensitivityFromQRCodeInImage:signpostPayload:"
- "sensitivityFromQRCodeInVideo:request:signpostPayload:progressHandler:cancelBlock:"
- "setEmbedding:"
- "setSeed:"
- "shouldUseCDChangeToken"
- "shouldUseCDMomentsScheduledAsset"
- "shouldUseCDProgressHistory"
- "targetBounds"
- "tokenEmbeddingsForObservation:type:error:"
- "tokenEmbeddingsForTag:client:type:error:"

```
