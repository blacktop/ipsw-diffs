## AVCHalogen

> `/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/AVCHalogen`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-1005.13.1.1.0
-  __TEXT.__text: 0xa5d8
-  __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__cstring: 0x285a
-  __TEXT.__const: 0xb0
+1015.5.1.0.0
+  __TEXT.__text: 0xafe4
+  __TEXT.__auth_stubs: 0x8e0
+  __TEXT.__cstring: 0x2a28
+  __TEXT.__const: 0xb8
   __TEXT.__oslogstring: 0x4b
-  __TEXT.__unwind_info: 0x380
+  __TEXT.__unwind_info: 0x3a0
   __DATA_CONST.__const: 0x3e8
   __DATA_CONST.__cfstring: 0x2a0
-  __DATA_CONST.__auth_got: 0x460
-  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__auth_got: 0x470
+  __DATA_CONST.__got: 0x1f0
   __DATA.__data: 0x1c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  Functions: 219
-  Symbols:   207
-  CStrings:  201
+  Functions: 229
+  Symbols:   211
+  CStrings:  213
 
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
