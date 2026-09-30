## AirPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/AirPlayHalogen.driver/AirPlayHalogen`

```diff

-860.7.1.0.0
-  __TEXT.__text: 0xcfb0
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x28ad
-  __TEXT.__unwind_info: 0x2c0
-  __DATA_CONST.__auth_got: 0x458
-  __DATA_CONST.__got: 0x1a8
+890.61.4.11.2
+  __TEXT.__text: 0xe500
+  __TEXT.__auth_stubs: 0x920
+  __TEXT.__const: 0xbc
+  __TEXT.__cstring: 0x3121
+  __TEXT.__oslogstring: 0x6b
+  __TEXT.__unwind_info: 0x300
+  __DATA_CONST.__auth_got: 0x490
+  __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__const: 0x7b0
-  __DATA_CONST.__cfstring: 0x240
+  __DATA_CONST.__cfstring: 0x2a0
   __DATA.__data: 0x238
   __DATA.__bss: 0x100
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  UUID: 6F825268-E07D-3B60-B85A-6437BAD42D27
-  Functions: 295
-  Symbols:   198
-  CStrings:  210
+  UUID: 0564BBC1-6C6D-35C7-BC1B-A7294F064BC0
+  Functions: 312
+  Symbols:   209
+  CStrings:  266
 
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
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_log_get_emitter
+ _kAPEndpointProperty_HALVolumeDB
+ _kAPEndpointStreamAudioEngineNotification_DynamicLatencyOffsetChanged
+ _kAPEndpointStreamAudioEngineProperty_DynamicLatencyOffsetMs
+ _kAPEndpointStreamAudioEngineProperty_StartupOptions
+ _kAPHALAudioDeviceCreationOption_AudioStreamOverride
+ _kAPSRadarLoggingComponent_AirPlayNewBugs
+ _kFigEndpointStreamAudioEngineResumeOption_EndpointStreamHint
+ _kFigEndpointStreamProperty_SupportedAudioFormatDescriptions
+ _os_log_type_enabled
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
+ "APHALHandoffAudioControl.c"
+ "APHALHandoffAudioDevice.c"
+ "APHALHandoffAudioStream.c"
+ "AirPlayHALPluginFactory %s: apPlugin_InstantiateAirPlayEndpointManager: APGetEndpointManager returned [%p]"
+ "AudioEngineDynamicLatencyOffsetChangedCallback"
+ "Could not allocate APHALAudioSharedState"
+ "Could not allocate APHALHandoffAudioSharedState"
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
