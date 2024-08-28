## CarPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen`

```diff

-830.2.0.0.0
-  __TEXT.__text: 0x6cf0
-  __TEXT.__auth_stubs: 0x510
-  __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x1107
-  __TEXT.__oslogstring: 0x190
-  __TEXT.__unwind_info: 0x100
-  __DATA_CONST.__auth_got: 0x288
+830.4.1.0.0
+  __TEXT.__text: 0x6e4c
+  __TEXT.__auth_stubs: 0x550
+  __TEXT.__const: 0xa8
+  __TEXT.__cstring: 0x118f
+  __TEXT.__oslogstring: 0x1d1
+  __TEXT.__unwind_info: 0x108
+  __DATA_CONST.__auth_got: 0x2a8
   __DATA_CONST.__got: 0x110
   __DATA_CONST.__const: 0x2d0
   __DATA_CONST.__cfstring: 0x60
   __DATA.__data: 0xe0
-  __DATA.__common: 0x10
+  __DATA.__common: 0x20
   __DATA.__bss: 0x8c
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   Functions: 45
-  Symbols:   122
-  CStrings:  105
+  Symbols:   126
+  CStrings:  111
 
Symbols:
+ _os_log_type_enabled
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _FigSignalErrorAt3
+ __os_log_send_and_compose_impl
- _FigSignalErrorAt
CStrings:
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
+ "CarPlayHALPluginFactory %!s(MISSING): CarPlayEndpointManagerCarPlay = [%!p(MISSING)]"
+ "APHALCarAudioStream.c"
+ "(Fig)"
+ "kAudioHardwareIllegalOperationError"
+ "Unknown config change action"

```
