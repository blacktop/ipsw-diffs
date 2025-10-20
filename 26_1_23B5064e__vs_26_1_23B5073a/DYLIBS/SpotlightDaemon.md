## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2400.13.1.101.0
-  __TEXT.__text: 0xaa914
-  __TEXT.__auth_stubs: 0x1ec0
-  __TEXT.__objc_methlist: 0x439c
-  __TEXT.__const: 0x388
-  __TEXT.__cstring: 0x8123
-  __TEXT.__oslogstring: 0xa565
-  __TEXT.__gcc_except_tab: 0x418c
+2400.14.100.0.0
+  __TEXT.__text: 0xb048c
+  __TEXT.__auth_stubs: 0x1f00
+  __TEXT.__objc_methlist: 0x444c
+  __TEXT.__const: 0x398
+  __TEXT.__cstring: 0x85dc
+  __TEXT.__oslogstring: 0xab32
+  __TEXT.__gcc_except_tab: 0x42d4
   __TEXT.__dlopen_cstrs: 0x4a
-  __TEXT.__unwind_info: 0x2220
+  __TEXT.__unwind_info: 0x22b8
   __TEXT.__objc_classname: 0x4dd
-  __TEXT.__objc_methname: 0xec10
-  __TEXT.__objc_methtype: 0x25cb
-  __TEXT.__objc_stubs: 0xba00
-  __DATA_CONST.__got: 0xaf0
-  __DATA_CONST.__const: 0x3d20
+  __TEXT.__objc_methname: 0xecb7
+  __TEXT.__objc_methtype: 0x25e7
+  __TEXT.__objc_stubs: 0xba80
+  __DATA_CONST.__got: 0xae0
+  __DATA_CONST.__const: 0x3d48
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35c8
+  __DATA_CONST.__objc_selrefs: 0x35e8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x100
-  __DATA_CONST.__objc_arraydata: 0x2e8
-  __AUTH_CONST.__auth_got: 0xf78
-  __AUTH_CONST.__const: 0x10c8
-  __AUTH_CONST.__cfstring: 0x6da0
-  __AUTH_CONST.__objc_const: 0x5b88
+  __DATA_CONST.__objc_arraydata: 0x358
+  __AUTH_CONST.__auth_got: 0xf98
+  __AUTH_CONST.__const: 0x10a8
+  __AUTH_CONST.__cfstring: 0x7700
+  __AUTH_CONST.__objc_const: 0x5b68
   __AUTH_CONST.__objc_arrayobj: 0x3d8
-  __AUTH_CONST.__objc_intobj: 0x210
-  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__objc_intobj: 0x240
+  __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x470
+  __DATA.__objc_ivar: 0x46c
   __DATA.__data: 0x868
-  __DATA.__bss: 0x10c
+  __DATA.__bss: 0x104
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0xd70
-  __DATA_DIRTY.__data: 0x158
+  __DATA_DIRTY.__data: 0x2e8
   __DATA_DIRTY.__bss: 0x5f8
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: BD27E7D7-E577-32EF-B5CD-01B204C3F68F
-  Functions: 2807
-  Symbols:   9616
-  CStrings:  5735
+  UUID: 6FC5AB95-B759-3A5F-A670-3D2BE6CDC7BA
+  Functions: 2861
+  Symbols:   9738
+  CStrings:  5920
 
