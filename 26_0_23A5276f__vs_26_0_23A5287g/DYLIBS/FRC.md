## FRC

> `/System/Library/PrivateFrameworks/FRC.framework/FRC`

```diff

-228.0.0.0.0
-  __TEXT.__text: 0x312ec
+229.0.0.0.0
+  __TEXT.__text: 0x320b0
   __TEXT.__auth_stubs: 0xe30
-  __TEXT.__objc_methlist: 0x2da4
+  __TEXT.__objc_methlist: 0x2e4c
   __TEXT.__const: 0x560
-  __TEXT.__cstring: 0x54de
+  __TEXT.__cstring: 0x56de
   __TEXT.__oslogstring: 0x76e
   __TEXT.__gcc_except_tab: 0x12c
-  __TEXT.__unwind_info: 0x960
-  __TEXT.__objc_classname: 0x337
-  __TEXT.__objc_methname: 0xb11d
-  __TEXT.__objc_methtype: 0x3471
-  __TEXT.__objc_stubs: 0x55c0
-  __DATA_CONST.__got: 0x400
+  __TEXT.__unwind_info: 0x980
+  __TEXT.__objc_classname: 0x340
+  __TEXT.__objc_methname: 0xb32e
+  __TEXT.__objc_methtype: 0x3574
+  __TEXT.__objc_stubs: 0x56c0
+  __DATA_CONST.__got: 0x408
   __DATA_CONST.__const: 0x508
-  __DATA_CONST.__objc_classlist: 0x138
+  __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c28
-  __DATA_CONST.__objc_superrefs: 0x100
+  __DATA_CONST.__objc_selrefs: 0x1c68
+  __DATA_CONST.__objc_superrefs: 0x108
   __AUTH_CONST.__auth_got: 0x728
   __AUTH_CONST.__const: 0xd8
-  __AUTH_CONST.__cfstring: 0x3200
-  __AUTH_CONST.__objc_const: 0x80e0
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0xa28
+  __AUTH_CONST.__cfstring: 0x3280
+  __AUTH_CONST.__objc_const: 0x8268
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0xa44
   __DATA.__data: 0x140
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0xbe0

   - /System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DB2B0F79-FE93-33E0-9B02-524BEC441823
-  Functions: 1063
-  Symbols:   4061
-  CStrings:  3036
+  UUID: 0CE8CE6B-D4D7-361B-B924-43A96CBA054A
+  Functions: 1082
+  Symbols:   4118
+  CStrings:  3072
 
Symbols:
+ -[FRCBlit .cxx_destruct]
+ -[FRCBlit copyBuffer:toTexture:commandBuffer:]
+ -[FRCBlit copyTexture:toBuffer:commandBuffer:]
+ -[FRCBlit init]
+ -[FRCBlit setupMetal]
+ -[FRCLivePhotoMetadataReader stillImageTransformAvailable]
+ -[FRCOpticalFlowEstimator flowAdaptationFrom:to:inputFlow:outputFlow:]
+ -[OpticalFlow createTexturesFromCVPixelBuffer:interleave:arrayLength:withCommandBuffer:]
+ -[OpticalFlow flowAdaptationFirstFrame:secondFrame:inputFlow:outputFlow:]
+ -[OpticalFlow reshuffleFlow:previousFlow:destination:waitForComplete:]
+ -[OpticalFlow setUseE5RT:]
+ -[OpticalFlow subsampleBuffer:destination:toCommandBuffer:]
+ -[OpticalFlow useE5RT]
+ -[OpticalFlowE5 encodeUnormNormalize:destination:toCommandBuffer:]
+ -[OpticalFlowE5 opticalFlowFirstFrame:secondFrame:originalFirst:originalSecond:flow:]
+ -[OpticalFlowE5 rotationForBuffer:]
+ _OBJC_CLASS_$_FRCBlit
+ _OBJC_IVAR_$_FRCBlit._bufferToTexture
+ _OBJC_IVAR_$_FRCBlit._bufferToTextureTwoComponent
+ _OBJC_IVAR_$_FRCBlit._textureToBuffer
+ _OBJC_IVAR_$_FRCBlit._textureToBufferTwoComponent
+ _OBJC_IVAR_$_FRCLivePhotoMetadataReader._stillImageTransformAvailable
+ _OBJC_IVAR_$_OpticalFlow._blit
+ _OBJC_IVAR_$_OpticalFlow._useE5RT
+ _OBJC_IVAR_$_OpticalFlowE5._subsampledBGRAFirst
+ _OBJC_IVAR_$_OpticalFlowE5._subsampledBGRASecond
+ _OBJC_METACLASS_$_FRCBlit
+ __OBJC_$_INSTANCE_METHODS_FRCBlit
+ __OBJC_$_INSTANCE_VARIABLES_FRCBlit
+ __OBJC_CLASS_RO_$_FRCBlit
+ __OBJC_METACLASS_RO_$_FRCBlit
+ _convertOneComponet16HalfToTwoComponent16Half
+ _convertOneComponet16HalfToTwoComponent16Half.cold.1
+ _convertOneComponet16HalfToTwoComponent16Half.cold.2
+ _convertTwoComponet16HalfToOneComponent16Half
+ _convertTwoComponet16HalfToOneComponent16Half.cold.1
+ _convertTwoComponet16HalfToOneComponent16Half.cold.2
+ _objc_msgSend$copyBuffer:toTexture:commandBuffer:
+ _objc_msgSend$copyTexture:toBuffer:commandBuffer:
+ _objc_msgSend$createTexturesFromCVPixelBuffer:interleave:arrayLength:withCommandBuffer:
+ _objc_msgSend$encodeUnormNormalize:destination:toCommandBuffer:
+ _objc_msgSend$flowAdaptationFirstFrame:secondFrame:inputFlow:outputFlow:
+ _objc_msgSend$opticalFlowFirstFrame:secondFrame:originalFirst:originalSecond:flow:
+ _objc_msgSend$reshuffleFlow:previousFlow:destination:waitForComplete:
+ _objc_msgSend$rotationForBuffer:
+ _objc_msgSend$setUseE5RT:
+ _objc_msgSend$subsampleBuffer:destination:toCommandBuffer:
- -[FRCLivePhotoMetadataReader stillImageTransformAvailble]
- -[OpticalFlow reshuffleFlow:previsouFlow:destination:waitForComplete:]
- -[OpticalFlowE5 subsampleAndNormalizeInput:to:]
- _OBJC_IVAR_$_FRCLivePhotoMetadataReader._stillImageTransformAvailble
- _OBJC_IVAR_$_OpticalFlowE5._subsampledBGRA
- _objc_msgSend$reshuffleFlow:previsouFlow:destination:waitForComplete:
- _objc_msgSend$subsampleAndNormalizeInput:to:
CStrings:
+ "@\"FRCBlit\""
+ "@48@0:8^{__CVBuffer=}16Q24Q32@40"
+ "Execution failed. returned error = %u. msg = %s\n"
+ "FRCBlit"
+ "Pre-compiled E5 Bundle for %@ is not available. Switching to runtime compilation."
+ "TB,R,N,V_stillImageTransformAvailable"
+ "_blit"
+ "_bufferToTexture"
+ "_bufferToTextureTwoComponent"
+ "_stillImageTransformAvailable"
+ "_subsampledBGRAFirst"
+ "_subsampledBGRASecond"
+ "_textureToBuffer"
+ "_textureToBufferTwoComponent"
+ "bufferToTexture"
+ "bufferToTwoComponentTexture"
+ "convertOneComponet16HalfToTwoComponent16Half"
+ "convertTwoComponet16HalfToOneComponent16Half"
+ "copyBuffer:toTexture:commandBuffer:"
+ "copyTexture:toBuffer:commandBuffer:"
+ "createTexturesFromCVPixelBuffer:interleave:arrayLength:withCommandBuffer:"
+ "encodeUnormNormalize:destination:toCommandBuffer:"
+ "flowAdaptationFirstFrame:secondFrame:inputFlow:outputFlow:"
+ "flowAdaptationFrom:to:inputFlow:outputFlow:"
+ "kCVPixelFormatType_OneComponent16Half == CVPixelBufferGetPixelFormatType(destination)"
+ "kCVPixelFormatType_OneComponent16Half == CVPixelBufferGetPixelFormatType(source)"
+ "kCVPixelFormatType_TwoComponent16Half == CVPixelBufferGetPixelFormatType(destination)"
+ "kCVPixelFormatType_TwoComponent16Half == CVPixelBufferGetPixelFormatType(source)"
+ "opticalFlowFirstFrame:secondFrame:originalFirst:originalSecond:flow:"
+ "q24@0:8^{__CVBuffer=}16"
+ "reshuffleFlow:previousFlow:destination:waitForComplete:"
+ "rotationForBuffer:"
+ "stillImageTransformAvailable"
+ "subsampleBuffer:destination:toCommandBuffer:"
+ "textureToBuffer"
+ "twoComponentTextureToBuffer"
+ "v40@0:8@16^{__CVBuffer=}24@32"
+ "v40@0:8^{__CVBuffer=}16@24@32"
+ "v40@0:8^{__CVBuffer=}16^{__CVBuffer=}24@32"
+ "v56@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40^{__CVBuffer=}48"
- "Excecution failed. returned error = %u. msg = %s\n"
- "Pre-compiled E5 Bundle for %@ is not availble. Switching to runtime compilation."
- "TB,R,N,V_stillImageTransformAvailble"
- "_stillImageTransformAvailble"
- "_subsampledBGRA"
- "reshuffleFlow:previsouFlow:destination:waitForComplete:"
- "stillImageTransformAvailble"
- "subsampleAndNormalizeInput:to:"

```
