## AVCHalogen

> `/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/AVCHalogen`

```diff

-950.7.1.0.0
-  __TEXT.__text: 0x9e40 sha256:e0979ccab1008f3af18d0e4a4653a4a28c50f06cb06f8c361d9740ad421735f0
-  __TEXT.__auth_stubs: 0x870 sha256:b4cee46381acda66361e21702320c7cd8f9061b4f02122e4603b354d03502812
-  __TEXT.__cstring: 0x25df sha256:89395433e0506dcff4fdb55d8707c36e91bbde7f60cbafa819542f45d5d58177
-  __TEXT.__const: 0xa0 sha256:08cf867d8030e59aeec8a03823c3663cf7cbd5570225a15a7c70ac851ef95987
-  __TEXT.__unwind_info: 0x210 sha256:3b4bfb0ea9c226fba6517a1e98e53aea5d9dccfb3e1f8f53b3fe3ffa1165e450
-  __DATA_CONST.__auth_got: 0x438 sha256:6bd437b91bab8d6fb1fef7e9e68f49aaef5bda3ae61eb14eb092d6297f4e9859
-  __DATA_CONST.__got: 0x1c8 sha256:4e46cfae42a8c6cab52fc5ebd65557160cccaab7a48003ffc427fe79d869e84d
-  __DATA_CONST.__const: 0x3e0 sha256:7676a2164839080593d7c4d637277311cc0fcb5c7ad242d7995b66f6251fb04d
-  __DATA_CONST.__cfstring: 0x220 sha256:c6ef7399d3e28c927572c84d36e711a794e93c011bbe04de30444833968fab65
-  __DATA.__data: 0x1c0 sha256:538eaa6a6eedd73193b58e24a1a6111a2e2c299e5e20a992ee485ced66475f2e
+980.58.1.11.1
+  __TEXT.__text: 0xac60 sha256:d33260546dd17909172c16e8f9e389c68c97a285e989d861b926a21739f458e9
+  __TEXT.__auth_stubs: 0x8c0 sha256:8705c100e596d888b0d83af736736f197ecc0a5a29f9b743ced7e97c474f62ed
+  __TEXT.__cstring: 0x2a52 sha256:f582ebb7af8ea5fab5cdafdb36223c18a4a8e6440f11e1b6f1ba7e0d9228cec0
+  __TEXT.__const: 0xb0 sha256:f809c0a3ea62bb2becd7de04aca33c448fac75a8d6a519b9970e38c7b5fee4b6
+  __TEXT.__oslogstring: 0x4b sha256:14b44e6a8a1c600f49ecb615b648bcbb87f09e96aceb1cc5b8a8895532b75978
+  __TEXT.__unwind_info: 0x228 sha256:948626bd93fb7f2831c68346b7cae4686642851b09002687775b57faae45d864
+  __DATA_CONST.__const: 0x3e8 sha256:439d5acb550a2253d35f67a2ca8736cdc4394d9793aecdf07f438496b2f768e3
+  __DATA_CONST.__cfstring: 0x2a0 sha256:3b80965a5d0f10c716871c19363020cfecdb3ae2776022d060c5e10648f29ee6
+  __DATA_CONST.__auth_got: 0x460 sha256:3a2aa22f649953d251f875480679135e5ba56689431618248bb253bb77fe04a4
+  __DATA_CONST.__got: 0x1e0 sha256:48fe5492238810f117996e08cdd7756d3310274108febd6829b0da5ac9df9ef4
+  __DATA.__data: 0x1c0 sha256:0a3cbe3a6f17b43f310b1cbd1bd48b63418ac86653cb8268692f1ef4917601d5
   __DATA.__bss: 0x90 sha256:81c611f35bff79491538b2f7cf201c7597a661a5c549633541c62bdc8af1613f
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

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
