## AirPlaySupport

> `/System/Library/PrivateFrameworks/AirPlaySupport.framework/Versions/A/AirPlaySupport`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__auth_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-960.10.1.0.0
-  __TEXT.__text: 0x8f648
+960.13.1.0.0
+  __TEXT.__text: 0x8f4ec
   __TEXT.__auth_stubs: 0x2ec0
   __TEXT.__objc_methlist: 0x27c
   __TEXT.__const: 0xd6c
   __TEXT.__dlopen_cstrs: 0xaa
   __TEXT.__gcc_except_tab: 0x210
-  __TEXT.__cstring: 0x2611e
+  __TEXT.__cstring: 0x25ef9
   __TEXT.__unwind_info: 0x1768
   __TEXT.__objc_classname: 0x66
   __TEXT.__objc_methname: 0x944

   - /usr/lib/libobjc.A.dylib
   Functions: 2029
   Symbols:   3990
-  CStrings:  3543
+  CStrings:  3521
 
Symbols:
+ _FigSignalErrorAtGM
- _FigSignalErrorAt3
Functions:
~ _APSSharedRingBuffer_CreateWithBufferAndState : 820 -> 652
~ _APSSharedRingBuffer_Create : 1032 -> 980
~ _APSAPAPExtensionConvertLoudnessInfoDictLoudnessParametersToBBuf : 696 -> 632
~ _APSAudioFormatDescriptionCreateWithAudioFormatIndex : 796 -> 756
~ _APSAudioFormatDescriptionListCreate : 456 -> 432
CStrings:
+ "%s signalled err=%d at <>:%d"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "-108"
- "-6705"
- "-877"
- "-878"
- "-879"
- "-880"
- "APSAPAPExtensionLoudnessInfoUtils.c"
- "APSAudioFormatDescription.c"
- "APSAudioFormatDescriptionList.c"
- "APSSharedRingBuffer.c"
- "Could not allocate APSAudioFormatDescription"
- "Could not allocate APSAudioFormatDescriptionList"
- "Failed to create bufferMemObject"
- "Failed to create stateMemObject"
- "bufferMemory region maps to NULL"
- "bufferMemorySize is zero"
- "kCMBaseObjectError_AllocationFailed"
- "loudness key missing"
- "sample peak key missing"
- "stateMemObject maps to NULL"
- "stateMemoryLength < sizeof(RingState)"
- "true peak key missing"
```
