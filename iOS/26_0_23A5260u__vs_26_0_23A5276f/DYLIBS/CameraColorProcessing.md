## CameraColorProcessing

> `/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`

```diff

-650.0.0.122.4
-  __TEXT.__text: 0x84140
+655.0.0.122.4
+  __TEXT.__text: 0x82f2c
   __TEXT.__auth_stubs: 0x780
   __TEXT.__objc_methlist: 0x1d64
   __TEXT.__const: 0x694c
-  __TEXT.__gcc_except_tab: 0x4848
-  __TEXT.__cstring: 0x7d3e
+  __TEXT.__gcc_except_tab: 0x4838
+  __TEXT.__cstring: 0x7d8e
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__oslogstring: 0xb1dd
-  __TEXT.__unwind_info: 0xb68
+  __TEXT.__oslogstring: 0xaf11
+  __TEXT.__unwind_info: 0xb60
   __TEXT.__eh_frame: 0x90
   __TEXT.__objc_classname: 0x43d
-  __TEXT.__objc_methname: 0x4935
+  __TEXT.__objc_methname: 0x4922
   __TEXT.__objc_methtype: 0xc26b
-  __TEXT.__objc_stubs: 0x2be0
+  __TEXT.__objc_stubs: 0x2bc0
   __DATA_CONST.__got: 0x438
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_classlist: 0xc8

   __DATA_CONST.__objc_arraydata: 0x280
   __AUTH_CONST.__auth_got: 0x3d8
   __AUTH_CONST.__const: 0x430
-  __AUTH_CONST.__cfstring: 0x2a00
-  __AUTH_CONST.__objc_const: 0x4968
+  __AUTH_CONST.__cfstring: 0x28c0
+  __AUTH_CONST.__objc_const: 0x4948
   __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x454
+  __DATA.__objc_ivar: 0x450
   __DATA.__data: 0xfe8
   __DATA.__common: 0x420
   __DATA_DIRTY.__objc_data: 0x500

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 221F7A86-CD47-376E-A546-9DC0AD7B974B
-  Functions: 1007
-  Symbols:   3558
-  CStrings:  3070
+  UUID: 29177C0A-C1A4-34D5-B64F-37A498475677
+  Functions: 994
+  Symbols:   3530
+  CStrings:  3037
 
Symbols:
+ -[HazeProperties haze_threshold_divider]
+ -[HazeProperties setHaze_threshold_divider:]
+ _OBJC_IVAR_$_AWBStatistics._fitWbTmRGBToANSTInputPipelineState
+ _OBJC_IVAR_$_AWBStatistics._resizeANSTPipelineState
+ _OBJC_IVAR_$_HazeProperties._haze_threshold_divider
+ ___block_literal_global.146
+ ___block_literal_global.210
+ _objc_msgSend$haze_threshold_divider
+ _objc_msgSend$setHaze_threshold_divider:
- -[AWBStatistics _createShaders].cold.8
- -[HazeEstimation hazePropertiesForLTM]
- -[HazeEstimation setHazePropertiesForLTM:]
- -[LTMProcessor initWithCommandQueue:].cold.9
- -[LTMProcessor setDehazeTuningParamsFrom:].cold.11
- -[LTMProcessor setDehazeTuningParamsFrom:].cold.12
- -[LTMProcessor setDehazeTuningParamsFrom:].cold.13
- -[LTMProcessor setDehazeTuningParamsFrom:].cold.14
- -[LTMProcessor setDehazeTuningParamsFrom:].cold.15
- -[LTMProcessor setDehazeTuningParamsFrom:].cold.16
- -[LTMProcessor setDehazeTuningParamsFrom:].cold.17
- -[LTMProcessor setDehazeTuningParamsFrom:].cold.18
- -[LTMProcessor setDehazeTuningParamsFrom:].cold.19
- _OBJC_IVAR_$_AWBStatistics._computeAWBStatsBayerPipelineState
- _OBJC_IVAR_$_AWBStatistics._fitWbTmRGBToANSTInput
- _OBJC_IVAR_$_AWBStatistics._resizeANST
- _OBJC_IVAR_$_HazeEstimation._hazePropertiesForLTM
- ___block_literal_global.150
- ___block_literal_global.211
- _objc_msgSend$hazePropertiesForLTM
- _objc_msgSend$hazeValueForLTM
- _objc_msgSend$setHazePropertiesForLTM:
CStrings:
+ "( imageTexInfo.flags & MTLPixelFormatFlagsIsFloatCompatible )"
+ "SoftAWB::awbStatsBayerFast"
+ "SoftAWB::awbStatsQuadraFast"
+ "SoftAWB::fitWbTmRGBToANSTInput"
+ "SoftAWB::normTileStats"
+ "SoftAWB::normWindowStats"
+ "SoftAWB::resetMtlBuffer"
+ "SoftAWB::resizeANST"
+ "Tf,N,V_haze_threshold_divider"
+ "Unexpected pipeline configuration, expected: fast pipeline and floating point input format, found: precise pipeline and fixed point input format?"
+ "_fitWbTmRGBToANSTInputPipelineState"
+ "_haze_threshold_divider"
+ "_resizeANSTPipelineState"
+ "haze_threshold_divider"
+ "kCMBaseObjectError_UnsupportedOperation"
+ "setHaze_threshold_divider:"
- "\t\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf6"
- "<<<< LTMAlgorithm >>>> %s: --- Haze estimation for LTM ---"
- "<<<< LTMAlgorithm >>>> %s: Could not read min_display_black_forLTM field"
- "<<<< LTMAlgorithm >>>> %s: Could not read reluC2_forLTM field"
- "<<<< LTMAlgorithm >>>> %s: Could not read reluC3_forLTM field"
- "<<<< LTMAlgorithm >>>> %s: Could not read reluC4_forLTM field"
- "<<<< LTMAlgorithm >>>> %s: Could not read reluC5_forLTM field"
- "<<<< LTMAlgorithm >>>> %s: Could not read sr_min_forLTM field"
- "<<<< LTMAlgorithm >>>> %s: Could not read sr_pow_forLTM field"
- "<<<< LTMAlgorithm >>>> %s: Could not read sr_sat_forLTM field"
- "<<<< LTMAlgorithm >>>> %s: Could not read sr_var_forLTM field"
- "<<<< LTMAlgorithm >>>> %s: The properties hazePropertiesForLTM.* not present in a plist"
- "T@\"HazeProperties\",&,N,V_hazePropertiesForLTM"
- "_computeAWBStatsBayerPipelineState"
- "_fitWbTmRGBToANSTInput"
- "_hazeEstimator.hazePropertiesForLTM"
- "_hazeEstimator.hazePropertiesForLTM is NULL"
- "_hazePropertiesForLTM"
- "_resizeANST"
- "awbStatsBayer"
- "awbStatsBayerFast"
- "awbStatsQuadraFast"
- "fitWbTmRGBToANSTInput"
- "hazePropertiesForLTM"
- "min_display_black_forLTM"
- "normTileStats"
- "normWindowStats"
- "reluC1_forLTM"
- "reluC2_forLTM"
- "reluC3_forLTM"
- "reluC4_forLTM"
- "reluC5_forLTM"
- "resetMtlBuffer"
- "resizeANST"
- "setHazePropertiesForLTM:"
- "sr_min_forLTM"
- "sr_pow_forLTM"
- "sr_sat_forLTM"
- "sr_var_forLTM"

```
