## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/Versions/A/AirPlaySender`

```diff

-980.77.5.3.0
-  __TEXT.__text: 0x1cb36c
+1005.7.1.0.0
+  __TEXT.__text: 0x1ccffc
   __TEXT.__objc_methlist: 0x92c
   __TEXT.__const: 0xd580
   __TEXT.__gcc_except_tab: 0x62c
-  __TEXT.__cstring: 0x70df9
+  __TEXT.__cstring: 0x718bc
   __TEXT.__dlopen_cstrs: 0x164
   __TEXT.__oslogstring: 0xb55
-  __TEXT.__unwind_info: 0x71c0
+  __TEXT.__unwind_info: 0x71e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4318
+  __DATA_CONST.__const: 0x4328
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_arraydata: 0x170
   __DATA_CONST.__got: 0x1de0
   __AUTH_CONST.__const: 0x7200
-  __AUTH_CONST.__cfstring: 0x10540
+  __AUTH_CONST.__cfstring: 0x105c0
   __AUTH_CONST.__objc_const: 0xc58
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x1b8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9053
-  Symbols:   8797
-  CStrings:  9188
+  Functions: 9066
+  Symbols:   8801
+  CStrings:  9265
 
Symbols:
+ APEndpointCreateDecoratedName
+ _APEndpointCopyAudioOutputLatencyMsForStream
+ _APSCMTimeMakeWithRTPTimestamp
+ _APSenderSessionGetFallbackToInfraReasonForUnselectedTransport
+ _APTDiagnosticSendStreamInfo
+ _APTNANDataSessionGetDatapathRSSI
+ _APTransportConnectionQoSFromSocketQoS
+ _FigEndpointSetProperty
+ _FigSignalErrorAt3
+ ___block_descriptor_56_e15_v24?0r^v8r^v16l
+ ___endpoint_performRemoteTeardown_block_invoke
+ ___endpoint_performRemoteTeardown_block_invoke_2
+ ___endpoint_performRemoteTeardown_block_invoke_3
+ _bufferedAudioEngine_isHoseClusterBuddy
+ _emp_demoteEndpoint
+ _endpointAggregate_handleAudioStreamResumed
+ _endpoint_handleAudioStreamResumed
+ _kAPEndpointProperty_AudioOutputLatencyMs
+ _kAPEndpointStreamBufferedAudioEngineCreationOption_ForceFirstRemoteMediaTime
+ _kAPEndpointStreamConnectionKey_QoS
+ _sessionfactory_RemoveAirPlaySession
+ _sessionfactory_RemoveSessionClient
+ emp_demoteEndpoint
+ sessionfactory_RemoveAirPlaySession
+ sessionfactory_RemoveSessionClient
- _APTDiagnosticMulticastDataToAllHosts
- _FigSignalErrorAtGM
- _OUTLINED_FUNCTION_267
- _OUTLINED_FUNCTION_268
- _OUTLINED_FUNCTION_269
- _OUTLINED_FUNCTION_270
- _OUTLINED_FUNCTION_271
- _OUTLINED_FUNCTION_272
- _OUTLINED_FUNCTION_273
- _OUTLINED_FUNCTION_274
- _OUTLINED_FUNCTION_275
- _OUTLINED_FUNCTION_276
- _OUTLINED_FUNCTION_277
- ___block_descriptor_48_e15_v24?0r^v8r^v16l
- ___endpoint_prepareLocalTeardown_block_invoke
- ___endpoint_prepareLocalTeardown_block_invoke_2
- ___endpoint_prepareLocalTeardown_block_invoke_3
- ___epp_EnsureAuthorizedWithCompletionCallback_block_invoke_2
- _apsession_getNANRSSI
- _bufferedAudioEngine_isHoseInStereoPair
- epp_EnsureAuthorizedWithCompletionCallback
CStrings:
+ "%@ms"
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "-108"
+ "-876"
+ "-877"
+ "-878"
+ "-879"
+ "-880"
+ "1005.7.1"
+ "<ProactiveNANPairing> [%{ptr}] Feature disabled from prefs"
+ "APAudioEngineBufferedAdapter.c"
+ "APAudioSourceSharedMemory.c"
+ "APEndpoint.m"
+ "APEndpointCreateDecoratedName"
+ "APEndpointPlaybackSessionRemoteControl.m"
+ "APEndpointStreamAggregateAudio.c"
+ "APSampleBufferConsumerForEndpointStreamAudioEngine.c"
+ "APVirtualDisplayTestSink.c"
+ "Action not supported"
+ "Allocation error"
+ "Audio source has been invalidated"
+ "AudioOutputLatencyMs"
+ "BAE [%{ptr}] %s(startup) maxWaitPhaseTwoClusterBuddyMs set to %d (%lld ticks)\n"
+ "BAE [%{ptr}] %s(test) Forcing firstRemoteMediaTime to %1.6f (%lld/%d)\n"
+ "BAE [%{ptr}] %s[0x%04X] (startup) Cluster Member hose [%{ptr}] (%@) Primed -> Ready %s (clusterUUID %@)\n"
+ "Cannot register path"
+ "Failed allocating audio buffer"
+ "Failed to create bufferMemObject"
+ "Failed to create deep copy"
+ "Failed to create stateMemObject"
+ "Failed to de-serialize"
+ "Failed to serialize"
+ "Invalid Trigger Token"
+ "Item is NULL"
+ "NULL audioEngine"
+ "NULL bufferMemObject in message"
+ "NULL stateMemObject in message"
+ "NULL trigger"
+ "NULL triggerTokenOut"
+ "No data in response"
+ "No incoming message"
+ "No matched request found"
+ "No trigger installed"
+ "OSStatus epp_Dissociate(FigEndpointRef)_block_invoke"
+ "OSStatus sessionfactory_RemoveAirPlaySession(APSenderSessionFactoryRef, CFStringRef)"
+ "Object invalidated"
+ "Only support one trigger installed at a time"
+ "Scheduling kFigEndpointManagerNotification_AvailableEndpointsChanged in %lld ns with %llu ns leeway\n"
+ "[%{ptr}] %@ is%s recommended%?{end} with err=%#m"
+ "[%{ptr}] Activation callback %@ for [%{ptr}]"
+ "[%{ptr}] Authorization request callback %@ for [%{ptr}] result %#m"
+ "[%{ptr}] COLLISION %@ clusterPlus [%{ptr}] subEndpointPlus [%{ptr}] has inner [%{ptr}] but found real [%{ptr}]"
+ "[%{ptr}] COLLISION %@ plus [%{ptr}] has inner [%{ptr}] but found real [%{ptr}]"
+ "[%{ptr}] Completion callback %@ for [%{ptr}]"
+ "[%{ptr}] Dissociating inner [%{ptr}]"
+ "[%{ptr}] Duplicate activate in stage %d; keeping current activation\n"
+ "[%{ptr}] Ensure Authorized with inner [%{ptr}] proxyID %@"
+ "[%{ptr}] Failed to remove session for deviceID %@: %#m\n"
+ "[%{ptr}] NAN RSSI sample failed: %#m\n"
+ "[%{ptr}] Removing session client for %@ endpoint [%{ptr}] due to failure in upgrade session path.\n"
+ "[%{ptr}] Removing session for %@ due to failure in new session path.\n"
+ "[%{ptr}] Send Command callback %@ for [%{ptr}] forward? %s"
+ "[%{ptr}] Set up %@ stream and useRealtimeAPAT=%s (localDeviceType=%d receiverSupportsRealtimeAPAT=%s isScreenMirroringUsage=%s engineType=%@"
+ "[%{ptr}] audio output latency: %@ms\n"
+ "alloc failed"
+ "because peer was primed or better"
+ "bufferMemory region maps to NULL"
+ "bufferMemorySize is zero"
+ "bufferedAudioEngine_isHoseClusterBuddy"
+ "can't find valid video track"
+ "com.apple.private.restrict-post.AirPlay.DACP.mutetoggle"
+ "com.apple.private.restrict-post.AirPlay.DACP.volumedown"
+ "com.apple.private.restrict-post.AirPlay.DACP.volumeup"
+ "due to timeout"
+ "err"
+ "forceFirstRemoteMediaTime"
+ "kCMBaseObjectError_AllocationFailed"
+ "kCMBaseObjectError_Invalidated"
+ "kCMBaseObjectError_ParamErr"
+ "kCMBaseObjectError_ValueNotAvailable"
+ "kFigEndpointError_AllocationFailed"
+ "kFigEndpointPlaybackSessionError_AllocationFailed"
+ "kFigEndpointPlaybackSessionError_InvalidParameter"
+ "kFigEndpointStreamAudioEngineError_AllocationFailed"
+ "maxWaitPhaseTwoClusterBuddyMs"
+ "messageID is missing in response event"
+ "sbceas_InstallLowWaterTrigger_block_invoke"
+ "sbceas_RemoveLowWaterTrigger_block_invoke"
+ "sessionfactory_RemoveAirPlaySession"
+ "stateMemObject maps to NULL"
+ "stateMemoryLength < sizeof(RingState)"
+ "streamConnectionKeyQoS"
+ "type is missing in response event"
+ "void bufferedAudioEngine_updateHosesPrimed(FigEndpointStreamAudioEngineRef, uint64_t, uint64_t, Boolean, APAudioEngineBufferedPrimingStats *)"
+ "void endpointAggregate_handleAudioStreamResumed(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
+ "void endpointCluster_CallActivationCompletionCallback(FigEndpointRef, uint64_t, FigEndpointFeatures, OSStatus, FigEndpointActivationCompletionCallback, void *)"
+ "void endpoint_handleAudioStreamResumed(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
+ "void endpoint_performRemoteTeardown(void *)_block_invoke"
- "%s signalled err=%d at <>:%d"
- "980.77.5.3"
- "BAE [%{ptr}] %s[0x%04X] (startup) Stereo Pair Hoses [%{ptr}] (%@) Primed -> Ready due to timeout\n"
- "BAE [%{ptr}] %s[0x%04X] (startup) Stereo Pair hose (peer) [%{ptr}] (%@) Primed -> Ready because peer was primed or better\n"
- "BAE [%{ptr}] %s[0x%04X] (startup) Stereo Pair hose [%{ptr}] (%@) Primed -> Ready because peer was primed or better\n"
- "Scheduling kFigEndpointManagerNotification_AvailableEndpointsChanged in %lld ns\n"
- "Terminus_MeshRegistration"
- "[%{ptr}] %@ is%s recommended?{end} with err=%#m"
- "[%{ptr}] Activation callback with inner [%{ptr}] context %@ forward? %s"
- "[%{ptr}] Authorization request completion callback for inner %s [%{ptr}] result %#m"
- "[%{ptr}] Completion callback with inner [%{ptr}] context %@ forward? %s"
- "[%{ptr}] Dissociating"
- "[%{ptr}] Ensure Authorized with inner [%{ptr}] context %@"
- "[%{ptr}] Send Command callback with inner [%{ptr}] context %@ forward? %s"
- "[%{ptr}] Set up %@ stream and useRealtimeAPAT=%s (localDeviceType=%d receiverSupportsRealtimeAPAT=%s isScreenMirroringUsage=%s"
- "bufferedAudioEngine_isHoseInStereoPair"
- "com.apple.AirTunes.DACP.mutetoggle"
- "com.apple.AirTunes.DACP.volumedown"
- "com.apple.AirTunes.DACP.volumeup"
- "void bufferedAudioEngine_updateHosesPrimed(FigEndpointStreamAudioEngineRef, uint64_t, Boolean, APAudioEngineBufferedPrimingStats *)"
- "void endpoint_prepareLocalTeardown(APEndpointDeactivationContext *)_block_invoke"
```
