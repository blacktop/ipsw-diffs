## NRFV4

> `/System/Library/VideoProcessors/NRFV4.bundle/NRFV4`

```diff

-664.40.18.0.0
-  __TEXT.__text: 0x28a4e0
-  __TEXT.__auth_stubs: 0xfa0
-  __TEXT.__objc_methlist: 0x11c08
+664.42.7.0.1
+  __TEXT.__text: 0x28aab0
+  __TEXT.__auth_stubs: 0xf80
+  __TEXT.__objc_methlist: 0x11c50
   __TEXT.__const: 0x102fb0
-  __TEXT.__cstring: 0x3361b
+  __TEXT.__cstring: 0x336d9
   __TEXT.__gcc_except_tab: 0x19cc
-  __TEXT.__oslogstring: 0x351ff
+  __TEXT.__oslogstring: 0x3565b
   __TEXT.__dlopen_cstrs: 0x10c
   __TEXT.__unwind_info: 0x4e18
-  __TEXT.__objc_classname: 0x31f3
-  __TEXT.__objc_methname: 0x34166
-  __TEXT.__objc_methtype: 0x1722f
-  __TEXT.__objc_stubs: 0x16400
-  __DATA_CONST.__got: 0xc28
-  __DATA_CONST.__const: 0x1380
+  __TEXT.__objc_classname: 0x31fa
+  __TEXT.__objc_methname: 0x3423e
+  __TEXT.__objc_methtype: 0x172b9
+  __TEXT.__objc_stubs: 0x16480
+  __DATA_CONST.__got: 0xbe0
+  __DATA_CONST.__const: 0x1358
   __DATA_CONST.__objc_classlist: 0xd98
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6720
+  __DATA_CONST.__objc_selrefs: 0x6738
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xa68
   __DATA_CONST.__objc_arraydata: 0xec0
-  __AUTH_CONST.__auth_got: 0x7e8
+  __AUTH_CONST.__auth_got: 0x7d8
   __AUTH_CONST.__const: 0x820
-  __AUTH_CONST.__cfstring: 0x13aa0
-  __AUTH_CONST.__objc_const: 0x373b8
+  __AUTH_CONST.__cfstring: 0x13ae0
+  __AUTH_CONST.__objc_const: 0x37470
   __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0xb58
-  __AUTH_CONST.__objc_intobj: 0xa50
+  __AUTH_CONST.__objc_intobj: 0xa20
   __AUTH_CONST.__objc_floatobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x550
   __AUTH.__objc_data: 0x1220
-  __DATA.__objc_ivar: 0x3a44
+  __DATA.__objc_ivar: 0x3a54
   __DATA.__data: 0xba8
   __DATA.__common: 0x20
-  __DATA.__bss: 0x14
+  __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x75d0
-  __DATA_DIRTY.__bss: 0x150
+  __DATA_DIRTY.__bss: 0x140
   __DATA_DIRTY.__common: 0xf8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 93A587BC-603F-3130-98A9-DDF358EA1D43
-  Functions: 13399
-  Symbols:   39479
-  CStrings:  19355
+  UUID: AD56110C-77EC-3027-8538-D2138F489336
+  Functions: 13404
+  Symbols:   39492
+  CStrings:  19375
 
Symbols:
+ -[H13FastBayerProcStage(SSC) runSSCWithArgs:inputTexture:inputFrame:outputMetadata:]
+ -[H13FastBayerProcStage(SSC) runSSCWithArgs:inputTexture:inputFrame:outputMetadata:].cold.1
+ -[H13FastBayerProcStage(SSC) runSSCWithArgs:inputTexture:inputFrame:outputMetadata:].cold.2
+ -[H13FastBayerProcStage(SSC) runSSCWithArgs:inputTexture:inputFrame:outputMetadata:].cold.3
+ -[H13FastRawScaleStage(Vision) runFaceDetectionOnPixelBuffer:withInputFrame:config:]
+ -[H13FastRawScaleStage(Vision) runFaceDetectionOnPixelBuffer:withInputFrame:config:].cold.1
+ -[LearnedDemosaicNetworkPostANEStage processTilePipelineStage:].cold.2
+ -[LearnedDemosaicNetworkShared recoveryYUVImage]
+ -[LearnedDemosaicNetworkShared setRecoveryYUVImage:]
+ -[LearnedDemosaicNetworkStage recoveryYUVImage]
+ -[LearnedDemosaicNetworkStage setRecoveryYUVImage:]
+ -[LearnedDemosaicNetworkStage updateParametersFromMetadata:bayerPattern:lscGainsTexture:lscGainParameters:correctDefectPixels:]
+ -[LearnedDemosaicNetworkStage updateParametersFromMetadata:bayerPattern:lscGainsTexture:lscGainParameters:correctDefectPixels:].cold.1
+ -[LearnedDemosaicNetworkStage updateParametersFromMetadata:bayerPattern:lscGainsTexture:lscGainParameters:correctDefectPixels:].cold.2
+ -[LearnedDemosaicNetworkStage updateParametersFromMetadata:bayerPattern:lscGainsTexture:lscGainParameters:correctDefectPixels:].cold.3
+ -[LearnedFusionProcessor addFrame:].cold.4
+ -[SoftISPInputFrame faceRectsForSSC]
+ -[SoftISPInputFrame setFaceRectsForSSC:]
+ _OBJC_IVAR_$_LearnedDemosaicNetworkShared._recoveryYUVImage
+ _OBJC_IVAR_$_LearnedDemosaicNetworkStage._recoveryYUVImage
+ _OBJC_IVAR_$_LearnedFusionProcessor._proxySyntheticReferenceTextureYUV
+ _OBJC_IVAR_$_SoftISPInputFrame._faceRectsForSSC
+ __OBJC_$_PROP_LIST_SoftISPInputFrame
+ ___37-[LearnedFusionProcessor runPipeline]_block_invoke.292
+ ___84-[H13FastBayerProcStage(SSC) runSSCWithArgs:inputTexture:inputFrame:outputMetadata:]_block_invoke
+ ___84-[H13FastBayerProcStage(SSC) runSSCWithArgs:inputTexture:inputFrame:outputMetadata:]_block_invoke_2
+ ___84-[H13FastBayerProcStage(SSC) runSSCWithArgs:inputTexture:inputFrame:outputMetadata:]_block_invoke_3
+ ___84-[H13FastRawScaleStage(Vision) runFaceDetectionOnPixelBuffer:withInputFrame:config:]_block_invoke
+ ___84-[H13FastRawScaleStage(Vision) runFaceDetectionOnPixelBuffer:withInputFrame:config:]_block_invoke_2
+ ___84-[H13FastRawScaleStage(Vision) runFaceDetectionOnPixelBuffer:withInputFrame:config:]_block_invoke_3
+ ___84-[H13FastRawScaleStage(Vision) runFaceDetectionOnPixelBuffer:withInputFrame:config:]_block_invoke_4
+ _kFigCaptureSampleBufferAttachmentKey_SyntheticReferencePixelBuffer
+ _objc_msgSend$faceRectsForSSC
+ _objc_msgSend$recoveryYUVImage
+ _objc_msgSend$runFaceDetectionOnPixelBuffer:withInputFrame:config:
+ _objc_msgSend$runSSCWithArgs:inputTexture:inputFrame:outputMetadata:
+ _objc_msgSend$setFaceRectsForSSC:
+ _objc_msgSend$setRecoveryYUVImage:
+ _objc_msgSend$syntheticReferencePixelBuffer
+ _objc_msgSend$updateParametersFromMetadata:bayerPattern:lscGainsTexture:lscGainParameters:correctDefectPixels:
+ _runFaceDetectionOnPixelBuffer:withInputFrame:config:.asyncQueue
+ _runFaceDetectionOnPixelBuffer:withInputFrame:config:.onceToken
- -[H13FastBayerProcStage(SSC) runSSCWithArgs:inputTexture:outputMetadata:firstPixel:isQuadra:]
- -[H13FastBayerProcStage(SSC) runSSCWithArgs:inputTexture:outputMetadata:firstPixel:isQuadra:].cold.1
- -[H13FastBayerProcStage(SSC) runSSCWithArgs:inputTexture:outputMetadata:firstPixel:isQuadra:].cold.2
- -[H13FastBayerProcStage(SSC) runSSCWithArgs:inputTexture:outputMetadata:firstPixel:isQuadra:].cold.3
- -[H13FastRawScaleStage(Vision) runFaceDetectionOnPixelBuffer:withMetadataToUpdate:config:pts:]
- -[H13FastRawScaleStage(Vision) runFaceDetectionOnPixelBuffer:withMetadataToUpdate:config:pts:].cold.1
- -[LearnedDemosaicNetworkStage updateParametersFromMetadata:bayerPattern:lscGainsTexture:lscGainParameters:]
- -[LearnedDemosaicNetworkStage updateParametersFromMetadata:bayerPattern:lscGainsTexture:lscGainParameters:].cold.1
- -[LearnedDemosaicNetworkStage updateParametersFromMetadata:bayerPattern:lscGainsTexture:lscGainParameters:].cold.2
- -[LearnedDemosaicNetworkStage updateParametersFromMetadata:bayerPattern:lscGainsTexture:lscGainParameters:].cold.3
- _CMTimeConvertScale
- _FigNanosecondsToHostTime
- ___37-[LearnedFusionProcessor runPipeline]_block_invoke.289
- ___93-[H13FastBayerProcStage(SSC) runSSCWithArgs:inputTexture:outputMetadata:firstPixel:isQuadra:]_block_invoke
- ___93-[H13FastBayerProcStage(SSC) runSSCWithArgs:inputTexture:outputMetadata:firstPixel:isQuadra:]_block_invoke_2
- ___93-[H13FastBayerProcStage(SSC) runSSCWithArgs:inputTexture:outputMetadata:firstPixel:isQuadra:]_block_invoke_3
- ___94-[H13FastRawScaleStage(Vision) runFaceDetectionOnPixelBuffer:withMetadataToUpdate:config:pts:]_block_invoke
- ___94-[H13FastRawScaleStage(Vision) runFaceDetectionOnPixelBuffer:withMetadataToUpdate:config:pts:]_block_invoke.26
- ___94-[H13FastRawScaleStage(Vision) runFaceDetectionOnPixelBuffer:withMetadataToUpdate:config:pts:]_block_invoke_2
- ___94-[H13FastRawScaleStage(Vision) runFaceDetectionOnPixelBuffer:withMetadataToUpdate:config:pts:]_block_invoke_2.29
- ___94-[H13FastRawScaleStage(Vision) runFaceDetectionOnPixelBuffer:withMetadataToUpdate:config:pts:]_block_invoke_3
- ___block_descriptor_56_e8_32s40s_e21_"NSMutableArray"8?0ls32l8s40l8
- _kFigCaptureStreamDetectedObjectKey_GroupID
- _kFigCaptureStreamDetectedObjectKey_Modality
- _kFigCaptureStreamMetadata_AngleInfoPitch
- _kFigCaptureStreamMetadata_AngleInfoRoll
- _kFigCaptureStreamMetadata_AngleInfoYaw
- _kFigCaptureStreamMetadata_ConfidenceLevel
- _kFigCaptureStreamMetadata_DetectedFacesArray
- _kFigCaptureStreamMetadata_EyeCoveringConfidenceLevel
- _kFigCaptureStreamMetadata_FaceMaskConfidenceLevel
- _kFigCaptureStreamMetadata_Timestamp
- _objc_msgSend$pitch
- _objc_msgSend$runFaceDetectionOnPixelBuffer:withMetadataToUpdate:config:pts:
- _objc_msgSend$runSSCWithArgs:inputTexture:outputMetadata:firstPixel:isQuadra:
- _objc_msgSend$updateParametersFromMetadata:bayerPattern:lscGainsTexture:lscGainParameters:
- _runFaceDetectionOnPixelBuffer:withMetadataToUpdate:config:pts:.asyncQueue
- _runFaceDetectionOnPixelBuffer:withMetadataToUpdate:config:pts:.onceToken
CStrings:
+ "-[LearnedDemosaicNetworkStage updateParametersFromMetadata:bayerPattern:lscGainsTexture:lscGainParameters:correctDefectPixels:]"
+ "-[LearnedFusionProcessor runLearnedDemosaicNetworkStageOnGivenFrame:label:tuningParams:]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: _proxySyntheticReferenceTextureYUV is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: correctDefectPixels = %d, frameId = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: Recovery luma and chroma textures must both be nil or both be non-nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: _recoveryYUVImage is nil in LearnedDemosaic updateParameters and conflicts with correctDefectPixels.."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: correctDefectPixels = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Failed to bind syntheticReferenceYUV to PixelBuffer, processinType= %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: SyntheticReference output is expected to be hf20"
+ "T@\"LumaChromaImage\",&,N,V_recoveryYUVImage"
+ "T@\"NSArray\",&,N,V_faceRectsForSSC"
+ "^{?=ffBBI{?=ff}}16@0:8"
+ "_faceRectsForSSC"
+ "_proxySyntheticReferenceTextureYUV"
+ "_recoveryYUVImage"
+ "faceId"
+ "faceRectsForSSC"
+ "i40@0:8^{__CVBuffer=}16@24^{VisionParams=BCI}32"
+ "i48@0:8^{SSCConfig=iif}16@24@32@40"
+ "nrf.lf.demosaic.correctDefectPixels"
+ "nrf.lf.demosaic.defectPixelsThreshold"
+ "recoveryYUVImage"
+ "runFaceDetectionOnPixelBuffer:withInputFrame:config:"
+ "runSSCWithArgs:inputTexture:inputFrame:outputMetadata:"
+ "setFaceRectsForSSC:"
+ "setRecoveryYUVImage:"
+ "updateParametersFromMetadata:bayerPattern:lscGainsTexture:lscGainParameters:correctDefectPixels:"
+ "{?=\"outGain\"f\"hrGainDownRatio\"f\"rotateTile180\"B\"isQuadra\"B\"defectivePixelZeroChannelThreshold\"I\"srcRawFullResNormalizeFactor\"\"lscParams\"{?=\"lscScale\"\"lscOffset\"\"lscNormalization\"f\"lscModulationWeight\"f}}"
+ "\xf0\xf0\xf0\xd1"
- "-[LearnedDemosaicNetworkStage updateParametersFromMetadata:bayerPattern:lscGainsTexture:lscGainParameters:]"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: syntheticReferenceYUV is nil"
- "^{?=ffBB}16@0:8"
- "i48@0:8^{SSCConfig=iif}16@24@32i40B44"
- "i64@0:8^{__CVBuffer=}16@24^{VisionParams=BCI}32{?=qiIq}40"
- "pitch"
- "runFaceDetectionOnPixelBuffer:withMetadataToUpdate:config:pts:"
- "runSSCWithArgs:inputTexture:outputMetadata:firstPixel:isQuadra:"
- "updateParametersFromMetadata:bayerPattern:lscGainsTexture:lscGainParameters:"
- "{?=\"outGain\"f\"hrGainDownRatio\"f\"rotateTile180\"B\"isQuadra\"B}"
- "\xf0\xf0\xf0\xc1"

```
