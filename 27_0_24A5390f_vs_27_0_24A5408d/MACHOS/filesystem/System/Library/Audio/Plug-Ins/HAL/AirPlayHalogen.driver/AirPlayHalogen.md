## AirPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/AirPlayHalogen.driver/AirPlayHalogen`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-980.71.1.0.0
-  __TEXT.__text: 0xecd0
-  __TEXT.__auth_stubs: 0x970
+980.75.1.0.0
+  __TEXT.__text: 0xe7fc
+  __TEXT.__auth_stubs: 0x930
   __TEXT.__const: 0xcc
-  __TEXT.__cstring: 0x3468
-  __TEXT.__oslogstring: 0xb6
-  __TEXT.__unwind_info: 0x320
+  __TEXT.__cstring: 0x3182
+  __TEXT.__oslogstring: 0x4b
+  __TEXT.__unwind_info: 0x308
   __DATA_CONST.__const: 0x7b8
   __DATA_CONST.__cfstring: 0x320
-  __DATA_CONST.__auth_got: 0x4b8
+  __DATA_CONST.__auth_got: 0x498
   __DATA_CONST.__got: 0x1e0
   __DATA.__data: 0x238
   __DATA.__bss: 0x100
-  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  Functions: 320
-  Symbols:   218
-  CStrings:  266
+  Functions: 316
+  Symbols:   214
+  CStrings:  241
 
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
- "APHALHandoffAudioControl.c"
- "APHALHandoffAudioDevice.c"
- "APHALHandoffAudioStream.c"
- "AirPlayHALPluginFactory %s: apPlugin_InstantiateAirPlayEndpointManager: APGetEndpointManager returned [%p]"
- "Could not allocate APHALAudioSharedState"
- "Could not allocate APHALHandoffAudioSharedState"
- "Could not allocate volumeContextRef"
- "Device was unplugged"
- "EndpointStream has NULL ID"
- "Expecting WriteMix operation"
- "Failed to create notification queue"
- "NULL changeRecord"
- "Need at least one supported PCM format from endpointStream"
- "No AudioEngine"
- "Unknown change action"
- "kAudioHardwareBadDeviceError"
- "kAudioHardwareBadObjectError"
- "kAudioHardwareIllegalOperationError"
- "kAudioHardwareUnsupportedOperationError"
- "kCMBaseObjectError_AllocationFailed"
- "kCMBaseObjectError_ParamErr"
- "kFigEndpointStreamError_InvalidParameter"
```
