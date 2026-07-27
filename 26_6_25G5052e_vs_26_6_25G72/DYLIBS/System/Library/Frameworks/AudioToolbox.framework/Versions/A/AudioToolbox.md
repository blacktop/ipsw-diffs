## AudioToolbox

> `/System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__auth_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1556.702.0.0.0
-  __TEXT.__text: 0x183208
+1556.704.0.0.0
+  __TEXT.__text: 0x1832bc
   __TEXT.__auth_stubs: 0x3150
   __TEXT.__objc_methlist: 0x15c4
   __TEXT.__const: 0xeee
   __TEXT.__dlopen_cstrs: 0x334
   __TEXT.__gcc_except_tab: 0x16cf0
-  __TEXT.__cstring: 0xaf12
+  __TEXT.__cstring: 0xb60b
   __TEXT.__oslogstring: 0x18057
   __TEXT.__unwind_info: 0x7d40
   __TEXT.__objc_classname: 0x325

   - /usr/lib/swift/libswiftos.dylib
   Functions: 5779
   Symbols:   10135
-  CStrings:  4383
+  CStrings:  4466
 
Functions:
~ __ZN20AudioQueueXPC_Server13EnqueueBufferEjNSt3__14spanIK26AQBufferCreateDestroyEventLm18446744073709551615EEEjjjNS1_IK28AudioStreamPacketDescriptionLm18446744073709551615EEEjjNS1_IK24AudioQueueParameterEventLm18446744073709551615EEE19XAudioTimeStampBaseb : 5640 -> 5800
~ __ZN20AudioQueueXPC_Server13OfflineRenderEj19XAudioTimeStampBaseNSt3__14spanIK26AQBufferCreateDestroyEventLm18446744073709551615EEEjj : 1904 -> 1924
CStrings:
+ "AQInternalGetOfflineBufferCompletions"
+ "AQInternalPreflightOfflineRender"
+ "AQInternalScheduledStart"
+ "AQServer_CheckStopFromPause"
+ "AddPropertyListener"
+ "AudioQueueDeassignFromSubmixTap"
+ "AudioQueueDeviceHasDisconnected"
+ "AudioQueueDeviceStoppedFromBelow"
+ "AudioQueueIOBindingChanged"
+ "AudioQueueInternalDeliverProcessingNodeEvents"
+ "AudioQueueInternalFormatChanged"
+ "AudioQueueInternalNotifyRunning"
+ "AudioQueueInternalPause"
+ "AudioQueueInternalReleasePlayResources"
+ "AudioQueueInternalStop_Sync"
+ "AudioQueueLatencyChanged"
+ "AudioQueueNotifyReadyToRestart"
+ "CreateTimeline"
+ "DebugPrint"
+ "DeviceGetCurrentTime"
+ "DeviceGetNearestStartTime"
+ "DeviceIsRunning"
+ "DeviceTranslateTime"
+ "DisposeQueue"
+ "DisposeTimeline"
+ "Flush"
+ "GetCurrentTime"
+ "GetMaxIOBufferFrameSize"
+ "GetNearestStartTime"
+ "GetParameter"
+ "GetPendingCallbackMessages"
+ "GetProperty"
+ "GetPropertySize"
+ "GetSampleRate"
+ "GetStreamFormat"
+ "GetTotalNumberChannels"
+ "HandleAQGetParameter"
+ "HandleAQGetProperty"
+ "HandleAQScheduledParameters"
+ "HandleAQSetParameter"
+ "HandleAQSetProperty"
+ "LatencySamples"
+ "MapSharedBuffers"
+ "MixerConnectQueue"
+ "MixerDispose"
+ "MixerGetProperty"
+ "MixerGetPropertySize"
+ "MixerNew"
+ "MixerRender"
+ "MixerReset"
+ "MixerSetProperty"
+ "NewQueue"
+ "ProcessingNodeDispose"
+ "ProcessingNodeInstantiate"
+ "ProcessingTapDispose"
+ "ProcessingTapInit"
+ "ProcessingTapNew"
+ "QueueGetCurrentTime"
+ "RemovePropertyListener"
+ "ScaleOrUnscaleSampleTime"
+ "SetAudioQueue"
+ "SetParameter"
+ "SetTopologyFlags"
+ "StartIO_Primitive"
+ "TranslateTime"
+ "_InternalDispose"
+ "bluetoothAlternateTransportMode"
+ "bluetoothUserHeadTrackingModeForBundleID"
+ "bluetoothUserSpatialModeForBundleID"
+ "calibrationData"
+ "customHRTFMode"
+ "dynamicLatency"
+ "enableHeadTrackingMode"
+ "getHeadTracker"
+ "getHeadTrackingSupport"
+ "hasDefaultOutputSpeakerPort"
+ "setClockDevice"
+ "setSpatialStreamInfo"
+ "setVolumeScalar"
+ "triggerSPENOnAlternateTransportChange"
+ "volumeScalar"
+ "volumeScalarMappedToHWCurve"
+ "~RemoteClient_block_invoke"
```
