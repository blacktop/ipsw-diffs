## AVCHalogen

> `/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/AVCHalogen`

```diff

-890.73.1.11.1
-  __TEXT.__text: 0xa3ec
+890.77.2.0.0
+  __TEXT.__text: 0xa2f0
   __TEXT.__auth_stubs: 0x870
-  __TEXT.__cstring: 0x279f
+  __TEXT.__cstring: 0x25df
   __TEXT.__const: 0xa0
   __TEXT.__unwind_info: 0x218
   __DATA_CONST.__auth_got: 0x438

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  UUID: 30B98249-B374-36B9-9A88-0A1C69CC83A8
-  Functions: 219
+  UUID: D87802D6-A097-3698-B801-D17E6108B1B8
+  Functions: 220
   Symbols:   198
-  CStrings:  218
+  CStrings:  201
 
Symbols:
+ _FigSignalErrorAtGM
- _FigSignalErrorAt3
CStrings:
+ "%s signalled err=%d at <>:%d"
+ "Created APHALAudioDevice [%{ptr}] for stream [%{ptr}]%?{end} and endpoint [%{ptr}]"
+ "[%{ptr}] APHALAudioDevice Finalized\n"
+ "[%{ptr}] Created APHALAudioStream [%{ptr}]\n"
+ "[%{ptr}] Releasing APHALAudioStream [%{ptr}]\n"
+ "[%{ptr}] StopIO total: %1.3f ms\n"
+ "void device_Finalize(CMBaseObjectRef)"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "APHALAudioControl.c"
- "APHALAudioDevice.c"
- "APHALAudioStream.c"
- "Could not allocate APHALAudioSharedState"
- "Could not allocate volumeContextRef"
- "Created APHALAudioDevice [%{ptr}]"
- "Device was unplugged"
- "EndpointStream has NULL ID"
- "Expecting WriteMix operation"
- "Failed to create notification queue"
- "NULL changeRecord"
- "Need at least one supported PCM format from endpointStream"
- "No AudioEngine"
- "No compatible transport format exists for selected PCM format."
- "Unknown change action"
- "[%{ptr}] StopIO\n"
- "kAudioHardwareBadDeviceError"
- "kAudioHardwareBadObjectError"
- "kAudioHardwareIllegalOperationError"
- "kAudioHardwareUnsupportedOperationError"
- "kCMBaseObjectError_AllocationFailed"
- "kCMBaseObjectError_ParamErr"
- "kFigEndpointStreamError_InvalidParameter"

```
