## AirPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/AirPlayHalogen.driver/AirPlayHalogen`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-1005.13.1.1.0
-  __TEXT.__text: 0xe280
-  __TEXT.__auth_stubs: 0x930
-  __TEXT.__const: 0xcc
-  __TEXT.__cstring: 0x3182
+1015.5.1.0.0
+  __TEXT.__text: 0xec90
+  __TEXT.__auth_stubs: 0x950
+  __TEXT.__const: 0xd8
+  __TEXT.__cstring: 0x3350
   __TEXT.__oslogstring: 0x4b
-  __TEXT.__unwind_info: 0x4c8
+  __TEXT.__unwind_info: 0x4e8
   __DATA_CONST.__const: 0x7b8
   __DATA_CONST.__cfstring: 0x320
-  __DATA_CONST.__auth_got: 0x498
-  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__auth_got: 0x4a8
+  __DATA_CONST.__got: 0x1f0
   __DATA.__data: 0x238
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  Functions: 316
-  Symbols:   214
-  CStrings:  241
+  Functions: 326
+  Symbols:   218
+  CStrings:  253
 
Symbols:
+ _APAudioSinkJitterBufferCreate
+ _CFGetAllocator
+ _kAPHALAudioDeviceCreationOptionDeviceType_BidirectionalAudio
+ _kFigEndpointStreamProperty_AudioSink
CStrings:
+ "### [%{ptr}] BidirectionalAudio input StartIO failed: %#m\n"
+ "APHALAudioStream-%{ptr}-input"
+ "OSStatus APHALAudioStreamCreate(CFAllocatorRef, FigHALAudioObjectMapper, AudioObjectID, FigEndpointStreamAudioEngineRef, AudioServerPlugInHostRef, APHALAudioSharedStateRef, Boolean, FigHALAudioStreamRef *)"
+ "OSStatus device_startInputIO(FigHALAudioDeviceRef)"
+ "OSStatus device_stopInputIO(FigHALAudioDeviceRef)"
+ "[%{ptr}] BidirectionalAudio input StartIO: input=%s\n"
+ "[%{ptr}] BidirectionalAudio input StopIO completed: %#m\n"
+ "[%{ptr}] Created APHALAudioStream (input) [%{ptr}]\n"
+ "[%{ptr}]APHALDevice-input linked to audioSink %{ptr} \n"
+ "device_startInputIO"
+ "device_stopInputIO"
+ "off"
+ "on"
- "OSStatus APHALAudioStreamCreate(CFAllocatorRef, FigHALAudioObjectMapper, AudioObjectID, FigEndpointStreamAudioEngineRef, AudioServerPlugInHostRef, APHALAudioSharedStateRef, FigHALAudioStreamRef *)"
```
