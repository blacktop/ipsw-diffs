## AirPlaySupport

> `/System/Library/PrivateFrameworks/AirPlaySupport.framework/Versions/A/AirPlaySupport`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-980.67.2.0.0
-  __TEXT.__text: 0xc6384
+980.71.1.0.0
+  __TEXT.__text: 0xc6b04
   __TEXT.__objc_methlist: 0x38c
   __TEXT.__const: 0xee8
   __TEXT.__dlopen_cstrs: 0x158
   __TEXT.__gcc_except_tab: 0x374
-  __TEXT.__cstring: 0x32035
+  __TEXT.__cstring: 0x3221e
   __TEXT.__oslogstring: 0x1cc
-  __TEXT.__unwind_info: 0x1dd8
+  __TEXT.__unwind_info: 0x1de0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2708
+  __DATA_CONST.__const: 0x2710
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__got: 0x650
   __AUTH_CONST.__const: 0x44a8
-  __AUTH_CONST.__cfstring: 0x6fe0
+  __AUTH_CONST.__cfstring: 0x7100
   __AUTH_CONST.__objc_const: 0x7a8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x48

   __AUTH.__data: 0x350
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x25b8
-  __DATA.__bss: 0xb10
+  __DATA.__bss: 0xb08
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__data: 0xa00
   __DATA_DIRTY.__bss: 0x658

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2616
-  Symbols:   5032
-  CStrings:  4307
+  Functions: 2619
+  Symbols:   5036
+  CStrings:  4320
 
Symbols:
+ GCC_except_table1224
+ GCC_except_table1230
+ GCC_except_table1299
+ GCC_except_table1304
+ GCC_except_table1317
+ GCC_except_table1345
+ GCC_except_table1496
+ GCC_except_table1536
+ GCC_except_table1542
+ GCC_except_table1782
+ GCC_except_table1785
+ GCC_except_table1788
+ GCC_except_table1792
+ GCC_except_table2090
+ GCC_except_table2231
+ GCC_except_table2464
+ GCC_except_table2467
+ GCC_except_table2468
+ GCC_except_table2540
+ GCC_except_table950
+ _APSAudioProtocolDriverSenderHoseControllerMulticastAPATRequestSubHoseControllerDemotion
+ _APSCFDictionarySetDictionaryCopy
+ _APSTapToRadarInvokeWithUserNotification
+ ___alm_HandleLatencyChange_block_invoke
+ _alm_HandleLatencyChange
+ _apsTapToRadarInvokeDetailed
+ _kAPSAudioProtocolDriverHoseProperty_IsRoutedViaPrimaryAssist
- GCC_except_table1222
- GCC_except_table1229
- GCC_except_table1297
- GCC_except_table1302
- GCC_except_table1315
- GCC_except_table1343
- GCC_except_table1492
- GCC_except_table1534
- GCC_except_table1540
- GCC_except_table1780
- GCC_except_table1783
- GCC_except_table1786
- GCC_except_table1790
- GCC_except_table2088
- GCC_except_table2229
- GCC_except_table2462
- GCC_except_table2465
- GCC_except_table2466
- GCC_except_table2538
- GCC_except_table949
- _APSCopyNetworkInterfaceType
- __alm_UpdateRoleLatencies_block_invoke
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
