## FRC

> `/System/Library/PrivateFrameworks/FRC.framework/FRC`

```diff

-230.0.0.0.0
-  __TEXT.__text: 0x32104
-  __TEXT.__auth_stubs: 0xe30
-  __TEXT.__objc_methlist: 0x2e4c
-  __TEXT.__const: 0x560
-  __TEXT.__cstring: 0x56de
-  __TEXT.__oslogstring: 0x76e
-  __TEXT.__gcc_except_tab: 0x12c
-  __TEXT.__unwind_info: 0x980
-  __TEXT.__objc_classname: 0x340
-  __TEXT.__objc_methname: 0xb32e
-  __TEXT.__objc_methtype: 0x3574
-  __TEXT.__objc_stubs: 0x56c0
-  __DATA_CONST.__got: 0x408
-  __DATA_CONST.__const: 0x508
-  __DATA_CONST.__objc_classlist: 0x140
+242.0.0.0.0
+  __TEXT.__text: 0x3bb84
+  __TEXT.__auth_stubs: 0xf00
+  __TEXT.__objc_methlist: 0x36bc
+  __TEXT.__const: 0x5b0
+  __TEXT.__cstring: 0x5f0c
+  __TEXT.__oslogstring: 0xbf2
+  __TEXT.__gcc_except_tab: 0x270
+  __TEXT.__unwind_info: 0xbe8
+  __TEXT.__objc_classname: 0x3cc
+  __TEXT.__objc_methname: 0xceb8
+  __TEXT.__objc_methtype: 0x3cb6
+  __TEXT.__objc_stubs: 0x64e0
+  __DATA_CONST.__got: 0x448
+  __DATA_CONST.__const: 0x6e0
+  __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c68
-  __DATA_CONST.__objc_superrefs: 0x108
-  __AUTH_CONST.__auth_got: 0x728
-  __AUTH_CONST.__const: 0xd8
-  __AUTH_CONST.__cfstring: 0x3280
-  __AUTH_CONST.__objc_const: 0x8268
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0xa44
+  __DATA_CONST.__objc_selrefs: 0x2110
+  __DATA_CONST.__objc_superrefs: 0x130
+  __AUTH_CONST.__auth_got: 0x790
+  __AUTH_CONST.__const: 0x118
+  __AUTH_CONST.__cfstring: 0x37e0
+  __AUTH_CONST.__objc_const: 0x9868
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0xc58
   __DATA.__data: 0x140
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0xb90
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/Frameworks/Vision.framework/Vision

   - /System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FA0DD73D-27C2-3877-A5FF-AA326774948B
-  Functions: 1082
-  Symbols:   4119
-  CStrings:  3072
+  UUID: EBEA55CB-5E4A-3165-B040-9F9B032B5C7F
+  Functions: 1354
+  Symbols:   4983
+  CStrings:  3530
 
Symbols:
+ -[Backwarp commandQueue]
+ -[Backwarp encodeToCommandBuffer:source:flow:destination:]
+ -[Backwarp setCommandQueue:]
+ -[Correlation commandQueue]
+ -[Correlation encode5x5ToCommandBuffer:first:second:flow:destination:]
+ -[Correlation encodeToCommandBuffer:first:second:destination:scaleInput:]
+ -[Correlation setCommandQueue:]
+ -[E5Model .cxx_destruct]
+ -[E5Model IOSurfaceSharedEvent]
+ -[E5Model allocateBufferObjects]
+ -[E5Model allocateBufferObjects].cold.1
+ -[E5Model allocateBufferObjects].cold.2
+ -[E5Model allocateBufferObjects].cold.3
+ -[E5Model allocateBufferObjects].cold.4
+ -[E5Model allocateBufferObjects].cold.5
+ -[E5Model allocateBufferObjects].cold.6
+ -[E5Model bindPorts]
+ -[E5Model bindPorts].cold.1
+ -[E5Model bindPorts].cold.2
+ -[E5Model buildLibraryForModel:]
+ -[E5Model buildLibraryForModel:].cold.1
+ -[E5Model buildLibraryForModel:].cold.2
+ -[E5Model buildLibraryForModel:].cold.3
+ -[E5Model buildLibraryForModel:].cold.4
+ -[E5Model buildLibraryForModel:].cold.5
+ -[E5Model buildLibraryForModel:].cold.6
+ -[E5Model buildLibraryFromE5BundleForModel:]
+ -[E5Model buildLibraryFromE5BundleForModel:].cold.1
+ -[E5Model createFunctionListFromLibrary]
+ -[E5Model dealloc]
+ -[E5Model deviceType]
+ -[E5Model encodeStream]
+ -[E5Model encodeStream].cold.1
+ -[E5Model encodeStream].cold.2
+ -[E5Model encodeStream].cold.3
+ -[E5Model encodeStream].cold.4
+ -[E5Model encodeStream].cold.5
+ -[E5Model encodeStream].cold.6
+ -[E5Model executeAsync:]
+ -[E5Model executeAsync:].cold.1
+ -[E5Model executeAsync:].cold.2
+ -[E5Model executeSync]
+ -[E5Model executeSync].cold.1
+ -[E5Model firstInputSurface]
+ -[E5Model functionName:]
+ -[E5Model getPortNames]
+ -[E5Model getPortNames].cold.1
+ -[E5Model getPortShape:width:height:channels:bytesPerComponent:]
+ -[E5Model getPortShape:width:height:channels:bytesPerComponent:].cold.1
+ -[E5Model getPortShape:width:height:channels:bytesPerComponent:].cold.10
+ -[E5Model getPortShape:width:height:channels:bytesPerComponent:].cold.11
+ -[E5Model getPortShape:width:height:channels:bytesPerComponent:].cold.2
+ -[E5Model getPortShape:width:height:channels:bytesPerComponent:].cold.3
+ -[E5Model getPortShape:width:height:channels:bytesPerComponent:].cold.4
+ -[E5Model getPortShape:width:height:channels:bytesPerComponent:].cold.5
+ -[E5Model getPortShape:width:height:channels:bytesPerComponent:].cold.6
+ -[E5Model getPortShape:width:height:channels:bytesPerComponent:].cold.7
+ -[E5Model getPortShape:width:height:channels:bytesPerComponent:].cold.8
+ -[E5Model getPortShape:width:height:channels:bytesPerComponent:].cold.9
+ -[E5Model initWithModel:]
+ -[E5Model initWithModel:].cold.1
+ -[E5Model initializeFunction:]
+ -[E5Model initializeFunction:].cold.1
+ -[E5Model initializeFunction:].cold.2
+ -[E5Model initializeFunction:].cold.3
+ -[E5Model initializeFunction:].cold.4
+ -[E5Model initializeFunction:].cold.5
+ -[E5Model initializeFunction:].cold.6
+ -[E5Model initializeFunctionForUsage:]
+ -[E5Model initializeLibrary:]
+ -[E5Model initializeLibrary:].cold.1
+ -[E5Model inputIOSurface:]
+ -[E5Model inputIOSurfaceByName:]
+ -[E5Model inputSize:]
+ -[E5Model modelName]
+ -[E5Model outputIOSurface:]
+ -[E5Model outputIOSurfaceByName:]
+ -[E5Model outputSize:]
+ -[E5Model releaseBufferObjects]
+ -[E5Model releaseE5Resoruces]
+ -[E5Model resetStream:]
+ -[E5Model resetStream:].cold.1
+ -[E5Model secondInputSurface]
+ -[E5Model setDeviceType:]
+ -[E5Model setFirstInputSurfac:]
+ -[E5Model setFirstInputSurface:]
+ -[E5Model setIOSurfaceSharedEvent:]
+ -[E5Model setInputIOSurface:index:]
+ -[E5Model setInputIOSurface:index:].cold.1
+ -[E5Model setOutputIOSurface:index:]
+ -[E5Model setOutputIOSurface:index:].cold.1
+ -[E5Model setSecondInputSurfac:]
+ -[E5Model setSecondInputSurface:]
+ -[FRCBlit copyLinearBuffer:toLinearBuffer:commandBuffer:]
+ -[FRCBlit copyLinearBuffer:toTexture:commandBuffer:]
+ -[FRCBlit copyTexture:toLinearBuffer:commandBuffer:]
+ -[FRCFrameSynthesizer initWithUsage:qualityMode:bypassFrameStats:]
+ -[FRCFrameSynthesizer initWithUsage:qualityMode:normalizationMode:]
+ -[FRCImageProcessor commandQueue]
+ -[FRCImageProcessor setCommandQueue:]
+ -[FRCMetalBase commandQueue]
+ -[FRCMetalBase setCommandQueue:]
+ -[FRCOpticalFlowEstimator matchFlow:callback:]
+ -[FRCOpticalFlowEstimator matchFlow:toFullSizeFlow:callback:]
+ -[FRCOpticalFlowEstimator opticalFlowFrom:to:flow:completionHandler:]
+ -[FRCOpticalFlowEstimatorConfiguration commandQueue]
+ -[FRCOpticalFlowEstimatorConfiguration inputDownsampling]
+ -[FRCOpticalFlowEstimatorConfiguration setCommandQueue:]
+ -[FRCOpticalFlowEstimatorConfiguration setInputDownsampling:]
+ -[FRCOpticalFlowEstimatorConfiguration setWaitForCompletion:]
+ -[FRCOpticalFlowEstimatorConfiguration waitForCompletion]
+ -[FlowUpscaler .cxx_destruct]
+ -[FlowUpscaler EnableGpuWaitForComplete]
+ -[FlowUpscaler allocateHRFlowBufferWithHrWidth:hrHeight:]
+ -[FlowUpscaler allocateHRFlowBufferWithHrWidth:hrHeight:].cold.1
+ -[FlowUpscaler allocateInternalBuffersWithLrWidth:lrHeight:hrWidth:hrHeight:]
+ -[FlowUpscaler commandBufferWait:flag:]
+ -[FlowUpscaler dealloc]
+ -[FlowUpscaler encodeComputeRGBandFlowEdgeToCommandBuffer:rgb:flow:destination:edgeThresh:]
+ -[FlowUpscaler encodeDeblockToCommandBuffer:flow:output:upscaleFactor:]
+ -[FlowUpscaler encodeDilateEdgeMapToCommandBuffer:input:destination:]
+ -[FlowUpscaler encodeDownscaleImageToCommandBuffer:input:output:]
+ -[FlowUpscaler encodeHighUpscaleToCommandBuffer:lrFlow:rgbFlowEdge:hrImage:flow1:flow2:rgb1:rgb2:internalResult:hrFlow:]
+ -[FlowUpscaler encodeLowResClusterToCommandBuffer:lrFlow:lrImage:rgbFlowEdge:flow1:flow2:rgb1:rgb2:internalResult:]
+ -[FlowUpscaler flowUpscalingFromImage:inputFlow:outputFlow:completionHandler:]
+ -[FlowUpscaler initWithLrWidth:lrHeight:hrWidth:hrHeight:]
+ -[FlowUpscaler initWithLrWidth:lrHeight:hrWidth:hrHeight:].cold.1
+ -[FlowUpscaler initWithLrWidth:lrHeight:hrWidth:hrHeight:].cold.2
+ -[FlowUpscaler releaseBufferAndTexture]
+ -[FlowUpscaler releaseResources]
+ -[FlowUpscaler setEnableGpuWaitForComplete:]
+ -[FlowUpscaler upscaleRefinedFloV2With:RGB:lrFlow:output:]
+ -[MotionBlur .cxx_destruct]
+ -[MotionBlur computePipelineStateFor:withConstants:]
+ -[MotionBlur computeVelocityMapWithDisplacement:outVelocity:outNeighborMaxVelocity:tileMax:]
+ -[MotionBlur encodeNeighborMaxFlowWithCommandBuffer:tileMax:searchRange:neighborMax:]
+ -[MotionBlur encodeNeighborMaxFlowWithCommandBuffer:tileMax:searchRange:neighborMax:].cold.1
+ -[MotionBlur encodeTileMaxVelocityWithCommandBuffer:velocity:tileSize:tileMax:]
+ -[MotionBlur encodeTileMaxVelocityWithCommandBuffer:velocity:tileSize:tileMax:].cold.1
+ -[MotionBlur encodeVelocityForMotionBlurWithCommandBuffer:displacement:velocity:timeScale:tileSize:searchRange:]
+ -[MotionBlur encodeVelocityForMotionBlurWithCommandBuffer:displacement:velocity:timeScale:tileSize:searchRange:].cold.1
+ -[MotionBlur initWithDevice:commandQueue:library:pipelineLibrary:timeScale:tileSize:searchRange:]
+ -[MotionBlurOpticalFlowEstimator .cxx_destruct]
+ -[MotionBlurOpticalFlowEstimator allocateResources]
+ -[MotionBlurOpticalFlowEstimator computeOpticalFlowFrom:]
+ -[MotionBlurOpticalFlowEstimator computeOpticalFlowFrom:flow:completionHandler:]
+ -[MotionBlurOpticalFlowEstimator computeOpticalFlowFrom:flow:completionHandler:].cold.1
+ -[MotionBlurOpticalFlowEstimator computeOpticalFlowFrom:flow:completionHandler:].cold.2
+ -[MotionBlurOpticalFlowEstimator createReferenceFrameBufferwithWidth:height:]
+ -[MotionBlurOpticalFlowEstimator dealloc]
+ -[MotionBlurOpticalFlowEstimator flowHeight]
+ -[MotionBlurOpticalFlowEstimator flowWidth]
+ -[MotionBlurOpticalFlowEstimator initWithWidth:height:]
+ -[MotionBlurOpticalFlowEstimator initWithWidth:height:commandQueue:]
+ -[MotionBlurOpticalFlowEstimator initWithWidth:height:commandQueue:e5Model:]
+ -[MotionBlurOpticalFlowEstimator initWithWidth:height:commandQueue:e5Model:].cold.1
+ -[MotionBlurOpticalFlowEstimator initWithWidth:height:e5Model:]
+ -[MotionBlurOpticalFlowEstimator initWithWidth:height:useE5Model:]
+ -[MotionBlurOpticalFlowEstimator releaseResources]
+ -[MotionBlurOpticalFlowEstimator reset]
+ -[MotionBlurOpticalFlowEstimator setFlowHeight:]
+ -[MotionBlurOpticalFlowEstimator setFlowWidth:]
+ -[MotionBlurOpticalFlowEstimator setModelFromDefaults]
+ -[MotionBlurOpticalFlowEstimator setUpscaleFlow:]
+ -[MotionBlurOpticalFlowEstimator setUsage:]
+ -[MotionBlurOpticalFlowEstimator swapFrameBufferReference]
+ -[MotionBlurOpticalFlowEstimator upscaleFlow]
+ -[MotionBlurOpticalFlowEstimator usage]
+ -[MotionBlurProcessor .cxx_destruct]
+ -[MotionBlurProcessor createTextureBufferForTilesWithWidth:height:]
+ -[MotionBlurProcessor createTextureBufferWithWidth:height:]
+ -[MotionBlurProcessor createWithWidth:height:pixelFormat:]
+ -[MotionBlurProcessor initWithDevice:width:height:]
+ -[MotionBlurProcessor searchRange]
+ -[MotionBlurProcessor tileSize]
+ -[MotionBlurProcessor timeScale]
+ -[NeuFlow .cxx_destruct]
+ -[NeuFlow adaptationLayerFeature0]
+ -[NeuFlow adaptationLayerFeature1]
+ -[NeuFlow adaptationLayerInputConcatenatedCostVolume]
+ -[NeuFlow adaptationLayerInputFlow]
+ -[NeuFlow adaptationLayerOutputFlow]
+ -[NeuFlow allocateResources]
+ -[NeuFlow allocateTextures]
+ -[NeuFlow baseLayerHeight]
+ -[NeuFlow baseLayerWidth]
+ -[NeuFlow checkDefaults]
+ -[NeuFlow computeBaseFlowWithIteration:]
+ -[NeuFlow computeCorrelationForAdaptationLayerToCommandBuffer:]
+ -[NeuFlow computeCorrelationToCommandBufferSurface:iterationCount:]
+ -[NeuFlow computeCorrelationWithFirstFeature:secondFeature:flow:warpedFeature:correleation:toCommandBuffer:]
+ -[NeuFlow computeCorrelationWithFirstFeatureSurface:secondFeatureSurface:flowSurface:correleationSurface:toCommandBufferSurface:]
+ -[NeuFlow computeFlowWithIterationAsync:toCommandBuffer:]
+ -[NeuFlow computeFlowWithIterationSync:]
+ -[NeuFlow contextChannels]
+ -[NeuFlow createNetworkModules]
+ -[NeuFlow dealloc]
+ -[NeuFlow executeANEPart1]
+ -[NeuFlow executeANEPart2]
+ -[NeuFlow executeAdaptationLayer]
+ -[NeuFlow featureChannels]
+ -[NeuFlow firstInput]
+ -[NeuFlow initWithMode:]
+ -[NeuFlow initWithMode:].cold.1
+ -[NeuFlow initWithMode:].cold.2
+ -[NeuFlow init]
+ -[NeuFlow initialContext]
+ -[NeuFlow initialFeature0]
+ -[NeuFlow initialFeature1]
+ -[NeuFlow initialFlow]
+ -[NeuFlow initializeModels]
+ -[NeuFlow initializeModels].cold.1
+ -[NeuFlow initializeModels].cold.2
+ -[NeuFlow initializeModels].cold.3
+ -[NeuFlow opticalFlowFirstFrame:secondFrame:flow:]
+ -[NeuFlow opticalFlowFirstFrame:secondFrame:flow:callback:]
+ -[NeuFlow releaseResources]
+ -[NeuFlow secondInput]
+ -[NeuFlow secondStageInputCorrelation]
+ -[NeuFlow secondStageInputFlow]
+ -[NeuFlow secondStageInputInitialContext]
+ -[NeuFlow secondStageInputUpdatedContext]
+ -[NeuFlow secondStageOutputContext]
+ -[NeuFlow secondStageOutputFlow]
+ -[NeuFlow setAdaptationLayerInputFlow:]
+ -[NeuFlow setSecondStageInputInitialContext:]
+ -[NeuFlow setTotalIteration:]
+ -[NeuFlow switchUsageTo:]
+ -[NeuFlow totalIteration]
+ -[NeuFlow warpedFeature]
+ -[OpticalFlow blit]
+ -[OpticalFlow commandQueue]
+ -[OpticalFlow correlation]
+ -[OpticalFlow estimateFlowFromFirstFeatures:secondFeature:storage:outputFlow:callback:]
+ -[OpticalFlow estimateFlowLevel:withEstimator:firstFeatures:secondFeatures:correlation:upscaledFlow:warpedImage:prevFlow:outputFlow:callback:waitForComplete:]
+ -[OpticalFlow estimateStageFlowFromFirstFeatures:secondFeature:storage:baseStage:startLevel:lastLevel:startFlow:outputFlow:callback:]
+ -[OpticalFlow opticalFlowFirstFrame:secondFrame:flow:callback:]
+ -[OpticalFlow postProcessFlow:outputFlow:callback:]
+ -[OpticalFlow reshuffleFlow:previousFlow:destination:callback:waitForComplete:]
+ -[OpticalFlow setCommandQueue:]
+ -[OpticalFlow updateCompletion]
+ -[OpticalFlow updateFlowSizeForLevel3]
+ -[OpticalFlow waitForAllTaskCompletionAsynchronously]
+ -[OpticalFlowE5 allocateResources]
+ -[OpticalFlowE5 checkFlowLevel]
+ -[OpticalFlowE5 copyLinearBufferToTexturebyBLITSource:to:]
+ -[OpticalFlowE5 encodeConvertLinearBuffer:toPixelBuffer:commandBuffer:]
+ -[OpticalFlowE5 isE5OnlyResulution]
+ -[OpticalFlowE5 opticalFlowFirstFrame:secondFrame:flow:callback:]
+ -[OpticalFlowE5 opticalFlowFirstFrame:secondFrame:originalFirst:originalSecond:flow:callback:]
+ -[OpticalFlowE5 releaseResources]
+ -[OpticalFlowE5 upscaleFinalFlow:outFlow:commandBuffer:]
+ -[Synthesis commandQueue]
+ -[Synthesis initWithMode:mtlDevice:commandQueue:]
+ -[Synthesis setCommandQueue:]
+ GCC_except_table20
+ GCC_except_table25
+ GCC_except_table30
+ OBJC_IVAR_$_E5Model._completionEvent
+ OBJC_IVAR_$_E5Model._dependentEvent
+ OBJC_IVAR_$_E5Model._function
+ OBJC_IVAR_$_E5Model._functionNames
+ OBJC_IVAR_$_E5Model._inputPortNames
+ OBJC_IVAR_$_E5Model._inputSurfaces
+ OBJC_IVAR_$_E5Model._input_ports
+ OBJC_IVAR_$_E5Model._library
+ OBJC_IVAR_$_E5Model._logger
+ OBJC_IVAR_$_E5Model._networkInputSize
+ OBJC_IVAR_$_E5Model._networkOutputSize
+ OBJC_IVAR_$_E5Model._num_input_ports
+ OBJC_IVAR_$_E5Model._num_output_ports
+ OBJC_IVAR_$_E5Model._operation
+ OBJC_IVAR_$_E5Model._outputPortNames
+ OBJC_IVAR_$_E5Model._outputSurfaces
+ OBJC_IVAR_$_E5Model._output_ports
+ OBJC_IVAR_$_E5Model._signPostId
+ _CFRetain
+ _FRCGetE5UsageFromSize
+ _GetLog.logger
+ _GetLog.onceToken
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryFromPath
+ _IOSurfaceGetBytesPerRow
+ _IOSurfaceGetHeight
+ _OBJC_CLASS_$_E5Model
+ _OBJC_CLASS_$_FlowUpscaler
+ _OBJC_CLASS_$_IOSurfaceSharedEventListener
+ _OBJC_CLASS_$_MotionBlur
+ _OBJC_CLASS_$_MotionBlurOpticalFlowEstimator
+ _OBJC_CLASS_$_MotionBlurProcessor
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_CLASS_$_NeuFlow
+ _OBJC_IVAR_$_Backwarp._backwarp2CKernel
+ _OBJC_IVAR_$_Backwarp._backwarpLossWithFlowMagnitude2CKernel
+ _OBJC_IVAR_$_Correlation._correlation5x5SIMDKernel
+ _OBJC_IVAR_$_Correlation._correlationWithScaleSIMDKernel
+ _OBJC_IVAR_$_E5Model._IOSurfaceSharedEvent
+ _OBJC_IVAR_$_E5Model._deviceType
+ _OBJC_IVAR_$_E5Model._firstInputSurface
+ _OBJC_IVAR_$_E5Model._inputBufferObject
+ _OBJC_IVAR_$_E5Model._modelName
+ _OBJC_IVAR_$_E5Model._outputBufferObject
+ _OBJC_IVAR_$_E5Model._secondInputSurface
+ _OBJC_IVAR_$_E5Model._stream
+ _OBJC_IVAR_$_FRCBlit._linearBufferToLinearBuffer
+ _OBJC_IVAR_$_FRCBlit._linearBufferToTextureOneComponent
+ _OBJC_IVAR_$_FRCBlit._linearBufferToTextureTwoComponent
+ _OBJC_IVAR_$_FRCBlit._rgTextureToLinearBuffer
+ _OBJC_IVAR_$_FRCBlit._rgbaTextureToLinearBuffer
+ _OBJC_IVAR_$_FRCBlit._textureArrayToLinearBuffer
+ _OBJC_IVAR_$_FRCFrameInterpolator._commandQueue
+ _OBJC_IVAR_$_FRCFrameInterpolator._device
+ _OBJC_IVAR_$_FRCFrameSynthesizer._commandQueue
+ _OBJC_IVAR_$_FRCFrameSynthesizer._device
+ _OBJC_IVAR_$_FRCImageProcessor._commandQueue
+ _OBJC_IVAR_$_FRCMetalBase._commandQueue
+ _OBJC_IVAR_$_FRCOpticalFlowEstimator._completion_semaphore
+ _OBJC_IVAR_$_FRCOpticalFlowEstimator._waitForCompletion
+ _OBJC_IVAR_$_FRCOpticalFlowEstimatorConfiguration._commandQueue
+ _OBJC_IVAR_$_FRCOpticalFlowEstimatorConfiguration._inputDownsampling
+ _OBJC_IVAR_$_FRCOpticalFlowEstimatorConfiguration._waitForCompletion
+ _OBJC_IVAR_$_FlowUpscaler._EnableGpuWaitForComplete
+ _OBJC_IVAR_$_FlowUpscaler._combinedRGBFlowEdge
+ _OBJC_IVAR_$_FlowUpscaler._combinedRGBFlowEdgeTexture
+ _OBJC_IVAR_$_FlowUpscaler._computeRgbFlowEdgeKernel
+ _OBJC_IVAR_$_FlowUpscaler._deblockKernel
+ _OBJC_IVAR_$_FlowUpscaler._dilateEdgeMap
+ _OBJC_IVAR_$_FlowUpscaler._dilateEdgeMapKernel
+ _OBJC_IVAR_$_FlowUpscaler._dilateEdgeMapTexture
+ _OBJC_IVAR_$_FlowUpscaler._downscaleImageKernel
+ _OBJC_IVAR_$_FlowUpscaler._downscalePackedImageKernel
+ _OBJC_IVAR_$_FlowUpscaler._flow1
+ _OBJC_IVAR_$_FlowUpscaler._flow1Texture
+ _OBJC_IVAR_$_FlowUpscaler._flow2
+ _OBJC_IVAR_$_FlowUpscaler._flow2Texture
+ _OBJC_IVAR_$_FlowUpscaler._flowUpscaleHighresUpscaleKernel
+ _OBJC_IVAR_$_FlowUpscaler._flowUpscaleLowresClusterKernel
+ _OBJC_IVAR_$_FlowUpscaler._internalHrFlow
+ _OBJC_IVAR_$_FlowUpscaler._internalHrFlowTexture
+ _OBJC_IVAR_$_FlowUpscaler._internalResult
+ _OBJC_IVAR_$_FlowUpscaler._internalResultTexture
+ _OBJC_IVAR_$_FlowUpscaler._logger
+ _OBJC_IVAR_$_FlowUpscaler._lrFlowHeight
+ _OBJC_IVAR_$_FlowUpscaler._lrFlowWidth
+ _OBJC_IVAR_$_FlowUpscaler._lrRgb
+ _OBJC_IVAR_$_FlowUpscaler._lrRgbTexture
+ _OBJC_IVAR_$_FlowUpscaler._rgb1
+ _OBJC_IVAR_$_FlowUpscaler._rgb1Texture
+ _OBJC_IVAR_$_FlowUpscaler._rgb2
+ _OBJC_IVAR_$_FlowUpscaler._rgb2Texture
+ _OBJC_IVAR_$_FlowUpscaler._signPostId
+ _OBJC_IVAR_$_MotionBlur._commandQueue
+ _OBJC_IVAR_$_MotionBlur._device
+ _OBJC_IVAR_$_MotionBlur._flowToVelocityKernel
+ _OBJC_IVAR_$_MotionBlur._library
+ _OBJC_IVAR_$_MotionBlur._logger
+ _OBJC_IVAR_$_MotionBlur._neighborMaxVelocityKernel
+ _OBJC_IVAR_$_MotionBlur._pipelineLibrary
+ _OBJC_IVAR_$_MotionBlur._searchRange
+ _OBJC_IVAR_$_MotionBlur._tileMaxVelocityKernel
+ _OBJC_IVAR_$_MotionBlur._tileSize
+ _OBJC_IVAR_$_MotionBlur._timeScale
+ _OBJC_IVAR_$_MotionBlurOpticalFlowEstimator._colorPixelBufferRGBA
+ _OBJC_IVAR_$_MotionBlurOpticalFlowEstimator._device
+ _OBJC_IVAR_$_MotionBlurOpticalFlowEstimator._downscaledColorBuffers
+ _OBJC_IVAR_$_MotionBlurOpticalFlowEstimator._flowHeight
+ _OBJC_IVAR_$_MotionBlurOpticalFlowEstimator._flowUpscaler
+ _OBJC_IVAR_$_MotionBlurOpticalFlowEstimator._flowWidth
+ _OBJC_IVAR_$_MotionBlurOpticalFlowEstimator._frameIndex
+ _OBJC_IVAR_$_MotionBlurOpticalFlowEstimator._imageScaler
+ _OBJC_IVAR_$_MotionBlurOpticalFlowEstimator._inputHeight
+ _OBJC_IVAR_$_MotionBlurOpticalFlowEstimator._inputWidth
+ _OBJC_IVAR_$_MotionBlurOpticalFlowEstimator._logger
+ _OBJC_IVAR_$_MotionBlurOpticalFlowEstimator._opticalFlowConfiguration
+ _OBJC_IVAR_$_MotionBlurOpticalFlowEstimator._opticalFlowEstimator
+ _OBJC_IVAR_$_MotionBlurOpticalFlowEstimator._preScaledFlowTexture
+ _OBJC_IVAR_$_MotionBlurOpticalFlowEstimator._preUpscaledFlow
+ _OBJC_IVAR_$_MotionBlurOpticalFlowEstimator._prevColorPixelBufferRGBA
+ _OBJC_IVAR_$_MotionBlurOpticalFlowEstimator._tmpPixelBufferRGBA
+ _OBJC_IVAR_$_MotionBlurOpticalFlowEstimator._upscaleFlow
+ _OBJC_IVAR_$_MotionBlurOpticalFlowEstimator._usage
+ _OBJC_IVAR_$_MotionBlurProcessor._device
+ _OBJC_IVAR_$_MotionBlurProcessor._height
+ _OBJC_IVAR_$_MotionBlurProcessor._logger
+ _OBJC_IVAR_$_MotionBlurProcessor._searchRange
+ _OBJC_IVAR_$_MotionBlurProcessor._tileSize
+ _OBJC_IVAR_$_MotionBlurProcessor._timeScale
+ _OBJC_IVAR_$_MotionBlurProcessor._width
+ _OBJC_IVAR_$_NeuFlow._adaptationCorrelationTexture
+ _OBJC_IVAR_$_NeuFlow._ane1
+ _OBJC_IVAR_$_NeuFlow._ane2
+ _OBJC_IVAR_$_NeuFlow._ane3
+ _OBJC_IVAR_$_NeuFlow._baseLayerHeight
+ _OBJC_IVAR_$_NeuFlow._baseLayerWidth
+ _OBJC_IVAR_$_NeuFlow._contextChannels
+ _OBJC_IVAR_$_NeuFlow._correlationBuffer
+ _OBJC_IVAR_$_NeuFlow._correlationTexture
+ _OBJC_IVAR_$_NeuFlow._feature0Texture
+ _OBJC_IVAR_$_NeuFlow._feature1Texture
+ _OBJC_IVAR_$_NeuFlow._featureChannels
+ _OBJC_IVAR_$_NeuFlow._flowTexture
+ _OBJC_IVAR_$_NeuFlow._logger
+ _OBJC_IVAR_$_NeuFlow._sharedEvent
+ _OBJC_IVAR_$_NeuFlow._sharedEventListener
+ _OBJC_IVAR_$_NeuFlow._signalValue
+ _OBJC_IVAR_$_NeuFlow._synchronizationQueue
+ _OBJC_IVAR_$_NeuFlow._totalIteration
+ _OBJC_IVAR_$_NeuFlow._warpedFeature
+ _OBJC_IVAR_$_Normalization._bypassStatistics
+ _OBJC_IVAR_$_Normalization._denormalizeToMonochromeKernel
+ _OBJC_IVAR_$_Normalization._normalizeMonochromeToPlanarKernel
+ _OBJC_IVAR_$_OpticalFlow._taskCompletionSemaphore
+ _OBJC_IVAR_$_OpticalFlow._taskCompletionUpdateQueue
+ _OBJC_IVAR_$_OpticalFlow._taskCompletionWaitQueue
+ _OBJC_IVAR_$_OpticalFlow._totalTasks
+ _OBJC_IVAR_$_OpticalFlow._totalTasksCompleted
+ _OBJC_IVAR_$_OpticalFlowE5._alignFlowSize
+ _OBJC_IVAR_$_OpticalFlowE5._flowOutputLevel
+ _OBJC_IVAR_$_OpticalFlowE5._level3Flow
+ _OBJC_IVAR_$_OpticalFlowE5._networkInputSize
+ _OBJC_IVAR_$_OpticalFlowE5._networkOutputSize
+ _OBJC_IVAR_$_OpticalFlowE5._opticalFlowModel
+ _OBJC_IVAR_$_OpticalFlowE5._sharedEvent
+ _OBJC_IVAR_$_OpticalFlowE5._sharedEventListener
+ _OBJC_IVAR_$_OpticalFlowE5._signalValue
+ _OBJC_IVAR_$_OpticalFlowE5._synchronizationQueue
+ _OBJC_METACLASS_$_E5Model
+ _OBJC_METACLASS_$_FlowUpscaler
+ _OBJC_METACLASS_$_MotionBlur
+ _OBJC_METACLASS_$_MotionBlurOpticalFlowEstimator
+ _OBJC_METACLASS_$_MotionBlurProcessor
+ _OBJC_METACLASS_$_NeuFlow
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ __OBJC_$_INSTANCE_METHODS_E5Model
+ __OBJC_$_INSTANCE_METHODS_FlowUpscaler
+ __OBJC_$_INSTANCE_METHODS_MotionBlur
+ __OBJC_$_INSTANCE_METHODS_MotionBlurOpticalFlowEstimator
+ __OBJC_$_INSTANCE_METHODS_MotionBlurProcessor
+ __OBJC_$_INSTANCE_METHODS_NeuFlow
+ __OBJC_$_INSTANCE_VARIABLES_E5Model
+ __OBJC_$_INSTANCE_VARIABLES_FlowUpscaler
+ __OBJC_$_INSTANCE_VARIABLES_MotionBlur
+ __OBJC_$_INSTANCE_VARIABLES_MotionBlurOpticalFlowEstimator
+ __OBJC_$_INSTANCE_VARIABLES_MotionBlurProcessor
+ __OBJC_$_INSTANCE_VARIABLES_NeuFlow
+ __OBJC_$_PROP_LIST_Backwarp
+ __OBJC_$_PROP_LIST_E5Model
+ __OBJC_$_PROP_LIST_FRCMetalBase
+ __OBJC_$_PROP_LIST_FlowUpscaler
+ __OBJC_$_PROP_LIST_MotionBlurOpticalFlowEstimator
+ __OBJC_$_PROP_LIST_NeuFlow
+ __OBJC_CLASS_RO_$_E5Model
+ __OBJC_CLASS_RO_$_FlowUpscaler
+ __OBJC_CLASS_RO_$_MotionBlur
+ __OBJC_CLASS_RO_$_MotionBlurOpticalFlowEstimator
+ __OBJC_CLASS_RO_$_MotionBlurProcessor
+ __OBJC_CLASS_RO_$_NeuFlow
+ __OBJC_METACLASS_RO_$_E5Model
+ __OBJC_METACLASS_RO_$_FlowUpscaler
+ __OBJC_METACLASS_RO_$_MotionBlur
+ __OBJC_METACLASS_RO_$_MotionBlurOpticalFlowEstimator
+ __OBJC_METACLASS_RO_$_MotionBlurProcessor
+ __OBJC_METACLASS_RO_$_NeuFlow
+ ___133-[OpticalFlow estimateStageFlowFromFirstFeatures:secondFeature:storage:baseStage:startLevel:lastLevel:startFlow:outputFlow:callback:]_block_invoke
+ ___133-[OpticalFlow estimateStageFlowFromFirstFeatures:secondFeature:storage:baseStage:startLevel:lastLevel:startFlow:outputFlow:callback:]_block_invoke_2
+ ___158-[OpticalFlow estimateFlowLevel:withEstimator:firstFeatures:secondFeatures:correlation:upscaledFlow:warpedImage:prevFlow:outputFlow:callback:waitForComplete:]_block_invoke
+ ___24-[E5Model executeAsync:]_block_invoke
+ ___24-[E5Model executeAsync:]_block_invoke.cold.1
+ ___24-[E5Model executeAsync:]_block_invoke.cold.2
+ ___31-[OpticalFlow updateCompletion]_block_invoke
+ ___46-[FRCOpticalFlowEstimator opticalFlowFrom:to:]_block_invoke
+ ___51-[OpticalFlow postProcessFlow:outputFlow:callback:]_block_invoke
+ ___51-[OpticalFlow postProcessFlow:outputFlow:callback:]_block_invoke_2
+ ___53-[OpticalFlow waitForAllTaskCompletionAsynchronously]_block_invoke
+ ___53-[OpticalFlow waitForAllTaskCompletionAsynchronously]_block_invoke_2
+ ___54-[FRCLivePhotoMetadataReader parseStillImageMetadata:]_block_invoke
+ ___58-[FlowUpscaler upscaleRefinedFloV2With:RGB:lrFlow:output:]_block_invoke
+ ___59-[NeuFlow opticalFlowFirstFrame:secondFrame:flow:callback:]_block_invoke
+ ___60-[FRCLivePhotoMetadataReader createMetadataAdaptorForAsset:]_block_invoke
+ ___63-[OpticalFlow opticalFlowFirstFrame:secondFrame:flow:callback:]_block_invoke
+ ___69-[FRCOpticalFlowEstimator opticalFlowFrom:to:flow:completionHandler:]_block_invoke
+ ___71-[OpticalFlowE5 encodeConvertLinearBuffer:toPixelBuffer:commandBuffer:]_block_invoke
+ ___78-[FlowUpscaler flowUpscalingFromImage:inputFlow:outputFlow:completionHandler:]_block_invoke
+ ___79-[OpticalFlow reshuffleFlow:previousFlow:destination:callback:waitForComplete:]_block_invoke
+ ___84-[OpticalFlow opticalFlowFirstFrame:secondFrame:flowForward:flowBackward:reUseFlow:]_block_invoke
+ ___87-[OpticalFlow estimateFlowFromFirstFeatures:secondFeature:storage:outputFlow:callback:]_block_invoke
+ ___87-[OpticalFlow estimateFlowFromFirstFeatures:secondFeature:storage:outputFlow:callback:]_block_invoke_2
+ ___94-[OpticalFlowE5 opticalFlowFirstFrame:secondFrame:originalFirst:originalSecond:flow:callback:]_block_invoke
+ ___GetLog_block_invoke
+ ___NSDictionary0__struct
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_41_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e29_v24?0"NSArray"8"NSError"16lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32s_e14_v28?0Q8Q16i24ls32l8
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s_e33_v24?0"IOSurfaceSharedEvent"8Q16ls32l8
+ __os_signpost_emit_with_name_impl
+ _createBufferFromFile
+ _createFP16TextureFromIOSurface
+ _dispatch_async
+ _e5rt_async_event_create_from_iosurface_shared_event
+ _e5rt_async_event_set_active_future_value
+ _e5rt_buffer_object_create_from_iosurface
+ _e5rt_e5_compiler_options_set_mil_entry_points
+ _e5rt_execution_stream_submit_async
+ _e5rt_program_library_get_function_names
+ _e5rt_program_library_get_num_functions
+ _getSoCGeneration
+ _gettimeofday
+ _isCopyNecessaryForCVtoTextureArray
+ _kIOMainPortDefault
+ _objc_msgSend$EnableGpuWaitForComplete
+ _objc_msgSend$IOSurfaceSharedEvent
+ _objc_msgSend$adaptationLayerFeature0
+ _objc_msgSend$adaptationLayerFeature1
+ _objc_msgSend$adaptationLayerInputConcatenatedCostVolume
+ _objc_msgSend$adaptationLayerOutputFlow
+ _objc_msgSend$allocateHRFlowBufferWithHrWidth:hrHeight:
+ _objc_msgSend$allocateInternalBuffersWithLrWidth:lrHeight:hrWidth:hrHeight:
+ _objc_msgSend$allocateTextures
+ _objc_msgSend$blit
+ _objc_msgSend$checkFlowLevel
+ _objc_msgSend$commandBufferWait:flag:
+ _objc_msgSend$commandQueue
+ _objc_msgSend$compare:
+ _objc_msgSend$computeCorrelationForAdaptationLayerToCommandBuffer:
+ _objc_msgSend$computeCorrelationToCommandBufferSurface:iterationCount:
+ _objc_msgSend$computeCorrelationWithFirstFeature:secondFeature:flow:warpedFeature:correleation:toCommandBuffer:
+ _objc_msgSend$computeCorrelationWithFirstFeatureSurface:secondFeatureSurface:flowSurface:correleationSurface:toCommandBufferSurface:
+ _objc_msgSend$computeFlowWithIterationAsync:toCommandBuffer:
+ _objc_msgSend$computeFlowWithIterationSync:
+ _objc_msgSend$computePipelineStateFor:withConstants:
+ _objc_msgSend$copyLinearBuffer:toLinearBuffer:commandBuffer:
+ _objc_msgSend$copyLinearBuffer:toTexture:commandBuffer:
+ _objc_msgSend$copyTexture:toLinearBuffer:commandBuffer:
+ _objc_msgSend$correlation
+ _objc_msgSend$createFunctionListFromLibrary
+ _objc_msgSend$createNetworkModules
+ _objc_msgSend$createWithWidth:height:pixelFormat:
+ _objc_msgSend$description
+ _objc_msgSend$encode5x5ToCommandBuffer:first:second:flow:destination:
+ _objc_msgSend$encodeComputeRGBandFlowEdgeToCommandBuffer:rgb:flow:destination:edgeThresh:
+ _objc_msgSend$encodeConvertLinearBuffer:toPixelBuffer:commandBuffer:
+ _objc_msgSend$encodeDeblockToCommandBuffer:flow:output:upscaleFactor:
+ _objc_msgSend$encodeDilateEdgeMapToCommandBuffer:input:destination:
+ _objc_msgSend$encodeDownscaleImageToCommandBuffer:input:output:
+ _objc_msgSend$encodeHighUpscaleToCommandBuffer:lrFlow:rgbFlowEdge:hrImage:flow1:flow2:rgb1:rgb2:internalResult:hrFlow:
+ _objc_msgSend$encodeLowResClusterToCommandBuffer:lrFlow:lrImage:rgbFlowEdge:flow1:flow2:rgb1:rgb2:internalResult:
+ _objc_msgSend$encodeNeighborMaxFlowWithCommandBuffer:tileMax:searchRange:neighborMax:
+ _objc_msgSend$encodeStream
+ _objc_msgSend$encodeTileMaxVelocityWithCommandBuffer:velocity:tileSize:tileMax:
+ _objc_msgSend$encodeToCommandBuffer:first:second:destination:scaleInput:
+ _objc_msgSend$encodeToCommandBuffer:source:flow:destination:
+ _objc_msgSend$encodeVelocityForMotionBlurWithCommandBuffer:displacement:velocity:timeScale:tileSize:searchRange:
+ _objc_msgSend$estimateFlowFromFirstFeatures:secondFeature:storage:outputFlow:callback:
+ _objc_msgSend$estimateFlowLevel:withEstimator:firstFeatures:secondFeatures:correlation:upscaledFlow:warpedImage:prevFlow:outputFlow:callback:waitForComplete:
+ _objc_msgSend$estimateStageFlowFromFirstFeatures:secondFeature:storage:baseStage:startLevel:lastLevel:startFlow:outputFlow:callback:
+ _objc_msgSend$executeANEPart1
+ _objc_msgSend$executeANEPart2
+ _objc_msgSend$executeAdaptationLayer
+ _objc_msgSend$executeAsync:
+ _objc_msgSend$executeSync
+ _objc_msgSend$firstInput
+ _objc_msgSend$firstInputSurface
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$flowUpscalingFromImage:inputFlow:outputFlow:completionHandler:
+ _objc_msgSend$functionName:
+ _objc_msgSend$getPortShape:width:height:channels:bytesPerComponent:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$initWithLrWidth:lrHeight:hrWidth:hrHeight:
+ _objc_msgSend$initWithMode:mtlDevice:commandQueue:
+ _objc_msgSend$initWithModel:
+ _objc_msgSend$initWithUsage:qualityMode:normalizationMode:
+ _objc_msgSend$initWithWidth:height:commandQueue:e5Model:
+ _objc_msgSend$initWithWidth:height:e5Model:
+ _objc_msgSend$initWithWidth:height:useE5Model:
+ _objc_msgSend$initialContext
+ _objc_msgSend$initialFeature0
+ _objc_msgSend$initialFeature1
+ _objc_msgSend$initialFlow
+ _objc_msgSend$initializeFunction:
+ _objc_msgSend$initializeFunctionForUsage:
+ _objc_msgSend$initializeLibrary:
+ _objc_msgSend$initializeModels
+ _objc_msgSend$inputDownsampling
+ _objc_msgSend$inputIOSurface:
+ _objc_msgSend$inputSize:
+ _objc_msgSend$isE5OnlyResulution
+ _objc_msgSend$linearTextureArrayAlignmentBytes
+ _objc_msgSend$linearTextureArrayAlignmentSlice
+ _objc_msgSend$loadTracksWithMediaType:completionHandler:
+ _objc_msgSend$localizedCaseInsensitiveContainsString:
+ _objc_msgSend$matchFlow:toFullSizeFlow:callback:
+ _objc_msgSend$modelName
+ _objc_msgSend$newComputePipelineStateWithDescriptor:error:
+ _objc_msgSend$opticalFlowFirstFrame:secondFrame:flow:callback:
+ _objc_msgSend$opticalFlowFirstFrame:secondFrame:originalFirst:originalSecond:flow:callback:
+ _objc_msgSend$opticalFlowFrom:to:
+ _objc_msgSend$opticalFlowFrom:to:flow:completionHandler:
+ _objc_msgSend$outputIOSurface:
+ _objc_msgSend$outputSize:
+ _objc_msgSend$postProcessFlow:outputFlow:callback:
+ _objc_msgSend$rangeAtIndex:
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$releaseBufferAndTexture
+ _objc_msgSend$releaseE5Resoruces
+ _objc_msgSend$reshuffleFlow:previousFlow:destination:callback:waitForComplete:
+ _objc_msgSend$secondInput
+ _objc_msgSend$secondInputSurface
+ _objc_msgSend$secondStageInputCorrelation
+ _objc_msgSend$secondStageInputFlow
+ _objc_msgSend$secondStageInputUpdatedContext
+ _objc_msgSend$secondStageOutputContext
+ _objc_msgSend$secondStageOutputFlow
+ _objc_msgSend$setAdaptationLayerInputFlow:
+ _objc_msgSend$setCommandQueue:
+ _objc_msgSend$setDeviceType:
+ _objc_msgSend$setE5Model:
+ _objc_msgSend$setIOSurfaceSharedEvent:
+ _objc_msgSend$setInputIOSurface:index:
+ _objc_msgSend$setLabel:
+ _objc_msgSend$setMipmapLevelCount:
+ _objc_msgSend$setMode:
+ _objc_msgSend$setModelFromDefaults
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setOutputPixelFormat:
+ _objc_msgSend$setPipelineLibrary:
+ _objc_msgSend$setResourceOptions:
+ _objc_msgSend$setSecondStageInputInitialContext:
+ _objc_msgSend$setStreamingMode:
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$updateCompletion
+ _objc_msgSend$updateFlowSizeForLevel3
+ _objc_msgSend$upscaleFinalFlow:outFlow:commandBuffer:
+ _objc_msgSend$upscaleRefinedFloV2With:RGB:lrFlow:output:
+ _objc_msgSend$waitForAllTaskCompletionAsynchronously
+ _objc_msgSend$waitForCompletion
+ _object_getClassName
+ _os_signpost_enabled
+ _os_signpost_id_generate
- -[FRCOpticalFlowEstimator matchFlow:]
- -[FRCOpticalFlowEstimator matchFlow:toFullSizeFlow:]
- -[OpticalFlow estimateFlowLevel:withEstimator:firstFeatures:secondFeatures:correlation:upscaledFlow:warpedImage:prevFlow:outputFlow:waitForComplete:]
- -[OpticalFlow estimateStageFlowFromFirstFeatures:secondFeature:storage:baseStage:startLevel:lastLevel:startFlow:outputFlow:]
- -[OpticalFlow postProcessFlow:outputFlow:]
- -[OpticalFlow reshuffleFlow:previousFlow:destination:waitForComplete:]
- -[OpticalFlowE5 allocateBufferObjects]
- -[OpticalFlowE5 bindPorts]
- -[OpticalFlowE5 buildLibraryForModel:]
- -[OpticalFlowE5 buildLibraryForModel:].cold.1
- -[OpticalFlowE5 buildLibraryFromE5BundleForModel:]
- -[OpticalFlowE5 buildLibraryFromE5BundleForModel:].cold.1
- -[OpticalFlowE5 createFP16TextureFromIOSurface:width:height:channels:]
- -[OpticalFlowE5 encodeConvertLinearBuffer:toPixelBuffer:]
- -[OpticalFlowE5 executeModel]
- -[OpticalFlowE5 executeModel].cold.1
- -[OpticalFlowE5 getPortNames]
- -[OpticalFlowE5 initializeModel:]
- -[OpticalFlowE5 initializeModel:].cold.1
- -[OpticalFlowE5 opticalFlowFirstFrame:secondFrame:originalFirst:originalSecond:flow:]
- -[OpticalFlowE5 releaseBufferObjects]
- -[OpticalFlowE5 resetStream:]
- GCC_except_table29
- OBJC_IVAR_$_FRCMetalBase._commandQueue
- _FRCGetUsageFromSizeE5
- _OBJC_IVAR_$_FRCOpticalFlowEstimator._bypassInputNormalization
- _OBJC_IVAR_$_OpticalFlowE5._backwarp
- _OBJC_IVAR_$_OpticalFlowE5._fidelityWeightBufferObject
- _OBJC_IVAR_$_OpticalFlowE5._function
- _OBJC_IVAR_$_OpticalFlowE5._inputBufferObject
- _OBJC_IVAR_$_OpticalFlowE5._inputPortNames
- _OBJC_IVAR_$_OpticalFlowE5._inputSize
- _OBJC_IVAR_$_OpticalFlowE5._input_ports
- _OBJC_IVAR_$_OpticalFlowE5._library
- _OBJC_IVAR_$_OpticalFlowE5._num_input_ports
- _OBJC_IVAR_$_OpticalFlowE5._operation
- _OBJC_IVAR_$_OpticalFlowE5._outputBufferObject
- _OBJC_IVAR_$_OpticalFlowE5._outputPortName
- _OBJC_IVAR_$_OpticalFlowE5._outputSize
- _OBJC_IVAR_$_OpticalFlowE5._output_port
- _OBJC_IVAR_$_OpticalFlowE5._stream
- _OBJC_IVAR_$_OpticalFlowE5._subsampledOriginalFirst
- _OBJC_IVAR_$_OpticalFlowE5._subsampledOriginalSecond
- ___149-[OpticalFlow estimateFlowLevel:withEstimator:firstFeatures:secondFeatures:correlation:upscaledFlow:warpedImage:prevFlow:outputFlow:waitForComplete:]_block_invoke
- ___42-[OpticalFlow postProcessFlow:outputFlow:]_block_invoke
- _e5rt_async_event_create
- _getPortShape
- _getPortShape.cold.1
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$bundleWithIdentifier:
- _objc_msgSend$createFP16TextureFromIOSurface:width:height:channels:
- _objc_msgSend$encodeConvertLinearBuffer:toPixelBuffer:
- _objc_msgSend$encodeUnormNormalize:destination:toCommandBuffer:
- _objc_msgSend$estimateFlowLevel:withEstimator:firstFeatures:secondFeatures:correlation:upscaledFlow:warpedImage:prevFlow:outputFlow:waitForComplete:
- _objc_msgSend$estimateStageFlowFromFirstFeatures:secondFeature:storage:baseStage:startLevel:lastLevel:startFlow:outputFlow:
- _objc_msgSend$executeModel
- _objc_msgSend$initializeModel:
- _objc_msgSend$matchFlow:toFullSizeFlow:
- _objc_msgSend$opticalFlowFirstFrame:secondFrame:flow:
- _objc_msgSend$opticalFlowFirstFrame:secondFrame:originalFirst:originalSecond:flow:
- _objc_msgSend$postProcessFlow:outputFlow:
- _objc_msgSend$releaseAdaptationLayerStorage
- _objc_msgSend$reshuffleFlow:previousFlow:destination:waitForComplete:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x6
- _objc_retain_x7
CStrings:
+ "\t%d: %s\n"
+ "\n"
+ "\"A2"
+ "-[MotionBlur encodeNeighborMaxFlowWithCommandBuffer:tileMax:searchRange:neighborMax:]"
+ "-[MotionBlur encodeTileMaxVelocityWithCommandBuffer:velocity:tileSize:tileMax:]"
+ "-[MotionBlur encodeVelocityForMotionBlurWithCommandBuffer:displacement:velocity:timeScale:tileSize:searchRange:]"
+ ">> ERROR: Failed to create 5x5 correlation kernel"
+ ">> ERROR: Failed to create backwarp 2D"
+ ">> ERROR: Failed to create backwarpLossWithFlowMagnitude2 kernel"
+ ">> ERROR: Failed to create correlation kernel"
+ ">> ERROR: Failed to create correlation with scale kernel"
+ "@\"<MTLPipelineLibrarySPI>\""
+ "@\"<MTLSharedEventSPI>\""
+ "@\"E5Model\""
+ "@\"FRCOpticalFlowEstimator\""
+ "@\"FRCOpticalFlowEstimatorConfiguration\""
+ "@\"FlowUpscaler\""
+ "@\"IOSurfaceSharedEvent\""
+ "@\"IOSurfaceSharedEventListener\""
+ "@24@0:8i16i20"
+ "@28@0:8i16i20B24"
+ "@32@0:8i16i20@24"
+ "@40@0:8i16i20@24@32"
+ "@40@0:8q16@24@32"
+ "@40@0:8q16q24q32"
+ "@48@0:8Q16Q24Q32Q40"
+ "@60@0:8@16@24@32@40f48i52i56"
+ "ANE Done Signaling %lld"
+ "Async execution callback returned error code = %d. msg = %s\n"
+ "Available functions:"
+ "B24@0:8Q16"
+ "B32@0:8@16q24"
+ "B32@0:8q16@24"
+ "B56@0:8^{__IOSurface=}16^{__IOSurface=}24^{__IOSurface=}32^{__IOSurface=}40@48"
+ "B56@0:8^{e5rt_io_port=}16^Q24^Q32^Q40^Q48"
+ "B64@0:8@16@24@32@40@48@56"
+ "Building model from %@"
+ "Building network from %@"
+ "CPU"
+ "Cannot find network model in %@"
+ "E5 Model: %@"
+ "E5 async call failed. returned error = %u. msg = %s\n"
+ "E5 pre process"
+ "E5Model"
+ "EnableGpuWaitForComplete"
+ "Error loading metadata tracks: %@"
+ "Error!  Failed to create opticalFlowEstimator"
+ "Error! Tensor dtype is %ld bits. Must be fp16"
+ "Error! The same buffer is used as the previous call"
+ "Error! To use the async mothod, do not call createReferenceFrameBufferwithWidth:width:height:"
+ "FRC"
+ "FRC::bufferToTexture"
+ "FRC::bufferToTwoComponentTexture"
+ "FRC::compute_rgb_flow_edge"
+ "FRC::deblock"
+ "FRC::dilate_edge_map"
+ "FRC::downscaleImage"
+ "FRC::downscalePackedImage"
+ "FRC::flowUpscaleHighresUpscale"
+ "FRC::flowUpscaleLowresCluster"
+ "FRC::linearBufferToLinearBuffer"
+ "FRC::linearBufferToOneComponentTexture"
+ "FRC::linearBufferToTwoComponentTexture"
+ "FRC::rgTextureToLineraBuffer"
+ "FRC::rgbaBufferToLineraBuffer"
+ "FRC::textureArrayToLinearBuffer"
+ "FRC::textureToBuffer"
+ "FRC::twoComponentTextureToBuffer"
+ "FRCInternal"
+ "Failed to create E5 Model"
+ "FlowUpscale buffer Init failed"
+ "FlowUpscale_Init"
+ "FlowUpscale_UpscaleFlow"
+ "FlowUpscaler"
+ "FlowUpscaler created successfully: (%ld x %ld) to (%ld x %ld)"
+ "Forcing MotionBlur Flow to %@"
+ "Framework bundle path: %@"
+ "H(\\d+)"
+ "IODeviceTree:/arm-io"
+ "IOSurfaceSharedEvent"
+ "IOSurfaceSharedEvent is not set"
+ "Input Width=%{public,name=sourceWidth}ld Input Height=%{public,name=sourceHeight}ld"
+ "Input image[%d] %@: %ld x %ld x %ld"
+ "JiandongDBG: ####2-0-2"
+ "JiandongDBG: ####2-a2 %.2f"
+ "Level %ld Flow"
+ "Model init failed"
+ "MotionBlur"
+ "MotionBlur.m"
+ "MotionBlurFlowModel"
+ "MotionBlurOpticalFlowEstimator"
+ "MotionBlurProcessor"
+ "NeuFlow"
+ "NeuFlow (ANE+GPU) created successfully"
+ "NeuFlow2Lite"
+ "NeuFlowIteration"
+ "Neuflow2_s8_ctx_flowAttn_lite_432x768_landscape_1x_s8Refine_ML_lv1flow_part1_ANE"
+ "Neuflow2_s8_ctx_flowAttn_lite_432x768_landscape_1x_s8Refine_ML_lv1flow_part2_ANE"
+ "Neuflow2_s8_ctx_flowAttn_lite_432x768_landscape_1x_s8Refine_ML_lv1flow_part3_ANE"
+ "Number of Output Ports = %ld"
+ "Output Flow[%d] %@: %ld x %ld x %ld"
+ "Port is a surface type"
+ "Port is a tensor type"
+ "R"
+ "Resetting state"
+ "T@\"<MTLCommandQueue>\",&,N,V_commandQueue"
+ "T@\"Correlation\",R,N,V_correlation"
+ "T@\"FRCBlit\",R,N,V_blit"
+ "T@\"IOSurfaceSharedEvent\",&,N,V_IOSurfaceSharedEvent"
+ "T@\"NSString\",R,N,V_modelName"
+ "TB,N,V_EnableGpuWaitForComplete"
+ "TB,N,V_inputDownsampling"
+ "TB,N,V_upscaleFlow"
+ "TQ,R,N,V_baseLayerHeight"
+ "TQ,R,N,V_baseLayerWidth"
+ "TQ,R,N,V_contextChannels"
+ "TQ,R,N,V_featureChannels"
+ "T^{__IOSurface=},N,V_firstInputSurface"
+ "T^{__IOSurface=},N,V_secondInputSurface"
+ "Taks completion wait"
+ "Task completion update"
+ "The model does not support level2 flow. forcing to level 1 flow"
+ "Ti,N,V_deviceType"
+ "Ti,N,V_flowHeight"
+ "Ti,N,V_flowWidth"
+ "Tq,N,V_totalIteration"
+ "Unable to create pipelineState (%s): %s"
+ "[1^{e5rt_async_event}]"
+ "[6^{__IOSurface}]"
+ "[6^{e5rt_buffer_object}]"
+ "[6^{e5rt_io_port}]"
+ "[6{?=\"width\"Q\"height\"Q\"channels\"Q}]"
+ "^{__CVBuffer=}24@0:8i16i20"
+ "^{__CVBuffer=}32@0:8^{__CVBuffer=}16@?24"
+ "^{__IOSurface=}24@0:8@16"
+ "^{__IOSurface=}24@0:8q16"
+ "^{e5rt_async_event=}"
+ "_EnableGpuWaitForComplete"
+ "_IOSurfaceSharedEvent"
+ "_adaptationCorrelationTexture"
+ "_alignFlowSize"
+ "_ane1"
+ "_ane2"
+ "_ane3"
+ "_backwarp2CKernel"
+ "_backwarpLossWithFlowMagnitude2CKernel"
+ "_baseLayerHeight"
+ "_baseLayerWidth"
+ "_bypassStatistics"
+ "_colorPixelBufferRGBA"
+ "_combinedRGBFlowEdge"
+ "_combinedRGBFlowEdgeTexture"
+ "_completionEvent"
+ "_computeRgbFlowEdgeKernel"
+ "_contextChannels"
+ "_correlation5x5SIMDKernel"
+ "_correlationBuffer"
+ "_correlationTexture"
+ "_correlationWithScaleSIMDKernel"
+ "_deblockKernel"
+ "_denormalizeToMonochromeKernel"
+ "_dependentEvent"
+ "_dilateEdgeMap"
+ "_dilateEdgeMapKernel"
+ "_dilateEdgeMapTexture"
+ "_downscaleImageKernel"
+ "_downscalePackedImageKernel"
+ "_downscaledColorBuffers"
+ "_feature0Texture"
+ "_feature1Texture"
+ "_featureChannels"
+ "_firstInputSurface"
+ "_flow1"
+ "_flow1Texture"
+ "_flow2"
+ "_flow2Texture"
+ "_flowOutputLevel"
+ "_flowTexture"
+ "_flowToVelocityKernel"
+ "_flowUpscaleHighresUpscaleKernel"
+ "_flowUpscaleLowresClusterKernel"
+ "_flowUpscaler"
+ "_functionNames"
+ "_imageScaler"
+ "_inputDownsampling"
+ "_inputSurfaces"
+ "_internalHrFlow"
+ "_internalHrFlowTexture"
+ "_internalResult"
+ "_internalResultTexture"
+ "_level3Flow"
+ "_linearBufferToLinearBuffer"
+ "_linearBufferToTextureOneComponent"
+ "_linearBufferToTextureTwoComponent"
+ "_lrFlowHeight"
+ "_lrFlowWidth"
+ "_lrRgb"
+ "_lrRgbTexture"
+ "_modelName"
+ "_neighborMaxVelocityKernel"
+ "_networkInputSize"
+ "_networkOutputSize"
+ "_normalizeMonochromeToPlanarKernel"
+ "_num_output_ports"
+ "_opticalFlowConfiguration"
+ "_opticalFlowEstimator"
+ "_opticalFlowModel"
+ "_outputPortNames"
+ "_outputSurfaces"
+ "_output_ports"
+ "_pipelineLibrary"
+ "_preScaledFlowTexture"
+ "_preUpscaledFlow"
+ "_prevColorPixelBufferRGBA"
+ "_rgTextureToLinearBuffer"
+ "_rgb1"
+ "_rgb1Texture"
+ "_rgb2"
+ "_rgb2Texture"
+ "_rgbaTextureToLinearBuffer"
+ "_searchRange"
+ "_secondInputSurface"
+ "_signPostId"
+ "_taskCompletionSemaphore"
+ "_taskCompletionUpdateQueue"
+ "_taskCompletionWaitQueue"
+ "_textureArrayToLinearBuffer"
+ "_tileMaxVelocityKernel"
+ "_tileSize"
+ "_timeScale"
+ "_tmpPixelBufferRGBA"
+ "_totalIteration"
+ "_totalTasks"
+ "_totalTasksCompleted"
+ "_upscaleFlow"
+ "_warpedFeature"
+ "adaptationLayerFeature0"
+ "adaptationLayerFeature1"
+ "adaptationLayerInputConcatenatedCostVolume"
+ "adaptationLayerInputFlow"
+ "adaptationLayerOutputFlow"
+ "allocateHRFlowBufferWithHrWidth:hrHeight:"
+ "allocateInternalBuffersWithLrWidth:lrHeight:hrWidth:hrHeight:"
+ "allocateTextures"
+ "backwarp2C"
+ "backwarpLossWithFlow2CMagnitude"
+ "baseLayerHeight"
+ "baseLayerWidth"
+ "blit"
+ "checkFlowLevel"
+ "com.FRC.NeuFlow"
+ "com.FRC.OpticalFlowE5"
+ "commandBufferWait:flag:"
+ "commandQueue"
+ "compare:"
+ "completion Event"
+ "computeBaseFlowWithIteration:"
+ "computeCorrelationForAdaptationLayerToCommandBuffer:"
+ "computeCorrelationToCommandBufferSurface:iterationCount:"
+ "computeCorrelationWithFirstFeature:secondFeature:flow:warpedFeature:correleation:toCommandBuffer:"
+ "computeCorrelationWithFirstFeatureSurface:secondFeatureSurface:flowSurface:correleationSurface:toCommandBufferSurface:"
+ "computeFlowWithIterationAsync:toCommandBuffer:"
+ "computeFlowWithIterationSync:"
+ "computeOpticalFlowFrom:"
+ "computeOpticalFlowFrom:flow:completionHandler:"
+ "computePipelineStateFor:withConstants:"
+ "computeVelocityMapWithDisplacement:outVelocity:outNeighborMaxVelocity:tileMax:"
+ "contextChannels"
+ "copyLinearBuffer:toLinearBuffer:commandBuffer:"
+ "copyLinearBuffer:toTexture:commandBuffer:"
+ "copyLinearBufferToTexturebyBLITSource:to:"
+ "copyTexture:toLinearBuffer:commandBuffer:"
+ "correlation"
+ "correlation5x5SIMD"
+ "createFunctionListFromLibrary"
+ "createNetworkModules"
+ "createReferenceFrameBufferwithWidth:height:"
+ "createTextureBufferForTilesWithWidth:height:"
+ "createTextureBufferWithWidth:height:"
+ "createWithWidth:height:pixelFormat:"
+ "denormalizeToMonochrome"
+ "deviceType"
+ "e5rt_async_event_create_from_iosurface_shared_event(&_completionEvent, \"completion Event\", self.IOSurfaceSharedEvent)"
+ "e5rt_async_event_create_from_iosurface_shared_event(&_dependentEvent[0], \"dependent Event\", self.IOSurfaceSharedEvent)"
+ "e5rt_buffer_object_create_from_iosurface(&_inputBufferObject[index], surface)"
+ "e5rt_buffer_object_create_from_iosurface(&_outputBufferObject[index], surface)"
+ "e5rt_buffer_object_get_iosurface(_inputBufferObject[inputIdx], &_inputSurfaces[inputIdx])"
+ "e5rt_buffer_object_get_iosurface(_outputBufferObject[outputIdx], &_outputSurfaces[outputIdx])"
+ "e5rt_e5_compiler_options_set_mil_entry_points(options, entry_points, 1)"
+ "e5rt_execution_stream_operation_bind_completion_event(_operation, _completionEvent)"
+ "e5rt_execution_stream_operation_bind_dependent_events(_operation, _dependentEvent, 1)"
+ "e5rt_execution_stream_operation_retain_output_port(_operation, _outputPortNames[outputIdx].UTF8String, &_output_ports[outputIdx])"
+ "e5rt_io_port_bind_buffer_object(_output_ports[i], _outputBufferObject[i])"
+ "e5rt_io_port_retain_tensor_desc(_output_ports[outputIdx], &output_tensor_desc)"
+ "e5rt_program_library_retain_program_function(_library, functionName.UTF8String, &_function)"
+ "e5rt_tensor_desc_alloc_buffer_object(output_tensor_desc, E5RT_BUFFER_OBJECT_TYPE_IOSURFACE, 1, &_outputBufferObject[outputIdx])"
+ "enableInputScale"
+ "encode5x5ToCommandBuffer:first:second:flow:destination:"
+ "encodeComputeRGBandFlowEdgeToCommandBuffer:rgb:flow:destination:edgeThresh:"
+ "encodeConvertLinearBuffer:toPixelBuffer:commandBuffer:"
+ "encodeDeblockToCommandBuffer:flow:output:upscaleFactor:"
+ "encodeDilateEdgeMapToCommandBuffer:input:destination:"
+ "encodeDownscaleImageToCommandBuffer:input:output:"
+ "encodeHighUpscaleToCommandBuffer:lrFlow:rgbFlowEdge:hrImage:flow1:flow2:rgb1:rgb2:internalResult:hrFlow:"
+ "encodeLowResClusterToCommandBuffer:lrFlow:lrImage:rgbFlowEdge:flow1:flow2:rgb1:rgb2:internalResult:"
+ "encodeNeighborMaxFlowWithCommandBuffer:tileMax:searchRange:neighborMax:"
+ "encodeStream"
+ "encodeTileMaxVelocityWithCommandBuffer:velocity:tileSize:tileMax:"
+ "encodeToCommandBuffer:first:second:destination:scaleInput:"
+ "encodeToCommandBuffer:source:flow:destination:"
+ "encodeVelocityForMotionBlurWithCommandBuffer:displacement:velocity:timeScale:tileSize:searchRange:"
+ "estimateFlowFromFirstFeatures:secondFeature:storage:outputFlow:callback:"
+ "estimateFlowLevel:withEstimator:firstFeatures:secondFeatures:correlation:upscaledFlow:warpedImage:prevFlow:outputFlow:callback:waitForComplete:"
+ "estimateStageFlowFromFirstFeatures:secondFeature:storage:baseStage:startLevel:lastLevel:startFlow:outputFlow:callback:"
+ "executeANEPart1"
+ "executeANEPart2"
+ "executeAdaptationLayer"
+ "executeAsync:"
+ "executeSync"
+ "faild to create adaptation layer model"
+ "faild to create first model"
+ "faild to create modules"
+ "faild to create second model"
+ "failed to build library for %@"
+ "failed to get surface format"
+ "featureChannels"
+ "firstInput"
+ "firstInputSurface"
+ "firstMatchInString:options:range:"
+ "flowToVelocityConversion"
+ "flowUpscalingFromImage:inputFlow:outputFlow:completionHandler:"
+ "functionName:"
+ "getPortShape:width:height:channels:bytesPerComponent:"
+ "initWithCapacity:"
+ "initWithData:encoding:"
+ "initWithDevice:commandQueue:library:pipelineLibrary:timeScale:tileSize:searchRange:"
+ "initWithDevice:width:height:"
+ "initWithLrWidth:lrHeight:hrWidth:hrHeight:"
+ "initWithMode:mtlDevice:commandQueue:"
+ "initWithModel:"
+ "initWithUsage:qualityMode:bypassFrameStats:"
+ "initWithUsage:qualityMode:normalizationMode:"
+ "initWithWidth:height:"
+ "initWithWidth:height:commandQueue:"
+ "initWithWidth:height:commandQueue:e5Model:"
+ "initWithWidth:height:e5Model:"
+ "initWithWidth:height:useE5Model:"
+ "initialContext"
+ "initialFeature0"
+ "initialFeature1"
+ "initialFlow"
+ "initializeFunction:"
+ "initializeFunctionForUsage:"
+ "initializeLibrary:"
+ "initializeModels"
+ "inputDownsampling"
+ "inputIOSurface:"
+ "inputIOSurfaceByName:"
+ "inputSize:"
+ "isE5OnlyResulution"
+ "landscape432x244"
+ "landscape736x416"
+ "landscape768x432"
+ "landscape864x488"
+ "linearTextureArrayAlignmentBytes"
+ "linearTextureArrayAlignmentSlice"
+ "loadTracksWithMediaType:completionHandler:"
+ "localizedCaseInsensitiveContainsString:"
+ "matchFlow:callback:"
+ "matchFlow:toFullSizeFlow:callback:"
+ "modelName"
+ "neighborMaxVelocity"
+ "newComputePipelineStateWithDescriptor:error:"
+ "normalizeMonochromeToTextureArray"
+ "opticalFlowFirstFrame:secondFrame:flow:callback:"
+ "opticalFlowFirstFrame:secondFrame:originalFirst:originalSecond:flow:callback:"
+ "opticalFlowFrom:to:flow:completionHandler:"
+ "outputIOSurface:"
+ "outputIOSurfaceByName:"
+ "outputSize:"
+ "postProcessFlow:outputFlow:callback:"
+ "q40@0:8@16@24@32"
+ "q40@0:8^{__CVBuffer=}16^{__CVBuffer=}24@?32"
+ "q44@0:8@16@24@32i40"
+ "q48@0:8@16@24@32@40"
+ "q48@0:8@16@24@32@?40"
+ "q48@0:8Q16Q24Q32Q40"
+ "q48@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32@?40"
+ "q52@0:8@16@24@32@40f48"
+ "q88@0:8@16@24@32@40@48@56@64@72@80"
+ "q96@0:8@16@24@32@40@48@56@64@72@80@88"
+ "rangeAtIndex:"
+ "regularExpressionWithPattern:options:error:"
+ "releaseBufferAndTexture"
+ "releaseE5Resoruces"
+ "reshuffleFlow:previousFlow:destination:callback:waitForComplete:"
+ "scaleValue"
+ "searchRange"
+ "secondInput"
+ "secondInputSurface"
+ "secondStageInputCorrelation"
+ "secondStageInputFlow"
+ "secondStageInputInitialContext"
+ "secondStageInputUpdatedContext"
+ "secondStageOutputContext"
+ "secondStageOutputFlow"
+ "setAdaptationLayerInputFlow:"
+ "setCommandQueue:"
+ "setDeviceType:"
+ "setEnableGpuWaitForComplete:"
+ "setFirstInputSurfac:"
+ "setFirstInputSurface:"
+ "setFlowHeight:"
+ "setFlowWidth:"
+ "setIOSurfaceSharedEvent:"
+ "setInputDownsampling:"
+ "setInputIOSurface:index:"
+ "setLabel:"
+ "setMipmapLevelCount:"
+ "setModelFromDefaults"
+ "setObject:atIndexedSubscript:"
+ "setOutputIOSurface:index:"
+ "setPipelineLibrary:"
+ "setResourceOptions:"
+ "setSecondInputSurfac:"
+ "setSecondInputSurface:"
+ "setSecondStageInputInitialContext:"
+ "setTotalIteration:"
+ "setUpscaleFlow:"
+ "soc-generation"
+ "substringWithRange:"
+ "swapFrameBufferReference"
+ "the output size is not multiple of original flow size"
+ "tileMaxVelocity"
+ "tileSize"
+ "timeScale"
+ "totalIteration"
+ "updateCompletion"
+ "updateFlowSizeForLevel3"
+ "upscaleFinalFlow:outFlow:commandBuffer:"
+ "upscaleRefinedFloV2With:RGB:lrFlow:output:"
+ "v24@?0@\"IOSurfaceSharedEvent\"8Q16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v28@0:8@16B24"
+ "v28@?0Q8Q16i24"
+ "v32@0:8Q16Q24"
+ "v32@0:8^{__IOSurface=}16q24"
+ "v40@0:8@16^{__IOSurface=}24@32"
+ "v40@0:8^{__CVBuffer=}16^{__CVBuffer=}24@?32"
+ "v40@0:8^{__IOSurface=}16@24@32"
+ "v40@0:8^{__IOSurface=}16^{__CVBuffer=}24@32"
+ "v40@0:8^{__IOSurface=}16^{__IOSurface=}24@32"
+ "v44@0:8@16@24i32@36"
+ "v48@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32@?40"
+ "v52@0:8@16@24@3240B48"
+ "v52@0:8@16@24@32@40B48"
+ "v52@0:8@16@24@32f40i44i48"
+ "v52@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32@?40B48"
+ "v56@0:8^{?={?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}^{__CVBuffer}^{__CVBuffer}}16^{?={?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}^{__CVBuffer}^{__CVBuffer}}24^{?={?=[6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}]^{__CVBuffer}I}{?=[6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}]^{__CVBuffer}I}}32^{__CVBuffer=}40@?48"
+ "v64@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40^{__CVBuffer=}48@?56"
+ "v76@0:8^{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}16^{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}24^{?=[6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}]^{__CVBuffer}I}32B40i44i48^{__CVBuffer=}52^{__CVBuffer=}60@?68"
+ "v96@0:8I16^@20^{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}28^{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}36^{__CVBuffer=}44^{__CVBuffer=}52^{__CVBuffer=}60^{__CVBuffer=}68^{__CVBuffer=}76@?84B92"
+ "waitForAllTaskCompletionAsynchronously"
+ "warpedFeature"
+ "{?=QQQ}24@0:8q16"
- "\"A"
- "@48@0:8^{__IOSurface=}16q24q32q40"
- "Error invalid number of input ports (%ld)\n"
- "Failed to build model"
- "Input image [%@]: %ld x %ld x %ld"
- "Output Flow [%@]: %ld x %ld x %ld"
- "[2^{e5rt_buffer_object}]"
- "[2^{e5rt_io_port}]"
- "[OpticalFlowE5] Error! Tensor dtype is %ld bits. Must be fp16"
- "[OpticalFlowE5] Port is a surface type"
- "[OpticalFlowE5] Port is a tensor type"
- "[OpticalFlowE5] failed to get surface format"
- "^{e5rt_buffer_object=}"
- "^{e5rt_io_port=}"
- "_fidelityWeightBufferObject"
- "_inputSize"
- "_outputPortName"
- "_outputSize"
- "_output_port"
- "_subsampledOriginalFirst"
- "_subsampledOriginalSecond"
- "bufferToTexture"
- "bufferToTwoComponentTexture"
- "bundleWithIdentifier:"
- "completion event"
- "createFP16TextureFromIOSurface:width:height:channels:"
- "e5rt_async_event_create(&completionEvent, \"completion event\", E5RT_ASYNC_EVENT_TYPE_IOSURFACE_SHARED_EVENT)"
- "e5rt_async_event_create(&dependentEvent, \"dependent Event\", E5RT_ASYNC_EVENT_TYPE_IOSURFACE_SHARED_EVENT)"
- "e5rt_buffer_object_get_iosurface(_inputBufferObject[0], &_firstFrameSurface)"
- "e5rt_buffer_object_get_iosurface(_inputBufferObject[1], &_secondFrameSurface)"
- "e5rt_buffer_object_get_iosurface(_outputBufferObject, &_outputSurface)"
- "e5rt_execution_stream_operation_bind_completion_event(_operation, completionEvent)"
- "e5rt_execution_stream_operation_bind_dependent_events(_operation, &dependentEvent, 1)"
- "e5rt_execution_stream_operation_retain_output_port(_operation, _outputPortName.UTF8String, &_output_port)"
- "e5rt_io_port_bind_buffer_object(_output_port, _outputBufferObject)"
- "e5rt_io_port_retain_tensor_desc(_output_port, &output_tensor_desc)"
- "e5rt_program_library_retain_program_function(_library, \"main\", &_function)"
- "e5rt_tensor_desc_alloc_buffer_object(output_tensor_desc, E5RT_BUFFER_OBJECT_TYPE_IOSURFACE, 1, &_outputBufferObject)"
- "encodeConvertLinearBuffer:toPixelBuffer:"
- "estimateFlowLevel:withEstimator:firstFeatures:secondFeatures:correlation:upscaledFlow:warpedImage:prevFlow:outputFlow:waitForComplete:"
- "estimateStageFlowFromFirstFeatures:secondFeature:storage:baseStage:startLevel:lastLevel:startFlow:outputFlow:"
- "executeModel"
- "failed to build library"
- "initializeModel:"
- "matchFlow:"
- "matchFlow:toFullSizeFlow:"
- "opticalFlowFirstFrame:secondFrame:originalFirst:originalSecond:flow:"
- "postProcessFlow:outputFlow:"
- "reshuffleFlow:previousFlow:destination:waitForComplete:"
- "textureToBuffer"
- "twoComponentTextureToBuffer"
- "v44@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32B40"
- "v48@0:8@16@24@32f40B44"
- "v56@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40^{__CVBuffer=}48"
- "v68@0:8^{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}16^{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}24^{?=[6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}]^{__CVBuffer}I}32B40i44i48^{__CVBuffer=}52^{__CVBuffer=}60"
- "v88@0:8I16^@20^{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}28^{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}36^{__CVBuffer=}44^{__CVBuffer=}52^{__CVBuffer=}60^{__CVBuffer=}68^{__CVBuffer=}76B84"

```
