## AirPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/AirPlayHalogen.driver/AirPlayHalogen`

```diff

-870.10.1.0.0
-  __TEXT.__text: 0xd7e8
-  __TEXT.__auth_stubs: 0x900
+870.12.2.0.0
+  __TEXT.__text: 0xcfb0
+  __TEXT.__auth_stubs: 0x8b0
   __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x2bca
-  __TEXT.__oslogstring: 0x6b
-  __TEXT.__unwind_info: 0x2e0
-  __DATA_CONST.__auth_got: 0x480
+  __TEXT.__cstring: 0x28ad
+  __TEXT.__unwind_info: 0x2c0
+  __DATA_CONST.__auth_got: 0x458
   __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__const: 0x7b0
   __DATA_CONST.__cfstring: 0x240
   __DATA.__data: 0x238
   __DATA.__bss: 0x100
-  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  UUID: 43C9DE43-4455-341B-A94F-05DA8DF2F32B
-  Functions: 296
-  Symbols:   203
-  CStrings:  238
+  UUID: B3DC8032-ED0A-3D04-BF85-1C363DA4DBCA
+  Functions: 295
+  Symbols:   198
+  CStrings:  210
 
Symbols:
+ _FigSignalErrorAt
- _FigSignalErrorAt3
- __os_log_send_and_compose_impl
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _fig_log_get_emitter
- _os_log_type_enabled
Functions (added):
+ sub_1ec8
+ sub_24b4
+ sub_2ec4
+ sub_4014
+ sub_5178
+ sub_51c0
+ sub_51ec
+ sub_9ad8
+ sub_b830
+ sub_ba20
+ sub_bb10
+ sub_bd2c
+ sub_bed0
+ sub_c120
+ sub_c1c4
+ sub_c2bc
+ sub_c418
+ sub_c47c
+ sub_c810
+ sub_cd38
+ sub_d020
+ sub_d3a4
+ sub_d63c
+ sub_d7a8

Functions (removed):
- sub_25c0
- sub_4140
- sub_440c
- sub_5338
- sub_67e0
- sub_7a90
- sub_80b4
- sub_9d58
- sub_bad4
- sub_bd24
- sub_be74
- sub_c0f0
- sub_c27c
- sub_c590
- sub_c68c
- sub_c7dc
- sub_ca00
- sub_cdec
- sub_d354
- sub_d6f4
- sub_d7d8
- sub_dad4
- sub_db78
- sub_de6c
- sub_e02c
CStrings:
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "(Fig)"
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
- "com.apple.coremedia"
- "kAudioHardwareBadDeviceError"
- "kAudioHardwareBadObjectError"
- "kAudioHardwareIllegalOperationError"
- "kAudioHardwareUnsupportedOperationError"
- "kCMBaseObjectError_AllocationFailed"
- "kCMBaseObjectError_ParamErr"
- "kFigEndpointStreamError_InvalidParameter"

```
