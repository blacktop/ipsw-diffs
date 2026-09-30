## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

```diff

-802.61.1.0.0
-  __TEXT.__text: 0x54ac4
-  __TEXT.__auth_stubs: 0xc90
+802.88.0.0.0
+  __TEXT.__text: 0x54864
+  __TEXT.__auth_stubs: 0xca0
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x8
-  __TEXT.__cstring: 0x1daf4
+  __TEXT.__cstring: 0x1e4a0
   __TEXT.__const: 0x11438
   __TEXT.__gcc_except_tab: 0x458
   __TEXT.__objc_methname: 0xb
-  __TEXT.__unwind_info: 0x5d8
-  __DATA_CONST.__auth_got: 0x658
+  __TEXT.__unwind_info: 0x5c8
+  __DATA_CONST.__auth_got: 0x660
   __DATA_CONST.__got: 0x3d0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x2700
+  __DATA_CONST.__const: 0x2710
   __DATA_CONST.__cfstring: 0x3a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 512
-  Symbols:   330
-  CStrings:  2339
+  Functions: 510
+  Symbols:   331
+  CStrings:  2341
 
Symbols:
+ _CFStringGetSystemEncoding
+ _strcpy
- _dlsym
CStrings:
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | AVE MCTF: (CFGetTypeID) failed"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | AVE MCTF: (CFGetTypeID) failed\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) iMCTFPriority = %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) iMCTFPriority = %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) iaLFSResult %!d(MISSING) %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) iaLFSResult %!d(MISSING) %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) iaLRSResult %!d(MISSING) %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) iaLRSResult %!d(MISSING) %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) iaVTMCTFMode = %!s(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) iaVTMCTFMode = %!s(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING)::%!s(MISSING) Exit %!p(MISSING) %!l(MISSING)ld %!p(MISSING) %!d(MISSING) %!p(MISSING) %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING)::%!s(MISSING) Exit %!p(MISSING) %!l(MISSING)ld %!p(MISSING) %!d(MISSING) %!p(MISSING) %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING)::%!s(MISSING):%!d(MISSING) %!s(MISSING) | fail to create dictionary"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING)::%!s(MISSING):%!d(MISSING) %!s(MISSING) | fail to create dictionary\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING)::%!s(MISSING):%!d(MISSING) fail to calculate checksum %!p(MISSING) %!l(MISSING)ld %!p(MISSING) %!p(MISSING) %!d(MISSING) %!p(MISSING) %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING)::%!s(MISSING):%!d(MISSING) fail to calculate checksum %!p(MISSING) %!l(MISSING)ld %!p(MISSING) %!p(MISSING) %!d(MISSING) %!p(MISSING) %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING)::%!s(MISSING):%!d(MISSING) fail to filter chroma %!p(MISSING) %!l(MISSING)ld %!p(MISSING) %!p(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING)::%!s(MISSING):%!d(MISSING) fail to filter chroma %!p(MISSING) %!l(MISSING)ld %!p(MISSING) %!p(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)\n"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING)::%!s(MISSING):%!d(MISSING) fail to scale ref frame %!p(MISSING) %!l(MISSING)ld %!p(MISSING) %!p(MISSING) %!p(MISSING) %!d(MISSING)"
+ "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING)::%!s(MISSING):%!d(MISSING) fail to scale ref frame %!p(MISSING) %!l(MISSING)ld %!p(MISSING) %!p(MISSING) %!p(MISSING) %!d(MISSING)\n"
+ "21:26:47"
+ "802.88.0"
+ "AVE_PreemptiveLoadBalancing"
+ "CFStringGetTypeID() == CFGetTypeID(pValue) || CFNumberGetTypeID() == CFGetTypeID(pValue)"
+ "Frame#, FrameDiff, Fn_SetLrmeDiff, HW_LrmeDiff, Fn_SetLrrcDiff, HW_LrrcDiff, Fn_SetPipeDiff, HW_PipeDiff, Fn_PipeDoneDiff, FrameQIn, Fn_SetLrmeStart, HW_LrmeStart, Fn_SetLRMEDone, Fn_SetLrrcStart, HW_LrrcStart, Fn_SetLRRCDone, Fn_SetPipeStart, HW_PipeStart, Fn_SetPipeDone, HW_LrmeDone, HW_LrrcDone, HW_PipeDone, Fn_PipeDoneStart, Fn_PipeDoneEnd, LrmeStatsDone, LrrcStatsDone, PipeStatsDone, FrameOut\n"
+ "FrameNum, SliceNum, CoreID, CoreMode, IBTimeDiff, FrameDiff, InQueueTime, Fn_StartEventLRMEFS_Diff, Hw_LrmeFS_Diff, LrmeFSDone_Diff, Fn_StartEventPipe_Diff, Hw_Pipe_Diff, PipeDone_Diff, Fn_StartEventTranscode_Diff, Hw_Transcode_Diff, TranscodeDone_Diff, IBTimeS, IBTimeE, FrameIn, Fn_StartEventLRMEFS_Start, Hw_LRMEFS_Start, Fn_StartEventLRMEFS_End, Fn_StartEventLRMERC_StartP0, Hw_LRMERC_StartP0, Fn_StartEventLRMERC_EndP0, Fn_StartEventLRMERC_StartP1, Hw_LRMERC_StartP1, Fn_StartEventLRMERC_EndP1, Fn_StartEventLRMERC_StartP2, Hw_LRMERC_StartP2, Fn_StartEventLRMERC_EndP2, Fn_StartEventLRMERC_StartP3, Hw_LRMERC_StartP3, Fn_StartEventLRMERC_EndP3, Fn_StartEventLRMERC_StartP4, Hw_LRMERC_StartP4, Fn_StartEventLRMERC_EndP4, Fn_StartEventLRMERC_StartP5, Hw_LRMERC_StartP5, Fn_StartEventLRMERC_EndP5, Fn_StartEventPipe_Start, Hw_Pipe_Start, Fn_StartEventPipe_End, Fn_StartEventTranscode_Start, Hw_Transcode_Start, Fn_StartEventTranscode_End, Hw_LRMEFS_End, Fn_DoneEventLRMEFS_Start, Fn_DoneEventLRMEFS_End, Hw_LRMERC_EndP0, Fn_DoneEventLRMERC_StartP0, Fn_DoneEventLRMERC_EndP0, Hw_LRMERC_EndP1, Fn_DoneEventLRMERC_StartP1, Fn_DoneEventLRMERC_EndP1, Hw_LRMERC_EndP2, Fn_DoneEventLRMERC_StartP2, Fn_DoneEventLRMERC_EndP2, Hw_LRMERC_EndP3, Fn_DoneEventLRMERC_StartP3, Fn_DoneEventLRMERC_EndP3, Hw_LRMERC_EndP4, Fn_DoneEventLRMERC_StartP4, Fn_DoneEventLRMERC_EndP4, Hw_LRMERC_EndP5, Fn_DoneEventLRMERC_StartP5, Fn_DoneEventLRMERC_EndP5, Hw_Pipe_End, Fn_DoneEventPipe_Start, Fn_DoneEventPipe_End, Hw_Transcode_End, Fn_DoneEventTranscode_Start, Fn_DoneEventTranscode_End, Fn_GetStatsEventLRMEFS_Start, Fn_GetStatsEventLRMEFS_End, Fn_GetStatsEventLRMERC_Start, Fn_GetStatsEventLRMERC_End, Fn_GetStatsEventPipe_Start, Fn_GetStatsEventPipe_End, Fn_GetStatsEventTranscode_Start, Fn_GetStatsEventTranscode_End, FrameOut, FnPostXCODEProcess_StartTime, FnPostXCODEProcess_EndTime,CPMU0, CPMU1, CPMU2, CPMU5, CPMU6, CPMU7\n"
+ "Jul 15 2024"
+ "LFSRef"
+ "LFSRefChroma"
+ "LFSRefChromaHeader"
+ "LFSRefLumaHeader"
+ "LFSResult"
+ "LRSNeighborMV"
+ "LRSResult"
+ "TemporalFilterPriority"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | AVE MCTF: (CFStringGetTypeID) failed"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | AVE MCTF: (CFStringGetTypeID) failed\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | invalid VCP"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) %!s(MISSING) | invalid VCP\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) iaLowResRCResult %!d(MISSING) %!d(MISSING)"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) iaLowResRCResult %!d(MISSING) %!d(MISSING)\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) iaLowResResult %!d(MISSING) %!d(MISSING)"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING):%!d(MISSING) iaLowResResult %!d(MISSING) %!d(MISSING)\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING)::%!s(MISSING) Exit %!p(MISSING) %!l(MISSING)ld %!p(MISSING) %!d(MISSING) %!p(MISSING) %!d(MISSING) %!d(MISSING)"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING)::%!s(MISSING) Exit %!p(MISSING) %!l(MISSING)ld %!p(MISSING) %!d(MISSING) %!p(MISSING) %!d(MISSING) %!d(MISSING)\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING)::%!s(MISSING):%!d(MISSING) %!s(MISSING) | fail to create CFArray"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING)::%!s(MISSING):%!d(MISSING) %!s(MISSING) | fail to create CFArray\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING)::%!s(MISSING):%!d(MISSING) failed %!p(MISSING) %!l(MISSING)ld %!p(MISSING) %!p(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING)::%!s(MISSING):%!d(MISSING) failed %!p(MISSING) %!l(MISSING)ld %!p(MISSING) %!p(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING)::%!s(MISSING):%!d(MISSING) failed %!p(MISSING) %!l(MISSING)ld %!p(MISSING) %!p(MISSING) %!d(MISSING) %!p(MISSING) %!d(MISSING)"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING)::%!s(MISSING):%!d(MISSING) failed %!p(MISSING) %!l(MISSING)ld %!p(MISSING) %!p(MISSING) %!d(MISSING) %!p(MISSING) %!d(MISSING)\n"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING)::%!s(MISSING):%!d(MISSING) failed %!p(MISSING) %!l(MISSING)ld %!p(MISSING) %!p(MISSING) %!p(MISSING) %!d(MISSING)"
- "%!l(MISSING)ld %!d(MISSING) AVE %!s(MISSING): %!s(MISSING)::%!s(MISSING):%!d(MISSING) failed %!p(MISSING) %!l(MISSING)ld %!p(MISSING) %!p(MISSING) %!p(MISSING) %!d(MISSING)\n"
- "20:40:23"
- "802.61.1"
- "AVE_VCP_Destroy"
- "CFStringGetTypeID() == CFGetTypeID(pValue)"
- "Jul  3 2024"
- "LowResRCResult"
- "LowResRef"
- "LowResRefChroma"
- "LowResRefChromaHeader"
- "LowResRefLumaHeader"
- "LowResResult"
- "MCTFMode"
- "VCPAVEContextRelease"
- "pChecksumDict != __null"
- "pcVCP != __null"

```
