## CarPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen`

```diff

-860.7.1.0.0
-  __TEXT.__text: 0x7110
-  __TEXT.__auth_stubs: 0x520
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x1103
-  __TEXT.__oslogstring: 0x52
+890.61.4.11.2
+  __TEXT.__text: 0x7270
+  __TEXT.__auth_stubs: 0x560
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x118b
+  __TEXT.__oslogstring: 0x93
   __TEXT.__unwind_info: 0x188
-  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__auth_got: 0x2b0
   __DATA_CONST.__got: 0x110
   __DATA_CONST.__const: 0x2d0
   __DATA_CONST.__cfstring: 0x60
   __DATA.__data: 0xe0
-  __DATA.__common: 0x10
+  __DATA.__common: 0x20
   __DATA.__bss: 0x8c
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  UUID: DE2D5CF4-7DC9-3891-8B55-C9261C6A9216
+  UUID: 62973A78-BCD1-3D23-9631-6A38BBACDAA2
   Functions: 141
-  Symbols:   123
-  CStrings:  100
+  Symbols:   127
+  CStrings:  106
 
Symbols:
+ _FigSignalErrorAt3
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _os_log_type_enabled
- _FigSignalErrorAt
Functions:
~ sub_1e90 : 2704 -> 2708
~ sub_5864 -> sub_5868 : 376 -> 424
~ sub_6028 -> sub_605c : 92 -> 392
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "(Fig)"
+ "APHALCarAudioStream.c"
+ "CarPlayHALPluginFactory %s: CarPlayEndpointManagerCarPlay = [%p]"
+ "Unknown config change action"
+ "kAudioHardwareIllegalOperationError"

```
