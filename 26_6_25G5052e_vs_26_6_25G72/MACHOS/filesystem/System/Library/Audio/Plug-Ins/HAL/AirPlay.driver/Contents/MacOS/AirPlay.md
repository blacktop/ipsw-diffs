## AirPlay

> `/System/Library/Audio/Plug-Ins/HAL/AirPlay.driver/Contents/MacOS/AirPlay`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-960.10.1.0.0
-  __TEXT.__text: 0xa40c
-  __TEXT.__auth_stubs: 0x930
+960.13.1.0.0
+  __TEXT.__text: 0xa02c
+  __TEXT.__auth_stubs: 0x8f0
   __TEXT.__const: 0xa4
-  __TEXT.__cstring: 0x2a64
-  __TEXT.__oslogstring: 0x6b
-  __TEXT.__unwind_info: 0x228
-  __DATA_CONST.__auth_got: 0x498
+  __TEXT.__cstring: 0x27be
+  __TEXT.__unwind_info: 0x218
+  __DATA_CONST.__auth_got: 0x478
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__const: 0x3e0
   __DATA_CONST.__cfstring: 0x220
   __DATA.__data: 0x158
-  __DATA.__common: 0x10
   __DATA.__bss: 0x90
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/Versions/A/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  Functions: 236
-  Symbols:   210
-  CStrings:  208
+  Functions: 232
+  Symbols:   206
+  CStrings:  186
 
Symbols:
+ _FigSignalErrorAtGM
- _FigSignalErrorAt3
- __os_log_send_and_compose_impl
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _os_log_type_enabled
CStrings:
+ "%s signalled err=%d at <>:%d"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "APHALAudioControl.c"
- "APHALAudioDevice.c"
- "APHALAudioStream.c"
- "AirPlayHALPluginFactory %s: apPlugin_InstantiateAirPlayEndpointManager: APGetEndpointManager returned [%p]"
- "Could not allocate APHALAudioSharedState"
- "Could not allocate volumeContextRef"
- "Device was unplugged"
- "EndpointStream has NULL ID"
- "Expecting WriteMix operation"
- "Failed to create notification queue"
- "NULL changeRecord"
- "Need at least one supported PCM format from endpointStream"
- "No AudioEngine"
- "No compatible transport format exists for selected PCM format."
- "Unknown change action"
- "kAudioHardwareBadDeviceError"
- "kAudioHardwareBadObjectError"
- "kAudioHardwareIllegalOperationError"
- "kAudioHardwareUnsupportedOperationError"
- "kCMBaseObjectError_AllocationFailed"
- "kCMBaseObjectError_ParamErr"
- "kFigEndpointStreamError_InvalidParameter"
```
