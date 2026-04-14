## AirPlayHalogen

> `filesystem/System/Library/Audio/Plug-Ins/HAL/AirPlayHalogen.driver/AirPlayHalogen`

```diff

-950.2.1.0.0
-  __TEXT.__text: 0xe0d8
-  __TEXT.__auth_stubs: 0x920
+950.5.2.0.0
+  __TEXT.__text: 0xdb88
+  __TEXT.__auth_stubs: 0x8e0
   __TEXT.__const: 0xbc
-  __TEXT.__cstring: 0x3207
-  __TEXT.__oslogstring: 0x6b
-  __TEXT.__unwind_info: 0x308
-  __DATA_CONST.__auth_got: 0x490
+  __TEXT.__cstring: 0x2ee2
+  __TEXT.__unwind_info: 0x2e8
+  __DATA_CONST.__auth_got: 0x470
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__const: 0x7b0
   __DATA_CONST.__cfstring: 0x2a0
   __DATA.__data: 0x238
   __DATA.__bss: 0x100
-  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  UUID: 149B5A8E-10D4-3B5F-8487-6B57C562B718
-  Functions: 329
-  Symbols:   209
-  CStrings:  270
+  UUID: 0312480E-1994-321F-BFE4-AEDFD8E11CBE
+  Functions: 323
+  Symbols:   205
+  CStrings:  244
 
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
