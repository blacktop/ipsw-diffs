## SiriUIFoundation

> `/System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-3600.55.26.0.0
-  __TEXT.__text: 0x916d8
-  __TEXT.__objc_methlist: 0x46a8
-  __TEXT.__const: 0x388c
-  __TEXT.__cstring: 0x6836
-  __TEXT.__oslogstring: 0x703b
-  __TEXT.__gcc_except_tab: 0x9dc
+3600.55.30.0.0
+  __TEXT.__text: 0x910e8
+  __TEXT.__objc_methlist: 0x46b8
+  __TEXT.__const: 0x389c
+  __TEXT.__cstring: 0x66f6
+  __TEXT.__oslogstring: 0x6fcb
+  __TEXT.__gcc_except_tab: 0x97c
   __TEXT.__ustring: 0x22
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__swift5_typeref: 0x1594

   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_assocty: 0x228
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x26b8
+  __TEXT.__unwind_info: 0x2690
   __TEXT.__eh_frame: 0x23c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x19a0
+  __DATA_CONST.__const: 0x1978
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x160
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f28
+  __DATA_CONST.__objc_selrefs: 0x2f38
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__got: 0xa78
-  __AUTH_CONST.__const: 0x3b21
-  __AUTH_CONST.__cfstring: 0x2400
-  __AUTH_CONST.__objc_const: 0x8f90
+  __AUTH_CONST.__const: 0x3aa1
+  __AUTH_CONST.__cfstring: 0x23a0
+  __AUTH_CONST.__objc_const: 0x8ff0
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0xf40
+  __AUTH_CONST.__auth_got: 0xf38
   __AUTH.__objc_data: 0x1170
   __AUTH.__data: 0xc28
-  __DATA.__objc_ivar: 0x424
+  __DATA.__objc_ivar: 0x430
   __DATA.__data: 0x1768
-  __DATA.__bss: 0x4680
+  __DATA.__bss: 0x4670
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0xf48
   __DATA_DIRTY.__data: 0x9d0
-  __DATA_DIRTY.__bss: 0x238
+  __DATA_DIRTY.__bss: 0x208
   __DATA_DIRTY.__common: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3369
-  Symbols:   4825
-  CStrings:  1137
+  Functions: 3358
+  Symbols:   4809
+  CStrings:  1132
 
Symbols:
+ -[SRUIFStateFeedbackDefaultProvider isFadingOut]
+ -[SRUIFStateFeedbackDefaultProvider setPlaybackBarrierEngaged:]
+ -[SRUIFStateFeedbackManager _fadeProcessingFeedbackAtResponseStart]
+ -[SRUIFStateFeedbackManager lastScheduledDelayToneInterval]
+ GCC_except_table22
+ GCC_except_table31
+ GCC_except_table56
+ _OBJC_IVAR_$_SRUIFStateFeedbackDefaultProvider._isFadingOut
+ _OBJC_IVAR_$_SRUIFStateFeedbackDefaultProvider._playbackBarrierEngaged
+ _OBJC_IVAR_$_SRUIFStateFeedbackManager._lastScheduledDelayToneInterval
+ _objc_msgSend$_fadeProcessingFeedbackAtResponseStart
- -[SRUIFStateFeedbackDefaultProvider _startLatencyResponseFeedback:withCompletion:]
- -[SRUIFStateFeedbackManager _playLatencyResponseFeedback]
- GCC_except_table15
- GCC_except_table21
- GCC_except_table24
- GCC_except_table45
- GCC_except_table49
- GCC_except_table54
- _AFSoundIDGetName
- ___57-[SRUIFStateFeedbackManager _playLatencyResponseFeedback]_block_invoke
- ___82-[SRUIFStateFeedbackDefaultProvider _startLatencyResponseFeedback:withCompletion:]_block_invoke
- ___82-[SRUIFStateFeedbackDefaultProvider _startLatencyResponseFeedback:withCompletion:]_block_invoke_2
- ___block_descriptor_40_e8_32w_e20_v24?0q8"NSError"16lw32l8
- ___latencyResponseFadeInDuration_block_invoke
- ___latencyResponseFadeOutDuration_block_invoke
- ___latencyResponseLoopCount_block_invoke
- ___latencyResponseVolume_block_invoke
- _latencyResponseFadeInDuration.cachedValue
- _latencyResponseFadeInDuration.onceToken
- _latencyResponseFadeOutDuration.cachedValue
- _latencyResponseFadeOutDuration.onceToken
- _latencyResponseLoopCount.cachedValue
- _latencyResponseLoopCount.onceToken
- _latencyResponseVolume.cachedValue
- _latencyResponseVolume.onceToken
- _objc_msgSend$_playLatencyResponseFeedback
- _objc_msgSend$_startLatencyResponseFeedback:withCompletion:
CStrings:
+ "%s #statefeedback Fade-out started, suppressing further volume decay"
+ "%s #statefeedback Playback barrier %@"
+ "%s #statefeedback Playback barrier engaged; rejecting audio session acquisition and playback"
+ "%s #statefeedback Playback barrier engaged; rejecting playAudioPlaybackRequest"
+ "%s #statefeedback Playback barrier engaged; rejecting state feedback type %ld"
+ "%s #statefeedback Volume decay reschedule suppressed - fade-out in progress"
+ "%s #statefeedback Volume decay suppressed - fade-out in progress"
+ "%s #statefeedback fading processing loop at TTS start"
+ "%s #statefeedback no processing feedback in flight at TTS start; nothing to fade"
+ "%s #statefeedback synthesis response TTS did finish, canceling feedback"
+ "%s #statefeedback synthesis response TTS will start, fading out the processing loop"
+ "%s #tts [stopStream] [rdar://178734021] Stream %@ is queued or activating, deferring stop until the stream starts (fix active)"
+ "-[SRUIFStateFeedbackDefaultProvider setPlaybackBarrierEngaged:]"
+ "-[SRUIFStateFeedbackManager _fadeProcessingFeedbackAtResponseStart]"
+ "Playback barrier engaged"
+ "disengaged"
+ "engaged"
- "%s #statefeedback Failed to play latencyResponse tone with error: %@"
- "%s #statefeedback Playing siriLatencyResponse tone for synthesis transition (latencyResponseFadeOutDuration: %f)"
- "%s #statefeedback latency response feedback not needed. Skipping latency response tone"
- "%s #statefeedback latency response feedback started with error, inform delegate anyway"
- "%s #statefeedback latency response feedback started, inform delegate immediately"
- "%s #statefeedback playing latency response feedback for synthesis transition"
- "%s #statefeedback siriLatencyResponse audio resource not found, not playing latency response tone"
- "%s #statefeedback siriLatencyResponse sound not found, using %@"
- "%s #statefeedback synthesis response TTS did finish, canceling latency response tone"
- "%s #statefeedback synthesis response TTS will start, transitioning from delay to latency response tone"
- "%s #tts [stopStream] Stream %@ is being processed (audio session activating), deferring stop"
- "%s #tts [stopStream] Waiting for the stream task to begin processing"
- "-[SRUIFStateFeedbackDefaultProvider _startLatencyResponseFeedback:withCompletion:]"
- "-[SRUIFStateFeedbackDefaultProvider _startLatencyResponseFeedback:withCompletion:]_block_invoke_2"
- "-[SRUIFStateFeedbackManager _playLatencyResponseFeedback]"
- "-[SRUIFStateFeedbackManager _playLatencyResponseFeedback]_block_invoke"
- "SRUIFSiriStateFeedbackTypeLatencyResponse"
- "SiriLatencyResponseFadeInDuration"
- "SiriLatencyResponseFadeOutDuration"
- "SiriLatencyResponseLoopCount"
- "SiriLatencyResponseVolume"
- "siriLatencyResponse"
```
