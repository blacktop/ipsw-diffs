## ACTFramework

> `/System/Library/PrivateFrameworks/ACTFramework.framework/ACTFramework`

```diff

-511.100.2.0.0
-  __TEXT.__text: 0x39a60
-  __TEXT.__auth_stubs: 0x14e0
-  __TEXT.__objc_methlist: 0x14b8
-  __TEXT.__const: 0xe50
-  __TEXT.__cstring: 0x447d
+535.0.0.0.0
+  __TEXT.__text: 0x3645c
+  __TEXT.__auth_stubs: 0x1470
+  __TEXT.__objc_methlist: 0x1508
+  __TEXT.__const: 0xdc0
+  __TEXT.__cstring: 0x3644
+  __TEXT.__gcc_except_tab: 0x18
   __TEXT.__oslogstring: 0x44f
-  __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__unwind_info: 0x970
-  __TEXT.__objc_classname: 0x1d4
-  __TEXT.__objc_methname: 0x40b2
-  __TEXT.__objc_methtype: 0xfc2
-  __TEXT.__objc_stubs: 0x2340
-  __DATA_CONST.__got: 0x378
-  __DATA_CONST.__const: 0x630
-  __DATA_CONST.__objc_classlist: 0x80
+  __TEXT.__unwind_info: 0x8d8
+  __TEXT.__objc_classname: 0x20f
+  __TEXT.__objc_methname: 0x41b8
+  __TEXT.__objc_methtype: 0x10d6
+  __TEXT.__objc_stubs: 0x22e0
+  __DATA_CONST.__got: 0x3a0
+  __DATA_CONST.__const: 0x448
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc78
-  __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0xa80
-  __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x1a80
-  __AUTH_CONST.__objc_const: 0x4a98
-  __AUTH_CONST.__objc_intobj: 0x150
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x39c
-  __DATA.__data: 0x200
-  __DATA.__bss: 0x80
-  __DATA.__common: 0x11
-  __DATA_DIRTY.__objc_data: 0x460
-  __DATA_DIRTY.__bss: 0x20
-  __DATA_DIRTY.__common: 0x48
+  __DATA_CONST.__objc_selrefs: 0xc70
+  __DATA_CONST.__objc_superrefs: 0x80
+  __AUTH_CONST.__auth_got: 0xa48
+  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__cfstring: 0x1a20
+  __AUTH_CONST.__objc_const: 0x5400
+  __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x400
+  __DATA.__data: 0x180
+  __DATA.__bss: 0x70
+  __DATA_DIRTY.__objc_data: 0x4b0
+  __DATA_DIRTY.__common: 0x68
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B167CBD2-58CD-3087-91AD-1BFE6DAB9AD2
-  Functions: 945
-  Symbols:   975
-  CStrings:  1600
+  UUID: C3E09DEE-44C2-35C3-83DF-7A94D33A57C8
+  Functions: 903
+  Symbols:   964
+  CStrings:  1548
 
Symbols:
+ _ACT_getHostTime
+ _CGRectZero
+ _FigSignalErrorAtGM
+ _LegacyPano_copyProperty
+ _LegacyPano_createProcessor
+ _LegacyPano_finishProcessing
+ _LegacyPano_invalidate
+ _LegacyPano_processSampleBuffer
+ _LegacyPano_reset
+ _LegacyPano_stopCapture
+ _OBJC_CLASS_$_ButterworthHighPassFilter
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_PanoramaMiniPreviewOutput
+ _OBJC_CLASS_$_PanoramaRectanglingStage
+ _OBJC_METACLASS_$_ButterworthHighPassFilter
+ _OBJC_METACLASS_$_PanoramaMiniPreviewOutput
+ _OBJC_METACLASS_$_PanoramaRectanglingStage
+ _RobustPano_createProcessor
+ __addFileWithData
+ _assemblyThread
+ _calculateHalfResolution
+ _calculateHalfResolutionWithVector2
+ _debugWriteThread
+ _getCVPixelFormat
+ _getChromaMTLPixelFormat
+ _getLumaMTLPixelFormat
+ _kACTPanoramaVerticalDriftFilterWeight
+ _kFigCapturePortType_FrontFacingCamera
+ _kFigNRFSampleBufferProcessorOption_PrepareForProcessingTypes
+ _kVTPixelRotationPropertyKey_FlipHorizontalOrientation
+ _noiseReductionThread
+ _previewThread
+ _registrationThread
+ _sbp_pano_getStorage
+ _setDownscaledResolution
+ _tan
+ _transformToHomography
+ _translationToHomography
- _ACT_FigSampleBufferProcessorCreateForPanoramaWithOptionsAndPreviewScale
- _CFStringGetCStringPtr
- _CFStringGetLength
- _CFStringGetSystemEncoding
- _CMTimeMake
- _FastRegistration_compareSignatures
- _FastRegistration_computePaddedRowByteSize
- _FastRegistration_computeSignatures
- _FastRegistration_getStatusDescription
- _FastRegistration_initRoi
- _FastRegistration_isRoiInImage
- _FastRegistration_register
- _FastRegistration_statusDescription
- _FastRegistration_vImageBufferFree
- _FastRegistration_vImageBufferMalloc
- _FigSignalErrorAt3
- _GetHostTime
- _OBJC_CLASS_$_PanoramaPreviewOutput
- _OBJC_METACLASS_$_PanoramaPreviewOutput
- _Projections_computeMeanStdTable
- _Projections_computeProjectionDerivative
- _Projections_computeProjectionLineRegressionQuality
- _Projections_computeShiftBruteForce
- _Projections_computeShiftDescent
- _Projections_fastRecSqrtf
- _Projections_fastSqrtf
- _Projections_getStatusDescription
- _Projections_isZero
- _Projections_normalizeMeanStdUsingTable
- _Projections_projectionCols_planar8UtoF
- _Projections_projectionRowsCols_planar8UtoF
- _Projections_projectionRows_planar8UtoF
- _Projections_smoothProjection
- _Projections_statusDescription
- _RobustPano_cropRect
- _RobustPano_new
- _USE_ISP_MOTION
- ___sincosf_stret
- ___stdoutp
- __invalidateDebugWriteThread
- _addOrReplaceKeyValueToTargetDictionary
- _allocateSignatureBuffers
- _dispatch_barrier_sync
- _getHostTime
- _kACTPanoramaPreviewThumbnailAttachmentKey
- _kACTPanoramaPreviewThumbnailJPEGSizeAttachmentKey
- _kACTPanoramaThumbnailAttachmentKey
- _vDSP_vabs
- _vDSP_vflt32
CStrings:
+ "%s signalled err=%d at <>:%d"
+ "*"
+ "-[PanoramaGyroStage update:sliceType:sliceID:]"
+ "-[PanoramaProcessor addFrame:registrationCallback:]_block_invoke"
+ "/Library/Caches/com.apple.xbs/Sources/ACTFramework/LegacyPano/ABReg.c"
+ "/Library/Caches/com.apple.xbs/Sources/ACTFramework/LegacyPano/ACTRegistration.c"
+ "/Library/Caches/com.apple.xbs/Sources/ACTFramework/LegacyPano/Projections.c"
+ "/Library/Caches/com.apple.xbs/Sources/ACTFramework/Utilities/ACTDataDump.c"
+ "@\"ButterworthHighPassFilter\""
+ "@\"NSString\""
+ "@\"PanoramaMiniPreviewOutput\""
+ "@\"PanoramaRectanglingStage\""
+ "@24@0:8f16f20"
+ "@28@0:8@16i24"
+ "@88@0:8{?=QQQQBiiffffBBi}16"
+ "@96@0:8@16{?=QQQQBiiffffBBi}24"
+ "ACTPanoramaRobustPanoDisableCropping"
+ "ACTPanoramaVerticalDriftFilterWeight"
+ "ButterworthHighPassFilter"
+ "Common"
+ "CropRect"
+ "NRFParameters"
+ "PanoramaMiniPreviewOutput"
+ "PanoramaRectanglingStage"
+ "T@\"<MTLTexture>\",&,N,V_outputMask"
+ "T@\"PanoramaMiniPreviewOutput\",&,N,V_miniPreviewOutput"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_boundingBox"
+ "Version"
+ "_CVPixelFormat"
+ "_MTLPixelFormatUV"
+ "_MTLPixelFormatY"
+ "_a"
+ "_atlasFilter"
+ "_b"
+ "_bitDepth"
+ "_boundingBox"
+ "_commonInitWithContext:sliceWidth:sliceHeight:bitDepth:"
+ "_createDummyOutputWidth:height:"
+ "_curMetadata"
+ "_curPixbufToStitch"
+ "_gyroMode"
+ "_hasStitchedSlicesWithNoError"
+ "_mask"
+ "_maskHeight"
+ "_maskWidth"
+ "_miniPreviewOutput"
+ "_order"
+ "_panoHeight"
+ "_panoWidth"
+ "_params"
+ "_portType"
+ "_rectanglingMode"
+ "_rectanglingStage"
+ "_transformMatrixAccumulatedForFinal"
+ "_transformMatrixAccumulatedForMini"
+ "_txtyAccumulatedForFinal"
+ "_txtyAccumulatedForMini"
+ "_x"
+ "_y"
+ "addSlice:metadata:sliceHomography:stitchingMask:roi:sliceType:"
+ "adjustBoundingBox"
+ "boundingBox"
+ "calculateCoefficientsWithCutoff:sampleRate:"
+ "cropAPI:"
+ "cropAPI:initialRect:"
+ "cropWithInitialRect:"
+ "currentAccumulatedHomographyForThread:"
+ "dataWithBytes:length:"
+ "dictionary"
+ "downsample:to:inputBitDepth:outputBitDepth:"
+ "encodedFinalAsset"
+ "f20@0:8f16"
+ "filterSample:"
+ "getCropRect"
+ "getMaskAsBuffer:bufferOut:widthOut:heightOut:"
+ "i124@0:8^{__CVBuffer=}16@24{?=[3]}32@80{CGRect={CGPoint=dd}{CGSize=dd}}88i120"
+ "i36@0:8@16i24Q28"
+ "i36@0:8i16Q20Q28"
+ "i40@0:8^{__CVBuffer=}16^{__CVBuffer=}24i32i36"
+ "i44@0:8@16Q24Q32i40"
+ "i48@0:8@16^*24^i32^i40"
+ "i52@0:8i16Q20Q28Q36Q44"
+ "i56@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24"
+ "i88@0:8{?=QQQQBiiffffBBi}16"
+ "initWithCommandQueue:"
+ "initWithContext:bitDepth:"
+ "initWithCutoffFrequency:sampleRate:"
+ "isEqualToString:"
+ "miniPreviewOutput"
+ "numberWithUnsignedLong:"
+ "outputMask"
+ "prepareToProcess:sliceWidth:sliceHeight:"
+ "prepareToProcess:sliceWidth:sliceHeight:gridWidth:gridHeight:"
+ "prepareToProcessWithDevice:library:commandQueue:width:height:"
+ "setBoundingBox:"
+ "setMiniPreviewOutput:"
+ "setOutputMask:"
+ "setParameters:"
+ "update:sliceType:sliceID:"
+ "v24@0:8f16f20"
+ "{?=\"sliceWidth\"Q\"sliceHeight\"Q\"panoWidth\"Q\"panoHeight\"Q\"enableTranslationCorrection\"B\"movingAverageFilterSize\"i\"referenceMeanStartingFrame\"i\"atlasTranslationShiftLowThreshold\"f\"atlasTranslationShiftHighThreshold\"f\"atlasTranslationCorrectionStrength\"f\"verticalDriftFilterWeight\"f\"useNRFTypePano\"B\"disableCropping\"B\"bitDepth\"i}"
+ "{?=[3]}20@0:8i16"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "{Default|direction:%d}\n"
- "!!! you should not read this !!!"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "-[MetalContext bindIOSurfaceToMTL2DTexture:pixelFormat:width:height:plane:]"
- "-[MetalContext bindPixelBufferToMTL2DTexture:pixelFormat:plane:]"
- "-[MetalContext bindPixelBufferToMTL2DTexture:pixelFormat:textureSize:plane:]"
- "-[MetalContext initWithDevice:library:commandQueue:]"
- "-[MetalContext init]"
- "-[PanoramaGyroStage update:sliceType:sliceWidth:sliceHeight:sliceID:]"
- "-[PanoramaProcessor addFrame:registrationCallback:]_block_invoke_2"
- "/Library/Caches/com.apple.xbs/Sources/ACTFramework/ABReg.c"
- "/Library/Caches/com.apple.xbs/Sources/ACTFramework/ACTDataDump.c"
- "/Library/Caches/com.apple.xbs/Sources/ACTFramework/ACTRegistration.c"
- "/Library/Caches/com.apple.xbs/Sources/ACTFramework/Projections.c"
- "/Library/Caches/com.apple.xbs/Sources/ACTFramework/Video/Projections/FastRegistration_Core.c"
- "/Library/Caches/com.apple.xbs/Sources/ACTFramework/Video/Projections/Projections_Core.c"
- "/Library/Caches/com.apple.xbs/Sources/ACTFramework/Video/Projections/Projections_Optimizer.c"
- "@\"PanoramaPreviewOutput\""
- "@64@0:8{?=QQBiifffiB}16"
- "@72@0:8@16{?=QQBiifffiB}24"
- "ACTPanoramaPreviewThumbnail"
- "ACTPanoramaPreviewThumbnailJPEGSize"
- "ACTPanoramaRobustPanoNRFversion"
- "ACTPanoramaThumbnail"
- "ACTThread.c"
- "ACTThreadCreate"
- "ACT_FigSampleBufferProcessorCreateForPanoramaWithOptions"
- "ACT_FigSampleBufferProcessorCreateForPanoramaWithOptionsAndPreviewSize"
- "BandPassNoiseReduction.c"
- "Cannot create an MTLCommandQueue."
- "Cannot create an MTLDevice."
- "Cannot create an MTLLibrary."
- "D93"
- "D94"
- "DebugMotionDataFromISP"
- "DoBandPassNoiseReductionComplete"
- "FastRegistration error %d:%s in %s @ %s:%d\n"
- "FastRegistration_status FastRegistration_computeSignatures(const vImage_Buffer *, _Bool, dispatch_queue_t, FastRegistration_Signatures *)"
- "FastRegistration_status FastRegistration_processProjections(float *, vImagePixelCount)"
- "FastRegistration_status FastRegistration_register(const FastRegistration_Signatures *, const FastRegistration_Signatures *, float, dispatch_queue_t, float *, float *, float *, float *)"
- "FigSampleBufferProcessor_Panorama.c"
- "Final edge: top: %d, bottom: %d, left: %d, right: %d \n"
- "FocalLenIn35mmFilm"
- "FrameID:%04d time %.3f: gyro updated with debug motion data\n"
- "IOsurface height is smaller than texture height"
- "IOsurface width is smaller than texture width"
- "ISPMotionToHomography"
- "MetalContext.m"
- "NULL options"
- "NULL outProcessor"
- "NULL propertyValueOut"
- "PanoramaPreviewOutput"
- "Print out once crop ratio 0.0: %f \n"
- "Projections error %d:%s in %s @ %s:%d\n"
- "Projections_status Projections_computeCost(int, float, float, const float *, int, const Projections_meanStdTable *, const float *, int, const Projections_meanStdTable *, int, float *)"
- "Projections_status Projections_computeProjectionDerivative(const float *, int, float *)"
- "Projections_status Projections_computeShiftBruteForce(const float *, int, const Projections_meanStdTable *, const float *, int, const Projections_meanStdTable *, int, float, float *, float *, float *, float *)"
- "Projections_status Projections_computeShiftDescent(const float *, int, const Projections_meanStdTable *, const float *, int, const Projections_meanStdTable *, int, float *, float *)"
- "Projections_status Projections_projectionRowsCols_planar8UtoF(const uint8_t *, int, int, size_t, float *, float *)"
- "T@\"PanoramaPreviewOutput\",&,N,V_previewOutput"
- "Ti,N,V_assemblyMode"
- "Ti,N,V_stitchingMode"
- "Unable to create MTLTexture"
- "Unable to create MTLTextureDescriptor"
- "_accumulatedInitialHomography"
- "_commonInitWithContext:NRFversion:"
- "_createDebugWriteThread"
- "_createDummyOutput"
- "_curTime"
- "_currentInitialHomography"
- "_focalLength"
- "_isTranslationValid"
- "_lastMetadata"
- "_outputAtlasHomography"
- "_panoramaParams"
- "_previewOutput"
- "_rotation"
- "_transformMatrix"
- "_translation"
- "_translationRate"
- "addSlice:metadata:sliceHomography:stitchingMask:motionCue:roi:sliceType:"
- "assemblyMode"
- "autocropMask"
- "compare:"
- "could not create ACTThread mutex"
- "could not create ACTThread semaphore"
- "could not create ACTThread thread"
- "could not create helperThread"
- "d"
- "downsample:to:"
- "encodedResult"
- "error creating assemblyThread"
- "error creating debugWriteThread"
- "error creating noiseReductionThread"
- "error creating previewThread"
- "error creating registrationThread"
- "error with the projections computation"
- "function not implemented"
- "getMaskAsBuffer:widthOut:heightOut:"
- "getRegistrationWidth:height:"
- "i132@0:8^{__CVBuffer=}16@24{?=[3]}32@80@88{CGRect={CGPoint=dd}{CGSize=dd}}96i128"
- "i24@0:8^{?=II[0{?=QQS(?=[64C]{?=SSiiiiiiiiii}{?=SSiiiiiiiiiiiiiiSSiiii})}]}16"
- "i28@0:8@16i24"
- "i36@0:8I16Q20Q28"
- "i40@0:8@16i24f28f32i36"
- "i40@0:8^*16^Q24^Q32"
- "i48@0:8Q16Q24Q32Q40"
- "i64@0:8{?=QQBiifffiB}16"
- "initWithCapacity:"
- "internal error"
- "invalid option"
- "invalid parameter"
- "kFigBaseObjectError_AllocationFailed"
- "kFigBaseObjectError_ParamErr"
- "memory allocation error"
- "metalContext"
- "numberWithInt:"
- "objectAtIndex:"
- "ok"
- "out of boundaries"
- "out of bounds error"
- "pixelBuffer does not contain an IOSurface"
- "prepareRegistrationWithDevice:library:commandQueue:width:height:"
- "prepareToProcess:sliceHeight:"
- "prepareToProcessPanoWidth:panoHeight:"
- "prepareToProcessSliceWidth:sliceHeight:stagingWidth:stagingHeight:"
- "prepareToProcess_PanoSpecific:frameWidth:frameHeight:"
- "previewOutput"
- "projectionCols_planar8UtoF"
- "projectionRows_planar8UtoF"
- "refineInitialHomography:"
- "robustPano.disableV1"
- "sbp_pano_copyProperty"
- "setAssemblyMode:"
- "setPanoramaParameters:"
- "setPreviewOutput:"
- "setStitchingMode:"
- "sortedArrayUsingSelector:"
- "stitchingMode"
- "stock_pano.jpg"
- "swingData.csv"
- "toHomography"
- "transformToHomography"
- "translationToHomography"
- "update:sliceType:sliceWidth:sliceHeight:sliceID:"
- "updateWithDebugISPMedian:"
- "v32@0:8^Q16^Q24"
- "vImage error"
- "{?=\"frameWidth\"Q\"frameHeight\"Q\"enableTranslationCorrection\"B\"movingAverageFilterSize\"i\"referenceMeanStartingFrame\"i\"atlasTranslationShiftLowThreshold\"f\"atlasTranslationShiftHighThreshold\"f\"atlasTranslationCorrectionStrength\"f\"NRFversion\"i\"useNRFTypePano\"B}"
- "{?=[3]}64@0:8{?=[3]}16"
- "{Finishing|EndTS:%.3f} {Finishing|TotalTime:%.3f}\n"
- "{Finishing|ThumbnailCreationTime:%.3f}\n"
- "{Finishing|ThumbnailMaxWidth:%d}{Finishing|ThumbnailMaxHeight:%d}{Finishing|ThumbnailScale:%f}{Finishing|ThumbnailWidth:%f}{Finishing|ThumbnailHeight:%f}\n"
- "{SwingEstimator|direction:%d}\n"

```
