## DeepVideoProcessingCore

> `/System/Library/PrivateFrameworks/DeepVideoProcessingCore.framework/DeepVideoProcessingCore`

```diff

-  __TEXT.__text: 0x6d674
-  __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_methlist: 0x50b4
+  __TEXT.__text: 0x6c888
+  __TEXT.__auth_stubs: 0xf00
+  __TEXT.__objc_methlist: 0x4fb4
   __TEXT.__const: 0x688
-  __TEXT.__cstring: 0x658b
-  __TEXT.__oslogstring: 0x33ab
+  __TEXT.__cstring: 0x62f1
+  __TEXT.__oslogstring: 0x3423
   __TEXT.__gcc_except_tab: 0x2e0
-  __TEXT.__unwind_info: 0x12f0
-  __TEXT.__objc_classname: 0x6cb
-  __TEXT.__objc_methname: 0x13c81
-  __TEXT.__objc_methtype: 0x77ae
-  __TEXT.__objc_stubs: 0x77e0
-  __DATA_CONST.__got: 0x388
+  __TEXT.__unwind_info: 0x12d8
+  __TEXT.__objc_classname: 0x6c2
+  __TEXT.__objc_methname: 0x138b0
+  __TEXT.__objc_methtype: 0x77c5
+  __TEXT.__objc_stubs: 0x7720
+  __DATA_CONST.__got: 0x3b8
   __DATA_CONST.__const: 0x310
-  __DATA_CONST.__objc_classlist: 0x280
+  __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29d8
-  __DATA_CONST.__objc_superrefs: 0x258
+  __DATA_CONST.__objc_selrefs: 0x2950
+  __DATA_CONST.__objc_superrefs: 0x250
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x778
+  __AUTH_CONST.__auth_got: 0x798
   __AUTH_CONST.__const: 0xf0
-  __AUTH_CONST.__cfstring: 0x3260
-  __AUTH_CONST.__objc_const: 0x11208
-  __AUTH_CONST.__objc_intobj: 0x180
+  __AUTH_CONST.__cfstring: 0x31e0
+  __AUTH_CONST.__objc_const: 0x10d60
+  __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1900
-  __DATA.__objc_ivar: 0x150c
+  __AUTH.__objc_data: 0x18b0
+  __DATA.__objc_ivar: 0x149c
   __DATA.__data: 0x260
   __DATA.__bss: 0x8
   __DATA.__common: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2540
-  Symbols:   8602
-  CStrings:  4682
+  Functions: 2508
+  Symbols:   8516
+  CStrings:  4622
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
Symbols:
+ -[FRNet convertBuffer:toOutputBuffer:outputAttachment:rotationMethod:crop:waitForCompletion:]
+ -[FRNet convertToRGB:to:rotate:]
+ -[FRNet getColorConsistentOutputRGBVia:currentRGB:attachment:destinationFrame:]
+ -[ISRNet allocateOutputBufferObjects]
+ -[ISRNet getOutputPortNames]
+ -[ISRNet initializeOutputPorts]
+ -[ISRNet outputSurface]
+ -[ISRNet setOutputSurface:]
+ -[OFNormalization convertFP16IOSurface:toRGBBuffer:]
+ -[OFNormalization convertRGBBuffer:toFP16IOSurface:]
+ -[OFNormalization copyRGBBuffer:toTextureArray:]
+ -[OFNormalization encodeCopyRGBBufferToCommandBuffer:source:destination:]
+ -[OFNormalization encodePostprocessSRFrameToCommandBuffer:srFrameY:bicubicY:bicubicUV:outputY:outputUV:]
+ -[OFNormalization postprocessSRFrame:bicubicYUV:outputYUV:]
+ -[Upsampler encodeUpsampleRBGPackedToCommandBuffer:source:destination:scaleFactor:useBGROrdinal:]
+ -[Upsampler upsampleRBGPackedBuffer:toUpsampledTexture:scaleFactor:useBGROrdinal:]
+ -[VEScaler transformAndPadSourceBuffer:destinationBuffer:rotate:waitForCompletion:]
+ -[VSRNet allocateOutputBufferObjects]
+ -[VSRNet getOutputPortNames]
+ -[VSRNet initWithModelPath:inputWidth:inputHeight:currentLRSurface:warpedHRSurface:]
+ -[VSRNet initializeOutputPorts]
+ -[VSRNet processSuperResolutionToOutputBuffer:]
+ -[Warper computeErrorMaskForSourceRGB:referenceRGB:flow:outputErrorMask:threshold:scaleFactor:]
+ -[Warper encodeWarpBlendPreviousRGBToCommandBuffer:previousHR:withCurrentLR:viaLowResFlow:viaErrorMask:scaleFactor:effectiveOutputWidth:effectiveOutputHeight:destination:]
+ -[Warper warpBlendPreviousHRRGBTexture:withCurrentLRRGBTexture:viaLowResFlow:viaErrorMask:scaleFactor:effectiveOutputWidth:effectiveOutputHeight:toShuffledTexture:]
+ GCC_except_table28
+ _CFDictionaryGetValue
+ _IOSurfaceCreate
+ _IOSurfaceGetBytesPerRow
+ _OBJC_IVAR_$_FRNet._currPaddedLRRGBSurface
+ _OBJC_IVAR_$_FRNet._currPaddedLRRGBTexture
+ _OBJC_IVAR_$_FRNet._currentLRRGBTexture
+ _OBJC_IVAR_$_FRNet._highResRGBBuffer
+ _OBJC_IVAR_$_FRNet._highResRGBTexture
+ _OBJC_IVAR_$_FRNet._previousLRRGB
+ _OBJC_IVAR_$_FRNet._rghaPixelFormat
+ _OBJC_IVAR_$_FRNet._warpedHRRGBSurface
+ _OBJC_IVAR_$_FRNet._warpedHRRGBTexture
+ _OBJC_IVAR_$_ISRNet._outputBufferObject
+ _OBJC_IVAR_$_ISRNet._outputPortName
+ _OBJC_IVAR_$_ISRNet._outputSurface
+ _OBJC_IVAR_$_ISRNet._output_port
+ _OBJC_IVAR_$_Upsampler._upsampleBGRToRGBKernel
+ _OBJC_IVAR_$_Upsampler._upsampleRGBToRGBKernel
+ _OBJC_IVAR_$_VSRNet._outputBufferObject
+ _OBJC_IVAR_$_VSRNet._outputPortName
+ _OBJC_IVAR_$_VSRNet._outputSurface
+ _OBJC_IVAR_$_VSRNet._output_port
+ _OBJC_IVAR_$_Warper._warpBlendShuffleRGBKernel
+ _createPlanar16HalfIOSurface
+ _createTextureViaPlanar16HalfIOSurface
+ _e5rt_buffer_object_create_from_iosurface
+ _kCVImageBufferCGColorSpaceKey
+ _kIOSurfaceAllocSize
+ _kIOSurfaceBytesPerElement
+ _kIOSurfaceBytesPerRow
+ _kIOSurfaceHeight
+ _kIOSurfacePixelFormat
+ _kIOSurfaceWidth
+ _objc_msgSend$computeErrorMaskForSourceRGB:referenceRGB:flow:outputErrorMask:threshold:scaleFactor:
+ _objc_msgSend$convertBuffer:toOutputBuffer:outputAttachment:rotationMethod:crop:waitForCompletion:
+ _objc_msgSend$convertFP16IOSurface:toRGBBuffer:
+ _objc_msgSend$convertRGBBuffer:toFP16IOSurface:
+ _objc_msgSend$convertToRGB:to:rotate:
+ _objc_msgSend$copyRGBBuffer:toTextureArray:
+ _objc_msgSend$encodeCopyRGBBufferToCommandBuffer:source:destination:
+ _objc_msgSend$encodePostprocessSRFrameToCommandBuffer:srFrameY:bicubicY:bicubicUV:outputY:outputUV:
+ _objc_msgSend$encodeUpsampleRBGPackedToCommandBuffer:source:destination:scaleFactor:useBGROrdinal:
+ _objc_msgSend$encodeWarpBlendPreviousRGBToCommandBuffer:previousHR:withCurrentLR:viaLowResFlow:viaErrorMask:scaleFactor:effectiveOutputWidth:effectiveOutputHeight:destination:
+ _objc_msgSend$getColorConsistentOutputRGBVia:currentRGB:attachment:destinationFrame:
+ _objc_msgSend$initWithModelPath:inputWidth:inputHeight:currentLRSurface:warpedHRSurface:
+ _objc_msgSend$initializeOutputPorts
+ _objc_msgSend$postprocessSRFrame:bicubicYUV:outputYUV:
+ _objc_msgSend$processSuperResolutionToOutputBuffer:
+ _objc_msgSend$transformAndPadSourceBuffer:destinationBuffer:rotate:waitForCompletion:
+ _objc_msgSend$upsampleRBGPackedBuffer:toUpsampledTexture:scaleFactor:useBGROrdinal:
+ _objc_msgSend$warpBlendPreviousHRRGBTexture:withCurrentLRRGBTexture:viaLowResFlow:viaErrorMask:scaleFactor:effectiveOutputWidth:effectiveOutputHeight:toShuffledTexture:
- -[FRNet convertToRGB:to:withRGBFormat:rotate:]
- -[FRNet getColorConsistentOutputRGBVia:bicubicRGB:laplacianMask:attachment:destinationFrame:]
- -[FRNet setUseLaplacianMask:]
- -[FRNet useLaplacianMask]
- -[LoGFilter .cxx_destruct]
- -[LoGFilter createMaskFrom:to:]
- -[LoGFilter encodeDiffToCommandBuffer:texture0:texture1:]
- -[LoGFilter encodeToCommandBuffer:sourceTexture:destinationTexture:]
- -[LoGFilter encodeUpsampleScaleToCommandBuffer:sourceTexture:destinationTexture:]
- -[LoGFilter init]
- -[LoGFilter maskScaleFactor]
- -[LoGFilter maskStrength]
- -[LoGFilter setMaskScaleFactor:]
- -[LoGFilter setMaskStrength:]
- -[OFNormalization convertBuffer:toFP16IOSurface:]
- -[OFNormalization convertBuffer:toFP16ShuffledIOSurface:]
- -[OFNormalization convertFP16IOSurface:toBuffer:]
- -[OFNormalization denormalizeRGB:to:]
- -[OFNormalization encodeDenormalizeRGBToCommandBuffer:source:destination:]
- -[OFNormalization encodeNormalizationRGBToCommandBuffer:source:destination:]
- -[OFNormalization encodeNormalizeLumaToCommandBuffer:source:destination:]
- -[OFNormalization encodePostprocessSRFrameToCommandBuffer:srFrameY:bicubicY:bicubicUV:laplacianMask:outputY:outputUV:]
- -[OFNormalization normalizeLumaFromFrame:toTexture:]
- -[OFNormalization normalizeRGB:to:]
- -[OFNormalization postprocessSRFrame:bicubicYUV:laplacianMask:outputYUV:]
- -[SRNet allocateOutputBufferObjects]
- -[SRNet getOutputPortNames]
- -[SRNet outputBufferObject]
- -[SRNet outputPortName]
- -[SRNet outputSurface]
- -[SRNet output_port]
- -[SRNet setOutputPortName:]
- -[SRNet setOutputSurface:]
- -[Upsampler encodeUpsampleRBGPackedToCommandBuffer:source:destination:scaleFactor:]
- -[Upsampler upsampleRBGPackedBuffer:to:scaleFactor:]
- -[VSRNet allocateInputBufferObjects]
- -[VSRNet initWithModelPath:inputWidth:inputHeight:]
- -[VSRNet inputSurface]
- -[VSRNet prevHRSurface]
- -[VSRNet processSuperResolutionInputBuffer:withPrevHighResolutionFrame:outputBuffer:]
- -[VSRNet setInputSurface:]
- -[VSRNet setPrevHRSurface:]
- -[Warper computeErrorMask:reference:flow:output:threshold:scaleFactor:]
- -[Warper encodeWarpBlendToCommandBuffer:source:scaleFactor:withLowResFlow:withBicubicUpscaled:withErrorMask:destination:]
- -[Warper warpBlendBufferRGBTexture:scaleFactor:withLowResFlowTexture:withBicubicUpscaledTexture:withErrorMaskTexture:toHighResBufferTexture:]
- GCC_except_table31
- _OBJC_CLASS_$_LoGFilter
- _OBJC_CLASS_$_MPSImageGaussianBlur
- _OBJC_IVAR_$_FRNet._attachmentRGBDict
- _OBJC_IVAR_$_FRNet._bicubicRGB
- _OBJC_IVAR_$_FRNet._bicubicRGBTexture
- _OBJC_IVAR_$_FRNet._currentLRYUV
- _OBJC_IVAR_$_FRNet._highResolutionNormalizedBufferPool
- _OBJC_IVAR_$_FRNet._laplacianMask
- _OBJC_IVAR_$_FRNet._logFilter
- _OBJC_IVAR_$_FRNet._lowResolutionNormalizedBufferPool
- _OBJC_IVAR_$_FRNet._normalizedCurrentLowResLuma
- _OBJC_IVAR_$_FRNet._normalizedCurrentLowResLumaTexture
- _OBJC_IVAR_$_FRNet._normalizedPreviousLowResLuma
- _OBJC_IVAR_$_FRNet._normalizedPreviousLowResLumaTexture
- _OBJC_IVAR_$_FRNet._normalizedRGB
- _OBJC_IVAR_$_FRNet._outputPixelFormat
- _OBJC_IVAR_$_FRNet._previousHRRGB
- _OBJC_IVAR_$_FRNet._previousHRRGBTexture
- _OBJC_IVAR_$_FRNet._previousHighResolutionOutput
- _OBJC_IVAR_$_FRNet._previousLR
- _OBJC_IVAR_$_FRNet._previousLRYUV
- _OBJC_IVAR_$_FRNet._removeCMAttachment
- _OBJC_IVAR_$_FRNet._rgbaPixelFormat
- _OBJC_IVAR_$_FRNet._srNetHROutput
- _OBJC_IVAR_$_FRNet._useLaplacianMask
- _OBJC_IVAR_$_FRNet._vtTransferSession
- _OBJC_IVAR_$_FRNet._warpedHR
- _OBJC_IVAR_$_FRNet._warpedHRTexture
- _OBJC_IVAR_$_LoGFilter._absoluteDiffKernel
- _OBJC_IVAR_$_LoGFilter._gauss1
- _OBJC_IVAR_$_LoGFilter._gauss2
- _OBJC_IVAR_$_LoGFilter._gauss3
- _OBJC_IVAR_$_LoGFilter._gaussianFilteredTexture1
- _OBJC_IVAR_$_LoGFilter._gaussianFilteredTexture2
- _OBJC_IVAR_$_LoGFilter._maskScaleFactor
- _OBJC_IVAR_$_LoGFilter._maskStrength
- _OBJC_IVAR_$_LoGFilter._upsampleScaleKernel
- _OBJC_IVAR_$_OFNormalization._copyRgbTo4x4ShuffledTextureArray
- _OBJC_IVAR_$_OFNormalization._denormalizeRGBKernel
- _OBJC_IVAR_$_OFNormalization._normalizeLumaKernel
- _OBJC_IVAR_$_OFNormalization._normalizeLumaPacked420Kernel
- _OBJC_IVAR_$_OFNormalization._normalizeRGBKernel
- _OBJC_IVAR_$_SRNet._outputBufferObject
- _OBJC_IVAR_$_SRNet._outputPortName
- _OBJC_IVAR_$_SRNet._outputSurface
- _OBJC_IVAR_$_SRNet._output_port
- _OBJC_IVAR_$_Upsampler._imageUpsampleRGBPackedKernel
- _OBJC_IVAR_$_VSRNet._inputSurface
- _OBJC_IVAR_$_VSRNet._prevHRSurface
- _OBJC_IVAR_$_Warper._warpBlendRGBKernel
- _OBJC_METACLASS_$_LoGFilter
- __OBJC_$_INSTANCE_METHODS_LoGFilter
- __OBJC_$_INSTANCE_VARIABLES_LoGFilter
- __OBJC_$_PROP_LIST_LoGFilter
- __OBJC_$_PROP_LIST_VSRNet
- __OBJC_CLASS_RO_$_LoGFilter
- __OBJC_METACLASS_RO_$_LoGFilter
- _objc_msgSend$computeErrorMask:reference:flow:output:threshold:scaleFactor:
- _objc_msgSend$convertBuffer:toFP16IOSurface:
- _objc_msgSend$convertBuffer:toFP16ShuffledIOSurface:
- _objc_msgSend$convertFP16IOSurface:toBuffer:
- _objc_msgSend$createMaskFrom:to:
- _objc_msgSend$encodeDenormalizeRGBToCommandBuffer:source:destination:
- _objc_msgSend$encodeDiffToCommandBuffer:texture0:texture1:
- _objc_msgSend$encodeNormalizationRGBToCommandBuffer:source:destination:
- _objc_msgSend$encodeNormalizeLumaToCommandBuffer:source:destination:
- _objc_msgSend$encodePostprocessSRFrameToCommandBuffer:srFrameY:bicubicY:bicubicUV:laplacianMask:outputY:outputUV:
- _objc_msgSend$encodeUpsampleRBGPackedToCommandBuffer:source:destination:scaleFactor:
- _objc_msgSend$encodeUpsampleScaleToCommandBuffer:sourceTexture:destinationTexture:
- _objc_msgSend$encodeWarpBlendToCommandBuffer:source:scaleFactor:withLowResFlow:withBicubicUpscaled:withErrorMask:destination:
- _objc_msgSend$getColorConsistentOutputRGBVia:bicubicRGB:laplacianMask:attachment:destinationFrame:
- _objc_msgSend$initWithDevice:sigma:
- _objc_msgSend$normalizeLumaFromFrame:toTexture:
- _objc_msgSend$outputBufferObject
- _objc_msgSend$outputSurface
- _objc_msgSend$output_port
- _objc_msgSend$postprocessSRFrame:bicubicYUV:laplacianMask:outputYUV:
- _objc_msgSend$processSuperResolutionInputBuffer:withPrevHighResolutionFrame:outputBuffer:
- _objc_msgSend$setEdgeMode:
- _objc_msgSend$upsampleRBGPackedBuffer:to:scaleFactor:
- _objc_msgSend$warpBlendBufferRGBTexture:scaleFactor:withLowResFlowTexture:withBicubicUpscaledTexture:withErrorMaskTexture:toHighResBufferTexture:
CStrings:
+ "  CGColorSpace: %s"
+ "  ColorPrimaries: %s"
+ "  TransferFunction: %s"
+ "  YCbCrMatrix: %s"
+ "!!"
+ "@56@0:8@16Q24Q32^^{__IOSurface}40^^{__IOSurface}48"
+ "A!"
+ "B40@0:8^{__CVBuffer=}16@24f32B36"
+ "B48@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CFDictionary=}32^{__CVBuffer=}40"
+ "B80@0:8@16@24@32@40Q48Q56Q64@72"
+ "B88@0:8@16@24@32@40@48Q56Q64Q72@80"
+ "Error: _inputPortName does not match valid name\n"
+ "FRNet: Input missing crucial color attachments!"
+ "MISSING"
+ "_currPaddedLRRGBSurface"
+ "_currPaddedLRRGBTexture"
+ "_currentLRRGBTexture"
+ "_highResRGBBuffer"
+ "_highResRGBTexture"
+ "_previousLRRGB"
+ "_rghaPixelFormat"
+ "_upsampleBGRToRGBKernel"
+ "_upsampleRGBToRGBKernel"
+ "_warpBlendShuffleRGBKernel"
+ "_warpedHRRGBSurface"
+ "_warpedHRRGBTexture"
+ "computeErrorMaskForSourceRGB:referenceRGB:flow:outputErrorMask:threshold:scaleFactor:"
+ "convertBuffer:toOutputBuffer:outputAttachment:rotationMethod:crop:waitForCompletion:"
+ "convertFP16IOSurface:toRGBBuffer:"
+ "convertRGBBuffer:toFP16IOSurface:"
+ "convertToRGB:to:rotate:"
+ "copyRGBBuffer:toTextureArray:"
+ "e5rt_buffer_object_create_from_iosurface(&_inputBufferObjects[i], *currentLRSurface)"
+ "e5rt_buffer_object_create_from_iosurface(&_inputBufferObjects[i], *warpedHRSurface)"
+ "e5rt_execution_stream_operation_retain_output_port(self.operation, _outputPortName.UTF8String, &_output_port)"
+ "e5rt_io_port_bind_buffer_object(_input_ports[i], _inputBufferObjects[i])"
+ "e5rt_io_port_bind_buffer_object(_output_port, _outputBufferObject)"
+ "encodeCopyRGBBufferToCommandBuffer:source:destination:"
+ "encodePostprocessSRFrameToCommandBuffer:srFrameY:bicubicY:bicubicUV:outputY:outputUV:"
+ "encodeUpsampleRBGPackedToCommandBuffer:source:destination:scaleFactor:useBGROrdinal:"
+ "encodeWarpBlendPreviousRGBToCommandBuffer:previousHR:withCurrentLR:viaLowResFlow:viaErrorMask:scaleFactor:effectiveOutputWidth:effectiveOutputHeight:destination:"
+ "getColorConsistentOutputRGBVia:currentRGB:attachment:destinationFrame:"
+ "hr_prev"
+ "initWithModelPath:inputWidth:inputHeight:currentLRSurface:warpedHRSurface:"
+ "initializeOutputPorts"
+ "lr_curr"
+ "postprocessSRFrame:bicubicYUV:outputYUV:"
+ "present"
+ "processSuperResolutionToOutputBuffer:"
+ "transformAndPadSourceBuffer:destinationBuffer:rotate:waitForCompletion:"
+ "upsampleBGRToRGB"
+ "upsampleRBGPackedBuffer:toUpsampledTexture:scaleFactor:useBGROrdinal:"
+ "upsampleRGBToRGB"
+ "v56@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CFDictionary=}32q40B48B52"
+ "v64@0:8@16@24@32@40@48@56"
+ "warpBlendPreviousHRRGBTexture:withCurrentLRRGBTexture:viaLowResFlow:viaErrorMask:scaleFactor:effectiveOutputWidth:effectiveOutputHeight:toShuffledTexture:"
+ "warpBlendShuffleRGB"
- "@\"LoGFilter\""
- "@\"MPSImageGaussianBlur\""
- "B36@0:8^{__CVBuffer=}16^{__CVBuffer=}24f32"
- "B56@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CFDictionary=}40^{__CVBuffer=}48"
- "B64@0:8@16Q24@32@40@48@56"
- "B72@0:8@16@24Q32@40@48@56@64"
- "Input0 [%@]: %ld x %ld x %ld"
- "Input1 [%@]: %ld x %ld x %ld"
- "LoGFilter"
- "T@\"NSString\",&,N,V_outputPortName"
- "TB,N,V_useLaplacianMask"
- "T^{__IOSurface=},N,V_prevHRSurface"
- "T^{e5rt_buffer_object=},R,N,V_outputBufferObject"
- "T^{e5rt_io_port=},R,N,V_output_port"
- "Tf,N,V_maskScaleFactor"
- "Tf,N,V_maskStrength"
- "^{e5rt_buffer_object=}16@0:8"
- "^{e5rt_io_port=}16@0:8"
- "_absoluteDiffKernel"
- "_attachmentRGBDict"
- "_bicubicRGB"
- "_bicubicRGBTexture"
- "_copyRgbTo4x4ShuffledTextureArray"
- "_currentLRYUV"
- "_denormalizeRGBKernel"
- "_gauss1"
- "_gauss2"
- "_gauss3"
- "_gaussianFilteredTexture1"
- "_gaussianFilteredTexture2"
- "_highResolutionNormalizedBufferPool"
- "_imageUpsampleRGBPackedKernel"
- "_laplacianMask"
- "_logFilter"
- "_lowResolutionNormalizedBufferPool"
- "_maskScaleFactor"
- "_maskStrength"
- "_normalizeLumaKernel"
- "_normalizeLumaPacked420Kernel"
- "_normalizeRGBKernel"
- "_normalizedCurrentLowResLuma"
- "_normalizedCurrentLowResLumaTexture"
- "_normalizedPreviousLowResLuma"
- "_normalizedPreviousLowResLumaTexture"
- "_prevHRSurface"
- "_previousHRRGB"
- "_previousHRRGBTexture"
- "_previousHighResolutionOutput"
- "_previousLR"
- "_previousLRYUV"
- "_removeCMAttachment"
- "_upsampleScaleKernel"
- "_useLaplacianMask"
- "_warpBlendRGBKernel"
- "_warpedHR"
- "_warpedHRTexture"
- "absoluteDifference"
- "computeErrorMask:reference:flow:output:threshold:scaleFactor:"
- "convertBuffer:toFP16IOSurface:"
- "convertBuffer:toFP16ShuffledIOSurface:"
- "convertFP16IOSurface:toBuffer:"
- "copyRgbTo4x4ShuffledTextureArray"
- "createMaskFrom:to:"
- "denormalizeRGB"
- "denormalizeRGB:to:"
- "e5rt_buffer_object_get_iosurface(_inputBufferObjects[0], &_inputSurface)"
- "e5rt_buffer_object_get_iosurface(_inputBufferObjects[0], &_prevHRSurface)"
- "e5rt_buffer_object_get_iosurface(_inputBufferObjects[1], &_inputSurface)"
- "e5rt_buffer_object_get_iosurface(_inputBufferObjects[1], &_prevHRSurface)"
- "e5rt_execution_stream_operation_retain_output_port(_operation, _outputPortName.UTF8String, &_output_port)"
- "e5rt_io_port_bind_buffer_object(_input_ports[0], _inputBufferObjects[0])"
- "e5rt_io_port_bind_buffer_object(_input_ports[1], _inputBufferObjects[1])"
- "e5rt_io_port_bind_buffer_object(self.output_port, self.outputBufferObject)"
- "e5rt_io_port_retain_tensor_desc(_input_ports[0], &input_tensor_desc0)"
- "e5rt_io_port_retain_tensor_desc(_input_ports[1], &input_tensor_desc1)"
- "e5rt_tensor_desc_alloc_buffer_object(input_tensor_desc0, E5RT_BUFFER_OBJECT_TYPE_IOSURFACE, 1, &_inputBufferObjects[0])"
- "e5rt_tensor_desc_alloc_buffer_object(input_tensor_desc1, E5RT_BUFFER_OBJECT_TYPE_IOSURFACE, 1, &_inputBufferObjects[1])"
- "encodeDenormalizeRGBToCommandBuffer:source:destination:"
- "encodeDiffToCommandBuffer:texture0:texture1:"
- "encodeNormalizationRGBToCommandBuffer:source:destination:"
- "encodeNormalizeLumaToCommandBuffer:source:destination:"
- "encodePostprocessSRFrameToCommandBuffer:srFrameY:bicubicY:bicubicUV:laplacianMask:outputY:outputUV:"
- "encodeUpsampleRBGPackedToCommandBuffer:source:destination:scaleFactor:"
- "encodeUpsampleScaleToCommandBuffer:sourceTexture:destinationTexture:"
- "encodeWarpBlendToCommandBuffer:source:scaleFactor:withLowResFlow:withBicubicUpscaled:withErrorMask:destination:"
- "getColorConsistentOutputRGBVia:bicubicRGB:laplacianMask:attachment:destinationFrame:"
- "initWithDevice:sigma:"
- "maskScaleFactor"
- "maskStrength"
- "normalizeLuma"
- "normalizeLumaFromFrame:toTexture:"
- "normalizeLumaPacked420"
- "normalizeRGB"
- "normalizeRGB:to:"
- "outputBufferObject"
- "outputPortName"
- "output_port"
- "postprocessSRFrame:bicubicYUV:laplacianMask:outputYUV:"
- "prevHRSurface"
- "processSuperResolutionInputBuffer:withPrevHighResolutionFrame:outputBuffer:"
- "scaleOutput"
- "setEdgeMode:"
- "setMaskScaleFactor:"
- "setMaskStrength:"
- "setOutputPortName:"
- "setPrevHRSurface:"
- "setUseLaplacianMask:"
- "upsampleRBGPackedBuffer:to:scaleFactor:"
- "upsampleRGBPackedImage"
- "useLaplacianMask"
- "v44@0:8@16@24@32f40"
- "warpBlendBufferRGBTexture:scaleFactor:withLowResFlowTexture:withBicubicUpscaledTexture:withErrorMaskTexture:toHighResBufferTexture:"
- "warpBlendImageRGB"

```
