## AirPlaySupport

> `/System/Library/PrivateFrameworks/AirPlaySupport.framework/Versions/A/AirPlaySupport`

```diff

-980.71.1.0.0
-  __TEXT.__text: 0xc6b04
-  __TEXT.__objc_methlist: 0x38c
+980.77.5.3.0
+  __TEXT.__text: 0xc6784
+  __TEXT.__objc_methlist: 0x374
   __TEXT.__const: 0xee8
   __TEXT.__dlopen_cstrs: 0x158
-  __TEXT.__gcc_except_tab: 0x374
-  __TEXT.__cstring: 0x3221e
+  __TEXT.__gcc_except_tab: 0x368
+  __TEXT.__cstring: 0x31fce
   __TEXT.__oslogstring: 0x1cc
-  __TEXT.__unwind_info: 0x1de0
+  __TEXT.__unwind_info: 0x1dd0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2710
+  __DATA_CONST.__const: 0x26e0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x600
+  __DATA_CONST.__objc_selrefs: 0x5f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__got: 0x650
   __AUTH_CONST.__const: 0x44a8
-  __AUTH_CONST.__cfstring: 0x7100
+  __AUTH_CONST.__cfstring: 0x7060
   __AUTH_CONST.__objc_const: 0x7a8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2619
-  Symbols:   5036
-  CStrings:  4320
+  Functions: 2613
+  Symbols:   5024
+  CStrings:  4289
 
Symbols:
+ GCC_except_table1132
+ GCC_except_table1219
+ GCC_except_table1220
+ GCC_except_table1221
+ GCC_except_table1295
+ GCC_except_table1300
+ GCC_except_table1313
+ GCC_except_table1341
+ GCC_except_table1490
+ GCC_except_table1492
+ GCC_except_table1532
+ GCC_except_table1538
+ GCC_except_table1778
+ GCC_except_table1781
+ GCC_except_table1784
+ GCC_except_table2086
+ GCC_except_table2225
+ GCC_except_table2458
+ GCC_except_table2461
+ GCC_except_table2462
+ GCC_except_table2534
+ GCC_except_table532
+ GCC_except_table946
+ _CMTimebaseGetTimeAndRate
+ _FigSignalErrorAtGM
+ _TapToRadarKitLibraryCore
- -[APSTimeSyncNetworkClock disablePort:]
- -[APSTimeSyncNetworkClock enablePort:]
- GCC_except_table1136
- GCC_except_table1223
- GCC_except_table1224
- GCC_except_table1230
- GCC_except_table1299
- GCC_except_table1304
- GCC_except_table1317
- GCC_except_table1345
- GCC_except_table1494
- GCC_except_table1496
- GCC_except_table1536
- GCC_except_table1542
- GCC_except_table1782
- GCC_except_table1785
- GCC_except_table1792
- GCC_except_table2090
- GCC_except_table2231
- GCC_except_table2464
- GCC_except_table2467
- GCC_except_table2468
- GCC_except_table2540
- GCC_except_table536
- GCC_except_table950
- _CM8021ASClockDisablePort
- _CM8021ASClockEnablePort
- _FigSignalErrorAt3
- _TapToRadarKitLibrary
- ___block_descriptor_56_e15_v24?0r^v8r^v16l
- ___ptpClock_copyPeerListForRegularPeer_block_invoke_5
- ___ptpClock_copyPeerListForRegularPeer_block_invoke_6
- ___ptpClock_enablePortsBasedOnTopology_block_invoke
- _kAPSNetworkClockPeerDictionaryKey_IsEnabled
- _kAPSNetworkClockPeerDictionaryKey_IsTightSyncGroupLeader
- _objc_msgSend$disablePort:
- _objc_msgSend$enablePort:
- _ptpClock_enablePortsBasedOnTopology
CStrings:
+ "%s signalled err=%d at <>:%d"
+ "Not invoking TTR: TTRKit unavailable"
+ "Not invoking TTR: TapToRadarService unavailable"
+ "Not invoking TTR: non-internal build"
+ "OSStatus ptpClock_SetOrUpdateLocalPeerInfo(APSNetworkClockRef, void *, CFDictionaryRef)"
+ "[%{ptr}] Promoted subHoseController [%{ptr}] to multicast, next SeqNum: %u"
+ "[%{ptr}] discontinuity, %s. lastEndPTSDequeuedForSBAR=%1.6f (%lld/%d), peekSBufPTS=%1.6f (%lld/%d), isBelowLowWaterLevel=%d, gap=%1.6f s (maxEnqueueGap %1.6f s)\n"
+ "[%{ptr}] holding sbuf across large discontinuity; lastEndPTSDequeuedForSBAR=%1.6f (%lld/%d), peekSBufPTS=%1.6f (%lld/%d), gap=%1.6f s (maxEnqueueGap %1.6f s), low-water timer rescheduled to synchronizerTime=%1.6f\n"
+ "enqueueing across gap within margin"
+ "holding sbuf"
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
- "IsEnabled"
- "IsTightSyncGroupLeader"
- "Not invoking TTR on non-internal builds"
- "OSStatus ptpClock_SetOrUpdateLocalPeerInfo(APSNetworkClockRef, CFDictionaryRef)"
- "TapToRadarService does not exist. A radar cannot be started"
- "[%{ptr}] %'@ already %s"
- "[%{ptr}] Disabling clock port for peer %'@\n"
- "[%{ptr}] Enabling clock port for peer %'@\n"
- "[%{ptr}] Promoted subHoseController [%{ptr}] to multicast"
- "[%{ptr}] discontinuity, yielding until low water. lastEndPTSDequeuedForSBAR=%1.6f (%lld/%d), peekSBufPTS=%1.6f (%lld/%d), isBelowLowWaterLevel=%d\n"
- "anpi"
- "anri"
- "bufferMemory region maps to NULL"
- "bufferMemorySize is zero"
- "enabled"
- "kCMBaseObjectError_AllocationFailed"
- "loudness key missing"
- "nan"
- "ptpClock_enableOnePortOrAll"
- "ptpClock_enablePortsBasedOnTopology"
- "ptpClock_hasPeerWithTightSyncUUID"
- "sample peak key missing"
- "stateMemObject maps to NULL"
- "stateMemoryLength < sizeof(RingState)"
- "true peak key missing"
- "void ptpClock_enableOnePortOrAll(APSNetworkClockRef, void *, CFDictionaryRef, CFStringRef, CFStringRef)"
```
