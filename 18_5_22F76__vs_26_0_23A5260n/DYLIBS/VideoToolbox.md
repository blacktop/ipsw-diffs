## VideoToolbox

> `/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`

```diff

-3225.7.1.0.0
-  __TEXT.__text: 0x42567c
-  __TEXT.__auth_stubs: 0x35f0
-  __TEXT.__cstring: 0x9871
-  __TEXT.__const: 0x40a0
-  __TEXT.__oslogstring: 0x1108
-  __TEXT.__dlopen_cstrs: 0x4f
-  __TEXT.__gcc_except_tab: 0x5c
-  __TEXT.__unwind_info: 0x5030
-  __TEXT.__eh_frame: 0x5c44
-  __TEXT.__objc_classname: 0x18
-  __TEXT.__objc_methname: 0x6b5
-  __TEXT.__objc_stubs: 0x900
-  __DATA_CONST.__got: 0xce8
-  __DATA_CONST.__const: 0x3150
-  __DATA_CONST.__objc_classlist: 0x8
+3255.61.4.11.7
+  __TEXT.__text: 0x512580
+  __TEXT.__auth_stubs: 0x3900
+  __TEXT.__delay_helper: 0xc8
+  __TEXT.__objc_methlist: 0xe2c
+  __TEXT.__const: 0x4188
+  __TEXT.__cstring: 0x38e4e
+  __TEXT.__oslogstring: 0x2815c
+  __TEXT.__gcc_except_tab: 0xf0
+  __TEXT.__dlopen_cstrs: 0x9b
+  __TEXT.__unwind_info: 0x5940
+  __TEXT.__eh_frame: 0x5b54
+  __TEXT.__objc_classname: 0x37a
+  __TEXT.__objc_methname: 0x2477
+  __TEXT.__objc_methtype: 0x950
+  __TEXT.__objc_stubs: 0x1860
+  __DATA_CONST.__got: 0xdb0
+  __DATA_CONST.__const: 0x3a08
+  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x240
-  __AUTH_CONST.__auth_got: 0x1b08
-  __AUTH_CONST.__const: 0x41ea8
-  __AUTH_CONST.__cfstring: 0x8b60
-  __AUTH_CONST.__objc_const: 0x90
-  __AUTH.__data: 0x38
-  __DATA.__data: 0x230
-  __DATA.__bss: 0x440
-  __DATA.__common: 0x78
+  __DATA_CONST.__objc_selrefs: 0x800
+  __DATA_CONST.__objc_superrefs: 0xb8
+  __DATA_CONST.__objc_arraydata: 0x20
+  __AUTH_CONST.__auth_got: 0x1c90
+  __AUTH_CONST.__const: 0x4d460
+  __AUTH_CONST.__cfstring: 0x24480
+  __AUTH_CONST.__objc_const: 0x3390
+  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH.__objc_data: 0x730
+  __AUTH.__data: 0x70
+  __DATA.__objc_ivar: 0x218
+  __DATA.__data: 0x3cc
+  __DATA.__bss: 0x5d0
+  __DATA.__common: 0x308
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x260
+  __DATA_DIRTY.__data: 0x2b8
+  __DATA_DIRTY.__common: 0x130
   __DATA_DIRTY.__bss: 0x560
-  __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/ColorSync
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppleJPEG.framework/AppleJPEG
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler
   - /System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/VideoToolboxParavirtualizationSupport.framework/VideoToolboxParavirtualizationSupport
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5CD446DE-DCB4-3CD5-80F1-54E6F6FEBBC5
-  Functions: 6863
-  Symbols:   18027
-  CStrings:  2711
+  UUID: 627BACEF-02B2-3F58-AEED-B8A177A7C394
+  Functions: 9031
+  Symbols:   22232
+  CStrings:  14571
 
Symbols:
+ +[VTFrameRateConversionConfiguration defaultRevision]
+ +[VTFrameRateConversionConfiguration isSupported]
+ +[VTFrameRateConversionConfiguration processorSupported]
+ +[VTFrameRateConversionConfiguration supportedRevisions]
+ +[VTLowLatencyFrameInterpolationConfiguration isSupported]
+ +[VTLowLatencySuperResolutionScalerConfiguration isSupported]
+ +[VTLowLatencySuperResolutionScalerConfiguration maximumDimensions]
+ +[VTLowLatencySuperResolutionScalerConfiguration minimumDimensions]
+ +[VTLowLatencySuperResolutionScalerConfiguration supportedScaleFactorsForFrameWidth:frameHeight:]
+ +[VTLowLatencySuperResolutionScalerConfiguration supportedScaleFactorsForFrameWidth:frameHeight:].cold.1
+ +[VTMotionBlurConfiguration defaultRevision]
+ +[VTMotionBlurConfiguration isSupported]
+ +[VTMotionBlurConfiguration processorSupported]
+ +[VTMotionBlurConfiguration supportedRevisions]
+ +[VTOpticalFlowConfiguration defaultRevision]
+ +[VTOpticalFlowConfiguration isSupported]
+ +[VTOpticalFlowConfiguration processorSupported]
+ +[VTOpticalFlowConfiguration supportedRevisions]
+ +[VTSuperResolutionScalerConfiguration defaultRevision]
+ +[VTSuperResolutionScalerConfiguration isSupported]
+ +[VTSuperResolutionScalerConfiguration supportedRevisions]
+ +[VTSuperResolutionScalerConfiguration supportedScaleFactors]
+ +[VTTemporalNoiseFilterConfiguration _loadCapabilities]
+ +[VTTemporalNoiseFilterConfiguration _loadCapabilities].cold.1
+ +[VTTemporalNoiseFilterConfiguration isSupported]
+ +[VTTemporalNoiseFilterConfiguration maximumDimensions]
+ +[VTTemporalNoiseFilterConfiguration minimumDimensions]
+ +[VTTestProcessorConfiguration isSupported]
+ +[VTTestProcessorConfiguration maximumDimensions]
+ +[VTTestProcessorConfiguration minimumDimensions]
+ +[VTTestProcessorConfiguration processorSupported]
+ -[VTFrameProcessor createSharedEventListener]
+ -[VTFrameProcessor dealloc]
+ -[VTFrameProcessor destroySharedEventListener]
+ -[VTFrameProcessor endSession]
+ -[VTFrameProcessor init]
+ -[VTFrameProcessor internalEndSession]
+ -[VTFrameProcessor processWithCommandBuffer:parameters:]
+ -[VTFrameProcessor processWithParameters:completionHandler:]
+ -[VTFrameProcessor processWithParameters:error:]
+ -[VTFrameProcessor processWithParameters:frameOutputHandler:]
+ -[VTFrameProcessor startSessionWithConfiguration:error:]
+ -[VTFrameProcessor startSessionWithConfiguration:error:].cold.1
+ -[VTFrameProcessor startSessionWithConfiguration:error:].cold.2
+ -[VTFrameProcessor startSessionWithConfiguration:error:].cold.3
+ -[VTFrameProcessor startSessionWithConfiguration:error:].cold.4
+ -[VTFrameProcessorFrame buffer]
+ -[VTFrameProcessorFrame dealloc]
+ -[VTFrameProcessorFrame initWithBuffer:presentationTimeStamp:]
+ -[VTFrameProcessorFrame initWithBuffer:presentationTimeStamp:].cold.1
+ -[VTFrameProcessorFrame initWithBuffer:presentationTimeStamp:].cold.2
+ -[VTFrameProcessorFrame presentationTimeStamp]
+ -[VTFrameProcessorFrame veFrame]
+ -[VTFrameProcessorOpticalFlow backwardFlow]
+ -[VTFrameProcessorOpticalFlow dealloc]
+ -[VTFrameProcessorOpticalFlow forwardFlow]
+ -[VTFrameProcessorOpticalFlow initWithForwardFlow:backwardFlow:]
+ -[VTFrameProcessorOpticalFlow initWithForwardFlow:backwardFlow:].cold.1
+ -[VTFrameProcessorOpticalFlow initWithForwardFlow:backwardFlow:].cold.2
+ -[VTFrameProcessorOpticalFlow initWithForwardFlow:backwardFlow:].cold.3
+ -[VTFrameProcessorOpticalFlow veFrameOpticalFlow]
+ -[VTFrameRateConversionConfiguration dealloc]
+ -[VTFrameRateConversionConfiguration destinationPixelBufferAttributes]
+ -[VTFrameRateConversionConfiguration frameHeight]
+ -[VTFrameRateConversionConfiguration frameSupportedPixelFormats]
+ -[VTFrameRateConversionConfiguration frameWidth]
+ -[VTFrameRateConversionConfiguration initWithFrameWidth:frameHeight:usePrecomputedFlow:qualityPrioritization:revision:]
+ -[VTFrameRateConversionConfiguration qualityPrioritization]
+ -[VTFrameRateConversionConfiguration revision]
+ -[VTFrameRateConversionConfiguration sourcePixelBufferAttributes]
+ -[VTFrameRateConversionConfiguration usePrecomputedFlow]
+ -[VTFrameRateConversionConfiguration veConfiguration]
+ -[VTFrameRateConversionParameters dealloc]
+ -[VTFrameRateConversionParameters destinationFrames]
+ -[VTFrameRateConversionParameters initWithSourceFrame:nextFrame:opticalFlow:interpolationPhase:submissionMode:destinationFrames:]
+ -[VTFrameRateConversionParameters interpolationPhase]
+ -[VTFrameRateConversionParameters nextFrame]
+ -[VTFrameRateConversionParameters opticalFlow]
+ -[VTFrameRateConversionParameters sourceFrame]
+ -[VTFrameRateConversionParameters submissionMode]
+ -[VTFrameRateConversionParameters veParameters]
+ -[VTLowLatencyFrameInterpolationConfiguration dealloc]
+ -[VTLowLatencyFrameInterpolationConfiguration destinationPixelBufferAttributes]
+ -[VTLowLatencyFrameInterpolationConfiguration frameHeight]
+ -[VTLowLatencyFrameInterpolationConfiguration frameSupportedPixelFormats]
+ -[VTLowLatencyFrameInterpolationConfiguration frameWidth]
+ -[VTLowLatencyFrameInterpolationConfiguration initWithFrameWidth:frameHeight:numberOfInterpolatedFrames:]
+ -[VTLowLatencyFrameInterpolationConfiguration initWithFrameWidth:frameHeight:spatialScaleFactor:]
+ -[VTLowLatencyFrameInterpolationConfiguration numberOfInterpolatedFrames]
+ -[VTLowLatencyFrameInterpolationConfiguration sourcePixelBufferAttributes]
+ -[VTLowLatencyFrameInterpolationConfiguration spatialScaleFactor]
+ -[VTLowLatencyFrameInterpolationConfiguration vcpConfiguration]
+ -[VTLowLatencyFrameInterpolationImplementation dealloc]
+ -[VTLowLatencyFrameInterpolationImplementation finishProcessing]
+ -[VTLowLatencyFrameInterpolationImplementation init]
+ -[VTLowLatencyFrameInterpolationImplementation processWithParameters:frameOutputHandler:]
+ -[VTLowLatencyFrameInterpolationImplementation processWithParams:error:]
+ -[VTLowLatencyFrameInterpolationImplementation startSessionWithConfiguration:error:]
+ -[VTLowLatencyFrameInterpolationParameters dealloc]
+ -[VTLowLatencyFrameInterpolationParameters destinationFrames]
+ -[VTLowLatencyFrameInterpolationParameters initWithSourceFrame:previousFrame:interpolationPhase:destinationFrames:]
+ -[VTLowLatencyFrameInterpolationParameters interpolationPhase]
+ -[VTLowLatencyFrameInterpolationParameters parameterDispatchGroup]
+ -[VTLowLatencyFrameInterpolationParameters previousFrame]
+ -[VTLowLatencyFrameInterpolationParameters sourceFrame]
+ -[VTLowLatencySuperResolutionScalerConfiguration dealloc]
+ -[VTLowLatencySuperResolutionScalerConfiguration destinationPixelBufferAttributes]
+ -[VTLowLatencySuperResolutionScalerConfiguration frameHeight]
+ -[VTLowLatencySuperResolutionScalerConfiguration frameSupportedPixelFormats]
+ -[VTLowLatencySuperResolutionScalerConfiguration frameWidth]
+ -[VTLowLatencySuperResolutionScalerConfiguration initWithFrameWidth:frameHeight:scaleFactor:]
+ -[VTLowLatencySuperResolutionScalerConfiguration scaleFactor]
+ -[VTLowLatencySuperResolutionScalerConfiguration sourcePixelBufferAttributes]
+ -[VTLowLatencySuperResolutionScalerConfiguration vcpConfiguration]
+ -[VTLowLatencySuperResolutionScalerImplementation dealloc]
+ -[VTLowLatencySuperResolutionScalerImplementation finishProcessing]
+ -[VTLowLatencySuperResolutionScalerImplementation init]
+ -[VTLowLatencySuperResolutionScalerImplementation processWithParams:error:]
+ -[VTLowLatencySuperResolutionScalerImplementation startSessionWithConfiguration:error:]
+ -[VTLowLatencySuperResolutionScalerParameters dealloc]
+ -[VTLowLatencySuperResolutionScalerParameters destinationFrame]
+ -[VTLowLatencySuperResolutionScalerParameters initWithSourceFrame:destinationFrame:]
+ -[VTLowLatencySuperResolutionScalerParameters sourceFrame]
+ -[VTMotionBlurConfiguration dealloc]
+ -[VTMotionBlurConfiguration destinationPixelBufferAttributes]
+ -[VTMotionBlurConfiguration frameHeight]
+ -[VTMotionBlurConfiguration frameSupportedPixelFormats]
+ -[VTMotionBlurConfiguration frameWidth]
+ -[VTMotionBlurConfiguration initWithFrameWidth:frameHeight:usePrecomputedFlow:qualityPrioritization:revision:]
+ -[VTMotionBlurConfiguration qualityPrioritization]
+ -[VTMotionBlurConfiguration revision]
+ -[VTMotionBlurConfiguration sourcePixelBufferAttributes]
+ -[VTMotionBlurConfiguration usePrecomputedFlow]
+ -[VTMotionBlurConfiguration veConfiguration]
+ -[VTMotionBlurParameters dealloc]
+ -[VTMotionBlurParameters destinationFrame]
+ -[VTMotionBlurParameters initWithSourceFrame:nextFrame:previousFrame:nextOpticalFlow:previousOpticalFlow:motionBlurStrength:submissionMode:destinationFrame:]
+ -[VTMotionBlurParameters motionBlurStrength]
+ -[VTMotionBlurParameters nextFrame]
+ -[VTMotionBlurParameters nextOpticalFlow]
+ -[VTMotionBlurParameters previousFrame]
+ -[VTMotionBlurParameters previousOpticalFlow]
+ -[VTMotionBlurParameters sourceFrame]
+ -[VTMotionBlurParameters submissionMode]
+ -[VTMotionBlurParameters veParameters]
+ -[VTOpticalFlowConfiguration dealloc]
+ -[VTOpticalFlowConfiguration destinationPixelBufferAttributes]
+ -[VTOpticalFlowConfiguration frameHeight]
+ -[VTOpticalFlowConfiguration frameSupportedPixelFormats]
+ -[VTOpticalFlowConfiguration frameWidth]
+ -[VTOpticalFlowConfiguration initWithFrameWidth:frameHeight:qualityPrioritization:revision:]
+ -[VTOpticalFlowConfiguration qualityPrioritization]
+ -[VTOpticalFlowConfiguration revision]
+ -[VTOpticalFlowConfiguration sourcePixelBufferAttributes]
+ -[VTOpticalFlowConfiguration veConfiguration]
+ -[VTOpticalFlowParameters dealloc]
+ -[VTOpticalFlowParameters destinationOpticalFlow]
+ -[VTOpticalFlowParameters initWithSourceFrame:nextFrame:submissionMode:destinationOpticalFlow:]
+ -[VTOpticalFlowParameters nextFrame]
+ -[VTOpticalFlowParameters sourceFrame]
+ -[VTOpticalFlowParameters submissionMode]
+ -[VTOpticalFlowParameters veParameters]
+ -[VTSuperResolutionScalerConfiguration configurationModelPercentageAvailable]
+ -[VTSuperResolutionScalerConfiguration configurationModelStatus]
+ -[VTSuperResolutionScalerConfiguration dealloc]
+ -[VTSuperResolutionScalerConfiguration destinationPixelBufferAttributes]
+ -[VTSuperResolutionScalerConfiguration downloadConfigurationModelWithCompletionHandler:]
+ -[VTSuperResolutionScalerConfiguration frameHeight]
+ -[VTSuperResolutionScalerConfiguration frameSupportedPixelFormats]
+ -[VTSuperResolutionScalerConfiguration frameWidth]
+ -[VTSuperResolutionScalerConfiguration initWithFrameWidth:frameHeight:scaleFactor:inputType:usePrecomputedFlow:qualityPrioritization:revision:]
+ -[VTSuperResolutionScalerConfiguration inputType]
+ -[VTSuperResolutionScalerConfiguration qualityPrioritization]
+ -[VTSuperResolutionScalerConfiguration revision]
+ -[VTSuperResolutionScalerConfiguration scaleFactor]
+ -[VTSuperResolutionScalerConfiguration sourcePixelBufferAttributes]
+ -[VTSuperResolutionScalerConfiguration usesPrecomputedFlow]
+ -[VTSuperResolutionScalerConfiguration veConfiguration]
+ -[VTSuperResolutionScalerParameters dealloc]
+ -[VTSuperResolutionScalerParameters destinationFrame]
+ -[VTSuperResolutionScalerParameters initWithSourceFrame:previousFrame:previousOutputFrame:opticalFlow:submissionMode:destinationFrame:]
+ -[VTSuperResolutionScalerParameters opticalFlow]
+ -[VTSuperResolutionScalerParameters previousFrame]
+ -[VTSuperResolutionScalerParameters previousOutputFrame]
+ -[VTSuperResolutionScalerParameters sourceFrame]
+ -[VTSuperResolutionScalerParameters submissionMode]
+ -[VTSuperResolutionScalerParameters veParameters]
+ -[VTTemporalNoiseFilterConfiguration dealloc]
+ -[VTTemporalNoiseFilterConfiguration destinationPixelBufferAttributes]
+ -[VTTemporalNoiseFilterConfiguration frameHeight]
+ -[VTTemporalNoiseFilterConfiguration frameSupportedPixelFormats]
+ -[VTTemporalNoiseFilterConfiguration frameWidth]
+ -[VTTemporalNoiseFilterConfiguration initWithFrameWidth:frameHeight:]
+ -[VTTemporalNoiseFilterConfiguration loadProperties]
+ -[VTTemporalNoiseFilterConfiguration nextFrameCount]
+ -[VTTemporalNoiseFilterConfiguration previousFrameCount]
+ -[VTTemporalNoiseFilterConfiguration sourcePixelBufferAttributes]
+ -[VTTemporalNoiseFilterImplementation _checkForDiscontinuity:]
+ -[VTTemporalNoiseFilterImplementation _clearStaledPendingFramesFromQueue]
+ -[VTTemporalNoiseFilterImplementation _completeFrame:]
+ -[VTTemporalNoiseFilterImplementation _completeFrames]
+ -[VTTemporalNoiseFilterImplementation _createPendingFrame:inputFrame:]
+ -[VTTemporalNoiseFilterImplementation _findFrameInQueue:]
+ -[VTTemporalNoiseFilterImplementation _freePendingFrame:]
+ -[VTTemporalNoiseFilterImplementation _processFrame:outputFrame:useClientProvidedOutputFrame:]
+ -[VTTemporalNoiseFilterImplementation _processReferenceFrameIfNotProcessed:]
+ -[VTTemporalNoiseFilterImplementation _processReferenceFrameIfNotProcessed:].cold.1
+ -[VTTemporalNoiseFilterImplementation _processSourceFrameIfNotProcessed:completionHandler:]
+ -[VTTemporalNoiseFilterImplementation _processSourceFrameIfNotProcessed:completionHandler:].cold.1
+ -[VTTemporalNoiseFilterImplementation _setFilterStrength:]
+ -[VTTemporalNoiseFilterImplementation _validateParameters:error:]
+ -[VTTemporalNoiseFilterImplementation _validateParameters:error:].cold.1
+ -[VTTemporalNoiseFilterImplementation _validateParameters:error:].cold.2
+ -[VTTemporalNoiseFilterImplementation _validateParameters:error:].cold.3
+ -[VTTemporalNoiseFilterImplementation _validateParameters:error:].cold.4
+ -[VTTemporalNoiseFilterImplementation _validateParameters:error:].cold.5
+ -[VTTemporalNoiseFilterImplementation _validateParameters:error:].cold.6
+ -[VTTemporalNoiseFilterImplementation _validateParameters:error:].cold.7
+ -[VTTemporalNoiseFilterImplementation _validateParameters:error:].cold.8
+ -[VTTemporalNoiseFilterImplementation _validateParameters:error:].cold.9
+ -[VTTemporalNoiseFilterImplementation configuration]
+ -[VTTemporalNoiseFilterImplementation dealloc]
+ -[VTTemporalNoiseFilterImplementation finishProcessing]
+ -[VTTemporalNoiseFilterImplementation handleEmittedFrame:presentationTimestamp:status:infoFlags:]
+ -[VTTemporalNoiseFilterImplementation init]
+ -[VTTemporalNoiseFilterImplementation processWithParams:completionHandler:error:]
+ -[VTTemporalNoiseFilterImplementation processWithParams:error:]
+ -[VTTemporalNoiseFilterImplementation startSessionWithConfiguration:error:]
+ -[VTTemporalNoiseFilterImplementation startSessionWithConfiguration:error:].cold.1
+ -[VTTemporalNoiseFilterImplementation startSessionWithConfiguration:error:].cold.2
+ -[VTTemporalNoiseFilterParameters dealloc]
+ -[VTTemporalNoiseFilterParameters destinationFrame]
+ -[VTTemporalNoiseFilterParameters discontinuity]
+ -[VTTemporalNoiseFilterParameters filterStrength]
+ -[VTTemporalNoiseFilterParameters initWithSourceFrame:nextFrames:previousFrames:destinationFrame:filterStrength:discontinuity:]
+ -[VTTemporalNoiseFilterParameters nextFrames]
+ -[VTTemporalNoiseFilterParameters previousFrames]
+ -[VTTemporalNoiseFilterParameters setDiscontinuity:]
+ -[VTTemporalNoiseFilterParameters setFilterStrength:]
+ -[VTTemporalNoiseFilterParameters sourceFrame]
+ -[VTTestProcessorConfiguration dealloc]
+ -[VTTestProcessorConfiguration destinationPixelBufferAttributes]
+ -[VTTestProcessorConfiguration flags]
+ -[VTTestProcessorConfiguration frameHeight]
+ -[VTTestProcessorConfiguration frameSupportedPixelFormats]
+ -[VTTestProcessorConfiguration frameWidth]
+ -[VTTestProcessorConfiguration initWithFrameWidth:frameHeight:flags:]
+ -[VTTestProcessorConfiguration initWithFrameWidth:frameHeight:flags:].cold.1
+ -[VTTestProcessorConfiguration sourcePixelBufferAttributes]
+ -[VTTestProcessorImplementation dealloc]
+ -[VTTestProcessorImplementation finishProcessing]
+ -[VTTestProcessorImplementation init]
+ -[VTTestProcessorImplementation processWithParams:error:]
+ -[VTTestProcessorImplementation startSessionWithConfiguration:error:]
+ -[VTTestProcessorParameters dealloc]
+ -[VTTestProcessorParameters destinationFrame]
+ -[VTTestProcessorParameters initWithSourceFrame:nextFrame:previousFrame:destinationFrame:]
+ -[VTTestProcessorParameters nextFrame]
+ -[VTTestProcessorParameters previousFrame]
+ -[VTTestProcessorParameters sourceFrame]
+ GCC_except_table13
+ GCC_except_table21
+ GCC_except_table76
+ _AppleJPEGVideoDecoder_DecodeFrame.cold.3
+ _CFAllocatorAllocateTyped
+ _CFSetCreate
+ _CMPhotoLibrary
+ _CMPhotoLibraryCore
+ _CMPhotoLibraryCore.frameworkLibrary
+ _CMSampleBufferGetTotalSampleSize
+ _CVMetalBufferCacheCreate
+ _CVMetalBufferCacheCreateBufferFromImage
+ _CVMetalBufferGetBuffer
+ _DepthWrapperDecoder_StartSession.cold.11
+ _DepthWrapperDecoder_StartSession.cold.12
+ _DepthWrapperEncoder_CreateInstance.cold.2
+ _DepthWrapperEncoder_CreateInstance.cold.3
+ _DepthWrapperEncoder_CreateInstance.cold.4
+ _DolbyVisionDecoder_DecodeFrame.cold.18
+ _DolbyVisionDecoder_DecodeFrame.cold.19
+ _DolbyVisionDecoder_DecodeFrame.cold.20
+ _DolbyVisionDecoder_DecodeFrame.cold.21
+ _DolbyVisionDecoder_DecodeFrame.cold.22
+ _DolbyVisionDecoder_DecodeFrame.cold.23
+ _DolbyVisionDecoder_DecodeFrame.cold.24
+ _FigAtomicIncrement64
+ _FigCFArrayCreateConcatenationOfTwoArrays
+ _FigCFDictionaryApplyBlock
+ _FigCFDictionaryGetCGRectIfPresent
+ _FigCFDictionaryGetCGSizeIfPresent
+ _FigCFDictionaryGetDictionaryValue
+ _FigCFDictionaryGetDoubleIfPresent
+ _FigCFDictionarySetCGRect
+ _FigCFDictionarySetCGSize
+ _FigDerivedFormatDescriptionCreate
+ _FigExecuteBlockWithAutoreleasePool
+ _FigGetIOSurfaceAcceleratorCapabilityQuadraBayerRepacking
+ _FigGetUpTime
+ _FigHEVCBridge_CreateHDR10PlusITUT35Payload
+ _FigHEVCBridge_CreateSEIMessageWithITUT35Payload
+ _FigHostTimeToNanoseconds
+ _FigInMemoryDeserializerCopyCFData
+ _FigInMemorySerializerAppendCFData
+ _FigIsTypeOfDispatchQueue
+ _FigLogPowerEvent
+ _FigRegisterIOSurfacePixelTransferCapabilityOnce.interchangeDisparityPixelFormatTypes
+ _FigRegisterIOSurfacePixelTransferCapabilityOnce.interchangeSenselArrayPixelFormatTypes
+ _FigRegisterIOSurfacePixelTransferCapabilityOnce.uncompressedDisparityPixelFormatTypes
+ _FigRegisterIOSurfacePixelTransferCapabilityOnce.uncompressedSenselArrayPixelFormatTypes
+ _FigRegistryAddSearchPath
+ _FigRemote_CopyArrayOfPropertyListFromData
+ _FigSignalErrorAt3
+ _FigThreadGetMachThreadPriorityValue
+ _FigVideoFormatDescriptionCreateSecurityInfoExtension
+ _IOSurfaceGetAllocSize
+ _IOSurfaceGetTypeID
+ _NSClassFromString
+ _NSLog
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_MTLSharedEventListener
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSIndexSet
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_RBSProcessHandle
+ _OBJC_CLASS_$_RBSProcessIdentifier
+ _OBJC_CLASS_$_VTFrameProcessor
+ _OBJC_CLASS_$_VTFrameProcessorFrame
+ _OBJC_CLASS_$_VTFrameProcessorOpticalFlow
+ _OBJC_CLASS_$_VTFrameRateConversionConfiguration
+ _OBJC_CLASS_$_VTFrameRateConversionParameters
+ _OBJC_CLASS_$_VTLowLatencyFrameInterpolationConfiguration
+ _OBJC_CLASS_$_VTLowLatencyFrameInterpolationImplementation
+ _OBJC_CLASS_$_VTLowLatencyFrameInterpolationParameters
+ _OBJC_CLASS_$_VTLowLatencySuperResolutionScalerConfiguration
+ _OBJC_CLASS_$_VTLowLatencySuperResolutionScalerImplementation
+ _OBJC_CLASS_$_VTLowLatencySuperResolutionScalerParameters
+ _OBJC_CLASS_$_VTMotionBlurConfiguration
+ _OBJC_CLASS_$_VTMotionBlurParameters
+ _OBJC_CLASS_$_VTOpticalFlowConfiguration
+ _OBJC_CLASS_$_VTOpticalFlowParameters
+ _OBJC_CLASS_$_VTSuperResolutionScalerConfiguration
+ _OBJC_CLASS_$_VTSuperResolutionScalerParameters
+ _OBJC_CLASS_$_VTTemporalNoiseFilterConfiguration
+ _OBJC_CLASS_$_VTTemporalNoiseFilterImplementation
+ _OBJC_CLASS_$_VTTemporalNoiseFilterParameters
+ _OBJC_CLASS_$_VTTestProcessorConfiguration
+ _OBJC_CLASS_$_VTTestProcessorImplementation
+ _OBJC_CLASS_$_VTTestProcessorParameters
+ _OBJC_IVAR_$_VTFrameProcessor._configuration
+ _OBJC_IVAR_$_VTFrameProcessor._device
+ _OBJC_IVAR_$_VTFrameProcessor._processFrameQueue
+ _OBJC_IVAR_$_VTFrameProcessor._processor
+ _OBJC_IVAR_$_VTFrameProcessor._processorType
+ _OBJC_IVAR_$_VTFrameProcessor._sharedEventList
+ _OBJC_IVAR_$_VTFrameProcessor._sharedEventListLock
+ _OBJC_IVAR_$_VTFrameProcessor._sharedEventListTearingDown
+ _OBJC_IVAR_$_VTFrameProcessor._sharedEventListener
+ _OBJC_IVAR_$_VTFrameProcessor._veFrameProcessor
+ _OBJC_IVAR_$_VTFrameProcessorFrame._buffer
+ _OBJC_IVAR_$_VTFrameProcessorFrame._presentationTimeStamp
+ _OBJC_IVAR_$_VTFrameProcessorFrame._veFrame
+ _OBJC_IVAR_$_VTFrameProcessorOpticalFlow._backwardFlow
+ _OBJC_IVAR_$_VTFrameProcessorOpticalFlow._forwardFlow
+ _OBJC_IVAR_$_VTFrameProcessorOpticalFlow._veFrameOpticalFlow
+ _OBJC_IVAR_$_VTFrameRateConversionConfiguration._destinationPixelBufferAttributes
+ _OBJC_IVAR_$_VTFrameRateConversionConfiguration._frameHeight
+ _OBJC_IVAR_$_VTFrameRateConversionConfiguration._frameSupportedPixelFormats
+ _OBJC_IVAR_$_VTFrameRateConversionConfiguration._frameWidth
+ _OBJC_IVAR_$_VTFrameRateConversionConfiguration._qualityPrioritization
+ _OBJC_IVAR_$_VTFrameRateConversionConfiguration._revision
+ _OBJC_IVAR_$_VTFrameRateConversionConfiguration._sourcePixelBufferAttributes
+ _OBJC_IVAR_$_VTFrameRateConversionConfiguration._usePrecomputedFlow
+ _OBJC_IVAR_$_VTFrameRateConversionConfiguration._veConfiguration
+ _OBJC_IVAR_$_VTFrameRateConversionParameters._destinationFrames
+ _OBJC_IVAR_$_VTFrameRateConversionParameters._interpolationPhase
+ _OBJC_IVAR_$_VTFrameRateConversionParameters._nextFrame
+ _OBJC_IVAR_$_VTFrameRateConversionParameters._opticalFlow
+ _OBJC_IVAR_$_VTFrameRateConversionParameters._sourceFrame
+ _OBJC_IVAR_$_VTFrameRateConversionParameters._submissionMode
+ _OBJC_IVAR_$_VTFrameRateConversionParameters._veDestinationFrames
+ _OBJC_IVAR_$_VTFrameRateConversionParameters._veParameters
+ _OBJC_IVAR_$_VTLowLatencyFrameInterpolationConfiguration._destinationPixelBufferAttributes
+ _OBJC_IVAR_$_VTLowLatencyFrameInterpolationConfiguration._frameHeight
+ _OBJC_IVAR_$_VTLowLatencyFrameInterpolationConfiguration._frameSupportedPixelFormats
+ _OBJC_IVAR_$_VTLowLatencyFrameInterpolationConfiguration._frameWidth
+ _OBJC_IVAR_$_VTLowLatencyFrameInterpolationConfiguration._numberOfInterpolatedFrames
+ _OBJC_IVAR_$_VTLowLatencyFrameInterpolationConfiguration._sourcePixelBufferAttributes
+ _OBJC_IVAR_$_VTLowLatencyFrameInterpolationConfiguration._spatialScaleFactor
+ _OBJC_IVAR_$_VTLowLatencyFrameInterpolationConfiguration.vcpConfiguration
+ _OBJC_IVAR_$_VTLowLatencyFrameInterpolationImplementation._vcpFrameInterpolationProcessor
+ _OBJC_IVAR_$_VTLowLatencyFrameInterpolationParameters._destinationFrames
+ _OBJC_IVAR_$_VTLowLatencyFrameInterpolationParameters._interpolationPhase
+ _OBJC_IVAR_$_VTLowLatencyFrameInterpolationParameters._parameterDispatchGroup
+ _OBJC_IVAR_$_VTLowLatencyFrameInterpolationParameters._previousFrame
+ _OBJC_IVAR_$_VTLowLatencyFrameInterpolationParameters._sourceFrame
+ _OBJC_IVAR_$_VTLowLatencySuperResolutionScalerConfiguration._destinationPixelBufferAttributes
+ _OBJC_IVAR_$_VTLowLatencySuperResolutionScalerConfiguration._frameHeight
+ _OBJC_IVAR_$_VTLowLatencySuperResolutionScalerConfiguration._frameSupportedPixelFormats
+ _OBJC_IVAR_$_VTLowLatencySuperResolutionScalerConfiguration._frameWidth
+ _OBJC_IVAR_$_VTLowLatencySuperResolutionScalerConfiguration._scaleFactor
+ _OBJC_IVAR_$_VTLowLatencySuperResolutionScalerConfiguration._sourcePixelBufferAttributes
+ _OBJC_IVAR_$_VTLowLatencySuperResolutionScalerConfiguration.vcpConfiguration
+ _OBJC_IVAR_$_VTLowLatencySuperResolutionScalerImplementation._vcpSuperResolutionProcessor
+ _OBJC_IVAR_$_VTLowLatencySuperResolutionScalerParameters._destinationFrame
+ _OBJC_IVAR_$_VTLowLatencySuperResolutionScalerParameters._sourceFrame
+ _OBJC_IVAR_$_VTMotionBlurConfiguration._destinationPixelBufferAttributes
+ _OBJC_IVAR_$_VTMotionBlurConfiguration._frameHeight
+ _OBJC_IVAR_$_VTMotionBlurConfiguration._frameSupportedPixelFormats
+ _OBJC_IVAR_$_VTMotionBlurConfiguration._frameWidth
+ _OBJC_IVAR_$_VTMotionBlurConfiguration._qualityPrioritization
+ _OBJC_IVAR_$_VTMotionBlurConfiguration._revision
+ _OBJC_IVAR_$_VTMotionBlurConfiguration._sourcePixelBufferAttributes
+ _OBJC_IVAR_$_VTMotionBlurConfiguration._usePrecomputedFlow
+ _OBJC_IVAR_$_VTMotionBlurConfiguration._veConfiguration
+ _OBJC_IVAR_$_VTMotionBlurParameters._destinationFrame
+ _OBJC_IVAR_$_VTMotionBlurParameters._motionBlurStrength
+ _OBJC_IVAR_$_VTMotionBlurParameters._nextFrame
+ _OBJC_IVAR_$_VTMotionBlurParameters._nextOpticalFlow
+ _OBJC_IVAR_$_VTMotionBlurParameters._previousFrame
+ _OBJC_IVAR_$_VTMotionBlurParameters._previousOpticalFlow
+ _OBJC_IVAR_$_VTMotionBlurParameters._sourceFrame
+ _OBJC_IVAR_$_VTMotionBlurParameters._submissionMode
+ _OBJC_IVAR_$_VTMotionBlurParameters._veParameters
+ _OBJC_IVAR_$_VTOpticalFlowConfiguration._destinationPixelBufferAttributes
+ _OBJC_IVAR_$_VTOpticalFlowConfiguration._flowPixelFormat
+ _OBJC_IVAR_$_VTOpticalFlowConfiguration._frameHeight
+ _OBJC_IVAR_$_VTOpticalFlowConfiguration._frameSupportedPixelFormats
+ _OBJC_IVAR_$_VTOpticalFlowConfiguration._frameWidth
+ _OBJC_IVAR_$_VTOpticalFlowConfiguration._qualityPrioritization
+ _OBJC_IVAR_$_VTOpticalFlowConfiguration._revision
+ _OBJC_IVAR_$_VTOpticalFlowConfiguration._sourcePixelBufferAttributes
+ _OBJC_IVAR_$_VTOpticalFlowConfiguration._veConfiguration
+ _OBJC_IVAR_$_VTOpticalFlowParameters._destinationOpticalFlow
+ _OBJC_IVAR_$_VTOpticalFlowParameters._nextFrame
+ _OBJC_IVAR_$_VTOpticalFlowParameters._sourceFrame
+ _OBJC_IVAR_$_VTOpticalFlowParameters._submissionMode
+ _OBJC_IVAR_$_VTOpticalFlowParameters._veParameters
+ _OBJC_IVAR_$_VTSuperResolutionScalerConfiguration._destinationPixelBufferAttributes
+ _OBJC_IVAR_$_VTSuperResolutionScalerConfiguration._frameHeight
+ _OBJC_IVAR_$_VTSuperResolutionScalerConfiguration._frameSupportedPixelFormats
+ _OBJC_IVAR_$_VTSuperResolutionScalerConfiguration._frameWidth
+ _OBJC_IVAR_$_VTSuperResolutionScalerConfiguration._inputType
+ _OBJC_IVAR_$_VTSuperResolutionScalerConfiguration._precomputedFlow
+ _OBJC_IVAR_$_VTSuperResolutionScalerConfiguration._qualityPrioritization
+ _OBJC_IVAR_$_VTSuperResolutionScalerConfiguration._revision
+ _OBJC_IVAR_$_VTSuperResolutionScalerConfiguration._scaleFactor
+ _OBJC_IVAR_$_VTSuperResolutionScalerConfiguration._sourcePixelBufferAttributes
+ _OBJC_IVAR_$_VTSuperResolutionScalerConfiguration._veConfiguration
+ _OBJC_IVAR_$_VTSuperResolutionScalerParameters._destinationFrame
+ _OBJC_IVAR_$_VTSuperResolutionScalerParameters._opticalFlow
+ _OBJC_IVAR_$_VTSuperResolutionScalerParameters._previousFrame
+ _OBJC_IVAR_$_VTSuperResolutionScalerParameters._previousOutputFrame
+ _OBJC_IVAR_$_VTSuperResolutionScalerParameters._sourceFrame
+ _OBJC_IVAR_$_VTSuperResolutionScalerParameters._submissionMode
+ _OBJC_IVAR_$_VTSuperResolutionScalerParameters._veParameters
+ _OBJC_IVAR_$_VTTemporalNoiseFilterConfiguration._destinationPixelBufferAttributes
+ _OBJC_IVAR_$_VTTemporalNoiseFilterConfiguration._frameHeight
+ _OBJC_IVAR_$_VTTemporalNoiseFilterConfiguration._frameSupportedPixelFormats
+ _OBJC_IVAR_$_VTTemporalNoiseFilterConfiguration._frameWidth
+ _OBJC_IVAR_$_VTTemporalNoiseFilterConfiguration._nextFrameCount
+ _OBJC_IVAR_$_VTTemporalNoiseFilterConfiguration._previousFrameCount
+ _OBJC_IVAR_$_VTTemporalNoiseFilterConfiguration._sourcePixelBufferAttributes
+ _OBJC_IVAR_$_VTTemporalNoiseFilterImplementation._configuration
+ _OBJC_IVAR_$_VTTemporalNoiseFilterImplementation.filterInternal
+ _OBJC_IVAR_$_VTTemporalNoiseFilterParameters._destinationFrame
+ _OBJC_IVAR_$_VTTemporalNoiseFilterParameters._discontinuity
+ _OBJC_IVAR_$_VTTemporalNoiseFilterParameters._filterStrength
+ _OBJC_IVAR_$_VTTemporalNoiseFilterParameters._nextFrames
+ _OBJC_IVAR_$_VTTemporalNoiseFilterParameters._previousFrames
+ _OBJC_IVAR_$_VTTemporalNoiseFilterParameters._sourceFrame
+ _OBJC_IVAR_$_VTTestProcessorConfiguration._destinationPixelBufferAttributes
+ _OBJC_IVAR_$_VTTestProcessorConfiguration._flags
+ _OBJC_IVAR_$_VTTestProcessorConfiguration._frameHeight
+ _OBJC_IVAR_$_VTTestProcessorConfiguration._frameSupportedPixelFormats
+ _OBJC_IVAR_$_VTTestProcessorConfiguration._frameWidth
+ _OBJC_IVAR_$_VTTestProcessorConfiguration._sourcePixelBufferAttributes
+ _OBJC_IVAR_$_VTTestProcessorImplementation._flags
+ _OBJC_IVAR_$_VTTestProcessorImplementation._pixelTransferSession
+ _OBJC_IVAR_$_VTTestProcessorParameters._destinationFrame
+ _OBJC_IVAR_$_VTTestProcessorParameters._nextFrame
+ _OBJC_IVAR_$_VTTestProcessorParameters._previousFrame
+ _OBJC_IVAR_$_VTTestProcessorParameters._sourceFrame
+ _OBJC_METACLASS_$_VTFrameProcessor
+ _OBJC_METACLASS_$_VTFrameProcessorFrame
+ _OBJC_METACLASS_$_VTFrameProcessorOpticalFlow
+ _OBJC_METACLASS_$_VTFrameRateConversionConfiguration
+ _OBJC_METACLASS_$_VTFrameRateConversionParameters
+ _OBJC_METACLASS_$_VTLowLatencyFrameInterpolationConfiguration
+ _OBJC_METACLASS_$_VTLowLatencyFrameInterpolationImplementation
+ _OBJC_METACLASS_$_VTLowLatencyFrameInterpolationParameters
+ _OBJC_METACLASS_$_VTLowLatencySuperResolutionScalerConfiguration
+ _OBJC_METACLASS_$_VTLowLatencySuperResolutionScalerImplementation
+ _OBJC_METACLASS_$_VTLowLatencySuperResolutionScalerParameters
+ _OBJC_METACLASS_$_VTMotionBlurConfiguration
+ _OBJC_METACLASS_$_VTMotionBlurParameters
+ _OBJC_METACLASS_$_VTOpticalFlowConfiguration
+ _OBJC_METACLASS_$_VTOpticalFlowParameters
+ _OBJC_METACLASS_$_VTSuperResolutionScalerConfiguration
+ _OBJC_METACLASS_$_VTSuperResolutionScalerParameters
+ _OBJC_METACLASS_$_VTTemporalNoiseFilterConfiguration
+ _OBJC_METACLASS_$_VTTemporalNoiseFilterImplementation
+ _OBJC_METACLASS_$_VTTemporalNoiseFilterParameters
+ _OBJC_METACLASS_$_VTTestProcessorConfiguration
+ _OBJC_METACLASS_$_VTTestProcessorImplementation
+ _OBJC_METACLASS_$_VTTestProcessorParameters
+ _OUTLINED_FUNCTION_100
+ _OUTLINED_FUNCTION_101
+ _OUTLINED_FUNCTION_102
+ _OUTLINED_FUNCTION_103
+ _OUTLINED_FUNCTION_104
+ _OUTLINED_FUNCTION_105
+ _OUTLINED_FUNCTION_70
+ _OUTLINED_FUNCTION_71
+ _OUTLINED_FUNCTION_72
+ _OUTLINED_FUNCTION_73
+ _OUTLINED_FUNCTION_74
+ _OUTLINED_FUNCTION_75
+ _OUTLINED_FUNCTION_76
+ _OUTLINED_FUNCTION_77
+ _OUTLINED_FUNCTION_78
+ _OUTLINED_FUNCTION_79
+ _OUTLINED_FUNCTION_80
+ _OUTLINED_FUNCTION_81
+ _OUTLINED_FUNCTION_82
+ _OUTLINED_FUNCTION_83
+ _OUTLINED_FUNCTION_84
+ _OUTLINED_FUNCTION_85
+ _OUTLINED_FUNCTION_86
+ _OUTLINED_FUNCTION_87
+ _OUTLINED_FUNCTION_88
+ _OUTLINED_FUNCTION_89
+ _OUTLINED_FUNCTION_90
+ _OUTLINED_FUNCTION_91
+ _OUTLINED_FUNCTION_92
+ _OUTLINED_FUNCTION_93
+ _OUTLINED_FUNCTION_94
+ _OUTLINED_FUNCTION_95
+ _OUTLINED_FUNCTION_96
+ _OUTLINED_FUNCTION_97
+ _OUTLINED_FUNCTION_98
+ _OUTLINED_FUNCTION_99
+ _ParavirtualizedMotionEstimationProcessor_CompleteFrames
+ _ParavirtualizedMotionEstimationProcessor_CopyDebugDescription
+ _ParavirtualizedMotionEstimationProcessor_CopyProperty
+ _ParavirtualizedMotionEstimationProcessor_CopySerializableProperties
+ _ParavirtualizedMotionEstimationProcessor_CopySupportedPropertyDictionary
+ _ParavirtualizedMotionEstimationProcessor_CreateInstance
+ _ParavirtualizedMotionEstimationProcessor_CreateInstance.cold.1
+ _ParavirtualizedMotionEstimationProcessor_CreateInstance.cold.2
+ _ParavirtualizedMotionEstimationProcessor_CreateInstance.cold.3
+ _ParavirtualizedMotionEstimationProcessor_Finalize
+ _ParavirtualizedMotionEstimationProcessor_Invalidate
+ _ParavirtualizedMotionEstimationProcessor_ProcessFrames
+ _ParavirtualizedMotionEstimationProcessor_ProcessFrames.cold.1
+ _ParavirtualizedMotionEstimationProcessor_ProcessFrames.cold.2
+ _ParavirtualizedMotionEstimationProcessor_ProcessFrames.cold.3
+ _ParavirtualizedMotionEstimationProcessor_ProcessFrames.cold.4
+ _ParavirtualizedMotionEstimationProcessor_ProcessFrames.cold.5
+ _ParavirtualizedMotionEstimationProcessor_ProcessFrames.cold.6
+ _ParavirtualizedMotionEstimationProcessor_ProcessFrames.cold.7
+ _ParavirtualizedMotionEstimationProcessor_SetProperties
+ _ParavirtualizedMotionEstimationProcessor_SetProperty
+ _ParavirtualizedMotionEstimationProcessor_StartSession
+ _RegisterVTDeghostingFrameBuffer
+ _RegisterVTDeghostingProcessorType
+ _RegisterVTDeghostingSession
+ _TestIPBVideoDecoder_DecodeFrameSynchronously
+ _TestIPBVideoDecoder_Invalidate
+ _TestIPBVideoDecoder_WorkerThread
+ _TestIPBVideoDecoder_WorkerThread.cold.1
+ _TestIPBVideoEncoder_EncodeMultiImageFrame.cold.6
+ _TestIPBVideoEncoder_EncodeMultiImageFrame.cold.7
+ _VTCompressionSessionCreateWithOptions.cold.5
+ _VTCompressionSessionCreateWithOptions.cold.6
+ _VTCompressionSessionRemoteClient_CompleteTemporalFilterFrames
+ _VTCompressionSessionRemoteClient_CopyTemporalFilterList
+ _VTCompressionSessionRemoteClient_TemporalFilterCreate
+ _VTCompressionSessionRemoteClient_TemporalProcessFrame
+ _VTCompressionSessionRemoteServer_CompleteTemporalFilterFrames
+ _VTCompressionSessionRemoteServer_CopyTemporalFilterList
+ _VTCompressionSessionRemoteServer_TemporalFilterCreate
+ _VTCompressionSessionRemoteServer_TemporalProcessFrame
+ _VTCompressionSessionSetProperty.cold.1
+ _VTCompressionSessionSetProperty.cold.2
+ _VTCreateArrayRepresentationOfHomographyMatrix
+ _VTCreateHomographyMatrixWithArrayRepresentation
+ _VTDecoderSessionEmitDecodedFrame.cold.1
+ _VTDecoderSessionRegisterCustomPixelFormat.cold.1
+ _VTDecoderSessionRegisterCustomPixelFormat.cold.2
+ _VTDecompressionSessionAnalyzeAndInterruptFrame
+ _VTDecompressionSessionCreateWithOptions.cold.6
+ _VTDecompressionSessionRemoteBridge_Create.cold.3
+ _VTDecompressionSessionRemote_CanAcceptFormatDescription.cold.2
+ _VTDecompressionSessionRemote_CanAcceptFormatDescription.cold.3
+ _VTDecompressionSessionRemote_GetMinOutputPresentationTimeStampOfFramesBeingDecoded.cold.1
+ _VTDecompressionSessionRemote_GetMinOutputPresentationTimeStampOfFramesBeingDecoded.cold.2
+ _VTDecompressionSessionSetContentAnalyzer
+ _VTDeghostingFrameBufferCreate
+ _VTDeghostingFrameBufferGetFrame
+ _VTDeghostingFrameBufferGetParameters
+ _VTDeghostingFrameBufferGetTypeID
+ _VTDeghostingFrameBufferGetTypeID.sVTDeghostingFrameBufferOnce
+ _VTDeghostingProcessorCopyFormattingDesc
+ _VTDeghostingProcessorGetCMBaseObject
+ _VTDeghostingProcessorGetClassID
+ _VTDeghostingProcessorGetClassID.sRegisterVTDeghostingProcessorTypeOnce
+ _VTDeghostingProcessorGetTypeID
+ _VTDeghostingProcessorSessionEmitRepair
+ _VTDeghostingProcessorSessionEmitRepair.cold.1
+ _VTDeghostingProcessorSessionEmitStatistics
+ _VTDeghostingProcessorSessionEmitStatistics.cold.1
+ _VTDeghostingSessionCopyProperty
+ _VTDeghostingSessionCopyProperty.cold.1
+ _VTDeghostingSessionCopyProperty.cold.2
+ _VTDeghostingSessionCopyProperty.cold.3
+ _VTDeghostingSessionCopyProperty.cold.4
+ _VTDeghostingSessionCopyProperty.cold.5
+ _VTDeghostingSessionCopySerializableProperties
+ _VTDeghostingSessionCopySerializableProperties.cold.1
+ _VTDeghostingSessionCopySerializableProperties.cold.2
+ _VTDeghostingSessionCopySerializableProperties.cold.3
+ _VTDeghostingSessionCopySerializableProperties.cold.4
+ _VTDeghostingSessionCopySupportedPropertyDictionary
+ _VTDeghostingSessionCopySupportedPropertyDictionary.cold.1
+ _VTDeghostingSessionCopySupportedPropertyDictionary.cold.2
+ _VTDeghostingSessionCopySupportedPropertyDictionary.cold.3
+ _VTDeghostingSessionCopySupportedPropertyDictionary.cold.4
+ _VTDeghostingSessionCopySupportedPropertyDictionary.cold.5
+ _VTDeghostingSessionCopySupportedPropertyDictionary.cold.6
+ _VTDeghostingSessionCopySupportedPropertyDictionary.cold.7
+ _VTDeghostingSessionCreateForGeneratingStatistics
+ _VTDeghostingSessionCreateForRepairingImages
+ _VTDeghostingSessionGetTypeID
+ _VTDeghostingSessionInvalidate
+ _VTDeghostingSessionMitigateGhosts
+ _VTDeghostingSessionMitigateGhosts.cold.1
+ _VTDeghostingSessionMitigateGhosts.cold.2
+ _VTDeghostingSessionMitigateGhosts.cold.3
+ _VTDeghostingSessionMitigateGhosts.cold.4
+ _VTDeghostingSessionMitigateGhosts.cold.5
+ _VTDeghostingSessionMitigateGhosts.cold.6
+ _VTDeghostingSessionMitigateGhosts2
+ _VTDeghostingSessionMitigateGhosts2.cold.1
+ _VTDeghostingSessionMitigateGhosts2.cold.2
+ _VTDeghostingSessionMitigateGhosts2.cold.3
+ _VTDeghostingSessionMitigateGhosts2.cold.4
+ _VTDeghostingSessionMitigateGhosts2.cold.5
+ _VTDeghostingSessionMitigateGhosts2.cold.6
+ _VTDeghostingSessionRequestStatistics
+ _VTDeghostingSessionRequestStatistics.cold.1
+ _VTDeghostingSessionRequestStatistics.cold.2
+ _VTDeghostingSessionRequestStatistics.cold.3
+ _VTDeghostingSessionRequestStatistics.cold.4
+ _VTDeghostingSessionRequestStatistics.cold.5
+ _VTDeghostingSessionRequestStatistics2
+ _VTDeghostingSessionRequestStatistics2.cold.1
+ _VTDeghostingSessionRequestStatistics2.cold.2
+ _VTDeghostingSessionRequestStatistics2.cold.3
+ _VTDeghostingSessionRequestStatistics2.cold.4
+ _VTDeghostingSessionRequestStatistics2.cold.5
+ _VTDeghostingSessionSetProperties
+ _VTDeghostingSessionSetProperties.cold.1
+ _VTDeghostingSessionSetProperties.cold.2
+ _VTDeghostingSessionSetProperties.cold.3
+ _VTDeghostingSessionSetProperties.cold.4
+ _VTDeghostingSessionSetProperties.cold.5
+ _VTDeghostingSessionSetProperty
+ _VTDeghostingSessionSetProperty.cold.1
+ _VTDeghostingSessionSetProperty.cold.2
+ _VTDeghostingSessionSetProperty.cold.3
+ _VTDeghostingSessionSetProperty.cold.4
+ _VTDeghostingSessionSetProperty.cold.5
+ _VTEncoderSessionCreateVideoSecurityInfoExtension
+ _VTEncoderSessionCreateVideoSecurityInfoExtension.cold.1
+ _VTEncoderSessionCreateVideoSecurityInfoExtension.cold.2
+ _VTFrameProcessorErrorDomain
+ _VTFrameSiloGetProgressOfCurrentPass.cold.3
+ _VTFrameSiloGetProgressOfCurrentPass.cold.4
+ _VTFrameSiloGetProgressOfCurrentPass.cold.5
+ _VTGetOnePassScalingPropertyValue
+ _VTHDRImageStatisticsGenerationSessionCreate.cold.4
+ _VTHDRImageStatisticsGenerationSessionCreate.cold.5
+ _VTHDRMetadataGenerationSessionCopySessionState
+ _VTHDRMetadataGenerationSessionCreate.cold.1
+ _VTHDRMetadataGenerationSessionCreate.cold.10
+ _VTHDRMetadataGenerationSessionCreate.cold.11
+ _VTHDRMetadataGenerationSessionCreate.cold.12
+ _VTHDRMetadataGenerationSessionCreate.cold.13
+ _VTHDRMetadataGenerationSessionCreate.cold.14
+ _VTHDRMetadataGenerationSessionCreate.cold.15
+ _VTHDRMetadataGenerationSessionCreate.cold.16
+ _VTHDRMetadataGenerationSessionCreate.cold.17
+ _VTHDRMetadataGenerationSessionCreate.cold.18
+ _VTHDRMetadataGenerationSessionCreate.cold.2
+ _VTHDRMetadataGenerationSessionCreate.cold.3
+ _VTHDRMetadataGenerationSessionCreate.cold.4
+ _VTHDRMetadataGenerationSessionCreate.cold.5
+ _VTHDRMetadataGenerationSessionCreate.cold.6
+ _VTHDRMetadataGenerationSessionCreate.cold.7
+ _VTHDRMetadataGenerationSessionCreate.cold.8
+ _VTHDRMetadataGenerationSessionCreate.cold.9
+ _VTHDRMetadataGenerationSessionCreateDataFromStatistics.cold.13
+ _VTHDRMetadataGenerationSessionCreateDataFromStatisticsDictionary.cold.1
+ _VTHDRMetadataGenerationSessionCreateSDRPreservationStaticData
+ _VTHDRMetadataGenerationSessionSetFramesPerSecond.cold.3
+ _VTIsBackgroundRunningSupportedForClientPID
+ _VTIsBackgroundRunningSupportedForClientPID.cold.1
+ _VTIsBackgroundRunningSupportedForClientPID.cold.2
+ _VTIsBackgroundRunningSupportedForClientPID.onceToken
+ _VTIsMVHEVCWithAlphaDecodingEnabledViaDefaults
+ _VTIsMVHEVCWithAlphaDecodingEnabledViaDefaults.cold.1
+ _VTIsMVHEVCWithAlphaDecodingEnabledViaDefaults.enableMVHEVCWithAlphaDecoding
+ _VTIsMVHEVCWithAlphaDecodingEnabledViaDefaults.mvhevcWithAlphaCheckOnce
+ _VTIsPixelBufferProtected
+ _VTMTSRenderPassBarrierGetTypeID.sRegisterVTMTSRenderPassBarrierOnce
+ _VTMTSRenderPassDescriptorGetTypeID.sRegisterVTMTSRenderPassDescriptorOnce
+ _VTMakePixelBufferPoolSharingIDFromSource
+ _VTMetalTransferSessionGetTypeID
+ _VTMetalTransferSessionSetPropertyInternal
+ _VTMotionEstimationProcessorSelectAndCreateInstance
+ _VTMotionEstimationProcessorSelectAndCreateInstance.cold.1
+ _VTMotionEstimationProcessorSelectAndCreateInstance.cold.2
+ _VTMotionEstimationProcessorSelectAndCreateInstance.cold.3
+ _VTMotionEstimationProcessorSelectAndCreateInstance.cold.4
+ _VTMotionEstimationProcessorSessionCleanUpAfterProcessing
+ _VTMotionEstimationProcessorSessionCreateMotionVectorPixelBufferWithOptions
+ _VTMotionEstimationProcessorSessionCreateMotionVectorPixelBufferWithOptions.cold.1
+ _VTMotionEstimationProcessorSessionCreateMotionVectorPixelBufferWithOptions.cold.2
+ _VTMotionEstimationSessionCopySerializableProperties.cold.2
+ _VTMotionEstimationSessionCopySerializableProperties.cold.3
+ _VTMotionEstimationSessionCopySerializableProperties.cold.4
+ _VTMultiPassStorageCreate.cold.4
+ _VTMultiPassStorageRemote_Create.cold.2
+ _VTMultiPassStorageRemote_Create.cold.3
+ _VTMultiPassStorageRemote_Create.cold.4
+ _VTMultiPassStorageRemote_Create.cold.5
+ _VTNextUniquePixelBufferPoolSharingIDFromSource
+ _VTNextUniquePixelBufferPoolSharingIDFromSource.sUniqueID
+ _VTParavirtualizationCopyFilteredPixelBufferAttributes
+ _VTParavirtualizationCopyFilteredPixelBufferAttributes.cold.1
+ _VTParavirtualizationCreateMessageBoxToRelinquishSurfaceMappingIDs
+ _VTParavirtualizationCreateMessageBoxToRelinquishSurfaceMappingIDs.cold.1
+ _VTParavirtualizationCreateMessageBoxToRelinquishSurfaceMappingIDs.cold.2
+ _VTParavirtualizationCreateSampleBufferFromSerializedAtomDataBlockBuffer.cold.16
+ _VTParavirtualizationCreateSampleBufferFromSerializedAtomDataBlockBuffer.cold.17
+ _VTParavirtualizationCreateSampleBufferFromSerializedAtomDataBlockBuffer.cold.18
+ _VTParavirtualizationFigErrorHexDump
+ _VTParavirtualizationHostCopyDecoderCapabilitiesReply
+ _VTParavirtualizationHostCopyDecoderListReply
+ _VTParavirtualizationHostCopyEncoderListReply
+ _VTParavirtualizationHostCopyMotionEstimationProcessorListReply
+ _VTParavirtualizationHostDecoderSessionCleanUpAfterDecode
+ _VTParavirtualizationHostDecoderSessionCleanUpAfterTileDecode
+ _VTParavirtualizationHostDecoderSessionCompleteInvalidate
+ _VTParavirtualizationHostDecoderSessionCreate
+ _VTParavirtualizationHostDecoderSessionCreatePixelBufferWithOptions
+ _VTParavirtualizationHostDecoderSessionCreatePixelBufferWithOptions.cold.1
+ _VTParavirtualizationHostDecoderSessionCreatePixelBufferWithOptions.cold.2
+ _VTParavirtualizationHostDecoderSessionCreatePixelBufferWithOptions.cold.3
+ _VTParavirtualizationHostDecoderSessionDeliverMessageFromGuest
+ _VTParavirtualizationHostDecoderSessionEmitDecodedFrame
+ _VTParavirtualizationHostDecoderSessionEmitDecodedMultiImageFrame
+ _VTParavirtualizationHostDecoderSessionEmitDecodedMultiImageFrame.cold.1
+ _VTParavirtualizationHostDecoderSessionEmitDecodedMultiImageFrame.cold.2
+ _VTParavirtualizationHostDecoderSessionEmitDecodedTile
+ _VTParavirtualizationHostDecoderSessionGetDestinationPixelBufferAttributes
+ _VTParavirtualizationHostDecoderSessionInvalidate
+ _VTParavirtualizationHostDecoderSessionSetPixelBufferAttributes
+ _VTParavirtualizationHostDecoderSessionSetTileDecodeRequirements
+ _VTParavirtualizationHostEncoderSessionCompleteInvalidate
+ _VTParavirtualizationHostEncoderSessionCreate
+ _VTParavirtualizationHostEncoderSessionCreateTileVideoFormatDescription
+ _VTParavirtualizationHostEncoderSessionCreateVideoFormatDescription
+ _VTParavirtualizationHostEncoderSessionDeliverMessageFromGuest
+ _VTParavirtualizationHostEncoderSessionEmitEncodedFrame
+ _VTParavirtualizationHostEncoderSessionEmitEncodedTile
+ _VTParavirtualizationHostEncoderSessionInvalidate
+ _VTParavirtualizationHostEncoderSessionMultipassStorageCopyDataAtTimeStamp
+ _VTParavirtualizationHostEncoderSessionMultipassStorageCopyIdentifier
+ _VTParavirtualizationHostEncoderSessionMultipassStorageGetTimeStamp
+ _VTParavirtualizationHostEncoderSessionMultipassStorageGetTimeStampAndDuration
+ _VTParavirtualizationHostEncoderSessionMultipassStorageInvalidate
+ _VTParavirtualizationHostEncoderSessionMultipassStorageSetDataAtTimeStamp
+ _VTParavirtualizationHostEncoderSessionMultipassStorageSetIdentifier
+ _VTParavirtualizationHostEncoderSessionSetPixelBufferAttributes
+ _VTParavirtualizationHostEncoderSessionSetTileAttributes
+ _VTParavirtualizationHostEncoderSessionSetTileEncodeRequirements
+ _VTParavirtualizationHostEncoderSessionSetTimeRangesForNextPass
+ _VTParavirtualizationHostMotionEstimationProcessorCreate
+ _VTParavirtualizationHostMotionEstimationProcessorSessionCleanUpAfterProcessing
+ _VTParavirtualizationHostMotionEstimationProcessorSessionCompleteInvalidate
+ _VTParavirtualizationHostMotionEstimationProcessorSessionCreateMotionVectorPixelBufferWithOptions
+ _VTParavirtualizationHostMotionEstimationProcessorSessionDeliverMessageFromGuest
+ _VTParavirtualizationHostMotionEstimationProcessorSessionEmitMotionVectors
+ _VTParavirtualizationHostMotionEstimationProcessorSessionInvalidate
+ _VTParavirtualizationHostMotionEstimationProcessorSessionSetMotionVectorPixelBufferAttributes
+ _VTParavirtualizationHostMotionEstimationProcessorSessionSetSourcePixelBufferAttributes
+ _VTParavirtualizationHostSessionCompleteInvalidate
+ _VTParavirtualizationHostSessionCreate
+ _VTParavirtualizationHostSessionCreate.cold.1
+ _VTParavirtualizationHostSessionCreate.cold.2
+ _VTParavirtualizationHostSessionCreate.cold.3
+ _VTParavirtualizationHostSessionCreate.cold.4
+ _VTParavirtualizationHostSessionCreate.cold.5
+ _VTParavirtualizationHostSessionCreate.cold.6
+ _VTParavirtualizationHostSessionCreateTerminateAllSessionsMessage
+ _VTParavirtualizationHostSessionCreateTerminateAllSessionsMessage.kTerminateAllSessionsMessage
+ _VTParavirtualizationHostSessionDeliverMessageFromGuest
+ _VTParavirtualizationHostSessionGetTypeID
+ _VTParavirtualizationHostSessionGetTypeID.cold.1
+ _VTParavirtualizationHostSessionInvalidate
+ _VTParavirtualizationMessageAppendPixelBufferAndIOSurfaceAttachments.cold.3
+ _VTParavirtualizationMessageCopyFigTagCollectionArray.cold.4
+ _VTParavirtualizationMessageCopyFigTagCollectionArray.cold.5
+ _VTParavirtualizationPixelBufferAttributesContainIOSurfaceProtectionOptions
+ _VTParavirtualizedHostJPEGSupportHandleMessage
+ _VTParavirtualizedHostJPEGSupportHandleMessage.cold.1
+ _VTParavirtualizedHostJPEGSupportHandleMessage.cold.2
+ _VTParavirtualizedHostJPEGSupportHandleMessage.cold.3
+ _VTPixelBufferAttributesMediatorCopyProperty.cold.9
+ _VTPixelBufferAttributesMediatorCreate.cold.4
+ _VTPixelBufferAttributesMediatorCreate.cold.5
+ _VTPixelBufferAttributesMediatorCreate.cold.6
+ _VTPixelBufferConformerCopyConformedTaggedBufferGroup.cold.1
+ _VTPixelBufferConformerCopyConformedTaggedBufferGroup.cold.2
+ _VTPixelBufferConformerCopyConformedTaggedBufferGroup.cold.3
+ _VTPixelBufferConformerCopyConformedTaggedBufferGroup.cold.4
+ _VTPixelGraphMetalDirectBlitterTable
+ _VTPixelTransferGraphBuildChain.cold.1
+ _VTPixelTransferGraphBuildChain.cold.2
+ _VTPixelTransferSessionGetNextDirectMetalBlitter
+ _VTReadOnePassMetalScalingFeatureFlag
+ _VTRequiresUnalignedBlackFill
+ _VTSessionGetBooleanIfPresent
+ _VTSessionSetBooleanProperty
+ _VTTemporalFilterPluginCopyProperty
+ _VTTemporalFilterPluginSessionCleanUpAfterProcessing
+ _VTTemporalFilterPluginSessionCreateOutputPixelBuffer
+ _VTTemporalFilterPluginSessionCreateOutputPixelBuffer.cold.1
+ _VTTemporalFilterPluginSessionCreateOutputPixelBuffer.cold.2
+ _VTTemporalFilterPluginSessionCreateOutputPixelBuffer.cold.3
+ _VTTemporalFilterPluginSessionCreateOutputPixelBuffer.cold.4
+ _VTTemporalFilterPluginSessionCreateOutputPixelBuffer.cold.5
+ _VTTemporalFilterRemote_CopyList
+ _VTTemporalFilterSessionCopySupportedPropertyDictionary.cold.1
+ _VTTemporalFilterSessionCreate.cold.4
+ _VTTemporalFilterSessionProcessFrameWithOutputPixelBuffer
+ _VTTemporalFilterSessionProcessFrameWithOutputPixelBuffer.cold.1
+ _VTTemporalFilterSessionProcessFrameWithOutputPixelBuffer.cold.2
+ _VTTemporalFilterSessionProcessFrameWithOutputPixelBuffer.cold.3
+ _VTTemporalFilterSessionRemote_CompleteFrames
+ _VTTemporalFilterSessionRemote_CompleteFrames.cold.1
+ _VTTemporalFilterSessionRemote_Create
+ _VTTemporalFilterSessionRemote_ProcessFrame
+ _VTVideoCodecService_ShouldUseSeparateCodecProcessForEncode.featureOnHomePodEnabled
+ __DASContinuedProcessingTaskAssertionTag
+ __MergedGlobals.127
+ __MergedGlobals.56
+ __OBJC_$_CLASS_METHODS_VTFrameRateConversionConfiguration
+ __OBJC_$_CLASS_METHODS_VTLowLatencyFrameInterpolationConfiguration
+ __OBJC_$_CLASS_METHODS_VTLowLatencySuperResolutionScalerConfiguration
+ __OBJC_$_CLASS_METHODS_VTMotionBlurConfiguration
+ __OBJC_$_CLASS_METHODS_VTOpticalFlowConfiguration
+ __OBJC_$_CLASS_METHODS_VTSuperResolutionScalerConfiguration
+ __OBJC_$_CLASS_METHODS_VTTemporalNoiseFilterConfiguration
+ __OBJC_$_CLASS_METHODS_VTTestProcessorConfiguration
+ __OBJC_$_CLASS_PROP_LIST_VTFrameProcessorConfiguration
+ __OBJC_$_CLASS_PROP_LIST_VTFrameRateConversionConfiguration
+ __OBJC_$_CLASS_PROP_LIST_VTLowLatencyFrameInterpolationConfiguration
+ __OBJC_$_CLASS_PROP_LIST_VTLowLatencySuperResolutionScalerConfiguration
+ __OBJC_$_CLASS_PROP_LIST_VTMotionBlurConfiguration
+ __OBJC_$_CLASS_PROP_LIST_VTOpticalFlowConfiguration
+ __OBJC_$_CLASS_PROP_LIST_VTSuperResolutionScalerConfiguration
+ __OBJC_$_CLASS_PROP_LIST_VTTemporalNoiseFilterConfiguration
+ __OBJC_$_CLASS_PROP_LIST_VTTestProcessorConfiguration
+ __OBJC_$_INSTANCE_METHODS_VTFrameProcessor
+ __OBJC_$_INSTANCE_METHODS_VTFrameProcessorFrame
+ __OBJC_$_INSTANCE_METHODS_VTFrameProcessorOpticalFlow
+ __OBJC_$_INSTANCE_METHODS_VTFrameRateConversionConfiguration
+ __OBJC_$_INSTANCE_METHODS_VTFrameRateConversionParameters
+ __OBJC_$_INSTANCE_METHODS_VTLowLatencyFrameInterpolationConfiguration
+ __OBJC_$_INSTANCE_METHODS_VTLowLatencyFrameInterpolationImplementation
+ __OBJC_$_INSTANCE_METHODS_VTLowLatencyFrameInterpolationParameters
+ __OBJC_$_INSTANCE_METHODS_VTLowLatencySuperResolutionScalerConfiguration
+ __OBJC_$_INSTANCE_METHODS_VTLowLatencySuperResolutionScalerImplementation
+ __OBJC_$_INSTANCE_METHODS_VTLowLatencySuperResolutionScalerParameters
+ __OBJC_$_INSTANCE_METHODS_VTMotionBlurConfiguration
+ __OBJC_$_INSTANCE_METHODS_VTMotionBlurParameters
+ __OBJC_$_INSTANCE_METHODS_VTOpticalFlowConfiguration
+ __OBJC_$_INSTANCE_METHODS_VTOpticalFlowParameters
+ __OBJC_$_INSTANCE_METHODS_VTSuperResolutionScalerConfiguration
+ __OBJC_$_INSTANCE_METHODS_VTSuperResolutionScalerParameters
+ __OBJC_$_INSTANCE_METHODS_VTTemporalNoiseFilterConfiguration
+ __OBJC_$_INSTANCE_METHODS_VTTemporalNoiseFilterImplementation
+ __OBJC_$_INSTANCE_METHODS_VTTemporalNoiseFilterParameters
+ __OBJC_$_INSTANCE_METHODS_VTTestProcessorConfiguration
+ __OBJC_$_INSTANCE_METHODS_VTTestProcessorImplementation
+ __OBJC_$_INSTANCE_METHODS_VTTestProcessorParameters
+ __OBJC_$_INSTANCE_VARIABLES_VTFrameProcessor
+ __OBJC_$_INSTANCE_VARIABLES_VTFrameProcessorFrame
+ __OBJC_$_INSTANCE_VARIABLES_VTFrameProcessorOpticalFlow
+ __OBJC_$_INSTANCE_VARIABLES_VTFrameRateConversionConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_VTFrameRateConversionParameters
+ __OBJC_$_INSTANCE_VARIABLES_VTLowLatencyFrameInterpolationConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_VTLowLatencyFrameInterpolationImplementation
+ __OBJC_$_INSTANCE_VARIABLES_VTLowLatencyFrameInterpolationParameters
+ __OBJC_$_INSTANCE_VARIABLES_VTLowLatencySuperResolutionScalerConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_VTLowLatencySuperResolutionScalerImplementation
+ __OBJC_$_INSTANCE_VARIABLES_VTLowLatencySuperResolutionScalerParameters
+ __OBJC_$_INSTANCE_VARIABLES_VTMotionBlurConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_VTMotionBlurParameters
+ __OBJC_$_INSTANCE_VARIABLES_VTOpticalFlowConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_VTOpticalFlowParameters
+ __OBJC_$_INSTANCE_VARIABLES_VTSuperResolutionScalerConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_VTSuperResolutionScalerParameters
+ __OBJC_$_INSTANCE_VARIABLES_VTTemporalNoiseFilterConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_VTTemporalNoiseFilterImplementation
+ __OBJC_$_INSTANCE_VARIABLES_VTTemporalNoiseFilterParameters
+ __OBJC_$_INSTANCE_VARIABLES_VTTestProcessorConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_VTTestProcessorImplementation
+ __OBJC_$_INSTANCE_VARIABLES_VTTestProcessorParameters
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST_VTFrameProcessorConfiguration
+ __OBJC_$_PROP_LIST_VTFrameProcessorFrame
+ __OBJC_$_PROP_LIST_VTFrameProcessorOpticalFlow
+ __OBJC_$_PROP_LIST_VTFrameProcessorParameters
+ __OBJC_$_PROP_LIST_VTFrameRateConversionConfiguration
+ __OBJC_$_PROP_LIST_VTFrameRateConversionParameters
+ __OBJC_$_PROP_LIST_VTLowLatencyFrameInterpolationConfiguration
+ __OBJC_$_PROP_LIST_VTLowLatencyFrameInterpolationImplementation
+ __OBJC_$_PROP_LIST_VTLowLatencyFrameInterpolationParameters
+ __OBJC_$_PROP_LIST_VTLowLatencySuperResolutionScalerConfiguration
+ __OBJC_$_PROP_LIST_VTLowLatencySuperResolutionScalerImplementation
+ __OBJC_$_PROP_LIST_VTLowLatencySuperResolutionScalerParameters
+ __OBJC_$_PROP_LIST_VTMotionBlurConfiguration
+ __OBJC_$_PROP_LIST_VTMotionBlurParameters
+ __OBJC_$_PROP_LIST_VTOpticalFlowConfiguration
+ __OBJC_$_PROP_LIST_VTOpticalFlowParameters
+ __OBJC_$_PROP_LIST_VTSuperResolutionScalerConfiguration
+ __OBJC_$_PROP_LIST_VTSuperResolutionScalerParameters
+ __OBJC_$_PROP_LIST_VTTemporalNoiseFilterConfiguration
+ __OBJC_$_PROP_LIST_VTTemporalNoiseFilterImplementation
+ __OBJC_$_PROP_LIST_VTTemporalNoiseFilterParameters
+ __OBJC_$_PROP_LIST_VTTestProcessorConfiguration
+ __OBJC_$_PROP_LIST_VTTestProcessorImplementation
+ __OBJC_$_PROP_LIST_VTTestProcessorParameters
+ __OBJC_$_PROTOCOL_CLASS_METHODS_OPT_VTFrameProcessorConfiguration
+ __OBJC_$_PROTOCOL_CLASS_METHODS_VTFrameProcessorConfiguration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_VTFrameProcessorConfiguration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_VTFrameProcessorParameters
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_VTFrameProcessorConfiguration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_VTFrameProcessorImplementationPrivate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_VTFrameProcessorParameters
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_VTFrameProcessorConfiguration
+ __OBJC_$_PROTOCOL_METHOD_TYPES_VTFrameProcessorImplementationPrivate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_VTFrameProcessorParameters
+ __OBJC_$_PROTOCOL_REFS_VTFrameProcessorConfiguration
+ __OBJC_$_PROTOCOL_REFS_VTFrameProcessorImplementationPrivate
+ __OBJC_$_PROTOCOL_REFS_VTFrameProcessorParameters
+ __OBJC_CLASS_PROTOCOLS_$_VTFrameRateConversionConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_VTFrameRateConversionParameters
+ __OBJC_CLASS_PROTOCOLS_$_VTLowLatencyFrameInterpolationConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_VTLowLatencyFrameInterpolationImplementation
+ __OBJC_CLASS_PROTOCOLS_$_VTLowLatencyFrameInterpolationParameters
+ __OBJC_CLASS_PROTOCOLS_$_VTLowLatencySuperResolutionScalerConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_VTLowLatencySuperResolutionScalerImplementation
+ __OBJC_CLASS_PROTOCOLS_$_VTLowLatencySuperResolutionScalerParameters
+ __OBJC_CLASS_PROTOCOLS_$_VTMotionBlurConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_VTMotionBlurParameters
+ __OBJC_CLASS_PROTOCOLS_$_VTOpticalFlowConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_VTOpticalFlowParameters
+ __OBJC_CLASS_PROTOCOLS_$_VTSuperResolutionScalerConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_VTSuperResolutionScalerParameters
+ __OBJC_CLASS_PROTOCOLS_$_VTTemporalNoiseFilterConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_VTTemporalNoiseFilterImplementation
+ __OBJC_CLASS_PROTOCOLS_$_VTTemporalNoiseFilterParameters
+ __OBJC_CLASS_PROTOCOLS_$_VTTestProcessorConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_VTTestProcessorImplementation
+ __OBJC_CLASS_PROTOCOLS_$_VTTestProcessorParameters
+ __OBJC_CLASS_RO_$_VTFrameProcessor
+ __OBJC_CLASS_RO_$_VTFrameProcessorFrame
+ __OBJC_CLASS_RO_$_VTFrameProcessorOpticalFlow
+ __OBJC_CLASS_RO_$_VTFrameRateConversionConfiguration
+ __OBJC_CLASS_RO_$_VTFrameRateConversionParameters
+ __OBJC_CLASS_RO_$_VTLowLatencyFrameInterpolationConfiguration
+ __OBJC_CLASS_RO_$_VTLowLatencyFrameInterpolationImplementation
+ __OBJC_CLASS_RO_$_VTLowLatencyFrameInterpolationParameters
+ __OBJC_CLASS_RO_$_VTLowLatencySuperResolutionScalerConfiguration
+ __OBJC_CLASS_RO_$_VTLowLatencySuperResolutionScalerImplementation
+ __OBJC_CLASS_RO_$_VTLowLatencySuperResolutionScalerParameters
+ __OBJC_CLASS_RO_$_VTMotionBlurConfiguration
+ __OBJC_CLASS_RO_$_VTMotionBlurParameters
+ __OBJC_CLASS_RO_$_VTOpticalFlowConfiguration
+ __OBJC_CLASS_RO_$_VTOpticalFlowParameters
+ __OBJC_CLASS_RO_$_VTSuperResolutionScalerConfiguration
+ __OBJC_CLASS_RO_$_VTSuperResolutionScalerParameters
+ __OBJC_CLASS_RO_$_VTTemporalNoiseFilterConfiguration
+ __OBJC_CLASS_RO_$_VTTemporalNoiseFilterImplementation
+ __OBJC_CLASS_RO_$_VTTemporalNoiseFilterParameters
+ __OBJC_CLASS_RO_$_VTTestProcessorConfiguration
+ __OBJC_CLASS_RO_$_VTTestProcessorImplementation
+ __OBJC_CLASS_RO_$_VTTestProcessorParameters
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_VTFrameProcessorConfiguration
+ __OBJC_LABEL_PROTOCOL_$_VTFrameProcessorImplementationPrivate
+ __OBJC_LABEL_PROTOCOL_$_VTFrameProcessorParameters
+ __OBJC_METACLASS_RO_$_VTFrameProcessor
+ __OBJC_METACLASS_RO_$_VTFrameProcessorFrame
+ __OBJC_METACLASS_RO_$_VTFrameProcessorOpticalFlow
+ __OBJC_METACLASS_RO_$_VTFrameRateConversionConfiguration
+ __OBJC_METACLASS_RO_$_VTFrameRateConversionParameters
+ __OBJC_METACLASS_RO_$_VTLowLatencyFrameInterpolationConfiguration
+ __OBJC_METACLASS_RO_$_VTLowLatencyFrameInterpolationImplementation
+ __OBJC_METACLASS_RO_$_VTLowLatencyFrameInterpolationParameters
+ __OBJC_METACLASS_RO_$_VTLowLatencySuperResolutionScalerConfiguration
+ __OBJC_METACLASS_RO_$_VTLowLatencySuperResolutionScalerImplementation
+ __OBJC_METACLASS_RO_$_VTLowLatencySuperResolutionScalerParameters
+ __OBJC_METACLASS_RO_$_VTMotionBlurConfiguration
+ __OBJC_METACLASS_RO_$_VTMotionBlurParameters
+ __OBJC_METACLASS_RO_$_VTOpticalFlowConfiguration
+ __OBJC_METACLASS_RO_$_VTOpticalFlowParameters
+ __OBJC_METACLASS_RO_$_VTSuperResolutionScalerConfiguration
+ __OBJC_METACLASS_RO_$_VTSuperResolutionScalerParameters
+ __OBJC_METACLASS_RO_$_VTTemporalNoiseFilterConfiguration
+ __OBJC_METACLASS_RO_$_VTTemporalNoiseFilterImplementation
+ __OBJC_METACLASS_RO_$_VTTemporalNoiseFilterParameters
+ __OBJC_METACLASS_RO_$_VTTestProcessorConfiguration
+ __OBJC_METACLASS_RO_$_VTTestProcessorImplementation
+ __OBJC_METACLASS_RO_$_VTTestProcessorParameters
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_VTFrameProcessorConfiguration
+ __OBJC_PROTOCOL_$_VTFrameProcessorImplementationPrivate
+ __OBJC_PROTOCOL_$_VTFrameProcessorParameters
+ __XCompleteTemporalFilterFrames
+ __XCopyTemporalFilterList
+ __XTemporalFilterCreate
+ __XTemporalProcessFrame
+ ___30-[VTFrameProcessor endSession]_block_invoke
+ ___48-[VTFrameProcessor processWithParameters:error:]_block_invoke
+ ___54-[VTTemporalNoiseFilterImplementation _completeFrame:]_block_invoke
+ ___56-[VTFrameProcessor processWithCommandBuffer:parameters:]_block_invoke
+ ___56-[VTFrameProcessor processWithCommandBuffer:parameters:]_block_invoke_2
+ ___56-[VTFrameProcessor processWithCommandBuffer:parameters:]_block_invoke_3
+ ___56-[VTFrameProcessor processWithCommandBuffer:parameters:]_block_invoke_4
+ ___56-[VTFrameProcessor processWithCommandBuffer:parameters:]_block_invoke_5
+ ___60-[VTFrameProcessor processWithParameters:completionHandler:]_block_invoke
+ ___60-[VTFrameProcessor processWithParameters:completionHandler:]_block_invoke_2
+ ___60-[VTFrameProcessor processWithParameters:completionHandler:]_block_invoke_3
+ ___60-[VTFrameProcessor processWithParameters:completionHandler:]_block_invoke_4
+ ___60-[VTFrameProcessor processWithParameters:completionHandler:]_block_invoke_5
+ ___60-[VTFrameProcessor processWithParameters:completionHandler:]_block_invoke_6
+ ___61-[VTFrameProcessor processWithParameters:frameOutputHandler:]_block_invoke
+ ___63-[VTTemporalNoiseFilterImplementation processWithParams:error:]_block_invoke
+ ___72-[VTLowLatencyFrameInterpolationImplementation processWithParams:error:]_block_invoke
+ ___88-[VTSuperResolutionScalerConfiguration downloadConfigurationModelWithCompletionHandler:]_block_invoke
+ ___89-[VTLowLatencyFrameInterpolationImplementation processWithParameters:frameOutputHandler:]_block_invoke
+ ___CMPhotoLibraryCore_block_invoke
+ ___DecompressionMultiImageOutputCallback_block_invoke
+ ___DecompressionMultiImageOutputCallback_block_invoke_2
+ ___MuxedAlphaEncoder_EncodeFrame_block_invoke.39
+ ___MuxedAlphaEncoder_EncodeFrame_block_invoke.40
+ ___MuxedAlphaEncoder_EncodeFrame_block_invoke.40.cold.1
+ ___MuxedAlphaEncoder_EncodeFrame_block_invoke.40.cold.2
+ ___MuxedAlphaEncoder_EncodeFrame_block_invoke.40.cold.3
+ ___MuxedAlphaEncoder_EncodeFrame_block_invoke.40.cold.4
+ ___MuxedAlphaEncoder_EncodeFrame_block_invoke.40.cold.5
+ ___MuxedAlphaEncoder_EncodeFrame_block_invoke.40.cold.6
+ ___MuxedAlphaEncoder_EncodeMultiImageFrame_block_invoke.64
+ ___MuxedAlphaEncoder_EncodeMultiImageFrame_block_invoke.65
+ ___MuxedAlphaEncoder_EncodeMultiImageFrame_block_invoke.65.cold.1
+ ___MuxedAlphaEncoder_EncodeMultiImageFrame_block_invoke.65.cold.2
+ ___MuxedAlphaEncoder_EncodeMultiImageFrame_block_invoke.65.cold.3
+ ___MuxedAlphaEncoder_EncodeMultiImageFrame_block_invoke.65.cold.4
+ ___MuxedAlphaEncoder_EncodeMultiImageFrame_block_invoke.65.cold.5
+ ___NSDictionary0__struct
+ ___ParavirtualizedMotionEstimationProcessor_CreateInstance_block_invoke
+ ___ParavirtualizedMotionEstimationProcessor_CreateInstance_block_invoke.cold.1
+ ___ParavirtualizedMotionEstimationProcessor_CreateInstance_block_invoke.cold.2
+ ___TileDecompressionOutputCallback_block_invoke
+ ___TileDecompressionOutputCallback_block_invoke_2
+ ___VTCompressionSessionRemoteServer_CompleteTemporalFilterFrames_block_invoke
+ ___VTCompressionSessionRemoteServer_EncodeFrame_block_invoke.27
+ ___VTCompressionSessionRemoteServer_TemporalProcessFrame_block_invoke
+ ___VTDecompressionSessionAnalyzeAndInterruptFrame_block_invoke
+ ___VTDecompressionSessionRemote_DecodeTile_block_invoke.32
+ ___VTIsBackgroundRunningSupportedForClientPID_block_invoke
+ ___VTIsMVHEVCWithAlphaDecodingEnabledViaDefaults_block_invoke
+ ___VTParavirtualizationHostDecoderSessionCompleteInvalidate_block_invoke
+ ___VTParavirtualizationHostDecoderSessionDeliverMessageFromGuest_block_invoke
+ ___VTParavirtualizationHostDecoderSessionDeliverMessageFromGuest_block_invoke.cold.1
+ ___VTParavirtualizationHostDecoderSessionDeliverMessageFromGuest_block_invoke.cold.10
+ ___VTParavirtualizationHostDecoderSessionDeliverMessageFromGuest_block_invoke.cold.2
+ ___VTParavirtualizationHostDecoderSessionDeliverMessageFromGuest_block_invoke.cold.3
+ ___VTParavirtualizationHostDecoderSessionDeliverMessageFromGuest_block_invoke.cold.4
+ ___VTParavirtualizationHostDecoderSessionDeliverMessageFromGuest_block_invoke.cold.5
+ ___VTParavirtualizationHostDecoderSessionDeliverMessageFromGuest_block_invoke.cold.6
+ ___VTParavirtualizationHostDecoderSessionDeliverMessageFromGuest_block_invoke.cold.7
+ ___VTParavirtualizationHostDecoderSessionDeliverMessageFromGuest_block_invoke.cold.8
+ ___VTParavirtualizationHostDecoderSessionDeliverMessageFromGuest_block_invoke.cold.9
+ ___VTParavirtualizationHostDecoderSessionInvalidate_block_invoke
+ ___VTParavirtualizationHostEncoderSessionDeliverMessageFromGuest_block_invoke
+ ___VTParavirtualizationHostEncoderSessionDeliverMessageFromGuest_block_invoke.cold.1
+ ___VTParavirtualizationHostEncoderSessionDeliverMessageFromGuest_block_invoke.cold.10
+ ___VTParavirtualizationHostEncoderSessionDeliverMessageFromGuest_block_invoke.cold.11
+ ___VTParavirtualizationHostEncoderSessionDeliverMessageFromGuest_block_invoke.cold.12
+ ___VTParavirtualizationHostEncoderSessionDeliverMessageFromGuest_block_invoke.cold.13
+ ___VTParavirtualizationHostEncoderSessionDeliverMessageFromGuest_block_invoke.cold.14
+ ___VTParavirtualizationHostEncoderSessionDeliverMessageFromGuest_block_invoke.cold.15
+ ___VTParavirtualizationHostEncoderSessionDeliverMessageFromGuest_block_invoke.cold.16
+ ___VTParavirtualizationHostEncoderSessionDeliverMessageFromGuest_block_invoke.cold.17
+ ___VTParavirtualizationHostEncoderSessionDeliverMessageFromGuest_block_invoke.cold.2
+ ___VTParavirtualizationHostEncoderSessionDeliverMessageFromGuest_block_invoke.cold.3
+ ___VTParavirtualizationHostEncoderSessionDeliverMessageFromGuest_block_invoke.cold.4
+ ___VTParavirtualizationHostEncoderSessionDeliverMessageFromGuest_block_invoke.cold.5
+ ___VTParavirtualizationHostEncoderSessionDeliverMessageFromGuest_block_invoke.cold.6
+ ___VTParavirtualizationHostEncoderSessionDeliverMessageFromGuest_block_invoke.cold.7
+ ___VTParavirtualizationHostEncoderSessionDeliverMessageFromGuest_block_invoke.cold.8
+ ___VTParavirtualizationHostEncoderSessionDeliverMessageFromGuest_block_invoke.cold.9
+ ___VTParavirtualizationHostEncoderSessionInvalidate_block_invoke
+ ___VTParavirtualizationHostMotionEstimationProcessorSessionDeliverMessageFromGuest_block_invoke
+ ___VTParavirtualizationHostMotionEstimationProcessorSessionDeliverMessageFromGuest_block_invoke.cold.1
+ ___VTParavirtualizationHostMotionEstimationProcessorSessionDeliverMessageFromGuest_block_invoke.cold.2
+ ___VTParavirtualizationHostMotionEstimationProcessorSessionDeliverMessageFromGuest_block_invoke.cold.3
+ ___VTParavirtualizationHostMotionEstimationProcessorSessionDeliverMessageFromGuest_block_invoke.cold.4
+ ___VTParavirtualizationHostMotionEstimationProcessorSessionDeliverMessageFromGuest_block_invoke.cold.5
+ ___VTParavirtualizationHostMotionEstimationProcessorSessionInvalidate_block_invoke
+ ___VTParavirtualizationHostSessionCompleteInvalidate_block_invoke
+ ___VTParavirtualizationHostSessionCompleteInvalidate_block_invoke_2
+ ___VTParavirtualizationHostSessionCompleteInvalidate_block_invoke_3
+ ___VTParavirtualizationHostSessionInvalidate_block_invoke
+ ___VTParavirtualizationHostSessionInvalidate_block_invoke_2
+ ___VTPixelBlitterColorHandlingOptimized_setup_block_invoke.20
+ ___VTPixelBlitterColorHandlingOptimized_setup_block_invoke.23
+ ___VTPixelBlitterColorHandlingOptimized_setup_block_invoke.23.cold.1
+ ___VTPixelBlitterColorHandlingOptimized_setup_block_invoke.23.cold.2
+ ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke.417
+ ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke.419
+ ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke.419.cold.1
+ ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke.419.cold.2
+ ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke.419.cold.3
+ ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke.419.cold.4
+ ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke.419.cold.5
+ ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke.419.cold.6
+ ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke.419.cold.7
+ ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke.419.cold.8
+ ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke.419.cold.9
+ ___VTTemporalFilterRemote_CopyList_block_invoke
+ ___VTTemporalFilterSessionRemote_Create_block_invoke
+ ___block_descriptor_32_e44_v24?0"VEMotionBlurParameters"8"NSError"16l
+ ___block_descriptor_32_e66_i24?0^{OpaqueCMBlockBuffer=}8^{OpaqueFigCFWeakReferenceHolder=}16l
+ ___block_descriptor_40_e8_32b_e8_v16?0q8ls32l8
+ ___block_descriptor_40_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32o40b_e44_v24?0"VEMotionBlurParameters"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32o40o_e29_v24?0"<MTLSharedEvent>"8Q16ls32l8s40l8
+ ___block_descriptor_48_e8_32o40r_e27_v32?0q8"NSNumber"16B24i28lr40l8s32l8
+ ___block_descriptor_48_e8_32o_e53_v24?0"VTTemporalNoiseFilterParameters"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32o40o48b_e27_v32?0q8"NSNumber"16B24i28ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32o40o48b_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32o40o48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
+ ___block_descriptor_68_e8_32r_e124_B108?0{CGColorConversionIteratorData=Iqqqqqq^^{CGColorTRCData}^^{CGColorMatrixData}^^{CGColorNxMTransformData}}8q84q92^q100lr32l8
+ ___block_descriptor_76_e8_32r_e119_B100?0{CGColorConversionIteratorData=Iqqqqqq^^{CGColorTRCData}^^{CGColorMatrixData}^^{CGColorNxMTransformData}}8q84q92lr32l8
+ ___block_descriptor_93_e8_32o40o48b_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_tmp.101
+ ___block_descriptor_tmp.102
+ ___block_descriptor_tmp.103
+ ___block_descriptor_tmp.107
+ ___block_descriptor_tmp.109
+ ___block_descriptor_tmp.111
+ ___block_descriptor_tmp.112
+ ___block_descriptor_tmp.113
+ ___block_descriptor_tmp.116
+ ___block_descriptor_tmp.118
+ ___block_descriptor_tmp.119
+ ___block_descriptor_tmp.120
+ ___block_descriptor_tmp.121
+ ___block_descriptor_tmp.127
+ ___block_descriptor_tmp.142
+ ___block_descriptor_tmp.201
+ ___block_descriptor_tmp.238
+ ___block_descriptor_tmp.239
+ ___block_descriptor_tmp.26
+ ___block_descriptor_tmp.28
+ ___block_descriptor_tmp.29
+ ___block_descriptor_tmp.30
+ ___block_descriptor_tmp.35
+ ___block_descriptor_tmp.36
+ ___block_descriptor_tmp.40
+ ___block_descriptor_tmp.41
+ ___block_descriptor_tmp.42
+ ___block_descriptor_tmp.43
+ ___block_descriptor_tmp.44
+ ___block_descriptor_tmp.45
+ ___block_descriptor_tmp.46
+ ___block_descriptor_tmp.47
+ ___block_descriptor_tmp.49
+ ___block_descriptor_tmp.51
+ ___block_descriptor_tmp.52
+ ___block_descriptor_tmp.53
+ ___block_descriptor_tmp.55
+ ___block_descriptor_tmp.56
+ ___block_descriptor_tmp.57
+ ___block_descriptor_tmp.58
+ ___block_descriptor_tmp.60
+ ___block_descriptor_tmp.61
+ ___block_descriptor_tmp.62
+ ___block_descriptor_tmp.63
+ ___block_descriptor_tmp.64
+ ___block_descriptor_tmp.65
+ ___block_descriptor_tmp.68
+ ___block_descriptor_tmp.70
+ ___block_descriptor_tmp.75
+ ___block_descriptor_tmp.76
+ ___block_descriptor_tmp.77
+ ___block_descriptor_tmp.84
+ ___block_descriptor_tmp.99
+ ___block_literal_global.101
+ ___block_literal_global.105
+ ___block_literal_global.109
+ ___block_literal_global.111
+ ___block_literal_global.113
+ ___block_literal_global.115
+ ___block_literal_global.129
+ ___block_literal_global.13
+ ___block_literal_global.144
+ ___block_literal_global.15
+ ___block_literal_global.19
+ ___block_literal_global.203
+ ___block_literal_global.24
+ ___block_literal_global.241
+ ___block_literal_global.33
+ ___block_literal_global.37
+ ___block_literal_global.38
+ ___block_literal_global.4
+ ___block_literal_global.40
+ ___block_literal_global.42
+ ___block_literal_global.45
+ ___block_literal_global.51
+ ___block_literal_global.53
+ ___block_literal_global.57
+ ___block_literal_global.63
+ ___block_literal_global.70
+ ___block_literal_global.78
+ ___block_literal_global.79
+ ___block_literal_global.84
+ ___block_literal_global.86
+ ___dsrxpc_callback_handleEmitMultiImage_XPC_block_invoke
+ ___dsrxpc_callback_handleEmitTile_XPC_block_invoke
+ ___dsrxpc_waitForAsynchronousFrames_block_invoke
+ ___dsrxpc_waitForAsynchronousFrames_block_invoke_2
+ ___dssxpc_WaitForAsynchronousFrames_XPCMessage_block_invoke
+ ___getCMPhotoParavirtualizedHostJPEGHardwareCopyCapabilitiesSymbolLoc_block_invoke
+ ___getCMPhotoParavirtualizedHostJPEGHardwareDecodeSymbolLoc_block_invoke
+ ___getCMPhotoParavirtualizedHostJPEGHardwareEncodeSymbolLoc_block_invoke
+ ___getFigCPECryptorCreateCryptorFromSerializedRecipeSymbolLoc_block_invoke
+ ___isMCTFRunningOutOfProcess_block_invoke
+ ___loadVCPFrameworkOnce_block_invoke
+ ___loadVEFrameworkOnce_block_invoke
+ ___vtDecompressionSessionRemote_DecodeFrameCommon_block_invoke.53
+ ___vtGuestCopyDecoderCapabilities_block_invoke
+ ___vtLoadParavirtualizedMotionEstimationProcessors_block_invoke
+ ___vtLoadParavirtualizedMotionEstimationProcessors_block_invoke_2
+ ___vtParavirtualizationHostDecoderSession_getSpecialCaseHandlersForSettingProperties_block_invoke
+ ___vtParavirtualizationHostDecoderSession_isPropertyInDenyList_block_invoke
+ ___vtParavirtualizationHostEncoderSession_getSpecialCaseHandlersForSettingProperties_block_invoke
+ ___vtParavirtualizationHostEncoderSession_isPropertyInDenyList_block_invoke
+ ___vtTemporalFilterSessionShouldUseSeparateProcess_block_invoke
+ ___vtTemporalFilterShouldUseSeparateProcess_block_invoke
+ ___vtcss_appStateChangeListener_block_invoke.61
+ ___vtdsr_dequeueAllPendingFramesAndCallbackClientForEach_block_invoke.cold.4
+ __block_invoke.specialCasePropertyAndHandlerPairs
+ __loadedCapabilities
+ __maximumDimensions
+ __minimumDimensions
+ __processorSupported
+ _alphadecoder_mergeBaseAndAlpha.cold.4
+ _alphadecoder_mergeBaseAndAlpha.cold.5
+ _alphadecoder_transferPlane.cold.2
+ _alphadecoder_transferPlane.cold.3
+ _alphadecoder_transferPlane.cold.4
+ _alphaencoder_demuxBaseAndAlpha.cold.5
+ _alphaencoder_demuxBaseAndAlpha.cold.6
+ _alphaencoder_transferPlane.cold.2
+ _alphaencoder_transferPlane.cold.3
+ _alphaencoder_transferPlane.cold.4
+ _appendSrcTextureDescriptions_3PlaneSample
+ _audit_stringCMPhoto
+ _createAppleP3ColorSpace.cold.1
+ _createAppleP3ColorSpace.cold.2
+ _createAppleP3ColorSpace.cold.3
+ _createAppleP3ColorSpace.cold.4
+ _createAppleP3ColorSpace.cold.5
+ _createAppleP3ColorSpace.cold.6
+ _createAppleP3ColorSpace.cold.7
+ _dlopenHelper$DuetActivityScheduler
+ _dlopenHelperFlag$DuetActivityScheduler
+ _dovi_byteAtOffsetMatches
+ _dsrxpc_handleEmitMultiImage
+ _dsrxpc_waitForAsynchronousFrames.cold.1
+ _dsrxpc_waitForAsynchronousFrames.cold.2
+ _dssxpc_EmitCallbackReturnValue
+ _dssxpc_FlushPixelBufferPool
+ _dssxpc_SetMultiImageCallback
+ _dssxpc_WaitForAsynchronousFrames_XPCMessage
+ _dssxpc_ensureEventLinkIfSupported
+ _dssxpc_ensureEventLinkIfSupported.cold.1
+ _dssxpc_ensureEventLinkIfSupported.cold.2
+ _dssxpc_ensureEventLinkIfSupported.cold.3
+ _dssxpc_ensureEventLinkIfSupported.cold.4
+ _dssxpc_ensureEventLinkIfSupported.cold.5
+ _dssxpc_ensureEventLinkIfSupported.cold.6
+ _dssxpc_ensureEventLinkIfSupported.cold.7
+ _dssxpc_ensureEventLinkIfSupported.cold.8
+ _dssxpc_ensureEventLinkIfSupported.onceToken
+ _dssxpc_ensureEventLinkIfSupported.prefersEventLink
+ _dssxpc_ensureEventLinkIfSupported.prefersEventLinkForApp
+ _dssxpc_maxNumberOfEmitFrameEventLinksToCreatePerSession.onceToken
+ _figNoteRect
+ _fig_log_get_emitter
+ _filterOutputCallback
+ _gAppleJPEGVideoDecoderTrace
+ _gCompressionSessionRemoteTrace
+ _gCompressionSessionServerTrace
+ _gDecompressionSessionRemoteTrace
+ _gDecompressionSessionServerTrace
+ _gDecompressionSessionXPCServerTrace
+ _gFigDepthWrapperDecoder
+ _gFigDepthWrapperEncoder
+ _gFigDolbyVisionDecoder
+ _gFigIOSurfaceSupportTrace
+ _gFigMuxedAlphaDecoder
+ _gFigMuxedAlphaEncoder
+ _gFigVTCSTrace
+ _gFigVTDSTrace
+ _gFigVTRestrictionsTrace
+ _gFigVTTileCSTrace
+ _gFigVTTileDSTrace
+ _gFigVTTransferTrace
+ _gParavirtualizedHostJPEGSupport
+ _gParavirtualizedJPEGSession
+ _gParavirtualizedMotionEstimationProcessor
+ _gSRSEnhancementFilterTrace
+ _gTestIPBVideoDecoderTrace
+ _gTestIPBVideoEncoder
+ _gVTCGUtilitiesTrace
+ _gVTDeghostingSessionTrace
+ _gVTFigAudioSessionTrace
+ _gVTFrameSilo
+ _gVTHDRImageStatisticsGenerationSessionTrace
+ _gVTHDRMetadataGenerationSession
+ _gVTHDRPerFrameMetadataGenerationSession
+ _gVTIORegistryKeyServiceTrace
+ _gVTMotionEstimationSessionTrace
+ _gVTMultiPassStorage
+ _gVTPixelBufferAttributesMediator
+ _gVTPixelBufferConformer
+ _gVTPixelRotationSessionTrace
+ _gVTPixelTransferSessionBlitterTrace
+ _gVTPixelTransferSessionGraphTrace
+ _gVTPoolsTrace
+ _gVTPreprocessingSession
+ _gVTRBSTrace
+ _gVTRateControlSession
+ _gVTTemporalFilterSelectionTrace
+ _gVTTemporalFilterSession
+ _gVTTemporalNoiseFilterImplementationTrace
+ _gVTVideoDecoderCapabilitiesTrace
+ _gVTVideoDecoderLoaderTrace
+ _gVTVideoDecoderSelectionTrace
+ _gVTVideoEncoderLoaderTrace
+ _gVTVideoEncoderSelectionTrace
+ _gVideoCodecServiceTrace
+ _getCMPhotoParavirtualizedHostJPEGHardwareCopyCapabilitiesSymbolLoc
+ _getCMPhotoParavirtualizedHostJPEGHardwareCopyCapabilitiesSymbolLoc.ptr
+ _getCMPhotoParavirtualizedHostJPEGHardwareDecodeSymbolLoc
+ _getCMPhotoParavirtualizedHostJPEGHardwareDecodeSymbolLoc.ptr
+ _getCMPhotoParavirtualizedHostJPEGHardwareEncodeSymbolLoc
+ _getCMPhotoParavirtualizedHostJPEGHardwareEncodeSymbolLoc.ptr
+ _getFigCPECryptorCreateCryptorFromSerializedRecipeSymbolLoc.ptr
+ _getValuesFromDictionary.cold.11
+ _globalVTMTLProperties.0
+ _gotLoadHelper_x8$__DASContinuedProcessingTaskAssertionTag
+ _hypotf
+ _isMCTFRunningOutOfProcess.onceToken
+ _isMCTFRunningOutOfProcess.runningOutOfProcess
+ _kCFAllocatorNull
+ _kCMFormatDescriptionExtensionAtom_ReencryptedSkipPattern
+ _kCMObjectLibraryClassID_VideoDeghostingProcessor
+ _kCVPixelBufferIOSurfacePurgeableKey
+ _kCVPixelBufferProResRAWKey_MetadataExtension
+ _kFigFormatDescriptionExtension_CameraCalibrationDataLensCollection
+ _kFigPowerLogSupportEventKey_ClientProcessID
+ _kFigPowerLogSupportEventKey_LogID
+ _kFigPowerLogSupportEventKey_VTSession_IsHDR
+ _kFigPowerLogSupportEventKey_VTSession_IsHardware
+ _kFigPowerLogSupportEventKey_VTSession_NumFramesDecoded
+ _kFigPowerLogSupportEventKey_VTSession_NumFramesDropped
+ _kFigPowerLogSupportEventKey_VTSession_NumFramesEncoded
+ _kFigPowerLogSupportEventKey_VTSession_ResHeight
+ _kFigPowerLogSupportEventKey_VTSession_ResWidth
+ _kFigPowerLogSupportEventKey_VTSession_SessionDuration
+ _kFigPowerLogSupportEventKey_VTSession_VideoCodecType
+ _kParavirtualizedMotionEstimationProcessorVTable
+ _kParavirtualizedMotionEstimationProcessor_BaseClass
+ _kParavirtualizedMotionEstimationProcessor_MotionEstimationProcessorClass
+ _kVTCameraCalibrationExtrinsicOriginSource_StereoCameraSystemBaseline
+ _kVTCameraCalibrationLensAlgorithmKind_ParametricLens
+ _kVTCameraCalibrationLensDomain_Color
+ _kVTCameraCalibrationLensRole_Left
+ _kVTCameraCalibrationLensRole_Mono
+ _kVTCameraCalibrationLensRole_Right
+ _kVTCompressionPictureInPictureRegion_BorderBottom
+ _kVTCompressionPictureInPictureRegion_BorderLeft
+ _kVTCompressionPictureInPictureRegion_BorderRight
+ _kVTCompressionPictureInPictureRegion_BorderTop
+ _kVTCompressionPictureInPictureRegion_Rectangle
+ _kVTCompressionPreset_Balanced
+ _kVTCompressionPreset_HighQuality
+ _kVTCompressionPreset_HighSpeed
+ _kVTCompressionPreset_VideoConferencing
+ _kVTCompressionPropertyCameraCalibrationKey_ExtrinsicOrientationQuaternion
+ _kVTCompressionPropertyCameraCalibrationKey_ExtrinsicOriginSource
+ _kVTCompressionPropertyCameraCalibrationKey_IntrinsicMatrix
+ _kVTCompressionPropertyCameraCalibrationKey_IntrinsicMatrixExtensionsProjectionOffset
+ _kVTCompressionPropertyCameraCalibrationKey_IntrinsicMatrixExtensionsRadialDistortionK1
+ _kVTCompressionPropertyCameraCalibrationKey_IntrinsicMatrixExtensionsRadialDistortionK2
+ _kVTCompressionPropertyCameraCalibrationKey_IntrinsicMatrixExtensionsSkew
+ _kVTCompressionPropertyCameraCalibrationKey_IntrinsicMatrixExtensionsTangentialDistortionP1
+ _kVTCompressionPropertyCameraCalibrationKey_IntrinsicMatrixExtensionsTangentialDistortionP2
+ _kVTCompressionPropertyCameraCalibrationKey_IntrinsicMatrixProjectionOffset
+ _kVTCompressionPropertyCameraCalibrationKey_IntrinsicMatrixReferenceDimensions
+ _kVTCompressionPropertyCameraCalibrationKey_LensAlgorithmKind
+ _kVTCompressionPropertyCameraCalibrationKey_LensDistortions
+ _kVTCompressionPropertyCameraCalibrationKey_LensDomain
+ _kVTCompressionPropertyCameraCalibrationKey_LensFrameAdjustmentsPolynomialX
+ _kVTCompressionPropertyCameraCalibrationKey_LensFrameAdjustmentsPolynomialY
+ _kVTCompressionPropertyCameraCalibrationKey_LensIdentifier
+ _kVTCompressionPropertyCameraCalibrationKey_LensRole
+ _kVTCompressionPropertyCameraCalibrationKey_RadialAngleLimit
+ _kVTCompressionPropertyKey_CameraCalibrationDataLensCollection
+ _kVTCompressionPropertyKey_ConstantQualityFactor
+ _kVTCompressionPropertyKey_CurrentHDRMetadataGenerationState
+ _kVTCompressionPropertyKey_EnableUserQPMap
+ _kVTCompressionPropertyKey_EncoderEncryptionKeyID
+ _kVTCompressionPropertyKey_InitialHDRMetadataGenerationState
+ _kVTCompressionPropertyKey_LowMemory
+ _kVTCompressionPropertyKey_PictureInPictureRegion
+ _kVTCompressionPropertyKey_SupportedPresetDictionaries
+ _kVTCompressionPropertyKey_VBVBufferDuration
+ _kVTCompressionPropertyKey_VBVInitialDelayPercentage
+ _kVTCompressionPropertyKey_VBVMaxBitRate
+ _kVTCompressionPropertyKey_VariableBitRate
+ _kVTDeghostingBoundingBoxRepairOptionKey_EnableBlurFilter
+ _kVTDeghostingBoundingBoxRepairOptionKey_SpatialFilterWeight
+ _kVTDeghostingBoundingBoxRepairOptionKey_SpatioTemporalFilterWeight
+ _kVTDeghostingBoundingBoxRepairOptionKey_StrongSpatialFilterWeight
+ _kVTDeghostingBoundingBoxStatisticsKey_MaximumGradient
+ _kVTDeghostingBoundingBoxStatisticsKey_MaximumTemporalDifference
+ _kVTDeghostingFrameKey_BorderPixels
+ _kVTDeghostingFrameKey_BoundingBoxes
+ _kVTDeghostingFrameKey_Homography
+ _kVTDeghostingFrameKey_PixelBuffer
+ _kVTDeghostingFrameKey_RepairWeights
+ _kVTDeghostingPropertyKey_BorderPixelBufferAttributes
+ _kVTDeghostingPropertyKey_Priority
+ _kVTDeghostingPropertyKey_RealTime
+ _kVTDeghostingSessionCreationOption_MaximumReferenceFrameDistance
+ _kVTHDRMetadataGenerationSessionOptions_HDR10PlusKey
+ _kVTHDRMetadataGenerationSessionOptions_InitialSessionState
+ _kVTHDRMetadataGenerationSessionOptions_PreserveSDRRangeKey
+ _kVTHDRMetadataInsertionMode_RequestSDRRangePreservation
+ _kVTHeroEye_Left
+ _kVTHeroEye_Right
+ _kVTHostInfo_BuildVersion
+ _kVTMotionEstimationProcessor_IsParavirtualizationAware
+ _kVTMotionEstimationProcessor_IsParavirtualized
+ _kVTMotionEstimationSessionCreationOption_AllowClientProcessEstimate
+ _kVTMotionEstimationSessionCreationOption_HostProcessorID
+ _kVTMotionEstimationSessionCreationOption_IncludeMotionConfidence
+ _kVTMotionEstimationSessionCreationOption_UseMultiPassSearch
+ _kVTPixelTransferPropertyKey_AllowOnePassMetalScaling
+ _kVTPixelTransferPropertyKey_MetalCompletionQueue
+ _kVTPixelTransferPropertyKey_MetalSubmissionQueue
+ _kVTProjectionKind_Equirectangular
+ _kVTProjectionKind_HalfEquirectangular
+ _kVTProjectionKind_ParametricImmersive
+ _kVTProjectionKind_Rectilinear
+ _kVTTemporalFilter_FactoryFunctionHasSpecificationArgument
+ _kVTTemporalFilter_HostTemporalFilterID
+ _kVTVideoEncoderMultipassStorage_ParavirtualizationHostEncoderSession
+ _kVTVideoEncoderSpecification_EnableAppleOnlySWAV1
+ _kVTViewPackingKind_OverUnder
+ _kVTViewPackingKind_SideBySide
+ _kVTWarpKind_ApplicationDefined
+ _loadVCPFrameworkOnce
+ _loadVCPFrameworkOnce.cold.1
+ _loadVCPFrameworkOnce.vcpFrameworkLoaded
+ _loadVCPFrameworkOnce.vcpLibraryLoaderOnce
+ _loadVEFrameworkOnce
+ _loadVEFrameworkOnce.cold.1
+ _loadVEFrameworkOnce.frameworkLoaded
+ _loadVEFrameworkOnce.veLibraryLoaderOnce
+ _log2
+ _objc_enumerationMutation
+ _objc_msgSend$_checkForDiscontinuity:
+ _objc_msgSend$_clearStaledPendingFramesFromQueue
+ _objc_msgSend$_completeFrame:
+ _objc_msgSend$_completeFrames
+ _objc_msgSend$_createPendingFrame:inputFrame:
+ _objc_msgSend$_findFrameInQueue:
+ _objc_msgSend$_freePendingFrame:
+ _objc_msgSend$_loadCapabilities
+ _objc_msgSend$_processFrame:outputFrame:useClientProvidedOutputFrame:
+ _objc_msgSend$_processReferenceFrameIfNotProcessed:
+ _objc_msgSend$_processSourceFrameIfNotProcessed:completionHandler:
+ _objc_msgSend$_setFilterStrength:
+ _objc_msgSend$_validateParameters:error:
+ _objc_msgSend$addObject:
+ _objc_msgSend$buffer
+ _objc_msgSend$code
+ _objc_msgSend$compare:
+ _objc_msgSend$copy
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$createSharedEventListener
+ _objc_msgSend$currentState
+ _objc_msgSend$dealloc
+ _objc_msgSend$defaultRevision
+ _objc_msgSend$destinationFrame
+ _objc_msgSend$destinationFrames
+ _objc_msgSend$destinationPixelBufferAttributes
+ _objc_msgSend$destroySharedEventListener
+ _objc_msgSend$dictionaryWithObject:forKey:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$discontinuity
+ _objc_msgSend$dispatchThreads:threadsPerThreadgroup:
+ _objc_msgSend$domain
+ _objc_msgSend$downloadAssetWithCompletionHandler:
+ _objc_msgSend$encodeSignalEvent:value:
+ _objc_msgSend$encodeWaitForEvent:value:
+ _objc_msgSend$endSession
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$filterStrength
+ _objc_msgSend$finishProcessing
+ _objc_msgSend$flags
+ _objc_msgSend$floatValue
+ _objc_msgSend$flowBufferHeight
+ _objc_msgSend$flowBufferPixelFormat
+ _objc_msgSend$flowBufferWidth
+ _objc_msgSend$frameHeight
+ _objc_msgSend$framePreferredPixelFormats
+ _objc_msgSend$frameWidth
+ _objc_msgSend$getAssetStatusWithPercentCompleted:
+ _objc_msgSend$handleEmittedFrame:presentationTimestamp:status:infoFlags:
+ _objc_msgSend$handleForIdentifier:error:
+ _objc_msgSend$identifierWithPid:
+ _objc_msgSend$initWithBuffer:presentationTimeStamp:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithConfiguration:error:
+ _objc_msgSend$initWithDispatchQueue:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithForwardFlow:backwardFlow:
+ _objc_msgSend$initWithFrameWidth:frameHeight:qualityPrioritization:revision:
+ _objc_msgSend$initWithFrameWidth:frameHeight:scaleFactor:inputType:usePrecomputedFlow:qualityPrioritization:revision:
+ _objc_msgSend$initWithFrameWidth:frameHeight:usePrecomputedFlow:qualityPrioritization:revision:
+ _objc_msgSend$initWithFrameWidth:sourceframeHeight:
+ _objc_msgSend$initWithSourceFrame:nextFrame:opticalFlow:interpolationPhase:submissionMode:destinationFrames:
+ _objc_msgSend$initWithSourceFrame:nextFrame:previousFrame:nextOpticalFlow:previousOpticalFlow:motionBlurStrength:submissionMode:destinationFrame:
+ _objc_msgSend$initWithSourceFrame:nextFrame:submissionMode:opticalFlow:
+ _objc_msgSend$initWithSourceFrame:previousFrame:previousOutputFrame:opticalFlow:destinationFrame:
+ _objc_msgSend$initWithWidth:height:pixelFormat:spatialScaleFactor:
+ _objc_msgSend$internalEndSession
+ _objc_msgSend$interpolationPhase
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$lastObject
+ _objc_msgSend$loadProperties
+ _objc_msgSend$maximumDimensions
+ _objc_msgSend$maximumSupportedHeight
+ _objc_msgSend$maximumSupportedWidth
+ _objc_msgSend$minimumDimensions
+ _objc_msgSend$minimumSupportedHeight
+ _objc_msgSend$minimumSupportedWidth
+ _objc_msgSend$newSharedEvent
+ _objc_msgSend$nextFrameCount
+ _objc_msgSend$nextFrames
+ _objc_msgSend$notifyListener:atValue:block:
+ _objc_msgSend$numberWithFloat:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$parameterDispatchGroup
+ _objc_msgSend$presentationTimeStamp
+ _objc_msgSend$previousFrame
+ _objc_msgSend$previousFrameCount
+ _objc_msgSend$previousFrames
+ _objc_msgSend$processWithCommandBuffer:parameters:completionHandler:
+ _objc_msgSend$processWithParameters:completionHandler:
+ _objc_msgSend$processWithParameters:error:
+ _objc_msgSend$processWithParameters:frameOutputHandler:
+ _objc_msgSend$processWithParams:completionHandler:error:
+ _objc_msgSend$processWithParams:error:
+ _objc_msgSend$processWithPreviousFrame:currentFrame:interpolationPhases:outputBuffers:error:frameCompletionHandler:
+ _objc_msgSend$processWithSourceFrame:destinationframe:error:
+ _objc_msgSend$removeObject:
+ _objc_msgSend$setCompletionQueue:
+ _objc_msgSend$setMaxTemporalExponentialFactor:
+ _objc_msgSend$setScaleFactor:
+ _objc_msgSend$setSignaledValue:
+ _objc_msgSend$setSubmissionQueue:
+ _objc_msgSend$setThreadgroupMemoryLength:atIndex:
+ _objc_msgSend$sourceFrame
+ _objc_msgSend$sourcePixelBufferAttributes
+ _objc_msgSend$startSessionWithConfiguration:error:
+ _objc_msgSend$startSessionWithConfigurationMode:error:
+ _objc_msgSend$supportedPixelFormats
+ _objc_msgSend$supportedRevisions
+ _objc_msgSend$supportedScaleFactors
+ _objc_msgSend$supportsFamily:
+ _objc_msgSend$tags
+ _objc_msgSend$userInfo
+ _objc_msgSend$vcpConfiguration
+ _objc_msgSend$veConfiguration
+ _objc_msgSend$veFrame
+ _objc_msgSend$veFrameOpticalFlow
+ _objc_msgSend$veParameters
+ _objc_msgSend$waitUntilSignaledValue:timeoutMS:
+ _objc_msgSendSuper2
+ _objc_opt_isKindOfClass
+ _objc_release_x21
+ _objc_release_x23
+ _objc_release_x26
+ _objc_release_x27
+ _objc_retain_x19
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x8
+ _paravirtualizedMotionEstimationProcessor_rememberPixelBufferAndUUID
+ _paravirtualizedVideoDecoder_HandleMessageFromHost
+ _paravirtualizedVideoDecoder_HandleMessageFromHost.cold.1
+ _paravirtualizedVideoDecoder_HandleMessageFromHost.cold.2
+ _paravirtualizedVideoDecoder_HandleMessageFromHost.cold.3
+ _paravirtualizedVideoDecoder_HandleMessageFromHost.cold.4
+ _paravirtualizedVideoDecoder_HandleMessageFromHost.cold.5
+ _paravirtualizedVideoDecoder_HandleMessageFromHost.cold.6
+ _paravirtualizedVideoDecoder_dictionarySetValue
+ _paravirtualizedVideoEncoder_HandleMessageFromHost
+ _paravirtualizedVideoEncoder_HandleMessageFromHost.cold.1
+ _paravirtualizedVideoEncoder_HandleMessageFromHost.cold.10
+ _paravirtualizedVideoEncoder_HandleMessageFromHost.cold.2
+ _paravirtualizedVideoEncoder_HandleMessageFromHost.cold.3
+ _paravirtualizedVideoEncoder_HandleMessageFromHost.cold.4
+ _paravirtualizedVideoEncoder_HandleMessageFromHost.cold.5
+ _paravirtualizedVideoEncoder_HandleMessageFromHost.cold.6
+ _paravirtualizedVideoEncoder_HandleMessageFromHost.cold.7
+ _paravirtualizedVideoEncoder_HandleMessageFromHost.cold.8
+ _paravirtualizedVideoEncoder_HandleMessageFromHost.cold.9
+ _parseProResRAWMetadataExtension
+ _sInitializeTemporalFiltersRegistryOnce
+ _sSymbolsAvailable
+ _sTemporalFilterRegistryMutex
+ _sVCPBundleHandle
+ _sVCPGetVersionFunc
+ _sVCPRateControlCopySupportedPropertiesFunc
+ _sVCPRateControlSessionBeforeEmitEncodedFrameFunc
+ _sVCPRateControlSessionBeforeEncodeFrameFunc
+ _sVCPRateControlSessionBeforePrepareToEncodeFramesFunc
+ _sVCPRateControlSessionCompleteFramesFunc
+ _sVCPRateControlSessionCopyPropertyFunc
+ _sVCPRateControlSessionCreateFunc
+ _sVCPRateControlSessionSetPropertyFunc
+ _sVCPReactionObserverCreateFunc
+ _sVTDeghostingFrameBufferClass
+ _sVTDeghostingFrameBufferID
+ _sVTDeghostingProcessorClassDesc
+ _sVTDeghostingProcessorClassID
+ _sVTDeghostingSessionClass
+ _sVTDeghostingSessionPropertyCallbacks
+ _sVTDeghostingSessionSupportedPropertyDictionary
+ _sVTMTSRenderPassBarrierID
+ _sVTMTSRenderPassDescriptorID
+ _sVTUseVeryShortTimeouts
+ _scalerCapabilities.flagBayerRepacking
+ _setLevel4Info
+ _strncmp
+ _temporalFilterSessionOutputCallback
+ _temporalFilterSessionOutputCallback.cold.1
+ _translateNSErrorToVTFrameProcessorError
+ _validRotation
+ _validateDeviceProperties
+ _vtAddProfileToDict.cold.1
+ _vtAddProfileToDict.cold.2
+ _vtAddProfileToDict.cold.3
+ _vtAddProfileToDict.cold.4
+ _vtBuildPixelBufferPoolsCommon.cold.10
+ _vtBuildPixelBufferPoolsCommon.cold.7
+ _vtBuildPixelBufferPoolsCommon.cold.8
+ _vtBuildPixelBufferPoolsCommon.cold.9
+ _vtClonePendingFrameSurfaceStuff
+ _vtClonePendingTileSurfaceStuff
+ _vtClonePixelBufferSurfaceStuff
+ _vtCodecTypeStringIsEligibleForParavirtualization
+ _vtCompressionSessionAddDolbyVisionVideoFormatDescriptionExtensions.cold.2
+ _vtCompressionSessionCompressionWork.cold.9
+ _vtCompressionSessionIsHEVC10BitCompatible
+ _vtCompressionSessionOutputFrame
+ _vtCompressionSessionSetHDRFormatAndInitializeMetadataGeneration
+ _vtCompressionSessionSetHDRFormatAndInitializeMetadataGeneration.cold.1
+ _vtCompressionSessionStoreHDRDefaultWrites.hdr10PlusExtractionEnabled
+ _vtCompressionSessionStoreHDRDefaultWrites.sdrPreservationEnabled
+ _vtCompressionSessionValidateCameraCalibrationDataLensCollection
+ _vtCompressionSessionValidateInitialHDRMetadataState
+ _vtCompressionSessionValidateInputQueueMaxCount
+ _vtCopyCodecProfilesArrayAndDictionaryForEmbedded
+ _vtCopyCodecProfilesArrayAndDictionaryForEmbedded.cold.1
+ _vtCopyCodecProfilesArrayAndDictionaryForEmbedded.cold.2
+ _vtCopyCodecProfilesArrayAndDictionaryForEmbedded.cold.3
+ _vtCreateDecoderCapabilitiesDictionary
+ _vtCreateDecoderCapabilitiesDictionary.cold.1
+ _vtCreateDecoderCapabilitiesDictionary.cold.10
+ _vtCreateDecoderCapabilitiesDictionary.cold.11
+ _vtCreateDecoderCapabilitiesDictionary.cold.12
+ _vtCreateDecoderCapabilitiesDictionary.cold.13
+ _vtCreateDecoderCapabilitiesDictionary.cold.14
+ _vtCreateDecoderCapabilitiesDictionary.cold.15
+ _vtCreateDecoderCapabilitiesDictionary.cold.2
+ _vtCreateDecoderCapabilitiesDictionary.cold.3
+ _vtCreateDecoderCapabilitiesDictionary.cold.4
+ _vtCreateDecoderCapabilitiesDictionary.cold.5
+ _vtCreateDecoderCapabilitiesDictionary.cold.6
+ _vtCreateDecoderCapabilitiesDictionary.cold.7
+ _vtCreateDecoderCapabilitiesDictionary.cold.8
+ _vtCreateDecoderCapabilitiesDictionary.cold.9
+ _vtCreateDeghostingProcessorRegistry
+ _vtCreateH264OrHEVCDecoderCapabilitiesDictionaryInternal
+ _vtCreateProfileSupportEntryDictionaryForVP9Embedded
+ _vtDeghostingFrameBufferCopyDebugDesc
+ _vtDeghostingFrameBufferFinalize
+ _vtDeghostingFrameBufferInit
+ _vtDeghostingSessionCopyDebugDesc
+ _vtDeghostingSessionCreate
+ _vtDeghostingSessionCreateSupportedPropertyDictionary
+ _vtDeghostingSessionEmitCommon
+ _vtDeghostingSessionFinalize
+ _vtDeghostingSessionFrameEnter
+ _vtDeghostingSessionInit
+ _vtDeghostingSessionProcessCommon
+ _vtDeghostingSessionProcessCommon.cold.1
+ _vtDeghostingSessionProcessCommon.cold.2
+ _vtDeghostingSessionProcessCommon2
+ _vtDeghostingSessionProcessCommon2.cold.1
+ _vtDeghostingSessionProcessCommon2.cold.2
+ _vtDeghostingSessionSetOneProperty
+ _vtDictionarySetValue
+ _vtFilterRegistryItemForHardwareAcceleratedDecodersOnly
+ _vtFilterRegistryItemForHardwareAcceleratedEncodersOnly
+ _vtFilterRegistryItemForHardwareAcceleratedMotionEstimationProcessorsOnly
+ _vtFilterRegistryItemForParavirtualizedMotionEstimationProcessorsOnly
+ _vtFreePendingFrameSurfaceStuff
+ _vtFreePendingTileSurfaceStuff
+ _vtFreePixelBufferSurfaceStuff
+ _vtInitializeMotionEstimationProcessorRegistry
+ _vtInitializeTemporalFilterRegistry
+ _vtIsHardwareCodecAvailable
+ _vtMetalTransferSessionTransferImageCommonSync.cold.10
+ _vtMetalTransferSessionTransferImageCommonSync.cold.11
+ _vtMetalTransferSessionTransferImageCommonSync.cold.12
+ _vtMetalTransferSessionTransferImageCommonSync.cold.13
+ _vtMetalTransferSessionTransferImageCommonSync.cold.14
+ _vtMetalTransferSessionTransferImageCommonSync.cold.15
+ _vtMetalTransferSessionTransferImageCommonSync.cold.16
+ _vtMetalTransferSessionTransferImageCommonSync.cold.17
+ _vtMetalTransferSessionTransferImageCommonSync.cold.18
+ _vtMetalTransferSessionTransferImageCommonSync.cold.9
+ _vtMotionEstimationSessionGetProcessorCreateInstanceFunction
+ _vtParavirtualizationAppendDecoderDescription
+ _vtParavirtualizationHostDecoderSession_CopyDebugDesc
+ _vtParavirtualizationHostDecoderSession_Finalize
+ _vtParavirtualizationHostDecoderSession_Init
+ _vtParavirtualizationHostDecoderSession_RegisterType
+ _vtParavirtualizationHostDecoderSession_RegisterType.sVTParavirtualizationHostDecoderSessionClass
+ _vtParavirtualizationHostDecoderSession_callMessageToGuestHandler
+ _vtParavirtualizationHostDecoderSession_getSpecialCaseHandlersForSettingProperties.sCreateDictionaryOnce
+ _vtParavirtualizationHostDecoderSession_getSpecialCaseHandlersForSettingProperties.sSpecialCaseHandlersForSettingProperties
+ _vtParavirtualizationHostDecoderSession_handleAnySpecialCaseSetPropertyAndCopyReplacementValue
+ _vtParavirtualizationHostDecoderSession_handleAnySpecialCaseSetPropertyAndCopyReplacementValue.cold.1
+ _vtParavirtualizationHostDecoderSession_isPropertyInDenyList
+ _vtParavirtualizationHostDecoderSession_isPropertyInDenyList.cold.1
+ _vtParavirtualizationHostDecoderSession_isPropertyInDenyList.denyList
+ _vtParavirtualizationHostDecoderSession_isPropertyInDenyList.onceToken
+ _vtParavirtualizationHostDecoderSession_lookupAndRetainUUIDForPendingPixelBuffer
+ _vtParavirtualizationHostDecoderSession_sendMessageToGuest
+ _vtParavirtualizationHostDecoderSession_sendMessageToGuestAndCopyReplySync
+ _vtParavirtualizationHostEncoderSessionCleanUpAfterEncode
+ _vtParavirtualizationHostEncoderSession_CopyDebugDesc
+ _vtParavirtualizationHostEncoderSession_Finalize
+ _vtParavirtualizationHostEncoderSession_Init
+ _vtParavirtualizationHostEncoderSession_RegisterType
+ _vtParavirtualizationHostEncoderSession_RegisterType.sVTParavirtualizationHostEncoderSessionClass
+ _vtParavirtualizationHostEncoderSession_callMessageToGuestHandler
+ _vtParavirtualizationHostEncoderSession_getSpecialCaseHandlersForSettingProperties.sCreateDictionaryOnce
+ _vtParavirtualizationHostEncoderSession_getSpecialCaseHandlersForSettingProperties.sSpecialCaseHandlersForSettingProperties
+ _vtParavirtualizationHostEncoderSession_handleAnySpecialCaseSetPropertyAndCopyReplacementValue
+ _vtParavirtualizationHostEncoderSession_handleAnySpecialCaseSetPropertyAndCopyReplacementValue.cold.1
+ _vtParavirtualizationHostEncoderSession_handleMultiPassStorageSetPropertyAndCopyReplacementValue
+ _vtParavirtualizationHostEncoderSession_isPropertyInDenyList
+ _vtParavirtualizationHostEncoderSession_isPropertyInDenyList.cold.1
+ _vtParavirtualizationHostEncoderSession_isPropertyInDenyList.denyList
+ _vtParavirtualizationHostEncoderSession_isPropertyInDenyList.onceToken
+ _vtParavirtualizationHostEncoderSession_lookupRetainAndForgetPendingFramePixelBuffersAndUUIDsAndMappingIDs
+ _vtParavirtualizationHostEncoderSession_lookupRetainAndForgetPendingTilePixelBuffersAndUUIDsAndMappingIDs
+ _vtParavirtualizationHostEncoderSession_sendMessageToGuest
+ _vtParavirtualizationHostEncoderSession_sendMessageToGuestAndCopyReplySync
+ _vtParavirtualizationHostMotionEstimationProcessorSession_CopyDebugDesc
+ _vtParavirtualizationHostMotionEstimationProcessorSession_Finalize
+ _vtParavirtualizationHostMotionEstimationProcessorSession_Init
+ _vtParavirtualizationHostMotionEstimationProcessorSession_RegisterType
+ _vtParavirtualizationHostMotionEstimationProcessorSession_RegisterType.sVTParavirtualizationMotionEstimationProcessorSessionClass
+ _vtParavirtualizationHostMotionEstimationProcessorSession_callMessageToGuestHandler
+ _vtParavirtualizationHostMotionEstimationProcessorSession_rememberPixelBufferAndUUIDAndMappingID
+ _vtParavirtualizationHostMotionEstimationProcessorSession_rememberPixelBufferAndUUIDAndMappingID.cold.1
+ _vtParavirtualizationHostMotionEstimationProcessorSession_sendMessageToGuest
+ _vtParavirtualizationHostMotionEstimationProcessorSession_sendMessageToGuestAndCopyReplySync
+ _vtParavirtualizationHostSession_CopyDebugDesc
+ _vtParavirtualizationHostSession_Finalize
+ _vtParavirtualizationHostSession_Init
+ _vtParavirtualizationHostSession_RegisterType
+ _vtParavirtualizationHostSession_RegisterType.sVTParavirtualizationHostSessionClass
+ _vtParavirtualizationHostSession_callMessageToGuestHandler
+ _vtParavirtualizationInvalidateHostDecoderSessionAndRemoveItFromHostSession
+ _vtParavirtualizationInvalidateHostEncoderSessionAndRemoveItFromHostSession
+ _vtParavirtualizationIsPixelFormatCompressed
+ _vtPopulateMotionEstimationRegistry
+ _vtPopulateTemporalFilterRegistry
+ _vtPreprocessingSessionEnsureResolutionIsPartOfSession.cold.2
+ _vtPreprocessingSessionEnsureResolutionIsPartOfSession.cold.3
+ _vtRateControlSessionRegisterBundle.cold.1
+ _vtRateControlSessionRegisterBundle.cold.10
+ _vtRateControlSessionRegisterBundle.cold.2
+ _vtRateControlSessionRegisterBundle.cold.3
+ _vtRateControlSessionRegisterBundle.cold.4
+ _vtRateControlSessionRegisterBundle.cold.5
+ _vtRateControlSessionRegisterBundle.cold.6
+ _vtRateControlSessionRegisterBundle.cold.7
+ _vtRateControlSessionRegisterBundle.cold.8
+ _vtRateControlSessionRegisterBundle.cold.9
+ _vtTemporalFilterSessionProcessFrameCommon
+ _vtTemporalFilterSessionProcessFrameCommon.cold.1
+ _vtTemporalFilterSessionProcessFrameCommon.cold.2
+ _vtTemporalFilterSessionProcessFrameCommon.cold.3
+ _vtTemporalFilterSessionProcessFrameCommon.cold.4
+ _vtTemporalFilterSessionProcessFrameCommon.cold.5
+ _vtTemporalFilterSessionShouldUseSeparateProcess.featureEnabled
+ _vtTemporalFilterSessionShouldUseSeparateProcess.onceToken
+ _vtTemporalFilterShouldUseSeparateProcess.featureEnabled
+ _vtTileCompressionSessionTrackTileLeavingEncoder
+ _vtUnregisterParavirtualizedMotionEstimationProcessors
+ _vt_Copy_a2vy_Crop
+ _vt_Rotate_Celeste.sAlreadyLogged.22
+ _vtcss_appStateChangeListener.allowDynamicMemoryUsage
+ _vtcss_appStateChangeListener.cold.1
+ _vtcss_appStateChangeListener.dynamicBackgroundMemoryOnce
+ _vtmtsGetDstCropDimensions
+ _vtmtsGetIsCropped
+ _vtmtsSetupMetalDirectBlitter
+ _vtmtsSetupRenderOperationsForFunctionConstant
+ _vtmtsSetupRenderOperationsForFunctionConstant.cold.1
+ _vtmtsSetupRenderOperationsForFunctionConstant.cold.2
- GCC_except_table65
- _CFAllocatorAllocate
- _FigPlaybackLogPowerEvent
- _FigSignalErrorAt
- _MediaToolboxLibrary
- _VTCopyDecoderCapabilitiesDictionaryForCodecTypes.cold.10
- _VTCopyDecoderCapabilitiesDictionaryForCodecTypes.cold.11
- _VTCopyDecoderCapabilitiesDictionaryForCodecTypes.cold.12
- _VTCopyDecoderCapabilitiesDictionaryForCodecTypes.cold.6
- _VTCopyDecoderCapabilitiesDictionaryForCodecTypes.cold.7
- _VTCopyDecoderCapabilitiesDictionaryForCodecTypes.cold.8
- _VTCopyDecoderCapabilitiesDictionaryForCodecTypes.cold.9
- _VTCopyRAWProcessorExtensionProperties
- _VTCopyVP9DecoderCapabilitiesDictionary.cold.1
- _VTCopyVP9DecoderCapabilitiesDictionary.cold.2
- _VTCopyVP9DecoderCapabilitiesDictionary.cold.3
- _VTCopyVP9DecoderCapabilitiesDictionary.cold.4
- _VTCopyVideoDecoderExtensionProperties
- _VTDistributedCompressionGetSegmentsToReencode.cold.1
- _VTDistributedCompressionGetSegmentsToReencode.cold.2
- _VTDistributedCompressionGetSegmentsToReencode.cold.3
- _VTDistributedPreprocessingGetOverlap.cold.1
- _VTDistributedPreprocessingGetOverlap.cold.2
- _VTHDRMetadataGenerationSessionInsertData.cold.1
- _VTHDRMetadataGenerationSessionInsertData.cold.2
- _VTHDRMetadataGenerationSessionInsertData.cold.3
- _VTHDRMetadataGenerationSessionInsertData.cold.4
- _VTHDRMetadataGenerationSessionInsertData.cold.5
- _VTHDRMetadataGenerationSessionInsertData.cold.6
- _VTHDRMetadataGenerationSessionInsertData.cold.7
- _VTMotionEstimationProcessorSessionCreateMotionVectorPixelBuffer.cold.1
- _VTMotionEstimationProcessorSessionCreateMotionVectorPixelBuffer.cold.2
- _VTMotionEstimationProcessorSessionCreateMotionVectorPixelBuffer.cold.3
- _VTMotionEstimationSessionCreate.cold.1
- _VTMotionEstimationSessionCreate.cold.10
- _VTMotionEstimationSessionCreate.cold.11
- _VTMotionEstimationSessionCreate.cold.12
- _VTMotionEstimationSessionCreate.cold.2
- _VTMotionEstimationSessionCreate.cold.3
- _VTMotionEstimationSessionCreate.cold.4
- _VTMotionEstimationSessionCreate.cold.5
- _VTMotionEstimationSessionCreate.cold.6
- _VTMotionEstimationSessionCreate.cold.7
- _VTMotionEstimationSessionCreate.cold.8
- _VTMotionEstimationSessionCreate.cold.9
- _VTMotionEstimationSessionGetTypeID.sVTMotionEstimationSessionOnce
- _VTMotionEstimationSession_ShouldUseSeparateProcess.featureEnabled
- _VTMotionEstimationSession_ShouldUseSeparateProcess.onceToken
- _VTPreprocessingSessionPreprocessFrame.cold.1
- _VTPreprocessingSessionPreprocessFrame.cold.2
- _VTPreprocessingSessionPreprocessFrame.cold.3
- _VTPreprocessingSessionPreprocessFrame.cold.4
- _VTSelectAndCreateRAWProcessorInstance
- _VTTemporalFilterSessionProcessFrame.cold.1
- _VTTemporalFilterSessionProcessFrame.cold.2
- _VTTemporalFilterSessionProcessFrame.cold.3
- _VTTemporalFilterSessionProcessFrame.cold.4
- _VTTemporalFilterSessionProcessFrame.cold.5
- __MergedGlobals.367
- ___MuxedAlphaEncoder_EncodeFrame_block_invoke_2
- ___MuxedAlphaEncoder_EncodeFrame_block_invoke_3
- ___MuxedAlphaEncoder_EncodeFrame_block_invoke_3.cold.1
- ___MuxedAlphaEncoder_EncodeFrame_block_invoke_3.cold.2
- ___MuxedAlphaEncoder_EncodeFrame_block_invoke_3.cold.3
- ___MuxedAlphaEncoder_EncodeFrame_block_invoke_3.cold.4
- ___MuxedAlphaEncoder_EncodeFrame_block_invoke_3.cold.5
- ___MuxedAlphaEncoder_EncodeFrame_block_invoke_3.cold.6
- ___MuxedAlphaEncoder_EncodeMultiImageFrame_block_invoke_2
- ___MuxedAlphaEncoder_EncodeMultiImageFrame_block_invoke_3
- ___MuxedAlphaEncoder_EncodeMultiImageFrame_block_invoke_3.cold.1
- ___MuxedAlphaEncoder_EncodeMultiImageFrame_block_invoke_3.cold.2
- ___MuxedAlphaEncoder_EncodeMultiImageFrame_block_invoke_3.cold.3
- ___MuxedAlphaEncoder_EncodeMultiImageFrame_block_invoke_3.cold.4
- ___MuxedAlphaEncoder_EncodeMultiImageFrame_block_invoke_3.cold.5
- ___ParavirtualizedVideoDecoder_CreateInstanceWithSpecification_block_invoke.cold.1
- ___ParavirtualizedVideoDecoder_CreateInstanceWithSpecification_block_invoke.cold.2
- ___ParavirtualizedVideoDecoder_CreateInstanceWithSpecification_block_invoke.cold.3
- ___ParavirtualizedVideoDecoder_CreateInstanceWithSpecification_block_invoke.cold.4
- ___ParavirtualizedVideoDecoder_CreateInstanceWithSpecification_block_invoke.cold.5
- ___ParavirtualizedVideoDecoder_CreateInstanceWithSpecification_block_invoke.cold.6
- ___ParavirtualizedVideoDecoder_CreateInstanceWithSpecification_block_invoke.cold.7
- ___ParavirtualizedVideoDecoder_CreateInstanceWithSpecification_block_invoke.cold.8
- ___ParavirtualizedVideoEncoder_CreateInstanceWithSpecification_block_invoke.cold.1
- ___ParavirtualizedVideoEncoder_CreateInstanceWithSpecification_block_invoke.cold.10
- ___ParavirtualizedVideoEncoder_CreateInstanceWithSpecification_block_invoke.cold.11
- ___ParavirtualizedVideoEncoder_CreateInstanceWithSpecification_block_invoke.cold.12
- ___ParavirtualizedVideoEncoder_CreateInstanceWithSpecification_block_invoke.cold.2
- ___ParavirtualizedVideoEncoder_CreateInstanceWithSpecification_block_invoke.cold.3
- ___ParavirtualizedVideoEncoder_CreateInstanceWithSpecification_block_invoke.cold.4
- ___ParavirtualizedVideoEncoder_CreateInstanceWithSpecification_block_invoke.cold.5
- ___ParavirtualizedVideoEncoder_CreateInstanceWithSpecification_block_invoke.cold.6
- ___ParavirtualizedVideoEncoder_CreateInstanceWithSpecification_block_invoke.cold.7
- ___ParavirtualizedVideoEncoder_CreateInstanceWithSpecification_block_invoke.cold.8
- ___ParavirtualizedVideoEncoder_CreateInstanceWithSpecification_block_invoke.cold.9
- ___VTCompressionSessionRemoteServer_EncodeFrame_block_invoke_2
- ___VTDecompressionSessionRemote_DecodeTile_block_invoke_2
- ___VTPixelBlitterColorHandlingOptimized_setup_block_invoke_3
- ___VTPixelBlitterColorHandlingOptimized_setup_block_invoke_4
- ___VTPixelBlitterColorHandlingOptimized_setup_block_invoke_4.cold.1
- ___VTPixelBlitterColorHandlingOptimized_setup_block_invoke_4.cold.2
- ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke_3
- ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke_4
- ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke_4.cold.1
- ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke_4.cold.2
- ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke_4.cold.3
- ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke_4.cold.4
- ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke_4.cold.5
- ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke_4.cold.6
- ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke_4.cold.7
- ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke_4.cold.8
- ___VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke_4.cold.9
- ___block_descriptor_60_e8_32r_e119_B100?0{CGColorConversionIteratorData=Iqqqqqq^^{CGColorTRCData}^^{CGColorMatrixData}^^{CGColorNxMTransformData}}8q84q92lr32l8
- ___block_descriptor_60_e8_32r_e124_B108?0{CGColorConversionIteratorData=Iqqqqqq^^{CGColorTRCData}^^{CGColorMatrixData}^^{CGColorNxMTransformData}}8q84q92^q100lr32l8
- ___block_descriptor_tmp.1
- ___block_descriptor_tmp.10
- ___block_descriptor_tmp.16
- ___block_descriptor_tmp.193
- ___block_descriptor_tmp.2
- ___block_descriptor_tmp.21
- ___block_descriptor_tmp.3
- ___block_descriptor_tmp.4
- ___block_descriptor_tmp.5
- ___block_descriptor_tmp.59
- ___block_descriptor_tmp.6
- ___block_descriptor_tmp.69
- ___block_descriptor_tmp.7
- ___block_descriptor_tmp.71
- ___block_descriptor_tmp.78
- ___block_descriptor_tmp.79
- ___block_descriptor_tmp.80
- ___block_descriptor_tmp.81
- ___block_descriptor_tmp.83
- ___block_descriptor_tmp.88
- ___block_descriptor_tmp.9
- ___block_literal_global.12
- ___block_literal_global.17
- ___block_literal_global.18
- ___block_literal_global.195
- ___block_literal_global.21
- ___block_literal_global.23
- ___block_literal_global.25
- ___block_literal_global.34
- ___block_literal_global.5
- ___block_literal_global.52
- ___block_literal_global.56
- ___block_literal_global.61
- ___block_literal_global.7
- ___block_literal_global.81
- ___block_literal_global.90
- ___dsrxpc_callback_handleEmitTile_block_invoke
- ___dsrxpc_handleEmitMultiImage_block_invoke
- ___dssxpc_WaitForAsynchronousFrames_block_invoke
- ___getFigFairPlayCPELimitedCryptorCreateSymbolLoc_block_invoke
- ___getFigPKDCPELimitedCryptorCreateWithExternalProtectionMethodsSymbolLoc_block_invoke
- ___getFigPKDMSECPELimitedCryptorCreateWithExternalProtectionMethodsSymbolLoc_block_invoke
- ___sprintf_chk
- ___vtDecompressionSessionRemote_DecodeFrameCommon_block_invoke_2
- _checkIOSurfaceProtectionOptions
- _dssxpc_WaitForAsynchronousFrames
- _dssxpc_waitTime
- _gCompressionSessionRemoteClient
- _getFigFairPlayCPELimitedCryptorCreateSymbolLoc.ptr
- _getFigPKDCPELimitedCryptorCreateWithExternalProtectionMethodsSymbolLoc.ptr
- _getFigPKDMSECPELimitedCryptorCreateWithExternalProtectionMethodsSymbolLoc.ptr
- _kFigPowerLogSupportPlaybackEventKey_LogID
- _kFigPowerLogSupportPlaybackEventKey_VTSession_IsHDR
- _kFigPowerLogSupportPlaybackEventKey_VTSession_IsHardware
- _kFigPowerLogSupportPlaybackEventKey_VTSession_NumFramesDecoded
- _kFigPowerLogSupportPlaybackEventKey_VTSession_NumFramesDropped
- _kFigPowerLogSupportPlaybackEventKey_VTSession_NumFramesEncoded
- _kFigPowerLogSupportPlaybackEventKey_VTSession_ProcessID
- _kFigPowerLogSupportPlaybackEventKey_VTSession_ResHeight
- _kFigPowerLogSupportPlaybackEventKey_VTSession_ResWidth
- _kFigPowerLogSupportPlaybackEventKey_VTSession_SessionDuration
- _kFigPowerLogSupportPlaybackEventKey_VTSession_VideoCodecType
- _kVTCompressionPropertyKey_RecommendedParallelizationLimit
- _kVTDecompressionPropertyKey_DecoderProducesRAWOutput
- _kVTDecompressionPropertyKey_GuestExternalProtectionStatus
- _kVTDecompressionPropertyKey_RequestRAWOutput
- _kVTExtensionProperties_CodecNameKey
- _kVTExtensionProperties_ContainingBundleNameKey
- _kVTExtensionProperties_ContainingBundleURLKey
- _kVTExtensionProperties_ExtensionIdentifierKey
- _kVTExtensionProperties_ExtensionNameKey
- _kVTExtensionProperties_ExtensionURLKey
- _kVTVideoDecoderSpecification_GuestExternalProtectionStatus
- _objc_release_x22
- _paravirtualizedVideoDecoder_DrawCharsToPixelBuffer
- _paravirtualizedVideoDecoder_FillPixelBufferWithYCbCrColor
- _paravirtualizedVideoDecoder_handleGuestExternalProtectionStatusSetPropertyAndCopyReplacementValue
- _sCreateAndPopulateTemporalFiltersRegistryOnce
- _sCreateRegistryOnce
- _sMotionEstimationRegistry
- _sTemporalFilterRegistry
- _sVTCompressionSessionRemoteID
- _sVTMotionEstimationSessionID
- _sVideoDecoderRegistry
- _softLink_FigFairPlayCPELimitedCryptorCreate
- _softLink_FigFairPlayCPELimitedCryptorCreate.cold.1
- _vtCompressionSessionInitializeDolbyHDRSessions
- _vtCompressionSessionIsDolbyCompatible
- _vtCompressionSessionSetHDRFormat
- _vtCreateAndPopulateTemporalFilterRegistry
- _vtMetalTransferSessionRebuild
- _vtMotionEstimationSessionFinalize.cold.3
- _vtVideoDecoderInfoInitOnce
- _vt_Rotate_Celeste.sAlreadyLogged.7
- _vtcg_createCGCompatiblePixelBuffer.cold.1
- _vtcg_createCGCompatiblePixelBuffer.cold.2
- _vtcg_createCGCompatiblePixelBuffer.cold.3
- _vtcg_createCGCompatiblePixelBuffer.cold.4
- _vtcg_createCGCompatiblePixelBuffer.cold.5
CStrings:
+ "  "
+ "   "
+ " ! compressionSessionOut"
+ " (catchup only)"
+ " (guest waiting)"
+ " (host waiting)"
+ " (in place)"
+ " (reply for guest)"
+ " (reply for host)"
+ " (to be continued)"
+ " -- CLIENT DIED"
+ " -- INVALIDATED"
+ " NOT"
+ " [%zu]"
+ " flipH"
+ " flipV"
+ "! imageBuffer"
+ "! outputCallback "
+ "! sampleBuffer"
+ "! session"
+ "! taggedBufferGroup"
+ "! temporalFilterSessionOut "
+ "#16@0:8"
+ "%02x "
+ "%c"
+ "%c%c%c%c "
+ "%p-"
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "%zu "
+ "(%s) "
+ "(...)"
+ "(Fig)"
+ "(will output non-protected IOSurfaces)"
+ "(will output protected IOSurfaces to protected display)"
+ "+[VTTemporalNoiseFilterConfiguration _loadCapabilities]"
+ "-1"
+ "-108"
+ "-304"
+ "-[VTFrameProcessor init]"
+ "-[VTFrameProcessorFrame initWithBuffer:presentationTimeStamp:]"
+ "-[VTFrameProcessorOpticalFlow initWithForwardFlow:backwardFlow:]"
+ "-[VTTemporalNoiseFilterConfiguration loadProperties]"
+ "-[VTTemporalNoiseFilterImplementation _checkForDiscontinuity:]"
+ "-[VTTemporalNoiseFilterImplementation _completeFrame:]"
+ "-[VTTemporalNoiseFilterImplementation _completeFrame:]_block_invoke"
+ "-[VTTemporalNoiseFilterImplementation _completeFrames]"
+ "-[VTTemporalNoiseFilterImplementation _processFrame:outputFrame:useClientProvidedOutputFrame:]"
+ "-[VTTemporalNoiseFilterImplementation _processReferenceFrameIfNotProcessed:]"
+ "-[VTTemporalNoiseFilterImplementation _processSourceFrameIfNotProcessed:completionHandler:]"
+ "-[VTTemporalNoiseFilterImplementation _setFilterStrength:]"
+ "-[VTTemporalNoiseFilterImplementation _validateParameters:error:]"
+ "-[VTTemporalNoiseFilterImplementation finishProcessing]"
+ "-[VTTemporalNoiseFilterImplementation handleEmittedFrame:presentationTimestamp:status:infoFlags:]"
+ "-[VTTemporalNoiseFilterImplementation processWithParams:completionHandler:error:]"
+ "-[VTTemporalNoiseFilterImplementation processWithParams:error:]"
+ "-[VTTemporalNoiseFilterImplementation processWithParams:error:]_block_invoke"
+ "-[VTTemporalNoiseFilterImplementation startSessionWithConfiguration:error:]"
+ "...<- "
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Celeste/Sources/VideoToolboxRemote/VTCompressionSession_Remote.c"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Celeste/Sources/VideoToolboxRemote/VTCompressionSession_Server.c"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Celeste/Sources/VideoToolboxRemote/VTDecompressionSession_Remote.c"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Celeste/Sources/VideoToolboxRemote/VTDecompressionSession_Server.c"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Can't guess what this image's colourspace is"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: GetConversionRoutine: unrecognised source colourspace"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Unhandled case in JPEG GetConversionRoutine: 8-grey -> ?"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Unhandled case in JPEG GetConversionRoutine: YCbCr 411 -> ?"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Unhandled case in JPEG GetConversionRoutine: YCbCr 422 -> ?"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Unhandled case in JPEG GetConversionRoutine: YCbCr with funny sampling -> ?"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Warning in GetConversionRoutine: unhandled number of components"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_block.c %s: Warning: JPEG is doing nothing."
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_blockdecode.c %s: Decode Error in DecodeBlocks"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: JPEG SOF marker has a bad quantization table selector"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: JPEG SOF marker has a bad sampling factor"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: JPEG SOF marker has too many components for us"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: Progressive JPEG scan SOS has Se > 63"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: Progressive JPEG scan SOS has Ss > Se"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: Progressive JPEG scan trying to use undefined AC huffman table"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: Progressive JPEG scan trying to use undefined DC huffman table"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_marker.c %s: Sequential JPEG trying to use undefined huffman table"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_progressive.c %s: Bad data: attempted to place a value outside this scan's coefficient range."
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_prototypeDecode.c %s: Mismatch between the height allocated and what is read from the bitstream."
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoCodecs/JPEG/JPEG_prototypeDecode.c %s: Mismatch between the width allocated and what is read from the bitstream."
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s:  Calculated dataSize + HeaderSize %d is larger than allocated size %d"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s:  height %d is not multiple of tileHeight %d, we can only fill whole tile CVPixelBuffer will not be black filled."
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s:  width %d is not multiple of tileWidth %d, we can only fill whole tile CVPixelBuffer will not be black filled."
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: BlackBlock is more than %d bytes -- need to increase limit in VT to accommodate this pixel format: '%.4s'"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: bad value for kCVPixelFormatBlockHeight"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: bad value for kCVPixelFormatBlockHeight for pixelformat '%.4s' (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: bad value for kCVPixelFormatBlockWidth for pixelformat '%.4s' (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: bad value for kCVPixelFormatHorizontalSubsampling for pixelformat '%.4s' (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: bad value for kCVPixelFormatVerticalSubsampling for pixelformat '%.4s' (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: blackfillHeightInTiles %d is greater than planeHeightInTiles %d"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: blackfillWidthInTiles %d is greater than planeWidthInTiles %d"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: dataPattern is NULL"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: destination address is NULL"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: didn't find kCVPixelFormatPlane dictionary for index %zu for pixelformat '%.4s' (%d) in pixel format description dictionary"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: didn't find kCVPixelFormatPlanes for pixelformat '%.4s' (%d) in pixel format description dictionary"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: kCVPixelFormatBitsPerBlock not set for pixelformat '%.4s' (%d) in pixel format description dictionary"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: left offset %d is not tileWidth %d aligned, we can only black fill whole tile"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: planeIndex out of range"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTBlackFill.c %s: top offset %d is not tileHeight %d aligned, we can only black fill whole tile"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTCMSessionSupport.c %s: MediaExperience is absent - CMSession support disabled."
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTFrameProcessor/VTFrameProcessorFrame.m %s: Buffer %p not IOsurface backed. VTFrameProcessorFrame requires IOsurface backing"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTFrameProcessor/VTFrameProcessorFrame.m %s: Fail to initialize"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTFrameProcessor/VTFrameProcessorFrame.m %s: Input buffer cannot be nil in VTFrameProcessorFrame"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTFrameProcessor/VTFrameProcessorFrame.m %s: backwardFlow %p is not IOSurface backed"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTFrameProcessor/VTFrameProcessorFrame.m %s: backwardFlow cannot be nil in VTFrameProcessorOpticalFlow"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTFrameProcessor/VTFrameProcessorFrame.m %s: forwardFlow %p is not IOSurface backed"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTFrameProcessor/VTFrameProcessorFrame.m %s: forwardFlow cannot be nil in VTFrameProcessorOpticalFlow"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/VideoToolbox/VTTestMotionEstimationProcessor.c %s: unrecognised property key %@"
+ "/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler"
+ "/System/Library/PrivateFrameworks/VideoEffect.framework/VideoEffect"
+ "/System/Library/VideoEncoders/AV1SW.videoencoder"
+ "<-"
+ "<< TestIPBVideoDecoder >>"
+ "<< TestIPBVideoDecoder >> %s: (%p)"
+ "<< TestIPBVideoDecoder >> %s: (%p) called for session %p with dimensions %d x %d"
+ "<< TestIPBVideoDecoder >> %s: <QTError errmsg=\"IPB: Incorrect sequence for %s%s (display #%s)%s intended [%s], actual [%s]%s\""
+ "<< TestIPBVideoDecoder >> %s: Packing type is None"
+ "<< TestIPBVideoDecoder >> %s: Packing type is Over-Under"
+ "<< TestIPBVideoDecoder >> %s: Packing type is Side-by-Side"
+ "<< TestIPBVideoDecoder >> %s: Returning instance %p"
+ "<< TestIPBVideoDecoder >> %s: Setting delay of %d ms before sending decoded frames"
+ "<< TestIPBVideoDecoder >> %s: Video has stereo views"
+ "<< TestIPBVideoDecoder >> %s: decoding %s%s (display #%s)%s%s"
+ "<<< VTRotation >>>"
+ "<<< VTRotation >>> %s: Falling back to generic 180 rotation"
+ "<<< VTRotation >>> %s: Falling back to generic 90 rotation"
+ "<<< VTRotation >>> %s: Falling back to generic in-place 180 rotation"
+ "<<< VTRotationCeleste >>>"
+ "<<< VTRotationCeleste >>> %s: %s: {%.2f,%.2f},{%.2f,%.2f}"
+ "<<< VTRotationCeleste >>> %s: IOSurfaceAcceleratorCreate failed with %d"
+ "<<< VTRotationCeleste >>> %s: IOSurfaceAcceleratorGetHistogram failed with %d, transfer succeeded but histogram isn't available"
+ "<<< VTRotationCeleste >>> %s: IOSurfaceAcceleratorTransformSurface %d %c%c%c%c [%lf,%lf,%lf,%lf] (%d,%d,%d) => %c%c%c%c [%lf,%lf,%lf,%lf] (%d,%d,%d)"
+ "<<< VTRotationCeleste >>> %s: dest pixel format %c%c%c%c unsupported"
+ "<<< VTRotationCeleste >>> %s: dest width/height not even"
+ "<<< VTRotationCeleste >>> %s: destination full height not even"
+ "<<< VTRotationCeleste >>> %s: destination full width not even"
+ "<<< VTRotationCeleste >>> %s: hardware does not support color conversion"
+ "<<< VTRotationCeleste >>> %s: hardware doesn't support yuvs/f for a rotation of %i degrees"
+ "<<< VTRotationCeleste >>> %s: height scale factor %f is outside of allowed range %f to %f"
+ "<<< VTRotationCeleste >>> %s: out of bounds dest rect"
+ "<<< VTRotationCeleste >>> %s: out of bounds source rect"
+ "<<< VTRotationCeleste >>> %s: rotation degrees:%i not supported"
+ "<<< VTRotationCeleste >>> %s: source pixel format %c%c%c%c unsupported"
+ "<<< VTRotationCeleste >>> %s: source width/height not even"
+ "<<< VTRotationCeleste >>> %s: unsupported IOSurfaceCompressType %d for plane %d for pixel format %c%c%c%c"
+ "<<< VTRotationCeleste >>> %s: width scale factor %f is outside of allowed range %f to %f"
+ "<<<< AppleJPEGVideoDecoder >>>>"
+ "<<<< CompressionSessionRemote >>>>"
+ "<<<< CompressionSessionRemote >>>> %s: "
+ "<<<< CompressionSessionRemote >>>> %s: %d: IOSurfacePort %d, pixelBufferAtomData %p, pixelBufferAtomDataCnt %d, iClient->lastSerializedPixelBufferDataSize %zd"
+ "<<<< CompressionSessionRemote >>>> %s: %d: tagCollectionDataLength -> %d"
+ "<<<< CompressionSessionRemote >>>> %s: (%p) %@"
+ "<<<< CompressionSessionRemote >>>> %s: (%p) %@ : %@"
+ "<<<< CompressionSessionRemote >>>> %s: (%p) called"
+ "<<<< CompressionSessionRemote >>>> %s: (%p) client callback for frame (%llu) with error (%d)"
+ "<<<< CompressionSessionRemote >>>> %s: (%p) frameRefcon (%llu) missing in pendingFrames, frameErrorStatus (%d)"
+ "<<<< CompressionSessionRemote >>>> %s: (%p) server connection died"
+ "<<<< CompressionSessionRemote >>>> %s: ***FRAME IS PENDING"
+ "<<<< CompressionSessionRemote >>>> %s: CreatePixelBuffer failed (%i)"
+ "<<<< CompressionSessionRemote >>>> %s: CreatePropertyList failed (%i)"
+ "<<<< CompressionSessionRemote >>>> %s: CreateSampleBuffer failed (%i)"
+ "<<<< CompressionSessionRemote >>>> %s: FigTaggedBufferGroupGetCount(taggedBufferGroup %p) -> %d"
+ "<<<< CompressionSessionRemote >>>> %s: Session was invalidated"
+ "<<<< CompressionSessionRemote >>>> %s: VTCompressionSessionRemoteClient_TemporalProcessFrame returned %d"
+ "<<<< CompressionSessionRemote >>>> %s: [%p] %s %@"
+ "<<<< CompressionSessionRemote >>>> %s: [session %p] remapped %i to kVTVideoEncoderMalfunctionErr (%i)"
+ "<<<< CompressionSessionRemote >>>> %s: called"
+ "<<<< CompressionSessionRemote >>>> %s: calling VTCompressionSessionRemoteClient_CopyTemporalFilterList"
+ "<<<< CompressionSessionRemote >>>> %s: calling VTCompressionSessionRemoteClient_Create"
+ "<<<< CompressionSessionRemote >>>> %s: calling VTCompressionSessionRemoteClient_MultiPassStorageCreate"
+ "<<<< CompressionSessionRemote >>>> %s: calling VTCompressionSessionRemoteClient_TemporalFilterCreate"
+ "<<<< CompressionSessionRemote >>>> %s: calling VTCompressionSessionRemoteClient_TemporalProcessFrame"
+ "<<<< CompressionSessionRemote >>>> %s: calling VTMotionEstimationSessionRemote_Create"
+ "<<<< CompressionSessionRemote >>>> %s: calling VTTileCompressionSessionRemote_Create"
+ "<<<< CompressionSessionRemote >>>> %s: calling client with frame"
+ "<<<< CompressionSessionRemote >>>> %s: clientCallbackQueue enter"
+ "<<<< CompressionSessionRemote >>>> %s: clientCallbackQueue exit"
+ "<<<< CompressionSessionRemote >>>> %s: create remote compression session %p for session:%p"
+ "<<<< CompressionSessionRemote >>>> %s: create remote temporal filter session %p for session:%p"
+ "<<<< CompressionSessionRemote >>>> %s: creating pixel buffer pool failed %i"
+ "<<<< CompressionSessionRemote >>>> %s: dequeue failed (%i)"
+ "<<<< CompressionSessionRemote >>>> %s: enter"
+ "<<<< CompressionSessionRemote >>>> %s: error serializing tagged buffer group %p index %d pixel buffer:%p err:%i"
+ "<<<< CompressionSessionRemote >>>> %s: exit"
+ "<<<< CompressionSessionRemote >>>> %s: localErr: %d, listOfTemporalFiltersOutData: %p, listOfTemporalFiltersOutData: %u"
+ "<<<< CompressionSessionRemote >>>> %s: lookup for client 0x%llx returned %p"
+ "<<<< CompressionSessionRemote >>>> %s: neither callback nor handler?"
+ "<<<< CompressionSessionRemote >>>> %s: no frame available"
+ "<<<< CompressionSessionRemote >>>> %s: pending notification!"
+ "<<<< CompressionSessionRemote >>>> %s: serverErr: %d, infoFlags: %d"
+ "<<<< CompressionSessionRemote >>>> Fig"
+ "<<<< CompressionSessionServer >>>>"
+ "<<<< CompressionSessionServer >>>> %s: FigRemote_CreatePixelBufferFromSerializedAtomData failed for tagged buffer %d"
+ "<<<< CompressionSessionServer >>>> %s: FigTaggedBufferGroupCreate(count %d) -> %p, err %d"
+ "<<<< CompressionSessionServer >>>> %s: VTTemporalFilterSessionProcessFrame returned %d"
+ "<<<< CompressionSessionServer >>>> %s: Will use same memory profile if app goes to background - thank you for setting \"defaults write com.apple.coremedia vtcsserver_dynamicbackgroundmemory -bool NO\""
+ "<<<< CompressionSessionServer >>>> %s: called"
+ "<<<< CompressionSessionServer >>>> %s: calling VTTemporalFilterSessionProcessFrame"
+ "<<<< CompressionSessionServer >>>> %s: client [%p] is UNREGISTERING"
+ "<<<< CompressionSessionServer >>>> %s: client allocated for pid %i"
+ "<<<< CompressionSessionServer >>>> %s: client died, done waiting for pendingFrameSemaphore"
+ "<<<< CompressionSessionServer >>>> %s: client with pid %u being notified of application state change to %u"
+ "<<<< CompressionSessionServer >>>> %s: created compression session:%p with err:%i"
+ "<<<< CompressionSessionServer >>>> %s: created multipass storage:%p with err:%i"
+ "<<<< CompressionSessionServer >>>> %s: created temporal filter session:%p with err:%i"
+ "<<<< CompressionSessionServer >>>> %s: created tile compression session:%p with err:%i"
+ "<<<< CompressionSessionServer >>>> %s: enter"
+ "<<<< CompressionSessionServer >>>> %s: error serializing pixelbuffer buffer:%p err:%i"
+ "<<<< CompressionSessionServer >>>> %s: error serializing sample buffer:%p err:%i"
+ "<<<< CompressionSessionServer >>>> %s: exit"
+ "<<<< CompressionSessionServer >>>> %s: exit: morePending:%i, error:%i"
+ "<<<< CompressionSessionServer >>>> %s: frameProperties:%@"
+ "<<<< CompressionSessionServer >>>> %s: key:\"VTMultiPassStorage\" value:%@ err:%i"
+ "<<<< CompressionSessionServer >>>> %s: key:%@ value:%@ err:%i"
+ "<<<< CompressionSessionServer >>>> %s: listOfTemporalFilters: %@"
+ "<<<< CompressionSessionServer >>>> %s: listOfTemporalFiltersOutData: %p, listOfTemporalFiltersOutDataSize: %zu"
+ "<<<< CompressionSessionServer >>>> %s: new client"
+ "<<<< CompressionSessionServer >>>> %s: new temporal filter session client"
+ "<<<< CompressionSessionServer >>>> %s: options:%@"
+ "<<<< CompressionSessionServer >>>> %s: properties:%@ err:%i"
+ "<<<< CompressionSessionServer >>>> %s: setting kVTCompressionPropertyKey_ClientPID failed (err=%d)"
+ "<<<< CompressionSessionServer >>>> %s: task (pid %u) is NOT running foreground - invalidating session"
+ "<<<< CompressionSessionServer >>>> %s: task (pid %u) is running background"
+ "<<<< CompressionSessionServer >>>> %s: task (pid %u) is running foreground"
+ "<<<< CompressionSessionServer >>>> %s: task (pid %u) unexpected app state %u"
+ "<<<< CompressionSessionServer >>>> %s: tileProperties:%@"
+ "<<<< CompressionSessionServer >>>> Fig"
+ "<<<< DecompressionSessionRemote >>>>"
+ "<<<< DecompressionSessionRemote >>>> %s: "
+ "<<<< DecompressionSessionRemote >>>> %s:  return: %d"
+ "<<<< DecompressionSessionRemote >>>> %s:  sync frame - dequeue anything pending"
+ "<<<< DecompressionSessionRemote >>>> %s: %p Received \"%@\""
+ "<<<< DecompressionSessionRemote >>>> %s: %p server connection died"
+ "<<<< DecompressionSessionRemote >>>> %s: %{public}@"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) %@"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) %@ : %@"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) Added pending frame info: nextFrameIdentifier: %ld, frameID: %llu, original refcon: %p, sample count: %zu"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) Done waiting for decodeReturnSemaphore"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) EventLink decode frame message was cancelled"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) EventLink waitForAsynchronousFrames message was cancelled"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) FigTaggedBufferGroupCreate(count %d) -> %p, err %d"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) Received emitframe: frameID %d, status %d"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) Received emitframe: frameID: %d"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) Received emitframe: frameID: %d, status = %d"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) Sending message through EventLink failed. Err %d. Falling back to XPC."
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) Took EventLink path"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) Took XPC path"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) WARNING: Emitting frameID: (%llu) with error: %d"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) WARNING: waited %016lld seconds for video decompression session decode frames return."
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) async emit callback "
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) called"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) emit callback: frameID %d, status %d "
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) emit callback: frameID: %llu, DS output refCon: %p, originalRefCon: %p, imageBuffer: %p, framePTS: %lld/%d, frameDuration:  %lld/%d"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) failed to send emit return message to server: %d"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) got FinishDelayedFramesReturn from server"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) got FinishDelayedTilesReturn from server"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) got decode status from Server"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) got finishReturn from Server"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) memory origin copied: %p, err: %d"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) neither callback nor handler?"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) no client callback?"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) no multi image callback ?"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) resetting error (%d), since emit callback has been called"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) return err: %d"
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) skipping emit callback."
+ "<<<< DecompressionSessionRemote >>>> %s: (%p) tagCollectionCFData is %p while pixelBuffer is %p. Dump these data."
+ "<<<< DecompressionSessionRemote >>>> %s: ***FRAME IS PENDING"
+ "<<<< DecompressionSessionRemote >>>> %s: Called."
+ "<<<< DecompressionSessionRemote >>>> %s: Client/Server decompression session will prefer decode frames over XPC -- thank you for setting \"defaults write com.apple.coremedia decompression_session_xpc_decode_frame_prefers_event_link -bool no\""
+ "<<<< DecompressionSessionRemote >>>> %s: FigRemote_CreatePixelBufferFromSerializedAtomData failed for tagged buffer %d"
+ "<<<< DecompressionSessionRemote >>>> %s: FigTaggedBufferGroupCreate(count %d) -> %p, err %d"
+ "<<<< DecompressionSessionRemote >>>> %s: Lost server connection"
+ "<<<< DecompressionSessionRemote >>>> %s: Session was invalidated"
+ "<<<< DecompressionSessionRemote >>>> %s: Unknown opCode: 0x%0x"
+ "<<<< DecompressionSessionRemote >>>> %s: VTDecompressionSessionRemoteClient_DequeueNextPendingFrame -> gotFrame %d, serverErr %d, morePending %d; frameIOSurfacePort %d, taggedBuffers[0].IOSurfacePort %d, taggedBuffers[1].IOSurfacePort %d, taggedBuffers[2].IOSurfacePort %d, taggedBuffers[3].IOSurfacePort %d, taggedBuffers[4].IOSurfacePort %d"
+ "<<<< DecompressionSessionRemote >>>> %s: WARNING: waited %016lld seconds for video decompress session to complete asynchronous frames."
+ "<<<< DecompressionSessionRemote >>>> %s: WARNING: waited %016lld seconds for video decompression session decode tile; maybe it is stuck for app cannot handle emit-tile ?"
+ "<<<< DecompressionSessionRemote >>>> %s: WARNING: waited %lld seconds for video decompress session to complete asynchronous frames."
+ "<<<< DecompressionSessionRemote >>>> %s: [%p] %s %@"
+ "<<<< DecompressionSessionRemote >>>> %s: [%p] (0x%016llx) waited %d ms for outputCallbackDispatchGroup. (Long wait time can happen when the client app goes to background)"
+ "<<<< DecompressionSessionRemote >>>> %s: [%p] WARNING: finished waiting for decompression session to complete asynchronous frames %s%s%s."
+ "<<<< DecompressionSessionRemote >>>> %s: [%p] WARNING: waited %lld seconds for decompression session to complete asynchronous frames."
+ "<<<< DecompressionSessionRemote >>>> %s: [%p] err: %d canDoIt : %d"
+ "<<<< DecompressionSessionRemote >>>> %s: [%p] waited %d ms for outputCallbackDispatchGroup. (Long wait time can happen when the client app goes to background)"
+ "<<<< DecompressionSessionRemote >>>> %s: called"
+ "<<<< DecompressionSessionRemote >>>> %s: called [%p]"
+ "<<<< DecompressionSessionRemote >>>> %s: called [outputHandler: %p] [multiImageOutputHandler: %p] [sampleCount: %d] remoteRefCon %d originalRefCon %p"
+ "<<<< DecompressionSessionRemote >>>> %s: called. [%p]"
+ "<<<< DecompressionSessionRemote >>>> %s: called. [%p] (0x%016llx)"
+ "<<<< DecompressionSessionRemote >>>> %s: called. [%p] Property key: %@"
+ "<<<< DecompressionSessionRemote >>>> %s: called. [%p] Property key: %@, value: %@"
+ "<<<< DecompressionSessionRemote >>>> %s: called. [%p] callback: %p, refcon: %p"
+ "<<<< DecompressionSessionRemote >>>> %s: called. [%p] sampleBuffer: %p, decodeFlags: 0x%x, frameOptions: %p, outputHandler: %p, multiImageOutputHandler: %p"
+ "<<<< DecompressionSessionRemote >>>> %s: called. [%p] sampleBuffer: %p, decodeFlags: 0x%x, frameOptions: %p, sourceFrameRefCon: %p"
+ "<<<< DecompressionSessionRemote >>>> %s: called. [%p] sampleBuffer: %p, decodeFlags: 0x%x, tileCropOffset: (%d, %d), tileCropDimension: %d x %d, imageBuffer: %p, offsetWithinImageBuffer: (%d, %d)"
+ "<<<< DecompressionSessionRemote >>>> %s: called. remote bridge: %@"
+ "<<<< DecompressionSessionRemote >>>> %s: called. remote bridge: %@, callback: %p, refcon: %p"
+ "<<<< DecompressionSessionRemote >>>> %s: called. remote bridge: %@, formatDesc: %@"
+ "<<<< DecompressionSessionRemote >>>> %s: called. remote bridge: %@, properties %@"
+ "<<<< DecompressionSessionRemote >>>> %s: called. remote bridge: %@, property key: %@"
+ "<<<< DecompressionSessionRemote >>>> %s: called. remote bridge: %@, property key: %@, value: %@"
+ "<<<< DecompressionSessionRemote >>>> %s: called. remote bridge: %@, sampleBuffer: %p, decodeFlags: 0x%x, frameOptions: %p, outputHandler: %p, multiImageOutputHandler: %p"
+ "<<<< DecompressionSessionRemote >>>> %s: called. remote bridge: %@, sampleBuffer: %p, decodeFlags: 0x%x, frameOptions: %p, sourceFrameRefCon: %p"
+ "<<<< DecompressionSessionRemote >>>> %s: called. remote bridge: %@, sampleBuffer: %p, decodeFlags: 0x%x, tileCropOffset: (%d, %d), tileCropDimensions (%d x %d)"
+ "<<<< DecompressionSessionRemote >>>> %s: called. session bridge: %@"
+ "<<<< DecompressionSessionRemote >>>> %s: called. session: %@"
+ "<<<< DecompressionSessionRemote >>>> %s: called: [%p]"
+ "<<<< DecompressionSessionRemote >>>> %s: calling client with frame remoteRefCon %d"
+ "<<<< DecompressionSessionRemote >>>> %s: cannot create remote client: %d"
+ "<<<< DecompressionSessionRemote >>>> %s: clientCallbackQueue enter"
+ "<<<< DecompressionSessionRemote >>>> %s: clientCallbackQueue exit"
+ "<<<< DecompressionSessionRemote >>>> %s: create remote decompression session %p for session:%p"
+ "<<<< DecompressionSessionRemote >>>> %s: create remote tile decompression session %p for session:%p"
+ "<<<< DecompressionSessionRemote >>>> %s: create remote tile decompression session %p for tile session:%p"
+ "<<<< DecompressionSessionRemote >>>> %s: dequeue failed (%i)"
+ "<<<< DecompressionSessionRemote >>>> %s: enter"
+ "<<<< DecompressionSessionRemote >>>> %s: entered. session: %@"
+ "<<<< DecompressionSessionRemote >>>> %s: exit"
+ "<<<< DecompressionSessionRemote >>>> %s: found frame with frame remoteRefCon %d original refCon %p"
+ "<<<< DecompressionSessionRemote >>>> %s: frameID: %llu, outstanding sample count: %zu, outstanding emit count: %zu"
+ "<<<< DecompressionSessionRemote >>>> %s: lookup for client 0x%llx returned %p"
+ "<<<< DecompressionSessionRemote >>>> %s: neither callback nor handler?"
+ "<<<< DecompressionSessionRemote >>>> %s: no frame available"
+ "<<<< DecompressionSessionRemote >>>> %s: pending notification!"
+ "<<<< DecompressionSessionRemote >>>> %s: pixel bufer recipient created: %p"
+ "<<<< DecompressionSessionRemote >>>> %s: return [%p] err: %d"
+ "<<<< DecompressionSessionRemote >>>> %s: return [%p] err: %d "
+ "<<<< DecompressionSessionRemote >>>> %s: return. minOutputPTS: %llu / %d"
+ "<<<< DecompressionSessionRemote >>>> %s: return. remote bridge: %p, err: %d"
+ "<<<< DecompressionSessionRemote >>>> %s: return. session bridge: %p: err: %d"
+ "<<<< DecompressionSessionRemote >>>> %s: server connection died!"
+ "<<<< DecompressionSessionRemote >>>> Fig"
+ "<<<< DecompressionSessionServer >>>>"
+ "<<<< DecompressionSessionServer >>>> %s: %d: IOSurfacePortOut %d, pixelBufferAtomDataOut %p, pixelBufferAtomDataCntOut %d, iClient->lastSerializedPixelBufferDataSize %zd"
+ "<<<< DecompressionSessionServer >>>> %s: %d: tagCollectionDataLength -> %d"
+ "<<<< DecompressionSessionServer >>>> %s: CopyProperty %@ failed. err=%d"
+ "<<<< DecompressionSessionServer >>>> %s: FigTaggedBufferGroupGetCount(frame->taggedBufferGroup %p) -> %d"
+ "<<<< DecompressionSessionServer >>>> %s: VTDecompressionSessionSetMultiImageCallback -> %d"
+ "<<<< DecompressionSessionServer >>>> %s: [%p] Tile statistics: count: %d, %{public}s: %d x %d, canvas size: %d x %d"
+ "<<<< DecompressionSessionServer >>>> %s: called"
+ "<<<< DecompressionSessionServer >>>> %s: called client [%p]"
+ "<<<< DecompressionSessionServer >>>> %s: called client [%p]%s%s"
+ "<<<< DecompressionSessionServer >>>> %s: called with cmd_port %d == client %p"
+ "<<<< DecompressionSessionServer >>>> %s: client %p died or invalidated (2)"
+ "<<<< DecompressionSessionServer >>>> %s: client %p: break from enforceQueueLimit loop. subSession: %p, subTileSession: %p, iClient->clientDied: %d,  iClient->invalidated: %d, iClient->subSessionIsGone: %d"
+ "<<<< DecompressionSessionServer >>>> %s: client [%p] about to invalidate subDecompressionSession"
+ "<<<< DecompressionSessionServer >>>> %s: client [%p] about to invalidate subTileDecompressionSession"
+ "<<<< DecompressionSessionServer >>>> %s: client [%p] allocated for pid %i"
+ "<<<< DecompressionSessionServer >>>> %s: client [%p] disposing clientConnection %p"
+ "<<<< DecompressionSessionServer >>>> %s: client [%p] freeing queued frames"
+ "<<<< DecompressionSessionServer >>>> %s: client [%p] invalidating session %p "
+ "<<<< DecompressionSessionServer >>>> %s: client [%p] is UNREGISTERING, setting clientDied"
+ "<<<< DecompressionSessionServer >>>> %s: client [%p] signalling pendingFrameSemaphore, waiting on asyncMessageHandlerGroup"
+ "<<<< DecompressionSessionServer >>>> %s: client allocated for pid %i"
+ "<<<< DecompressionSessionServer >>>> %s: client not found for cmd_port %d"
+ "<<<< DecompressionSessionServer >>>> %s: client with pid %u being notified of application state change to %u"
+ "<<<< DecompressionSessionServer >>>> %s: created decompression session:%p with err:%i"
+ "<<<< DecompressionSessionServer >>>> %s: enter"
+ "<<<< DecompressionSessionServer >>>> %s: error %i"
+ "<<<< DecompressionSessionServer >>>> %s: error serializing pixel buffer:%@ err:%i"
+ "<<<< DecompressionSessionServer >>>> %s: error serializing pixel buffer:%p err:%i"
+ "<<<< DecompressionSessionServer >>>> %s: error serializing tagged buffer group %p index %d pixel buffer:%p err:%i"
+ "<<<< DecompressionSessionServer >>>> %s: exit"
+ "<<<< DecompressionSessionServer >>>> %s: exit: morePending:%i, error:%i"
+ "<<<< DecompressionSessionServer >>>> %s: frame %p enqueued"
+ "<<<< DecompressionSessionServer >>>> %s: new client"
+ "<<<< DecompressionSessionServer >>>> %s: new client created: %p"
+ "<<<< DecompressionSessionServer >>>> %s: new tile client"
+ "<<<< DecompressionSessionServer >>>> %s: new tile client created: %p"
+ "<<<< DecompressionSessionServer >>>> %s: returning (%i)"
+ "<<<< DecompressionSessionServer >>>> %s: setting kVTDecompressionPropertyKey_ClientPID failed (err=%d)"
+ "<<<< DecompressionSessionServer >>>> %s: status %d, taggedBufferGroup %p, pts %1.3f, dur %1.3f %s%s"
+ "<<<< DecompressionSessionServer >>>> %s: task (pid %u) is NOT running foreground - invalidating session"
+ "<<<< DecompressionSessionServer >>>> %s: task (pid %u) is running background"
+ "<<<< DecompressionSessionServer >>>> %s: task (pid %u) is running foreground"
+ "<<<< DecompressionSessionServer >>>> %s: task (pid %u) unexpected app state %u"
+ "<<<< DecompressionSessionServer >>>> Fig"
+ "<<<< DecompressionSessionXPCServer >>>>"
+ "<<<< DecompressionSessionXPCServer >>>> %s:  client record: %@"
+ "<<<< DecompressionSessionXPCServer >>>> %s:  client: %@"
+ "<<<< DecompressionSessionXPCServer >>>> %s: Called %@, PID: %d"
+ "<<<< DecompressionSessionXPCServer >>>> %s: Called for %d"
+ "<<<< DecompressionSessionXPCServer >>>> %s: Called for PID: %d"
+ "<<<< DecompressionSessionXPCServer >>>> %s: Client/Server decompression session will create up to %d event links to handle multiple threads -- thank you for setting \"defaults write com.apple.coremedia decompression_session_xpc_max_emit_frame_event_links -int %d\""
+ "<<<< DecompressionSessionXPCServer >>>> %s: Client/Server decompression session will prefer emit frames over XPC -- thank you for setting \"defaults write com.apple.coremedia decompression_session_xpc_emit_frame_prefers_event_link -bool no\""
+ "<<<< DecompressionSessionXPCServer >>>> %s: Client/Server decompression session will prefer emit frames over XPC for applications -- thank you for setting \"defaults write com.apple.coremedia decompression_session_xpc_emit_frame_prefers_event_link_for_app -bool no\""
+ "<<<< DecompressionSessionXPCServer >>>> %s: Created VTPerClientAudioSession for PID %d: %p, audio session: %p"
+ "<<<< DecompressionSessionXPCServer >>>> %s: Current cache: %@"
+ "<<<< DecompressionSessionXPCServer >>>> %s: DecompressionSessionMessageQueue create with FigThreadPriority %d"
+ "<<<< DecompressionSessionXPCServer >>>> %s: Dispose message received. Disassociate client: %p"
+ "<<<< DecompressionSessionXPCServer >>>> %s: Failed to set up emit frame event link. Err = %d"
+ "<<<< DecompressionSessionXPCServer >>>> %s: Found vtPerClientAudioSession for PID %d in cache"
+ "<<<< DecompressionSessionXPCServer >>>> %s: Initializing gPerClientAudioSessionCache"
+ "<<<< DecompressionSessionXPCServer >>>> %s: No sub session"
+ "<<<< DecompressionSessionXPCServer >>>> %s: Output shows 0 MultiImage, at presentation time %1.3f, duration %1.3f"
+ "<<<< DecompressionSessionXPCServer >>>> %s: Received async message '%c%c%c%c'"
+ "<<<< DecompressionSessionXPCServer >>>> %s: Received message '%c%c%c%c' from connection: %p"
+ "<<<< DecompressionSessionXPCServer >>>> %s: Removed vtPerClientAudioSession %p from cache, PID: %d"
+ "<<<< DecompressionSessionXPCServer >>>> %s: Unknown NoReply opCode: 0x%0x"
+ "<<<< DecompressionSessionXPCServer >>>> %s: Unknown opCode: 0x%0x"
+ "<<<< DecompressionSessionXPCServer >>>> %s: Unsupported DecoderEmitsFramesFromConsistentThread"
+ "<<<< DecompressionSessionXPCServer >>>> %s: Unsupported MachThreadPriorityForThreadEmittingFrames"
+ "<<<< DecompressionSessionXPCServer >>>> %s: VTDecompressionSessionSetMultiImageCallback -> %d"
+ "<<<< DecompressionSessionXPCServer >>>> %s: VTDecompressionSessionXPC server starting."
+ "<<<< DecompressionSessionXPCServer >>>> %s: WARNING: client (%p): waited %016lld seconds for emit frame return."
+ "<<<< DecompressionSessionXPCServer >>>> %s: [%p] dispatch to asyncMessageHandlerQueue"
+ "<<<< DecompressionSessionXPCServer >>>> %s: [%p] finishDelayedFrames: send return message"
+ "<<<< DecompressionSessionXPCServer >>>> %s: [%p] finishDelayedTiles: send return message"
+ "<<<< DecompressionSessionXPCServer >>>> %s: [%p] tileRefCon %lld, infoFlags 0x%x, imageBuffer %p, cropOffset (%d, %d), cropDimensions %d x %d, offsetWithinImageBuffer (%d, %d)"
+ "<<<< DecompressionSessionXPCServer >>>> %s: called. [%p] sourceFrameRefcon: %lld, infoFlags: 0x%x, imageBuffer: %p, pst: %lld / %d, duration: %lld / %d"
+ "<<<< DecompressionSessionXPCServer >>>> %s: client (%p) got 'emit callback return' xpc message. singnal emitFrameReturnSemaphore"
+ "<<<< DecompressionSessionXPCServer >>>> %s: client (%p) signal emitFrameReturnSemaphore before invalidation"
+ "<<<< DecompressionSessionXPCServer >>>> %s: client (%p): emit frame EventLink message cancelled: err=%d"
+ "<<<< DecompressionSessionXPCServer >>>> %s: client (%p): emit frame EventLink message failed: err=%d. Fall back to XPC path"
+ "<<<< DecompressionSessionXPCServer >>>> %s: client (%p): semaphore wait done."
+ "<<<< DecompressionSessionXPCServer >>>> %s: client (%p): wait for emitFrameReturnSemaphore"
+ "<<<< DecompressionSessionXPCServer >>>> %s: client (objId = %lld) being notified of application state change to %u"
+ "<<<< DecompressionSessionXPCServer >>>> %s: client already ask to stop session, decompressionSession status callback should not be blocked"
+ "<<<< DecompressionSessionXPCServer >>>> %s: created decompression session:%p with err:%i"
+ "<<<< DecompressionSessionXPCServer >>>> %s: created tile decompression session:%p with err:%d"
+ "<<<< DecompressionSessionXPCServer >>>> %s: decoderEmitsFramesFromConsistentThread != true"
+ "<<<< DecompressionSessionXPCServer >>>> %s: decoderEmitsFramesFromConsistentThread: %@"
+ "<<<< DecompressionSessionXPCServer >>>> %s: decoderMachThreadPriority %d"
+ "<<<< DecompressionSessionXPCServer >>>> %s: decompression_session_xpc_max_emit_frame_event_links too large. Using %d"
+ "<<<< DecompressionSessionXPCServer >>>> %s: dispose client record due to err: %d"
+ "<<<< DecompressionSessionXPCServer >>>> %s: disposing refcon: %p"
+ "<<<< DecompressionSessionXPCServer >>>> %s: err %d"
+ "<<<< DecompressionSessionXPCServer >>>> %s: iClient: %p Encountered new thread %p. Created event link %d of %d"
+ "<<<< DecompressionSessionXPCServer >>>> %s: iClient: %p: Cannot create more event links. Will not use event link for thread %p"
+ "<<<< DecompressionSessionXPCServer >>>> %s: memory recipient copied: %p, err: %d"
+ "<<<< DecompressionSessionXPCServer >>>> %s: new client: %s"
+ "<<<< DecompressionSessionXPCServer >>>> %s: new tile decompression session client in server side. (client process: %s)"
+ "<<<< DecompressionSessionXPCServer >>>> %s: pixel buffer origin copied: %p, err: %d"
+ "<<<< DecompressionSessionXPCServer >>>> %s: pixelBufferOrigin created: %p, err: %d"
+ "<<<< DecompressionSessionXPCServer >>>> %s: pixelBufferOrigin objectID: %llu set to context: %p, err: %d"
+ "<<<< DecompressionSessionXPCServer >>>> %s: prefersEventLink == false"
+ "<<<< DecompressionSessionXPCServer >>>> %s: prefersEventLinkForApp == false AND clientRequestsEventLinkSupport == false"
+ "<<<< DecompressionSessionXPCServer >>>> %s: setting kVTDecompressionPropertyKey_ClientPID failed (err=%d)"
+ "<<<< DecompressionSessionXPCServer >>>> %s: taggedBufferGroup count = %ld, frameID = %d, status = %d"
+ "<<<< DecompressionSessionXPCServer >>>> %s: task (objId = %016llx) unexpected app state %u"
+ "<<<< DecompressionSessionXPCServer >>>> %s: task (objId = %lld) is NOT running foreground. Invalidating client: %p"
+ "<<<< DecompressionSessionXPCServer >>>> %s: task (objId = %lld) is running background"
+ "<<<< DecompressionSessionXPCServer >>>> %s: task (objId = %lld) is running foreground"
+ "<<<< DepthWrapperDecoder >>>>"
+ "<<<< DepthWrapperDecoder >>>> %s: (%p) WARNING: waited %d seconds but %d frames still pending"
+ "<<<< DepthWrapperDecoder >>>> %s: (%p) created"
+ "<<<< DepthWrapperEncoder >>>>"
+ "<<<< DepthWrapperEncoder >>>> %s: (%p)"
+ "<<<< DepthWrapperEncoder >>>> %s: (%p) Disregarding error %d from base encoder for property %@"
+ "<<<< DepthWrapperEncoder >>>> %s: (%p) WARNING: waited %d seconds but %d frames still pending"
+ "<<<< DepthWrapperEncoder >>>> %s: (%p) built depth/disparity format description: status %d, formatdesc %p"
+ "<<<< DepthWrapperEncoder >>>> %s: (%p) created"
+ "<<<< DepthWrapperEncoder >>>> %s: (%p) created depth sbuf %p (%d bytes) status %d overallStatus %d"
+ "<<<< DepthWrapperEncoder >>>> %s: (%p) emitting frame: status %d, infoflags %d, sbuf %p (%d bytes, dts %1.3f, pts %1.3f)"
+ "<<<< DepthWrapperEncoder >>>> %s: (%p) encoded base frame: status %d, infoflags %d, sbuf %p (%d bytes, dts %1.3f, pts %1.3f)"
+ "<<<< DepthWrapperEncoder >>>> %s: (%p) encoding frame %d pts %1.3f: pixelbuffer %p -> base pixelBuffer %p"
+ "<<<< DepthWrapperEncoder >>>> %s: (%p) untilPTS %1.3f"
+ "<<<< DepthWrapperEncoder >>>> %s: Property %@ is being set on %c%c%c%c encoder to %@"
+ "<<<< DepthWrapperEncoder >>>> %s: Property %@ is being set on base encoder to %@"
+ "<<<< DepthWrapperEncoder >>>> %s: Property %@ is being set on depth encoder to %@"
+ "<<<< DepthWrapperEncoder >>>> %s: Property %@ is being set on depth encoder to %@ (ignored)"
+ "<<<< DepthWrapperEncoder >>>> %s: created base compression session %p status %d"
+ "<<<< DolbyVision >>>>"
+ "<<<< DolbyVision >>>> %s: %x match to %x"
+ "<<<< DolbyVision >>>> %s: (%p) Attaching HDR10+ to pixelBuffer"
+ "<<<< DolbyVision >>>> %s: (%p) Attaching RPU to pixelBuffer"
+ "<<<< DolbyVision >>>> %s: (%p) RPU data was at end; skipping filler data in base layer"
+ "<<<< DolbyVision >>>> %s: (%p) WARNING: Unrecognized codecType, (%c%c%c%c)"
+ "<<<< DolbyVision >>>> %s: (%p) WARNING: waited %d seconds but %d frames still pending"
+ "<<<< DolbyVision >>>> %s: (%p) appended adjusted 4-byte length code + %d bytes at %d to dynamicReproductionMetadata (now %d bytes)"
+ "<<<< DolbyVision >>>> %s: (%p) appended adjusted 4-byte length code + %d bytes at %d to hdr10PlusMetadata (now %d bytes)"
+ "<<<< DolbyVision >>>> %s: (%p) bl_present_flag = %d"
+ "<<<< DolbyVision >>>> %s: (%p) bl_signal_compatibility_id = %d"
+ "<<<< DolbyVision >>>> %s: (%p) bl_signal_compatibility_id = %d extractRPU %d extractSEI_ITUT35 %d"
+ "<<<< DolbyVision >>>> %s: (%p) dv_level = %d"
+ "<<<< DolbyVision >>>> %s: (%p) dv_md_compression = %d"
+ "<<<< DolbyVision >>>> %s: (%p) dv_profile = %d"
+ "<<<< DolbyVision >>>> %s: (%p) dv_version_major = %d"
+ "<<<< DolbyVision >>>> %s: (%p) dv_version_minor = %d"
+ "<<<< DolbyVision >>>> %s: (%p) el_present_flag = %d"
+ "<<<< DolbyVision >>>> %s: (%p) naluType:%d appended %d bytes at %d to baseLayerBlockBuffer (now %d bytes)"
+ "<<<< DolbyVision >>>> %s: (%p) processing %d byte frame"
+ "<<<< DolbyVision >>>> %s: (%p) processing %d naluSize"
+ "<<<< DolbyVision >>>> %s: (%p) rpu_present_flag = %d"
+ "<<<< DolbyVision >>>> %s: (%p) subsampleAuxEntryCount %d; last bytesOfClearData %d, subtracting numBytesRemovedAtEnd %d"
+ "<<<< DolbyVision >>>> %s: Preferences overriding baseLayerDecoderOutputPixelFormat to (%c%c%c%c)"
+ "<<<< DolbyVision >>>> %s: adding interchange compressed format %c%c%c%c for DoVi"
+ "<<<< DolbyVision >>>> %s: kVTDecompressionPropertyKey_PropagatePerFrameHDRDisplayMetadata set to %s"
+ "<<<< DolbyVision >>>> %s: totalLength %zu, blockData %p"
+ "<<<< IOSurface Support >>>>"
+ "<<<< IOSurface Support >>>> %s: Failed to set custom scaling coefficients with error %d. Falling back to using default coefficients."
+ "<<<< IOSurface Support >>>> %s: IOSurfaceAcceleratorGetHistogram failed with %d, transfer succeeded but histogram isn't available"
+ "<<<< IOSurface Support >>>> %s: IOSurfaceAcceleratorTransformSurface %d %c%c%c%c [%f,%f,%f,%f,%zu,%zu] (%d,%d,%d) => %c%c%c%c [%d,%d,%d,%d,%zu,%zu] (%d,%d,%d)"
+ "<<<< IOSurface Support >>>> %s: could not find any display service"
+ "<<<< JPEG >>>>"
+ "<<<< MuxedAlphaDecoder >>>>"
+ "<<<< MuxedAlphaDecoder >>>> %s: (%p) WARNING: waited %d seconds but %d frames still pending"
+ "<<<< MuxedAlphaDecoder >>>> %s: Alpha Layer Bit Depth: %d (should be 8)"
+ "<<<< MuxedAlphaDecoder >>>> %s: Alpha Layer FullRangeVideo flag is %@ (should be 1)"
+ "<<<< MuxedAlphaDecoder >>>> %s: Color Layer FullRangeVideo flag is %@ (should be 0)"
+ "<<<< MuxedAlphaDecoder >>>> %s: Correcting Alpha layerID for poorly authored HEVC with Alpha"
+ "<<<< MuxedAlphaDecoder >>>> %s: Error(%d) in FigVideoFormatDescriptionDetermineCompatibilityWithCoreMediaRequirementsForHEVCWithAlpha()"
+ "<<<< MuxedAlphaDecoder >>>> %s: Property %@ is being set on muxa decoder to %@"
+ "<<<< MuxedAlphaDecoder >>>> %s: SelectPixelFormatWithAlpha CopyProperty retrieved %d"
+ "<<<< MuxedAlphaDecoder >>>> %s: Setting optimization properties for layer %d"
+ "<<<< MuxedAlphaDecoder >>>> %s: Unexpected pixel format %c%c%c%c selected for HEVC+alpha decode."
+ "<<<< MuxedAlphaDecoder >>>> %s: WriteDirectlyToPlanesOfTargetCVPixelBuffer CopyProperty retrieved %d for layer %d"
+ "<<<< MuxedAlphaDecoder >>>> %s: [%p] FigCPECryptorGetExternalProtectionMethods, err %d\n"
+ "<<<< MuxedAlphaDecoder >>>> %s: [%p] attempting alpha DRM decoding without buffer optimization -- not supported"
+ "<<<< MuxedAlphaDecoder >>>> %s: [%p] cannot get pixel buffer attr from decompression session"
+ "<<<< MuxedAlphaDecoder >>>> %s: copying color sub-decoder pixel buffer attrs: %@"
+ "<<<< MuxedAlphaDecoder >>>> %s: format descriptions compatible with triplanar decode optimization: %d"
+ "<<<< MuxedAlphaDecoder >>>> %s: pixel formats - color sub-decoder selected: %c%c%c%c | requested alpha sub-decoder output: %c%c%c%c | muxed triplanar output: %c%c%c%c"
+ "<<<< MuxedAlphaDecoder >>>> %s: re-set PixelBufferAttributes : %@"
+ "<<<< MuxedAlphaEncoder >>>>"
+ "<<<< MuxedAlphaEncoder >>>> %s: (%p)"
+ "<<<< MuxedAlphaEncoder >>>> %s: (%p) Disregarding error %d from base encoder for property %@"
+ "<<<< MuxedAlphaEncoder >>>> %s: (%p) WARNING: waited %d seconds but %d frames still pending"
+ "<<<< MuxedAlphaEncoder >>>> %s: (%p) built muxed alpha format description: status %d, formatdesc %p"
+ "<<<< MuxedAlphaEncoder >>>> %s: (%p) check poc_lsb_not_present_flag for muxed alpha format description : status %d, formatdesc %p"
+ "<<<< MuxedAlphaEncoder >>>> %s: (%p) created"
+ "<<<< MuxedAlphaEncoder >>>> %s: (%p) created muxed sbuf %p (%d bytes) status %d mergedStatus %d"
+ "<<<< MuxedAlphaEncoder >>>> %s: (%p) dimensions %d x %d; created base compression session %p, alpha compression session %p, status %d"
+ "<<<< MuxedAlphaEncoder >>>> %s: (%p) emitting muxed frame: status %d, infoflags %d, sbuf %p (%d bytes, dts %1.3f, pts %1.3f)"
+ "<<<< MuxedAlphaEncoder >>>> %s: (%p) encoded alpha frame: status %d, infoflags %d, sbuf %p (%d bytes, dts %1.3f, pts %1.3f)"
+ "<<<< MuxedAlphaEncoder >>>> %s: (%p) encoded base frame: status %d, infoflags %d, sbuf %p (%d bytes, dts %1.3f, pts %1.3f)"
+ "<<<< MuxedAlphaEncoder >>>> %s: (%p) encoding frame %d pts %1.3f: muxed pixelbuffer %p -> base pixelBuffer %p, alpha pixelBuffer %p"
+ "<<<< MuxedAlphaEncoder >>>> %s: (%p) encoding frame %d pts %1.3f: muxed taggedBufferGroup %p -> base taggedBufferGroup %p, alpha taggedBufferGroup %p"
+ "<<<< MuxedAlphaEncoder >>>> %s: (%p) pts %1.3f"
+ "<<<< MuxedAlphaEncoder >>>> %s: (%p) untilPTS %1.3f"
+ "<<<< MuxedAlphaEncoder >>>> %s: AlphaChannelMode not set by client or frame-encode -- returning NULL"
+ "<<<< MuxedAlphaEncoder >>>> %s: Color videoLayerIDs=%d,%d Alpha videoLayerIDs=%d,%d"
+ "<<<< MuxedAlphaEncoder >>>> %s: Invalid alpha profile %@"
+ "<<<< MuxedAlphaEncoder >>>> %s: Mismatch between pixel buffer's alpha channel mode: %@, and session's current alpha channel mode: %s"
+ "<<<< MuxedAlphaEncoder >>>> %s: Property %@ is a bit-rate property and is set on base encoder and NOT on alpha encoder to %@. Alpha encoder works on fixed QP"
+ "<<<< MuxedAlphaEncoder >>>> %s: Property %@ is being set on alpha encoder to %@"
+ "<<<< MuxedAlphaEncoder >>>> %s: Property %@ is being set on both base and alpha encoders to %@"
+ "<<<< MuxedAlphaEncoder >>>> %s: Property %@ is being set on muxa encoder to %@"
+ "<<<< MuxedAlphaEncoder >>>> %s: Property %@ is being set to %@ on muxa encoder (this may not change sub-encoder profiles)"
+ "<<<< MuxedAlphaEncoder >>>> %s: Setting profile %@ on alpha encoder"
+ "<<<< MuxedAlphaEncoder >>>> %s: Setting profile %@ on color encoder"
+ "<<<< MuxedAlphaEncoder >>>> %s: Setting rep_format info (bit_depth_vps_luma&chroma_minus8, chroma_format_vps_idc)) on color encoder and sps_rep_format_idx on alpha encoder"
+ "<<<< MuxedAlphaEncoder >>>> %s: WARNING: %d keys in dictionary were ignored -- original dictionary is %@"
+ "<<<< MuxedAlphaEncoder >>>> %s: client changed value for alpha channel mode: %@ after a frame was already encoded. Session's current alpha channel mode: %s"
+ "<<<< MuxedAlphaEncoder >>>> %s: unrecognized AlphaChannelMode attachment %@ on CVPixelBuffer %p"
+ "<<<< ParavirtualizedHostJPEGSupport >>>> %s: Calling CMPhoto to decode image"
+ "<<<< ParavirtualizedHostJPEGSupport >>>> %s: Calling CMPhoto to encode image"
+ "<<<< ParavirtualizedHostJPEGSupport >>>> %s: Calling CMPhoto to get HW capabilities"
+ "<<<< ParavirtualizedHostJPEGSupport >>>> %s: Encode successful with size %d"
+ "<<<< ParavirtualizedHostJPEGSupport >>>> %s: Extracted operation options %@"
+ "<<<< ParavirtualizedHostJPEGSupport >>>> %s: Got capabilities %@"
+ "<<<< ParavirtualizedHostJPEGSupport >>>> %s: Relinquishing %zd surfaces"
+ "<<<< ParavirtualizedHostJPEGSupport >>>> %s: called with message %d"
+ "<<<< ParavirtualizedHostJPEGSupport >>>> %s: operationErr: %d"
+ "<<<< ParavirtualizedJPEGSession >>>>"
+ "<<<< ParavirtualizedJPEGSession >>>> %s: Decode <%p %zd> <%p %zdx%zd> %@"
+ "<<<< ParavirtualizedJPEGSession >>>> %s: Encode <%p %zdx%zd> <%p %zd> %@"
+ "<<<< ParavirtualizedJPEGSession >>>> %s: HW capabilities: %@"
+ "<<<< ParavirtualizedJPEGSession >>>> %s: called"
+ "<<<< ParavirtualizedMotionEstimationProcessor >>>>"
+ "<<<< ParavirtualizedMotionEstimationProcessor >>>> %s:  %d x %d -> %d"
+ "<<<< ParavirtualizedMotionEstimationProcessor >>>> %s: %d UUIDs"
+ "<<<< ParavirtualizedMotionEstimationProcessor >>>> %s: %p %c%c%c%c (%zd bytes)"
+ "<<<< ParavirtualizedMotionEstimationProcessor >>>> %s: (processor %{public}@) ProcessFrames failed with error %d, requestID %lu referenceFrame %p currentFrame %p motionEstimationFrameFlags %u additionalFrameOptions %@"
+ "<<<< ParavirtualizedMotionEstimationProcessor >>>> %s: -> %d"
+ "<<<< ParavirtualizedMotionEstimationProcessor >>>> %s: GuestRemoveHandlerForUUID failed with error %d"
+ "<<<< ParavirtualizedMotionEstimationProcessor >>>> %s: Not implemented yet..."
+ "<<<< ParavirtualizedMotionEstimationProcessor >>>> %s: Sending the message '-mep' failed with error %d"
+ "<<<< ParavirtualizedMotionEstimationProcessor >>>> %s: error %d in setting properties %@"
+ "<<<< ParavirtualizedMotionEstimationProcessor >>>> %s: error %d in setting property %@ with value %@"
+ "<<<< ParavirtualizedMotionEstimationProcessor >>>> %s: guest UUID %{private}@, guestProtocolVersion %u hostProtocolVersion %u hostInfo %{public}@, guestBuildVersion %{public}@"
+ "<<<< ParavirtualizedMotionEstimationProcessor >>>> %s: pixelBufferUUID %@ pixelBuffer %@"
+ "<<<< ParavirtualizedMotionEstimationProcessor >>>> %s: requestID %lu referenceFrame %p currentFrame %p motionEstimationFrameFlags %u additionalFrameOptions %@"
+ "<<<< ParavirtualizedMotionEstimationProcessor >>>> %s: requestID %lu: status %d infoFlags 0x%x additionalInfo %@ -> %d"
+ "<<<< ParavirtualizedMotionEstimationProcessor >>>> %s: unhandled message %c%c%c%c"
+ "<<<< ParavirtualizedMotionEstimationProcessor >>>> %s: warning: inputAndOutputPixelBuffers now has %d buffers"
+ "<<<< ParavirtualizedVideoDecoder >>>>"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: %c%c%c%c %d x %d -> %d"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: %d UUIDs"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: %p %c%c%c%c (%zd bytes)"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: (decoder %p) CopySupportedPropertyDictionary with error %d"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: (decoder %p) FinishDelayedFrames failed with error %d"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: (decoder %p) FinishDelayedTiles failed with error %d"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: (decoder %p) StartTileSession failed with error %d for codecType '%c%c%c%c' %d x %d"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: (decoder %p) VTDecoderSessionCreatePixelBufferWithOptions failed with err %d for frame %d options %{public}@"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: (decoder %p) VTDecoderSessionEmitDecodedFrame failed with error %d, frame %d, status %d, infoFlags 0x%x, pixelBuffer %p"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: (decoder %p) VTDecoderSessionEmitDecodedMultiImageFrame failed with error %d for frame %d: status %d decodeFlags 0x%x taggedBufferGroup %{public}@"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: (decoder %p) VTDecoderSessionGetDestinationPixelBufferAttributes failed with error %d"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: (decoder %p) VTDecoderSessionSetPixelBufferAttributes failed with error %d for %{public}@"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: (decoder %p) VTTileDecoderSessionEmitDecodedTile failed with error %d for tile %p: status %d decodeFlags 0x%x pixelBuffer %p"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: (decoder %p) VTTileDecoderSessionSetTileDecodeRequirements failed with error %d for canvasPixelBufferAttributes=%{public}@ tileDecodeRequirementsDesc=%{public}@"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: (decoder %p) VTVideoDecoderStartSession failed for %d x %d with error %d"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: (decoder %p) guest UUID %{private}@ codecType %c%c%c%c, decoderID %{private}@ -> %d, guestProtocolVersion %u hostProtocolVersion %u hostInfo %{public}@, guestBuildVersion %{public}@"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: (decoder %{public}@ decoderSession %p decompressionSession %{public}@ ) DecodeFrame failed with error %d, frame %d: sbuf PTS %1.3f, %zd bytes, decodeFlags 0x%x, frameOptions %{public}@"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: -> err %d"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: At decode tile %lld, pendingTilePixelBuffers %@"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: No tiles are using pixel buffer with UUID %@. Why wasn't the entry for tile %lld removed from pendingTilePixelBuffers?"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: Unrecognized pixelBufferUUID %@"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: at emit tile %lld, pendingTilePixelBuffers %@"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: codecType is %c%c%c%c, calling FigCPECryptorCreateProcessedBlockBufferAndSubsampleAuxiliaryDataWithOptions on the guest"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: decoder %p"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: decoder %p -> %d"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: decoder %p, CopyProperty failed with error %d for %{public}@"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: decoder %p, CopySerializableProperties failed with error %d"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: decoder %p, error %d in setting properties %{public}@"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: decoder %p, error %d in setting property %{public}@ with value %{public}@"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: destinationPixelBufferAttributes %@"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: failed to get the number of sample timing entries\n"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: failed to get timingArray"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: frame %d: sbuf PTS %1.3f, %zd bytes, decodeFlags 0x%x, frameOptions %@"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: frame %d: status %d decodeFlags 0x%x pixelBuffer %p -> %d"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: frame %d: status %d decodeFlags 0x%x taggedBufferGroup %@ -> %d"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: frameOptions is unsupported and dropped because hostProtocolVersion is < kVTParavirtualizationProtocolVersion_Fall2024"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: numSamples is %d instead of 1"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: pixelBufferUUID %@ pixelBuffer %@"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: pixelBufferUUIDArray %@ pixelBufferArray %@"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: tile %p: sbuf PTS %1.3f, %zd bytes, tileCropOffset [%d, %d], tileCropDimensions %d x %d, pixelBuffer %p, offsetWithinPixelBuffer [%d, %d] decodeFlags 0x%x"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: tile %p: status %d decodeFlags 0x%x pixelBuffer %p -> %d"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: warning: pendingFramePixelBuffers now has %d buffers"
+ "<<<< ParavirtualizedVideoDecoder >>>> %s: warning: pendingTilePixelBuffers now has %d buffers"
+ "<<<< ParavirtualizedVideoEncoder >>>>"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: %c%c%c%c (%zd bytes)"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: %d x %d -> %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) -> %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) BeginPass failed for beginPassFlags %u with error %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) BeginPass failed for furtherPassesRequested %d with error %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) CompleteFrames failed with error %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) CompleteTiles failed with error %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) CopySupportedPropertyDictionary failed with error %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) EmitEncodedTiled failed for tile %lld pixelBufferUUID %@ status %d encodeFlags 0x%x sampleBuffer %@ with error %d "
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) EncodeMultiImageFrame failed with error %d for frame %p: taggedBufferGroup %@ PTS %1.3f duration %1.3f frameProperties %@"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) GuestRemoveHandlerForUUID failed with error %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) PrepareToEncodeFrames failed with error %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) PrepareToEncodeTiles failed with error %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) Sending the message '-enc' failed with error %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) StartSession failed for %d x %d with error %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) StartTileSession failed with error %d for %d x %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) VTEncoderSessionSetTimeRangesForNextPass failed for timeRangeCount %d with error %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) VTMultiPassStorageCopyDataAtTimeStamp failed for timeStamp %1.3f index %d with error %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) VTMultiPassStorageCopyIdentifier failed with error %d, identifier %{public}@"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) VTMultiPassStorageGetTimeStamp failed for fromTimeStamp %1.3f MultipassStep %@ timeStamp %1.3f with error %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) VTMultiPassStorageGetTimeStampAndDuration failed for fromTimeStamp %1.3f MultipassStep %@ timeStamp %1.3f duration %1.3f with error %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) VTMultiPassStorageInvalidate failed with error %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) VTMultiPassStorageSetDataAtTimeStamp failed for timeStamp %1.3f index %d with error %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) VTMultiPassStorageSetIdentifier failed for videoEncoderIdentifierAndVersion %{public}@ with error %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) VTTileEncoderSessionCreateVideoFormatDescription failed with error %d for '%c%c%c%c', %d x %d %{public}@"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) VTTileEncoderSessionSetTileAttributes failed with error %d for %d x %d, %{public}@"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) VTTileEncoderSessionSetTileEncodeRequirements failed with error %d, %{public}@, %{public}@"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p) error %d in setting property %{public}@ with value %{public}@"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p, encoderSession %p) VTEncoderSessionCreateVideoFormatDescription failed with error %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p, encoderSession %p) VTEncoderSessionEmitEncodedFrame failed with error %d, frame %d: sbuf PTS %1.3f, %zd bytes, status %d encodeFlags 0x%x"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %p, encoderSession %p) VTEncoderSessionSetPixelBufferAttributes failed with error %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %{public}@, encoderSession %p, compressionSession %{public}@) EncodeFrame failed with error %d, frame %d: pixelBuffer %p PTS %1.3f duration %1.3f frameProperties %{public}@"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: At encode tile %lld, pendingTilePixelBuffers %@"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: Called to emit encoded tile %lld pixelBufferUUID %@ status %d encodeFlags 0x%x sampleBuffer %@ -> %d "
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: Called to encode tile %lld pixelBuffer %p pixelBufferUUID %@ tileOffset (%d, %d) tileAperture %d x %d tileProperties %@ encodeFlags 0x%x -> %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: Tile %lld pixelBufferUUID %@ encodeTileDidComplete %d tileWasEmitted %d tilesDict %@"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: encoder %p"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: encoder %p -> %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: encoder %p beginPassFlags %u -> %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: encoder %p fromTimeStamp %1.3f MultipassStep %@ timeStamp %1.3f -> %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: encoder %p fromTimeStamp %1.3f MultipassStep %@ timeStamp %1.3f duration %1.3f -> %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: encoder %p furtherPassesRequested %d -> err %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: encoder %p identifier %@"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: encoder %p timeRangeCount %d -> %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: encoder %p timeStamp %1.3f index %d -> %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: encoder %p videoEncoderIdentifierAndVersion %@ -> %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: frame %p: pixelBuffer %p PTS %1.3f duration %1.3f frameProperties %@"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: frame %p: sbuf PTS %1.3f, %zd bytes, status %d encodeFlags 0x%x -> %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: frame %p: taggedBufferGroup %@ PTS %1.3f duration %1.3f frameProperties %@"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: guest UUID %{private}@, codecType %c%c%c%c, encoderID %{private}@ -> %d, guestProtocolVersion %u hostProtocolVersion %u hostInfo %{public}@, guestBuildVersion %{public}@"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: pixelBuffer is NULL for bufferIndex %d"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: pixelBufferUUID %@ pixelBufferDict %@"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: warning: pendingFramePixelBuffers now has %d buffers"
+ "<<<< ParavirtualizedVideoEncoder >>>> %s: warning: pendingTilePixelBuffers now has %d buffers"
+ "<<<< SRSEnhancementTemporalFilter >>>>"
+ "<<<< SRSEnhancementTemporalFilter >>>> %s: "
+ "<<<< SRSEnhancementTemporalFilter >>>> %s: Created filter: %p"
+ "<<<< SRSEnhancementTemporalFilter >>>> %s: IOSurfaceAcceleratorTransformSurface returned %p  (PTS %1.3f) "
+ "<<<< SRSEnhancementTemporalFilter >>>> %s: VTTemporalFilterPluginSessionEmitOutputFrame failed"
+ "<<<< SRSEnhancementTemporalFilter >>>> %s: building intermedia pool: %@"
+ "<<<< SRSEnhancementTemporalFilter >>>> %s: calculated dimensions: source%dx%d rawOutput:%dx%d  Output:%dx%d (width scale: %1.3f height scale: %1.3f)"
+ "<<<< SRSEnhancementTemporalFilter >>>> %s: configuring scaling from [%dx%d] to [%dx%d]  (raw output dimensions: %dx%d) "
+ "<<<< SRSEnhancementTemporalFilter >>>> %s: input buffer %p  (PTS %1.3f) "
+ "<<<< SRSEnhancementTemporalFilter >>>> %s: perform secondary scaling (PTS %1.3f) "
+ "<<<< SRSEnhancementTemporalFilter >>>> %s: received kVTTemporalFilterPropertyKey_FilterParameters override for 'StaticWeak' usage"
+ "<<<< SRSEnhancementTemporalFilter >>>> %s: received kVTTemporalFilterPropertyKey_FilterParameters override for 'Weak' usage"
+ "<<<< SRSEnhancementTemporalFilter >>>> %s: running scaler: [source: %p] [SRS: %p -> %p] [MSR: %p -> %p] [secondary scaling: %s] [skip SRS: %s] "
+ "<<<< SRSEnhancementTemporalFilter >>>> %s: sending destination pixelBufferAttributes: %@"
+ "<<<< SRSEnhancementTemporalFilter >>>> %s: setting override pixel format to %c%c%c%c ( from string %@ )"
+ "<<<< SRSEnhancementTemporalFilter >>>> %s: skip SRS for frame  (PTS %1.3f) "
+ "<<<< TestIPBVideoEncoder >>>>"
+ "<<<< TestIPBVideoEncoder >>>> %s: Emitting %s%s (display #%s PTS %1.3f), dependency: %s"
+ "<<<< VT-CS >>>>"
+ "<<<< VT-CS >>>> %s: %p"
+ "<<<< VT-CS >>>> %s: Configuration exceeds all Dolby levels - default to highest level"
+ "<<<< VT-CS >>>> %s: Created new dummy attributes %p"
+ "<<<< VT-CS >>>> %s: Discarding unsupported property key %@"
+ "<<<< VT-CS >>>> %s: EncoderType: Hardware"
+ "<<<< VT-CS >>>> %s: EncoderType: Software"
+ "<<<< VT-CS >>>> %s: EncoderType: Unknown"
+ "<<<< VT-CS >>>> %s: FigTaggedBufferGroupCreate(count %d) -> %p, err %d"
+ "<<<< VT-CS >>>> %s: HDR metadata insertion %s -- thank you for setting \"defaults write com.apple.coremedia hdrenabled\""
+ "<<<< VT-CS >>>> %s: HDR metadata stat generation %s -- thank you for setting \"defaults write com.apple.coremedia hdralwaysgeneratestats\""
+ "<<<< VT-CS >>>> %s: Need to build dummy attributes for the first time"
+ "<<<< VT-CS >>>> %s: Need to rebuild dummy attributes"
+ "<<<< VT-CS >>>> %s: PIPELINED: Color Sync"
+ "<<<< VT-CS >>>> %s: PIPELINED: Pixel Transfer Session"
+ "<<<< VT-CS >>>> %s: RateControl Session handled SetProperty for %@ (err %d)"
+ "<<<< VT-CS >>>> %s: Undefined codecProfileLevel - default to highest level"
+ "<<<< VT-CS >>>> %s: VTVideoEncoderStartSession failed - err: %d"
+ "<<<< VT-CS >>>> %s: [%p]"
+ "<<<< VT-CS >>>> %s: [%p] %@ %@"
+ "<<<< VT-CS >>>> %s: [%p] %@ setting failed with err = %d"
+ "<<<< VT-CS >>>> %s: [%p] 'AllowClientProcessEncode' in compressionSessionOptions is: %@"
+ "<<<< VT-CS >>>> %s: [%p] Calling video encoder for imageBuffer: %p/%p context: %p (%lld/%d)"
+ "<<<< VT-CS >>>> %s: [%p] HDR stats:  [%@]"
+ "<<<< VT-CS >>>> %s: [%p] HDR stats:  minPQ = %f, maxPQ = %f, avgPQ = %f standardDeviation = %f\n"
+ "<<<< VT-CS >>>> %s: [%p] HDR10Plus [dynamicHDR10PlusData %@]"
+ "<<<< VT-CS >>>> %s: [%p] InputQueueMaxCount %d"
+ "<<<< VT-CS >>>> %s: [%p] Output frame for sourceFrameRefCon: %p frame: %p sampleBuffer: %p status: %d"
+ "<<<< VT-CS >>>> %s: [%p] Unsupported DolbyVision Profile %d"
+ "<<<< VT-CS >>>> %s: [%p] Unsupported DolbyVision profile %d"
+ "<<<< VT-CS >>>> %s: [%p] Unsupported property key %@ (it's not in the SupportedPropertyDictionary)"
+ "<<<< VT-CS >>>> %s: [%p] VideoEncoder: %@ %@"
+ "<<<< VT-CS >>>> %s: [%p] [dynamicHDRDolbyData %@] Using fake data"
+ "<<<< VT-CS >>>> %s: [%p] [hdrStats %@][dynamicHDRData %@]"
+ "<<<< VT-CS >>>> %s: [%p] dolbyVisionProfile %d"
+ "<<<< VT-CS >>>> %s: [%p] frameProperties [%@]"
+ "<<<< VT-CS >>>> %s: [%p] imageBuffer: %p context: %p (%lld/%d)"
+ "<<<< VT-CS >>>> %s: [%p] imageBuffer: %p/%p context: %p (%lld/%d)"
+ "<<<< VT-CS >>>> %s: [%p] kVTCompressionPropertyKey_HDRMetadataInsertionMode %@"
+ "<<<< VT-CS >>>> %s: [%p] kVTCompressionPropertyKey_PreserveDynamicHDRMetadata %@"
+ "<<<< VT-CS >>>> %s: [%p] retaining hdrPaddingNALU"
+ "<<<< VT-CS >>>> %s: [%p] sourceFrameRefCon: %p frame: %p imageBuffer: %p/%p context: %p"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided ambientViewingEnvironmentData for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided auxiliaryTypeInfo for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided baselineValue for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided cameraCalibrationDataLensCollection for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided cleanAperture for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided colorPrimaries for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided contentLightLevelInfo for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided disparityAdjustment for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided fieldCount for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided fieldDetail for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided gammaLevel for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided hasAdditionalViews for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided hasEyeViewsReversed for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided hasLeftStereoEyeView for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided hasRightStereoEyeView for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided heroEye for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided horizontalFieldOfView for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided iccProfile for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided logFormatIdentifier for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided masteringDisplayColorVolume for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided pixelAspectRatio for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided projectionKind for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided transferFunction for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided transportIdentifier for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided viewPackingKind for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided warpKind for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder provided ycbcrMatrix for format description"
+ "<<<< VT-CS >>>> %s: [%p] video encoder returned (err %d) kVTCompressionPropertyKey_AmbientViewingEnvironment"
+ "<<<< VT-CS >>>> %s: [%p] video encoder returned (err %d) kVTCompressionPropertyKey_InsertTrailingBytes"
+ "<<<< VT-CS >>>> %s: [%p] video encoder says it doesn't support kVTCompressionPropertyKey_InsertTrailingBytes"
+ "<<<< VT-CS >>>> %s: [%p] video encoder says it supports kVTCompressionPropertyKey_AmbientViewingEnvironment"
+ "<<<< VT-CS >>>> %s: [%p] video encoder says it supports kVTCompressionPropertyKey_InsertTrailingBytes"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing ambientViewingEnvironmentData for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing auxiliaryTypeInfo for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing baselineValue for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing cameraCalibrationDataLensCollection for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing cleanAperture for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing colorPrimaries for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing contentLightLevelInfo for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing disparityAdjustment for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing fieldCount for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing fieldDetail for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing gammaLevel for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing hasAdditionalViews for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing hasEyeViewsReversed for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing hasLeftStereoEyeView for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing hasRightStereoEyeView for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing heroEye for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing horizontalFieldOfView for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing iccProfile for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing logFormatIdentifier for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing masteringDisplayColorVolume for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing pixelAspectRatio for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing projectionKind for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing transferFunction for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing transportIdentifier for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing viewPackingKind for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing warpKind for format description"
+ "<<<< VT-CS >>>> %s: [%p] video toolbox providing ycbcrMatrix for format description"
+ "<<<< VT-CS >>>> %s: [%p][hdrFormat %d]"
+ "<<<< VT-CS >>>> %s: [session: %p] frame %p was already emitted, returning early (status %d)"
+ "<<<< VT-CS >>>> %s: [session: %p] localCodecType is %d, not supported for Dolby Vision 5"
+ "<<<< VT-CS >>>> %s: [session: %p]: create compression session for %s-process encoding: codec %c%c%c%c"
+ "<<<< VT-CS >>>> %s: appending %1.3f"
+ "<<<< VT-CS >>>> %s: copied ambientViewingEnvironmentData from video encoder"
+ "<<<< VT-CS >>>> %s: copied cleanAperture from video encoder"
+ "<<<< VT-CS >>>> %s: copied colorPrimaries %@ from video encoder"
+ "<<<< VT-CS >>>> %s: copied contentLightLevelInfo from video encoder"
+ "<<<< VT-CS >>>> %s: copied fieldCount from video encoder"
+ "<<<< VT-CS >>>> %s: copied fieldDetail from video encoder"
+ "<<<< VT-CS >>>> %s: copied gammaLevel %@ from video encoder"
+ "<<<< VT-CS >>>> %s: copied iccProfile %@ from video encoder"
+ "<<<< VT-CS >>>> %s: copied masteringDisplayColorVolume from video encoder"
+ "<<<< VT-CS >>>> %s: copied pixelAspectRatio from video encoder"
+ "<<<< VT-CS >>>> %s: copied transferFunction %@ from video encoder"
+ "<<<< VT-CS >>>> %s: copied ycbcrMatrix %@ from video encoder"
+ "<<<< VT-CS >>>> %s: creating ambient viewing environment default"
+ "<<<< VT-CS >>>> %s: current pts %f - previous %f = %f"
+ "<<<< VT-CS >>>> %s: enable ambient viewing environment %s -- thank you for setting \"defaults write com.apple.coremedia enableambientve\""
+ "<<<< VT-CS >>>> %s: encoderSession [%p] ownerSession [%p]"
+ "<<<< VT-CS >>>> %s: generateDM4 %s -- thank you for setting \"defaults write com.apple.coremedia generateDM4\""
+ "<<<< VT-CS >>>> %s: generateDM4 set to %d"
+ "<<<< VT-CS >>>> %s: hdr10PlusExtractionEnabled %s -- thank you for setting \"defaults write com.apple.coremedia hdr10PlusExtractionEnabled\""
+ "<<<< VT-CS >>>> %s: image buffer ambientData %@"
+ "<<<< VT-CS >>>> %s: invalid argument configuration %p %p"
+ "<<<< VT-CS >>>> %s: kCVImageBufferHDRImageStatisticsInfoFilteredKey %@"
+ "<<<< VT-CS >>>> %s: kCVImageBufferHDRImageStatisticsInfoRawKey %@"
+ "<<<< VT-CS >>>> %s: kVTHDRImageStatisticsInfo_Filtered %@"
+ "<<<< VT-CS >>>> %s: levelIdx %ld"
+ "<<<< VT-CS >>>> %s: neither outputCallback nor outputHandler!"
+ "<<<< VT-CS >>>> %s: new AmbientViewingEnvironment %@ (err %d)"
+ "<<<< VT-CS >>>> %s: pixelBuffer %p at index %d of taggedBufferGroup %@"
+ "<<<< VT-CS >>>> %s: returning %1.3f"
+ "<<<< VT-CS >>>> %s: scaling mode %@, cleanAperture mismatch => pixelBuffer not compatible"
+ "<<<< VT-CS >>>> %s: scaling mode %@, pixelAspectRatio mismatch => pixelBuffer not compatible"
+ "<<<< VT-CS >>>> %s: sdrPreservationEnabled %s -- thank you for setting \"defaults write com.apple.coremedia sdrPreservationEnabled\""
+ "<<<< VT-CS >>>> %s: session->codecProfileLevel [%@]"
+ "<<<< VT-CS >>>> %s: session[%p, colorPrimaries %@ transferFunction %@ ycbcrMatrix %@]"
+ "<<<< VT-CS >>>> %s: setting generateAmbientViewingEnvironment to true"
+ "<<<< VT-CS >>>> %s: setting previous pts %f"
+ "<<<< VT-CS >>>> %s: total pending frames = %d, in encoder = %d"
+ "<<<< VT-CS >>>> %s: using duration of %f"
+ "<<<< VT-CS >>>> %s: using pts of %f previous is %f"
+ "<<<< VT-CS >>>> %s: video encoder handled CopyProperty for %@ (err %d)"
+ "<<<< VT-CS >>>> %s: video encoder handled SetProperty for %@ (err %d)"
+ "<<<< VT-CS >>>> %s: video encoder handled SetProperty synthesized for FigThreadPriority for RealTime (err %d)"
+ "<<<< VT-CS >>>> %s: video encoder handled kVTCompressionPropertyKey_AmbientViewingEnvironment %@ (err %d)"
+ "<<<< VT-CS >>>> %s: video encoder returned NULL colorPrimaries, expected %@"
+ "<<<< VT-CS >>>> %s: video encoder returned NULL gammaLevel, expected %@"
+ "<<<< VT-CS >>>> %s: video encoder returned NULL iccProfile, expected %@"
+ "<<<< VT-CS >>>> %s: video encoder returned NULL transferFunction, expected %@"
+ "<<<< VT-CS >>>> %s: video encoder returned NULL ycbcrMatrix, expected %@"
+ "<<<< VT-CS >>>> %s: video toolbox handled CopyProperty for %@"
+ "<<<< VT-CS >>>> %s: video toolbox handled SetProperty for %@"
+ "<<<< VT-CS >>>> %s: videoEncoderSpecification: %@"
+ "<<<< VT-CS >>>> %s: vtCompressionSessionColorSyncWork %d"
+ "<<<< VT-CS >>>> %s: vtCompressionSessionEncodeWork %d"
+ "<<<< VT-CS >>>> %s: vtCompressionSessionIOSurfaceSynchronizationWork %d"
+ "<<<< VT-CS >>>> %s: vtCompressionSessionPixelTransferSessionWork %d"
+ "<<<< VT-CS >>>> %s: warning: low-latency rate control not supported for multi-image encoding"
+ "<<<< VT-CS >>>> %s: width: %d height: %d codec: %c%c%c%c"
+ "<<<< VT-DS >>>>"
+ "<<<< VT-DS >>>> %s: %p"
+ "<<<< VT-DS >>>> %s: %p hdr10PlusEnabled is %s"
+ "<<<< VT-DS >>>> %s: (%p) changing format description from %p to %p"
+ "<<<< VT-DS >>>> %s: (%p) frame %p still pending after failed DecodeFrame call"
+ "<<<< VT-DS >>>> %s: (%p) frame %p still pending after synchronous immediate DecodeFrame call"
+ "<<<< VT-DS >>>> %s: Celestial: default asyncpixeltransfer = <%s>"
+ "<<<< VT-DS >>>> %s: DecoderType: Hardware"
+ "<<<< VT-DS >>>> %s: DecoderType: Software"
+ "<<<< VT-DS >>>> %s: DecoderType: Unknown"
+ "<<<< VT-DS >>>> %s: Discarding unsupported property key %@"
+ "<<<< VT-DS >>>> %s: DolbyVision 8.1"
+ "<<<< VT-DS >>>> %s: DolbyVision 8.4"
+ "<<<< VT-DS >>>> %s: GEN: HLG generating"
+ "<<<< VT-DS >>>> %s: GEN: attaching"
+ "<<<< VT-DS >>>> %s: GEN: average %f, minimum %f, maximum %f, standardDeviation %f"
+ "<<<< VT-DS >>>> %s: GEN: dolby found, not generating"
+ "<<<< VT-DS >>>> %s: GEN: generatePerFrameHDRDisplayMetadata == false"
+ "<<<< VT-DS >>>> %s: GEN: generating"
+ "<<<< VT-DS >>>> %s: GEN: it's %s"
+ "<<<< VT-DS >>>> %s: GEN: turning off"
+ "<<<< VT-DS >>>> %s: GEN: turning on"
+ "<<<< VT-DS >>>> %s: HDR (AV1): Routing to Wrapper Decoder %c%c%c%c"
+ "<<<< VT-DS >>>> %s: HDR(AV1): subLayerCodec Not in list %c%c%c%c"
+ "<<<< VT-DS >>>> %s: HDR10(+)"
+ "<<<< VT-DS >>>> %s: HDR: Routing to Wrapper Decoder %c%c%c%c"
+ "<<<< VT-DS >>>> %s: HDR: subLayerCodec Not in list %c%c%c%c"
+ "<<<< VT-DS >>>> %s: HDR: thank you for setting \"defaults write com.apple.coremedia vt_addDolbyOverride %d\""
+ "<<<< VT-DS >>>> %s: Hardware decode %s supported for codec: %c%c%c%c"
+ "<<<< VT-DS >>>> %s: NULL decoder session"
+ "<<<< VT-DS >>>> %s: OnlyTheseFrames ReducedFrameDelivery: %@"
+ "<<<< VT-DS >>>> %s: QualityOfService ReducedFrameDelivery: %@"
+ "<<<< VT-DS >>>> %s: QualityOfService TemporalLevelLimit: %@"
+ "<<<< VT-DS >>>> %s: Registering custom pixel format: %c%c%c%c"
+ "<<<< VT-DS >>>> %s: Session was invalidated"
+ "<<<< VT-DS >>>> %s: Set kVTDecompressionPropertyKey_AllowBitstreamToChangeFrameDimensions=false for <%p> status: %d"
+ "<<<< VT-DS >>>> %s: TransferFunction is %@"
+ "<<<< VT-DS >>>> %s: Unknown YCbCrMatrix; not guessing other missing color parameters"
+ "<<<< VT-DS >>>> %s: Unknown color primaries; not guessing other missing color parameters"
+ "<<<< VT-DS >>>> %s: Unknown transfer function; not guessing other missing color parameters"
+ "<<<< VT-DS >>>> %s: Unsupported property key %@ (it's not in the SupportedPropertyDictionary)"
+ "<<<< VT-DS >>>> %s: VTDS_PixelBufferCache Frame: %p [ id: %@ ] pixelBuffer [ %p ] created and added to cache (size = %ld)"
+ "<<<< VT-DS >>>> %s: VTDS_PixelBufferCache Frame: %p [ id: %@ ] pixelBuffer [ %p ] returned from cache"
+ "<<<< VT-DS >>>> %s: VTDS_PixelBufferCache Frame: %p [ id: %@ ] removed from cache (size = %ld)"
+ "<<<< VT-DS >>>> %s: VTPixelTransferSessionTransferImage failed with %d"
+ "<<<< VT-DS >>>> %s: VTVideoDecoderStartSession failed - err: %d"
+ "<<<< VT-DS >>>> %s: WARNING: waited %d seconds for video decoder to complete asynchronous frames (pendingFrames: %{public}s, minPTS: %1.3f, maxPTS: %1.3f); maybe it is stuck or has a buggy path that does not complete a frame?"
+ "<<<< VT-DS >>>> %s: Warning: discarding taggedBufferGroup %p because there is no multi-image-aware output callback to receive it"
+ "<<<< VT-DS >>>> %s: [session: %p]"
+ "<<<< VT-DS >>>> %s: [session: %p] %@ %@"
+ "<<<< VT-DS >>>> %s: [session: %p] Called from video decoder for frame: %p imageBuffer: %p"
+ "<<<< VT-DS >>>> %s: [session: %p] Calling video decoder for frame: %p sampleBuffer: %p"
+ "<<<< VT-DS >>>> %s: [session: %p] Done "
+ "<<<< VT-DS >>>> %s: [session: %p] Failed to create dispatch queue/group for async pixel transfer so doing it synchronously"
+ "<<<< VT-DS >>>> %s: [session: %p] HEVC format description bit depth change detected, possibly spuriously: currentBitsPerComponent: %d, newBitsPerComponent: %d"
+ "<<<< VT-DS >>>> %s: [session: %p] HEVC format description bit depth change detected: currentBitsPerComponent: %d, newBitsPerComponent: %d"
+ "<<<< VT-DS >>>> %s: [session: %p] Output frame for sourceFrameRefCon: %p frame: %p imageBuffer: %p status: %d"
+ "<<<< VT-DS >>>> %s: [session: %p] SubDuct: %@ %@"
+ "<<<< VT-DS >>>> %s: [session: %p] VideoDecoder: %@ %@"
+ "<<<< VT-DS >>>> %s: [session: %p] creating os_transaction: %p"
+ "<<<< VT-DS >>>> %s: [session: %p] failed to obscure frame %p with error %d"
+ "<<<< VT-DS >>>> %s: [session: %p] frame %p is obscured because of sensitive content"
+ "<<<< VT-DS >>>> %s: [session: %p] frame %p was already emitted, returning early (discarding imageBuffer %p, status %d)"
+ "<<<< VT-DS >>>> %s: [session: %p] sourceFrameRefCon: %p sampleBuffer: %p, decodeFlags: %d"
+ "<<<< VT-DS >>>> %s: [session: %p]: create decompression session for %s-process decoding: codec %c%c%c%c"
+ "<<<< VT-DS >>>> %s: calling VTDecoderSessionRegisterCustomPixelFormat on unsupported platform"
+ "<<<< VT-DS >>>> %s: create a decoder %c%c%c%c starting from index %d"
+ "<<<< VT-DS >>>> %s: decoder requested VideoToolbox handle QualityOfService"
+ "<<<< VT-DS >>>> %s: decompressionSessionOptions: %@"
+ "<<<< VT-DS >>>> %s: dolby8p1enabled %d"
+ "<<<< VT-DS >>>> %s: dolbyVision10p4Enabled %d"
+ "<<<< VT-DS >>>> %s: dropping frame: temporal level limit is %d  frame temporal level is %d"
+ "<<<< VT-DS >>>> %s: hdr10PlusEnabled %d"
+ "<<<< VT-DS >>>> %s: incomplete color information; added: %s%s%s"
+ "<<<< VT-DS >>>> %s: invalid argument configuration"
+ "<<<< VT-DS >>>> %s: invalid argument configuration %p %p %p %p"
+ "<<<< VT-DS >>>> %s: kCVPixelFormatCodecType missing in customPixelFormat"
+ "<<<< VT-DS >>>> %s: neither imageBuffer nor taggedBufferGroup -- shouldn't be called"
+ "<<<< VT-DS >>>> %s: neither outputCallback nor outputHandler"
+ "<<<< VT-DS >>>> %s: no pixelBuffer at index %d of taggedBufferGroup %@"
+ "<<<< VT-DS >>>> %s: not supported for paravirtualization host decoders -- decoder must call VTDecoderSessionCreatePixelBuffer instead"
+ "<<<< VT-DS >>>> %s: pixelBuffer %p at index %d of destinationTaggedBufferGroup %@"
+ "<<<< VT-DS >>>> %s: pixelBuffer %p at index %d of taggedBufferGroup %@"
+ "<<<< VT-DS >>>> %s: video decoder returned removed error (%d) - eGPU is unplugged"
+ "<<<< VT-DS >>>> %s: videoDecoderSpecification: %@"
+ "<<<< VT-DS >>>> %s: videoFormatDescription: %@"
+ "<<<< VT-DS >>>> %s: vtShouldDecodeFrame: %s [filter:%d rate:%f] [temporalLevelLimit: %d frame level: %d]"
+ "<<<< VT-RBS >>>>"
+ "<<<< VT-RBS >>>> %s: Failed to get processHandle for pid %d"
+ "<<<< VT-Restrictions >>>>"
+ "<<<< VT-Restrictions >>>> %s: Entitlement \"%@\" is not present."
+ "<<<< VT-Restrictions >>>> %s: Found boolean entitlement: \"%@\" --> %s"
+ "<<<< VT-Restrictions >>>> %s: Found entitlement \"%@\" but it is not boolean."
+ "<<<< VT-Restrictions >>>> %s: SecTaskCopyValueForEntitlement failed for \"%@\", error: %@"
+ "<<<< VTCGUtilities >>>>"
+ "<<<< VTCGUtilities >>>> %s: CFDataCreateMutableCopy Failed."
+ "<<<< VTCGUtilities >>>> %s: CFDataGetMutableBytePtr Failed."
+ "<<<< VTCGUtilities >>>> %s: CFDictionaryCreate Failed."
+ "<<<< VTCGUtilities >>>> %s: ColorSync is not available."
+ "<<<< VTCGUtilities >>>> %s: ColorSyncMakeProfile Failed."
+ "<<<< VTCGUtilities >>>> %s: ColorSyncProfileCopyHeader Failed."
+ "<<<< VTCGUtilities >>>> %s: ColorSyncProfileCreateMutableCopy Failed."
+ "<<<< VTCGUtilities >>>> %s: IOSurface %p bulkAttachments.premultipliedAlpha says premultiplied alpha"
+ "<<<< VTCGUtilities >>>> %s: IOSurface %p bulkAttachments.premultipliedAlpha says straight alpha"
+ "<<<< VTCGUtilities >>>> %s: IOSurface %p has unknown bulkAttachments.premultipliedAlpha %d -> assume premultiplied"
+ "<<<< VTDeghostingSession >>>>"
+ "<<<< VTDeghostingSession >>>> %s: WARNING: frame->mode != mode"
+ "<<<< VTDeghostingSession >>>> %s: WARNING: frame->outputBuffer != outputBuffer"
+ "<<<< VTDeghostingSession >>>> %s: [processorSession: %p]"
+ "<<<< VTDeghostingSession >>>> %s: [session: %p]"
+ "<<<< VTDeghostingSession >>>> %s: [session: %p] dimensions(%d,%d)"
+ "<<<< VTDeghostingSession >>>> %s: [session: %p] key: %@"
+ "<<<< VTFigAudioSession >>>>"
+ "<<<< VTFigAudioSession >>>> %s: CMSessionCreate"
+ "<<<< VTFigAudioSession >>>> %s: VTFigAudioSessionCreateUsingPrimaryAVAudioSessionSiblingForAuditToken"
+ "<<<< VTFrameSilo >>>>"
+ "<<<< VTFrameSilo >>>> %s: %@"
+ "<<<< VTFrameSilo >>>> %s: discarding output PTS info"
+ "<<<< VTFrameSilo >>>> %s: reconstituting sample buffer with DTS that isn't in formatDescriptionRanges"
+ "<<<< VTHDRImageStatisticsGenerationSession >>>>"
+ "<<<< VTHDRImageStatisticsGenerationSession >>>> %s: (%p) format: '%c%c%c%c', region: (%.2f, %.2f)[%.2f x %.2f]"
+ "<<<< VTHDRImageStatisticsGenerationSession >>>> %s: (%p) frame#: %u, bins: %u, average: %.4f, minimum: %.4f, maximum: %.4f, SD: %.4f"
+ "<<<< VTHDRImageStatisticsGenerationSession >>>> %s: (%p), Histogram Generation Mode is Unknown:%d"
+ "<<<< VTHDRImageStatisticsGenerationSession >>>> %s: (%p), Histogram Generation Mode set to Default"
+ "<<<< VTHDRImageStatisticsGenerationSession >>>> %s: (%p), Histogram Generation Mode set to MPSOnly"
+ "<<<< VTHDRImageStatisticsGenerationSession >>>> %s: (%p), Histogram Generation Mode set to MSROnly"
+ "<<<< VTHDRImageStatisticsGenerationSession >>>> %s: Histogram size (%zu) is invalid"
+ "<<<< VTHDRImageStatisticsGenerationSession >>>> %s: PixelTransferSession failed. Fallback to MPS. Performance may degrade."
+ "<<<< VTHDRImageStatisticsGenerationSession >>>> %s: PixelTransferSession succeeded but histogram isn't available. Fallback to MPS. Performance may degrade."
+ "<<<< VTHDRMetadataGenerationSession >>>>"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s:     Height %.0f"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s:     Width %.0f"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s:     X %.0f"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s:     Y %.0f"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s:   AnchorPQ %f"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s:   AnchorPower %f"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s:   Average %f"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s:   AverageOffset %d"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s:   FirstFrame %d"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s:   FramesPerSecond %f"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s:   GenerateDM4 %d"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s:   LEVEL1 %d"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s:   LEVEL3 %d"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s:   LEVEL4 %d"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s:   LEVEL5 %d"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s:   Maximum %f"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s:   MaximumOffset %d"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s:   Minimum %f"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s:   MinimumOffset %d"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s:   PixelBufferSize"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s:   RegionOfInterest"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s: %p"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s: After CMBlockBufferAppendBufferReference replacementBlockBufferRef %@"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s: HDR session state"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s: STATS: (OUT) min %d, max %d, avg %d"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s: STATS: Generating DM4"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s: STATS: POST_LEGAL min %f, max %f, avg %f"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s: STATS: PRE_LEGAL min %f, max %f, avg %f"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s: STATS: anchorPQ %d anchorPower %d"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s: STATS: anchorPower %g anchorPQ %g"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s: STATS: averageOffset %d minimumOffset %d maximumOffset %d"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s: STATS: fps %f (OUT) min %d, max %d, avg %d"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s: STATS: localStatisticsIn genDM4 %d, Available level1 %d level3 %d level4 %d"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s: appending sizeOfHDRMetadata %zu"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s: fps=%f"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s: hdrMetadataGenerationSession->firstFrame %s resetFilter %s"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s: new sample size %zu"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s: offsetIntoSampleBuffer %zu replacementBlockBufferRef %@"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s: old sample size %zu"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s: replacing sizeOfHDRMetadata %zu at offsetIntoSampleBuffer %zu"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s: resetStatisticsFiltering %s"
+ "<<<< VTHDRMetadataGenerationSession >>>> %s: session state dict = %@"
+ "<<<< VTHDRPerFrameMetadataGenerationSession >>>>"
+ "<<<< VTIORegistryKeyService >>>> %s: Caching search result of registry key %@ in IOService %@"
+ "<<<< VTIORegistryKeyService >>>> %s: Checking registry key %@ in Device IOService %@"
+ "<<<< VTIORegistryKeyService >>>> %s: Finding registry key %@ in IOService %@"
+ "<<<< VTIORegistryKeyService >>>> %s: Found cached registry key %@ in IOService %@"
+ "<<<< VTIORegistryKeyService >>>> %s: IOService object missing for %@"
+ "<<<< VTIORegistryKeyService >>>> %s: IOServiceName %@ was not found in IORegistry (err: %d)"
+ "<<<< VTIORegistryKeyService >>>> %s: Initializing cache for Device IOService %@"
+ "<<<< VTIORegistryKeyService >>>> %s: Initializing gVTIORegistryKeyServiceCache"
+ "<<<< VTMediator >>>>"
+ "<<<< VTMediator >>>> %s: %p resolved pixel buffer attributes to %@"
+ "<<<< VTMediator >>>> %s: Cannot find any preferred pixel format types. Resorting to default pipeline config."
+ "<<<< VTMediator >>>> %s: Cannot resolve attributes. Resorting to simplified pipeline config."
+ "<<<< VTMediator >>>> %s: called"
+ "<<<< VTMediator >>>> %s: called %p"
+ "<<<< VTMediator >>>> %s: called %p %@"
+ "<<<< VTMediator >>>> %s: called %p %@->%@"
+ "<<<< VTMediator >>>> %s: created <VTPixelBufferAttributesMediator %p>"
+ "<<<< VTMetalTransferSession >>>>"
+ "<<<< VTMetalTransferSession >>>> %s: %@"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTMetalTransferDescriptionKey_ShouldWaitToComplete %d -> false"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTMetalTransferDescriptionKey_ShouldWaitToComplete %d -> true"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTMetalTransferPropertyKey_AllowLowQualityScaling %d -> false"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTMetalTransferPropertyKey_AllowLowQualityScaling %d -> true"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTMetalTransferPropertyKey_PreferRenderKernel %d -> false"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTMetalTransferPropertyKey_PreferRenderKernel %d -> true"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTPixelRotationPropertyKey_FlipHorizontalOrientation %@ -> %@"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTPixelRotationPropertyKey_FlipVerticalOrientation %@ -> %@"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTPixelRotationPropertyKey_Rotation %@ -> %@"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_DestinationColorPrimaries %@ -> %@"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_DestinationICCProfile %@ -> %@"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_DestinationTransferFunction %@ -> %@"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_DestinationYCbCrMatrix %@ -> %@"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_HLGInvOETFOpticalScale %@ -> %@"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_HLGInvOETFOpticalScale %@ -> NULL"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_HLGOETFOpticalScale %@ -> %@"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_HLGOETFOpticalScale %@ -> NULL"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_Label %@ -> %@"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_Label %@ -> NULL"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_MetalCompletionQueue <%p>%@ -> <%p>%@"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_MetalSubmissionQueue <%p>%@ -> <%p>%@"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_PQEOTFOpticalScale %@ -> %@"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_PQEOTFOpticalScale %@ -> NULL"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_PQInvEOTFOpticalScale %@ -> %@"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_PQInvEOTFOpticalScale %@ -> NULL"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_WriteBlackPixelsOutsideDestRect %d -> false"
+ "<<<< VTMetalTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_WriteBlackPixelsOutsideDestRect %d -> true"
+ "<<<< VTMetalTransferSession >>>> %s: Color processing Begin"
+ "<<<< VTMetalTransferSession >>>> %s: Color processing End"
+ "<<<< VTMetalTransferSession >>>> %s: Color processing stage %ld of %ld 3D Lookup Table"
+ "<<<< VTMetalTransferSession >>>> %s: Color processing stage %ld of %ld HLG Scene Referred Mapping gamma:%2.2f gain:%2.2f luminance_coefficients:{%2.2f %2.2f %2.2f %2.2f}"
+ "<<<< VTMetalTransferSession >>>> %s: Color processing stage %ld of %ld LuminanceScaling  gamma:%2.2f gain:%2.2f luminance_coefficients:{%2.2f %2.2f %2.2f %2.2f}"
+ "<<<< VTMetalTransferSession >>>> %s: Color processing stage %ld of %ld Matrix ( %2.4f, %2.4f, %2.4f,   %2.4f, %2.4f, %2.4f,   %2.4f, %2.4f, %2.4f  )"
+ "<<<< VTMetalTransferSession >>>> %s: Color processing stage %ld of %ld PQ Tone Mapping eotf (m1, m2, c1, c2, c3) :%2.15f %2.10f %2.10f %2.10f %2.10f eetf: masterPeakInv %2.10f, masterBlackInv %2.10f, targetPeakInv %2.10f, targetBlackInv %2.10f, maxLum %2.10f, minLum %2.10f, KneeStart %2.10f, KneeStart %2.10fluminance_coefficients:{%2.10f %2.10f %2.10f %2.10f}"
+ "<<<< VTMetalTransferSession >>>> %s: Color processing stage %ld of %ld TRC type %d gamma:%f a:%f b:%f c:%f d:%f e:%f f:%f g:%f  in range[%f,%f] out range[%f,%f]"
+ "<<<< VTMetalTransferSession >>>> %s: Destination colorspace: %@"
+ "<<<< VTMetalTransferSession >>>> %s: Elapsed GPU Time %f"
+ "<<<< VTMetalTransferSession >>>> %s: Failed assertion: (pixelBytes(%lu) <= bytesPerElement(%zu) * pixelsPerBlock(%d)) pixelFormat(%c%c%c%c) metalFormat(%lu) (VTMetalTransferSession.m:%d)"
+ "<<<< VTMetalTransferSession >>>> %s: Incompatible bayer operation requested."
+ "<<<< VTMetalTransferSession >>>> %s: Incompatible source bayer component order."
+ "<<<< VTMetalTransferSession >>>> %s: Invalid rotation"
+ "<<<< VTMetalTransferSession >>>> %s: MTLDevice (%p): %@"
+ "<<<< VTMetalTransferSession >>>> %s: Requesting a LUT stage when caller has limited us to max %d"
+ "<<<< VTMetalTransferSession >>>> %s: Requesting a LuminanceScaling %ld stage when caller has limited us to max %d"
+ "<<<< VTMetalTransferSession >>>> %s: Requesting a Matrix %ld stage when caller has limited us to max %d"
+ "<<<< VTMetalTransferSession >>>> %s: Requesting a TRC %ld stage when caller has limited us to max %d"
+ "<<<< VTMetalTransferSession >>>> %s: Running in the background for reason %d, setting GPU priority low"
+ "<<<< VTMetalTransferSession >>>> %s: Session %p using device %@"
+ "<<<< VTMetalTransferSession >>>> %s: SetGPUPriorityLow is true, setting GPU priority low"
+ "<<<< VTMetalTransferSession >>>> %s: Source      colorspace: %@"
+ "<<<< VTMetalTransferSession >>>> %s: Will%s allow one pass Metal scaling -- thank you for setting \"ffctl CoreMedia/AllowOnePassMetalScaling=%s\""
+ "<<<< VTMetalTransferSession >>>> %s: colorOps rgbToYUV:( %2.4f, %2.4f, %2.4f,   %2.4f, %2.4f, %2.4f,   %2.4f, %2.4f, %2.4f )"
+ "<<<< VTMetalTransferSession >>>> %s: colorOps yuvToRGB:( %2.4f, %2.4f, %2.4f,   %2.4f, %2.4f, %2.4f,   %2.4f, %2.4f, %2.4f )"
+ "<<<< VTMetalTransferSession >>>> %s: colorOps yuvToyuv:( %2.4f, %2.4f, %2.4f,   %2.4f, %2.4f, %2.4f,   %2.4f, %2.4f, %2.4f )"
+ "<<<< VTMetalTransferSession >>>> %s: computeFunction not found %@"
+ "<<<< VTMetalTransferSession >>>> %s: cropAndScale  scale:( %2.2f, %2.2f )  src[0].offset:( %2.2f, %2.2f )  dstOffset:( %d, %d )  dimensions:( %d, %d )"
+ "<<<< VTMetalTransferSession >>>> %s: debayer method %d: needHighPrecision: %d, isFullFloatSamplable: %d, shouldUseFullFloatTexture: %d"
+ "<<<< VTMetalTransferSession >>>> %s: failed to create a MTLCommandBuffer. MTLCommandQueue = %p"
+ "<<<< VTMetalTransferSession >>>> %s: fragmentFunction not found.%@"
+ "<<<< VTMetalTransferSession >>>> %s: intermediateTexture with invalid dimensions."
+ "<<<< VTMetalTransferSession >>>> %s: processComputeKernelSyncFunctionConstant failed %d."
+ "<<<< VTMetalTransferSession >>>> %s: processRenderKernelSyncFunctionConstant failed %d."
+ "<<<< VTMetalTransferSession >>>> %s: renderPass count: %d"
+ "<<<< VTMetalTransferSession >>>> %s: textData:( %2.2f, %2.2f, %2.2f, %2.2f )  vertData:( %2.2f, %2.2f, %2.2f, %2.2f )"
+ "<<<< VTMetalTransferSession >>>> %s: use advanced debayer pass"
+ "<<<< VTMetalTransferSession >>>> %s: vertexFunction not found. %@"
+ "<<<< VTMotionEstimationSession >>>>"
+ "<<<< VTMotionEstimationSession >>>> %s: %c%c%c%c (%zd bytes) guestUUID %@"
+ "<<<< VTMotionEstimationSession >>>> %s: Client requested confidence value, but the processor doesn't acknowledge supporting it."
+ "<<<< VTMotionEstimationSession >>>> %s: Found a match to %@"
+ "<<<< VTMotionEstimationSession >>>> %s: WARNING: waited %d seconds for motion estimation processor to complete asynchronous frames; maybe it is stuck or has a buggy path that does not complete a frame?"
+ "<<<< VTMotionEstimationSession >>>> %s: Will%s connect to videocodecd for motion estimation -- thank you for setting \"ffctl CoreMedia/SeparateCodecProcess_MotionEstimation=%s\""
+ "<<<< VTMotionEstimationSession >>>> %s: [session: %p]"
+ "<<<< VTMotionEstimationSession >>>> %s: [session: %p] dimensions(%d,%d)"
+ "<<<< VTMotionEstimationSession >>>> %s: [session: %p] key: %@"
+ "<<<< VTMotionEstimationSession >>>> %s: [session: %p] ref %p current %p"
+ "<<<< VTMotionEstimationSession >>>> %s: begin"
+ "<<<< VTMotionEstimationSession >>>> %s: couldn't access path \"%s\""
+ "<<<< VTMotionEstimationSession >>>> %s: err %d, guestProtocolVersion %d, hostProtocolVersion %d"
+ "<<<< VTMotionEstimationSession >>>> %s: registered paravirtualized motion estimation processor for (%@ / %@) err %d"
+ "<<<< VTMultiPassStorage >>>>"
+ "<<<< VTMultiPassStorage >>>> %s: %p"
+ "<<<< VTMultiPassStorage >>>> %s: %p created new file at %@"
+ "<<<< VTMultiPassStorage >>>> %s: %p created new temporary file at %@"
+ "<<<< VTMultiPassStorage >>>> %s: %p opened existing file at %@"
+ "<<<< VTMultiPassStorage >>>> %s: Greater %d@%lld/%d"
+ "<<<< VTMultiPassStorage >>>> %s: Less %d@%lld/%d"
+ "<<<< VTMultiPassStorage >>>> %s: deleting %d@%lld/%d"
+ "<<<< VTMultiPassStorage >>>> %s: mismatch between storage (%@) and client (%@)"
+ "<<<< VTMultiPassStorage >>>> %s: writing %d@%lld/%d offset:%lld writeByteCount:%lld"
+ "<<<< VTPIXELBUFFERCONFORMER >>>>"
+ "<<<< VTPIXELBUFFERCONFORMER >>>> %s: <VTPixelBufferConformer %p> Has no target attributes. Functioning as pass through only."
+ "<<<< VTPIXELBUFFERCONFORMER >>>> %s: Buffer pool found to be incompatible."
+ "<<<< VTPIXELBUFFERCONFORMER >>>> %s: Called %@"
+ "<<<< VTPIXELBUFFERCONFORMER >>>> %s: Cannot allocate buffer from pool. Returning error."
+ "<<<< VTPIXELBUFFERCONFORMER >>>> %s: Source pixel buffer has no value for attribute %@"
+ "<<<< VTPIXELBUFFERCONFORMER >>>> %s: VTPixelBufferConformer <%p> conformed buffer <%p> in format [%d] to buffer <%p> as format [%d]"
+ "<<<< VTPIXELBUFFERCONFORMER >>>> %s: VTPixelBufferConformer <%p> created new pool <%p>"
+ "<<<< VTPIXELBUFFERCONFORMER >>>> %s: called. <VTPixelBufferConformer %p> : sourceBuffer is conformant"
+ "<<<< VTPIXELBUFFERCONFORMER >>>> %s: called. <VTPixelBufferConformer %p> conformed NULL sourceBuffer to NULL conformedBufferOut"
+ "<<<< VTPIXELBUFFERCONFORMER >>>> %s: called. Created <VTPixelBufferConformer %p>"
+ "<<<< VTPIXELBUFFERCONFORMER >>>> %s: conformedTaggedBufferGroupOut is NULL, do nothing"
+ "<<<< VTPIXELBUFFERCONFORMER >>>> %s: sourceTaggedBufferGroup is NULL."
+ "<<<< VTParavirtualization >>>>"
+ "<<<< VTParavirtualization >>>> %s: %@ -> %@"
+ "<<<< VTParavirtualization >>>> %s: %c%c%c%c (%zd bytes)%s%s"
+ "<<<< VTParavirtualization >>>> %s: %p"
+ "<<<< VTParavirtualization >>>> %s: %s"
+ "<<<< VTParavirtualization >>>> %s: (%p %s) %c%c%c%c about to signal semaphore %p for replyIdentifier %lld"
+ "<<<< VTParavirtualization >>>> %s: (%p %s) %c%c%c%c after signalling semaphore %p for replyIdentifier %lld, result %d"
+ "<<<< VTParavirtualization >>>> %s: (%p %s) %c%c%c%c not signalling semaphore %p for replyIdentifier %lld because we haven't yet received the full reply"
+ "<<<< VTParavirtualization >>>> %s: (%p %s) about to wait on semaphore %p for replyIdentifier %lld"
+ "<<<< VTParavirtualization >>>> %s: (%p %s) no pending reply struct found for replyIdentifier %lld"
+ "<<<< VTParavirtualization >>>> %s: (%p %s) wait succeeded on semaphore %p for replyIdentifier %lld; reply message %c%c%c%c"
+ "<<<< VTParavirtualization >>>> %s: (%p %s) warning: abandoning iosurfaceMappingID %lld, possible protocol mismatch"
+ "<<<< VTParavirtualization >>>> %s: (%p %s) warning: releasing iosurface %p id %d, possible protocol mismatch"
+ "<<<< VTParavirtualization >>>> %s: (%p %s) wrote replyIdentifier %lld into message type %c%c%c%c (%zd bytes)"
+ "<<<< VTParavirtualization >>>> %s: (%p) %c%c%c%c (%zd bytes) -> uuid %02x%02x%02x%02x..."
+ "<<<< VTParavirtualization >>>> %s: -> %p"
+ "<<<< VTParavirtualization >>>> %s: IOSurfaceGetBulkAttachments returned error %d for ioSurface %p"
+ "<<<< VTParavirtualization >>>> %s: IOSurfaceGetDataProperty of IOSurfaceDataProperty index %u returned error %d for ioSurface %p"
+ "<<<< VTParavirtualization >>>> %s: Relinquishing surface mapping ID %d"
+ "<<<< VTParavirtualization >>>> %s: box length %lld at offset %zd exceeds remaining length %zd"
+ "<<<< VTParavirtualization >>>> %s: box length %lld at offset %zd is too small"
+ "<<<< VTParavirtualization >>>> %s: guest UUID not found"
+ "<<<< VTParavirtualization >>>> %s: guestUUID %@ was not found!"
+ "<<<< VTParavirtualization >>>> %s: hostSession %p is invalid - skipping sending message of type %c%c%c%c to the guest"
+ "<<<< VTParavirtualization >>>> %s: hostSession %p is invalid - skipping sending reply type %c%c%c%c to the guest"
+ "<<<< VTParavirtualization >>>> %s: message type %c%c%c%c (%zd bytes) flags 0x%x uuid %02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x"
+ "<<<< VTParavirtualization >>>> %s: parameter box of length %lld at offset %zd matches target parameter %c%c%c%c but has type %c%c%c%c where %c%c%c%c was expected"
+ "<<<< VTParavirtualization >>>> %s: replyTimeOutInNanoSeconds is %d"
+ "<<<< VTParavirtualization >>>> %s: timeout waiting for pending reply with identifier %lld, messageType '%c%c%c%c'"
+ "<<<< VTParavirtualization >>>> %s: uuid %02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x"
+ "<<<< VTParavirtualization >>>> %s: warning: message says guest not waiting for reply but reply is marked as a reply for guest"
+ "<<<< VTParavirtualization >>>> %s: warning: message says guest waiting for reply and to be continued"
+ "<<<< VTParavirtualization >>>> %s: warning: message says guest waiting for reply but reply is not marked as a reply for guest"
+ "<<<< VTParavirtualization >>>> %s: warning: message says host not waiting for reply but reply is marked as a reply for host"
+ "<<<< VTParavirtualization >>>> %s: warning: message says host waiting for reply and to be continued"
+ "<<<< VTParavirtualization >>>> %s: warning: message says host waiting for reply but reply is not marked as a reply for host"
+ "<<<< VTParavirtualizationHostDecoder >>>>"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: %p"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) %@ %@ -> %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) %@ -> %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) %@ -> %d, %@"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) %d surfaceMappingIDs to relinquish, leaving %d pending frames"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) %d x %d -> %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) %d, %@"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) %{public}s pixelBufferAttributes %@"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) -> %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) -> %d, %@"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) CreatePixelBuffer failed for frame %d with error %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) EmitDecodedFrame failed for frame %d status %d infoFlags %d pixelBuffer %p with error %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) EmitDecodedMultiImageFrame failed for frame %d status %d infoFlags %d taggedBufferGroup %{public}@ with error %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) EmitDecodedTile failed for tile %lld status %d decodeFlags %d pixelBuffer %p with err %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) GetDestinationPixelBufferAttributes failed with error %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) IOSurfaceMappingIDsToRelinquish %d %@"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) SetTileDecodeRequirements failed with error %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) VTVideoDecoderCopyProperty for %{public}@ failed with error %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) VTVideoDecoderCopySerializableProperties failed for %{public}@ with error %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) VTVideoDecoderCopySupportedPropertyDictionary failed for %{public}@ with error %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) VTVideoDecoderDecodeFrame or VTVideoDecoderDecodeFrameWithOptions failed with error %d, frame %d, flags 0x%x"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) VTVideoDecoderDecodeTile failed with error %d, tile %lld tileCropOffset [%d, %d], tileCropDimensions %d x %d, offsetWithinPixelBuffer [%d, %d] flags 0x%x"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) VTVideoDecoderFinishDelayedFrames failed with error %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) VTVideoDecoderFinishDelayedTiles failed with error %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) VTVideoDecoderInvalidate failed with error %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) VTVideoDecoderSetProperties failed for %{public}@ with error %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) VTVideoDecoderSetProperty for %{public}@ failed with error %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) VTVideoDecoderStartSession failed for %d x %d with error %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) VTVideoDecoderStartTileSession failed for %d x %d with error %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) frame %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) frame %d sbuf %d bytes flags 0x%x frameOptions %@ -> %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) frame %d status %d infoFlags %d pixelBuffer %p"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) frame %d status %d infoFlags %d taggedBufferGroup %@"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) number of pending frames %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) tile %lld hostDecoderSession->tileSurfaceMappingIDsInUse %@"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) tile %lld pixelBuffer %p pixelBufferUUID %@ ioSurfaceMappingID %lld hostDecoderSession->tileSurfaceMappingIDsInUse %@"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) tile %lld sbuf %d bytes tileCropOffset [%d, %d], tileCropDimensions %d x %d, pixelBuffer %p, offsetWithinPixelBuffer [%d, %d] flags 0x%x -> %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p decoder %p) tile %lld status %d decodeFlags %d pixelBuffer %p"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p) %c%c%c%c (%zd bytes)%s%s%s (%d iosurfaces)"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p) %c%c%c%c (%zd bytes)%s%s%s -> error %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p) WARNING: waited %u seconds for pending frames %@, calling CleanUpAfterDecode"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p) WARNING: waited %u seconds for pending tiles %@, calling CleanUpAfterTileDecode"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p) unrecognized messageType %c%c%c%c"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: NULL pixel buffer in taggedBufferGroup for bufferIndex %d"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: NULL pixelBufferUUID for pixelBuffer %p"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: Removing %@ because it is in the deny list"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: Something went wrong. tilesWithIOSurfaceMappingID = 0 for ioSurfaceMappingID %lld."
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: Tile %lld should be in tilesWithIOSurfaceMappingID %@, but it is missing!"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: Why does tilesWithIOSurfaceMappingID contain no entry for tile %lld when stuff->surfaceMappingIDArray says that ioSurfaceMappingID %lld is being used for that tile?"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: destinationPixelBufferAttributes %@"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: frame %d pixelBuffer %p pixelBufferUUID %@ iosurfaceMappingID %lld -- %d pixel buffers now pending"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: guestProtocolVersion %u hostProtocolVersion %u, guestInfo %{public}@, hostBuildVersion %{public}@"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: hostDecoderSession %p is invalid - skipping delivering message of type %c%c%c%c from the guest"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: hostDecoderSession %p is invalid - skipping sending message type %c%c%c%c to the guest"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: pixelBuffer %p not found in pendingFramesToSurfaceStuff (%d entries)"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: tagCollection is NULL for bufferIndex %d"
+ "<<<< VTParavirtualizationHostEncoder >>>>"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: %p"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) %@ %@ -> %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) %@ -> %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) %@ -> %d, %@"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) %@-> %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) %d surface mapping IDs to relinquish"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) %d x %d -> %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) %d, %@"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) -> %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) -> %d, %@"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) MultipassIdentifier %@ -> %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) MultipassStorageCopyDataAtTimeStamp failed for timeStamp %1.3f index %d with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) MultipassStorageCopyIdentifier failed for %{public}@ with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) MultipassStorageGetTimeStamp failed for fromTimeStamp %1.3f MultipassStep %@ TimeStamp %1.3f with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) MultipassStorageGetTimeStampAndDuration failed for fromTimeStamp %1.3f MultipassStep %@ TimeStamp %1.3f Duration %1.3f with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) MultipassStorageInvalidate failed with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) MultipassStorageSetDataAtTimeStamp failed for timeStamp %1.3f index %d with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) MultipassStorageSetIdentifier failed for %{public}@ with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) SetTimeRangesForNextPass failed for timeRangeCount %d with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) VTVideoEncoderBeginPass failed for beginPassFlags %u with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) VTVideoEncoderCompleteFrames failed for completeUntilPTS %1.3f with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) VTVideoEncoderCompleteTiles failed with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) VTVideoEncoderCopyProperty failed for %{public}@ with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) VTVideoEncoderCopySerializableProperties failed with error %d, for %{public}@"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) VTVideoEncoderCopySupportedPropertyDictionary failed for %{public}@ with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) VTVideoEncoderEncodeMultiImageFrame failed for frame %d PTS %1.3f duration %1.3f flags 0x%x with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) VTVideoEncoderEndPass failed for furtherPassesRequested %d with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) VTVideoEncoderInvalidate failed with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) VTVideoEncoderPrepareToEncodeFrames failed with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) VTVideoEncoderPrepareToEncodeTiles failed with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) VTVideoEncoderSetProperties failed for %{public}@ with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) VTVideoEncoderSetProperty failed for %{public}@ %{public}@ with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) VTVideoEncoderStartSession failed for %d x %d with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) VTVideoEncoderStartTileSession failed for %d x %d with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) beginPassFlags %u -> %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) completeUntilPTS %1.3f-> %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) frame %d PTS %1.3f duration %1.3f flags 0x%x -> %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) frame %lld pixelBuffer %p pixelBufferUUID %@ ioSurfaceMappingID %lld"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) frame %lld pixelBufferUUIDArray %@ ioSurfaceMappingIDArray %@"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) fromTimeStamp %1.3f MultipassStep %@ TimeStamp %1.3f -> %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) fromTimeStamp %1.3f MultipassStep %@ TimeStamp %1.3f Duration %1.3f -> %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) furtherPassesRequested %d -> %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) tile %lld status %d encodeFlags 0x%x sampleBuffer %@"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) tile %lld tileOffset (%d, %d) tileAperture %d x %d tileProperties %@ flags 0x%x -> %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) tileIndex %lld hostEncoderSession->tileSurfaceMappingIDsInUse %@"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) tileIndex %lld pixelBuffer %p pixelBufferUUID %@ ioSurfaceMappingID %lld hostEncoderSession->tileSurfaceMappingIDsInUse %@"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) timeRangeCount %d -> %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p encoder %p) timeStamp %1.3f index %d -> %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p) %c%c%c%c (%zd bytes)%s%s%s (%d iosurfaces)"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p) %c%c%c%c (%zd bytes)%s%s%s -> error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p) WARNING: waited %u seconds but EmitEncodedFrame calls are still pending"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p) WARNING: waited %u seconds but EmitEncodedTile calls are still pending"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p) unrecognized messageType %c%c%c%c"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: CVPixelBufferCreateWithIOSurface failed with error %d"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: CreateVideoFormatDescription failed with error %d (%p encoder %p)"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: CreateVideoFormatDescription failed with error %d, (%p encoder %p)"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: EmitEncodedFrame failed with error %d for frame %p: sbuf PTS %1.3f, %zd bytes, encodeFlags 0x%x (%p encoder %p)"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: EmitEncodedTile failed with error %d for tile %p: sbuf PTS %1.3f, %zd bytes, encodeFlags 0x%x (%p encoer %p)"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: Removing %@ because it is in the deny list"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: SetPixelBufferAttributes failed with error %d, (%p encoder %p)"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: SetTileAttributes failed with error %d (%p encoder %p)"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: SetTileEncodeRequirements failed with error %d (%p encoder %p)"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: This shouldn't have happened. How come EmitEncodedFrame was called more than once for frame %lld?"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: This shouldn't have happened. How come EmitEncodedTile was called more than once for tile %lld?"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: This shouldn't have happened. How come EncodeTileDidComplete was called more than once for tile %lld?"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: This shouldn't have happened. How come encodeFrameDidComplete was called more than once for frame %lld?"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: Tile %lld should be in tilesWithIOSurfaceMappingID %@, but it is missing!"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: VTVideoEncoderEncodeFrame failed with error %d, (%p encoder %p) frame %d PTS %1.3f duration %1.3f flags 0x%x"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: VTVideoEncoderEncodeTile failed with error %d, (%p encoder %p) tile %lld tileOffset (%d, %d) tileAperture %d x %d tileProperties %{public}@ flags 0x%x"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: Why does tilesWithIOSurfaceMappingID contain no entry for tile %lld when stuff->surfaceMappingIDArray says that ioSurfaceMappingID %lld is being used for that tile?"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: frame %p: sbuf PTS %1.3f, %zd bytes, encodeFlags 0x%x"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: guestProtocolVersion %u hostProtocolVersion %u, guestInfo %{public}@, hostBuildVersion %{public}@"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: hostEncoderSession %p is invalid - skipping delivering message of type %c%c%c%c from the guest"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: hostEncoderSession %p is invalid - skipping sending message of type %c%c%c%c to the guest"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: message type %c%c%c%c (%zd bytes) flags 0x%x uuid %02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: tile %p: sbuf PTS %1.3f, %zd bytes, encodeFlags 0x%x"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>>"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: %p"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: (%p decoder %p) %@ -> %d"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: (%p processor %p) %@ %@ -> %d"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: (%p processor %p) %@ -> %d, %@"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: (%p processor %p) %d surface mapping IDs to relinquish"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: (%p processor %p) %d surfaceMappingIDs to relinquish, mappingIDsDesc %@, pixelBufferUUIDDesc %@, leaving %d pixel buffers"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: (%p processor %p) %d, %@"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: (%p processor %p) -> %d"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: (%p processor %p) err %d pixelBufferAttributes %@"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: (%p processor %p) pixelBuffer %p still retained by someone else in this process"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: (%p processor %p) requestID %d"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: (%p processor %p) requestID %lu flags 0x%x frameOptions %@ -> %d"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: (%p processor %p) requestID %lu pixelBuffer %p pixelBufferUUID %@ iosurfaceMappingID %llu"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: (%p processor %p) requestID %lu status %d infoFlags %d additionalInfo %@ pixelBuffer %p"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: (%p processorSession %p) %d x %d -> %d"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: (%p processor] %p) -> %d"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: (%p) %c%c%c%c (%zd bytes)%s%s%s (%d iosurfaces)"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: (%p) WARNING: waited %u seconds for processing frames, calling CleanUpAfterProcessing"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: (%p) unrecognized messageType %c%c%c%c"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: Not implemented yet..."
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: There are %ld mapped IOSurfaces still present after final cleanup -- were they leaked by the motion estimation processor?  They are likely to be leaked or abandoned now."
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: guestProtocolVersion %u hostProtocolVersion %u, guestInfo %{public}@, hostBuildVersion %{public}@"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: hostProcessorSession %p is invalid - skipping delivering message of type %c%c%c%c from the guest"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: hostProcessorSession %p is invalid - skipping sending message type %c%c%c%c to the guest"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: pixelBuffer %p not found in pixelBufferSurfaceStuff (%d entries)"
+ "<<<< VTParavirtualizationHostMotionEstimationProcessor >>>> %s: requestID %lu pixelBuffer %p pixelBufferUUID %@ iosurfaceMappingID %lld -- %d pixel buffers now pending"
+ "<<<< VTParavirtualizationSampleBufferSerialization >>>>"
+ "<<<< VTParavirtualizationSampleBufferSerialization >>>> %s: Expected number of sampleAttachments is 0."
+ "<<<< VTParavirtualizationSampleBufferSerialization >>>> %s: Key %@ was not found. Going to append CFString instead of key index"
+ "<<<< VTParavirtualizationSampleBufferSerialization >>>> %s: atomType %c%c%c%c, plist %@"
+ "<<<< VTParavirtualizationSampleBufferSerialization >>>> %s: expectedNumSamples is %ld whereas FigCFArrayGetCount( sampleAttachmentsOnBuffer ) is %ld"
+ "<<<< VTParavirtualizationSampleBufferSerialization >>>> %s: unrecognized protected video codec type %c%c%c%c -- cannot create cryptor"
+ "<<<< VTParavirtualizationSampleBufferSerialization >>>> %s: vtParavirtualizationAtomWriterAppendCFType encountered an unsupported serializable CFType value: %@"
+ "<<<< VTPixelRotationSession >>>>"
+ "<<<< VTPixelRotationSession >>>> %s: %p enableHardwareTransfer=%d session_enableHardware=%d  avoidHardware=%d  compressedUnalignedBlackfill=%d  isProtectedTransfer=%d"
+ "<<<< VTPixelRotationSession >>>> %s: %p enableMetalTransfer=%d  avoidHardware=%d  isAudioAccessory=%d  canUseMetalInTheBackground=%d  session_enableGPU=%d  isProtectedTransfer=%d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTMetalTransferPropertyKey_AllowLowQualityScaling %d -> %d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTMetalTransferPropertyKey_PreferRenderKernel %d -> %d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelRotationPropertyKey_AllowPixelTransferChain %d -> %d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelRotationPropertyKey_AllowPixelTransferGraph %d -> %d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelRotationPropertyKey_DestinationColorPrimaries %{public}@ -> %{public}@"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelRotationPropertyKey_DestinationICCProfile %{public}@ -> %{public}@"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelRotationPropertyKey_DestinationTransferFunction %{public}@ -> %{public}@"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelRotationPropertyKey_DestinationYCbCrMatrix %{public}@ -> %{public}@"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelRotationPropertyKey_EnableGPUAcceleratedTransfer %d -> %d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelRotationPropertyKey_EnableHardwareAcceleratedTransfer %d -> %d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelRotationPropertyKey_EnableHighSpeedTransfer NA -> %d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelRotationPropertyKey_EnableHistogram NA -> %d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelRotationPropertyKey_EnableSoftwareTransfer %d -> %d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelRotationPropertyKey_FlipHorizontalOrientation %d -> %d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelRotationPropertyKey_FlipVerticalOrientation %d -> %d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelRotationPropertyKey_ForceDisableVectorInstructions %d -> %d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelRotationPropertyKey_ForceSingleThreaded %d -> %d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelRotationPropertyKey_HistogramRectangle NA -> %{public}@"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelRotationPropertyKey_Rotation %d -> %d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelRotationPropertyKey_SetGPUPriorityLow %d -> %d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelRotationPropertyKey_ZeroFillData NA -> %d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_AllowFallbacks %d -> %d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_AllowOnePassMetalScaling %{public}s -> %{public}s"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_DestinationRectangle [%ld, %ld, %ld, %ld] -> [%ld, %ld, %ld, %ld]"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_DisableDither %d -> %d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_DownsamplingMode %d -> %d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_DownsamplingMode %d -> false"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_DownsamplingMode %d -> true"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_HLGInvOETFOpticalScale %{public}@ -> %{public}@"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_HLGOETFOpticalScale %{public}@ -> %{public}@"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_HLGOETFOpticalScale %{public}@ -> NULL"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_Label %{public}@ -> %{public}@"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_Label %{public}@ -> NULL"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_MetalCompletionQueue <%p>%@ -> <%p>%@"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_MetalSubmissionQueue <%p>%@ -> <%p>%@"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_PQEOTFOpticalScale %{public}@ -> %{public}@"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_PQEOTFOpticalScale %{public}@ -> NULL"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_PQInvEOTFOpticalScale %{public}@ -> %{public}@"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_PQInvEOTFOpticalScale %{public}@ -> NULL"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_ReducedPrecisionFractionalOffsets %d -> %d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_SourceCropRectangle [%ld, %ld, %ld, %ld] -> [%ld, %ld, %ld, %ld]"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_WriteBlackPixelsOutsideDestRect %d -> %d"
+ "<<<< VTPixelRotationSession >>>> %s: %p kVTPixelTransferPropertyKey_vImageFlags %llu -> %llu"
+ "<<<< VTPixelRotationSession >>>> %s: %{public}s: {%.2f,%.2f},{%.2f,%.2f}"
+ "<<<< VTPixelRotationSession >>>> %s: (%p) Building VT Chain for '%c%c%c%c' %{public}s sid 0x%x to '%c%c%c%c' %{public}s sid 0x%x  %d degrees %{public}s %{public}s %lf ms"
+ "<<<< VTPixelRotationSession >>>> %s: (%p) Built chain stage (%ld of %ld) %{public}@"
+ "<<<< VTPixelRotationSession >>>> %s: (%p) Transfer '%c%c%c%c' [%d x %d] sid 0x%x to '%c%c%c%c' [%d x %d] sid 0x%x %d degrees%{public}s%{public}s %lf ms"
+ "<<<< VTPixelRotationSession >>>> %s: (%p) primaries:%{public}@ transfer:%{public}@ matrix:%{public}@ icc:%{public}@ cgcolor:%{public}@ -> primaries:%{public}@ transfer:%{public}@ matrix:%{public}@ icc:%{public}@"
+ "<<<< VTPixelRotationSession >>>> %s: Re-attempting VTPixelTransferGraphBuildChain with HW transfers disabled"
+ "<<<< VTPixelRotationSession >>>> %s: Re-attempting VTPixelTransferGraphBuildChain with Metal transfers disabled"
+ "<<<< VTPixelRotationSession >>>> %s: ReducedPrecisionFractionalOffsets is not available on current hardware."
+ "<<<< VTPixelRotationSession >>>> %s: VTPixelRotationSession Unsupported pixel format %c%c%c%c"
+ "<<<< VTPixelRotationSession >>>> %s: out of bounds dest rect"
+ "<<<< VTPixelRotationSession >>>> %s: out of bounds source rect"
+ "<<<< VTPixelRotationSession >>>> %s: scaling not supported in software path (%i degrees). Dimensions don't match. %fx%f -> %fx%f"
+ "<<<< VTPixelRotationSession >>>> %s: src/dest pixel format differ"
+ "<<<< VTPixelRotationSession >>>> %s: vtPixelRotationChainDoTransfer failed"
+ "<<<< VTPixelTransferGraph >>>>"
+ "<<<< VTPixelTransferGraph >>>> %s: %s"
+ "<<<< VTPixelTransferGraph >>>> %s: Graph search statistics: time %lf s  total nodes %zu  edges %zu  nodes explored %zu  resulting edge count %d  path cost %zu"
+ "<<<< VTPixelTransferGraph >>>> %s: Graph search: found single shot gpu; skipping full graph search"
+ "<<<< VTPixelTransferGraph >>>> %s: Graph search: found single shot hardware; skipping full graph search"
+ "<<<< VTPixelTransferGraph >>>> %s: [%c%c%c%c fields %d  matrix %d  depth %d  desc %d] => [%c%c%c%c fields %d  matrix %d  depth %d  desc %d]"
+ "<<<< VTPixelTransferGraph >>>> %s: dstDescription for %c%c%c%c is NULL"
+ "<<<< VTPixelTransferGraph >>>> %s: srcDescription for %c%c%c%c is NULL"
+ "<<<< VTPixelTransferSession >>>>"
+ "<<<< VTPixelTransferSession >>>> %s: "
+ "<<<< VTPixelTransferSession >>>> %s: %p VTFillPixelsOutsideDestRectWithBlack failed with code %d  %c%c%c%c [%d x %d] rect:(%d, %d, %d, %d)"
+ "<<<< VTPixelTransferSession >>>> %s: %p enableHardwareTransfer=%d  preferMetal=%d  session_enableHardware=%d  avoidHardware=%d  allowHardware=%d  compressedUnalignedBlackfill=%d  isProtectedTransfer=%d"
+ "<<<< VTPixelTransferSession >>>> %s: %p enableMetalTransfer=%d  allowMetalTransfer=%d  avoidHardware=%d  isAudioAccessory=%d  canUseMetalInTheBackground=%d  session_enableGPU=%d  isProtectedTransfer=%d"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTMetalTransferPropertyKey_RequireDeviceRegistryID %d -> %llu"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTMetalTransferPropertyKey_RequireDeviceRegistryID %d -> 0"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_AllowFallbacks %d -> %d"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_AllowLowQualityScaling %d -> %d"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_AllowOnePassMetalScaling %{public}s -> %{public}s"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_AllowPixelTransferChain %d -> %d"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_AllowPixelTransferGraph %d -> %d"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_Convert10BitHDRToSDRFor8BitDestinationWithUnspecifiedColorProperties %d -> %d"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_DestinationCleanAperture %{public}@ -> %{public}@"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_DestinationColorPrimaries %{public}@ -> %{public}@"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_DestinationICCProfile %{public}@ -> %{public}@"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_DestinationPixelAspectRatio %{public}@ -> %{public}@"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_DestinationRectangle [%ld, %ld, %ld, %ld] -> [%ld, %ld, %ld, %ld]"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_DestinationTransferFunction %{public}@ -> %{public}@"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_DestinationYCbCrMatrix %{public}@ -> %{public}@"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_DisableDither %d -> %d"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_DownsamplingMode %{public}@ -> %{public}@"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_EnableGPUAcceleratedTransfer %d -> %d"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_EnableHardwareAcceleratedTransfer %d -> %d"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_EnableHighSpeedTransfer %d -> %d"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_EnableHistogram %d -> %d"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_EnableSoftwareTransfer %d -> %d"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_ForceDisableVectorInstructions %d -> %d"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_ForceSingleThreaded %d -> %d"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_HLGInvOETFOpticalScale %{public}@ -> %{public}@"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_HLGInvOETFOpticalScale %{public}@ -> NULL"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_HLGOETFOpticalScale %{public}@ -> %{public}@"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_HLGOETFOpticalScale %{public}@ -> NULL"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_HistogramRectangle %{public}@ -> %{public}@"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_Label %{public}@ -> %{public}@"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_MetalCompletionQueue <%p>%@ -> <%p>%@"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_MetalSubmissionQueue <%p>%@ -> <%p>%@"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_PQEOTFOpticalScale %{public}@ -> %{public}@"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_PQEOTFOpticalScale %{public}@ -> NULL"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_PQInvEOTFOpticalScale %{public}@ -> %{public}@"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_PQInvEOTFOpticalScale %{public}@ -> NULL"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_RealTime %d -> %d"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_RealTime %{public}@ -> %{public}@"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_ReducedPrecisionFractionalOffsets %d -> %d"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_ScalingMode %{public}@ -> %{public}@"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_SetGPUPriorityLow %d -> %d"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_SourceCropRectangle [%ld, %ld, %ld, %ld] -> [%ld, %ld, %ld, %ld]"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_UseOptimalMSRCoefficients %d -> %d"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_WriteBlackPixelsOutsideDestRect %d -> %d"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_vImageFlags %llu -> %llu"
+ "<<<< VTPixelTransferSession >>>> %s: %p kVTPixelTransferPropertyKey_vImageFlags %llu -> 0"
+ "<<<< VTPixelTransferSession >>>> %s: (%p) Blitting inline, then using dynamic module for scaling"
+ "<<<< VTPixelTransferSession >>>> %s: (%p) Building VT Chain for '%c%c%c%c' %{public}s sid 0x%x to '%c%c%c%c' %{public}s sid 0x%x"
+ "<<<< VTPixelTransferSession >>>> %s: (%p) Built chain stage (%ld of %ld) %{public}@"
+ "<<<< VTPixelTransferSession >>>> %s: (%p) Can't find compatible dynamic module"
+ "<<<< VTPixelTransferSession >>>> %s: (%p) Can't reuse dynamic module, closing service"
+ "<<<< VTPixelTransferSession >>>> %s: (%p) Dynamic session for '%c%c%c%c' (%d x %d) to '%c%c%c%c' (%d x %d)"
+ "<<<< VTPixelTransferSession >>>> %s: (%p) Failed %{public}s for '%c%c%c%c' (%d x %d) offset: (%d, %d) %{public}s%{public}s primaries:%{public}@ transfer:%{public}@ matrix:%{public}@ icc:%{public}p cgcolor:%{public}p to '%c%c%c%c' (%d x %d) offset: (%d, %d) %{public}s primaries:%{public}@ transfer:%{public}@ matrix:%{public}@ icc:%p%{public}s%{public}s."
+ "<<<< VTPixelTransferSession >>>> %s: (%p) Failed to build chain, closing dynamic pixel transfer service"
+ "<<<< VTPixelTransferSession >>>> %s: (%p) IntermediateBuffer '%c%c%c%c' (%d, %d, %d, %d) sid 0x%x"
+ "<<<< VTPixelTransferSession >>>> %s: (%p) Transfer '%c%c%c%c' [%d x %d] sid 0x%x to '%c%c%c%c' [%d x %d] sid 0x%x %lf ms"
+ "<<<< VTPixelTransferSession >>>> %s: (%p) Unsupported chroma location. Chroma siting will be incorrect. <%{public}@>"
+ "<<<< VTPixelTransferSession >>>> %s: (%p) Using dynamic module for scaling, then blitting inline"
+ "<<<< VTPixelTransferSession >>>> %s: (%p) found dynamic session!"
+ "<<<< VTPixelTransferSession >>>> %s: (%p) intermediate->dest service failed validation"
+ "<<<< VTPixelTransferSession >>>> %s: (%p) primaries:%{public}@ transfer:%{public}@ matrix:%{public}@ icc:%{public}@ cgcolor:%{public}@ -> primaries:%{public}@ transfer:%{public}@ matrix:%{public}@ icc:%{public}@"
+ "<<<< VTPixelTransferSession >>>> %s: (%p) source->dest service failed validation"
+ "<<<< VTPixelTransferSession >>>> %s: (%p) source->intermediate service failed validation"
+ "<<<< VTPixelTransferSession >>>> %s: BuildColorCorrector errored %d"
+ "<<<< VTPixelTransferSession >>>> %s: Can not use Metal and CPU scaling."
+ "<<<< VTPixelTransferSession >>>> %s: Can't reuse dynamic pixel transfer service, opening a new one"
+ "<<<< VTPixelTransferSession >>>> %s: Check SW transfer '%c%c%c%c' to '%c%c%c%c' flags(%u)"
+ "<<<< VTPixelTransferSession >>>> %s: Check dynamically registered transfer '%c%c%c%c' to '%c%c%c%c' flags(%u)"
+ "<<<< VTPixelTransferSession >>>> %s: Color processing Begin"
+ "<<<< VTPixelTransferSession >>>> %s: Color processing End"
+ "<<<< VTPixelTransferSession >>>> %s: Color processing stage %ld Matrix ( %2.4f, %2.4f, %2.4f,   %2.4f, %2.4f, %2.4f,   %2.4f, %2.4f, %2.4f  )"
+ "<<<< VTPixelTransferSession >>>> %s: Destination colorspace: %@"
+ "<<<< VTPixelTransferSession >>>> %s: Extra stage %ld CGColorNxMTransformStageCallback"
+ "<<<< VTPixelTransferSession >>>> %s: Failed VTSessionSetProperty for key %{public}@ value %{public}@"
+ "<<<< VTPixelTransferSession >>>> %s: Found a Metal blitter and sw scale '%c%c%c%c' to '%c%c%c%c' flags(%u)"
+ "<<<< VTPixelTransferSession >>>> %s: Found a Metal transfer '%c%c%c%c' to '%c%c%c%c' flags(%u)"
+ "<<<< VTPixelTransferSession >>>> %s: Found a dynamically registered transfer '%c%c%c%c' to '%c%c%c%c' flags(%u)"
+ "<<<< VTPixelTransferSession >>>> %s: Found a sw blitter transfer '%c%c%c%c' to '%c%c%c%c' flags(%u)"
+ "<<<< VTPixelTransferSession >>>> %s: Found a sw blitter, then sw scale '%c%c%c%c' to '%c%c%c%c' flags(%u)"
+ "<<<< VTPixelTransferSession >>>> %s: Found a sw scaler transfer '%c%c%c%c' to '%c%c%c%c' flags(%u)"
+ "<<<< VTPixelTransferSession >>>> %s: Invalid CVPixelBuffer. Pixelformat: %c%c%c%c BaseAddress: %p RowBytes: %zu DataSize: %zu."
+ "<<<< VTPixelTransferSession >>>> %s: Invalid CVPixelBuffer. Pixelformat: %c%c%c%c Plane: %zu BaseAddress: %p RowBytes: %zu PlaneSize: %zu."
+ "<<<< VTPixelTransferSession >>>> %s: Invalid dst rect fullHeight %d < (Height %d + top %d) for vImageConvert_420Yp8_CbCr8ToARGB8888()"
+ "<<<< VTPixelTransferSession >>>> %s: Invalid dst rect fullWidth %d < (Width %d + left %d) for vImageConvert_420Yp8_CbCr8ToARGB8888()"
+ "<<<< VTPixelTransferSession >>>> %s: Invalid dst rect left %d for vImageConvert_420Yp8_CbCr8ToARGB8888()"
+ "<<<< VTPixelTransferSession >>>> %s: Invalid dst rect top %d for vImageConvert_420Yp8_CbCr8ToARGB8888()"
+ "<<<< VTPixelTransferSession >>>> %s: Invalid src rect fullHeight %d < (Height %d + top %d) for vImageConvert_420Yp8_CbCr8ToARGB8888()"
+ "<<<< VTPixelTransferSession >>>> %s: Invalid src rect fullWidth %d < (Width %d + left %d) for vImageConvert_420Yp8_CbCr8ToARGB8888()"
+ "<<<< VTPixelTransferSession >>>> %s: Invalid src rect left %d for vImageConvert_420Yp8_CbCr8ToARGB8888()"
+ "<<<< VTPixelTransferSession >>>> %s: Invalid src rect top %d for vImageConvert_420Yp8_CbCr8ToARGB8888()"
+ "<<<< VTPixelTransferSession >>>> %s: No dynamic session found. Closing out old session (%p)."
+ "<<<< VTPixelTransferSession >>>> %s: Re-attempting VTPixelTransferGraphBuildChain with HW transfers disabled"
+ "<<<< VTPixelTransferSession >>>> %s: Re-attempting VTPixelTransferGraphBuildChain with Metal transfers disabled"
+ "<<<< VTPixelTransferSession >>>> %s: ReducedPrecisionFractionalOffsets is not available on current hardware."
+ "<<<< VTPixelTransferSession >>>> %s: Reusing dynamic pixel transfer service"
+ "<<<< VTPixelTransferSession >>>> %s: Searching: Can VT transfer '%c%c%c%c' to '%c%c%c%c' flags(%u)"
+ "<<<< VTPixelTransferSession >>>> %s: Source      colorspace: %@"
+ "<<<< VTPixelTransferSession >>>> %s: Stage %ld TRC %d: %lf %lf %lf %lf %lf %lf %lf"
+ "<<<< VTPixelTransferSession >>>> %s: Stage %ld kCGColorHLGLuminanceScaling"
+ "<<<< VTPixelTransferSession >>>> %s: VTPixelTransferChainDoTransfer failed"
+ "<<<< VTPixelTransferSession >>>> %s: VTPixelTransferSessionCreate failed to create a VTMetalTransferSessionCreate"
+ "<<<< VTPixelTransferSession >>>> %s: YCbCr->RGB transfer:%p RGB->YCbCr transfer:%p"
+ "<<<< VTPixelTransferSession >>>> %s: color corrector cannot do needed transfer from %c%c%c%c to %c%c%c%c"
+ "<<<< VTPixelTransferSession >>>> %s: dlopen(vImage) failed: \"%{public}s\""
+ "<<<< VTPixelTransferSession >>>> %s: invalid pixelAspectRatio hSpacing value. reseting to default 1"
+ "<<<< VTPixelTransferSession >>>> %s: invalid pixelAspectRatio vSpacing value. reseting to default 1"
+ "<<<< VTPixelTransferSession >>>> %s: rejecting bad clean aperture"
+ "<<<< VTPixelTransferSession >>>> %s: session: %p"
+ "<<<< VTPools >>>>"
+ "<<<< VTPools >>>> %s: Found existing record for sharingID %lld"
+ "<<<< VTPools >>>> %s: Found matched pool %p for sharingID %lld"
+ "<<<< VTPools >>>> %s: Found released pool while searching (sharingID %lld)"
+ "<<<< VTPools >>>> %s: No existing record for sharingID %lld so new one created"
+ "<<<< VTPools >>>> %s: No match so created pixelbufferpool %p for sharingID %lld"
+ "<<<< VTPools >>>> %s: No shared pool so removing the shareIDList entry for sharingID %lld as well"
+ "<<<< VTPools >>>> %s: Pixel buffer attributes failed to reconcile. Creating separate pixel buffer pools for codec and client.  codec pool %{public}@, format: %{public}@"
+ "<<<< VTPools >>>> %s: Set kCVPixelBufferIOSurfacePurgeableKey=true to reconciledAttributes"
+ "<<<< VTPools >>>> %s: Shared pool cleanup. Removing pool for sharingID %lld"
+ "<<<< VTPools >>>> %s: Unsupported CFType for poolSharingOption"
+ "<<<< VTPools >>>> %s: [Alpha-REORDER] first attributes: %{public}@"
+ "<<<< VTPools >>>> %s: [Alpha-REORDER] second attributes: %{public}@"
+ "<<<< VTPools >>>> %s: [REORDER] first attributes (after): %{public}@"
+ "<<<< VTPools >>>> %s: [REORDER] first attributes (before): %{public}@"
+ "<<<< VTPools >>>> %s: [REORDER] first attributes: %{public}@"
+ "<<<< VTPools >>>> %s: [REORDER] second attributes (after): %{public}@"
+ "<<<< VTPools >>>> %s: [REORDER] second attributes (before): %{public}@"
+ "<<<< VTPools >>>> %s: [REORDER] second attributes: %{public}@"
+ "<<<< VTPools >>>> %s: called"
+ "<<<< VTPools >>>> %s: choosing HTPC format %c%c%c%c by preference"
+ "<<<< VTPools >>>> %s: choosing interchange compressed format %c%c%c%c by preference"
+ "<<<< VTPools >>>> %s: client format: %{public}@"
+ "<<<< VTPools >>>> %s: first attributes: %{public}@"
+ "<<<< VTPools >>>> %s: interchange compressed format %c%c%c%c, skipping"
+ "<<<< VTPools >>>> %s: pixel buffer attributes reconciled: creating common pixel buffer pool %{public}@, format: %{public}@"
+ "<<<< VTPools >>>> %s: prioritizing alpha pixel formats"
+ "<<<< VTPools >>>> %s: second attributes: %{public}@"
+ "<<<< VTPools >>>> %s: vtCreateResolvedPixelBufferAttributesDictionary returned %d "
+ "<<<< VTPreprocessingSession >>>>"
+ "<<<< VTPreprocessingSession >>>> %s: %d frames still pending after calling VTVideoEncoderCompletePreprocessingFrames"
+ "<<<< VTPreprocessingSession >>>> %s: (%p/%p/%p): noErr but NULL imageBuffer"
+ "<<<< VTPreprocessingSession >>>> %s: Unsupported property key %@ (it's not in the SupportedPropertyDictionary)"
+ "<<<< VTPreprocessingSession >>>> %s: encoder emitted garbage/repeated resolution %p for frame %p"
+ "<<<< VTRateControlSession >>>>"
+ "<<<< VTRateControlSession >>>> %s: RateControlSession %p - Invalidate"
+ "<<<< VTRateControlSession >>>> %s: RateControlSession created: %p"
+ "<<<< VTRateControlSession >>>> %s: RateControlSession: %p - CompleteFrame"
+ "<<<< VTRateControlSession >>>> %s: RateControlSession: %p - EmitEncodeFrame [frame: %p sampleBuffer: %p status: %d rateControlFrameRefCon %p]"
+ "<<<< VTRateControlSession >>>> %s: RateControlSession: %p - EncodeFrame"
+ "<<<< VTRateControlSession >>>> %s: RateControlSession: %p - EncodeFrame callback"
+ "<<<< VTRateControlSession >>>> %s: RateControlSession: %p - PrapareToEncodeFrame"
+ "<<<< VTRateControlSession >>>> %s: VCPReactionObserverCreate failed."
+ "<<<< VTRateControlSession >>>> %s: VCPReactionObserverCreate is not available."
+ "<<<< VTRateControlSession >>>> %s: VCPReactionObserverCreate succeeded but observer is NULL."
+ "<<<< VTRateControlSession >>>> %s: dlopen(%s) failed: \"%s\""
+ "<<<< VTTemporalFilterSelection >>>>"
+ "<<<< VTTemporalFilterSelection >>>> %s: Capabilities found for %@"
+ "<<<< VTTemporalFilterSelection >>>> %s: ClassImplementationID in info is not a string"
+ "<<<< VTTemporalFilterSelection >>>> %s: Copy temporal filter list from server"
+ "<<<< VTTemporalFilterSelection >>>> %s: Did not meet IORegistry required key dependency"
+ "<<<< VTTemporalFilterSelection >>>> %s: Getting %@ key from %@ IORegitry Service for Temporal Filter Capabilities"
+ "<<<< VTTemporalFilterSelection >>>> %s: IORegistry required key (%@) found in Service %@"
+ "<<<< VTTemporalFilterSelection >>>> %s: IORegistry required key (%@) not found in Service %@"
+ "<<<< VTTemporalFilterSelection >>>> %s: IORegistry required key (%@) was not found in the list of services"
+ "<<<< VTTemporalFilterSelection >>>> %s: Invalid value '%@' found for kVTTemporalFilter_IORegistryCapabilitiesKey"
+ "<<<< VTTemporalFilterSelection >>>> %s: Invalid value '%@' found for kVTTemporalFilter_TemporalFilterCapabilities"
+ "<<<< VTTemporalFilterSelection >>>> %s: No capabilities found for %@"
+ "<<<< VTTemporalFilterSelection >>>> %s: VTTemporalFilterClass in matchInfo is not a string"
+ "<<<< VTTemporalFilterSelection >>>> %s: VTTemporalFilterClassName in info is not a string"
+ "<<<< VTTemporalFilterSelection >>>> %s: VTTemporalFilterName in info is not a string"
+ "<<<< VTTemporalFilterSelection >>>> %s: Will%s connect to videocodecd for temporal filtering -- thank you for setting \"ffctl CoreMedia/SeparateCodecProcess_TemporalFilter=%s\""
+ "<<<< VTTemporalFilterSelection >>>> %s: couldn't access path \"%s\""
+ "<<<< VTTemporalFilterSelection >>>> %s: found CMDependencies"
+ "<<<< VTTemporalFilterSelection >>>> %s: kVTTemporalFilter_IORegistryCapabilitiesKey found in CMMatchingInfo"
+ "<<<< VTTemporalFilterSelection >>>> %s: kVTTemporalFilter_TemporalFilterCapabilities found in CMMatchingInfo"
+ "<<<< VTTemporalFilterSelection >>>> %s: rejecting temporal filter %p --  class aint a CFString"
+ "<<<< VTTemporalFilterSelection >>>> %s: temporal filter created with filter class\":%@\", encoderID \"%@\""
+ "<<<< VTTemporalFilterSession >>>>"
+ "<<<< VTTemporalFilterSession >>>> %s: Checking Pool compatibility with Pixel Buffer Attributes"
+ "<<<< VTTemporalFilterSession >>>> %s: Checking compatibility: %@, %@"
+ "<<<< VTTemporalFilterSession >>>> %s: Client set output pool is used as filter output pixel buffer pool"
+ "<<<< VTTemporalFilterSession >>>> %s: Client set output pool is used as session output pixel buffer pool"
+ "<<<< VTTemporalFilterSession >>>> %s: Compatibility check failed with error: %d"
+ "<<<< VTTemporalFilterSession >>>> %s: Copy Pixel Buffer for Filter Input"
+ "<<<< VTTemporalFilterSession >>>> %s: Copy Pixel Buffer for Filter Output"
+ "<<<< VTTemporalFilterSession >>>> %s: Created session %p"
+ "<<<< VTTemporalFilterSession >>>> %s: Creating input pixel transfer session"
+ "<<<< VTTemporalFilterSession >>>> %s: Creating output pixel transfer session"
+ "<<<< VTTemporalFilterSession >>>> %s: Creating session"
+ "<<<< VTTemporalFilterSession >>>> %s: Discarding unsupported property key %@"
+ "<<<< VTTemporalFilterSession >>>> %s: Invalidating session %p"
+ "<<<< VTTemporalFilterSession >>>> %s: Output Pixel Buffer Pool has been set by the client"
+ "<<<< VTTemporalFilterSession >>>> %s: Sending client set output pixel buffer: session (%p), pluginSession (%p), clientOutputPixelBuffer (%p)"
+ "<<<< VTTemporalFilterSession >>>> %s: Unsupported property key %@ (it's not in the SupportedPropertyDictionary)"
+ "<<<< VTTemporalFilterSession >>>> %s: Will%s connect to videocodecd for temporal filtering -- thank you for setting \"ffctl CoreMedia/SeparateCodecProcess_TemporalFilter=%s\""
+ "<<<< VTTemporalFilterSession >>>> %s: flush pending frames"
+ "<<<< VTTemporalFilterSession >>>> %s: kVTTemporalFilterPropertyKey_OutputPixelBufferPool is not supported in RPC"
+ "<<<< VTTemporalFilterSession >>>> %s: not supported for paravirtualization host temporal filter plugins -- temporal filter plugins must call VTTemporalFilterPluginSessionCreateOutputPixelBuffer instead"
+ "<<<< VTTemporalFilterSession >>>> %s: temporal filter plugin handled CopyProperty for %@ (err %d)"
+ "<<<< VTTemporalFilterSession >>>> %s: temporal filter plugin handled SetProperty for %@ (err %d)"
+ "<<<< VTTemporalFilterSession >>>> %s: transferring input pixel buffer from type %c%c%c%c to %c%c%c%c"
+ "<<<< VTTemporalFilterSession >>>> %s: transferring output pixel buffer from type %c%c%c%c to %c%c%c%c"
+ "<<<< VTTemporalFilterSession >>>> %s: video toolbox handled CopyProperty for %@"
+ "<<<< VTTemporalFilterSession >>>> %s: video toolbox handled SetProperty for %@"
+ "<<<< VTTemporalNoiseFilterImplementation >>>>"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: (%p) Completed frame processing. PTS: %f, error: %@"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: (%p) Emitted frame was not found in pending frame list: pendingFrame: %p, PTS: %f"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: (%p) Failed to complete frame: emittedPixelBuffer: %p, PTS: %f"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: (%p) Failed to emit frame: pendingFrame: %p, PTS: %f, err; %d"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: (%p) Failed with error: %d"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: (%p) Pending frame (%p): PTS: %f, frameEmitted: %d"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: (%p) called"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: (%p) called on MCTF session (%p) with filterStrength: (%d)"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: (%p) called with params: (%p)"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: (%p) called with pixelBuffer: (%p), presentationTimestamp: (%f)"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: (%p) called with pixelBuffer: (%p), presentationTimestamp: (%f), processedWithDestinationFrame: (%d)"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: (%p) failed with error: %d"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: (%p) flush pending frames"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: (%p) input parameters validation failed with error: %d"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: (%p) nextFrame: (%p), PTS: (%f)"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: (%p) previousFrame: (%p), PTS: (%f)"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: (%p) sourceFrame: (%p), PTS: (%f)"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: Discontinuity found: %@"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: Failed to load instance properties: (%d)"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: Skipping since the reference frame has been already processed and emitted."
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: VTCopyTemporalFilterList() failed (%d)\n"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: Will %s connect to videocodecd for temporal filtering -- thank you for setting \"ffctl CoreMedia/SeparateCodecProcess_TemporalFilter=%s\""
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: discontinuity flag is set"
+ "<<<< VTTemporalNoiseFilterImplementation >>>> %s: loading capabilities"
+ "<<<< VTTileCompressionSession >>>>"
+ "<<<< VTTileCompressionSession >>>> %s: Discarding unsupported property key %@"
+ "<<<< VTTileCompressionSession >>>> %s: Encoder handled CopyProperty %@  value: %@ "
+ "<<<< VTTileCompressionSession >>>> %s: Encoder handled SetProperty %@  value: %@ "
+ "<<<< VTTileCompressionSession >>>> %s: Unsupported property key %@ (it's not in the SupportedPropertyDictionary)"
+ "<<<< VTTileCompressionSession >>>> %s: VTVideoEncoderStartTileSession failed - err: %d.  will look for another encoder."
+ "<<<< VTTileCompressionSession >>>> %s: VideoToolbox handled CopyProperty %@  value: %@ "
+ "<<<< VTTileCompressionSession >>>> %s: VideoToolbox handled SetProperty %@  value: %@ "
+ "<<<< VTTileCompressionSession >>>> %s: adding client tile %p (encoder tile %p) to pending list"
+ "<<<< VTTileCompressionSession >>>> %s: found no tile info for encoder tile %p in pending tile list"
+ "<<<< VTTileCompressionSession >>>> %s: pending tile list not empty after VTTileCompressionSessionInvalidate"
+ "<<<< VTTileCompressionSession >>>> %s: received updated tile requirements: canvas attributes: %@  tile requirements: %@ "
+ "<<<< VTTileCompressionSession >>>> %s: removing client tile %p (encoder tile %p) from pending list"
+ "<<<< VTTileDecompressionSession >>>>"
+ "<<<< VTTileDecompressionSession >>>> %s:  Created %p [remote %p]"
+ "<<<< VTTileDecompressionSession >>>> %s: %@ adding client tile %p (decoder tile %p) to pending list"
+ "<<<< VTTileDecompressionSession >>>> %s: %@ decode tile offset[%d,%d] dimensions[%dx%d] into imageBuffer %p at offset [%d, %d]"
+ "<<<< VTTileDecompressionSession >>>> %s: %@ emit tile offset[%d,%d] dimensions[%dx%d] into imageBuffer %p at offset [%d, %d] error: %d"
+ "<<<< VTTileDecompressionSession >>>> %s: %@ removing client tile %p (decoder tile %p) from pending list"
+ "<<<< VTTileDecompressionSession >>>> %s: Created %@"
+ "<<<< VTTileDecompressionSession >>>> %s: Decoder handled CopyProperty %@  value: %@ "
+ "<<<< VTTileDecompressionSession >>>> %s: Decoder handled SetProperty %@  value: %@ "
+ "<<<< VTTileDecompressionSession >>>> %s: Discarding unsupported property key %@"
+ "<<<< VTTileDecompressionSession >>>> %s: Finalizing %p"
+ "<<<< VTTileDecompressionSession >>>> %s: Invalidating %@"
+ "<<<< VTTileDecompressionSession >>>> %s: Unsupported property key %@ (it's not in the SupportedPropertyDictionary)"
+ "<<<< VTTileDecompressionSession >>>> %s: VTVideoDecoderStartTileSession failed - err: %d.  will look for another decoder."
+ "<<<< VTTileDecompressionSession >>>> %s: VideoToolbox handled CopyProperty %@  value: %@ "
+ "<<<< VTTileDecompressionSession >>>> %s: VideoToolbox handled SetProperty %@  value: %@ "
+ "<<<< VTTileDecompressionSession >>>> %s: found no tile info for decoder tile %p in pending tile list"
+ "<<<< VTTileDecompressionSession >>>> %s: pending tile list not empty after VTTileDecompressionSessionInvalidate"
+ "<<<< VTTileDecompressionSession >>>> %s: received updated tile requirements: canvas attributes: %@  tile requirements: %@ "
+ "<<<< VTTileDecompressionSession >>>> %s: unsupported kVTDecompressionPropertyKey_PixelBufferPool request for VTTileDecompressionSession"
+ "<<<< VTTransferService >>>>"
+ "<<<< VTTransferService >>>> %s: Fill unspecified color properties with 709 due to convert10BitHDRToSDRFor8BitDestinationWithUnspecifiedColorProperties: srcBitsPerComponent: %d, destBitsPerComponent: %d"
+ "<<<< VTTransferService >>>> %s: attached CGColorSpace %s session color space: %@ vs %@"
+ "<<<< VTTransferService >>>> %s: simple ColorPrimaries mismatch: %@ vs %@"
+ "<<<< VTTransferService >>>> %s: simple ICCProfile mismatch: %@ vs %@"
+ "<<<< VTTransferService >>>> %s: simple TransferFunction mismatch: %@ vs %@"
+ "<<<< VTTransferService >>>> %s: simple YCbCrMatrix mismatch: %@ vs %@"
+ "<<<< VTTransferService >>>> %s: vImageConverter_CreateWithCGColorConversionInfo failed with %d"
+ "<<<< VTVDCapabilites >>>>"
+ "<<<< VTVDCapabilites >>>> %s: Failed to copy codec capabilities from the host for codecType '%c%c%c%c', err %d"
+ "<<<< VTVDCapabilites >>>> %s: I don't currently know how to create a decoder capabilities dictionary for codec type %c%c%c%c"
+ "<<<< VTVDCapabilites >>>> %s: NULL profileNumberKey"
+ "<<<< VTVDCapabilites >>>> %s: NULL profileSupportDict"
+ "<<<< VTVDCapabilites >>>> %s: No max decodable value - assume everything is decodable"
+ "<<<< VTVDCapabilites >>>> %s: No max playable value - assume decodable and playable are the same"
+ "<<<< VTVDCapabilites >>>> %s: ProRes codecType not found in MediaValidator"
+ "<<<< VTVDCapabilites >>>> %s: Unable to get doViProfilesArray and/or doViProfilesDict"
+ "<<<< VTVDCapabilites >>>> %s: Unable to get profilesArray and/or codecProfilesDict for %@"
+ "<<<< VTVDCapabilites >>>> %s: Unable to get validatorProfilesArray and/or validatorAV1Dict for av01"
+ "<<<< VTVDCapabilites >>>> %s: begin, codecType '%c%c%c%c'"
+ "<<<< VTVDCapabilites >>>> %s: codec %@ not found in MediaValidator plist"
+ "<<<< VTVDCapabilites >>>> %s: couldn't create profile %@ support dictionary"
+ "<<<< VTVDCapabilites >>>> %s: couldn't create profiles array"
+ "<<<< VTVDCapabilites >>>> %s: decoderCapabilities is NULL for codecType %c%c%c%c"
+ "<<<< VTVDCapabilites >>>> %s: err %d, guestProtocolVersion %d, hostProtocolVersion %d"
+ "<<<< VTVDCapabilites >>>> %s: inContext can't be NULL"
+ "<<<< VTVDCapabilites >>>> %s: level is %d - max decodable level is %d "
+ "<<<< VTVDCapabilites >>>> %s: level is %d - max playable level is %d "
+ "<<<< VTVDCapabilites >>>> %s: no MediaValidator data found"
+ "<<<< VTVDCapabilites >>>> %s: no ProRes decoder registered for codec type"
+ "<<<< VTVDCapabilites >>>> %s: no SupportedLevels array found"
+ "<<<< VTVDCapabilites >>>> %s: no SupportedProfiles array found"
+ "<<<< VTVDCapabilites >>>> %s: no VideoCodecProfiles entry"
+ "<<<< VTVDCapabilites >>>> %s: profile %d is in supported list, but no per-profile details.  Assume all levels are playable"
+ "<<<< VTVDCapabilites >>>> %s: profile %d is in supported list, but the per-profile details dont list it.  Assume all levels are playable"
+ "<<<< VTVDCapabilites >>>> %s: value can't be NULL"
+ "<<<< VTVideoDecoderLoader >>>> %s:  did not find entry point %s of dylib %s"
+ "<<<< VTVideoDecoderLoader >>>> %s: calling entry point %s of dylib %s"
+ "<<<< VTVideoDecoderLoader >>>> %s: did not find dylib %s - %s"
+ "<<<< VTVideoDecoderLoader >>>> %s: done"
+ "<<<< VTVideoDecoderSelection >>>>"
+ "<<<< VTVideoDecoderSelection >>>> %s: %c%c%c%c (%zd bytes) guestUUID %@"
+ "<<<< VTVideoDecoderSelection >>>> %s: '%c%c%c%c' not allowed in VideoDecoderSpecification dict"
+ "<<<< VTVideoDecoderSelection >>>> %s: Calling VTLoadVideoDecoders..."
+ "<<<< VTVideoDecoderSelection >>>> %s: Calling vtLoadBuiltinVideoDecoders..."
+ "<<<< VTVideoDecoderSelection >>>> %s: ClassImplementationID in info is not a string"
+ "<<<< VTVideoDecoderSelection >>>> %s: CodecType in matchInfo is not a string or array, skipping item"
+ "<<<< VTVideoDecoderSelection >>>> %s: VTRestrictions applied to disallow the use of codecType %@ "
+ "<<<< VTVideoDecoderSelection >>>> %s: VTRestrictions applied to disallow the use of hardware decoders %@ "
+ "<<<< VTVideoDecoderSelection >>>> %s: appending %@: rating %d, name %@, decoderID %@ ioRegistryDict %@"
+ "<<<< VTVideoDecoderSelection >>>> %s: appending %@: rating %d, name %@, decoderID %@ ioRegistryDict %@ isPreferredInternalPlugin %s"
+ "<<<< VTVideoDecoderSelection >>>> %s: begin"
+ "<<<< VTVideoDecoderSelection >>>> %s: called to re-load paravirtualized video decoders"
+ "<<<< VTVideoDecoderSelection >>>> %s: codecType %c%c%c%c, createMethod %p, infoDict %@"
+ "<<<< VTVideoDecoderSelection >>>> %s: codecType =  %c%c%c%c "
+ "<<<< VTVideoDecoderSelection >>>> %s: err %d, guestProtocolVersion %d, hostProtocolVersion %d"
+ "<<<< VTVideoDecoderSelection >>>> %s: index = %d: %@"
+ "<<<< VTVideoDecoderSelection >>>> %s: no video decoder accepted for '%c%c%c%c'"
+ "<<<< VTVideoDecoderSelection >>>> %s: no video decoder available for '%c%c%c%c'"
+ "<<<< VTVideoDecoderSelection >>>> %s: no video decoder available for '%c%c%c%c' (requireHardware)"
+ "<<<< VTVideoDecoderSelection >>>> %s: no video decoder available for '%c%c%c%c' for required ID %@ "
+ "<<<< VTVideoDecoderSelection >>>> %s: no video decoder found for '%c%c%c%c'"
+ "<<<< VTVideoDecoderSelection >>>> %s: registering paravirtualized decoder for %@ (%@ / %@)"
+ "<<<< VTVideoDecoderSelection >>>> %s: registryItems {"
+ "<<<< VTVideoDecoderSelection >>>> %s: rejecting decoder %p -- cannot interpret CodecType"
+ "<<<< VTVideoDecoderSelection >>>> %s: rejecting decoder %p -- not hardware accelerated"
+ "<<<< VTVideoDecoderSelection >>>> %s: skipping HW accelerated non-paravirtualized codec"
+ "<<<< VTVideoDecoderSelection >>>> %s: skipping SW AV1"
+ "<<<< VTVideoDecoderSelection >>>> %s: skipping SW AV1 as EnableAppleOnlySWAV1 opt-in option not specified"
+ "<<<< VTVideoDecoderSelection >>>> %s: skipping appending %c%c%c%c -- protected"
+ "<<<< VTVideoDecoderSelection >>>> %s: skipping non-paravirtualized decoder because RequireParavirtualizedDecoder is true."
+ "<<<< VTVideoDecoderSelection >>>> %s: skipping paravirtualized decoder as instructed"
+ "<<<< VTVideoDecoderSelection >>>> %s: the decoder exceeds the max layer of wrapper of wrapper"
+ "<<<< VTVideoDecoderSelection >>>> %s: video decoder [%d %p] failed to open (err %d) for '%c%c%c%c'"
+ "<<<< VTVideoDecoderSelection >>>> %s: video decoder created with codecType '%c%c%c%c', decoderID \"%@\", decoderName \"%@\""
+ "<<<< VTVideoDecoderSelection >>>> %s: videoDecoderSpecification2 = %@"
+ "<<<< VTVideoDecoderSelection >>>> %s: will look for internal bundles first.  thanks for setting \"defaults write com.apple.coremedia prefer_internal_codecs -bool YES\")"
+ "<<<< VTVideoDecoderSelection >>>> %s: }"
+ "<<<< VTVideoEncoderLoader >>>> %s:  did not find entry point %s of dylib %s"
+ "<<<< VTVideoEncoderLoader >>>> %s: calling entry point %s of dylib %s"
+ "<<<< VTVideoEncoderLoader >>>> %s: did not find dylib %s - %s"
+ "<<<< VTVideoEncoderLoader >>>> %s: done"
+ "<<<< VTVideoEncoderSelection >>>>"
+ "<<<< VTVideoEncoderSelection >>>> %s: %c%c%c%c (%zd bytes) guestUUID %@"
+ "<<<< VTVideoEncoderSelection >>>> %s: %d encoders share encoderID %@ -- picking the first I found"
+ "<<<< VTVideoEncoderSelection >>>> %s: ClassImplementationID in info is not a string"
+ "<<<< VTVideoEncoderSelection >>>> %s: CodecType in matchInfo is not a string"
+ "<<<< VTVideoEncoderSelection >>>> %s: VTCodecName in info is not a string"
+ "<<<< VTVideoEncoderSelection >>>> %s: VTEncoderName in info is not a string"
+ "<<<< VTVideoEncoderSelection >>>> %s: VTRestrictions applied to disallow the use of hardware encoders %@ "
+ "<<<< VTVideoEncoderSelection >>>> %s: appending %c%c%c%c: rating %d, name %@, encoderID %@"
+ "<<<< VTVideoEncoderSelection >>>> %s: begin"
+ "<<<< VTVideoEncoderSelection >>>> %s: called to re-load paravirtualized video encoders"
+ "<<<< VTVideoEncoderSelection >>>> %s: codecType %c%c%c%c, createMethod %p, infoDict %@"
+ "<<<< VTVideoEncoderSelection >>>> %s: err %d, guestProtocolVersion %d, hostProtocolVersion %d"
+ "<<<< VTVideoEncoderSelection >>>> %s: no video encoder accepted for '%c%c%c%c'\n"
+ "<<<< VTVideoEncoderSelection >>>> %s: no video encoder available for '%c%c%c%c'"
+ "<<<< VTVideoEncoderSelection >>>> %s: no video encoder available for '%c%c%c%c' (requireHardware)"
+ "<<<< VTVideoEncoderSelection >>>> %s: no video encoder available for '%c%c%c%c' for required ID %@ "
+ "<<<< VTVideoEncoderSelection >>>> %s: no video encoder found for '%c%c%c%c'\n"
+ "<<<< VTVideoEncoderSelection >>>> %s: registering paravirtualized encoder for %c%c%c%c (%@ / %@)"
+ "<<<< VTVideoEncoderSelection >>>> %s: rejecting encoder %p --  CodecType aint a CFString"
+ "<<<< VTVideoEncoderSelection >>>> %s: rejecting encoder %p -- not compatible with profile"
+ "<<<< VTVideoEncoderSelection >>>> %s: skipping HW accelerated non-paravirtualized codec"
+ "<<<< VTVideoEncoderSelection >>>> %s: skipping SW AV1 as EnableAppleOnlySWAV1 opt-in option is not specified"
+ "<<<< VTVideoEncoderSelection >>>> %s: skipping non-paravirtualized encoder because RequireParavirtualizedEncoder is set to true."
+ "<<<< VTVideoEncoderSelection >>>> %s: skipping paravirtualized encoder as instructed"
+ "<<<< VTVideoEncoderSelection >>>> %s: skipping restricted SW AV1"
+ "<<<< VTVideoEncoderSelection >>>> %s: unexpected value in profile array: %d"
+ "<<<< VTVideoEncoderSelection >>>> %s: video encoder [%d %p %p] failed to open for '%c%c%c%c'"
+ "<<<< VTVideoEncoderSelection >>>> %s: video encoder created with codecType '%c%c%c%c', encoderID \"%@\", encoderName \"%@\""
+ "<<<< VTVideoEncoderSelection >>>> %s: will look for internal bundles first.  thanks for setting \"defaults write com.apple.coremedia prefer_internal_codecs -bool YES\")"
+ "<<<< VTVideoProcessingParavirtualization >>>> %s: codecType=%c%c%c%c"
+ "<<<< VideoCodecServiceUtil >>>> %s: Client/Server tile decompression session will not prefer MIG -- thank you for setting \"defaults write com.apple.coremedia tile_decompression_session_prefers_mig -bool no\""
+ "<<<< VideoCodecServiceUtil >>>> %s: Will NOT connect to videocodecd for encode -- thank you for setting \"ffctl CoreMedia/SeparateCodecProcess_Encode=off\""
+ "<<<< VideoCodecServiceUtil >>>> %s: Will NOT connect to videocodecd for encode -- thank you for setting \"ffctl CoreMedia/SeparateCodecProcess_Encode_OnHomePod=off\""
+ "<<<< VideoCodecServiceUtil >>>> %s: Will connect to videocodecd for encode -- thank you for setting \"ffctl CoreMedia/SeparateCodecProcess_Encode_OnHomePod=on\""
+ "<<<< VideoCodecServiceUtil >>>> %s: Will use %s interface for remote decompression session -- thank you for setting \"ffctl CoreMedia/SeparateCodecProcess_MIGDecode=%s\""
+ "<<<< VideoCodecServiceUtil >>>> %s: Will use %s interface for remote decompression session as set by default value of feature flag CoreMedia/SeparateCodecProcess_MIGDecode=%s"
+ "<<<< VideoCodecServiceUtil >>>> %s: Will%s connect to videocodecd -- thank you for setting \"ffctl CoreMedia/SeparateCodecProcess=%s\""
+ "<<<< VideoCodecServiceUtil >>>> %s: Will%s connect to videocodecd as set by default value of feature flag CoreMedia/SeparateCodecProcess=%s"
+ "<<<< VideoCodecServiceUtil >>>> %s: Will%s connect to videocodecd for encode -- thank you for setting \"ffctl CoreMedia/SeparateCodecProcess_Encode=%s\""
+ "<<<< VideoCodecServiceUtil >>>> %s: device name is %@"
+ "<<<< VideoCodecServiceUtil >>>> %s: mediaplaybackd will%s use OOP decode -- thank you for setting \"ffctl CoreMedia/MediaplaybackdUseOutOfProcessDecode=%s\""
+ "<<<< VideoCodecServiceUtil >>>> %s: mediaplaybackd will%s use OOP decode as set by default value of feature flag CoreMedia/MediaplaybackdUseOutOfProcessDecode=%s"
+ "<ColorOptimizedBlitter>"
+ "<ParavirtualizedMotionEstimationProcessor %p UUID %02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x>"
+ "<VTMotionEstimationSession %p [%p]>{\n"
+ "=32p box wrong size"
+ "=32s box wrong size"
+ "=dat box too short"
+ "=fds box too short"
+ "=s32 box wrong length"
+ "=s64 box wrong length"
+ "=sbf box too short"
+ "=tc+ box too short"
+ "=tim box wrong size"
+ "=u32 box wrong length"
+ "=ui+ box length invalid"
+ "=ui+ box too short"
+ "=uui box wrong length"
+ "=vdi box wrong size"
+ "@\"<MTLDevice>\""
+ "@\"<VTFrameProcessorConfiguration>\""
+ "@\"<VTFrameProcessorImplementationPrivate>\""
+ "@\"MTLSharedEventListener\""
+ "@\"NSArray\""
+ "@\"NSArray\"16@0:8"
+ "@\"NSDictionary\""
+ "@\"NSDictionary\"16@0:8"
+ "@\"NSMutableArray\""
+ "@\"NSObject<OS_dispatch_group>\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"NSString\"16@0:8"
+ "@\"VCPFrameSuperResolutionConfiguration\""
+ "@\"VCPFrameSuperResolutionProcessor\""
+ "@\"VCPVideoInterpolationConfiguration\""
+ "@\"VCPVideoInterpolationSession\""
+ "@\"VEFrame\""
+ "@\"VEFrameOpticalFlow\""
+ "@\"VEFrameProcessor\""
+ "@\"VEFrameRateConversionConfiguration\""
+ "@\"VEFrameRateConversionParameters\""
+ "@\"VEMotionBlurConfiguration\""
+ "@\"VEMotionBlurParameters\""
+ "@\"VEOpticalFlowConfiguration\""
+ "@\"VEOpticalFlowParameters\""
+ "@\"VESuperResolutionConfiguration\""
+ "@\"VESuperResolutionParameters\""
+ "@\"VTFrameProcessorFrame\""
+ "@\"VTFrameProcessorFrame\"16@0:8"
+ "@\"VTFrameProcessorOpticalFlow\""
+ "@\"VTTemporalNoiseFilterConfiguration\""
+ "@16@0:8"
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@32@0:8@16@24"
+ "@32@0:8^{__CVBuffer=}16^{__CVBuffer=}24"
+ "@32@0:8q16q24"
+ "@36@0:8q16q24f32"
+ "@40@0:8:16@24@32"
+ "@40@0:8q16q24q32"
+ "@48@0:8@16@24@32@40"
+ "@48@0:8@16@24q32@40"
+ "@48@0:8^{__CVBuffer=}16{?=qiIq}24"
+ "@48@0:8q16q24q32q40"
+ "@52@0:8q16q24B32q36q44"
+ "@56@0:8@16@24@32@40f48C52"
+ "@64@0:8@16@24@32@40q48@56"
+ "@68@0:8q16q24q32q40B48q52q60"
+ "@80@0:8@16@24@32@40@48q56q64@72"
+ "A pixel format with a specific color component range was requested, but the encoder doesn't support it."
+ "ALWAYS"
+ "AV1RegisterEncoder"
+ "Allocation failed"
+ "AllowClientProcessEstimate"
+ "AllowOnePassMetalScaling"
+ "AlphaChannelMode set to NULL after a frame was already encoded -- don't do that"
+ "AmbientViewingEnvironment not 8 bytes"
+ "AmbientViewingEnvironment not data"
+ "AppleJPEG decoding failed!"
+ "AppleJPEGVideoDecoder.c"
+ "AppleJPEGVideoDecoder_CopyProperty"
+ "AppleJPEGVideoDecoder_CopySupportedPropertyDictionary"
+ "AppleJPEGVideoDecoder_CreateInstance"
+ "AppleJPEGVideoDecoder_DecodeFrame"
+ "AppleJPEGVideoDecoder_SetProperty"
+ "ApplicationDefined"
+ "Auxiliary type info should be a string."
+ "B"
+ "B16@0:8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "B32@0:8@\"<VTFrameProcessorConfiguration>\"16^@24"
+ "B32@0:8@\"<VTFrameProcessorParameters>\"16^@24"
+ "B32@0:8@16^@24"
+ "B40@0:8@16@?24^@32"
+ "Bad poolAttributesOut"
+ "Bad poolName parameter"
+ "Balanced"
+ "BaselineValue should be a CFNumber"
+ "Block_copy failed"
+ "BorderBottom"
+ "BorderLeft"
+ "BorderPixelBufferAttributes"
+ "BorderPixels"
+ "BorderRight"
+ "BorderTop"
+ "BoundingBoxes"
+ "C"
+ "C16@0:8"
+ "CFArrayCreate failed"
+ "CFArrayCreateCopy failed"
+ "CFArrayCreateMutable failed"
+ "CFArrayCreateMutable failed for array"
+ "CFArrayCreateMutable failed for ioSurfaceMappingIDArray"
+ "CFArrayCreateMutable failed for pixelBufferArray"
+ "CFArrayCreateMutable failed for pixelBufferUUIDArray"
+ "CFArrayCreateMutable failed for tagCollectionArray"
+ "CFArrayCreateMutable for sharedPoolArray failed"
+ "CFDataCreate failed"
+ "CFDataCreateMutable failed"
+ "CFDataCreateMutable failed for tagCollectionAsCFData"
+ "CFDataCreateMutableCopy failed"
+ "CFDictionaryCreate failed"
+ "CFDictionaryCreate failed (once)"
+ "CFDictionaryCreate readWritePropertiesDict failed"
+ "CFDictionaryCreateMutable failed"
+ "CFDictionaryCreateMutable failed for dictionary"
+ "CFDictionaryCreateMutable failed for pendingFramePixelBuffers"
+ "CFDictionaryCreateMutable failed for pendingTilePixelBuffers"
+ "CFDictionaryCreateMutable failed for uuidToVTParavirtualizationHostDecoderSession"
+ "CFDictionaryCreateMutable failed for uuidToVTParavirtualizationHostEncoderSession"
+ "CFDictionaryCreateMutable failed for uuidToVTParavirtualizationHostMotionEstimationProcessorSession"
+ "CFDictionaryCreateMutableCopy failed"
+ "CFNumberCreate failed"
+ "CFStringCreateWithBytes failed"
+ "CFStringCreateWithFormat failed"
+ "CFURLCopyAbsoluteURL failed for absoluteURL"
+ "CFURLGetString failed"
+ "CFUUIDCreateFromUUIDBytes failed"
+ "CGImage creation failed"
+ "CMBlockBufferCreateContiguous failed"
+ "CMBlockBufferGetDataPointer failed"
+ "CMDerivedObjectCreate failed"
+ "CMPhotoParavirtualizedHostJPEGHardwareCopyCapabilities"
+ "CMPhotoParavirtualizedHostJPEGHardwareDecode"
+ "CMPhotoParavirtualizedHostJPEGHardwareEncode"
+ "CMTaggedBufferGroupCreate failed"
+ "CVMetalTextureCacheCreate failed"
+ "CVPixelBufferPoolCreate failed (trying to create non-reconciled client pool)"
+ "CVPixelBufferPoolCreate failed (trying to create non-reconciled codec pool)"
+ "CVPixelBufferPoolCreate failed (trying to create reconciled pool)"
+ "CVPixelBufferPoolCreatePixelBuffer error"
+ "CVPixelBufferPoolCreatePixelBuffer failed"
+ "CVPixelBufferPoolCreatePixelBuffer returned an error"
+ "CVPixelFormatDescriptionGetDescriptionWithPixelFormatType failed"
+ "CameraCalibrationDataLensCollection"
+ "CameraCalibrationDataLensCollection should be a CFArray"
+ "CameraCalibrationDataLensCollection should include IntrinsicMatrix"
+ "CameraCalibrationDataLensCollection should include IntrinsicMatrixReferenceDimensions"
+ "CameraCalibrationDataLensCollection should include LensAlgorithmKind"
+ "CameraCalibrationDataLensCollection should include LensDomain"
+ "CameraCalibrationDataLensCollection should include LensIdentifier"
+ "CameraCalibrationDataLensCollection should include LensRole"
+ "CameraCalibrationDataLensCollection should include a CFDictionary"
+ "Can't find callbacks for this -- is it really a VT session?"
+ "Cannot allocate buffer from pool but no error observed."
+ "Cannot conform a buffer without specifying the destination conformedBufferOut param"
+ "Cannot create pixel format description from pixelFormat"
+ "Cannot load vcp lib"
+ "ChromaLocation not recognised"
+ "CleanAperture not a dictionary"
+ "Client requested confidence value, but the processor doesn't acknowledge supporting it."
+ "Color"
+ "ColorPrimaries "
+ "ColorPrimaries not recognised"
+ "Compositor limited to  BGRA, l10r, RGhA, RGfA"
+ "Compression Session was NULL"
+ "CompressionOutputCallback"
+ "Connection refcon is already set. This is a redundant attempt to establish pixel buffer origin connection."
+ "ConstantQualityFactor"
+ "ContentLightLevelInfo not 4 bytes"
+ "ContentLightLevelInfo not data"
+ "Could not allocate common memory pool"
+ "Could not allocate memory pool CMBlockBuffer"
+ "Could not create VTHDRImageStatisticsGenerationSessionCreate"
+ "Could not create VTParavirtualizationHostDecoderSession"
+ "Could not create VTParavirtualizationHostEncoderSession"
+ "Could not create VTParavirtualizationHostMotionEstimationProcessorSession"
+ "Could not create VTParavirtualizationHostSession"
+ "Could not create VTParavirtualizationReplyClerk"
+ "Could not generate histgram likely due to an invalid configuration"
+ "Could not select and open decoder instance"
+ "Could not select and open encoder instance"
+ "Creating an array after the start."
+ "Creating motion vector pixel buffer pool failed"
+ "CurrentHDRMetadataGenerationState"
+ "DISABLED"
+ "DOES match"
+ "DecodeACRefine"
+ "DecodeBlocks"
+ "Decoded pixel buffer has no value for critical attribute"
+ "DecompressionMultiImageOutputCallback"
+ "DecompressionOutputCallback"
+ "DecompressionSessionMessageQueue create failed"
+ "DeghostingPriority"
+ "DepthWrapperDecoder.c"
+ "DepthWrapperDecoder_CreateInstance"
+ "DepthWrapperDecoder_DecodeFrame"
+ "DepthWrapperDecoder_FinishDelayedFrames"
+ "DepthWrapperDecoder_SetProperty"
+ "DepthWrapperDecoder_StartSession"
+ "DepthWrapperEncoder.c"
+ "DepthWrapperEncoder_CompleteFrames"
+ "DepthWrapperEncoder_CopyProperty"
+ "DepthWrapperEncoder_CreateInstance"
+ "DepthWrapperEncoder_EncodeFrame"
+ "DepthWrapperEncoder_EncodeFrame_block_invoke"
+ "DepthWrapperEncoder_Finalize"
+ "DepthWrapperEncoder_SetProperty"
+ "DepthWrapperEncoder_StartSession"
+ "Destination crop rect has negative offset."
+ "Destination crop rect is larger than entire dimensions."
+ "Destination pixelFormat changed."
+ "Dictionary Ref was NULL"
+ "Dictionary allocation failed"
+ "DisparityAdjustment should be a CFNumber"
+ "DoNothing"
+ "DoVi metadata compression not supported"
+ "DolbyMetadataVersionKey must be 3 or 4"
+ "DolbyStatistics"
+ "DolbyVisionDecoder.c"
+ "DolbyVisionDecoder_CopySupportedPropertyDictionary"
+ "DolbyVisionDecoder_CreateInstance"
+ "DolbyVisionDecoder_DecodeFrame"
+ "DolbyVisionDecoder_Invalidate"
+ "DolbyVisionDecoder_SetProperty"
+ "Dovi Enhancement layer not supported"
+ "ENABLED"
+ "Emitted buffer is empty"
+ "EnableBlurFilter"
+ "EnableUserQPMap"
+ "EncodeFrame but MVHEVCVideoLayerIDs property was set"
+ "EncodeMultiImageFrame but MVHEVCVideoLayerIDs property was not set"
+ "EncodeMultiImageFrame but taggedBufferGroup NULL"
+ "EncoderEncryptionKeyID"
+ "Equirectangular"
+ "Error creating processFrameQueue"
+ "Error in init: Create device"
+ "Event link already configured"
+ "Expect BeginPass/EndPass pairs"
+ "ExtrinsicOrientationQuaternion"
+ "ExtrinsicOriginSource"
+ "FALSE"
+ "Fail to allocate OpaqueVTTemporalNoiseFilterInternal"
+ "Fail to create effect configuration"
+ "Fail to initialize"
+ "Failed allocating dictionary"
+ "Failed allocating number"
+ "Failed allocating pixel buffer attributes dictionary"
+ "Failed allocating pixel format array"
+ "Failed allocating string"
+ "Failed allocation IOSurface dictionary"
+ "Failed allocation properties dictionary"
+ "Failed copying dictionary"
+ "Failed creating cache modes array"
+ "Failed to allocate connectionRefCon"
+ "Failed to allocate frame"
+ "Failed to allocate guestUUIDObject"
+ "Failed to allocate reconciledAttributesPlus for purgeable"
+ "Failed to allocate reorderedEncoderPixelFormatsArray."
+ "Failed to calloc info."
+ "Failed to create CGDataProvider"
+ "Failed to create CVPixelBuffer."
+ "Failed to create buffers array"
+ "Failed to create emptyDict"
+ "Failed to create newAttributes"
+ "Failed to create tags buffers array"
+ "Failed to find image buffer"
+ "Failed to find tag collection for buffer"
+ "Failed to generate temporary file name"
+ "Failed to get base address of CVPixelBuffer."
+ "Failed to get base address of IOSurface."
+ "Failed to get create CVPixelBuffer."
+ "Failed to get create a CGColorSpace."
+ "Failed to load properties"
+ "Failed to write storage header"
+ "Fatal: connectionRefcon is not set up. Pixel buffer origin has not been established."
+ "FieldCount not 1 or 2"
+ "FieldCount not a number"
+ "FieldDetail not recognised"
+ "FigAV1Bridge_CopyITU_T_T35MetadataHDR10PlusMetadata failed"
+ "FigAudioSession function pointers has not been set."
+ "FigCFCreateCombinedDictionary"
+ "FigCFDictionaryCreateMutableCopy failed"
+ "FigCFNumberCreateSInt32 failed"
+ "FigCFNumberCreateUInt32 failed for dvh1CodecNumber"
+ "FigCFNumberCreateUInt32 failed for hvc1CodecNumber"
+ "FigCFWeakReferenceHolderCreateWithReferencedObject for decoder failed"
+ "FigCFWeakReferenceHolderCreateWithReferencedObject for encoder failed"
+ "FigCFWeakReferenceHolderCreateWithReferencedObject for processor failed"
+ "FigCPECryptorCreateCryptorFromSerializedRecipe"
+ "FigCalloc failed"
+ "FigCalloc failed for ioSurfaceArray"
+ "FigCalloc returned NULL"
+ "FigCreatePixelBufferAttributesWithIOSurfaceSupport"
+ "FigCreatePixelBufferCacheModeArray"
+ "FigCreateProtectedIOSurfaceBackedCVPixelBufferWithAttributes failed for intermediate scaling buffer"
+ "FigDerivedObjectCreate failed"
+ "FigDispatchQueueCreateWithPriority failed"
+ "FigDispatchQueueCreateWithPriority failed for notification queue"
+ "FigIOSurfacePixelTransferServiceStorage allocation failed"
+ "FigIOSurfaceSupport.c"
+ "FigMalloc failed"
+ "FigMalloc failed for plistDataBuffer"
+ "FigMalloc failed for sampleSizeArray"
+ "FigMalloc failed for sampleSizeArrayOfUInt32"
+ "FigMallocArrayWithOverhead failed for keysArray"
+ "FigMallocArrayWithOverhead failed for sampleSizeArray"
+ "FigMallocArrayWithOverhead failed for sampleSizeArrayOfUInt32"
+ "FigMallocArrayWithOverhead failed for timingInfoArray"
+ "FigMallocArrayWithOverhead failed for valuesArray"
+ "FigOSTransactionCreate() failed!"
+ "FigPriorityQueueCreate failed"
+ "FigRegistryCopyFilteredItemList returned no items"
+ "FigRegistryCopyFilteredItemList returned null or non-array"
+ "FigRegistryCopyItemList returned empty item"
+ "FigRegistryCopyItemList returned no item in array"
+ "FigRegistryCopyItemList returned non-array"
+ "FigRegistryItemGetFactory returned NULL"
+ "FigRegistryItemGetFactory returned err"
+ "FigRegistryItemGetFactory returned error"
+ "FirstFrame"
+ "FrameCompletionHandlerQueue"
+ "FramesPerSecond"
+ "GammaLevel not a number"
+ "GammaLevel not greater than 0"
+ "GenerateDM4"
+ "GeneratePerFrameHDRDisplayMetadata must be a CFBoolean"
+ "GetConversionRoutine"
+ "GuestWaitingForReply not set but using reply-waiting utility"
+ "GuestWaitingForReply set but using non-waiting utility"
+ "HDR10Plus"
+ "HDRMetadataInsertionMode_RequestSDRRangePreservation"
+ "HEVCProfileSupportList must be non-NULL"
+ "HalfEquirectangular"
+ "HasAdditionalViews should be a CFBoolean"
+ "HasEyeViewsReversed should be a CFBoolean"
+ "HasLeftStereoEyeView should be a CFBoolean"
+ "HasRightStereoEyeView should be a CFBoolean"
+ "HeroEye should be a CFString"
+ "HighQuality"
+ "HighSpeed"
+ "Homography"
+ "HorizontalFieldOfView should be a CFNumber"
+ "HostProcessorID"
+ "HostTemporalFilterID"
+ "HostWaitingForReply not set but using reply-waiting utility"
+ "HostWaitingForReply set but using guest utility"
+ "HostWaitingForReply set but using non-waiting utility"
+ "I"
+ "ICCProfile not data"
+ "IOSurface is NULL"
+ "IOSurfaceAcceleratorCapabilitiesQuadraBayerRepacking"
+ "IOSurfaceAcceleratorCreate failed"
+ "IOSurfaceAcceleratorTransferSurface failed"
+ "IOSurfaceAcceleratorTransformSurface failed"
+ "ITUVariantCSCEnable"
+ "Image height does not match expected height"
+ "Image width does not match expected width"
+ "IncludeMotionConfidence"
+ "InitialHDRMetadataGenerationState"
+ "InitialHDRMetadataState should be a CFDictionary"
+ "InitialSessionState"
+ "InputQueueMaxCount must be greater than -1"
+ "InputQueueMaxCount should be a CFNumber"
+ "IntrinsicMatrix"
+ "IntrinsicMatrixExtensionsProjectionOffset"
+ "IntrinsicMatrixExtensionsRadialDistortionK1"
+ "IntrinsicMatrixExtensionsRadialDistortionK2"
+ "IntrinsicMatrixExtensionsSkew"
+ "IntrinsicMatrixExtensionsTangentialDistortionP1"
+ "IntrinsicMatrixExtensionsTangentialDistortionP2"
+ "IntrinsicMatrixProjectionOffset"
+ "IntrinsicMatrixReferenceDimensions"
+ "Invalid NULL colorSyncQueue"
+ "Invalid NULL compressionQueue"
+ "Invalid NULL dispatch queue"
+ "Invalid NULL dispatchFunction"
+ "Invalid NULL preparationQueue"
+ "Invalid VTHDRMetadataInsertionMode setting"
+ "Invalid cache profile"
+ "Invalid call to complete frame"
+ "Invalid colorSubencoder.leftRightViewIDs"
+ "Invalid colorSubencoder.videoLayerIDs"
+ "Invalid colorSubencoder.viewIDs"
+ "Invalid compression type"
+ "Invalid dataBlockBuffer as it as more than 1 sample size array"
+ "Invalid dataBlockBuffer as it has more than 1 CMFormatDescription"
+ "Invalid dataBlockBuffer as it has more than 1 sample timing info array"
+ "Invalid destination CVPixelBuffer"
+ "Invalid destination cropping params"
+ "Invalid filterStrength value"
+ "Invalid height"
+ "Invalid histogram rectangle"
+ "Invalid number of tag collections(color left/right and alpha left/right)"
+ "Invalid pixelBuffer"
+ "Invalid pixelFormatDesc"
+ "Invalid pixelFormatDesc pixelFormatPlanes"
+ "Invalid planeBytesPerTileHeader"
+ "Invalid planeHeight"
+ "Invalid planeWidth"
+ "Invalid rotation"
+ "Invalid source CVPixelBuffer"
+ "Invalid source cropping params"
+ "Invalid tileHeight"
+ "Invalid tileWidth"
+ "Invalid totalDataSize + totalHeaderSize"
+ "Invalid width"
+ "It is unsupported to have kCVImageBufferTransferFunctionKey and kCVImageBufferLogTransferFunctionKey; Ignoring kCVImageBufferTransferFunctionKey"
+ "JPEGVideoDecoder.c"
+ "JPEGVideoDecoder_CopyProperty"
+ "JPEGVideoDecoder_CopySupportedPropertyDictionary"
+ "JPEGVideoDecoder_CreateInstance"
+ "JPEGVideoDecoder_SetProperty"
+ "JPEG_marker.c"
+ "LEVEL1"
+ "LEVEL3"
+ "LEVEL4"
+ "LEVEL5"
+ "Last past reference frame does not match with the last processed source frame"
+ "Left"
+ "LensAlgorithmKind"
+ "LensDistortions"
+ "LensDomain"
+ "LensFrameAdjustmentsPolynomialX"
+ "LensFrameAdjustmentsPolynomialY"
+ "LensIdentifier"
+ "LensRole"
+ "Lost server connection"
+ "LowMemory"
+ "MIG"
+ "MTLCreateSystemDefaultDevice failed"
+ "MTLDevice is nil"
+ "MTLTexture is nil"
+ "MasteringDisplayColorVolume not 24 bytes"
+ "MasteringDisplayColorVolume not data"
+ "Maximum <= Minimum"
+ "Maximum missing"
+ "Maximum too big"
+ "MaximumGradient"
+ "MaximumReferenceFrameDistance"
+ "MaximumTemporalDifference"
+ "Metal Performance Shaders Framework isn't available"
+ "Metal VTPixelTransferSession failed"
+ "Metal transfer session cannot handle more than one b16q or bp64 sources"
+ "MetalCompletionQueue"
+ "MetalSubmissionQueue"
+ "Minimum < 0"
+ "Minimum missing"
+ "Minimum too big"
+ "Mismatch between rowbytes in CGImage and allocated buffer."
+ "Mismatch stereo tag(s) of taggedBufferGroup to the kVTCompressionPropertyKey_MVHEVCViewIDs/MVHEVCLeftAndRightViewIDs property values"
+ "Missing FigAudioSessionCreateWithCMSession function pointer."
+ "Missing VideoLayerID tag"
+ "Missing in_audio_mx_server_process function pointer."
+ "Missing pFigAudioSessionCreateUsingPrimaryAVAudioSessionSiblingForAuditToken function pointer."
+ "Missing pointer to kAudioSessionNotification_ApplicationStateDidChange"
+ "Missing pointer to kAudioSessionNotification_Interruption"
+ "Mono"
+ "MuxedAlphaDecoder is blocked on pending merges -- 10 second timeout expired"
+ "MuxedAlphaDecoder.c"
+ "MuxedAlphaDecoder_CreateInstance"
+ "MuxedAlphaDecoder_DecodeFrame"
+ "MuxedAlphaDecoder_FinishDelayedFrames"
+ "MuxedAlphaDecoder_StartSession"
+ "MuxedAlphaEncoder.c"
+ "MuxedAlphaEncoder_CompleteFrames"
+ "MuxedAlphaEncoder_CopyProperty"
+ "MuxedAlphaEncoder_CreateInstance"
+ "MuxedAlphaEncoder_EncodeFrame"
+ "MuxedAlphaEncoder_EncodeFrame_block_invoke"
+ "MuxedAlphaEncoder_EncodeMultiImageFrame"
+ "MuxedAlphaEncoder_EncodeMultiImageFrame_block_invoke"
+ "MuxedAlphaEncoder_Finalize"
+ "MuxedAlphaEncoder_StartSession"
+ "NEVER"
+ "NO"
+ "NSObject"
+ "NULL alphaNuhLayerIdArray"
+ "NULL alphaNuhLayerIdNumber"
+ "NULL alphaVideoLayerIDs"
+ "NULL bufferArray"
+ "NULL callback"
+ "NULL compressionSample"
+ "NULL decoder session"
+ "NULL decompression session"
+ "NULL destination buffer"
+ "NULL dictionaryOut"
+ "NULL encoder session"
+ "NULL encoderID"
+ "NULL factory function"
+ "NULL format description"
+ "NULL handler"
+ "NULL hdrMetadataGenerationSession"
+ "NULL imageBuffer"
+ "NULL key"
+ "NULL lastCryptorInOut"
+ "NULL lastFormatDescriptionInOut"
+ "NULL message"
+ "NULL metadataData"
+ "NULL mtl_commandQueue"
+ "NULL output parameter"
+ "NULL outputPixelBuffer!"
+ "NULL pendingFrame"
+ "NULL pendingFrameInfo"
+ "NULL pixelBuffer"
+ "NULL pixelBuffer!"
+ "NULL pixelBufferOut"
+ "NULL pluginSession!"
+ "NULL propertyDictionary"
+ "NULL propertyKey"
+ "NULL propertyValue"
+ "NULL propertyValueOut"
+ "NULL replyOut"
+ "NULL sampleBuffer"
+ "NULL sampleBufferOut"
+ "NULL serializablePropertiesDictionary"
+ "NULL session"
+ "NULL session!"
+ "NULL session->filter!"
+ "NULL session->framesWeAreTracking!"
+ "NULL sessionOut"
+ "NULL source buffer"
+ "NULL supportedPropertyDictionaryOut"
+ "NULL tagCollectionArray"
+ "NULL timestamp entry"
+ "NULL videoEncoderID"
+ "Needs Half or Float"
+ "No HDR metadata generated - unexpected HDR format"
+ "No baseLayerSampleBuffer"
+ "No image statistics found"
+ "No outputHandler provided"
+ "No pixelFormat."
+ "No statistics found"
+ "No subduct; I don't recognize this property!"
+ "No such frame found"
+ "Noise filter strength changed"
+ "Not VTDecompressionSession object"
+ "Not VTTileDecompressionSession object"
+ "Not a CFBoolean"
+ "Not a CFDictionary"
+ "Not a CFNumber"
+ "Not a VTMetalTransferSession"
+ "Not a recognized serialized sample buffer"
+ "Not supported in RPC mode"
+ "Not supported in paravirtualization of temporal filters"
+ "Not valid when generating HDR10Plus"
+ "Number of entries for pixelBufferArray differs from number of entries for tagCollectionArray"
+ "Number of pixel buffers does not match number of pixel buffer UUIDs -- some UUID must have been unrecognized"
+ "Number of sources in this composite pass exceeds kVTMetalSessionMaxCompositeSourcesPerPass"
+ "One or more pixel buffer dimension is 0"
+ "Only 1 sample allowed"
+ "OnlyTheseFrames unrecognized value"
+ "Operation not currently supported for compressed IOSurfaces."
+ "OutputBitDepth is not recognized"
+ "OutputPoolRequestedMinimumBufferCount < 0"
+ "OverUnder"
+ "Padding Buffer allocation failed"
+ "Parameter is not a CFDictionary"
+ "ParametricImmersive"
+ "ParametricLens"
+ "ParavirtualizationHostEncoderSession"
+ "ParavirtualizationVideoDecoder_HandleDecoderSessionEmitDecodedTileMessage"
+ "ParavirtualizedMotionEstimationProcessor.c"
+ "ParavirtualizedMotionEstimationProcessor_CopySupportedPropertyDictionary"
+ "ParavirtualizedMotionEstimationProcessor_CreateInstance"
+ "ParavirtualizedMotionEstimationProcessor_Finalize"
+ "ParavirtualizedMotionEstimationProcessor_HandleDiscardMotionPixelBuffer"
+ "ParavirtualizedMotionEstimationProcessor_HandleEmitMotionVectors"
+ "ParavirtualizedMotionEstimationProcessor_Invalidate"
+ "ParavirtualizedMotionEstimationProcessor_ProcessFrames"
+ "ParavirtualizedMotionEstimationProcessor_SetProperties"
+ "ParavirtualizedMotionEstimationProcessor_SetProperty"
+ "ParavirtualizedMotionEstimationProcessor_StartSession"
+ "ParavirtualizedVideoDecoder.c"
+ "ParavirtualizedVideoDecoder_CopyProperty"
+ "ParavirtualizedVideoDecoder_CopySerializableProperties"
+ "ParavirtualizedVideoDecoder_CopySupportedPropertyDictionary"
+ "ParavirtualizedVideoDecoder_Finalize"
+ "ParavirtualizedVideoDecoder_FinishDelayedFrames"
+ "ParavirtualizedVideoDecoder_FinishDelayedTiles"
+ "ParavirtualizedVideoDecoder_HandleDecoderSessionCreatePixelBufferMessage"
+ "ParavirtualizedVideoDecoder_HandleDecoderSessionDiscardPixelBuffer"
+ "ParavirtualizedVideoDecoder_HandleDecoderSessionGetDestinationPixelBufferAttributes"
+ "ParavirtualizedVideoDecoder_HandleDecoderSessionSetPixelBufferAttributesMessage"
+ "ParavirtualizedVideoDecoder_HandleDecoderSessionSetTileDecodeRequirementsMessage"
+ "ParavirtualizedVideoDecoder_StartSession"
+ "ParavirtualizedVideoDecoder_StartTileSession"
+ "ParavirtualizedVideoEncoder.c"
+ "ParavirtualizedVideoEncoder_BeginPass"
+ "ParavirtualizedVideoEncoder_CompleteFrames"
+ "ParavirtualizedVideoEncoder_CompleteTiles"
+ "ParavirtualizedVideoEncoder_CopySupportedPropertyDictionary"
+ "ParavirtualizedVideoEncoder_EncodeMultiImageFrame"
+ "ParavirtualizedVideoEncoder_EndPass"
+ "ParavirtualizedVideoEncoder_HandleEncoderSessionCreateTileVideoFormatDescription"
+ "ParavirtualizedVideoEncoder_HandleEncoderSessionCreateVideoFormatDescription"
+ "ParavirtualizedVideoEncoder_HandleEncoderSessionEmitEncodedFrameMessage"
+ "ParavirtualizedVideoEncoder_HandleEncoderSessionEmitEncodedTile"
+ "ParavirtualizedVideoEncoder_HandleEncoderSessionMultipassCopyDataAtTimeStamp"
+ "ParavirtualizedVideoEncoder_HandleEncoderSessionMultipassCopyIdentifier"
+ "ParavirtualizedVideoEncoder_HandleEncoderSessionMultipassGetTimeStamp"
+ "ParavirtualizedVideoEncoder_HandleEncoderSessionMultipassGetTimeStampAndDuration"
+ "ParavirtualizedVideoEncoder_HandleEncoderSessionMultipassInvalidate"
+ "ParavirtualizedVideoEncoder_HandleEncoderSessionMultipassSetDataAtTimeStamp"
+ "ParavirtualizedVideoEncoder_HandleEncoderSessionMultipassSetIdentifier"
+ "ParavirtualizedVideoEncoder_HandleEncoderSessionSetPixelBufferAttributesMessage"
+ "ParavirtualizedVideoEncoder_HandleEncoderSessionSetTileAttributes"
+ "ParavirtualizedVideoEncoder_HandleEncoderSessionSetTileEncodeRequirements"
+ "ParavirtualizedVideoEncoder_HandleEncoderSessionSetTimeRangesForNextPass"
+ "ParavirtualizedVideoEncoder_PrepareToEncodeFrames"
+ "ParavirtualizedVideoEncoder_PrepareToEncodeTiles"
+ "ParavirtualizedVideoEncoder_StartSession"
+ "ParavirtualizedVideoEncoder_StartTileSession"
+ "PendingFrameItem allocation failed"
+ "PictureInPictureRegion"
+ "Pixel Buffer Pool is not compatible with Pixel Buffer Attributes"
+ "PixelAspectRatio not a dictionary"
+ "PixelBuffer is not CGImage compatible"
+ "PixelBufferSize"
+ "PixelFormatComponentRange not recognised"
+ "PixelTransferProperties must be NULL or a CFDictionary"
+ "PowerLogSessionID should be a CFString"
+ "PreMultiplied"
+ "PrepareEncodedSampleBuffersForPaddedWrites should be a CFBoolean"
+ "PrepareToEncodeFrames wait for return failed."
+ "PrepareToEncodeTiles wait for return failed."
+ "PreserveSDRRange"
+ "Processor is NULL"
+ "ProfileLevel is not recognized"
+ "ProjectionKind should be a CFString"
+ "Property value for ClientPID was invalid"
+ "Provided rectangle outside frame boundary for data"
+ "Provided rectangle outside frame boundary for metadata"
+ "Q16@0:8"
+ "RadialAngleLimit"
+ "RateControl Session was NULL"
+ "Read-only property"
+ "Received NULL IOSurface"
+ "Rectangle"
+ "Rectilinear"
+ "ReducedFrameDelivery out of range 0.0...1.0"
+ "RegionOfInterest"
+ "RegionOfInterest height greater than 8191"
+ "RegionOfInterest height must be greater than 0"
+ "RegionOfInterest must be contained in pixel buffer"
+ "RegionOfInterest origin.x greater than 8191"
+ "RegionOfInterest origin.y greater than 8191"
+ "RegionOfInterest width greater than 8191"
+ "RegionOfInterest width must be greater than 0"
+ "RepairWeights"
+ "RequestedMVHEVCVideoLayerIDs but content is not MV-HEVC"
+ "RequestedMVHEVCVideoLayerIDs must be CFArray or NULL"
+ "Right"
+ "SRSEnhancementFilter.c"
+ "SRSEnhancementFilter_CopySupportedPropertyDictionary"
+ "SRSEnhancementFilter_CreateInstance"
+ "SRSEnhancementFilter_ProcessFrame"
+ "SRSEnhancementFilter_ProcessFrame_block_invoke"
+ "SRSEnhancementFilter_SetProperty"
+ "SRSEnhancementFilter_StartSession"
+ "Sample buffer not ready"
+ "SecTaskCreateFromSelf failed"
+ "SeparateCodecProcess_TemporalFilter"
+ "Server session is gone"
+ "Session does not have multipass enabled"
+ "Session has no server connection"
+ "Session is NULL"
+ "Session is invalidated"
+ "Session is not Repair"
+ "Session is not Statistics"
+ "Session is wrong CFType"
+ "Session supported properties dictionary is NULL."
+ "Session was NULL"
+ "Session was invalidated"
+ "Set allocation failed"
+ "Should not call vt_SetFigAudioSessionFunctions twice"
+ "ShouldApplyGDC"
+ "SideBySide"
+ "Silo was invalidated"
+ "Source crop rect has negative offset."
+ "Source crop rect is larger than entire dimensions."
+ "Source pixelFormat changed."
+ "SpatialFilterWeight"
+ "SpatioTemporalFilterWeight"
+ "Start session needs to set motion vector pixelBuffer attributes"
+ "Start session needs to set source pixelBuffer attributes"
+ "StereoCameraSystemBaseline"
+ "Straight"
+ "StrongSpatialFilterWeight"
+ "SupportedPresetDictionaries"
+ "T#,R"
+ "T@\"NSArray\",?,R,N"
+ "T@\"NSArray\",R,N"
+ "T@\"NSArray\",R,N,V_destinationFrames"
+ "T@\"NSArray\",R,N,V_frameSupportedPixelFormats"
+ "T@\"NSArray\",R,N,V_interpolationPhase"
+ "T@\"NSArray\",R,N,V_nextFrames"
+ "T@\"NSArray\",R,N,V_previousFrames"
+ "T@\"NSDictionary\",R,N"
+ "T@\"NSDictionary\",R,N,V_destinationPixelBufferAttributes"
+ "T@\"NSDictionary\",R,N,V_sourcePixelBufferAttributes"
+ "T@\"NSIndexSet\",R,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "T@\"VTFrameProcessorFrame\",?,R,N"
+ "T@\"VTFrameProcessorFrame\",R,N"
+ "T@\"VTFrameProcessorFrame\",R,N,V_destinationFrame"
+ "T@\"VTFrameProcessorFrame\",R,N,V_nextFrame"
+ "T@\"VTFrameProcessorFrame\",R,N,V_previousFrame"
+ "T@\"VTFrameProcessorFrame\",R,N,V_previousOutputFrame"
+ "T@\"VTFrameProcessorFrame\",R,N,V_sourceFrame"
+ "T@\"VTFrameProcessorOpticalFlow\",R,N,V_destinationOpticalFlow"
+ "T@\"VTFrameProcessorOpticalFlow\",R,N,V_nextOpticalFlow"
+ "T@\"VTFrameProcessorOpticalFlow\",R,N,V_opticalFlow"
+ "T@\"VTFrameProcessorOpticalFlow\",R,N,V_previousOpticalFlow"
+ "T@\"VTTemporalNoiseFilterConfiguration\",R,N,V_configuration"
+ "TB,R,N,GisSupported"
+ "TB,R,N,GusesPrecomputedFlow,V_precomputedFlow"
+ "TB,R,N,V_usePrecomputedFlow"
+ "TC,N,V_discontinuity"
+ "TC,R,N"
+ "TQ,R"
+ "TRUE"
+ "T^{__CVBuffer=},R,N,V_backwardFlow"
+ "T^{__CVBuffer=},R,N,V_buffer"
+ "T^{__CVBuffer=},R,N,V_forwardFlow"
+ "TemporalLevelLimit must be a CFNumber or NULL"
+ "TestIPBAsynchronousDecodeFrameDelayMilliseconds"
+ "TestIPBAsynchronousDecodeFrameDelayMilliseconds must be CFNumber"
+ "TestIPBQueuedFrameRetain"
+ "TestIPBVideoDecoder.c"
+ "TestIPBVideoDecoder_CopyProperty"
+ "TestIPBVideoDecoder_CopySupportedPropertyDictionary"
+ "TestIPBVideoDecoder_CreateInstance"
+ "TestIPBVideoDecoder_Finalize"
+ "TestIPBVideoDecoder_Invalidate"
+ "TestIPBVideoDecoder_SetProperty"
+ "TestIPBVideoDecoder_StartSession"
+ "TestIPBVideoEncoder.c"
+ "TestIPBVideoEncoder_EncodeFrame"
+ "TestIPBVideoEncoder_EncodeMultiImageFrame"
+ "TestIPBVideoEncoder_emitFrame"
+ "TestProcessor"
+ "Tf,N,V_filterStrength"
+ "Tf,R,N"
+ "Tf,R,N,V_scaleFactor"
+ "The alpha stream is not compatible with CoreMedia requirements"
+ "ThreadCount must be CFNumber"
+ "TileCompressionOutputCallback"
+ "TileDecompressionOutputCallback"
+ "ToBeContinued set but using reply-waiting utility"
+ "Tq,?,R,N"
+ "Tq,R,N"
+ "Tq,R,N,V_flags"
+ "Tq,R,N,V_frameHeight"
+ "Tq,R,N,V_frameWidth"
+ "Tq,R,N,V_inputType"
+ "Tq,R,N,V_motionBlurStrength"
+ "Tq,R,N,V_nextFrameCount"
+ "Tq,R,N,V_numberOfInterpolatedFrames"
+ "Tq,R,N,V_previousFrameCount"
+ "Tq,R,N,V_qualityPrioritization"
+ "Tq,R,N,V_revision"
+ "Tq,R,N,V_scaleFactor"
+ "Tq,R,N,V_spatialScaleFactor"
+ "Tq,R,N,V_submissionMode"
+ "TransferFunction "
+ "TransferFunction not recognised"
+ "TransportIdentifier should be a CFNumber"
+ "Trying to create a ComputeState from a non-compute description"
+ "Trying to create a RenderState from a non-render description"
+ "T{?=ii},?,R,N"
+ "T{?=ii},R,N"
+ "T{?=qiIq},R,N,V_presentationTimeStamp"
+ "UUID already registered"
+ "UUID not found"
+ "Unexpected atom encountered in CFType parsing."
+ "Unrecognised VTVideoDecoderFrame token passed in by decoder"
+ "Unrecognised VTVideoEncoderFrame token passed in by encoder"
+ "Unrecognised VTVideoEncoderPreprocessingFrame token passed in by encoder"
+ "Unsupported codec type in format description"
+ "Unsupported in Client/Server mode"
+ "Unsupported operation"
+ "Unsupported outputPixelBuffer format"
+ "Unsupported pixel format"
+ "Unsupported property key (it's not in the SupportedPropertyDictionary)"
+ "Unsupported protocol version"
+ "UseMultiPassSearch"
+ "VBVBufferDuration"
+ "VBVInitialDelayPercentage"
+ "VBVMaxBitRate"
+ "VCPFrameSuperResolutionConfiguration"
+ "VCPFrameSuperResolutionProcessor"
+ "VCPVideoInterpolationConfiguration"
+ "VCPVideoInterpolationSession"
+ "VEFrame"
+ "VEFrameOpticalFlow"
+ "VEFrameProcessor"
+ "VEFrameRateConversionConfiguration"
+ "VEFrameRateConversionParameters"
+ "VEMotionBlurConfiguration"
+ "VEMotionBlurParameters"
+ "VEOpticalFlowConfiguration"
+ "VEOpticalFlowParameters"
+ "VESuperResolutionConfiguration"
+ "VESuperResolutionParameters"
+ "VEVideoEffectErrorDomain"
+ "VTApplyRestrictions"
+ "VTApplyRestrictions called after instantiating VTCompressionSession"
+ "VTApplyRestrictions called after instantiating VTDecompressionSession"
+ "VTBlackFill.c"
+ "VTBlackFillGetPixelFormatPixelBlockInfo"
+ "VTBlitter_ColorHandling_Optimized.c"
+ "VTBuildPixelBufferPools"
+ "VTBuildPixelBufferPools2"
+ "VTCGUtilities.c"
+ "VTCelesteRotationNodeCreate"
+ "VTCompressionSession.c"
+ "VTCompressionSessionBeginPass"
+ "VTCompressionSessionCompleteFrames"
+ "VTCompressionSessionCopyProperty"
+ "VTCompressionSessionCopySerializableProperties"
+ "VTCompressionSessionCopySupportedPropertyDictionary"
+ "VTCompressionSessionCreateWithOptions"
+ "VTCompressionSessionEncodeFrame"
+ "VTCompressionSessionEncodeFrameWithOutputHandler"
+ "VTCompressionSessionEncodeMultiImageFrame"
+ "VTCompressionSessionEncodeMultiImageFrameWithOutputHandler"
+ "VTCompressionSessionEndPass"
+ "VTCompressionSessionGetPixelBufferPool"
+ "VTCompressionSessionGetTimeRangesForNextPass"
+ "VTCompressionSessionPrepareToEncodeFrames"
+ "VTCompressionSessionRemoteCallbackServer_CompleteFramesReturn"
+ "VTCompressionSessionRemoteCallbackServer_EncodeReturn"
+ "VTCompressionSessionRemoteCallbackServer_FrameIsPending"
+ "VTCompressionSessionRemoteCallbackServer_NotificationIsPending"
+ "VTCompressionSessionRemoteCallbackServer_PrepareToEncodeFramesReturn"
+ "VTCompressionSessionRemoteCallbackServer_PrepareToEncodeTilesReturn"
+ "VTCompressionSessionRemoteServer_BeginPass"
+ "VTCompressionSessionRemoteServer_CompleteFrames"
+ "VTCompressionSessionRemoteServer_CompleteMotionEstimation"
+ "VTCompressionSessionRemoteServer_CompleteTemporalFilterFrames"
+ "VTCompressionSessionRemoteServer_CompleteTiles"
+ "VTCompressionSessionRemoteServer_CopyProperty"
+ "VTCompressionSessionRemoteServer_CopySerializableProperties"
+ "VTCompressionSessionRemoteServer_CopySupportedPropertyDictionary"
+ "VTCompressionSessionRemoteServer_CopyTemporalFilterList"
+ "VTCompressionSessionRemoteServer_Create"
+ "VTCompressionSessionRemoteServer_DequeueNextPendingEncodedFrame"
+ "VTCompressionSessionRemoteServer_Destroy"
+ "VTCompressionSessionRemoteServer_EncodeFrame"
+ "VTCompressionSessionRemoteServer_EncodeFrame_block_invoke"
+ "VTCompressionSessionRemoteServer_EncodeTile"
+ "VTCompressionSessionRemoteServer_EncodeTile_block_invoke"
+ "VTCompressionSessionRemoteServer_EndPass"
+ "VTCompressionSessionRemoteServer_EstimateMotion"
+ "VTCompressionSessionRemoteServer_EstimateMotion_block_invoke"
+ "VTCompressionSessionRemoteServer_EstimateMotion_block_invoke_2"
+ "VTCompressionSessionRemoteServer_GetNextPendingNotification"
+ "VTCompressionSessionRemoteServer_GetTimeRangesForNextPass"
+ "VTCompressionSessionRemoteServer_MotionEstimationCopySourcePixelBufferAttributes"
+ "VTCompressionSessionRemoteServer_MotionEstimationCreate"
+ "VTCompressionSessionRemoteServer_MultiPassStorageCopyDataAtTimeStamp"
+ "VTCompressionSessionRemoteServer_MultiPassStorageCopyIdentifier"
+ "VTCompressionSessionRemoteServer_MultiPassStorageCreate"
+ "VTCompressionSessionRemoteServer_MultiPassStorageDestroy"
+ "VTCompressionSessionRemoteServer_MultiPassStorageGetTimeStamp"
+ "VTCompressionSessionRemoteServer_MultiPassStorageGetTimeStampAndDuration"
+ "VTCompressionSessionRemoteServer_MultiPassStorageSetDataAtTimeStamp"
+ "VTCompressionSessionRemoteServer_MultiPassStorageSetIdentifier"
+ "VTCompressionSessionRemoteServer_PrepareToEncodeFrames"
+ "VTCompressionSessionRemoteServer_PrepareToEncodeTiles"
+ "VTCompressionSessionRemoteServer_SetMultiPassStorage"
+ "VTCompressionSessionRemoteServer_SetProperties"
+ "VTCompressionSessionRemoteServer_SetProperty"
+ "VTCompressionSessionRemoteServer_TemporalFilterCreate"
+ "VTCompressionSessionRemoteServer_TemporalProcessFrame"
+ "VTCompressionSessionRemoteServer_TemporalProcessFrame_block_invoke"
+ "VTCompressionSessionRemoteServer_TileCreate"
+ "VTCompressionSessionRemote_Create_block_invoke"
+ "VTCompressionSessionRemote_GetPixelBufferPool"
+ "VTCompressionSessionRemote_Invalidate"
+ "VTCompressionSessionServerStart"
+ "VTCompressionSessionSetProperties"
+ "VTCompressionSessionSetProperty"
+ "VTCompressionSession_Remote.c"
+ "VTCompressionSession_Server.c"
+ "VTCopyDecoderCapabilitiesDictionaryForCodecTypes"
+ "VTCopyRegistryKeyValueForDeviceIOService"
+ "VTCopySupportedPropertyForVideoEncoderID"
+ "VTCopyTemporalFilterList"
+ "VTCopyVideoDecoderList"
+ "VTCopyVideoDecoderRegistryMatchArrayForCodecType"
+ "VTCopyVideoEncoderList"
+ "VTCreateCGImageFromCVPixelBuffer"
+ "VTCreateCGImageFromIOSurfaceAndAttributes"
+ "VTCreateColorAttachments"
+ "VTCreatePixelBufferPoolAttributesWithName"
+ "VTCreateVImageConverter"
+ "VTCreateVideoEncoderInstanceFromEncoderID"
+ "VTCreateYCbCrCFStringsAndProvideDefaults"
+ "VTCreateYCbCrCFStringsAndProvideDefaultsFromColorSpaceHint"
+ "VTDecoderSessionCreatePixelBuffer failed"
+ "VTDecoderSessionEmitDecodedFrame"
+ "VTDecoderSessionForgetPixelBufferForFrame"
+ "VTDecoderSessionGetDestinationPixelBufferAttributes"
+ "VTDecoderSessionRegisterCustomPixelFormat"
+ "VTDecoderSessionSetPixelBufferAttributes"
+ "VTDecoderSessionTrace"
+ "VTDecompressionSession.c"
+ "VTDecompressionSessionAnalyzeAndInterruptFrame"
+ "VTDecompressionSessionCanAcceptFormatDescription"
+ "VTDecompressionSessionCopyBlackPixelBuffer"
+ "VTDecompressionSessionCopyProperty"
+ "VTDecompressionSessionCopySerializableProperties"
+ "VTDecompressionSessionCopySupportedPropertyDictionary"
+ "VTDecompressionSessionCreateWithOptions"
+ "VTDecompressionSessionDecodeFrameWithOptions"
+ "VTDecompressionSessionDecodeFrameWithOptionsAndMultiImageCapableOutputHandler"
+ "VTDecompressionSessionDecodeFrameWithOptionsAndOutputHandler"
+ "VTDecompressionSessionFinishDelayedFrames"
+ "VTDecompressionSessionFlushPixelBufferPool"
+ "VTDecompressionSessionGetMinAndMaxOutputPresentationTimeStampOfFramesBeingDecoded"
+ "VTDecompressionSessionGetMinOutputPresentationTimeStampOfFramesBeingDecoded"
+ "VTDecompressionSessionRemoteBridge_CanAcceptFormatDescription"
+ "VTDecompressionSessionRemoteBridge_CopyBlackPixelBuffer"
+ "VTDecompressionSessionRemoteBridge_CopyProperty"
+ "VTDecompressionSessionRemoteBridge_CopySerializableProperties"
+ "VTDecompressionSessionRemoteBridge_CopySupportedPropertyDictionary"
+ "VTDecompressionSessionRemoteBridge_Create"
+ "VTDecompressionSessionRemoteBridge_DecodeFrame"
+ "VTDecompressionSessionRemoteBridge_DecodeFrameWithOutputHandler"
+ "VTDecompressionSessionRemoteBridge_DecodeTile"
+ "VTDecompressionSessionRemoteBridge_FinishDelayedFrames"
+ "VTDecompressionSessionRemoteBridge_FinishDelayedTiles"
+ "VTDecompressionSessionRemoteBridge_FlushPixelBufferPool"
+ "VTDecompressionSessionRemoteBridge_GetMinAndMaxOutputPresentationTimeStampOfFramesBeingDecoded"
+ "VTDecompressionSessionRemoteBridge_GetMinOutputPresentationTimeStampOfFramesBeingDecoded"
+ "VTDecompressionSessionRemoteBridge_Invalidate"
+ "VTDecompressionSessionRemoteBridge_SetMultiImageCallback"
+ "VTDecompressionSessionRemoteBridge_SetProperties"
+ "VTDecompressionSessionRemoteBridge_SetProperty"
+ "VTDecompressionSessionRemoteCallbackServer_DecodeFrameReturn"
+ "VTDecompressionSessionRemoteCallbackServer_FinishDelayedFramesReturn"
+ "VTDecompressionSessionRemoteCallbackServer_FrameIsPending"
+ "VTDecompressionSessionRemoteCallbackServer_NotificationIsPending"
+ "VTDecompressionSessionRemoteServer_CanAcceptFormatDescription"
+ "VTDecompressionSessionRemoteServer_CopyBlackPixelBuffer"
+ "VTDecompressionSessionRemoteServer_CopyProperty"
+ "VTDecompressionSessionRemoteServer_CopySerializableProperties"
+ "VTDecompressionSessionRemoteServer_CopySupportedPropertyDictionary"
+ "VTDecompressionSessionRemoteServer_Create"
+ "VTDecompressionSessionRemoteServer_DecodeFrame"
+ "VTDecompressionSessionRemoteServer_DecodeFrame_block_invoke"
+ "VTDecompressionSessionRemoteServer_DecodeTile"
+ "VTDecompressionSessionRemoteServer_DecodeTile_block_invoke"
+ "VTDecompressionSessionRemoteServer_DequeueNextPendingFrame"
+ "VTDecompressionSessionRemoteServer_Destroy"
+ "VTDecompressionSessionRemoteServer_EnableMIO"
+ "VTDecompressionSessionRemoteServer_FinishDelayedFrames"
+ "VTDecompressionSessionRemoteServer_FinishDelayedTiles"
+ "VTDecompressionSessionRemoteServer_FlushPixelBufferPool"
+ "VTDecompressionSessionRemoteServer_GetMinOutputPresentationTimeStampOfFramesBeingDecoded"
+ "VTDecompressionSessionRemoteServer_GetNextPendingNotification"
+ "VTDecompressionSessionRemoteServer_Invalidate"
+ "VTDecompressionSessionRemoteServer_SetProperties"
+ "VTDecompressionSessionRemoteServer_SetProperty"
+ "VTDecompressionSessionRemoteXPC_CanAcceptFormatDescription"
+ "VTDecompressionSessionRemoteXPC_CopyBlackPixelBuffer"
+ "VTDecompressionSessionRemoteXPC_CopyProperty"
+ "VTDecompressionSessionRemoteXPC_CopySerializableProperties"
+ "VTDecompressionSessionRemoteXPC_CopySupportedPropertyDictionary"
+ "VTDecompressionSessionRemoteXPC_Create"
+ "VTDecompressionSessionRemoteXPC_DecodeFrame"
+ "VTDecompressionSessionRemoteXPC_DecodeFrameWithOutputHandler"
+ "VTDecompressionSessionRemoteXPC_DecodeTile"
+ "VTDecompressionSessionRemoteXPC_FinishDelayedFrames"
+ "VTDecompressionSessionRemoteXPC_FinishDelayedTiles"
+ "VTDecompressionSessionRemoteXPC_FlushPixelBufferPool"
+ "VTDecompressionSessionRemoteXPC_GetMinAndMaxOutputPresentationTimeStampOfFramesBeingDecoded"
+ "VTDecompressionSessionRemoteXPC_GetMinOutputPresentationTimeStampOfFramesBeingDecoded"
+ "VTDecompressionSessionRemoteXPC_Invalidate"
+ "VTDecompressionSessionRemoteXPC_SetMultiImageCallback"
+ "VTDecompressionSessionRemoteXPC_SetProperties"
+ "VTDecompressionSessionRemoteXPC_SetProperty"
+ "VTDecompressionSessionRemoteXPC_WaitForAsynchronousFrames"
+ "VTDecompressionSessionRemote_CopyBlackPixelBuffer"
+ "VTDecompressionSessionRemote_DecodeFrameWithOutputHandler"
+ "VTDecompressionSessionRemote_SetMultiImageCallback"
+ "VTDecompressionSessionServerStart"
+ "VTDecompressionSessionServerStartXPC"
+ "VTDecompressionSessionSetDecoderSessionAsPixelBufferSource"
+ "VTDecompressionSessionSetMultiImageCallback"
+ "VTDecompressionSessionSetProperties"
+ "VTDecompressionSessionSetProperty"
+ "VTDecompressionSessionWaitForAsynchronousFrames"
+ "VTDecompressionSession_Remote.c"
+ "VTDecompressionSession_RemoteBridge.c"
+ "VTDecompressionSession_RemoteXPC.c"
+ "VTDecompressionSession_Server.c"
+ "VTDecompressionSession_ServerXPC.c"
+ "VTDeghostingFrameBuffer"
+ "VTDeghostingProcessor"
+ "VTDeghostingProcessorSessionEmitRepair"
+ "VTDeghostingProcessorSessionEmitStatistics"
+ "VTDeghostingProcessorStartSession failed"
+ "VTDeghostingSession"
+ "VTDeghostingSession.m"
+ "VTDeghostingSessionCopyProperty"
+ "VTDeghostingSessionCopySerializableProperties"
+ "VTDeghostingSessionCopySupportedPropertyDictionary"
+ "VTDeghostingSessionInvalidate"
+ "VTDeghostingSessionMitigateGhosts"
+ "VTDeghostingSessionMitigateGhosts2"
+ "VTDeghostingSessionRequestStatistics"
+ "VTDeghostingSessionRequestStatistics2"
+ "VTDeghostingSessionSetProperties"
+ "VTDeghostingSessionSetProperty"
+ "VTDistributedCompressionGetSegmentRanges"
+ "VTDistributedCompressionGetSegmentsToReencode"
+ "VTDistributedPreprocessingGetOverlap"
+ "VTDoesIOServiceSupportRegistryKey"
+ "VTEncoderPreprocessingSessionEmitPreprocessedFrame"
+ "VTEncoderPreprocessingSessionSetSourcePixelBufferAttributes"
+ "VTEncoderSessionCreateCMBlockBuffer"
+ "VTEncoderSessionCreateMVHEVCThreeDimensionalReferenceDisplaysInfoSEIWithDefaults"
+ "VTEncoderSessionCreateTimeStampQueue"
+ "VTEncoderSessionCreateVideoFormatDescription"
+ "VTEncoderSessionCreateVideoFormatDescriptionFromHEVCParameterSets"
+ "VTEncoderSessionCreateVideoSecurityInfoExtension"
+ "VTEncoderSessionDequeueDecodeTimeStamp"
+ "VTEncoderSessionEmitEncodedFrame"
+ "VTEncoderSessionEnqueuePresentationTimeStamp"
+ "VTEncoderSessionSetPixelBufferAttributes"
+ "VTEncoderSessionSetTimeRangesForNextPass"
+ "VTFigAudioSession.c"
+ "VTFigAudioSessionCreate"
+ "VTFigAudioSessionCreateUsingPrimaryAVAudioSessionSiblingForAuditToken"
+ "VTFigAudioSessionCreateWithCMSession"
+ "VTFigAudioSessionInitialize"
+ "VTFigAudioSessionInitialize_block_invoke"
+ "VTFillBufferPixelsWithBlack"
+ "VTFillBufferPixelsWithBlack with unsupported compression type"
+ "VTFillPixelBufferBorderWithBlack"
+ "VTFillPixelBufferWithBlack"
+ "VTFrameProcessor"
+ "VTFrameProcessor.m"
+ "VTFrameProcessorConfiguration"
+ "VTFrameProcessorErrorDomain"
+ "VTFrameProcessorFrame"
+ "VTFrameProcessorImplementationPrivate"
+ "VTFrameProcessorInvalidParameterError"
+ "VTFrameProcessorMemoryAllocationFailure"
+ "VTFrameProcessorOpticalFlow"
+ "VTFrameProcessorParameters"
+ "VTFrameProcessorProcessingError"
+ "VTFrameProcessor_TemporalNoiseFilter.m"
+ "VTFrameRateConversionConfiguration"
+ "VTFrameRateConversionParameters"
+ "VTFrameSilo can only handle compressed data"
+ "VTFrameSilo.c"
+ "VTFrameSiloAddSampleBuffer"
+ "VTFrameSiloCallFunctionForEachSampleBuffer"
+ "VTFrameSiloCreate"
+ "VTFrameSiloGetProgressOfCurrentPass"
+ "VTFrameSiloSetTimeRangesForNextPass"
+ "VTGetBitsPerComponentFromPixelFormatType"
+ "VTGetDecoderCapabilitesForFormatDescription"
+ "VTGetHEVCCapabilitesForFormatDescription"
+ "VTHDRImageStatisticsGenerationSession.m"
+ "VTHDRImageStatisticsGenerationSessionCreate"
+ "VTHDRImageStatisticsGenerationSessionCreate failed"
+ "VTHDRImageStatisticsGenerationSessionCreateStatistics"
+ "VTHDRMetadataGenerationSession.c"
+ "VTHDRMetadataGenerationSessionCopySessionState"
+ "VTHDRMetadataGenerationSessionCreate"
+ "VTHDRMetadataGenerationSessionCreate failed"
+ "VTHDRMetadataGenerationSessionCreateDataFromStatistics"
+ "VTHDRMetadataGenerationSessionCreateDataFromStatisticsDictionary"
+ "VTHDRMetadataGenerationSessionCreatePaddingNALUForEncoder"
+ "VTHDRMetadataGenerationSessionCreateSDRPreservationStaticData"
+ "VTHDRMetadataGenerationSessionInsertData"
+ "VTHDRMetadataGenerationSessionInvalidate"
+ "VTHDRMetadataGenerationSessionSetFramesPerSecond"
+ "VTHDRMetadataInsertionMode is only valid for HEVC or ProRes codec types"
+ "VTHDRMetadataInsertionMode should be a string."
+ "VTHDRPerFrameMetadataGenerationSession.c"
+ "VTHDRPerFrameMetadataGenerationSessionAttachMetadata"
+ "VTHDRPerFrameMetadataGenerationSessionCreate"
+ "VTHostBuildVersion"
+ "VTImageRotationSession.c"
+ "VTImageRotationSessionCreate"
+ "VTInAudioMXServerProcess"
+ "VTIsHardwareDecodeSupported"
+ "VTIsPixelBufferCompatibleWithColorProperties"
+ "VTLowLatencyFrameInterpolationConfiguration"
+ "VTLowLatencyFrameInterpolationImplementation"
+ "VTLowLatencyFrameInterpolationParameters"
+ "VTLowLatencySuperResolutionScalerConfiguration"
+ "VTLowLatencySuperResolutionScalerImplementation"
+ "VTLowLatencySuperResolutionScalerParameters"
+ "VTMTSComputeDirect_btp2_to_btp2"
+ "VTMetalTransferSession.m"
+ "VTMetalTransferSessionComposeImageWithAffineMatrix"
+ "VTMetalTransferSessionCompositeImageSync"
+ "VTMetalTransferSessionConfigureForSourceAndDest"
+ "VTMetalTransferSessionCopyProperty"
+ "VTMetalTransferSessionCopySupportedPropertyDictionary"
+ "VTMetalTransferSessionCreate"
+ "VTMetalTransferSessionCreate FigDerivedObjectCreate failed"
+ "VTMetalTransferSessionGenerateColorBars"
+ "VTMetalTransferSessionGetRequiredAlignment"
+ "VTMetalTransferSessionSetProperty: unknown key."
+ "VTMetalTransferSessionSetPropertyInternal"
+ "VTMetalTransferSessionTransferImageSync"
+ "VTMotionBlurConfiguration"
+ "VTMotionBlurParameters"
+ "VTMotionEstimationProcessorSelectAndCreateInstance"
+ "VTMotionEstimationProcessorSessionEmitMotionVectors"
+ "VTMotionEstimationProcessorSessionSetMotionVectorPixelBufferAttributes"
+ "VTMotionEstimationProcessorSessionSetSourcePixelBufferAttributes"
+ "VTMotionEstimationProcessorStartSession failed"
+ "VTMotionEstimationSession.m"
+ "VTMotionEstimationSessionCompleteFrames"
+ "VTMotionEstimationSessionCopyProperty"
+ "VTMotionEstimationSessionCopySerializableProperties"
+ "VTMotionEstimationSessionCopySourcePixelBufferAttributes"
+ "VTMotionEstimationSessionCopySupportedPropertyDictionary"
+ "VTMotionEstimationSessionCreate"
+ "VTMotionEstimationSessionEstimateMotionVectors"
+ "VTMotionEstimationSessionEstimateMotionVectorsCommon"
+ "VTMotionEstimationSessionInvalidate"
+ "VTMotionEstimationSessionRemote_Create_block_invoke"
+ "VTMotionEstimationSessionSetProperties"
+ "VTMotionEstimationSessionSetProperty"
+ "VTMotionEstimationSession_ShouldUseSeparateProcess_block_invoke"
+ "VTMultiPassStorage is not supported by the encoder"
+ "VTMultiPassStorage.c"
+ "VTMultiPassStorageClose"
+ "VTMultiPassStorageCopyDataAtTimeStamp"
+ "VTMultiPassStorageCopyIdentifier"
+ "VTMultiPassStorageCreate"
+ "VTMultiPassStorageGetTimeStamp"
+ "VTMultiPassStorageInvalidate"
+ "VTMultiPassStorageRemote_Create_block_invoke"
+ "VTMultiPassStorageSetDataAtTimeStamp"
+ "VTMultiPassStorageSetIdentifier"
+ "VTMultiPassStorageWriteMerged"
+ "VTMultiPassStorageWriteSegment"
+ "VTOpticalFlowConfiguration"
+ "VTOpticalFlowParameters"
+ "VTPSharedPool alloc failed"
+ "VTPSharedPoolsForSharingID alloc failed"
+ "VTParavirtualization.c"
+ "VTParavirtualizationCopyFilteredPixelBufferAttributes"
+ "VTParavirtualizationCopyNotificationQueueForGuestUUID"
+ "VTParavirtualizationCreateMessageBoxToRelinquishSurfaceMappingIDs"
+ "VTParavirtualizationCreateReplyAndByteStream"
+ "VTParavirtualizationCreateSerializedAtomDataBlockBufferForSampleBuffer"
+ "VTParavirtualizationFigErrorHexDump"
+ "VTParavirtualizationGuestInstallHandlerForUUID"
+ "VTParavirtualizationGuestRemoveHandlerForUUID"
+ "VTParavirtualizationGuestSendMessageWithIOSurfacesToHostAndCopyReplySync"
+ "VTParavirtualizationGuestSendMessageWithIOSurfacesToHostAsync"
+ "VTParavirtualizationHostDecoderSession"
+ "VTParavirtualizationHostDecoderSession %p RC: %d decoder %p"
+ "VTParavirtualizationHostDecoderSessionCleanUpAfterDecode"
+ "VTParavirtualizationHostDecoderSessionCleanUpAfterTileDecode"
+ "VTParavirtualizationHostDecoderSessionCompleteInvalidate"
+ "VTParavirtualizationHostDecoderSessionCreate"
+ "VTParavirtualizationHostDecoderSessionCreatePixelBufferWithOptions"
+ "VTParavirtualizationHostDecoderSessionDeliverMessageFromGuest"
+ "VTParavirtualizationHostDecoderSessionDeliverMessageFromGuest_block_invoke"
+ "VTParavirtualizationHostDecoderSessionEmitDecodedFrame"
+ "VTParavirtualizationHostDecoderSessionEmitDecodedMultiImageFrame"
+ "VTParavirtualizationHostDecoderSessionEmitDecodedTile"
+ "VTParavirtualizationHostDecoderSessionGetDestinationPixelBufferAttributes"
+ "VTParavirtualizationHostDecoderSessionSetTileDecodeRequirements"
+ "VTParavirtualizationHostEncoderSession"
+ "VTParavirtualizationHostEncoderSession %p RC: %d encoder %p"
+ "VTParavirtualizationHostEncoderSessionCompleteInvalidate"
+ "VTParavirtualizationHostEncoderSessionCreate"
+ "VTParavirtualizationHostEncoderSessionCreateTileVideoFormatDescription"
+ "VTParavirtualizationHostEncoderSessionCreateVideoFormatDescription"
+ "VTParavirtualizationHostEncoderSessionDeliverMessageFromGuest"
+ "VTParavirtualizationHostEncoderSessionDeliverMessageFromGuest_block_invoke"
+ "VTParavirtualizationHostEncoderSessionEmitEncodedFrame"
+ "VTParavirtualizationHostEncoderSessionEmitEncodedTile"
+ "VTParavirtualizationHostEncoderSessionMultipassStorageCopyDataAtTimeStamp"
+ "VTParavirtualizationHostEncoderSessionMultipassStorageCopyIdentifier"
+ "VTParavirtualizationHostEncoderSessionMultipassStorageGetTimeStamp"
+ "VTParavirtualizationHostEncoderSessionMultipassStorageGetTimeStampAndDuration"
+ "VTParavirtualizationHostEncoderSessionMultipassStorageInvalidate"
+ "VTParavirtualizationHostEncoderSessionMultipassStorageSetDataAtTimeStamp"
+ "VTParavirtualizationHostEncoderSessionMultipassStorageSetIdentifier"
+ "VTParavirtualizationHostEncoderSessionSetPixelBufferAttributes"
+ "VTParavirtualizationHostEncoderSessionSetTileAttributes"
+ "VTParavirtualizationHostEncoderSessionSetTileEncodeRequirements"
+ "VTParavirtualizationHostEncoderSessionSetTimeRangesForNextPass"
+ "VTParavirtualizationHostMotionEstimationProcessorCreate"
+ "VTParavirtualizationHostMotionEstimationProcessorSession"
+ "VTParavirtualizationHostMotionEstimationProcessorSession %p RC: %d processor %p"
+ "VTParavirtualizationHostMotionEstimationProcessorSessionCleanUpAfterProcessing"
+ "VTParavirtualizationHostMotionEstimationProcessorSessionCompleteInvalidate"
+ "VTParavirtualizationHostMotionEstimationProcessorSessionCreateMotionVectorPixelBufferWithOptions"
+ "VTParavirtualizationHostMotionEstimationProcessorSessionDeliverMessageFromGuest"
+ "VTParavirtualizationHostMotionEstimationProcessorSessionDeliverMessageFromGuest_block_invoke"
+ "VTParavirtualizationHostMotionEstimationProcessorSessionEmitMotionVectors"
+ "VTParavirtualizationHostMotionEstimationProcessorSessionSetMotionVectorPixelBufferAttributes"
+ "VTParavirtualizationHostMotionEstimationProcessorSessionSetSourcePixelBufferAttributes"
+ "VTParavirtualizationHostSession"
+ "VTParavirtualizationHostSession %p RC: %d  %d decoder sessions %d, encoder sessions"
+ "VTParavirtualizationHostSessionCreate"
+ "VTParavirtualizationHostSessionDeliverMessageFromGuest"
+ "VTParavirtualizationHostSessionInvalidate"
+ "VTParavirtualizationMessageAppendCFDataWithLimitFromOffset"
+ "VTParavirtualizationMessageAppendCFUUIDArray"
+ "VTParavirtualizationMessageAppendCMSampleBuffer"
+ "VTParavirtualizationMessageAppendCMSampleBufferWithLimitAndCopyRemainingData"
+ "VTParavirtualizationMessageAppendFigTagCollectionArray"
+ "VTParavirtualizationMessageAppendPixelBufferAndIOSurfaceAttachments"
+ "VTParavirtualizationMessageCFDataRequiresFragmentation"
+ "VTParavirtualizationMessageCopyCFData"
+ "VTParavirtualizationMessageCopyCFDictionary"
+ "VTParavirtualizationMessageCopyCFPropertyList"
+ "VTParavirtualizationMessageCopyCFUUID"
+ "VTParavirtualizationMessageCopyCFUUIDArray"
+ "VTParavirtualizationMessageCopyCMFormatDescription"
+ "VTParavirtualizationMessageCopyCMSampleBuffer"
+ "VTParavirtualizationMessageCopyFigTagCollectionArray"
+ "VTParavirtualizationMessageGetCMTime"
+ "VTParavirtualizationMessageGetCMVideoDimensions"
+ "VTParavirtualizationMessageGetSInt32"
+ "VTParavirtualizationMessageGetSInt64"
+ "VTParavirtualizationMessageGetUInt32"
+ "VTParavirtualizationMessageGetVTInt32Point"
+ "VTParavirtualizationMessageGetVTInt32Size"
+ "VTParavirtualizationReplyClerkCreate"
+ "VTParavirtualizationReplyClerkDeliverReply"
+ "VTParavirtualizationReplyClerkPrepareForReply"
+ "VTParavirtualizationReplyClerkWaitForReply"
+ "VTParavirtualizationSampleBufferSerialization.c"
+ "VTParavirtualizedHostDecoder.c"
+ "VTParavirtualizedHostEncoder.c"
+ "VTParavirtualizedHostJPEGSupportHandleMessage"
+ "VTParavirtualizedHostMotionEstimationProcessor.c"
+ "VTParavirtualizedJPEGSession.c"
+ "VTParavirtualizedJPEGSessionCopyCapabilities"
+ "VTParavirtualizedJPEGSessionCreate_block_invoke"
+ "VTParavirtualizedJPEGSessionDecodeImage"
+ "VTParavirtualizedJPEGSessionEncodeImage"
+ "VTPixelBlitterColorHandlingOptimized_setup"
+ "VTPixelBlitterColorHandlingOptimized_setup_block_invoke"
+ "VTPixelBlitterColorHandlingOptimized_setup_block_invoke_2"
+ "VTPixelBufferAttributesMediator allocation failed"
+ "VTPixelBufferAttributesMediator.c"
+ "VTPixelBufferAttributesMediatorAddLayer"
+ "VTPixelBufferAttributesMediatorCopyProperty"
+ "VTPixelBufferAttributesMediatorCreate"
+ "VTPixelBufferAttributesMediatorRemoveLayer"
+ "VTPixelBufferAttributesMediatorRemoveRequestedPixelBufferAttributesForKey"
+ "VTPixelBufferAttributesMediatorSetProperty"
+ "VTPixelBufferAttributesMediatorSetRequestedPixelBufferAttributesForKey"
+ "VTPixelBufferConformer allocation failed"
+ "VTPixelBufferConformer failed to create pixel buffer from pool"
+ "VTPixelBufferConformer.c"
+ "VTPixelBufferConformerCopyBlackPixelBuffer"
+ "VTPixelBufferConformerCopyConformedPixelBuffer"
+ "VTPixelBufferConformerCopyConformedTaggedBufferGroup"
+ "VTPixelBufferConformerCreateWithAttributes"
+ "VTPixelRotationSession.c"
+ "VTPixelRotationSessionCopySerializableProperties"
+ "VTPixelRotationSessionCopySupportedPropertyDictionary"
+ "VTPixelRotationSessionCreateWithRotationAndFlip"
+ "VTPixelRotationSessionRotateImage"
+ "VTPixelRotationSessionSetProperties"
+ "VTPixelTransferChain.c"
+ "VTPixelTransferChainAppendRotationNode"
+ "VTPixelTransferChainAppendScalerNode"
+ "VTPixelTransferChainAppendSoftwareNode"
+ "VTPixelTransferChainCreate"
+ "VTPixelTransferChainNodeSessionCopySerializableProperties"
+ "VTPixelTransferGraph did not find a path, falling back."
+ "VTPixelTransferGraph, but recovered on legacy path"
+ "VTPixelTransferGraph.c"
+ "VTPixelTransferGraphBuildChain"
+ "VTPixelTransferNodeCelesteRotationCopySupportedPropertyDictionary"
+ "VTPixelTransferNodeCelesteRotationSetProperty"
+ "VTPixelTransferNodeRotationDoTransfer"
+ "VTPixelTransferSession.c"
+ "VTPixelTransferSessionCanTransfer"
+ "VTPixelTransferSessionCopySerializableProperties"
+ "VTPixelTransferSessionCopySupportedPropertyDictionary"
+ "VTPixelTransferSessionCreate"
+ "VTPixelTransferSessionCreate (for color properties) forbidden by kVTCompressionPropertyKey_AllowPixelTransfer"
+ "VTPixelTransferSessionCreate (for pixel buffer attributes) forbidden by kVTCompressionPropertyKey_AllowPixelTransfer"
+ "VTPixelTransferSessionSetProperties"
+ "VTPixelTransferSessionTransferImage failed, trying to transfer image to destination buffer"
+ "VTPools.c"
+ "VTPopulateColorPrimariesAndTransferFunctionValuesModern"
+ "VTPopulateColorPrimariesAndTransferFunctionValuesModern err"
+ "VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke"
+ "VTPopulateColorPrimariesAndTransferFunctionValuesModern_block_invoke_2"
+ "VTPreprocessing.c"
+ "VTPreprocessingSessionAddResolution"
+ "VTPreprocessingSessionCompleteFrames"
+ "VTPreprocessingSessionCopyProperty"
+ "VTPreprocessingSessionCopySerializableProperties"
+ "VTPreprocessingSessionCopySupportedPropertyDictionary"
+ "VTPreprocessingSessionCreate"
+ "VTPreprocessingSessionPreprocessFrame"
+ "VTPreprocessingSessionSetProperties"
+ "VTPreprocessingSessionSetProperty"
+ "VTRBSSupport.m"
+ "VTRateControlGetVersion"
+ "VTRateControlReactionObserverCreate"
+ "VTRateControlSession.c"
+ "VTRateControlSessionBeforeEmitEncodedFrame"
+ "VTRateControlSessionBeforeEncodeFrame"
+ "VTRateControlSessionBeforePrepareToEncodeFrames"
+ "VTRateControlSessionCompleteFrames"
+ "VTRateControlSessionCopyProperty"
+ "VTRateControlSessionCopySupportedPropertyDictionary"
+ "VTRateControlSessionCopySupportedPropertyDictionary failed"
+ "VTRateControlSessionCreate"
+ "VTRateControlSessionCreate failed"
+ "VTRateControlSessionSetProperty"
+ "VTReadOnePassMetalScalingFeatureFlag"
+ "VTRegisterPixelTransferCapabilityMxN"
+ "VTRegisterVideoDecoderWithInfo"
+ "VTRegisterVideoEncoderWithInfo"
+ "VTRestrictVideoDecoders"
+ "VTRestrictVideoDecoders called after instantiating VTDecompression session"
+ "VTRestrictVideoDecoders called more than once"
+ "VTRestrictions applied more than once"
+ "VTRestrictions.c"
+ "VTRotateCeleste.c"
+ "VTRotation.c"
+ "VTRunningBoardServicesHasAttributeWithTagForPID"
+ "VTSelectAndCreateTemporalFilterInstance"
+ "VTSelectAndCreateVideoDecoderInstanceInternal"
+ "VTSelectAndCreateVideoEncoderInstanceInternal"
+ "VTSession.c"
+ "VTSessionCopyProperty"
+ "VTSessionCopySerializableProperties"
+ "VTSessionCopySupportedPropertyDictionary"
+ "VTSessionRegisterCallbacksForTypeID"
+ "VTSessionSetProperties"
+ "VTSessionSetProperty"
+ "VTSuperResolutionScalerConfiguration"
+ "VTSuperResolutionScalerParameters"
+ "VTTemporalFilterPluginCopySupportedPropertyDictionary failed"
+ "VTTemporalFilterPluginSessionConcludeInputFrame"
+ "VTTemporalFilterPluginSessionCreateOutputPixelBuffer"
+ "VTTemporalFilterPluginSessionEmitOutputFrame"
+ "VTTemporalFilterPluginSessionGetClientInputPixelBufferAttributesHint"
+ "VTTemporalFilterPluginSessionGetClientOutputPixelBufferAttributes"
+ "VTTemporalFilterPluginSessionGetOutputPixelBufferPool"
+ "VTTemporalFilterPluginSessionSetInputPixelBufferAttributes"
+ "VTTemporalFilterPluginSessionSetOutputPixelBufferAttributes"
+ "VTTemporalFilterRemote_CopyList"
+ "VTTemporalFilterRemote_CopyList_block_invoke"
+ "VTTemporalFilterSelection.c"
+ "VTTemporalFilterSession.c"
+ "VTTemporalFilterSessionCompleteFrames"
+ "VTTemporalFilterSessionCopyProperty"
+ "VTTemporalFilterSessionCopySerializableProperties"
+ "VTTemporalFilterSessionCopySupportedPropertyDictionary"
+ "VTTemporalFilterSessionCreate"
+ "VTTemporalFilterSessionInvalidate"
+ "VTTemporalFilterSessionProcessFrameWithOutputPixelBuffer"
+ "VTTemporalFilterSessionRemote_CompleteFrames"
+ "VTTemporalFilterSessionRemote_Create"
+ "VTTemporalFilterSessionRemote_Create_block_invoke"
+ "VTTemporalFilterSessionRemote_ProcessFrame"
+ "VTTemporalFilterSessionSessionSetProperty"
+ "VTTemporalFilterSessionSetProperties"
+ "VTTemporalNoiseFilterConfiguration"
+ "VTTemporalNoiseFilterImplementation"
+ "VTTemporalNoiseFilterParameters"
+ "VTTestMotionEstimationProcessor.c"
+ "VTTestMotionEstimationProcessor_CopyProperty"
+ "VTTestMotionEstimationProcessor_CopySupportedPropertyDictionary"
+ "VTTestMotionEstimationProcessor_SetProperty"
+ "VTTestProcessorConfiguration"
+ "VTTestProcessorImplementation"
+ "VTTestProcessorParameters"
+ "VTTileCompressionSession.c"
+ "VTTileCompressionSessionCopyProperty"
+ "VTTileCompressionSessionCopySerializableProperties"
+ "VTTileCompressionSessionCopySupportedPropertyDictionary"
+ "VTTileCompressionSessionCreate"
+ "VTTileCompressionSessionInvalidate"
+ "VTTileCompressionSessionRemote_Create_block_invoke"
+ "VTTileCompressionSessionSetProperties"
+ "VTTileCompressionSessionSetProperty"
+ "VTTileDecoderSessionEmitDecodedTile"
+ "VTTileDecoderSessionSetTileDecodeRequirements"
+ "VTTileDecompressionSession.c"
+ "VTTileDecompressionSessionCopyProperty"
+ "VTTileDecompressionSessionCopySerializableProperties"
+ "VTTileDecompressionSessionCopySupportedPropertyDictionary"
+ "VTTileDecompressionSessionCreate"
+ "VTTileDecompressionSessionDecodeTile"
+ "VTTileDecompressionSessionInvalidate"
+ "VTTileDecompressionSessionRemoteBridge_Create"
+ "VTTileDecompressionSessionRemoteXPC_Create"
+ "VTTileDecompressionSessionSetProperties"
+ "VTTileDecompressionSessionSetProperty"
+ "VTTileEncoderSessionSetTileEncodeRequirements"
+ "VTTransferService.c"
+ "VTVPParavirtualizedH264VideoEncoder_CreateInstance"
+ "VTVPParavirtualizedHEVCVideoEncoder_CreateInstance"
+ "VTVerifyNoRestrictionsInEffect"
+ "VTVideoCodecService_ShouldUseOOPDecodeForVideoPlayer_block_invoke"
+ "VTVideoCodecService_ShouldUseSeparateCodecProcessForDecode_block_invoke"
+ "VTVideoCodecService_ShouldUseSeparateCodecProcessForEncode_block_invoke"
+ "VTVideoCodecService_ShouldUseXPCRemoteTileDecompressionSession_block_invoke"
+ "VTVideoDecoderCapabilities.c"
+ "VTVideoDecoderCopySupportedPropertyDictionary failed"
+ "VTVideoDecoderDecodeFrame returned error"
+ "VTVideoDecoderDecodeTile returned error"
+ "VTVideoDecoderSelection.c"
+ "VTVideoEncoderCompletePreprocessingFrames did not complete all frames"
+ "VTVideoEncoderCopySupportedPropertyDictionary failed"
+ "VTVideoEncoderSelection.c"
+ "VariableBitRate"
+ "Video decoder emitting frame before it was asked to decode anything"
+ "Video decoder not accepted"
+ "Video decoder not available"
+ "Video encoder not accepted"
+ "Video encoder not available"
+ "VideoConferencing"
+ "ViewPackingKind should be a CFString"
+ "Vv16@0:8"
+ "WarpKind should be a CFString"
+ "We can not handle left offset"
+ "We can not handle top offset"
+ "Write-only property"
+ "Wrong type for pixel format"
+ "XPC"
+ "YCbCrMatrix not recognised"
+ "YES"
+ "Zero bytesPerRow."
+ "Zero height."
+ "Zero width."
+ "[%d x %d]"
+ "[%d x %d] rect:(%d, %d, %d, %d)"
+ "[%d x %d] rect:(%lf, %lf, %lf, %lf)"
+ "[INVALIDATED]"
+ "[SERVER DIED]"
+ "[SERVER SESSION GONE]"
+ "[VTDecompressionSessionXPCRemote %p] [objId = 0x%016llx] "
+ "[VTDeghostingProcessor]"
+ "[VTPixelTransferNodeDynamic] %c%c%c%c [%f, %f, %f, %f, %ld, %ld] -> %c%c%c%c [%f, %f, %f, %f, %ld, %ld]%s"
+ "[VTPixelTransferNodeRotation] %@%s"
+ "[VTPixelTransferNodeScaler] %@"
+ "[VTPixelTransferNodeSoftware] %@%s"
+ "^{OpaqueVTPixelTransferSession=}"
+ "^{OpaqueVTTemporalNoiseFilterInternal=^{OpaqueVTTemporalFilterSession}^{OpaqueVTPixelTransferSession}@@@{pendingFrameList=^{PendingFrameItem}}^{OpaqueFigSimpleMutex}{?=qiIq}{?=qiIq}iBB}"
+ "^{PendingFrameItem=@@{?=qiIq}CC^{__CVBuffer}iI@?{?=^{PendingFrameItem}}}40@0:8{?=qiIq}16"
+ "^{PendingFrameItem=@@{?=qiIq}CC^{__CVBuffer}iI@?{?=^{PendingFrameItem}}}48@0:8{?=qiIq}16@40"
+ "^{_NSZone=}16@0:8"
+ "^{__CVBuffer=}"
+ "^{__CVBuffer=}16@0:8"
+ "_CFRuntimeCreateInstance failed"
+ "_VTPixelRotationSessionRotateSubImage"
+ "_VTPixelTransferSessionCopyProperty"
+ "_VTPixelTransferSessionSetProperty"
+ "_VTPixelTransferSessionTransferImage"
+ "_backwardFlow"
+ "_buffer"
+ "_checkForDiscontinuity:"
+ "_clearStaledPendingFramesFromQueue"
+ "_completeFrame:"
+ "_completeFrames"
+ "_configuration"
+ "_createBestGuessYCbCrCFStringFromColorSpace"
+ "_createPendingFrame:inputFrame:"
+ "_destinationFrame"
+ "_destinationFrames"
+ "_destinationOpticalFlow"
+ "_destinationPixelBufferAttributes"
+ "_device"
+ "_discontinuity"
+ "_filterStrength"
+ "_findFrameInQueue:"
+ "_flags"
+ "_flowPixelFormat"
+ "_forwardFlow"
+ "_frameHeight"
+ "_frameSupportedPixelFormats"
+ "_frameWidth"
+ "_freePendingFrame:"
+ "_getImageBytePointerFromIOSurface"
+ "_getImageBytePointerFromPixelBuffer"
+ "_inputType"
+ "_interpolationPhase"
+ "_loadCapabilities"
+ "_motionBlurStrength"
+ "_nextFrame"
+ "_nextFrameCount"
+ "_nextFrames"
+ "_nextOpticalFlow"
+ "_numberOfInterpolatedFrames"
+ "_opticalFlow"
+ "_parameterDispatchGroup"
+ "_pixelTransferSession"
+ "_precomputedFlow"
+ "_presentationTimeStamp"
+ "_previousFrame"
+ "_previousFrameCount"
+ "_previousFrames"
+ "_previousOpticalFlow"
+ "_previousOutputFrame"
+ "_processFrame:outputFrame:useClientProvidedOutputFrame:"
+ "_processFrameQueue"
+ "_processReferenceFrameIfNotProcessed:"
+ "_processSourceFrameIfNotProcessed:completionHandler:"
+ "_processor"
+ "_processorType"
+ "_qualityPrioritization"
+ "_revision"
+ "_scaleFactor"
+ "_setFilterStrength:"
+ "_sharedEventList"
+ "_sharedEventListLock"
+ "_sharedEventListTearingDown"
+ "_sharedEventListener"
+ "_sourceFrame"
+ "_sourcePixelBufferAttributes"
+ "_spatialScaleFactor"
+ "_submissionMode"
+ "_usePrecomputedFlow"
+ "_validateParameters:error:"
+ "_vcpFrameInterpolationProcessor"
+ "_vcpSuperResolutionProcessor"
+ "_veConfiguration"
+ "_veDestinationFrames"
+ "_veFrame"
+ "_veFrameOpticalFlow"
+ "_veFrameProcessor"
+ "_veParameters"
+ "addObject:"
+ "all sessions have been terminated."
+ "alloc err"
+ "allocate failed"
+ "allocatedPixelBuffer == NULL"
+ "allocation error"
+ "allocation failed for emptyIOSurfaceDict"
+ "allocation failed for pixelBufferArray"
+ "allocation failed for replacementCanvasPixelBufferAttributes"
+ "allocation failed for replacementPixelBufferAttributes"
+ "allocation of mig based remote session failed"
+ "allocation of remote session bridge failed"
+ "allocation of xpc based remote session failed"
+ "alpha DRM without buffer optimization not supported"
+ "alphadecoder_copyPixelBufferAttributesAddingIOSurfaceProtectionOptions"
+ "alphadecoder_copyPixelBufferAttributesFromDecompressionSession"
+ "alphadecoder_createPixelBufferAttributesDictionary"
+ "alphadecoder_createSubLayerVTDecompressionSession"
+ "alphadecoder_findMatchedMuxedAndAlphaPixelFormat"
+ "alphadecoder_getBitsPerBlockForPlanarPixelFormat"
+ "alphadecoder_getPrimaryPixelFormatFromDecompressionSessionPixelBufferPool"
+ "alphadecoder_mergeBaseAndAlpha"
+ "alphadecoder_mergeBaseAndAlphaTaggedBufferGroup"
+ "alphadecoder_setMultiviewColorAndAlphaVideoLayerIDs"
+ "alphadecoder_transferPlane"
+ "alphaencoder_configureSubEncodersByProfile"
+ "alphaencoder_createDerivedSampleBuffer"
+ "alphaencoder_createMultiviewMuxedSampleBuffer"
+ "alphaencoder_createMuxedSampleBuffer"
+ "alphaencoder_createPixelBufferAttributesDictionary"
+ "alphaencoder_demuxBaseAndAlpha"
+ "alphaencoder_emitEncodedFrame"
+ "alphaencoder_getBitDepthAndChromaFormatIdcForHEVCProfile"
+ "alphaencoder_getBitsPerBlockForPlanarPixelFormat"
+ "alphaencoder_setKeysInListFromDictionaryIfPresent"
+ "alphaencoder_setLeftAndRightViewIDsToMVHEVCColorAlphaEncoder"
+ "alphaencoder_setSessionPropertiesInListFromDictionaryIfPresent"
+ "alphaencoder_setVideoLayerIDsToMVHEVCColorAlphaEncoder"
+ "alphaencoder_setViewIDsToMVHEVCColorAlphaEncoder"
+ "alphaencoder_transferPlane"
+ "alphaencoder_validateThatPixelBufferUsesConsistentPremultiplicationMode"
+ "alphaencoder_writeDullChromaPlane"
+ "anchorPQ"
+ "anchorPower"
+ "appendIntToArray"
+ "appendedDataOut must not be NULL"
+ "applejpegCreatePixelBufferAttributesDictionary"
+ "applejpegCreateSuggestedQualityOfServiceTiers"
+ "applejpegCreateSupportedPropertyDictionary"
+ "array allocation failed"
+ "asked to black-fill partial tile"
+ "atom has invalid size"
+ "atom type is not 'aray'"
+ "atom type is not 'dict'"
+ "atom type is not 'idxk' and is not 'strk' "
+ "atom type is not 'keyv'"
+ "atom type is not 'tagc'"
+ "atomDataLength is 0"
+ "atomDataSize is not a multiple of 4"
+ "atomDataSize is wrong for 'idxk'"
+ "attachments alloc failed"
+ "attachmentsData should be non NULL"
+ "attachmentsLength should be greater than zero"
+ "attributesOut is NULL"
+ "autorelease"
+ "ave was wrong size"
+ "average pixel"
+ "average pixel value greater than maximum"
+ "average pixel value less than minimum"
+ "averageOut is NULL"
+ "backingSurface == NULL"
+ "backwardFlow"
+ "bad box length"
+ "bad destinationPixelFormatTypeCount"
+ "bad disparityCurveData"
+ "bad hSpacing"
+ "bad message opcode"
+ "bad parameter"
+ "bad parameter type"
+ "bad property value - OnlyTheseFrames should be CFString"
+ "bad property value - PowerLogSessionID should be CFString"
+ "bad property value - should be CFNumber"
+ "bad sourcePixelFormatTypeCount"
+ "bad vSpacing"
+ "bad value AllowPixelTransferChain"
+ "bad value DestinationColorPrimaries"
+ "bad value DestinationICCProfile"
+ "bad value DestinationRectangle"
+ "bad value DestinationTransferFunction"
+ "bad value DestinationYCbCrMatrix"
+ "bad value DisableDither"
+ "bad value EnableGPUAcceleratedTransfer"
+ "bad value EnableHardwareAcceleratedTransfer"
+ "bad value EnableHighSpeedTransfer"
+ "bad value EnableHistogram"
+ "bad value EnableSoftwareTransfer"
+ "bad value FlipHorizontalOrientation"
+ "bad value FlipVerticalOrientation"
+ "bad value ForceDisableVectorInstructions"
+ "bad value ForceSingleThreaded"
+ "bad value HistogramRectangle"
+ "bad value Rotation"
+ "bad value SetGPUPriorityLow"
+ "bad value SourceCropRectangle"
+ "bad value UseOptimalMSRCoefficients"
+ "bad value for AllowFallbacks"
+ "bad value for AllowLowQualityScaling"
+ "bad value for AllowPixelTransferChain"
+ "bad value for AllowPixelTransferGraph"
+ "bad value for AlphaChannelMode"
+ "bad value for ClientPID property"
+ "bad value for EnableHighSpeedTransfer"
+ "bad value for EnableHistogram"
+ "bad value for ForceDisableVectorInstructions"
+ "bad value for ForceSingleThreaded"
+ "bad value for HLGInvOETFOpticalScale property"
+ "bad value for HLGOETFOpticalScale property"
+ "bad value for HistogramRectangle"
+ "bad value for Label"
+ "bad value for Label property"
+ "bad value for Metal completion queue property"
+ "bad value for Metal submission queue property"
+ "bad value for PQEOTFOpticalScale property"
+ "bad value for PQInvEOTFOpticalScale property"
+ "bad value for PreferRenderKernel"
+ "bad value for RealTime property"
+ "bad value for ReducedPrecisionFractionalOffsets"
+ "bad value for RequireDeviceRegistryID"
+ "bad value for WriteBlackPixelsOutsideDestRect"
+ "bad value for ZeroFillData"
+ "bad value for kVTPixelTransferPropertyKey_AllowOnePassMetalScaling"
+ "bad value for kVTPixelTransferPropertyKey_Convert10BitHDRToSDRFor8BitDestinationWithUnspecifiedColorProperties"
+ "bad value for kVTPixelTransferPropertyKey_DownsamplingMode"
+ "bad value for kVTPixelTransferPropertyKey_MetalCompletionQueue"
+ "bad value for kVTPixelTransferPropertyKey_MetalSubmissionQueue"
+ "bad value for vImageFlags"
+ "bad value in CleanAperture"
+ "bad value kVTPixelTransferPropertyKey_DisableDither"
+ "base and alpha sbuf DTS mismatch"
+ "base and alpha sbuf PTS mismatch"
+ "base and alpha sbuf droppable mismatch"
+ "base and alpha sbuf notsync mismatch"
+ "basedOnPixelBuffer is NULL"
+ "bl_present_flag != 1"
+ "box too short"
+ "buffer"
+ "buildDestinationPixelBufferAttributes"
+ "callback was NULL"
+ "called with no array"
+ "called with two arrays"
+ "caller must specify a transferType"
+ "calling vtDecompressionSubDuctEmitTransferredFrame on unsupported platform"
+ "calloc failed"
+ "calloc failed for sampleSizeArray"
+ "calloc failed for sampleTimingArray"
+ "cannot get pixel buffer pool pixel buffer attributes"
+ "cannot pass in NULL numFramesLookAheadOut"
+ "cannot pass in NULL numFramesLookBehindOut"
+ "cannot pass in NULL numSegmentsOut"
+ "cannot pass in NULL segmentRanges"
+ "cannot pass in NULL segmentRangesOut"
+ "cannot pass in NULL segmentsToReencodeOut"
+ "cant get path"
+ "cfArrayOut is NULL"
+ "cfDictionaryOut is NULL"
+ "cfURLOut is NULL"
+ "cgImageOut == NULL"
+ "chooseOutputFormatForInputPixelFormat"
+ "chromaBitsPerElement must be at least 16"
+ "class"
+ "client changed value for AlphaChannelMode changed after a frame was already encoded"
+ "clientPID should not be 0"
+ "code"
+ "codecArray must be non-null"
+ "color dictionaries do not match"
+ "colorBuffer NULL"
+ "colorSpaceOut is NULL"
+ "colorSyncPixelTransferSession is NULL"
+ "com.apple.coremedia.compressionsession.temporalfiltercallback"
+ "com.apple.coremedia.ipbvideodecoder"
+ "com.apple.coremedia.videotoolbox.paravirtualization.host.decoder"
+ "com.apple.coremedia.videotoolbox.paravirtualization.host.encoder"
+ "com.apple.coremedia.videotoolbox.paravirtualization.host.motion.estimation.processor"
+ "com.apple.gdc"
+ "com.apple.testProcessor"
+ "com.apple.videotoolbox.paravirtualization"
+ "com.apple.videotoolbox.temporalfilter.mctf"
+ "com.apple.videotoolbox.videodeghostingprocessor"
+ "commandQueue invalid"
+ "compare:"
+ "compressed data write error"
+ "compressed metadata write error"
+ "compressionMetadataPattern is zero, value must be non-zero"
+ "compressionsessionremote_trace"
+ "compressionsessionserver_trace"
+ "computeCropAndScaleBuf is NULL"
+ "config is nil"
+ "configuration"
+ "configurationModelPercentageAvailable"
+ "configurationModelStatus"
+ "conformsToProtocol:"
+ "context allocation failed"
+ "context is NULL"
+ "convertedPixelBuffer == NULL"
+ "copy"
+ "copyDolbyStatisticsState"
+ "copySessionState"
+ "could not create instance"
+ "could not create session object"
+ "couldn't create a copy of profiles array"
+ "couldn't create av1CapabilitiesDict"
+ "couldn't create capabilitiesDict"
+ "couldn't create copy of profiles array"
+ "couldn't create dvh1CapabilitiesDict"
+ "couldn't create per profile support dictionary"
+ "couldn't create per-profile support dict"
+ "couldn't create perCodecCapabilitiesDict"
+ "couldn't create profileNumber"
+ "couldn't create support dictionary"
+ "couldn't create vp9CapabilitiesDict"
+ "couldn't create vtPerProfileSupportDict"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "couoldn't create capabilitiesDict"
+ "crap"
+ "create mutable failed"
+ "createAppleP3ColorSpace"
+ "createArrayWithCacheModes"
+ "createCacheModeArrayForCurrentCPUAndProfile"
+ "createDataFromStatistics"
+ "createInferredPropertiesForCodec"
+ "createInstanceFunction returned NULL"
+ "createInstanceFunction returned err"
+ "createInstanceFunction returned error"
+ "createSharedEventListener"
+ "createStatisticsDictionaryFromAttachments"
+ "currentBuffer is NULL"
+ "currentBuffer is not a CVPixelBuffer"
+ "currentBuffer transfer failure"
+ "currentFrame is NULL"
+ "currentFrame isn't backed by an IOSurface"
+ "currentProcessHasTrueBooleanEntitlement"
+ "currentState"
+ "dataLength must be less than INT32_MAX"
+ "ddovi_parseAV1FrameAndCreateHDR10PlusMetadata"
+ "dealloc"
+ "debayer must use compute kernel"
+ "debugDescription"
+ "decode timestamp was not in a valid time range"
+ "decoderCapabilities is not a CFDictionary"
+ "decoderCapabilitiesDict must be non-NULL"
+ "decompressionOutputCallback must be NULL"
+ "decompressionOutputCallback must be non-NULL"
+ "decompression_session_xpc_emit_frame_prefers_event_link_for_app"
+ "decompressionsessionremote_trace"
+ "decompressionsessionserver_trace"
+ "decompressionsessionxpcserver_trace"
+ "defaultRevision"
+ "deghosting_trace"
+ "depth_decoder_trace"
+ "depth_encoder_trace"
+ "depthdecoder_createBaseFormatDescription"
+ "depthdecoder_createPixelBufferAttributesDictionary"
+ "depthencoder_createFormatDescription"
+ "depthencoder_createPixelBufferAttributesDictionary"
+ "depthencoder_emitEncodedFrame"
+ "description=CoreMedia_VideoToolbox-3255.61.4.11.7"
+ "descriptionOut parameter is NULL"
+ "dest buffer's rect"
+ "dest rect"
+ "dest row bytes range check failed"
+ "destMultiPassStorage was NULL"
+ "destMultiPassStorage was invalidated"
+ "destination description invalid"
+ "destination frame does not conform to required pixel buffer attributes"
+ "destination pixel buffer format is not same as source buffer pixel format"
+ "destination pixel buffer is nil"
+ "destinationBuffer is NULL"
+ "destinationFrame"
+ "destinationFrame is nil"
+ "destinationFrames"
+ "destinationOpticalFlow"
+ "destinationPixelBufferAttributes"
+ "destinationPixelFormat is invalid (0)"
+ "destroySharedEventListener"
+ "device is NULL"
+ "deviceIsHomePod"
+ "dictionaryOut is NULL"
+ "dictionaryOut was NULL"
+ "dictionaryWithObject:forKey:"
+ "dictionaryWithObjects:forKeys:count:"
+ "did not find decryptContext"
+ "did not find vmps atom"
+ "didTransfer was false"
+ "discontinuity"
+ "disparityCurveData not CFData"
+ "disparityCurveData too small"
+ "dispatchThreads:threadsPerThreadgroup:"
+ "dispatch_group_create failed"
+ "does NOT match"
+ "domain"
+ "doomedErr"
+ "dovi_attachMetadataToPixelBuffer"
+ "dovi_buildSubLayerFormatDescription"
+ "dovi_buildSubLayerVTDecompressionSession"
+ "dovi_byteAtOffsetMatches"
+ "dovi_parseFrameAndCreateBaseDataBufferAndDynamicReproductionMetadataForDolbyVisionRPU"
+ "dovi_parseFrameAndCreateRPUFromAV1OBU"
+ "dovi_parseHEVCFrameAndCreateHDR10PlusMetadata"
+ "dovi_setExtendedStreamType"
+ "dovi_trace"
+ "dovi_updateCommonEncryptionSubsampleAuxDataIfNecessary"
+ "downloadAssetWithCompletionHandler:"
+ "downloadConfigurationModelWithCompletionHandler:"
+ "dsrxpc_CreateNewSession"
+ "dsrxpc_DecodeFrameCommon"
+ "dsrxpc_Finalize"
+ "dsrxpc_callback_handleDecodeReturnValueAndUnblockWaitingThread"
+ "dsrxpc_callback_handleEmitFrame_IPCMessage"
+ "dsrxpc_callback_handleEmitFrame_XPC"
+ "dsrxpc_callback_handleEmitFrame_XPC_block_invoke"
+ "dsrxpc_callback_handleEmitMultiImage_IPCMessage"
+ "dsrxpc_callback_handleEmitMultiImage_XPC"
+ "dsrxpc_callback_handleEmitMultiImage_XPC_block_invoke"
+ "dsrxpc_callback_handleEmitTile_IPCMessage"
+ "dsrxpc_callback_handleEmitTile_XPC"
+ "dsrxpc_callback_handleEmitTile_XPC_block_invoke"
+ "dsrxpc_callback_handleFinishDelayedFramesReturnAndUnblockWaitingThread"
+ "dsrxpc_callback_handleFinishDelayedTilesReturnAndUnblockWaitingThread"
+ "dsrxpc_callback_handleWaitForFinishReturnAndUnblockWaitingThread"
+ "dsrxpc_copyPixelBufferRecipient"
+ "dsrxpc_decrementPendingFrameInfoOutstandingSampleCount"
+ "dsrxpc_emitPendingFramesForAllSamplesWithError"
+ "dsrxpc_emitPendingFramesForOneSampleWithError"
+ "dsrxpc_ensureClonePixelBufferPool"
+ "dsrxpc_eventLink_MessageHandler"
+ "dsrxpc_handleEmitFrame"
+ "dsrxpc_handleEmitMultiImage"
+ "dsrxpc_handleServerSessionIsGone"
+ "dsrxpc_oneTimeInitialization"
+ "dsrxpc_prepareForCallsOfDecodeFrameFromConsistentThread"
+ "dsrxpc_prepareForCallsOfDecodeFrameFromConsistentThread_block_invoke"
+ "dsrxpc_tryDecrementPendingFrameInfoOutstandingEmitCountToEmit"
+ "dsrxpc_waitForAsynchronousFrames"
+ "dsrxpc_xpcClient_DeadConnectionCallback"
+ "dsrxpc_xpcClient_DeadServerConnectionCallback"
+ "dsrxpc_xpcClient_MessageHandler"
+ "dsrxpc_xpcClient_NotificationFilter"
+ "dsrxpc_xpcClient_SetUpEventLink"
+ "dss_EventLinkServerMessageHandler"
+ "dssxpc_CopyBlackPixelBuffer"
+ "dssxpc_CopyProperty"
+ "dssxpc_CopySerializableProperties"
+ "dssxpc_CopySupportedPropertyDictionary"
+ "dssxpc_Create"
+ "dssxpc_CreateTile"
+ "dssxpc_DecodeFrame_IPCMessage"
+ "dssxpc_DecodeFrame_XPCMessage"
+ "dssxpc_DecodeTile"
+ "dssxpc_DisposeClientRecord"
+ "dssxpc_EmitCallbackReturnValue"
+ "dssxpc_EstablishPixelBufferOriginConnection"
+ "dssxpc_FinishDelayedFrames"
+ "dssxpc_FinishDelayedFrames_block_invoke"
+ "dssxpc_FinishDelayedTiles"
+ "dssxpc_FinishDelayedTiles_block_invoke"
+ "dssxpc_FlushPixelBufferPool"
+ "dssxpc_InitializeClient"
+ "dssxpc_ReplyingMessageHandler"
+ "dssxpc_SetMultiImageCallback"
+ "dssxpc_SetProperties"
+ "dssxpc_SetProperty"
+ "dssxpc_appStateChangeListener"
+ "dssxpc_copyImageBufferAttributesForIOSurface"
+ "dssxpc_copyPixelBufferOriginForConnection"
+ "dssxpc_disposeConnectionRefcon"
+ "dssxpc_dscr_Finalize"
+ "dssxpc_ensureEventLinkIfSupported"
+ "dssxpc_ensureEventLinkIfSupported_block_invoke"
+ "dssxpc_invalidateSession"
+ "dssxpc_maxNumberOfEmitFrameEventLinksToCreatePerSession_block_invoke"
+ "dstFuncConst is NULL"
+ "dumpSessionState"
+ "dv_version_major != 1"
+ "dv_version_major != 3 for dv_profile == 20"
+ "dv_version_minor != 0"
+ "dvcC or dvvC < 9 bytes"
+ "either isDecodable or mayBePlayable must be non-NULL"
+ "emitted tagged buffer group does not have a pixel buffer at this index"
+ "empty pixel format type array"
+ "empty session->framesWeAreTracking!"
+ "empty timestamp queue (VTEncoderSessionEnqueuePresentationTimeStamp was not called enough times?)"
+ "encodeSignalEvent:value:"
+ "encodeWaitForEvent:value:"
+ "encoder emitted garbage/repeated resolution for a frame"
+ "encoder has no codecType?"
+ "encoder session is NULL"
+ "endSession"
+ "enhancementLayer NALu prefix found but el_present_flag was false"
+ "err"
+ "err combining dictionaries"
+ "err getting processor supported properties"
+ "error combining dictionaries"
+ "error getting processor supported properties"
+ "errorWithDomain:code:userInfo:"
+ "expected CFDictionary but disappointed"
+ "expected string for propertyKey"
+ "f"
+ "f16@0:8"
+ "factory function returned noErr but NULL decoderInstance"
+ "factory function returned noErr but NULL encoderInstance"
+ "failed allocating Dolby state"
+ "failed allocating HDR state"
+ "failed property dictionary allocation"
+ "failed to allocate attributes"
+ "failed to allocate newPixelBufferDict"
+ "failed to allocate newTilesDict"
+ "failed to allocate pixelBufferPoolAttributes"
+ "failed to allocate pixelBufferUUID"
+ "failed to allocate tileInfo"
+ "failed to build pixel buffer pools"
+ "failed to create a VTPixelTransferSession"
+ "failed to create a source CVPixelBuffer"
+ "failed to create a source pixelbuffer pool"
+ "failed to create empty dictionary"
+ "failed to create pool"
+ "failed to create videoToolboxProperties"
+ "failed to find the pending frame info"
+ "failed to serialize tagCollection"
+ "figIOSurfaceAcceleratedPixelTransfer_Open"
+ "figIOSurfaceAcceleratedPixelTransfer_Transfer"
+ "figIOSurfaceAcceleratedPixelTransfer_TransferM2"
+ "figNoteRect"
+ "file does not start with correct atoms"
+ "filterInternal"
+ "filterStatistics"
+ "filterStrength"
+ "filteredPropertyDictionary is empty"
+ "final bytesOfClearData less than the RPU data we removed?"
+ "finishProcessing"
+ "flags"
+ "flip only horizontal or vertical but not both"
+ "floatValue"
+ "flowBufferHeight"
+ "flowBufferPixelFormat"
+ "flowBufferWidth"
+ "formatDescription must be HEVC or DolbyVision"
+ "formatDescription must be non-NULL"
+ "formatDescription must be video type"
+ "forwardFlow"
+ "found unresolved boxes for video decoding against 'must' box"
+ "frame is NULL"
+ "frame was never tracked"
+ "frameHeight"
+ "frameHeight is greater than VTTemporalNoiseFilterConfiguration.maximumDimensions.height"
+ "frameHeight is less than VTTemporalNoiseFilterConfiguration.minimumDimensions.height"
+ "framePreferredPixelFormats"
+ "frameSupportedPixelFormats"
+ "frameWidth"
+ "frameWidth is greater than VTTemporalNoiseFilterConfiguration.maximumDimensions.width"
+ "frameWidth is less than VTTemporalNoiseFilterConfiguration.minimumDimensions.width"
+ "framesPerSeconds must be <= 240.0"
+ "framesPerSeconds must be > 0.0"
+ "framesWeAreTracking allocation failed"
+ "framesilo_trace"
+ "fromTimeStamp is not contained in time range"
+ "fromTimeStamp is not numeric or invalid"
+ "fullPathData non-NULL-terminated"
+ "functions should not be NULL"
+ "future reference frame does not conform to required pixel buffer attributes"
+ "future reference frame pixel buffer format is not same as source buffer pixel format"
+ "generateHDR10Plus and SDRRangePreservation need to be set"
+ "getAssetStatusWithPercentCompleted:"
+ "getCGRectIfPresent"
+ "getValuesFromDictionary"
+ "guest UUID already in use"
+ "guest UUID not found"
+ "h/w acceleration(interlaced content override) is required"
+ "hSpacing <= 0"
+ "handleEmittedFrame:presentationTimestamp:status:infoFlags:"
+ "handleForIdentifier:error:"
+ "hash"
+ "hdr10PlusExtractionEnabled"
+ "hdr10PlusMetadataWithNoEmulationPreventionBytes failed"
+ "hdrFormat must be set"
+ "hdrImageStatisticsGenerationSessionOut is NULL"
+ "hdrMetadataDataOut NULL"
+ "hdrimagestatistics_trace"
+ "hdrmetadatasession_trace"
+ "hdrperframemetadatasession_trace"
+ "header region fill is too big"
+ "height mismatch"
+ "height must be greater than 0"
+ "hlgSceneReferredMapping is NULL"
+ "host decoder session"
+ "host encoder session"
+ "i"
+ "i20@0:8i16"
+ "i24@0:8@16"
+ "i24@0:8^{PendingFrameItem=@@{?=qiIq}CC^{__CVBuffer}iI@?{?=^{PendingFrameItem}}}16"
+ "i32@0:8@16@?24"
+ "i36@0:8@16@24C32"
+ "identifierWithPid:"
+ "imageBuffer is NULL"
+ "imageDataProvider == NULL"
+ "imageOut == NULL"
+ "in"
+ "inPixelBuffer == NULL"
+ "incorrect 32bit atom"
+ "info == NULL"
+ "info was NULL"
+ "init"
+ "initWithBuffer:presentationTimeStamp:"
+ "initWithCapacity:"
+ "initWithConfiguration:error:"
+ "initWithDispatchQueue:"
+ "initWithDomain:code:userInfo:"
+ "initWithForwardFlow:backwardFlow:"
+ "initWithFrameWidth:frameHeight:"
+ "initWithFrameWidth:frameHeight:flags:"
+ "initWithFrameWidth:frameHeight:numberOfInterpolatedFrames:"
+ "initWithFrameWidth:frameHeight:qualityPrioritization:revision:"
+ "initWithFrameWidth:frameHeight:scaleFactor:"
+ "initWithFrameWidth:frameHeight:scaleFactor:inputType:usePrecomputedFlow:qualityPrioritization:revision:"
+ "initWithFrameWidth:frameHeight:spatialScaleFactor:"
+ "initWithFrameWidth:frameHeight:usePrecomputedFlow:qualityPrioritization:revision:"
+ "initWithFrameWidth:sourceframeHeight:"
+ "initWithSourceFrame:destinationFrame:"
+ "initWithSourceFrame:nextFrame:opticalFlow:interpolationPhase:submissionMode:destinationFrames:"
+ "initWithSourceFrame:nextFrame:previousFrame:destinationFrame:"
+ "initWithSourceFrame:nextFrame:previousFrame:nextOpticalFlow:previousOpticalFlow:motionBlurStrength:submissionMode:destinationFrame:"
+ "initWithSourceFrame:nextFrame:submissionMode:destinationOpticalFlow:"
+ "initWithSourceFrame:nextFrame:submissionMode:opticalFlow:"
+ "initWithSourceFrame:nextFrames:previousFrames:destinationFrame:filterStrength:discontinuity:"
+ "initWithSourceFrame:previousFrame:interpolationPhase:destinationFrames:"
+ "initWithSourceFrame:previousFrame:previousOutputFrame:opticalFlow:destinationFrame:"
+ "initWithSourceFrame:previousFrame:previousOutputFrame:opticalFlow:submissionMode:destinationFrame:"
+ "initWithWidth:height:pixelFormat:spatialScaleFactor:"
+ "inplace rotation not supported"
+ "inplace rotation not supported for VTPixelRotationSessionTransferSubImage"
+ "inputType"
+ "integral dest rect"
+ "integral source rect"
+ "intermediateTextureArray is NULL"
+ "internalEndSession"
+ "interpolationPhase"
+ "invalid bufferCache"
+ "invalid computeState"
+ "invalid data size in message"
+ "invalid dimensions.height"
+ "invalid dimensions.width"
+ "invalid dstDescription"
+ "invalid dstImage"
+ "invalid dstMetalBuffer"
+ "invalid options"
+ "invalid pixelBuffer"
+ "invalid regionOfInterest"
+ "invalid renderPass"
+ "invalid rotation"
+ "invalid session"
+ "invalid sourceBuffers[i]"
+ "invalid srcDescription"
+ "invalid srcImage"
+ "invalid srcImages"
+ "invalid srcMetalBuffer"
+ "invalid textures"
+ "invalid textures count"
+ "invalid vcp lib"
+ "invalid vtmtsTextureDescriptors"
+ "invalidated"
+ "invariant failure: no TilesDict entry"
+ "invariant failure: no entry for this tile found in TilesDict"
+ "ioSurface is NULL"
+ "ipbdecoder_trace"
+ "is"
+ "is NOT"
+ "isEqual:"
+ "isEqualToString:"
+ "isKindOfClass:"
+ "isMCTFRunningOutOfProcess_block_invoke"
+ "isMemberOfClass:"
+ "isProxy"
+ "isSupported"
+ "jpeg_DecodeFrameSynchronously"
+ "jpeg_createQualityOfServiceTier"
+ "jpeg_createSuggestedQualityOfServiceTiers"
+ "jpeg_createSupportedPropertyDictionary"
+ "jpeg_decompress failed"
+ "jpeg_predecompress"
+ "jpeg_predecompress failed"
+ "kCMBaseObjectError_AllocationFailed"
+ "kCMBaseObjectError_ParamErr"
+ "kCMBaseObjectError_PropertyNotFound"
+ "kCMBaseObjectError_UnsupportedOperation"
+ "kCMFormatDescriptionBridgeError_AllocationFailed"
+ "kCMFormatDescriptionBridgeError_InvalidFormatDescription"
+ "kCMFormatDescriptionError_InvalidParameter"
+ "kFigCFUtilitiesError_AllocationFailed"
+ "kFigCFUtilitiesError_InvalidParameter"
+ "kVTAllocationFailedErr"
+ "kVTColorCorrectionImageRotationFailedErr"
+ "kVTCompressionPropertyKey_HDRMetadataInsertionMode cannot be set after encoding has started"
+ "kVTCompressionPropertyKey_InitialHDRMetadataGenerationState cannot be set after encoding has started"
+ "kVTCouldNotCreateInstanceErr"
+ "kVTCouldNotFindMotionEstimationProcessorErr"
+ "kVTCouldNotFindTemporalFilterErr"
+ "kVTCouldNotFindVideoDecoderErr"
+ "kVTCouldNotFindVideoEncoderErr"
+ "kVTDecompressionSessionXPCPendingFrameNotFoundErr"
+ "kVTDecompressionSessionXPCPixelBufferOriginErr"
+ "kVTDecompressionSessionXPCRedundantConnection"
+ "kVTFigAudioSessionInitializationErr"
+ "kVTFormatDescriptionChangeNotSupportedErr"
+ "kVTFrameSiloInvalidTimeRangeErr"
+ "kVTFrameSiloInvalidTimeStampErr"
+ "kVTInvalidSessionErr"
+ "kVTMetalTransferDescriptionKey_ShouldWaitToComplete takes a kCFBoolean"
+ "kVTMetalTransferPropertyKey_AllowLowQualityScaling takes a kCFBoolean"
+ "kVTMetalTransferPropertyKey_PreferRenderKernel takes a kCFBoolean"
+ "kVTMultiPassStorageInvalidErr"
+ "kVTParameterErr"
+ "kVTParavirtualizationNotAvailableErr"
+ "kVTParavirtualizationProtocolErr"
+ "kVTParavirtualizationTerminatedAllSessionsErr"
+ "kVTParavirtualizationUnrecognizedGuestUUIDErr"
+ "kVTPixelRotationNotSupportedErr"
+ "kVTPixelTransferNotPermittedErr"
+ "kVTPixelTransferNotSupportedErr"
+ "kVTPixelTransferPropertyKey_WriteBlackPixelsOutsideDestRect takes a kCFBoolean"
+ "kVTPropertyNotSupportedErr"
+ "kVTPropertyReadOnlyErr"
+ "kVTRestrictions_AvoidHardwareDecoders not set"
+ "kVTRestrictions_AvoidHardwareDecoders was set previously"
+ "kVTRestrictions_AvoidHardwareEncoders was set previously"
+ "kVTRestrictions_AvoidHardwarePixelTransfer not set"
+ "kVTRestrictions_AvoidHardwarePixelTransfer was set previously"
+ "kVTRestrictions_AvoidIOSurfaceBackings not set"
+ "kVTRestrictions_AvoidIOSurfaceBackings was set previously"
+ "kVTRestrictions_RegisterLimitedSystemDecodersWithoutValidation set with not codecType list"
+ "kVTRestrictions_RunVideoDecodersInProcess not set"
+ "kVTRestrictions_RunVideoDecodersInProcess was set previously"
+ "kVTRestrictions_RunVideoEncodersInProcess was set previously"
+ "kVTSessionMalfunctionErr"
+ "kVTVideoDecoderBackwardIncompatibleFormatErr"
+ "kVTVideoDecoderBadDataErr"
+ "kVTVideoDecoderMalfunctionErr"
+ "kVTVideoDecoderUnsupportedDataFormatErr"
+ "kVTVideoEncoderMVHEVCLeftAndRightViewIDsMismatchErr"
+ "kVTVideoEncoderMVHEVCVideoLayerIDsMismatchErr"
+ "kVTVideoEncoderMalfunctionErr"
+ "key is not a CFString"
+ "lastObject"
+ "left offset is not tile aligned, asked to black-fill partial tile"
+ "lengthToAppendToMessage is 0 or negative."
+ "listIndex out of bounds"
+ "listener was NULL"
+ "loadProperties"
+ "loadSenselSittingOffsetsFromLittleEndianCFData"
+ "logNodeInfo"
+ "lumScaling is NULL"
+ "lumaBitsPerElement must be at least 8"
+ "malloc failed"
+ "marker_detect"
+ "marker_detect(): detected eventual overrun aborting"
+ "matchInfo failed"
+ "matrixValueOut must be non-NULL"
+ "maxSegments must be greater than zero"
+ "maximum pixel"
+ "maximumDimensions"
+ "maximumOut is NULL"
+ "maximumSupportedHeight"
+ "maximumSupportedWidth"
+ "media type is not kCMMediaType_Video"
+ "mediator_trace"
+ "memory allocation failed"
+ "message too small"
+ "metalTransferSessionOut parameter is NULL"
+ "minimum pixel"
+ "minimumDimensions"
+ "minimumOut is NULL"
+ "minimumSupportedHeight"
+ "minimumSupportedWidth"
+ "mismatch between baseLayerTaggedBufferGroup and alphaLayerTaggedBufferGroup"
+ "mismatch between pixel buffer's alpha channel mode and encoder's current setting"
+ "missing anchorPQ"
+ "missing anchorPower"
+ "missing average"
+ "missing averageOffset"
+ "missing callback"
+ "missing firstFrame"
+ "missing framesPerSecond"
+ "missing generateDM4"
+ "missing level1InfoAvailable"
+ "missing level3InfoAvailable"
+ "missing level4InfoAvailable"
+ "missing level5InfoAvailable"
+ "missing maximum"
+ "missing maximumOffset"
+ "missing minimum"
+ "missing minimumOffset"
+ "missing pixelBufferSize"
+ "missing regionOfInterest"
+ "missing transfer type"
+ "more than 5 buffers in tagged buffer group not yet supported"
+ "motion estimation session is NULL"
+ "motionBlurStrength"
+ "motionVectorPixelBufferAttributes is not a dictionary"
+ "motionestimation_trace"
+ "multiImageCapableHandler must be non-NULL"
+ "multiPassStorage was NULL"
+ "multiPassStorage was invalidated"
+ "multipassstorage_trace"
+ "mutableExtensions allocation failed"
+ "mutableExtensionsDict was NULL"
+ "muxed_alpha_decoder_trace"
+ "muxed_alpha_encoder_trace"
+ "nalu Length size must be 2 or 4"
+ "naluSize too big"
+ "naluSize too small"
+ "newClient creation failed"
+ "newSharedEvent"
+ "nextFrame"
+ "nextFrameCount"
+ "nextFrames"
+ "nextOpticalFlow"
+ "no 'hvcC' data"
+ "no SampleDescriptionExtensionAtoms"
+ "no SampleDescriptionExtensionAtoms CFDictionary"
+ "no agglomeratedPixelFormatTypesArray"
+ "no attributesCopy"
+ "no attributesToResolveCollection"
+ "no available device"
+ "no base SampleDescriptionExtensionAtoms"
+ "no base extensions"
+ "no blackBufferOut"
+ "no block buffer in sample"
+ "no codecCapabilitiesDict"
+ "no codecType"
+ "no creationRequestMessageFromGuest"
+ "no current pixelBuffer"
+ "no cvResolvedPixelBufferAttributesMutableCopy"
+ "no decoder dictionary"
+ "no decoder list array"
+ "no depthExtensionsAtoms Dictionary"
+ "no dest IOSurface"
+ "no destinationBuffer"
+ "no disparityCurveData Data"
+ "no encoder dictionary"
+ "no encoder list array"
+ "no entry found for this pixelBufferUUID"
+ "no extensions"
+ "no factory functions"
+ "no formatDesc"
+ "no formatDescription"
+ "no hvcC found"
+ "no imageBuffer"
+ "no kCVPixelBufferPixelFormatTypeKey?"
+ "no layers"
+ "no messageToGuestHandler"
+ "no motion estimation processor array"
+ "no motion estimation processor dictionary"
+ "no motion estimation processor registry"
+ "no motion estimation registry"
+ "no mutex"
+ "no otherStakeHoldersOrdered"
+ "no otherStakeHoldersToAttributesMap"
+ "no pending reply struct found for replyIdentifier"
+ "no pixel format type in pixel buffer attributes"
+ "no pixel formats left"
+ "no pixelBuffer"
+ "no pixelBufferAttributes"
+ "no property key"
+ "no reference pixelBuffer"
+ "no sampleBuffer"
+ "no sampleDescriptionExtensions"
+ "no samples at timestamp"
+ "no session or tile session"
+ "no source IOSurface"
+ "no sourceBuffers"
+ "no string"
+ "no subDuct"
+ "no temporal filter registry"
+ "no temporal filter storage"
+ "no updatedPBA"
+ "no valid Celeste Rotation instance for EnableHighSpeedTransfer"
+ "no valid Celeste Rotation instance for EnableHistogram"
+ "no valid Celeste Rotation instance for HistogramData"
+ "no valid Celeste Rotation instance for HistogramRectangle"
+ "no valid Celeste Rotation instance for ZeroFillData"
+ "no video decoder registry"
+ "no video decoder registry at all"
+ "no video encoder registry"
+ "no video encoder registry at all"
+ "no vtPixelBufferAttributesMediatorCALayerDesiredAttributes"
+ "non-IOSurface backed CVPixelBuffer."
+ "non-numeric presentationTimeStamp"
+ "non-pixelBuffer in taggedBufferGroup"
+ "not CFBoolean"
+ "not CFData"
+ "not NULL or a CFBoolean"
+ "not a CFBoolean"
+ "not a CFData"
+ "not a CFNumber"
+ "not a CFString"
+ "not a VTMultiPassStorage object"
+ "not a dict"
+ "not a dictionary"
+ "not a number or boolean"
+ "not configured"
+ "not enough data in message"
+ "not valid rotation"
+ "notifyListener:atValue:block:"
+ "numSegments must be greater than zero"
+ "numberOfInterpolatedFrames"
+ "numberWithFloat:"
+ "numberWithInt:"
+ "numberWithInteger:"
+ "numberWithUnsignedInt:"
+ "objectAtIndex:"
+ "off"
+ "on"
+ "only Monochrome10_AutoLevel is supported"
+ "only replies expected"
+ "only video format description is supported"
+ "opticalFlow"
+ "originalPixelBuffer == NULL"
+ "originalSampleSize < derivedSampleSize"
+ "originalSubsampleAuxDataLength % sizeof(CommonEncryptionSubsampleAuxData) != 0"
+ "out-of"
+ "out-of-range offset in CleanAperture"
+ "outImageDataProvider == NULL"
+ "output pixel buffer pool was NULL"
+ "outputCallback must be NULL"
+ "outputCallback must be non-NULL"
+ "outputHandler is NULL"
+ "outputHandler must be non-NULL"
+ "outputMultiImageCallback already set"
+ "outputMultiImageCallback must be NULL"
+ "owner session is NULL"
+ "parameter set pointers alloc failure"
+ "parameter set sizes alloc failure"
+ "parameterDispatchGroup"
+ "paravirtualizedMotionEstimationProcessor_HandleMessageFromHost"
+ "paravirtualizedMotionEstimationProcessor_forgetPixelBufferByUUID"
+ "paravirtualizedMotionEstimationProcessor_lookupRetainPixelBufferByUUID"
+ "paravirtualizedMotionEstimationProcessor_rememberPixelBufferAndUUID"
+ "paravirtualizedVideoDecoder_createReencryptedSampleBufferIfNecessary"
+ "paravirtualizedVideoDecoder_lookupRetainAndForgetPendingFramePixelBufferByUUID"
+ "paravirtualizedVideoDecoder_lookupRetainAndForgetPendingFramePixelBuffersByUUIDs"
+ "paravirtualizedVideoDecoder_lookupRetainAndForgetPendingTilePixelBufferByUUID"
+ "paravirtualizedVideoDecoder_rememberPendingFramePixelBufferAndUUID"
+ "paravirtualizedVideoDecoder_rememberPendingTilePixelBufferAndCopyUUID"
+ "paravirtualizedVideoEncoder_CopySupportedPropertyDictionaryInternal"
+ "paravirtualizedVideoEncoder_forgetPendingFramePixelBufferByUUID"
+ "paravirtualizedVideoEncoder_lookupRetainAndForgetPendingTilePixelBufferByUUID"
+ "paravirtualizedVideoEncoder_rememberPendingFramePixelBufferAndUUID"
+ "paravirtualizedVideoEncoder_rememberPendingTilePixelBufferAndCopyUUID"
+ "past reference frame does not conform to required pixel buffer attributes"
+ "past reference frame pixel buffer format is not same as source buffer pixel format"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "pixel buffer isn't backed by an IOSurface!"
+ "pixel format type not a number"
+ "pixelBuffer == NULL"
+ "pixelBuffer is NULL"
+ "pixelBuffer is neither PQ nor HLG"
+ "pixelBuffer is somehow NULL"
+ "pixelBuffer isn't backed up by an IOSurface!"
+ "pixelBuffer was NULL"
+ "pixelFormat does not produce CVPixelFormatDescription"
+ "pixelFormatList is not a CFArray"
+ "pixelRotationSessionOut was NULL"
+ "pixelTransferBufferPool is NULL"
+ "pixelTransferSession is NULL"
+ "pixel_rotation_trace"
+ "pixelbuffer must be IOSurface backed"
+ "pixeltransfer_trace"
+ "pixeltransfergraph_trace"
+ "planarPixelFormat contains fewer than 2 planes"
+ "planarPixelFormat is not planar"
+ "planeBaseRequirement"
+ "pqToneMapping is NULL"
+ "pqToneMapping->pq_eotf.c1 value does not match the predefined constant"
+ "pqToneMapping->pq_eotf.c2 value does not match the predefined constant"
+ "pqToneMapping->pq_eotf.c3 value does not match the predefined constant"
+ "pqToneMapping->pq_eotf.m1 value does not match the predefined constant"
+ "pqToneMapping->pq_eotf.m2 value does not match the predefined constant"
+ "pq_eetf.minLum value does not match the predefined constant"
+ "precomputedFlow"
+ "preprocessingSession allocation failed"
+ "preprocessingSession cannot be NULL"
+ "preprocessingsession_trace"
+ "presentation timestamps of future reference frames are not in chronological order"
+ "presentation timestamps of last source frame and current source frame are not in chronological order"
+ "presentation timestamps of past reference frames and source frame are not in chronological order"
+ "presentation timestamps of past reference frames are not in chronological order"
+ "presentationTimeStamp"
+ "previousFrame"
+ "previousFrameCount"
+ "previousFrames"
+ "previousOpticalFlow"
+ "previousOutputFrame"
+ "problems with the markers"
+ "processComputeKernelSyncFunctionConstant"
+ "processMetalBlitterDirect"
+ "processRenderKernelSyncFunctionConstant"
+ "processWithCommandBuffer:parameters:"
+ "processWithCommandBuffer:parameters:completionHandler:"
+ "processWithParameters:completionHandler:"
+ "processWithParameters:error:"
+ "processWithParameters:frameOutputHandler:"
+ "processWithParams:completionHandler:error:"
+ "processWithParams:error:"
+ "processWithPreviousFrame:currentFrame:interpolationPhases:outputBuffers:error:frameCompletionHandler:"
+ "processWithSourceFrame:destinationframe:error:"
+ "processor not supported"
+ "processor unsupported"
+ "processorSession is NULL"
+ "processorSupported"
+ "profile not recognized"
+ "progressOut was NULL"
+ "property is in the deny list"
+ "property is not CFBoolean or NULL"
+ "property is not CVPixelBufferPool"
+ "property is read-only"
+ "propertyDictionary is NULL"
+ "propertyKey is NULL"
+ "propertyValueOut is NULL"
+ "propertyValueOut was NULL"
+ "protected IOSurface, CVPixelBuffer will not be black filled."
+ "pv_host_jpeg_support_trace"
+ "pv_jpeg_session_trace"
+ "pv_meprocessor_trace"
+ "pvjpeg_copySessionCapabilities"
+ "q"
+ "q16@0:8"
+ "qualityPrioritization"
+ "rangeCurveType isn't 1"
+ "rangeCurveVersion > 0"
+ "rangeMax <= rangeMin"
+ "rangeMin < 0"
+ "ratecontrol_session_trace"
+ "read_SOF"
+ "read_SOS"
+ "read_SOS_progressive"
+ "received invalid value for keyIndex"
+ "referenceBuffer"
+ "referenceBuffer is not a CVPixelBuffer"
+ "referenceBuffer transfer failure"
+ "referenceFrame is NULL"
+ "referenceFrame isn't backed by an IOSurface"
+ "registered pixel transfer service failed to open; falling back"
+ "registered pixel transfer service failed to transfer; falling back"
+ "registry creation failed"
+ "release"
+ "remaining data too small to contain a NALu"
+ "remoteSession is NULL"
+ "remoteSession is NULL."
+ "remoteSession is invalidated"
+ "remoteSessionGone was already handled"
+ "remoteSessionOut is NULL"
+ "removeObject:"
+ "requested blackfill area is larger than plane area"
+ "reserved byte is not 0x01"
+ "resetStatistics"
+ "respondsToSelector:"
+ "restoreSessionState"
+ "restoreStateDict must be a CFDictionary"
+ "result"
+ "retain"
+ "retainCount"
+ "revision"
+ "rotation inplace not allowed"
+ "rotationDegrees must be 0,90,180 or 270"
+ "rowBytes == 0"
+ "sDeghostingRegistry is NULL."
+ "sVTMotionEstimationSessionSupportedPropertyDictionary is NULL"
+ "sample buffer DTS is invalid"
+ "sample buffer had no block buffer"
+ "sample buffer was NULL"
+ "sample buffer was invalid"
+ "sample buffers must have strictly increasing decode timestamps"
+ "sample must have a format description"
+ "sampleAttachments should be non NULL"
+ "sampleAttachmentsAfterReencryption is NULL even though we asked to create it if necessary in CMSampleBufferGetSampleAttachmentsArray"
+ "sbufSampleAttachments should be non NULL"
+ "scaleFactor"
+ "sdrPreservationEnabled"
+ "segmentRange was not valid"
+ "self"
+ "semaphore/mutex alloc failed"
+ "senselSitting CFData size does not match VTMSNumSenselSittingOffsets (8 integers)"
+ "serializedCryptorRecipe create failed."
+ "server death was already handled"
+ "session and tileSession cannot be both NULL or both non-NULL"
+ "session cannot be NULL"
+ "session is NULL"
+ "session was invalidated"
+ "sessionClient is NULL"
+ "sessionOut is NULL"
+ "sessionPropertyApplier"
+ "setCompletionQueue:"
+ "setDiscontinuity:"
+ "setFilterStrength:"
+ "setLevel4Info"
+ "setMaxTemporalExponentialFactor:"
+ "setScaleFactor:"
+ "setSignaledValue:"
+ "setSubmissionQueue:"
+ "setThreadgroupMemoryLength:atIndex:"
+ "setupBackgroundColor"
+ "setupRenderRotationAndCrop"
+ "shouldUseMIGInterfaceForRemoteDecompressionSession_block_invoke"
+ "silo was NULL"
+ "softlink:r:path:/System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto"
+ "source buffer's rect"
+ "source frame does not conform to required pixel buffer attributes"
+ "source pixel buffer is nil"
+ "source rect"
+ "source row bytes range check failed"
+ "sourceFrame"
+ "sourceFrame is nil"
+ "sourceHeight must be greater than 0"
+ "sourceMultiPassStorage was NULL"
+ "sourceMultiPassStorage was invalidated"
+ "sourcePixelBufferAttributes"
+ "sourcePixelBufferAttributes is NULL"
+ "sourcePixelBufferAttributes is not a dictionary"
+ "sourcePixelFormat is invalid (0)"
+ "sourceURL was NULL"
+ "sourceURLs was NULL"
+ "sourceWidth must be greater than 0"
+ "spatialScaleFactor"
+ "srcAttachmentsDictionaryOut and dstAttachmentsDictionaryOut must be non-NULL"
+ "srcFuncConst is NULL"
+ "srcMatrixValueOut and dstMatrixValueOut must be non-NULL"
+ "srsFilter_calculateOutputDimensions"
+ "srsenhancementfilter_trace"
+ "standardDeviationOut is NULL"
+ "standardized dest rect"
+ "standardized source rect"
+ "startSessionWithConfiguration:error:"
+ "startSessionWithConfigurationMode:error:"
+ "starting tile size"
+ "stateDictionaryOut is NULL"
+ "status"
+ "step not CFString"
+ "step was NULL"
+ "storageClient is NULL"
+ "strideRequirement"
+ "string allocation failed"
+ "stub"
+ "submissionMode"
+ "subsampleAuxEntryCount < 1"
+ "superclass"
+ "support_mvhevcwithalpha_decoding"
+ "supported"
+ "supportedPixelFormats"
+ "supportedPropertyDictionaryOut is NULL"
+ "supportedPropertyDictionaryOut was NULL"
+ "supportedRevisions"
+ "supportedScaleFactors"
+ "supportedScaleFactorsForFrameWidth:frameHeight:"
+ "supportsFamily:"
+ "surface == NULL"
+ "surfaceParameterCount is not 2"
+ "tagCollection is NULL"
+ "tagged buffer group contains 0 buffers"
+ "tagged buffer group does not have a pixel buffer at this index"
+ "taggedBufferGroup count is 0"
+ "taggedBufferGroup count mismatch with MVHEVCVideoLayerIDs count"
+ "taggedBufferGroup has 0 entries"
+ "tags"
+ "tddss_NoReplyMessageHandler"
+ "temporalFilterSessionOutputCallback"
+ "temporalfilterselection_trace"
+ "temporalfiltersession_trace"
+ "testipb_CreatePixelBufferAndDrawFrame"
+ "testipb_TraceFrame"
+ "testipb_createSupportedPropertyDictionary"
+ "testipb_encoder_trace"
+ "testipb_getFramePackingType"
+ "tile size"
+ "timeRange duration must be numeric"
+ "timeRange must be kCMTimeRangeInvalid or valid"
+ "timeRange must be valid"
+ "timeRange start epoch must be zero"
+ "timeRange start must be numeric"
+ "timeRangeArray must not be NULL"
+ "timeRangeArrayOut is NULL"
+ "timeRangeCount must be greater than 0"
+ "timeRangeCount must be greater than zero"
+ "timeRangeCountOut is NULL"
+ "timeRanges intersect with one another"
+ "timeRanges is NULL"
+ "timeRanges must be in ascending order"
+ "timeStamp is not contained in time range"
+ "timeStamp is not numeric or invalid"
+ "timeStampOut was NULL"
+ "timingArrayEntries should be one"
+ "tiny box length"
+ "top offset is not tile aligned, asked to black-fill partial tile"
+ "transfer function must not change during session"
+ "transferservice_trace"
+ "true"
+ "typeID already registered"
+ "un-named"
+ "unable to identify video encoder"
+ "uncompressed pixel format is NOT available"
+ "unexpected codecType, neither dish nor deph"
+ "unexpected histSize"
+ "unexpected number of sampleAttachments"
+ "unknown streamType"
+ "unrecognised OnlyTheseFrames property value"
+ "unrecognised callbacks->version (expected 0)"
+ "unrecognised property key"
+ "unrecognized AlphaChannelMode attachment"
+ "unrecognized codecType, neither dish nor deph"
+ "unrecognized messageType"
+ "unrecognized motion vector pixel buffer UUID"
+ "unrecognized pending pixel buffer UUID"
+ "unrecognized pending tile pixel buffer UUID"
+ "unrecognized resolution"
+ "unrecognized step"
+ "unsupported muxed alpha configuration"
+ "useFilteredStatistics"
+ "usePrecomputedFlow"
+ "userInfo"
+ "usesPrecomputedFlow"
+ "v16@0:8"
+ "v16@?0q8"
+ "v20@0:8C16"
+ "v20@0:8f16"
+ "v24@0:8@?16"
+ "v24@0:8^{PendingFrameItem=@@{?=qiIq}CC^{__CVBuffer}iI@?{?=^{PendingFrameItem}}}16"
+ "v24@?0@\"<MTLSharedEvent>\"8Q16"
+ "v24@?0@\"VEMotionBlurParameters\"8@\"NSError\"16"
+ "v24@?0@\"VTTemporalNoiseFilterParameters\"8@\"NSError\"16"
+ "v24@?0r^v8r^v16"
+ "v32@0:8@16@24"
+ "v32@0:8@16@?24"
+ "v32@?0q8@\"NSNumber\"16B24i28"
+ "v56@0:8^{__CVBuffer=}16{?=qiIq}24i48I52"
+ "vImageConverterOut must be non-NULL"
+ "vImageLoadFunctions"
+ "vParavirtualizationGetReplyTimeoutInNanoSeconds_block_invoke"
+ "vSpacing <= 0"
+ "validRotation"
+ "validateDeviceProperties"
+ "value in array was not a CFUUID"
+ "value in array was not a FigTagCollection"
+ "vcpConfiguration"
+ "veConfiguration"
+ "veFrame"
+ "veFrameOpticalFlow"
+ "veParameters"
+ "video decoder does not support new format description"
+ "video encoder does not support multi-image frame encoding"
+ "video encoder emitted noErr but NULL imageBuffer"
+ "videoEncoderID must not be NULL"
+ "videoEncoderIdentifierAndVersion not CFString"
+ "videoEncoderIdentifierAndVersion was NULL"
+ "videoLayerID in taggedBufferGroup not found in MVHEVCVideoLayerIDs"
+ "videocodecserviceutil_trace"
+ "videodecoderselection_trace"
+ "videoencoderselection_trace"
+ "vmps atom has funny size"
+ "vmps atom has non-sorted entries"
+ "vtAddDVH1CapabilitiesForEmbedded"
+ "vtAddDolbyOverride_block_invoke"
+ "vtAddProfileToDict"
+ "vtBufferGetCleanRect"
+ "vtBufferGetPixelAndPictureAspectRatio"
+ "vtBuildPixelBufferPoolsCommon"
+ "vtCheckIORegistryRequiredDependencyForFilter"
+ "vtCodecTypeIsEligibleForParavirtualization"
+ "vtCompressionSessionAddAmbientViewingEnvironmentToHVCC"
+ "vtCompressionSessionAddDolbyVisionVideoFormatDescriptionExtensions"
+ "vtCompressionSessionAddPropertyToPartition"
+ "vtCompressionSessionBuildAndRunPipeline"
+ "vtCompressionSessionColorSyncWork"
+ "vtCompressionSessionCompleteFramesCallback"
+ "vtCompressionSessionCompleteFramesWork"
+ "vtCompressionSessionCompressionWork"
+ "vtCompressionSessionComputeDolbyVisionLevel"
+ "vtCompressionSessionConfirmSpatialAndColorProperties"
+ "vtCompressionSessionCopyFallbackVideoFormatDescriptionExtensions"
+ "vtCompressionSessionCopyPartitionedProperties"
+ "vtCompressionSessionCopyPropertiesHandledByVideoToolbox"
+ "vtCompressionSessionCreateDolbyAtom"
+ "vtCompressionSessionCreateHDRMetadata"
+ "vtCompressionSessionCreatePropertiesHandledByVideoToolbox"
+ "vtCompressionSessionCreateSimplePixelBufferAttributesFromPixelBuffer"
+ "vtCompressionSessionEncodeFrameCommon"
+ "vtCompressionSessionEnsurePixelBufferPoolsAreUpToDate"
+ "vtCompressionSessionFinalize"
+ "vtCompressionSessionIOSurfaceSynchronizationWork"
+ "vtCompressionSessionInitializeMetadataGenerationForHDRSessions"
+ "vtCompressionSessionIsHLG"
+ "vtCompressionSessionIsIPT"
+ "vtCompressionSessionIsPQ"
+ "vtCompressionSessionOutputFrame"
+ "vtCompressionSessionPipelineContextHandleError"
+ "vtCompressionSessionPipelineContextPerformNextWork"
+ "vtCompressionSessionPipelineCreateContext"
+ "vtCompressionSessionPixelTransferSessionWork"
+ "vtCompressionSessionPrepareToEncodeFramesInternal"
+ "vtCompressionSessionPrunePropertiesUnsupportedByVideoEncoder"
+ "vtCompressionSessionRemovePixelFormatWithUndesiredComponentRange"
+ "vtCompressionSessionReorderPixelFormatByTransferability"
+ "vtCompressionSessionSendConfigToCoreAnalytics_block_invoke"
+ "vtCompressionSessionSetHDRFormatAndInitializeMetadataGeneration"
+ "vtCompressionSessionStoreHDRDefaultWrites_block_invoke"
+ "vtCompressionSessionTrackFrameExitedEncoder"
+ "vtCompressionSessionTrackFrameGetHDRData"
+ "vtCompressionSessionTrackFrameGetRateControlInfo"
+ "vtCompressionSessionTrackFrameSetHDRStatistics"
+ "vtCompressionSessionTrackFrameUpdateRateControlInfo"
+ "vtCompressionSessionUpdateAmbientViewingEnvironment"
+ "vtCompressionSessionValidateAmbientViewingEnvironment"
+ "vtCompressionSessionValidateAuxiliaryTypeInfo"
+ "vtCompressionSessionValidateBaselineValue"
+ "vtCompressionSessionValidateCameraCalibrationDataLensCollection"
+ "vtCompressionSessionValidateChromaLocation"
+ "vtCompressionSessionValidateCleanAperture"
+ "vtCompressionSessionValidateColorPrimaries"
+ "vtCompressionSessionValidateContentLightLevelInfo"
+ "vtCompressionSessionValidateDisparityAdjustment"
+ "vtCompressionSessionValidateFieldCount"
+ "vtCompressionSessionValidateFieldDetail"
+ "vtCompressionSessionValidateGammaLevel"
+ "vtCompressionSessionValidateHDRMetadata"
+ "vtCompressionSessionValidateHasAdditionalViews"
+ "vtCompressionSessionValidateHasEyeViewsReversed"
+ "vtCompressionSessionValidateHasLeftStereoEyeView"
+ "vtCompressionSessionValidateHasRightStereoEyeView"
+ "vtCompressionSessionValidateHeroEye"
+ "vtCompressionSessionValidateHorizontalFieldOfView"
+ "vtCompressionSessionValidateICCProfile"
+ "vtCompressionSessionValidateInitialHDRMetadataState"
+ "vtCompressionSessionValidateInputQueueMaxCount"
+ "vtCompressionSessionValidateMasteringDisplayColorVolume"
+ "vtCompressionSessionValidateMultiPassStorage"
+ "vtCompressionSessionValidatePixelAspectRatio"
+ "vtCompressionSessionValidatePixelFormatComponentRange"
+ "vtCompressionSessionValidatePowerLogSessionID"
+ "vtCompressionSessionValidatePrepareEncodedSampleBuffersForPaddedWrites"
+ "vtCompressionSessionValidateProjectionKind"
+ "vtCompressionSessionValidateTransferFunction"
+ "vtCompressionSessionValidateTransportIdentifier"
+ "vtCompressionSessionValidateViewPackingKind"
+ "vtCompressionSessionValidateWarpKind"
+ "vtCompressionSessionValidateYCbCrMatrix"
+ "vtCopyCacheDictionaryForIOService"
+ "vtCopyCodecArrayWithHEVCAddedIfDolbyVisionPresent"
+ "vtCopyCodecList"
+ "vtCopyCodecProfilesArrayAndDictionaryForEmbedded"
+ "vtCopyExpandedDecoderListForWrappers"
+ "vtCopyExpandedEncoderListForWrappers"
+ "vtCopyGuessedMissingColorSpaceAttachmentsFromFormatDescription"
+ "vtCopyPerClientAudioSessionForAuditToken"
+ "vtCopyTemporalFilterCapabilities"
+ "vtCopyTemporalFilterCapabilitiesFromIORegistry"
+ "vtCoreAnalyticsInitialize"
+ "vtCreateAV1DecoderCapabilitiesDictionaryInternal"
+ "vtCreateCompletePixelBufferAttributesFromSourceBufferAttributes"
+ "vtCreateCompletePixelBufferAttributesFromTargetAttributes"
+ "vtCreateDVH1DecoderCapabilitiesDictionaryInternal"
+ "vtCreateDecoderCapabilitiesDictionary"
+ "vtCreateDecoderCapabilitiesDictionaryInternal"
+ "vtCreateDynamicSession"
+ "vtCreateFrameTypesArrayElement"
+ "vtCreateH264OrHEVCCapabilitiesDictionaryForEmbedded"
+ "vtCreateIntermediatePixelBuffer"
+ "vtCreateNamedPixelBufferPool"
+ "vtCreateOnlyTheseFrameDict"
+ "vtCreateOrReuseSharedPixelBufferPool"
+ "vtCreatePixelBufferIfPixelBufferPoolIsCompatibleWithAttributes"
+ "vtCreatePrioritizedPixelFormatListByAlpha"
+ "vtCreateProResDecoderCapabilitiesDictionaryInternal"
+ "vtCreateProfileSupportEntryDictionaryForVP9Embedded"
+ "vtCreateQualityOfServiceTier"
+ "vtCreateReorderedPixelBufferAttributes"
+ "vtCreateResolvedPixelBufferAttributesDictionary"
+ "vtCreateSuggestedQualityOfServiceTiers"
+ "vtCreateTexDescGlobalSample"
+ "vtCreateTexDescGlobalWrite"
+ "vtCreateUsablePixelBufferAttributes"
+ "vtCreateVP9DecoderCapabilitiesDictionaryInternal"
+ "vtCreateVideoFomatDescriptionFromHEVCParameterSets"
+ "vtDecoderSessionCreatePixelBufferWithOptionsInternal"
+ "vtDecoderSessionEmitDecodedFrameCommon"
+ "vtDecoderSessionGetSubDuctPixelBufferPool"
+ "vtDecompressionDuctCreate"
+ "vtDecompressionDuctDecodeSingleFrame"
+ "vtDecompressionDuctEmitDecodedFrame"
+ "vtDecompressionSessionAddPropertyToPartition"
+ "vtDecompressionSessionCopyPartitionedProperties"
+ "vtDecompressionSessionCopyPropertiesHandledByVideoToolbox"
+ "vtDecompressionSessionCreateDestinationForEmittedFrameIfNecessary"
+ "vtDecompressionSessionCreatePropertiesHandledByVideoToolbox"
+ "vtDecompressionSessionDecodeFrameCommon"
+ "vtDecompressionSessionDeterminePolicyForPossibleHDR10PlusContent"
+ "vtDecompressionSessionDeterminePolicyForPossibleHDR10PlusContent_block_invoke"
+ "vtDecompressionSessionFinalize"
+ "vtDecompressionSessionGeneratePerFrameHDRMetadataforEmittedImageBuffer"
+ "vtDecompressionSessionGeneratePerFrameHDRMetadataforEmittedImageBufferCommon"
+ "vtDecompressionSessionHandleAnyFormatDescriptionChange"
+ "vtDecompressionSessionOutputFrame"
+ "vtDecompressionSessionSetupDolbyVision10p4_block_invoke"
+ "vtDecompressionSessionSetupDolbyVision8p1_block_invoke"
+ "vtDecompressionSessionTransferImageToDestinationBufferAndEmitTransferredFrame"
+ "vtDecompressionSessionUpdateAttachmentsForEmittedFrame"
+ "vtDecompressionSetAllowBitstreamToChangeFrameDimensionsIfNecessary"
+ "vtDecompressionSubDuctAsyncPixelTransfer_StartWorkerThreads"
+ "vtDecompressionSubDuctCopyProperty"
+ "vtDecompressionSubDuctEmitTransferredFrame"
+ "vtDecompressionSubDuctEnsurePixelBufferPoolsAreUpToDate"
+ "vtDecompressionSubDuctGetWrapperSessionFrame"
+ "vtDecompressionSubDuctSetProperty"
+ "vtDecompressionSubDuctTrackFrameEnteringCodec"
+ "vtDecompressionSubDuctTrackFrameExitedCodecAndCopyFormatDescription"
+ "vtDecompressionSubDuctTransferFrameAndCallOutputCallback_Asynchronously"
+ "vtDecompressionSubDuctTransferFrameAndCallOutputCallback_Synchronously"
+ "vtDeghostingSessionCreate"
+ "vtDeghostingSessionEmitCommon"
+ "vtDeghostingSessionFinalize"
+ "vtDeghostingSessionGetProcessorCreateInstanceFunction"
+ "vtDeghostingSessionGetProcessorCreateInstanceFunction returned NULL"
+ "vtDeghostingSessionGetProcessorCreateInstanceFunction returned error"
+ "vtDeghostingSessionProcessCommon"
+ "vtDeghostingSessionProcessCommon2"
+ "vtDoesFrameRequireIOSurfaceSynchronization"
+ "vtExtractValuesFromAmbientViewingEnvironmentData"
+ "vtFillHTPCPlanePixelsWithBlack"
+ "vtFillInterchangePlanePixelsWithBlack"
+ "vtFilterRegistryItemByCodecType"
+ "vtFilterRegistryItemByCodecTypeAndVideoDecoderSpecification"
+ "vtFilterRegistryItemByCodecTypeAndVideoEncoderSpecification"
+ "vtFilterRegistryItemByEncoderID"
+ "vtFilterRegistryItemByFilterClassAndFilterSpecification"
+ "vtFilterRegistryItemWithPlatformRestrictions"
+ "vtFindDynamicSession"
+ "vtFormatDescriptionIsPQ"
+ "vtFrameSiloCreateDataFromSampleBuffer"
+ "vtFrameSiloCreateSampleBufferFromData"
+ "vtFrameSiloUpdateFormatDescriptionRangesFromSampleBuffer"
+ "vtGetEnableAsynchronousTransferOnce"
+ "vtGetFirstPixelFormatFromPixelBufferAttributes"
+ "vtGetHEVCDecoderCapabilitiesForFormatDescription"
+ "vtGetPreferInternalDecoders"
+ "vtGetPreferInternalEncoders"
+ "vtGuessMissingColorSpaceAttachmentsGuts"
+ "vtGuestCopyDecoderCapabilities"
+ "vtGuestCopyDecoderListRequest"
+ "vtGuestCopyEncoderListRequest"
+ "vtGuestCopyMotionEstimationProcessorsList"
+ "vtHandleMessageFromHost"
+ "vtInitializeDeviceGroupsAndCache"
+ "vtInitializeMotionEstimationProcessorRegistry"
+ "vtInitializePerClientAudioSessionStorage"
+ "vtInitializeVideoDecoderRegistry"
+ "vtIsFrameCompatibleWithAttributes"
+ "vtIsFrameCompatibleWithColorPropertiesAndDoesFrameHaveDesiredColorRange"
+ "vtIsPixelBufferCompatibleWithAttributes"
+ "vtLoadParavirtualizedMotionEstimationProcessors"
+ "vtLoadParavirtualizedVideoDecoders"
+ "vtLoadParavirtualizedVideoEncoders"
+ "vtLoadTemporalFilterPluginsFromPath"
+ "vtMetalTransferSessionCreatePixelBufferDescriptionWithOptions"
+ "vtMetalTransferSessionCreateSupportedPropertyDictionary"
+ "vtMetalTransferSessionRebuild"
+ "vtMetalTransferSessionTransferImageCommonSync"
+ "vtMotionEstimationProcessorSessionCreateMotionVectorPixelBufferInternal"
+ "vtMotionEstimationSessionCompleteFramesInternal"
+ "vtMotionEstimationSessionFinalize"
+ "vtMotionEstimationSessionGetProcessorCreateInstanceFunction"
+ "vtMotionEstimationSessionGetProcessorCreateInstanceFunction returned NULL"
+ "vtMotionEstimationSessionGetProcessorCreateInstanceFunction returned err"
+ "vtMultiPassStorageCopyStorageToMultiPassStorage"
+ "vtMultiPassStorageCreateEmptyTable"
+ "vtMultiPassStorageCreateTemporaryFile"
+ "vtMultiPassStorageReadTableFromFile"
+ "vtParavirtualizationAddSampleBufferAttachments"
+ "vtParavirtualizationAppendDecoderDescriptionForRegistryItem"
+ "vtParavirtualizationAppendEncoderDescriptionForRegistryItem"
+ "vtParavirtualizationAtomDataReaderCopyCFArray"
+ "vtParavirtualizationAtomDataReaderCopyCFDictionary"
+ "vtParavirtualizationAtomDataReaderCopyCFPropertyList"
+ "vtParavirtualizationAtomDataReaderCopyCFType"
+ "vtParavirtualizationAtomDataReaderCopyCFURL"
+ "vtParavirtualizationAtomDataReaderCopyCGColorSpace"
+ "vtParavirtualizationAtomDataReaderCopyCMFormatDescription"
+ "vtParavirtualizationAtomDataReaderCopyExtensions"
+ "vtParavirtualizationAtomDataReaderCopyKeyValuePair"
+ "vtParavirtualizationAtomDataReaderCopyNotPropagatedSampleBufferAttachments"
+ "vtParavirtualizationAtomDataReaderCopyPropagatedSampleBufferAttachments"
+ "vtParavirtualizationAtomDataReaderCopySampleAttachmentsArray"
+ "vtParavirtualizationAtomDataReaderGetCryptorRecipeDetails"
+ "vtParavirtualizationAtomWriterAppendCFDictionary"
+ "vtParavirtualizationAtomWriterAppendCFType"
+ "vtParavirtualizationAtomWriterAppendCFURL"
+ "vtParavirtualizationAtomWriterAppendKeyValuePairAtom"
+ "vtParavirtualizationAtomWriterAppendSampleSizeArray"
+ "vtParavirtualizationAtomWriterAppendSampleTimingInfo"
+ "vtParavirtualizationCreateCryptor"
+ "vtParavirtualizationCreateSampleBuffer"
+ "vtParavirtualizationFormatDescriptionAtomWriterAppendCMFormatDescription"
+ "vtParavirtualizationGuestDispatchOneMessageFromHost"
+ "vtParavirtualizationGuestSetup_block_invoke"
+ "vtParavirtualizationHostDecoderSession_Finalize"
+ "vtParavirtualizationHostDecoderSession_HandleDecoderCopyProperty"
+ "vtParavirtualizationHostDecoderSession_HandleDecoderCopySerializableProperties"
+ "vtParavirtualizationHostDecoderSession_HandleDecoderCopySupportedPropertyDictionary"
+ "vtParavirtualizationHostDecoderSession_HandleDecoderDecodeFrame"
+ "vtParavirtualizationHostDecoderSession_HandleDecoderDecodeTile"
+ "vtParavirtualizationHostDecoderSession_HandleDecoderFinishDelayedFrames"
+ "vtParavirtualizationHostDecoderSession_HandleDecoderFinishDelayedTiles"
+ "vtParavirtualizationHostDecoderSession_HandleDecoderSetProperties"
+ "vtParavirtualizationHostDecoderSession_HandleDecoderSetProperty"
+ "vtParavirtualizationHostDecoderSession_HandleDecoderStartSession"
+ "vtParavirtualizationHostDecoderSession_HandleDecoderStartTileSession"
+ "vtParavirtualizationHostDecoderSession_HandleInvalidateDecoder"
+ "vtParavirtualizationHostDecoderSession_callMessageToGuestHandler"
+ "vtParavirtualizationHostDecoderSession_lookupAndRetainUUIDForPendingPixelBuffer"
+ "vtParavirtualizationHostDecoderSession_lookupRetainAndForgetPendingTilePixelBuffersAndUUIDsAndMappingIDs"
+ "vtParavirtualizationHostDecoderSession_rememberPendingFramePixelBufferAndUUIDAndMappingID"
+ "vtParavirtualizationHostDecoderSession_rememberPendingTilePixelBufferAndUUIDAndMappingID"
+ "vtParavirtualizationHostDecoderSession_sendMessageToGuest"
+ "vtParavirtualizationHostDecoderSession_sendMessageToGuestAndCopyReplyAndIOSurfaceSync"
+ "vtParavirtualizationHostDecoderSession_sendMessageToGuestAndCopyReplySync"
+ "vtParavirtualizationHostDecoderSession_sendResolvedDecoderPixelBufferAttributesToGuest"
+ "vtParavirtualizationHostEncoderSessionCleanUpAfterEncode"
+ "vtParavirtualizationHostEncoderSession_Finalize"
+ "vtParavirtualizationHostEncoderSession_HandleEncoderBeginPass"
+ "vtParavirtualizationHostEncoderSession_HandleEncoderCompleteFrames"
+ "vtParavirtualizationHostEncoderSession_HandleEncoderCompleteTiles"
+ "vtParavirtualizationHostEncoderSession_HandleEncoderCopyProperty"
+ "vtParavirtualizationHostEncoderSession_HandleEncoderCopySerializableProperties"
+ "vtParavirtualizationHostEncoderSession_HandleEncoderCopySupportedPropertyDictionary"
+ "vtParavirtualizationHostEncoderSession_HandleEncoderEncodeFrame"
+ "vtParavirtualizationHostEncoderSession_HandleEncoderEncodeMultiImageFrame"
+ "vtParavirtualizationHostEncoderSession_HandleEncoderEncodeTile"
+ "vtParavirtualizationHostEncoderSession_HandleEncoderEndPass"
+ "vtParavirtualizationHostEncoderSession_HandleEncoderPrepareToEncodeFrames"
+ "vtParavirtualizationHostEncoderSession_HandleEncoderPrepareToEncodeTiles"
+ "vtParavirtualizationHostEncoderSession_HandleEncoderSetProperties"
+ "vtParavirtualizationHostEncoderSession_HandleEncoderSetProperty"
+ "vtParavirtualizationHostEncoderSession_HandleEncoderStartSession"
+ "vtParavirtualizationHostEncoderSession_HandleEncoderStartTileSession"
+ "vtParavirtualizationHostEncoderSession_HandleInvalidateEncoder"
+ "vtParavirtualizationHostEncoderSession_callMessageToGuestHandler"
+ "vtParavirtualizationHostEncoderSession_lookupRetainAndForgetPendingFramePixelBuffersAndUUIDsAndMappingIDs"
+ "vtParavirtualizationHostEncoderSession_lookupRetainAndForgetPendingTilePixelBuffersAndUUIDsAndMappingIDs"
+ "vtParavirtualizationHostEncoderSession_rememberPendingFramePixelBufferAndUUIDAndMappingID"
+ "vtParavirtualizationHostEncoderSession_rememberPendingFramePixelBuffersAndUUIDsAndMappingIDs"
+ "vtParavirtualizationHostEncoderSession_rememberPendingTilePixelBufferAndUUIDAndMappingID"
+ "vtParavirtualizationHostEncoderSession_sendMessageToGuest"
+ "vtParavirtualizationHostEncoderSession_sendMessageToGuestAndCopyReplySync"
+ "vtParavirtualizationHostMotionEstimationProcessorSession_Finalize"
+ "vtParavirtualizationHostMotionEstimationProcessorSession_HandleCompleteFrames"
+ "vtParavirtualizationHostMotionEstimationProcessorSession_HandleCopyProperty"
+ "vtParavirtualizationHostMotionEstimationProcessorSession_HandleCopySerializableProperties"
+ "vtParavirtualizationHostMotionEstimationProcessorSession_HandleCopySupportedPropertyDictionary"
+ "vtParavirtualizationHostMotionEstimationProcessorSession_HandleInvalidate"
+ "vtParavirtualizationHostMotionEstimationProcessorSession_HandleProcessFrames"
+ "vtParavirtualizationHostMotionEstimationProcessorSession_HandleSetProperties"
+ "vtParavirtualizationHostMotionEstimationProcessorSession_HandleSetProperty"
+ "vtParavirtualizationHostMotionEstimationProcessorSession_HandleStartSession"
+ "vtParavirtualizationHostMotionEstimationProcessorSession_callMessageToGuestHandler"
+ "vtParavirtualizationHostMotionEstimationProcessorSession_cleanUpAfterProcessingInternal"
+ "vtParavirtualizationHostMotionEstimationProcessorSession_copyArrayOfSurfaceMappingIDsToRelinquishAndArrayOfPixelBufferUUIDsToDiscard"
+ "vtParavirtualizationHostMotionEstimationProcessorSession_lookupAndRetainUUIDForPixelBuffer"
+ "vtParavirtualizationHostMotionEstimationProcessorSession_rememberPixelBufferAndUUIDAndMappingID"
+ "vtParavirtualizationHostMotionEstimationProcessorSession_rememberPixelBuffersAndUUIDsAndMappingIDs"
+ "vtParavirtualizationHostMotionEstimationProcessorSession_sendMessageToGuest"
+ "vtParavirtualizationHostMotionEstimationProcessorSession_sendMessageToGuestAndCopyReplyAndIOSurfaceSync"
+ "vtParavirtualizationHostMotionEstimationProcessorSession_sendMessageToGuestAndCopyReplySync"
+ "vtParavirtualizationHostSession_Finalize"
+ "vtParavirtualizationHostSession_callMessageToGuestHandler"
+ "vtParavirtualizationInvalidateHostDecoderSessionAndRemoveItFromHostSession"
+ "vtParavirtualizationInvalidateHostEncoderSessionAndRemoveItFromHostSession"
+ "vtParavirtualizationInvalidateHostMotionEstimationProcessorSessionAndRemoveItFromHostSession"
+ "vtParavirtualizationReplyClerk_Finalize"
+ "vtPerClientAudioSessionCreate"
+ "vtPerClientAudioSessionFinalize"
+ "vtPixelBufferAttributesMediatorCopyMediatedPixelBufferAttributes"
+ "vtPixelBufferAttributesMediatorFinalize"
+ "vtPixelBufferConformerFinalize"
+ "vtPixelFormatContainsYCbCr"
+ "vtPixelRotation_IsValidForSoftware"
+ "vtPixelRotation_Rotate"
+ "vtPixelTransferChainAppendDynamicNode"
+ "vtPixelTransferSessionCanDynamicTransfer"
+ "vtPixelTransferSessionCreateColorPrimariesArray"
+ "vtPixelTransferSessionCreateDownsamplingModesArray"
+ "vtPixelTransferSessionCreateScalingModesArray"
+ "vtPixelTransferSessionCreateSupportedPropertyDictionary"
+ "vtPixelTransferSessionCreateTransferFunctionsArray"
+ "vtPixelTransferSessionCreateYCbCrMatricesArray"
+ "vtPixelTransferSession_BuildColorCorrector"
+ "vtPixelTransferSession_CanReuseChain"
+ "vtPixelTransferSession_PrepareBlitterParameters"
+ "vtPopulateVideoDecoderRegistry"
+ "vtPopulateVideoEncoderRegistry"
+ "vtPreprocessingSessionCopyProperties"
+ "vtPreprocessingSessionCreateProperties"
+ "vtPreprocessingSessionEnsureResolutionIsPartOfSession"
+ "vtPreprocessingSessionFrameExitedEncoder"
+ "vtPreprocessingSessionTrackFrameEnteringEncoder"
+ "vtRateControlReactionObserverCallback"
+ "vtRateControlSessionBeforeEncodeCallback"
+ "vtRateControlSessionBeforeEncodeFrameCallback"
+ "vtRateControlSessionCompleteFramesCallback"
+ "vtRateControlSessionInvalidate"
+ "vtRateControlSessionRegisterBundle"
+ "vtRegisterParavirtualizedMotionEstimationProcessors"
+ "vtRegisterParavirtualizedVideoDecoders"
+ "vtRegisterParavirtualizedVideoEncoders"
+ "vtRegisterTemporalFilterInternal"
+ "vtRegisterVideoDecoderInternal"
+ "vtRegisterVideoDecoderWithInfoKeysAndValuesInternal"
+ "vtRegisterVideoDecoderWithInfoKeysAndValuesInternal2"
+ "vtRegisterVideoEncoderInternal"
+ "vtRegisterVideoEncoderWithInfoKeysAndValuesInternal"
+ "vtSetupNodeInfoTable failed"
+ "vtShouldDecodeFrame"
+ "vtShouldHEVCFlavorsUseWrapperDecoder"
+ "vtTemporalFilterPluginSessionCreateOutputPixelBufferWithOptionsInternal"
+ "vtTemporalFilterSessionAddPropertyToPartition"
+ "vtTemporalFilterSessionCheckPoolCompatibilityWithPixelBufferAttributes"
+ "vtTemporalFilterSessionCopyPartitionedProperties"
+ "vtTemporalFilterSessionCopyPixelBufferForFilterInput"
+ "vtTemporalFilterSessionCopyPixelBufferForFilterOutput"
+ "vtTemporalFilterSessionCopyPropertiesHandledByVideoToolbox"
+ "vtTemporalFilterSessionCreatePropertiesHandledByVideoToolbox"
+ "vtTemporalFilterSessionProcessFrameCommon"
+ "vtTemporalFilterSessionShouldUseSeparateProcess_block_invoke"
+ "vtTemporalFilterSessionTrackFrameEnteringPlugin"
+ "vtTemporalFilterSessionTrackFrameExitingPlugin"
+ "vtTemporalFilterSessionValidateBooleanProperty"
+ "vtTemporalFilterSessionValidateOutputPixelBufferPool"
+ "vtTemporalFilterSessionWaitForCompletion"
+ "vtTemporalFilterShouldUseSeparateProcess_block_invoke"
+ "vtTestMotionEstimationProcessor_createSupportedPropertyDictionary"
+ "vtTileCompressionSessionAddPropertyToPartition"
+ "vtTileCompressionSessionCopyPartitionedProperties"
+ "vtTileCompressionSessionCreateVideoToolboxPropertyDictionary"
+ "vtTileCompressionSessionTrackTileEnteringEncoder_block_invoke"
+ "vtTileCompressionSessionTrackTileLeavingEncoder"
+ "vtTileCompressionSessionTrackTileLeavingEncoder_block_invoke"
+ "vtTileDecompressionSessionAddPropertyToPartition"
+ "vtTileDecompressionSessionCopyPartitionedProperties"
+ "vtTileDecompressionSessionFinalize"
+ "vtTileDecompressionSessionTrackTileEnteringDecoder"
+ "vtTileDecompressionSessionTrackTileLeavingDecoder"
+ "vtTimeStampRetain"
+ "vtTryToLoadVideoDecoder"
+ "vtTryToLoadVideoEncoder"
+ "vtUnregisterParavirtualizedMotionEstimationProcessors"
+ "vtUnregisterParavirtualizedVideoDecoders"
+ "vtUnregisterParavirtualizedVideoEncoders"
+ "vtWritePatternToMemory"
+ "vt_CopyAvg_2vuy_420f"
+ "vt_CopyAvg_2vuy_420v"
+ "vt_CopyAvg_2vuy_f420"
+ "vt_CopyAvg_2vuy_sf20"
+ "vt_CopyAvg_2vuy_sv20"
+ "vt_CopyAvg_2vuy_tf20"
+ "vt_CopyAvg_2vuy_tv20"
+ "vt_CopyAvg_2vuy_v0a8"
+ "vt_CopyAvg_2vuy_x420"
+ "vt_CopyAvg_2vuy_xf20"
+ "vt_CopyAvg_2vuy_y420"
+ "vt_CopyAvg_422f_420f"
+ "vt_CopyAvg_422f_420v"
+ "vt_CopyAvg_422f_f420"
+ "vt_CopyAvg_422f_sf20"
+ "vt_CopyAvg_422f_sv20"
+ "vt_CopyAvg_422f_tf20"
+ "vt_CopyAvg_422f_tv20"
+ "vt_CopyAvg_422f_v0a8"
+ "vt_CopyAvg_422f_x420"
+ "vt_CopyAvg_422f_xf20"
+ "vt_CopyAvg_422f_y420"
+ "vt_CopyAvg_422v_420f"
+ "vt_CopyAvg_422v_420v"
+ "vt_CopyAvg_422v_f420"
+ "vt_CopyAvg_422v_sf20"
+ "vt_CopyAvg_422v_sv20"
+ "vt_CopyAvg_422v_tf20"
+ "vt_CopyAvg_422v_tv20"
+ "vt_CopyAvg_422v_v0a8"
+ "vt_CopyAvg_422v_x420"
+ "vt_CopyAvg_422v_xf20"
+ "vt_CopyAvg_422v_y420"
+ "vt_CopyAvg_444f_2vuy"
+ "vt_CopyAvg_444f_420f"
+ "vt_CopyAvg_444f_420v"
+ "vt_CopyAvg_444f_422f"
+ "vt_CopyAvg_444f_422v"
+ "vt_CopyAvg_444f_f420"
+ "vt_CopyAvg_444f_s2as"
+ "vt_CopyAvg_444f_sf20"
+ "vt_CopyAvg_444f_sf22"
+ "vt_CopyAvg_444f_sv20"
+ "vt_CopyAvg_444f_sv22"
+ "vt_CopyAvg_444f_t2as"
+ "vt_CopyAvg_444f_tf20"
+ "vt_CopyAvg_444f_tf22"
+ "vt_CopyAvg_444f_tv20"
+ "vt_CopyAvg_444f_tv22"
+ "vt_CopyAvg_444f_v0a8"
+ "vt_CopyAvg_444f_v216"
+ "vt_CopyAvg_444f_v2a8"
+ "vt_CopyAvg_444f_x2as"
+ "vt_CopyAvg_444f_x420"
+ "vt_CopyAvg_444f_x422"
+ "vt_CopyAvg_444f_xf20"
+ "vt_CopyAvg_444f_xf22"
+ "vt_CopyAvg_444f_y420"
+ "vt_CopyAvg_444v_2vuy"
+ "vt_CopyAvg_444v_420f"
+ "vt_CopyAvg_444v_420v"
+ "vt_CopyAvg_444v_422f"
+ "vt_CopyAvg_444v_422v"
+ "vt_CopyAvg_444v_f420"
+ "vt_CopyAvg_444v_s2as"
+ "vt_CopyAvg_444v_sf20"
+ "vt_CopyAvg_444v_sf22"
+ "vt_CopyAvg_444v_sv20"
+ "vt_CopyAvg_444v_sv22"
+ "vt_CopyAvg_444v_t2as"
+ "vt_CopyAvg_444v_tf20"
+ "vt_CopyAvg_444v_tf22"
+ "vt_CopyAvg_444v_tv20"
+ "vt_CopyAvg_444v_tv22"
+ "vt_CopyAvg_444v_v0a8"
+ "vt_CopyAvg_444v_v216"
+ "vt_CopyAvg_444v_v2a8"
+ "vt_CopyAvg_444v_x2as"
+ "vt_CopyAvg_444v_x420"
+ "vt_CopyAvg_444v_x422"
+ "vt_CopyAvg_444v_xf20"
+ "vt_CopyAvg_444v_xf22"
+ "vt_CopyAvg_444v_y420"
+ "vt_CopyAvg_s2as_v0a8"
+ "vt_CopyAvg_s4as_s2as"
+ "vt_CopyAvg_s4as_t2as"
+ "vt_CopyAvg_s4as_v0a8"
+ "vt_CopyAvg_s4as_v2a8"
+ "vt_CopyAvg_s4as_x2as"
+ "vt_CopyAvg_sf22_420f"
+ "vt_CopyAvg_sf22_420v"
+ "vt_CopyAvg_sf22_f420"
+ "vt_CopyAvg_sf22_sf20"
+ "vt_CopyAvg_sf22_sv20"
+ "vt_CopyAvg_sf22_tf20"
+ "vt_CopyAvg_sf22_tv20"
+ "vt_CopyAvg_sf22_v0a8"
+ "vt_CopyAvg_sf22_x420"
+ "vt_CopyAvg_sf22_xf20"
+ "vt_CopyAvg_sf22_y420"
+ "vt_CopyAvg_sf44_2vuy"
+ "vt_CopyAvg_sf44_420f"
+ "vt_CopyAvg_sf44_420v"
+ "vt_CopyAvg_sf44_422f"
+ "vt_CopyAvg_sf44_422v"
+ "vt_CopyAvg_sf44_f420"
+ "vt_CopyAvg_sf44_s2as"
+ "vt_CopyAvg_sf44_sf20"
+ "vt_CopyAvg_sf44_sf22"
+ "vt_CopyAvg_sf44_sv20"
+ "vt_CopyAvg_sf44_sv22"
+ "vt_CopyAvg_sf44_t2as"
+ "vt_CopyAvg_sf44_tf20"
+ "vt_CopyAvg_sf44_tf22"
+ "vt_CopyAvg_sf44_tv20"
+ "vt_CopyAvg_sf44_tv22"
+ "vt_CopyAvg_sf44_v0a8"
+ "vt_CopyAvg_sf44_v216"
+ "vt_CopyAvg_sf44_v2a8"
+ "vt_CopyAvg_sf44_x2as"
+ "vt_CopyAvg_sf44_x420"
+ "vt_CopyAvg_sf44_x422"
+ "vt_CopyAvg_sf44_xf20"
+ "vt_CopyAvg_sf44_xf22"
+ "vt_CopyAvg_sf44_y420"
+ "vt_CopyAvg_sv22_420f"
+ "vt_CopyAvg_sv22_420v"
+ "vt_CopyAvg_sv22_f420"
+ "vt_CopyAvg_sv22_sf20"
+ "vt_CopyAvg_sv22_sv20"
+ "vt_CopyAvg_sv22_tf20"
+ "vt_CopyAvg_sv22_tv20"
+ "vt_CopyAvg_sv22_v0a8"
+ "vt_CopyAvg_sv22_x420"
+ "vt_CopyAvg_sv22_xf20"
+ "vt_CopyAvg_sv22_y420"
+ "vt_CopyAvg_sv44_2vuy"
+ "vt_CopyAvg_sv44_420f"
+ "vt_CopyAvg_sv44_420v"
+ "vt_CopyAvg_sv44_422f"
+ "vt_CopyAvg_sv44_422v"
+ "vt_CopyAvg_sv44_f420"
+ "vt_CopyAvg_sv44_s2as"
+ "vt_CopyAvg_sv44_sf20"
+ "vt_CopyAvg_sv44_sf22"
+ "vt_CopyAvg_sv44_sv20"
+ "vt_CopyAvg_sv44_sv22"
+ "vt_CopyAvg_sv44_t2as"
+ "vt_CopyAvg_sv44_tf20"
+ "vt_CopyAvg_sv44_tf22"
+ "vt_CopyAvg_sv44_tv20"
+ "vt_CopyAvg_sv44_tv22"
+ "vt_CopyAvg_sv44_v0a8"
+ "vt_CopyAvg_sv44_v216"
+ "vt_CopyAvg_sv44_v2a8"
+ "vt_CopyAvg_sv44_x2as"
+ "vt_CopyAvg_sv44_x420"
+ "vt_CopyAvg_sv44_x422"
+ "vt_CopyAvg_sv44_xf20"
+ "vt_CopyAvg_sv44_xf22"
+ "vt_CopyAvg_sv44_y420"
+ "vt_CopyAvg_t2as_v0a8"
+ "vt_CopyAvg_t4as_s2as"
+ "vt_CopyAvg_t4as_t2as"
+ "vt_CopyAvg_t4as_v0a8"
+ "vt_CopyAvg_t4as_v2a8"
+ "vt_CopyAvg_t4as_x2as"
+ "vt_CopyAvg_tf22_420f"
+ "vt_CopyAvg_tf22_420v"
+ "vt_CopyAvg_tf22_f420"
+ "vt_CopyAvg_tf22_sf20"
+ "vt_CopyAvg_tf22_sv20"
+ "vt_CopyAvg_tf22_tf20"
+ "vt_CopyAvg_tf22_tv20"
+ "vt_CopyAvg_tf22_v0a8"
+ "vt_CopyAvg_tf22_x420"
+ "vt_CopyAvg_tf22_xf20"
+ "vt_CopyAvg_tf22_y420"
+ "vt_CopyAvg_tf44_2vuy"
+ "vt_CopyAvg_tf44_420f"
+ "vt_CopyAvg_tf44_420v"
+ "vt_CopyAvg_tf44_422f"
+ "vt_CopyAvg_tf44_422v"
+ "vt_CopyAvg_tf44_f420"
+ "vt_CopyAvg_tf44_s2as"
+ "vt_CopyAvg_tf44_sf20"
+ "vt_CopyAvg_tf44_sf22"
+ "vt_CopyAvg_tf44_sv20"
+ "vt_CopyAvg_tf44_sv22"
+ "vt_CopyAvg_tf44_t2as"
+ "vt_CopyAvg_tf44_tf20"
+ "vt_CopyAvg_tf44_tf22"
+ "vt_CopyAvg_tf44_tv20"
+ "vt_CopyAvg_tf44_tv22"
+ "vt_CopyAvg_tf44_v0a8"
+ "vt_CopyAvg_tf44_v216"
+ "vt_CopyAvg_tf44_v2a8"
+ "vt_CopyAvg_tf44_x2as"
+ "vt_CopyAvg_tf44_x420"
+ "vt_CopyAvg_tf44_x422"
+ "vt_CopyAvg_tf44_xf20"
+ "vt_CopyAvg_tf44_xf22"
+ "vt_CopyAvg_tf44_y420"
+ "vt_CopyAvg_tv22_420f"
+ "vt_CopyAvg_tv22_420v"
+ "vt_CopyAvg_tv22_f420"
+ "vt_CopyAvg_tv22_sf20"
+ "vt_CopyAvg_tv22_sv20"
+ "vt_CopyAvg_tv22_tf20"
+ "vt_CopyAvg_tv22_tv20"
+ "vt_CopyAvg_tv22_v0a8"
+ "vt_CopyAvg_tv22_x420"
+ "vt_CopyAvg_tv22_xf20"
+ "vt_CopyAvg_tv22_y420"
+ "vt_CopyAvg_tv44_2vuy"
+ "vt_CopyAvg_tv44_420f"
+ "vt_CopyAvg_tv44_420v"
+ "vt_CopyAvg_tv44_422f"
+ "vt_CopyAvg_tv44_422v"
+ "vt_CopyAvg_tv44_f420"
+ "vt_CopyAvg_tv44_s2as"
+ "vt_CopyAvg_tv44_sf20"
+ "vt_CopyAvg_tv44_sf22"
+ "vt_CopyAvg_tv44_sv20"
+ "vt_CopyAvg_tv44_sv22"
+ "vt_CopyAvg_tv44_t2as"
+ "vt_CopyAvg_tv44_tf20"
+ "vt_CopyAvg_tv44_tf22"
+ "vt_CopyAvg_tv44_tv20"
+ "vt_CopyAvg_tv44_tv22"
+ "vt_CopyAvg_tv44_v0a8"
+ "vt_CopyAvg_tv44_v216"
+ "vt_CopyAvg_tv44_v2a8"
+ "vt_CopyAvg_tv44_x2as"
+ "vt_CopyAvg_tv44_x420"
+ "vt_CopyAvg_tv44_x422"
+ "vt_CopyAvg_tv44_xf20"
+ "vt_CopyAvg_tv44_xf22"
+ "vt_CopyAvg_tv44_y420"
+ "vt_CopyAvg_v210_420f"
+ "vt_CopyAvg_v210_420v"
+ "vt_CopyAvg_v210_x420"
+ "vt_CopyAvg_v210_xf20"
+ "vt_CopyAvg_v216_420f"
+ "vt_CopyAvg_v216_420v"
+ "vt_CopyAvg_v216_f420"
+ "vt_CopyAvg_v216_sf20"
+ "vt_CopyAvg_v216_sv20"
+ "vt_CopyAvg_v216_tf20"
+ "vt_CopyAvg_v216_tv20"
+ "vt_CopyAvg_v216_v0a8"
+ "vt_CopyAvg_v216_x420"
+ "vt_CopyAvg_v216_xf20"
+ "vt_CopyAvg_v216_y420"
+ "vt_CopyAvg_v2a8_v0a8"
+ "vt_CopyAvg_v4a8_s2as"
+ "vt_CopyAvg_v4a8_t2as"
+ "vt_CopyAvg_v4a8_v0a8"
+ "vt_CopyAvg_v4a8_v2a8"
+ "vt_CopyAvg_v4a8_x2as"
+ "vt_CopyAvg_x2as_v0a8"
+ "vt_CopyAvg_x422_420f"
+ "vt_CopyAvg_x422_420v"
+ "vt_CopyAvg_x422_f420"
+ "vt_CopyAvg_x422_sf20"
+ "vt_CopyAvg_x422_sv20"
+ "vt_CopyAvg_x422_tf20"
+ "vt_CopyAvg_x422_tv20"
+ "vt_CopyAvg_x422_v0a8"
+ "vt_CopyAvg_x422_x420"
+ "vt_CopyAvg_x422_xf20"
+ "vt_CopyAvg_x422_y420"
+ "vt_CopyAvg_x444_2vuy"
+ "vt_CopyAvg_x444_420f"
+ "vt_CopyAvg_x444_420v"
+ "vt_CopyAvg_x444_422f"
+ "vt_CopyAvg_x444_422v"
+ "vt_CopyAvg_x444_f420"
+ "vt_CopyAvg_x444_s2as"
+ "vt_CopyAvg_x444_sf20"
+ "vt_CopyAvg_x444_sf22"
+ "vt_CopyAvg_x444_sv20"
+ "vt_CopyAvg_x444_sv22"
+ "vt_CopyAvg_x444_t2as"
+ "vt_CopyAvg_x444_tf20"
+ "vt_CopyAvg_x444_tf22"
+ "vt_CopyAvg_x444_tv20"
+ "vt_CopyAvg_x444_tv22"
+ "vt_CopyAvg_x444_v0a8"
+ "vt_CopyAvg_x444_v216"
+ "vt_CopyAvg_x444_v2a8"
+ "vt_CopyAvg_x444_x2as"
+ "vt_CopyAvg_x444_x420"
+ "vt_CopyAvg_x444_x422"
+ "vt_CopyAvg_x444_xf20"
+ "vt_CopyAvg_x444_xf22"
+ "vt_CopyAvg_x444_y420"
+ "vt_CopyAvg_x4as_s2as"
+ "vt_CopyAvg_x4as_t2as"
+ "vt_CopyAvg_x4as_v0a8"
+ "vt_CopyAvg_x4as_v2a8"
+ "vt_CopyAvg_x4as_x2as"
+ "vt_CopyAvg_xf22_420f"
+ "vt_CopyAvg_xf22_420v"
+ "vt_CopyAvg_xf22_f420"
+ "vt_CopyAvg_xf22_sf20"
+ "vt_CopyAvg_xf22_sv20"
+ "vt_CopyAvg_xf22_tf20"
+ "vt_CopyAvg_xf22_tv20"
+ "vt_CopyAvg_xf22_v0a8"
+ "vt_CopyAvg_xf22_x420"
+ "vt_CopyAvg_xf22_xf20"
+ "vt_CopyAvg_xf22_y420"
+ "vt_CopyAvg_xf44_2vuy"
+ "vt_CopyAvg_xf44_420f"
+ "vt_CopyAvg_xf44_420v"
+ "vt_CopyAvg_xf44_422f"
+ "vt_CopyAvg_xf44_422v"
+ "vt_CopyAvg_xf44_f420"
+ "vt_CopyAvg_xf44_s2as"
+ "vt_CopyAvg_xf44_sf20"
+ "vt_CopyAvg_xf44_sf22"
+ "vt_CopyAvg_xf44_sv20"
+ "vt_CopyAvg_xf44_sv22"
+ "vt_CopyAvg_xf44_t2as"
+ "vt_CopyAvg_xf44_tf20"
+ "vt_CopyAvg_xf44_tf22"
+ "vt_CopyAvg_xf44_tv20"
+ "vt_CopyAvg_xf44_tv22"
+ "vt_CopyAvg_xf44_v0a8"
+ "vt_CopyAvg_xf44_v216"
+ "vt_CopyAvg_xf44_v2a8"
+ "vt_CopyAvg_xf44_x2as"
+ "vt_CopyAvg_xf44_x420"
+ "vt_CopyAvg_xf44_x422"
+ "vt_CopyAvg_xf44_xf20"
+ "vt_CopyAvg_xf44_xf22"
+ "vt_CopyAvg_xf44_y420"
+ "vt_CopyAvg_y408_420f"
+ "vt_CopyAvg_y408_420v"
+ "vt_CopyAvg_y408_422f"
+ "vt_CopyAvg_y408_422v"
+ "vt_CopyAvg_y408_f420"
+ "vt_CopyAvg_y408_s2as"
+ "vt_CopyAvg_y408_sf20"
+ "vt_CopyAvg_y408_sf22"
+ "vt_CopyAvg_y408_sv20"
+ "vt_CopyAvg_y408_sv22"
+ "vt_CopyAvg_y408_t2as"
+ "vt_CopyAvg_y408_tf20"
+ "vt_CopyAvg_y408_tf22"
+ "vt_CopyAvg_y408_tv20"
+ "vt_CopyAvg_y408_tv22"
+ "vt_CopyAvg_y408_v0a8"
+ "vt_CopyAvg_y408_v2a8"
+ "vt_CopyAvg_y408_x2as"
+ "vt_CopyAvg_y408_x420"
+ "vt_CopyAvg_y408_x422"
+ "vt_CopyAvg_y408_xf20"
+ "vt_CopyAvg_y408_xf22"
+ "vt_CopyAvg_y408_y420"
+ "vt_CopyAvg_y416_420f"
+ "vt_CopyAvg_y416_420v"
+ "vt_CopyAvg_y416_422f"
+ "vt_CopyAvg_y416_422v"
+ "vt_CopyAvg_y416_f420"
+ "vt_CopyAvg_y416_s2as"
+ "vt_CopyAvg_y416_sf20"
+ "vt_CopyAvg_y416_sf22"
+ "vt_CopyAvg_y416_sv20"
+ "vt_CopyAvg_y416_sv22"
+ "vt_CopyAvg_y416_t2as"
+ "vt_CopyAvg_y416_tf20"
+ "vt_CopyAvg_y416_tf22"
+ "vt_CopyAvg_y416_tv20"
+ "vt_CopyAvg_y416_tv22"
+ "vt_CopyAvg_y416_v0a8"
+ "vt_CopyAvg_y416_v2a8"
+ "vt_CopyAvg_y416_x2as"
+ "vt_CopyAvg_y416_x420"
+ "vt_CopyAvg_y416_x422"
+ "vt_CopyAvg_y416_xf20"
+ "vt_CopyAvg_y416_xf22"
+ "vt_CopyAvg_y416_y420"
+ "vt_CopyAvg_yuvf_420v"
+ "vt_CopyAvg_yuvs_420f"
+ "vt_CopyAvg_yuvs_420v"
+ "vt_CopyAvg_yuvs_420v_vec"
+ "vt_CopyAvg_yuvs_y420"
+ "vt_CopyDec_2vuy_420f"
+ "vt_CopyDec_2vuy_420v"
+ "vt_CopyDec_2vuy_f420"
+ "vt_CopyDec_2vuy_sf20"
+ "vt_CopyDec_2vuy_sv20"
+ "vt_CopyDec_2vuy_tf20"
+ "vt_CopyDec_2vuy_tv20"
+ "vt_CopyDec_2vuy_v0a8"
+ "vt_CopyDec_2vuy_x420"
+ "vt_CopyDec_2vuy_xf20"
+ "vt_CopyDec_422f_420f"
+ "vt_CopyDec_422f_420v"
+ "vt_CopyDec_422f_f420"
+ "vt_CopyDec_422f_sf20"
+ "vt_CopyDec_422f_sv20"
+ "vt_CopyDec_422f_tf20"
+ "vt_CopyDec_422f_tv20"
+ "vt_CopyDec_422f_v0a8"
+ "vt_CopyDec_422f_x420"
+ "vt_CopyDec_422f_xf20"
+ "vt_CopyDec_422f_y420"
+ "vt_CopyDec_422v_420f"
+ "vt_CopyDec_422v_420v"
+ "vt_CopyDec_422v_f420"
+ "vt_CopyDec_422v_sf20"
+ "vt_CopyDec_422v_sv20"
+ "vt_CopyDec_422v_tf20"
+ "vt_CopyDec_422v_tv20"
+ "vt_CopyDec_422v_v0a8"
+ "vt_CopyDec_422v_x420"
+ "vt_CopyDec_422v_xf20"
+ "vt_CopyDec_422v_y420"
+ "vt_CopyDec_444f_2vuy"
+ "vt_CopyDec_444f_420f"
+ "vt_CopyDec_444f_420v"
+ "vt_CopyDec_444f_422f"
+ "vt_CopyDec_444f_422v"
+ "vt_CopyDec_444f_f420"
+ "vt_CopyDec_444f_s2as"
+ "vt_CopyDec_444f_sf20"
+ "vt_CopyDec_444f_sf22"
+ "vt_CopyDec_444f_sv20"
+ "vt_CopyDec_444f_sv22"
+ "vt_CopyDec_444f_t2as"
+ "vt_CopyDec_444f_tf20"
+ "vt_CopyDec_444f_tf22"
+ "vt_CopyDec_444f_tv20"
+ "vt_CopyDec_444f_tv22"
+ "vt_CopyDec_444f_v0a8"
+ "vt_CopyDec_444f_v216"
+ "vt_CopyDec_444f_v2a8"
+ "vt_CopyDec_444f_x2as"
+ "vt_CopyDec_444f_x420"
+ "vt_CopyDec_444f_x422"
+ "vt_CopyDec_444f_xf20"
+ "vt_CopyDec_444f_xf22"
+ "vt_CopyDec_444f_y420"
+ "vt_CopyDec_444v_2vuy"
+ "vt_CopyDec_444v_420f"
+ "vt_CopyDec_444v_420v"
+ "vt_CopyDec_444v_422f"
+ "vt_CopyDec_444v_422v"
+ "vt_CopyDec_444v_f420"
+ "vt_CopyDec_444v_s2as"
+ "vt_CopyDec_444v_sf20"
+ "vt_CopyDec_444v_sf22"
+ "vt_CopyDec_444v_sv20"
+ "vt_CopyDec_444v_sv22"
+ "vt_CopyDec_444v_t2as"
+ "vt_CopyDec_444v_tf20"
+ "vt_CopyDec_444v_tf22"
+ "vt_CopyDec_444v_tv20"
+ "vt_CopyDec_444v_tv22"
+ "vt_CopyDec_444v_v0a8"
+ "vt_CopyDec_444v_v216"
+ "vt_CopyDec_444v_v2a8"
+ "vt_CopyDec_444v_x2as"
+ "vt_CopyDec_444v_x420"
+ "vt_CopyDec_444v_x422"
+ "vt_CopyDec_444v_xf20"
+ "vt_CopyDec_444v_xf22"
+ "vt_CopyDec_444v_y420"
+ "vt_CopyDec_s2as_v0a8"
+ "vt_CopyDec_s4as_s2as"
+ "vt_CopyDec_s4as_t2as"
+ "vt_CopyDec_s4as_v0a8"
+ "vt_CopyDec_s4as_v2a8"
+ "vt_CopyDec_s4as_x2as"
+ "vt_CopyDec_sf22_420f"
+ "vt_CopyDec_sf22_420v"
+ "vt_CopyDec_sf22_f420"
+ "vt_CopyDec_sf22_sf20"
+ "vt_CopyDec_sf22_sv20"
+ "vt_CopyDec_sf22_tf20"
+ "vt_CopyDec_sf22_tv20"
+ "vt_CopyDec_sf22_v0a8"
+ "vt_CopyDec_sf22_x420"
+ "vt_CopyDec_sf22_xf20"
+ "vt_CopyDec_sf22_y420"
+ "vt_CopyDec_sf44_2vuy"
+ "vt_CopyDec_sf44_420f"
+ "vt_CopyDec_sf44_420v"
+ "vt_CopyDec_sf44_422f"
+ "vt_CopyDec_sf44_422v"
+ "vt_CopyDec_sf44_f420"
+ "vt_CopyDec_sf44_s2as"
+ "vt_CopyDec_sf44_sf20"
+ "vt_CopyDec_sf44_sf22"
+ "vt_CopyDec_sf44_sv20"
+ "vt_CopyDec_sf44_sv22"
+ "vt_CopyDec_sf44_t2as"
+ "vt_CopyDec_sf44_tf20"
+ "vt_CopyDec_sf44_tf22"
+ "vt_CopyDec_sf44_tv20"
+ "vt_CopyDec_sf44_tv22"
+ "vt_CopyDec_sf44_v0a8"
+ "vt_CopyDec_sf44_v216"
+ "vt_CopyDec_sf44_v2a8"
+ "vt_CopyDec_sf44_x2as"
+ "vt_CopyDec_sf44_x420"
+ "vt_CopyDec_sf44_x422"
+ "vt_CopyDec_sf44_xf20"
+ "vt_CopyDec_sf44_xf22"
+ "vt_CopyDec_sf44_y420"
+ "vt_CopyDec_sv22_420f"
+ "vt_CopyDec_sv22_420v"
+ "vt_CopyDec_sv22_f420"
+ "vt_CopyDec_sv22_sf20"
+ "vt_CopyDec_sv22_sv20"
+ "vt_CopyDec_sv22_tf20"
+ "vt_CopyDec_sv22_tv20"
+ "vt_CopyDec_sv22_v0a8"
+ "vt_CopyDec_sv22_x420"
+ "vt_CopyDec_sv22_xf20"
+ "vt_CopyDec_sv22_y420"
+ "vt_CopyDec_sv44_2vuy"
+ "vt_CopyDec_sv44_420f"
+ "vt_CopyDec_sv44_420v"
+ "vt_CopyDec_sv44_422f"
+ "vt_CopyDec_sv44_422v"
+ "vt_CopyDec_sv44_f420"
+ "vt_CopyDec_sv44_s2as"
+ "vt_CopyDec_sv44_sf20"
+ "vt_CopyDec_sv44_sf22"
+ "vt_CopyDec_sv44_sv20"
+ "vt_CopyDec_sv44_sv22"
+ "vt_CopyDec_sv44_t2as"
+ "vt_CopyDec_sv44_tf20"
+ "vt_CopyDec_sv44_tf22"
+ "vt_CopyDec_sv44_tv20"
+ "vt_CopyDec_sv44_tv22"
+ "vt_CopyDec_sv44_v0a8"
+ "vt_CopyDec_sv44_v216"
+ "vt_CopyDec_sv44_v2a8"
+ "vt_CopyDec_sv44_x2as"
+ "vt_CopyDec_sv44_x420"
+ "vt_CopyDec_sv44_x422"
+ "vt_CopyDec_sv44_xf20"
+ "vt_CopyDec_sv44_xf22"
+ "vt_CopyDec_sv44_y420"
+ "vt_CopyDec_t2as_v0a8"
+ "vt_CopyDec_t4as_s2as"
+ "vt_CopyDec_t4as_t2as"
+ "vt_CopyDec_t4as_v0a8"
+ "vt_CopyDec_t4as_v2a8"
+ "vt_CopyDec_t4as_x2as"
+ "vt_CopyDec_tf22_420f"
+ "vt_CopyDec_tf22_420v"
+ "vt_CopyDec_tf22_f420"
+ "vt_CopyDec_tf22_sf20"
+ "vt_CopyDec_tf22_sv20"
+ "vt_CopyDec_tf22_tf20"
+ "vt_CopyDec_tf22_tv20"
+ "vt_CopyDec_tf22_v0a8"
+ "vt_CopyDec_tf22_x420"
+ "vt_CopyDec_tf22_xf20"
+ "vt_CopyDec_tf22_y420"
+ "vt_CopyDec_tf44_2vuy"
+ "vt_CopyDec_tf44_420f"
+ "vt_CopyDec_tf44_420v"
+ "vt_CopyDec_tf44_422f"
+ "vt_CopyDec_tf44_422v"
+ "vt_CopyDec_tf44_f420"
+ "vt_CopyDec_tf44_s2as"
+ "vt_CopyDec_tf44_sf20"
+ "vt_CopyDec_tf44_sf22"
+ "vt_CopyDec_tf44_sv20"
+ "vt_CopyDec_tf44_sv22"
+ "vt_CopyDec_tf44_t2as"
+ "vt_CopyDec_tf44_tf20"
+ "vt_CopyDec_tf44_tf22"
+ "vt_CopyDec_tf44_tv20"
+ "vt_CopyDec_tf44_tv22"
+ "vt_CopyDec_tf44_v0a8"
+ "vt_CopyDec_tf44_v216"
+ "vt_CopyDec_tf44_v2a8"
+ "vt_CopyDec_tf44_x2as"
+ "vt_CopyDec_tf44_x420"
+ "vt_CopyDec_tf44_x422"
+ "vt_CopyDec_tf44_xf20"
+ "vt_CopyDec_tf44_xf22"
+ "vt_CopyDec_tf44_y420"
+ "vt_CopyDec_tv22_420f"
+ "vt_CopyDec_tv22_420v"
+ "vt_CopyDec_tv22_f420"
+ "vt_CopyDec_tv22_sf20"
+ "vt_CopyDec_tv22_sv20"
+ "vt_CopyDec_tv22_tf20"
+ "vt_CopyDec_tv22_tv20"
+ "vt_CopyDec_tv22_v0a8"
+ "vt_CopyDec_tv22_x420"
+ "vt_CopyDec_tv22_xf20"
+ "vt_CopyDec_tv22_y420"
+ "vt_CopyDec_tv44_2vuy"
+ "vt_CopyDec_tv44_420f"
+ "vt_CopyDec_tv44_420v"
+ "vt_CopyDec_tv44_422f"
+ "vt_CopyDec_tv44_422v"
+ "vt_CopyDec_tv44_f420"
+ "vt_CopyDec_tv44_s2as"
+ "vt_CopyDec_tv44_sf20"
+ "vt_CopyDec_tv44_sf22"
+ "vt_CopyDec_tv44_sv20"
+ "vt_CopyDec_tv44_sv22"
+ "vt_CopyDec_tv44_t2as"
+ "vt_CopyDec_tv44_tf20"
+ "vt_CopyDec_tv44_tf22"
+ "vt_CopyDec_tv44_tv20"
+ "vt_CopyDec_tv44_tv22"
+ "vt_CopyDec_tv44_v0a8"
+ "vt_CopyDec_tv44_v216"
+ "vt_CopyDec_tv44_v2a8"
+ "vt_CopyDec_tv44_x2as"
+ "vt_CopyDec_tv44_x420"
+ "vt_CopyDec_tv44_x422"
+ "vt_CopyDec_tv44_xf20"
+ "vt_CopyDec_tv44_xf22"
+ "vt_CopyDec_tv44_y420"
+ "vt_CopyDec_v210_420f"
+ "vt_CopyDec_v210_420v"
+ "vt_CopyDec_v210_x420"
+ "vt_CopyDec_v210_xf20"
+ "vt_CopyDec_v216_420f"
+ "vt_CopyDec_v216_420v"
+ "vt_CopyDec_v216_f420"
+ "vt_CopyDec_v216_sf20"
+ "vt_CopyDec_v216_sv20"
+ "vt_CopyDec_v216_tf20"
+ "vt_CopyDec_v216_tv20"
+ "vt_CopyDec_v216_v0a8"
+ "vt_CopyDec_v216_x420"
+ "vt_CopyDec_v216_xf20"
+ "vt_CopyDec_v216_y420"
+ "vt_CopyDec_v2a8_v0a8"
+ "vt_CopyDec_v4a8_s2as"
+ "vt_CopyDec_v4a8_t2as"
+ "vt_CopyDec_v4a8_v0a8"
+ "vt_CopyDec_v4a8_v2a8"
+ "vt_CopyDec_v4a8_x2as"
+ "vt_CopyDec_x2as_v0a8"
+ "vt_CopyDec_x422_420f"
+ "vt_CopyDec_x422_420v"
+ "vt_CopyDec_x422_f420"
+ "vt_CopyDec_x422_sf20"
+ "vt_CopyDec_x422_sv20"
+ "vt_CopyDec_x422_tf20"
+ "vt_CopyDec_x422_tv20"
+ "vt_CopyDec_x422_v0a8"
+ "vt_CopyDec_x422_x420"
+ "vt_CopyDec_x422_xf20"
+ "vt_CopyDec_x422_y420"
+ "vt_CopyDec_x444_2vuy"
+ "vt_CopyDec_x444_420f"
+ "vt_CopyDec_x444_420v"
+ "vt_CopyDec_x444_422f"
+ "vt_CopyDec_x444_422v"
+ "vt_CopyDec_x444_f420"
+ "vt_CopyDec_x444_s2as"
+ "vt_CopyDec_x444_sf20"
+ "vt_CopyDec_x444_sf22"
+ "vt_CopyDec_x444_sv20"
+ "vt_CopyDec_x444_sv22"
+ "vt_CopyDec_x444_t2as"
+ "vt_CopyDec_x444_tf20"
+ "vt_CopyDec_x444_tf22"
+ "vt_CopyDec_x444_tv20"
+ "vt_CopyDec_x444_tv22"
+ "vt_CopyDec_x444_v0a8"
+ "vt_CopyDec_x444_v216"
+ "vt_CopyDec_x444_v2a8"
+ "vt_CopyDec_x444_x2as"
+ "vt_CopyDec_x444_x420"
+ "vt_CopyDec_x444_x422"
+ "vt_CopyDec_x444_xf20"
+ "vt_CopyDec_x444_xf22"
+ "vt_CopyDec_x444_y420"
+ "vt_CopyDec_x4as_s2as"
+ "vt_CopyDec_x4as_t2as"
+ "vt_CopyDec_x4as_v0a8"
+ "vt_CopyDec_x4as_v2a8"
+ "vt_CopyDec_x4as_x2as"
+ "vt_CopyDec_xf22_420f"
+ "vt_CopyDec_xf22_420v"
+ "vt_CopyDec_xf22_f420"
+ "vt_CopyDec_xf22_sf20"
+ "vt_CopyDec_xf22_sv20"
+ "vt_CopyDec_xf22_tf20"
+ "vt_CopyDec_xf22_tv20"
+ "vt_CopyDec_xf22_v0a8"
+ "vt_CopyDec_xf22_x420"
+ "vt_CopyDec_xf22_xf20"
+ "vt_CopyDec_xf22_y420"
+ "vt_CopyDec_xf44_2vuy"
+ "vt_CopyDec_xf44_420f"
+ "vt_CopyDec_xf44_420v"
+ "vt_CopyDec_xf44_422f"
+ "vt_CopyDec_xf44_422v"
+ "vt_CopyDec_xf44_f420"
+ "vt_CopyDec_xf44_s2as"
+ "vt_CopyDec_xf44_sf20"
+ "vt_CopyDec_xf44_sf22"
+ "vt_CopyDec_xf44_sv20"
+ "vt_CopyDec_xf44_sv22"
+ "vt_CopyDec_xf44_t2as"
+ "vt_CopyDec_xf44_tf20"
+ "vt_CopyDec_xf44_tf22"
+ "vt_CopyDec_xf44_tv20"
+ "vt_CopyDec_xf44_tv22"
+ "vt_CopyDec_xf44_v0a8"
+ "vt_CopyDec_xf44_v216"
+ "vt_CopyDec_xf44_v2a8"
+ "vt_CopyDec_xf44_x2as"
+ "vt_CopyDec_xf44_x420"
+ "vt_CopyDec_xf44_x422"
+ "vt_CopyDec_xf44_xf20"
+ "vt_CopyDec_xf44_xf22"
+ "vt_CopyDec_xf44_y420"
+ "vt_CopyDec_y408_420f"
+ "vt_CopyDec_y408_420v"
+ "vt_CopyDec_y408_422f"
+ "vt_CopyDec_y408_422v"
+ "vt_CopyDec_y408_f420"
+ "vt_CopyDec_y408_s2as"
+ "vt_CopyDec_y408_sf20"
+ "vt_CopyDec_y408_sf22"
+ "vt_CopyDec_y408_sv20"
+ "vt_CopyDec_y408_sv22"
+ "vt_CopyDec_y408_t2as"
+ "vt_CopyDec_y408_tf20"
+ "vt_CopyDec_y408_tf22"
+ "vt_CopyDec_y408_tv20"
+ "vt_CopyDec_y408_tv22"
+ "vt_CopyDec_y408_v0a8"
+ "vt_CopyDec_y408_v2a8"
+ "vt_CopyDec_y408_x2as"
+ "vt_CopyDec_y408_x420"
+ "vt_CopyDec_y408_x422"
+ "vt_CopyDec_y408_xf20"
+ "vt_CopyDec_y408_xf22"
+ "vt_CopyDec_y408_y420"
+ "vt_CopyDec_y416_420f"
+ "vt_CopyDec_y416_420v"
+ "vt_CopyDec_y416_422f"
+ "vt_CopyDec_y416_422v"
+ "vt_CopyDec_y416_f420"
+ "vt_CopyDec_y416_s2as"
+ "vt_CopyDec_y416_sf20"
+ "vt_CopyDec_y416_sf22"
+ "vt_CopyDec_y416_sv20"
+ "vt_CopyDec_y416_sv22"
+ "vt_CopyDec_y416_t2as"
+ "vt_CopyDec_y416_tf20"
+ "vt_CopyDec_y416_tf22"
+ "vt_CopyDec_y416_tv20"
+ "vt_CopyDec_y416_tv22"
+ "vt_CopyDec_y416_v0a8"
+ "vt_CopyDec_y416_v2a8"
+ "vt_CopyDec_y416_x2as"
+ "vt_CopyDec_y416_x420"
+ "vt_CopyDec_y416_x422"
+ "vt_CopyDec_y416_xf20"
+ "vt_CopyDec_y416_xf22"
+ "vt_CopyDec_y416_y420"
+ "vt_CopyDec_yuvf_420v"
+ "vt_CopyDec_yuvs_420f"
+ "vt_CopyDec_yuvs_420v"
+ "vt_CopyDec_yuvs_y420"
+ "vt_Copy_10bitBiPlanarYUV422_v210"
+ "vt_Copy_24RGB_2vuyITU2020"
+ "vt_Copy_24RGB_2vuyITU601"
+ "vt_Copy_24RGB_2vuyITU709"
+ "vt_Copy_24RGB_420fITU2020"
+ "vt_Copy_24RGB_420fITU601"
+ "vt_Copy_24RGB_420fITU709"
+ "vt_Copy_24RGB_420vITU2020"
+ "vt_Copy_24RGB_420vITU601"
+ "vt_Copy_24RGB_420vITU709"
+ "vt_Copy_24RGB_a2vyITU2020"
+ "vt_Copy_24RGB_a2vyITU601"
+ "vt_Copy_24RGB_a2vyITU709"
+ "vt_Copy_24RGB_yuvsITU2020"
+ "vt_Copy_24RGB_yuvsITU601"
+ "vt_Copy_24RGB_yuvsITU709"
+ "vt_Copy_2vuyITU2020_24RGB"
+ "vt_Copy_2vuyITU2020_32ARGB"
+ "vt_Copy_2vuyITU2020_32BGRA"
+ "vt_Copy_2vuyITU2020_8GRAYSCALE"
+ "vt_Copy_2vuyITU601_24RGB"
+ "vt_Copy_2vuyITU601_32ARGB"
+ "vt_Copy_2vuyITU601_32BGRA"
+ "vt_Copy_2vuyITU601_8GRAYSCALE"
+ "vt_Copy_2vuyITU709_24RGB"
+ "vt_Copy_2vuyITU709_32ARGB"
+ "vt_Copy_2vuyITU709_32BGRA"
+ "vt_Copy_2vuyITU709_8GRAYSCALE"
+ "vt_Copy_2vuy_420f"
+ "vt_Copy_2vuy_420v"
+ "vt_Copy_2vuy_422f"
+ "vt_Copy_2vuy_422v"
+ "vt_Copy_2vuy_444f"
+ "vt_Copy_2vuy_444v"
+ "vt_Copy_2vuy_f420"
+ "vt_Copy_2vuy_s2as"
+ "vt_Copy_2vuy_s4as"
+ "vt_Copy_2vuy_sf20"
+ "vt_Copy_2vuy_sf22"
+ "vt_Copy_2vuy_sf44"
+ "vt_Copy_2vuy_sv20"
+ "vt_Copy_2vuy_sv22"
+ "vt_Copy_2vuy_sv44"
+ "vt_Copy_2vuy_t2as"
+ "vt_Copy_2vuy_t4as"
+ "vt_Copy_2vuy_tf20"
+ "vt_Copy_2vuy_tf22"
+ "vt_Copy_2vuy_tf44"
+ "vt_Copy_2vuy_tv20"
+ "vt_Copy_2vuy_tv22"
+ "vt_Copy_2vuy_tv44"
+ "vt_Copy_2vuy_v0a8"
+ "vt_Copy_2vuy_v2a8"
+ "vt_Copy_2vuy_v4a8"
+ "vt_Copy_2vuy_x2as"
+ "vt_Copy_2vuy_x420"
+ "vt_Copy_2vuy_x422"
+ "vt_Copy_2vuy_x444"
+ "vt_Copy_2vuy_x4as"
+ "vt_Copy_2vuy_xf20"
+ "vt_Copy_2vuy_xf22"
+ "vt_Copy_2vuy_xf44"
+ "vt_Copy_2vuy_y420"
+ "vt_Copy_2vuy_yuvs"
+ "vt_Copy_2vuy_yuvs_vec"
+ "vt_Copy_32ARGB_2vuyITU2020"
+ "vt_Copy_32ARGB_2vuyITU601"
+ "vt_Copy_32ARGB_2vuyITU709"
+ "vt_Copy_32ARGB_32BGRA"
+ "vt_Copy_32ARGB_420fITU2020"
+ "vt_Copy_32ARGB_420fITU601"
+ "vt_Copy_32ARGB_420fITU709"
+ "vt_Copy_32ARGB_420vITU2020"
+ "vt_Copy_32ARGB_420vITU601"
+ "vt_Copy_32ARGB_420vITU709"
+ "vt_Copy_32ARGB_a2vyITU2020"
+ "vt_Copy_32ARGB_a2vyITU601"
+ "vt_Copy_32ARGB_a2vyITU709"
+ "vt_Copy_32ARGB_p420ITU2020"
+ "vt_Copy_32ARGB_p420ITU601"
+ "vt_Copy_32ARGB_p420ITU709"
+ "vt_Copy_32ARGB_pf20ITU2020"
+ "vt_Copy_32ARGB_pf20ITU601"
+ "vt_Copy_32ARGB_pf20ITU709"
+ "vt_Copy_32ARGB_y420ITU2020"
+ "vt_Copy_32ARGB_y420ITU601"
+ "vt_Copy_32ARGB_y420ITU709"
+ "vt_Copy_32ARGB_yuvsITU2020"
+ "vt_Copy_32ARGB_yuvsITU601"
+ "vt_Copy_32ARGB_yuvsITU709"
+ "vt_Copy_32BGRA_2vuyITU2020"
+ "vt_Copy_32BGRA_2vuyITU601"
+ "vt_Copy_32BGRA_2vuyITU709"
+ "vt_Copy_32BGRA_32ARGB"
+ "vt_Copy_32BGRA_420fITU2020"
+ "vt_Copy_32BGRA_420fITU601"
+ "vt_Copy_32BGRA_420fITU709"
+ "vt_Copy_32BGRA_420vITU2020"
+ "vt_Copy_32BGRA_420vITU601"
+ "vt_Copy_32BGRA_420vITU709"
+ "vt_Copy_32BGRA_444fITU2020"
+ "vt_Copy_32BGRA_444fITU601"
+ "vt_Copy_32BGRA_444fITU709"
+ "vt_Copy_32BGRA_444vITU2020"
+ "vt_Copy_32BGRA_444vITU601"
+ "vt_Copy_32BGRA_444vITU709"
+ "vt_Copy_32BGRA_OneComponentITU2020"
+ "vt_Copy_32BGRA_OneComponentITU601"
+ "vt_Copy_32BGRA_OneComponentITU709"
+ "vt_Copy_32BGRA_a2vyITU2020"
+ "vt_Copy_32BGRA_a2vyITU601"
+ "vt_Copy_32BGRA_a2vyITU709"
+ "vt_Copy_32BGRA_p420ITU2020"
+ "vt_Copy_32BGRA_p420ITU601"
+ "vt_Copy_32BGRA_p420ITU709"
+ "vt_Copy_32BGRA_pf20ITU2020"
+ "vt_Copy_32BGRA_pf20ITU601"
+ "vt_Copy_32BGRA_pf20ITU709"
+ "vt_Copy_32BGRA_y420ITU2020"
+ "vt_Copy_32BGRA_y420ITU601"
+ "vt_Copy_32BGRA_y420ITU709"
+ "vt_Copy_32BGRA_yuvfITU2020"
+ "vt_Copy_32BGRA_yuvfITU2020_vec"
+ "vt_Copy_32BGRA_yuvfITU601"
+ "vt_Copy_32BGRA_yuvfITU601_vec"
+ "vt_Copy_32BGRA_yuvfITU709"
+ "vt_Copy_32BGRA_yuvfITU709_vec"
+ "vt_Copy_32BGRA_yuvsITU2020"
+ "vt_Copy_32BGRA_yuvsITU2020_vec"
+ "vt_Copy_32BGRA_yuvsITU601"
+ "vt_Copy_32BGRA_yuvsITU601_vec"
+ "vt_Copy_32BGRA_yuvsITU709"
+ "vt_Copy_32BGRA_yuvsITU709_vec"
+ "vt_Copy_420fITU2020F_24RGB_vec"
+ "vt_Copy_420fITU2020F_32ARGB_vec"
+ "vt_Copy_420fITU2020F_32BGRA_vec"
+ "vt_Copy_420fITU601F_24RGB_vec"
+ "vt_Copy_420fITU601F_32ARGB_vec"
+ "vt_Copy_420fITU601F_32BGRA_vec"
+ "vt_Copy_420fITU709F_24RGB_vec"
+ "vt_Copy_420fITU709F_32ARGB_vec"
+ "vt_Copy_420fITU709F_32BGRA_vec"
+ "vt_Copy_420f_2vuy"
+ "vt_Copy_420f_420v"
+ "vt_Copy_420f_420v_vec"
+ "vt_Copy_420f_422v"
+ "vt_Copy_420f_444f"
+ "vt_Copy_420f_444v"
+ "vt_Copy_420f_8GRAYSCALE"
+ "vt_Copy_420f_s2as"
+ "vt_Copy_420f_s4as"
+ "vt_Copy_420f_sf20"
+ "vt_Copy_420f_sf22"
+ "vt_Copy_420f_sf44"
+ "vt_Copy_420f_sv20"
+ "vt_Copy_420f_sv22"
+ "vt_Copy_420f_sv44"
+ "vt_Copy_420f_t2as"
+ "vt_Copy_420f_t4as"
+ "vt_Copy_420f_tf20"
+ "vt_Copy_420f_tf22"
+ "vt_Copy_420f_tf44"
+ "vt_Copy_420f_tv20"
+ "vt_Copy_420f_tv22"
+ "vt_Copy_420f_tv44"
+ "vt_Copy_420f_v0a8"
+ "vt_Copy_420f_v216"
+ "vt_Copy_420f_v2a8"
+ "vt_Copy_420f_v4a8"
+ "vt_Copy_420f_x2as"
+ "vt_Copy_420f_x420"
+ "vt_Copy_420f_x422"
+ "vt_Copy_420f_x444"
+ "vt_Copy_420f_x4as"
+ "vt_Copy_420f_xf20"
+ "vt_Copy_420f_xf22"
+ "vt_Copy_420f_xf44"
+ "vt_Copy_420f_y408"
+ "vt_Copy_420f_y416"
+ "vt_Copy_420f_y420"
+ "vt_Copy_420f_yuvs"
+ "vt_Copy_420v"
+ "vt_Copy_420vITU2020_24RGB_vec"
+ "vt_Copy_420vITU2020_32ARGB_vec"
+ "vt_Copy_420vITU2020_32BGRA_vec"
+ "vt_Copy_420vITU601_24RGB_vec"
+ "vt_Copy_420vITU601_32ARGB_vec"
+ "vt_Copy_420vITU601_32BGRA_vec"
+ "vt_Copy_420vITU709_24RGB_vec"
+ "vt_Copy_420vITU709_32ARGB_vec"
+ "vt_Copy_420vITU709_32BGRA_vec"
+ "vt_Copy_420v_2vuy"
+ "vt_Copy_420v_420f"
+ "vt_Copy_420v_422f"
+ "vt_Copy_420v_422v"
+ "vt_Copy_420v_444f"
+ "vt_Copy_420v_444v"
+ "vt_Copy_420v_8GRAYSCALE"
+ "vt_Copy_420v_Crop"
+ "vt_Copy_420v_OneComponent"
+ "vt_Copy_420v_f420"
+ "vt_Copy_420v_s2as"
+ "vt_Copy_420v_s4as"
+ "vt_Copy_420v_sf20"
+ "vt_Copy_420v_sf22"
+ "vt_Copy_420v_sf44"
+ "vt_Copy_420v_sv20"
+ "vt_Copy_420v_sv22"
+ "vt_Copy_420v_sv44"
+ "vt_Copy_420v_t2as"
+ "vt_Copy_420v_t4as"
+ "vt_Copy_420v_tf20"
+ "vt_Copy_420v_tf22"
+ "vt_Copy_420v_tf44"
+ "vt_Copy_420v_tv20"
+ "vt_Copy_420v_tv22"
+ "vt_Copy_420v_tv44"
+ "vt_Copy_420v_v0a8"
+ "vt_Copy_420v_v216"
+ "vt_Copy_420v_v2a8"
+ "vt_Copy_420v_v4a8"
+ "vt_Copy_420v_x2as"
+ "vt_Copy_420v_x420"
+ "vt_Copy_420v_x422"
+ "vt_Copy_420v_x444"
+ "vt_Copy_420v_x4as"
+ "vt_Copy_420v_xf20"
+ "vt_Copy_420v_xf22"
+ "vt_Copy_420v_xf44"
+ "vt_Copy_420v_y408"
+ "vt_Copy_420v_y416"
+ "vt_Copy_420v_y420"
+ "vt_Copy_420v_y420_vec"
+ "vt_Copy_420v_yuvf"
+ "vt_Copy_420v_yuvf_vec"
+ "vt_Copy_420v_yuvs"
+ "vt_Copy_420v_yuvs_vec"
+ "vt_Copy_420vf_TRC_Mat_TRC_2vuyf"
+ "vt_Copy_420vf_TRC_Mat_TRC_420vf"
+ "vt_Copy_420vf_TRC_Mat_TRC_420vf_neon_fp16"
+ "vt_Copy_420vf_TRC_Mat_TRC_422vf"
+ "vt_Copy_420vf_TRC_Mat_TRC_422vf_neon_fp16"
+ "vt_Copy_420vf_TRC_Mat_TRC_444vf"
+ "vt_Copy_420vf_TRC_Mat_TRC_444vf_neon_fp16"
+ "vt_Copy_420vf_TRC_Mat_TRC_BGRA"
+ "vt_Copy_420vf_TRC_Mat_TRC_BGRA_neon_fp16"
+ "vt_Copy_420vf_TRC_Mat_TRC_RGfA"
+ "vt_Copy_420vf_TRC_Mat_TRC_RGfA_neon_fp16"
+ "vt_Copy_420vf_TRC_Mat_TRC_RGhA"
+ "vt_Copy_420vf_TRC_Mat_TRC_RGhA_neon_fp16"
+ "vt_Copy_420vf_TRC_Mat_TRC_b64a"
+ "vt_Copy_420vf_TRC_Mat_TRC_l10r"
+ "vt_Copy_420vf_TRC_Mat_TRC_l64r"
+ "vt_Copy_420vf_TRC_Mat_TRC_v216"
+ "vt_Copy_420vf_TRC_Mat_TRC_xf420"
+ "vt_Copy_420vf_TRC_Mat_TRC_xf420_neon_fp16"
+ "vt_Copy_420vf_TRC_Mat_TRC_xf422"
+ "vt_Copy_420vf_TRC_Mat_TRC_xf422_neon_fp16"
+ "vt_Copy_420vf_TRC_Mat_TRC_xf444"
+ "vt_Copy_420vf_TRC_Mat_TRC_xf444_neon_fp16"
+ "vt_Copy_420vf_TRC_Mat_TRC_yuvsf"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_2vuyf"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_420vf"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_420vf_neon_fp16"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_422vf"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_422vf_neon_fp16"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_444vf"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_444vf_neon_fp16"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_BGRA"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_BGRA_neon_fp16"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_RGfA"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_RGfA_neon_fp16"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_RGhA"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_RGhA_neon_fp16"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_b64a"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_l10r"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_l64r"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_v216"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_xf420"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_xf420_neon_fp16"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_xf422"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_xf422_neon_fp16"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_xf444"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_xf444_neon_fp16"
+ "vt_Copy_420vf_TRC_Tone_Mat_TRC_yuvsf"
+ "vt_Copy_420vf_rgb_2vuyf"
+ "vt_Copy_420vf_rgb_420vf"
+ "vt_Copy_420vf_rgb_420vf_neon_fp16"
+ "vt_Copy_420vf_rgb_422vf"
+ "vt_Copy_420vf_rgb_422vf_neon_fp16"
+ "vt_Copy_420vf_rgb_444vf"
+ "vt_Copy_420vf_rgb_444vf_neon_fp16"
+ "vt_Copy_420vf_rgb_BGRA"
+ "vt_Copy_420vf_rgb_BGRA_neon_fp16"
+ "vt_Copy_420vf_rgb_RGfA"
+ "vt_Copy_420vf_rgb_RGfA_neon_fp16"
+ "vt_Copy_420vf_rgb_RGhA"
+ "vt_Copy_420vf_rgb_RGhA_neon_fp16"
+ "vt_Copy_420vf_rgb_b64a"
+ "vt_Copy_420vf_rgb_l10r"
+ "vt_Copy_420vf_rgb_l64r"
+ "vt_Copy_420vf_rgb_v216"
+ "vt_Copy_420vf_rgb_xf420"
+ "vt_Copy_420vf_rgb_xf420_neon_fp16"
+ "vt_Copy_420vf_rgb_xf422"
+ "vt_Copy_420vf_rgb_xf422_neon_fp16"
+ "vt_Copy_420vf_rgb_xf444"
+ "vt_Copy_420vf_rgb_xf444_neon_fp16"
+ "vt_Copy_420vf_rgb_yuvsf"
+ "vt_Copy_422f_2vuy"
+ "vt_Copy_422f_420f"
+ "vt_Copy_422f_420v"
+ "vt_Copy_422f_422v"
+ "vt_Copy_422f_444f"
+ "vt_Copy_422f_444v"
+ "vt_Copy_422f_f420"
+ "vt_Copy_422f_s2as"
+ "vt_Copy_422f_s4as"
+ "vt_Copy_422f_sf20"
+ "vt_Copy_422f_sf22"
+ "vt_Copy_422f_sf44"
+ "vt_Copy_422f_sv20"
+ "vt_Copy_422f_sv22"
+ "vt_Copy_422f_sv44"
+ "vt_Copy_422f_t2as"
+ "vt_Copy_422f_t4as"
+ "vt_Copy_422f_tf20"
+ "vt_Copy_422f_tf22"
+ "vt_Copy_422f_tf44"
+ "vt_Copy_422f_tv20"
+ "vt_Copy_422f_tv22"
+ "vt_Copy_422f_tv44"
+ "vt_Copy_422f_v0a8"
+ "vt_Copy_422f_v216"
+ "vt_Copy_422f_v2a8"
+ "vt_Copy_422f_v4a8"
+ "vt_Copy_422f_x2as"
+ "vt_Copy_422f_x420"
+ "vt_Copy_422f_x422"
+ "vt_Copy_422f_x444"
+ "vt_Copy_422f_x4as"
+ "vt_Copy_422f_xf20"
+ "vt_Copy_422f_xf22"
+ "vt_Copy_422f_xf44"
+ "vt_Copy_422f_y408"
+ "vt_Copy_422f_y416"
+ "vt_Copy_422f_y420"
+ "vt_Copy_422v"
+ "vt_Copy_422v_2vuy"
+ "vt_Copy_422v_420f"
+ "vt_Copy_422v_420v"
+ "vt_Copy_422v_422f"
+ "vt_Copy_422v_444f"
+ "vt_Copy_422v_444v"
+ "vt_Copy_422v_Crop"
+ "vt_Copy_422v_f420"
+ "vt_Copy_422v_s2as"
+ "vt_Copy_422v_s4as"
+ "vt_Copy_422v_sf20"
+ "vt_Copy_422v_sf22"
+ "vt_Copy_422v_sf44"
+ "vt_Copy_422v_sv20"
+ "vt_Copy_422v_sv22"
+ "vt_Copy_422v_sv44"
+ "vt_Copy_422v_t2as"
+ "vt_Copy_422v_t4as"
+ "vt_Copy_422v_tf20"
+ "vt_Copy_422v_tf22"
+ "vt_Copy_422v_tf44"
+ "vt_Copy_422v_tv20"
+ "vt_Copy_422v_tv22"
+ "vt_Copy_422v_tv44"
+ "vt_Copy_422v_v0a8"
+ "vt_Copy_422v_v216"
+ "vt_Copy_422v_v2a8"
+ "vt_Copy_422v_v4a8"
+ "vt_Copy_422v_x2as"
+ "vt_Copy_422v_x420"
+ "vt_Copy_422v_x422"
+ "vt_Copy_422v_x444"
+ "vt_Copy_422v_x4as"
+ "vt_Copy_422v_xf20"
+ "vt_Copy_422v_xf22"
+ "vt_Copy_422v_xf44"
+ "vt_Copy_422v_y408"
+ "vt_Copy_422v_y416"
+ "vt_Copy_422v_y420"
+ "vt_Copy_422vf_TRC_Mat_TRC_2vuyf"
+ "vt_Copy_422vf_TRC_Mat_TRC_420vf"
+ "vt_Copy_422vf_TRC_Mat_TRC_420vf_neon_fp16"
+ "vt_Copy_422vf_TRC_Mat_TRC_422vf"
+ "vt_Copy_422vf_TRC_Mat_TRC_422vf_neon_fp16"
+ "vt_Copy_422vf_TRC_Mat_TRC_444vf"
+ "vt_Copy_422vf_TRC_Mat_TRC_444vf_neon_fp16"
+ "vt_Copy_422vf_TRC_Mat_TRC_BGRA"
+ "vt_Copy_422vf_TRC_Mat_TRC_BGRA_neon_fp16"
+ "vt_Copy_422vf_TRC_Mat_TRC_RGfA"
+ "vt_Copy_422vf_TRC_Mat_TRC_RGfA_neon_fp16"
+ "vt_Copy_422vf_TRC_Mat_TRC_RGhA"
+ "vt_Copy_422vf_TRC_Mat_TRC_RGhA_neon_fp16"
+ "vt_Copy_422vf_TRC_Mat_TRC_b64a"
+ "vt_Copy_422vf_TRC_Mat_TRC_l10r"
+ "vt_Copy_422vf_TRC_Mat_TRC_l64r"
+ "vt_Copy_422vf_TRC_Mat_TRC_v216"
+ "vt_Copy_422vf_TRC_Mat_TRC_xf420"
+ "vt_Copy_422vf_TRC_Mat_TRC_xf420_neon_fp16"
+ "vt_Copy_422vf_TRC_Mat_TRC_xf422"
+ "vt_Copy_422vf_TRC_Mat_TRC_xf422_neon_fp16"
+ "vt_Copy_422vf_TRC_Mat_TRC_xf444"
+ "vt_Copy_422vf_TRC_Mat_TRC_xf444_neon_fp16"
+ "vt_Copy_422vf_TRC_Mat_TRC_yuvsf"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_2vuyf"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_420vf"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_420vf_neon_fp16"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_422vf"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_422vf_neon_fp16"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_444vf"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_444vf_neon_fp16"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_BGRA"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_BGRA_neon_fp16"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_RGfA"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_RGfA_neon_fp16"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_RGhA"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_RGhA_neon_fp16"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_b64a"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_l10r"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_l64r"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_v216"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_xf420"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_xf420_neon_fp16"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_xf422"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_xf422_neon_fp16"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_xf444"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_xf444_neon_fp16"
+ "vt_Copy_422vf_TRC_Tone_Mat_TRC_yuvsf"
+ "vt_Copy_422vf_rgb_2vuyf"
+ "vt_Copy_422vf_rgb_420vf"
+ "vt_Copy_422vf_rgb_420vf_neon_fp16"
+ "vt_Copy_422vf_rgb_422vf"
+ "vt_Copy_422vf_rgb_422vf_neon_fp16"
+ "vt_Copy_422vf_rgb_444vf"
+ "vt_Copy_422vf_rgb_444vf_neon_fp16"
+ "vt_Copy_422vf_rgb_BGRA"
+ "vt_Copy_422vf_rgb_BGRA_neon_fp16"
+ "vt_Copy_422vf_rgb_RGfA"
+ "vt_Copy_422vf_rgb_RGfA_neon_fp16"
+ "vt_Copy_422vf_rgb_RGhA"
+ "vt_Copy_422vf_rgb_RGhA_neon_fp16"
+ "vt_Copy_422vf_rgb_b64a"
+ "vt_Copy_422vf_rgb_l10r"
+ "vt_Copy_422vf_rgb_l64r"
+ "vt_Copy_422vf_rgb_v216"
+ "vt_Copy_422vf_rgb_xf420"
+ "vt_Copy_422vf_rgb_xf420_neon_fp16"
+ "vt_Copy_422vf_rgb_xf422"
+ "vt_Copy_422vf_rgb_xf422_neon_fp16"
+ "vt_Copy_422vf_rgb_xf444"
+ "vt_Copy_422vf_rgb_xf444_neon_fp16"
+ "vt_Copy_422vf_rgb_yuvsf"
+ "vt_Copy_444f_2vuy"
+ "vt_Copy_444f_420f"
+ "vt_Copy_444f_420v"
+ "vt_Copy_444f_422f"
+ "vt_Copy_444f_422v"
+ "vt_Copy_444f_444v"
+ "vt_Copy_444f_f420"
+ "vt_Copy_444f_s2as"
+ "vt_Copy_444f_s4as"
+ "vt_Copy_444f_sf20"
+ "vt_Copy_444f_sf22"
+ "vt_Copy_444f_sf44"
+ "vt_Copy_444f_sv20"
+ "vt_Copy_444f_sv22"
+ "vt_Copy_444f_sv44"
+ "vt_Copy_444f_t2as"
+ "vt_Copy_444f_t4as"
+ "vt_Copy_444f_tf20"
+ "vt_Copy_444f_tf22"
+ "vt_Copy_444f_tf44"
+ "vt_Copy_444f_tv20"
+ "vt_Copy_444f_tv22"
+ "vt_Copy_444f_tv44"
+ "vt_Copy_444f_v0a8"
+ "vt_Copy_444f_v216"
+ "vt_Copy_444f_v2a8"
+ "vt_Copy_444f_v4a8"
+ "vt_Copy_444f_x2as"
+ "vt_Copy_444f_x420"
+ "vt_Copy_444f_x422"
+ "vt_Copy_444f_x444"
+ "vt_Copy_444f_x4as"
+ "vt_Copy_444f_xf20"
+ "vt_Copy_444f_xf22"
+ "vt_Copy_444f_xf44"
+ "vt_Copy_444f_y408"
+ "vt_Copy_444f_y416"
+ "vt_Copy_444f_y420"
+ "vt_Copy_444v"
+ "vt_Copy_444v_2vuy"
+ "vt_Copy_444v_420f"
+ "vt_Copy_444v_420v"
+ "vt_Copy_444v_422f"
+ "vt_Copy_444v_422v"
+ "vt_Copy_444v_444f"
+ "vt_Copy_444v_Crop"
+ "vt_Copy_444v_f420"
+ "vt_Copy_444v_s2as"
+ "vt_Copy_444v_s4as"
+ "vt_Copy_444v_sf20"
+ "vt_Copy_444v_sf22"
+ "vt_Copy_444v_sf44"
+ "vt_Copy_444v_sv20"
+ "vt_Copy_444v_sv22"
+ "vt_Copy_444v_sv44"
+ "vt_Copy_444v_t2as"
+ "vt_Copy_444v_t4as"
+ "vt_Copy_444v_tf20"
+ "vt_Copy_444v_tf22"
+ "vt_Copy_444v_tf44"
+ "vt_Copy_444v_tv20"
+ "vt_Copy_444v_tv22"
+ "vt_Copy_444v_tv44"
+ "vt_Copy_444v_v0a8"
+ "vt_Copy_444v_v216"
+ "vt_Copy_444v_v2a8"
+ "vt_Copy_444v_v4a8"
+ "vt_Copy_444v_x2as"
+ "vt_Copy_444v_x420"
+ "vt_Copy_444v_x422"
+ "vt_Copy_444v_x444"
+ "vt_Copy_444v_x4as"
+ "vt_Copy_444v_xf20"
+ "vt_Copy_444v_xf22"
+ "vt_Copy_444v_xf44"
+ "vt_Copy_444v_y408"
+ "vt_Copy_444v_y416"
+ "vt_Copy_444v_y420"
+ "vt_Copy_444vf_TRC_Mat_TRC_2vuyf"
+ "vt_Copy_444vf_TRC_Mat_TRC_420vf"
+ "vt_Copy_444vf_TRC_Mat_TRC_420vf_neon_fp16"
+ "vt_Copy_444vf_TRC_Mat_TRC_422vf"
+ "vt_Copy_444vf_TRC_Mat_TRC_422vf_neon_fp16"
+ "vt_Copy_444vf_TRC_Mat_TRC_444vf"
+ "vt_Copy_444vf_TRC_Mat_TRC_444vf_neon_fp16"
+ "vt_Copy_444vf_TRC_Mat_TRC_BGRA"
+ "vt_Copy_444vf_TRC_Mat_TRC_BGRA_neon_fp16"
+ "vt_Copy_444vf_TRC_Mat_TRC_RGfA"
+ "vt_Copy_444vf_TRC_Mat_TRC_RGfA_neon_fp16"
+ "vt_Copy_444vf_TRC_Mat_TRC_RGhA"
+ "vt_Copy_444vf_TRC_Mat_TRC_RGhA_neon_fp16"
+ "vt_Copy_444vf_TRC_Mat_TRC_b64a"
+ "vt_Copy_444vf_TRC_Mat_TRC_l10r"
+ "vt_Copy_444vf_TRC_Mat_TRC_l64r"
+ "vt_Copy_444vf_TRC_Mat_TRC_v216"
+ "vt_Copy_444vf_TRC_Mat_TRC_xf420"
+ "vt_Copy_444vf_TRC_Mat_TRC_xf420_neon_fp16"
+ "vt_Copy_444vf_TRC_Mat_TRC_xf422"
+ "vt_Copy_444vf_TRC_Mat_TRC_xf422_neon_fp16"
+ "vt_Copy_444vf_TRC_Mat_TRC_xf444"
+ "vt_Copy_444vf_TRC_Mat_TRC_xf444_neon_fp16"
+ "vt_Copy_444vf_TRC_Mat_TRC_yuvsf"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_2vuyf"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_420vf"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_420vf_neon_fp16"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_422vf"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_422vf_neon_fp16"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_444vf"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_444vf_neon_fp16"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_BGRA"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_BGRA_neon_fp16"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_RGfA"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_RGfA_neon_fp16"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_RGhA"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_RGhA_neon_fp16"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_b64a"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_l10r"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_l64r"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_v216"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_xf420"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_xf420_neon_fp16"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_xf422"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_xf422_neon_fp16"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_xf444"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_xf444_neon_fp16"
+ "vt_Copy_444vf_TRC_Tone_Mat_TRC_yuvsf"
+ "vt_Copy_444vf_rgb_2vuyf"
+ "vt_Copy_444vf_rgb_420vf"
+ "vt_Copy_444vf_rgb_420vf_neon_fp16"
+ "vt_Copy_444vf_rgb_422vf"
+ "vt_Copy_444vf_rgb_422vf_neon_fp16"
+ "vt_Copy_444vf_rgb_444vf"
+ "vt_Copy_444vf_rgb_444vf_neon_fp16"
+ "vt_Copy_444vf_rgb_BGRA"
+ "vt_Copy_444vf_rgb_BGRA_neon_fp16"
+ "vt_Copy_444vf_rgb_RGfA"
+ "vt_Copy_444vf_rgb_RGfA_neon_fp16"
+ "vt_Copy_444vf_rgb_RGhA"
+ "vt_Copy_444vf_rgb_RGhA_neon_fp16"
+ "vt_Copy_444vf_rgb_b64a"
+ "vt_Copy_444vf_rgb_l10r"
+ "vt_Copy_444vf_rgb_l64r"
+ "vt_Copy_444vf_rgb_v216"
+ "vt_Copy_444vf_rgb_xf420"
+ "vt_Copy_444vf_rgb_xf420_neon_fp16"
+ "vt_Copy_444vf_rgb_xf422"
+ "vt_Copy_444vf_rgb_xf422_neon_fp16"
+ "vt_Copy_444vf_rgb_xf444"
+ "vt_Copy_444vf_rgb_xf444_neon_fp16"
+ "vt_Copy_444vf_rgb_yuvsf"
+ "vt_Copy_64RGBA_f420ITU2020"
+ "vt_Copy_64RGBA_f420ITU601"
+ "vt_Copy_64RGBA_f420ITU709"
+ "vt_Copy_64RGBA_p420ITU2020"
+ "vt_Copy_64RGBA_p420ITU601"
+ "vt_Copy_64RGBA_p420ITU709"
+ "vt_Copy_64RGBA_pf20ITU2020"
+ "vt_Copy_64RGBA_pf20ITU601"
+ "vt_Copy_64RGBA_pf20ITU709"
+ "vt_Copy_64RGBA_y420ITU2020"
+ "vt_Copy_64RGBA_y420ITU601"
+ "vt_Copy_64RGBA_y420ITU709"
+ "vt_Copy_8GRAYSCALE_2vuyITU2020"
+ "vt_Copy_8GRAYSCALE_2vuyITU601"
+ "vt_Copy_8GRAYSCALE_2vuyITU709"
+ "vt_Copy_8GRAYSCALE_420f"
+ "vt_Copy_8GRAYSCALE_420v"
+ "vt_Copy_8GRAYSCALE_a2vyITU2020"
+ "vt_Copy_8GRAYSCALE_a2vyITU601"
+ "vt_Copy_8GRAYSCALE_a2vyITU709"
+ "vt_Copy_8GRAYSCALE_yuvsITU2020"
+ "vt_Copy_8GRAYSCALE_yuvsITU601"
+ "vt_Copy_8GRAYSCALE_yuvsITU709"
+ "vt_Copy_BGRA_TRC_Mat_TRC_2vuyf"
+ "vt_Copy_BGRA_TRC_Mat_TRC_420vf"
+ "vt_Copy_BGRA_TRC_Mat_TRC_420vf_neon_fp16"
+ "vt_Copy_BGRA_TRC_Mat_TRC_422vf"
+ "vt_Copy_BGRA_TRC_Mat_TRC_422vf_neon_fp16"
+ "vt_Copy_BGRA_TRC_Mat_TRC_444vf"
+ "vt_Copy_BGRA_TRC_Mat_TRC_444vf_neon_fp16"
+ "vt_Copy_BGRA_TRC_Mat_TRC_BGRA"
+ "vt_Copy_BGRA_TRC_Mat_TRC_BGRA_neon_fp16"
+ "vt_Copy_BGRA_TRC_Mat_TRC_RGfA"
+ "vt_Copy_BGRA_TRC_Mat_TRC_RGfA_neon_fp16"
+ "vt_Copy_BGRA_TRC_Mat_TRC_RGhA"
+ "vt_Copy_BGRA_TRC_Mat_TRC_RGhA_neon_fp16"
+ "vt_Copy_BGRA_TRC_Mat_TRC_b64a"
+ "vt_Copy_BGRA_TRC_Mat_TRC_l10r"
+ "vt_Copy_BGRA_TRC_Mat_TRC_l64r"
+ "vt_Copy_BGRA_TRC_Mat_TRC_v216"
+ "vt_Copy_BGRA_TRC_Mat_TRC_xf420"
+ "vt_Copy_BGRA_TRC_Mat_TRC_xf420_neon_fp16"
+ "vt_Copy_BGRA_TRC_Mat_TRC_xf422"
+ "vt_Copy_BGRA_TRC_Mat_TRC_xf422_neon_fp16"
+ "vt_Copy_BGRA_TRC_Mat_TRC_xf444"
+ "vt_Copy_BGRA_TRC_Mat_TRC_xf444_neon_fp16"
+ "vt_Copy_BGRA_TRC_Mat_TRC_yuvsf"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_2vuyf"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_420vf"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_420vf_neon_fp16"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_422vf"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_422vf_neon_fp16"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_444vf"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_444vf_neon_fp16"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_BGRA"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_BGRA_neon_fp16"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_RGfA"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_RGfA_neon_fp16"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_RGhA"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_RGhA_neon_fp16"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_b64a"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_l10r"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_l64r"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_v216"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_xf420"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_xf420_neon_fp16"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_xf422"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_xf422_neon_fp16"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_xf444"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_xf444_neon_fp16"
+ "vt_Copy_BGRA_TRC_Tone_Mat_TRC_yuvsf"
+ "vt_Copy_BGRA_rgb_2vuyf"
+ "vt_Copy_BGRA_rgb_420vf"
+ "vt_Copy_BGRA_rgb_420vf_neon_fp16"
+ "vt_Copy_BGRA_rgb_422vf"
+ "vt_Copy_BGRA_rgb_422vf_neon_fp16"
+ "vt_Copy_BGRA_rgb_444vf"
+ "vt_Copy_BGRA_rgb_444vf_neon_fp16"
+ "vt_Copy_BGRA_rgb_BGRA"
+ "vt_Copy_BGRA_rgb_BGRA_neon_fp16"
+ "vt_Copy_BGRA_rgb_RGfA"
+ "vt_Copy_BGRA_rgb_RGfA_neon_fp16"
+ "vt_Copy_BGRA_rgb_RGhA"
+ "vt_Copy_BGRA_rgb_RGhA_neon_fp16"
+ "vt_Copy_BGRA_rgb_b64a"
+ "vt_Copy_BGRA_rgb_l10r"
+ "vt_Copy_BGRA_rgb_l64r"
+ "vt_Copy_BGRA_rgb_v216"
+ "vt_Copy_BGRA_rgb_xf420"
+ "vt_Copy_BGRA_rgb_xf420_neon_fp16"
+ "vt_Copy_BGRA_rgb_xf422"
+ "vt_Copy_BGRA_rgb_xf422_neon_fp16"
+ "vt_Copy_BGRA_rgb_xf444"
+ "vt_Copy_BGRA_rgb_xf444_neon_fp16"
+ "vt_Copy_BGRA_rgb_yuvsf"
+ "vt_Copy_Float_Half"
+ "vt_Copy_Half_Float"
+ "vt_Copy_L010_L008"
+ "vt_Copy_L010_L016"
+ "vt_Copy_L565_32BGRA"
+ "vt_Copy_L565_5551"
+ "vt_Copy_NonPlanar128"
+ "vt_Copy_NonPlanar128_Crop"
+ "vt_Copy_NonPlanar16"
+ "vt_Copy_NonPlanar16_Crop"
+ "vt_Copy_NonPlanar32"
+ "vt_Copy_NonPlanar32_Crop"
+ "vt_Copy_NonPlanar64"
+ "vt_Copy_NonPlanar64_Crop"
+ "vt_Copy_NonPlanar8"
+ "vt_Copy_NonPlanar8_Crop"
+ "vt_Copy_OneComponent_420f"
+ "vt_Copy_OneComponent_420v"
+ "vt_Copy_PlanarYUV422_2vuy"
+ "vt_Copy_PlanarYUV422_v216"
+ "vt_Copy_PlanarYUV422_yuvs"
+ "vt_Copy_R10k_32ARGB"
+ "vt_Copy_R10k_32BGRA"
+ "vt_Copy_RGfA_TRC_Mat_TRC_2vuyf"
+ "vt_Copy_RGfA_TRC_Mat_TRC_420vf"
+ "vt_Copy_RGfA_TRC_Mat_TRC_420vf_neon_fp16"
+ "vt_Copy_RGfA_TRC_Mat_TRC_422vf"
+ "vt_Copy_RGfA_TRC_Mat_TRC_422vf_neon_fp16"
+ "vt_Copy_RGfA_TRC_Mat_TRC_444vf"
+ "vt_Copy_RGfA_TRC_Mat_TRC_444vf_neon_fp16"
+ "vt_Copy_RGfA_TRC_Mat_TRC_BGRA"
+ "vt_Copy_RGfA_TRC_Mat_TRC_BGRA_neon_fp16"
+ "vt_Copy_RGfA_TRC_Mat_TRC_RGfA"
+ "vt_Copy_RGfA_TRC_Mat_TRC_RGfA_neon_fp16"
+ "vt_Copy_RGfA_TRC_Mat_TRC_RGhA"
+ "vt_Copy_RGfA_TRC_Mat_TRC_RGhA_neon_fp16"
+ "vt_Copy_RGfA_TRC_Mat_TRC_b64a"
+ "vt_Copy_RGfA_TRC_Mat_TRC_l10r"
+ "vt_Copy_RGfA_TRC_Mat_TRC_l64r"
+ "vt_Copy_RGfA_TRC_Mat_TRC_v216"
+ "vt_Copy_RGfA_TRC_Mat_TRC_xf420"
+ "vt_Copy_RGfA_TRC_Mat_TRC_xf420_neon_fp16"
+ "vt_Copy_RGfA_TRC_Mat_TRC_xf422"
+ "vt_Copy_RGfA_TRC_Mat_TRC_xf422_neon_fp16"
+ "vt_Copy_RGfA_TRC_Mat_TRC_xf444"
+ "vt_Copy_RGfA_TRC_Mat_TRC_xf444_neon_fp16"
+ "vt_Copy_RGfA_TRC_Mat_TRC_yuvsf"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_2vuyf"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_420vf"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_420vf_neon_fp16"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_422vf"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_422vf_neon_fp16"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_444vf"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_444vf_neon_fp16"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_BGRA"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_BGRA_neon_fp16"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_RGfA"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_RGfA_neon_fp16"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_RGhA"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_RGhA_neon_fp16"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_b64a"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_l10r"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_l64r"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_v216"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_xf420"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_xf420_neon_fp16"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_xf422"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_xf422_neon_fp16"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_xf444"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_xf444_neon_fp16"
+ "vt_Copy_RGfA_TRC_Tone_Mat_TRC_yuvsf"
+ "vt_Copy_RGfA_p420ITU2020"
+ "vt_Copy_RGfA_p420ITU601"
+ "vt_Copy_RGfA_p420ITU709"
+ "vt_Copy_RGfA_pf20ITU2020"
+ "vt_Copy_RGfA_pf20ITU601"
+ "vt_Copy_RGfA_pf20ITU709"
+ "vt_Copy_RGfA_rgb_2vuyf"
+ "vt_Copy_RGfA_rgb_420vf"
+ "vt_Copy_RGfA_rgb_420vf_neon_fp16"
+ "vt_Copy_RGfA_rgb_422vf"
+ "vt_Copy_RGfA_rgb_422vf_neon_fp16"
+ "vt_Copy_RGfA_rgb_444vf"
+ "vt_Copy_RGfA_rgb_444vf_neon_fp16"
+ "vt_Copy_RGfA_rgb_BGRA"
+ "vt_Copy_RGfA_rgb_BGRA_neon_fp16"
+ "vt_Copy_RGfA_rgb_RGfA"
+ "vt_Copy_RGfA_rgb_RGfA_neon_fp16"
+ "vt_Copy_RGfA_rgb_RGhA"
+ "vt_Copy_RGfA_rgb_RGhA_neon_fp16"
+ "vt_Copy_RGfA_rgb_b64a"
+ "vt_Copy_RGfA_rgb_l10r"
+ "vt_Copy_RGfA_rgb_l64r"
+ "vt_Copy_RGfA_rgb_v216"
+ "vt_Copy_RGfA_rgb_xf420"
+ "vt_Copy_RGfA_rgb_xf420_neon_fp16"
+ "vt_Copy_RGfA_rgb_xf422"
+ "vt_Copy_RGfA_rgb_xf422_neon_fp16"
+ "vt_Copy_RGfA_rgb_xf444"
+ "vt_Copy_RGfA_rgb_xf444_neon_fp16"
+ "vt_Copy_RGfA_rgb_yuvsf"
+ "vt_Copy_RGhA_TRC_Mat_TRC_2vuyf"
+ "vt_Copy_RGhA_TRC_Mat_TRC_420vf"
+ "vt_Copy_RGhA_TRC_Mat_TRC_420vf_neon_fp16"
+ "vt_Copy_RGhA_TRC_Mat_TRC_422vf"
+ "vt_Copy_RGhA_TRC_Mat_TRC_422vf_neon_fp16"
+ "vt_Copy_RGhA_TRC_Mat_TRC_444vf"
+ "vt_Copy_RGhA_TRC_Mat_TRC_444vf_neon_fp16"
+ "vt_Copy_RGhA_TRC_Mat_TRC_BGRA"
+ "vt_Copy_RGhA_TRC_Mat_TRC_BGRA_neon_fp16"
+ "vt_Copy_RGhA_TRC_Mat_TRC_RGfA"
+ "vt_Copy_RGhA_TRC_Mat_TRC_RGfA_neon_fp16"
+ "vt_Copy_RGhA_TRC_Mat_TRC_RGhA"
+ "vt_Copy_RGhA_TRC_Mat_TRC_RGhA_neon_fp16"
+ "vt_Copy_RGhA_TRC_Mat_TRC_b64a"
+ "vt_Copy_RGhA_TRC_Mat_TRC_l10r"
+ "vt_Copy_RGhA_TRC_Mat_TRC_l64r"
+ "vt_Copy_RGhA_TRC_Mat_TRC_v216"
+ "vt_Copy_RGhA_TRC_Mat_TRC_xf420"
+ "vt_Copy_RGhA_TRC_Mat_TRC_xf420_neon_fp16"
+ "vt_Copy_RGhA_TRC_Mat_TRC_xf422"
+ "vt_Copy_RGhA_TRC_Mat_TRC_xf422_neon_fp16"
+ "vt_Copy_RGhA_TRC_Mat_TRC_xf444"
+ "vt_Copy_RGhA_TRC_Mat_TRC_xf444_neon_fp16"
+ "vt_Copy_RGhA_TRC_Mat_TRC_yuvsf"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_2vuyf"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_420vf"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_420vf_neon_fp16"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_422vf"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_422vf_neon_fp16"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_444vf"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_444vf_neon_fp16"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_BGRA"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_BGRA_neon_fp16"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_RGfA"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_RGfA_neon_fp16"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_RGhA"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_RGhA_neon_fp16"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_b64a"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_l10r"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_l64r"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_v216"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_xf420"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_xf420_neon_fp16"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_xf422"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_xf422_neon_fp16"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_xf444"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_xf444_neon_fp16"
+ "vt_Copy_RGhA_TRC_Tone_Mat_TRC_yuvsf"
+ "vt_Copy_RGhA_p420ITU2020"
+ "vt_Copy_RGhA_p420ITU601"
+ "vt_Copy_RGhA_p420ITU709"
+ "vt_Copy_RGhA_pf20ITU2020"
+ "vt_Copy_RGhA_pf20ITU601"
+ "vt_Copy_RGhA_pf20ITU709"
+ "vt_Copy_RGhA_rgb_2vuyf"
+ "vt_Copy_RGhA_rgb_420vf"
+ "vt_Copy_RGhA_rgb_420vf_neon_fp16"
+ "vt_Copy_RGhA_rgb_422vf"
+ "vt_Copy_RGhA_rgb_422vf_neon_fp16"
+ "vt_Copy_RGhA_rgb_444vf"
+ "vt_Copy_RGhA_rgb_444vf_neon_fp16"
+ "vt_Copy_RGhA_rgb_BGRA"
+ "vt_Copy_RGhA_rgb_BGRA_neon_fp16"
+ "vt_Copy_RGhA_rgb_RGfA"
+ "vt_Copy_RGhA_rgb_RGfA_neon_fp16"
+ "vt_Copy_RGhA_rgb_RGhA"
+ "vt_Copy_RGhA_rgb_RGhA_neon_fp16"
+ "vt_Copy_RGhA_rgb_b64a"
+ "vt_Copy_RGhA_rgb_l10r"
+ "vt_Copy_RGhA_rgb_l64r"
+ "vt_Copy_RGhA_rgb_v216"
+ "vt_Copy_RGhA_rgb_xf420"
+ "vt_Copy_RGhA_rgb_xf420_neon_fp16"
+ "vt_Copy_RGhA_rgb_xf422"
+ "vt_Copy_RGhA_rgb_xf422_neon_fp16"
+ "vt_Copy_RGhA_rgb_xf444"
+ "vt_Copy_RGhA_rgb_xf444_neon_fp16"
+ "vt_Copy_RGhA_rgb_yuvsf"
+ "vt_Copy_a2vyITU2020_24RGB"
+ "vt_Copy_a2vyITU2020_32ARGB"
+ "vt_Copy_a2vyITU2020_32BGRA"
+ "vt_Copy_a2vyITU2020_8GRAYSCALE"
+ "vt_Copy_a2vyITU601_24RGB"
+ "vt_Copy_a2vyITU601_32ARGB"
+ "vt_Copy_a2vyITU601_32BGRA"
+ "vt_Copy_a2vyITU601_8GRAYSCALE"
+ "vt_Copy_a2vyITU709_24RGB"
+ "vt_Copy_a2vyITU709_32ARGB"
+ "vt_Copy_a2vyITU709_32BGRA"
+ "vt_Copy_a2vyITU709_8GRAYSCALE"
+ "vt_Copy_a2vy_Crop"
+ "vt_Copy_b3a8_b3a8"
+ "vt_Copy_b3a8_b3a8_Crop"
+ "vt_Copy_b64a_TRC_Mat_TRC_2vuyf"
+ "vt_Copy_b64a_TRC_Mat_TRC_420vf"
+ "vt_Copy_b64a_TRC_Mat_TRC_422vf"
+ "vt_Copy_b64a_TRC_Mat_TRC_444vf"
+ "vt_Copy_b64a_TRC_Mat_TRC_BGRA"
+ "vt_Copy_b64a_TRC_Mat_TRC_RGfA"
+ "vt_Copy_b64a_TRC_Mat_TRC_RGhA"
+ "vt_Copy_b64a_TRC_Mat_TRC_b64a"
+ "vt_Copy_b64a_TRC_Mat_TRC_l10r"
+ "vt_Copy_b64a_TRC_Mat_TRC_l64r"
+ "vt_Copy_b64a_TRC_Mat_TRC_v216"
+ "vt_Copy_b64a_TRC_Mat_TRC_xf420"
+ "vt_Copy_b64a_TRC_Mat_TRC_xf422"
+ "vt_Copy_b64a_TRC_Mat_TRC_xf444"
+ "vt_Copy_b64a_TRC_Mat_TRC_yuvsf"
+ "vt_Copy_b64a_TRC_Tone_Mat_TRC_2vuyf"
+ "vt_Copy_b64a_TRC_Tone_Mat_TRC_420vf"
+ "vt_Copy_b64a_TRC_Tone_Mat_TRC_422vf"
+ "vt_Copy_b64a_TRC_Tone_Mat_TRC_444vf"
+ "vt_Copy_b64a_TRC_Tone_Mat_TRC_BGRA"
+ "vt_Copy_b64a_TRC_Tone_Mat_TRC_RGfA"
+ "vt_Copy_b64a_TRC_Tone_Mat_TRC_RGhA"
+ "vt_Copy_b64a_TRC_Tone_Mat_TRC_b64a"
+ "vt_Copy_b64a_TRC_Tone_Mat_TRC_l10r"
+ "vt_Copy_b64a_TRC_Tone_Mat_TRC_l64r"
+ "vt_Copy_b64a_TRC_Tone_Mat_TRC_v216"
+ "vt_Copy_b64a_TRC_Tone_Mat_TRC_xf420"
+ "vt_Copy_b64a_TRC_Tone_Mat_TRC_xf422"
+ "vt_Copy_b64a_TRC_Tone_Mat_TRC_xf444"
+ "vt_Copy_b64a_TRC_Tone_Mat_TRC_yuvsf"
+ "vt_Copy_b64a_rgb_2vuyf"
+ "vt_Copy_b64a_rgb_420vf"
+ "vt_Copy_b64a_rgb_422vf"
+ "vt_Copy_b64a_rgb_444vf"
+ "vt_Copy_b64a_rgb_BGRA"
+ "vt_Copy_b64a_rgb_RGfA"
+ "vt_Copy_b64a_rgb_RGhA"
+ "vt_Copy_b64a_rgb_b64a"
+ "vt_Copy_b64a_rgb_l10r"
+ "vt_Copy_b64a_rgb_l64r"
+ "vt_Copy_b64a_rgb_v216"
+ "vt_Copy_b64a_rgb_xf420"
+ "vt_Copy_b64a_rgb_xf422"
+ "vt_Copy_b64a_rgb_xf444"
+ "vt_Copy_b64a_rgb_yuvsf"
+ "vt_Copy_f420_x422"
+ "vt_Copy_f420_xf22"
+ "vt_Copy_l10r_TRC_Mat_TRC_2vuyf"
+ "vt_Copy_l10r_TRC_Mat_TRC_420vf"
+ "vt_Copy_l10r_TRC_Mat_TRC_422vf"
+ "vt_Copy_l10r_TRC_Mat_TRC_444vf"
+ "vt_Copy_l10r_TRC_Mat_TRC_BGRA"
+ "vt_Copy_l10r_TRC_Mat_TRC_RGfA"
+ "vt_Copy_l10r_TRC_Mat_TRC_RGhA"
+ "vt_Copy_l10r_TRC_Mat_TRC_b64a"
+ "vt_Copy_l10r_TRC_Mat_TRC_l10r"
+ "vt_Copy_l10r_TRC_Mat_TRC_l64r"
+ "vt_Copy_l10r_TRC_Mat_TRC_v216"
+ "vt_Copy_l10r_TRC_Mat_TRC_xf420"
+ "vt_Copy_l10r_TRC_Mat_TRC_xf422"
+ "vt_Copy_l10r_TRC_Mat_TRC_xf444"
+ "vt_Copy_l10r_TRC_Mat_TRC_yuvsf"
+ "vt_Copy_l10r_TRC_Tone_Mat_TRC_2vuyf"
+ "vt_Copy_l10r_TRC_Tone_Mat_TRC_420vf"
+ "vt_Copy_l10r_TRC_Tone_Mat_TRC_422vf"
+ "vt_Copy_l10r_TRC_Tone_Mat_TRC_444vf"
+ "vt_Copy_l10r_TRC_Tone_Mat_TRC_BGRA"
+ "vt_Copy_l10r_TRC_Tone_Mat_TRC_RGfA"
+ "vt_Copy_l10r_TRC_Tone_Mat_TRC_RGhA"
+ "vt_Copy_l10r_TRC_Tone_Mat_TRC_b64a"
+ "vt_Copy_l10r_TRC_Tone_Mat_TRC_l10r"
+ "vt_Copy_l10r_TRC_Tone_Mat_TRC_l64r"
+ "vt_Copy_l10r_TRC_Tone_Mat_TRC_v216"
+ "vt_Copy_l10r_TRC_Tone_Mat_TRC_xf420"
+ "vt_Copy_l10r_TRC_Tone_Mat_TRC_xf422"
+ "vt_Copy_l10r_TRC_Tone_Mat_TRC_xf444"
+ "vt_Copy_l10r_TRC_Tone_Mat_TRC_yuvsf"
+ "vt_Copy_l10r_rgb_2vuyf"
+ "vt_Copy_l10r_rgb_420vf"
+ "vt_Copy_l10r_rgb_422vf"
+ "vt_Copy_l10r_rgb_444vf"
+ "vt_Copy_l10r_rgb_BGRA"
+ "vt_Copy_l10r_rgb_RGfA"
+ "vt_Copy_l10r_rgb_RGhA"
+ "vt_Copy_l10r_rgb_b64a"
+ "vt_Copy_l10r_rgb_l10r"
+ "vt_Copy_l10r_rgb_l64r"
+ "vt_Copy_l10r_rgb_v216"
+ "vt_Copy_l10r_rgb_xf420"
+ "vt_Copy_l10r_rgb_xf422"
+ "vt_Copy_l10r_rgb_xf444"
+ "vt_Copy_l10r_rgb_yuvsf"
+ "vt_Copy_l64r_TRC_Mat_TRC_2vuyf"
+ "vt_Copy_l64r_TRC_Mat_TRC_420vf"
+ "vt_Copy_l64r_TRC_Mat_TRC_422vf"
+ "vt_Copy_l64r_TRC_Mat_TRC_444vf"
+ "vt_Copy_l64r_TRC_Mat_TRC_BGRA"
+ "vt_Copy_l64r_TRC_Mat_TRC_RGfA"
+ "vt_Copy_l64r_TRC_Mat_TRC_RGhA"
+ "vt_Copy_l64r_TRC_Mat_TRC_b64a"
+ "vt_Copy_l64r_TRC_Mat_TRC_l10r"
+ "vt_Copy_l64r_TRC_Mat_TRC_l64r"
+ "vt_Copy_l64r_TRC_Mat_TRC_v216"
+ "vt_Copy_l64r_TRC_Mat_TRC_xf420"
+ "vt_Copy_l64r_TRC_Mat_TRC_xf422"
+ "vt_Copy_l64r_TRC_Mat_TRC_xf444"
+ "vt_Copy_l64r_TRC_Mat_TRC_yuvsf"
+ "vt_Copy_l64r_TRC_Tone_Mat_TRC_2vuyf"
+ "vt_Copy_l64r_TRC_Tone_Mat_TRC_420vf"
+ "vt_Copy_l64r_TRC_Tone_Mat_TRC_422vf"
+ "vt_Copy_l64r_TRC_Tone_Mat_TRC_444vf"
+ "vt_Copy_l64r_TRC_Tone_Mat_TRC_BGRA"
+ "vt_Copy_l64r_TRC_Tone_Mat_TRC_RGfA"
+ "vt_Copy_l64r_TRC_Tone_Mat_TRC_RGhA"
+ "vt_Copy_l64r_TRC_Tone_Mat_TRC_b64a"
+ "vt_Copy_l64r_TRC_Tone_Mat_TRC_l10r"
+ "vt_Copy_l64r_TRC_Tone_Mat_TRC_l64r"
+ "vt_Copy_l64r_TRC_Tone_Mat_TRC_v216"
+ "vt_Copy_l64r_TRC_Tone_Mat_TRC_xf420"
+ "vt_Copy_l64r_TRC_Tone_Mat_TRC_xf422"
+ "vt_Copy_l64r_TRC_Tone_Mat_TRC_xf444"
+ "vt_Copy_l64r_TRC_Tone_Mat_TRC_yuvsf"
+ "vt_Copy_l64r_rgb_2vuyf"
+ "vt_Copy_l64r_rgb_420vf"
+ "vt_Copy_l64r_rgb_422vf"
+ "vt_Copy_l64r_rgb_444vf"
+ "vt_Copy_l64r_rgb_BGRA"
+ "vt_Copy_l64r_rgb_RGfA"
+ "vt_Copy_l64r_rgb_RGhA"
+ "vt_Copy_l64r_rgb_b64a"
+ "vt_Copy_l64r_rgb_l10r"
+ "vt_Copy_l64r_rgb_l64r"
+ "vt_Copy_l64r_rgb_v216"
+ "vt_Copy_l64r_rgb_xf420"
+ "vt_Copy_l64r_rgb_xf422"
+ "vt_Copy_l64r_rgb_xf444"
+ "vt_Copy_l64r_rgb_yuvsf"
+ "vt_Copy_p420ITU2020_ARGB"
+ "vt_Copy_p420ITU2020_BGRA"
+ "vt_Copy_p420ITU2020_RGfA"
+ "vt_Copy_p420ITU2020_RGhA"
+ "vt_Copy_p420ITU2020_l64r"
+ "vt_Copy_p420ITU601_ARGB"
+ "vt_Copy_p420ITU601_BGRA"
+ "vt_Copy_p420ITU601_RGfA"
+ "vt_Copy_p420ITU601_RGhA"
+ "vt_Copy_p420ITU601_l64r"
+ "vt_Copy_p420ITU709_ARGB"
+ "vt_Copy_p420ITU709_BGRA"
+ "vt_Copy_p420ITU709_RGfA"
+ "vt_Copy_p420ITU709_RGhA"
+ "vt_Copy_p420ITU709_l64r"
+ "vt_Copy_p420_420f"
+ "vt_Copy_p420_420v"
+ "vt_Copy_p420_f420"
+ "vt_Copy_p420_x420"
+ "vt_Copy_p420_xf20"
+ "vt_Copy_p420_y420"
+ "vt_Copy_pf20ITU2020_ARGB"
+ "vt_Copy_pf20ITU2020_BGRA"
+ "vt_Copy_pf20ITU2020_RGfA"
+ "vt_Copy_pf20ITU2020_RGhA"
+ "vt_Copy_pf20ITU2020_l64r"
+ "vt_Copy_pf20ITU601_ARGB"
+ "vt_Copy_pf20ITU601_BGRA"
+ "vt_Copy_pf20ITU601_RGfA"
+ "vt_Copy_pf20ITU601_RGhA"
+ "vt_Copy_pf20ITU601_l64r"
+ "vt_Copy_pf20ITU709_ARGB"
+ "vt_Copy_pf20ITU709_BGRA"
+ "vt_Copy_pf20ITU709_RGfA"
+ "vt_Copy_pf20ITU709_RGhA"
+ "vt_Copy_pf20ITU709_l64r"
+ "vt_Copy_pf20_420f"
+ "vt_Copy_pf20_420v"
+ "vt_Copy_pf20_f420"
+ "vt_Copy_pf20_x420"
+ "vt_Copy_pf20_xf20"
+ "vt_Copy_pf20_y420"
+ "vt_Copy_s2as_s4as"
+ "vt_Copy_s2as_t2as"
+ "vt_Copy_s2as_t4as"
+ "vt_Copy_s2as_v0a8"
+ "vt_Copy_s2as_v2a8"
+ "vt_Copy_s2as_v4a8"
+ "vt_Copy_s2as_x2as"
+ "vt_Copy_s2as_x4as"
+ "vt_Copy_s2as_y408"
+ "vt_Copy_s2as_y416"
+ "vt_Copy_s4as_s2as"
+ "vt_Copy_s4as_t2as"
+ "vt_Copy_s4as_t4as"
+ "vt_Copy_s4as_v0a8"
+ "vt_Copy_s4as_v2a8"
+ "vt_Copy_s4as_v4a8"
+ "vt_Copy_s4as_x2as"
+ "vt_Copy_s4as_x4as"
+ "vt_Copy_s4as_y408"
+ "vt_Copy_s4as_y416"
+ "vt_Copy_sf20_2vuy"
+ "vt_Copy_sf20_420f"
+ "vt_Copy_sf20_420v"
+ "vt_Copy_sf20_422f"
+ "vt_Copy_sf20_422v"
+ "vt_Copy_sf20_444f"
+ "vt_Copy_sf20_444v"
+ "vt_Copy_sf20_f420"
+ "vt_Copy_sf20_s2as"
+ "vt_Copy_sf20_s4as"
+ "vt_Copy_sf20_sf22"
+ "vt_Copy_sf20_sf44"
+ "vt_Copy_sf20_sv20"
+ "vt_Copy_sf20_sv22"
+ "vt_Copy_sf20_sv44"
+ "vt_Copy_sf20_t2as"
+ "vt_Copy_sf20_t4as"
+ "vt_Copy_sf20_tf20"
+ "vt_Copy_sf20_tf22"
+ "vt_Copy_sf20_tf44"
+ "vt_Copy_sf20_tv20"
+ "vt_Copy_sf20_tv22"
+ "vt_Copy_sf20_tv44"
+ "vt_Copy_sf20_v0a8"
+ "vt_Copy_sf20_v216"
+ "vt_Copy_sf20_v2a8"
+ "vt_Copy_sf20_v4a8"
+ "vt_Copy_sf20_x2as"
+ "vt_Copy_sf20_x420"
+ "vt_Copy_sf20_x422"
+ "vt_Copy_sf20_x444"
+ "vt_Copy_sf20_x4as"
+ "vt_Copy_sf20_xf20"
+ "vt_Copy_sf20_xf22"
+ "vt_Copy_sf20_xf44"
+ "vt_Copy_sf20_y408"
+ "vt_Copy_sf20_y416"
+ "vt_Copy_sf20_y420"
+ "vt_Copy_sf22_2vuy"
+ "vt_Copy_sf22_420f"
+ "vt_Copy_sf22_420v"
+ "vt_Copy_sf22_422f"
+ "vt_Copy_sf22_422v"
+ "vt_Copy_sf22_444f"
+ "vt_Copy_sf22_444v"
+ "vt_Copy_sf22_f420"
+ "vt_Copy_sf22_s2as"
+ "vt_Copy_sf22_s4as"
+ "vt_Copy_sf22_sf20"
+ "vt_Copy_sf22_sf44"
+ "vt_Copy_sf22_sv20"
+ "vt_Copy_sf22_sv22"
+ "vt_Copy_sf22_sv44"
+ "vt_Copy_sf22_t2as"
+ "vt_Copy_sf22_t4as"
+ "vt_Copy_sf22_tf20"
+ "vt_Copy_sf22_tf22"
+ "vt_Copy_sf22_tf44"
+ "vt_Copy_sf22_tv20"
+ "vt_Copy_sf22_tv22"
+ "vt_Copy_sf22_tv44"
+ "vt_Copy_sf22_v0a8"
+ "vt_Copy_sf22_v216"
+ "vt_Copy_sf22_v2a8"
+ "vt_Copy_sf22_v4a8"
+ "vt_Copy_sf22_x2as"
+ "vt_Copy_sf22_x420"
+ "vt_Copy_sf22_x422"
+ "vt_Copy_sf22_x444"
+ "vt_Copy_sf22_x4as"
+ "vt_Copy_sf22_xf20"
+ "vt_Copy_sf22_xf22"
+ "vt_Copy_sf22_xf44"
+ "vt_Copy_sf22_y408"
+ "vt_Copy_sf22_y416"
+ "vt_Copy_sf22_y420"
+ "vt_Copy_sf44_2vuy"
+ "vt_Copy_sf44_420f"
+ "vt_Copy_sf44_420v"
+ "vt_Copy_sf44_422f"
+ "vt_Copy_sf44_422v"
+ "vt_Copy_sf44_444f"
+ "vt_Copy_sf44_444v"
+ "vt_Copy_sf44_f420"
+ "vt_Copy_sf44_s2as"
+ "vt_Copy_sf44_s4as"
+ "vt_Copy_sf44_sf20"
+ "vt_Copy_sf44_sf22"
+ "vt_Copy_sf44_sv20"
+ "vt_Copy_sf44_sv22"
+ "vt_Copy_sf44_sv44"
+ "vt_Copy_sf44_t2as"
+ "vt_Copy_sf44_t4as"
+ "vt_Copy_sf44_tf20"
+ "vt_Copy_sf44_tf22"
+ "vt_Copy_sf44_tf44"
+ "vt_Copy_sf44_tv20"
+ "vt_Copy_sf44_tv22"
+ "vt_Copy_sf44_tv44"
+ "vt_Copy_sf44_v0a8"
+ "vt_Copy_sf44_v216"
+ "vt_Copy_sf44_v2a8"
+ "vt_Copy_sf44_v4a8"
+ "vt_Copy_sf44_x2as"
+ "vt_Copy_sf44_x420"
+ "vt_Copy_sf44_x422"
+ "vt_Copy_sf44_x444"
+ "vt_Copy_sf44_x4as"
+ "vt_Copy_sf44_xf20"
+ "vt_Copy_sf44_xf22"
+ "vt_Copy_sf44_xf44"
+ "vt_Copy_sf44_y408"
+ "vt_Copy_sf44_y416"
+ "vt_Copy_sf44_y420"
+ "vt_Copy_sv20_2vuy"
+ "vt_Copy_sv20_420f"
+ "vt_Copy_sv20_420v"
+ "vt_Copy_sv20_422f"
+ "vt_Copy_sv20_422v"
+ "vt_Copy_sv20_444f"
+ "vt_Copy_sv20_444v"
+ "vt_Copy_sv20_f420"
+ "vt_Copy_sv20_s2as"
+ "vt_Copy_sv20_s4as"
+ "vt_Copy_sv20_sf20"
+ "vt_Copy_sv20_sf22"
+ "vt_Copy_sv20_sf44"
+ "vt_Copy_sv20_sv22"
+ "vt_Copy_sv20_sv44"
+ "vt_Copy_sv20_t2as"
+ "vt_Copy_sv20_t4as"
+ "vt_Copy_sv20_tf20"
+ "vt_Copy_sv20_tf22"
+ "vt_Copy_sv20_tf44"
+ "vt_Copy_sv20_tv20"
+ "vt_Copy_sv20_tv22"
+ "vt_Copy_sv20_tv44"
+ "vt_Copy_sv20_v0a8"
+ "vt_Copy_sv20_v216"
+ "vt_Copy_sv20_v2a8"
+ "vt_Copy_sv20_v4a8"
+ "vt_Copy_sv20_x2as"
+ "vt_Copy_sv20_x420"
+ "vt_Copy_sv20_x422"
+ "vt_Copy_sv20_x444"
+ "vt_Copy_sv20_x4as"
+ "vt_Copy_sv20_xf20"
+ "vt_Copy_sv20_xf22"
+ "vt_Copy_sv20_xf44"
+ "vt_Copy_sv20_y408"
+ "vt_Copy_sv20_y416"
+ "vt_Copy_sv20_y420"
+ "vt_Copy_sv22_2vuy"
+ "vt_Copy_sv22_420f"
+ "vt_Copy_sv22_420v"
+ "vt_Copy_sv22_422f"
+ "vt_Copy_sv22_422v"
+ "vt_Copy_sv22_444f"
+ "vt_Copy_sv22_444v"
+ "vt_Copy_sv22_f420"
+ "vt_Copy_sv22_s2as"
+ "vt_Copy_sv22_s4as"
+ "vt_Copy_sv22_sf20"
+ "vt_Copy_sv22_sf22"
+ "vt_Copy_sv22_sf44"
+ "vt_Copy_sv22_sv20"
+ "vt_Copy_sv22_sv44"
+ "vt_Copy_sv22_t2as"
+ "vt_Copy_sv22_t4as"
+ "vt_Copy_sv22_tf20"
+ "vt_Copy_sv22_tf22"
+ "vt_Copy_sv22_tf44"
+ "vt_Copy_sv22_tv20"
+ "vt_Copy_sv22_tv22"
+ "vt_Copy_sv22_tv44"
+ "vt_Copy_sv22_v0a8"
+ "vt_Copy_sv22_v216"
+ "vt_Copy_sv22_v2a8"
+ "vt_Copy_sv22_v4a8"
+ "vt_Copy_sv22_x2as"
+ "vt_Copy_sv22_x420"
+ "vt_Copy_sv22_x422"
+ "vt_Copy_sv22_x444"
+ "vt_Copy_sv22_x4as"
+ "vt_Copy_sv22_xf20"
+ "vt_Copy_sv22_xf22"
+ "vt_Copy_sv22_xf44"
+ "vt_Copy_sv22_y408"
+ "vt_Copy_sv22_y416"
+ "vt_Copy_sv22_y420"
+ "vt_Copy_sv44_2vuy"
+ "vt_Copy_sv44_420f"
+ "vt_Copy_sv44_420v"
+ "vt_Copy_sv44_422f"
+ "vt_Copy_sv44_422v"
+ "vt_Copy_sv44_444f"
+ "vt_Copy_sv44_444v"
+ "vt_Copy_sv44_f420"
+ "vt_Copy_sv44_s2as"
+ "vt_Copy_sv44_s4as"
+ "vt_Copy_sv44_sf20"
+ "vt_Copy_sv44_sf22"
+ "vt_Copy_sv44_sf44"
+ "vt_Copy_sv44_sv20"
+ "vt_Copy_sv44_sv22"
+ "vt_Copy_sv44_t2as"
+ "vt_Copy_sv44_t4as"
+ "vt_Copy_sv44_tf20"
+ "vt_Copy_sv44_tf22"
+ "vt_Copy_sv44_tf44"
+ "vt_Copy_sv44_tv20"
+ "vt_Copy_sv44_tv22"
+ "vt_Copy_sv44_tv44"
+ "vt_Copy_sv44_v0a8"
+ "vt_Copy_sv44_v216"
+ "vt_Copy_sv44_v2a8"
+ "vt_Copy_sv44_v4a8"
+ "vt_Copy_sv44_x2as"
+ "vt_Copy_sv44_x420"
+ "vt_Copy_sv44_x422"
+ "vt_Copy_sv44_x444"
+ "vt_Copy_sv44_x4as"
+ "vt_Copy_sv44_xf20"
+ "vt_Copy_sv44_xf22"
+ "vt_Copy_sv44_xf44"
+ "vt_Copy_sv44_y408"
+ "vt_Copy_sv44_y416"
+ "vt_Copy_sv44_y420"
+ "vt_Copy_t2as_s2as"
+ "vt_Copy_t2as_s4as"
+ "vt_Copy_t2as_t4as"
+ "vt_Copy_t2as_v0a8"
+ "vt_Copy_t2as_v2a8"
+ "vt_Copy_t2as_v4a8"
+ "vt_Copy_t2as_x2as"
+ "vt_Copy_t2as_x4as"
+ "vt_Copy_t2as_y408"
+ "vt_Copy_t2as_y416"
+ "vt_Copy_t4as_s2as"
+ "vt_Copy_t4as_s4as"
+ "vt_Copy_t4as_t2as"
+ "vt_Copy_t4as_v0a8"
+ "vt_Copy_t4as_v2a8"
+ "vt_Copy_t4as_v4a8"
+ "vt_Copy_t4as_x2as"
+ "vt_Copy_t4as_x4as"
+ "vt_Copy_t4as_y408"
+ "vt_Copy_t4as_y416"
+ "vt_Copy_tf20_2vuy"
+ "vt_Copy_tf20_420f"
+ "vt_Copy_tf20_420v"
+ "vt_Copy_tf20_422f"
+ "vt_Copy_tf20_422v"
+ "vt_Copy_tf20_444f"
+ "vt_Copy_tf20_444v"
+ "vt_Copy_tf20_f420"
+ "vt_Copy_tf20_s2as"
+ "vt_Copy_tf20_s4as"
+ "vt_Copy_tf20_sf20"
+ "vt_Copy_tf20_sf22"
+ "vt_Copy_tf20_sf44"
+ "vt_Copy_tf20_sv20"
+ "vt_Copy_tf20_sv22"
+ "vt_Copy_tf20_sv44"
+ "vt_Copy_tf20_t2as"
+ "vt_Copy_tf20_t4as"
+ "vt_Copy_tf20_tf22"
+ "vt_Copy_tf20_tf44"
+ "vt_Copy_tf20_tv20"
+ "vt_Copy_tf20_tv22"
+ "vt_Copy_tf20_tv44"
+ "vt_Copy_tf20_v0a8"
+ "vt_Copy_tf20_v216"
+ "vt_Copy_tf20_v2a8"
+ "vt_Copy_tf20_v4a8"
+ "vt_Copy_tf20_x2as"
+ "vt_Copy_tf20_x420"
+ "vt_Copy_tf20_x422"
+ "vt_Copy_tf20_x444"
+ "vt_Copy_tf20_x4as"
+ "vt_Copy_tf20_xf20"
+ "vt_Copy_tf20_xf22"
+ "vt_Copy_tf20_xf44"
+ "vt_Copy_tf20_y408"
+ "vt_Copy_tf20_y416"
+ "vt_Copy_tf20_y420"
+ "vt_Copy_tf22_2vuy"
+ "vt_Copy_tf22_420f"
+ "vt_Copy_tf22_420v"
+ "vt_Copy_tf22_422f"
+ "vt_Copy_tf22_422v"
+ "vt_Copy_tf22_444f"
+ "vt_Copy_tf22_444v"
+ "vt_Copy_tf22_f420"
+ "vt_Copy_tf22_s2as"
+ "vt_Copy_tf22_s4as"
+ "vt_Copy_tf22_sf20"
+ "vt_Copy_tf22_sf22"
+ "vt_Copy_tf22_sf44"
+ "vt_Copy_tf22_sv20"
+ "vt_Copy_tf22_sv22"
+ "vt_Copy_tf22_sv44"
+ "vt_Copy_tf22_t2as"
+ "vt_Copy_tf22_t4as"
+ "vt_Copy_tf22_tf20"
+ "vt_Copy_tf22_tf44"
+ "vt_Copy_tf22_tv20"
+ "vt_Copy_tf22_tv22"
+ "vt_Copy_tf22_tv44"
+ "vt_Copy_tf22_v0a8"
+ "vt_Copy_tf22_v216"
+ "vt_Copy_tf22_v2a8"
+ "vt_Copy_tf22_v4a8"
+ "vt_Copy_tf22_x2as"
+ "vt_Copy_tf22_x420"
+ "vt_Copy_tf22_x422"
+ "vt_Copy_tf22_x444"
+ "vt_Copy_tf22_x4as"
+ "vt_Copy_tf22_xf20"
+ "vt_Copy_tf22_xf22"
+ "vt_Copy_tf22_xf44"
+ "vt_Copy_tf22_y408"
+ "vt_Copy_tf22_y416"
+ "vt_Copy_tf22_y420"
+ "vt_Copy_tf44_2vuy"
+ "vt_Copy_tf44_420f"
+ "vt_Copy_tf44_420v"
+ "vt_Copy_tf44_422f"
+ "vt_Copy_tf44_422v"
+ "vt_Copy_tf44_444f"
+ "vt_Copy_tf44_444v"
+ "vt_Copy_tf44_f420"
+ "vt_Copy_tf44_s2as"
+ "vt_Copy_tf44_s4as"
+ "vt_Copy_tf44_sf20"
+ "vt_Copy_tf44_sf22"
+ "vt_Copy_tf44_sf44"
+ "vt_Copy_tf44_sv20"
+ "vt_Copy_tf44_sv22"
+ "vt_Copy_tf44_sv44"
+ "vt_Copy_tf44_t2as"
+ "vt_Copy_tf44_t4as"
+ "vt_Copy_tf44_tf20"
+ "vt_Copy_tf44_tf22"
+ "vt_Copy_tf44_tv20"
+ "vt_Copy_tf44_tv22"
+ "vt_Copy_tf44_tv44"
+ "vt_Copy_tf44_v0a8"
+ "vt_Copy_tf44_v216"
+ "vt_Copy_tf44_v2a8"
+ "vt_Copy_tf44_v4a8"
+ "vt_Copy_tf44_x2as"
+ "vt_Copy_tf44_x420"
+ "vt_Copy_tf44_x422"
+ "vt_Copy_tf44_x444"
+ "vt_Copy_tf44_x4as"
+ "vt_Copy_tf44_xf20"
+ "vt_Copy_tf44_xf22"
+ "vt_Copy_tf44_xf44"
+ "vt_Copy_tf44_y408"
+ "vt_Copy_tf44_y416"
+ "vt_Copy_tf44_y420"
+ "vt_Copy_tv20_2vuy"
+ "vt_Copy_tv20_420f"
+ "vt_Copy_tv20_420v"
+ "vt_Copy_tv20_422f"
+ "vt_Copy_tv20_422v"
+ "vt_Copy_tv20_444f"
+ "vt_Copy_tv20_444v"
+ "vt_Copy_tv20_f420"
+ "vt_Copy_tv20_s2as"
+ "vt_Copy_tv20_s4as"
+ "vt_Copy_tv20_sf20"
+ "vt_Copy_tv20_sf22"
+ "vt_Copy_tv20_sf44"
+ "vt_Copy_tv20_sv20"
+ "vt_Copy_tv20_sv22"
+ "vt_Copy_tv20_sv44"
+ "vt_Copy_tv20_t2as"
+ "vt_Copy_tv20_t4as"
+ "vt_Copy_tv20_tf20"
+ "vt_Copy_tv20_tf22"
+ "vt_Copy_tv20_tf44"
+ "vt_Copy_tv20_tv22"
+ "vt_Copy_tv20_tv44"
+ "vt_Copy_tv20_v0a8"
+ "vt_Copy_tv20_v216"
+ "vt_Copy_tv20_v2a8"
+ "vt_Copy_tv20_v4a8"
+ "vt_Copy_tv20_x2as"
+ "vt_Copy_tv20_x420"
+ "vt_Copy_tv20_x422"
+ "vt_Copy_tv20_x444"
+ "vt_Copy_tv20_x4as"
+ "vt_Copy_tv20_xf20"
+ "vt_Copy_tv20_xf22"
+ "vt_Copy_tv20_xf44"
+ "vt_Copy_tv20_y408"
+ "vt_Copy_tv20_y416"
+ "vt_Copy_tv20_y420"
+ "vt_Copy_tv22_2vuy"
+ "vt_Copy_tv22_420f"
+ "vt_Copy_tv22_420v"
+ "vt_Copy_tv22_422f"
+ "vt_Copy_tv22_422v"
+ "vt_Copy_tv22_444f"
+ "vt_Copy_tv22_444v"
+ "vt_Copy_tv22_f420"
+ "vt_Copy_tv22_s2as"
+ "vt_Copy_tv22_s4as"
+ "vt_Copy_tv22_sf20"
+ "vt_Copy_tv22_sf22"
+ "vt_Copy_tv22_sf44"
+ "vt_Copy_tv22_sv20"
+ "vt_Copy_tv22_sv22"
+ "vt_Copy_tv22_sv44"
+ "vt_Copy_tv22_t2as"
+ "vt_Copy_tv22_t4as"
+ "vt_Copy_tv22_tf20"
+ "vt_Copy_tv22_tf22"
+ "vt_Copy_tv22_tf44"
+ "vt_Copy_tv22_tv20"
+ "vt_Copy_tv22_tv44"
+ "vt_Copy_tv22_v0a8"
+ "vt_Copy_tv22_v216"
+ "vt_Copy_tv22_v2a8"
+ "vt_Copy_tv22_v4a8"
+ "vt_Copy_tv22_x2as"
+ "vt_Copy_tv22_x420"
+ "vt_Copy_tv22_x422"
+ "vt_Copy_tv22_x444"
+ "vt_Copy_tv22_x4as"
+ "vt_Copy_tv22_xf20"
+ "vt_Copy_tv22_xf22"
+ "vt_Copy_tv22_xf44"
+ "vt_Copy_tv22_y408"
+ "vt_Copy_tv22_y416"
+ "vt_Copy_tv22_y420"
+ "vt_Copy_tv44_2vuy"
+ "vt_Copy_tv44_420f"
+ "vt_Copy_tv44_420v"
+ "vt_Copy_tv44_422f"
+ "vt_Copy_tv44_422v"
+ "vt_Copy_tv44_444f"
+ "vt_Copy_tv44_444v"
+ "vt_Copy_tv44_f420"
+ "vt_Copy_tv44_s2as"
+ "vt_Copy_tv44_s4as"
+ "vt_Copy_tv44_sf20"
+ "vt_Copy_tv44_sf22"
+ "vt_Copy_tv44_sf44"
+ "vt_Copy_tv44_sv20"
+ "vt_Copy_tv44_sv22"
+ "vt_Copy_tv44_sv44"
+ "vt_Copy_tv44_t2as"
+ "vt_Copy_tv44_t4as"
+ "vt_Copy_tv44_tf20"
+ "vt_Copy_tv44_tf22"
+ "vt_Copy_tv44_tf44"
+ "vt_Copy_tv44_tv20"
+ "vt_Copy_tv44_tv22"
+ "vt_Copy_tv44_v0a8"
+ "vt_Copy_tv44_v216"
+ "vt_Copy_tv44_v2a8"
+ "vt_Copy_tv44_v4a8"
+ "vt_Copy_tv44_x2as"
+ "vt_Copy_tv44_x420"
+ "vt_Copy_tv44_x422"
+ "vt_Copy_tv44_x444"
+ "vt_Copy_tv44_x4as"
+ "vt_Copy_tv44_xf20"
+ "vt_Copy_tv44_xf22"
+ "vt_Copy_tv44_xf44"
+ "vt_Copy_tv44_y408"
+ "vt_Copy_tv44_y416"
+ "vt_Copy_tv44_y420"
+ "vt_Copy_v0a8"
+ "vt_Copy_v0a8_Crop"
+ "vt_Copy_v0a8_s2as"
+ "vt_Copy_v0a8_s4as"
+ "vt_Copy_v0a8_t2as"
+ "vt_Copy_v0a8_t4as"
+ "vt_Copy_v0a8_v2a8"
+ "vt_Copy_v0a8_v4a8"
+ "vt_Copy_v0a8_x2as"
+ "vt_Copy_v0a8_x4as"
+ "vt_Copy_v0a8_y408"
+ "vt_Copy_v0a8_y416"
+ "vt_Copy_v210"
+ "vt_Copy_v210_2vuy"
+ "vt_Copy_v210_420f"
+ "vt_Copy_v210_420v"
+ "vt_Copy_v210_422v"
+ "vt_Copy_v210_Crop"
+ "vt_Copy_v210_x420"
+ "vt_Copy_v210_x422"
+ "vt_Copy_v210_xf20"
+ "vt_Copy_v210_yuvs"
+ "vt_Copy_v216_420f"
+ "vt_Copy_v216_420v"
+ "vt_Copy_v216_422f"
+ "vt_Copy_v216_422v"
+ "vt_Copy_v216_444f"
+ "vt_Copy_v216_444v"
+ "vt_Copy_v216_f420"
+ "vt_Copy_v216_s2as"
+ "vt_Copy_v216_s4as"
+ "vt_Copy_v216_sf20"
+ "vt_Copy_v216_sf22"
+ "vt_Copy_v216_sf44"
+ "vt_Copy_v216_sv20"
+ "vt_Copy_v216_sv22"
+ "vt_Copy_v216_sv44"
+ "vt_Copy_v216_t2as"
+ "vt_Copy_v216_t4as"
+ "vt_Copy_v216_tf20"
+ "vt_Copy_v216_tf22"
+ "vt_Copy_v216_tf44"
+ "vt_Copy_v216_tv20"
+ "vt_Copy_v216_tv22"
+ "vt_Copy_v216_tv44"
+ "vt_Copy_v216_v0a8"
+ "vt_Copy_v216_v2a8"
+ "vt_Copy_v216_v4a8"
+ "vt_Copy_v216_x2as"
+ "vt_Copy_v216_x420"
+ "vt_Copy_v216_x422"
+ "vt_Copy_v216_x444"
+ "vt_Copy_v216_x4as"
+ "vt_Copy_v216_xf20"
+ "vt_Copy_v216_xf22"
+ "vt_Copy_v216_xf44"
+ "vt_Copy_v216_y420"
+ "vt_Copy_v2a8"
+ "vt_Copy_v2a8_Crop"
+ "vt_Copy_v2a8_s2as"
+ "vt_Copy_v2a8_s4as"
+ "vt_Copy_v2a8_t2as"
+ "vt_Copy_v2a8_t4as"
+ "vt_Copy_v2a8_v0a8"
+ "vt_Copy_v2a8_v4a8"
+ "vt_Copy_v2a8_x2as"
+ "vt_Copy_v2a8_x4as"
+ "vt_Copy_v2a8_y408"
+ "vt_Copy_v2a8_y416"
+ "vt_Copy_v4a8"
+ "vt_Copy_v4a8_Crop"
+ "vt_Copy_v4a8_s2as"
+ "vt_Copy_v4a8_s4as"
+ "vt_Copy_v4a8_t2as"
+ "vt_Copy_v4a8_t4as"
+ "vt_Copy_v4a8_v0a8"
+ "vt_Copy_v4a8_v2a8"
+ "vt_Copy_v4a8_x2as"
+ "vt_Copy_v4a8_x4as"
+ "vt_Copy_v4a8_y408"
+ "vt_Copy_v4a8_y416"
+ "vt_Copy_w30r_b3a8"
+ "vt_Copy_w30r_b3a8_Crop"
+ "vt_Copy_x2as"
+ "vt_Copy_x2as_Crop"
+ "vt_Copy_x2as_s2as"
+ "vt_Copy_x2as_s4as"
+ "vt_Copy_x2as_t2as"
+ "vt_Copy_x2as_t4as"
+ "vt_Copy_x2as_v0a8"
+ "vt_Copy_x2as_v2a8"
+ "vt_Copy_x2as_v4a8"
+ "vt_Copy_x2as_x4as"
+ "vt_Copy_x2as_y408"
+ "vt_Copy_x2as_y416"
+ "vt_Copy_x420"
+ "vt_Copy_x420_2vuy"
+ "vt_Copy_x420_420f"
+ "vt_Copy_x420_420v"
+ "vt_Copy_x420_422f"
+ "vt_Copy_x420_422v"
+ "vt_Copy_x420_444f"
+ "vt_Copy_x420_444v"
+ "vt_Copy_x420_Crop"
+ "vt_Copy_x420_f420"
+ "vt_Copy_x420_s2as"
+ "vt_Copy_x420_s4as"
+ "vt_Copy_x420_sf20"
+ "vt_Copy_x420_sf22"
+ "vt_Copy_x420_sf44"
+ "vt_Copy_x420_sv20"
+ "vt_Copy_x420_sv22"
+ "vt_Copy_x420_sv44"
+ "vt_Copy_x420_t2as"
+ "vt_Copy_x420_t4as"
+ "vt_Copy_x420_tf20"
+ "vt_Copy_x420_tf22"
+ "vt_Copy_x420_tf44"
+ "vt_Copy_x420_tv20"
+ "vt_Copy_x420_tv22"
+ "vt_Copy_x420_tv44"
+ "vt_Copy_x420_v0a8"
+ "vt_Copy_x420_v216"
+ "vt_Copy_x420_v2a8"
+ "vt_Copy_x420_v4a8"
+ "vt_Copy_x420_x2as"
+ "vt_Copy_x420_x422"
+ "vt_Copy_x420_x444"
+ "vt_Copy_x420_x4as"
+ "vt_Copy_x420_xf20"
+ "vt_Copy_x420_xf22"
+ "vt_Copy_x420_xf44"
+ "vt_Copy_x420_y408"
+ "vt_Copy_x420_y416"
+ "vt_Copy_x420_y420"
+ "vt_Copy_x422"
+ "vt_Copy_x422_2vuy"
+ "vt_Copy_x422_420f"
+ "vt_Copy_x422_420v"
+ "vt_Copy_x422_422f"
+ "vt_Copy_x422_422v"
+ "vt_Copy_x422_444f"
+ "vt_Copy_x422_444v"
+ "vt_Copy_x422_Crop"
+ "vt_Copy_x422_f420"
+ "vt_Copy_x422_s2as"
+ "vt_Copy_x422_s4as"
+ "vt_Copy_x422_sf20"
+ "vt_Copy_x422_sf22"
+ "vt_Copy_x422_sf44"
+ "vt_Copy_x422_sv20"
+ "vt_Copy_x422_sv22"
+ "vt_Copy_x422_sv44"
+ "vt_Copy_x422_t2as"
+ "vt_Copy_x422_t4as"
+ "vt_Copy_x422_tf20"
+ "vt_Copy_x422_tf22"
+ "vt_Copy_x422_tf44"
+ "vt_Copy_x422_tv20"
+ "vt_Copy_x422_tv22"
+ "vt_Copy_x422_tv44"
+ "vt_Copy_x422_v0a8"
+ "vt_Copy_x422_v210"
+ "vt_Copy_x422_v216"
+ "vt_Copy_x422_v2a8"
+ "vt_Copy_x422_v4a8"
+ "vt_Copy_x422_x2as"
+ "vt_Copy_x422_x420"
+ "vt_Copy_x422_x444"
+ "vt_Copy_x422_x4as"
+ "vt_Copy_x422_xf20"
+ "vt_Copy_x422_xf22"
+ "vt_Copy_x422_xf44"
+ "vt_Copy_x422_y408"
+ "vt_Copy_x422_y416"
+ "vt_Copy_x422_y420"
+ "vt_Copy_x444"
+ "vt_Copy_x444_2vuy"
+ "vt_Copy_x444_420f"
+ "vt_Copy_x444_420v"
+ "vt_Copy_x444_422f"
+ "vt_Copy_x444_422v"
+ "vt_Copy_x444_444f"
+ "vt_Copy_x444_444v"
+ "vt_Copy_x444_Crop"
+ "vt_Copy_x444_f420"
+ "vt_Copy_x444_s2as"
+ "vt_Copy_x444_s4as"
+ "vt_Copy_x444_sf20"
+ "vt_Copy_x444_sf22"
+ "vt_Copy_x444_sf44"
+ "vt_Copy_x444_sv20"
+ "vt_Copy_x444_sv22"
+ "vt_Copy_x444_sv44"
+ "vt_Copy_x444_t2as"
+ "vt_Copy_x444_t4as"
+ "vt_Copy_x444_tf20"
+ "vt_Copy_x444_tf22"
+ "vt_Copy_x444_tf44"
+ "vt_Copy_x444_tv20"
+ "vt_Copy_x444_tv22"
+ "vt_Copy_x444_tv44"
+ "vt_Copy_x444_v0a8"
+ "vt_Copy_x444_v216"
+ "vt_Copy_x444_v2a8"
+ "vt_Copy_x444_v4a8"
+ "vt_Copy_x444_x2as"
+ "vt_Copy_x444_x420"
+ "vt_Copy_x444_x422"
+ "vt_Copy_x444_x44p"
+ "vt_Copy_x444_x4as"
+ "vt_Copy_x444_xf20"
+ "vt_Copy_x444_xf22"
+ "vt_Copy_x444_xf44"
+ "vt_Copy_x444_y408"
+ "vt_Copy_x444_y416"
+ "vt_Copy_x444_y420"
+ "vt_Copy_x44p_x444"
+ "vt_Copy_x4as"
+ "vt_Copy_x4as_Crop"
+ "vt_Copy_x4as_s2as"
+ "vt_Copy_x4as_s4as"
+ "vt_Copy_x4as_t2as"
+ "vt_Copy_x4as_t4as"
+ "vt_Copy_x4as_v0a8"
+ "vt_Copy_x4as_v2a8"
+ "vt_Copy_x4as_v4a8"
+ "vt_Copy_x4as_x2as"
+ "vt_Copy_x4as_y408"
+ "vt_Copy_x4as_y416"
+ "vt_Copy_xf20_2vuy"
+ "vt_Copy_xf20_420v"
+ "vt_Copy_xf20_422f"
+ "vt_Copy_xf20_422v"
+ "vt_Copy_xf20_444f"
+ "vt_Copy_xf20_444v"
+ "vt_Copy_xf20_f420"
+ "vt_Copy_xf20_s2as"
+ "vt_Copy_xf20_s4as"
+ "vt_Copy_xf20_sf20"
+ "vt_Copy_xf20_sf22"
+ "vt_Copy_xf20_sf44"
+ "vt_Copy_xf20_sv20"
+ "vt_Copy_xf20_sv22"
+ "vt_Copy_xf20_sv44"
+ "vt_Copy_xf20_t2as"
+ "vt_Copy_xf20_t4as"
+ "vt_Copy_xf20_tf20"
+ "vt_Copy_xf20_tf22"
+ "vt_Copy_xf20_tf44"
+ "vt_Copy_xf20_tv20"
+ "vt_Copy_xf20_tv22"
+ "vt_Copy_xf20_tv44"
+ "vt_Copy_xf20_v0a8"
+ "vt_Copy_xf20_v216"
+ "vt_Copy_xf20_v2a8"
+ "vt_Copy_xf20_v4a8"
+ "vt_Copy_xf20_x2as"
+ "vt_Copy_xf20_x420"
+ "vt_Copy_xf20_x422"
+ "vt_Copy_xf20_x444"
+ "vt_Copy_xf20_x4as"
+ "vt_Copy_xf20_xf22"
+ "vt_Copy_xf20_xf44"
+ "vt_Copy_xf20_y408"
+ "vt_Copy_xf20_y416"
+ "vt_Copy_xf20_y420"
+ "vt_Copy_xf22_2vuy"
+ "vt_Copy_xf22_420f"
+ "vt_Copy_xf22_420v"
+ "vt_Copy_xf22_422f"
+ "vt_Copy_xf22_422v"
+ "vt_Copy_xf22_444f"
+ "vt_Copy_xf22_444v"
+ "vt_Copy_xf22_f420"
+ "vt_Copy_xf22_s2as"
+ "vt_Copy_xf22_s4as"
+ "vt_Copy_xf22_sf20"
+ "vt_Copy_xf22_sf22"
+ "vt_Copy_xf22_sf44"
+ "vt_Copy_xf22_sv20"
+ "vt_Copy_xf22_sv22"
+ "vt_Copy_xf22_sv44"
+ "vt_Copy_xf22_t2as"
+ "vt_Copy_xf22_t4as"
+ "vt_Copy_xf22_tf20"
+ "vt_Copy_xf22_tf22"
+ "vt_Copy_xf22_tf44"
+ "vt_Copy_xf22_tv20"
+ "vt_Copy_xf22_tv22"
+ "vt_Copy_xf22_tv44"
+ "vt_Copy_xf22_v0a8"
+ "vt_Copy_xf22_v216"
+ "vt_Copy_xf22_v2a8"
+ "vt_Copy_xf22_v4a8"
+ "vt_Copy_xf22_x2as"
+ "vt_Copy_xf22_x420"
+ "vt_Copy_xf22_x422"
+ "vt_Copy_xf22_x444"
+ "vt_Copy_xf22_x4as"
+ "vt_Copy_xf22_xf20"
+ "vt_Copy_xf22_xf44"
+ "vt_Copy_xf22_y408"
+ "vt_Copy_xf22_y416"
+ "vt_Copy_xf22_y420"
+ "vt_Copy_xf420_TRC_Mat_TRC_2vuyf"
+ "vt_Copy_xf420_TRC_Mat_TRC_420vf"
+ "vt_Copy_xf420_TRC_Mat_TRC_420vf_neon_fp16"
+ "vt_Copy_xf420_TRC_Mat_TRC_422vf"
+ "vt_Copy_xf420_TRC_Mat_TRC_422vf_neon_fp16"
+ "vt_Copy_xf420_TRC_Mat_TRC_444vf"
+ "vt_Copy_xf420_TRC_Mat_TRC_444vf_neon_fp16"
+ "vt_Copy_xf420_TRC_Mat_TRC_BGRA"
+ "vt_Copy_xf420_TRC_Mat_TRC_BGRA_neon_fp16"
+ "vt_Copy_xf420_TRC_Mat_TRC_RGfA"
+ "vt_Copy_xf420_TRC_Mat_TRC_RGfA_neon_fp16"
+ "vt_Copy_xf420_TRC_Mat_TRC_RGhA"
+ "vt_Copy_xf420_TRC_Mat_TRC_RGhA_neon_fp16"
+ "vt_Copy_xf420_TRC_Mat_TRC_b64a"
+ "vt_Copy_xf420_TRC_Mat_TRC_l10r"
+ "vt_Copy_xf420_TRC_Mat_TRC_l64r"
+ "vt_Copy_xf420_TRC_Mat_TRC_v216"
+ "vt_Copy_xf420_TRC_Mat_TRC_xf420"
+ "vt_Copy_xf420_TRC_Mat_TRC_xf420_neon_fp16"
+ "vt_Copy_xf420_TRC_Mat_TRC_xf422"
+ "vt_Copy_xf420_TRC_Mat_TRC_xf422_neon_fp16"
+ "vt_Copy_xf420_TRC_Mat_TRC_xf444"
+ "vt_Copy_xf420_TRC_Mat_TRC_xf444_neon_fp16"
+ "vt_Copy_xf420_TRC_Mat_TRC_yuvsf"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_2vuyf"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_420vf"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_420vf_neon_fp16"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_422vf"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_422vf_neon_fp16"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_444vf"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_444vf_neon_fp16"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_BGRA"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_BGRA_neon_fp16"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_RGfA"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_RGfA_neon_fp16"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_RGhA"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_RGhA_neon_fp16"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_b64a"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_l10r"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_l64r"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_v216"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_xf420"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_xf420_neon_fp16"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_xf422"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_xf422_neon_fp16"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_xf444"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_xf444_neon_fp16"
+ "vt_Copy_xf420_TRC_Tone_Mat_TRC_yuvsf"
+ "vt_Copy_xf420_rgb_2vuyf"
+ "vt_Copy_xf420_rgb_420vf"
+ "vt_Copy_xf420_rgb_420vf_neon_fp16"
+ "vt_Copy_xf420_rgb_422vf"
+ "vt_Copy_xf420_rgb_422vf_neon_fp16"
+ "vt_Copy_xf420_rgb_444vf"
+ "vt_Copy_xf420_rgb_444vf_neon_fp16"
+ "vt_Copy_xf420_rgb_BGRA"
+ "vt_Copy_xf420_rgb_BGRA_neon_fp16"
+ "vt_Copy_xf420_rgb_RGfA"
+ "vt_Copy_xf420_rgb_RGfA_neon_fp16"
+ "vt_Copy_xf420_rgb_RGhA"
+ "vt_Copy_xf420_rgb_RGhA_neon_fp16"
+ "vt_Copy_xf420_rgb_b64a"
+ "vt_Copy_xf420_rgb_l10r"
+ "vt_Copy_xf420_rgb_l64r"
+ "vt_Copy_xf420_rgb_v216"
+ "vt_Copy_xf420_rgb_xf420"
+ "vt_Copy_xf420_rgb_xf420_neon_fp16"
+ "vt_Copy_xf420_rgb_xf422"
+ "vt_Copy_xf420_rgb_xf422_neon_fp16"
+ "vt_Copy_xf420_rgb_xf444"
+ "vt_Copy_xf420_rgb_xf444_neon_fp16"
+ "vt_Copy_xf420_rgb_yuvsf"
+ "vt_Copy_xf422_TRC_Mat_TRC_2vuyf"
+ "vt_Copy_xf422_TRC_Mat_TRC_420vf"
+ "vt_Copy_xf422_TRC_Mat_TRC_420vf_neon_fp16"
+ "vt_Copy_xf422_TRC_Mat_TRC_422vf"
+ "vt_Copy_xf422_TRC_Mat_TRC_422vf_neon_fp16"
+ "vt_Copy_xf422_TRC_Mat_TRC_444vf"
+ "vt_Copy_xf422_TRC_Mat_TRC_444vf_neon_fp16"
+ "vt_Copy_xf422_TRC_Mat_TRC_BGRA"
+ "vt_Copy_xf422_TRC_Mat_TRC_BGRA_neon_fp16"
+ "vt_Copy_xf422_TRC_Mat_TRC_RGfA"
+ "vt_Copy_xf422_TRC_Mat_TRC_RGfA_neon_fp16"
+ "vt_Copy_xf422_TRC_Mat_TRC_RGhA"
+ "vt_Copy_xf422_TRC_Mat_TRC_RGhA_neon_fp16"
+ "vt_Copy_xf422_TRC_Mat_TRC_b64a"
+ "vt_Copy_xf422_TRC_Mat_TRC_l10r"
+ "vt_Copy_xf422_TRC_Mat_TRC_l64r"
+ "vt_Copy_xf422_TRC_Mat_TRC_v216"
+ "vt_Copy_xf422_TRC_Mat_TRC_xf420"
+ "vt_Copy_xf422_TRC_Mat_TRC_xf420_neon_fp16"
+ "vt_Copy_xf422_TRC_Mat_TRC_xf422"
+ "vt_Copy_xf422_TRC_Mat_TRC_xf422_neon_fp16"
+ "vt_Copy_xf422_TRC_Mat_TRC_xf444"
+ "vt_Copy_xf422_TRC_Mat_TRC_xf444_neon_fp16"
+ "vt_Copy_xf422_TRC_Mat_TRC_yuvsf"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_2vuyf"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_420vf"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_420vf_neon_fp16"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_422vf"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_422vf_neon_fp16"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_444vf"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_444vf_neon_fp16"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_BGRA"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_BGRA_neon_fp16"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_RGfA"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_RGfA_neon_fp16"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_RGhA"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_RGhA_neon_fp16"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_b64a"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_l10r"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_l64r"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_v216"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_xf420"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_xf420_neon_fp16"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_xf422"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_xf422_neon_fp16"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_xf444"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_xf444_neon_fp16"
+ "vt_Copy_xf422_TRC_Tone_Mat_TRC_yuvsf"
+ "vt_Copy_xf422_rgb_2vuyf"
+ "vt_Copy_xf422_rgb_420vf"
+ "vt_Copy_xf422_rgb_420vf_neon_fp16"
+ "vt_Copy_xf422_rgb_422vf"
+ "vt_Copy_xf422_rgb_422vf_neon_fp16"
+ "vt_Copy_xf422_rgb_444vf"
+ "vt_Copy_xf422_rgb_444vf_neon_fp16"
+ "vt_Copy_xf422_rgb_BGRA"
+ "vt_Copy_xf422_rgb_BGRA_neon_fp16"
+ "vt_Copy_xf422_rgb_RGfA"
+ "vt_Copy_xf422_rgb_RGfA_neon_fp16"
+ "vt_Copy_xf422_rgb_RGhA"
+ "vt_Copy_xf422_rgb_RGhA_neon_fp16"
+ "vt_Copy_xf422_rgb_b64a"
+ "vt_Copy_xf422_rgb_l10r"
+ "vt_Copy_xf422_rgb_l64r"
+ "vt_Copy_xf422_rgb_v216"
+ "vt_Copy_xf422_rgb_xf420"
+ "vt_Copy_xf422_rgb_xf420_neon_fp16"
+ "vt_Copy_xf422_rgb_xf422"
+ "vt_Copy_xf422_rgb_xf422_neon_fp16"
+ "vt_Copy_xf422_rgb_xf444"
+ "vt_Copy_xf422_rgb_xf444_neon_fp16"
+ "vt_Copy_xf422_rgb_yuvsf"
+ "vt_Copy_xf444_TRC_Mat_TRC_2vuyf"
+ "vt_Copy_xf444_TRC_Mat_TRC_420vf"
+ "vt_Copy_xf444_TRC_Mat_TRC_420vf_neon_fp16"
+ "vt_Copy_xf444_TRC_Mat_TRC_422vf"
+ "vt_Copy_xf444_TRC_Mat_TRC_422vf_neon_fp16"
+ "vt_Copy_xf444_TRC_Mat_TRC_444vf"
+ "vt_Copy_xf444_TRC_Mat_TRC_444vf_neon_fp16"
+ "vt_Copy_xf444_TRC_Mat_TRC_BGRA"
+ "vt_Copy_xf444_TRC_Mat_TRC_BGRA_neon_fp16"
+ "vt_Copy_xf444_TRC_Mat_TRC_RGfA"
+ "vt_Copy_xf444_TRC_Mat_TRC_RGfA_neon_fp16"
+ "vt_Copy_xf444_TRC_Mat_TRC_RGhA"
+ "vt_Copy_xf444_TRC_Mat_TRC_RGhA_neon_fp16"
+ "vt_Copy_xf444_TRC_Mat_TRC_b64a"
+ "vt_Copy_xf444_TRC_Mat_TRC_l10r"
+ "vt_Copy_xf444_TRC_Mat_TRC_l64r"
+ "vt_Copy_xf444_TRC_Mat_TRC_v216"
+ "vt_Copy_xf444_TRC_Mat_TRC_xf420"
+ "vt_Copy_xf444_TRC_Mat_TRC_xf420_neon_fp16"
+ "vt_Copy_xf444_TRC_Mat_TRC_xf422"
+ "vt_Copy_xf444_TRC_Mat_TRC_xf422_neon_fp16"
+ "vt_Copy_xf444_TRC_Mat_TRC_xf444"
+ "vt_Copy_xf444_TRC_Mat_TRC_xf444_neon_fp16"
+ "vt_Copy_xf444_TRC_Mat_TRC_yuvsf"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_2vuyf"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_420vf"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_420vf_neon_fp16"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_422vf"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_422vf_neon_fp16"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_444vf"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_444vf_neon_fp16"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_BGRA"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_BGRA_neon_fp16"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_RGfA"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_RGfA_neon_fp16"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_RGhA"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_RGhA_neon_fp16"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_b64a"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_l10r"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_l64r"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_v216"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_xf420"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_xf420_neon_fp16"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_xf422"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_xf422_neon_fp16"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_xf444"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_xf444_neon_fp16"
+ "vt_Copy_xf444_TRC_Tone_Mat_TRC_yuvsf"
+ "vt_Copy_xf444_rgb_2vuyf"
+ "vt_Copy_xf444_rgb_420vf"
+ "vt_Copy_xf444_rgb_420vf_neon_fp16"
+ "vt_Copy_xf444_rgb_422vf"
+ "vt_Copy_xf444_rgb_422vf_neon_fp16"
+ "vt_Copy_xf444_rgb_444vf"
+ "vt_Copy_xf444_rgb_444vf_neon_fp16"
+ "vt_Copy_xf444_rgb_BGRA"
+ "vt_Copy_xf444_rgb_BGRA_neon_fp16"
+ "vt_Copy_xf444_rgb_RGfA"
+ "vt_Copy_xf444_rgb_RGfA_neon_fp16"
+ "vt_Copy_xf444_rgb_RGhA"
+ "vt_Copy_xf444_rgb_RGhA_neon_fp16"
+ "vt_Copy_xf444_rgb_b64a"
+ "vt_Copy_xf444_rgb_l10r"
+ "vt_Copy_xf444_rgb_l64r"
+ "vt_Copy_xf444_rgb_v216"
+ "vt_Copy_xf444_rgb_xf420"
+ "vt_Copy_xf444_rgb_xf420_neon_fp16"
+ "vt_Copy_xf444_rgb_xf422"
+ "vt_Copy_xf444_rgb_xf422_neon_fp16"
+ "vt_Copy_xf444_rgb_xf444"
+ "vt_Copy_xf444_rgb_xf444_neon_fp16"
+ "vt_Copy_xf444_rgb_yuvsf"
+ "vt_Copy_xf44_2vuy"
+ "vt_Copy_xf44_420f"
+ "vt_Copy_xf44_420v"
+ "vt_Copy_xf44_422f"
+ "vt_Copy_xf44_422v"
+ "vt_Copy_xf44_444f"
+ "vt_Copy_xf44_444v"
+ "vt_Copy_xf44_f420"
+ "vt_Copy_xf44_s2as"
+ "vt_Copy_xf44_s4as"
+ "vt_Copy_xf44_sf20"
+ "vt_Copy_xf44_sf22"
+ "vt_Copy_xf44_sf44"
+ "vt_Copy_xf44_sv20"
+ "vt_Copy_xf44_sv22"
+ "vt_Copy_xf44_sv44"
+ "vt_Copy_xf44_t2as"
+ "vt_Copy_xf44_t4as"
+ "vt_Copy_xf44_tf20"
+ "vt_Copy_xf44_tf22"
+ "vt_Copy_xf44_tf44"
+ "vt_Copy_xf44_tv20"
+ "vt_Copy_xf44_tv22"
+ "vt_Copy_xf44_tv44"
+ "vt_Copy_xf44_v0a8"
+ "vt_Copy_xf44_v216"
+ "vt_Copy_xf44_v2a8"
+ "vt_Copy_xf44_v4a8"
+ "vt_Copy_xf44_x2as"
+ "vt_Copy_xf44_x420"
+ "vt_Copy_xf44_x422"
+ "vt_Copy_xf44_x444"
+ "vt_Copy_xf44_x4as"
+ "vt_Copy_xf44_xf20"
+ "vt_Copy_xf44_xf22"
+ "vt_Copy_xf44_y408"
+ "vt_Copy_xf44_y416"
+ "vt_Copy_xf44_y420"
+ "vt_Copy_y408_420f"
+ "vt_Copy_y408_420v"
+ "vt_Copy_y408_422f"
+ "vt_Copy_y408_422v"
+ "vt_Copy_y408_444f"
+ "vt_Copy_y408_444v"
+ "vt_Copy_y408_f420"
+ "vt_Copy_y408_s2as"
+ "vt_Copy_y408_s4as"
+ "vt_Copy_y408_sf20"
+ "vt_Copy_y408_sf22"
+ "vt_Copy_y408_sf44"
+ "vt_Copy_y408_sv20"
+ "vt_Copy_y408_sv22"
+ "vt_Copy_y408_sv44"
+ "vt_Copy_y408_t2as"
+ "vt_Copy_y408_t4as"
+ "vt_Copy_y408_tf20"
+ "vt_Copy_y408_tf22"
+ "vt_Copy_y408_tf44"
+ "vt_Copy_y408_tv20"
+ "vt_Copy_y408_tv22"
+ "vt_Copy_y408_tv44"
+ "vt_Copy_y408_v0a8"
+ "vt_Copy_y408_v2a8"
+ "vt_Copy_y408_v4a8"
+ "vt_Copy_y408_x2as"
+ "vt_Copy_y408_x420"
+ "vt_Copy_y408_x422"
+ "vt_Copy_y408_x444"
+ "vt_Copy_y408_x4as"
+ "vt_Copy_y408_xf20"
+ "vt_Copy_y408_xf22"
+ "vt_Copy_y408_xf44"
+ "vt_Copy_y408_y420"
+ "vt_Copy_y416_420f"
+ "vt_Copy_y416_420v"
+ "vt_Copy_y416_422f"
+ "vt_Copy_y416_422v"
+ "vt_Copy_y416_444f"
+ "vt_Copy_y416_444v"
+ "vt_Copy_y416_f420"
+ "vt_Copy_y416_s2as"
+ "vt_Copy_y416_s4as"
+ "vt_Copy_y416_sf20"
+ "vt_Copy_y416_sf22"
+ "vt_Copy_y416_sf44"
+ "vt_Copy_y416_sv20"
+ "vt_Copy_y416_sv22"
+ "vt_Copy_y416_sv44"
+ "vt_Copy_y416_t2as"
+ "vt_Copy_y416_t4as"
+ "vt_Copy_y416_tf20"
+ "vt_Copy_y416_tf22"
+ "vt_Copy_y416_tf44"
+ "vt_Copy_y416_tv20"
+ "vt_Copy_y416_tv22"
+ "vt_Copy_y416_tv44"
+ "vt_Copy_y416_v0a8"
+ "vt_Copy_y416_v2a8"
+ "vt_Copy_y416_v4a8"
+ "vt_Copy_y416_x2as"
+ "vt_Copy_y416_x420"
+ "vt_Copy_y416_x422"
+ "vt_Copy_y416_x444"
+ "vt_Copy_y416_x4as"
+ "vt_Copy_y416_xf20"
+ "vt_Copy_y416_xf22"
+ "vt_Copy_y416_xf44"
+ "vt_Copy_y416_y420"
+ "vt_Copy_y420"
+ "vt_Copy_y420ITU2020_32ARGB_vec"
+ "vt_Copy_y420ITU2020_32BGRA_vec"
+ "vt_Copy_y420ITU601_32ARGB_vec"
+ "vt_Copy_y420ITU601_32BGRA_vec"
+ "vt_Copy_y420ITU709_32ARGB_vec"
+ "vt_Copy_y420ITU709_32BGRA_vec"
+ "vt_Copy_y420_2vuy"
+ "vt_Copy_y420_420f"
+ "vt_Copy_y420_420v"
+ "vt_Copy_y420_444v"
+ "vt_Copy_y420_Crop"
+ "vt_Copy_y420_x422"
+ "vt_Copy_y420_xf22"
+ "vt_Copy_y420_yuvs"
+ "vt_Copy_yuvf_420v"
+ "vt_Copy_yuvsITU2020_24RGB"
+ "vt_Copy_yuvsITU2020_32ARGB"
+ "vt_Copy_yuvsITU2020_32BGRA"
+ "vt_Copy_yuvsITU2020_8GRAYSCALE"
+ "vt_Copy_yuvsITU601_24RGB"
+ "vt_Copy_yuvsITU601_32ARGB"
+ "vt_Copy_yuvsITU601_32BGRA"
+ "vt_Copy_yuvsITU601_8GRAYSCALE"
+ "vt_Copy_yuvsITU709_24RGB"
+ "vt_Copy_yuvsITU709_32ARGB"
+ "vt_Copy_yuvsITU709_32BGRA"
+ "vt_Copy_yuvsITU709_8GRAYSCALE"
+ "vt_Copy_yuvs_2vuy"
+ "vt_Copy_yuvs_2vuy_vec"
+ "vt_Copy_yuvs_420f"
+ "vt_Copy_yuvs_420v"
+ "vt_Copy_yuvs_420v_vec"
+ "vt_Copy_yuvs_y420"
+ "vt_Flip_16_Hor"
+ "vt_Flip_16_Ver"
+ "vt_Flip_2vuy_Hor"
+ "vt_Flip_2vuy_Ver"
+ "vt_Flip_32_Hor"
+ "vt_Flip_32_Ver"
+ "vt_Flip_420v_Hor"
+ "vt_Flip_420v_Ver"
+ "vt_Flip_64_Hor"
+ "vt_Flip_64_Ver"
+ "vt_Flip_8_Hor"
+ "vt_Flip_8_Ver"
+ "vt_Flip_b3a8_Hor"
+ "vt_Flip_b3a8_Ver"
+ "vt_Flip_v216_Hor"
+ "vt_Flip_v216_Ver"
+ "vt_Flip_x420_Hor"
+ "vt_Flip_x420_Ver"
+ "vt_Flip_y420_Hor"
+ "vt_Flip_y420_Ver"
+ "vt_Flip_yuvs_Hor"
+ "vt_Flip_yuvs_Ver"
+ "vt_Rotate_16_180"
+ "vt_Rotate_16_90CCW"
+ "vt_Rotate_16_90CW"
+ "vt_Rotate_2vuy_180"
+ "vt_Rotate_2vuy_90CCW"
+ "vt_Rotate_2vuy_90CW"
+ "vt_Rotate_32_180"
+ "vt_Rotate_32_90CCW"
+ "vt_Rotate_32_90CW"
+ "vt_Rotate_420v"
+ "vt_Rotate_420v_180"
+ "vt_Rotate_420v_90CCW"
+ "vt_Rotate_420v_90CW"
+ "vt_Rotate_64_180"
+ "vt_Rotate_64_90CCW"
+ "vt_Rotate_64_90CW"
+ "vt_Rotate_8"
+ "vt_Rotate_8_180"
+ "vt_Rotate_8_90CCW"
+ "vt_Rotate_8_90CW"
+ "vt_Rotate_b3a8_180"
+ "vt_Rotate_b3a8_90CCW"
+ "vt_Rotate_b3a8_90CW"
+ "vt_Rotate_v216_180"
+ "vt_Rotate_v216_90CCW"
+ "vt_Rotate_v216_90CW"
+ "vt_Rotate_x420"
+ "vt_Rotate_x420_180"
+ "vt_Rotate_x420_90CCW"
+ "vt_Rotate_x420_90CW"
+ "vt_Rotate_y420"
+ "vt_Rotate_y420_180"
+ "vt_Rotate_y420_90CCW"
+ "vt_Rotate_y420_90CW"
+ "vt_Rotate_yuvs_180"
+ "vt_Rotate_yuvs_90CCW"
+ "vt_Rotate_yuvs_90CW"
+ "vt_Scale_101010_Together"
+ "vt_Scale_16ARGB_Together"
+ "vt_Scale_16_SeparatePlanes"
+ "vt_Scale_16_Y_and_UVPlanes"
+ "vt_Scale_8ARGB_Together"
+ "vt_Scale_8_SeparatePlanes"
+ "vt_Scale_8_Y_and_UVPlanes"
+ "vt_Scale_HalfFloatRGBA_Together"
+ "vt_Scale_HalfFloat_Y_and_UVPlanes"
+ "vt_Scale_L008"
+ "vt_Scale_L00f"
+ "vt_Scale_L00h"
+ "vt_Scale_L016"
+ "vt_Scale_floatARGB_Together"
+ "vt_VImage_Copy#_2vuf_32ARGB"
+ "vt_VImage_Copy#_2vuf_32BGRA"
+ "vt_VImage_Copy#_2vuy_32ARGB"
+ "vt_VImage_Copy#_2vuy_32BGRA"
+ "vt_VImage_Copy#_32ARGB_2vuf"
+ "vt_VImage_Copy#_32ARGB_2vuy"
+ "vt_VImage_Copy#_32ARGB_32BGRA"
+ "vt_VImage_Copy#_32ARGB_420f"
+ "vt_VImage_Copy#_32ARGB_420v"
+ "vt_VImage_Copy#_32ARGB_R10k"
+ "vt_VImage_Copy#_32ARGB_RGhA"
+ "vt_VImage_Copy#_32ARGB_f420"
+ "vt_VImage_Copy#_32ARGB_v210"
+ "vt_VImage_Copy#_32ARGB_v216"
+ "vt_VImage_Copy#_32ARGB_v410"
+ "vt_VImage_Copy#_32ARGB_xw20"
+ "vt_VImage_Copy#_32ARGB_xw22"
+ "vt_VImage_Copy#_32ARGB_xw44"
+ "vt_VImage_Copy#_32ARGB_y408"
+ "vt_VImage_Copy#_32ARGB_y416"
+ "vt_VImage_Copy#_32ARGB_y420"
+ "vt_VImage_Copy#_32ARGB_yuvf"
+ "vt_VImage_Copy#_32ARGB_yuvs"
+ "vt_VImage_Copy#_32BGRA_2vuf"
+ "vt_VImage_Copy#_32BGRA_2vuy"
+ "vt_VImage_Copy#_32BGRA_32ARGB"
+ "vt_VImage_Copy#_32BGRA_420f"
+ "vt_VImage_Copy#_32BGRA_420v"
+ "vt_VImage_Copy#_32BGRA_R10k"
+ "vt_VImage_Copy#_32BGRA_RGhA"
+ "vt_VImage_Copy#_32BGRA_f420"
+ "vt_VImage_Copy#_32BGRA_v0a8"
+ "vt_VImage_Copy#_32BGRA_v210"
+ "vt_VImage_Copy#_32BGRA_v216"
+ "vt_VImage_Copy#_32BGRA_v410"
+ "vt_VImage_Copy#_32BGRA_xw20"
+ "vt_VImage_Copy#_32BGRA_xw22"
+ "vt_VImage_Copy#_32BGRA_xw44"
+ "vt_VImage_Copy#_32BGRA_y408"
+ "vt_VImage_Copy#_32BGRA_y416"
+ "vt_VImage_Copy#_32BGRA_y420"
+ "vt_VImage_Copy#_32BGRA_yuvf"
+ "vt_VImage_Copy#_32BGRA_yuvs"
+ "vt_VImage_Copy#_420f_32ARGB"
+ "vt_VImage_Copy#_420f_32BGRA"
+ "vt_VImage_Copy#_420v_32ARGB"
+ "vt_VImage_Copy#_420v_32BGRA"
+ "vt_VImage_Copy#_L008_L016"
+ "vt_VImage_Copy#_L016_L008"
+ "vt_VImage_Copy#_L565_1555"
+ "vt_VImage_Copy#_L565_32ARGB"
+ "vt_VImage_Copy#_L565_32BGRA"
+ "vt_VImage_Copy#_L565_5551"
+ "vt_VImage_Copy#_OneComponent_32BGRA"
+ "vt_VImage_Copy#_R10k_32ARGB"
+ "vt_VImage_Copy#_R10k_32BGRA"
+ "vt_VImage_Copy#_R10k_RGhA"
+ "vt_VImage_Copy#_RGfA_32ARGB"
+ "vt_VImage_Copy#_RGfA_32BGRA"
+ "vt_VImage_Copy#_RGfA_RGhA"
+ "vt_VImage_Copy#_RGhA_32ARGB"
+ "vt_VImage_Copy#_RGhA_32BGRA"
+ "vt_VImage_Copy#_RGhA_R10k"
+ "vt_VImage_Copy#_RGhA_RGfA"
+ "vt_VImage_Copy#_RGhA_l64r"
+ "vt_VImage_Copy#_RGhA_v210"
+ "vt_VImage_Copy#_RGhA_v216"
+ "vt_VImage_Copy#_RGhA_v410"
+ "vt_VImage_Copy#_RGhA_y416"
+ "vt_VImage_Copy#_f420_32ARGB"
+ "vt_VImage_Copy#_f420_32BGRA"
+ "vt_VImage_Copy#_l64r_RGhA"
+ "vt_VImage_Copy#_l64r_v216"
+ "vt_VImage_Copy#_l64r_v410"
+ "vt_VImage_Copy#_l64r_y416"
+ "vt_VImage_Copy#_v210_32ARGB"
+ "vt_VImage_Copy#_v210_32BGRA"
+ "vt_VImage_Copy#_v210_RGhA"
+ "vt_VImage_Copy#_v216_32ARGB"
+ "vt_VImage_Copy#_v216_32BGRA"
+ "vt_VImage_Copy#_v216_RGhA"
+ "vt_VImage_Copy#_v216_l64r"
+ "vt_VImage_Copy#_v410_32ARGB"
+ "vt_VImage_Copy#_v410_32BGRA"
+ "vt_VImage_Copy#_v410_RGhA"
+ "vt_VImage_Copy#_v410_l64r"
+ "vt_VImage_Copy#_w30r_x420"
+ "vt_VImage_Copy#_w30r_x422"
+ "vt_VImage_Copy#_w30r_x444"
+ "vt_VImage_Copy#_w30r_xf20"
+ "vt_VImage_Copy#_w30r_xf22"
+ "vt_VImage_Copy#_w30r_xf44"
+ "vt_VImage_Copy#_w30r_xw20"
+ "vt_VImage_Copy#_w30r_xw22"
+ "vt_VImage_Copy#_w30r_xw44"
+ "vt_VImage_Copy#_x420_w30r"
+ "vt_VImage_Copy#_x422_w30r"
+ "vt_VImage_Copy#_x444_w30r"
+ "vt_VImage_Copy#_xf20_w30r"
+ "vt_VImage_Copy#_xf22_w30r"
+ "vt_VImage_Copy#_xf44_w30r"
+ "vt_VImage_Copy#_xw20_32ARGB"
+ "vt_VImage_Copy#_xw20_32BGRA"
+ "vt_VImage_Copy#_xw20_w30r"
+ "vt_VImage_Copy#_xw22_32ARGB"
+ "vt_VImage_Copy#_xw22_32BGRA"
+ "vt_VImage_Copy#_xw22_w30r"
+ "vt_VImage_Copy#_xw44_32ARGB"
+ "vt_VImage_Copy#_xw44_32BGRA"
+ "vt_VImage_Copy#_xw44_w30r"
+ "vt_VImage_Copy#_y408_32ARGB"
+ "vt_VImage_Copy#_y408_32BGRA"
+ "vt_VImage_Copy#_y408_y416"
+ "vt_VImage_Copy#_y416_32ARGB"
+ "vt_VImage_Copy#_y416_32BGRA"
+ "vt_VImage_Copy#_y416_RGhA"
+ "vt_VImage_Copy#_y416_l64r"
+ "vt_VImage_Copy#_y416_y408"
+ "vt_VImage_Copy#_y420_32ARGB"
+ "vt_VImage_Copy#_y420_32BGRA"
+ "vt_VImage_Copy#_yuvf_32ARGB"
+ "vt_VImage_Copy#_yuvf_32BGRA"
+ "vt_VImage_Copy#_yuvs_32ARGB"
+ "vt_VImage_Copy#_yuvs_32BGRA"
+ "vt_VImage_Copy_32ARGB_b3a8"
+ "vt_VImage_Copy_32ARGB_w30r"
+ "vt_VImage_Copy_32BGRA_b3a8"
+ "vt_VImage_Copy_32BGRA_w30r"
+ "vt_VImage_Copy_420f_32ARGB"
+ "vt_VImage_Copy_420f_32BGRA"
+ "vt_VImage_Copy_420v_32ARGB"
+ "vt_VImage_Copy_420v_32BGRA"
+ "vt_VImage_Copy_RGfA_b3a8"
+ "vt_VImage_Copy_RGfA_w30r"
+ "vt_VImage_Copy_b3a8_32ARGB"
+ "vt_VImage_Copy_b3a8_32BGRA"
+ "vt_VImage_Copy_b3a8_RGfA"
+ "vt_VImage_Copy_b3a8_RGhA"
+ "vt_VImage_Copy_b3a8_l64r"
+ "vt_VImage_Copy_l64r_b3a8"
+ "vt_VImage_Copy_l64r_w30r"
+ "vt_VImage_Copy_w30r_32ARGB"
+ "vt_VImage_Copy_w30r_32BGRA"
+ "vt_VImage_Copy_w30r_RGfA"
+ "vt_VImage_Copy_w30r_RGhA"
+ "vt_VImage_Copy_w30r_l64r"
+ "vt_VImage_Setup_2vuf_32ARGB"
+ "vt_VImage_Setup_2vuf_32BGRA"
+ "vt_VImage_Setup_2vuy_32ARGB"
+ "vt_VImage_Setup_2vuy_32BGRA"
+ "vt_VImage_Setup_32ARGB_2vuf"
+ "vt_VImage_Setup_32ARGB_2vuy"
+ "vt_VImage_Setup_32ARGB_32BGRA"
+ "vt_VImage_Setup_32ARGB_420f"
+ "vt_VImage_Setup_32ARGB_420v"
+ "vt_VImage_Setup_32ARGB_R10k"
+ "vt_VImage_Setup_32ARGB_RGhA"
+ "vt_VImage_Setup_32ARGB_f420"
+ "vt_VImage_Setup_32ARGB_v210"
+ "vt_VImage_Setup_32ARGB_v216"
+ "vt_VImage_Setup_32ARGB_v410"
+ "vt_VImage_Setup_32ARGB_y408"
+ "vt_VImage_Setup_32ARGB_y416"
+ "vt_VImage_Setup_32ARGB_y420"
+ "vt_VImage_Setup_32ARGB_yuvf"
+ "vt_VImage_Setup_32ARGB_yuvs"
+ "vt_VImage_Setup_32BGRA_2vuf"
+ "vt_VImage_Setup_32BGRA_2vuy"
+ "vt_VImage_Setup_32BGRA_32ARGB"
+ "vt_VImage_Setup_32BGRA_420f"
+ "vt_VImage_Setup_32BGRA_420v"
+ "vt_VImage_Setup_32BGRA_R10k"
+ "vt_VImage_Setup_32BGRA_RGhA"
+ "vt_VImage_Setup_32BGRA_f420"
+ "vt_VImage_Setup_32BGRA_v0a8"
+ "vt_VImage_Setup_32BGRA_v210"
+ "vt_VImage_Setup_32BGRA_v216"
+ "vt_VImage_Setup_32BGRA_v410"
+ "vt_VImage_Setup_32BGRA_xw20"
+ "vt_VImage_Setup_32BGRA_xw22"
+ "vt_VImage_Setup_32BGRA_xw44"
+ "vt_VImage_Setup_32BGRA_y408"
+ "vt_VImage_Setup_32BGRA_y416"
+ "vt_VImage_Setup_32BGRA_y420"
+ "vt_VImage_Setup_32BGRA_yuvf"
+ "vt_VImage_Setup_32BGRA_yuvs"
+ "vt_VImage_Setup_420f_32ARGB"
+ "vt_VImage_Setup_420f_32BGRA"
+ "vt_VImage_Setup_420v_32ARGB"
+ "vt_VImage_Setup_420v_32BGRA"
+ "vt_VImage_Setup_L008_L016"
+ "vt_VImage_Setup_L016_L008"
+ "vt_VImage_Setup_L565_1555"
+ "vt_VImage_Setup_L565_32ARGB"
+ "vt_VImage_Setup_L565_32BGRA"
+ "vt_VImage_Setup_L565_5551"
+ "vt_VImage_Setup_OneComponent_32BGRA"
+ "vt_VImage_Setup_R10k_32ARGB"
+ "vt_VImage_Setup_R10k_32BGRA"
+ "vt_VImage_Setup_R10k_RGhA"
+ "vt_VImage_Setup_RGfA_32ARGB"
+ "vt_VImage_Setup_RGfA_32BGRA"
+ "vt_VImage_Setup_RGfA_RGhA"
+ "vt_VImage_Setup_RGhA_32ARGB"
+ "vt_VImage_Setup_RGhA_32BGRA"
+ "vt_VImage_Setup_RGhA_R10k"
+ "vt_VImage_Setup_RGhA_RGfA"
+ "vt_VImage_Setup_RGhA_l64r"
+ "vt_VImage_Setup_RGhA_v210"
+ "vt_VImage_Setup_RGhA_v216"
+ "vt_VImage_Setup_RGhA_v410"
+ "vt_VImage_Setup_RGhA_y416"
+ "vt_VImage_Setup_f420_32ARGB"
+ "vt_VImage_Setup_f420_32BGRA"
+ "vt_VImage_Setup_l64r_RGhA"
+ "vt_VImage_Setup_l64r_v216"
+ "vt_VImage_Setup_l64r_v410"
+ "vt_VImage_Setup_l64r_y416"
+ "vt_VImage_Setup_v210_32ARGB"
+ "vt_VImage_Setup_v210_32BGRA"
+ "vt_VImage_Setup_v210_RGhA"
+ "vt_VImage_Setup_v216_32ARGB"
+ "vt_VImage_Setup_v216_32BGRA"
+ "vt_VImage_Setup_v216_RGhA"
+ "vt_VImage_Setup_v216_l64r"
+ "vt_VImage_Setup_v410_32ARGB"
+ "vt_VImage_Setup_v410_32BGRA"
+ "vt_VImage_Setup_v410_RGhA"
+ "vt_VImage_Setup_v410_l64r"
+ "vt_VImage_Setup_w30r_x420"
+ "vt_VImage_Setup_w30r_x422"
+ "vt_VImage_Setup_w30r_x444"
+ "vt_VImage_Setup_w30r_xf20"
+ "vt_VImage_Setup_w30r_xf22"
+ "vt_VImage_Setup_w30r_xf44"
+ "vt_VImage_Setup_w30r_xw20"
+ "vt_VImage_Setup_w30r_xw22"
+ "vt_VImage_Setup_w30r_xw44"
+ "vt_VImage_Setup_x420_w30r"
+ "vt_VImage_Setup_x422_w30r"
+ "vt_VImage_Setup_x444_w30r"
+ "vt_VImage_Setup_xf20_w30r"
+ "vt_VImage_Setup_xf22_w30r"
+ "vt_VImage_Setup_xf44_w30r"
+ "vt_VImage_Setup_xw20_32ARGB"
+ "vt_VImage_Setup_xw20_32BGRA"
+ "vt_VImage_Setup_xw20_w30r"
+ "vt_VImage_Setup_xw22_32ARGB"
+ "vt_VImage_Setup_xw22_32BGRA"
+ "vt_VImage_Setup_xw22_w30r"
+ "vt_VImage_Setup_xw44_32ARGB"
+ "vt_VImage_Setup_xw44_32BGRA"
+ "vt_VImage_Setup_xw44_w30r"
+ "vt_VImage_Setup_y408_32ARGB"
+ "vt_VImage_Setup_y408_32BGRA"
+ "vt_VImage_Setup_y408_y416"
+ "vt_VImage_Setup_y416_32ARGB"
+ "vt_VImage_Setup_y416_32BGRA"
+ "vt_VImage_Setup_y416_RGhA"
+ "vt_VImage_Setup_y416_l64r"
+ "vt_VImage_Setup_y416_y408"
+ "vt_VImage_Setup_y420_32BGRA"
+ "vt_VImage_Setup_yuvf_32ARGB"
+ "vt_VImage_Setup_yuvf_32BGRA"
+ "vt_VImage_Setup_yuvs_32ARGB"
+ "vt_VImage_Setup_yuvs_32BGRA"
+ "vt_checkCMSessionIsSupported"
+ "vtcg_convertPixelBuffer"
+ "vtcg_createCGCompatiblePixelBuffer"
+ "vtcg_createCGImageWithProvider"
+ "vtcg_createDeferredImageProviderWithIOSurface"
+ "vtcg_createDeferredImageProviderWithPixelBuffer"
+ "vtcg_createPixelBufferAttributesWithIOSurfaceSupport"
+ "vtcs_trace"
+ "vtcsr_Finalize"
+ "vtcsr_dequeueAllPendingFramesAndCallbackClientForEach"
+ "vtcsr_dequeueAllPendingFramesAndCallbackClientForEach_block_invoke"
+ "vtcsr_handleDeadServerConnection"
+ "vtcsr_handleDeadServerConnection_block_invoke"
+ "vtcsr_handleMachErrorsInternal"
+ "vtcsr_postNotificationWithPayload"
+ "vtcss_appStateChangeListener"
+ "vtcss_appStateChangeListener_block_invoke"
+ "vtcss_enqueueFrame"
+ "vtcss_initializeClient"
+ "vtcsserver_dynamicbackgroundmemory"
+ "vtds_trace"
+ "vtdsr_Finalize"
+ "vtdsr_dequeueAllPendingFramesAndCallbackClientForEach"
+ "vtdsr_dequeueAllPendingFramesAndCallbackClientForEach_block_invoke"
+ "vtdsr_dequeueNextPendingFrameAndCallbackClient_block_invoke"
+ "vtdsr_handleDeadServerConnection"
+ "vtdsr_handleDeadServerConnection_block_invoke_2"
+ "vtdsr_postNotificationWithPayload"
+ "vtdsrb_Finalize"
+ "vtdss_TileStatisticsLogAndInvalidate"
+ "vtdss_TileStatisticsLogAndReset"
+ "vtdss_appStateChangeListener"
+ "vtdss_enqueueFrame"
+ "vtdss_enqueueFrame_block_invoke"
+ "vtdss_enqueueTaggedBufferGroup"
+ "vtdss_initializeClient"
+ "vtfigaudiosession_trace"
+ "vtfp_mctf_trace"
+ "vtframeprocessor-queue-%p"
+ "vthisgsInitializeHistogramMPS"
+ "vthisgsValidateFrameworkMPS"
+ "vtioregistrykeyservice_trace"
+ "vtmsSetupDebayerPassForStage"
+ "vtmtsAppendCompositePass"
+ "vtmtsBuildSource did not append texture descriptions"
+ "vtmtsCreateComputeStateFromDescription"
+ "vtmtsCreateRenderStateFromDescription"
+ "vtmtsGetAlphaPlaneIndexWithPixelFormat"
+ "vtmtsSetUpProcessingNeeds"
+ "vtmtsSetupMetalDirectBlitter"
+ "vtmtsSetupMetalObjects"
+ "vtmtsSetupRenderOperationsForFunctionConstant"
+ "vtpixelbufferconformer_trace"
+ "vtpools_trace"
+ "vtpvScanForParameterBoxWithType"
+ "vtpvScanForTopLevelBoxWithType"
+ "vtrbs_trace"
+ "vtrestrictions_trace"
+ "vttiledecompression_trace"
+ "vtvideodecodercapabilites_trace"
+ "waitUntilSignaledValue:timeoutMS:"
+ "we didn't find anything matching hostProcessID"
+ "we expect to use the semaphore for back pressure"
+ "weakReferenceTable_AddPointerAndGetKey"
+ "weakReferenceTable_CopyPointerFromKey"
+ "weakReferenceTable_OneTimeInitialization failed"
+ "weakReferenceTable_RemovePointer"
+ "width * height > 1 Gibipixel"
+ "width <= 0 || height <= 0"
+ "width mismatch"
+ "width must be greater than 0"
+ "wrapped decoder ID missing from matchInfo"
+ "wrapped encoder ID missing from matchInfo"
+ "wrong height"
+ "wrong width"
+ "zero pixel format type"
+ "zone"
+ "{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}"
+ "{?=ii}16@0:8"
+ "{?=qiIq}16@0:8"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "<<<< ParavirtualizedVideoDecoder >>>> %s: (decoder %{public}@ decoderSession %p decompressionSession %{public}@ ) DecodeFrame failed with error %d, frame %p: sbuf PTS %1.3f, %zd bytes, decodeFlags 0x%x, frameOptions %@"
- "<<<< ParavirtualizedVideoDecoder >>>> %s: error %d in setting properties %@"
- "<<<< ParavirtualizedVideoDecoder >>>> %s: error %d in setting property %@ with value %@"
- "<<<< ParavirtualizedVideoDecoder >>>> %s: guest UUID %{private}@, codecType %c%c%c%c, decoderID %{private}@ externalProtectionStatus=%u"
- "<<<< ParavirtualizedVideoDecoder >>>> %s: guestProtocolVersion %u hostProtocolVersion %u hostInfo %{public}@, guestBuildVersion %{public}@"
- "<<<< ParavirtualizedVideoEncoder >>>> %s: (encoder %{public}@, encoderSession %p, compressionSession %{public}@) EncodeFrame failed with error %d, frame %p: pixelBuffer %p PTS %1.3f duration %1.3f frameProperties %{public}@"
- "<<<< ParavirtualizedVideoEncoder >>>> %s: -> %d"
- "<<<< ParavirtualizedVideoEncoder >>>> %s: GuestRemoveHandlerForUUID failed with error %d"
- "<<<< ParavirtualizedVideoEncoder >>>> %s: Sending the message '-enc' failed with error %d"
- "<<<< ParavirtualizedVideoEncoder >>>> %s: error %d in setting property %@ with value %@"
- "<<<< ParavirtualizedVideoEncoder >>>> %s: guest UUID %{private}@, codecType %c%c%c%c, encoderID %{private}@"
- "<<<< ParavirtualizedVideoEncoder >>>> %s: guestProtocolVersion %u hostProtocolVersion %u hostInfo %{public}@, guestBuildVersion %{public}@"
- "<<<< VTPixelTransferSession >>>> %s: (%p) Failed %s for '%c%c%c%c' (%d x %d) offset: (%d, %d) %s%s primaries:%@ transfer:%@ matrix:%@ icc:%p cgcolor:%p to '%c%c%c%c' (%d x %d) offset: (%d, %d) %s primaries:%@ transfer:%@ matrix:%@ icc:%p%s%s."
- "DecoderProducesRAWOutput"
- "FigFairPlayCPELimitedCryptorCreate"
- "FigPKDCPELimitedCryptorCreateWithExternalProtectionMethods"
- "FigPKDMSECPELimitedCryptorCreateWithExternalProtectionMethods"
- "GuestExternalProtectionStatus"
- "IsDRMSubstitute"
- "MediaExtensionCodecName"
- "MediaExtensionContainingBundleName"
- "MediaExtensionContainingBundleURL"
- "MediaExtensionIdentifier"
- "MediaExtensionName"
- "MediaExtensionURL"
- "Protected video was decoded successfully"
- "RecommendedParallelizationLimit"
- "RequestRAWOutput"
- "VTGuestExternalProtectionStatus"
- "[VTDecompressionSessionXPCRemote %p] [objId = %016llx] "
- "[VTPixelTransferNodeDynamic]"
- "description=CoreMedia_VideoToolbox-3225.7.1"
- "frameNumber: %5d"
- "in the host, then replaced with this"
- "paravirtualized:%@:%c%c%c%c"
- "unprotected blue frame in the guest."

```
