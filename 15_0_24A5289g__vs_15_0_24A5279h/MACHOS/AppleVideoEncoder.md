## AppleVideoEncoder

> `/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/Contents/MacOS/AppleVideoEncoder`

```diff

-802.61.1.0.0
-  __TEXT.__text: 0xdf13c
+802.37.1.0.0
+  __TEXT.__text: 0xe28ec
   __TEXT.__auth_stubs: 0xf00
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x8
-  __TEXT.__cstring: 0x58f87
-  __TEXT.__const: 0x15948
+  __TEXT.__cstring: 0x59b1a
+  __TEXT.__const: 0x130f8
   __TEXT.__gcc_except_tab: 0x5cc
   __TEXT.__objc_methname: 0xb
-  __TEXT.__unwind_info: 0x7d0
+  __TEXT.__unwind_info: 0x7d8
   __DATA_CONST.__auth_got: 0x790
-  __DATA_CONST.__got: 0x8f8
+  __DATA_CONST.__got: 0x8f0
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x2ea8
+  __DATA_CONST.__const: 0x2bc0
   __DATA_CONST.__cfstring: 0x2500
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8
-  __DATA.__data: 0xb8
-  __DATA.__bss: 0x8c8
+  __DATA.__data: 0xb0
+  __DATA.__bss: 0x688
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/Versions/A/CoreVideo

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 691
-  Symbols:   542
-  CStrings:  5686
+  Functions: 682
+  Symbols:   541
+  CStrings:  5717
 
Symbols:
+ _kVTCompressionPropertyKey_ClientPID
+ _thread_info
- _CFDictionaryCreateMutableCopy
- _kVTCompressionPropertyKey_MaxFrameDelayCount
- _kVTVideoEncoder_IsHardwareAccelerated
CStrings:
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | AVE_HEVCNewDefaultsBasedOnProfileUsageDefault failed"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | AVE_HEVCNewDefaultsBasedOnProfileUsageDefault failed\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | FIG: Invalid Quality %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | FIG: Invalid Quality %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | FIG: Property ThroughputRateMode supported only on H.265 codec. Failed."
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | FIG: Property ThroughputRateMode supported only on H.265 codec. Failed.\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | FIG: pEncoderPrivateStorage = NULL."
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | FIG: pEncoderPrivateStorage = NULL.\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | FIG: pEncoderPrivateStorage == NULL"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | FIG: pEncoderPrivateStorage == NULL\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | FIG: pEncoderPrivateStorage->VideoParams.bMultiViewDepth = %!d(MISSING) and pEncoderPrivateStorage->VideoParams.bMultiViewDisparity = %!d(MISSING) -> fail."
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | FIG: pEncoderPrivateStorage->VideoParams.bMultiViewDepth = %!d(MISSING) and pEncoderPrivateStorage->VideoParams.bMultiViewDisparity = %!d(MISSING) -> fail.\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | OF: AVE_ValidateEncoderParameters failed, err = %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | OF: AVE_ValidateEncoderParameters failed, err = %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | fail to get refernce buffers %!p(MISSING) %!p(MISSING) %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | fail to get refernce buffers %!p(MISSING) %!p(MISSING) %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | invalid VideoLayerID in taggedBuffer %!d(MISSING) %!d(MISSING) %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | invalid VideoLayerID in taggedBuffer %!d(MISSING) %!d(MISSING) %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | mismatch VideoLayerID %!d(MISSING) in taggedBuffer"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | mismatch VideoLayerID %!d(MISSING) in taggedBuffer\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | wrong paramter %!p(MISSING) %!p(MISSING) %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | wrong paramter %!p(MISSING) %!p(MISSING) %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) Quality set with wrong RC mode %!d(MISSING) %!p(MISSING) %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) Quality set with wrong RC mode %!d(MISSING) %!p(MISSING) %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): AVE FIG WARINING: kCVImageBufferChromaLocationTopFieldKey with invalid value -> use default"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): AVE FIG WARINING: kCVImageBufferChromaLocationTopFieldKey with invalid value -> use default\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: ClientPID = %!u(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: ClientPID = %!u(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: EnableVariableB = %!s(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: EnableVariableB = %!s(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: NonDroppableFrameRate/BaseLayerFrameRate set and ExpectedFrameRate less than NonDroppableFrameRate defaulting expected frame rate to NonDroppableFrameRate value"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: NonDroppableFrameRate/BaseLayerFrameRate set and ExpectedFrameRate less than NonDroppableFrameRate defaulting expected frame rate to NonDroppableFrameRate value\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: NumberOfTemporalLayers value is not optimal. Overriding with optimal value."
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: NumberOfTemporalLayers value is not optimal. Overriding with optimal value.\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: ThroughputRateMode = %!u(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: ThroughputRateMode = %!u(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: asked for AVE_kVTCompressionPropertyKey_EnableVariableB return %!s(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: asked for AVE_kVTCompressionPropertyKey_EnableVariableB return %!s(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: asked for kVTCompressionPropertyKey_ClientPID return %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: asked for kVTCompressionPropertyKey_ClientPID return %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: asked for kVTCompressionPropertyKey_MaximumRealtimeFrameRate return %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: asked for kVTCompressionPropertyKey_MaximumRealtimeFrameRate return %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: iInitialQP = (%!d(MISSING),%!d(MISSING),%!d(MISSING)) and bIsLossless is true not supported. Set them to 0."
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: iInitialQP = (%!d(MISSING),%!d(MISSING),%!d(MISSING)) and bIsLossless is true not supported. Set them to 0.\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: iMaximumRealtimeFrameRate = %!u(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: iMaximumRealtimeFrameRate = %!u(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: received ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"MaximumRealtimeFrameRate\" \"\"))"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: received ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"MaximumRealtimeFrameRate\" \"\"))\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: received AVE_kVTCompressionPropertyKey_EnableVariableB"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: received AVE_kVTCompressionPropertyKey_EnableVariableB\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: received kVTCompressionPropertyKey_ClientPID"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: received kVTCompressionPropertyKey_ClientPID\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): H264FrameRec: f %!d(MISSING) currentPriority %!d(MISSING) thread %!p(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): H264FrameRec: f %!d(MISSING) currentPriority %!d(MISSING) thread %!p(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): H264FrameRec: f %!d(MISSING) invalid_policy threadBasicInfo.policy %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): H264FrameRec: f %!d(MISSING) invalid_policy threadBasicInfo.policy %!d(MISSING)\n"
+ "((pEncoderPrivateStorage->SPSHevcParams.bit_depth_luma_minus8 == 0) && (pEncoderPrivateStorage->SPSHevcParams.bit_depth_chroma_minus8 == 0))"
+ "((pEncoderPrivateStorage->SPSHevcParams.bit_depth_luma_minus8 == 2) && (pEncoderPrivateStorage->SPSHevcParams.bit_depth_chroma_minus8 == 2))"
+ "(codecType == kCMVideoCodecType_HEVC)"
+ "(pEncoderPrivateStorage->VideoParams.input_bitdepth == 8) || (pEncoderPrivateStorage->VideoParams.input_bitdepth == 10)"
+ "(psFwStats != __null) && (pSVEMap != __null)"
+ "20:47:01"
+ "802.37.1"
+ "AVE_AddSupportedProperty(PropertyDictionary, kVTPropertyType_Boolean, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"EnableVariableB\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionary, kVTPropertyType_Number, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"MaximumRealtimeFrameRate\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionary, kVTPropertyType_Number, kVTCompressionPropertyKey_ClientPID, false)"
+ "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Number, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"MaximumRealtimeFrameRate\" \"\")), false)"
+ "AVE_AttachMVStats"
+ "AVE_AverageNonDroppableFramerate"
+ "AVE_BaseLayerFrameRate"
+ "AVE_ClientPID"
+ "AVE_Cpmu2"
+ "AVE_Cpmu5"
+ "AVE_Cpmu6"
+ "AVE_Cpmu7"
+ "AVE_DPM_MODE"
+ "AVE_DbgInternalParams"
+ "AVE_Deblock"
+ "AVE_EnableHWEventTrace"
+ "AVE_EnableQPModChroma"
+ "AVE_EnableRCFW"
+ "AVE_EnableStaticAreasLowQP"
+ "AVE_EntropySelection"
+ "AVE_FrameRateTargetForBitrate"
+ "AVE_HEVCNewDefaultsBasedOnProfileUsageDefault"
+ "AVE_HevcSplitDecision"
+ "AVE_HighSpeedAndFastDRAMAtStartUp"
+ "AVE_MaximumRealtimeFrameRate"
+ "AVE_MultiReferencePSpacing"
+ "AVE_NumMergeCandidates"
+ "AVE_NumTemporalLayers"
+ "AVE_OverrideSNR"
+ "AVE_ThroughputRateMode"
+ "AVE_UsageMode"
+ "EnableVariableB"
+ "Jun 20 2024"
+ "MaximumRealtimeFrameRate"
+ "pEncoderPrivateStorage->VideoParams.sSliceMap.iNum != 0"
+ "pEncoderPrivateStorage->VideoParams.sSliceMap.iNum <= ((32) < (256) ? (32) : (256))"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING) Enter %!f(MISSING) %!p(MISSING)"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING) Enter %!f(MISSING) %!p(MISSING)\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING) Exit %!f(MISSING) %!p(MISSING) %!d(MISSING)"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING) Exit %!f(MISSING) %!p(MISSING) %!d(MISSING)\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | AddSEIDebugMetadata: SEI buffer overflow. pSEISize:%!d(MISSING)"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | AddSEIDebugMetadata: SEI buffer overflow. pSEISize:%!d(MISSING)\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | FIG: Invalid Quality %!f(MISSING)"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | FIG: Invalid Quality %!f(MISSING)\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | OF: AVE_USL_Drv_Start failed, err = %!d(MISSING)"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | OF: AVE_USL_Drv_Start failed, err = %!d(MISSING)\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | fail to get reference buffers %!p(MISSING) %!p(MISSING) %!d(MISSING)"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | fail to get reference buffers %!p(MISSING) %!p(MISSING) %!d(MISSING)\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | invalid VideoLayerID in taggedBuffer %!d(MISSING) %!d(MISSING) %!p(MISSING)"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | invalid VideoLayerID in taggedBuffer %!d(MISSING) %!d(MISSING) %!p(MISSING)\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | mismatch VideoLayerID %!l(MISSING)ld in taggedBuffer"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | mismatch VideoLayerID %!l(MISSING)ld in taggedBuffer\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) Quality set with wrong RC mode %!f(MISSING) %!p(MISSING) %!d(MISSING)"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) Quality set with wrong RC mode %!f(MISSING) %!p(MISSING) %!d(MISSING)\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: Enable WP required Async mode. Force to disable WP"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: Enable WP required Async mode. Force to disable WP\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: asked for kVTCompressionPropertyKey_MaxFrameDelayCount return %!d(MISSING)"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: asked for kVTCompressionPropertyKey_MaxFrameDelayCount return %!d(MISSING)\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: asked for kVTCompressionPropertyKey_MaximumRealTimeFrameRate return %!d(MISSING)"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: asked for kVTCompressionPropertyKey_MaximumRealTimeFrameRate return %!d(MISSING)\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: iMaximumRealTimeFrameRate = %!u(MISSING)"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: iMaximumRealTimeFrameRate = %!u(MISSING)\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: iThroughputMode = %!u(MISSING)"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: iThroughputMode = %!u(MISSING)\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: received ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"MaximumRealTimeFrameRate\" \"\"))"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: received ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"MaximumRealTimeFrameRate\" \"\"))\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): MultiRef and WP not supported together. Disabling MultiRef."
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): MultiRef and WP not supported together. Disabling MultiRef.\n"
- "(codecType == kCMVideoCodecType_HEVC || codecType == kFigVideoCodecType_HEVC_WirelessDisplayEncrypted)"
- "(psFwStats != __null) && (pEUMap != __null)"
- "22:10:13"
- "802.61.1"
- "AVE_AddSupportedProperty(PropertyDictionary, kVTPropertyType_Boolean, kVTCompressionPropertyKey_MaxFrameDelayCount, false)"
- "AVE_AddSupportedProperty(PropertyDictionary, kVTPropertyType_Number, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"MaximumRealTimeFrameRate\" \"\")), false)"
- "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Number, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"MaximumRealTimeFrameRate\" \"\")), false)"
- "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Number, kVTCompressionPropertyKey_SourceFrameCount, false)"
- "AVE_BFrameNum"
- "AVE_BaseFrameRate"
- "AVE_DLB_Cfg"
- "AVE_DPM_Mode"
- "AVE_DeblockMode"
- "AVE_ExpectedFrameRate"
- "AVE_FrameRateTargetForAverageBitrate"
- "AVE_LookAheadFrameCount"
- "AVE_MaximumRealTimeFrameRate"
- "AVE_MergeCandidateNum"
- "AVE_SEIFeatureOff"
- "AVE_SEIFeatureOn"
- "AVE_SNR"
- "AVE_TemporalLayerNum"
- "AVE_ThroughputMode"
- "AVE_Usage"
- "AVE_VBVInitialDelay"
- "EntropyCodingHeader"
- "GGM"
- "Jul  1 2024"
- "LowResRefChroma"
- "LowResRefChromaHeader"
- "LowResRefLumaHeader"
- "MaximumRealTimeFrameRate"
- "SLOW"
- "ULTRA"
- "ULTRA1"
- "com.apple.videotoolbox.videoencoder.ohvc"

```
