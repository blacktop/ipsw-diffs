## NRFV4

> `/System/Library/VideoProcessors/NRFV4.bundle/NRFV4`

```diff

-659.0.0.0.4
-  __TEXT.__text: 0x2de3b0
-  __TEXT.__auth_stubs: 0xfc0
+661.0.0.0.3
+  __TEXT.__text: 0x2deeb4
+  __TEXT.__auth_stubs: 0xf90
   __TEXT.__objc_methlist: 0x10400
   __TEXT.__const: 0x1027c8
-  __TEXT.__cstring: 0x5b01b
-  __TEXT.__gcc_except_tab: 0x1d20
-  __TEXT.__oslogstring: 0x4f8e7
+  __TEXT.__cstring: 0x5b013
+  __TEXT.__gcc_except_tab: 0x1d10
+  __TEXT.__oslogstring: 0x4fc36
   __TEXT.__dlopen_cstrs: 0x10c
-  __TEXT.__unwind_info: 0x4d48
+  __TEXT.__unwind_info: 0x4d58
   __TEXT.__objc_classname: 0x2dc0
-  __TEXT.__objc_methname: 0x31897
+  __TEXT.__objc_methname: 0x31880
   __TEXT.__objc_methtype: 0x15ee6
-  __TEXT.__objc_stubs: 0x14fa0
-  __DATA_CONST.__got: 0xc18
+  __TEXT.__objc_stubs: 0x14f20
+  __DATA_CONST.__got: 0xc10
   __DATA_CONST.__const: 0x1340
   __DATA_CONST.__objc_classlist: 0xc98
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x61b0
+  __DATA_CONST.__objc_selrefs: 0x6180
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x9a0
   __DATA_CONST.__objc_arraydata: 0xe40
-  __AUTH_CONST.__auth_got: 0x7f8
+  __AUTH_CONST.__auth_got: 0x7e0
   __AUTH_CONST.__const: 0x7e0
-  __AUTH_CONST.__cfstring: 0x13180
+  __AUTH_CONST.__cfstring: 0x13120
   __AUTH_CONST.__objc_const: 0x328a8
   __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0xae0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 156B3B1E-F7A0-378E-857D-FAD6A16F00BC
-  Functions: 12571
-  Symbols:   37919
-  CStrings:  23698
+  UUID: 63D0F146-9FD2-3AD4-81AD-F0C9D5BEB758
+  Functions: 12581
+  Symbols:   37997
+  CStrings:  23703
 
Symbols:
+ -[DeepFusionProcessor processFrameForRegistration:isReference:].cold.4
+ -[DenoiseFusePipeline addFrame:cfp:processingType:createPyramid:batchCount:].cold.7
+ -[DenoiseFusePipeline addFrame:cfp:processingType:createPyramid:batchCount:].cold.8
+ -[LearnedNRProcessor addInputResource:backingPixelBufferDimensions:]
+ -[LearnedNRProcessor addInputResource:backingPixelBufferDimensions:].cold.1
+ -[LearnedNRProcessor addInputResource:backingPixelBufferDimensions:].cold.2
+ -[LearnedNRProcessor addInputResource:backingPixelBufferDimensions:].cold.3
+ -[LearnedNRProcessor addInputResource:backingPixelBufferDimensions:].cold.4
+ -[LearnedNRProcessor addInputResource:backingPixelBufferDimensions:].cold.5
+ -[LearnedNRProcessor generateGainMapIfNeeded:]
+ -[LearnedNRProcessor generateGainMapIfNeeded:].cold.1
+ -[LearnedNRProcessor generateGainMapIfNeeded:].cold.2
+ -[LearnedNRProcessor generateGainMapIfNeeded:].cold.3
+ -[LearnedNRProcessor generateGainMapIfNeeded:].cold.4
+ -[LearnedNRProcessor generateGainMapIfNeeded:].cold.5
+ -[SubjectRelightingStage runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:glassesMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:iptSkinMedian:].cold.1
+ -[SubjectRelightingStage runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:glassesMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:iptSkinMedian:].cold.2
+ -[SubjectRelightingStage runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:glassesMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:iptSkinMedian:].cold.3
+ -[SubjectRelightingStage runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:glassesMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:iptSkinMedian:].cold.4
+ -[SubjectRelightingStage runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:glassesMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:iptSkinMedian:].cold.5
+ -[SubjectRelightingStage runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:glassesMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:iptSkinMedian:].cold.6
+ -[SubjectRelightingStage runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:glassesMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:iptSkinMedian:].cold.7
+ -[SubjectRelightingStage runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:glassesMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:iptSkinMedian:].cold.8
+ -[SubjectRelightingStage runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:glassesMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:iptSkinMedian:].cold.9
+ ___115-[CMIRawNightModeRegistrationStage processConstrainedNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:]_block_invoke.364
+ ___119-[CMIRawNightModeRegistrationStage processRegWarpRegDenseNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:]_block_invoke.271
+ ___119-[CMIRawNightModeRegistrationStage processRegWarpRegDenseNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:]_block_invoke.272
+ ___block_literal_global.274
+ ___block_literal_global.339
+ _objc_msgSend$cameraInfoForPortType:
+ _objc_msgSend$generateGainMapIfNeeded:
+ _objc_msgSend$getInternalAWBMetadataForMIWB:cameraInfo:metadata:validRect:secondaryModuleConfig:secondaryCameraInfo:
+ _objc_msgSend$moduleConfigForPortType:
- -[CMISoftwareFlashRenderingRegistrationV2 registerImage:referenceLumaTexture:].cold.3
- -[LearnedNRProcessor addInputResource:]
- -[LearnedNRProcessor addInputResource:].cold.1
- -[LearnedNRProcessor addInputResource:].cold.2
- -[LearnedNRProcessor addInputResource:].cold.3
- -[LearnedNRProcessor addInputResource:].cold.4
- -[LearnedNRProcessor addInputResource:].cold.5
- -[LearnedNRProcessor generateGainMapIfNeeded]
- -[LearnedNRProcessor generateGainMapIfNeeded].cold.1
- -[LearnedNRProcessor generateGainMapIfNeeded].cold.2
- -[LearnedNRProcessor generateGainMapIfNeeded].cold.3
- -[LearnedNRProcessor generateGainMapIfNeeded].cold.4
- -[LearnedNRProcessor generateGainMapIfNeeded].cold.5
- _OBJC_CLASS_$_NSInvocation
- ___115-[CMIRawNightModeRegistrationStage processConstrainedNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:]_block_invoke.363
- ___119-[CMIRawNightModeRegistrationStage processRegWarpRegDenseNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:]_block_invoke.270
- ___119-[CMIRawNightModeRegistrationStage processRegWarpRegDenseNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:]_block_invoke_2.288
- ___NRFReportRecoverableError_block_invoke
- ___block_literal_global.272
- ___block_literal_global.292
- ___block_literal_global.337
- _exit
- _getprogname
- _objc_msgSend$generateGainMapIfNeeded
- _objc_msgSend$getReturnValue:
- _objc_msgSend$invocationWithMethodSignature:
- _objc_msgSend$invoke
- _objc_msgSend$methodSignatureForSelector:
- _objc_msgSend$setArgument:atIndex:
- _objc_msgSend$setSelector:
- _objc_msgSend$setTarget:
- _strcmp
CStrings:
+ "-[LearnedNRProcessor addInputResource:backingPixelBufferDimensions:]"
+ "-[LearnedNRProcessor generateGainMapIfNeeded:]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  originalFrameHeight %d\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  originalFrameWidth %d\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: inputChromaFormat cannot be MTLPixelFormatInvalid"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: inputLumaFormat cannot be MTLPixelFormatInvalid"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: setGainMapConfig failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: postProcYuvImage not set right for gainMap"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: setGainMapConfig failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: setGainMapConfig failed, bailing (%d)"
+ "< %@ >, status: %d"
+ "<<<< CMISoftwareFlashRendering >>>> %s: allocateResources failed"
+ "<<<< CMISoftwareFlashRendering >>>> %s: processNonReferenceTexture failed"
+ "<<<< CMISoftwareFlashRendering >>>> %s: processReferenceTexture failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: processNonReferenceTexture failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: setGainMapConfig failed, bailing (%d)"
+ "<<<< RawNightMode >>>> %s: processNonReferenceTexture failed"
+ "<<<< RawProcFrames >>>> %s: Ignoring registration error, frameID: %d, isReferenceFrame : %s, isEVM : %s"
+ "<<<< SoftISP >>>> %s: Could not get internal AWB metadata for MIWB: miwbErr = %d."
+ "com.apple.cameracapture.ane-error"
+ "generateGainMapIfNeeded:"
+ "ibpErr == ibpErrCode_NoError || ibpErr == ibpErrCode_InsufficientInliers"
+ "inputChromaFormat != MTLPixelFormatInvalid"
+ "inputLumaFormat != MTLPixelFormatInvalid"
+ "instanceMask0"
+ "instanceMask1"
+ "instanceMask2"
+ "instanceMask3"
+ "miwbErr == 0 "
- "-[LearnedNRProcessor addInputResource:]"
- "-[LearnedNRProcessor generateGainMapIfNeeded]"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/Common/NRFCommon.m %s: Deferred processing: exiting due to recoverable error ( %@ )"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: It's unfortuate that we need to downscale the input Band0 second time for generating the GainMap, please look into it."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: _downscaledInput not set right for gainMap"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: prepareDownscaledInputWithBand0 for GainMap failed with err = %d"
- "<<<< RawProcFrames >>>> %s: Ignoring registraion error, frameID: %d, isReferenceFrame : %s, isEVM : %s"
- "<<<< SoftISP >>>> %s: Could not get internal AWB metadata for MIWB: miwbErr = %d. MIWB won't be run."
- "NRFReportRecoverableError_block_invoke"
- "Network error during processing with message < %@ >, status: %d"
- "com.apple.cameracapture.gpu-error"
- "continuation"
- "deferredmediad"
- "generateGainMapIfNeeded"
- "getInternalAWBMetadataForMIWB:cameraInfo:metadata:validRect:"
- "getReturnValue:"
- "invocationWithMethodSignature:"
- "invoke"
- "methodSignatureForSelector:"
- "setArgument:atIndex:"
- "setSelector:"
- "setTarget:"

```
