## ToneLibrary

> `/System/Library/PrivateFrameworks/ToneLibrary.framework/Versions/A/ToneLibrary`

```diff

-633.0.0.0.0
-  __TEXT.__text: 0x22158
-  __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0x18c4
-  __TEXT.__const: 0xbc
-  __TEXT.__gcc_except_tab: 0x79c
-  __TEXT.__cstring: 0x3632
-  __TEXT.__oslogstring: 0x4e0f
+639.0.0.0.0
+  __TEXT.__text: 0x22a28
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__objc_methlist: 0x1c30
+  __TEXT.__const: 0x94
+  __TEXT.__gcc_except_tab: 0x7a8
+  __TEXT.__cstring: 0x37a0
+  __TEXT.__oslogstring: 0x4f33
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x96
-  __TEXT.__unwind_info: 0x8e0
-  __TEXT.__objc_classname: 0x330
-  __TEXT.__objc_methname: 0x5872
+  __TEXT.__unwind_info: 0x930
+  __TEXT.__objc_classname: 0x366
+  __TEXT.__objc_methname: 0x5d3a
   __TEXT.__objc_methtype: 0x985
-  __TEXT.__objc_stubs: 0x3420
-  __DATA_CONST.__got: 0x238
-  __DATA_CONST.__const: 0x720
-  __DATA_CONST.__objc_classlist: 0xd8
+  __TEXT.__objc_stubs: 0x3480
+  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__const: 0x738
+  __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1028
+  __DATA_CONST.__objc_selrefs: 0x1170
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xa8
+  __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x288
+  __AUTH_CONST.__auth_got: 0x290
   __AUTH_CONST.__const: 0x950
-  __AUTH_CONST.__cfstring: 0x3ac0
-  __AUTH_CONST.__objc_const: 0x3370
+  __AUTH_CONST.__cfstring: 0x3d00
+  __AUTH_CONST.__objc_const: 0x33d0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x27c
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x2ac
   __DATA.__data: 0x2b8
   __DATA.__bss: 0x118
   __DATA.__common: 0x4

   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 853F892C-83DF-33DD-895D-D2DCE04BB947
-  Functions: 724
-  Symbols:   1933
-  CStrings:  2129
+  UUID: 15F024CD-2721-305B-9D1E-10D0A325F823
+  Functions: 769
+  Symbols:   2014
+  CStrings:  2219
 
Symbols:
+ +[TLAlertController sharedAlertController].cold.1
+ +[TLAlertQueuePlayerAnalytics isDeviceCurrentlyCharging]
+ +[TLAudioQueue sharedAudioQueue].cold.1
+ +[TLBacklight sharedBacklight].cold.1
+ +[TLCapabilitiesManager sharedCapabilitiesManager].cold.1
+ +[TLContentProtectionStateObserver sharedContentProtectionStateObserver].cold.1
+ +[TLSystemApplication defaultSystemApplication].cold.1
+ +[TLToneManager sharedToneManager].cold.1
+ -[TLAlertPlaybackBeginEvent _initWithAudioSessionReporterID:]
+ -[TLAlertPlaybackBeginEvent audioSessionReporterID]
+ -[TLAlertPlaybackBeginEvent description]
+ -[TLAlertPlaybackBeginEvent hash]
+ -[TLAlertPlaybackBeginEvent isEqual:]
+ -[TLAlertQueuePlayerAnalytics .cxx_destruct]
+ -[TLAlertQueuePlayerAnalytics _initializeToneIdentifierAndToneKindFromAlert:]
+ -[TLAlertQueuePlayerAnalytics alertType]
+ -[TLAlertQueuePlayerAnalytics attenuationTime]
+ -[TLAlertQueuePlayerAnalytics description]
+ -[TLAlertQueuePlayerAnalytics didAttenuatePlayback]
+ -[TLAlertQueuePlayerAnalytics initWithAlert:]
+ -[TLAlertQueuePlayerAnalytics isAttentionAwarenessSupportEnabled]
+ -[TLAlertQueuePlayerAnalytics setAttentionAwarenessSupportEnabled:]
+ -[TLAlertQueuePlayerAnalytics setAttenuationTime:]
+ -[TLAlertQueuePlayerAnalytics setDidAttenuatePlayback:]
+ -[TLAlertQueuePlayerAnalytics setStartTime:]
+ -[TLAlertQueuePlayerAnalytics setStopTime:]
+ -[TLAlertQueuePlayerAnalytics setUserVolume:]
+ -[TLAlertQueuePlayerAnalytics setWasDeviceChargingOnStart:]
+ -[TLAlertQueuePlayerAnalytics setWasDeviceChargingOnStop:]
+ -[TLAlertQueuePlayerAnalytics startTime]
+ -[TLAlertQueuePlayerAnalytics stopTime]
+ -[TLAlertQueuePlayerAnalytics toneIdentifierForAnalytics]
+ -[TLAlertQueuePlayerAnalytics toneKindForAnalytics]
+ -[TLAlertQueuePlayerAnalytics userVolume]
+ -[TLAlertQueuePlayerAnalytics wasDeviceChargingOnStart]
+ -[TLAlertQueuePlayerAnalytics wasDeviceChargingOnStop]
+ -[TLCapabilitiesManager hasFaceIDCapability]
+ -[TLToneManager _soundForToneIdentifier:].cold.1
+ GCC_except_table56
+ OBJC_IVAR_$_TLAlertPlaybackBeginEvent._audioSessionReporterID
+ OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._alertType
+ OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._attentionAwarenessSupportEnabled
+ OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._attenuationTime
+ OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._didAttenuatePlayback
+ OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._startTime
+ OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._stopTime
+ OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._toneIdentifierForAnalytics
+ OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._toneKindForAnalytics
+ OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._userVolume
+ OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._wasDeviceChargingOnStart
+ OBJC_IVAR_$_TLAlertQueuePlayerAnalytics._wasDeviceChargingOnStop
+ TLLocalizedString.cold.1
+ TLLogGeneral.cold.1
+ TLLogPlayback.cold.1
+ TLLogToneManagement.cold.1
+ TLLogVibrationManagement.cold.1
+ _IOPSDrawingUnlimitedPower
+ _OBJC_CLASS_$_TLAlertPlaybackBeginEvent
+ _OBJC_CLASS_$_TLAlertQueuePlayerAnalytics
+ _OBJC_METACLASS_$_TLAlertPlaybackBeginEvent
+ _OBJC_METACLASS_$_TLAlertQueuePlayerAnalytics
+ _TLAlertTypeValidateConsistencyOfEnumeration.cold.1
+ _TLToneAnalyticsKindAlarmWakeUp
+ _TLToneAnalyticsKindOther
+ _TLToneAnalyticsKindSystemRingtone
+ __125-[TLAlertQueuePlayerController _startPlaybackForStateDescriptor:usingConfirmedPlayableAsset:hasAlreadyDetectedUserAttention:]_block_invoke.49
+ __43-[TLToneManager toneWithIdentifierIsValid:]_block_invoke.cold.1
+ __60-[TLAlertSystemSoundController _processPlayTaskDescriptors:]_block_invoke.11
+ __60-[TLAlertSystemSoundController _processPlayTaskDescriptors:]_block_invoke.17
+ __61-[TLAlertSystemSoundController _didCompletePlaybackForAlert:]_block_invoke.28
+ __OBJC_$_CLASS_METHODS_TLAlertQueuePlayerAnalytics
+ __OBJC_$_CLASS_PROP_LIST_TLAlertQueuePlayerAnalytics
+ __OBJC_$_INSTANCE_METHODS_TLAlertPlaybackBeginEvent
+ __OBJC_$_INSTANCE_METHODS_TLAlertQueuePlayerAnalytics
+ __OBJC_$_INSTANCE_VARIABLES_TLAlertPlaybackBeginEvent
+ __OBJC_$_INSTANCE_VARIABLES_TLAlertQueuePlayerAnalytics
+ __OBJC_$_PROP_LIST_TLAlertPlaybackBeginEvent
+ __OBJC_$_PROP_LIST_TLAlertQueuePlayerAnalytics
+ __OBJC_CLASS_RO_$_TLAlertPlaybackBeginEvent
+ __OBJC_CLASS_RO_$_TLAlertQueuePlayerAnalytics
+ __OBJC_METACLASS_RO_$_TLAlertPlaybackBeginEvent
+ __OBJC_METACLASS_RO_$_TLAlertQueuePlayerAnalytics
+ _objc_msgSend$_initWithAudioSessionReporterID:
+ _objc_msgSend$_initializeToneIdentifierAndToneKindFromAlert:
+ _objc_msgSend$alert:didBeginPlayingWithEvent:
- GCC_except_table38
- GCC_except_table55
- __60-[TLAlertSystemSoundController _processPlayTaskDescriptors:]_block_invoke.13
- __60-[TLAlertSystemSoundController _processPlayTaskDescriptors:]_block_invoke.14
- __61-[TLAlertSystemSoundController _didCompletePlaybackForAlert:]_block_invoke.25
CStrings:
+ "%{public}@: -_startPlayback… hasAlreadyDetected…: Calling -alert:didBeginPlayingWithEvent: on playback observer %{public}@ with %{public}@ for %{public}@."
+ "%{public}@: -_startPlayback… hasAlreadyDetected…: Calling -alertDidBeginPlaying: on playback observer %{public}@ for %{public}@."
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ToneLibrary/Library/Playback/BackEnds/QueuePlayer/TLAlertQueuePlayerController.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ToneLibrary/Library/Playback/BackEnds/SystemSound/TLAlertSystemSoundController.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ToneLibrary/Library/Playback/TLAlertController.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ToneLibrary/Library/Playback/TLAlertType.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ToneLibrary/Library/Utilities/TLAudioQueue.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ToneLibrary/Library/Utilities/TLBacklight.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ToneLibrary/Library/Utilities/TLContentProtectionStateObserver.m"
+ "; alertType = %@"
+ "; attenuationTime = %f"
+ "; audioSessionReporterID = %lld"
+ "; didAttenuatePlayback = %@"
+ "; isAttentionAwarenessSupportEnabled = %@"
+ "; startTime = %f"
+ "; stopTime = %f"
+ "; toneIdentifierForAnalytics = \"%@\""
+ "; toneKindForAnalytics = \"%@\""
+ "; userVolume = %f"
+ "; wasDeviceChargingOnStart = %@"
+ "; wasDeviceChargingOnStop = %@"
+ "NO"
+ "T@\"NSString\",R,N,V_toneIdentifierForAnalytics"
+ "T@\"NSString\",R,N,V_toneKindForAnalytics"
+ "TB,N,GisAttentionAwarenessSupportEnabled,V_attentionAwarenessSupportEnabled"
+ "TB,N,V_didAttenuatePlayback"
+ "TB,N,V_wasDeviceChargingOnStart"
+ "TB,N,V_wasDeviceChargingOnStop"
+ "TLAlertPlaybackBeginEvent"
+ "TLAlertQueuePlayerAnalytics"
+ "Td,N,V_attenuationTime"
+ "Td,N,V_startTime"
+ "Td,N,V_stopTime"
+ "Tf,N,V_userVolume"
+ "Tq,R,N,V_alertType"
+ "Tq,R,N,V_audioSessionReporterID"
+ "YES"
+ "_alertType"
+ "_attentionAwarenessSupportEnabled"
+ "_attenuationTime"
+ "_audioSessionReporterID"
+ "_didAttenuatePlayback"
+ "_initWithAudioSessionReporterID:"
+ "_initializeToneIdentifierAndToneKindFromAlert:"
+ "_startTime"
+ "_stopTime"
+ "_toneIdentifierForAnalytics"
+ "_toneKindForAnalytics"
+ "_userVolume"
+ "_wasDeviceChargingOnStart"
+ "_wasDeviceChargingOnStop"
+ "alarmWakeUp"
+ "alert:didBeginPlayingWithEvent:"
+ "alertType"
+ "attentionAwarenessSupportEnabled"
+ "attenuationTime"
+ "audioSessionReporterID"
+ "default"
+ "didAttenuatePlayback"
+ "hasFaceIDCapability"
+ "isAttentionAwarenessSupportEnabled"
+ "isDeviceCurrentlyCharging"
+ "otherTone"
+ "setAttentionAwarenessSupportEnabled:"
+ "setAttenuationTime:"
+ "setDidAttenuatePlayback:"
+ "setStartTime:"
+ "setStopTime:"
+ "setUserVolume:"
+ "setWasDeviceChargingOnStart:"
+ "setWasDeviceChargingOnStop:"
+ "startTime"
+ "stopTime"
+ "system"
+ "toneIdentifierForAnalytics"
+ "toneKindForAnalytics"
+ "userVolume"
+ "wasDeviceChargingOnStart"
+ "wasDeviceChargingOnStop"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ToneLibrary/Library/Playback/BackEnds/QueuePlayer/TLAlertQueuePlayerController.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ToneLibrary/Library/Playback/BackEnds/SystemSound/TLAlertSystemSoundController.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ToneLibrary/Library/Playback/TLAlertController.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ToneLibrary/Library/Playback/TLAlertType.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ToneLibrary/Library/Utilities/TLAudioQueue.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ToneLibrary/Library/Utilities/TLBacklight.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ToneLibrary/Library/Utilities/TLContentProtectionStateObserver.m"

```
