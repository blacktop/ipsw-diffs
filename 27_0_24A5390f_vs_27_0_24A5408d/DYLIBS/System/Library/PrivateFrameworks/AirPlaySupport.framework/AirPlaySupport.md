## AirPlaySupport

> `/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
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

-980.71.1.0.0
-  __TEXT.__text: 0xcc6f4
-  __TEXT.__objc_methlist: 0x38c
+980.75.1.0.0
+  __TEXT.__text: 0xcc33c
+  __TEXT.__objc_methlist: 0x374
   __TEXT.__const: 0xf18
   __TEXT.__dlopen_cstrs: 0x158
-  __TEXT.__gcc_except_tab: 0x374
-  __TEXT.__cstring: 0x33eb1
+  __TEXT.__gcc_except_tab: 0x368
+  __TEXT.__cstring: 0x33c69
   __TEXT.__oslogstring: 0x252
-  __TEXT.__unwind_info: 0x1e08
+  __TEXT.__unwind_info: 0x1e00
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3070
+  __DATA_CONST.__const: 0x3040
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a8
+  __DATA_CONST.__objc_selrefs: 0x698
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__got: 0x7a8
   __AUTH_CONST.__const: 0x3c98
-  __AUTH_CONST.__cfstring: 0x7380
+  __AUTH_CONST.__cfstring: 0x72e0
   __AUTH_CONST.__objc_const: 0x7a8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2630
-  Symbols:   5163
-  CStrings:  4488
+  Functions: 2624
+  Symbols:   5150
+  CStrings:  4458
 
Symbols:
+ GCC_except_table1156
+ GCC_except_table1182
+ GCC_except_table1183
+ GCC_except_table1184
+ GCC_except_table1305
+ GCC_except_table1471
+ GCC_except_table1473
+ GCC_except_table1600
+ GCC_except_table1796
+ GCC_except_table1799
+ GCC_except_table1802
+ GCC_except_table1971
+ GCC_except_table2221
+ GCC_except_table2522
+ GCC_except_table2527
+ GCC_except_table2536
+ GCC_except_table2592
+ GCC_except_table2595
+ GCC_except_table2596
+ GCC_except_table589
+ GCC_except_table975
+ _FigSignalErrorAtGM
+ _TapToRadarKitLibraryCore
- -[APSTimeSyncNetworkClock disablePort:]
- -[APSTimeSyncNetworkClock enablePort:]
- GCC_except_table1160
- GCC_except_table1186
- GCC_except_table1187
- GCC_except_table1193
- GCC_except_table1309
- GCC_except_table1475
- GCC_except_table1477
- GCC_except_table1608
- GCC_except_table1800
- GCC_except_table1803
- GCC_except_table1810
- GCC_except_table1975
- GCC_except_table2227
- GCC_except_table2528
- GCC_except_table2533
- GCC_except_table2542
- GCC_except_table2598
- GCC_except_table2601
- GCC_except_table2602
- GCC_except_table593
- GCC_except_table979
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
