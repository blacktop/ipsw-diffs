## AVCHalogen

> `/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/AVCHalogen`

```diff

-890.79.1.2.0
-  __TEXT.__text: 0xa2f0
+920.5.1.11.1
+  __TEXT.__text: 0xa5bc
   __TEXT.__auth_stubs: 0x870
-  __TEXT.__cstring: 0x25df
+  __TEXT.__cstring: 0x2885
   __TEXT.__const: 0xa0
-  __TEXT.__unwind_info: 0x218
+  __TEXT.__unwind_info: 0x220
   __DATA_CONST.__auth_got: 0x438
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__const: 0x3e0

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  UUID: 39290749-E882-3E80-8E1F-DD1B525DBF06
-  Functions: 220
+  UUID: 2D8C3740-1A00-3F0E-B2DC-584B0A70A2AD
+  Functions: 222
   Symbols:   198
-  CStrings:  201
+  CStrings:  222
 
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
+ "Need at least one supported PCM format from endpointStream"
+ "No AudioEngine"
+ "No compatible transport format exists for selected PCM format."
+ "Unknown change action"
+ "kAudioHardwareBadDeviceError"
+ "kAudioHardwareBadObjectError"
+ "kAudioHardwareIllegalOperationError"
+ "kAudioHardwareUnsupportedOperationError"
+ "kCMBaseObjectError_AllocationFailed"
+ "kCMBaseObjectError_ParamErr"
+ "kFigEndpointStreamError_InvalidParameter"
- "%s signalled err=%d at <>:%d"

```
