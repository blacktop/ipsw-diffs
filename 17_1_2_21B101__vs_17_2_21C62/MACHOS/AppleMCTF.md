## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

```diff

-703.40.1.0.0
-  __TEXT.__text: 0xe7ac0
+703.54.1.0.0
+  __TEXT.__text: 0xe9760
   __TEXT.__auth_stubs: 0xeb0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__cstring: 0x637c1
-  __TEXT.__const: 0x10798
+  __TEXT.__cstring: 0x640c5
+  __TEXT.__const: 0x107a8
   __TEXT.__gcc_except_tab: 0x1fc
-  __TEXT.__unwind_info: 0x748
+  __TEXT.__unwind_info: 0x76c
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x760
   __DATA_CONST.__got: 0x8a8
   __DATA_CONST.__auth_ptr: 0x30
   __DATA_CONST.__const: 0x2300
-  __DATA_CONST.__cfstring: 0x2320
+  __DATA_CONST.__cfstring: 0x23c0
   __DATA.__data: 0x20
-  __DATA.__bss: 0x5c8
+  __DATA.__bss: 0x5d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo

   - /System/Library/PrivateFrameworks/OpticalFlowFramework.framework/OpticalFlowFramework
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 615
+  Functions: 622
   Symbols:   561
-  CStrings:  6217
+  CStrings:  6269
 
CStrings:
+ "%lld %d AVE %s: %s:%d %s | CreateOutputVQMetricsFile Error: *pOutFile != NULL \n"
+ "%lld %d AVE %s: %s:%d %s | CreateOutputVQMetricsFile Error: *pOutFile != NULL \n\n"
+ "%lld %d AVE %s: %s:%d %s | FIG: AVE_PrepareHEVCLevel failed"
+ "%lld %d AVE %s: %s:%d %s | FIG: AVE_PrepareHEVCLevel failed\n"
+ "%lld %d AVE %s: %s:%d %s | FIG: Incorrect sHardQPRange [%d %d]"
+ "%lld %d AVE %s: %s:%d %s | FIG: Incorrect sHardQPRange [%d %d]\n"
+ "%lld %d AVE %s: %s:%d %s | FIG: Incorrect sSoftQPRange [%d %d]"
+ "%lld %d AVE %s: %s:%d %s | FIG: Incorrect sSoftQPRange [%d %d]\n"
+ "%lld %d AVE %s: %s:%d %s | WriteVQMetrics Error: pOutFile == NULL \n"
+ "%lld %d AVE %s: %s:%d %s | WriteVQMetrics Error: pOutFile == NULL \n\n"
+ "%lld %d AVE %s: %s:%d %s | fail to create CFNumber %p %lf %p"
+ "%lld %d AVE %s: %s:%d %s | fail to create CFNumber %p %lf %p\n"
+ "%lld %d AVE %s: %s:%d %s | wrong parameter %p %lf %p"
+ "%lld %d AVE %s: %s:%d %s | wrong parameter %p %lf %p\n"
+ "%lld %d AVE %s: %s:%d kVTCompressionProperty_SoftMinH264QuantizationParameter is deprecated, please use kVTCompressionProperty_SoftMinQuantizationParameter"
+ "%lld %d AVE %s: %s:%d kVTCompressionProperty_SoftMinH264QuantizationParameter is deprecated, please use kVTCompressionProperty_SoftMinQuantizationParameter\n"
+ "%lld %d AVE %s: %s:%d | Enter %d"
+ "%lld %d AVE %s: %s:%d | Enter %d\n"
+ "%lld %d AVE %s: %s:%d | Exit %d | %d"
+ "%lld %d AVE %s: %s:%d | Exit %d | %d\n"
+ "%lld %d AVE %s: %s:%d | could not open file %s | %d \n"
+ "%lld %d AVE %s: %s:%d | could not open file %s | %d \n\n"
+ "%lld %d AVE %s: %s:%d | opened file %s to write | %d\n"
+ "%lld %d AVE %s: %s:%d | opened file %s to write | %d\n\n"
+ "%lld %d AVE %s: %s:%d | write VQMetrics failed %p %d | %d \n"
+ "%lld %d AVE %s: %s:%d | write VQMetrics failed %p %d | %d \n\n"
+ "%lld %d AVE %s: %s:%d | write VQMetrics(PSNR, MSE, SSIM) to file %p %d | %d\n"
+ "%lld %d AVE %s: %s:%d | write VQMetrics(PSNR, MSE, SSIM) to file %p %d | %d\n\n"
+ "%lld %d AVE %s: FIG: HEVCLevel %d incompatible with other settings (min should be %d)"
+ "%lld %d AVE %s: FIG: HEVCLevel %d incompatible with other settings (min should be %d)\n"
+ "%lld %d AVE %s: FIG: HEVCLevel received (%d) is too high... consider lowering it with these settings (min should be %d)"
+ "%lld %d AVE %s: FIG: HEVCLevel received (%d) is too high... consider lowering it with these settings (min should be %d)\n"
+ "%lld %d AVE %s: FIG: asked for AVE_kVTCompressionPropertyKey_CalculateMeanSquaredError return %s"
+ "%lld %d AVE %s: FIG: asked for AVE_kVTCompressionPropertyKey_CalculateMeanSquaredError return %s\n"
+ "%lld %d AVE %s: FIG: iCalculateMeanSquaredError = %s"
+ "%lld %d AVE %s: FIG: iCalculateMeanSquaredError = %s\n"
+ "%lld %d AVE %s: FIG: iQP = %u"
+ "%lld %d AVE %s: FIG: iQP = %u\n"
+ "%lld %d AVE %s: FIG: received AVE_kVTCompressionPropertyKey_CalculateMeanSquaredError"
+ "%lld %d AVE %s: FIG: received AVE_kVTCompressionPropertyKey_CalculateMeanSquaredError\n"
+ "%lld %d AVE %s: sRCParams.sHardQPRange.iMax %d"
+ "%lld %d AVE %s: sRCParams.sHardQPRange.iMax %d\n"
+ "%lld %d AVE %s: sRCParams.sHardQPRange.iMin %d"
+ "%lld %d AVE %s: sRCParams.sHardQPRange.iMin %d\n"
+ "*pOutFile == __null"
+ "-VQMetrics.txt"
+ "AVE_AddSupportedProperty(PropertyDictionary, kVTPropertyType_Boolean, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"CalculateMeanSquaredError\" \"\")), false)"
+ "AVE_CFArray_AddDouble"
+ "AVE_CFDict_AddDouble"
+ "AVE_DumpFeature"
+ "AVE_Dump_CreateOutputVQMetricsFile"
+ "AVE_Dump_WriteVQMetrics"
+ "AVE_HardMaxQP"
+ "AVE_HardMinQP"
+ "AVE_SoftMaxQP"
+ "AVE_SoftMinQP"
+ "CalculateMeanSquaredError"
+ "ChromaBlueMeanSquaredError"
+ "ChromaRedMeanSquaredError"
+ "CreateQualityMetricsDictionary"
+ "DBUG_DumpObjectiveMeasurements"
+ "FrameID %d: MSE(Y/U/V) %5.2f, %5.2f, %5.2f    PSNR(Y/U/V) %5.2f, %5.2f, %5.2f \n"
+ "LumaMeanSquaredError"
+ "QualityMetrics"
+ "pChromaBlueMeanSquaredErrorArr != __null"
+ "pChromaRedMeanSquaredErrorArr != __null"
+ "pLumaMeanSquaredErrorArr != __null"
+ "pQualityMetricsDict != __null"
- "%lld %d AVE %s: %s:%d %s | FIG: Incorrect QP range %d %d"
- "%lld %d AVE %s: %s:%d %s | FIG: Incorrect QP range %d %d\n"
- "%lld %d AVE %s: %s:%d kVTCompressionProperty_MaxQuantizationParameter is deprecated, please use kVTCompressionPropertyKey_MaxAllowedFrameQP"
- "%lld %d AVE %s: %s:%d kVTCompressionProperty_MaxQuantizationParameter is deprecated, please use kVTCompressionPropertyKey_MaxAllowedFrameQP\n"
- "%lld %d AVE %s: %s:%d kVTCompressionProperty_SoftMaxQuantizationParameter is deprecated, please use kVTCompressionPropertyKey_MaxAllowedFrameQP"
- "%lld %d AVE %s: %s:%d kVTCompressionProperty_SoftMaxQuantizationParameter is deprecated, please use kVTCompressionPropertyKey_MaxAllowedFrameQP\n"
- "%lld %d AVE %s: %s:%d kVTCompressionProperty_SoftMinH264QuantizationParameter is deprecated, please use kVTCompressionPropertyKey_MinAllowedFrameQP"
- "%lld %d AVE %s: %s:%d kVTCompressionProperty_SoftMinH264QuantizationParameter is deprecated, please use kVTCompressionPropertyKey_MinAllowedFrameQP\n"
- "%lld %d AVE %s: %s:%d kVTCompressionProperty_SoftMinQuantizationParameter is deprecated, please use kVTCompressionPropertyKey_MinAllowedFrameQP"
- "%lld %d AVE %s: %s:%d kVTCompressionProperty_SoftMinQuantizationParameter is deprecated, please use kVTCompressionPropertyKey_MinAllowedFrameQP\n"
- "%lld %d AVE %s: sRCParams.sQPRange.iMax %d"
- "%lld %d AVE %s: sRCParams.sQPRange.iMax %d\n"
- "%lld %d AVE %s: sRCParams.sQPRange.iMin %d"
- "%lld %d AVE %s: sRCParams.sQPRange.iMin %d\n"
- "AVE_MaxQP"
- "AVE_MinQP"

```
