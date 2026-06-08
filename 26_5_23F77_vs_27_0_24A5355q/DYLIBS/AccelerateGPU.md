## AccelerateGPU

> `/System/Library/PrivateFrameworks/AccelerateGPU.framework/AccelerateGPU`

```diff

 35.0.0.0.0
-  __TEXT.__text: 0x40c8
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__gcc_except_tab: 0x83c
+  __TEXT.__text: 0x4124
+  __TEXT.__gcc_except_tab: 0x840
   __TEXT.__const: 0x58
   __TEXT.__cstring: 0x82f
   __TEXT.__unwind_info: 0x190
-  __TEXT.__objc_methname: 0x3ac
-  __TEXT.__objc_stubs: 0x420
-  __DATA_CONST.__got: 0x28
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x108
-  __AUTH_CONST.__auth_got: 0x100
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x6e0
+  __AUTH_CONST.__auth_got: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Metal.framework/Metal
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 395D6C04-3B9C-32BA-BCD0-503F63D611D8
+  UUID: AF983728-BA58-3E29-8181-65CA71DB29D2
   Functions: 39
-  Symbols:   132
-  CStrings:  144
+  Symbols:   131
+  CStrings:  111
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_storeStrong
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x27
Functions:
~ _gpuImageBufferCreate : 232 -> 224
~ _gpuImageMatrixMultiply_ARGB8888 : 612 -> 620
~ _gpuImagePiecewisePolynomial_PlanarF : 548 -> 556
~ _gpuCreateSession : 3572 -> 3576
~ _gpuExecuteBlockBegin : 156 -> 148
~ _gpuExecuteBlockEndWithCompletionHandler : 260 -> 272
~ _gpuImageRotate90_ARGB8888 : 1044 -> 1052
~ _gpuImagePiecewiseGamma_Planar8 : 556 -> 564
~ _gpuImagePiecewiseGamma_PlanarF : 372 -> 380
~ _gpuImageHistogramCalculation_ARGB8888 : 1140 -> 1152
~ _gpuImageConvert_ARGB8888toPlanar8 : 420 -> 428
~ _gpuImageConvert_Planar8toARGB8888 : 420 -> 428
~ _gpuImagePremultipliedConstAlphaBlend_ARGB8888 : 156 -> 160
~ _gpuGetLibrary : 224 -> 208
~ _gpuImageTentConvolve_ARGB8888 : 440 -> 448
~ _gpuImageConvolution_ARGB8888 : 1268 -> 1284
~ _gpuImageSeparableConvolution_ARGB8888 : 1696 -> 1704
~ _gpuImageBoxConvolve_ARGB8888 : 1800 -> 1804
CStrings:
- "URLWithString:"
- "addCompletedHandler:"
- "blitCommandEncoder"
- "bundleWithIdentifier:"
- "commandBuffer"
- "commit"
- "commitAndWaitUntilSubmitted"
- "computeCommandEncoderWithDispatchType:"
- "contents"
- "copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:"
- "dispatchThreadgroups:threadsPerThreadgroup:"
- "dispatchThreads:threadsPerThreadgroup:"
- "endEncoding"
- "maxBufferLength"
- "maxTotalThreadsPerThreadgroup"
- "minimumLinearTextureAlignmentForPixelFormat:"
- "newBufferWithBytesNoCopy:length:options:deallocator:"
- "newBufferWithLength:options:"
- "newCommandQueue"
- "newComputePipelineStateWithFunction:error:"
- "newFunctionWithName:"
- "newLibraryWithURL:error:"
- "newTextureWithDescriptor:offset:bytesPerRow:"
- "pathForResource:ofType:"
- "setBuffer:offset:atIndex:"
- "setBytes:length:atIndex:"
- "setComputePipelineState:"
- "setTexture:atIndex:"
- "setThreadgroupMemoryLength:atIndex:"
- "stringByResolvingSymlinksInPath"
- "texture2DDescriptorWithPixelFormat:width:height:mipmapped:"
- "threadExecutionWidth"
- "waitUntilCompleted"

```
