## AccelerateGPU

> `/System/Library/PrivateFrameworks/AccelerateGPU.framework/AccelerateGPU`

```diff

 35.0.0.0.0
-  __TEXT.__text: 0x40a0
-  __TEXT.__auth_stubs: 0x1d0
-  __TEXT.__gcc_except_tab: 0x860
-  __TEXT.__const: 0x30
+  __TEXT.__text: 0x40c8
+  __TEXT.__auth_stubs: 0x1e0
+  __TEXT.__gcc_except_tab: 0x83c
+  __TEXT.__const: 0x58
   __TEXT.__cstring: 0x82f
   __TEXT.__unwind_info: 0x190
   __TEXT.__objc_methname: 0x3ac

   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x108
-  __AUTH_CONST.__auth_got: 0xf8
+  __AUTH_CONST.__auth_got: 0x100
   __AUTH_CONST.__cfstring: 0x6e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EA1C0976-F150-3BCD-8086-5A487B281FE7
+  UUID: 74DD2121-5AF8-3A8E-A68F-14EBCE30B5C0
   Functions: 39
-  Symbols:   131
+  Symbols:   132
   CStrings:  144
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x27
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
- _objc_storeStrong
Functions:
~ _gpuImageBufferCreate : 224 -> 232
~ _gpuImageMatrixMultiply_ARGB8888 : 620 -> 612
~ _gpuImagePiecewisePolynomial_PlanarF : 556 -> 548
~ _gpuCreateSession : 3564 -> 3572
~ _gpuExecuteBlockBegin : 148 -> 156
~ _gpuExecuteBlockEndWithCompletionHandler : 272 -> 260
~ _gpuImageRotate90_ARGB8888 : 1040 -> 1044
~ _gpuImagePiecewiseGamma_Planar8 : 564 -> 556
~ _gpuImagePiecewiseGamma_PlanarF : 380 -> 372
~ _gpuImageHistogramCalculation_ARGB8888 : 1124 -> 1140
~ _gpuImageConvert_ARGB8888toPlanar8 : 428 -> 420
~ _gpuImageConvert_Planar8toARGB8888 : 428 -> 420
~ _gpuImagePremultipliedConstAlphaBlend_ARGB8888 : 160 -> 156
~ _gpuGetLibrary : 208 -> 224
~ _gpuImageConvolution_ARGB8888 : 1284 -> 1268
~ _gpuImageSeparableConvolution_ARGB8888 : 1644 -> 1696
~ _gpuImageBoxConvolve_ARGB8888 : 1792 -> 1800

```
