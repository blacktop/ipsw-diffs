## AVCHalogen

> `/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/Contents/MacOS/AVCHalogen`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-980.71.1.0.0
-  __TEXT.__text: 0xad78
+980.77.5.3.0
+  __TEXT.__text: 0xab40
   __TEXT.__auth_stubs: 0x8f0
-  __TEXT.__cstring: 0x2a6a
+  __TEXT.__cstring: 0x285a
   __TEXT.__const: 0xb0
   __TEXT.__oslogstring: 0x4b
   __TEXT.__unwind_info: 0x230

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/Versions/A/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  Functions: 225
+  Functions: 223
   Symbols:   210
-  CStrings:  219
+  CStrings:  201
 
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
- "No AudioEngine"
- "Unknown change action"
- "kAudioHardwareBadDeviceError"
- "kAudioHardwareBadObjectError"
- "kAudioHardwareIllegalOperationError"
- "kAudioHardwareUnsupportedOperationError"
- "kCMBaseObjectError_AllocationFailed"
- "kFigEndpointStreamError_InvalidParameter"
```
