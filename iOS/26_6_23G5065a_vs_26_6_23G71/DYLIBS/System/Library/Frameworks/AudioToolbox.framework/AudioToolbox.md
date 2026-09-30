## AudioToolbox

> `/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`

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
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

   __TEXT.__const: 0x1314
   __TEXT.__dlopen_cstrs: 0x71d
   __TEXT.__gcc_except_tab: 0x28a40
-  __TEXT.__cstring: 0x1faac
-  __TEXT.__oslogstring: 0x3b65b
+  __TEXT.__cstring: 0x2026b
+  __TEXT.__oslogstring: 0x3b675
   __TEXT.__unwind_info: 0xc988
   __TEXT.__objc_classname: 0x417
   __TEXT.__objc_methname: 0x5d13

   - /usr/lib/swift/libswiftos.dylib
   Functions: 9543
   Symbols:   16539
-  CStrings:  8963
+  CStrings:  9050
 
CStrings:
+ "%25s:%-5d EXCEPTION (%d) [error != noErr is false]: \"\""
+ "@@ Strips Jul 11 2026 16:52:56"
+ "AQInternalGetOfflineBufferCompletions"
+ "AQInternalPreflightOfflineRender"
+ "AQInternalScheduledStart"
+ "AQServer_CheckStopFromPause"
+ "AddPropertyListener"
+ "AssignToSubmixTap_block_invoke"
+ "AudioQueueCheckSpatializationAfterRouteChange"
+ "AudioQueueDeassignFromSubmixTap_block_invoke"
+ "AudioQueueInternalDeliverProcessingNodeEvents"
+ "AudioQueueInternalNotifyRunning"
+ "AudioQueueInternalPause"
+ "AudioQueueInternalReleasePlayResources"
+ "AudioQueueInternalStop_Sync_block_invoke"
+ "AudioQueueNotifyReadyToRestart"
+ "AudioQueueSiriListeningPropertyChanged_block_invoke"
+ "CreateTimeline"
+ "DebugPrint"
+ "DeviceGetCurrentTime"
+ "DeviceGetNearestStartTime"
+ "DeviceIsRunning"
+ "DeviceTranslateTime"
+ "DisposeQueue_block_invoke"
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
+ "MixerConnectQueue_block_invoke"
+ "MixerDispose"
+ "MixerGetProperty"
+ "MixerGetPropertySize"
+ "MixerNew"
+ "MixerRender"
+ "MixerReset"
+ "MixerSetProperty"
+ "NewQueue"
+ "Pause_block_invoke"
+ "Prime_block_invoke"
+ "ProcessingNodeDispose"
+ "ProcessingNodeInstantiate"
+ "ProcessingTapDispose"
+ "ProcessingTapInit"
+ "ProcessingTapNew"
+ "QueueGetCurrentTime"
+ "RemovePropertyListener"
+ "ScaleOrUnscaleSampleTime"
+ "SetAudioQueue_block_invoke"
+ "SetOfflineRenderFormat_block_invoke"
+ "SetParameter"
+ "SetRoutingBehavior"
+ "SetTopologyFlags"
+ "StartIO_Primitive"
+ "Start_block_invoke"
+ "Stop_block_invoke"
+ "TranslateTime"
+ "_InternalDispose_block_invoke"
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
- "%25s:%-5d EXCEPTION (%d): \"\""
- "@@ Strips Jul  7 2026 23:09:51"
```
