## VideoStabilizationV2

> `/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2`

```diff

-  __TEXT.__text: 0x59308
+  __TEXT.__text: 0x59f58
   __TEXT.__auth_stubs: 0xd60
-  __TEXT.__objc_stubs: 0x32c0
-  __TEXT.__objc_methlist: 0x1c04
-  __TEXT.__const: 0x700
-  __TEXT.__objc_methname: 0x5bb7
+  __TEXT.__objc_stubs: 0x3300
+  __TEXT.__objc_methlist: 0x1c44
+  __TEXT.__const: 0x6f0
+  __TEXT.__objc_methname: 0x5c7f
   __TEXT.__objc_classname: 0x1ee
   __TEXT.__objc_methtype: 0x191a
-  __TEXT.__cstring: 0x9725
-  __TEXT.__oslogstring: 0xf0c3
+  __TEXT.__cstring: 0x9784
+  __TEXT.__oslogstring: 0xf2d4
   __TEXT.__gcc_except_tab: 0x400
-  __TEXT.__unwind_info: 0x8a8
+  __TEXT.__unwind_info: 0x8b8
   __DATA_CONST.__const: 0x270
   __DATA_CONST.__cfstring: 0xa20
   __DATA_CONST.__objc_classlist: 0x88

   __DATA_CONST.__objc_dictobj: 0xc58
   __DATA_CONST.__objc_arrayobj: 0x2580
   __DATA_CONST.__auth_got: 0x6c0
-  __DATA_CONST.__got: 0x898
+  __DATA_CONST.__got: 0x8c0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x4508
-  __DATA.__objc_selrefs: 0xff0
-  __DATA.__objc_ivar: 0x4b0
+  __DATA.__objc_const: 0x4598
+  __DATA.__objc_selrefs: 0x1008
+  __DATA.__objc_ivar: 0x4bc
   __DATA.__objc_data: 0x550
   __DATA.__data: 0x300
   __DATA.__common: 0x60

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1424
-  Symbols:   2921
-  CStrings:  2912
+  Functions: 1430
+  Symbols:   2936
+  CStrings:  2927
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ -[VISConfigurationV2 setUndistortedOverscanEnabled:]
+ -[VISConfigurationV2 undistortedOverscanEnabled]
+ -[affineGPUMetal setUndistortedDimensions:height:]
+ GCC_except_table10
+ GCC_except_table18
+ GCC_except_table22
+ GCC_except_table27
+ GCC_except_table39
+ OBJC_IVAR_$_VISConfigurationV2._undistortedOverscanEnabled
+ OBJC_IVAR_$_affineGPUMetal._undistortedInputHeight
+ OBJC_IVAR_$_affineGPUMetal._undistortedInputWidth
+ _AffineTransformSetUndistortedInputSize
+ _kCVImageBufferColorPrimaries_ITU_R_2020
+ _kCVImageBufferYCbCrMatrix_ITU_R_2020
+ _kFigCaptureStreamGDCCoefficientsKey_PolynomialMax
+ _kFigVideoStabilizationSampleBufferAttachmentKey_StabilizationTransformsParameters
+ _kFigVideoStabilizationSampleBufferProcessorOption_UndistortedOverscanEnabled
+ _objc_msgSend$setUndistortedDimensions:height:
+ _objc_msgSend$undistortedOverscanEnabled
- GCC_except_table17
- GCC_except_table21
- GCC_except_table26
- GCC_except_table38
- GCC_except_table9
- _OUTLINED_FUNCTION_178
- _OUTLINED_FUNCTION_179
- _kFigVideoStabilizationSampleBufferAttachmentKey_GPUTransformsParameters
CStrings:
+ "-[affineGPUMetal setUndistortedDimensions:height:]"
+ "<<<< GyroVideoStabilizationV2 >>>> %s: Configuration: Overscan < 0, undistorted overscan enabled."
+ "<<<< GyroVideoStabilizationV2 >>>> %s: Options: UndistortedOverscanEnabled: %s"
+ "<<<< GyroVideoStabilizationV2 >>>> %s: Undistorted input dimensions: ( %d x %d ) derived from ( %d x %d )"
+ "<<<< GyroVideoStabilizationV2 >>>> %s: Undistorted overscan (per side): %d x %d"
+ "<<<< GyroVideoStabilizationV2 >>>> %s: Updated panning speed threshold: %f"
+ "<<<< affineGPUMetalV2 >>>> %s: Undistorted input width = %d, Undistorted input height = %d"
+ "TB,N,V_undistortedOverscanEnabled"
+ "_attachStabilizationParameters"
+ "_extractStabilizationParameters"
+ "_undistortedInputHeight"
+ "_undistortedInputWidth"
+ "_undistortedOverscanEnabled"
+ "sbp_computeUndistortedOverscanFromDistortionModel"
+ "setUndistortedDimensions:height:"
+ "setUndistortedOverscanEnabled:"
+ "storage->tmpStabilizationXformsParams"
+ "storage->undistortedOverscanRectEnabled"
+ "undistortedOverscanEnabled"
- "( overscanWidth >= 0 ) && ( overscanHeight >= 0 )"
- "_attachGPUStabilizationParameters"
- "_extractGPUStabilizationParameters"
- "storage->tmpGPUXformsParams"

```
