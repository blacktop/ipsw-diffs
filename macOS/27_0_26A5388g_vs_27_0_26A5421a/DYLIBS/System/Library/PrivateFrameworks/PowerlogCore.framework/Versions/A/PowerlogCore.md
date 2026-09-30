## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/Versions/A/PowerlogCore`

```diff

-3486.0.81.501.3
-  __TEXT.__text: 0xd4a6c
-  __TEXT.__objc_methlist: 0x8a88
-  __TEXT.__const: 0x658
-  __TEXT.__cstring: 0x3fd18
+3486.1.2.0.0
+  __TEXT.__text: 0xd5848
+  __TEXT.__objc_methlist: 0x8ad0
+  __TEXT.__const: 0x650
+  __TEXT.__cstring: 0x3fee3
   __TEXT.__oslogstring: 0x7220
-  __TEXT.__gcc_except_tab: 0x20f8
-  __TEXT.__unwind_info: 0x2a68
+  __TEXT.__gcc_except_tab: 0x2140
+  __TEXT.__unwind_info: 0x2a90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5198
+  __DATA_CONST.__objc_selrefs: 0x51c8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2b0
-  __DATA_CONST.__objc_arraydata: 0x42408
+  __DATA_CONST.__objc_arraydata: 0x42720
   __DATA_CONST.__got: 0x618
-  __AUTH_CONST.__const: 0x3740
-  __AUTH_CONST.__cfstring: 0x67f60
+  __AUTH_CONST.__const: 0x37a0
+  __AUTH_CONST.__cfstring: 0x683a0
   __AUTH_CONST.__objc_const: 0x9cc8
   __AUTH_CONST.__objc_intobj: 0x49c8
   __AUTH_CONST.__objc_doubleobj: 0x13a0
-  __AUTH_CONST.__objc_arrayobj: 0xf48
-  __AUTH_CONST.__objc_dictobj: 0xef88
-  __AUTH_CONST.__auth_got: 0xb18
+  __AUTH_CONST.__objc_arrayobj: 0xf60
+  __AUTH_CONST.__objc_dictobj: 0xf028
+  __AUTH_CONST.__auth_got: 0xb20
   __AUTH.__objc_data: 0x460
   __DATA.__objc_ivar: 0x708
   __DATA.__data: 0x440
-  __DATA.__bss: 0x15d1
+  __DATA.__bss: 0x1601
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1c70
   __DATA_DIRTY.__data: 0x14

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4502
-  Symbols:   8619
-  CStrings:  14445
+  Functions: 4514
+  Symbols:   8646
+  CStrings:  14480
 
Symbols:
+ +[PLIOKitOperatorComposition rebuildPerBankArraysInBatteryData:forPackID:]
+ +[PLSQLiteConnection tableColumnPresenceCacheSem]
+ +[PLSQLiteConnection tableColumnPresenceCache]
+ +[PLUtilities getHardwarePerfKind:]
+ -[PLSQLiteConnection clearTableColumnPresenceCache]
+ -[PLSQLiteConnection tableHasColumn:inTable:]
+ GCC_except_table106
+ GCC_except_table108
+ GCC_except_table113
+ GCC_except_table117
+ GCC_except_table122
+ GCC_except_table145
+ GCC_except_table147
+ GCC_except_table202
+ GCC_except_table82
+ ___35+[PLUtilities getHardwarePerfKind:]_block_invoke
+ ___46+[PLSQLiteConnection tableColumnPresenceCache]_block_invoke
+ ___49+[PLSQLiteConnection tableColumnPresenceCacheSem]_block_invoke
+ ___snprintf_chk
+ _objc_msgSend$clearTableColumnPresenceCache
+ _objc_msgSend$rebuildPerBankArraysInBatteryData:forPackID:
+ _objc_msgSend$tableColumnPresenceCache
+ _objc_msgSend$tableColumnPresenceCacheSem
+ _objc_msgSend$tableHasColumn:inTable:
+ getHardwarePerfKind:.cache
+ getHardwarePerfKind:.cacheOnce
+ tableColumnPresenceCache.onceToken
+ tableColumnPresenceCache.tableColumnPresenceCache
+ tableColumnPresenceCacheSem.onceToken
+ tableColumnPresenceCacheSem.tableColumnPresenceCacheSem
- GCC_except_table102
- GCC_except_table107
- GCC_except_table139
CStrings:
+ "%@|%@|%@"
+ "CPUEnergyM"
+ "CellVoltage"
+ "CellWom"
+ "CoreSpeech"
+ "DaySinceAccountChange"
+ "DaySinceReset"
+ "DaySinceSetup"
+ "DaySinceUpgrade"
+ "MailProgress"
+ "MessagesDonated"
+ "MessagesIndexable"
+ "OneMonthDonatedPercentage"
+ "OneMonthHeaderDonationPercentage"
+ "OneMonthIndexableCount"
+ "OneYearDonatedPercentage"
+ "OneYearHeaderDonationPercentage"
+ "OneYearIndexableCount"
+ "PDEB"
+ "PDTP"
+ "RaTableRaw"
+ "RedonationCount"
+ "SixMonthDonatedPercentage"
+ "SixMonthHeaderDonationPercentage"
+ "SixMonthIndexableCount"
+ "SuppressionType2ClientStateChange"
+ "ThreeMonthDonatedPercentage"
+ "ThreeMonthHeaderDonationPercentage"
+ "ThreeMonthIndexableCount"
+ "TotalDonatedMessageBodies"
+ "TotalDonatedMessages"
+ "TotalIndexableMessages"
+ "TotalPendingRedonationsCount"
+ "ViewObstructedType2StateChange"
+ "batteryPackIndex"
+ "bookmarkFailureCount"
+ "bookmarkRecoveryCount"
+ "cascadeEntitiesQueriedCount"
+ "embeddingsCount"
+ "embeddingsSizeBytes"
+ "entitiesExtractionCount"
+ "entitiesProcessedCount"
+ "hw.perflevel%u.name"
+ "lmeSlotEntityCount"
+ "lmeSlotUpdatedCount"
+ "profileRebuildCount"
+ "profileRebuildReason"
+ "profileSizeBytes"
+ "rankingEventCount"
+ "rankingEventType"
+ "rankingItemsPerEventAvg"
+ "rankingItemsPerEventMax"
- "PLBatteryAgent_EventBackward_RebalanceData"
- "PLDisplayAgent_EventBackward_APLStatsX"
- "PLDisplayAgent_EventPoint_DisplayX"
- "PLIOReportAgent_EventBackward_DCPSECscanout"
- "PLIOReportAgent_EventBackward_DCPSECscanoutstats"
- "PLIOReportAgent_EventBackward_DCPSECswap"
- "PLIOReportAgent_EventBackward_Multitouch2Multitouchhighlevelstats"
- "PLIOReportAgent_EventBackward_Multitouch2touch"
- "PLScreenStateAgent_EventForward_ScreenStateX"
- "RebalanceEnableStatus"
- "RebalanceErrorFlags"
- "RebalanceHWBypassFETStatus0"
- "RebalanceHWBypassFETStatus1"
- "RebalanceInrushCurrentDebug"
- "RebalanceNotRebalancingReason"
- "RebalanceOutputStruct"
- "RebalanceTimeSeconds"
```
