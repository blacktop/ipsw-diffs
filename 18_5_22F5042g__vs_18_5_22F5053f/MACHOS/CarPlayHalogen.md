## CarPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen`

```diff

-860.3.1.0.0
-  __TEXT.__text: 0x726c
-  __TEXT.__auth_stubs: 0x560
-  __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x118b
-  __TEXT.__oslogstring: 0x93
+860.5.2.0.0
+  __TEXT.__text: 0x7110
+  __TEXT.__auth_stubs: 0x520
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x1103
+  __TEXT.__oslogstring: 0x52
   __TEXT.__unwind_info: 0x188
-  __DATA_CONST.__auth_got: 0x2b0
+  __DATA_CONST.__auth_got: 0x290
   __DATA_CONST.__got: 0x110
   __DATA_CONST.__const: 0x2d0
   __DATA_CONST.__cfstring: 0x60
   __DATA.__data: 0xe0
-  __DATA.__common: 0x20
+  __DATA.__common: 0x10
   __DATA.__bss: 0x8c
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   Functions: 141
-  Symbols:   127
-  CStrings:  103
+  Symbols:   123
+  CStrings:  97
 
Symbols:
+ _FigSignalErrorAt
- _FigSignalErrorAt3
- __os_log_send_and_compose_impl
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _os_log_type_enabled
CStrings:
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "(Fig)"
- "APHALCarAudioStream.c"
- "CarPlayHALPluginFactory %s: CarPlayEndpointManagerCarPlay = [%p]"
- "Unknown config change action"
- "kAudioHardwareIllegalOperationError"

```
