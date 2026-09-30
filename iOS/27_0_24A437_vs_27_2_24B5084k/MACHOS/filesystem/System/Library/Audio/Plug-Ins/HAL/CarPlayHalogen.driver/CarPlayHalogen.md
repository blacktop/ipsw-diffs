## CarPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-980.77.1.2.0
-  __TEXT.__text: 0x6f8c
-  __TEXT.__auth_stubs: 0x560
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x12c5
-  __TEXT.__oslogstring: 0x52
-  __TEXT.__unwind_info: 0x2a8
+1005.7.1.0.0
+  __TEXT.__text: 0x70e8
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x132a
+  __TEXT.__oslogstring: 0x93
+  __TEXT.__unwind_info: 0x2b0
   __DATA_CONST.__const: 0x2d0
   __DATA_CONST.__cfstring: 0x60
-  __DATA_CONST.__auth_got: 0x2b0
-  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__auth_got: 0x2d8
+  __DATA_CONST.__got: 0x118
   __DATA.__data: 0xe0
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   Functions: 157
-  Symbols:   125
-  CStrings:  107
+  Symbols:   131
+  CStrings:  111
 
Symbols:
+ _FigSignalErrorAt3
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _os_log_type_enabled
- _FigSignalErrorAtGM
Functions:
~ sub_99c -> sub_9ec : 2668 -> 2672
~ sub_6454 -> sub_64a8 : 384 -> 424
~ sub_66e0 -> sub_675c : 92 -> 396
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "APHALCarAudioStream.c"
+ "CarPlayHALPluginFactory %s: CarPlayEndpointManagerCarPlay = [%p]"
+ "Unknown config change action"
+ "kAudioHardwareIllegalOperationError"
- "%s signalled err=%d at <>:%d"
```
