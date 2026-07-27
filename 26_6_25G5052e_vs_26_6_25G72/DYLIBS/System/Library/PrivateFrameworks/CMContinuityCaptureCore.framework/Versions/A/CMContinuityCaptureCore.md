## CMContinuityCaptureCore

> `/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/Versions/A/CMContinuityCaptureCore`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-665.140.4.0.0
-  __TEXT.__text: 0x9004c
-  __TEXT.__auth_stubs: 0xdc0
+665.140.6.0.0
+  __TEXT.__text: 0x8b3e0
+  __TEXT.__auth_stubs: 0xd70
   __TEXT.__objc_methlist: 0x4c64
-  __TEXT.__const: 0x390
-  __TEXT.__cstring: 0x83b9
-  __TEXT.__oslogstring: 0xbf45
-  __TEXT.__gcc_except_tab: 0x2f18
-  __TEXT.__unwind_info: 0x20d8
-  __TEXT.__objc_classname: 0xc2c
-  __TEXT.__objc_methname: 0xbc13
+  __TEXT.__const: 0x370
+  __TEXT.__cstring: 0x7628
+  __TEXT.__gcc_except_tab: 0x2e14
+  __TEXT.__oslogstring: 0xa3ee
+  __TEXT.__unwind_info: 0x2098
+  __TEXT.__objc_classname: 0xc2b
+  __TEXT.__objc_methname: 0xbbf9
   __TEXT.__objc_methtype: 0x2677
-  __TEXT.__objc_stubs: 0x8b80
-  __DATA_CONST.__got: 0x648
-  __DATA_CONST.__const: 0x8f0
+  __TEXT.__objc_stubs: 0x8b60
+  __DATA_CONST.__got: 0x640
+  __DATA_CONST.__const: 0x8d0
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2838
+  __DATA_CONST.__objc_selrefs: 0x2830
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0x6f0
-  __AUTH_CONST.__const: 0x2090
-  __AUTH_CONST.__cfstring: 0x47e0
+  __AUTH_CONST.__auth_got: 0x6c8
+  __AUTH_CONST.__const: 0x20d0
+  __AUTH_CONST.__cfstring: 0x4760
   __AUTH_CONST.__objc_const: 0x8a78
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_arrayobj: 0x60

   __AUTH.__objc_data: 0xb90
   __DATA.__objc_ivar: 0x7d4
   __DATA.__data: 0xd60
-  __DATA.__common: 0x60
+  __DATA.__common: 0x40
   __DATA.__bss: 0xa0
   __DATA_DIRTY.__objc_data: 0x460
   __DATA_DIRTY.__bss: 0xc0
-  __DATA_DIRTY.__common: 0x30
+  __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2258
-  Symbols:   5106
-  CStrings:  3931
+  Functions: 2250
+  Symbols:   5094
+  CStrings:  3823
 
