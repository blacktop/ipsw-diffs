## AV1SW.videodecoder

> `/System/Library/VideoDecoders/AV1SW.videodecoder`

```diff

 158.5.0.0.0
-  __TEXT.__text: 0x9d610
-  __TEXT.__auth_stubs: 0x9a0
+  __TEXT.__text: 0x9ed0c
   __TEXT.__objc_methlist: 0xc8
-  __TEXT.__const: 0x14700
-  __TEXT.__gcc_except_tab: 0x744
+  __TEXT.__const: 0x14b30
+  __TEXT.__gcc_except_tab: 0x6cc
   __TEXT.__oslogstring: 0x69c
-  __TEXT.__cstring: 0x983
-  __TEXT.__unwind_info: 0x7f8
+  __TEXT.__cstring: 0x988
+  __TEXT.__unwind_info: 0x1d38
   __TEXT.__eh_frame: 0x3c8
-  __TEXT.__objc_classname: 0x11
-  __TEXT.__objc_methname: 0x758
-  __TEXT.__objc_methtype: 0x610
-  __TEXT.__objc_stubs: 0x660
-  __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0x800
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x818
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__objc_selrefs: 0x1b0
-  __AUTH_CONST.__auth_got: 0x4e0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__cfstring: 0x240
   __AUTH_CONST.__objc_const: 0x420
+  __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x4a8
   __DATA.__objc_ivar: 0x6c
   __DATA.__bss: 0x1c
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EBBD77CF-6D37-31DB-A608-1B73902D4BB3
-  Functions: 1702
-  Symbols:   225
-  CStrings:  254
+  UUID: 6DA43AED-1D26-3853-8BAF-1354112183D6
+  Functions: 1703
+  Symbols:   223
+  CStrings:  150
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x25
CStrings:
- ".cxx_construct"
- ".cxx_destruct"
- "@\"<MTLBuffer>\""
- "@\"<MTLCommandQueue>\""
- "@\"<MTLComputePipelineState>\""
- "@\"<MTLDevice>\""
- "@\"<MTLLibrary>\""
- "@\"<MTLTexture>\""
- "@16@0:8"
- "@32@0:8@16@24"
- "@32@0:8^{__CVBuffer=}16i24i28"
- "B"
- "B16@0:8"
- "TB,R,V_broken444"
- "Ti,R,V_maximumTextureDimension"
- "VCPAV1Metal"
- "[2{CF<__CVMetalTextureCache *>=\"value_\"^{__CVMetalTextureCache}}]"
- "_blitKernelChroma"
- "_blitKernelLuma"
- "_blitKernelUnorm"
- "_broken444"
- "_commandQueue"
- "_device"
- "_filmGrainChroma"
- "_filmGrainLuma"
- "_gpuBitdepth"
- "_grainPatch"
- "_grainTextureUV"
- "_grainTextureY"
- "_height"
- "_integerWrites"
- "_layout"
- "_library"
- "_maximumTextureDimension"
- "_offsets"
- "_offsetsStride"
- "_offsetsTex"
- "_onePixelPerWrite"
- "_openAttempted"
- "_scalingLUT"
- "_supportsNonUniformThreadgroup"
- "_textureCacheDst"
- "_textureCacheSrc"
- "_width"
- "applyFilmGrain:forPicture:toPixelBuffer:"
- "blitCommandEncoder"
- "broken444"
- "bundleForClass:"
- "commandBuffer"
- "commit"
- "compileBlitForPicture:andPixelBuffer:"
- "compileFilmGrainForPicture:andPixelBuffer:"
- "compileFunction:constantValues:"
- "computeCommandEncoder"
- "containsString:"
- "contents"
- "copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:"
- "copyPicture:toPixelBuffer:"
- "copyPixelBuffer:toPixelBuffer:"
- "dictionaryWithObjects:forKeys:count:"
- "dispatchThreadgroups:threadsPerThreadgroup:"
- "dispatchThreads:threadsPerThreadgroup:"
- "dstTexture:forPlane:bitdepth:"
- "encodeBlit:forPicture:toPixelBuffer:plane:"
- "endEncoding"
- "error"
- "fileURLWithPath:"
- "height"
- "i"
- "i16@0:8"
- "i32@0:8^{Dav1dPicture=^{Dav1dSequenceHeader}^{Dav1dFrameHeader}[3^v][2q]{Dav1dPictureParameters=iiii}{Dav1dDataProps=qqqQ{Dav1dUserData=*^{Dav1dRef}}}^{Dav1dContentLightLevel}^{Dav1dMasteringDisplay}^{Dav1dITUTT35}Q[4Q]^{Dav1dRef}^{Dav1dRef}^{Dav1dRef}^{Dav1dRef}^{Dav1dRef}[4Q]^{Dav1dRef}^v}16^{__CVBuffer=}24"
- "i32@0:8^{__CVBuffer=}16^{__CVBuffer=}24"
- "i40@0:8^v16^{Dav1dPicture=^{Dav1dSequenceHeader}^{Dav1dFrameHeader}[3^v][2q]{Dav1dPictureParameters=iiii}{Dav1dDataProps=qqqQ{Dav1dUserData=*^{Dav1dRef}}}^{Dav1dContentLightLevel}^{Dav1dMasteringDisplay}^{Dav1dITUTT35}Q[4Q]^{Dav1dRef}^{Dav1dRef}^{Dav1dRef}^{Dav1dRef}^{Dav1dRef}[4Q]^{Dav1dRef}^v}24^{__CVBuffer=}32"
- "length"
- "maximumTextureDimension"
- "metalIsSupported"
- "minimumLinearTextureAlignmentForPixelFormat:"
- "newBufferWithLength:options:"
- "newCommandQueue"
- "newComputePipelineStateWithFunction:error:"
- "newDefaultLibraryWithBundle:error:"
- "newFunctionWithName:"
- "newFunctionWithName:constantValues:error:"
- "newLibraryWithURL:error:"
- "newTextureWithDescriptor:"
- "newTextureWithDescriptor:offset:bytesPerRow:"
- "openDevice"
- "setBuffer:offset:atIndex:"
- "setBytes:length:atIndex:"
- "setComputePipelineState:"
- "setConstantValue:type:atIndex:"
- "setStorageMode:"
- "setTexture:atIndex:"
- "setUsage:"
- "srcTexture:forPlane:bitdepth:"
- "supportsFamily:"
- "texture2DDescriptorWithPixelFormat:width:height:mipmapped:"
- "updatePictureFormat:pixelBuffer:"
- "v16@0:8"
- "v32@0:8^{Dav1dPicture=^{Dav1dSequenceHeader}^{Dav1dFrameHeader}[3^v][2q]{Dav1dPictureParameters=iiii}{Dav1dDataProps=qqqQ{Dav1dUserData=*^{Dav1dRef}}}^{Dav1dContentLightLevel}^{Dav1dMasteringDisplay}^{Dav1dITUTT35}Q[4Q]^{Dav1dRef}^{Dav1dRef}^{Dav1dRef}^{Dav1dRef}^{Dav1dRef}[4Q]^{Dav1dRef}^v}16^{__CVBuffer=}24"
- "v44@0:8@16^{Dav1dPicture=^{Dav1dSequenceHeader}^{Dav1dFrameHeader}[3^v][2q]{Dav1dPictureParameters=iiii}{Dav1dDataProps=qqqQ{Dav1dUserData=*^{Dav1dRef}}}^{Dav1dContentLightLevel}^{Dav1dMasteringDisplay}^{Dav1dITUTT35}Q[4Q]^{Dav1dRef}^{Dav1dRef}^{Dav1dRef}^{Dav1dRef}^{Dav1dRef}[4Q]^{Dav1dRef}^v}24^{__CVBuffer=}32i40"
- "vendorName"
- "waitUntilCompleted"
- "width"

```
