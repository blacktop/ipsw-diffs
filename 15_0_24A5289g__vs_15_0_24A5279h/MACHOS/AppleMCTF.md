## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/Contents/MacOS/AppleMCTF`

```diff

-802.61.1.0.0
-  __TEXT.__text: 0x54af8
-  __TEXT.__auth_stubs: 0xc90
+802.37.1.0.0
+  __TEXT.__text: 0x5592c
+  __TEXT.__auth_stubs: 0xca0
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x8
-  __TEXT.__cstring: 0x1daee
-  __TEXT.__const: 0x11438
+  __TEXT.__cstring: 0x1e122
+  __TEXT.__const: 0xecc8
   __TEXT.__gcc_except_tab: 0x458
   __TEXT.__objc_methname: 0xb
-  __TEXT.__unwind_info: 0x5d8
-  __DATA_CONST.__auth_got: 0x658
-  __DATA_CONST.__got: 0x3d0
+  __TEXT.__unwind_info: 0x5d0
+  __DATA_CONST.__auth_got: 0x660
+  __DATA_CONST.__got: 0x410
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x2700
+  __DATA_CONST.__const: 0x2478
   __DATA_CONST.__cfstring: 0x3a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8
-  __DATA.__data: 0x80
-  __DATA.__bss: 0x8d0
+  __DATA.__data: 0x78
+  __DATA.__bss: 0x690
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/Versions/A/CoreVideo

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 512
-  Symbols:   330
-  CStrings:  2338
+  Functions: 501
+  Symbols:   339
+  CStrings:  2362
 
Symbols:
+ _kCVImageBufferChromaLocationBottomFieldKey
+ _kCVImageBufferChromaLocationTopFieldKey
+ _kCVImageBufferChromaLocation_Bottom
+ _kCVImageBufferChromaLocation_BottomLeft
+ _kCVImageBufferChromaLocation_Center
+ _kCVImageBufferChromaLocation_Left
+ _kCVImageBufferChromaLocation_Top
+ _kCVImageBufferChromaLocation_TopLeft
+ _thread_info
CStrings:
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | fail to get refernce buffers %!p(MISSING) %!p(MISSING) %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | fail to get refernce buffers %!p(MISSING) %!p(MISSING) %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | wrong paramter %!p(MISSING) %!p(MISSING) %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | wrong paramter %!p(MISSING) %!p(MISSING) %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): AVE FIG WARINING: kCVImageBufferChromaLocationTopFieldKey with invalid value -> use default"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): AVE FIG WARINING: kCVImageBufferChromaLocationTopFieldKey with invalid value -> use default\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: Unknown dynamic range"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: Unknown dynamic range\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: chroma_loc_info_present_flag %!d(MISSING) , chroma_sample_loc_type_top_field %!d(MISSING), chroma_sample_loc_type_bottom_field %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: chroma_loc_info_present_flag %!d(MISSING) , chroma_sample_loc_type_top_field %!d(MISSING), chroma_sample_loc_type_bottom_field %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: chroma_loc_info_present_flag TRUE"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: chroma_loc_info_present_flag TRUE\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: chroma_sample_loc_type_top_field %!d(MISSING), chroma_sample_loc_type_bottom_field %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: chroma_sample_loc_type_top_field %!d(MISSING), chroma_sample_loc_type_bottom_field %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: kCVImageBufferChromaLocationBottomFieldKey found!"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: kCVImageBufferChromaLocationBottomFieldKey found!\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: kCVImageBufferChromaLocationTopFieldKey found!"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: kCVImageBufferChromaLocationTopFieldKey found!\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: video_full_range_flag %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): FIG: video_full_range_flag %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): H264FrameRec: f %!d(MISSING) currentPriority %!d(MISSING) thread %!p(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): H264FrameRec: f %!d(MISSING) currentPriority %!d(MISSING) thread %!p(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): H264FrameRec: f %!d(MISSING) invalid_policy threadBasicInfo.policy %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): H264FrameRec: f %!d(MISSING) invalid_policy threadBasicInfo.policy %!d(MISSING)\n"
+ "(psFwStats != __null) && (pSVEMap != __null)"
+ "20:47:39"
+ "802.37.1"
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
+ "AVE_HevcSplitDecision"
+ "AVE_HighSpeedAndFastDRAMAtStartUp"
+ "AVE_MaximumRealtimeFrameRate"
+ "AVE_MultiReferencePSpacing"
+ "AVE_NumMergeCandidates"
+ "AVE_NumTemporalLayers"
+ "AVE_OverrideSNR"
+ "AVE_ThroughputRateMode"
+ "AVE_UsageMode"
+ "Jun 20 2024"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | AddSEIDebugMetadata: SEI buffer overflow. pSEISize:%!d(MISSING)"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | AddSEIDebugMetadata: SEI buffer overflow. pSEISize:%!d(MISSING)\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | fail to get reference buffers %!p(MISSING) %!p(MISSING) %!d(MISSING)"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | fail to get reference buffers %!p(MISSING) %!p(MISSING) %!d(MISSING)\n"
- "(psFwStats != __null) && (pEUMap != __null)"
- "22:10:52"
- "802.61.1"
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

```
