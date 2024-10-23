## AVCHalogen

> `/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/AVCHalogen`

```diff

-830.10.1.1.0
-  __TEXT.__text: 0x8ab4
+835.13.1.11.1
+  __TEXT.__text: 0x8ca4
   __TEXT.__auth_stubs: 0x850
-  __TEXT.__cstring: 0x2135
+  __TEXT.__cstring: 0x2266
   __TEXT.__const: 0xa0
   __TEXT.__unwind_info: 0x158
   __DATA_CONST.__auth_got: 0x428
-  __DATA_CONST.__got: 0x1b0
+  __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__const: 0x3e0
-  __DATA_CONST.__cfstring: 0x200
+  __DATA_CONST.__cfstring: 0x1c0
   __DATA.__data: 0x1c0
   __DATA.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  Functions: 76
-  Symbols:   193
-  CStrings:  162
+  Functions: 75
+  Symbols:   192
+  CStrings:  177
 
Symbols:
+ _FigSignalErrorAt3
+ _fig_log_get_emitter
- _APSTapToRadarInvoke
- _FigSignalErrorAt
- _kAPSRadarLoggingComponent_AirPlayNewBugs
CStrings:
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
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
- "Streaming Audio Bounds Violation"
- "Streaming Audio DoIO Bounds Checking Violation: %!@(MISSING) (log latency: %!f(MISSING) ms)\n"
- "TTR: Streaming Audio DoIO Bounds Checking Violation"
- "bad"
- "good"
- "sampleRate=%!u(MISSING)[%!s(MISSING)] bytesPerFrame=%!u(MISSING)[%!s(MISSING)] ioBufferFrameSize=%!u(MISSING)[%!s(MISSING)] framesToDrop=%!u(MISSING)[%!s(MISSING)] bytesToDrop=%!l(MISSING)lu length=%!l(MISSING)lu"
- "stream_ttrLogger"
- "void stream_ttrLogger(const APSAsyncLoggerParameters *, Float64)"

```
