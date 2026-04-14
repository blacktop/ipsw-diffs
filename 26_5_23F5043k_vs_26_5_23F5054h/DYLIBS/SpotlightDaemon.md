## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2418.5.3.100.0
-  __TEXT.__text: 0xbb824
-  __TEXT.__auth_stubs: 0x1fd0
-  __TEXT.__objc_methlist: 0x46d4
+2418.5.5.101.0
+  __TEXT.__text: 0xbc894
+  __TEXT.__auth_stubs: 0x1ff0
+  __TEXT.__objc_methlist: 0x4704
   __TEXT.__const: 0x368
-  __TEXT.__cstring: 0x8b37
-  __TEXT.__gcc_except_tab: 0x454c
-  __TEXT.__oslogstring: 0xb117
+  __TEXT.__cstring: 0x8cce
+  __TEXT.__gcc_except_tab: 0x45f0
+  __TEXT.__oslogstring: 0xb444
   __TEXT.__dlopen_cstrs: 0x4a
-  __TEXT.__unwind_info: 0x2748
+  __TEXT.__unwind_info: 0x2770
   __TEXT.__objc_classname: 0x5af
-  __TEXT.__objc_methname: 0xfd89
-  __TEXT.__objc_methtype: 0x2799
-  __TEXT.__objc_stubs: 0xc8c0
+  __TEXT.__objc_methname: 0xfe20
+  __TEXT.__objc_methtype: 0x27b2
+  __TEXT.__objc_stubs: 0xc940
   __DATA_CONST.__got: 0xbb8
-  __DATA_CONST.__const: 0x4030
+  __DATA_CONST.__const: 0x4048
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3980
+  __DATA_CONST.__objc_selrefs: 0x39a0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x2e0
-  __AUTH_CONST.__auth_got: 0x1000
+  __AUTH_CONST.__auth_got: 0x1010
   __AUTH_CONST.__const: 0x1168
-  __AUTH_CONST.__cfstring: 0x7660
+  __AUTH_CONST.__cfstring: 0x7840
   __AUTH_CONST.__objc_const: 0x5ae8
   __AUTH_CONST.__objc_arrayobj: 0x378
   __AUTH_CONST.__objc_intobj: 0x210

   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0xf00
   __DATA_DIRTY.__data: 0x158
-  __DATA_DIRTY.__bss: 0x658
+  __DATA_DIRTY.__bss: 0x670
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 8CDD96B2-6015-36B0-8653-E80AFD048FC8
-  Functions: 3092
-  Symbols:   10470
-  CStrings:  6140
+  UUID: EE40C66D-AFD6-30EF-BB22-8F69B5B1DF29
+  Functions: 3107
+  Symbols:   10508
+  CStrings:  6190
 
