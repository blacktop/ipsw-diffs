## VideoEffect

> `/System/Library/PrivateFrameworks/VideoEffect.framework/VideoEffect`

```diff

-2.10.0.0.0
-  __TEXT.__text: 0x9eec
-  __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_methlist: 0x894
-  __TEXT.__const: 0x1b2
-  __TEXT.__cstring: 0xccb
-  __TEXT.__oslogstring: 0x79
+3.6.0.0.0
+  __TEXT.__text: 0xb200
+  __TEXT.__objc_methlist: 0x9dc
+  __TEXT.__const: 0x1ea
+  __TEXT.__cstring: 0xe9d
+  __TEXT.__oslogstring: 0x169
   __TEXT.__gcc_except_tab: 0x74
   __TEXT.__swift5_typeref: 0xa
-  __TEXT.__unwind_info: 0x2d8
-  __TEXT.__objc_classname: 0x189
-  __TEXT.__objc_methname: 0x1b73
-  __TEXT.__objc_methtype: 0x42a
-  __TEXT.__objc_stubs: 0x11e0
-  __DATA_CONST.__got: 0x2d8
-  __DATA_CONST.__const: 0x148
-  __DATA_CONST.__objc_classlist: 0x68
+  __TEXT.__unwind_info: 0x318
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x170
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5a0
-  __DATA_CONST.__objc_superrefs: 0x68
+  __DATA_CONST.__objc_selrefs: 0x668
+  __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x408
-  __AUTH_CONST.__cfstring: 0x6e0
-  __AUTH_CONST.__objc_const: 0x3a70
-  __AUTH_CONST.__objc_intobj: 0x120
+  __DATA_CONST.__got: 0x330
+  __AUTH_CONST.__cfstring: 0x820
+  __AUTH_CONST.__objc_const: 0x45b8
+  __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x160
+  __AUTH_CONST.__auth_got: 0x430
+  __AUTH.__objc_data: 0x4b0
+  __DATA.__objc_ivar: 0x19c
   __DATA.__data: 0x138
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/PrivateFrameworks/DeepVideoProcessingCore.framework/DeepVideoProcessingCore
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2E79E1E4-958C-3972-9B96-F0F03EEBEA82
-  Functions: 281
-  Symbols:   1223
-  CStrings:  495
+  UUID: 14989276-0065-3A81-BDA6-4099F5A2F4D7
+  Functions: 318
+  Symbols:   1381
+  CStrings:  182
 
Symbols:
+ +[VELensFlareMitigationParameters opticalCentersReferenceSize]
+ -[VEDenseUpscalerConfiguration .cxx_destruct]
+ -[VEDenseUpscalerConfiguration denseBufferPixelFormat]
+ -[VEDenseUpscalerConfiguration destinationHeight]
+ -[VEDenseUpscalerConfiguration destinationWidth]
+ -[VEDenseUpscalerConfiguration frameHeight]
+ -[VEDenseUpscalerConfiguration framePreferredPixelFormats]
+ -[VEDenseUpscalerConfiguration frameSupportedPixelFormats]
+ -[VEDenseUpscalerConfiguration frameWidth]
+ -[VEDenseUpscalerConfiguration initWithSourceWidth:sourceHeight:destinationWidth:destinationHeight:frameWidth:frameHeight:type:]
+ -[VEDenseUpscalerConfiguration sourceHeight]
+ -[VEDenseUpscalerConfiguration sourceWidth]
+ -[VEDenseUpscalerConfiguration type]
+ -[VEDenseUpscalerParameters .cxx_destruct]
+ -[VEDenseUpscalerParameters destinationFrame]
+ -[VEDenseUpscalerParameters guideFrame]
+ -[VEDenseUpscalerParameters initWithSourceFrame:guideFrame:destinationFrame:]
+ -[VEDenseUpscalerParameters sourceFrame]
+ -[VEFrameProcessor internalLoadState:error:]
+ -[VEFrameProcessor internalLoadState:error:].cold.1
+ -[VEFrameProcessor internalSaveState:]
+ -[VEFrameProcessor internalSaveState:].cold.1
+ -[VEFrameProcessor loadState:error:]
+ -[VEFrameProcessor saveState:]
+ -[VELensFlareMitigationParameters debugTrackBuffer]
+ -[VELensFlareMitigationParameters initWithSourceFrame:nextFrame:opticalFlow:sourceFrameOpticalCenter:futureOpticalCenters:pastOpticalCenters:previousOutputFrame:previousPreviousOutputFrame:submissionMode:destinationFrame:]
+ -[VELensFlareMitigationParameters initWithSourceFrame:nextFrame:opticalFlow:sourceFrameOpticalCenter:futureOpticalCenters:pastOpticalCenters:previousOutputFrame:previousPreviousOutputFrame:submissionMode:destinationFrame:debugTrackBuffer:]
+ -[VELensFlareMitigationParameters initWithSourceFrame:nextFrame:opticalFlow:sourceFrameOpticalCenter:nextFrameOpticalCenter:opticalCenterShift:previousOutputFrame:previousPreviousOutputFrame:submissionMode:destinationFrame:debugTrackBuffer:]
+ -[VEMotionBlurParameters initWithSourceFrame:nextFrame:previousFrame:nextOpticalFlow:previousOpticalFlow:motionBlurStrength:submissionMode:destinationFrame:].cold.1
+ _IOSurfaceCreate
+ _IOSurfaceGetBytesPerRow
+ _OBJC_CLASS_$_DVPDenseUpscalerConfiguration
+ _OBJC_CLASS_$_DVPDenseUpscalerParameters
+ _OBJC_CLASS_$_DenseUpscalerProcessor
+ _OBJC_CLASS_$_VEDenseUpscalerConfiguration
+ _OBJC_CLASS_$_VEDenseUpscalerParameters
+ _OBJC_IVAR_$_VEDenseUpscalerConfiguration._denseBufferPixelFormat
+ _OBJC_IVAR_$_VEDenseUpscalerConfiguration._destinationHeight
+ _OBJC_IVAR_$_VEDenseUpscalerConfiguration._destinationWidth
+ _OBJC_IVAR_$_VEDenseUpscalerConfiguration._frameHeight
+ _OBJC_IVAR_$_VEDenseUpscalerConfiguration._framePreferredPixelFormats
+ _OBJC_IVAR_$_VEDenseUpscalerConfiguration._frameSupportedPixelFormats
+ _OBJC_IVAR_$_VEDenseUpscalerConfiguration._frameWidth
+ _OBJC_IVAR_$_VEDenseUpscalerConfiguration._sourceHeight
+ _OBJC_IVAR_$_VEDenseUpscalerConfiguration._sourceWidth
+ _OBJC_IVAR_$_VEDenseUpscalerConfiguration._type
+ _OBJC_IVAR_$_VEDenseUpscalerParameters._destinationFrame
+ _OBJC_IVAR_$_VEDenseUpscalerParameters._guideFrame
+ _OBJC_IVAR_$_VEDenseUpscalerParameters._sourceFrame
+ _OBJC_IVAR_$_VEFrameProcessor._denseUpscalerProcessor
+ _OBJC_IVAR_$_VELensFlareMitigationParameters._debugTrackBuffer
+ _OBJC_METACLASS_$_VEDenseUpscalerConfiguration
+ _OBJC_METACLASS_$_VEDenseUpscalerParameters
+ __OBJC_$_CLASS_PROP_LIST_VELensFlareMitigationParameters
+ __OBJC_$_INSTANCE_METHODS_VEDenseUpscalerConfiguration
+ __OBJC_$_INSTANCE_METHODS_VEDenseUpscalerParameters
+ __OBJC_$_INSTANCE_VARIABLES_VEDenseUpscalerConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_VEDenseUpscalerParameters
+ __OBJC_$_PROP_LIST_VEDenseUpscalerConfiguration
+ __OBJC_$_PROP_LIST_VEDenseUpscalerParameters
+ __OBJC_CLASS_PROTOCOLS_$_VEDenseUpscalerConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_VEDenseUpscalerParameters
+ __OBJC_CLASS_RO_$_VEDenseUpscalerConfiguration
+ __OBJC_CLASS_RO_$_VEDenseUpscalerParameters
+ __OBJC_METACLASS_RO_$_VEDenseUpscalerConfiguration
+ __OBJC_METACLASS_RO_$_VEDenseUpscalerParameters
+ ___30-[VEFrameProcessor saveState:]_block_invoke
+ ___36-[VEFrameProcessor loadState:error:]_block_invoke
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
+ __os_log_impl
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_VideoEffect
+ _createPlanar16HalfIOSurface
+ _createTextureViaPlanar16HalfIOSurface
+ _dvpDenseUpscalerConfigFromVE
+ _dvpDenseUpscalerParamsFromVE
+ _kIOSurfaceAllocSize
+ _kIOSurfaceBytesPerElement
+ _kIOSurfaceBytesPerRow
+ _kIOSurfaceHeight
+ _kIOSurfacePixelFormat
+ _kIOSurfaceWidth
+ _memoryUsageTabISR
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$debugTrackBuffer
+ _objc_msgSend$destinationHeight
+ _objc_msgSend$destinationWidth
+ _objc_msgSend$getMotionShiftFromPastOpticalCenters:futureOpticalCenters:currentOpticalCenter:currentOpticalCenterShift:
+ _objc_msgSend$getValue:
+ _objc_msgSend$guideFrame
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$initWithSourceFrame:guideFrame:destinationFrame:
+ _objc_msgSend$initWithSourceFrame:nextFrame:opticalFlow:sourceFrameOpticalCenter:futureOpticalCenters:pastOpticalCenters:previousOutputFrame:previousPreviousOutputFrame:submissionMode:destinationFrame:debugTrackBuffer:
+ _objc_msgSend$initWithSourceFrame:nextFrame:opticalFlow:sourceFrameOpticalCenter:nextFrameOpticalCenter:opticalCenterShift:previousOutputFrame:previousPreviousOutputFrame:submissionMode:destinationFrame:debugTrackBuffer:
+ _objc_msgSend$initWithSourceWidth:sourceHeight:destinationWidth:destinationHeight:frameWidth:frameHeight:type:
+ _objc_msgSend$initWithSourceWidth:sourceHeight:destinationWidth:destinationHeight:type:
+ _objc_msgSend$internalLoadState:error:
+ _objc_msgSend$internalSaveState:
+ _objc_msgSend$opticalCentersReferenceSize
+ _objc_msgSend$processWithDenseUpscalerParams:error:
+ _objc_msgSend$sourceHeight
+ _objc_msgSend$sourceWidth
+ _objc_msgSend$startSessionWithDenseUpscalerConfig:error:
+ _objc_msgSend$type
+ _objc_retain_x2
+ _objc_retain_x28
+ _swift_release_x19
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_VideoEffect
- _objc_autorelease
- _objc_msgSend$initWithSourceFrame:nextFrame:opticalFlow:sourceFrameOpticalCenter:nextFrameOpticalCenter:opticalCenterShift:previousOutputFrame:previousPreviousOutputFrame:submissionMode:destinationFrame:
- _swift_release
CStrings:
+ "\n"
+ "Could not init DenseUpscalerProcessor"
+ "DenseUpscalerProcessor already created"
+ "Error! Failed to create outputTexture. Buffer Size: %ld x %ld, Format: %d"
+ "Failed to call getMotionShiftFromPastOpticalCenters"
+ "Failed to create texture descriptor\n"
+ "Failed to initialize"
+ "Failed to initialize: Invalid destination parameters"
+ "Failed to initialize: Invalid motion blur strength parameter %ld, expected range [%d, %d]"
+ "Failed to initialize: Invalid source or destination frame"
+ "Failed to initialize: Invalid source or destination frames"
+ "Failed to initialize: Invalid source or reference frame"
+ "Failed to initialize: Mismatch between source and next frame's pixel formats"
+ "Failed to initialize: Mismatch between source and reference frame's pixel formats"
+ "Failed to initialize: Mismatch between source, next, and previous frame's pixel formats"
+ "Failed to initialize: Mismatch between source, previous, and previousOutput frame's pixel formats"
+ "VDGProcessor state placeholder"
+ "VEDenseUpscalerConfiguration: Destination must be >= source dimensions"
+ "VEDenseUpscalerConfiguration: Invalid destination dimensions"
+ "VEDenseUpscalerConfiguration: Invalid frame dimensions"
+ "VEDenseUpscalerConfiguration: Invalid source dimensions"
+ "VEDenseUpscalerParameters: destinationFrame is nil"
+ "VEDenseUpscalerParameters: guideFrame is nil"
+ "VEDenseUpscalerParameters: sourceFrame is nil"
+ "denseUpscalerConfiguration is missing"
+ "loadState VDG placeholder: %@"
+ "loadState: no active processor supports state serialization"
+ "readPNG: Error! File name is NULL"
+ "readPNG: Error! Invalid file name"
+ "saveState: no active processor supports state serialization"
+ "\x82"
- "\t"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<MTLDevice>\""
- "@\"FRCProcessor\""
- "@\"MTLSharedEventListener\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"OpticalFlowProcessor\""
- "@\"VDGProcessor\""
- "@\"VEFrame\""
- "@\"VEFrame\"16@0:8"
- "@\"VEFrameOpticalFlow\""
- "@\"VSAProcessor\""
- "@\"VSRProcessor\""
- "@112@0:8@16@24@32{CGPoint=dd}40{CGPoint=dd}56d72@80@88q96@104"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@32@0:8^{__CVBuffer=}16^{__CVBuffer=}24"
- "@40@0:8:16@24@32"
- "@48@0:8@16@24q32@40"
- "@48@0:8^{__CVBuffer=}16{?=qiIq}24"
- "@48@0:8q16q24q32q40"
- "@52@0:8q16q24B32q36q44"
- "@56@0:8@16@24@32@40@48"
- "@64@0:8@16@24@32@40q48@56"
- "@68@0:8q16q24q32q40B48q52q60"
- "@80@0:8@16@24@32@40@48q56q64@72"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8q16"
- "B32@0:8@16^@24"
- "B40@0:8^{CGPoint=dd}16Q24^d32"
- "Error! Faild to create outputTextute. Buffer Size: %ld x %ld, Format: %d"
- "Fail to initialize"
- "Fail to initialize: Mismatch between source, previous and previousOutput frame's pixel formats"
- "Fail to to initialize: Invalid destination parameters"
- "Fail to to initialize: Invalid motion blur strength parameter"
- "Fail to to initialize: Invalid source or destination frame"
- "Fail to to initialize: Invalid source or destination frames"
- "Fail to to initialize: Invalid source or reference frame"
- "Fail to to initialize: Mismatch between source and next frame's pixel formats"
- "Fail to to initialize: Mismatch between source and reference frame's pixel formats"
- "Fail to to initialize: Mismatch between source, next and previous frame's pixel formats"
- "Fail to to initialize: Mismatch between source, next frame's pixel formats"
- "Failed to cretae texture descriptor\n"
- "I16@0:8"
- "NSObject"
- "PNGRepresentationOfImage:format:colorSpace:options:"
- "Q16@0:8"
- "T#,R"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_destinationFrames"
- "T@\"NSArray\",R,N,V_framePreferredPixelFormats"
- "T@\"NSArray\",R,N,V_frameSupportedPixelFormats"
- "T@\"NSArray\",R,N,V_interpolationPhase"
- "T@\"NSIndexSet\",R,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"VEFrame\",R,N"
- "T@\"VEFrame\",R,N,V_destinationFrame"
- "T@\"VEFrame\",R,N,V_nextFrame"
- "T@\"VEFrame\",R,N,V_previousFrame"
- "T@\"VEFrame\",R,N,V_previousOutputFrame"
- "T@\"VEFrame\",R,N,V_previousPreviousOutputFrame"
- "T@\"VEFrame\",R,N,V_sourceFrame"
- "T@\"VEFrameOpticalFlow\",R,N,V_nextOpticalFlow"
- "T@\"VEFrameOpticalFlow\",R,N,V_opticalFlow"
- "T@\"VEFrameOpticalFlow\",R,N,V_previousOpticalFlow"
- "TB,R,N,V_usePrecomputedFlow"
- "TI,R,N,V_flowBufferPixelFormat"
- "TIFFRepresentationOfImage:format:colorSpace:options:"
- "TQ,R"
- "T^{__CVBuffer=},R,N,V_backwardFlow"
- "T^{__CVBuffer=},R,N,V_buffer"
- "T^{__CVBuffer=},R,N,V_forwardFlow"
- "Td,R,N,V_opticalCenterShift"
- "Tq,R,N"
- "Tq,R,N,V_flowBufferHeight"
- "Tq,R,N,V_flowBufferWidth"
- "Tq,R,N,V_frameHeight"
- "Tq,R,N,V_frameWidth"
- "Tq,R,N,V_inputType"
- "Tq,R,N,V_motionBlurStrength"
- "Tq,R,N,V_qualityPrioritization"
- "Tq,R,N,V_revision"
- "Tq,R,N,V_scaleFactor"
- "Tq,R,N,V_submissionMode"
- "T{?=qiIq},R,N,V_presentationTimeStamp"
- "T{CGPoint=dd},R,N,V_nextFrameOpticalCenter"
- "T{CGPoint=dd},R,N,V_sourceFrameOpticalCenter"
- "UTF8String"
- "VEConfiguration"
- "VEFrame"
- "VEFrameOpticalFlow"
- "VEFrameProcessor"
- "VEFrameRateConversionConfiguration"
- "VEFrameRateConversionParameters"
- "VELensFlareMitigationConfiguration"
- "VELensFlareMitigationParameters"
- "VEMotionBlurConfiguration"
- "VEMotionBlurParameters"
- "VEOpticalFlowConfiguration"
- "VEOpticalFlowParameters"
- "VEParameters"
- "VESuperResolutionConfiguration"
- "VESuperResolutionParameters"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__CVBuffer=}"
- "^{__CVBuffer=}16@0:8"
- "_backwardFlow"
- "_buffer"
- "_destinationFrame"
- "_destinationFrames"
- "_device"
- "_flowBufferHeight"
- "_flowBufferPixelFormat"
- "_flowBufferWidth"
- "_forwardFlow"
- "_frameHeight"
- "_framePreferredPixelFormats"
- "_frameSupportedPixelFormats"
- "_frameWidth"
- "_frcProcessor"
- "_inputType"
- "_interpolationPhase"
- "_motionBlurStrength"
- "_nextFrame"
- "_nextFrameOpticalCenter"
- "_nextOpticalFlow"
- "_opticalCenterShift"
- "_opticalFlow"
- "_presentationTimeStamp"
- "_previousFrame"
- "_previousOpticalFlow"
- "_previousOutputFrame"
- "_previousPreviousOutputFrame"
- "_processFrameQueue"
- "_qualityPrioritization"
- "_revision"
- "_scaleFactor"
- "_sharedEventList"
- "_sharedEventListLock"
- "_sharedEventListTearingDown"
- "_sharedEventListener"
- "_sourceFrame"
- "_sourceFrameOpticalCenter"
- "_submissionMode"
- "_usePrecomputedFlow"
- "_vdgProcessor"
- "_vsaProcessor"
- "_vsrProcessor"
- "addObject:"
- "array"
- "arrayLength"
- "autorelease"
- "backwardFlow"
- "blitCommandEncoder"
- "boolValue"
- "buffer"
- "bytes"
- "class"
- "colorSpace"
- "conformsToProtocol:"
- "containsIndex:"
- "containsObject:"
- "contents"
- "context"
- "copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:"
- "copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:"
- "count"
- "createSharedEventListener"
- "d"
- "d16@0:8"
- "dataWithLength:"
- "dealloc"
- "debugDescription"
- "defaultRevision"
- "description"
- "destinationFrame"
- "destinationFrames"
- "destroySharedEventListener"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "downloadAssetWithCompletionHandler:"
- "downloadMobileAssetWithInputType:withCompletionHandler:"
- "encodeSignalEvent:value:"
- "encodeWaitForEvent:value:"
- "endEncoding"
- "endSession"
- "errorWithDomain:code:userInfo:"
- "extent"
- "fileURLWithPath:"
- "finishProcessing"
- "floatValue"
- "flowBufferHeight"
- "flowBufferPixelFormat"
- "flowBufferWidth"
- "forwardFlow"
- "frameHeight"
- "framePreferredPixelFormats"
- "frameSupportedPixelFormats"
- "frameWidth"
- "getAssetStatusWithPercentCompleted:"
- "getBytes:bytesPerRow:bytesPerImage:fromRegion:mipmapLevel:slice:"
- "getFlowBufferDimensionsFromFrameWidth:frameHeight:revision:"
- "getMobileAssetStatusForInputType:percentCompleted:"
- "getMotionShiftFromOpticalCenters:opticalCenterArrayLen:opticalCenterMotionShifts:"
- "hash"
- "height"
- "imageWithCVPixelBuffer:options:"
- "imageWithContentsOfURL:options:"
- "indexSetWithIndexesInRange:"
- "init"
- "initWithArray:"
- "initWithBuffer:presentationTimeStamp:"
- "initWithDispatchQueue:"
- "initWithForwardFlow:backwardFlow:"
- "initWithFrameWidth:FrameHeight:revision:"
- "initWithFrameWidth:FrameHeight:usePrecomputedFlow:"
- "initWithFrameWidth:FrameHeight:usePrecomputedFlow:revision:"
- "initWithFrameWidth:frameHeight:inputType:usePrecomputedFlow:"
- "initWithFrameWidth:frameHeight:qualityPrioritization:revision:"
- "initWithFrameWidth:frameHeight:scaleFactor:inputType:usePrecomputedFlow:qualityPrioritization:revision:"
- "initWithFrameWidth:frameHeight:usePrecomputedFlow:qualityPrioritization:revision:"
- "initWithSourceFrame:nextFrame:opticalFlow:interpolationPhase:submissionMode:destinationFrames:"
- "initWithSourceFrame:nextFrame:opticalFlow:sourceFrameOpticalCenter:nextFrameOpticalCenter:opticalCenterShift:previousOutputFrame:previousPreviousOutputFrame:submissionMode:destinationFrame:"
- "initWithSourceFrame:nextFrame:previousFrame:nextOpticalFlow:previousOpticalFlow:motionBlurStrength:submissionMode:destinationFrame:"
- "initWithSourceFrame:nextFrame:submissionMode:opticalFlow:"
- "initWithSourceFrame:previousFrame:previousOutputFrame:opticalFlow:destinationFrame:"
- "initWithSourceFrame:previousFrame:previousOutputFrame:opticalFlow:submissionMode:destinationFrame:"
- "inputType"
- "intValue"
- "integerValue"
- "internalEndSession"
- "internalProcessWithParameters:error:"
- "internalStartSessionWithConfigurations:error:"
- "interpolationPhase"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSupportedRevision:"
- "isSupportedScaleFactor:"
- "lastIndex"
- "lastObject"
- "length"
- "motionBlurStrength"
- "mutableBytes"
- "newBufferWithIOSurface:"
- "newLinearTextureWithDescriptor:offset:bytesPerRow:bytesPerImage:"
- "newSharedEvent"
- "newTextureWithDescriptor:"
- "newTextureWithDescriptor:iosurface:plane:"
- "nextFrame"
- "nextFrameOpticalCenter"
- "nextOpticalFlow"
- "notifyListener:atValue:block:"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedLong:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "opticalCenterShift"
- "opticalFlow"
- "pathExtension"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pixelFormat"
- "presentationTimeStamp"
- "previousFrame"
- "previousOpticalFlow"
- "previousOutputFrame"
- "previousPreviousOutputFrame"
- "processWithCommandBuffer:parameters:completionHandler:"
- "processWithDeghostingParams:error:"
- "processWithFrameRateParams:error:"
- "processWithListParameters:completionHandler:"
- "processWithListParameters:error:"
- "processWithMotionBlurParams:error:"
- "processWithOpticalFlowParams:error:"
- "processWithParameters:completionHandler:"
- "processWithParameters:error:"
- "processWithSuperResolutionParams:error:"
- "properties"
- "q"
- "q16@0:8"
- "q24@0:8^q16"
- "qualityPrioritization"
- "readPNG: Error ! File name is NULL"
- "readPNG: Error ! Invalid file name"
- "release"
- "removeAllObjects"
- "removeObject:"
- "render:toCVPixelBuffer:bounds:colorSpace:"
- "replaceRegion:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "revision"
- "scaleFactor"
- "self"
- "setArrayLength:"
- "setHeight:"
- "setObject:forKeyedSubscript:"
- "setPixelFormat:"
- "setSignaledValue:"
- "setStorageMode:"
- "setStreamingMode:"
- "setTextureType:"
- "setUsage:"
- "setWidth:"
- "sourceFrame"
- "sourceFrameOpticalCenter"
- "startSessionWithConfiguration:error:"
- "startSessionWithDeghostingConfig:error:"
- "startSessionWithFrameRateConfig:error:"
- "startSessionWithListConfigurations:error:"
- "startSessionWithMotionBlurConfig:error:"
- "startSessionWithOpticalFlowConfig:error:"
- "startSessionWithSuperResolutionConfig:error:"
- "stringWithUTF8String:"
- "submissionMode"
- "superclass"
- "supportedRevisions"
- "supportedScaleFactors"
- "texture2DDescriptorWithPixelFormat:width:height:mipmapped:"
- "textureType"
- "updateOpticalFlowDimensions"
- "usePrecomputedFlow"
- "v16@0:8"
- "v24@0:8@?16"
- "v32@0:8@16@?24"
- "v40@0:8@16@24@?32"
- "waitUntilSignaledValue:timeoutMS:"
- "width"
- "zone"
- "{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}"
- "{?=qiIq}16@0:8"
- "{CGPoint=\"x\"d\"y\"d}"
- "{CGPoint=dd}16@0:8"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
