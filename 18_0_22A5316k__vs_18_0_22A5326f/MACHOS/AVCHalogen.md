## AVCHalogen

> `/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/AVCHalogen`

```diff

-800.68.1.0.0
-  __TEXT.__text: 0x8ad8
-  __TEXT.__auth_stubs: 0x810
-  __TEXT.__cstring: 0x21c2
+800.72.2.0.0
+  __TEXT.__text: 0x8874
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__cstring: 0x1fc8
   __TEXT.__const: 0xa0
   __TEXT.__unwind_info: 0x158
-  __DATA_CONST.__auth_got: 0x408
+  __DATA_CONST.__auth_got: 0x420
   __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__const: 0x3e0
   __DATA_CONST.__cfstring: 0x1c0

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  Functions: 74
-  Symbols:   188
-  CStrings:  175
+  Functions: 75
+  Symbols:   191
+  CStrings:  154
 
Symbols:
+ _APSRingBufferCreate
+ _APSRingBufferDequeueBytes
+ _APSRingBufferEnqueueBytes
+ _APSRingBufferGetBytesUsed
+ _FigSignalErrorAt
- _FigSignalErrorAt3
- _fig_log_get_emitter
CStrings:
+ "[%!{(MISSING)ptr}] ZTS Info. NowTicks: %!l(MISSING)u SampleTime: %!f(MISSING) HostTime: %!l(MISSING)u (log latency: %!f(MISSING) ms)"
+ "void stream_zeroTimeStampLogger(const APSAsyncLoggerParameters *, Float64)"
- "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
- "(Fig)"
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
- "Unknown change action"
- "com.apple.coremedia"
- "kAudioHardwareBadDeviceError"
- "kAudioHardwareBadObjectError"
- "kAudioHardwareIllegalOperationError"
- "kAudioHardwareUnsupportedOperationError"
- "kCMBaseObjectError_AllocationFailed"
- "kCMBaseObjectError_ParamErr"
- "kFigEndpointStreamError_InvalidParameter"

```
