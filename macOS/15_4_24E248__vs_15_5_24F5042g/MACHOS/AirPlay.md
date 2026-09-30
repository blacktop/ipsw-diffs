## AirPlay

> `/System/Library/Audio/Plug-Ins/HAL/AirPlay.driver/Contents/MacOS/AirPlay`

```diff

-850.19.1.0.0
-  __TEXT.__text: 0x93c8
-  __TEXT.__auth_stubs: 0x8c0
+860.3.1.0.0
+  __TEXT.__text: 0x998c
+  __TEXT.__auth_stubs: 0x910
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x21a7
-  __TEXT.__unwind_info: 0x1e8
-  __DATA_CONST.__auth_got: 0x460
+  __TEXT.__cstring: 0x2445
+  __TEXT.__oslogstring: 0x6b
+  __TEXT.__unwind_info: 0x1f8
+  __DATA_CONST.__auth_got: 0x488
   __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__const: 0x3e0
   __DATA_CONST.__cfstring: 0x1c0
   __DATA.__data: 0x158
+  __DATA.__common: 0x10
   __DATA.__bss: 0x90
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/Versions/A/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  Functions: 207
-  Symbols:   199
-  CStrings:  156
+  Functions: 208
+  Symbols:   204
+  CStrings:  180
 
Symbols:
+ _FigSignalErrorAt3
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_log_get_emitter
+ _os_log_type_enabled
- _FigSignalErrorAt
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "(Fig)"
+ "APHALAudioControl.c"
+ "APHALAudioDevice.c"
+ "APHALAudioStream.c"
+ "AirPlayHALPluginFactory %s: apPlugin_InstantiateAirPlayEndpointManager: APGetEndpointManager returned [%p]"
+ "Could not allocate APHALAudioSharedState"
+ "Could not allocate volumeContextRef"
+ "Device was unplugged"
+ "EndpointStream has NULL ID"
+ "Expecting WriteMix operation"
+ "Failed to create notification queue"
+ "NULL changeRecord"
+ "Need at least one supported PCM format from endpointStream"
+ "No AudioEngine"
+ "Unknown change action"
+ "com.apple.coremedia"
+ "kAudioHardwareBadDeviceError"
+ "kAudioHardwareBadObjectError"
+ "kAudioHardwareIllegalOperationError"
+ "kAudioHardwareUnsupportedOperationError"
+ "kCMBaseObjectError_AllocationFailed"
+ "kCMBaseObjectError_ParamErr"
+ "kFigEndpointStreamError_InvalidParameter"

```
