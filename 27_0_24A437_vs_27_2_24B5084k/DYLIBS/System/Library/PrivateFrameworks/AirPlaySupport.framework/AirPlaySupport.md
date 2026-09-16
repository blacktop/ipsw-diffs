## AirPlaySupport

> `/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport`

```diff

-980.77.1.2.0
-  __TEXT.__text: 0xc8044
+1005.7.1.0.0
+  __TEXT.__text: 0xc8400
   __TEXT.__objc_methlist: 0x374
-  __TEXT.__const: 0xf18
+  __TEXT.__const: 0xf38
   __TEXT.__dlopen_cstrs: 0x158
   __TEXT.__gcc_except_tab: 0x368
-  __TEXT.__cstring: 0x33c69
+  __TEXT.__cstring: 0x33f15
   __TEXT.__oslogstring: 0x252
-  __TEXT.__unwind_info: 0x29b8
+  __TEXT.__unwind_info: 0x29b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__got: 0x7a8
-  __AUTH_CONST.__const: 0x3c98
-  __AUTH_CONST.__cfstring: 0x72e0
+  __AUTH_CONST.__const: 0x3c78
+  __AUTH_CONST.__cfstring: 0x72c0
   __AUTH_CONST.__objc_const: 0x7a8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2624
-  Symbols:   5151
-  CStrings:  4458
+  Functions: 2625
+  Symbols:   5150
+  CStrings:  4481
 
Symbols:
+ GCC_except_table1157
+ GCC_except_table1185
+ GCC_except_table1306
+ GCC_except_table1472
+ GCC_except_table1474
+ GCC_except_table1599
+ GCC_except_table1603
+ GCC_except_table1795
+ GCC_except_table1798
+ GCC_except_table1801
+ GCC_except_table1805
+ GCC_except_table1970
+ GCC_except_table2220
+ GCC_except_table2523
+ GCC_except_table2528
+ GCC_except_table2537
+ GCC_except_table2593
+ GCC_except_table2597
+ GCC_except_table291
+ GCC_except_table293
+ GCC_except_table557
+ GCC_except_table590
+ GCC_except_table976
+ _APSCMTimeMakeWithRTPTimestamp
+ _APSSignalStrengthDBmFromScaled
+ _APSSignalStrengthScaledFromDBm
+ _FigSignalErrorAt3
- GCC_except_table1156
- GCC_except_table1182
- GCC_except_table1305
- GCC_except_table1471
- GCC_except_table1473
- GCC_except_table1600
- GCC_except_table1604
- GCC_except_table1796
- GCC_except_table1799
- GCC_except_table1802
- GCC_except_table1806
- GCC_except_table1971
- GCC_except_table2221
- GCC_except_table2522
- GCC_except_table2527
- GCC_except_table2536
- GCC_except_table2592
- GCC_except_table2595
- GCC_except_table290
- GCC_except_table292
- GCC_except_table556
- GCC_except_table589
- GCC_except_table975
- _APSIsHomeKitManagerEnabled
- _APSIsHomeKitManagerEnabled.sIsHomeKitManagerEnabled
- _APSIsHomeKitManagerEnabled.sIsHomeKitManagerEnabledOnce
- _FigSignalErrorAtGM
- ___APSIsHomeKitManagerEnabled_block_invoke
CStrings:
+ "### %@ [Glitch Underrun Start]. SeqNum: %u. RTPStartTime: %lld.\n"
+ "%@ Pre-warming audio HW\n"
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "-108"
+ "-6705"
+ "-877"
+ "-878"
+ "-879"
+ "-880"
+ "APSAPAPExtensionLoudnessInfoUtils.c"
+ "APSAudioFormatDescription.c"
+ "APSAudioFormatDescriptionList.c"
+ "APSSharedRingBuffer.c"
+ "Could not allocate APSAudioFormatDescription"
+ "Could not allocate APSAudioFormatDescriptionList"
+ "Failed to create bufferMemObject"
+ "Failed to create stateMemObject"
+ "ProcessLatencyReport endpointID: %@ inIsSessionReport: %s networkLatencyMs: %u prevMaxNetworkLatencyMs: %u outOfBoundsCount: %.0lf tloVarEstimateMs: %llu"
+ "almEndToEndLatencyOverrideP2PMs"
+ "bufferMemory region maps to NULL"
+ "bufferMemorySize is zero"
+ "hoseAUAudioIOAssertionDurationSecs"
+ "kCMBaseObjectError_AllocationFailed"
+ "loudness key missing"
+ "sample peak key missing"
+ "stateMemObject maps to NULL"
+ "stateMemoryLength < sizeof(RingState)"
+ "true peak key missing"
+ "void glitchReporter_LogGlitch(CFStringRef, APSGlitchReporterLogEventType, uint32_t, int64_t, Float64)"
- "%s signalled err=%d at <>:%d"
- "Home"
- "MediaGroups"
- "ProcessLatencyReport endpointID: %@ inIsSessionReport: %s networkLatencyMs: %u prevMaxNetworkLatencyMs: %u outOfBoundsCount: %.0lf duringInitialRamp: %s tloVarEstimateMs: %llu"
- "tightSyncUUID"
- "void glitchReporter_LogGlitch(CFStringRef, uint32_t, int64_t, Float64)"
```
