## Portrait

> `/System/Library/PrivateFrameworks/Portrait.framework/Portrait`

```diff

-436.120.4.0.0
-  __TEXT.__text: 0x9a188
-  __TEXT.__auth_stubs: 0x11a0
+478.0.0.0.0
+  __TEXT.__text: 0x9d474
+  __TEXT.__auth_stubs: 0x13a0
   __TEXT.__delay_stubs: 0x2ec
-  __TEXT.__delay_helper: 0x110
-  __TEXT.__objc_methlist: 0x94e4
-  __TEXT.__const: 0x21270
-  __TEXT.__cstring: 0x7a6c
-  __TEXT.__oslogstring: 0x4662
-  __TEXT.__gcc_except_tab: 0x698
+  __TEXT.__delay_helper: 0x230
+  __TEXT.__objc_methlist: 0x980c
+  __TEXT.__const: 0x21260
+  __TEXT.__cstring: 0x6f10
+  __TEXT.__oslogstring: 0x4864
+  __TEXT.__gcc_except_tab: 0x171c
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x2140
-  __TEXT.__objc_classname: 0x130d
-  __TEXT.__objc_methname: 0x1a2c1
-  __TEXT.__objc_methtype: 0x569e
-  __TEXT.__objc_stubs: 0xf660
-  __DATA_CONST.__got: 0x8e8
-  __DATA_CONST.__const: 0x7b8
-  __DATA_CONST.__objc_classlist: 0x560
+  __TEXT.__unwind_info: 0x2130
+  __TEXT.__objc_classname: 0x13a8
+  __TEXT.__objc_methname: 0x1a923
+  __TEXT.__objc_methtype: 0x5800
+  __TEXT.__objc_stubs: 0xf920
+  __DATA_CONST.__got: 0x8f0
+  __DATA_CONST.__const: 0xa00
+  __DATA_CONST.__objc_classlist: 0x580
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4e80
+  __DATA_CONST.__objc_selrefs: 0x4fb8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x4c8
-  __DATA_CONST.__objc_arraydata: 0x678
-  __AUTH_CONST.__auth_got: 0x970
-  __AUTH_CONST.__const: 0x2e0
-  __AUTH_CONST.__cfstring: 0x5080
-  __AUTH_CONST.__objc_const: 0x1c4e0
-  __AUTH_CONST.__objc_intobj: 0x990
+  __DATA_CONST.__objc_superrefs: 0x4f0
+  __DATA_CONST.__objc_arraydata: 0x7a8
+  __DATA_CONST.__vfx_script_tbl: 0x50
+  __DATA_CONST.__vfx_script_tbx: 0x48
+  __AUTH_CONST.__auth_got: 0xa70
+  __AUTH_CONST.__const: 0x400
+  __AUTH_CONST.__cfstring: 0x51c0
+  __AUTH_CONST.__objc_const: 0x1ce78
+  __AUTH_CONST.__objc_intobj: 0xb58
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH.__objc_data: 0x1b80
-  __AUTH.__data: 0xbd0
-  __DATA.__objc_ivar: 0x16fc
-  __DATA.__data: 0x810
-  __DATA.__bss: 0x208
-  __DATA_DIRTY.__objc_data: 0x1a40
+  __AUTH_CONST.__objc_dictobj: 0x168
+  __AUTH.__objc_data: 0x1bd0
+  __AUTH.__data: 0x9e0
+  __DATA.__objc_ivar: 0x1768
+  __DATA.__data: 0x818
+  __DATA.__bss: 0xe40
+  __DATA_DIRTY.__objc_data: 0x1b30
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /System/Library/Frameworks/Vision.framework/Vision
   - /System/Library/PrivateFrameworks/AppleDepth.framework/AppleDepth
+  - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
   - /System/Library/PrivateFrameworks/FusionTracker.framework/FusionTracker
   - /System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 98736B97-C87B-3747-94E3-B477D58DA4A3
-  Functions: 4056
-  Symbols:   14459
-  CStrings:  7412
+  UUID: 8584DB87-AD9C-3838-97E9-1E0CF8C410B6
+  Functions: 4029
+  Symbols:   15040
+  CStrings:  7576
 
Symbols:
+ +[PTCVMNetwork depthPrioritizationFromEffectQuality:]
+ +[PTCVMNetwork isSupported]
+ +[PTColorConversion getChromaOffset:]
+ +[PTEffectPersonSegmentationViSegHQVisionCoreE5 segmentationSizeForColorSize:]
+ +[PTEffectPersonSegmentationViSegHQVisionCoreE5 segmentationSizeForColorSize:].cold.1
+ +[PTImageblockConfig adjustScissorRectToImageBlocks:imageBlockSize:]
+ +[PTLKTFlow _computeScalingFactor:dst_tex:scale_xy_inv:coeff:]
+ +[PTLKTFlow _computeScalingFactor:dst_tex:scale_xy_inv:coeff:].cold.1
+ +[PTMetalTextureUtil macroBlockSizeForPixelFormat:device:]
+ +[PTPixelBufferUtil compressedPixelFormat:]
+ +[PTPixelBufferUtil compressedPixelFormat:compression:]
+ +[PTPixelBufferUtil compressedPixelFormat:compression:].cold.1
+ +[PTPixelBufferUtil createTextureFromPixelBuffer:device:textureCache:sRGB:metalYCBCRConversion:]
+ +[PTPixelBufferUtil createTextureFromPixelBuffer:device:textureCache:sRGB:metalYCBCRConversion:].cold.1
+ +[PTPixelBufferUtil getMTLTextureDescriptor:device:metalYCBCRConversion:]
+ +[PTPixelBufferUtil getMTLTextureDescriptor:device:metalYCBCRConversion:].cold.1
+ +[PTPixelBufferUtil is420YpCbCr8:]
+ +[PTPixelBufferUtil supportsMetalYCBCRConversion:]
+ +[PTPixelBufferUtil supportsMetalYCBCRConversion]
+ +[PTPixelBufferUtil supportsMetalYCBCRConversion].cold.1
+ +[PTRaytracingUtils createFocusObject:anamorphicFactor:radialObstructionFactor:colorSize:circleOfConfusionReference:fNumberLimitWeight:]
+ +[PTTexture createFromPixelbuffer:device:textureCache:metalYCBCRConversion:read:write:]
+ +[PTTexture createFromPixelbuffer:device:textureCache:metalYCBCRConversion:read:write:].cold.1
+ +[PTTexture createFromPixelbuffer:device:textureCache:metalYCBCRConversion:read:write:].cold.2
+ +[PTTexture createFromPixelbuffer:device:textureCache:metalYCBCRConversion:read:write:].cold.3
+ -[PTBackgroundReplacement applyPortraitBlur:inColorBuffer:inColorPyramid:inBackgroundBuffer:effectRenderRequest:]
+ -[PTBackgroundReplacement replaceBackground:inColor:inColorPyramid:inSegmentation:effectRenderRequest:outColor:frameIndex:]
+ -[PTBackgroundReplacement replaceBackground:inColor:inColorPyramid:inSegmentation:effectRenderRequest:outColor:frameIndex:].cold.1
+ -[PTBackgroundReplacement replaceBackground:inColor:inColorPyramid:inSegmentation:effectRenderRequest:outColor:frameIndex:].cold.2
+ -[PTBackgroundReplacement replaceBackground:inColor:inColorPyramid:inSegmentation:effectRenderRequest:outColor:frameIndex:].cold.3
+ -[PTBackgroundReplacement replaceBackground:inColor:inColorPyramid:inSegmentation:effectRenderRequest:outColor:frameIndex:].cold.4
+ -[PTCVMNetwork depthPrioritization]
+ -[PTCVMNetwork initWithMetalContext:colorSize:depthPrioritization:sharedResources:]
+ -[PTCVMNetwork initWithMetalContext:colorSize:depthPrioritization:sharedResources:].cold.1
+ -[PTCVMNetwork initWithMetalContext:colorSize:depthPrioritization:sharedResources:].cold.2
+ -[PTCVMNetwork initWithMetalContext:colorSize:depthPrioritization:sharedResources:].cold.3
+ -[PTCVMNetwork initWithMetalContext:colorSize:depthPrioritization:sharedResources:].cold.4
+ -[PTCVMNetwork initWithMetalContext:colorSize:depthPrioritization:sharedResources:].cold.5
+ -[PTCVMNetwork initWithMetalContext:colorSize:depthPrioritization:sharedResources:].cold.6
+ -[PTCVMNetwork initWithMetalContext:colorSize:depthPrioritization:sharedResources:].cold.7
+ -[PTCVMNetwork initWithMetalContext:colorSize:depthPrioritization:sharedResources:].cold.8
+ -[PTCVMNetwork initWithMetalContext:colorSize:depthPrioritization:sharedResources:].cold.9
+ -[PTColorTemperatureCorrection estimateColorTemperatureFromBackground:colorTransferFunction:matrixYUVtoRGB:inBackgroundLuma:inBackgroundChroma:outColorTemperatureBuffer:]
+ -[PTDisparityPostProcessing computeOpticalFlow:outDisplacement:].cold.1
+ -[PTDisparityPostProcessing temporalDisparityFilter:inDisplacement:inDisparityFilteredPrev:outDisparityFiltered:disparityBias:].cold.1
+ -[PTDisparityPostProcessing temporalDisparityFilter:inStatePrev:inDisparity:outDisparityFiltered:outState:].cold.1
+ -[PTEffect initWithDescriptor:sharedResources:].cold.3
+ -[PTEffect initWithDescriptor:sharedResources:].cold.4
+ -[PTEffect reconfigure:isInitialized:]
+ -[PTEffect reconfigureWithNewSize:]
+ -[PTEffect resetIfNeeded]
+ -[PTEffect resetIfNeeded].cold.1
+ -[PTEffect updateHumanDetections:]
+ -[PTEffectComposition .cxx_destruct]
+ -[PTEffectComposition computeDownsamplingFactorWithInputSource:inputTarget:renderRequest:]
+ -[PTEffectComposition initWithConfig:]
+ -[PTEffectComposition initWithConfig:].cold.1
+ -[PTEffectComposition initWithConfig:].cold.2
+ -[PTEffectComposition initWithConfig:].cold.3
+ -[PTEffectComposition initWithConfig:].cold.4
+ -[PTEffectComposition render:renderRequest:]
+ -[PTEffectComposition render:renderRequest:].cold.1
+ -[PTEffectComposition render:renderRequest:].cold.2
+ -[PTEffectComposition render:renderRequest:].cold.3
+ -[PTEffectCompositionConfig .cxx_destruct]
+ -[PTEffectCompositionConfig device]
+ -[PTEffectCompositionConfig setDevice:]
+ -[PTEffectCompositionRenderRequest inputCropRect]
+ -[PTEffectCompositionRenderRequest inputSourcePixelBuffer]
+ -[PTEffectCompositionRenderRequest inputTargetPixelBuffer]
+ -[PTEffectCompositionRenderRequest inputTargetRectCornerRadius]
+ -[PTEffectCompositionRenderRequest inputTargetRect]
+ -[PTEffectCompositionRenderRequest outputPixelBuffer]
+ -[PTEffectCompositionRenderRequest setInputCropRect:]
+ -[PTEffectCompositionRenderRequest setInputSourcePixelBuffer:]
+ -[PTEffectCompositionRenderRequest setInputTargetPixelBuffer:]
+ -[PTEffectCompositionRenderRequest setInputTargetRect:]
+ -[PTEffectCompositionRenderRequest setInputTargetRectCornerRadius:]
+ -[PTEffectCompositionRenderRequest setOutputPixelBuffer:]
+ -[PTEffectDebugLayer initWithMetalContext:effectRelighting:effectDescritor:renderState:util:colorConversion:msrColorPyramid:vfxRenderEffect:depthConverter:disparityFixedFocus:faceDisparityArray:focusDisparityRaw:focusDisparityModifiers:]
+ -[PTEffectDebugLayer renderDebugInformation:effectRenderRequest:reactionStates:disparity:disparityCentered:normal:diffuse:temporalFilter:humanDetections:transform:fNumber:focusDisparityRaw:useDisparityBufferForReactions:outColor:]
+ -[PTEffectDebugLayer renderDebugInformation:effectRenderRequest:reactionStates:disparity:disparityCentered:normal:diffuse:temporalFilter:humanDetections:transform:fNumber:focusDisparityRaw:useDisparityBufferForReactions:outColor:].cold.1
+ -[PTEffectDescriptor init]
+ -[PTEffectDescriptor isEqual:]
+ -[PTEffectPersonSegmentation initWithMetalContext:colorSize:msrColorPyramid:cvmNetwork:effectQuality:prewarmOnly:sharedResources:].cold.5
+ -[PTEffectPersonSegmentation runPersonSegmentationToOutPersonSegmentationMatteBuffer:inRGBA:outUpscaledSegmentation:].cold.1
+ -[PTEffectPersonSegmentationViSegHQVisionCore colorSize]
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 .cxx_destruct]
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 clearIOSurface:value:]
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 clearIOSurface:value:].cold.1
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 clearIOSurface:value:].cold.2
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 colorSize]
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 createEspressoBuffer:fromNetwork:name:isInput:]
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 createEspressoBuffer:fromNetwork:name:isInput:].cold.1
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 createEspressoBuffer:fromNetwork:name:isInput:].cold.2
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 dealloc]
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 dealloc].cold.1
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 debugTextures]
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:]
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.1
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.10
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.11
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.12
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.13
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.14
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.15
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.16
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.17
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.18
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.19
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.2
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.20
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.21
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.22
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.23
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.24
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.25
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.26
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.27
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.28
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.3
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.4
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.5
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.6
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.7
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.8
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 initWithMetalContext:colorSize:].cold.9
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 outputPixelbuffer]
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 postProcessUpdateFrame]
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 postProcessUpdateFrame].cold.1
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 reset]
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 reset].cold.1
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:]
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.1
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.10
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.11
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.12
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.13
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.14
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.15
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.16
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.17
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.18
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.19
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.2
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.20
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.21
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.22
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.23
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.24
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.25
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.3
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.4
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.5
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.6
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.7
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.8
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:].cold.9
+ -[PTEffectReaction init]
+ -[PTEffectRelighting initWithMetalContext:availableEffectTypes:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:]
+ -[PTEffectRelighting initWithMetalContext:availableEffectTypes:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.1
+ -[PTEffectRelighting initWithMetalContext:availableEffectTypes:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.10
+ -[PTEffectRelighting initWithMetalContext:availableEffectTypes:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.11
+ -[PTEffectRelighting initWithMetalContext:availableEffectTypes:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.2
+ -[PTEffectRelighting initWithMetalContext:availableEffectTypes:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.3
+ -[PTEffectRelighting initWithMetalContext:availableEffectTypes:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.4
+ -[PTEffectRelighting initWithMetalContext:availableEffectTypes:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.5
+ -[PTEffectRelighting initWithMetalContext:availableEffectTypes:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.6
+ -[PTEffectRelighting initWithMetalContext:availableEffectTypes:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.7
+ -[PTEffectRelighting initWithMetalContext:availableEffectTypes:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.8
+ -[PTEffectRelighting initWithMetalContext:availableEffectTypes:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.9
+ -[PTEffectRelighting studioLightInColor:inDiffuse:inDisparity:inFocusDisparityModifier:outColor:relightStrength:studioLightFromSegmentationBlend:studioLightEffectModifier:]
+ -[PTEffectRelighting studioLightInColor:inDiffuse:inDisparity:inFocusDisparityModifier:outColor:relightStrength:studioLightFromSegmentationBlend:studioLightEffectModifier:].cold.1
+ -[PTEffectRenderRequest alsColor]
+ -[PTEffectRenderRequest alsLuxLevel]
+ -[PTEffectRenderRequest ambientLightSensor]
+ -[PTEffectRenderRequest metadataDictionary]
+ -[PTEffectRenderRequest setAlsColor:]
+ -[PTEffectRenderRequest setAlsLuxLevel:]
+ -[PTEffectRenderRequest setAmbientLightSensor:]
+ -[PTEffectRenderRequest setMetadataDictionary:]
+ -[PTEffectRenderer copyInColor:toOutColor:]
+ -[PTEffectRenderer copyInColor:toOutColor:].cold.1
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:]
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.1
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.10
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.11
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.12
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.13
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.14
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.15
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.16
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.17
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.18
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.19
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.2
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.20
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.21
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.22
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.23
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.24
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.25
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.26
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.27
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.28
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.29
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.3
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.30
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.31
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.32
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.33
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.34
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.35
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.4
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.5
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.6
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.7
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.8
+ -[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.9
+ -[PTEffectResources effectUtil]
+ -[PTEffectResources faceAttributesNetwork]
+ -[PTEffectResources setEffectUtil:]
+ -[PTEffectResources setUtil:]
+ -[PTEffectResources setVfxResources:]
+ -[PTEffectResources util]
+ -[PTEffectResources vfxResources]
+ -[PTEffectUtil sampleFaceRects:maxFaceRects:faceRects:faceRectsState:focusDisparityMax:inDisparity:outFaceDistanceArray:]
+ -[PTEffectUtil updateDisparity:inScreenCaptureRect:inDisparity:outDisparity:focalLenIn35mmFilm:fNumber:]
+ -[PTEffectUtil updateFocusObject:faceRectCount:disparityFocusOffsetSDOF:disparityFocusOffsetReactions:disparityFocusOffsetStudioLight:exponentialMovingAverageSDOF:exponentialMovingAverageStudioLight:faceRectsState:isFirstFrame:emitNewReaction:focusOnAll:lastFocus:inFaceDisparityArray:outDisparityModifiers:outDisparityFocus:outStudioLightEffectModifier:outUseDisparityBufferForReactions:]
+ -[PTImageblockConfig initWithTextureSize:scissorRect:outRect:imageblockSize:]
+ -[PTInferenceANEConfig E5ExecutionPriority]
+ -[PTInferenceANEConfig E5ExecutionPriority].cold.1
+ -[PTLKTFlow .cxx_destruct]
+ -[PTLKTFlow _computeFeatures:in_tex:out_tex:]
+ -[PTLKTFlow _computeFeaturesDerivatives:in_tex:out_tex:]
+ -[PTLKTFlow _computeOpticalFlow:computeFeatureI0:computeFeatureI1:]
+ -[PTLKTFlow _computeOpticalFlowBidirectional:]
+ -[PTLKTFlow _computeOpticalFlowBidirectional:].cold.1
+ -[PTLKTFlow _createImagePyramid:in_tex:I_idx:]
+ -[PTLKTFlow _doNLRegularization:in_uv_tex:join_tex:w_tex:out_uv_tex:]
+ -[PTLKTFlow _doSolver:scale:in_uv_tex:in_G0_tex:in_G1_tex:in_C0_tex:in_C1_tex:out_uv_tex:out_w_tex:]
+ -[PTLKTFlow _downscale2X:in_tex:out_tex:]
+ -[PTLKTFlow _enqueueFlowConsistency:in_uv0_tex:in_uv1_tex:out_uv_tex:]
+ -[PTLKTFlow _enqueueKeypointsFromFlow:in_uv_fwd_tex:in_uv_bwd_tex:out_kpt_buf:block_size:bidirectional_error:out_num_keypoints:]
+ -[PTLKTFlow _enqueueKeypointsFromFlow:in_uv_fwd_tex:in_uv_bwd_tex:out_kpt_buf:block_size:bidirectional_error:out_num_keypoints:].cold.1
+ -[PTLKTFlow _initMemory:height:nscales:]
+ -[PTLKTFlow _initMemory:height:nscales:].cold.1
+ -[PTLKTFlow _setDefaultParameters]
+ -[PTLKTFlow _setupBuffer:]
+ -[PTLKTFlow _setupBuffer:].cold.1
+ -[PTLKTFlow _setupBuffer:].cold.2
+ -[PTLKTFlow _setupBuffer:].cold.3
+ -[PTLKTFlow _setupPipelines:]
+ -[PTLKTFlow _setupPipelines:].cold.1
+ -[PTLKTFlow _zeroFlow:uv_tex:]
+ -[PTLKTFlow aux_size]
+ -[PTLKTFlow computeKeypointsFromTexForwardFlow:backwardFlow:bidirectionalError:blockSize:outNumKeypoints:commandBuffer:]
+ -[PTLKTFlow estimateFlowFromTexReference:target:commandBuffer:]
+ -[PTLKTFlow estimateFlowStreamTex:commandBuffer:]
+ -[PTLKTFlow estimateFlowStreamTex:index:doOpticalFlow:commandBuffer:]
+ -[PTLKTFlow initWithMetalContext:width:height:nscales:]
+ -[PTLKTFlow initWithMetalContext:width:height:nscales:].cold.1
+ -[PTLKTFlow initWithMetalContext:width:height:nscales:].cold.2
+ -[PTLKTFlow isBidirectional]
+ -[PTLKTFlow isInverse]
+ -[PTLKTFlow isValid]
+ -[PTLKTFlow keypoints]
+ -[PTLKTFlow needConversionBGRA2YUVA]
+ -[PTLKTFlow newBufferWithPixelFormat:width:data:metalContext:]
+ -[PTLKTFlow newBufferWithPixelFormat:width:data:metalContext:].cold.1
+ -[PTLKTFlow nlreg_padding]
+ -[PTLKTFlow nlreg_radius]
+ -[PTLKTFlow nlreg_sigma_c]
+ -[PTLKTFlow nlreg_sigma_l]
+ -[PTLKTFlow nlreg_sigma_w]
+ -[PTLKTFlow nscales]
+ -[PTLKTFlow nwarpings]
+ -[PTLKTFlow ref_size]
+ -[PTLKTFlow reset]
+ -[PTLKTFlow setIsBidirectional:]
+ -[PTLKTFlow setIsInverse:]
+ -[PTLKTFlow setNeedConversionBGRA2YUVA:]
+ -[PTLKTFlow setNlreg_padding:]
+ -[PTLKTFlow setNlreg_radius:]
+ -[PTLKTFlow setNlreg_sigma_c:]
+ -[PTLKTFlow setNlreg_sigma_l:]
+ -[PTLKTFlow setNlreg_sigma_w:]
+ -[PTLKTFlow setNwarpings:]
+ -[PTLKTFlow setOutputTexUV:]
+ -[PTLKTFlow setOutputTexUVForward:backward:]
+ -[PTLKTFlow setPreset:]
+ -[PTLKTFlow setPreset:].cold.1
+ -[PTLKTFlow setUseNonLocalRegularization:]
+ -[PTLKTFlow streamFrameCount]
+ -[PTLKTFlow useNonLocalRegularization]
+ -[PTMSRResize addAdditionalOutput:allowCompressed:]
+ -[PTMSRResize addAdditionalOutput:allowCompressed:pixelFormat:]
+ -[PTMSRResize addAdditionalOutput:allowCompressed:pixelFormat:].cold.1
+ -[PTMSRResize computeDownsamplingStepsWithInputSize:targetSize:]
+ -[PTMSRResize downsample:]
+ -[PTMSRResize downsample:].cold.1
+ -[PTMSRResize downsample:].cold.2
+ -[PTMSRResize downsample:].cold.3
+ -[PTMSRResize downsample:].cold.4
+ -[PTMSRResize downsampleToLayer:source:dest:]
+ -[PTMSRResize initWithMetalContext:inputSize:targetSize:rotateTargetPixelBuffer:compressedIntermediates:sRGB:sharedResources:]
+ -[PTMSRResize initWithMetalContext:inputSize:targetSize:rotateTargetPixelBuffer:compressedIntermediates:sRGB:sharedResources:].cold.1
+ -[PTMSRResize initWithMetalContext:inputSize:targetSize:rotateTargetPixelBuffer:compressedIntermediates:sRGB:sharedResources:].cold.2
+ -[PTMSRResize initWithMetalContext:inputSize:targetSize:rotateTargetPixelBuffer:compressedIntermediates:sRGB:sharedResources:].cold.3
+ -[PTMSRResize initWithMetalContext:inputSize:targetSize:rotateTargetPixelBuffer:compressedIntermediates:sRGB:sharedResources:].cold.4
+ -[PTMSRResize initWithMetalContext:inputSize:targetSize:rotateTargetPixelBuffer:compressedIntermediates:sRGB:sharedResources:].cold.5
+ -[PTMSRResize initWithMetalContext:inputSize:targetSize:rotateTargetPixelBuffer:compressedIntermediates:sRGB:sharedResources:].cold.6
+ -[PTMSRResize transform:crop:rotationDegree:toDest:synchronous:]
+ -[PTMSRResize transform:crop:rotationDegree:toDest:synchronous:].cold.1
+ -[PTMSRResize transform:crop:rotationDegree:toDest:synchronous:].cold.2
+ -[PTMSRResizeAdditionalOutput allowCompressed]
+ -[PTMSRResizeAdditionalOutput initWithSize:colorSpace:pixelFormat:allowCompressed:]
+ -[PTMSRResizeAdditionalOutput initWithSize:colorSpace:pixelFormat:allowCompressed:].cold.1
+ -[PTMSRResizeAdditionalOutput setAllowCompressed:]
+ -[PTMetalContext commandBuffer].cold.3
+ -[PTMetalContext initWithFigMetalContext:]
+ -[PTMetalContext supportsFamily:]
+ -[PTPersonSemanticsNetwork bindInputPixelBuffer:]
+ -[PTPersonSemanticsNetwork initWithMetalContext:sharedResources:]
+ -[PTPersonSemanticsNetwork initWithMetalContext:sharedResources:].cold.1
+ -[PTPersonSemanticsNetwork initWithMetalContext:sharedResources:].cold.2
+ -[PTPersonSemanticsNetwork initWithMetalContext:sharedResources:].cold.3
+ -[PTPersonSemanticsNetwork initWithMetalContext:sharedResources:].cold.4
+ -[PTPersonSemanticsNetwork initWithMetalContext:sharedResources:].cold.5
+ -[PTPersonSemanticsNetwork initWithMetalContext:sharedResources:].cold.6
+ -[PTPersonSemanticsNetwork initWithMetalContext:sharedResources:].cold.7
+ -[PTPersonSemanticsNetwork initWithMetalContext:sharedResources:].cold.8
+ -[PTPixelBufferSize height]
+ -[PTPixelBufferSize initWithWidth:height:]
+ -[PTPixelBufferSize setHeight:]
+ -[PTPixelBufferSize setWidth:]
+ -[PTPixelBufferSize width]
+ -[PTPyramid updatePyramid:inPTTexture:]
+ -[PTPyramid updatePyramid:inPTTexture:].cold.1
+ -[PTRaytracingUtils disparityApplyPostModifier:inDisparity:outDisparity:postModifier:]
+ -[PTRaytracingUtils disparityApplyPostModifier:inDisparity:outDisparity:postModifier:].cold.1
+ -[PTRaytracingUtils disparityMinMaxApplyPostModifier:disparityMinMaxBuffer:postModifier:]
+ -[PTRaytracingUtils disparityMinMaxApplyPostModifier:disparityMinMaxBuffer:postModifier:].cold.1
+ -[PTRaytracingUtils disparityPortraitPreviewDeadzone:inDisparity:outDisparity:postModifier:]
+ -[PTRaytracingUtils disparityPortraitPreviewDeadzone:inDisparity:outDisparity:postModifier:].cold.1
+ -[PTRaytracingV14 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:]
+ -[PTRaytracingV14 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.1
+ -[PTRaytracingV14 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.2
+ -[PTRaytracingV14 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.3
+ -[PTRaytracingV14 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.4
+ -[PTRaytracingV14 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.5
+ -[PTRaytracingV2002 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:]
+ -[PTRaytracingV2002 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.1
+ -[PTRaytracingV2002 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.10
+ -[PTRaytracingV2002 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.11
+ -[PTRaytracingV2002 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.12
+ -[PTRaytracingV2002 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.13
+ -[PTRaytracingV2002 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.14
+ -[PTRaytracingV2002 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.15
+ -[PTRaytracingV2002 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.16
+ -[PTRaytracingV2002 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.17
+ -[PTRaytracingV2002 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.2
+ -[PTRaytracingV2002 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.3
+ -[PTRaytracingV2002 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.4
+ -[PTRaytracingV2002 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.5
+ -[PTRaytracingV2002 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.6
+ -[PTRaytracingV2002 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.7
+ -[PTRaytracingV2002 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.8
+ -[PTRaytracingV2002 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.9
+ -[PTRaytracingV3001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:]
+ -[PTRaytracingV3001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.1
+ -[PTRaytracingV3001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.10
+ -[PTRaytracingV3001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.11
+ -[PTRaytracingV3001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.12
+ -[PTRaytracingV3001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.13
+ -[PTRaytracingV3001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.14
+ -[PTRaytracingV3001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.15
+ -[PTRaytracingV3001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.16
+ -[PTRaytracingV3001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.17
+ -[PTRaytracingV3001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.18
+ -[PTRaytracingV3001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.19
+ -[PTRaytracingV3001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.2
+ -[PTRaytracingV3001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.20
+ -[PTRaytracingV3001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.3
+ -[PTRaytracingV3001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.4
+ -[PTRaytracingV3001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.5
+ -[PTRaytracingV3001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.6
+ -[PTRaytracingV3001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.7
+ -[PTRaytracingV3001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.8
+ -[PTRaytracingV3001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.9
+ -[PTRaytracingV4001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:]
+ -[PTRaytracingV4001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.1
+ -[PTRaytracingV4001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.10
+ -[PTRaytracingV4001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.11
+ -[PTRaytracingV4001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.12
+ -[PTRaytracingV4001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.13
+ -[PTRaytracingV4001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.14
+ -[PTRaytracingV4001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.15
+ -[PTRaytracingV4001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.16
+ -[PTRaytracingV4001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.17
+ -[PTRaytracingV4001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.2
+ -[PTRaytracingV4001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.3
+ -[PTRaytracingV4001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.4
+ -[PTRaytracingV4001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.5
+ -[PTRaytracingV4001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.6
+ -[PTRaytracingV4001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.7
+ -[PTRaytracingV4001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.8
+ -[PTRaytracingV4001 initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.9
+ -[PTRenderDebugLayer initWithMetalContext:]
+ -[PTRenderDebugLayer renderDebugLayer:renderRequest:inDisparityDiff:focusObject:quality:edgeTolerance:debugTextures:debugRendering:]
+ -[PTRenderDebugLayer renderTurboMix:inTex:inRGBA:outRGBA:valueOffset:valueMinMax:valueAbs:colorRangeMax:channelMultiplier:mixWithRGBFraction:region:]
+ -[PTSRLv2Plist readPlist:]
+ -[PTSingleColorCubeCorrectionStage .cxx_destruct]
+ -[PTSingleColorCubeCorrectionStage cubeTexture]
+ -[PTSingleColorCubeCorrectionStage init:cubeSize:data:]
+ -[PTSingleColorCubeCorrectionStage init:cubeSize:data:].cold.1
+ -[PTSingleColorCubeCorrectionStage load3DTextureFromData:cubeSize:metal:outTexture:]
+ -[PTSingleColorCubeCorrectionStage load3DTextureFromData:cubeSize:metal:outTexture:].cold.1
+ -[PTStudioLightColorCorrectionAndConversion .cxx_destruct]
+ -[PTStudioLightColorCorrectionAndConversion cubeTexture]
+ -[PTStudioLightColorCorrectionAndConversion initWithMetalContext:correctionColorCube:]
+ -[PTStudioLightColorCorrectionAndConversion initWithMetalContext:correctionColorCube:].cold.1
+ -[PTStudioLightColorCorrectionAndConversion initWithMetalContext:correctionColorCube:].cold.2
+ -[PTStudioLightColorCorrectionAndConversion initWithMetalContext:correctionColorCube:].cold.3
+ -[PTStudioLightColorCorrectionAndConversion initializeCubeMap:inputTexture:]
+ -[PTStudioLightColorCorrectionAndConversion rgbMinMax]
+ -[PTSyntheticLight estimateLightIntensityWithFaceRects:inColor:numberOfFaceRects:transform:humanDetections:asyncWork:]
+ -[PTSyntheticLight estimateLightIntensityWithFaceRects:inColor:numberOfFaceRects:transform:humanDetections:asyncWork:].cold.1
+ -[PTSyntheticLight initWithMetalContext:msrColorPyramid:colorSize:prewarmOnly:sharedResources:]
+ -[PTSyntheticLight initWithMetalContext:msrColorPyramid:colorSize:prewarmOnly:sharedResources:].cold.1
+ -[PTSyntheticLight initWithMetalContext:msrColorPyramid:colorSize:prewarmOnly:sharedResources:].cold.2
+ -[PTSyntheticLight initWithMetalContext:msrColorPyramid:colorSize:prewarmOnly:sharedResources:].cold.3
+ -[PTSyntheticLight initWithMetalContext:msrColorPyramid:colorSize:prewarmOnly:sharedResources:].cold.4
+ -[PTSyntheticLight initWithMetalContext:msrColorPyramid:colorSize:prewarmOnly:sharedResources:].cold.5
+ -[PTSyntheticLight initWithMetalContext:msrColorPyramid:colorSize:prewarmOnly:sharedResources:].cold.6
+ -[PTSyntheticLight initWithMetalContext:msrColorPyramid:colorSize:prewarmOnly:sharedResources:].cold.7
+ -[PTSyntheticLight initWithMetalContext:msrColorPyramid:colorSize:prewarmOnly:sharedResources:].cold.8
+ -[PTSyntheticLight initWithMetalContext:msrColorPyramid:colorSize:prewarmOnly:sharedResources:].cold.9
+ -[PTTexture imageBlockSize]
+ -[PTTexture imageBlockSize].cold.1
+ -[PTTexture(PTTextureAdditions) asRGBAFromYUV]
+ -[PTTexture(PTTextureAdditions) asRGBA]
+ -[PTTexture(PTTextureAdditions) asYUV]
+ -[PTTextureRGBA asRGBA]
+ -[PTTextureRGBA imageBlockSize]
+ -[PTTextureRGBA initWithTexture:]
+ -[PTTextureRGBAFromYUV .cxx_destruct]
+ -[PTTextureRGBAFromYUV asRGBAFromYUV]
+ -[PTTextureRGBAFromYUV asRGBA]
+ -[PTTextureRGBAFromYUV asYUV]
+ -[PTTextureRGBAFromYUV initWithTexture:]
+ -[PTTextureRGBAFromYUV setTextureAsYUV:]
+ -[PTTextureRGBAFromYUV textureAsYUV]
+ -[PTTextureYUV asYUV]
+ -[PTTextureYUV imageBlockSize]
+ -[PTTextureYUV initWithLumaTexture:chromaTexture:]
+ -[PTVFXRenderEffect finalColorDescriptor]
+ -[PTVFXRenderEffect initVFX:sharedResources:asyncInitQueue:]
+ -[PTVFXRenderEffect initWithMetalContext:colorSize:colorConversion:prewarmOnly:humanDetections:sharedResources:asyncInitQueue:]
+ -[PTVFXRenderEffect initWithMetalContext:colorSize:colorConversion:prewarmOnly:humanDetections:sharedResources:asyncInitQueue:].cold.1
+ -[PTVFXRenderEffect initWithMetalContext:colorSize:colorConversion:prewarmOnly:humanDetections:sharedResources:asyncInitQueue:].cold.2
+ -[PTVFXRenderEffect loadActionForAttachment:]
+ -[PTVFXRenderEffect textureForAttachment:withDescriptor:]
+ -[PTVFXRenderEffectBinding alphaTexture]
+ -[PTVFXRenderEffectBinding rootAssetNode]
+ -[PTVFXRenderEffectBinding rootNode]
+ -[PTVFXRenderEffectBinding setAlphaTexture:]
+ -[PTVFXRenderEffectBinding setRootAssetNode:]
+ -[PTVFXRenderEffectBinding setRootNode:]
+ -[PTVFXResources .cxx_destruct]
+ -[PTVFXResources asyncVFXInit:metalContext:]
+ -[PTVFXResources camera]
+ -[PTVFXResources lightBinding]
+ -[PTVFXResources reactionTemplates]
+ -[PTVFXResources setCamera:]
+ -[PTVFXResources setLightBinding:]
+ -[PTVFXResources setReactionTemplates:]
+ -[PTVFXResources setVfxRenderer:]
+ -[PTVFXResources setWorld:]
+ -[PTVFXResources vfxRenderer]
+ -[PTVFXResources world]
+ -[PTVFXResourcesLogger .cxx_destruct]
+ -[PTVFXResourcesLogger initWithName:index:]
+ -[PTVFXResourcesLogger initWithName:index:].cold.1
+ -[PTVFXResourcesLogger progressHandler]
+ GCC_except_table11
+ GCC_except_table13
+ GCC_except_table29
+ GCC_except_table32
+ GCC_except_table39
+ GCC_except_table41
+ GCC_except_table42
+ GCC_except_table44
+ GCC_except_table46
+ GCC_except_table48
+ GCC_except_table49
+ GCC_except_table50
+ GCC_except_table51
+ GCC_except_table52
+ GCC_except_table53
+ GCC_except_table67
+ GCC_except_table8
+ OBJC_IVAR_$_PTSRLv2Plist.biasFactorSRLv2
+ OBJC_IVAR_$_PTSRLv2Plist.faceExpDifThreshold
+ OBJC_IVAR_$_PTSRLv2Plist.maskThreshold
+ OBJC_IVAR_$_PTSRLv2Plist.maxBoost_I
+ OBJC_IVAR_$_PTSRLv2Plist.maxBoost_II
+ OBJC_IVAR_$_PTSRLv2Plist.maxBoost_III
+ OBJC_IVAR_$_PTSRLv2Plist.maxBoost_IV
+ OBJC_IVAR_$_PTSRLv2Plist.maxBoost_V
+ OBJC_IVAR_$_PTSRLv2Plist.maxBoost_VI
+ OBJC_IVAR_$_PTSRLv2Plist.maxCurveBoost
+ OBJC_IVAR_$_PTSRLv2Plist.maxTargetRatioDarkening
+ OBJC_IVAR_$_PTSRLv2Plist.maxTargetRatioLimit
+ OBJC_IVAR_$_PTSRLv2Plist.minCurveBoost
+ OBJC_IVAR_$_PTSRLv2Plist.minFaceSize
+ OBJC_IVAR_$_PTSRLv2Plist.relightOnlyPersonMask
+ OBJC_IVAR_$_PTSRLv2Plist.targetMedian_I
+ OBJC_IVAR_$_PTSRLv2Plist.targetMedian_II
+ OBJC_IVAR_$_PTSRLv2Plist.targetMedian_III
+ OBJC_IVAR_$_PTSRLv2Plist.targetMedian_IV
+ OBJC_IVAR_$_PTSRLv2Plist.targetMedian_V
+ OBJC_IVAR_$_PTSRLv2Plist.targetMedian_VI
+ OBJC_IVAR_$_PTSRLv2Plist.toneSimilaritySigma
+ _CVIsCompressedPixelFormatAvailable
+ _CVPixelBufferPoolCreate
+ _CVPixelBufferPoolCreatePixelBuffer
+ _CVPixelBufferPoolRelease
+ _MTLPixelFormatGetInfoForDevice
+ _OBJC_CLASS_$_FigM2MController
+ _OBJC_CLASS_$_FigMetalContext
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_PTEffectComposition
+ _OBJC_CLASS_$_PTEffectCompositionConfig
+ _OBJC_CLASS_$_PTEffectCompositionRenderRequest
+ _OBJC_CLASS_$_PTEffectPersonSegmentationViSegHQVisionCoreE5
+ _OBJC_CLASS_$_PTLKTFlow
+ _OBJC_CLASS_$_PTPixelBufferSize
+ _OBJC_CLASS_$_PTSRLv2Plist
+ _OBJC_CLASS_$_PTSingleColorCubeCorrectionStage
+ _OBJC_CLASS_$_PTStudioLightColorCorrectionAndConversion
+ _OBJC_CLASS_$_PTTextureRGBAFromYUV
+ _OBJC_CLASS_$_PTVFXResources
+ _OBJC_CLASS_$_PTVFXResourcesLogger
+ _OBJC_CLASS_$_VFXAssetNode
+ _OBJC_CLASS_$_VFXClientTextureAsset
+ _OBJC_CLASS_$_VFXNode
+ _OBJC_CLASS_$_VFXRenderOptions
+ _OBJC_CLASS_$_VFXTextureAttachmentDescriptor
+ _OBJC_CLASS_$_VFXTransaction
+ _OBJC_CLASS_$_VFXWorld
+ _OBJC_CLASS_$_VisionCoreVideoSegmentationE5NetworkDescriptor
+ _OBJC_IVAR_$_PTCVMNetwork._depthPrioritization
+ _OBJC_IVAR_$_PTEffect._reset
+ _OBJC_IVAR_$_PTEffectComposition._composite
+ _OBJC_IVAR_$_PTEffectComposition._metalContext
+ _OBJC_IVAR_$_PTEffectComposition._sourceMipmap
+ _OBJC_IVAR_$_PTEffectComposition.metalTextureCache
+ _OBJC_IVAR_$_PTEffectCompositionConfig._device
+ _OBJC_IVAR_$_PTEffectCompositionRenderRequest._inputCropRect
+ _OBJC_IVAR_$_PTEffectCompositionRenderRequest._inputSourcePixelBuffer
+ _OBJC_IVAR_$_PTEffectCompositionRenderRequest._inputTargetPixelBuffer
+ _OBJC_IVAR_$_PTEffectCompositionRenderRequest._inputTargetRect
+ _OBJC_IVAR_$_PTEffectCompositionRenderRequest._inputTargetRectCornerRadius
+ _OBJC_IVAR_$_PTEffectCompositionRenderRequest._outputPixelBuffer
+ _OBJC_IVAR_$_PTEffectDebugLayer._effectDescritor
+ _OBJC_IVAR_$_PTEffectPersonSegmentationViSegHQVisionCore._colorSize
+ _OBJC_IVAR_$_PTEffectPersonSegmentationViSegHQVisionCoreE5._asyncDispatchQueue
+ _OBJC_IVAR_$_PTEffectPersonSegmentationViSegHQVisionCoreE5._boundInputIOSurface
+ _OBJC_IVAR_$_PTEffectPersonSegmentationViSegHQVisionCoreE5._colorSize
+ _OBJC_IVAR_$_PTEffectPersonSegmentationViSegHQVisionCoreE5._e5Functions
+ _OBJC_IVAR_$_PTEffectPersonSegmentationViSegHQVisionCoreE5._e5SurfaceMatting
+ _OBJC_IVAR_$_PTEffectPersonSegmentationViSegHQVisionCoreE5._ebuffer
+ _OBJC_IVAR_$_PTEffectPersonSegmentationViSegHQVisionCoreE5._es
+ _OBJC_IVAR_$_PTEffectPersonSegmentationViSegHQVisionCoreE5._esop
+ _OBJC_IVAR_$_PTEffectPersonSegmentationViSegHQVisionCoreE5._frameCount
+ _OBJC_IVAR_$_PTEffectPersonSegmentationViSegHQVisionCoreE5._inputE5Surface
+ _OBJC_IVAR_$_PTEffectPersonSegmentationViSegHQVisionCoreE5._metalContext
+ _OBJC_IVAR_$_PTEffectPersonSegmentationViSegHQVisionCoreE5._networkPorts
+ _OBJC_IVAR_$_PTEffectPersonSegmentationViSegHQVisionCoreE5._pixelBufferMatting
+ _OBJC_IVAR_$_PTEffectPersonSegmentationViSegHQVisionCoreE5._semaphore
+ _OBJC_IVAR_$_PTEffectPersonSegmentationViSegHQVisionCoreE5._textureMatting
+ _OBJC_IVAR_$_PTEffectPersonSegmentationViSegHQVisionCoreE5._viSegHQDescriptor
+ _OBJC_IVAR_$_PTEffectRelighting._colorCorrectionAndConversion
+ _OBJC_IVAR_$_PTEffectRenderRequest._alsColor
+ _OBJC_IVAR_$_PTEffectRenderRequest._alsLuxLevel
+ _OBJC_IVAR_$_PTEffectRenderRequest._ambientLightSensor
+ _OBJC_IVAR_$_PTEffectRenderRequest._metadataDictionary
+ _OBJC_IVAR_$_PTEffectRenderer._colorPyramid
+ _OBJC_IVAR_$_PTEffectRenderer._intermediateColor
+ _OBJC_IVAR_$_PTEffectRenderer._intermediateColorPixelbuffers
+ _OBJC_IVAR_$_PTEffectResources._effectUtil
+ _OBJC_IVAR_$_PTEffectResources._faceAttributesNetwork
+ _OBJC_IVAR_$_PTEffectResources._util
+ _OBJC_IVAR_$_PTEffectResources._vfxResources
+ _OBJC_IVAR_$_PTHandGestureDetector._msrResize
+ _OBJC_IVAR_$_PTHandGestureDetector._pixelBufferPool
+ _OBJC_IVAR_$_PTLKTFlow._Adiagb_buf
+ _OBJC_IVAR_$_PTLKTFlow._C0_tex
+ _OBJC_IVAR_$_PTLKTFlow._C1_tex
+ _OBJC_IVAR_$_PTLKTFlow._G0_tex
+ _OBJC_IVAR_$_PTLKTFlow._G1_tex
+ _OBJC_IVAR_$_PTLKTFlow._I_tex
+ _OBJC_IVAR_$_PTLKTFlow._I_u32_alias_tex
+ _OBJC_IVAR_$_PTLKTFlow._Ixy_buf
+ _OBJC_IVAR_$_PTLKTFlow._aux_pyr_size
+ _OBJC_IVAR_$_PTLKTFlow._aux_size
+ _OBJC_IVAR_$_PTLKTFlow._computePipelines
+ _OBJC_IVAR_$_PTLKTFlow._current_frame_index
+ _OBJC_IVAR_$_PTLKTFlow._idt_buf
+ _OBJC_IVAR_$_PTLKTFlow._indexUpdated
+ _OBJC_IVAR_$_PTLKTFlow._isBidirectional
+ _OBJC_IVAR_$_PTLKTFlow._isInverse
+ _OBJC_IVAR_$_PTLKTFlow._isValid
+ _OBJC_IVAR_$_PTLKTFlow._kpt_buf
+ _OBJC_IVAR_$_PTLKTFlow._maxThreadExecutionWidth
+ _OBJC_IVAR_$_PTLKTFlow._needConversionBGRA2YUVA
+ _OBJC_IVAR_$_PTLKTFlow._nlreg_padding
+ _OBJC_IVAR_$_PTLKTFlow._nlreg_radius
+ _OBJC_IVAR_$_PTLKTFlow._nlreg_sigma_c
+ _OBJC_IVAR_$_PTLKTFlow._nlreg_sigma_l
+ _OBJC_IVAR_$_PTLKTFlow._nlreg_sigma_w
+ _OBJC_IVAR_$_PTLKTFlow._nscales
+ _OBJC_IVAR_$_PTLKTFlow._nwarpings
+ _OBJC_IVAR_$_PTLKTFlow._ref_pyr_size
+ _OBJC_IVAR_$_PTLKTFlow._ref_size
+ _OBJC_IVAR_$_PTLKTFlow._streamFrameCount
+ _OBJC_IVAR_$_PTLKTFlow._useNonLocalRegularization
+ _OBJC_IVAR_$_PTLKTFlow._uv_bwd_tex
+ _OBJC_IVAR_$_PTLKTFlow._uv_bwd_tex_user_ref
+ _OBJC_IVAR_$_PTLKTFlow._uv_bwd_u32_alias_tex
+ _OBJC_IVAR_$_PTLKTFlow._uv_fwd_tex
+ _OBJC_IVAR_$_PTLKTFlow._uv_fwd_tex_user_ref
+ _OBJC_IVAR_$_PTLKTFlow._uv_fwd_u32_alias_tex
+ _OBJC_IVAR_$_PTLKTFlow._w_tex
+ _OBJC_IVAR_$_PTMSRResize._msrController
+ _OBJC_IVAR_$_PTMSRResizeAdditionalOutput._allowCompressed
+ _OBJC_IVAR_$_PTMetalContext._figMetalContext
+ _OBJC_IVAR_$_PTMetalTextureUtil._supportGPUFamilyApple7
+ _OBJC_IVAR_$_PTPixelBufferSize._height
+ _OBJC_IVAR_$_PTPixelBufferSize._width
+ _OBJC_IVAR_$_PTPyramid._updateLevel0FromRGBA
+ _OBJC_IVAR_$_PTPyramid._updateLevel0FromYUV
+ _OBJC_IVAR_$_PTPyramid._updateLevel0and1FromRGBA
+ _OBJC_IVAR_$_PTPyramid._updateLevel0and1FromYUV
+ _OBJC_IVAR_$_PTRaytracingV2002._disparityDiffUpscaled
+ _OBJC_IVAR_$_PTRaytracingV3001._disparityDiffUpscaled
+ _OBJC_IVAR_$_PTRaytracingV3001._radialObstructionFactor
+ _OBJC_IVAR_$_PTRaytracingV4001._radialObstructionFactor
+ _OBJC_IVAR_$_PTSingleColorCubeCorrectionStage._defaultCubeTexture
+ _OBJC_IVAR_$_PTStudioLightColorCorrectionAndConversion._correctionColorCube
+ _OBJC_IVAR_$_PTStudioLightColorCorrectionAndConversion._cubeTexture
+ _OBJC_IVAR_$_PTStudioLightColorCorrectionAndConversion._rgbMinMax
+ _OBJC_IVAR_$_PTStudioLightColorCorrectionAndConversion._studioLightColorCorrectionRGBToYUV
+ _OBJC_IVAR_$_PTTextureRGBA._imageblockSize
+ _OBJC_IVAR_$_PTTextureRGBAFromYUV._textureAsYUV
+ _OBJC_IVAR_$_PTTextureYUV._imageblockSize
+ _OBJC_IVAR_$_PTVFXRenderEffect._colorAttachmentDescriptor
+ _OBJC_IVAR_$_PTVFXRenderEffect._colorTexture
+ _OBJC_IVAR_$_PTVFXRenderEffect._depthTexture
+ _OBJC_IVAR_$_PTVFXRenderEffect._vfxResources
+ _OBJC_IVAR_$_PTVFXRenderEffectBinding._alphaTexture
+ _OBJC_IVAR_$_PTVFXRenderEffectBinding._rootAssetNode
+ _OBJC_IVAR_$_PTVFXRenderEffectBinding._rootNode
+ _OBJC_IVAR_$_PTVFXResources._camera
+ _OBJC_IVAR_$_PTVFXResources._lightBinding
+ _OBJC_IVAR_$_PTVFXResources._reactionTemplates
+ _OBJC_IVAR_$_PTVFXResources._vfxRenderer
+ _OBJC_IVAR_$_PTVFXResources._world
+ _OBJC_IVAR_$_PTVFXResourcesLogger._index
+ _OBJC_IVAR_$_PTVFXResourcesLogger._name
+ _OBJC_IVAR_$_PTVFXResourcesLogger._verboseLogging
+ _OBJC_METACLASS_$_PTEffectComposition
+ _OBJC_METACLASS_$_PTEffectCompositionConfig
+ _OBJC_METACLASS_$_PTEffectCompositionRenderRequest
+ _OBJC_METACLASS_$_PTEffectPersonSegmentationViSegHQVisionCoreE5
+ _OBJC_METACLASS_$_PTLKTFlow
+ _OBJC_METACLASS_$_PTPixelBufferSize
+ _OBJC_METACLASS_$_PTSRLv2Plist
+ _OBJC_METACLASS_$_PTSingleColorCubeCorrectionStage
+ _OBJC_METACLASS_$_PTStudioLightColorCorrectionAndConversion
+ _OBJC_METACLASS_$_PTTextureRGBAFromYUV
+ _OBJC_METACLASS_$_PTVFXResources
+ _OBJC_METACLASS_$_PTVFXResourcesLogger
+ _VFXRenderGraphFinalColorAttachment
+ _VFXRenderGraphMainDepthAttachment
+ _VFXWorldLoaderOptionMetalLibraryURL
+ _VisionCoreVideoSegmentationE5InferenceNetworkIdentifier
+ __OBJC_$_CLASS_METHODS_PTEffectPersonSegmentationViSegHQVisionCoreE5
+ __OBJC_$_CLASS_METHODS_PTLKTFlow
+ __OBJC_$_CLASS_METHODS_PTMetalTextureUtil
+ __OBJC_$_INSTANCE_METHODS_PTEffectComposition
+ __OBJC_$_INSTANCE_METHODS_PTEffectCompositionConfig
+ __OBJC_$_INSTANCE_METHODS_PTEffectCompositionRenderRequest
+ __OBJC_$_INSTANCE_METHODS_PTEffectPersonSegmentationViSegHQVisionCoreE5
+ __OBJC_$_INSTANCE_METHODS_PTLKTFlow
+ __OBJC_$_INSTANCE_METHODS_PTPixelBufferSize
+ __OBJC_$_INSTANCE_METHODS_PTSRLv2Plist
+ __OBJC_$_INSTANCE_METHODS_PTSingleColorCubeCorrectionStage
+ __OBJC_$_INSTANCE_METHODS_PTStudioLightColorCorrectionAndConversion
+ __OBJC_$_INSTANCE_METHODS_PTTextureRGBAFromYUV
+ __OBJC_$_INSTANCE_METHODS_PTVFXResources
+ __OBJC_$_INSTANCE_METHODS_PTVFXResourcesLogger
+ __OBJC_$_INSTANCE_VARIABLES_PTEffectComposition
+ __OBJC_$_INSTANCE_VARIABLES_PTEffectCompositionConfig
+ __OBJC_$_INSTANCE_VARIABLES_PTEffectCompositionRenderRequest
+ __OBJC_$_INSTANCE_VARIABLES_PTEffectPersonSegmentationViSegHQVisionCoreE5
+ __OBJC_$_INSTANCE_VARIABLES_PTLKTFlow
+ __OBJC_$_INSTANCE_VARIABLES_PTPixelBufferSize
+ __OBJC_$_INSTANCE_VARIABLES_PTSRLv2Plist
+ __OBJC_$_INSTANCE_VARIABLES_PTSingleColorCubeCorrectionStage
+ __OBJC_$_INSTANCE_VARIABLES_PTStudioLightColorCorrectionAndConversion
+ __OBJC_$_INSTANCE_VARIABLES_PTTextureRGBAFromYUV
+ __OBJC_$_INSTANCE_VARIABLES_PTVFXResources
+ __OBJC_$_INSTANCE_VARIABLES_PTVFXResourcesLogger
+ __OBJC_$_PROP_LIST_PTEffectCompositionConfig
+ __OBJC_$_PROP_LIST_PTEffectCompositionRenderRequest
+ __OBJC_$_PROP_LIST_PTEffectPersonSegmentationViSegHQVisionCoreE5
+ __OBJC_$_PROP_LIST_PTLKTFlow
+ __OBJC_$_PROP_LIST_PTPixelBufferSize
+ __OBJC_$_PROP_LIST_PTTextureRGBAFromYUV
+ __OBJC_$_PROP_LIST_PTVFXResources
+ __OBJC_$_PROP_LIST_VFXTextureAttachmentProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_VFXTextureAttachmentProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_VFXTextureAttachmentProvider
+ __OBJC_$_PROTOCOL_REFS_VFXTextureAttachmentProvider
+ __OBJC_CLASS_PROTOCOLS_$_PTEffectPersonSegmentationViSegHQVisionCoreE5
+ __OBJC_CLASS_PROTOCOLS_$_PTVFXRenderEffect
+ __OBJC_CLASS_RO_$_PTEffectComposition
+ __OBJC_CLASS_RO_$_PTEffectCompositionConfig
+ __OBJC_CLASS_RO_$_PTEffectCompositionRenderRequest
+ __OBJC_CLASS_RO_$_PTEffectPersonSegmentationViSegHQVisionCoreE5
+ __OBJC_CLASS_RO_$_PTLKTFlow
+ __OBJC_CLASS_RO_$_PTPixelBufferSize
+ __OBJC_CLASS_RO_$_PTSRLv2Plist
+ __OBJC_CLASS_RO_$_PTSingleColorCubeCorrectionStage
+ __OBJC_CLASS_RO_$_PTStudioLightColorCorrectionAndConversion
+ __OBJC_CLASS_RO_$_PTTextureRGBAFromYUV
+ __OBJC_CLASS_RO_$_PTVFXResources
+ __OBJC_CLASS_RO_$_PTVFXResourcesLogger
+ __OBJC_LABEL_PROTOCOL_$_VFXTextureAttachmentProvider
+ __OBJC_METACLASS_RO_$_PTEffectComposition
+ __OBJC_METACLASS_RO_$_PTEffectCompositionConfig
+ __OBJC_METACLASS_RO_$_PTEffectCompositionRenderRequest
+ __OBJC_METACLASS_RO_$_PTEffectPersonSegmentationViSegHQVisionCoreE5
+ __OBJC_METACLASS_RO_$_PTLKTFlow
+ __OBJC_METACLASS_RO_$_PTPixelBufferSize
+ __OBJC_METACLASS_RO_$_PTSRLv2Plist
+ __OBJC_METACLASS_RO_$_PTSingleColorCubeCorrectionStage
+ __OBJC_METACLASS_RO_$_PTStudioLightColorCorrectionAndConversion
+ __OBJC_METACLASS_RO_$_PTTextureRGBAFromYUV
+ __OBJC_METACLASS_RO_$_PTVFXResources
+ __OBJC_METACLASS_RO_$_PTVFXResourcesLogger
+ __OBJC_PROTOCOL_$_VFXTextureAttachmentProvider
+ __Z39particle_update_hearts_particleUpdate_6PKvRDv3_fRjRfS4_S0_
+ __Z39particle_update_lasers_particleUpdate_4PvRDv4_fS_
+ __Z44particle_update_fireworks_particleUpdate_268PKvRfRDv4_fS0_
+ __Z44particle_update_fireworks_particleUpdate_292PKvRfRDv4_fS3_S0_
+ __ZL13sSRLAsyncLock
+ __ZL17_vfx_objc_sel_uv0
+ __ZL18__vfx_script_table
+ __ZL18_vfx_objc_sel_node
+ __ZL19_vfx_objc_sel_begin
+ __ZL19_vfx_objc_sel_clone
+ __ZL19_vfx_objc_sel_count
+ __ZL20_vfx_objc_sel_commit
+ __ZL20yellowSatFixCubeData
+ __ZL21_vfx_objc_cls_NSValue
+ __ZL21_vfx_objc_cls_VFXNode
+ __ZL22__vfx_script_table_ref
+ __ZL22_vfx_objc_cls_NSNumber
+ __ZL22_vfx_objc_cls_NSString
+ __ZL22_vfx_objc_sel_boneNode
+ __ZL23_vfx_objc_sel_deepClone
+ __ZL23_vfx_objc_sel_faceIndex
+ __ZL23_vfx_objc_sel_setState_
+ __ZL24_vfx_objc_sel_childNodes
+ __ZL24_vfx_objc_sel_dictionary
+ __ZL24_vfx_objc_sel_parentNode
+ __ZL25_vfx_objc_sel__screenSize
+ __ZL25_vfx_objc_sel_firstObject
+ __ZL25_vfx_objc_sel_localNormal
+ __ZL25_vfx_objc_sel_physicsBody
+ __ZL25_vfx_objc_sel_worldNormal
+ __ZL25sPTEffectDisableAsyncWork
+ __ZL26_vfx_objc_cls_NSDictionary
+ __ZL27_vfx_objc_sel_addChildNode_
+ __ZL27_vfx_objc_sel_geometryIndex
+ __ZL27_vfx_objc_sel_projectPoint_
+ __ZL28_vfx_objc_cls_VFXTransaction
+ __ZL28_vfx_objc_sel_localRotateBy_
+ __ZL28_vfx_objc_sel_modelTransform
+ __ZL28_vfx_objc_sel_setStateNamed_
+ __ZL29_vfx_objc_sel_numberWithBool_
+ __ZL29_vfx_objc_sel_script_rootNode
+ __ZL29_vfx_objc_sel_unprojectPoint_
+ __ZL30_vfx_objc_sel_insertChildNode_
+ __ZL30_vfx_objc_sel_localCoordinates
+ __ZL30_vfx_objc_sel_numberWithFloat_
+ __ZL30_vfx_objc_sel_presentationNode
+ __ZL30_vfx_objc_sel_setValue_forKey_
+ __ZL30_vfx_objc_sel_valueForKeyPath_
+ __ZL30_vfx_objc_sel_worldCoordinates
+ __ZL31_vfx_objc_sel_localTranslateBy_
+ __ZL31_vfx_objc_sel_setObject_forKey_
+ __ZL31sForceSynchronousInitialization
+ __ZL32_vfx_objc_sel_childNodeWithName_
+ __ZL32_vfx_objc_sel_presentationObject
+ __ZL33_vfx_objc_cls_NSMutableDictionary
+ __ZL33_vfx_objc_sel_applyForce_impulse_
+ __ZL33_vfx_objc_sel_removeAllAnimations
+ __ZL33_vfx_objc_sel_script_instantiate_
+ __ZL34_vfx_objc_sel__contentsScaleFactor
+ __ZL34_vfx_objc_sel_addAnimation_forKey_
+ __ZL34_vfx_objc_sel_applyTorque_impulse_
+ __ZL34_vfx_objc_sel_presentationBoneNode
+ __ZL34_vfx_objc_sel_removeFromParentNode
+ __ZL34_vfx_objc_sel_setValue_forKeyPath_
+ __ZL35_vfx_objc_sel_convertVector_toNode_
+ __ZL35_vfx_objc_sel_stringWithUTF8String_
+ __ZL36_vfx_objc_sel_removeAnimationForKey_
+ __ZL36_vfx_objc_sel_rotateBy_aroundTarget_
+ __ZL37_vfx_objc_sel_convertPosition_toNode_
+ __ZL37_vfx_objc_sel_convertVector_fromNode_
+ __ZL37_vfx_objc_sel_script_hitTest_options_
+ __ZL38_vfx_objc_sel_convertTransform_toNode_
+ __ZL38_vfx_objc_sel_insertChildNode_atIndex_
+ __ZL39_vfx_objc_sel_addAnimationAsset_forKey_
+ __ZL39_vfx_objc_sel_convertPosition_fromNode_
+ __ZL40_vfx_objc_sel_convertTransform_fromNode_
+ __ZL40_vfx_objc_sel_numberWithUnsignedInteger_
+ __ZL42_vfx_objc_sel_setAnimationDurationAsFloat_
+ __ZL44_vfx_objc_sel_applyForce_atPosition_impulse_
+ __ZL53_vfx_objc_sel_removeAnimationForKey_blendOutDuration_
+ __ZL54_vfx_objc_sel_removeAllAnimationsWithBlendOutDuration_
+ __ZL58_vfx_objc_sel_hitTestWithSegmentFromPoint_toPoint_options_
+ __ZSt9terminatev
+ __ZZL34vfx_script_initialize_objc_helpersvE4once
+ ___118-[PTSyntheticLight estimateLightIntensityWithFaceRects:inColor:numberOfFaceRects:transform:humanDetections:asyncWork:]_block_invoke
+ ___126-[PTHandGestureDetector detectGesturesFromBuffer:timeStamp:withRotationDegrees:withDetectedHands:withDetectedFaces:asyncWork:]_block_invoke.140
+ ___137-[PTEffectRenderer initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:]_block_invoke
+ ___38-[PTEffect reconfigure:isInitialized:]_block_invoke
+ ___38-[PTEffect reconfigure:isInitialized:]_block_invoke_2
+ ___39-[PTVFXResourcesLogger progressHandler]_block_invoke
+ ___39-[PTVFXResourcesLogger progressHandler]_block_invoke.cold.1
+ ___44-[PTVFXResources asyncVFXInit:metalContext:]_block_invoke
+ ___44-[PTVFXResources asyncVFXInit:metalContext:]_block_invoke.89
+ ___44-[PTVFXResources asyncVFXInit:metalContext:]_block_invoke.cold.1
+ ___44-[PTVFXResources asyncVFXInit:metalContext:]_block_invoke.cold.2
+ ___44-[PTVFXResources asyncVFXInit:metalContext:]_block_invoke.cold.3
+ ___44-[PTVFXResources asyncVFXInit:metalContext:]_block_invoke.cold.4
+ ___49+[PTPixelBufferUtil supportsMetalYCBCRConversion]_block_invoke
+ ___59-[PTEffectRenderer render:waitUntilCompleted:gpuCompleted:]_block_invoke_2
+ ___85-[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:]_block_invoke
+ ___85-[PTEffectPersonSegmentationViSegHQVisionCoreE5 runPersonSegmentationForPixelBuffer:]_block_invoke.cold.1
+ ___88-[PTHandGestureDetector initWithFrameSize:asyncInitQueue:externalHandDetectionsEnabled:]_block_invoke.cold.1
+ ____ZL34vfx_script_initialize_objc_helpersv_block_invoke
+ ___block_descriptor_120_ea8_32s40s48r56w_e5_v8?0lw56l8s32l8r48l8s40l8
+ ___block_descriptor_40_e8_32s_e24_v28?0f8"NSError"12^B20ls32l8
+ ___block_descriptor_40_ea8_32s_e28_v16?0"<MTLCommandBuffer>"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e28_v16?0"<MTLCommandBuffer>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_52_ea8_32s40s_e28_v16?0"<MTLCommandBuffer>"8ls32l8s40l8
+ ___block_descriptor_56_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_64_e8_32s40s48s56w_e28_v16?0"<MTLCommandBuffer>"8lw56l8s32l8s40l8s48l8
+ ___block_descriptor_75_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_91_ea8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_tmp
+ ___block_literal_global.122
+ ___block_literal_global.141
+ ___clang_call_terminate
+ ___cxa_begin_catch
+ ___getVCPRequestCoreMLANEPriorityPropertyKeySymbolLoc_block_invoke
+ ___getVCPRequestEspressoPlanPriorityPropertyKeySymbolLoc_block_invoke
+ ___vfx_script_balloons_graph_159
+ ___vfx_script_balloons_graph_159.cold.1
+ ___vfx_script_balloons_graph_160
+ ___vfx_script_balloons_graph_160.cold.1
+ ___vfx_script_balloons_graph_163
+ ___vfx_script_balloons_graph_163.cold.1
+ ___vfx_script_balloons_graph_166
+ ___vfx_script_balloons_graph_166.cold.1
+ ___vfx_script_balloons_graph_169
+ ___vfx_script_balloons_graph_169.cold.1
+ ___vfx_script_balloons_graph_170
+ ___vfx_script_balloons_graph_170.cold.1
+ ___vfx_script_balloons_graph_171
+ ___vfx_script_balloons_graph_171.cold.1
+ ___vfx_script_balloons_graph_172
+ ___vfx_script_balloons_graph_172.cold.1
+ ___vfx_script_balloons_graph_173
+ ___vfx_script_balloons_graph_173.cold.1
+ ___vfx_script_balloons_graph_177
+ ___vfx_script_balloons_graph_177.cold.1
+ ___vfx_script_balloons_particleInit_161
+ ___vfx_script_balloons_particleInit_161.cold.1
+ ___vfx_script_balloons_particleInit_164
+ ___vfx_script_balloons_particleInit_164.cold.1
+ ___vfx_script_balloons_particleInit_167
+ ___vfx_script_balloons_particleInit_167.cold.1
+ ___vfx_script_balloons_particleInit_174
+ ___vfx_script_balloons_particleInit_174.cold.1
+ ___vfx_script_balloons_particleInit_175
+ ___vfx_script_balloons_particleInit_175.cold.1
+ ___vfx_script_balloons_particleUpdate_162
+ ___vfx_script_balloons_particleUpdate_162.cold.1
+ ___vfx_script_balloons_particleUpdate_165
+ ___vfx_script_balloons_particleUpdate_165.cold.1
+ ___vfx_script_balloons_particleUpdate_168
+ ___vfx_script_balloons_particleUpdate_168.cold.1
+ ___vfx_script_balloons_particleUpdate_176
+ ___vfx_script_balloons_particleUpdate_176.cold.1
+ ___vfx_script_confetti_graph_233
+ ___vfx_script_confetti_graph_233.cold.1
+ ___vfx_script_confetti_graph_236
+ ___vfx_script_confetti_graph_236.cold.1
+ ___vfx_script_confetti_graph_239
+ ___vfx_script_confetti_graph_239.cold.1
+ ___vfx_script_confetti_graph_242
+ ___vfx_script_confetti_graph_242.cold.1
+ ___vfx_script_confetti_graph_243
+ ___vfx_script_confetti_graph_243.cold.1
+ ___vfx_script_confetti_graph_246
+ ___vfx_script_confetti_graph_246.cold.1
+ ___vfx_script_confetti_graph_247
+ ___vfx_script_confetti_graph_247.cold.1
+ ___vfx_script_confetti_particleInit_234
+ ___vfx_script_confetti_particleInit_234.cold.1
+ ___vfx_script_confetti_particleInit_237
+ ___vfx_script_confetti_particleInit_237.cold.1
+ ___vfx_script_confetti_particleInit_240
+ ___vfx_script_confetti_particleInit_240.cold.1
+ ___vfx_script_confetti_particleInit_244
+ ___vfx_script_confetti_particleInit_244.cold.1
+ ___vfx_script_confetti_particleInit_248
+ ___vfx_script_confetti_particleInit_248.cold.1
+ ___vfx_script_confetti_particleUpdate_235
+ ___vfx_script_confetti_particleUpdate_235.cold.1
+ ___vfx_script_confetti_particleUpdate_238
+ ___vfx_script_confetti_particleUpdate_238.cold.1
+ ___vfx_script_confetti_particleUpdate_241
+ ___vfx_script_confetti_particleUpdate_241.cold.1
+ ___vfx_script_confetti_particleUpdate_245
+ ___vfx_script_confetti_particleUpdate_245.cold.1
+ ___vfx_script_fireworks_graph_353
+ ___vfx_script_fireworks_graph_353.cold.1
+ ___vfx_script_fireworks_graph_356
+ ___vfx_script_fireworks_graph_356.cold.1
+ ___vfx_script_fireworks_graph_357
+ ___vfx_script_fireworks_graph_357.cold.1
+ ___vfx_script_fireworks_graph_359
+ ___vfx_script_fireworks_graph_359.cold.1
+ ___vfx_script_fireworks_graph_361
+ ___vfx_script_fireworks_graph_361.cold.1
+ ___vfx_script_fireworks_graph_364
+ ___vfx_script_fireworks_graph_364.cold.1
+ ___vfx_script_fireworks_graph_367
+ ___vfx_script_fireworks_graph_367.cold.1
+ ___vfx_script_fireworks_graph_370
+ ___vfx_script_fireworks_graph_370.cold.1
+ ___vfx_script_fireworks_graph_373
+ ___vfx_script_fireworks_graph_373.cold.1
+ ___vfx_script_fireworks_graph_376
+ ___vfx_script_fireworks_graph_376.cold.1
+ ___vfx_script_fireworks_graph_379
+ ___vfx_script_fireworks_graph_379.cold.1
+ ___vfx_script_fireworks_graph_382
+ ___vfx_script_fireworks_graph_382.cold.1
+ ___vfx_script_fireworks_graph_385
+ ___vfx_script_fireworks_graph_385.cold.1
+ ___vfx_script_fireworks_graph_388
+ ___vfx_script_fireworks_graph_388.cold.1
+ ___vfx_script_fireworks_graph_391
+ ___vfx_script_fireworks_graph_391.cold.1
+ ___vfx_script_fireworks_graph_394
+ ___vfx_script_fireworks_graph_394.cold.1
+ ___vfx_script_fireworks_graph_395
+ ___vfx_script_fireworks_graph_395.cold.1
+ ___vfx_script_fireworks_graph_396
+ ___vfx_script_fireworks_graph_396.cold.1
+ ___vfx_script_fireworks_graph_397
+ ___vfx_script_fireworks_graph_397.cold.1
+ ___vfx_script_fireworks_graph_398
+ ___vfx_script_fireworks_graph_398.cold.1
+ ___vfx_script_fireworks_graph_399
+ ___vfx_script_fireworks_graph_399.cold.1
+ ___vfx_script_fireworks_graph_401
+ ___vfx_script_fireworks_graph_401.cold.1
+ ___vfx_script_fireworks_particleInit_351
+ ___vfx_script_fireworks_particleInit_351.cold.1
+ ___vfx_script_fireworks_particleInit_354
+ ___vfx_script_fireworks_particleInit_354.cold.1
+ ___vfx_script_fireworks_particleInit_358
+ ___vfx_script_fireworks_particleInit_358.cold.1
+ ___vfx_script_fireworks_particleInit_360
+ ___vfx_script_fireworks_particleInit_360.cold.1
+ ___vfx_script_fireworks_particleInit_362
+ ___vfx_script_fireworks_particleInit_362.cold.1
+ ___vfx_script_fireworks_particleInit_368
+ ___vfx_script_fireworks_particleInit_368.cold.1
+ ___vfx_script_fireworks_particleInit_371
+ ___vfx_script_fireworks_particleInit_371.cold.1
+ ___vfx_script_fireworks_particleInit_374
+ ___vfx_script_fireworks_particleInit_374.cold.1
+ ___vfx_script_fireworks_particleInit_380
+ ___vfx_script_fireworks_particleInit_380.cold.1
+ ___vfx_script_fireworks_particleInit_386
+ ___vfx_script_fireworks_particleInit_386.cold.1
+ ___vfx_script_fireworks_particleInit_392
+ ___vfx_script_fireworks_particleInit_392.cold.1
+ ___vfx_script_fireworks_particleInit_400
+ ___vfx_script_fireworks_particleInit_400.cold.1
+ ___vfx_script_fireworks_particleUpdate_268
+ ___vfx_script_fireworks_particleUpdate_268.cold.1
+ ___vfx_script_fireworks_particleUpdate_292
+ ___vfx_script_fireworks_particleUpdate_292.cold.1
+ ___vfx_script_fireworks_particleUpdate_352
+ ___vfx_script_fireworks_particleUpdate_352.cold.1
+ ___vfx_script_fireworks_particleUpdate_355
+ ___vfx_script_fireworks_particleUpdate_355.cold.1
+ ___vfx_script_fireworks_particleUpdate_363
+ ___vfx_script_fireworks_particleUpdate_363.cold.1
+ ___vfx_script_fireworks_particleUpdate_369
+ ___vfx_script_fireworks_particleUpdate_369.cold.1
+ ___vfx_script_fireworks_particleUpdate_372
+ ___vfx_script_fireworks_particleUpdate_372.cold.1
+ ___vfx_script_fireworks_particleUpdate_375
+ ___vfx_script_fireworks_particleUpdate_375.cold.1
+ ___vfx_script_fireworks_particleUpdate_381
+ ___vfx_script_fireworks_particleUpdate_381.cold.1
+ ___vfx_script_fireworks_particleUpdate_387
+ ___vfx_script_fireworks_particleUpdate_387.cold.1
+ ___vfx_script_fireworks_particleUpdate_393
+ ___vfx_script_fireworks_particleUpdate_393.cold.1
+ ___vfx_script_hearts_graph_222
+ ___vfx_script_hearts_graph_222.cold.1
+ ___vfx_script_hearts_graph_226
+ ___vfx_script_hearts_graph_226.cold.1
+ ___vfx_script_hearts_graph_227
+ ___vfx_script_hearts_graph_227.cold.1
+ ___vfx_script_hearts_graph_228
+ ___vfx_script_hearts_graph_228.cold.1
+ ___vfx_script_hearts_graph_231
+ ___vfx_script_hearts_graph_231.cold.1
+ ___vfx_script_hearts_graph_232
+ ___vfx_script_hearts_graph_232.cold.1
+ ___vfx_script_hearts_graph_233
+ ___vfx_script_hearts_graph_233.cold.1
+ ___vfx_script_hearts_graph_234
+ ___vfx_script_hearts_graph_234.cold.1
+ ___vfx_script_hearts_graph_235
+ ___vfx_script_hearts_graph_235.cold.1
+ ___vfx_script_hearts_particleInit_223
+ ___vfx_script_hearts_particleInit_223.cold.1
+ ___vfx_script_hearts_particleInit_224
+ ___vfx_script_hearts_particleInit_224.cold.1
+ ___vfx_script_hearts_particleInit_229
+ ___vfx_script_hearts_particleInit_229.cold.1
+ ___vfx_script_hearts_particleUpdate_225
+ ___vfx_script_hearts_particleUpdate_225.cold.1
+ ___vfx_script_hearts_particleUpdate_230
+ ___vfx_script_hearts_particleUpdate_230.cold.1
+ ___vfx_script_hearts_particleUpdate_6
+ ___vfx_script_hearts_particleUpdate_6.cold.1
+ ___vfx_script_lasers_graph_134
+ ___vfx_script_lasers_graph_134.cold.1
+ ___vfx_script_lasers_graph_135
+ ___vfx_script_lasers_graph_135.cold.1
+ ___vfx_script_lasers_graph_136
+ ___vfx_script_lasers_graph_136.cold.1
+ ___vfx_script_lasers_graph_138
+ ___vfx_script_lasers_graph_138.cold.1
+ ___vfx_script_lasers_graph_140
+ ___vfx_script_lasers_graph_140.cold.1
+ ___vfx_script_lasers_graph_141
+ ___vfx_script_lasers_graph_141.cold.1
+ ___vfx_script_lasers_graph_142
+ ___vfx_script_lasers_graph_142.cold.1
+ ___vfx_script_lasers_graph_146
+ ___vfx_script_lasers_graph_146.cold.1
+ ___vfx_script_lasers_graph_150
+ ___vfx_script_lasers_graph_150.cold.1
+ ___vfx_script_lasers_graph_151
+ ___vfx_script_lasers_graph_151.cold.1
+ ___vfx_script_lasers_graph_154
+ ___vfx_script_lasers_graph_154.cold.1
+ ___vfx_script_lasers_graph_156
+ ___vfx_script_lasers_graph_156.cold.1
+ ___vfx_script_lasers_particleInit_137
+ ___vfx_script_lasers_particleInit_137.cold.1
+ ___vfx_script_lasers_particleInit_143
+ ___vfx_script_lasers_particleInit_143.cold.1
+ ___vfx_script_lasers_particleInit_145
+ ___vfx_script_lasers_particleInit_145.cold.1
+ ___vfx_script_lasers_particleInit_148
+ ___vfx_script_lasers_particleInit_148.cold.1
+ ___vfx_script_lasers_particleInit_152
+ ___vfx_script_lasers_particleInit_152.cold.1
+ ___vfx_script_lasers_particleInit_155
+ ___vfx_script_lasers_particleInit_155.cold.1
+ ___vfx_script_lasers_particleUpdate_139
+ ___vfx_script_lasers_particleUpdate_139.cold.1
+ ___vfx_script_lasers_particleUpdate_144
+ ___vfx_script_lasers_particleUpdate_144.cold.1
+ ___vfx_script_lasers_particleUpdate_147
+ ___vfx_script_lasers_particleUpdate_147.cold.1
+ ___vfx_script_lasers_particleUpdate_149
+ ___vfx_script_lasers_particleUpdate_149.cold.1
+ ___vfx_script_lasers_particleUpdate_153
+ ___vfx_script_lasers_particleUpdate_153.cold.1
+ ___vfx_script_lasers_particleUpdate_157
+ ___vfx_script_lasers_particleUpdate_157.cold.1
+ ___vfx_script_lasers_particleUpdate_4
+ ___vfx_script_lasers_particleUpdate_4.cold.1
+ ___vfx_script_lighting_graph_6
+ ___vfx_script_lighting_graph_6.cold.1
+ ___vfx_script_lighting_graph_7
+ ___vfx_script_lighting_graph_7.cold.1
+ ___vfx_script_lighting_graph_8
+ ___vfx_script_lighting_graph_8.cold.1
+ ___vfx_script_rain_graph_216
+ ___vfx_script_rain_graph_216.cold.1
+ ___vfx_script_rain_graph_219
+ ___vfx_script_rain_graph_219.cold.1
+ ___vfx_script_rain_graph_222
+ ___vfx_script_rain_graph_222.cold.1
+ ___vfx_script_rain_graph_223
+ ___vfx_script_rain_graph_223.cold.1
+ ___vfx_script_rain_graph_226
+ ___vfx_script_rain_graph_226.cold.1
+ ___vfx_script_rain_graph_229
+ ___vfx_script_rain_graph_229.cold.1
+ ___vfx_script_rain_graph_232
+ ___vfx_script_rain_graph_232.cold.1
+ ___vfx_script_rain_graph_233
+ ___vfx_script_rain_graph_233.cold.1
+ ___vfx_script_rain_particleInit_213
+ ___vfx_script_rain_particleInit_213.cold.1
+ ___vfx_script_rain_particleInit_220
+ ___vfx_script_rain_particleInit_220.cold.1
+ ___vfx_script_rain_particleInit_230
+ ___vfx_script_rain_particleInit_230.cold.1
+ ___vfx_script_rain_particleUpdate_214
+ ___vfx_script_rain_particleUpdate_214.cold.1
+ ___vfx_script_rain_particleUpdate_215
+ ___vfx_script_rain_particleUpdate_215.cold.1
+ ___vfx_script_rain_particleUpdate_221
+ ___vfx_script_rain_particleUpdate_221.cold.1
+ ___vfx_script_rain_particleUpdate_231
+ ___vfx_script_rain_particleUpdate_231.cold.1
+ ___vfx_script_thumbsup_graph_127
+ ___vfx_script_thumbsup_graph_127.cold.1
+ ___vfx_script_thumbsup_graph_128
+ ___vfx_script_thumbsup_graph_128.cold.1
+ ___vfx_script_thumbsup_graph_130
+ ___vfx_script_thumbsup_graph_130.cold.1
+ ___vfx_script_thumbsup_graph_132
+ ___vfx_script_thumbsup_graph_132.cold.1
+ ___vfx_script_thumbsup_graph_134
+ ___vfx_script_thumbsup_graph_134.cold.1
+ ___vfx_script_thumbsup_graph_136
+ ___vfx_script_thumbsup_graph_136.cold.1
+ ___vfx_script_thumbsup_particleInit_129
+ ___vfx_script_thumbsup_particleInit_129.cold.1
+ ___vfx_script_thumbsup_particleInit_133
+ ___vfx_script_thumbsup_particleInit_133.cold.1
+ ___vfx_script_thumbsup_particleInit_138
+ ___vfx_script_thumbsup_particleInit_138.cold.1
+ ___vfx_script_thumbsup_particleUpdate_131
+ ___vfx_script_thumbsup_particleUpdate_131.cold.1
+ ___vfx_script_thumbsup_particleUpdate_135
+ ___vfx_script_thumbsup_particleUpdate_135.cold.1
+ ___vfx_script_thumbsup_particleUpdate_137
+ ___vfx_script_thumbsup_particleUpdate_137.cold.1
+ _dataPtrFromE5Buffer
+ _dataPtrFromE5Buffer.cold.1
+ _e5rt_buffer_object_alloc
+ _e5rt_buffer_object_get_data_ptr
+ _e5rt_buffer_object_get_size
+ _e5rt_buffer_object_release
+ _e5rt_e5_compiler_compile
+ _e5rt_e5_compiler_create
+ _e5rt_e5_compiler_options_create
+ _e5rt_e5_compiler_options_release
+ _e5rt_e5_compiler_options_set_compute_device_types_mask
+ _e5rt_e5_compiler_options_set_mil_entry_points
+ _e5rt_e5_compiler_release
+ _e5rt_error_code_get_string
+ _e5rt_execution_stream_create
+ _e5rt_execution_stream_encode_operation
+ _e5rt_execution_stream_execute_sync
+ _e5rt_execution_stream_operation_create_precompiled_compute_operation_with_options
+ _e5rt_execution_stream_operation_get_input_names
+ _e5rt_execution_stream_operation_get_num_inputs
+ _e5rt_execution_stream_operation_get_num_outputs
+ _e5rt_execution_stream_operation_get_output_names
+ _e5rt_execution_stream_operation_release
+ _e5rt_execution_stream_operation_retain_input_port
+ _e5rt_execution_stream_operation_retain_output_port
+ _e5rt_execution_stream_release
+ _e5rt_execution_stream_reset
+ _e5rt_execution_stream_set_ane_execution_priority
+ _e5rt_get_last_error_message
+ _e5rt_io_port_bind_buffer_object
+ _e5rt_io_port_bind_surface_object
+ _e5rt_io_port_release
+ _e5rt_precompiled_compute_op_create_options_create_with_program_function
+ _e5rt_precompiled_compute_op_create_options_release
+ _e5rt_precompiled_compute_op_create_options_set_operation_name
+ _e5rt_program_function_release
+ _e5rt_program_library_create
+ _e5rt_program_library_release
+ _e5rt_program_library_retain_program_function
+ _e5rt_surface_object_create_from_iosurface
+ _e5rt_surface_object_release
+ _getVCPRequestCoreMLANEPriorityPropertyKey
+ _getVCPRequestCoreMLANEPriorityPropertyKey.cold.1
+ _getVCPRequestCoreMLANEPriorityPropertyKeySymbolLoc
+ _getVCPRequestCoreMLANEPriorityPropertyKeySymbolLoc.ptr
+ _getVCPRequestEspressoPlanPriorityPropertyKey
+ _getVCPRequestEspressoPlanPriorityPropertyKey.cold.1
+ _getVCPRequestEspressoPlanPriorityPropertyKeySymbolLoc
+ _getVCPRequestEspressoPlanPriorityPropertyKeySymbolLoc.ptr
+ _gotLoadHelper_x27$_OBJC_CLASS_$_VFXClientTextureAsset
+ _gotLoadHelper_x8$_OBJC_CLASS_$_VFXAssetNode
+ _gotLoadHelper_x8$_OBJC_CLASS_$_VFXNode
+ _gotLoadHelper_x8$_OBJC_CLASS_$_VFXRenderOptions
+ _gotLoadHelper_x8$_OBJC_CLASS_$_VFXTextureAttachmentDescriptor
+ _gotLoadHelper_x8$_OBJC_CLASS_$_VFXTransaction
+ _gotLoadHelper_x8$_OBJC_CLASS_$_VFXWorld
+ _gotLoadHelper_x8$_VFXRenderGraphFinalColorAttachment
+ _gotLoadHelper_x8$_VFXRenderGraphMainDepthAttachment
+ _gotLoadHelper_x8$_VFXWorldLoaderOptionMetalLibraryURL
+ _kCVPixelBufferHeightKey
+ _kCVPixelBufferPlaneAlignmentKey
+ _kCVPixelBufferPoolMaximumBufferAgeKey
+ _kCVPixelBufferPoolMinimumBufferCountKey
+ _kCVPixelBufferPoolNameKey
+ _kCVPixelBufferWidthKey
+ _memsetE5Buffer
+ _memsetE5Buffer.cold.1
+ _memsetE5Buffer.cold.2
+ _objc_lookUpClass
+ _objc_msgSend$E5ExecutionPriority
+ _objc_msgSend$_computeFeatures:in_tex:out_tex:
+ _objc_msgSend$_computeFeaturesDerivatives:in_tex:out_tex:
+ _objc_msgSend$_createImagePyramid:in_tex:I_idx:
+ _objc_msgSend$_doNLRegularization:in_uv_tex:join_tex:w_tex:out_uv_tex:
+ _objc_msgSend$_doSolver:scale:in_uv_tex:in_G0_tex:in_G1_tex:in_C0_tex:in_C1_tex:out_uv_tex:out_w_tex:
+ _objc_msgSend$_downscale2X:in_tex:out_tex:
+ _objc_msgSend$_enqueueFlowConsistency:in_uv0_tex:in_uv1_tex:out_uv_tex:
+ _objc_msgSend$_enqueueKeypointsFromFlow:in_uv_fwd_tex:in_uv_bwd_tex:out_kpt_buf:block_size:bidirectional_error:out_num_keypoints:
+ _objc_msgSend$_setupBuffer:
+ _objc_msgSend$_setupPipelines:
+ _objc_msgSend$_zeroFlow:uv_tex:
+ _objc_msgSend$addAdditionalOutput:allowCompressed:
+ _objc_msgSend$addAdditionalOutput:allowCompressed:pixelFormat:
+ _objc_msgSend$addChildNode:
+ _objc_msgSend$adjustScissorRectToImageBlocks:imageBlockSize:
+ _objc_msgSend$allowCompressed
+ _objc_msgSend$applyPortraitBlur:inColorBuffer:inColorPyramid:inBackgroundBuffer:effectRenderRequest:
+ _objc_msgSend$arrayLength
+ _objc_msgSend$asRGBAFromYUV
+ _objc_msgSend$asYUV
+ _objc_msgSend$assetRegistry
+ _objc_msgSend$asyncVFXInit:metalContext:
+ _objc_msgSend$behaviorGraph
+ _objc_msgSend$blitCommandEncoder
+ _objc_msgSend$camera
+ _objc_msgSend$characterDirectionForLanguage:
+ _objc_msgSend$childNodeWithName:recursively:
+ _objc_msgSend$childNodes
+ _objc_msgSend$clearIOSurface:value:
+ _objc_msgSend$clientIdentifier
+ _objc_msgSend$compressedPixelFormat:
+ _objc_msgSend$compressedPixelFormat:compression:
+ _objc_msgSend$computeDownsamplingFactorWithInputSource:inputTarget:renderRequest:
+ _objc_msgSend$computeDownsamplingStepsWithInputSize:targetSize:
+ _objc_msgSend$computePipelineStateFor:constants:
+ _objc_msgSend$copyInColor:toOutColor:
+ _objc_msgSend$createFocusObject:anamorphicFactor:radialObstructionFactor:colorSize:circleOfConfusionReference:fNumberLimitWeight:
+ _objc_msgSend$createFromPixelbuffer:device:textureCache:metalYCBCRConversion:read:write:
+ _objc_msgSend$createTextureFromPixelBuffer:device:textureCache:sRGB:metalYCBCRConversion:
+ _objc_msgSend$depthPrioritization
+ _objc_msgSend$depthPrioritizationFromEffectQuality:
+ _objc_msgSend$descriptorForInput:error:
+ _objc_msgSend$descriptorForOutput:error:
+ _objc_msgSend$disparityApplyPostModifier:inDisparity:outDisparity:postModifier:
+ _objc_msgSend$disparityMinMaxApplyPostModifier:disparityMinMaxBuffer:postModifier:
+ _objc_msgSend$disparityPortraitPreviewDeadzone:inDisparity:outDisparity:postModifier:
+ _objc_msgSend$downsample:
+ _objc_msgSend$downsample:dst:sync_m2m:
+ _objc_msgSend$downsampleToLayer:source:dest:
+ _objc_msgSend$effectUtil
+ _objc_msgSend$estimateColorTemperatureFromBackground:colorTransferFunction:matrixYUVtoRGB:inBackgroundLuma:inBackgroundChroma:outColorTemperatureBuffer:
+ _objc_msgSend$estimateLightIntensityWithFaceRects:inColor:numberOfFaceRects:transform:humanDetections:asyncWork:
+ _objc_msgSend$faceAttributesNetwork
+ _objc_msgSend$flush
+ _objc_msgSend$functionForIdentifier:error:
+ _objc_msgSend$generateMipmapsForTexture:
+ _objc_msgSend$getChromaOffset:
+ _objc_msgSend$getMTLTextureDescriptor:device:metalYCBCRConversion:
+ _objc_msgSend$imageBlockSize
+ _objc_msgSend$initVFX:sharedResources:asyncInitQueue:
+ _objc_msgSend$initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:
+ _objc_msgSend$initWithFigMetalContext:
+ _objc_msgSend$initWithLumaTexture:chromaTexture:
+ _objc_msgSend$initWithMetalContext:availableEffectTypes:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:
+ _objc_msgSend$initWithMetalContext:colorSize:colorConversion:prewarmOnly:humanDetections:sharedResources:asyncInitQueue:
+ _objc_msgSend$initWithMetalContext:colorSize:depthPrioritization:sharedResources:
+ _objc_msgSend$initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:
+ _objc_msgSend$initWithMetalContext:correctionColorCube:
+ _objc_msgSend$initWithMetalContext:effectRelighting:effectDescritor:renderState:util:colorConversion:msrColorPyramid:vfxRenderEffect:depthConverter:disparityFixedFocus:faceDisparityArray:focusDisparityRaw:focusDisparityModifiers:
+ _objc_msgSend$initWithMetalContext:inputSize:targetSize:rotateTargetPixelBuffer:compressedIntermediates:sRGB:sharedResources:
+ _objc_msgSend$initWithMetalContext:msrColorPyramid:colorSize:prewarmOnly:sharedResources:
+ _objc_msgSend$initWithMetalContext:sharedResources:
+ _objc_msgSend$initWithName:index:
+ _objc_msgSend$initWithSize:colorSpace:pixelFormat:allowCompressed:
+ _objc_msgSend$initWithTextureSize:scissorRect:outRect:imageblockSize:
+ _objc_msgSend$initWithWidth:height:
+ _objc_msgSend$initWithbundle:andOptionalCommandQueue:
+ _objc_msgSend$initializeCubeMap:inputTexture:
+ _objc_msgSend$inputCropRect
+ _objc_msgSend$inputSourcePixelBuffer
+ _objc_msgSend$inputTargetPixelBuffer
+ _objc_msgSend$inputTargetRect
+ _objc_msgSend$inputTargetRectCornerRadius
+ _objc_msgSend$is420YpCbCr8:
+ _objc_msgSend$library
+ _objc_msgSend$lightBinding
+ _objc_msgSend$macroBlockSizeForPixelFormat:device:
+ _objc_msgSend$mergeWorld:parentNode:parentAssetNode:
+ _objc_msgSend$newBufferWithPixelFormat:width:data:metalContext:
+ _objc_msgSend$outputPixelBuffer
+ _objc_msgSend$postProcessUpdateFrameForInferenceOutputKeyBuffer:inferenceOutputValueBuffer:postProcessingOutputKeyBuffer:postProcessingOutputValueBuffer:error:
+ _objc_msgSend$preferredLanguages
+ _objc_msgSend$prepareForRenderer:progressHandler:
+ _objc_msgSend$progressHandler
+ _objc_msgSend$reconfigure:isInitialized:
+ _objc_msgSend$removeFromParent
+ _objc_msgSend$removeFromParentNode
+ _objc_msgSend$renderWithTextureAttachmentProvider:options:
+ _objc_msgSend$rendererWithCommandQueue:options:
+ _objc_msgSend$replaceBackground:inColor:inColorPyramid:inSegmentation:effectRenderRequest:outColor:frameIndex:
+ _objc_msgSend$resetIfNeeded
+ _objc_msgSend$rgbMinMax
+ _objc_msgSend$rootAssetNode
+ _objc_msgSend$rootNode
+ _objc_msgSend$sampleFaceRects:maxFaceRects:faceRects:faceRectsState:focusDisparityMax:inDisparity:outFaceDistanceArray:
+ _objc_msgSend$setAntialiasingMode:
+ _objc_msgSend$setArrayLength:
+ _objc_msgSend$setCustomFilter:alignment:src:dst:luma_param:chroma_param:
+ _objc_msgSend$setEffectUtil:
+ _objc_msgSend$setProjectionTransform:
+ _objc_msgSend$setRootAssetNode:
+ _objc_msgSend$setRootNode:
+ _objc_msgSend$setTextureAsYUV:
+ _objc_msgSend$setUtil:
+ _objc_msgSend$setVfxResources:
+ _objc_msgSend$setWorld:
+ _objc_msgSend$studioLightInColor:inDiffuse:inDisparity:inFocusDisparityModifier:outColor:relightStrength:studioLightFromSegmentationBlend:studioLightEffectModifier:
+ _objc_msgSend$supportsMetalYCBCRConversion
+ _objc_msgSend$supportsMetalYCBCRConversion:
+ _objc_msgSend$transform:crop:rotationDegree:toDest:synchronous:
+ _objc_msgSend$transform:srcRect:dst:dstRect:rotate:sync_m2m:
+ _objc_msgSend$updateAtTime:
+ _objc_msgSend$updateDisparity:inScreenCaptureRect:inDisparity:outDisparity:focalLenIn35mmFilm:fNumber:
+ _objc_msgSend$updateFocusObject:faceRectCount:disparityFocusOffsetSDOF:disparityFocusOffsetReactions:disparityFocusOffsetStudioLight:exponentialMovingAverageSDOF:exponentialMovingAverageStudioLight:faceRectsState:isFirstFrame:emitNewReaction:focusOnAll:lastFocus:inFaceDisparityArray:outDisparityModifiers:outDisparityFocus:outStudioLightEffectModifier:outUseDisparityBufferForReactions:
+ _objc_msgSend$updateHumanDetections:
+ _objc_msgSend$updatePyramid:inPTTexture:
+ _objc_msgSend$util
+ _objc_msgSend$vfxRenderer
+ _objc_msgSend$vfxResources
+ _objc_msgSend$world
+ _objc_msgSend$worldWithURL:options:error:
+ _renderDebugInformation:effectRenderRequest:reactionStates:disparity:disparityCentered:normal:diffuse:temporalFilter:humanDetections:transform:fNumber:focusDisparityRaw:useDisparityBufferForReactions:outColor:.frameIndex
+ _sel_registerName
+ _supportsMetalYCBCRConversion.hasHardwareSupport
+ _supportsMetalYCBCRConversion.token
- +[LKTFlowGPU _computeScalingFactor:dst_tex:scale_xy_inv:coeff:]
- +[LKTFlowGPU _computeScalingFactor:dst_tex:scale_xy_inv:coeff:].cold.1
- +[PTImageblockConfig adjustScissorRectToImageBlocks:]
- +[PTPixelBufferUtil createTextureFromPixelBuffer:device:textureCache:sRGB:].cold.1
- +[PTPixelBufferUtil getMTLTextureDescriptor:device:].cold.1
- +[PTRaytracingUtils createFocusObject:anamorphicFactor:colorSize:circleOfConfusionReference:fNumberLimitWeight:]
- +[PTRenderPipeline prewarmForCameraCaptured].cold.3
- +[PTTexture createFromPixelbuffer:device:textureCache:read:write:].cold.1
- +[PTTexture createFromPixelbuffer:device:textureCache:read:write:].cold.2
- -[LKTFlowGPU .cxx_destruct]
- -[LKTFlowGPU _computeFeaturesDerivativesWithCommandBuffer:in_tex:out_tex:]
- -[LKTFlowGPU _computeFeaturesWithCommandBuffer:in_tex:out_tex:]
- -[LKTFlowGPU _computeOpticalFlow:computeFeatureI0:computeFeatureI1:]
- -[LKTFlowGPU _computeOpticalFlowBidirectional:]
- -[LKTFlowGPU _createImagePyramidWithCommandBuffer:in_tex:I_idx:]
- -[LKTFlowGPU _doNLRegularizationWithCommandBuffer:in_uv_tex:join_tex:w_tex:out_uv_tex:]
- -[LKTFlowGPU _doSolverWithCommandBuffer:scale:in_uv_tex:in_G0_tex:in_G1_tex:in_C0_tex:in_C1_tex:out_uv_tex:out_w_tex:]
- -[LKTFlowGPU _downscale2XWithCommandBuffer:in_tex:out_tex:]
- -[LKTFlowGPU _enqueueFlowConsistencyWithCommandBuffer:in_uv0_tex:in_uv1_tex:out_uv_tex:]
- -[LKTFlowGPU _enqueueKeypointsFromFlowWithCommandBuffer:in_uv_fwd_tex:in_uv_bwd_tex:out_kpt_buf:block_size:bidirectional_error:out_num_keypoints:]
- -[LKTFlowGPU _initMemory:height:nscales:]
- -[LKTFlowGPU _setDefaultParameters]
- -[LKTFlowGPU _setupBuffer]
- -[LKTFlowGPU _setupBuffer].cold.1
- -[LKTFlowGPU _setupBuffer].cold.2
- -[LKTFlowGPU _setupBuffer].cold.3
- -[LKTFlowGPU _setupPipelines]
- -[LKTFlowGPU _setupPipelines].cold.1
- -[LKTFlowGPU _zeroFlowWithCommandBuffer:uv_tex:]
- -[LKTFlowGPU aux_size]
- -[LKTFlowGPU computeKeypointsFromTexForwardFlow:backwardFlow:bidirectionalError:blockSize:outNumKeypoints:commandBuffer:]
- -[LKTFlowGPU estimateFlowFromTexReference:target:commandBuffer:]
- -[LKTFlowGPU estimateFlowStreamTex:commandBuffer:]
- -[LKTFlowGPU estimateFlowStreamTex:index:doOpticalFlow:commandBuffer:]
- -[LKTFlowGPU initWithMetalContext:width:height:nscales:]
- -[LKTFlowGPU initWithMetalContext:width:height:nscales:].cold.1
- -[LKTFlowGPU initWithMetalContext:width:height:nscales:].cold.2
- -[LKTFlowGPU isBidirectional]
- -[LKTFlowGPU isInverse]
- -[LKTFlowGPU isValid]
- -[LKTFlowGPU keypoints]
- -[LKTFlowGPU needConversionBGRA2YUVA]
- -[LKTFlowGPU newBufferWithPixelFormat:width:data:]
- -[LKTFlowGPU newBufferWithPixelFormat:width:data:].cold.1
- -[LKTFlowGPU nlreg_padding]
- -[LKTFlowGPU nlreg_radius]
- -[LKTFlowGPU nlreg_sigma_c]
- -[LKTFlowGPU nlreg_sigma_l]
- -[LKTFlowGPU nlreg_sigma_w]
- -[LKTFlowGPU nscales]
- -[LKTFlowGPU nwarpings]
- -[LKTFlowGPU ref_size]
- -[LKTFlowGPU reset]
- -[LKTFlowGPU setIsBidirectional:]
- -[LKTFlowGPU setIsInverse:]
- -[LKTFlowGPU setNeedConversionBGRA2YUVA:]
- -[LKTFlowGPU setNlreg_padding:]
- -[LKTFlowGPU setNlreg_radius:]
- -[LKTFlowGPU setNlreg_sigma_c:]
- -[LKTFlowGPU setNlreg_sigma_l:]
- -[LKTFlowGPU setNlreg_sigma_w:]
- -[LKTFlowGPU setNwarpings:]
- -[LKTFlowGPU setOutputTexUV:]
- -[LKTFlowGPU setOutputTexUVForward:backward:]
- -[LKTFlowGPU setPreset:]
- -[LKTFlowGPU setUseNonLocalRegularization:]
- -[LKTFlowGPU streamFrameCount]
- -[LKTFlowGPU useNonLocalRegularization]
- -[PTBackgroundReplacement applyPortraitBlur:inColorBuffer:inBackgroundBuffer:effectRenderRequest:]
- -[PTBackgroundReplacement replaceBackground:inYUV:inSegmentation:effectRenderRequest:outYUV:frameIndex:]
- -[PTBackgroundReplacement replaceBackground:inYUV:inSegmentation:effectRenderRequest:outYUV:frameIndex:].cold.1
- -[PTBackgroundReplacement replaceBackground:inYUV:inSegmentation:effectRenderRequest:outYUV:frameIndex:].cold.2
- -[PTBackgroundReplacement replaceBackground:inYUV:inSegmentation:effectRenderRequest:outYUV:frameIndex:].cold.3
- -[PTBackgroundReplacement replaceBackground:inYUV:inSegmentation:effectRenderRequest:outYUV:frameIndex:].cold.4
- -[PTCVMNetwork highResNetwork]
- -[PTCVMNetwork initWithMetalContext:colorSize:effectUtil:util:useHighResNetwork:sharedResources:]
- -[PTCVMNetwork initWithMetalContext:colorSize:effectUtil:util:useHighResNetwork:sharedResources:].cold.1
- -[PTCVMNetwork initWithMetalContext:colorSize:effectUtil:util:useHighResNetwork:sharedResources:].cold.2
- -[PTCVMNetwork initWithMetalContext:colorSize:effectUtil:util:useHighResNetwork:sharedResources:].cold.3
- -[PTCVMNetwork initWithMetalContext:colorSize:effectUtil:util:useHighResNetwork:sharedResources:].cold.4
- -[PTCVMNetwork initWithMetalContext:colorSize:effectUtil:util:useHighResNetwork:sharedResources:].cold.5
- -[PTCVMNetwork initWithMetalContext:colorSize:effectUtil:util:useHighResNetwork:sharedResources:].cold.6
- -[PTCVMNetwork initWithMetalContext:colorSize:effectUtil:util:useHighResNetwork:sharedResources:].cold.7
- -[PTCVMNetwork initWithMetalContext:colorSize:effectUtil:util:useHighResNetwork:sharedResources:].cold.8
- -[PTCVMNetwork initWithMetalContext:colorSize:effectUtil:util:useHighResNetwork:sharedResources:].cold.9
- -[PTEffect validPixelBuffer:].cold.3
- -[PTEffectDebugLayer initWithMetalContext:effectRelighting:renderState:util:colorConversion:msrColorPyramid:vfxRenderEffect:depthConverter:disparityFixedFocus:faceDisparityArray:focusDisparityRaw:focusDisparityModifiers:]
- -[PTEffectDebugLayer renderDebugInformation:effectRenderRequest:reactionStates:disparity:disparityCentered:normal:diffuse:temporalFilter:humanDetections:transform:fNumber:focusDisparityRaw:useDisparityBufferForReactions:outYUV:]
- -[PTEffectDebugLayer renderDebugInformation:effectRenderRequest:reactionStates:disparity:disparityCentered:normal:diffuse:temporalFilter:humanDetections:transform:fNumber:focusDisparityRaw:useDisparityBufferForReactions:outYUV:].cold.1
- -[PTEffectManagerDebug .cxx_destruct]
- -[PTEffectManagerDebug depthNearFar]
- -[PTEffectManagerDebug depthOutputPixelFormat]
- -[PTEffectManagerDebug effectPriority]
- -[PTEffectManagerDebug effectType]
- -[PTEffectManagerDebug enabled]
- -[PTEffectManagerDebug initWithMetalContext:colorSize:]
- -[PTEffectManagerDebug initWithMetalContext:colorSize:].cold.1
- -[PTEffectManagerDebug initWithMetalContext:colorSize:].cold.2
- -[PTEffectManagerDebug render:renderRequest:input:output:]
- -[PTEffectManagerDebug reverseZ]
- -[PTEffectManagerDebug rgbaOutputPixelFormat]
- -[PTEffectManagerDebug setDepthNearFar:]
- -[PTEffectManagerDebug setEnabled:]
- -[PTEffectManagerDebug setReverseZ:]
- -[PTEffectManagerDebug update:renderRequest:]
- -[PTEffectRelighting initWithMetalContext:faceAttributesNetwork:availableEffectTypes:effectUtil:util:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:]
- -[PTEffectRelighting initWithMetalContext:faceAttributesNetwork:availableEffectTypes:effectUtil:util:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.1
- -[PTEffectRelighting initWithMetalContext:faceAttributesNetwork:availableEffectTypes:effectUtil:util:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.10
- -[PTEffectRelighting initWithMetalContext:faceAttributesNetwork:availableEffectTypes:effectUtil:util:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.11
- -[PTEffectRelighting initWithMetalContext:faceAttributesNetwork:availableEffectTypes:effectUtil:util:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.2
- -[PTEffectRelighting initWithMetalContext:faceAttributesNetwork:availableEffectTypes:effectUtil:util:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.3
- -[PTEffectRelighting initWithMetalContext:faceAttributesNetwork:availableEffectTypes:effectUtil:util:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.4
- -[PTEffectRelighting initWithMetalContext:faceAttributesNetwork:availableEffectTypes:effectUtil:util:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.5
- -[PTEffectRelighting initWithMetalContext:faceAttributesNetwork:availableEffectTypes:effectUtil:util:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.6
- -[PTEffectRelighting initWithMetalContext:faceAttributesNetwork:availableEffectTypes:effectUtil:util:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.7
- -[PTEffectRelighting initWithMetalContext:faceAttributesNetwork:availableEffectTypes:effectUtil:util:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.8
- -[PTEffectRelighting initWithMetalContext:faceAttributesNetwork:availableEffectTypes:effectUtil:util:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:].cold.9
- -[PTEffectRelighting studioLightInYUV:inDiffuse:inDisparity:inFocusDisparityModifier:outYUV:relightStrength:studioLightFromSegmentationBlend:studioLightEffectModifier:]
- -[PTEffectRelighting studioLightInYUV:inDiffuse:inDisparity:inFocusDisparityModifier:outYUV:relightStrength:studioLightFromSegmentationBlend:studioLightEffectModifier:].cold.1
- -[PTEffectRenderer copyInYUV:toOutYUV:]
- -[PTEffectRenderer copyInYUV:toOutYUV:].cold.1
- -[PTEffectRenderer copyInYUV:toOutYUV:].cold.2
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:]
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.1
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.10
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.11
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.12
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.13
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.14
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.15
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.16
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.17
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.18
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.19
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.2
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.20
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.21
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.22
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.23
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.24
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.25
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.26
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.27
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.28
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.29
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.3
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.30
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.31
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.32
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.33
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.34
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.35
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.36
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.37
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.38
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.4
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.5
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.6
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.7
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.8
- -[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:].cold.9
- -[PTEffectRenderer lowResDisparitySizeFromEffectDescriptor]
- -[PTEffectUtil copySingleChannelInTex:outTex:]
- -[PTEffectUtil initWithMetalContext:].cold.5
- -[PTEffectUtil sampleFaceRectsWithMaxFaceRects:faceRects:faceRectsState:focusDisparityMax:inDisparity:outFaceDistanceArray:]
- -[PTEffectUtil updateDisparityWithScreenCaptureRect:inDisparity:outDisparity:focalLenIn35mmFilm:fNumber:]
- -[PTEffectUtil updateFocusObjectWithFaceRectCount:disparityFocusOffsetSDOF:disparityFocusOffsetReactions:disparityFocusOffsetStudioLight:exponentialMovingAverageSDOF:exponentialMovingAverageStudioLight:faceRectsState:isFirstFrame:emitNewReaction:focusOnAll:lastFocus:inFaceDisparityArray:outDisparityModifiers:outDisparityFocus:outStudioLightEffectModifier:outUseDisparityBufferForReactions:]
- -[PTImageblockConfig initWithTextureSize:scissorRect:outRect:]
- -[PTMSRResize _downsample:toDest:useCustomFilter:centerAlignment:synchronous:]
- -[PTMSRResize _rotate:toDest:synchronous:]
- -[PTMSRResize addAdditionalOutput:]
- -[PTMSRResize downsampleQuarterSizeToTargetSize:]
- -[PTMSRResize downsampleQuarterSizeToTargetSize:].cold.1
- -[PTMSRResize downsampleQuarterSizeToTargetSize:].cold.2
- -[PTMSRResize downsampleQuarterSizeToTargetSize:].cold.3
- -[PTMSRResize downsampleQuarterSizeToTargetSize:].cold.4
- -[PTMSRResize downsampleToLayer:]
- -[PTMSRResize downsampleToQuarterSize:]
- -[PTMSRResize downsampleToQuarterSize:].cold.1
- -[PTMSRResize downsampleToQuarterSize:].cold.2
- -[PTMSRResize initWithMetalContext:inputSize:targetSize:rotateTargetPixelBuffer:sRGB:sharedResources:]
- -[PTMSRResize initWithMetalContext:inputSize:targetSize:rotateTargetPixelBuffer:sRGB:sharedResources:].cold.1
- -[PTMSRResize initWithMetalContext:inputSize:targetSize:rotateTargetPixelBuffer:sRGB:sharedResources:].cold.2
- -[PTMSRResize initWithMetalContext:inputSize:targetSize:rotateTargetPixelBuffer:sRGB:sharedResources:].cold.3
- -[PTMSRResize initWithMetalContext:inputSize:targetSize:rotateTargetPixelBuffer:sRGB:sharedResources:].cold.4
- -[PTMSRResize initWithMetalContext:inputSize:targetSize:rotateTargetPixelBuffer:sRGB:sharedResources:].cold.5
- -[PTMSRResize initWithMetalContext:inputSize:targetSize:rotateTargetPixelBuffer:sRGB:sharedResources:].cold.6
- -[PTMSRResize init].cold.1
- -[PTMSRResize pyramidRGBAPixelBuffer]
- -[PTMSRResize queryCapabilities]
- -[PTMSRResize queryCapabilities].cold.1
- -[PTMSRResize rotate:crop:rotationDegree:toDest:synchronous:]
- -[PTMSRResize rotate:crop:rotationDegree:toDest:synchronous:].cold.1
- -[PTMSRResize setCustomFilter:alignment:sourceWidth:sourceHeight:destinationWidth:destinationHeight:luma_param:chroma_param:]
- -[PTMSRResizeAdditionalOutput initWithSize:colorSpace:]
- -[PTMSRResizeAdditionalOutput initWithSize:colorSpace:].cold.1
- -[PTMetalContext computePipelineStateFor:withConstants:].cold.1
- -[PTMetalContext initWithCommandQueue:bundleClass:].cold.2
- -[PTMetalContext initWithCommandQueue:bundleClass:].cold.3
- -[PTMetalContext initWithCommandQueue:bundleClass:].cold.4
- -[PTMetalContext initWithCommandQueue:bundleClass:].cold.5
- -[PTMetalContext initWithCommandQueue:bundleClass:].cold.6
- -[PTPersonSemanticsNetwork initWithMetalContext:effectUtil:sharedResources:]
- -[PTPersonSemanticsNetwork initWithMetalContext:effectUtil:sharedResources:].cold.1
- -[PTPersonSemanticsNetwork initWithMetalContext:effectUtil:sharedResources:].cold.2
- -[PTPersonSemanticsNetwork initWithMetalContext:effectUtil:sharedResources:].cold.3
- -[PTPersonSemanticsNetwork initWithMetalContext:effectUtil:sharedResources:].cold.4
- -[PTPersonSemanticsNetwork initWithMetalContext:effectUtil:sharedResources:].cold.5
- -[PTPersonSemanticsNetwork initWithMetalContext:effectUtil:sharedResources:].cold.6
- -[PTPersonSemanticsNetwork initWithMetalContext:effectUtil:sharedResources:].cold.7
- -[PTPersonSemanticsNetwork initWithMetalContext:effectUtil:sharedResources:].cold.8
- -[PTPyramid bicubic]
- -[PTPyramid initWithMetalContext:colorSize:pixelFormat:skipFullSizeLayer:doFirstLevelGaussianDownsample:mipmapLevelCount:].cold.10
- -[PTPyramid initWithMetalContext:colorSize:pixelFormat:skipFullSizeLayer:doFirstLevelGaussianDownsample:mipmapLevelCount:].cold.9
- -[PTPyramid setBicubic:]
- -[PTPyramid updateLevel0FromPTTextureRGBA:inPTTextureRGBA:doFirstLevelGaussianDownsample:]
- -[PTPyramid updateLevel0FromPTTextureRGBA:inPTTextureRGBA:doFirstLevelGaussianDownsample:].cold.1
- -[PTPyramid updateLevel0FromPTTextureYUV:inPTTextureYUV:doFirstLevelGaussianDownsample:]
- -[PTPyramid updateLevel0FromPTTextureYUV:inPTTextureYUV:doFirstLevelGaussianDownsample:].cold.1
- -[PTPyramid updateLevel0and1FromPTTextureRGBA:inPTTextureRGBA:]
- -[PTPyramid updateLevel0and1FromPTTextureRGBA:inPTTextureRGBA:].cold.1
- -[PTPyramid updateLevel0and1FromPTTextureYUV:inPTTextureYUV:]
- -[PTPyramid updateLevel0and1FromPTTextureYUV:inPTTextureYUV:].cold.1
- -[PTPyramid updatePyramidFromPTTexture:inPTTexture:]
- -[PTQualitySettings disparityGuidedFilterEpsilon]
- -[PTQualitySettings doDisparityUpsampling]
- -[PTQualitySettings setDisparityGuidedFilterEpsilon:]
- -[PTRaytracingUtils disparityApplyPostModifier:inDisparity:outDisparity:postModfier:]
- -[PTRaytracingUtils disparityApplyPostModifier:inDisparity:outDisparity:postModfier:].cold.1
- -[PTRaytracingUtils disparityMinMaxApplyPostModifier:disparityMinMaxBuffer:postModfier:]
- -[PTRaytracingUtils disparityMinMaxApplyPostModifier:disparityMinMaxBuffer:postModfier:].cold.1
- -[PTRaytracingUtils disparityPortraitPreviewDeadzone:inDisparity:outDisparity:postModfier:]
- -[PTRaytracingUtils disparityPortraitPreviewDeadzone:inDisparity:outDisparity:postModfier:].cold.1
- -[PTRaytracingV14 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:]
- -[PTRaytracingV14 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.1
- -[PTRaytracingV14 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.2
- -[PTRaytracingV14 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.3
- -[PTRaytracingV14 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.4
- -[PTRaytracingV14 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.5
- -[PTRaytracingV2002 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:]
- -[PTRaytracingV2002 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.1
- -[PTRaytracingV2002 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.10
- -[PTRaytracingV2002 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.11
- -[PTRaytracingV2002 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.12
- -[PTRaytracingV2002 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.13
- -[PTRaytracingV2002 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.14
- -[PTRaytracingV2002 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.15
- -[PTRaytracingV2002 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.16
- -[PTRaytracingV2002 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.17
- -[PTRaytracingV2002 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.2
- -[PTRaytracingV2002 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.3
- -[PTRaytracingV2002 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.4
- -[PTRaytracingV2002 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.5
- -[PTRaytracingV2002 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.6
- -[PTRaytracingV2002 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.7
- -[PTRaytracingV2002 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.8
- -[PTRaytracingV2002 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.9
- -[PTRaytracingV3001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:]
- -[PTRaytracingV3001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.1
- -[PTRaytracingV3001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.10
- -[PTRaytracingV3001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.11
- -[PTRaytracingV3001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.12
- -[PTRaytracingV3001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.13
- -[PTRaytracingV3001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.14
- -[PTRaytracingV3001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.15
- -[PTRaytracingV3001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.16
- -[PTRaytracingV3001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.17
- -[PTRaytracingV3001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.18
- -[PTRaytracingV3001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.19
- -[PTRaytracingV3001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.2
- -[PTRaytracingV3001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.20
- -[PTRaytracingV3001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.3
- -[PTRaytracingV3001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.4
- -[PTRaytracingV3001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.5
- -[PTRaytracingV3001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.6
- -[PTRaytracingV3001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.7
- -[PTRaytracingV3001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.8
- -[PTRaytracingV3001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.9
- -[PTRaytracingV4001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:]
- -[PTRaytracingV4001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.1
- -[PTRaytracingV4001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.10
- -[PTRaytracingV4001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.11
- -[PTRaytracingV4001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.12
- -[PTRaytracingV4001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.13
- -[PTRaytracingV4001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.14
- -[PTRaytracingV4001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.15
- -[PTRaytracingV4001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.16
- -[PTRaytracingV4001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.17
- -[PTRaytracingV4001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.2
- -[PTRaytracingV4001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.3
- -[PTRaytracingV4001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.4
- -[PTRaytracingV4001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.5
- -[PTRaytracingV4001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.6
- -[PTRaytracingV4001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.7
- -[PTRaytracingV4001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.8
- -[PTRaytracingV4001 initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:].cold.9
- -[PTRenderDebugLayer initWithMetalContext:renderEffects:]
- -[PTRenderDebugLayer renderDebugLayer:renderRequest:inDisparity:disparityOffset:focusObject:quality:edgeTolerance:debugTextures:debugRendering:]
- -[PTRenderDebugLayer renderTurboMix:inTex:inRGBA:outRGBA:valueOffset:valueMinMax:valueAbs:colorRangeMax:channelMultiplier:mixFraction:region:]
- -[PTRenderEffectContainer .cxx_destruct]
- -[PTRenderEffectContainer initWithMetalContext:renderEffect:colorSize:]
- -[PTRenderEffectContainer initWithMetalContext:rgbaOutputPixelFormat:depthOutputPixelFormat:colorSize:]
- -[PTRenderEffectContainer initWithMetalContext:rgbaOutputPixelFormat:depthOutputPixelFormat:colorSize:].cold.1
- -[PTRenderEffectContainer initWithMetalContext:rgbaOutputPixelFormat:depthOutputPixelFormat:colorSize:].cold.2
- -[PTRenderEffectContainer initWithMetalContext:rgbaOutputPixelFormat:depthOutputPixelFormat:colorSize:].cold.3
- -[PTRenderEffectContainer renderEffectInput]
- -[PTRenderEffectContainer renderEffectOutput]
- -[PTRenderEffectContainer renderEffect]
- -[PTRenderEffectContainer setRenderEffect:]
- -[PTRenderEffectContainer setRenderEffectInput:]
- -[PTRenderEffectContainer setRenderEffectOutput:]
- -[PTRenderEffectInput focusDistance]
- -[PTRenderEffectInput setFocusDistance:]
- -[PTRenderEffectOutput .cxx_destruct]
- -[PTRenderEffectOutput effectDepth]
- -[PTRenderEffectOutput effectRGBA]
- -[PTRenderEffectOutput initWithEffectRGBA:effectDepth:]
- -[PTRenderPipelineState addRenderEffect:]
- -[PTScreenCaptureComposite .cxx_destruct]
- -[PTScreenCaptureComposite floatingAlphaCutout:inPersonSegmentation:bilbyPersonMask:bilbyEffectMask:bilbyFloatingBackgroundRGBA:outVideoColorBufferRGBA:]
- -[PTScreenCaptureComposite initWithMetalContext:]
- -[PTScreenCaptureComposite initWithMetalContext:].cold.1
- -[PTSyntheticLight estimateLightIntensityWithFaceRects:inTex:numberOfFaceRects:transform:humanDetections:asyncWork:]
- -[PTSyntheticLight estimateLightIntensityWithFaceRects:inTex:numberOfFaceRects:transform:humanDetections:asyncWork:].cold.1
- -[PTSyntheticLight initWithMetalContext:faceAttributesNetwork:effectUtil:msrColorPyramid:colorSize:prewarmOnly:sharedResources:]
- -[PTSyntheticLight initWithMetalContext:faceAttributesNetwork:effectUtil:msrColorPyramid:colorSize:prewarmOnly:sharedResources:].cold.1
- -[PTSyntheticLight initWithMetalContext:faceAttributesNetwork:effectUtil:msrColorPyramid:colorSize:prewarmOnly:sharedResources:].cold.2
- -[PTSyntheticLight initWithMetalContext:faceAttributesNetwork:effectUtil:msrColorPyramid:colorSize:prewarmOnly:sharedResources:].cold.3
- -[PTSyntheticLight initWithMetalContext:faceAttributesNetwork:effectUtil:msrColorPyramid:colorSize:prewarmOnly:sharedResources:].cold.4
- -[PTSyntheticLight initWithMetalContext:faceAttributesNetwork:effectUtil:msrColorPyramid:colorSize:prewarmOnly:sharedResources:].cold.5
- -[PTSyntheticLight initWithMetalContext:faceAttributesNetwork:effectUtil:msrColorPyramid:colorSize:prewarmOnly:sharedResources:].cold.6
- -[PTSyntheticLight initWithMetalContext:faceAttributesNetwork:effectUtil:msrColorPyramid:colorSize:prewarmOnly:sharedResources:].cold.7
- -[PTSyntheticLight initWithMetalContext:faceAttributesNetwork:effectUtil:msrColorPyramid:colorSize:prewarmOnly:sharedResources:].cold.8
- -[PTSyntheticLight initWithMetalContext:faceAttributesNetwork:effectUtil:msrColorPyramid:colorSize:prewarmOnly:sharedResources:].cold.9
- -[PTVFXRenderEffect addNewEffectFromEvent:renderRequest:time:presenterOverlaySmall:].cold.6
- -[PTVFXRenderEffect addNewEffectFromEvent:renderRequest:time:presenterOverlaySmall:].cold.7
- -[PTVFXRenderEffect asyncVFXInit]
- -[PTVFXRenderEffect asyncVFXInit].cold.1
- -[PTVFXRenderEffect asyncVFXInit].cold.2
- -[PTVFXRenderEffect initVFX:asyncInitQueue:]
- -[PTVFXRenderEffect initWithMetalContext:colorSize:colorConversion:prewarmOnly:humanDetections:asyncInitQueue:]
- -[PTVFXRenderEffect initWithMetalContext:colorSize:colorConversion:prewarmOnly:humanDetections:asyncInitQueue:].cold.1
- -[PTVFXRenderEffect initWithMetalContext:colorSize:colorConversion:prewarmOnly:humanDetections:asyncInitQueue:].cold.2
- -[PTVFXRenderEffect reactionTemplates]
- -[PTVFXRenderEffect setReactionTemplates:]
- -[PTVFXRenderEffect setupCommonVFXSceneLoadOptions:metalLibraryURL:commandQueue:]
- -[PTVFXRenderEffectBinding effect]
- -[PTVFXRenderEffectBinding setEffect:]
- -[SRLv2Plist readPlist:]
- -[SingleColorCubeCorrectionStage .cxx_destruct]
- -[SingleColorCubeCorrectionStage cubeTexture]
- -[SingleColorCubeCorrectionStage init:cubeSize:data:]
- -[SingleColorCubeCorrectionStage init:cubeSize:data:].cold.1
- -[SingleColorCubeCorrectionStage load3DTextureFromData:cubeSize:metal:outTexture:]
- -[SingleColorCubeCorrectionStage load3DTextureFromData:cubeSize:metal:outTexture:].cold.1
- OBJC_IVAR_$_SRLv2Plist.biasFactorSRLv2
- OBJC_IVAR_$_SRLv2Plist.faceExpDifThreshold
- OBJC_IVAR_$_SRLv2Plist.maskThreshold
- OBJC_IVAR_$_SRLv2Plist.maxBoost_I
- OBJC_IVAR_$_SRLv2Plist.maxBoost_II
- OBJC_IVAR_$_SRLv2Plist.maxBoost_III
- OBJC_IVAR_$_SRLv2Plist.maxBoost_IV
- OBJC_IVAR_$_SRLv2Plist.maxBoost_V
- OBJC_IVAR_$_SRLv2Plist.maxBoost_VI
- OBJC_IVAR_$_SRLv2Plist.maxCurveBoost
- OBJC_IVAR_$_SRLv2Plist.maxTargetRatioDarkening
- OBJC_IVAR_$_SRLv2Plist.maxTargetRatioLimit
- OBJC_IVAR_$_SRLv2Plist.minCurveBoost
- OBJC_IVAR_$_SRLv2Plist.minFaceSize
- OBJC_IVAR_$_SRLv2Plist.relightOnlyPersonMask
- OBJC_IVAR_$_SRLv2Plist.targetMedian_I
- OBJC_IVAR_$_SRLv2Plist.targetMedian_II
- OBJC_IVAR_$_SRLv2Plist.targetMedian_III
- OBJC_IVAR_$_SRLv2Plist.targetMedian_IV
- OBJC_IVAR_$_SRLv2Plist.targetMedian_V
- OBJC_IVAR_$_SRLv2Plist.targetMedian_VI
- OBJC_IVAR_$_SRLv2Plist.toneSimilaritySigma
- _CFDictionaryGetValueIfPresent
- _CFDictionaryRemoveValue
- _CFDictionarySetValue
- _CFGetTypeID
- _CFNumberGetTypeID
- _CFNumberGetValue
- _FigCFDictionaryGetInt32IfPresent
- _FigCFDictionaryGetInt32IfPresent.cold.1
- _FigCFDictionaryGetInt32IfPresent.cold.2
- _IOObjectRelease
- _IORegistryEntrySearchCFProperty
- _IOServiceGetMatchingService
- _IOServiceMatching
- _IOSurfaceAcceleratorCreate
- _IOSurfaceAcceleratorSetCustomFilter
- _IOSurfaceAcceleratorTransformSurface
- _NSSelectorFromString
- _OBJC_CLASS_$_LKTFlowGPU
- _OBJC_CLASS_$_MTLComputePipelineDescriptor
- _OBJC_CLASS_$_NSInvocation
- _OBJC_CLASS_$_PTEffectManagerDebug
- _OBJC_CLASS_$_PTRenderEffectContainer
- _OBJC_CLASS_$_PTRenderEffectInput
- _OBJC_CLASS_$_PTRenderEffectOutput
- _OBJC_CLASS_$_PTScreenCaptureComposite
- _OBJC_CLASS_$_SRLv2Plist
- _OBJC_CLASS_$_SingleColorCubeCorrectionStage
- _OBJC_CLASS_$_VFXSceneLoadOptions
- _OBJC_CLASS_$__TtC3VFX8VFXScene
- _OBJC_IVAR_$_LKTFlowGPU._Adiagb_buf
- _OBJC_IVAR_$_LKTFlowGPU._C0_tex
- _OBJC_IVAR_$_LKTFlowGPU._C1_tex
- _OBJC_IVAR_$_LKTFlowGPU._G0_tex
- _OBJC_IVAR_$_LKTFlowGPU._G1_tex
- _OBJC_IVAR_$_LKTFlowGPU._I_tex
- _OBJC_IVAR_$_LKTFlowGPU._I_u32_alias_tex
- _OBJC_IVAR_$_LKTFlowGPU._Ixy_buf
- _OBJC_IVAR_$_LKTFlowGPU._aux_pyr_size
- _OBJC_IVAR_$_LKTFlowGPU._aux_size
- _OBJC_IVAR_$_LKTFlowGPU._computePipelines
- _OBJC_IVAR_$_LKTFlowGPU._current_frame_index
- _OBJC_IVAR_$_LKTFlowGPU._idt_buf
- _OBJC_IVAR_$_LKTFlowGPU._indexUpdated
- _OBJC_IVAR_$_LKTFlowGPU._isBidirectional
- _OBJC_IVAR_$_LKTFlowGPU._isInverse
- _OBJC_IVAR_$_LKTFlowGPU._isValid
- _OBJC_IVAR_$_LKTFlowGPU._kpt_buf
- _OBJC_IVAR_$_LKTFlowGPU._maxThreadExecutionWidth
- _OBJC_IVAR_$_LKTFlowGPU._metalContext
- _OBJC_IVAR_$_LKTFlowGPU._needConversionBGRA2YUVA
- _OBJC_IVAR_$_LKTFlowGPU._nlreg_padding
- _OBJC_IVAR_$_LKTFlowGPU._nlreg_radius
- _OBJC_IVAR_$_LKTFlowGPU._nlreg_sigma_c
- _OBJC_IVAR_$_LKTFlowGPU._nlreg_sigma_l
- _OBJC_IVAR_$_LKTFlowGPU._nlreg_sigma_w
- _OBJC_IVAR_$_LKTFlowGPU._nscales
- _OBJC_IVAR_$_LKTFlowGPU._nwarpings
- _OBJC_IVAR_$_LKTFlowGPU._ref_pyr_size
- _OBJC_IVAR_$_LKTFlowGPU._ref_size
- _OBJC_IVAR_$_LKTFlowGPU._streamFrameCount
- _OBJC_IVAR_$_LKTFlowGPU._useNonLocalRegularization
- _OBJC_IVAR_$_LKTFlowGPU._uv_bwd_tex
- _OBJC_IVAR_$_LKTFlowGPU._uv_bwd_tex_user_ref
- _OBJC_IVAR_$_LKTFlowGPU._uv_bwd_u32_alias_tex
- _OBJC_IVAR_$_LKTFlowGPU._uv_fwd_tex
- _OBJC_IVAR_$_LKTFlowGPU._uv_fwd_tex_user_ref
- _OBJC_IVAR_$_LKTFlowGPU._uv_fwd_u32_alias_tex
- _OBJC_IVAR_$_LKTFlowGPU._w_tex
- _OBJC_IVAR_$_PTCVMNetwork._useHighResNetwork
- _OBJC_IVAR_$_PTEffect._faceAttributesNetwork
- _OBJC_IVAR_$_PTEffectManagerDebug._effectDepthDebug
- _OBJC_IVAR_$_PTEffectManagerDebug._util
- _OBJC_IVAR_$_PTEffectManagerDebug.depthNearFar
- _OBJC_IVAR_$_PTEffectManagerDebug.depthOutputPixelFormat
- _OBJC_IVAR_$_PTEffectManagerDebug.effectPriority
- _OBJC_IVAR_$_PTEffectManagerDebug.effectType
- _OBJC_IVAR_$_PTEffectManagerDebug.enabled
- _OBJC_IVAR_$_PTEffectManagerDebug.maxDepth
- _OBJC_IVAR_$_PTEffectManagerDebug.reverseZ
- _OBJC_IVAR_$_PTEffectManagerDebug.rgbaOutputPixelFormat
- _OBJC_IVAR_$_PTEffectRenderer._effectUtil
- _OBJC_IVAR_$_PTEffectRenderer._intermediateYUV
- _OBJC_IVAR_$_PTEffectRenderer._util
- _OBJC_IVAR_$_PTEffectUtil._copySingleChannel
- _OBJC_IVAR_$_PTHandGestureDetector._pixelTransferSession
- _OBJC_IVAR_$_PTMSRResize._accelRef
- _OBJC_IVAR_$_PTMSRResize._cap
- _OBJC_IVAR_$_PTMSRResize._supportsSymmetricScaling
- _OBJC_IVAR_$_PTPyramid._bicubic
- _OBJC_IVAR_$_PTPyramid._updateLevel0Box2x2FromRGBA
- _OBJC_IVAR_$_PTPyramid._updateLevel0Box2x2FromYUV
- _OBJC_IVAR_$_PTPyramid._updateLevel0Gaussian3x3FromRGBA
- _OBJC_IVAR_$_PTPyramid._updateLevel0Gaussian3x3FromYUV
- _OBJC_IVAR_$_PTPyramid._updateLevel0and1Gaussian3x3FromRGBA
- _OBJC_IVAR_$_PTPyramid._updateLevel0and1Gaussian3x3FromYUV
- _OBJC_IVAR_$_PTQualitySettings._disparityGuidedFilterEpsilon
- _OBJC_IVAR_$_PTRaytracingV2002._disparitySize
- _OBJC_IVAR_$_PTRaytracingV2002._disparitySizeUpscaled
- _OBJC_IVAR_$_PTRaytracingV2002._disparityUpscaled
- _OBJC_IVAR_$_PTRaytracingV3001._disparitySize
- _OBJC_IVAR_$_PTRaytracingV3001._disparitySizeUpscaled
- _OBJC_IVAR_$_PTRaytracingV3001._disparityUpscaled
- _OBJC_IVAR_$_PTRaytracingV3001._renderEffects
- _OBJC_IVAR_$_PTRaytracingV4001._disparitySize
- _OBJC_IVAR_$_PTRaytracingV4001._disparitySizeUpscaled
- _OBJC_IVAR_$_PTRenderEffectContainer._renderEffect
- _OBJC_IVAR_$_PTRenderEffectContainer._renderEffectInput
- _OBJC_IVAR_$_PTRenderEffectContainer._renderEffectOutput
- _OBJC_IVAR_$_PTRenderEffectInput.focusDistance
- _OBJC_IVAR_$_PTRenderEffectOutput._effectDepth
- _OBJC_IVAR_$_PTRenderEffectOutput._effectRGBA
- _OBJC_IVAR_$_PTRenderPipelineState._renderEffects
- _OBJC_IVAR_$_PTScreenCaptureComposite._floatingAlphaCutout
- _OBJC_IVAR_$_PTScreenCaptureComposite._matrixRGBtoYUV
- _OBJC_IVAR_$_PTScreenCaptureComposite._metalContext
- _OBJC_IVAR_$_PTVFXRenderEffect._camera
- _OBJC_IVAR_$_PTVFXRenderEffect._lightBinding
- _OBJC_IVAR_$_PTVFXRenderEffect._lighting
- _OBJC_IVAR_$_PTVFXRenderEffect._reactionTemplates
- _OBJC_IVAR_$_PTVFXRenderEffect._vfxRenderer
- _OBJC_IVAR_$_PTVFXRenderEffectBinding._effect
- _OBJC_IVAR_$_SingleColorCubeCorrectionStage._defaultCubeTexture
- _OBJC_METACLASS_$_LKTFlowGPU
- _OBJC_METACLASS_$_PTEffectManagerDebug
- _OBJC_METACLASS_$_PTRenderEffectContainer
- _OBJC_METACLASS_$_PTRenderEffectInput
- _OBJC_METACLASS_$_PTRenderEffectOutput
- _OBJC_METACLASS_$_PTScreenCaptureComposite
- _OBJC_METACLASS_$_SRLv2Plist
- _OBJC_METACLASS_$_SingleColorCubeCorrectionStage
- __OBJC_$_CLASS_METHODS_LKTFlowGPU
- __OBJC_$_INSTANCE_METHODS_LKTFlowGPU
- __OBJC_$_INSTANCE_METHODS_PTEffectManagerDebug
- __OBJC_$_INSTANCE_METHODS_PTRenderEffectContainer
- __OBJC_$_INSTANCE_METHODS_PTRenderEffectInput
- __OBJC_$_INSTANCE_METHODS_PTRenderEffectOutput
- __OBJC_$_INSTANCE_METHODS_PTScreenCaptureComposite
- __OBJC_$_INSTANCE_METHODS_SRLv2Plist
- __OBJC_$_INSTANCE_METHODS_SingleColorCubeCorrectionStage
- __OBJC_$_INSTANCE_VARIABLES_LKTFlowGPU
- __OBJC_$_INSTANCE_VARIABLES_PTEffectManagerDebug
- __OBJC_$_INSTANCE_VARIABLES_PTRenderEffectContainer
- __OBJC_$_INSTANCE_VARIABLES_PTRenderEffectInput
- __OBJC_$_INSTANCE_VARIABLES_PTRenderEffectOutput
- __OBJC_$_INSTANCE_VARIABLES_PTScreenCaptureComposite
- __OBJC_$_INSTANCE_VARIABLES_SRLv2Plist
- __OBJC_$_INSTANCE_VARIABLES_SingleColorCubeCorrectionStage
- __OBJC_$_PROP_LIST_LKTFlowGPU
- __OBJC_$_PROP_LIST_PTEffectManagerDebug
- __OBJC_$_PROP_LIST_PTRenderEffect
- __OBJC_$_PROP_LIST_PTRenderEffectContainer
- __OBJC_$_PROP_LIST_PTRenderEffectInput
- __OBJC_$_PROP_LIST_PTRenderEffectOutput
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PTRenderEffect
- __OBJC_$_PROTOCOL_METHOD_TYPES_PTRenderEffect
- __OBJC_$_PROTOCOL_REFS_PTRenderEffect
- __OBJC_CLASS_PROTOCOLS_$_PTEffectManagerDebug
- __OBJC_CLASS_RO_$_LKTFlowGPU
- __OBJC_CLASS_RO_$_PTEffectManagerDebug
- __OBJC_CLASS_RO_$_PTRenderEffectContainer
- __OBJC_CLASS_RO_$_PTRenderEffectInput
- __OBJC_CLASS_RO_$_PTRenderEffectOutput
- __OBJC_CLASS_RO_$_PTScreenCaptureComposite
- __OBJC_CLASS_RO_$_SRLv2Plist
- __OBJC_CLASS_RO_$_SingleColorCubeCorrectionStage
- __OBJC_LABEL_PROTOCOL_$_PTRenderEffect
- __OBJC_METACLASS_RO_$_LKTFlowGPU
- __OBJC_METACLASS_RO_$_PTEffectManagerDebug
- __OBJC_METACLASS_RO_$_PTRenderEffectContainer
- __OBJC_METACLASS_RO_$_PTRenderEffectInput
- __OBJC_METACLASS_RO_$_PTRenderEffectOutput
- __OBJC_METACLASS_RO_$_PTScreenCaptureComposite
- __OBJC_METACLASS_RO_$_SRLv2Plist
- __OBJC_METACLASS_RO_$_SingleColorCubeCorrectionStage
- __OBJC_PROTOCOL_$_PTRenderEffect
- __Z34ParticleInit_rain_particleInit_149PKvjS0_jRDv4_fRfRDv2_f
- __Z34ParticleInit_rain_particleInit_161PKvjDv2_fjRDv3_f
- __Z34ParticleInit_rain_particleInit_167PKvjDv3_fDv2_fRDv4_fRS1_
- __Z35ParticleInit_hearts_particleInit_17PKvjRDv2_f
- __Z35ParticleInit_hearts_particleInit_28PKvjDv3_fjRS1_S2_
- __Z35ParticleInit_lasers_particleInit_26PKvjjRDv3_fRDv4_fRf
- __Z35ParticleInit_lasers_particleInit_27PKvjDv3_fjRS1_S2_
- __Z35ParticleInit_lasers_particleInit_28PKvjDv3_fjRS1_S2_
- __Z35ParticleInit_lasers_particleInit_58PKvjjRDv3_fRDv4_fRf
- __Z36ParticleInit_balloons_particleInit_9PKvjDv2_fjmRDv3_fRDv4_fS5_
- __Z36ParticleInit_hearts_particleInit_127PKvjDv3_fjjbS1_fS0_RS1_S2_RDv4_f
- __Z36ParticleInit_hearts_particleInit_130PKvjS0_RDv3_fRDv4_fS4_S2_
- __Z36ParticleInit_lasers_particleInit_117PKvjDv3_fjRS1_S2_
- __Z36ParticleInit_lasers_particleInit_141PKvjRDv2_f
- __Z37ParticleInit_balloons_particleInit_40PKvjDv3_fDv2_fjRS1_RDv4_fS3_
- __Z37ParticleInit_balloons_particleInit_51PKvjRDv2_f
- __Z37ParticleInit_balloons_particleInit_58PKvjDv2_fRS1_
- __Z37ParticleInit_confetti_particleInit_29PKvjRDv2_f
- __Z37ParticleInit_fireworks_particleInit_8PKvjDv4_fRS1_
- __Z37ParticleInit_thumbsup_particleInit_13PKvjDv3_fbmRDv4_fRS1_RfS3_S3_
- __Z37ParticleInit_thumbsup_particleInit_78PKvjbjbDv3_fmRDv4_fRS1_S4_
- __Z37ParticleUpdate_rain_particleUpdate_36PKvjDv3_fS1_S1_S0_ffRDv4_fRS1_S3_
- __Z37ParticleUpdate_rain_particleUpdate_95PKvjDv4_fS0_fffRS1_
- __Z38ParticleInit_balloons_particleInit_140PKvjDv2_fjDv3_fRS2_RDv4_fS3_S5_
- __Z38ParticleInit_confetti_particleInit_113PKvjffbjS0_jS0_RDv3_fRDv4_fS4_
- __Z38ParticleInit_confetti_particleInit_146PKvjffjjS0_jS0_RDv3_fRDv4_fS4_S4_
- __Z38ParticleInit_confetti_particleInit_172PKvjffjS0_jS0_RDv3_fRDv4_fS4_S4_
- __Z38ParticleInit_fireworks_particleInit_14PKvjDv3_fjDv4_fS0_RS1_RS2_
- __Z38ParticleInit_fireworks_particleInit_54PKvjS0_Dv4_fjRS1_
- __Z38ParticleInit_fireworks_particleInit_86PKvjjRDv4_f
- __Z38ParticleInit_thumbsup_particleInit_142PKvjDv3_fbmRDv4_fRS1_RfS3_S3_
- __Z38ParticleUpdate_rain_particleUpdate_122PKvjS0_ffRDv4_f
- __Z38ParticleUpdate_rain_particleUpdate_194PKvjDv2_fjRDv3_fRDv4_f
- __Z39ParticleInit_fireworks_particleInit_118PKvjmjfS0_RDv4_fS2_Rf
- __Z39ParticleInit_fireworks_particleInit_140PKvjRDv4_f
- __Z39ParticleInit_fireworks_particleInit_169PKvjDv4_fRS1_
- __Z39ParticleInit_fireworks_particleInit_182PKvjDv3_fjRS1_S2_
- __Z39ParticleInit_fireworks_particleInit_189PKvjRDv2_f
- __Z39ParticleInit_fireworks_particleInit_217PKvjmjfRDv4_fS2_RDv3_f
- __Z39ParticleInit_fireworks_particleInit_219PKvjjRDv4_f
- __Z39ParticleInit_fireworks_particleInit_235PKvjDv3_fS1_jS0_Dv4_fRS1_RS2_
- __Z39ParticleInit_fireworks_particleInit_264PKvjmjfS0_RDv4_fS2_Rf
- __Z39ParticleUpdate_hearts_particleUpdate_59PKvjDv4_ffRS1_
- __Z39ParticleUpdate_hearts_particleUpdate_95PKvjS0_ffRDv4_f
- __Z39ParticleUpdate_lasers_particleUpdate_18PKvjDv4_fS0_fS1_RS1_
- __Z39ParticleUpdate_lasers_particleUpdate_71PKvjDv4_fS0_fS1_RS1_
- __Z39ParticleUpdate_lasers_particleUpdate_83PKvjS0_ffS0_fjRDv4_fR10simd_quatf
- __Z39ParticleUpdate_lasers_particleUpdate_84PKvjS0_ffRDv4_f
- __Z40ParticleUpdate_hearts_particleUpdate_210PKvjjfDv4_ffDv3_fS0_bjR10simd_quatfRS1_RS2_
- __Z40ParticleUpdate_lasers_particleUpdate_114PKvjS0_fffRDv4_f
- __Z40ParticleUpdate_lasers_particleUpdate_119PKvjS0_ffS0_fRDv4_f
- __Z40ParticleUpdate_thumbsup_particleUpdate_6PKvjS0_fDv3_fS0_ffbfS0_S0_S0_S0_S0_RS1_RfRDv4_f
- __Z40particle_update_lasers_particleUpdate_21PKvRDv4_fS0_
- __Z41ParticleUpdate_balloons_particleUpdate_36PKvjDv2_fRS1_
- __Z41ParticleUpdate_balloons_particleUpdate_81PKvjDv3_fS0_fS0_fS1_RDv4_fRS1_R10simd_quatf
- __Z41ParticleUpdate_balloons_particleUpdate_89PKvjS0_fRDv4_fRDv3_fS2_
- __Z41ParticleUpdate_confetti_particleUpdate_25PKvjjDv3_fS0_fR10simd_quatfRDv4_f
- __Z41ParticleUpdate_thumbsup_particleUpdate_34PKvjDv4_fS1_ffS0_S1_S0_RDv3_fRf
- __Z41ParticleUpdate_thumbsup_particleUpdate_76PKvjDv4_fS1_ffS0_fjS1_S0_fRDv3_fRf
- __Z41particle_update_hearts_particleUpdate_100PKvRDv3_fRjRfS4_S0_
- __Z42ParticleUpdate_balloons_particleUpdate_121PKvjDv3_fS0_fS0_fS1_RDv4_fRS1_R10simd_quatf
- __Z42ParticleUpdate_confetti_particleUpdate_124PKvjjR10simd_quatf
- __Z42ParticleUpdate_confetti_particleUpdate_196PKvjjDv3_fS0_fR10simd_quatfRDv4_f
- __Z42ParticleUpdate_fireworks_particleUpdate_22PKvjDv4_fS0_ffRS1_
- __Z42ParticleUpdate_fireworks_particleUpdate_39PKvjS0_ffRDv4_f
- __Z42ParticleUpdate_fireworks_particleUpdate_52PKvjDv4_fS0_ffRS1_
- __Z42ParticleUpdate_fireworks_particleUpdate_73PKvjDv4_ffS1_fS0_fRfS2_RS1_RDv3_f
- __Z43ParticleUpdate_fireworks_particleUpdate_142PKvjDv4_fjS0_ffRS1_
- __Z43ParticleUpdate_fireworks_particleUpdate_143PKvjDv4_ffS1_fS0_fRfS2_RS1_RDv3_f
- __Z43ParticleUpdate_fireworks_particleUpdate_223PKvjDv4_fS0_ffRS1_
- __Z43ParticleUpdate_fireworks_particleUpdate_257PKvjDv4_fS0_fjS0_fRS1_
- __Z43ParticleUpdate_fireworks_particleUpdate_273PKvjDv4_fS0_ffRS1_
- __Z43ParticleUpdate_fireworks_particleUpdate_322PKvjDv4_fS0_ffRS1_
- __Z43particle_update_fireworks_particleUpdate_85PKvRfRDv4_fS3_S0_
- __Z44particle_update_fireworks_particleUpdate_238PKvRfRDv4_fS0_
- __Z52Main_rain_graph_2AEE11A5_5806_4949_9017_97A31959A146PKvjRf
- __Z52Main_rain_graph_47225A01_2C47_433D_93D9_BF1D85A3839FPKvjDv3_fDv2_fRS1_
- __Z52Main_rain_graph_72169E6B_0B70_473E_B19D_953F01AC5993PKvjfRf
- __Z52Main_rain_graph_B55CB68B_5374_45B9_9B3B_050825454545PKvjRf
- __Z52Main_rain_graph_C718F1B2_4BA3_4E66_8269_7C49E171E2ECPKvjDv3_fRS1_S2_S2_
- __Z52Main_rain_graph_D83B875F_FB36_42AC_BCF5_9AD248F8E2ABPKvjDv3_fRS1_S2_S2_
- __Z52Main_rain_graph_EDF6BEEC_34C4_489E_ABEC_1C4A62E25E40PKvjDv3_fRS1_
- __Z53Spawn_rain_graph_25FC010E_3796_4569_84C9_8E9B3FC08F4BPKvjfRf
- __Z53Spawn_rain_graph_43A66462_6D38_40C4_9563_E3E4B018C43APKvjfS0_fRf
- __Z53Spawn_rain_graph_999F57E4_3BBD_4410_9780_400191D6A26BPKvjfS0_fRf
- __Z53Spawn_rain_graph_FA88FCF0_73CA_480E_A020_897384F93F5CPKvjfRf
- __Z54Init_hearts_graph_77839324_3A35_4199_A55E_F65CEF5F32BFPKvjbR15vfx_float_rangeRDv3_f
- __Z54Init_hearts_graph_B8CFD00B_F83D_48B4_B9F3_B556F2C755C4PKvjR15vfx_float_range
- __Z54Main_hearts_graph_06A14A47_3880_4300_8226_188BD75B83F1PKvjfRf
- __Z54Main_hearts_graph_3E785FDE_1E85_40AA_A8D6_985C11FFF991PKvjRb
- __Z54Main_hearts_graph_4267197A_7D75_425E_8F36_26328B281570PKvj10simd_quatffRDv3_fS3_Rf
- __Z54Main_hearts_graph_4E082B7E_A3DB_40F5_9D67_FBFC9824FD2DPKvjfRf
- __Z54Main_hearts_graph_6501AA18_D88F_4677_984C_34E780A7C1F0PKvjRDv3_f
- __Z54Main_hearts_graph_6CDCF767_47EA_4180_9CAC_F5ACFF8AE4CFPKvjDv3_fRS1_
- __Z54Main_hearts_graph_781609DE_FEF0_4B99_B009_050ADBDF1B32PKvjDv3_ffbRS1_Rf
- __Z54Main_hearts_graph_D45D06FA_D64A_4215_983D_70FBC27B23B0PKvjfRf
- __Z54Main_lasers_graph_1415613D_8457_4B24_9F2B_BDCEA47A7E46PKvjRf
- __Z54Main_lasers_graph_31BFE03A_347F_4F4B_8062_57C3C496211BPKvjRDv3_fRf
- __Z54Main_lasers_graph_3AFCB8D6_52EB_4CCA_8CDC_E3DC4941B357PKvjRf
- __Z54Main_lasers_graph_598E1865_A878_4D27_8744_3FC0B2A676F9PKvjfRf
- __Z54Main_lasers_graph_5BEEC0A4_8351_4E81_B071_E7FCF2740A98PKvjDv3_fRS1_
- __Z54Main_lasers_graph_75AE1D4B_87B4_4422_8E85_FE9D23E01F3BPKvjRDv3_fS2_S2_
- __Z54Main_lasers_graph_C0E70AB3_A28A_4D4F_8BEB_9516B357779CPKvjRb
- __Z54Main_lasers_graph_CD99FC2C_17B7_466E_930E_F05728CE31E3PKvjfRf
- __Z55Spawn_hearts_graph_27B2C751_CFE3_4369_B337_BEA7A4125BA6PKvjbR13vfx_int_range
- __Z55Spawn_hearts_graph_B0667801_C60E_4D93_B9A1_27F790726520PKvjfbRf
- __Z55Spawn_lasers_graph_84E516C9_0301_4F69_B83A_25056C254AE8PKvjbR13vfx_int_range
- __Z56Init_balloons_graph_0C92C45F_EBE3_4B04_B05E_4634866C142EPKvjfDv2_fRDv3_fS3_
- __Z56Init_balloons_graph_C007B07C_DCA2_428B_9117_ECF37793469APKvjfDv2_fRDv3_fS3_
- __Z56Init_confetti_graph_586EC683_ECAC_48E9_B645_74C36BE0B254PKvjjR15vfx_float_range
- __Z56Init_confetti_graph_77839324_3A35_4199_A55E_F65CEF5F32BFPKvjjR15vfx_float_range
- __Z56Init_thumbsup_graph_31C4109F_11CA_46CC_B9D5_22B60B283208PKvjRDv3_fS2_
- __Z56Init_thumbsup_graph_5BEF5B4C_59E5_4DBA_86B0_DB00779F419DPKvjRDv3_fS2_
- __Z56Init_thumbsup_graph_E58E02C9_8189_4980_ABED_6DF4C8EF7375PKvjbR15vfx_float_rangeRDv3_f
- __Z56Main_balloons_graph_002BE311_BD95_45E8_95C2_2D34D7AFF9B4PKvjDv2_fRfS2_
- __Z56Main_balloons_graph_30F6F52E_9FD9_4037_93CA_CCE724034EB4PKvjRb
- __Z56Main_balloons_graph_598E1865_A878_4D27_8744_3FC0B2A676F9PKvjfRf
- __Z56Main_balloons_graph_5CC22647_AE13_4002_961E_197A930CB43APKvjRm
- __Z56Main_balloons_graph_B84097E5_E449_4B6D_91CB_A59BE625458APKvjRDv3_f
- __Z56Main_balloons_graph_CD99FC2C_17B7_466E_930E_F05728CE31E3PKvjfRf
- __Z56Main_confetti_graph_06A14A47_3880_4300_8226_188BD75B83F1PKvjfRf
- __Z56Main_confetti_graph_47AC3C7A_C039_41DA_AD43_881D7E0F565APKvjDv3_fffRS1_
- __Z56Main_confetti_graph_47C93548_02F8_4EF6_928F_74CE4F39BBDEPKvjDv4_fRDv3_f
- __Z56Main_confetti_graph_5ECD10AA_AB39_44AA_809D_DE6EF1C771A6PKvjDv4_fRDv3_f
- __Z56Main_confetti_graph_6501AA18_D88F_4677_984C_34E780A7C1F0PKvjRDv3_f
- __Z56Main_confetti_graph_9855979D_D680_4AC7_999F_4BD84B083C71PKvjRb
- __Z56Main_confetti_graph_C7F30F02_BA8A_4DBA_8AB9_BEAFDE59A291PKvjDv3_fffRS1_
- __Z56Main_confetti_graph_D45D06FA_D64A_4215_983D_70FBC27B23B0PKvjfRf
- __Z56Main_lighting_graph_2A1A65D6_42D2_422D_B043_7BA6751C7A80PKvjfRf
- __Z56Main_lighting_graph_9DD82DB1_83CC_4C95_8122_529530C0E9A5PKvjfRf
- __Z56Main_lighting_graph_B9299884_EF40_4793_BAD0_BB82A60C4C1EPKvjfRf
- __Z56Main_thumbsup_graph_38F35C26_FEA0_47AB_B998_9FF24156FD6DPKvjiRj
- __Z56Main_thumbsup_graph_451D2F34_D7DE_4C4D_9A5C_B1A778F1CA1CPKvjbiRDv3_fRj
- __Z56Main_thumbsup_graph_8D318DBD_EF7B_44D4_B5E6_F743F93F2B64PKvjRf
- __Z56Main_thumbsup_graph_8EC5E521_8C63_47F8_B96D_2B0B5A296B7APKvjRf
- __Z56Main_thumbsup_graph_A591C9B7_84C4_4BEA_8829_4366B5881232PKvjbbRfS1_
- __Z56Main_thumbsup_graph_B59F1B79_7E62_4E5A_99DF_F365094C2D38PKvjiRj
- __Z57Init_fireworks_graph_3C6ED067_7943_49AD_A0AE_15130042E793PKvjR15vfx_float_rangeRDv3_f
- __Z57Init_fireworks_graph_402F3097_0BA4_4A83_9FEB_E7261701F766PKvjR15vfx_float_rangeRDv3_f
- __Z57Init_fireworks_graph_4F52B7E1_CA7E_4C70_B2C9_199EA88DF652PKvjR15vfx_float_rangeRDv3_f
- __Z57Init_fireworks_graph_514A5D4A_9A37_436A_B056_B2F8227D2BE1PKvjR15vfx_float_range
- __Z57Init_fireworks_graph_5AC753AC_F888_4AEE_B41F_BA9FA15941CCPKvjR15vfx_float_rangeS2_RDv3_f
- __Z57Init_fireworks_graph_5C6FE0C4_5B31_468F_9708_94003733DEC5PKvjR15vfx_float_rangeRDv3_f
- __Z57Init_fireworks_graph_647D8C58_3A96_4185_83BF_F834C05973E6PKvjDv4_fR15vfx_float_rangeRDv3_fRS1_
- __Z57Init_fireworks_graph_913AA320_A3AD_4B97_B3CE_288034B4B02BPKvjR15vfx_float_range
- __Z57Init_fireworks_graph_9C215676_B35D_4738_8604_1B0696C120C9PKvjR15vfx_float_range
- __Z57Init_fireworks_graph_9F0A8F07_3A67_4589_A511_28A794F02526PKvjR15vfx_float_rangeRDv3_f
- __Z57Init_fireworks_graph_A5860394_860A_466B_9036_4241BA694F84PKvjR15vfx_float_rangeRDv3_f
- __Z57Init_fireworks_graph_BE082C18_F014_49F4_AE91_49F0A20CA327PKvjR15vfx_float_rangeRDv3_f
- __Z57Init_fireworks_graph_FB239A73_A49B_49A1_B28F_F8EB686AE087PKvjR15vfx_float_rangeS2_RDv3_f
- __Z57Main_fireworks_graph_10EDDCB9_24C0_4755_971D_D6EC1FAF1000PKvjDv4_fRS1_
- __Z57Main_fireworks_graph_155128CD_E118_4113_8D6F_8B7F5BA2555DPKvjfRf
- __Z57Main_fireworks_graph_4AD865B9_2CA1_4C82_AA72_EC49942DA9DEPKvjfRf
- __Z57Main_fireworks_graph_4E8B4DDD_D3C2_4DDF_ACF2_2ECC08723FDBPKvjRm
- __Z57Main_fireworks_graph_5AFE93DC_23D2_46C1_93C9_29F6F7292984PKvjfRf
- __Z57Main_fireworks_graph_5DD07B06_8DCA_42DA_80D9_81BBED0FBF33PKvjfRf
- __Z57Main_fireworks_graph_72691A8E_EB30_4566_BC51_64DA827A694APKvjRb
- __Z57Main_fireworks_graph_A51B6B76_047A_469C_B965_C43FB2E4CAC7PKvjDv4_fRDv3_fS3_
- __Z57Main_fireworks_graph_DB777B14_A366_4CC8_8010_6DFA3030539EPKvjfRf
- __Z57Spawn_balloons_graph_8F8209A1_99A0_4036_A138_3AB3E67064C6PKvjfbmR13vfx_int_range
- __Z57Spawn_balloons_graph_F1142E3A_E67C_40DC_BC13_10D44D3F90F7PKvjfbmR13vfx_int_range
- __Z57Spawn_confetti_graph_16E7F806_2D73_4A39_B82C_90F26336105APKvjfffbbR13vfx_int_rangeS2_
- __Z57Spawn_confetti_graph_A9645361_1E28_4A66_8CE1_0FBB358E68C4PKvjfffbbR13vfx_int_rangeS2_
- __Z57Spawn_confetti_graph_B0667801_C60E_4D93_B9A1_27F790726520PKvjfffbbR13vfx_int_rangeS2_
- __Z58Render_thumbsup_graph_0E7F5D5F_BCDE_46CD_975C_9DB38EBC84DEPKvjRDv3_f
- __Z58Render_thumbsup_graph_891A5752_872E_4295_B8CA_3104EA0A6053PKvjRDv3_f
- __Z58Spawn_fireworks_graph_1E09F83D_74E8_4C33_AF7B_D1F4C7561C24PKvjfR13vfx_int_range
- __Z58Spawn_fireworks_graph_1F546ADD_0390_45D8_A31D_6FD1CEDB0057PKvjfRf
- __Z58Spawn_fireworks_graph_224CDDEA_614F_4333_A343_6F25B6068E45PKvjS0_ffRf
- __Z58Spawn_fireworks_graph_32BE36EE_4AAF_45ED_8B70_F204A610CBF9PKvjfRf
- __Z58Spawn_fireworks_graph_4F9764F9_0AFB_41B2_A2E5_90D5BEA2660FPKvjfRf
- __Z58Spawn_fireworks_graph_68ABBDD2_799D_4316_B610_A615A6E5C6C0PKvjfRf
- __Z58Spawn_fireworks_graph_70391988_6235_4105_AB03_8B09A79D6EF6PKvjfR13vfx_int_range
- __Z58Spawn_fireworks_graph_C96088C0_AF79_4824_9185_0DFF8E90BFB3PKvjfR13vfx_int_range
- __Z58Spawn_fireworks_graph_C9C0CC36_AD87_4391_B404_40CBC37682DCPKvjfR13vfx_int_range
- __Z58Spawn_fireworks_graph_CC976411_EC12_4A2C_A577_DD5F08309A69PKvjS0_ffRf
- __Z58Spawn_fireworks_graph_CECA8E5C_A7BB_4D57_BBA3_E684CB761DA9PKvjfRf
- __Z58Spawn_fireworks_graph_E9D5C3AC_14D8_4C9E_A340_8873556A15ACPKvjfRf
- __Z58Spawn_fireworks_graph_EA69B710_0EB0_430A_84ED_99FDFB897003PKvjbR13vfx_int_range
- __Z58Spawn_fireworks_graph_EF83050E_3420_4C5E_B29A_63DE74130B60PKvjfRf
- __Z59Render_fireworks_graph_07D62C9C_6FAA_4BD9_910F_CDEA5CFCCC06PKvjfRf
- __ZL14simd_matrix3x310simd_quatf
- __ZZ27__vfx_get_script_table_rainE11scriptTable
- __ZZ29__vfx_get_script_table_heartsE11scriptTable
- __ZZ29__vfx_get_script_table_lasersE11scriptTable
- __ZZ31__vfx_get_script_table_balloonsE11scriptTable
- __ZZ31__vfx_get_script_table_confettiE11scriptTable
- __ZZ31__vfx_get_script_table_lightingE11scriptTable
- __ZZ31__vfx_get_script_table_thumbsupE11scriptTable
- __ZZ32__vfx_get_script_table_fireworksE11scriptTable
- ___116-[PTSyntheticLight estimateLightIntensityWithFaceRects:inTex:numberOfFaceRects:transform:humanDetections:asyncWork:]_block_invoke
- ___126-[PTHandGestureDetector detectGesturesFromBuffer:timeStamp:withRotationDegrees:withDetectedHands:withDetectedFaces:asyncWork:]_block_invoke.136
- ___157-[PTEffectRenderer initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:]_block_invoke
- ___19-[PTEffect render:]_block_invoke.247
- ___24-[PTEffect reconfigure:]_block_invoke
- ___24-[PTEffect reconfigure:]_block_invoke_2
- ___33-[PTVFXRenderEffect asyncVFXInit]_block_invoke
- ___44-[PTVFXRenderEffect initVFX:asyncInitQueue:]_block_invoke
- ___59-[PTEffectRenderer render:waitUntilCompleted:gpuCompleted:]_block_invoke.109
- ___59-[PTEffectRenderer render:waitUntilCompleted:gpuCompleted:]_block_invoke.cold.1
- ___block_descriptor_120_e8_32s40s48r56w_e5_v8?0lw56l8s32l8r48l8s40l8
- ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
- ___block_descriptor_48_e8_32s40w_e28_v16?0"<MTLCommandBuffer>"8lw40l8s32l8
- ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_52_e8_32s40s_e28_v16?0"<MTLCommandBuffer>"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48w_e28_v16?0"<MTLCommandBuffer>"8lw48l8s32l8s40l8
- ___block_descriptor_56_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_68_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_84_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_literal_global.238
- ___block_literal_global.251
- ___vfx_get_script_table_balloons
- ___vfx_get_script_table_confetti
- ___vfx_get_script_table_fireworks
- ___vfx_get_script_table_hearts
- ___vfx_get_script_table_lasers
- ___vfx_get_script_table_lighting
- ___vfx_get_script_table_rain
- ___vfx_get_script_table_thumbsup
- ___vfx_script_balloons_graph_002BE311_BD95_45E8_95C2_2D34D7AFF9B4
- ___vfx_script_balloons_graph_0C92C45F_EBE3_4B04_B05E_4634866C142E
- ___vfx_script_balloons_graph_30F6F52E_9FD9_4037_93CA_CCE724034EB4
- ___vfx_script_balloons_graph_598E1865_A878_4D27_8744_3FC0B2A676F9
- ___vfx_script_balloons_graph_5CC22647_AE13_4002_961E_197A930CB43A
- ___vfx_script_balloons_graph_8F8209A1_99A0_4036_A138_3AB3E67064C6
- ___vfx_script_balloons_graph_B84097E5_E449_4B6D_91CB_A59BE625458A
- ___vfx_script_balloons_graph_C007B07C_DCA2_428B_9117_ECF37793469A
- ___vfx_script_balloons_graph_CD99FC2C_17B7_466E_930E_F05728CE31E3
- ___vfx_script_balloons_graph_F1142E3A_E67C_40DC_BC13_10D44D3F90F7
- ___vfx_script_balloons_particleInit_140
- ___vfx_script_balloons_particleInit_40
- ___vfx_script_balloons_particleInit_51
- ___vfx_script_balloons_particleInit_58
- ___vfx_script_balloons_particleInit_9
- ___vfx_script_balloons_particleUpdate_121
- ___vfx_script_balloons_particleUpdate_36
- ___vfx_script_balloons_particleUpdate_81
- ___vfx_script_balloons_particleUpdate_89
- ___vfx_script_confetti_graph_06A14A47_3880_4300_8226_188BD75B83F1
- ___vfx_script_confetti_graph_16E7F806_2D73_4A39_B82C_90F26336105A
- ___vfx_script_confetti_graph_47AC3C7A_C039_41DA_AD43_881D7E0F565A
- ___vfx_script_confetti_graph_47C93548_02F8_4EF6_928F_74CE4F39BBDE
- ___vfx_script_confetti_graph_586EC683_ECAC_48E9_B645_74C36BE0B254
- ___vfx_script_confetti_graph_5ECD10AA_AB39_44AA_809D_DE6EF1C771A6
- ___vfx_script_confetti_graph_6501AA18_D88F_4677_984C_34E780A7C1F0
- ___vfx_script_confetti_graph_77839324_3A35_4199_A55E_F65CEF5F32BF
- ___vfx_script_confetti_graph_9855979D_D680_4AC7_999F_4BD84B083C71
- ___vfx_script_confetti_graph_A9645361_1E28_4A66_8CE1_0FBB358E68C4
- ___vfx_script_confetti_graph_B0667801_C60E_4D93_B9A1_27F790726520
- ___vfx_script_confetti_graph_C7F30F02_BA8A_4DBA_8AB9_BEAFDE59A291
- ___vfx_script_confetti_graph_D45D06FA_D64A_4215_983D_70FBC27B23B0
- ___vfx_script_confetti_particleInit_113
- ___vfx_script_confetti_particleInit_146
- ___vfx_script_confetti_particleInit_172
- ___vfx_script_confetti_particleInit_29
- ___vfx_script_confetti_particleUpdate_124
- ___vfx_script_confetti_particleUpdate_196
- ___vfx_script_confetti_particleUpdate_25
- ___vfx_script_fireworks_graph_07D62C9C_6FAA_4BD9_910F_CDEA5CFCCC06
- ___vfx_script_fireworks_graph_10EDDCB9_24C0_4755_971D_D6EC1FAF1000
- ___vfx_script_fireworks_graph_155128CD_E118_4113_8D6F_8B7F5BA2555D
- ___vfx_script_fireworks_graph_1E09F83D_74E8_4C33_AF7B_D1F4C7561C24
- ___vfx_script_fireworks_graph_1F546ADD_0390_45D8_A31D_6FD1CEDB0057
- ___vfx_script_fireworks_graph_224CDDEA_614F_4333_A343_6F25B6068E45
- ___vfx_script_fireworks_graph_32BE36EE_4AAF_45ED_8B70_F204A610CBF9
- ___vfx_script_fireworks_graph_3C6ED067_7943_49AD_A0AE_15130042E793
- ___vfx_script_fireworks_graph_402F3097_0BA4_4A83_9FEB_E7261701F766
- ___vfx_script_fireworks_graph_4AD865B9_2CA1_4C82_AA72_EC49942DA9DE
- ___vfx_script_fireworks_graph_4E8B4DDD_D3C2_4DDF_ACF2_2ECC08723FDB
- ___vfx_script_fireworks_graph_4F52B7E1_CA7E_4C70_B2C9_199EA88DF652
- ___vfx_script_fireworks_graph_4F9764F9_0AFB_41B2_A2E5_90D5BEA2660F
- ___vfx_script_fireworks_graph_514A5D4A_9A37_436A_B056_B2F8227D2BE1
- ___vfx_script_fireworks_graph_5AC753AC_F888_4AEE_B41F_BA9FA15941CC
- ___vfx_script_fireworks_graph_5AFE93DC_23D2_46C1_93C9_29F6F7292984
- ___vfx_script_fireworks_graph_5C6FE0C4_5B31_468F_9708_94003733DEC5
- ___vfx_script_fireworks_graph_5DD07B06_8DCA_42DA_80D9_81BBED0FBF33
- ___vfx_script_fireworks_graph_647D8C58_3A96_4185_83BF_F834C05973E6
- ___vfx_script_fireworks_graph_68ABBDD2_799D_4316_B610_A615A6E5C6C0
- ___vfx_script_fireworks_graph_70391988_6235_4105_AB03_8B09A79D6EF6
- ___vfx_script_fireworks_graph_72691A8E_EB30_4566_BC51_64DA827A694A
- ___vfx_script_fireworks_graph_913AA320_A3AD_4B97_B3CE_288034B4B02B
- ___vfx_script_fireworks_graph_9C215676_B35D_4738_8604_1B0696C120C9
- ___vfx_script_fireworks_graph_9F0A8F07_3A67_4589_A511_28A794F02526
- ___vfx_script_fireworks_graph_A51B6B76_047A_469C_B965_C43FB2E4CAC7
- ___vfx_script_fireworks_graph_A5860394_860A_466B_9036_4241BA694F84
- ___vfx_script_fireworks_graph_BE082C18_F014_49F4_AE91_49F0A20CA327
- ___vfx_script_fireworks_graph_C96088C0_AF79_4824_9185_0DFF8E90BFB3
- ___vfx_script_fireworks_graph_C9C0CC36_AD87_4391_B404_40CBC37682DC
- ___vfx_script_fireworks_graph_CC976411_EC12_4A2C_A577_DD5F08309A69
- ___vfx_script_fireworks_graph_CECA8E5C_A7BB_4D57_BBA3_E684CB761DA9
- ___vfx_script_fireworks_graph_DB777B14_A366_4CC8_8010_6DFA3030539E
- ___vfx_script_fireworks_graph_E9D5C3AC_14D8_4C9E_A340_8873556A15AC
- ___vfx_script_fireworks_graph_EA69B710_0EB0_430A_84ED_99FDFB897003
- ___vfx_script_fireworks_graph_EF83050E_3420_4C5E_B29A_63DE74130B60
- ___vfx_script_fireworks_graph_FB239A73_A49B_49A1_B28F_F8EB686AE087
- ___vfx_script_fireworks_particleInit_118
- ___vfx_script_fireworks_particleInit_14
- ___vfx_script_fireworks_particleInit_140
- ___vfx_script_fireworks_particleInit_169
- ___vfx_script_fireworks_particleInit_182
- ___vfx_script_fireworks_particleInit_189
- ___vfx_script_fireworks_particleInit_217
- ___vfx_script_fireworks_particleInit_219
- ___vfx_script_fireworks_particleInit_235
- ___vfx_script_fireworks_particleInit_264
- ___vfx_script_fireworks_particleInit_54
- ___vfx_script_fireworks_particleInit_8
- ___vfx_script_fireworks_particleInit_86
- ___vfx_script_fireworks_particleUpdate_142
- ___vfx_script_fireworks_particleUpdate_143
- ___vfx_script_fireworks_particleUpdate_22
- ___vfx_script_fireworks_particleUpdate_223
- ___vfx_script_fireworks_particleUpdate_238
- ___vfx_script_fireworks_particleUpdate_257
- ___vfx_script_fireworks_particleUpdate_273
- ___vfx_script_fireworks_particleUpdate_322
- ___vfx_script_fireworks_particleUpdate_39
- ___vfx_script_fireworks_particleUpdate_52
- ___vfx_script_fireworks_particleUpdate_73
- ___vfx_script_fireworks_particleUpdate_85
- ___vfx_script_hearts_graph_06A14A47_3880_4300_8226_188BD75B83F1
- ___vfx_script_hearts_graph_27B2C751_CFE3_4369_B337_BEA7A4125BA6
- ___vfx_script_hearts_graph_3E785FDE_1E85_40AA_A8D6_985C11FFF991
- ___vfx_script_hearts_graph_4267197A_7D75_425E_8F36_26328B281570
- ___vfx_script_hearts_graph_4E082B7E_A3DB_40F5_9D67_FBFC9824FD2D
- ___vfx_script_hearts_graph_6501AA18_D88F_4677_984C_34E780A7C1F0
- ___vfx_script_hearts_graph_6CDCF767_47EA_4180_9CAC_F5ACFF8AE4CF
- ___vfx_script_hearts_graph_77839324_3A35_4199_A55E_F65CEF5F32BF
- ___vfx_script_hearts_graph_781609DE_FEF0_4B99_B009_050ADBDF1B32
- ___vfx_script_hearts_graph_B0667801_C60E_4D93_B9A1_27F790726520
- ___vfx_script_hearts_graph_B8CFD00B_F83D_48B4_B9F3_B556F2C755C4
- ___vfx_script_hearts_graph_D45D06FA_D64A_4215_983D_70FBC27B23B0
- ___vfx_script_hearts_particleInit_127
- ___vfx_script_hearts_particleInit_130
- ___vfx_script_hearts_particleInit_17
- ___vfx_script_hearts_particleInit_28
- ___vfx_script_hearts_particleUpdate_100
- ___vfx_script_hearts_particleUpdate_210
- ___vfx_script_hearts_particleUpdate_59
- ___vfx_script_hearts_particleUpdate_95
- ___vfx_script_lasers_graph_1415613D_8457_4B24_9F2B_BDCEA47A7E46
- ___vfx_script_lasers_graph_31BFE03A_347F_4F4B_8062_57C3C496211B
- ___vfx_script_lasers_graph_3AFCB8D6_52EB_4CCA_8CDC_E3DC4941B357
- ___vfx_script_lasers_graph_598E1865_A878_4D27_8744_3FC0B2A676F9
- ___vfx_script_lasers_graph_5BEEC0A4_8351_4E81_B071_E7FCF2740A98
- ___vfx_script_lasers_graph_75AE1D4B_87B4_4422_8E85_FE9D23E01F3B
- ___vfx_script_lasers_graph_84E516C9_0301_4F69_B83A_25056C254AE8
- ___vfx_script_lasers_graph_C0E70AB3_A28A_4D4F_8BEB_9516B357779C
- ___vfx_script_lasers_graph_CD99FC2C_17B7_466E_930E_F05728CE31E3
- ___vfx_script_lasers_particleInit_117
- ___vfx_script_lasers_particleInit_141
- ___vfx_script_lasers_particleInit_26
- ___vfx_script_lasers_particleInit_27
- ___vfx_script_lasers_particleInit_28
- ___vfx_script_lasers_particleInit_58
- ___vfx_script_lasers_particleUpdate_114
- ___vfx_script_lasers_particleUpdate_119
- ___vfx_script_lasers_particleUpdate_18
- ___vfx_script_lasers_particleUpdate_21
- ___vfx_script_lasers_particleUpdate_71
- ___vfx_script_lasers_particleUpdate_83
- ___vfx_script_lasers_particleUpdate_84
- ___vfx_script_lighting_graph_2A1A65D6_42D2_422D_B043_7BA6751C7A80
- ___vfx_script_lighting_graph_9DD82DB1_83CC_4C95_8122_529530C0E9A5
- ___vfx_script_lighting_graph_B9299884_EF40_4793_BAD0_BB82A60C4C1E
- ___vfx_script_rain_graph_25FC010E_3796_4569_84C9_8E9B3FC08F4B
- ___vfx_script_rain_graph_2AEE11A5_5806_4949_9017_97A31959A146
- ___vfx_script_rain_graph_43A66462_6D38_40C4_9563_E3E4B018C43A
- ___vfx_script_rain_graph_47225A01_2C47_433D_93D9_BF1D85A3839F
- ___vfx_script_rain_graph_72169E6B_0B70_473E_B19D_953F01AC5993
- ___vfx_script_rain_graph_999F57E4_3BBD_4410_9780_400191D6A26B
- ___vfx_script_rain_graph_B55CB68B_5374_45B9_9B3B_050825454545
- ___vfx_script_rain_graph_C718F1B2_4BA3_4E66_8269_7C49E171E2EC
- ___vfx_script_rain_graph_D83B875F_FB36_42AC_BCF5_9AD248F8E2AB
- ___vfx_script_rain_graph_EDF6BEEC_34C4_489E_ABEC_1C4A62E25E40
- ___vfx_script_rain_graph_FA88FCF0_73CA_480E_A020_897384F93F5C
- ___vfx_script_rain_particleInit_149
- ___vfx_script_rain_particleInit_161
- ___vfx_script_rain_particleInit_167
- ___vfx_script_rain_particleUpdate_122
- ___vfx_script_rain_particleUpdate_194
- ___vfx_script_rain_particleUpdate_36
- ___vfx_script_rain_particleUpdate_95
- ___vfx_script_thumbsup_graph_0E7F5D5F_BCDE_46CD_975C_9DB38EBC84DE
- ___vfx_script_thumbsup_graph_31C4109F_11CA_46CC_B9D5_22B60B283208
- ___vfx_script_thumbsup_graph_38F35C26_FEA0_47AB_B998_9FF24156FD6D
- ___vfx_script_thumbsup_graph_451D2F34_D7DE_4C4D_9A5C_B1A778F1CA1C
- ___vfx_script_thumbsup_graph_5BEF5B4C_59E5_4DBA_86B0_DB00779F419D
- ___vfx_script_thumbsup_graph_891A5752_872E_4295_B8CA_3104EA0A6053
- ___vfx_script_thumbsup_graph_8D318DBD_EF7B_44D4_B5E6_F743F93F2B64
- ___vfx_script_thumbsup_graph_8EC5E521_8C63_47F8_B96D_2B0B5A296B7A
- ___vfx_script_thumbsup_graph_A591C9B7_84C4_4BEA_8829_4366B5881232
- ___vfx_script_thumbsup_graph_B59F1B79_7E62_4E5A_99DF_F365094C2D38
- ___vfx_script_thumbsup_graph_E58E02C9_8189_4980_ABED_6DF4C8EF7375
- ___vfx_script_thumbsup_particleInit_13
- ___vfx_script_thumbsup_particleInit_142
- ___vfx_script_thumbsup_particleInit_78
- ___vfx_script_thumbsup_particleUpdate_34
- ___vfx_script_thumbsup_particleUpdate_6
- ___vfx_script_thumbsup_particleUpdate_76
- _expf
- _filter_coefficients
- _filter_coefficients.cold.1
- _filter_coefficients.cold.2
- _gotLoadHelper_x8$_OBJC_CLASS_$_VFXSceneLoadOptions
- _gotLoadHelper_x8$_OBJC_CLASS_$__TtC3VFX8VFXScene
- _kCFBooleanFalse
- _kCFBooleanTrue
- _kIOMainPortDefault
- _kIOSurfaceAcceleratorLockInScaler
- _kIOSurfaceAcceleratorSkipAsyncCallback
- _kIOSurfaceAcceleratorSymmetricScaling
- _kIOSurfaceAcceleratorSymmetricTransformKey
- _kIOSurfaceAcceleratorUseCustomFilter
- _m2m_complete
- _objc_msgSend$_computeFeaturesDerivativesWithCommandBuffer:in_tex:out_tex:
- _objc_msgSend$_computeFeaturesWithCommandBuffer:in_tex:out_tex:
- _objc_msgSend$_createImagePyramidWithCommandBuffer:in_tex:I_idx:
- _objc_msgSend$_doNLRegularizationWithCommandBuffer:in_uv_tex:join_tex:w_tex:out_uv_tex:
- _objc_msgSend$_doSolverWithCommandBuffer:scale:in_uv_tex:in_G0_tex:in_G1_tex:in_C0_tex:in_C1_tex:out_uv_tex:out_w_tex:
- _objc_msgSend$_downsample:toDest:useCustomFilter:centerAlignment:synchronous:
- _objc_msgSend$_downscale2XWithCommandBuffer:in_tex:out_tex:
- _objc_msgSend$_enqueueFlowConsistencyWithCommandBuffer:in_uv0_tex:in_uv1_tex:out_uv_tex:
- _objc_msgSend$_enqueueKeypointsFromFlowWithCommandBuffer:in_uv_fwd_tex:in_uv_bwd_tex:out_kpt_buf:block_size:bidirectional_error:out_num_keypoints:
- _objc_msgSend$_rotate:toDest:synchronous:
- _objc_msgSend$_setupBuffer
- _objc_msgSend$_setupPipelines
- _objc_msgSend$_zeroFlowWithCommandBuffer:uv_tex:
- _objc_msgSend$addAdditionalOutput:
- _objc_msgSend$addEffectFrom:error:
- _objc_msgSend$addEffectFromTemplate:
- _objc_msgSend$adjustScissorRectToImageBlocks:
- _objc_msgSend$applyPortraitBlur:inColorBuffer:inBackgroundBuffer:effectRenderRequest:
- _objc_msgSend$architecture
- _objc_msgSend$asyncVFXInit
- _objc_msgSend$bindingName
- _objc_msgSend$bindingOf:named:
- _objc_msgSend$cameras
- _objc_msgSend$clearCaches
- _objc_msgSend$copyInYUV:toOutYUV:
- _objc_msgSend$createFocusObject:anamorphicFactor:colorSize:circleOfConfusionReference:fNumberLimitWeight:
- _objc_msgSend$disparityApplyPostModifier:inDisparity:outDisparity:postModfier:
- _objc_msgSend$disparityGuidedFilterEpsilon
- _objc_msgSend$disparityMinMaxApplyPostModifier:disparityMinMaxBuffer:postModfier:
- _objc_msgSend$disparityPortraitPreviewDeadzone:inDisparity:outDisparity:postModfier:
- _objc_msgSend$doDisparityUpsampling
- _objc_msgSend$downsampleQuarterSizeToTargetSize:
- _objc_msgSend$downsampleToLayer:
- _objc_msgSend$downsampleToQuarterSize:
- _objc_msgSend$drawTurboLegend:outRGBA:rect:maxValue:
- _objc_msgSend$effect
- _objc_msgSend$effectDepth
- _objc_msgSend$effectRGBA
- _objc_msgSend$encodeWithCommandBuffer:
- _objc_msgSend$estimateLightIntensityWithFaceRects:inTex:numberOfFaceRects:transform:humanDetections:asyncWork:
- _objc_msgSend$fetchClientTextureIDWithNamed:
- _objc_msgSend$finalizeEncoding
- _objc_msgSend$highResNetwork
- _objc_msgSend$initVFX:asyncInitQueue:
- _objc_msgSend$initWithCommandQueue:
- _objc_msgSend$initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:
- _objc_msgSend$initWithEffectRGBA:effectDepth:
- _objc_msgSend$initWithMetalContext:colorSize:colorConversion:prewarmOnly:humanDetections:asyncInitQueue:
- _objc_msgSend$initWithMetalContext:colorSize:effectUtil:util:useHighResNetwork:sharedResources:
- _objc_msgSend$initWithMetalContext:effectRelighting:renderState:util:colorConversion:msrColorPyramid:vfxRenderEffect:depthConverter:disparityFixedFocus:faceDisparityArray:focusDisparityRaw:focusDisparityModifiers:
- _objc_msgSend$initWithMetalContext:effectUtil:sharedResources:
- _objc_msgSend$initWithMetalContext:faceAttributesNetwork:availableEffectTypes:effectUtil:util:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:
- _objc_msgSend$initWithMetalContext:faceAttributesNetwork:effectUtil:msrColorPyramid:colorSize:prewarmOnly:sharedResources:
- _objc_msgSend$initWithMetalContext:inputSize:targetSize:rotateTargetPixelBuffer:sRGB:sharedResources:
- _objc_msgSend$initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:
- _objc_msgSend$initWithMetalContext:rgbaOutputPixelFormat:depthOutputPixelFormat:colorSize:
- _objc_msgSend$initWithSize:colorSpace:
- _objc_msgSend$initWithTextureSize:scissorRect:outRect:
- _objc_msgSend$invocationWithMethodSignature:
- _objc_msgSend$invoke
- _objc_msgSend$ioSurface
- _objc_msgSend$iosurface
- _objc_msgSend$lowercaseString
- _objc_msgSend$methodSignatureForSelector:
- _objc_msgSend$newBufferWithPixelFormat:width:data:
- _objc_msgSend$newComputePipelineStateWithDescriptor:error:
- _objc_msgSend$newDefaultLibraryWithBundle:error:
- _objc_msgSend$newPipelineLibraryWithFilePath:error:
- _objc_msgSend$pathForResource:ofType:
- _objc_msgSend$positionBinding
- _objc_msgSend$prepare
- _objc_msgSend$queryCapabilities
- _objc_msgSend$reconfigure:
- _objc_msgSend$removeEffect:
- _objc_msgSend$replaceBackground:inYUV:inSegmentation:effectRenderRequest:outYUV:frameIndex:
- _objc_msgSend$resourcePath
- _objc_msgSend$revision
- _objc_msgSend$rotate:crop:rotationDegree:toDest:synchronous:
- _objc_msgSend$sampleFaceRectsWithMaxFaceRects:faceRects:faceRectsState:focusDisparityMax:inDisparity:outFaceDistanceArray:
- _objc_msgSend$scene
- _objc_msgSend$setArgument:atIndex:
- _objc_msgSend$setAutomaticallyPrepareScene:
- _objc_msgSend$setClientTextureWithId:texture:
- _objc_msgSend$setColorPixelFormat:
- _objc_msgSend$setComputeFunction:
- _objc_msgSend$setCustomFilter:alignment:sourceWidth:sourceHeight:destinationWidth:destinationHeight:luma_param:chroma_param:
- _objc_msgSend$setDepthTexture:
- _objc_msgSend$setDisparityGuidedFilterEpsilon:
- _objc_msgSend$setEffect:
- _objc_msgSend$setEnableDeferredRendering:
- _objc_msgSend$setInternalPixelFormatDepth:
- _objc_msgSend$setIsEnabled:
- _objc_msgSend$setMetalLibraryURL:
- _objc_msgSend$setProjection:
- _objc_msgSend$setScene:
- _objc_msgSend$setSelector:
- _objc_msgSend$setSetupAsTemplate:
- _objc_msgSend$setTarget:
- _objc_msgSend$setThreadGroupSizeIsMultipleOfThreadExecutionWidth:
- _objc_msgSend$setupCommonVFXSceneLoadOptions:metalLibraryURL:commandQueue:
- _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
- _objc_msgSend$studioLightInYUV:inDiffuse:inDisparity:inFocusDisparityModifier:outYUV:relightStrength:studioLightFromSegmentationBlend:studioLightEffectModifier:
- _objc_msgSend$updateDisparityWithScreenCaptureRect:inDisparity:outDisparity:focalLenIn35mmFilm:fNumber:
- _objc_msgSend$updateFocusObjectWithFaceRectCount:disparityFocusOffsetSDOF:disparityFocusOffsetReactions:disparityFocusOffsetStudioLight:exponentialMovingAverageSDOF:exponentialMovingAverageStudioLight:faceRectsState:isFirstFrame:emitNewReaction:focusOnAll:lastFocus:inFaceDisparityArray:outDisparityModifiers:outDisparityFocus:outStudioLightEffectModifier:outUseDisparityBufferForReactions:
- _objc_msgSend$updateLevel0FromPTTextureRGBA:inPTTextureRGBA:doFirstLevelGaussianDownsample:
- _objc_msgSend$updateLevel0FromPTTextureYUV:inPTTextureYUV:doFirstLevelGaussianDownsample:
- _objc_msgSend$updateLevel0and1FromPTTextureRGBA:inPTTextureRGBA:
- _objc_msgSend$updateLevel0and1FromPTTextureYUV:inPTTextureYUV:
- _objc_msgSend$updatePyramidFromPTTexture:inPTTexture:
- _objc_msgSend$updateWithDeltaTime:
- _objc_retain_x12
- _render:.onceToken
- _renderDebugInformation:effectRenderRequest:reactionStates:disparity:disparityCentered:normal:diffuse:temporalFilter:humanDetections:transform:fNumber:focusDisparityRaw:useDisparityBufferForReactions:outYUV:.frameIndex
- _sForceSynchronousInitialization
- _sPTEffectDisableAsyncWork
- _sSRLAsyncLock
- _yellowSatFixCubeData
CStrings:
+ "#\xf0\xf0\xf0b$"
+ "*"
+ "+[PTLKTFlow _computeScalingFactor:dst_tex:scale_xy_inv:coeff:]"
+ "-[PTMSRResize initWithMetalContext:inputSize:targetSize:rotateTargetPixelBuffer:compressedIntermediates:sRGB:sharedResources:]"
+ "40@0:8@16@24@32"
+ "@\"<MTLTexture>\"32@0:8@\"NSString\"16@\"MTLTextureDescriptor\"24"
+ "@\"<VFXGraphBinding>\""
+ "@\"FigM2MController\""
+ "@\"FigMetalContext\""
+ "@\"PTLKTFlow\""
+ "@\"PTSRLv2Plist\""
+ "@\"PTSingleColorCubeCorrectionStage\""
+ "@\"PTStudioLightColorCorrectionAndConversion\""
+ "@\"PTVFXResources\""
+ "@\"VFXAssetNode\""
+ "@\"VFXCamera\""
+ "@\"VFXClientTextureAsset\""
+ "@\"VFXNode\""
+ "@\"VFXTextureAttachmentDescriptor\""
+ "@\"VFXTextureAttachmentDescriptor\"16@0:8"
+ "@\"VFXWorld\""
+ "@\"VisionCoreVideoSegmentationE5NetworkDescriptor\""
+ "@120@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112"
+ "@36@0:8^{__CVBuffer=}16@24B32"
+ "@44@0:8Q16i24r^v28@36"
+ "@52@0:8^{__CVBuffer=}16@24^{__CVMetalTextureCache=}32B40B44B48"
+ "@56@0:8{?=QQQ}16^{CGColorSpace=}40I48B52"
+ "@64@0:8@16{?=QQQ}24q48@56"
+ "@64@0:8{?=QQQ}16{?=QQQ}40"
+ "@68@0:816{?=QQQQ}2052Q60"
+ "@68@0:8@16@24{?=QQQ}32B56@60"
+ "@72@0:8@16@24q32@40@48@56@64"
+ "@80@0:8@\"PTMetalContext\"16{CGSize=dd}24{CGSize=dd}40q56B64@\"NSDictionary\"68i76"
+ "@80@0:8@16Q24B32{?=QQQ}36@60B68@72"
+ "@80@0:8@16{CGSize=dd}24{CGSize=dd}40q56B64@68i76"
+ "@84@0:8@16{?=QQQ}24@48B56@60@68@76"
+ "@92@0:8@16{?=QQQ}24{?=QQQ}48B72B76B80@84"
+ "@?16@0:8"
+ "A!"
+ "AB"
+ "B20@0:8I16"
+ "B40@0:8^^{e5rt_buffer_object}16i24@28B36"
+ "CVPixelBufferCreate failed %i using %@"
+ "Camera"
+ "Camera not found"
+ "Cannot have additional output smaller that 4x than targetSize"
+ "Commandbuffer is nil"
+ "Configure PTEffect (ptr %p). Type: %lu AvailableTypes: %lu quality: %lu size: %f x %f"
+ "E5ExecutionPriority"
+ "E5RT error (%s): %s"
+ "Error aspect ratio not maintained during crop"
+ "Error creating E5RT execution stream"
+ "Error creating E5RT execution stream operation"
+ "Error creating VisionCoreVideoSegmentationE5NetworkDescriptor for version %@. Error %@"
+ "Error getting VisionCoreE5RTFunction for %@ (%@). Error %@"
+ "Failed to create world from %@ error %@"
+ "Failed to get VisionCoreTensorDescriptor for %s: %@!"
+ "H11"
+ "Hand Gesture Detector Pool"
+ "I24@0:8I16i20"
+ "I28@0:8^{__IOSurface=}16f24"
+ "I32@0:8@16@24"
+ "I56@0:8^{__CVBuffer=}1624i40^{__CVBuffer=}44B52"
+ "IBLIntensity"
+ "IBLIntensity binding not found"
+ "Ignore reconfigureWithNewSize: due to equal descriptor"
+ "Invalid parameter. The number of scales specified is too large"
+ "Invalid parameter. Unknown preset"
+ "Invalid pixelbuffer"
+ "Invalid pixelbuffer size. inputTargetRGBA must equal outputDestination"
+ "MSR transform failed %i"
+ "NSDictionary"
+ "NSMutableDictionary"
+ "NSNumber"
+ "NSString"
+ "NSValue"
+ "PTCVMNetwork network outDisparityRotated"
+ "PTCVMNetwork network reset"
+ "PTDisparityPostProcessing computeOpticalFlow"
+ "PTDisparityPostProcessing prepare filter"
+ "PTDisparityPostProcessing temporalDisparityFilter"
+ "PTEffect copyTemporalState"
+ "PTEffect keepOldDelegateAlive"
+ "PTEffect reset"
+ "PTEffectComposition"
+ "PTEffectCompositionConfig"
+ "PTEffectCompositionRenderRequest"
+ "PTEffectDebugLayer renderDebugInformation"
+ "PTEffectPersonSegmentation runPersonSegmentation"
+ "PTEffectPersonSegmentationViSegHQVisionCoreE5"
+ "PTEffectRenderer Restore temporal state"
+ "PTEffectRenderer filter disparity and normal."
+ "PTEffectRenderer prepare disparity filter"
+ "PTEffectRenderer renderByPass"
+ "PTEffectRenderer renderPostLightEstimation"
+ "PTEffectRenderer renderPostSegmentationMask"
+ "PTEffectTemporalFilter temporalDisparityFilter"
+ "PTEspressoGenericExecutor convertBindInput"
+ "PTEspressoGenericExecutor convertBindOutput"
+ "PTLKTFlow"
+ "PTLKTFlow Init failed"
+ "PTLKTFlow.m"
+ "PTPixelBufferSize"
+ "PTRaytracingV14RenderState init noise"
+ "PTSRLv2Plist"
+ "PTSingleColorCubeCorrectionStage"
+ "PTStudioLightColorCorrectionAndConversion"
+ "PTSyntheticLight estimateLightIntensityWithFaceRects"
+ "PTSyntheticLight updateSubjectRelighting"
+ "PTTextureRGBAFromYUV"
+ "PTVFXResources"
+ "PTVFXResources wait for resources"
+ "PTVFXResourcesLogger"
+ "Portrait.framework"
+ "Q24@0:8@\"NSString\"16"
+ "Q32@0:8Q16@24"
+ "Reconfigure PTEffect (ptr %p). Type: %lu AvailableTypes: %lu quality: %lu size: %f x %f"
+ "T,V_alsColor"
+ "T@\"<MTLDevice>\",&,V_device"
+ "T@\"<VFXGraphBinding>\",&,N,V_backgroundDimmingBinding"
+ "T@\"<VFXGraphBinding>\",&,N,V_durationBinding"
+ "T@\"<VFXGraphBinding>\",&,N,V_headPositionBinding"
+ "T@\"<VFXGraphBinding>\",&,N,V_lightBinding"
+ "T@\"<VFXGraphBinding>\",&,N,V_positionBinding"
+ "T@\"NSDictionary\",&,N,V_metadataDictionary"
+ "T@\"PTEffectUtil\",&,N,V_effectUtil"
+ "T@\"PTFaceAttributesNetwork\",R"
+ "T@\"PTTextureYUV\",&,V_textureAsYUV"
+ "T@\"PTUtil\",&,N,V_util"
+ "T@\"PTVFXResources\",&,N,V_vfxResources"
+ "T@\"VFXAssetNode\",&,N,V_rootAssetNode"
+ "T@\"VFXCamera\",&,N,V_camera"
+ "T@\"VFXClientTextureAsset\",&,N,V_alphaTexture"
+ "T@\"VFXNode\",&,N,V_rootNode"
+ "T@\"VFXRenderer\",&,N,V_vfxRenderer"
+ "T@\"VFXTextureAttachmentDescriptor\",R,&,N"
+ "T@\"VFXWorld\",&,N,V_world"
+ "TB,V_allowCompressed"
+ "T^{__CVBuffer=},V_inputSourcePixelBuffer"
+ "T^{__CVBuffer=},V_inputTargetPixelBuffer"
+ "T^{__CVBuffer=},V_outputPixelBuffer"
+ "Tf,V_alsLuxLevel"
+ "Tf,V_ambientLightSensor"
+ "Tf,V_inputTargetRectCornerRadius"
+ "Ti,V_height"
+ "Ti,V_width"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},V_inputCropRect"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},V_inputTargetRect"
+ "Unhandled pixelformat %@\n"
+ "Unsupported rotation %i"
+ "VCPRequestCoreMLANEPriorityPropertyKey"
+ "VCPRequestEspressoPlanPriorityPropertyKey"
+ "VFX Init %@ error %@"
+ "VFX Init %@ progress %f stop %i "
+ "VFX Init Start %@"
+ "VFX initialization aborted"
+ "VFXNode"
+ "VFXTextureAttachmentProvider"
+ "VFXTransaction"
+ "[2@\"PTTexture\"]"
+ "[2^{e5rt_surface_object}]"
+ "[3@\"VisionCoreE5RTFunction\"]"
+ "[3[11^{e5rt_io_port}]]"
+ "[3^{e5rt_execution_stream_operation}]"
+ "[3^{e5rt_execution_stream}]"
+ "[4[2^{e5rt_buffer_object}]]"
+ "^{__CVBuffer=}44@0:8{?=QQQ}16B40"
+ "^{__CVBuffer=}48@0:8{?=QQQ}16B40I44"
+ "^{__CVPixelBufferPool=}"
+ "^{e5rt_surface_object=}"
+ "__vfx_script_balloons_graph_159"
+ "__vfx_script_balloons_graph_160"
+ "__vfx_script_balloons_graph_163"
+ "__vfx_script_balloons_graph_166"
+ "__vfx_script_balloons_graph_169"
+ "__vfx_script_balloons_graph_170"
+ "__vfx_script_balloons_graph_171"
+ "__vfx_script_balloons_graph_172"
+ "__vfx_script_balloons_graph_173"
+ "__vfx_script_balloons_graph_177"
+ "__vfx_script_balloons_particleInit_161"
+ "__vfx_script_balloons_particleInit_164"
+ "__vfx_script_balloons_particleInit_167"
+ "__vfx_script_balloons_particleInit_174"
+ "__vfx_script_balloons_particleInit_175"
+ "__vfx_script_balloons_particleUpdate_162"
+ "__vfx_script_balloons_particleUpdate_165"
+ "__vfx_script_balloons_particleUpdate_168"
+ "__vfx_script_balloons_particleUpdate_176"
+ "__vfx_script_confetti_graph_233"
+ "__vfx_script_confetti_graph_236"
+ "__vfx_script_confetti_graph_239"
+ "__vfx_script_confetti_graph_242"
+ "__vfx_script_confetti_graph_243"
+ "__vfx_script_confetti_graph_246"
+ "__vfx_script_confetti_graph_247"
+ "__vfx_script_confetti_particleInit_234"
+ "__vfx_script_confetti_particleInit_237"
+ "__vfx_script_confetti_particleInit_240"
+ "__vfx_script_confetti_particleInit_244"
+ "__vfx_script_confetti_particleInit_248"
+ "__vfx_script_confetti_particleUpdate_235"
+ "__vfx_script_confetti_particleUpdate_238"
+ "__vfx_script_confetti_particleUpdate_241"
+ "__vfx_script_confetti_particleUpdate_245"
+ "__vfx_script_fireworks_graph_353"
+ "__vfx_script_fireworks_graph_356"
+ "__vfx_script_fireworks_graph_357"
+ "__vfx_script_fireworks_graph_359"
+ "__vfx_script_fireworks_graph_361"
+ "__vfx_script_fireworks_graph_364"
+ "__vfx_script_fireworks_graph_367"
+ "__vfx_script_fireworks_graph_370"
+ "__vfx_script_fireworks_graph_373"
+ "__vfx_script_fireworks_graph_376"
+ "__vfx_script_fireworks_graph_379"
+ "__vfx_script_fireworks_graph_382"
+ "__vfx_script_fireworks_graph_385"
+ "__vfx_script_fireworks_graph_388"
+ "__vfx_script_fireworks_graph_391"
+ "__vfx_script_fireworks_graph_394"
+ "__vfx_script_fireworks_graph_395"
+ "__vfx_script_fireworks_graph_396"
+ "__vfx_script_fireworks_graph_397"
+ "__vfx_script_fireworks_graph_398"
+ "__vfx_script_fireworks_graph_399"
+ "__vfx_script_fireworks_graph_401"
+ "__vfx_script_fireworks_particleInit_351"
+ "__vfx_script_fireworks_particleInit_354"
+ "__vfx_script_fireworks_particleInit_358"
+ "__vfx_script_fireworks_particleInit_360"
+ "__vfx_script_fireworks_particleInit_362"
+ "__vfx_script_fireworks_particleInit_368"
+ "__vfx_script_fireworks_particleInit_371"
+ "__vfx_script_fireworks_particleInit_374"
+ "__vfx_script_fireworks_particleInit_380"
+ "__vfx_script_fireworks_particleInit_386"
+ "__vfx_script_fireworks_particleInit_392"
+ "__vfx_script_fireworks_particleInit_400"
+ "__vfx_script_fireworks_particleUpdate_268"
+ "__vfx_script_fireworks_particleUpdate_292"
+ "__vfx_script_fireworks_particleUpdate_352"
+ "__vfx_script_fireworks_particleUpdate_355"
+ "__vfx_script_fireworks_particleUpdate_363"
+ "__vfx_script_fireworks_particleUpdate_369"
+ "__vfx_script_fireworks_particleUpdate_372"
+ "__vfx_script_fireworks_particleUpdate_375"
+ "__vfx_script_fireworks_particleUpdate_381"
+ "__vfx_script_fireworks_particleUpdate_387"
+ "__vfx_script_fireworks_particleUpdate_393"
+ "__vfx_script_hearts_graph_222"
+ "__vfx_script_hearts_graph_226"
+ "__vfx_script_hearts_graph_227"
+ "__vfx_script_hearts_graph_228"
+ "__vfx_script_hearts_graph_231"
+ "__vfx_script_hearts_graph_232"
+ "__vfx_script_hearts_graph_233"
+ "__vfx_script_hearts_graph_234"
+ "__vfx_script_hearts_graph_235"
+ "__vfx_script_hearts_particleInit_223"
+ "__vfx_script_hearts_particleInit_224"
+ "__vfx_script_hearts_particleInit_229"
+ "__vfx_script_hearts_particleUpdate_225"
+ "__vfx_script_hearts_particleUpdate_230"
+ "__vfx_script_hearts_particleUpdate_6"
+ "__vfx_script_lasers_graph_134"
+ "__vfx_script_lasers_graph_135"
+ "__vfx_script_lasers_graph_136"
+ "__vfx_script_lasers_graph_138"
+ "__vfx_script_lasers_graph_140"
+ "__vfx_script_lasers_graph_141"
+ "__vfx_script_lasers_graph_142"
+ "__vfx_script_lasers_graph_146"
+ "__vfx_script_lasers_graph_150"
+ "__vfx_script_lasers_graph_151"
+ "__vfx_script_lasers_graph_154"
+ "__vfx_script_lasers_graph_156"
+ "__vfx_script_lasers_particleInit_137"
+ "__vfx_script_lasers_particleInit_143"
+ "__vfx_script_lasers_particleInit_145"
+ "__vfx_script_lasers_particleInit_148"
+ "__vfx_script_lasers_particleInit_152"
+ "__vfx_script_lasers_particleInit_155"
+ "__vfx_script_lasers_particleUpdate_139"
+ "__vfx_script_lasers_particleUpdate_144"
+ "__vfx_script_lasers_particleUpdate_147"
+ "__vfx_script_lasers_particleUpdate_149"
+ "__vfx_script_lasers_particleUpdate_153"
+ "__vfx_script_lasers_particleUpdate_157"
+ "__vfx_script_lasers_particleUpdate_4"
+ "__vfx_script_lighting_graph_6"
+ "__vfx_script_lighting_graph_7"
+ "__vfx_script_lighting_graph_8"
+ "__vfx_script_rain_graph_216"
+ "__vfx_script_rain_graph_219"
+ "__vfx_script_rain_graph_222"
+ "__vfx_script_rain_graph_223"
+ "__vfx_script_rain_graph_226"
+ "__vfx_script_rain_graph_229"
+ "__vfx_script_rain_graph_232"
+ "__vfx_script_rain_graph_233"
+ "__vfx_script_rain_particleInit_213"
+ "__vfx_script_rain_particleInit_220"
+ "__vfx_script_rain_particleInit_230"
+ "__vfx_script_rain_particleUpdate_214"
+ "__vfx_script_rain_particleUpdate_215"
+ "__vfx_script_rain_particleUpdate_221"
+ "__vfx_script_rain_particleUpdate_231"
+ "__vfx_script_thumbsup_graph_127"
+ "__vfx_script_thumbsup_graph_128"
+ "__vfx_script_thumbsup_graph_130"
+ "__vfx_script_thumbsup_graph_132"
+ "__vfx_script_thumbsup_graph_134"
+ "__vfx_script_thumbsup_graph_136"
+ "__vfx_script_thumbsup_particleInit_129"
+ "__vfx_script_thumbsup_particleInit_133"
+ "__vfx_script_thumbsup_particleInit_138"
+ "__vfx_script_thumbsup_particleUpdate_131"
+ "__vfx_script_thumbsup_particleUpdate_135"
+ "__vfx_script_thumbsup_particleUpdate_137"
+ "_allowCompressed"
+ "_alphaTexture"
+ "_alsColor"
+ "_alsLuxLevel"
+ "_ambientLightSensor"
+ "_boundInputIOSurface"
+ "_colorAttachmentDescriptor"
+ "_colorCorrectionAndConversion"
+ "_colorPyramid"
+ "_colorTexture"
+ "_composite"
+ "_computeFeatures:in_tex:out_tex:"
+ "_computeFeaturesDerivatives:in_tex:out_tex:"
+ "_contentsScaleFactor"
+ "_correctionColorCube"
+ "_createImagePyramid:in_tex:I_idx:"
+ "_cubeTexture"
+ "_depthPrioritization"
+ "_depthTexture"
+ "_doNLRegularization:in_uv_tex:join_tex:w_tex:out_uv_tex:"
+ "_doSolver:scale:in_uv_tex:in_G0_tex:in_G1_tex:in_C0_tex:in_C1_tex:out_uv_tex:out_w_tex:"
+ "_downscale2X:in_tex:out_tex:"
+ "_e5Functions"
+ "_e5SurfaceMatting"
+ "_effectDescritor"
+ "_enqueueFlowConsistency:in_uv0_tex:in_uv1_tex:out_uv_tex:"
+ "_enqueueKeypointsFromFlow:in_uv_fwd_tex:in_uv_bwd_tex:out_kpt_buf:block_size:bidirectional_error:out_num_keypoints:"
+ "_es"
+ "_esop"
+ "_figMetalContext"
+ "_inputCropRect"
+ "_inputE5Surface"
+ "_inputSourcePixelBuffer"
+ "_inputTargetPixelBuffer"
+ "_inputTargetRect"
+ "_inputTargetRectCornerRadius"
+ "_intermediateColor"
+ "_intermediateColorPixelbuffers"
+ "_intermediateColor[i]"
+ "_metadataDictionary"
+ "_metalContext.imageblocksSupported"
+ "_mipmapLevels[0].pixelFormat == MTLPixelFormatRGBA8Unorm_sRGB || _mipmapLevels[0].pixelFormat == MTLPixelFormatRGBA8Unorm || _mipmapLevels[0].pixelFormat == MTLPixelFormatRGBA16Float || _mipmapLevels[0].pixelFormat == MTLPixelFormatBGR10_XR_sRGB"
+ "_msrController"
+ "_msrResize"
+ "_networkPorts"
+ "_outputPixelBuffer"
+ "_pixelBufferPool"
+ "_radialObstructionFactor"
+ "_rgbMinMax"
+ "_rootAssetNode"
+ "_rootNode"
+ "_screenSize"
+ "_setupBuffer:"
+ "_setupPipelines:"
+ "_sourceMipmap"
+ "_studioLightColorCorrectionRGBToYUV"
+ "_supportGPUFamilyApple7"
+ "_textureAsYUV"
+ "_updateLevel0FromRGBA"
+ "_updateLevel0FromRGBA[colorTransferFunctionToLinear]"
+ "_updateLevel0FromYUV"
+ "_updateLevel0FromYUV[colorTransferFunctionToLinear]"
+ "_updateLevel0and1FromRGBA"
+ "_updateLevel0and1FromRGBA[colorTransferFunctionToLinear]"
+ "_updateLevel0and1FromYUV"
+ "_updateLevel0and1FromYUV[colorTransferFunctionToLinear]"
+ "_uv_bwd_tex_user_ref != nil"
+ "_verboseLogging"
+ "_vfxResources"
+ "_world"
+ "_zeroFlow:uv_tex:"
+ "addAdditionalOutput:allowCompressed:"
+ "addAdditionalOutput:allowCompressed:pixelFormat:"
+ "addAnimation:forKey:"
+ "addAnimationAsset:forKey:"
+ "addChildNode:"
+ "adjustScissorRectToImageBlocks:imageBlockSize:"
+ "allowCompressed"
+ "alphaTexture"
+ "alsColor"
+ "alsLuxLevel"
+ "ambientLightSensor"
+ "applyForce:atPosition:impulse:"
+ "applyForce:impulse:"
+ "applyPortraitBlur:inColorBuffer:inColorPyramid:inBackgroundBuffer:effectRenderRequest:"
+ "applyTorque:impulse:"
+ "arrayLength"
+ "asRGBA"
+ "asRGBAFromYUV"
+ "asYUV"
+ "assetRegistry"
+ "asyncVFXInit:metalContext:"
+ "begin"
+ "behaviorGraph"
+ "bindInputPixelBuffer:"
+ "blitCommandEncoder"
+ "boneNode"
+ "camera"
+ "characterDirectionForLanguage:"
+ "childNodeWithName:"
+ "childNodeWithName:recursively:"
+ "childNodes"
+ "clearIOSurface:value:"
+ "clientIdentifier"
+ "clone"
+ "composite"
+ "compressedPixelFormat:"
+ "compressedPixelFormat:compression:"
+ "computeDownsamplingFactorWithInputSource:inputTarget:renderRequest:"
+ "computeDownsamplingStepsWithInputSize:targetSize:"
+ "computePipelineStateFor:constants:"
+ "config.device"
+ "convertPosition:fromNode:"
+ "convertPosition:toNode:"
+ "convertTransform:fromNode:"
+ "convertTransform:toNode:"
+ "convertVector:fromNode:"
+ "convertVector:toNode:"
+ "copyInColor:toOutColor:"
+ "createFocusObject:anamorphicFactor:radialObstructionFactor:colorSize:circleOfConfusionReference:fNumberLimitWeight:"
+ "createFromPixelbuffer:device:textureCache:metalYCBCRConversion:read:write:"
+ "createTextureFromPixelBuffer:device:textureCache:sRGB:metalYCBCRConversion:"
+ "cvErr"
+ "deepClone"
+ "depthPrioritization"
+ "depthPrioritizationFromEffectQuality:"
+ "descriptorForInput:error:"
+ "descriptorForOutput:error:"
+ "disparityApplyPostModifier:inDisparity:outDisparity:postModifier:"
+ "disparityMinMaxApplyPostModifier:disparityMinMaxBuffer:postModifier:"
+ "disparityPortraitPreviewDeadzone:inDisparity:outDisparity:postModifier:"
+ "downsample:"
+ "downsample:dst:sync_m2m:"
+ "downsampleToLayer:source:dest:"
+ "effectUtil"
+ "estimateColorTemperatureFromBackground:colorTransferFunction:matrixYUVtoRGB:inBackgroundLuma:inBackgroundChroma:outColorTemperatureBuffer:"
+ "estimateLightIntensityWithFaceRects:inColor:numberOfFaceRects:transform:humanDetections:asyncWork:"
+ "faceAttributesNetwork"
+ "faceIndex"
+ "finalColorDescriptor"
+ "flush"
+ "functionForIdentifier:error:"
+ "generateMipmapsForTexture:"
+ "geometryIndex"
+ "getChromaOffset:"
+ "getMTLTextureDescriptor:device:metalYCBCRConversion:"
+ "harvesting.gpufamily"
+ "hitTestWithSegmentFromPoint:toPoint:options:"
+ "i108@0:8@16@24@32@40{PTFocus=ffffff}48@96f104"
+ "i28@0:8i16i20i24"
+ "i36@0:8B16@20@28"
+ "i36@0:8i16^{__CVBuffer=}20^{__CVBuffer=}28"
+ "i68@0:8@16@24@32@40@48@56i64"
+ "imageBlockSize"
+ "initVFX:sharedResources:asyncInitQueue:"
+ "initWithConfig:"
+ "initWithDescriptor:metalContext:depthPrioritization:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:"
+ "initWithFigMetalContext:"
+ "initWithLumaTexture:chromaTexture:"
+ "initWithMetalContext:availableEffectTypes:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:"
+ "initWithMetalContext:colorSize:colorConversion:prewarmOnly:humanDetections:sharedResources:asyncInitQueue:"
+ "initWithMetalContext:colorSize:depthPrioritization:sharedResources:"
+ "initWithMetalContext:colorSize:disparitySize:debugRendering:verbose:options:quality:"
+ "initWithMetalContext:correctionColorCube:"
+ "initWithMetalContext:effectRelighting:effectDescritor:renderState:util:colorConversion:msrColorPyramid:vfxRenderEffect:depthConverter:disparityFixedFocus:faceDisparityArray:focusDisparityRaw:focusDisparityModifiers:"
+ "initWithMetalContext:inputSize:targetSize:rotateTargetPixelBuffer:compressedIntermediates:sRGB:sharedResources:"
+ "initWithMetalContext:msrColorPyramid:colorSize:prewarmOnly:sharedResources:"
+ "initWithMetalContext:sharedResources:"
+ "initWithName:index:"
+ "initWithSize:colorSpace:pixelFormat:allowCompressed:"
+ "initWithTextureSize:scissorRect:outRect:imageblockSize:"
+ "initWithWidth:height:"
+ "initWithbundle:andOptionalCommandQueue:"
+ "initializeCubeMap:inputTexture:"
+ "input"
+ "inputCropRect"
+ "inputSourcePixelBuffer"
+ "inputTargetPixelBuffer"
+ "inputTargetRect"
+ "inputTargetRectCornerRadius"
+ "input_hidden"
+ "input_key"
+ "input_value"
+ "insertChildNode:"
+ "insertChildNode:atIndex:"
+ "is420YpCbCr8:"
+ "kDoFirstLevelGaussianDownsample"
+ "lightBinding"
+ "loadActionForAttachment:"
+ "localCoordinates"
+ "localNormal"
+ "localRotateBy:"
+ "localTranslateBy:"
+ "macroBlockSizeForPixelFormat:device:"
+ "mergeWorld:parentNode:parentAssetNode:"
+ "metadataDictionary"
+ "metalTextureCache"
+ "modelTransform"
+ "newBufferWithPixelFormat:width:data:metalContext:"
+ "node"
+ "num_keypoints <= MAX_KEYPOINTS"
+ "outputPixelBuffer"
+ "output_hidden"
+ "output_key"
+ "output_prob"
+ "output_value"
+ "parentNode"
+ "physicsBody"
+ "postProcessUpdateFrameForInferenceOutputKeyBuffer:inferenceOutputValueBuffer:postProcessingOutputKeyBuffer:postProcessingOutputValueBuffer:error:"
+ "preferredLanguages"
+ "prepareForRenderer:progressHandler:"
+ "presentationBoneNode"
+ "presentationNode"
+ "presentationObject"
+ "progressHandler"
+ "projectPoint:"
+ "q24@0:8q16"
+ "rate"
+ "reconfigure:isInitialized:"
+ "reconfigureWithNewSize:"
+ "removeAllAnimations"
+ "removeAllAnimationsWithBlendOutDuration:"
+ "removeAnimationForKey:"
+ "removeAnimationForKey:blendOutDuration:"
+ "removeFromParent"
+ "removeFromParentNode"
+ "render:renderRequest:"
+ "renderDebugInformation:effectRenderRequest:reactionStates:disparity:disparityCentered:normal:diffuse:temporalFilter:humanDetections:transform:fNumber:focusDisparityRaw:useDisparityBufferForReactions:outColor:"
+ "renderDebugLayer:renderRequest:inDisparityDiff:focusObject:quality:edgeTolerance:debugTextures:debugRendering:"
+ "renderTurboMix:inTex:inRGBA:outRGBA:valueOffset:valueMinMax:valueAbs:colorRangeMax:channelMultiplier:mixWithRGBFraction:region:"
+ "renderWithTextureAttachmentProvider:options:"
+ "rendererWithCommandQueue:options:"
+ "replaceBackground:inColor:inColorPyramid:inSegmentation:effectRenderRequest:outColor:frameIndex:"
+ "resetIfNeeded"
+ "rgbMinMax"
+ "rootAssetNode"
+ "rootNode"
+ "rotateBy:aroundTarget:"
+ "sampleFaceRects:maxFaceRects:faceRects:faceRectsState:focusDisparityMax:inDisparity:outFaceDistanceArray:"
+ "script_hitTest:options:"
+ "script_instantiate:"
+ "script_rootNode"
+ "setAllowCompressed:"
+ "setAlphaTexture:"
+ "setAlsColor:"
+ "setAlsLuxLevel:"
+ "setAmbientLightSensor:"
+ "setAnimationDurationAsFloat:"
+ "setAntialiasingMode:"
+ "setArrayLength:"
+ "setCamera:"
+ "setCustomFilter:alignment:src:dst:luma_param:chroma_param:"
+ "setEffectUtil:"
+ "setInputCropRect:"
+ "setInputSourcePixelBuffer:"
+ "setInputTargetPixelBuffer:"
+ "setInputTargetRect:"
+ "setInputTargetRectCornerRadius:"
+ "setLightBinding:"
+ "setMetadataDictionary:"
+ "setOutputPixelBuffer:"
+ "setProjectionTransform:"
+ "setRootAssetNode:"
+ "setRootNode:"
+ "setState:"
+ "setStateNamed:"
+ "setTextureAsYUV:"
+ "setUtil:"
+ "setValue:forKey:"
+ "setValue:forKeyPath:"
+ "setVfxRenderer:"
+ "setVfxResources:"
+ "setWorld:"
+ "sharedResources.effectUtil"
+ "sharedResources.util"
+ "studioLightColorCorrectionRGBToYUV"
+ "studioLightInColor:inDiffuse:inDisparity:inFocusDisparityModifier:outColor:relightStrength:studioLightFromSegmentationBlend:studioLightEffectModifier:"
+ "supportsMetalYCBCRConversion"
+ "supportsMetalYCBCRConversion:"
+ "supportsSourceTaggedBuffers"
+ "textureAsYUV"
+ "textureForAttachment:withDescriptor:"
+ "transform:crop:rotationDegree:toDest:synchronous:"
+ "transform:srcRect:dst:dstRect:rotate:sync_m2m:"
+ "unprojectPoint:"
+ "updateAtTime:"
+ "updateDisparity:inScreenCaptureRect:inDisparity:outDisparity:focalLenIn35mmFilm:fNumber:"
+ "updateFocusObject:faceRectCount:disparityFocusOffsetSDOF:disparityFocusOffsetReactions:disparityFocusOffsetStudioLight:exponentialMovingAverageSDOF:exponentialMovingAverageStudioLight:faceRectsState:isFirstFrame:emitNewReaction:focusOnAll:lastFocus:inFaceDisparityArray:outDisparityModifiers:outDisparityFocus:outStudioLightEffectModifier:outUseDisparityBufferForReactions:"
+ "updateHumanDetections:"
+ "updateLevel0FromRGBA"
+ "updateLevel0FromYUV"
+ "updateLevel0and1FromRGBA"
+ "updateLevel0and1FromYUV"
+ "updatePyramid:inPTTexture:"
+ "util"
+ "uv0"
+ "v104@0:8@16@24{PTFocus=ffffff}32{PTFocusEdge=ffff}80@96"
+ "v112@0:8@16@24@32{PTFocus=ffffff}40i88f92@96q104"
+ "v128@0:8@16i24{PTDisparityFocusOffset=ff}28{PTDisparityFocusOffset=ff}36{PTDisparityFocusOffset=ff}44f52f56^i60B68B72B76@80@88@96@104@112@120"
+ "v28@?0f8@\"NSError\"12^B20"
+ "v32@0:816"
+ "v64@0:8@16i24^28^i36f44@48@56"
+ "v76@0:8@16i24{half3x4=[3{half4=[4 ]}]}28@52@60@68"
+ "v80@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24@56@64f72f76"
+ "v88@0:8@16@24@32{PTFocus=ffffff}40"
+ "v92@0:8@16@24@32{PTFocus=ffffff}40f88"
+ "valueForKeyPath:"
+ "vfxRenderer"
+ "vfxResources"
+ "world"
+ "worldCoordinates"
+ "worldNormal"
+ "worldWithURL:options:error:"
+ "{?=QQQQ}56@0:8{?=QQQQ}16Q48"
+ "{PTFocus=ffffff}48@0:8@16f24f2832f40f44"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xe8"
- "%@_%@"
- "+[LKTFlowGPU _computeScalingFactor:dst_tex:scale_xy_inv:coeff:]"
- "-[PTMSRResize initWithMetalContext:inputSize:targetSize:rotateTargetPixelBuffer:sRGB:sharedResources:]"
- "10 bit YUV is unexpected"
- "@\"<PTRenderEffect>\""
- "@\"<VFXBinding>\""
- "@\"<_TtP3VFX10VFXBinding_>\""
- "@\"LKTFlowGPU\""
- "@\"PTRenderEffectInput\""
- "@\"PTRenderEffectManager\""
- "@\"PTRenderEffectOutput\""
- "@\"SRLv2Plist\""
- "@\"SingleColorCubeCorrectionStage\""
- "@\"_TtC3VFX9VFXCamera\""
- "@\"_TtC3VFX9VFXEffect\""
- "@104@0:8@16@24Q32@40@48B56{?=QQQ}60@84B92@96"
- "@112@0:8@16@24@32@40@48@56@64@72@80@88@96@104"
- "@36@0:8Q16i24r^v28"
- "@48@0:8{?=QQQ}16^{CGColorSpace=}40"
- "@56@0:8@16@24{?=QQQ}32"
- "@60@0:816{?=QQQQ}2052"
- "@64@0:8@16Q24Q32{?=QQQ}40"
- "@76@0:8@16@24B32@36@44@52@60@68"
- "@76@0:8@16{?=QQQ}24@48@56B64@68"
- "@76@0:8@16{?=QQQ}24@48B56@60@68"
- "@84@0:8@16@24@32@40{?=QQQ}48B72@76"
- "@88@0:8@\"PTMetalContext\"16@\"PTRenderEffectManager\"24{CGSize=dd}32{CGSize=dd}48q64B72@\"NSDictionary\"76i84"
- "@88@0:8@16@24{CGSize=dd}32{CGSize=dd}48q64B72@76i84"
- "@88@0:8@16{?=QQQ}24{?=QQQ}48B72B76@80"
- "Apple"
- "AppleM2ScalerCSCDriver"
- "Async task during destruction"
- "B0"
- "Cannot create effect %i"
- "Cannot create texture"
- "Configure PTEffect (ptr %p). Type: %lu AvailableTypes: %lu quality: %lu"
- "Error creating library %@ from %@"
- "Error creating pipeline library %@ from className %@. Falling back to MTLLibrary"
- "Expected 1 camera was %i"
- "Failed to prewarm PTRenderPipeline: latest version not included"
- "I56@0:8^{__IOSurface=}1624i40^{__IOSurface=}44B52"
- "IOService"
- "IOSurfaceAcceleratorCapabilitiesDict"
- "IOSurfaceAcceleratorCapabilitiesSymmetricScaling"
- "IOSurfaceAcceleratorCreate failed %i"
- "IOSurfaceAcceleratorFilterCoefficientsPostPointBits"
- "IOSurfaceAcceleratorFilterCoefficientsPrePointBits"
- "IOSurfaceAcceleratorFilterHorizontalPhasesCount"
- "IOSurfaceAcceleratorFilterHorizontalTapsCount"
- "IOSurfaceAcceleratorFilterVerticalPhasesCount"
- "IOSurfaceAcceleratorFilterVerticalTapsCount"
- "Invalid parameter"
- "LKT::KeypointsFromFlow"
- "LKTFlowGPU"
- "LKTFlowGPU Init failed"
- "LKTFlowGPU.m"
- "MLAneQoS"
- "MSR error %i"
- "MSR supportsSymmetricScaling %i"
- "PTEffectManagerDebug"
- "PTRenderEffect"
- "PTRenderEffectContainer"
- "PTRenderEffectInput"
- "PTRenderEffectOutput"
- "PTScreenCaptureComposite"
- "Position binding not found"
- "Resolved gpuName: %@"
- "SRLv2Plist"
- "SingleColorCubeCorrectionStage"
- "Skybox"
- "T@\"<MTLTexture>\",R,V_effectDepth"
- "T@\"<MTLTexture>\",R,V_effectRGBA"
- "T@\"<PTRenderEffect>\",&,N,V_renderEffect"
- "T@\"<VFXBinding>\",&,N,V_backgroundDimmingBinding"
- "T@\"<VFXBinding>\",&,N,V_durationBinding"
- "T@\"<VFXBinding>\",&,N,V_headPositionBinding"
- "T@\"<VFXBinding>\",&,N,V_positionBinding"
- "T@\"PTRenderEffectInput\",&,N,V_renderEffectInput"
- "T@\"PTRenderEffectOutput\",&,N,V_renderEffectOutput"
- "T@\"_TtC3VFX9VFXEffect\",&,N,V_effect"
- "TB,N,V_bicubic"
- "TB,Venabled"
- "TQ,R,VeffectPriority"
- "Tf,V_disparityGuidedFilterEpsilon"
- "Tf,VfocusDistance"
- "The number of scales specified is too large"
- "Ts,R"
- "Ts,R,VeffectType"
- "Unable to create pipelineState (%s): %s"
- "Unknown preset"
- "VTPixelTransferSessionTransferImage failed %i"
- "[2@\"PTTextureYUV\"]"
- "^^{__CVBuffer}16@0:8"
- "^{__CVBuffer=}40@0:8{?=QQQ}16"
- "^{__IOSurfaceAccelerator=}"
- "__vfx_script_balloons_graph_002BE311_BD95_45E8_95C2_2D34D7AFF9B4"
- "__vfx_script_balloons_graph_0C92C45F_EBE3_4B04_B05E_4634866C142E"
- "__vfx_script_balloons_graph_30F6F52E_9FD9_4037_93CA_CCE724034EB4"
- "__vfx_script_balloons_graph_598E1865_A878_4D27_8744_3FC0B2A676F9"
- "__vfx_script_balloons_graph_5CC22647_AE13_4002_961E_197A930CB43A"
- "__vfx_script_balloons_graph_8F8209A1_99A0_4036_A138_3AB3E67064C6"
- "__vfx_script_balloons_graph_B84097E5_E449_4B6D_91CB_A59BE625458A"
- "__vfx_script_balloons_graph_C007B07C_DCA2_428B_9117_ECF37793469A"
- "__vfx_script_balloons_graph_CD99FC2C_17B7_466E_930E_F05728CE31E3"
- "__vfx_script_balloons_graph_F1142E3A_E67C_40DC_BC13_10D44D3F90F7"
- "__vfx_script_balloons_particleInit_140"
- "__vfx_script_balloons_particleInit_40"
- "__vfx_script_balloons_particleInit_51"
- "__vfx_script_balloons_particleInit_58"
- "__vfx_script_balloons_particleInit_9"
- "__vfx_script_balloons_particleUpdate_121"
- "__vfx_script_balloons_particleUpdate_36"
- "__vfx_script_balloons_particleUpdate_81"
- "__vfx_script_balloons_particleUpdate_89"
- "__vfx_script_confetti_graph_06A14A47_3880_4300_8226_188BD75B83F1"
- "__vfx_script_confetti_graph_16E7F806_2D73_4A39_B82C_90F26336105A"
- "__vfx_script_confetti_graph_47AC3C7A_C039_41DA_AD43_881D7E0F565A"
- "__vfx_script_confetti_graph_47C93548_02F8_4EF6_928F_74CE4F39BBDE"
- "__vfx_script_confetti_graph_586EC683_ECAC_48E9_B645_74C36BE0B254"
- "__vfx_script_confetti_graph_5ECD10AA_AB39_44AA_809D_DE6EF1C771A6"
- "__vfx_script_confetti_graph_6501AA18_D88F_4677_984C_34E780A7C1F0"
- "__vfx_script_confetti_graph_77839324_3A35_4199_A55E_F65CEF5F32BF"
- "__vfx_script_confetti_graph_9855979D_D680_4AC7_999F_4BD84B083C71"
- "__vfx_script_confetti_graph_A9645361_1E28_4A66_8CE1_0FBB358E68C4"
- "__vfx_script_confetti_graph_B0667801_C60E_4D93_B9A1_27F790726520"
- "__vfx_script_confetti_graph_C7F30F02_BA8A_4DBA_8AB9_BEAFDE59A291"
- "__vfx_script_confetti_graph_D45D06FA_D64A_4215_983D_70FBC27B23B0"
- "__vfx_script_confetti_particleInit_113"
- "__vfx_script_confetti_particleInit_146"
- "__vfx_script_confetti_particleInit_172"
- "__vfx_script_confetti_particleInit_29"
- "__vfx_script_confetti_particleUpdate_124"
- "__vfx_script_confetti_particleUpdate_196"
- "__vfx_script_confetti_particleUpdate_25"
- "__vfx_script_fireworks_graph_07D62C9C_6FAA_4BD9_910F_CDEA5CFCCC06"
- "__vfx_script_fireworks_graph_10EDDCB9_24C0_4755_971D_D6EC1FAF1000"
- "__vfx_script_fireworks_graph_155128CD_E118_4113_8D6F_8B7F5BA2555D"
- "__vfx_script_fireworks_graph_1E09F83D_74E8_4C33_AF7B_D1F4C7561C24"
- "__vfx_script_fireworks_graph_1F546ADD_0390_45D8_A31D_6FD1CEDB0057"
- "__vfx_script_fireworks_graph_224CDDEA_614F_4333_A343_6F25B6068E45"
- "__vfx_script_fireworks_graph_32BE36EE_4AAF_45ED_8B70_F204A610CBF9"
- "__vfx_script_fireworks_graph_3C6ED067_7943_49AD_A0AE_15130042E793"
- "__vfx_script_fireworks_graph_402F3097_0BA4_4A83_9FEB_E7261701F766"
- "__vfx_script_fireworks_graph_4AD865B9_2CA1_4C82_AA72_EC49942DA9DE"
- "__vfx_script_fireworks_graph_4E8B4DDD_D3C2_4DDF_ACF2_2ECC08723FDB"
- "__vfx_script_fireworks_graph_4F52B7E1_CA7E_4C70_B2C9_199EA88DF652"
- "__vfx_script_fireworks_graph_4F9764F9_0AFB_41B2_A2E5_90D5BEA2660F"
- "__vfx_script_fireworks_graph_514A5D4A_9A37_436A_B056_B2F8227D2BE1"
- "__vfx_script_fireworks_graph_5AC753AC_F888_4AEE_B41F_BA9FA15941CC"
- "__vfx_script_fireworks_graph_5AFE93DC_23D2_46C1_93C9_29F6F7292984"
- "__vfx_script_fireworks_graph_5C6FE0C4_5B31_468F_9708_94003733DEC5"
- "__vfx_script_fireworks_graph_5DD07B06_8DCA_42DA_80D9_81BBED0FBF33"
- "__vfx_script_fireworks_graph_647D8C58_3A96_4185_83BF_F834C05973E6"
- "__vfx_script_fireworks_graph_68ABBDD2_799D_4316_B610_A615A6E5C6C0"
- "__vfx_script_fireworks_graph_70391988_6235_4105_AB03_8B09A79D6EF6"
- "__vfx_script_fireworks_graph_72691A8E_EB30_4566_BC51_64DA827A694A"
- "__vfx_script_fireworks_graph_913AA320_A3AD_4B97_B3CE_288034B4B02B"
- "__vfx_script_fireworks_graph_9C215676_B35D_4738_8604_1B0696C120C9"
- "__vfx_script_fireworks_graph_9F0A8F07_3A67_4589_A511_28A794F02526"
- "__vfx_script_fireworks_graph_A51B6B76_047A_469C_B965_C43FB2E4CAC7"
- "__vfx_script_fireworks_graph_A5860394_860A_466B_9036_4241BA694F84"
- "__vfx_script_fireworks_graph_BE082C18_F014_49F4_AE91_49F0A20CA327"
- "__vfx_script_fireworks_graph_C96088C0_AF79_4824_9185_0DFF8E90BFB3"
- "__vfx_script_fireworks_graph_C9C0CC36_AD87_4391_B404_40CBC37682DC"
- "__vfx_script_fireworks_graph_CC976411_EC12_4A2C_A577_DD5F08309A69"
- "__vfx_script_fireworks_graph_CECA8E5C_A7BB_4D57_BBA3_E684CB761DA9"
- "__vfx_script_fireworks_graph_DB777B14_A366_4CC8_8010_6DFA3030539E"
- "__vfx_script_fireworks_graph_E9D5C3AC_14D8_4C9E_A340_8873556A15AC"
- "__vfx_script_fireworks_graph_EA69B710_0EB0_430A_84ED_99FDFB897003"
- "__vfx_script_fireworks_graph_EF83050E_3420_4C5E_B29A_63DE74130B60"
- "__vfx_script_fireworks_graph_FB239A73_A49B_49A1_B28F_F8EB686AE087"
- "__vfx_script_fireworks_particleInit_118"
- "__vfx_script_fireworks_particleInit_14"
- "__vfx_script_fireworks_particleInit_140"
- "__vfx_script_fireworks_particleInit_169"
- "__vfx_script_fireworks_particleInit_182"
- "__vfx_script_fireworks_particleInit_189"
- "__vfx_script_fireworks_particleInit_217"
- "__vfx_script_fireworks_particleInit_219"
- "__vfx_script_fireworks_particleInit_235"
- "__vfx_script_fireworks_particleInit_264"
- "__vfx_script_fireworks_particleInit_54"
- "__vfx_script_fireworks_particleInit_8"
- "__vfx_script_fireworks_particleInit_86"
- "__vfx_script_fireworks_particleUpdate_142"
- "__vfx_script_fireworks_particleUpdate_143"
- "__vfx_script_fireworks_particleUpdate_22"
- "__vfx_script_fireworks_particleUpdate_223"
- "__vfx_script_fireworks_particleUpdate_238"
- "__vfx_script_fireworks_particleUpdate_257"
- "__vfx_script_fireworks_particleUpdate_273"
- "__vfx_script_fireworks_particleUpdate_322"
- "__vfx_script_fireworks_particleUpdate_39"
- "__vfx_script_fireworks_particleUpdate_52"
- "__vfx_script_fireworks_particleUpdate_73"
- "__vfx_script_fireworks_particleUpdate_85"
- "__vfx_script_hearts_graph_06A14A47_3880_4300_8226_188BD75B83F1"
- "__vfx_script_hearts_graph_27B2C751_CFE3_4369_B337_BEA7A4125BA6"
- "__vfx_script_hearts_graph_3E785FDE_1E85_40AA_A8D6_985C11FFF991"
- "__vfx_script_hearts_graph_4267197A_7D75_425E_8F36_26328B281570"
- "__vfx_script_hearts_graph_4E082B7E_A3DB_40F5_9D67_FBFC9824FD2D"
- "__vfx_script_hearts_graph_6501AA18_D88F_4677_984C_34E780A7C1F0"
- "__vfx_script_hearts_graph_6CDCF767_47EA_4180_9CAC_F5ACFF8AE4CF"
- "__vfx_script_hearts_graph_77839324_3A35_4199_A55E_F65CEF5F32BF"
- "__vfx_script_hearts_graph_781609DE_FEF0_4B99_B009_050ADBDF1B32"
- "__vfx_script_hearts_graph_B0667801_C60E_4D93_B9A1_27F790726520"
- "__vfx_script_hearts_graph_B8CFD00B_F83D_48B4_B9F3_B556F2C755C4"
- "__vfx_script_hearts_graph_D45D06FA_D64A_4215_983D_70FBC27B23B0"
- "__vfx_script_hearts_particleInit_127"
- "__vfx_script_hearts_particleInit_130"
- "__vfx_script_hearts_particleInit_17"
- "__vfx_script_hearts_particleInit_28"
- "__vfx_script_hearts_particleUpdate_100"
- "__vfx_script_hearts_particleUpdate_210"
- "__vfx_script_hearts_particleUpdate_59"
- "__vfx_script_hearts_particleUpdate_95"
- "__vfx_script_lasers_graph_1415613D_8457_4B24_9F2B_BDCEA47A7E46"
- "__vfx_script_lasers_graph_31BFE03A_347F_4F4B_8062_57C3C496211B"
- "__vfx_script_lasers_graph_3AFCB8D6_52EB_4CCA_8CDC_E3DC4941B357"
- "__vfx_script_lasers_graph_598E1865_A878_4D27_8744_3FC0B2A676F9"
- "__vfx_script_lasers_graph_5BEEC0A4_8351_4E81_B071_E7FCF2740A98"
- "__vfx_script_lasers_graph_75AE1D4B_87B4_4422_8E85_FE9D23E01F3B"
- "__vfx_script_lasers_graph_84E516C9_0301_4F69_B83A_25056C254AE8"
- "__vfx_script_lasers_graph_C0E70AB3_A28A_4D4F_8BEB_9516B357779C"
- "__vfx_script_lasers_graph_CD99FC2C_17B7_466E_930E_F05728CE31E3"
- "__vfx_script_lasers_particleInit_117"
- "__vfx_script_lasers_particleInit_141"
- "__vfx_script_lasers_particleInit_26"
- "__vfx_script_lasers_particleInit_27"
- "__vfx_script_lasers_particleInit_28"
- "__vfx_script_lasers_particleInit_58"
- "__vfx_script_lasers_particleUpdate_114"
- "__vfx_script_lasers_particleUpdate_119"
- "__vfx_script_lasers_particleUpdate_18"
- "__vfx_script_lasers_particleUpdate_21"
- "__vfx_script_lasers_particleUpdate_71"
- "__vfx_script_lasers_particleUpdate_83"
- "__vfx_script_lasers_particleUpdate_84"
- "__vfx_script_lighting_graph_2A1A65D6_42D2_422D_B043_7BA6751C7A80"
- "__vfx_script_lighting_graph_9DD82DB1_83CC_4C95_8122_529530C0E9A5"
- "__vfx_script_lighting_graph_B9299884_EF40_4793_BAD0_BB82A60C4C1E"
- "__vfx_script_rain_graph_25FC010E_3796_4569_84C9_8E9B3FC08F4B"
- "__vfx_script_rain_graph_2AEE11A5_5806_4949_9017_97A31959A146"
- "__vfx_script_rain_graph_43A66462_6D38_40C4_9563_E3E4B018C43A"
- "__vfx_script_rain_graph_47225A01_2C47_433D_93D9_BF1D85A3839F"
- "__vfx_script_rain_graph_72169E6B_0B70_473E_B19D_953F01AC5993"
- "__vfx_script_rain_graph_999F57E4_3BBD_4410_9780_400191D6A26B"
- "__vfx_script_rain_graph_B55CB68B_5374_45B9_9B3B_050825454545"
- "__vfx_script_rain_graph_C718F1B2_4BA3_4E66_8269_7C49E171E2EC"
- "__vfx_script_rain_graph_D83B875F_FB36_42AC_BCF5_9AD248F8E2AB"
- "__vfx_script_rain_graph_EDF6BEEC_34C4_489E_ABEC_1C4A62E25E40"
- "__vfx_script_rain_graph_FA88FCF0_73CA_480E_A020_897384F93F5C"
- "__vfx_script_rain_particleInit_149"
- "__vfx_script_rain_particleInit_161"
- "__vfx_script_rain_particleInit_167"
- "__vfx_script_rain_particleUpdate_122"
- "__vfx_script_rain_particleUpdate_194"
- "__vfx_script_rain_particleUpdate_36"
- "__vfx_script_rain_particleUpdate_95"
- "__vfx_script_thumbsup_graph_0E7F5D5F_BCDE_46CD_975C_9DB38EBC84DE"
- "__vfx_script_thumbsup_graph_31C4109F_11CA_46CC_B9D5_22B60B283208"
- "__vfx_script_thumbsup_graph_38F35C26_FEA0_47AB_B998_9FF24156FD6D"
- "__vfx_script_thumbsup_graph_451D2F34_D7DE_4C4D_9A5C_B1A778F1CA1C"
- "__vfx_script_thumbsup_graph_5BEF5B4C_59E5_4DBA_86B0_DB00779F419D"
- "__vfx_script_thumbsup_graph_891A5752_872E_4295_B8CA_3104EA0A6053"
- "__vfx_script_thumbsup_graph_8D318DBD_EF7B_44D4_B5E6_F743F93F2B64"
- "__vfx_script_thumbsup_graph_8EC5E521_8C63_47F8_B96D_2B0B5A296B7A"
- "__vfx_script_thumbsup_graph_A591C9B7_84C4_4BEA_8829_4366B5881232"
- "__vfx_script_thumbsup_graph_B59F1B79_7E62_4E5A_99DF_F365094C2D38"
- "__vfx_script_thumbsup_graph_E58E02C9_8189_4980_ABED_6DF4C8EF7375"
- "__vfx_script_thumbsup_particleInit_13"
- "__vfx_script_thumbsup_particleInit_142"
- "__vfx_script_thumbsup_particleInit_78"
- "__vfx_script_thumbsup_particleUpdate_34"
- "__vfx_script_thumbsup_particleUpdate_6"
- "__vfx_script_thumbsup_particleUpdate_76"
- "_accelRef"
- "_bicubic"
- "_cap"
- "_computeFeaturesDerivativesWithCommandBuffer:in_tex:out_tex:"
- "_computeFeaturesWithCommandBuffer:in_tex:out_tex:"
- "_copySingleChannel"
- "_createImagePyramidWithCommandBuffer:in_tex:I_idx:"
- "_disparityGuidedFilterEpsilon"
- "_disparitySizeUpscaled"
- "_doNLRegularizationWithCommandBuffer:in_uv_tex:join_tex:w_tex:out_uv_tex:"
- "_doSolverWithCommandBuffer:scale:in_uv_tex:in_G0_tex:in_G1_tex:in_C0_tex:in_C1_tex:out_uv_tex:out_w_tex:"
- "_downsample:toDest:useCustomFilter:centerAlignment:synchronous:"
- "_downscale2XWithCommandBuffer:in_tex:out_tex:"
- "_effect"
- "_effectDepth"
- "_effectDepthDebug"
- "_effectRGBA"
- "_enqueueFlowConsistencyWithCommandBuffer:in_uv0_tex:in_uv1_tex:out_uv_tex:"
- "_enqueueKeypointsFromFlowWithCommandBuffer:in_uv_fwd_tex:in_uv_bwd_tex:out_kpt_buf:block_size:bidirectional_error:out_num_keypoints:"
- "_floatingAlphaCutout"
- "_intermediateYUV"
- "_intermediateYUV[i]"
- "_lighting"
- "_mainMetalContext.commandBuffer"
- "_matrixRGBtoYUV"
- "_metalContext.commandBuffer"
- "_mipmapLevels[0].pixelFormat == MTLPixelFormatRGBA8Unorm || _mipmapLevels[0].pixelFormat == MTLPixelFormatRGBA16Float || _mipmapLevels[0].pixelFormat == MTLPixelFormatBGR10_XR_sRGB"
- "_renderEffectInput"
- "_renderEffectOutput"
- "_renderEffects"
- "_rotate:toDest:synchronous:"
- "_setupBuffer"
- "_setupPipelines"
- "_supportsSymmetricScaling"
- "_updateLevel0Box2x2FromRGBA"
- "_updateLevel0Box2x2FromRGBA[colorTransferFunctionToLinear]"
- "_updateLevel0Box2x2FromYUV"
- "_updateLevel0Box2x2FromYUV[colorTransferFunctionToLinear]"
- "_updateLevel0Gaussian3x3FromRGBA"
- "_updateLevel0Gaussian3x3FromRGBA[colorTransferFunctionToLinear]"
- "_updateLevel0Gaussian3x3FromYUV"
- "_updateLevel0Gaussian3x3FromYUV[colorTransferFunctionToLinear]"
- "_updateLevel0and1Gaussian3x3FromRGBA"
- "_updateLevel0and1Gaussian3x3FromRGBA[colorTransferFunctionToLinear]"
- "_updateLevel0and1Gaussian3x3FromYUV"
- "_updateLevel0and1Gaussian3x3FromYUV[colorTransferFunctionToLinear]"
- "_useHighResNetwork"
- "_zeroFlowWithCommandBuffer:uv_tex:"
- "addAdditionalOutput:"
- "addEffectFrom %@ error %@"
- "addEffectFrom:error:"
- "addEffectFromTemplate:"
- "addRenderEffect:"
- "adjustScissorRectToImageBlocks:"
- "applegpu_"
- "applyPortraitBlur:inColorBuffer:inBackgroundBuffer:effectRenderRequest:"
- "architecture"
- "asyncVFXInit"
- "bicubic"
- "bindingName"
- "bindingOf:named:"
- "cameras"
- "chroma"
- "clearCaches"
- "copyInYUV:toOutYUV:"
- "copySingleChannel"
- "copySingleChannelInTex:outTex:"
- "createFocusObject:anamorphicFactor:colorSize:circleOfConfusionReference:fNumberLimitWeight:"
- "disparityApplyPostModifier:inDisparity:outDisparity:postModfier:"
- "disparityGuidedFilterEpsilon"
- "disparityMinMaxApplyPostModifier:disparityMinMaxBuffer:postModfier:"
- "disparityPortraitPreviewDeadzone:inDisparity:outDisparity:postModfier:"
- "doDisparityUpsampling"
- "downsampleQuarterSizeToTargetSize:"
- "downsampleToLayer:"
- "downsampleToQuarterSize:"
- "effect"
- "effectDepth"
- "effectDepthDebug"
- "effectPriority"
- "effectRGBA"
- "encodeWithCommandBuffer:"
- "estimateLightIntensityWithFaceRects:inTex:numberOfFaceRects:transform:humanDetections:asyncWork:"
- "fetchClientTextureIDWithNamed:"
- "figCFDictionaryGetNumberIfPresent"
- "finalizeEncoding"
- "floatingAlphaCutout"
- "floatingAlphaCutout:inPersonSegmentation:bilbyPersonMask:bilbyEffectMask:bilbyFloatingBackgroundRGBA:outVideoColorBufferRGBA:"
- "g16p"
- "g17p"
- "gpu name: %@"
- "gpu revision: %@"
- "highResNetwork"
- "i100@0:8@16@24@32@40{PTFocus=ffffff}48@88f96"
- "i28@0:8B16@20"
- "i36@0:8@16@24B32"
- "i36@0:8^{__IOSurface=}16^{__IOSurface=}24B32"
- "i44@0:8^{__IOSurface=}16^{__IOSurface=}24B32B36B40"
- "i64@0:8i16i20Q24Q32Q40Q48f56f60"
- "initVFX:asyncInitQueue:"
- "initWithDescriptor:metalContext:useHighResNetwork:faceAttributesNetwork:humanDetections:prevTemporalState:asyncInitQueue:sharedResources:"
- "initWithEffectRGBA:effectDepth:"
- "initWithMetalContext:colorSize:colorConversion:prewarmOnly:humanDetections:asyncInitQueue:"
- "initWithMetalContext:colorSize:effectUtil:util:useHighResNetwork:sharedResources:"
- "initWithMetalContext:effectRelighting:renderState:util:colorConversion:msrColorPyramid:vfxRenderEffect:depthConverter:disparityFixedFocus:faceDisparityArray:focusDisparityRaw:focusDisparityModifiers:"
- "initWithMetalContext:effectUtil:sharedResources:"
- "initWithMetalContext:faceAttributesNetwork:availableEffectTypes:effectUtil:util:prewarmOnly:colorSize:msrColorPyramid:studiolightFromSegmentation:sharedResources:"
- "initWithMetalContext:faceAttributesNetwork:effectUtil:msrColorPyramid:colorSize:prewarmOnly:sharedResources:"
- "initWithMetalContext:inputSize:targetSize:rotateTargetPixelBuffer:sRGB:sharedResources:"
- "initWithMetalContext:renderEffect:colorSize:"
- "initWithMetalContext:renderEffects:"
- "initWithMetalContext:renderEffects:colorSize:disparitySize:debugRendering:verbose:options:quality:"
- "initWithMetalContext:rgbaOutputPixelFormat:depthOutputPixelFormat:colorSize:"
- "initWithSize:colorSpace:"
- "initWithTextureSize:scissorRect:outRect:"
- "intensity"
- "intsz + decsz <= (int)(sizeof( ret ) * 8)"
- "invocationWithMethodSignature:"
- "invoke"
- "iosurface"
- "key != NULL"
- "lowResDisparitySizeFromEffectDescriptor"
- "lowercaseString"
- "luma"
- "maxDepth"
- "metalContext.commandBuffer"
- "newBufferWithPixelFormat:width:data:"
- "newComputePipelineStateWithDescriptor:error:"
- "newDefaultLibraryWithBundle:error:"
- "newPipelineLibraryWithFilePath:error:"
- "pathForResource:ofType:"
- "planPriority"
- "prepare"
- "pyramidRGBAPixelBuffer"
- "queryCapabilities"
- "removeEffect:"
- "render:renderRequest:input:output:"
- "renderDebugInformation:effectRenderRequest:reactionStates:disparity:disparityCentered:normal:diffuse:temporalFilter:humanDetections:transform:fNumber:focusDisparityRaw:useDisparityBufferForReactions:outYUV:"
- "renderDebugLayer:renderRequest:inDisparity:disparityOffset:focusObject:quality:edgeTolerance:debugTextures:debugRendering:"
- "renderEffectInput"
- "renderEffectOutput"
- "renderTurboMix:inTex:inRGBA:outRGBA:valueOffset:valueMinMax:valueAbs:colorRangeMax:channelMultiplier:mixFraction:region:"
- "replaceBackground:inYUV:inSegmentation:effectRenderRequest:outYUV:frameIndex:"
- "resourcePath"
- "revision"
- "rotate:crop:rotationDegree:toDest:synchronous:"
- "s"
- "s16@0:8"
- "sampleFaceRectsWithMaxFaceRects:faceRects:faceRectsState:focusDisparityMax:inDisparity:outFaceDistanceArray:"
- "scene"
- "setArgument:atIndex:"
- "setAutomaticallyPrepareScene:"
- "setBicubic:"
- "setClientTextureWithId:texture:"
- "setColorPixelFormat:"
- "setComputeFunction:"
- "setCustomFilter:alignment:sourceWidth:sourceHeight:destinationWidth:destinationHeight:luma_param:chroma_param:"
- "setDepthTexture:"
- "setDisparityGuidedFilterEpsilon:"
- "setDoNotClearRenderOutput:"
- "setEffect:"
- "setEnableDeferredRendering:"
- "setEnabled:"
- "setInternalPixelFormatDepth:"
- "setIsEnabled:"
- "setMetalLibraryURL:"
- "setProjection:"
- "setRenderEffectInput:"
- "setRenderEffectOutput:"
- "setScene:"
- "setSelector:"
- "setSetupAsTemplate:"
- "setTarget:"
- "setThreadGroupSizeIsMultipleOfThreadExecutionWidth:"
- "setupCommonVFXSceneLoadOptions:metalLibraryURL:commandQueue:"
- "stringByReplacingOccurrencesOfString:withString:"
- "studioLightInYUV:inDiffuse:inDisparity:inFocusDisparityModifier:outYUV:relightStrength:studioLightFromSegmentationBlend:studioLightEffectModifier:"
- "to_fixed"
- "update:renderRequest:"
- "updateDisparityWithScreenCaptureRect:inDisparity:outDisparity:focalLenIn35mmFilm:fNumber:"
- "updateFocusObjectWithFaceRectCount:disparityFocusOffsetSDOF:disparityFocusOffsetReactions:disparityFocusOffsetStudioLight:exponentialMovingAverageSDOF:exponentialMovingAverageStudioLight:faceRectsState:isFirstFrame:emitNewReaction:focusOnAll:lastFocus:inFaceDisparityArray:outDisparityModifiers:outDisparityFocus:outStudioLightEffectModifier:outUseDisparityBufferForReactions:"
- "updateLevel0Box2x2FromRGBA"
- "updateLevel0Box2x2FromYUV"
- "updateLevel0FromPTTextureRGBA:inPTTextureRGBA:doFirstLevelGaussianDownsample:"
- "updateLevel0FromPTTextureYUV:inPTTextureYUV:doFirstLevelGaussianDownsample:"
- "updateLevel0Gaussian3x3FromRGBA"
- "updateLevel0Gaussian3x3FromYUV"
- "updateLevel0and1FromPTTextureRGBA:inPTTextureRGBA:"
- "updateLevel0and1FromPTTextureYUV:inPTTextureYUV:"
- "updateLevel0and1Gaussian3x3FromRGBA"
- "updateLevel0and1Gaussian3x3FromYUV"
- "updatePyramidFromPTTexture:inPTTexture:"
- "updateWithDeltaTime:"
- "v108@0:8@16@24@32f40{PTFocus=ffffff}44i84f88@92q100"
- "v120@0:8i16{PTDisparityFocusOffset=ff}20{PTDisparityFocusOffset=ff}28{PTDisparityFocusOffset=ff}36f44f48^i52B60B64B68@72@80@88@96@104@112"
- "v24@0:8@\"<PTRenderEffect>\"16"
- "v28@0:8f16@\"PTRenderRequest\"20"
- "v28@0:8i16i20i24"
- "v48@0:8@\"<MTLCommandBuffer>\"16@\"PTRenderRequest\"24@\"PTRenderEffectInput\"32@\"PTRenderEffectOutput\"40"
- "v56@0:8i16^20^i28f36@40@48"
- "v72@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48@56f64f68"
- "v80@0:8@16@24@32{PTFocus=ffffff}40"
- "v84@0:8@16@24@32{PTFocus=ffffff}40f80"
- "v96@0:8@16@24{PTFocus=ffffff}32{PTFocusEdge=ffff}72@88"
- "valuePtr != NULL"
- "{?=\"hTaps\"i\"vTaps\"i\"hPhases\"i\"vPhases\"i\"prePointBits\"i\"postPointBits\"i}"
- "{?=QQQQ}48@0:8{?=QQQQ}16"
- "{PTFocus=ffffff}44@0:8@16f2428f36f40"
- "{half3x4=\"columns\"[3{half4=\"values\"[4 ]}]}"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xc8"

```
