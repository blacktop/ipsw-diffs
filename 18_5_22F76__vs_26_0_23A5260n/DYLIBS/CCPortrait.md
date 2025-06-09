## CCPortrait

> `/System/Library/VideoProcessors/CCPortrait.bundle/CCPortrait`

```diff

-587.122.6.0.2
-  __TEXT.__text: 0x3dc98
+650.0.0.122.4
+  __TEXT.__text: 0x3d63c
   __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_methlist: 0x2a7c
+  __TEXT.__objc_methlist: 0x2b4c
   __TEXT.__const: 0x2c8
-  __TEXT.__gcc_except_tab: 0xba4
-  __TEXT.__cstring: 0x6c5e
-  __TEXT.__oslogstring: 0x1d4a
-  __TEXT.__unwind_info: 0x8c0
-  __TEXT.__objc_classname: 0x38d
-  __TEXT.__objc_methname: 0x7acf
-  __TEXT.__objc_methtype: 0x3072
-  __TEXT.__objc_stubs: 0x4b80
-  __DATA_CONST.__got: 0x3a0
+  __TEXT.__gcc_except_tab: 0x820
+  __TEXT.__cstring: 0x770b
+  __TEXT.__oslogstring: 0x1ca2
+  __TEXT.__unwind_info: 0x8d0
+  __TEXT.__objc_classname: 0x38b
+  __TEXT.__objc_methname: 0x7cc5
+  __TEXT.__objc_methtype: 0x33f8
+  __TEXT.__objc_stubs: 0x4a40
+  __DATA_CONST.__got: 0x390
   __DATA_CONST.__const: 0x1b8
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ca8
+  __DATA_CONST.__objc_selrefs: 0x1d30
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__auth_got: 0x430
   __AUTH_CONST.__const: 0x9c0
-  __AUTH_CONST.__cfstring: 0x52e0
-  __AUTH_CONST.__objc_const: 0x4ce8
+  __AUTH_CONST.__cfstring: 0x52a0
+  __AUTH_CONST.__objc_const: 0x4d88
   __AUTH_CONST.__objc_intobj: 0xb58
   __AUTH_CONST.__objc_floatobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x378
+  __DATA.__objc_ivar: 0x374
   __DATA.__data: 0x2b8
-  __DATA.__bss: 0xb8
+  __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0xb40
-  __DATA_DIRTY.__bss: 0xb8
+  __DATA_DIRTY.__bss: 0xe8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage
+  - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface

   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BA9A6E48-B168-3D7A-9A9B-FC7E3FE61E5F
-  Functions: 1240
-  Symbols:   358
-  CStrings:  3428
+  UUID: 65A023D3-1182-3C9D-9925-4A05E4C435A9
+  Functions: 1264
+  Symbols:   356
+  CStrings:  3549
 
Symbols:
+ _FigDebugAssert3
+ _FigSignalErrorAt3
- _OBJC_CLASS_$_MTLComputePipelineDescriptor
- ___stack_chk_fail
- ___stack_chk_guard
- _bzero
CStrings:
+ "!_inputAlpha || [_inputAlpha conformsToProtocol:@protocol(MTLTexture)]"
+ "!_inputAlpha || [_inputAlpha isKindOfClass:CIImage.class]"
+ "!_inputImage"
+ "!_inputImageChroma"
+ "!_inputImageLuma"
+ "!_outputImageChroma"
+ "!_outputImageLuma"
+ "%s assert: \"%s\" at %s (%s:%d) - %s%s(err=%d)"
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "%{public}s Unable to init metalContext for bundle %@"
+ "( -73465 )"
+ "(2 == [_fgSegmentArray count]) is NULL"
+ "(2 == [_segmentArray count]) is NULL"
+ "(Fig)"
+ "(_maxBlur > 0.0f) && (_maxBlur <= 1.0f)"
+ "+[UniDeviceCache findComputeKernel:metalContext:constants:]"
+ "-[UniKernel _findKernelInCache:metalContext:coreImageLibrary:constants:]"
+ "-[UniKernelInternal initWithName:metalContext:coreImageLibrary:constants:]"
+ "@\"<MTL4Archive>\"32@0:8@\"NSURL\"16^@24"
+ "@\"<MTL4ArgumentTable>\"32@0:8@\"MTL4ArgumentTableDescriptor\"16^@24"
+ "@\"<MTL4CommandAllocator>\"16@0:8"
+ "@\"<MTL4CommandAllocator>\"32@0:8@\"MTL4CommandAllocatorDescriptor\"16^@24"
+ "@\"<MTL4CommandBuffer>\"16@0:8"
+ "@\"<MTL4CommandQueue>\"16@0:8"
+ "@\"<MTL4CommandQueue>\"32@0:8@\"MTL4CommandQueueDescriptor\"16^@24"
+ "@\"<MTL4Compiler>\"32@0:8@\"MTL4CompilerDescriptor\"16^@24"
+ "@\"<MTL4CounterHeap>\"32@0:8@\"MTL4CounterHeapDescriptor\"16^@24"
+ "@\"<MTL4PipelineDataSetSerializer>\"24@0:8@\"MTL4PipelineDataSetSerializerDescriptor\"16"
+ "@\"<MTLBuffer>\"40@0:8Q16Q24q32"
+ "@\"<MTLFunctionHandle>\"24@0:8@\"<MTL4BinaryFunction>\"16"
+ "@\"<MTLFunctionHandle>\"24@0:8@\"<MTLFunction>\"16"
+ "@\"<MTLTensor>\"32@0:8@\"MTLTensorDescriptor\"16^@24"
+ "@\"<MTLTensor>\"40@0:8@\"MTLTensorDescriptor\"16Q24^@32"
+ "@\"<MTLTexture>\"24@0:8@\"MTLTextureViewDescriptor\"16"
+ "@\"<MTLTextureViewPool>\"32@0:8@\"MTLResourceViewPoolDescriptor\"16^@24"
+ "@\"FigMetalContext\""
+ "@40@0:8@16Q24^@32"
+ "@40@0:8Q16Q24q32"
+ "Couldn't validate arguments"
+ "Failed to extract rendering parameters"
+ "Fig"
+ "T@\"FigMetalContext\",&,N,VmetalContext"
+ "[_fgSegmentArray[0] isKindOfClass:[NSData class]] && [_fgSegmentArray[1] isKindOfClass:[NSData class]] is NULL"
+ "[_inputBlurMap conformsToProtocol:@protocol(MTLTexture)]"
+ "[_inputBlurMap isKindOfClass:CIImage.class]"
+ "[_inputHalfResRGTex conformsToProtocol:@protocol(MTLTexture)]"
+ "[_inputHalfResTex1 conformsToProtocol:@protocol(MTLTexture)]"
+ "[_inputHalfResTex1sRGB conformsToProtocol:@protocol(MTLTexture)]"
+ "[_inputHalfResTex2 conformsToProtocol:@protocol(MTLTexture)]"
+ "[_inputHalfResTex2sRGB conformsToProtocol:@protocol(MTLTexture)]"
+ "[_inputImage isKindOfClass:CIImage.class]"
+ "[_inputImageChroma conformsToProtocol:@protocol(MTLTexture)]"
+ "[_inputImageChroma isKindOfClass:CIImage.class]"
+ "[_inputImageLuma conformsToProtocol:@protocol(MTLTexture)]"
+ "[_inputImageLuma isKindOfClass:CIImage.class]"
+ "[_inputIntermediateTex conformsToProtocol:@protocol(MTLTexture)]"
+ "[_intermediates validateForMetal]"
+ "[_metadata isKindOfClass:NSData.class]"
+ "[_outputImageChroma conformsToProtocol:@protocol(MTLTexture)]"
+ "[_outputImageLuma conformsToProtocol:@protocol(MTLTexture)]"
+ "[_segmentArray[0] isKindOfClass:[NSData class]] && [_segmentArray[1] isKindOfClass:[NSData class]] is NULL"
+ "[args validateForCoreImage]"
+ "[args validateForMetal]"
+ "_addNoiseOnly is NULL"
+ "_antialiasRGBAX is NULL"
+ "_antialiasRGBAY is NULL"
+ "_antialiasX is NULL"
+ "_antialiasY is NULL"
+ "_blendRaytraced is NULL"
+ "_extractNegativeBlurValues is NULL"
+ "_extractPositiveBlurValues is NULL"
+ "_fgSegmentArray is NULL"
+ "_findKernelInCache:metalContext:coreImageLibrary:constants:"
+ "_gainmapMultiply is NULL"
+ "_highlightRecovery is NULL"
+ "_inputScale > 0.0f"
+ "_library is NULL"
+ "_localContrast is NULL"
+ "_lumaNoiseAmplitude >= 0.0f"
+ "_morphology is NULL"
+ "_prefilterX is NULL"
+ "_prefilterY is NULL"
+ "_preprocess is NULL"
+ "_preprocessScaled is NULL"
+ "_segmentArray is NULL"
+ "_simulatedAperture > 0.0"
+ "_sparseNoAlpha is NULL"
+ "_sparseNoAlphaRayFg is NULL"
+ "_sparseWithAlpha is NULL"
+ "_yuv1 is NULL"
+ "_yuv2 is NULL"
+ "bail"
+ "bundle is NULL"
+ "bundlePath"
+ "computePipelineStateFor:constants:"
+ "computePipelineStateFor:constants:additionnalPipelineOptions:reflection:"
+ "config_params is NULL"
+ "findComputeKernel:metalContext:constants:"
+ "functionHandleWithBinaryFunction:"
+ "functionHandleWithFunction:"
+ "image is NULL"
+ "image1As_sRGB is NULL"
+ "image2As_sRGB is NULL"
+ "imageRayFg is NULL"
+ "initWithName:metalContext:coreImageLibrary:constants:"
+ "initWithbundle:andOptionalCommandQueue:"
+ "inputAlpha is not valid"
+ "inputBlurMap is not valid"
+ "inputHalfResRGTex is not valid"
+ "inputHalfResTex1 is not valid"
+ "inputHalfResTex1sRGB is not valid"
+ "inputHalfResTex2 is not valid"
+ "inputHalfResTex2sRGB is not valid"
+ "inputImage is not valid"
+ "inputImage not expected"
+ "inputImageChroma is not valid"
+ "inputImageChroma not expected"
+ "inputImageLuma is not valid"
+ "inputImageLuma not expected"
+ "inputIntermediateTex is not valid"
+ "inputScale is not valid"
+ "intermediates not valid"
+ "lumaNoiseAmplitude is not valid"
+ "maxBlur is not valid"
+ "metadata is not valid"
+ "newArchiveWithURL:error:"
+ "newArgumentTableWithDescriptor:error:"
+ "newBufferWithLength:options:placementSparsePageSize:"
+ "newCommandAllocator"
+ "newCommandAllocatorWithDescriptor:error:"
+ "newCommandBuffer"
+ "newCompilerWithDescriptor:error:"
+ "newCounterHeapWithDescriptor:error:"
+ "newMTL4CommandQueue"
+ "newMTL4CommandQueueWithDescriptor:error:"
+ "newPipelineDataSetSerializerWithDescriptor:"
+ "newTensorWithDescriptor:error:"
+ "newTensorWithDescriptor:offset:error:"
+ "newTextureViewPoolWithDescriptor:error:"
+ "newTextureViewWithDescriptor:"
+ "outputImageChroma is not valid"
+ "outputImageChroma not expected"
+ "outputImageLuma is not valid"
+ "outputImageLuma not expected"
+ "queryTimestampFrequency"
+ "renderingParameters"
+ "self is NULL"
+ "setMetalContext:"
+ "simulatedAperture is not valid"
+ "sizeOfCounterHeapEntry:"
+ "sparseBufferTier"
+ "sparseTextureTier"
+ "tensorSizeAndAlignWithDescriptor:"
+ "{?=QQ}24@0:8@\"MTLTensorDescriptor\"16"
- "%{public}s Error = %@"
- "%{public}s Unable to create function %@; must be one of %s"
- "%{public}s Unable to load library for class %@ and hence associated function: _combineRGBAndAlpha"
- "%{public}s Unable to open %s metal libary"
- "(2 == [_fgSegmentArray count]) is NULL, (%s) at %s:%d"
- "(2 == [_segmentArray count]) is NULL, (%s) at %s:%d"
- "+[UniDeviceCache findComputeKernel:library:pipelineLibrary:constants:]"
- "-[UniKernel _findKernelInCache:metalLibrary:coreImageLibrary:pipelineLibrary:constants:]"
- "-[UniKernelInternal initWithName:metalLibrary:coreImageLibrary:pipelineLibrary:constants:]"
- "@\"<MTLLibrary>\""
- "@\"<MTLPipelineLibrarySPI>\""
- "@56@0:8@16@24@32@40@48"
- "Error compiling library: %@"
- "T@\"<MTLLibrary>\",&,Vlibrary"
- "T@\"<MTLPipelineLibrarySPI>\",&,N,VpipelineLibrary"
- "[_fgSegmentArray[0] isKindOfClass:[NSData class]] && [_fgSegmentArray[1] isKindOfClass:[NSData class]] is NULL, (%s) at %s:%d"
- "[_segmentArray[0] isKindOfClass:[NSData class]] && [_segmentArray[1] isKindOfClass:[NSData class]] is NULL, (%s) at %s:%d"
- "_findKernelInCache:metalLibrary:coreImageLibrary:pipelineLibrary:constants:"
- "default"
- "findComputeKernel:library:pipelineLibrary:constants:"
- "functionNames"
- "initWithName:metalLibrary:coreImageLibrary:pipelineLibrary:constants:"
- "newComputePipelineStateWithDescriptor:error:"
- "newFunctionWithName:constantValues:error:"
- "newFunctionWithName:constantValues:pipelineLibrary:error:"
- "newPipelineLibraryWithFilePath:error:"
- "pipelineLibrary"
- "resourcePath"
- "setComputeFunction:"
- "setLibrary:"
- "setPipelineLibrary:"

```
