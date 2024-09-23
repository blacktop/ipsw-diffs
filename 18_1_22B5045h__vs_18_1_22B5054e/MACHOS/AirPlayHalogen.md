## AirPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/AirPlayHalogen.driver/AirPlayHalogen`

```diff

-830.6.1.0.0
-  __TEXT.__text: 0xcce0
-  __TEXT.__auth_stubs: 0x910
+830.8.4.0.0
+  __TEXT.__text: 0xc594
+  __TEXT.__auth_stubs: 0x8c0
   __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x2d37
-  __TEXT.__oslogstring: 0x6b
-  __TEXT.__unwind_info: 0x208
-  __DATA_CONST.__auth_got: 0x488
+  __TEXT.__cstring: 0x2a1a
+  __TEXT.__unwind_info: 0x200
+  __DATA_CONST.__auth_got: 0x460
   __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__const: 0x7b0
   __DATA_CONST.__cfstring: 0x280
   __DATA.__data: 0x238
   __DATA.__bss: 0x100
-  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   Functions: 131
-  Symbols:   205
-  CStrings:  228
+  Symbols:   200
+  CStrings:  200
 
Symbols:
+ _FigSignalErrorAt
- _fig_log_get_emitter
- __os_log_send_and_compose_impl
- _FigSignalErrorAt3
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _os_log_type_enabled
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
CStrings:
- "APHALHandoffAudioStream.c"
- "No AudioEngine"
- "APHALAudioControl.c"
- "com.apple.coremedia"
- "kAudioHardwareUnsupportedOperationError"
- "Could not allocate APHALHandoffAudioSharedState"
- "Could not allocate volumeContextRef"
- "APHALAudioStream.c"
- "kFigEndpointStreamError_InvalidParameter"
- "Unknown change action"
- "EndpointStream has NULL ID"
- "(Fig)"
- "NULL changeRecord"
- "AirPlayHALPluginFactory %!s(MISSING): apPlugin_InstantiateAirPlayEndpointManager: APGetEndpointManager returned [%!p(MISSING)]"
- "Could not allocate APHALAudioSharedState"
- "kCMBaseObjectError_AllocationFailed"
- "Need at least one supported PCM format from endpointStream"
- "kAudioHardwareIllegalOperationError"
- "kCMBaseObjectError_ParamErr"
- "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
- "APHALAudioDevice.c"
- "Device was unplugged"
- "APHALHandoffAudioControl.c"
- "APHALHandoffAudioDevice.c"
- "Failed to create notification queue"
- "kAudioHardwareBadDeviceError"
- "Expecting WriteMix operation"
- "kAudioHardwareBadObjectError"

```
