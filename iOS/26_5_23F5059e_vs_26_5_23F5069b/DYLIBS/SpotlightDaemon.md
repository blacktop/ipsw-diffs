## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2418.5.7.0.0
-  __TEXT.__text: 0xbc9d8
-  __TEXT.__auth_stubs: 0x2010
-  __TEXT.__objc_methlist: 0x4704
+2418.5.9.101.0
+  __TEXT.__text: 0xbceb8
+  __TEXT.__auth_stubs: 0x2030
+  __TEXT.__objc_methlist: 0x4714
   __TEXT.__const: 0x388
   __TEXT.__cstring: 0x8cbf
   __TEXT.__gcc_except_tab: 0x45f0
-  __TEXT.__oslogstring: 0xb444
+  __TEXT.__oslogstring: 0xb466
   __TEXT.__dlopen_cstrs: 0x4a
-  __TEXT.__unwind_info: 0x2768
-  __TEXT.__objc_classname: 0x5af
-  __TEXT.__objc_methname: 0xfe20
-  __TEXT.__objc_methtype: 0x27b2
-  __TEXT.__objc_stubs: 0xc940
+  __TEXT.__unwind_info: 0x2780
+  __TEXT.__objc_classname: 0x5b0
+  __TEXT.__objc_methname: 0xfe89
+  __TEXT.__objc_methtype: 0x27df
+  __TEXT.__objc_stubs: 0xc960
   __DATA_CONST.__got: 0xbc0
   __DATA_CONST.__const: 0x4048
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x39a0
+  __DATA_CONST.__objc_selrefs: 0x39a8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x2e0
-  __AUTH_CONST.__auth_got: 0x1020
+  __AUTH_CONST.__auth_got: 0x1030
   __AUTH_CONST.__const: 0x1168
   __AUTH_CONST.__cfstring: 0x7820
-  __AUTH_CONST.__objc_const: 0x5ae8
+  __AUTH_CONST.__objc_const: 0x5b48
   __AUTH_CONST.__objc_arrayobj: 0x378
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x4bc
+  __DATA.__objc_ivar: 0x4c8
   __DATA.__data: 0x810
   __DATA.__bss: 0x128
   __DATA.__common: 0x4

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 4FB84D4A-EB00-3DCB-8651-CDC00AF9677F
-  Functions: 3107
-  Symbols:   10512
-  CStrings:  6188
+  UUID: 2A7164EC-3C25-3EF9-A71A-C101CDEB2E66
+  Functions: 3112
+  Symbols:   10526
+  CStrings:  6194
 
