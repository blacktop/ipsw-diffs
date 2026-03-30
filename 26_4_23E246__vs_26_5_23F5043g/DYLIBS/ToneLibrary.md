## ToneLibrary

> `/System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary`

```diff

-663.503.300.0.0
-  __TEXT.__text: 0x4c8ec
-  __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_methlist: 0x2de0
-  __TEXT.__const: 0x160
-  __TEXT.__gcc_except_tab: 0x16c8
-  __TEXT.__cstring: 0x60ae
-  __TEXT.__oslogstring: 0xdd03
+663.602.0.0.0
+  __TEXT.__text: 0x4de98
+  __TEXT.__auth_stubs: 0x8e0
+  __TEXT.__objc_methlist: 0x30a0
+  __TEXT.__const: 0x170
+  __TEXT.__gcc_except_tab: 0x1764
+  __TEXT.__cstring: 0x64e4
+  __TEXT.__oslogstring: 0xdf65
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x534
-  __TEXT.__unwind_info: 0x1290
-  __TEXT.__objc_classname: 0x597
-  __TEXT.__objc_methname: 0xad2f
-  __TEXT.__objc_methtype: 0x1136
-  __TEXT.__objc_stubs: 0x7140
-  __DATA_CONST.__got: 0x458
+  __TEXT.__unwind_info: 0x12f8
+  __TEXT.__objc_classname: 0x599
+  __TEXT.__objc_methname: 0xb8f8
+  __TEXT.__objc_methtype: 0x10b6
+  __TEXT.__objc_stubs: 0x7740
+  __DATA_CONST.__got: 0x450
   __DATA_CONST.__const: 0x1950
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2110
+  __DATA_CONST.__objc_selrefs: 0x22a0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x480
+  __AUTH_CONST.__auth_got: 0x488
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x5b40
-  __AUTH_CONST.__objc_const: 0x4e50
+  __AUTH_CONST.__cfstring: 0x5fa0
+  __AUTH_CONST.__objc_const: 0x5300
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x44c
+  __DATA.__objc_ivar: 0x4ac
   __DATA.__data: 0x3e0
   __DATA.__common: 0x4
   __DATA.__bss: 0x240

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 597D0FB7-E128-349A-8B74-F844BB05F3D5
-  Functions: 1429
-  Symbols:   5375
-  CStrings:  3852
+  UUID: 047D08A0-C77A-3635-A9F8-AB9C455CEB4C
+  Functions: 1487
+  Symbols:   5566
+  CStrings:  4019
 
Symbols:
+ +[TLAttentionAwarenessEffectCoordinator targetCutoffFrequencyForEffectMix:]
+ +[TLAttentionAwarenessEffectCoordinator targetGlobalGainReductionForEffectMix:initialVolume:]
+ +[TLAttentionAwarenessEffectCoordinator targetReverbWetDryMixForEffectMix:]
+ +[TLAttentionAwarenessEffectProcessor targetCutoffFrequencyForEffectMix:]
+ +[TLAttentionAwarenessEffectProcessor targetGlobalGainReductionForEffectMix:initialVolume:]
+ +[TLAttentionAwarenessEffectProcessor targetReverbWetDryMixForEffectMix:]
+ -[TLAlertQueuePlayerAnalytics attenuatedCutoffFrequency]
+ -[TLAlertQueuePlayerAnalytics attenuatedGlobalGainReduction]
+ -[TLAlertQueuePlayerAnalytics attenuatedReverbMix]
+ -[TLAlertQueuePlayerAnalytics attenuationRampInStartTime]
+ -[TLAlertQueuePlayerAnalytics attenuationRampInStopTime]
+ -[TLAlertQueuePlayerAnalytics attenuationRampOutStartTime]
+ -[TLAlertQueuePlayerAnalytics attenuationRampOutStopTime]
+ -[TLAlertQueuePlayerAnalytics didReachAttenuationTimeout]
+ -[TLAlertQueuePlayerAnalytics setAttenuatedCutoffFrequency:]
+ -[TLAlertQueuePlayerAnalytics setAttenuatedGlobalGainReduction:]
+ -[TLAlertQueuePlayerAnalytics setAttenuatedReverbMix:]
+ -[TLAlertQueuePlayerAnalytics setAttenuationRampInStartTime:]
+ -[TLAlertQueuePlayerAnalytics setAttenuationRampInStopTime:]
+ -[TLAlertQueuePlayerAnalytics setAttenuationRampOutStartTime:]
+ -[TLAlertQueuePlayerAnalytics setAttenuationRampOutStopTime:]
+ -[TLAlertQueuePlayerAnalytics setDidReachAttenuationTimeout:]
+ -[TLAlertQueuePlayerAnalytics setTargetAttenuatedCutoffFrequency:]
+ -[TLAlertQueuePlayerAnalytics setTargetAttenuatedGlobalGainReduction:]
+ -[TLAlertQueuePlayerAnalytics setTargetAttenuatedReverbMix:]
+ -[TLAlertQueuePlayerAnalytics setTargetAttenuationRampInDuration:]
+ -[TLAlertQueuePlayerAnalytics setTargetAttenuationRampOutDuration:]
+ -[TLAlertQueuePlayerAnalytics setTargetAttenuationTimeoutDuration:]
+ -[TLAlertQueuePlayerAnalytics setTargetUnattenuatedCutoffFrequency:]
+ -[TLAlertQueuePlayerAnalytics setTargetUnattenuatedGlobalGainReduction:]
+ -[TLAlertQueuePlayerAnalytics setTargetUnattenuatedReverbMix:]
+ -[TLAlertQueuePlayerAnalytics setUnattenuatedCutoffFrequency:]
+ -[TLAlertQueuePlayerAnalytics setUnattenuatedGlobalGainReduction:]
+ -[TLAlertQueuePlayerAnalytics setUnattenuatedReverbMix:]
+ -[TLAlertQueuePlayerAnalytics targetAttenuatedCutoffFrequency]
+ -[TLAlertQueuePlayerAnalytics targetAttenuatedGlobalGainReduction]
+ -[TLAlertQueuePlayerAnalytics targetAttenuatedReverbMix]
+ -[TLAlertQueuePlayerAnalytics targetAttenuationRampInDuration]
+ -[TLAlertQueuePlayerAnalytics targetAttenuationRampOutDuration]
+ -[TLAlertQueuePlayerAnalytics targetAttenuationTimeoutDuration]
+ -[TLAlertQueuePlayerAnalytics targetUnattenuatedCutoffFrequency]
+ -[TLAlertQueuePlayerAnalytics targetUnattenuatedGlobalGainReduction]
+ -[TLAlertQueuePlayerAnalytics targetUnattenuatedReverbMix]
+ -[TLAlertQueuePlayerAnalytics unattenuatedCutoffFrequency]
+ -[TLAlertQueuePlayerAnalytics unattenuatedGlobalGainReduction]
+ -[TLAlertQueuePlayerAnalytics unattenuatedReverbMix]
+ -[TLAlertQueuePlayerController _cancelAttentionAwarenessDuckingTimerForStateDescriptor:]
+ -[TLAlertQueuePlayerController _enableAttenuatedHapticTrack:]
+ -[TLAlertQueuePlayerController _handleAttentionAwarenessDuckingTimeoutForStateDescriptor:]
+ -[TLAlertQueuePlayerController _performAttentionAwarenessDuckingTimeoutActionForStateDescriptor:]
+ -[TLAlertQueuePlayerController _startAttentionAwarenessDuckingTimerForStateDescriptor:]
+ -[TLAttentionAwarenessEffectCoordinator currentCutoffFrequency]
+ -[TLAttentionAwarenessEffectCoordinator currentLowPassFilterGlobalGain]
+ -[TLAttentionAwarenessEffectCoordinator currentReverbWetDryMix]
+ -[TLAttentionAwarenessEffectCoordinator effectMix]
+ -[TLAttentionAwarenessEffectCoordinator initWithAudioSession:initialVolume:]
+ -[TLAttentionAwarenessEffectCoordinator initialVolume]
+ -[TLAttentionAwarenessEffectCoordinator setEffectMix:]
+ -[TLAttentionAwarenessEffectCoordinator setEffectMix:effectMixFadeDuration:completion:]
+ -[TLAttentionAwarenessEffectCoordinator setInitialVolume:]
+ -[TLAttentionAwarenessEffectProcessor currentCutoffFrequency]
+ -[TLAttentionAwarenessEffectProcessor currentLowPassFilterGlobalGain]
+ -[TLAttentionAwarenessEffectProcessor currentReverbWetDryMix]
+ -[TLAttentionAwarenessEffectProcessor effectMix]
+ -[TLAttentionAwarenessEffectProcessor initWithProcessingFormat:framesPerRender:audioSession:initialEffectMix:initialVolume:]
+ -[TLAttentionAwarenessEffectProcessor initWithProcessingFormat:framesPerRender:audioSession:initialEffectMix:initialVolume:].cold.1
+ -[TLAttentionAwarenessEffectProcessor initWithProcessingFormat:framesPerRender:audioSession:initialEffectMix:initialVolume:].cold.2
+ -[TLAttentionAwarenessEffectProcessor initWithProcessingFormat:framesPerRender:audioSession:initialEffectMix:initialVolume:].cold.3
+ -[TLAttentionAwarenessEffectProcessor setEffectMix:]
+ -[TLAttentionAwarenessEffectProcessor setEffectMix:effectMixFadeDuration:completion:]
+ GCC_except_table18
+ GCC_except_table46
+ GCC_except_table56
+ GCC_except_table91
+ _OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._attenuatedCutoffFrequency
+ _OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._attenuatedGlobalGainReduction
+ _OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._attenuatedReverbMix
+ _OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._attenuationRampInStartTime
+ _OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._attenuationRampInStopTime
+ _OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._attenuationRampOutStartTime
+ _OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._attenuationRampOutStopTime
+ _OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._didReachAttenuationTimeout
+ _OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._targetAttenuatedCutoffFrequency
+ _OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._targetAttenuatedGlobalGainReduction
+ _OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._targetAttenuatedReverbMix
+ _OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._targetAttenuationRampInDuration
+ _OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._targetAttenuationRampOutDuration
+ _OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._targetAttenuationTimeoutDuration
+ _OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._targetUnattenuatedCutoffFrequency
+ _OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._targetUnattenuatedGlobalGainReduction
+ _OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._targetUnattenuatedReverbMix
+ _OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._unattenuatedCutoffFrequency
+ _OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._unattenuatedGlobalGainReduction
+ _OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._unattenuatedReverbMix
+ _OBJC_IVAR_$_TLAlertQueuePlayerController._attentionAwarenessDuckingTimerSource
+ _OBJC_IVAR_$_TLAttentionAwarenessEffectCoordinator._effectMix
+ _OBJC_IVAR_$_TLAttentionAwarenessEffectCoordinator._initialVolume
+ _OBJC_IVAR_$_TLAttentionAwarenessEffectProcessor._currentEffectMix
+ _OBJC_IVAR_$_TLAttentionAwarenessEffectProcessor._effectMix
+ _OBJC_IVAR_$_TLAttentionAwarenessEffectProcessor._initialVolume
+ __OBJC_$_CLASS_METHODS_TLAttentionAwarenessEffectCoordinator
+ __OBJC_$_CLASS_METHODS_TLAttentionAwarenessEffectProcessor
+ ___124-[TLAttentionAwarenessEffectProcessor initWithProcessingFormat:framesPerRender:audioSession:initialEffectMix:initialVolume:]_block_invoke
+ ___48-[TLAttentionAwarenessEffectProcessor effectMix]_block_invoke
+ ___61-[TLAttentionAwarenessEffectProcessor currentCutoffFrequency]_block_invoke
+ ___61-[TLAttentionAwarenessEffectProcessor currentReverbWetDryMix]_block_invoke
+ ___69-[TLAttentionAwarenessEffectProcessor currentLowPassFilterGlobalGain]_block_invoke
+ ___83-[TLAlertQueuePlayerController _didPrepareToPlayMusicForStateDescriptor:withError:]_block_invoke.158
+ ___85-[TLAttentionAwarenessEffectProcessor setEffectMix:effectMixFadeDuration:completion:]_block_invoke
+ ___85-[TLAttentionAwarenessEffectProcessor setEffectMix:effectMixFadeDuration:completion:]_block_invoke.19
+ ___85-[TLAttentionAwarenessEffectProcessor setEffectMix:effectMixFadeDuration:completion:]_block_invoke.20
+ ___85-[TLAttentionAwarenessEffectProcessor setEffectMix:effectMixFadeDuration:completion:]_block_invoke.cold.1
+ ___87-[TLAlertQueuePlayerController _didReceiveAttentionPollingEventOfType:stateDescriptor:]_block_invoke
+ ___87-[TLAlertQueuePlayerController _didReceiveAttentionPollingEventOfType:stateDescriptor:]_block_invoke_2
+ ___87-[TLAlertQueuePlayerController _startAttentionAwarenessDuckingTimerForStateDescriptor:]_block_invoke
+ ___97-[TLAlertQueuePlayerController _performAttentionAwarenessDuckingTimeoutActionForStateDescriptor:]_block_invoke
+ ___97-[TLAlertQueuePlayerController _performAttentionAwarenessDuckingTimeoutActionForStateDescriptor:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_68_e8_32s40bs48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_72_e8_32bs40r48w_e5_v8?0lw48l8r40l8s32l8
+ _log10f
+ _objc_msgSend$_cancelAttentionAwarenessDuckingTimerForStateDescriptor:
+ _objc_msgSend$_enableAttenuatedHapticTrack:
+ _objc_msgSend$_handleAttentionAwarenessDuckingTimeoutForStateDescriptor:
+ _objc_msgSend$_performAttentionAwarenessDuckingTimeoutActionForStateDescriptor:
+ _objc_msgSend$_startAttentionAwarenessDuckingTimerForStateDescriptor:
+ _objc_msgSend$attenuatedCutoffFrequency
+ _objc_msgSend$attenuatedGlobalGainReduction
+ _objc_msgSend$attenuatedReverbMix
+ _objc_msgSend$attenuationRampInStartTime
+ _objc_msgSend$attenuationRampInStopTime
+ _objc_msgSend$attenuationRampOutStartTime
+ _objc_msgSend$attenuationRampOutStopTime
+ _objc_msgSend$bandwidth
+ _objc_msgSend$currentCutoffFrequency
+ _objc_msgSend$currentLowPassFilterGlobalGain
+ _objc_msgSend$currentReverbWetDryMix
+ _objc_msgSend$didReachAttenuationTimeout
+ _objc_msgSend$initWithAudioSession:initialVolume:
+ _objc_msgSend$initWithProcessingFormat:framesPerRender:audioSession:initialEffectMix:initialVolume:
+ _objc_msgSend$initialVolume
+ _objc_msgSend$setAttenuatedCutoffFrequency:
+ _objc_msgSend$setAttenuatedGlobalGainReduction:
+ _objc_msgSend$setAttenuatedReverbMix:
+ _objc_msgSend$setAttenuationRampInStartTime:
+ _objc_msgSend$setAttenuationRampInStopTime:
+ _objc_msgSend$setAttenuationRampOutStartTime:
+ _objc_msgSend$setAttenuationRampOutStopTime:
+ _objc_msgSend$setBandwidth:
+ _objc_msgSend$setDidReachAttenuationTimeout:
+ _objc_msgSend$setEffectMix:
+ _objc_msgSend$setEffectMix:effectMixFadeDuration:completion:
+ _objc_msgSend$setFilterType:
+ _objc_msgSend$setFrequency:
+ _objc_msgSend$setGain:
+ _objc_msgSend$setTargetAttenuatedCutoffFrequency:
+ _objc_msgSend$setTargetAttenuatedGlobalGainReduction:
+ _objc_msgSend$setTargetAttenuatedReverbMix:
+ _objc_msgSend$setTargetAttenuationRampInDuration:
+ _objc_msgSend$setTargetAttenuationRampOutDuration:
+ _objc_msgSend$setTargetAttenuationTimeoutDuration:
+ _objc_msgSend$setTargetUnattenuatedCutoffFrequency:
+ _objc_msgSend$setTargetUnattenuatedGlobalGainReduction:
+ _objc_msgSend$setTargetUnattenuatedReverbMix:
+ _objc_msgSend$setUnattenuatedCutoffFrequency:
+ _objc_msgSend$setUnattenuatedGlobalGainReduction:
+ _objc_msgSend$setUnattenuatedReverbMix:
+ _objc_msgSend$setWetDryMix:
+ _objc_msgSend$targetAttenuatedCutoffFrequency
+ _objc_msgSend$targetAttenuatedGlobalGainReduction
+ _objc_msgSend$targetAttenuatedReverbMix
+ _objc_msgSend$targetAttenuationRampInDuration
+ _objc_msgSend$targetAttenuationRampOutDuration
+ _objc_msgSend$targetAttenuationTimeoutDuration
+ _objc_msgSend$targetCutoffFrequencyForEffectMix:
+ _objc_msgSend$targetGlobalGainReductionForEffectMix:initialVolume:
+ _objc_msgSend$targetReverbWetDryMixForEffectMix:
+ _objc_msgSend$targetUnattenuatedCutoffFrequency
+ _objc_msgSend$targetUnattenuatedGlobalGainReduction
+ _objc_msgSend$targetUnattenuatedReverbMix
+ _objc_msgSend$unattenuatedCutoffFrequency
+ _objc_msgSend$unattenuatedGlobalGainReduction
+ _objc_msgSend$unattenuatedReverbMix
- -[TLAttentionAwarenessEffectCoordinator effectParameters]
- -[TLAttentionAwarenessEffectCoordinator initWithEffectParameters:audioSession:]
- -[TLAttentionAwarenessEffectCoordinator setEffectParameters:]
- -[TLAttentionAwarenessEffectCoordinator setEffectParameters:effectMixFadeDuration:]
- -[TLAttentionAwarenessEffectProcessor _applyEffectParameters:includingEffectMix:]
- -[TLAttentionAwarenessEffectProcessor _applyEffectParameters:includingEffectMix:].cold.1
- -[TLAttentionAwarenessEffectProcessor _applyEffectParameters:includingEffectMix:].cold.2
- -[TLAttentionAwarenessEffectProcessor _currentEffectMix]
- -[TLAttentionAwarenessEffectProcessor effectParameters]
- -[TLAttentionAwarenessEffectProcessor initWithProcessingFormat:framesPerRender:audioSession:effectParameters:]
- -[TLAttentionAwarenessEffectProcessor initWithProcessingFormat:framesPerRender:audioSession:effectParameters:].cold.1
- -[TLAttentionAwarenessEffectProcessor initWithProcessingFormat:framesPerRender:audioSession:effectParameters:].cold.2
- -[TLAttentionAwarenessEffectProcessor initWithProcessingFormat:framesPerRender:audioSession:effectParameters:].cold.3
- -[TLAttentionAwarenessEffectProcessor setEffectParameters:]
- -[TLAttentionAwarenessEffectProcessor setEffectParameters:effectMixFadeDuration:]
- GCC_except_table10
- GCC_except_table12
- _OBJC_CLASS_$_AVAudioConnectionPoint
- _OBJC_IVAR_$_TLAttentionAwarenessEffectCoordinator._effectParameters
- _OBJC_IVAR_$_TLAttentionAwarenessEffectProcessor._effectParameters
- _TLAttentionAwarenessEffectParametersMake
- ___110-[TLAttentionAwarenessEffectProcessor initWithProcessingFormat:framesPerRender:audioSession:effectParameters:]_block_invoke
- ___110-[TLAttentionAwarenessEffectProcessor initWithProcessingFormat:framesPerRender:audioSession:effectParameters:]_block_invoke.21
- ___55-[TLAttentionAwarenessEffectProcessor effectParameters]_block_invoke
- ___81-[TLAttentionAwarenessEffectProcessor setEffectParameters:effectMixFadeDuration:]_block_invoke
- ___81-[TLAttentionAwarenessEffectProcessor setEffectParameters:effectMixFadeDuration:]_block_invoke.26
- ___81-[TLAttentionAwarenessEffectProcessor setEffectParameters:effectMixFadeDuration:]_block_invoke.27
- ___81-[TLAttentionAwarenessEffectProcessor setEffectParameters:effectMixFadeDuration:]_block_invoke.cold.1
- ___83-[TLAlertQueuePlayerController _didPrepareToPlayMusicForStateDescriptor:withError:]_block_invoke.150
- ___block_descriptor_40_e8_32s_e46_v32?0"AVAudioUnitEQFilterParameters"8Q16^B24ls32l8
- ___block_descriptor_60_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_64_e8_32r40w_e5_v8?0lw40l8r32l8
- _objc_msgSend$_applyEffectParameters:includingEffectMix:
- _objc_msgSend$_currentEffectMix
- _objc_msgSend$bypass
- _objc_msgSend$connect:to:fromBus:toBus:format:
- _objc_msgSend$connect:toConnectionPoints:fromBus:format:
- _objc_msgSend$destinationForMixer:bus:
- _objc_msgSend$effectParameters
- _objc_msgSend$enumerateObjectsUsingBlock:
- _objc_msgSend$filterType
- _objc_msgSend$initWithEffectParameters:audioSession:
- _objc_msgSend$initWithNode:bus:
- _objc_msgSend$initWithProcessingFormat:framesPerRender:audioSession:effectParameters:
- _objc_msgSend$setEffectParameters:
- _objc_msgSend$setEffectParameters:effectMixFadeDuration:
CStrings:
+ "%{public}@: -_cancelAttentionAwarenessDuckingTimerForStateDescriptor:(%{public}@): Canceling ducking timer for tone: %{public}@."
+ "%{public}@: -_enableAttenuatedHapticTrack:(%s) […]: [hapticPlayerItemTrack setActiveHapticChannelIndex:%ld] on %{public}@."
+ "%{public}@: -_enableAttenuatedHapticTrack:(disabled) […]: [attenuatedHapticPlayerItemTrack setMutesHaptics:%@] on %{public}@."
+ "%{public}@: -_enableAttenuatedHapticTrack:(enabled) […]: [hapticPlayerItemTrack setMutesHaptics:%@] on %{public}@."
+ "%{public}@: -_handleAttentionAwarenessDuckingTimeoutForStateDescriptor:(%{public}@) currentToneIdentifier:(%{public}@)."
+ "%{public}@: -_handleAttentionAwarenessDuckingTimeout…: Same ducked tone (%{public}@) has been playing for %.0f seconds. Triggering ducking timeout action."
+ "%{public}@: -_handleAttentionAwarenessDuckingTimeout…: Tone has changed or playback stopped. Current: %{public}@, Expected: %{public}@. No action needed."
+ "%{public}@: -_performAttentionAwarenessDuckingTimeoutActionForStateDescriptor:(%{public}@) toneIdentifier:(%{public}@)."
+ "%{public}@: -_startAttentionAwarenessDuckingTimerForStateDescriptor:(%{public}@) toneIdentifier:(%{public}@)."
+ "%{public}@: -_startAttentionAwarenessDuckingTimer…: Started %.0f-second ducking timer for tone: %{public}@."
+ "%{public}@: -_startPlayback… hasAlreadyDetected…: Pre-applying attention-aware effect mix (1.0) because user attention was already detected."
+ "%{public}@: -_startPlayback… hasAlreadyDetected…: [hapticPlayerItemTrack setEnabled:YES] and [hapticPlayerItemTrack setMutesHaptics:YES] on %{public}@."
+ "%{public}@: -init. Configured high shelf filter: frequency = %0.0f Hz, bandwidth = %0.2f, gain = %0.1f dB."
+ "%{public}@: -init. Disabled EQ band #%lu (bypassed)."
+ "%{public}@: -setEffectMix:. Current effect mix: %0.2f."
+ "; attenuatedCutoffFrequency = %f"
+ "; attenuatedReverbMix = %f"
+ "; attenuationRampInStartTime = %f"
+ "; attenuationRampInStopTime = %f"
+ "; attenuationRampOutStartTime = %f"
+ "; attenuationRampOutStopTime = %f"
+ "; didReachAttenuationTimeout = %@"
+ "; targetAttenuatedCutoffFrequency = %f"
+ "; targetAttenuatedReverbMix = %f"
+ "; targetAttenuationRampInDuration = %f"
+ "; targetAttenuationRampOutDuration = %f"
+ "; targetAttenuationTimeoutDuration = %f"
+ "; targetUnattenuatedCutoffFrequency = %f"
+ "; targetUnattenuatedReverbMix = %f"
+ "; unattenuatedCutoffFrequency = %f"
+ "; unattenuatedReverbMix = %f"
+ "@28@0:8@16f24"
+ "@44@0:8@16I24@28f36f40"
+ "TB,N,V_didReachAttenuationTimeout"
+ "Td,N,V_attenuationRampInStartTime"
+ "Td,N,V_attenuationRampInStopTime"
+ "Td,N,V_attenuationRampOutStartTime"
+ "Td,N,V_attenuationRampOutStopTime"
+ "Td,N,V_targetAttenuationRampInDuration"
+ "Td,N,V_targetAttenuationRampOutDuration"
+ "Td,N,V_targetAttenuationTimeoutDuration"
+ "Tf,N"
+ "Tf,N,V_attenuatedCutoffFrequency"
+ "Tf,N,V_attenuatedGlobalGainReduction"
+ "Tf,N,V_attenuatedReverbMix"
+ "Tf,N,V_initialVolume"
+ "Tf,N,V_targetAttenuatedCutoffFrequency"
+ "Tf,N,V_targetAttenuatedGlobalGainReduction"
+ "Tf,N,V_targetAttenuatedReverbMix"
+ "Tf,N,V_targetUnattenuatedCutoffFrequency"
+ "Tf,N,V_targetUnattenuatedGlobalGainReduction"
+ "Tf,N,V_targetUnattenuatedReverbMix"
+ "Tf,N,V_unattenuatedCutoffFrequency"
+ "Tf,N,V_unattenuatedGlobalGainReduction"
+ "Tf,N,V_unattenuatedReverbMix"
+ "Tf,R,N"
+ "_attentionAwarenessDuckingTimerSource"
+ "_attenuatedCutoffFrequency"
+ "_attenuatedGlobalGainReduction"
+ "_attenuatedReverbMix"
+ "_attenuationRampInStartTime"
+ "_attenuationRampInStopTime"
+ "_attenuationRampOutStartTime"
+ "_attenuationRampOutStopTime"
+ "_cancelAttentionAwarenessDuckingTimerForStateDescriptor:"
+ "_didReachAttenuationTimeout"
+ "_effectMix"
+ "_enableAttenuatedHapticTrack:"
+ "_handleAttentionAwarenessDuckingTimeoutForStateDescriptor:"
+ "_initialVolume"
+ "_performAttentionAwarenessDuckingTimeoutActionForStateDescriptor:"
+ "_startAttentionAwarenessDuckingTimerForStateDescriptor:"
+ "_targetAttenuatedCutoffFrequency"
+ "_targetAttenuatedGlobalGainReduction"
+ "_targetAttenuatedReverbMix"
+ "_targetAttenuationRampInDuration"
+ "_targetAttenuationRampOutDuration"
+ "_targetAttenuationTimeoutDuration"
+ "_targetUnattenuatedCutoffFrequency"
+ "_targetUnattenuatedGlobalGainReduction"
+ "_targetUnattenuatedReverbMix"
+ "_unattenuatedCutoffFrequency"
+ "_unattenuatedGlobalGainReduction"
+ "_unattenuatedReverbMix"
+ "attenuated"
+ "attenuatedCutoffFrequency"
+ "attenuatedGlobalGainReduction"
+ "attenuatedReverbMix"
+ "attenuationRampInStart"
+ "attenuationRampInStartTime"
+ "attenuationRampInStop"
+ "attenuationRampInStopTime"
+ "attenuationRampOutStart"
+ "attenuationRampOutStartTime"
+ "attenuationRampOutStop"
+ "attenuationRampOutStopTime"
+ "attenuationTimeoutWasReached"
+ "bandwidth"
+ "currentCutoffFrequency"
+ "currentLowPassFilterGlobalGain"
+ "currentReverbWetDryMix"
+ "didReachAttenuationTimeout"
+ "effectMix"
+ "f24@0:8f16f20"
+ "initWithAudioSession:initialVolume:"
+ "initWithProcessingFormat:framesPerRender:audioSession:initialEffectMix:initialVolume:"
+ "initialVolume"
+ "setAttenuatedCutoffFrequency:"
+ "setAttenuatedGlobalGainReduction:"
+ "setAttenuatedReverbMix:"
+ "setAttenuationRampInStartTime:"
+ "setAttenuationRampInStopTime:"
+ "setAttenuationRampOutStartTime:"
+ "setAttenuationRampOutStopTime:"
+ "setBandwidth:"
+ "setDidReachAttenuationTimeout:"
+ "setEffectMix:"
+ "setEffectMix:effectMixFadeDuration:completion:"
+ "setFilterType:"
+ "setFrequency:"
+ "setGain:"
+ "setInitialVolume:"
+ "setTargetAttenuatedCutoffFrequency:"
+ "setTargetAttenuatedGlobalGainReduction:"
+ "setTargetAttenuatedReverbMix:"
+ "setTargetAttenuationRampInDuration:"
+ "setTargetAttenuationRampOutDuration:"
+ "setTargetAttenuationTimeoutDuration:"
+ "setTargetUnattenuatedCutoffFrequency:"
+ "setTargetUnattenuatedGlobalGainReduction:"
+ "setTargetUnattenuatedReverbMix:"
+ "setUnattenuatedCutoffFrequency:"
+ "setUnattenuatedGlobalGainReduction:"
+ "setUnattenuatedReverbMix:"
+ "setWetDryMix:"
+ "targetAttenuatedCutoffFrequency"
+ "targetAttenuatedGlobalGainReduction"
+ "targetAttenuatedReverbMix"
+ "targetAttenuationRampInDuration"
+ "targetAttenuationRampOutDuration"
+ "targetAttenuationTimeoutDuration"
+ "targetCutoffFrequencyForEffectMix:"
+ "targetGlobalGainReductionForEffectMix:initialVolume:"
+ "targetReverbWetDryMixForEffectMix:"
+ "targetUnattenuatedCutoffFrequency"
+ "targetUnattenuatedGlobalGainReduction"
+ "targetUnattenuatedReverbMix"
+ "unattenuatedCutoffFrequency"
+ "unattenuatedGlobalGainReduction"
+ "unattenuatedReverbMix"
+ "v36@0:8f16d20@?28"
+ "\x92"
- "%{public}@: -_applyEffectParameters:. Low pass filter global gain is already set to %0.2f."
- "%{public}@: -_applyEffectParameters:. Set low pass filter global gain to %0.2f for audio session category %{public}@."
- "%{public}@: -_applyEffectParameters:. Volume for low pass filter global gain: %0.2f."
- "%{public}@: -_didReceiveAttentionPollingEventOfType:(%{public}@) […]: [attenuatedHapticPlayerItemTrack setMutesHaptics:NO] on %{public}@."
- "%{public}@: -_didReceiveAttentionPollingEventOfType:(%{public}@) […]: [hapticPlayerItemTrack setActiveHapticChannelIndex:%ld] on %{public}@."
- "%{public}@: -_didReceiveAttentionPollingEventOfType:(%{public}@) […]: [hapticPlayerItemTrack setMutesHaptics:YES] on %{public}@."
- "%{public}@: -_startPlayback… hasAlreadyDetected…: [hapticPlayerItemTrack setEnabled:NO] and [hapticPlayerItemTrack setMutesHaptics:YES] on %{public}@."
- "%{public}@: -init. Equalizer band #%lu: filterType = %ld, gain = %f, frequency = %f, bypass = %{BOOL}d."
- "%{public}@: -init. Equalizer bypass: %{BOOL}d. Number of bands: %lu."
- "%{public}@: -init. Error loading equalizer preset: %{public}@."
- "%{public}@: -setEffectParameters:. Current low pass filter global gain: %0.2f."
- "@36@0:8{?=Bff}16@28"
- "@48@0:8@16I24@28{?=Bff}36"
- "PearlID_Equalizer"
- "T{?=Bff},N"
- "_applyEffectParameters:includingEffectMix:"
- "_effectParameters"
- "bypass"
- "connect:to:fromBus:toBus:format:"
- "connect:toConnectionPoints:fromBus:format:"
- "destinationForMixer:bus:"
- "effectParameters"
- "enumerateObjectsUsingBlock:"
- "filterType"
- "initWithEffectParameters:audioSession:"
- "initWithNode:bus:"
- "initWithProcessingFormat:framesPerRender:audioSession:effectParameters:"
- "setEffectParameters:"
- "setEffectParameters:effectMixFadeDuration:"
- "v28@0:8{?=Bff}16"
- "v32@0:8{?=Bff}16B28"
- "v32@?0@\"AVAudioUnitEQFilterParameters\"8Q16^B24"
- "v36@0:8{?=Bff}16d28"
- "{?=\"shouldBypassLowPassFilter\"B\"volumeForLowPassFilterGlobalGain\"f\"effectMix\"f}"
- "{?=Bff}16@0:8"

```
