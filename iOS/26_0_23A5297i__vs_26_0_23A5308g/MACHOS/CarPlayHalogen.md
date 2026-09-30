## CarPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen`

```diff

-890.73.1.11.1
-  __TEXT.__text: 0x7300
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x118b
-  __TEXT.__oslogstring: 0x93
+890.77.2.0.0
+  __TEXT.__text: 0x71ac
+  __TEXT.__auth_stubs: 0x530
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x1126
+  __TEXT.__oslogstring: 0x52
   __TEXT.__unwind_info: 0x1b0
-  __DATA_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__auth_got: 0x298
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__const: 0x2d0
   __DATA_CONST.__cfstring: 0x60
   __DATA.__data: 0xe0
-  __DATA.__common: 0x20
+  __DATA.__common: 0x10
   __DATA.__bss: 0x8c
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  UUID: 2D5F8B27-116A-3C9D-8D79-579B7968307A
+  UUID: 4CD9DBEF-AB76-3991-806E-DABA317CA74C
   Functions: 141
-  Symbols:   129
-  CStrings:  106
+  Symbols:   125
+  CStrings:  102
 
Symbols:
+ _FigSignalErrorAtGM
- _FigSignalErrorAt3
- __os_log_send_and_compose_impl
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _os_log_type_enabled
Functions:
~ sub_665c : 424 -> 384
~ sub_6874 -> sub_684c : 392 -> 92
CStrings:
+ "%s signalled err=%d at <>:%d"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "APHALCarAudioStream.c"
- "CarPlayHALPluginFactory %s: CarPlayEndpointManagerCarPlay = [%p]"
- "Unknown config change action"
- "kAudioHardwareIllegalOperationError"

```
