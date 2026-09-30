## SignpostSupport

> `/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport`

```diff

-203.0.0.0.0
-  __TEXT.__text: 0x74dbc
-  __TEXT.__objc_methlist: 0xa02c
+205.0.0.0.0
+  __TEXT.__text: 0x7640c
+  __TEXT.__objc_methlist: 0xa38c
   __TEXT.__const: 0x19f8
-  __TEXT.__cstring: 0x1a737
+  __TEXT.__cstring: 0x1ac8f
   __TEXT.__oslogstring: 0xef4
-  __TEXT.__gcc_except_tab: 0x2604
+  __TEXT.__gcc_except_tab: 0x2608
   __TEXT.__ustring: 0x3e
-  __TEXT.__unwind_info: 0x3070
+  __TEXT.__unwind_info: 0x30b8
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
   __AUTH_CONST.__const: 0x1868
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
   __DATA_DIRTY.__bss: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4105
-  Symbols:   8824
-  CStrings:  3920
+  Functions: 4176
+  Symbols:   8957
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
+ GCC_except_table148
+ GCC_except_table167
+ GCC_except_table175
+ GCC_except_table177
+ GCC_except_table179
+ GCC_except_table202
+ GCC_except_table204
+ GCC_except_table211
+ GCC_except_table215
+ GCC_except_table240
+ GCC_except_table247
+ GCC_except_table274
+ GCC_except_table276
+ GCC_except_table283
+ GCC_except_table284
+ GCC_except_table287
+ GCC_except_table318
+ GCC_except_table332
+ GCC_except_table345
+ GCC_except_table355
+ GCC_except_table365
+ GCC_except_table375
+ GCC_except_table385
+ GCC_except_table395
+ GCC_except_table405
+ GCC_except_table415
+ GCC_except_table95
+ GCC_except_table96
+ _OBJC_IVAR_$_SSVMStats._activeInternalPageCount
+ _OBJC_IVAR_$_SSVMStats._executableCount
+ _OBJC_IVAR_$_SSVMStats._inactiveInternalPageCount
+ _OBJC_IVAR_$_SSVMStats._pageinsIntervalDelta
+ _OBJC_IVAR_$_SSVMStats._purgeablePageableCount
+ _OBJC_IVAR_$_SSVMStats._purgeableWiredCount
+ _OBJC_IVAR_$_SSVMStats._realtimePageCount
+ _OBJC_IVAR_$_SSVMStatsAggregation._activeExternalPageCount
+ _OBJC_IVAR_$_SSVMStatsAggregation._activeInternalPageCount
+ _OBJC_IVAR_$_SSVMStatsAggregation._executableCount
+ _OBJC_IVAR_$_SSVMStatsAggregation._inactiveExternalPageCount
+ _OBJC_IVAR_$_SSVMStatsAggregation._inactiveInternalPageCount
+ _OBJC_IVAR_$_SSVMStatsAggregation._pageinsIntervalDelta
+ _OBJC_IVAR_$_SSVMStatsAggregation._purgeablePageableCount
+ _OBJC_IVAR_$_SSVMStatsAggregation._purgeableWiredCount
+ _OBJC_IVAR_$_SSVMStatsAggregation._realtimePageCount
+ _OBJC_IVAR_$_SSVMStatsDeltas._activeExternalPageDelta
+ _OBJC_IVAR_$_SSVMStatsDeltas._activeInternalPageDelta
+ _OBJC_IVAR_$_SSVMStatsDeltas._executableCountDelta
+ _OBJC_IVAR_$_SSVMStatsDeltas._inactiveExternalPageDelta
+ _OBJC_IVAR_$_SSVMStatsDeltas._inactiveInternalPageDelta
+ _OBJC_IVAR_$_SSVMStatsDeltas._purgeablePageableDelta
+ _OBJC_IVAR_$_SSVMStatsDeltas._purgeableWiredDelta
+ _OBJC_IVAR_$_SSVMStatsDeltas._realtimePageDelta
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
- GCC_except_table127
- GCC_except_table139
- GCC_except_table146
- GCC_except_table147
- GCC_except_table149
- GCC_except_table151
- GCC_except_table155
- GCC_except_table156
- GCC_except_table187
- GCC_except_table191
- GCC_except_table192
- GCC_except_table210
- GCC_except_table223
- GCC_except_table227
- GCC_except_table228
- GCC_except_table246
- GCC_except_table259
- GCC_except_table286
- GCC_except_table290
- GCC_except_table304
- GCC_except_table317
- GCC_except_table327
- GCC_except_table337
- GCC_except_table347
- GCC_except_table357
- GCC_except_table367
- GCC_except_table387
- GCC_except_table88
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
