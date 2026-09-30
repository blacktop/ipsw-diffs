## NewsToday

> `/System/Library/PrivateFrameworks/NewsToday.framework/NewsToday`

```diff

-5871.1.0.0.0
-  __TEXT.__text: 0x47c58
-  __TEXT.__auth_stubs: 0xda0
-  __TEXT.__objc_methlist: 0x63dc
+5877.1.0.0.0
+  __TEXT.__text: 0x48be8
+  __TEXT.__auth_stubs: 0xe20
+  __TEXT.__objc_methlist: 0x6454
   __TEXT.__const: 0xcf8
   __TEXT.__oslogstring: 0x15a0
-  __TEXT.__cstring: 0x8eb5
+  __TEXT.__cstring: 0x8f45
   __TEXT.__ustring: 0x16
-  __TEXT.__gcc_except_tab: 0xa68
+  __TEXT.__gcc_except_tab: 0xa9c
   __TEXT.__constg_swiftt: 0x240
   __TEXT.__swift5_typeref: 0x3a1
   __TEXT.__swift5_reflstr: 0x78d

   __TEXT.__swift5_types: 0x38
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x20
-  __TEXT.__unwind_info: 0x1018
-  __TEXT.__eh_frame: 0x8d0
+  __TEXT.__unwind_info: 0x1038
+  __TEXT.__eh_frame: 0x8e8
   __TEXT.__objc_classname: 0xb60
-  __TEXT.__objc_methname: 0x137db
-  __TEXT.__objc_methtype: 0x2082
-  __TEXT.__objc_stubs: 0x9860
-  __DATA_CONST.__got: 0xa08
-  __DATA_CONST.__const: 0x1778
+  __TEXT.__objc_methname: 0x13a55
+  __TEXT.__objc_methtype: 0x20a2
+  __TEXT.__objc_stubs: 0x9a60
+  __DATA_CONST.__got: 0xa48
+  __DATA_CONST.__const: 0x17c8
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3cc8
+  __DATA_CONST.__objc_selrefs: 0x3d48
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x1b8
   __DATA_CONST.__objc_arraydata: 0x1a0
-  __AUTH_CONST.__auth_got: 0x6e0
+  __AUTH_CONST.__auth_got: 0x720
   __AUTH_CONST.__const: 0xda8
-  __AUTH_CONST.__cfstring: 0x1dc0
-  __AUTH_CONST.__objc_const: 0xdc38
+  __AUTH_CONST.__cfstring: 0x1de0
+  __AUTH_CONST.__objc_const: 0xdd70
   __AUTH_CONST.__objc_intobj: 0x120
+  __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x508
   __AUTH.__data: 0x198
-  __DATA.__objc_ivar: 0x5a0
-  __DATA.__data: 0x13f0
+  __DATA.__objc_ivar: 0x5b8
+  __DATA.__data: 0x1400
   __DATA.__bss: 0x16a0
   __DATA_DIRTY.__objc_data: 0xff0
   __DATA_DIRTY.__bss: 0x78

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A1C707BA-D7CB-3366-9544-676DE3022339
-  Functions: 1982
-  Symbols:   6621
-  CStrings:  4049
+  UUID: FB448A8C-02BB-3594-A1AA-E5990B2EA226
+  Functions: 2004
+  Symbols:   6688
+  CStrings:  4081
 
Symbols:
+ -[NTCatchUpOperation _fetchForYouResultsUsingDaemonWithCompletion:]
+ -[NTCatchUpOperation _fetchForYouResultsUsingDaemonWithCompletion:].cold.1
+ -[NTCatchUpOperation _fetchForYouResultsUsingFeedRequestWithCompletion:]
+ -[NTCatchUpOperation _fetchForYouResultsUsingFeedRequestWithCompletion:].cold.1
+ -[NTCatchUpOperation setShouldIssueShadowDaemonFetch:]
+ -[NTCatchUpOperation shouldIssueShadowDaemonFetch]
+ -[NTForYouRequest enableGlobalESL]
+ -[NTForYouRequest enablePeopleAlsoRead]
+ -[NTForYouRequest enablePerTagESL]
+ -[NTForYouRequest preferredESLRatio]
+ -[NTForYouSectionFetchDescriptor _resolvedForYouSource]
+ -[NTForYouSectionFetchDescriptor _shouldIssueShadowDaemonFetch]
+ -[NTForYouSectionFetchDescriptor appConfiguration]
+ -[NTHeadlinePersonalizationMetadata initWithArticleID:publisherID:scoredTopicIDs:scoreProfile:]
+ -[NTHeadlinePersonalizationMetadata initWithArticleID:publisherID:scoredTopicIDs:scoreProfile:].cold.1
+ -[NTHeadlinePersonalizationMetadata initWithArticleID:publisherID:scoredTopicIDs:scoreProfile:].cold.2
+ -[NTHeadlinePersonalizationMetadata initWithArticleID:publisherID:scoredTopicIDs:scoreProfile:].cold.3
+ -[NTHeadlinePersonalizationMetadata scoreProfile]
+ -[NTTodayPrivateData initWithDerivedPersonalizationData:localNewsTagID:mutedTagIDs:autoFavoriteTagIDs:purchasedTagIDs:groupableTagIDs:rankedAllSubscribedTagIDs:rankedAllSubscriptionDates:recentlySeenHistoryItems:recentlyReadHistoryItems:onboardingVersion:bundleSubscription:]
+ _FCCKWidgetSectionConfigForYouSectionEnableGlobalESLKey
+ _FCCKWidgetSectionConfigForYouSectionEnablePeopleAlsoReadKey
+ _FCCKWidgetSectionConfigForYouSectionEnablePerTagESLKey
+ _FCCKWidgetSectionConfigForYouSectionPreferredESLRatioKey
+ _FCWidgetForYouSourceOverrideSharedPreferenceKey
+ _OBJC_CLASS_$_NTPBScoreProfile
+ _OBJC_IVAR_$_NTCatchUpOperation._shouldIssueShadowDaemonFetch
+ _OBJC_IVAR_$_NTForYouRequest._enableGlobalESL
+ _OBJC_IVAR_$_NTForYouRequest._enablePeopleAlsoRead
+ _OBJC_IVAR_$_NTForYouRequest._enablePerTagESL
+ _OBJC_IVAR_$_NTForYouRequest._preferredESLRatio
+ _OBJC_IVAR_$_NTForYouSectionFetchDescriptor._appConfiguration
+ _OBJC_IVAR_$_NTHeadlinePersonalizationMetadata._scoreProfile
+ __OBJC_$_PROP_LIST_NTHeadlinePersonalizationMetadata.77
+ ___64-[NTCatchUpOperation _fetchForYouResultsIfNeededWithCompletion:]_block_invoke_5
+ ___64-[NTCatchUpOperation _fetchForYouResultsIfNeededWithCompletion:]_block_invoke_6
+ ___67-[NTCatchUpOperation _fetchForYouResultsUsingDaemonWithCompletion:]_block_invoke
+ ___67-[NTCatchUpOperation _fetchForYouResultsUsingDaemonWithCompletion:]_block_invoke_2
+ ___67-[NTCatchUpOperation _fetchForYouResultsUsingDaemonWithCompletion:]_block_invoke_3
+ ___72-[NTCatchUpOperation _fetchForYouResultsUsingFeedRequestWithCompletion:]_block_invoke
+ ___72-[NTCatchUpOperation _fetchForYouResultsUsingFeedRequestWithCompletion:]_block_invoke_2
+ ___72-[NTCatchUpOperation _fetchForYouResultsUsingFeedRequestWithCompletion:]_block_invoke_3
+ ___82-[NTCatchUpOperation _fetchArticleListAndArticleIDsResultsIfNeededWithCompletion:]_block_invoke.92
+ ___block_descriptor_40_e8_32s_e85_v32?0"NTCatchUpOperationResults"8"NTCatchUpOperationForYouFetchInfo"16"NSError"24ls32l8
+ ___block_descriptor_48_e8_32s40bs_e49_v36?0"NSArray"8"NSDictionary"16B24"NSError"28ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e85_v32?0"NTCatchUpOperationResults"8"NTCatchUpOperationForYouFetchInfo"16"NSError"24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e85_v32?0"NTCatchUpOperationResults"8"NTCatchUpOperationForYouFetchInfo"16"NSError"24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
+ _objc_msgSend$_fetchForYouResultsUsingDaemonWithCompletion:
+ _objc_msgSend$_fetchForYouResultsUsingFeedRequestWithCompletion:
+ _objc_msgSend$_resolvedForYouSource
+ _objc_msgSend$_shouldIssueShadowDaemonFetch
+ _objc_msgSend$data
+ _objc_msgSend$enableGlobalESL
+ _objc_msgSend$enablePeopleAlsoRead
+ _objc_msgSend$enablePerTagESL
+ _objc_msgSend$initWithArticleID:publisherID:scoredTopicIDs:scoreProfile:
+ _objc_msgSend$initWithData:
+ _objc_msgSend$initWithDerivedPersonalizationData:localNewsTagID:mutedTagIDs:autoFavoriteTagIDs:purchasedTagIDs:groupableTagIDs:rankedAllSubscribedTagIDs:rankedAllSubscriptionDates:recentlySeenHistoryItems:recentlyReadHistoryItems:onboardingVersion:bundleSubscription:
+ _objc_msgSend$preferredESLRatio
+ _objc_msgSend$setEnableGlobalESL:
+ _objc_msgSend$setEnablePeopleAlsoRead:
+ _objc_msgSend$setEnablePerTagESL:
+ _objc_msgSend$setPreferredESLRatio:
+ _objc_msgSend$setShouldIssueShadowDaemonFetch:
+ _objc_msgSend$shouldIssueShadowDaemonFetch
+ _objc_msgSend$widgetForYouShadowDaemonFetchEnabled
- -[NTHeadlinePersonalizationMetadata initWithArticleID:publisherID:scoredTopicIDs:]
- -[NTHeadlinePersonalizationMetadata initWithArticleID:publisherID:scoredTopicIDs:].cold.1
- -[NTHeadlinePersonalizationMetadata initWithArticleID:publisherID:scoredTopicIDs:].cold.2
- -[NTHeadlinePersonalizationMetadata initWithArticleID:publisherID:scoredTopicIDs:].cold.3
- -[NTTodayPrivateData initWithDerivedPersonalizationData:localNewsTagID:mutedTagIDs:autoFavoriteTagIDs:purchasedTagIDs:groupableTagIDs:rankedAllSubscribedTagIDs:rankedAllSubscriptionDates:recentlySeenHistoryItems:recentlyReadHistoryItems:onboardingVersion:bundleSubscription:userEmbeddingData:]
- -[NTTodayPrivateData userEmbeddingData]
- _FCWidgetForYouSourceSharedPreferenceKey
- _OBJC_IVAR_$_NTTodayPrivateData._userEmbeddingData
- __OBJC_$_PROP_LIST_NTHeadlinePersonalizationMetadata.65
- ___64-[NTCatchUpOperation _fetchForYouResultsIfNeededWithCompletion:]_block_invoke.90
- ___82-[NTCatchUpOperation _fetchArticleListAndArticleIDsResultsIfNeededWithCompletion:]_block_invoke.96
- ___block_descriptor_41_e8_32s_e5_8?0ls32l8
- ___block_descriptor_49_e8_32s40bs_e49_v36?0"NSArray"8"NSDictionary"16B24"NSError"28ls32l8s40l8
- ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- _objc_msgSend$initWithArticleID:publisherID:scoredTopicIDs:
- _objc_msgSend$initWithDerivedPersonalizationData:localNewsTagID:mutedTagIDs:autoFavoriteTagIDs:purchasedTagIDs:groupableTagIDs:rankedAllSubscribedTagIDs:rankedAllSubscriptionDates:recentlySeenHistoryItems:recentlyReadHistoryItems:onboardingVersion:bundleSubscription:userEmbeddingData:
- _objc_msgSend$userEmbeddingData
CStrings:
+ "\f"
+ "-[NTCatchUpOperation _fetchForYouResultsUsingDaemonWithCompletion:]"
+ "-[NTCatchUpOperation _fetchForYouResultsUsingFeedRequestWithCompletion:]"
+ "-[NTHeadlinePersonalizationMetadata initWithArticleID:publisherID:scoredTopicIDs:scoreProfile:]"
+ "@\"NTPBScoreProfile\""
+ "@\"NTPBScoreProfile\"16@0:8"
+ "@112@0:8@16@24@32@40@48@56@64@72@80@88@96@104"
+ "T@\"<FCNewsAppConfiguration>\",R,N,V_appConfiguration"
+ "T@\"NTPBScoreProfile\",R,N"
+ "T@\"NTPBScoreProfile\",R,N,V_scoreProfile"
+ "TB,N,V_shouldIssueShadowDaemonFetch"
+ "TB,R,N,V_enableGlobalESL"
+ "TB,R,N,V_enablePeopleAlsoRead"
+ "TB,R,N,V_enablePerTagESL"
+ "Td,R,N,V_preferredESLRatio"
+ "_enableGlobalESL"
+ "_enablePeopleAlsoRead"
+ "_enablePerTagESL"
+ "_fetchForYouResultsUsingDaemonWithCompletion:"
+ "_fetchForYouResultsUsingFeedRequestWithCompletion:"
+ "_preferredESLRatio"
+ "_resolvedForYouSource"
+ "_scoreProfile"
+ "_shouldIssueShadowDaemonFetch"
+ "enableGlobalESL"
+ "enablePeopleAlsoRead"
+ "enablePerTagESL"
+ "initWithArticleID:publisherID:scoredTopicIDs:scoreProfile:"
+ "initWithData:"
+ "initWithDerivedPersonalizationData:localNewsTagID:mutedTagIDs:autoFavoriteTagIDs:purchasedTagIDs:groupableTagIDs:rankedAllSubscribedTagIDs:rankedAllSubscriptionDates:recentlySeenHistoryItems:recentlyReadHistoryItems:onboardingVersion:bundleSubscription:"
+ "preferredESLRatio"
+ "setEnableGlobalESL:"
+ "setEnablePeopleAlsoRead:"
+ "setEnablePerTagESL:"
+ "setPreferredESLRatio:"
+ "setShouldIssueShadowDaemonFetch:"
+ "shouldIssueShadowDaemonFetch"
+ "widgetForYouShadowDaemonFetchEnabled"
- "-[NTHeadlinePersonalizationMetadata initWithArticleID:publisherID:scoredTopicIDs:]"
- "@\"NSData\""
- "@120@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112"
- "T@\"NSData\",R,C,N"
- "T@\"NSData\",R,C,N,V_userEmbeddingData"
- "_userEmbeddingData"
- "initWithArticleID:publisherID:scoredTopicIDs:"
- "initWithDerivedPersonalizationData:localNewsTagID:mutedTagIDs:autoFavoriteTagIDs:purchasedTagIDs:groupableTagIDs:rankedAllSubscribedTagIDs:rankedAllSubscriptionDates:recentlySeenHistoryItems:recentlyReadHistoryItems:onboardingVersion:bundleSubscription:userEmbeddingData:"
- "userEmbeddingData"

```
