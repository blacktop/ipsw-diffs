## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/Versions/A/SpotlightDaemon`

```diff

-2328.7.8.7.0
-  __TEXT.__text: 0x9d794
-  __TEXT.__auth_stubs: 0x1ad0
-  __TEXT.__objc_methlist: 0x36b4
-  __TEXT.__const: 0x310
-  __TEXT.__cstring: 0x7407
-  __TEXT.__gcc_except_tab: 0x3b64
-  __TEXT.__oslogstring: 0x84f3
-  __TEXT.__unwind_info: 0x1eb8
-  __TEXT.__objc_classname: 0x43c
-  __TEXT.__objc_methname: 0xc52a
-  __TEXT.__objc_methtype: 0x2079
-  __TEXT.__objc_stubs: 0x9ee0
-  __DATA_CONST.__got: 0x890
+2333.22.13.7.0
+  __TEXT.__text: 0xa3274
+  __TEXT.__auth_stubs: 0x1b20
+  __TEXT.__objc_methlist: 0x3d94
+  __TEXT.__const: 0x350
+  __TEXT.__cstring: 0x76b4
+  __TEXT.__oslogstring: 0x88df
+  __TEXT.__gcc_except_tab: 0x3c5c
+  __TEXT.__unwind_info: 0x2000
+  __TEXT.__objc_classname: 0x469
+  __TEXT.__objc_methname: 0xcb67
+  __TEXT.__objc_methtype: 0x21cf
+  __TEXT.__objc_stubs: 0xa500
+  __DATA_CONST.__got: 0x8c0
   __DATA_CONST.__const: 0x4a8
-  __DATA_CONST.__objc_classlist: 0x140
+  __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2dd0
+  __DATA_CONST.__objc_selrefs: 0x3078
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x390
-  __AUTH_CONST.__auth_got: 0xd80
-  __AUTH_CONST.__const: 0x4338
-  __AUTH_CONST.__cfstring: 0x62e0
-  __AUTH_CONST.__objc_const: 0x5918
+  __AUTH_CONST.__auth_got: 0xda8
+  __AUTH_CONST.__const: 0x45b8
+  __AUTH_CONST.__cfstring: 0x6580
+  __AUTH_CONST.__objc_const: 0x52c0
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x3b4
+  __AUTH.__objc_data: 0x5f0
+  __DATA.__objc_ivar: 0x3d0
   __DATA.__data: 0x9a0
-  __DATA.__bss: 0x3d0
+  __DATA.__bss: 0x3f8
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x730
-  __DATA_DIRTY.__bss: 0x160
+  __DATA_DIRTY.__bss: 0x170
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: EF7703DD-D9E6-3262-B3DC-5B792606F1F2
-  Functions: 2530
-  Symbols:   5929
-  CStrings:  5016
+  UUID: 44131307-2A9D-3181-9B3E-6ED4344ABB15
+  Functions: 2631
+  Symbols:   6137
+  CStrings:  5160
 
Symbols:
+ +[CSRecieverState sharedInstance].cold.1
+ +[MDAgent sharedAgent].cold.1
+ +[SDMigrationMonitor sharedInstance].cold.1
+ +[SDPommesFeature baseBundleIDs].cold.1
+ +[SDPommesFeature isSearchToolClientBundle:].cold.1
+ +[SDPommesFeature isSpotlightUIClientBundle:]
+ +[SDTraceItem stringFromReferenceDate:].cold.1
+ +[SPConcreteCoreSpotlightIndexer _sharedSynonyms].cold.1
+ +[SPCoreSpotlightContactsUpdater sharedInstance].cold.1
+ +[SPCoreSpotlightIndexer allProtectionClasses].cold.1
+ +[SPCoreSpotlightIndexer loginWindowNotificationInit].cold.1
+ +[SPCoreSpotlightIndexer sharedInstance].cold.1
+ +[SPCoreSpotlightIndexer totalIndexDiskSpace].cold.1
+ +[SPCorrectionHandler sharedHandler].cold.1
+ +[SPHistoricalReportManager sharedInstance]
+ +[SPHistoricalReportManager sharedInstance].cold.1
+ +[SPQueryResultsQueue startTrackingResultsQueue:].cold.1
+ +[SpotlightDaemonServer sharedDaemonServer].cold.1
+ +[SpotlightReceiverConnection setup].cold.1
+ -[CSSearchAgent _prepareQueryContext:searchConnection:].cold.3
+ -[CSSearchClientConnection description]
+ -[CSSearchClientConnectionKey description]
+ -[MDSearchableIndexService _handleAssetsCommand:]
+ -[MDSearchableIndexService fetchBundleIDs:]
+ -[MDSearchableIndexService fetchBundleIDs:].cold.1
+ -[MDSearchableIndexService fetchBundleIDs:].cold.2
+ -[SDLockHandler cxUnlocked]
+ -[SDPommesSynonyms generateDateSynonymsFromToken:previousToken:isOrdinalToken:].cold.1
+ -[SPConcreteCoreSpotlightIndexer _startInternalQueryWithIndex:query:fetchAttributes:forBundleIds:resultsHandler:resultQueue:]
+ -[SPConcreteCoreSpotlightIndexer completeIndexingItemFor:delegate:didBeginThrottle:didEndThrottle:error:live:queue:slow:startTime:dataLen:completionHandler:]
+ -[SPConcreteCoreSpotlightIndexer finishDeleteBatchForQueryQueue:bundleID:blockTime:]
+ -[SPConcreteCoreSpotlightIndexer fixupBundlesWithGroup:]
+ -[SPConcreteCoreSpotlightIndexer onDemandOpen]
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:].cold.1
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:].cold.10
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:].cold.11
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:].cold.12
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:].cold.13
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:].cold.14
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:].cold.15
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:].cold.2
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:].cold.3
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:].cold.4
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:].cold.5
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:].cold.6
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:].cold.7
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:].cold.8
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:].cold.9
+ -[SPConcreteCoreSpotlightIndexer openIndexForUpgradeSynchronous:].cold.3
+ -[SPConcreteCoreSpotlightIndexer readyIndex:].cold.1
+ -[SPConcreteCoreSpotlightIndexer setOnDemandOpen:]
+ -[SPConcreteCoreSpotlightIndexer updateIndexRankingDates:]
+ -[SPConcreteCoreSpotlightIndexer updateKnownBundles:group:]
+ -[SPCoreSpotlightIndexer _enumerateIndexersWithProtectionClasses:forBundleIds:inferSpecialIndexes:block:]
+ -[SPCoreSpotlightIndexer _enumerateIndexersWithProtectionClasses:forQueryWithContext:forBundleIds:inferSpecialIndexes:block:]
+ -[SPCoreSpotlightIndexer _enumerateIndexersWithProtectionClasses:inferSpecialIndexes:block:]
+ -[SPCoreSpotlightIndexer checkMailMigrationToClassCComplete]
+ -[SPCoreSpotlightIndexer fetchBundleIdsForProtectionClass:completionHandler:]
+ -[SPCoreSpotlightIndexer handleAssetsCommand:]
+ -[SPCoreSpotlightIndexer init].cold.6
+ -[SPCoreSpotlightIndexer issueBundleFixup:completionHandler:]
+ -[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]
+ -[SPCoreSpotlightIndexer moveBackMailToClassA]
+ -[SPCoreSpotlightIndexer moveMailToClassCWithoutClone]
+ -[SPCoreSpotlightIndexer moveMailToClassC]
+ -[SPCoreSpotlightIndexer processSearchString:intoTrimmedString:andTokens:].cold.1
+ -[SPCoreSpotlightTask _makeSIQueryWithQueryString:queryContext:].cold.1
+ -[SPCoreSpotlightTask _pommesBundlesWithQueryContext:queryID:]
+ -[SPHistoricalReport .cxx_destruct]
+ -[SPHistoricalReport dictionaryRepresentation]
+ -[SPHistoricalReport initWithDictionary:]
+ -[SPHistoricalReport report]
+ -[SPHistoricalReport setReport:]
+ -[SPHistoricalReport setTimestamp:]
+ -[SPHistoricalReport setType:]
+ -[SPHistoricalReport timestamp]
+ -[SPHistoricalReport type]
+ -[SPHistoricalReportManager .cxx_destruct]
+ -[SPHistoricalReportManager cleanupOldReports]
+ -[SPHistoricalReportManager filenameDateFormatter]
+ -[SPHistoricalReportManager filenameDateFormatter].cold.1
+ -[SPHistoricalReportManager getReportsForDateInterval:reportHandler:]
+ -[SPHistoricalReportManager init]
+ -[SPHistoricalReportManager init].cold.1
+ -[SPHistoricalReportManager saveReport:withType:errorHandler:]
+ -[SPIndexStorageUsageCollector collectAtPath:completionBlock:].cold.1
+ -[SpotlightDaemonServer clientTypeForBundleID:jobType:].cold.1
+ CSRedactString.cold.1
+ CSRedactStringArray.cold.1
+ GCC_except_table1013
+ GCC_except_table1058
+ GCC_except_table1065
+ GCC_except_table107
+ GCC_except_table1106
+ GCC_except_table111
+ GCC_except_table1112
+ GCC_except_table118
+ GCC_except_table119
+ GCC_except_table1274
+ GCC_except_table1277
+ GCC_except_table1278
+ GCC_except_table1279
+ GCC_except_table128
+ GCC_except_table129
+ GCC_except_table132
+ GCC_except_table136
+ GCC_except_table1410
+ GCC_except_table1439
+ GCC_except_table149
+ GCC_except_table150
+ GCC_except_table16
+ GCC_except_table174
+ GCC_except_table175
+ GCC_except_table176
+ GCC_except_table177
+ GCC_except_table178
+ GCC_except_table179
+ GCC_except_table188
+ GCC_except_table190
+ GCC_except_table191
+ GCC_except_table217
+ GCC_except_table219
+ GCC_except_table221
+ GCC_except_table23
+ GCC_except_table232
+ GCC_except_table236
+ GCC_except_table240
+ GCC_except_table273
+ GCC_except_table280
+ GCC_except_table292
+ GCC_except_table320
+ GCC_except_table343
+ GCC_except_table37
+ GCC_except_table372
+ GCC_except_table382
+ GCC_except_table383
+ GCC_except_table408
+ GCC_except_table424
+ GCC_except_table436
+ GCC_except_table439
+ GCC_except_table482
+ GCC_except_table491
+ GCC_except_table51
+ GCC_except_table511
+ GCC_except_table516
+ GCC_except_table526
+ GCC_except_table527
+ GCC_except_table56
+ GCC_except_table579
+ GCC_except_table580
+ GCC_except_table581
+ GCC_except_table61
+ GCC_except_table62
+ GCC_except_table659
+ GCC_except_table680
+ GCC_except_table69
+ GCC_except_table698
+ GCC_except_table70
+ GCC_except_table702
+ GCC_except_table706
+ GCC_except_table73
+ GCC_except_table737
+ GCC_except_table749
+ GCC_except_table760
+ GCC_except_table784
+ GCC_except_table785
+ GCC_except_table793
+ GCC_except_table834
+ GCC_except_table885
+ GCC_except_table921
+ GCC_except_table925
+ GCC_except_table926
+ GCC_except_table93
+ GCC_except_table932
+ GCC_except_table934
+ GCC_except_table940
+ GCC_except_table953
+ GCC_except_table956
+ GCC_except_table966
+ GCC_except_table975
+ GCC_except_table980
+ GCC_except_table985
+ GCC_except_table990
+ GCC_except_table996
+ OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._onDemandOpen
+ OBJC_IVAR_$_SPHistoricalReport._report
+ OBJC_IVAR_$_SPHistoricalReport._timestamp
+ OBJC_IVAR_$_SPHistoricalReport._type
+ OBJC_IVAR_$_SPHistoricalReportManager._queue
+ OBJC_IVAR_$_SPHistoricalReportManager._reportsDirectory
+ OBJC_IVAR_$_SPHistoricalReportManager._retentionDays
+ SDTraceAdd.cold.1
+ SPLogDirectory.cold.1
+ _MDItemInterestingDate
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_SPHistoricalReport
+ _OBJC_CLASS_$_SPHistoricalReportManager
+ _OBJC_METACLASS_$_SPHistoricalReport
+ _OBJC_METACLASS_$_SPHistoricalReportManager
+ _SILogBulkDeleteEvent
+ _SINotifyLowspace
+ _SIUpdateKnownBundles
+ __100-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:completionHandler:]_block_invoke.1594
+ __101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke.1557
+ __105-[SPConcreteCoreSpotlightIndexer willModifySearchableItemsWithIdentifiers:forBundleID:completionHandler:]_block_invoke.1380
+ __107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.3204
+ __108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1525
+ __108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1533
+ __108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1543
+ __108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1547
+ __108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_2.1544
+ __109-[MDSearchableIndexService deleteUserActivitiesWithPersistentIdentifiers:bundleID:options:completionHandler:]_block_invoke.142
+ __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2464
+ __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2468
+ __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2468.cold.1
+ __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2472
+ __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2472.cold.1
+ __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2473
+ __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2473.cold.1
+ __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2474
+ __143-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:force:postFilter:]_block_invoke.255
+ __143-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:force:postFilter:]_block_invoke.256
+ __143-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:force:postFilter:]_block_invoke_2.257
+ __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1321
+ __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1323
+ __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1323.cold.1
+ __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1323.cold.2
+ __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1326
+ __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1326.cold.1
+ __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1326.cold.2
+ __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1329
+ __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke_2.1322
+ __186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1256
+ __186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1256.cold.1
+ __186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1256.cold.2
+ __186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1256.cold.3
+ __186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1256.cold.4
+ __186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1281
+ __186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1294
+ __186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1295
+ __186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1296
+ __28-[CSSearchAgent startQuery:]_block_invoke.167
+ __28-[CSSearchAgent startQuery:]_block_invoke.173
+ __28-[CSSearchAgent startQuery:]_block_invoke.176
+ __28-[CSSearchAgent startQuery:]_block_invoke.182
+ __28-[CSSearchAgent startQuery:]_block_invoke.182.cold.1
+ __28-[CSSearchAgent startQuery:]_block_invoke.185
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2165
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2179
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2183
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2190
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2191
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2194
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2206
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2208
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2208.cold.1
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2209
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2211
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2211.cold.1
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2212
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2214
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2214.cold.1
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2218
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2220
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2221
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2224
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2224.cold.1
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2232
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2232.cold.1
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2232.cold.2
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2233
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2241
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2248
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2248.cold.1
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2249
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2250
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2250.cold.1
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2254
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2265
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2266
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2271
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2271.cold.1
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2271.cold.2
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.2285
+ __30-[SPCoreSpotlightIndexer init]_block_invoke_2.2172
+ __30-[SPCoreSpotlightIndexer init]_block_invoke_2.2242
+ __30-[SPCoreSpotlightIndexer init]_block_invoke_2.2268
+ __30-[SPCoreSpotlightIndexer init]_block_invoke_2.2268.cold.1
+ __30-[SPCoreSpotlightIndexer init]_block_invoke_2.2275
+ __30-[SPCoreSpotlightIndexer init]_block_invoke_3.2276
+ __30-[SPCoreSpotlightIndexer init]_block_invoke_4.2277
+ __31-[SPCoreSpotlightIndexer start]_block_invoke.2313
+ __31-[SPCoreSpotlightIndexer start]_block_invoke.2317
+ __31-[SPCoreSpotlightIndexer start]_block_invoke.2320
+ __31-[SPCoreSpotlightIndexer start]_block_invoke_2.2321
+ __34-[CSSearchAgent startSimpleQuery:]_block_invoke.194
+ __39-[SPCoreSpotlightIndexer queryPreheat:]_block_invoke.2455
+ __40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.431
+ __40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.432
+ __40-[SPCoreSpotlightIndexer issueHeartbeat]_block_invoke.2399
+ __40-[SPCoreSpotlightIndexer issueHeartbeat]_block_invoke.2409
+ __40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.3219
+ __40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.3220
+ __41-[MDSearchableIndexService issueCommand:]_block_invoke.262
+ __41-[MDSearchableIndexService issueCommand:]_block_invoke.262.cold.1
+ __42-[SPCoreSpotlightIndexer handleLikelyExit]_block_invoke.2450
+ __44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2091
+ __44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2091.cold.1
+ __50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke.1359
+ __50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke.1364
+ __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke.526
+ __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke.526.cold.1
+ __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke.529
+ __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke.529.cold.1
+ __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke.530
+ __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke.536
+ __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke_2.540
+ __54-[MDSearchableIndexService _runLibraryDeletedCommand:]_block_invoke.244
+ __57-[SPConcreteCoreSpotlightIndexer zombifyAllContactItems:]_block_invoke.1461
+ __57-[SPConcreteCoreSpotlightIndexer zombifyAllContactItems:]_block_invoke_2.1462
+ __58-[SPConcreteCoreSpotlightIndexer reindexSystemPreferences]_block_invoke.467
+ __58-[SPConcreteCoreSpotlightIndexer reindexSystemPreferences]_block_invoke.468
+ __58-[SPConcreteCoreSpotlightIndexer removeSandboxExtensions:]_block_invoke.1517
+ __58-[SPConcreteCoreSpotlightIndexer removeSandboxExtensions:]_block_invoke_2.1518
+ __58-[SPCoreSpotlightIndexer handleRankingCommand:completion:]_block_invoke.3196
+ __58-[SPCoreSpotlightIndexer handleRankingCommand:completion:]_block_invoke_2.3197
+ __59-[SPConcreteCoreSpotlightIndexer _performXPCActivity:name:]_block_invoke.443
+ __59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.198
+ __59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.199
+ __59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.207
+ __59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.207.cold.1
+ __59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.211
+ __59-[SPCoreSpotlightIndexer issueSharedDocumentAttributeFixup]_block_invoke.2375
+ __60-[SPConcreteCoreSpotlightIndexer _addNewClientWithBundleID:]_block_invoke.1051
+ __60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.218
+ __60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.226
+ __60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.226.cold.1
+ __60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke.1232
+ __60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_2.1235
+ __60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_3.1238
+ __63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.482
+ __63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.482.cold.1
+ __63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.488
+ __63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.488.cold.1
+ __63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.492
+ __65-[SPConcreteCoreSpotlightIndexer openIndexForUpgradeSynchronous:]_block_invoke.904
+ __67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2105
+ __67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2106
+ __68-[SPCoreSpotlightIndexer deleteActionsBeforeTime:completionHandler:]_block_invoke.2567
+ __69-[SPConcreteCoreSpotlightIndexer issueDumpReverse:completionHandler:]_block_invoke.1131
+ __70-[SPConcreteCoreSpotlightIndexer removeExpiredItemsForBundleId:group:]_block_invoke.520
+ __70-[SPConcreteCoreSpotlightIndexer writeDiagnostic:bundleID:identifier:]_block_invoke.1181
+ __70-[SPConcreteCoreSpotlightIndexer writeDiagnostic:bundleID:identifier:]_block_invoke.1191
+ __70-[SPConcreteCoreSpotlightIndexer writeDiagnostic:bundleID:identifier:]_block_invoke_2.1182
+ __70-[SPConcreteCoreSpotlightIndexer writeDiagnostic:bundleID:identifier:]_block_invoke_2.1195
+ __71-[SPConcreteCoreSpotlightIndexer performIndexerTask:completionHandler:]_block_invoke.1056
+ __72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1045
+ __72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1046
+ __73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1478
+ __73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1478.cold.1
+ __73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1482
+ __73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1482.cold.1
+ __73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1485
+ __73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1500
+ __73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1501
+ __73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1507
+ __73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.cold.1
+ __73-[SPCoreSpotlightIndexer deleteActionsWithIdentifiers:completionHandler:]_block_invoke.2572
+ __75-[SPCoreSpotlightIndexer _reindexAllItemsWithExtensionsAndCompletionBlock:]_block_invoke.3236
+ __76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1334
+ __76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1338
+ __76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1351
+ __76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1351.cold.1
+ __76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1339
+ __78-[MDSearchableIndexService performDataMigrationWithTimeout:completionHandler:]_block_invoke.151
+ __78-[MDSearchableIndexService performDataMigrationWithTimeout:completionHandler:]_block_invoke.163
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1002
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1007
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1009
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1009.cold.1
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1013
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1016
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1017
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1018
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1021
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1024
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1032
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1036
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.921
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.932
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.964
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.972
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.972.cold.1
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.997
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.997.cold.1
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1008
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1037
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.925
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.935
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.990
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.990.cold.1
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.938
+ __78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.991
+ __78-[SPConcreteCoreSpotlightIndexer scheduleMaintenance:description:forDarkWake:]_block_invoke.456
+ __78-[SPCoreSpotlightIndexer _reindexAllIdentifiersWithExtension:completionBlock:]_block_invoke.3229
+ __78-[SpotlightDaemonServer handleJob:bundleID:protectionClass:completionHandler:]_block_invoke.27
+ __78-[SpotlightDaemonServer handleJob:bundleID:protectionClass:completionHandler:]_block_invoke_2.29
+ __79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.1096
+ __79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.1097
+ __79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.1112
+ __79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.1112.cold.1
+ __79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_2.1098
+ __79-[SPCoreSpotlightIndexer deleteAllUserActivities:fromClient:completionHandler:]_block_invoke.2562
+ __79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2515
+ __79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2516
+ __79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2517
+ __80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.2360
+ __81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2629
+ __81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2634
+ __81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke_2.2638
+ __84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.188
+ __84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.188.cold.1
+ __84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.188.cold.2
+ __84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.3203
+ __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3133
+ __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3133.cold.1
+ __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3135
+ __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3139
+ __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3139.cold.1
+ __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3140
+ __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3141
+ __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3141.cold.1
+ __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3142
+ __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3146
+ __87-[SPCoreSpotlightIndexer rewriteQueryWithQueryString:context:matchInfo:rewriteHandler:]_block_invoke.2486
+ __89-[SPCoreSpotlightIndexer _reindexAllItemsWithExtensionsAndIdentifiersAndCompletionBlock:]_block_invoke.3245
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2717
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2725
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2745
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2781
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2785
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2789
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2809
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2823
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2836
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3013
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3023
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3026
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3033
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3039
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3040
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3046
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3050
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3069
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2726
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2813
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2837
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3085
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3089
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3120
+ __92-[SPConcreteCoreSpotlightIndexer deleteItemsForQuery:bundleID:fromClient:completionHandler:]_block_invoke.1398
+ __92-[SPConcreteCoreSpotlightIndexer deleteItemsForQuery:bundleID:fromClient:completionHandler:]_block_invoke.1401
+ __92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1060
+ __92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1061
+ __93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2550
+ __93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2556
+ __93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.2557
+ __94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.551
+ __94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.552
+ __94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.553
+ __94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.556
+ __96-[SpotlightDaemonServer handleJob:protectionClass:perClientCompletionHandler:completionHandler:]_block_invoke.77
+ __97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1419
+ __97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1428
+ __97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1428.cold.1
+ __97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1432
+ __97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_2.1433
+ __97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2341
+ __97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2341.cold.1
+ __97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2342
+ __97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2350
+ __97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2355
+ __97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke_2.cold.1
+ __97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke_2.cold.2
+ __OBJC_$_CLASS_METHODS_SPHistoricalReportManager
+ __OBJC_$_INSTANCE_METHODS_SPHistoricalReport
+ __OBJC_$_INSTANCE_METHODS_SPHistoricalReportManager
+ __OBJC_$_INSTANCE_VARIABLES_SPHistoricalReport
+ __OBJC_$_INSTANCE_VARIABLES_SPHistoricalReportManager
+ __OBJC_$_PROP_LIST_SPHistoricalReport
+ __OBJC_CLASS_RO_$_SPHistoricalReport
+ __OBJC_CLASS_RO_$_SPHistoricalReportManager
+ __OBJC_METACLASS_RO_$_SPHistoricalReport
+ __OBJC_METACLASS_RO_$_SPHistoricalReportManager
+ __SIProtectionClass
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEENS5_IS8_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__110__pop_heapB8ne190102INS_17_ClassicAlgPolicyE22_compareTopKCandidatesNS_11__wrap_iterIPNS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEEvT1_SE_RT0_NS_15iterator_traitsISE_E15difference_typeE
+ __ZNSt3__110__pop_heapB8ne190102INS_17_ClassicAlgPolicyE27_compareCorectionCandidatesNS_11__wrap_iterIPNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEEEEEEvT1_SE_RT0_NS_15iterator_traitsISE_E15difference_typeE
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
+ __ZNSt3__114__split_bufferINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEERNS5_IS8_EEE17__destruct_at_endB8ne190102EPS8_
+ __ZNSt3__114__split_bufferINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEERNS_9allocatorIS8_EEE17__destruct_at_endB8ne190102EPS8_
+ __ZNSt3__114priority_queueINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEENS_6vectorIS8_NS5_IS8_EEEE27_compareCorectionCandidatesE4pushEOS8_
+ __ZNSt3__114priority_queueINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_6vectorIS8_NS_9allocatorIS8_EEEE22_compareTopKCandidatesE4pushEOS8_
+ __ZNSt3__117__floyd_sift_downB8ne190102INS_17_ClassicAlgPolicyER22_compareTopKCandidatesNS_11__wrap_iterIPNS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEET1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
+ __ZNSt3__117__floyd_sift_downB8ne190102INS_17_ClassicAlgPolicyER27_compareCorectionCandidatesNS_11__wrap_iterIPNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEEEEEET1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEfEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEENS5_IS8_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEENS5_IS8_EEE7__clearB8ne190102Ev
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE22__base_destruct_at_endB8ne190102EPS8_
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne190102EmRKf
+ __ZNSt3__19__sift_upB8ne190102INS_17_ClassicAlgPolicyER22_compareTopKCandidatesNS_11__wrap_iterIPNS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEEvT1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
+ __ZNSt3__19__sift_upB8ne190102INS_17_ClassicAlgPolicyER27_compareCorectionCandidatesNS_11__wrap_iterIPNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEEEEEEvT1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_6
+ ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_7
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_4
+ ___157-[SPConcreteCoreSpotlightIndexer completeIndexingItemFor:delegate:didBeginThrottle:didEndThrottle:error:live:queue:slow:startTime:dataLen:completionHandler:]_block_invoke
+ ___43+[SPHistoricalReportManager sharedInstance]_block_invoke
+ ___43-[MDSearchableIndexService fetchBundleIDs:]_block_invoke
+ ___50-[SPHistoricalReportManager filenameDateFormatter]_block_invoke
+ ___56-[SPConcreteCoreSpotlightIndexer fixupBundlesWithGroup:]_block_invoke
+ ___56-[SPConcreteCoreSpotlightIndexer fixupBundlesWithGroup:]_block_invoke_2
+ ___59-[SPConcreteCoreSpotlightIndexer updateKnownBundles:group:]_block_invoke
+ ___61-[SPCoreSpotlightIndexer issueBundleFixup:completionHandler:]_block_invoke
+ ___61-[SPCoreSpotlightIndexer issueBundleFixup:completionHandler:]_block_invoke_2
+ ___61-[SPCoreSpotlightIndexer issueBundleFixup:completionHandler:]_block_invoke_3
+ ___62-[SPHistoricalReportManager saveReport:withType:errorHandler:]_block_invoke
+ ___69-[SPHistoricalReportManager getReportsForDateInterval:reportHandler:]_block_invoke
+ ___77-[SPCoreSpotlightIndexer fetchBundleIdsForProtectionClass:completionHandler:]_block_invoke
+ ___77-[SPCoreSpotlightIndexer fetchBundleIdsForProtectionClass:completionHandler:]_block_invoke_2
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3
+ ___84-[SPConcreteCoreSpotlightIndexer finishDeleteBatchForQueryQueue:bundleID:blockTime:]_block_invoke
+ ___88-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithPersonaIds:completionHandler:]_block_invoke_5
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_17
+ ___92-[SPConcreteCoreSpotlightIndexer deleteItemsForQuery:bundleID:fromClient:completionHandler:]_block_invoke_5
+ ___95-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsSinceDate:forBundleID:completionHandler:]_block_invoke
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke_2
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96s_e5_v8?0l
+ ___block_descriptor_123_e8_32s40s48s56s64bs72r80r88w_e17_v16?0"NSError"8l
+ ___block_descriptor_136_e8_32s40s48r56r64r72r80r_e20_v20?0"NSError"8B16l
+ ___block_descriptor_138_e8_32s40s48s56s64s72s80s88s96s104s112bs_e5_v8?0l
+ ___block_descriptor_152_e8_32s40s48s56s64s72r80r88r96r104r112w_e69_v48?0"SPQueryJob"8q16Q24^{__MDStoreOIDArray=}32^{__MDPlistBytes=}40l
+ ___block_descriptor_178_e8_32s40s48s56s64s72s80s88s96s104s112s120s128bs136w_e18_v20?0^{__SI=}8C16l
+ ___block_descriptor_32_e42_v48?0^{__CFString=}8B16B20q24q32?<v?>40l
+ ___block_descriptor_40_e8_32bs_e20_v20?0"NSError"8B16l
+ ___block_descriptor_40_e8_32r_e8_v16?0d8l
+ ___block_descriptor_40_e8_32s_e20_v20?0"NSError"8B16l
+ ___block_descriptor_48_e8_32s40s_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0l
+ ___block_descriptor_60_e8_32s40s48s_e18_v20?0^{__SI=}8C16l
+ ___block_descriptor_64_e8_32s40r48r_e21_v32?0I8S12^q16I24I28l
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0l
+ ___block_descriptor_68_e8_32s40s48s56bs_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56bs_e22_v20?0^{__CFData=}8B16l
+ ___block_descriptor_72_e8_32s40s48s56s_e18_v20?0^{__SI=}8C16l
+ ___block_descriptor_80_e8_32s40s48s56s64r_e69_v48?0"SPQueryJob"8q16Q24^{__MDStoreOIDArray=}32^{__MDPlistBytes=}40l
+ ___block_descriptor_80_e8_32s40s48s_e31_v16?0"BGRepeatingSystemTask"8l
+ ___block_descriptor_81_e8_32s40s48s56s64bs_e18_v20?0^{__SI=}8C16l
+ ___block_descriptor_84_e8_32s40s48s56s64r72r_e17_v16?0"NSError"8l
+ ___block_descriptor_88_e8_32s40s48s56s64r72r_e69_v48?0"SPQueryJob"8q16Q24^{__MDStoreOIDArray=}32^{__MDPlistBytes=}40l
+ ___block_descriptor_88_e8_32s40s48s56s64r_e18_v20?0^{__SI=}8C16l
+ ___block_descriptor_92_e8_32s40s48s56s64s72s80r_e17_v16?0"NSError"8l
+ ___block_descriptor_96_e8_32s40s48s56r64r72r_e5_v8?0l
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e18_v20?0^{__SI=}8C16l
+ ___copy_helper_block_e8_32s40s48r56r64r72r80r
+ ___copy_helper_block_e8_32s40s48s56s64s72r80r88r96r104r112w
+ ___copy_helper_block_e8_32s40s48s56s64s72s80r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s
+ ___destroy_helper_block_e8_32s40s48r56r64r72r80r
+ ___destroy_helper_block_e8_32s40s48s56s64s72r80r88r96r104r112w
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s
+ __block_literal_global.1015
+ __block_literal_global.1020
+ __block_literal_global.1023
+ __block_literal_global.1026
+ __block_literal_global.1034
+ __block_literal_global.1225
+ __block_literal_global.1228
+ __block_literal_global.1234
+ __block_literal_global.1237
+ __block_literal_global.1240
+ __block_literal_global.1283
+ __block_literal_global.1298
+ __block_literal_global.1325
+ __block_literal_global.1328
+ __block_literal_global.154
+ __block_literal_global.1614
+ __block_literal_global.1626
+ __block_literal_global.190
+ __block_literal_global.2067
+ __block_literal_global.2072
+ __block_literal_global.2082
+ __block_literal_global.2087
+ __block_literal_global.2108
+ __block_literal_global.2110
+ __block_literal_global.2112
+ __block_literal_global.2115
+ __block_literal_global.2126
+ __block_literal_global.2137
+ __block_literal_global.2185
+ __block_literal_global.220
+ __block_literal_global.222
+ __block_literal_global.2270
+ __block_literal_global.2274
+ __block_literal_global.2334
+ __block_literal_global.2336
+ __block_literal_global.2340
+ __block_literal_global.2362
+ __block_literal_global.243
+ __block_literal_global.2432
+ __block_literal_global.2437
+ __block_literal_global.2439
+ __block_literal_global.2443
+ __block_literal_global.2449
+ __block_literal_global.2452
+ __block_literal_global.2457
+ __block_literal_global.246
+ __block_literal_global.2504
+ __block_literal_global.2543
+ __block_literal_global.2559
+ __block_literal_global.260
+ __block_literal_global.2665
+ __block_literal_global.2955
+ __block_literal_global.2960
+ __block_literal_global.2965
+ __block_literal_global.2970
+ __block_literal_global.2975
+ __block_literal_global.2980
+ __block_literal_global.2985
+ __block_literal_global.3152
+ __block_literal_global.32
+ __block_literal_global.3218
+ __block_literal_global.3239
+ __block_literal_global.3780
+ __block_literal_global.3819
+ __block_literal_global.3827
+ __block_literal_global.3863
+ __block_literal_global.3870
+ __block_literal_global.45
+ __block_literal_global.480
+ __block_literal_global.522
+ __block_literal_global.75
+ __block_literal_global.874
+ __block_literal_global.895
+ __block_literal_global.898
+ __block_literal_global.900
+ __block_literal_global.923
+ __block_literal_global.928
+ __block_literal_global.934
+ __block_literal_global.937
+ __block_literal_global.940
+ __block_literal_global.974
+ _flock
+ _fsync
+ _memcpy
+ _objc_msgSend$_enumerateIndexersWithProtectionClasses:forBundleIds:inferSpecialIndexes:block:
+ _objc_msgSend$_enumerateIndexersWithProtectionClasses:forQueryWithContext:forBundleIds:inferSpecialIndexes:block:
+ _objc_msgSend$_enumerateIndexersWithProtectionClasses:inferSpecialIndexes:block:
+ _objc_msgSend$_handleAssetsCommand:
+ _objc_msgSend$_pommesBundlesWithQueryContext:queryID:
+ _objc_msgSend$_startInternalQueryWithIndex:query:fetchAttributes:forBundleIds:resultsHandler:resultQueue:
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$checkAdmission:background:didBeginThrottle:didEndThrottle:live:slow:memoryPressure:
+ _objc_msgSend$cleanupOldReports
+ _objc_msgSend$completeIndexingItemFor:delegate:didBeginThrottle:didEndThrottle:error:live:queue:slow:startTime:dataLen:completionHandler:
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$dateFromString:
+ _objc_msgSend$dictionaryRepresentation
+ _objc_msgSend$endDate
+ _objc_msgSend$fetchAllParametersForLanguages:
+ _objc_msgSend$fetchBundleIDs:
+ _objc_msgSend$fetchBundleIdsForProtectionClass:completionHandler:
+ _objc_msgSend$filenameDateFormatter
+ _objc_msgSend$filterOutHiddenApps
+ _objc_msgSend$finishDeleteBatchForQueryQueue:bundleID:blockTime:
+ _objc_msgSend$fixupBundlesWithGroup:
+ _objc_msgSend$handleAssetsCommand:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$isPhotosBundle:
+ _objc_msgSend$isPriority
+ _objc_msgSend$isSpotlightUIClientBundle:
+ _objc_msgSend$issueBundleFixup:completionHandler:
+ _objc_msgSend$lengthOfBytesUsingEncoding:
+ _objc_msgSend$localeWithLocaleIdentifier:
+ _objc_msgSend$mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:
+ _objc_msgSend$mutableBytes
+ _objc_msgSend$openIndex:shouldReindexAll:readOnly:forcePC:
+ _objc_msgSend$report
+ _objc_msgSend$resourcePath
+ _objc_msgSend$saveReport:withType:errorHandler:
+ _objc_msgSend$setByAddingObjectsFromArray:
+ _objc_msgSend$setExpectedDuration:
+ _objc_msgSend$setGroupConcurrencyLimit:
+ _objc_msgSend$setGroupName:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$setPriority:
+ _objc_msgSend$setReport:
+ _objc_msgSend$setRequiresExternalPower:
+ _objc_msgSend$setRequiresNetworkConnectivity:
+ _objc_msgSend$setRequiresProtectionClass:
+ _objc_msgSend$setRequiresUserInactivity:
+ _objc_msgSend$setResourceIntensive:
+ _objc_msgSend$setResources:
+ _objc_msgSend$setTimestamp:
+ _objc_msgSend$setType:
+ _objc_msgSend$startDate
+ _objc_msgSend$submitTaskRequest:error:
+ _objc_msgSend$textContentSummary
+ _objc_msgSend$timestamp
+ _objc_msgSend$updateIndexRankingDates:
+ _objc_msgSend$updateKnownBundles:group:
+ _read
+ _sMailProtectionClass
+ filenameDateFormatter.formatter
+ filenameDateFormatter.onceToken
+ getSystemVersionString.cold.1
+ kSPReindexAllCompletedBundleIDs_block_invoke_4.queueNum
+ kSPReindexAllCompletedBundleIDs_block_invoke_5.queueNum
+ kSPReindexAllCompletedBundleIDs_block_invoke_6.queueNum
+ logForCSLogCategoryDaemonClient.cold.1
+ logForCSLogCategoryDefault.cold.1
+ logForCSLogCategoryIndex.cold.1
+ logForCSLogCategoryPersonalization.cold.1
+ logForCSLogCategoryPhotosQU.cold.1
+ logForCSLogCategoryQuery.cold.1
+ logForCSLogCategoryRecs.cold.1
+ logForCSLogCategoryUA.cold.1
+ openIndex:shouldReindexAll:readOnly:forcePC:.onceToken
- -[SPConcreteCoreSpotlightIndexer completeIndexingItemFor:delegate:didBeginThrottle:didEndThrottle:error:live:queue:slow:startTime:completionHandler:]
- -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:].cold.1
- -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:].cold.10
- -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:].cold.2
- -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:].cold.3
- -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:].cold.4
- -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:].cold.5
- -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:].cold.6
- -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:].cold.7
- -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:].cold.8
- -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:].cold.9
- -[SPCoreSpotlightIndexer _enumerateIndexersWithProtectionClasses:forBundleIds:inferPriorityIndex:block:]
- -[SPCoreSpotlightIndexer _enumerateIndexersWithProtectionClasses:inferPriorityIndex:block:]
- -[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]
- -[SPCoreSpotlightTask _pommesBundlesWithQueryContext:]
- GCC_except_table1012
- GCC_except_table1014
- GCC_except_table1019
- GCC_except_table106
- GCC_except_table1066
- GCC_except_table108
- GCC_except_table114
- GCC_except_table115
- GCC_except_table116
- GCC_except_table122
- GCC_except_table1228
- GCC_except_table123
- GCC_except_table1236
- GCC_except_table1237
- GCC_except_table1238
- GCC_except_table124
- GCC_except_table133
- GCC_except_table134
- GCC_except_table1346
- GCC_except_table135
- GCC_except_table137
- GCC_except_table1373
- GCC_except_table141
- GCC_except_table142
- GCC_except_table154
- GCC_except_table155
- GCC_except_table182
- GCC_except_table184
- GCC_except_table185
- GCC_except_table211
- GCC_except_table213
- GCC_except_table215
- GCC_except_table22
- GCC_except_table226
- GCC_except_table229
- GCC_except_table233
- GCC_except_table265
- GCC_except_table272
- GCC_except_table284
- GCC_except_table312
- GCC_except_table335
- GCC_except_table364
- GCC_except_table374
- GCC_except_table375
- GCC_except_table38
- GCC_except_table40
- GCC_except_table400
- GCC_except_table416
- GCC_except_table42
- GCC_except_table426
- GCC_except_table45
- GCC_except_table46
- GCC_except_table465
- GCC_except_table473
- GCC_except_table490
- GCC_except_table502
- GCC_except_table503
- GCC_except_table54
- GCC_except_table552
- GCC_except_table553
- GCC_except_table554
- GCC_except_table57
- GCC_except_table60
- GCC_except_table631
- GCC_except_table652
- GCC_except_table67
- GCC_except_table670
- GCC_except_table674
- GCC_except_table678
- GCC_except_table68
- GCC_except_table704
- GCC_except_table71
- GCC_except_table714
- GCC_except_table722
- GCC_except_table746
- GCC_except_table747
- GCC_except_table75
- GCC_except_table755
- GCC_except_table792
- GCC_except_table843
- GCC_except_table879
- GCC_except_table883
- GCC_except_table884
- GCC_except_table89
- GCC_except_table890
- GCC_except_table891
- GCC_except_table892
- GCC_except_table898
- GCC_except_table911
- GCC_except_table914
- GCC_except_table924
- GCC_except_table938
- GCC_except_table943
- GCC_except_table948
- GCC_except_table954
- GCC_except_table968
- _OUTLINED_FUNCTION_42
- _OUTLINED_FUNCTION_43
- _OUTLINED_FUNCTION_44
- _OUTLINED_FUNCTION_45
- _OUTLINED_FUNCTION_46
- _OUTLINED_FUNCTION_47
- _OUTLINED_FUNCTION_48
- _OUTLINED_FUNCTION_49
- _OUTLINED_FUNCTION_50
- __101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke.1497
- __105-[SPConcreteCoreSpotlightIndexer willModifySearchableItemsWithIdentifiers:forBundleID:completionHandler:]_block_invoke.1354
- __107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.3120
- __108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1467
- __108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1473
- __108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1483
- __108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1487
- __108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_2.1484
- __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2391
- __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2393
- __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2393.cold.1
- __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2397
- __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2397.cold.1
- __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2398
- __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2398.cold.1
- __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2399
- __143-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:force:postFilter:]_block_invoke.243
- __143-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:force:postFilter:]_block_invoke.250
- __143-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:force:postFilter:]_block_invoke_2.251
- __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1274
- __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1274.cold.1
- __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1274.cold.2
- __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1295
- __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1297
- __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1297.cold.1
- __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1297.cold.2
- __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1303
- __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke_2.1296
- __186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1230
- __186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1230.cold.1
- __186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1230.cold.2
- __186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1230.cold.3
- __186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1255
- __186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1268
- __186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1269
- __186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1270
- __28-[CSSearchAgent startQuery:]_block_invoke.160
- __28-[CSSearchAgent startQuery:]_block_invoke.166
- __28-[CSSearchAgent startQuery:]_block_invoke.169
- __28-[CSSearchAgent startQuery:]_block_invoke.171
- __28-[CSSearchAgent startQuery:]_block_invoke.175
- __28-[CSSearchAgent startQuery:]_block_invoke.175.cold.1
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2089
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2103
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2107
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2114
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2115
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2118
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2130
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2132
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2132.cold.1
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2133
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2135
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2135.cold.1
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2136
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2138
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2138.cold.1
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2143
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2145
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2146
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2149
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2149.cold.1
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2161
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2161.cold.1
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2161.cold.2
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2162
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2167
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2174
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2174.cold.1
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2175
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2176
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2176.cold.1
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2180
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2193
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2193.cold.1
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2193.cold.2
- __30-[SPCoreSpotlightIndexer init]_block_invoke.2207
- __30-[SPCoreSpotlightIndexer init]_block_invoke_2.2096
- __30-[SPCoreSpotlightIndexer init]_block_invoke_2.2168
- __30-[SPCoreSpotlightIndexer init]_block_invoke_2.2197
- __30-[SPCoreSpotlightIndexer init]_block_invoke_3.2198
- __30-[SPCoreSpotlightIndexer init]_block_invoke_4.2199
- __31-[SPCoreSpotlightIndexer start]_block_invoke.2234
- __31-[SPCoreSpotlightIndexer start]_block_invoke.2239
- __34-[CSSearchAgent startSimpleQuery:]_block_invoke.187
- __39-[SPCoreSpotlightIndexer queryPreheat:]_block_invoke.2379
- __40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.419
- __40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.420
- __40-[SPCoreSpotlightIndexer issueHeartbeat]_block_invoke.2317
- __40-[SPCoreSpotlightIndexer issueHeartbeat]_block_invoke.2327
- __40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.3135
- __40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.3136
- __41-[MDSearchableIndexService issueCommand:]_block_invoke.251
- __41-[MDSearchableIndexService issueCommand:]_block_invoke.251.cold.1
- __42-[SPCoreSpotlightIndexer handleLikelyExit]_block_invoke.2371
- __44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2015
- __44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2015.cold.1
- __50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke.1333
- __50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke.1338
- __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke.506
- __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke.506.cold.1
- __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke.509
- __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke.509.cold.1
- __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke.510
- __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke.516
- __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke_2.520
- __54-[MDSearchableIndexService _runLibraryDeletedCommand:]_block_invoke.232
- __57-[SPConcreteCoreSpotlightIndexer zombifyAllContactItems:]_block_invoke.1422
- __57-[SPConcreteCoreSpotlightIndexer zombifyAllContactItems:]_block_invoke_2.1423
- __58-[SPConcreteCoreSpotlightIndexer reindexSystemPreferences]_block_invoke.455
- __58-[SPConcreteCoreSpotlightIndexer reindexSystemPreferences]_block_invoke.456
- __58-[SPConcreteCoreSpotlightIndexer removeSandboxExtensions:]_block_invoke.1459
- __58-[SPConcreteCoreSpotlightIndexer removeSandboxExtensions:]_block_invoke_2.1460
- __58-[SPCoreSpotlightIndexer handleRankingCommand:completion:]_block_invoke.3112
- __58-[SPCoreSpotlightIndexer handleRankingCommand:completion:]_block_invoke_2.3113
- __59-[SPConcreteCoreSpotlightIndexer _performXPCActivity:name:]_block_invoke.431
- __59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.192
- __59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.193
- __59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.201
- __59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.201.cold.1
- __59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.205
- __59-[SPCoreSpotlightIndexer issueSharedDocumentAttributeFixup]_block_invoke.2293
- __60-[SPConcreteCoreSpotlightIndexer _addNewClientWithBundleID:]_block_invoke.1027
- __60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.212
- __60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.220
- __60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.220.cold.1
- __60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke.1208
- __60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_2.1211
- __60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_3.1214
- __63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.470
- __63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.470.cold.1
- __63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.476
- __63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.476.cold.1
- __63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.480
- __65-[SPConcreteCoreSpotlightIndexer openIndexForUpgradeSynchronous:]_block_invoke.886
- __67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2029
- __67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2030
- __68-[SPCoreSpotlightIndexer deleteActionsBeforeTime:completionHandler:]_block_invoke.2491
- __69-[SPConcreteCoreSpotlightIndexer issueDumpReverse:completionHandler:]_block_invoke.1107
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.1000
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.1008
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.1012
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.903
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.914
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.943
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.951
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.951.cold.1
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.976
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.976.cold.1
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.981
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.986
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.988
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.988.cold.1
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.993
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.994
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.997
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.1013
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.907
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.917
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.969
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.969.cold.1
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.987
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.992
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_3.920
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_3.970
- __70-[SPConcreteCoreSpotlightIndexer removeExpiredItemsForBundleId:group:]_block_invoke.500
- __70-[SPConcreteCoreSpotlightIndexer writeDiagnostic:bundleID:identifier:]_block_invoke.1157
- __70-[SPConcreteCoreSpotlightIndexer writeDiagnostic:bundleID:identifier:]_block_invoke.1167
- __70-[SPConcreteCoreSpotlightIndexer writeDiagnostic:bundleID:identifier:]_block_invoke_2.1158
- __70-[SPConcreteCoreSpotlightIndexer writeDiagnostic:bundleID:identifier:]_block_invoke_2.1171
- __71-[SPConcreteCoreSpotlightIndexer performIndexerTask:completionHandler:]_block_invoke.1032
- __72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1021
- __72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1022
- __73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1432
- __73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1432.cold.1
- __73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1433
- __73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1448
- __73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1451
- __73-[SPCoreSpotlightIndexer deleteActionsWithIdentifiers:completionHandler:]_block_invoke.2496
- __75-[SPCoreSpotlightIndexer _reindexAllItemsWithExtensionsAndCompletionBlock:]_block_invoke.3152
- __76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1308
- __76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1312
- __76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1325
- __76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1325.cold.1
- __76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1313
- __78-[MDSearchableIndexService performDataMigrationWithTimeout:completionHandler:]_block_invoke.147
- __78-[MDSearchableIndexService performDataMigrationWithTimeout:completionHandler:]_block_invoke.159
- __78-[SPConcreteCoreSpotlightIndexer scheduleMaintenance:description:forDarkWake:]_block_invoke.444
- __78-[SPCoreSpotlightIndexer _reindexAllIdentifiersWithExtension:completionBlock:]_block_invoke.3145
- __78-[SpotlightDaemonServer handleJob:bundleID:protectionClass:completionHandler:]_block_invoke.24
- __78-[SpotlightDaemonServer handleJob:bundleID:protectionClass:completionHandler:]_block_invoke_2.26
- __79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.1072
- __79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.1073
- __79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.1088
- __79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.1088.cold.1
- __79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_2.1074
- __79-[SPCoreSpotlightIndexer deleteAllUserActivities:fromClient:completionHandler:]_block_invoke.2486
- __79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2442
- __79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2443
- __79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2444
- __80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.2278
- __81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2553
- __81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2558
- __81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke_2.2562
- __84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.182
- __84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.182.cold.1
- __84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.182.cold.2
- __84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.3119
- __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3049
- __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3049.cold.1
- __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3051
- __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3055
- __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3055.cold.1
- __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3056
- __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3057
- __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3057.cold.1
- __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3058
- __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3062
- __87-[SPCoreSpotlightIndexer rewriteQueryWithQueryString:context:matchInfo:rewriteHandler:]_block_invoke.2413
- __89-[SPCoreSpotlightIndexer _reindexAllItemsWithExtensionsAndIdentifiersAndCompletionBlock:]_block_invoke.3161
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2641
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2649
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2669
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2702
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2706
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2710
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2730
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2744
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2757
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2929
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2939
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2942
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2949
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2955
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2956
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2962
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2966
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2985
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2650
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2734
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2758
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3001
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3005
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3036
- __92-[SPConcreteCoreSpotlightIndexer deleteItemsForQuery:bundleID:fromClient:completionHandler:]_block_invoke.1365
- __92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1036
- __92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1037
- __93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2477
- __93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2480
- __93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.2481
- __94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.531
- __94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.532
- __94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.533
- __94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.536
- __96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.2259
- __96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.2259.cold.1
- __96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.2260
- __96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.2268
- __96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.2273
- __96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke_2.cold.1
- __96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke_2.cold.2
- __96-[SpotlightDaemonServer handleJob:protectionClass:perClientCompletionHandler:completionHandler:]_block_invoke.74
- __97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1383
- __97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1393
- __97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_2.1394
- __97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_3.cold.1
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEfEEEENS_16reverse_iteratorIPS8_EEEclB8ne180100Ev
- __ZNKSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEENS5_IS8_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__110__pop_heapB8ne180100INS_17_ClassicAlgPolicyE22_compareTopKCandidatesNS_11__wrap_iterIPNS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEEvT1_SE_RT0_NS_15iterator_traitsISE_E15difference_typeE
- __ZNSt3__110__pop_heapB8ne180100INS_17_ClassicAlgPolicyE27_compareCorectionCandidatesNS_11__wrap_iterIPNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEEEEEEvT1_SE_RT0_NS_15iterator_traitsISE_E15difference_typeE
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100ILi0EEEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
- __ZNSt3__114__split_bufferINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEERNS5_IS8_EEE17__destruct_at_endB8ne180100EPS8_
- __ZNSt3__114__split_bufferINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEERNS_9allocatorIS8_EEE17__destruct_at_endB8ne180100EPS8_
- __ZNSt3__117__floyd_sift_downB8ne180100INS_17_ClassicAlgPolicyER22_compareTopKCandidatesNS_11__wrap_iterIPNS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEET1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
- __ZNSt3__117__floyd_sift_downB8ne180100INS_17_ClassicAlgPolicyER27_compareCorectionCandidatesNS_11__wrap_iterIPNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEEEEEET1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEfEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ne180100INS_9allocatorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEfEEEENS_16reverse_iteratorIPS8_EESC_SC_EET2_RT_T0_T1_SD_
- __ZNSt3__14pairIU8__strongP8NSStringU8__strongP8NSNumberEaSB8ne180100ERKS7_
- __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEENS5_IS8_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEENS5_IS8_EEE21__push_back_slow_pathIRKS8_EEPS8_OT_
- __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEENS5_IS8_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS8_RS9_EE
- __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEENS5_IS8_EEE7__clearB8ne180100Ev
- __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE21__push_back_slow_pathIRKS8_EEPS8_OT_
- __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE22__base_destruct_at_endB8ne180100EPS8_
- __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS8_RSA_EE
- __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2EmRKf
- __ZNSt3__19__sift_upB8ne180100INS_17_ClassicAlgPolicyER22_compareTopKCandidatesNS_11__wrap_iterIPNS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEEvT1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
- __ZNSt3__19__sift_upB8ne180100INS_17_ClassicAlgPolicyER27_compareCorectionCandidatesNS_11__wrap_iterIPNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEEEEEEvT1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- __ZSt9terminatev
- ___149-[SPConcreteCoreSpotlightIndexer completeIndexingItemFor:delegate:didBeginThrottle:didEndThrottle:error:live:queue:slow:startTime:completionHandler:]_block_invoke
- ___31-[SPCoreSpotlightIndexer start]_block_invoke_3
- ___31-[SPCoreSpotlightIndexer start]_block_invoke_4
- ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke
- ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2
- ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_3
- ___96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke
- ___96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke_2
- ___block_descriptor_104_e8_32s40s48s56r64r72w_e69_v48?0"SPQueryJob"8q16Q24^{__MDStoreOIDArray=}32^{__MDPlistBytes=}40l
- ___block_descriptor_115_e8_32s40s48s56s64bs72r80r88w_e17_v16?0"NSError"8l
- ___block_descriptor_130_e8_32s40s48s56s64s72s80s88s96s104s112bs_e5_v8?0l
- ___block_descriptor_136_e8_32s40s48s56s64s72s80s_e17_v16?0"NSError"8l
- ___block_descriptor_170_e8_32s40s48s56s64s72s80s88s96s104s112s120s128bs136w_e18_v20?0^{__SI=}8C16l
- ___block_descriptor_32_e39_v40?0^{__CFString=}8B16B20q24?<v?>32l
- ___block_descriptor_56_e8_32s40s_e18_v20?0^{__SI=}8C16l
- ___block_descriptor_64_e8_32s40s48bs_e22_v20?0^{__CFData=}8B16l
- ___block_descriptor_64_e8_32s40s48r56r_e17_v16?0"NSError"8l
- ___block_descriptor_64_e8_32s40s48r_e18_v20?0^{__SI=}8C16l
- ___block_descriptor_64_e8_32s40s48s56r_e17_v16?0"NSError"8l
- ___block_descriptor_72_e8_32s40s48r_e5_v8?0l
- ___block_descriptor_72_e8_32s40s48s56r_e69_v48?0"SPQueryJob"8q16Q24^{__MDStoreOIDArray=}32^{__MDPlistBytes=}40l
- ___block_descriptor_73_e8_32s40s48s56bs_e18_v20?0^{__SI=}8C16l
- ___block_descriptor_80_e8_32s40s48s56r64r_e69_v48?0"SPQueryJob"8q16Q24^{__MDStoreOIDArray=}32^{__MDPlistBytes=}40l
- ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e18_v20?0^{__SI=}8C16l
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e5_v8?0l
- ___clang_call_terminate
- ___cxa_begin_catch
- __block_literal_global.1002
- __block_literal_global.1010
- __block_literal_global.1201
- __block_literal_global.1204
- __block_literal_global.1210
- __block_literal_global.1213
- __block_literal_global.1216
- __block_literal_global.1257
- __block_literal_global.1272
- __block_literal_global.1299
- __block_literal_global.1302
- __block_literal_global.150
- __block_literal_global.1552
- __block_literal_global.1565
- __block_literal_global.184
- __block_literal_global.1991
- __block_literal_global.1996
- __block_literal_global.2006
- __block_literal_global.2011
- __block_literal_global.2032
- __block_literal_global.2034
- __block_literal_global.2036
- __block_literal_global.2039
- __block_literal_global.2050
- __block_literal_global.2061
- __block_literal_global.2109
- __block_literal_global.214
- __block_literal_global.216
- __block_literal_global.2196
- __block_literal_global.2252
- __block_literal_global.2254
- __block_literal_global.2258
- __block_literal_global.2280
- __block_literal_global.231
- __block_literal_global.234
- __block_literal_global.2350
- __block_literal_global.2358
- __block_literal_global.2360
- __block_literal_global.2364
- __block_literal_global.2370
- __block_literal_global.2373
- __block_literal_global.2381
- __block_literal_global.2431
- __block_literal_global.2470
- __block_literal_global.2483
- __block_literal_global.254
- __block_literal_global.2589
- __block_literal_global.2876
- __block_literal_global.2881
- __block_literal_global.2886
- __block_literal_global.2891
- __block_literal_global.2896
- __block_literal_global.29
- __block_literal_global.2901
- __block_literal_global.3068
- __block_literal_global.3134
- __block_literal_global.3155
- __block_literal_global.3685
- __block_literal_global.3724
- __block_literal_global.3732
- __block_literal_global.3768
- __block_literal_global.3775
- __block_literal_global.468
- __block_literal_global.502
- __block_literal_global.69
- __block_literal_global.856
- __block_literal_global.877
- __block_literal_global.880
- __block_literal_global.882
- __block_literal_global.905
- __block_literal_global.910
- __block_literal_global.916
- __block_literal_global.919
- __block_literal_global.922
- __block_literal_global.953
- __block_literal_global.978
- __block_literal_global.996
- _objc_msgSend$_enumerateIndexersWithProtectionClasses:forBundleIds:inferPriorityIndex:block:
- _objc_msgSend$_enumerateIndexersWithProtectionClasses:inferPriorityIndex:block:
- _objc_msgSend$_pommesBundlesWithQueryContext:
- _objc_msgSend$completeIndexingItemFor:delegate:didBeginThrottle:didEndThrottle:error:live:queue:slow:startTime:completionHandler:
- _objc_msgSend$fetchAllParametersForLanguages:resourcePath:
- _objc_msgSend$isSearchCLIBundle:
- _objc_msgSend$mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:
- openIndex:shouldReindexAll:readOnly:.onceToken
CStrings:
+ "### fixupBundles %@ - %@"
+ "### fixupBundles complete"
+ "### fixupBundles found %@ - %@"
+ "### fixupBundles starting %@ %@"
+ "%@_type%d.json"
+ "/Library/Spotlight/CoreSpotlight/HistoricalReports"
+ "2333.22.13.7"
+ "@\"NSDate\""
+ "@_kMDItemBundleID=*"
+ "Attempted to recreate search connection for existing connection:%@ key:%@"
+ "B64@0:8^{__SI=}16@24@32@40@48@56"
+ "CSSearchClientConnection bundleID:%@, protectionClass:%@, conn:%@"
+ "Can't open index as part of readying the index, dataclass:%@"
+ "Error creating historical reports directory: %@"
+ "Fail to save app usage report. Error: %@"
+ "Failed to expire restartAttachmentImport task with error: %@"
+ "Handle job type %ld from %@ (pc: %@)"
+ "Ignoring job:%@ with spotlight daemon clients, excludedBundleIDs:%@"
+ "Index open, result:%d, dataclass:%@, shouldReindexAll:%@, forcePC:%@ createCount:%lu"
+ "SPHistoricalReport"
+ "SPHistoricalReportManager"
+ "Slow client state fetch reply by %f seconds"
+ "T@\"NSDate\",&,V_timestamp"
+ "T@\"NSDictionary\",&,V_report"
+ "TB,N,V_onDemandOpen"
+ "TI,V_type"
+ "Throttling indexing reply for %@ by %g s (%g s) (%s) (%lu)"
+ "[%@] Failed to submit the BGST task with error: %@"
+ "[6i]"
+ "[qid=%llu] QoS _mSIQWQS: %d prio: %lld"
+ "[qid=%llu] _mSIQWQS: pRB#: %lu, pR: %@, wQO: %@"
+ "[qid=%llu] _pBWQC: uP: %@, iPB: %@"
+ "[qid=%llu] _pBWQC: uP: YES"
+ "_enumerateIndexersWithProtectionClasses:forBundleIds:inferSpecialIndexes:block:"
+ "_enumerateIndexersWithProtectionClasses:forQueryWithContext:forBundleIds:inferSpecialIndexes:block:"
+ "_enumerateIndexersWithProtectionClasses:inferSpecialIndexes:block:"
+ "_handleAssetsCommand:"
+ "_kMDItemIndexRankingDateSeconds=0"
+ "_onDemandOpen"
+ "_pommesBundlesWithQueryContext:queryID:"
+ "_report"
+ "_reportsDirectory"
+ "_retentionDays"
+ "_startInternalQueryWithIndex:query:fetchAttributes:forBundleIds:resultsHandler:resultQueue:"
+ "_timestamp"
+ "_type"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "bulk"
+ "bundlefixup"
+ "checkMailMigrationToClassCComplete"
+ "cleanupOldReports"
+ "com.apple.search.framework"
+ "com.apple.searchd.internal.attachmentImports.%d"
+ "com.apple.searchd.internal.bundle.deletes.%@.%d"
+ "com.apple.searchd.internal.deletes.%@.%d"
+ "com.apple.searchd.restartAttachmentImport"
+ "com.apple.searchd.restartAttachmentImport."
+ "com.apple.spotlightknowledge.historicalReports"
+ "completeIndexingItemFor:delegate:didBeginThrottle:didEndThrottle:error:live:queue:slow:startTime:dataLen:completionHandler:"
+ "cxUnlocked"
+ "dataWithLength:"
+ "dateFromString:"
+ "deleteItems Query bundleID:%@ delay by %f"
+ "deleteItems Query bundleID:%@ resume immediately"
+ "dictionaryRepresentation"
+ "en_US_POSIX"
+ "endDate"
+ "fbi"
+ "fetchAllParametersForLanguages:"
+ "fetchBundleIDs:"
+ "fetchBundleIds not supported"
+ "fetchBundleIdsForProtectionClass:completionHandler:"
+ "filenameDateFormatter"
+ "filterOutHiddenApps"
+ "finishDeleteBatchForQueryQueue:bundleID:blockTime:"
+ "fixupBundlesWithGroup:"
+ "getReportsForDateInterval:reportHandler:"
+ "handleAssetsCommand:"
+ "i36@0:8B16B20B24@28"
+ "initWithDictionary:"
+ "initWithIdentifier:"
+ "ipc"
+ "isPriority"
+ "isSpotlightUIClientBundle:"
+ "issueBundleFixup:completionHandler:"
+ "kIndexOptionManaged"
+ "kMDItemInterestingDate_Ranking=*"
+ "kSPBundleFixUpVersion"
+ "kSPIndexRankingDate"
+ "lengthOfBytesUsingEncoding:"
+ "localeWithLocaleIdentifier:"
+ "mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:"
+ "moveBackMailToClassA"
+ "moveMailToClassC"
+ "moveMailToClassCWithoutClone"
+ "mutableBytes"
+ "onDemandOpen"
+ "openIndex %@: SINotifyLowspace error: %d"
+ "openIndex %@: SIOpenIndexAtPathWithCallbacks failed due to low space (ENOSPC), trying read only mode"
+ "openIndex %@: unable to send low disk space notification: %d"
+ "openIndex:shouldReindexAll:readOnly:forcePC:"
+ "report"
+ "resourcePath"
+ "saveReport:withType:errorHandler:"
+ "setByAddingObjectsFromArray:"
+ "setExpectedDuration:"
+ "setGroupConcurrencyLimit:"
+ "setGroupName:"
+ "setLocale:"
+ "setOnDemandOpen:"
+ "setPriority:"
+ "setReport:"
+ "setRequiresExternalPower:"
+ "setRequiresNetworkConnectivity:"
+ "setRequiresProtectionClass:"
+ "setRequiresUserInactivity:"
+ "setResourceIntensive:"
+ "setResources:"
+ "setTimestamp:"
+ "setType:"
+ "startDate"
+ "submitTaskRequest:error:"
+ "textContentSummary"
+ "timestamp"
+ "updateIndexRankingDates"
+ "updateIndexRankingDates:"
+ "updateKnownBundles:group:"
+ "v116@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32q40@\"NSData\"48@\"NSData\"56@\"NSData\"64@\"NSData\"72@\"NSData\"80@\"NSString\"88@\"NSData\"96B104@?<v@?@\"NSError\"B>108"
+ "v16@?0d8"
+ "v20@?0@\"NSError\"8B16"
+ "v24@0:8@\"NSObject<OS_xpc_object>\"16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v36@0:8@16I24@?28"
+ "v40@0:8@16@24d32"
+ "v48@?0^{__CFString=}8B16B20q24q32@?<v@?>40"
+ "v88@0:8@16@24B32B36@40B48@52B60d64Q72@?80"
+ "yyyyMMdd-HHmm"
- ".."
- "/Library/Spotlight/Assets"
- "2328.7.8.7"
- "Handle job type %ld from %@"
- "Index open, result:%d, dataclass:%@, shouldReindexAll:%@, createCount:%lu"
- "QoS _mSIQWQS: %d prio: %lld"
- "Throttling indexing reply for %@ by %g s"
- "[5i]"
- "_enumerateIndexersWithProtectionClasses:forBundleIds:inferPriorityIndex:block:"
- "_enumerateIndexersWithProtectionClasses:inferPriorityIndex:block:"
- "_pBWQC: uP: %@, iPB: %@"
- "_pBWQC: uP: YES"
- "_pommesBundlesWithQueryContext:"
- "completeIndexingItemFor:delegate:didBeginThrottle:didEndThrottle:error:live:queue:slow:startTime:completionHandler:"
- "fetchAllParametersForLanguages:resourcePath:"
- "mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:"
- "v40@?0^{__CFString=}8B16B20q24@?<v@?>32"
- "v80@0:8@16@24B32B36@40B48@52B60d64@?72"

```
