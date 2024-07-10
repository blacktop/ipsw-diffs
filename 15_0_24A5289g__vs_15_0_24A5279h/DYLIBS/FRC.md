## FRC

> `/System/Library/PrivateFrameworks/FRC.framework/Versions/A/FRC`

```diff

-213.0.0.0.0
-  __TEXT.__text: 0x301b8
+210.0.0.0.0
+  __TEXT.__text: 0x2ff4c
   __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_methlist: 0x283c
+  __TEXT.__objc_methlist: 0x27e4
   __TEXT.__const: 0x558
-  __TEXT.__cstring: 0x485b
-  __TEXT.__oslogstring: 0x449
-  __TEXT.__gcc_except_tab: 0x128
-  __TEXT.__unwind_info: 0x910
+  __TEXT.__cstring: 0x480e
+  __TEXT.__oslogstring: 0x42c
+  __TEXT.__gcc_except_tab: 0x120
+  __TEXT.__unwind_info: 0x908
   __TEXT.__objc_classname: 0x311
-  __TEXT.__objc_methname: 0xa672
-  __TEXT.__objc_methtype: 0x3185
-  __TEXT.__objc_stubs: 0x5040
+  __TEXT.__objc_methname: 0xa506
+  __TEXT.__objc_methtype: 0x3174
+  __TEXT.__objc_stubs: 0x4fc0
   __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x210
+  __DATA_CONST.__const: 0x200
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19c0
+  __DATA_CONST.__objc_selrefs: 0x1988
   __DATA_CONST.__objc_superrefs: 0xf8
   __AUTH_CONST.__auth_got: 0x478
   __AUTH_CONST.__const: 0x448
-  __AUTH_CONST.__cfstring: 0x2f40
-  __AUTH_CONST.__objc_const: 0x7c90
+  __AUTH_CONST.__cfstring: 0x2ee0
+  __AUTH_CONST.__objc_const: 0x7bf0
   __AUTH.__objc_data: 0xbe0
-  __DATA.__objc_ivar: 0x948
+  __DATA.__objc_ivar: 0x938
   __DATA.__data: 0x140
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/Versions/A/IOSurfaceAccelerator
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1003
-  Symbols:   2825
-  CStrings:  541
+  Functions: 995
+  Symbols:   2809
+  CStrings:  538
 
Symbols:
+ GCC_except_table15
+ __115-[FRCFrameInterpolator interpolateBetweenFirstFrame:secondFrame:timeScales:outputSize:outputPixelFormat:withError:]_block_invoke.95
+ __115-[FRCFrameInterpolator interpolateBetweenFirstFrame:secondFrame:timeScales:outputSize:outputPixelFormat:withError:]_block_invoke.96
+ __115-[FRCFrameInterpolator interpolateBetweenFirstFrame:secondFrame:timeScales:outputSize:outputPixelFormat:withError:]_block_invoke.97
+ __115-[FRCFrameInterpolator interpolateBetweenFirstFrame:secondFrame:timeScales:outputSize:outputPixelFormat:withError:]_block_invoke.98
+ __115-[FRCFrameInterpolator interpolateBetweenFirstFrame:secondFrame:timeScales:outputSize:outputPixelFormat:withError:]_block_invoke.99
- -[FRCFrameInterpolator legacyNormalizationMode]
- -[FRCFrameInterpolator setLegacyNormalizationMode:]
- -[FRCFrameSynthesizer initWithUsage:qualityMode:useLegacyNormalization:]
- -[FRCImageProcessor initLegacyModeWithUsage:]
- -[FRCImageProcessor initWithUsage:normalizationMode:]
- -[FRCOpticalFlowEstimatorConfiguration legacyNormalization]
- -[FRCOpticalFlowEstimatorConfiguration setLegacyNormalization:]
- -[Normalization initWithMode:]
- GCC_except_table16
- GCC_except_table26
- OBJC_IVAR_$_FRCFrameInterpolator._legacyNormalizationMode
- OBJC_IVAR_$_FRCOpticalFlowEstimatorConfiguration._legacyNormalization
- OBJC_IVAR_$_Normalization._denormalizeYCbCr10UnpackedRenderKernel
- OBJC_IVAR_$_Normalization._disableSIMDSum
- __115-[FRCFrameInterpolator interpolateBetweenFirstFrame:secondFrame:timeScales:outputSize:outputPixelFormat:withError:]_block_invoke.104
- __115-[FRCFrameInterpolator interpolateBetweenFirstFrame:secondFrame:timeScales:outputSize:outputPixelFormat:withError:]_block_invoke.105
- __115-[FRCFrameInterpolator interpolateBetweenFirstFrame:secondFrame:timeScales:outputSize:outputPixelFormat:withError:]_block_invoke.106
- __115-[FRCFrameInterpolator interpolateBetweenFirstFrame:secondFrame:timeScales:outputSize:outputPixelFormat:withError:]_block_invoke.107
- __115-[FRCFrameInterpolator interpolateBetweenFirstFrame:secondFrame:timeScales:outputSize:outputPixelFormat:withError:]_block_invoke.108
- _objc_msgSend$initLegacyModeWithUsage:
- _objc_msgSend$initWithUsage:normalizationMode:
- _objc_msgSend$initWithUsage:qualityMode:useLegacyNormalization:
- _objc_msgSend$legacyNormalization
CStrings:
+ "[FRC] Session started successfully [usage:%!d(MISSING) (%!l(MISSING)dx%!l(MISSING)d), tiling:%!d(MISSING), 1/4 flow:%!d(MISSING), synthesis:%!d(MISSING), concurrent flow:%!d(MISSING), twoStage:%!d(MISSING), self Norm: %!d(MISSING), temporal filtering: %!d(MISSING), linear splatting: %!d(MISSING), flow adaptation: %!d(MISSING), flow revision: %!d(MISSING)]\n"
- "Input buffer is NULL"
- "Invalid input parameters."
- "[FRC] Session started successfully [usage:%!d(MISSING) (%!l(MISSING)dx%!l(MISSING)d), quality:%!d(MISSING), tiling:%!d(MISSING), 1/4 flow:%!d(MISSING), synthesis:%!d(MISSING), concurrent flow:%!d(MISSING), twoStage:%!d(MISSING), self Norm: %!d(MISSING), temporal filtering: %!d(MISSING), linear splatting: %!d(MISSING), flow adaptation: %!d(MISSING), flow revision: %!d(MISSING)]\n"
- "timeScale is NULL"

```
