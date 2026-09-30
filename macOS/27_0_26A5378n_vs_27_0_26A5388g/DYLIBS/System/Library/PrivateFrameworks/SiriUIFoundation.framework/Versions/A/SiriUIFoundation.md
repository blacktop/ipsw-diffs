## SiriUIFoundation

> `/System/Library/PrivateFrameworks/SiriUIFoundation.framework/Versions/A/SiriUIFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-3600.55.26.0.0
-  __TEXT.__text: 0x7f0cc
-  __TEXT.__objc_methlist: 0x4300
-  __TEXT.__const: 0x32cc
-  __TEXT.__cstring: 0x62b6
-  __TEXT.__oslogstring: 0x5c87
-  __TEXT.__gcc_except_tab: 0x9b4
+3600.55.30.0.0
+  __TEXT.__text: 0x7ea80
+  __TEXT.__objc_methlist: 0x4310
+  __TEXT.__const: 0x32dc
+  __TEXT.__cstring: 0x6176
+  __TEXT.__oslogstring: 0x5c17
+  __TEXT.__gcc_except_tab: 0x954
   __TEXT.__ustring: 0x22
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__swift5_typeref: 0x119e

   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_assocty: 0x228
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x21d8
+  __TEXT.__unwind_info: 0x21b8
   __TEXT.__eh_frame: 0x1950
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x158
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c18
+  __DATA_CONST.__objc_selrefs: 0x2c28
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x908
-  __AUTH_CONST.__const: 0x4bb1
-  __AUTH_CONST.__cfstring: 0x2240
-  __AUTH_CONST.__objc_const: 0x8848
+  __AUTH_CONST.__const: 0x4b01
+  __AUTH_CONST.__cfstring: 0x21e0
+  __AUTH_CONST.__objc_const: 0x88a8
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0xbb8
+  __AUTH_CONST.__auth_got: 0xbb0
   __AUTH.__objc_data: 0xff0
   __AUTH.__data: 0xb98
-  __DATA.__objc_ivar: 0x3fc
+  __DATA.__objc_ivar: 0x408
   __DATA.__data: 0x1520
-  __DATA.__bss: 0x4100
+  __DATA.__bss: 0x40f0
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0xef8
   __DATA_DIRTY.__data: 0x8c8
-  __DATA_DIRTY.__bss: 0x230
+  __DATA_DIRTY.__bss: 0x210
   __DATA_DIRTY.__common: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3111
-  Symbols:   4610
-  CStrings:  1042
+  Functions: 3100
+  Symbols:   4590
+  CStrings:  1037
 
Symbols:
+ -[SRUIFStateFeedbackDefaultProvider isFadingOut]
+ -[SRUIFStateFeedbackDefaultProvider setPlaybackBarrierEngaged:]
+ -[SRUIFStateFeedbackManager _fadeProcessingFeedbackAtResponseStart]
+ -[SRUIFStateFeedbackManager lastScheduledDelayToneInterval]
+ GCC_except_table29
+ GCC_except_table45
+ GCC_except_table56
+ GCC_except_table62
+ OBJC_IVAR_$_SRUIFStateFeedbackDefaultProvider._isFadingOut
+ OBJC_IVAR_$_SRUIFStateFeedbackDefaultProvider._playbackBarrierEngaged
+ OBJC_IVAR_$_SRUIFStateFeedbackManager._lastScheduledDelayToneInterval
+ _objc_msgSend$_fadeProcessingFeedbackAtResponseStart
- -[SRUIFStateFeedbackDefaultProvider _startLatencyResponseFeedback:withCompletion:]
- -[SRUIFStateFeedbackManager _playLatencyResponseFeedback]
- GCC_except_table19
- GCC_except_table21
- GCC_except_table23
- GCC_except_table28
- GCC_except_table33
- GCC_except_table57
- GCC_except_table63
- GCC_except_table68
- GCC_except_table72
- _AFSoundIDGetName
- __82-[SRUIFStateFeedbackDefaultProvider _startLatencyResponseFeedback:withCompletion:]_block_invoke
- __82-[SRUIFStateFeedbackDefaultProvider _startLatencyResponseFeedback:withCompletion:]_block_invoke_2
- ___57-[SRUIFStateFeedbackManager _playLatencyResponseFeedback]_block_invoke
- ___82-[SRUIFStateFeedbackDefaultProvider _startLatencyResponseFeedback:withCompletion:]_block_invoke
- ___82-[SRUIFStateFeedbackDefaultProvider _startLatencyResponseFeedback:withCompletion:]_block_invoke_2
- ___block_descriptor_40_e8_32w_e20_v24?0q8"NSError"16l
- ___latencyResponseFadeInDuration_block_invoke
- ___latencyResponseFadeOutDuration_block_invoke
- ___latencyResponseLoopCount_block_invoke
- ___latencyResponseVolume_block_invoke
- _objc_msgSend$_playLatencyResponseFeedback
- _objc_msgSend$_startLatencyResponseFeedback:withCompletion:
- latencyResponseFadeInDuration.cachedValue
- latencyResponseFadeInDuration.onceToken
- latencyResponseFadeOutDuration.cachedValue
- latencyResponseFadeOutDuration.onceToken
- latencyResponseLoopCount.cachedValue
- latencyResponseLoopCount.onceToken
- latencyResponseVolume.cachedValue
- latencyResponseVolume.onceToken
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
