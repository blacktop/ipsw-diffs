## CMContinuityCaptureCore

> `/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/Versions/A/CMContinuityCaptureCore`

```diff

-587.101.4.0.0
-  __TEXT.__text: 0x9161c
-  __TEXT.__auth_stubs: 0xd80
+587.120.2.0.1
+  __TEXT.__text: 0x96a98
+  __TEXT.__auth_stubs: 0xdd0
   __TEXT.__objc_methlist: 0x4adc
-  __TEXT.__const: 0x318
-  __TEXT.__cstring: 0x75a8
-  __TEXT.__gcc_except_tab: 0x418c
-  __TEXT.__oslogstring: 0xa28e
-  __TEXT.__unwind_info: 0x1fe8
-  __TEXT.__objc_classname: 0xc00
-  __TEXT.__objc_methname: 0xb7f2
+  __TEXT.__const: 0x328
+  __TEXT.__cstring: 0x8319
+  __TEXT.__oslogstring: 0xbde5
+  __TEXT.__gcc_except_tab: 0x439c
+  __TEXT.__unwind_info: 0x2030
+  __TEXT.__objc_classname: 0xc01
+  __TEXT.__objc_methname: 0xb80c
   __TEXT.__objc_methtype: 0x262b
-  __TEXT.__objc_stubs: 0x8900
-  __DATA_CONST.__got: 0x620
-  __DATA_CONST.__const: 0x8b8
+  __TEXT.__objc_stubs: 0x8920
+  __DATA_CONST.__got: 0x628
+  __DATA_CONST.__const: 0x8d8
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2780
+  __DATA_CONST.__objc_selrefs: 0x2788
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__auth_got: 0x6d0
-  __AUTH_CONST.__const: 0x20a0
-  __AUTH_CONST.__cfstring: 0x4640
+  __AUTH_CONST.__auth_got: 0x6f8
+  __AUTH_CONST.__const: 0x2060
+  __AUTH_CONST.__cfstring: 0x46c0
   __AUTH_CONST.__objc_const: 0x8808
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_arrayobj: 0x60

   __AUTH.__objc_data: 0xfa0
   __DATA.__objc_ivar: 0x7b4
   __DATA.__data: 0xd60
-  __DATA.__common: 0x60
+  __DATA.__common: 0x90
   __DATA.__bss: 0x160
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio

   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/Versions/A/WiFiPeerToPeer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2214
-  Symbols:   5536
-  CStrings:  3893
+  Functions: 2222
+  Symbols:   5559
+  CStrings:  4001
 
Symbols:
+ -[CVPixelBufferCoder initWithCoder:].cold.2
+ -[CVPixelBufferCoder initWithCoder:].cold.3
+ GCC_except_table10
+ _CFPreferencesGetAppIntegerValue
+ _CVPixelBufferGetIOSurface
+ _IOSurfaceGetID
+ __62-[CMContinuityCaptureAudioDevice stopCaptureStack:completion:]_block_invoke.83
+ __70-[CMContinuityCaptureAudioInputProvider _bringUpXPCConnectionToHelper]_block_invoke.131
+ __70-[CMContinuityCaptureAudioInputProvider _bringUpXPCConnectionToHelper]_block_invoke.132
+ __76-[CMContinuityCaptureAudioInputProvider listener:shouldAcceptNewConnection:]_block_invoke.115
+ __76-[CMContinuityCaptureAudioInputProvider listener:shouldAcceptNewConnection:]_block_invoke.117
+ __76-[CMContinuityCaptureAudioInputProvider listener:shouldAcceptNewConnection:]_block_invoke.118
+ __87-[CMContinuityCaptureAudioInputProvider getRemotelyCollectedLatencyMetricsForUniqueID:]_block_invoke.36
+ ___67-[CMContinuityCaptureTimeSyncClock startEmittingHeartBeatSignposts]_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ __block_literal_global.282
+ __block_literal_global.73
+ __block_literal_global.79
+ __block_literal_global.85
+ __block_literal_global.89
+ _dispatch_activate
+ _gCMContinuityCaptureAudioXPCHelperTrace
+ _gCMContinuityCaptureMetricsReporterTrace
+ _gCMContinuityCaptureTimeSyncClockTrace
+ _gGMFigKTraceEnabled
+ _kdebug_trace
+ _objc_msgSend$availableClockIdentifiers
- +[CMContinuityCaptureAudioInputProvider sharedInstance].cold.1
- __62-[CMContinuityCaptureAudioDevice stopCaptureStack:completion:]_block_invoke.80
- __76-[CMContinuityCaptureAudioInputProvider listener:shouldAcceptNewConnection:]_block_invoke.113
- __76-[CMContinuityCaptureAudioInputProvider listener:shouldAcceptNewConnection:]_block_invoke.114
- ___70-[CMContinuityCaptureAudioInputProvider _bringUpXPCConnectionToHelper]_block_invoke_3
- ___70-[CMContinuityCaptureAudioInputProvider _bringUpXPCConnectionToHelper]_block_invoke_4
- ___76-[CMContinuityCaptureAudioInputProvider listener:shouldAcceptNewConnection:]_block_invoke_2
- ___87-[CMContinuityCaptureAudioInputProvider getRemotelyCollectedLatencyMetricsForUniqueID:]_block_invoke_2
- __block_literal_global.274
- __block_literal_global.45
- __block_literal_global.76
- __block_literal_global.82
CStrings:
+ "+[CMContinuityCaptureAudioInputProvider sharedInstance]_block_invoke"
+ "-[CMContinuityCaptureAudioInputProvider _bringUpXPCConnectionToHelper]_block_invoke"
+ "-[CMContinuityCaptureAudioInputProvider _bringUpXPCConnectionToHelper]_block_invoke_2"
+ "-[CMContinuityCaptureAudioInputProvider enqueueSampleBuffer:forAudioDeviceUID:]"
+ "-[CMContinuityCaptureAudioInputProvider enqueueSampleBuffer:forAudioDeviceUID:]_block_invoke"
+ "-[CMContinuityCaptureAudioInputProvider getRemotelyCollectedLatencyMetricsForUniqueID:]_block_invoke"
+ "-[CMContinuityCaptureAudioInputProvider listener:shouldAcceptNewConnection:]_block_invoke"
+ "-[CMContinuityCaptureAudioInputProvider publishDeviceForClientDeviceUID:audioDeviceUID:name:deviceModel:]_block_invoke"
+ "-[CMContinuityCaptureAudioInputProvider receiverConnectedWithReply:]"
+ "-[CMContinuityCaptureAudioInputProvider receiverConnectedWithReply:]_block_invoke_2"
+ "-[CMContinuityCaptureAudioInputProvider startCollectingLatencyMetricsRemotelyWithUniqueID:forAudioDeviceUID:]"
+ "-[CMContinuityCaptureAudioInputProvider startCollectingLatencyMetricsRemotelyWithUniqueID:forAudioDeviceUID:]_block_invoke"
+ "-[CMContinuityCaptureAudioInputProvider startFillingSilenceAudioDataIfApplicableForAudioDeviceUID:]"
+ "-[CMContinuityCaptureAudioInputProvider startFillingSilenceAudioDataIfApplicableForAudioDeviceUID:]_block_invoke"
+ "-[CMContinuityCaptureAudioInputProvider terminateDeviceForClientDeviceUID:]_block_invoke"
+ "-[CMContinuityCaptureAudioInputProvider updateAvailableAudioDeviceUIDs:]"
+ "-[CMContinuityCaptureAudioInputProvider updateNetworkClockWithSynchronizedNetworkTime:forSampleTime:networkClockIdentifier:transportTypeIsUSB:forAudioDeviceUID:]"
+ "-[CMContinuityCaptureAudioInputProvider updateNetworkClockWithSynchronizedNetworkTime:forSampleTime:networkClockIdentifier:transportTypeIsUSB:forAudioDeviceUID:]_block_invoke"
+ "-[CMContinuityCaptureAudioInputProvider updateUSBActive:forAudioDeviceUID:]"
+ "-[CMContinuityCaptureAudioInputProvider updateUSBActive:forAudioDeviceUID:]_block_invoke"
+ "-[CMContinuityCaptureAudioInputProvider useCachedNetworkClockIfPossibleForAudioDeviceUID:]"
+ "-[CMContinuityCaptureAudioInputProvider useCachedNetworkClockIfPossibleForAudioDeviceUID:]_block_invoke"
+ "-[CMContinuityCaptureAudioXPCHelper _updateRemoteReceiver:]"
+ "-[CMContinuityCaptureAudioXPCHelper listener:shouldAcceptNewConnection:]"
+ "-[CMContinuityCaptureAudioXPCHelper providerConnectedWithListenerEndpoint:]"
+ "-[CMContinuityCaptureAudioXPCHelper receiverConnected]"
+ "-[CMContinuityCaptureFrameLatencyMetrics addLatencyNumberInMilliSeconds:]"
+ "-[CMContinuityCaptureLocalFrameLatencyMetrics _finishCollectingMetrics]"
+ "-[CMContinuityCaptureMetricsReporter _addLatencyMetrics:]"
+ "-[CMContinuityCaptureMetricsReporter _clearAndSubmitAllMetrics]"
+ "-[CMContinuityCaptureMetricsReporter _clearAndSubmitAllMetrics]_block_invoke"
+ "-[CMContinuityCaptureMetricsReporter _submitMetricsToRTCReporting:]"
+ "-[CMContinuityCaptureTimeSyncClock initWithClock:]"
+ "-[CMContinuityCaptureTimeSyncClock startEmittingHeartBeatSignposts]"
+ "-[CMContinuityCaptureTimeSyncClock startEmittingHeartBeatSignposts]_block_invoke"
+ "-[CVPixelBufferCoder _createPixelBufferForImage:fillWidth:fillHeight:]"
+ "-[CVPixelBufferCoder encodeWithCoder:]"
+ "-[CVPixelBufferCoder initWithCoder:]"
+ "-[NSCoder(CVPixelBuffer) decodeCVPixelBufferForKey:expectSourceMedia:]"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: %@ ContinuityCaptureMic feature flag not enabled"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Calling on receiver proxy %@ enqueue sbuf with pts %.3f"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Calling on receiver proxy %@ finish collecting latency metrics with uniqueID %lld"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Calling on receiver proxy %@ publish device for sidecar device UID %@ audio device UID %@ name %@"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Calling on receiver proxy %@ start collecting latency metrics with uniqueID %lld for UID %@"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Calling on receiver proxy %@ startFillingSilenceAudioDataIfApplicable for UID %@"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Calling on receiver proxy %@ terminate device for UID %@"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Calling on receiver proxy %@ to publish stored device UIDs %@, firstDeviceDiscoveryFinished %d "
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Calling on receiver proxy %@ update network clock with synchronized network time %llu sampleTime %llu clock identifier %llu transportTypeIsUSB %d for UID %@"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Calling on receiver proxy %@ updateUSBActive %d for UID %@"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Calling on receiver proxy %@ use cached network clock if possible for UID %@"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Created a connection to helper %@ remote xpcHelper %@"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Received audio buffer from AVC without attached network timestamp. Dropping buffer."
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Receiver connected %@ delegate %@"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Receiver proxy %@ told me to start streaming for UID %@"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Receiver proxy %@ told me to stop streaming for UID %@"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Skip collecting latency metrics with nil UID"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Skip enqueueing sbuf %p UID %@"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Skip pause enqueuing audioData with nil UID"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Skip update USBActive with nil UID"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Skip updating synchronized network time with nil UID"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Skip updating using cached network clock with nil UID"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Trying to terminate audio device for sidecar device UID %@ but couldn't find audio device UID"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Update available audio device UIDs %@"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: Updated connection to receiver %@ -> %@ audioInputReceiver %@"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: connection interrupted %@, client should connect back again"
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: connection interrupted %@. Scheduling reconnect in 5sec."
+ "<<<< CMContinuityCaptureAudioInputProvider >>>> %s: connection invalidated %@"
+ "<<<< CMContinuityCaptureAudioRouteManager >>>> %s: Failed to find audioDevice with UID %@ availableDevices %@"
+ "<<<< CMContinuityCaptureAudioXPCHelper >>>> %s: Connection %@ does not have the proper entitlement '%@' to use CMContinuityCaptureAudioInputProvider."
+ "<<<< CMContinuityCaptureAudioXPCHelper >>>> %s: Connection %@ does not have the proper entitlement '%@' to use CMContinuityCaptureAudioInputReceiver."
+ "<<<< CMContinuityCaptureAudioXPCHelper >>>> %s: Got new connection for unknown listener %@ connection %@"
+ "<<<< CMContinuityCaptureAudioXPCHelper >>>> %s: Got new connection from audio provider %@ (expecting from ContinuityCaptureAgent)"
+ "<<<< CMContinuityCaptureAudioXPCHelper >>>> %s: Got new connection from audio receiver %@ (expecting from coreaudiod)"
+ "<<<< CMContinuityCaptureAudioXPCHelper >>>> %s: Provider connected with new listener endpoint %@ -> %@"
+ "<<<< CMContinuityCaptureAudioXPCHelper >>>> %s: Provider listener endpoint is already available, sending it to remote receiver now. This might be a result from process crashing"
+ "<<<< CMContinuityCaptureAudioXPCHelper >>>> %s: Remote receiver connected %@"
+ "<<<< CMContinuityCaptureAudioXPCHelper >>>> %s: Update remote receiver %@ -> %@"
+ "<<<< CMContinuityCaptureMetricsReporter >>>> %s: %@ RTCReporting %@ started successfully with sessionInfo %@"
+ "<<<< CMContinuityCaptureMetricsReporter >>>> %s: %@ failed to submit RTCReporting payload for %@, error %@"
+ "<<<< CMContinuityCaptureMetricsReporter >>>> %s: %@ finishing collecting metrics, collecting remotely:%d"
+ "<<<< CMContinuityCaptureMetricsReporter >>>> %s: %@ sessionID %d submitting metrics %@"
+ "<<<< CMContinuityCaptureMetricsReporter >>>> %s: %@ submit payload succeeded:%d error %@ %@"
+ "<<<< CMContinuityCaptureMetricsReporter >>>> %s: %@:%llu trying to add an invalid latency number %d -- dropping"
+ "<<<< CMContinuityCaptureMetricsReporter >>>> %s: Failed waiting for RTCReportingSession startConfiguration to complete after %f seconds"
+ "<<<< CMContinuityCaptureMetricsReporter >>>> %s: Metric reporter %@ adding %@ with mediaID %d uniqueID:%llu. Current metrics count %lu"
+ "<<<< CMContinuityCaptureMetricsReporter >>>> %s: RTCReporting failed to create with sessionInfo %@"
+ "<<<< CMContinuityCaptureMetricsReporter >>>> %s: RTCReporting session startConfiguration completes, signalling startGroup %@"
+ "<<<< CMContinuityCaptureMetricsReporter >>>> %s: RTCReporting startConfiguration completion handler called with nil backends, metrics won't be sent out"
+ "<<<< CMContinuityCaptureTimeSyncClock >>>> %s: %@ %lld: (%lld) %lld -> %lld"
+ "<<<< CMContinuityCaptureTimeSyncClock >>>> %s: %@ starting heart beat signposts with interval %lu seconds"
+ "<<<< CMContinuityCaptureTimeSyncClock >>>> %s: Failed to create PTP clock with identifier %llu, available identifiers %@"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: Could not create pixel buffer: %d"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: Could not read source media %@, falling back to pixel buffer copy"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: Could not serialize pixel buffer, error %d"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: Error creating pixel buffer %zu x %zu: %d"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: Expected source media but pixel buffer data was found instead (not fatal)"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: Failed to create pixel buffer %zu x %zu"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: Fallback not using atom data, outdated peer connection for pixel buffer"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: No pixel data"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: bad source image offset"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: image planes don't match, encoded %d allocated %d"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: source image offset overrun"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: source image stride overrun"
+ "availableClockIdentifiers"
+ "cmcontinuitycaptureaudioxpchelper_trace"
+ "cmcontinuitycapturemetricsreporter_trace"
+ "cmcontinuitycapturetimesyncclock_trace"
+ "continuitycapture_timesync_heartbeat_interval"

```
