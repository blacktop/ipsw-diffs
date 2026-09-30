## AVFCapture

> `/System/Library/PrivateFrameworks/AVFCapture.framework/Versions/A/AVFCapture`

```diff

-  __TEXT.__text: 0x1f8c1c
-  __TEXT.__objc_methlist: 0x16454
-  __TEXT.__cstring: 0x39719
-  __TEXT.__const: 0x1342
-  __TEXT.__gcc_except_tab: 0x3688
-  __TEXT.__oslogstring: 0x2f751
+  __TEXT.__text: 0x1ffe04
+  __TEXT.__objc_methlist: 0x16a9c
+  __TEXT.__cstring: 0x41b59
+  __TEXT.__const: 0x1602
+  __TEXT.__gcc_except_tab: 0x3750
+  __TEXT.__oslogstring: 0x2fc5f
   __TEXT.__dlopen_cstrs: 0x275
   __TEXT.__ustring: 0x112
   __TEXT.__swift5_typeref: 0xef

   __TEXT.__swift5_reflstr: 0x24
   __TEXT.__swift5_fieldmd: 0x50
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x6ae0
+  __TEXT.__unwind_info: 0x6c68
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x17b8
-  __DATA_CONST.__objc_classlist: 0x920
+  __DATA_CONST.__const: 0x1818
+  __DATA_CONST.__objc_classlist: 0x950
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0xc8
+  __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9070
+  __DATA_CONST.__objc_selrefs: 0x9580
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x778
-  __DATA_CONST.__objc_arraydata: 0x2a8
-  __DATA_CONST.__got: 0x2ab8
-  __AUTH_CONST.__const: 0x3150
-  __AUTH_CONST.__cfstring: 0x16420
-  __AUTH_CONST.__objc_const: 0x23380
+  __DATA_CONST.__objc_superrefs: 0x7a8
+  __DATA_CONST.__objc_arraydata: 0x2b0
+  __DATA_CONST.__got: 0x2bd8
+  __AUTH_CONST.__const: 0x32e0
+  __AUTH_CONST.__cfstring: 0x16820
+  __AUTH_CONST.__objc_const: 0x24340
   __AUTH_CONST.__objc_intobj: 0xa50
-  __AUTH_CONST.__objc_arrayobj: 0x270
+  __AUTH_CONST.__objc_arrayobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x14d0
-  __AUTH.__objc_data: 0x26e0
+  __AUTH_CONST.__auth_got: 0x1528
+  __AUTH.__objc_data: 0x3d10
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x241c
-  __DATA.__data: 0xee0
-  __DATA.__bss: 0xa50
+  __DATA.__objc_ivar: 0x2538
+  __DATA.__data: 0xfa0
+  __DATA.__bss: 0xaa0
   __DATA.__common: 0x4e0
-  __DATA_DIRTY.__objc_data: 0x3480
+  __DATA_DIRTY.__objc_data: 0x2030
   __DATA_DIRTY.__data: 0x188
   __DATA_DIRTY.__common: 0x310
-  __DATA_DIRTY.__bss: 0x6b8
+  __DATA_DIRTY.__bss: 0x6dc
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVRouting.framework/Versions/A/AVRouting
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /System/Library/Frameworks/IOSurface.framework/Versions/A/IOSurface
   - /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
   - /System/Library/Frameworks/MediaToolbox.framework/Versions/A/MediaToolbox
+  - /System/Library/Frameworks/Metal.framework/Versions/A/Metal
   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10903
-  Symbols:   23428
-  CStrings:  9787
+  Functions: 11067
+  Symbols:   23944
+  CStrings:  9882
 
Sections:
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ +[AVCaptureVideoAnalyticsAdaptor defaultCommandQueue]
+ +[AVCaptureVideoAnalyticsAdaptor initialize]
+ +[AVCaptureVideoHistogramAnalyticsLayerAppearance _getLuminanceMatricesWithLineColors:fillStartColors:fillEndColors:]
+ +[AVCaptureVideoHistogramAnalyticsLayerAppearance _getRGBMatricesWithLineColors:fillStartColors:fillEndColors:]
+ +[AVCaptureVideoHistogramAnalyticsLayerAppearance _matrixFromDefault:disablingChannels:]
+ +[AVCaptureVideoHistogramAnalyticsLayerAppearance defaultLuminanceAppearance]
+ +[AVCaptureVideoHistogramAnalyticsLayerAppearance defaultRGBCompositeAppearance]
+ +[AVCaptureVideoHistogramAnalyticsLayerAppearance defaultRGBParadeAppearance]
+ +[AVCaptureVideoWaveformAnalyticsLayerAppearance _getLuminanceFillColors]
+ +[AVCaptureVideoWaveformAnalyticsLayerAppearance _getRGBFillColors]
+ +[AVCaptureVideoWaveformAnalyticsLayerAppearance _getYUVFillColors]
+ +[AVCaptureVideoWaveformAnalyticsLayerAppearance _matrixFromDefault:disablingChannels:]
+ +[AVCaptureVideoWaveformAnalyticsLayerAppearance defaultLuminanceAppearance]
+ +[AVCaptureVideoWaveformAnalyticsLayerAppearance defaultRGBCompositeAppearance]
+ +[AVCaptureVideoWaveformAnalyticsLayerAppearance defaultRGBParadeAppearance]
+ +[AVCaptureVideoWaveformAnalyticsLayerAppearance defaultYUVCompositeAppearance]
+ +[AVCaptureVideoWaveformAnalyticsLayerAppearance defaultYUVParadeAppearance]
+ +[AVProVideoStorage _replenishErrorForOSStatus:]
+ -[AVCaptureMetadataOutput handleChangedActiveFormat:forDevice:]
+ -[AVCapturePhotoSettings _setHighResolutionPhotoEnabled:]
+ -[AVCaptureVideoAnalyticsAdaptor _convertPixelBufferViaCoreImage:commandBuffer:]
+ -[AVCaptureVideoAnalyticsAdaptor _hasAttachedVideoDataOutput]
+ -[AVCaptureVideoAnalyticsAdaptor _processPixelBuffer:slotReleaseHandler:]
+ -[AVCaptureVideoAnalyticsAdaptor attachToRenderer:]
+ -[AVCaptureVideoAnalyticsAdaptor attachToVideoDataOutput:error:]
+ -[AVCaptureVideoAnalyticsAdaptor attachedVideoDataOutput]
+ -[AVCaptureVideoAnalyticsAdaptor captureOutput:didOutputSampleBuffer:fromConnection:]
+ -[AVCaptureVideoAnalyticsAdaptor dealloc]
+ -[AVCaptureVideoAnalyticsAdaptor detachFromRenderer:]
+ -[AVCaptureVideoAnalyticsAdaptor detachFromVideoDataOutput]
+ -[AVCaptureVideoAnalyticsAdaptor flushRemovingDisplayedImage:]
+ -[AVCaptureVideoAnalyticsAdaptor frameCount]
+ -[AVCaptureVideoAnalyticsAdaptor ingestCGImage:error:]
+ -[AVCaptureVideoAnalyticsAdaptor ingestPixelBuffer:attachments:error:]
+ -[AVCaptureVideoAnalyticsAdaptor ingestSampleBuffer:error:]
+ -[AVCaptureVideoAnalyticsAdaptor init]
+ -[AVCaptureVideoAnalyticsAdaptor isSuspended]
+ -[AVCaptureVideoAnalyticsAdaptor renderers]
+ -[AVCaptureVideoAnalyticsAdaptor resume]
+ -[AVCaptureVideoAnalyticsAdaptor setAttachedVideoDataOutput:]
+ -[AVCaptureVideoAnalyticsAdaptor setFrameCount:]
+ -[AVCaptureVideoAnalyticsAdaptor setRenderers:]
+ -[AVCaptureVideoAnalyticsAdaptor setSignpostLogger:]
+ -[AVCaptureVideoAnalyticsAdaptor setSuspended:]
+ -[AVCaptureVideoAnalyticsAdaptor signpostLogger]
+ -[AVCaptureVideoAnalyticsAdaptor suspend]
+ -[AVCaptureVideoAnalyticsAdaptor suspended]
+ -[AVCaptureVideoAnalyticsAdaptor videoDataOutput]
+ -[AVCaptureVideoHistogramAnalyticsLayer _computeHistogramFromTexture:]
+ -[AVCaptureVideoHistogramAnalyticsLayer _createGraphicsPipelinesWithBlendMode:]
+ -[AVCaptureVideoHistogramAnalyticsLayer _initializeHistogramTextures]
+ -[AVCaptureVideoHistogramAnalyticsLayer _initializeRenderingPipeline]
+ -[AVCaptureVideoHistogramAnalyticsLayer _renderCurrentFrameImmediate]
+ -[AVCaptureVideoHistogramAnalyticsLayer _renderFrameToUpdate:sourceTexture:]
+ -[AVCaptureVideoHistogramAnalyticsLayer _renderInterpolatedHistogramToDrawable:]
+ -[AVCaptureVideoHistogramAnalyticsLayer _renderInterpolatedHistogramWithBackPressureToDrawable:]
+ -[AVCaptureVideoHistogramAnalyticsLayer _renderInterpolatedHistogram]
+ -[AVCaptureVideoHistogramAnalyticsLayer _startDisplayLink]
+ -[AVCaptureVideoHistogramAnalyticsLayer _stopDisplayLink]
+ -[AVCaptureVideoHistogramAnalyticsLayer appearance]
+ -[AVCaptureVideoHistogramAnalyticsLayer dealloc]
+ -[AVCaptureVideoHistogramAnalyticsLayer init]
+ -[AVCaptureVideoHistogramAnalyticsLayer layoutSublayers]
+ -[AVCaptureVideoHistogramAnalyticsLayer metalDisplayLink:needsUpdate:]
+ -[AVCaptureVideoHistogramAnalyticsLayer renderWithSampleImage:commandBuffer:]
+ -[AVCaptureVideoHistogramAnalyticsLayer setAppearance:]
+ -[AVCaptureVideoHistogramAnalyticsLayer setSolidFillForChannel:color:]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance channelBlendMode]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance channelFillColorEnd]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance channelFillColorStart]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance channelFillGradientAngle]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance channelLineColor]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance channelLineThickness]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance copyWithZone:]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance initWithSubstrateColor:channelFillColorStart:channelFillColorEnd:channelLineColor:channelFillGradientAngle:channelLineThickness:channelBlendMode:isParade:numberOfBars:smoothness:]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance init]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance isParade]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance numberOfBars]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance setChannelBlendMode:]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance setChannelFillColorEnd:]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance setChannelFillColorStart:]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance setChannelFillGradientAngle:]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance setChannelLineColor:]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance setChannelLineThickness:]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance setIsParade:]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance setNumberOfBars:]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance setSmoothness:]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance setSubstrateColor:]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance smoothness]
+ -[AVCaptureVideoHistogramAnalyticsLayerAppearance substrateColor]
+ -[AVCaptureVideoWaveformAnalyticsLayer appearance]
+ -[AVCaptureVideoWaveformAnalyticsLayer dealloc]
+ -[AVCaptureVideoWaveformAnalyticsLayer init]
+ -[AVCaptureVideoWaveformAnalyticsLayer isMirrored]
+ -[AVCaptureVideoWaveformAnalyticsLayer layoutSublayers]
+ -[AVCaptureVideoWaveformAnalyticsLayer renderWithSampleImage:commandBuffer:]
+ -[AVCaptureVideoWaveformAnalyticsLayer setAppearance:]
+ -[AVCaptureVideoWaveformAnalyticsLayer setMirrored:]
+ -[AVCaptureVideoWaveformAnalyticsLayer setVideoRotationAngle:]
+ -[AVCaptureVideoWaveformAnalyticsLayer videoRotationAngle]
+ -[AVCaptureVideoWaveformAnalyticsLayerAppearance channelBlendMode]
+ -[AVCaptureVideoWaveformAnalyticsLayerAppearance channelFillColor]
+ -[AVCaptureVideoWaveformAnalyticsLayerAppearance copyWithZone:]
+ -[AVCaptureVideoWaveformAnalyticsLayerAppearance initWithSubstrateColor:channelFillColor:channelBlendMode:isParade:smoothness:]
+ -[AVCaptureVideoWaveformAnalyticsLayerAppearance init]
+ -[AVCaptureVideoWaveformAnalyticsLayerAppearance isParade]
+ -[AVCaptureVideoWaveformAnalyticsLayerAppearance setChannelBlendMode:]
+ -[AVCaptureVideoWaveformAnalyticsLayerAppearance setChannelFillColor:]
+ -[AVCaptureVideoWaveformAnalyticsLayerAppearance setIsParade:]
+ -[AVCaptureVideoWaveformAnalyticsLayerAppearance setSmoothness:]
+ -[AVCaptureVideoWaveformAnalyticsLayerAppearance setSubstrateColor:]
+ -[AVCaptureVideoWaveformAnalyticsLayerAppearance smoothness]
+ -[AVCaptureVideoWaveformAnalyticsLayerAppearance substrateColor]
+ -[AVProVideoStorage _attemptReplenishWithCapacity:attemptCount:]
+ -[AVProVideoStorage _finalizeReplenishWithError:]
+ -[AVProVideoStorage _isBusyForPropertyReads]
+ -[AVProVideoStorage _maximumCapacityComponentsIncludingPurgeableSpace:]
+ -[AVProVideoStorage _setCapacity:options:completion:]
+ -[AVProVideoStorage _updateBusyReasons:]
+ -[AVProVideoStorage busyReasons]
+ -[AVProVideoStorage maximumCapacityComponents]
+ -[AVProVideoStorage replenishCapacityWithCompletionHandler:]
+ -[AVProVideoStorageMaximumCapacityComponents initWithMaximumCapacity:purgeableSpace:]
+ -[AVProVideoStorageMaximumCapacityComponents maximumCapacity]
+ -[AVProVideoStorageMaximumCapacityComponents purgeableSpace]
+ -[AVProVideoStorageSetCapacityOptions replenishMode]
+ -[AVProVideoStorageSetCapacityOptions setReplenishMode:]
+ GCC_except_table112
+ OBJC_IVAR_$_AVCaptureVideoAnalyticsAdaptor._attachedVideoDataOutput
+ OBJC_IVAR_$_AVCaptureVideoAnalyticsAdaptor._cgImageRing
+ OBJC_IVAR_$_AVCaptureVideoAnalyticsAdaptor._cgImageRingHeights
+ OBJC_IVAR_$_AVCaptureVideoAnalyticsAdaptor._cgImageRingSemaphores
+ OBJC_IVAR_$_AVCaptureVideoAnalyticsAdaptor._cgImageRingWidths
+ OBJC_IVAR_$_AVCaptureVideoAnalyticsAdaptor._ciOutputRing
+ OBJC_IVAR_$_AVCaptureVideoAnalyticsAdaptor._ciOutputRingIndex
+ OBJC_IVAR_$_AVCaptureVideoAnalyticsAdaptor._ciOutputRingIndexLock
+ OBJC_IVAR_$_AVCaptureVideoAnalyticsAdaptor._ciOutputRingSemaphore
+ OBJC_IVAR_$_AVCaptureVideoAnalyticsAdaptor._frameCount
+ OBJC_IVAR_$_AVCaptureVideoAnalyticsAdaptor._inFlightFrameSemaphore
+ OBJC_IVAR_$_AVCaptureVideoAnalyticsAdaptor._renderers
+ OBJC_IVAR_$_AVCaptureVideoAnalyticsAdaptor._renderersLock
+ OBJC_IVAR_$_AVCaptureVideoAnalyticsAdaptor._sampleBufferQueue
+ OBJC_IVAR_$_AVCaptureVideoAnalyticsAdaptor._signpostLogger
+ OBJC_IVAR_$_AVCaptureVideoAnalyticsAdaptor._suspended
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._appearance
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._backPressureSemaphore
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._cachedThermalState
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._commandQueue
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._currentHistogramTexture
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._displayLink
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._displayScale
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._fragmentFunction
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._hasNewVideoFrame
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._histogramAccumulationBuffer
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._histogramComputePSO
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._histogramNormalizePSO
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._interpolationProgress
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._lastComputeTime
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._lastDrawableSize
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._lastSourceTexture
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._lastThermalStateCheck
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._previousHistogramTexture
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._renderPipelineStateFill
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._renderPipelineStateLine
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._shaderLibrary
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._startTime
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._vertexFunctionFill
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayer._vertexFunctionLine
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayerAppearance._channelBlendMode
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayerAppearance._channelFillColorEnd
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayerAppearance._channelFillColorStart
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayerAppearance._channelFillGradientAngle
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayerAppearance._channelLineColor
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayerAppearance._channelLineThickness
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayerAppearance._isParade
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayerAppearance._numberOfBars
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayerAppearance._smoothness
+ OBJC_IVAR_$_AVCaptureVideoHistogramAnalyticsLayerAppearance._substrateColor
+ OBJC_IVAR_$_AVCaptureVideoWaveformAnalyticsLayer._appearance
+ OBJC_IVAR_$_AVCaptureVideoWaveformAnalyticsLayer._appearanceLock
+ OBJC_IVAR_$_AVCaptureVideoWaveformAnalyticsLayer._displayScale
+ OBJC_IVAR_$_AVCaptureVideoWaveformAnalyticsLayer._filamentVertexBuffer
+ OBJC_IVAR_$_AVCaptureVideoWaveformAnalyticsLayer._filamentVertexCountBuffer
+ OBJC_IVAR_$_AVCaptureVideoWaveformAnalyticsLayer._indirectCommandBuffer
+ OBJC_IVAR_$_AVCaptureVideoWaveformAnalyticsLayer._lastDrawableSize
+ OBJC_IVAR_$_AVCaptureVideoWaveformAnalyticsLayer._mirrored
+ OBJC_IVAR_$_AVCaptureVideoWaveformAnalyticsLayer._precursorTexture
+ OBJC_IVAR_$_AVCaptureVideoWaveformAnalyticsLayer._videoRotationAngle
+ OBJC_IVAR_$_AVCaptureVideoWaveformAnalyticsLayerAppearance._channelBlendMode
+ OBJC_IVAR_$_AVCaptureVideoWaveformAnalyticsLayerAppearance._channelFillColor
+ OBJC_IVAR_$_AVCaptureVideoWaveformAnalyticsLayerAppearance._isParade
+ OBJC_IVAR_$_AVCaptureVideoWaveformAnalyticsLayerAppearance._smoothness
+ OBJC_IVAR_$_AVCaptureVideoWaveformAnalyticsLayerAppearance._substrateColor
+ OBJC_IVAR_$_AVProVideoStorage._busyReasons
+ OBJC_IVAR_$_AVProVideoStorage._pendingReplenishCompletion
+ OBJC_IVAR_$_AVProVideoStorage._replenishDecrementBytes
+ OBJC_IVAR_$_AVProVideoStorage._replenishMaxAttempts
+ OBJC_IVAR_$_AVProVideoStorageMaximumCapacityComponents._maximumCapacity
+ OBJC_IVAR_$_AVProVideoStorageMaximumCapacityComponents._purgeableSpace
+ OBJC_IVAR_$_AVProVideoStorageSetCapacityOptions._replenishMode
+ _AVGQIV52D6ZY6YNMNKTM3AFFHYPXPM
+ _AVProVideoStorageBusyReasonAdjustingCapacity
+ _AVProVideoStorageBusyReasonCapturing
+ _AVProVideoStorageBusyReasonReplenishing
+ _CVMetalTextureCacheCreate
+ _CVPixelBufferGetPlaneCount
+ _CVPixelBufferIsPlanar
+ _FigCFDictionaryGetInt32IfPresent
+ _FigCFNumberGetSInt32
+ _MTLCreateSystemDefaultDevice
+ _NSRunLoopCommonModes
+ _OBJC_CLASS_$_AVCaptureVideoAnalyticsAdaptor
+ _OBJC_CLASS_$_AVCaptureVideoHistogramAnalyticsLayer
+ _OBJC_CLASS_$_AVCaptureVideoHistogramAnalyticsLayerAppearance
+ _OBJC_CLASS_$_AVCaptureVideoWaveformAnalyticsLayer
+ _OBJC_CLASS_$_AVCaptureVideoWaveformAnalyticsLayerAppearance
+ _OBJC_CLASS_$_AVProVideoStorageMaximumCapacityComponents
+ _OBJC_CLASS_$_AVProVideoStorageSetCapacityOptions
+ _OBJC_CLASS_$_CAMetalDisplayLink
+ _OBJC_CLASS_$_CAMetalLayer
+ _OBJC_CLASS_$_CIContext
+ _OBJC_CLASS_$_MTLCompileOptions
+ _OBJC_CLASS_$_MTLIndirectCommandBufferDescriptor
+ _OBJC_CLASS_$_MTLRenderPassDescriptor
+ _OBJC_CLASS_$_MTLRenderPipelineDescriptor
+ _OBJC_CLASS_$_MTLTextureDescriptor
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_CLASS_$_NSRunLoop
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_METACLASS_$_AVCaptureVideoAnalyticsAdaptor
+ _OBJC_METACLASS_$_AVCaptureVideoHistogramAnalyticsLayer
+ _OBJC_METACLASS_$_AVCaptureVideoHistogramAnalyticsLayerAppearance
+ _OBJC_METACLASS_$_AVCaptureVideoWaveformAnalyticsLayer
+ _OBJC_METACLASS_$_AVCaptureVideoWaveformAnalyticsLayerAppearance
+ _OBJC_METACLASS_$_AVProVideoStorageMaximumCapacityComponents
+ _OBJC_METACLASS_$_AVProVideoStorageSetCapacityOptions
+ _OBJC_METACLASS_$_CAMetalLayer
+ _PromotedConst
+ __39-[AVProVideoStorage _reconnectToServer]_block_invoke
+ __96-[AVCaptureVideoHistogramAnalyticsLayer _renderInterpolatedHistogramWithBackPressureToDrawable:]_block_invoke
+ __OBJC_$_CLASS_METHODS_AVCaptureVideoAnalyticsAdaptor
+ __OBJC_$_CLASS_METHODS_AVCaptureVideoHistogramAnalyticsLayerAppearance
+ __OBJC_$_CLASS_METHODS_AVCaptureVideoWaveformAnalyticsLayerAppearance
+ __OBJC_$_INSTANCE_METHODS_AVCaptureVideoAnalyticsAdaptor
+ __OBJC_$_INSTANCE_METHODS_AVCaptureVideoHistogramAnalyticsLayer
+ __OBJC_$_INSTANCE_METHODS_AVCaptureVideoHistogramAnalyticsLayerAppearance
+ __OBJC_$_INSTANCE_METHODS_AVCaptureVideoWaveformAnalyticsLayer
+ __OBJC_$_INSTANCE_METHODS_AVCaptureVideoWaveformAnalyticsLayerAppearance
+ __OBJC_$_INSTANCE_METHODS_AVProVideoStorage
+ __OBJC_$_INSTANCE_METHODS_AVProVideoStorageMaximumCapacityComponents
+ __OBJC_$_INSTANCE_METHODS_AVProVideoStorageSetCapacityOptions
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureVideoAnalyticsAdaptor
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureVideoHistogramAnalyticsLayer
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureVideoHistogramAnalyticsLayerAppearance
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureVideoWaveformAnalyticsLayer
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureVideoWaveformAnalyticsLayerAppearance
+ __OBJC_$_INSTANCE_VARIABLES_AVProVideoStorageMaximumCapacityComponents
+ __OBJC_$_INSTANCE_VARIABLES_AVProVideoStorageSetCapacityOptions
+ __OBJC_$_PROP_LIST_AVCaptureVideoAnalyticsAdaptor
+ __OBJC_$_PROP_LIST_AVCaptureVideoHistogramAnalyticsLayer
+ __OBJC_$_PROP_LIST_AVCaptureVideoHistogramAnalyticsLayerAppearance
+ __OBJC_$_PROP_LIST_AVCaptureVideoWaveformAnalyticsLayer
+ __OBJC_$_PROP_LIST_AVCaptureVideoWaveformAnalyticsLayerAppearance
+ __OBJC_$_PROP_LIST_AVProVideoStorageMaximumCapacityComponents
+ __OBJC_$_PROP_LIST_AVProVideoStorageSetCapacityOptions
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVCaptureVideoAnalyticsAdaptorRendering
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAMetalDisplayLinkDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVCaptureVideoAnalyticsAdaptorRendering
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAMetalDisplayLinkDelegate
+ __OBJC_$_PROTOCOL_REFS_AVCaptureVideoAnalyticsAdaptorRendering
+ __OBJC_CLASS_PROTOCOLS_$_AVCaptureVideoAnalyticsAdaptor
+ __OBJC_CLASS_PROTOCOLS_$_AVCaptureVideoHistogramAnalyticsLayer
+ __OBJC_CLASS_PROTOCOLS_$_AVCaptureVideoHistogramAnalyticsLayerAppearance
+ __OBJC_CLASS_PROTOCOLS_$_AVCaptureVideoWaveformAnalyticsLayer
+ __OBJC_CLASS_PROTOCOLS_$_AVCaptureVideoWaveformAnalyticsLayerAppearance
+ __OBJC_CLASS_RO_$_AVCaptureVideoAnalyticsAdaptor
+ __OBJC_CLASS_RO_$_AVCaptureVideoHistogramAnalyticsLayer
+ __OBJC_CLASS_RO_$_AVCaptureVideoHistogramAnalyticsLayerAppearance
+ __OBJC_CLASS_RO_$_AVCaptureVideoWaveformAnalyticsLayer
+ __OBJC_CLASS_RO_$_AVCaptureVideoWaveformAnalyticsLayerAppearance
+ __OBJC_CLASS_RO_$_AVProVideoStorageMaximumCapacityComponents
+ __OBJC_CLASS_RO_$_AVProVideoStorageSetCapacityOptions
+ __OBJC_LABEL_PROTOCOL_$_AVCaptureVideoAnalyticsAdaptorRendering
+ __OBJC_LABEL_PROTOCOL_$_CAMetalDisplayLinkDelegate
+ __OBJC_METACLASS_RO_$_AVCaptureVideoAnalyticsAdaptor
+ __OBJC_METACLASS_RO_$_AVCaptureVideoHistogramAnalyticsLayer
+ __OBJC_METACLASS_RO_$_AVCaptureVideoHistogramAnalyticsLayerAppearance
+ __OBJC_METACLASS_RO_$_AVCaptureVideoWaveformAnalyticsLayer
+ __OBJC_METACLASS_RO_$_AVCaptureVideoWaveformAnalyticsLayerAppearance
+ __OBJC_METACLASS_RO_$_AVProVideoStorageMaximumCapacityComponents
+ __OBJC_METACLASS_RO_$_AVProVideoStorageSetCapacityOptions
+ __OBJC_PROTOCOL_$_AVCaptureVideoAnalyticsAdaptorRendering
+ __OBJC_PROTOCOL_$_CAMetalDisplayLinkDelegate
+ __PromotedConst
+ ___44+[AVCaptureVideoAnalyticsAdaptor initialize]_block_invoke
+ ___46-[AVProVideoStorage _syncPropertiesFromServer]_block_invoke
+ ___49-[AVProVideoStorage _finalizeReplenishWithError:]_block_invoke
+ ___49-[AVProVideoStorage _finalizeReplenishWithError:]_block_invoke_2
+ ___53+[AVCaptureVideoAnalyticsAdaptor defaultCommandQueue]_block_invoke
+ ___53-[AVProVideoStorage _setCapacity:options:completion:]_block_invoke
+ ___54-[AVCaptureVideoAnalyticsAdaptor ingestCGImage:error:]_block_invoke
+ ___60-[AVProVideoStorage replenishCapacityWithCompletionHandler:]_block_invoke
+ ___64-[AVProVideoStorage _attemptReplenishWithCapacity:attemptCount:]_block_invoke
+ ___70-[AVCaptureVideoHistogramAnalyticsLayer metalDisplayLink:needsUpdate:]_block_invoke
+ ___73-[AVCaptureVideoAnalyticsAdaptor _processPixelBuffer:slotReleaseHandler:]_block_invoke
+ ___80-[AVCaptureVideoHistogramAnalyticsLayer _renderInterpolatedHistogramToDrawable:]_block_invoke
+ ___96-[AVCaptureVideoHistogramAnalyticsLayer _renderInterpolatedHistogramWithBackPressureToDrawable:]_block_invoke
+ ___avVirtualCardNotification_block_invoke
+ ___block_descriptor_32_e22_v16?0"NSMutableSet"8l
+ ___block_descriptor_33_e22_v16?0"NSMutableSet"8l
+ ___block_descriptor_40_e8_32o_e28_v16?0"<MTLCommandBuffer>"8l
+ ___block_descriptor_48_e8_32o40o_e8_v12?0I8l
+ ___block_descriptor_56_e8_32o40b_e5_v8?0l
+ ___block_descriptor_56_e8_32o40o48b_e28_v16?0"<MTLCommandBuffer>"8l
+ ___block_descriptor_56_e8_32o_e17_v16?0"NSError"8l
+ ___copy_helper_block_e8_32o40o48b
+ ___destroy_helper_block_e8_32o40o48b
+ ___tg_getFilamentRenderPipeline_block_invoke
+ ___tg_getFilamentVertexBuildPipeline_block_invoke
+ ___tg_getIndirectArgsBuildPipeline_block_invoke
+ ___tg_getPrecursorBuildPipeline_block_invoke
+ ___tg_getWaveformShaderLibrary_block_invoke
+ ___tg_updatePixelAccurateSize_block_invoke
+ ___updatePixelAccurateSize_block_invoke
+ ___vcc_handleAllocationCallback_block_invoke_2
+ __onceToken
+ __os_log_debug_impl
+ __os_log_error_impl
+ __sharedCIContext
+ __sharedCIImageOptions
+ __sharedCITextureCache
+ __sharedCommandQueue
+ __sharedDevice
+ _configureBlend
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dynamicHistogramUpdateInterval
+ _gAVProVideoStorageTrace
+ _kCIContextCVMetalTextureCache
+ _kCIContextCacheIntermediates
+ _kCIContextUseSoftwareRenderer
+ _kCIContextWorkingFormat
+ _kCIFormatBGRA8
+ _kCVPixelBufferMetalCompatibilityKey
+ _kDefaultHistogramFillEndColors
+ _kDefaultHistogramFillStartColors
+ _kDefaultHistogramLineColors
+ _kDefaultWaveformFillColors
+ _kFigProVideoStorageNotificationPayloadKey_BusyFlags
+ _kFigProVideoStorageNotification_BusyReasons
+ _kFigProVideoStorageProperty_BusyReasons
+ _kFigVirtualCaptureCardMaximumCapacityComponentsKey_MaximumCapacity
+ _kFigVirtualCaptureCardMaximumCapacityComponentsKey_PurgeableSpace
+ _kFigVirtualCaptureCardProperty_MaximumCapacityComponents
+ _kFigVirtualCaptureCardProperty_MaximumCapacityComponentsExcludingPurgeable
+ _kFigVirtualCaptureCardSetCapacityOption_ReplenishMode
+ _objc_msgSend$_attemptReplenishWithCapacity:attemptCount:
+ _objc_msgSend$_computeHistogramFromTexture:
+ _objc_msgSend$_convertPixelBufferViaCoreImage:commandBuffer:
+ _objc_msgSend$_createGraphicsPipelinesWithBlendMode:
+ _objc_msgSend$_finalizeReplenishWithError:
+ _objc_msgSend$_getLuminanceFillColors
+ _objc_msgSend$_getLuminanceMatricesWithLineColors:fillStartColors:fillEndColors:
+ _objc_msgSend$_getRGBFillColors
+ _objc_msgSend$_getRGBMatricesWithLineColors:fillStartColors:fillEndColors:
+ _objc_msgSend$_getYUVFillColors
+ _objc_msgSend$_hasAttachedVideoDataOutput
+ _objc_msgSend$_initializeHistogramTextures
+ _objc_msgSend$_initializeRenderingPipeline
+ _objc_msgSend$_isBusyForPropertyReads
+ _objc_msgSend$_matrixFromDefault:disablingChannels:
+ _objc_msgSend$_maximumCapacityComponentsIncludingPurgeableSpace:
+ _objc_msgSend$_processPixelBuffer:slotReleaseHandler:
+ _objc_msgSend$_renderFrameToUpdate:sourceTexture:
+ _objc_msgSend$_renderInterpolatedHistogram
+ _objc_msgSend$_renderInterpolatedHistogramToDrawable:
+ _objc_msgSend$_renderInterpolatedHistogramWithBackPressureToDrawable:
+ _objc_msgSend$_replenishErrorForOSStatus:
+ _objc_msgSend$_setCapacity:options:completion:
+ _objc_msgSend$_setHighResolutionPhotoEnabled:
+ _objc_msgSend$_startDisplayLink
+ _objc_msgSend$_stopDisplayLink
+ _objc_msgSend$_updateBusyReasons:
+ _objc_msgSend$addCompletedHandler:
+ _objc_msgSend$addToRunLoop:forMode:
+ _objc_msgSend$busyReasons
+ _objc_msgSend$channelBlendMode
+ _objc_msgSend$channelFillColor
+ _objc_msgSend$channelFillColorEnd
+ _objc_msgSend$channelFillColorStart
+ _objc_msgSend$channelFillGradientAngle
+ _objc_msgSend$channelLineColor
+ _objc_msgSend$channelLineThickness
+ _objc_msgSend$colorAttachments
+ _objc_msgSend$commandBuffer
+ _objc_msgSend$computeCommandEncoder
+ _objc_msgSend$contentsScale
+ _objc_msgSend$contextWithMTLCommandQueue:options:
+ _objc_msgSend$defaultCommandQueue
+ _objc_msgSend$defaultLuminanceAppearance
+ _objc_msgSend$defaultRGBCompositeAppearance
+ _objc_msgSend$detachFromVideoDataOutput
+ _objc_msgSend$dispatchThreadgroups:threadsPerThreadgroup:
+ _objc_msgSend$drawPrimitives:indirectBuffer:indirectBufferOffset:
+ _objc_msgSend$drawPrimitives:vertexStart:vertexCount:
+ _objc_msgSend$drawable
+ _objc_msgSend$endEncoding
+ _objc_msgSend$extent
+ _objc_msgSend$imageByApplyingTransform:
+ _objc_msgSend$imageWithCGImage:options:
+ _objc_msgSend$initWithMaximumCapacity:purgeableSpace:
+ _objc_msgSend$initWithMetalLayer:
+ _objc_msgSend$initWithOptions:capacity:
+ _objc_msgSend$isParade
+ _objc_msgSend$mainRunLoop
+ _objc_msgSend$maximumCapacityComponents
+ _objc_msgSend$newBufferWithLength:options:
+ _objc_msgSend$newCommandQueue
+ _objc_msgSend$newComputePipelineStateWithFunction:error:
+ _objc_msgSend$newFunctionWithName:
+ _objc_msgSend$newLibraryWithSource:options:error:
+ _objc_msgSend$newRenderPipelineStateWithDescriptor:error:
+ _objc_msgSend$newTextureWithDescriptor:
+ _objc_msgSend$nextDrawable
+ _objc_msgSend$numberOfBars
+ _objc_msgSend$pixelFormat
+ _objc_msgSend$presentDrawable:
+ _objc_msgSend$reason
+ _objc_msgSend$render:toCVPixelBuffer:bounds:colorSpace:
+ _objc_msgSend$render:toMTLTexture:commandBuffer:bounds:colorSpace:
+ _objc_msgSend$renderCommandEncoderWithDescriptor:
+ _objc_msgSend$renderPassDescriptor
+ _objc_msgSend$renderWithSampleImage:commandBuffer:
+ _objc_msgSend$replaceRegion:mipmapLevel:withBytes:bytesPerRow:
+ _objc_msgSend$replenishMode
+ _objc_msgSend$setAllowsNextDrawableTimeout:
+ _objc_msgSend$setAlphaBlendOperation:
+ _objc_msgSend$setBlendingEnabled:
+ _objc_msgSend$setBuffer:offset:atIndex:
+ _objc_msgSend$setBytes:length:atIndex:
+ _objc_msgSend$setChannelBlendMode:
+ _objc_msgSend$setChannelFillColor:
+ _objc_msgSend$setChannelFillColorEnd:
+ _objc_msgSend$setChannelFillColorStart:
+ _objc_msgSend$setChannelFillGradientAngle:
+ _objc_msgSend$setChannelLineColor:
+ _objc_msgSend$setChannelLineThickness:
+ _objc_msgSend$setClearColor:
+ _objc_msgSend$setCommandTypes:
+ _objc_msgSend$setComputePipelineState:
+ _objc_msgSend$setDestinationAlphaBlendFactor:
+ _objc_msgSend$setDestinationRGBBlendFactor:
+ _objc_msgSend$setDevice:
+ _objc_msgSend$setDrawableSize:
+ _objc_msgSend$setFragmentFunction:
+ _objc_msgSend$setFramebufferOnly:
+ _objc_msgSend$setInheritBuffers:
+ _objc_msgSend$setInheritPipelineState:
+ _objc_msgSend$setIsParade:
+ _objc_msgSend$setLabel:
+ _objc_msgSend$setLoadAction:
+ _objc_msgSend$setMaxVertexBufferBindCount:
+ _objc_msgSend$setMaximumDrawableCount:
+ _objc_msgSend$setNumberOfBars:
+ _objc_msgSend$setPixelFormat:
+ _objc_msgSend$setRenderPipelineState:
+ _objc_msgSend$setReplenishMode:
+ _objc_msgSend$setRgbBlendOperation:
+ _objc_msgSend$setSampleBufferDelegate:queue:
+ _objc_msgSend$setSmoothness:
+ _objc_msgSend$setSourceAlphaBlendFactor:
+ _objc_msgSend$setSourceRGBBlendFactor:
+ _objc_msgSend$setStorageMode:
+ _objc_msgSend$setStoreAction:
+ _objc_msgSend$setSubstrateColor:
+ _objc_msgSend$setTexture:
+ _objc_msgSend$setTexture:atIndex:
+ _objc_msgSend$setUsage:
+ _objc_msgSend$setVertexBuffer:offset:atIndex:
+ _objc_msgSend$setVertexBytes:length:atIndex:
+ _objc_msgSend$setVertexFunction:
+ _objc_msgSend$setVertexTexture:atIndex:
+ _objc_msgSend$smoothness
+ _objc_msgSend$substrateColor
+ _objc_msgSend$superlayer
+ _objc_msgSend$targetPresentationTimestamp
+ _objc_msgSend$texture
+ _objc_msgSend$texture2DDescriptorWithPixelFormat:width:height:mipmapped:
+ _objc_msgSend$thermalState
+ _objc_msgSend$waitUntilCompleted
+ _tg_getWaveformShaderLibrary
+ _tg_updatePixelAccurateSize
+ _updatePixelAccurateSize
+ tg_getFilamentRenderPipeline.cachedPipelines
+ tg_getFilamentRenderPipeline.onceToken
+ tg_getFilamentVertexBuildPipeline.cachedPipeline
+ tg_getFilamentVertexBuildPipeline.onceToken
+ tg_getIndirectArgsBuildPipeline.cachedPipeline
+ tg_getIndirectArgsBuildPipeline.onceToken
+ tg_getPrecursorBuildPipeline.cachedPipeline
+ tg_getPrecursorBuildPipeline.onceToken
+ tg_getWaveformShaderLibrary.cachedLibrary
+ tg_getWaveformShaderLibrary.onceToken
- +[AVVirtualCaptureCard sharedVirtualCaptureCard]
- -[AVProVideoStorage _updateBusy:]
- -[AVProVideoStorage(Deprecated) capacity]
- -[AVProVideoStorage(Deprecated) freeSize]
- GCC_except_table95
- OBJC_IVAR_$_AVProVideoStorage._busy
- _OBJC_CLASS_$_AVVirtualCaptureCard
- _OBJC_METACLASS_$_AVVirtualCaptureCard
- __OBJC_$_CLASS_METHODS_AVVirtualCaptureCard
- __OBJC_$_CLASS_PROP_LIST_AVVirtualCaptureCard
- __OBJC_$_INSTANCE_METHODS_AVProVideoStorage(Deprecated)
- __OBJC_CLASS_RO_$_AVVirtualCaptureCard
- __OBJC_METACLASS_RO_$_AVVirtualCaptureCard
- ___44-[AVProVideoStorage setCapacity:completion:]_block_invoke
- _gAVVirtualCaptureCardTrace
- _kFigVirtualCaptureCardProperty_IsBusy
- _kFigVirtualCaptureCardProperty_MaximumCapacity
- _objc_msgSend$_updateBusy:
- _objc_msgSend$isBusy
CStrings:
+ "\n\n#include <metal_stdlib>\nusing namespace metal;\n\nconstant int PRECURSOR_WIDTH = 100;\nconstant int PRECURSOR_HEIGHT = 100;\nconstant int CHANNEL_COUNT = 4;\nconstant int SEGMENTS_PER_ROW = PRECURSOR_WIDTH - 1;\nconstant int VERTICES_PER_SEGMENT = 6;\nconstant float FILAMENT_THICKNESS_SCALE = 1.5;\nconstant uint MAX_VERTEX_COUNT = uint(CHANNEL_COUNT * PRECURSOR_HEIGHT * SEGMENTS_PER_ROW * VERTICES_PER_SEGMENT);\n\nstruct VertexOut {\n    float4 position [[position]];\n    float2 localUV;\n    float4 color;\n    float intensity;\n};\n\nstruct FilamentVertex {\n    float2 position;\n    float2 localUV;\n    float4 color;\n    float intensity;\n};\n\ninline float channelValueAtIndex(float4 sampleValue, int ch)\n{\n    if (ch == 0) return sampleValue.r;\n    if (ch == 1) return sampleValue.g;\n    if (ch == 2) return sampleValue.b;\n    return sampleValue.a;\n}\n\ninline float2 compositePointForChannel(float columnCenter, float value)\n{\n    return float2(columnCenter, 1.0 - value);\n}\n\ninline float2 paradePointForChannel(float columnCenter, float value, int ch, int slotIndex, int activeCount)\n{\n    const float gap = 0.0125;\n    const float usableWidth = 1.0 - gap * float(activeCount - 1);\n    const float slotWidth = usableWidth / float(activeCount);\n    float x = float(slotIndex) * (slotWidth + gap) + columnCenter * slotWidth;\n    float y = 1.0 - value;\n    return float2(x, y);\n}\n\ninline float2 uvToClip(float2 uv)\n{\n    return float2(uv.x * 2.0 - 1.0, 1.0 - uv.y * 2.0);\n}\n\ninline void writeVertex(\n    device FilamentVertex *outVertices,\n    uint vertexIndex,\n    float2 uv,\n    float2 localUV,\n    float4 color,\n    float intensity\n)\n{\n    if (vertexIndex >= MAX_VERTEX_COUNT) {\n        return;\n    }\n\n    FilamentVertex v;\n    v.position = uvToClip(uv);\n    v.localUV = localUV;\n    v.color = color;\n    v.intensity = intensity;\n    outVertices[vertexIndex] = v;\n}\n\n// Stores average RGB + luma in a 100x100 lattice from pre-converted RGBA source.\nkernel void waveform_build_precursor(\n    texture2d<float, access::sample> sourceTexture [[texture(0)]],\n    texture2d<half, access::write> precursorTexture [[texture(1)]],\n    constant float &rotationDegrees [[buffer(0)]],\n    constant bool &mirrored [[buffer(1)]],\n    uint2 gid [[thread_position_in_grid]]\n)\n{\n    if (gid.x >= PRECURSOR_WIDTH || gid.y >= PRECURSOR_HEIGHT) {\n        return;\n    }\n\n    constexpr sampler nearestSampler(mag_filter::nearest,\n                                     min_filter::nearest,\n                                     address::clamp_to_edge);\n\n    float2 sourceSize = float2(sourceTexture.get_width(), sourceTexture.get_height());\n\n    float2 cellMin = float2(gid) / float2(PRECURSOR_WIDTH, PRECURSOR_HEIGHT);\n    float2 cellMax = float2(gid + 1) / float2(PRECURSOR_WIDTH, PRECURSOR_HEIGHT);\n\n    float angleRadians = -rotationDegrees * (M_PI_F / 180.0);\n    float ca = cos(angleRadians);\n    float sa = sin(angleRadians);\n\n    float2 corners[4] = {\n        float2(cellMin.x, cellMin.y),\n        float2(cellMax.x, cellMin.y),\n        float2(cellMin.x, cellMax.y),\n        float2(cellMax.x, cellMax.y)\n    };\n\n    float2 srcMin = float2(1.0e30);\n    float2 srcMax = float2(-1.0e30);\n    for (int i = 0; i < 4; i++) {\n        float2 uv = corners[i];\n        if (mirrored) {\n            uv.x = 1.0 - uv.x;\n        }\n        float2 c = uv - 0.5;\n        float2 r = float2(ca * c.x - sa * c.y, sa * c.x + ca * c.y) + 0.5;\n        srcMin = min(srcMin, r);\n        srcMax = max(srcMax, r);\n    }\n\n    int x0 = int(floor(srcMin.x * sourceSize.x));\n    int x1 = int(ceil(srcMax.x * sourceSize.x));\n    int y0 = int(floor(srcMin.y * sourceSize.y));\n    int y1 = int(ceil(srcMax.y * sourceSize.y));\n\n    x0 = clamp(x0, 0, int(sourceSize.x) - 1);\n    x1 = clamp(x1, x0 + 1, int(sourceSize.x));\n    y0 = clamp(y0, 0, int(sourceSize.y) - 1);\n    y1 = clamp(y1, y0 + 1, int(sourceSize.y));\n\n    float3 accumRGB = float3(0.0);\n    float accumLuma = 0.0;\n    float sampleCount = 0.0;\n\n    for (int sy = y0; sy < y1; sy++) {\n        for (int sx = x0; sx < x1; sx++) {\n            float2 coord = (float2(sx, sy) + 0.5) / sourceSize;\n            float3 rgb = clamp(sourceTexture.sample(nearestSampler, coord).rgb, 0.0, 1.0);\n            float luma = dot(rgb, float3(0.299, 0.587, 0.114));\n\n            accumRGB += rgb;\n            accumLuma += luma;\n            sampleCount += 1.0;\n        }\n    }\n\n    float invCount = 1.0 / max(sampleCount, 1.0);\n    float3 avgRGB = accumRGB * invCount;\n    float avgLuma = accumLuma * invCount;\n\n    precursorTexture.write(half4(half3(avgRGB), half(avgLuma)), gid);\n}\n\n// One thread emits one segment for one channel and one precursor row.\nkernel void waveform_build_filament_vertices(\n    texture2d<float, access::sample> precursorTexture [[texture(0)]],\n    device FilamentVertex *outVertices [[buffer(0)]],\n    device atomic_uint *vertexCount [[buffer(1)]],\n    constant float4x4 &channelColors [[buffer(2)]],\n    constant bool &isParade [[buffer(3)]],\n    constant float &smoothness [[buffer(4)]],\n    uint3 gid [[thread_position_in_grid]]\n)\n{\n    uint column = gid.x;\n    uint row = gid.y;\n    uint ch = gid.z;\n\n    if (column >= uint(SEGMENTS_PER_ROW) || row >= uint(PRECURSOR_HEIGHT) || ch >= uint(CHANNEL_COUNT)) {\n        return;\n    }\n\n    float4 channelColor = channelColors.columns[ch];\n    if (channelColor.a <= 0.0) {\n        return;\n    }\n\n    constexpr sampler nearestSampler(mag_filter::nearest,\n                                     min_filter::nearest,\n                                     address::clamp_to_edge);\n\n    float x0 = (float(column) + 0.5) / float(PRECURSOR_WIDTH);\n    float x1 = (float(column + 1) + 0.5) / float(PRECURSOR_WIDTH);\n    float ySample = (float(row) + 0.5) / float(PRECURSOR_HEIGHT);\n\n    float4 p0 = precursorTexture.sample(nearestSampler, float2(x0, ySample));\n    float4 p1 = precursorTexture.sample(nearestSampler, float2(x1, ySample));\n\n    float value0 = channelValueAtIndex(p0, int(ch));\n    float value1 = channelValueAtIndex(p1, int(ch));\n\n    // Compute parade slot index and active channel count from channelColors\n    int slotIndex = 0;\n    int activeCount = 0;\n    for (int i = 0; i < CHANNEL_COUNT; i++) {\n        if (channelColors.columns[i].w > 0.0) {\n            if (i < int(ch)) slotIndex++;\n            activeCount++;\n        }\n    }\n\n    float2 a = isParade ? paradePointForChannel(x0, value0, int(ch), slotIndex, activeCount) : compositePointForChannel(x0, value0);\n    float2 b = isParade ? paradePointForChannel(x1, value1, int(ch), slotIndex, activeCount) : compositePointForChannel(x1, value1);\n\n    float energy0 = max(p0.a, 0.001);\n    float energy1 = max(p1.a, 0.001);\n    float energy = 0.5 * (energy0 + energy1);\n\n    float2 dir = b - a;\n    float len = max(length(dir), 1e-6);\n    dir /= len;\n\n    float2 normal = float2(-dir.y, dir.x);\n\n    float thickness = mix(0.0005, 0.003, smoothness) * FILAMENT_THICKNESS_SCALE;\n    float2 offset = normal * thickness;\n\n    float2 p00 = a - offset;\n    float2 p01 = a + offset;\n    float2 p10 = b - offset;\n    float2 p11 = b + offset;\n\n    float intensity = energy * mix(1.4, 0.9, smoothness);\n\n    uint baseVertex = atomic_fetch_add_explicit(vertexCount,\n                                                uint(VERTICES_PER_SEGMENT),\n                                                memory_order_relaxed);\n    if (baseVertex + uint(VERTICES_PER_SEGMENT) > MAX_VERTEX_COUNT) {\n        return;\n    }\n\n    // Triangle 1\n    writeVertex(outVertices, baseVertex + 0, p00, float2(0.0, -1.0), channelColor, intensity);\n    writeVertex(outVertices, baseVertex + 1, p01, float2(0.0,  1.0), channelColor, intensity);\n    writeVertex(outVertices, baseVertex + 2, p10, float2(1.0, -1.0), channelColor, intensity);\n\n    // Triangle 2\n    writeVertex(outVertices, baseVertex + 3, p10, float2(1.0, -1.0), channelColor, intensity);\n    writeVertex(outVertices, baseVertex + 4, p01, float2(0.0,  1.0), channelColor, intensity);\n    writeVertex(outVertices, baseVertex + 5, p11, float2(1.0,  1.0), channelColor, intensity);\n}\n\nvertex VertexOut waveform_filament_vertex(\n    device const FilamentVertex *vertices [[buffer(0)]],\n    uint vid [[vertex_id]]\n)\n{\n    VertexOut out;\n    FilamentVertex v = vertices[vid];\n    out.position = float4(v.position, 0.0, 1.0);\n    out.localUV = v.localUV;\n    out.color = v.color;\n    out.intensity = v.intensity;\n    return out;\n}\n\nfragment float4 waveform_filament_fragment(VertexOut in [[stage_in]])\n{\n    // localUV.y is -1..1 across the filament thickness.\n    float d = abs(in.localUV.y);\n\n    // Soft filament core + halo.\n    float core = exp(-pow(d / 0.45, 2.0));\n    float halo = exp(-pow(d / 1.25, 2.0));\n    float shape = core + 0.35 * halo;\n\n    // Low per-filament contribution — density builds up via additive blending.\n    float brightness = shape * in.intensity * 0.12;\n    float3 color = in.color.rgb * brightness;\n\n    return float4(color, brightness * in.color.a);\n}\n\nkernel void waveform_build_indirect_args(\n    device atomic_uint *vertexCount [[buffer(0)]],\n    device MTLDrawPrimitivesIndirectArguments *indirectArgs [[buffer(1)]],\n    uint gid [[thread_position_in_grid]]\n)\n{\n    if (gid == 0) {\n        uint count = atomic_load_explicit(vertexCount, memory_order_relaxed);\n        // Clamp to maximum to prevent buffer overrun\n        count = min(count, MAX_VERTEX_COUNT);\n        indirectArgs->vertexCount = count;\n        indirectArgs->instanceCount = 1;\n        indirectArgs->vertexStart = 0;\n        indirectArgs->baseInstance = 0;\n    }\n}\n\n"
+ "\n#include <metal_stdlib>\nusing namespace metal;\n\n#define HISTOGRAM_BIN_COUNT 256\n#define HISTOGRAM_CHANNEL_COUNT 4\n#define RED_CHANNEL_OFFSET 0\n#define GREEN_CHANNEL_OFFSET 256\n#define BLUE_CHANNEL_OFFSET 512\n#define LUMA_CHANNEL_OFFSET 768\n#define SQUARE_ROOT_OF_THREE 1.73205080757\n\nenum HistogramMode {\n\tLuminance       = 0,\n\tCompositeRGB    = 1,\n\tRGBParade       = 2\n};\n\nenum GradientInterpolation {\n\tLinear = 0,\n\tLogarithmic = 1,\n\tExponential = 2,\n\tSigmoid = 3\n};\n\nstruct ChannelAppearance {\n\tfloat4 lineColor;\n\tfloat  lineThickness;     // pixels\n\tfloat4 fillColorStart;\n\tfloat4 fillColorEnd;\n\tfloat  gradientAngle;     // radians (0.0 = horizontal L→R, π/2 = vertical T→B)\n\tfloat  smoothness;        // smoothness factor for histogram curve interpolation (0.0 = sharp, 1.0 = smooth)\n};\n\nstruct VSOut {\n\tfloat4 position [[position]];\n\tfloat4 color;\n\tfloat2 uv [[user(locn0)]];\n};\n\ninline float applyGradientInterpolation(float interpolationValue, uint interpolationType)\n{\n\tinterpolationValue = clamp(interpolationValue, 0.0, 1.0);\n\tswitch (interpolationType) {\n\t\tcase Sigmoid:      return smoothstep(0.0, 1.0, interpolationValue);\n\t\tcase Exponential:  return (exp(interpolationValue) - 1.0) / (M_E_F - 1.0);\n\t\tcase Logarithmic:  return log(1.0 + interpolationValue * (M_E_F - 1.0)) / M_E_F;\n\t\tdefault:           return interpolationValue;\n\t}\n}\n\nkernel void computeHistogram(texture2d<float,access::sample> sourceTexture [[texture(0)]],\n\t\t\t\t\t\t\t device atomic_uint *histogramBuffer [[buffer(0)]],\n\t\t\t\t\t\t\t constant uint &histogramMode [[buffer(1)]],\n\t\t\t\t\t\t\t uint2 gridId [[thread_position_in_grid]]) {\n\tif (gridId.x>=sourceTexture.get_width()||gridId.y>=sourceTexture.get_height()) return;\n\tconstexpr sampler textureSampler(mag_filter::linear,min_filter::linear);\n\tfloat2 textureCoord=float2(gridId)/float2(sourceTexture.get_width(),sourceTexture.get_height());\n\tfloat3 color=clamp(sourceTexture.sample(textureSampler,textureCoord).rgb,0.0,1.0);\n\tfloat luminance = 1.0 - (length(float3(1.0) - color.rgb) / SQUARE_ROOT_OF_THREE); // Evaluate against perceptual luma\n\n\t// Calculate bins for RGB and luminance\n\tuint redBin=uint(color.r*255.0), greenBin=uint(color.g*255.0), blueBin=uint(color.b*255.0), luminanceBin=uint(luminance*255.0);\n\t\n\t// Always accumulate RGB and luminance\n\tatomic_fetch_add_explicit(&histogramBuffer[RED_CHANNEL_OFFSET+redBin],1,memory_order_relaxed);\n\tatomic_fetch_add_explicit(&histogramBuffer[GREEN_CHANNEL_OFFSET+greenBin],1,memory_order_relaxed);\n\tatomic_fetch_add_explicit(&histogramBuffer[BLUE_CHANNEL_OFFSET+blueBin],1,memory_order_relaxed);\n\tatomic_fetch_add_explicit(&histogramBuffer[LUMA_CHANNEL_OFFSET+luminanceBin],1,memory_order_relaxed);\n}\n\nkernel void normalizeHistogramToTexture(device const uint* histogramBuffer [[buffer(0)]],\n\t\t\t\t\t\t\t\t\t\ttexture2d<float, access::write> outputTexture [[texture(0)]],\n\t\t\t\t\t\t\t\t\t\tconstant uint& histogramMode [[buffer(1)]],\n\t\t\t\t\t\t\t\t\t\tuint gridId [[thread_position_in_grid]]) {\n\tif (gridId >= HISTOGRAM_BIN_COUNT) return;\n\t\n\tuint maxRedCount = 1, maxGreenCount = 1, maxBlueCount = 1, maxLuminanceCount = 1;\n\tfor (uint i = 0; i < HISTOGRAM_BIN_COUNT; ++i) {\n\t\tmaxRedCount = max(maxRedCount, histogramBuffer[RED_CHANNEL_OFFSET + i]);\n\t\tmaxGreenCount = max(maxGreenCount, histogramBuffer[GREEN_CHANNEL_OFFSET + i]);\n\t\tmaxBlueCount = max(maxBlueCount, histogramBuffer[BLUE_CHANNEL_OFFSET + i]);\n\t\tmaxLuminanceCount = max(maxLuminanceCount, histogramBuffer[LUMA_CHANNEL_OFFSET + i]);\n\t}\n\t\n\tfloat normalizedRed = float(histogramBuffer[RED_CHANNEL_OFFSET + gridId]) / float(maxRedCount);\n\tfloat normalizedGreen = float(histogramBuffer[GREEN_CHANNEL_OFFSET + gridId]) / float(maxGreenCount);\n\tfloat normalizedBlue = float(histogramBuffer[BLUE_CHANNEL_OFFSET + gridId]) / float(maxBlueCount);\n\tfloat normalizedLuminance = float(histogramBuffer[LUMA_CHANNEL_OFFSET + gridId]) / float(maxLuminanceCount);\n\t\n\toutputTexture.write(float4(normalizedRed, normalizedGreen, normalizedBlue, normalizedLuminance), uint2(gridId, 0));\n}\n\ninline float channelHeight(uint channelIndex, float4 values)\n{\n\treturn (channelIndex==0)?values.r : (channelIndex==1)?values.g : (channelIndex==2)?values.b : values.a;\n}\n\ninline float4 sampleHistSmooth(texture2d<float, access::sample> previousHistogram,\n\t\t\t\t\t\t\t   texture2d<float, access::sample> currentHistogram,\n\t\t\t\t\t\t\t   float interpolation,\n\t\t\t\t\t\t\t   int binIndex,\n\t\t\t\t\t\t\t   float smoothness)\n{\n\tconstexpr sampler textureSampler(coord::pixel, filter::linear);\n\t// Use smoothness to control the radius: 0.5 gives original behavior (1.5)\n\tconst float radius = 1.5 * (0.1 + 0.9 * smoothness); // Range: 0.15 to 1.5\n\tconst int radiusInt = int(ceil(radius));\n\tfloat4 previousValue = 0.0, currentValue = 0.0; float weightSum = 0.0;\n\n\tint maxBin = (int)previousHistogram.get_width() - 1; // supports 256-bin\n\n\tfor (int offset = -radiusInt; offset <= radiusInt; ++offset) {\n\t\tint sampledBin = binIndex + offset;\n\t\tif (sampledBin >= 0 && sampledBin <= maxBin) {\n\t\t\tfloat distance = abs(float(offset));\n\t\t\tif (distance <= radius) {\n\t\t\t\tfloat weight = exp(-0.5 * pow(distance/2.0, 2.0));\n\t\t\t\tpreviousValue += previousHistogram.sample(textureSampler, float2(sampledBin + 0.5, 0.5)) * weight;\n\t\t\t\tcurrentValue += currentHistogram.sample(textureSampler, float2(sampledBin + 0.5, 0.5)) * weight;\n\t\t\t\tweightSum += weight;\n\t\t\t}\n\t\t}\n\t}\n\tpreviousValue /= max(weightSum, 1e-6);\n\tcurrentValue /= max(weightSum, 1e-6);\n\treturn mix(previousValue, currentValue, interpolation);\n}\n\ninline float normalizedDeviceCoordinateXFromBin(uint binIndex, uint channelIndex, uint histogramMode)\n{\n\tif (histogramMode == RGBParade) {\n\t\t// Add small gaps between channels in parade mode\n\t\tconst float gapWidth = 0.025; // Small gap between channels (1.25% of total width per gap)\n\t\tconst float totalGapWidth = gapWidth * 2.0; // Two gaps (between channels)\n\t\tconst float availableWidth = 2.0 - totalGapWidth;\n\t\tconst float channelWidth = availableWidth / 3.0;\n\t\t\n\t\tfloat channelOffset = -1.0 + (float(channelIndex) * (channelWidth + gapWidth));\n\t\treturn channelOffset + (channelWidth * float(binIndex) / 255.0);\n\t}\n\treturn -1.0 + (2.0 * float(binIndex) / 255.0);\n}\n\ninline float normalizedDeviceCoordinateYFromHeight(float height)\n{\n\treturn -1.0 + height * 1.8; // bottom anchored\n}\n\nvertex VSOut histogramVertex_Fill(uint vertexId [[vertex_id]],\n\t\t\t\t\t\t\t\t  texture2d<float, access::sample> previousHistogram [[texture(0)]],\n\t\t\t\t\t\t\t\t  texture2d<float, access::sample> currentHistogram [[texture(1)]],\n\t\t\t\t\t\t\t\t  constant float &interpolation           [[buffer(0)]],\n\t\t\t\t\t\t\t\t  constant float2 &drawableSize           [[buffer(1)]],\n\t\t\t\t\t\t\t\t  constant uint &histogramMode            [[buffer(2)]],\n\t\t\t\t\t\t\t\t  constant uint &channelIndex             [[buffer(3)]],\n\t\t\t\t\t\t\t\t  constant ChannelAppearance &appearance  [[buffer(4)]],\n\t\t\t\t\t\t\t\t  constant uint &numberOfBars             [[buffer(6)]])\n{\n\tVSOut output;\n\t\n\t// Check if we should render bars (numberOfBars > 1) or solid curve\n\tif (numberOfBars > 1) {\n\t\t// Calculate bars per channel based on histogram mode\n\t\tuint barsPerChannel;\n\t\tif (histogramMode == RGBParade) {\n\t\t\t// In parade modes, divide total bars among 3 channels\n\t\t\tbarsPerChannel = numberOfBars / 3;\n\t\t} else {\n\t\t\t// In other modes, use all bars for the single display\n\t\t\tbarsPerChannel = numberOfBars;\n\t\t}\n\t\t\n\t\t// Render histogram as bars - configurable number of bars per channel\n\t\tconst uint numBars = barsPerChannel;\n\t\tconst uint binsPerBar = HISTOGRAM_BIN_COUNT / numBars;\n\t\t\n\t\t// Calculate which bar and which vertex within that bar\n\t\tuint barIndex = vertexId / 4;\n\t\tuint vertexInBar = vertexId % 4;\n\t\t\n\t\t// If we exceed the number of bars, return degenerate vertex\n\t\tif (barIndex >= numBars) {\n\t\t\toutput.position = float4(0.0, 0.0, 0.0, 1.0);\n\t\t\toutput.uv = float2(0.0, 0.0);\n\t\t\toutput.color = float4(0.0, 0.0, 0.0, 0.0);\n\t\t\treturn output;\n\t\t}\n\t\t\n\t\t// Sample histogram data for this bar - average across multiple bins\n\t\tfloat totalValue = 0.0;\n\t\tuint startBin = barIndex * binsPerBar;\n\t\tuint endBin = min(startBin + binsPerBar, uint(HISTOGRAM_BIN_COUNT));\n\t\t\n\t\tfor (uint binIndex = startBin; binIndex < endBin; binIndex++) {\n\t\t\tfloat4 histogramValues = sampleHistSmooth(previousHistogram, currentHistogram, interpolation, int(binIndex), appearance.smoothness);\n\t\t\ttotalValue += channelHeight(channelIndex, histogramValues);\n\t\t}\n\t\tfloat averageHeight = totalValue / float(endBin - startBin);\n\t\t\n\t\t// Calculate bar layout based on histogram mode\n\t\tfloat channelWidth, channelOffset;\n\t\t\n\t\tif (histogramMode == RGBParade) {\n\t\t\t// Add small gaps between channels in parade mode (matching normalizedDeviceCoordinateXFromBin)\n\t\t\tconst float gapWidth = 0.025; // Small gap between channels (1.25% of total width per gap)\n\t\t\tconst float totalGapWidth = gapWidth * 2.0; // Two gaps\n\t\t\tconst float availableWidth = 2.0 - totalGapWidth;\n\t\t\tchannelWidth = availableWidth / 3.0;\n\t\t\tchannelOffset = -1.0 + (float(channelIndex) * (channelWidth + gapWidth));\n\t\t} else {\n\t\t\tchannelWidth = 2.0;  // Full width\n\t\t\tchannelOffset = -1.0; // Starting position\n\t\t}\n\t\t\n\t\t// Calculate bar dimensions with spacing\n\t\tconst float spacingRatio = 0.3; // 30% spacing between bars (3x the original 10%)\n\t\tconst float barWidth = (channelWidth * (1.0 - spacingRatio)) / float(numBars);\n\t\tconst float barSpacing = (channelWidth * spacingRatio) / float(numBars + 1);\n\t\t\n\t\t// Calculate bar position\n\t\tfloat barCenterX = channelOffset + barSpacing + (barWidth * 0.5) + (float(barIndex) * (barWidth + barSpacing));\n\t\t\n\t\t// Calculate bar height based on histogram data (bottom-anchored)\n\t\tfloat baseY = -0.9;  // Bottom baseline\n\t\tfloat maxHeight = 1.7; // Maximum bar height in NDC\n\t\tfloat barTop = baseY + (averageHeight * maxHeight);\n\t\t\n\t\t// Triangle strip vertices for each bar:\n\t\t// 0: bottom-left, 1: bottom-right, 2: top-left, 3: top-right\n\t\tfloat2 positions[4] = {\n\t\t\tfloat2(barCenterX - barWidth * 0.5, baseY),    // bottom-left\n\t\t\tfloat2(barCenterX + barWidth * 0.5, baseY),    // bottom-right\n\t\t\tfloat2(barCenterX - barWidth * 0.5, barTop),   // top-left\n\t\t\tfloat2(barCenterX + barWidth * 0.5, barTop)    // top-right\n\t\t};\n\t\t\n\t\t// UV coordinates for gradient application\n\t\tfloat2 uvs[4] = {\n\t\t\tfloat2(0.0, 0.0), // bottom-left\n\t\t\tfloat2(1.0, 0.0), // bottom-right\n\t\t\tfloat2(0.0, 1.0), // top-left\n\t\t\tfloat2(1.0, 1.0)  // top-right\n\t\t};\n\t\t\n\t\toutput.position = float4(positions[vertexInBar], 0.0, 1.0);\n\t\toutput.uv = uvs[vertexInBar];\n\t\t\n\t\t// Apply gradient based on appearance settings\n\t\tfloat gradientT;\n\t\tfloat positionFactor = float(barIndex) / float(numBars - 1);\n\t\tfloat heightFactor = (vertexInBar >= 2) ? averageHeight : 0.0; // Top vertices use height\n\t\t\n\t\t// Calculate gradient direction from angle\n\t\tfloat cosAngle = cos(appearance.gradientAngle);\n\t\tfloat sinAngle = sin(appearance.gradientAngle);\n\t\t\n\t\t// Interpolate based on angle:\n\t\t// 0° (horizontal) = pure positionFactor, 90° (vertical) = pure heightFactor\n\t\tgradientT = cosAngle * positionFactor + sinAngle * (1.0 - heightFactor);\n\t\tgradientT = clamp(gradientT, 0.0, 1.0);\n\t\t\n\t\t// Determine interpolation type based on dominant direction\n\t\tuint interpolationType = (abs(cosAngle) > abs(sinAngle)) ? Linear : Sigmoid;\n\t\t\n\t\tgradientT = applyGradientInterpolation(gradientT, interpolationType);\n\t\toutput.color = mix(appearance.fillColorStart, appearance.fillColorEnd, gradientT);\n\t\treturn output;\n\t}\n\t\n\t// Original SolidCurve implementation\n\tuint binIndex  = vertexId >> 1;\n\tuint vertexSide = vertexId & 1u;\n\n\tfloat4 histogramValues  = sampleHistSmooth(previousHistogram, currentHistogram, interpolation, (int)binIndex, appearance.smoothness);\n\tfloat  heightValue = channelHeight(channelIndex, histogramValues);\n\n\tfloat  ndcXPosition = normalizedDeviceCoordinateXFromBin(binIndex, channelIndex, histogramMode);\n\tfloat  yCurvePosition = normalizedDeviceCoordinateYFromHeight(heightValue);\n\tfloat  yBasePosition  = normalizedDeviceCoordinateYFromHeight(0.0);\n\n\toutput.position = float4(ndcXPosition, (vertexSide==0)? yBasePosition : yCurvePosition, 0, 1);\n\toutput.uv = float2(0.5, 0.5); // Default UV for non-bar rendering\n\n\tfloat positionFactor = float(binIndex) / 255.0;\n\tfloat heightFactor = (vertexSide == 0) ? 0.0 : heightValue;\n\n\t// Calculate gradient direction from angle\n\tfloat cosAngle = cos(appearance.gradientAngle);\n\tfloat sinAngle = sin(appearance.gradientAngle);\n\t\n\t// Interpolate based on angle:\n\t// 0° (horizontal) = pure positionFactor, 90° (vertical) = pure heightFactor\n\tfloat gradientT = cosAngle * positionFactor + sinAngle * (1.0 - heightFactor);\n\tgradientT = clamp(gradientT, 0.0, 1.0);\n\t\n\t// Determine interpolation type based on dominant direction\n\tuint interpolationType = (abs(cosAngle) > abs(sinAngle)) ? Linear : Sigmoid;\n\t\n\tgradientT = applyGradientInterpolation(gradientT, interpolationType);\n\toutput.color = mix(appearance.fillColorStart, appearance.fillColorEnd, gradientT);\n\treturn output;\n}\n\nvertex VSOut histogramVertex_Line(uint vertexId [[vertex_id]],\n\t\t\t\t\t\t\t\t  texture2d<float, access::sample> previousHistogram [[texture(0)]],\n\t\t\t\t\t\t\t\t  texture2d<float, access::sample> currentHistogram [[texture(1)]],\n\t\t\t\t\t\t\t\t  constant float &interpolation           [[buffer(0)]],\n\t\t\t\t\t\t\t\t  constant float2 &drawableSize           [[buffer(1)]],\n\t\t\t\t\t\t\t\t  constant uint &histogramMode            [[buffer(2)]],\n\t\t\t\t\t\t\t\t  constant uint &channelIndex             [[buffer(3)]],\n\t\t\t\t\t\t\t\t  constant ChannelAppearance &appearance  [[buffer(4)]],\n\t\t\t\t\t\t\t\t  constant float &displayScale            [[buffer(5)]],\n\t\t\t\t\t\t\t\t  constant uint &numberOfBars             [[buffer(6)]])\n{\n\tVSOut output;\n\n\t// Check if we should render bars (numberOfBars > 1) or solid curve\n\tif (numberOfBars > 1) {\n\t\t// Calculate bars per channel based on histogram mode\n\t\tuint barsPerChannel;\n\t\tif (histogramMode == RGBParade) {\n\t\t\t// In parade modes, divide total bars among 3 channels\n\t\t\tbarsPerChannel = numberOfBars / 3;\n\t\t} else {\n\t\t\t// In other modes, use all bars for the single display\n\t\t\tbarsPerChannel = numberOfBars;\n\t\t}\n\t\t\n\t\t// For bar mode, render outlines around each bar\n\t\tconst uint numBars = barsPerChannel;\n\t\tconst uint binsPerBar = HISTOGRAM_BIN_COUNT / numBars;\n\t\t\n\t\t// Each bar outline uses 8 vertices (4 vertices * 2 for line strip)\n\t\tuint barIndex = vertexId / 8;\n\t\tuint vertexInBarOutline = vertexId % 8;\n\t\t\n\t\t// If we exceed the number of bars, return degenerate vertex\n\t\tif (barIndex >= numBars) {\n\t\t\toutput.position = float4(0.0, 0.0, 0.0, 1.0);\n\t\t\toutput.uv = float2(0.0, 0.0);\n\t\t\toutput.color = float4(0.0, 0.0, 0.0, 0.0); // Transparent\n\t\t\treturn output;\n\t\t}\n\t\t\n\t\t// Sample histogram data for this bar - average across multiple bins\n\t\tfloat totalValue = 0.0;\n\t\tuint startBin = barIndex * binsPerBar;\n\t\tuint endBin = min(startBin + binsPerBar, uint(HISTOGRAM_BIN_COUNT));\n\t\t\n\t\tfor (uint binIndex = startBin; binIndex < endBin; binIndex++) {\n\t\t\tfloat4 histogramValues = sampleHistSmooth(previousHistogram, currentHistogram, interpolation, int(binIndex), appearance.smoothness);\n\t\t\ttotalValue += channelHeight(channelIndex, histogramValues);\n\t\t}\n\t\tfloat averageHeight = totalValue / float(endBin - startBin);\n\t\t\n\t\t// Calculate bar layout based on histogram mode\n\t\tfloat channelWidth, channelOffset;\n\t\t\n\t\tif (histogramMode == RGBParade) {\n\t\t\t// Add small gaps between channels in parade mode (matching normalizedDeviceCoordinateXFromBin)\n\t\t\tconst float gapWidth = 0.025; // Small gap between channels (1.25% of total width per gap)\n\t\t\tconst float totalGapWidth = gapWidth * 2.0; // Two gaps\n\t\t\tconst float availableWidth = 2.0 - totalGapWidth;\n\t\t\tchannelWidth = availableWidth / 3.0;\n\t\t\tchannelOffset = -1.0 + (float(channelIndex) * (channelWidth + gapWidth));\n\t\t} else {\n\t\t\tchannelWidth = 2.0;  // Full width\n\t\t\tchannelOffset = -1.0; // Starting position\n\t\t}\n\t\t\n\t\t// Calculate bar dimensions with spacing\n\t\tconst float spacingRatio = 0.3; // 30% spacing between bars (3x the original 10%)\n\t\tconst float barWidth = (channelWidth * (1.0 - spacingRatio)) / float(numBars);\n\t\tconst float barSpacing = (channelWidth * spacingRatio) / float(numBars + 1);\n\t\t\n\t\t// Calculate bar position\n\t\tfloat barCenterX = channelOffset + barSpacing + (barWidth * 0.5) + (float(barIndex) * (barWidth + barSpacing));\n\t\t\n\t\t// Calculate bar height based on histogram data (bottom-anchored)\n\t\tfloat baseY = -0.9;  // Bottom baseline\n\t\tfloat maxHeight = 1.7; // Maximum bar height in NDC\n\t\tfloat barTop = baseY + (averageHeight * maxHeight);\n\t\t\n\t\t// Calculate line thickness in NDC coordinates\n\t\tfloat2 pixelsToNdc = float2(2.0 / max(drawableSize.x, 1.0), 2.0 / max(drawableSize.y, 1.0));\n\t\tfloat scaledThickness = appearance.lineThickness * displayScale;\n\t\tfloat halfThickness = 0.5 * max(scaledThickness, 1.0);\n\t\tfloat2 thicknessOffset = halfThickness * pixelsToNdc;\n\t\t\n\t\t// Define bar corners with line thickness offset\n\t\tfloat leftX = barCenterX - (barWidth * 0.5);\n\t\tfloat rightX = barCenterX + (barWidth * 0.5);\n\t\t\n\t\t// Generate outline vertices (line strip around the bar perimeter)\n\t\t// Order: bottom-left -> bottom-right -> top-right -> top-left -> back to bottom-left (+ duplicates for strip)\n\t\tfloat2 outlinePositions[8] = {\n\t\t\tfloat2(leftX, baseY),          // 0: bottom-left\n\t\t\tfloat2(rightX, baseY),         // 1: bottom-right\n\t\t\tfloat2(rightX, barTop),        // 2: top-right\n\t\t\tfloat2(leftX, barTop),         // 3: top-left\n\t\t\tfloat2(leftX, baseY),          // 4: back to bottom-left (close rectangle)\n\t\t\tfloat2(leftX, baseY),          // 5: degenerate vertex\n\t\t\tfloat2(leftX, baseY),          // 6: degenerate vertex\n\t\t\tfloat2(leftX, baseY)           // 7: degenerate vertex\n\t\t};\n\t\t\n\t\toutput.position = float4(outlinePositions[vertexInBarOutline], 0.0, 1.0);\n\t\toutput.uv = float2(0.5, 0.5);\n\t\toutput.color = appearance.lineColor;\n\t\treturn output;\n\t}\n\t\n\t// Original SolidCurve implementation - trace the fill shape perimeter (no bottom edge)\n\t// Total vertices: left edge + curve + right edge (no bottom edge)\n\tuint totalVertices = HISTOGRAM_BIN_COUNT * 2 + 4; // curve + left/right edges only\n\tuint binIndex;\n\tfloat lineThicknessSide;\n\tfloat currentXPosition, currentYPosition;\n\t\n\tif (vertexId < 2) {\n\t\t// First 2 vertices: left edge from bottom to curve start (with inset)\n\t\tbinIndex = 0;\n\t\tfloat4 histogramValues = sampleHistSmooth(previousHistogram, currentHistogram, interpolation, 0, appearance.smoothness);\n\t\tfloat heightValue = channelHeight(channelIndex, histogramValues);\n\t\t\n\t\t// Apply 1-pixel inset to X position\n\t\tfloat baseXPosition = normalizedDeviceCoordinateXFromBin(0, channelIndex, histogramMode);\n\t\tfloat insetPixels = 1.0 * displayScale; // 1 pixel inset\n\t\tfloat2 pixelsToNdc = float2(2.0 / max(drawableSize.x, 1.0), 2.0 / max(drawableSize.y, 1.0));\n\t\tfloat insetNDC = insetPixels * pixelsToNdc.x;\n\t\tcurrentXPosition = baseXPosition + insetNDC;\n\t\t\n\t\tlineThicknessSide = (vertexId & 1u) ? 1.0 : -1.0;\n\t\tif (vertexId == 0) {\n\t\t\tcurrentYPosition = normalizedDeviceCoordinateYFromHeight(0.0); // bottom\n\t\t} else {\n\t\t\tcurrentYPosition = normalizedDeviceCoordinateYFromHeight(heightValue); // curve start\n\t\t}\n\t} else if (vertexId >= totalVertices - 2) {\n\t\t// Last 2 vertices: right edge from curve end to bottom (with inset)\n\t\tbinIndex = 255;\n\t\tfloat4 histogramValues = sampleHistSmooth(previousHistogram, currentHistogram, interpolation, 255, appearance.smoothness);\n\t\tfloat heightValue = channelHeight(channelIndex, histogramValues);\n\t\t\n\t\t// Apply 1-pixel inset to X position\n\t\tfloat baseXPosition = normalizedDeviceCoordinateXFromBin(255, channelIndex, histogramMode);\n\t\tfloat insetPixels = 1.0 * displayScale; // 1 pixel inset\n\t\tfloat2 pixelsToNdc = float2(2.0 / max(drawableSize.x, 1.0), 2.0 / max(drawableSize.y, 1.0));\n\t\tfloat insetNDC = insetPixels * pixelsToNdc.x;\n\t\tcurrentXPosition = baseXPosition - insetNDC;\n\t\t\n\t\tuint edgeVertexId = vertexId - (totalVertices - 2);\n\t\tlineThicknessSide = (edgeVertexId & 1u) ? 1.0 : -1.0;\n\t\tif (edgeVertexId == 0) {\n\t\t\tcurrentYPosition = normalizedDeviceCoordinateYFromHeight(heightValue); // curve end\n\t\t} else {\n\t\t\tcurrentYPosition = normalizedDeviceCoordinateYFromHeight(0.0); // bottom\n\t\t}\n\t} else {\n\t\t// Middle vertices: trace the histogram curve\n\t\tuint adjustedVertexId = vertexId - 2;\n\t\tbinIndex = adjustedVertexId >> 1;\n\t\tlineThicknessSide = (adjustedVertexId & 1u) ? 1.0 : -1.0;\n\t\t\n\t\tfloat4 currentValues = sampleHistSmooth(previousHistogram, currentHistogram, interpolation, (int)binIndex, appearance.smoothness);\n\t\tfloat currentYValue = channelHeight(channelIndex, currentValues);\n\t\tcurrentXPosition = normalizedDeviceCoordinateXFromBin(binIndex, channelIndex, histogramMode);\n\t\tcurrentYPosition = normalizedDeviceCoordinateYFromHeight(currentYValue);\n\t}\n\n\t// Calculate normal for line thickness\n\tfloat2 tangent, normal;\n\t\n\tif (vertexId < 2 || vertexId >= totalVertices - 2) {\n\t\t// For edge vertices, use horizontal normal for vertical lines\n\t\ttangent = float2(0.0, 1.0);\n\t\tif (vertexId < 2) {\n\t\t\tnormal = float2(1.0, 0.0); // Left edge normal points right\n\t\t} else {\n\t\t\tnormal = float2(-1.0, 0.0); // Right edge normal points left\n\t\t}\n\t} else {\n\t\t// Curve vertices: calculate normal from tangent\n\t\tint previousBinIndex = max(int(binIndex) - 1, 0);\n\t\tint nextBinIndex = min(int(binIndex) + 1, 255);\n\n\t\tfloat4 previousValues = sampleHistSmooth(previousHistogram, currentHistogram, interpolation, previousBinIndex, appearance.smoothness);\n\t\tfloat4 nextValues = sampleHistSmooth(previousHistogram, currentHistogram, interpolation, nextBinIndex, appearance.smoothness);\n\t\tfloat previousYValue = channelHeight(channelIndex, previousValues);\n\t\tfloat nextYValue = channelHeight(channelIndex, nextValues);\n\n\t\tfloat previousXPosition = normalizedDeviceCoordinateXFromBin((uint)previousBinIndex, channelIndex, histogramMode);\n\t\tfloat nextXPosition = normalizedDeviceCoordinateXFromBin((uint)nextBinIndex, channelIndex, histogramMode);\n\t\tfloat previousYPosition = normalizedDeviceCoordinateYFromHeight(previousYValue);\n\t\tfloat nextYPosition = normalizedDeviceCoordinateYFromHeight(nextYValue);\n\t\t\n\t\ttangent = normalize(float2(nextXPosition - previousXPosition, nextYPosition - previousYPosition) + float2(1e-6, 0.0));\n\t\tnormal = normalize(float2(-tangent.y, tangent.x));\n\t}\n\n\tfloat2 pixelsToNdc = float2(2.0 / max(drawableSize.x, 1.0), 2.0 / max(drawableSize.y, 1.0));\n\tfloat scaledThickness = appearance.lineThickness * displayScale;\n\tfloat halfThickness = 0.5 * max(scaledThickness, 1.0);\n\tfloat2 thicknessOffset = normal * halfThickness * pixelsToNdc;\n\n\toutput.position = float4(currentXPosition + lineThicknessSide * thicknessOffset.x,\n\t\t\t\t\t\t   currentYPosition + lineThicknessSide * thicknessOffset.y, 0, 1);\n\toutput.uv = float2(0.5, 0.5);\n\toutput.color = appearance.lineColor;\n\treturn output;\n}\n\nfragment float4 histogramFragment(VSOut in [[stage_in]])\n{\n\tfloat4 color = in.color;\n\t\n\t// Early discard for fully transparent pixels to ensure alpha is honored\n\tif (color.a <= 0.001) {\n\t\tdiscard_fragment();\n\t}\n\t\n\tcolor.rgb *= color.a; // premultiply\n\treturn color;\n}\n"
+ "%lu_%d"
+ "-[AVProVideoStorage _attemptReplenishWithCapacity:attemptCount:]"
+ "-[AVProVideoStorage _attemptReplenishWithCapacity:attemptCount:]_block_invoke"
+ "-[AVProVideoStorage _maximumCapacityComponentsIncludingPurgeableSpace:]"
+ "-[AVProVideoStorage _setCapacity:options:completion:]"
+ "-[AVProVideoStorage _updateBusyReasons:]"
+ "-[AVProVideoStorage replenishCapacityWithCompletionHandler:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RRM9P2/Sources/CameraCapture_AVF/AVFCapture/BW/Sources/AVCaptureConnection.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RRM9P2/Sources/CameraCapture_AVF/AVFCapture/BW/Sources/AVCaptureDevice.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RRM9P2/Sources/CameraCapture_AVF/AVFCapture/BW/Sources/AVCaptureVideoPreviewLayer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RRM9P2/Sources/CameraCapture_AVF/AVFCapture/BW/Sources/AVSpatialOverCaptureVideoPreviewLayer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RRM9P2/Sources/CameraCapture_AVF/AVFCapture/Common/Sources/AVCaptureCommon.m %s: could not determine proprietary defaults domain for %{private}@, so using unknown"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RRM9P2/Sources/CameraCapture_AVF/AVFCapture/Common/Sources/AVCaptureCommon.m %s: not caching \"unknown\" proprietary defaults domain for %{private}@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RRM9P2/Sources/CameraCapture_AVF/AVFCapture/Common/Sources/AVControlCenterModules.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RRM9P2/Sources/CameraCapture_AVF/AVFCapture/Tundra/Sources/AVCaptureDevice.m"
+ "<<<< AVCapturePhotoOutput >>>> %s: Client requested highResolutionPhotoEnabled on photo output: %@ but highResolutionCaptureEnabled is NO, correcting highResolutionPhotoEnabled to NO on client's photo settings %@"
+ "<<<< AVControlCenterModules >>>> %s: %{public}@ active:0 It's in the mic mode specific disallow list"
+ "<<<< AVProVideoStorage >>>>"
+ "<<<< AVProVideoStorage >>>> %s: Error (%d) creating capture card"
+ "<<<< AVProVideoStorage >>>> %s: Failed to cancel set capacity (err=%d)"
+ "<<<< AVProVideoStorage >>>> %s: Failed to perform recovery (err=%d)"
+ "<<<< AVProVideoStorage >>>> %s: Failed to reconnect to server"
+ "<<<< AVProVideoStorage >>>> %s: Failed to send garbage collection hint (err=%d)"
+ "<<<< AVProVideoStorage >>>> %s: Garbage collection hint sent successfully"
+ "<<<< AVProVideoStorage >>>> %s: Invoking replenish completion handler with reconnectToServer."
+ "<<<< AVProVideoStorage >>>> %s: Invoking setCapacity completion handler with reconnectToServer."
+ "<<<< AVProVideoStorage >>>> %s: Received %@:%@"
+ "<<<< AVProVideoStorage >>>> %s: Requested capacity (%lld) is larger than maximum available capacity (%lld)."
+ "<<<< AVProVideoStorage >>>> %s: Unable to allocate/init AVProVideoStorage"
+ "<<<< AVProVideoStorage >>>> %s: Unable to copy property 'hasOpenedSettings'"
+ "<<<< AVProVideoStorage >>>> %s: Unable to copy property 'initialCapacity'"
+ "<<<< AVProVideoStorage >>>> %s: Unable to copy property 'maximumCapacityComponents'"
+ "<<<< AVProVideoStorage >>>> %s: Unable to copy property 'remainingCapacity'"
+ "<<<< AVProVideoStorage >>>> %s: Unable to show system user interface"
+ "<<<< AVProVideoStorage >>>> %s: [%@] Ignoring BusyReasonsChanged payload with negative bitmask (%d)"
+ "<<<< AVProVideoStorage >>>> %s: [%@] IsBusy property returned %d"
+ "<<<< AVProVideoStorage >>>> %s: [%@] Replenish attempt %lu/%lu, target=%lld"
+ "<<<< AVProVideoStorage >>>> %s: [%@] Replenishing capacity: target=%lld"
+ "<<<< AVProVideoStorage >>>> %s: [%@] Returning initialCapacity %ld"
+ "<<<< AVProVideoStorage >>>> %s: [%@] Returning maximum capacity %ld"
+ "<<<< AVProVideoStorage >>>> %s: [%@] Returning performRecoveryWithForce:%d result=%d"
+ "<<<< AVProVideoStorage >>>> %s: [%@] Returning remainingCapacity %ld"
+ "<<<< AVProVideoStorage >>>> %s: [%@] Setting new capacity to %lli (replenishMode=%d)"
+ "<<<< AVProVideoStorage >>>> %s: [%@] Syncing BusyReasons from server: 0x%x (err=%d)"
+ "<<<< AVProVideoStorage >>>> %s: [%@] Syncing IsRecoveryRequired from server: %d (err=%d)"
+ "<<<< AVProVideoStorage >>>> %s: [%@] Updating busyReasons KVO: %@ -> %@"
+ "<<<< AVProVideoStorage >>>> %s: [%@] Updating recoveryRequired KVO: %d -> %d"
+ "<<<< AVProVideoStorage >>>> %s: [%@] _attemptReplenish skipped: no replenish in progress"
+ "<<<< AVProVideoStorage >>>> %s: [%@] allocation callback statusError=%d"
+ "<<<< AVProVideoStorage >>>> %s: [%@] cancelSetCapacity returned with err=%d"
+ "<<<< AVProVideoStorage >>>> %s: [%@] hasOpenedSettings property returned %d"
+ "<<<< AVProVideoStorage >>>> %s: [%@] isRecoveryRequired property returned %d"
+ "<<<< AVProVideoStorage >>>> %s: [%@] replenish attempt %lu failed (%@); retrying"
+ "<<<< AVProVideoStorage >>>> %s: [%@] replenish attempt would target non-positive capacity (%lld); finalizing as failure"
+ "<<<< AVProVideoStorage >>>> %s: [%@] replenish exhausted %lu attempts (last err=%@)"
+ "<<<< AVProVideoStorage >>>> %s: [%@] replenish marked busy"
+ "<<<< AVProVideoStorage >>>> %s: [%@] replenishCapacityWithCompletionHandler returned err=%d"
+ "<<<< AVProVideoStorage >>>> %s: [%@] sendGarbageCollectionHint returned with err=%d"
+ "<<<< AVProVideoStorage >>>> %s: [%@] setCapacity callback called %d"
+ "<<<< AVProVideoStorage >>>> %s: [%@] setCapacity marked busy, capacity=%lli"
+ "<<<< AVProVideoStorage >>>> %s: [%@] setCapacity method returned with %lld"
+ "<<<< AVProVideoStorage >>>> %s: [%@] showSystemUserInterface called %d"
+ "<<<< AVProVideoStorage >>>> %s: cancelSetCapacity called successfully"
+ "<<<< AVProVideoStorage >>>> %s: maximumCapacityComponents property returned NULL"
+ "<<<< AVProVideoStorage >>>> %s: performRecoveryWithForce:%d called successfully"
+ "<<<< AVProVideoStorage >>>> %s: setting up VCC %@"
+ "<<<< AVProVideoStorage >>>> %s: tearing down VCC %@"
+ "AVCaptureVideoAnalyticsAdaptor.FrameCommandBuffer"
+ "AVCaptureVideoAnalyticsAdaptor.SharedCommandQueue"
+ "AVCaptureVideoAnalyticsAdaptor.m"
+ "AVGQIV52D6ZY6YNMNKTM3AFFHYPXPM"
+ "AVProVideoStorageBusyReasonAdjustingCapacity"
+ "AVProVideoStorageBusyReasonCapturing"
+ "AVProVideoStorageBusyReasonReplenishing"
+ "Build Filament Precursor"
+ "Build Filament Vertices"
+ "Build Indirect Args"
+ "Display Link Histogram Render"
+ "Histogram Compute"
+ "Histogram Render"
+ "LastShownBuild:AVCaptureConnection.m:857"
+ "LastShownDate:AVCaptureConnection.m:857"
+ "Pro Video Storage has not been configured with an initial capacity."
+ "Pro Video Storage is busy."
+ "Render Filament Geometry"
+ "Unable to fetch maximumCapacityComponentsExcludingPurgeable."
+ "Waveform Filament Precursor"
+ "Waveform Filament Vertex Buffer"
+ "Waveform Filament Vertex Count"
+ "Waveform Indirect Draw Arguments"
+ "[AVCVAA] CIContext render threw %{public}@: %{public}@"
+ "[AVCVAA] Dropping frame: %d in-flight frames already queued"
+ "[AVCVAA] Dropping frame: CG ingest ring full (%d slots in flight)"
+ "[AVCVAA] Dropping frame: CI output ring full"
+ "[AVCVAA] First frame: %zux%zu, pixelFormat=0x%08X ('%s'), planar=%d, planes=%zu"
+ "[AVCVAA] Renderer %@ committed the shared command buffer. Renderers must encode only; the adaptor commits."
+ "busyReasons"
+ "com.apple.avfoundation.videoadaptor"
+ "com.apple.avfoundation.videoadaptor.sampleprocessing"
+ "com.apple.inputmethod.ironwood"
+ "computeHistogram"
+ "description=CameraCapture_AVF-758.0.0.0.1"
+ "histogramFragment"
+ "histogramVertex_Fill"
+ "histogramVertex_Line"
+ "normalizeHistogramToTexture"
+ "signpost"
+ "v12@?0I8"
+ "v16@?0@\"<MTLCommandBuffer>\"8"
+ "v16@?0@\"NSError\"8"
+ "v16@?0@\"NSMutableSet\"8"
+ "waveform_build_filament_vertices"
+ "waveform_build_indirect_args"
+ "waveform_build_precursor"
+ "waveform_filament_fragment"
+ "waveform_filament_vertex"
- "-[AVProVideoStorage _updateBusy:]"
- "-[AVProVideoStorage maximumCapacity]"
- "-[AVProVideoStorage setCapacity:completion:]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nDbxbx/Sources/CameraCapture_AVF/AVFCapture/BW/Sources/AVCaptureConnection.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nDbxbx/Sources/CameraCapture_AVF/AVFCapture/BW/Sources/AVCaptureDevice.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nDbxbx/Sources/CameraCapture_AVF/AVFCapture/BW/Sources/AVCaptureVideoPreviewLayer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nDbxbx/Sources/CameraCapture_AVF/AVFCapture/BW/Sources/AVSpatialOverCaptureVideoPreviewLayer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nDbxbx/Sources/CameraCapture_AVF/AVFCapture/Common/Sources/AVCaptureCommon.m %s: could not determine proprietary defaults domain for %{private}@, so using unknown"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nDbxbx/Sources/CameraCapture_AVF/AVFCapture/Common/Sources/AVCaptureCommon.m %s: not caching \"unknown\" proprietary defaults domain for %{private}@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nDbxbx/Sources/CameraCapture_AVF/AVFCapture/Common/Sources/AVControlCenterModules.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nDbxbx/Sources/CameraCapture_AVF/AVFCapture/Tundra/Sources/AVCaptureDevice.m"
- "<<<< AVVirtualCaptureCard >>>>"
- "<<<< AVVirtualCaptureCard >>>> %s: Error (%d) creating capture card"
- "<<<< AVVirtualCaptureCard >>>> %s: Failed to cancel set capacity (err=%d)"
- "<<<< AVVirtualCaptureCard >>>> %s: Failed to perform recovery (err=%d)"
- "<<<< AVVirtualCaptureCard >>>> %s: Failed to reconnect to server"
- "<<<< AVVirtualCaptureCard >>>> %s: Failed to send garbage collection hint (err=%d)"
- "<<<< AVVirtualCaptureCard >>>> %s: Garbage collection hint sent successfully"
- "<<<< AVVirtualCaptureCard >>>> %s: Invoking setCapacity completion handler with reconnectToServer."
- "<<<< AVVirtualCaptureCard >>>> %s: Received %@:%@"
- "<<<< AVVirtualCaptureCard >>>> %s: Requested capacity (%lld) is larger than maximum available capacity (%lld)."
- "<<<< AVVirtualCaptureCard >>>> %s: Unable to allocate/init AVProVideoStorage"
- "<<<< AVVirtualCaptureCard >>>> %s: Unable to copy property 'capacity'"
- "<<<< AVVirtualCaptureCard >>>> %s: Unable to copy property 'hasOpenedSettings'"
- "<<<< AVVirtualCaptureCard >>>> %s: Unable to copy property 'initialCapacity'"
- "<<<< AVVirtualCaptureCard >>>> %s: Unable to copy property 'remainingCapacity'"
- "<<<< AVVirtualCaptureCard >>>> %s: Unable to show system user interface"
- "<<<< AVVirtualCaptureCard >>>> %s: [%@] Attempted to set capacity to a value equal to current capacity. Doing nothing."
- "<<<< AVVirtualCaptureCard >>>> %s: [%@] IsBusy property returned %d"
- "<<<< AVVirtualCaptureCard >>>> %s: [%@] Returning initialCapacity %ld"
- "<<<< AVVirtualCaptureCard >>>> %s: [%@] Returning maximum capacity %ld"
- "<<<< AVVirtualCaptureCard >>>> %s: [%@] Returning performRecoveryWithForce:%d result=%d"
- "<<<< AVVirtualCaptureCard >>>> %s: [%@] Returning remainingCapacity %ld"
- "<<<< AVVirtualCaptureCard >>>> %s: [%@] Setting new capacity to %lli"
- "<<<< AVVirtualCaptureCard >>>> %s: [%@] Syncing IsBusy from server: %d (err=%d)"
- "<<<< AVVirtualCaptureCard >>>> %s: [%@] Syncing IsRecoveryRequired from server: %d (err=%d)"
- "<<<< AVVirtualCaptureCard >>>> %s: [%@] Updating busy KVO: %d -> %d"
- "<<<< AVVirtualCaptureCard >>>> %s: [%@] Updating recoveryRequired KVO: %d -> %d"
- "<<<< AVVirtualCaptureCard >>>> %s: [%@] allocation callback wasBusy=%d statusError=%d"
- "<<<< AVVirtualCaptureCard >>>> %s: [%@] cancelSetCapacity returned with err=%d"
- "<<<< AVVirtualCaptureCard >>>> %s: [%@] hasOpenedSettings property returned %d"
- "<<<< AVVirtualCaptureCard >>>> %s: [%@] isRecoveryRequired property returned %d"
- "<<<< AVVirtualCaptureCard >>>> %s: [%@] sendGarbageCollectionHint returned with err=%d"
- "<<<< AVVirtualCaptureCard >>>> %s: [%@] setCapacity callback called %d"
- "<<<< AVVirtualCaptureCard >>>> %s: [%@] setCapacity marked busy, capacity=%lli"
- "<<<< AVVirtualCaptureCard >>>> %s: [%@] setCapacity method returned with %lld"
- "<<<< AVVirtualCaptureCard >>>> %s: [%@] showSystemUserInterface called %d"
- "<<<< AVVirtualCaptureCard >>>> %s: cancelSetCapacity called successfully"
- "<<<< AVVirtualCaptureCard >>>> %s: performRecoveryWithForce:%d called successfully"
- "<<<< AVVirtualCaptureCard >>>> %s: setting up VCC %@"
- "<<<< AVVirtualCaptureCard >>>> %s: tearing down VCC %@"
- "Capturing ProRes on this device requires Virtual Capture Card. Set usesVirtualCaptureCard = YES or capture to external storage device."
- "LastShownBuild:AVCaptureConnection.m:831"
- "LastShownDate:AVCaptureConnection.m:831"
- "description=CameraCapture_AVF-753.0.0.121.4"

```
