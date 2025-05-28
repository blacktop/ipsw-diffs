## NewsCore

> `/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore`

```diff

-5325.6.0.0.0
-  __TEXT.__text: 0x2c59ec
-  __TEXT.__auth_stubs: 0x1360
-  __TEXT.__objc_methlist: 0x28c98
-  __TEXT.__const: 0x1408
+5345.2.0.0.0
+  __TEXT.__text: 0x2c5894
+  __TEXT.__auth_stubs: 0x1350
+  __TEXT.__objc_methlist: 0x28d90
+  __TEXT.__const: 0x13f8
   __TEXT.__swift5_typeref: 0x89
-  __TEXT.__cstring: 0x46055
-  __TEXT.__oslogstring: 0xf004
+  __TEXT.__cstring: 0x460f7
+  __TEXT.__oslogstring: 0xef06
   __TEXT.__gcc_except_tab: 0x362c
   __TEXT.__dlopen_cstrs: 0x11c
   __TEXT.__ustring: 0x122
-  __TEXT.__unwind_info: 0x9a9c
-  __TEXT.__objc_classname: 0x6a37
-  __TEXT.__objc_methname: 0x7931b
-  __TEXT.__objc_methtype: 0xbaac
-  __TEXT.__objc_stubs: 0x31120
+  __TEXT.__unwind_info: 0x9ad0
+  __TEXT.__objc_classname: 0x6a71
+  __TEXT.__objc_methname: 0x799cb
+  __TEXT.__objc_methtype: 0xbb74
+  __TEXT.__objc_stubs: 0x31160
   __DATA_CONST.__got: 0x370
-  __DATA_CONST.__const: 0xfe90
-  __DATA_CONST.__objc_classlist: 0x1918
+  __DATA_CONST.__const: 0xfec0
+  __DATA_CONST.__objc_classlist: 0x1920
   __DATA_CONST.__objc_catlist: 0x268
   __DATA_CONST.__objc_protolist: 0x6b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x612b0
-  __DATA_CONST.__objc_selrefs: 0x126d8
+  __DATA_CONST.__objc_const: 0x615b8
+  __DATA_CONST.__objc_selrefs: 0x12730
+  __DATA_CONST.__objc_protorefs: 0xa8
+  __DATA_CONST.__objc_classrefs: 0x1e78
+  __DATA_CONST.__objc_superrefs: 0x1390
   __DATA_CONST.__objc_arraydata: 0xfc8
   __AUTH_CONST.__const: 0x4670
-  __AUTH_CONST.__objc_const: 0x12650
-  __AUTH_CONST.__cfstring: 0x29940
+  __AUTH_CONST.__objc_const: 0x12698
+  __AUTH_CONST.__cfstring: 0x299e0
   __AUTH_CONST.__objc_intobj: 0x1308
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_dictobj: 0xbe0
   __AUTH_CONST.__objc_doubleobj: 0x110
-  __AUTH_CONST.__auth_got: 0x9c8
-  __AUTH.__objc_data: 0x3ed0
-  __DATA.__objc_protorefs: 0xa8
-  __DATA.__objc_classrefs: 0x1e68
-  __DATA.__objc_superrefs: 0x1380
-  __DATA.__objc_ivar: 0x3e20
+  __AUTH_CONST.__auth_got: 0x9c0
+  __AUTH.__objc_data: 0x3b10
+  __DATA.__objc_ivar: 0x3e38
   __DATA.__data: 0x5118
-  __DATA.__common: 0x8
   __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_ivar: 0xeb8
-  __DATA_DIRTY.__objc_data: 0xbc20
+  __DATA_DIRTY.__objc_data: 0xc030
   __DATA_DIRTY.__data: 0x30
-  __DATA_DIRTY.__common: 0x170
+  __DATA_DIRTY.__common: 0x178
   __DATA_DIRTY.__bss: 0xe48
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17810
-  Symbols:   57917
-  CStrings:  27678
+  Functions: 17828
+  Symbols:   57975
+  CStrings:  27727
 
Symbols:
+ -[FCAppleAccount dynamicPrimaryLanguageCode]
+ -[FCAppleAccount dynamicSupportedContentLanguage]
+ -[FCEndpointConfiguration appAnalyticsAppHeartbeatBaseURLString]
+ -[FCEndpointConfiguration initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:puzzlesArchiveAPIBaseURLString:appAnalyticsNotificationReceiptBaseURLString:authTokenAPIBaseURLString:sportsDataVisualizationAPIBaseURLString:fineGrainedNewsletterSubscriptionBaseURLString:appAnalyticsSportsEventsBaseURLString:appAnalyticsAppHealthBaseURLString:appAnalyticsAppHeartbeatBaseURLString:ckOrderFeedBaseURLString:ckMultiFetchBaseURLString:ckRecordFetchBaseURLString:ckEdgeCachedOrderFeedBaseURLString:ckEdgeCachedMultiFetchBaseURLString:]
+ -[FCNewsAppConfig appAnalyticsAppHeartbeatEndpointUrlForEnvironment:]
+ -[FCNewsAppConfig audioPlaylistSweepListeningPercentageThreshold]
+ -[FCNewsAppConfig audioPlaylistSweepRecencyThresholdInDays]
+ -[FCNewsAppConfig foregroundHeartbeatEventEnabled]
+ -[FCNewsTabiConfiguration setTagSuggestionsConfiguration:]
+ -[FCNewsTabiConfiguration tagSuggestionsConfiguration]
+ -[FCNewsTabiTagSuggestionsConfiguration .cxx_destruct]
+ -[FCNewsTabiTagSuggestionsConfiguration bundleOutputConfiguration]
+ -[FCNewsTabiTagSuggestionsConfiguration initWithDictionary:]
+ -[FCNewsTabiTagSuggestionsConfiguration nonBundleOutputConfiguration]
+ -[FCNewsTabiTagSuggestionsConfiguration setBundleOutputConfiguration:]
+ -[FCNewsTabiTagSuggestionsConfiguration setNonBundleOutputConfiguration:]
+ -[FCNewsTabiTagSuggestionsOutputConfiguration .cxx_destruct]
+ -[FCNewsTabiTagSuggestionsOutputConfiguration channelIDsOutputName]
+ -[FCNewsTabiTagSuggestionsOutputConfiguration channelScoresOutputName]
+ -[FCNewsTabiTagSuggestionsOutputConfiguration initWithDictionary:]
+ -[FCNewsTabiTagSuggestionsOutputConfiguration setChannelIDsOutputName:]
+ -[FCNewsTabiTagSuggestionsOutputConfiguration setChannelScoresOutputName:]
+ -[FCNewsTabiTagSuggestionsOutputConfiguration setTopicIDsOutputName:]
+ -[FCNewsTabiTagSuggestionsOutputConfiguration setTopicScoresOutputName:]
+ -[FCNewsTabiTagSuggestionsOutputConfiguration topicIDsOutputName]
+ -[FCNewsTabiTagSuggestionsOutputConfiguration topicScoresOutputName]
+ _.str.130
+ _.str.136
+ _FCNewsForegroundHeartbeatEventEnabledKey
+ _OBJC_CLASS_$_FCNewsTabiTagSuggestionsConfiguration
+ _OBJC_CLASS_$_FCNewsTabiTagSuggestionsOutputConfiguration
+ _OBJC_IVAR_$_FCEndpointConfiguration._appAnalyticsAppHeartbeatBaseURLString
+ _OBJC_IVAR_$_FCNewsTabiConfiguration._tagSuggestionsConfiguration
+ _OBJC_IVAR_$_FCNewsTabiTagSuggestionsConfiguration._bundleOutputConfiguration
+ _OBJC_IVAR_$_FCNewsTabiTagSuggestionsConfiguration._nonBundleOutputConfiguration
+ _OBJC_IVAR_$_FCNewsTabiTagSuggestionsOutputConfiguration._channelIDsOutputName
+ _OBJC_IVAR_$_FCNewsTabiTagSuggestionsOutputConfiguration._channelScoresOutputName
+ _OBJC_IVAR_$_FCNewsTabiTagSuggestionsOutputConfiguration._topicIDsOutputName
+ _OBJC_IVAR_$_FCNewsTabiTagSuggestionsOutputConfiguration._topicScoresOutputName
+ _OBJC_METACLASS_$_FCNewsTabiTagSuggestionsConfiguration
+ _OBJC_METACLASS_$_FCNewsTabiTagSuggestionsOutputConfiguration
+ __OBJC_$_INSTANCE_METHODS_FCNewsTabiTagSuggestionsConfiguration
+ __OBJC_$_INSTANCE_METHODS_FCNewsTabiTagSuggestionsOutputConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_FCNewsTabiTagSuggestionsConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_FCNewsTabiTagSuggestionsOutputConfiguration
+ __OBJC_$_PROP_LIST_FCAppleAccount.235
+ __OBJC_$_PROP_LIST_FCContentContext.471
+ __OBJC_$_PROP_LIST_FCContentContextInternal.643
+ __OBJC_$_PROP_LIST_FCDerivedPersonalizationData.114
+ __OBJC_$_PROP_LIST_FCFeldsparIDProvider.114
+ __OBJC_$_PROP_LIST_FCFetchedValueManager.122
+ __OBJC_$_PROP_LIST_FCMutableNotificationData.137
+ __OBJC_$_PROP_LIST_FCMutableTodayPrivateData.248
+ __OBJC_$_PROP_LIST_FCNetworkSession.240
+ __OBJC_$_PROP_LIST_FCNewsAvailabilityMonitor.117
+ __OBJC_$_PROP_LIST_FCNewsTabiTagSuggestionsConfiguration
+ __OBJC_$_PROP_LIST_FCNewsTabiTagSuggestionsOutputConfiguration
+ __OBJC_$_PROP_LIST_FCNewsletterManager.306
+ __OBJC_$_PROP_LIST_FCNotificationDropboxData.120
+ __OBJC_$_PROP_LIST_FCPaymentTransactionManager.111
+ __OBJC_$_PROP_LIST_FCPrivateDataContext.241
+ __OBJC_$_PROP_LIST_FCPrivateDataContextInternal.298
+ __OBJC_$_PROP_LIST_FCReadonlyPersonalizationAggregateStore.155
+ __OBJC_$_PROP_LIST_FCTodayPrivateData.189
+ __OBJC_CLASS_RO_$_FCNewsTabiTagSuggestionsConfiguration
+ __OBJC_CLASS_RO_$_FCNewsTabiTagSuggestionsOutputConfiguration
+ __OBJC_METACLASS_RO_$_FCNewsTabiTagSuggestionsConfiguration
+ __OBJC_METACLASS_RO_$_FCNewsTabiTagSuggestionsOutputConfiguration
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeI26NTPBKeyValuePair_ValueTypeU8__strongPU32objcproto21FCKeyValueStoreCoding10objc_classEEPvEEEEEclB8ue170006EPSA_
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ ___103-[FCSubscriptionController fetchAllTagsWithCallbackQueue:maximumCachedAge:qualityOfService:completion:]_block_invoke.393
+ ___103-[FCSubscriptionController fetchAllTagsWithCallbackQueue:maximumCachedAge:qualityOfService:completion:]_block_invoke_2.394
+ ___122-[FCSubscriptionController addAutoFavoriteSubscriptionForTagIDs:groupableSubscriptionForTagIDs:originProvider:completion:]_block_invoke.415
+ ___122-[FCSubscriptionController addAutoFavoriteSubscriptionForTagIDs:groupableSubscriptionForTagIDs:originProvider:completion:]_block_invoke.421
+ ___122-[FCSubscriptionController addAutoFavoriteSubscriptionForTagIDs:groupableSubscriptionForTagIDs:originProvider:completion:]_block_invoke.427
+ ___122-[FCSubscriptionController addAutoFavoriteSubscriptionForTagIDs:groupableSubscriptionForTagIDs:originProvider:completion:]_block_invoke_2.418
+ ___122-[FCSubscriptionController addAutoFavoriteSubscriptionForTagIDs:groupableSubscriptionForTagIDs:originProvider:completion:]_block_invoke_2.428
+ ___211-[FCHeadlineClusterOrderingPersonalizedTopical orderTopicsWithClusteredHeadlines:additionalHeadlines:subscribedTagIDs:scoresByArticleID:personalizer:tagNameProvider:personalizationTreatment:translationProvider:]_block_invoke.280
+ ___211-[FCHeadlineClusterOrderingPersonalizedTopical orderTopicsWithClusteredHeadlines:additionalHeadlines:subscribedTagIDs:scoresByArticleID:personalizer:tagNameProvider:personalizationTreatment:translationProvider:]_block_invoke.287
+ ___211-[FCHeadlineClusterOrderingPersonalizedTopical orderTopicsWithClusteredHeadlines:additionalHeadlines:subscribedTagIDs:scoresByArticleID:personalizer:tagNameProvider:personalizationTreatment:translationProvider:]_block_invoke_2.281
+ ___211-[FCHeadlineClusterOrderingPersonalizedTopical orderTopicsWithClusteredHeadlines:additionalHeadlines:subscribedTagIDs:scoresByArticleID:personalizer:tagNameProvider:personalizationTreatment:translationProvider:]_block_invoke_2.288
+ ___29-[FCOperation _startIfNeeded]_block_invoke.85
+ ___39-[FCCKPrivateDatabase _continueStartUp]_block_invoke.147
+ ___41-[NTPBAVAsset(Bookmark) resolvedCacheURL]_block_invoke.120
+ ___43-[FCRecordsFetchOperation performOperation]_block_invoke.292
+ ___43-[FCRecordsFetchOperation performOperation]_block_invoke.297
+ ___43-[FCRecordsFetchOperation performOperation]_block_invoke_2.293
+ ___43-[FCRecordsFetchOperation performOperation]_block_invoke_2.298
+ ___44-[FCAppleAccount dynamicPrimaryLanguageCode]_block_invoke
+ ___44-[FCAppleAccount dynamicPrimaryLanguageCode]_block_invoke_2
+ ___48-[FCOperation _handleThrottlingFromError:delay:]_block_invoke.102
+ ___48-[FCTodayFeedConfigOperation _fetchFromNewsEdge]_block_invoke.80
+ ___48-[FCTodayFeedConfigOperation _fetchFromNewsEdge]_block_invoke_2.81
+ ___54-[FCSubscriptionController _saveReadableSubscriptions]_block_invoke.518
+ ___58-[FCSearchOperation _fetchFullHeadlineResultsForArticles:]_block_invoke.217
+ ___71-[FCCloudContext fetchShouldSecureSubscriptionsForDatabase:completion:]_block_invoke.200
+ ___71-[FCCloudContext fetchShouldSecureSubscriptionsForDatabase:completion:]_block_invoke_2.201
+ ___76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke.173
+ ___76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke.182
+ ___76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke_2.174
+ ___76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke_2.184
+ ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke.449
+ ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke_2.450
+ ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke_3.454
+ ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke_4.457
+ ___87-[FCCloudContext fetchOriginalDataShouldBeDeletedAfterMigrationForDatabase:completion:]_block_invoke.189
+ ___87-[FCCloudContext fetchOriginalDataShouldBeDeletedAfterMigrationForDatabase:completion:]_block_invoke_2.190
+ ___block_literal_global.1193
+ ___block_literal_global.1260
+ ___block_literal_global.133
+ ___block_literal_global.1335
+ ___block_literal_global.1337
+ ___block_literal_global.1339
+ ___block_literal_global.1347
+ ___block_literal_global.1358
+ ___block_literal_global.1363
+ ___block_literal_global.1368
+ ___block_literal_global.1373
+ ___block_literal_global.141
+ ___block_literal_global.143
+ ___block_literal_global.145
+ ___block_literal_global.167
+ ___block_literal_global.1742
+ ___block_literal_global.1774
+ ___block_literal_global.1826
+ ___block_literal_global.1839
+ ___block_literal_global.1852
+ ___block_literal_global.1862
+ ___block_literal_global.1875
+ ___block_literal_global.191
+ ___block_literal_global.2008
+ ___block_literal_global.2033
+ ___block_literal_global.2103
+ ___block_literal_global.2116
+ ___block_literal_global.220
+ ___block_literal_global.242
+ ___block_literal_global.266
+ ___block_literal_global.269
+ ___block_literal_global.272
+ ___block_literal_global.277
+ ___block_literal_global.309
+ ___block_literal_global.312
+ ___block_literal_global.314
+ ___block_literal_global.316
+ ___block_literal_global.319
+ ___block_literal_global.321
+ ___block_literal_global.328
+ ___block_literal_global.367
+ ___block_literal_global.393
+ ___block_literal_global.402
+ ___block_literal_global.405
+ ___block_literal_global.417
+ ___block_literal_global.420
+ ___block_literal_global.431
+ ___block_literal_global.434
+ ___block_literal_global.439
+ ___block_literal_global.453
+ ___block_literal_global.456
+ ___block_literal_global.467
+ ___block_literal_global.470
+ ___block_literal_global.485
+ ___block_literal_global.77
+ ___block_literal_global.853
+ ___block_literal_global.882
+ _kFCNewsTabiTagSuggestionsConfigurationBundleOutputNameKey
+ _kFCNewsTabiTagSuggestionsConfigurationKey
+ _kFCNewsTabiTagSuggestionsConfigurationNonBundleOutputNameKey
+ _kFCNewsTabiTagSuggestionsOutputConfigurationChannelIDsOutputName
+ _kFCNewsTabiTagSuggestionsOutputConfigurationChannelScoresOutputName
+ _kFCNewsTabiTagSuggestionsOutputConfigurationTopicIDsOutputName
+ _kFCNewsTabiTagSuggestionsOutputConfigurationTopicScoresOutputName
+ _objc_msgSend$appAnalyticsAppHeartbeatBaseURLString
+ _objc_msgSend$initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:puzzlesArchiveAPIBaseURLString:appAnalyticsNotificationReceiptBaseURLString:authTokenAPIBaseURLString:sportsDataVisualizationAPIBaseURLString:fineGrainedNewsletterSubscriptionBaseURLString:appAnalyticsSportsEventsBaseURLString:appAnalyticsAppHealthBaseURLString:appAnalyticsAppHeartbeatBaseURLString:ckOrderFeedBaseURLString:ckMultiFetchBaseURLString:ckRecordFetchBaseURLString:ckEdgeCachedOrderFeedBaseURLString:ckEdgeCachedMultiFetchBaseURLString:
+ _objc_msgSend$tagSuggestionsConfiguration
- +[FCResourceUnarchiver unarchiveResources:into:error:]
- -[FCEndpointConfiguration initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:appAnalyticsNotificationReceiptBaseURLString:authTokenAPIBaseURLString:sportsDataVisualizationAPIBaseURLString:fineGrainedNewsletterSubscriptionBaseURLString:appAnalyticsSportsEventsBaseURLString:appAnalyticsAppHealthBaseURLString:ckOrderFeedBaseURLString:ckMultiFetchBaseURLString:ckRecordFetchBaseURLString:ckEdgeCachedOrderFeedBaseURLString:ckEdgeCachedMultiFetchBaseURLString:]
- -[FCTopStoriesStyleConfiguration background_color]
- -[FCTopStoriesStyleConfiguration dark_style_background_color]
- _.str.129
- _.str.135
- _BOMCopierSetFatalErrorHandler
- _FCCKWidgetSectionConfigItemTypeWebEmbedKey
- _FCResourceUnarchiverCopyFatalErrorHandler
- _FCResourceUnarchiverCopyFileFinishedHandler
- _FCResourceUnarchiverErrorDomain
- _OBJC_CLASS_$_FCResourceUnarchiver
- _OBJC_IVAR_$_FCTopStoriesStyleConfiguration._background_color
- _OBJC_IVAR_$_FCTopStoriesStyleConfiguration._dark_style_background_color
- _OBJC_METACLASS_$_FCResourceUnarchiver
- __OBJC_$_CLASS_METHODS_FCResourceUnarchiver
- __OBJC_$_PROP_LIST_FCAppleAccount.232
- __OBJC_$_PROP_LIST_FCContentContext.468
- __OBJC_$_PROP_LIST_FCContentContextInternal.639
- __OBJC_$_PROP_LIST_FCDerivedPersonalizationData.113
- __OBJC_$_PROP_LIST_FCFeldsparIDProvider.113
- __OBJC_$_PROP_LIST_FCFetchedValueManager.121
- __OBJC_$_PROP_LIST_FCMutableNotificationData.136
- __OBJC_$_PROP_LIST_FCMutableTodayPrivateData.247
- __OBJC_$_PROP_LIST_FCNetworkSession.239
- __OBJC_$_PROP_LIST_FCNewsAvailabilityMonitor.116
- __OBJC_$_PROP_LIST_FCNewsletterManager.305
- __OBJC_$_PROP_LIST_FCNotificationDropboxData.119
- __OBJC_$_PROP_LIST_FCPaymentTransactionManager.110
- __OBJC_$_PROP_LIST_FCPrivateDataContext.240
- __OBJC_$_PROP_LIST_FCPrivateDataContextInternal.297
- __OBJC_$_PROP_LIST_FCReadonlyPersonalizationAggregateStore.154
- __OBJC_$_PROP_LIST_FCTodayPrivateData.188
- __OBJC_CLASS_RO_$_FCResourceUnarchiver
- __OBJC_METACLASS_RO_$_FCResourceUnarchiver
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI26NTPBKeyValuePair_ValueTypeU8__strongPU32objcproto21FCKeyValueStoreCoding10objc_classEENS_22__unordered_map_hasherIS2_S6_NS_4hashIiEENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S6_SB_S9_Lb1EEENS_9allocatorIS6_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS6_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI26NTPBKeyValuePair_ValueTypeU8__strongPU32objcproto21FCKeyValueStoreCoding10objc_classEENS_22__unordered_map_hasherIS2_S6_NS_4hashIiEENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S6_SB_S9_Lb1EEENS_9allocatorIS6_EEED2Ev
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeI26NTPBKeyValuePair_ValueTypeU8__strongPU32objcproto21FCKeyValueStoreCoding10objc_classEEPvEEEEEclB7v160006EPSA_
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___103-[FCSubscriptionController fetchAllTagsWithCallbackQueue:maximumCachedAge:qualityOfService:completion:]_block_invoke.389
- ___103-[FCSubscriptionController fetchAllTagsWithCallbackQueue:maximumCachedAge:qualityOfService:completion:]_block_invoke_2.392
- ___122-[FCSubscriptionController addAutoFavoriteSubscriptionForTagIDs:groupableSubscriptionForTagIDs:originProvider:completion:]_block_invoke.413
- ___122-[FCSubscriptionController addAutoFavoriteSubscriptionForTagIDs:groupableSubscriptionForTagIDs:originProvider:completion:]_block_invoke.419
- ___122-[FCSubscriptionController addAutoFavoriteSubscriptionForTagIDs:groupableSubscriptionForTagIDs:originProvider:completion:]_block_invoke.423
- ___122-[FCSubscriptionController addAutoFavoriteSubscriptionForTagIDs:groupableSubscriptionForTagIDs:originProvider:completion:]_block_invoke_2.416
- ___122-[FCSubscriptionController addAutoFavoriteSubscriptionForTagIDs:groupableSubscriptionForTagIDs:originProvider:completion:]_block_invoke_2.424
- ___211-[FCHeadlineClusterOrderingPersonalizedTopical orderTopicsWithClusteredHeadlines:additionalHeadlines:subscribedTagIDs:scoresByArticleID:personalizer:tagNameProvider:personalizationTreatment:translationProvider:]_block_invoke.279
- ___211-[FCHeadlineClusterOrderingPersonalizedTopical orderTopicsWithClusteredHeadlines:additionalHeadlines:subscribedTagIDs:scoresByArticleID:personalizer:tagNameProvider:personalizationTreatment:translationProvider:]_block_invoke.286
- ___211-[FCHeadlineClusterOrderingPersonalizedTopical orderTopicsWithClusteredHeadlines:additionalHeadlines:subscribedTagIDs:scoresByArticleID:personalizer:tagNameProvider:personalizationTreatment:translationProvider:]_block_invoke_2.280
- ___211-[FCHeadlineClusterOrderingPersonalizedTopical orderTopicsWithClusteredHeadlines:additionalHeadlines:subscribedTagIDs:scoresByArticleID:personalizer:tagNameProvider:personalizationTreatment:translationProvider:]_block_invoke_2.287
- ___29-[FCOperation _startIfNeeded]_block_invoke.84
- ___37-[FCAppleAccount primaryLanguageCode]_block_invoke_2
- ___37-[FCAppleAccount primaryLanguageCode]_block_invoke_3
- ___39-[FCCKPrivateDatabase _continueStartUp]_block_invoke.146
- ___41-[NTPBAVAsset(Bookmark) resolvedCacheURL]_block_invoke.119
- ___43-[FCRecordsFetchOperation performOperation]_block_invoke.290
- ___43-[FCRecordsFetchOperation performOperation]_block_invoke.296
- ___43-[FCRecordsFetchOperation performOperation]_block_invoke_2.292
- ___43-[FCRecordsFetchOperation performOperation]_block_invoke_2.297
- ___48-[FCOperation _handleThrottlingFromError:delay:]_block_invoke.101
- ___48-[FCTodayFeedConfigOperation _fetchFromNewsEdge]_block_invoke.78
- ___48-[FCTodayFeedConfigOperation _fetchFromNewsEdge]_block_invoke_2.80
- ___54-[FCSubscriptionController _saveReadableSubscriptions]_block_invoke.516
- ___58-[FCSearchOperation _fetchFullHeadlineResultsForArticles:]_block_invoke.216
- ___71-[FCCloudContext fetchShouldSecureSubscriptionsForDatabase:completion:]_block_invoke.198
- ___71-[FCCloudContext fetchShouldSecureSubscriptionsForDatabase:completion:]_block_invoke_2.200
- ___76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke.172
- ___76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke.181
- ___76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke_2.173
- ___76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke_2.183
- ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke.447
- ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke_2.448
- ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke_3.452
- ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke_4.455
- ___87-[FCCloudContext fetchOriginalDataShouldBeDeletedAfterMigrationForDatabase:completion:]_block_invoke.187
- ___87-[FCCloudContext fetchOriginalDataShouldBeDeletedAfterMigrationForDatabase:completion:]_block_invoke_2.189
- ___block_literal_global.1190
- ___block_literal_global.1257
- ___block_literal_global.1332
- ___block_literal_global.1334
- ___block_literal_global.1336
- ___block_literal_global.1344
- ___block_literal_global.1355
- ___block_literal_global.1360
- ___block_literal_global.1365
- ___block_literal_global.1370
- ___block_literal_global.140
- ___block_literal_global.142
- ___block_literal_global.166
- ___block_literal_global.1745
- ___block_literal_global.1777
- ___block_literal_global.1829
- ___block_literal_global.1842
- ___block_literal_global.1855
- ___block_literal_global.1865
- ___block_literal_global.1878
- ___block_literal_global.190
- ___block_literal_global.2011
- ___block_literal_global.2036
- ___block_literal_global.2106
- ___block_literal_global.2119
- ___block_literal_global.219
- ___block_literal_global.241
- ___block_literal_global.265
- ___block_literal_global.268
- ___block_literal_global.271
- ___block_literal_global.276
- ___block_literal_global.308
- ___block_literal_global.311
- ___block_literal_global.313
- ___block_literal_global.315
- ___block_literal_global.318
- ___block_literal_global.320
- ___block_literal_global.327
- ___block_literal_global.366
- ___block_literal_global.400
- ___block_literal_global.403
- ___block_literal_global.407
- ___block_literal_global.415
- ___block_literal_global.418
- ___block_literal_global.432
- ___block_literal_global.435
- ___block_literal_global.451
- ___block_literal_global.454
- ___block_literal_global.461
- ___block_literal_global.468
- ___block_literal_global.479
- ___block_literal_global.76
- ___block_literal_global.850
- ___block_literal_global.879
- _objc_msgSend$initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:puzzlesArchiveAPIBaseURLString:appAnalyticsNotificationReceiptBaseURLString:authTokenAPIBaseURLString:sportsDataVisualizationAPIBaseURLString:fineGrainedNewsletterSubscriptionBaseURLString:appAnalyticsSportsEventsBaseURLString:appAnalyticsAppHealthBaseURLString:ckOrderFeedBaseURLString:ckMultiFetchBaseURLString:ckRecordFetchBaseURLString:ckEdgeCachedOrderFeedBaseURLString:ckEdgeCachedMultiFetchBaseURLString:
CStrings:
+ "; tagSuggestionsConfiguration: %@"
+ "@\"FCNewsTabiTagSuggestionsConfiguration\""
+ "@\"FCNewsTabiTagSuggestionsOutputConfiguration\""
+ "@184@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176"
+ "FCNewsTabiTagSuggestionsConfiguration"
+ "FCNewsTabiTagSuggestionsOutputConfiguration"
+ "T@\"<FCChannelProviding>\",?,R,C,N"
+ "T@\"<FCHeadlineMetadata>\",?,R,C,N"
+ "T@\"<FCHeadlineStocksFields>\",?,R,N"
+ "T@\"<FCHeadlineStocksFields>\",?,R,N,V_stocksFields"
+ "T@\"<FCNewsAppConfiguration>\",?,R,N"
+ "T@\"<FCNewsAppConfiguration><FCJSONEncodableObjectProviding>\",?,R,N"
+ "T@\"<FCNewsAppConfigurationInternal>\",?,R,N"
+ "T@\"COMAPPLEFELDSPARPROTOCOLLIVERPOOLArticleContentExpiration\",?,R,N"
+ "T@\"FCAppReviewRequestConfig\",?,R,N"
+ "T@\"FCArticleAudioTrack\",?,R,N"
+ "T@\"FCArticleAudioTrack\",?,R,N,V_narrativeTrack"
+ "T@\"FCArticleAudioTrack\",?,R,N,V_narrativeTrackSample"
+ "T@\"FCArticleLinkBehaviorConfig\",?,R,N"
+ "T@\"FCArticleModalBrandBarConfig\",?,R,N"
+ "T@\"FCAssetHandle\",?,R,N"
+ "T@\"FCColor\",?,R,N"
+ "T@\"FCColor\",?,R,N,V_thumbnailImageAccentColor"
+ "T@\"FCColor\",?,R,N,V_thumbnailImageBackgroundColor"
+ "T@\"FCColor\",?,R,N,V_thumbnailImagePrimaryColor"
+ "T@\"FCColor\",?,R,N,V_thumbnailImageTextColor"
+ "T@\"FCEmbedProxyConfiguration\",?,R,N"
+ "T@\"FCHeadlineExperimentalTitleMetadata\",?,R,C,N"
+ "T@\"FCHeadlineExperimentalTitleMetadata\",?,R,C,N,V_experimentalTitleMetadata"
+ "T@\"FCHeadlineThumbnailMetadata\",?,R,N"
+ "T@\"FCIssue\",?,R,C,N"
+ "T@\"FCIssue\",?,R,C,N,V_parentIssue"
+ "T@\"FCLaunchPresentationConfig\",?,R,N"
+ "T@\"FCLaunchPresentationConfig\",?,R,N,V_launchPresentationConfig"
+ "T@\"FCLocationSharingUpsellConfig\",?,R,N"
+ "T@\"FCLocationSharingUpsellConfig\",?,R,N,V_locationSharingUpsellConfig"
+ "T@\"FCNewsPersonalizationConfiguration\",?,R,C,N"
+ "T@\"FCNewsPersonalizationConfiguration\",?,R,C,N,V_newsPersonalizationConfiguration"
+ "T@\"FCNewsPlusLabelConfigGroup\",?,R,N"
+ "T@\"FCNewsTabiConfiguration\",?,R,C,N"
+ "T@\"FCNewsTabiConfiguration\",?,R,C,N,V_newsTabiConfiguration"
+ "T@\"FCNewsTabiTagSuggestionsConfiguration\",&,N,V_tagSuggestionsConfiguration"
+ "T@\"FCNewsTabiTagSuggestionsOutputConfiguration\",&,N,V_bundleOutputConfiguration"
+ "T@\"FCNewsTabiTagSuggestionsOutputConfiguration\",&,N,V_nonBundleOutputConfiguration"
+ "T@\"FCPaidBundleConfiguration\",?,R,N"
+ "T@\"FCPaidBundleConfiguration\",?,R,N,V_paidBundleConfig"
+ "T@\"FCPaidBundleViaOfferConfig\",?,R,N"
+ "T@\"FCPaidBundleViaOfferConfig\",?,R,N,V_paidBundleViaOfferConfig"
+ "T@\"FCPersonalizationPublisherDampeningConfig\",?,R,N"
+ "T@\"FCSmarterMessagingConfig\",?,R,N"
+ "T@\"FCSportsFavoritesSyncModalConfig\",?,R,N"
+ "T@\"FCSportsPrivacyConfiguration\",?,R,N"
+ "T@\"FCSportsPrivacyConfiguration\",?,R,N,V_sportsPrivacyConfiguration"
+ "T@\"FCSportsUpsellConfig\",?,R,N"
+ "T@\"FCSportsUpsellConfig\",?,R,N,V_sportsUpsellConfig"
+ "T@\"FCStatelessPersonalizationPublisherFavorability\",?,R,C,N"
+ "T@\"FCTimesOfDayConfiguration\",?,R,C,N"
+ "T@\"FCTimesOfDayConfiguration\",?,R,C,N,V_timesOfDayConfiguration"
+ "T@\"NSArray\",?,R,C,N"
+ "T@\"NSArray\",?,R,C,N,V_iAdCategories"
+ "T@\"NSArray\",?,R,C,N,V_linkedArticleIDs"
+ "T@\"NSArray\",?,R,C,N,V_linkedIssueIDs"
+ "T@\"NSArray\",?,R,C,N,V_narrativeTrackBuddyArticleIDs"
+ "T@\"NSArray\",?,R,N"
+ "T@\"NSArray\",?,R,N,V_tagsExpiration"
+ "T@\"NSData\",?,R,N"
+ "T@\"NSData\",?,R,N,V_backingArticleRecordData"
+ "T@\"NSData\",?,R,N,V_float16FullBodyEncoding"
+ "T@\"NSData\",?,R,N,V_float16TitleEncoding"
+ "T@\"NSDate\",?,R,N"
+ "T@\"NSDictionary\",?,R,C,N"
+ "T@\"NSDictionary\",?,R,C,N,V_superfeedConfigOverrideResourceIDs"
+ "T@\"NSDictionary\",?,R,N"
+ "T@\"NSDictionary\",?,R,N,V_campaignReferralConfigsByID"
+ "T@\"NSDictionary\",?,R,N,V_channelPaywallConfigsByChannelID"
+ "T@\"NSDictionary\",?,R,N,V_channelPickerConfigsByName"
+ "T@\"NSDictionary\",?,R,N,V_channelUpsellConfigsByChannelID"
+ "T@\"NSSet\",?,R"
+ "T@\"NSString\",&,N,V_channelScoresOutputName"
+ "T@\"NSString\",&,N,V_topicIDsOutputName"
+ "T@\"NSString\",&,N,V_topicScoresOutputName"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"NSString\",?,R,C,N,V_clusterID"
+ "T@\"NSString\",?,R,N"
+ "T@\"NSString\",?,R,N,V_blockedArticleLearnMoreURL"
+ "T@\"NSString\",?,R,N,V_layeredThumbnailJSON"
+ "T@\"NSString\",?,R,N,V_mySportsHighlightsTagID"
+ "T@\"NSString\",?,R,N,V_mySportsScoresTagID"
+ "T@\"NSString\",?,R,N,V_narrativeTrackPreferredUpsellVariantID"
+ "T@\"NSString\",?,R,N,V_narrativeTrackTextRanges"
+ "T@\"NSString\",?,R,N,V_sharedWithYouTagID"
+ "T@\"NSString\",?,R,N,V_sportEventHighlightsTagID"
+ "T@\"NSString\",?,R,N,V_sportHighlightsTagID"
+ "T@\"NSString\",?,R,N,V_sportLeagueHighlightsTagID"
+ "T@\"NSString\",?,R,N,V_sportLeagueScoresTagID"
+ "T@\"NSString\",?,R,N,V_sportScoresTagID"
+ "T@\"NSString\",?,R,N,V_sportTeamHighlightsTagID"
+ "T@\"NSString\",?,R,N,V_sportTeamScoresTagID"
+ "T@\"NSString\",R,N,V_appAnalyticsAppHeartbeatBaseURLString"
+ "T@\"NSURL\",?,R,C"
+ "T@\"NSURL\",?,R,N"
+ "TB,?,R,N"
+ "TB,?,R,N,GisArticleToolbarCompressionEnabled"
+ "TB,?,R,N,GisBundlePaid"
+ "TB,?,R,N,GisBundlePaid,V_bundlePaid"
+ "TB,?,R,N,GisIssueOnly"
+ "TB,?,R,N,GisIssueOnly,V_issueOnly"
+ "TB,?,R,N,GisPrivateDataEncryptionRequired"
+ "TB,?,R,N,GisPrivateDataEncryptionRequired,V_privateDataEncryptionRequired"
+ "TB,?,R,N,GshouldProxyURLBucketFetch"
+ "TB,?,R,N,V_disableBookmarking"
+ "TB,?,R,N,V_hasAudioTrack"
+ "TB,?,R,N,V_hideModalCloseButton"
+ "TB,?,R,N,V_isLocalDraft"
+ "TB,?,R,N,V_privateDataShouldSecureSubscriptions"
+ "TB,?,R,N,V_reduceVisibility"
+ "TB,?,R,N,V_reduceVisibilityForNonFollowers"
+ "TB,?,R,N,V_showBundleSoftPaywall"
+ "TB,?,R,N,V_useTransparentNavigationBar"
+ "TB,?,R,N,V_webConverted"
+ "TB,?,R,N,V_webEmbedsEnabled"
+ "TQ,?,R,N"
+ "Td,?,R,N"
+ "Td,?,R,N,V_layeredThumbnailAspectRatio"
+ "Tq,?,R,N"
+ "Tq,?,R,N,V_bodyTextLength"
+ "_appAnalyticsAppHeartbeatBaseURLString"
+ "_channelScoresOutputName"
+ "_tagSuggestionsConfiguration"
+ "_topicIDsOutputName"
+ "_topicScoresOutputName"
+ "accommodatePresentedItemEvictionWithCompletionHandler:"
+ "appAnalyticsAppHeartbeatBaseURLString"
+ "appAnalyticsAppHeartbeatEndpointUrlForEnvironment:"
+ "appHeartbeatEventsEndpointUrl"
+ "audioPlaylistSweepListeningPercentageThreshold"
+ "audioPlaylistSweepRecencyThresholdInDays"
+ "channelScoresOutputName"
+ "contentKeySession:didProvideContentKeyRequests:forInitializationData:"
+ "contentKeySession:externalProtectionStatusDidChangeForContentKey:"
+ "dynamicSupportedContentLanguage"
+ "endpointConfig - environment: %ld, clientAPIURL: %@, notificationsURL: %@, staticAssetURL: %@, remoteDataSourcesURL: %@, newsletterURL: %@, appHeartbeatUrl: %@"
+ "foregroundHeartbeatEventEnabled"
+ "initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:puzzlesArchiveAPIBaseURLString:appAnalyticsNotificationReceiptBaseURLString:authTokenAPIBaseURLString:sportsDataVisualizationAPIBaseURLString:fineGrainedNewsletterSubscriptionBaseURLString:appAnalyticsSportsEventsBaseURLString:appAnalyticsAppHealthBaseURLString:appAnalyticsAppHeartbeatBaseURLString:ckOrderFeedBaseURLString:ckMultiFetchBaseURLString:ckRecordFetchBaseURLString:ckEdgeCachedOrderFeedBaseURLString:ckEdgeCachedMultiFetchBaseURLString:"
+ "news.features.foregroundHeartbeatEventEnabled"
+ "setChannelScoresOutputName:"
+ "setTagSuggestionsConfiguration:"
+ "setTopicIDsOutputName:"
+ "setTopicScoresOutputName:"
+ "tagSuggestionsConfiguration"
+ "topicIDsOutputName"
+ "topicScoresOutputName"
+ "v32@0:8@\"AVContentKeySession\"16@\"AVContentKey\"24"
+ "v40@0:8@\"AVContentKeySession\"16@\"NSArray\"24@\"NSData\"32"
- "\x02\x16"
- "@168@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160"
- "FCResourceUnarchiver"
- "FCResourceUnarchiverErrorDomain"
- "Failed to extract resource %@"
- "Failed to extract resource %@ due to missing on-disk URL."
- "T@\"<FCHeadlineMetadata>\",R,C,N"
- "T@\"<FCHeadlineStocksFields>\",R,N"
- "T@\"<FCHeadlineStocksFields>\",R,N,V_stocksFields"
- "T@\"<FCNewsAppConfiguration><FCJSONEncodableObjectProviding>\",R,N"
- "T@\"<FCNewsAppConfigurationInternal>\",R,N"
- "T@\"COMAPPLEFELDSPARPROTOCOLLIVERPOOLArticleContentExpiration\",R,N"
- "T@\"FCAppReviewRequestConfig\",R,N"
- "T@\"FCArticleAudioTrack\",R,N"
- "T@\"FCArticleAudioTrack\",R,N,V_narrativeTrack"
- "T@\"FCArticleAudioTrack\",R,N,V_narrativeTrackSample"
- "T@\"FCArticleLinkBehaviorConfig\",R,N"
- "T@\"FCArticleModalBrandBarConfig\",R,N"
- "T@\"FCColor\",R,N,V_background_color"
- "T@\"FCColor\",R,N,V_dark_style_background_color"
- "T@\"FCColor\",R,N,V_thumbnailImageAccentColor"
- "T@\"FCColor\",R,N,V_thumbnailImageBackgroundColor"
- "T@\"FCColor\",R,N,V_thumbnailImagePrimaryColor"
- "T@\"FCColor\",R,N,V_thumbnailImageTextColor"
- "T@\"FCEmbedProxyConfiguration\",R,N"
- "T@\"FCHeadlineExperimentalTitleMetadata\",R,C,N"
- "T@\"FCHeadlineExperimentalTitleMetadata\",R,C,N,V_experimentalTitleMetadata"
- "T@\"FCHeadlineThumbnailMetadata\",R,N"
- "T@\"FCIssue\",R,C,N"
- "T@\"FCIssue\",R,C,N,V_parentIssue"
- "T@\"FCLaunchPresentationConfig\",R,N"
- "T@\"FCLaunchPresentationConfig\",R,N,V_launchPresentationConfig"
- "T@\"FCLocationSharingUpsellConfig\",R,N"
- "T@\"FCLocationSharingUpsellConfig\",R,N,V_locationSharingUpsellConfig"
- "T@\"FCNewsPersonalizationConfiguration\",R,C,N"
- "T@\"FCNewsPersonalizationConfiguration\",R,C,N,V_newsPersonalizationConfiguration"
- "T@\"FCNewsPlusLabelConfigGroup\",R,N"
- "T@\"FCNewsTabiConfiguration\",R,C,N"
- "T@\"FCNewsTabiConfiguration\",R,C,N,V_newsTabiConfiguration"
- "T@\"FCPaidBundleConfiguration\",R,N"
- "T@\"FCPaidBundleConfiguration\",R,N,V_paidBundleConfig"
- "T@\"FCPaidBundleViaOfferConfig\",R,N"
- "T@\"FCPaidBundleViaOfferConfig\",R,N,V_paidBundleViaOfferConfig"
- "T@\"FCPersonalizationPublisherDampeningConfig\",R,N"
- "T@\"FCSmarterMessagingConfig\",R,N"
- "T@\"FCSportsFavoritesSyncModalConfig\",R,N"
- "T@\"FCSportsPrivacyConfiguration\",R,N"
- "T@\"FCSportsPrivacyConfiguration\",R,N,V_sportsPrivacyConfiguration"
- "T@\"FCSportsUpsellConfig\",R,N"
- "T@\"FCSportsUpsellConfig\",R,N,V_sportsUpsellConfig"
- "T@\"FCStatelessPersonalizationPublisherFavorability\",R,C,N"
- "T@\"FCTimesOfDayConfiguration\",R,C,N"
- "T@\"FCTimesOfDayConfiguration\",R,C,N,V_timesOfDayConfiguration"
- "T@\"NSArray\",R,C,N,V_linkedArticleIDs"
- "T@\"NSArray\",R,C,N,V_linkedIssueIDs"
- "T@\"NSArray\",R,C,N,V_narrativeTrackBuddyArticleIDs"
- "T@\"NSArray\",R,N,V_tagsExpiration"
- "T@\"NSData\",R,N,V_backingArticleRecordData"
- "T@\"NSData\",R,N,V_float16FullBodyEncoding"
- "T@\"NSData\",R,N,V_float16TitleEncoding"
- "T@\"NSDictionary\",R,C,N,V_superfeedConfigOverrideResourceIDs"
- "T@\"NSDictionary\",R,N,V_campaignReferralConfigsByID"
- "T@\"NSDictionary\",R,N,V_channelPaywallConfigsByChannelID"
- "T@\"NSDictionary\",R,N,V_channelPickerConfigsByName"
- "T@\"NSDictionary\",R,N,V_channelUpsellConfigsByChannelID"
- "T@\"NSSet\",R"
- "T@\"NSString\",R,C,N,V_clusterID"
- "T@\"NSString\",R,N,V_blockedArticleLearnMoreURL"
- "T@\"NSString\",R,N,V_layeredThumbnailJSON"
- "T@\"NSString\",R,N,V_mySportsHighlightsTagID"
- "T@\"NSString\",R,N,V_mySportsScoresTagID"
- "T@\"NSString\",R,N,V_narrativeTrackPreferredUpsellVariantID"
- "T@\"NSString\",R,N,V_narrativeTrackTextRanges"
- "T@\"NSString\",R,N,V_sharedWithYouTagID"
- "T@\"NSString\",R,N,V_sportEventHighlightsTagID"
- "T@\"NSString\",R,N,V_sportHighlightsTagID"
- "T@\"NSString\",R,N,V_sportLeagueHighlightsTagID"
- "T@\"NSString\",R,N,V_sportLeagueScoresTagID"
- "T@\"NSString\",R,N,V_sportScoresTagID"
- "T@\"NSString\",R,N,V_sportTeamHighlightsTagID"
- "T@\"NSString\",R,N,V_sportTeamScoresTagID"
- "TB,R,N,GisArticleToolbarCompressionEnabled"
- "TB,R,N,GisIssueOnly"
- "TB,R,N,GisIssueOnly,V_issueOnly"
- "TB,R,N,GisPrivateDataEncryptionRequired"
- "TB,R,N,GisPrivateDataEncryptionRequired,V_privateDataEncryptionRequired"
- "TB,R,N,GshouldProxyURLBucketFetch"
- "TB,R,N,V_disableBookmarking"
- "TB,R,N,V_hasAudioTrack"
- "TB,R,N,V_hideModalCloseButton"
- "TB,R,N,V_privateDataShouldSecureSubscriptions"
- "TB,R,N,V_reduceVisibility"
- "TB,R,N,V_reduceVisibilityForNonFollowers"
- "TB,R,N,V_showBundleSoftPaywall"
- "TB,R,N,V_useTransparentNavigationBar"
- "TB,R,N,V_webConverted"
- "TB,R,N,V_webEmbedsEnabled"
- "Td,R,N,V_layeredThumbnailAspectRatio"
- "Tq,R,N,V_bodyTextLength"
- "_background_color"
- "_dark_style_background_color"
- "background_color"
- "dark_style_background_color"
- "embedWeb"
- "encountered fatal error %s"
- "endpointConfig - environment: %ld, clientAPIURL: %@, notificationsURL: %@, staticAssetURL: %@, remoteDataSourcesURL: %@, newsletterURL: %@"
- "failed to extract %lu files from zip archive in %.2fs to %{public}@"
- "finished unzipping %lu total files to %{public}@"
- "initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:appAnalyticsNotificationReceiptBaseURLString:authTokenAPIBaseURLString:sportsDataVisualizationAPIBaseURLString:fineGrainedNewsletterSubscriptionBaseURLString:appAnalyticsSportsEventsBaseURLString:appAnalyticsAppHealthBaseURLString:ckOrderFeedBaseURLString:ckMultiFetchBaseURLString:ckRecordFetchBaseURLString:ckEdgeCachedOrderFeedBaseURLString:ckEdgeCachedMultiFetchBaseURLString:"
- "successfully extracted %lu files from zip archive in %.2fs to %{public}@"
- "unarchiveResources:into:error:"

```
