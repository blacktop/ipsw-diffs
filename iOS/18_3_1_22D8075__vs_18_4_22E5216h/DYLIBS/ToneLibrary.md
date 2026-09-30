## ToneLibrary

> `/System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary`

```diff

-633.0.0.0.0
-  __TEXT.__text: 0x47cd4
+638.0.0.0.0
+  __TEXT.__text: 0x49074
   __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_methlist: 0x2868
-  __TEXT.__const: 0x178
-  __TEXT.__gcc_except_tab: 0x168c
-  __TEXT.__cstring: 0x5944
-  __TEXT.__oslogstring: 0xcfd9
+  __TEXT.__objc_methlist: 0x2d40
+  __TEXT.__const: 0x158
+  __TEXT.__gcc_except_tab: 0x1698
+  __TEXT.__cstring: 0x5be6
+  __TEXT.__oslogstring: 0xd18a
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x534
-  __TEXT.__unwind_info: 0x11b8
-  __TEXT.__objc_classname: 0x53a
-  __TEXT.__objc_methname: 0xa18b
-  __TEXT.__objc_methtype: 0x109b
-  __TEXT.__objc_stubs: 0x69a0
-  __DATA_CONST.__got: 0x420
-  __DATA_CONST.__const: 0x18a0
-  __DATA_CONST.__objc_classlist: 0x140
+  __TEXT.__unwind_info: 0x1240
+  __TEXT.__objc_classname: 0x595
+  __TEXT.__objc_methname: 0xa8a4
+  __TEXT.__objc_methtype: 0x10fc
+  __TEXT.__objc_stubs: 0x6ea0
+  __DATA_CONST.__got: 0x458
+  __DATA_CONST.__const: 0x18e0
+  __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e78
+  __DATA_CONST.__objc_selrefs: 0x2058
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__auth_got: 0x4a8
-  __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x5660
-  __AUTH_CONST.__objc_const: 0x4c98
+  __AUTH_CONST.__const: 0x380
+  __AUTH_CONST.__cfstring: 0x5a00
+  __AUTH_CONST.__objc_const: 0x4d40
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x3e4
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x430
   __DATA.__data: 0x3e0
   __DATA.__common: 0x4
-  __DATA.__bss: 0x228
+  __DATA.__bss: 0x238
   __DATA_DIRTY.__objc_data: 0xbe0
   __DATA_DIRTY.__bss: 0x1d0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/AudioAnalytics.framework/AudioAnalytics
+  - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libAudioStatistics.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1327
-  Symbols:   1869
-  CStrings:  2950
+  Functions: 1388
+  Symbols:   1945
+  CStrings:  3066
 
Symbols:
+ _IOPSDrawingUnlimitedPower
+ _OBJC_CLASS_$_AudioAnalyticsReporter
+ _OBJC_CLASS_$_FBSDisplayLayoutMonitor
+ _OBJC_CLASS_$_FBSDisplayLayoutMonitorConfiguration
+ _OBJC_CLASS_$_TLAlertPlaybackBeginEvent
+ _OBJC_CLASS_$_TLAlertQueuePlayerAnalytics
+ _OBJC_CLASS_$_TLAlertQueuePlayerAnalyticsRecorder
+ _OBJC_METACLASS_$_TLAlertPlaybackBeginEvent
+ _OBJC_METACLASS_$_TLAlertQueuePlayerAnalytics
+ _OBJC_METACLASS_$_TLAlertQueuePlayerAnalyticsRecorder
+ _SBSDisplayLayoutElementStandByIdentifier
+ _TLToneAnalyticsKindAlarmWakeUp
+ _TLToneAnalyticsKindOther
+ _TLToneAnalyticsKindSystemRingtone
- _objc_retain_x11
CStrings:
+ "\x11\x14"
+ "%{public}@: -_startPlayback… hasAlreadyDetected…: Calling -alert:didBeginPlayingWithEvent: on playback observer %{public}@ with %{public}@ for %{public}@."
+ "%{public}@: -_startPlayback… hasAlreadyDetected…: Calling -alertDidBeginPlaying: on playback observer %{public}@ for %{public}@."
+ "%{public}@: Did send analytics message: %{public}@"
+ "%{public}@: Recording analytics: %{public}@"
+ "%{public}@: isDisplayInStandByMode = %{BOOL}u"
+ "; alertType = %@"
+ "; attenuationTime = %f"
+ "; audioSessionReporterID = %lld"
+ "; didAttenuatePlayback = %@"
+ "; isAttentionAwarenessSupportEnabled = %@"
+ "; reporterID = %lld"
+ "; startTime = %f"
+ "; stopTime = %f"
+ "; toneIdentifierForAnalytics = \"%@\""
+ "; toneKindForAnalytics = \"%@\""
+ "; userVolume = %f"
+ "; wasDeviceChargingOnStart = %@"
+ "; wasDeviceChargingOnStop = %@"
+ "@\"FBSDisplayLayoutMonitor\""
+ "@\"TLAlertQueuePlayerAnalytics\""
+ "@\"TLAlertQueuePlayerAnalyticsRecorder\""
+ "NO"
+ "T@\"NSString\",R,N,V_toneIdentifierForAnalytics"
+ "T@\"NSString\",R,N,V_toneKindForAnalytics"
+ "T@\"TLAlertQueuePlayerAnalytics\",&,N,V_analytics"
+ "T@\"TLAlertQueuePlayerAnalyticsRecorder\",R"
+ "TB,N,GisAttentionAwarenessSupportEnabled,V_attentionAwarenessSupportEnabled"
+ "TB,N,V_didAttenuatePlayback"
+ "TB,N,V_wasDeviceChargingOnStart"
+ "TB,N,V_wasDeviceChargingOnStop"
+ "TLAlertPlaybackBeginEvent"
+ "TLAlertQueuePlayerAnalytics"
+ "TLAlertQueuePlayerAnalyticsRecorder"
+ "Td,N,V_attenuationTime"
+ "Td,N,V_startTime"
+ "Td,N,V_stopTime"
+ "Tf,N,V_userVolume"
+ "Tq,N,V_reporterID"
+ "Tq,R,N,V_alertType"
+ "Tq,R,N,V_audioSessionReporterID"
+ "YES"
+ "_alertType"
+ "_analytics"
+ "_analyticsRecorder"
+ "_attentionAwarenessSupportEnabled"
+ "_attenuationTime"
+ "_audioSessionReporterID"
+ "_beginMonitoringDisplayLayout"
+ "_didAttenuatePlayback"
+ "_hasInitializedDisplayInStandByModeFlag"
+ "_initWithAudioSessionReporterID:"
+ "_initializeAnalyticsFromPreviousStateDescriptor:"
+ "_initializeToneIdentifierAndToneKindFromAlert:"
+ "_isDisplayInStandByMode"
+ "_layoutMonitor"
+ "_reporterID"
+ "_startTime"
+ "_stopTime"
+ "_toneIdentifierForAnalytics"
+ "_toneKindForAnalytics"
+ "_updateWithDisplayLayout:"
+ "_userVolume"
+ "_wasDeviceChargingOnStart"
+ "_wasDeviceChargingOnStop"
+ "alarmWakeUp"
+ "alert:didBeginPlayingWithEvent:"
+ "analytics"
+ "attentionAwarenessSupportEnabled"
+ "attenuationTime"
+ "audioSessionReporterID"
+ "configurationForDefaultMainDisplayMonitor"
+ "date"
+ "default"
+ "deviceChargingOnToneStart"
+ "deviceChargingOnToneStop"
+ "deviceHasAttentionAwarenessEnabled"
+ "deviceHasFaceID"
+ "didAttenuatePlayback"
+ "elements"
+ "hasFaceIDCapability"
+ "initWithReporterID:"
+ "isAttentionAwarenessSupportEnabled"
+ "isDeviceCurrentlyCharging"
+ "isDisplayInStandByMode"
+ "monitorWithConfiguration:"
+ "otherTone"
+ "recordAnalytics:"
+ "setAnalytics:"
+ "setAttentionAwarenessSupportEnabled:"
+ "setAttenuationTime:"
+ "setDidAttenuatePlayback:"
+ "setNeedsUserInteractivePriority:"
+ "setReporterID:"
+ "setStartTime:"
+ "setStopTime:"
+ "setTransitionHandler:"
+ "setUserVolume:"
+ "setWasDeviceChargingOnStart:"
+ "setWasDeviceChargingOnStop:"
+ "sharedRecorder"
+ "startTime"
+ "stopTime"
+ "system"
+ "timeIntervalSinceReferenceDate"
+ "timeToAttenuate"
+ "timeToStopAlert"
+ "toneIdentifierForAnalytics"
+ "toneKind"
+ "toneKindForAnalytics"
+ "toneWasAttenuated"
+ "userVolume"
+ "v32@?0@\"FBSDisplayLayoutMonitor\"8@\"FBSDisplayLayout\"16@\"FBSDisplayLayoutTransitionContext\"24"
+ "wasDeviceChargingOnStart"
+ "wasDeviceChargingOnStop"
- "\x13"

```
