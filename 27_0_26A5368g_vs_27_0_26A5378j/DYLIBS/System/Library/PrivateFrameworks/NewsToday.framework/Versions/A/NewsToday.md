## NewsToday

> `/System/Library/PrivateFrameworks/NewsToday.framework/Versions/A/NewsToday`

```diff

-  __TEXT.__text: 0x4b64c
-  __TEXT.__objc_methlist: 0x6504
+  __TEXT.__text: 0x4beac
+  __TEXT.__objc_methlist: 0x652c
   __TEXT.__const: 0xd08
-  __TEXT.__oslogstring: 0x16f0
-  __TEXT.__cstring: 0x9655
+  __TEXT.__oslogstring: 0x17e0
+  __TEXT.__cstring: 0x96f5
   __TEXT.__ustring: 0x16
   __TEXT.__gcc_except_tab: 0xa70
   __TEXT.__constg_swiftt: 0x240

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x20
   __TEXT.__swift_as_cont: 0x20
-  __TEXT.__unwind_info: 0xf40
+  __TEXT.__unwind_info: 0xf50
   __TEXT.__eh_frame: 0x900
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x498
+  __DATA_CONST.__const: 0x4b8
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d98
+  __DATA_CONST.__objc_selrefs: 0x3dc8
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x1a0
-  __DATA_CONST.__got: 0xa80
-  __AUTH_CONST.__const: 0x24b8
+  __DATA_CONST.__got: 0xa88
+  __AUTH_CONST.__const: 0x2568
   __AUTH_CONST.__cfstring: 0x1e20
-  __AUTH_CONST.__objc_const: 0xdf20
+  __AUTH_CONST.__objc_const: 0xdf80
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x680
-  __AUTH.__objc_data: 0x4e0
+  __AUTH_CONST.__auth_got: 0x678
+  __AUTH.__objc_data: 0x490
   __AUTH.__data: 0x168
-  __DATA.__objc_ivar: 0x5c4
+  __DATA.__objc_ivar: 0x5cc
   __DATA.__data: 0x13d0
   __DATA.__bss: 0x16a0
-  __DATA_DIRTY.__objc_data: 0x1068
+  __DATA_DIRTY.__objc_data: 0x10b8
   __DATA_DIRTY.__data: 0x78
   __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2091
-  Symbols:   5036
-  CStrings:  1058
+  Functions: 2098
+  Symbols:   5061
+  CStrings:  1063
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[NTForYouSectionFetchDescriptor initWithForYouConfiguration:appConfiguration:topStoriesChannelID:localNewsTagID:localNewsSelectionCriteria:hiddenFeedIDs:allowPaidBundleFeed:mutedTagIDs:purchasedTagIDs:rankedAllSubscribedTagIDs:paidAccessChecker:groupingService:]
+ -[NTForYouSectionFetchDescriptor localNewsSelectionCriteria]
+ -[NTLocalNewsPromotionTransformation initWithLocalNewsTagID:localNewsPromotionIndex:localNewsSelectionCriteria:baseTransformation:]
+ -[NTLocalNewsPromotionTransformation localNewsSelectionCriteria]
+ -[NTNewsTodayResultOperation _assembleQueueDescriptorsWithConfig:allowOnlyWatchEligibleSections:respectsWidgetVisibleSectionsLimit:personalizationTreatment:aggregateStore:appConfiguration:todayData:localNewsSelectionCriteria:completion:]
+ -[NTNewsTodayResultOperation _resolveLocalNewsSelectionCriteriaWithAppConfig:]
+ -[NTQueueConfigSectionQueueDescriptor initWithQueueConfig:appConfiguration:todayData:localNewsSelectionCriteria:inFavoritesOnlyMode:respectsWidgetVisibleSectionsLimit:groupingService:]
+ -[NTSectionConfigSectionDescriptor initWithSectionConfig:appConfiguration:topStoriesChannelID:hiddenFeedIDs:allowPaidBundleFeed:todayData:localNewsSelectionCriteria:supplementalFeedFilterOptions:groupingService:]
+ OBJC_IVAR_$_NTForYouSectionFetchDescriptor._localNewsSelectionCriteria
+ OBJC_IVAR_$_NTLocalNewsPromotionTransformation._localNewsSelectionCriteria
+ _FCURLForLocalNewsSelectionCriteria
+ _OBJC_CLASS_$_FCFeedTransformationLowQualityContentFilter
+ _OBJC_CLASS_$_FCFileCoordinatedLocalNewsSelectionCriteriaDropbox
+ _OBJC_CLASS_$_FCLocalNewsSelectionCriteria
+ __237-[NTNewsTodayResultOperation _assembleQueueDescriptorsWithConfig:allowOnlyWatchEligibleSections:respectsWidgetVisibleSectionsLimit:personalizationTreatment:aggregateStore:appConfiguration:todayData:localNewsSelectionCriteria:completion:]_block_invoke
+ ___184-[NTQueueConfigSectionQueueDescriptor initWithQueueConfig:appConfiguration:todayData:localNewsSelectionCriteria:inFavoritesOnlyMode:respectsWidgetVisibleSectionsLimit:groupingService:]_block_invoke
+ ___237-[NTNewsTodayResultOperation _assembleQueueDescriptorsWithConfig:allowOnlyWatchEligibleSections:respectsWidgetVisibleSectionsLimit:personalizationTreatment:aggregateStore:appConfiguration:todayData:localNewsSelectionCriteria:completion:]_block_invoke
+ ___237-[NTNewsTodayResultOperation _assembleQueueDescriptorsWithConfig:allowOnlyWatchEligibleSections:respectsWidgetVisibleSectionsLimit:personalizationTreatment:aggregateStore:appConfiguration:todayData:localNewsSelectionCriteria:completion:]_block_invoke_2
+ ___237-[NTNewsTodayResultOperation _assembleQueueDescriptorsWithConfig:allowOnlyWatchEligibleSections:respectsWidgetVisibleSectionsLimit:personalizationTreatment:aggregateStore:appConfiguration:todayData:localNewsSelectionCriteria:completion:]_block_invoke_3
+ ___237-[NTNewsTodayResultOperation _assembleQueueDescriptorsWithConfig:allowOnlyWatchEligibleSections:respectsWidgetVisibleSectionsLimit:personalizationTreatment:aggregateStore:appConfiguration:todayData:localNewsSelectionCriteria:completion:]_block_invoke_4
+ ___57-[NTLocalNewsPromotionTransformation transformFeedItems:]_block_invoke_3
+ ___78-[NTNewsTodayResultOperation _resolveLocalNewsSelectionCriteriaWithAppConfig:]_block_invoke
+ ___block_descriptor_32_e24_"NSSet"16?0"NSArray"8l
+ ___block_descriptor_40_e8_32s_e5_B8?0l
+ ___block_descriptor_48_e8_32s40s_e36_B16?0"<NTFeedTransformationItem>"8l
+ ___block_descriptor_65_e8_32s40s48s56s_e66_"NTSectionConfigSectionDescriptor"16?0"NTPBTodaySectionConfig"8l
+ ___block_descriptor_66_e8_32s40s48s56s_e58_"<NTSectionQueueDescriptor>"16?0"NTPBTodayQueueConfig"8l
+ ___block_descriptor_72_e8_32s40s48s56s_e5_B8?0l
+ _objc_msgSend$_assembleQueueDescriptorsWithConfig:allowOnlyWatchEligibleSections:respectsWidgetVisibleSectionsLimit:personalizationTreatment:aggregateStore:appConfiguration:todayData:localNewsSelectionCriteria:completion:
+ _objc_msgSend$_resolveLocalNewsSelectionCriteriaWithAppConfig:
+ _objc_msgSend$deprecatedSportsTopicTagIds
+ _objc_msgSend$descriptionForRejectionReason:item:channelID:
+ _objc_msgSend$initWithForYouConfiguration:appConfiguration:topStoriesChannelID:localNewsTagID:localNewsSelectionCriteria:hiddenFeedIDs:allowPaidBundleFeed:mutedTagIDs:purchasedTagIDs:rankedAllSubscribedTagIDs:paidAccessChecker:groupingService:
+ _objc_msgSend$initWithLocalNewsTagID:localNewsPromotionIndex:localNewsSelectionCriteria:baseTransformation:
+ _objc_msgSend$initWithMinBodyTextLength:forbiddenChannelIDs:tagTimeoutsSeconds:forbiddenSportsTagIDs:maxAgeSecondsByChannelID:topicAllowListByChannelID:allowSportsByChannelID:allowedSportsPublisherIDsByChannelID:
+ _objc_msgSend$initWithQueueConfig:appConfiguration:todayData:localNewsSelectionCriteria:inFavoritesOnlyMode:respectsWidgetVisibleSectionsLimit:groupingService:
+ _objc_msgSend$initWithSectionConfig:appConfiguration:topStoriesChannelID:hiddenFeedIDs:allowPaidBundleFeed:todayData:localNewsSelectionCriteria:supplementalFeedFilterOptions:groupingService:
+ _objc_msgSend$loadSelectionCriteria
+ _objc_msgSend$localInForYouTopicTagAllowList
+ _objc_msgSend$localNewsSelectionCriteria
+ _objc_msgSend$rejectionReasonForItem:channelID:otherClusterIDs:
- -[NTForYouSectionFetchDescriptor initWithForYouConfiguration:appConfiguration:topStoriesChannelID:localNewsTagID:hiddenFeedIDs:allowPaidBundleFeed:mutedTagIDs:purchasedTagIDs:rankedAllSubscribedTagIDs:paidAccessChecker:groupingService:]
- -[NTLocalNewsPromotionTransformation initWithLocalNewsTagID:localNewsPromotionIndex:baseTransformation:]
- -[NTNewsTodayResultOperation _assembleQueueDescriptorsWithConfig:allowOnlyWatchEligibleSections:respectsWidgetVisibleSectionsLimit:personalizationTreatment:aggregateStore:appConfiguration:todayData:completion:]
- -[NTQueueConfigSectionQueueDescriptor initWithQueueConfig:appConfiguration:todayData:inFavoritesOnlyMode:respectsWidgetVisibleSectionsLimit:groupingService:]
- -[NTSectionConfigSectionDescriptor initWithSectionConfig:appConfiguration:topStoriesChannelID:hiddenFeedIDs:allowPaidBundleFeed:todayData:supplementalFeedFilterOptions:groupingService:]
- __210-[NTNewsTodayResultOperation _assembleQueueDescriptorsWithConfig:allowOnlyWatchEligibleSections:respectsWidgetVisibleSectionsLimit:personalizationTreatment:aggregateStore:appConfiguration:todayData:completion:]_block_invoke
- ___157-[NTQueueConfigSectionQueueDescriptor initWithQueueConfig:appConfiguration:todayData:inFavoritesOnlyMode:respectsWidgetVisibleSectionsLimit:groupingService:]_block_invoke
- ___210-[NTNewsTodayResultOperation _assembleQueueDescriptorsWithConfig:allowOnlyWatchEligibleSections:respectsWidgetVisibleSectionsLimit:personalizationTreatment:aggregateStore:appConfiguration:todayData:completion:]_block_invoke
- ___210-[NTNewsTodayResultOperation _assembleQueueDescriptorsWithConfig:allowOnlyWatchEligibleSections:respectsWidgetVisibleSectionsLimit:personalizationTreatment:aggregateStore:appConfiguration:todayData:completion:]_block_invoke_2
- ___210-[NTNewsTodayResultOperation _assembleQueueDescriptorsWithConfig:allowOnlyWatchEligibleSections:respectsWidgetVisibleSectionsLimit:personalizationTreatment:aggregateStore:appConfiguration:todayData:completion:]_block_invoke_3
- ___210-[NTNewsTodayResultOperation _assembleQueueDescriptorsWithConfig:allowOnlyWatchEligibleSections:respectsWidgetVisibleSectionsLimit:personalizationTreatment:aggregateStore:appConfiguration:todayData:completion:]_block_invoke_4
- ___block_descriptor_57_e8_32s40s48s_e66_"NTSectionConfigSectionDescriptor"16?0"NTPBTodaySectionConfig"8l
- ___block_descriptor_58_e8_32s40s48s_e58_"<NTSectionQueueDescriptor>"16?0"NTPBTodayQueueConfig"8l
- _objc_msgSend$_assembleQueueDescriptorsWithConfig:allowOnlyWatchEligibleSections:respectsWidgetVisibleSectionsLimit:personalizationTreatment:aggregateStore:appConfiguration:todayData:completion:
- _objc_msgSend$initWithForYouConfiguration:appConfiguration:topStoriesChannelID:localNewsTagID:hiddenFeedIDs:allowPaidBundleFeed:mutedTagIDs:purchasedTagIDs:rankedAllSubscribedTagIDs:paidAccessChecker:groupingService:
- _objc_msgSend$initWithLocalNewsTagID:localNewsPromotionIndex:baseTransformation:
- _objc_msgSend$initWithQueueConfig:appConfiguration:todayData:inFavoritesOnlyMode:respectsWidgetVisibleSectionsLimit:groupingService:
- _objc_msgSend$initWithSectionConfig:appConfiguration:topStoriesChannelID:hiddenFeedIDs:allowPaidBundleFeed:todayData:supplementalFeedFilterOptions:groupingService:
- _swift_willThrowTypedImpl
CStrings:
+ "-[NTForYouSectionFetchDescriptor initWithForYouConfiguration:appConfiguration:topStoriesChannelID:localNewsTagID:localNewsSelectionCriteria:hiddenFeedIDs:allowPaidBundleFeed:mutedTagIDs:purchasedTagIDs:rankedAllSubscribedTagIDs:paidAccessChecker:groupingService:]"
+ "-[NTLocalNewsPromotionTransformation initWithLocalNewsTagID:localNewsPromotionIndex:localNewsSelectionCriteria:baseTransformation:]"
+ "-[NTNewsTodayResultOperation _assembleQueueDescriptorsWithConfig:allowOnlyWatchEligibleSections:respectsWidgetVisibleSectionsLimit:personalizationTreatment:aggregateStore:appConfiguration:todayData:localNewsSelectionCriteria:completion:]"
+ "-[NTQueueConfigSectionQueueDescriptor initWithQueueConfig:appConfiguration:todayData:localNewsSelectionCriteria:inFavoritesOnlyMode:respectsWidgetVisibleSectionsLimit:groupingService:]"
+ "-[NTSectionConfigSectionDescriptor initWithSectionConfig:appConfiguration:topStoriesChannelID:hiddenFeedIDs:allowPaidBundleFeed:todayData:localNewsSelectionCriteria:supplementalFeedFilterOptions:groupingService:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Classes/FRRingBuffer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Extensions/FeldsparToday/NTPBTodayPersonalizationEvent+FTAdditions.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTArticleIDsSectionFetchDescriptor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTArticleListSectionFetchDescriptor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTCatchUpOperation.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTCatchUpOperationRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTFeedTransformationFeedItem.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTFeedTransformationHeadlineItem.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTFeedTransformationIncrementalPersonalizedDiversifiedLimit.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTFeedTransformationUtilities.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTForYouRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTForYouSectionFetchDescriptor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTHeadline.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTHeadlinePersonalizationMetadata.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTItemsSectionFetchDescriptor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTLocalNewsPromotionTransformation.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTNewsModuleDescriptorsOperation.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTNewsSourceAvailabilityEntry.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTNewsTodayResultOperation.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTNewsTodayResultsContentFillAggregator.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTNewsTodayResultsExplicitAllocationAggregator.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTNewsTodayResultsSourceFetchHelper.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTNewsTodayResultsSourceUtilities.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTNoContentModuleDescriptorsOperation.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTNoContentTodayResultOperation.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTPBTodaySectionConfig+NTAdditions.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTPersonalizedSectionFetchDescriptor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTPersonalizedSectionTransformations.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTQueueConfigSectionQueueDescriptor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTSectionConfigSectionDescriptor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTSectionFeedFilterTransformation.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTSectionPlaceholderDescriptor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTSourceAvailabilityManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTStabilizingTransformation.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTagSectionFetchDescriptor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTodayConfig+Mastering.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTodayConfigConversionOperation.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTodayConfigOperation.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTodayContext.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTodayHeadlineProtoitem.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTodayHeadlineProtoitemUtilities.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTodayItemOperation.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTodayPrivateData.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTodayResults.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTodayResultsSource.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5YbEgK/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTWidgetConfigDataOperation.m"
+ "@\"NSSet\"16@?0@\"NSArray\"8"
+ "B8@?0"
+ "allowing local news candidate %{public}@ because we have no selection criteria"
+ "rejecting local news candidate %{public}@ because it has no feed transformation item"
+ "rejecting local news candidate %{public}@ for reason: %{public}@"
+ "returning For You without regard for local news because we could not find any eligible articles for the local news channel"
- "-[NTForYouSectionFetchDescriptor initWithForYouConfiguration:appConfiguration:topStoriesChannelID:localNewsTagID:hiddenFeedIDs:allowPaidBundleFeed:mutedTagIDs:purchasedTagIDs:rankedAllSubscribedTagIDs:paidAccessChecker:groupingService:]"
- "-[NTLocalNewsPromotionTransformation initWithLocalNewsTagID:localNewsPromotionIndex:baseTransformation:]"
- "-[NTNewsTodayResultOperation _assembleQueueDescriptorsWithConfig:allowOnlyWatchEligibleSections:respectsWidgetVisibleSectionsLimit:personalizationTreatment:aggregateStore:appConfiguration:todayData:completion:]"
- "-[NTQueueConfigSectionQueueDescriptor initWithQueueConfig:appConfiguration:todayData:inFavoritesOnlyMode:respectsWidgetVisibleSectionsLimit:groupingService:]"
- "-[NTSectionConfigSectionDescriptor initWithSectionConfig:appConfiguration:topStoriesChannelID:hiddenFeedIDs:allowPaidBundleFeed:todayData:supplementalFeedFilterOptions:groupingService:]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Classes/FRRingBuffer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Extensions/FeldsparToday/NTPBTodayPersonalizationEvent+FTAdditions.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTArticleIDsSectionFetchDescriptor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTArticleListSectionFetchDescriptor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTCatchUpOperation.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTCatchUpOperationRequest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTFeedTransformationFeedItem.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTFeedTransformationHeadlineItem.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTFeedTransformationIncrementalPersonalizedDiversifiedLimit.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTFeedTransformationUtilities.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTForYouRequest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTForYouSectionFetchDescriptor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTHeadline.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTHeadlinePersonalizationMetadata.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTItemsSectionFetchDescriptor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTLocalNewsPromotionTransformation.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTNewsModuleDescriptorsOperation.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTNewsSourceAvailabilityEntry.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTNewsTodayResultOperation.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTNewsTodayResultsContentFillAggregator.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTNewsTodayResultsExplicitAllocationAggregator.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTNewsTodayResultsSourceFetchHelper.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTNewsTodayResultsSourceUtilities.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTNoContentModuleDescriptorsOperation.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTNoContentTodayResultOperation.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTPBTodaySectionConfig+NTAdditions.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTPersonalizedSectionFetchDescriptor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTPersonalizedSectionTransformations.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTQueueConfigSectionQueueDescriptor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTSectionConfigSectionDescriptor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTSectionFeedFilterTransformation.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTSectionPlaceholderDescriptor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTSourceAvailabilityManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTStabilizingTransformation.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTagSectionFetchDescriptor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTodayConfig+Mastering.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTodayConfigConversionOperation.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTodayConfigOperation.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTodayContext.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTodayHeadlineProtoitem.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTodayHeadlineProtoitemUtilities.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTodayItemOperation.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTodayPrivateData.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTodayResults.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTTodayResultsSource.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CDJECh/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsToday/NTWidgetConfigDataOperation.m"
- "returning For You without regard for local news because we could not find any articles for the local news channel"

```
