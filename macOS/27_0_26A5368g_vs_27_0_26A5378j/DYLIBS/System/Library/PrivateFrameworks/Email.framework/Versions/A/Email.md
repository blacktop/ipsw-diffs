## Email

> `/System/Library/PrivateFrameworks/Email.framework/Versions/A/Email`

```diff

-  __TEXT.__text: 0xebd20
-  __TEXT.__objc_methlist: 0xd8b4
-  __TEXT.__gcc_except_tab: 0x1be18
-  __TEXT.__const: 0x14cc
-  __TEXT.__cstring: 0xc75f
-  __TEXT.__oslogstring: 0x6993
+  __TEXT.__text: 0xef060
+  __TEXT.__objc_methlist: 0xd984
+  __TEXT.__gcc_except_tab: 0x1bf40
+  __TEXT.__const: 0x18cc
+  __TEXT.__cstring: 0xc86f
+  __TEXT.__oslogstring: 0x6bb3
   __TEXT.__dlopen_cstrs: 0x10a
-  __TEXT.__ustring: 0x154
-  __TEXT.__swift5_typeref: 0x3cc
-  __TEXT.__constg_swiftt: 0x464
+  __TEXT.__ustring: 0x170
+  __TEXT.__swift5_typeref: 0x486
+  __TEXT.__constg_swiftt: 0x538
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_reflstr: 0x32f
-  __TEXT.__swift5_fieldmd: 0x4c4
+  __TEXT.__swift5_reflstr: 0x40f
+  __TEXT.__swift5_fieldmd: 0x610
   __TEXT.__swift5_assocty: 0x120
-  __TEXT.__swift5_proto: 0xf8
-  __TEXT.__swift5_types: 0x68
-  __TEXT.__swift5_capture: 0x38
+  __TEXT.__swift5_proto: 0x130
+  __TEXT.__swift5_types: 0x7c
+  __TEXT.__swift5_capture: 0x48
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x82e0
-  __TEXT.__eh_frame: 0x200
+  __TEXT.__unwind_info: 0x8450
+  __TEXT.__eh_frame: 0x328
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1998
-  __DATA_CONST.__objc_classlist: 0x5a0
+  __DATA_CONST.__const: 0x19a8
+  __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x340
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6888
+  __DATA_CONST.__objc_selrefs: 0x68d8
   __DATA_CONST.__objc_protorefs: 0x118
-  __DATA_CONST.__objc_superrefs: 0x480
+  __DATA_CONST.__objc_superrefs: 0x488
   __DATA_CONST.__objc_arraydata: 0x1e8
-  __DATA_CONST.__got: 0xd38
-  __AUTH_CONST.__const: 0x5240
-  __AUTH_CONST.__cfstring: 0xa9e0
-  __AUTH_CONST.__objc_const: 0x17c50
+  __DATA_CONST.__got: 0xd60
+  __AUTH_CONST.__const: 0x54d0
+  __AUTH_CONST.__cfstring: 0xaaa0
+  __AUTH_CONST.__objc_const: 0x17df8
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0xa00
-  __AUTH.__objc_data: 0x4c0
-  __AUTH.__data: 0x158
-  __DATA.__objc_ivar: 0xd08
-  __DATA.__data: 0x2900
-  __DATA.__bss: 0x1ae0
-  __DATA_DIRTY.__objc_data: 0x3560
+  __AUTH_CONST.__auth_got: 0xa68
+  __AUTH.__objc_data: 0x1020
+  __AUTH.__data: 0x180
+  __DATA.__objc_ivar: 0xd10
+  __DATA.__data: 0x29e8
+  __DATA.__bss: 0x21e0
+  __DATA_DIRTY.__objc_data: 0x2b28
   __DATA_DIRTY.__data: 0x240
   __DATA_DIRTY.__bss: 0xcd0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5283
-  Symbols:   14439
-  CStrings:  3563
+  Functions: 5399
+  Symbols:   14519
+  CStrings:  3585
 
Sections:
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[CSSearchableItem(SFMailRankingSignals) em_isSemanticMatch]
+ -[CSSearchableItem(SFMailRankingSignals) em_isSyntacticMatch]
+ -[EMBaseMessageListItem searchRelevanceRank]
+ -[EMBaseMessageListItem setSearchRelevanceRank:]
+ -[EMDiagnosticInfoGatherer downloadLimitDiagnosticsWithCompletionHandler:]
+ -[EMDiagnosticInfoGatherer(DonationVisualizationDebugging) donationVisualizationDataWithCompletionHandler:]
+ -[EMDiagnosticInfoGatherer(DonationVisualizationDebugging) donationVisualizationMessageDetailsForDatabaseID:completionHandler:]
+ -[EMMessageListItemChange searchRelevanceRank]
+ -[EMMessageListItemChange setSearchRelevanceRank:]
+ -[EMSearchResultMetadata .cxx_destruct]
+ -[EMSearchResultMetadata initWithRankingSignals:rankPosition:]
+ -[EMSearchResultMetadata rankPosition]
+ -[EMSearchResultMetadata rankingSignals]
+ -[EMThread searchRelevanceRank]
+ -[EMThread setSearchRelevanceRank:]
+ OBJC_IVAR_$_EMBaseMessageListItem._searchRelevanceRank
+ OBJC_IVAR_$_EMMessageListItemChange._searchRelevanceRank
+ OBJC_IVAR_$_EMSearchResultMetadata._rankPosition
+ OBJC_IVAR_$_EMSearchResultMetadata._rankingSignals
+ OBJC_IVAR_$_EMThread._searchRelevanceRank
+ _EMGenerativeModelsEnhancedSiriAvailabilityDidChange
+ _EMIsCurrentUserManagedAppleAccountForShare
+ _EMMessageListItemKeyPathSearchRelevanceRank
+ _EMPersistenceStatisticsKeyAllKnownItemsIsPartial
+ _EMSearchIndexAgeBucketBodiesIndexedMetric
+ _EMSearchIndexAgeBucketHeadersIndexedMetric
+ _EMSearchIndexAgeBucketKeyPrefix
+ _EMSearchIndexAgeBucketTotalMetric
+ _EMStartObservingEnhancedSiriAvailability
+ _OBJC_CLASS_$_EMSearchResultMetadata
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$__TtC5Email34EMEnhancedSiriAvailabilityObserver
+ _OBJC_METACLASS_$_EMSearchResultMetadata
+ _OBJC_METACLASS_$__TtC5Email34EMEnhancedSiriAvailabilityObserver
+ _OUTLINED_FUNCTION_6
+ __80-[EMHideMyEmail generateReplyToEmailForRecipient:hmeAddress:account:completion:]_block_invoke_3
+ __CLASS_METHODS__TtC5Email34EMEnhancedSiriAvailabilityObserver
+ __DATA__TtC5Email34EMEnhancedSiriAvailabilityObserver
+ __INSTANCE_METHODS__TtC5Email34EMEnhancedSiriAvailabilityObserver
+ __IVARS__TtC5Email34EMEnhancedSiriAvailabilityObserver
+ __METACLASS_DATA__TtC5Email34EMEnhancedSiriAvailabilityObserver
+ __OBJC_$_INSTANCE_METHODS_EMDiagnosticInfoGatherer(DonationVisualizationDebugging)
+ __OBJC_$_INSTANCE_METHODS_EMSearchResultMetadata
+ __OBJC_$_INSTANCE_VARIABLES_EMSearchResultMetadata
+ __OBJC_$_PROP_LIST_CSSearchableItem_$_SFMailRankingSignals
+ __OBJC_$_PROP_LIST_EMSearchResultMetadata
+ __OBJC_CLASS_RO_$_EMSearchResultMetadata
+ __OBJC_METACLASS_RO_$_EMSearchResultMetadata
+ ___80-[EMHideMyEmail generateReplyToEmailForRecipient:hmeAddress:account:completion:]_block_invoke_3
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_memcpy0_1
+ ___swift_memcpy80_8
+ ___swift_memcpy8_8
+ __swift_closure_destructor
+ _associated conformance 5Email26EMDownloadLimitDiagnosticsV10CodingKeys33_3EAB6CF011A973CBB1484E4E568085C7LLOSHAASQ
+ _associated conformance 5Email26EMDownloadLimitDiagnosticsV10CodingKeys33_3EAB6CF011A973CBB1484E4E568085C7LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 5Email26EMDownloadLimitDiagnosticsV10CodingKeys33_3EAB6CF011A973CBB1484E4E568085C7LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 5Email26EMDownloadLimitDiagnosticsV7AccountV10CodingKeys33_3EAB6CF011A973CBB1484E4E568085C7LLOSHAASQ
+ _associated conformance 5Email26EMDownloadLimitDiagnosticsV7AccountV10CodingKeys33_3EAB6CF011A973CBB1484E4E568085C7LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 5Email26EMDownloadLimitDiagnosticsV7AccountV10CodingKeys33_3EAB6CF011A973CBB1484E4E568085C7LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _objc_msgSend$currentUserParticipant
+ _objc_msgSend$donationVisualizationDataWithCompletionHandler:
+ _objc_msgSend$donationVisualizationMessageDetailsForDatabaseID:completionHandler:
+ _objc_msgSend$downloadLimitDiagnosticsWithCompletionHandler:
+ _objc_msgSend$em_isSemanticMatch
+ _objc_msgSend$em_isSyntacticMatch
+ _objc_msgSend$groupList
+ _objc_msgSend$phoneNumber
+ _objc_msgSend$searchRelevanceRank
+ _objc_msgSend$setSearchRelevanceRank:
+ _swift_initStackObject
+ _swift_setDeallocating
+ _symbolic Say_____G 5Email26EMDownloadLimitDiagnosticsV7AccountV
+ _symbolic Sb
+ _symbolic _____ 5Email26EMDownloadLimitDiagnosticsV
+ _symbolic _____ 5Email26EMDownloadLimitDiagnosticsV10CodingKeys33_3EAB6CF011A973CBB1484E4E568085C7LLO
+ _symbolic _____ 5Email26EMDownloadLimitDiagnosticsV7AccountV
+ _symbolic _____ 5Email26EMDownloadLimitDiagnosticsV7AccountV10CodingKeys33_3EAB6CF011A973CBB1484E4E568085C7LLO
+ _symbolic _____ 5Email34EMEnhancedSiriAvailabilityObserverC
+ _symbolic ______ypt s11AnyHashableV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 5Email26EMDownloadLimitDiagnosticsV10CodingKeys33_3EAB6CF011A973CBB1484E4E568085C7LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 5Email26EMDownloadLimitDiagnosticsV7AccountV10CodingKeys33_3EAB6CF011A973CBB1484E4E568085C7LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 5Email26EMDownloadLimitDiagnosticsV10CodingKeys33_3EAB6CF011A973CBB1484E4E568085C7LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 5Email26EMDownloadLimitDiagnosticsV7AccountV10CodingKeys33_3EAB6CF011A973CBB1484E4E568085C7LLO
+ _symbolic _____y______yptG s23_ContiguousArrayStorageC s11AnyHashableV
+ _symbolic _____y_____ypG s18_DictionaryStorageC s11AnyHashableV
+ _type_layout_string 5Email26EMDownloadLimitDiagnosticsV
+ _type_layout_string 5Email26EMDownloadLimitDiagnosticsV7AccountV
- -[EMBaseMessageListItem searchRelevanceScore]
- -[EMBaseMessageListItem setSearchRelevanceScore:]
- -[EMMessageListItemChange searchRelevanceScore]
- -[EMMessageListItemChange setSearchRelevanceScore:]
- -[EMThread searchRelevanceScore]
- -[EMThread setSearchRelevanceScore:]
- OBJC_IVAR_$_EMBaseMessageListItem._searchRelevanceScore
- OBJC_IVAR_$_EMMessageListItemChange._searchRelevanceScore
- OBJC_IVAR_$_EMThread._searchRelevanceScore
- _EMIsManagedAppleAccount
- _EMMessageListItemKeyPathSearchRelevanceScore
- _EMPersistenceStatisticsKeyPercentIndexedLastMonth
- _EMPersistenceStatisticsKeyPercentIndexedLastTwoDays
- _EMPersistenceStatisticsKeyPercentUnindexedBodiesInFrecentMailboxes
- _EMUserDefaultHasCompletedAppleIntelligenceOnboarding
- __80-[EMHideMyEmail generateReplyToEmailForRecipient:hmeAddress:account:completion:]_block_invoke_2
- __OBJC_$_INSTANCE_METHODS_EMDiagnosticInfoGatherer
- _objc_msgSend$searchRelevanceScore
- _objc_msgSend$setSearchRelevanceScore:
- _swift_runtimeSupportsNoncopyableTypes
- get_type_metadata 15Synchronization5MutexVy5Email21ActivityStateObserverC0E0OG noncopyable
CStrings:
+ "%@\n\tConversationID:%@\n\tSubject:%@\n\tSenderList:%@\n\tToList:%@\n\tCCList:%@\n\tSummary:%@\n\tGenerated Summary:%@ (isUrgent = %@)\n\tFlags:%@\n\tConversationNotificationLevel:%ld\n\tCategory:%@\n\tBusinessLogoID:%@\n\tIsVIP:%@\n\tIsBlocked:%@\n\tSearchResultType:%ld\n\tSearchRelevanceRank:%@\n\tUnsubscribeType:%ld\n\tDate:%@\n\tDisplayDate:%@\n\tMailboxes:%@\n\tCount:%lu"
+ "%@\n\tConversationID:%@\n\tSubject:%@\n\tSenderList:%@\n\tToList:%@\n\tCCList:%@\n\tSummary:%@\n\tGenerated Summary:%@ (isUrgent = %@)\n\tFlags:%@\n\tConversationNotificationLevel:%ld\n\tCategory:%@\n\tBusinessLogoID:%@\n\tIsVIP:%@\n\tIsBlocked:%@\n\tSearchResultType:%ld\n\tSearchRelevanceRank:%@\n\tUnsubscribeType:%ld\n\tDate:%@\n\tDisplayDate:%@\n\tMailboxes:%@\n\tCount:%lu\n\tSupportsArchiving:%@ \n\tShouldArchive:%@\n\tdisplayMessageItemID:%@"
+ "%@\n\tMailboxes:%@\n\tSenderAddress:%@\n\tSubject:%@ \n\tCategory:%@\n\tBusinessID:%llu\n\tBusinessLogoID:%@\n\tisAuthenticated:%@\n\tToList:%@ \n\tCCList:%@ \n\tBCCList:%@ \n\tFlags:%@ \n\tConversationNotificationLevel:%ld \n\tIsVIP:%@ \n\tIsBlocked:%@ \n\tSearchResultType:%ld \n\tSearchRelevanceRank:%@ \n\tUnsubscribeType:%ld \n\tConversationID:%@ \n\tDate:%@ \n\tDisplayDate:%@ \n\tSummary:%@\n\tGenerated Summary:%@ (isUrgent = %@)"
+ "%@\n\tObjectID:%@\n\tMailboxes:%@\n\tSenderAddress:%@\n\tSubject:%@ \n\tCategory:%@\n\tBusinessID:%llu\n\tBusinessLogoID:%@\n\tisAuthenticated:%@\n\tToList:%@ \n\tCCList:%@ \n\tBCCList:%@ \n\tFlags:%@ \n\tConversationNotificationLevel:%ld \n\tIsVIP:%@ \n\tIsBlocked:%@ \n\tSearchResultType:%ld \n\tSearchRelevanceRank:%@ \n\tUnsubscribeType:%ld \n\tConversationID:%@ \n\tDate:%@ \n\tDisplayDate:%@ \n\tRemind Me:%@ \n\tFollow Up:%@ \n\tSummary:%@ \n\tGenerated Summary:%@ (isUrgent = %@)\n\tSupportsArchiving:%@ \n\tShouldArchive:%@"
+ "%@ \n\tConversationID:%@ \n\tFlags:%@ \n\tConversationNotificationLevel:%ld \n\tIsBlocked:%@ \n\tSearchResultType:%ld \n\tSearchRelevanceRank:%@ \n\tunsubscribeType:%ld \n\tDate:%@ \n\tSupports Archiving:%@ \n\tShould Archive By Default:%@"
+ "Categorizing…"
+ "EFPropertyKey_searchRelevanceRank"
+ "EMEnhancedSiriIsAvailable"
+ "EMGenerativeModelsEnhancedSiriAvailabilityDidChange"
+ "EMHMERecipientCreationRequest.m"
+ "Enhanced Siri availability changed to isAvailable=%{bool}d; posting EMGenerativeModelsEnhancedSiriAvailabilityDidChange"
+ "Failed to parse HME address string: %{private}@"
+ "Generating replyTo for recipient:%{private}@ rawHME:%{private}@ processedHME:%{private}@"
+ "HME address parsed but has no simpleAddress: localPart=%{private}@ domain=%{private}@ isGroup=%{BOOL}d"
+ "Invalid HME address format"
+ "Missing required fields for HME request: hmeAddress=%{private}@ recipient=%{private}@"
+ "Unable to create a secure connection to the server (“%1$@” %2$@)."
+ "ageBucket"
+ "allKnownItemsIsPartial"
+ "bodiesIndexed"
+ "generateReplyToEmailForRecipient: missing required argument — account=%{public}@ recipientAddress=%{private}@ processedHMEAddress=%{private}@"
+ "headersIndexed"
+ "hmeAddress"
+ "messagesDownloadedCount"
+ "olderMessagesIndexedCount"
+ "overQuotaCount24h"
+ "recipient"
+ "searchRelevanceRank"
+ "searchRelevanceRank: %@"
+ "serverRecentlyUnavailable"
+ "serverUnavailableCount24h"
+ "total"
- "% indexed last 2 days"
- "% indexed last month"
- "% unindexed bodies in frecent"
- "%@\n\tConversationID:%@\n\tSubject:%@\n\tSenderList:%@\n\tToList:%@\n\tCCList:%@\n\tSummary:%@\n\tGenerated Summary:%@ (isUrgent = %@)\n\tFlags:%@\n\tConversationNotificationLevel:%ld\n\tCategory:%@\n\tBusinessLogoID:%@\n\tIsVIP:%@\n\tIsBlocked:%@\n\tSearchResultType:%ld\n\tSearchRelevanceScore:%@\n\tUnsubscribeType:%ld\n\tDate:%@\n\tDisplayDate:%@\n\tMailboxes:%@\n\tCount:%lu"
- "%@\n\tConversationID:%@\n\tSubject:%@\n\tSenderList:%@\n\tToList:%@\n\tCCList:%@\n\tSummary:%@\n\tGenerated Summary:%@ (isUrgent = %@)\n\tFlags:%@\n\tConversationNotificationLevel:%ld\n\tCategory:%@\n\tBusinessLogoID:%@\n\tIsVIP:%@\n\tIsBlocked:%@\n\tSearchResultType:%ld\n\tSearchRelevanceScore:%@\n\tUnsubscribeType:%ld\n\tDate:%@\n\tDisplayDate:%@\n\tMailboxes:%@\n\tCount:%lu\n\tSupportsArchiving:%@ \n\tShouldArchive:%@\n\tdisplayMessageItemID:%@"
- "%@\n\tMailboxes:%@\n\tSenderAddress:%@\n\tSubject:%@ \n\tCategory:%@\n\tBusinessID:%llu\n\tBusinessLogoID:%@\n\tisAuthenticated:%@\n\tToList:%@ \n\tCCList:%@ \n\tBCCList:%@ \n\tFlags:%@ \n\tConversationNotificationLevel:%ld \n\tIsVIP:%@ \n\tIsBlocked:%@ \n\tSearchResultType:%ld \n\tSearchRelevanceScore:%@ \n\tUnsubscribeType:%ld \n\tConversationID:%@ \n\tDate:%@ \n\tDisplayDate:%@ \n\tSummary:%@\n\tGenerated Summary:%@ (isUrgent = %@)"
- "%@\n\tObjectID:%@\n\tMailboxes:%@\n\tSenderAddress:%@\n\tSubject:%@ \n\tCategory:%@\n\tBusinessID:%llu\n\tBusinessLogoID:%@\n\tisAuthenticated:%@\n\tToList:%@ \n\tCCList:%@ \n\tBCCList:%@ \n\tFlags:%@ \n\tConversationNotificationLevel:%ld \n\tIsVIP:%@ \n\tIsBlocked:%@ \n\tSearchResultType:%ld \n\tSearchRelevanceScore:%@ \n\tUnsubscribeType:%ld \n\tConversationID:%@ \n\tDate:%@ \n\tDisplayDate:%@ \n\tRemind Me:%@ \n\tFollow Up:%@ \n\tSummary:%@ \n\tGenerated Summary:%@ (isUrgent = %@)\n\tSupportsArchiving:%@ \n\tShouldArchive:%@"
- "%@ \n\tConversationID:%@ \n\tFlags:%@ \n\tConversationNotificationLevel:%ld \n\tIsBlocked:%@ \n\tSearchResultType:%ld \n\tSearchRelevanceScore:%@ \n\tunsubscribeType:%ld \n\tDate:%@ \n\tSupports Archiving:%@ \n\tShould Archive By Default:%@"
- "Categorizing..."
- "EFPropertyKey_searchRelevanceScore"
- "HasCompletedAppleIntelligenceOnboarding"
- "ReplyTo address Request %@ for recipient:%@ hmeAddress:%@"
- "Unable to create a secure connection to the server (”%1$@” %2$@)."
- "searchRelevanceScore"
- "searchRelevanceScore: %@"

```
