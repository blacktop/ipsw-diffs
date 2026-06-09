## AccelerateGPU

> `/System/Library/PrivateFrameworks/AccelerateGPU.framework/AccelerateGPU`

```diff

 35.0.0.0.0
-  __TEXT.__text: 0x40c8 sha256:767f20b41e495116f783faa8956cb5a5ad725abca059e4e049c1c31bd4a383e7
-  __TEXT.__auth_stubs: 0x1e0 sha256:08847198a92115209bfb2d05620a570a89eaa28ce8ac3bcc1c7652ac5b56cc11
-  __TEXT.__gcc_except_tab: 0x83c sha256:f5e3c64cfcaae8f9bfd666d3544c7190b44c3583aa7a0219ab259375790b4510
+  __TEXT.__text: 0x4124 sha256:9c0a37e642c00b7bce131bee92f1c3bc7520ede2dc45926b99b5256089f0cfc3
+  __TEXT.__gcc_except_tab: 0x840 sha256:54cab008ccdf6ee60120052edcf65a3bb63afe678ccfd41a45d01124822a93a5
   __TEXT.__const: 0x58 sha256:78fb5cc629ad5af6159bd060c0e42ff70d37d578c8b8596960b59263694c3733
   __TEXT.__cstring: 0x82f sha256:2297cf122e213c0a4269ee528d5d2becefd1fe1cd3a08285e80900205b8132fc
-  __TEXT.__unwind_info: 0x190 sha256:ac02ba6c9c1a09c02852d053ace449e1006805a29b97fa3544f62bdcea426da9
-  __TEXT.__objc_methname: 0x3ac sha256:3ebb8bc3bc94344c2c114cd1af351c00dfb35b9e45b86d3289a490a7270ae8b0
-  __TEXT.__objc_stubs: 0x420 sha256:b739750deeadae7aa69e02e511d44e46d15b16e92cc25d0c06da0145b8500f28
-  __DATA_CONST.__got: 0x28 sha256:2c34ce1df23b838c5abf2a7f6437cca3d3067ed509ff25f11df6b11b582b51eb
-  __DATA_CONST.__const: 0x28 sha256:60ba0c1403ed75507d963a87d7a94f045a1ffecad96854a620f81063a892198c
+  __TEXT.__unwind_info: 0x190 sha256:900c8bd95312d78459b0d351e3a0e5d950404cba6f66c2ca3f53a70f34ccd97e
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
+  __DATA_CONST.__const: 0x28 sha256:758db769cb5c32d5ea77980f81e7c2df2a9a091e820f5c1bac6091feffa6f878
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x108 sha256:735bb0bec2e9810316af91fc6109fccc01ce9b1a366ea8613ff2d7b1a4bc810e
-  __AUTH_CONST.__auth_got: 0x100 sha256:5341e6b2646979a70e57653007a1f310169421ec9bdd9f1a5648f75ade005af1
-  __AUTH_CONST.__cfstring: 0x6e0 sha256:e9798f6f3307d208584cf5ead591809f91c472cdf2f96ee307eb8b52d5f97465
+  __DATA_CONST.__objc_selrefs: 0x108 sha256:2d54891559a672e80ec8233934187c49553bebc947674e598a274667242f8ddf
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__cfstring: 0x6e0 sha256:a94d2a2bd4c6d58e8702945497e03deb912973a47a858e596c647f55d3e302ee
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
~ _gpuImageBufferDestroy : sha256 87382d2563a33ea040e98d63f269cafbaba970879a8e6d58f1676d74e46633fe -> d2bdf807ed5f36a9905356f0caf4efa0545c62a5dc829286d4a4e581b0e2616f
~ _gpuImageBufferGetInfo : sha256 149df2827d6aa790a65cd11e2de6f83df355c930aa3955684e163a0f15ddd0f5 -> d1a410be8092cc19b7a55b2c2385fb0c2e3ecd39cb94342756ba8807c51133a3
~ _gpuImageBufferGetData : sha256 9cb56453d634589772a07cfc3b535958c9f26dad6375523c9196f8da235b2f0c -> 5e3c0514af15b100705f56c9e128716a4f8dcc01fa6a531cc0546fcdfd9dd91b
~ _gpuImageMatrixMultiply_ARGB8888 : 612 -> 620
~ _gpuImagePiecewisePolynomial_PlanarF : 548 -> 556
~ _gpuCreateSession : 3572 -> 3576
~ _gpuExecuteBlockBegin : 156 -> 148
~ _gpuExecuteBlockEnd : sha256 809411f910cbf3584f7c9a4d27fefd2c919e01fd2b9339971b4085bb8ac04520 -> 2656ea125470bdff52072cb8ec279b943f8d2f71dbdae12e6bdac91bce04ba2a
~ _gpuExecuteBlockEndWithCompletionHandler : 260 -> 272
~ _gpuImageRotate90_ARGB8888 : 1044 -> 1052
~ _gpuImagePiecewiseGamma_Planar8 : 556 -> 564
~ _gpuImagePiecewiseGamma_PlanarF : 372 -> 380
~ _gpuImageHistogramCalculation_ARGB8888 : 1140 -> 1152
~ _gpuImageConvert_ARGB8888toPlanar8 : 420 -> 428
~ _gpuImageConvert_Planar8toARGB8888 : 420 -> 428
~ _gpuImagePermuteChannels_ARGB8888 : sha256 d116ac345e0670456c174419c6ef80be3c1054328f5787d8dbcb79afcb178c5b -> 703c8a5f9f81960afce16e2a584f95c8c9c0f90cc90abea6bf6deff7803285cd
~ __ZL13gpuImageBlendPU34objcproto23MTLComputePipelineState11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectP16gpuImageBuffer_sS4_S4_13GPUImageFlags : sha256 6e6d48cd83f04447c625a2f514b7b9166d81031554198ee65a571037adea4729 -> c42b7e6498d7e51d7986165cd8138847dcb125ce0e7e6fab7eb11f86a22baac6
~ _gpuImagePremultipliedConstAlphaBlend_ARGB8888 : 156 -> 160
~ _gpuIsAppleFamily : sha256 416310029aaf98fb6808a5511f22e362ad138b24861f0a41e39881b1eb94042a -> 0db52f1a4439973a97f7abca7f6ee67299c77a12371e79129179b37c276f0233
~ _gpuGetLibrary : 224 -> 208
~ _gpuMaxBufferLength : sha256 de910ea54ddb12e68bcea040c04001b6ebd2566c1d135e78a408df01edfd1499 -> 4c758c5a1da99044d18d9de6a91ced61a69fcde45d1d9b346a216688a342a5b9
~ _gpuImageTentConvolve_ARGB8888 : 440 -> 448
~ __ZL32gpuImagePremultiplyUnpremultiplyPU34objcproto23MTLComputePipelineState11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectP16gpuImageBuffer_sS4_13GPUImageFlags : sha256 2f843d140ebf2bd60675b80f10cf614a5aefc1e1e51353a2b34cf709391cbd7d -> efeb0c7a0c20cbb0cfda2e6ec3ad7c9fd7e2c1b050a8ef40fdada89f45537cef
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
