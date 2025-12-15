## AVCHalogen

> `/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/AVCHalogen`

```diff

-925.5.1.1.0
-  __TEXT.__text: 0xa2f0
+935.3.1.0.0
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
-  UUID: EBC7AD41-8007-3BD0-96DF-0CAE26F10118
-  Functions: 220
+  UUID: BF0442AC-E3AB-3352-B612-2920BF47512F
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