Symbols:
+ ___70-[CMContinuityCaptureAudioInputProvider _bringUpXPCConnectionToHelper]_block_invoke_3
+ ___70-[CMContinuityCaptureAudioInputProvider _bringUpXPCConnectionToHelper]_block_invoke_4
+ ___76-[CMContinuityCaptureAudioInputProvider listener:shouldAcceptNewConnection:]_block_invoke_2
+ ___87-[CMContinuityCaptureAudioInputProvider getRemotelyCollectedLatencyMetricsForUniqueID:]_block_invoke_2
- GCC_except_table10
- GCC_except_table33
- _CFPreferencesGetAppIntegerValue
- _CVPixelBufferGetIOSurface
- _IOSurfaceGetID
- __70-[CMContinuityCaptureAudioInputProvider _bringUpXPCConnectionToHelper]_block_invoke
- __87-[CMContinuityCaptureAudioInputProvider getRemotelyCollectedLatencyMetricsForUniqueID:]_block_invoke
- ___67-[CMContinuityCaptureTimeSyncClock startEmittingHeartBeatSignposts]_block_invoke
- ___block_descriptor_40_e5_v8?0l
- _dispatch_activate
- _gCMContinuityCaptureAudioXPCHelperTrace
- _gCMContinuityCaptureMetricsReporterTrace
- _gCMContinuityCaptureTimeSyncClockTrace
- _gGMFigKTraceEnabled
- _kdebug_trace
- _objc_msgSend$availableClockIdentifiers
CStrings:
- "+[CMContinuityCaptureAudioInputProvider sharedInstance]_block_invoke"
- "-[CMContinuityCaptureAudioInputProvider _bringUpXPCConnectionToHelper]_block_invoke"
- "-[CMContinuityCaptureAudioInputProvider _bringUpXPCConnectionToHelper]_block_invoke_2"
- "-[CMContinuityCaptureAudioInputProvider enqueueSampleBuffer:forAudioDeviceUID:]"
- "-[CMContinuityCaptureAudioInputProvider enqueueSampleBuffer:forAudioDeviceUID:]_block_invoke"
- "-[CMContinuityCaptureAudioInputProvider getRemotelyCollectedLatencyMetricsForUniqueID:]_block_invoke"
- "-[CMContinuityCaptureAudioInputProvider listener:shouldAcceptNewConnection:]_block_invoke"
- "-[CMContinuityCaptureAudioInputProvider publishDeviceForClientDeviceUID:audioDeviceUID:name:deviceModel:voiceAmplificationModeSupported:]_block_invoke"
- "-[CMContinuityCaptureAudioInputProvider receiverConnectedWithReply:]"
- "-[CMContinuityCaptureAudioInputProvider receiverConnectedWithReply:]_block_invoke_2"
- "-[CMContinuityCaptureAudioInputProvider startCollectingLatencyMetricsRemotelyWithUniqueID:forAudioDeviceUID:]"
- "-[CMContinuityCaptureAudioInputProvider startCollectingLatencyMetricsRemotelyWithUniqueID:forAudioDeviceUID:]_block_invoke"
- "-[CMContinuityCaptureAudioInputProvider startFillingSilenceAudioDataIfApplicableForAudioDeviceUID:]"
- "-[CMContinuityCaptureAudioInputProvider startFillingSilenceAudioDataIfApplicableForAudioDeviceUID:]_block_invoke"
- "-[CMContinuityCaptureAudioInputProvider terminateDeviceForClientDeviceUID:]_block_invoke"
- "-[CMContinuityCaptureAudioInputProvider updateAvailableAudioDeviceUIDs:]"
- "-[CMContinuityCaptureAudioInputProvider updateNetworkClockWithSynchronizedNetworkTime:forSampleTime:networkClockIdentifier:transportTypeIsUSB:forAudioDeviceUID:]"
- "-[CMContinuityCaptureAudioInputProvider updateNetworkClockWithSynchronizedNetworkTime:forSampleTime:networkClockIdentifier:transportTypeIsUSB:forAudioDeviceUID:]_block_invoke"
- "-[CMContinuityCaptureAudioInputProvider updateUSBActive:forAudioDeviceUID:]"
- "-[CMContinuityCaptureAudioInputProvider updateUSBActive:forAudioDeviceUID:]_block_invoke"
- "-[CMContinuityCaptureAudioInputProvider useCachedNetworkClockIfPossibleForAudioDeviceUID:]"
- "-[CMContinuityCaptureAudioInputProvider useCachedNetworkClockIfPossibleForAudioDeviceUID:]_block_invoke"
- "-[CMContinuityCaptureAudioXPCHelper _updateRemoteReceiver:]"
- "-[CMContinuityCaptureAudioXPCHelper listener:shouldAcceptNewConnection:]"
- "-[CMContinuityCaptureAudioXPCHelper providerConnectedWithListenerEndpoint:]"
- "-[CMContinuityCaptureAudioXPCHelper receiverConnected]"
- "-[CMContinuityCaptureFrameLatencyMetrics addLatencyNumberInMilliSeconds:]"
- "-[CMContinuityCaptureLocalFrameLatencyMetrics _finishCollectingMetrics]"
- "-[CMContinuityCaptureMetricsReporter _addLatencyMetrics:]"
- "-[CMContinuityCaptureMetricsReporter _clearAndSubmitAllMetrics]"
- "-[CMContinuityCaptureMetricsReporter _clearAndSubmitAllMetrics]_block_invoke"
- "-[CMContinuityCaptureMetricsReporter _submitMetricsToRTCReporting:]"
- "-[CMContinuityCaptureTimeSyncClock initWithClock:]"
- "-[CMContinuityCaptureTimeSyncClock startEmittingHeartBeatSignposts]"
- "-[CMContinuityCaptureTimeSyncClock startEmittingHeartBeatSignposts]_block_invoke"
- "-[CVPixelBufferCoder _createPixelBufferForImage:fillWidth:fillHeight:]"
- "-[CVPixelBufferCoder encodeWithCoder:]"
- "-[CVPixelBufferCoder initWithCoder:]"
- "-[NSCoder(CVPixelBuffer) decodeCVPixelBufferForKey:expectSourceMedia:]"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: %@ ContinuityCaptureMic feature flag not enabled"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Calling on receiver proxy %@ enqueue sbuf with pts %.3f"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Calling on receiver proxy %@ finish collecting latency metrics with uniqueID %lld"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Calling on receiver proxy %@ publish device for sidecar device UID %@ audio device UID %@ name %@"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Calling on receiver proxy %@ start collecting latency metrics with uniqueID %lld for UID %@"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Calling on receiver proxy %@ startFillingSilenceAudioDataIfApplicable for UID %@"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Calling on receiver proxy %@ terminate device for UID %@"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Calling on receiver proxy %@ to publish stored device UIDs %@, firstDeviceDiscoveryFinished %d "
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Calling on receiver proxy %@ update network clock with synchronized network time %llu sampleTime %llu clock identifier %llu transportTypeIsUSB %d for UID %@"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Calling on receiver proxy %@ updateUSBActive %d for UID %@"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Calling on receiver proxy %@ use cached network clock if possible for UID %@"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Created a connection to helper %@ remote xpcHelper %@"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Received audio buffer from AVC without attached network timestamp. Dropping buffer."
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Receiver connected %@ delegate %@"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Receiver proxy %@ told me to start streaming for UID %@"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Receiver proxy %@ told me to stop streaming for UID %@"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Skip collecting latency metrics with nil UID"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Skip enqueueing sbuf %p UID %@"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Skip pause enqueuing audioData with nil UID"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Skip update USBActive with nil UID"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Skip updating synchronized network time with nil UID"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Skip updating using cached network clock with nil UID"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Trying to terminate audio device for sidecar device UID %@ but couldn't find audio device UID"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Update available audio device UIDs %@"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Updated connection to receiver %@ -> %@ audioInputReceiver %@"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: connection interrupted %@, client should connect back again"
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: connection interrupted %@. Scheduling reconnect in 5sec."
- "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: connection invalidated %@"
- "<<<< CMContinuityCaptureAudioRouteManager >>>> %s: Failed to find audioDevice with UID %@ availableDevices %@"
- "<<<< CMContinuityCaptureAudioXPCHelper >>>> %s: Connection %@ does not have the proper entitlement '%@' to use CMContinuityCaptureAudioInputProvider."
- "<<<< CMContinuityCaptureAudioXPCHelper >>>> %s: Connection %@ does not have the proper entitlement '%@' to use CMContinuityCaptureAudioInputReceiver."
- "<<<< CMContinuityCaptureAudioXPCHelper >>>> %s: Got new connection for unknown listener %@ connection %@"
- "<<<< CMContinuityCaptureAudioXPCHelper >>>> %s: Got new connection from audio provider %@ (expecting from ContinuityCaptureAgent)"
- "<<<< CMContinuityCaptureAudioXPCHelper >>>> %s: Got new connection from audio receiver %@ (expecting from coreaudiod)"
- "<<<< CMContinuityCaptureAudioXPCHelper >>>> %s: Provider connected with new listener endpoint %@ -> %@"
- "<<<< CMContinuityCaptureAudioXPCHelper >>>> %s: Provider listener endpoint is already available, sending it to remote receiver now. This might be a result from process crashing"
- "<<<< CMContinuityCaptureAudioXPCHelper >>>> %s: Remote receiver connected %@"
- "<<<< CMContinuityCaptureAudioXPCHelper >>>> %s: Update remote receiver %@ -> %@"
- "<<<< CMContinuityCaptureMetricsReporter >>>> %s: %@ RTCReporting %@ started successfully with sessionInfo %@"
- "<<<< CMContinuityCaptureMetricsReporter >>>> %s: %@ failed to submit RTCReporting payload for %@, error %@"
- "<<<< CMContinuityCaptureMetricsReporter >>>> %s: %@ finishing collecting metrics, collecting remotely:%d"
- "<<<< CMContinuityCaptureMetricsReporter >>>> %s: %@ sessionID %d submitting metrics %@"
- "<<<< CMContinuityCaptureMetricsReporter >>>> %s: %@ submit payload succeeded:%d error %@ %@"
- "<<<< CMContinuityCaptureMetricsReporter >>>> %s: %@:%llu trying to add an invalid latency number %d -- dropping"
- "<<<< CMContinuityCaptureMetricsReporter >>>> %s: Failed waiting for RTCReportingSession startConfiguration to complete after %f seconds"
- "<<<< CMContinuityCaptureMetricsReporter >>>> %s: Metric reporter %@ adding %@ with mediaID %d uniqueID:%llu. Current metrics count %lu"
- "<<<< CMContinuityCaptureMetricsReporter >>>> %s: RTCReporting failed to create with sessionInfo %@"
- "<<<< CMContinuityCaptureMetricsReporter >>>> %s: RTCReporting session startConfiguration completes, signalling startGroup %@"
- "<<<< CMContinuityCaptureMetricsReporter >>>> %s: RTCReporting startConfiguration completion handler called with nil backends, metrics won't be sent out"
- "<<<< CMContinuityCaptureTimeSyncClock >>>> %s: %@ %lld: (%lld) %lld -> %lld"
- "<<<< CMContinuityCaptureTimeSyncClock >>>> %s: %@ starting heart beat signposts with interval %lu seconds"
- "<<<< CMContinuityCaptureTimeSyncClock >>>> %s: Failed to create PTP clock with identifier %llu, available identifiers %@"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: Could not create pixel buffer: %d"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: Could not read source media %@, falling back to pixel buffer copy"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: Could not serialize pixel buffer, error %d"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: Error creating pixel buffer %zu x %zu: %d"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: Expected source media but pixel buffer data was found instead (not fatal)"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: Failed to create pixel buffer %zu x %zu"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: Fallback not using atom data, outdated peer connection for pixel buffer"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: No pixel data"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: bad source image offset"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: image planes don't match, encoded %d allocated %d"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: source image offset overrun"
- "<<<< NSCoding+CVPixelBufferRef >>>> %s: source image stride overrun"
- "availableClockIdentifiers"
- "cmcontinuitycaptureaudioxpchelper_trace"
- "cmcontinuitycapturemetricsreporter_trace"
- "cmcontinuitycapturetimesyncclock_trace"
- "continuitycapture_timesync_heartbeat_interval"
```
