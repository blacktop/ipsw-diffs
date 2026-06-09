## vImage

> `/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage`

```diff

-632.120.2.0.0
-  __TEXT.__text: 0x29dd50 sha256:ea5ec7164fe264286e289f493998a5505dfceb1e9b23e6f19cc67e294ef8b2cb
-  __TEXT.__auth_stubs: 0x480 sha256:71b8531d9b233a87c32cfe3ca25dd8e0ca3d2444bd75a88c5bfa88d26b61c8de
-  __TEXT.__delay_stubs: 0x780 sha256:52c6acfac23cb170ca8de7c5ba2cbea1d303457d73cef863139da789d001dfdb
-  __TEXT.__delay_helper: 0x5a4 sha256:840920fcdc6eedfaff3f469d6121ac5efd04aa59373fc327a1d24dca103c9b90
-  __TEXT.__const: 0x9a010 sha256:a852bb902e3001b83778c54428d3d38ce2917f14d818bf03701f29142f0f5beb
-  __TEXT.__cstring: 0x6acd sha256:ad895ec4206840dda7135965268e2ddfdeed15c44e53c60a01060150e106ef3e
-  __TEXT.__unwind_info: 0x2378 sha256:1a63e59142a6e992bb7a6c8aa722007ae04d9638ccc54955f48216dcfdc38241
-  __TEXT.__eh_frame: 0x27a8 sha256:3bca684f26600a2e00e7a18b9dec89188678cdc75620fa86dbe9e4fec357aad6
-  __DATA_CONST.__got: 0xb0 sha256:86d2cf5b090f43ee54d8f7c1dcf746a853951191457ff6dac96269a9d24860b9
-  __DATA_CONST.__const: 0x2f20 sha256:4080d6de4e5a07f1dc1aaa2558ad6396e65efefc1496f76652a26a80e3ed26c9
-  __AUTH_CONST.__auth_got: 0x330 sha256:0645a4a67dcec462dc9f335bb0564e6e39bf12ea7e40cf8de81418210102c2d1
-  __AUTH_CONST.__const: 0xbd88 sha256:403bff7c2ce2db319bb9add5a8d29a5f1e5fc1e7e8aafcf83932385492e3ad64
-  __DATA.__data: 0x50 sha256:5a227daf156b5c9471292a7a4aad14d3df793ad96702ce20d7f986eafa888107
+649.0.0.0.0
+  __TEXT.__text: 0x29b640 sha256:fa60a99cf35717485681f8af918674091b0cc243c7691aced31085cf32e73d26
+  __TEXT.__delay_stubs: 0x780 sha256:4e398ffb084c46d5ea43804ba643b8acb81b19662a7f74b36c274667917194c0
+  __TEXT.__delay_helper: 0x5a4 sha256:d839d6551e6116ce0a6d247abf6901bf13450b678d9958d893c229419a440687
+  __TEXT.__const: 0x99ef0 sha256:8946e6117c52718e3a3606d4a16939f5aca3ba32ed7703307409e74c74384547
+  __TEXT.__cstring: 0x6ac7 sha256:7edb8761d565f4cf8a6652266203ea408679e08029f845d6d3bef54b8e10f7d4
+  __TEXT.__unwind_info: 0x2380 sha256:169f6cc325390dbe86caf2be165746810208f3be3e710e7de803f88dcb0d8707
+  __TEXT.__eh_frame: 0x25d0 sha256:11d0923bbe43d569ce09a28afe88c2dc658267c290aa6190c7a74813d51d9a97
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x2f20 sha256:fa6f0dcc9ab3968cdc89217ca826fd0db44836d7bce494ae0d70f76f8ceea285
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0xbd88 sha256:4e8856569bb7392fd5ef56c39b108f1852218b8a910b0008e24915e13f3c3b4b
+  __AUTH_CONST.__auth_got: 0x328 sha256:33e15ec51f02d31aedb153489237b7938676d30e5a211a4498ae4910930e1a86
+  __DATA.__data: 0x50 sha256:f2731cf45f3bc55ec874f994d4fb6acc35566c2636a13db68b3134430d619065
   __DATA.__common: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
-  __DATA_DIRTY.__data: 0x118 sha256:5285815a31afc186c38e95827f771ee6bc8fc7f6e40c1916287fb27671f11d46
+  __DATA_DIRTY.__data: 0x118 sha256:c41c3c4498ce020f18b74ef9ac56854e00dc72e4ec47b69b8712d4685375336d
   __DATA_DIRTY.__bss: 0x290 sha256:e06e79cdfedfc6d6107b945613e65b2de3a209e40115b9b00ab048d2b91cd7d5
   __DATA_DIRTY.__common: 0x140 sha256:7b6436b0c98f62380866d9432c2af0ee08ce16a171bda6951aecd95ee1307d61
   - /System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/Libraries/libCGInterfaces.dylib

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
-  UUID: ED8B656D-BFA5-3984-B5B3-41D4320D6EFC
-  Functions: 3368
-  Symbols:   7208
+  UUID: 88A571DE-D99D-3D68-A517-71FEB6DF9257
+  Functions: 3334
+  Symbols:   7135
   CStrings:  404
 
Symbols:
+ _Init_CGInterfaces$loadHelper_x8
+ _gpuCreateSession$loadHelper_x8
+ _gpuImageAlphaBlend_ARGB8888$loadHelper_x8
+ _gpuImageConvert_ARGB8888toPlanar8$loadHelper_x8
+ _gpuImageConvert_Planar8toARGB8888$loadHelper_x8
+ _gpuImageMatrixMultiply_ARGB8888$loadHelper_x8
+ _gpuImagePermuteChannels_ARGB8888$loadHelper_x8
+ _gpuImagePiecewiseGamma_Planar8$loadHelper_x8
+ _gpuImagePiecewiseGamma_PlanarF$loadHelper_x8
+ _gpuImagePiecewisePolynomial_PlanarF$loadHelper_x8
+ _gpuImagePremultipliedAlphaBlend_ARGB8888$loadHelper_x8
+ _gpuImagePremultiplyData_ARGB8888$loadHelper_x8
+ _gpuImagePremultiplyData_RGBA8888$loadHelper_x8
+ _gpuImageRotate90_ARGB8888$loadHelper_x8
+ _gpuImageUnpremultiplyData_ARGB8888$loadHelper_x8
+ _gpuImageUnpremultiplyData_RGBA8888$loadHelper_x8
+ _vImage_malloc_typed
+ _vvpowf$loadHelper_x8
- ___sme_memset
- _gotLoadHelper_x8$_Init_CGInterfaces
- _gotLoadHelper_x8$_gpuCreateSession
- _gotLoadHelper_x8$_gpuImageAlphaBlend_ARGB8888
- _gotLoadHelper_x8$_gpuImageConvert_ARGB8888toPlanar8
- _gotLoadHelper_x8$_gpuImageConvert_Planar8toARGB8888
- _gotLoadHelper_x8$_gpuImageMatrixMultiply_ARGB8888
- _gotLoadHelper_x8$_gpuImagePermuteChannels_ARGB8888
- _gotLoadHelper_x8$_gpuImagePiecewiseGamma_Planar8
- _gotLoadHelper_x8$_gpuImagePiecewiseGamma_PlanarF
- _gotLoadHelper_x8$_gpuImagePiecewisePolynomial_PlanarF
- _gotLoadHelper_x8$_gpuImagePremultipliedAlphaBlend_ARGB8888
- _gotLoadHelper_x8$_gpuImagePremultiplyData_ARGB8888
- _gotLoadHelper_x8$_gpuImagePremultiplyData_RGBA8888
- _gotLoadHelper_x8$_gpuImageRotate90_ARGB8888
- _gotLoadHelper_x8$_gpuImageUnpremultiplyData_ARGB8888
- _gotLoadHelper_x8$_gpuImageUnpremultiplyData_RGBA8888
- _gotLoadHelper_x8$_vvpowf
- _vHorizontal_Reflect_ARGB_8888_SME2
- _vHorizontal_Reflect_ARGB_8888_SME2_internal
- _vHorizontal_Reflect_Planar_UInt16_SME2
- _vHorizontal_Reflect_Planar_UInt16_SME2_internal
- _vHorizontal_Reflect_Planar_UInt8_SME2
- _vHorizontal_Reflect_Planar_UInt8_SME2_internal
- _vHorizontal_Scale_ARGB_8888_SME_64x16
- _vHorizontal_Scale_ARGB_8888_SME_64x16_internal
- _vHorizontal_Scale_CbCr8_SME_64x16
- _vHorizontal_Scale_CbCr8_SME_64x16_internal
- _vHorizontal_Scale_Planar_UInt8_SME_64x16
- _vHorizontal_Scale_Planar_UInt8_SME_64x16_internal
- _vImage_malloc
- _vRotateClockwise270Degree_ARGB8888_SME2_internal
- _vRotateClockwise270Degree_UInt16_SME2
- _vRotateClockwise270Degree_UInt16_SME2_internal
- _vRotateClockwise270Degree_UInt8_SME2
- _vRotateClockwise270Degree_UInt8_SME2_internal
- _vRotateClockwise90Degree_ARGB8888_SME2_internal
- _vRotateClockwise90Degree_UInt16_SME2
- _vRotateClockwise90Degree_UInt16_SME2_internal
- _vRotateClockwise90Degree_UInt8_SME2
- _vRotateClockwise90Degree_UInt8_SME2_internal
- _vRotate_90_ARGB_8888_270Degree_SME2
- _vRotate_90_ARGB_8888_90Degree_SME2
- _vVertical_Reflect_ARGB_16S_SME2
- _vVertical_Reflect_ARGB_16U_SME2
- _vVertical_Reflect_ARGB_8888_SME2
- _vVertical_Reflect_ARGB_8888_SME2_internal
- _vVertical_Reflect_Planar_UInt8_SME2
- _vVertical_Reflect_Planar_UInt8_SME2_internal
- _vVertical_Scale_ARGB_8888_SME_64x16
- _vVertical_Scale_ARGB_8888_SME_64x16_internal
- _vVertical_Scale_CbCr8_SME_64x16
- _vVertical_Scale_CbCr8_SME_64x16_internal
- _vVertical_Scale_Planar_UInt8_SME_64x16
- _vVertical_Scale_Planar_UInt8_SME_64x16_internal
CStrings:
+ "649"
- "632.120.2"

```
