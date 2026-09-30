## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2400.8.1.0.0
-  __TEXT.__text: 0xb0148
+2400.11.100.0.0
+  __TEXT.__text: 0xb022c
   __TEXT.__auth_stubs: 0x1f00
   __TEXT.__objc_methlist: 0x4454
   __TEXT.__const: 0x398
-  __TEXT.__cstring: 0x85a3
+  __TEXT.__cstring: 0x85ac
   __TEXT.__oslogstring: 0xab32
-  __TEXT.__gcc_except_tab: 0x42e0
+  __TEXT.__gcc_except_tab: 0x42d4
   __TEXT.__dlopen_cstrs: 0x4a
-  __TEXT.__unwind_info: 0x22b0
+  __TEXT.__unwind_info: 0x22b8
   __TEXT.__objc_classname: 0x4dd
-  __TEXT.__objc_methname: 0xeca8
-  __TEXT.__objc_methtype: 0x25e3
-  __TEXT.__objc_stubs: 0xba80
-  __DATA_CONST.__got: 0xac8
-  __DATA_CONST.__const: 0x3cf8
+  __TEXT.__objc_methname: 0xecc1
+  __TEXT.__objc_methtype: 0x25e7
+  __TEXT.__objc_stubs: 0xbaa0
+  __DATA_CONST.__got: 0xae0
+  __DATA_CONST.__const: 0x3d48
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35e8
+  __DATA_CONST.__objc_selrefs: 0x35f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x350

   __AUTH_CONST.__objc_arrayobj: 0x3d8
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0xf0
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x470
   __DATA.__data: 0x868
-  __DATA.__bss: 0x114
-  __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0xd20
+  __DATA.__bss: 0x104
+  __DATA.__common: 0x4
+  __DATA_DIRTY.__objc_data: 0xd70
   __DATA_DIRTY.__data: 0x2e8
-  __DATA_DIRTY.__bss: 0x5e8
-  __DATA_DIRTY.__common: 0xc
+  __DATA_DIRTY.__bss: 0x5f8
+  __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 2CFED1C9-DEFF-3636-A4C0-15113561819F
-  Functions: 2861
-  Symbols:   9734
-  CStrings:  5915
+  UUID: A4825DF5-DB6F-38C4-A0F1-52C7227CDF90
+  Functions: 2862
+  Symbols:   9742
+  CStrings:  5917
 
