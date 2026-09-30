## AirPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/AirPlayHalogen.driver/AirPlayHalogen`

```diff

-850.19.1.1.1
-  __TEXT.__text: 0xcfb0
-  __TEXT.__auth_stubs: 0x8b0
+860.3.1.0.0
+  __TEXT.__text: 0xd7e8
+  __TEXT.__auth_stubs: 0x900
   __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x28ad
-  __TEXT.__unwind_info: 0x2c0
-  __DATA_CONST.__auth_got: 0x458
+  __TEXT.__cstring: 0x2bca
+  __TEXT.__oslogstring: 0x6b
+  __TEXT.__unwind_info: 0x2e0
+  __DATA_CONST.__auth_got: 0x480
   __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__const: 0x7b0
   __DATA_CONST.__cfstring: 0x240
   __DATA.__data: 0x238
   __DATA.__bss: 0x100
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  Functions: 295
-  Symbols:   198
-  CStrings:  192
+  Functions: 296
+  Symbols:   203
+  CStrings:  220
 
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
+ "APHALHandoffAudioControl.c"
+ "APHALHandoffAudioDevice.c"
+ "APHALHandoffAudioStream.c"
+ "AirPlayHALPluginFactory %s: apPlugin_InstantiateAirPlayEndpointManager: APGetEndpointManager returned [%p]"
+ "Could not allocate APHALAudioSharedState"
+ "Could not allocate APHALHandoffAudioSharedState"
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
