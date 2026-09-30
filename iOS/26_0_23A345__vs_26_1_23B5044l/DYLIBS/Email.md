## Email

> `/System/Library/PrivateFrameworks/Email.framework/Email`

```diff

-3864.100.1.2.9
-  __TEXT.__text: 0xcc1b0
+3864.200.33.2.2
+  __TEXT.__text: 0xcd0f4
   __TEXT.__auth_stubs: 0x14e0
-  __TEXT.__objc_methlist: 0xc6fc
-  __TEXT.__gcc_except_tab: 0x1ac18
+  __TEXT.__objc_methlist: 0xc824
+  __TEXT.__gcc_except_tab: 0x1af08
   __TEXT.__const: 0x11b8
-  __TEXT.__cstring: 0xb42c
-  __TEXT.__oslogstring: 0x6023
+  __TEXT.__cstring: 0xb45c
+  __TEXT.__oslogstring: 0x6083
   __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__ustring: 0x154
   __TEXT.__constg_swiftt: 0x3e8

   __TEXT.__swift5_capture: 0x38
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x78d0
+  __TEXT.__unwind_info: 0x7988
   __TEXT.__eh_frame: 0x1f8
-  __TEXT.__objc_classname: 0x1a20
-  __TEXT.__objc_methname: 0x1a8db
-  __TEXT.__objc_methtype: 0x467f
-  __TEXT.__objc_stubs: 0x11860
-  __DATA_CONST.__got: 0xc60
-  __DATA_CONST.__const: 0x4158
+  __TEXT.__objc_classname: 0x1a1d
+  __TEXT.__objc_methname: 0x1ae89
+  __TEXT.__objc_methtype: 0x46e3
+  __TEXT.__objc_stubs: 0x11b40
+  __DATA_CONST.__got: 0xc90
+  __DATA_CONST.__const: 0x4208
   __DATA_CONST.__objc_classlist: 0x568
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x330
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5cf0
+  __DATA_CONST.__objc_selrefs: 0x5de0
   __DATA_CONST.__objc_protorefs: 0x118
   __DATA_CONST.__objc_superrefs: 0x470
   __DATA_CONST.__objc_arraydata: 0x1d0
   __AUTH_CONST.__auth_got: 0xa80
   __AUTH_CONST.__const: 0x1828
-  __AUTH_CONST.__cfstring: 0x9a00
-  __AUTH_CONST.__objc_const: 0x15f18
+  __AUTH_CONST.__cfstring: 0x9a60
+  __AUTH_CONST.__objc_const: 0x16060
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x618
   __AUTH.__data: 0x158
-  __DATA.__objc_ivar: 0xba4
+  __DATA.__objc_ivar: 0xbc0
   __DATA.__data: 0x2898
-  __DATA.__bss: 0x1b80
+  __DATA.__bss: 0x1ba0
   __DATA_DIRTY.__objc_data: 0x31b0
   __DATA_DIRTY.__data: 0x1e0
-  __DATA_DIRTY.__bss: 0x860
+  __DATA_DIRTY.__bss: 0x848
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/LockdownMode.framework/LockdownMode
   - /System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy
+  - /System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FB9DA18C-04CA-3FE4-8654-D21B2133736A
-  Functions: 4706
-  Symbols:   17484
-  CStrings:  8296
+  UUID: D704C17E-E8BE-3FA5-8101-D55E4AAC907A
+  Functions: 4731
+  Symbols:   17593
+  CStrings:  8346
 
Symbols:
+ +[EMInternalPreferences registerForDefaultChanges]
+ +[EMParsecInstantAnswers _dateComponentsForDate:inTimeZone:]
+ +[EMParsecInstantAnswers _flightArrivalDateFromUpdatedFlightInformation:]
+ +[EMParsecInstantAnswers _flightDepartureDateFromUpdatedFlightInformation:]
+ +[EMParsecInstantAnswers flightArrivalDateComponentsFromUpdatedFlightInformation:arrivalTimeZone:]
+ +[EMParsecInstantAnswers flightDepartureDateComponentsFromUpdatedFlightInformation:departureTimeZone:]
+ +[EMParsecInstantAnswers flightURLFromUpdatedFlightInformation:]
+ +[EMParsecInstantAnswers inlineCardWithManageReservationButton:bodyCardSectionID:buttonsCardSectionID:]
+ +[EMParsecInstantAnswers updatedFlightInformationForInstantAnswer:]
+ -[EMCachingContactStore _commonInitWithStore:options:emailAddressCache:cacheFuture:]
+ -[EMCachingContactStore _commonInitWithStore:options:emailAddressCache:cacheFuture:scheduler:]
+ -[EMCachingContactStore _scheduleEmailAddressCachePopulationImpl]
+ -[EMCachingContactStore cacheCanStartFuture]
+ -[EMCachingContactStore emailAddressCacheFinishedFuture]
+ -[EMCachingContactStore emailAddressCacheFinished]
+ -[EMCachingContactStore initForTestingWithStore:options:cacheFuture:scheduler:]
+ -[EMCachingContactStore initWithOptions:cacheFuture:]
+ -[EMCachingContactStore initWithStore:options:cacheFuture:]
+ -[EMCachingContactStore setCacheCanStartFuture:]
+ -[EMCachingContactStore setEmailAddressCacheFinished:]
+ -[EMDaemonInterface wantsBlockedSenderManager]
+ -[EMDiagnosticInfoGatherer gatherIndexingDiagnosticsWithRedaction:completionHandler:]
+ -[EMInstantAnswer bodyCardSectionID]
+ -[EMInstantAnswer buttonsCardSectionID]
+ -[EMInstantAnswerFlight infoIsLive]
+ -[EMMessageRepository messageForSearchIndexerIdentifier:]
+ GCC_except_table171
+ GCC_except_table183
+ GCC_except_table184
+ GCC_except_table189
+ GCC_except_table190
+ GCC_except_table196
+ GCC_except_table200
+ GCC_except_table201
+ GCC_except_table206
+ GCC_except_table211
+ GCC_except_table212
+ GCC_except_table216
+ GCC_except_table219
+ GCC_except_table222
+ GCC_except_table223
+ GCC_except_table229
+ _EMParsecInstantAnswersFlightArrivalActualTimeKey
+ _EMParsecInstantAnswersFlightArrivalGateKey
+ _EMParsecInstantAnswersFlightArrivalTerminalKey
+ _EMParsecInstantAnswersFlightCarrierWebsiteKey
+ _EMParsecInstantAnswersFlightDepartureActualTimeKey
+ _EMParsecInstantAnswersFlightDepartureGateKey
+ _EMParsecInstantAnswersFlightDepartureTerminalKey
+ _EMParsecInstantAnswersFlightDivertedAirportKey
+ _EMParsecInstantAnswersFlightStatusKey
+ _OBJC_CLASS_$_SFButtonListCardSection
+ _OBJC_CLASS_$_SFCard
+ _OBJC_CLASS_$_SFCardSection
+ _OBJC_CLASS_$_SFCommandButtonItem
+ _OBJC_CLASS_$_SFManageReservationCommand
+ _OBJC_CLASS_$_SFViewEmailCommand
+ _OBJC_IVAR_$_EMCachingContactStore._cacheCanStartFuture
+ _OBJC_IVAR_$_EMCachingContactStore._emailAddressCacheFinished
+ _OBJC_IVAR_$_EMDaemonInterface._wantsBlockedSenderManager
+ _OBJC_IVAR_$_EMInstantAnswer._bodyCardSectionID
+ _OBJC_IVAR_$_EMInstantAnswer._buttonsCardSectionID
+ _OBJC_IVAR_$_EMInstantAnswerFlight._infoIsLive
+ _OBJC_IVAR_$_EMMailbox._accountLock
+ ___111+[EMMessageListItemPredicates predicateForMessagesWithActiveFollowUpInAccountsOfMailboxes:mailboxTypeResolver:]_block_invoke.132
+ ___203-[EMSearchableIndexTopHitsQuery initWithSearchString:filterQueries:bundleID:keyboardLanguage:updatedSuggestion:generateSuggestions:logDescription:resultLimit:suggestionLimit:customFlags:feedbackQueryID:]_block_invoke.109
+ ___44-[EMMessageRepository metadataForAddresses:]_block_invoke.508
+ ___44-[EMMessageRepository metadataForAddresses:]_block_invoke.508.cold.1
+ ___45-[EMDaemonInterface resetProtocolConnections]_block_invoke.326
+ ___50+[EMInternalPreferences registerForDefaultChanges]_block_invoke
+ ___50-[EMDaemonInterface _connectionForProtocol:error:]_block_invoke.323
+ ___54-[EMMessageRepository persistentIDForMessageObjectID:]_block_invoke.537
+ ___54-[EMMessageRepository persistentIDForMessageObjectID:]_block_invoke.537.cold.1
+ ___55-[EMMessageRepository setUpURLCacheWithMemoryCapacity:]_block_invoke.517
+ ___55-[EMMessageRepository setUpURLCacheWithMemoryCapacity:]_block_invoke.520
+ ___57-[EMMessageRepository messageForSearchIndexerIdentifier:]_block_invoke
+ ___58-[EMMessageRepository cachedMetadataJSONForKey:messageID:]_block_invoke.503
+ ___61-[EMContentRepresentation _distantLoaderBlockForContentItem:]_block_invoke.154
+ ___65-[EMCachingContactStore _scheduleEmailAddressCachePopulationImpl]_block_invoke
+ ___65-[EMCachingContactStore _scheduleEmailAddressCachePopulationImpl]_block_invoke.cold.1
+ ___74-[EMMessageRepository requestRichLinkURLsForMessageIDs:completionHandler:]_block_invoke.491
+ ___76-[EMMessageRepository requestAttachmentURLsForMessageIDs:completionHandler:]_block_invoke.489
+ ___82-[EMMessageRepository _removeItemsFromObservedItemsCacheIfNotObservedByObservers:]_block_invoke.480
+ ___86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.242
+ ___86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.247
+ ___86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.255
+ ___88-[EMMessageRepository requestRichLinkMetadataForRichLinkID:messageID:completionHandler:]_block_invoke.487
+ ___block_descriptor_40_ea8_32s_e39_"<EFFuture>"16?0"EMMessageObjectID"8ls32l8
+ ___block_descriptor_40_ea8_32w_e16_v16?0"NSNull"8lw32l8
+ ___block_descriptor_48_ea8_32s40r_e48_v32?0"EMObjectID"8"<EMMessageListItem>"16^B24ls32l8r40l8
+ ___block_literal_global.128
+ ___block_literal_global.131
+ ___block_literal_global.135
+ ___block_literal_global.138
+ ___block_literal_global.150
+ ___block_literal_global.163
+ ___block_literal_global.168
+ ___block_literal_global.179
+ ___block_literal_global.184
+ ___block_literal_global.259
+ ___block_literal_global.328
+ ___block_literal_global.412
+ ___block_literal_global.465
+ ___block_literal_global.500
+ ___block_literal_global.511
+ ___block_literal_global.550
+ ___block_literal_global.552
+ __scheduleEmailAddressCachePopulationImpl.cacheRequestCount
+ _log.log.86
+ _log.onceToken.87
+ _objc_msgSend$_commonInitWithStore:options:emailAddressCache:cacheFuture:
+ _objc_msgSend$_commonInitWithStore:options:emailAddressCache:cacheFuture:scheduler:
+ _objc_msgSend$_dateComponentsForDate:inTimeZone:
+ _objc_msgSend$_flightArrivalDateFromUpdatedFlightInformation:
+ _objc_msgSend$_flightDepartureDateFromUpdatedFlightInformation:
+ _objc_msgSend$_scheduleEmailAddressCachePopulationImpl
+ _objc_msgSend$bodyCardSectionID
+ _objc_msgSend$buttonsCardSectionID
+ _objc_msgSend$cacheCanStartFuture
+ _objc_msgSend$calendarWithIdentifier:
+ _objc_msgSend$contactExistsForEmailAddress:
+ _objc_msgSend$emailAddressCacheFinished
+ _objc_msgSend$flightArrivalDateComponentsFromUpdatedFlightInformation:arrivalTimeZone:
+ _objc_msgSend$flightDepartureDateComponentsFromUpdatedFlightInformation:departureTimeZone:
+ _objc_msgSend$flightURLFromUpdatedFlightInformation:
+ _objc_msgSend$gatherIndexingDiagnosticsWithRedaction:completionHandler:
+ _objc_msgSend$infoIsLive
+ _objc_msgSend$initWithOptions:cacheFuture:
+ _objc_msgSend$initWithStore:options:cacheFuture:
+ _objc_msgSend$messageObjectIDForSearchIndexerIdentifier:completionHandler:
+ _objc_msgSend$setButtons:
+ _objc_msgSend$setCardSectionId:
+ _objc_msgSend$setCardSections:
+ _objc_msgSend$setCommand:
+ _objc_msgSend$setEmailAddressCacheFinished:
+ _objc_msgSend$setUniqueId:
+ _objc_msgSend$updatedFlightInformationForInstantAnswer:
+ _objc_msgSend$wantsBlockedSenderManager
+ _registerForDefaultChanges.onceToken
- +[EMParsecInstantAnswers updatedFlightURLForInstantAnswer:]
- -[EMCachingContactStore _commonInitWithStore:options:emailAddressCache:]
- -[EMDiagnosticInfoGatherer gatherIndexingDiagnosticsWithCompletionHandler:]
- GCC_except_table175
- GCC_except_table187
- GCC_except_table188
- GCC_except_table192
- GCC_except_table197
- GCC_except_table198
- GCC_except_table202
- GCC_except_table209
- GCC_except_table210
- GCC_except_table214
- GCC_except_table215
- GCC_except_table220
- GCC_except_table221
- GCC_except_table227
- _EMUserDefaultAddedCommerceMailboxToFavorites
- ___111+[EMMessageListItemPredicates predicateForMessagesWithActiveFollowUpInAccountsOfMailboxes:mailboxTypeResolver:]_block_invoke.133
- ___203-[EMSearchableIndexTopHitsQuery initWithSearchString:filterQueries:bundleID:keyboardLanguage:updatedSuggestion:generateSuggestions:logDescription:resultLimit:suggestionLimit:customFlags:feedbackQueryID:]_block_invoke.112
- ___43+[EMInternalPreferences preferenceEnabled:]_block_invoke
- ___44-[EMMessageRepository metadataForAddresses:]_block_invoke.506
- ___44-[EMMessageRepository metadataForAddresses:]_block_invoke.506.cold.1
- ___45-[EMDaemonInterface resetProtocolConnections]_block_invoke.325
- ___50-[EMDaemonInterface _connectionForProtocol:error:]_block_invoke.322
- ___54-[EMMessageRepository persistentIDForMessageObjectID:]_block_invoke.534
- ___54-[EMMessageRepository persistentIDForMessageObjectID:]_block_invoke.534.cold.1
- ___55-[EMMessageRepository setUpURLCacheWithMemoryCapacity:]_block_invoke.515
- ___55-[EMMessageRepository setUpURLCacheWithMemoryCapacity:]_block_invoke.518
- ___58-[EMMessageRepository cachedMetadataJSONForKey:messageID:]_block_invoke.501
- ___61-[EMCachingContactStore _scheduleEmailAddressCachePopulation]_block_invoke.cold.1
- ___61-[EMContentRepresentation _distantLoaderBlockForContentItem:]_block_invoke.157
- ___74-[EMMessageRepository requestRichLinkURLsForMessageIDs:completionHandler:]_block_invoke.489
- ___76-[EMMessageRepository requestAttachmentURLsForMessageIDs:completionHandler:]_block_invoke.487
- ___82-[EMMessageRepository _removeItemsFromObservedItemsCacheIfNotObservedByObservers:]_block_invoke.478
- ___86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.240
- ___86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.243
- ___86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.253
- ___88-[EMMessageRepository requestRichLinkMetadataForRichLinkID:messageID:completionHandler:]_block_invoke.485
- ___block_literal_global.129
- ___block_literal_global.132
- ___block_literal_global.136
- ___block_literal_global.139
- ___block_literal_global.151
- ___block_literal_global.161
- ___block_literal_global.169
- ___block_literal_global.180
- ___block_literal_global.185
- ___block_literal_global.257
- ___block_literal_global.327
- ___block_literal_global.415
- ___block_literal_global.459
- ___block_literal_global.498
- ___block_literal_global.509
- ___block_literal_global.544
- ___block_literal_global.549
- __scheduleEmailAddressCachePopulation.cacheRequestCount
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_Email
- _log.log.88
- _log.onceToken.89
- _objc_msgSend$_commonInitWithStore:options:emailAddressCache:
- _objc_msgSend$gatherIndexingDiagnosticsWithCompletionHandler:
- _objc_msgSend$initWithStore:options:
- _objc_msgSend$predicateForUnfiredReadLaterMessagesInInbox
- _objc_msgSend$updatedFlightURLForInstantAnswer:
- _preferenceEnabled:.onceToken
CStrings:
+ "...\n"
+ "@\"<EFFuture>\"16@?0@\"EMMessageObjectID\"8"
+ "@32@0:8Q16@24"
+ "@36@0:8B16@20@28"
+ "EFPropertyKey_bodyCardSectionID"
+ "EFPropertyKey_buttonsCardSectionID"
+ "EFPropertyKey_infoIsLive"
+ "T@\"EAEmailAddressSet\",&,N,V_blockedSenders"
+ "T@\"EFFuture\",&,N,V_cacheCanStartFuture"
+ "T@\"EFPromise\",&,V_emailAddressCacheFinished"
+ "T@\"NSString\",R,N,V_bodyCardSectionID"
+ "T@\"NSString\",R,N,V_buttonsCardSectionID"
+ "TB,R,N,V_infoIsLive"
+ "TB,R,N,V_wantsBlockedSenderManager"
+ "[instant answers][flights api] successfully updated flight instant answer with live info."
+ "_accountLock"
+ "_bodyCardSectionID"
+ "_buttonsCardSectionID"
+ "_cacheCanStartFuture"
+ "_commonInitWithStore:options:emailAddressCache:cacheFuture:"
+ "_commonInitWithStore:options:emailAddressCache:cacheFuture:scheduler:"
+ "_dateComponentsForDate:inTimeZone:"
+ "_emailAddressCacheFinished"
+ "_flightArrivalDateFromUpdatedFlightInformation:"
+ "_flightDepartureDateFromUpdatedFlightInformation:"
+ "_infoIsLive"
+ "_scheduleEmailAddressCachePopulationImpl"
+ "_wantsBlockedSenderManager"
+ "bodyCardSectionID"
+ "buttonsCardSectionID"
+ "cacheCanStartFuture"
+ "calendarWithIdentifier:"
+ "emailAddressCacheFinished"
+ "emailAddressCacheFinishedFuture"
+ "flightArrivalDateComponentsFromUpdatedFlightInformation:arrivalTimeZone:"
+ "flightDepartureDateComponentsFromUpdatedFlightInformation:departureTimeZone:"
+ "flightURLFromUpdatedFlightInformation:"
+ "gatherIndexingDiagnosticsWithRedaction:completionHandler:"
+ "infoIsLive"
+ "initForTestingWithStore:options:cacheFuture:scheduler:"
+ "initWithOptions:cacheFuture:"
+ "initWithStore:options:cacheFuture:"
+ "inlineCardWithManageReservationButton:bodyCardSectionID:buttonsCardSectionID:"
+ "messageForSearchIndexerIdentifier:"
+ "messageObjectIDForSearchIndexerIdentifier:completionHandler:"
+ "registerForDefaultChanges"
+ "setButtons:"
+ "setCacheCanStartFuture:"
+ "setCardSectionId:"
+ "setCardSections:"
+ "setCommand:"
+ "setEmailAddressCacheFinished:"
+ "setUniqueId:"
+ "updatedFlightInformationForInstantAnswer:"
+ "v16@?0@\"NSNull\"8"
+ "v32@0:8@\"NSString\"16@?<v@?@\"EMMessageObjectID\"@\"NSError\">24"
+ "v32@0:8q16@?<v@?@\"NSURL\"@\"NSError\">24"
+ "v56@0:8@16Q24@32@40@48"
+ "wantsBlockedSenderManager"
- "AddCommerceMailboxToFavorites"
- "InstantAnswers"
- "OneTimeCodes"
- "RemindMeEverywhere"
- "Shoji"
- "SnippetHighlighting"
- "T@\"NSSet\",&,N,V_blockedSenders"
- "_commonInitWithStore:options:emailAddressCache:"
- "gatherIndexingDiagnosticsWithCompletionHandler:"
- "updatedFlightURLForInstantAnswer:"
- "v24@0:8@?<v@?@\"NSURL\"@\"NSError\">16"
- "v40@0:8@16Q24@32"

```
