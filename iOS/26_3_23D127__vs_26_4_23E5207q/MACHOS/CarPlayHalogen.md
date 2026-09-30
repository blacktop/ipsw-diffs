## CarPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen`

```diff

-935.7.1.0.0
-  __TEXT.__text: 0x71a8
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x1126
-  __TEXT.__oslogstring: 0x52
+940.19.1.0.0
+  __TEXT.__text: 0x6f68
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
-  UUID: 61D2C691-E80D-3682-986B-DEE17D5BE63C
-  Functions: 142
-  Symbols:   125
-  CStrings:  102
+  UUID: 9479213F-6039-3CC5-9C88-EA22AC585A04
+  Functions: 148
+  Symbols:   129
+  CStrings:  106
 
Symbols:
+ _FigSignalErrorAt3
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _os_log_type_enabled
- _FigSignalErrorAtGM
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "APHALCarAudioStream.c"
+ "CarPlayHALPluginFactory %s: CarPlayEndpointManagerCarPlay = [%p]"
+ "Unknown config change action"
+ "kAudioHardwareIllegalOperationError"
- "%s signalled err=%d at <>:%d"

```
