## TrialServer

> `/System/Library/PrivateFrameworks/TrialServer.framework/Versions/A/TrialServer`

```diff

-429.0.4.6.0
-  __TEXT.__text: 0x189bf0
-  __TEXT.__auth_stubs: 0xce0
-  __TEXT.__objc_methlist: 0xac64
+429.20.0.0.0
+  __TEXT.__text: 0x18f640
+  __TEXT.__auth_stubs: 0xd10
+  __TEXT.__delay_helper: 0x1d8
+  __TEXT.__objc_methlist: 0xbea4
   __TEXT.__const: 0xf90
-  __TEXT.__gcc_except_tab: 0xa104
-  __TEXT.__cstring: 0x160dd
-  __TEXT.__oslogstring: 0x1da54
   __TEXT.__dlopen_cstrs: 0xe0
-  __TEXT.__unwind_info: 0x46d8
-  __TEXT.__objc_classname: 0x2781
-  __TEXT.__objc_methname: 0x1d7b2
-  __TEXT.__objc_methtype: 0x52be
-  __TEXT.__objc_stubs: 0x144a0
-  __DATA_CONST.__got: 0x1308
-  __DATA_CONST.__const: 0xf50
-  __DATA_CONST.__objc_classlist: 0x910
+  __TEXT.__gcc_except_tab: 0xa264
+  __TEXT.__cstring: 0x16e69
+  __TEXT.__oslogstring: 0x1e347
+  __TEXT.__unwind_info: 0x4700
+  __TEXT.__objc_classname: 0x2842
+  __TEXT.__objc_methname: 0x1e1ac
+  __TEXT.__objc_methtype: 0x53d4
+  __TEXT.__objc_stubs: 0x14d00
+  __DATA_CONST.__got: 0x1368
+  __DATA_CONST.__const: 0xfe0
+  __DATA_CONST.__objc_classlist: 0x938
   __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x1f0
+  __DATA_CONST.__objc_protolist: 0x1f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5a60
+  __DATA_CONST.__objc_selrefs: 0x5d48
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x5d8
-  __DATA_CONST.__objc_arraydata: 0x3b8
-  __AUTH_CONST.__auth_got: 0x680
-  __AUTH_CONST.__const: 0x7cf0
-  __AUTH_CONST.__cfstring: 0xdae0
-  __AUTH_CONST.__objc_const: 0x18880
-  __AUTH_CONST.__objc_arrayobj: 0x2e8
-  __AUTH_CONST.__objc_intobj: 0x930
+  __DATA_CONST.__objc_superrefs: 0x5f0
+  __DATA_CONST.__objc_arraydata: 0x348
+  __AUTH_CONST.__auth_got: 0x698
+  __AUTH_CONST.__const: 0x7f20
+  __AUTH_CONST.__cfstring: 0xe0c0
+  __AUTH_CONST.__objc_const: 0x171a8
+  __AUTH_CONST.__objc_arrayobj: 0x2d0
+  __AUTH_CONST.__objc_intobj: 0x990
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x48d0
-  __AUTH.__data: 0x8c0
-  __DATA.__objc_ivar: 0xa94
-  __DATA.__data: 0x24c8
+  __AUTH.__objc_data: 0x4a60
+  __AUTH.__data: 0x8e8
+  __DATA.__objc_ivar: 0xac0
+  __DATA.__data: 0x2558
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x3f0
+  __DATA.__common: 0x8
+  __DATA.__bss: 0x400
   __DATA_DIRTY.__objc_data: 0x11d0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /System/Library/PrivateFrameworks/AppleAccount.framework/Versions/A/AppleAccount
   - /System/Library/PrivateFrameworks/AppleFlatBuffers.framework/Versions/A/AppleFlatBuffers
   - /System/Library/PrivateFrameworks/ApplePushService.framework/Versions/A/ApplePushService
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/Versions/A/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/Versions/A/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams
   - /System/Library/PrivateFrameworks/CacheDelete.framework/Versions/A/CacheDelete
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/Versions/A/CrashReporterSupport
+  - /System/Library/PrivateFrameworks/GenerativeModels.framework/Versions/A/GenerativeModels
   - /System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/Versions/A/ProactiveSupport

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 7A183A1C-4F5C-365D-8A7E-B5F0E2E2BC9F
-  Functions: 5007
-  Symbols:   12540
-  CStrings:  10400
+  UUID: F482FD12-D199-37FE-9E0D-68EFB739DE11
+  Functions: 5042
+  Symbols:   12757
+  CStrings:  10652
 
Symbols:
+ +[TRIActivateTreatmentTask taskWithExperiment:treatmentId:factorPackSetId:counterfactualTreatments:taskAttributing:requiresTreatmentInstallation:capabilityModifier:startTime:taskOptions:]
+ +[TRIBGSTManager _submitDeactivationBGSTRequestAfterSeconds:gracePeriodInSeconds:]
+ +[TRIBiomeExperimentUpdateStreamWriter clearExperimentUpdatesStream]
+ +[TRIBiomeExperimentUpdateStreamWriter deleteObsoleteEventsFromExperimentsUpdateStream]
+ +[TRIBiomeExperimentUpdateStreamWriter writeExperimentUpdateWithRecord:withExperimentStateIsActive:withUserId:]
+ +[TRIFetchFactorPackSetTask taskWithFactorPackSetId:treatmentId:isCounterfactualTreatment:taskAttribution:experimentDeployment:]
+ +[TRIMobileAssetUtil _getCurrentPallasAudienceForAssetType:]
+ +[TRIMobileAssetUtil _getCurrentPallasURLForAssetType:]
+ +[TRIMobileAssetUtil _setPallasAudience:forAssetType:]
+ +[TRIMobileAssetUtil _setPallasURL:forAssetType:]
+ +[TRIMobileAssetUtil eliminableAssetTypes]
+ -[TRIActivateTreatmentTask counterfactualTreatments]
+ -[TRIAssetStoreDatabase underlyingDatabase]
+ -[TRIBGSTManager .cxx_destruct]
+ -[TRIBGSTManager expireBGST:]
+ -[TRIBGSTManager initWithServerContext:asyncQueue:]
+ -[TRIBGSTManager markAllBGSTsAsCompleted]
+ -[TRIBGSTManager markBGSTAsStarted:]
+ -[TRIBGSTManager scheduleDeactivationBGSTWithEarliestDeactivationTaskScheduledDate:gracePeriodInSeconds:]
+ -[TRIBGSTManagerGuardedData .cxx_destruct]
+ -[TRIClientExperimentArtifact(Counterfactuals) counterfactualsTreatmentsToFactorPackSetIdsWithActiveTreatmentId:]
+ -[TRIClientExperimentArtifact(Counterfactuals) isCompatibleCounterfactual]
+ -[TRIExperimentDependentSystemCovariates tri_checkAIUseCaseEnabled:]
+ -[TRIExperimentRecord(Counterfactuals) counterfactualsTreatmentsToFactorPackSetIds]
+ -[TRIExperimentRecord(Counterfactuals) hasCounterfactualTreatmentReferencingFactorPackSetId:]
+ -[TRIExperimentUpdateProcessor .cxx_destruct]
+ -[TRIExperimentUpdateProcessor _updateExperimentEndDateWithDeployment:withNewEndDate:scheduleDeactivationTask:scheduleDeactivationNow:]
+ -[TRIExperimentUpdateProcessor initWithExperimentDatabase:]
+ -[TRIExperimentUpdateProcessor processUpdateOperationForExistingExperimentWithEndDate:withExperimentDeployment:]
+ -[TRIExperimentUpdateScheduler .cxx_destruct]
+ -[TRIExperimentUpdateScheduler experimentDatabase]
+ -[TRIExperimentUpdateScheduler initWithExperimentDatabase:taskQueue:]
+ -[TRIExperimentUpdateScheduler queue]
+ -[TRIExperimentUpdateScheduler scheduleExperimentUpdateOperationsForExperimentWithNewEndDate:withDeployment:]
+ -[TRIFetchFactorPackSetTask initWithFactorPackSetId:treatmentId:isCounterfactualTreatment:taskAttribution:experimentDeployment:]
+ -[TRINamespaceResolverStorage _overwriteActiveFactorProvidersUsingGlobalPath:withNamespaceMap:rolloutDeploymentMap:experimentDeploymentMap:experimentTreatmentMap:treatmentFactorPackSetIdsMap:counterfactualTreatmentsMap:factorPackMap:]
+ -[TRINotificationReactionChecker reactionForUpdateExperimentDeployment:]
+ -[TRIPersistentUserSettings persistAIState:]
+ -[TRIPersistentUserSettings persistedAIState]
+ -[TRIPushNotificationHandler _handleExperimentUpdateNotification:]
+ -[TRIPushNotificationHandler experimentUpdateScheduler]
+ -[TRIPushNotificationHandler initWithNotificationChecker:hotfixScheduler:rollbackScheduler:experimentUpdateScheduler:]
+ -[TRISystemCovariates tri_checkAIUseCaseEnabled:]
+ -[TRITaskQueue _scheduleDeactivationBGST:]
+ -[TRITaskQueue resumeWithBGST:executeWhenSuspended:]
+ -[TRIXPCActivityManager _registerDeactivationBGST]
+ GCC_except_table100
+ GCC_except_table50
+ GCC_except_table92
+ GCC_except_table94
+ OBJC_IVAR_$_TRIBGSTManager._asyncQueue
+ OBJC_IVAR_$_TRIBGSTManager._lock
+ OBJC_IVAR_$_TRIBGSTManager._serverContext
+ OBJC_IVAR_$_TRIBGSTManagerGuardedData.identifierToTask
+ OBJC_IVAR_$_TRIExperimentUpdateProcessor._experimentDatabase
+ OBJC_IVAR_$_TRIExperimentUpdateScheduler._experimentDatabase
+ OBJC_IVAR_$_TRIExperimentUpdateScheduler._queue
+ OBJC_IVAR_$_TRIPushNotificationHandler._experimentUpdateScheduler
+ OBJC_IVAR_$_TRITaskQueueGuardedData.bgstManager
+ _BiomeLibrary
+ _CFStringGetTypeID
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_CLASS_$_BMSQLDatabase
+ _OBJC_CLASS_$_BMTrialNamespaceUpdates
+ _OBJC_CLASS_$_BMTrialNamespaceUpdatesNamespaceNamesList
+ _OBJC_CLASS_$_GMAvailabilityWrapper
+ _OBJC_CLASS_$_TRIBGSTManager
+ _OBJC_CLASS_$_TRIBGSTManagerGuardedData
+ _OBJC_CLASS_$_TRIBiomeExperimentUpdateStreamWriter
+ _OBJC_CLASS_$_TRIExperimentUpdateProcessor
+ _OBJC_CLASS_$_TRIExperimentUpdateScheduler
+ _OBJC_METACLASS_$_TRIBGSTManager
+ _OBJC_METACLASS_$_TRIBGSTManagerGuardedData
+ _OBJC_METACLASS_$_TRIBiomeExperimentUpdateStreamWriter
+ _OBJC_METACLASS_$_TRIExperimentUpdateProcessor
+ _OBJC_METACLASS_$_TRIExperimentUpdateScheduler
+ _TRIBGSTSchedulingDelayInSeconds
+ _TRIBackgroundSystemTaskIdentifier_Deactivation
+ _TRIPersistentAIState
+ __100-[TRIBackgroundMLTaskDatabase deactivateTaskDeployment:deactivatedFactorPackSetId:usingTransaction:]_block_invoke.128
+ __101-[TRIBackgroundMLTaskHistoryDatabase getAllAllocationStatusesForBMLTId:deploymentId:factorPackSetId:]_block_invoke.76
+ __101-[TRIFactorPackSetStorage enumerateCompatibleFactorPacksForFactorPackSet:usingLegacyPaths:withBlock:]_block_invoke.141
+ __101-[TRIFactorPackSetStorage enumerateCompatibleFactorPacksForFactorPackSet:usingLegacyPaths:withBlock:]_block_invoke.147
+ __101-[TRIRemoteAssetStoreOperator saveAssetWithIdentifier:sourcePath:flockWitness:removeSourceOnFailure:]_block_invoke.354
+ __101-[TRIXPCNamespaceManagementRequestHandler getSandboxExtensionTokensForIdentifierQueryWithCompletion:]_block_invoke.266
+ __101-[TRIXPCStatusRequestHandler evaluationHistoryRecordsForMLRuntimeWithLimit:newerThanDate:completion:]_block_invoke.136
+ __102-[TRICKNativeArtifactProvider _fetchRolloutNotificationWithRolloutId:deploymentId:options:completion:]_block_invoke.223
+ __102-[TRIRolloutHistoryDatabase getAllAllocationStatusesForRolloutId:rampId:deploymentId:factorPackSetId:]_block_invoke.105
+ __103-[TRIActivateTreatmentBaseTask _experimentRecord:hasConflictWithExperimentsInDatabase:conflictEndTime:]_block_invoke.30
+ __103-[TRIActivateTreatmentBaseTask _experimentRecord:hasConflictWithExperimentsInDatabase:conflictEndTime:]_block_invoke.31
+ __103-[TRIXPCNamespaceManagementRequestHandler setPurgeabilityLevelsForFactors:forNamespaceName:completion:]_block_invoke.226
+ __104+[TRIClientFactorPackUtils _enumerateAssetFactorLevelsInFlatBufferStorage:trialAssetBlock:maAssetBlock:]_block_invoke.303
+ __104+[TRIClientFactorPackUtils _enumerateAssetFactorLevelsInFlatBufferStorage:trialAssetBlock:maAssetBlock:]_block_invoke.306
+ __105-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:completion:]_block_invoke.109
+ __105-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:completion:]_block_invoke.112
+ __105-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:completion:]_block_invoke.113
+ __105-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:completion:]_block_invoke.96
+ __106-[TRIBackgroundMLTaskDatabase activateDeployment:withFactorPackSetId:targetingRuleIndex:usingTransaction:]_block_invoke.121
+ __106-[TRIBackgroundMLTaskDatabase targetTaskDeployment:toFactorPackSetId:targetingRuleIndex:usingTransaction:]_block_invoke.113
+ __106-[TRIRemoteAssetPatcher applyPatchWithFilename:toSrcDir:writingToEmptyDestDir:postPatchCompression:error:]_block_invoke.26
+ __108+[TRISetupAssistantFetchUtils getIncompatibleNamespaceNamesForTriClientRollout:namespaceDescriptorProvider:]_block_invoke.50
+ __108-[TRICKNativeArtifactProvider fetchAssetsWithIndexes:fromTreatmentWithRecordId:options:progress:completion:]_block_invoke.207
+ __108-[TRIRolloutDatabase _enumerateRecordsMatchingWhereClause:bind:prependingWithClause:usingTransaction:block:]_block_invoke.117
+ __108-[TRIRolloutDatabase _enumerateRecordsMatchingWhereClause:bind:prependingWithClause:usingTransaction:block:]_block_invoke.125
+ __108-[TRIXPCNamespaceManagementRequestHandler rejectFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke.243
+ __108-[TRIXPCNamespaceManagementRequestHandler rejectFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke.247
+ __108-[TRIXPCNamespaceManagementRequestHandler rejectFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke_2.248
+ __108-[TRIXPCNamespaceManagementRequestHandler statusOfDownloadForFactors:withNamespace:factorsState:completion:]_block_invoke.254
+ __108-[TRIXPCNamespaceManagementRequestHandler statusOfDownloadForFactors:withNamespace:factorsState:completion:]_block_invoke.255
+ __108-[TRIXPCNamespaceManagementRequestHandler statusOfDownloadForFactors:withNamespace:factorsState:completion:]_block_invoke.260
+ __109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.390
+ __109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.395
+ __109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.400
+ __109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.404
+ __109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.408
+ __109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.410
+ __109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.413
+ __109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.421
+ __109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.423
+ __109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.402
+ __109-[TRIXPCNamespaceManagementRequestHandler promoteFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke.251
+ __109-[TRIXPCNamespaceManagementRequestHandler promoteFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke.252
+ __109-[TRIXPCNamespaceManagementRequestHandler promoteFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke_2.253
+ __111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.318
+ __111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.325
+ __112-[TRIInternalServiceRequestHandler experimentNotificationsWithExperimentId:cloudKitContainer:teamId:completion:]_block_invoke.47
+ __112-[TRIInternalServiceRequestHandler experimentNotificationsWithExperimentId:cloudKitContainer:teamId:completion:]_block_invoke.77
+ __113+[TRICacheDeleteCallbacks registerCallbacksWithPaths:experimentDatabase:rolloutDatabase:taskQueue:loggingClient:]_block_invoke.92
+ __113+[TRICacheDeleteCallbacks registerCallbacksWithPaths:experimentDatabase:rolloutDatabase:taskQueue:loggingClient:]_block_invoke.94
+ __113-[TRIFetchTreatmentTask _downloadAndSaveMAAssets:options:downloadNotificationKey:context:errorResult:fetchError:]_block_invoke.308
+ __113-[TRIPushServiceConnectionMultiplexer _expectedChannelIdsForRolloutDeployments:experimentIds:maxChannelsAllowed:]_block_invoke.36
+ __114-[TRIXPCNamespaceManagementRequestHandler immediateDownloadForNamespaceNames:allowExpensiveNetworking:completion:]_block_invoke.208
+ __114-[TRIXPCNamespaceManagementRequestHandler immediateDownloadForNamespaceNames:allowExpensiveNetworking:completion:]_block_invoke.210
+ __114-[TRIXPCNamespaceManagementRequestHandler immediateDownloadForNamespaceNames:allowExpensiveNetworking:completion:]_block_invoke.217
+ __115+[TRIReferenceManagedDir collectGarbageForManagedDir:withExternalReferenceStore:usingTempDir:managedDirWasDeleted:]_block_invoke.67
+ __115-[TRICKNativeArtifactProvider _fetchRecordIdsForAssetsWithIds:options:cursor:cancelableOp:resultBuffer:completion:]_block_invoke.241
+ __116-[TRICKNativeArtifactProvider _fetchRolloutNotificationsWithCursor:options:sinceDate:namespaceNames:resultsHandler:]_block_invoke.219
+ __116-[TRIRolloutDatabase targetDeployment:toFactorPackSetId:targetingRuleIndex:deallocatedDeployments:usingTransaction:]_block_invoke.191
+ __118+[TRIXPCNamespaceManagementRequestHandler _notificationKeyWithNamespace:assetIndexesByTreatment:assetIdsByFactorPack:]_block_invoke.177
+ __118+[TRIXPCNamespaceManagementRequestHandler usingServerContext:deregisterNamespaceWithName:teamId:taskQueue:completion:]_block_invoke.338
+ __118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.568
+ __118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.574
+ __118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.581
+ __118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.592
+ __118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.595
+ __118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke_2.575
+ __118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke_2.582
+ __119-[TRICKNativeArtifactProvider fetchDiffSourceRecordIdsWithTargetAssetIds:isAcceptableSourceAssetId:options:completion:]_block_invoke.274
+ __119-[TRICKNativeArtifactProvider fetchDiffSourceRecordIdsWithTargetAssetIds:isAcceptableSourceAssetId:options:completion:]_block_invoke.276
+ __119-[TRIXPCNamespaceManagementRequestHandler startDownloadLevelsForFactors:withNamespace:factorsState:options:completion:]_block_invoke.183
+ __119-[TRIXPCNamespaceManagementRequestHandler startDownloadLevelsForFactors:withNamespace:factorsState:options:completion:]_block_invoke.190
+ __119-[TRIXPCNamespaceManagementRequestHandler startDownloadLevelsForFactors:withNamespace:factorsState:options:completion:]_block_invoke_2.191
+ __122-[TRIXPCNamespaceManagementRequestHandler removeLevelsForFactors:withNamespace:factorsState:removeImmediately:completion:]_block_invoke.220
+ __122-[TRIXPCNamespaceManagementRequestHandler removeLevelsForFactors:withNamespace:factorsState:removeImmediately:completion:]_block_invoke.224
+ __122-[TRIXPCNamespaceManagementRequestHandler removeLevelsForFactors:withNamespace:factorsState:removeImmediately:completion:]_block_invoke_2.225
+ __124-[TRIInternalServiceRequestHandler rolloutNotificationWithLatestDeploymentForRolloutId:cloudKitContainer:teamId:completion:]_block_invoke.82
+ __124-[TRIInternalServiceRequestHandler rolloutNotificationWithLatestDeploymentForRolloutId:cloudKitContainer:teamId:completion:]_block_invoke.88
+ __125-[TRIExperimentDatabase addExperimentWithExperimentDeployment:environment:type:status:startDate:endDate:namespaces:artifact:]_block_invoke.39
+ __125-[TRIExperimentDatabase addExperimentWithExperimentDeployment:environment:type:status:startDate:endDate:namespaces:artifact:]_block_invoke.57
+ __126-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:serverContext:completion:]_block_invoke.227
+ __126-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:serverContext:completion:]_block_invoke.242
+ __126-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:serverContext:completion:]_block_invoke.250
+ __126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke.439
+ __126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke.448
+ __126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke.456
+ __126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke.461
+ __126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_2.445
+ __126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_2.458
+ __127-[TRICKNativeArtifactProvider _fetchNotificationsWithQueryType:withCursor:withNamespaceNames:sinceDate:options:resultsHandler:]_block_invoke.166
+ __127-[TRICKNativeArtifactProvider _fetchNotificationsWithQueryType:withCursor:withNamespaceNames:sinceDate:options:resultsHandler:]_block_invoke.169
+ __127-[TRICKNativeArtifactProvider _fetchNotificationsWithQueryType:withCursor:withNamespaceNames:sinceDate:options:resultsHandler:]_block_invoke.173
+ __127-[TRIFetchOnDemandFactorsTask _asyncFetchMAAssetsFromFactorPacksWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.608
+ __127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.488
+ __127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.492
+ __127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.501
+ __127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke_2.497
+ __128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.596
+ __128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.598
+ __128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.599
+ __128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.604
+ __128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke_2.597
+ __129-[TRISelectRolloutNotificationListTask _processRolloutArtifact:rolloutsProcessed:remainingNamespaces:targeter:context:taskQueue:]_block_invoke.36
+ __130-[TRICKNativeArtifactProvider _fetchExperimentsWithCursor:withNamespaceNames:sinceDate:fetchRollbacksOnly:options:resultsHandler:]_block_invoke.159
+ __131-[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:privacyFilterPolicy:deploymentEnvironment:completion:]_block_invoke.55
+ __131-[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:privacyFilterPolicy:deploymentEnvironment:completion:]_block_invoke.78
+ __131-[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:privacyFilterPolicy:deploymentEnvironment:completion:]_block_invoke.86
+ __131-[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:privacyFilterPolicy:deploymentEnvironment:completion:]_block_invoke.90
+ __133+[TRIClientFactorPackUtils requiredAssetsForInstallationWithFactorPack:assetStore:maProvider:subscriptionSettings:aliasToUnaliasMap:]_block_invoke.350
+ __138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke.558
+ __138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke.559
+ __138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke.563
+ __144-[TRISQLiteCKDatabase _evalQueryOperationWithRecordType:predicate:sortDescriptors:offset:resultsLimit:desiredKeys:txn:error:recordMatchedBlock:]_block_invoke.168
+ __144-[TRISQLiteCKDatabase _evalQueryOperationWithRecordType:predicate:sortDescriptors:offset:resultsLimit:desiredKeys:txn:error:recordMatchedBlock:]_block_invoke.170
+ __145-[TRITaskQueue _partitionTaskGroup:byRunnabilityGivenCapabilities:runnableAtDate:topoSortedCurrentlyRunnable:blocked:allowOnlyRootTasksRunnable:]_block_invoke.276
+ __151-[TRIFetchTreatmentTask _fetchAssetsWithArtifactProvider:recordId:experimentRecord:assetIndexes:downloadOptions:context:assetURLs:treatmentFetchError:]_block_invoke.367
+ __154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.512
+ __154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.516
+ __154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.519
+ __154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.525
+ __154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.529
+ __154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.530
+ __154-[TRIPurgeableExperimentAndRolloutProvider _factorPackSetHasPurgeableFactorsWithFPSId:eagerFactors:overriddenFactors:purgeableNamespaces:returningAssets:]_block_invoke.54
+ __156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.349
+ __156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.350
+ __158-[TRICKNativeArtifactProvider fetchDiffsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.279
+ __158-[TRICKNativeArtifactProvider fetchDiffsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.283
+ __158-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromFactorPacksWithContext:assetDiffFetchPlan:requiredAssetIds:downloadOptions:updatingAggregateProgress:]_block_invoke.539
+ __159-[TRICKNativeArtifactProvider fetchAssetsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.248
+ __159-[TRICKNativeArtifactProvider fetchAssetsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.250
+ __159-[TRICKNativeArtifactProvider fetchAssetsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.258
+ __163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.438
+ __163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.443
+ __163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.449
+ __163-[TRIXPCNamespaceManagementRequestHandler registerNamespaceWithNamespaceName:compatibilityVersion:defaultsFileURL:applicationGroup:cloudKitContainerId:completion:]_block_invoke.103
+ __163-[TRIXPCNamespaceManagementRequestHandler registerNamespaceWithNamespaceName:compatibilityVersion:defaultsFileURL:applicationGroup:cloudKitContainerId:completion:]_block_invoke.105
+ __163-[TRIXPCNamespaceManagementRequestHandler registerNamespaceWithNamespaceName:compatibilityVersion:defaultsFileURL:applicationGroup:cloudKitContainerId:completion:]_block_invoke.141
+ __164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.326
+ __164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.330
+ __164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.335
+ __165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.417
+ __165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.423
+ __165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.430
+ __165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.437
+ __165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.440
+ __165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.445
+ __165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.431
+ __170-[TRIRolloutDatabase deactivateDeploymentsWithRolloutId:deactivatedDeployment:deactivatedFactorPackSetId:deactivatedRampId:deactivationStateTransitions:usingTransaction:]_block_invoke.210
+ __174-[TRIPurgeableExperimentAndRolloutProvider _purgeablesForRolloutsFromNamespaces:eagerFactors:overriddenFactors:shouldGenerateAssetPaths:purgeableExperiments:purgeableAssets:]_block_invoke.34
+ __177-[TRIPurgeableExperimentAndRolloutProvider _purgeablesForExperimentsFromNamespaces:eagerFactors:overriddenFactors:shouldGenerateAssetPaths:purgeableExperiments:purgeableAssets:]_block_invoke.31
+ __177-[TRIRolloutDatabase activateDeployment:withFactorPackSetId:targetingRuleIndex:deactivatedDeployments:deactivatedFactorPackSetIds:deactivationStateTransitions:usingTransaction:]_block_invoke.200
+ __178-[TRIInternalServiceRequestHandler registerNamespaceWithNamespaceName:compatibilityVersion:defaultsFileURL:teamId:appContainerId:appContainerType:cloudKitContainerId:completion:]_block_invoke.130
+ __179+[TRIXPCNamespaceManagementRequestHandler _immediateDownloadForNamespaceNames:usingEntitlementWitness:serverContext:taskQueue:allowExpensiveNetworking:taskAttribution:completion:]_block_invoke.409
+ __184+[TRIClientFactorPackUtils unlinkedOnDemandAssetsWithFactorPack:flatbufferFactorLevels:factorPackPath:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:unlinkedMAAssetsOnDisk:]_block_invoke.361
+ __184+[TRIClientFactorPackUtils unlinkedOnDemandAssetsWithFactorPack:flatbufferFactorLevels:factorPackPath:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:unlinkedMAAssetsOnDisk:]_block_invoke.364
+ __19-[TRIDServer start]_block_invoke.340
+ __19-[TRIDServer start]_block_invoke.349
+ __19-[TRIDServer start]_block_invoke.352
+ __19-[TRIDServer start]_block_invoke.356
+ __220+[TRIDiffableAssetBuilder buildAndSaveDiffableAssetsWithAssetIds:metadataForAssetId:artifactProvider:options:paths:assetsDownloadSize:perAssetIdCompletionBlockOnSuccess:perAssetIdCompletionBlockOnError:retryAfter:error:]_block_invoke.39
+ __220+[TRIDiffableAssetBuilder buildAndSaveDiffableAssetsWithAssetIds:metadataForAssetId:artifactProvider:options:paths:assetsDownloadSize:perAssetIdCompletionBlockOnSuccess:perAssetIdCompletionBlockOnError:retryAfter:error:]_block_invoke.44
+ __220+[TRIDiffableAssetBuilder buildAndSaveDiffableAssetsWithAssetIds:metadataForAssetId:artifactProvider:options:paths:assetsDownloadSize:perAssetIdCompletionBlockOnSuccess:perAssetIdCompletionBlockOnError:retryAfter:error:]_block_invoke.49
+ __220+[TRIDiffableAssetBuilder buildAndSaveDiffableAssetsWithAssetIds:metadataForAssetId:artifactProvider:options:paths:assetsDownloadSize:perAssetIdCompletionBlockOnSuccess:perAssetIdCompletionBlockOnError:retryAfter:error:]_block_invoke.51
+ __220+[TRIDiffableAssetBuilder buildAndSaveDiffableAssetsWithAssetIds:metadataForAssetId:artifactProvider:options:paths:assetsDownloadSize:perAssetIdCompletionBlockOnSuccess:perAssetIdCompletionBlockOnError:retryAfter:error:]_block_invoke.67
+ __220+[TRIDiffableAssetBuilder buildAndSaveDiffableAssetsWithAssetIds:metadataForAssetId:artifactProvider:options:paths:assetsDownloadSize:perAssetIdCompletionBlockOnSuccess:perAssetIdCompletionBlockOnError:retryAfter:error:]_block_invoke_2.45
+ __234-[TRINamespaceResolverStorage _overwriteActiveFactorProvidersUsingGlobalPath:withNamespaceMap:rolloutDeploymentMap:experimentDeploymentMap:experimentTreatmentMap:treatmentFactorPackSetIdsMap:counterfactualTreatmentsMap:factorPackMap:]_block_invoke.218
+ __257+[TRIXPCNamespaceManagementRequestHandler _startDownloadAssetIndexesByTreatment:usingEntitlementWitness:serverContext:taskQueue:experimentIds:assetIdsByFactorPack:rolloutFactorNames:rolloutDeployments:namespace:taskAttribution:factorsState:notificationKey:]_block_invoke.382
+ __257+[TRIXPCNamespaceManagementRequestHandler _startDownloadAssetIndexesByTreatment:usingEntitlementWitness:serverContext:taskQueue:experimentIds:assetIdsByFactorPack:rolloutFactorNames:rolloutDeployments:namespace:taskAttribution:factorsState:notificationKey:]_block_invoke.386
+ __257+[TRIXPCNamespaceManagementRequestHandler _startDownloadAssetIndexesByTreatment:usingEntitlementWitness:serverContext:taskQueue:experimentIds:assetIdsByFactorPack:rolloutFactorNames:rolloutDeployments:namespace:taskAttribution:factorsState:notificationKey:]_block_invoke.390
+ __27-[TRITaskDatabase allTasks]_block_invoke.114
+ __27-[TRITaskDatabase allTasks]_block_invoke.118
+ __27-[TRITaskDatabase allTasks]_block_invoke.127
+ __27-[TRITaskDatabase allTasks]_block_invoke_2.131
+ __34-[TRICancelableMAOperation cancel]_block_invoke.474
+ __36-[TRIBGSTManager markBGSTAsStarted:]_block_invoke.28
+ __36-[TRISQLiteCKDatabase addOperation:]_block_invoke.92
+ __39-[TRIRolloutHistoryDatabase addRecord:]_block_invoke.41
+ __40-[TRITaskDatabase tasksDependentOnTask:]_block_invoke.206
+ __41+[TRIClientFactorPackUtils uniqueAssets:]_block_invoke.372
+ __41-[TRITaskDatabase _tasksForQuery:onPrep:]_block_invoke.148
+ __41-[TRITaskDatabase _tasksForQuery:onPrep:]_block_invoke_2.149
+ __42-[TRIDatabase migration_addTaskCapability]_block_invoke.308
+ __42-[TRIExperimentHistoryDatabase addRecord:]_block_invoke.42
+ __42-[TRIKVStore blobForKey:usingTransaction:]_block_invoke.31
+ __44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.375
+ __44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.385
+ __44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.397
+ __44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.416
+ __44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.430
+ __44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.435
+ __44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.436
+ __44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.386
+ __44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.398
+ __44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.417
+ __44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.437
+ __46-[TRIRolloutDatabase addNewRolloutWithRecord:]_block_invoke.39
+ __46-[TRIRolloutDatabase addNewRolloutWithRecord:]_block_invoke.43
+ __46-[TRIRolloutDatabase addNewRolloutWithRecord:]_block_invoke.58
+ __46-[TRISQLiteCKDatabase _processQueryOperation:]_block_invoke.107
+ __46-[TRITaskQueue _registerRetryActivityForDate:]_block_invoke.319
+ __47-[TRIFetchOnDemandFactorsTask _asPersistedTask]_block_invoke.622
+ __47-[TRIFetchOnDemandFactorsTask _asPersistedTask]_block_invoke_2.624
+ __47-[TRISQLiteCKDatabase _upsertRecord:txn:error:]_block_invoke.467
+ __47-[TRISQLiteCKDatabase _upsertRecord:txn:error:]_block_invoke_2.468
+ __47-[TRISQLiteCKDatabase _upsertRecord:txn:error:]_block_invoke_3.472
+ __47-[TRISQLiteCKDatabase _upsertRecord:txn:error:]_block_invoke_4.479
+ __47-[TRISQLiteCKDatabase _upsertRecord:txn:error:]_block_invoke_5.480
+ __47-[TRITaskQueue _finalizeTask:withId:runResult:]_block_invoke.220
+ __47-[TRITaskQueue _finalizeTask:withId:runResult:]_block_invoke.222
+ __49-[TRITaskDatabase removeTaskWithId:cleanupBlock:]_block_invoke.84
+ __49-[TRITaskDatabase removeTaskWithId:cleanupBlock:]_block_invoke.89
+ __49-[TRITaskDatabase removeTaskWithId:cleanupBlock:]_block_invoke_2.93
+ __49-[TRITaskDatabase removeTaskWithId:cleanupBlock:]_block_invoke_3.97
+ __50-[TRITaskDatabase directDependenciesOfTaskWithId:]_block_invoke.202
+ __50-[TRITaskQueue _registerTaskQueueActivityForDate:]_block_invoke.323
+ __50-[TRITaskQueue _registerTaskQueueActivityForDate:]_block_invoke.326
+ __50-[TRITaskQueue cancelTasksWithTag:excludingTasks:]_block_invoke.303
+ __52-[TRIRetargetAllTask runUsingContext:withTaskQueue:]_block_invoke.33
+ __52-[TRIRetargetAllTask runUsingContext:withTaskQueue:]_block_invoke.38
+ __53-[TRIMAProvider installedAssetsMatchingFullAssetIds:]_block_invoke.500
+ __53-[TRIXPCActivityManager _registerPostUpgradeActivity]_block_invoke.356
+ __55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.401
+ __56-[TRIXPCStatusRequestHandler bmltRecordsWithCompletion:]_block_invoke.164
+ __56-[TRIXPCStatusRequestHandler bmltRecordsWithCompletion:]_block_invoke.165
+ __57-[TRIAssetPurger purgeableAssetSizeForPurgeabilityLevel:]_block_invoke.113
+ __57-[TRIAssetPurger purgeableAssetSizeForPurgeabilityLevel:]_block_invoke.117
+ __57-[TRIDisenrollRolloutTask runUsingContext:withTaskQueue:]_block_invoke.56
+ __57-[TRIFetchOnDemandFactorsTask _requiredDiskSpaceForPlan:]_block_invoke.463
+ __57-[TRIXPCActivityManager _registerHotfixTargetingActivity]_block_invoke.369
+ __57-[TRIXPCActivityManager _registerHotfixTargetingActivity]_block_invoke_2.370
+ __58-[TRIXPCActivityManager _registerFetchExperimentsActivity]_block_invoke.340
+ __59-[TRIActivateTreatmentTask runTaskUsingContext:experiment:]_block_invoke.170
+ __59-[TRIActivateTreatmentTask runTaskUsingContext:experiment:]_block_invoke.172
+ __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.505
+ __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.513
+ __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.514
+ __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.533
+ __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.534
+ __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.551
+ __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.557
+ __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.561
+ __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.565
+ __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.568
+ __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.553
+ __59-[TRITaskQueue activeActivityDescriptorGrantingCapability:]_block_invoke.344
+ __59-[TRIXPCStatusRequestHandler rolloutRecordsWithCompletion:]_block_invoke.167
+ __59-[TRIXPCStatusRequestHandler rolloutRecordsWithCompletion:]_block_invoke.168
+ __60-[TRIBackgroundMLTaskDatabase taskRecordWithTaskDeployment:]_block_invoke.103
+ __60-[TRIDeactivateTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.59
+ __60-[TRIDeactivateTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.73
+ __60-[TRIDeactivateTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.79
+ __60-[TRIDeactivateTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.94
+ __60-[TRIRolloutDatabase recordWithDeployment:usingTransaction:]_block_invoke.134
+ __60-[TRIXPCActivityManager _registerCellularActivityWithDelay:]_block_invoke.337
+ __60-[TRIXPCActivityManager registerSetupAssistantFetchActivity]_block_invoke.364
+ __60-[TRIXPCActivityManager registerSetupAssistantFetchActivity]_block_invoke.365
+ __61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.439
+ __61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.460
+ __61-[TRITaskDatabase addTask:startTime:tags:dependencies:error:]_block_invoke.37
+ __61-[TRITaskDatabase addTask:startTime:tags:dependencies:error:]_block_invoke.40
+ __61-[TRITaskDatabase addTask:startTime:tags:dependencies:error:]_block_invoke.50
+ __61-[TRITaskDatabase addTask:startTime:tags:dependencies:error:]_block_invoke.60
+ __61-[TRITaskDatabase addTask:startTime:tags:dependencies:error:]_block_invoke.68
+ __62-[TRIInternalServiceRequestHandler taskRecordsWithCompletion:]_block_invoke.37
+ __63-[TRIFetchBMLTNotificationsTask runUsingContext:withTaskQueue:]_block_invoke.91
+ __63-[TRIFetchBMLTNotificationsTask runUsingContext:withTaskQueue:]_block_invoke.92
+ __63-[TRITaskQueue enumerateTasksWithTagsIntersectingTagSet:block:]_block_invoke.306
+ __63-[TRITaskQueue enumerateTasksWithTagsIntersectingTagSet:block:]_block_invoke.307
+ __63-[TRITaskQueue enumerateTasksWithTagsIntersectingTagSet:block:]_block_invoke.309
+ __64-[TRIInternalServiceRequestHandler setFailureInjectionDelegate:]_block_invoke.115
+ __65-[TRIMaintenanceTask _cleanupUnusedContentWithContext:nextTasks:]_block_invoke.110
+ __65-[TRIMaintenanceTask _cleanupUnusedContentWithContext:nextTasks:]_block_invoke.114
+ __65-[TRIMaintenanceTask _cleanupUnusedContentWithContext:nextTasks:]_block_invoke.87
+ __65-[TRIMaintenanceTask _cleanupUnusedContentWithContext:nextTasks:]_block_invoke.93
+ __65-[TRIMaintenanceTask _cleanupUnusedContentWithContext:nextTasks:]_block_invoke_2.99
+ __66-[TRIAssetStoreDatabase enumerateAllAutoAssetReferencesWithBlock:]_block_invoke.157
+ __66-[TRIExperimentDatabase experimentRecordWithExperimentDeployment:]_block_invoke.171
+ __66-[TRIFetchBMLTNotificationsTask fetchSingleDeploymentWithContext:]_block_invoke.72
+ __66-[TRIInternalServiceRequestHandler submitTask:options:completion:]_block_invoke.92
+ __66-[TRISQLiteCKDatabase _deleteRecordsWithRecordIds:recordType:txn:]_block_invoke.438
+ __67-[TRIActiveLowLevelFactorsWriter _remoteWriteExperimentData:error:]_block_invoke.88
+ __67-[TRIContentTracker _addOrDropRefWithContentIdentifier:changeType:]_block_invoke.72
+ __67-[TRIContentTracker _addOrDropRefWithContentIdentifier:changeType:]_block_invoke.76
+ __69-[TRIAssetStoreDatabase addReferenceToAutoAssetId:forLifetimeOfPath:]_block_invoke.114
+ __69-[TRIAssetStoreDatabase addReferenceToAutoAssetId:forLifetimeOfPath:]_block_invoke.122
+ __69-[TRIAssetStoreDatabase addReferenceToAutoAssetId:forLifetimeOfPath:]_block_invoke_2.129
+ __69-[TRIBackgroundMLTaskDatabase deactivateDeployment:usingTransaction:]_block_invoke.124
+ __69-[TRIFetchFactorPackSetTask _requiredAssetsForFactorPackSet:context:]_block_invoke.389
+ __69-[TRITaskQueue resumeWithXPCActivityDescriptor:executeWhenSuspended:]_block_invoke.103
+ __69-[TRITaskQueue resumeWithXPCActivityDescriptor:executeWhenSuspended:]_block_invoke.111
+ __69-[TRIXPCStatusRequestHandler activeEvaluationsForBMLTWithCompletion:]_block_invoke.142
+ __69-[TRIXPCStatusRequestHandler activeEvaluationsForBMLTWithCompletion:]_block_invoke.147
+ __70-[TRIRunningXPCActivityDescriptor initWithActivity:capabilities:name:]_block_invoke.23
+ __70-[TRISelectRolloutNotificationListTask runUsingContext:withTaskQueue:]_block_invoke.69
+ __71-[TRIActivateTargetedBMLTDeploymentTask runUsingContext:withTaskQueue:]_block_invoke.82
+ __71-[TRIAssetPurger purgeAssetsForPurgeabilityLevel:requestedPurgeAmount:]_block_invoke.138
+ __71-[TRICKNativeArtifactProvider fetchTreatmentWithId:options:completion:]_block_invoke.198
+ __71-[TRIInternalServiceRequestHandler removeUnusedChannelsWithCompletion:]_block_invoke.120
+ __71-[TRIInternalServiceRequestHandler removeUnusedChannelsWithCompletion:]_block_invoke.125
+ __72-[TRIAssetPurger _enumeratePurgeCandidatesForPurgeableConstructs:block:]_block_invoke.154
+ __72-[TRIAssetPurger _enumeratePurgeCandidatesForPurgeableConstructs:block:]_block_invoke.158
+ __72-[TRIXPCActivityManager _scheduleFetchTaskWithActivityDescriptor:label:]_block_invoke.320
+ __73-[TRIFetchFactorPackSetTask _saveFactorPackSet:requiredAssetMap:context:]_block_invoke.466
+ __73-[TRIFetchOnDemandFactorsTask _updateFactorPacksByMergingAssets:context:]_block_invoke.417
+ __73-[TRITaskQueue _evaluateRunConditionsWithGuardedData:shouldContinueWork:]_block_invoke.97
+ __74-[TRIAssetStoreDatabase enumerateAssetIdsWithoutLiveReferencesUsingBlock:]_block_invoke.193
+ __74-[TRIAssetStoreDatabase enumerateAssetIdsWithoutLiveReferencesUsingBlock:]_block_invoke_2.203
+ __74-[TRIInternalServiceRequestHandler dynamicNamespaceRecordsWithCompletion:]_block_invoke.171
+ __74-[TRISQLiteMADatabase eliminatePromotedNeverLockedForSelector:completion:]_block_invoke.414
+ __74-[TRISQLiteMADatabase eliminatePromotedNeverLockedForSelector:completion:]_block_invoke_2.415
+ __74-[TRISQLiteMADatabase eliminatePromotedNeverLockedForSelector:completion:]_block_invoke_3.419
+ __74-[TRIXPCStatusRequestHandler activeEvaluationsForMLRuntimeWithCompletion:]_block_invoke.116
+ __74-[TRIXPCStatusRequestHandler activeEvaluationsForMLRuntimeWithCompletion:]_block_invoke.129
+ __75-[TRICKNativeArtifactProvider fetchFactorPackSetWithId:options:completion:]_block_invoke.230
+ __77-[TRIRolloutHistoryDatabase _enumerateRecordsMatchingWhereClause:bind:block:]_block_invoke.55
+ __77-[TRIRolloutHistoryDatabase _enumerateRecordsMatchingWhereClause:bind:block:]_block_invoke.63
+ __77-[TRIRolloutHistoryDatabase _enumerateRecordsMatchingWhereClause:bind:block:]_block_invoke.81
+ __78-[NSFileManager(TRIServer) triRemoveCachedANEBinariesForModelsFromPath:error:]_block_invoke.30
+ __78-[NSFileManager(TRIServer) triRemoveCachedANEBinariesForModelsFromPath:error:]_block_invoke.57
+ __78-[TRIDatabase initWithPaths:databasePath:storageManagement:performMigrations:]_block_invoke.58
+ __78-[TRIDatabase initWithPaths:databasePath:storageManagement:performMigrations:]_block_invoke.61
+ __78-[TRIInternalServiceRequestHandler resumeSQLiteCKDatabaseQueueWithCompletion:]_block_invoke.119
+ __78-[TRIXPCActivityManager _scheduleMaintenanceTaskWithActivityDescriptor:label:]_block_invoke.326
+ __79-[TRIFactorPackSetStorage migrateEligibleFactorPacksToGlobalWithServerContext:]_block_invoke.160
+ __79-[TRIFactorPackSetStorage migrateEligibleFactorPacksToGlobalWithServerContext:]_block_invoke.163
+ __79-[TRIInternalServiceRequestHandler suspendSQLiteCKDatabaseQueueWithCompletion:]_block_invoke.117
+ __79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.514
+ __79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.519
+ __79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.524
+ __79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.528
+ __79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke_2.515
+ __80-[TRIExperimentHistoryDatabase _enumerateRecordsMatchingWhereClause:bind:block:]_block_invoke.59
+ __80-[TRIExperimentHistoryDatabase _enumerateRecordsMatchingWhereClause:bind:block:]_block_invoke.67
+ __80-[TRIExperimentHistoryDatabase _enumerateRecordsMatchingWhereClause:bind:block:]_block_invoke.91
+ __80-[TRIInternalServiceRequestHandler lastFetchDateForContainer:teamId:completion:]_block_invoke.100
+ __81-[TRITaskQueue _addTask:options:guardedData:taskIdOut:accumulatedNewTaskRecords:]_block_invoke.288
+ __81-[TRIXPCActivityManager _registerPostUpgradeActivityRequireInexpensiveNetworking]_block_invoke.357
+ __82-[TRICKNativeArtifactProvider fetchBMLTCatalogNotificationWithOptions:completion:]_block_invoke.287
+ __82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.112
+ __82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.117
+ __82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.122
+ __82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.130
+ __82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.132
+ __82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.133
+ __82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.135
+ __82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.140
+ __82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke_2.124
+ __82-[TRIInternalServiceRequestHandler _activeExperimentFactorLevelsForNamespaceName:]_block_invoke.308
+ __83-[TRIExperimentDatabase _enumerateExperimentRecordsMatchingWhereClause:bind:block:]_block_invoke.106
+ __83-[TRIExperimentDatabase _enumerateExperimentRecordsMatchingWhereClause:bind:block:]_block_invoke.115
+ __83-[TRIExperimentDatabase _enumerateExperimentRecordsMatchingWhereClause:bind:block:]_block_invoke.148
+ __83-[TRITaskQueue _startImmediateTasksIfNotAlreadyQueued:guardedData:didStartNewWork:]_block_invoke.255
+ __83-[TRITaskQueue _startImmediateTasksIfNotAlreadyQueued:guardedData:didStartNewWork:]_block_invoke.256
+ __83-[TRITaskQueue _startImmediateTasksIfNotAlreadyQueued:guardedData:didStartNewWork:]_block_invoke.257
+ __84-[TRICKNativeArtifactProvider _fetchBMLTNotificationsWithCursor:options:completion:]_block_invoke.299
+ __84-[TRIInternalServiceRequestHandler setLastFetchDate:forContainer:teamId:completion:]_block_invoke.107
+ __84-[TRIRemoteAssetStoreOperator saveFactorPackToGlobalPath:fromTemporaryPath:factors:]_block_invoke.375
+ __86+[TRIXPCActivitySupport unsafe_immediatelyScheduleActivityWithLaunchDaemonDescriptor:]_block_invoke.134
+ __86-[TRICKNativeArtifactProvider fetchBMLTNotificationWithDeployment:options:completion:]_block_invoke.294
+ __86-[TRIFetchBMLTNotificationsTask _processBMLTCatalogArtifact:deactivatedBMLTs:context:]_block_invoke.53
+ __86-[TRIMaintenanceTask _synchronizePushService:usingRolloutDatabase:experimentDatabase:]_block_invoke.124
+ __86-[TRIMaintenanceTask _synchronizePushService:usingRolloutDatabase:experimentDatabase:]_block_invoke.127
+ __86-[TRISQLiteCKDatabase _loadArrayForRecordType:recordId:fieldKey:indexRange:txn:error:]_block_invoke.223
+ __86-[TRISQLiteCKDatabase _loadArrayForRecordType:recordId:fieldKey:indexRange:txn:error:]_block_invoke.241
+ __86-[TRISQLiteCKDatabase _replaceArrayFieldWithKey:recordType:recordId:values:txn:error:]_block_invoke.507
+ __86-[TRISQLiteCKDatabase _replaceArrayFieldWithKey:recordType:recordId:values:txn:error:]_block_invoke.527
+ __86-[TRISQLiteCKDatabase _replaceArrayFieldWithKey:recordType:recordId:values:txn:error:]_block_invoke_2.516
+ __86-[TRISQLiteCKDatabase _replaceArrayFieldWithKey:recordType:recordId:values:txn:error:]_block_invoke_3.517
+ __87-[TRICKNativeArtifactProvider _fetchRolloutNotificationsWithCursor:options:completion:]_block_invoke.220
+ __88-[TRIAssetStoreDatabase initWithPaths:databasePath:storageManagement:performMigrations:]_block_invoke.66
+ __88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.340
+ __88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.342
+ __89-[TRIAssetStore _linkDirectoryAssetWithIdentifier:toCurrentPath:futurePath:flockWitness:]_block_invoke.371
+ __90-[TRIExperimentDatabase namespacesAreAvailableForExperiment:startDate:endDate:namespaces:]_block_invoke.209
+ __90-[TRINamespaceResolverStorage overwriteActiveFactorProvidersUsingTransaction:fromContext:]_block_invoke.203
+ __90-[TRINamespaceResolverStorage overwriteActiveFactorProvidersUsingTransaction:fromContext:]_block_invoke.204
+ __90-[TRINamespaceResolverStorage overwriteActiveFactorProvidersUsingTransaction:fromContext:]_block_invoke.206
+ __90-[TRISQLiteCKDatabase _parseScalarExpression:forRecordType:toSQLExpr:paramBindings:error:]_block_invoke.318
+ __91-[TRIInternalServiceRequestHandler deregisterNamespaceWithNamespaceName:teamId:completion:]_block_invoke.153
+ __91-[TRIXPCNamespaceManagementRequestHandler deregisterNamespaceWithNamespaceName:completion:]_block_invoke.144
+ __91-[TRIXPCNamespaceManagementRequestHandler deregisterNamespaceWithNamespaceName:completion:]_block_invoke.145
+ __91-[TRIXPCNamespaceManagementRequestHandler deregisterNamespaceWithNamespaceName:completion:]_block_invoke_2.146
+ __92-[TRIInternalServiceRequestHandler activeBMLTInformationWithPrivacyFilterPolicy:completion:]_block_invoke.315
+ __92-[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]_block_invoke.341
+ __92-[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]_block_invoke.345
+ __92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.200
+ __92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.242
+ __92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.245
+ __92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.247
+ __92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.252
+ __92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.264
+ __92-[TRIXPCNamespaceManagementRequestHandler loadNamespaceMetadataForNamespaceName:completion:]_block_invoke.230
+ __92-[TRIXPCNamespaceManagementRequestHandler loadNamespaceMetadataForNamespaceName:completion:]_block_invoke.234
+ __92-[TRIXPCNamespaceManagementRequestHandler loadNamespaceMetadataForNamespaceName:completion:]_block_invoke_2.235
+ __93-[TRIActivationEventDatabase activationEventRecordWithParentId:factorPackSetId:deploymentId:]_block_invoke.62
+ __93-[TRIInternalServiceRequestHandler startDownloadNamespaceWithName:teamId:options:completion:]_block_invoke.164
+ __93-[TRIXPCNamespaceManagementRequestHandler startDownloadNamespaceWithName:options:completion:]_block_invoke.147
+ __93-[TRIXPCNamespaceManagementRequestHandler startDownloadNamespaceWithName:options:completion:]_block_invoke.161
+ __93-[TRIXPCNamespaceManagementRequestHandler startDownloadNamespaceWithName:options:completion:]_block_invoke_2.162
+ __94+[TRIXPCActivitySupport registerActivityWithLaunchDaemonDescriptor:checkInBlock:asyncHandler:]_block_invoke.120
+ __95-[TRIInternalServiceRequestHandler activeRolloutInformationWithPrivacyFilterPolicy:completion:]_block_invoke.177
+ __95-[TRIInternalServiceRequestHandler activeRolloutInformationWithPrivacyFilterPolicy:completion:]_block_invoke.179
+ __96-[TRICKNativeArtifactProvider _fetchExperimentWithExperimentId:deploymentId:options:completion:]_block_invoke.144
+ __96-[TRICKNativeArtifactProvider _fetchExperimentWithExperimentId:deploymentId:options:completion:]_block_invoke.147
+ __96-[TRISQLiteCKDatabase _evalFetchRecordsOperationWithRecordIds:recordType:desiredKeys:txn:error:]_block_invoke.425
+ __97-[TRIExperimentHistoryDatabase getAllAllocationStatusesForExperimentId:deploymentId:treatmentId:]_block_invoke.141
+ __98-[TRIXPCNamespaceManagementRequestHandler setProvisionalFactorPackId:forNamespaceName:completion:]_block_invoke.237
+ __98-[TRIXPCNamespaceManagementRequestHandler setProvisionalFactorPackId:forNamespaceName:completion:]_block_invoke.241
+ __98-[TRIXPCNamespaceManagementRequestHandler setProvisionalFactorPackId:forNamespaceName:completion:]_block_invoke_2.242
+ __Block_byref_object_copy_.244
+ __Block_byref_object_copy_.73
+ __Block_byref_object_dispose_.245
+ __Block_byref_object_dispose_.74
+ __OBJC_$_CLASS_METHODS_TRIBGSTManager
+ __OBJC_$_CLASS_METHODS_TRIBiomeExperimentUpdateStreamWriter
+ __OBJC_$_CLASS_METHODS_TRIClientExperimentArtifact(FactorPacks|CloudKit|Counterfactuals)
+ __OBJC_$_INSTANCE_METHODS_TRIBGSTManager
+ __OBJC_$_INSTANCE_METHODS_TRIBGSTManagerGuardedData
+ __OBJC_$_INSTANCE_METHODS_TRIClientExperimentArtifact(FactorPacks|CloudKit|Counterfactuals)
+ __OBJC_$_INSTANCE_METHODS_TRIExperimentRecord(VersionedNamespaces|Counterfactuals|Utils)
+ __OBJC_$_INSTANCE_METHODS_TRIExperimentUpdateProcessor
+ __OBJC_$_INSTANCE_METHODS_TRIExperimentUpdateScheduler
+ __OBJC_$_INSTANCE_VARIABLES_TRIBGSTManager
+ __OBJC_$_INSTANCE_VARIABLES_TRIBGSTManagerGuardedData
+ __OBJC_$_INSTANCE_VARIABLES_TRIExperimentUpdateProcessor
+ __OBJC_$_INSTANCE_VARIABLES_TRIExperimentUpdateScheduler
+ __OBJC_$_PROP_LIST_TRIExperimentUpdateScheduler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TRIExperimentUpdateSchedulerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TRIExperimentUpdateSchedulerProtocol
+ __OBJC_$_PROTOCOL_REFS_TRIExperimentUpdateSchedulerProtocol
+ __OBJC_CLASS_PROTOCOLS_$_TRIExperimentUpdateScheduler
+ __OBJC_CLASS_RO_$_TRIBGSTManager
+ __OBJC_CLASS_RO_$_TRIBGSTManagerGuardedData
+ __OBJC_CLASS_RO_$_TRIBiomeExperimentUpdateStreamWriter
+ __OBJC_CLASS_RO_$_TRIExperimentUpdateProcessor
+ __OBJC_CLASS_RO_$_TRIExperimentUpdateScheduler
+ __OBJC_LABEL_PROTOCOL_$_TRIExperimentUpdateSchedulerProtocol
+ __OBJC_METACLASS_RO_$_TRIBGSTManager
+ __OBJC_METACLASS_RO_$_TRIBGSTManagerGuardedData
+ __OBJC_METACLASS_RO_$_TRIBiomeExperimentUpdateStreamWriter
+ __OBJC_METACLASS_RO_$_TRIExperimentUpdateProcessor
+ __OBJC_METACLASS_RO_$_TRIExperimentUpdateScheduler
+ __OBJC_PROTOCOL_$_TRIExperimentUpdateSchedulerProtocol
+ ___105-[TRIBGSTManager scheduleDeactivationBGSTWithEarliestDeactivationTaskScheduledDate:gracePeriodInSeconds:]_block_invoke
+ ___113-[TRIClientExperimentArtifact(Counterfactuals) counterfactualsTreatmentsToFactorPackSetIdsWithActiveTreatmentId:]_block_invoke
+ ___135-[TRIExperimentUpdateProcessor _updateExperimentEndDateWithDeployment:withNewEndDate:scheduleDeactivationTask:scheduleDeactivationNow:]_block_invoke
+ ___234-[TRINamespaceResolverStorage _overwriteActiveFactorProvidersUsingGlobalPath:withNamespaceMap:rolloutDeploymentMap:experimentDeploymentMap:experimentTreatmentMap:treatmentFactorPackSetIdsMap:counterfactualTreatmentsMap:factorPackMap:]_block_invoke
+ ___29-[TRIBGSTManager expireBGST:]_block_invoke
+ ___36-[TRIBGSTManager markBGSTAsStarted:]_block_invoke
+ ___36-[TRIBGSTManager markBGSTAsStarted:]_block_invoke_2
+ ___40-[TRIActivateTreatmentTask dependencies]_block_invoke
+ ___41-[TRIBGSTManager markAllBGSTsAsCompleted]_block_invoke
+ ___41-[TRIBGSTManager markAllBGSTsAsCompleted]_block_invoke_2
+ ___42+[TRIActivateTreatmentTask parseFromData:]_block_invoke
+ ___42-[TRITaskQueue _scheduleDeactivationBGST:]_block_invoke
+ ___50-[TRIXPCActivityManager _registerDeactivationBGST]_block_invoke
+ ___50-[TRIXPCActivityManager _registerDeactivationBGST]_block_invoke_2
+ ___52-[TRITaskQueue resumeWithBGST:executeWhenSuspended:]_block_invoke
+ ___56-[TRIExpressionValidator _validSystemCovariateFunction:]_block_invoke
+ ___66-[TRIPushNotificationHandler _handleExperimentUpdateNotification:]_block_invoke
+ ___68+[TRIBiomeExperimentUpdateStreamWriter clearExperimentUpdatesStream]_block_invoke
+ ___79-[TRIExperimentDatabase hasRecordReferencingFactorPackSetId:withReferenceType:]_block_invoke_4
+ ___87+[TRIBiomeExperimentUpdateStreamWriter deleteObsoleteEventsFromExperimentsUpdateStream]_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88r_e28_v24?0"TRIFactorLevel"8^B16l
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88r_e33_v32?0"TRIFBFactorLevel"8Q16^B24l
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88r_e74_v32?0"TRIClientFactorPackStreamingParser"8"TRIFBFastFactorLevels"16^B24l
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s_e33_v24?0"TRIExperimentRecord"8^B16l
+ ___block_descriptor_32_e23_B16?0"TRITaskRecord"8l
+ ___block_descriptor_32_e26_B24?0"BMStoreEvent"8^B16l
+ ___block_descriptor_32_e35_v16?0"TRIBGSTManagerGuardedData"8l
+ ___block_descriptor_32_e39_v32?0"NSString"8"BGSystemTask"16^B24l
+ ___block_descriptor_40_e8_32s_e22_v16?0"BGSystemTask"8l
+ ___block_descriptor_40_e8_32s_e35_v16?0"TRIBGSTManagerGuardedData"8l
+ ___block_descriptor_40_e8_32s_e55_v32?0"NSString"8"NSString<TRIFactorPackSetId>"16^B24l
+ ___block_descriptor_48_e8_32s40s_e15_v28?0I8Q12^B20l
+ ___block_descriptor_48_e8_32s40s_e55_v32?0"NSString"8"NSString<TRIFactorPackSetId>"16^B24l
+ ___block_descriptor_48_e8_32s40w_e47_v24?0"TRIServerContext"8"<TRITaskQueuing>"16l
+ ___block_descriptor_48_e8_32w40w_e5_v8?0l
+ ___block_descriptor_56_e8_32s40s48s_e64_{_PASDBTransactionCompletion_=B}16?0"_PASSqlWriteTransaction"8l
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0l
+ ___block_descriptor_56_e8_32s40s_e35_v16?0"TRIBGSTManagerGuardedData"8l
+ ___block_descriptor_56_e8_32s_e26_B24?0"BMStoreEvent"8^B16l
+ ___block_descriptor_64_e8_32s40bs48bs_e47_v24?0"TRIServerContext"8"<TRITaskQueuing>"16l
+ ___block_descriptor_64_e8_32s40s48bs_e74_v32?0"TRIClientFactorPackStreamingParser"8"TRIFBFastFactorLevels"16^B24l
+ ___block_descriptor_88_e8_32s40s48s56r64r72r_e57_v40?0Q8"TRIClientBMLTArtifact"16"NSDate"24"NSError"32l
+ ___block_descriptor_88_e8_32s40s48s56r64r72r_e60_v40?0Q8"TRIClientRolloutArtifact"16"NSDate"24"NSError"32l
+ ___copy_helper_block_e8_32s40s48w
+ ___copy_helper_block_e8_32w40w
+ ___destroy_helper_block_e8_32s40s48w
+ ___destroy_helper_block_e8_32w40w
+ ___namespaceDictionaryForClientSelectedNamespace_block_invoke.490
+ __block_literal_global.100
+ __block_literal_global.110
+ __block_literal_global.112
+ __block_literal_global.125
+ __block_literal_global.127
+ __block_literal_global.129
+ __block_literal_global.140
+ __block_literal_global.142
+ __block_literal_global.171
+ __block_literal_global.215
+ __block_literal_global.217
+ __block_literal_global.224
+ __block_literal_global.261
+ __block_literal_global.279
+ __block_literal_global.281
+ __block_literal_global.286
+ __block_literal_global.296
+ __block_literal_global.298
+ __block_literal_global.305
+ __block_literal_global.311
+ __block_literal_global.318
+ __block_literal_global.32
+ __block_literal_global.33
+ __block_literal_global.332
+ __block_literal_global.334
+ __block_literal_global.339
+ __block_literal_global.348
+ __block_literal_global.350
+ __block_literal_global.351
+ __block_literal_global.358
+ __block_literal_global.37
+ __block_literal_global.400
+ __block_literal_global.41
+ __block_literal_global.415
+ __block_literal_global.422
+ __block_literal_global.424
+ __block_literal_global.426
+ __block_literal_global.441
+ __block_literal_global.450
+ __block_literal_global.463
+ __block_literal_global.492
+ __block_literal_global.509
+ __block_literal_global.518
+ __block_literal_global.521
+ __block_literal_global.532
+ __block_literal_global.549
+ __block_literal_global.553
+ __block_literal_global.560
+ __block_literal_global.563
+ __block_literal_global.610
+ __block_literal_global.63
+ __block_literal_global.68
+ __block_literal_global.79
+ __block_literal_global.97
+ __experimentUpdateProcessor
+ _categoricalValueForTriggerEvent
+ _dlopen
+ _dlopenHelper$BackgroundSystemTasks
+ _dlopenHelper$GenerativeModels
+ _dlopenHelperFlag$BackgroundSystemTasks
+ _dlopenHelperFlag$GenerativeModels
+ _gotLoadHelper_x25$_OBJC_CLASS_$_BGSystemTaskScheduler
+ _gotLoadHelper_x8$_OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _gotLoadHelper_x8$_OBJC_CLASS_$_BGSystemTaskScheduler
+ _gotLoadHelper_x8$_OBJC_CLASS_$_GMAvailabilityWrapper
+ _kCFPreferencesAnyHost
+ _objc_msgSend$Experiment
+ _objc_msgSend$NamespaceUpdates
+ _objc_msgSend$Trial
+ _objc_msgSend$_getCurrentPallasAudienceForAssetType:
+ _objc_msgSend$_getCurrentPallasURLForAssetType:
+ _objc_msgSend$_handleExperimentUpdateNotification:
+ _objc_msgSend$_overwriteActiveFactorProvidersUsingGlobalPath:withNamespaceMap:rolloutDeploymentMap:experimentDeploymentMap:experimentTreatmentMap:treatmentFactorPackSetIdsMap:counterfactualTreatmentsMap:factorPackMap:
+ _objc_msgSend$_registerDeactivationBGST
+ _objc_msgSend$_scheduleDeactivationBGST:
+ _objc_msgSend$_setPallasAudience:forAssetType:
+ _objc_msgSend$_setPallasURL:forAssetType:
+ _objc_msgSend$_submitDeactivationBGSTRequestAfterSeconds:gracePeriodInSeconds:
+ _objc_msgSend$_updateExperimentEndDateWithDeployment:withNewEndDate:scheduleDeactivationTask:scheduleDeactivationNow:
+ _objc_msgSend$appleIntelligenceState
+ _objc_msgSend$clearExperimentUpdatesStream
+ _objc_msgSend$counterfactualLogging
+ _objc_msgSend$counterfactualTreatmentIds
+ _objc_msgSend$counterfactualTreatments
+ _objc_msgSend$counterfactualTreatments_Count
+ _objc_msgSend$counterfactualsTreatmentsToFactorPackSetIds
+ _objc_msgSend$counterfactualsTreatmentsToFactorPackSetIdsWithActiveTreatmentId:
+ _objc_msgSend$currentWithUseCaseIdentifiers:
+ _objc_msgSend$deleteObsoleteEventsFromExperimentsUpdateStream
+ _objc_msgSend$deleteWithPolicy:eventsPassingTest:
+ _objc_msgSend$eliminableAssetTypes
+ _objc_msgSend$eventBody
+ _objc_msgSend$executeQuery:
+ _objc_msgSend$experimentUpdateNotification
+ _objc_msgSend$expireBGST:
+ _objc_msgSend$getBytes:length:
+ _objc_msgSend$hasCounterfactualLogging
+ _objc_msgSend$hasCounterfactualTreatmentReferencingFactorPackSetId:
+ _objc_msgSend$initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:counterfactualTreatmentIds:
+ _objc_msgSend$initWithExperimentDatabase:
+ _objc_msgSend$initWithFactorPackSetId:treatmentId:isCounterfactualTreatment:taskAttribution:experimentDeployment:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithNamespaceName:
+ _objc_msgSend$initWithNamespaceNames:experimentStatus:userId:experimentId:deploymentId:treatmentId:
+ _objc_msgSend$initWithNotificationChecker:hotfixScheduler:rollbackScheduler:experimentUpdateScheduler:
+ _objc_msgSend$initWithServerContext:asyncQueue:
+ _objc_msgSend$initWithUseCase:
+ _objc_msgSend$isCompatibleCounterfactual
+ _objc_msgSend$isCounterfactualTreatment
+ _objc_msgSend$markAllBGSTsAsCompleted
+ _objc_msgSend$markBGSTAsStarted:
+ _objc_msgSend$member:
+ _objc_msgSend$newEndDate
+ _objc_msgSend$next
+ _objc_msgSend$persistAIState:
+ _objc_msgSend$persistedAIState
+ _objc_msgSend$processUpdateOperationForExistingExperimentWithEndDate:withExperimentDeployment:
+ _objc_msgSend$pruner
+ _objc_msgSend$reactionForUpdateExperimentDeployment:
+ _objc_msgSend$registerForTaskWithIdentifier:usingQueue:launchHandler:
+ _objc_msgSend$resumeWithBGST:executeWhenSuspended:
+ _objc_msgSend$row
+ _objc_msgSend$scheduleAfter
+ _objc_msgSend$scheduleDeactivationBGSTWithEarliestDeactivationTaskScheduledDate:gracePeriodInSeconds:
+ _objc_msgSend$scheduleExperimentUpdateOperationsForExperimentWithNewEndDate:withDeployment:
+ _objc_msgSend$sendEvent:
+ _objc_msgSend$setCounterfactualTreatments:
+ _objc_msgSend$setExpirationHandler:
+ _objc_msgSend$setIsCounterfactualTreatment:
+ _objc_msgSend$setRequiresExternalPower:
+ _objc_msgSend$setRequiresNetworkConnectivity:
+ _objc_msgSend$setScheduleAfter:
+ _objc_msgSend$setTaskCompleted
+ _objc_msgSend$setTaskExpiredWithRetryAfter:error:
+ _objc_msgSend$setTrySchedulingBefore:
+ _objc_msgSend$sharedScheduler
+ _objc_msgSend$source
+ _objc_msgSend$submitTaskRequest:error:
+ _objc_msgSend$taskRequestForIdentifier:
+ _objc_msgSend$taskWithExperiment:treatmentId:factorPackSetId:counterfactualTreatments:taskAttributing:requiresTreatmentInstallation:capabilityModifier:startTime:taskOptions:
+ _objc_msgSend$taskWithFactorPackSetId:treatmentId:isCounterfactualTreatment:taskAttribution:experimentDeployment:
+ _objc_msgSend$updateTaskRequest:error:
+ _objc_msgSend$writeExperimentUpdateWithRecord:withExperimentStateIsActive:withUserId:
+ descriptor.descriptor.112
+ descriptor.descriptor.131
+ descriptor.descriptor.138
+ descriptor.descriptor.145
+ descriptor.descriptor.165
+ descriptor.descriptor.175
+ descriptor.descriptor.182
+ descriptor.descriptor.198
+ descriptor.descriptor.211
+ descriptor.descriptor.224
+ descriptor.descriptor.231
+ descriptor.descriptor.244
+ descriptor.descriptor.251
+ descriptor.descriptor.258
+ descriptor.descriptor.264
+ descriptor.descriptor.270
+ descriptor.descriptor.285
+ descriptor.descriptor.294
+ descriptor.descriptor.304
+ descriptor.descriptor.331
+ descriptor.descriptor.343
+ descriptor.descriptor.356
+ descriptor.descriptor.373
+ descriptor.descriptor.380
+ descriptor.descriptor.407
+ descriptor.descriptor.426
+ descriptor.descriptor.439
+ descriptor.descriptor.466
+ descriptor.fields.113
+ descriptor.fields.132
+ descriptor.fields.139
+ descriptor.fields.146
+ descriptor.fields.166
+ descriptor.fields.176
+ descriptor.fields.183
+ descriptor.fields.199
+ descriptor.fields.212
+ descriptor.fields.225
+ descriptor.fields.232
+ descriptor.fields.245
+ descriptor.fields.252
+ descriptor.fields.271
+ descriptor.fields.286
+ descriptor.fields.295
+ descriptor.fields.305
+ descriptor.fields.332
+ descriptor.fields.344
+ descriptor.fields.357
+ descriptor.fields.374
+ descriptor.fields.381
+ descriptor.fields.408
+ descriptor.fields.420
+ descriptor.fields.440
+ descriptor.fields.460
- +[TRIActivateTreatmentTask taskWithExperiment:treatmentId:factorPackSetId:taskAttributing:requiresTreatmentInstallation:capabilityModifier:startTime:taskOptions:]
- +[TRIFetchFactorPackSetTask taskWithFactorPackSetId:treatmentId:taskAttribution:experimentDeployment:]
- +[TRIMobileAssetUtil allTrialAssetTypes]
- +[TRIMobileAssetUtil siriTrialAssetTypes]
- -[TRIFetchFactorPackSetTask initWithFactorPackSetId:treatmentId:taskAttribution:experimentDeployment:]
- -[TRIFetchMultipleExperimentNotificationsTask _updateExperimentEndDateWithArtifact:context:database:scheduleDeactivationTask:scheduleDeactivationNow:]
- -[TRINamespaceResolverStorage _overwriteActiveFactorProvidersUsingGlobalPath:withNamespaceMap:rolloutDeploymentMap:experimentDeploymentMap:experimentTreatmentMap:factorPackMap:]
- -[TRIPushNotificationHandler initWithNotificationChecker:hotfixScheduler:rollbackScheduler:]
- GCC_except_table70
- GCC_except_table76
- GCC_except_table88
- GCC_except_table90
- GCC_except_table95
- GCC_except_table96
- __100-[TRIBackgroundMLTaskDatabase deactivateTaskDeployment:deactivatedFactorPackSetId:usingTransaction:]_block_invoke.122
- __101-[TRIBackgroundMLTaskHistoryDatabase getAllAllocationStatusesForBMLTId:deploymentId:factorPackSetId:]_block_invoke.70
- __101-[TRIFactorPackSetStorage enumerateCompatibleFactorPacksForFactorPackSet:usingLegacyPaths:withBlock:]_block_invoke.126
- __101-[TRIFactorPackSetStorage enumerateCompatibleFactorPacksForFactorPackSet:usingLegacyPaths:withBlock:]_block_invoke.129
- __101-[TRIRemoteAssetStoreOperator saveAssetWithIdentifier:sourcePath:flockWitness:removeSourceOnFailure:]_block_invoke.348
- __101-[TRIXPCNamespaceManagementRequestHandler getSandboxExtensionTokensForIdentifierQueryWithCompletion:]_block_invoke.248
- __101-[TRIXPCStatusRequestHandler evaluationHistoryRecordsForMLRuntimeWithLimit:newerThanDate:completion:]_block_invoke.130
- __102-[TRICKNativeArtifactProvider _fetchRolloutNotificationWithRolloutId:deploymentId:options:completion:]_block_invoke.217
- __102-[TRIRolloutHistoryDatabase getAllAllocationStatusesForRolloutId:rampId:deploymentId:factorPackSetId:]_block_invoke.99
- __103-[TRIActivateTreatmentBaseTask _experimentRecord:hasConflictWithExperimentsInDatabase:conflictEndTime:]_block_invoke.24
- __103-[TRIActivateTreatmentBaseTask _experimentRecord:hasConflictWithExperimentsInDatabase:conflictEndTime:]_block_invoke.25
- __103-[TRIXPCNamespaceManagementRequestHandler setPurgeabilityLevelsForFactors:forNamespaceName:completion:]_block_invoke.208
- __104+[TRIClientFactorPackUtils _enumerateAssetFactorLevelsInFlatBufferStorage:trialAssetBlock:maAssetBlock:]_block_invoke.297
- __104+[TRIClientFactorPackUtils _enumerateAssetFactorLevelsInFlatBufferStorage:trialAssetBlock:maAssetBlock:]_block_invoke.300
- __105-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:completion:]_block_invoke.103
- __105-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:completion:]_block_invoke.106
- __105-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:completion:]_block_invoke.107
- __105-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:completion:]_block_invoke.90
- __106-[TRIBackgroundMLTaskDatabase activateDeployment:withFactorPackSetId:targetingRuleIndex:usingTransaction:]_block_invoke.115
- __106-[TRIBackgroundMLTaskDatabase targetTaskDeployment:toFactorPackSetId:targetingRuleIndex:usingTransaction:]_block_invoke.107
- __106-[TRIRemoteAssetPatcher applyPatchWithFilename:toSrcDir:writingToEmptyDestDir:postPatchCompression:error:]_block_invoke.20
- __108+[TRISetupAssistantFetchUtils getIncompatibleNamespaceNamesForTriClientRollout:namespaceDescriptorProvider:]_block_invoke.44
- __108-[TRICKNativeArtifactProvider fetchAssetsWithIndexes:fromTreatmentWithRecordId:options:progress:completion:]_block_invoke.201
- __108-[TRIRolloutDatabase _enumerateRecordsMatchingWhereClause:bind:prependingWithClause:usingTransaction:block:]_block_invoke.111
- __108-[TRIRolloutDatabase _enumerateRecordsMatchingWhereClause:bind:prependingWithClause:usingTransaction:block:]_block_invoke.119
- __108-[TRIXPCNamespaceManagementRequestHandler rejectFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke.225
- __108-[TRIXPCNamespaceManagementRequestHandler rejectFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke.229
- __108-[TRIXPCNamespaceManagementRequestHandler rejectFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke_2.230
- __108-[TRIXPCNamespaceManagementRequestHandler statusOfDownloadForFactors:withNamespace:factorsState:completion:]_block_invoke.236
- __108-[TRIXPCNamespaceManagementRequestHandler statusOfDownloadForFactors:withNamespace:factorsState:completion:]_block_invoke.237
- __108-[TRIXPCNamespaceManagementRequestHandler statusOfDownloadForFactors:withNamespace:factorsState:completion:]_block_invoke.242
- __109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.378
- __109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.383
- __109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.386
- __109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.388
- __109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.392
- __109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.396
- __109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.399
- __109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.401
- __109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.409
- __109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.390
- __109-[TRIXPCNamespaceManagementRequestHandler promoteFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke.233
- __109-[TRIXPCNamespaceManagementRequestHandler promoteFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke.234
- __109-[TRIXPCNamespaceManagementRequestHandler promoteFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke_2.235
- __111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.312
- __111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.319
- __112-[TRIInternalServiceRequestHandler experimentNotificationsWithExperimentId:cloudKitContainer:teamId:completion:]_block_invoke.41
- __112-[TRIInternalServiceRequestHandler experimentNotificationsWithExperimentId:cloudKitContainer:teamId:completion:]_block_invoke.55
- __113+[TRICacheDeleteCallbacks registerCallbacksWithPaths:experimentDatabase:rolloutDatabase:taskQueue:loggingClient:]_block_invoke.86
- __113+[TRICacheDeleteCallbacks registerCallbacksWithPaths:experimentDatabase:rolloutDatabase:taskQueue:loggingClient:]_block_invoke.88
- __113-[TRIFetchTreatmentTask _downloadAndSaveMAAssets:options:downloadNotificationKey:context:errorResult:fetchError:]_block_invoke.302
- __113-[TRIPushServiceConnectionMultiplexer _expectedChannelIdsForRolloutDeployments:experimentIds:maxChannelsAllowed:]_block_invoke.20
- __114-[TRIXPCNamespaceManagementRequestHandler immediateDownloadForNamespaceNames:allowExpensiveNetworking:completion:]_block_invoke.190
- __114-[TRIXPCNamespaceManagementRequestHandler immediateDownloadForNamespaceNames:allowExpensiveNetworking:completion:]_block_invoke.192
- __114-[TRIXPCNamespaceManagementRequestHandler immediateDownloadForNamespaceNames:allowExpensiveNetworking:completion:]_block_invoke.199
- __115+[TRIReferenceManagedDir collectGarbageForManagedDir:withExternalReferenceStore:usingTempDir:managedDirWasDeleted:]_block_invoke.61
- __115-[TRICKNativeArtifactProvider _fetchRecordIdsForAssetsWithIds:options:cursor:cancelableOp:resultBuffer:completion:]_block_invoke.235
- __116-[TRICKNativeArtifactProvider _fetchRolloutNotificationsWithCursor:options:sinceDate:namespaceNames:resultsHandler:]_block_invoke.213
- __116-[TRIRolloutDatabase targetDeployment:toFactorPackSetId:targetingRuleIndex:deallocatedDeployments:usingTransaction:]_block_invoke.185
- __118+[TRIXPCNamespaceManagementRequestHandler _notificationKeyWithNamespace:assetIndexesByTreatment:assetIdsByFactorPack:]_block_invoke.165
- __118+[TRIXPCNamespaceManagementRequestHandler usingServerContext:deregisterNamespaceWithName:teamId:taskQueue:completion:]_block_invoke.320
- __118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.556
- __118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.562
- __118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.569
- __118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.580
- __118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.583
- __118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke_2.563
- __118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke_2.570
- __119-[TRICKNativeArtifactProvider fetchDiffSourceRecordIdsWithTargetAssetIds:isAcceptableSourceAssetId:options:completion:]_block_invoke.268
- __119-[TRICKNativeArtifactProvider fetchDiffSourceRecordIdsWithTargetAssetIds:isAcceptableSourceAssetId:options:completion:]_block_invoke.270
- __119-[TRIXPCNamespaceManagementRequestHandler startDownloadLevelsForFactors:withNamespace:factorsState:options:completion:]_block_invoke.171
- __119-[TRIXPCNamespaceManagementRequestHandler startDownloadLevelsForFactors:withNamespace:factorsState:options:completion:]_block_invoke.178
- __119-[TRIXPCNamespaceManagementRequestHandler startDownloadLevelsForFactors:withNamespace:factorsState:options:completion:]_block_invoke_2.179
- __122-[TRIXPCNamespaceManagementRequestHandler removeLevelsForFactors:withNamespace:factorsState:removeImmediately:completion:]_block_invoke.202
- __122-[TRIXPCNamespaceManagementRequestHandler removeLevelsForFactors:withNamespace:factorsState:removeImmediately:completion:]_block_invoke.206
- __122-[TRIXPCNamespaceManagementRequestHandler removeLevelsForFactors:withNamespace:factorsState:removeImmediately:completion:]_block_invoke_2.207
- __124-[TRIInternalServiceRequestHandler rolloutNotificationWithLatestDeploymentForRolloutId:cloudKitContainer:teamId:completion:]_block_invoke.60
- __124-[TRIInternalServiceRequestHandler rolloutNotificationWithLatestDeploymentForRolloutId:cloudKitContainer:teamId:completion:]_block_invoke.66
- __125-[TRIExperimentDatabase addExperimentWithExperimentDeployment:environment:type:status:startDate:endDate:namespaces:artifact:]_block_invoke.33
- __125-[TRIExperimentDatabase addExperimentWithExperimentDeployment:environment:type:status:startDate:endDate:namespaces:artifact:]_block_invoke.51
- __126-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:serverContext:completion:]_block_invoke.206
- __126-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:serverContext:completion:]_block_invoke.221
- __126-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:serverContext:completion:]_block_invoke.229
- __126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke.433
- __126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke.442
- __126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke.450
- __126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke.455
- __126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_2.439
- __126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_2.452
- __127-[TRICKNativeArtifactProvider _fetchNotificationsWithQueryType:withCursor:withNamespaceNames:sinceDate:options:resultsHandler:]_block_invoke.160
- __127-[TRICKNativeArtifactProvider _fetchNotificationsWithQueryType:withCursor:withNamespaceNames:sinceDate:options:resultsHandler:]_block_invoke.163
- __127-[TRICKNativeArtifactProvider _fetchNotificationsWithQueryType:withCursor:withNamespaceNames:sinceDate:options:resultsHandler:]_block_invoke.167
- __127-[TRIFetchOnDemandFactorsTask _asyncFetchMAAssetsFromFactorPacksWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.596
- __127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.468
- __127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.476
- __127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.489
- __127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke_2.485
- __128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.584
- __128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.586
- __128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.587
- __128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.592
- __128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke_2.585
- __129-[TRISelectRolloutNotificationListTask _processRolloutArtifact:rolloutsProcessed:remainingNamespaces:targeter:context:taskQueue:]_block_invoke.30
- __130-[TRICKNativeArtifactProvider _fetchExperimentsWithCursor:withNamespaceNames:sinceDate:fetchRollbacksOnly:options:resultsHandler:]_block_invoke.153
- __131-[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:privacyFilterPolicy:deploymentEnvironment:completion:]_block_invoke.43
- __131-[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:privacyFilterPolicy:deploymentEnvironment:completion:]_block_invoke.72
- __131-[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:privacyFilterPolicy:deploymentEnvironment:completion:]_block_invoke.80
- __131-[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:privacyFilterPolicy:deploymentEnvironment:completion:]_block_invoke.84
- __133+[TRIClientFactorPackUtils requiredAssetsForInstallationWithFactorPack:assetStore:maProvider:subscriptionSettings:aliasToUnaliasMap:]_block_invoke.344
- __138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke.546
- __138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke.547
- __138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke.551
- __144-[TRISQLiteCKDatabase _evalQueryOperationWithRecordType:predicate:sortDescriptors:offset:resultsLimit:desiredKeys:txn:error:recordMatchedBlock:]_block_invoke.162
- __144-[TRISQLiteCKDatabase _evalQueryOperationWithRecordType:predicate:sortDescriptors:offset:resultsLimit:desiredKeys:txn:error:recordMatchedBlock:]_block_invoke.164
- __145-[TRITaskQueue _partitionTaskGroup:byRunnabilityGivenCapabilities:runnableAtDate:topoSortedCurrentlyRunnable:blocked:allowOnlyRootTasksRunnable:]_block_invoke.261
- __151-[TRIFetchTreatmentTask _fetchAssetsWithArtifactProvider:recordId:experimentRecord:assetIndexes:downloadOptions:context:assetURLs:treatmentFetchError:]_block_invoke.361
- __154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.500
- __154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.501
- __154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.504
- __154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.507
- __154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.517
- __154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.518
- __154-[TRIPurgeableExperimentAndRolloutProvider _factorPackSetHasPurgeableFactorsWithFPSId:eagerFactors:overriddenFactors:purgeableNamespaces:returningAssets:]_block_invoke.35
- __156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.343
- __156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.344
- __158-[TRICKNativeArtifactProvider fetchDiffsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.273
- __158-[TRICKNativeArtifactProvider fetchDiffsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.277
- __158-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromFactorPacksWithContext:assetDiffFetchPlan:requiredAssetIds:downloadOptions:updatingAggregateProgress:]_block_invoke.527
- __159-[TRICKNativeArtifactProvider fetchAssetsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.242
- __159-[TRICKNativeArtifactProvider fetchAssetsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.244
- __159-[TRICKNativeArtifactProvider fetchAssetsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.252
- __163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.420
- __163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.425
- __163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.431
- __163-[TRIXPCNamespaceManagementRequestHandler registerNamespaceWithNamespaceName:compatibilityVersion:defaultsFileURL:applicationGroup:cloudKitContainerId:completion:]_block_invoke.129
- __163-[TRIXPCNamespaceManagementRequestHandler registerNamespaceWithNamespaceName:compatibilityVersion:defaultsFileURL:applicationGroup:cloudKitContainerId:completion:]_block_invoke.91
- __163-[TRIXPCNamespaceManagementRequestHandler registerNamespaceWithNamespaceName:compatibilityVersion:defaultsFileURL:applicationGroup:cloudKitContainerId:completion:]_block_invoke.93
- __164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.318
- __164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.320
- __164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.329
- __165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.399
- __165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.405
- __165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.418
- __165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.425
- __165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.428
- __165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.433
- __165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.419
- __170-[TRIRolloutDatabase deactivateDeploymentsWithRolloutId:deactivatedDeployment:deactivatedFactorPackSetId:deactivatedRampId:deactivationStateTransitions:usingTransaction:]_block_invoke.204
- __174-[TRIPurgeableExperimentAndRolloutProvider _purgeablesForRolloutsFromNamespaces:eagerFactors:overriddenFactors:shouldGenerateAssetPaths:purgeableExperiments:purgeableAssets:]_block_invoke.28
- __177-[TRINamespaceResolverStorage _overwriteActiveFactorProvidersUsingGlobalPath:withNamespaceMap:rolloutDeploymentMap:experimentDeploymentMap:experimentTreatmentMap:factorPackMap:]_block_invoke.204
- __177-[TRIPurgeableExperimentAndRolloutProvider _purgeablesForExperimentsFromNamespaces:eagerFactors:overriddenFactors:shouldGenerateAssetPaths:purgeableExperiments:purgeableAssets:]_block_invoke.25
- __177-[TRIRolloutDatabase activateDeployment:withFactorPackSetId:targetingRuleIndex:deactivatedDeployments:deactivatedFactorPackSetIds:deactivationStateTransitions:usingTransaction:]_block_invoke.194
- __178-[TRIInternalServiceRequestHandler registerNamespaceWithNamespaceName:compatibilityVersion:defaultsFileURL:teamId:appContainerId:appContainerType:cloudKitContainerId:completion:]_block_invoke.108
- __179+[TRIXPCNamespaceManagementRequestHandler _immediateDownloadForNamespaceNames:usingEntitlementWitness:serverContext:taskQueue:allowExpensiveNetworking:taskAttribution:completion:]_block_invoke.391
- __184+[TRIClientFactorPackUtils unlinkedOnDemandAssetsWithFactorPack:flatbufferFactorLevels:factorPackPath:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:unlinkedMAAssetsOnDisk:]_block_invoke.355
- __184+[TRIClientFactorPackUtils unlinkedOnDemandAssetsWithFactorPack:flatbufferFactorLevels:factorPackPath:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:unlinkedMAAssetsOnDisk:]_block_invoke.358
- __19-[TRIDServer start]_block_invoke.334
- __19-[TRIDServer start]_block_invoke.343
- __19-[TRIDServer start]_block_invoke.346
- __19-[TRIDServer start]_block_invoke.350
- __220+[TRIDiffableAssetBuilder buildAndSaveDiffableAssetsWithAssetIds:metadataForAssetId:artifactProvider:options:paths:assetsDownloadSize:perAssetIdCompletionBlockOnSuccess:perAssetIdCompletionBlockOnError:retryAfter:error:]_block_invoke.33
- __220+[TRIDiffableAssetBuilder buildAndSaveDiffableAssetsWithAssetIds:metadataForAssetId:artifactProvider:options:paths:assetsDownloadSize:perAssetIdCompletionBlockOnSuccess:perAssetIdCompletionBlockOnError:retryAfter:error:]_block_invoke.38
- __220+[TRIDiffableAssetBuilder buildAndSaveDiffableAssetsWithAssetIds:metadataForAssetId:artifactProvider:options:paths:assetsDownloadSize:perAssetIdCompletionBlockOnSuccess:perAssetIdCompletionBlockOnError:retryAfter:error:]_block_invoke.43
- __220+[TRIDiffableAssetBuilder buildAndSaveDiffableAssetsWithAssetIds:metadataForAssetId:artifactProvider:options:paths:assetsDownloadSize:perAssetIdCompletionBlockOnSuccess:perAssetIdCompletionBlockOnError:retryAfter:error:]_block_invoke.45
- __220+[TRIDiffableAssetBuilder buildAndSaveDiffableAssetsWithAssetIds:metadataForAssetId:artifactProvider:options:paths:assetsDownloadSize:perAssetIdCompletionBlockOnSuccess:perAssetIdCompletionBlockOnError:retryAfter:error:]_block_invoke.61
- __220+[TRIDiffableAssetBuilder buildAndSaveDiffableAssetsWithAssetIds:metadataForAssetId:artifactProvider:options:paths:assetsDownloadSize:perAssetIdCompletionBlockOnSuccess:perAssetIdCompletionBlockOnError:retryAfter:error:]_block_invoke_2.39
- __257+[TRIXPCNamespaceManagementRequestHandler _startDownloadAssetIndexesByTreatment:usingEntitlementWitness:serverContext:taskQueue:experimentIds:assetIdsByFactorPack:rolloutFactorNames:rolloutDeployments:namespace:taskAttribution:factorsState:notificationKey:]_block_invoke.364
- __257+[TRIXPCNamespaceManagementRequestHandler _startDownloadAssetIndexesByTreatment:usingEntitlementWitness:serverContext:taskQueue:experimentIds:assetIdsByFactorPack:rolloutFactorNames:rolloutDeployments:namespace:taskAttribution:factorsState:notificationKey:]_block_invoke.368
- __257+[TRIXPCNamespaceManagementRequestHandler _startDownloadAssetIndexesByTreatment:usingEntitlementWitness:serverContext:taskQueue:experimentIds:assetIdsByFactorPack:rolloutFactorNames:rolloutDeployments:namespace:taskAttribution:factorsState:notificationKey:]_block_invoke.372
- __27-[TRITaskDatabase allTasks]_block_invoke.108
- __27-[TRITaskDatabase allTasks]_block_invoke.112
- __27-[TRITaskDatabase allTasks]_block_invoke.121
- __27-[TRITaskDatabase allTasks]_block_invoke_2.125
- __34-[TRICancelableMAOperation cancel]_block_invoke.468
- __36-[TRISQLiteCKDatabase addOperation:]_block_invoke.86
- __39-[TRIRolloutHistoryDatabase addRecord:]_block_invoke.35
- __40-[TRITaskDatabase tasksDependentOnTask:]_block_invoke.200
- __41+[TRIClientFactorPackUtils uniqueAssets:]_block_invoke.366
- __41-[TRITaskDatabase _tasksForQuery:onPrep:]_block_invoke.142
- __41-[TRITaskDatabase _tasksForQuery:onPrep:]_block_invoke_2.143
- __42-[TRIDatabase migration_addTaskCapability]_block_invoke.302
- __42-[TRIExperimentHistoryDatabase addRecord:]_block_invoke.36
- __42-[TRIKVStore blobForKey:usingTransaction:]_block_invoke.25
- __44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.369
- __44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.382
- __44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.401
- __44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.415
- __44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.420
- __44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.421
- __44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.383
- __44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.402
- __44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.422
- __46-[TRIRolloutDatabase addNewRolloutWithRecord:]_block_invoke.33
- __46-[TRIRolloutDatabase addNewRolloutWithRecord:]_block_invoke.37
- __46-[TRIRolloutDatabase addNewRolloutWithRecord:]_block_invoke.52
- __46-[TRISQLiteCKDatabase _processQueryOperation:]_block_invoke.101
- __46-[TRITaskQueue _registerRetryActivityForDate:]_block_invoke.304
- __47-[TRIFetchOnDemandFactorsTask _asPersistedTask]_block_invoke.610
- __47-[TRIFetchOnDemandFactorsTask _asPersistedTask]_block_invoke_2.612
- __47-[TRISQLiteCKDatabase _upsertRecord:txn:error:]_block_invoke.461
- __47-[TRISQLiteCKDatabase _upsertRecord:txn:error:]_block_invoke_2.462
- __47-[TRISQLiteCKDatabase _upsertRecord:txn:error:]_block_invoke_3.466
- __47-[TRISQLiteCKDatabase _upsertRecord:txn:error:]_block_invoke_4.473
- __47-[TRISQLiteCKDatabase _upsertRecord:txn:error:]_block_invoke_5.474
- __47-[TRITaskQueue _finalizeTask:withId:runResult:]_block_invoke.203
- __47-[TRITaskQueue _finalizeTask:withId:runResult:]_block_invoke.205
- __49-[TRITaskDatabase removeTaskWithId:cleanupBlock:]_block_invoke.78
- __49-[TRITaskDatabase removeTaskWithId:cleanupBlock:]_block_invoke.83
- __49-[TRITaskDatabase removeTaskWithId:cleanupBlock:]_block_invoke_2.87
- __49-[TRITaskDatabase removeTaskWithId:cleanupBlock:]_block_invoke_3.91
- __50-[TRITaskDatabase directDependenciesOfTaskWithId:]_block_invoke.196
- __50-[TRITaskQueue _registerTaskQueueActivityForDate:]_block_invoke.308
- __50-[TRITaskQueue _registerTaskQueueActivityForDate:]_block_invoke.311
- __50-[TRITaskQueue cancelTasksWithTag:excludingTasks:]_block_invoke.288
- __52-[TRIRetargetAllTask runUsingContext:withTaskQueue:]_block_invoke.27
- __52-[TRIRetargetAllTask runUsingContext:withTaskQueue:]_block_invoke.32
- __53-[TRIMAProvider installedAssetsMatchingFullAssetIds:]_block_invoke.494
- __53-[TRIXPCActivityManager _registerPostUpgradeActivity]_block_invoke.344
- __55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.389
- __56-[TRIXPCStatusRequestHandler bmltRecordsWithCompletion:]_block_invoke.150
- __56-[TRIXPCStatusRequestHandler bmltRecordsWithCompletion:]_block_invoke.151
- __57-[TRIAssetPurger purgeableAssetSizeForPurgeabilityLevel:]_block_invoke.101
- __57-[TRIAssetPurger purgeableAssetSizeForPurgeabilityLevel:]_block_invoke.105
- __57-[TRIDisenrollRolloutTask runUsingContext:withTaskQueue:]_block_invoke.50
- __57-[TRIFetchOnDemandFactorsTask _requiredDiskSpaceForPlan:]_block_invoke.451
- __57-[TRIXPCActivityManager _registerHotfixTargetingActivity]_block_invoke.363
- __57-[TRIXPCActivityManager _registerHotfixTargetingActivity]_block_invoke_2.364
- __58-[TRIXPCActivityManager _registerFetchExperimentsActivity]_block_invoke.334
- __59-[TRIActivateTreatmentTask runTaskUsingContext:experiment:]_block_invoke.158
- __59-[TRIActivateTreatmentTask runTaskUsingContext:experiment:]_block_invoke.160
- __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.480
- __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.487
- __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.491
- __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.511
- __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.512
- __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.529
- __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.535
- __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.539
- __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.543
- __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.546
- __59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.531
- __59-[TRITaskQueue activeActivityDescriptorGrantingCapability:]_block_invoke.329
- __59-[TRIXPCStatusRequestHandler rolloutRecordsWithCompletion:]_block_invoke.153
- __59-[TRIXPCStatusRequestHandler rolloutRecordsWithCompletion:]_block_invoke.154
- __60-[TRIBackgroundMLTaskDatabase taskRecordWithTaskDeployment:]_block_invoke.97
- __60-[TRIDeactivateTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.53
- __60-[TRIDeactivateTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.66
- __60-[TRIDeactivateTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.72
- __60-[TRIDeactivateTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.87
- __60-[TRIRolloutDatabase recordWithDeployment:usingTransaction:]_block_invoke.128
- __60-[TRIXPCActivityManager _registerCellularActivityWithDelay:]_block_invoke.331
- __60-[TRIXPCActivityManager registerSetupAssistantFetchActivity]_block_invoke.358
- __60-[TRIXPCActivityManager registerSetupAssistantFetchActivity]_block_invoke.359
- __61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.427
- __61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.436
- __61-[TRITaskDatabase addTask:startTime:tags:dependencies:error:]_block_invoke.31
- __61-[TRITaskDatabase addTask:startTime:tags:dependencies:error:]_block_invoke.34
- __61-[TRITaskDatabase addTask:startTime:tags:dependencies:error:]_block_invoke.44
- __61-[TRITaskDatabase addTask:startTime:tags:dependencies:error:]_block_invoke.54
- __61-[TRITaskDatabase addTask:startTime:tags:dependencies:error:]_block_invoke.62
- __62-[TRIInternalServiceRequestHandler taskRecordsWithCompletion:]_block_invoke.31
- __63-[TRIFetchBMLTNotificationsTask runUsingContext:withTaskQueue:]_block_invoke.73
- __63-[TRIFetchBMLTNotificationsTask runUsingContext:withTaskQueue:]_block_invoke.74
- __63-[TRITaskQueue enumerateTasksWithTagsIntersectingTagSet:block:]_block_invoke.291
- __63-[TRITaskQueue enumerateTasksWithTagsIntersectingTagSet:block:]_block_invoke.292
- __63-[TRITaskQueue enumerateTasksWithTagsIntersectingTagSet:block:]_block_invoke.294
- __64-[TRIInternalServiceRequestHandler setFailureInjectionDelegate:]_block_invoke.93
- __65-[TRIMaintenanceTask _cleanupUnusedContentWithContext:nextTasks:]_block_invoke.79
- __65-[TRIMaintenanceTask _cleanupUnusedContentWithContext:nextTasks:]_block_invoke.85
- __65-[TRIMaintenanceTask _cleanupUnusedContentWithContext:nextTasks:]_block_invoke.90
- __65-[TRIMaintenanceTask _cleanupUnusedContentWithContext:nextTasks:]_block_invoke.94
- __65-[TRIMaintenanceTask _cleanupUnusedContentWithContext:nextTasks:]_block_invoke_2.91
- __66-[TRIAssetStoreDatabase enumerateAllAutoAssetReferencesWithBlock:]_block_invoke.151
- __66-[TRIExperimentDatabase experimentRecordWithExperimentDeployment:]_block_invoke.165
- __66-[TRIFetchBMLTNotificationsTask fetchSingleDeploymentWithContext:]_block_invoke.66
- __66-[TRIInternalServiceRequestHandler submitTask:options:completion:]_block_invoke.70
- __66-[TRISQLiteCKDatabase _deleteRecordsWithRecordIds:recordType:txn:]_block_invoke.432
- __67-[TRIActiveLowLevelFactorsWriter _remoteWriteExperimentData:error:]_block_invoke.82
- __67-[TRIContentTracker _addOrDropRefWithContentIdentifier:changeType:]_block_invoke.60
- __67-[TRIContentTracker _addOrDropRefWithContentIdentifier:changeType:]_block_invoke.70
- __69-[TRIAssetStoreDatabase addReferenceToAutoAssetId:forLifetimeOfPath:]_block_invoke.108
- __69-[TRIAssetStoreDatabase addReferenceToAutoAssetId:forLifetimeOfPath:]_block_invoke.116
- __69-[TRIAssetStoreDatabase addReferenceToAutoAssetId:forLifetimeOfPath:]_block_invoke_2.123
- __69-[TRIBackgroundMLTaskDatabase deactivateDeployment:usingTransaction:]_block_invoke.118
- __69-[TRIFetchFactorPackSetTask _requiredAssetsForFactorPackSet:context:]_block_invoke.377
- __69-[TRITaskQueue resumeWithXPCActivityDescriptor:executeWhenSuspended:]_block_invoke.91
- __69-[TRITaskQueue resumeWithXPCActivityDescriptor:executeWhenSuspended:]_block_invoke.99
- __69-[TRIXPCStatusRequestHandler activeEvaluationsForBMLTWithCompletion:]_block_invoke.136
- __69-[TRIXPCStatusRequestHandler activeEvaluationsForBMLTWithCompletion:]_block_invoke.141
- __70-[TRIRunningXPCActivityDescriptor initWithActivity:capabilities:name:]_block_invoke.17
- __70-[TRISelectRolloutNotificationListTask runUsingContext:withTaskQueue:]_block_invoke.63
- __71-[TRIActivateTargetedBMLTDeploymentTask runUsingContext:withTaskQueue:]_block_invoke.76
- __71-[TRIAssetPurger purgeAssetsForPurgeabilityLevel:requestedPurgeAmount:]_block_invoke.126
- __71-[TRICKNativeArtifactProvider fetchTreatmentWithId:options:completion:]_block_invoke.192
- __71-[TRIInternalServiceRequestHandler removeUnusedChannelsWithCompletion:]_block_invoke.103
- __71-[TRIInternalServiceRequestHandler removeUnusedChannelsWithCompletion:]_block_invoke.98
- __72-[TRIAssetPurger _enumeratePurgeCandidatesForPurgeableConstructs:block:]_block_invoke.142
- __72-[TRIAssetPurger _enumeratePurgeCandidatesForPurgeableConstructs:block:]_block_invoke.146
- __72-[TRIXPCActivityManager _scheduleFetchTaskWithActivityDescriptor:label:]_block_invoke.314
- __73-[TRIFetchFactorPackSetTask _saveFactorPackSet:requiredAssetMap:context:]_block_invoke.454
- __73-[TRIFetchOnDemandFactorsTask _updateFactorPacksByMergingAssets:context:]_block_invoke.405
- __73-[TRITaskQueue _evaluateRunConditionsWithGuardedData:shouldContinueWork:]_block_invoke.85
- __74-[TRIAssetStoreDatabase enumerateAssetIdsWithoutLiveReferencesUsingBlock:]_block_invoke.196
- __74-[TRIAssetStoreDatabase enumerateAssetIdsWithoutLiveReferencesUsingBlock:]_block_invoke_2.206
- __74-[TRIInternalServiceRequestHandler dynamicNamespaceRecordsWithCompletion:]_block_invoke.150
- __74-[TRISQLiteMADatabase eliminatePromotedNeverLockedForSelector:completion:]_block_invoke.408
- __74-[TRISQLiteMADatabase eliminatePromotedNeverLockedForSelector:completion:]_block_invoke_2.409
- __74-[TRISQLiteMADatabase eliminatePromotedNeverLockedForSelector:completion:]_block_invoke_3.413
- __74-[TRIXPCStatusRequestHandler activeEvaluationsForMLRuntimeWithCompletion:]_block_invoke.110
- __74-[TRIXPCStatusRequestHandler activeEvaluationsForMLRuntimeWithCompletion:]_block_invoke.123
- __75-[TRICKNativeArtifactProvider fetchFactorPackSetWithId:options:completion:]_block_invoke.224
- __77-[TRIRolloutHistoryDatabase _enumerateRecordsMatchingWhereClause:bind:block:]_block_invoke.49
- __77-[TRIRolloutHistoryDatabase _enumerateRecordsMatchingWhereClause:bind:block:]_block_invoke.51
- __77-[TRIRolloutHistoryDatabase _enumerateRecordsMatchingWhereClause:bind:block:]_block_invoke.75
- __78-[NSFileManager(TRIServer) triRemoveCachedANEBinariesForModelsFromPath:error:]_block_invoke.24
- __78-[NSFileManager(TRIServer) triRemoveCachedANEBinariesForModelsFromPath:error:]_block_invoke.51
- __78-[TRIDatabase initWithPaths:databasePath:storageManagement:performMigrations:]_block_invoke.52
- __78-[TRIDatabase initWithPaths:databasePath:storageManagement:performMigrations:]_block_invoke.55
- __78-[TRIInternalServiceRequestHandler resumeSQLiteCKDatabaseQueueWithCompletion:]_block_invoke.97
- __78-[TRIXPCActivityManager _scheduleMaintenanceTaskWithActivityDescriptor:label:]_block_invoke.320
- __79-[TRIFactorPackSetStorage migrateEligibleFactorPacksToGlobalWithServerContext:]_block_invoke.140
- __79-[TRIFactorPackSetStorage migrateEligibleFactorPacksToGlobalWithServerContext:]_block_invoke.143
- __79-[TRIInternalServiceRequestHandler suspendSQLiteCKDatabaseQueueWithCompletion:]_block_invoke.95
- __79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.501
- __79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.508
- __79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.518
- __79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.522
- __79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke_2.509
- __80-[TRIExperimentHistoryDatabase _enumerateRecordsMatchingWhereClause:bind:block:]_block_invoke.53
- __80-[TRIExperimentHistoryDatabase _enumerateRecordsMatchingWhereClause:bind:block:]_block_invoke.55
- __80-[TRIExperimentHistoryDatabase _enumerateRecordsMatchingWhereClause:bind:block:]_block_invoke.85
- __80-[TRIInternalServiceRequestHandler lastFetchDateForContainer:teamId:completion:]_block_invoke.78
- __81-[TRITaskQueue _addTask:options:guardedData:taskIdOut:accumulatedNewTaskRecords:]_block_invoke.273
- __81-[TRIXPCActivityManager _registerPostUpgradeActivityRequireInexpensiveNetworking]_block_invoke.351
- __82-[TRICKNativeArtifactProvider fetchBMLTCatalogNotificationWithOptions:completion:]_block_invoke.281
- __82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.106
- __82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.111
- __82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.114
- __82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.116
- __82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.124
- __82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.127
- __82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.129
- __82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.134
- __82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke_2.118
- __82-[TRIInternalServiceRequestHandler _activeExperimentFactorLevelsForNamespaceName:]_block_invoke.285
- __83-[TRIExperimentDatabase _enumerateExperimentRecordsMatchingWhereClause:bind:block:]_block_invoke.100
- __83-[TRIExperimentDatabase _enumerateExperimentRecordsMatchingWhereClause:bind:block:]_block_invoke.103
- __83-[TRIExperimentDatabase _enumerateExperimentRecordsMatchingWhereClause:bind:block:]_block_invoke.142
- __83-[TRITaskQueue _startImmediateTasksIfNotAlreadyQueued:guardedData:didStartNewWork:]_block_invoke.240
- __83-[TRITaskQueue _startImmediateTasksIfNotAlreadyQueued:guardedData:didStartNewWork:]_block_invoke.241
- __83-[TRITaskQueue _startImmediateTasksIfNotAlreadyQueued:guardedData:didStartNewWork:]_block_invoke.242
- __84-[TRICKNativeArtifactProvider _fetchBMLTNotificationsWithCursor:options:completion:]_block_invoke.293
- __84-[TRIInternalServiceRequestHandler setLastFetchDate:forContainer:teamId:completion:]_block_invoke.85
- __84-[TRIRemoteAssetStoreOperator saveFactorPackToGlobalPath:fromTemporaryPath:factors:]_block_invoke.369
- __86+[TRIXPCActivitySupport unsafe_immediatelyScheduleActivityWithLaunchDaemonDescriptor:]_block_invoke.128
- __86-[TRICKNativeArtifactProvider fetchBMLTNotificationWithDeployment:options:completion:]_block_invoke.288
- __86-[TRIFetchBMLTNotificationsTask _processBMLTCatalogArtifact:deactivatedBMLTs:context:]_block_invoke.47
- __86-[TRIMaintenanceTask _synchronizePushService:usingRolloutDatabase:experimentDatabase:]_block_invoke.116
- __86-[TRIMaintenanceTask _synchronizePushService:usingRolloutDatabase:experimentDatabase:]_block_invoke.119
- __86-[TRISQLiteCKDatabase _loadArrayForRecordType:recordId:fieldKey:indexRange:txn:error:]_block_invoke.217
- __86-[TRISQLiteCKDatabase _loadArrayForRecordType:recordId:fieldKey:indexRange:txn:error:]_block_invoke.235
- __86-[TRISQLiteCKDatabase _replaceArrayFieldWithKey:recordType:recordId:values:txn:error:]_block_invoke.501
- __86-[TRISQLiteCKDatabase _replaceArrayFieldWithKey:recordType:recordId:values:txn:error:]_block_invoke.521
- __86-[TRISQLiteCKDatabase _replaceArrayFieldWithKey:recordType:recordId:values:txn:error:]_block_invoke_2.510
- __86-[TRISQLiteCKDatabase _replaceArrayFieldWithKey:recordType:recordId:values:txn:error:]_block_invoke_3.511
- __87-[TRICKNativeArtifactProvider _fetchRolloutNotificationsWithCursor:options:completion:]_block_invoke.214
- __88-[TRIAssetStoreDatabase initWithPaths:databasePath:storageManagement:performMigrations:]_block_invoke.60
- __88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.334
- __88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.336
- __89-[TRIAssetStore _linkDirectoryAssetWithIdentifier:toCurrentPath:futurePath:flockWitness:]_block_invoke.365
- __90-[TRIExperimentDatabase namespacesAreAvailableForExperiment:startDate:endDate:namespaces:]_block_invoke.203
- __90-[TRINamespaceResolverStorage overwriteActiveFactorProvidersUsingTransaction:fromContext:]_block_invoke.179
- __90-[TRINamespaceResolverStorage overwriteActiveFactorProvidersUsingTransaction:fromContext:]_block_invoke.192
- __90-[TRISQLiteCKDatabase _parseScalarExpression:forRecordType:toSQLExpr:paramBindings:error:]_block_invoke.312
- __91-[TRIInternalServiceRequestHandler deregisterNamespaceWithNamespaceName:teamId:completion:]_block_invoke.132
- __91-[TRIXPCNamespaceManagementRequestHandler deregisterNamespaceWithNamespaceName:completion:]_block_invoke.132
- __91-[TRIXPCNamespaceManagementRequestHandler deregisterNamespaceWithNamespaceName:completion:]_block_invoke.133
- __91-[TRIXPCNamespaceManagementRequestHandler deregisterNamespaceWithNamespaceName:completion:]_block_invoke_2.134
- __92-[TRIInternalServiceRequestHandler activeBMLTInformationWithPrivacyFilterPolicy:completion:]_block_invoke.292
- __92-[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]_block_invoke.318
- __92-[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]_block_invoke.322
- __92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.194
- __92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.236
- __92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.239
- __92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.241
- __92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.246
- __92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.258
- __92-[TRIXPCNamespaceManagementRequestHandler loadNamespaceMetadataForNamespaceName:completion:]_block_invoke.212
- __92-[TRIXPCNamespaceManagementRequestHandler loadNamespaceMetadataForNamespaceName:completion:]_block_invoke.216
- __92-[TRIXPCNamespaceManagementRequestHandler loadNamespaceMetadataForNamespaceName:completion:]_block_invoke_2.217
- __93-[TRIActivationEventDatabase activationEventRecordWithParentId:factorPackSetId:deploymentId:]_block_invoke.56
- __93-[TRIInternalServiceRequestHandler startDownloadNamespaceWithName:teamId:options:completion:]_block_invoke.143
- __93-[TRIXPCNamespaceManagementRequestHandler startDownloadNamespaceWithName:options:completion:]_block_invoke.135
- __93-[TRIXPCNamespaceManagementRequestHandler startDownloadNamespaceWithName:options:completion:]_block_invoke.149
- __93-[TRIXPCNamespaceManagementRequestHandler startDownloadNamespaceWithName:options:completion:]_block_invoke_2.150
- __94+[TRIXPCActivitySupport registerActivityWithLaunchDaemonDescriptor:checkInBlock:asyncHandler:]_block_invoke.114
- __95-[TRIInternalServiceRequestHandler activeRolloutInformationWithPrivacyFilterPolicy:completion:]_block_invoke.156
- __95-[TRIInternalServiceRequestHandler activeRolloutInformationWithPrivacyFilterPolicy:completion:]_block_invoke.158
- __96-[TRICKNativeArtifactProvider _fetchExperimentWithExperimentId:deploymentId:options:completion:]_block_invoke.138
- __96-[TRICKNativeArtifactProvider _fetchExperimentWithExperimentId:deploymentId:options:completion:]_block_invoke.141
- __96-[TRISQLiteCKDatabase _evalFetchRecordsOperationWithRecordIds:recordType:desiredKeys:txn:error:]_block_invoke.419
- __97-[TRIExperimentHistoryDatabase getAllAllocationStatusesForExperimentId:deploymentId:treatmentId:]_block_invoke.135
- __98-[TRIAssetStoreDatabase enumerateOnDiskMAReferencesWithoutCorrespondingDatabaseEntriesUsingBlock:]_block_invoke.159
- __98-[TRIAssetStoreDatabase enumerateOnDiskMAReferencesWithoutCorrespondingDatabaseEntriesUsingBlock:]_block_invoke.164
- __98-[TRIXPCNamespaceManagementRequestHandler setProvisionalFactorPackId:forNamespaceName:completion:]_block_invoke.219
- __98-[TRIXPCNamespaceManagementRequestHandler setProvisionalFactorPackId:forNamespaceName:completion:]_block_invoke.223
- __98-[TRIXPCNamespaceManagementRequestHandler setProvisionalFactorPackId:forNamespaceName:completion:]_block_invoke_2.224
- __Block_byref_object_copy_.238
- __Block_byref_object_copy_.67
- __Block_byref_object_dispose_.239
- __Block_byref_object_dispose_.68
- __OBJC_$_CLASS_METHODS_TRIClientExperimentArtifact(FactorPacks|CloudKit)
- __OBJC_$_INSTANCE_METHODS_TRIClientExperimentArtifact(FactorPacks|CloudKit)
- __OBJC_$_INSTANCE_METHODS_TRIExperimentRecord(VersionedNamespaces|Utils)
- ___150-[TRIFetchMultipleExperimentNotificationsTask _updateExperimentEndDateWithArtifact:context:database:scheduleDeactivationTask:scheduleDeactivationNow:]_block_invoke
- ___177-[TRINamespaceResolverStorage _overwriteActiveFactorProvidersUsingGlobalPath:withNamespaceMap:rolloutDeploymentMap:experimentDeploymentMap:experimentTreatmentMap:factorPackMap:]_block_invoke
- ___block_descriptor_40_e8_32r_e18_16?0"NSString"8l
- ___block_descriptor_40_e8_32r_e29_v24?0"NSArray"8"NSError"16l
- ___block_descriptor_40_e8_32s_e74_v32?0"TRIClientFactorPackStreamingParser"8"TRIFBFastFactorLevels"16^B24l
- ___block_descriptor_48_e8_32s40bs_e74_v32?0"TRIClientFactorPackStreamingParser"8"TRIFBFastFactorLevels"16^B24l
- ___block_descriptor_66_e8_32s40s48s56r_e64_{_PASDBTransactionCompletion_=B}16?0"_PASSqlWriteTransaction"8l
- ___block_descriptor_80_e8_32s40s48s56r64r72r_e57_v40?0Q8"TRIClientBMLTArtifact"16"NSDate"24"NSError"32l
- ___block_descriptor_80_e8_32s40s48s56r64r72r_e60_v40?0Q8"TRIClientRolloutArtifact"16"NSDate"24"NSError"32l
- ___block_descriptor_88_e8_32s40s48s56s64s72s_e33_v24?0"TRIExperimentRecord"8^B16l
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88r_e28_v24?0"TRIFactorLevel"8^B16l
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88r_e74_v32?0"TRIClientFactorPackStreamingParser"8"TRIFBFastFactorLevels"16^B24l
- ___namespaceDictionaryForClientSelectedNamespace_block_invoke.467
- __block_literal_global.104
- __block_literal_global.113
- __block_literal_global.115
- __block_literal_global.117
- __block_literal_global.130
- __block_literal_global.134
- __block_literal_global.155
- __block_literal_global.159
- __block_literal_global.201
- __block_literal_global.203
- __block_literal_global.251
- __block_literal_global.255
- __block_literal_global.264
- __block_literal_global.27
- __block_literal_global.278
- __block_literal_global.280
- __block_literal_global.283
- __block_literal_global.287
- __block_literal_global.288
- __block_literal_global.295
- __block_literal_global.31
- __block_literal_global.316
- __block_literal_global.317
- __block_literal_global.319
- __block_literal_global.326
- __block_literal_global.333
- __block_literal_global.335
- __block_literal_global.345
- __block_literal_global.35
- __block_literal_global.352
- __block_literal_global.385
- __block_literal_global.393
- __block_literal_global.397
- __block_literal_global.401
- __block_literal_global.403
- __block_literal_global.418
- __block_literal_global.435
- __block_literal_global.444
- __block_literal_global.457
- __block_literal_global.469
- __block_literal_global.497
- __block_literal_global.498
- __block_literal_global.501
- __block_literal_global.526
- __block_literal_global.529
- __block_literal_global.531
- __block_literal_global.533
- __block_literal_global.536
- __block_literal_global.539
- __block_literal_global.57
- __block_literal_global.598
- __block_literal_global.62
- __block_literal_global.73
- __block_literal_global.88
- __block_literal_global.90
- _objc_msgSend$_overwriteActiveFactorProvidersUsingGlobalPath:withNamespaceMap:rolloutDeploymentMap:experimentDeploymentMap:experimentTreatmentMap:factorPackMap:
- _objc_msgSend$_updateExperimentEndDateWithArtifact:context:database:scheduleDeactivationTask:scheduleDeactivationNow:
- _objc_msgSend$allTrialAssetTypes
- _objc_msgSend$initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:
- _objc_msgSend$initWithFactorPackSetId:treatmentId:taskAttribution:experimentDeployment:
- _objc_msgSend$initWithNotificationChecker:hotfixScheduler:rollbackScheduler:
- _objc_msgSend$siriTrialAssetTypes
- _objc_msgSend$subpathsOfDirectoryAtPath:error:
- _objc_msgSend$taskWithExperiment:treatmentId:factorPackSetId:taskAttributing:requiresTreatmentInstallation:capabilityModifier:startTime:taskOptions:
- _objc_msgSend$taskWithFactorPackSetId:treatmentId:taskAttribution:experimentDeployment:
- descriptor.descriptor.107
- descriptor.descriptor.126
- descriptor.descriptor.133
- descriptor.descriptor.140
- descriptor.descriptor.161
- descriptor.descriptor.171
- descriptor.descriptor.178
- descriptor.descriptor.194
- descriptor.descriptor.207
- descriptor.descriptor.220
- descriptor.descriptor.227
- descriptor.descriptor.240
- descriptor.descriptor.247
- descriptor.descriptor.254
- descriptor.descriptor.260
- descriptor.descriptor.266
- descriptor.descriptor.281
- descriptor.descriptor.290
- descriptor.descriptor.300
- descriptor.descriptor.327
- descriptor.descriptor.339
- descriptor.descriptor.352
- descriptor.descriptor.369
- descriptor.descriptor.376
- descriptor.descriptor.393
- descriptor.descriptor.412
- descriptor.descriptor.425
- descriptor.descriptor.445
- descriptor.fields.108
- descriptor.fields.127
- descriptor.fields.134
- descriptor.fields.141
- descriptor.fields.162
- descriptor.fields.172
- descriptor.fields.179
- descriptor.fields.195
- descriptor.fields.208
- descriptor.fields.221
- descriptor.fields.228
- descriptor.fields.241
- descriptor.fields.248
- descriptor.fields.267
- descriptor.fields.282
- descriptor.fields.291
- descriptor.fields.301
- descriptor.fields.328
- descriptor.fields.340
- descriptor.fields.353
- descriptor.fields.370
- descriptor.fields.377
- descriptor.fields.394
- descriptor.fields.413
- descriptor.fields.426
- descriptor.fields.446
CStrings:
+ "-[TRIDServer _registerXpcStreamEventHandler]_block_invoke"
+ "-[TRIInternalServiceRequestHandler activeBMLTInformationWithPrivacyFilterPolicy:completion:]_block_invoke"
+ "-[TRIInternalServiceRequestHandler activeRolloutInformationWithPrivacyFilterPolicy:completion:]_block_invoke"
+ "-[TRIInternalServiceRequestHandler experimentNotificationsWithExperimentId:cloudKitContainer:teamId:completion:]_block_invoke"
+ "-[TRIInternalServiceRequestHandler lastFetchDateForContainer:teamId:completion:]_block_invoke"
+ "-[TRIInternalServiceRequestHandler logSystemCovariates]_block_invoke"
+ "-[TRIInternalServiceRequestHandler rolloutNotificationWithLatestDeploymentForRolloutId:cloudKitContainer:teamId:completion:]_block_invoke"
+ "-[TRIInternalServiceRequestHandler setLastFetchDate:forContainer:teamId:completion:]_block_invoke"
+ "-[TRIInternalServiceRequestHandler setSubscription:namespaceName:completion:]_block_invoke"
+ "-[TRIInternalServiceRequestHandler subscriptionForNamespaceName:completion:]_block_invoke"
+ "-[TRIXPCNamespaceManagementRequestHandler _setPurgeabilityLevelsForFactors:usingEntitlementWitness:namespace:paths:completion:]_block_invoke"
+ "-[TRIXPCNamespaceManagementRequestHandler loadNamespaceMetadataForNamespaceName:completion:]_block_invoke"
+ "-[TRIXPCNamespaceManagementRequestHandler setPurgeabilityLevelsForFactors:forNamespaceName:completion:]_block_invoke_2"
+ "-[TRIXPCNamespaceManagementRequestHandler startDownloadLevelsForFactors:withNamespace:factorsState:options:completion:]_block_invoke"
+ "-[TRIXPCNamespaceManagementRequestHandler statusOfDownloadForFactors:withNamespace:factorsState:completion:]_block_invoke_2"
+ "/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/Versions/A/BackgroundSystemTasks"
+ "/System/Library/PrivateFrameworks/GenerativeModels.framework/Versions/A/GenerativeModels"
+ "<%@:%@,%d,%ld,r:%d>"
+ "@\"<TRIExperimentUpdateSchedulerProtocol>\""
+ "@\"TRIBGSTManager\""
+ "@40@0:8@16@24B32B36"
+ "@52@0:8@16@24B32@36@44"
+ "@84@0:8@16@24@32@40@48B56@60@68@76"
+ "AppleIntelligence use-case targeting is disabled on triald_system"
+ "AppleIntelligenceState"
+ "B24@?0@\"BMStoreEvent\"8^B16"
+ "B76@0:8B16@20@28@36@44@52@60@68"
+ "BGST %@ was expired, but we failed to request rescheduling: %@"
+ "BGST %@ was expired, requested rescheduling"
+ "BMLT fetch requested but no deployment was provided"
+ "Blob length (%lu) is insufficient for reading persisted AI State"
+ "Clearing Experiment Updates Biome Stream due to D&U opt-out"
+ "Counterfactuals"
+ "Currently running deactivation BGST. Completing and rescheduling it."
+ "Data to be persisted for Apple Intelligence and usage was nil"
+ "Deferral requested before checking to see if biome should be cleared."
+ "Deferral requested before pruning Biome Stream."
+ "Deferral requested before publishing low level factors."
+ "Deferral requested before reporting experiments metric."
+ "Error querying Obsolete Biome Events: %@"
+ "Experiment update notification missing artifact"
+ "Failed to reschedule deactivation BGST with error: %@"
+ "Failed to submit deactivation BGST with error: %@"
+ "Failed to update experiment end date due to missing existing experiment record."
+ "Found Pallas settings for %{public}@: Audience %{public}@, matches new setting: %d"
+ "Found Pallas settings for %{public}@: Pallas URL %{public}@, matches new setting: %d"
+ "Found missing MA ref db entry: %{public}@"
+ "Invalid FPS ID for counterfactuals in TRIActivateTreatmentPersistedTask: %{public}@"
+ "Invalid useCaseId: %@"
+ "Mar  7 2025"
+ "Marking all BGSTs as completed as the task queue has finished"
+ "MobileAssetAssetAudience"
+ "NamespaceUpdates"
+ "Neither protobuf nor flatbuffer were found in a factor pack of FPS with id %@"
+ "New BGST added, need to update task queue capabilities"
+ "No key-value store present for persisted AI State retrieval"
+ "No persisted AI State and usage state found for key: %{public}@"
+ "Not able to log post-launch telemetry for exp_st_AL. Experiment record not found after downloading FPS: %@"
+ "Not scheduling deactivation BGST as there's already a BGST scheduled to run in %lld seconds"
+ "Not scheduling deactivation BGST as there's no scheduled deactivation tasks"
+ "Not scheduling deactivation BGST as there's no scheduled tasks"
+ "PallasUrlOverrideV2"
+ "Processing experiment update for experiment: %{public}@ deployment: %u"
+ "Pruning Obsolete events from biome stream"
+ "Queueing counterfactual FPS fetch (ExperimentId: %@, TreatmentId: %@, FPSId: %@)"
+ "Rescheduling deactivation BGST to run in %lld seconds (previously %lld)"
+ "Running deactivation BGST"
+ "SELECT * FROM \"Trial.Experiment.NamespaceUpdates\" WHERE experimentStatus=2 AND eventTimestamp < '%f'"
+ "Scheduled the deactivation BGST to run in %lld seconds from now."
+ "Setting PallasURL for %{public}@ to %{public}@"
+ "Setting audience setting for %{public}@ to %{public}@"
+ "Skipping post-launch FPS task telemetry for counterfactual treatment: %@ (FPS: %@)"
+ "T@\"<TRIExperimentUpdateSchedulerProtocol>\",R,N,V_experimentUpdateScheduler"
+ "T@\"NSDictionary\",R,N,V_counterfactualTreatments"
+ "T@\"NSMutableDictionary\",&,D,N"
+ "T@\"_PASSqliteDatabase\",R,N"
+ "TRIBGSTManager"
+ "TRIBGSTManager.m"
+ "TRIBGSTManagerGuardedData"
+ "TRIBiomeExperimentUpdateStreamWriter"
+ "TRIBiomeExperimentUpdateStreamWriter.m"
+ "TRIDServer: AI State Change Notification received"
+ "TRIDServer: AI State changed, queueing retargeting"
+ "TRIExperimentUpdateProcessor"
+ "TRIExperimentUpdateScheduler"
+ "TRIExperimentUpdateSchedulerProtocol"
+ "TRIPurgeableExperimentAndRolloutProvider.m"
+ "TrialXP-429.20"
+ "Unable to find subpaths of treatments dir %{public}@"
+ "Unable to rollback because the artifact contains no deployment"
+ "[RADAR SEARCH] Missing FPE layer for an experiment in namespace %@"
+ "[serverContext.paths namespaceDescriptorsDefaultDir]"
+ "_counterfactualTreatments"
+ "_experimentDeployment.experimentId"
+ "_experimentUpdateScheduler"
+ "_getCurrentPallasAudienceForAssetType:"
+ "_getCurrentPallasURLForAssetType:"
+ "_handleExperimentUpdateNotification:"
+ "_isCounterfactualTreatment"
+ "_overwriteActiveFactorProvidersUsingGlobalPath:withNamespaceMap:rolloutDeploymentMap:experimentDeploymentMap:experimentTreatmentMap:treatmentFactorPackSetIdsMap:counterfactualTreatmentsMap:factorPackMap:"
+ "_registerDeactivationBGST"
+ "_scheduleDeactivationBGST:"
+ "_setPallasAudience:forAssetType:"
+ "_setPallasURL:forAssetType:"
+ "_submitDeactivationBGSTRequestAfterSeconds:gracePeriodInSeconds:"
+ "_updateExperimentEndDateWithDeployment:withNewEndDate:scheduleDeactivationTask:scheduleDeactivationNow:"
+ "appleIntelligenceState"
+ "artifact.experiment.endDate.date"
+ "artifact.experimentDeployment.taskTag"
+ "artifact.namespaceNames"
+ "artifact.rollout.rampId"
+ "bgstManager"
+ "clearExperimentUpdatesStream"
+ "com.apple.MobileAsset"
+ "com.apple.gms.availability.notification"
+ "com.apple.triald.deactivation"
+ "com.apple.triald.persisted.AIState"
+ "counterfactualLogging"
+ "counterfactualTreatmentIds"
+ "counterfactualTreatments"
+ "counterfactualTreatments_Count"
+ "counterfactualsTreatmentsToFactorPackSetIds"
+ "counterfactualsTreatmentsToFactorPackSetIdsWithActiveTreatmentId:"
+ "currentWithUseCaseIdentifiers:"
+ "delete-obsolete-events"
+ "deleteObsoleteEventsFromExperimentsUpdateStream"
+ "deleteWithPolicy:eventsPassingTest:"
+ "eliminableAssetTypes"
+ "eventBody"
+ "executeQuery:"
+ "experimentRecord.artifact.experiment.channelId"
+ "experimentUpdateNotification"
+ "experimentUpdateScheduler"
+ "expireBGST:"
+ "factorPack"
+ "factorPack.factorPackId"
+ "factorPack.selectedNamespace"
+ "factorPack.selectedNamespace.name"
+ "fbFactorLevel.namespaceName"
+ "fbFactorPack.namespaceName"
+ "fbFactorPack.sourceAsFactorPackId"
+ "flatbufferFactorLevel.namespaceName"
+ "getBytes:length:"
+ "hasCounterfactualLogging"
+ "hasCounterfactualTreatmentReferencingFactorPackSetId:"
+ "hasIsCounterfactualTreatment"
+ "identifierToTask"
+ "initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:counterfactualTreatmentIds:"
+ "initWithExperimentDatabase:"
+ "initWithFactorPackSetId:treatmentId:isCounterfactualTreatment:taskAttribution:experimentDeployment:"
+ "initWithIdentifier:"
+ "initWithNamespaceName:"
+ "initWithNamespaceNames:experimentStatus:userId:experimentId:deploymentId:treatmentId:"
+ "initWithNotificationChecker:hotfixScheduler:rollbackScheduler:experimentUpdateScheduler:"
+ "initWithServerContext:asyncQueue:"
+ "initWithUseCase:"
+ "invalid type for key: %@ | expecting string"
+ "isCompatibleCounterfactual"
+ "isCounterfactualTreatment"
+ "macOSLaunchDaemonExperimentation"
+ "markAllBGSTsAsCompleted"
+ "markBGSTAsStarted:"
+ "member:"
+ "newEndDate"
+ "next"
+ "opt-out-security-updates"
+ "pbFactorPack.selectedNamespace.name"
+ "persistAIState:"
+ "persistedAIState"
+ "processUpdateOperationForExistingExperimentWithEndDate:withExperimentDeployment:"
+ "protoFactorPack.selectedNamespace.name"
+ "pruner"
+ "reactionForUpdateExperimentDeployment:"
+ "record.experimentDeployment"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "result.backgroundTask"
+ "result.backgroundTask.pluginId"
+ "resumeWithBGST:executeWhenSuspended:"
+ "rolloutRecord.namespaces"
+ "root"
+ "row"
+ "scheduleAfter"
+ "scheduleDeactivationBGSTWithEarliestDeactivationTaskScheduledDate:gracePeriodInSeconds:"
+ "scheduleExperimentUpdateOperationsForExperimentWithNewEndDate:withDeployment:"
+ "selectedNamespace.name"
+ "self.experimentDeployment.experimentId"
+ "sendEvent:"
+ "server context not full initialised before logging system covariates"
+ "serverContext.client.trackingId"
+ "serverContext.namespaceDatabase"
+ "serverContext.paths"
+ "setCounterfactualTreatments:"
+ "setExpirationHandler:"
+ "setIsCounterfactualTreatment:"
+ "setRequiresExternalPower:"
+ "setRequiresNetworkConnectivity:"
+ "setScheduleAfter:"
+ "setTaskCompleted"
+ "setTaskExpiredWithRetryAfter:error:"
+ "setTrySchedulingBefore:"
+ "sharedScheduler"
+ "source"
+ "submitTaskRequest:error:"
+ "taskRequestForIdentifier:"
+ "taskWithExperiment:treatmentId:factorPackSetId:counterfactualTreatments:taskAttributing:requiresTreatmentInstallation:capabilityModifier:startTime:taskOptions:"
+ "taskWithFactorPackSetId:treatmentId:isCounterfactualTreatment:taskAttribution:experimentDeployment:"
+ "treatmentFactorPackSetIds"
+ "tri_checkAIUseCaseEnabled:"
+ "updateTaskRequest:error:"
+ "v16@?0@\"BGSystemTask\"8"
+ "v16@?0@\"TRIBGSTManagerGuardedData\"8"
+ "v32@0:8@\"BGSystemTask\"16@?<v@?>24"
+ "v32@0:8@\"NSDate\"16@\"TRIExperimentDeployment\"24"
+ "v32@0:8@16q24"
+ "v32@0:8q16q24"
+ "v32@?0@\"NSString\"8@\"BGSystemTask\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSString<TRIFactorPackSetId>\"16^B24"
+ "v36@0:8@16B24@28"
+ "writeExperimentUpdateWithRecord:withExperimentStateIsActive:withUserId:"
+ "{?=C}24@0:8@\"TRIExperimentDeployment\"16"
- "@76@0:8@16@24@32@40B48@52@60@68"
- "B60@0:8B16@20@28@36@44@52"
- "Dec 18 2024"
- "Deferral requested before reporting storage telemetry."
- "Did not find any missing MA ref db entries"
- "Failed to update experiment end date due to missing information, ignoring."
- "Found missing MA ref db entries: %{public}@"
- "Setting Siri-specific audience setting for %{public}@ to %{public}@ with Pallas URL %{public}@"
- "Setting audience setting for %{public}@ to %{public}@ with Pallas URL %{public}@"
- "TRIActivateTreatment is instantiated with a factor pack set id when FPE write is disabled."
- "TrialXP-429.0.4.6"
- "Unable to find subpaths of treatments dir %{public}@: %{public}@"
- "_overwriteActiveFactorProvidersUsingGlobalPath:withNamespaceMap:rolloutDeploymentMap:experimentDeploymentMap:experimentTreatmentMap:factorPackMap:"
- "_updateExperimentEndDateWithArtifact:context:database:scheduleDeactivationTask:scheduleDeactivationNow:"
- "allTrialAssetTypes"
- "initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:"
- "initWithFactorPackSetId:treatmentId:taskAttribution:experimentDeployment:"
- "initWithNotificationChecker:hotfixScheduler:rollbackScheduler:"
- "siriTrialAssetTypes"
- "subpathsOfDirectoryAtPath:error:"
- "taskWithExperiment:treatmentId:factorPackSetId:taskAttributing:requiresTreatmentInstallation:capabilityModifier:startTime:taskOptions:"
- "taskWithFactorPackSetId:treatmentId:taskAttribution:experimentDeployment:"

```
