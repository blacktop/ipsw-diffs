## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/Contents/MacOS/AppleMCTF`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-913.29.1.0.0
-  __TEXT.__text: 0x86710
+913.43.1.0.0
+  __TEXT.__text: 0x879d4
   __TEXT.__auth_stubs: 0xd70
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x2837c
-  __TEXT.__const: 0x22a18
+  __TEXT.__cstring: 0x286c9
+  __TEXT.__const: 0x229f8
   __TEXT.__gcc_except_tab: 0x628
   __TEXT.__objc_methname: 0xb
   __TEXT.__unwind_info: 0x670
-  __DATA_CONST.__const: 0x53b0
-  __DATA_CONST.__cfstring: 0x940
+  __DATA_CONST.__const: 0x5430
+  __DATA_CONST.__cfstring: 0x980
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x6c8
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_selrefs: 0x8
   __DATA.__data: 0xa0
-  __DATA.__bss: 0x8d0
+  __DATA.__bss: 0x8d8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/Versions/A/CoreVideo

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 666
+  Functions: 670
   Symbols:   341
-  CStrings:  3427
+  CStrings:  3444
 
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
+ "%lld %d AVE %s: %s:%d %s | AVE_MCTF_DecideGatingType failed %p %p %lld %d"
+ "%lld %d AVE %s: %s:%d %s | AVE_MCTF_DecideGatingType failed %p %p %lld %d\n"
+ "%lld %d AVE %s: %s:%d %s | AVE_MCTF_DecidePreFiltAdjType failed %p %p %lld %d"
+ "%lld %d AVE %s: %s:%d %s | AVE_MCTF_DecidePreFiltAdjType failed %p %p %lld %d\n"
+ "%lld %d AVE %s: %s:%d %s | wrong params, %d %d %p %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | wrong params, %d %d %p %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | wrong params, %d %p %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | wrong params, %d %p %d %d %d\n"
+ "%lld %d AVE %s: fail to send PS %p %p %d, dropping frame"
+ "%lld %d AVE %s: fail to send PS %p %p %d, dropping frame\n"
+ "21:53:05"
+ "913.43.1"
+ "AVE_MCTFFnumChangeResetMCTF"
+ "AVE_MCTFGatingType"
+ "AVE_MCTFPreFiltAdjType"
+ "AVE_MCTF_DecideGatingType"
+ "AVE_MCTF_DecidePreFiltAdjType"
+ "AVE_PROPERTY_KEY_MCTF_GATING_TYPE"
+ "AVE_PROPERTY_KEY_MCTF_PRE_FILT_ADJ_TYPE"
+ "AVE_Prop_MCTF_GetMCTFGatingType"
+ "AVE_Prop_MCTF_GetMCTFPreFiltAdjType"
+ "AVE_Prop_MCTF_SetMCTFGatingType"
+ "AVE_Prop_MCTF_SetMCTFPreFiltAdjType"
+ "Aug 11 2026"
+ "MCTFGatingType"
+ "MCTFGatingType = %d\n"
+ "MCTFPreFiltAdjType"
+ "MCTFPreFiltAdjType = %d\n"
+ "iGatingType >= -1 && iGatingType < AVE_MCTF_GatingType_Max"
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
- "%lld %d AVE %s: %s:%d %s | AVE_MCTF_GetGatingType failed %p %p %lld %d"
- "%lld %d AVE %s: %s:%d %s | AVE_MCTF_GetGatingType failed %p %p %lld %d\n"
- "%lld %d AVE %s: %s:%d %s | AVE_MCTF_GetPreFiltAdjType failed %p %p %lld %d"
- "%lld %d AVE %s: %s:%d %s | AVE_MCTF_GetPreFiltAdjType failed %p %p %lld %d\n"
- "%lld %d AVE %s: %s:%d %s | wrong params, %p %d %d %d"
- "%lld %d AVE %s: %s:%d %s | wrong params, %p %d %d %d\n"
- "%lld %d AVE %s: %s:%d %s | wrong params, %p %d %d %d %p"
- "%lld %d AVE %s: %s:%d %s | wrong params, %p %d %d %d %p\n"
- "%lld %d AVE %s: %s::%s:%d %s | fail to send PS %p %p"
- "%lld %d AVE %s: %s::%s:%d %s | fail to send PS %p %p\n"
- "21:33:36"
- "913.29.1"
- "AVE_MCTF_GetGatingType"
- "AVE_MCTF_GetPreFiltAdjType"
- "Jul 14 2026"
- "psData != __null && eDevType > AVE_DevType_None && eDevType < AVE_DevType_Max && eWorkMode > AVE_MCTF_WorkMode_None && eWorkMode < AVE_MCTF_WorkMode_Max && eLatencyMode > AVE_MCTF_Mode_Invalid && eLatencyMode < AVE_MCTF_Mode_Max"
```
