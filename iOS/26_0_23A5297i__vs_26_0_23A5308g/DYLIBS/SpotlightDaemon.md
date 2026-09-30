## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2387.1.0.0.0
-  __TEXT.__text: 0xae4f8
-  __TEXT.__auth_stubs: 0x1eb0
-  __TEXT.__objc_methlist: 0x4424
+2391.1.0.0.0
+  __TEXT.__text: 0xaf838
+  __TEXT.__auth_stubs: 0x1ed0
+  __TEXT.__objc_methlist: 0x444c
   __TEXT.__const: 0x398
-  __TEXT.__cstring: 0x81b2
-  __TEXT.__oslogstring: 0xaafa
-  __TEXT.__gcc_except_tab: 0x4274
+  __TEXT.__cstring: 0x82cb
+  __TEXT.__oslogstring: 0xab33
+  __TEXT.__gcc_except_tab: 0x42d4
   __TEXT.__dlopen_cstrs: 0x4a
-  __TEXT.__unwind_info: 0x2280
-  __TEXT.__objc_classname: 0x4d0
-  __TEXT.__objc_methname: 0xec1a
-  __TEXT.__objc_methtype: 0x25b6
-  __TEXT.__objc_stubs: 0xba00
-  __DATA_CONST.__got: 0xac0
-  __DATA_CONST.__const: 0x3c30
-  __DATA_CONST.__objc_classlist: 0x160
+  __TEXT.__unwind_info: 0x22a0
+  __TEXT.__objc_classname: 0x4dd
+  __TEXT.__objc_methname: 0xec54
+  __TEXT.__objc_methtype: 0x25d3
+  __TEXT.__objc_stubs: 0xba20
+  __DATA_CONST.__got: 0xac8
+  __DATA_CONST.__const: 0x3c80
+  __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35c8
+  __DATA_CONST.__objc_selrefs: 0x35d0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x338
-  __AUTH_CONST.__auth_got: 0xf70
-  __AUTH_CONST.__const: 0x1068
-  __AUTH_CONST.__cfstring: 0x7300
-  __AUTH_CONST.__objc_const: 0x5ae0
+  __AUTH_CONST.__auth_got: 0xf80
+  __AUTH_CONST.__const: 0x10a8
+  __AUTH_CONST.__cfstring: 0x7480
+  __AUTH_CONST.__objc_const: 0x5b98
   __AUTH_CONST.__objc_arrayobj: 0x3d8
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_ivar: 0x46c
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x470
   __DATA.__data: 0x868
-  __DATA.__bss: 0x131
-  __DATA.__common: 0x4
-  __DATA_DIRTY.__objc_data: 0xdc0
+  __DATA.__bss: 0x114
+  __DATA.__common: 0x10
+  __DATA_DIRTY.__objc_data: 0xd20
   __DATA_DIRTY.__data: 0x2e8
-  __DATA_DIRTY.__bss: 0x5b8
-  __DATA_DIRTY.__common: 0x8
+  __DATA_DIRTY.__bss: 0x5e8
+  __DATA_DIRTY.__common: 0xc
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 2CE4A278-2BC9-3FC4-B25F-39179CBAA4AC
-  Functions: 2829
-  Symbols:   9634
-  CStrings:  5843
+  UUID: 7A4F9A16-E7B1-3673-A11D-7C2D0411F2AF
+  Functions: 2852
+  Symbols:   9707
+  CStrings:  5873
 
