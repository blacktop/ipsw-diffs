## MediaToolbox

> `/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`

```diff

-3290.3.2.0.0
-  __TEXT.__text: 0xb8bf44
+3290.4.2.11.1
+  __TEXT.__text: 0xb8d1bc
   __TEXT.__auth_stubs: 0xb370
   __TEXT.__objc_methlist: 0x2484
   __TEXT.__const: 0x4e4e0
-  __TEXT.__cstring: 0x6b094
-  __TEXT.__oslogstring: 0x56ede
+  __TEXT.__cstring: 0x6b1d1
+  __TEXT.__oslogstring: 0x571f4
   __TEXT.__ustring: 0x23e
   __TEXT.__gcc_except_tab: 0x106c
   __TEXT.__dlopen_cstrs: 0x1c8
-  __TEXT.__unwind_info: 0x13408
+  __TEXT.__unwind_info: 0x13430
   __TEXT.__eh_frame: 0x298
   __TEXT.__objc_classname: 0x82d
   __TEXT.__objc_methname: 0x6aba
   __TEXT.__objc_methtype: 0x2901
   __TEXT.__objc_stubs: 0x6100
   __DATA_CONST.__got: 0x3910
-  __DATA_CONST.__const: 0x23518
+  __DATA_CONST.__const: 0x23588
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x59d0
-  __AUTH_CONST.__const: 0x414e8
-  __AUTH_CONST.__cfstring: 0x4ff20
+  __AUTH_CONST.__const: 0x41518
+  __AUTH_CONST.__cfstring: 0x4ff60
   __AUTH_CONST.__objc_const: 0x4db8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D4ECBC59-A74E-3F1F-B392-2C4EB6A4F238
-  Functions: 39026
-  Symbols:   100526
-  CStrings:  31697
+  UUID: 0D0B09D6-7183-3899-845B-28A77A29D72D
+  Functions: 39041
+  Symbols:   100591
+  CStrings:  31712
 
Symbols:
+ _FigBufferedAirPlayAudioRenderPipelineSetPropertiesToUpdateAtTransition
+ _FigBufferedAirPlayAudioRenderPipelineSetPropertiesToUpdateAtTransition.cold.1
+ _FigBufferedAirPlayAudioRenderPipelineSetPropertiesToUpdateAtTransition.cold.2
+ ___block_descriptor_tmp.193
+ ___block_descriptor_tmp.210
+ ___block_descriptor_tmp.211
+ ___block_descriptor_tmp.223
+ ___block_descriptor_tmp.224
+ ___block_descriptor_tmp.225
+ ___block_descriptor_tmp.226
+ ___fbapspManager_InspectSampleBuffer_block_invoke
+ ___fbapspManager_flushFromTime_block_invoke.214
+ ___fbapspManager_flushFromTime_block_invoke.214.cold.1
+ ___fbapspManager_flushFromTime_block_invoke.214.cold.2
+ ___fbapspManager_flushFromTime_block_invoke.216
+ ___fbapspManager_processTransitionIDIfFound_block_invoke
+ ___fbapspManager_setPropertiesToUpdateAtTransition_block_invoke
+ _bapspPassthrough_setPropertiesToUpdateAndStartAtTransition
+ _bapspTranscode_setPropertiesToUpdateAndStartAtTransition
+ _fbapop_removePropertiesToUpdateAtTransition
+ _fbapop_setPropertiesToUpdateAtTransition
+ _fbaprp_removePropertiesToUpdateAtTransitionAndFreeTransitionRosterRecord
+ _fbaprp_retainAndKeepSampleBuffersBeforeTransitionIDMarkerFilterCallback
+ _fbaprp_transitionRosterRemoveRecordsStartingFromTransitionID.cold.2
+ _fbapspManager_removePropertiesToUpdateAtTransition
+ _fbapspManager_setPropertiesToUpdateAtTransition
+ _figAudioQueueRenderPipelineStartAndUseTimebaseAtTransition.cold.3
+ _figAudioQueueRenderPipelineStartAndUseTimebaseAtTransition.cold.4
+ _fpfsi_CompleteAlternateListContainsMultichannelVariant
+ _kFigTrialFactor_AllowFastStartInLL
- _OUTLINED_FUNCTION_876
- _OUTLINED_FUNCTION_877
- _OUTLINED_FUNCTION_878
- ___block_descriptor_tmp.189
- ___block_descriptor_tmp.191
- ___block_descriptor_tmp.203
- ___block_descriptor_tmp.209
- ___fbapspManager_flushFromTime_block_invoke.210
- ___fbapspManager_flushFromTime_block_invoke.211
- ___fbapspManager_flushFromTime_block_invoke.211.cold.1
- ___fbapspManager_flushFromTime_block_invoke.211.cold.2
- _fbaprp_copySbufBeforeTransitionIDForBufferQueueResetCallback
- _fbaprp_transitionRosterFreeRecord
- _figAudioQueueRenderPipelineSetPropertiesToUpdateAtTransition.cold.1
CStrings:
+ "<<<< FigBufferedAirPlayAudioChainSubPipePassthrough >>>> %s: [%p] %{public}s bapspPassthrough no-op"
+ "<<<< FigBufferedAirPlayOutputProxy >>>> %s: [%p] %{public}s rpID[%@]%s delegate to SubPipeManager - TransitionID=`%@`"
+ "<<<< FigBufferedAirPlayOutputProxy >>>> %s: [%p] %{public}s rpID[%@]%s delegate to SubPipeManager - TransitionID=`%@`, PropertiesToUpdateAtTransition=%@"
+ "<<<< FigBufferedAirPlayRP >>>> %s: [%p] %{public}s Failed to process and retain input queue data before transition %@ in srcBufferQueue"
+ "<<<< FigBufferedAirPlayRP >>>> %s: [%p] %{public}s Remove PropertiesToUpdateAtTransition transitionID=%@"
+ "<<<< FigBufferedAirPlayRP >>>> %s: [%p] %{public}s received RequestForRetransmission notification without Token or warehouseRetransmissionAvailable=%d"
+ "<<<< FigBufferedAirPlaySubPipeManager >>>> %s: [%p] %{public}s Updating firstSbufOPTS. OPTS=%1.3f, mixStartMediaTimeOffset=%1.3f SBUF=%@"
+ "<<<< Warehouse RP >>>> %s: %{public}s (%p) retransmitted %d original sbufs (indexes %d..%d) from warehouse, OPTS %1.3f ... %1.3f"
+ "allowFastStartInLowLatency"
+ "bapspPassthrough_setPropertiesToUpdateAndStartAtTransition"
+ "fbapop_removePropertiesToUpdateAtTransition"
+ "fbapop_setPropertiesToUpdateAtTransition"
+ "fbaprp_removePropertiesToUpdateAtTransitionAndFreeTransitionRosterRecord"
+ "fbapspManager_updateFirstSbufInfoAndMixStartMediaTimeOffset"
+ "iq_freewheel"
- "<<<< FigBufferedAirPlayRP >>>> %s: [%p] %{public}s Failed to find transition %@ in srcBufferQueue and FigSampleBufferProcessor"
- "<<<< FigBufferedAirPlayRP >>>> %s: [%p] %{public}s received RequestForRetransmission notification without Token"

```
