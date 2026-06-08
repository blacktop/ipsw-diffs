## vImage

> `/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage`

```diff

-632.120.2.0.0
-  __TEXT.__text: 0x29dd50
-  __TEXT.__auth_stubs: 0x480
+649.0.0.0.0
+  __TEXT.__text: 0x29b640
   __TEXT.__delay_stubs: 0x780
   __TEXT.__delay_helper: 0x5a4
-  __TEXT.__const: 0x9a010
-  __TEXT.__cstring: 0x6acd
-  __TEXT.__unwind_info: 0x2378
-  __TEXT.__eh_frame: 0x27a8
-  __DATA_CONST.__got: 0xb0
+  __TEXT.__const: 0x99ef0
+  __TEXT.__cstring: 0x6ac7
+  __TEXT.__unwind_info: 0x2380
+  __TEXT.__eh_frame: 0x25d0
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x2f20
-  __AUTH_CONST.__auth_got: 0x330
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xbd88
+  __AUTH_CONST.__auth_got: 0x328
   __DATA.__data: 0x50
   __DATA.__common: 0x8
   __DATA.__bss: 0x10

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
