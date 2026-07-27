## AVCHalogen

> `/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/Contents/MacOS/AVCHalogen`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-960.10.1.0.0
-  __TEXT.__text: 0xa1fc
+960.13.1.0.0
+  __TEXT.__text: 0x9f44
   __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__cstring: 0x2885
+  __TEXT.__cstring: 0x25df
   __TEXT.__const: 0xa0
-  __TEXT.__unwind_info: 0x220
+  __TEXT.__unwind_info: 0x210
   __DATA_CONST.__auth_got: 0x450
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__const: 0x3e0

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/Versions/A/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  Functions: 233
+  Functions: 229
   Symbols:   201
-  CStrings:  205
+  CStrings:  184
 
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
