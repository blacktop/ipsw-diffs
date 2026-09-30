## AVCHalogen

> `/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/AVCHalogen`

```diff

-940.21.1.0.0
-  __TEXT.__text: 0xa0f8
+940.22.2.0.0
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
-  UUID: 662FDBA0-C385-3E88-A82D-541A0501040E
-  Functions: 231
+  UUID: A12DF24B-4139-3F30-9EAB-A0146F76E068
+  Functions: 227
   Symbols:   198
-  CStrings:  222
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
