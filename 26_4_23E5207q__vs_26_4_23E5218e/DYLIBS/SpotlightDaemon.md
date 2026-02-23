## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2418.4.8.2.100
-  __TEXT.__text: 0xbbaa0
-  __TEXT.__auth_stubs: 0x1fb0
-  __TEXT.__objc_methlist: 0x4854
-  __TEXT.__const: 0x378
-  __TEXT.__gcc_except_tab: 0x45a4
-  __TEXT.__cstring: 0x8fcc
-  __TEXT.__oslogstring: 0xb28c
+2418.4.10.1.0
+  __TEXT.__text: 0xbc428
+  __TEXT.__auth_stubs: 0x1fd0
+  __TEXT.__objc_methlist: 0x485c
+  __TEXT.__const: 0x368
+  __TEXT.__gcc_except_tab: 0x4638
+  __TEXT.__cstring: 0x901b
+  __TEXT.__oslogstring: 0xb392
   __TEXT.__dlopen_cstrs: 0x4a
-  __TEXT.__unwind_info: 0x2780
+  __TEXT.__unwind_info: 0x2798
   __TEXT.__objc_classname: 0x5fb
-  __TEXT.__objc_methname: 0xffcb
-  __TEXT.__objc_methtype: 0x288a
-  __TEXT.__objc_stubs: 0xc940
-  __DATA_CONST.__got: 0xb70
-  __DATA_CONST.__const: 0x4058
+  __TEXT.__objc_methname: 0x10027
+  __TEXT.__objc_methtype: 0x28ab
+  __TEXT.__objc_stubs: 0xc9c0
+  __DATA_CONST.__got: 0xb78
+  __DATA_CONST.__const: 0x4080
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x39f8
+  __DATA_CONST.__objc_selrefs: 0x3a18
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x130
-  __DATA_CONST.__objc_arraydata: 0x2d8
-  __AUTH_CONST.__auth_got: 0xff0
-  __AUTH_CONST.__const: 0x1128
-  __AUTH_CONST.__cfstring: 0x75a0
+  __DATA_CONST.__objc_arraydata: 0x2e0
+  __AUTH_CONST.__auth_got: 0x1000
+  __AUTH_CONST.__const: 0x1168
+  __AUTH_CONST.__cfstring: 0x7640
   __AUTH_CONST.__objc_const: 0x5ee8
   __AUTH_CONST.__objc_arrayobj: 0x378
   __AUTH_CONST.__objc_intobj: 0x210

   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x4e4
   __DATA.__data: 0x870
-  __DATA.__bss: 0x120
+  __DATA.__bss: 0x128
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0xf50
   __DATA_DIRTY.__data: 0x158

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 051597D8-C30B-3F71-A1A8-43C56A54DF4D
-  Functions: 3111
-  Symbols:   10531
-  CStrings:  6176
+  UUID: 801CF5D8-5A31-31A2-8DAC-2DA132090CB0
+  Functions: 3116
+  Symbols:   10555
+  CStrings:  6197
 
