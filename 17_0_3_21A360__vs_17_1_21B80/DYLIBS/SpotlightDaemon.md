## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2268.1.8.0.0
-  __TEXT.__text: 0x6e400
-  __TEXT.__auth_stubs: 0x1740
-  __TEXT.__objc_methlist: 0x2ea8
+2274.0.3.0.0
+  __TEXT.__text: 0x70f88
+  __TEXT.__auth_stubs: 0x1770
+  __TEXT.__objc_methlist: 0x2ed0
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x4f22
-  __TEXT.__gcc_except_tab: 0x25c0
-  __TEXT.__oslogstring: 0x588e
-  __TEXT.__unwind_info: 0x1968
+  __TEXT.__cstring: 0x506c
+  __TEXT.__gcc_except_tab: 0x26ac
+  __TEXT.__oslogstring: 0x602f
+  __TEXT.__unwind_info: 0x19c4
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x409
-  __TEXT.__objc_methname: 0xa286
-  __TEXT.__objc_methtype: 0x1b39
-  __TEXT.__objc_stubs: 0x81c0
-  __DATA_CONST.__got: 0x400
-  __DATA_CONST.__const: 0x2c20
+  __TEXT.__objc_methname: 0xa334
+  __TEXT.__objc_methtype: 0x1b5a
+  __TEXT.__objc_stubs: 0x8300
+  __DATA_CONST.__got: 0x428
+  __DATA_CONST.__const: 0x2cc0
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4270
-  __DATA_CONST.__objc_selrefs: 0x2578
-  __DATA_CONST.__objc_arraydata: 0x150
-  __AUTH_CONST.__const: 0xa40
-  __AUTH_CONST.__cfstring: 0x3a60
+  __DATA_CONST.__objc_const: 0x4290
+  __DATA_CONST.__objc_selrefs: 0x25b0
+  __DATA_CONST.__objc_arraydata: 0x168
+  __AUTH_CONST.__const: 0xaa0
+  __AUTH_CONST.__cfstring: 0x3c40
   __AUTH_CONST.__objc_const: 0xf78
   __AUTH_CONST.__objc_intobj: 0x168
-  __AUTH_CONST.__objc_arrayobj: 0x1f8
+  __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0xbb8
+  __AUTH_CONST.__auth_got: 0xbd0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x370
   __DATA.__objc_superrefs: 0xd0
-  __DATA.__objc_ivar: 0x368
-  __DATA.__data: 0x398
+  __DATA.__objc_ivar: 0x36c
+  __DATA.__data: 0x3d8
   __DATA.__thread_ptrs: 0x8
-  __DATA.__bss: 0x141
+  __DATA.__bss: 0x1a9
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xaa0
   __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0x370
+  __DATA_DIRTY.__bss: 0x320
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2006
-  Symbols:   6865
-  CStrings:  3227
+  Functions: 2036
+  Symbols:   6961
+  CStrings:  3291
 
