## AppleVideoEncoder

> `/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder`

```diff

-904.58.0.0.0
-  __TEXT.__text: 0x18acd4
+904.72.0.0.0
+  __TEXT.__text: 0x18aee8
   __TEXT.__auth_stubs: 0x1050
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0xc
   __TEXT.__const: 0x221a8
-  __TEXT.__cstring: 0x5222a
+  __TEXT.__cstring: 0x51efa
   __TEXT.__gcc_except_tab: 0x6f0
   __TEXT.__objc_methname: 0xb
   __TEXT.__unwind_info: 0x888
   __DATA_CONST.__auth_got: 0x838
   __DATA_CONST.__got: 0x760
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0xaac0
-  __DATA_CONST.__cfstring: 0x1580
+  __DATA_CONST.__const: 0xa098
+  __DATA_CONST.__cfstring: 0x3080
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8
   __DATA.__data: 0x158

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D73DA6EB-F090-3F0D-8953-526200BD93F3
-  Functions: 1569
+  UUID: 6DECB29B-B9FE-3F41-839B-C4900F84DCA6
+  Functions: 1575
   Symbols:   511
-  CStrings:  6744
+  CStrings:  6956
 
CStrings:
+ "%lld %d AVE %s: %s:%d  %p %lld %p %p %p iaVTLatencyMode = %s"
+ "%lld %d AVE %s: %s:%d  %p %lld %p %p %p iaVTLatencyMode = %s\n"
+ "%lld %d AVE %s: %s:%d %s | fail to add property %p %d %d 0x%x %lld | %d %s %p %d 0x%x 0x%llx %d"
+ "%lld %d AVE %s: %s:%d %s | fail to add property %p %d %d 0x%x %lld | %d %s %p %d 0x%x 0x%llx %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to get property %p %lld %d 0x%x %p %p %p | %s %p %d 0x%x 0x%llx %d"
+ "%lld %d AVE %s: %s:%d %s | fail to get property %p %lld %d 0x%x %p %p %p | %s %p %d 0x%x 0x%llx %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to set property %p %lld %d 0x%x %p %p | %s %p %d 0x%x 0x%llx %d"
+ "%lld %d AVE %s: %s:%d %s | fail to set property %p %lld %d 0x%x %p %p | %s %p %d 0x%x 0x%llx %d\n"
+ "%lld %d AVE %s: %s:%d %s | get function is not supported %p %lld %d 0x%x %p %p %p | %s %p %d 0x%x 0x%llx"
+ "%lld %d AVE %s: %s:%d %s | get function is not supported %p %lld %d 0x%x %p %p %p | %s %p %d 0x%x 0x%llx\n"
+ "%lld %d AVE %s: %s:%d %s | invalid LatencyMode %p %lld %p %p %p"
+ "%lld %d AVE %s: %s:%d %s | invalid LatencyMode %p %lld %p %p %p\n"
+ "%lld %d AVE %s: %s:%d %s | invalid LatencyMode %p %lld %p %p %p %d (%d, %d)"
+ "%lld %d AVE %s: %s:%d %s | invalid LatencyMode %p %lld %p %p %p %d (%d, %d)\n"
+ "%lld %d AVE %s: %s:%d %s | set function is not supported %p %lld %d 0x%x %p %p | %s %p %d 0x%x 0x%llx"
+ "%lld %d AVE %s: %s:%d %s | set function is not supported %p %lld %d 0x%x %p %p | %s %p %d 0x%x 0x%llx\n"
+ "%lld %d AVE %s: %s:%d fail to create preset %p %lld %d %p %p %d 0x%x %d %p %p %d %p %s"
+ "%lld %d AVE %s: %s:%d fail to create preset %p %lld %d %p %p %d 0x%x %d %p %p %d %p %s\n"
+ "%lld %d AVE %s: %s:%d fail to find property entry %p %lld %d %p %p %d 0x%x %d %p %p %p %s %d"
+ "%lld %d AVE %s: %s:%d fail to find property entry %p %lld %d %p %p %d 0x%x %d %p %p %p %s %d\n"
+ "%lld %d AVE %s: UserQpMapSize (%d) is smaller than required (%d), copying only received data"
+ "%lld %d AVE %s: UserQpMapSize (%d) is smaller than required (%d), copying only received data\n"
+ "22:32:32"
+ "22:32:33"
+ "22:32:35"
+ "904.72.0"
+ "AVE_MCTF_Mode_Invalid < eMCTFLatencyMode && eMCTFLatencyMode < AVE_MCTF_Mode_Max"
+ "AVE_Prop_AVC_GetEnableUserQPForFacetime"
+ "AVE_Prop_AVC_SetEnableUserQPForFacetime"
+ "AVE_Prop_HEVC_GetEnableUserQPForFacetime"
+ "AVE_Prop_HEVC_GetMCTFLatencyMode"
+ "AVE_Prop_HEVC_SetEnableUserQPForFacetime"
+ "AVE_Prop_HEVC_SetMCTFLatencyMode"
+ "AVE_kVTCompressionPropertyKey_EnableUserQPForFacetime"
+ "AVE_kVTMotionEstimationProcessor_MotionEstimationSearchMode"
+ "AVE_kVTMotionEstimationProcessor_SupportedMotionSearchModes"
+ "AVE_kVTMotionEstimationProcessor_lrmeRCPassNum"
+ "Auto"
+ "CFStringGetTypeID() == CFGetTypeID(pValue) || CFNumberGetTypeID() == CFGetTypeID(pValue)"
+ "EnableUserQPForFacetime"
+ "Jul 25 2025"
+ "Low"
+ "MCTFLatencyMode"
+ "Medium"
+ "kVTCompressionPreset_Balanced"
+ "kVTCompressionPreset_HighQuality"
+ "kVTCompressionPreset_HighSpeed"
+ "kVTCompressionPropertyKey_TemporalNoiseReductionLatencyMode"
- "%lld %d AVE %s: %s:%d %s | current SoC A0 doesn't support ChromaFmt_422 or ChromaFmt_444. Fail."
- "%lld %d AVE %s: %s:%d %s | current SoC A0 doesn't support ChromaFmt_422 or ChromaFmt_444. Fail.\n"
- "%lld %d AVE %s: %s:%d %s | current SoC A0 doesn't support ChromaFmt_422. Fail."
- "%lld %d AVE %s: %s:%d %s | current SoC A0 doesn't support ChromaFmt_422. Fail.\n"
- "%lld %d AVE %s: %s:%d %s | current SoC A0 doesn't support SliceEncodingMode. Fail."
- "%lld %d AVE %s: %s:%d %s | current SoC A0 doesn't support SliceEncodingMode. Fail.\n"
- "%lld %d AVE %s: %s:%d %s | fail to add property %p %d %d 0x%x %lld | %d %s %s %d %d 0x%x 0x%llx %d"
- "%lld %d AVE %s: %s:%d %s | fail to add property %p %d %d 0x%x %lld | %d %s %s %d %d 0x%x 0x%llx %d\n"
- "%lld %d AVE %s: %s:%d %s | fail to create CFString %p %d 0x%x %lld %p"
- "%lld %d AVE %s: %s:%d %s | fail to create CFString %p %d 0x%x %lld %p\n"
- "%lld %d AVE %s: %s:%d %s | fail to get property %p %lld %d 0x%x %p %p %p | %s %s %d %d 0x%x 0x%llx %d"
- "%lld %d AVE %s: %s:%d %s | fail to get property %p %lld %d 0x%x %p %p %p | %s %s %d %d 0x%x 0x%llx %d\n"
- "%lld %d AVE %s: %s:%d %s | fail to set property %p %lld %d 0x%x %p %p | %s %s %d %d 0x%x 0x%llx %d"
- "%lld %d AVE %s: %s:%d %s | fail to set property %p %lld %d 0x%x %p %p | %s %s %d %d 0x%x 0x%llx %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create CFString %p %d %p %lld %d 0x%x %s"
- "%lld %d AVE %s: %s:%d %s | failed to create CFString %p %d %p %lld %d 0x%x %s\n"
- "%lld %d AVE %s: %s:%d %s | failed to create CFString %p %lld %d %p %p %d 0x%x %d %p %d %s"
- "%lld %d AVE %s: %s:%d %s | failed to create CFString %p %lld %d %p %p %d 0x%x %d %p %d %s\n"
- "%lld %d AVE %s: %s:%d %s | failed to create CFString %p %lld %d %p %p %d 0x%x %d %p %p %s %d"
- "%lld %d AVE %s: %s:%d %s | failed to create CFString %p %lld %d %p %p %d 0x%x %d %p %p %s %d\n"
- "%lld %d AVE %s: %s:%d %s | get function is not supported %p %lld %d 0x%x %p %p %p | %s %s %d %d 0x%x 0x%llx"
- "%lld %d AVE %s: %s:%d %s | get function is not supported %p %lld %d 0x%x %p %p %p | %s %s %d %d 0x%x 0x%llx\n"
- "%lld %d AVE %s: %s:%d %s | set function is not supported %p %lld %d 0x%x %p %p | %s %s %d %d 0x%x 0x%llx"
- "%lld %d AVE %s: %s:%d %s | set function is not supported %p %lld %d 0x%x %p %p | %s %s %d %d 0x%x 0x%llx\n"
- "%lld %d AVE %s: %s:%d current SoC A0 doesn't support ANFD."
- "%lld %d AVE %s: %s:%d current SoC A0 doesn't support ANFD.\n"
- "%lld %d AVE %s: %s:%d current SoC A0 doesn't support BPictures."
- "%lld %d AVE %s: %s:%d current SoC A0 doesn't support BPictures.\n"
- "%lld %d AVE %s: %s:%d current SoC A0 doesn't support HiP/HiB."
- "%lld %d AVE %s: %s:%d current SoC A0 doesn't support HiP/HiB.\n"
- "%lld %d AVE %s: %s:%d current SoC A0 doesn't support MV-HEVC with B frames, force using I/P frames"
- "%lld %d AVE %s: %s:%d current SoC A0 doesn't support MV-HEVC with B frames, force using I/P frames\n"
- "%lld %d AVE %s: %s:%d failed to create preset %p %lld %d %p %p %d 0x%x %d %p %p %d %s"
- "%lld %d AVE %s: %s:%d failed to create preset %p %lld %d %p %p %d 0x%x %d %p %p %d %s\n"
- "%lld %d AVE %s: %s:%d failed to find property entry %p %lld %d %p %p %d 0x%x %d %p %p %s %d"
- "%lld %d AVE %s: %s:%d failed to find property entry %p %lld %d %p %p %d 0x%x %d %p %p %s %d\n"
- "%lld %d AVE %s: %s:%d: iDevRevision = 0x%x bIsErebusA0 %d"
- "%lld %d AVE %s: %s:%d: iDevRevision = 0x%x bIsErebusA0 %d\n"
- "%lld %d AVE %s: Insufficient size for userQPMap, %d, %d"
- "%lld %d AVE %s: Insufficient size for userQPMap, %d, %d\n"
- "00:48:33"
- "00:48:35"
- "00:48:36"
- "00:48:37"
- "904.58.0"
- "AVE_PROPERTY_KEY_BPICTURES"
- "BPictures"
- "Jul 15 2025"
- "kOFSessionPropertyKey_MotionEstimationSearchMode"
- "kOFSessionPropertyKey_SupportedMotionSearchModes"
- "pCFKey != __null"
- "pINS->saSPS[AVE_BASE_LAYER].chroma_format_idc != ChromaFmt_422"

```
