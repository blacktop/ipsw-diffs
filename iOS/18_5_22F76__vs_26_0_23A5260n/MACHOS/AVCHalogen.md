## AVCHalogen

> `/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/AVCHalogen`

```diff

-860.7.1.0.0
-  __TEXT.__text: 0x9238
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__cstring: 0x1fc8
+890.61.4.11.2
+  __TEXT.__text: 0xa3ec
+  __TEXT.__auth_stubs: 0x870
+  __TEXT.__cstring: 0x279f
   __TEXT.__const: 0xa0
-  __TEXT.__unwind_info: 0x1e8
-  __DATA_CONST.__auth_got: 0x420
-  __DATA_CONST.__got: 0x1a8
+  __TEXT.__unwind_info: 0x218
+  __DATA_CONST.__auth_got: 0x438
+  __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__const: 0x3e0
-  __DATA_CONST.__cfstring: 0x1c0
+  __DATA_CONST.__cfstring: 0x220
   __DATA.__data: 0x1c0
   __DATA.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  UUID: 80C52DC8-084D-3078-A88A-A69B5BEA1036
-  Functions: 202
-  Symbols:   191
-  CStrings:  168
+  UUID: DDD766D5-EAB2-3834-BB56-4005E176C964
+  Functions: 219
+  Symbols:   198
+  CStrings:  218
 
Symbols:
+ _APAudioEngineBufferedAdapterCreate
+ _APAudioFormatGetTransportAudioFormatForPCMFormatSender
+ _APSAudioFormatDescriptionGetASBD
+ _APSAudioFormatDescriptionGetPCMASBD
+ _APSAudioFormatDescriptionListCopyDebugString
+ _APSAudioFormatDescriptionListCreateASRDArrayPCM
+ _APSAudioFormatDescriptionListCreateIntersection
+ _APSAudioFormatDescriptionListCreateWithFigEndpointStreamAudioFormatDescriptionArray
+ _APSAudioFormatDescriptionListFindCompatibleTransportFromPCMAndSetDefault
+ _APSAudioFormatDescriptionListGetDefaultFormat
+ _APSAudioFormatDescriptionListGetFormatCount
+ _APSSettingsGetDouble
+ _APSTapToRadarInvoke
+ _APSZTSControllerCreate
+ _APSZTSControllerGetZeroTimeStamp
+ _CFAllocatorAllocateTyped
+ _FigSignalErrorAt3
+ _fig_log_get_emitter
+ _kAPEndpointProperty_HALVolumeDB
+ _kAPEndpointStreamAudioEngineNotification_DynamicLatencyOffsetChanged
+ _kAPEndpointStreamAudioEngineProperty_DynamicLatencyOffsetMs
+ _kAPEndpointStreamAudioEngineProperty_StartupOptions
+ _kAPHALAudioDeviceCreationOption_AudioStreamOverride
+ _kAPSRadarLoggingComponent_AirPlayNewBugs
+ _kFigEndpointStreamAudioEngineResumeOption_EndpointStreamHint
+ _kFigEndpointStreamProperty_SupportedAudioFormatDescriptions
- _APAudioFormatGetTransportAudioFormatForPCMFormatLowLatencySender
- _APSLatencyOffsetStepperCreate
- _APSLatencyOffsetStepperGetOffsetSamples
- _APSLatencyOffsetStepperSetTargetLatencyOffset
- _APSLatencyOffsetStepperStepForInterval
- _CFAllocatorAllocate
- _CFNumberGetValue
- _CMClockConvertHostTimeToSystemUnits
- _CMTimebaseGetTimeWithTimeScale
- _FigGetCFPreferenceDoubleWithDefault
- _FigSignalErrorAt
- _FigSimpleMutexCreate
- _FigSimpleMutexDestroy
- _FigSimpleMutexLock
- _FigSimpleMutexUnlock
- _kAPEndpointStreamNotificationPayloadKey_DynamicLatencyOffsetMs
- _kAPEndpointStreamNotification_DynamicLatencyOffsetDidChange
- _kAPEndpointStreamProperty_DynamicLatencyOffsetMs
- _kFigEndpointProperty_VolumeDB
CStrings:
+ " [%{ptr}] APHALAudioDevice executing without using default transport formats"
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "(Fig)"
+ "APHALAudioControl.c"
+ "APHALAudioDevice.c"
+ "APHALAudioStream.c"
+ "AudioEngineDynamicLatencyOffsetChangedCallback"
+ "Could not allocate APHALAudioSharedState"
+ "Could not allocate volumeContextRef"
+ "Device was unplugged"
+ "EndpointStream has NULL ID"
+ "Expecting WriteMix operation"
+ "Failed to create notification queue"
+ "Initializing default output format [%{asbd}]"
+ "NULL changeRecord"
+ "Need at least one supported PCM format from endpointStream"
+ "No AudioEngine"
+ "No compatible transport format exists for selected PCM format."
+ "OSStatus VerifyDefaultOutputFormat(APHALAudioStreamStorage *)"
+ "OSStatus device_copyEndpointAndEndpointStreamFromCreationParameters(CFAllocatorRef, FigEndpointRef, FigEndpointStreamRef, CFDictionaryRef, FigEndpointRef *, FigEndpointStreamRef *, CFStringRef *, Boolean *, CFDictionaryRef *, CFDictionaryRef *)"
+ "Replacing Audio endpoint stream[%{ptr}] with BufferedAudio endpoint stream[%{ptr}]\n"
+ "SetupMonitoring"
+ "Streaming Audio Bounds Violation"
+ "Streaming Audio DoIO Bounds Checking Violation: %@ (log latency: %1.3f ms)\n"
+ "TTR: Streaming Audio DoIO Bounds Checking Violation"
+ "Unknown change action"
+ "VerifyDefaultOutputFormat"
+ "Verifying default output format [%{asbd}]"
+ "[%s] mSampleRate = %f. mFormatID = %C. prevailingPCMASBD: [%{asbd}]\n"
+ "[%s] prevailingTransportFormat: [%{asbd}]"
+ "[%{ptr}] %s: IODiscontinuity ,%1.3f, ExpectedFrame ,%1.3f, ReceivedFrame ,%1.3f, (log latency: %1.3f ms)"
+ "[%{ptr}] %s: NowTicks ,%lu, SampleTime ,%1.3f, HostTime ,%lu, (log latency: %1.3f ms)"
+ "[%{ptr}] Audio format %{asbd} sent to audio engine for transport format.\n"
+ "[%{ptr}] LLA Multichannel Audio format %{asbd} sent to audio engine for transport format.\n"
+ "[%{ptr}] Setting dynamic latency offset to %d\n"
+ "[%{ptr}] Updated dynamic latency offset to %d ms\n"
+ "[%{ptr}] Using %@[%{ptr}]"
+ "[%{ptr}] storage->shared->prevailingTransportFormat not set as expected"
+ "[%{ptr}] storage->shared->supportedTransportFormats not set as expected"
+ "[%{ptr}] supportedTransportFormats=%@"
+ "bad"
+ "com.apple.coremedia"
+ "device_GetZeroTimeStampWithPresentationOffset"
+ "good"
+ "kAudioHardwareBadDeviceError"
+ "kAudioHardwareBadObjectError"
+ "kAudioHardwareIllegalOperationError"
+ "kAudioHardwareUnsupportedOperationError"
+ "kCMBaseObjectError_AllocationFailed"
+ "kCMBaseObjectError_ParamErr"
+ "kFigEndpointStreamError_InvalidParameter"
+ "maxRateOfChange"
+ "mediumLatencyPathway"
+ "sampleRate=%u[%s] bytesPerFrame=%u[%s] ioBufferFrameSize=%u[%s] framesToDrop=%u[%s] bytesToDrop=%llu length=%llu"
+ "stream_discontinuityLogger"
+ "stream_ttrLogger"
+ "stream_zeroTimeStampLogger"
+ "void AudioEngineDynamicLatencyOffsetChangedCallback(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
+ "void stream_ttrLogger(const APSAsyncLoggerParameters *, Float64)"
- "EndpointStreamDynamicLatencyOffsetDidChangeCallback"
- "Initialize default output format [%{asbd}]"
- "InitializeDefaultOutputFormat"
- "OSStatus InitializeDefaultOutputFormat(APHALAudioStreamStorage *)"
- "OSStatus device_copyEndpointAndEndpointStreamFromCreationParameters(CFAllocatorRef, FigEndpointRef, FigEndpointStreamRef, CFDictionaryRef, FigEndpointRef *, FigEndpointStreamRef *, CFDictionaryRef *)"
- "SetupEndpointStreamMonitoring"
- "[%s] mSampleRate = %f. mFormatID = %C. prevailingASBD: [%{asbd}]\n"
- "[%{ptr}] IODiscontinuity: %1.3f ms. Frame expected: %1.3f; got: %1.3f. (log latency: %1.3f ms)\n"
- "[%{ptr}] ZTS Info. NowTicks: %lu SampleTime: %1.3f HostTime: %lu (log latency: %1.3f ms)"
- "[%{ptr}] using AudioEngine [%{ptr}]"
- "device_GetZeroTimeStampWithSkewOffset"
- "latencyOffsetUpdateMaxRate"

```