Symbols:
+ +[SPConcreteCoreSpotlightIndexer initialize].cold.1
+ -[SPConcreteCoreSpotlightIndexer _flushPendingNotificationBatches]
+ -[SPConcreteCoreSpotlightIndexer _flushPendingNotificationBatches].cold.1
+ GCC_except_table104
+ GCC_except_table1046
+ GCC_except_table1082
+ GCC_except_table1088
+ GCC_except_table1089
+ GCC_except_table1097
+ GCC_except_table1098
+ GCC_except_table1106
+ GCC_except_table1121
+ GCC_except_table1125
+ GCC_except_table1135
+ GCC_except_table1145
+ GCC_except_table1152
+ GCC_except_table1159
+ GCC_except_table1166
+ GCC_except_table1173
+ GCC_except_table1189
+ GCC_except_table1260
+ GCC_except_table1266
+ GCC_except_table1313
+ GCC_except_table1320
+ GCC_except_table1442
+ GCC_except_table1447
+ GCC_except_table1448
+ GCC_except_table1512
+ GCC_except_table1517
+ GCC_except_table1518
+ GCC_except_table165
+ GCC_except_table1707
+ GCC_except_table178
+ GCC_except_table183
+ GCC_except_table196
+ GCC_except_table203
+ GCC_except_table213
+ GCC_except_table216
+ GCC_except_table219
+ GCC_except_table220
+ GCC_except_table228
+ GCC_except_table229
+ GCC_except_table237
+ GCC_except_table238
+ GCC_except_table251
+ GCC_except_table258
+ GCC_except_table272
+ GCC_except_table280
+ GCC_except_table318
+ GCC_except_table328
+ GCC_except_table340
+ GCC_except_table373
+ GCC_except_table395
+ GCC_except_table423
+ GCC_except_table424
+ GCC_except_table439
+ GCC_except_table440
+ GCC_except_table469
+ GCC_except_table493
+ GCC_except_table507
+ GCC_except_table510
+ GCC_except_table523
+ GCC_except_table524
+ GCC_except_table561
+ GCC_except_table572
+ GCC_except_table591
+ GCC_except_table597
+ GCC_except_table614
+ GCC_except_table615
+ GCC_except_table624
+ GCC_except_table646
+ GCC_except_table672
+ GCC_except_table673
+ GCC_except_table697
+ GCC_except_table761
+ GCC_except_table785
+ GCC_except_table806
+ GCC_except_table810
+ GCC_except_table814
+ GCC_except_table842
+ GCC_except_table871
+ GCC_except_table903
+ GCC_except_table932
+ GCC_except_table933
+ GCC_except_table942
+ GCC_except_table958
+ GCC_except_table959
+ GCC_except_table995
+ OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._notifyBatchLock
+ OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._notifyBatchTimerScheduled
+ OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._pendingNotificationBatches
+ _OUTLINED_FUNCTION_50
+ ___107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.3519
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2643.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2646
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2646.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2647
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2647.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2648
+ ___236-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:liftingRules:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.404
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2313
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2326
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2335
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2339
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2345
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2346
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2356
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2371
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2378
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2379
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2385
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2387
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2393
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2394
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2395.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2400
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2409
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2419
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2422
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2322
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2331
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2349
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2357
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2374
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2389
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2389.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2397
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2397.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2401
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2420
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2423
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2323
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2323.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2352
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2405
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2421
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2421.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2424
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_4.2425
+ ___31-[SPCoreSpotlightIndexer start]_block_invoke.2493
+ ___39-[SPCoreSpotlightIndexer queryPreheat:]_block_invoke.2629
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.3532
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.3533
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_3.3536
+ ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2257
+ ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2257.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2488
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2488.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2488.cold.2
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2489
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2489.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2490
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2490.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2491
+ ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke.2467
+ ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke_2.2470
+ ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke_3.2471
+ ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.371
+ ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.377
+ ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.377.cold.1
+ ___63-[SPCoreSpotlightIndexer _deleteNonMailBundlesFromClassAIndex:]_block_invoke.2461
+ ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.350
+ ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.355
+ ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.363
+ ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.363.cold.1
+ ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.365
+ ___66-[SPConcreteCoreSpotlightIndexer _flushPendingNotificationBatches]_block_invoke
+ ___66-[SPConcreteCoreSpotlightIndexer _flushPendingNotificationBatches]_block_invoke.340
+ ___66-[SPConcreteCoreSpotlightIndexer _flushPendingNotificationBatches]_block_invoke.340.cold.1
+ ___66-[SPConcreteCoreSpotlightIndexer _flushPendingNotificationBatches]_block_invoke.340.cold.2
+ ___66-[SPConcreteCoreSpotlightIndexer _flushPendingNotificationBatches]_block_invoke.cold.1
+ ___66-[SPConcreteCoreSpotlightIndexer _flushPendingNotificationBatches]_block_invoke.cold.2
+ ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2267
+ ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2267.cold.1
+ ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2268
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2560
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2564
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2573
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2573.cold.1
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2579
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2579.cold.1
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2580
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2563
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2565
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2571
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2577
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2583
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2692
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2696
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2695
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2697
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_3.2700
+ ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.2539
+ ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke_2.2540
+ ___81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2813
+ ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.3515
+ ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke_2.3518
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3454.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3458
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3458.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3459
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3460
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3460.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3461
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2898
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2909
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2932
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2966
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2970
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2974
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3000
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3008
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3021
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3210
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3280
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3281
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3296
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3300
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3304
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3323
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_10.3418
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_11.3419
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_12.3429
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_13.3430
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_14.3437
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_15.3440
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_16.3441
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2912
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3022
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3214
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3284
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3354
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.2913
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3032
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3218
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3358
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3033
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3225
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3362
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5.3256
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5.3386
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_6.3257
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_6.3387
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_7.3260
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_7.3391
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_8.3270
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_8.3404
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_9.3409
+ ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2739
+ ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.2740
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2529.cold.1
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2534
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2535
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke_2.2536
+ ___block_literal_global.2231
+ ___block_literal_global.2249
+ ___block_literal_global.2253
+ ___block_literal_global.2270
+ ___block_literal_global.2274
+ ___block_literal_global.2277
+ ___block_literal_global.2294
+ ___block_literal_global.2310
+ ___block_literal_global.2312
+ ___block_literal_global.2316
+ ___block_literal_global.2341
+ ___block_literal_global.2348
+ ___block_literal_global.2359
+ ___block_literal_global.2381
+ ___block_literal_global.2399
+ ___block_literal_global.2496
+ ___block_literal_global.2500
+ ___block_literal_global.2516
+ ___block_literal_global.2520
+ ___block_literal_global.2528
+ ___block_literal_global.2546
+ ___block_literal_global.2559
+ ___block_literal_global.2567
+ ___block_literal_global.2595
+ ___block_literal_global.2602
+ ___block_literal_global.2604
+ ___block_literal_global.2610
+ ___block_literal_global.2631
+ ___block_literal_global.2675
+ ___block_literal_global.2729
+ ___block_literal_global.2742
+ ___block_literal_global.2846
+ ___block_literal_global.3175
+ ___block_literal_global.3189
+ ___block_literal_global.338
+ ___block_literal_global.342
+ ___block_literal_global.3470
+ ___block_literal_global.3531
+ ___block_literal_global.3549
+ ___block_literal_global.369
+ ___block_literal_global.373
+ ___block_literal_global.4135
+ ___block_literal_global.4179
+ ___block_literal_global.4273
+ ___block_literal_global.4281
+ ___block_literal_global.4283
+ ___block_literal_global.4314
+ ___block_literal_global.4321
+ ___collectSpotlightLogs_block_invoke.4200
+ ___processItemsForImportInner_block_invoke.4229
+ _mach_vm_allocate
+ _mach_vm_deallocate
+ _objc_msgSend$_flushPendingNotificationBatches
- -[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:].cold.1
- GCC_except_table101
- GCC_except_table102
- GCC_except_table1044
- GCC_except_table1080
- GCC_except_table1086
- GCC_except_table1087
- GCC_except_table1093
- GCC_except_table1094
- GCC_except_table1104
- GCC_except_table1119
- GCC_except_table1123
- GCC_except_table1133
- GCC_except_table1143
- GCC_except_table1150
- GCC_except_table1157
- GCC_except_table1164
- GCC_except_table1171
- GCC_except_table1187
- GCC_except_table1256
- GCC_except_table1264
- GCC_except_table1311
- GCC_except_table1318
- GCC_except_table1440
- GCC_except_table1445
- GCC_except_table1446
- GCC_except_table1506
- GCC_except_table1511
- GCC_except_table1515
- GCC_except_table163
- GCC_except_table1704
- GCC_except_table176
- GCC_except_table181
- GCC_except_table194
- GCC_except_table201
- GCC_except_table211
- GCC_except_table212
- GCC_except_table217
- GCC_except_table218
- GCC_except_table221
- GCC_except_table226
- GCC_except_table227
- GCC_except_table233
- GCC_except_table236
- GCC_except_table249
- GCC_except_table252
- GCC_except_table270
- GCC_except_table278
- GCC_except_table316
- GCC_except_table326
- GCC_except_table338
- GCC_except_table371
- GCC_except_table393
- GCC_except_table421
- GCC_except_table422
- GCC_except_table437
- GCC_except_table438
- GCC_except_table467
- GCC_except_table491
- GCC_except_table505
- GCC_except_table508
- GCC_except_table519
- GCC_except_table522
- GCC_except_table559
- GCC_except_table570
- GCC_except_table589
- GCC_except_table595
- GCC_except_table612
- GCC_except_table613
- GCC_except_table622
- GCC_except_table644
- GCC_except_table669
- GCC_except_table670
- GCC_except_table695
- GCC_except_table759
- GCC_except_table783
- GCC_except_table79
- GCC_except_table804
- GCC_except_table808
- GCC_except_table812
- GCC_except_table840
- GCC_except_table869
- GCC_except_table901
- GCC_except_table930
- GCC_except_table931
- GCC_except_table940
- GCC_except_table956
- GCC_except_table957
- GCC_except_table993
- ___107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.3514
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2636
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2638
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2638.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2641.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2642
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2642.cold.1
- ___236-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:liftingRules:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.402
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2308
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2321
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2330
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2334
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2340
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2341
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2351
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2366
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2373
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2374
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2380
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2382
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2383
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2389
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2390
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2390.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2404
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2414
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2417
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2317
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2326
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2344
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2352
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2369
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2384
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2384.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2392
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2392.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2396
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2415
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2418
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2318
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2318.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2347
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2400
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2416
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2416.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2419
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_4.2420
- ___31-[SPCoreSpotlightIndexer start]_block_invoke.2488
- ___39-[SPCoreSpotlightIndexer queryPreheat:]_block_invoke.2624
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.3527
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.3528
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_3.3531
- ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2252
- ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2252.cold.1
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2479
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2483
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2483.cold.1
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2483.cold.2
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2484.cold.1
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2485
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2485.cold.1
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2486
- ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke.2462
- ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke_2.2465
- ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke_3.2466
- ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.369
- ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.376
- ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.376.cold.1
- ___63-[SPCoreSpotlightIndexer _deleteNonMailBundlesFromClassAIndex:]_block_invoke.2456
- ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.348
- ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.353
- ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.362
- ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.362.cold.1
- ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.364
- ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2262
- ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2262.cold.1
- ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2263
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2555
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2559
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2563
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2568.cold.1
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2569
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2574.cold.1
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2575
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2558
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2560
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2566
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2572
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2578
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2687
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2691
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2690
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2692
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_3.2695
- ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.2534
- ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke_2.2535
- ___81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2808
- ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.338
- ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.338.cold.1
- ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.338.cold.2
- ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.cold.1
- ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.cold.2
- ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.3510
- ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke_2.3513
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3449
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3449.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3451
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3453
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3453.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3455
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3455.cold.1
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2893
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2904
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2927
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2961
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2965
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2969
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2995
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3003
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3016
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3205
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3275
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3276
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3286
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3290
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3299
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3318
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_10.3413
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_11.3414
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_12.3424
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_13.3425
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_14.3432
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_15.3435
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_16.3436
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2907
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3017
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3209
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3279
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3349
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.2908
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3027
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3213
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3353
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3028
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3220
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3357
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5.3251
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5.3381
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_6.3252
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_6.3382
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_7.3255
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_7.3386
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_8.3265
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_8.3399
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_9.3404
- ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2734
- ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.2735
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2524
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2524.cold.1
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2525
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke_2.2531
- ___block_literal_global.2221
- ___block_literal_global.2244
- ___block_literal_global.2248
- ___block_literal_global.2265
- ___block_literal_global.2267
- ___block_literal_global.2269
- ___block_literal_global.2289
- ___block_literal_global.2305
- ___block_literal_global.2307
- ___block_literal_global.2311
- ___block_literal_global.2336
- ___block_literal_global.2343
- ___block_literal_global.2354
- ___block_literal_global.2376
- ___block_literal_global.2394
- ___block_literal_global.2491
- ___block_literal_global.2495
- ___block_literal_global.2511
- ___block_literal_global.2515
- ___block_literal_global.2523
- ___block_literal_global.2541
- ___block_literal_global.2554
- ___block_literal_global.2562
- ___block_literal_global.2590
- ___block_literal_global.2597
- ___block_literal_global.2599
- ___block_literal_global.2605
- ___block_literal_global.2626
- ___block_literal_global.2670
- ___block_literal_global.2724
- ___block_literal_global.2737
- ___block_literal_global.2841
- ___block_literal_global.3140
- ___block_literal_global.3184
- ___block_literal_global.336
- ___block_literal_global.340
- ___block_literal_global.3465
- ___block_literal_global.3526
- ___block_literal_global.3544
- ___block_literal_global.368
- ___block_literal_global.372
- ___block_literal_global.4130
- ___block_literal_global.4174
- ___block_literal_global.4268
- ___block_literal_global.4276
- ___block_literal_global.4278
- ___block_literal_global.4309
- ___block_literal_global.4316
- ___collectSpotlightLogs_block_invoke.4195
- ___processItemsForImportInner_block_invoke.4224
CStrings:
+ "Failed to allocate for schema: %d"
+ "_flushPendingNotificationBatches"
+ "_notifyBatchLock"
+ "_notifyBatchTimerScheduled"
+ "_pendingNotificationBatches"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "\xf0Q"
- "\xf01"

```
