## AVCHalogen

> `/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/AVCHalogen`

```diff

-950.7.1.0.0
-  __TEXT.__text: 0x9e40
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__cstring: 0x25df
-  __TEXT.__const: 0xa0
-  __TEXT.__unwind_info: 0x210
-  __DATA_CONST.__auth_got: 0x438
-  __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0x3e0
-  __DATA_CONST.__cfstring: 0x220
+980.58.1.11.1
+  __TEXT.__text: 0xac60
+  __TEXT.__auth_stubs: 0x8c0
+  __TEXT.__cstring: 0x2a52
+  __TEXT.__const: 0xb0
+  __TEXT.__oslogstring: 0x4b
+  __TEXT.__unwind_info: 0x228
+  __DATA_CONST.__const: 0x3e8
+  __DATA_CONST.__cfstring: 0x2a0
+  __DATA_CONST.__auth_got: 0x460
+  __DATA_CONST.__got: 0x1e0
   __DATA.__data: 0x1c0
   __DATA.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  UUID: 8C2DB39E-85AF-3B6F-9315-6AC73751FA39
-  Functions: 227
-  Symbols:   198
-  CStrings:  201
+  UUID: 568A5667-D620-3D23-AB11-0E32BBF587B1
+  Functions: 220
+  Symbols:   207
+  CStrings:  239
 
Symbols:
+ _APAudioFormatSelectorRealTimeCreate
+ _APGetSignpostsLogHandle
+ _APSIsMac
+ _APSSetFBOPropertyDictionary
+ _APSSettingsGetBooleanIfPresent
+ _CFNumberGetValue
+ _CUObfuscatedPtr
+ _FigCFDictionarySetInt64
+ _FigCFDictionarySetUInt32
+ _FigCFDictionarySetValueFromKeyInDict
+ _FigCFNumberCreateUInt32
+ _FigSignalErrorAt3
+ _UpTicksToMilliseconds
+ __os_signpost_emit_with_name_impl
+ _kAPAudioEngineResumeOption_HALLatencyMs
+ _kAPAudioFormatSelectorCreationOption_UsingP2P
+ _kAPEndpointStreamAudioEngineType_Buffered
+ _kAPEndpointStreamBufferedAudioEngineProperty_HALStartIOMetrics
+ _kAPEndpointStreamProperty_AudioEngineType
+ _kAPHALAudioDeviceCreationOption_IsP2PConnection
+ _kAPHALAudioStreamProperty_StreamLatency
+ _kFigEndpointStreamType_Audio
+ _os_signpost_enabled
- _APAudioEngineBufferedAdapterCreate
- _APSAudioFormatDescriptionGetPCMASBD
- _APSAudioFormatDescriptionListCopyDebugString
- _APSAudioFormatDescriptionListCreateASRDArrayPCM
- _APSAudioFormatDescriptionListCreateSenderDefaultList
- _APSAudioFormatDescriptionListCreateWithFigEndpointStreamAudioFormatDescriptionArray
- _APSAudioFormatDescriptionListFindCompatibleTransportFromPCMAndSetDefault
- _APSAudioFormatDescriptionListGetDefaultFormat
- _APSAudioFormatDescriptionListGetFormatCount
- _FigSignalErrorAtGM
- _kAPEndpointStreamAudioEngineProperty_StartupOptions
- _kAPHALAudioDeviceCreationOption_AudioStreamOverride
- _kFigEndpointStreamProperty_SupportedAudioFormatDescriptions
- _kFigEndpointStreamProperty_SupportedPCMFormats
CStrings:
+ "### [%{ptr}] ESAE latency changed, retrying via OutputLatencyChanged notification\n"
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "APHALAudioControl.c"
+ "APHALAudioDevice.c"
+ "APHALAudioStream.c"
+ "Could not allocate APHALAudioSharedState"
+ "Could not allocate volumeContextRef"
+ "Created APHALAudioDevice [%{ptr}] type %@ for stream [%{ptr}]%?{end} and endpoint [%{ptr}]"
+ "Device was unplugged"
+ "EndpointStream has NULL ID"
+ "Error: %d"
+ "Expecting WriteMix operation"
+ "Failed to create notification queue"
+ "HAL Audio Device Start IO"
+ "HAL Audio Stream Start IO"
+ "HALStartIOResumeAudioEngineMs"
+ "HALStartIOSetEndpointStreamMs"
+ "HALStartIOTotalMs"
+ "NULL changeRecord"
+ "No AudioEngine"
+ "OSStatus device_GetPropertyData(FigHALAudioObjectRef, const AudioObjectPropertyAddress *, UInt32, const void *, UInt32, UInt32 *, void *)"
+ "OSStatus device_GetZeroTimeStampWithoutPresentationOffset(FigHALAudioDeviceRef, Float64 *, Float64 *, UInt64 *)"
+ "OSStatus device_copyEndpointAndEndpointStreamFromCreationParameters(CFAllocatorRef, FigEndpointRef, FigEndpointStreamRef, CFDictionaryRef, FigEndpointRef *, FigEndpointStreamRef *, CFStringRef *, CFDictionaryRef *, CFDictionaryRef *)"
+ "RTAE Resume"
+ "StreamLatency"
+ "UInt32 stream_GetStreamLatency(FigHALAudioStreamRef)"
+ "Unknown change action"
+ "[%{ptr}] AudioEngineType=%@"
+ "[%{ptr}] Changing isActive to %d"
+ "[%{ptr}] Copying property AudioEngineType from endpointStream [%{ptr}] failed. err=%#m"
+ "[%{ptr}] File writer [%{ptr}] created with error:%#m for APHALAudioStream."
+ "[%{ptr}] Forcing canBeDefaultSystemDevice from %s to %s"
+ "[%{ptr}] StartIO engineResume: %llu ms\n"
+ "[%{ptr}] StartIO setEndpointStream: %llu ms\n"
+ "[%{ptr}] StartIO total: %llu ms\n"
+ "[%{ptr}] StopIO engineSuspend: %llu ms\n"
+ "[%{ptr}] StopIO total: %llu ms\n"
+ "[%{ptr}] [%s] mSampleRate = %f. mFormatID = %C. newPCMFormatASBD: [%{asbd}]\n"
+ "[%{ptr}] [objectID %d] StartIO storage->isActive %d"
+ "[%{ptr}] converted output latency value=%lld timescale=%lld asbd.mSampleRate=%.0f to %lld samples"
+ "[%{ptr}] currentSampleHostTuple hostTime=%llu sampleTime=%.0f presentationSampleTime=%.0f (diff=%.0f) streamLatency=%llu outSamplePresentationTime=%.0f"
+ "[%{ptr}] failed to convert output latency value=%lld timescale=%lld asbd.mSampleRate=%.0f. Using %llu samples"
+ "[%{ptr}] halLatencyMs: %u\n"
+ "canBeDefaultSystemDevice"
+ "device_processStartIOMetrics"
+ "kAudioHardwareBadDeviceError"
+ "kAudioHardwareBadObjectError"
+ "kAudioHardwareIllegalOperationError"
+ "kAudioHardwareUnsupportedOperationError"
+ "kCMBaseObjectError_AllocationFailed"
+ "kFigEndpointStreamError_InvalidParameter"
+ "stream_GetPropertyData"
+ "stream_GetPropertyDataSize"
+ "stream_GetStreamLatency"
+ "stream_TTRBoundsCheckingForDoIO"
+ "stream_detectAndLogDoIODiscontinuity"
- " [%{ptr}] APHALAudioDevice executing without using default transport formats"
- "%s signalled err=%d at <>:%d"
- "Created APHALAudioDevice [%{ptr}] for stream [%{ptr}]%?{end} and endpoint [%{ptr}]"
- "Failed converting output latency. Using 0"
- "GetBestSupportedPCMASBDForSampleRate"
- "Initializing default output format [%{asbd}]"
- "OSStatus VerifyDefaultOutputFormat(APHALAudioStreamStorage *)"
- "OSStatus device_copyEndpointAndEndpointStreamFromCreationParameters(CFAllocatorRef, FigEndpointRef, FigEndpointStreamRef, CFDictionaryRef, FigEndpointRef *, FigEndpointStreamRef *, CFStringRef *, Boolean *, CFDictionaryRef *, CFDictionaryRef *)"
- "OSStatus stream_GetPropertyData(FigHALAudioObjectRef, const AudioObjectPropertyAddress *, UInt32, const void *, UInt32, UInt32 *, void *)"
- "Replacing Audio endpoint stream[%{ptr}] with BufferedAudio endpoint stream[%{ptr}]\n"
- "VerifyDefaultOutputFormat"
- "Verifying default output format [%{asbd}]"
- "[%s] mSampleRate = %f. mFormatID = %C. prevailingPCMASBD: [%{asbd}]\n"
- "[%s] prevailingTransportFormat: [%{asbd}]"
- "[%{ptr}] AudioDeviceType [%@]. SupportedPCMFormat[%d]: [%{asbd}]\n"
- "[%{ptr}] StartIO setEndpointStream: %1.3f ms\n"
- "[%{ptr}] StartIO total: %1.3f ms\n"
- "[%{ptr}] StopIO total: %1.3f ms\n"
- "[%{ptr}] storage->shared->prevailingTransportFormat not set as expected"
- "[%{ptr}] storage->shared->supportedTransportFormats not set as expected"
- "[%{ptr}] supportedTransportFormats=%@"
- "mediumLatencyPathway"

```
