## AirPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/AirPlayHalogen.driver/AirPlayHalogen`

```diff

-950.7.1.0.0
-  __TEXT.__text: 0xdb88 sha256:c37ebc481f83f2219f5a78477698c628bcf541a775758ef4a9800dc1d06bf1fa
-  __TEXT.__auth_stubs: 0x8e0 sha256:e358ee27ac29e74fb2fcbb8ff6141ff9f953053f085fa1e05af9bdb6ea0dfb98
-  __TEXT.__const: 0xbc sha256:4df1b6adca28c2c39851dc9456e6f503537a523d71a6eb8caae2c189956530ec
-  __TEXT.__cstring: 0x2ee2 sha256:4353bbf10ffa27034b6361a72e0e28f40e9cdf729180b9357c1b3da6ee067fdf
-  __TEXT.__unwind_info: 0x2e8 sha256:e99b8b40cf2bf13cdfc643e15db05ed06ff979ce059ea7abe69fa4978feddc69
-  __DATA_CONST.__auth_got: 0x470 sha256:86de2f0b4d923ccc137a61e69f4abe4dca197d00c25c735748607d25f9461317
-  __DATA_CONST.__got: 0x1c8 sha256:98ba975b5bfce2017804a4aa77d1a948ccbb79cf19860d1463aed6cb18b0d7f8
-  __DATA_CONST.__const: 0x7b0 sha256:e909af94a096ce71b1d9e208b91df4b8b798719f1dba9a8ade2210182bec89a4
-  __DATA_CONST.__cfstring: 0x2a0 sha256:81c87514eeecea0369c5aaa676da5a590b4169fdccc9211a93c08f3f68fd8f88
-  __DATA.__data: 0x238 sha256:aeaa473882977f96e4e27695fde6ae54b4390e82c8ddb675e1aefbc2b77fc4e5
+980.58.1.11.1
+  __TEXT.__text: 0xec6c sha256:4769e28da3220fc9fe74c460bf8a9fdef21b0446c14d9ecd0178bd292abf0ea7
+  __TEXT.__auth_stubs: 0x970 sha256:adbe7c99cd845f027c241560759670d508ca078d77a9e625d50acc2e94de598b
+  __TEXT.__const: 0xcc sha256:91b546dbd478bba6581c99502627260f1b77fce5108d6d6519a4d1edd7d5de82
+  __TEXT.__cstring: 0x3450 sha256:69d9df65036a6c57b8f1da774a6ff5de23cf580b124f863056f8e9692750722e
+  __TEXT.__oslogstring: 0xb6 sha256:d7fdc6a19737cdc4e9619526b5465763be7e2b34f17d95d46a0486a858169b35
+  __TEXT.__unwind_info: 0x318 sha256:1712dd8ed79cb1ca07ccd835a14afc01c0f41b5c37bc3797170fbe4426e95fcc
+  __DATA_CONST.__const: 0x7b8 sha256:a109fb9ed307134cbb260c7750d7ecd45a818abd3ba252fb22ae4b953347b7e4
+  __DATA_CONST.__cfstring: 0x320 sha256:bbdbcad4ae05fdc41f1620e57e663bd831bbbc58072d96939c1786fb060e973a
+  __DATA_CONST.__auth_got: 0x4b8 sha256:44d0b04e022f0e2fc4a62c9874196dcbffee0eebc950eb0c07923e63ef10a5eb
+  __DATA_CONST.__got: 0x1e0 sha256:63c177e66ae15064e275814c86a37392f4647a097bc6bcb9b6d1b4d2fa864d3b
+  __DATA.__data: 0x238 sha256:f661290da6ea1d2a457e22bb73ba276a3571edb6bb867170256cddee3694c6dd
   __DATA.__bss: 0x100 sha256:5341e6b2646979a70e57653007a1f310169421ec9bdd9f1a5648f75ade005af1
+  __DATA.__common: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  UUID: 86251763-CDE5-3627-85BA-A9DBD6785400
-  Functions: 323
-  Symbols:   205
-  CStrings:  244
+  UUID: 25F4142E-CFBF-33C2-B0B3-945B0290CBDF
+  Functions: 319
+  Symbols:   218
+  CStrings:  290
 
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
+ __os_log_send_and_compose_impl
+ __os_signpost_emit_with_name_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _kAPAudioEngineResumeOption_HALLatencyMs
+ _kAPAudioFormatSelectorCreationOption_UsingP2P
+ _kAPEndpointStreamAudioEngineType_Buffered
+ _kAPEndpointStreamBufferedAudioEngineProperty_HALStartIOMetrics
+ _kAPEndpointStreamProperty_AudioEngineType
+ _kAPHALAudioDeviceCreationOption_IsP2PConnection
+ _kAPHALAudioStreamProperty_StreamLatency
+ _kFigEndpointStreamType_Audio
+ _os_log_type_enabled
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
+ "APHALHandoffAudioControl.c"
+ "APHALHandoffAudioDevice.c"
+ "APHALHandoffAudioStream.c"
+ "AirPlayHALPluginFactory %s: apPlugin_InstantiateAirPlayEndpointManager: APGetEndpointManager returned [%p]"
+ "Could not allocate APHALAudioSharedState"
+ "Could not allocate APHALHandoffAudioSharedState"
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
+ "Need at least one supported PCM format from endpointStream"
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
+ "kCMBaseObjectError_ParamErr"
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
