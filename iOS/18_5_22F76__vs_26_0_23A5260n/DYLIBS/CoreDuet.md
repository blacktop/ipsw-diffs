## CoreDuet

> `/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet`

```diff

-1892.22.0.0.0
-  __TEXT.__text: 0x195e7c
+1917.0.1.0.0
+  __TEXT.__text: 0x19be50
   __TEXT.__auth_stubs: 0x14e0
-  __TEXT.__objc_methlist: 0x119b4
-  __TEXT.__cstring: 0x160c7
-  __TEXT.__const: 0x5b8
-  __TEXT.__oslogstring: 0x185d4
-  __TEXT.__gcc_except_tab: 0x7fbc
+  __TEXT.__objc_methlist: 0x11a4c
+  __TEXT.__cstring: 0x161a9
+  __TEXT.__const: 0x5a8
+  __TEXT.__oslogstring: 0x18869
+  __TEXT.__gcc_except_tab: 0x8000
   __TEXT.__dlopen_cstrs: 0xb6
-  __TEXT.__unwind_info: 0x55c0
-  __TEXT.__objc_classname: 0x2c51
-  __TEXT.__objc_methname: 0x26717
-  __TEXT.__objc_methtype: 0x6239
-  __TEXT.__objc_stubs: 0x17400
-  __DATA_CONST.__got: 0x1190
-  __DATA_CONST.__const: 0x3d20
-  __DATA_CONST.__objc_classlist: 0xc30
+  __TEXT.__unwind_info: 0x54e8
+  __TEXT.__objc_classname: 0x2c66
+  __TEXT.__objc_methname: 0x268e8
+  __TEXT.__objc_methtype: 0x61e7
+  __TEXT.__objc_stubs: 0x176a0
+  __DATA_CONST.__got: 0x11a0
+  __DATA_CONST.__const: 0x3da0
+  __DATA_CONST.__objc_classlist: 0xc38
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x81b0
+  __DATA_CONST.__objc_selrefs: 0x8258
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x6a8
-  __DATA_CONST.__objc_arraydata: 0x738
+  __DATA_CONST.__objc_arraydata: 0x7e8
   __AUTH_CONST.__auth_got: 0xa80
-  __AUTH_CONST.__const: 0x1e00
-  __AUTH_CONST.__cfstring: 0x13360
-  __AUTH_CONST.__objc_const: 0x232a0
+  __AUTH_CONST.__const: 0x1f20
+  __AUTH_CONST.__cfstring: 0x13480
+  __AUTH_CONST.__objc_const: 0x23368
   __AUTH_CONST.__objc_intobj: 0x2400
   __AUTH_CONST.__objc_doubleobj: 0x50
-  __AUTH_CONST.__objc_arrayobj: 0x660
+  __AUTH_CONST.__objc_arrayobj: 0x6d8
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x4b50
-  __DATA.__objc_ivar: 0x17e0
+  __AUTH.__objc_data: 0x4ba0
+  __DATA.__objc_ivar: 0x17e8
   __DATA.__data: 0x19e0
-  __DATA.__bss: 0xbb8
+  __DATA.__bss: 0xc10
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x2e90
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D8D650FF-9A08-31A6-BE39-F858D9DE4A0C
-  Functions: 8802
-  Symbols:   28004
-  CStrings:  14390
+  UUID: A116C5EF-3E4B-3603-AA66-89D3477DAA28
+  Functions: 8808
+  Symbols:   27951
+  CStrings:  14445
 
Symbols:
+ +[_CDDecommissionUtils allowedStreams]
+ +[_CDDecommissionUtils allowedStreams].cold.1
+ +[_CDDecommissionUtils filterEvents:]
+ +[_CDDecommissionUtils isCompletelyDisabled]
+ +[_CDDecommissionUtils isCoreDuetProcess]
+ +[_CDDecommissionUtils isCoreDuetProcess].cold.1
+ +[_CDDecommissionUtils isDigitalHealthProcess]
+ +[_CDDecommissionUtils isDigitalHealthProcess].cold.1
+ +[_CDDecommissionUtils isDigitalHealthSyncDisabled]
+ +[_CDDecommissionUtils isKnowledgeDaemon]
+ +[_CDDecommissionUtils isKnowledgeDaemon].cold.1
+ +[_CDDecommissionUtils isRequestAllowed:]
+ +[_CDDecommissionUtils isRequestAllowed:].cold.1
+ +[_CDDecommissionUtils knowledgeStoreDisabledError]
+ +[_CDDecommissionUtils logFault]
+ +[_CDDecommissionUtils logFault].cold.1
+ +[_CDLogging psBackgroundProcessingChannel]
+ +[_CDLogging psBackgroundProcessingChannel].cold.1
+ -[_CDContactStatistics hash]
+ -[_CDContactStatistics isEqual:]
+ -[_CDContactStatistics isEqualToContactStatistics:]
+ -[_CDInteractionsStatistics computeSASSFeatureWithSceneCategoriesDetectedInPhoto:andConfiguredSceneCategoryTags:]
+ -[_CDInteractionsStatistics removeFeature:andConversation:]
+ -[_CDInteractionsStatisticsConfig computeConversationGroupNameForConversationId:interactionRecord:inInteractionsStatistics:]
+ -[_CDInteractionsStatisticsConfig computeConversationINImageURLForConversationId:interactionRecord:inInteractionsStatistics:]
+ -[_CDInteractionsStatisticsConfig configuredSceneCategoryTagNames]
+ -[_CDInteractionsStatisticsConfig detectedSceneCategoryNamesFromSceneNetTags:]
+ -[_CDInteractionsStatisticsConfig sceneTagsInPhotoIdentifiers]
+ -[_CDInteractionsStatisticsConfig setSceneTagsInPhotoIdentifiers:]
+ -[_CDReceiverNotifier handleXPCNotificationEvent:].cold.9
+ -[_CDReceiverNotifier publishXPCEventForRelevantShortcuts:bundleID:uid:]
+ -[_CDReceiverNotifier publishXPCEventForRelevantShortcuts:bundleID:uid:].cold.1
+ -[_CDReceiverNotifier publishXPCEventForRelevantShortcuts:bundleID:uid:].cold.2
+ GCC_except_table169
+ GCC_except_table302
+ GCC_except_table307
+ GCC_except_table310
+ GCC_except_table313
+ GCC_except_table316
+ GCC_except_table319
+ GCC_except_table322
+ GCC_except_table325
+ GCC_except_table331
+ GCC_except_table334
+ GCC_except_table337
+ GCC_except_table343
+ GCC_except_table346
+ GCC_except_table352
+ GCC_except_table358
+ GCC_except_table361
+ GCC_except_table364
+ GCC_except_table367
+ GCC_except_table373
+ GCC_except_table379
+ GCC_except_table384
+ GCC_except_table390
+ GCC_except_table449
+ GCC_except_table452
+ GCC_except_table455
+ GCC_except_table458
+ GCC_except_table461
+ GCC_except_table464
+ GCC_except_table467
+ GCC_except_table470
+ GCC_except_table473
+ GCC_except_table482
+ GCC_except_table485
+ _OBJC_CLASS_$_BMAppRelevantShortcuts
+ _OBJC_CLASS_$__CDDecommissionUtils
+ _OBJC_IVAR_$__CDInteractionsStatisticsConfig._sceneTagsInPhotoIdentifiers
+ _OBJC_IVAR_$__CDReceiverNotifier._relevantShortcutsStream
+ _OBJC_IVAR_$__CDSpotlightItemRecorder._relevantShortcutsStream
+ _OBJC_METACLASS_$__CDDecommissionUtils
+ __CDAppRelevantShortcutsBundleIDKey
+ __CDAppRelevantShortcutsKey
+ __CDCurrentProcessName
+ __OBJC_$_CLASS_METHODS__CDDecommissionUtils
+ __OBJC_CLASS_RO_$__CDDecommissionUtils
+ __OBJC_METACLASS_RO_$__CDDecommissionUtils
+ ___100-[_CDInteractionStore queryInteractionsUsingPredicate:sortDescriptors:limit:offset:objectIDs:error:]_block_invoke.379
+ ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.725
+ ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.733
+ ___116-[_CDInteractionsStatisticsConfig computePhotoFeaturesForConversationId:interactionRecord:inInteractionsStatistics:]_block_invoke
+ ___122-[_CDInteractionsStatisticsConfig computeScenesBasedFeaturesForConversationId:interactionRecord:inInteractionsStatistics:]_block_invoke
+ ___144-[_CDInteractionsStatisticsConfig computeNumberOfEngagedSuggestionsOfPhotoFeaturesForConversationId:interactionRecord:inInteractionsStatistics:]_block_invoke
+ ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.1134
+ ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.1134.cold.1
+ ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.1139
+ ___31-[_CDInteractionCache _refetch]_block_invoke.260
+ ___31-[_CDInteractionCache _refetch]_block_invoke.260.cold.1
+ ___37+[_CDDecommissionUtils filterEvents:]_block_invoke
+ ___38+[_CDDecommissionUtils allowedStreams]_block_invoke
+ ___41+[_CDDecommissionUtils isCoreDuetProcess]_block_invoke
+ ___41+[_CDDecommissionUtils isKnowledgeDaemon]_block_invoke
+ ___41-[_CDInteractionStore metadataDictionary]_block_invoke.481
+ ___43+[_CDLogging psBackgroundProcessingChannel]_block_invoke
+ ___43+[_CDLogging psBackgroundProcessingChannel]_block_invoke.cold.1
+ ___46+[_CDDecommissionUtils isDigitalHealthProcess]_block_invoke
+ ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1200
+ ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1200.cold.1
+ ___50-[_CDReceiverNotifier handleXPCNotificationEvent:]_block_invoke
+ ___53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.299
+ ___53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.332
+ ___58-[_CDInteractionStore getInteractionsStatisticsForConfig:]_block_invoke.461
+ ___58-[_CDInteractionStore getInteractionsStatisticsForConfig:]_block_invoke_2.465
+ ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_28
+ ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_29
+ ___64-[_CDSiriLearningSettings _startWithCallback:invokeCallbackNow:]_block_invoke.194
+ ___64-[_CDSiriLearningSettings _startWithCallback:invokeCallbackNow:]_block_invoke.197
+ ___64-[_DKKnowledgeStore deleteObjects:responseQueue:withCompletion:]_block_invoke.8
+ ___65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke.746
+ ___66-[_CDSocialInteractionAdvisor tuneUsingSettings:heartBeatHandler:]_block_invoke.209
+ ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.817
+ ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.817.cold.1
+ ___70-[_CDInteractionStore fetchOrCreateContactRecord:context:cache:error:]_block_invoke.cold.2
+ ___75-[_CDSocialInteractionAdvisor rankContacts:withSeedContacts:usingSettings:]_block_invoke.195
+ ___77+[_DKSync2Policy possiblyDownloadSyncPolicyWithPolicyDownloadIntervalInDays:]_block_invoke.146
+ ___77+[_DKSync2Policy possiblyDownloadSyncPolicyWithPolicyDownloadIntervalInDays:]_block_invoke.146.cold.1
+ ___77+[_DKSync2Policy possiblyDownloadSyncPolicyWithPolicyDownloadIntervalInDays:]_block_invoke.146.cold.2
+ ___77+[_DKSync2Policy possiblyDownloadSyncPolicyWithPolicyDownloadIntervalInDays:]_block_invoke.148
+ ___78-[_CDInteractionsStatisticsConfig detectedSceneCategoryNamesFromSceneNetTags:]_block_invoke
+ ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.807
+ ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.807.cold.1
+ ___87-[_CDSocialInteractionAdvisor adviseInteractionsForDate:andSeedContacts:usingSettings:]_block_invoke.204
+ ___90-[_CDSpotlightItemRecorder saveRateLimitedEvents:donatorUid:responseQueue:withCompletion:]_block_invoke.781
+ ___95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.821
+ ___block_descriptor_32_e29_16?0"_CDAttachmentRecord"8l
+ ___block_descriptor_40_e21_B24?0"_DKEvent"816l
+ ___block_descriptor_40_e8_32s_e26_B24?0"BMStoreEvent"8^B16ls32l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e5_C8?0ls32l8s40l8s48l8r64l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e5_v8?0ls32l8s40l8s48l8s56l8r72l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72r80r_e5_v8?0ls32l8s40l8s48l8s56l8r72l8r80l8s64l8
+ ___block_literal_global.1171
+ ___block_literal_global.126
+ ___block_literal_global.151
+ ___block_literal_global.182
+ ___block_literal_global.192
+ ___block_literal_global.206
+ ___block_literal_global.219
+ ___block_literal_global.258
+ ___block_literal_global.268
+ ___block_literal_global.270
+ ___block_literal_global.272
+ ___block_literal_global.274
+ ___block_literal_global.276
+ ___block_literal_global.278
+ ___block_literal_global.280
+ ___block_literal_global.282
+ ___block_literal_global.284
+ ___block_literal_global.286
+ ___block_literal_global.288
+ ___block_literal_global.290
+ ___block_literal_global.292
+ ___block_literal_global.294
+ ___block_literal_global.296
+ ___block_literal_global.298
+ ___block_literal_global.300
+ ___block_literal_global.302
+ ___block_literal_global.304
+ ___block_literal_global.306
+ ___block_literal_global.308
+ ___block_literal_global.310
+ ___block_literal_global.312
+ ___block_literal_global.314
+ ___block_literal_global.316
+ ___block_literal_global.318
+ ___block_literal_global.320
+ ___block_literal_global.322
+ ___block_literal_global.334
+ ___block_literal_global.337
+ ___block_literal_global.339
+ ___block_literal_global.341
+ ___block_literal_global.363
+ ___block_literal_global.424
+ ___block_literal_global.484
+ ___block_literal_global.490
+ ___block_literal_global.505
+ ___block_literal_global.54
+ ___block_literal_global.578
+ ___block_literal_global.732
+ ___block_literal_global.737
+ ___block_literal_global.781
+ ___block_literal_global.788
+ ___get_PSContactHandleFeatureProviderClass_block_invoke
+ _allowedStreams.allowedStreams
+ _allowedStreams.onceToken
+ _get_PSContactHandleFeatureProviderClass
+ _get_PSContactHandleFeatureProviderClass.softClass
+ _isCoreDuetProcess.isKnowledgeDaemon
+ _isCoreDuetProcess.onceToken
+ _isDigitalHealthProcess.isKnowledgeDaemon
+ _isDigitalHealthProcess.onceToken
+ _isKnowledgeDaemon.isKnowledgeDaemon
+ _isKnowledgeDaemon.onceToken
+ _objc_msgSend$RelevantShortcuts
+ _objc_msgSend$_setError
+ _objc_msgSend$_uniqueIdentifier
+ _objc_msgSend$allowedStreams
+ _objc_msgSend$deleteEventsPassingTest:
+ _objc_msgSend$filterEvents:
+ _objc_msgSend$hasError
+ _objc_msgSend$initWithBundleID:keyImageProxyIdentifier:serializedRelevantShortcut:
+ _objc_msgSend$isCompletelyDisabled
+ _objc_msgSend$isCoreDuetProcess
+ _objc_msgSend$isDigitalHealthProcess
+ _objc_msgSend$isDigitalHealthSyncDisabled
+ _objc_msgSend$isEqualToContactStatistics:
+ _objc_msgSend$isKnowledgeDaemon
+ _objc_msgSend$isRequestAllowed:
+ _objc_msgSend$knowledgeStoreDisabledError
+ _objc_msgSend$logFault
+ _objc_msgSend$position
+ _objc_msgSend$pruner
+ _objc_msgSend$removeFeature:andConversation:
+ _objc_msgSend$setPosition:
+ _psBackgroundProcessingChannel.onceToken
+ _psBackgroundProcessingChannel.psBackgroundProcessingChannel
- +[_DKKnowledgeStore isDisabled]
- +[_DKKnowledgeStore isDisabled].cold.1
- +[_DKKnowledgeStore knowledgeStoreDisabledError]
- +[_DKSync2Coordinator _syncTypeFromActivity:].cold.4
- -[_CDInteractionStore truncateInteractionsToCount:]
- -[_CDInteractionStore truncateInteractionsToCount:].cold.1
- -[_CDInteractionsStatistics computeSASSFeatureWithScenesDetectedInPhoto:andConfiguredScenes:]
- -[_CDInteractionsStatisticsConfig scenesBasedFeaturesNames]
- -[_CDInteractionsStatisticsConfig scenesInPhotoIdentifiers]
- -[_CDInteractionsStatisticsConfig setScenesInPhotoIdentifiers:]
- -[_CDInteractionsStatisticsConfig topLevelScenesFromSceneNetTags:]
- -[_CDPeriodicScheduler registerJob:].cold.1
- -[_CDPeriodicScheduler updateExecutionCriteriaOnJob:].cold.1
- -[_DKSync2Coordinator __performSyncWithCompletion:].cold.4
- -[_DKSync2Coordinator _performSyncWithSyncType:completion:].cold.2
- -[_DKSync2Coordinator _performSyncWithSyncType:completion:].cold.3
- -[_DKSync2Coordinator _performSyncWithSyncType:completion:].cold.4
- -[_DKSync2Coordinator _performSyncWithSyncType:completion:].cold.5
- -[_DKSync2Coordinator _performSyncWithSyncType:completion:].cold.6
- -[_DKSync2Coordinator _performSyncWithSyncType:completion:].cold.7
- -[_DKSync2Coordinator _performSyncWithSyncType:completion:].cold.8
- -[_DKSync2Coordinator _possiblyPerformInitialSync].cold.1
- -[_DKSync2Coordinator _registerPeriodicJobWithInterval:].cold.1
- -[_DKSync2Coordinator _registerTriggeredSyncActivityWithIsStartup:].cold.1
- -[_DKSync2Coordinator _runTriggeredSyncActivity:].cold.1
- -[_DKSync2Coordinator _updatedExecutionCriteriaFromType:].cold.3
- -[_DKSync2Coordinator _updatedExecutionCriteriaFromType:].cold.4
- -[_DKSync2Coordinator start].cold.1
- -[_DKSync2Coordinator start].cold.2
- -[_DKSync2Coordinator start].cold.3
- -[_DKSync2Coordinator(APSConnectionDelegate) connection:didReceivePublicToken:].cold.1
- -[_DKSync2Coordinator(_DKKnowledgeStorageEventNotificationDelegate) _databaseDidDeleteFromStreamNameCounts:].cold.1
- -[_DKSync2Coordinator(_DKKnowledgeStorageEventNotificationDelegate) _databaseDidDeleteFromStreamNameCounts:].cold.2
- GCC_except_table163
- GCC_except_table172
- GCC_except_table174
- GCC_except_table175
- GCC_except_table176
- GCC_except_table177
- GCC_except_table186
- GCC_except_table187
- GCC_except_table192
- GCC_except_table202
- GCC_except_table204
- GCC_except_table303
- GCC_except_table308
- GCC_except_table311
- GCC_except_table314
- GCC_except_table317
- GCC_except_table320
- GCC_except_table323
- GCC_except_table329
- GCC_except_table332
- GCC_except_table335
- GCC_except_table341
- GCC_except_table344
- GCC_except_table350
- GCC_except_table356
- GCC_except_table359
- GCC_except_table362
- GCC_except_table365
- GCC_except_table371
- GCC_except_table377
- GCC_except_table382
- GCC_except_table388
- GCC_except_table447
- GCC_except_table450
- GCC_except_table453
- GCC_except_table456
- GCC_except_table459
- GCC_except_table462
- GCC_except_table465
- GCC_except_table468
- GCC_except_table471
- GCC_except_table474
- GCC_except_table483
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _InteractionAnalysisPETInteractionEventsReadFrom.cold.1
- _OBJC_IVAR_$__CDInteractionsStatisticsConfig._scenesInPhotoIdentifiers
- __DKPRChangeSetReadFrom.cold.1
- ___100-[_CDInteractionStore queryInteractionsUsingPredicate:sortDescriptors:limit:offset:objectIDs:error:]_block_invoke.369
- ___108-[_DKSync2Coordinator(_DKKnowledgeStorageEventNotificationDelegate) _databaseDidDeleteFromStreamNameCounts:]_block_invoke.cold.2
- ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.719
- ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.727
- ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.1128
- ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.1128.cold.1
- ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.1133
- ___31-[_CDInteractionCache _refetch]_block_invoke.254
- ___31-[_CDInteractionCache _refetch]_block_invoke.254.cold.1
- ___36-[_CDPeriodicScheduler registerJob:]_block_invoke.61.cold.1
- ___36-[_CDPeriodicScheduler registerJob:]_block_invoke.61.cold.2
- ___36-[_CDPeriodicScheduler registerJob:]_block_invoke.cold.3
- ___37-[_DKSync2Coordinator syncWithReply:]_block_invoke_2.cold.2
- ___41-[_CDInteractionStore metadataDictionary]_block_invoke.471
- ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1194
- ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1194.cold.1
- ___51-[_DKSync2Coordinator __performSyncWithCompletion:]_block_invoke.cold.1
- ___53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.293
- ___53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.326
- ___58-[_CDInteractionStore getInteractionsStatisticsForConfig:]_block_invoke.451
- ___58-[_CDInteractionStore getInteractionsStatisticsForConfig:]_block_invoke_2.455
- ___59-[_CDInteractionsStatisticsConfig scenesBasedFeaturesNames]_block_invoke
- ___59-[_DKSync2Coordinator _performSyncWithSyncType:completion:]_block_invoke.cold.1
- ___59-[_DKSync2Coordinator _performSyncWithSyncType:completion:]_block_invoke.cold.2
- ___60-[_DKSync2Coordinator _registerRapportLaunchOnDemandHandler]_block_invoke.cold.1
- ___64-[_CDSiriLearningSettings _startWithCallback:invokeCallbackNow:]_block_invoke.188
- ___64-[_CDSiriLearningSettings _startWithCallback:invokeCallbackNow:]_block_invoke.191
- ___64-[_DKKnowledgeStore deleteObjects:responseQueue:withCompletion:]_block_invoke.14
- ___65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke.740
- ___65-[_DKSync2Coordinator _synchronizeWithUrgency:client:completion:]_block_invoke.cold.2
- ___66-[_CDInteractionsStatisticsConfig topLevelScenesFromSceneNetTags:]_block_invoke
- ___66-[_CDSocialInteractionAdvisor tuneUsingSettings:heartBeatHandler:]_block_invoke.203
- ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.806
- ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.806.cold.1
- ___75-[_CDSocialInteractionAdvisor rankContacts:withSeedContacts:usingSettings:]_block_invoke.189
- ___77+[_DKSync2Policy possiblyDownloadSyncPolicyWithPolicyDownloadIntervalInDays:]_block_invoke.143
- ___77+[_DKSync2Policy possiblyDownloadSyncPolicyWithPolicyDownloadIntervalInDays:]_block_invoke.143.cold.1
- ___77+[_DKSync2Policy possiblyDownloadSyncPolicyWithPolicyDownloadIntervalInDays:]_block_invoke.143.cold.2
- ___77+[_DKSync2Policy possiblyDownloadSyncPolicyWithPolicyDownloadIntervalInDays:]_block_invoke.145
- ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.796
- ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.796.cold.1
- ___83-[_DKSync2Coordinator(APSConnectionDelegate) connection:didReceiveIncomingMessage:]_block_invoke.cold.2
- ___87-[_CDSocialInteractionAdvisor adviseInteractionsForDate:andSeedContacts:usingSettings:]_block_invoke.198
- ___95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.810
- ___block_descriptor_32_e18_16?0"NSString"8l
- ___block_descriptor_72_e8_32s40s48s56r64r_e5_C8?0ls32l8s40l8s48l8r56l8r64l8
- ___block_descriptor_88_e8_32s40s48s56s64r72r80r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8r72l8r80l8
- ___block_literal_global.1165
- ___block_literal_global.122
- ___block_literal_global.148
- ___block_literal_global.176
- ___block_literal_global.186
- ___block_literal_global.200
- ___block_literal_global.213
- ___block_literal_global.252
- ___block_literal_global.259
- ___block_literal_global.267
- ___block_literal_global.269
- ___block_literal_global.271
- ___block_literal_global.273
- ___block_literal_global.275
- ___block_literal_global.277
- ___block_literal_global.279
- ___block_literal_global.281
- ___block_literal_global.283
- ___block_literal_global.285
- ___block_literal_global.287
- ___block_literal_global.289
- ___block_literal_global.291
- ___block_literal_global.293
- ___block_literal_global.295
- ___block_literal_global.297
- ___block_literal_global.299
- ___block_literal_global.301
- ___block_literal_global.303
- ___block_literal_global.305
- ___block_literal_global.307
- ___block_literal_global.309
- ___block_literal_global.311
- ___block_literal_global.313
- ___block_literal_global.315
- ___block_literal_global.327
- ___block_literal_global.331
- ___block_literal_global.353
- ___block_literal_global.414
- ___block_literal_global.474
- ___block_literal_global.480
- ___block_literal_global.495
- ___block_literal_global.55
- ___block_literal_global.567
- ___block_literal_global.726
- ___block_literal_global.731
- ___block_literal_global.775
- ___block_literal_global.777
- _extend_feature_name
CStrings:
+ "%{public}@: Requested sync is a periodic sync. Marking period job as complete while current sync continues."
+ "%{public}@: Sync is decommisioned on this platform. All features, except DigitalHealth, have been disabled"
+ "%{public}@: Sync is decommisioned on this platform. All features, including DigitalHealth, have been disabled"
+ "%{public}@: XPC activity in unexpected CHECK_IN state %lu"
+ "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightRecorder.m:552"
+ "@\"BMStream\""
+ "@16@?0@\"_CDAttachmentRecord\"8"
+ "About to run handler for %@"
+ "B24@?0@\"_DKEvent\"8@16"
+ "ConversationGroupName"
+ "ConversationINImageURL"
+ "Couldn't create os_log_t psBackgroundProcessingChannel"
+ "DecommissionKnowledgeStore"
+ "DecommissionKnowledgeStoreFault"
+ "Donating Relevant Shortcuts to Biome"
+ "Failed to encoding XPC event for Relevant Shortcuts object with error: %@"
+ "Job %@ missing task to execute"
+ "MobileSafari"
+ "Publishing XPC event with Relevant Shortcuts: %{private}@; uid: %d"
+ "RelevantShortcuts"
+ "Safari"
+ "Safari Technology Preview"
+ "SafariViewService"
+ "ScreenTimeAgent"
+ "T@\"NSSet\",&,N,V_sceneTagsInPhotoIdentifiers"
+ "Unexpected record type %{public}@ (%{sensitive}@)"
+ "UsageTrackingAgent"
+ "Web App"
+ "_CDAppRelevantShortcutsBundleIDKey"
+ "_CDAppRelevantShortcutsKey"
+ "_CDDecommissionUtils"
+ "_PSContactHandleFeatureProvider"
+ "_relevantShortcutsStream"
+ "_sceneTagsInPhotoIdentifiers"
+ "_setError"
+ "_uniqueIdentifier"
+ "allowedStreams"
+ "cdknowledgetool"
+ "computeSASSFeatureWithSceneCategoriesDetectedInPhoto:andConfiguredSceneCategoryTags:"
+ "configuredSceneCategoryTagNames"
+ "deleteEventsPassingTest:"
+ "detectedSceneCategoryNamesFromSceneNetTags:"
+ "fetchOrCreateContactRecord: nil existingObjectWithID for %{public}@"
+ "filterEvents:"
+ "hasError"
+ "initWithBundleID:keyImageProxyIdentifier:serializedRelevantShortcut:"
+ "interactionFeaturesForHandle:reply:"
+ "isCompletelyDisabled"
+ "isCoreDuetProcess"
+ "isDigitalHealthProcess"
+ "isDigitalHealthSyncDisabled"
+ "isEqualToContactStatistics:"
+ "isKnowledgeDaemon"
+ "isRequestAllowed:"
+ "knowledgeStoreDisabledError"
+ "logFault"
+ "position"
+ "pruner"
+ "psBackgroundProcessing"
+ "psBackgroundProcessingChannel"
+ "publishXPCEventForRelevantShortcuts:bundleID:uid:"
+ "removeFeature:andConversation:"
+ "sceneTagsInPhotoIdentifiers"
+ "setPosition:"
+ "setSceneTagsInPhotoIdentifiers:"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\">24"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightRecorder.m:550"
- "@16@?0@\"NSString\"8"
- "DecomissionKnowledgeStore"
- "DecomissionKnowledgeStoreFault"
- "T@\"NSSet\",&,N,V_scenesInPhotoIdentifiers"
- "_scenesInPhotoIdentifiers"
- "computeSASSFeatureWithScenesDetectedInPhoto:andConfiguredScenes:"
- "computeShareSheetEphemeralFeaturesWithPredictionContext:reply:"
- "conditioned_%@"
- "scenesBasedFeaturesNames"
- "scenesInPhotoIdentifiers"
- "setScenesInPhotoIdentifiers:"
- "topLevelScenesFromSceneNetTags:"
- "truncateInteractionsToCount got nil cutoffDate for interaction %{sensitive}@ from bundle id %{public}@, target bundle id %{public}@"
- "truncateInteractionsToCount:"
- "truncateInteractionsToCount:%tu (cutoffDate: %@)"
- "truncateInteractionsToCount:0"
- "v32@0:8@\"_PSPredictionContext\"16@?<v@?@\"NSDictionary\">24"
- "v40@0:8@\"NSDictionary\"16@\"_PSPredictionContext\"24@?<v@?@\"_PSPredictionContext\">32"
- "validateCoreMLScoringModelWithRawInput:predictionContext:reply:"

```
