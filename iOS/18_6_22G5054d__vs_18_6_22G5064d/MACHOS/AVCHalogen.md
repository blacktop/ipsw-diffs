## AVCHalogen

> `/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/AVCHalogen`

```diff

-870.8.1.0.0
-  __TEXT.__text: 0x9238
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__cstring: 0x1fc8
+870.10.1.0.0
+  __TEXT.__text: 0x96d4
+  __TEXT.__auth_stubs: 0x850
+  __TEXT.__cstring: 0x2266
   __TEXT.__const: 0xa0
-  __TEXT.__unwind_info: 0x1e8
-  __DATA_CONST.__auth_got: 0x420
+  __TEXT.__unwind_info: 0x1f0
+  __DATA_CONST.__auth_got: 0x428
   __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__const: 0x3e0
   __DATA_CONST.__cfstring: 0x1c0

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  UUID: 9F762C8A-04D3-3BA7-8F50-B97F46C2826C
-  Functions: 202
-  Symbols:   191
-  CStrings:  168
+  UUID: D60AE543-2E50-32AA-97BE-43B8798FA13F
+  Functions: 203
+  Symbols:   192
+  CStrings:  191
 
Symbols:
+ _FigSignalErrorAt3
+ _fig_log_get_emitter
- _FigSignalErrorAt
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "(Fig)"
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
+ "Unknown change action"
+ "com.apple.coremedia"
+ "kAudioHardwareBadDeviceError"
+ "kAudioHardwareBadObjectError"
+ "kAudioHardwareIllegalOperationError"
+ "kAudioHardwareUnsupportedOperationError"
+ "kCMBaseObjectError_AllocationFailed"
+ "kCMBaseObjectError_ParamErr"
+ "kFigEndpointStreamError_InvalidParameter"

```