Symbols:
+ -[SPConcreteCoreSpotlightIndexer getAggregateIndexWipeCount]
+ -[SPConcreteCoreSpotlightIndexer getIndexDirectorySize:]
+ -[SPConcreteCoreSpotlightIndexer getIndexDirectorySize:].cold.1
+ -[SPConcreteCoreSpotlightIndexer getIndexDirectorySize:].cold.2
+ -[SPConcreteCoreSpotlightIndexer incrementIndexWipeCount]
+ -[SPConcreteCoreSpotlightIndexer incrementIndexWipeCount].cold.1
+ -[SPConcreteCoreSpotlightIndexer indexLossAnalyticsDictWithPreviousIndexCreationDate:size:openingInReadOnly:fullyCreated:markedPurgeable:vectorIndexDrop:forAnalytics:]
+ -[SPConcreteCoreSpotlightIndexer indexLossAnalyticsDictWithPreviousIndexCreationDate:size:openingInReadOnly:fullyCreated:markedPurgeable:vectorIndexDrop:forAnalytics:].cold.1
+ -[SPConcreteCoreSpotlightIndexer indexLossAnalyticsDictWithPreviousIndexCreationDate:size:openingInReadOnly:fullyCreated:markedPurgeable:vectorIndexDrop:forAnalytics:].cold.2
+ -[SPConcreteCoreSpotlightIndexer indexLossAnalyticsDictWithPreviousIndexCreationDate:size:openingInReadOnly:fullyCreated:markedPurgeable:vectorIndexDrop:forAnalytics:].cold.3
+ -[SPConcreteCoreSpotlightIndexer indexLossAnalyticsDictWithPreviousIndexCreationDate:size:openingInReadOnly:fullyCreated:markedPurgeable:vectorIndexDrop:forAnalytics:].cold.4
+ -[SPConcreteCoreSpotlightIndexer indexLossAnalyticsDictWithPreviousIndexCreationDate:size:openingInReadOnly:fullyCreated:markedPurgeable:vectorIndexDrop:forAnalytics:].cold.5
+ -[SPConcreteCoreSpotlightIndexer indexLossAnalyticsDictWithPreviousIndexCreationDate:size:openingInReadOnly:fullyCreated:markedPurgeable:vectorIndexDrop:forAnalytics:].cold.6
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:].cold.14
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:].cold.15
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:].cold.16
+ -[SPConcreteCoreSpotlightIndexer shouldNotLogIndexDrop:ignoreParentDirectoryAge:]
+ -[SPConcreteCoreSpotlightIndexer vectorIndexDropsPath]
+ -[SPConcreteCoreSpotlightIndexer writeIndexCreationDate:]
+ -[SPConcreteCoreSpotlightIndexer writeIndexCreationDate:].cold.1
+ -[SPConcreteCoreSpotlightIndexer writeIndexCreationDate:].cold.2
+ -[SPConcreteCoreSpotlightIndexer writeIndexDropAnalyticsDate:]
+ -[SPConcreteCoreSpotlightIndexer writeIndexDropAnalyticsDate:].cold.1
+ -[SPConcreteCoreSpotlightIndexer writeIndexLossEventToFile:vector:]
+ -[SPConcreteCoreSpotlightIndexer writeIndexLossEventToFile:vector:].cold.1
+ -[SPConcreteCoreSpotlightIndexer writeIndexLossEventToFile:vector:].cold.2
+ -[SPConcreteCoreSpotlightIndexer writeIndexLossEventToFile:vector:].cold.3
+ -[SPConcreteCoreSpotlightIndexer writeIndexLossEventToFile:vector:].cold.4
+ -[SPConcreteCoreSpotlightIndexer writeIndexLossEventToFile:vector:].cold.5
+ -[SPConcreteCoreSpotlightIndexer writeIndexLossEventToFile:vector:].cold.6
+ -[SPConcreteCoreSpotlightIndexer writeIndexSuccessfulOpenDate:]
+ -[SPConcreteCoreSpotlightIndexer writeIndexSuccessfulOpenDate:].cold.1
+ -[SPConcreteCoreSpotlightIndexer writeSDBObjectCount:]
+ -[SPConcreteCoreSpotlightIndexer writeSDBObjectCount:].cold.1
+ -[SPCoreSpotlightIndexer dumpIndexAgesAtPath:]
+ -[SPCoreSpotlightIndexer dumpIndexAges]
+ -[SPCoreSpotlightIndexer dumpIndexAnalyticsAtPath:]
+ -[SPCoreSpotlightIndexer dumpIndexAnalytics]
+ -[SPCoreSpotlightIndexer issueHeartbeat].cold.1
+ -[SPCoreSpotlightIndexer sendAnalytics:]
+ GCC_except_table1008
+ GCC_except_table1013
+ GCC_except_table1018
+ GCC_except_table1023
+ GCC_except_table1029
+ GCC_except_table1045
+ GCC_except_table1099
+ GCC_except_table1101
+ GCC_except_table1106
+ GCC_except_table1147
+ GCC_except_table1153
+ GCC_except_table1267
+ GCC_except_table1268
+ GCC_except_table1336
+ GCC_except_table1339
+ GCC_except_table1341
+ GCC_except_table1342
+ GCC_except_table1509
+ GCC_except_table1538
+ GCC_except_table234
+ GCC_except_table236
+ GCC_except_table238
+ GCC_except_table249
+ GCC_except_table257
+ GCC_except_table287
+ GCC_except_table294
+ GCC_except_table304
+ GCC_except_table329
+ GCC_except_table349
+ GCC_except_table376
+ GCC_except_table377
+ GCC_except_table386
+ GCC_except_table387
+ GCC_except_table430
+ GCC_except_table446
+ GCC_except_table455
+ GCC_except_table457
+ GCC_except_table458
+ GCC_except_table489
+ GCC_except_table513
+ GCC_except_table532
+ GCC_except_table533
+ GCC_except_table541
+ GCC_except_table584
+ GCC_except_table585
+ GCC_except_table586
+ GCC_except_table611
+ GCC_except_table672
+ GCC_except_table696
+ GCC_except_table722
+ GCC_except_table726
+ GCC_except_table730
+ GCC_except_table758
+ GCC_except_table784
+ GCC_except_table801
+ GCC_except_table814
+ GCC_except_table838
+ GCC_except_table839
+ GCC_except_table847
+ GCC_except_table883
+ GCC_except_table922
+ GCC_except_table953
+ GCC_except_table957
+ GCC_except_table958
+ GCC_except_table965
+ GCC_except_table966
+ GCC_except_table974
+ GCC_except_table987
+ GCC_except_table999
+ _MDBootTime
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _SIGetObjectCount
+ __CFURLGetVolumePropertyFlags
+ __SIGetFieldNameForId
+ __SISetVectorIndexDropCallback
+ ___101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke.1529
+ ___105-[SPConcreteCoreSpotlightIndexer willModifySearchableItemsWithIdentifiers:forBundleID:completionHandler:]_block_invoke.1378
+ ___107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.3176
+ ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke.1569
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2447
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2449
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2449.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2452
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2452.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2453
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2453.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2454
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1498
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1506
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1512
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1518
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1521
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1513
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1519
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1522
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1522.cold.1
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1514
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1514.cold.1
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1520
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1402
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1410
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1410.cold.1
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_2.1406
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_3.1407
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_4.1408
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1318
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1318.cold.1
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1318.cold.2
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1337
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1339
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1339.cold.1
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1339.cold.2
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1342
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1342.cold.1
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1342.cold.2
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1345
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke_2.1338
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1233
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1233.cold.1
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1233.cold.2
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1233.cold.3
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1233.cold.4
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1260
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1272
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1301
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1306
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1310
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1313
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1284
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1302
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1307
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1307.cold.1
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1314
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_3.1285
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_4.1286
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2165
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2178
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2187
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2191
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2196
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2197
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2198
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2210
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2214
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2215
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2222
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2226
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2228
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2228.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2229
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2231
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2231.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2232
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2234
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2234.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2238
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2240
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2241
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2246
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2246.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2246.cold.2
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2247
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2254
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2257
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2262
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2269
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2270
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2275
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2275.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2275.cold.2
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2174
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2183
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2218
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2223
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2242
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2242.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2255
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2258
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2258.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2272
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2272.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2279
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2175
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2175.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2256
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2256.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2280
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_7
+ ___31-[SPCoreSpotlightIndexer start]_block_invoke.2341
+ ___39-[SPCoreSpotlightIndexer queryPreheat:]_block_invoke.2438
+ ___40+[SPCoreSpotlightIndexer sharedInstance]_block_invoke.cold.2
+ ___40+[SPCoreSpotlightIndexer sharedInstance]_block_invoke.cold.3
+ ___40+[SPCoreSpotlightIndexer sharedInstance]_block_invoke.cold.4
+ ___40+[SPCoreSpotlightIndexer sharedInstance]_block_invoke.cold.5
+ ___40-[SPCoreSpotlightIndexer issueHeartbeat]_block_invoke
+ ___40-[SPCoreSpotlightIndexer issueHeartbeat]_block_invoke.2405
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.3187
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.3188
+ ___40-[SPCoreSpotlightIndexer sendAnalytics:]_block_invoke
+ ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2112
+ ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2112.cold.1
+ ___46-[SPCoreSpotlightIndexer dumpIndexAgesAtPath:]_block_invoke
+ ___50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke.1366
+ ___51-[SPCoreSpotlightIndexer dumpIndexAnalyticsAtPath:]_block_invoke
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2332
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2336
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2336.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2336.cold.2
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2337
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2337.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2338
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2338.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2339
+ ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1655
+ ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1656
+ ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke.2320
+ ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke_2.2321
+ ___60-[SPConcreteCoreSpotlightIndexer _addNewClientWithBundleID:]_block_invoke.1075
+ ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke.1209
+ ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_2.1212
+ ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_3.1215
+ ___63-[SPCoreSpotlightIndexer _deleteNonMailBundlesFromClassAIndex:]_block_invoke.2316
+ ___65-[SPConcreteCoreSpotlightIndexer openIndexForUpgradeSynchronous:]_block_invoke.967
+ ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2122
+ ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2123
+ ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1069
+ ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1070
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1456
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1456.cold.1
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1460
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1460.cold.1
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1461
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1475
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1477
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1478
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1482
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1348
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1352
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1358
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1358.cold.1
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1353
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1024
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1030
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1032
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1034
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1034.cold.1
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1039
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1040
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1043
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1046
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1054
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1058
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.985
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.990
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1031
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1033
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1038
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.986
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.992
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.995
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_4.998
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.1108
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_2.1109
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_3.1116
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_3.1116.cold.1
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2489
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2490
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2491
+ ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.2370
+ ___81-[SPConcreteCoreSpotlightIndexer processDecryptsForBundleID:persona:infos:group:]_block_invoke.1218
+ ___81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2572
+ ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.3175
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3124
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3124.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3126
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3128
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3128.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3129
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3130
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3130.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3131
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2657
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2664
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2684
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2718
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2722
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2726
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2746
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2758
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2998
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2999
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3006
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3010
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3011
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3015
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3019
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3038
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2665
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2750
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2772
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3060
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3064
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3088
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5.3089
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_6.3093
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_7.3106
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_8.3111
+ ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1079
+ ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1080
+ ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2518
+ ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.2519
+ ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1417
+ ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1427
+ ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_2.1428
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2363
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2363.cold.1
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2364
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2368
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2369
+ ___block_descriptor_32_e12_v20?0I8^v12l
+ ___block_descriptor_40_e8_32s_e26_"NSMutableDictionary"8?0ls32l8
+ ___block_descriptor_48_e8_32s_e15_v32?0816^B24ls32l8
+ ___block_literal_global.1000
+ ___block_literal_global.1042
+ ___block_literal_global.1045
+ ___block_literal_global.1048
+ ___block_literal_global.1060
+ ___block_literal_global.1204
+ ___block_literal_global.1207
+ ___block_literal_global.1211
+ ___block_literal_global.1214
+ ___block_literal_global.1217
+ ___block_literal_global.1262
+ ___block_literal_global.1274
+ ___block_literal_global.1309
+ ___block_literal_global.1316
+ ___block_literal_global.1341
+ ___block_literal_global.1344
+ ___block_literal_global.1412
+ ___block_literal_global.1524
+ ___block_literal_global.1579
+ ___block_literal_global.1589
+ ___block_literal_global.2093
+ ___block_literal_global.2098
+ ___block_literal_global.2104
+ ___block_literal_global.2108
+ ___block_literal_global.2125
+ ___block_literal_global.2127
+ ___block_literal_global.2129
+ ___block_literal_global.2132
+ ___block_literal_global.2149
+ ___block_literal_global.2162
+ ___block_literal_global.2164
+ ___block_literal_global.2168
+ ___block_literal_global.2193
+ ___block_literal_global.2217
+ ___block_literal_global.2225
+ ___block_literal_global.2274
+ ___block_literal_global.2278
+ ___block_literal_global.2344
+ ___block_literal_global.2358
+ ___block_literal_global.2360
+ ___block_literal_global.2362
+ ___block_literal_global.2372
+ ___block_literal_global.2424
+ ___block_literal_global.2429
+ ___block_literal_global.2431
+ ___block_literal_global.2433
+ ___block_literal_global.2440
+ ___block_literal_global.2476
+ ___block_literal_global.2514
+ ___block_literal_global.2521
+ ___block_literal_global.2605
+ ___block_literal_global.2890
+ ___block_literal_global.2895
+ ___block_literal_global.2900
+ ___block_literal_global.2905
+ ___block_literal_global.2910
+ ___block_literal_global.2915
+ ___block_literal_global.2920
+ ___block_literal_global.2925
+ ___block_literal_global.2930
+ ___block_literal_global.3134
+ ___block_literal_global.3186
+ ___block_literal_global.3199
+ ___block_literal_global.3775
+ ___block_literal_global.3845
+ ___block_literal_global.3894
+ ___block_literal_global.3902
+ ___block_literal_global.3904
+ ___block_literal_global.3941
+ ___block_literal_global.3948
+ ___block_literal_global.939
+ ___block_literal_global.958
+ ___block_literal_global.961
+ ___block_literal_global.963
+ ___block_literal_global.981
+ ___block_literal_global.988
+ ___block_literal_global.994
+ ___block_literal_global.997
+ ___processItemsForImportInner_block_invoke.3862
+ ___reportVectorIndexDrop_block_invoke
+ _createResetTouchFileForUUID
+ _indexHeartbeatPath
+ _indexOpenRecordPath
+ _newHeartbeatDict
+ _newHeartbeatDict.cold.1
+ _newIndexOpensDict
+ _objc_msgSend$dumpIndexAges
+ _objc_msgSend$dumpIndexAgesAtPath:
+ _objc_msgSend$dumpIndexAnalytics
+ _objc_msgSend$dumpIndexAnalyticsAtPath:
+ _objc_msgSend$getAggregateIndexWipeCount
+ _objc_msgSend$getIndexDirectorySize:
+ _objc_msgSend$incrementIndexWipeCount
+ _objc_msgSend$indexLossAnalyticsDictWithPreviousIndexCreationDate:size:openingInReadOnly:fullyCreated:markedPurgeable:vectorIndexDrop:forAnalytics:
+ _objc_msgSend$initWithTimeIntervalSince1970:
+ _objc_msgSend$lastLoadedBundleVersion
+ _objc_msgSend$numberWithLong:
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$shouldNotLogIndexDrop:ignoreParentDirectoryAge:
+ _objc_msgSend$vectorIndexDropsPath
+ _objc_msgSend$writeIndexCreationDate:
+ _objc_msgSend$writeIndexDropAnalyticsDate:
+ _objc_msgSend$writeIndexLossEventToFile:vector:
+ _objc_msgSend$writeIndexSuccessfulOpenDate:
+ _objc_msgSend$writeSDBObjectCount:
+ _pthread_rwlock_rdlock
+ _sIndexHeartbeatLock
+ _sIndexOpenRecordLock
+ _sRootsInstalled
- -[SPConcreteCoreSpotlightIndexer _shouldPurge].cold.1
- -[SPCoreSpotlightIndexer analytics]
- GCC_except_table1000
- GCC_except_table1006
- GCC_except_table1022
- GCC_except_table1076
- GCC_except_table1078
- GCC_except_table1083
- GCC_except_table1124
- GCC_except_table1130
- GCC_except_table1244
- GCC_except_table1245
- GCC_except_table1293
- GCC_except_table1296
- GCC_except_table1298
- GCC_except_table1299
- GCC_except_table1454
- GCC_except_table1483
- GCC_except_table218
- GCC_except_table220
- GCC_except_table222
- GCC_except_table235
- GCC_except_table243
- GCC_except_table271
- GCC_except_table278
- GCC_except_table288
- GCC_except_table313
- GCC_except_table333
- GCC_except_table360
- GCC_except_table361
- GCC_except_table371
- GCC_except_table372
- GCC_except_table400
- GCC_except_table428
- GCC_except_table431
- GCC_except_table440
- GCC_except_table442
- GCC_except_table474
- GCC_except_table483
- GCC_except_table503
- GCC_except_table517
- GCC_except_table526
- GCC_except_table569
- GCC_except_table570
- GCC_except_table571
- GCC_except_table595
- GCC_except_table656
- GCC_except_table680
- GCC_except_table709
- GCC_except_table713
- GCC_except_table717
- GCC_except_table744
- GCC_except_table770
- GCC_except_table787
- GCC_except_table800
- GCC_except_table824
- GCC_except_table825
- GCC_except_table833
- GCC_except_table860
- GCC_except_table899
- GCC_except_table930
- GCC_except_table934
- GCC_except_table935
- GCC_except_table941
- GCC_except_table942
- GCC_except_table943
- GCC_except_table944
- GCC_except_table951
- GCC_except_table976
- GCC_except_table985
- GCC_except_table995
- _OBJC_CLASS_$_CSIdentifierCodedArray
- _OBJC_CLASS_$_SIAnalytics
- _OBJC_IVAR_$_SPCoreSpotlightIndexer._analytics
- _SIGetIndexDirectorySize
- __BootTimeDate
- ___101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke.1341
- ___105-[SPConcreteCoreSpotlightIndexer willModifySearchableItemsWithIdentifiers:forBundleID:completionHandler:]_block_invoke.1192
- ___107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.2951
- ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke.1381
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2205
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2207
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2207.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2210
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2210.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2211
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2211.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2212
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1310
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1318
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1324
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1330
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1333
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1325
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1331
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1334
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1334.cold.1
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1326
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1326.cold.1
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1332
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1216
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1224
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1224.cold.1
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_2.1220
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_3.1221
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_4.1222
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1131
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1131.cold.1
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1131.cold.2
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1151
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1153
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1153.cold.1
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1153.cold.2
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1156
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1156.cold.1
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1156.cold.2
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1159
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke_2.1152
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1046
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1046.cold.1
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1046.cold.2
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1046.cold.3
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1046.cold.4
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1073
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1085
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1114
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1119
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1123
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1126
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1097
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1115
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1120
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1120.cold.1
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1127
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_3.1098
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_4.1099
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.1964
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.1977
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.1991
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.1995
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2000
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2001
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2002
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2014
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2018
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2019
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2026
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2030
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2032
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2032.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2033
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2035
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2035.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2036
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2040
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2041
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2047
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2049
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2050
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2055
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2055.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2055.cold.2
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2056
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2063
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2066
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2071
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2078
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2079
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2084
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.1973
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.1978
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2022
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2027
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2051
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2051.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2064
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2067
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2067.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2081
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2081.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2085
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.1974
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.1974.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.1979
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2065
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2065.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2086
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_4.2087
- ___31-[SPCoreSpotlightIndexer start]_block_invoke.2148
- ___39-[SPCoreSpotlightIndexer queryPreheat:]_block_invoke.2196
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.2962
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.2963
- ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.1911
- ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.1911.cold.1
- ___50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke.1180
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2139
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2143
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2143.cold.1
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2143.cold.2
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2144
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2144.cold.1
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2145
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2145.cold.1
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2146
- ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1467
- ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1468
- ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke.2127
- ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke_2.2128
- ___60-[SPConcreteCoreSpotlightIndexer _addNewClientWithBundleID:]_block_invoke.888
- ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke.1022
- ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_2.1025
- ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_3.1028
- ___63-[SPCoreSpotlightIndexer _deleteNonMailBundlesFromClassAIndex:]_block_invoke.2123
- ___65-[SPConcreteCoreSpotlightIndexer openIndexForUpgradeSynchronous:]_block_invoke.789
- ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.1921
- ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.1922
- ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.882
- ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.883
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1270
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1270.cold.1
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1274
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1274.cold.1
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1275
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1287
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1289
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1290
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1294
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1162
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1166
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1172
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1172.cold.1
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1167
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.809
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.814
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.843
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.845
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.847
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.847.cold.1
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.852
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.853
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.856
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.859
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.867
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.871
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.810
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.816
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.844
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.846
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.851
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.819
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_4.822
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.921
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_2.922
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_3.929
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_3.929.cold.1
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2247
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2248
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2249
- ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.2177
- ___81-[SPConcreteCoreSpotlightIndexer processDecryptsForBundleID:persona:infos:group:]_block_invoke.1031
- ___81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2334
- ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.2950
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2899
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2899.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2901
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2903
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2903.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2904
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2905
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2905.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2906
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2419
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2426
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2446
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2480
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2484
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2488
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2508
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2520
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2533
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2763
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2764
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2775
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2776
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2780
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2784
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2803
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2427
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2512
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2534
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2834
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.2838
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.2862
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5.2863
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_6.2867
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_7.2881
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_8.2886
- ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.892
- ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.893
- ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2276
- ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.2277
- ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1231
- ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1241
- ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_2.1242
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2170
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2170.cold.1
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2171
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2175
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2176
- ___block_descriptor_32_e17_v32?0^8^16^24l
- ___block_descriptor_48_e8_32s40w_e31_v16?0"BGRepeatingSystemTask"8lw40l8s32l8
- ___block_literal_global.1017
- ___block_literal_global.1020
- ___block_literal_global.1024
- ___block_literal_global.1027
- ___block_literal_global.1030
- ___block_literal_global.1075
- ___block_literal_global.1087
- ___block_literal_global.1122
- ___block_literal_global.1129
- ___block_literal_global.1155
- ___block_literal_global.1158
- ___block_literal_global.1226
- ___block_literal_global.1336
- ___block_literal_global.1391
- ___block_literal_global.1401
- ___block_literal_global.1892
- ___block_literal_global.1897
- ___block_literal_global.1903
- ___block_literal_global.1907
- ___block_literal_global.1924
- ___block_literal_global.1926
- ___block_literal_global.1928
- ___block_literal_global.1931
- ___block_literal_global.1948
- ___block_literal_global.1961
- ___block_literal_global.1963
- ___block_literal_global.1967
- ___block_literal_global.1982
- ___block_literal_global.1997
- ___block_literal_global.2021
- ___block_literal_global.2029
- ___block_literal_global.2043
- ___block_literal_global.2083
- ___block_literal_global.2151
- ___block_literal_global.2165
- ___block_literal_global.2167
- ___block_literal_global.2169
- ___block_literal_global.2179
- ___block_literal_global.2182
- ___block_literal_global.2187
- ___block_literal_global.2189
- ___block_literal_global.2191
- ___block_literal_global.2198
- ___block_literal_global.2234
- ___block_literal_global.2272
- ___block_literal_global.2279
- ___block_literal_global.2367
- ___block_literal_global.2655
- ___block_literal_global.2660
- ___block_literal_global.2665
- ___block_literal_global.2670
- ___block_literal_global.2675
- ___block_literal_global.2680
- ___block_literal_global.2685
- ___block_literal_global.2690
- ___block_literal_global.2695
- ___block_literal_global.2909
- ___block_literal_global.2961
- ___block_literal_global.2974
- ___block_literal_global.3548
- ___block_literal_global.3601
- ___block_literal_global.3651
- ___block_literal_global.3659
- ___block_literal_global.3661
- ___block_literal_global.3689
- ___block_literal_global.3696
- ___block_literal_global.758
- ___block_literal_global.780
- ___block_literal_global.783
- ___block_literal_global.785
- ___block_literal_global.805
- ___block_literal_global.812
- ___block_literal_global.818
- ___block_literal_global.821
- ___block_literal_global.824
- ___block_literal_global.855
- ___block_literal_global.858
- ___block_literal_global.861
- ___block_literal_global.873
- ___processItemsForImportInner_block_invoke.3619
- ___updatedFrom2024Seed_block_invoke.cold.3
- __getCountsForItems
- _is2024Seed.cold.2
- _is2024Seed.cold.3
- _objc_msgSend$addCount
- _objc_msgSend$getCurrentSpotlightVersionWithRoots:
- _objc_msgSend$getPreviousBuild
- _objc_msgSend$initWithDeletes:
- _objc_msgSend$initWithParentDirectoryPath:corespotlight:heartbeatIndex:resourcesCallback:
- _objc_msgSend$otaBundleVersion
- _objc_msgSend$recordRequestsForIndex:adds:updates:deletes:
- _objc_msgSend$reportHeartbeats
- _objc_msgSend$runCommand:
- _objc_msgSend$sendHeartbeatEvent
- _objc_msgSend$sendIndexDropEventWithCorruptIndex:path:readOnly:reason:
- _objc_msgSend$setPurgeability:forIndex:
- _objc_msgSend$trialSpotlightRolloutID
- _objc_msgSend$trialSpotlightTreatmentID
- _objc_msgSend$updateCount
CStrings:
+ "\nCoreSpotlight Indexes Age Info:\n%@\n"
+ "\nCoreSpotlight Indexes Analytics Info:\n%@\n"
+ "%@\n%@"
+ "%@/Library/Logs/CrashReporter/DiagnosticLogs/Search"
+ "%@/heartbeat.plist"
+ "%@/indexOpenRecord.plist"
+ "%@/spotlight_%@index_drop.%@.%d.%@.%@.%03d.txt"
+ "%@/spotlight_%@index_drop.%@.%d.%@.%@.txt"
+ "%@/vectorIndexDrops.plist"
+ "%u"
+ "2400.14.100"
+ "=== Spotlight Diagnostic (%d) %@\n\n"
+ "@\"NSMutableDictionary\"8@?0"
+ "@56@0:8q16q24B32B36B40@44B52"
+ "CX"
+ "Did not find heartbeat file"
+ "EmbeddingDonation"
+ "Error %@ writing index creation date"
+ "Error %@ writing index creation date for %@"
+ "Error %@ writing index drop analytics date for %@"
+ "Error %@ writing index info"
+ "Error %@ writing index object count for %@"
+ "Error %@ writing index successful open date for %@"
+ "Error fetching parent directory age: %d"
+ "Error getting parent directory age: %d"
+ "Failed to delete vectorIndexDrops.plist (%u, %@)"
+ "Failed to get age of heartbeat file"
+ "Failed to get age of index directory"
+ "Failed to get build number"
+ "Failed to get previous build"
+ "Failed to get properties of corrupted index, err: %d"
+ "Failed to obtain index file info:%s (%s)"
+ "Getting total size of all index files in %@"
+ "ProductBuildVersion"
+ "TextSemanticSearch"
+ "[IndexLoss] (%@) Created intentional drop touch file %@"
+ "[IndexLoss] (%@) Failed to create index drop touch file %@ : %d"
+ "[IndexLoss] (%@) Trial intentional drop for %@"
+ "[IndexLoss] (%s) Failed to get FS info, err:%d"
+ "[IndexLoss] (%s) Failed to get volume path url"
+ "[IndexLoss] (%s) Failed to get volume property flags, err:%@"
+ "[IndexLoss] (%s) Got volume property flags 0x%llx"
+ "[IndexLoss] (%s) Intentional drop (%@) with reason %s"
+ "[IndexLoss] (%s) Not reporting drop (%d, %d, %d, %d, %s) for reason %d"
+ "[IndexLoss] (%s) Sending analytics (%d, %d, %d, %d, %s)"
+ "[IndexLoss] Could not open heartbeat file"
+ "[IndexLoss] Empty dictionary"
+ "[IndexLoss] Event does not have a timestamp"
+ "[IndexLoss] FS (%llu, %llu, 0x%x) mounted at path %s"
+ "[IndexLoss] Failed to create directory: %@"
+ "[IndexLoss] Failed to create file at %@"
+ "[IndexLoss] Over 100 drops with same timestamp %@"
+ "[IndexLoss] Wrote to %@"
+ "[IndexLoss] rebuild reason %@"
+ "[IndexLoss] writing out to file"
+ "[VectorIndexDrop] (%s) count %ld, rdonly %d, prefix %@, property %@, reason %ld"
+ "_age"
+ "_obj_count"
+ "_wipes"
+ "_wipes_aggregate"
+ "age"
+ "build"
+ "buildbeforeupgrade"
+ "com.apple.searchd.indexes.heartbeat"
+ "com.apple.searchd.indexrebuildcount"
+ "com.apple.searchd.vectorindexdrop"
+ "disable_index_drop_reporting"
+ "diskimage"
+ "droppedindexage"
+ "droppedindexsize"
+ "dropreason"
+ "droptime"
+ "dumpIndexAges"
+ "dumpIndexAgesAtPath:"
+ "dumpIndexAnalytics"
+ "dumpIndexAnalyticsAtPath:"
+ "embeddingdonationon"
+ "externalvolume"
+ "fileprotection"
+ "filesystemflags"
+ "filesystemfree"
+ "filesystemsize"
+ "filesystemtype"
+ "getAggregateIndexWipeCount"
+ "getIndexDirectorySize:"
+ "heartbeat"
+ "heartbeat_age"
+ "i28@0:8@16B24"
+ "incrementIndexWipeCount"
+ "index dropped %@"
+ "indexAnalyticsDump"
+ "indexLossAnalyticsDictWithPreviousIndexCreationDate:size:openingInReadOnly:fullyCreated:markedPurgeable:vectorIndexDrop:forAnalytics:"
+ "indexloss"
+ "indexrebuildcount"
+ "initWithTimeIntervalSince1970:"
+ "invalid event name"
+ "lastAnalytics"
+ "lastLoadedBundleVersion"
+ "lastOpen"
+ "lastSent"
+ "numberWithLong:"
+ "obj_count"
+ "otaversion"
+ "parentDirectory_age"
+ "parentDirectory_agw"
+ "pc%@_%@"
+ "prefix"
+ "previousbuild"
+ "previousspotlightversion"
+ "processIdentifier"
+ "processname"
+ "propertyname"
+ "readonly"
+ "readonlyfilesystem"
+ "readonlyopen"
+ "rebuildreason"
+ "rootsinstalled"
+ "sendAnalytics:"
+ "shouldNotLogIndexDrop:ignoreParentDirectoryAge:"
+ "spotlightversion"
+ "supportspsid"
+ "textsemanticsearchon"
+ "timesinceboot"
+ "timesinceupdate"
+ "v2"
+ "v20@?0I8^v12"
+ "vectorIndexDropsPath"
+ "vector_"
+ "vectorcount"
+ "vectorindexon"
+ "wherecorrupted"
+ "wipes"
+ "wipes_aggregate"
+ "writeIndexCreationDate:"
+ "writeIndexDropAnalyticsDate:"
+ "writeIndexLossEventToFile:vector:"
+ "writeIndexSuccessfulOpenDate:"
+ "writeSDBObjectCount:"
+ "\xa11\xb1"
- "=== Spotlight Diagnostic (%d) %@\n%@\n\n"
- "@\"SIAnalytics\""
- "Build version nil"
- "Build version nil (seed)"
- "Error while getting index directory size for purging"
- "Performing scheduled repeating task %@"
- "Reference to indexer is nil, quitting %@"
- "Registering BGST repeating task %@"
- "Spotlight roots from commit %@ are installed"
- "Spotlight-%@"
- "_analytics"
- "analytics"
- "getCurrentSpotlightVersionWithRoots:"
- "getPreviousBuild"
- "initWithDeletes:"
- "initWithParentDirectoryPath:corespotlight:heartbeatIndex:resourcesCallback:"
- "otaBundleVersion"
- "recordRequestsForIndex:adds:updates:deletes:"
- "reportHeartbeats"
- "runCommand:"
- "sendHeartbeatEvent"
- "sendIndexDropEventWithCorruptIndex:path:readOnly:reason:"
- "setPurgeability:forIndex:"
- "trialSpotlightRolloutID"
- "trialSpotlightTreatmentID"
- "updateCount"
- "v32@?0^@8^@16^@24"
- "\xb11\xb1"

```
