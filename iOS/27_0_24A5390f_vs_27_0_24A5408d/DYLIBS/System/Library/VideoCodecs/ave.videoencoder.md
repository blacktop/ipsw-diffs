## ave.videoencoder

> `/System/Library/VideoCodecs/ave.videoencoder`

```diff

-913.29.1.0.0
-  __TEXT.__text: 0x16fc0c
+913.43.1.0.0
+  __TEXT.__text: 0x172070
   __TEXT.__init_offsets: 0xc
-  __TEXT.__const: 0x252b4
+  __TEXT.__const: 0x25294
   __TEXT.__gcc_except_tab: 0x6e4
-  __TEXT.__cstring: 0x4c3fc
+  __TEXT.__cstring: 0x4c88d
   __TEXT.__unwind_info: 0xa48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__objc_selrefs: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x57d0
-  __AUTH_CONST.__cfstring: 0x3020
+  __AUTH_CONST.__const: 0x58d0
+  __AUTH_CONST.__cfstring: 0x3060
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__auth_got: 0x760
   __DATA.__data: 0x80
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0x1060
+  __DATA_DIRTY.__bss: 0x1068
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1527
-  Symbols:   2329
-  CStrings:  6329
+  Functions: 1535
+  Symbols:   2337
+  CStrings:  6353
 
Symbols:
+ __Z23AVE_MCTF_AdjustStrengthPK19_S_AVE_ISP_MetadataS1_14_E_AVE_DevType20_E_AVE_MCTF_WorkModePiP24_E_AVE_MCTF_ParamSetTypeS4_S4_
+ __Z25AVE_MCTF_DecideGatingTypeiiPK19_S_AVE_ISP_Metadata14_E_AVE_DevType20_E_AVE_MCTF_WorkMode16_E_AVE_MCTF_ModeP22_E_AVE_MCTF_GatingType
+ __Z29AVE_MCTF_DecidePreFiltAdjTypeiiPK19_S_AVE_ISP_Metadata14_E_AVE_DevType20_E_AVE_MCTF_WorkMode16_E_AVE_MCTF_ModeP26_E_AVE_MCTF_PreFiltAdjType
+ __Z30AVE_Prop_AVC_GetMCTFGatingTypePvS_PK13__CFAllocatorPK10__CFStringS_
+ __Z30AVE_Prop_AVC_SetMCTFGatingTypePvS_PK10__CFStringPKv
+ __Z31AVE_Prop_HEVC_GetMCTFGatingTypePvS_PK13__CFAllocatorPK10__CFStringS_
+ __Z31AVE_Prop_HEVC_SetMCTFGatingTypePvS_PK10__CFStringPKv
+ __Z34AVE_Prop_AVC_GetMCTFPreFiltAdjTypePvS_PK13__CFAllocatorPK10__CFStringS_
+ __Z34AVE_Prop_AVC_SetMCTFPreFiltAdjTypePvS_PK10__CFStringPKv
+ __Z35AVE_Prop_HEVC_GetMCTFPreFiltAdjTypePvS_PK13__CFAllocatorPK10__CFStringS_
+ __Z35AVE_Prop_HEVC_SetMCTFPreFiltAdjTypePvS_PK10__CFStringPKv
- __Z22AVE_MCTF_GetGatingTypePK19_S_AVE_ISP_Metadata14_E_AVE_DevType20_E_AVE_MCTF_WorkMode16_E_AVE_MCTF_ModeP22_E_AVE_MCTF_GatingType
- __Z23AVE_MCTF_AdjustStrengthPK19_S_AVE_ISP_Metadata14_E_AVE_DevType20_E_AVE_MCTF_WorkModePiP24_E_AVE_MCTF_ParamSetTypeS4_S4_
- __Z26AVE_MCTF_GetPreFiltAdjTypePK19_S_AVE_ISP_Metadata14_E_AVE_DevType20_E_AVE_MCTF_WorkMode16_E_AVE_MCTF_ModeP26_E_AVE_MCTF_PreFiltAdjType
CStrings:
+ "%lld %d AVE %s: %s Enter %d %d %p %d %d %d %p"
+ "%lld %d AVE %s: %s Enter %d %d %p %d %d %d %p\n"
+ "%lld %d AVE %s: %s Exit %d %d %p %d %d %d %p %d"
+ "%lld %d AVE %s: %s Exit %d %d %p %d %d %d %p %d\n"
+ "%lld %d AVE %s: %s fNumberChange: %.4f (%d) ->%.4f (%d), sID : %d -> %d DynamicStrength:0"
+ "%lld %d AVE %s: %s fNumberChange: %.4f (%d) ->%.4f (%d), sID : %d -> %d DynamicStrength:0\n"
+ "%lld %d AVE %s: %s:%d %p sID 0x%x gMode %d lMode %d gating type %d"
+ "%lld %d AVE %s: %s:%d %p sID 0x%x gMode %d lMode %d gating type %d\n"
+ "%lld %d AVE %s: %s:%d %p sID 0x%x gMode %d lMode %d prefilt adj type %d"
+ "%lld %d AVE %s: %s:%d %p sID 0x%x gMode %d lMode %d prefilt adj type %d\n"
+ "%lld %d AVE %s: %s:%d %p sID 0x%x noise level %d rIdx %d/%d strength %d"
+ "%lld %d AVE %s: %s:%d %p sID 0x%x noise level %d rIdx %d/%d strength %d\n"
+ "%lld %d AVE %s: %s:%d %s | AVE_MCTF_DecideGatingType failed %d"
+ "%lld %d AVE %s: %s:%d %s | AVE_MCTF_DecideGatingType failed %d\n"
+ "%lld %d AVE %s: %s:%d %s | AVE_MCTF_DecidePreFiltAdjType failed %d"
+ "%lld %d AVE %s: %s:%d %s | AVE_MCTF_DecidePreFiltAdjType failed %d\n"
+ "%lld %d AVE %s: %s:%d %s | HW does not support non-zero look ahead %p %lld %p %p %p %d"
+ "%lld %d AVE %s: %s:%d %s | HW does not support non-zero look ahead %p %lld %p %p %p %d\n"
+ "%lld %d AVE %s: %s:%d %s | wrong params, %d %d %p %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | wrong params, %d %d %p %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | wrong params, %d %p %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | wrong params, %d %p %d %d %d\n"
+ "%lld %d AVE %s: fail to send PS %p %p %d, dropping frame"
+ "%lld %d AVE %s: fail to send PS %p %p %d, dropping frame\n"
+ "913.43.1"
+ "AVE_MCTFFnumChangeResetMCTF"
+ "AVE_MCTFGatingType"
+ "AVE_MCTFPreFiltAdjType"
+ "AVE_MCTF_DecideGatingType"
+ "AVE_MCTF_DecidePreFiltAdjType"
+ "AVE_PROPERTY_KEY_MCTF_GATING_TYPE"
+ "AVE_PROPERTY_KEY_MCTF_PRE_FILT_ADJ_TYPE"
+ "AVE_Prop_AVC_GetMCTFGatingType"
+ "AVE_Prop_AVC_GetMCTFPreFiltAdjType"
+ "AVE_Prop_AVC_SetMCTFGatingType"
+ "AVE_Prop_AVC_SetMCTFPreFiltAdjType"
+ "AVE_Prop_HEVC_GetMCTFGatingType"
+ "AVE_Prop_HEVC_GetMCTFPreFiltAdjType"
+ "AVE_Prop_HEVC_SetMCTFGatingType"
+ "AVE_Prop_HEVC_SetMCTFPreFiltAdjType"
+ "MCTFGatingType"
+ "MCTFGatingType = %d\n"
+ "MCTFPreFiltAdjType"
+ "MCTFPreFiltAdjType = %d\n"
+ "iGatingType >= -1 && iGatingType < AVE_MCTF_GatingType_Max"
+ "iLAFrameCnt == 0"
+ "iPreFiltAdjType >= -1 && iPreFiltAdjType < AVE_MCTF_PreFiltAdjType_Max"
+ "psData != __null && eDevType > AVE_DevType_None && eDevType < AVE_DevType_Max && eWorkMode > AVE_MCTF_WorkMode_None && eWorkMode < AVE_MCTF_WorkMode_Max && eLatencyMode > AVE_MCTF_Mode_Invalid && eLatencyMode < AVE_MCTF_Mode_Max && peGatingType != __null"
- "%lld %d AVE %s: %s Enter %p %d %d %d %p"
- "%lld %d AVE %s: %s Enter %p %d %d %d %p\n"
- "%lld %d AVE %s: %s Exit %p %d %d %d %p %d"
- "%lld %d AVE %s: %s Exit %p %d %d %d %p %d\n"
- "%lld %d AVE %s: %s:%d %p sID 0x%x gating type %d"
- "%lld %d AVE %s: %s:%d %p sID 0x%x gating type %d\n"
- "%lld %d AVE %s: %s:%d %p sID 0x%x noise level %d rIdx %d/%d s %d"
- "%lld %d AVE %s: %s:%d %p sID 0x%x noise level %d rIdx %d/%d s %d\n"
- "%lld %d AVE %s: %s:%d %p sID 0x%x prefilt adj type %d"
- "%lld %d AVE %s: %s:%d %p sID 0x%x prefilt adj type %d\n"
- "%lld %d AVE %s: %s:%d %s | AVE_MCTF_GetGatingType failed %d"
- "%lld %d AVE %s: %s:%d %s | AVE_MCTF_GetGatingType failed %d\n"
- "%lld %d AVE %s: %s:%d %s | AVE_MCTF_GetPreFiltAdjType failed %d"
- "%lld %d AVE %s: %s:%d %s | AVE_MCTF_GetPreFiltAdjType failed %d\n"
- "%lld %d AVE %s: %s:%d %s | wrong params, %p %d %d %d"
- "%lld %d AVE %s: %s:%d %s | wrong params, %p %d %d %d\n"
- "%lld %d AVE %s: %s:%d %s | wrong params, %p %d %d %d %p"
- "%lld %d AVE %s: %s:%d %s | wrong params, %p %d %d %d %p\n"
- "%lld %d AVE %s: %s::%s:%d %s | fail to send PS %p %p"
- "%lld %d AVE %s: %s::%s:%d %s | fail to send PS %p %p\n"
- "913.29.1"
- "AVE_MCTF_GetGatingType"
- "AVE_MCTF_GetPreFiltAdjType"
- "psData != __null && eDevType > AVE_DevType_None && eDevType < AVE_DevType_Max && eWorkMode > AVE_MCTF_WorkMode_None && eWorkMode < AVE_MCTF_WorkMode_Max && eLatencyMode > AVE_MCTF_Mode_Invalid && eLatencyMode < AVE_MCTF_Mode_Max"
```
