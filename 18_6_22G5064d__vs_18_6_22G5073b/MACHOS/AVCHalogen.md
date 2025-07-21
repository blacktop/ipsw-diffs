## AVCHalogen

> `/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/AVCHalogen`

```diff

-870.10.1.0.0
-  __TEXT.__text: 0x96d4
-  __TEXT.__auth_stubs: 0x850
-  __TEXT.__cstring: 0x2266
+870.12.2.0.0
+  __TEXT.__text: 0x9238
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__cstring: 0x1fc8
   __TEXT.__const: 0xa0
-  __TEXT.__unwind_info: 0x1f0
-  __DATA_CONST.__auth_got: 0x428
+  __TEXT.__unwind_info: 0x1e8
+  __DATA_CONST.__auth_got: 0x420
   __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__const: 0x3e0
   __DATA_CONST.__cfstring: 0x1c0

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  UUID: D60AE543-2E50-32AA-97BE-43B8798FA13F
-  Functions: 203
-  Symbols:   192
-  CStrings:  191
+  UUID: DB59E0C0-6476-368A-8740-7EBB54975513
+  Functions: 202
+  Symbols:   191
+  CStrings:  168
 
Symbols:
+ _FigSignalErrorAt
- _FigSignalErrorAt3
- _fig_log_get_emitter
Functions (added):
+ sub_5168
+ sub_60ac
+ sub_6ef0
+ sub_8054
+ sub_809c
+ sub_822c
+ sub_8754
+ sub_89f8
+ sub_8a3c
+ sub_8dc0
+ sub_9058
+ sub_923c
+ sub_9504
+ sub_95a8
+ sub_96a0
+ sub_97fc

Functions (removed):
- sub_5168
- sub_60d0
- sub_610c
- sub_6f0c
- sub_80d0
- sub_8268
- sub_87d0
- sub_8b70
- sub_8c54
- sub_8f50
- sub_8ff4
- sub_92e8
- sub_9520
- sub_9834
- sub_9930
- sub_9a80
- sub_9ca4
CStrings:
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
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
