## Portrait

> `/System/Library/PrivateFrameworks/Portrait.framework/Portrait`

```diff

-478.0.0.0.0
-  __TEXT.__text: 0x9d474
-  __TEXT.__auth_stubs: 0x13a0
+484.0.0.0.0
+  __TEXT.__text: 0x9dec8
+  __TEXT.__auth_stubs: 0x13c0
   __TEXT.__delay_stubs: 0x2ec
   __TEXT.__delay_helper: 0x230
-  __TEXT.__objc_methlist: 0x980c
+  __TEXT.__objc_methlist: 0x988c
   __TEXT.__const: 0x21260
-  __TEXT.__cstring: 0x6f10
-  __TEXT.__oslogstring: 0x4864
-  __TEXT.__gcc_except_tab: 0x171c
+  __TEXT.__cstring: 0x6f71
+  __TEXT.__oslogstring: 0x4923
+  __TEXT.__gcc_except_tab: 0x1790
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x2130
-  __TEXT.__objc_classname: 0x13a8
-  __TEXT.__objc_methname: 0x1a923
-  __TEXT.__objc_methtype: 0x5800
-  __TEXT.__objc_stubs: 0xf920
-  __DATA_CONST.__got: 0x8f0
+  __TEXT.__unwind_info: 0x2140
+  __TEXT.__objc_classname: 0x13a7
+  __TEXT.__objc_methname: 0x1ab6e
+  __TEXT.__objc_methtype: 0x583b
+  __TEXT.__objc_stubs: 0xfaa0
+  __DATA_CONST.__got: 0x900
   __DATA_CONST.__const: 0xa00
   __DATA_CONST.__objc_classlist: 0x580
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4fb8
+  __DATA_CONST.__objc_selrefs: 0x5020
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x4f0
   __DATA_CONST.__objc_arraydata: 0x7a8
   __DATA_CONST.__vfx_script_tbl: 0x50
   __DATA_CONST.__vfx_script_tbx: 0x48
-  __AUTH_CONST.__auth_got: 0xa70
+  __AUTH_CONST.__auth_got: 0xa80
   __AUTH_CONST.__const: 0x400
   __AUTH_CONST.__cfstring: 0x51c0
-  __AUTH_CONST.__objc_const: 0x1ce78
+  __AUTH_CONST.__objc_const: 0x1cf20
   __AUTH_CONST.__objc_intobj: 0xb58
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH.__objc_data: 0x1bd0
   __AUTH.__data: 0x9e0
-  __DATA.__objc_ivar: 0x1768
+  __DATA.__objc_ivar: 0x1770
   __DATA.__data: 0x818
   __DATA.__bss: 0xe40
   __DATA_DIRTY.__objc_data: 0x1b30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8584DB87-AD9C-3838-97E9-1E0CF8C410B6
-  Functions: 4029
-  Symbols:   15040
-  CStrings:  7576
+  UUID: 9BB60BC6-DEFC-32E1-A39A-FCAD4E4B6CBE
+  Functions: 4050
+  Symbols:   15101
+  CStrings:  7609
 
Symbols:
+ +[PTEffectUtil computeRectInPixelCoordinates:pixelBufferSize:alignment:]
+ -[PTEffect _createQueuesIfNotProvided]
+ -[PTEffect _createQueuesIfNotProvided].cold.1
+ -[PTEffectDescriptor asyncInitQueue]
+ -[PTEffectDescriptor asyncProcessingQueue]
+ -[PTEffectDescriptor setAsyncInitQueue:]
+ -[PTEffectDescriptor setAsyncProcessingQueue:]
+ -[PTEffectPersonSegmentation runPersonSegmentationToOutPersonSegmentationMatteBuffer:inColor:inSegmentationRGBA:inSegmentationRGBATexture:outUpscaledSegmentation:]
+ -[PTEffectPersonSegmentation runPersonSegmentationToOutPersonSegmentationMatteBuffer:inColor:inSegmentationRGBA:inSegmentationRGBATexture:outUpscaledSegmentation:].cold.1
+ -[PTEffectPersonSegmentation runPersonSegmentationToOutPersonSegmentationMatteBuffer:inColor:inSegmentationRGBA:inSegmentationRGBATexture:outUpscaledSegmentation:].cold.2
+ -[PTEffectReaction setStartTimeSeconds:]
+ -[PTEffectReaction startTimeSeconds]
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:]
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.1
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.10
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.11
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.12
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.13
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.14
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.15
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.16
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.17
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.18
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.19
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.2
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.20
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.21
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.22
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.23
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.24
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.25
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.26
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.27
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.28
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.29
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.3
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.30
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.31
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.32
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.33
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.34
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.35
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.4
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.5
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.6
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.7
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.8
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:].cold.9
+ -[PTMSRResize addAdditionalOutput:allowCompressed:pixelFormat:highQuality:]
+ -[PTMSRResize addAdditionalOutput:allowCompressed:pixelFormat:highQuality:].cold.1
+ -[PTMSRResize enablePyramidDownsampling]
+ -[PTMSRResize setEnablePyramidDownsampling:]
+ -[PTMSRResizeAdditionalOutput .cxx_destruct]
+ -[PTMSRResizeAdditionalOutput enabled]
+ -[PTMSRResizeAdditionalOutput initWithSize:colorSpace:pixelFormat:allowCompressed:metalDevice:]
+ -[PTMSRResizeAdditionalOutput initWithSize:colorSpace:pixelFormat:allowCompressed:metalDevice:].cold.1
+ -[PTMSRResizeAdditionalOutput setEnabled:]
+ -[PTMSRResizeAdditionalOutput texture]
+ -[PTVFXRenderEffect dealloc]
+ -[PTVFXRenderEffect renderWithBackgroundDimming:effectRGBA:inCenteredDisparity:inSegmentation:effectDepth:disparityFiltered:focusDisparityModifiers:renderRequest:debugType:].cold.1
+ -[PTVFXRenderEffect renderWithBackgroundDimming:effectRGBA:inCenteredDisparity:inSegmentation:effectDepth:disparityFiltered:focusDisparityModifiers:renderRequest:debugType:].cold.2
+ GCC_except_table34
+ GCC_except_table37
+ GCC_except_table40
+ GCC_except_table47
+ GCC_except_table56
+ GCC_except_table58
+ GCC_except_table71
+ _OBJC_IVAR_$_PTEffectDescriptor._asyncInitQueue
+ _OBJC_IVAR_$_PTEffectDescriptor._asyncProcessingQueue
+ _OBJC_IVAR_$_PTEffectReaction._startTimeSeconds
+ _OBJC_IVAR_$_PTMSRResize._enablePyramidDownsampling
+ _OBJC_IVAR_$_PTMSRResize._inputSize
+ _OBJC_IVAR_$_PTMSRResizeAdditionalOutput._enabled
+ _OBJC_IVAR_$_PTMSRResizeAdditionalOutput._texture
+ __OBJC_$_PROP_LIST_PTMSRResize
+ ___122-[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:]_block_invoke
+ ___28-[PTVFXRenderEffect dealloc]_block_invoke
+ ___block_literal_global.135
+ ___block_literal_global.154
+ __dispatch_main_q
+ _dispatch_after
+ _dispatch_time
+ _objc_msgSend$_createQueuesIfNotProvided
+ _objc_msgSend$_purgeDevice
+ _objc_msgSend$addAdditionalOutput:allowCompressed:pixelFormat:highQuality:
+ _objc_msgSend$asRGBA
+ _objc_msgSend$asyncInitQueue
+ _objc_msgSend$asyncProcessingQueue
+ _objc_msgSend$computeRectInPixelCoordinates:pixelBufferSize:alignment:
+ _objc_msgSend$enabled
+ _objc_msgSend$getMTLTextureFromPixelBuffer:device:
+ _objc_msgSend$initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:
+ _objc_msgSend$initWithSize:colorSpace:pixelFormat:allowCompressed:metalDevice:
+ _objc_msgSend$runPersonSegmentationToOutPersonSegmentationMatteBuffer:inColor:inSegmentationRGBA:inSegmentationRGBATexture:outUpscaledSegmentation:
+ _objc_msgSend$setAsyncInitQueue:
+ _objc_msgSend$setAsyncProcessingQueue:
+ _objc_msgSend$setEnablePyramidDownsampling:
+ _objc_msgSend$setEnabled:
+ _objc_msgSend$setStartTimeSeconds:
+ _objc_msgSend$startTimeSeconds
+ _objc_msgSend$texture
+ _purgeMetalDevice
+ _purgeMetalDevice.cold.1
+ _purgeMetalDevice.cold.2
- +[PTDisparityPostProcessing prewarmForMediaserverd]
- +[PTEffect prewarmForMediaserverd]
- +[PTRenderPipeline prewarmForMediaserverd]
- -[PTEffectPersonSegmentation runPersonSegmentationToOutPersonSegmentationMatteBuffer:inRGBA:outUpscaledSegmentation:]
- -[PTEffectPersonSegmentation runPersonSegmentationToOutPersonSegmentationMatteBuffer:inRGBA:outUpscaledSegmentation:].cold.1
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:]
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.1
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.10
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.11
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.12
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.13
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.14
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.15
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.16
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.17
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.18
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.19
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.2
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.20
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.21
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.22
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.23
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.24
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.25
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.26
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.27
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.28
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.29
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.3
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.30
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.31
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.32
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.33
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.34
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.35
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.4
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.5
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.6
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.7
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.8
- -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.9
- -[PTMSRResize addAdditionalOutput:allowCompressed:pixelFormat:]
- -[PTMSRResize addAdditionalOutput:allowCompressed:pixelFormat:].cold.1
- -[PTMSRResizeAdditionalOutput initWithSize:colorSpace:pixelFormat:allowCompressed:]
- -[PTMSRResizeAdditionalOutput initWithSize:colorSpace:pixelFormat:allowCompressed:].cold.1
- GCC_except_table29
- GCC_except_table32
- GCC_except_table48
- GCC_except_table50
- GCC_except_table67
- _OBJC_IVAR_$_PTEffect._asyncInitQueue
- _OBJC_IVAR_$_PTEffectPersonSegmentation._guideRGBACoefficientsSegmentation
- _OBJC_IVAR_$_PTEffectPersonSegmentationViSegHQVisionCoreE5._asyncDispatchQueue
- _OBJC_IVAR_$_PTEffectRenderer._asyncInitQueue
- _OBJC_IVAR_$_PTEffectRenderer._asyncQueue
- ___137-[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:]_block_invoke
- ___block_literal_global.122
- ___block_literal_global.141
- _objc_msgSend$addAdditionalOutput:allowCompressed:
- _objc_msgSend$addAdditionalOutput:allowCompressed:pixelFormat:
- _objc_msgSend$allowCompressed
- _objc_msgSend$initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:
- _objc_msgSend$initWithSize:colorSpace:pixelFormat:allowCompressed:
- _objc_msgSend$prewarmForCameraCaptured
- _objc_msgSend$runPersonSegmentationToOutPersonSegmentationMatteBuffer:inRGBA:outUpscaledSegmentation:
CStrings:
+ "#\xf0\xf0\xf0b#"
+ "56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}164852"
+ "@\"PTMSRResizeAdditionalOutput\""
+ "@44@0:8{?=QQQ}16B40"
+ "@52@0:8{?=QQQ}16B40I44B48"
+ "@64@0:8@16@24q32@40@48@56"
+ "@64@0:8{?=QQQ}16^{CGColorSpace=}40I48B52@56"
+ "Async init queue not provided, creating one"
+ "Async processing queue not provided, creating one"
+ "Force [_MTLDevice _purgeDevice]"
+ "Force [_MTLDevice _purgeDevice] not supported"
+ "T@\"<MTLTexture>\",R,V_texture"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_asyncInitQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_asyncProcessingQueue"
+ "TB,V_enablePyramidDownsampling"
+ "TB,V_enabled"
+ "Td,V_startTimeSeconds"
+ "Unexpected texture"
+ "_asyncProcessingQueue"
+ "_createQueuesIfNotProvided"
+ "_enablePyramidDownsampling"
+ "_enabled"
+ "_inputSize"
+ "_purgeDevice"
+ "_startTimeSeconds"
+ "_texture"
+ "addAdditionalOutput:allowCompressed:pixelFormat:highQuality:"
+ "asyncInitQueue"
+ "asyncProcessingQueue"
+ "com.apple.portrait.effect_processing"
+ "com.apple.portrait.espresso_callback"
+ "computeRectInPixelCoordinates:pixelBufferSize:alignment:"
+ "enablePyramidDownsampling"
+ "i56@0:8@16@24^{__CVBuffer=}32@40@48"
+ "initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:sharedResources:"
+ "initWithSize:colorSpace:pixelFormat:allowCompressed:metalDevice:"
+ "rect[2] == effectRGBA.width"
+ "rect[3] == effectRGBA.height"
+ "runPersonSegmentationToOutPersonSegmentationMatteBuffer:inColor:inSegmentationRGBA:inSegmentationRGBATexture:outUpscaledSegmentation:"
+ "setAsyncInitQueue:"
+ "setAsyncProcessingQueue:"
+ "setEnablePyramidDownsampling:"
+ "setEnabled:"
+ "setStartTimeSeconds:"
+ "startTimeSeconds"
+ "texture"
- "#\xf0\xf0\xf0b$"
- "@56@0:8{?=QQQ}16^{CGColorSpace=}40I48B52"
- "@72@0:8@16@24q32@40@48@56@64"
- "^{__CVBuffer=}44@0:8{?=QQQ}16B40"
- "^{__CVBuffer=}48@0:8{?=QQQ}16B40I44"
- "_asyncQueue"
- "_guideRGBACoefficientsSegmentation"
- "addAdditionalOutput:allowCompressed:pixelFormat:"
- "com.apple.portrait.async_queue"
- "i40@0:8@16^{__CVBuffer=}24@32"
- "initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:"
- "initWithSize:colorSpace:pixelFormat:allowCompressed:"
- "monocular-depth-sync"
- "prewarmForMediaserverd"
- "runPersonSegmentationToOutPersonSegmentationMatteBuffer:inRGBA:outUpscaledSegmentation:"

```
