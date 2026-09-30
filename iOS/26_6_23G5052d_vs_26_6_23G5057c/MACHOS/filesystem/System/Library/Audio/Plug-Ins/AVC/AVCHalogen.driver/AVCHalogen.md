## AVCHalogen

> `/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/AVCHalogen`

```diff

-  __TEXT.__text: 0xa0f8
+  __TEXT.__text: 0x9e40
   __TEXT.__auth_stubs: 0x870
-  __TEXT.__cstring: 0x2885
+  __TEXT.__cstring: 0x25df
   __TEXT.__const: 0xa0
-  __TEXT.__unwind_info: 0x220
+  __TEXT.__unwind_info: 0x210
   __DATA_CONST.__auth_got: 0x438
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__const: 0x3e0

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  Functions: 231
+  Functions: 227
   Symbols:   198
-  CStrings:  222
+  CStrings:  201
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Symbols:
+ _FigSignalErrorAtGM
- _FigSignalErrorAt3
CStrings:
+ "%s signalled err=%d at <>:%d"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "APHALAudioControl.c"
- "APHALAudioDevice.c"
- "APHALAudioStream.c"
- "Could not allocate APHALAudioSharedState"
- "Could not allocate volumeContextRef"
- "Device was unplugged"
- "EndpointStream has NULL ID"
- "Expecting WriteMix operation"
- "Failed to create notification queue"
- "NULL changeRecord"
- "Need at least one supported PCM format from endpointStream"
- "No AudioEngine"
- "No compatible transport format exists for selected PCM format."
- "Unknown change action"
- "kAudioHardwareBadDeviceError"
- "kAudioHardwareBadObjectError"
- "kAudioHardwareIllegalOperationError"
- "kAudioHardwareUnsupportedOperationError"
- "kCMBaseObjectError_AllocationFailed"
- "kCMBaseObjectError_ParamErr"
- "kFigEndpointStreamError_InvalidParameter"

```
