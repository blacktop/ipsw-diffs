## FRC

> `/System/Library/PrivateFrameworks/FRC.framework/Versions/A/FRC`

```diff

-259.0.0.0.0
-  __TEXT.__text: 0x41f14
-  __TEXT.__objc_methlist: 0x3a9c
-  __TEXT.__const: 0x5b0
-  __TEXT.__cstring: 0x659e
-  __TEXT.__oslogstring: 0xec3
+263.0.0.0.0
+  __TEXT.__text: 0x44fb0
+  __TEXT.__objc_methlist: 0x3bcc
+  __TEXT.__const: 0x5d0
+  __TEXT.__cstring: 0x6900
+  __TEXT.__oslogstring: 0x1029
   __TEXT.__gcc_except_tab: 0x270
-  __TEXT.__unwind_info: 0x1070
+  __TEXT.__unwind_info: 0x1118
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x230
-  __DATA_CONST.__objc_classlist: 0x178
+  __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22d0
-  __DATA_CONST.__objc_superrefs: 0x138
-  __DATA_CONST.__got: 0x460
-  __AUTH_CONST.__const: 0x688
-  __AUTH_CONST.__cfstring: 0x3e60
-  __AUTH_CONST.__objc_const: 0xa710
+  __DATA_CONST.__objc_selrefs: 0x2380
+  __DATA_CONST.__objc_superrefs: 0x140
+  __DATA_CONST.__got: 0x468
+  __AUTH_CONST.__const: 0x6a8
+  __AUTH_CONST.__cfstring: 0x4180
+  __AUTH_CONST.__objc_const: 0xaf20
   __AUTH_CONST.__auth_got: 0x6c8
-  __DATA.__objc_ivar: 0xdb0
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0xe88
   __DATA.__data: 0x140
   __DATA_DIRTY.__objc_data: 0xeb0
   __DATA_DIRTY.__bss: 0x8

   - /System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/Versions/A/IOSurfaceAccelerator
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1464
-  Symbols:   3825
-  CStrings:  840
+  Functions: 1507
+  Symbols:   3934
+  CStrings:  885
 
Symbols:
+ -[FRCMotionBlurFlowRefiner .cxx_destruct]
+ -[FRCMotionBlurFlowRefiner computeDilatedErrorMap:errorMap:dilatedErrorMap:searchRadius:]
+ -[FRCMotionBlurFlowRefiner computeDisparityEdgeMap:disparity:disparityEdgeMap:edgeTolerance:]
+ -[FRCMotionBlurFlowRefiner computeVelocityEdgeMap:inVelocity:velocityEdgeMap:edgeThresh:]
+ -[FRCMotionBlurFlowRefiner computeVelocityMapWithDisplacement:displacement:outVelocity:outNeighborMaxVelocity:tileMax:]
+ -[FRCMotionBlurFlowRefiner correctDisplacementErrorWithDisparity:inDisplacement:disparity:displacementErrorMap:debugTexture:correcttedDisplacement:sparseSampleStep:invUpscaleRatio:]
+ -[FRCMotionBlurFlowRefiner correctDisplacementMagnitudeError:inDisplacement:correcttedDisplacement:debugTexture:]
+ -[FRCMotionBlurFlowRefiner detectDisplacementErrorWithDisparity:inDisplacement:disparity:lowResDisplacementErrorMap:disparityEdgeMaxMap:velocityEdgeMap:displacementErrorMap:debugTexture:sparseSampleStep:invUpscaleRatio:isSecondIteration:isUpscaled:]
+ -[FRCMotionBlurFlowRefiner encodeFlowRefineToCommandBuffer:opticalFlow:disparity:inputRGBATex:velocity:neighborMaxVelocity:upsampledVelocity:]
+ -[FRCMotionBlurFlowRefiner encodeNeighborMaxFlowToCommandBuffer:tileMax:neighborMax:]
+ -[FRCMotionBlurFlowRefiner encodePostUpscaleFlowRefineToCommandBuffer:disparity:rgbaSizeVelocity:upsampledVelocity:]
+ -[FRCMotionBlurFlowRefiner encodePreUpscaleFlowRefineToCommandBuffer:opticalFlow:disparity:velocity:neighborMaxVelocity:]
+ -[FRCMotionBlurFlowRefiner encodeTileMaxVelocityToCommandBuffer:velocity:tileMax:]
+ -[FRCMotionBlurFlowRefiner encodeVelocityForMotionBlurToCommandBuffer:displacement:velocity:]
+ -[FRCMotionBlurFlowRefiner ensureDisparityEdgeMapsForDisparity:]
+ -[FRCMotionBlurFlowRefiner initWithDevice:commandQueue:flowSize:rgbaSize:upscaleRatio:timeScale:tileSize:searchRange:]
+ -[FRCMotionBlurFlowRefiner rgbaSizeVelocity]
+ -[FRCMotionBlurFlowRefiner upsampleVelocity:inVelocity:disparity:upsampledVelocity:]
+ -[Forwarp deterministicAccumulation]
+ -[Forwarp initWithDevice:commmandQueue:mode:deterministicAccumulation:]
+ -[NeuFlow isUsageSupported:]
+ -[Synthesis deterministicAccumulation]
+ -[Synthesis setDeterministicAccumulation:]
+ FRCMotionBlurFlowRefinerLog
+ FRCMotionBlurFlowRefinerLog.once
+ FRCMotionBlurFlowRefinerLog.sLog
+ OBJC_IVAR_$_FRCFrameInterpolator._deterministicSynthesis
+ OBJC_IVAR_$_FRCImageProcessor._originalFrameCMAttachment
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._computeDisplacementErrorMaxPipeline
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._correctDisplacementErrorPipeline
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._correctDisplacementMagnitudeErrorPipeline
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._correctedDisplacement
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._correctedDisplacement0
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._correctedUpscaledVelocity
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._correctedUpscaledVelocity0
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._detectDisplacementErrorPipeline
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._disparityEdgeMap
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._disparityEdgeMaxMap
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._disparityEdgePipeline
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._displacementErrorMap
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._displacementErrorMaxMap
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._displacementErrorStats
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._displacementMagnitudeErrorStats
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._flowToVelocityPipeline
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._flowUpscaler
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._neighborMaxVelocityPipeline
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._rgbaSize
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._rgbaSizeVelocity
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._searchRange
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._tileMaxVelocity
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._tileMaxVelocityPipeline
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._tileSize
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._timeScale
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._upsampleVelocityPipeline
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._upscaleRatio
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._upscaledVelocityEdgeMap
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._upscaledVelocityEdgeMaxMap
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._upscaledVelocityErrorMap
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._upscaledVelocityErrorStats
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._velocityEdgePipeline
+ OBJC_IVAR_$_FRCMotionBlurFlowRefiner._velocityMagnitudeErrorStats
+ OBJC_IVAR_$_Forwarp._deterministicAccumulation
+ OBJC_IVAR_$_NeuFlow._ane1InputFirst
+ OBJC_IVAR_$_NeuFlow._ane1InputSecond
+ OBJC_IVAR_$_NeuFlow._ane1OutputContextS8
+ OBJC_IVAR_$_NeuFlow._ane1OutputFeature0S4
+ OBJC_IVAR_$_NeuFlow._ane1OutputFeature0S8
+ OBJC_IVAR_$_NeuFlow._ane1OutputFeature1S4
+ OBJC_IVAR_$_NeuFlow._ane1OutputFeature1S8
+ OBJC_IVAR_$_NeuFlow._ane1OutputFlow
+ OBJC_IVAR_$_NeuFlow._ane2InputContextS8
+ OBJC_IVAR_$_NeuFlow._ane2InputCorrelation
+ OBJC_IVAR_$_NeuFlow._ane2InputFlow
+ OBJC_IVAR_$_NeuFlow._ane2InputIterContextS8
+ OBJC_IVAR_$_NeuFlow._ane2OutputContextS8
+ OBJC_IVAR_$_NeuFlow._ane2OutputFlow
+ OBJC_IVAR_$_NeuFlow._ane3InputCostVolume
+ OBJC_IVAR_$_NeuFlow._ane3InputFlow
+ OBJC_IVAR_$_NeuFlow._ane3OutputFlow
+ OBJC_IVAR_$_NeuFlow._modelType
+ OBJC_IVAR_$_Synthesis._deterministicAccumulation
+ _FRCMotionBlurFlowRefinerLog
+ _OBJC_CLASS_$_FRCMotionBlurFlowRefiner
+ _OBJC_METACLASS_$_FRCMotionBlurFlowRefiner
+ __OBJC_$_INSTANCE_METHODS_FRCMotionBlurFlowRefiner
+ __OBJC_$_INSTANCE_VARIABLES_FRCMotionBlurFlowRefiner
+ __OBJC_$_PROP_LIST_FRCMotionBlurFlowRefiner
+ __OBJC_CLASS_RO_$_FRCMotionBlurFlowRefiner
+ __OBJC_METACLASS_RO_$_FRCMotionBlurFlowRefiner
+ ___FRCMotionBlurFlowRefinerLog_block_invoke
+ _createInputTextureFromCVPixelBuffer
+ _kCVPixelFormatContainsGrayscale
+ _objc_msgSend$computeDilatedErrorMap:errorMap:dilatedErrorMap:searchRadius:
+ _objc_msgSend$computeDisparityEdgeMap:disparity:disparityEdgeMap:edgeTolerance:
+ _objc_msgSend$computeVelocityEdgeMap:inVelocity:velocityEdgeMap:edgeThresh:
+ _objc_msgSend$computeVelocityMapWithDisplacement:displacement:outVelocity:outNeighborMaxVelocity:tileMax:
+ _objc_msgSend$correctDisplacementErrorWithDisparity:inDisplacement:disparity:displacementErrorMap:debugTexture:correcttedDisplacement:sparseSampleStep:invUpscaleRatio:
+ _objc_msgSend$correctDisplacementMagnitudeError:inDisplacement:correcttedDisplacement:debugTexture:
+ _objc_msgSend$detectDisplacementErrorWithDisparity:inDisplacement:disparity:lowResDisplacementErrorMap:disparityEdgeMaxMap:velocityEdgeMap:displacementErrorMap:debugTexture:sparseSampleStep:invUpscaleRatio:isSecondIteration:isUpscaled:
+ _objc_msgSend$dispatchThreads:threadsPerThreadgroup:
+ _objc_msgSend$encodeNeighborMaxFlowToCommandBuffer:tileMax:neighborMax:
+ _objc_msgSend$encodePostUpscaleFlowRefineToCommandBuffer:disparity:rgbaSizeVelocity:upsampledVelocity:
+ _objc_msgSend$encodePreUpscaleFlowRefineToCommandBuffer:opticalFlow:disparity:velocity:neighborMaxVelocity:
+ _objc_msgSend$encodeTileMaxVelocityToCommandBuffer:velocity:tileMax:
+ _objc_msgSend$encodeVelocityForMotionBlurToCommandBuffer:displacement:velocity:
+ _objc_msgSend$ensureDisparityEdgeMapsForDisparity:
+ _objc_msgSend$initWithDevice:commmandQueue:mode:deterministicAccumulation:
+ _objc_msgSend$isUsageSupported:
+ _objc_msgSend$setDeterministicAccumulation:
+ _objc_msgSend$upsampleVelocity:inVelocity:disparity:upsampledVelocity:
- OBJC_IVAR_$_NeuFlow._useDistilledModel
CStrings:
+ "Cannot allocate FlowUpscaler"
+ "Cannot allocate MTLComputeCommandEncoder"
+ "DeterministicSynthesis"
+ "FRCMotionBlurFlowRefiner"
+ "FRCMotionBlurFlowRefiner initialized: flowSize=%.0fx%.0f rgbaSize=%.0fx%.0f upscaleRatio=%.3f timeScale=%.3f tileSize=%d searchRange=%d"
+ "Failed to init %s"
+ "NeuFlow2_Flode_part1"
+ "NeuFlow2_Flode_part2"
+ "NeuFlow2_Flode_part3"
+ "NeuFlowUseFlodeDistilledModel"
+ "Setting deterministicSynthesis to %d"
+ "Usage is not supported"
+ "Using Flode Distilled Model"
+ "_computeDisplacementErrorMaxPipeline"
+ "_correctDisplacementErrorPipeline"
+ "_correctDisplacementMagnitudeErrorPipeline"
+ "_detectDisplacementErrorPipeline"
+ "_disparityEdgePipeline"
+ "_flowToVelocityPipeline"
+ "_neighborMaxVelocityPipeline"
+ "_tileMaxVelocityPipeline"
+ "_upsampleVelocityPipeline"
+ "_velocityEdgePipeline"
+ "com.apple.frc"
+ "computeDisplacementErrorMax"
+ "compute_disparity_edge"
+ "compute_flow_edge"
+ "correctDisplacementErrorWithDisparity"
+ "correctDisplacementMagnitudeError"
+ "detectDisplacementErrorWithDisparity"
+ "feature0_s4"
+ "feature0_s8"
+ "feature1_s4"
+ "feature1_s8"
+ "flow0_init_s8"
+ "flow0_refined"
+ "flow0_s1"
+ "flowToVelocityConversionRefiner"
+ "img0"
+ "img1"
+ "iter_context_s8_new"
+ "landscape640x368"
+ "neighborMaxVelocityRefiner"
+ "tileMaxVelocityRefiner"
+ "upsampleVelocity"
```
