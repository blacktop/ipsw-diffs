## AVCHalogen

> `/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/AVCHalogen`

```diff

-830.2.0.0.0
-  __TEXT.__text: 0x8874
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__cstring: 0x1fc8
+830.4.1.0.0
+  __TEXT.__text: 0x8ee4
+  __TEXT.__auth_stubs: 0x860
+  __TEXT.__cstring: 0x23d3
   __TEXT.__const: 0xa0
   __TEXT.__unwind_info: 0x158
-  __DATA_CONST.__auth_got: 0x420
-  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__auth_got: 0x430
+  __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__const: 0x3e0
-  __DATA_CONST.__cfstring: 0x1c0
+  __DATA_CONST.__cfstring: 0x200
   __DATA.__data: 0x1c0
   __DATA.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  Functions: 75
-  Symbols:   191
-  CStrings:  154
+  Functions: 76
+  Symbols:   194
+  CStrings:  185
 
Symbols:
+ _fig_log_get_emitter
+ _kAPSRadarLoggingComponent_AirPlayNewBugs
+ _FigSignalErrorAt3
+ _APSTapToRadarInvoke
- _FigSignalErrorAt
CStrings:
+ "Could not allocate APHALAudioSharedState"
+ "Failed to create notification queue"
+ "Streaming Audio Bounds Violation"
+ "good"
+ "sampleRate=%!u(MISSING)[%!s(MISSING)] bytesPerFrame=%!u(MISSING)[%!s(MISSING)] ioBufferFrameSize=%!u(MISSING)[%!s(MISSING)] framesToDrop=%!u(MISSING)[%!s(MISSING)] bytesToDrop=%!l(MISSING)lu length=%!l(MISSING)lu"
+ "stream_ttrLogger"
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
+ "APHALAudioControl.c"
+ "kAudioHardwareIllegalOperationError"
+ "(Fig)"
+ "kAudioHardwareBadDeviceError"
+ "com.apple.coremedia"
+ "APHALAudioStream.c"
+ "Expecting WriteMix operation"
+ "Device was unplugged"
+ "Streaming Audio DoIO Bounds Checking Violation: %!@(MISSING) (log latency: %!f(MISSING) ms)\n"
+ "TTR: Streaming Audio DoIO Bounds Checking Violation"
+ "Need at least one supported PCM format from endpointStream"
+ "Could not allocate volumeContextRef"
+ "void stream_ttrLogger(const APSAsyncLoggerParameters *, Float64)"
+ "APHALAudioDevice.c"
+ "kCMBaseObjectError_ParamErr"
+ "No AudioEngine"
+ "EndpointStream has NULL ID"
+ "Unknown change action"
+ "kFigEndpointStreamError_InvalidParameter"
+ "bad"
+ "kAudioHardwareUnsupportedOperationError"
+ "kAudioHardwareBadObjectError"
+ "NULL changeRecord"
+ "kCMBaseObjectError_AllocationFailed"

```
