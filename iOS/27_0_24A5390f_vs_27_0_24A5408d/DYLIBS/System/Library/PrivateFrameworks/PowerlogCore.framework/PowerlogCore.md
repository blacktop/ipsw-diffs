## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`

```diff

-3486.0.81.502.4
-  __TEXT.__text: 0xe7c60
-  __TEXT.__objc_methlist: 0x9758
-  __TEXT.__const: 0x1ba0
-  __TEXT.__cstring: 0x42c16
+3486.2.4.0.0
+  __TEXT.__text: 0xe8568
+  __TEXT.__objc_methlist: 0x97a8
+  __TEXT.__const: 0x1b98
+  __TEXT.__cstring: 0x43086
   __TEXT.__oslogstring: 0x8a24
-  __TEXT.__gcc_except_tab: 0x29f0
-  __TEXT.__unwind_info: 0x30e0
+  __TEXT.__gcc_except_tab: 0x2a38
+  __TEXT.__unwind_info: 0x3108
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5968
+  __DATA_CONST.__objc_selrefs: 0x59a0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2d0
-  __DATA_CONST.__objc_arraydata: 0x43d08
+  __DATA_CONST.__objc_arraydata: 0x441d8
   __DATA_CONST.__got: 0x7e8
-  __AUTH_CONST.__const: 0x24e0
-  __AUTH_CONST.__cfstring: 0x6be60
-  __AUTH_CONST.__objc_const: 0xaa00
+  __AUTH_CONST.__const: 0x2540
+  __AUTH_CONST.__cfstring: 0x6c560
+  __AUTH_CONST.__objc_const: 0xaa30
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x4a70
   __AUTH_CONST.__objc_doubleobj: 0x13a0
   __AUTH_CONST.__objc_arrayobj: 0x1188
-  __AUTH_CONST.__objc_dictobj: 0xf7f8
-  __AUTH_CONST.__auth_got: 0xdb8
+  __AUTH_CONST.__objc_dictobj: 0xf910
+  __AUTH_CONST.__auth_got: 0xdc0
   __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x7cc
+  __DATA.__objc_ivar: 0x7d0
   __DATA.__data: 0x4a0
-  __DATA.__bss: 0x16b1
+  __DATA.__bss: 0x1709
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1e50
   __DATA_DIRTY.__data: 0x28
-  __DATA_DIRTY.__bss: 0x11c0
+  __DATA_DIRTY.__bss: 0x1198
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4940
-  Symbols:   9336
-  CStrings:  15136
+  Functions: 4953
+  Symbols:   9358
+  CStrings:  15193
 
Symbols:
+ +[PLSQLiteConnection tableColumnPresenceCacheSem]
+ +[PLSQLiteConnection tableColumnPresenceCache]
+ +[PLUtilities getHardwarePerfKind:]
+ -[PLContextualizedMetricData reducedAccuracySeconds]
+ -[PLContextualizedMetricData setReducedAccuracySeconds:]
+ -[PLSQLiteConnection clearTableColumnPresenceCache]
+ -[PLSQLiteConnection tableHasColumn:inTable:]
+ GCC_except_table100
+ GCC_except_table107
+ GCC_except_table116
+ GCC_except_table139
+ GCC_except_table141
+ GCC_except_table203
+ _OBJC_IVAR_$_PLContextualizedMetricData._reducedAccuracySeconds
+ ___35+[PLUtilities getHardwarePerfKind:]_block_invoke
+ ___46+[PLSQLiteConnection tableColumnPresenceCache]_block_invoke
+ ___49+[PLSQLiteConnection tableColumnPresenceCacheSem]_block_invoke
+ ___snprintf_chk
+ _getHardwarePerfKind:.cache
+ _getHardwarePerfKind:.cacheOnce
+ _objc_msgSend$clearTableColumnPresenceCache
+ _objc_msgSend$tableColumnPresenceCache
+ _objc_msgSend$tableColumnPresenceCacheSem
+ _objc_msgSend$tableHasColumn:inTable:
+ _tableColumnPresenceCache.onceToken
+ _tableColumnPresenceCache.tableColumnPresenceCache
+ _tableColumnPresenceCacheSem.onceToken
+ _tableColumnPresenceCacheSem.tableColumnPresenceCacheSem
- GCC_except_table101
- GCC_except_table105
- GCC_except_table133
- GCC_except_table72
- GCC_except_table94
- GCC_except_table96
CStrings:
+ "%@|%@|%@"
+ "CPUEnergyM"
+ "CoreSpeech"
+ "DaySinceAccountChange"
+ "DaySinceReset"
+ "DaySinceSetup"
+ "DaySinceUpgrade"
+ "Indexing"
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
+ "RedonationCount"
+ "ReducedAccuracy"
+ "SiriTools"
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
+ "entityCount"
+ "enumCount"
+ "hw.perflevel%u.name"
+ "intentCount"
+ "lmeSlotEntityCount"
+ "lmeSlotUpdatedCount"
+ "profileRebuildCount"
+ "profileRebuildReason"
+ "profileSizeBytes"
+ "rankingEventCount"
+ "rankingEventType"
+ "rankingItemsPerEventAvg"
+ "rankingItemsPerEventMax"
+ "reducedAccuracy"
+ "totalItemCount"
+ "\xf0\xf0Ec"
- "\xf0\xf05c"
```
