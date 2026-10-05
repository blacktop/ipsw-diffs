## AirPlaySupport

> `/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport`

```diff

-1005.8.1.0.0
-  __TEXT.__text: 0xc8504
+1005.12.1.0.0
+  __TEXT.__text: 0xc83c4
   __TEXT.__objc_methlist: 0x374
   __TEXT.__const: 0xf38
   __TEXT.__dlopen_cstrs: 0x158
   __TEXT.__gcc_except_tab: 0x368
-  __TEXT.__cstring: 0x33f56
+  __TEXT.__cstring: 0x33d5f
   __TEXT.__oslogstring: 0x252
-  __TEXT.__unwind_info: 0x29b8
+  __TEXT.__unwind_info: 0x29c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2627
-  Symbols:   4973
-  CStrings:  4484
+  Functions: 2628
+  Symbols:   4974
+  CStrings:  4463
 
Symbols:
+ GCC_except_table2596
+ GCC_except_table2600
+ _APSAudioHoseMetricCollectorSetSenderRTMetrics
+ _FigSignalErrorAtGM
- GCC_except_table2595
- GCC_except_table2598
- _FigSignalErrorAt3
Functions:
~ _APSSharedRingBuffer_CreateWithBufferAndState : 820 -> 652
~ _APSSharedRingBuffer_Create : 1032 -> 980
~ _protocolDriverSenderTCP_Flush : 268 -> 244
~ _protocolDriverSenderTCP_FlushFromTime : 380 -> 356
~ _APSAudioFormatDescriptionCreateWithAudioFormatIndex : 816 -> 776
~ _APSAudioFormatDescriptionListCreate : 456 -> 420
~ _APSAPAPExtensionConvertLoudnessInfoDictLoudnessParametersToBBuf : 692 -> 536
~ _APSAudioHoseMetricCollectorCreate : 624 -> 628
~ _APSAudioHoseMetricCollectorDeregisterHose : 1420 -> 1436
+ _APSAudioHoseMetricCollectorSetSenderRTMetrics
~ __APSAudioHoseMetricCollectorFinalize : 200 -> 212
CStrings:
+ "%s signalled err=%d at <>:%d"
+ "APSAudioHoseMetricCollectorSetSenderRTMetrics"
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