Symbols:
+ -[CSSearchClientConnection setQueryTask:forQueryID:].cold.1
+ -[SPConcreteCoreSpotlightIndexer checkDocIDConsistency]
+ -[SPConcreteCoreSpotlightIndexer checkDocIDConsistency].cold.1
+ -[SPConcreteCoreSpotlightIndexer docIDCheckDropTouchFileCreate]
+ -[SPConcreteCoreSpotlightIndexer docIDCheckDropTouchFileExists]
+ -[SPConcreteCoreSpotlightIndexer issueDocIDConsistencyCheck:]
+ -[SPConcreteCoreSpotlightIndexer issueDocIDConsistencyCheck:].cold.1
+ -[SPConcreteCoreSpotlightIndexer issueDocIDConsistencyCheck:].cold.2
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:].cold.14
+ -[SPConcreteCoreSpotlightIndexer shouldDropForKnownDocIDInconsistencyCriteria:version:dropReason:]
+ -[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:].cold.4
+ GCC_except_table1044
+ GCC_except_table1080
+ GCC_except_table1086
+ GCC_except_table1087
+ GCC_except_table1093
+ GCC_except_table1094
+ GCC_except_table1095
+ GCC_except_table1096
+ GCC_except_table1104
+ GCC_except_table1119
+ GCC_except_table1123
+ GCC_except_table1133
+ GCC_except_table1143
+ GCC_except_table1150
+ GCC_except_table1157
+ GCC_except_table1164
+ GCC_except_table1171
+ GCC_except_table1187
+ GCC_except_table1258
+ GCC_except_table1264
+ GCC_except_table1311
+ GCC_except_table1318
+ GCC_except_table1440
+ GCC_except_table1445
+ GCC_except_table1446
+ GCC_except_table1506
+ GCC_except_table1509
+ GCC_except_table1511
+ GCC_except_table1514
+ GCC_except_table1515
+ GCC_except_table1704
+ GCC_except_table270
+ GCC_except_table278
+ GCC_except_table316
+ GCC_except_table326
+ GCC_except_table338
+ GCC_except_table371
+ GCC_except_table393
+ GCC_except_table421
+ GCC_except_table422
+ GCC_except_table437
+ GCC_except_table438
+ GCC_except_table467
+ GCC_except_table491
+ GCC_except_table505
+ GCC_except_table508
+ GCC_except_table519
+ GCC_except_table521
+ GCC_except_table522
+ GCC_except_table559
+ GCC_except_table570
+ GCC_except_table589
+ GCC_except_table595
+ GCC_except_table612
+ GCC_except_table613
+ GCC_except_table622
+ GCC_except_table644
+ GCC_except_table669
+ GCC_except_table670
+ GCC_except_table671
+ GCC_except_table695
+ GCC_except_table759
+ GCC_except_table783
+ GCC_except_table804
+ GCC_except_table808
+ GCC_except_table812
+ GCC_except_table82
+ GCC_except_table840
+ GCC_except_table869
+ GCC_except_table901
+ GCC_except_table930
+ GCC_except_table931
+ GCC_except_table940
+ GCC_except_table956
+ GCC_except_table957
+ GCC_except_table993
+ __SICheckIndexDocIDConsistency
+ __SIIssueIndexDropForDocIDInconsistency
+ ___101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke.1633
+ ___101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke_2.1634
+ ___105-[SPConcreteCoreSpotlightIndexer willModifySearchableItemsWithIdentifiers:forBundleID:completionHandler:]_block_invoke.1438
+ ___105-[SPConcreteCoreSpotlightIndexer willModifySearchableItemsWithIdentifiers:forBundleID:completionHandler:]_block_invoke_2.1442
+ ___107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.3517
+ ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke.1680
+ ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke_2.1671
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2639
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2641
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2641.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2644
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2644.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2645
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2645.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2646
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1593
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1602
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1608
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1620
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1623
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1594
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1611
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1621
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1624
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1624.cold.1
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1612
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1622
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_4.1613
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_5.1616
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_5.1616.cold.1
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1467
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1476
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1476.cold.1
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_2.1471
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_3.1472
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_4.1473
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_5.1474
+ ___131-[SPConcreteCoreSpotlightIndexer persistDonationProgress:fromBundle:clientIndexName:personaID:canCreateNewIndex:completionHandler:]_block_invoke.1260
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1357
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1357.cold.1
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1357.cold.2
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1378
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1380
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1380.cold.1
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1380.cold.2
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1383
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1383.cold.1
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1383.cold.2
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1386
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke_2.1361
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke_2.1379
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1267
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1267.cold.1
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1267.cold.2
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1267.cold.3
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1267.cold.4
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1296
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1318
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1335
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1340
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1344
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1347
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1300
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1319
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1336
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1341
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1341.cold.1
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1348
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_3.1320
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_3.1351
+ ___236-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:liftingRules:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.402
+ ___236-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:liftingRules:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.403
+ ___236-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:liftingRules:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.410
+ ___236-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:liftingRules:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.411
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2311
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2324
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2333
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2337
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2354
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2369
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2376
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2377
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2383
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2385
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2386
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2391
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2392
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2393
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2393.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2398
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2407
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2417
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2420
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2320
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2329
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2347
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2355
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2372
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2387
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2387.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2395
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2395.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2399
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2418
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2421
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2321
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2321.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2350
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2403
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2419
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2419.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2422
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_4.2423
+ ___31-[SPCoreSpotlightIndexer start]_block_invoke.2491
+ ___39-[SPCoreSpotlightIndexer queryPreheat:]_block_invoke.2627
+ ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.704
+ ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.704.cold.1
+ ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.705
+ ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.717
+ ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke_2.709
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.3530
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.3531
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_3.3534
+ ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2255
+ ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2255.cold.1
+ ___50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke.1415
+ ___50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke_2.1416
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2482
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2486
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2486.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2486.cold.2
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2487
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2487.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2488
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2488.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2489
+ ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1786
+ ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1787
+ ___57-[SPConcreteCoreSpotlightIndexer zombifyAllContactItems:]_block_invoke.1531
+ ___59-[SPConcreteCoreSpotlightIndexer _performXPCActivity:name:]_block_invoke.726
+ ___59-[SPConcreteCoreSpotlightIndexer _performXPCActivity:name:]_block_invoke_2.730
+ ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke.2465
+ ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke_2.2468
+ ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke_3.2469
+ ___60-[SPConcreteCoreSpotlightIndexer _addNewClientWithBundleID:]_block_invoke.1057
+ ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.369
+ ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.370
+ ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.376
+ ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.376.cold.1
+ ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke.1237
+ ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_2.1240
+ ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_3.1243
+ ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.750
+ ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.750.cold.1
+ ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.754
+ ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.754.cold.1
+ ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.756
+ ___63-[SPCoreSpotlightIndexer _deleteNonMailBundlesFromClassAIndex:]_block_invoke.2459
+ ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.348
+ ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.349
+ ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.353
+ ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.354
+ ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.362
+ ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.362.cold.1
+ ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.364
+ ___65-[SPConcreteCoreSpotlightIndexer openIndexForUpgradeSynchronous:]_block_invoke.925
+ ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.781.cold.1
+ ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.782
+ ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.782.cold.1
+ ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.783
+ ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.783.cold.1
+ ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.784
+ ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.790
+ ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke_2.794
+ ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2265
+ ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2265.cold.1
+ ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2266
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2558
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2562
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2566
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2571
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2571.cold.1
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2572
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2577
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2577.cold.1
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2578
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2561
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2563
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2569
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2575
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2581
+ ___70-[SPConcreteCoreSpotlightIndexer writeDiagnostic:bundleID:identifier:]_block_invoke_9
+ ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1046
+ ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1047
+ ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke_2.1050
+ ___72-[SPConcreteCoreSpotlightIndexer fetchMeCard:isNotCreateNewIndex:group:]_block_invoke.854
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1538
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1545
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1545.cold.1
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1549
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1549.cold.1
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1550
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1564
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1566
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1570
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke_2.1569
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke_2.1573
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1391
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1396
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1402
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1392
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1397
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1405
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1405.cold.1
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1002
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1006
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1012
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1018
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1029
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1033
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.943
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.954
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.983
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.989
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.994
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1005
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1009
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1015
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1021
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.946
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.956
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.988
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.992
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.997
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.997.cold.1
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.1001
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.947
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.959
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.993
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_4.950
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_4.962
+ ___78-[SPConcreteCoreSpotlightIndexer scheduleMaintenance:description:forDarkWake:]_block_invoke.742
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.1129
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_2.1132
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_3.1133
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_4.1140
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2690
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2694
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2693
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2695
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_3.2698
+ ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.2537
+ ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke_2.2538
+ ___81-[SPConcreteCoreSpotlightIndexer processDecryptsForBundleID:persona:infos:group:]_block_invoke.1246
+ ___81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2811
+ ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.338
+ ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.338.cold.1
+ ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.338.cold.2
+ ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.3513
+ ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke_2.3516
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3452
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3452.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3454
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3456
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3456.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3457
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3458
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3458.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3459
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2896
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2907
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2968
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2972
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2998
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3006
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3019
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3208
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3278
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3289
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3293
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3294
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3298
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3302
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3321
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_10.3416
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_11.3417
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_12.3427
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_13.3428
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_14.3435
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_15.3438
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_16.3439
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2910
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3020
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3212
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3282
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3352
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.2911
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3030
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3216
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3356
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3031
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3223
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3360
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5.3254
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5.3384
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_6.3255
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_6.3385
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_7.3258
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_7.3389
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_8.3268
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_8.3402
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_9.3407
+ ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1065
+ ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1066
+ ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2737
+ ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.2738
+ ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.803
+ ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.804
+ ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.805
+ ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.809
+ ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke_2.808
+ ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke_2.812
+ ___96-[SpotlightDaemonServer handleJob:protectionClass:perClientCompletionHandler:completionHandler:]_block_invoke.89
+ ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1487
+ ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1497
+ ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_2.1498
+ ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_3.1499
+ ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_4.1502
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2527
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2527.cold.1
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2528
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2532
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2533
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke_2.2534
+ ___block_literal_global.1011
+ ___block_literal_global.1017
+ ___block_literal_global.1023
+ ___block_literal_global.1035
+ ___block_literal_global.1232
+ ___block_literal_global.1235
+ ___block_literal_global.1239
+ ___block_literal_global.1242
+ ___block_literal_global.1245
+ ___block_literal_global.1298
+ ___block_literal_global.1343
+ ___block_literal_global.1353
+ ___block_literal_global.1382
+ ___block_literal_global.1385
+ ___block_literal_global.1478
+ ___block_literal_global.1626
+ ___block_literal_global.1692
+ ___block_literal_global.1720
+ ___block_literal_global.2224
+ ___block_literal_global.2229
+ ___block_literal_global.2247
+ ___block_literal_global.2251
+ ___block_literal_global.2270
+ ___block_literal_global.2275
+ ___block_literal_global.2292
+ ___block_literal_global.2308
+ ___block_literal_global.2310
+ ___block_literal_global.2314
+ ___block_literal_global.2339
+ ___block_literal_global.2346
+ ___block_literal_global.2357
+ ___block_literal_global.2379
+ ___block_literal_global.2397
+ ___block_literal_global.2494
+ ___block_literal_global.2498
+ ___block_literal_global.2514
+ ___block_literal_global.2518
+ ___block_literal_global.2526
+ ___block_literal_global.2544
+ ___block_literal_global.2557
+ ___block_literal_global.2565
+ ___block_literal_global.2593
+ ___block_literal_global.2600
+ ___block_literal_global.2602
+ ___block_literal_global.2608
+ ___block_literal_global.2629
+ ___block_literal_global.2673
+ ___block_literal_global.2727
+ ___block_literal_global.2740
+ ___block_literal_global.2844
+ ___block_literal_global.3143
+ ___block_literal_global.3148
+ ___block_literal_global.3153
+ ___block_literal_global.3158
+ ___block_literal_global.3163
+ ___block_literal_global.3168
+ ___block_literal_global.3173
+ ___block_literal_global.3187
+ ___block_literal_global.336
+ ___block_literal_global.340
+ ___block_literal_global.3468
+ ___block_literal_global.3529
+ ___block_literal_global.3547
+ ___block_literal_global.368
+ ___block_literal_global.372
+ ___block_literal_global.4133
+ ___block_literal_global.4177
+ ___block_literal_global.4271
+ ___block_literal_global.4279
+ ___block_literal_global.4281
+ ___block_literal_global.4312
+ ___block_literal_global.4319
+ ___block_literal_global.707
+ ___block_literal_global.748
+ ___block_literal_global.775
+ ___block_literal_global.847
+ ___block_literal_global.852
+ ___block_literal_global.882
+ ___block_literal_global.916
+ ___block_literal_global.919
+ ___block_literal_global.921
+ ___block_literal_global.939
+ ___block_literal_global.961
+ ___block_literal_global.964
+ ___block_literal_global.985
+ ___collectSpotlightLogs_block_invoke.4198
+ ___processItemsForImportInner_block_invoke.4227
+ _clientTypeForBundleID:jobType:.gamesDaemonEnabled
+ _objc_msgSend$checkDocIDConsistency
+ _objc_msgSend$docIDCheckDropTouchFileCreate
+ _objc_msgSend$docIDCheckDropTouchFileExists
+ _objc_msgSend$issueDocIDConsistencyCheck:
+ _objc_msgSend$shouldDropForKnownDocIDInconsistencyCriteria:version:dropReason:
- -[SPConcreteCoreSpotlightIndexer creationTouchFileUnlink]
- GCC_except_table1039
- GCC_except_table1075
- GCC_except_table1081
- GCC_except_table1082
- GCC_except_table1088
- GCC_except_table1089
- GCC_except_table1090
- GCC_except_table1091
- GCC_except_table1099
- GCC_except_table1114
- GCC_except_table1118
- GCC_except_table1128
- GCC_except_table1138
- GCC_except_table1145
- GCC_except_table1152
- GCC_except_table1159
- GCC_except_table1166
- GCC_except_table1182
- GCC_except_table1248
- GCC_except_table1250
- GCC_except_table1303
- GCC_except_table1310
- GCC_except_table1432
- GCC_except_table1437
- GCC_except_table1438
- GCC_except_table1498
- GCC_except_table1501
- GCC_except_table1503
- GCC_except_table1504
- GCC_except_table1691
- GCC_except_table269
- GCC_except_table277
- GCC_except_table315
- GCC_except_table325
- GCC_except_table337
- GCC_except_table367
- GCC_except_table389
- GCC_except_table416
- GCC_except_table417
- GCC_except_table432
- GCC_except_table433
- GCC_except_table462
- GCC_except_table486
- GCC_except_table500
- GCC_except_table503
- GCC_except_table514
- GCC_except_table516
- GCC_except_table517
- GCC_except_table554
- GCC_except_table565
- GCC_except_table584
- GCC_except_table590
- GCC_except_table607
- GCC_except_table608
- GCC_except_table617
- GCC_except_table639
- GCC_except_table664
- GCC_except_table665
- GCC_except_table666
- GCC_except_table690
- GCC_except_table754
- GCC_except_table778
- GCC_except_table799
- GCC_except_table803
- GCC_except_table807
- GCC_except_table835
- GCC_except_table864
- GCC_except_table896
- GCC_except_table925
- GCC_except_table926
- GCC_except_table935
- GCC_except_table951
- GCC_except_table952
- GCC_except_table988
- ___101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke.1596
- ___101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke_2.1597
- ___105-[SPConcreteCoreSpotlightIndexer willModifySearchableItemsWithIdentifiers:forBundleID:completionHandler:]_block_invoke.1401
- ___105-[SPConcreteCoreSpotlightIndexer willModifySearchableItemsWithIdentifiers:forBundleID:completionHandler:]_block_invoke_2.1405
- ___107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.3464
- ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke.1643
- ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke_2.1634
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2597
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2599
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2599.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2602
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2602.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2603
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2603.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2604
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1556
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1565
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1571
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1583
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1586
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1557
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1574
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1584
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1587
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1587.cold.1
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1575
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1585
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_4.1576
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_5.1579
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_5.1579.cold.1
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1430
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1439
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1439.cold.1
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_2.1434
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_3.1435
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_4.1436
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_5.1437
- ___131-[SPConcreteCoreSpotlightIndexer persistDonationProgress:fromBundle:clientIndexName:personaID:canCreateNewIndex:completionHandler:]_block_invoke.1223
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1320
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1320.cold.1
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1320.cold.2
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1341
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1343
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1343.cold.1
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1343.cold.2
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1346
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1346.cold.1
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1346.cold.2
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1349
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke_2.1324
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke_2.1342
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1230
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1230.cold.1
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1230.cold.2
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1230.cold.3
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1230.cold.4
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1259
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1281
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1298
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1303
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1307
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1310
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1263
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1282
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1299
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1304
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1304.cold.1
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1311
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_3.1283
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_3.1314
- ___236-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:liftingRules:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.399
- ___236-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:liftingRules:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.400
- ___236-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:liftingRules:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.407
- ___236-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:liftingRules:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.408
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2269
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2282
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2291
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2295
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2301
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2302
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2312
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2327
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2334
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2335
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2341
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2349
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2350
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2351
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2351.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2356
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2365
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2375
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2378
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2278
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2287
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2305
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2313
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2330
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2345
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2345.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2353
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2353.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2357
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2376
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2379
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2279
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2279.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2308
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2361
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2377
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2377.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2380
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_4.2381
- ___31-[SPCoreSpotlightIndexer start]_block_invoke.2449
- ___39-[SPCoreSpotlightIndexer queryPreheat:]_block_invoke.2585
- ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.701
- ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.701.cold.1
- ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.702
- ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.714
- ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke_2.706
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.3477
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.3478
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_3.3481
- ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2213
- ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2213.cold.1
- ___50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke.1378
- ___50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke_2.1379
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2440
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2444
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2444.cold.1
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2444.cold.2
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2445
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2445.cold.1
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2446
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2446.cold.1
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2447
- ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1749
- ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1750
- ___57-[SPConcreteCoreSpotlightIndexer zombifyAllContactItems:]_block_invoke.1494
- ___59-[SPConcreteCoreSpotlightIndexer _performXPCActivity:name:]_block_invoke.723
- ___59-[SPConcreteCoreSpotlightIndexer _performXPCActivity:name:]_block_invoke_2.727
- ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke.2423
- ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke_2.2426
- ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke_3.2427
- ___60-[SPConcreteCoreSpotlightIndexer _addNewClientWithBundleID:]_block_invoke.1050
- ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.366
- ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.367
- ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.373
- ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.373.cold.1
- ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke.1200
- ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_2.1203
- ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_3.1206
- ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.747
- ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.747.cold.1
- ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.751
- ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.751.cold.1
- ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.753
- ___63-[SPCoreSpotlightIndexer _deleteNonMailBundlesFromClassAIndex:]_block_invoke.2417
- ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.345
- ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.346
- ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.350
- ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.351
- ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.359
- ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.359.cold.1
- ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.361
- ___65-[SPConcreteCoreSpotlightIndexer openIndexForUpgradeSynchronous:]_block_invoke.919
- ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.778
- ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.778.cold.1
- ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.779
- ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.779.cold.1
- ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.780
- ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.780.cold.1
- ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.787
- ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke_2.791
- ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2223
- ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2223.cold.1
- ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2224
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2516
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2520
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2524
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2529
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2529.cold.1
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2530
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2535
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2535.cold.1
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2536
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2519
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2521
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2527
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2533
- ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2539
- ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1039
- ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1040
- ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke_2.1043
- ___72-[SPConcreteCoreSpotlightIndexer fetchMeCard:isNotCreateNewIndex:group:]_block_invoke.851
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1501
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1508
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1508.cold.1
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1512
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1512.cold.1
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1513
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1527
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1529
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1533
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke_2.1532
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke_2.1536
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1354
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1359
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1365
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1355
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1360
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1368
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1368.cold.1
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1005
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1011
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1022
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1026
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.937
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.948
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.976
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.980
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.982
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.995
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.999
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1002
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1008
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1014
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.940
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.950
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.981
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.985
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.990
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.990.cold.1
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.998
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.941
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.953
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.986
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.994
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_4.944
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_4.956
- ___78-[SPConcreteCoreSpotlightIndexer scheduleMaintenance:description:forDarkWake:]_block_invoke.739
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.1095
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_2.1098
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_3.1099
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_4.1106
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2648
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2652
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2651
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2653
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_3.2656
- ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.2495
- ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke_2.2496
- ___81-[SPConcreteCoreSpotlightIndexer processDecryptsForBundleID:persona:infos:group:]_block_invoke.1209
- ___81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2769
- ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.335
- ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.335.cold.1
- ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.335.cold.2
- ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.3460
- ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke_2.3463
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3399
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3399.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3401
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3403
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3403.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3404
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3405
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3405.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3406
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2854
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2865
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2888
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2922
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2926
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2956
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2977
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3166
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3236
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3237
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3247
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3251
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3252
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3256
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3260
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_10.3374
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_11.3375
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_12.3385
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_13.3386
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2868
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2978
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3170
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3240
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3310
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.2869
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.2988
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3174
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3314
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.2989
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3181
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3318
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5.3212
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5.3342
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_6.3213
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_6.3343
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_7.3216
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_7.3347
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_8.3226
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_8.3360
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_9.3365
- ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1058
- ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1059
- ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2695
- ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.2696
- ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.800
- ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.801
- ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.802
- ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.806
- ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke_2.805
- ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke_2.809
- ___96-[SpotlightDaemonServer handleJob:protectionClass:perClientCompletionHandler:completionHandler:]_block_invoke.85
- ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1450
- ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1460
- ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_2.1461
- ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_3.1462
- ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_4.1465
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2485
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2485.cold.1
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2486
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2490
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2491
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke_2.2492
- ___block_literal_global.1004
- ___block_literal_global.1010
- ___block_literal_global.1016
- ___block_literal_global.1028
- ___block_literal_global.1195
- ___block_literal_global.1198
- ___block_literal_global.1202
- ___block_literal_global.1205
- ___block_literal_global.1208
- ___block_literal_global.1261
- ___block_literal_global.1306
- ___block_literal_global.1316
- ___block_literal_global.1345
- ___block_literal_global.1348
- ___block_literal_global.1441
- ___block_literal_global.1589
- ___block_literal_global.1655
- ___block_literal_global.1683
- ___block_literal_global.2182
- ___block_literal_global.2187
- ___block_literal_global.2205
- ___block_literal_global.2209
- ___block_literal_global.2226
- ___block_literal_global.2228
- ___block_literal_global.2230
- ___block_literal_global.2233
- ___block_literal_global.2250
- ___block_literal_global.2266
- ___block_literal_global.2297
- ___block_literal_global.2304
- ___block_literal_global.2315
- ___block_literal_global.2337
- ___block_literal_global.2355
- ___block_literal_global.2452
- ___block_literal_global.2456
- ___block_literal_global.2472
- ___block_literal_global.2476
- ___block_literal_global.2484
- ___block_literal_global.2502
- ___block_literal_global.2515
- ___block_literal_global.2523
- ___block_literal_global.2551
- ___block_literal_global.2558
- ___block_literal_global.2560
- ___block_literal_global.2566
- ___block_literal_global.2587
- ___block_literal_global.2631
- ___block_literal_global.2685
- ___block_literal_global.2698
- ___block_literal_global.2802
- ___block_literal_global.3101
- ___block_literal_global.3106
- ___block_literal_global.3111
- ___block_literal_global.3116
- ___block_literal_global.3121
- ___block_literal_global.3126
- ___block_literal_global.3131
- ___block_literal_global.3145
- ___block_literal_global.333
- ___block_literal_global.337
- ___block_literal_global.3415
- ___block_literal_global.3476
- ___block_literal_global.3494
- ___block_literal_global.365
- ___block_literal_global.369
- ___block_literal_global.4080
- ___block_literal_global.4124
- ___block_literal_global.4218
- ___block_literal_global.4226
- ___block_literal_global.4228
- ___block_literal_global.4259
- ___block_literal_global.4266
- ___block_literal_global.704
- ___block_literal_global.745
- ___block_literal_global.772
- ___block_literal_global.844
- ___block_literal_global.849
- ___block_literal_global.879
- ___block_literal_global.910
- ___block_literal_global.913
- ___block_literal_global.915
- ___block_literal_global.933
- ___block_literal_global.946
- ___block_literal_global.955
- ___block_literal_global.978
- ___collectSpotlightLogs_block_invoke.4145
- ___processItemsForImportInner_block_invoke.4174
- _objc_msgSend$creationTouchFileUnlink
CStrings:
+ "*warn* client checkin %@ has wrong protection class for %@"
+ "23E"
+ "23F"
+ "B40@0:8^{__SI=}16q24^@32"
+ "CSDisableGamesDaemonClient"
+ "DocID Consistency: %@\n\n"
+ "Failed to serialize docID consistency check results: %@"
+ "GamesDaemon"
+ "No index for dataclass:%@ - can't open to journal"
+ "No index for dataclass:%@ - creating"
+ "Overwriting existing query task for qid=%ld (client=%@)."
+ "Skipping open dataclass:%@ - docID consistency check requested drop"
+ "checkDocIDConsistency"
+ "checked"
+ "com.apple.corespotlight.daemon.games"
+ "com.apple.games"
+ "docID consistency check failed for dataclass:%@"
+ "docID consistency check requested drop"
+ "docID consistency check skipped %lu index(es) (not open, device may be locked): %@"
+ "docID consistency check: already completed for dataclass:%@, version: %ld"
+ "docID consistency check: dropping index for dataclass:%@, checked: %ld, mismatched: %ld, missing: %ld, unmapped: %ld, reason: %@"
+ "docID consistency check: failed for dataclass:%@, will retry next launch"
+ "docID consistency check: failed to create touch file for dataclass:%@, error: %d"
+ "docID consistency check: passed for dataclass:%@, checked: %ld"
+ "docID consistency check: starting for dataclass:%@ (stored version: %ld, target version: %d)"
+ "docIDCheckDropRequested"
+ "docIDCheckDropTouchFileCreate"
+ "docIDCheckDropTouchFileExists"
+ "docidcheck"
+ "inconsistency found, mismatched: %ld, missing: %ld"
+ "issueDocIDConsistencyCheck:"
+ "kSIConsistencyCheck"
+ "kSIConsistencyCheck=%@ (affected build, evidence may have been lost)"
+ "kSPDocIDConsistencyCheck"
+ "mismatched"
+ "missing"
+ "shouldDropForKnownDocIDInconsistencyCriteria:version:dropReason:"
+ "skipped"
+ "unmapped"
- "*warn* client checkin %@ has wrong protection class for for %@"
- "No index for for dataclass:%@ - can't open to journal"
- "No index for for dataclass:%@ - creating"
- "creationTouchFileUnlink"

```