Symbols:
+ +[SpotlightSender clearCache].cold.1
+ +[SpotlightSender clientConnection:].cold.1
+ +[SpotlightSender clientConnection:jobType:].cold.1
+ +[SpotlightSender copyDiagnosticInfo].cold.1
+ +[SpotlightSender enabledForClient:].cold.1
+ +[SpotlightSender(SpotlightScheduledSender) addOrUpdateSearchableItemsInJournalFd:atOffset:size:indexType:bundleID:protectionClass:serialNumber:journalCookie:additionalAttributes:client:config:completionHandler:]
+ -[SPConcreteCoreSpotlightIndexer checkAdmission:background:didBeginThrottle:didEndThrottle:live:slow:memoryPressure:].cold.1
+ -[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]
+ -[SPConcreteCoreSpotlightIndexer setHasPhotosOrText].cold.2
+ -[SPDASManager .cxx_destruct]
+ -[SPDASManager context]
+ -[SPDASManager init]
+ -[SPDASManager setContext:]
+ -[SpotlightReceiverConnection indexWithFd:offset:size:indexType:bundleID:protectionClass:serialNumber:journalCookie:config:additionalAttributes:completionHandler:]
+ GCC_except_table1007
+ GCC_except_table1012
+ GCC_except_table1017
+ GCC_except_table1028
+ GCC_except_table1044
+ GCC_except_table1098
+ GCC_except_table1100
+ GCC_except_table1105
+ GCC_except_table1146
+ GCC_except_table1152
+ GCC_except_table1257
+ GCC_except_table1258
+ GCC_except_table1326
+ GCC_except_table1329
+ GCC_except_table1331
+ GCC_except_table1332
+ GCC_except_table1499
+ GCC_except_table1528
+ GCC_except_table159
+ GCC_except_table169
+ GCC_except_table176
+ GCC_except_table188
+ GCC_except_table191
+ GCC_except_table192
+ GCC_except_table195
+ GCC_except_table200
+ GCC_except_table205
+ GCC_except_table207
+ GCC_except_table208
+ GCC_except_table216
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
+ GCC_except_table415
+ GCC_except_table430
+ GCC_except_table443
+ GCC_except_table446
+ GCC_except_table455
+ GCC_except_table457
+ GCC_except_table458
+ GCC_except_table489
+ GCC_except_table498
+ GCC_except_table512
+ GCC_except_table517
+ GCC_except_table531
+ GCC_except_table532
+ GCC_except_table540
+ GCC_except_table583
+ GCC_except_table584
+ GCC_except_table585
+ GCC_except_table610
+ GCC_except_table671
+ GCC_except_table695
+ GCC_except_table721
+ GCC_except_table725
+ GCC_except_table729
+ GCC_except_table757
+ GCC_except_table783
+ GCC_except_table800
+ GCC_except_table813
+ GCC_except_table82
+ GCC_except_table837
+ GCC_except_table838
+ GCC_except_table846
+ GCC_except_table882
+ GCC_except_table921
+ GCC_except_table952
+ GCC_except_table956
+ GCC_except_table963
+ GCC_except_table964
+ GCC_except_table965
+ GCC_except_table966
+ GCC_except_table973
+ GCC_except_table986
+ GCC_except_table989
+ GCC_except_table998
+ _MDInstantSenderQueue.sInstantSenderOnce
+ _MDInstantSenderQueue.sMDInstantSenderQueue
+ _OBJC_CLASS_$_SPDASManager
+ _OBJC_IVAR_$_SPDASManager._context
+ _OBJC_METACLASS_$_SPDASManager
+ _SIHasPhotos
+ _SIHasText
+ __OBJC_$_INSTANCE_METHODS_SPDASManager
+ __OBJC_$_INSTANCE_VARIABLES_SPDASManager
+ __OBJC_CLASS_RO_$_SPDASManager
+ __OBJC_METACLASS_RO_$_SPDASManager
+ ___101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke.1524
+ ___105-[SPConcreteCoreSpotlightIndexer willModifySearchableItemsWithIdentifiers:forBundleID:completionHandler:]_block_invoke.1375
+ ___107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.3165
+ ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke.1564
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2442
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2444
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2444.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2447
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2447.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2448
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2448.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2449
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1493
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1501
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1507
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1513
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1516
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1508
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1514
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1517
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1517.cold.1
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1509
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1509.cold.1
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1515
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1399
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1407
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1407.cold.1
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_2.1403
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_3.1404
+ ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_4.1405
+ ___163-[SpotlightReceiverConnection indexWithFd:offset:size:indexType:bundleID:protectionClass:serialNumber:journalCookie:config:additionalAttributes:completionHandler:]_block_invoke
+ ___163-[SpotlightReceiverConnection indexWithFd:offset:size:indexType:bundleID:protectionClass:serialNumber:journalCookie:config:additionalAttributes:completionHandler:]_block_invoke.328
+ ___163-[SpotlightReceiverConnection indexWithFd:offset:size:indexType:bundleID:protectionClass:serialNumber:journalCookie:config:additionalAttributes:completionHandler:]_block_invoke.cold.1
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1315
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1315.cold.1
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1315.cold.2
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1334
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1336
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1336.cold.1
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1336.cold.2
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1339
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1339.cold.1
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1339.cold.2
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1342
+ ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke_2.1335
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1230
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1230.cold.1
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1230.cold.2
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1230.cold.3
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1230.cold.4
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1257
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1269
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1298
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1307
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1310
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1281
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1299
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1304.cold.1
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1311
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_3.1282
+ ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_4.1283
+ ___20-[SPDASManager init]_block_invoke
+ ___223-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.342
+ ___223-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.343
+ ___223-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.350
+ ___223-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.351
+ ___29+[SpotlightSender clearCache]_block_invoke
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2182
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2186
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2191
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2193
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2205
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2209
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2217
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2221
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2223.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2224
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2226
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2226.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2227
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2229.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2235
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2241.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2241.cold.2
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2242
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2252
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2257
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2264
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2265
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2270
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2270.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke.2270.cold.2
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2169
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2178
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2213
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2218
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2250
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2253
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2253.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2267
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2267.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2274
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2170
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2170.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2251
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2251.cold.1
+ ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2275
+ ___31-[SPCoreSpotlightIndexer start]_block_invoke.2336
+ ___36+[SpotlightSender clientConnection:]_block_invoke
+ ___36+[SpotlightSender enabledForClient:]_block_invoke
+ ___37+[SpotlightSender copyDiagnosticInfo]_block_invoke
+ ___37+[SpotlightSender setupInstantSender]_block_invoke.cold.1
+ ___37+[SpotlightSender setupInstantSender]_block_invoke_2
+ ___39-[SPCoreSpotlightIndexer queryPreheat:]_block_invoke.2433
+ ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.619
+ ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.619.cold.1
+ ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.620
+ ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.627
+ ___40-[SPCoreSpotlightIndexer issueHeartbeat]_block_invoke.2400
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.3176
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.3177
+ ___44+[SpotlightSender clientConnection:jobType:]_block_invoke
+ ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2107
+ ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2107.cold.1
+ ___50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke.1363
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2327
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2331
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2331.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2331.cold.2
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2332
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2332.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2333
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2333.cold.1
+ ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2334
+ ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1650
+ ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1651
+ ___59-[SPConcreteCoreSpotlightIndexer _performXPCActivity:name:]_block_invoke.634
+ ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke.2315
+ ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke_2.2316
+ ___60-[SPConcreteCoreSpotlightIndexer _addNewClientWithBundleID:]_block_invoke.1072
+ ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.309
+ ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.310
+ ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.316
+ ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.316.cold.1
+ ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke.1206
+ ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_2.1209
+ ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_3.1212
+ ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.679
+ ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.679.cold.1
+ ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.680
+ ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.680.cold.1
+ ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.681
+ ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.681.cold.1
+ ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.682
+ ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.686
+ ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.652
+ ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.652.cold.1
+ ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.656
+ ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.656.cold.1
+ ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.658
+ ___63-[SPCoreSpotlightIndexer _deleteNonMailBundlesFromClassAIndex:]_block_invoke.2311
+ ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke
+ ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.288
+ ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.289
+ ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.293
+ ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.294
+ ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.302
+ ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.302.cold.1
+ ___64-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn:key:]_block_invoke.304
+ ___65-[SPConcreteCoreSpotlightIndexer openIndexForUpgradeSynchronous:]_block_invoke.964
+ ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2117
+ ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2118
+ ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1066
+ ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1067
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1453
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1453.cold.1
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1457
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1457.cold.1
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1458
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1472
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1473
+ ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1477
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1345
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1349
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1355
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1355.cold.1
+ ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1350
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1029
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1031
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1031.cold.1
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1036
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1037
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1040
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1043
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1051
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1055
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.982
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.987
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1028
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1030
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1035
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.983
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.989
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.992
+ ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_4.995
+ ___78-[SPConcreteCoreSpotlightIndexer scheduleMaintenance:description:forDarkWake:]_block_invoke.644
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.1105
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_2.1106
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_3.1113
+ ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_3.1113.cold.1
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2484
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2485
+ ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2486
+ ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.2365
+ ___81-[SPConcreteCoreSpotlightIndexer processDecryptsForBundleID:persona:infos:group:]_block_invoke.1215
+ ___81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2567
+ ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.278
+ ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.278.cold.1
+ ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.278.cold.2
+ ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.3164
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3113
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3113.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3115
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3117
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3117.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3118
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3119
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3119.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3120
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2652
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2659
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2679
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2713
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2717
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2721
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2741
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2753
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2766
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2993
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2994
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3001
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3005
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3006
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3010
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3014
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.3033
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2660
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2745
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2767
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3055
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_21
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_22
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_23
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3059
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3083
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5.3084
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_6.3088
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_7.3101
+ ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_8.3106
+ ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1076
+ ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1077
+ ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2513
+ ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.2514
+ ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.698
+ ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.699
+ ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.700
+ ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.701
+ ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1414
+ ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1424
+ ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_2.1425
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2358
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2358.cold.1
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2359
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2363
+ ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2364
+ ___MDInstantSenderQueue_block_invoke
+ ___block_descriptor_124_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_41_e8_32s_e8_v16?0Q8ls32l8
+ ___block_descriptor_48_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_e8_32s40r_e69_v48?0"SPQueryJob"8q16Q24^{__MDStoreOIDArray=}32^{__MDPlistBytes=}40ls32l8r40l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8r56l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e8_v12?0B8ls32l8s40l8s48l8r72l8s56l8s64l8
+ ___block_literal_global.1039
+ ___block_literal_global.1042
+ ___block_literal_global.1045
+ ___block_literal_global.1057
+ ___block_literal_global.1208
+ ___block_literal_global.1211
+ ___block_literal_global.1214
+ ___block_literal_global.1259
+ ___block_literal_global.1271
+ ___block_literal_global.1313
+ ___block_literal_global.1338
+ ___block_literal_global.1341
+ ___block_literal_global.1409
+ ___block_literal_global.1519
+ ___block_literal_global.1574
+ ___block_literal_global.1584
+ ___block_literal_global.2088
+ ___block_literal_global.2093
+ ___block_literal_global.2099
+ ___block_literal_global.2103
+ ___block_literal_global.2120
+ ___block_literal_global.2122
+ ___block_literal_global.2124
+ ___block_literal_global.2127
+ ___block_literal_global.2157
+ ___block_literal_global.2159
+ ___block_literal_global.2163
+ ___block_literal_global.2188
+ ___block_literal_global.2212
+ ___block_literal_global.2220
+ ___block_literal_global.2269
+ ___block_literal_global.2273
+ ___block_literal_global.2353
+ ___block_literal_global.2355
+ ___block_literal_global.2357
+ ___block_literal_global.2367
+ ___block_literal_global.2424
+ ___block_literal_global.2426
+ ___block_literal_global.2428
+ ___block_literal_global.2435
+ ___block_literal_global.2471
+ ___block_literal_global.2509
+ ___block_literal_global.2516
+ ___block_literal_global.259
+ ___block_literal_global.2600
+ ___block_literal_global.263
+ ___block_literal_global.280
+ ___block_literal_global.2885
+ ___block_literal_global.2890
+ ___block_literal_global.2895
+ ___block_literal_global.2900
+ ___block_literal_global.2905
+ ___block_literal_global.2910
+ ___block_literal_global.2915
+ ___block_literal_global.2920
+ ___block_literal_global.2925
+ ___block_literal_global.308
+ ___block_literal_global.312
+ ___block_literal_global.3123
+ ___block_literal_global.3175
+ ___block_literal_global.3188
+ ___block_literal_global.3721
+ ___block_literal_global.3840
+ ___block_literal_global.3848
+ ___block_literal_global.3850
+ ___block_literal_global.3887
+ ___block_literal_global.3894
+ ___block_literal_global.481
+ ___block_literal_global.524
+ ___block_literal_global.619
+ ___block_literal_global.622
+ ___block_literal_global.650
+ ___block_literal_global.675
+ ___block_literal_global.936
+ ___block_literal_global.955
+ ___block_literal_global.958
+ ___block_literal_global.960
+ ___block_literal_global.978
+ ___block_literal_global.985
+ ___block_literal_global.991
+ ___block_literal_global.994
+ ___block_literal_global.997
+ ___processItemsForImportInner_block_invoke.3808
+ ___processItemsForImport_block_invoke.cold.2
+ ___startAgents_block_invoke
+ _gDASManager
+ _objc_msgSend$indexWithFd:offset:size:indexType:bundleID:protectionClass:serialNumber:journalCookie:config:additionalAttributes:completionHandler:
+ _objc_msgSend$issuePriorityIndexFixupOn:key:
- +[SpotlightSender(SpotlightScheduledSender) addOrUpdateSearchableItemsInJournalFd:atOffset:size:indexType:protectionClass:serialNumber:journalCookie:additionalAttributes:client:config:completionHandler:]
- -[SpotlightReceiverConnection indexWithFd:offset:size:indexType:protectionClass:serialNumber:journalCookie:config:additionalAttributes:completionHandler:]
- GCC_except_table1001
- GCC_except_table1006
- GCC_except_table1011
- GCC_except_table1016
- GCC_except_table1038
- GCC_except_table1089
- GCC_except_table1091
- GCC_except_table1096
- GCC_except_table1137
- GCC_except_table1143
- GCC_except_table1248
- GCC_except_table1249
- GCC_except_table1317
- GCC_except_table1320
- GCC_except_table1322
- GCC_except_table1323
- GCC_except_table1488
- GCC_except_table1517
- GCC_except_table163
- GCC_except_table170
- GCC_except_table179
- GCC_except_table180
- GCC_except_table182
- GCC_except_table189
- GCC_except_table193
- GCC_except_table194
- GCC_except_table201
- GCC_except_table202
- GCC_except_table210
- GCC_except_table228
- GCC_except_table230
- GCC_except_table232
- GCC_except_table243
- GCC_except_table251
- GCC_except_table281
- GCC_except_table288
- GCC_except_table298
- GCC_except_table323
- GCC_except_table343
- GCC_except_table370
- GCC_except_table371
- GCC_except_table380
- GCC_except_table381
- GCC_except_table409
- GCC_except_table424
- GCC_except_table437
- GCC_except_table440
- GCC_except_table449
- GCC_except_table451
- GCC_except_table452
- GCC_except_table483
- GCC_except_table492
- GCC_except_table506
- GCC_except_table511
- GCC_except_table525
- GCC_except_table526
- GCC_except_table534
- GCC_except_table55
- GCC_except_table577
- GCC_except_table578
- GCC_except_table579
- GCC_except_table604
- GCC_except_table665
- GCC_except_table689
- GCC_except_table715
- GCC_except_table719
- GCC_except_table723
- GCC_except_table751
- GCC_except_table777
- GCC_except_table794
- GCC_except_table807
- GCC_except_table831
- GCC_except_table832
- GCC_except_table840
- GCC_except_table876
- GCC_except_table915
- GCC_except_table946
- GCC_except_table950
- GCC_except_table951
- GCC_except_table958
- GCC_except_table959
- GCC_except_table960
- GCC_except_table967
- GCC_except_table980
- GCC_except_table983
- GCC_except_table992
- ___101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke.1517
- ___105-[SPConcreteCoreSpotlightIndexer willModifySearchableItemsWithIdentifiers:forBundleID:completionHandler:]_block_invoke.1368
- ___107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.3116
- ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke.1557
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2426
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2428
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2428.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2431
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2431.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2432
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2432.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2433
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1486
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1494
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1500
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1506
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1509
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1501
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1507
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1510
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1510.cold.1
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1502
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1502.cold.1
- ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1508
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1392
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1400
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke.1400.cold.1
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_2.1396
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_3.1397
- ___125-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:forBundleID:fromClient:reason:completionHandler:]_block_invoke_4.1398
- ___154-[SpotlightReceiverConnection indexWithFd:offset:size:indexType:protectionClass:serialNumber:journalCookie:config:additionalAttributes:completionHandler:]_block_invoke
- ___154-[SpotlightReceiverConnection indexWithFd:offset:size:indexType:protectionClass:serialNumber:journalCookie:config:additionalAttributes:completionHandler:]_block_invoke.328
- ___154-[SpotlightReceiverConnection indexWithFd:offset:size:indexType:protectionClass:serialNumber:journalCookie:config:additionalAttributes:completionHandler:]_block_invoke.cold.1
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1308
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1308.cold.1
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1308.cold.2
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1327
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1329
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1329.cold.1
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1329.cold.2
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1332
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1332.cold.1
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1332.cold.2
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1335
- ___178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke_2.1328
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1220
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1220.cold.1
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1220.cold.2
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1220.cold.3
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1220.cold.4
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1247
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1259
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1291
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1296
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1300
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1271
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1292
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1297
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1297.cold.1
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_3.1272
- ___186-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_4.1273
- ___223-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.331
- ___223-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.332
- ___223-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.339
- ___223-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttributeArray:completionValueArray:alwaysReindexWithCompletionAttribute:force:postFilter:group:forceMerge:]_block_invoke.340
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2147
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2169
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2178
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2179
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2180
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2196
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2197
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2204
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2208
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2210.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2211
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2213
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2213.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2214
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2216
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2216.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2220
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2222
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2228
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2228.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2228.cold.2
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2248
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2254
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2254.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke.2254.cold.2
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2156
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2165
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2200
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2205
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2224
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2224.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2234
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2251
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2251.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_2.2258
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2157
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2157.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2235
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2235.cold.1
- ___30-[SPCoreSpotlightIndexer init]_block_invoke_3.2259
- ___31-[SPCoreSpotlightIndexer start]_block_invoke.2320
- ___39-[SPCoreSpotlightIndexer queryPreheat:]_block_invoke.2417
- ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.608
- ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.608.cold.1
- ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.609
- ___40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.617
- ___40-[SPCoreSpotlightIndexer issueHeartbeat]_block_invoke.2384
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.3127
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.3128
- ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2094
- ___44-[SPCoreSpotlightIndexer purgeIndexForSize:]_block_invoke.2094.cold.1
- ___50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke.1356
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2311
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2315
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2315.cold.1
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2315.cold.2
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2316
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2316.cold.1
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2317
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2317.cold.1
- ___51-[SPCoreSpotlightIndexer moveMailToClassCWithClone]_block_invoke.2318
- ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1640
- ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke_2
- ___59-[SPConcreteCoreSpotlightIndexer _performXPCActivity:name:]_block_invoke.624
- ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke
- ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.277
- ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.278
- ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.282
- ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.283
- ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.291
- ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.291.cold.1
- ___59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.293
- ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke.2299
- ___59-[SPCoreSpotlightIndexer _moveClassAIndexToClassCMailIndex]_block_invoke_2.2300
- ___60-[SPConcreteCoreSpotlightIndexer _addNewClientWithBundleID:]_block_invoke.1062
- ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.298
- ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.299
- ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.305
- ___60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.305.cold.1
- ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke.1196
- ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_2.1199
- ___60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_3.1202
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.669
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.669.cold.1
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.670
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.670.cold.1
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.671
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.671.cold.1
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.672
- ___62-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:activity:]_block_invoke.676
- ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.642
- ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.642.cold.1
- ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.646
- ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.646.cold.1
- ___63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.648
- ___63-[SPCoreSpotlightIndexer _deleteNonMailBundlesFromClassAIndex:]_block_invoke.2295
- ___65-[SPConcreteCoreSpotlightIndexer openIndexForUpgradeSynchronous:]_block_invoke.954
- ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2104
- ___67-[SPCoreSpotlightIndexer registerCacheDeleteCallbackForVolumePath:]_block_invoke.2105
- ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1056
- ___72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.1057
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1446
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1446.cold.1
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1450
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1450.cold.1
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1451
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1465
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1466
- ___73-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:depth:]_block_invoke.1470
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1338
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1342
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1348
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1348.cold.1
- ___76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1343
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1011
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1017
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1019
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1021.cold.1
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1026
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1030
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1033
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1041
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.1045
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.972
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke.977
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1018
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1020
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.1025
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.973
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_2.979
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_3.982
- ___78-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:]_block_invoke_4.985
- ___78-[SPConcreteCoreSpotlightIndexer scheduleMaintenance:description:forDarkWake:]_block_invoke.634
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.1095
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_2.1096
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_3.1103
- ___79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_3.1103.cold.1
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2468
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke.2469
- ___79-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:reason:completionHandler:]_block_invoke_2.2470
- ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.2349
- ___81-[SPConcreteCoreSpotlightIndexer processDecryptsForBundleID:persona:infos:group:]_block_invoke.1205
- ___81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2551
- ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.270
- ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.270.cold.1
- ___84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.270.cold.2
- ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.3115
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3064
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3064.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3066
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3068
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3068.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3069
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3070
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3070.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3071
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2636
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2643
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2663
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2697
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2701
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2705
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2725
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2737
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2750
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2944
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2945
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2952
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2956
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2957
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2961
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2965
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2984
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2644
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2729
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2751
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.3006
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.3010
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4.3034
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5.3035
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_6.3039
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_7.3052
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_8.3057
- ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1066
- ___92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.1067
- ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2497
- ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.2498
- ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.688
- ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.689
- ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.690
- ___94-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:depth:]_block_invoke.691
- ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1407
- ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1417
- ___97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_2.1418
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2342
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2342.cold.1
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2343
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2347
- ___97-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:]_block_invoke.2348
- ___block_descriptor_116_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_48_e8_32r40r_e13_v24?0^8^B16lr32l8r40l8
- ___block_descriptor_56_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40r48r_e69_v48?0"SPQueryJob"8q16Q24^{__MDStoreOIDArray=}32^{__MDPlistBytes=}40ls32l8r40l8r48l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e8_v12?0B8ls32l8s40l8s48l8r64l8s56l8
- ___block_literal_global.1029
- ___block_literal_global.1032
- ___block_literal_global.1035
- ___block_literal_global.1047
- ___block_literal_global.1191
- ___block_literal_global.1194
- ___block_literal_global.1198
- ___block_literal_global.1249
- ___block_literal_global.1261
- ___block_literal_global.1299
- ___block_literal_global.1331
- ___block_literal_global.1334
- ___block_literal_global.1402
- ___block_literal_global.1512
- ___block_literal_global.1567
- ___block_literal_global.1577
- ___block_literal_global.2075
- ___block_literal_global.2080
- ___block_literal_global.2086
- ___block_literal_global.2090
- ___block_literal_global.2107
- ___block_literal_global.2109
- ___block_literal_global.2111
- ___block_literal_global.2114
- ___block_literal_global.2131
- ___block_literal_global.2146
- ___block_literal_global.2150
- ___block_literal_global.2175
- ___block_literal_global.2199
- ___block_literal_global.2207
- ___block_literal_global.2253
- ___block_literal_global.2257
- ___block_literal_global.2323
- ___block_literal_global.2337
- ___block_literal_global.2341
- ___block_literal_global.2351
- ___block_literal_global.2403
- ___block_literal_global.2408
- ___block_literal_global.2410
- ___block_literal_global.2412
- ___block_literal_global.2455
- ___block_literal_global.2493
- ___block_literal_global.2500
- ___block_literal_global.2584
- ___block_literal_global.260
- ___block_literal_global.264
- ___block_literal_global.272
- ___block_literal_global.2869
- ___block_literal_global.2874
- ___block_literal_global.2879
- ___block_literal_global.2884
- ___block_literal_global.2889
- ___block_literal_global.2894
- ___block_literal_global.2899
- ___block_literal_global.2904
- ___block_literal_global.2909
- ___block_literal_global.297
- ___block_literal_global.301
- ___block_literal_global.3074
- ___block_literal_global.3126
- ___block_literal_global.3139
- ___block_literal_global.3672
- ___block_literal_global.3742
- ___block_literal_global.3799
- ___block_literal_global.3801
- ___block_literal_global.3838
- ___block_literal_global.3845
- ___block_literal_global.522
- ___block_literal_global.611
- ___block_literal_global.640
- ___block_literal_global.665
- ___block_literal_global.926
- ___block_literal_global.945
- ___block_literal_global.948
- ___block_literal_global.950
- ___block_literal_global.968
- ___block_literal_global.975
- ___block_literal_global.981
- ___block_literal_global.984
- ___block_literal_global.987
- ___processItemsForImportInner_block_invoke.3759
- _objc_msgSend$indexWithFd:offset:size:indexType:protectionClass:serialNumber:journalCookie:config:additionalAttributes:completionHandler:
CStrings:
+ "%@ %@ - %@\n"
+ "(%@) deleteActivities, options:0x%lx"
+ "(%@) deleteAllActivities, options:0x%lx"
+ "2391.1"
+ "@\"_DASSystemContext\""
+ "Complete will modify fixup query for bundleID:%@ pc: %@"
+ "InstantSender"
+ "SPDASManager"
+ "[IndexLoss] (%s) Intentional drop (%@) with reason %s"
+ "_context"
+ "addOrUpdateSearchableItemsInJournalFd:atOffset:size:indexType:bundleID:protectionClass:serialNumber:journalCookie:additionalAttributes:client:config:completionHandler:"
+ "clearDerived"
+ "clearDerivedHasPhotos"
+ "clearDerivedHasText"
+ "clearDerivedMail"
+ "clearDerivedPhotosAndText"
+ "indexWithFd:offset:size:indexType:bundleID:protectionClass:serialNumber:journalCookie:config:additionalAttributes:completionHandler:"
+ "issuePriorityIndexFixupOn:key:"
+ "kMDItemPhotosMediaTypes!=*  && _kMDItemBundleID!=\"com.apple.searchd\""
+ "kMDItemPhotosMediaTypes=*"
+ "kSPDerived"
+ "kSPEmail"
+ "kSPHasInitializedPhotosAndText"
+ "properties"
+ "v100@0:8i16Q20Q28Q36@44@52Q60@68@76@84@?92"
+ "v108@0:8i16Q20Q28Q36@44@52Q60@68@76q84@92@?100"
- "(%@) deleteActivties, options:0x%lx"
- "(%@) deleteAllActivties, options:0x%lx"
- "2387.1"
- "Complete wil modify fixup query for bundleID:%@ pc: %@"
- "addOrUpdateSearchableItemsInJournalFd:atOffset:size:indexType:protectionClass:serialNumber:journalCookie:additionalAttributes:client:config:completionHandler:"
- "indexWithFd:offset:size:indexType:protectionClass:serialNumber:journalCookie:config:additionalAttributes:completionHandler:"
- "v100@0:8i16Q20Q28Q36@44Q52@60@68q76@84@?92"
- "v92@0:8i16Q20Q28Q36@44Q52@60@68@76@?84"

```
