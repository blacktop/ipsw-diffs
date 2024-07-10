## AppPredictionInternal

> `/System/Library/PrivateFrameworks/AppPredictionInternal.framework/Versions/A/AppPredictionInternal`

```diff

-569.0.1.0.0
-  __TEXT.__text: 0x47ecb8
-  __TEXT.__auth_stubs: 0x2d70
-  __TEXT.__objc_methlist: 0x3549c
-  __TEXT.__const: 0x2702
-  __TEXT.__cstring: 0x55d12
-  __TEXT.__oslogstring: 0x37876
-  __TEXT.__gcc_except_tab: 0xec60
+571.0.3.0.0
+  __TEXT.__text: 0x47fedc
+  __TEXT.__auth_stubs: 0x2dc0
+  __TEXT.__objc_methlist: 0x35574
+  __TEXT.__const: 0x2782
+  __TEXT.__cstring: 0x563f2
+  __TEXT.__oslogstring: 0x378e6
+  __TEXT.__gcc_except_tab: 0xec88
   __TEXT.__dlopen_cstrs: 0x10a
-  __TEXT.__swift5_typeref: 0xd14
-  __TEXT.__constg_swiftt: 0x14c8
-  __TEXT.__swift5_reflstr: 0x62b
-  __TEXT.__swift5_fieldmd: 0x948
-  __TEXT.__swift5_proto: 0xc4
-  __TEXT.__swift5_types: 0x110
+  __TEXT.__swift5_typeref: 0xd48
+  __TEXT.__constg_swiftt: 0x1504
+  __TEXT.__swift5_reflstr: 0x65b
+  __TEXT.__swift5_fieldmd: 0x970
+  __TEXT.__swift5_proto: 0xc8
+  __TEXT.__swift5_types: 0x118
   __TEXT.__swift5_assocty: 0x1c8
-  __TEXT.__swift5_capture: 0x35c
+  __TEXT.__swift5_capture: 0x380
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xd2b0
-  __TEXT.__eh_frame: 0x198c
+  __TEXT.__unwind_info: 0xd340
+  __TEXT.__eh_frame: 0x1a9c
   __TEXT.__objc_classname: 0x899f
-  __TEXT.__objc_methname: 0xa98ed
-  __TEXT.__objc_methtype: 0x190e6
-  __TEXT.__objc_stubs: 0x4a260
-  __DATA_CONST.__got: 0x33b8
-  __DATA_CONST.__const: 0x40b8
-  __DATA_CONST.__objc_classlist: 0x1e88
+  __TEXT.__objc_methname: 0xa9c1c
+  __TEXT.__objc_methtype: 0x1913a
+  __TEXT.__objc_stubs: 0x4a480
+  __DATA_CONST.__got: 0x33c0
+  __DATA_CONST.__const: 0x40f8
+  __DATA_CONST.__objc_classlist: 0x1e90
   __DATA_CONST.__objc_catlist: 0x120
   __DATA_CONST.__objc_protolist: 0x490
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ad98
+  __DATA_CONST.__objc_selrefs: 0x1ae38
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x14a8
   __DATA_CONST.__objc_arraydata: 0x1208
-  __AUTH_CONST.__auth_got: 0x16d0
-  __AUTH_CONST.__auth_ptr: 0x478
-  __AUTH_CONST.__const: 0xef98
-  __AUTH_CONST.__cfstring: 0x38f00
-  __AUTH_CONST.__objc_const: 0x83620
-  __AUTH_CONST.__objc_intobj: 0x33c0
+  __AUTH_CONST.__auth_got: 0x16f8
+  __AUTH_CONST.__auth_ptr: 0x490
+  __AUTH_CONST.__const: 0xefe8
+  __AUTH_CONST.__cfstring: 0x39120
+  __AUTH_CONST.__objc_const: 0x83898
+  __AUTH_CONST.__objc_intobj: 0x33a8
   __AUTH_CONST.__objc_arrayobj: 0x1008
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH.__objc_data: 0x13528
-  __AUTH.__data: 0x1d38
-  __DATA.__objc_ivar: 0x4940
-  __DATA.__data: 0x3d20
-  __DATA.__bss: 0x2428
+  __AUTH.__data: 0x1dd8
+  __DATA.__objc_ivar: 0x4960
+  __DATA.__data: 0x3d50
+  __DATA.__bss: 0x24b8
   __DATA.__common: 0xb8
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 23870
-  Symbols:   50708
-  CStrings:  8545
+  Functions: 23913
+  Symbols:   50776
+  CStrings:  8577
 
Symbols:
+ +[_ATXInternalInstallNotification _installedAppsWithDatesFromNotificationData:]
+ -[ATXNotificationTelemetryQueryResult isDeliveredInPrioritySection]
+ -[ATXNotificationTelemetryQueryResult isDeterminedUrgentByModel]
+ -[ATXNotificationTelemetryQueryResult isPartOfStack]
+ -[ATXNotificationTelemetryQueryResult isStackSummary]
+ -[ATXNotificationTelemetryQueryResult isSummarized]
+ -[ATXNotificationTelemetryQueryResult setIsDeliveredInPrioritySection:]
+ -[ATXNotificationTelemetryQueryResult setIsDeterminedUrgentByModel:]
+ -[ATXNotificationTelemetryQueryResult setIsPartOfStack:]
+ -[ATXNotificationTelemetryQueryResult setIsStackSummary:]
+ -[ATXNotificationTelemetryQueryResult setIsSummarized:]
+ -[ATXNotificationTelemetryQueryResult setSubtitleLength:]
+ -[ATXNotificationTelemetryQueryResult setSummaryLength:]
+ -[ATXNotificationTelemetryQueryResult setTitleLength:]
+ -[ATXNotificationTelemetryQueryResult subtitleLength]
+ -[ATXNotificationTelemetryQueryResult summaryLength]
+ -[ATXNotificationTelemetryQueryResult titleLength]
+ -[ATXNotificationsLoggingServer logNotificationEvent:notification:reason:interactionUI:]
+ -[ATXSettingsActionsServer _suggestedActionsWithRequest:]
+ -[ATXSleepSuggestionServer predictedSleepSuggestionWithCompletionHandler:].cold.9
+ -[ATXUserNotificationBiomeStream sendEvent:notification:deliveryReason:interactionUI:]
+ -[_ATXAppPredictor _initDependencies]
+ -[_ATXAppPredictor _initDependencies].cold.1
+ OBJC_IVAR_$_ATXNotificationTelemetryQueryResult._isDeliveredInPrioritySection
+ OBJC_IVAR_$_ATXNotificationTelemetryQueryResult._isDeterminedUrgentByModel
+ OBJC_IVAR_$_ATXNotificationTelemetryQueryResult._isPartOfStack
+ OBJC_IVAR_$_ATXNotificationTelemetryQueryResult._isStackSummary
+ OBJC_IVAR_$_ATXNotificationTelemetryQueryResult._isSummarized
+ OBJC_IVAR_$_ATXNotificationTelemetryQueryResult._subtitleLength
+ OBJC_IVAR_$_ATXNotificationTelemetryQueryResult._summaryLength
+ OBJC_IVAR_$_ATXNotificationTelemetryQueryResult._titleLength
+ OBJC_IVAR_$__ATXAppPredictor._dependenciesAreInitialized
+ _OBJC_CLASS_$_ATXSettingsActionsClientRequest
+ __110-[ATXNotificationAndSuggestionDatabase hasSuggestionBeenShownForEntityId:suggestionType:scope:sinceTimestamp:]_block_invoke.102
+ __110-[ATXNotificationAndSuggestionDatabase hasSuggestionBeenShownForEntityId:suggestionType:scope:sinceTimestamp:]_block_invoke_2.104
+ __110-[ATXNotificationAndSuggestionDatabase hasSuggestionBeenShownForEntityId:suggestionType:scope:sinceTimestamp:]_block_invoke_2.104.cold.1
+ __112-[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationWithBundleId:notificationId:recordTimestamp:]_block_invoke.374
+ __112-[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationWithBundleId:notificationId:recordTimestamp:]_block_invoke.374.cold.1
+ __113-[ATXNotificationAndSuggestionDatabase getSmartPauseFeaturesForBundleIds:sinceTimestamp:positiveEngagementEnums:]_block_invoke.188
+ __113-[ATXNotificationAndSuggestionDatabase getSmartPauseFeaturesForBundleIds:sinceTimestamp:positiveEngagementEnums:]_block_invoke_2.200
+ __113-[ATXNotificationAndSuggestionDatabase getSmartPauseFeaturesForBundleIds:sinceTimestamp:positiveEngagementEnums:]_block_invoke_2.200.cold.1
+ __113-[ATXNotificationAndSuggestionDatabase insertNotificationFromEvent:deliveryMethod:modeIdentifier:deliveryReason:]_block_invoke.72
+ __113-[ATXNotificationAndSuggestionDatabase insertNotificationFromEvent:deliveryMethod:modeIdentifier:deliveryReason:]_block_invoke.72.cold.1
+ __114-[ATXNotificationAndSuggestionDatabase engagementStatusOfActiveAndProminentAndMessageNotificationsSinceTimestamp:]_block_invoke.126
+ __114-[ATXNotificationAndSuggestionDatabase engagementStatusOfActiveAndProminentAndMessageNotificationsSinceTimestamp:]_block_invoke.126.cold.1
+ __116-[ATXNotificationAndSuggestionDatabase engagementStatusOfActiveAndProminentNotificationsWithUrgency:sinceTimestamp:]_block_invoke.123
+ __116-[ATXNotificationAndSuggestionDatabase engagementStatusOfActiveAndProminentNotificationsWithUrgency:sinceTimestamp:]_block_invoke.123.cold.1
+ __200-[_ATXAppPredictor predictWithLimit:consumerSubType:intent:candidateBundleIdentifiers:candidateActiontypes:scoreLogger:predictionItemsToKeep:predictedItemsOutParameter:context:datastore:featureCache:]_block_invoke.153
+ __47-[ATXNotificationAndSuggestionDatabase analyze]_block_invoke.335
+ __47-[ATXNotificationAndSuggestionDatabase analyze]_block_invoke.335.cold.1
+ __53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.275
+ __53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.275.cold.1
+ __53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.276
+ __53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.276.cold.1
+ __63-[ATXSleepSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.50
+ __63-[ATXSleepSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.50.cold.1
+ __64-[ATXNotificationAndSuggestionDatabase currentActiveSuggestions]_block_invoke.174
+ __64-[ATXNotificationAndSuggestionDatabase currentActiveSuggestions]_block_invoke.174.cold.1
+ __68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke.75
+ __68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke.79
+ __68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke.79.cold.1
+ __68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke_2.76
+ __69-[ATXNotificationAndSuggestionDatabase mostRecentActiveNotifications]_block_invoke.140
+ __69-[ATXNotificationAndSuggestionDatabase mostRecentActiveNotifications]_block_invoke.140.cold.1
+ __79-[ATXNotificationAndSuggestionDatabase allBundleIdsOfNotificationsOnLockscreen]_block_invoke.272
+ __79-[ATXNotificationAndSuggestionDatabase allBundleIdsOfNotificationsOnLockscreen]_block_invoke.272.cold.1
+ __84-[ATXNotificationAndSuggestionDatabase allNotificationsFromBundleId:sinceTimestamp:]_block_invoke.263
+ __84-[ATXNotificationAndSuggestionDatabase allNotificationsFromBundleId:sinceTimestamp:]_block_invoke.263.cold.1
+ __84-[ATXNotificationAndSuggestionDatabase updateNotificationUIForNotifications:nextUI:]_block_invoke.85
+ __84-[ATXNotificationAndSuggestionDatabase updateNotificationUIForNotifications:nextUI:]_block_invoke.85.cold.1
+ __88-[ATXNotificationAndSuggestionDatabase _countNotificationsPerAppWithFilters:stmtBinder:]_block_invoke.226
+ __88-[ATXNotificationAndSuggestionDatabase _countNotificationsPerAppWithFilters:stmtBinder:]_block_invoke_2.227
+ __88-[ATXNotificationAndSuggestionDatabase _countNotificationsPerAppWithFilters:stmtBinder:]_block_invoke_2.227.cold.1
+ __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke.311
+ __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke.320
+ __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke.327
+ __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.329
+ __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.329.cold.1
+ __91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke.288
+ __91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke.294
+ __91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.296
+ __91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.296.cold.1
+ __96-[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationsFromTimestamp:endTimestamp:]_block_invoke.368
+ __96-[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationsFromTimestamp:endTimestamp:]_block_invoke.368.cold.1
+ __97-[ATXNotificationAndSuggestionDatabase allNotificationsBetweenStartTimestamp:endTimestamp:limit:]_block_invoke.207
+ __97-[ATXNotificationAndSuggestionDatabase allNotificationsBetweenStartTimestamp:endTimestamp:limit:]_block_invoke_2.208
+ __97-[ATXNotificationAndSuggestionDatabase allNotificationsBetweenStartTimestamp:endTimestamp:limit:]_block_invoke_2.208.cold.1
+ __99-[ATXNotificationAndSuggestionDatabase prepAndRunQuery:batchSize:XPCActivity:onPrep:onRow:onError:]_block_invoke.302
+ __Block_byref_object_copy_.143
+ __Block_byref_object_dispose_.144
+ __DATA__TtCC21AppPredictionInternal28ContextualEngineContextStoreP33_1731BDF3B55A79F3801A90F52E5A9D7411GuardedData
+ __IVARS__TtCC21AppPredictionInternal28ContextualEngineContextStoreP33_1731BDF3B55A79F3801A90F52E5A9D7411GuardedData
+ __METACLASS_DATA__TtCC21AppPredictionInternal28ContextualEngineContextStoreP33_1731BDF3B55A79F3801A90F52E5A9D7411GuardedData
+ ___37-[_ATXAppPredictor _initDependencies]_block_invoke
+ ___57-[ATXSettingsActionsServer _suggestedActionsWithRequest:]_block_invoke
+ ___76-[_ATXInternalInstallNotification registerForNotificationsWithInstallBlock:]_block_invoke
+ ___79+[_ATXInternalInstallNotification _installedAppsWithDatesFromNotificationData:]_block_invoke
+ ___ATXInitializeInOwnerProcess_block_invoke.387
+ ___ATXInitializeInOwnerProcess_block_invoke.398
+ ___ATXInitializeInOwnerProcess_block_invoke_2.394
+ ___ATXInitializeInOwnerProcess_block_invoke_2.394.cold.1
+ __block_literal_global.213
+ __block_literal_global.269
+ __block_literal_global.274
+ __block_literal_global.298
+ __block_literal_global.316
+ __block_literal_global.337
+ __block_literal_global.389
+ __block_literal_global.396
+ __block_literal_global.400
+ __block_literal_global.404
+ __block_literal_global.407
+ __block_literal_global.409
+ __block_literal_global.412
+ __block_literal_global.416
+ __block_literal_global.418
+ __block_literal_global.421
+ __block_literal_global.424
+ __block_literal_global.428
+ __block_literal_global.431
+ __block_literal_global.436
+ __block_literal_global.440
+ __block_literal_global.444
+ __block_literal_global.448
+ __block_literal_global.452
+ __block_literal_global.458
+ __block_literal_global.464
+ __block_literal_global.469
+ __block_literal_global.473
+ __block_literal_global.484
+ __block_literal_global.490
+ __block_literal_global.495
+ __block_literal_global.498
+ __block_literal_global.513
+ __block_literal_global.519
+ __block_literal_global.523
+ __block_literal_global.527
+ __block_literal_global.532
+ __block_literal_global.536
+ __block_literal_global.542
+ __block_literal_global.546
+ __block_literal_global.550
+ __block_literal_global.553
+ __block_literal_global.558
+ __block_literal_global.561
+ __block_literal_global.564
+ __block_literal_global.567
+ __block_literal_global.570
+ __block_literal_global.574
+ __block_literal_global.578
+ __registerForDailyRoutinesCTSJob_block_invoke.419
+ __registerForEverydayShortcutsTriggersCTSJobs_block_invoke.414
+ __registerForNotificationAndSuggestionDatastorePruning_block_invoke.556
+ _kATXNotificationDeliveredInPrioritySection
+ _kATXNotificationIsDeterminedUrgentByModel
+ _kATXNotificationIsPartOfStack
+ _kATXNotificationIsStackSummary
+ _kATXNotificationIsSummarized
+ _kATXSleepSchedulePredictedBedTimeDateComponent
+ _kATXUserNotificationSubtitleLength
+ _kATXUserNotificationSummaryLength
+ _kATXUserNotificationTitleLength
+ _objc_msgSend$_initDependencies
+ _objc_msgSend$_installedAppsWithDatesFromNotificationData:
+ _objc_msgSend$_suggestedActionsWithRequest:
+ _objc_msgSend$initFromUserNotification:eventType:timestamp:deliveryReason:deliveryUI:
+ _objc_msgSend$isDeliveredInPrioritySection
+ _objc_msgSend$isDeterminedUrgentByModel
+ _objc_msgSend$isPartOfStack
+ _objc_msgSend$isStackSummary
+ _objc_msgSend$isSummarized
+ _objc_msgSend$publisherWithOptions:
+ _objc_msgSend$sendEvent:notification:deliveryReason:interactionUI:
+ _objc_msgSend$setIsDeliveredInPrioritySection:
+ _objc_msgSend$setIsDeterminedUrgentByModel:
+ _objc_msgSend$setIsPartOfStack:
+ _objc_msgSend$setIsStackSummary:
+ _objc_msgSend$setIsSummarized:
+ _objc_msgSend$setSubtitleLength:
+ _objc_msgSend$setSummaryLength:
+ _objc_msgSend$setTitleLength:
+ _objc_msgSend$subtitleLength
+ _objc_msgSend$summaryLength
+ _objc_msgSend$titleLength
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _swift_defaultActor_initialize
+ _swift_getAtKeyPath
+ _swift_getKeyPath
+ _symbolic BD
+ _symbolic _____ 21AppPredictionInternal28ContextualEngineContextStoreC11GuardedData33_1731BDF3B55A79F3801A90F52E5A9D74LLC
+ _symbolic ______pSg 21AppPredictionInternal36ContextualEngineContextStoreDelegateP
+ _symbolic _____y_____G 2os21OSAllocatedUnfairLockV 21AppPredictionInternal28ContextualEngineContextStoreC11GuardedData33_1731BDF3B55A79F3801A90F52E5A9D74LLC
+ _symbolic _____y__________G s13ManagedBufferCsRi__rlE 21AppPredictionInternal28ContextualEngineContextStoreC11GuardedData33_1731BDF3B55A79F3801A90F52E5A9D74LLC So16os_unfair_lock_sV
+ block_copy_helper.31
+ block_copy_helper.35
+ block_descriptor.33
+ block_descriptor.37
+ block_destroy_helper.32
+ block_destroy_helper.36
- -[ATXUserNotificationBiomeStream sendEvent:notification:deliveryReason:]
- -[_ATXAppPredictor _initIOSOnlyDependencies]
- -[_ATXAppPredictor _initIOSOnlyDependencies].cold.1
- OBJC_IVAR_$__ATXAppPredictor._iOSOnlyDependenciesInitialized
- __110-[ATXNotificationAndSuggestionDatabase hasSuggestionBeenShownForEntityId:suggestionType:scope:sinceTimestamp:]_block_invoke.94
- __110-[ATXNotificationAndSuggestionDatabase hasSuggestionBeenShownForEntityId:suggestionType:scope:sinceTimestamp:]_block_invoke_2.96
- __110-[ATXNotificationAndSuggestionDatabase hasSuggestionBeenShownForEntityId:suggestionType:scope:sinceTimestamp:]_block_invoke_2.96.cold.1
- __112-[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationWithBundleId:notificationId:recordTimestamp:]_block_invoke.358
- __112-[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationWithBundleId:notificationId:recordTimestamp:]_block_invoke.358.cold.1
- __113-[ATXNotificationAndSuggestionDatabase getSmartPauseFeaturesForBundleIds:sinceTimestamp:positiveEngagementEnums:]_block_invoke.180
- __113-[ATXNotificationAndSuggestionDatabase getSmartPauseFeaturesForBundleIds:sinceTimestamp:positiveEngagementEnums:]_block_invoke_2.192
- __113-[ATXNotificationAndSuggestionDatabase getSmartPauseFeaturesForBundleIds:sinceTimestamp:positiveEngagementEnums:]_block_invoke_2.192.cold.1
- __113-[ATXNotificationAndSuggestionDatabase insertNotificationFromEvent:deliveryMethod:modeIdentifier:deliveryReason:]_block_invoke.64
- __113-[ATXNotificationAndSuggestionDatabase insertNotificationFromEvent:deliveryMethod:modeIdentifier:deliveryReason:]_block_invoke.64.cold.1
- __114-[ATXNotificationAndSuggestionDatabase engagementStatusOfActiveAndProminentAndMessageNotificationsSinceTimestamp:]_block_invoke.118
- __114-[ATXNotificationAndSuggestionDatabase engagementStatusOfActiveAndProminentAndMessageNotificationsSinceTimestamp:]_block_invoke.118.cold.1
- __116-[ATXNotificationAndSuggestionDatabase engagementStatusOfActiveAndProminentNotificationsWithUrgency:sinceTimestamp:]_block_invoke.115
- __116-[ATXNotificationAndSuggestionDatabase engagementStatusOfActiveAndProminentNotificationsWithUrgency:sinceTimestamp:]_block_invoke.115.cold.1
- __200-[_ATXAppPredictor predictWithLimit:consumerSubType:intent:candidateBundleIdentifiers:candidateActiontypes:scoreLogger:predictionItemsToKeep:predictedItemsOutParameter:context:datastore:featureCache:]_block_invoke.154
- __47-[ATXNotificationAndSuggestionDatabase analyze]_block_invoke.327
- __47-[ATXNotificationAndSuggestionDatabase analyze]_block_invoke.327.cold.1
- __53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.267
- __53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.267.cold.1
- __53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.268
- __53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.268.cold.1
- __53-[_ATXInternalNotification registerForNotifications:]_block_invoke.25
- __63-[ATXSleepSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.48
- __63-[ATXSleepSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.48.cold.1
- __64-[ATXNotificationAndSuggestionDatabase currentActiveSuggestions]_block_invoke.166
- __64-[ATXNotificationAndSuggestionDatabase currentActiveSuggestions]_block_invoke.166.cold.1
- __68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke.67
- __68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke.71
- __68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke.71.cold.1
- __68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke_2.68
- __69-[ATXNotificationAndSuggestionDatabase mostRecentActiveNotifications]_block_invoke.132
- __69-[ATXNotificationAndSuggestionDatabase mostRecentActiveNotifications]_block_invoke.132.cold.1
- __79-[ATXNotificationAndSuggestionDatabase allBundleIdsOfNotificationsOnLockscreen]_block_invoke.264
- __79-[ATXNotificationAndSuggestionDatabase allBundleIdsOfNotificationsOnLockscreen]_block_invoke.264.cold.1
- __84-[ATXNotificationAndSuggestionDatabase allNotificationsFromBundleId:sinceTimestamp:]_block_invoke.255
- __84-[ATXNotificationAndSuggestionDatabase allNotificationsFromBundleId:sinceTimestamp:]_block_invoke.255.cold.1
- __84-[ATXNotificationAndSuggestionDatabase updateNotificationUIForNotifications:nextUI:]_block_invoke.77
- __84-[ATXNotificationAndSuggestionDatabase updateNotificationUIForNotifications:nextUI:]_block_invoke.77.cold.1
- __88-[ATXNotificationAndSuggestionDatabase _countNotificationsPerAppWithFilters:stmtBinder:]_block_invoke.218
- __88-[ATXNotificationAndSuggestionDatabase _countNotificationsPerAppWithFilters:stmtBinder:]_block_invoke_2.219
- __88-[ATXNotificationAndSuggestionDatabase _countNotificationsPerAppWithFilters:stmtBinder:]_block_invoke_2.219.cold.1
- __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke.303
- __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke.312
- __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke.319
- __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.313
- __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.313.cold.1
- __91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke.280
- __91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke.286
- __91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.288
- __91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.288.cold.1
- __96-[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationsFromTimestamp:endTimestamp:]_block_invoke.352
- __96-[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationsFromTimestamp:endTimestamp:]_block_invoke.352.cold.1
- __97-[ATXNotificationAndSuggestionDatabase allNotificationsBetweenStartTimestamp:endTimestamp:limit:]_block_invoke.199
- __97-[ATXNotificationAndSuggestionDatabase allNotificationsBetweenStartTimestamp:endTimestamp:limit:]_block_invoke_2.200
- __97-[ATXNotificationAndSuggestionDatabase allNotificationsBetweenStartTimestamp:endTimestamp:limit:]_block_invoke_2.200.cold.1
- __99-[ATXNotificationAndSuggestionDatabase prepAndRunQuery:batchSize:XPCActivity:onPrep:onRow:onError:]_block_invoke.294
- __Block_byref_object_copy_.144
- __Block_byref_object_dispose_.145
- ___44-[_ATXAppPredictor _initIOSOnlyDependencies]_block_invoke
- ___53-[_ATXInternalNotification registerForNotifications:]_block_invoke_2
- ___74-[ATXSettingsActionsServer suggestedActionsWithRequest:completionHandler:]_block_invoke
- ___ATXInitializeInOwnerProcess_block_invoke.388
- ___ATXInitializeInOwnerProcess_block_invoke.399
- ___ATXInitializeInOwnerProcess_block_invoke_2.395
- ___ATXInitializeInOwnerProcess_block_invoke_2.395.cold.1
- __block_literal_global.149
- __block_literal_global.155
- __block_literal_global.205
- __block_literal_global.261
- __block_literal_global.290
- __block_literal_global.308
- __block_literal_global.315
- __block_literal_global.329
- __block_literal_global.390
- __block_literal_global.397
- __block_literal_global.401
- __block_literal_global.405
- __block_literal_global.408
- __block_literal_global.410
- __block_literal_global.413
- __block_literal_global.417
- __block_literal_global.419
- __block_literal_global.422
- __block_literal_global.425
- __block_literal_global.429
- __block_literal_global.432
- __block_literal_global.437
- __block_literal_global.441
- __block_literal_global.445
- __block_literal_global.449
- __block_literal_global.453
- __block_literal_global.459
- __block_literal_global.465
- __block_literal_global.470
- __block_literal_global.474
- __block_literal_global.485
- __block_literal_global.491
- __block_literal_global.496
- __block_literal_global.499
- __block_literal_global.509
- __block_literal_global.514
- __block_literal_global.520
- __block_literal_global.524
- __block_literal_global.528
- __block_literal_global.533
- __block_literal_global.537
- __block_literal_global.543
- __block_literal_global.547
- __block_literal_global.551
- __block_literal_global.554
- __block_literal_global.559
- __block_literal_global.562
- __block_literal_global.565
- __block_literal_global.568
- __block_literal_global.571
- __block_literal_global.575
- __block_literal_global.579
- __registerForDailyRoutinesCTSJob_block_invoke.420
- __registerForEverydayShortcutsTriggersCTSJobs_block_invoke.415
- __registerForNotificationAndSuggestionDatastorePruning_block_invoke.557
- _objc_msgSend$_initIOSOnlyDependencies
- _objc_msgSend$initFromUserNotification:eventType:timestamp:deliveryReason:
- _objc_msgSend$logNotificationEvent:notification:reason:
- _objc_msgSend$logNotificationGroupEvent:eventIdentifier:timestamp:
- _objc_msgSend$sendEvent:notification:deliveryReason:
- block_copy_helper.5
- block_copy_helper.9
- block_descriptor.11
- block_descriptor.7
- block_destroy_helper.10
- block_destroy_helper.6
- objectdestroy.28Tm
CStrings:
+ "$defaultActor"
+ ":isDeliveredInPrioritySection"
+ ":isDeterminedUrgentByModel"
+ ":isPartOfStack"
+ ":isStackSummary"
+ ":isSummarized"
+ ":notificationSubtitleLength"
+ ":notificationTitleLength"
+ ":summaryLength"
+ "ALTER TABLE notifications ADD COLUMN isDeliveredInPrioritySection INTEGER NOT NULL DEFAULT 0"
+ "ALTER TABLE notifications ADD COLUMN isDeterminedUrgentByModel INTEGER NOT NULL DEFAULT 0"
+ "ALTER TABLE notifications ADD COLUMN isPartOfStack INTEGER NOT NULL DEFAULT 0"
+ "ALTER TABLE notifications ADD COLUMN isStackSummary INTEGER NOT NULL DEFAULT 0"
+ "ALTER TABLE notifications ADD COLUMN isSummarized INTEGER NOT NULL DEFAULT 0"
+ "ALTER TABLE notifications ADD COLUMN notificationSubtitleLength INTEGER"
+ "ALTER TABLE notifications ADD COLUMN notificationTitleLength INTEGER"
+ "ALTER TABLE notifications ADD COLUMN summaryLength INTEGER"
+ "INSERT OR IGNORE INTO notifications VALUES (:uuid, :receiveTimestamp, :deliveryMethod, :urgency, :bundleId, :threadId, :contactId, :isGroupMessage, :isMessage, :latestOutcome, :latestOutcomeTimestamp, :isProminent, :isActive, 0, :rawIdentifier, :modeIdentifier, NULL, NULL, :deliveryReason, :recordTimestamp, :notificationID, :notificationBodyLength, :notificationTitleLength, :notificationSubtitleLength, :summaryLength, :isSummarized, :isPartOfStack, :isStackSummary, :isDeliveredInPrioritySection, :isDeterminedUrgentByModel)"
+ "SELECT     uuid,     receiveTimestamp,     deliveryMethod,     urgency,     bundleId,     isMessage,     deliveryReason,     firstUI,     mostRecentUI,     receivedMode,     latestOutcome,     latestOutcomeTimestamp,     numExpansions,     notificationBodyLength,     notificationTitleLength,     notificationSubtitleLength,     summaryLength,     isSummarized,     isPartOfStack,     isStackSummary,     isDeliveredInPrioritySection     isDeterminedUrgentByModel FROM notifications WHERE     bundleId = :bundleId AND     notificationId = :notificationId AND     recordTimestamp = :recordTimestamp ORDER BY recordTimestamp DESC LIMIT 1 "
+ "SELECT     uuid,     receiveTimestamp,     deliveryMethod,     urgency,     bundleId,     isMessage,     deliveryReason,     firstUI,     mostRecentUI,     receivedMode,     latestOutcome,     latestOutcomeTimestamp,     numExpansions,     notificationBodyLength,     notificationTitleLength,     notificationSubtitleLength,     summaryLength,     isSummarized,     isPartOfStack,     isStackSummary,     isDeliveredInPrioritySection     isDeterminedUrgentByModel FROM notifications WHERE     receiveTimestamp > :startTimestamp AND     receiveTimestamp < :endTimestamp "
+ "Widget Stack Change Alert"
+ "_TtCC21AppPredictionInternal28ContextualEngineContextStoreP33_1731BDF3B55A79F3801A90F52E5A9D7411GuardedData"
+ "bodyLength"
+ "deliveredInPrioritySection"
+ "isDeliveredInPrioritySection"
+ "isDeterminedUrgentByModel"
+ "isPartOfStack"
+ "isStackSummary"
+ "isSummarized"
+ "lockedState"
+ "notificationSubtitleLength"
+ "notificationTitleLength"
+ "subtitleLength"
+ "summaryLength"
+ "summaryTopLineLength"
+ "titleLength"
- "Avocado Stack Change Alert"
- "INSERT OR IGNORE INTO notifications VALUES (:uuid, :receiveTimestamp, :deliveryMethod, :urgency, :bundleId, :threadId, :contactId, :isGroupMessage, :isMessage, :latestOutcome, :latestOutcomeTimestamp, :isProminent, :isActive, 0, :rawIdentifier, :modeIdentifier, NULL, NULL, :deliveryReason, :recordTimestamp, :notificationID, :notificationBodyLength)"
- "SELECT     uuid,     receiveTimestamp,     deliveryMethod,     urgency,     bundleId,     isMessage,     deliveryReason,     firstUI,     mostRecentUI,     receivedMode,     latestOutcome,     latestOutcomeTimestamp,     numExpansions,     notificationBodyLength FROM notifications WHERE     bundleId = :bundleId AND     notificationId = :notificationId AND     recordTimestamp = :recordTimestamp ORDER BY recordTimestamp DESC LIMIT 1 "
- "SELECT     uuid,     receiveTimestamp,     deliveryMethod,     urgency,     bundleId,     isMessage,     deliveryReason,     firstUI,     mostRecentUI,     receivedMode,     latestOutcome,     latestOutcomeTimestamp,     numExpansions,     notificationBodyLength FROM notifications WHERE     receiveTimestamp > :startTimestamp AND     receiveTimestamp < :endTimestamp "

```
