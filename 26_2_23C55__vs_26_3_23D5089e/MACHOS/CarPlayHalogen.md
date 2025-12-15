## CarPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen`

```diff

-925.5.1.1.0
-  __TEXT.__text: 0x71a8
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x1126
-  __TEXT.__oslogstring: 0x52
+935.3.1.0.0
+  __TEXT.__text: 0x72fc
+  __TEXT.__auth_stubs: 0x570
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x118b
+  __TEXT.__oslogstring: 0x93
   __TEXT.__unwind_info: 0x1b0
-  __DATA_CONST.__auth_got: 0x298
+  __DATA_CONST.__auth_got: 0x2b8
   __DATA_CONST.__got: 0x118
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
-  UUID: E4FA8A8F-9583-3373-99DA-41FF45A592B5
+  UUID: C5A2F5FA-957C-382A-91FF-0CD5EF29CAA5
   Functions: 142
-  Symbols:   125
-  CStrings:  102
+  Symbols:   129
+  CStrings:  106
 
Symbols:
+ _FigSignalErrorAt3
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _os_log_type_enabled
- _FigSignalErrorAtGM
Functions:
~ sub_6658 : 384 -> 424
~ sub_6848 -> sub_6870 : 92 -> 392
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "APHALCarAudioStream.c"
+ "CarPlayHALPluginFactory %s: CarPlayEndpointManagerCarPlay = [%p]"
+ "Unknown config change action"
+ "kAudioHardwareIllegalOperationError"
- "%s signalled err=%d at <>:%d"

```