Symbols:
+ -[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]
+ -[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]
+ -[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities].cold.1
+ -[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities].cold.2
+ -[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities].cold.3
+ -[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities].cold.4
+ -[SPCoreSpotlightIndexer revokeExpiredItems:protected:expirationRef:]
+ GCC_except_table1024
+ GCC_except_table1060
+ GCC_except_table1066
+ GCC_except_table1067
+ GCC_except_table1074
+ GCC_except_table1075
+ GCC_except_table1076
+ GCC_except_table1084
+ GCC_except_table1099
+ GCC_except_table1103
+ GCC_except_table1113
+ GCC_except_table1123
+ GCC_except_table1130
+ GCC_except_table1137
+ GCC_except_table1144
+ GCC_except_table1151
+ GCC_except_table1167
+ GCC_except_table1233
+ GCC_except_table1235
+ GCC_except_table1241
+ GCC_except_table1288
+ GCC_except_table1295
+ GCC_except_table1417
+ GCC_except_table1422
+ GCC_except_table1423
+ GCC_except_table1483
+ GCC_except_table1486
+ GCC_except_table1488
+ GCC_except_table1489
+ GCC_except_table1676
+ GCC_except_table258
+ GCC_except_table266
+ GCC_except_table304
+ GCC_except_table314
+ GCC_except_table326
+ GCC_except_table356
+ GCC_except_table378
+ GCC_except_table788
+ GCC_except_table792
+ GCC_except_table796
+ GCC_except_table824
+ GCC_except_table853
+ GCC_except_table885
+ GCC_except_table914
+ GCC_except_table915
+ GCC_except_table924
+ GCC_except_table940
+ GCC_except_table941
+ GCC_except_table973
+ ___101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke.1581
+ ___101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke_2.1582
+ ___105-[SPConcreteCoreSpotlightIndexer willModifySearchableItemsWithIdentifiers:forBundleID:completionHandler:]_block_invoke.1387
+ ___105-[SPConcreteCoreSpotlightIndexer willModifySearchableItemsWithIdentifiers:forBundleID:completionHandler:]_block_invoke_2.1391
+ ___107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.3448
+ ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke.1628
+ ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke_2.1619
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2581
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2583
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2583.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2586
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2586.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2587
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2587.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2588
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1541
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1556
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1568
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1571
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1542
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1559
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1569
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1572
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1572.cold.1
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1560
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1570
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_4.1561
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_5.1564
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_5.1564.cold.1
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1416
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1425
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1425.cold.1
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_2.1420
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_3.1421
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_4.1422
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_5.1423
+ ___131-[SPConcreteCoreSpotlightIndexer persistDonationProgress:fromBundle:clientIndexName:personaID:canCreateNewIndex:completionHandler:]_block_invoke.1212
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1306
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1306.cold.1
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1306.cold.2
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1327
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1329.cold.1
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1329.cold.2
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1332
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1332.cold.1
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1332.cold.2
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1335
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke_2.1310
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke_2.1328
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1219
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1219.cold.1
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1219.cold.2
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1219.cold.3
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1219.cold.4
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1245
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1267
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1284
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1289
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1293
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1296
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1249
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1268
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1285
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1290
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1290.cold.1
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1297
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_3.1269
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_3.1300
+ ___28-[CSSearchAgent startQuery:]_block_invoke.178
+ ___28-[CSSearchAgent startQuery:]_block_invoke.178.cold.1
+ ___28-[CSSearchAgent startQuery:]_block_invoke.178.cold.2
+ ___28-[CSSearchAgent startQuery:]_block_invoke.178.cold.3
+ ___28-[CSSearchAgent startQuery:]_block_invoke.216
+ ___28-[CSSearchAgent startQuery:]_block_invoke.220
+ ___28-[CSSearchAgent startQuery:]_block_invoke.230
+ ___28-[CSSearchAgent startQuery:]_block_invoke.241
+ ___28-[CSSearchAgent startQuery:]_block_invoke_2.228
+ ___28-[CSSearchAgent startQuery:]_block_invoke_2.232
+ ___28-[CSSearchAgent startQuery:]_block_invoke_2.232.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2252
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2265
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2274
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2278
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2284
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2285
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2295
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2310
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2317
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2318
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2324
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2326
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2332
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2333
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2334
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2334.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2339
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2348
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2358
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2361
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2261
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2270
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2288
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2296
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2328
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2328.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2336
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2336.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2340
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2359
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2362
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2262
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2262.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2291
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2344
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2360
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2360.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2363
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_4.2364
+ ___31-[SPCoreSpotlightIndexer start]_block_invoke.2432
+ ___39-[SPCoreSpotlightIndexer queryPreheat:]_block_invoke.2569
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.3461
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.3462
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_3.3465
+ ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2196
+ ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2196.cold.1
+ ___50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke.1364
+ ___50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke_2.1365
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2423
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2427
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2427.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2427.cold.2
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2428
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2428.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2429
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2429.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2430
+ ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1734
+ ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1735
+ ___57-[SPConcreteCoreSpotlightIndexer zombifyAllContactItems:]_block_invoke.1480
+ ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke.2406
+ ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke_2.2409
+ ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke_3.2410
+ ___60-[SPConcreteCoreSpotlightIndexer _addNewClientWithBundleID:]_block_invoke.1039
+ ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke.1189
+ ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_2.1192
+ ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_3.1195
+ ___63-[SPCoreSpotlightIndexer _deleteNonMailBundlesFromClassAIndex:]_block_invoke.2400
+ ___65-[SPConcreteCoreSpotlightIndexer openIndexForUpgradeSynchronous:]_block_invoke.902
+ ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke
+ ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.759
+ ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.759.cold.1
+ ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.760
+ ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.760.cold.1
+ ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.761
+ ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.761.cold.1
+ ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.762
+ ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.768
+ ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke.cold.1
+ ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke_2
+ ___67-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:expirationRef:]_block_invoke_2.772
+ ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2206
+ ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2206.cold.1
+ ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2207
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2499
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2503
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2507
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2512
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2512.cold.1
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2513
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2519
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2519.cold.1
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke.2520
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2502
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2504
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2510
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2516
+ ___67-[SPCoreSpotlightIndexer registerPostJournalPlaybackBGSTActivities]_block_invoke_2.2523
+ ___69-[SPCoreSpotlightIndexer revokeExpiredItems:protected:expirationRef:]_block_invoke
+ ___69-[SPCoreSpotlightIndexer revokeExpiredItems:protected:expirationRef:]_block_invoke_2
+ ___69-[SPCoreSpotlightIndexer revokeExpiredItems:protected:expirationRef:]_block_invoke_3
+ ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1028
+ ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1029
+ ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke_2.1032
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1486
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1493
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1493.cold.1
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1497
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1497.cold.1
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1498
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1514
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1518
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke_2.1517
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke_2.1521
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1340
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1351
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1341
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1346
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1354
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1354.cold.1
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1000
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1011
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1015
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.920
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.931
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.959
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.969
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.971
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.976
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.984
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.988
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.994
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1003
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.923
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.933
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.974
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.979
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.979.cold.1
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.987
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.991
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.997
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.924
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.936
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.975
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.983
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_4.927
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_4.939
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.1084
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_2.1087
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_3.1088
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_4.1095
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2632
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2636
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2635
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2637
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_3.2640
+ ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.2478
+ ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke_2.2479
+ ___81-[SPConcreteCoreSpotlightIndexer processDecryptsForBundleID:persona:infos:group:]_block_invoke.1198
+ ___81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2753
+ ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.3444
+ ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke_2.3447
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3383
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3383.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3385
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3387
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3387.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3388
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3389
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3389.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3390
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2838
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2849
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2872
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2906
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2910
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2914
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2940
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2948
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2961
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3150
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3231
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3235
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3236
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3240
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3244
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3263
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_10.3358
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_11.3359
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_12.3369
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_13.3370
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2852
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2962
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3154
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3224
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3294
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.2853
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.2972
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3158
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3298
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.2973
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3165
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3302
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5.3196
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5.3326
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_6.3197
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_6.3327
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_7.3200
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_7.3331
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_8.3210
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_8.3344
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_9.3349
+ ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1047
+ ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1048
+ ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2679
+ ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.2680
+ ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1436
+ ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1446
+ ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_2.1447
+ ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_3.1448
+ ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_4.1451
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2468
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2468.cold.1
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2469
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2473
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2474
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke_2.2475
+ ___block_descriptor_173_e8_32s40s48s56s64s72s80bs88bs96w_e29_v24?0"NSArray"8"NSError"16ls32l8s80l8s40l8s48l8s56l8s64l8s88l8s72l8w96l8
+ ___block_descriptor_174_e8_32s40s48s56s64bs72bs80r88r96w_e17_v16?0"NSError"8lw96l8r80l8s64l8s72l8r88l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_48_e8_32s_e40_v16?0"SPConcreteCoreSpotlightIndexer"8ls32l8
+ ___block_descriptor_57_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48w_e5_v8?0ls32l8w48l8s40l8
+ ___block_descriptor_92_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_96_e8_32s40s48s56s64w_e69_v48?0"SPQueryJob"8q16Q24^{__MDStoreOIDArray=}32^{__MDPlistBytes=}40lw64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.1005
+ ___block_literal_global.1017
+ ___block_literal_global.1184
+ ___block_literal_global.1187
+ ___block_literal_global.1194
+ ___block_literal_global.1197
+ ___block_literal_global.1247
+ ___block_literal_global.1292
+ ___block_literal_global.1302
+ ___block_literal_global.1331
+ ___block_literal_global.1334
+ ___block_literal_global.1427
+ ___block_literal_global.1574
+ ___block_literal_global.1640
+ ___block_literal_global.1668
+ ___block_literal_global.2165
+ ___block_literal_global.2170
+ ___block_literal_global.2188
+ ___block_literal_global.2192
+ ___block_literal_global.2211
+ ___block_literal_global.2213
+ ___block_literal_global.2216
+ ___block_literal_global.2233
+ ___block_literal_global.2249
+ ___block_literal_global.2251
+ ___block_literal_global.2255
+ ___block_literal_global.2280
+ ___block_literal_global.2287
+ ___block_literal_global.2298
+ ___block_literal_global.2320
+ ___block_literal_global.2435
+ ___block_literal_global.2439
+ ___block_literal_global.2455
+ ___block_literal_global.2459
+ ___block_literal_global.2467
+ ___block_literal_global.2498
+ ___block_literal_global.2506
+ ___block_literal_global.2542
+ ___block_literal_global.2544
+ ___block_literal_global.2550
+ ___block_literal_global.2571
+ ___block_literal_global.2615
+ ___block_literal_global.2669
+ ___block_literal_global.2682
+ ___block_literal_global.2786
+ ___block_literal_global.3105
+ ___block_literal_global.3110
+ ___block_literal_global.3115
+ ___block_literal_global.3129
+ ___block_literal_global.3399
+ ___block_literal_global.3460
+ ___block_literal_global.3478
+ ___block_literal_global.4064
+ ___block_literal_global.4108
+ ___block_literal_global.4202
+ ___block_literal_global.4210
+ ___block_literal_global.4212
+ ___block_literal_global.4243
+ ___block_literal_global.4250
+ ___block_literal_global.891
+ ___block_literal_global.894
+ ___block_literal_global.896
+ ___block_literal_global.916
+ ___block_literal_global.935
+ ___block_literal_global.938
+ ___block_literal_global.941
+ ___block_literal_global.961
+ ___block_literal_global.993
+ ___block_literal_global.999
+ ___collectSpotlightLogs_block_invoke.4129
+ ___processItemsForImportInner_block_invoke.4158
+ _mach_port_deallocate
+ _mach_task_self_
+ _objc_msgSend$isUnsafeQuery
+ _objc_msgSend$ownerToken
+ _objc_msgSend$registerPostJournalPlaybackBGSTActivities
+ _objc_msgSend$revokeExpiredItems:expirationRef:
+ _objc_msgSend$revokeExpiredItems:protected:expirationRef:
+ _objc_msgSend$setOwnerToken:
+ _taskABExpired
+ _taskExpired
+ _xpc_dictionary_copy_mach_send
- -[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]
- -[SPCoreSpotlightIndexer init].cold.6
- -[SPCoreSpotlightIndexer init].cold.7
- -[SPCoreSpotlightIndexer init].cold.8
- -[SPCoreSpotlightIndexer revokeExpiredItems:activity:protected:]
- GCC_except_table1021
- GCC_except_table1057
- GCC_except_table1063
- GCC_except_table1064
- GCC_except_table1070
- GCC_except_table1071
- GCC_except_table1072
- GCC_except_table1081
- GCC_except_table1096
- GCC_except_table1100
- GCC_except_table1110
- GCC_except_table1120
- GCC_except_table1127
- GCC_except_table1134
- GCC_except_table1141
- GCC_except_table1148
- GCC_except_table1164
- GCC_except_table1230
- GCC_except_table1232
- GCC_except_table1238
- GCC_except_table1285
- GCC_except_table1292
- GCC_except_table1414
- GCC_except_table1419
- GCC_except_table1420
- GCC_except_table1479
- GCC_except_table1482
- GCC_except_table1484
- GCC_except_table1485
- GCC_except_table1671
- GCC_except_table257
- GCC_except_table265
- GCC_except_table303
- GCC_except_table313
- GCC_except_table325
- GCC_except_table355
- GCC_except_table377
- GCC_except_table800
- GCC_except_table804
- GCC_except_table808
- GCC_except_table836
- GCC_except_table865
- GCC_except_table897
- GCC_except_table926
- GCC_except_table927
- GCC_except_table936
- GCC_except_table970
- ___101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke.1575
- ___101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke_2.1576
- ___105-[SPConcreteCoreSpotlightIndexer willModifySearchableItemsWithIdentifiers:forBundleID:completionHandler:]_block_invoke.1381
- ___105-[SPConcreteCoreSpotlightIndexer willModifySearchableItemsWithIdentifiers:forBundleID:completionHandler:]_block_invoke_2.1385
- ___107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.3433
- ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke.1622
- ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke_2.1613
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2566
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2568
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2568.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2571
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2571.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2572
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2572.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2573
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1535
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1544
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1562
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1565
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1536
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1553
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1563
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1566
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1566.cold.1
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1554
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1564
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_4.1555
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_5.1558
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_5.1558.cold.1
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1410
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1419
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1419.cold.1
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_2.1414
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_3.1415
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_4.1416
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_5.1417
- ___131-[SPConcreteCoreSpotlightIndexer persistDonationProgress:fromBundle:clientIndexName:personaID:canCreateNewIndex:completionHandler:]_block_invoke.1206
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1300
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1300.cold.1
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1300.cold.2
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1321
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1323
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1323.cold.1
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1323.cold.2
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1326
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1326.cold.1
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1326.cold.2
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke_2.1304
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke_2.1322
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1213
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1213.cold.1
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1213.cold.2
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1213.cold.3
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1213.cold.4
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1239
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1261
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1278
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1283
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1287
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1290
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1243
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1262
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1279
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1284
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1284.cold.1
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1291
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_3.1263
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_3.1294
- ___28-[CSSearchAgent startQuery:]_block_invoke.177
- ___28-[CSSearchAgent startQuery:]_block_invoke.177.cold.1
- ___28-[CSSearchAgent startQuery:]_block_invoke.177.cold.2
- ___28-[CSSearchAgent startQuery:]_block_invoke.177.cold.3
- ___28-[CSSearchAgent startQuery:]_block_invoke.215
- ___28-[CSSearchAgent startQuery:]_block_invoke.219
- ___28-[CSSearchAgent startQuery:]_block_invoke.229
- ___28-[CSSearchAgent startQuery:]_block_invoke.240
- ___28-[CSSearchAgent startQuery:]_block_invoke_2.227
- ___28-[CSSearchAgent startQuery:]_block_invoke_2.231
- ___28-[CSSearchAgent startQuery:]_block_invoke_2.231.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2245
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2258
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2267
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2271
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2276
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2277
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2282
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2294
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2301
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2302
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2312
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2316
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2321
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2321.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2322
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2327.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2328
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2335
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2336
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2342
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2344
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2345
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2350
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2351
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2352
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2352.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2357
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2366
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2376
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2379
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2254
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2263
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2280
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2297
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2305
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2319
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2325
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2331
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2346
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2346.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2354
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2354.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2358
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2377
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2380
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2255
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2255.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2308
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2362
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2378
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2378.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2381
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_4.2382
- ___31-[SPCoreSpotlightIndexer start]_block_invoke.2450
- ___39-[SPCoreSpotlightIndexer queryPreheat:]_block_invoke.2554
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.3446
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.3447
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_3.3450
- ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2189
- ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2189.cold.1
- ___50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke.1358
- ___50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke_2.1359
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2441
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2445
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2445.cold.1
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2445.cold.2
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2446
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2446.cold.1
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2447
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2447.cold.1
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2448
- ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1728
- ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1729
- ___57-[SPConcreteCoreSpotlightIndexer zombifyAllContactItems:]_block_invoke.1474
- ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke.2424
- ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke_2.2427
- ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke_3.2428
- ___60-[SPConcreteCoreSpotlightIndexer _addNewClientWithBundleID:]_block_invoke.1030
- ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke.1183
- ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_2.1186
- ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_3.1189
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.759
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.759.cold.1
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.760
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.760.cold.1
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.761
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.761.cold.1
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.762
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.768
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.cold.1
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke_2
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke_2.772
- ___63-[SPCoreSpotlightIndexer _deleteNonMailBundlesFromClassAIndex:]_block_invoke.2418
- ___64-[SPCoreSpotlightIndexer revokeExpiredItems:activity:protected:]_block_invoke
- ___64-[SPCoreSpotlightIndexer revokeExpiredItems:activity:protected:]_block_invoke_2
- ___64-[SPCoreSpotlightIndexer revokeExpiredItems:activity:protected:]_block_invoke_3
- ___65-[SPConcreteCoreSpotlightIndexer openIndexForUpgradeSynchronous:]_block_invoke.893
- ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2199
- ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2200
- ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1019
- ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1020
- ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke_2.1023
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1480
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1487
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1487.cold.1
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1491
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1491.cold.1
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1492
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1506
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1508
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke_2.1511
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke_2.1515
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1334
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1339
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1335
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1340
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1348
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1348.cold.1
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1002
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1006
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.911
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.922
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.950
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.960
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.962
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.967
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.975
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.979
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.985
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.991
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.914
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.924
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.961
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.965
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.970.cold.1
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.978
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.982
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.988
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.994
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.915
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.927
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.966
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.974
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_4.918
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_4.930
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.1075
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_2.1078
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_3.1079
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_4.1086
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2617
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2621
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2620
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2622
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_3.2625
- ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.2496
- ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke_2.2497
- ___81-[SPConcreteCoreSpotlightIndexer processDecryptsForBundleID:persona:infos:group:]_block_invoke.1192
- ___81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2738
- ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.3429
- ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke_2.3432
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3368
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3368.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3370
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3372
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3372.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3373
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3374
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3374.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3375
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2823
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2834
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2857
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2891
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2895
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2899
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2925
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2933
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2946
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3135
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3205
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3206
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3216
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3225
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3229
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3248
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_10.3343
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_11.3344
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_12.3354
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_13.3355
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2837
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2947
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3139
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3209
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3279
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.2838
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.2957
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3143
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3283
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.2958
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3150
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3287
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5.3181
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5.3311
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_6.3182
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_6.3312
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_7.3185
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_7.3316
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_8.3195
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_8.3329
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_9.3334
- ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1038
- ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1039
- ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2664
- ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.2665
- ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1430
- ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1440
- ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_2.1441
- ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_3.1442
- ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_4.1445
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2486
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2486.cold.1
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2487
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2491
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2492
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke_2.2493
- ___block_descriptor_104_e8_32s40s48s56s64s72r80w_e69_v48?0"SPQueryJob"8q16Q24^{__MDStoreOIDArray=}32^{__MDPlistBytes=}40lw80l8s32l8r72l8s40l8s48l8s56l8s64l8
- ___block_descriptor_169_e8_32s40s48s56s64s72s80bs88bs96w_e29_v24?0"NSArray"8"NSError"16ls32l8s80l8s40l8s48l8s56l8s64l8s88l8s72l8w96l8
- ___block_descriptor_170_e8_32s40s48s56s64bs72bs80r88r96w_e17_v16?0"NSError"8lw96l8r80l8s64l8s72l8r88l8s32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48r56w_e5_v8?0lr48l8s32l8w56l8s40l8
- ___block_descriptor_72_e8_32s40s48r56w_e69_v48?0"SPQueryJob"8q16Q24^{__MDStoreOIDArray=}32^{__MDPlistBytes=}40lw56l8r48l8s32l8s40l8
- ___block_descriptor_88_e8_32bs_e17_v16?0"NSError"8ls32l8
- ___block_literal_global.1008
- ___block_literal_global.1178
- ___block_literal_global.1181
- ___block_literal_global.1185
- ___block_literal_global.1188
- ___block_literal_global.1241
- ___block_literal_global.1286
- ___block_literal_global.1296
- ___block_literal_global.1325
- ___block_literal_global.1328
- ___block_literal_global.1421
- ___block_literal_global.1568
- ___block_literal_global.1634
- ___block_literal_global.1662
- ___block_literal_global.2158
- ___block_literal_global.2163
- ___block_literal_global.2181
- ___block_literal_global.2185
- ___block_literal_global.2202
- ___block_literal_global.2204
- ___block_literal_global.2206
- ___block_literal_global.2226
- ___block_literal_global.2242
- ___block_literal_global.2244
- ___block_literal_global.2248
- ___block_literal_global.2273
- ___block_literal_global.2304
- ___block_literal_global.2315
- ___block_literal_global.2356
- ___block_literal_global.2453
- ___block_literal_global.2457
- ___block_literal_global.2473
- ___block_literal_global.2477
- ___block_literal_global.2503
- ___block_literal_global.2520
- ___block_literal_global.2527
- ___block_literal_global.2529
- ___block_literal_global.2556
- ___block_literal_global.2600
- ___block_literal_global.2654
- ___block_literal_global.2667
- ___block_literal_global.2771
- ___block_literal_global.3070
- ___block_literal_global.3075
- ___block_literal_global.3080
- ___block_literal_global.3114
- ___block_literal_global.3384
- ___block_literal_global.3445
- ___block_literal_global.3463
- ___block_literal_global.4047
- ___block_literal_global.4091
- ___block_literal_global.4185
- ___block_literal_global.4193
- ___block_literal_global.4195
- ___block_literal_global.4226
- ___block_literal_global.4233
- ___block_literal_global.882
- ___block_literal_global.885
- ___block_literal_global.887
- ___block_literal_global.907
- ___block_literal_global.920
- ___block_literal_global.926
- ___block_literal_global.932
- ___block_literal_global.952
- ___block_literal_global.984
- ___block_literal_global.990
- ___block_literal_global.996
- ___collectSpotlightLogs_block_invoke.4112
- ___processItemsForImportInner_block_invoke.4141
- _objc_msgSend$revokeExpiredItems:activity:
- _objc_msgSend$revokeExpiredItems:activity:protected:
CStrings:
+ "### calculateDirectorySize %llu"
+ "###calculateDirectorySize %s: fsctl failed errno: %d"
+ "*warn* Failed to get index size for %s. err=%d"
+ ".dropped.%d.log"
+ ".dropped.1.log"
+ "/AppleInternal/Library/BuildRoots/4~CJI8ugDTCqHvTcF02m5GArYOeCq95FQ6fsbJ4UE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI8ugDTCqHvTcF02m5GArYOeCq95FQ6fsbJ4UE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI8ugDTCqHvTcF02m5GArYOeCq95FQ6fsbJ4UE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI8ugDTCqHvTcF02m5GArYOeCq95FQ6fsbJ4UE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:412: libc++ Hardening assertion __pos < size() failed: string_view[] index out of bounds\n"
+ "CacheDelete: NOT allowing purge for %s: %llu/%llu"
+ "CacheDelete: allowing purge for %s: %llu/%llu"
+ "Failed to expire task with error"
+ "Marked BGST activity:%@ as deferred"
+ "com.apple.intelligenceflow.intelligenceflowd"
+ "isUnsafeQuery"
+ "ot"
+ "ownerToken"
+ "registerPostJournalPlaybackBGSTActivities"
+ "revokeExpiredItems:expirationRef:"
+ "revokeExpiredItems:protected:expirationRef:"
+ "setOwnerToken:"
+ "v32@0:8@16^B24"
+ "v36@0:8@16B24^B28"
- "/AppleInternal/Library/BuildRoots/4~CIU-ugCx5Jy9nZVdHPgVksRmwqNy2ZXscLHgAPk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CIU-ugCx5Jy9nZVdHPgVksRmwqNy2ZXscLHgAPk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CIU-ugCx5Jy9nZVdHPgVksRmwqNy2ZXscLHgAPk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CIU-ugCx5Jy9nZVdHPgVksRmwqNy2ZXscLHgAPk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:412: libc++ Hardening assertion __pos < size() failed: string_view[] index out of bounds\n"
- "Marked XPC activity:%s as deferred"
- "revokeExpiredItems:activity:"
- "revokeExpiredItems:activity:protected:"

```