Symbols:
+ -[SPConcreteCoreSpotlightIndexer deleteHasTopHitAppShortcutsWithResultsHandler:completionHandler:]
+ -[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:].cold.1
+ -[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:].cold.2
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]
+ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:].cold.1
+ -[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:force:postFilter:].cold.1
+ -[SPConcreteCoreSpotlightIndexer setKnownClients:]
+ -[SPCoreSpotlightIndexer _openIndex:forInit:readOnly:]
+ -[SPCoreSpotlightIndexer openIndex:forInit:readOnly:]
+ -[SPCoreSpotlightIndexer openIndex:readOnly:]
+ -[SPCoreSpotlightIndexer recycleIndex:]
+ GCC_except_table148
+ GCC_except_table150
+ GCC_except_table161
+ GCC_except_table186
+ GCC_except_table193
+ GCC_except_table203
+ GCC_except_table228
+ GCC_except_table248
+ GCC_except_table267
+ GCC_except_table268
+ GCC_except_table277
+ GCC_except_table278
+ GCC_except_table302
+ GCC_except_table323
+ GCC_except_table324
+ GCC_except_table325
+ GCC_except_table353
+ GCC_except_table361
+ GCC_except_table375
+ GCC_except_table393
+ GCC_except_table394
+ GCC_except_table436
+ GCC_except_table437
+ GCC_except_table438
+ GCC_except_table491
+ GCC_except_table525
+ GCC_except_table534
+ GCC_except_table540
+ GCC_except_table564
+ GCC_except_table565
+ GCC_except_table573
+ GCC_except_table594
+ GCC_except_table630
+ GCC_except_table657
+ GCC_except_table661
+ GCC_except_table668
+ GCC_except_table669
+ GCC_except_table670
+ GCC_except_table675
+ GCC_except_table681
+ GCC_except_table684
+ GCC_except_table701
+ GCC_except_table706
+ GCC_except_table711
+ GCC_except_table716
+ GCC_except_table722
+ GCC_except_table728
+ GCC_except_table763
+ GCC_except_table765
+ GCC_except_table770
+ GCC_except_table805
+ GCC_except_table811
+ GCC_except_table906
+ GCC_except_table907
+ OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._readOnly
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterGetLocalCenter
+ _MDItemExternalID
+ _MDItemHasTopHitAppShortcuts
+ _MDItemRelatedAppBundleIdentifier
+ _MDItemRunnableShortcutsIsAppShortcutTopHit
+ _OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._knownClients
+ ___101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke.897
+ ___105-[SPConcreteCoreSpotlightIndexer willModifySearchableItemsWithIdentifiers:forBundleID:completionHandler:]_block_invoke.799
+ ___107-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:completionHandler:]_block_invoke.819
+ ___107-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:completionHandler:]_block_invoke.819.cold.1
+ ___107-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:completionHandler:]_block_invoke_10
+ ___107-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:completionHandler:]_block_invoke_11
+ ___107-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:completionHandler:]_block_invoke_3
+ ___107-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:completionHandler:]_block_invoke_4
+ ___107-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:completionHandler:]_block_invoke_5
+ ___107-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:completionHandler:]_block_invoke_6
+ ___107-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:completionHandler:]_block_invoke_7
+ ___107-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:completionHandler:]_block_invoke_8
+ ___107-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:completionHandler:]_block_invoke_9
+ ___107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.1945
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1443
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1445
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1445.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1448
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1448.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1449
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1449.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1450
+ ___158-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:completionHandler:]_block_invoke.688
+ ___158-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:completionHandler:]_block_invoke.688.cold.1
+ ___158-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:completionHandler:]_block_invoke.715
+ ___158-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:completionHandler:]_block_invoke.727
+ ___158-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:completionHandler:]_block_invoke.756
+ ___158-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:completionHandler:]_block_invoke.761
+ ___158-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:completionHandler:]_block_invoke.765
+ ___158-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:completionHandler:]_block_invoke_2.739
+ ___158-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:completionHandler:]_block_invoke_2.757
+ ___158-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:completionHandler:]_block_invoke_2.762
+ ___158-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:completionHandler:]_block_invoke_2.762.cold.1
+ ___158-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:completionHandler:]_block_invoke_3.740
+ ___158-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:completionHandler:]_block_invoke_4.741
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.767
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.767.cold.1
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.786
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.788
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke_2.787
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.1306
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.1318
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.1322
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.1327
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.1328
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.1329
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.1341
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.1343
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.1343.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.1344
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.1346
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.1346.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.1347
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.1348
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.1313
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.1349
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.1350
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_4.1351
+ ___31-[SPCoreSpotlightIndexer start]_block_invoke.1381
+ ___31-[SPCoreSpotlightIndexer start]_block_invoke.cold.2
+ ___39-[SPCoreSpotlightIndexer recycleIndex:]_block_invoke
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.1956
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.1957
+ ___45-[SPConcreteCoreSpotlightIndexer resumeIndex]_block_invoke_2
+ ___53-[SPCoreSpotlightIndexer openIndex:forInit:readOnly:]_block_invoke
+ ___54-[SPCoreSpotlightIndexer _openIndex:forInit:readOnly:]_block_invoke
+ ___60-[SPConcreteCoreSpotlightIndexer _addNewClientWithBundleID:]_block_invoke.540
+ ___67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.857
+ ___67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.857.cold.1
+ ___67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.859
+ ___67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.861
+ ___67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.861.cold.1
+ ___67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.862
+ ___67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke_2.860
+ ___67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke_2.860.cold.1
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.483
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.500
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.501
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.503
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.503.cold.1
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.508
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.509
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.512
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.515
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.523
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.527
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.485
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.502
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.507
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_3
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_3.488
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_4
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_4.491
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_5
+ ___70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_6
+ ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.532
+ ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.533
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1577
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1587
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1601
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1632
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1636
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1640
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1669
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1846
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1847
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1854
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1858
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1859
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1863
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1867
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1886
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke_2.1588
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke_2.1660
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke_2.1682
+ ___72-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:completionHandler:]_block_invoke.1457
+ ___72-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:completionHandler:]_block_invoke.1458
+ ___72-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:completionHandler:]_block_invoke_2.1459
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.575
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_2.576
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_3.586
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_3.586.cold.1
+ ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.1409
+ ___81-[SPConcreteCoreSpotlightIndexer processDecryptsForBundleID:persona:infos:group:]_block_invoke.677
+ ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.1944
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1895
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1895.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1897
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1899
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1899.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1900
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1901
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1901.cold.1
+ ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.547
+ ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.548
+ ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.1479
+ ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.1480
+ ___96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.1402
+ ___96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.1402.cold.1
+ ___96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.1403
+ ___96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.1407
+ ___96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.1408
+ ___97-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:shouldGC:completionHandler:]_block_invoke.872
+ ___97-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:shouldGC:completionHandler:]_block_invoke.876
+ ___97-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:shouldGC:completionHandler:]_block_invoke.882
+ ___97-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:shouldGC:completionHandler:]_block_invoke.890
+ ___97-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:shouldGC:completionHandler:]_block_invoke_2.883
+ ___97-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:shouldGC:completionHandler:]_block_invoke_2.891
+ ___97-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:shouldGC:completionHandler:]_block_invoke_2.891.cold.1
+ ___97-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:shouldGC:completionHandler:]_block_invoke_3.884
+ ___97-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:shouldGC:completionHandler:]_block_invoke_4.888
+ ___97-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:shouldGC:completionHandler:]_block_invoke_5.889
+ ___97-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:shouldGC:completionHandler:]_block_invoke_6
+ ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.825
+ ___block_descriptor_40_e8_32s_e67_v44?0i8Q12^{__MDStoreOIDArray=}20^{__MDPlistBytes=}28"NSString"36ls32l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e22_v24?0"NSString"8^B16ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e18_v20?0^{__SI=}8C16ls32l8
+ ___block_descriptor_51_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e18_v20?0^{__SI=}8C16lr48l8s40l8s32l8
+ ___block_descriptor_67_e8_32s40s48r56r_e57_v32?0"NSString"8"SPConcreteCoreSpotlightIndexer"16^B24ls32l8r48l8r56l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs56w_e17_v16?0"NSError"8ls32l8w56l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56bs64w_e5_v8?0ls32l8s40l8s48l8w64l8s56l8
+ ___block_literal_global.1268
+ ___block_literal_global.1273
+ ___block_literal_global.1278
+ ___block_literal_global.1286
+ ___block_literal_global.1298
+ ___block_literal_global.1324
+ ___block_literal_global.1397
+ ___block_literal_global.1399
+ ___block_literal_global.1401
+ ___block_literal_global.1411
+ ___block_literal_global.1414
+ ___block_literal_global.1422
+ ___block_literal_global.1424
+ ___block_literal_global.1426
+ ___block_literal_global.1433
+ ___block_literal_global.1477
+ ___block_literal_global.1482
+ ___block_literal_global.1530
+ ___block_literal_global.1794
+ ___block_literal_global.1799
+ ___block_literal_global.1804
+ ___block_literal_global.1809
+ ___block_literal_global.1814
+ ___block_literal_global.1903
+ ___block_literal_global.1955
+ ___block_literal_global.1968
+ ___block_literal_global.2379
+ ___block_literal_global.2381
+ ___block_literal_global.2445
+ ___block_literal_global.2452
+ ___block_literal_global.517
+ ___block_literal_global.529
+ ___block_literal_global.675
+ ___block_literal_global.717
+ ___block_literal_global.729
+ ___block_literal_global.764
+ ___block_literal_global.821
+ ___block_literal_global.893
+ ___block_literal_global.937
+ ___block_literal_global.947
+ ___initializeDiskSpaceNotificationListener_block_invoke
+ ___processItemsForImport_block_invoke.2399
+ __dispatch_source_type_vfs
+ __unnamed_array_storage.1294
+ __unnamed_array_storage.1364
+ __unnamed_array_storage.1379
+ __unnamed_array_storage.1951
+ __unnamed_array_storage.2386
+ __unnamed_array_storage.2390
+ __unnamed_array_storage.2442
+ __unnamed_array_storage.573
+ __unnamed_array_storage.584
+ __unnamed_array_storage.632
+ __unnamed_array_storage.751
+ __unnamed_array_storage.804
+ __unnamed_array_storage.855
+ __unnamed_array_storage.934
+ _gVFSEventQueue
+ _gVFSEventSource
+ _handleLowDiskSpace
+ _initializeDiskSpaceNotificationListener.sVFSEventLock
+ _isAppleInternalInstall
+ _objc_msgSend$_openIndex:forInit:readOnly:
+ _objc_msgSend$attributesOfFileSystemForPath:error:
+ _objc_msgSend$deleteHasTopHitAppShortcutsWithResultsHandler:completionHandler:
+ _objc_msgSend$openIndex:forInit:readOnly:
+ _objc_msgSend$openIndex:readOnly:
+ _objc_msgSend$openIndex:shouldReindexAll:readOnly:
+ _objc_msgSend$recycleIndex:
+ _objc_msgSend$setByAddingObject:
+ _objc_msgSend$setKnownClients:
+ _objc_msgSend$setLowPriority:
+ _objc_msgSend$unlock
+ _objc_msgSend$unsignedLongValue
+ _openIndex:shouldReindexAll:readOnly:.lastReport
+ _openIndex:shouldReindexAll:readOnly:.lastTime
+ _openIndex:shouldReindexAll:readOnly:.onceToken
+ _openIndex:shouldReindexAll:readOnly:.totalCost
+ _sVeryLowDiskSpace
- -[SPConcreteCoreSpotlightIndexer _setClientState:clientStateName:forBundleID:completionHandler:]
- -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:].cold.1
- -[SPConcreteCoreSpotlightIndexer updateItems:forBundleId:]
- -[SPCoreSpotlightIndexer _openIndex:forInit:]
- -[SPCoreSpotlightIndexer openIndex:forInit:]
- GCC_except_table151
- GCC_except_table156
- GCC_except_table164
- GCC_except_table188
- GCC_except_table195
- GCC_except_table205
- GCC_except_table230
- GCC_except_table250
- GCC_except_table272
- GCC_except_table273
- GCC_except_table282
- GCC_except_table283
- GCC_except_table303
- GCC_except_table343
- GCC_except_table351
- GCC_except_table365
- GCC_except_table378
- GCC_except_table379
- GCC_except_table421
- GCC_except_table422
- GCC_except_table423
- GCC_except_table475
- GCC_except_table509
- GCC_except_table518
- GCC_except_table524
- GCC_except_table548
- GCC_except_table549
- GCC_except_table557
- GCC_except_table578
- GCC_except_table612
- GCC_except_table639
- GCC_except_table643
- GCC_except_table644
- GCC_except_table650
- GCC_except_table651
- GCC_except_table652
- GCC_except_table656
- GCC_except_table665
- GCC_except_table673
- GCC_except_table682
- GCC_except_table687
- GCC_except_table697
- GCC_except_table703
- GCC_except_table709
- GCC_except_table741
- GCC_except_table743
- GCC_except_table748
- GCC_except_table783
- GCC_except_table789
- GCC_except_table885
- GCC_except_table886
- OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._knownClients
- _OUTLINED_FUNCTION_38
- ___101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke_3
- ___105-[SPConcreteCoreSpotlightIndexer willModifySearchableItemsWithIdentifiers:forBundleID:completionHandler:]_block_invoke.774
- ___107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.1869
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1397
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1399
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1399.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1402
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1402.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1403
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1403.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1404
- ___158-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:completionHandler:]_block_invoke.686
- ___158-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:completionHandler:]_block_invoke.686.cold.1
- ___158-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:completionHandler:]_block_invoke.713
- ___158-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:completionHandler:]_block_invoke.725
- ___158-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:completionHandler:]_block_invoke.740
- ___158-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:completionHandler:]_block_invoke_2.737
- ___158-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:completionHandler:]_block_invoke_3.738
- ___158-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:completionHandler:]_block_invoke_4.739
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.742
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.742.cold.1
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.761
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.763
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke_2.762
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.1263
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.1275
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.1279
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.1284
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.1285
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.1286
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.1298
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.1300
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.1300.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.1301
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.1303
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.1303.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.1304
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.1305
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.1270
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.1306
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.1307
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_4.1308
- ___31-[SPCoreSpotlightIndexer start]_block_invoke.1338
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.1880
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.1881
- ___44-[SPCoreSpotlightIndexer openIndex:forInit:]_block_invoke
- ___45-[SPCoreSpotlightIndexer _openIndex:forInit:]_block_invoke
- ___58-[SPConcreteCoreSpotlightIndexer updateItems:forBundleId:]_block_invoke
- ___58-[SPConcreteCoreSpotlightIndexer updateItems:forBundleId:]_block_invoke_2
- ___60-[SPConcreteCoreSpotlightIndexer _addNewClientWithBundleID:]_block_invoke.536
- ___61-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:]_block_invoke
- ___61-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:]_block_invoke.483
- ___61-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:]_block_invoke.497
- ___61-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:]_block_invoke.498
- ___61-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:]_block_invoke.500
- ___61-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:]_block_invoke.505
- ___61-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:]_block_invoke.506
- ___61-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:]_block_invoke.509
- ___61-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:]_block_invoke.512
- ___61-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:]_block_invoke.520
- ___61-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:]_block_invoke.523
- ___61-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:]_block_invoke_2
- ___61-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:]_block_invoke_2.485
- ___61-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:]_block_invoke_2.499
- ___61-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:]_block_invoke_2.504
- ___61-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:]_block_invoke_3
- ___61-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:]_block_invoke_3.488
- ___61-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:]_block_invoke_4
- ___61-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:]_block_invoke_4.491
- ___61-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:]_block_invoke_5
- ___61-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:]_block_invoke_6
- ___67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.818
- ___67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.818.cold.1
- ___67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.820
- ___67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.822
- ___67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.822.cold.1
- ___67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.823
- ___67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke_2.821
- ___67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke_2.821.cold.1
- ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.528
- ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.529
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1531
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1541
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1555
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1586
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1590
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1594
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1623
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1800
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1801
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1808
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1812
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1813
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke_2.1542
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke_2.1614
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke_2.1636
- ___72-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:completionHandler:]_block_invoke.1411
- ___72-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:completionHandler:]_block_invoke.1412
- ___72-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:completionHandler:]_block_invoke_2.1413
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.572
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_2.573
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_3.583
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_3.583.cold.1
- ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.1363
- ___81-[SPConcreteCoreSpotlightIndexer processDecryptsForBundleID:persona:infos:group:]_block_invoke.675
- ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.1868
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1819
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1819.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1821
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1823
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1823.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1824
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1825
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1825.cold.1
- ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.544
- ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.545
- ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.1433
- ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.1434
- ___96-[SPConcreteCoreSpotlightIndexer _setClientState:clientStateName:forBundleID:completionHandler:]_block_invoke
- ___96-[SPConcreteCoreSpotlightIndexer _setClientState:clientStateName:forBundleID:completionHandler:]_block_invoke.674
- ___96-[SPConcreteCoreSpotlightIndexer _setClientState:clientStateName:forBundleID:completionHandler:]_block_invoke.cold.1
- ___96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.1356
- ___96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.1356.cold.1
- ___96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.1357
- ___96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.1361
- ___96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.1362
- ___97-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:shouldGC:completionHandler:]_block_invoke.833
- ___97-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:shouldGC:completionHandler:]_block_invoke.837
- ___97-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:shouldGC:completionHandler:]_block_invoke.843
- ___97-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:shouldGC:completionHandler:]_block_invoke_2.844
- ___97-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:shouldGC:completionHandler:]_block_invoke_3.845
- ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_6
- ___block_descriptor_50_e8_32s40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_56_e8_32s40bs48r_e18_v20?0^{__SI=}8C16lr48l8s32l8s40l8
- ___block_descriptor_66_e8_32s40s48r56r_e57_v32?0"NSString"8"SPConcreteCoreSpotlightIndexer"16^B24ls32l8r48l8r56l8s40l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e18_v20?0^{__SI=}8C16ls64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
- ___block_literal_global.1219
- ___block_literal_global.1224
- ___block_literal_global.1229
- ___block_literal_global.1237
- ___block_literal_global.1255
- ___block_literal_global.1281
- ___block_literal_global.1351
- ___block_literal_global.1353
- ___block_literal_global.1355
- ___block_literal_global.1365
- ___block_literal_global.1368
- ___block_literal_global.1376
- ___block_literal_global.1378
- ___block_literal_global.1380
- ___block_literal_global.1385
- ___block_literal_global.1387
- ___block_literal_global.1436
- ___block_literal_global.1484
- ___block_literal_global.1748
- ___block_literal_global.1753
- ___block_literal_global.1758
- ___block_literal_global.1763
- ___block_literal_global.1768
- ___block_literal_global.1827
- ___block_literal_global.1879
- ___block_literal_global.1892
- ___block_literal_global.2301
- ___block_literal_global.2303
- ___block_literal_global.2359
- ___block_literal_global.2366
- ___block_literal_global.508
- ___block_literal_global.525
- ___block_literal_global.672
- ___block_literal_global.715
- ___block_literal_global.727
- ___block_literal_global.891
- ___block_literal_global.901
- ___processItemsForImport_block_invoke.2321
- __setClientStateInner
- __unnamed_array_storage.1251
- __unnamed_array_storage.1321
- __unnamed_array_storage.1336
- __unnamed_array_storage.1875
- __unnamed_array_storage.2308
- __unnamed_array_storage.2312
- __unnamed_array_storage.2356
- __unnamed_array_storage.570
- __unnamed_array_storage.581
- __unnamed_array_storage.629
- __unnamed_array_storage.888
- _objc_msgSend$_openIndex:forInit:
- _objc_msgSend$openIndex:forInit:
- _openIndex:shouldReindexAll:.lastReport
- _openIndex:shouldReindexAll:.lastTime
- _openIndex:shouldReindexAll:.onceToken
- _openIndex:shouldReindexAll:.totalCost
CStrings:
+ "%@: readOnly = %@\n"
+ "%@=1"
+ "*warn* Skipped nil indexer because index path %@ doesn't exist."
+ "/private/var/mobile/spotlightForceLowDisk"
+ "2AD\x12\x11"
+ ":EA:_kMDItemHasTopHitAppShortcuts"
+ "<= 5 seconds off! bootTime:%.0f vs. stored bootTime:%.0f"
+ "Cannot delete attributes in _deleteSearchableItmesMatchingQuery: index:%p suspended:%d readOnly:%d"
+ "Cannot delete in deleteItemsForQuery because the index is read-only"
+ "Cannot delete items because the index is read-only. dataclass:%@"
+ "Cannot fixup messages attachment because the index is read-only"
+ "Cannot index items because the index is read-only, dataclass:%@, index:%p, suspended:%s"
+ "Cannot reindex attributes because the index is read-only. dataclass:%@"
+ "Converting CoreSpotlight index to read-only"
+ "Converting index to read-only"
+ "Converting index to read-write"
+ "Default"
+ "Dropping check-in for new client, bundleID:%@, dataclass:%@, index:%p, canceled:%@, readOnly:%d"
+ "Error retrieving fsProperties: %@"
+ "Forcing low disk due to a file existing at %s"
+ "Mismatch! bootTime:%.0f with stored bootTime:%.0f"
+ "NO\n"
+ "NSFileSystemFreeSize"
+ "Received empty update vfsevent; assuming not in low disk space state"
+ "Received low disk space vfsevent; assuming very low disk ended"
+ "Received very low disk space vfsevent"
+ "Recycling index"
+ "Releasing assertion %@ (%@)"
+ "T@\"NSSet\",&,V_knownClients"
+ "The index is unavailable, dataclass:%@, index:%p, suspended:%s, readOnly:%d"
+ "The index is unavailable, dataclass:%@, index:%p, suspended:%s, readonly:%d"
+ "VFSEventQueue"
+ "Very low disk space detected; opening CoreSpotlight index as read-only"
+ "YES\n"
+ "[TopHitAppShortcuts] deleteAllSearchableItems complete"
+ "[TopHitAppShortcuts] deleteAllSearchableItems start"
+ "[TopHitAppShortcuts] deleteAllSearchableItems updating error %@"
+ "[TopHitAppShortcuts] deleteSearchableItems complete"
+ "[TopHitAppShortcuts] deleteSearchableItems start"
+ "[TopHitAppShortcuts] deleteSearchableItems updating error %@"
+ "[TopHitAppShortcuts] indexFromBundle complete"
+ "[TopHitAppShortcuts] indexFromBundle start"
+ "[TopHitAppShortcuts] indexFromBundle updating error %@"
+ "[TopHitAppShortcuts] set flag for %@"
+ "[TopHitAppShortcuts] void flag for %@"
+ "_openIndex:forInit:readOnly:"
+ "_readOnly"
+ "attributesOfFileSystemForPath:error:"
+ "com.apple.Spotlight.lowdiskspace"
+ "com_apple_shortcuts_runnable_is_app_shortcut_top_hit"
+ "deleteHasTopHitAppShortcutsWithResultsHandler:completionHandler:"
+ "deleteSearchableItemsWithFileProviderDomains failed: index:%p suspended:%d readOnly:%d"
+ "i28@0:8B16B20B24"
+ "isLowDisk"
+ "kIndexOptionReadOnly"
+ "openIndex:forInit:readOnly:"
+ "openIndex:readOnly:"
+ "openIndex:shouldReindexAll:readOnly:"
+ "processDecryptsForBundleID failed: index is readOnly"
+ "processImportForBundleID failed: index is readOnly"
+ "recycleIndex:"
+ "sVeryLowDiskSpace = "
+ "setByAddingObject:"
+ "setKnownClients:"
+ "setLowDisk"
+ "setLowPriority:"
+ "setNormalDisk"
+ "transferDeleteJournalsToDirectory failed: index:%p suspended:%d readOnly:%d"
+ "unlocking"
+ "unsignedLongValue"
+ "v32@0:8@?16@?24"
- "31D\x11\x11"
- "Dropping check-in for new client, bundleID:%@, dataclass:%@, index:%p, canceled:%@"
- "Mismatch! bootTime:%g with stored bootTime:%g"
- "Saving the client state for bundleID:%@, clientState:%@/%ld"
- "T@\"NSMutableSet\",R,N,V_knownClients"
- "_openIndex:forInit:"
- "_setClientState:clientStateName:forBundleID:completionHandler:"
- "clearSandboxExtensionOnReboot canceled"
- "openIndex:forInit:"
- "updateItems:forBundleId:"

```
