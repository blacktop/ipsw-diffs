## AppleProResHWEncoder.videoencoder

> `/System/Library/VideoEncoders/AppleProResHWEncoder.videoencoder`

```diff

-500.55.0.0.0
-  __TEXT.__text: 0x1e3c0
-  __TEXT.__auth_stubs: 0xa70
+500.71.0.0.0
+  __TEXT.__text: 0x1e3fc
+  __TEXT.__auth_stubs: 0xa60
   __TEXT.__const: 0x741b0
-  __TEXT.__cstring: 0x121d
+  __TEXT.__cstring: 0x1223
   __TEXT.__gcc_except_tab: 0x308
-  __TEXT.__oslogstring: 0x2e8c
-  __TEXT.__unwind_info: 0x3d0
+  __TEXT.__oslogstring: 0x2ece
+  __TEXT.__unwind_info: 0x3c8
   __DATA_CONST.__got: 0x228
-  __AUTH_CONST.__auth_got: 0x540
+  __AUTH_CONST.__auth_got: 0x538
   __AUTH_CONST.__const: 0x188
   __AUTH_CONST.__cfstring: 0x240
   __DATA.__data: 0xb

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: EB0390DE-9290-3165-81A9-338F0A620516
-  Functions: 411
-  Symbols:   1210
-  CStrings:  353
+  UUID: 4C6744A8-96C6-387C-9F65-59348ADD0933
+  Functions: 413
+  Symbols:   1213
+  CStrings:  351
 
Symbols:
+ GCC_except_table35
+ GCC_except_table41
+ GCC_except_table44
+ GCC_except_table45
+ GCC_except_table49
+ GCC_except_table9
+ __Z16checkFrameHeaderP17ProResFrameHeaderb21ProRes_UserClientTypej.cold.16
+ __Z23reportEncodeSessionInfojjjjjhbjjjjbjjbbNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZL28ProResEncoder_GetInInfoSizesP37ProRes_EncodeFrame_UserKernel_In_InfojbffP16_APR_FeatureListhbPjjb
+ __ZL28ProResEncoder_GetInInfoSizesP37ProRes_EncodeFrame_UserKernel_In_InfojbffP16_APR_FeatureListhbPjjb.cold.1
+ __ZL28ProResEncoder_GetInInfoSizesP37ProRes_EncodeFrame_UserKernel_In_InfojbffP16_APR_FeatureListhbPjjb.cold.2
+ __ZL28ProResEncoder_GetInInfoSizesP37ProRes_EncodeFrame_UserKernel_In_InfojbffP16_APR_FeatureListhbPjjb.cold.3
+ __ZL28ProResEncoder_GetInInfoSizesP37ProRes_EncodeFrame_UserKernel_In_InfojbffP16_APR_FeatureListhbPjjb.cold.4
+ __ZN19ProResFrameReceiver26getNumFramesOverTargetSizeEv
+ __ZN19ProResFrameReceiver27getSumOfFramesOvershootPercEv
+ ____Z23reportEncodeSessionInfojjjjjhbjjjjbjjbbNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE_block_invoke
+ ___block_descriptor_tmp.31
- GCC_except_table10
- GCC_except_table2
- GCC_except_table33
- GCC_except_table39
- GCC_except_table42
- GCC_except_table43
- GCC_except_table47
- GCC_except_table6
- __Z15getHardwareTypePc
- __Z23reportEncodeSessionInfojjjjjhbjjbjjbbNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
- __ZL28ProResEncoder_GetInInfoSizesP37ProRes_EncodeFrame_UserKernel_In_InfojbffP16_APR_FeatureListhbjb
- __ZL28ProResEncoder_GetInInfoSizesP37ProRes_EncodeFrame_UserKernel_In_InfojbffP16_APR_FeatureListhbjb.cold.1
- __ZL28ProResEncoder_GetInInfoSizesP37ProRes_EncodeFrame_UserKernel_In_InfojbffP16_APR_FeatureListhbjb.cold.2
- __ZL28ProResEncoder_GetInInfoSizesP37ProRes_EncodeFrame_UserKernel_In_InfojbffP16_APR_FeatureListhbjb.cold.3
- __ZL28ProResEncoder_GetInInfoSizesP37ProRes_EncodeFrame_UserKernel_In_InfojbffP16_APR_FeatureListhbjb.cold.4
- ____Z23reportEncodeSessionInfojjjjjhbjjbjjbbNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE_block_invoke
- ___block_descriptor_tmp.36
- _sysctlbyname
CStrings:
+ "ERROR AppleProResHW (0x%x): %d: %s(): Unsupported RAW bayerPattern\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Unsupported RAW cfaPattern\n"
+ "avgTargetOvershootPercent"
+ "percentFramesOverTarget"
- "AppleTV"
- "ERROR AppleProResHW (0x%x): %d: %s(): Unsupported bayer_pattern %d\n"
- "hardwareType"
- "hw.machine"
- "iPad"
- "iPhone"

```
