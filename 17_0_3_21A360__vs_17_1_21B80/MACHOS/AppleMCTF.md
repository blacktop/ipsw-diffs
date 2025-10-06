## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

```diff

-703.6.9.0.0
-  __TEXT.__text: 0xe4920
+703.40.1.0.0
+  __TEXT.__text: 0xe7ac0
   __TEXT.__auth_stubs: 0xeb0
   __TEXT.__init_offsets: 0x8
+  __TEXT.__cstring: 0x637c1
   __TEXT.__const: 0x10798
-  __TEXT.__cstring: 0x62a97
   __TEXT.__gcc_except_tab: 0x1fc
-  __TEXT.__unwind_info: 0x738
+  __TEXT.__unwind_info: 0x748
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x760
   __DATA_CONST.__got: 0x8a8
   __DATA_CONST.__auth_ptr: 0x30
   __DATA_CONST.__const: 0x2300
-  __DATA_CONST.__cfstring: 0x2300
+  __DATA_CONST.__cfstring: 0x2320
   __DATA.__data: 0x20
-  __DATA.__bss: 0x5c0
+  __DATA.__bss: 0x5c8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo

   - /System/Library/PrivateFrameworks/OpticalFlowFramework.framework/OpticalFlowFramework
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 4CE45C79-A7A8-3EC3-BEF5-09A2D642E1DB
-  Functions: 605
+  UUID: C2A82B70-3B43-339A-ADFE-ACF1D2EAD688
+  Functions: 615
   Symbols:   561
-  CStrings:  6433
+  CStrings:  6498
 
CStrings:
+ "%lld %d AVE %s: %s Enter %d"
+ "%lld %d AVE %s: %s Enter %d\n"
+ "%lld %d AVE %s: %s Enter %d %d %p"
+ "%lld %d AVE %s: %s Enter %d %d %p\n"
+ "%lld %d AVE %s: %s Enter %p %d %lld"
+ "%lld %d AVE %s: %s Enter %p %d %lld\n"
+ "%lld %d AVE %s: %s Exit %d %d"
+ "%lld %d AVE %s: %s Exit %d %d\n"
+ "%lld %d AVE %s: %s Exit %d %d %p %d"
+ "%lld %d AVE %s: %s Exit %d %d %p %d\n"
+ "%lld %d AVE %s: %s Exit %p %d %lld %d"
+ "%lld %d AVE %s: %s Exit %p %d %lld %d\n"
+ "%lld %d AVE %s: %s:%d %s | FIG: MV-HEVC does not support BaseLayerFrameRate"
+ "%lld %d AVE %s: %s:%d %s | FIG: MV-HEVC does not support BaseLayerFrameRate\n"
+ "%lld %d AVE %s: %s:%d %s | FIG: MV-HEVC does not support CHROMA_FORMAT_MONOCHROME, CHROMA_FORMAT_422, or CHROMA_FORMAT_444"
+ "%lld %d AVE %s: %s:%d %s | FIG: MV-HEVC does not support CHROMA_FORMAT_MONOCHROME, CHROMA_FORMAT_422, or CHROMA_FORMAT_444\n"
+ "%lld %d AVE %s: %s:%d %s | MV-HEVC does not support CHROMA_FORMAT_MONOCHROME, CHROMA_FORMAT_422, or CHROMA_FORMAT_444"
+ "%lld %d AVE %s: %s:%d %s | MV-HEVC does not support CHROMA_FORMAT_MONOCHROME, CHROMA_FORMAT_422, or CHROMA_FORMAT_444\n"
+ "%lld %d AVE %s: %s:%d %s | MV-HEVC does not support kVTCompressionPropertyKey_BaseLayerFrameRate"
+ "%lld %d AVE %s: %s:%d %s | MV-HEVC does not support kVTCompressionPropertyKey_BaseLayerFrameRate\n"
+ "%lld %d AVE %s: %s:%d %s | fail to create time stats %d %d %p"
+ "%lld %d AVE %s: %s:%d %s | fail to create time stats %d %d %p\n"
+ "%lld %d AVE %s: %s:%d %s | fail to initialize time stats %p %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | fail to initialize time stats %p %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to allocate memory of time pair %p %d %d"
+ "%lld %d AVE %s: %s:%d %s | failed to allocate memory of time pair %p %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | wrong parameters %d %d %p"
+ "%lld %d AVE %s: %s:%d %s | wrong parameters %d %d %p\n"
+ "%lld %d AVE %s: %s:%d %s | wrong parameters %p %d %d %p %d"
+ "%lld %d AVE %s: %s:%d %s | wrong parameters %p %d %d %p %d\n"
+ "%lld %d AVE %s: %s:%d %s | wrong parameters %p %d %lld"
+ "%lld %d AVE %s: %s:%d %s | wrong parameters %p %d %lld\n"
+ "%lld %d AVE %s: %s:%d %s | wrong state %p %d %lld"
+ "%lld %d AVE %s: %s:%d %s | wrong state %p %d %lld\n"
+ "%lld %d AVE %s: %s:%d: %d ForceKeyFrame IDR without COMPLETE MiniGOP"
+ "%lld %d AVE %s: %s:%d: %d ForceKeyFrame IDR without COMPLETE MiniGOP\n"
+ "%lld %d AVE %s: FIG: FLLB BFrameCap %d %d %d | %d %d %d %d"
+ "%lld %d AVE %s: FIG: FLLB BFrameCap %d %d %d | %d %d %d %d\n"
+ "%lld %d AVE %s: FIG: disable FLLB %d->0 | %p | %d %d %d %d | %d %d %d %d %d %d %d %d %d %d %d %d"
+ "%lld %d AVE %s: FIG: disable FLLB %d->0 | %p | %d %d %d %d | %d %d %d %d %d %d %d %d %d %d %d %d\n"
+ "%lld %d AVE %s: TimeStats ID: %d %s | Open: %lld Close: %lld Prepare: %lld Start: %lld Stop: %lld Complete: %lld"
+ "%lld %d AVE %s: TimeStats ID: %d %s | Open: %lld Close: %lld Prepare: %lld Start: %lld Stop: %lld Complete: %lld\n"
+ "%lld %d AVE %s: TimeStats ID: %d %s | Process: %lld - %lld - %lld Count: %d"
+ "%lld %d AVE %s: TimeStats ID: %d %s | Process: %lld - %lld - %lld Count: %d\n"
+ "%lld %d AVE %s: TimeStats ID: %d %s | Session: %lld Process: %lld"
+ "%lld %d AVE %s: TimeStats ID: %d %s | Session: %lld Process: %lld\n"
+ "AVE_LogConsole"
+ "AVE_Log_UpdateConsole"
+ "AVE_TimeStats_AddEndTime"
+ "AVE_TimeStats_AddStartTime"
+ "AVE_TimeStats_Calc"
+ "AVE_TimeStats_Create"
+ "AVE_TimeStats_Destroy"
+ "AVE_TimeStats_Init"
+ "AVE_TimeStats_MaxCnt"
+ "AVE_TimeStats_Print"
+ "AVE_TimeStats_Restart"
+ "AVE_TimeStats_Uninit"
+ "SessionIndicator"
+ "TimeStats ID: %d %s | Open: %lld Close: %lld Prepare: %lld Start: %lld Stop: %lld Complete: %lld"
+ "TimeStats ID: %d %s | Open: %lld Close: %lld Prepare: %lld Start: %lld Stop: %lld Complete: %lld\n"
+ "TimeStats ID: %d %s | Process: %lld - %lld - %lld Count: %d"
+ "TimeStats ID: %d %s | Process: %lld - %lld - %lld Count: %d\n"
+ "TimeStats ID: %d %s | Session: %lld Process: %lld"
+ "TimeStats ID: %d %s | Session: %lld Process: %lld\n"
+ "encoderPrivateStorage->sRCParams.ui32AverageNonDroppableFrameRate == 0"
+ "encoderPrivateStorage->saSPS[0].chroma_format_idc == CHROMA_FORMAT_420"
+ "num >= 0 && ppTS != __null"
+ "pFPS != __null && 0 < fps && fps < 100000 && num >= 0"
+ "pTP != __null"
+ "pTS != __null"
+ "pTS != __null && 0 <= pos && pos < AVE_TimeStats_Pos_Max && ts >= 0"
+ "pTS != __null && num >= 0"
+ "pTS->psTP != __null"
- "%lld %d AVE %s: %s:%d %s | FIG: chroma_format_idc != 1 and profile_idc = %d."
- "%lld %d AVE %s: %s:%d %s | FIG: chroma_format_idc != 1 and profile_idc = %d.\n"
- "%lld %d AVE %s: FIG: FIG: Currently Disabling BaseLayerFrameRate   when iLayerNum > 1"
- "%lld %d AVE %s: FIG: FIG: Currently Disabling BaseLayerFrameRate   when iLayerNum > 1\n"
- "%lld %d AVE %s: FIG: FLLB BFrameCap %d %d %d %d %d"
- "%lld %d AVE %s: FIG: FLLB BFrameCap %d %d %d %d %d\n"
- "%lld %d AVE %s: FIG: disable FLLB %d 0 | %p %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d"
- "%lld %d AVE %s: FIG: disable FLLB %d 0 | %p %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d\n"
- "(pEncoderPrivateStorage->SPSHevcParams.PTL.general_profile_idc == SH_HEVC_PROFILE_MAINREXT)"
- "pFPS != __null && 0 < fps && fps < 100000"

```
