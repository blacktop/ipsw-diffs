## CarPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen`

```diff

-940.23.1.0.0
-  __TEXT.__text: 0x72dc
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x1361
-  __TEXT.__oslogstring: 0x52
+950.2.1.0.0
+  __TEXT.__text: 0x7430
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x13c6
+  __TEXT.__oslogstring: 0x93
   __TEXT.__unwind_info: 0x1a8
-  __DATA_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__auth_got: 0x2d8
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
-  UUID: FE5FCF87-D32E-3142-84DC-395C31C71058
+  UUID: DEC88D40-0CDF-3CEF-ACDC-38A03EFB9462
   Functions: 153
-  Symbols:   129
-  CStrings:  112
+  Symbols:   133
+  CStrings:  116
 
Symbols:
+ _FigSignalErrorAt3
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _os_log_type_enabled
- _FigSignalErrorAtGM
Functions:
~ sub_68dc : 384 -> 424
~ sub_6b6c -> sub_6b94 : 92 -> 392
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "APHALCarAudioStream.c"
+ "CarPlayHALPluginFactory %s: CarPlayEndpointManagerCarPlay = [%p]"
+ "Unknown config change action"
+ "kAudioHardwareIllegalOperationError"
- "%s signalled err=%d at <>:%d"

```
