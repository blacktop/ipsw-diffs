## AirPlaySupport

> `/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-980.67.2.0.0
-  __TEXT.__text: 0xcbf8c
+980.71.1.0.0
+  __TEXT.__text: 0xcc6f4
   __TEXT.__objc_methlist: 0x38c
   __TEXT.__const: 0xf18
   __TEXT.__dlopen_cstrs: 0x158
   __TEXT.__gcc_except_tab: 0x374
-  __TEXT.__cstring: 0x33cc8
+  __TEXT.__cstring: 0x33eb1
   __TEXT.__oslogstring: 0x252
   __TEXT.__unwind_info: 0x1e08
   __TEXT.__objc_stubs: 0x0

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3068
+  __DATA_CONST.__const: 0x3070
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__got: 0x7a8
   __AUTH_CONST.__const: 0x3c98
-  __AUTH_CONST.__cfstring: 0x7260
+  __AUTH_CONST.__cfstring: 0x7380
   __AUTH_CONST.__objc_const: 0x7a8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x48

   __AUTH.__data: 0x350
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x2778
-  __DATA.__bss: 0xc18
+  __DATA.__bss: 0xc10
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__data: 0x8a8
   __DATA_DIRTY.__bss: 0x5f8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2627
-  Symbols:   5159
-  CStrings:  4475
+  Functions: 2630
+  Symbols:   5163
+  CStrings:  4488
 
Symbols:
+ GCC_except_table1187
+ GCC_except_table1193
+ GCC_except_table1309
+ GCC_except_table143
+ GCC_except_table1477
+ GCC_except_table1604
+ GCC_except_table1608
+ GCC_except_table174
+ GCC_except_table1800
+ GCC_except_table1803
+ GCC_except_table1806
+ GCC_except_table1810
+ GCC_except_table182
+ GCC_except_table1975
+ GCC_except_table2227
+ GCC_except_table2528
+ GCC_except_table2533
+ GCC_except_table2542
+ GCC_except_table2601
+ GCC_except_table2602
+ GCC_except_table290
+ GCC_except_table292
+ GCC_except_table556
+ GCC_except_table593
+ GCC_except_table979
+ _APSAudioProtocolDriverSenderHoseControllerMulticastAPATRequestSubHoseControllerDemotion
+ _APSCFDictionarySetDictionaryCopy
+ _APSTapToRadarInvokeWithUserNotification
+ ___alm_HandleLatencyChange_block_invoke
+ _alm_HandleLatencyChange
+ _apsTapToRadarInvokeDetailed
+ _kAPSAudioProtocolDriverHoseProperty_IsRoutedViaPrimaryAssist
- GCC_except_table1185
- GCC_except_table1192
- GCC_except_table1307
- GCC_except_table142
- GCC_except_table1473
- GCC_except_table1603
- GCC_except_table1607
- GCC_except_table173
- GCC_except_table1799
- GCC_except_table1802
- GCC_except_table1805
- GCC_except_table1809
- GCC_except_table181
- GCC_except_table1973
- GCC_except_table2224
- GCC_except_table2525
- GCC_except_table2530
- GCC_except_table2539
- GCC_except_table2595
- GCC_except_table2599
- GCC_except_table289
- GCC_except_table291
- GCC_except_table555
- GCC_except_table592
- GCC_except_table978
- _APSCopyNetworkInterfaceType
- ___alm_UpdateRoleLatencies_block_invoke_2
- _priorityDispatcher_heartbeatTick
CStrings:
+ "%@ [Media] fillEndTS <= fillBegTS, stop\n"
+ "%@ [Media] nodeEndTS <= cursorTS, toss\n"
+ "%@ [RTP] fillEndTS <= fillBegTS, stop\n"
+ "%@ [RTP] nodeEndTS <= cursorTS, toss\n"
+ "APSAudioProtocolDriverHoseProperty_IsRoutedViaPrimaryAssist"
+ "APSAudioProtocolDriverSenderHoseControllerMulticastAPATRequestSubHoseControllerDemotion"
+ "APSCFDictionarySetDictionaryCopy"
+ "APSTapToRadarInvokeWithUserNotification"
+ "AppleUSBNCM11Data"
+ "Not invoking TTR on non-internal builds"
+ "OSStatus APSEndpointStreamAudioHoseAUCreate(CFAllocatorRef, CFAllocatorRef, CFStringRef, CFStringRef, APSNetworkClockRef, APAudioFormat, uint32_t, uint32_t, APSEndpointStreamAudioHoseTransportMessageFormat, int32_t, APSCryptorRef, int32_t, CFDictionaryRef, APSEndpointStreamAudioHoseAURef *)"
+ "OSStatus APSStreamingAudioRendererCreate(CFAllocatorRef, CFStringRef, APSPassThroughJitterBufferRef, APAudioFormat, uint32_t, uint32_t, APSStreamingAudioRendererRef *)"
+ "ProcessLatencyReport endpointID: %@ targetDelayInSec: %.3lf measuredMaxSec: %.3lf target99p99InSec: %.3lf target99p9InSec: %.3lf target99InSec: %.3lf target98InSec: %.3lf target97InSec: %.3lf target96InSec: %.3lf target95InSec: %.3lf customPercentileInSec: %.3lf"
+ "TapToRadarService does not exist. A radar cannot be started"
+ "[%{ptr}] (%@) SeqNum: %u, lastSentMediaTime: %1.3f, TotalTxByteCount: %llu, TotalRTPTxByteCount: %llu, TotalRTCPTxByteCount: %llu, RTPTxPacketCount: %llu, RTCPTxPacketCount: %llu, ReTxPacketCount: %llu, RTT Estimate: %lld ms, RTO Estimate: %lld ms, TLO Estimate: %lld ms, TLOVAR Estimate: %lld ms, OWD Estimate: %lld ms, CCFBReceived: %llu, State: %s, Retransmission Rate: %f (%llu/%llu) (async log latency: %1.3f ms)"
+ "[%{ptr}] Hose: [%{ptr}] Multicast RTC Metrics: primaryAssistUsed: %s"
+ "[%{ptr}] HoseController [%{ptr}] failed to setMulticastGroupInfo with err=%#m -- staying in unicast"
+ "alm_HandleLatencyChange"
+ "anpi"
+ "anri"
+ "avclaBinResolutionSec"
+ "avclaCustomDistributionPercentile"
+ "avclaMinNumberOfElementsNeeded"
+ "avclaTargetPercentile"
+ "avclaWindowLengthSec"
+ "multicastPrimaryAssistUsed"
+ "void apsTapToRadarInvokeDetailed(CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFOptionFlags, CFStringRef, CFStringRef, CFArrayRef, Boolean)"
+ "void apsTapToRadarInvokeDetailed(CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFOptionFlags, CFStringRef, CFStringRef, CFArrayRef, Boolean)_block_invoke_2"
- "%@ [Media] nodeEndTS <= windowBegTS, toss\n"
- "%@ [RTP] nodeEndTS <= windowBegTS, toss\n"
- "APSCopyNetworkInterfaceType"
- "APSPriorityDispatcher.heartbeat"
- "Not invoking TTR on non-internal builds\n"
- "OSStatus APSEndpointStreamAudioHoseAUCreate(CFAllocatorRef, CFAllocatorRef, CFStringRef, CFStringRef, APSNetworkClockRef, APAudioFormat, uint32_t, APSEndpointStreamAudioHoseTransportMessageFormat, int32_t, APSCryptorRef, int32_t, CFDictionaryRef, APSEndpointStreamAudioHoseAURef *)"
- "OSStatus APSStreamingAudioRendererCreate(CFAllocatorRef, CFStringRef, APSPassThroughJitterBufferRef, APAudioFormat, uint32_t, APSStreamingAudioRendererRef *)"
- "ProcessLatencyReport endpointID: %@ targetDelayInSec: %.3lf measuredMaxSec: %.3lf target99p99InSec: %.3lf target99p9InSec: %.3lf target99InSec:  %.3lf target98InSec:  %.3lf target97InSec:  %.3lf target96InSec:  %.3lf target95InSec:  %.3lf"
- "TapToRadarService does not exist. A radar cannot be started\n"
- "[%{ptr}] (%@) SeqNum: %u, lastSentMediaTime: %1.3f, TotalTxByteCount: %llu, TotalRTPTxByteCount: %llu, TotalRTCPTxByteCount: %llu, TxPacketCount: %llu, ReTxPacketCount: %llu, RTT Estimate: %lld ms, RTO Estimate: %lld ms, TLO Estimate: %lld ms, TLOVAR Estimate: %lld ms, OWD Estimate: %lld ms, CCFBReceived: %llu, State: %s, Retransmission Rate: %f (%llu/%llu) (async log latency: %1.3f ms)"
- "[%{ptr}] HoseController [%{ptr}] failed to setMulticastGroupInfo with err=%d -- staying in unicast"
- "nanSignalStrengthThreshold"
- "void APSTapToRadarInvoke(CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFArrayRef, Boolean)"
- "void apsTapToRadarInvokeDetailed(CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFArrayRef, Boolean)"
- "void apsTapToRadarInvokeDetailed(CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFArrayRef, Boolean)_block_invoke_2"
```
