## momentsd

> `/usr/libexec/momentsd`

```diff

-202.0.2.0.0
-  __TEXT.__text: 0x20b360
+202.0.5.0.0
+  __TEXT.__text: 0x20e50c
   __TEXT.__auth_stubs: 0x15c0
-  __TEXT.__objc_stubs: 0x1a240
-  __TEXT.__objc_methlist: 0xe0d8
-  __TEXT.__cstring: 0x20add
-  __TEXT.__objc_classname: 0x1857
-  __TEXT.__objc_methtype: 0x2a94
-  __TEXT.__objc_methname: 0x2bda7
-  __TEXT.__oslogstring: 0x2813f
-  __TEXT.__const: 0xbe0
-  __TEXT.__gcc_except_tab: 0x78d8
+  __TEXT.__objc_stubs: 0x1a3e0
+  __TEXT.__objc_methlist: 0xe180
+  __TEXT.__cstring: 0x20f6d
+  __TEXT.__objc_classname: 0x1856
+  __TEXT.__objc_methtype: 0x2ad3
+  __TEXT.__objc_methname: 0x2c0fd
+  __TEXT.__oslogstring: 0x2843f
+  __TEXT.__const: 0xbf0
+  __TEXT.__gcc_except_tab: 0x78c0
   __TEXT.__ustring: 0xe
   __TEXT.__dlopen_cstrs: 0x51
   __TEXT.__swift5_typeref: 0x150

   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_reflstr: 0x30
-  __TEXT.__unwind_info: 0x4360
+  __TEXT.__unwind_info: 0x43b0
   __TEXT.__eh_frame: 0x388
   __DATA_CONST.__auth_got: 0xaf8
   __DATA_CONST.__got: 0x9b0
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA_CONST.__const: 0x93b8
-  __DATA_CONST.__cfstring: 0x1fb80
+  __DATA_CONST.__const: 0x9578
+  __DATA_CONST.__cfstring: 0x20120
   __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0xe0

   __DATA_CONST.__objc_arraydata: 0x1110
   __DATA_CONST.__objc_arrayobj: 0x828
   __DATA_CONST.__objc_floatobj: 0x280
-  __DATA_CONST.__objc_doubleobj: 0x2f0
+  __DATA_CONST.__objc_doubleobj: 0x310
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x19298
-  __DATA.__objc_selrefs: 0x7b70
-  __DATA.__objc_ivar: 0x12b8
+  __DATA.__objc_const: 0x193c8
+  __DATA.__objc_selrefs: 0x7bd8
+  __DATA.__objc_ivar: 0x12cc
   __DATA.__objc_data: 0x4480
   __DATA.__data: 0x1280
   __DATA.__common: 0xf4
-  __DATA.__bss: 0x1a8
+  __DATA.__bss: 0x1b0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MomentsData.framework/MomentsData
+  - /System/Library/PrivateFrameworks/MomentsIntelligence.framework/MomentsIntelligence
   - /System/Library/PrivateFrameworks/PersonalizationPortrait.framework/PersonalizationPortrait
   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
-  - /System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7013
-  Symbols:   49768
-  CStrings:  13635
+  Functions: 7038
+  Symbols:   50015
+  CStrings:  13714
 
Symbols:
+ __block_literal_global.458
+ _kMOClusteringAnalyticsPersonPhenotypeCount
+ _kMOClusteringAnalyticsUniquePlaceNameCount
+ _kMOClusteringAnalyticsPlaceTypeFromPhotoTraitsPhenotype
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.833
+ -[MOClusterMetadata subSuggestionIDsBeforePruning]
+ __52+[MOPlatformInfo generativeModelsAvailabilityStatus]_block_invoke.cold.1
+ OBJC_IVAR_$_MORoutineServiceManager._airportCategories
+ _kMOEventClusterBundleAnalyticsEvent
+ _kMOClusteringAnalyticsWithCoworkerPhenotype
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.824
+ ___62-[MOPersistenceManager acquireBackgroundProcessingPermissions]_block_invoke
+ __50-[MODaemonClient getMomentsNotificationsSchedule:]_block_invoke.279
+ __82-[MOBundleClusteringManager _getClusterBundleFrom:withEmbeddings:andCreationDate:]_block_invoke.313
+ GCC_except_table181
+ _kMOClusteringAnalyticsUniqueCombinedPlaceTypeCount
+ __block_literal_global.508
+ _objc_msgSend$getSuperTypeEnum:
+ -[MOClusterMetadata setWeekOfYearHistogram:]
+ GCC_except_table175
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e34_v24?0"NSError"8"NSDictionary"16ls72l8s32l8s40l8s48l8s56l8s64l8
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.399
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.825
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.401
+ _kMOClusteringAnalyticsUniqueTopLevelActivityCount
+ ___97-[MODaemonClient softRefreshEventsWithContext:andRefreshVariant:andIgnoreLastTrigger:andHandler:]_block_invoke
+ _kMOClusteringAnalyticsSecondLevelActivityPhenotypeExists
+ _kMOAnomalyAnalyticsOutlierScore
+ _kMOClusteringAnalyticsUniqueContactNamesCount
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.841
+ __82-[MOBundleClusteringManager _getClusterBundleFrom:withEmbeddings:andCreationDate:]_block_invoke.324
+ _kMOClusteringAnalyticsCombinedPlaceTypePhenotype
+ __50-[MOPhotoManager _rehydratePhotoMemories:handler:]_block_invoke.409
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.415.cold.1
+ -[MODaemonClient setPersistenceManager:]
+ __block_literal_global.545
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.416
+ __60-[MODaemonClient _logEngagementEvent:timestamp:withContext:]_block_invoke.465
+ _kMOClusteringAnalyticsUniqueDayOfWeekCount
+ -[MOBundleClusteringManager submitAnomalyBundleInternalAnalytics:withOnboardingStatus:andSubmissionDate:].cold.1
+ __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.540
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.421
+ __75-[MOPhotoManager fetchAndSaveSharedPhotosBetweenStartDate:EndDate:handler:]_block_invoke.403
+ _kMOEventClusterAnomalyAnalyticsEvent
+ ___133-[MOPhotoManager _fetchCuratedPhotosFromHighlights:StartDate:EndDate:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke_2
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.395
+ __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.407
+ __82-[MOBundleClusteringManager _getClusterBundleFrom:withEmbeddings:andCreationDate:]_block_invoke.353
+ __70-[MOPhotoManager _updatePhotoMemoriesDeletedAtSource:library:handler:]_block_invoke.413
+ gmsAvailabilityStatus.onceToken
+ _kMOClusteringAnalyticsUniqueSecondLevelActivityCount
+ OBJC_IVAR_$_MOClusterMetadata._subSuggestionIDsBeforePruning
+ _kMOClusteringAnalyticsActivityTypeFromPhotoTraitsPhenotype
+ +[MOPlatformInfo generativeModelsAvailabilityStatus]
+ _kMOClusteringAnalyticsUniqueTimeTagCount
+ OBJC_IVAR_$_MOClusterMetadata._weekOfYearHistogram
+ _kMOClusteringAnalyticsUniquePlaceTypeFromPhotoTraitsCount
+ OBJC_IVAR_$_MOEventManager.collectQueue
+ _objc_msgSend$softRefreshEventsWithContext:andRefreshVariant:andIgnoreLastTrigger:andHandler:
+ OBJC_IVAR_$_MOPhotoManager._gmsAvailabilityStatus
+ GCC_except_table121
+ GCC_except_table148
+ _objc_msgSend$getDefaultAnalyticsResultWithOnboardingStatus:
+ _objc_msgSend$setWeekOfYearHistogram:
+ __74-[MORoutineServiceManager _fetchVisitsBetweenStartDate:CompletionHandler:]_block_invoke.158.cold.2
+ __84-[MODaemonClient didAppEntryUpdateUsingSuggestions:onEvent:duringInterval:withInfo:]_block_invoke.476
+ _kMOClusteringAnalyticsSubBundleCount
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8s40l8s48l8s56l8s64l8r72l8
+ _objc_msgSend$submitAnomalyBundleInternalAnalytics:withOnboardingStatus:andSubmissionDate:
+ _kMOBundleClusterMetadatasubSuggestionIDsBeforePruning
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.829
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.825.cold.1
+ _objc_msgSend$acquireBackgroundProcessingPermissions
+ __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.300
+ -[MOPhotoManager gmsAvailabilityStatus]
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.837
+ _OBJC_CLASS_$_MOMomentsIntelligenceServiceManager
+ __block_literal_global.467
+ __block_literal_global.327
+ __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.207
+ ___39-[MOPhotoManager gmsAvailabilityStatus]_block_invoke
+ _objc_msgSend$submitClusterBundleInternalAnalytics:withOnboardingStatus:andSubmissionDate:
+ GCC_except_table136
+ __140-[MOEngagementAndSuggestionAnalyticsManager _submitSuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:]_block_invoke.258
+ __68-[MOPhotoManager _updatePhotoEventsDeletedAtSource:library:handler:]_block_invoke.412
+ _objc_msgSend$_processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:
+ _objc_msgSend$weekOfYearHistogram
+ _kMOClusteringAnalyticsUniqueActivityTypeFromPhotoTraitsCount
+ __block_literal_global.506
+ ___97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke
+ _kMOAnomalyAnalyticsIsSignificant
+ _kMOClusteringAnalyticsWithFamilyPhenotype
+ _kMOClusteringAnalyticsUniqueTimeContextFromPhotoTraitsCount
+ _kAnalyticsScalingFactorForfloatValue
+ -[MOClusterMetadata weekOfYearHistogram]
+ _objc_msgSend$sharedInstance
+ ___105-[MOBundleClusteringManager submitAnomalyBundleInternalAnalytics:withOnboardingStatus:andSubmissionDate:]_block_invoke
+ __82-[MOBundleClusteringManager _getClusterBundleFrom:withEmbeddings:andCreationDate:]_block_invoke.352
+ -[MOClusterMetadata setSubSuggestionIDsBeforePruning:]
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.406
+ GCC_except_table178
+ ___block_descriptor_40_e8_32r_e20_v20?0B8"NSError"12lr32l8
+ __82-[MOBundleClusteringManager _getClusterBundleFrom:withEmbeddings:andCreationDate:]_block_invoke.397
+ GCC_except_table19
+ _kMOClusteringAnalyticsEnclosingAreaPhenotypeExists
+ __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.191
+ ___97-[MODaemonClient softRefreshEventsWithContext:andRefreshVariant:andIgnoreLastTrigger:andHandler:]_block_invoke_2
+ _kMOClusteringAnalyticsPhenotypeFieldCount
+ GCC_except_table190
+ __74-[MORoutineServiceManager _fetchVisitsBetweenStartDate:CompletionHandler:]_block_invoke.158.cold.1
+ _kMOClusteringAnalyticsUniquePersonRelationshipCount
+ _kMOClusteringAnalyticsUniqueOtherSubjectFromPhotoTraitsCount
+ __62-[MOEventManager _collectEventsWithRefreshVariant:andHandler:]_block_invoke.188
+ __62-[MOEventManager _collectEventsWithRefreshVariant:andHandler:]_block_invoke.186
+ GCC_except_table171
+ _kMOClusteringAnalyticsPlaceNamePhenotypeExists
+ -[MODaemonClient softRefreshEventsWithContext:andRefreshVariant:andIgnoreLastTrigger:andHandler:]
+ OBJC_IVAR_$_MODaemonClient._persistenceManager
+ -[MOBundleClusteringManager submitClusterBundleInternalAnalytics:withOnboardingStatus:andSubmissionDate:]
+ _objc_msgSend$generativeModelsAvailabilityStatus
+ __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke_2.205
+ -[MOBundleClusteringManager _getClusterBundleFrom:withEmbeddings:andCreationDate:].cold.9
+ -[MOBundleClusteringManager submitAnomalyBundleInternalAnalytics:withOnboardingStatus:andSubmissionDate:]
+ __block_literal_global.336
+ _kMOAnomalyAnalyticsBundleGoodnessScore
+ _kMOBundleClusterMetadataWeekOfYearHistogram
+ GCC_except_table184
+ __71-[MODaemonClient _purgeEventsWithContext:andRefreshVariant:andHandler:]_block_invoke.343
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.390
+ ___52+[MOPlatformInfo generativeModelsAvailabilityStatus]_block_invoke
+ __71-[MODaemonClient _fetchEventBundlesWithOptions:withContext:andHandler:]_block_invoke.319
+ +[MOEventBundle getSuperTypeEnum:]
+ -[MOBundleClusteringManager _countValidKeysInHistogram:]
+ __62-[MOEventManager _collectEventsWithRefreshVariant:andHandler:]_block_invoke.186.cold.1
+ _kMOClusteringAnalyticsDayOfWeekPhenotypeExists
+ __82-[MOBundleClusteringManager _getClusterBundleFrom:withEmbeddings:andCreationDate:]_block_invoke_2.391
+ _kMOClusteringAnalyticsUniqueEnclosingPlaceNameCount
+ _kMOClusteringAnalyticsOtherSubjectFromPhotoTraitsPhenotype
+ _kMOClusteringAnalyticsTopLevelActivityPhenotype
+ _kMOAnomalyAnalyticsScalingFactorForFloatValue
+ __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.407.cold.1
+ _kMOClusteringAnalyticsTimeTagPhenotypeExists
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.405.cold.2
+ -[MOBundleClusteringManager submitClusterBundleInternalAnalytics:withOnboardingStatus:andSubmissionDate:].cold.1
+ __82-[MODaemonClient _analyzeTrendsInEvents:withContext:andRefreshVariant:andHandler:]_block_invoke.359
+ -[MODaemonClient acquireBackgroundProcessingPermissionsForMomentsWithHander:]
+ _objc_msgSend$fetchGenerativeModelsAvailabilityWithReply:
+ GCC_except_table140
+ __block_literal_global.317
+ -[MODaemonClient persistenceManager]
+ _kMOClusteringAnalyticsSubBundleCountBeforePruning
+ __82-[MOBundleClusteringManager _getClusterBundleFrom:withEmbeddings:andCreationDate:]_block_invoke.334
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.411
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.425
+ _kMOTimeContextEmbeddingWeekOfYear
+ -[MOClusterMetadata initWithIdentifier:isFiltered:phenoType:topLevelActivityHistogram:secondLevelActivityHistogram:activityTypeFromPhotoTraitsHistogram:timeTagHistogram:dayOfWeekHistogram:weekOfYearHistogram:timeContextFromPhotoTraitsHistogram:placeNameHistogram:combinedPlaceTypeHistogram:enclosingPlaceNameHistogram:placeTypeFromPhotoTraitsHistogram:contactNamesHistogram:personRelationshipHistogram:socialEventFromPhotoTraitsHistogram:otherSubjectFromPhotoTraitsHistogram:subBundleGoodnessScores:subSuggestionIDsBeforePruning:]
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96r104r_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8s40l8s48l8r96l8s56l8s64l8s72l8s80l8s88l8r104l8
+ __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.240
+ ___block_descriptor_64_e8_32s40s48s56bs_e46_v32?0"NSArray"8"NSError"16"NSDictionary"24ls32l8s56l8s40l8s48l8
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.405.cold.1
+ __140-[MOEngagementAndSuggestionAnalyticsManager _submitSuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:]_block_invoke.256
+ __65-[MODaemonClient _fetchEventsWithOptions:withContext:andHandler:]_block_invoke.296
+ +[MOEngagementAndSuggestionAnalyticsManager getDefaultAnalyticsResultWithOnboardingStatus:]
+ _kMOClusteringAnalyticsWithMyPetPhenotype
+ _objc_msgSend$setSubSuggestionIDsBeforePruning:
+ ___block_descriptor_48_e8_32s40s_e29_v32?0"NSDictionary"8Q16^B24ls32l8s40l8
+ GCC_except_table187
+ _objc_msgSend$initWithIdentifier:isFiltered:phenoType:topLevelActivityHistogram:secondLevelActivityHistogram:activityTypeFromPhotoTraitsHistogram:timeTagHistogram:dayOfWeekHistogram:weekOfYearHistogram:timeContextFromPhotoTraitsHistogram:placeNameHistogram:combinedPlaceTypeHistogram:enclosingPlaceNameHistogram:placeTypeFromPhotoTraitsHistogram:contactNamesHistogram:personRelationshipHistogram:socialEventFromPhotoTraitsHistogram:otherSubjectFromPhotoTraitsHistogram:subBundleGoodnessScores:subSuggestionIDsBeforePruning:
+ _kMOClusteringAnalyticsUniqueWeekOfYearCount
+ -[MOPersistenceManager acquireBackgroundProcessingPermissions]
+ __block_literal_global.469
+ _objc_msgSend$_countValidKeysInHistogram:
+ ___82-[MOBundleClusteringManager _getClusterBundleFrom:withEmbeddings:andCreationDate:]_block_invoke_3
+ GCC_except_table153
+ _kMOClusteringAnalyticsWithChildPhenotype
+ _objc_msgSend$gmsAvailabilityStatus
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.399.cold.1
+ -[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]
+ __74-[MORoutineServiceManager _fetchVisitsBetweenStartDate:CompletionHandler:]_block_invoke.158
+ __block_literal_global.550
+ _kMOClusteringAnalyticsWithFriendPhenotype
+ _kMOClusteringAnalyticsUniqueSocialEventFromPhotoTraitsCount
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8s72l8s48l8s56l8s64l8
+ __53-[MOManageServer listener:shouldAcceptNewConnection:]_block_invoke.221
+ __block_literal_global.223
+ _kMOClusteringAnalyticsTimeContextFromPhotoTraitsPhenotype
+ _kMOClusteringAnalyticsSocialEventFromPhotoTraitsPhenotype
+ _kMOClusteringAnalyticsIsWeekendPhenotype
+ __65-[MODaemonClient _fetchEventsWithOptions:withContext:andHandler:]_block_invoke.291
+ __65-[MODaemonClient scheduleDatabaseUpgradeWithContext:andDelegate:]_block_invoke.242
+ __69-[MOPhotoManager fetchAndSavePhotoMemoriesStartDate:EndDate:handler:]_block_invoke.405
+ _objc_msgSend$subSuggestionIDsBeforePruning
+ __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.303
+ ___105-[MOBundleClusteringManager submitClusterBundleInternalAnalytics:withOnboardingStatus:andSubmissionDate:]_block_invoke
+ __OBJC_$_CLASS_METHODS_MOEngagementAndSuggestionAnalyticsManager
- __82-[MODaemonClient _analyzeTrendsInEvents:withContext:andRefreshVariant:andHandler:]_block_invoke.358
- GCC_except_table174
- __60-[MODaemonClient _logEngagementEvent:timestamp:withContext:]_block_invoke.463
- -[MOPhotoManager meContact]
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.826.cold.1
- __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke_2.204
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.404.cold.1
- GCC_except_table152
- __140-[MOEngagementAndSuggestionAnalyticsManager _submitSuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:]_block_invoke.255
- __50-[MOPhotoManager _rehydratePhotoMemories:handler:]_block_invoke.408
- __65-[MODaemonClient _fetchEventsWithOptions:withContext:andHandler:]_block_invoke.295
- __74-[MORoutineServiceManager _fetchVisitsBetweenStartDate:CompletionHandler:]_block_invoke.157.cold.1
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.404
- ___block_descriptor_88_e8_32s40s48s56s64s72s80r_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8s40l8s48l8s56l8s64l8s72l8r80l8
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.842
- __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.239
- GCC_except_table135
- __block_literal_global.505
- GCC_except_table120
- GCC_except_table139
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.826
- __75-[MOPhotoManager fetchAndSaveSharedPhotosBetweenStartDate:EndDate:handler:]_block_invoke.402
- __71-[MODaemonClient _fetchEventBundlesWithOptions:withContext:andHandler:]_block_invoke.318
- __block_literal_global.507
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.834
- __84-[MODaemonClient didAppEntryUpdateUsingSuggestions:onEvent:duringInterval:withInfo:]_block_invoke.475
- ___block_descriptor_72_e8_32s40s48s56s64bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8s64l8s48l8s56l8
- ___block_descriptor_56_e8_32s40s48bs_e46_v32?0"NSArray"8"NSError"16"NSDictionary"24ls32l8s48l8s40l8
- _OBJC_CLASS_$_PXPeopleUtilities
- __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.539
- __block_literal_global.140
- -[MOPhotoManager setMeContact:]
- __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.406
- __65-[MODaemonClient scheduleDatabaseUpgradeWithContext:andDelegate:]_block_invoke.241
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.400
- GCC_except_table186
- __block_literal_global.457
- GCC_except_table189
- ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s96s104r112r_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8s40l8s48l8s56l8r104l8s64l8s72l8s80l8s88l8s96l8r112l8
- GCC_except_table170
- __50-[MODaemonClient getMomentsNotificationsSchedule:]_block_invoke.278
- GCC_except_table131
- __62-[MOEventManager _collectEventsWithRefreshVariant:andHandler:]_block_invoke.185.cold.1
- __block_literal_global.549
- ___76-[MODaemonClient softRefreshEventsWithContext:andRefreshVariant:andHandler:]_block_invoke_2
- __82-[MOBundleClusteringManager _getClusterBundleFrom:withEmbeddings:andCreationDate:]_block_invoke_2.215
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.404.cold.2
- GCC_except_table177
- __82-[MOBundleClusteringManager _getClusterBundleFrom:withEmbeddings:andCreationDate:]_block_invoke.175
- GCC_except_table99
- __62-[MOEventManager _collectEventsWithRefreshVariant:andHandler:]_block_invoke.187
- __65-[MODaemonClient _fetchEventsWithOptions:withContext:andHandler:]_block_invoke.290
- __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.299
- __133-[MOPhotoManager _fetchCuratedPhotosFromHighlights:StartDate:EndDate:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.354
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.822
- __71-[MODaemonClient _purgeEventsWithContext:andRefreshVariant:andHandler:]_block_invoke.341
- _objc_msgSend$_getDefaultAnalyticsResultWithOnboardingStatus:
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.393
- __62-[MOEventManager _collectEventsWithRefreshVariant:andHandler:]_block_invoke.185
- ___76-[MODaemonClient softRefreshEventsWithContext:andRefreshVariant:andHandler:]_block_invoke
- GCC_except_table71
- __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.301
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.830
- ___block_descriptor_72_e8_32s40s48s56s64bs_e34_v24?0"NSError"8"NSDictionary"16ls64l8s32l8s40l8s48l8s56l8
- __82-[MOBundleClusteringManager _getClusterBundleFrom:withEmbeddings:andCreationDate:]_block_invoke.136
- __block_literal_global.544
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.388
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.398
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.838
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.414
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.414.cold.1
- __69-[MOPhotoManager fetchAndSavePhotoMemoriesStartDate:EndDate:handler:]_block_invoke.404
- _objc_msgSend$fetchMeContact
- __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.206
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.409
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.398.cold.1
- __block_literal_global.468
- -[MOEngagementAndSuggestionAnalyticsManager _getDefaultAnalyticsResultWithOnboardingStatus:]
- GCC_except_table183
- _objc_msgSend$meContact
- -[MOClusterMetadata initWithIdentifier:isFiltered:phenoType:topLevelActivityHistogram:secondLevelActivityHistogram:activityTypeFromPhotoTraitsHistogram:timeTagHistogram:dayOfWeekHistogram:timeContextFromPhotoTraitsHistogram:placeNameHistogram:combinedPlaceTypeHistogram:enclosingPlaceNameHistogram:placeTypeFromPhotoTraitsHistogram:contactNamesHistogram:personRelationshipHistogram:socialEventFromPhotoTraitsHistogram:otherSubjectFromPhotoTraitsHistogram:subBundleGoodnessScores:]
- __68-[MOPhotoManager _updatePhotoEventsDeletedAtSource:library:handler:]_block_invoke.411
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.424
- __74-[MORoutineServiceManager _fetchVisitsBetweenStartDate:CompletionHandler:]_block_invoke.157.cold.2
- GCC_except_table180
- __82-[MOBundleClusteringManager _getClusterBundleFrom:withEmbeddings:andCreationDate:]_block_invoke.213
- __block_literal_global.159
- __82-[MOBundleClusteringManager _getClusterBundleFrom:withEmbeddings:andCreationDate:]_block_invoke.157
- __70-[MOPhotoManager _updatePhotoMemoriesDeletedAtSource:library:handler:]_block_invoke.412
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.419
- __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.189
- __74-[MORoutineServiceManager _fetchVisitsBetweenStartDate:CompletionHandler:]_block_invoke.157
- OBJC_IVAR_$_MOPhotoManager._meContact
- __block_literal_global.150
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.825
- __140-[MOEngagementAndSuggestionAnalyticsManager _submitSuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:]_block_invoke.257
- __block_literal_global.218
- __block_literal_global.470
- __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.406.cold.1
- __82-[MOBundleClusteringManager _getClusterBundleFrom:withEmbeddings:andCreationDate:]_block_invoke.147
- __53-[MOManageServer listener:shouldAcceptNewConnection:]_block_invoke.216
- _objc_msgSend$initWithIdentifier:isFiltered:phenoType:topLevelActivityHistogram:secondLevelActivityHistogram:activityTypeFromPhotoTraitsHistogram:timeTagHistogram:dayOfWeekHistogram:timeContextFromPhotoTraitsHistogram:placeNameHistogram:combinedPlaceTypeHistogram:enclosingPlaceNameHistogram:placeTypeFromPhotoTraitsHistogram:contactNamesHistogram:personRelationshipHistogram:socialEventFromPhotoTraitsHistogram:otherSubjectFromPhotoTraitsHistogram:subBundleGoodnessScores:
CStrings:
+ "com.apple.Moments.MOClusterBundle"
+ "phenotypeFieldCount"
+ "weekOfYearCount"
+ "_weekOfYearHistogram"
+ "withCoworkerPhenotype"
+ "Completed cluster Bundle CoreAnalytics submission."
+ "_subSuggestionIDsBeforePruning"
+ "success"
+ "setWeekOfYearHistogram:"
+ "getDefaultAnalyticsResultWithOnboardingStatus:"
+ "uniqueTopLevelActivityCount"
+ "MOPersonalizedSensingEnabled"
+ "\x0f\b"
+ "socialEventFromPhotoTraitsPhenotype"
+ "TQ,R,V_gmsAvailabilityStatus"
+ "topLevelActivityPhenotype"
+ "initWithIdentifier:isFiltered:phenoType:topLevelActivityHistogram:secondLevelActivityHistogram:activityTypeFromPhotoTraitsHistogram:timeTagHistogram:dayOfWeekHistogram:weekOfYearHistogram:timeContextFromPhotoTraitsHistogram:placeNameHistogram:combinedPlaceTypeHistogram:enclosingPlaceNameHistogram:placeTypeFromPhotoTraitsHistogram:contactNamesHistogram:personRelationshipHistogram:socialEventFromPhotoTraitsHistogram:otherSubjectFromPhotoTraitsHistogram:subBundleGoodnessScores:subSuggestionIDsBeforePruning:"
+ "v44@0:8@\"MOXPCContext\"16Q24B32@?<v@?@\"NSError\">36"
+ "sharedInstance"
+ "subBundleCountBeforePruning"
+ "otherSubjectFromPhotoTraitsPhenotype"
+ "submitClusterBundleInternalAnalytics:withOnboardingStatus:andSubmissionDate:"
+ "fetchPhotosBetweenStartDate, #scenes, startDate, %!@(MISSING), endDate, %!@(MISSING), scenes, %!@(MISSING)"
+ "generativeModelsAvailabilityStatus"
+ "collectQueue"
+ "Cluster bundle CA payload is empty. Skip submission"
+ "timeTagCount"
+ "fail"
+ "Submit internal cluster bundle analytics"
+ "%!@(MISSING), using reconstructed GEOAddressObject value for map item, %!@(MISSING), address, %!@(MISSING)"
+ "contactNamesCount"
+ "personRelationshipCount"
+ "[GenerateClusterAndAnomalyBundles] Completed biome donation for cluster bundles."
+ "weekOfYearHistogram"
+ "activityTypeFromPhotoTraitsCount"
+ "Submitted coreAnalytics payload to %!@(MISSING): %!{(MISSING)private}@"
+ "%!l(MISSING)u anomaly bundles are ready for CoreAnalytics donation"
+ "withFriendPhenotype"
+ "Anomaly bundle CA payload is empty. Skip submission"
+ "withMyPetPhenotype"
+ "placeTypeFromPhotoTraitsPhenotype"
+ "activityTypeFromPhotoTraitsPhenotype"
+ "@172@0:8@16B24@28@36@44@52@60@68@76@84@92@100@108@116@124@132@140@148@156@164"
+ "subBundleCount"
+ "enclosingAreaPhenotypeExists"
+ "socialEventFromPhotoTraitsCount"
+ "withFamilyPhenotype"
+ "uniqueSecondLevelActivityCount"
+ "enclosingPlaceNameCount"
+ "placeTypeFromPhotoTraitsCount"
+ "timeContextFromPhotoTraitsPhenotype"
+ "%!@(MISSING), using routine cached GEOAddressObject value for map item, %!@(MISSING), address, %!@(MISSING)"
+ "fetchGenerativeModelsAvailabilityWithReply:"
+ "combinedPlaceTypePhenotype"
+ "setSubSuggestionIDsBeforePruning:"
+ "v20@?0B8@\"NSError\"12"
+ "gmsAvailabilityStatus,%!l(MISSING)u"
+ "dayOfWeekCount"
+ "otherSubjectFromPhotoTraitsCount"
+ "[GenerateClusterAndAnomalyBundles] No anomaly bundle was detected. Skiping anomaly bundle annotation."
+ "acquireBackgroundProcessingPermissionsForMomentsWithHander:"
+ "placeNameCount"
+ "_countValidKeysInHistogram:"
+ "%!l(MISSING)u cluster bundles are ready for CoreAnalytics donation"
+ "fetchPhotosBetweenStartDate, #scenes, shortlisted assets with uuid %!@(MISSING) and localIdentifier %!@(MISSING) and scenes %!@(MISSING)"
+ "[GenerateClusterAndAnomalyBundles] Start Biome donation for cluster bundles"
+ "\x11\x1d"
+ "personPhenotypeCount"
+ "com.apple.Moments.MOAnomalyBundle"
+ "acquireBackgroundProcessingPermissionsForDB, result, %!@(MISSING)"
+ "placeNamePhenotypeExists"
+ "_gmsAvailabilityStatus"
+ "timeContextFromPhotoTraitsCount"
+ "\x1f\x04"
+ "anomalyIsSignificant"
+ "gmsAvailabilityStatus"
+ "secondLevelActivityPhenotypeExists"
+ "getSuperTypeEnum:"
+ "withChildPhenotype"
+ "_processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:"
+ "subSuggestionIDsBeforePruning"
+ "submitAnomalyBundleInternalAnalytics:withOnboardingStatus:andSubmissionDate:"
+ "timeTagPhenotypeExists"
+ "Completed Anomaly Bundle CoreAnalytics submission."
+ "[GenerateClusterAndAnomalyBundles] Submit internal anomaly bundle analytics"
+ "scalingFactorForFloatValue"
+ "Could not get GMS Availability"
+ "\x01\x17"
+ "T@\"NSDictionary\",&,N,V_weekOfYearHistogram"
+ "softRefreshEventsWithContext:andRefreshVariant:andIgnoreLastTrigger:andHandler:"
+ "T@\"NSArray\",&,N,V_subSuggestionIDsBeforePruning"
+ "isWeekendPhenotype"
+ "v24@0:8@?<v@?B>16"
+ "[GenerateClusterAndAnomalyBundles] Submit internal cluster bundle analytics"
+ "acquireBackgroundProcessingPermissions"
+ "dayOfWeekPhenotypeExists"
+ "SubSuggestionIDs before pruning %!@(MISSING)"
+ "combinedPlaceTypeCount"
- "Current PHPerson matched as the me person from Me Card, settng it as mePerson"
- "@\"CNContact\""
- "\x1f\x02"
- "\x11\x1c"
- "meContact"
- "me contact from me card: %!@(MISSING)"
- "\x0f\a"
- "[GenerateClusterAndAnomalyBundles] No anomaly bundle was detected. Stopping process."
- "T@\"CNContact\",&,N,V_meContact"
- "fetchPhotosBetweenStartDate, #traits, #scenes, startDate, %!@(MISSING), endDate, %!@(MISSING), scenes, %!@(MISSING)"
- "@156@0:8@16B24@28@36@44@52@60@68@76@84@92@100@108@116@124@132@140@148"
- "%!@(MISSING), using routine cached GEOAddressObject value for poi, %!@(MISSING), address, %!@(MISSING)"
- "fetchPhotosBetweenStartDate, #traits, shortlisted assets with uuid %!@(MISSING) and localIdentifier %!@(MISSING) and scenes %!@(MISSING)"
- "_getDefaultAnalyticsResultWithOnboardingStatus:"
- "\x17"
- "_meContact"
- "%!@(MISSING), using reconstructed GEOAddressObject value for poi, %!@(MISSING), address, %!@(MISSING)"
- "fetchMeContact"
- "initWithIdentifier:isFiltered:phenoType:topLevelActivityHistogram:secondLevelActivityHistogram:activityTypeFromPhotoTraitsHistogram:timeTagHistogram:dayOfWeekHistogram:timeContextFromPhotoTraitsHistogram:placeNameHistogram:combinedPlaceTypeHistogram:enclosingPlaceNameHistogram:placeTypeFromPhotoTraitsHistogram:contactNamesHistogram:personRelationshipHistogram:socialEventFromPhotoTraitsHistogram:otherSubjectFromPhotoTraitsHistogram:subBundleGoodnessScores:"
- "setMeContact:"

```
