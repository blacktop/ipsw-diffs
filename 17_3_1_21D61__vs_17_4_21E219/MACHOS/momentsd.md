## momentsd

> `/usr/libexec/momentsd`

```diff

-127.0.55.0.0
-  __TEXT.__text: 0x1b076c
+130.0.11.0.0
+  __TEXT.__text: 0x1b4ab4
   __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_stubs: 0x16240
-  __TEXT.__objc_methlist: 0xbccc
-  __TEXT.__objc_classname: 0x1528
-  __TEXT.__objc_methname: 0x23d37
-  __TEXT.__objc_methtype: 0x23c2
-  __TEXT.__cstring: 0x1cdc4
-  __TEXT.__oslogstring: 0x2085a
-  __TEXT.__const: 0x7d2
-  __TEXT.__gcc_except_tab: 0x4e20
+  __TEXT.__objc_stubs: 0x16500
+  __TEXT.__objc_methlist: 0xbdc4
+  __TEXT.__objc_classname: 0x1544
+  __TEXT.__objc_methname: 0x241b5
+  __TEXT.__objc_methtype: 0x23e7
+  __TEXT.__cstring: 0x1d2b4
+  __TEXT.__oslogstring: 0x20b35
+  __TEXT.__const: 0x7f2
+  __TEXT.__gcc_except_tab: 0x4f00
   __TEXT.__ustring: 0x124
   __TEXT.__dlopen_cstrs: 0x51
   __TEXT.__constg_swiftt: 0x118

   __TEXT.__swift5_capture: 0x70
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_reflstr: 0x30
-  __TEXT.__unwind_info: 0x3958
-  __TEXT.__eh_frame: 0x270
+  __TEXT.__unwind_info: 0x39f8
+  __TEXT.__eh_frame: 0x298
   __DATA_CONST.__auth_got: 0x880
-  __DATA_CONST.__got: 0x2e0
+  __DATA_CONST.__got: 0x2f0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x77f0
-  __DATA_CONST.__cfstring: 0x1cd60
-  __DATA_CONST.__objc_classlist: 0x5a8
+  __DATA_CONST.__const: 0x7a90
+  __DATA_CONST.__cfstring: 0x1d420
+  __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x2a90
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x990
+  __DATA_CONST.__objc_superrefs: 0x4a8
+  __DATA_CONST.__objc_intobj: 0x2b68
   __DATA_CONST.__objc_floatobj: 0x270
-  __DATA_CONST.__objc_arraydata: 0xb10
-  __DATA_CONST.__objc_arrayobj: 0x4c8
+  __DATA_CONST.__objc_arraydata: 0xb28
+  __DATA_CONST.__objc_arrayobj: 0x4e0
   __DATA_CONST.__objc_doubleobj: 0x2f0
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x15450
-  __DATA.__objc_selrefs: 0x6860
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x978
-  __DATA.__objc_superrefs: 0x4a8
-  __DATA.__objc_ivar: 0xf8c
-  __DATA.__objc_data: 0x3a10
+  __DATA.__objc_const: 0x15580
+  __DATA.__objc_selrefs: 0x6928
+  __DATA.__objc_ivar: 0xf9c
+  __DATA.__objc_data: 0x3a60
   __DATA.__data: 0x1078
   __DATA.__bss: 0x168
   __DATA.__common: 0xb8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6158
-  Symbols:   43680
-  CStrings:  11730
+  Functions: 6199
+  Symbols:   44046
+  CStrings:  11836
 
Symbols:
+ +[JournalAppSettingsUtilities boolForKey:]
+ +[JournalAppSettingsUtilities objectForKey:]
+ +[JournalAppSettingsUtilities setBool:forKey:]
+ +[JournalAppSettingsUtilities setObject:forKey:]
+ +[JournalAppSettingsUtilities settingsBundle]
+ +[JournalAppSettingsUtilities settingsDefaults]
+ -[MOEngagementHistoryManager determineAddedCharacterBinRange:]
+ -[MOEngagementHistoryManager updateBundle:forSuggestionEvent:withSummary:].cold.20
+ -[MOEngagementHistoryManager updateBundle:forSuggestionEvent:withSummary:].cold.21
+ -[MOEngagementHistoryManager updateBundle:forSuggestionEvent:withSummary:].cold.22
+ -[MOEngagementHistoryManager updateBundle:forSuggestionEvent:withSummary:].cold.23
+ -[MOEngagementHistoryManager updateBundle:forSuggestionEvent:withSummary:].cold.24
+ -[MOEngagementHistoryManager updateBundle:forSuggestionEvent:withSummary:].cold.25
+ -[MONotificationsManager _postNotificationWithTitle:message:defaultActionURL:notificationIdentifier:withIcon:usingTrigger:useSubordinateIcon:userInfo:handler:]
+ -[MONotificationsManager createBundleInformationForAnalyticsWithBundle:]
+ -[MONotificationsManager engagementHistoryManager]
+ -[MONotificationsManager eventBundleManager]
+ -[MONotificationsManager getBiomeContextDictionaryWithUserInfo:]
+ -[MONotificationsManager getNotificationScheduledDeliverySetting]
+ -[MONotificationsManager setEventBundleManager:]
+ -[MONotificationsManager submitEngagementHistoryUpdateWithEvent:userInfo:]
+ -[MONotificationsManager submitNotificationEngagementEventAnalyticsForBundles:userInfo:fromTrigger:withPostingDate:]
+ -[MOOnboardingAndSettingsPersistence _fetchSignificantLocationEnablementStatus]
+ -[MOOnboardingAndSettingsPersistence determineOnboardingDurationBinRange]
+ -[MOOnboardingAndSettingsPersistence determineOnboardingDurationBinRange].cold.1
+ -[MORoutineServiceManager _fetchRealTimeVisitsBetweenStartDate:EndDate:CompletionHandler:]
+ -[MORoutineServiceManager _fetchRealTimeVisitsForStartDate:CompletionHandler:]
+ -[MORoutineServiceManager fetchConsolidatedEvents:withStored:handler:]
+ /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/momentsd.build/Objects-normal/arm64e/JournalAppSettingsUtilities.o
+ /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/momentsd.build/Objects-normal/arm64e/MONotificationManagerKeys.o
+ GCC_except_table108
+ GCC_except_table129
+ GCC_except_table139
+ GCC_except_table152
+ GCC_except_table161
+ GCC_except_table41
+ GCC_except_table49
+ GCC_except_table55
+ GCC_except_table62
+ GCC_except_table66
+ GCC_except_table71
+ GCC_except_table78
+ JournalAppSettingsUtilities.m
+ MONotificationManagerKeys.m
+ OBJC_IVAR_$_MONotificationsManager._engagementHistoryManager
+ OBJC_IVAR_$_MONotificationsManager._eventBundleManager
+ OBJC_IVAR_$_MOOnboardingAndSettingsPersistence._cachedRoutineState
+ OBJC_IVAR_$_MOOnboardingAndSettingsPersistence._cachedRoutineStateTimestamp
+ _JOURNALING_SCHEDULE
+ _JOURNALING_SCHEDULE_DETAIL
+ _JURASSIC_APP_GROUP_IDENTIFIER
+ _LOCK_JOURNAL
+ _MOSuggestionEngagementEventNotificationDequeued
+ _MOSuggestionEngagementEventNotificationDismissed
+ _MOSuggestionEngagementEventNotificationOverriden
+ _MOSuggestionEngagementEventNotificationPosted
+ _MOSuggestionEngagementEventNotificationQueued
+ _MOSuggestionEngagementEventNotificationTapped
+ _OBJC_CLASS_$_BMMomentsEngagementNotificationInfo
+ _OBJC_CLASS_$_JournalAppSettingsUtilities
+ _OBJC_CLASS_$_UNNotificationCategory
+ _OBJC_METACLASS_$_JournalAppSettingsUtilities
+ _REQUIRE_PASSCODE
+ _SAVE_TO_PHOTOS
+ _SKIP_JOURNALING_SUGGESTIONS
+ _UNNotificationDefaultActionIdentifier
+ _UNNotificationDismissActionIdentifier
+ __101-[MONotificationsManager _getNewTargetTimeToWriteEventBundlesUsingAppSchedule:withCompletionHandler:]_block_invoke.653
+ __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.566
+ __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.566.cold.1
+ __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.568
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.227
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.231
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.231.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.237.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.240
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.242
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.242.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.242.cold.2
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.232
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.238
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.225
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.233
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.239
+ __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.528
+ __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.534
+ __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.534.cold.1
+ __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.535
+ __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.370
+ __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.373
+ __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_2.371
+ __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_3.372
+ __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.355
+ __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.361
+ __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_2.357
+ __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_3.359
+ __125-[MONotificationsManager _postTimeToWriteSystemNotificationUsingEventBundles:withTrigger:usingAppSchedule:completionHandler:]_block_invoke.717
+ __125-[MONotificationsManager _postTimeToWriteSystemNotificationUsingEventBundles:withTrigger:usingAppSchedule:completionHandler:]_block_invoke.cold.1
+ __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.383
+ __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.386
+ __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_2.384
+ __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_3.385
+ __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.376
+ __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.379
+ __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_2.377
+ __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_3.378
+ __38-[MOEventManager storeEvents:handler:]_block_invoke.275
+ __42-[MOBiomeManager donateEvents:andBundles:]_block_invoke.1165
+ __44-[MOEventManager _purgePreOnboardingEvents:]_block_invoke.454
+ __44-[MOEventManager _purgePreOnboardingEvents:]_block_invoke.455
+ __47-[MOEventManager _rehydrateEvents:withHandler:]_block_invoke.317
+ __48-[MOEventManager _updateEventsDeletedAtSources:]_block_invoke.422
+ __48-[MOEventManager _updateEventsDeletedAtSources:]_block_invoke.423
+ __48-[MONotificationsManager _clearAllNotifications]_block_invoke.cold.1
+ __49-[MOBiomeManager _updateDataStreamWithEngagement]_block_invoke.1179
+ __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.125
+ __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.126
+ __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.126.cold.1
+ __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke_2.cold.1
+ __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke_2.cold.2
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.324
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.328
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.332
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.342
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.352
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.356
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.360
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.364
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.368
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.372
+ __59-[MOEventManager fetchEventsWithOptions:CompletionHandler:]_block_invoke.282
+ __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.286
+ __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.288
+ __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.290
+ __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.465
+ __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.481
+ __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.481.cold.1
+ __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.430
+ __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.434
+ __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.438
+ __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.442
+ __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.446
+ __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.450
+ __61-[MOEventManager cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.376
+ __61-[MOHealthKitManager _updateWorkoutsDeletedAtSource:handler:]_block_invoke.129
+ __61-[MOHealthKitManager _updateWorkoutsDeletedAtSource:handler:]_block_invoke.129.cold.1
+ __61-[MOHealthKitManager _updateWorkoutsDeletedAtSource:handler:]_block_invoke.130
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.389
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.389.cold.1
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.393
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.400
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.400.cold.1
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.407
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.407.cold.1
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.411
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.411.cold.1
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.415.cold.1
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.416
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.416.cold.1
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.418
+ __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.1190
+ __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.1200
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.249
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.250
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.251
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.255
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.256
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.260
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.269
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.270
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.271
+ __66-[MOHealthKitManager _rehydrateStoredEvents:fromWorkouts:handler:]_block_invoke.123
+ __69-[MOBiomeManager fetchMomentsEngagementForBundles:CompletionHandler:]_block_invoke.1183
+ __69-[MONotificationsManager serviceSuggestionsNotificationsWithHandler:]_block_invoke.572
+ __71-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterOnboarding]_block_invoke.217
+ __71-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterOnboarding]_block_invoke_2.218
+ __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.227
+ __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.229
+ __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.230
+ __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.230.cold.1
+ __75-[MOHealthKitManager fetchAndSaveWorkoutsBetweenStartDate:EndDate:handler:]_block_invoke.131
+ __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke.391
+ __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke.397
+ __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke_2.392
+ __78-[MORoutineServiceManager _fetchRealTimeVisitsForStartDate:CompletionHandler:]_block_invoke.cold.1
+ __82-[MOBiomeManager fetchMomentsEventDataBetweenStartDate:EndDate:CompletionHandler:]_block_invoke.1185
+ __82-[MOHealthKitManager fetchAndSaveMindfulSessionsBetweenStartDate:EndDate:handler:]_block_invoke.132
+ __84-[MOEventManager _fetchEventsFromDBAndRehydrateEventsWithOptions:CompletionHandler:]_block_invoke.296
+ __88-[MORoutineServiceManager _fetchFamiliarityIndexesLOIForDateInterval:CompletionHandler:]_block_invoke.162
+ __88-[MORoutineServiceManager _fetchFamiliarityIndexesLOIForDateInterval:CompletionHandler:]_block_invoke.162.cold.1
+ __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.596
+ __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.596.cold.1
+ __89-[MORoutineServiceManager _fetchVisitsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.205
+ __89-[MORoutineServiceManager _fetchVisitsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.206
+ __89-[MORoutineServiceManager _fetchVisitsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.206.cold.1
+ __89-[MORoutineServiceManager _fetchVisitsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.208
+ __91-[MOHealthKitManager _fetchWorkoutEventsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.157
+ __OBJC_$_CLASS_METHODS_JournalAppSettingsUtilities
+ __OBJC_CLASS_RO_$_JournalAppSettingsUtilities
+ __OBJC_METACLASS_RO_$_JournalAppSettingsUtilities
+ __ZNKSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ue170006Ev
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__113__nth_elementB8ue170006INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_11__wrap_iterIPdEEEEvT1_S8_S8_T0_
+ __ZNSt3__116__selection_sortB8ue170006INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_11__wrap_iterIPdEEEEvT1_S8_T0_
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__17__sort3B8ue170006INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_11__wrap_iterIPdEEEEjT1_S8_S8_T0_
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ ___48-[MONotificationsManager _clearAllNotifications]_block_invoke
+ ___50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke_2
+ ___55-[MOHealthKitManager _createEventsFromWorkout:handler:]_block_invoke_3
+ ___65-[MONotificationsManager getNotificationScheduledDeliverySetting]_block_invoke
+ ___66-[MOHealthKitManager _rehydrateStoredEvents:fromWorkouts:handler:]_block_invoke_3
+ ___71-[MOOnboardingAndSettingsPersistence getSnapshotDictionaryForAnalytics]_block_invoke
+ ___74-[MONotificationsManager submitEngagementHistoryUpdateWithEvent:userInfo:]_block_invoke
+ ___78-[MORoutineServiceManager _fetchRealTimeVisitsForStartDate:CompletionHandler:]_block_invoke
+ ___79-[MOOnboardingAndSettingsPersistence _fetchSignificantLocationEnablementStatus]_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64bs72r80r88r96r_e5_v8?0ls32l8s40l8s48l8s56l8r72l8s64l8r80l8r88l8r96l8
+ ___block_descriptor_112_e8_32s40s48s56s64s72bs80r88r96r104r_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8r80l8s72l8r88l8r96l8r104l8s48l8s56l8s64l8
+ ___block_descriptor_112_e8_32s40s48s56s64s72bs80r88r96r104r_e5_v8?0lr80l8s32l8s72l8r88l8r96l8s40l8r104l8s48l8s56l8s64l8
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80bs88r96r104r112r_e5_v8?0ls32l8r88l8r96l8s40l8s48l8s56l8r104l8s80l8r112l8s64l8s72l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSArray"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e32_v16?0"UNNotificationSettings"8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSArray"8ls32l8s40l8
+ ___block_descriptor_56_e8_32r40r_e34_v24?0"NSDictionary"8"NSError"16lr32l8r40l8
+ ___block_descriptor_56_e8_32s40s48s_e46_v32?0"NSArray"8"NSError"16"NSDictionary"24ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s_e20_v24?0q8"NSError"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8r64l8s56l8
+ ___block_descriptor_81_e8_32s40s48s56s64s72bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ __block_literal_global.318
+ __block_literal_global.320
+ __block_literal_global.322
+ __block_literal_global.353
+ __block_literal_global.369
+ __block_literal_global.375
+ __block_literal_global.382
+ __block_literal_global.388
+ _kMONotifications_analyticsDict
+ _kMONotifications_bundleID
+ _kMONotifications_endDate
+ _kMONotifications_engagementNotificationLatency
+ _kMONotifications_goodnessScore
+ _kMONotifications_hasJournalSchedule
+ _kMONotifications_interfaceType
+ _kMONotifications_numScheduledDays
+ _kMONotifications_onDefaultSchedule
+ _kMONotifications_postingDate
+ _kMONotifications_queuePostingLatency
+ _kMONotifications_recentOnboarding
+ _kMONotifications_scheduledDeliverySetting
+ _kMONotifications_subType
+ _kMONotifications_submissionTimeDay
+ _kMONotifications_submissionTimeHour
+ _kMONotifications_submissionTimeMinute
+ _kMONotifications_submissionTimeMonth
+ _kMONotifications_submissionTimeYear
+ _kMONotifications_suggestionCount
+ _kMONotifications_suggestionEndDateDay
+ _kMONotifications_suggestionEndDateHour
+ _kMONotifications_suggestionEndDateMonth
+ _kMONotifications_suggestionEndDateYear
+ _kMONotifications_suggestionID
+ _kMONotifications_suggestionNotificationLatency
+ _kMONotifications_superType
+ _kMONotifications_trigger
+ _kMOUsageContextNotificationPostTime
+ _kMOUsageContextNotificationSuggestionCount
+ _kMOUserNotificationBundleIdentifier
+ _objc_msgSend$_fetchRealTimeVisitsBetweenStartDate:EndDate:CompletionHandler:
+ _objc_msgSend$_fetchRealTimeVisitsForStartDate:CompletionHandler:
+ _objc_msgSend$_fetchSignificantLocationEnablementStatus
+ _objc_msgSend$_postNotificationWithTitle:message:defaultActionURL:notificationIdentifier:withIcon:usingTrigger:useSubordinateIcon:userInfo:handler:
+ _objc_msgSend$actionIdentifier
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$categoryWithIdentifier:actions:intentIdentifiers:options:
+ _objc_msgSend$createBundleInformationForAnalyticsWithBundle:
+ _objc_msgSend$determineAddedCharacterBinRange:
+ _objc_msgSend$determineOnboardingDurationBinRange
+ _objc_msgSend$fetchConsolidatedEvents:withStored:handler:
+ _objc_msgSend$getApplicationsWithDataAccess:
+ _objc_msgSend$getBiomeContextDictionaryWithUserInfo:
+ _objc_msgSend$getDeliveredNotificationsWithCompletionHandler:
+ _objc_msgSend$getNotificationScheduledDeliverySetting
+ _objc_msgSend$getPendingNotificationRequestsWithCompletionHandler:
+ _objc_msgSend$initWithNotificationEventTimestamp:notificationPostingTimestamp:notificationSuggestionCount:
+ _objc_msgSend$initWithType:timestamp:fullBundleOrderedSet:clientIdentifier:viewContainerName:viewVisibleTime:suggestionType:viewVisibleSuggestionsCount:viewTotalSuggestionsCount:notificationInfo:
+ _objc_msgSend$scheduledDeliverySetting
+ _objc_msgSend$setCategoryIdentifier:
+ _objc_msgSend$setNotificationCategories:
+ _objc_msgSend$setShouldBackgroundDefaultAction:
+ _objc_msgSend$setUserInfo:
+ _objc_msgSend$submitEngagementHistoryUpdateWithEvent:userInfo:
+ _objc_msgSend$submitNotificationEngagementEventAnalyticsForBundles:userInfo:fromTrigger:withPostingDate:
+ _unnamed_array_storage.1215
- -[MONotificationsManager _postNotificationWithTitle:message:defaultActionURL:notificationIdentifier:withIcon:usingTrigger:useSubordinateIcon:handler:]
- GCC_except_table106
- GCC_except_table127
- GCC_except_table137
- GCC_except_table38
- GCC_except_table48
- GCC_except_table64
- GCC_except_table74
- GCC_except_table92
- _$s8momentsd13MOWeatherDataC11temperature9windSpeed13weatherSummry10symbolNameAC10Foundation11MeasurementVySo17NSUnitTemperatureCG_AJySo0mF0CGS2StcfcTf4nnggn_n
- __101-[MONotificationsManager _getNewTargetTimeToWriteEventBundlesUsingAppSchedule:withCompletionHandler:]_block_invoke.501
- __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.421
- __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.421.cold.1
- __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.423
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.228
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.228.cold.1
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.234
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.234.cold.1
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.239
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.239.cold.1
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.239.cold.2
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.229
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.235
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.230
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.236
- __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.383
- __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.389
- __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.389.cold.1
- __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.390
- __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.366
- __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.369
- __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_2.367
- __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_3.368
- __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.351
- __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.357
- __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_2.353
- __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_3.355
- __125-[MONotificationsManager _postTimeToWriteSystemNotificationUsingEventBundles:withTrigger:usingAppSchedule:completionHandler:]_block_invoke.571
- __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.379
- __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.382
- __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_2.380
- __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_3.381
- __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.372
- __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.375
- __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_2.373
- __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_3.374
- __38-[MOEventManager storeEvents:handler:]_block_invoke.272
- __42-[MOBiomeManager donateEvents:andBundles:]_block_invoke.1135
- __44-[MOEventManager _purgePreOnboardingEvents:]_block_invoke.451
- __44-[MOEventManager _purgePreOnboardingEvents:]_block_invoke.452
- __47-[MOEventManager _rehydrateEvents:withHandler:]_block_invoke.314
- __48-[MOEventManager _updateEventsDeletedAtSources:]_block_invoke.419
- __48-[MOEventManager _updateEventsDeletedAtSources:]_block_invoke.420
- __49-[MOBiomeManager _updateDataStreamWithEngagement]_block_invoke.1149
- __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.123
- __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.123.cold.1
- __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.123.cold.2
- __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.124
- __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.124.cold.1
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.321
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.325
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.329
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.339
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.349
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.353
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.357
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.361
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.365
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.369
- __59-[MOEventManager fetchEventsWithOptions:CompletionHandler:]_block_invoke.279
- __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.283
- __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.284
- __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.285
- __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.462
- __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.478
- __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.478.cold.1
- __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.427
- __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.431
- __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.435
- __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.439
- __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.443
- __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.447
- __61-[MOEventManager cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.373
- __61-[MOHealthKitManager _updateWorkoutsDeletedAtSource:handler:]_block_invoke.125
- __61-[MOHealthKitManager _updateWorkoutsDeletedAtSource:handler:]_block_invoke.125.cold.1
- __61-[MOHealthKitManager _updateWorkoutsDeletedAtSource:handler:]_block_invoke.128
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.386
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.386.cold.1
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.390
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.397
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.397.cold.1
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.404
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.404.cold.1
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.408
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.408.cold.1
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.412
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.412.cold.1
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.413
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.413.cold.1
- __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.1160
- __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.1170
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.246
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.247
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.248
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.252
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.253
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.257
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.261
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.262
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.263
- __66-[MOHealthKitManager _rehydrateStoredEvents:fromWorkouts:handler:]_block_invoke.122
- __69-[MOBiomeManager fetchMomentsEngagementForBundles:CompletionHandler:]_block_invoke.1153
- __71-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterOnboarding]_block_invoke.196
- __71-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterOnboarding]_block_invoke_2.197
- __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.206
- __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.208
- __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.209
- __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.209.cold.1
- __75-[MOHealthKitManager fetchAndSaveWorkoutsBetweenStartDate:EndDate:handler:]_block_invoke.129
- __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke.387
- __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke.393
- __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke_2.388
- __82-[MOBiomeManager fetchMomentsEventDataBetweenStartDate:EndDate:CompletionHandler:]_block_invoke.1155
- __82-[MOHealthKitManager fetchAndSaveMindfulSessionsBetweenStartDate:EndDate:handler:]_block_invoke.130
- __84-[MOEventManager _fetchEventsFromDBAndRehydrateEventsWithOptions:CompletionHandler:]_block_invoke.293
- __88-[MORoutineServiceManager _fetchFamiliarityIndexesLOIForDateInterval:CompletionHandler:]_block_invoke.159
- __88-[MORoutineServiceManager _fetchFamiliarityIndexesLOIForDateInterval:CompletionHandler:]_block_invoke.159.cold.1
- __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.446
- __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.446.cold.1
- __89-[MORoutineServiceManager _fetchVisitsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.198
- __89-[MORoutineServiceManager _fetchVisitsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.199
- __89-[MORoutineServiceManager _fetchVisitsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.199.cold.1
- __91-[MOHealthKitManager _fetchWorkoutEventsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.155
- __ZNKSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB7v160006Ev
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__113__nth_elementB7v160006INS_17_ClassicAlgPolicyERNS_6__lessIddEENS_11__wrap_iterIPdEEEEvT1_S8_S8_T0_
- __ZNSt3__116__selection_sortB7v160006INS_17_ClassicAlgPolicyERNS_6__lessIddEENS_11__wrap_iterIPdEEEEvT1_S8_T0_
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZNSt3__17__sort3B7v160006INS_17_ClassicAlgPolicyERNS_6__lessIddEENS_11__wrap_iterIPdEEEEjT1_S8_S8_T0_
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___78-[MOOnboardingAndSettingsPersistence fetchSignificantLocationEnablementStatus]_block_invoke
- ___block_descriptor_104_e8_32s40s48s56s64s72bs80r88r96r_e5_v8?0lr80l8s32l8s72l8s40l8r88l8r96l8s48l8s56l8s64l8
- ___block_descriptor_120_e8_32s40s48s56s64s72s80s88r96r104r112r_e5_v8?0ls32l8r88l8r96l8s40l8s48l8s56l8s64l8r104l8r112l8s72l8s80l8
- ___block_descriptor_48_e8_32s40r_e20_v24?0q8"NSError"16lr40l8s32l8
- ___block_descriptor_57_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
- ___block_descriptor_96_e8_32s40s48s56s64r72r80r88r_e34_v24?0"NSError"8"NSDictionary"16ls32l8r64l8r72l8r80l8r88l8s40l8s48l8s56l8
- __block_literal_global.315
- __block_literal_global.317
- __block_literal_global.319
- __block_literal_global.349
- __block_literal_global.361
- __block_literal_global.371
- __block_literal_global.384
- __block_literal_global.386
- _objc_msgSend$_postNotificationWithTitle:message:defaultActionURL:notificationIdentifier:withIcon:usingTrigger:useSubordinateIcon:handler:
- _objc_msgSend$initWithType:timestamp:fullBundleOrderedSet:clientIdentifier:viewContainerName:viewVisibleTime:suggestionType:viewVisibleSuggestionsCount:viewTotalSuggestionsCount:
- _objc_msgSend$internalInstall
- _unnamed_array_storage.1185
CStrings:
+ "\x01\x113"
+ "%@, PAH home visit idx, %lu, startDate, %@, endDate, %@"
+ "%@, event.id, %@, loi, %@, mapItem, %@, mapItem.length, %lu, placeType, %@, mapItemPlaceType, %@, userType, %lu, name, %@, category, %@, source, %lu, wifiLabelType, %lu, confidence, %f, isPreOnboardedVisit, %d, distanceFromVisitToPlace, %f, timezone, %@"
+ "%@,TAH home visit idx, %lu, startDate, %@, endDate, %@"
+ "%K != %lu"
+ "(endDate == %@)"
+ "(startDate < %@)"
+ "(startDate == %@)"
+ "(type == %lu)"
+ "@max.endDate"
+ "@max.startDate"
+ "AnalyticsOverrideAppUsageLookbackWindow"
+ "Checking RT state..."
+ "JOURNALING_SCHEDULE"
+ "JOURNALING_SCHEDULE_DETAIL"
+ "JournalAppSettingsUtilities"
+ "LOCK_JOURNAL"
+ "Notification analytics submitted: %{private}@"
+ "NotificationDequeued"
+ "NotificationDismissed"
+ "NotificationOverride"
+ "NotificationPosted"
+ "NotificationQueued"
+ "NotificationTapped"
+ "Number of delivered notifications in NotificationCenter currently: %@"
+ "Number of hindsight home events, %lu"
+ "Number of real time home events that are stored, %lu"
+ "Number of real time home events, %lu"
+ "Number of real time new home events to be deleted is , %lu"
+ "Onboarding bin %@, for onboarding time since now: %@"
+ "REQUIRE_PASSCODE"
+ "Received RT state response with state: %@ and error: %@"
+ "RoutineManagerFetchEventsfetchRealTimeVisit"
+ "SAVE_TO_PHOTOS"
+ "SKIP_JOURNALING_SUGGESTIONS"
+ "T@\"MOEngagementHistoryManager\",R,N,V_engagementHistoryManager"
+ "T@\"NSString\",?,R,C"
+ "Updated RT state: %@"
+ "User onboarding date is nil, keeping duration bin as Unknown"
+ "UserNotification getPendingNotificationRequest timed-out for analytics"
+ "UserNotificationLastDeliveredID"
+ "_cachedRoutineState"
+ "_cachedRoutineStateTimestamp"
+ "_fetchRealTimeVisitsBetweenStartDate:EndDate:CompletionHandler:"
+ "_fetchRealTimeVisitsForStartDate:CompletionHandler:"
+ "_fetchSignificantLocationEnablementStatus"
+ "_postNotificationWithTitle:message:defaultActionURL:notificationIdentifier:withIcon:usingTrigger:useSubordinateIcon:userInfo:handler:"
+ "actionIdentifier"
+ "addedCharactersBinned"
+ "analyticsDict"
+ "appIsJournalAppUsed"
+ "appOtherJournalAppUsed"
+ "boolForKey:"
+ "categoryWithIdentifier:actions:intentIdentifiers:options:"
+ "com.apple.Moments.Notifications"
+ "com.apple.health.workout.event.create"
+ "com.apple.health.workout.rehydrate"
+ "com.apple.health.workout.route.fetch"
+ "createBundleInformationForAnalyticsWithBundle:"
+ "determineAddedCharacterBinRange:"
+ "determineOnboardingDurationBinRange"
+ "engagementLatency"
+ "fetchConsolidatedEvents:withStored:handler:"
+ "fetchRealTimeVisit"
+ "fetchRealTimeVisit failed with error, %@"
+ "fetchRealTimestoredVisits returned visits count, %lu"
+ "getBiomeContextDictionaryWithUserInfo:"
+ "getDeliveredNotificationsWithCompletionHandler:"
+ "getNotificationScheduledDeliverySetting"
+ "getPendingNotificationRequestsWithCompletionHandler:"
+ "goodnessScore"
+ "group.com.apple.Journal"
+ "hasJournalSchedule"
+ "initWithNotificationEventTimestamp:notificationPostingTimestamp:notificationSuggestionCount:"
+ "initWithType:timestamp:fullBundleOrderedSet:clientIdentifier:viewContainerName:viewVisibleTime:suggestionType:viewVisibleSuggestionsCount:viewTotalSuggestionsCount:notificationInfo:"
+ "isOnDefaultNotificationSchedule"
+ "journalConfigLockJournal"
+ "journalConfigSkipSuggestions"
+ "journalIsInstalled"
+ "notificationEventTrigger"
+ "numScheduledDays"
+ "numSuggestionInNotification"
+ "onboardingDurationBin"
+ "postingDate"
+ "queuePostingLatency"
+ "recentOnboarding"
+ "scheduledDeliverySetting"
+ "setBool:forKey:"
+ "setCategoryIdentifier:"
+ "setNotificationCategories:"
+ "setShouldBackgroundDefaultAction:"
+ "setUserInfo:"
+ "settingsBundle"
+ "settingsDefaults"
+ "subType"
+ "submit Notification engagement using userInfo for suggID: %@"
+ "submitEngagementHistoryUpdateWithEvent:userInfo:"
+ "submitNotificationEngagementEventAnalyticsForBundles:userInfo:fromTrigger:withPostingDate:"
+ "suggestionEndDateDay"
+ "suggestionEndDateHour"
+ "suggestionEndDateMonth"
+ "suggestionEndDateYear"
+ "suggestionNotificationDequeued"
+ "suggestionNotificationDismissed"
+ "suggestionNotificationLatency"
+ "suggestionNotificationOverriden"
+ "suggestionNotificationPosted"
+ "suggestionNotificationQueued"
+ "suggestionNotificationTapped"
+ "superType"
+ "trigger.nextTriggerDate: %@"
+ "v28@0:8B16@20"
+ "v48@0:8@16@24Q32@40"
+ "v84@0:8@16@24@32@40@48@56B64@68@?76"
- "\x01\x11\x13"
- "%@, event.id, %@, loi, %@, mapItem, %@, mapItem.length, %lu, placeType, %@, mapItemPlaceType, %@, userType, %lu, name, %@, category, %@, source, %lu, wifiLabelType, %lu, confidence, %f, isPreOnboardedVisit,%d, distanceFromVisitToPlace, %f, timezone, %@"
- "%@, home visit idx, %lu, startDate, %@, endDate, %@"
- "Bundle is not available"
- "MOEventBundleLabelLocalizer localizedString is not found, key, %@, value, %@, tag, %@, defaultLanguageBundle, %@, defaultLocalizedString, %@"
- "Waiting for translation"
- "_postNotificationWithTitle:message:defaultActionURL:notificationIdentifier:withIcon:usingTrigger:useSubordinateIcon:handler:"
- "initWithType:timestamp:fullBundleOrderedSet:clientIdentifier:viewContainerName:viewVisibleTime:suggestionType:viewVisibleSuggestionsCount:viewTotalSuggestionsCount:"
- "v76@0:8@16@24@32@40@48@56B64@?68"

```
