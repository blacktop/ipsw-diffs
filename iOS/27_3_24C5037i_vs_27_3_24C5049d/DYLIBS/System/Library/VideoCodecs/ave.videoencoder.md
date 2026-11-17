## ave.videoencoder

> `/System/Library/VideoCodecs/ave.videoencoder`

```diff

-913.64.1.0.0
-  __TEXT.__text: 0x174db4
+913.72.1.0.0
+  __TEXT.__text: 0x174f14
   __TEXT.__init_offsets: 0xc
   __TEXT.__const: 0x2534c
   __TEXT.__gcc_except_tab: 0x6e8
-  __TEXT.__cstring: 0x4d6fa
+  __TEXT.__cstring: 0x4d7ca
   __TEXT.__unwind_info: 0x1980
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libobjc.A.dylib
   Functions: 1547
   Symbols:   2353
-  CStrings:  6416
+  CStrings:  6419
 
Functions:
~ __Z29AVE_Session_HEVC_StartSessionP19_S_AVE_Session_HEVCP16_S_AVE_Dimension : 2584 -> 2592
~ __Z15AVE_HEVC_EncodeP19_S_AVE_Session_HEVCP25OpaqueVTVideoEncoderFrameP10__CVBufferP11_S_AVE_RectP14_S_AVE_TimeExtS8_PK14__CFDictionaryi : 10232 -> 10276
~ __Z24AVE_HEVC_ST_RPS_RetrievePK14__CFDictionaryP19HEVC_SHORT_TERM_RPS : 1364 -> 1388
~ __Z16AVE_DRL_RetrievePK9__CFArrayP14_S_AVE_DRL_Cfg : 508 -> 724
~ __Z34AVE_Session_HEVC_ProcessMultiFrameP19_S_AVE_Session_HEVCP25OpaqueVTVideoEncoderFrameP25OpaqueCMTaggedBufferGroupP11_S_AVE_RectP14_S_AVE_TimeExtS8_PK14__CFDictionary : 2972 -> 2976
~ __Z23AVE_MCTF_AdjustStrengthPK19_S_AVE_ISP_MetadataS1_14_E_AVE_DevType20_E_AVE_MCTF_WorkModePiP24_E_AVE_MCTF_ParamSetTypeS4_S4_ : 3640 -> 3652
~ __Z16AVE_DLB_ParseCfgPKcP14_S_AVE_DLB_Cfg : 756 -> 800
CStrings:
+ "%lld %d AVE %s: %s:%d %s | AVE_MCTF_AdjustStrength failed %p %p %lld %d %d"
+ "%lld %d AVE %s: %s:%d %s | AVE_MCTF_AdjustStrength failed %p %p %lld %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | too many DRL entries %d (max %d)"
+ "%lld %d AVE %s: %s:%d %s | too many DRL entries %d (max %d)\n"
+ "913.72.1"
+ "num <= 2"
+ "pInfo->num_negative_pics <= 16 && pInfo->num_positive_pics <= 16 && (pInfo->num_negative_pics + pInfo->num_positive_pics) <= 16"
- "%lld %d AVE %s: %s:%d %s | AVE_MCTF_AdjustStrength failed %p %p %lld %d"
- "%lld %d AVE %s: %s:%d %s | AVE_MCTF_AdjustStrength failed %p %p %lld %d\n"
- "913.64.1"
- "pInfo->num_negative_pics <= 16 && pInfo->num_positive_pics <= 16"
```
