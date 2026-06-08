## CarPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen`

```diff

-950.7.1.0.0
-  __TEXT.__text: 0x72dc
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x1361
-  __TEXT.__oslogstring: 0x52
-  __TEXT.__unwind_info: 0x1a8
-  __DATA_CONST.__auth_got: 0x2b8
-  __DATA_CONST.__got: 0x118
+980.58.1.11.1
+  __TEXT.__text: 0x7210
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x1235
+  __TEXT.__oslogstring: 0x93
+  __TEXT.__unwind_info: 0x1a0
   __DATA_CONST.__const: 0x2d0
   __DATA_CONST.__cfstring: 0x60
+  __DATA_CONST.__auth_got: 0x2d8
+  __DATA_CONST.__got: 0x118
   __DATA.__data: 0xe0
-  __DATA.__common: 0x10
   __DATA.__bss: 0x8c
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  UUID: 8B7EBD42-136B-3978-9A26-F9436D3EED92
+  UUID: B7F1B2C7-D229-3785-8204-9D695C0933A2
   Functions: 153
-  Symbols:   129
-  CStrings:  112
+  Symbols:   131
+  CStrings:  109
 
Symbols:
+ _FigSignalErrorAt3
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _os_log_type_enabled
- _FigSignalErrorAtGM
- _kAPEndpointStreamCarPlayAudioControl_SpeechEvent
- _kAPEndpointStreamCarPlayAudioControl_SpeechEventKey_Event
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "APHALCarAudioStream.c"
+ "CarPlayHALPluginFactory %s: CarPlayEndpointManagerCarPlay = [%p]"
+ "Unknown config change action"
+ "kAudioHardwareIllegalOperationError"
- "%s signalled err=%d at <>:%d"
- "%s, isUnplugged=%d\n"
- "Boolean carDevice_HasProperty(FigHALAudioObjectRef, const AudioObjectPropertyAddress *)"
- "Boolean carDevice_IsPropertySettable(FigHALAudioObjectRef, const AudioObjectPropertyAddress *)"
- "UInt32 carDevice_GetPropertyDataSize(FigHALAudioObjectRef, const AudioObjectPropertyAddress *, UInt32, const void *)"
- "carDevice_GetPropertyDataSize"
- "carDevice_HasProperty"
- "carDevice_IsPropertySettable"

```
