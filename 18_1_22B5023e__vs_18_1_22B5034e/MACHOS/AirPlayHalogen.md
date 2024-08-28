## AirPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/AirPlayHalogen.driver/AirPlayHalogen`

```diff

-830.2.0.0.0
-  __TEXT.__text: 0xc354
-  __TEXT.__auth_stubs: 0x8b0
+830.4.1.0.0
+  __TEXT.__text: 0xcce0
+  __TEXT.__auth_stubs: 0x910
   __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x28ad
-  __TEXT.__unwind_info: 0x200
-  __DATA_CONST.__auth_got: 0x458
-  __DATA_CONST.__got: 0x1a8
+  __TEXT.__cstring: 0x2d37
+  __TEXT.__oslogstring: 0x6b
+  __TEXT.__unwind_info: 0x208
+  __DATA_CONST.__auth_got: 0x488
+  __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__const: 0x7b0
-  __DATA_CONST.__cfstring: 0x240
+  __DATA_CONST.__cfstring: 0x280
   __DATA.__data: 0x238
   __DATA.__bss: 0x100
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  Functions: 130
-  Symbols:   198
-  CStrings:  192
+  Functions: 131
+  Symbols:   205
+  CStrings:  228
 
Symbols:
+ _FigSignalErrorAt3
+ _os_log_type_enabled
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_log_get_emitter
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _kAPSRadarLoggingComponent_AirPlayNewBugs
+ _APSTapToRadarInvoke
- _FigSignalErrorAt
CStrings:
+ "bad"
+ "kAudioHardwareBadDeviceError"
+ "sampleRate=%!u(MISSING)[%!s(MISSING)] bytesPerFrame=%!u(MISSING)[%!s(MISSING)] ioBufferFrameSize=%!u(MISSING)[%!s(MISSING)] framesToDrop=%!u(MISSING)[%!s(MISSING)] bytesToDrop=%!l(MISSING)lu length=%!l(MISSING)lu"
+ "Need at least one supported PCM format from endpointStream"
+ "APHALHandoffAudioControl.c"
+ "EndpointStream has NULL ID"
+ "void stream_ttrLogger(const APSAsyncLoggerParameters *, Float64)"
+ "Unknown change action"
+ "kAudioHardwareUnsupportedOperationError"
+ "NULL changeRecord"
+ "TTR: Streaming Audio DoIO Bounds Checking Violation"
+ "Failed to create notification queue"
+ "AirPlayHALPluginFactory %!s(MISSING): apPlugin_InstantiateAirPlayEndpointManager: APGetEndpointManager returned [%!p(MISSING)]"
+ "Could not allocate APHALHandoffAudioSharedState"
+ "APHALHandoffAudioDevice.c"
+ "stream_ttrLogger"
+ "kFigEndpointStreamError_InvalidParameter"
+ "Device was unplugged"
+ "(Fig)"
+ "APHALAudioControl.c"
+ "Could not allocate APHALAudioSharedState"
+ "com.apple.coremedia"
+ "APHALAudioStream.c"
+ "APHALHandoffAudioStream.c"
+ "Could not allocate volumeContextRef"
+ "kCMBaseObjectError_ParamErr"
+ "No AudioEngine"
+ "Streaming Audio DoIO Bounds Checking Violation: %!@(MISSING) (log latency: %!f(MISSING) ms)\n"
+ "kAudioHardwareBadObjectError"
+ "APHALAudioDevice.c"
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
+ "kAudioHardwareIllegalOperationError"
+ "kCMBaseObjectError_AllocationFailed"
+ "good"
+ "Streaming Audio Bounds Violation"
+ "Expecting WriteMix operation"

```
