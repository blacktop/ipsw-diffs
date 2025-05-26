## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

-3301.20.3.0.0
-  __TEXT.__text: 0x1b8a80
-  __TEXT.__auth_stubs: 0x1ac0
-  __TEXT.__objc_stubs: 0x22900
-  __TEXT.__objc_methlist: 0x1ae38
-  __TEXT.__const: 0x250
-  __TEXT.__gcc_except_tab: 0x2f78
-  __TEXT.__cstring: 0x31aaf
-  __TEXT.__objc_methname: 0x44b90
-  __TEXT.__oslogstring: 0x2749f
-  __TEXT.__objc_classname: 0x3f0a
-  __TEXT.__objc_methtype: 0x8eb0
+3302.21.3.1.1
+  __TEXT.__text: 0x1b8e20
+  __TEXT.__auth_stubs: 0x1ad0
+  __TEXT.__objc_stubs: 0x229c0
+  __TEXT.__objc_methlist: 0x1adb0
+  __TEXT.__const: 0x2a0
+  __TEXT.__gcc_except_tab: 0x2ff8
+  __TEXT.__cstring: 0x31a1d
+  __TEXT.__objc_methname: 0x44bc8
+  __TEXT.__oslogstring: 0x27552
+  __TEXT.__objc_classname: 0x3f0c
+  __TEXT.__objc_methtype: 0x8ed5
   __TEXT.__dlopen_cstrs: 0x3c9
-  __TEXT.__unwind_info: 0x680c
+  __TEXT.__unwind_info: 0x67fc
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0xd78
-  __DATA_CONST.__got: 0x750
+  __DATA_CONST.__auth_got: 0xd80
+  __DATA_CONST.__got: 0x778
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x6a98
-  __DATA_CONST.__cfstring: 0xac60
+  __DATA_CONST.__const: 0x6bb0
+  __DATA_CONST.__cfstring: 0xabe0
   __DATA_CONST.__objc_classlist: 0xbf0
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x548

   __DATA_CONST.__objc_arrayobj: 0x198
   __DATA_CONST.__objc_dictobj: 0x398
   __DATA_CONST.__objc_floatobj: 0x4f0
-  __DATA.__objc_const: 0x58e88
-  __DATA.__objc_selrefs: 0xc9b8
+  __DATA.__objc_const: 0x58db8
+  __DATA.__objc_selrefs: 0xc9a8
   __DATA.__objc_protorefs: 0xf8
-  __DATA.__objc_classrefs: 0x1380
+  __DATA.__objc_classrefs: 0x1398
   __DATA.__objc_superrefs: 0x9c8
-  __DATA.__objc_ivar: 0x2344
+  __DATA.__objc_ivar: 0x232c
   __DATA.__objc_data: 0x7760
   __DATA.__data: 0x3f60
   __DATA.__bss: 0xa18

   - /System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC
   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics
+  - /System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration
   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation
   - /System/Library/PrivateFrameworks/SiriLiminal.framework/SiriLiminal
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 11311
-  Symbols:   951
-  CStrings:  17986
+  Functions: 11292
+  Symbols:   960
+  CStrings:  17977
 
