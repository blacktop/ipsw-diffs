## AirPlaySupport

> `/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport`

```diff

-  __TEXT.__text: 0x95748
+  __TEXT.__text: 0x955ec
   __TEXT.__auth_stubs: 0x3180
   __TEXT.__objc_methlist: 0x2c4
   __TEXT.__const: 0xda4
   __TEXT.__dlopen_cstrs: 0x102
   __TEXT.__gcc_except_tab: 0x260
-  __TEXT.__cstring: 0x27da1
+  __TEXT.__cstring: 0x27b7c
   __TEXT.__oslogstring: 0x6c
   __TEXT.__unwind_info: 0x17f0
   __TEXT.__objc_classname: 0x7d

   - /usr/lib/libobjc.A.dylib
   Functions: 2069
   Symbols:   5385
-  CStrings:  4467
+  CStrings:  4445
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ _FigSignalErrorAtGM
- _FigSignalErrorAt3
Functions:
~ _APSSharedRingBuffer_CreateWithBufferAndState : 820 -> 652
~ _APSSharedRingBuffer_Create : 1032 -> 980
~ _APSAudioFormatDescriptionCreateWithAudioFormatIndex : 796 -> 756
~ _APSAudioFormatDescriptionListCreate : 456 -> 432
~ _APSAPAPExtensionConvertLoudnessInfoDictLoudnessParametersToBBuf : 696 -> 632
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
