## AirPlay

> `/System/Library/Audio/Plug-Ins/HAL/AirPlay.driver/Contents/MacOS/AirPlay`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-980.71.1.0.0
-  __TEXT.__text: 0xaf8c
-  __TEXT.__auth_stubs: 0x980
+980.77.5.3.0
+  __TEXT.__text: 0xac28
+  __TEXT.__auth_stubs: 0x940
   __TEXT.__const: 0xb4
-  __TEXT.__cstring: 0x2c49
-  __TEXT.__oslogstring: 0xb6
-  __TEXT.__unwind_info: 0x240
+  __TEXT.__cstring: 0x2a39
+  __TEXT.__oslogstring: 0x4b
+  __TEXT.__unwind_info: 0x230
   __DATA_CONST.__const: 0x3e8
   __DATA_CONST.__cfstring: 0x2a0
-  __DATA_CONST.__auth_got: 0x4c0
+  __DATA_CONST.__auth_got: 0x4a0
   __DATA_CONST.__got: 0x1e0
   __DATA.__data: 0x158
-  __DATA.__common: 0x10
   __DATA.__bss: 0x90
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/Versions/A/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  Functions: 228
-  Symbols:   219
-  CStrings:  222
+  Functions: 226
+  Symbols:   215
+  CStrings:  203
 
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
- "No AudioEngine"
- "Unknown change action"
- "kAudioHardwareBadDeviceError"
- "kAudioHardwareBadObjectError"
- "kAudioHardwareIllegalOperationError"
- "kAudioHardwareUnsupportedOperationError"
- "kCMBaseObjectError_AllocationFailed"
- "kFigEndpointStreamError_InvalidParameter"
```