Symbols:
+ _AVSystemController_RouteDescriptionKey_BTDetails_IsA2DPRoute
+ _AVSystemController_RouteDescriptionKey_BTDetails_IsHFPRoute
+ _AVSystemController_RouteDescriptionKey_RouteCurrentlyPicked
+ _AVSystemController_RouteDescriptionKey_RouteUID
+ _BTDeviceAddressFromString
+ _OBJC_CLASS_$_SCDAContext
+ _OBJC_CLASS_$_SCDAGoodnessScoreOverrideState
+ _OBJC_CLASS_$_SCDAPerceptualAudioHash
+ _kCSDiagnosticReporterVoiceTriggerLaunchDelayTooHigh
CStrings:
+ "\x1f\n\x12"
+ "%s Bypass audio here because ::                   1> VoiceTrigger enabled = %{public}d;                   2> phrase spotter bypassed = %{public}d;                   3> should ignore due to hearst routed and not in splitter = %{public}d;                   4> has HFP during call = %{public}d;                   5> AVVC recording client # = %{public}lu                   heartbeat = %{public}lld"
+ "%s Current Picked route supportDoAP: %d"
+ "%s Fetched CSBluetoothDeviceInfo: %{private}@ for BTDevice with address: %{private}@, supportDoAP: %d"
+ "%s Has hearst routed and not in splitter ignore AOP trigger notification"
+ "%s Hearst Route Status=%ld, splitterState = %{public}lu"
+ "%s Hearst status: %{public}ld"
+ "%s Notifying Hearst Route State: %{public}ld"
+ "%s Received Hearst event: %{public}ld"
+ "%s Rejecting RC: ASR is running on-device (full UoD)"
+ "%s Report unexpectedly long launch latency %{publlic}.3f AudioTimeConverter: %@"
+ "%s Resetting _isInitialTurnAnnounceFollowup"
+ "%s Updating attending options for Announce to: %@"
+ "%s Using cached CSBluetoothDeviceInfo: %{private}@ for BTDevice with Address: %{private}@"
+ "%s sampleRate=%{public}lu, recordContext=%{public}@, disableRCSelection=%d"
+ "-[CSAttendingSpeechDetectionController _updateAttendingOptionsForAnnounce:]"
+ "-[CSAudioRouteChangeMonitor getHearstRouteStatus:]"
+ "-[CSAudioRouteChangeMonitor hearstRouteStatus]"
+ "-[CSAudioRouteChangeMonitorImpl _fetchHearstRouteStatusWithCompletion:]_block_invoke"
+ "-[CSAudioRouteChangeMonitorImpl _notifyHearstRouteStatus:]"
+ "-[CSAudioRouteChangeMonitorImplWatch _fetchHearstRouteStatusWithCompletion:]_block_invoke"
+ "-[CSAudioRouteChangeMonitorImplWatch _notifyHearstRouteStatus:]"
+ "-[CSBluetoothManager _getBluetoothDeviceInfoForDeviceWithBTAddressString:]"
+ "-[CSCarKitUtils _invalidateCachedCarPlayCapabilities]"
+ "-[CSCarKitUtils _updateCarPlayCapabilitiesDict]"
+ "-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]"
+ "-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke"
+ "-[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]"
+ "-[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke"
+ "-[CSNNVADEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke"
+ "-[CSSiriLauncher notifyCarPlayVoiceTrigger:deviceId:myriadPHash:completion:]_block_invoke_3"
+ "-[CSSiriLauncher notifyDarwinVoiceTrigger:deviceId:myriadPHash:myriadLateActivationExpirationTime:completion:]_block_invoke_3"
+ "-[CSVoiceTriggerSecondPass _reportDiagnosticsForDelayedVTLaunchIfNeeded:]"
+ "B40@0:8@16@24@32"
+ "F\x12A\x14\x14\x14#!\x11"
+ "TB,N,V_disableRCSelection"
+ "TB,R,N,V_isInitialTurnAnnounceFollowup"
+ "Tq,N,V_hearstRouteStatus"
+ "_carCapabilitiesLock"
+ "_delayBecauseCarKitSendsNotificationBeforeCapabilitiesActuallyReady"
+ "_disableRCSelection"
+ "_fetchCarCapabilitiesInBackgroundWithCompletion:"
+ "_fetchHearstRouteStatusWithCompletion:"
+ "_getBluetoothDeviceInfoForDeviceWithBTAddressString:"
+ "_hasHFPDuringPhoneCall"
+ "_hasHearstRoutedAndNotInSplitter"
+ "_hearstRouteStatus"
+ "_invalidateCachedCarPlayCapabilities"
+ "_isInitialTurnAnnounceFollowup"
+ "_notifyHearstRouteStatus:"
+ "_reportDiagnosticsForDelayedVTLaunchIfNeeded:"
+ "_stopReasonFromHint:"
+ "_updateAttendingOptionsForAnnounce:"
+ "_updateCarPlayCapabilitiesDict"
+ "copyWithRecordType:"
+ "disableRCSelection"
+ "getBTDeviceInfoWithBTAddressString:withCompletion:"
+ "getHearstRouteStatus:"
+ "hearstRouteStatus"
+ "isCurrentlyInActiveCall"
+ "isCurrentlyInSplitterState"
+ "isInitialTurnAnnounceFollowup"
+ "isMagusSupportedWithInputOrigin:recordRoute:playbackRoute:"
+ "isTriggerlessAnnounce"
+ "resetForNewRequestWithSampleRate:recordContext:disableRCSelection:"
+ "routeIsDoAPSupportedWithRouteUID:withCompletion:"
+ "setDisableRCSelection:"
+ "setHearstRouteStatus:"
+ "supportsSCDAFramework"
+ "v16@?0@\"<SCDAContextMutating>\"8"
+ "v16@?0@\"CSBluetoothDeviceInfo\"8"
+ "v36@0:8Q16@\"CSAudioRecordContext\"24B32"
+ "v36@0:8Q16@24B32"
- "\x1f\f"
- "%s Bypass audio here because ::                   1> VoiceTrigger enabled = %{public}d;                   2> phrase spotter bypassed = %{public}d;                   3> should ignore due to accessory connected and not in splitter = %{public}d;                   4> has hearst routable during call = %{public}d;                   5> AVVC recording client # = %{public}lu                   heartbeat = %{public}lld"
- "%s Has out of band siri input source and not in splitter ignore AOP trigger notification"
- "%s Hearst Routed=%d, Hearst Owned=%d (mac-only), splitterState = %{public}lu"
- "%s Hearst connected ? %{public}@"
- "%s Notifying Hearst Connection State : %{public}d"
- "%s Notifying Hearst Routed State : %{public}d"
- "%s Notifying Siri Input Source Out Of Band State : %{public}d"
- "%s Picked Output Audio Route : %{public}@"
- "%s Picked output audio route is nil"
- "%s Received Hearst %{public}@ event"
- "%s Received Hearst Ownership event, new ownershipStatus: %lu"
- "%s Received Siri Input Source %{public}@ event"
- "-[CSAudioRouteChangeMonitor getHearstConnected:]"
- "-[CSAudioRouteChangeMonitor getHearstRouted:]"
- "-[CSAudioRouteChangeMonitor getSiriInputSourceOutOfBand:]"
- "-[CSAudioRouteChangeMonitor hearstConnected]"
- "-[CSAudioRouteChangeMonitor hearstRouted]"
- "-[CSAudioRouteChangeMonitor siriInputSourceOutOfBand]"
- "-[CSAudioRouteChangeMonitorImpl _notifyHearstConnectionState:]"
- "-[CSAudioRouteChangeMonitorImpl _notifyHearstRoutedState:]"
- "-[CSAudioRouteChangeMonitorImpl _notifySiriInputSourceOutOfBandState:]"
- "-[CSAudioRouteChangeMonitorImplWatch _fetchHearstRoutedState]"
- "-[CSAudioRouteChangeMonitorImplWatch _notifyHearstRoutedState:]"
- "-[CSAudioRouteChangeMonitorImplWatch _notifySiriInputSourceOutOfBandState:]"
- "-[CSBuiltInVoiceTrigger _receivedHearstConnectedEvent:]"
- "-[CSBuiltInVoiceTrigger _receivedHearstOwnershipEvent:]"
- "-[CSBuiltInVoiceTrigger _receivedSiriInputSourceOutOfBandEvent:]"
- "-[CSCarKitUtils _getAndPotentiallyCacheCarPlayCapabilitiesDict]"
- "-[CSCarKitUtils invalidateCachedCarPlayCapabilities]"
- "-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:]"
- "-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:]_block_invoke"
- "-[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:]"
- "-[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:]_block_invoke"
- "-[CSNNVADEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:]_block_invoke"
- "-[CSSiriLauncher notifyCarPlayVoiceTrigger:deviceId:myriadPHash:completion:]_block_invoke_2"
- "-[CSSiriLauncher notifyDarwinVoiceTrigger:deviceId:myriadPHash:myriadLateActivationExpirationTime:completion:]_block_invoke_2"
- "Not Routed"
- "Routed"
- "TB,N,V_isHearstConnected"
- "TB,N,V_isHearstRouted"
- "TB,N,V_isSiriInputSourceOutOfBand"
- "Tq,N,V_hearstOwnershipStatus"
- "V\x12A\x18\x143!\x11"
- "_fetchHearstRoutedState"
- "_fetchSiriInputSourceOutOfBandState"
- "_getAndPotentiallyCacheCarPlayCapabilitiesDict"
- "_hasHearstRoutableDuringPhoneCall"
- "_hasSiriInputOutOfBandAndNotInSplitter"
- "_hearstOwnershipStatus"
- "_isHearstConnected"
- "_isHearstOwned"
- "_isHearstRouted"
- "_isSiriInputSourceOutOfBand"
- "_notifyHearstConnectionState:"
- "_notifyHearstRoutedState:"
- "_notifySiriInputSourceOutOfBandState:"
- "_recacheCarCapabilitiesLock"
- "_receivedHearstConnectedEvent:"
- "_receivedHearstOwnershipEvent:"
- "_receivedSiriInputSourceOutOfBandEvent:"
- "fetchCarCapabilitiesInBackgroundWithCompletion:"
- "getHearstConnected:"
- "getHearstRouted:"
- "getSiriInputSourceOutOfBand:"
- "hearstConnected"
- "hearstOwnershipStatus"
- "hearstRouted"
- "invalidateCachedCarPlayCapabilities"
- "isHearstConnected"
- "isHearstRouted"
- "isNotOutOfBand"
- "isOutOfBand"
- "isSiriInputSourceOutOfBand"
- "resetForNewRequestWithSampleRate:recordContext:"
- "setHearstOwnershipStatus:"
- "setIsHearstConnected:"
- "setIsHearstRouted:"
- "setIsSiriInputSourceOutOfBand:"
- "siriInputSource"
- "siriInputSourceOutOfBand"
- "v32@0:8Q16@\"CSAudioRecordContext\"24"

```
