## CoreSpotlight

> `/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight`

```diff

-2333.50.1.0.0
-  __TEXT.__text: 0xc9708
-  __TEXT.__auth_stubs: 0x1bd0
-  __TEXT.__objc_methlist: 0xc590
-  __TEXT.__const: 0xc22
-  __TEXT.__gcc_except_tab: 0x2e94
-  __TEXT.__cstring: 0x11eb2
-  __TEXT.__oslogstring: 0x6d15
+2374.0.1.0.0
+  __TEXT.__text: 0xcee6c
+  __TEXT.__auth_stubs: 0x1bf0
+  __TEXT.__objc_methlist: 0xc990
+  __TEXT.__const: 0xc5a
+  __TEXT.__gcc_except_tab: 0x2f00
+  __TEXT.__cstring: 0x12aa2
+  __TEXT.__oslogstring: 0x7e01
   __TEXT.__ustring: 0x3c
   __TEXT.__dlopen_cstrs: 0x3f1
   __TEXT.__swift5_typeref: 0x2a0

   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x31e0
-  __TEXT.__eh_frame: 0x210
-  __TEXT.__objc_classname: 0xf9f
-  __TEXT.__objc_methname: 0x1cd40
-  __TEXT.__objc_methtype: 0x21b8
-  __TEXT.__objc_stubs: 0xf920
-  __DATA_CONST.__got: 0x780
-  __DATA_CONST.__const: 0x4cd0
+  __TEXT.__unwind_info: 0x3300
+  __TEXT.__eh_frame: 0x1e8
+  __TEXT.__objc_classname: 0xfb9
+  __TEXT.__objc_methname: 0x1d800
+  __TEXT.__objc_methtype: 0x21c2
+  __TEXT.__objc_stubs: 0xfbc0
+  __DATA_CONST.__got: 0x790
+  __DATA_CONST.__const: 0x4f88
   __DATA_CONST.__objc_classlist: 0x448
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x74a8
+  __DATA_CONST.__objc_selrefs: 0x7798
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x330
-  __DATA_CONST.__objc_arraydata: 0xd20
-  __AUTH_CONST.__auth_got: 0xdf8
+  __DATA_CONST.__objc_arraydata: 0xd48
+  __AUTH_CONST.__auth_got: 0xe08
   __AUTH_CONST.__const: 0x1768
-  __AUTH_CONST.__cfstring: 0x119a0
-  __AUTH_CONST.__objc_const: 0x121c0
-  __AUTH_CONST.__objc_arrayobj: 0xa20
-  __AUTH_CONST.__objc_intobj: 0x750
+  __AUTH_CONST.__cfstring: 0x12600
+  __AUTH_CONST.__objc_const: 0x125a0
+  __AUTH_CONST.__objc_arrayobj: 0xa50
+  __AUTH_CONST.__objc_intobj: 0x798
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__objc_doubleobj: 0x90
-  __AUTH.__objc_data: 0x1310
+  __AUTH_CONST.__objc_doubleobj: 0xa0
+  __AUTH.__objc_data: 0x1ab8
   __AUTH.__data: 0x3a0
-  __DATA.__objc_ivar: 0xb50
-  __DATA.__data: 0xa90
-  __DATA.__bss: 0x1230
-  __DATA_DIRTY.__objc_data: 0x17c0
-  __DATA_DIRTY.__data: 0x1c
-  __DATA_DIRTY.__bss: 0x7558
+  __DATA.__objc_ivar: 0xb74
+  __DATA.__data: 0xa48
+  __DATA.__bss: 0x11c0
+  __DATA_DIRTY.__objc_data: 0x1018
+  __DATA_DIRTY.__data: 0x18
+  __DATA_DIRTY.__bss: 0x7eb0
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: E6D9E817-5620-37A7-93BF-1F12A8A72F47
-  Functions: 5315
-  Symbols:   16971
-  CStrings:  11680
+  UUID: 6A35F957-5774-3C95-BCEB-F8D2E0395F93
+  Functions: 5441
+  Symbols:   17318
+  CStrings:  12061
 
Symbols:
+ +[CSAttributedQuery _getNSDateComponentsFromDictionary:]
+ +[CSUserQuery queryParserResourcesInfo]
+ +[CSUserQuery skipTextSemanticSearchForSearchString:queryContext:skipReason:]
+ -[CSAddressTag .cxx_destruct]
+ -[CSAddressTag initWithAddress:synonyms:type:lat:lng:confidence:]
+ -[CSAddressTag lat]
+ -[CSAddressTag lng]
+ -[CSAddressTag type]
+ -[CSQueryRankingConfiguration .cxx_destruct]
+ -[CSQueryRankingConfiguration additionalFetchAttributes]
+ -[CSQueryRankingConfiguration bundleIDs]
+ -[CSQueryRankingConfiguration enableExtendedEmbeddingTimeout]
+ -[CSQueryRankingConfiguration enablePommesRanking]
+ -[CSQueryRankingConfiguration enablePommesSuggestions]
+ -[CSQueryRankingConfiguration enableSemanticSearch]
+ -[CSQueryRankingConfiguration enableSuggestions]
+ -[CSQueryRankingConfiguration enableUniversalSuggestions]
+ -[CSQueryRankingConfiguration initWithQueryContext:options:]
+ -[CSQueryRankingConfiguration initWithQueryContext:options:].cold.1
+ -[CSQueryRankingConfiguration isCJK]
+ -[CSQueryRankingConfiguration isColdStart]
+ -[CSQueryRankingConfiguration isMail]
+ -[CSQueryRankingConfiguration isMessages]
+ -[CSQueryRankingConfiguration isNotes]
+ -[CSQueryRankingConfiguration isPhotos]
+ -[CSQueryRankingConfiguration isPommesCtl]
+ -[CSQueryRankingConfiguration isPommesZKW]
+ -[CSQueryRankingConfiguration isSafari]
+ -[CSQueryRankingConfiguration isSearch]
+ -[CSQueryRankingConfiguration isSettings]
+ -[CSQueryRankingConfiguration isShortcutsSearch]
+ -[CSQueryRankingConfiguration isSpotlight]
+ -[CSQueryRankingConfiguration isWallet]
+ -[CSQueryRankingConfiguration maxSuggestionCount]
+ -[CSQueryRankingConfiguration nlpContextID]
+ -[CSQueryRankingConfiguration parseOptions]
+ -[CSQueryRankingConfiguration suggestionRankingWeights]
+ -[CSSearchQueryContext isWallet]
+ -[CSSearchableIndex _validateOperationWithItems:identifiers:].cold.7
+ -[CSSearchableItem needsTimeSensitive]
+ -[CSSearchableItemAttributeSet(CSAttributes) counterpartBundleID]
+ -[CSSearchableItemAttributeSet(CSAttributes) groupID]
+ -[CSSearchableItemAttributeSet(CSAttributes) remotePlaceholderBundleID]
+ -[CSSearchableItemAttributeSet(CSAttributes) setCounterpartBundleID:]
+ -[CSSearchableItemAttributeSet(CSAttributes) setGroupID:]
+ -[CSSearchableItemAttributeSet(CSAttributes) setRemotePlaceholderBundleID:]
+ -[CSSearchableItemAttributeSet(CSEmbeddingVector) photoEmbeddingVectorIds]
+ -[CSSearchableItemAttributeSet(CSEmbeddingVector) primaryTextEmbeddingVectorIds]
+ -[CSSearchableItemAttributeSet(CSEmbeddingVector) secondaryTextEmbeddingVectorIds]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventCarrierName]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventCustomerAddresses]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventCustomerTelephoneNumbers]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventEndLocationAddressCountry]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventEndLocationAddressLatitude]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventEndLocationAddressLocality]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventEndLocationAddressLongitude]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventEndLocationAddressRegion]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventEndPersonNames]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventEstimatedEndDateTimeZone]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventEstimatedEndDate]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventEstimatedStartDateTimeZone]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventEstimatedStartDate]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventOrderDateTimeZone]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventOrderDate]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventStartLocationAddressCountry]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventStartLocationAddressLatitude]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventStartLocationAddressLocality]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventStartLocationAddressLongitude]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventStartLocationAddressRegion]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventStartPersonNames]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) eventTrackingNumber]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) preExtractionIsPartial]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventCarrierName:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventCustomerAddresses:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventCustomerTelephoneNumbers:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventEndLocationAddressCountry:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventEndLocationAddressLatitude:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventEndLocationAddressLocality:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventEndLocationAddressLongitude:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventEndLocationAddressRegion:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventEndPersonNames:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventEstimatedEndDate:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventEstimatedEndDateTimeZone:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventEstimatedStartDate:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventEstimatedStartDateTimeZone:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventOrderDate:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventOrderDateTimeZone:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventStartLocationAddressCountry:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventStartLocationAddressLatitude:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventStartLocationAddressLocality:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventStartLocationAddressLongitude:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventStartLocationAddressRegion:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventStartPersonNames:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setEventTrackingNumber:]
+ -[CSSearchableItemAttributeSet(CSEvent_Generic) setPreExtractionIsPartial:]
+ -[CSSearchableItemAttributeSet(CSInterfaces) isWindowTabEntity]
+ -[CSSearchableItemAttributeSet(CSInterfaces) setIsWindowTabEntity:]
+ -[CSSearchableItemAttributeSet(CSMail_Private) isTimeSensitive]
+ -[CSSearchableItemAttributeSet(CSMail_Private) setIsTimeSensitive:]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) eventRelatedMessageIdentifiers]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) eventRelatedSourceBundleIdentifiers]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) setEventRelatedMessageIdentifiers:]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) setEventRelatedSourceBundleIdentifiers:]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) setShortcutsToolInvocation:]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) setShortcutsToolInvocationSummary:]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) setTimeSensitiveStatus:]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) shortcutsToolInvocationSummary]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) shortcutsToolInvocation]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) timeSensitiveStatus]
+ -[CSSearchableItemAttributeSet(CSQuery) matchingHints]
+ -[CSSearchableItemAttributeSet(CSQuery) retrievalType]
+ -[CSSearchableItemAttributeSet(CSQuery) setMatchingHints:]
+ -[CSSuggestionsRanker initWithQueryRankingConfiguration:]
+ -[CSSuggestionsRanker queryRankingConfiguration]
+ -[CSUserQueryParser _CSUserQueryQPResourcesInfo]
+ -[NSDateComponents(local) isUninitialized]
+ GCC_except_table1003
+ GCC_except_table131
+ GCC_except_table146
+ GCC_except_table22
+ GCC_except_table290
+ GCC_except_table303
+ GCC_except_table316
+ GCC_except_table326
+ GCC_except_table329
+ GCC_except_table332
+ GCC_except_table334
+ GCC_except_table339
+ GCC_except_table342
+ GCC_except_table344
+ GCC_except_table419
+ GCC_except_table426
+ GCC_except_table437
+ GCC_except_table463
+ GCC_except_table511
+ GCC_except_table691
+ GCC_except_table84
+ _CSCardSubTypeBusinessCard
+ _CSCardSubTypeDriverLicense
+ _CSCardSubTypeEmployeeCard
+ _CSCardSubTypeGreenCard
+ _CSCardSubTypeInsuranceCard
+ _CSCardSubTypeMedicalCard
+ _CSCardSubTypeMembershipCard
+ _CSCardSubTypePassport
+ _CSCardSubTypeSSN
+ _CSCardSubTypeStateID
+ _CSCardSubTypeStudentCard
+ _CSCardSubTypeTransitCard
+ _CSEventStatusCancelled
+ _CSEventStatusConfirmed
+ _CSEventStatusDelivered
+ _CSEventStatusIssue
+ _CSEventStatusIssueUnknown
+ _CSEventStatusModified
+ _CSEventStatusOnTheWay
+ _CSEventStatusOutForDelivery
+ _CSEventStatusShipped
+ _CSEventStatusUnknown
+ _CSEventSubTypeCarrier
+ _CSEventSubTypeMerchant
+ _CSEventTypeOrder
+ _MDItemAppEntitySubtitle
+ _MDItemCounterpartBundleID
+ _MDItemDerivedIsFromMe
+ _MDItemDerivedIsFromMeRanking
+ _MDItemDerivedIsMeRanking
+ _MDItemDerivedIsMeRankingOCR
+ _MDItemDerivedIsMeRankingOCRTextContentMatch
+ _MDItemDerivedIsMeRankingPreExtraction
+ _MDItemDerivedIsMeRankingSpan
+ _MDItemDerivedIsMeRankingTextContentMatch
+ _MDItemDerivedIsMeRankingToken
+ _MDItemEventCarrierName
+ _MDItemEventCustomerAddresses
+ _MDItemEventCustomerTelephoneNumbers
+ _MDItemEventEndLocationAddressCountry
+ _MDItemEventEndLocationAddressLatitude
+ _MDItemEventEndLocationAddressLocality
+ _MDItemEventEndLocationAddressLongitude
+ _MDItemEventEndLocationAddressRegion
+ _MDItemEventEndPersonNames
+ _MDItemEventEstimatedEndDate
+ _MDItemEventEstimatedEndDateTimeZone
+ _MDItemEventEstimatedStartDate
+ _MDItemEventEstimatedStartDateTimeZone
+ _MDItemEventOrderDate
+ _MDItemEventOrderDateTimeZone
+ _MDItemEventRelatedMessageIdentifiers
+ _MDItemEventRelatedSourceBundleIdentifiers
+ _MDItemEventStartLocationAddressCountry
+ _MDItemEventStartLocationAddressLatitude
+ _MDItemEventStartLocationAddressLocality
+ _MDItemEventStartLocationAddressLongitude
+ _MDItemEventStartLocationAddressRegion
+ _MDItemEventStartPersonNames
+ _MDItemEventTrackingNumber
+ _MDItemIsScreenCapture
+ _MDItemIsTimeSensitive
+ _MDItemIsWindowTabEntity
+ _MDItemPhotoEmbeddingVectorIds
+ _MDItemPreExtractionIsPartial
+ _MDItemPrimaryTextEmbeddingVectorIds
+ _MDItemRemotePlaceholderBundleID
+ _MDItemSecondaryTextEmbeddingVectorIds
+ _MDItemShortcutsToolInvocation
+ _MDItemShortcutsToolInvocationSummary
+ _MDItemShortcutsToolType
+ _MDItemTimeSensitiveStatus
+ _MDItemWindowProcessIdentifier
+ _MDItemWindowProcessIdentifierVersion
+ _MDMessageLpDescription
+ _MDMessageLpTitle
+ _MDQueryResultEmbeddingVectorIds
+ _MDSearchableWebsiteSourcePageURL
+ _MDSearchableWebsiteTopDomain
+ _MDToolInvocationData
+ _MDToolInvocationSummaryData
+ _OBJC_CLASS_$_CSQueryRankingConfiguration
+ _OBJC_IVAR_$_CSAddressTag._lat
+ _OBJC_IVAR_$_CSAddressTag._lng
+ _OBJC_IVAR_$_CSAddressTag._type
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._additionalFetchAttributes
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._bundleIDs
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._enableExtendedEmbeddingTimeout
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._enablePommesRanking
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._enablePommesSuggestions
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._enableSemanticSearch
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._enableSuggestions
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._enableUniversalSuggestions
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._isCJK
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._isColdStart
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._isMail
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._isMessages
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._isNotes
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._isPhotos
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._isPommesCtl
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._isPommesZKW
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._isSafari
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._isSearch
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._isSettings
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._isShortcutsSearch
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._isSpotlight
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._isWallet
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._maxSuggestionCount
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._nlpContextID
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._parseOptions
+ _OBJC_IVAR_$_CSQueryRankingConfiguration._suggestionRankingWeights
+ _OBJC_IVAR_$_CSSuggestionsRanker._queryRankingConfiguration
+ _OBJC_METACLASS_$_CSQueryRankingConfiguration
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ __OBJC_$_INSTANCE_METHODS_CSQueryRankingConfiguration
+ __OBJC_$_INSTANCE_METHODS_CSSearchableItemAttributeSet(CSAttributes|CSQuery|CSPrivateAttributes|CSMediaAnalysis_Private|CSWallet_Private|CSMail_Private|CSSafari_Private|CSFileProvider_Private|CSInteraction_private|CSAppDemotion_Private|CSNews_Private|CSPortrait_Private|CSPhone_Private|CSPhotos_Private|CSMotion|CSMessages_Private|CSNotifications_Private|CSAddressBook_Private|Containment|EventsExtras|CSCustomAttributes|CSCoderAdditions|CSInstantAnswer|CSDonatedEvent|CSEvent_Flight|CSEvent_Hotel|SwiftUI_Archiving|CSEvent_Restaurant|CSEvent_Generic|CSCard|CSContact|AppEntity|CSEmbeddingVector|AllEventTypes|CSInterfaces)
+ __OBJC_$_INSTANCE_VARIABLES_CSAddressTag
+ __OBJC_$_INSTANCE_VARIABLES_CSQueryRankingConfiguration
+ __OBJC_$_PROP_LIST_CSAddressTag
+ __OBJC_$_PROP_LIST_CSQueryRankingConfiguration
+ __OBJC_CLASS_RO_$_CSQueryRankingConfiguration
+ __OBJC_METACLASS_RO_$_CSQueryRankingConfiguration
+ ___21-[CSSearchQuery poll]_block_invoke.1033
+ ___34-[CSSearchConnection cancelQuery:]_block_invoke.1378
+ ___34-[CSSearchConnection cancelQuery:]_block_invoke.1378.cold.1
+ ___36-[CSSearchQuery processResultItems:]_block_invoke.1089
+ ___54-[CSSearchQuery copyResultsFromPlist:protectionClass:]_block_invoke.1061
+ ___56+[CSAttributedQuery _getNSDateComponentsFromDictionary:]_block_invoke
+ ___60-[CSQueryRankingConfiguration initWithQueryContext:options:]_block_invoke
+ ___64-[CSUserQuery queryStringWithQueryContext:searchString:options:]_block_invoke.678
+ ___67-[CSSearchableItem(Internal) _standardizeExtractedNumericEntities:]_block_invoke.295
+ ___67-[CSSearchableItem(Internal) _standardizeExtractedNumericEntities:]_block_invoke.313
+ ___80-[CSSearchQuery filterMegadomePeopleSuggestions:isShortQuery:completionHandler:]_block_invoke.1065
+ ___94-[CSUserQuery filterContactPeopleSuggestions:cachedSuggestionsEmailToScope:completionHandler:]_block_invoke.726
+ ___MDQueryParserCopyResourcesInfo
+ ___block_descriptor_40_e8_32r_e35_v32?0"NSString"8"NSNumber"16^B24lr32l8
+ ___block_descriptor_64_e8_32s40r48r56r_e11_B20?0Q8B16ls32l8r40l8r48l8r56l8
+ ___block_descriptor_80_e8_32s40s48s_e59_"CSExternalAnalysisTag"40?0Q8"NSString"16"NSArray"24d32ls32l8s40l8s48l8
+ ___block_literal_global.1036
+ ___block_literal_global.1042
+ ___block_literal_global.1142
+ ___block_literal_global.1356
+ ___block_literal_global.1358
+ ___block_literal_global.1361
+ ___block_literal_global.1364
+ ___block_literal_global.1389
+ ___block_literal_global.1421
+ ___block_literal_global.1447
+ ___block_literal_global.1474
+ ___block_literal_global.1525
+ ___block_literal_global.1527
+ ___block_literal_global.1529
+ ___block_literal_global.1542
+ ___block_literal_global.1544
+ ___block_literal_global.1546
+ ___block_literal_global.1963
+ ___block_literal_global.230
+ ___block_literal_global.247
+ ___block_literal_global.249
+ ___block_literal_global.25
+ ___block_literal_global.251
+ ___block_literal_global.253
+ ___block_literal_global.288
+ ___block_literal_global.297
+ ___block_literal_global.327
+ ___block_literal_global.38
+ ___block_literal_global.440
+ ___block_literal_global.562
+ ___block_literal_global.591
+ ___block_literal_global.775
+ ___block_literal_global.838
+ ___block_literal_global.846
+ ___block_literal_global.978
+ ___isDebugVerboseMode_block_invoke
+ ___logForCSLogCategoryItems_block_invoke
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_CoreSpotlight
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_CoreSpotlight
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_CoreSpotlight
+ _initWithQueryContext:options:.gIsFeatureFlagsEnabled
+ _initWithQueryContext:options:.gIsMailSemanticSearchEnabled
+ _initWithQueryContext:options:.onceToken
+ _isDebugVerboseMode
+ _isDebugVerboseMode.cold.1
+ _isDebugVerboseMode.debugEnabled
+ _isDebugVerboseMode.onceToken
+ _logForCSLogCategoryItems
+ _logForCSLogCategoryItems.cold.1
+ _logForCSLogCategoryItems.onceToken
+ _logForCSLogCategoryItems.sQueryLog
+ _objc_msgSend$_CSUserQueryQPResourcesInfo
+ _objc_msgSend$_getNSDateComponentsFromDictionary:
+ _objc_msgSend$additionalFetchAttributes
+ _objc_msgSend$attribute:atIndex:effectiveRange:
+ _objc_msgSend$era
+ _objc_msgSend$initWithAddress:synonyms:type:lat:lng:confidence:
+ _objc_msgSend$initWithQueryContext:options:
+ _objc_msgSend$initWithQueryRankingConfiguration:
+ _objc_msgSend$isColdStart
+ _objc_msgSend$isMessages
+ _objc_msgSend$isUninitialized
+ _objc_msgSend$isWallet
+ _objc_msgSend$lat
+ _objc_msgSend$lng
+ _objc_msgSend$numberWithLong:
+ _objc_msgSend$parseOptions
+ _objc_msgSend$queryRankingConfiguration
+ _objc_msgSend$setWeekOfMonth:
+ _objc_msgSend$setWeekOfYear:
+ _objc_msgSend$setWeekday:
+ _objc_msgSend$setWeekdayOrdinal:
+ _objc_msgSend$setYearForWeekOfYear:
+ _objc_msgSend$skipTextSemanticSearchForSearchString:queryContext:skipReason:
+ _objc_msgSend$timeZone
+ _objc_msgSend$timeZoneWithAbbreviation:
+ _objc_msgSend$weekOfMonth
+ _objc_msgSend$weekOfYear
+ _objc_msgSend$weekday
+ _objc_msgSend$weekdayOrdinal
+ _objc_msgSend$yearForWeekOfYear
+ _os_signpost_id_generate
+ _queryStringWithQueryContext:searchString:options:.onceAttributesToken.677
+ _updateDenseCandidatesAndReturnItemToBeSentToClientNow.cold.1
+ _updateDenseCandidatesAndReturnItemToBeSentToClientNow.cold.2
+ _updateDenseCandidatesAndReturnItemToBeSentToClientNow.cold.3
+ _updateTopHitCandidatesAndReturnItemToBeSentToClientNow.cold.10
+ _updateTopHitCandidatesAndReturnItemToBeSentToClientNow.cold.11
+ _updateTopHitCandidatesAndReturnItemToBeSentToClientNow.cold.12
+ _updateTopHitCandidatesAndReturnItemToBeSentToClientNow.cold.13
+ _updateTopHitCandidatesAndReturnItemToBeSentToClientNow.cold.14
+ _updateTopHitCandidatesAndReturnItemToBeSentToClientNow.cold.15
+ _updateTopHitCandidatesAndReturnItemToBeSentToClientNow.cold.2
+ _updateTopHitCandidatesAndReturnItemToBeSentToClientNow.cold.3
+ _updateTopHitCandidatesAndReturnItemToBeSentToClientNow.cold.4
+ _updateTopHitCandidatesAndReturnItemToBeSentToClientNow.cold.5
+ _updateTopHitCandidatesAndReturnItemToBeSentToClientNow.cold.6
+ _updateTopHitCandidatesAndReturnItemToBeSentToClientNow.cold.7
+ _updateTopHitCandidatesAndReturnItemToBeSentToClientNow.cold.8
+ _updateTopHitCandidatesAndReturnItemToBeSentToClientNow.cold.9
- +[CSUserQuery flattenCSFieldSpecifications:]
- +[CSUserQuery skipTextSemanticSearchForSearchString:tokenCount:queryContext:skipReason:]
- -[CSAddressTag initWithAddress:synonyms:confidence:]
- -[CSRankingConfiguration .cxx_destruct]
- -[CSRankingConfiguration bundleIDs]
- -[CSRankingConfiguration enableExtendedEmbeddingTimeout]
- -[CSRankingConfiguration enablePommesRanking]
- -[CSRankingConfiguration enablePommesSuggestions]
- -[CSRankingConfiguration enableSemanticSearch]
- -[CSRankingConfiguration enableSuggestions]
- -[CSRankingConfiguration enableUniversalSuggestions]
- -[CSRankingConfiguration initWithQueryContext:]
- -[CSRankingConfiguration initWithQueryContext:].cold.1
- -[CSRankingConfiguration isCJK]
- -[CSRankingConfiguration isMail]
- -[CSRankingConfiguration isNotes]
- -[CSRankingConfiguration isPhotos]
- -[CSRankingConfiguration isPommesCtl]
- -[CSRankingConfiguration isPommesZKW]
- -[CSRankingConfiguration isSafari]
- -[CSRankingConfiguration isSearch]
- -[CSRankingConfiguration isSettings]
- -[CSRankingConfiguration isSpotlight]
- -[CSRankingConfiguration maxSuggestionCount]
- -[CSRankingConfiguration nlpContextID]
- -[CSRankingConfiguration suggestionRankingWeights]
- -[CSSearchableItemAttributeSet(CSQueryResultMatchingHint) matchingHints]
- -[CSSearchableItemAttributeSet(CSQueryResultMatchingHint) setMatchingHints:]
- -[CSSuggestionsRanker initWithRankingConfiguration:]
- -[CSSuggestionsRanker rankingConfiguration]
- GCC_except_table114
- GCC_except_table289
- GCC_except_table302
- GCC_except_table310
- GCC_except_table315
- GCC_except_table324
- GCC_except_table328
- GCC_except_table331
- GCC_except_table333
- GCC_except_table337
- GCC_except_table341
- GCC_except_table343
- GCC_except_table415
- GCC_except_table425
- GCC_except_table436
- GCC_except_table462
- GCC_except_table510
- GCC_except_table65
- GCC_except_table678
- GCC_except_table83
- GCC_except_table984
- _OBJC_CLASS_$_CSRankingConfiguration
- _OBJC_IVAR_$_CSRankingConfiguration._bundleIDs
- _OBJC_IVAR_$_CSRankingConfiguration._enableExtendedEmbeddingTimeout
- _OBJC_IVAR_$_CSRankingConfiguration._enablePommesRanking
- _OBJC_IVAR_$_CSRankingConfiguration._enablePommesSuggestions
- _OBJC_IVAR_$_CSRankingConfiguration._enableSemanticSearch
- _OBJC_IVAR_$_CSRankingConfiguration._enableSuggestions
- _OBJC_IVAR_$_CSRankingConfiguration._enableUniversalSuggestions
- _OBJC_IVAR_$_CSRankingConfiguration._isCJK
- _OBJC_IVAR_$_CSRankingConfiguration._isMail
- _OBJC_IVAR_$_CSRankingConfiguration._isNotes
- _OBJC_IVAR_$_CSRankingConfiguration._isPhotos
- _OBJC_IVAR_$_CSRankingConfiguration._isPommesCtl
- _OBJC_IVAR_$_CSRankingConfiguration._isPommesZKW
- _OBJC_IVAR_$_CSRankingConfiguration._isSafari
- _OBJC_IVAR_$_CSRankingConfiguration._isSearch
- _OBJC_IVAR_$_CSRankingConfiguration._isSettings
- _OBJC_IVAR_$_CSRankingConfiguration._isSpotlight
- _OBJC_IVAR_$_CSRankingConfiguration._maxSuggestionCount
- _OBJC_IVAR_$_CSRankingConfiguration._nlpContextID
- _OBJC_IVAR_$_CSRankingConfiguration._suggestionRankingWeights
- _OBJC_IVAR_$_CSSuggestionsRanker._rankingConfiguration
- _OBJC_METACLASS_$_CSRankingConfiguration
- __OBJC_$_INSTANCE_METHODS_CSRankingConfiguration
- __OBJC_$_INSTANCE_METHODS_CSSearchableItemAttributeSet(CSAttributes|CSQueryResultMatchingHint|CSPrivateAttributes|CSMediaAnalysis_Private|CSWallet_Private|CSMail_Private|CSSafari_Private|CSFileProvider_Private|CSInteraction_private|CSAppDemotion_Private|CSNews_Private|CSPortrait_Private|CSPhone_Private|CSPhotos_Private|CSMotion|CSMessages_Private|CSNotifications_Private|CSAddressBook_Private|Containment|EventsExtras|CSCustomAttributes|CSCoderAdditions|CSInstantAnswer|CSDonatedEvent|CSEvent_Flight|CSEvent_Hotel|SwiftUI_Archiving|CSEvent_Restaurant|CSEvent_Generic|CSCard|CSContact|AppEntity|CSEmbeddingVector|AllEventTypes)
- __OBJC_$_INSTANCE_VARIABLES_CSRankingConfiguration
- __OBJC_$_PROP_LIST_CSRankingConfiguration
- __OBJC_CLASS_RO_$_CSRankingConfiguration
- __OBJC_METACLASS_RO_$_CSRankingConfiguration
- ___21-[CSSearchQuery poll]_block_invoke.1029
- ___34-[CSSearchConnection cancelQuery:]_block_invoke.1374
- ___34-[CSSearchConnection cancelQuery:]_block_invoke.1374.cold.1
- ___36-[CSSearchQuery processResultItems:]_block_invoke.1085
- ___47-[CSRankingConfiguration initWithQueryContext:]_block_invoke
- ___54-[CSSearchQuery copyResultsFromPlist:protectionClass:]_block_invoke.1057
- ___64-[CSUserQuery queryStringWithQueryContext:searchString:options:]_block_invoke.720
- ___67-[CSSearchableItem(Internal) _standardizeExtractedNumericEntities:]_block_invoke.283
- ___67-[CSSearchableItem(Internal) _standardizeExtractedNumericEntities:]_block_invoke.301
- ___80-[CSSearchQuery filterMegadomePeopleSuggestions:isShortQuery:completionHandler:]_block_invoke.1061
- ___94-[CSUserQuery filterContactPeopleSuggestions:cachedSuggestionsEmailToScope:completionHandler:]_block_invoke.770
- ___block_descriptor_64_e8_32s40s48s56s_e41_v40?0"NSDictionary"8{_NSRange=QQ}16^B32ls32l8s40l8s48l8s56l8
- ___block_literal_global.1032
- ___block_literal_global.1038
- ___block_literal_global.1133
- ___block_literal_global.1350
- ___block_literal_global.1352
- ___block_literal_global.1357
- ___block_literal_global.1360
- ___block_literal_global.1380
- ___block_literal_global.1412
- ___block_literal_global.1438
- ___block_literal_global.1470
- ___block_literal_global.1496
- ___block_literal_global.1498
- ___block_literal_global.1500
- ___block_literal_global.1502
- ___block_literal_global.1504
- ___block_literal_global.1506
- ___block_literal_global.1508
- ___block_literal_global.1924
- ___block_literal_global.233
- ___block_literal_global.235
- ___block_literal_global.237
- ___block_literal_global.239
- ___block_literal_global.241
- ___block_literal_global.276
- ___block_literal_global.303
- ___block_literal_global.31
- ___block_literal_global.482
- ___block_literal_global.604
- ___block_literal_global.633
- ___block_literal_global.722
- ___block_literal_global.766
- ___block_literal_global.810
- ___block_literal_global.832
- ___block_literal_global.970
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_CoreSpotlight
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_CoreSpotlight
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_CoreSpotlight
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_CoreSpotlight
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_CoreSpotlight
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_CoreSpotlight
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_CoreSpotlight
- _initWithQueryContext:.gIsFeatureFlagsEnabled
- _initWithQueryContext:.gIsMailSemanticSearchEnabled
- _initWithQueryContext:.onceToken
- _objc_msgSend$containsCJK
- _objc_msgSend$enableExtendedEmbeddingTimeout
- _objc_msgSend$enableSemanticSearch
- _objc_msgSend$flattenCSFieldSpecifications:
- _objc_msgSend$initWithAddress:synonyms:confidence:
- _objc_msgSend$initWithQueryContext:
- _objc_msgSend$initWithRankingConfiguration:
- _objc_msgSend$rankingConfiguration
- _objc_msgSend$skipTextSemanticSearchForSearchString:tokenCount:queryContext:skipReason:
- _queryStringWithQueryContext:searchString:options:.onceAttributesToken.719
- _swift_bridgeObjectRetain
CStrings:
+ "@\"CSQueryRankingConfiguration\""
+ "@64@0:8@16@24@32@40@48d56"
+ "CATEGORY"
+ "CSInterfaces"
+ "CSQuery"
+ "CSQueryRankingConfiguration"
+ "Could not archive queryUnderstandingOutput %@"
+ "Could not unarchive queryUnderstandingOutput %@"
+ "DebugVerboseModeQuery"
+ "Disabling"
+ "E"
+ "Enabling"
+ "F"
+ "H"
+ "InvalidValue"
+ "T@\"CSQueryRankingConfiguration\",R,N,V_queryRankingConfiguration"
+ "T@\"NSArray\",R,C"
+ "T@\"NSArray\",R,N,V_additionalFetchAttributes"
+ "T@\"NSData\",&,N"
+ "T@\"NSDictionary\",R,N,V_parseOptions"
+ "T@\"NSNumber\",R,N,V_lat"
+ "T@\"NSNumber\",R,N,V_lng"
+ "T@\"NSNumber\",R,N,V_type"
+ "TB,R,N,V_isColdStart"
+ "TB,R,N,V_isMessages"
+ "TB,R,N,V_isShortcutsSearch"
+ "TB,R,N,V_isWallet"
+ "UTI"
+ "W"
+ "Y"
+ "[qid=%ld] ### cancel error %@"
+ "[qid=%ld] ### error %@/%ld reply:%@"
+ "[qid=%ld] %@"
+ "[qid=%ld] %lu. Final Photos item identifier (%@), L1Score=%f, L2Score=%f"
+ "[qid=%ld] Canceling"
+ "[qid=%ld] Dropping results"
+ "[qid=%ld] Finished"
+ "[qid=%ld] Finished (cancelled)"
+ "[qid=%ld] Finished with error error:%@/%ld"
+ "[qid=%ld] Found: %ld instant answers"
+ "[qid=%ld] Found: %ld items"
+ "[qid=%ld] Found: %ld suggestions"
+ "[qid=%ld] Gather ended"
+ "[qid=%ld] Got completions %@"
+ "[qid=%ld] Handle batches %@ for query:%@"
+ "[qid=%ld] Handle completion batches %@ for query:%@"
+ "[qid=%ld] Handle instant answer batches %@ for query:%@"
+ "[qid=%ld] Handle suggestion batches %@ for query:%@"
+ "[qid=%ld] Opcode 0x%x not handled"
+ "[qid=%ld] Plists count %ld "
+ "[qid=%ld] Polling"
+ "[qid=%ld] Priority Gather ended"
+ "[qid=%ld] Received batch %@ for query:%@"
+ "[qid=%ld] Received completion %@ for query:%@"
+ "[qid=%ld] RemoveResults tag:0x%x opcode :0x%x"
+ "[qid=%ld] Removed: %ld items"
+ "[qid=%ld] Resolved attribute names: %@"
+ "[qid=%ld] Result oidData: %p"
+ "[qid=%ld] Results type: %d "
+ "[qid=%ld] Starting %@"
+ "[qid=%ld] Unknown type :%d"
+ "[qid=%ld] Updated: %ld items"
+ "[qid=%ld] [ContactSearch] Processed contacts: %lu, Author contacts: %lu"
+ "[qid=%ld] [ContactSearch] Processed contacts: %lu, Recipient contacts: %lu, Total trimmed contacts: %lu"
+ "[qid=%ld] [ContactSearch] suggestions.count %lu != results.count %lu"
+ "[qid=%ld] is a live query; also disabling blocking on index."
+ "[qid=%ld] moved: %ld items"
+ "[qid=%ld] wait for suggestion count"
+ "[qid=%ld][CSSearchQuery] QOS_topHitQueryParameters: %d"
+ "[qid=%ld][CSTopHitRanking] (queue: classic, stage: add, status: empty, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: classic, stage: add, status: free, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: classic, stage: add, status: full, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: classic, stage: remove, status: full, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: classic, stage: skip, status: full, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: dense(early), stage: add, status: empty, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: dense(early), stage: add, status: free, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: dense(early), stage: add, status: full, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: dense(early), stage: remove, status: full, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: dense(early), stage: skip, status: full, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: dense(early), stage: skip, status: non-dense, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: dense, stage: add, status: empty, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: dense, stage: add, status: free, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: dense, stage: add, status: full, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: dense, stage: remove, status: full, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: dense, stage: skip, status: full, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: hybrid, stage: add, status: empty, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: hybrid, stage: add, status: free, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: hybrid, stage: add, status: full, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: hybrid, stage: remove, status: full, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: hybrid, stage: skip, status: full, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: sparse, stage: add, status: empty, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: sparse, stage: add, status: free, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: sparse, stage: add, status: full, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: sparse, stage: remove, status: full, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] (queue: sparse, stage: skip, status: full, item: %@, pommesL1Score: %@, embeddingDistances: %@)"
+ "[qid=%ld][CSTopHitRanking] Finishing - clientBundleID=%@ hitCount=%ld, maxCount=%ld"
+ "[qid=%ld][CSTopHitRanking] Missing bundleID for item with ID: %@"
+ "[qid=%ld][CSTopHitRanking] Processing - clientBundleID=%@ maxDenseCount=%ld, maxCount=%ld, itemsCount=%lu"
+ "[qid=%ld][CSTopHitRanking] Stop \"finishing\" because query has been cancelled"
+ "[qid=%ld][CSTopHitRanking] Stop \"processing\" batch because query has been cancelled"
+ "[qid=%ld][CSTopHitRanking] clientBundleID=%@ hitCount=%ld (%lu), maxCount=%ld (%ld)"
+ "[qid=%ld][CSTopHitRanking] finishing - combining %lu topHitResults with %lu initial candidates to return a batch of %lu items"
+ "[qid=%ld][CSTopHitRanking] finishing - sending %lu dense items to client now"
+ "[qid=%ld][CSTopHitRanking] processing - current batch has %lu items (%ld items are L1 topHit candidates, %ld items are L2 topHit candidates)"
+ "[qid=%ld][CSTopHitRanking] processing - sending %lu items (out of initial %ld) to client now"
+ "[qid=%ld][CSTopHitRanking] query (length=%lu, trimmed length=%lu) is too short (threshold=%lu) for topHit results"
+ "[qid=%ld][CSUserQuery] %@ semantic search, clientDisabled: %@, isFeatureFlagsEnabled: %@, isGMOptedIn: %@, isClientAllowed: %@"
+ "[qid=%ld][CSUserQuery] %s query is a live query; also disabling blocking on index here."
+ "[qid=%ld][CSUserQuery] WARN - forcing allowSemanticSearch=YES for tools"
+ "[qid=%ld][CSUserQuery] enabling pommes suggestions"
+ "[qid=%ld][CSUserQuery] generating query"
+ "[qid=%ld][CSUserQuery] returning %lu suggestions"
+ "[qid=%ld][CSUserQuery] updating query context"
+ "[qid=%ld][ContactSearch]  %lu available at query completion"
+ "[qid=%ld][ContactSearch] All contacts are already processed or have [FROM] scopes"
+ "[qid=%ld][ContactSearch] Autoscoping couldn't be computed for any contacts"
+ "[qid=%ld][ContactSearch] Timed out waiting for results at query completion"
+ "[qid=%ld][ContactSearch] Total contacts: %lu, Cached contacts: %lu, Fresh contacts: %lu"
+ "[qid=%ld][ContactSearch] Waiting for results at query completion"
+ "[qid=%ld][ContactSearch] none available at query completion"
+ "[qid=%ld][QoS=%u] Starting %@"
+ "[qid=%ld][QoS=%u] didReturnResults"
+ "[qid=%ld][QoS=%u] didReturnResults inside method async call. attribute:%b counting:%b live:%b"
+ "[qid=%ld][QoS=%u] gather ended"
+ "[qid=%ld][QoS=%u] handleReply"
+ "[qid=%ld][QoS=%u] sendMessageAsync response"
+ "[qid=%ld][TopHit Thresholding][num_tokens=%lu] Results beyond the top %lu results are filtered"
+ "[qid=%ld][TopHit Thresholding][num_tokens=%lu] Thresholding applied at item %lu:\nScores={L1Score=%.04f, L1ScoreRatio=%.04f, L2Score=%.04f, L2ScoreRatio=%.04f, L2ScoreDiff=%.04f}"
+ "_CSUserQueryQPResourcesInfo"
+ "_additionalFetchAttributes"
+ "_getNSDateComponentsFromDictionary:"
+ "_isColdStart"
+ "_isMessages"
+ "_isShortcutsSearch"
+ "_isWallet"
+ "_kMDItemDerivedIsFromMe"
+ "_kMDItemDerivedIsFromMeRanking"
+ "_kMDItemDerivedIsMeRanking"
+ "_kMDItemDerivedIsMeRankingOCR"
+ "_kMDItemDerivedIsMeRankingOCRTextContentMatch"
+ "_kMDItemDerivedIsMeRankingPreExtraction"
+ "_kMDItemDerivedIsMeRankingSpan"
+ "_kMDItemDerivedIsMeRankingTextContentMatch"
+ "_kMDItemDerivedIsMeRankingToken"
+ "_kMDItemIsWindowTabEntity"
+ "_kMDItemPhotoEmbeddingVectorIds"
+ "_kMDItemPrimaryTextEmbeddingVectorIds"
+ "_kMDItemSecondaryTextEmbeddingVectorIds"
+ "_kMDItemShortcutsToolInvocation"
+ "_kMDItemShortcutsToolInvocationSummary"
+ "_kMDItemTimeSensitiveStatus"
+ "_parseOptions"
+ "_queryRankingConfiguration"
+ "additionalFetchAttributes"
+ "attribute:atIndex:effectiveRange:"
+ "authorAddresses:%s"
+ "authorEmailAddresses:%s"
+ "authorNames:%s"
+ "business_card"
+ "carrier"
+ "com.apple.Passbook"
+ "com.apple.WorkflowKit.BackgroundShortcutRunner"
+ "com.apple.shortcuts.search"
+ "com_apple_mobilesms_lpDescription"
+ "com_apple_mobilesms_lpTitle"
+ "com_apple_shortcuts_spotlight_tool_type"
+ "com_apple_shortcuts_tool_invocation"
+ "com_apple_shortcuts_tool_invocation_summary"
+ "confirmed"
+ "counterpartBundleID"
+ "delivered"
+ "editors:%s"
+ "era"
+ "eventCarrierName"
+ "eventCustomerAddresses"
+ "eventCustomerTelephoneNumbers"
+ "eventEndLocationAddressCountry"
+ "eventEndLocationAddressLatitude"
+ "eventEndLocationAddressLocality"
+ "eventEndLocationAddressLongitude"
+ "eventEndLocationAddressRegion"
+ "eventEndPersonNames"
+ "eventEstimatedEndDate"
+ "eventEstimatedEndDateTimeZone"
+ "eventEstimatedStartDate"
+ "eventEstimatedStartDateTimeZone"
+ "eventOrderDate"
+ "eventOrderDateTimeZone"
+ "eventRelatedMessageIdentifiers"
+ "eventRelatedSourceBundleIdentifiers"
+ "eventStartLocationAddressCountry"
+ "eventStartLocationAddressLatitude"
+ "eventStartLocationAddressLocality"
+ "eventStartLocationAddressLongitude"
+ "eventStartLocationAddressRegion"
+ "eventStartPersonNames"
+ "eventTrackingNumber"
+ "groupID"
+ "id_driver_license"
+ "id_employee_card"
+ "id_green_card"
+ "id_medical_insurance"
+ "id_passport"
+ "id_ssn"
+ "id_state_id"
+ "id_student_card"
+ "initWithAddress:synonyms:type:lat:lng:confidence:"
+ "initWithQueryContext:options:"
+ "initWithQueryRankingConfiguration:"
+ "insurance_card"
+ "isColdStart"
+ "isShortcutsSearch"
+ "isTimeSensitive"
+ "isUninitialized"
+ "isWallet"
+ "isWindowTabEntity"
+ "issue_unknown"
+ "kMDItemAppEntitySubtitle"
+ "kMDItemCounterpartBundleID"
+ "kMDItemEventCarrierName"
+ "kMDItemEventCustomerAddresses"
+ "kMDItemEventCustomerTelephoneNumbers"
+ "kMDItemEventEndLocationAddressCountry"
+ "kMDItemEventEndLocationAddressLatitude"
+ "kMDItemEventEndLocationAddressLocality"
+ "kMDItemEventEndLocationAddressLongitude"
+ "kMDItemEventEndLocationAddressRegion"
+ "kMDItemEventEndPersonNames"
+ "kMDItemEventEstimatedEndDate"
+ "kMDItemEventEstimatedEndDateTimeZone"
+ "kMDItemEventEstimatedStartDate"
+ "kMDItemEventEstimatedStartDateTimeZone"
+ "kMDItemEventOrderDate"
+ "kMDItemEventOrderDateTimeZone"
+ "kMDItemEventRelatedMessageIdentifiers"
+ "kMDItemEventRelatedSourceBundleIdentifiers"
+ "kMDItemEventStartLocationAddressCountry"
+ "kMDItemEventStartLocationAddressLatitude"
+ "kMDItemEventStartLocationAddressLocality"
+ "kMDItemEventStartLocationAddressLongitude"
+ "kMDItemEventStartLocationAddressRegion"
+ "kMDItemEventStartPersonNames"
+ "kMDItemEventTrackingNumber"
+ "kMDItemExtractedAddressesLatitudes"
+ "kMDItemExtractedAddressesLongitudes"
+ "kMDItemExtractedAddressesTypes"
+ "kMDItemIsScreenCapture"
+ "kMDItemIsTimeSensitive"
+ "kMDItemPreExtractionIsPartial"
+ "kMDItemRemotePlaceholderBundleID"
+ "kMDQueryResultEmbeddingVectorIds"
+ "kQPDateComponents"
+ "kQPEndDateComponents"
+ "kQPStartDateComponents"
+ "m"
+ "membership_card"
+ "merchant"
+ "modified"
+ "needsTimeSensitive"
+ "numberWithLong:"
+ "on_the_way"
+ "out_for_delivery"
+ "parseOptions"
+ "participants:%s"
+ "photoEmbeddingVectorIds"
+ "preExtractionIsPartial"
+ "primaryTextEmbeddingVectorIds"
+ "queryParserResourcesInfo"
+ "queryRankingConfiguration"
+ "quickWebsiteSearchProviderSourcePageURLString"
+ "quickWebsiteSearchProviderTopDomain"
+ "recipientAddresses:%s"
+ "recipientEmailAddresses:%s"
+ "recipientNames:%s"
+ "remotePlaceholderBundleID"
+ "retrievalType"
+ "secondaryTextEmbeddingVectorIds"
+ "setCounterpartBundleID:"
+ "setEventCarrierName:"
+ "setEventCustomerAddresses:"
+ "setEventCustomerTelephoneNumbers:"
+ "setEventEndLocationAddressCountry:"
+ "setEventEndLocationAddressLatitude:"
+ "setEventEndLocationAddressLocality:"
+ "setEventEndLocationAddressLongitude:"
+ "setEventEndLocationAddressRegion:"
+ "setEventEndPersonNames:"
+ "setEventEstimatedEndDate:"
+ "setEventEstimatedEndDateTimeZone:"
+ "setEventEstimatedStartDate:"
+ "setEventEstimatedStartDateTimeZone:"
+ "setEventOrderDate:"
+ "setEventOrderDateTimeZone:"
+ "setEventRelatedMessageIdentifiers:"
+ "setEventRelatedSourceBundleIdentifiers:"
+ "setEventStartLocationAddressCountry:"
+ "setEventStartLocationAddressLatitude:"
+ "setEventStartLocationAddressLocality:"
+ "setEventStartLocationAddressLongitude:"
+ "setEventStartLocationAddressRegion:"
+ "setEventStartPersonNames:"
+ "setEventTrackingNumber:"
+ "setGroupID:"
+ "setIsTimeSensitive:"
+ "setIsWindowTabEntity:"
+ "setPreExtractionIsPartial:"
+ "setRemotePlaceholderBundleID:"
+ "setShortcutsToolInvocation:"
+ "setShortcutsToolInvocationSummary:"
+ "setTimeSensitiveStatus:"
+ "setWeekOfMonth:"
+ "setWeekOfYear:"
+ "setWeekday:"
+ "setWeekdayOrdinal:"
+ "setYearForWeekOfYear:"
+ "shipped"
+ "shipping_order"
+ "shortcutsToolInvocation"
+ "shortcutsToolInvocationSummary"
+ "skipTextSemanticSearchForSearchString:queryContext:skipReason:"
+ "timeSensitiveStatus"
+ "timeZone"
+ "timeZoneWithAbbreviation:"
+ "transit_card"
+ "w"
+ "weekOfMonth"
+ "weekOfYear"
+ "weekday"
+ "weekdayOrdinal"
+ "windowProcessIdentifier"
+ "windowProcessIdentifierVersion"
+ "yearForWeekOfYear"
- "### cancel qid=%ld error %@"
- "### qid=%ld error %@ reply:%@"
- "%lu. Final Photos item identifier (%@), L1Score=%f, L2Score=%f"
- "@\"CSRankingConfiguration\""
- "B48@0:8@16@24@32^@40"
- "CSRankingConfiguration"
- "EmbeddingDonation"
- "Handle instant answer batches %@ for query:%@"
- "Photos"
- "T@\"CSRankingConfiguration\",R,N,V_rankingConfiguration"
- "[CSSearchQuery]QOS _topHitQueryParameters: %d"
- "[CSUserQuery] WARN - forcing allowSemanticSearch=YES for pommesctl"
- "[CSUserQuery][qid=%ld] %@ semantic search, isFeatureFlagsEnabled: %@, isClientAllowed: %@, isGMOptedIn: %@"
- "[CSUserQuery][qid=%ld] %s query is a live query; also disabling blocking on index here."
- "[CSUserQuery][qid=%ld] enabling pommes suggestions"
- "[CSUserQuery][qid=%ld] generating query"
- "[CSUserQuery][qid=%ld] updating query context"
- "[Pommes] Could not archive queryUnderstandingOutput %@"
- "[Pommes] Could not unarchive queryUnderstandingOutput %@"
- "[QoS] %u qid=%ld - Starting %@"
- "[QoS] %u qid=%ld - gather ended"
- "[QoS] %u qid=%ld - handleReply"
- "[QoS] %u qid=%ld didReturnResults"
- "[QoS] %u qid=%ld didReturnResults inside method async call. attribute:%b counting:%b live:%b"
- "[QoS] %u qid=%ld sendMessageAsync response"
- "[TopHit Thresholding][qid=%d][num_tokens=%lu] Results beyond the top %lu results are filtered"
- "[TopHit Thresholding][qid=%d][num_tokens=%lu] Thresholding applied at item %lu:\nScores={L1Score=%.04f, L1ScoreRatio=%.04f, L2Score=%.04f, L2ScoreRatio=%.04f, L2ScoreDiff=%.04f}"
- "_rankingConfiguration"
- "allowing"
- "disallowing"
- "flattenCSFieldSpecifications:"
- "initWithAddress:synonyms:confidence:"
- "initWithQueryContext:"
- "initWithRankingConfiguration:"
- "kMDUserQueryDictionaryQueryTokenCountKey"
- "qid=%d is a live query; also disabling blocking on index."
- "qid=%ld - %@"
- "qid=%ld - Canceling"
- "qid=%ld - Dropping results"
- "qid=%ld - Finished"
- "qid=%ld - Finished (cancelled)"
- "qid=%ld - Finished with error error:%@"
- "qid=%ld - Found: %ld instant answers"
- "qid=%ld - Found: %ld items"
- "qid=%ld - Found: %ld suggestions"
- "qid=%ld - Gather ended"
- "qid=%ld - Got completions %@"
- "qid=%ld - Handle completion batches %@ for query:%@"
- "qid=%ld - Handle instant answer batches %@ for query:%@"
- "qid=%ld - Handle suggestion batches %@ for query:%@"
- "qid=%ld - Missing bundleID for item with ID: %@"
- "qid=%ld - Opcode 0x%x not handled"
- "qid=%ld - Plists count %ld "
- "qid=%ld - Polling"
- "qid=%ld - Priority Gather ended"
- "qid=%ld - RemoveResults tag:0x%x opcode :0x%x"
- "qid=%ld - Removed: %ld items"
- "qid=%ld - Resolved attribute names: %@"
- "qid=%ld - Result oidData: %p"
- "qid=%ld - Results type: %d "
- "qid=%ld - Starting %@"
- "qid=%ld - Unknown type :%d"
- "qid=%ld - Updated: %ld items"
- "qid=%ld - [ContactSearch]  %lu available at query completion"
- "qid=%ld - [ContactSearch] All contacts are already processed or have [FROM] scopes"
- "qid=%ld - [ContactSearch] Autoscoping couldn't be computed for any contacts"
- "qid=%ld - [ContactSearch] Processed contacts: %lu, Author contacts: %lu"
- "qid=%ld - [ContactSearch] Processed contacts: %lu, Recipient contacts: %lu, Total trimmed contacts: %lu"
- "qid=%ld - [ContactSearch] Timed out waiting for results at query completion"
- "qid=%ld - [ContactSearch] Total contacts: %lu, Cached contacts: %lu, Fresh contacts: %lu"
- "qid=%ld - [ContactSearch] Waiting for results at query completion"
- "qid=%ld - [ContactSearch] none available at query completion"
- "qid=%ld - [ContactSearch] suggestions.count %lu != results.count %lu"
- "qid=%ld - moved: %ld items"
- "qid=%ld - wait for suggestion count"
- "qid=%lu - current batch has %ld items (%ld items are L1 topHit candidates, %ld items are L2 topHit candidates)"
- "qid=%lu - query (length=%lu, trimmed length=%lu) is too short (threshold=%lu) for topHit results"
- "qid=%lu - returning empty tophits"
- "query does not match length criteria (tokenCount: %u, normalizedQueryLength: %lu, containsCJK: %d)"
- "rankingConfiguration"
- "skipTextSemanticSearchForSearchString:tokenCount:queryContext:skipReason:"

```
