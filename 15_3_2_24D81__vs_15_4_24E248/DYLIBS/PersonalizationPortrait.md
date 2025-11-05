## PersonalizationPortrait

> `/System/Library/PrivateFrameworks/PersonalizationPortrait.framework/Versions/A/PersonalizationPortrait`

```diff

-1271.10.0.0.0
-  __TEXT.__text: 0x65278
+1276.10.4.0.0
+  __TEXT.__text: 0x64870
   __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__objc_methlist: 0x6558
-  __TEXT.__gcc_except_tab: 0x10a0
-  __TEXT.__const: 0x1b8
+  __TEXT.__objc_methlist: 0x6e9c
+  __TEXT.__const: 0x1b0
   __TEXT.__cstring: 0x597a
+  __TEXT.__gcc_except_tab: 0x1094
   __TEXT.__oslogstring: 0x3021
   __TEXT.__dlopen_cstrs: 0xd5
   __TEXT.__unwind_info: 0x1ba0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a68
+  __DATA_CONST.__objc_selrefs: 0x2bf8
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x358
   __DATA_CONST.__objc_arraydata: 0x370
   __AUTH_CONST.__auth_got: 0x388
   __AUTH_CONST.__const: 0x2290
   __AUTH_CONST.__cfstring: 0x7dc0
-  __AUTH_CONST.__objc_const: 0xd170
+  __AUTH_CONST.__objc_const: 0xc0c0
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x9d8
   __AUTH_CONST.__objc_arrayobj: 0x228

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CD698AD0-A6C7-3DE4-A295-3CB4924FA160
+  UUID: 0B24B01C-79B4-3257-AE79-AD0499246AFB
   Functions: 2568
   Symbols:   6121
   CStrings:  4996
Symbols:
+ EventKitLibraryCore.frameworkLibrary.1603
+ EventKitLibraryCore.frameworkLibrary.6381
+ __105-[PPConnectionsClient recentLocationsForConsumer:criteria:limit:explanationSet:client:error:handleBatch:]_block_invoke.99
+ __20-[PPEvent attendees]_block_invoke.179
+ __21-[PPEventClient init]_block_invoke.108
+ __23-[PPContactClient init]_block_invoke.100
+ __27-[PPConnectionsClient init]_block_invoke.79
+ __29-[PPTopicReadOnlyClient init]_block_invoke.102
+ __31-[PPSocialHighlightClient init]_block_invoke.87
+ __31-[PPTemporalClusterClient init]_block_invoke.77
+ __32-[PPEventStore _recordGenerator]_block_invoke.15
+ __32-[PPLocationReadOnlyClient init]_block_invoke.80
+ __34-[PPContactStore _recordGenerator]_block_invoke.27
+ __35-[PPNamedEntityReadOnlyClient init]_block_invoke.82
+ __38-[PPEventClient sendRTCLogsWithError:]_block_invoke.158
+ __39-[PPReranker rerankedMediaItems:error:]_block_invoke.31
+ __40-[PPConfigClient assetVersionWithError:]_block_invoke.73
+ __40-[PPSocialHighlightClient decayInterval]_block_invoke.98
+ __41+[PPUtils jaroSimilarityForString:other:]_block_invoke.53
+ __41-[PPContactStore _sendChangesToDelegates]_block_invoke.35
+ __46+[PPEvent deferredAllocationEventFromEKEvent:]_block_invoke.149
+ __46+[PPEvent deferredAllocationEventFromEKEvent:]_block_invoke_2.151
+ __46-[PPReranker _lazyLoadEntityRankMapWithError:]_block_invoke.14
+ __48-[PPXPCClientHelper _locked_establishConnection]_block_invoke.7
+ __50-[PPXPCNamedEntityStore _recordGeneratorForQuery:]_block_invoke.52
+ __56-[PPTopicReadWriteClient _doSyncCallWithError:syncCall:]_block_invoke.86
+ __57-[PPNamedEntityReadOnlyClient mapItemForPlaceName:error:]_block_invoke.110
+ __58-[PPSocialHighlightClient attributionForIdentifier:error:]_block_invoke.120
+ __59-[PPLocationReadWriteClient _doSyncCallWithError:syncCall:]_block_invoke.74
+ __61-[PPContactClient rankedContactsWithQuery:error:handleBatch:]_block_invoke.114
+ __61-[PPEventClient eventNameRecordsForClient:error:handleBatch:]_block_invoke.121
+ __62-[PPNamedEntityReadWriteClient _doSyncCallWithError:syncCall:]_block_invoke.94
+ __64-[PPEventClient interactionSummaryMetricsWithError:handleBatch:]_block_invoke.153
+ __65-[PPTopicReadOnlyClient rankedTopicsWithQuery:error:handleBatch:]_block_invoke.127
+ __66+[PPEvent convertBatchOfEKEvents:calendarInternPool:interningSet:]_block_invoke.157
+ __66-[PPEventClient eventHighlightsFrom:to:options:error:handleBatch:]_block_invoke.140
+ __66-[PPNotificationManager addMeCardChangeBlock:forLifetimeOfObject:]_block_invoke.163
+ __66-[PPNotificationManager addMeCardChangeBlock:forLifetimeOfObject:]_block_invoke.167
+ __66-[PPNotificationManager addMeCardChangeBlock:forLifetimeOfObject:]_block_invoke_2.168
+ __66-[PPNotificationManager addMeCardChangeBlock:forLifetimeOfObject:]_block_invoke_3.169
+ __68-[PPNotificationManager addContactsChangeBlock:forLifetimeOfObject:]_block_invoke.157
+ __68-[PPNotificationManager addEventKitChangeBlock:forLifetimeOfObject:]_block_invoke.202
+ __68-[PPNotificationManager addEventKitChangeBlock:forLifetimeOfObject:]_block_invoke.203
+ __68-[PPNotificationManager addEventKitChangeBlock:forLifetimeOfObject:]_block_invoke.206
+ __68-[PPNotificationManager addEventKitChangeBlock:forLifetimeOfObject:]_block_invoke.223
+ __68-[PPNotificationManager addPortraitChangeBlock:forLifetimeOfObject:]_block_invoke.182
+ __69-[PPInternalClient trialOverridePath:namespaceName:factorName:error:]_block_invoke.112
+ __71-[PPLocationReadOnlyClient rankedLocationsWithQuery:error:handleBatch:]_block_invoke.100
+ __71-[PPNotificationManager addSuggestionsChangeBlock:forLifetimeOfObject:]_block_invoke.249
+ __71-[PPTopicReadOnlyClient scoresForTopicMapping:query:error:handleBatch:]_block_invoke.140
+ __72-[PPEventClient resolveEventNameRecordChanges:client:error:handleBatch:]_block_invoke.131
+ __74-[PPNotificationManager addPortraitInvalidationBlock:forLifetimeOfObject:]_block_invoke.187
+ __74-[PPNotificationManager addPortraitInvalidationBlock:forLifetimeOfObject:]_block_invoke.190
+ __75+[PPCustomDonation donateLabeledStrings:bundleId:groupId:documentId:error:]_block_invoke.114
+ __76-[PPTopicReadOnlyClient unmapMappedTopicIdentifier:mappingIdentifier:error:]_block_invoke.157
+ __77-[PPRecordMonitoringHelper _setupRecentChangesWithDelegates:recordGenerator:]_block_invoke.13
+ __78-[PPNamedEntityReadOnlyClient rankedNamedEntitiesWithQuery:error:handleBatch:]_block_invoke.102
+ __78-[PPNotificationManager addCalendarVisibilityChangeBlock:forLifetimeOfObject:]_block_invoke.237
+ __81-[PPConnectionsClient recentLocationDonationsSinceDate:client:error:handleBatch:]_block_invoke.93
+ __86-[PPSocialHighlightClient rankedHighlightsWithLimit:client:variant:error:handleBatch:]_block_invoke.105
+ __88-[PPTemporalClusterClient rankedTemporalClustersForStartDate:endDate:error:handleBatch:]_block_invoke.91
+ __89-[PPXPCNamedEntityStore loadNamedEntityRecordsAndMonitorChangesWithDelegate:query:error:]_block_invoke.63
+ __91-[PPSocialHighlightClient rankedHighlightsForSyncedItems:client:variant:error:handleBatch:]_block_invoke.114
+ __94-[PPRecordMonitoringHelper _handleRecentChangesWithDelegates:changeGenerator:recordGenerator:]_block_invoke.15
+ __94-[PPRecordMonitoringHelper _handleRecentChangesWithDelegates:changeGenerator:recordGenerator:]_block_invoke.16
+ __95+[PPCustomDonation donateParsecNamedEntitiesAndTopics:rawQuery:reformulatedQuery:source:error:]_block_invoke.102
+ __95-[PPAdaptiveCoalescer coalesceRequestKey:handler:executeRequestAndInvokeHandlersBlock:nowDate:]_block_invoke.42
+ __95-[PPAdaptiveCoalescer coalesceRequestKey:handler:executeRequestAndInvokeHandlersBlock:nowDate:]_block_invoke.50
+ __Block_byref_object_copy_.1177
+ __Block_byref_object_copy_.1827
+ __Block_byref_object_copy_.2837
+ __Block_byref_object_copy_.3126
+ __Block_byref_object_copy_.3445
+ __Block_byref_object_copy_.3695
+ __Block_byref_object_copy_.371
+ __Block_byref_object_copy_.40
+ __Block_byref_object_copy_.4313
+ __Block_byref_object_copy_.4484
+ __Block_byref_object_copy_.4753
+ __Block_byref_object_copy_.493
+ __Block_byref_object_copy_.5373
+ __Block_byref_object_copy_.5444
+ __Block_byref_object_copy_.556
+ __Block_byref_object_copy_.5772
+ __Block_byref_object_copy_.6157
+ __Block_byref_object_copy_.6370
+ __Block_byref_object_copy_.6755
+ __Block_byref_object_copy_.7536
+ __Block_byref_object_dispose_.1178
+ __Block_byref_object_dispose_.1828
+ __Block_byref_object_dispose_.2838
+ __Block_byref_object_dispose_.3127
+ __Block_byref_object_dispose_.3446
+ __Block_byref_object_dispose_.3696
+ __Block_byref_object_dispose_.372
+ __Block_byref_object_dispose_.41
+ __Block_byref_object_dispose_.4314
+ __Block_byref_object_dispose_.4485
+ __Block_byref_object_dispose_.4754
+ __Block_byref_object_dispose_.494
+ __Block_byref_object_dispose_.5374
+ __Block_byref_object_dispose_.5445
+ __Block_byref_object_dispose_.557
+ __Block_byref_object_dispose_.5773
+ __Block_byref_object_dispose_.6158
+ __Block_byref_object_dispose_.6371
+ __Block_byref_object_dispose_.6756
+ __Block_byref_object_dispose_.7537
+ __EventKitLibraryCore_block_invoke.1604
+ __EventKitLibraryCore_block_invoke.6382
+ __block_literal_global.10
+ __block_literal_global.105
+ __block_literal_global.108
+ __block_literal_global.110
+ __block_literal_global.126
+ __block_literal_global.131
+ __block_literal_global.135
+ __block_literal_global.138
+ __block_literal_global.1386
+ __block_literal_global.139
+ __block_literal_global.142
+ __block_literal_global.146
+ __block_literal_global.15
+ __block_literal_global.153
+ __block_literal_global.1595
+ __block_literal_global.163
+ __block_literal_global.171
+ __block_literal_global.173
+ __block_literal_global.1752
+ __block_literal_global.178
+ __block_literal_global.178.6425
+ __block_literal_global.18
+ __block_literal_global.18.7469
+ __block_literal_global.1808
+ __block_literal_global.189
+ __block_literal_global.2025
+ __block_literal_global.204
+ __block_literal_global.206
+ __block_literal_global.207
+ __block_literal_global.208
+ __block_literal_global.209
+ __block_literal_global.21
+ __block_literal_global.218
+ __block_literal_global.226
+ __block_literal_global.231
+ __block_literal_global.231.8422
+ __block_literal_global.234
+ __block_literal_global.235
+ __block_literal_global.245
+ __block_literal_global.27
+ __block_literal_global.2711
+ __block_literal_global.2773
+ __block_literal_global.2835
+ __block_literal_global.296
+ __block_literal_global.298
+ __block_literal_global.30
+ __block_literal_global.30.7479
+ __block_literal_global.300
+ __block_literal_global.310
+ __block_literal_global.312
+ __block_literal_global.3135
+ __block_literal_global.33
+ __block_literal_global.332
+ __block_literal_global.34
+ __block_literal_global.3454
+ __block_literal_global.36
+ __block_literal_global.3778
+ __block_literal_global.380
+ __block_literal_global.382
+ __block_literal_global.384
+ __block_literal_global.39
+ __block_literal_global.4138
+ __block_literal_global.42
+ __block_literal_global.4482
+ __block_literal_global.45
+ __block_literal_global.4624
+ __block_literal_global.4755
+ __block_literal_global.48
+ __block_literal_global.500
+ __block_literal_global.51
+ __block_literal_global.54
+ __block_literal_global.5453
+ __block_literal_global.56
+ __block_literal_global.5684
+ __block_literal_global.608
+ __block_literal_global.6456
+ __block_literal_global.65.7503
+ __block_literal_global.6679
+ __block_literal_global.6803
+ __block_literal_global.69.7505
+ __block_literal_global.70
+ __block_literal_global.71.7544
+ __block_literal_global.7456
+ __block_literal_global.75
+ __block_literal_global.7543
+ __block_literal_global.7572
+ __block_literal_global.82
+ __block_literal_global.83
+ __block_literal_global.8343
+ __block_literal_global.8710
+ __block_literal_global.9
+ __block_literal_global.91
+ __block_literal_global.94
+ __block_literal_global.96
+ __block_literal_global.96.485
+ __block_literal_global.98
+ audit_stringEventKit.1616
+ audit_stringEventKit.6385
+ defaultStore._pasExprOnceResult.2409
+ defaultStore._pasExprOnceResult.9218
+ defaultStore._pasExprOnceResult.9587
+ defaultStore._pasOnceToken12.2408
+ defaultStore._pasOnceToken12.9586
+ featureNames._pasExprOnceResult.1753
+ featureNames._pasExprOnceResult.219
+ featureNames._pasExprOnceResult.228
+ featureNames._pasExprOnceResult.308
+ featureNames._pasExprOnceResult.377
+ featureNames._pasExprOnceResult.3776
+ featureNames._pasExprOnceResult.4137
+ featureNames._pasExprOnceResult.6680
+ featureNames._pasExprOnceResult.8344
+ featureNames._pasOnceToken4.1751
+ featureNames._pasOnceToken4.6678
+ featureNames._pasOnceToken6.8342
+ featureNames._pasOnceToken9.8421
+ sharedInstance._pasExprOnceResult.2900
+ sharedInstance._pasExprOnceResult.3469
+ sharedInstance._pasExprOnceResult.358
+ sharedInstance._pasExprOnceResult.411
+ sharedInstance._pasExprOnceResult.4391
+ sharedInstance._pasExprOnceResult.5127
+ sharedInstance._pasExprOnceResult.5200
+ sharedInstance._pasExprOnceResult.525
+ sharedInstance._pasExprOnceResult.5490
+ sharedInstance._pasExprOnceResult.6205
+ sharedInstance._pasExprOnceResult.6457
+ sharedInstance._pasExprOnceResult.6533
+ sharedInstance._pasExprOnceResult.6606
+ sharedInstance._pasExprOnceResult.7562
+ sharedInstance._pasOnceToken12.4390
+ sharedInstance._pasOnceToken12.5126
+ sharedInstance._pasOnceToken12.6455
+ sharedInstance._pasOnceToken2.3468
+ sharedInstance._pasOnceToken2.524
+ sharedInstance._pasOnceToken2.5489
+ sharedInstance._pasOnceToken2.7561
+ sharedInstance._pasOnceToken6.5199
+ sharedInstance._pasOnceToken6.6532
+ sharedInstance._pasOnceToken8.6204
+ sharedInstance._pasOnceToken8.6605
- EventKitLibraryCore.frameworkLibrary.1626
- EventKitLibraryCore.frameworkLibrary.6431
- __105-[PPConnectionsClient recentLocationsForConsumer:criteria:limit:explanationSet:client:error:handleBatch:]_block_invoke.93
- __20-[PPEvent attendees]_block_invoke.173
- __21-[PPEventClient init]_block_invoke.102
- __23-[PPContactClient init]_block_invoke.94
- __27-[PPConnectionsClient init]_block_invoke.73
- __29-[PPTopicReadOnlyClient init]_block_invoke.96
- __31-[PPSocialHighlightClient init]_block_invoke.81
- __31-[PPTemporalClusterClient init]_block_invoke.71
- __32-[PPEventStore _recordGenerator]_block_invoke.9
- __32-[PPLocationReadOnlyClient init]_block_invoke.74
- __34-[PPContactStore _recordGenerator]_block_invoke.21
- __35-[PPNamedEntityReadOnlyClient init]_block_invoke.76
- __38-[PPEventClient sendRTCLogsWithError:]_block_invoke.152
- __39-[PPReranker rerankedMediaItems:error:]_block_invoke.25
- __40-[PPConfigClient assetVersionWithError:]_block_invoke.67
- __40-[PPSocialHighlightClient decayInterval]_block_invoke.92
- __41+[PPUtils jaroSimilarityForString:other:]_block_invoke.47
- __41-[PPContactStore _sendChangesToDelegates]_block_invoke.29
- __46+[PPEvent deferredAllocationEventFromEKEvent:]_block_invoke.143
- __46+[PPEvent deferredAllocationEventFromEKEvent:]_block_invoke_2.145
- __46-[PPReranker _lazyLoadEntityRankMapWithError:]_block_invoke.11
- __48-[PPXPCClientHelper _locked_establishConnection]_block_invoke.3
- __50-[PPXPCNamedEntityStore _recordGeneratorForQuery:]_block_invoke.46
- __56-[PPTopicReadWriteClient _doSyncCallWithError:syncCall:]_block_invoke.80
- __57-[PPNamedEntityReadOnlyClient mapItemForPlaceName:error:]_block_invoke.104
- __58-[PPSocialHighlightClient attributionForIdentifier:error:]_block_invoke.114
- __59-[PPLocationReadWriteClient _doSyncCallWithError:syncCall:]_block_invoke.68
- __61-[PPContactClient rankedContactsWithQuery:error:handleBatch:]_block_invoke.108
- __61-[PPEventClient eventNameRecordsForClient:error:handleBatch:]_block_invoke.115
- __62-[PPNamedEntityReadWriteClient _doSyncCallWithError:syncCall:]_block_invoke.88
- __64-[PPEventClient interactionSummaryMetricsWithError:handleBatch:]_block_invoke.147
- __65-[PPTopicReadOnlyClient rankedTopicsWithQuery:error:handleBatch:]_block_invoke.121
- __66+[PPEvent convertBatchOfEKEvents:calendarInternPool:interningSet:]_block_invoke.151
- __66-[PPEventClient eventHighlightsFrom:to:options:error:handleBatch:]_block_invoke.134
- __66-[PPNotificationManager addMeCardChangeBlock:forLifetimeOfObject:]_block_invoke.157
- __66-[PPNotificationManager addMeCardChangeBlock:forLifetimeOfObject:]_block_invoke.161
- __66-[PPNotificationManager addMeCardChangeBlock:forLifetimeOfObject:]_block_invoke_2.162
- __66-[PPNotificationManager addMeCardChangeBlock:forLifetimeOfObject:]_block_invoke_3.163
- __68-[PPNotificationManager addContactsChangeBlock:forLifetimeOfObject:]_block_invoke.145
- __68-[PPNotificationManager addEventKitChangeBlock:forLifetimeOfObject:]_block_invoke.194
- __68-[PPNotificationManager addEventKitChangeBlock:forLifetimeOfObject:]_block_invoke.196
- __68-[PPNotificationManager addEventKitChangeBlock:forLifetimeOfObject:]_block_invoke.197
- __68-[PPNotificationManager addEventKitChangeBlock:forLifetimeOfObject:]_block_invoke.217
- __68-[PPNotificationManager addPortraitChangeBlock:forLifetimeOfObject:]_block_invoke.170
- __69-[PPInternalClient trialOverridePath:namespaceName:factorName:error:]_block_invoke.106
- __71-[PPLocationReadOnlyClient rankedLocationsWithQuery:error:handleBatch:]_block_invoke.94
- __71-[PPNotificationManager addSuggestionsChangeBlock:forLifetimeOfObject:]_block_invoke.237
- __71-[PPTopicReadOnlyClient scoresForTopicMapping:query:error:handleBatch:]_block_invoke.134
- __72-[PPEventClient resolveEventNameRecordChanges:client:error:handleBatch:]_block_invoke.125
- __74-[PPNotificationManager addPortraitInvalidationBlock:forLifetimeOfObject:]_block_invoke.181
- __74-[PPNotificationManager addPortraitInvalidationBlock:forLifetimeOfObject:]_block_invoke.184
- __75+[PPCustomDonation donateLabeledStrings:bundleId:groupId:documentId:error:]_block_invoke.108
- __76-[PPTopicReadOnlyClient unmapMappedTopicIdentifier:mappingIdentifier:error:]_block_invoke.151
- __77-[PPRecordMonitoringHelper _setupRecentChangesWithDelegates:recordGenerator:]_block_invoke.7
- __78-[PPNamedEntityReadOnlyClient rankedNamedEntitiesWithQuery:error:handleBatch:]_block_invoke.96
- __78-[PPNotificationManager addCalendarVisibilityChangeBlock:forLifetimeOfObject:]_block_invoke.231
- __81-[PPConnectionsClient recentLocationDonationsSinceDate:client:error:handleBatch:]_block_invoke.87
- __86-[PPSocialHighlightClient rankedHighlightsWithLimit:client:variant:error:handleBatch:]_block_invoke.99
- __88-[PPTemporalClusterClient rankedTemporalClustersForStartDate:endDate:error:handleBatch:]_block_invoke.85
- __89-[PPXPCNamedEntityStore loadNamedEntityRecordsAndMonitorChangesWithDelegate:query:error:]_block_invoke.57
- __91-[PPSocialHighlightClient rankedHighlightsForSyncedItems:client:variant:error:handleBatch:]_block_invoke.108
- __94-[PPRecordMonitoringHelper _handleRecentChangesWithDelegates:changeGenerator:recordGenerator:]_block_invoke.10
- __94-[PPRecordMonitoringHelper _handleRecentChangesWithDelegates:changeGenerator:recordGenerator:]_block_invoke.9
- __95+[PPCustomDonation donateParsecNamedEntitiesAndTopics:rawQuery:reformulatedQuery:source:error:]_block_invoke.96
- __95-[PPAdaptiveCoalescer coalesceRequestKey:handler:executeRequestAndInvokeHandlersBlock:nowDate:]_block_invoke.36
- __95-[PPAdaptiveCoalescer coalesceRequestKey:handler:executeRequestAndInvokeHandlersBlock:nowDate:]_block_invoke.44
- __Block_byref_object_copy_.1192
- __Block_byref_object_copy_.1855
- __Block_byref_object_copy_.2868
- __Block_byref_object_copy_.3159
- __Block_byref_object_copy_.34
- __Block_byref_object_copy_.3484
- __Block_byref_object_copy_.3737
- __Block_byref_object_copy_.395
- __Block_byref_object_copy_.4355
- __Block_byref_object_copy_.4526
- __Block_byref_object_copy_.4794
- __Block_byref_object_copy_.514
- __Block_byref_object_copy_.5414
- __Block_byref_object_copy_.5486
- __Block_byref_object_copy_.577
- __Block_byref_object_copy_.5814
- __Block_byref_object_copy_.6203
- __Block_byref_object_copy_.6420
- __Block_byref_object_copy_.6805
- __Block_byref_object_copy_.7584
- __Block_byref_object_dispose_.1193
- __Block_byref_object_dispose_.1856
- __Block_byref_object_dispose_.2869
- __Block_byref_object_dispose_.3160
- __Block_byref_object_dispose_.3485
- __Block_byref_object_dispose_.35
- __Block_byref_object_dispose_.3738
- __Block_byref_object_dispose_.396
- __Block_byref_object_dispose_.4356
- __Block_byref_object_dispose_.4527
- __Block_byref_object_dispose_.4795
- __Block_byref_object_dispose_.515
- __Block_byref_object_dispose_.5415
- __Block_byref_object_dispose_.5487
- __Block_byref_object_dispose_.578
- __Block_byref_object_dispose_.5815
- __Block_byref_object_dispose_.6204
- __Block_byref_object_dispose_.6421
- __Block_byref_object_dispose_.6806
- __Block_byref_object_dispose_.7585
- __EventKitLibraryCore_block_invoke.1627
- __EventKitLibraryCore_block_invoke.6432
- __block_literal_global.102
- __block_literal_global.104
- __block_literal_global.11
- __block_literal_global.120
- __block_literal_global.123
- __block_literal_global.125
- __block_literal_global.133
- __block_literal_global.136
- __block_literal_global.14
- __block_literal_global.140
- __block_literal_global.1405
- __block_literal_global.141
- __block_literal_global.156
- __block_literal_global.157
- __block_literal_global.159
- __block_literal_global.1617
- __block_literal_global.167
- __block_literal_global.17
- __block_literal_global.172
- __block_literal_global.1776
- __block_literal_global.183
- __block_literal_global.1833
- __block_literal_global.196
- __block_literal_global.198
- __block_literal_global.20
- __block_literal_global.200
- __block_literal_global.201
- __block_literal_global.202
- __block_literal_global.203
- __block_literal_global.2053
- __block_literal_global.220
- __block_literal_global.225
- __block_literal_global.225.8467
- __block_literal_global.227
- __block_literal_global.228
- __block_literal_global.229
- __block_literal_global.23
- __block_literal_global.236
- __block_literal_global.26
- __block_literal_global.2742
- __block_literal_global.28
- __block_literal_global.2804
- __block_literal_global.2866
- __block_literal_global.29
- __block_literal_global.290
- __block_literal_global.292
- __block_literal_global.294
- __block_literal_global.304
- __block_literal_global.306
- __block_literal_global.3168
- __block_literal_global.32
- __block_literal_global.3493
- __block_literal_global.35
- __block_literal_global.353
- __block_literal_global.374
- __block_literal_global.376
- __block_literal_global.378
- __block_literal_global.38
- __block_literal_global.3820
- __block_literal_global.41
- __block_literal_global.4180
- __block_literal_global.44
- __block_literal_global.4524
- __block_literal_global.4667
- __block_literal_global.47
- __block_literal_global.4796
- __block_literal_global.5
- __block_literal_global.50
- __block_literal_global.52
- __block_literal_global.521
- __block_literal_global.5495
- __block_literal_global.55
- __block_literal_global.57
- __block_literal_global.5726
- __block_literal_global.59.7547
- __block_literal_global.6
- __block_literal_global.628
- __block_literal_global.63.7551
- __block_literal_global.64
- __block_literal_global.65.7592
- __block_literal_global.6505
- __block_literal_global.6728
- __block_literal_global.6853
- __block_literal_global.73.7579
- __block_literal_global.7505
- __block_literal_global.7591
- __block_literal_global.76
- __block_literal_global.7620
- __block_literal_global.8
- __block_literal_global.8389
- __block_literal_global.8753
- __block_literal_global.88
- __block_literal_global.90
- __block_literal_global.90.506
- __block_literal_global.92
- __block_literal_global.93
- audit_stringEventKit.1639
- audit_stringEventKit.6435
- defaultStore._pasExprOnceResult.2441
- defaultStore._pasExprOnceResult.9261
- defaultStore._pasExprOnceResult.9629
- defaultStore._pasOnceToken12.2440
- defaultStore._pasOnceToken12.9628
- featureNames._pasExprOnceResult.1777
- featureNames._pasExprOnceResult.222
- featureNames._pasExprOnceResult.237
- featureNames._pasExprOnceResult.302
- featureNames._pasExprOnceResult.371
- featureNames._pasExprOnceResult.3818
- featureNames._pasExprOnceResult.4179
- featureNames._pasExprOnceResult.6729
- featureNames._pasExprOnceResult.8390
- featureNames._pasOnceToken4.1775
- featureNames._pasOnceToken4.6727
- featureNames._pasOnceToken6.8388
- featureNames._pasOnceToken9.8466
- sharedInstance._pasExprOnceResult.2931
- sharedInstance._pasExprOnceResult.3508
- sharedInstance._pasExprOnceResult.380
- sharedInstance._pasExprOnceResult.435
- sharedInstance._pasExprOnceResult.4433
- sharedInstance._pasExprOnceResult.5168
- sharedInstance._pasExprOnceResult.5241
- sharedInstance._pasExprOnceResult.546
- sharedInstance._pasExprOnceResult.5532
- sharedInstance._pasExprOnceResult.6251
- sharedInstance._pasExprOnceResult.6506
- sharedInstance._pasExprOnceResult.6582
- sharedInstance._pasExprOnceResult.6655
- sharedInstance._pasExprOnceResult.7610
- sharedInstance._pasOnceToken12.4432
- sharedInstance._pasOnceToken12.5167
- sharedInstance._pasOnceToken12.6504
- sharedInstance._pasOnceToken2.3507
- sharedInstance._pasOnceToken2.545
- sharedInstance._pasOnceToken2.5531
- sharedInstance._pasOnceToken2.7609
- sharedInstance._pasOnceToken6.5240
- sharedInstance._pasOnceToken6.6581
- sharedInstance._pasOnceToken8.6250
- sharedInstance._pasOnceToken8.6654
Functions:
~ -[PPTopicReadOnlyClient init] : 1056 -> 1044
~ -[PPXPCClientHelper remoteObjectProxy] : 100 -> 96
~ -[PPXPCClientHelper _locked_establishConnection] : 584 -> 572
~ -[PPScoredItem initWithCoder:] : 284 -> 288
~ -[PPSource initWithCoder:] : 720 -> 728
~ -[PPSourceMetadata initWithCoder:] : 276 -> 280
~ ___PPGetStringInternPool_block_invoke : 168 -> 172
~ -[PPTopicMetadata initWithCoder:] : 252 -> 256
~ -[PPSource isEqualToSource:] : 768 -> 780
~ -[PPXPCClientPipelinedBatchQueryManager handleReplyWithName:batch:isLast:error:queryId:completion:] : 784 -> 768
~ ___99-[PPXPCClientPipelinedBatchQueryManager handleReplyWithName:batch:isLast:error:queryId:completion:]_block_invoke : 156 -> 160
~ -[PPXPCClientHelper synchronousRemoteObjectProxyWithErrorHandler:] : 132 -> 128
~ -[PPNamedEntityReadOnlyClient init] : 820 -> 808
~ -[PPNamedEntity initWithCoder:] : 360 -> 364
~ -[PPNamedEntityMetadata initWithCoder:] : 156 -> 160
~ -[PPUniversalSearchSpotlightFeedback isEqualToPPUniversalSearchSpotlightFeedback:] : 324 -> 276
~ -[PPUniversalSearchSpotlightFeedback initWithCoder:] : 1008 -> 1012
~ -[PPQuickTypeQuery isResultEquivelentToQuickTypeQuery:] : 532 -> 444
~ -[PPQuickTypeQuery isEqualToQuickTypeQuery:] : 244 -> 216
~ -[PPQuickTypeQuery initWithCoder:] : 764 -> 760
~ -[PPQuickTypeQuery initWithType:subtype:semanticTag:fields:time:options:subFields:label:people:localeIdentifier:bundleIdentifier:recipients:timeoutSeconds:] : 412 -> 400
~ -[PPNamedEntityRecord isEqualToNamedEntityRecord:] : 484 -> 396
~ -[PPEventClient init] : 1108 -> 1096
~ -[PPFuzzyContactQuery isEqualToFuzzyContactQuery:] : 336 -> 268
~ -[PPTopicReadWriteClient _doDeletionSyncCallWithError:deletedCount:syncCall:] : 708 -> 700
~ -[PPTopicReadWriteClient _doSyncCallWithError:syncCall:] : 636 -> 628
~ -[PPCalendar isEqualToCalendar:] : 272 -> 224
~ -[PPCalendar initWithCoder:] : 248 -> 252
~ -[PPLocationQuery customizedDescription] : 1560 -> 1568
~ -[PPLocationQuery description] : 432 -> 428
~ -[PPLocationQuery isEqualToLocationQuery:] : 1004 -> 1024
~ -[PPScoredLabeledValue isEqualToScoredLabeledValue:] : 196 -> 168
~ -[PPScoredContact isEqualToScoredContact:] : 516 -> 408
~ -[PPScoredContact initWithCoder:] : 520 -> 524
~ -[PPScoredContact compare:] : 516 -> 520
~ -[PPXPCNamedEntityStore loadNamedEntityRecordsAndMonitorChangesWithDelegate:query:error:] : 372 -> 364
~ ___89-[PPXPCNamedEntityStore loadNamedEntityRecordsAndMonitorChangesWithDelegate:query:error:]_block_invoke : 388 -> 368
~ -[PPXPCNamedEntityStore _sendChangesToDelegatesForQuery:] : 320 -> 312
~ ___57-[PPXPCNamedEntityStore _sendChangesToDelegatesForQuery:]_block_invoke : 560 -> 556
~ -[PPXPCNamedEntityStore _recordGeneratorForQuery:] : 240 -> 232
~ -[PPAttendee initWithCoder:] : 468 -> 472
~ -[PPAttendee initWithEKParticipant:] : 268 -> 272
~ -[PPAttendee initWithName:emailAddress:urlString:isCurrentUser:status:] : 704 -> 712
~ -[PPEvent isEqual:] : 752 -> 732
~ -[PPEvent initWithCoder:] : 1188 -> 1192
~ _getEKObjectIDClass : 228 -> 224
~ -[PPEvent initWithEventIdentifier:objectID:title:location:calendar:startDate:endDate:availability:externalURIString:attendees:organizerName:eventFlags:notes:urlString:structuredLocationTitle:structuredLocationAddress:structuredLocationCoordinates:suggestedEventCategory:] : 2040 -> 2056
~ -[PPLabeledValue isEqualToLabeledValue:] : 212 -> 184
~ -[PPLabeledValue initWithCoder:] : 304 -> 308
~ -[PPSocialCollaboration initWithCoder:] : 1416 -> 1420
~ -[PPSocialCollaboration initWithIdentifier:resourceURL:timestamp:attributionIdentifiers:supplementaryData:collaborationIdentifier:contentDisplayName:contentCreationDate:contentUTIType:fileProviderId:earliestAttributionIdentifiers:localIdentity:localIdentityProof:handleToIdentityMap:score:] : 688 -> 684
~ _PPNewEKEventStore : 256 -> 252
~ -[PPAdaptiveCoalescer coalesceRequestKey:handler:executeRequestAndInvokeHandlersBlock:nowDate:] : 696 -> 700
~ -[PPConnectionsLocation isEqualToConnectionsLocation:] : 2028 -> 1540
~ -[PPConnectionsLocation addressDictionary] : 448 -> 444
~ -[PPTopicQuery customizedDescription] : 1744 -> 1760
~ -[PPTopicQuery description] : 428 -> 424
~ -[PPTopicQuery isEqualToTopicQuery:] : 1120 -> 1144
~ -[PPTemporalCluster initWithCoder:] : 1916 -> 1904
~ -[PPTemporalCluster initWithEvent:startDate:endDate:score:topics:entities:locations:contacts:contactHandles:mediaItems:] : 448 -> 456
~ -[PPContactNameRecordChangeResult isEqualToContactNameRecordChangeResult:] : 176 -> 148
~ +[PPUtils sqliteGlobEscape:] : 844 -> 836
~ +[PPUtils coordinatesToGeoHashWithLength:latitude:longitude:] : 456 -> 452
~ +[PPUtils Sha256ForData:withSalt:] : 324 -> 316
~ +[PPUtils enumerateChunksOfSize:fromArray:usingBlock:] : 380 -> 384
~ _PPIsServerContext : 68 -> 72
~ -[PPSocialHighlightClient init] : 712 -> 700
~ -[PPEventNameRecord isEqualToEventNameRecord:] : 404 -> 336
~ -[PPEventNameRecord initWithCoder:] : 640 -> 644
~ -[PPContactStore loadContactNameRecordsAndMonitorChangesWithDelegate:error:] : 280 -> 272
~ ___76-[PPContactStore loadContactNameRecordsAndMonitorChangesWithDelegate:error:]_block_invoke : 208 -> 204
~ -[PPSocialAttribution initWithCoder:] : 1432 -> 1436
~ ___94-[PPRecordMonitoringHelper _handleRecentChangesWithDelegates:changeGenerator:recordGenerator:]_block_invoke : 1208 -> 1184
~ ___77-[PPRecordMonitoringHelper _setupRecentChangesWithDelegates:recordGenerator:]_block_invoke : 576 -> 556
~ -[PPRecordMonitoringHelper loadRecordsAndMonitorChangesWithDelegate:recordGenerator:notificationRegistrationBlock:] : 332 -> 324
~ +[PPSentimentScoreEncoder encodeSentimentScore:] : 52 -> 40
~ -[PPScoredContactHandle isEqualToScoredContactHandle:] : 176 -> 148
~ -[PPScoredContactHandle initWithCoder:] : 252 -> 256
~ -[PPLocation isEqualToLocation:] : 980 -> 996
~ -[PPLocation initWithCoder:] : 252 -> 256
~ -[PPLocationRecord isEqualToLocationRecord:] : 476 -> 484
~ -[PPMutableLocationRecord setSentimentScore:] : 56 -> 44
~ +[PPLocationRecord describeAlgorithm:] : 152 -> 148
~ ___18-[PPSource sha256]_block_invoke : 268 -> 260
~ __71-[PPTopicReadOnlyClient scoresForTopicMapping:query:error:handleBatch:]_block_invoke.134 -> __71-[PPTopicReadOnlyClient scoresForTopicMapping:query:error:handleBatch:]_block_invoke.140 : 524 -> 528
~ -[PPEventStore loadEventNameRecordsAndMonitorChangesWithDelegate:error:] : 280 -> 272
~ ___72-[PPEventStore loadEventNameRecordsAndMonitorChangesWithDelegate:error:]_block_invoke : 204 -> 200
~ ___32-[PPEventStore _recordGenerator]_block_invoke : 560 -> 556
~ -[PPSpotlightScoringFeatureVector encodeAsData] : 476 -> 472
~ +[PPSpotlightScoringFeatureVector decodeFeatureVectorFromData:version:] : 1256 -> 1252
~ __48-[PPXPCClientHelper _locked_establishConnection]_block_invoke.3 -> __48-[PPXPCClientHelper _locked_establishConnection]_block_invoke.7 : 244 -> 240
~ -[PPQuickTypeItem compare:] : 356 -> 360
~ -[PPQuickTypeItem isEqualToQuickTypeItem:] : 712 -> 584
~ -[PPQuickTypeItem initWithCoder:] : 784 -> 788
~ -[PPQuickTypeItem initWithLabel:value:name:date:fields:originatingBundleID:originatingWebsiteURL:predictionAge:shouldAggregate:flags:score:source:sourceIdentifier:] : 492 -> 460
~ -[PPContactClient init] : 1032 -> 1020
~ -[PPConnectionsClient init] : 712 -> 700
~ -[PPSocialPerson initWithCoder:] : 364 -> 368
~ ___46-[PPReranker _lazyLoadEntityRankMapWithError:]_block_invoke : 604 -> 592
~ -[PPNamedEntityReadWriteClient flushDonationsWithError:] : 332 -> 328
~ -[PPNamedEntityReadWriteClient _doDeletionSyncCallWithError:deletedCount:syncCall:] : 708 -> 700
~ -[PPNamedEntityReadWriteClient _doSyncCallWithError:syncCall:] : 636 -> 628
~ -[PPScoredLocation initWithCoder:] : 220 -> 224
~ -[PPSocialHighlightStore iterRankedHighlightsForSyncedItems:client:variant:error:block:] : 312 -> 320
~ -[PPQuickTypeExplanationSet isEqualToQuickTypeExplanationSet:] : 508 -> 500
~ ___41-[PPNotificationHandler fireWithObjects:]_block_invoke : 728 -> 732
~ -[PPNotificationHandler _delayedExecutionAfterSeconds:] : 236 -> 228
~ -[PPNotificationManagerGuardedData description] : 400 -> 396
~ ___71-[PPNotificationManager addSuggestionsChangeBlock:forLifetimeOfObject:]_block_invoke : 564 -> 556
~ __71-[PPNotificationManager addSuggestionsChangeBlock:forLifetimeOfObject:]_block_invoke.237 -> __71-[PPNotificationManager addSuggestionsChangeBlock:forLifetimeOfObject:]_block_invoke.243 : 180 -> 176
~ ___78-[PPNotificationManager addCalendarVisibilityChangeBlock:forLifetimeOfObject:]_block_invoke : 656 -> 644
~ ___68-[PPNotificationManager addEventKitChangeBlock:forLifetimeOfObject:]_block_invoke : 920 -> 916
~ __68-[PPNotificationManager addEventKitChangeBlock:forLifetimeOfObject:]_block_invoke.194 -> __68-[PPNotificationManager addEventKitChangeBlock:forLifetimeOfObject:]_block_invoke.200 : 276 -> 268
~ ___68-[PPNotificationManager addEventKitChangeBlock:forLifetimeOfObject:]_block_invoke_2 : 1176 -> 1168
~ __68-[PPNotificationManager addEventKitChangeBlock:forLifetimeOfObject:]_block_invoke.196 -> __68-[PPNotificationManager addEventKitChangeBlock:forLifetimeOfObject:]_block_invoke.202 : 764 -> 768
~ -[PPNotificationManager fetchObjectChangesFromStore:usingBlock:] : 540 -> 536
~ ___74-[PPNotificationManager addPortraitInvalidationBlock:forLifetimeOfObject:]_block_invoke : 596 -> 588
~ ___68-[PPNotificationManager addPortraitChangeBlock:forLifetimeOfObject:]_block_invoke : 596 -> 588
~ ___66-[PPNotificationManager addMeCardChangeBlock:forLifetimeOfObject:]_block_invoke : 868 -> 848
~ __66-[PPNotificationManager addMeCardChangeBlock:forLifetimeOfObject:]_block_invoke.157 -> __66-[PPNotificationManager addMeCardChangeBlock:forLifetimeOfObject:]_block_invoke.163 : 180 -> 176
~ __66-[PPNotificationManager addMeCardChangeBlock:forLifetimeOfObject:]_block_invoke.161 -> __66-[PPNotificationManager addMeCardChangeBlock:forLifetimeOfObject:]_block_invoke.167 : 180 -> 176
~ ___68-[PPNotificationManager addContactsChangeBlock:forLifetimeOfObject:]_block_invoke : 584 -> 576
~ __68-[PPNotificationManager addContactsChangeBlock:forLifetimeOfObject:]_block_invoke.145 -> __68-[PPNotificationManager addContactsChangeBlock:forLifetimeOfObject:]_block_invoke.151 : 180 -> 176
~ +[PPNotificationManager _changePotentiallyAffectsCache:] : 1140 -> 1116
~ -[PPNotificationHandler(TestHelpers) waitOnQueueToDrain] : 312 -> 316
~ -[PPTemporalClusterClient init] : 824 -> 812
~ -[PPLocationReadOnlyClient init] : 820 -> 808
~ +[PPCustomDonation donateParsecNamedEntitiesAndTopics:rawQuery:reformulatedQuery:source:error:] : 1452 -> 1440
~ -[PPSocialHighlight initWithCoder:] : 996 -> 1000
~ -[PPEventHighlight isEqualToEventHighlight:] : 796 -> 648
~ -[PPEventHighlight copyWithZone:] : 324 -> 320
~ -[PPEventHighlight initWithCoder:] : 876 -> 880
~ -[PPSyncedSocialHighlight initWithCoder:] : 472 -> 476
~ -[PPLocationReadWriteClient _doDeletionSyncCallWithError:deletedCount:syncCall:] : 708 -> 700
~ -[PPLocationReadWriteClient _doSyncCallWithError:syncCall:] : 636 -> 628
~ _PPCollapseWhitespaceAndStrip : 1108 -> 1100
~ _PPStringIsWellFormed : 188 -> 184
~ _PPStringLooksLikeNumber : 484 -> 468
~ -[PPBaseFeedback isEqualToPPBaseFeedback:] : 452 -> 364
~ -[PPBaseFeedback initWithCoder:] : 472 -> 476
~ -[PPClientContactNameRecord initWithIdentifier:score:source:sourceIdentifier:changeType:firstName:phoneticFirstName:middleName:phoneticMiddleName:lastName:phoneticLastName:organizationName:jobTitle:nickname:relatedNames:streetNames:cityNames:] : 828 -> 824
~ -[PPContact isEqualToContact:] : 1348 -> 1040
~ -[PPContact initWithCoder:] : 1036 -> 1040
~ -[PPContact initWithFoundInAppsContact:] : 1796 -> 1792
~ -[PPContact initWithContactsContact:] : 2880 -> 2864
~ -[PPContact initWithIdentifier:source:namePrefix:givenName:middleName:familyName:nameSuffix:nickname:localizedFullName:organizationName:jobTitle:birthday:nonGregorianBirthday:phoneNumbers:emailAddresses:socialProfiles:postalAddresses:] : 860 -> 848
~ -[PPFeedbackItem isEqualToPPFeedbackItem:] : 176 -> 148
~ -[PPFeedbackItem initWithCoder:] : 204 -> 208
~ -[PPScoredEvent initWithCoder:] : 320 -> 324
~ -[PPTripPart initWithCoder:] : 512 -> 516
~ -[PPTopicRecord isEqualToTopicRecord:] : 472 -> 404
~ -[PPPostalAddress isEqualToPostalAddress:] : 692 -> 544
~ -[PPPostalAddress initWithThoroughfare:subThoroughfare:locality:subLocality:administrativeArea:subAdministrativeArea:postalCode:country:] : 396 -> 400
~ -[PPContactQuery isEqualToContactQuery:] : 672 -> 524
~ -[PPContactQuery description] : 168 -> 164
~ -[PPContactNameRecord initWithCoder:] : 1208 -> 1228
~ -[PPNotification isEqualToNotification:] : 524 -> 528
~ -[PPNotification initWithCoder:] : 488 -> 492
~ -[PPNamedEntityQuery customizedDescription] : 1716 -> 1736
~ -[PPNamedEntityQuery description] : 464 -> 456
~ -[PPNamedEntityQuery isEqualToNamedEntityQuery:] : 1404 -> 1420

```
