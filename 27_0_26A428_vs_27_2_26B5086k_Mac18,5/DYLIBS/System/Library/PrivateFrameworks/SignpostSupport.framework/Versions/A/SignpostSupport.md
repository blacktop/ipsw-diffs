## SignpostSupport

> `/System/Library/PrivateFrameworks/SignpostSupport.framework/Versions/A/SignpostSupport`

```diff

-203.0.0.0.0
-  __TEXT.__text: 0x7c5b0
-  __TEXT.__objc_methlist: 0xa02c
+205.0.0.0.0
+  __TEXT.__text: 0x7dc38
+  __TEXT.__objc_methlist: 0xa38c
   __TEXT.__const: 0x19f8
-  __TEXT.__cstring: 0x1a737
+  __TEXT.__cstring: 0x1ac8f
   __TEXT.__oslogstring: 0xef4
-  __TEXT.__gcc_except_tab: 0x2654
+  __TEXT.__gcc_except_tab: 0x2658
   __TEXT.__ustring: 0x3e
-  __TEXT.__unwind_info: 0x3060
+  __TEXT.__unwind_info: 0x30a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b78
+  __DATA_CONST.__objc_selrefs: 0x3cd0
   __DATA_CONST.__objc_superrefs: 0x488
   __DATA_CONST.__objc_arraydata: 0x50c8
   __DATA_CONST.__got: 0x470
   __AUTH_CONST.__const: 0x2228
-  __AUTH_CONST.__cfstring: 0x1ca60
-  __AUTH_CONST.__objc_const: 0x16c38
+  __AUTH_CONST.__cfstring: 0x1cda0
+  __AUTH_CONST.__objc_const: 0x17248
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x408
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0xf30
+  __DATA.__objc_ivar: 0xf90
   __DATA.__data: 0x1180
   __DATA_DIRTY.__objc_data: 0x3390
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4141
-  Symbols:   8887
-  CStrings:  3920
+  Functions: 4212
+  Symbols:   9017
+  CStrings:  3945
 
Symbols:
+ -[SSPSMImmutableVMStats activeInternalCount]
+ -[SSPSMImmutableVMStats executableCount]
+ -[SSPSMImmutableVMStats inactiveInternalCount]
+ -[SSPSMImmutableVMStats pageinsDelta]
+ -[SSPSMImmutableVMStats purgeablePageableCount]
+ -[SSPSMImmutableVMStats purgeableWiredCount]
+ -[SSPSMImmutableVMStats realtimeCount]
+ -[SSPSMMutableVMStats activeInternalCount]
+ -[SSPSMMutableVMStats executableCount]
+ -[SSPSMMutableVMStats inactiveInternalCount]
+ -[SSPSMMutableVMStats initWithActiveCount:speculativeCount:inactiveCount:freeCount:wireCount:compressorPageCount:internalPageCount:externalPageCount:totalUncompressedPagesInCompressor:swappedCount:swapCount:pageSharedRegionCount:pageinsDelta:executableCount:purgeablePageableCount:purgeableWiredCount:activeInternalCount:inactiveInternalCount:realtimeCount:]
+ -[SSPSMMutableVMStats pageinsDelta]
+ -[SSPSMMutableVMStats purgeablePageableCount]
+ -[SSPSMMutableVMStats purgeableWiredCount]
+ -[SSPSMMutableVMStats realtimeCount]
+ -[SSPSMMutableVMStats setActiveInternalCount:]
+ -[SSPSMMutableVMStats setExecutableCount:]
+ -[SSPSMMutableVMStats setInactiveInternalCount:]
+ -[SSPSMMutableVMStats setPageinsDelta:]
+ -[SSPSMMutableVMStats setPurgeablePageableCount:]
+ -[SSPSMMutableVMStats setPurgeableWiredCount:]
+ -[SSPSMMutableVMStats setRealtimeCount:]
+ -[SSPSMVMStats activeInternalCount]
+ -[SSPSMVMStats executableCount]
+ -[SSPSMVMStats inactiveInternalCount]
+ -[SSPSMVMStats initWithActiveCount:speculativeCount:inactiveCount:freeCount:wireCount:compressorPageCount:internalPageCount:externalPageCount:totalUncompressedPagesInCompressor:swappedCount:swapCount:pageSharedRegionCount:pageinsDelta:executableCount:purgeablePageableCount:purgeableWiredCount:activeInternalCount:inactiveInternalCount:realtimeCount:]
+ -[SSPSMVMStats pageinsDelta]
+ -[SSPSMVMStats purgeablePageableCount]
+ -[SSPSMVMStats purgeableWiredCount]
+ -[SSPSMVMStats realtimeCount]
+ -[SSVMStats activeExternalPageCount]
+ -[SSVMStats activeInternalPageCount]
+ -[SSVMStats executableCount]
+ -[SSVMStats inactiveExternalPageCount]
+ -[SSVMStats inactiveInternalPageCount]
+ -[SSVMStats pageinsIntervalDelta]
+ -[SSVMStats pageinsPerSecond]
+ -[SSVMStats purgeablePageableCount]
+ -[SSVMStats purgeableWiredCount]
+ -[SSVMStats realtimePageCount]
+ -[SSVMStatsAggregation activeExternalPageCount]
+ -[SSVMStatsAggregation activeInternalPageCount]
+ -[SSVMStatsAggregation executableCount]
+ -[SSVMStatsAggregation inactiveExternalPageCount]
+ -[SSVMStatsAggregation inactiveInternalPageCount]
+ -[SSVMStatsAggregation pageinsIntervalDelta]
+ -[SSVMStatsAggregation purgeablePageableCount]
+ -[SSVMStatsAggregation purgeableWiredCount]
+ -[SSVMStatsAggregation realtimePageCount]
+ -[SSVMStatsAggregation setActiveExternalPageCount:]
+ -[SSVMStatsAggregation setActiveInternalPageCount:]
+ -[SSVMStatsAggregation setExecutableCount:]
+ -[SSVMStatsAggregation setInactiveExternalPageCount:]
+ -[SSVMStatsAggregation setInactiveInternalPageCount:]
+ -[SSVMStatsAggregation setPageinsIntervalDelta:]
+ -[SSVMStatsAggregation setPurgeablePageableCount:]
+ -[SSVMStatsAggregation setPurgeableWiredCount:]
+ -[SSVMStatsAggregation setRealtimePageCount:]
+ -[SSVMStatsDeltas activeExternalPageDeltaPerSecond]
+ -[SSVMStatsDeltas activeExternalPageDelta]
+ -[SSVMStatsDeltas activeInternalPageDeltaPerSecond]
+ -[SSVMStatsDeltas activeInternalPageDelta]
+ -[SSVMStatsDeltas executableCountDeltaPerSecond]
+ -[SSVMStatsDeltas executableCountDelta]
+ -[SSVMStatsDeltas inactiveExternalPageDeltaPerSecond]
+ -[SSVMStatsDeltas inactiveExternalPageDelta]
+ -[SSVMStatsDeltas inactiveInternalPageDeltaPerSecond]
+ -[SSVMStatsDeltas inactiveInternalPageDelta]
+ -[SSVMStatsDeltas purgeablePageableDeltaPerSecond]
+ -[SSVMStatsDeltas purgeablePageableDelta]
+ -[SSVMStatsDeltas purgeableWiredDeltaPerSecond]
+ -[SSVMStatsDeltas purgeableWiredDelta]
+ -[SSVMStatsDeltas realtimePageDeltaPerSecond]
+ -[SSVMStatsDeltas realtimePageDelta]
+ GCC_except_table152
+ GCC_except_table171
+ GCC_except_table179
+ GCC_except_table181
+ GCC_except_table206
+ GCC_except_table208
+ GCC_except_table215
+ GCC_except_table242
+ GCC_except_table244
+ GCC_except_table255
+ GCC_except_table278
+ GCC_except_table280
+ GCC_except_table287
+ GCC_except_table288
+ GCC_except_table291
+ GCC_except_table318
+ GCC_except_table322
+ GCC_except_table349
+ GCC_except_table359
+ GCC_except_table379
+ GCC_except_table389
+ GCC_except_table99
+ OBJC_IVAR_$_SSVMStats._activeInternalPageCount
+ OBJC_IVAR_$_SSVMStats._executableCount
+ OBJC_IVAR_$_SSVMStats._inactiveInternalPageCount
+ OBJC_IVAR_$_SSVMStats._pageinsIntervalDelta
+ OBJC_IVAR_$_SSVMStats._purgeablePageableCount
+ OBJC_IVAR_$_SSVMStats._purgeableWiredCount
+ OBJC_IVAR_$_SSVMStats._realtimePageCount
+ OBJC_IVAR_$_SSVMStatsAggregation._activeExternalPageCount
+ OBJC_IVAR_$_SSVMStatsAggregation._activeInternalPageCount
+ OBJC_IVAR_$_SSVMStatsAggregation._executableCount
+ OBJC_IVAR_$_SSVMStatsAggregation._inactiveExternalPageCount
+ OBJC_IVAR_$_SSVMStatsAggregation._inactiveInternalPageCount
+ OBJC_IVAR_$_SSVMStatsAggregation._pageinsIntervalDelta
+ OBJC_IVAR_$_SSVMStatsAggregation._purgeablePageableCount
+ OBJC_IVAR_$_SSVMStatsAggregation._purgeableWiredCount
+ OBJC_IVAR_$_SSVMStatsAggregation._realtimePageCount
+ OBJC_IVAR_$_SSVMStatsDeltas._activeExternalPageDelta
+ OBJC_IVAR_$_SSVMStatsDeltas._activeInternalPageDelta
+ OBJC_IVAR_$_SSVMStatsDeltas._executableCountDelta
+ OBJC_IVAR_$_SSVMStatsDeltas._inactiveExternalPageDelta
+ OBJC_IVAR_$_SSVMStatsDeltas._inactiveInternalPageDelta
+ OBJC_IVAR_$_SSVMStatsDeltas._purgeablePageableDelta
+ OBJC_IVAR_$_SSVMStatsDeltas._purgeableWiredDelta
+ OBJC_IVAR_$_SSVMStatsDeltas._realtimePageDelta
+ _objc_msgSend$activeExternalPageCount
+ _objc_msgSend$activeExternalPageDelta
+ _objc_msgSend$activeExternalPageDeltaPerSecond
+ _objc_msgSend$activeInternalCount
+ _objc_msgSend$activeInternalPageCount
+ _objc_msgSend$activeInternalPageDelta
+ _objc_msgSend$activeInternalPageDeltaPerSecond
+ _objc_msgSend$executableCount
+ _objc_msgSend$executableCountDelta
+ _objc_msgSend$executableCountDeltaPerSecond
+ _objc_msgSend$inactiveExternalPageCount
+ _objc_msgSend$inactiveExternalPageDelta
+ _objc_msgSend$inactiveExternalPageDeltaPerSecond
+ _objc_msgSend$inactiveInternalCount
+ _objc_msgSend$inactiveInternalPageCount
+ _objc_msgSend$inactiveInternalPageDelta
+ _objc_msgSend$inactiveInternalPageDeltaPerSecond
+ _objc_msgSend$initWithActiveCount:speculativeCount:inactiveCount:freeCount:wireCount:compressorPageCount:internalPageCount:externalPageCount:totalUncompressedPagesInCompressor:swappedCount:swapCount:pageSharedRegionCount:pageinsDelta:executableCount:purgeablePageableCount:purgeableWiredCount:activeInternalCount:inactiveInternalCount:realtimeCount:
+ _objc_msgSend$pageinsDelta
+ _objc_msgSend$pageinsIntervalDelta
+ _objc_msgSend$pageinsPerSecond
+ _objc_msgSend$purgeablePageableCount
+ _objc_msgSend$purgeablePageableDelta
+ _objc_msgSend$purgeablePageableDeltaPerSecond
+ _objc_msgSend$purgeableWiredCount
+ _objc_msgSend$purgeableWiredDelta
+ _objc_msgSend$purgeableWiredDeltaPerSecond
+ _objc_msgSend$realtimeCount
+ _objc_msgSend$realtimePageCount
+ _objc_msgSend$realtimePageDelta
+ _objc_msgSend$realtimePageDeltaPerSecond
+ _objc_msgSend$setActiveInternalCount:
+ _objc_msgSend$setExecutableCount:
+ _objc_msgSend$setInactiveInternalCount:
+ _objc_msgSend$setPageinsDelta:
+ _objc_msgSend$setPurgeablePageableCount:
+ _objc_msgSend$setPurgeableWiredCount:
+ _objc_msgSend$setRealtimeCount:
- -[SSPSMMutableVMStats initWithActiveCount:speculativeCount:inactiveCount:freeCount:wireCount:compressorPageCount:internalPageCount:externalPageCount:totalUncompressedPagesInCompressor:swappedCount:swapCount:pageSharedRegionCount:]
- -[SSPSMVMStats initWithActiveCount:speculativeCount:inactiveCount:freeCount:wireCount:compressorPageCount:internalPageCount:externalPageCount:totalUncompressedPagesInCompressor:swappedCount:swapCount:pageSharedRegionCount:]
- GCC_except_table131
- GCC_except_table143
- GCC_except_table150
- GCC_except_table151
- GCC_except_table153
- GCC_except_table159
- GCC_except_table160
- GCC_except_table180
- GCC_except_table195
- GCC_except_table196
- GCC_except_table214
- GCC_except_table231
- GCC_except_table232
- GCC_except_table250
- GCC_except_table290
- GCC_except_table294
- GCC_except_table308
- GCC_except_table321
- GCC_except_table341
- GCC_except_table351
- GCC_except_table361
- GCC_except_table371
- GCC_except_table381
- GCC_except_table391
- GCC_except_table92
- _objc_msgSend$initWithActiveCount:speculativeCount:inactiveCount:freeCount:wireCount:compressorPageCount:internalPageCount:externalPageCount:totalUncompressedPagesInCompressor:swappedCount:swapCount:pageSharedRegionCount:
CStrings:
+ "Active:                      %lld pages (%.1f/s)\nSpeculative:                 %lld pages (%.1f/s)\nInactive:                    %lld pages (%.1f/s)\nFree:                        %lld pages (%.1f/s)\nWired:                       %lld pages (%.1f/s)\nCompressor:                  %lld pages (%.1f/s)\nInternal:                    %lld pages (%.1f/s)\nExternal:                    %lld pages (%.1f/s)\nUncompressed-in-compressor:  %lld pages (%.1f/s)\nCompressed-in-core:          %lld pages (%.1f/s)\nSwapped:                     %lld pages (%.1f/s)\nSwap:                        %lld pages (%.1f/s)\nShared region:               %lld pages (%.1f/s)\nExecutable:                  %lld pages (%.1f/s)\nPurgeable pageable:          %lld pages (%.1f/s)\nPurgeable wired:             %lld pages (%.1f/s)\nActive internal:             %lld pages (%.1f/s)\nInactive internal:           %lld pages (%.1f/s)\nRealtime:                    %lld pages (%.1f/s)\nActive external:      %lld pages (%.1f/s)\nInactive external:    %lld pages (%.1f/s)"
+ "Active:                      %u pages\nSpeculative:                 %u pages\nInactive:                    %u pages\nFree:                        %u pages\nWired:                       %u pages\nCompressor:                  %u pages\nInternal:                    %u pages\nExternal:                    %u pages\nUncompressed-in-compressor:  %u pages\nCompressed-in-core:          %u pages\nSwapped:                     %u pages\nSwap:                        %u pages\nShared region:               %u pages\nPageins (per-interval):      %u pages (%.1f/s)\nExecutable:                  %u pages\nPurgeable pageable:          %u pages\nPurgeable wired:             %u pages\nActive internal:             %u pages\nInactive internal:           %u pages\nRealtime:                    %u pages\nActive external:      %u pages\nInactive external:    %u pages"
+ "activeExternalPageCount"
+ "activeExternalPageDelta"
+ "activeExternalPageDeltaPerSecond"
+ "activeInternalPageCount"
+ "activeInternalPageDelta"
+ "activeInternalPageDeltaPerSecond"
+ "executableCount"
+ "executableCountDelta"
+ "executableCountDeltaPerSecond"
+ "inactiveExternalPageCount"
+ "inactiveExternalPageDelta"
+ "inactiveExternalPageDeltaPerSecond"
+ "inactiveInternalPageCount"
+ "inactiveInternalPageDelta"
+ "inactiveInternalPageDeltaPerSecond"
+ "pageinsIntervalDelta"
+ "pageinsPerSecond"
+ "purgeablePageableCount"
+ "purgeablePageableDelta"
+ "purgeablePageableDeltaPerSecond"
+ "purgeableWiredCount"
+ "purgeableWiredDelta"
+ "purgeableWiredDeltaPerSecond"
+ "realtimePageCount"
+ "realtimePageDelta"
+ "realtimePageDeltaPerSecond"
+ "\xf0a"
- "\r"
- "Active:                      %lld pages (%.1f/s)\nSpeculative:                 %lld pages (%.1f/s)\nInactive:                    %lld pages (%.1f/s)\nFree:                        %lld pages (%.1f/s)\nWired:                       %lld pages (%.1f/s)\nCompressor:                  %lld pages (%.1f/s)\nInternal:                    %lld pages (%.1f/s)\nExternal:                    %lld pages (%.1f/s)\nUncompressed-in-compressor:  %lld pages (%.1f/s)\nCompressed-in-core:          %lld pages (%.1f/s)\nSwapped:                     %lld pages (%.1f/s)\nSwap:                        %lld pages (%.1f/s)\nShared region:               %lld pages (%.1f/s)"
- "Active:                      %u pages\nSpeculative:                 %u pages\nInactive:                    %u pages\nFree:                        %u pages\nWired:                       %u pages\nCompressor:                  %u pages\nInternal:                    %u pages\nExternal:                    %u pages\nUncompressed-in-compressor:  %u pages\nCompressed-in-core:          %u pages\nSwapped:                     %u pages\nSwap:                        %u pages\nShared region:               %u pages"
- "\xd1"
```
