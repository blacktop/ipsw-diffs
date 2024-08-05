## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

```diff

-802.88.0.0.0
-  __TEXT.__text: 0x54864
-  __TEXT.__auth_stubs: 0xca0
+802.97.1.0.0
+  __TEXT.__text: 0x55754
+  __TEXT.__auth_stubs: 0xcc0
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x8
-  __TEXT.__cstring: 0x1e4a0
-  __TEXT.__const: 0x11438
+  __TEXT.__cstring: 0x1e90c
+  __TEXT.__const: 0x11448
   __TEXT.__gcc_except_tab: 0x458
   __TEXT.__objc_methname: 0xb
-  __TEXT.__unwind_info: 0x5c8
-  __DATA_CONST.__auth_got: 0x660
-  __DATA_CONST.__got: 0x3d0
+  __TEXT.__unwind_info: 0x5d8
+  __DATA_CONST.__auth_got: 0x670
+  __DATA_CONST.__got: 0x440
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x2710
-  __DATA_CONST.__cfstring: 0x3a0
+  __DATA_CONST.__const: 0x2760
+  __DATA_CONST.__cfstring: 0x3c0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8
   __DATA.__data: 0x80

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 510
-  Symbols:   331
-  CStrings:  2341
+  Functions: 515
+  Symbols:   347
+  CStrings:  2367
 
Symbols:
+ _CMGetAttachment
+ _kFigCaptureSampleBufferAttachmentKey_MetadataDictionary
+ _kFigCaptureStreamMetadata_AGC
+ _kFigCaptureStreamMetadata_ExposureTime
+ _kFigCaptureStreamMetadata_LuxLevel
+ _kFigCaptureStreamMetadata_NormalizedSNR
+ _kFigCaptureStreamMetadata_PortType
+ _kFigCaptureStreamMetadata_SNR
+ _kFigCaptureStreamMetadata_ScalingFactor
+ _kFigCaptureStreamMetadata_SensorID
+ _kFigCaptureStreamMetadata_TemporalNoiseReductionBand0Strength
+ _kFigCaptureStreamMetadata_TemporalNoiseReductionBand0StrengthModulationEnabled
+ _kFigCaptureStreamMetadata_ispDGain
+ _kFigCaptureStreamMetadata_ispDGainRangeExpansionFactor
+ _kFigCaptureStreamMetadata_sensorDGain
+ _strcmp
CStrings:
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!p(MISSING) %!d(MISSING) Default FilterStrength %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!p(MISSING) %!d(MISSING) Default FilterStrength %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!p(MISSING) %!d(MISSING) PerFrameData.iDynamicStrength %!d(MISSING) bVNRApplied %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!p(MISSING) %!d(MISSING) PerFrameData.iDynamicStrength %!d(MISSING) bVNRApplied %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!p(MISSING) %!p(MISSING) %!d(MISSING) %!p(MISSING) sensorID %!f(MISSING) strength %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!p(MISSING) %!p(MISSING) %!d(MISSING) %!p(MISSING) sensorID %!f(MISSING) strength %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | AVE_MCTF_AdjustStrength failed %!p(MISSING) %!d(MISSING) %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | AVE_MCTF_AdjustStrength failed %!p(MISSING) %!d(MISSING) %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | wrong parameter %!p(MISSING) %!p(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | wrong parameter %!p(MISSING) %!p(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | wrong params, pMCTF = %!p(MISSING) %!p(MISSING) %!p(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | wrong params, pMCTF = %!p(MISSING) %!p(MISSING) %!p(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) SF: %!f(MISSING) Port: %!s(MISSING) %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) SF: %!f(MISSING) Port: %!s(MISSING) %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) iDebugFeature = %!l(MISSING)lu"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) iDebugFeature = %!l(MISSING)lu\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): (AVE_GetProperty_internal) Get Debug Feature: %!l(MISSING)lu\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): (AVE_GetProperty_internal) Get Debug Feature: %!l(MISSING)lu\n\n"
+ "(pMCTF != __null) && (psData != __null)"
+ "20:49:57"
+ "802.97.1"
+ "AVE_CFDict_GetDouble"
+ "AVE_ISP_GetMetadata"
+ "AVE_ISP_RetrieveMetadata"
+ "AVE_MCTF_AdjustStrength"
+ "Jul 30 2024"
+ "MachineLearningVideoNoiseReductionApplied"
+ "PortTypeBack"
+ "PortTypeBackSuperWide"
+ "PortTypeBackTelephoto"
+ "PortTypeFront"
+ "pDict != __null && pData != __null"
+ "pImgBuf != __null && pData != __null"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) iDebugFeature = %!l(MISSING)u"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) iDebugFeature = %!l(MISSING)u\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): (AVE_GetProperty_internal) Get Debug Feature: %!l(MISSING)u\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): (AVE_GetProperty_internal) Get Debug Feature: %!l(MISSING)u\n\n"
- "21:26:47"
- "802.88.0"
- "Jul 15 2024"

```
