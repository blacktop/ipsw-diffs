## AirPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/AirPlayHalogen.driver/AirPlayHalogen`

```diff

-890.73.1.11.1
-  __TEXT.__text: 0xe500
-  __TEXT.__auth_stubs: 0x920
+890.77.2.0.0
+  __TEXT.__text: 0xe1a4
+  __TEXT.__auth_stubs: 0x8e0
   __TEXT.__const: 0xbc
-  __TEXT.__cstring: 0x3121
-  __TEXT.__oslogstring: 0x6b
-  __TEXT.__unwind_info: 0x300
-  __DATA_CONST.__auth_got: 0x490
+  __TEXT.__cstring: 0x2ee2
+  __TEXT.__unwind_info: 0x2f0
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
-  UUID: E82C3288-3E8B-3010-A424-7F1F73CF6B96
-  Functions: 312
-  Symbols:   209
-  CStrings:  266
+  UUID: 8B9701B6-F35F-38E7-9EE8-8167AAD3816A
+  Functions: 313
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
+ "Created APHALAudioDevice [%{ptr}] for stream [%{ptr}]%?{end} and endpoint [%{ptr}]"
+ "[%{ptr}] APHALAudioDevice Finalized\n"
+ "[%{ptr}] Created APHALAudioStream [%{ptr}]\n"
+ "[%{ptr}] Releasing APHALAudioStream [%{ptr}]\n"
+ "[%{ptr}] StopIO total: %1.3f ms\n"
+ "void device_Finalize(CMBaseObjectRef)"
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
- "Created APHALAudioDevice [%{ptr}]"
- "Device was unplugged"
- "EndpointStream has NULL ID"
- "Expecting WriteMix operation"
- "Failed to create notification queue"
- "NULL changeRecord"
- "Need at least one supported PCM format from endpointStream"
- "No AudioEngine"
- "No compatible transport format exists for selected PCM format."
- "Unknown change action"
- "[%{ptr}] StopIO\n"
- "kAudioHardwareBadDeviceError"
- "kAudioHardwareBadObjectError"
- "kAudioHardwareIllegalOperationError"
- "kAudioHardwareUnsupportedOperationError"
- "kCMBaseObjectError_AllocationFailed"
- "kCMBaseObjectError_ParamErr"
- "kFigEndpointStreamError_InvalidParameter"

```
