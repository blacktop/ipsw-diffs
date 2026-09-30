## CoreSpotlight

> `/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight`

```diff

-2400.22.0.0.0
-  __TEXT.__text: 0xd0050
-  __TEXT.__auth_stubs: 0x1c00
-  __TEXT.__objc_methlist: 0xca48
-  __TEXT.__const: 0xcd8
-  __TEXT.__gcc_except_tab: 0x2eec
-  __TEXT.__oslogstring: 0x7de9
-  __TEXT.__cstring: 0x12b62
-  __TEXT.__dlopen_cstrs: 0x3f1
+2418.4.8.2.100
+  __TEXT.__text: 0xe8a34
+  __TEXT.__auth_stubs: 0x1d20
+  __TEXT.__objc_methlist: 0xd808
+  __TEXT.__const: 0xd00
+  __TEXT.__cstring: 0x147d7
+  __TEXT.__gcc_except_tab: 0x2f90
+  __TEXT.__oslogstring: 0x849e
+  __TEXT.__dlopen_cstrs: 0x49b
   __TEXT.__ustring: 0x3c
   __TEXT.__swift5_typeref: 0x2a0
   __TEXT.__swift5_reflstr: 0x77

   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x33d8
-  __TEXT.__eh_frame: 0x1e8
-  __TEXT.__objc_classname: 0xfd3
-  __TEXT.__objc_methname: 0x1d9ca
-  __TEXT.__objc_methtype: 0x21d0
-  __TEXT.__objc_stubs: 0xfc80
-  __DATA_CONST.__got: 0x790
-  __DATA_CONST.__const: 0x4ff8
-  __DATA_CONST.__objc_classlist: 0x450
+  __TEXT.__unwind_info: 0x3d30
+  __TEXT.__eh_frame: 0x210
+  __TEXT.__objc_classname: 0x1180
+  __TEXT.__objc_methname: 0x20608
+  __TEXT.__objc_methtype: 0x2682
+  __TEXT.__objc_stubs: 0x10ba0
+  __DATA_CONST.__got: 0x838
+  __DATA_CONST.__const: 0x5470
+  __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x88
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x77f8
+  __DATA_CONST.__objc_selrefs: 0x7dd8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x338
-  __DATA_CONST.__objc_arraydata: 0xd48
-  __AUTH_CONST.__auth_got: 0xe10
-  __AUTH_CONST.__const: 0x18f0
-  __AUTH_CONST.__cfstring: 0x12680
-  __AUTH_CONST.__objc_const: 0x10810
-  __AUTH_CONST.__objc_arrayobj: 0xa50
-  __AUTH_CONST.__objc_intobj: 0x798
-  __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__objc_doubleobj: 0xc0
-  __AUTH.__objc_data: 0x1a68
+  __DATA_CONST.__objc_superrefs: 0x380
+  __DATA_CONST.__objc_arraydata: 0xd90
+  __AUTH_CONST.__auth_got: 0xea8
+  __AUTH_CONST.__const: 0x1a50
+  __AUTH_CONST.__cfstring: 0x13c00
+  __AUTH_CONST.__objc_const: 0x11eb8
+  __AUTH_CONST.__objc_arrayobj: 0xa80
+  __AUTH_CONST.__objc_intobj: 0x7b0
+  __AUTH_CONST.__objc_dictobj: 0x118
+  __AUTH_CONST.__objc_doubleobj: 0xd0
+  __AUTH.__objc_data: 0x1900
   __AUTH.__data: 0x3a0
-  __DATA.__objc_ivar: 0xb8c
-  __DATA.__data: 0xa58
-  __DATA.__bss: 0x1220
-  __DATA_DIRTY.__objc_data: 0x10b8
-  __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__bss: 0x7ea8
-  __DATA_DIRTY.__common: 0x10
+  __DATA.__objc_ivar: 0xc94
+  __DATA.__data: 0xab8
+  __DATA.__bss: 0x1320
+  __DATA_DIRTY.__objc_data: 0x15e0
+  __DATA_DIRTY.__data: 0x20
+  __DATA_DIRTY.__bss: 0x9a10
+  __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
+  - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CSExattrCrypto.framework/CSExattrCrypto
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 3E87C7B4-1514-3FF6-9596-7A74C72E64E5
-  Functions: 5480
-  Symbols:   17267
-  CStrings:  12099
+  UUID: FD962F93-B163-3197-8019-6C29A5DC715F
+  Functions: 5899
+  Symbols:   18652
+  CStrings:  12891
 
Symbols:
+ +[CSDonationProgress supportsSecureCoding]
+ +[CSDonationProgressFailure supportsSecureCoding]
+ +[CSIndexingPipelineOverallCompleteness supportsSecureCoding]
+ +[CSIndexingPipelineOverallCompletenessForBundle supportsSecureCoding]
+ +[CSInlineDonation _inlineDonationWithOverrideBundleID:protectionClass:addOrUpdateItems:associatedTextContent:associatedHTMLContent:deleteItemIdentifiers:deleteDomainIdentifiers:deleteAllItems:clientStateName:updatedClientState:expectedClientState:itemsDataSize:options:donationType:]
+ +[CSInlineDonation _inlineDonationWithOverrideBundleID:protectionClass:addOrUpdateItems:associatedTextContent:associatedHTMLContent:deleteItemIdentifiers:deleteDomainIdentifiers:deleteAllItems:clientStateName:updatedClientState:expectedClientState:itemsDataSize:options:donationType:].cold.1
+ +[CSInlineDonation inlineAddOrUpdateItems:associatedTextContent:associatedHTMLContent:deleteItemIdentifiers:overrideBundleID:protectionClass:clientStateName:updatedClientState:expectedClientState:itemsDataSize:options:]
+ +[CSInlineDonation inlineDeleteAllItemsWithOverrideBundleID:protectionClass:options:]
+ +[CSInlineDonation inlineDeleteDomainIdentifiers:overrideBundleID:protectionClass:options:]
+ +[CSInlineDonation isInlineCascadeDonationEnabled]
+ +[CSInlineDonation isInlineDocumentCacheEnabledForBundleID:]
+ +[CSInlineDonation sharedQueue]
+ +[CSInlineDonation sharedQueue].cold.1
+ +[CSInlineDonation translator]
+ +[CSInlineDonation translator].cold.1
+ +[CSInlineDonation translator].cold.2
+ +[CSInstantAnswers isInstantAnswerTriggerQuery:isCJK:isSearchToolClient:]
+ +[CSMockSearchableIndex _overrideDefaultSearchableIndexForTestingWithDoSet:searchableIndex:]
+ +[CSMockSearchableIndex _swizzleDefaultSearchableIndexWithDoSwizzle:]
+ +[CSMockSearchableIndex defaultSearchableIndex]
+ +[CSMockSearchableIndex defaultSearchableIndex].cold.1
+ +[CSMockSearchableIndex overrideDefaultSearchableIndexForTestingWithSearchableIndex:]
+ +[CSMockSearchableIndex restoreSwizzledDefaultSearchableIndex]
+ +[CSMockSearchableIndex swizzleDefaultSearchableIndex]
+ +[CSPersonalAnswers isEventIntentForQueryUnderstandingOutput:isSearchToolClient:isSearchToolCerberus:]
+ +[CSPersonalAnswers isEventIntentForQueryUnderstandingOutput:isSearchToolClient:isSearchToolCerberus:].cold.1
+ +[CSPersonalAnswers isEventIntentForQueryUnderstandingOutput:isSearchToolClient:isSearchToolCerberus:].cold.2
+ +[CSPipelineCompletenessReport supportsSecureCoding]
+ +[CSPipelineCompletenessReportStorage defaultInstance]
+ +[CSPlace supportsSecureCoding]
+ +[CSPowerHUD getSpotlightDataExpiration]
+ +[CSPowerHUD getSpotlightOperationsDataWithTimeInterval:]
+ +[CSPowerHUD isSpotlightDataExpired]
+ +[CSPowerHUD sharedInstance]
+ +[CSPowerHUD sharedInstance].cold.1
+ +[CSPowerHUD timeUntilSpotlightDataExpires]
+ +[CSRecurrenceRule supportsSecureCoding]
+ +[CSSearchConnection(InternalTestIndex) testSearchConnection]
+ +[CSSearchConnection(InternalTestIndex) testSearchConnection].cold.1
+ +[CSSearchQuery fetchDonationProgressForBundles:completionHandler:]
+ +[CSSearchableItemAttributeSet(EventType) localizedForKMDItemCardSubType:]
+ +[CSSearchableItemAttributeSet(EventType) localizedForKMDItemCardSubType:].cold.1
+ +[CSSearchableItemAttributeSet(EventType) localizedForKMDItemCardType:]
+ +[CSSearchableItemAttributeSet(EventType) localizedForKMDItemCardType:].cold.1
+ +[CSSearchableItemAttributeSet(EventType) localizedForKMDItemEventRestaurantMealType:]
+ +[CSSearchableItemAttributeSet(EventType) localizedForKMDItemEventRestaurantMealType:].cold.1
+ +[CSSearchableItemAttributeSet(EventType) localizedForKMDItemEventStatus:]
+ +[CSSearchableItemAttributeSet(EventType) localizedForKMDItemEventStatus:].cold.1
+ +[CSSearchableItemAttributeSet(EventType) localizedForKMDItemEventSubType:]
+ +[CSSearchableItemAttributeSet(EventType) localizedForKMDItemEventSubType:].cold.1
+ +[CSSearchableItemAttributeSet(MessagesSharedLink) localizedLinkSubTypeForLinkSubType:]
+ +[CSSearchableItemAttributeSet(MessagesSharedLink) localizedLinkSubTypeForLinkSubType:].cold.1
+ +[CSSearchableItemAttributeSet(MessagesSharedLink) localizedLinkTypeForLinkType:]
+ +[CSSearchableItemAttributeSet(MessagesSharedLink) localizedLinkTypeForLinkType:].cold.1
+ +[CSSearchableItemAttributeSet(MessagesSharedLink) localizedPrefixForPrefix:]
+ +[CSSearchableItemAttributeSet(MessagesSharedLink) localizedPrefixForPrefix:].cold.1
+ +[CSTestIndexConnection testConnectionForUser:]
+ +[CSTestSearchableIndex defaultSearchableIndex]
+ +[CSTestSearchableIndex defaultSearchableIndex].cold.1
+ -[CSAddressTag code]
+ -[CSAddressTag description]
+ -[CSAddressTag initWithAddress:synonyms:code:confidence:]
+ -[CSAddressTag initWithAddress:synonyms:code:type:lat:lng:confidence:]
+ -[CSDonationProgress .cxx_destruct]
+ -[CSDonationProgress allKnownItems]
+ -[CSDonationProgress dateOfNewestUndonatedItem]
+ -[CSDonationProgress description]
+ -[CSDonationProgress donatedItems]
+ -[CSDonationProgress encodeWithCoder:]
+ -[CSDonationProgress hash]
+ -[CSDonationProgress initWithAllKnownItems:itemsNeedingDonation:donatedItems:partiallyDonatedItems:itemsNeedingDonationForRedonationRequests:]
+ -[CSDonationProgress initWithAllKnownItems:itemsNeedingDonation:donatedItems:partiallyDonatedItems:itemsNeedingDonationForRedonationRequests:dateOfNewestUndonatedItem:]
+ -[CSDonationProgress initWithCoder:]
+ -[CSDonationProgress isEqual:]
+ -[CSDonationProgress itemsNeedingDonationForRedonationRequests]
+ -[CSDonationProgress itemsNeedingDonation]
+ -[CSDonationProgress partiallyDonatedItems]
+ -[CSDonationProgress(CSCoderAdditions) encodeWithCSCoder:]
+ -[CSDonationProgressFailure .cxx_destruct]
+ -[CSDonationProgressFailure encodeWithCoder:]
+ -[CSDonationProgressFailure failureReason]
+ -[CSDonationProgressFailure hash]
+ -[CSDonationProgressFailure initWithCoder:]
+ -[CSDonationProgressFailure initWithFailureReason:underlyingError:]
+ -[CSDonationProgressFailure isEqual:]
+ -[CSDonationProgressFailure underlyingError]
+ -[CSDonationProgressFailure(CSCoderAdditions) encodeWithCSCoder:]
+ -[CSDonationProgressQueryResult .cxx_destruct]
+ -[CSDonationProgressQueryResult bundleID]
+ -[CSDonationProgressQueryResult donationProgress]
+ -[CSDonationProgressQueryResult indexName]
+ -[CSDonationProgressQueryResult initWithBundleID:indexName:status:donationProgress:]
+ -[CSDonationProgressQueryResult status]
+ -[CSIndexingPipelineOverallCompleteness .cxx_destruct]
+ -[CSIndexingPipelineOverallCompleteness description]
+ -[CSIndexingPipelineOverallCompleteness donationCompeleteness]
+ -[CSIndexingPipelineOverallCompleteness encodeWithCoder:]
+ -[CSIndexingPipelineOverallCompleteness initWithCoder:]
+ -[CSIndexingPipelineOverallCompleteness initWithPipeline:overallCompleteness:donationCompeleteness:pipelineCompleteness:pipelineCompletenessHeuristicScore:pipelineReportAge:]
+ -[CSIndexingPipelineOverallCompleteness isSufficientlyComplete]
+ -[CSIndexingPipelineOverallCompleteness overallCompleteness]
+ -[CSIndexingPipelineOverallCompleteness pipelineCompletenessHeuristicScore]
+ -[CSIndexingPipelineOverallCompleteness pipelineCompleteness]
+ -[CSIndexingPipelineOverallCompleteness pipelineReportAge]
+ -[CSIndexingPipelineOverallCompleteness pipeline]
+ -[CSIndexingPipelineOverallCompleteness sufficientlyCompleteThreshold]
+ -[CSIndexingPipelineOverallCompletenessForBundle .cxx_destruct]
+ -[CSIndexingPipelineOverallCompletenessForBundle bundleID]
+ -[CSIndexingPipelineOverallCompletenessForBundle description]
+ -[CSIndexingPipelineOverallCompletenessForBundle donationProgress]
+ -[CSIndexingPipelineOverallCompletenessForBundle encodeWithCoder:]
+ -[CSIndexingPipelineOverallCompletenessForBundle initWithCoder:]
+ -[CSIndexingPipelineOverallCompletenessForBundle initWithPipeline:bundleID:overallCompleteness:donationCompeleteness:pipelineCompleteness:pipelineCompletenessHeuristicScore:pipelineReportAge:donationProgress:pipelineCompletenessFirstTimeBucket:pipelineCompletenessSecondBucket:pipelineCompletenessThirdBucket:]
+ -[CSIndexingPipelineOverallCompletenessForBundle pipelineCompletenessFirstTimeBucket]
+ -[CSIndexingPipelineOverallCompletenessForBundle pipelineCompletenessSecondBucket]
+ -[CSIndexingPipelineOverallCompletenessForBundle pipelineCompletenessThirdBucket]
+ -[CSInlineDonation .cxx_destruct]
+ -[CSInlineDonation _addOrUpdateItem:withIdentifier:donation:error:]
+ -[CSInlineDonation _logErrorWithCode:description:underlying:]
+ -[CSInlineDonation _perform:]
+ -[CSInlineDonation _perform:].cold.1
+ -[CSInlineDonation _perform:].cold.2
+ -[CSInlineDonation _reportErrorWithCode:clientDescription:donationErrorCode:underlying:]
+ -[CSInlineDonation _resolveDonationName]
+ -[CSInlineDonation _updateRevisionToken:error:]
+ -[CSInlineDonation addOrUpdateItems]
+ -[CSInlineDonation associatedHTMLContent]
+ -[CSInlineDonation associatedTextContent]
+ -[CSInlineDonation clientStateName]
+ -[CSInlineDonation deleteAllItems]
+ -[CSInlineDonation deleteDomainIdentifiers]
+ -[CSInlineDonation deleteItemIdentifiers]
+ -[CSInlineDonation description]
+ -[CSInlineDonation donationName]
+ -[CSInlineDonation donationTimestamp]
+ -[CSInlineDonation donationType]
+ -[CSInlineDonation expectedClientState]
+ -[CSInlineDonation initWithSourceIdentifier:addOrUpdateItems:associatedTextContent:associatedHTMLContent:deleteItemIdentifiers:deleteDomainIdentifiers:deleteAllItems:clientStateName:updatedClientState:expectedClientState:itemsDataSize:donationType:]
+ -[CSInlineDonation isInlineCacheEnabled]
+ -[CSInlineDonation itemsDataSize]
+ -[CSInlineDonation performDonationAsync:]
+ -[CSInlineDonation sourceIdentifier]
+ -[CSInlineDonation updatedClientState]
+ -[CSMockSearchableIndex .cxx_destruct]
+ -[CSMockSearchableIndex _bulkFetchPartialPathsForObjects:protectionClass:bundleID:completionHandler:]
+ -[CSMockSearchableIndex _deleleActionsWithIdentifiers:completionHandler:]
+ -[CSMockSearchableIndex _deleteActionsBeforeTime:completionHandler:]
+ -[CSMockSearchableIndex _fetchAttributes:protectionClass:bundleID:items:includeParents:options:completionHandler:]
+ -[CSMockSearchableIndex _fetchBundleIDsWithCompletionHandler:]
+ -[CSMockSearchableIndex _fetchCacheFileDescriptorsForProtectionClass:bundleID:items:completionHandler:]
+ -[CSMockSearchableIndex _initWithName:protectionClass:bundleIdentifier:options:]
+ -[CSMockSearchableIndex _issueCommand:completionHandler:]
+ -[CSMockSearchableIndex _issueDiagnose:logQuery:completionHandler:]
+ -[CSMockSearchableIndex _issueNonLaunchingCommand:]
+ -[CSMockSearchableIndex _openJournalFile:completionHandler:]
+ -[CSMockSearchableIndex _photosLibraryDeleted:completionHandler:]
+ -[CSMockSearchableIndex _setUser:]
+ -[CSMockSearchableIndex addInteraction:bundleID:protectionClass:completionHandler:]
+ -[CSMockSearchableIndex addInteraction:completionHandler:]
+ -[CSMockSearchableIndex batchedDeletedIdentifiers]
+ -[CSMockSearchableIndex batchedItems]
+ -[CSMockSearchableIndex beginIndexBatch]
+ -[CSMockSearchableIndex bulkFetchAttributes:protectionClass:bundleID:objects:attributeKeyIndex:includeParents:completionHandler:]
+ -[CSMockSearchableIndex bulkFetchCacheFileDescriptorForProtectionClass:bundleID:identifiers:reason:completionHandler:]
+ -[CSMockSearchableIndex changeStateOfSearchableItemsWithUIDs:toState:]
+ -[CSMockSearchableIndex changeStateOfSearchableItemsWithUIDs:toState:forUser:forBundleID:forUTIType:]
+ -[CSMockSearchableIndex clientStates]
+ -[CSMockSearchableIndex deleteAllInteractionsWithBundleID:protectionClass:completionHandler:]
+ -[CSMockSearchableIndex deleteAllInteractionsWithCompletionHandler:]
+ -[CSMockSearchableIndex deleteAllSearchableItemsForBundleID:completionHandler:]
+ -[CSMockSearchableIndex deleteAllSearchableItemsWithCompletionHandler:]
+ -[CSMockSearchableIndex deleteAllSearchableItemsWithProtectionClass:forBundleID:options:completionHandler:]
+ -[CSMockSearchableIndex deleteAllSearchableItemsWithProtectionClass:forBundleID:options:reason:completionHandler:]
+ -[CSMockSearchableIndex deleteAllSearchableItemsWithReason:completionHandler:]
+ -[CSMockSearchableIndex deleteAllUserActivities:completionHandler:]
+ -[CSMockSearchableIndex deleteInteractionsWithGroupIdentifiers:bundleID:protectionClass:completionHandler:]
+ -[CSMockSearchableIndex deleteInteractionsWithGroupIdentifiers:completionHandler:]
+ -[CSMockSearchableIndex deleteInteractionsWithIdentifiers:bundleID:protectionClass:completionHandler:]
+ -[CSMockSearchableIndex deleteInteractionsWithIdentifiers:completionHandler:]
+ -[CSMockSearchableIndex deleteSearchableItemsSinceDate:completionHandler:]
+ -[CSMockSearchableIndex deleteSearchableItemsSinceDate:protectionClass:forBundleID:options:completionHandler:]
+ -[CSMockSearchableIndex deleteSearchableItemsWithDomainIdentifiers:completionHandler:]
+ -[CSMockSearchableIndex deleteSearchableItemsWithDomainIdentifiers:protectionClass:forBundleID:options:completionHandler:]
+ -[CSMockSearchableIndex deleteSearchableItemsWithDomainIdentifiers:protectionClass:forBundleID:options:reason:completionHandler:]
+ -[CSMockSearchableIndex deleteSearchableItemsWithDomainIdentifiers:reason:completionHandler:]
+ -[CSMockSearchableIndex deleteSearchableItemsWithIdentifiers:completionHandler:]
+ -[CSMockSearchableIndex deleteSearchableItemsWithIdentifiers:reason:completionHandler:]
+ -[CSMockSearchableIndex deleteUserActivitiesWithPersistentIdentifiers:bundleID:completionHandler:]
+ -[CSMockSearchableIndex deletedInteractions]
+ -[CSMockSearchableIndex deletedItems]
+ -[CSMockSearchableIndex deletedUserActivities]
+ -[CSMockSearchableIndex description]
+ -[CSMockSearchableIndex donateRelevantActions:bundleID:completionHandler:]
+ -[CSMockSearchableIndex donateRelevantShortcuts:bundleID:completionHandler:]
+ -[CSMockSearchableIndex embeddingCompletenessForBundle:completion:]
+ -[CSMockSearchableIndex endIndexBatchWithClientState:completionHandler:]
+ -[CSMockSearchableIndex endIndexBatchWithClientState:critical:completionHandler:]
+ -[CSMockSearchableIndex endIndexBatchWithClientState:critical:reason:completionHandler:]
+ -[CSMockSearchableIndex endIndexBatchWithExpectedClientState:newClientState:completionHandler:]
+ -[CSMockSearchableIndex endIndexBatchWithExpectedClientState:newClientState:critical:completionHandler:]
+ -[CSMockSearchableIndex endIndexBatchWithExpectedClientState:newClientState:critical:reason:completionHandler:]
+ -[CSMockSearchableIndex endIndexBatchWithExpectedClientState:newClientState:reason:completionHandler:]
+ -[CSMockSearchableIndex errorOrNoopWithCompletionHandler:]
+ -[CSMockSearchableIndex errorUnsupportedWithCompletionHandler:]
+ -[CSMockSearchableIndex fetchAttributes:protectionClass:bundleID:identifiers:userCtx:flags:qos:completionHandler:]
+ -[CSMockSearchableIndex fetchCacheFileDescriptorsForProtectionClass:bundleID:identifiers:userCtx:flags:qos:completionHandler:]
+ -[CSMockSearchableIndex fetchDataForBundleIdentifier:itemIdentifier:contentType:completionHandler:]
+ -[CSMockSearchableIndex fetchLastClientStateWithCompletionHandler:]
+ -[CSMockSearchableIndex fetchLastClientStateWithProtectionClass:forBundleID:clientStateName:options:completionHandler:]
+ -[CSMockSearchableIndex finishIndexingWhileLocked:protectionClass:completionHandler:]
+ -[CSMockSearchableIndex flushUserActivities]
+ -[CSMockSearchableIndex indexDelegate]
+ -[CSMockSearchableIndex indexSearchableItems:completionHandler:]
+ -[CSMockSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:clientStateName:protectionClass:forBundleID:options:completionHandler:]
+ -[CSMockSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:clientStateName:protectionClass:forBundleID:options:reason:completionHandler:]
+ -[CSMockSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:completionHandler:]
+ -[CSMockSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:protectionClass:forBundleID:options:reason:completionHandler:]
+ -[CSMockSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:protectionClass:forBundleID:options:completionHandler:]
+ -[CSMockSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:protectionClass:forBundleID:options:reason:completionHandler:]
+ -[CSMockSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:protectionClass:forBundleID:options:completionHandler:]
+ -[CSMockSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:protectionClass:forBundleID:options:reason:completionHandler:]
+ -[CSMockSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:reason:completionHandler:]
+ -[CSMockSearchableIndex indexSearchableItems:returningItemsSanitizedForSpotlightTo:]
+ -[CSMockSearchableIndex indexUserActivity:]
+ -[CSMockSearchableIndex indexedItems]
+ -[CSMockSearchableIndex initWithName:]
+ -[CSMockSearchableIndex initWithName:bundleIdentifier:]
+ -[CSMockSearchableIndex initWithName:options:]
+ -[CSMockSearchableIndex initWithName:protectionClass:]
+ -[CSMockSearchableIndex initWithName:protectionClass:bundleIdentifier:]
+ -[CSMockSearchableIndex init]
+ -[CSMockSearchableIndex interactions]
+ -[CSMockSearchableIndex isEmbeddingVersionCurrent:error:]
+ -[CSMockSearchableIndex isInBatch]
+ -[CSMockSearchableIndex performDataMigrationWithTimeout:completionHandler:]
+ -[CSMockSearchableIndex performIndexJob:protectionClass:acknowledgementHandler:]
+ -[CSMockSearchableIndex prepareIndexingWhileLocked:protectionClass:holdAssertionFor:completionHandler:]
+ -[CSMockSearchableIndex provideDataForBundle:identifier:type:completionHandler:]
+ -[CSMockSearchableIndex provideDataForBundle:itemIdentifier:typeIdentifier:allowDownload:completionHandler:]
+ -[CSMockSearchableIndex provideDataForBundle:itemIdentifier:typeIdentifier:options:completionHandler:]
+ -[CSMockSearchableIndex provideFileURLForBundle:identifier:type:completionHandler:]
+ -[CSMockSearchableIndex provideFileURLForBundle:itemIdentifier:typeIdentifier:inPlace:allowDownload:completionHandler:]
+ -[CSMockSearchableIndex provideFileURLForBundle:itemIdentifier:typeIdentifier:options:completionHandler:]
+ -[CSMockSearchableIndex provideFileURLsForBundle:itemIdentifiers:typeIdentifier:options:completionHandler:]
+ -[CSMockSearchableIndex reset]
+ -[CSMockSearchableIndex setIndexDelegate:]
+ -[CSMockSearchableIndex setShouldSimulateErrors:]
+ -[CSMockSearchableIndex setSimulatedError:]
+ -[CSMockSearchableIndex shouldSimulateErrors]
+ -[CSMockSearchableIndex simulatedError]
+ -[CSMockSearchableIndex slowFetchAttributes:protectionClass:bundleID:identifiers:completionHandler:]
+ -[CSMockSearchableIndex slowFetchAttributes:protectionClass:bundleID:identifiers:options:completionHandler:]
+ -[CSMockSearchableIndex throttle:]
+ -[CSMockSearchableIndex throttle]
+ -[CSMockSearchableIndex transferDeletionJournalsForProtectionClass:toDirectory:completionHandler:]
+ -[CSMockSearchableIndex unthrottle:]
+ -[CSMockSearchableIndex unthrottle]
+ -[CSMockSearchableIndex updateCorrectionsWithFilePath:completionHandler:]
+ -[CSMockSearchableIndex updateCorrectionsWithFilePath:options:completionHandler:]
+ -[CSMockSearchableIndex userActivities]
+ -[CSMockSearchableIndex willModifySearchableItemsWithIdentifiers:completionHandler:]
+ -[CSMockSearchableIndex willModifySearchableItemsWithIdentifiers:protectionClass:forBundleID:options:completionHandler:]
+ -[CSPipelineCompletenessReport .cxx_destruct]
+ -[CSPipelineCompletenessReport bundleID]
+ -[CSPipelineCompletenessReport eligibleItems]
+ -[CSPipelineCompletenessReport encodeWithCoder:]
+ -[CSPipelineCompletenessReport initWithCoder:]
+ -[CSPipelineCompletenessReport initWithPipelineName:bundleID:eligibleItems:pipelineCompleteness:pipelineCompletenessHeuristicScore:pipelineCompletenessFirstTimeBucket:pipelineCompletenessSecondBucket:pipelineCompletenessThirdBucket:]
+ -[CSPipelineCompletenessReport pipelineCompletenessFirstTimeBucket]
+ -[CSPipelineCompletenessReport pipelineCompletenessHeuristicScore]
+ -[CSPipelineCompletenessReport pipelineCompletenessSecondBucket]
+ -[CSPipelineCompletenessReport pipelineCompletenessThirdBucket]
+ -[CSPipelineCompletenessReport pipelineCompleteness]
+ -[CSPipelineCompletenessReport pipeline]
+ -[CSPipelineCompletenessReport reportDate]
+ -[CSPipelineCompletenessReportStorage .cxx_destruct]
+ -[CSPipelineCompletenessReportStorage _createStorageDirectoryIfNotExistsWithError:]
+ -[CSPipelineCompletenessReportStorage _fileURLForPipeline:]
+ -[CSPipelineCompletenessReportStorage fetchCompletenessReportsForPipeline:error:]
+ -[CSPipelineCompletenessReportStorage initWithStorageURL:]
+ -[CSPipelineCompletenessReportStorage writeCompletenessReports:forPipeline:error:]
+ -[CSPlace .cxx_destruct]
+ -[CSPlace copyWithZone:]
+ -[CSPlace description]
+ -[CSPlace encodeWithCoder:]
+ -[CSPlace fullyFormattedAddress]
+ -[CSPlace hash]
+ -[CSPlace initWithCoder:]
+ -[CSPlace initWithFullyFormattedAddress:namedLocation:]
+ -[CSPlace initWithLatitude:longitude:fullyFormattedAddress:namedLocation:]
+ -[CSPlace initWithNamedLocation:]
+ -[CSPlace isEqual:]
+ -[CSPlace latitude]
+ -[CSPlace longitude]
+ -[CSPlace namedLocation]
+ -[CSPowerHUD .cxx_destruct]
+ -[CSPowerHUD biomeStream]
+ -[CSPowerHUD init]
+ -[CSPowerHUD setBiomeStream:]
+ -[CSPowerHUD writeToBiomeStreamWithBundleID:itemCount:baseOperation:]
+ -[CSPowerHUD writeToBiomeStreamWithBundleID:itemCount:baseOperation:identifier:reason:]
+ -[CSPowerHUD writeToBiomeStreamWithBundleID:itemCount:baseOperation:reason:]
+ -[CSRecurrenceRule .cxx_destruct]
+ -[CSRecurrenceRule copyWithZone:]
+ -[CSRecurrenceRule daysOfTheWeek]
+ -[CSRecurrenceRule description]
+ -[CSRecurrenceRule encodeWithCoder:]
+ -[CSRecurrenceRule hash]
+ -[CSRecurrenceRule initWithCoder:]
+ -[CSRecurrenceRule initWithDaysOfTheWeek:]
+ -[CSRecurrenceRule isEqual:]
+ -[CSRecurrenceRule setDaysOfTheWeek:]
+ -[CSRequestQueue .cxx_construct]
+ -[CSRequestQueue processWorkItemsUpToRequestID:]
+ -[CSSearchQuery handleGatherEnded].cold.1
+ -[CSSearchQuery logOwner]
+ -[CSSearchQuery setupFetchAttributesForSearch].cold.3
+ -[CSSearchQueryContext hasReadPurpose]
+ -[CSSearchQueryContext logToken]
+ -[CSSearchQueryContext mailQueryID]
+ -[CSSearchQueryContext setHasReadPurpose:]
+ -[CSSearchQueryContext setLogToken:]
+ -[CSSearchQueryContext setMailQueryID:]
+ -[CSSearchableIndex endIndexBatchWithExpectedClientState:newClientState:critical:reason:updatingDonationProgres:completionHandler:]
+ -[CSSearchableIndex endIndexBatchWithExpectedClientState:newClientState:critical:reason:updatingDonationProgres:completionHandler:].cold.1
+ -[CSSearchableIndex endIndexBatchWithExpectedClientState:newClientState:updatingDonationProgress:completionHandler:]
+ -[CSSearchableIndex endIndexBatchWithExpectedClientState:newClientState:updatingDonationProgress:critical:completionHandler:]
+ -[CSSearchableIndex endIndexBatchWithExpectedClientState:newClientState:updatingDonationProgress:reason:completionHandler:]
+ -[CSSearchableIndex fetchConsumedAndLatestSerialNums:completionHandler:]
+ -[CSSearchableIndex fetchConsumedAndLatestSerialNums:completionHandler:].cold.1
+ -[CSSearchableIndex fetchIndexingPipelineCompleteness:forBundles:completionHandler:]
+ -[CSSearchableIndex fetchIndexingPipelineOverallCompleteness:completionHandler:]
+ -[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:clientStateName:updatingDonationProgress:protectionClass:forBundleID:options:completionHandler:]
+ -[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:clientStateName:updatingDonationProgress:protectionClass:forBundleID:options:reason:completionHandler:]
+ -[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:updatingDonationProgress:protectionClass:forBundleID:options:reason:completionHandler:]
+ -[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:updatingDonationProgress:protectionClass:forBundleID:options:completionHandler:]
+ -[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:updatingDonationProgress:protectionClass:forBundleID:options:reason:completionHandler:]
+ -[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:updatingDonationProgress:protectionClass:forBundleID:options:completionHandler:]
+ -[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:updatingDonationProgress:protectionClass:forBundleID:options:reason:completionHandler:]
+ -[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:updatingDonationProgress:reason:completionHandler:]
+ -[CSSearchableIndex indexSearchableItems:updatingDonationProgress:completionHandler:]
+ -[CSSearchableIndex indexSearchableItems:updatingDonationProgress:completionHandler:].cold.1
+ -[CSSearchableIndex indexSearchableItems:updatingDonationProgress:completionHandler:].cold.2
+ -[CSSearchableIndex reportDonationProgress:completionHandler:]
+ -[CSSearchableIndex textContentCompletenessForBundle:completion:]
+ -[CSSearchableIndex(SpotlightKnowledge) indexDirectory:]
+ -[CSSearchableItem(Internal) _standardizePlaces:]
+ -[CSSearchableItemAttributeSet _getTimeComponentsForKey:]
+ -[CSSearchableItemAttributeSet _setTimeComponentsForKey:time:]
+ -[CSSearchableItemAttributeSet alarmRecurrenceRule]
+ -[CSSearchableItemAttributeSet alarmTime]
+ -[CSSearchableItemAttributeSet canSnooze]
+ -[CSSearchableItemAttributeSet hasSuggestedEdits]
+ -[CSSearchableItemAttributeSet isAlarmEnabled]
+ -[CSSearchableItemAttributeSet isCompleted]
+ -[CSSearchableItemAttributeSet isFlagged]
+ -[CSSearchableItemAttributeSet isRead]
+ -[CSSearchableItemAttributeSet isUserHidden]
+ -[CSSearchableItemAttributeSet isUserPrivate]
+ -[CSSearchableItemAttributeSet reminderRecurrenceRule]
+ -[CSSearchableItemAttributeSet reminderTime]
+ -[CSSearchableItemAttributeSet setAlarmEnabled:]
+ -[CSSearchableItemAttributeSet setAlarmRecurrenceRule:]
+ -[CSSearchableItemAttributeSet setAlarmTime:]
+ -[CSSearchableItemAttributeSet setCompleted:]
+ -[CSSearchableItemAttributeSet setFlagged:]
+ -[CSSearchableItemAttributeSet setRead:]
+ -[CSSearchableItemAttributeSet setReminderRecurrenceRule:]
+ -[CSSearchableItemAttributeSet setReminderTime:]
+ -[CSSearchableItemAttributeSet setSnooze:]
+ -[CSSearchableItemAttributeSet setSuggestedEdits:]
+ -[CSSearchableItemAttributeSet setTriggerState:]
+ -[CSSearchableItemAttributeSet setUserHidden:]
+ -[CSSearchableItemAttributeSet setUserPrivate:]
+ -[CSSearchableItemAttributeSet triggerState]
+ -[CSSearchableItemAttributeSet(AllEventTypes) getAllUniqueEventAttributes].cold.1
+ -[CSSearchableItemAttributeSet(CSAttributes) alternateTitles]
+ -[CSSearchableItemAttributeSet(CSAttributes) isFavorited]
+ -[CSSearchableItemAttributeSet(CSAttributes) place]
+ -[CSSearchableItemAttributeSet(CSAttributes) purchasedDate]
+ -[CSSearchableItemAttributeSet(CSAttributes) receivedDate]
+ -[CSSearchableItemAttributeSet(CSAttributes) releasedDate]
+ -[CSSearchableItemAttributeSet(CSAttributes) sentDate]
+ -[CSSearchableItemAttributeSet(CSAttributes) setAlternateTitles:]
+ -[CSSearchableItemAttributeSet(CSAttributes) setFavorited:]
+ -[CSSearchableItemAttributeSet(CSAttributes) setPlace:]
+ -[CSSearchableItemAttributeSet(CSAttributes) setPurchasedDate:]
+ -[CSSearchableItemAttributeSet(CSAttributes) setReceivedDate:]
+ -[CSSearchableItemAttributeSet(CSAttributes) setReleasedDate:]
+ -[CSSearchableItemAttributeSet(CSAttributes) setSentDate:]
+ -[CSSearchableItemAttributeSet(CSClock_Private) clockAlarmType]
+ -[CSSearchableItemAttributeSet(CSClock_Private) setClockAlarmType:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventEndDate]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventStartDate]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventEndDate:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventStartDate:]
+ -[CSSearchableItemAttributeSet(CSPhotos_Private) photosIdentificationDocumentsVersion]
+ -[CSSearchableItemAttributeSet(CSPhotos_Private) setPhotosIdentificationDocumentsVersion:]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) contentCatalog]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) detectedCardSubTypes]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) localizedLinkSubTypes]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) localizedLinkTypes]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) setContentCatalog:]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) setDetectedCardSubTypes:]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) setLocalizedLinkSubTypes:]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) setLocalizedLinkTypes:]
+ -[CSTestSearchQuery connection]
+ -[CSTestSearchableIndex connection]
+ -[CSXPCConnection dealloc]
+ -[FPProviderDomain(Private) isSpecialPhotosEmptyDomain]
+ -[FPProviderDomain(Private) isSpecialPhotosEmptyDomain].cold.1
+ GCC_except_table100
+ GCC_except_table101
+ GCC_except_table1053
+ GCC_except_table111
+ GCC_except_table112
+ GCC_except_table116
+ GCC_except_table117
+ GCC_except_table118
+ GCC_except_table124
+ GCC_except_table125
+ GCC_except_table132
+ GCC_except_table133
+ GCC_except_table137
+ GCC_except_table138
+ GCC_except_table153
+ GCC_except_table157
+ GCC_except_table161
+ GCC_except_table1622
+ GCC_except_table1628
+ GCC_except_table165
+ GCC_except_table169
+ GCC_except_table170
+ GCC_except_table174
+ GCC_except_table178
+ GCC_except_table179
+ GCC_except_table186
+ GCC_except_table187
+ GCC_except_table204
+ GCC_except_table207
+ GCC_except_table213
+ GCC_except_table214
+ GCC_except_table222
+ GCC_except_table223
+ GCC_except_table239
+ GCC_except_table240
+ GCC_except_table244
+ GCC_except_table245
+ GCC_except_table249
+ GCC_except_table250
+ GCC_except_table254
+ GCC_except_table268
+ GCC_except_table269
+ GCC_except_table272
+ GCC_except_table273
+ GCC_except_table277
+ GCC_except_table278
+ GCC_except_table280
+ GCC_except_table297
+ GCC_except_table298
+ GCC_except_table301
+ GCC_except_table305
+ GCC_except_table306
+ GCC_except_table309
+ GCC_except_table310
+ GCC_except_table315
+ GCC_except_table323
+ GCC_except_table328
+ GCC_except_table33
+ GCC_except_table335
+ GCC_except_table336
+ GCC_except_table338
+ GCC_except_table341
+ GCC_except_table346
+ GCC_except_table350
+ GCC_except_table351
+ GCC_except_table354
+ GCC_except_table356
+ GCC_except_table432
+ GCC_except_table433
+ GCC_except_table434
+ GCC_except_table435
+ GCC_except_table442
+ GCC_except_table479
+ GCC_except_table741
+ GCC_except_table83
+ GCC_except_table85
+ OBJC_IVAR_$_CSSearchQuery._cancelled
+ _AnalyticsSendEvent
+ _BiomeLibrary
+ _CFDataGetBytePtr
+ _CFStringCreateArrayBySeparatingStrings
+ _CFStringCreateByCombiningStrings
+ _CFStringCreateWithFormat
+ _CSCardSubTypeNationalID
+ _CSDonationTimestamp
+ _CSEventStatusPickedUp
+ _CSEventStatusReadyForPickup
+ _CSEventStatusUpdated
+ _CSEventStatusYetToBeShipped
+ _CSLinkedTimestamp
+ _CSLinkedTimestampFromHexString
+ _CSLinkedTimestampToHexString
+ _CSPipelineCompletenessReportStorageErrorDomain
+ _CSQueryAttributeMappingArray
+ _CSQueryAttributesMappingArrayCount
+ _CSQueryAttributesMappingArrayEntries
+ _CSSearchAgentTestMachServiceName
+ _CascadeSetsLibrary
+ _CascadeSetsLibraryCore.frameworkLibrary
+ _LinkServicesLibraryCore.frameworkLibrary
+ _MDFdTokenOwnerCreateForQuery
+ _MDFdTokenOwnerGetToken
+ _MDItemAlarmRecurrenceRule
+ _MDItemAlarmRecurrenceRuleDaysOfTheWeek
+ _MDItemAlarmTime
+ _MDItemAlarmTimeHour
+ _MDItemAlarmTimeMinute
+ _MDItemAlarmTimeSecond
+ _MDItemAlternateTitles
+ _MDItemAppEntitySchema
+ _MDItemCanSnooze
+ _MDItemClockAlarmEnabled
+ _MDItemClockAlarmType
+ _MDItemContentCatalog
+ _MDItemDerivedIsMeRankingTextContentMatchTokens
+ _MDItemDetectedCardSubTypes
+ _MDItemEventEndDate
+ _MDItemEventStartDate
+ _MDItemHasSuggestedEdits
+ _MDItemIsAlarmEnabled
+ _MDItemIsCompleted
+ _MDItemIsEnabled
+ _MDItemIsFavorited
+ _MDItemIsFlagged
+ _MDItemIsRead
+ _MDItemLocalizedLinkSubTypes
+ _MDItemLocalizedLinkTypes
+ _MDItemPhotosIdentificationDocumentsVersion
+ _MDItemPlace
+ _MDItemPurchasedDate
+ _MDItemReceivedDate
+ _MDItemRelatedBundleID
+ _MDItemReleasedDate
+ _MDItemReminderRecurrenceRule
+ _MDItemReminderRecurrenceRuleDaysOfTheWeek
+ _MDItemReminderTime
+ _MDItemReminderTimeHour
+ _MDItemReminderTimeMinute
+ _MDItemReminderTimeSecond
+ _MDItemSentDate
+ _MDItemTriggerState
+ _MDItemUserHidden
+ _MDItemUserPrivate
+ _NSDebugDescriptionErrorKey
+ _NSFilePathErrorKey
+ _NSInternalInconsistencyException
+ _OBJC_CLASS_$_BMPublisherOptions
+ _OBJC_CLASS_$_BMSpotlightOperations
+ _OBJC_CLASS_$_CSDonationProgress
+ _OBJC_CLASS_$_CSDonationProgressFailure
+ _OBJC_CLASS_$_CSDonationProgressQueryResult
+ _OBJC_CLASS_$_CSIndexingPipelineOverallCompleteness
+ _OBJC_CLASS_$_CSIndexingPipelineOverallCompletenessForBundle
+ _OBJC_CLASS_$_CSInlineDonation
+ _OBJC_CLASS_$_CSMockSearchableIndex
+ _OBJC_CLASS_$_CSPipelineCompletenessReport
+ _OBJC_CLASS_$_CSPipelineCompletenessReportStorage
+ _OBJC_CLASS_$_CSPlace
+ _OBJC_CLASS_$_CSPowerHUD
+ _OBJC_CLASS_$_CSRecurrenceRule
+ _OBJC_CLASS_$_CSTestIndexConnection
+ _OBJC_CLASS_$_CSTestSearchQuery
+ _OBJC_CLASS_$_CSTestSearchableIndex
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSScanner
+ _OBJC_IVAR_$_CSAddressTag._code
+ _OBJC_IVAR_$_CSDonationProgress._allKnownItems
+ _OBJC_IVAR_$_CSDonationProgress._dateOfNewestUndonatedItem
+ _OBJC_IVAR_$_CSDonationProgress._donatedItems
+ _OBJC_IVAR_$_CSDonationProgress._itemsNeedingDonation
+ _OBJC_IVAR_$_CSDonationProgress._itemsNeedingDonationForRedonationRequests
+ _OBJC_IVAR_$_CSDonationProgress._partiallyDonatedItems
+ _OBJC_IVAR_$_CSDonationProgressFailure._failureReason
+ _OBJC_IVAR_$_CSDonationProgressFailure._underlyingError
+ _OBJC_IVAR_$_CSDonationProgressQueryResult._bundleID
+ _OBJC_IVAR_$_CSDonationProgressQueryResult._donationProgress
+ _OBJC_IVAR_$_CSDonationProgressQueryResult._indexName
+ _OBJC_IVAR_$_CSDonationProgressQueryResult._status
+ _OBJC_IVAR_$_CSFileProviderDomainMonitor._needSave
+ _OBJC_IVAR_$_CSIndexingPipelineOverallCompleteness._donationCompeleteness
+ _OBJC_IVAR_$_CSIndexingPipelineOverallCompleteness._overallCompleteness
+ _OBJC_IVAR_$_CSIndexingPipelineOverallCompleteness._pipeline
+ _OBJC_IVAR_$_CSIndexingPipelineOverallCompleteness._pipelineCompleteness
+ _OBJC_IVAR_$_CSIndexingPipelineOverallCompleteness._pipelineCompletenessHeuristicScore
+ _OBJC_IVAR_$_CSIndexingPipelineOverallCompleteness._pipelineReportAge
+ _OBJC_IVAR_$_CSIndexingPipelineOverallCompletenessForBundle._bundleID
+ _OBJC_IVAR_$_CSIndexingPipelineOverallCompletenessForBundle._donationProgress
+ _OBJC_IVAR_$_CSIndexingPipelineOverallCompletenessForBundle._pipelineCompletenessFirstTimeBucket
+ _OBJC_IVAR_$_CSIndexingPipelineOverallCompletenessForBundle._pipelineCompletenessSecondBucket
+ _OBJC_IVAR_$_CSIndexingPipelineOverallCompletenessForBundle._pipelineCompletenessThirdBucket
+ _OBJC_IVAR_$_CSInlineDonation._addOrUpdateItems
+ _OBJC_IVAR_$_CSInlineDonation._associatedHTMLContent
+ _OBJC_IVAR_$_CSInlineDonation._associatedTextContent
+ _OBJC_IVAR_$_CSInlineDonation._clientStateName
+ _OBJC_IVAR_$_CSInlineDonation._deleteAllItems
+ _OBJC_IVAR_$_CSInlineDonation._deleteDomainIdentifiers
+ _OBJC_IVAR_$_CSInlineDonation._deleteItemIdentifiers
+ _OBJC_IVAR_$_CSInlineDonation._donationName
+ _OBJC_IVAR_$_CSInlineDonation._donationTimestamp
+ _OBJC_IVAR_$_CSInlineDonation._donationType
+ _OBJC_IVAR_$_CSInlineDonation._expectedClientState
+ _OBJC_IVAR_$_CSInlineDonation._isInlineCacheEnabled
+ _OBJC_IVAR_$_CSInlineDonation._itemsDataSize
+ _OBJC_IVAR_$_CSInlineDonation._sourceIdentifier
+ _OBJC_IVAR_$_CSInlineDonation._updatedClientState
+ _OBJC_IVAR_$_CSMockSearchableIndex._batchedDeletedIdentifiers
+ _OBJC_IVAR_$_CSMockSearchableIndex._batchedItems
+ _OBJC_IVAR_$_CSMockSearchableIndex._clientStates
+ _OBJC_IVAR_$_CSMockSearchableIndex._deletedInteractions
+ _OBJC_IVAR_$_CSMockSearchableIndex._deletedItems
+ _OBJC_IVAR_$_CSMockSearchableIndex._deletedUserActivities
+ _OBJC_IVAR_$_CSMockSearchableIndex._indexDelegate
+ _OBJC_IVAR_$_CSMockSearchableIndex._indexedItems
+ _OBJC_IVAR_$_CSMockSearchableIndex._interactions
+ _OBJC_IVAR_$_CSMockSearchableIndex._isInBatch
+ _OBJC_IVAR_$_CSMockSearchableIndex._name
+ _OBJC_IVAR_$_CSMockSearchableIndex._shouldSimulateErrors
+ _OBJC_IVAR_$_CSMockSearchableIndex._simulatedError
+ _OBJC_IVAR_$_CSMockSearchableIndex._userActivities
+ _OBJC_IVAR_$_CSPipelineCompletenessReport._bundleID
+ _OBJC_IVAR_$_CSPipelineCompletenessReport._eligibleItems
+ _OBJC_IVAR_$_CSPipelineCompletenessReport._pipeline
+ _OBJC_IVAR_$_CSPipelineCompletenessReport._pipelineCompleteness
+ _OBJC_IVAR_$_CSPipelineCompletenessReport._pipelineCompletenessFirstTimeBucket
+ _OBJC_IVAR_$_CSPipelineCompletenessReport._pipelineCompletenessHeuristicScore
+ _OBJC_IVAR_$_CSPipelineCompletenessReport._pipelineCompletenessSecondBucket
+ _OBJC_IVAR_$_CSPipelineCompletenessReport._pipelineCompletenessThirdBucket
+ _OBJC_IVAR_$_CSPipelineCompletenessReport._reportDate
+ _OBJC_IVAR_$_CSPipelineCompletenessReportStorage._storageURL
+ _OBJC_IVAR_$_CSPlace._fullyFormattedAddress
+ _OBJC_IVAR_$_CSPlace._latitude
+ _OBJC_IVAR_$_CSPlace._longitude
+ _OBJC_IVAR_$_CSPlace._namedLocation
+ _OBJC_IVAR_$_CSPowerHUD._biomeStream
+ _OBJC_IVAR_$_CSRecurrenceRule._daysOfTheWeek
+ _OBJC_IVAR_$_CSSearchQuery._logOwner
+ _OBJC_IVAR_$_CSSearchQueryContext._hasReadPurpose
+ _OBJC_IVAR_$_CSSearchQueryContext._logToken
+ _OBJC_IVAR_$_CSSearchQueryContext._mailQueryID
+ _OBJC_IVAR_$_CSTestSearchableIndex._user
+ _OBJC_METACLASS_$_CSDonationProgress
+ _OBJC_METACLASS_$_CSDonationProgressFailure
+ _OBJC_METACLASS_$_CSDonationProgressQueryResult
+ _OBJC_METACLASS_$_CSIndexingPipelineOverallCompleteness
+ _OBJC_METACLASS_$_CSIndexingPipelineOverallCompletenessForBundle
+ _OBJC_METACLASS_$_CSInlineDonation
+ _OBJC_METACLASS_$_CSMockSearchableIndex
+ _OBJC_METACLASS_$_CSPipelineCompletenessReport
+ _OBJC_METACLASS_$_CSPipelineCompletenessReportStorage
+ _OBJC_METACLASS_$_CSPlace
+ _OBJC_METACLASS_$_CSPowerHUD
+ _OBJC_METACLASS_$_CSRecurrenceRule
+ _OBJC_METACLASS_$_CSTestIndexConnection
+ _OBJC_METACLASS_$_CSTestSearchQuery
+ _OBJC_METACLASS_$_CSTestSearchableIndex
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _SSDefaultsGetAssetPathForLocalizedKeywords
+ _SSDefaultsGetAssetPathForLocalizedKeywords.cold.1
+ _UTTypeDirectory
+ _UTTypeEmailMessage
+ _UTTypeFolder
+ _UTTypeItem
+ _UTTypeMessage
+ __MDPlistContainerCreateWithBytesAndDeallocator
+ __MDPlistGetRootPlistObjectFromPlist
+ __OBJC_$_CLASS_METHODS_CSDonationProgress
+ __OBJC_$_CLASS_METHODS_CSDonationProgressFailure
+ __OBJC_$_CLASS_METHODS_CSIndexingPipelineOverallCompleteness
+ __OBJC_$_CLASS_METHODS_CSIndexingPipelineOverallCompletenessForBundle
+ __OBJC_$_CLASS_METHODS_CSInlineDonation
+ __OBJC_$_CLASS_METHODS_CSMockSearchableIndex
+ __OBJC_$_CLASS_METHODS_CSPipelineCompletenessReport
+ __OBJC_$_CLASS_METHODS_CSPipelineCompletenessReportStorage
+ __OBJC_$_CLASS_METHODS_CSPlace
+ __OBJC_$_CLASS_METHODS_CSPowerHUD
+ __OBJC_$_CLASS_METHODS_CSRecurrenceRule
+ __OBJC_$_CLASS_METHODS_CSSearchConnection(InternalTestIndex)
+ __OBJC_$_CLASS_METHODS_CSSearchableIndex(InternalSPI|SpotlightCache|SpotlightKnowledge)
+ __OBJC_$_CLASS_METHODS_CSSearchableItemAttributeSet(CSAttributes|CSQuery|CSPrivateAttributes|CSMediaAnalysis_Private|CSWallet_Private|CSMail_Private|CSSafari_Private|CSFileProvider_Private|CSInteraction_private|CSAppDemotion_Private|CSNews_Private|CSPortrait_Private|CSPhone_Private|CSPhotos_Private|CSMotion|CSMessages_Private|CSNotifications_Private|CSAddressBook_Private|Containment|EventsExtras|CSCustomAttributes|CSCoderAdditions|CSEvent_Flight|CSEvent_Hotel|SwiftUI_Archiving|CSEvent_Restaurant|CSEvent_Generic|CSCard|CSContact|AppEntity|CSEmbeddingVector|AllEventTypes|CSClock_Private|CSInterfaces|MessagesSharedLink|EventType)
+ __OBJC_$_CLASS_METHODS_CSTestIndexConnection
+ __OBJC_$_CLASS_METHODS_CSTestSearchableIndex
+ __OBJC_$_CLASS_METHODS_CSUserQuery(CSSuggestionBlending)
+ __OBJC_$_CLASS_PROP_LIST_CSDonationProgress
+ __OBJC_$_CLASS_PROP_LIST_CSDonationProgressFailure
+ __OBJC_$_CLASS_PROP_LIST_CSIndexingPipelineOverallCompleteness
+ __OBJC_$_CLASS_PROP_LIST_CSIndexingPipelineOverallCompletenessForBundle
+ __OBJC_$_CLASS_PROP_LIST_CSPipelineCompletenessReport
+ __OBJC_$_CLASS_PROP_LIST_CSPlace
+ __OBJC_$_CLASS_PROP_LIST_CSRecurrenceRule
+ __OBJC_$_INSTANCE_METHODS_CSDonationProgress(CSCoderAdditions)
+ __OBJC_$_INSTANCE_METHODS_CSDonationProgressFailure(CSCoderAdditions)
+ __OBJC_$_INSTANCE_METHODS_CSDonationProgressQueryResult
+ __OBJC_$_INSTANCE_METHODS_CSIndexingPipelineOverallCompleteness
+ __OBJC_$_INSTANCE_METHODS_CSIndexingPipelineOverallCompletenessForBundle
+ __OBJC_$_INSTANCE_METHODS_CSInlineDonation
+ __OBJC_$_INSTANCE_METHODS_CSMockSearchableIndex
+ __OBJC_$_INSTANCE_METHODS_CSPipelineCompletenessReport
+ __OBJC_$_INSTANCE_METHODS_CSPipelineCompletenessReportStorage
+ __OBJC_$_INSTANCE_METHODS_CSPlace
+ __OBJC_$_INSTANCE_METHODS_CSPowerHUD
+ __OBJC_$_INSTANCE_METHODS_CSRecurrenceRule
+ __OBJC_$_INSTANCE_METHODS_CSSearchableIndex(InternalSPI|SpotlightCache|SpotlightKnowledge)
+ __OBJC_$_INSTANCE_METHODS_CSSearchableItemAttributeSet(CSAttributes|CSQuery|CSPrivateAttributes|CSMediaAnalysis_Private|CSWallet_Private|CSMail_Private|CSSafari_Private|CSFileProvider_Private|CSInteraction_private|CSAppDemotion_Private|CSNews_Private|CSPortrait_Private|CSPhone_Private|CSPhotos_Private|CSMotion|CSMessages_Private|CSNotifications_Private|CSAddressBook_Private|Containment|EventsExtras|CSCustomAttributes|CSCoderAdditions|CSEvent_Flight|CSEvent_Hotel|SwiftUI_Archiving|CSEvent_Restaurant|CSEvent_Generic|CSCard|CSContact|AppEntity|CSEmbeddingVector|AllEventTypes|CSClock_Private|CSInterfaces|MessagesSharedLink|EventType)
+ __OBJC_$_INSTANCE_METHODS_CSTestSearchQuery
+ __OBJC_$_INSTANCE_METHODS_CSTestSearchableIndex
+ __OBJC_$_INSTANCE_METHODS_CSUserQuery
+ __OBJC_$_INSTANCE_VARIABLES_CSDonationProgress
+ __OBJC_$_INSTANCE_VARIABLES_CSDonationProgressFailure
+ __OBJC_$_INSTANCE_VARIABLES_CSDonationProgressQueryResult
+ __OBJC_$_INSTANCE_VARIABLES_CSIndexingPipelineOverallCompleteness
+ __OBJC_$_INSTANCE_VARIABLES_CSIndexingPipelineOverallCompletenessForBundle
+ __OBJC_$_INSTANCE_VARIABLES_CSInlineDonation
+ __OBJC_$_INSTANCE_VARIABLES_CSMockSearchableIndex
+ __OBJC_$_INSTANCE_VARIABLES_CSPipelineCompletenessReport
+ __OBJC_$_INSTANCE_VARIABLES_CSPipelineCompletenessReportStorage
+ __OBJC_$_INSTANCE_VARIABLES_CSPlace
+ __OBJC_$_INSTANCE_VARIABLES_CSPowerHUD
+ __OBJC_$_INSTANCE_VARIABLES_CSRecurrenceRule
+ __OBJC_$_INSTANCE_VARIABLES_CSTestSearchableIndex
+ __OBJC_$_PROP_LIST_CSDonationProgress
+ __OBJC_$_PROP_LIST_CSDonationProgressFailure
+ __OBJC_$_PROP_LIST_CSDonationProgressQueryResult
+ __OBJC_$_PROP_LIST_CSIndexingPipelineOverallCompleteness
+ __OBJC_$_PROP_LIST_CSIndexingPipelineOverallCompletenessForBundle
+ __OBJC_$_PROP_LIST_CSInlineDonation
+ __OBJC_$_PROP_LIST_CSMockSearchableIndex
+ __OBJC_$_PROP_LIST_CSPipelineCompletenessReport
+ __OBJC_$_PROP_LIST_CSPlace
+ __OBJC_$_PROP_LIST_CSPowerHUD
+ __OBJC_$_PROP_LIST_CSRecurrenceRule
+ __OBJC_$_PROTOCOL_REFS_DonationProgressReporting
+ __OBJC_CLASS_PROTOCOLS_$_CSDonationProgress(CSCoderAdditions)
+ __OBJC_CLASS_PROTOCOLS_$_CSDonationProgressFailure(CSCoderAdditions)
+ __OBJC_CLASS_PROTOCOLS_$_CSIndexingPipelineOverallCompleteness
+ __OBJC_CLASS_PROTOCOLS_$_CSIndexingPipelineOverallCompletenessForBundle
+ __OBJC_CLASS_PROTOCOLS_$_CSPipelineCompletenessReport
+ __OBJC_CLASS_PROTOCOLS_$_CSPlace
+ __OBJC_CLASS_PROTOCOLS_$_CSRecurrenceRule
+ __OBJC_CLASS_RO_$_CSDonationProgress
+ __OBJC_CLASS_RO_$_CSDonationProgressFailure
+ __OBJC_CLASS_RO_$_CSDonationProgressQueryResult
+ __OBJC_CLASS_RO_$_CSIndexingPipelineOverallCompleteness
+ __OBJC_CLASS_RO_$_CSIndexingPipelineOverallCompletenessForBundle
+ __OBJC_CLASS_RO_$_CSInlineDonation
+ __OBJC_CLASS_RO_$_CSMockSearchableIndex
+ __OBJC_CLASS_RO_$_CSPipelineCompletenessReport
+ __OBJC_CLASS_RO_$_CSPipelineCompletenessReportStorage
+ __OBJC_CLASS_RO_$_CSPlace
+ __OBJC_CLASS_RO_$_CSPowerHUD
+ __OBJC_CLASS_RO_$_CSRecurrenceRule
+ __OBJC_CLASS_RO_$_CSTestIndexConnection
+ __OBJC_CLASS_RO_$_CSTestSearchQuery
+ __OBJC_CLASS_RO_$_CSTestSearchableIndex
+ __OBJC_LABEL_PROTOCOL_$_DonationProgressReporting
+ __OBJC_METACLASS_RO_$_CSDonationProgress
+ __OBJC_METACLASS_RO_$_CSDonationProgressFailure
+ __OBJC_METACLASS_RO_$_CSDonationProgressQueryResult
+ __OBJC_METACLASS_RO_$_CSIndexingPipelineOverallCompleteness
+ __OBJC_METACLASS_RO_$_CSIndexingPipelineOverallCompletenessForBundle
+ __OBJC_METACLASS_RO_$_CSInlineDonation
+ __OBJC_METACLASS_RO_$_CSMockSearchableIndex
+ __OBJC_METACLASS_RO_$_CSPipelineCompletenessReport
+ __OBJC_METACLASS_RO_$_CSPipelineCompletenessReportStorage
+ __OBJC_METACLASS_RO_$_CSPlace
+ __OBJC_METACLASS_RO_$_CSPowerHUD
+ __OBJC_METACLASS_RO_$_CSRecurrenceRule
+ __OBJC_METACLASS_RO_$_CSTestIndexConnection
+ __OBJC_METACLASS_RO_$_CSTestSearchQuery
+ __OBJC_METACLASS_RO_$_CSTestSearchableIndex
+ __OBJC_PROTOCOL_$_DonationProgressReporting
+ __ZGVZN28CSQueryAttributeMappingTable11in_word_setEPKcjE8wordlist
+ __ZL14create_AMArrayPPKv
+ __ZN28CSQueryAttributeMappingTable11in_word_setEPKcj
+ __ZNSt11logic_errorC2EPKc
+ __ZNSt12length_errorC1B9foe210106EPKc
+ __ZNSt12length_errorD1Ev
+ __ZNSt20bad_array_new_lengthC1Ev
+ __ZNSt20bad_array_new_lengthD1Ev
+ __ZNSt3__120__throw_length_errorB9foe210106EPKc
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__16vectorIN12_GLOBAL__N_18WorkItemENS_9allocatorIS2_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__19__sift_upB9foe210106INS_17_ClassicAlgPolicyERN12_GLOBAL__N_118WorkItemComparatorENS_11__wrap_iterIPNS2_8WorkItemEEEEEvT1_S9_OT0_NS_15iterator_traitsIS9_E15difference_typeE
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
+ __ZTISt12length_error
+ __ZTISt20bad_array_new_length
+ __ZTVSt12length_error
+ __ZZ41+[CSRequestQueue _requestQueueAttribute:]E18shouldPropagateQos
+ __ZZ41+[CSRequestQueue _requestQueueAttribute:]E9onceToken
+ __ZZN28CSQueryAttributeMappingTable11in_word_setEPKcjE8wordlist
+ __ZdlPv
+ __ZnwmSt19__type_descriptor_t
+ ___102+[CSPersonalAnswers isEventIntentForQueryUnderstandingOutput:isSearchToolClient:isSearchToolCerberus:]_block_invoke
+ ___102-[CSMockSearchableIndex provideDataForBundle:itemIdentifier:typeIdentifier:options:completionHandler:]_block_invoke
+ ___105-[CSMockSearchableIndex provideFileURLForBundle:itemIdentifier:typeIdentifier:options:completionHandler:]_block_invoke
+ ___107-[CSMockSearchableIndex provideFileURLsForBundle:itemIdentifiers:typeIdentifier:options:completionHandler:]_block_invoke
+ ___114-[CSMockSearchableIndex fetchAttributes:protectionClass:bundleID:identifiers:userCtx:flags:qos:completionHandler:]_block_invoke
+ ___126-[CSMockSearchableIndex fetchCacheFileDescriptorsForProtectionClass:bundleID:identifiers:userCtx:flags:qos:completionHandler:]_block_invoke
+ ___131-[CSSearchableIndex endIndexBatchWithExpectedClientState:newClientState:critical:reason:updatingDonationProgres:completionHandler:]_block_invoke
+ ___131-[CSSearchableIndex endIndexBatchWithExpectedClientState:newClientState:critical:reason:updatingDonationProgres:completionHandler:]_block_invoke_2
+ ___192-[CSMockSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:protectionClass:forBundleID:options:reason:completionHandler:]_block_invoke
+ ___21-[CSSearchQuery poll]_block_invoke.1101
+ ___21-[CSSearchQuery poll]_block_invoke.cold.1
+ ___213-[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:updatingDonationProgress:protectionClass:forBundleID:options:reason:completionHandler:]_block_invoke
+ ___213-[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:updatingDonationProgress:protectionClass:forBundleID:options:reason:completionHandler:]_block_invoke.210
+ ___213-[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:updatingDonationProgress:protectionClass:forBundleID:options:reason:completionHandler:]_block_invoke_2
+ ___213-[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:updatingDonationProgress:protectionClass:forBundleID:options:reason:completionHandler:]_block_invoke_2.212
+ ___28+[CSPowerHUD sharedInstance]_block_invoke
+ ___30+[CSInlineDonation translator]_block_invoke
+ ___31+[CSInlineDonation sharedQueue]_block_invoke
+ ___34-[CSSearchConnection cancelQuery:]_block_invoke.1528
+ ___34-[CSSearchConnection cancelQuery:]_block_invoke.1528.cold.1
+ ___36-[CSSearchQuery processResultItems:]_block_invoke.1178
+ ___41-[CSInlineDonation performDonationAsync:]_block_invoke
+ ___46-[CSFileProviderDomainMonitor startMonitoring]_block_invoke.27
+ ___46-[CSFileProviderDomainMonitor startMonitoring]_block_invoke.29
+ ___46-[CSFileProviderDomainMonitor startMonitoring]_block_invoke_2.28
+ ___46-[CSSearchQuery setupFetchAttributesForSearch]_block_invoke
+ ___47+[CSMockSearchableIndex defaultSearchableIndex]_block_invoke
+ ___47+[CSTestIndexConnection testConnectionForUser:]_block_invoke
+ ___47+[CSTestSearchableIndex defaultSearchableIndex]_block_invoke
+ ___54-[CSSearchQuery copyResultsFromPlist:protectionClass:]_block_invoke.1135
+ ___55-[FPProviderDomain(Private) isSpecialPhotosEmptyDomain]_block_invoke
+ ___56-[CSSearchableIndex(SpotlightKnowledge) indexDirectory:]_block_invoke
+ ___57+[CSPowerHUD getSpotlightOperationsDataWithTimeInterval:]_block_invoke
+ ___57+[CSPowerHUD getSpotlightOperationsDataWithTimeInterval:]_block_invoke_2
+ ___57-[CSMockSearchableIndex _issueCommand:completionHandler:]_block_invoke
+ ___60-[CSMockSearchableIndex _openJournalFile:completionHandler:]_block_invoke
+ ___61+[CSSearchConnection(InternalTestIndex) testSearchConnection]_block_invoke
+ ___62-[CSMockSearchableIndex _fetchBundleIDsWithCompletionHandler:]_block_invoke
+ ___62-[CSSearchableIndex reportDonationProgress:completionHandler:]_block_invoke
+ ___62-[CSSearchableIndex reportDonationProgress:completionHandler:]_block_invoke_2
+ ___62-[CSSearchableIndex reportDonationProgress:completionHandler:]_block_invoke_3
+ ___62-[CSSearchableIndex reportDonationProgress:completionHandler:]_block_invoke_4
+ ___65-[CSMockSearchableIndex _photosLibraryDeleted:completionHandler:]_block_invoke
+ ___65-[CSSearchableIndex textContentCompletenessForBundle:completion:]_block_invoke
+ ___67+[CSSearchQuery fetchDonationProgressForBundles:completionHandler:]_block_invoke
+ ___67+[CSSearchQuery fetchDonationProgressForBundles:completionHandler:]_block_invoke.1233
+ ___67-[CSMockSearchableIndex _issueDiagnose:logQuery:completionHandler:]_block_invoke
+ ___67-[CSMockSearchableIndex embeddingCompletenessForBundle:completion:]_block_invoke
+ ___67-[CSSearchableItem(Internal) _standardizeExtractedNumericEntities:]_block_invoke.298
+ ___67-[CSSearchableItem(Internal) _standardizeExtractedNumericEntities:]_block_invoke.316
+ ___72-[CSSearchableIndex fetchConsumedAndLatestSerialNums:completionHandler:]_block_invoke
+ ___74-[CSSearchableItemAttributeSet(AllEventTypes) getAllUniqueEventAttributes]_block_invoke
+ ___76-[CSSearchableIndex performIndexJob:protectionClass:acknowledgementHandler:]_block_invoke.331
+ ___80-[CSSearchQuery filterMegadomePeopleSuggestions:isShortQuery:completionHandler:]_block_invoke.1147
+ ___80-[CSSearchableIndex fetchIndexingPipelineOverallCompleteness:completionHandler:]_block_invoke
+ ___80-[CSSearchableIndex fetchIndexingPipelineOverallCompleteness:completionHandler:]_block_invoke_2
+ ___80-[CSSearchableIndex fetchIndexingPipelineOverallCompleteness:completionHandler:]_block_invoke_3
+ ___84-[CSMockSearchableIndex indexSearchableItems:returningItemsSanitizedForSpotlightTo:]_block_invoke
+ ___84-[CSSearchableIndex fetchIndexingPipelineCompleteness:forBundles:completionHandler:]_block_invoke
+ ___84-[CSSearchableIndex fetchIndexingPipelineCompleteness:forBundles:completionHandler:]_block_invoke_2
+ ___84-[CSSearchableIndex fetchIndexingPipelineCompleteness:forBundles:completionHandler:]_block_invoke_3
+ ___88-[CSSearchQuery didReturnResults:resultsData:oidData:protectionClass:completionHandler:]_block_invoke.cold.5
+ ___99-[CSSearchableIndex _fetchCacheFileDescriptorsForProtectionClass:bundleID:items:completionHandler:]_block_invoke.401
+ ___Block_byref_object_copy_.399
+ ___Block_byref_object_dispose_.400
+ ___CascadeSetsLibraryCore_block_invoke
+ ___LinkServicesLibraryCore_block_invoke
+ ___SSDefaultsGetAssetPathForLocalizedKeywords_block_invoke
+ ___block_descriptor_110_e8_32s40s48s56s_e8_v16?0Q8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_118_e8_32s40s48s56s64r_e13_v24?0^8^B16ls32l8r64l8s40l8s48l8s56l8
+ ___block_descriptor_118_e8_32s40s48s56s64r_e8_v16?0Q8lr64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_122_e8_32s40s48s56r_e13_v24?0^8^B16ls32l8r56l8s40l8s48l8
+ ___block_descriptor_145_e8_32s40s48s56s64s72s80s88s96s104s112s120bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8
+ ___block_descriptor_217_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160w_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8s136l8s144l8s152l8w160l8
+ ___block_descriptor_40_e8_32r_e22_v16?0"BMStoreEvent"8lr32l8
+ ___block_descriptor_40_e8_32s_e23_v16?0"BPSCompletion"8ls32l8
+ ___block_descriptor_40_e8_32s_e26_v48?0r*8Q16{?=*Q{?=IC}}24ls32l8
+ ___block_descriptor_48_e8_32bs40r_e28_v24?0"NSData"8"NSError"16lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e25_v32?0"NSString"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSArray"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40r48r56r64r_e11_B20?0Q8B16ls32l8r40l8r48l8r56l8r64l8
+ ___block_descriptor_73_e8_32s40s48s56w_e5_v8?0ls32l8s40l8s48l8w56l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72w_e5_v8?0ls32l8s40l8s48l8s56l8s64l8w72l8
+ ___block_descriptor_96_e8_32s40s48s56s_e59_"CSExternalAnalysisTag"40?0Q8"NSString"16"NSArray"24d32ls32l8s40l8s48l8s56l8
+ ___block_descriptor_97_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_99_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
+ ___block_literal_global.1004
+ ___block_literal_global.1008
+ ___block_literal_global.1059
+ ___block_literal_global.1104
+ ___block_literal_global.1110
+ ___block_literal_global.15
+ ___block_literal_global.1502
+ ___block_literal_global.1504
+ ___block_literal_global.1506
+ ___block_literal_global.1509
+ ___block_literal_global.1512
+ ___block_literal_global.1622
+ ___block_literal_global.1624
+ ___block_literal_global.1626
+ ___block_literal_global.1640
+ ___block_literal_global.1642
+ ___block_literal_global.1644
+ ___block_literal_global.198
+ ___block_literal_global.2061
+ ___block_literal_global.250
+ ___block_literal_global.252
+ ___block_literal_global.254
+ ___block_literal_global.256
+ ___block_literal_global.263
+ ___block_literal_global.2654
+ ___block_literal_global.2682
+ ___block_literal_global.2700
+ ___block_literal_global.2726
+ ___block_literal_global.291
+ ___block_literal_global.300
+ ___block_literal_global.301
+ ___block_literal_global.318
+ ___block_literal_global.330
+ ___block_literal_global.364
+ ___block_literal_global.506
+ ___block_literal_global.520
+ ___block_literal_global.574
+ ___block_literal_global.725
+ ___block_literal_global.747
+ ___block_literal_global.835
+ ___block_literal_global.84
+ ___block_literal_global.884
+ ___block_literal_global.898
+ ___block_literal_global.906
+ ___block_literal_global.994
+ ___createKeywordDictionaryFromMDPlistObject_block_invoke
+ ___createKeywordDictionaryFromMDPlistObject_block_invoke.cold.1
+ ___cxa_allocate_exception
+ ___cxa_free_exception
+ ___cxa_guard_abort
+ ___cxa_throw
+ ___fetchMailVIPList_block_invoke.575
+ ___fetchMailVIPList_block_invoke.575.cold.1
+ ___fetchMailVIPList_block_invoke.575.cold.2
+ ___getCCItemErrorDomainSymbolLoc_block_invoke
+ ___getCCItemFieldPredicateClass_block_invoke
+ ___getCCItemFieldPredicateClass_block_invoke.cold.1
+ ___getCCSetDescriptorClass_block_invoke
+ ___getCCSetDescriptorClass_block_invoke.cold.1
+ ___getCCSetDonationClass_block_invoke
+ ___getCCSetDonationClass_block_invoke.cold.1
+ ___getCCSetErrorDomainSymbolLoc_block_invoke
+ ___getLNSpotlightCascadeTranslatorClass_block_invoke
+ ___getLNSpotlightCascadeTranslatorClass_block_invoke.cold.1
+ ___gxx_personality_v0
+ ___loadLocalizedEventTypeFromSRA_block_invoke
+ ___loadLocalizedEventTypeFromSRA_block_invoke.2727
+ ___loadLocalizedEventTypeFromSRA_block_invoke.cold.1
+ ___loadLocalizedEventTypeFromSRA_block_invoke.cold.2
+ ___loadLocalizedEventTypeFromSRA_block_invoke.cold.3
+ ___loadLocalizedMessagesSharedLinksFromSRA_block_invoke
+ ___loadLocalizedMessagesSharedLinksFromSRA_block_invoke.2683
+ ___loadLocalizedMessagesSharedLinksFromSRA_block_invoke.cold.1
+ ___loadLocalizedMessagesSharedLinksFromSRA_block_invoke.cold.2
+ ___loadLocalizedMessagesSharedLinksFromSRA_block_invoke.cold.3
+ ___messagesResources_block_invoke
+ ___messagesResources_block_invoke.cold.1
+ ___messagesResources_block_invoke.cold.2
+ ___messagesResources_block_invoke.cold.3
+ ___messagesResources_block_invoke.cold.4
+ ___messagesResources_block_invoke.cold.5
+ __md_fd_token_valid
+ __md_fd_token_write
+ __md_log_release_fd
+ __md_log_retain_fd
+ __md_utf8_cstr
+ __overrideDefaultSearchableIndexForTestingWithDoSet:searchableIndex:.defaultIndex
+ __overrideDefaultSearchableIndexForTestingWithDoSet:searchableIndex:.lock
+ __swizzleDefaultSearchableIndexWithDoSwizzle:.lock
+ __swizzleDefaultSearchableIndexWithDoSwizzle:.originalImp
+ _audit_stringCascadeSets
+ _audit_stringLinkServices
+ _class_getClassMethod
+ _createKeywordDictionaryFromMDPlistObject
+ _defaultSearchableIndex.onceToken.813
+ _defaultSearchableIndex.onceToken.820
+ _defaultSearchableIndex.sDefaultInstance.812
+ _defaultSearchableIndex.sDefaultInstance.819
+ _gCSQueryAttributeMappingArrayCount
+ _gCSQueryAttributeMappingArrayEntries
+ _getAllUniqueEventAttributes.deduplicatedArray
+ _getAllUniqueEventAttributes.onceToken
+ _getCCItemErrorDomainSymbolLoc.ptr
+ _getCCItemFieldPredicateClass.softClass
+ _getCCSetDescriptorClass.softClass
+ _getCCSetDonationClass
+ _getCCSetDonationClass.softClass
+ _getCCSetErrorDomainSymbolLoc.ptr
+ _getLNSpotlightCascadeTranslatorClass.softClass
+ _getSpotlightDataExpiration
+ _isEventIntentForQueryUnderstandingOutput:isSearchToolClient:isSearchToolCerberus:.isDebugLoggingEnabled
+ _isEventIntentForQueryUnderstandingOutput:isSearchToolClient:isSearchToolCerberus:.onceToken
+ _isSpecialPhotosEmptyDomain.once
+ _isSpecialPhotosEmptyDomain.photosProviderID
+ _isSpecialPhotosEmptyDomain.photosSpecialDomainIDs
+ _isSpotlightDataExpired
+ _kSpotlightDataExpirationInterval
+ _kSpotlightDataExpirationKey
+ _loadLocalizedEventTypeFromSRA.onceToken
+ _loadLocalizedMessagesSharedLinksFromSRA.onceToken
+ _localizedKMDItemCardSubType
+ _localizedKMDItemCardType
+ _localizedKMDItemEventRestaurantMealType
+ _localizedKMDItemEventStatus
+ _localizedKMDItemEventSubType
+ _localizedLinkSubTypes
+ _localizedLinkTypes
+ _localizedPrefix
+ _messagesResources.onceMessagesResourcesToken
+ _messagesResources.sMessagesResources
+ _method_exchangeImplementations
+ _method_getImplementation
+ _method_setImplementation
+ _objc_msgSend$Operations
+ _objc_msgSend$Spotlight
+ _objc_msgSend$URLByAppendingPathComponent:
+ _objc_msgSend$_addOrUpdateItem:withIdentifier:donation:error:
+ _objc_msgSend$_createStorageDirectoryIfNotExistsWithError:
+ _objc_msgSend$_fileURLForPipeline:
+ _objc_msgSend$_getTimeComponentsForKey:
+ _objc_msgSend$_inlineDonationWithOverrideBundleID:protectionClass:addOrUpdateItems:associatedTextContent:associatedHTMLContent:deleteItemIdentifiers:deleteDomainIdentifiers:deleteAllItems:clientStateName:updatedClientState:expectedClientState:itemsDataSize:options:donationType:
+ _objc_msgSend$_logErrorWithCode:description:underlying:
+ _objc_msgSend$_overrideDefaultSearchableIndexForTestingWithDoSet:searchableIndex:
+ _objc_msgSend$_parentTypes
+ _objc_msgSend$_perform:
+ _objc_msgSend$_reportErrorWithCode:clientDescription:donationErrorCode:underlying:
+ _objc_msgSend$_resolveDonationName
+ _objc_msgSend$_setTimeComponentsForKey:time:
+ _objc_msgSend$_standardizePlaces:
+ _objc_msgSend$_swizzleDefaultSearchableIndexWithDoSwizzle:
+ _objc_msgSend$_updateRevisionToken:error:
+ _objc_msgSend$addOrUpdateItem:error:
+ _objc_msgSend$alarmRecurrenceRule
+ _objc_msgSend$alarmTime
+ _objc_msgSend$allKnownItems
+ _objc_msgSend$biomeStream
+ _objc_msgSend$client
+ _objc_msgSend$containsIndex:
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$dataWithContentsOfURL:options:error:
+ _objc_msgSend$dateOfNewestUndonatedItem
+ _objc_msgSend$daysOfTheWeek
+ _objc_msgSend$deleteSearchableItemsWithIdentifiers:completionHandler:
+ _objc_msgSend$designateAsFullSet
+ _objc_msgSend$donatedItems
+ _objc_msgSend$donationCompeleteness
+ _objc_msgSend$donationProgress
+ _objc_msgSend$donationTimestamp
+ _objc_msgSend$encodeInt64:
+ _objc_msgSend$encodeString:
+ _objc_msgSend$endIndexBatchWithExpectedClientState:newClientState:critical:reason:updatingDonationProgres:completionHandler:
+ _objc_msgSend$errorOrNoopWithCompletionHandler:
+ _objc_msgSend$errorUnsupportedWithCompletionHandler:
+ _objc_msgSend$eventBody
+ _objc_msgSend$failureReason
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$finish:
+ _objc_msgSend$fullyFormattedAddress
+ _objc_msgSend$getReturnValue:
+ _objc_msgSend$groupIdentifier
+ _objc_msgSend$hasReadPurpose
+ _objc_msgSend$indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:clientStateName:updatingDonationProgress:protectionClass:forBundleID:options:reason:completionHandler:
+ _objc_msgSend$indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:updatingDonationProgress:protectionClass:forBundleID:options:reason:completionHandler:
+ _objc_msgSend$indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:updatingDonationProgress:protectionClass:forBundleID:options:reason:completionHandler:
+ _objc_msgSend$indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:updatingDonationProgress:protectionClass:forBundleID:options:reason:completionHandler:
+ _objc_msgSend$indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:updatingDonationProgress:reason:completionHandler:
+ _objc_msgSend$indexSearchableItems:updatingDonationProgress:completionHandler:
+ _objc_msgSend$initWithAddress:synonyms:code:confidence:
+ _objc_msgSend$initWithAddress:synonyms:code:type:lat:lng:confidence:
+ _objc_msgSend$initWithAllKnownItems:itemsNeedingDonation:donatedItems:partiallyDonatedItems:itemsNeedingDonationForRedonationRequests:dateOfNewestUndonatedItem:
+ _objc_msgSend$initWithBase64EncodedString:options:
+ _objc_msgSend$initWithBundleID:indexName:status:donationProgress:
+ _objc_msgSend$initWithClient:itemsCount:operation:reason:stringIdentifier:stringReason:
+ _objc_msgSend$initWithContentsOfFile:options:error:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$initWithDaysOfTheWeek:
+ _objc_msgSend$initWithFailureReason:underlyingError:
+ _objc_msgSend$initWithFullyFormattedAddress:namedLocation:
+ _objc_msgSend$initWithLatitude:longitude:fullyFormattedAddress:namedLocation:
+ _objc_msgSend$initWithNamedLocation:
+ _objc_msgSend$initWithPipeline:overallCompleteness:donationCompeleteness:pipelineCompleteness:pipelineCompletenessHeuristicScore:pipelineReportAge:
+ _objc_msgSend$initWithSourceIdentifier:addOrUpdateItems:associatedTextContent:associatedHTMLContent:deleteItemIdentifiers:deleteDomainIdentifiers:deleteAllItems:clientStateName:updatedClientState:expectedClientState:itemsDataSize:donationType:
+ _objc_msgSend$initWithStartDate:endDate:maxEvents:lastN:reversed:
+ _objc_msgSend$initWithStorageURL:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$inlineAddOrUpdateItems:associatedTextContent:associatedHTMLContent:deleteItemIdentifiers:overrideBundleID:protectionClass:clientStateName:updatedClientState:expectedClientState:itemsDataSize:options:
+ _objc_msgSend$inlineDeleteAllItemsWithOverrideBundleID:protectionClass:options:
+ _objc_msgSend$inlineDeleteDomainIdentifiers:overrideBundleID:protectionClass:options:
+ _objc_msgSend$isAllowedClientBundleIdentifier:
+ _objc_msgSend$isInlineCascadeDonationEnabled
+ _objc_msgSend$isInlineDocumentCacheEnabledForBundleID:
+ _objc_msgSend$isInstantAnswerTriggerQuery:isCJK:isSearchToolClient:
+ _objc_msgSend$isSpecialPhotosEmptyDomain
+ _objc_msgSend$isSufficientlyComplete
+ _objc_msgSend$itemsCount
+ _objc_msgSend$itemsDataSize
+ _objc_msgSend$itemsNeedingDonation
+ _objc_msgSend$itemsNeedingDonationForRedonationRequests
+ _objc_msgSend$latitude
+ _objc_msgSend$loadAllParametersForClient:locale:options:
+ _objc_msgSend$logToken
+ _objc_msgSend$longitude
+ _objc_msgSend$mailQueryID
+ _objc_msgSend$mailResultScoreL2
+ _objc_msgSend$namedLocation
+ _objc_msgSend$now
+ _objc_msgSend$null
+ _objc_msgSend$operation
+ _objc_msgSend$overallCompleteness
+ _objc_msgSend$partiallyDonatedItems
+ _objc_msgSend$performDonationAsync:
+ _objc_msgSend$persistentIdentifier
+ _objc_msgSend$pipeline
+ _objc_msgSend$pipelineCompleteness
+ _objc_msgSend$pipelineCompletenessFirstTimeBucket
+ _objc_msgSend$pipelineCompletenessHeuristicScore
+ _objc_msgSend$pipelineCompletenessSecondBucket
+ _objc_msgSend$pipelineCompletenessThirdBucket
+ _objc_msgSend$pipelineReportAge
+ _objc_msgSend$place
+ _objc_msgSend$predicateWithFieldType:equalsStringValue:error:
+ _objc_msgSend$priorRevisionTokenWithKey:
+ _objc_msgSend$processWorkItemsUpToRequestID:
+ _objc_msgSend$publisherWithUseCase:options:
+ _objc_msgSend$reminderRecurrenceRule
+ _objc_msgSend$reminderTime
+ _objc_msgSend$removeItemWithSourceItemIdentifier:error:
+ _objc_msgSend$removeItemsMatchingPredicate:error:
+ _objc_msgSend$requestID
+ _objc_msgSend$reset
+ _objc_msgSend$scanHexLongLong:
+ _objc_msgSend$scannerWithString:
+ _objc_msgSend$sendEvent:
+ _objc_msgSend$setAlarmRecurrenceRule:
+ _objc_msgSend$setBiomeStream:
+ _objc_msgSend$setDaysOfTheWeek:
+ _objc_msgSend$setFoundSuggestionsHandler:
+ _objc_msgSend$setFullyFormattedAddress:
+ _objc_msgSend$setHasReadPurpose:
+ _objc_msgSend$setLatitude:
+ _objc_msgSend$setLogToken:
+ _objc_msgSend$setLongitude:
+ _objc_msgSend$setMailQueryID:
+ _objc_msgSend$setNamedLocation:
+ _objc_msgSend$setReminderRecurrenceRule:
+ _objc_msgSend$sharedQueue
+ _objc_msgSend$sinkWithCompletion:receiveInput:
+ _objc_msgSend$source
+ _objc_msgSend$sourceIdentifier
+ _objc_msgSend$sourceIdentifierWithValue:error:
+ _objc_msgSend$startIncrementalSetDonationWithItemType:descriptors:options:error:
+ _objc_msgSend$stringIdentifier
+ _objc_msgSend$stringReason
+ _objc_msgSend$sufficientlyCompleteThreshold
+ _objc_msgSend$testConnectionForUser:
+ _objc_msgSend$testSearchConnection
+ _objc_msgSend$timeIntervalSinceNow
+ _objc_msgSend$timestamp
+ _objc_msgSend$translateItem:fromBundleId:error:
+ _objc_msgSend$translator
+ _objc_msgSend$unarchivedArrayOfObjectsOfClasses:fromData:error:
+ _objc_msgSend$underlyingError
+ _objc_msgSend$updateRevisionToken:withKey:error:
+ _objc_msgSend$writeToURL:options:error:
+ _objc_release_x10
+ _objc_terminate
+ _os_variant_has_internal_diagnostics
+ _sCSTestSearchConnection
+ _setupFetchAttributesForSearch.once
+ _sharedQueue.onceToken
+ _sharedQueue.sharedQueue
+ _sharedSearchConnection.onceToken
+ _testConnectionForUser:.onceToken
+ _testConnectionForUser:.sCSIndexConnection
+ _testSearchConnection.onceToken
+ _totalEnqueuedItemDataSize
+ _translator.onceToken
+ _translator.translator
- +[CSDonatedEvent eventFromData:]
- +[CSInstantAnswer dataFromInstantAnswers:]
- +[CSInstantAnswer dataFromInstantAnswers:].cold.1
- +[CSInstantAnswer instantAnswersFromData:]
- +[CSInstantAnswer instantAnswersFromData:].cold.1
- +[CSInstantAnswerAction actionWithType:andUrl:]
- +[CSInstantAnswers isInstantAnswerTriggerQuery:isCJK:isSearchTool:]
- +[CSPersonalAnswers personalAnswersEventIntentForQUOutput:isDebugLoggingEnabled:]
- +[CSPersonalAnswers personalAnswersEventIntentForQUOutput:isDebugLoggingEnabled:].cold.1
- -[CSAddressTag .cxx_destruct]
- -[CSDonatedEvent .cxx_destruct]
- -[CSDonatedEvent additionalInfo]
- -[CSDonatedEvent arrivalAirportCode]
- -[CSDonatedEvent arrivalAirportName]
- -[CSDonatedEvent arrivalDateTime]
- -[CSDonatedEvent arrivalTerminal]
- -[CSDonatedEvent attributes]
- -[CSDonatedEvent bookingInfoUrl]
- -[CSDonatedEvent checkInUrl]
- -[CSDonatedEvent confirmationNumber]
- -[CSDonatedEvent copyWithZone:]
- -[CSDonatedEvent courierName]
- -[CSDonatedEvent data]
- -[CSDonatedEvent deliveryDateTime]
- -[CSDonatedEvent departureAirportCode]
- -[CSDonatedEvent departureAirportName]
- -[CSDonatedEvent departureDateTime]
- -[CSDonatedEvent departureTerminal]
- -[CSDonatedEvent description]
- -[CSDonatedEvent docIDs]
- -[CSDonatedEvent flightCarrier]
- -[CSDonatedEvent flightNumber]
- -[CSDonatedEvent flightStatus]
- -[CSDonatedEvent fromAllowListedSender]
- -[CSDonatedEvent initWithAttributes:]
- -[CSDonatedEvent initWithData:]
- -[CSDonatedEvent initWithData:].cold.1
- -[CSDonatedEvent initWithType:]
- -[CSDonatedEvent merchantName]
- -[CSDonatedEvent mutableAttributes]
- -[CSDonatedEvent orderDateTime]
- -[CSDonatedEvent senderIsCourier]
- -[CSDonatedEvent setAdditionalInfo:]
- -[CSDonatedEvent setArrivalAirportCode:]
- -[CSDonatedEvent setArrivalAirportName:]
- -[CSDonatedEvent setArrivalDateTime:]
- -[CSDonatedEvent setArrivalTerminal:]
- -[CSDonatedEvent setBookingInfoUrl:]
- -[CSDonatedEvent setCheckInUrl:]
- -[CSDonatedEvent setConfirmationNumber:]
- -[CSDonatedEvent setCourierName:]
- -[CSDonatedEvent setDeliveryDateTime:]
- -[CSDonatedEvent setDepartureAirportCode:]
- -[CSDonatedEvent setDepartureAirportName:]
- -[CSDonatedEvent setDepartureDateTime:]
- -[CSDonatedEvent setDepartureTerminal:]
- -[CSDonatedEvent setDocIDs:]
- -[CSDonatedEvent setFlightCarrier:]
- -[CSDonatedEvent setFlightNumber:]
- -[CSDonatedEvent setFlightStatus:]
- -[CSDonatedEvent setFromAllowListedSender:]
- -[CSDonatedEvent setMerchantName:]
- -[CSDonatedEvent setMutableAttributes:]
- -[CSDonatedEvent setOrderDateTime:]
- -[CSDonatedEvent setSenderIsCourier:]
- -[CSDonatedEvent setTrackingNumber:]
- -[CSDonatedEvent setTrackingUrl:]
- -[CSDonatedEvent setType:]
- -[CSDonatedEvent trackingNumber]
- -[CSDonatedEvent trackingUrl]
- -[CSDonatedEvent type]
- -[CSFileProviderDomainMonitor domainDeleteQueue]
- -[CSFileProviderDomainMonitor setDomainDeleteQueue:]
- -[CSInstantAnswer .cxx_destruct]
- -[CSInstantAnswer actions]
- -[CSInstantAnswer addAction:]
- -[CSInstantAnswer attributes]
- -[CSInstantAnswer copyWithZone:]
- -[CSInstantAnswer description]
- -[CSInstantAnswer event]
- -[CSInstantAnswer initWithAttributes:]
- -[CSInstantAnswer initWithEvent:]
- -[CSInstantAnswer setActions:]
- -[CSInstantAnswer setEvent:]
- -[CSInstantAnswerAction .cxx_destruct]
- -[CSInstantAnswerAction attributes]
- -[CSInstantAnswerAction copyWithZone:]
- -[CSInstantAnswerAction description]
- -[CSInstantAnswerAction initWithAttributes:]
- -[CSInstantAnswerAction initWithType:andUrl:]
- -[CSInstantAnswerAction setType:]
- -[CSInstantAnswerAction setUrl:]
- -[CSInstantAnswerAction type]
- -[CSInstantAnswerAction url]
- -[CSRequestQueue async:critical:]
- -[CSRequestQueue handleEvent]
- -[CSSearchConnection startQuery:context:].cold.1
- -[CSSearchableIndex endIndexBatchWithExpectedClientState:newClientState:critical:reason:completionHandler:]
- -[CSSearchableIndex endIndexBatchWithExpectedClientState:newClientState:critical:reason:completionHandler:].cold.1
- -[CSSearchableIndex indexSearchableItems:completionHandler:].cold.1
- -[CSSearchableIndex indexSearchableItems:completionHandler:].cold.2
- -[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:clientStateName:protectionClass:forBundleID:options:reason:completionHandler:]
- -[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:protectionClass:forBundleID:options:reason:completionHandler:]
- -[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:protectionClass:forBundleID:options:completionHandler:]
- -[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:protectionClass:forBundleID:options:reason:completionHandler:]
- -[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:protectionClass:forBundleID:options:reason:completionHandler:]
- -[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:reason:completionHandler:]
- -[CSSearchableIndex isEmbeddingVersionCurrent:error:]
- -[CSSearchableIndexRequest setRequestID:]
- -[CSSearchableItemAttributeSet(CSDonatedEvent) donatedEvent]
- -[CSSearchableItemAttributeSet(CSDonatedEvent) setDonatedEvent:]
- -[CSSearchableItemAttributeSet(CSInstantAnswer) instantAnswers]
- -[CSSearchableItemAttributeSet(CSInstantAnswer) setInstantAnswers:]
- -[CSUserQuery foundInstantAnswersHandlerOld]
- -[CSUserQuery setFoundInstantAnswersHandlerOld:]
- -[CSUserQuery(CSInstantAnswer) handleFoundInstantAnswer:]
- -[CSUserQuery(CSInstantAnswer) handleFoundInstantAnswer:].cold.1
- -[CSUserQuery(CSInstantAnswer) processInstantAnswersWithFoundItems:]
- GCC_except_table1003
- GCC_except_table108
- GCC_except_table109
- GCC_except_table113
- GCC_except_table115
- GCC_except_table121
- GCC_except_table122
- GCC_except_table129
- GCC_except_table130
- GCC_except_table134
- GCC_except_table135
- GCC_except_table150
- GCC_except_table151
- GCC_except_table155
- GCC_except_table159
- GCC_except_table163
- GCC_except_table167
- GCC_except_table176
- GCC_except_table181
- GCC_except_table182
- GCC_except_table198
- GCC_except_table199
- GCC_except_table202
- GCC_except_table217
- GCC_except_table218
- GCC_except_table221
- GCC_except_table227
- GCC_except_table236
- GCC_except_table237
- GCC_except_table241
- GCC_except_table242
- GCC_except_table246
- GCC_except_table247
- GCC_except_table251
- GCC_except_table252
- GCC_except_table256
- GCC_except_table267
- GCC_except_table284
- GCC_except_table285
- GCC_except_table288
- GCC_except_table294
- GCC_except_table308
- GCC_except_table313
- GCC_except_table314
- GCC_except_table316
- GCC_except_table320
- GCC_except_table321
- GCC_except_table322
- GCC_except_table330
- GCC_except_table331
- GCC_except_table334
- GCC_except_table343
- GCC_except_table347
- GCC_except_table349
- GCC_except_table421
- GCC_except_table422
- GCC_except_table423
- GCC_except_table424
- GCC_except_table431
- GCC_except_table468
- GCC_except_table516
- GCC_except_table691
- GCC_except_table84
- GCC_except_table97
- GCC_except_table98
- _CSDonatedEventTypeFlight
- _CSDonatedEventTypeShipment
- _CSDonatedEventTypeUnknown
- _CSEventTypeMovie
- _CSEventTypeTicket
- _CSInstantAnswerActionTypeFlightBookingInfo
- _CSInstantAnswerActionTypeFlightCheckIn
- _CSInstantAnswerActionTypeShipmentTracking
- _MDItemDerivedIsMeRankingTextContentMatch
- _OBJC_CLASS_$_CSDonatedEvent
- _OBJC_CLASS_$_CSInstantAnswer
- _OBJC_CLASS_$_CSInstantAnswerAction
- _OBJC_IVAR_$_CSDonatedEvent._mutableAttributes
- _OBJC_IVAR_$_CSFileProviderDomainMonitor._domainDeleteQueue
- _OBJC_IVAR_$_CSInstantAnswer._actions
- _OBJC_IVAR_$_CSInstantAnswer._event
- _OBJC_IVAR_$_CSInstantAnswerAction._type
- _OBJC_IVAR_$_CSInstantAnswerAction._url
- _OBJC_IVAR_$_CSRequestQueue._workItemsQoS
- _OBJC_IVAR_$_CSRequestQueue._workSource
- _OBJC_IVAR_$_CSSearchQuery._cancelled
- _OBJC_IVAR_$_CSUserQuery._foundInstantAnswersHandlerOld
- _OBJC_METACLASS_$_CSDonatedEvent
- _OBJC_METACLASS_$_CSInstantAnswer
- _OBJC_METACLASS_$_CSInstantAnswerAction
- _UTTypeCopyParentIdentifiers
- __OBJC_$_CLASS_METHODS_CSDonatedEvent
- __OBJC_$_CLASS_METHODS_CSInstantAnswer
- __OBJC_$_CLASS_METHODS_CSInstantAnswerAction
- __OBJC_$_CLASS_METHODS_CSSearchConnection
- __OBJC_$_CLASS_METHODS_CSSearchableIndex(InternalSPI|SpotlightCache)
- __OBJC_$_CLASS_METHODS_CSSearchableItemAttributeSet
- __OBJC_$_CLASS_METHODS_CSUserQuery(CSSuggestionBlending|CSInstantAnswer)
- __OBJC_$_INSTANCE_METHODS_CSDonatedEvent
- __OBJC_$_INSTANCE_METHODS_CSInstantAnswer
- __OBJC_$_INSTANCE_METHODS_CSInstantAnswerAction
- __OBJC_$_INSTANCE_METHODS_CSSearchableIndex(InternalSPI|SpotlightCache)
- __OBJC_$_INSTANCE_METHODS_CSSearchableItemAttributeSet(CSAttributes|CSQuery|CSPrivateAttributes|CSMediaAnalysis_Private|CSWallet_Private|CSMail_Private|CSSafari_Private|CSFileProvider_Private|CSInteraction_private|CSAppDemotion_Private|CSNews_Private|CSPortrait_Private|CSPhone_Private|CSPhotos_Private|CSMotion|CSMessages_Private|CSNotifications_Private|CSAddressBook_Private|Containment|EventsExtras|CSCustomAttributes|CSCoderAdditions|CSInstantAnswer|CSDonatedEvent|CSEvent_Flight|CSEvent_Hotel|SwiftUI_Archiving|CSEvent_Restaurant|CSEvent_Generic|CSCard|CSContact|AppEntity|CSEmbeddingVector|AllEventTypes|CSInterfaces)
- __OBJC_$_INSTANCE_METHODS_CSUserQuery(CSSuggestionBlending|CSInstantAnswer)
- __OBJC_$_INSTANCE_VARIABLES_CSDonatedEvent
- __OBJC_$_INSTANCE_VARIABLES_CSInstantAnswer
- __OBJC_$_INSTANCE_VARIABLES_CSInstantAnswerAction
- __OBJC_$_PROP_LIST_CSDonatedEvent
- __OBJC_$_PROP_LIST_CSInstantAnswer
- __OBJC_$_PROP_LIST_CSInstantAnswerAction
- __OBJC_CLASS_PROTOCOLS_$_CSDonatedEvent
- __OBJC_CLASS_PROTOCOLS_$_CSInstantAnswer
- __OBJC_CLASS_PROTOCOLS_$_CSInstantAnswerAction
- __OBJC_CLASS_RO_$_CSDonatedEvent
- __OBJC_CLASS_RO_$_CSInstantAnswer
- __OBJC_CLASS_RO_$_CSInstantAnswerAction
- __OBJC_METACLASS_RO_$_CSDonatedEvent
- __OBJC_METACLASS_RO_$_CSInstantAnswer
- __OBJC_METACLASS_RO_$_CSInstantAnswerAction
- ___107-[CSSearchableIndex endIndexBatchWithExpectedClientState:newClientState:critical:reason:completionHandler:]_block_invoke
- ___107-[CSSearchableIndex endIndexBatchWithExpectedClientState:newClientState:critical:reason:completionHandler:]_block_invoke_2
- ___188-[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:protectionClass:forBundleID:options:reason:completionHandler:]_block_invoke
- ___188-[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:protectionClass:forBundleID:options:reason:completionHandler:]_block_invoke.203
- ___188-[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:protectionClass:forBundleID:options:reason:completionHandler:]_block_invoke_2
- ___188-[CSSearchableIndex indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:protectionClass:forBundleID:options:reason:completionHandler:]_block_invoke_2.204
- ___21-[CSSearchQuery poll]_block_invoke.1047
- ___34-[CSSearchConnection cancelQuery:]_block_invoke.1391
- ___34-[CSSearchConnection cancelQuery:]_block_invoke.1391.cold.1
- ___36-[CSSearchQuery processResultItems:]_block_invoke.1102
- ___46-[CSFileProviderDomainMonitor startMonitoring]_block_invoke.13
- ___46-[CSFileProviderDomainMonitor startMonitoring]_block_invoke_2.14
- ___54-[CSSearchQuery copyResultsFromPlist:protectionClass:]_block_invoke.1075
- ___59-[CSRequestQueue initWithLabel:target:critical:startBlock:]_block_invoke
- ___59-[CSRequestQueue initWithLabel:target:critical:startBlock:]_block_invoke_2
- ___67-[CSSearchableItem(Internal) _standardizeExtractedNumericEntities:]_block_invoke.295
- ___67-[CSSearchableItem(Internal) _standardizeExtractedNumericEntities:]_block_invoke.313
- ___76-[CSSearchableIndex performIndexJob:protectionClass:acknowledgementHandler:]_block_invoke.321
- ___80-[CSSearchQuery filterMegadomePeopleSuggestions:isShortQuery:completionHandler:]_block_invoke.1078
- ___99-[CSSearchableIndex _fetchCacheFileDescriptorsForProtectionClass:bundleID:items:completionHandler:]_block_invoke.387
- ___Block_byref_object_copy_.385
- ___Block_byref_object_dispose_.386
- ___block_descriptor_108_e8_32s40s48s56s_e8_v16?0Q8ls32l8s40l8s48l8s56l8
- ___block_descriptor_116_e8_32s40s48s56s64r_e13_v24?0^8^B16ls32l8r64l8s40l8s48l8s56l8
- ___block_descriptor_116_e8_32s40s48s56s64r_e8_v16?0Q8lr64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_120_e8_32s40s48s56r_e13_v24?0^8^B16ls32l8r56l8s40l8s48l8
- ___block_descriptor_129_e8_32s40s48s56s64s72s80s88s96s104bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
- ___block_descriptor_169_e8_32s40s48s56s64s72s80s88s96s104s112w_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8w112l8
- ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
- ___block_descriptor_64_e8_32s40r48r56r_e11_B20?0Q8B16ls32l8r40l8r48l8r56l8
- ___block_descriptor_80_e8_32s40s48s_e59_"CSExternalAnalysisTag"40?0Q8"NSString"16"NSArray"24d32ls32l8s40l8s48l8
- ___block_descriptor_88_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_89_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_91_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
- ___block_literal_global.1003
- ___block_literal_global.1050
- ___block_literal_global.1056
- ___block_literal_global.1367
- ___block_literal_global.1369
- ___block_literal_global.1371
- ___block_literal_global.1374
- ___block_literal_global.1377
- ___block_literal_global.1487
- ___block_literal_global.1525
- ___block_literal_global.1527
- ___block_literal_global.1529
- ___block_literal_global.1542
- ___block_literal_global.1544
- ___block_literal_global.1546
- ___block_literal_global.181
- ___block_literal_global.185
- ___block_literal_global.187
- ___block_literal_global.1963
- ___block_literal_global.20
- ___block_literal_global.236
- ___block_literal_global.247
- ___block_literal_global.249
- ___block_literal_global.251
- ___block_literal_global.253
- ___block_literal_global.286
- ___block_literal_global.288
- ___block_literal_global.290
- ___block_literal_global.305
- ___block_literal_global.319
- ___block_literal_global.327
- ___block_literal_global.479
- ___block_literal_global.493
- ___block_literal_global.547
- ___block_literal_global.687
- ___block_literal_global.704
- ___block_literal_global.775
- ___block_literal_global.824
- ___block_literal_global.838
- ___block_literal_global.846
- ___block_literal_global.987
- ___block_literal_global.991
- ___fetchMailVIPList_block_invoke.548
- ___fetchMailVIPList_block_invoke.548.cold.1
- ___fetchMailVIPList_block_invoke.548.cold.2
- ___getSKGEmbeddingVersionManagerClass_block_invoke
- ___getSKGEmbeddingVersionManagerClass_block_invoke.cold.1
- __dispatch_source_type_data_or
- __requestQueueAttribute:.onceToken
- __requestQueueAttribute:.shouldPropagateQos
- _defaultSearchableIndex.onceToken.770
- _defaultSearchableIndex.onceToken.777
- _defaultSearchableIndex.sDefaultInstance.769
- _defaultSearchableIndex.sDefaultInstance.776
- _dispatch_set_qos_class_floor
- _dispatch_source_get_data
- _dispatch_source_merge_data
- _dispatch_source_set_cancel_handler
- _getAllUniqueEventAttributes.attrs
- _getSKGEmbeddingVersionManagerClass.softClass
- _kUTTypeDirectory
- _kUTTypeEmailMessage
- _kUTTypeFolder
- _kUTTypeItem
- _kUTTypeMessage
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$actions
- _objc_msgSend$arrivalAirportCode
- _objc_msgSend$arrivalAirportName
- _objc_msgSend$async:critical:
- _objc_msgSend$copyWithZone:
- _objc_msgSend$courierName
- _objc_msgSend$currentEmbeddingVersionDataReturningError:
- _objc_msgSend$dataFromInstantAnswers:
- _objc_msgSend$departureAirportCode
- _objc_msgSend$departureAirportName
- _objc_msgSend$donatedEvent
- _objc_msgSend$event
- _objc_msgSend$eventFromData:
- _objc_msgSend$foundInstantAnswersHandlerOld
- _objc_msgSend$handleEvent
- _objc_msgSend$handleFoundInstantAnswer:
- _objc_msgSend$indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:protectionClass:forBundleID:options:reason:completionHandler:
- _objc_msgSend$initWithAddress:synonyms:type:lat:lng:confidence:
- _objc_msgSend$initWithEvent:
- _objc_msgSend$initWithType:andUrl:
- _objc_msgSend$instantAnswersFromData:
- _objc_msgSend$isInstantAnswerTriggerQuery:isCJK:isSearchTool:
- _objc_msgSend$merchantName
- _objc_msgSend$processInstantAnswersWithFoundItems:
- _objc_msgSend$removeObjectAtIndex:
- _objc_msgSend$setActions:
- _objc_msgSend$setEvent:
- _objc_msgSend$setMutableAttributes:
- _objc_msgSend$setType:
- _objc_msgSend$setUrl:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
- _onceTokenShared
CStrings:
+ "\rU"
+ " inline-cache"
+ "#messagesResources: Failed to soft-link SpotlightResources"
+ "#messagesResources: Failed to soft-link loadAllParametersForClient:locale:options:"
+ "#messagesResources: Failed to soft-link resourcesForClient:options:"
+ "#messagesResources: Failed to soft-link sharedResourcesManager"
+ "%@: %@ %@"
+ "%@: Completed donation deleting ALL items"
+ "%@: Encountered translation error for item: %@ error: %@"
+ "%@: Set existence required and no set exists, skipping donation"
+ "%@: Skipping cache content for item: %@ due to error: %@"
+ "%@: Skipping donation for unidentifiable source"
+ "%@: Skipping rejected item: %@ error: %@"
+ "%@: failed to load conforming LNSpotlightCascadeTranslator from LinkServices"
+ "%@:%@: Skipping donation (feature flag disabled)"
+ "%@:%@: Skipping donation (not applicable)"
+ "%@:%@: Skipping donation (protection class: %@)"
+ "%@:%@: Skipping donation (translator denied sourceIdentifier)"
+ "%@Hour"
+ "%@Minute"
+ "%@Second"
+ "%llX"
+ "%lu"
+ "*warn* Unbalanced resume of CSRequestQueue %s"
+ ", %@"
+ ".PhotosFileProvider"
+ ".cxx_construct"
+ "/AppleInternal/Library/BuildRoots/4~CIU-ugDPXOyvdfYB_QAU87F_Ti_htSLbt3NKGrY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU-ugDPXOyvdfYB_QAU87F_Ti_htSLbt3NKGrY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/Library/Spotlight/CoreSpotlight/PipelineCompletenessReporting"
+ "/boop"
+ "/draganddrop"
+ "<%@: All Known: %lu; Needing Donation: %lu; Donated: %@; Partially Donated: %@; Pending Redonation: %@; Newest Undonated Date: %@>"
+ "<%@:%p %@ %f (%ld, %ld) <%@>"
+ "<%@:%p %@ <%@, %@>"
+ "<%@:%p <%@>"
+ "<%@:%p; isInBatch=%@, indexedItems=%lu, deletedItems=%lu, userActivities=%lu, deletedUserActivities=%lu, interactions=%lu, deletedInteractions=%lu>"
+ "<%@> {\n  bundleID: %@\n  pipeline: %@\n  overallCompleteness: %@\n  donationCompleteness: %@\n  pipelineCompleteness: %@\n  pipelineCompletenessHeuristicScore: %@\n  pipelineReportAge: %.2f seconds\n  isSufficientlyComplete: %@\n  donationProgress: %@\n  pipelineCompletenessFirstTimeBucket: %@\n  pipelineCompletenessSecondBucket: %@\n  pipelineCompletenessThirdBucket: %@\n}"
+ "<%@> {\n  pipeline: %@\n  overallCompleteness: %@\n  donationCompleteness: %@\n  pipelineCompleteness: %@\n  pipelineCompletenessHeuristicScore: %@\n  pipelineReportAge: %.2f seconds\n  isSufficientlyComplete: %@\n}"
+ "?P"
+ "@\"<DonationProgressReporting>\""
+ "@\"BMSource\""
+ "@\"NSObject\""
+ "@104@0:8@16@24@32@40@48@56@64@72@80Q88q96"
+ "@104@0:8@16@24@32@40@48@56d64@72@80@88@96"
+ "@108@0:8@16@24@32@40@48@56B64@68@76@84Q92q100"
+ "@124@0:8@16@24@32@40@48@56@64B72@76@84@92Q100q108q116"
+ "@24@0:8d16"
+ "@28@0:8B16@20"
+ "@32@0:8@16B24B28"
+ "@32@0:8Q16@24"
+ "@48@0:8@16@24Q32@40"
+ "@48@0:8q16@24q32@40"
+ "@56@0:8Q16Q24@32@40@48"
+ "@64@0:8Q16Q24@32@40@48@56"
+ "@72@0:8@16@24q32q40d48d56d64"
+ "@80@0:8@16@24@32@40@48@56@64@72"
+ "@94@0:8^@16Q24^Q32@40@48^s56Q64{CSUnpackInfo=sssssss}72@86"
+ "AB"
+ "AppSpecificLocalizedKeywords"
+ "B24@0:8^@16"
+ "B48@0:8@16@24@32^@40"
+ "CCItemErrorDomain"
+ "CCItemFieldPredicate"
+ "CCSetDescriptor"
+ "CCSetDonation"
+ "CCSetErrorDomain"
+ "CSClock_Private"
+ "CSDonationProgress"
+ "CSDonationProgressFailure"
+ "CSDonationProgressQueryResult"
+ "CSIndexingPipelineOverallCompleteness"
+ "CSIndexingPipelineOverallCompletenessForBundle"
+ "CSInlineDonation"
+ "CSInlineDonation.shared"
+ "CSMockSearchableIndex"
+ "CSPipelineCompletenessReport"
+ "CSPipelineCompletenessReportStorage"
+ "CSPipelineCompletenessReportStorageErrorDomain"
+ "CSPlace"
+ "CSPowerHUD"
+ "CSRecurrenceRule"
+ "CSSearchableItemAttributeSet: loading messages resources"
+ "CSTestIndexConnection"
+ "CSTestSearchQuery"
+ "CSTestSearchableIndex"
+ "CSTestSearchableIndexShared"
+ "Cascade"
+ "Cleaned up removed domains:%@"
+ "Clock_alarmEnabled"
+ "Completed donation: %@ result: %@"
+ "Config file %@ with event type not found."
+ "Config file %@ with messages shared links not found."
+ "DonationProgressReporting"
+ "Dropping donation: %@ (%lu bytes with %u enqueued exceeding limit of %u)"
+ "End batch called while not in a batch"
+ "EventType"
+ "Expected client state does not match current state"
+ "Expected client state: %@ is not equal to priorClientState: %@ for client name: %@"
+ "Failed to add or update item: %@"
+ "Failed to archive completeness reports"
+ "Failed to create storage directory"
+ "Failed to decode stored donation progress from data, bundle: %@, indexName: %@"
+ "Failed to delete domainIdentifier: %@"
+ "Failed to finish donation"
+ "Failed to finish donation deleting ALL items"
+ "Failed to read file data"
+ "Failed to remove domains:%@. Error:%@"
+ "Failed to remove item: %@"
+ "Failed to request donation"
+ "Failed to resolve sourceIdentifier descriptor"
+ "Failed to unarchive completeness reports"
+ "Failed to update client state: %@ with client state name: %@"
+ "Failed to update linked timestamp: %@"
+ "Failed to write data to file"
+ "Initialized donation: %@"
+ "InternalTestIndex"
+ "Invalid parameters: pipeline must not be nil"
+ "Invalid parameters: reports and pipeline must not be nil"
+ "Invalid pipeline name"
+ "LNSpotlightCascadeTranslator"
+ "LT"
+ "MessagesSharedLink"
+ "N/A"
+ "No stored donation progress reports found for bundle: %@"
+ "NoOTA"
+ "Not supported in mock interface"
+ "Operations"
+ "Performing donation: %@"
+ "PowerHUD"
+ "SPAttributeFetchResults"
+ "SPAttributeNameResults"
+ "SPIndexFetchResultUnknown(%ld)"
+ "SPQueryCompletions"
+ "SPQueryCount"
+ "SPQueryFinished"
+ "SPQueryGatherEnded"
+ "SPQueryMatchInfo"
+ "SPQueryPhotosComputedData"
+ "SPQueryResults"
+ "SPQueryResultsRemoved"
+ "SPQueryResultsUpdated"
+ "SPQueryRewritten"
+ "SearchToolDebugMode"
+ "SpotlightDataExpiration"
+ "SpotlightKnowledge"
+ "SpotlightKnowledgePipelineRefactorStandalone"
+ "Submitting donation: %@ (%lu bytes with %u enqueued)"
+ "T@\"<CSSearchableIndexDelegate>\",W"
+ "T@\"<DonationProgressReporting>\",R,V_donationProgress"
+ "T@\"CSPlace\",C"
+ "T@\"NSArray\",C,V_daysOfTheWeek"
+ "T@\"NSArray\",R,N,V_addOrUpdateItems"
+ "T@\"NSArray\",R,N,V_deleteDomainIdentifiers"
+ "T@\"NSArray\",R,N,V_deleteItemIdentifiers"
+ "T@\"NSData\",R,N,V_expectedClientState"
+ "T@\"NSData\",R,N,V_updatedClientState"
+ "T@\"NSDate\",R,V_dateOfNewestUndonatedItem"
+ "T@\"NSDate\",R,V_reportDate"
+ "T@\"NSDictionary\",R,N,V_associatedHTMLContent"
+ "T@\"NSDictionary\",R,N,V_associatedTextContent"
+ "T@\"NSError\",&,N,V_simulatedError"
+ "T@\"NSError\",R,V_underlyingError"
+ "T@\"NSMutableArray\",R,N,V_batchedItems"
+ "T@\"NSMutableArray\",R,N,V_deletedUserActivities"
+ "T@\"NSMutableArray\",R,N,V_userActivities"
+ "T@\"NSMutableDictionary\",R,N,V_clientStates"
+ "T@\"NSMutableDictionary\",R,N,V_deletedInteractions"
+ "T@\"NSMutableDictionary\",R,N,V_deletedItems"
+ "T@\"NSMutableDictionary\",R,N,V_indexedItems"
+ "T@\"NSMutableDictionary\",R,N,V_interactions"
+ "T@\"NSMutableSet\",R,N,V_batchedDeletedIdentifiers"
+ "T@\"NSNumber\",&,GhasSuggestedEdits"
+ "T@\"NSNumber\",&,GisCompleted"
+ "T@\"NSNumber\",&,GisFavorited"
+ "T@\"NSNumber\",&,GisFlagged"
+ "T@\"NSNumber\",&,GisRead"
+ "T@\"NSNumber\",&,GisUserHidden"
+ "T@\"NSNumber\",&,GisUserPrivate"
+ "T@\"NSNumber\",R,N,V_latitude"
+ "T@\"NSNumber\",R,N,V_longitude"
+ "T@\"NSNumber\",R,V_donatedItems"
+ "T@\"NSNumber\",R,V_donationCompeleteness"
+ "T@\"NSNumber\",R,V_eligibleItems"
+ "T@\"NSNumber\",R,V_itemsNeedingDonationForRedonationRequests"
+ "T@\"NSNumber\",R,V_overallCompleteness"
+ "T@\"NSNumber\",R,V_partiallyDonatedItems"
+ "T@\"NSNumber\",R,V_pipelineCompleteness"
+ "T@\"NSNumber\",R,V_pipelineCompletenessFirstTimeBucket"
+ "T@\"NSNumber\",R,V_pipelineCompletenessHeuristicScore"
+ "T@\"NSNumber\",R,V_pipelineCompletenessSecondBucket"
+ "T@\"NSNumber\",R,V_pipelineCompletenessThirdBucket"
+ "T@\"NSObject\",R,N,V_logOwner"
+ "T@\"NSString\",&,N,V_mailQueryID"
+ "T@\"NSString\",R,N,V_clientStateName"
+ "T@\"NSString\",R,N,V_donationName"
+ "T@\"NSString\",R,N,V_fullyFormattedAddress"
+ "T@\"NSString\",R,N,V_namedLocation"
+ "T@\"NSString\",R,N,V_sourceIdentifier"
+ "T@\"NSString\",R,V_bundleID"
+ "T@\"NSString\",R,V_indexName"
+ "T@\"NSString\",R,V_pipeline"
+ "T@,&,N,V_biomeStream"
+ "TB,N,V_hasReadPurpose"
+ "TB,N,V_shouldSimulateErrors"
+ "TB,R,N,V_deleteAllItems"
+ "TB,R,N,V_isInBatch"
+ "TB,R,N,V_isInlineCacheEnabled"
+ "TQ,R,N,V_donationTimestamp"
+ "TQ,R,N,V_itemsDataSize"
+ "TQ,R,V_allKnownItems"
+ "TQ,R,V_failureReason"
+ "TQ,R,V_itemsNeedingDonation"
+ "TQ,R,V_status"
+ "Td,R"
+ "Td,R,V_pipelineReportAge"
+ "Tq,R,N,V_code"
+ "Tq,R,N,V_donationType"
+ "Tq,R,N,V_type"
+ "URLByAppendingPathComponent:"
+ "[16s]"
+ "[<%@ %p flag=0x%4.4x> qid=%ld] starting\n"
+ "[debug][personal answers][query][idx=%ld] queryUnderstandingOutput = %@"
+ "[personal answers][query][idx=%ld] queryUnderstandingOutput has event intent, kQPQUIntentLabels = %@"
+ "[qid=%ld] Finished with error error:%{public}@/%ld"
+ "[qid=%ld] Results type: %{public}@"
+ "[qid=%ld] attribute %@ : %@\n"
+ "[qid=%ld] complete %s %@\n"
+ "[qid=%ld] filterQuery[%u]: %@\n"
+ "[qid=%ld] finished %@\n"
+ "[qid=%ld] found %@/%@ l1: %f\n"
+ "[qid=%ld] found oid: %ld %@ %@\n"
+ "[qid=%ld] found oid: %ld %@ %@ l1: %f l2: %f rd: %ld cd: %ld\n"
+ "[qid=%ld] foundAdd oid: %ld %@ %@\n"
+ "[qid=%ld] foundAdd oid: %ld %@ %@ l1: %f rd: %ld cd: %ld\n"
+ "[qid=%ld] foundUpdate oid: %ld %@ %@\n"
+ "[qid=%ld] foundUpdate oid: %ld %@ %@ l1: %f rd: %ld cd: %ld\n"
+ "[qid=%ld] gather complete %s\n"
+ "[qid=%ld] polling \n"
+ "[qid=%ld] processing oid: %ld %@ %@ l1: %f rd: %ld cd: %ld\n"
+ "[qid=%ld] query for queryString(%d): %@\n"
+ "[qid=%ld] rankingQuery[%u]: %@\n"
+ "[qid=%ld] received %s notification\n"
+ "[qid=%ld] scopes(%d): %@\n"
+ "[qid=%ld] sdbFilter: %@\n"
+ "[qid=%ld][CSTopHitRanking] Finishing - clientBundleID=%@ hitCount=%ld, maxCount=%ld\n"
+ "[qid=%ld][CSTopHitRanking] Processing - clientBundleID=%@ maxDenseCount=%ld, maxCount=%ld, itemsCount=%lu\n"
+ "[qid=%ld][CSTopHitRanking] finishing - combining %lu topHitResults with %lu initial candidates to return a batch of %lu items\n"
+ "[qid=%ld][CSTopHitRanking] finishing - sending %lu dense items to client now\n"
+ "[qid=%ld][CSTopHitRanking] processing - current batch has %lu items (%ld items are L1 topHit candidates, %ld items are L2 topHit candidates)\n"
+ "[qid=%ld][CSTopHitRanking] processing oid: %lld %@/%@ l1: %f\n"
+ "[qid=%ld][CSTopHitRanking] using oid: %lld %@/%@ l1: %f\n"
+ "[qid=%ld][QoS=%u] Starting %{private}@"
+ "_addOrUpdateItem:withIdentifier:donation:error:"
+ "_addOrUpdateItems"
+ "_allKnownItems"
+ "_associatedHTMLContent"
+ "_associatedTextContent"
+ "_batchedDeletedIdentifiers"
+ "_batchedItems"
+ "_biomeStream"
+ "_clientStateName"
+ "_clientStates"
+ "_code"
+ "_createStorageDirectoryIfNotExistsWithError:"
+ "_dateOfNewestUndonatedItem"
+ "_daysOfTheWeek"
+ "_deleteAllItems"
+ "_deleteDomainIdentifiers"
+ "_deleteItemIdentifiers"
+ "_deletedInteractions"
+ "_deletedItems"
+ "_deletedUserActivities"
+ "_donatedItems"
+ "_donationCompeleteness"
+ "_donationName"
+ "_donationProgress"
+ "_donationTimestamp"
+ "_donationType"
+ "_eligibleItems"
+ "_expectedClientState"
+ "_failureReason"
+ "_fileURLForPipeline:"
+ "_fullyFormattedAddress"
+ "_getTimeComponentsForKey:"
+ "_hasReadPurpose"
+ "_indexName"
+ "_indexedItems"
+ "_inlineDonationWithOverrideBundleID:protectionClass:addOrUpdateItems:associatedTextContent:associatedHTMLContent:deleteItemIdentifiers:deleteDomainIdentifiers:deleteAllItems:clientStateName:updatedClientState:expectedClientState:itemsDataSize:options:donationType:"
+ "_interactions"
+ "_isInBatch"
+ "_isInlineCacheEnabled"
+ "_issueDiagnose:logQuery:completionHandler:"
+ "_itemsDataSize"
+ "_itemsNeedingDonation"
+ "_itemsNeedingDonationForRedonationRequests"
+ "_kMDItemAppEntitySchema"
+ "_kMDItemBundleID = \"%@\""
+ "_kMDItemClientDonationProgress_"
+ "_kMDItemClockAlarmType"
+ "_kMDItemDerivedIsMeRankingTextContentMatchTokens"
+ "_kMDItemEventRelatedMessageIdentifiers"
+ "_kMDItemEventRelatedSourceBundleIdentifiers"
+ "_kMDItemIndexRankingDateSeconds"
+ "_kMDItemPhotosIdentificationDocumentsVersion"
+ "_kMDItemRelatedBundleID"
+ "_kMDItemSDBInfo"
+ "_latitude"
+ "_logErrorWithCode:description:underlying:"
+ "_logOwner"
+ "_logToken"
+ "_longitude"
+ "_mailQueryID"
+ "_namedLocation"
+ "_needSave"
+ "_overallCompleteness"
+ "_overrideDefaultSearchableIndexForTestingWithDoSet:searchableIndex:"
+ "_parentTypes"
+ "_partiallyDonatedItems"
+ "_perform:"
+ "_pipeline"
+ "_pipelineCompleteness"
+ "_pipelineCompletenessFirstTimeBucket"
+ "_pipelineCompletenessHeuristicScore"
+ "_pipelineCompletenessSecondBucket"
+ "_pipelineCompletenessThirdBucket"
+ "_pipelineReportAge"
+ "_reportDate"
+ "_reportErrorWithCode:clientDescription:donationErrorCode:underlying:"
+ "_resolveDonationName"
+ "_setTimeComponentsForKey:time:"
+ "_shouldSimulateErrors"
+ "_simulatedError"
+ "_sourceIdentifier"
+ "_standardizePlaces:"
+ "_storageURL"
+ "_swizzleDefaultSearchableIndexWithDoSwizzle:"
+ "_underlyingError"
+ "_updateRevisionToken:error:"
+ "_updatedClientState"
+ "_userActivities"
+ "add-update-items:%lu delete-items:%lu"
+ "addOrUpdateItem:cacheContent:error:"
+ "addOrUpdateItem:error:"
+ "addOrUpdateItems"
+ "addupdateDeleteCount"
+ "alarmRecurrenceRule"
+ "alarmTime"
+ "allKnownItems"
+ "alternateTitles"
+ "associatedHTMLContent"
+ "associatedTextContent"
+ "attributeName"
+ "batchedDeletedIdentifiers"
+ "batchedItems"
+ "biomeStream"
+ "canSnooze"
+ "changeStateOfSearchableItemsWithUIDs:toState:forUser:forBundleID:forUTIType:"
+ "client"
+ "clientErrorCode"
+ "clientStateName"
+ "clientStates"
+ "clockAlarmType"
+ "com.apple.CascadeSets.InlineDonation"
+ "com.apple.Stickers"
+ "com.apple.corespotlight.powerhud"
+ "com.apple.searchd"
+ "com.apple.spotlight.IndexAgent.test"
+ "com.apple.spotlight.SearchAgent.test"
+ "completed"
+ "completenessReport_%@.plist"
+ "completions"
+ "containsIndex:"
+ "contentCatalog"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "createKeywordDictionaryFromMDPlistObject_block_invoke"
+ "dataWithContentsOfURL:options:error:"
+ "dateOfNewestUndonatedItem"
+ "daysOfTheWeek"
+ "defaultInstance"
+ "defaultMock"
+ "delete-all"
+ "delete-domains:%lu"
+ "deleteAllItems"
+ "deleteDomainIdentifiers"
+ "deleteDomainIdentifiersCount"
+ "deleteItemIdentifiers"
+ "deleteItemIdentifiersCount"
+ "deletedInteractions"
+ "deletedItems"
+ "deletedUserActivities"
+ "designateAsFullSet"
+ "detectedCardSubTypes"
+ "donatedItems"
+ "donation-progress-data-size"
+ "donation-progress-key"
+ "donation-timestamp"
+ "donationCompeleteness"
+ "donationName"
+ "donationProgress"
+ "donationTimestamp"
+ "donationType"
+ "dontationType"
+ "eligibleItems"
+ "endIndexBatchWithExpectedClientState:newClientState:critical:reason:updatingDonationProgres:completionHandler:"
+ "endIndexBatchWithExpectedClientState:newClientState:updatingDonationProgress:completionHandler:"
+ "endIndexBatchWithExpectedClientState:newClientState:updatingDonationProgress:critical:completionHandler:"
+ "endIndexBatchWithExpectedClientState:newClientState:updatingDonationProgress:reason:completionHandler:"
+ "errorOrNoopWithCompletionHandler:"
+ "errorUnsupportedWithCompletionHandler:"
+ "eventBody"
+ "eventEndDate"
+ "eventStartDate"
+ "expectedClientState"
+ "failureReason"
+ "favorited"
+ "fetch-indexing-pipeline-completeness"
+ "fetchAttributes:protectionClass:bundleID:identifiers:userCtx:flags:qos:completionHandler:"
+ "fetchCacheFileDescriptorsForProtectionClass:bundleID:identifiers:userCtx:flags:qos:completionHandler:"
+ "fetchCompletenessReportsForPipeline:error:"
+ "fetchConsumedAndLatestSerialNums: %@"
+ "fetchConsumedAndLatestSerialNums:%@"
+ "fetchConsumedAndLatestSerialNums:completionHandler:"
+ "fetchDonationProgressForBundles"
+ "fetchDonationProgressForBundles:completionHandler:"
+ "fetchIndexingPipelineCompleteness"
+ "fetchIndexingPipelineCompleteness:forBundles:completionHandler:"
+ "fetchIndexingPipelineOverallCompleteness:completionHandler:"
+ "fileExistsAtPath:"
+ "filePathArrayForKey:"
+ "finish:"
+ "flagged"
+ "gatherEnded"
+ "getReturnValue:"
+ "getSpotlightDataExpiration"
+ "getSpotlightOperationsDataWithTimeInterval:"
+ "groupIdentifier"
+ "hasReadPurpose"
+ "hasSuggestedEdits"
+ "hrp"
+ "id=%lu"
+ "id_national_id"
+ "id_social_security"
+ "index-directory"
+ "indexDirectory:"
+ "indexName"
+ "indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:clientStateName:updatingDonationProgress:protectionClass:forBundleID:options:completionHandler:"
+ "indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:clientStateName:updatingDonationProgress:protectionClass:forBundleID:options:reason:completionHandler:"
+ "indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:updatingDonationProgress:protectionClass:forBundleID:options:reason:completionHandler:"
+ "indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:updatingDonationProgress:protectionClass:forBundleID:options:completionHandler:"
+ "indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:updatingDonationProgress:protectionClass:forBundleID:options:reason:completionHandler:"
+ "indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:updatingDonationProgress:protectionClass:forBundleID:options:completionHandler:"
+ "indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:updatingDonationProgress:protectionClass:forBundleID:options:reason:completionHandler:"
+ "indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:updatingDonationProgress:reason:completionHandler:"
+ "indexSearchableItems:updatingDonationProgress:completionHandler:"
+ "indexedItems"
+ "indexing-pipeline"
+ "indexing-pipeline-completeness"
+ "indexing-pipeline-completeness-bundles"
+ "indexing-pipeline-completeness-size"
+ "initWithAddress:synonyms:code:confidence:"
+ "initWithAddress:synonyms:code:type:lat:lng:confidence:"
+ "initWithAllKnownItems:itemsNeedingDonation:donatedItems:partiallyDonatedItems:itemsNeedingDonationForRedonationRequests:"
+ "initWithAllKnownItems:itemsNeedingDonation:donatedItems:partiallyDonatedItems:itemsNeedingDonationForRedonationRequests:dateOfNewestUndonatedItem:"
+ "initWithBase64EncodedString:options:"
+ "initWithBundleID:indexName:status:donationProgress:"
+ "initWithClient:itemsCount:operation:reason:stringIdentifier:stringReason:"
+ "initWithContentsOfFile:options:error:"
+ "initWithData:encoding:"
+ "initWithDaysOfTheWeek:"
+ "initWithFailureReason:underlyingError:"
+ "initWithFullyFormattedAddress:namedLocation:"
+ "initWithLatitude:longitude:fullyFormattedAddress:namedLocation:"
+ "initWithNamedLocation:"
+ "initWithPipeline:bundleID:overallCompleteness:donationCompeleteness:pipelineCompleteness:pipelineCompletenessHeuristicScore:pipelineReportAge:donationProgress:pipelineCompletenessFirstTimeBucket:pipelineCompletenessSecondBucket:pipelineCompletenessThirdBucket:"
+ "initWithPipeline:overallCompleteness:donationCompeleteness:pipelineCompleteness:pipelineCompletenessHeuristicScore:pipelineReportAge:"
+ "initWithPipelineName:bundleID:eligibleItems:pipelineCompleteness:pipelineCompletenessHeuristicScore:pipelineCompletenessFirstTimeBucket:pipelineCompletenessSecondBucket:pipelineCompletenessThirdBucket:"
+ "initWithSourceIdentifier:addOrUpdateItems:associatedTextContent:associatedHTMLContent:deleteItemIdentifiers:deleteDomainIdentifiers:deleteAllItems:clientStateName:updatedClientState:expectedClientState:itemsDataSize:donationType:"
+ "initWithStartDate:endDate:maxEvents:lastN:reversed:"
+ "initWithStorageURL:"
+ "initWithSuiteName:"
+ "inlineAddOrUpdateItems:associatedTextContent:associatedHTMLContent:deleteItemIdentifiers:overrideBundleID:protectionClass:clientStateName:updatedClientState:expectedClientState:itemsDataSize:options:"
+ "inlineDeleteAllItemsWithOverrideBundleID:protectionClass:options:"
+ "inlineDeleteDomainIdentifiers:overrideBundleID:protectionClass:options:"
+ "inlineDonationErrorCode"
+ "interactions"
+ "invalid format in config file %@ for event type."
+ "invalid format in config file %@ for messages shared links."
+ "isAlarmEnabled"
+ "isAllowedClientBundleIdentifier:"
+ "isCacheEnabledSourceIdentifier:"
+ "isCompleted"
+ "isEventIntentForQueryUnderstandingOutput:isSearchToolClient:isSearchToolCerberus:"
+ "isFavorited"
+ "isFlagged"
+ "isInBatch"
+ "isInlineCacheEnabled"
+ "isInlineCascadeDonationEnabled"
+ "isInlineDocumentCacheEnabledForBundleID:"
+ "isInstantAnswerTriggerQuery:isCJK:isSearchToolClient:"
+ "isRead"
+ "isSpecialPhotosEmptyDomain"
+ "isSpotlightDataExpired"
+ "isSufficientlyComplete"
+ "isUserHidden"
+ "isUserPrivate"
+ "itemCacheContentWithText:html:error:"
+ "itemCount"
+ "itemType"
+ "itemsCount"
+ "itemsDataSize"
+ "itemsNeedingDonation"
+ "itemsNeedingDonationForRedonationRequests"
+ "kMDItemAlarm"
+ "kMDItemAlarmRecurrenceRule"
+ "kMDItemAlarmRecurrenceRuleDaysOfTheWeek"
+ "kMDItemAlarmTime"
+ "kMDItemAlarmTimeHour"
+ "kMDItemAlarmTimeMinute"
+ "kMDItemAlarmTimeSecond"
+ "kMDItemAlternateTitles"
+ "kMDItemCanSnooze"
+ "kMDItemContentCatalog"
+ "kMDItemDetectedCardSubTypes"
+ "kMDItemEventEndDate"
+ "kMDItemEventStartDate"
+ "kMDItemExtractedAddressesCodes"
+ "kMDItemHasSuggestedEdits"
+ "kMDItemIsAlarmEnabled"
+ "kMDItemIsCompleted"
+ "kMDItemIsEnabled"
+ "kMDItemIsFavorited"
+ "kMDItemIsFlagged"
+ "kMDItemIsRead"
+ "kMDItemLocalizedLinkSubTypes"
+ "kMDItemLocalizedLinkTypes"
+ "kMDItemPlace"
+ "kMDItemPurchasedDate"
+ "kMDItemReceivedDate"
+ "kMDItemReleasedDate"
+ "kMDItemReminder"
+ "kMDItemReminderRecurrenceRule"
+ "kMDItemReminderRecurrenceRuleDaysOfTheWeek"
+ "kMDItemReminderTime"
+ "kMDItemReminderTimeHour"
+ "kMDItemReminderTimeMinute"
+ "kMDItemReminderTimeSecond"
+ "kMDItemSentDate"
+ "kMDItemTriggerState"
+ "kMDItemUserHidden"
+ "kMDItemUserPrivate"
+ "keyLength > 0"
+ "loadAllParametersForClient:locale:options:"
+ "localizedForKMDItemCardSubType:"
+ "localizedForKMDItemCardType:"
+ "localizedForKMDItemEventRestaurantMealType:"
+ "localizedForKMDItemEventStatus:"
+ "localizedForKMDItemEventSubType:"
+ "localizedLinkSubTypeForLinkSubType:"
+ "localizedLinkSubTypes"
+ "localizedLinkTypeForLinkType:"
+ "localizedLinkTypes"
+ "localizedPrefixForPrefix:"
+ "localized_keywords.mdplist"
+ "logOwner"
+ "logToken"
+ "logfd"
+ "logfdo"
+ "mailQueryID"
+ "matchInfo"
+ "messagesSharedLinkPrefix"
+ "messagesSharedLinkSubType"
+ "messagesSharedLinkType"
+ "no data found in config file %@ for event type."
+ "no data found in config file %@ for messages shared links."
+ "no handler"
+ "none"
+ "now"
+ "null"
+ "operation"
+ "overallCompleteness"
+ "overrideDefaultSearchableIndexForTestingWithSearchableIndex:"
+ "partiallyDonatedItems"
+ "performDonationAsync:"
+ "photosData"
+ "photosIdentificationDocumentsVersion"
+ "picked_up"
+ "pipeline"
+ "pipelineCompleteness"
+ "pipelineCompletenessFirstTimeBucket"
+ "pipelineCompletenessHeuristicScore"
+ "pipelineCompletenessSecondBucket"
+ "pipelineCompletenessThirdBucket"
+ "pipelineReportAge"
+ "place"
+ "predicateWithFieldType:equalsStringValue:error:"
+ "priorRevisionTokenWithKey:"
+ "processWorkItemsUpToRequestID:"
+ "publisherWithUseCase:options:"
+ "purchasedDate"
+ "read"
+ "ready_for_pickup"
+ "receivedDate"
+ "releasedDate"
+ "reminderRecurrenceRule"
+ "reminderTime"
+ "removeItemWithSourceItemIdentifier:error:"
+ "removeItemsMatchingPredicate:error:"
+ "removed"
+ "report-donation-progress"
+ "reportDate"
+ "reportDonationProgress:completionHandler:"
+ "reset"
+ "restoreSwizzledDefaultSearchableIndex"
+ "rewritten"
+ "sTestConnectionName: %@"
+ "scanHexLongLong:"
+ "scannerWithString:"
+ "sendEvent:"
+ "sentDate"
+ "setAlarmEnabled:"
+ "setAlarmRecurrenceRule:"
+ "setAlarmTime:"
+ "setAlternateTitles:"
+ "setBiomeStream:"
+ "setClockAlarmType:"
+ "setCompleted:"
+ "setContentCatalog:"
+ "setDaysOfTheWeek:"
+ "setDetectedCardSubTypes:"
+ "setEventEndDate:"
+ "setEventStartDate:"
+ "setFavorited:"
+ "setFlagged:"
+ "setHasReadPurpose:"
+ "setLocalizedLinkSubTypes:"
+ "setLocalizedLinkTypes:"
+ "setLogToken:"
+ "setMailQueryID:"
+ "setPhotosIdentificationDocumentsVersion:"
+ "setPlace:"
+ "setPurchasedDate:"
+ "setRead:"
+ "setReceivedDate:"
+ "setReleasedDate:"
+ "setReminderRecurrenceRule:"
+ "setReminderTime:"
+ "setSentDate:"
+ "setShouldSimulateErrors:"
+ "setSimulatedError:"
+ "setSnooze:"
+ "setSuggestedEdits:"
+ "setTriggerState:"
+ "setUserHidden:"
+ "setUserPrivate:"
+ "sharedQueue"
+ "shouldSimulateErrors"
+ "simulatedError"
+ "sinkWithCompletion:receiveInput:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets"
+ "softlink:r:path:/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices"
+ "source"
+ "sourceIdentifier"
+ "sourceIdentifierWithValue:error:"
+ "spotlightInlineTextContent"
+ "startIncrementalSetDonationWithItemType:descriptors:options:error:"
+ "stringIdentifier"
+ "stringReason"
+ "success"
+ "sufficientlyCompleteThreshold"
+ "suggestedEdits"
+ "swizzleDefaultSearchableIndex"
+ "testConnectionForUser:"
+ "testSearchConnection"
+ "textContentCompleteness"
+ "textContentCompletenessForBundle:completion:"
+ "timeIntervalSinceNow"
+ "timeUntilSpotlightDataExpires"
+ "translateItem:fromBundleId:error:"
+ "translator"
+ "triggerState"
+ "unarchivedArrayOfObjectsOfClasses:fromData:error:"
+ "underlyingError"
+ "underlyingErrorCode"
+ "underlyingErrorDomain"
+ "unused"
+ "updateRevisionToken:withKey:error:"
+ "updatedClientState"
+ "userActivities"
+ "userHidden"
+ "userPrivate"
+ "v104@0:8@16@24@32@40@48@56@64@72q80q88@?96"
+ "v16@?0@\"BMStoreEvent\"8"
+ "v16@?0@\"BPSCompletion\"8"
+ "v32@0:8i16B20@?24"
+ "v40@0:8@16q24q32"
+ "v48@0:8@16q24q32q40"
+ "v56@0:8@16q24q32@40@48"
+ "v60@0:8@16@24B32q36@44@?52"
+ "v64@0:8@16@24@32@40I48I52@?56"
+ "v72@0:8@16@24@32@40@48I56I60@?64"
+ "v88@0:8@16@24@32@40@48@56@64q72@?80"
+ "vector"
+ "with handler"
+ "writeCompletenessReports:forPipeline:error:"
+ "writeToBiomeStreamWithBundleID:itemCount:baseOperation:"
+ "writeToBiomeStreamWithBundleID:itemCount:baseOperation:identifier:reason:"
+ "writeToBiomeStreamWithBundleID:itemCount:baseOperation:reason:"
+ "writeToURL:options:error:"
+ "yet_to_be_shipped"
+ "{%@: \"%@\" %@%@}"
+ "{atomic<unsigned int>=\"__a_\"{__cxx_atomic_impl<unsigned int, std::__cxx_atomic_base_impl<unsigned int>>=\"__a_value\"AI}}"
+ "{priority_queue<(anonymous namespace)::WorkItem, std::vector<(anonymous namespace)::WorkItem>, (anonymous namespace)::WorkItemComparator>=\"c\"{vector<(anonymous namespace)::WorkItem, std::allocator<(anonymous namespace)::WorkItem>>=\"__begin_\"^{WorkItem}\"__end_\"^{WorkItem}\"\"{?=\"__cap_\"^{WorkItem}}}\"comp\"{WorkItemComparator=}}"
- "\rV"
- "<%@:%p %@ %@"
- "<%@:%p, %@>"
- "@\"CSDonatedEvent\""
- "@92@0:8^@16Q24^Q32@40@48^s56Q64{CSUnpackInfo=ssssss}72@84"
- "AI"
- "CSDonatedEvent"
- "CSInstantAnswer"
- "CSInstantAnswerAction"
- "Cleaned up removed domains: %@"
- "ClientTopHitRank"
- "Received %lu instant answers for query: %@, instant answers:\n%@"
- "SKGEmbeddingVersionManager"
- "T@\"CSDonatedEvent\",&,N"
- "T@\"CSDonatedEvent\",&,N,V_event"
- "T@\"NSMutableArray\",&,N,V_actions"
- "T@\"NSMutableDictionary\",&,V_mutableAttributes"
- "T@\"NSNumber\",R,N,V_lat"
- "T@\"NSNumber\",R,N,V_lng"
- "T@\"NSNumber\",R,N,V_type"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_domainDeleteQueue"
- "T@\"NSString\",C,N,V_type"
- "T@\"NSString\",C,N,V_url"
- "T@?,C,V_foundInstantAnswersHandlerOld"
- "TAI,N,V_requestID"
- "[14s]"
- "[personal answers][query] queryUnderstandingOutput has event intent, kQPQUIntentLabels = %@"
- "[qid=%ld] %@"
- "[qid=%ld] Finished with error error:%@/%ld"
- "[qid=%ld] Results type: %d "
- "[qid=%ld] Starting %@"
- "[qid=%ld][QoS=%u] Starting %@"
- "_actions"
- "_domainDeleteQueue"
- "_event"
- "_foundInstantAnswersHandlerOld"
- "_kMDItemDerivedIsMeRankingTextContentMatch"
- "_workItemsQoS"
- "_workSource"
- "actionWithType:andUrl:"
- "actions"
- "addAction:"
- "additionalInfo"
- "arrivalAirportCode"
- "arrivalAirportName"
- "arrivalDateTime"
- "arrivalTerminal"
- "async:critical:"
- "bookingInfoUrl"
- "checkInUrl"
- "com.apple.corespotlight.fileProviderDomainMonitor.domainDelete"
- "confirmationNumber"
- "courierName"
- "currentEmbeddingVersionDataReturningError:"
- "dataFromInstantAnswers:"
- "deliveryDateTime"
- "departureAirportCode"
- "departureAirportName"
- "departureDateTime"
- "departureTerminal"
- "docIDs"
- "domainDeleteQueue"
- "event"
- "eventFromData:"
- "flight_booking_info"
- "flight_checkin"
- "foundInstantAnswersHandlerOld"
- "fromAllowListedSender"
- "handleEvent"
- "handleFoundInstantAnswer:"
- "id=%ld"
- "id_ssn"
- "initWithEvent:"
- "initWithType:"
- "initWithType:andUrl:"
- "instantAnswersFromData:"
- "isInstantAnswerTriggerQuery:isCJK:isSearchTool:"
- "kMDItemEventRelatedMessageIdentifiers"
- "kMDItemEventRelatedSourceBundleIdentifiers"
- "merchantName"
- "orderDateTime"
- "personalAnswersEventIntentForQUOutput:isDebugLoggingEnabled:"
- "processInstantAnswersWithFoundItems:"
- "removeObjectAtIndex:"
- "senderIsCourier"
- "setActions:"
- "setAdditionalInfo:"
- "setArrivalAirportCode:"
- "setArrivalAirportName:"
- "setArrivalDateTime:"
- "setArrivalTerminal:"
- "setBookingInfoUrl:"
- "setCheckInUrl:"
- "setConfirmationNumber:"
- "setCourierName:"
- "setDeliveryDateTime:"
- "setDepartureAirportCode:"
- "setDepartureAirportName:"
- "setDepartureDateTime:"
- "setDepartureTerminal:"
- "setDocIDs:"
- "setDomainDeleteQueue:"
- "setDonatedEvent:"
- "setEvent:"
- "setFoundInstantAnswersHandlerOld:"
- "setFromAllowListedSender:"
- "setInstantAnswers:"
- "setMerchantName:"
- "setMutableAttributes:"
- "setOrderDateTime:"
- "setRequestID:"
- "setSenderIsCourier:"
- "setTrackingNumber:"
- "setTrackingUrl:"
- "setUrl:"
- "shipment"
- "shipment_tracking"
- "trackingNumber"
- "trackingUrl"
- "v28@0:8@?16B24"

```
