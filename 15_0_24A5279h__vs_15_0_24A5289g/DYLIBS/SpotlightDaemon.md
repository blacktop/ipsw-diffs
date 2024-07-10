## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/Versions/A/SpotlightDaemon`

```diff

-2308.1.5.0.0
-  __TEXT.__text: 0x907ac
-  __TEXT.__auth_stubs: 0x1990
-  __TEXT.__objc_methlist: 0x33c4
-  __TEXT.__const: 0x2f0
-  __TEXT.__cstring: 0x6574
-  __TEXT.__gcc_except_tab: 0x3810
-  __TEXT.__oslogstring: 0x7499
-  __TEXT.__unwind_info: 0x1cf8
-  __TEXT.__objc_classname: 0x3f9
-  __TEXT.__objc_methname: 0xb8d4
-  __TEXT.__objc_methtype: 0x1f76
-  __TEXT.__objc_stubs: 0x94e0
-  __DATA_CONST.__got: 0x818
+2310.1.4.0.0
+  __TEXT.__text: 0x917b4
+  __TEXT.__auth_stubs: 0x1a10
+  __TEXT.__objc_methlist: 0x347c
+  __TEXT.__const: 0x308
+  __TEXT.__cstring: 0x66c0
+  __TEXT.__gcc_except_tab: 0x379c
+  __TEXT.__oslogstring: 0x755f
+  __TEXT.__unwind_info: 0x1d18
+  __TEXT.__objc_classname: 0x410
+  __TEXT.__objc_methname: 0xbad0
+  __TEXT.__objc_methtype: 0x1f84
+  __TEXT.__objc_stubs: 0x9580
+  __DATA_CONST.__got: 0x828
   __DATA_CONST.__const: 0x430
-  __DATA_CONST.__objc_classlist: 0x130
+  __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ae0
+  __DATA_CONST.__objc_selrefs: 0x2b58
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xd8
+  __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x298
-  __AUTH_CONST.__auth_got: 0xce0
+  __AUTH_CONST.__auth_got: 0xd20
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x3de8
+  __AUTH_CONST.__const: 0x3e18
   __AUTH_CONST.__cfstring: 0x5080
-  __AUTH_CONST.__objc_const: 0x5508
+  __AUTH_CONST.__objc_const: 0x56b8
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0x380
+  __AUTH.__objc_data: 0x500
+  __DATA.__objc_ivar: 0x398
   __DATA.__data: 0x998
   __DATA.__bss: 0x380
   __DATA.__common: 0x10

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Intents.framework/Versions/A/Intents
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
+  - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/MetadataUtilities.framework/Versions/A/MetadataUtilities
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2359
-  Symbols:   5547
-  CStrings:  1089
+  Functions: 2381
+  Symbols:   5600
+  CStrings:  1091
 
Symbols:
+ -[CSThresholdedTrigger .cxx_destruct]
+ -[CSThresholdedTrigger actionCounts]
+ -[CSThresholdedTrigger countThreshold]
+ -[CSThresholdedTrigger incrementAndCheckPerformActionForKey:]
+ -[CSThresholdedTrigger initWithCountThreshold:timeInterval:]
+ -[CSThresholdedTrigger lastActionDates]
+ -[CSThresholdedTrigger setActionCounts:]
+ -[CSThresholdedTrigger setCountThreshold:]
+ -[CSThresholdedTrigger setLastActionDates:]
+ -[CSThresholdedTrigger setTimeInterval:]
+ -[CSThresholdedTrigger timeInterval]
+ -[SPConcreteCoreSpotlightIndexer jwlIndex]
+ -[SPConcreteCoreSpotlightIndexer openJWLIndex]
+ -[SPConcreteCoreSpotlightIndexer openJWLIndex].cold.1
+ -[SPConcreteCoreSpotlightIndexer setJwlIndex:]
+ GCC_except_table1005
+ GCC_except_table1155
+ GCC_except_table1157
+ GCC_except_table1158
+ GCC_except_table1250
+ GCC_except_table1277
+ GCC_except_table167
+ GCC_except_table168
+ GCC_except_table219
+ GCC_except_table256
+ GCC_except_table263
+ GCC_except_table275
+ GCC_except_table303
+ GCC_except_table326
+ GCC_except_table355
+ GCC_except_table367
+ GCC_except_table392
+ GCC_except_table408
+ GCC_except_table418
+ GCC_except_table457
+ GCC_except_table465
+ GCC_except_table482
+ GCC_except_table495
+ GCC_except_table544
+ GCC_except_table615
+ GCC_except_table653
+ GCC_except_table663
+ GCC_except_table671
+ GCC_except_table696
+ GCC_except_table697
+ GCC_except_table705
+ GCC_except_table740
+ GCC_except_table787
+ GCC_except_table827
+ GCC_except_table828
+ GCC_except_table834
+ GCC_except_table835
+ GCC_except_table836
+ GCC_except_table842
+ GCC_except_table855
+ GCC_except_table858
+ GCC_except_table868
+ GCC_except_table877
+ GCC_except_table882
+ GCC_except_table887
+ GCC_except_table892
+ GCC_except_table898
+ GCC_except_table912
+ GCC_except_table953
+ GCC_except_table955
+ GCC_except_table960
+ GCC_except_table999
+ OBJC_IVAR_$_CSThresholdedTrigger._actionCounts
+ OBJC_IVAR_$_CSThresholdedTrigger._countThreshold
+ OBJC_IVAR_$_CSThresholdedTrigger._lastActionDates
+ OBJC_IVAR_$_CSThresholdedTrigger._timeInterval
+ OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._jwlIndex
+ OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._tryOpenJwlIndex
+ _CSGetDiskVersionForContentURL
+ _NSURLErrorKey
+ _OBJC_CLASS_$_CSThresholdedTrigger
+ _OBJC_METACLASS_$_CSThresholdedTrigger
+ _SICloseJWLIndex
+ _SIOpenJWLIndex
+ _UTTypePackage
+ __100-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:completionHandler:]_block_invoke.cold.1
+ __100-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:completionHandler:]_block_invoke.cold.2
+ __100-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:completionHandler:]_block_invoke.cold.3
+ __101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke.1398
+ __105-[SPConcreteCoreSpotlightIndexer willModifySearchableItemsWithIdentifiers:forBundleID:completionHandler:]_block_invoke.1268
+ __107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.2851
+ __108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1368
+ __108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1374
+ __108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1384
+ __108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1388
+ __108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_2.1385
+ __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2166.cold.1
+ __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2170
+ __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2170.cold.1
+ __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2171
+ __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2171.cold.1
+ __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2172
+ __143-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:force:postFilter:]_block_invoke.233
+ __143-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:force:postFilter:]_block_invoke.239
+ __143-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:force:postFilter:]_block_invoke.240
+ __143-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:force:postFilter:]_block_invoke_2.241
+ __176-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1144
+ __176-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1144.cold.1
+ __176-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1144.cold.2
+ __176-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1169
+ __176-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1182
+ __176-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1183
+ __176-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.cold.4
+ __176-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.cold.5
+ __176-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.cold.6
+ __176-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1184
+ __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1188
+ __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1188.cold.1
+ __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1188.cold.2
+ __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1209
+ __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1211.cold.1
+ __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1211.cold.2
+ __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1214
+ __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1214.cold.1
+ __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1214.cold.2
+ __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1217
+ __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke_2.1210
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.1926
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.1940
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.1944
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.1951
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.1952
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.1955
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.1972
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.1972.cold.1
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.1973
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.1975
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.1975.cold.1
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.1976
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.1977
+ __30-[SPCoreSpotlightIndexer init]_block_invoke.1988
+ __30-[SPCoreSpotlightIndexer init]_block_invoke_2.1933
+ __30-[SPCoreSpotlightIndexer init]_block_invoke_2.1978
+ __30-[SPCoreSpotlightIndexer init]_block_invoke_3.1979
+ __30-[SPCoreSpotlightIndexer init]_block_invoke_4.1980
+ __31-[SPCoreSpotlightIndexer start]_block_invoke.2015
+ __31-[SPCoreSpotlightIndexer start]_block_invoke.2020
+ __39-[SPCoreSpotlightIndexer queryPreheat:]_block_invoke.2152
+ __40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.409
+ __40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.410
+ __40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.2866
+ __40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.2867
+ __41-[MDSearchableIndexService issueCommand:]_block_invoke.240.cold.1
+ __41-[SPCoreSpotlightIndexer issueHeartbeat:]_block_invoke.2105
+ __41-[SPCoreSpotlightIndexer issueHeartbeat:]_block_invoke.2115
+ __42-[SPCoreSpotlightIndexer handleLikelyExit]_block_invoke.2143
+ __50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke.1247
+ __50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke.1252
+ __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke.490
+ __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke.490.cold.1
+ __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke.494
+ __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke.500
+ __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke_2.504
+ __57-[SPConcreteCoreSpotlightIndexer zombifyAllContactItems:]_block_invoke.1336
+ __57-[SPConcreteCoreSpotlightIndexer zombifyAllContactItems:]_block_invoke_2.1337
+ __58-[SPConcreteCoreSpotlightIndexer reindexSystemPreferences]_block_invoke.442
+ __58-[SPConcreteCoreSpotlightIndexer reindexSystemPreferences]_block_invoke.443
+ __58-[SPConcreteCoreSpotlightIndexer removeSandboxExtensions:]_block_invoke.1360
+ __58-[SPConcreteCoreSpotlightIndexer removeSandboxExtensions:]_block_invoke_2.1361
+ __58-[SPCoreSpotlightIndexer handleRankingCommand:completion:]_block_invoke.2843
+ __58-[SPCoreSpotlightIndexer handleRankingCommand:completion:]_block_invoke_2.2844
+ __59-[SPConcreteCoreSpotlightIndexer _performXPCActivity:name:]_block_invoke.421
+ __59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.188
+ __59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.189
+ __59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.197
+ __59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.197.cold.1
+ __59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.201
+ __59-[SPCoreSpotlightIndexer issueSharedDocumentAttributeFixup]_block_invoke.2082
+ __60-[SPConcreteCoreSpotlightIndexer _addNewClientWithBundleID:]_block_invoke.938
+ __60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.208
+ __60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.216
+ __60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.216.cold.1
+ __60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke.1119
+ __60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_2.1122
+ __60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_3.1125
+ __63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.454
+ __63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.454.cold.1
+ __63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.460
+ __63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.460.cold.1
+ __63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.464
+ __65-[SPConcreteCoreSpotlightIndexer openIndexForUpgradeSynchronous:]_block_invoke.806
+ __67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.1346
+ __67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.1346.cold.1
+ __67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.1347
+ __67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.1349.cold.1
+ __67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.1352
+ __68-[SPCoreSpotlightIndexer deleteActionsBeforeTime:completionHandler:]_block_invoke.2256
+ __69-[SPConcreteCoreSpotlightIndexer issueDumpReverse:completionHandler:]_block_invoke.1018
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.825
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.836
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.862
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.867
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.867.cold.1
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.893
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.893.cold.1
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.898
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.903
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.905
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.905.cold.1
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.910
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.911
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.922
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.926
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.829
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.839
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.885
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.885.cold.1
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.904
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.909
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.927
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_3.842
+ __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_3.886
+ __70-[SPConcreteCoreSpotlightIndexer removeExpiredItemsForBundleId:group:]_block_invoke.484
+ __70-[SPConcreteCoreSpotlightIndexer writeDiagnostic:bundleID:identifier:]_block_invoke.1068
+ __70-[SPConcreteCoreSpotlightIndexer writeDiagnostic:bundleID:identifier:]_block_invoke.1078
+ __70-[SPConcreteCoreSpotlightIndexer writeDiagnostic:bundleID:identifier:]_block_invoke_2.1069
+ __70-[SPConcreteCoreSpotlightIndexer writeDiagnostic:bundleID:identifier:]_block_invoke_2.1082
+ __71-[SPConcreteCoreSpotlightIndexer performIndexerTask:completionHandler:]_block_invoke.943
+ __72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.932
+ __72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.933
+ __72-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:completionHandler:]_block_invoke.2212
+ __72-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:completionHandler:]_block_invoke.2213
+ __72-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:completionHandler:]_block_invoke_2.2214
+ __73-[SPCoreSpotlightIndexer deleteActionsWithIdentifiers:completionHandler:]_block_invoke.2261
+ __75-[SPCoreSpotlightIndexer _reindexAllItemsWithExtensionsAndCompletionBlock:]_block_invoke.2883
+ __76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1222
+ __76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1226
+ __76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1239
+ __76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1239.cold.1
+ __76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1227
+ __78-[SPConcreteCoreSpotlightIndexer scheduleMaintenance:description:forDarkWake:]_block_invoke.434
+ __78-[SPCoreSpotlightIndexer _reindexAllIdentifiersWithExtension:completionBlock:]_block_invoke.2876
+ __79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.983
+ __79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.984
+ __79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.999
+ __79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.999.cold.1
+ __79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_2.985
+ __79-[SPCoreSpotlightIndexer deleteAllUserActivities:fromClient:completionHandler:]_block_invoke.2251
+ __80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.2065
+ __81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2318
+ __81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2323
+ __81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke_2.2327
+ __84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.178
+ __84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.178.cold.1
+ __84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.178.cold.2
+ __84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.2850
+ __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2784
+ __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2788
+ __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2788.cold.1
+ __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2789
+ __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2790
+ __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2790.cold.1
+ __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2791
+ __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2795
+ __87-[SPConcreteCoreSpotlightIndexer _saveCorruptIndexWithPath:shouldSendABC:fullyCreated:]_block_invoke.792
+ __87-[SPConcreteCoreSpotlightIndexer _saveCorruptIndexWithPath:shouldSendABC:fullyCreated:]_block_invoke.792.cold.1
+ __87-[SPCoreSpotlightIndexer rewriteQueryWithQueryString:context:matchInfo:rewriteHandler:]_block_invoke.2186
+ __88-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:]_block_invoke.515
+ __88-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:]_block_invoke.516
+ __88-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:]_block_invoke.517
+ __89-[SPCoreSpotlightIndexer _reindexAllItemsWithExtensionsAndIdentifiersAndCompletionBlock:]_block_invoke.2889
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2405
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2425
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2462
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2466
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2489
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2499
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2512
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2684
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2694
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2697
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2704
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2710
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2711
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2717
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2721
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2740
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2406
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2513
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2756
+ __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.2760
+ __92-[SPConcreteCoreSpotlightIndexer deleteItemsForQuery:bundleID:fromClient:completionHandler:]_block_invoke.1279
+ __92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.947
+ __92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.948
+ __93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2242
+ __93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2245
+ __93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.2246
+ __96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.2046
+ __96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.2046.cold.1
+ __96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.2047
+ __96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.2055
+ __96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.2060
+ __97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1297
+ __97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1307
+ __97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_2.1308
+ __OBJC_$_INSTANCE_METHODS_CSThresholdedTrigger
+ __OBJC_$_INSTANCE_VARIABLES_CSThresholdedTrigger
+ __OBJC_$_PROP_LIST_CSThresholdedTrigger
+ __OBJC_CLASS_RO_$_CSThresholdedTrigger
+ __OBJC_METACLASS_RO_$_CSThresholdedTrigger
+ ___block_descriptor_124_e8_32s40s48s56r_e28_v24?0"NSData"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSData"8"NSError"16l
+ __block_literal_global.1112
+ __block_literal_global.1121
+ __block_literal_global.1129
+ __block_literal_global.1171
+ __block_literal_global.1186
+ __block_literal_global.1213
+ __block_literal_global.1216
+ __block_literal_global.1449
+ __block_literal_global.1462
+ __block_literal_global.180
+ __block_literal_global.1868
+ __block_literal_global.1873
+ __block_literal_global.1877
+ __block_literal_global.1889
+ __block_literal_global.1898
+ __block_literal_global.1946
+ __block_literal_global.2034
+ __block_literal_global.2036
+ __block_literal_global.2045
+ __block_literal_global.2067
+ __block_literal_global.210
+ __block_literal_global.212
+ __block_literal_global.2122
+ __block_literal_global.2132
+ __block_literal_global.2142
+ __block_literal_global.2145
+ __block_literal_global.2154
+ __block_literal_global.2204
+ __block_literal_global.2235
+ __block_literal_global.2248
+ __block_literal_global.2348
+ __block_literal_global.244
+ __block_literal_global.2631
+ __block_literal_global.2636
+ __block_literal_global.2641
+ __block_literal_global.2646
+ __block_literal_global.2651
+ __block_literal_global.2656
+ __block_literal_global.2799
+ __block_literal_global.2865
+ __block_literal_global.2886
+ __block_literal_global.3411
+ __block_literal_global.3436
+ __block_literal_global.3443
+ __block_literal_global.405
+ __block_literal_global.452
+ __block_literal_global.486
+ __block_literal_global.785
+ __block_literal_global.800
+ __block_literal_global.805
+ __block_literal_global.827
+ __block_literal_global.832
+ __block_literal_global.838
+ __block_literal_global.869
+ __block_literal_global.895
+ __block_literal_global.913
+ __block_literal_global.924
+ __dyld_images_for_addresses
+ _arc4random_buf
+ _change_fdguard_np
+ _fgetattrlist
+ _guarded_close_np
+ _objc_autorelease
+ _objc_msgSend$conformsToType:
+ _objc_msgSend$isFileURL
+ _objc_msgSend$jwlIndex
+ _objc_msgSend$openJWLIndex
+ _objc_msgSend$timeInterval
+ _uuidBytesToString
- GCC_except_table1001
- GCC_except_table1151
- GCC_except_table1153
- GCC_except_table1154
- GCC_except_table1239
- GCC_except_table1266
- GCC_except_table134
- GCC_except_table135
- GCC_except_table146
- GCC_except_table217
- GCC_except_table255
- GCC_except_table262
- GCC_except_table274
- GCC_except_table302
- GCC_except_table325
- GCC_except_table354
- GCC_except_table365
- GCC_except_table391
- GCC_except_table407
- GCC_except_table417
- GCC_except_table456
- GCC_except_table464
- GCC_except_table481
- GCC_except_table493
- GCC_except_table541
- GCC_except_table611
- GCC_except_table649
- GCC_except_table659
- GCC_except_table667
- GCC_except_table692
- GCC_except_table693
- GCC_except_table701
- GCC_except_table736
- GCC_except_table783
- GCC_except_table819
- GCC_except_table824
- GCC_except_table830
- GCC_except_table831
- GCC_except_table832
- GCC_except_table838
- GCC_except_table851
- GCC_except_table854
- GCC_except_table864
- GCC_except_table873
- GCC_except_table878
- GCC_except_table883
- GCC_except_table888
- GCC_except_table894
- GCC_except_table908
- GCC_except_table949
- GCC_except_table951
- GCC_except_table956
- GCC_except_table995
- __101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke.1400
- __105-[SPConcreteCoreSpotlightIndexer willModifySearchableItemsWithIdentifiers:forBundleID:completionHandler:]_block_invoke.1270
- __107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.2843
- __108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1370
- __108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1376
- __108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1386
- __108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1390
- __108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_2.1387
- __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2158
- __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2160
- __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2160.cold.1
- __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2164.cold.1
- __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2165
- __114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2165.cold.1
- __143-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:force:postFilter:]_block_invoke.236
- __143-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:force:postFilter:]_block_invoke.242
- __143-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:force:postFilter:]_block_invoke.243
- __143-[SPConcreteCoreSpotlightIndexer reindexAttributes:ofItemsMatchingQuery:indexAttrName:withVersion:perItemCompletionAttribute:force:postFilter:]_block_invoke_2.244
- __176-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1146
- __176-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1146.cold.1
- __176-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1146.cold.2
- __176-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1171
- __176-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1184
- __176-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke.1185
- __176-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2.1186
- __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1190
- __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1190.cold.1
- __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1190.cold.2
- __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1213
- __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1213.cold.1
- __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1213.cold.2
- __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1216
- __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1216.cold.1
- __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1216.cold.2
- __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke.1219
- __178-[SPConcreteCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:forBundleID:options:completionHandler:]_block_invoke_2.1212
- __30-[SPCoreSpotlightIndexer init]_block_invoke.1920
- __30-[SPCoreSpotlightIndexer init]_block_invoke.1934
- __30-[SPCoreSpotlightIndexer init]_block_invoke.1938
- __30-[SPCoreSpotlightIndexer init]_block_invoke.1945
- __30-[SPCoreSpotlightIndexer init]_block_invoke.1946
- __30-[SPCoreSpotlightIndexer init]_block_invoke.1949
- __30-[SPCoreSpotlightIndexer init]_block_invoke.1961
- __30-[SPCoreSpotlightIndexer init]_block_invoke.1963
- __30-[SPCoreSpotlightIndexer init]_block_invoke.1963.cold.1
- __30-[SPCoreSpotlightIndexer init]_block_invoke.1964
- __30-[SPCoreSpotlightIndexer init]_block_invoke.1966
- __30-[SPCoreSpotlightIndexer init]_block_invoke.1966.cold.1
- __30-[SPCoreSpotlightIndexer init]_block_invoke.1971
- __30-[SPCoreSpotlightIndexer init]_block_invoke.1982
- __30-[SPCoreSpotlightIndexer init]_block_invoke_2.1927
- __30-[SPCoreSpotlightIndexer init]_block_invoke_2.1972
- __30-[SPCoreSpotlightIndexer init]_block_invoke_3.1973
- __30-[SPCoreSpotlightIndexer init]_block_invoke_4.1974
- __31-[SPCoreSpotlightIndexer start]_block_invoke.2009
- __31-[SPCoreSpotlightIndexer start]_block_invoke.2014
- __39-[SPCoreSpotlightIndexer queryPreheat:]_block_invoke.2146
- __40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.412
- __40-[SPConcreteCoreSpotlightIndexer dirty:]_block_invoke.413
- __40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.2858
- __40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.2859
- __41-[SPCoreSpotlightIndexer issueHeartbeat:]_block_invoke.2099
- __41-[SPCoreSpotlightIndexer issueHeartbeat:]_block_invoke.2109
- __42-[SPCoreSpotlightIndexer handleLikelyExit]_block_invoke.2137
- __50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke.1249
- __50-[SPConcreteCoreSpotlightIndexer validateVectors:]_block_invoke.1254
- __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke.496
- __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke.496.cold.1
- __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke.497
- __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke.503
- __53-[SPConcreteCoreSpotlightIndexer revokeExpiredItems:]_block_invoke_2.507
- __57-[SPConcreteCoreSpotlightIndexer zombifyAllContactItems:]_block_invoke.1338
- __57-[SPConcreteCoreSpotlightIndexer zombifyAllContactItems:]_block_invoke_2.1339
- __58-[SPConcreteCoreSpotlightIndexer reindexSystemPreferences]_block_invoke.445
- __58-[SPConcreteCoreSpotlightIndexer reindexSystemPreferences]_block_invoke.446
- __58-[SPConcreteCoreSpotlightIndexer removeSandboxExtensions:]_block_invoke.1362
- __58-[SPConcreteCoreSpotlightIndexer removeSandboxExtensions:]_block_invoke_2.1363
- __58-[SPCoreSpotlightIndexer handleRankingCommand:completion:]_block_invoke.2835
- __58-[SPCoreSpotlightIndexer handleRankingCommand:completion:]_block_invoke_2.2836
- __59-[SPConcreteCoreSpotlightIndexer _performXPCActivity:name:]_block_invoke.424
- __59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.191
- __59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.192
- __59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.200
- __59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.200.cold.1
- __59-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOn]_block_invoke.204
- __59-[SPCoreSpotlightIndexer issueSharedDocumentAttributeFixup]_block_invoke.2076
- __60-[SPConcreteCoreSpotlightIndexer _addNewClientWithBundleID:]_block_invoke.941
- __60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.211
- __60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.219
- __60-[SPConcreteCoreSpotlightIndexer issuePriorityIndexFixupOff]_block_invoke.219.cold.1
- __60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke.1122
- __60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_2.1125
- __60-[SPConcreteCoreSpotlightIndexer suspendIndexForDeviceLock:]_block_invoke_3.1128
- __63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.457
- __63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.457.cold.1
- __63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.463
- __63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.463.cold.1
- __63-[SPConcreteCoreSpotlightIndexer indexFinishedDrainingJournal:]_block_invoke.467
- __65-[SPConcreteCoreSpotlightIndexer openIndexForUpgradeSynchronous:]_block_invoke.809
- __67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.1348
- __67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.1348.cold.1
- __67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.1351
- __67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.1351.cold.1
- __67-[SPConcreteCoreSpotlightIndexer restartAttachmentImport:maxCount:]_block_invoke.1354
- __68-[SPCoreSpotlightIndexer deleteActionsBeforeTime:completionHandler:]_block_invoke.2250
- __69-[SPConcreteCoreSpotlightIndexer issueDumpReverse:completionHandler:]_block_invoke.1021
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.828
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.839
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.865
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.870
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.870.cold.1
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.896
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.896.cold.1
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.901
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.906
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.908
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.908.cold.1
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.913
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.920
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.925
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke.929
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.832
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.842
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.888
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.888.cold.1
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.907
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.912
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_2.930
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_3.845
- __70-[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:]_block_invoke_3.889
- __70-[SPConcreteCoreSpotlightIndexer removeExpiredItemsForBundleId:group:]_block_invoke.487
- __70-[SPConcreteCoreSpotlightIndexer writeDiagnostic:bundleID:identifier:]_block_invoke.1071
- __70-[SPConcreteCoreSpotlightIndexer writeDiagnostic:bundleID:identifier:]_block_invoke.1081
- __70-[SPConcreteCoreSpotlightIndexer writeDiagnostic:bundleID:identifier:]_block_invoke_2.1072
- __70-[SPConcreteCoreSpotlightIndexer writeDiagnostic:bundleID:identifier:]_block_invoke_2.1085
- __71-[SPConcreteCoreSpotlightIndexer performIndexerTask:completionHandler:]_block_invoke.946
- __72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.935
- __72-[SPConcreteCoreSpotlightIndexer checkInWithBundleID:completionHandler:]_block_invoke.936
- __72-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:completionHandler:]_block_invoke.2206
- __72-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:completionHandler:]_block_invoke.2207
- __72-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:completionHandler:]_block_invoke_2.2208
- __73-[SPCoreSpotlightIndexer deleteActionsWithIdentifiers:completionHandler:]_block_invoke.2255
- __75-[SPCoreSpotlightIndexer _reindexAllItemsWithExtensionsAndCompletionBlock:]_block_invoke.2875
- __76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1224
- __76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1228
- __76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1241
- __76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke.1241.cold.1
- __76-[SPConcreteCoreSpotlightIndexer validateConcreteIndexer:outFileDescriptor:]_block_invoke_2.1229
- __78-[SPConcreteCoreSpotlightIndexer scheduleMaintenance:description:forDarkWake:]_block_invoke.437
- __78-[SPCoreSpotlightIndexer _reindexAllIdentifiersWithExtension:completionBlock:]_block_invoke.2868
- __79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.1002
- __79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.1002.cold.1
- __79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.986
- __79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke.987
- __79-[SPConcreteCoreSpotlightIndexer fixupMessageAttachmentsWithCompletionHandler:]_block_invoke_2.988
- __79-[SPCoreSpotlightIndexer deleteAllUserActivities:fromClient:completionHandler:]_block_invoke.2245
- __80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.2059
- __81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2310
- __81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke.2315
- __81-[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:]_block_invoke_2.2319
- __84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.181
- __84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.181.cold.1
- __84-[SPConcreteCoreSpotlightIndexer notifyClientForItemUpdates:updatedItems:batchMask:]_block_invoke.181.cold.2
- __84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.2842
- __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2774
- __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2774.cold.1
- __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2776
- __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2780
- __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2780.cold.1
- __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2781
- __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2783
- __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.2787
- __87-[SPConcreteCoreSpotlightIndexer _saveCorruptIndexWithPath:shouldSendABC:fullyCreated:]_block_invoke.795
- __87-[SPConcreteCoreSpotlightIndexer _saveCorruptIndexWithPath:shouldSendABC:fullyCreated:]_block_invoke.795.cold.1
- __87-[SPCoreSpotlightIndexer rewriteQueryWithQueryString:context:matchInfo:rewriteHandler:]_block_invoke.2180
- __88-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:]_block_invoke.519
- __88-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:]_block_invoke.520
- __88-[SPConcreteCoreSpotlightIndexer requestRequiresImportWithoutSandboxExtension:maxCount:]_block_invoke.521
- __89-[SPCoreSpotlightIndexer _reindexAllItemsWithExtensionsAndIdentifiersAndCompletionBlock:]_block_invoke.2881
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2389
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2417
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2450
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2454
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2481
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2491
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2504
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2676
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2686
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2689
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2696
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2702
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2703
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2709
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2713
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke.2732
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2398
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2505
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2.2748
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3.2752
- __92-[SPConcreteCoreSpotlightIndexer deleteItemsForQuery:bundleID:fromClient:completionHandler:]_block_invoke.1281
- __92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.950
- __92-[SPConcreteCoreSpotlightIndexer performIndexerTask:withIndexDelegatesAndCompletionHandler:]_block_invoke.951
- __93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2236
- __93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.2239
- __93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.2240
- __96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.2040
- __96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.2040.cold.1
- __96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.2041
- __96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.2049
- __96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.2054
- __97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1299
- __97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke.1309
- __97-[SPConcreteCoreSpotlightIndexer deleteSearchableItemsWithFileProviderDomains:completionHandler:]_block_invoke_2.1310
- ___block_descriptor_108_e8_32s40s48s_e28_v24?0"NSData"8"NSError"16l
- __block_literal_global.1118
- __block_literal_global.1130
- __block_literal_global.1132
- __block_literal_global.1173
- __block_literal_global.1188
- __block_literal_global.1215
- __block_literal_global.1218
- __block_literal_global.1451
- __block_literal_global.1464
- __block_literal_global.183
- __block_literal_global.1862
- __block_literal_global.1867
- __block_literal_global.1871
- __block_literal_global.1883
- __block_literal_global.1892
- __block_literal_global.1940
- __block_literal_global.2028
- __block_literal_global.2030
- __block_literal_global.2039
- __block_literal_global.2061
- __block_literal_global.2116
- __block_literal_global.2124
- __block_literal_global.2126
- __block_literal_global.213
- __block_literal_global.2139
- __block_literal_global.2148
- __block_literal_global.215
- __block_literal_global.2198
- __block_literal_global.2229
- __block_literal_global.2242
- __block_literal_global.2340
- __block_literal_global.247
- __block_literal_global.2623
- __block_literal_global.2628
- __block_literal_global.2633
- __block_literal_global.2638
- __block_literal_global.2643
- __block_literal_global.2648
- __block_literal_global.2791
- __block_literal_global.2857
- __block_literal_global.2878
- __block_literal_global.3395
- __block_literal_global.3428
- __block_literal_global.3435
- __block_literal_global.408
- __block_literal_global.455
- __block_literal_global.489
- __block_literal_global.788
- __block_literal_global.806
- __block_literal_global.808
- __block_literal_global.830
- __block_literal_global.835
- __block_literal_global.847
- __block_literal_global.872
- __block_literal_global.898
- __block_literal_global.922
- __block_literal_global.927
CStrings:
+ "(_index && !_jwlIndex) || (!_index && _jwlIndex)"
+ "-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:completionHandler:]_block_invoke"
+ "-[SPConcreteCoreSpotlightIndexer indexFromBundle:personaID:options:items:itemsText:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:]_block_invoke"
+ "2310.1.4"
+ "kQPQueryEmbeddingEncodedData"
- "2308.1.5"
- "PhotosSodiumRanking"
- "kQPPhotosEmbeddingEncodedData"

```
