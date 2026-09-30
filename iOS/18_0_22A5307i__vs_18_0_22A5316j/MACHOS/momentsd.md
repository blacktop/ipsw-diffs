## momentsd

> `/usr/libexec/momentsd`

```diff

-185.0.0.0.0
-  __TEXT.__text: 0x1ffeec
-  __TEXT.__auth_stubs: 0x15b0
-  __TEXT.__objc_stubs: 0x19dc0
-  __TEXT.__objc_methlist: 0xde10
-  __TEXT.__cstring: 0x200cd
-  __TEXT.__objc_classname: 0x17e9
-  __TEXT.__objc_methtype: 0x2a1d
-  __TEXT.__objc_methname: 0x2b3e0
-  __TEXT.__oslogstring: 0x26b1f
-  __TEXT.__const: 0xbb0
-  __TEXT.__gcc_except_tab: 0x73b8
+191.0.0.0.0
+  __TEXT.__text: 0x20a6bc
+  __TEXT.__auth_stubs: 0x15c0
+  __TEXT.__objc_stubs: 0x1a220
+  __TEXT.__objc_methlist: 0xe0d0
+  __TEXT.__cstring: 0x20afd
+  __TEXT.__objc_classname: 0x1857
+  __TEXT.__objc_methtype: 0x2a94
+  __TEXT.__objc_methname: 0x2bd89
+  __TEXT.__oslogstring: 0x27f8f
+  __TEXT.__const: 0xbc0
+  __TEXT.__gcc_except_tab: 0x7804
   __TEXT.__ustring: 0xe
   __TEXT.__dlopen_cstrs: 0x51
   __TEXT.__swift5_typeref: 0x14c

   __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_reflstr: 0x30
   __TEXT.__info_plist: 0x471
-  __TEXT.__unwind_info: 0x41d0
+  __TEXT.__unwind_info: 0x4338
   __TEXT.__eh_frame: 0x388
-  __DATA_CONST.__auth_got: 0xaf0
-  __DATA_CONST.__got: 0x9b0
+  __DATA_CONST.__auth_got: 0xaf8
+  __DATA_CONST.__got: 0x9c0
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA_CONST.__const: 0x8e30
-  __DATA_CONST.__cfstring: 0x1f180
-  __DATA_CONST.__objc_classlist: 0x688
+  __DATA_CONST.__const: 0x92f0
+  __DATA_CONST.__cfstring: 0x1fb20
+  __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x538
-  __DATA_CONST.__objc_intobj: 0x2d18
-  __DATA_CONST.__objc_arraydata: 0xce0
-  __DATA_CONST.__objc_arrayobj: 0x570
-  __DATA_CONST.__objc_floatobj: 0x270
+  __DATA_CONST.__objc_superrefs: 0x540
+  __DATA_CONST.__objc_intobj: 0x3840
+  __DATA_CONST.__objc_arraydata: 0x1110
+  __DATA_CONST.__objc_arrayobj: 0x828
+  __DATA_CONST.__objc_floatobj: 0x280
   __DATA_CONST.__objc_doubleobj: 0x2f0
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x18e08
-  __DATA.__objc_selrefs: 0x79f8
-  __DATA.__objc_ivar: 0x127c
-  __DATA.__objc_data: 0x4390
-  __DATA.__data: 0x1268
-  __DATA.__common: 0xec
+  __DATA.__objc_const: 0x19298
+  __DATA.__objc_selrefs: 0x7b68
+  __DATA.__objc_ivar: 0x12b8
+  __DATA.__objc_data: 0x4480
+  __DATA.__data: 0x1280
+  __DATA.__common: 0xf4
   __DATA.__bss: 0x1a8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6875
-  Symbols:   48803
-  CStrings:  13388
+  Functions: 7000
+  Symbols:   49668
+  CStrings:  13623
 
Symbols:
+ +[MOEngagementAndSuggestionAnalyticsParams aggregationWindowMap]
+ +[MOEngagementAndSuggestionAnalyticsParams aggregationWindowMap]
+ +[MOEngagementAndSuggestionAnalyticsParams bundleSubTypeToAnalyticsSuggestionTypeMap]
+ +[MOEngagementAndSuggestionAnalyticsParams bundleSubTypeToAnalyticsSuggestionTypeMap]
+ +[MOEngagementAndSuggestionAnalyticsParams getCharacterCountBin:]
+ +[MOEngagementAndSuggestionAnalyticsParams getCharacterCountBin:]
+ +[MOEngagementAndSuggestionAnalyticsParams suggestionUIVisibilityCategoryToMOEventBundleVisibilityCategoryForUIMap]
+ +[MOEngagementAndSuggestionAnalyticsParams suggestionUIVisibilityCategoryToMOEventBundleVisibilityCategoryForUIMap]
+ +[MOEngagementAndSuggestionAnalyticsParams updateOnboardingStatusDictionaryKeys:]
+ +[MOEngagementAndSuggestionAnalyticsParams updateOnboardingStatusDictionaryKeys:]
+ +[MOEventBundleStore _isResourceTypeAllowedForResource:]
+ +[MOEventBundleStore _isResourceTypeAllowedForResource:]
+ +[MOEventBundleStore _recordDedupeKey:alreadySeenKeys:]
+ +[MOEventBundleStore _recordDedupeKey:alreadySeenKeys:]
+ +[MOEventBundleStore _recordDedupeKey:alreadySeenKeys:].cold.1
+ +[MOEventBundleStore _recordDedupeKey:alreadySeenKeys:].cold.1
+ +[MOEventBundleStore _recordResource:alreadySeenKeys:]
+ +[MOEventBundleStore _recordResource:alreadySeenKeys:]
+ +[MOEventBundleStore _recordResource:alreadySeenKeys:].cold.1
+ +[MOEventBundleStore _recordResource:alreadySeenKeys:].cold.1
+ +[MOEventBundleStore _recordResource:alreadySeenKeys:].cold.2
+ +[MOEventBundleStore _recordResource:alreadySeenKeys:].cold.2
+ +[MOPersonalizedSensingUtils _shouldRemoveBundle:checkVisibilityCategoryForUI:]
+ +[MOPersonalizedSensingUtils _shouldRemoveBundle:checkVisibilityCategoryForUI:]
+ +[MOPersonalizedSensingUtils getPersonalizedSensingAllowedBundles:allowVisits:]
+ +[MOPersonalizedSensingUtils getPersonalizedSensingAllowedBundles:allowVisits:]
+ +[MOPersonalizedSensingUtils getPersonalizedSensingAllowedBundles:allowVisits:].cold.1
+ +[MOPersonalizedSensingUtils getPersonalizedSensingAllowedBundles:allowVisits:].cold.1
+ +[MOPersonalizedSensingUtils getPersonalizedSensingAllowedBundles:allowVisits:].cold.2
+ +[MOPersonalizedSensingUtils getPersonalizedSensingAllowedBundles:allowVisits:].cold.2
+ +[MOResource getDedupeKeyForResourceData:type:error:]
+ +[MOResource getDedupeKeyForResourceData:type:error:]
+ +[MOResource getDedupeKeyForResourceData:type:error:].cold.1
+ +[MOResource getDedupeKeyForResourceData:type:error:].cold.1
+ +[MOResource getDedupeKeyForResourceData:type:error:].cold.2
+ +[MOResource getDedupeKeyForResourceData:type:error:].cold.2
+ +[MOResource getDedupeKeyForResourceData:type:error:].cold.3
+ +[MOResource getDedupeKeyForResourceData:type:error:].cold.3
+ +[MOResource getDedupeKeyForResourceData:type:error:].cold.4
+ +[MOResource getDedupeKeyForResourceData:type:error:].cold.4
+ +[MOResource getDictionaryForData:error:]
+ +[MOResource getDictionaryForData:error:]
+ +[MOResource getDictionaryForData:error:].cold.1
+ +[MOResource getDictionaryForData:error:].cold.1
+ -[MOEngagementAndSuggestionAnalyticsManager .cxx_destruct]
+ -[MOEngagementAndSuggestionAnalyticsManager .cxx_destruct]
+ -[MOEngagementAndSuggestionAnalyticsManager _getDefaultAnalyticsResultWithOnboardingStatus:]
+ -[MOEngagementAndSuggestionAnalyticsManager _getDefaultAnalyticsResultWithOnboardingStatus:]
+ -[MOEngagementAndSuggestionAnalyticsManager _submitSuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:]
+ -[MOEngagementAndSuggestionAnalyticsManager _submitSuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:]
+ -[MOEngagementAndSuggestionAnalyticsManager configurationManager]
+ -[MOEngagementAndSuggestionAnalyticsManager configurationManager]
+ -[MOEngagementAndSuggestionAnalyticsManager defaultsManager]
+ -[MOEngagementAndSuggestionAnalyticsManager defaultsManager]
+ -[MOEngagementAndSuggestionAnalyticsManager engagementHistoryManager]
+ -[MOEngagementAndSuggestionAnalyticsManager engagementHistoryManager]
+ -[MOEngagementAndSuggestionAnalyticsManager eventBundleStore]
+ -[MOEngagementAndSuggestionAnalyticsManager eventBundleStore]
+ -[MOEngagementAndSuggestionAnalyticsManager initWithUniverse:]
+ -[MOEngagementAndSuggestionAnalyticsManager initWithUniverse:]
+ -[MOEngagementAndSuggestionAnalyticsManager isReadyToSubmitAnalytics]
+ -[MOEngagementAndSuggestionAnalyticsManager isReadyToSubmitAnalytics]
+ -[MOEngagementAndSuggestionAnalyticsManager isReadyToSubmitAnalytics].cold.1
+ -[MOEngagementAndSuggestionAnalyticsManager isReadyToSubmitAnalytics].cold.1
+ -[MOEngagementAndSuggestionAnalyticsManager lastAnalyticsSubmissionDate]
+ -[MOEngagementAndSuggestionAnalyticsManager lastAnalyticsSubmissionDate]
+ -[MOEngagementAndSuggestionAnalyticsManager minimumTimeGapBetweenSubmissionsInDays]
+ -[MOEngagementAndSuggestionAnalyticsManager minimumTimeGapBetweenSubmissionsInDays]
+ -[MOEngagementAndSuggestionAnalyticsManager setConfigurationManager:]
+ -[MOEngagementAndSuggestionAnalyticsManager setConfigurationManager:]
+ -[MOEngagementAndSuggestionAnalyticsManager setDefaultsManager:]
+ -[MOEngagementAndSuggestionAnalyticsManager setDefaultsManager:]
+ -[MOEngagementAndSuggestionAnalyticsManager setEngagementHistoryManager:]
+ -[MOEngagementAndSuggestionAnalyticsManager setEngagementHistoryManager:]
+ -[MOEngagementAndSuggestionAnalyticsManager setEventBundleStore:]
+ -[MOEngagementAndSuggestionAnalyticsManager setEventBundleStore:]
+ -[MOEngagementAndSuggestionAnalyticsManager setLastAnalyticsSubmissionDate]
+ -[MOEngagementAndSuggestionAnalyticsManager setLastAnalyticsSubmissionDate]
+ -[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]
+ -[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]
+ -[MOEngagementAndSuggestionAnalyticsManager submitEngagementAndSuggestionPerformanceAnalyticsWithOnboardingStatus:AndCompletionHandler:]
+ -[MOEngagementAndSuggestionAnalyticsManager submitEngagementAndSuggestionPerformanceAnalyticsWithOnboardingStatus:AndCompletionHandler:]
+ -[MOEngagementAndSuggestionAnalyticsManager submitSuggestionPerformanceAnalyticsWithOnboardingStatus:AndCompletionHandler:]
+ -[MOEngagementAndSuggestionAnalyticsManager submitSuggestionPerformanceAnalyticsWithOnboardingStatus:AndCompletionHandler:]
+ -[MOEngagementHistoryManager fetchAppEntryEngagementEventsFromStartDate:toEndDate:withError:]
+ -[MOEngagementHistoryManager fetchAppEntryEngagementEventsFromStartDate:toEndDate:withError:]
+ -[MOEngagementHistoryManager fetchAppEntryEngagementEventsWithTypes:fromStartDate:toEndDate:withError:]
+ -[MOEngagementHistoryManager fetchAppEntryEngagementEventsWithTypes:fromStartDate:toEndDate:withError:]
+ -[MOEngagementHistoryManager fetchSuggestionEngagementEventsFromStartDate:toEndDate:withError:]
+ -[MOEngagementHistoryManager fetchSuggestionEngagementEventsFromStartDate:toEndDate:withError:]
+ -[MOEngagementHistoryManager fetchSuggestionEngagementEventsWithTypes:fromStartDate:toEndDate:withError:]
+ -[MOEngagementHistoryManager fetchSuggestionEngagementEventsWithTypes:fromStartDate:toEndDate:withError:]
+ -[MOEngagementHistoryManager isInternalBuild]
+ -[MOEngagementHistoryManager isInternalBuild]
+ -[MOEngagementHistoryManager submitSuggestionEngagementEventAnalytics:suggestionEngagementType:timestamp:withContext:withTrialExperimentIDs:].cold.1
+ -[MOEngagementHistoryManager submitSuggestionEngagementEventAnalytics:suggestionEngagementType:timestamp:withContext:withTrialExperimentIDs:].cold.1
+ -[MOEngagementHistoryManager suggestionEngagementTypesEligibleForRawExternalAnalytics]
+ -[MOEngagementHistoryManager suggestionEngagementTypesEligibleForRawExternalAnalytics]
+ -[MOEventBundle _allResourcesImpl]
+ -[MOEventBundle _allResourcesImpl]
+ -[MOEventBundle withResourcesUsingBlock:]
+ -[MOEventBundle withResourcesUsingBlock:]
+ -[MOEventBundleFetchOptions personalizedSensingFilter]
+ -[MOEventBundleFetchOptions personalizedSensingFilter]
+ -[MOEventBundleFetchOptions personalizedSensingVisitsAllowed]
+ -[MOEventBundleFetchOptions personalizedSensingVisitsAllowed]
+ -[MOEventBundleFetchOptions setPersonalizedSensingFilter:]
+ -[MOEventBundleFetchOptions setPersonalizedSensingFilter:]
+ -[MOEventBundleFetchOptions setPersonalizedSensingVisitsAllowed:]
+ -[MOEventBundleFetchOptions setPersonalizedSensingVisitsAllowed:]
+ -[MOEventBundleFetchOptions setSkipLocalization:]
+ -[MOEventBundleFetchOptions setSkipLocalization:]
+ -[MOEventBundleFetchOptions skipLocalization]
+ -[MOEventBundleFetchOptions skipLocalization]
+ -[MOEventBundleManager engagementAndSuggestionAnalyticsManager]
+ -[MOEventBundleManager engagementAndSuggestionAnalyticsManager]
+ -[MOEventBundleManager setEngagementAndSuggestionAnalyticsManager:]
+ -[MOEventBundleManager setEngagementAndSuggestionAnalyticsManager:]
+ -[MOEventBundleManager submitEventBundleInternalAnalytics:withSubmissionDate:withRefreshVariant:]
+ -[MOEventBundleManager submitEventBundleInternalAnalytics:withSubmissionDate:withRefreshVariant:]
+ -[MOEventBundleManager submitEventBundleInternalAnalytics:withSubmissionDate:withRefreshVariant:].cold.1
+ -[MOEventBundleManager submitEventBundleInternalAnalytics:withSubmissionDate:withRefreshVariant:].cold.1
+ -[MOEventBundleRanking isInternalBuild]
+ -[MOEventBundleRanking isInternalBuild]
+ -[MOEventBundleStore _updateLongTermBundles:context:].cold.1
+ -[MOEventBundleStore _updateLongTermBundles:context:].cold.1
+ -[MOEventBundleStore _updateLongTermBundles:context:].cold.2
+ -[MOEventBundleStore _updateLongTermBundles:context:].cold.2
+ -[MOEventBundleStore _updateLongTermBundles:context:].cold.3
+ -[MOEventBundleStore _updateLongTermBundles:context:].cold.3
+ -[MOEventBundleStore _updateLongTermBundles:context:].cold.4
+ -[MOEventBundleStore _updateLongTermBundles:context:].cold.4
+ -[MOEventBundleStore _updateLongTermBundles:context:].cold.5
+ -[MOEventBundleStore _updateLongTermBundles:context:].cold.5
+ -[MOEventBundleStore _updateLongTermBundles:context:].cold.6
+ -[MOEventBundleStore _updateLongTermBundles:context:].cold.6
+ -[MOEventBundleStore reset]
+ -[MOEventBundleStore reset]
+ -[MOEventWorkout isIndoors]
+ -[MOEventWorkout isIndoors]
+ -[MOEventWorkout setIsIndoors:]
+ -[MOEventWorkout setIsIndoors:]
+ -[MOPhotoManager mePerson]
+ -[MOPhotoManager mePerson]
+ -[MOPhotoManager setMePerson:]
+ -[MOPhotoManager setMePerson:]
+ -[MOResource getDedupeKeyError:]
+ -[MOResource getDedupeKeyError:]
+ -[MOResourceMO(CoreDataProperties) getDedupeKeyError:]
+ -[MOResourceMO(CoreDataProperties) getDedupeKeyError:]
+ -[MOSummarizationManager supressCoarseGranularityPropertyOfEventBundles:primaryBundles:bundleMapping:]
+ -[MOSummarizationManager supressCoarseGranularityPropertyOfEventBundles:primaryBundles:bundleMapping:]
+ /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/momentsd.build/Objects-normal/arm64e/MOEngagementAndSuggestionAnalyticsManager.o
+ /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/momentsd.build/Objects-normal/arm64e/MOEngagementAndSuggestionAnalyticsParams.o
+ /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/momentsd.build/Objects-normal/arm64e/MOPersonalizedSensingUtils.o
+ GCC_except_table100
+ GCC_except_table106
+ GCC_except_table126
+ GCC_except_table16
+ GCC_except_table36
+ GCC_except_table36
+ GCC_except_table36
+ GCC_except_table38
+ GCC_except_table92
+ GCC_except_table96
+ MOEngagementAndSuggestionAnalyticsManager.m
+ MOEngagementAndSuggestionAnalyticsParams.m
+ MOPersonalizedSensingUtils.m
+ OBJC_IVAR_$_MOEngagementAndSuggestionAnalyticsManager._configurationManager
+ OBJC_IVAR_$_MOEngagementAndSuggestionAnalyticsManager._defaultsManager
+ OBJC_IVAR_$_MOEngagementAndSuggestionAnalyticsManager._engagementHistoryManager
+ OBJC_IVAR_$_MOEngagementAndSuggestionAnalyticsManager._eventBundleStore
+ OBJC_IVAR_$_MOEngagementAndSuggestionAnalyticsManager._lastAnalyticsSubmissionDate
+ OBJC_IVAR_$_MOEngagementAndSuggestionAnalyticsManager._minimumTimeGapBetweenSubmissionsInDays
+ OBJC_IVAR_$_MOEngagementHistoryManager._isInternalBuild
+ OBJC_IVAR_$_MOEngagementHistoryManager._suggestionEngagementTypesEligibleForRawExternalAnalytics
+ OBJC_IVAR_$_MOEventBundleFetchOptions._personalizedSensingFilter
+ OBJC_IVAR_$_MOEventBundleFetchOptions._personalizedSensingVisitsAllowed
+ OBJC_IVAR_$_MOEventBundleFetchOptions._skipLocalization
+ OBJC_IVAR_$_MOEventBundleManager._engagementAndSuggestionAnalyticsManager
+ OBJC_IVAR_$_MOEventBundleRanking._isInternalBuild
+ OBJC_IVAR_$_MOEventWorkout._isIndoors
+ OBJC_IVAR_$_MOPhotoManager._mePerson
+ _HKMetadataKeyIndoorWorkout
+ _MOLogFacilityPersonalizedSensing
+ _MOLogFacilityPersonalizedSensing
+ _MOWorkoutMetaDataKeyIsIndoors
+ _MOWorkoutMetaDataKeyIsIndoors
+ _OBJC_CLASS_$_MOEngagementAndSuggestionAnalyticsManager
+ _OBJC_CLASS_$_MOEngagementAndSuggestionAnalyticsManager
+ _OBJC_CLASS_$_MOEngagementAndSuggestionAnalyticsParams
+ _OBJC_CLASS_$_MOEngagementAndSuggestionAnalyticsParams
+ _OBJC_CLASS_$_MOPersonalizedSensingUtils
+ _OBJC_CLASS_$_MOPersonalizedSensingUtils
+ _OBJC_CLASS_$_NSBatchDeleteRequest
+ _OBJC_METACLASS_$_MOEngagementAndSuggestionAnalyticsManager
+ _OBJC_METACLASS_$_MOEngagementAndSuggestionAnalyticsManager
+ _OBJC_METACLASS_$_MOEngagementAndSuggestionAnalyticsParams
+ _OBJC_METACLASS_$_MOEngagementAndSuggestionAnalyticsParams
+ _OBJC_METACLASS_$_MOPersonalizedSensingUtils
+ _OBJC_METACLASS_$_MOPersonalizedSensingUtils
+ __101-[MONotificationsManager _getNewTargetTimeToWriteEventBundlesUsingAppSchedule:withCompletionHandler:]_block_invoke.700
+ __101-[MONotificationsManager _getNewTargetTimeToWriteEventBundlesUsingAppSchedule:withCompletionHandler:]_block_invoke.700
+ __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.608
+ __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.608
+ __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.608.cold.1
+ __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.608.cold.1
+ __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.609
+ __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.609
+ __102-[MOSummarizationManager supressCoarseGranularityPropertyOfEventBundles:primaryBundles:bundleMapping:]_block_invoke_2.cold.1
+ __102-[MOSummarizationManager supressCoarseGranularityPropertyOfEventBundles:primaryBundles:bundleMapping:]_block_invoke_2.cold.1
+ __102-[MOSummarizationManager supressCoarseGranularityPropertyOfEventBundles:primaryBundles:bundleMapping:]_block_invoke_2.cold.2
+ __102-[MOSummarizationManager supressCoarseGranularityPropertyOfEventBundles:primaryBundles:bundleMapping:]_block_invoke_2.cold.2
+ __103-[MOEngagementHistoryManager fetchAppEntryEngagementEventsWithTypes:fromStartDate:toEndDate:withError:]_block_invoke.452
+ __103-[MOEngagementHistoryManager fetchAppEntryEngagementEventsWithTypes:fromStartDate:toEndDate:withError:]_block_invoke.452
+ __103-[MOEngagementHistoryManager fetchAppEntryEngagementEventsWithTypes:fromStartDate:toEndDate:withError:]_block_invoke_2.cold.1
+ __103-[MOEngagementHistoryManager fetchAppEntryEngagementEventsWithTypes:fromStartDate:toEndDate:withError:]_block_invoke_2.cold.1
+ __105-[MOEngagementHistoryManager fetchSuggestionEngagementEventsWithTypes:fromStartDate:toEndDate:withError:]_block_invoke.451
+ __105-[MOEngagementHistoryManager fetchSuggestionEngagementEventsWithTypes:fromStartDate:toEndDate:withError:]_block_invoke.451
+ __105-[MOEngagementHistoryManager fetchSuggestionEngagementEventsWithTypes:fromStartDate:toEndDate:withError:]_block_invoke_2.cold.1
+ __105-[MOEngagementHistoryManager fetchSuggestionEngagementEventsWithTypes:fromStartDate:toEndDate:withError:]_block_invoke_2.cold.1
+ __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.190
+ __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.190
+ __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.207
+ __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.207
+ __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.240
+ __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.240
+ __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke_2.205
+ __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke_2.205
+ __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.571
+ __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.571
+ __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.577
+ __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.577
+ __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.577.cold.1
+ __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.577.cold.1
+ __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.578
+ __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.578
+ __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.579
+ __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.579
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1174
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1174
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176.cold.1
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176.cold.1
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.797
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.797
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.804
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.804
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.801
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.801
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.805
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.805
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.805.cold.1
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.805.cold.1
+ __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.417
+ __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.417
+ __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.420
+ __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.420
+ __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_2.418
+ __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_2.418
+ __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_3.419
+ __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_3.419
+ __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.403
+ __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.403
+ __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.409
+ __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.409
+ __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_2.405
+ __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_2.405
+ __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_3.407
+ __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_3.407
+ __125-[MONotificationsManager _postTimeToWriteSystemNotificationUsingEventBundles:withTrigger:usingAppSchedule:completionHandler:]_block_invoke.769
+ __125-[MONotificationsManager _postTimeToWriteSystemNotificationUsingEventBundles:withTrigger:usingAppSchedule:completionHandler:]_block_invoke.769
+ __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.299
+ __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.299
+ __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.302
+ __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.302
+ __136-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAndSuggestionPerformanceAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.115
+ __136-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAndSuggestionPerformanceAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.115
+ __140-[MOEngagementAndSuggestionAnalyticsManager _submitSuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:]_block_invoke.256
+ __140-[MOEngagementAndSuggestionAnalyticsManager _submitSuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:]_block_invoke.256
+ __140-[MOEngagementAndSuggestionAnalyticsManager _submitSuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:]_block_invoke.258
+ __140-[MOEngagementAndSuggestionAnalyticsManager _submitSuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:]_block_invoke.258
+ __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.430
+ __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.430
+ __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.433
+ __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.433
+ __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_2.431
+ __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_2.431
+ __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_3.432
+ __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_3.432
+ __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.423
+ __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.423
+ __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.426
+ __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.426
+ __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_2.424
+ __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_2.424
+ __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_3.425
+ __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_3.425
+ __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.539
+ __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.539
+ __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.708
+ __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.708
+ __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.708.cold.1
+ __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.708.cold.1
+ __59-[MOEventBundleStore updateEventBundles:CompletionHandler:]_block_invoke.297
+ __59-[MOEventBundleStore updateEventBundles:CompletionHandler:]_block_invoke.297
+ __59-[MOEventBundleStore updateEventBundles:CompletionHandler:]_block_invoke.298
+ __59-[MOEventBundleStore updateEventBundles:CompletionHandler:]_block_invoke.298
+ __59-[MOEventBundleStore updateEventBundles:CompletionHandler:]_block_invoke.299
+ __59-[MOEventBundleStore updateEventBundles:CompletionHandler:]_block_invoke.299
+ __60-[MODaemonClient _logEngagementEvent:timestamp:withContext:]_block_invoke.464
+ __60-[MODaemonClient _logEngagementEvent:timestamp:withContext:]_block_invoke.464
+ __62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke.937
+ __62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke.937
+ __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.636
+ __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.636
+ __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.646
+ __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.646
+ __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.661
+ __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.661
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.623
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.623
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.631
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.631
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke_2.634
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke_2.634
+ __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.320
+ __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.320
+ __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.322
+ __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.322
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.384
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.384
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.407
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.407
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.414
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.414
+ __68-[MOEventBundleStore fetchEventBundleWithOptions:CompletionHandler:]_block_invoke.269
+ __68-[MOEventBundleStore fetchEventBundleWithOptions:CompletionHandler:]_block_invoke.269
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.821
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.821
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.825
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.825
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.826
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.826
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.826.cold.1
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.826.cold.1
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.830
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.830
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.834
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.834
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.838
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.838
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.842
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.842
+ __69-[MONotificationsManager serviceSuggestionsNotificationsWithHandler:]_block_invoke.613
+ __69-[MONotificationsManager serviceSuggestionsNotificationsWithHandler:]_block_invoke.613
+ __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.475
+ __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.475
+ __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.480
+ __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.480
+ __71-[MODaemonClient _fetchEventBundlesWithOptions:withContext:andHandler:]_block_invoke.318
+ __71-[MODaemonClient _fetchEventBundlesWithOptions:withContext:andHandler:]_block_invoke.318
+ __71-[MODaemonClient _purgeEventsWithContext:andRefreshVariant:andHandler:]_block_invoke.342
+ __71-[MODaemonClient _purgeEventsWithContext:andRefreshVariant:andHandler:]_block_invoke.342
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.347
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.347
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.348
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.348
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.352
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.352
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.356
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.356
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.689
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.689
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.689.cold.1
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.689.cold.1
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.690
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.690
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.690.cold.1
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.690.cold.1
+ __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.704
+ __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.704
+ __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.704.cold.1
+ __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.704.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.739
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.739
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.739.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.739.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.750
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.750
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.750.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.750.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.751
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.751
+ __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.308
+ __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.308
+ __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.310
+ __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.310
+ __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.316
+ __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.316
+ __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.316.cold.1
+ __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.316.cold.1
+ __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke.438
+ __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke.438
+ __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke.444
+ __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke.444
+ __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke_2.439
+ __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke_2.439
+ __79+[MOPersonalizedSensingUtils getPersonalizedSensingAllowedBundles:allowVisits:]_block_invoke.117
+ __79+[MOPersonalizedSensingUtils getPersonalizedSensingAllowedBundles:allowVisits:]_block_invoke.117
+ __79+[MOPersonalizedSensingUtils getPersonalizedSensingAllowedBundles:allowVisits:]_block_invoke.117.cold.1
+ __79+[MOPersonalizedSensingUtils getPersonalizedSensingAllowedBundles:allowVisits:]_block_invoke.117.cold.1
+ __79+[MOPersonalizedSensingUtils getPersonalizedSensingAllowedBundles:allowVisits:]_block_invoke.117.cold.2
+ __79+[MOPersonalizedSensingUtils getPersonalizedSensingAllowedBundles:allowVisits:]_block_invoke.117.cold.2
+ __79+[MOPersonalizedSensingUtils getPersonalizedSensingAllowedBundles:allowVisits:]_block_invoke.117.cold.3
+ __79+[MOPersonalizedSensingUtils getPersonalizedSensingAllowedBundles:allowVisits:]_block_invoke.117.cold.3
+ __81-[MOEventBundleManager fetchRehydratedEventBundlesWithOptions:CompletionHandler:]_block_invoke.694
+ __81-[MOEventBundleManager fetchRehydratedEventBundlesWithOptions:CompletionHandler:]_block_invoke.694
+ __82-[MOBiomeManager fetchMomentsEventDataBetweenStartDate:EndDate:CompletionHandler:]_block_invoke_2.631
+ __82-[MOBiomeManager fetchMomentsEventDataBetweenStartDate:EndDate:CompletionHandler:]_block_invoke_2.631
+ __82-[MODaemonClient _analyzeTrendsInEvents:withContext:andRefreshVariant:andHandler:]_block_invoke.358
+ __82-[MODaemonClient _analyzeTrendsInEvents:withContext:andRefreshVariant:andHandler:]_block_invoke.358
+ __84-[MODaemonClient didAppEntryUpdateUsingSuggestions:onEvent:duringInterval:withInfo:]_block_invoke.475
+ __84-[MODaemonClient didAppEntryUpdateUsingSuggestions:onEvent:duringInterval:withInfo:]_block_invoke.475
+ __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.335
+ __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.335
+ __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.336
+ __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.336
+ __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.343
+ __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.343
+ __85-[MOSummarizationManager _aggregateEventBundles:withAggregtaionDateInterval:handler:]_block_invoke.416
+ __85-[MOSummarizationManager _aggregateEventBundles:withAggregtaionDateInterval:handler:]_block_invoke.416
+ __85-[MOSummarizationManager _aggregateEventBundles:withAggregtaionDateInterval:handler:]_block_invoke_2.418
+ __85-[MOSummarizationManager _aggregateEventBundles:withAggregtaionDateInterval:handler:]_block_invoke_2.418
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1120
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1120
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1126
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1126
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1127
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1127
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1131
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1131
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.389
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.389
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.394
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.394
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.398
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.398
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.398.cold.1
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.398.cold.1
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.400
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.400
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.404.cold.1
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.404.cold.1
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.404.cold.2
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.404.cold.2
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.405
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.405
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.410
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.410
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.414.cold.1
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.414.cold.1
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.415
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.415
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.420
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.420
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.424
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.424
+ __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.637
+ __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.637
+ __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.637.cold.1
+ __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.637.cold.1
+ __93-[MOEngagementHistoryManager fetchAppEntryEngagementEventsFromStartDate:toEndDate:withError:]_block_invoke.450
+ __93-[MOEngagementHistoryManager fetchAppEntryEngagementEventsFromStartDate:toEndDate:withError:]_block_invoke.450
+ __93-[MOEngagementHistoryManager fetchAppEntryEngagementEventsFromStartDate:toEndDate:withError:]_block_invoke_2.cold.1
+ __93-[MOEngagementHistoryManager fetchAppEntryEngagementEventsFromStartDate:toEndDate:withError:]_block_invoke_2.cold.1
+ __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1162
+ __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1162
+ __95-[MOEngagementHistoryManager fetchSuggestionEngagementEventsFromStartDate:toEndDate:withError:]_block_invoke.449
+ __95-[MOEngagementHistoryManager fetchSuggestionEngagementEventsFromStartDate:toEndDate:withError:]_block_invoke.449
+ __95-[MOEngagementHistoryManager fetchSuggestionEngagementEventsFromStartDate:toEndDate:withError:]_block_invoke_2.cold.1
+ __95-[MOEngagementHistoryManager fetchSuggestionEngagementEventsFromStartDate:toEndDate:withError:]_block_invoke_2.cold.1
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.429
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.429
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.430
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.430
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.437
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.437
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.445
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.445
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.449
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.449
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.453
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.453
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.457
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.457
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.503
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.503
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.508
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.508
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.513
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.513
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.518
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.518
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.523
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.523
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.528
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.528
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.533
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.533
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.538
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.538
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.543
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.543
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.548
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.548
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.553
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.553
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.558
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.558
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.563
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.563
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.568
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.568
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.570
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.570
+ __OBJC_$_CLASS_METHODS_MOEngagementAndSuggestionAnalyticsParams
+ __OBJC_$_CLASS_METHODS_MOEventBundleStore
+ __OBJC_$_CLASS_METHODS_MOPersonalizedSensingUtils
+ __OBJC_$_INSTANCE_METHODS_MOEngagementAndSuggestionAnalyticsManager
+ __OBJC_$_INSTANCE_VARIABLES_MOEngagementAndSuggestionAnalyticsManager
+ __OBJC_$_INSTANCE_VARIABLES_MOEngagementAndSuggestionAnalyticsManager
+ __OBJC_$_PROP_LIST_MOEngagementAndSuggestionAnalyticsManager
+ __OBJC_$_PROP_LIST_MOEngagementAndSuggestionAnalyticsManager
+ __OBJC_CLASS_RO_$_MOEngagementAndSuggestionAnalyticsManager
+ __OBJC_CLASS_RO_$_MOEngagementAndSuggestionAnalyticsManager
+ __OBJC_CLASS_RO_$_MOEngagementAndSuggestionAnalyticsParams
+ __OBJC_CLASS_RO_$_MOEngagementAndSuggestionAnalyticsParams
+ __OBJC_CLASS_RO_$_MOPersonalizedSensingUtils
+ __OBJC_CLASS_RO_$_MOPersonalizedSensingUtils
+ __OBJC_METACLASS_RO_$_MOEngagementAndSuggestionAnalyticsManager
+ __OBJC_METACLASS_RO_$_MOEngagementAndSuggestionAnalyticsManager
+ __OBJC_METACLASS_RO_$_MOEngagementAndSuggestionAnalyticsParams
+ __OBJC_METACLASS_RO_$_MOEngagementAndSuggestionAnalyticsParams
+ __OBJC_METACLASS_RO_$_MOPersonalizedSensingUtils
+ __OBJC_METACLASS_RO_$_MOPersonalizedSensingUtils
+ ___102-[MOSummarizationManager supressCoarseGranularityPropertyOfEventBundles:primaryBundles:bundleMapping:]_block_invoke
+ ___102-[MOSummarizationManager supressCoarseGranularityPropertyOfEventBundles:primaryBundles:bundleMapping:]_block_invoke
+ ___102-[MOSummarizationManager supressCoarseGranularityPropertyOfEventBundles:primaryBundles:bundleMapping:]_block_invoke_2
+ ___102-[MOSummarizationManager supressCoarseGranularityPropertyOfEventBundles:primaryBundles:bundleMapping:]_block_invoke_2
+ ___103-[MOEngagementHistoryManager fetchAppEntryEngagementEventsWithTypes:fromStartDate:toEndDate:withError:]_block_invoke
+ ___103-[MOEngagementHistoryManager fetchAppEntryEngagementEventsWithTypes:fromStartDate:toEndDate:withError:]_block_invoke
+ ___103-[MOEngagementHistoryManager fetchAppEntryEngagementEventsWithTypes:fromStartDate:toEndDate:withError:]_block_invoke_2
+ ___103-[MOEngagementHistoryManager fetchAppEntryEngagementEventsWithTypes:fromStartDate:toEndDate:withError:]_block_invoke_2
+ ___105-[MOEngagementHistoryManager fetchSuggestionEngagementEventsWithTypes:fromStartDate:toEndDate:withError:]_block_invoke
+ ___105-[MOEngagementHistoryManager fetchSuggestionEngagementEventsWithTypes:fromStartDate:toEndDate:withError:]_block_invoke
+ ___105-[MOEngagementHistoryManager fetchSuggestionEngagementEventsWithTypes:fromStartDate:toEndDate:withError:]_block_invoke_2
+ ___105-[MOEngagementHistoryManager fetchSuggestionEngagementEventsWithTypes:fromStartDate:toEndDate:withError:]_block_invoke_2
+ ___112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke
+ ___112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke
+ ___112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke_2
+ ___112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke_2
+ ___123-[MOEngagementAndSuggestionAnalyticsManager submitSuggestionPerformanceAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke
+ ___123-[MOEngagementAndSuggestionAnalyticsManager submitSuggestionPerformanceAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke
+ ___136-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAndSuggestionPerformanceAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke
+ ___136-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAndSuggestionPerformanceAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke
+ ___140-[MOEngagementAndSuggestionAnalyticsManager _submitSuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:]_block_invoke
+ ___140-[MOEngagementAndSuggestionAnalyticsManager _submitSuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:]_block_invoke
+ ___27-[MOEventBundleStore reset]_block_invoke
+ ___27-[MOEventBundleStore reset]_block_invoke
+ ___34-[MOEventBundle _allResourcesImpl]_block_invoke
+ ___34-[MOEventBundle _allResourcesImpl]_block_invoke
+ ___41-[MOEventBundle withResourcesUsingBlock:]_block_invoke
+ ___41-[MOEventBundle withResourcesUsingBlock:]_block_invoke
+ ___62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke_4
+ ___62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke_4
+ ___65-[MOEventBundleRanking _fillDistincnessInfoForRanking:forBundle:]_block_invoke
+ ___65-[MOEventBundleRanking _fillDistincnessInfoForRanking:forBundle:]_block_invoke
+ ___79+[MOPersonalizedSensingUtils getPersonalizedSensingAllowedBundles:allowVisits:]_block_invoke
+ ___79+[MOPersonalizedSensingUtils getPersonalizedSensingAllowedBundles:allowVisits:]_block_invoke
+ ___81+[MOEngagementAndSuggestionAnalyticsParams updateOnboardingStatusDictionaryKeys:]_block_invoke
+ ___81+[MOEngagementAndSuggestionAnalyticsParams updateOnboardingStatusDictionaryKeys:]_block_invoke
+ ___93-[MOEngagementHistoryManager fetchAppEntryEngagementEventsFromStartDate:toEndDate:withError:]_block_invoke
+ ___93-[MOEngagementHistoryManager fetchAppEntryEngagementEventsFromStartDate:toEndDate:withError:]_block_invoke
+ ___93-[MOEngagementHistoryManager fetchAppEntryEngagementEventsFromStartDate:toEndDate:withError:]_block_invoke_2
+ ___93-[MOEngagementHistoryManager fetchAppEntryEngagementEventsFromStartDate:toEndDate:withError:]_block_invoke_2
+ ___95-[MOEngagementHistoryManager fetchSuggestionEngagementEventsFromStartDate:toEndDate:withError:]_block_invoke
+ ___95-[MOEngagementHistoryManager fetchSuggestionEngagementEventsFromStartDate:toEndDate:withError:]_block_invoke
+ ___95-[MOEngagementHistoryManager fetchSuggestionEngagementEventsFromStartDate:toEndDate:withError:]_block_invoke_2
+ ___95-[MOEngagementHistoryManager fetchSuggestionEngagementEventsFromStartDate:toEndDate:withError:]_block_invoke_2
+ ___97-[MOEventBundleManager submitEventBundleInternalAnalytics:withSubmissionDate:withRefreshVariant:]_block_invoke
+ ___97-[MOEventBundleManager submitEventBundleInternalAnalytics:withSubmissionDate:withRefreshVariant:]_block_invoke
+ ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s96s104r112r_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8s40l8s48l8s56l8r104l8s64l8s72l8s80l8s88l8s96l8r112l8
+ ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s96s104r112r_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8s40l8s48l8s56l8r104l8s64l8s72l8s80l8s88l8s96l8r112l8
+ ___block_descriptor_32_e32_v16?0"NSManagedObjectContext"8l
+ ___block_descriptor_32_e32_v16?0"NSManagedObjectContext"8l
+ ___block_descriptor_40_e8_32r_e23_v16?0"BPSCompletion"8lr32l8
+ ___block_descriptor_40_e8_32r_e23_v16?0"BPSCompletion"8lr32l8
+ ___block_descriptor_40_e8_32r_e24_v24?0"MOResource"8^B16lr32l8
+ ___block_descriptor_40_e8_32r_e24_v24?0"MOResource"8^B16lr32l8
+ ___block_descriptor_40_e8_32s_e24_v24?0"MOResource"8^B16ls32l8
+ ___block_descriptor_40_e8_32s_e24_v24?0"MOResource"8^B16ls32l8
+ ___block_descriptor_40_e8_32s_e35_B24?0"NSString"8"NSDictionary"16ls32l8
+ ___block_descriptor_40_e8_32s_e35_B24?0"NSString"8"NSDictionary"16ls32l8
+ ___block_descriptor_48_e8_32bs40r_e27_v32?0"MOResource"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32bs40r_e27_v32?0"MOResource"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e15_v32?0816^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e15_v32?0816^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e22_B16?0"BMStoreEvent"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e22_B16?0"BMStoreEvent"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e39_B24?0"NSDictionary"8"NSDictionary"16ls32l8
+ ___block_descriptor_48_e8_32s_e39_B24?0"NSDictionary"8"NSDictionary"16ls32l8
+ ___block_descriptor_48_e8_32s_e40_B24?0"MOEventBundle"8"NSDictionary"16ls32l8
+ ___block_descriptor_48_e8_32s_e40_B24?0"MOEventBundle"8"NSDictionary"16ls32l8
+ ___block_descriptor_56_e8_32bs40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32bs40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e23_v16?0"BPSCompletion"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e23_v16?0"BPSCompletion"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48r_e41_v24?0"MOEventBundle"8"MOEventBundle"16ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e41_v24?0"MOEventBundle"8"MOEventBundle"16ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e24_v24?0"MOResource"8^B16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e24_v24?0"MOResource"8^B16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8s56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8s56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8s56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8s56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8s56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8s56l8s40l8s48l8
+ ___block_descriptor_73_e8_32s40s48s56s_e30_v32?0"MOEventBundle"8Q16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_73_e8_32s40s48s56s_e30_v32?0"MOEventBundle"8Q16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32r40r48r56r64r72r_e29_v32?0"NSDictionary"8Q16^B24lr32l8r40l8r48l8r56l8r64l8r72l8
+ ___block_descriptor_88_e8_32r40r48r56r64r72r_e29_v32?0"NSDictionary"8Q16^B24lr32l8r40l8r48l8r56l8r64l8r72l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e46_v32?0"NSArray"8"NSError"16"NSDictionary"24ls32l8s40l8s48l8s56l8s72l8r80l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e46_v32?0"NSArray"8"NSError"16"NSDictionary"24ls32l8s40l8s48l8s56l8s72l8r80l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80r_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8s40l8s48l8s56l8s64l8s72l8r80l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80r_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8s40l8s48l8s56l8s64l8s72l8r80l8
+ __block_literal_global.315
+ __block_literal_global.315
+ __block_literal_global.350
+ __block_literal_global.350
+ __block_literal_global.352
+ __block_literal_global.352
+ __block_literal_global.369
+ __block_literal_global.369
+ __block_literal_global.401
+ __block_literal_global.401
+ __block_literal_global.416
+ __block_literal_global.416
+ __block_literal_global.422
+ __block_literal_global.422
+ __block_literal_global.426
+ __block_literal_global.426
+ __block_literal_global.428
+ __block_literal_global.428
+ __block_literal_global.430
+ __block_literal_global.430
+ __block_literal_global.432
+ __block_literal_global.432
+ __block_literal_global.443
+ __block_literal_global.443
+ __block_literal_global.451
+ __block_literal_global.451
+ __block_literal_global.457
+ __block_literal_global.457
+ __block_literal_global.466
+ __block_literal_global.466
+ __block_literal_global.468
+ __block_literal_global.468
+ __block_literal_global.470
+ __block_literal_global.470
+ __block_literal_global.505
+ __block_literal_global.505
+ __block_literal_global.507
+ __block_literal_global.507
+ __block_literal_global.544
+ __block_literal_global.544
+ __block_literal_global.549
+ __block_literal_global.549
+ __block_literal_global.626
+ __block_literal_global.626
+ __block_literal_global.633
+ __block_literal_global.633
+ __block_literal_global.636
+ __block_literal_global.636
+ __block_literal_global.653
+ __block_literal_global.653
+ __block_literal_global.693
+ __block_literal_global.693
+ __block_literal_global.757
+ __block_literal_global.757
+ __block_literal_global.762
+ __block_literal_global.762
+ __block_literal_global.764
+ __block_literal_global.764
+ __os_feature_enabled_impl
+ _kEventResourcePatternWorkoutIsIndoors
+ _kEventResourcePatternWorkoutIsIndoors
+ _kMOEngagementAndSuggestionAnalyticsParams_aggregationWindowKey
+ _kMOEngagementAndSuggestionAnalyticsParams_aggregationWindowKey
+ _kMOEngagementAndSuggestionAnalyticsParams_appTypeKey
+ _kMOEngagementAndSuggestionAnalyticsParams_appTypeKey
+ _kMOEngagementAndSuggestionAnalyticsParams_avgAgeofSensedSuggestionsInDaysKey
+ _kMOEngagementAndSuggestionAnalyticsParams_avgAgeofSensedSuggestionsInDaysKey
+ _kMOEngagementAndSuggestionAnalyticsParams_isActivitySettingsSwitchEnabledKey
+ _kMOEngagementAndSuggestionAnalyticsParams_isActivitySettingsSwitchEnabledKey
+ _kMOEngagementAndSuggestionAnalyticsParams_isBroadSystemLocationSettingsSwitchEnabledKey
+ _kMOEngagementAndSuggestionAnalyticsParams_isBroadSystemLocationSettingsSwitchEnabledKey
+ _kMOEngagementAndSuggestionAnalyticsParams_isCommunicationSettingsSwitchEnabledKey
+ _kMOEngagementAndSuggestionAnalyticsParams_isCommunicationSettingsSwitchEnabledKey
+ _kMOEngagementAndSuggestionAnalyticsParams_isMediaSettingsSwitchEnabledKey
+ _kMOEngagementAndSuggestionAnalyticsParams_isMediaSettingsSwitchEnabledKey
+ _kMOEngagementAndSuggestionAnalyticsParams_isNearbyPeopleSettingsSwitchEnabledKey
+ _kMOEngagementAndSuggestionAnalyticsParams_isNearbyPeopleSettingsSwitchEnabledKey
+ _kMOEngagementAndSuggestionAnalyticsParams_isPhotoSettingsSwitchEnabledKey
+ _kMOEngagementAndSuggestionAnalyticsParams_isPhotoSettingsSwitchEnabledKey
+ _kMOEngagementAndSuggestionAnalyticsParams_isReflectionSettingsSwitchEnabledKey
+ _kMOEngagementAndSuggestionAnalyticsParams_isReflectionSettingsSwitchEnabledKey
+ _kMOEngagementAndSuggestionAnalyticsParams_isSignificantLocationSettingsSwitchEnabledKey
+ _kMOEngagementAndSuggestionAnalyticsParams_isSignificantLocationSettingsSwitchEnabledKey
+ _kMOEngagementAndSuggestionAnalyticsParams_isStateOfMindSettingsSwitchEnabledKey
+ _kMOEngagementAndSuggestionAnalyticsParams_isStateOfMindSettingsSwitchEnabledKey
+ _kMOEngagementAndSuggestionAnalyticsParams_journalEntryAvgAssetCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_journalEntryAvgAssetCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_journalEntryAvgCharacterCountBinnedKey
+ _kMOEngagementAndSuggestionAnalyticsParams_journalEntryAvgCharacterCountBinnedKey
+ _kMOEngagementAndSuggestionAnalyticsParams_journalEntryCancelledCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_journalEntryCancelledCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_journalEntryCreatedCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_journalEntryCreatedCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_journalEntryDeletedCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_journalEntryDeletedCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_journalEntryEditedCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_journalEntryEditedCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_journalEntryTypeKey
+ _kMOEngagementAndSuggestionAnalyticsParams_journalEntryTypeKey
+ _kMOEngagementAndSuggestionAnalyticsParams_journalEntryWithNoAssetCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_journalEntryWithNoAssetCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_journalEntryWithZeroCharacterCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_journalEntryWithZeroCharacterCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_maxAgeofSensedSuggestionsInDaysKey
+ _kMOEngagementAndSuggestionAnalyticsParams_maxAgeofSensedSuggestionsInDaysKey
+ _kMOEngagementAndSuggestionAnalyticsParams_onboardingCompletionKey
+ _kMOEngagementAndSuggestionAnalyticsParams_onboardingCompletionKey
+ _kMOEngagementAndSuggestionAnalyticsParams_onboardingDurationBinKey
+ _kMOEngagementAndSuggestionAnalyticsParams_onboardingDurationBinKey
+ _kMOEngagementAndSuggestionAnalyticsParams_scalingFactorForAnalyticsKey
+ _kMOEngagementAndSuggestionAnalyticsParams_scalingFactorForAnalyticsKey
+ _kMOEngagementAndSuggestionAnalyticsParams_suggestionCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_suggestionCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_suggestionDeletedCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_suggestionDeletedCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_suggestionQuickAddCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_suggestionQuickAddCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_suggestionSelectedCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_suggestionSelectedCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_suggestionTypeKey
+ _kMOEngagementAndSuggestionAnalyticsParams_suggestionTypeKey
+ _kMOEngagementAndSuggestionAnalyticsParams_suggestionUIPlacementKey
+ _kMOEngagementAndSuggestionAnalyticsParams_suggestionUIPlacementKey
+ _kMOEngagementAndSuggestionAnalyticsParams_suggestionUIVisibilityCategoryKey
+ _kMOEngagementAndSuggestionAnalyticsParams_suggestionUIVisibilityCategoryKey
+ _kMOEngagementAndSuggestionAnalyticsParams_totalSuggestionViewToQuickAddConversionRateKey
+ _kMOEngagementAndSuggestionAnalyticsParams_totalSuggestionViewToQuickAddConversionRateKey
+ _kMOEngagementAndSuggestionAnalyticsParams_totalSuggestionViewToSelectConversionRateKey
+ _kMOEngagementAndSuggestionAnalyticsParams_totalSuggestionViewToSelectConversionRateKey
+ _kMOEngagementAndSuggestionAnalyticsParams_totalViewedInterstitialCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_totalViewedInterstitialCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_totalViewedSuggestionCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_totalViewedSuggestionCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_uniquePhotoMemorySuggestionSubTypeCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_uniquePhotoMemorySuggestionSubTypeCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_uniqueSensedSuggestionSubTypeCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_uniqueSensedSuggestionSubTypeCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_uniqueSensedSuggestionSuperTypeCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_uniqueSensedSuggestionSuperTypeCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_uniqueSuggestionViewToQuickAddConversionRateKey
+ _kMOEngagementAndSuggestionAnalyticsParams_uniqueSuggestionViewToQuickAddConversionRateKey
+ _kMOEngagementAndSuggestionAnalyticsParams_uniqueSuggestionViewToSelectConversionRateKey
+ _kMOEngagementAndSuggestionAnalyticsParams_uniqueSuggestionViewToSelectConversionRateKey
+ _kMOEngagementAndSuggestionAnalyticsParams_uniqueViewedInterstitalCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_uniqueViewedInterstitalCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_uniqueViewedSuggestionCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_uniqueViewedSuggestionCountKey
+ _kMOJournalAppBundleIdentifier
+ _kMOJournalAppBundleIdentifier
+ _kRejectedByVisitHeuristicsFilter
+ _kRejectedByVisitHeuristicsFilter
+ _kSuggestionAcceptThreshold
+ _kSuggestionAcceptThreshold
+ _kSuggestionRecommendThreshold
+ _kSuggestionRecommendThreshold
+ _objc_msgSend$_allResourcesImpl
+ _objc_msgSend$_getDefaultAnalyticsResultWithOnboardingStatus:
+ _objc_msgSend$_isResourceTypeAllowedForResource:
+ _objc_msgSend$_recordDedupeKey:alreadySeenKeys:
+ _objc_msgSend$_recordResource:alreadySeenKeys:
+ _objc_msgSend$_shouldRemoveBundle:checkVisibilityCategoryForUI:
+ _objc_msgSend$_submitSuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:
+ _objc_msgSend$aggregationWindowMap
+ _objc_msgSend$bundleSubTypeToAnalyticsSuggestionTypeMap
+ _objc_msgSend$engagementAndSuggestionAnalyticsManager
+ _objc_msgSend$executeRequest:error:
+ _objc_msgSend$fetchAppEntryEngagementEventsWithTypes:fromStartDate:toEndDate:withError:
+ _objc_msgSend$fetchMePersonWithOptions:
+ _objc_msgSend$fetchSuggestionEngagementEventsWithTypes:fromStartDate:toEndDate:withError:
+ _objc_msgSend$getCharacterCountBin:
+ _objc_msgSend$getDedupeKeyError:
+ _objc_msgSend$getDedupeKeyForResourceData:type:error:
+ _objc_msgSend$getDictionaryForData:error:
+ _objc_msgSend$getPersonalizedSensingAllowedBundles:allowVisits:
+ _objc_msgSend$initWithFetchRequest:
+ _objc_msgSend$isIndoors
+ _objc_msgSend$isReadyToSubmitAnalytics
+ _objc_msgSend$mePerson
+ _objc_msgSend$personalizedSensingFilter
+ _objc_msgSend$personalizedSensingVisitsAllowed
+ _objc_msgSend$result
+ _objc_msgSend$setIsIndoors:
+ _objc_msgSend$setLastAnalyticsSubmissionDate
+ _objc_msgSend$setResultType:
+ _objc_msgSend$submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:
+ _objc_msgSend$submitEngagementAndSuggestionPerformanceAnalyticsWithOnboardingStatus:AndCompletionHandler:
+ _objc_msgSend$submitEventBundleInternalAnalytics:withSubmissionDate:withRefreshVariant:
+ _objc_msgSend$submitSuggestionPerformanceAnalyticsWithOnboardingStatus:AndCompletionHandler:
+ _objc_msgSend$suggestionUIVisibilityCategoryToMOEventBundleVisibilityCategoryForUIMap
+ _objc_msgSend$supressCoarseGranularityPropertyOfEventBundles:primaryBundles:bundleMapping:
+ _objc_msgSend$updateOnboardingStatusDictionaryKeys:
+ _objc_msgSend$withResourcesUsingBlock:
+ _scalingFactorForAnalytics
+ _scalingFactorForAnalytics
+ _thirdPartyMediaSubtypeVariants
+ _thirdPartyMediaSubtypeVariants
- -[MOEventBundleManager submitEventBundleAnalytics:withSubmissionDate:withRefreshVariant:]
- -[MOEventBundleManager submitEventBundleAnalytics:withSubmissionDate:withRefreshVariant:]
- -[MOEventBundleManager submitEventBundleAnalytics:withSubmissionDate:withRefreshVariant:].cold.1
- -[MOEventBundleManager submitEventBundleAnalytics:withSubmissionDate:withRefreshVariant:].cold.1
- -[MOResource getDictionary].cold.1
- -[MOResource getDictionary].cold.1
- -[MOSummarizationManager supressCoarseGranularityPropertyOfEventBundles:primaryBundles:]
- -[MOSummarizationManager supressCoarseGranularityPropertyOfEventBundles:primaryBundles:]
- GCC_except_table102
- GCC_except_table103
- GCC_except_table125
- GCC_except_table19
- GCC_except_table19
- GCC_except_table94
- __101-[MONotificationsManager _getNewTargetTimeToWriteEventBundlesUsingAppSchedule:withCompletionHandler:]_block_invoke.703
- __101-[MONotificationsManager _getNewTargetTimeToWriteEventBundlesUsingAppSchedule:withCompletionHandler:]_block_invoke.703
- __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.611
- __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.611
- __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.611.cold.1
- __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.611.cold.1
- __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.612
- __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.612
- __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.574
- __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.574
- __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.580
- __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.580
- __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.580.cold.1
- __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.580.cold.1
- __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.581
- __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.581
- __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.582
- __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.582
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1157
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1157
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1159
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1159
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1159.cold.1
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1159.cold.1
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.794
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.794
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.801
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.801
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.798
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.798
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.802
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.802
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.802.cold.1
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.802.cold.1
- __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.413
- __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.413
- __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.416
- __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.416
- __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_2.414
- __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_2.414
- __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_3.415
- __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_3.415
- __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.399
- __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.399
- __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.405
- __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.405
- __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_2.401
- __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_2.401
- __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_3.403
- __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_3.403
- __125-[MONotificationsManager _postTimeToWriteSystemNotificationUsingEventBundles:withTrigger:usingAppSchedule:completionHandler:]_block_invoke.772
- __125-[MONotificationsManager _postTimeToWriteSystemNotificationUsingEventBundles:withTrigger:usingAppSchedule:completionHandler:]_block_invoke.772
- __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.298
- __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.298
- __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.300
- __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.300
- __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.426
- __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.426
- __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.429
- __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.429
- __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_2.427
- __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_2.427
- __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_3.428
- __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_3.428
- __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.419
- __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.419
- __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.422
- __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.422
- __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_2.420
- __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_2.420
- __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_3.421
- __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_3.421
- __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.538
- __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.538
- __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.704
- __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.704
- __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.704.cold.1
- __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.704.cold.1
- __59-[MOEventBundleStore removeEventBundles:CompletionHandler:]_block_invoke.cold.1
- __59-[MOEventBundleStore removeEventBundles:CompletionHandler:]_block_invoke.cold.1
- __59-[MOEventBundleStore updateEventBundles:CompletionHandler:]_block_invoke.292
- __59-[MOEventBundleStore updateEventBundles:CompletionHandler:]_block_invoke.292
- __59-[MOEventBundleStore updateEventBundles:CompletionHandler:]_block_invoke.293
- __59-[MOEventBundleStore updateEventBundles:CompletionHandler:]_block_invoke.293
- __59-[MOEventBundleStore updateEventBundles:CompletionHandler:]_block_invoke.294
- __59-[MOEventBundleStore updateEventBundles:CompletionHandler:]_block_invoke.294
- __60-[MODaemonClient _logEngagementEvent:timestamp:withContext:]_block_invoke.462
- __60-[MODaemonClient _logEngagementEvent:timestamp:withContext:]_block_invoke.462
- __60-[MOEventBundleStore removeAllBundlesWithCompletionHandler:]_block_invoke.cold.1
- __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.635
- __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.635
- __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.645
- __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.645
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.619
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.619
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.627
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.627
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke_2.630
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke_2.630
- __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.319
- __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.319
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.381
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.381
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.404
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.404
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.411
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.411
- __68-[MOEventBundleStore fetchEventBundleWithOptions:CompletionHandler:]_block_invoke.255
- __68-[MOEventBundleStore fetchEventBundleWithOptions:CompletionHandler:]_block_invoke.255
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.818
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.818
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.819
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.819
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.823
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.823
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.823.cold.1
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.823.cold.1
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.827
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.827
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.831
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.831
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.835
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.835
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.839
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.839
- __69-[MONotificationsManager serviceSuggestionsNotificationsWithHandler:]_block_invoke.616
- __69-[MONotificationsManager serviceSuggestionsNotificationsWithHandler:]_block_invoke.616
- __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.471
- __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.471
- __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.476
- __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.476
- __71-[MODaemonClient _fetchEventBundlesWithOptions:withContext:andHandler:]_block_invoke.317
- __71-[MODaemonClient _fetchEventBundlesWithOptions:withContext:andHandler:]_block_invoke.317
- __71-[MODaemonClient _purgeEventsWithContext:andRefreshVariant:andHandler:]_block_invoke.340
- __71-[MODaemonClient _purgeEventsWithContext:andRefreshVariant:andHandler:]_block_invoke.340
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.344
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.344
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.345
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.345
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.349
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.349
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.353
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.353
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.685
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.685
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.685.cold.1
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.685.cold.1
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.686
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.686
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.686.cold.1
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.686.cold.1
- __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.700
- __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.700
- __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.700.cold.1
- __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.700.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.731
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.731
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.731.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.731.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.742
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.742
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.742.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.742.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.747
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.747
- __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.287
- __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.287
- __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.289
- __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.289
- __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.295
- __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.295
- __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.295.cold.1
- __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.295.cold.1
- __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke.434
- __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke.434
- __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke.440
- __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke.440
- __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke_2.435
- __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke_2.435
- __81-[MOEventBundleManager fetchRehydratedEventBundlesWithOptions:CompletionHandler:]_block_invoke.690
- __81-[MOEventBundleManager fetchRehydratedEventBundlesWithOptions:CompletionHandler:]_block_invoke.690
- __82-[MODaemonClient _analyzeTrendsInEvents:withContext:andRefreshVariant:andHandler:]_block_invoke.357
- __82-[MODaemonClient _analyzeTrendsInEvents:withContext:andRefreshVariant:andHandler:]_block_invoke.357
- __84-[MODaemonClient didAppEntryUpdateUsingSuggestions:onEvent:duringInterval:withInfo:]_block_invoke.474
- __84-[MODaemonClient didAppEntryUpdateUsingSuggestions:onEvent:duringInterval:withInfo:]_block_invoke.474
- __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.332
- __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.332
- __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.333
- __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.333
- __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.340
- __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.340
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1103
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1103
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1109
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1109
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1110
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1110
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1114
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1114
- __88-[MOSummarizationManager supressCoarseGranularityPropertyOfEventBundles:primaryBundles:]_block_invoke_2.cold.1
- __88-[MOSummarizationManager supressCoarseGranularityPropertyOfEventBundles:primaryBundles:]_block_invoke_2.cold.1
- __88-[MOSummarizationManager supressCoarseGranularityPropertyOfEventBundles:primaryBundles:]_block_invoke_2.cold.2
- __88-[MOSummarizationManager supressCoarseGranularityPropertyOfEventBundles:primaryBundles:]_block_invoke_2.cold.2
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.387
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.387
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.392
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.392
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.397
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.397
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.397.cold.1
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.397.cold.1
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.399
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.399
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.403
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.403
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.403.cold.1
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.403.cold.1
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.403.cold.2
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.403.cold.2
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.408
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.408
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.413
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.413
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.413.cold.1
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.413.cold.1
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.418
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.418
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.423
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.423
- __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.640
- __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.640
- __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.640.cold.1
- __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.640.cold.1
- __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1145
- __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1145
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.426
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.426
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.427
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.427
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.434
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.434
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.442
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.442
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.446
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.446
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.450
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.450
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.454
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.454
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.499
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.499
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.504
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.504
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.509
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.509
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.514
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.514
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.519
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.519
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.524
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.524
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.529
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.529
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.534
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.534
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.539
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.539
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.544
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.544
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.549
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.549
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.554
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.554
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.559
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.559
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.564
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.564
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.566
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.566
- ___88-[MOSummarizationManager supressCoarseGranularityPropertyOfEventBundles:primaryBundles:]_block_invoke
- ___88-[MOSummarizationManager supressCoarseGranularityPropertyOfEventBundles:primaryBundles:]_block_invoke
- ___88-[MOSummarizationManager supressCoarseGranularityPropertyOfEventBundles:primaryBundles:]_block_invoke_2
- ___88-[MOSummarizationManager supressCoarseGranularityPropertyOfEventBundles:primaryBundles:]_block_invoke_2
- ___89-[MOEventBundleManager submitEventBundleAnalytics:withSubmissionDate:withRefreshVariant:]_block_invoke
- ___89-[MOEventBundleManager submitEventBundleAnalytics:withSubmissionDate:withRefreshVariant:]_block_invoke
- ___block_descriptor_48_e8_32s40r_e41_v24?0"MOEventBundle"8"MOEventBundle"16ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e41_v24?0"MOEventBundle"8"MOEventBundle"16ls32l8r40l8
- ___block_descriptor_72_e8_32s40s48s56bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8s56l8s48l8
- ___block_descriptor_72_e8_32s40s48s56bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8s56l8s48l8
- ___block_descriptor_80_e8_32s40s48s56s64bs72r_e46_v32?0"NSArray"8"NSError"16"NSDictionary"24ls32l8s40l8s48l8s64l8r72l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64bs72r_e46_v32?0"NSArray"8"NSError"16"NSDictionary"24ls32l8s40l8s48l8s64l8r72l8s56l8
- __block_literal_global.294
- __block_literal_global.294
- __block_literal_global.345
- __block_literal_global.345
- __block_literal_global.347
- __block_literal_global.347
- __block_literal_global.364
- __block_literal_global.364
- __block_literal_global.397
- __block_literal_global.397
- __block_literal_global.408
- __block_literal_global.408
- __block_literal_global.418
- __block_literal_global.418
- __block_literal_global.423
- __block_literal_global.423
- __block_literal_global.425
- __block_literal_global.425
- __block_literal_global.425
- __block_literal_global.425
- __block_literal_global.431
- __block_literal_global.431
- __block_literal_global.439
- __block_literal_global.439
- __block_literal_global.456
- __block_literal_global.456
- __block_literal_global.465
- __block_literal_global.465
- __block_literal_global.467
- __block_literal_global.467
- __block_literal_global.469
- __block_literal_global.469
- __block_literal_global.506
- __block_literal_global.506
- __block_literal_global.543
- __block_literal_global.543
- __block_literal_global.548
- __block_literal_global.548
- __block_literal_global.622
- __block_literal_global.622
- __block_literal_global.625
- __block_literal_global.625
- __block_literal_global.632
- __block_literal_global.632
- __block_literal_global.649
- __block_literal_global.649
- __block_literal_global.689
- __block_literal_global.689
- __block_literal_global.753
- __block_literal_global.753
- __block_literal_global.758
- __block_literal_global.758
- __block_literal_global.760
- __block_literal_global.760
- _objc_msgSend$submitEventBundleAnalytics:withSubmissionDate:withRefreshVariant:
- _objc_msgSend$supressCoarseGranularityPropertyOfEventBundles:primaryBundles:
CStrings:
+ "\x01\x1d"
+ "#bundlecuration, filtered activity summary bundle, reason shouldAllowActivityBundles=False & activity bundle, bundleId %!@(MISSING), suggestionId %!@(MISSING), bundleSubType %!l(MISSING)u, label, %!@(MISSING)"
+ "#bundlecuration, filtered bundle, reason UIrejected, id, %!@(MISSING), suggestion id, %!@(MISSING), label, %!@(MISSING)"
+ "#bundlecuration, filtered cluster bundle, reason clusterMetadata.isFiltered, bundleId %!@(MISSING), suggestionId %!@(MISSING), bundleSubType %!l(MISSING)u, label, %!@(MISSING)"
+ "#bundlecuration, filtered cluster bundle, reason shouldAllowActivityBundles=False & activity cluster, bundleId %!@(MISSING), suggestionId %!@(MISSING), bundleSubType %!l(MISSING)u, label, %!@(MISSING)"
+ "#bundlecuration, filtered cluster bundle, reason unsupported subtype, bundleId %!@(MISSING), suggestionId %!@(MISSING), bundleSubType %!l(MISSING)u, label, %!@(MISSING)"
+ "%!@(MISSING), request, %!@(MISSING), results count, %!@(MISSING), error, %!@(MISSING)"
+ "%!d(MISSING), Ingesting events for sub bundle, %!@(MISSING)"
+ "%!d(MISSING), Ingesting persons for sub bundle, %!@(MISSING)"
+ "%!d(MISSING), Ingesting photo trait for sub bundle, %!@(MISSING)"
+ "%!d(MISSING), Ingesting places for sub bundle, %!@(MISSING)"
+ "%!d(MISSING), Sub bundle place larger than city. skipping sub bundle, %!@(MISSING)"
+ "%!d(MISSING).%!d(MISSING), adding resource, %!@(MISSING)"
+ "<MOResourceMO identifier, %!@(MISSING), name, %!@(MISSING), type, %!@(MISSING), assets, %!@(MISSING), dedupe key, %!@(MISSING), data.length, %!l(MISSING)u, value, %!f(MISSING), sourceEventIdentifier, %!@(MISSING)"
+ "@\"MOEngagementAndSuggestionAnalyticsManager\""
+ "@\"PHPerson\""
+ "@32@0:8@16^@24"
+ "@40@0:8@16@24^@32"
+ "@40@0:8@16Q24^@32"
+ "Activity bundle was disabled. Collecting subBundleIDs of activity summaries to recover visit subbundles. subBundleID count=%!l(MISSING)u"
+ "B24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
+ "B24@?0@\"NSString\"8@\"NSDictionary\"16"
+ "CoarseGranularityAggregation: merge, suppressed, %!l(MISSING)u, bundle.interfacetype, %!l(MISSING)u, megaBundle.interfacetype, %!l(MISSING)u, bundle.summary, %!l(MISSING)u, bundle.aggregated, %!l(MISSING)u, bundle.granularity, %!l(MISSING)u, ratio, %!f(MISSING), bundle suggestionID, %!@(MISSING), mega bundle suggestionID, %!@(MISSING)"
+ "Current person matched with the me Person"
+ "Dedupe key not available for this type, %!@(MISSING)."
+ "Engagement and suggestion analytics were never submitted. Attempting to submit new analytics"
+ "EngagementAndSuggestionAnalyticsManager is initialized: lastAnalyticsSubmissionDate=%!@(MISSING) minimumTimeGapBetweenSubmissionsInDays=%!f(MISSING)"
+ "Event with identifier, %!@(MISSING), is a duplicate of a previously processed event"
+ "Journal entry engagement analytics result was submitted: %!@(MISSING)"
+ "Journal entryengagement event count from the last %!@(MISSING)days=%!l(MISSING)u"
+ "Last analytics submission date was updated from %!@(MISSING) to %!@(MISSING)"
+ "LastAnalyticsSubmissionDate"
+ "MOActivityForPersonalizedSensing"
+ "MOEngagementAndSuggestionAnalyticsManager"
+ "MOEngagementAndSuggestionAnalyticsParams"
+ "MOPersonalizedSensingUtils"
+ "MOWorkoutMetaDataKeyIsIndoors"
+ "Malformed dictionary, %!@(MISSING), for resource type, %!@(MISSING), the key %!@(MISSING) is missing."
+ "Malformed dictionary, %!@(MISSING), for resource type, %!@(MISSING), the one of the keys %!@(MISSING), %!@(MISSING), %!@(MISSING) is missing."
+ "Maps to one daily trip bundle."
+ "Me person from Photos: %!@(MISSING)"
+ "New dedupe key, %!@(MISSING)."
+ "Not allowed bundle by category (%!l(MISSING)u): %!@(MISSING)"
+ "Not allowed bundle: %!@(MISSING)"
+ "Not allowed visit bundle: %!@(MISSING)"
+ "PERSONALIZEDSENSING"
+ "Person added with contact identifier, %!@(MISSING)"
+ "Person added with local identifier, %!@(MISSING)"
+ "Person with contact identifier, %!@(MISSING), is a duplicate of a previously processed person object."
+ "Person with local identifier, %!@(MISSING), is a duplicate of a previously processed person object."
+ "Person, %!@(MISSING), has both identifier and contactIdentifier nil"
+ "Place added with identifier, %!@(MISSING)"
+ "Place with identifier, %!@(MISSING), is a duplicate of a previously processed place."
+ "PrivacySettingsOverrideLookBackWindowActivity"
+ "PrivacySettingsOverrideLookBackWindowCommunication"
+ "PrivacySettingsOverrideLookBackWindowLocation"
+ "PrivacySettingsOverrideLookBackWindowMedia"
+ "PrivacySettingsOverrideLookBackWindowPeople"
+ "PrivacySettingsOverrideLookBackWindowPhoto"
+ "PrivacySettingsOverrideLookBackWindowStateOfMind"
+ "Q20@0:8f16"
+ "Recent"
+ "Recommended"
+ "Resource with identifier, %!@(MISSING), is a duplicate of a previously processed resource"
+ "SubBundle of activity summary was recovered. bundleID %!@(MISSING), suggestionID %!@(MISSING), bundleSubType %!l(MISSING)u, goodnessScore %!f(MISSING), acceptThreshold %!f(MISSING)"
+ "SubBundle of activity summary was suppressed. bundleID %!@(MISSING), suggestionID %!@(MISSING), bundleSubType %!l(MISSING)u, rejectedByVisitHeuristicsFilter, %!@(MISSING) goodnessScore %!f(MISSING), acceptThreshold %!f(MISSING)"
+ "Submit internal eventBundle analytics"
+ "SubmitEngagementAnalytics"
+ "SubmitEngagementAndSuggestionPerformanceAnalyticssubmitEngagementAnalytics"
+ "SubmitEngagementAndSuggestionPerformanceAnalyticssubmitSuggestionPerformanceAnalytics"
+ "SubmitSuggestionPerformanceAnalytics"
+ "Submitting engagement metric analytics"
+ "Submitting suggestion performance metric analytics"
+ "Submitting suggestion performance metric for %!l(MISSING)u bundles."
+ "Submitting suggestion performance metric for suggestionVisibilityCategory %!@(MISSING) from the last %!@(MISSING)days : bundleCount=%!l(MISSING)u."
+ "Submitting suggestion performance metric from the last %!@(MISSING)days: bundleCount=%!l(MISSING)u."
+ "Suggestion engagement analytics result was submitted: %!@(MISSING)"
+ "Suggestion engagement event count from the last %!@(MISSING) days %!l(MISSING)u"
+ "Suggestion engagement signal analytics was suppressed: isInternalBuild=%!d(MISSING), suggestionEngagementType=%!@(MISSING)"
+ "Suggestion perf analytics result was submitted: %!@(MISSING)"
+ "Suggestion perf analytics submission was completed. Result: %!@(MISSING)"
+ "T@\"MOEngagementAndSuggestionAnalyticsManager\",&,N,V_engagementAndSuggestionAnalyticsManager"
+ "T@\"NSArray\",R,N,V_suggestionEngagementTypesEligibleForRawExternalAnalytics"
+ "T@\"NSDate\",R,N,V_lastAnalyticsSubmissionDate"
+ "T@\"PHPerson\",&,N,V_mePerson"
+ "TB,N,V_isIndoors"
+ "TB,N,V_personalizedSensingFilter"
+ "TB,N,V_personalizedSensingVisitsAllowed"
+ "TB,N,V_skipLocalization"
+ "TB,R,N,V_isInternalBuild"
+ "Tf,R,N,V_minimumTimeGapBetweenSubmissionsInDays"
+ "The dedupe key is nil for resource, %!@(MISSING)"
+ "The dedupe key is nil."
+ "The dedupe key, %!@(MISSING), was already seen."
+ "Total fetched suggestion engagement event count: %!l(MISSING)u, journal entry engagement event count: %!l(MISSING)u"
+ "Unable to deserialize data to dictionary, %!@(MISSING)"
+ "Unable to retrieve dedupe key due to error, %!@(MISSING). Falling back to identifier, %!@(MISSING)"
+ "Using for the dedupe key the dictionary, %!@(MISSING)"
+ "Using for the dedupe key the map item handler , %!l(MISSING)u"
+ "Using for the dedupe key, %!@(MISSING)"
+ "[bundleEventsWithRefreshVariant] refreshVariant %!l(MISSING)u, analytics result %!@(MISSING), error %!@(MISSING)"
+ "[bundleEventsWithRefreshVariant] refreshVariant %!l(MISSING)u, bundling result %!@(MISSING), error %!@(MISSING)"
+ "[bundleEventsWithRefreshVariant] refreshVariant %!l(MISSING)u, clustering result %!@(MISSING), error %!@(MISSING)"
+ "[bundleEventsWithRefreshVariant]refreshVariant %!l(MISSING)u, bundling result %!@(MISSING), error %!@(MISSING)"
+ "[fetchAllAppEntryEngagementEventsForType] Biome sink completion result with error:%!@(MISSING)"
+ "[fetchAllSuggestionEngagementEventsForType] Biome sink completion result with error:%!@(MISSING)"
+ "[fetchAppEntryEngagementEventsFromStartDate:toEndDate:withError] Biome sink completion result with error:%!@(MISSING)"
+ "[fetchSuggestionEngagementEventsFromStartDate:toEndDate:withErrror] Biome sink completion result with error:%!@(MISSING)"
+ "[submitEngagementAnalytics] Biome sink error:%!@(MISSING)"
+ "[submitEngagementAnalytics] result:%!@(MISSING), error:%!@(MISSING)"
+ "[submitEngagementAndSuggestionPerformanceAnalytics] completed analytics submission. Result:%!@(MISSING)"
+ "[submitSuggestionPerformanceAnalytics] result:%!@(MISSING), error:%!@(MISSING)"
+ "_allResourcesImpl"
+ "_engagementAndSuggestionAnalyticsManager"
+ "_getDefaultAnalyticsResultWithOnboardingStatus:"
+ "_isIndoors"
+ "_isResourceTypeAllowedForResource:"
+ "_lastAnalyticsSubmissionDate"
+ "_mePerson"
+ "_minimumTimeGapBetweenSubmissionsInDays"
+ "_personalizedSensingFilter"
+ "_personalizedSensingVisitsAllowed"
+ "_recordDedupeKey:alreadySeenKeys:"
+ "_recordResource:alreadySeenKeys:"
+ "_shouldRemoveBundle:checkVisibilityCategoryForUI:"
+ "_skipLocalization"
+ "_submitSuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:"
+ "_suggestionEngagementTypesEligibleForRawExternalAnalytics"
+ "aggregationWindow"
+ "aggregationWindowMap"
+ "appType"
+ "ascending, %!@(MISSING),  startDate, %!@(MISSING), endDate, %!@(MISSING), limit, %!@(MISSING), filterBundle, %!@(MISSING), skipRanking, %!@(MISSING), interfaceType, %!l(MISSING)u, pssFilter, %!@(MISSING), pssVisits, %!@(MISSING)"
+ "avgAgeofSensedSuggestionsInDays"
+ "bundleSubTypeToAnalyticsSuggestionTypeMap"
+ "com.apple.Moments.EngagementAggregatedMetrics"
+ "com.apple.Moments.SuggestionPerformanceAggregatedMetrics"
+ "daily trip bundles : %!@(MISSING)"
+ "engagementAndSuggestionAnalyticsManager"
+ "executeRequest:error:"
+ "fetchAppEntryEngagementEventsFromStartDate:toEndDate:withError:"
+ "fetchAppEntryEngagementEventsWithTypes:fromStartDate:toEndDate:withError:"
+ "fetchMePersonWithOptions:"
+ "fetchSuggestionEngagementEventsFromStartDate:toEndDate:withError:"
+ "fetchSuggestionEngagementEventsWithTypes:fromStartDate:toEndDate:withError:"
+ "fetched bundle count, %!l(MISSING)u, error, %!@(MISSING)"
+ "for daily trip bundle : %!@(MISSING)"
+ "getCharacterCountBin:"
+ "getDedupeKeyError:"
+ "getDedupeKeyForResourceData:type:error:"
+ "getDictionaryForData:error:"
+ "getPersonalizedSensingAllowedBundles:allowVisits:"
+ "got current person as me person from Photos, localIdentifier : %!@(MISSING)"
+ "got me person from Photo person localIdentifier :  %!@(MISSING)"
+ "initWithFetchRequest:"
+ "interfaceType == %!l(MISSING)uu AND bundleSuperType == %!l(MISSING)uu"
+ "isIndoors"
+ "isIndoors"
+ "isReadyToSubmitAnalytics"
+ "journalEntryAvgAssetCount"
+ "journalEntryAvgCharacterCountBinned"
+ "journalEntryCancelledCount"
+ "journalEntryCreatedCount"
+ "journalEntryDeletedCount"
+ "journalEntryEditedCount"
+ "journalEntryEngagementAnalyticsPayloadCount"
+ "journalEntryType"
+ "journalEntryWithNoAssetCount"
+ "journalEntryWithZeroCharacterCount"
+ "kEventResourcePatternWorkoutIsIndoors"
+ "kRejectedByVisitHeuristicsFilter"
+ "lastAnalyticsSubmissionDate"
+ "lastAnalyticsSubmissionDate"
+ "maxAgeofSensedSuggestionsInDays"
+ "mePerson"
+ "minimumTimeGapBetweenAnalyticsSubmissionsInDays"
+ "minimumTimeGapBetweenSubmissionsInDays"
+ "no bundle context is extracted due to 0 bundle fetched"
+ "onboardingCompletion"
+ "personalizedSensingFilter"
+ "personalizedSensingVisitsAllowed"
+ "pssFilter"
+ "pssVisits"
+ "resource data dictionary , %!@(MISSING)"
+ "result"
+ "scalingFactorForAnalyticsKey"
+ "setEngagementAndSuggestionAnalyticsManager:"
+ "setIsIndoors:"
+ "setLastAnalyticsSubmissionDate"
+ "setMePerson:"
+ "setPersonalizedSensingFilter:"
+ "setPersonalizedSensingVisitsAllowed:"
+ "setResultType:"
+ "setSkipLocalization:"
+ "skipLocalization"
+ "skipLocalization"
+ "startDate >= %!@(MISSING) AND endDate <= %!@(MISSING)"
+ "subBundleIDs=%!@(MISSING)"
+ "subSuggestionIDs=%!@(MISSING)"
+ "submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:"
+ "submitEngagementAndSuggestionPerformanceAnalyticsWithOnboardingStatus:AndCompletionHandler:"
+ "submitEventBundleInternalAnalytics:withSubmissionDate:withRefreshVariant:"
+ "submitSuggestionPerformanceAnalyticsWithOnboardingStatus:AndCompletionHandler:"
+ "suggestionAcceptThreshold"
+ "suggestionAnalyticsPayloadCount"
+ "suggestionCount"
+ "suggestionDeletedCount"
+ "suggestionEngagementAnalyticsPayloadCount"
+ "suggestionEngagementTypesEligibleForRawExternalAnalytics"
+ "suggestionQuickAddCount"
+ "suggestionRecommendThreshold"
+ "suggestionSelectedCount"
+ "suggestionUIPlacement"
+ "suggestionUIVisibilityCategory"
+ "suggestionUIVisibilityCategoryToMOEventBundleVisibilityCategoryForUIMap"
+ "summary trip Bundle : %!@(MISSING) maps to :"
+ "suppressed summary trip bundle : %!@(MISSING) "
+ "supressCoarseGranularityPropertyOfEventBundles:primaryBundles:bundleMapping:"
+ "total count of fetched bundles %!l(MISSING)u"
+ "totalSuggestionViewToQuickAddConversionRate"
+ "totalSuggestionViewToSelectConversionRate"
+ "totalViewedSuggestionCount"
+ "totalviewedInterstitialCount"
+ "uniquePhotoMemorySuggestionSubTypeCount"
+ "uniqueSensedSuggestionSubTypeCount"
+ "uniqueSensedSuggestionSuperTypeCount"
+ "uniqueSuggestionViewToQuickAddConversionRate"
+ "uniqueSuggestionViewToSelectConversionRate"
+ "uniqueViewedInterstitalCount"
+ "uniqueViewedSuggestionCount"
+ "updateOnboardingStatusDictionaryKeys:"
+ "v24@?0@\"MOResource\"8^B16"
+ "v32@?0@\"NSNumber\"8@\"NSNumber\"16^B24"
+ "withResourcesUsingBlock:"
- "\x01\x1c"
- "\t"
- "%!d(MISSING).%!d(MISSING), Cloned resource, %!@(MISSING)"
- "<MOResourceMO identifier, %!@(MISSING), name, %!@(MISSING), type, %!@(MISSING), assets, %!@(MISSING), data.length, %!l(MISSING)u, value, %!f(MISSING), sourceEventIdentifier, %!@(MISSING)"
- "CoarseGranularityAggregation: merge, suppressed, %!l(MISSING)u, bundle.interfacetype, %!l(MISSING)u, bundle.summary, %!l(MISSING)u, bundle.aggregated, %!l(MISSING)u, bundle.granularity, %!l(MISSING)u, ratio, %!f(MISSING), bundle %!@(MISSING), maga bundles, %!@(MISSING)"
- "[bundleEventsWithRefreshVariant] refreshVariant %!l(MISSING)u, bundling result %!@(MISSING)"
- "[bundleEventsWithRefreshVariant] refreshVariant %!l(MISSING)u, bundling result %!@(MISSING), clustering result %!@(MISSING)"
- "ascending, %!@(MISSING),  startDate, %!@(MISSING), endDate, %!@(MISSING), limit, %!@(MISSING), filterBundle, %!@(MISSING), skipRanking, %!@(MISSING), interfaceType, %!l(MISSING)u"
- "got me person from Photos, localIdentifier : %!@(MISSING)"
- "saving bundle deletion operation error, %!@(MISSING)"
- "saving bundle deletion operation succeeded"
- "submitEventBundleAnalytics:withSubmissionDate:withRefreshVariant:"
- "supressCoarseGranularityPropertyOfEventBundles:primaryBundles:"
- "trying to remove event bundles count %!l(MISSING)u"

```
