## MediaToolbox

> `/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`

```diff

-3185.13.1.0.0
-  __TEXT.__text: 0xf5542c
-  __TEXT.__auth_stubs: 0xbb90
+3185.16.2.0.0
+  __TEXT.__text: 0xf5aed8
+  __TEXT.__auth_stubs: 0xbba0
   __TEXT.__objc_methlist: 0x1d00
-  __TEXT.__cstring: 0x116947
-  __TEXT.__const: 0x54e20
-  __TEXT.__oslogstring: 0x12965f
+  __TEXT.__cstring: 0x117079
+  __TEXT.__const: 0x54e30
+  __TEXT.__oslogstring: 0x12a0ac
   __TEXT.__ustring: 0x1f8
   __TEXT.__gcc_except_tab: 0x136c
   __TEXT.__dlopen_cstrs: 0x166
-  __TEXT.__unwind_info: 0x117a0
+  __TEXT.__unwind_info: 0x118c8
   __TEXT.__eh_frame: 0x4448
   __TEXT.__objc_classname: 0x812
-  __TEXT.__objc_methname: 0x5e1e
+  __TEXT.__objc_methname: 0x5e2e
   __TEXT.__objc_methtype: 0x2492
-  __TEXT.__objc_stubs: 0x57e0
+  __TEXT.__objc_stubs: 0x5800
   __DATA_CONST.__got: 0x3518
-  __DATA_CONST.__const: 0x21910
+  __DATA_CONST.__const: 0x21a58
   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ac0
+  __DATA_CONST.__objc_selrefs: 0x1ac8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x5de0
+  __AUTH_CONST.__auth_got: 0x5de8
   __AUTH_CONST.__auth_ptr: 0x30
-  __AUTH_CONST.__const: 0x3e138
-  __AUTH_CONST.__cfstring: 0x4fc00
+  __AUTH_CONST.__const: 0x3e1b8
+  __AUTH_CONST.__cfstring: 0x4fee0
   __AUTH_CONST.__objc_const: 0x5440
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH.__objc_data: 0xff0
   __AUTH.__data: 0xae0
   __DATA.__objc_ivar: 0x2d0
-  __DATA.__data: 0x18400
-  __DATA.__common: 0x30d9
-  __DATA.__bss: 0x3888
+  __DATA.__data: 0x18410
+  __DATA.__bss: 0x38e8
+  __DATA.__common: 0x2eb9
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__data: 0x240
+  __DATA_DIRTY.__common: 0x360
   __DATA_DIRTY.__bss: 0x3a0
-  __DATA_DIRTY.__common: 0x130
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 23490
-  Symbols:   33599
-  CStrings:  52684
+  Functions: 23534
+  Symbols:   33659
+  CStrings:  52779
 
Symbols:
+ _FigAudioRenderingPreferencesCreate
+ _FigPlaybackTimerCancel
+ _FigPlaybackTimerCreate
+ _FigPlaybackTimerGetTypeID
+ _FigPlaybackTimerIsScheduled
+ _FigPlaybackTimerScheduleForTimebaseTime
+ _FigPlaybackTimerScheduleForTimebaseTimeWithTeardownHandlers
+ _FigPlayerInterstitialEventGetFirstItemStartOffset
+ _FigPlayerInterstitialEventSetFirstItemStartOffset
+ _FigSampleBufferConsumerCreateForBufferQueue2
+ _FigVideoCompositionProcessorHasAnySourceTracksInArray
+ _kFigAssetOptionKey_DisableL4S
+ _kFigFileType_QuickTimeAudio
+ _kFigOverlapRange_EventID
+ _kFigOverlapRange_Intro
+ _kFigOverlapRange_IntroStartTime
+ _kFigOverlapRange_Outro
+ _kFigOverlapRange_OutroEndTime
+ _kFigOverlapRange_OutroStartTime
+ _kFigPlaybackItemProperty_OverlapRange
+ _kFigPlaybackItemProperty_OverlappedPlaybackEndTime
+ _kFigRenderPipelineNotificationParameter_RetransmitTime
+ _kFigRenderPipelineNotification_WarehousePleaseRetransmitFromTime
+ _kFigRenderPipelineOption_AudioRenderingPreferences
+ _kFigRenderPipelineProperty_OverlapRange
CStrings:
+ "    "
+ "<<<< FAQ >>>> %!s(MISSING): [%!p(MISSING) %!{(MISSING)public}s] setting cryptor to %!p(MISSING), was %!p(MISSING)"
+ "<<<< FAQ >>>> %!s(MISSING): [%!p(MISSING)] new cryptor[%!p(MISSING)] does not conform to expected TypeID. Converting to NULL cryptor!"
+ "<<<< FigBufferedAirPlayAudioChainSubPipeTranscode >>>> %!s(MISSING): [%!p(MISSING)] %!{(MISSING)public}s Audio rendering preferences %!@(MISSING)"
+ "<<<< FigFilePlayer >>>> %!s(MISSING): Cannot reuse renderTriple for track %!d(MISSING)"
+ "<<<< FigFilePlayer >>>> %!s(MISSING): Track reference %!{(MISSING)public}@: track ID array count should be even. Has %!d(MISSING)"
+ "<<<< FigFilePlayer >>>> %!s(MISSING): [%!p(MISSING)|%!{(MISSING)public}s] <%!p(MISSING)|%!{(MISSING)public}s> Reuse render triples for video composition"
+ "<<<< FigPlayerOverlap >>>> %!s(MISSING): <%!p(MISSING)|%!{(MISSING)public}s> end time is %!f(MISSING)"
+ "<<<< FigPlayerOverlap >>>> %!s(MISSING): <%!p(MISSING)|%!{(MISSING)public}s> failed to get timebase, err = %!d(MISSING)"
+ "<<<< FigPlayerOverlap >>>> %!s(MISSING): <%!p(MISSING)|%!{(MISSING)public}s> failed to schedule timer, err = %!d(MISSING)"
+ "<<<< FigPlayerOverlap >>>> %!s(MISSING): Failed to remove timebase listener with error %!d(MISSING)"
+ "<<<< FigPlayerOverlap >>>> %!s(MISSING): [%!p(MISSING)|%!{(MISSING)public}s] OverlappedPlaybackEndTime = %!f(MISSING) scheduled for <%!p(MISSING)|%!{(MISSING)public}s>"
+ "<<<< FigPlayerOverlap >>>> %!s(MISSING): [%!p(MISSING)|%!{(MISSING)public}s] beginning outro of <%!p(MISSING)|%!{(MISSING)public}s> current time %!f(MISSING) overlapping with <%!p(MISSING)|%!{(MISSING)public}s> current time %!f(MISSING) at host time %!f(MISSING) (= %!f(MISSING) + %!f(MISSING)), source %!f(MISSING) (= %!f(MISSING) + %!f(MISSING)), requested advance time was %!f(MISSING)."
+ "<<<< FigPlayerOverlap >>>> %!s(MISSING): [%!p(MISSING)|%!{(MISSING)public}s] success, advance time %!f(MISSING) set as anchor time %!f(MISSING) (now %!f(MISSING) + %!f(MISSING)) (source clock %!f(MISSING) = now %!f(MISSING) + %!f(MISSING)) on sub-player %!p(MISSING), outro timebase time %!f(MISSING)."
+ "<<<< FigPlayerOverlap >>>> %!s(MISSING): [player %!p(MISSING)|%!{(MISSING)public}s] item <%!p(MISSING)|%!{(MISSING)public}s>: timebase %!p(MISSING) %!{(MISSING)public}@ rate %!f(MISSING), %!{(MISSING)public}s %!f(MISSING) = host %!f(MISSING) (now %!f(MISSING) + %!f(MISSING)) = source %!f(MISSING) (now %!f(MISSING) + %!f(MISSING))"
+ "<<<< FigPlayerOverlap >>>> %!s(MISSING): adding notification listener failed"
+ "<<<< FigPlayerOverlap >>>> %!s(MISSING): copy end time failed"
+ "<<<< FigPlayerOverlap >>>> %!s(MISSING): duration is not numeric"
+ "<<<< FigPlayerOverlap >>>> %!s(MISSING): end time dictionaty is null"
+ "<<<< FigPlayerOverlap >>>> %!s(MISSING): failed to cancel end time timer"
+ "<<<< FigPlayerOverlap >>>> %!s(MISSING): failed to re-schedule end time timer"
+ "<<<< FigPlayerOverlap >>>> %!s(MISSING): outro item is null"
+ "<<<< FigPlayerOverlap >>>> %!s(MISSING): overlapped playback end time equal or less than advance time = %!f(MISSING), it will be ignored"
+ "<<<< FigPlayerOverlap >>>> %!s(MISSING): set overlappedPlaybackEndTime = %!f(MISSING) for item <%!p(MISSING)|%!{(MISSING)public}s>"
+ "<<<< FigPlayer_AP >>>> %!s(MISSING): [%!p(MISSING)] %!{(MISSING)public}s PiPMute isMuted=%!d(MISSING)"
+ "<<<< FigStreamPlayer >>>> %!s(MISSING): [%!p(MISSING)|%!{(MISSING)public}s] <%!p(MISSING)|%!{(MISSING)public}s>: Can no longer CommitToGapless, track got deleted in Restart"
+ "<<<< FigStreamPlayer >>>> %!s(MISSING): [%!p(MISSING)|%!{(MISSING)public}s] <%!p(MISSING)|%!{(MISSING)public}s>: Moving sbufs from track's cache via playedOut"
+ "<<<< HLSPersistentStore >>>> %!s(MISSING): %!s(MISSING): [%!f(MISSING)] [%!p(MISSING)]: [fileFork:pathnum] %!p(MISSING):%!@(MISSING) %!{(MISSING)private}@ [HOLDTIME = %!f(MISSING)] (%!d(MISSING)/%!d(MISSING)/%!d(MISSING) acq/blk/err) [acquireTime = %!f(MISSING)] [unlockTime = %!f(MISSING)]"
+ "<<<< HLSPersistentStore >>>> %!s(MISSING): Inconsistency: no record of flock() attempt. unlockrace with lock?"
+ "<<<< HLSPersistentStore >>>> %!s(MISSING): LOG STATE: empty, stopping timer"
+ "<<<< HLSPersistentStore >>>> %!s(MISSING): LOG STATE: hlspersistent_flock_logging_trace >= 5: force log dump"
+ "<<<< HLSPersistentStore >>>> %!s(MISSING): LOG STATE: will fire again in %!f(MISSING) seconds"
+ "<<<< HLSPersistentStore >>>> %!s(MISSING): [%!p(MISSING)] Unexpected NULL logRecord"
+ "<<<< HLSPersistentStore >>>> %!s(MISSING): flock() HISTORY"
+ "<<<< HLSPersistentStore >>>> %!s(MISSING): flock() HISTORY DONE"
+ "<<<< HLSPersistentStore >>>> %!s(MISSING): flock() IN PROGRESS"
+ "<<<< HLSPersistentStore >>>> %!s(MISSING): flock() IN PROGRESS DONE"
+ "<<<< MENTOROUTPUT >>>> %!s(MISSING): (%!p(MISSING)): buffer queue duration is %!f(MISSING), high water duration is %!f(MISSING), buffer queue total size is %!z(MISSING)d, high water total size is %!z(MISSING)d  returning %!s(MISSING)"
+ "<<<< OUTPUTTOFORMATWRITER >>>> %!s(MISSING): (%!p(MISSING)): buffer queue duration is %!f(MISSING), high water duration is %!f(MISSING), buffer queue total size is %!z(MISSING)d, high water total size is %!z(MISSING)d  returning %!s(MISSING)"
+ "<FigPlaybackItemOverlap %!p(MISSING) %!s(MISSING) sub-item %!p(MISSING) advanceTime %!f(MISSING) overlappedPlaybackEndTime %!f(MISSING)>"
+ "<unknown>"
+ "AudioRenderingPreferences"
+ "FHRP_DisableL4S"
+ "Failed to create trackIDsOfChangedTracks"
+ "FigPlaybackTimer"
+ "FigPlaybackTimer.c"
+ "FigPlaybackTimerCancel"
+ "FigPlaybackTimerCreate"
+ "FigPlaybackTimerScheduleForTimebaseTimeWithTeardownHandlers"
+ "FigSampleBufferConsumerCreateForBufferQueue2"
+ "HELD"
+ "Intro"
+ "IntroStartTime"
+ "NULL timerOut"
+ "Outro"
+ "OutroEndTime"
+ "OutroStartTime"
+ "OverlapRange"
+ "OverlappedPlaybackEndTime"
+ "RetransmitTime"
+ "StartOffset"
+ "VERBOSE INTERNAL LOGGING: hlspersistent_flock_logging_trace >= 5"
+ "WarehousePleaseRetransmitFromTime"
+ "[FigPlaybackTimer %!p(MISSING)]: timebase: %!@(MISSING), dispatch_source %!p(MISSING)"
+ "adding timebase listener failed"
+ "anchored time"
+ "assetOption_DisableL4S"
+ "bad overlap range"
+ "bossTrackRangeIncludesAnyVideoProcessorSourceTrack"
+ "com.apple.coremedia.logging.flock"
+ "com.apple.quicktime-audio"
+ "com.apple.sonic.music"
+ "enableL4S"
+ "failed to allocate trackIDs"
+ "fl_logLockAcquisition"
+ "fl_logUnlock"
+ "flock held too long"
+ "flockLoggerTimerCallback"
+ "flockLogger_Log"
+ "flockLogger_LogAll"
+ "hlspersistent_flock_logging_trace"
+ "item timer start failed"
+ "itemfig_hasTrackReference"
+ "itemfig_reuseRenderTriplesForVideoComposition"
+ "itemoverlap_getEffectiveOverlappedPlaybackEndTime"
+ "itemoverlap_getEndTime"
+ "kFigPlaybackTimerError_AlreadyStarted"
+ "kFigPlaybackTimerError_ParamErr"
+ "overlapped playback end time wrong type"
+ "overlapped playback end time zero or less"
+ "playerairplay_SetPiPMuteOnBufferedAudio"
+ "playerairplay_handleSetProperty_block_invoke_2"
+ "playeroverlap_copyOverlappedPlaybackEndTime"
+ "playeroverlap_copyOverlappedPlaybackEndTimeInPlayerQueue"
+ "playeroverlap_maybeScheduleOverlappedPlaybackEndTime"
+ "playeroverlap_overlappedPlaybackEndTimeReached"
+ "playeroverlap_setOverlapRangeProperty failed"
+ "playeroverlap_setOverlappedPlaybackEndTime"
+ "playeroverlap_setOverlappedPlaybackEndTimeInPlayerQueue"
+ "playing time"
+ "qta"
+ "remove timer source failed"
+ "removing timebase listener failed"
+ "set_enablesL4S:"
+ "time is not numeric"
+ "timer already canceled"
+ "timer already started"
- "<<<< FAQ >>>> %!s(MISSING): [%!p(MISSING)] setting cryptor to %!p(MISSING), was %!p(MISSING)"
- "<<<< FigPlayerOverlap >>>> %!s(MISSING): Failed to remove timebase listeners with error %!d(MISSING)"
- "<<<< FigPlayerOverlap >>>> %!s(MISSING): [%!p(MISSING)|%!{(MISSING)public}s] beginning outro of <%!p(MISSING)|%!{(MISSING)public}s> current time %!f(MISSING) overlapping with <%!p(MISSING)|%!{(MISSING)public}s> current time %!f(MISSING) at host time %!f(MISSING)."
- "<<<< FigPlayerOverlap >>>> %!s(MISSING): [%!p(MISSING)|%!{(MISSING)public}s] success, advance time %!f(MISSING) set as anchor time %!f(MISSING) (now %!f(MISSING) + %!f(MISSING)) on sub-player %!p(MISSING), outro timebase time %!f(MISSING)."
- "<<<< FigPlayerOverlap >>>> %!s(MISSING): [player %!p(MISSING)|%!{(MISSING)public}s] item <%!p(MISSING)|%!{(MISSING)public}s>: timebase %!p(MISSING) %!{(MISSING)public}@"
- "<<<< FigPlayerOverlap >>>> %!s(MISSING): add timebase listener failed"
- "<<<< FigStreamPlayer >>>> %!s(MISSING): [%!p(MISSING)|%!{(MISSING)public}s] <%!p(MISSING)|%!{(MISSING)public}s>: Item ordinal (%!d(MISSING)) attempted to steal buffers from an existing audio renderChain %!p(MISSING), backed by %!@(MISSING), for track %!l(MISSING)d but encountered error %!d(MISSING)"
- "<<<< MENTOROUTPUT >>>> %!s(MISSING): (%!p(MISSING)): buffer queue duration is %!f(MISSING), high water mark is %!f(MISSING), returning %!s(MISSING)"
- "<<<< OUTPUTTOFORMATWRITER >>>> %!s(MISSING): (%!p(MISSING)): buffer queue duration is %!f(MISSING), high water mark is %!f(MISSING), returning %!s(MISSING)"
- "<FigPlaybackItemOverlap %!p(MISSING) %!s(MISSING) sub-item %!p(MISSING) advanceTime %!f(MISSING)>"
- "FigSampleBufferConsumerCreateForBufferQueue"
- "add timebase listener failed"

```
