## AVCHalogen

> `/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/AVCHalogen`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-980.77.1.2.0
-  __TEXT.__text: 0xa5d8
+1005.7.1.0.0
+  __TEXT.__text: 0xa804
   __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__cstring: 0x285a
+  __TEXT.__cstring: 0x2a6a
   __TEXT.__const: 0xb0
   __TEXT.__oslogstring: 0x4b
   __TEXT.__unwind_info: 0x380

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  Functions: 219
+  Functions: 221
   Symbols:   207
-  CStrings:  201
+  CStrings:  219
 
Symbols:
+ _FigSignalErrorAt3
- _FigSignalErrorAtGM
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "APHALAudioControl.c"
+ "APHALAudioDevice.c"
+ "APHALAudioStream.c"
+ "Could not allocate APHALAudioSharedState"
+ "Could not allocate volumeContextRef"
+ "Device was unplugged"
+ "EndpointStream has NULL ID"
+ "Expecting WriteMix operation"
+ "Failed to create notification queue"
+ "NULL changeRecord"
+ "No AudioEngine"
+ "Unknown change action"
+ "kAudioHardwareBadDeviceError"
+ "kAudioHardwareBadObjectError"
+ "kAudioHardwareIllegalOperationError"
+ "kAudioHardwareUnsupportedOperationError"
+ "kCMBaseObjectError_AllocationFailed"
+ "kFigEndpointStreamError_InvalidParameter"
- "%s signalled err=%d at <>:%d"
```