Symbols:
+ -[SPConcreteCoreSpotlightIndexer processImportForBundleID:withURLs:contentTypes:sandboxExtensions:andIdentifiers:options:inGroup:additionalAttributes:computeUpdaterAttributesAfterImport:cancelBlock:]
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
+ GCC_except_table1268
+ GCC_except_table1336
+ GCC_except_table1339
+ GCC_except_table1342
+ GCC_except_table1509
+ GCC_except_table1538
+ GCC_except_table513
+ GCC_except_table518
+ GCC_except_table533
+ GCC_except_table541
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
+ GCC_except_table839
+ GCC_except_table847
+ GCC_except_table883
+ GCC_except_table922
+ GCC_except_table953
+ GCC_except_table958
+ GCC_except_table967
+ GCC_except_table974
+ GCC_except_table987
+ GCC_except_table990
+ GCC_except_table999
+ _XPC_ACTIVITY_REQUIRES_CLASS_A
+ _XPC_ACTIVITY_REQUIRES_CLASS_B
+ _XPC_ACTIVITY_REQUIRES_CLASS_C
+ ___101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke.1526
+ ___107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.3173
+ ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke.1566
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2446
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2446.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2449.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2450
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2450.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2451
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1495
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1503
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1509
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1515
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1518
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1510
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1516
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1519
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1519.cold.1
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1511
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1511.cold.1
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1517
+ ___199-[SPConcreteCoreSpotlightIndexer processImportForBundleID:withURLs:contentTypes:sandboxExtensions:andIdentifiers:options:inGroup:additionalAttributes:computeUpdaterAttributesAfterImport:cancelBlock:]_block_invoke
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2162
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2175
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2184
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2188
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2194
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2195
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2207
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2211
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2212
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2219
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2225
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2225.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2228
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2228.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2231
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2231.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2237
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2238
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2243
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2243.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2243.cold.2
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2244
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2251
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2254
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2259
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2266
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2267
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2272
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2272.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2272.cold.2
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2171
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2180
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2215
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2220
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2239
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2239.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2252
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2255
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2255.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2269
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2269.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2276
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2172
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2172.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2253
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2253.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2277
+ ___31-[SPCoreSpotlightIndexer start]_block_invoke.2338
+ ___39-[SPCoreSpotlightIndexer queryPreheat:]_block_invoke.2435
+ ___40-[SPCoreSpotlightIndexer issueHeartbeat]_block_invoke.2402
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.3184
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.3185
+ ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2109
+ ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2109.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2329
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2333.cold.2
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2334.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2335
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2335.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2336
+ ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1652
+ ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1653
+ ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke.2317
+ ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke_2.2318
+ ___63-[SPCoreSpotlightIndexer _deleteNonMailBundlesFromClassAIndex:]_block_invoke.2313
+ ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2119
+ ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2120
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1474
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1475
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1479
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2486
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2487
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2488
+ ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.2367
+ ___81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2569
+ ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.3172
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3121.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3127
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3127.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3128
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2654
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2661
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2681
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2715
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2719
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2723
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2743
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2755
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2768
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2995
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2996
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3003
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3007
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3008
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3012
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3016
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3035
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2662
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2747
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2769
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3057
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3061
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3085
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5.3086
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_6.3090
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_7.3103
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_8.3108
+ ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2515
+ ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.2516
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2360
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2360.cold.1
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2361
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2365
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2366
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96r_e18_v20?0^{__SI=}8C16lr96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96s104r_e5_v8?0ls32l8r104l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_40_e8_32r_e5_B8?0lr32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_88_e8_32s40s48r56r64r_e5_v8?0lr48l8r56l8r64l8s32l8s40l8
+ ___block_descriptor_96_e8_32s40s48r56r64r72r_e5_v8?0lr48l8r56l8r64l8r72l8s32l8s40l8
+ ___block_literal_global.1521
+ ___block_literal_global.1576
+ ___block_literal_global.1586
+ ___block_literal_global.2090
+ ___block_literal_global.2095
+ ___block_literal_global.2101
+ ___block_literal_global.2105
+ ___block_literal_global.2126
+ ___block_literal_global.2129
+ ___block_literal_global.2146
+ ___block_literal_global.2161
+ ___block_literal_global.2165
+ ___block_literal_global.2190
+ ___block_literal_global.2214
+ ___block_literal_global.2222
+ ___block_literal_global.2271
+ ___block_literal_global.2275
+ ___block_literal_global.2341
+ ___block_literal_global.2359
+ ___block_literal_global.2369
+ ___block_literal_global.2421
+ ___block_literal_global.2430
+ ___block_literal_global.2437
+ ___block_literal_global.2473
+ ___block_literal_global.2511
+ ___block_literal_global.2518
+ ___block_literal_global.2602
+ ___block_literal_global.2887
+ ___block_literal_global.2892
+ ___block_literal_global.2897
+ ___block_literal_global.2902
+ ___block_literal_global.2907
+ ___block_literal_global.2912
+ ___block_literal_global.2917
+ ___block_literal_global.2922
+ ___block_literal_global.2927
+ ___block_literal_global.3131
+ ___block_literal_global.3183
+ ___block_literal_global.3196
+ ___block_literal_global.3772
+ ___block_literal_global.3842
+ ___block_literal_global.3891
+ ___block_literal_global.3901
+ ___block_literal_global.3938
+ ___block_literal_global.3945
+ ___processItemsForImportInner_block_invoke.3859
+ _objc_msgSend$dateSortedL1
+ _objc_msgSend$processImportForBundleID:withURLs:contentTypes:sandboxExtensions:andIdentifiers:options:inGroup:additionalAttributes:computeUpdaterAttributesAfterImport:cancelBlock:
- -[SPConcreteCoreSpotlightIndexer processImportForBundleID:withURLs:contentTypes:sandboxExtensions:andIdentifiers:options:inGroup:additionalAttributes:computeUpdaterAttributesAfterImport:]
- GCC_except_table1007
- GCC_except_table1012
- GCC_except_table1017
- GCC_except_table1022
- GCC_except_table1028
- GCC_except_table1044
- GCC_except_table1098
- GCC_except_table1100
- GCC_except_table1105
- GCC_except_table1146
- GCC_except_table1152
- GCC_except_table1266
- GCC_except_table1335
- GCC_except_table1338
- GCC_except_table1340
- GCC_except_table1508
- GCC_except_table1537
- GCC_except_table512
- GCC_except_table517
- GCC_except_table531
- GCC_except_table540
- GCC_except_table583
- GCC_except_table610
- GCC_except_table671
- GCC_except_table695
- GCC_except_table721
- GCC_except_table725
- GCC_except_table729
- GCC_except_table757
- GCC_except_table783
- GCC_except_table800
- GCC_except_table813
- GCC_except_table837
- GCC_except_table846
- GCC_except_table882
- GCC_except_table921
- GCC_except_table952
- GCC_except_table956
- GCC_except_table963
- GCC_except_table973
- GCC_except_table986
- GCC_except_table989
- GCC_except_table998
- ___101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke.1524
- ___107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.3171
- ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke.1564
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2442
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2444.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2447
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2447.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2448
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2448.cold.1
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1493
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1501
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1507
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1513
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1516
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1508
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1514
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1517
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1517.cold.1
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1509
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1509.cold.1
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1515
- ___187-[SPConcreteCoreSpotlightIndexer processImportForBundleID:withURLs:contentTypes:sandboxExtensions:andIdentifiers:options:inGroup:additionalAttributes:computeUpdaterAttributesAfterImport:]_block_invoke
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2160
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2173
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2182
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2186
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2191
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2192
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2205
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2209
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2210
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2217
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2221
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2223.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2224
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2226.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2227
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2229.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2233
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2236
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2241
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2241.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2241.cold.2
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2242
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2249
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2252
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2257
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2264
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2265
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2270
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2270.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2270.cold.2
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2169
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2178
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2213
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2218
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2237
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2237.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2250
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2253
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2253.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2267
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2267.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2274
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2170
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2170.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2251
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2251.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2275
- ___31-[SPCoreSpotlightIndexer start]_block_invoke.2336
- ___39-[SPCoreSpotlightIndexer queryPreheat:]_block_invoke.2433
- ___40-[SPCoreSpotlightIndexer issueHeartbeat]_block_invoke.2400
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.3182
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.3183
- ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2107
- ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2107.cold.1
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2327
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2331
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2331.cold.1
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2331.cold.2
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2332
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2332.cold.1
- ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1650
- ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1651
- ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke.2315
- ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke_2.2316
- ___63-[SPCoreSpotlightIndexer _deleteNonMailBundlesFromClassAIndex:]_block_invoke.2311
- ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2117
- ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2118
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1473
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1477
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2484
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2485
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2486
- ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.2365
- ___81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2567
- ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.3170
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3119
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3119.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3123.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3124
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2652
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2659
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2679
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2713
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2717
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2721
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2741
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2753
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2766
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2993
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2994
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3001
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3005
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3006
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3010
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3014
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3033
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2660
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2745
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2767
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3055
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3059
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3083
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5.3084
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_6.3088
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_7.3101
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_8.3106
- ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2513
- ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.2514
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2358
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2358.cold.1
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2359
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2363
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2364
- ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
- ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0lr48l8s32l8r56l8s40l8
- ___block_descriptor_96_e8_32s40s48s56r64r72r_e5_v8?0lr56l8r64l8s32l8r72l8s40l8s48l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e18_v20?0^{__SI=}8C16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_literal_global.1519
- ___block_literal_global.1574
- ___block_literal_global.1584
- ___block_literal_global.2088
- ___block_literal_global.2093
- ___block_literal_global.2099
- ___block_literal_global.2103
- ___block_literal_global.2120
- ___block_literal_global.2127
- ___block_literal_global.2144
- ___block_literal_global.2157
- ___block_literal_global.2163
- ___block_literal_global.2188
- ___block_literal_global.2212
- ___block_literal_global.2220
- ___block_literal_global.2269
- ___block_literal_global.2273
- ___block_literal_global.2339
- ___block_literal_global.2353
- ___block_literal_global.2367
- ___block_literal_global.2419
- ___block_literal_global.2424
- ___block_literal_global.2435
- ___block_literal_global.2471
- ___block_literal_global.2509
- ___block_literal_global.2516
- ___block_literal_global.2600
- ___block_literal_global.2885
- ___block_literal_global.2890
- ___block_literal_global.2895
- ___block_literal_global.2900
- ___block_literal_global.2905
- ___block_literal_global.2910
- ___block_literal_global.2915
- ___block_literal_global.2920
- ___block_literal_global.2925
- ___block_literal_global.3129
- ___block_literal_global.3181
- ___block_literal_global.3194
- ___block_literal_global.3770
- ___block_literal_global.3840
- ___block_literal_global.3889
- ___block_literal_global.3897
- ___block_literal_global.3936
- ___block_literal_global.3943
- ___processItemsForImportInner_block_invoke.3857
- _objc_msgSend$processImportForBundleID:withURLs:contentTypes:sandboxExtensions:andIdentifiers:options:inGroup:additionalAttributes:computeUpdaterAttributesAfterImport:
CStrings:
+ "2400.11.100"
+ "B8@?0"
+ "dateSortedL1"
+ "processImportForBundleID:withURLs:contentTypes:sandboxExtensions:andIdentifiers:options:inGroup:additionalAttributes:computeUpdaterAttributesAfterImport:cancelBlock:"
+ "v92@0:8@16@24@32@40@48q56@64@72B80@?84"
- "2400.8.1"
- "processImportForBundleID:withURLs:contentTypes:sandboxExtensions:andIdentifiers:options:inGroup:additionalAttributes:computeUpdaterAttributesAfterImport:"
- "v84@0:8@16@24@32@40@48q56@64@72B80"

```
