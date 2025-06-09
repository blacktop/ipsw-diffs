## TrialServer

> `/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer`

```diff

-429.20.2.0.0
-  __TEXT.__text: 0x168308
-  __TEXT.__auth_stubs: 0xf30
-  __TEXT.__delay_helper: 0x1d8
-  __TEXT.__objc_methlist: 0xbf84
-  __TEXT.__const: 0xf90
-  __TEXT.__dlopen_cstrs: 0x74
-  __TEXT.__gcc_except_tab: 0xa2ac
-  __TEXT.__cstring: 0x16e4a
-  __TEXT.__oslogstring: 0x1e526
-  __TEXT.__unwind_info: 0x4548
-  __TEXT.__objc_classname: 0x287c
-  __TEXT.__objc_methname: 0x1e550
-  __TEXT.__objc_methtype: 0x5482
-  __TEXT.__objc_stubs: 0x14e40
-  __DATA_CONST.__got: 0x1390
-  __DATA_CONST.__const: 0x6ea0
-  __DATA_CONST.__objc_classlist: 0x940
-  __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x200
+463.0.0.0.0
+  __TEXT.__text: 0x14f67c
+  __TEXT.__auth_stubs: 0xfe0
+  __TEXT.__delay_helper: 0x478
+  __TEXT.__objc_methlist: 0xbd3c
+  __TEXT.__const: 0xe60
+  __TEXT.__dlopen_cstrs: 0x101
+  __TEXT.__cstring: 0x1585e
+  __TEXT.__gcc_except_tab: 0x9aec
+  __TEXT.__oslogstring: 0x1cc54
+  __TEXT.__unwind_info: 0x42e8
+  __TEXT.__objc_classname: 0x2850
+  __TEXT.__objc_methname: 0x1e596
+  __TEXT.__objc_methtype: 0x5630
+  __TEXT.__objc_stubs: 0x152a0
+  __DATA_CONST.__got: 0x1358
+  __DATA_CONST.__const: 0x6a60
+  __DATA_CONST.__objc_classlist: 0x908
+  __DATA_CONST.__objc_catlist: 0x70
+  __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5de0
+  __DATA_CONST.__objc_selrefs: 0x60c0
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x5f8
-  __DATA_CONST.__objc_arraydata: 0x350
-  __AUTH_CONST.__auth_got: 0x7a8
-  __AUTH_CONST.__const: 0x1020
-  __AUTH_CONST.__cfstring: 0xe1a0
-  __AUTH_CONST.__objc_const: 0x173a0
-  __AUTH_CONST.__objc_arrayobj: 0x2e8
+  __DATA_CONST.__objc_superrefs: 0x5e0
+  __DATA_CONST.__objc_arraydata: 0x328
+  __AUTH_CONST.__auth_got: 0x800
+  __AUTH_CONST.__const: 0x11a0
+  __AUTH_CONST.__cfstring: 0xd9e0
+  __AUTH_CONST.__objc_const: 0x16788
   __AUTH_CONST.__objc_intobj: 0x990
+  __AUTH_CONST.__objc_arrayobj: 0x318
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x1748
-  __AUTH.__data: 0x8e8
-  __DATA.__objc_ivar: 0x8a8
-  __DATA.__data: 0x25b8
-  __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x168
-  __DATA_DIRTY.__objc_ivar: 0x22c
-  __DATA_DIRTY.__objc_data: 0x4538
-  __DATA_DIRTY.__common: 0x8
-  __DATA_DIRTY.__bss: 0x2a8
+  __AUTH.__objc_data: 0x1798
+  __AUTH.__data: 0x690
+  __DATA.__objc_ivar: 0x8e8
+  __DATA.__data: 0x2684
+  __DATA.__crash_info: 0x148
+  __DATA.__common: 0x48
+  __DATA.__bss: 0x130
+  __DATA_DIRTY.__objc_ivar: 0x1b8
+  __DATA_DIRTY.__objc_data: 0x42b8
+  __DATA_DIRTY.__common: 0x18
+  __DATA_DIRTY.__bss: 0x380
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
+  - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
+  - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
+  - /System/Library/PrivateFrameworks/ProactiveEventTracker.framework/ProactiveEventTracker
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/TrialProto.framework/TrialProto
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libParallelCompression.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: B36EFF05-4DCC-3355-A0BF-0315324CE14C
-  Functions: 4923
-  Symbols:   17612
-  CStrings:  10692
+  UUID: 7E55ED73-5213-382D-83ED-7C0D456EAA85
+  Functions: 4819
+  Symbols:   17419
+  CStrings:  10618
 
Symbols:
+ +[TRIActiveEnvVarExperiment envVarExperimentWithTargetedBundleIds:factorLevelStrings:]
+ +[TRIActiveEnvVarExperiment supportsSecureCoding]
+ +[TRIActiveEnvVarFactorStringBuilder _levelAsString:]
+ +[TRIActiveEnvVarFactorStringBuilder stringForFactorLevel:]
+ +[TRICKServerEnvironmentReader currentEnvironment]
+ +[TRICKServerEnvironmentReader currentPopulation]
+ +[TRICKServerEnvironmentReader validatedEnvironmentFromNumber:]
+ +[TRICKServerEnvironmentReader validatedPopulationFromNumber:]
+ +[TRICellularParameterManager sharedInstance]
+ +[TRIClientExperimentArtifact(CloudKit) artifactFromCKRecordResult:withContainer:teamId:requireDeploymentId:completion:]
+ +[TRIClientExperimentArtifact(CloudKit) shouldSetForLaunchDaemonFlagFromFields:experiment:error:]
+ +[TRIClientRolloutArtifact artifactWithRollout:populations:deploymentDate:downloadSize:forLaunchDaemon:]
+ +[TRIClientRolloutArtifact(CloudKit) shouldSetForLaunchDaemonFlagFromFields:rollout:error:]
+ +[TRIContentDescriptorUnion unionWithType:experiment:treatment:rollout:factorPackSet:]
+ +[TRIExperimentDatabase(EnvVarNamespacesProviding) _singularAndUniqueNamespaceInRecord:alreadyMapped:]
+ +[TRIExperimentPostLaunchEvent(EventFactory) activatedEventWithExperimentRecord:]
+ +[TRIExperimentPostLaunchEvent(EventFactory) allocationEventWithTriple:isDynamicEnrollment:environment:namespaces:]
+ +[TRIExperimentPostLaunchEvent(EventFactory) fetchedEventWithExperimentRecord:]
+ +[TRIExperimentRecord recordWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isManuallyTargeted:artifact:experimentType:]
+ +[TRIKnownEnvVarFactorsReader _knownFactorsFromPlistURL:]
+ +[TRIKnownEnvVarFactorsReader knownFactorsFromPaths:]
+ +[TRIMapsBucketIdChangeProcessor processMapsBucketIdChangeIfNecessaryForBucketId:withServerContext:withTaskQueue:]
+ +[TRIRolloutRecord recordWithDeployment:rampId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:namespaces:artifact:]
+ +[TRISystemConfiguration _sharedSystemInfo]
+ +[TRISystemConfiguration sharedInstance]
+ +[TRISystemDimensions(Factory) systemDimensions]
+ +[TRISystemInfo _aneVersion]
+ +[TRISystemInfo _appleIntelligenceState]
+ +[TRISystemInfo _carrierBundleIdentifier]
+ +[TRISystemInfo _carrierCountryIsoCode]
+ +[TRISystemInfo _hasAne]
+ +[TRISystemInfo _iCloudIdentifier]
+ +[TRISystemInfo _isAutomatedTestDevice]
+ +[TRISystemInfo _isDiagnosticsAndUsageEnabled]
+ +[TRISystemInfo _isSeedBuild]
+ +[TRISystemInfo _isVirtualMachine]
+ +[TRISystemInfo _mapsBucketId]
+ +[TRISystemInfo _persistentSystemInfoPath]
+ +[TRISystemInfo _sysEnabledInputModeIdentifiers]
+ +[TRISystemInfo _sysIsEnrolledInBetaProgram]
+ +[TRISystemInfo createSystemInfoWithFactorProvider:]
+ +[TRISystemInfo info]
+ +[TRISystemInfo loadSystemInfo]
+ +[TRISystemInfo supportsSecureCoding]
+ +[TRISystemInfo systemInfoFromFile:]
+ +[TRIXPCServices registerAgentToSystemService]
+ +[TRIXPCServices registerTrialServicesWithPromise:]
+ +[TRIXPCServices registerTrialSystemServicesWithPromise:]
+ -[TRIActiveEnvVarExperiment .cxx_destruct]
+ -[TRIActiveEnvVarExperiment copyWithReplacementFactorLevelStrings:]
+ -[TRIActiveEnvVarExperiment copyWithReplacementTargetedBundleIds:]
+ -[TRIActiveEnvVarExperiment copyWithZone:]
+ -[TRIActiveEnvVarExperiment description]
+ -[TRIActiveEnvVarExperiment encodeWithCoder:]
+ -[TRIActiveEnvVarExperiment factorLevelStrings]
+ -[TRIActiveEnvVarExperiment hash]
+ -[TRIActiveEnvVarExperiment initWithCoder:]
+ -[TRIActiveEnvVarExperiment initWithTargetedBundleIds:factorLevelStrings:]
+ -[TRIActiveEnvVarExperiment init]
+ -[TRIActiveEnvVarExperiment isEqual:]
+ -[TRIActiveEnvVarExperiment isEqualToenvVarExperiment:]
+ -[TRIActiveEnvVarExperiment targetedBundleIds]
+ -[TRIActiveEnvVarFactorsPublisher .cxx_destruct]
+ -[TRIActiveEnvVarFactorsPublisher initWithNamespacesProvider:factorRetriever:writer:]
+ -[TRIActiveEnvVarFactorsPublisher initWithServerContext:]
+ -[TRIActiveEnvVarFactorsPublisher publishLowLevelFactors]
+ -[TRIActiveEnvVarFactorsWriter .cxx_destruct]
+ -[TRIActiveEnvVarFactorsWriter _constructPlistForExperiments:]
+ -[TRIActiveEnvVarFactorsWriter initWithPaths:]
+ -[TRIActiveEnvVarFactorsWriter writeExperiments:]
+ -[TRIActiveLaunchdDeliveredExperimentsReader .cxx_destruct]
+ -[TRIActiveLaunchdDeliveredExperimentsReader _factorLevelStringsForNamespace:]
+ -[TRIActiveLaunchdDeliveredExperimentsReader allActiveExperiments]
+ -[TRIActiveLaunchdDeliveredExperimentsReader initWithNamespacesProvider:factorLevelsRetriever:]
+ -[TRIActiveSysctlFactorsProvider .cxx_destruct]
+ -[TRIActiveSysctlFactorsProvider activeSysctlFactorLevels]
+ -[TRIActiveSysctlFactorsProvider initWithActiveNamespacesProvider:factorLevelsRetriever:]
+ -[TRIActiveSysctlFactorsPublisher .cxx_destruct]
+ -[TRIActiveSysctlFactorsPublisher initWithServerContext:]
+ -[TRIActiveSysctlFactorsPublisher initWithSysctlFactorsProvider:sysctlWriter:]
+ -[TRIActiveSysctlFactorsPublisher publishSysctlFactors]
+ -[TRIBiomeDataStreamProvider .cxx_destruct]
+ -[TRIBiomeDataStreamProvider _streamForIdentifier:eventHandler:]
+ -[TRIBiomeDataStreamProvider _subscribeForStreamIdentifier:eventHandler:]
+ -[TRIBiomeDataStreamProvider _unsubscribeAllDataStreams]
+ -[TRIBiomeDataStreamProvider dealloc]
+ -[TRIBiomeDataStreamProvider init]
+ -[TRIBiomeDataStreamProvider readLastDataStreamEventForIdentifier:eventHandler:]
+ -[TRIBiomeDataStreamProvider readLastDataStreamEventForIdentifier:withFilter:eventHandler:]
+ -[TRIBiomeDataStreamProvider setShouldSubscribeWithWaking:]
+ -[TRIBiomeDataStreamProvider subscribeDataStreamForIdentifier:eventHandler:]
+ -[TRIBiomeDataStreamProvider unsubscribeAllDataStreams]
+ -[TRICellularParameterGuardedData .cxx_destruct]
+ -[TRICellularParameterGuardedData description]
+ -[TRICellularParameterManager .cxx_destruct]
+ -[TRICellularParameterManager _dispatchQueueForCarrierInfoGathering]
+ -[TRICellularParameterManager _fetchCarrierBundleIdentifier:]
+ -[TRICellularParameterManager _fetchCarrierCountryIsoCode:]
+ -[TRICellularParameterManager _updateSystemInfo]
+ -[TRICellularParameterManager carrierBundleChange:]
+ -[TRICellularParameterManager carrierBundleIdentifier]
+ -[TRICellularParameterManager carrierCountryIsoCode]
+ -[TRICellularParameterManager init]
+ -[TRICellularParameterManager preferredDataSimChanged:]
+ -[TRICellularParameterManager setCarrierBundleIdentifier:]
+ -[TRICellularParameterManager setCarrierCountryIsoCode:]
+ -[TRICellularParameterManager subscriberCountryCodeDidChange:]
+ -[TRIClient(Logger) logger]
+ -[TRIClientExperimentArtifact forLaunchDaemon]
+ -[TRIClientExperimentArtifact hasValidNamespacesWithError:]
+ -[TRIClientExperimentArtifact requiresTreatmentInstallation]
+ -[TRIClientExperimentArtifact setForLaunchDaemon:]
+ -[TRIClientRolloutArtifact copyWithReplacementForLaunchDaemon:]
+ -[TRIClientRolloutArtifact forLaunchDaemon]
+ -[TRIClientRolloutArtifact initWithRollout:populations:deploymentDate:downloadSize:forLaunchDaemon:]
+ -[TRIClientTreatmentStorage _deleteOnDemandAssetsWithFactorNames:treatment:namespace:inUseAssetDeletionBehavior:]
+ -[TRIClientTreatmentStorage _linkAssetWithId:treatmentId:assetStore:factor:]
+ -[TRIClientTreatmentStorage _saveNamespacePartitionedTreatmentsForTreatment:forNamespaceNames:]
+ -[TRIClientTreatmentStorage updateSavedTreatmentWithTreatmentId:deletingAssetsWithFactorNames:forNamespaceName:]
+ -[TRIClientTreatmentStorage updateSavedTreatmentWithTreatmentId:deletingAssetsWithFactorNames:forNamespaceName:inUseAssetDeletionBehavior:]
+ -[TRIContentDescriptorUnion initWithType:experiment:treatment:rollout:factorPackSet:]
+ -[TRIDServer _handleUserSettingsNotificationWithContext:]
+ -[TRIDatabase migration_dropBMLTDatabasesAndShadowEvaluationRolloutsAndExperiments]
+ -[TRIDatabase migration_dropShadowEvaluationDatabase]
+ -[TRIEagerExitManager .cxx_destruct]
+ -[TRIEagerExitManager dealloc]
+ -[TRIEagerExitManager exitTrialdCleanly]
+ -[TRIEagerExitManager handleTaskQueueEmptyNotificationWithCooldown:]
+ -[TRIEagerExitManager initWithExitCooldown:monitoringTaskQueue:]
+ -[TRIEagerExitManager setTaskQueue:]
+ -[TRIEagerExitManager taskQueue]
+ -[TRIExperimentDatabase enumerateActiveExperimentRecordsWithBlock:]
+ -[TRIExperimentDatabase(EnvVarNamespacesProviding) activeEnvVarNamespaces]
+ -[TRIExperimentDatabase(SysctlNamespacesProviding) activeSysctlNamespaces]
+ -[TRIExperimentHistoryDatabase(PostLaunchLogging) _isValidNextStateForEvent:]
+ -[TRIExperimentHistoryDatabase(PostLaunchLogging) storeExperimentEvent:isValidTransition:]
+ -[TRIExperimentRecord copyWithReplacementExperimentType:]
+ -[TRIExperimentRecord experimentType]
+ -[TRIExperimentRecord initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isManuallyTargeted:artifact:experimentType:]
+ -[TRIExternalParameterGuardedData .cxx_destruct]
+ -[TRIExternalParameterGuardedData description]
+ -[TRIExternalParameterManager .cxx_destruct]
+ -[TRIExternalParameterManager _fetchSiriDeviceAggregationIdRotationDate]
+ -[TRIExternalParameterManager _readParametersFromFile]
+ -[TRIExternalParameterManager _readSiriDeviceAggregationIdRotationDateFromEvent:]
+ -[TRIExternalParameterManager _updateSystemInfo]
+ -[TRIExternalParameterManager _writeParametersToFile]
+ -[TRIExternalParameterManager dictionary]
+ -[TRIExternalParameterManager initWithProvider:paths:]
+ -[TRIExternalParameterManager init]
+ -[TRIExternalParameterManager siriDeviceAggregationIdRotationDate]
+ -[TRIFBClientTreatmentStorage _deleteOnDemandAssetsWithFactorNames:treatment:namespace:]
+ -[TRIFBClientTreatmentStorage _linkAssetWithId:treatmentId:assetStore:factor:]
+ -[TRIFBClientTreatmentStorage _saveNamespacePartitionedTreatmentsForTreatment:forNamespaceNames:]
+ -[TRIFBClientTreatmentStorage updateSavedTreatmentWithTreatmentId:deletingAssetsWithFactorNames:forNamespaceName:]
+ -[TRIFBFactorPackStorage _writeIdBasedFactorPack:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]
+ -[TRIFactorPackStorage _writeFactorPackToLegacyPath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]
+ -[TRIInternalAgentToSystemServiceRequestHandler .cxx_destruct]
+ -[TRIInternalAgentToSystemServiceRequestHandler _getOnDemandReferenceCountsAtGlobalPath:onDemandFactorsPerUser:error:]
+ -[TRIInternalAgentToSystemServiceRequestHandler _updateOnDemandReferenceCountsForUser:atGlobalPath:addingFactors:removingFactors:newlyUnreferencedFactors:]
+ -[TRIInternalAgentToSystemServiceRequestHandler addSymlinkFromAssetWithIdentifier:toPath:flockWitness:completion:]
+ -[TRIInternalAgentToSystemServiceRequestHandler collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:completion:]
+ -[TRIInternalAgentToSystemServiceRequestHandler fixFileProtectionForAssetStoreWithCompletion:]
+ -[TRIInternalAgentToSystemServiceRequestHandler getOnDemandReferenceCountsPerUserAtGlobalPath:completion:]
+ -[TRIInternalAgentToSystemServiceRequestHandler initWithEntitlementWitness:]
+ -[TRIInternalAgentToSystemServiceRequestHandler logSystemCovariates]
+ -[TRIInternalAgentToSystemServiceRequestHandler migrateToGlobalAssetStoreIfNeededFromLocalStore:sourceExtension:completion:]
+ -[TRIInternalAgentToSystemServiceRequestHandler overwriteGlobalActiveFactorProvidersWithNamespaceMap:factorPackMap:rolloutDeploymentMap:completion:]
+ -[TRIInternalAgentToSystemServiceRequestHandler referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:sourceExtension:completion:]
+ -[TRIInternalAgentToSystemServiceRequestHandler removeAssetWithIdentifier:completion:]
+ -[TRIInternalAgentToSystemServiceRequestHandler removeUnreferencedGlobalFactorPacksWithCompletion:]
+ -[TRIInternalAgentToSystemServiceRequestHandler saveAssetWithIdentifier:sourcePath:flockWitness:removeSourceOnFailure:sourceExtension:completion:]
+ -[TRIInternalAgentToSystemServiceRequestHandler saveFactorPackForUserId:toGlobalPath:fromTemporaryPath:factors:sourceExtension:completion:]
+ -[TRIInternalAgentToSystemServiceRequestHandler updateFactorPackForUserId:atGlobalPath:deletingFactors:completion:]
+ -[TRIInternalAgentToSystemServiceRequestHandler updateFactorPackForUserId:atGlobalPath:populatingFactors:completion:]
+ -[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:serverContext:completion:]
+ -[TRIInternalServiceRequestHandler activeExperimentInformationWithEnvironments:completion:]
+ -[TRIInternalServiceRequestHandler activeRolloutInformationWithCompletion:]
+ -[TRIInternalServiceRequestHandler addWithoutRunningForTask:options:completion:]
+ -[TRIInternalServiceRequestHandler isOptedOutOfExperimentationWithCompletion:]
+ -[TRIInternalServiceRequestHandler resumeTaskQueueWithCompletion:]
+ -[TRIInternalServiceRequestHandler treatmentValidForExperimentWithId:treatmentId:completion:]
+ -[TRILogger .cxx_destruct]
+ -[TRILogger _dispatchLogEvent:]
+ -[TRILogger _incrementedLogEventCount]
+ -[TRILogger initWithClient:projectId:]
+ -[TRILogger initWithClient:projectId:logHandlers:]
+ -[TRILogger initWithProjectId:]
+ -[TRILogger initWithProjectId:logHandlers:]
+ -[TRILogger init]
+ -[TRILogger logEvent:]
+ -[TRILogger logHandlers]
+ -[TRILogger logWithMLRuntimeDimensions:metrics:factorState:]
+ -[TRILogger logWithNamespaceName:metrics:dimensions:]
+ -[TRILogger logWithProjectNameAndTrackingId:metrics:dimensions:trialSystemTelemetry:]
+ -[TRILogger logWithTrackingId:logLevel:message:]
+ -[TRILogger logWithTrackingId:logLevel:message:args:]
+ -[TRILogger logWithTrackingId:message:]
+ -[TRILogger logWithTrackingId:metric:]
+ -[TRILogger logWithTrackingId:metric:dimensions:]
+ -[TRILogger logWithTrackingId:metrics:dimensions:]
+ -[TRILogger logWithTrackingId:metrics:dimensions:systemDimensions:trialSystemTelemetry:]
+ -[TRILogger logWithTrackingId:metrics:dimensions:trialSystemTelemetry:]
+ -[TRILogger messageWithOneofField:withName:]
+ -[TRIMaintenanceSubTask .cxx_destruct]
+ -[TRIMaintenanceSubTask block]
+ -[TRIMaintenanceSubTask initWithName:subtaskBlock:]
+ -[TRIMaintenanceSubTask name]
+ -[TRIPETLogHandler logEvent:subgroupName:queue:]
+ -[TRIPersistentUserSettings persistActiveDicationLocales:]
+ -[TRIPersistentUserSettings persistMapsBucketId:]
+ -[TRIPersistentUserSettings persistMapsDeviceCountryCode:]
+ -[TRIPersistentUserSettings persistedActiveDicationLocales]
+ -[TRIPersistentUserSettings persistedMapsBucketId]
+ -[TRIPersistentUserSettings persistedMapsDeviceCountryCode]
+ -[TRIPurgeableExperimentAndRolloutProvider _checkTreatmentBasedExperimentForPurgeables:experimentAssets:experimentHasNamespaceWithEagerFactors:experimentHasPurgeableNamespace:overriddenFactors:record:shouldGenerateAssetPaths:storage:]
+ -[TRIRolloutDatabase enumerateActiveRecordsUsingTransaction:block:]
+ -[TRIRolloutRecord initWithDeployment:rampId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:namespaces:artifact:]
+ -[TRISignatureKey validateBase64Signature:forDigest:]
+ -[TRISysctlFactorLevel .cxx_destruct]
+ -[TRISysctlFactorLevel initWithSysctlName:level:]
+ -[TRISysctlFactorLevel isEqual:]
+ -[TRISysctlFactorLevel level]
+ -[TRISysctlFactorLevel sysctlName]
+ -[TRISysctlWriter writeSysctlWithName:intValue:]
+ -[TRISystemConfiguration .cxx_destruct]
+ -[TRISystemConfiguration _dispatchQueueForCarrierInfoGathering]
+ -[TRISystemConfiguration _systemInfoWithIsStale:]
+ -[TRISystemConfiguration _trialVersion]
+ -[TRISystemConfiguration _updateSystemInfo:]
+ -[TRISystemConfiguration aneVersion]
+ -[TRISystemConfiguration appleIntelligenceState]
+ -[TRISystemConfiguration carrierBundleIdentifier]
+ -[TRISystemConfiguration carrierCountryIsoCode]
+ -[TRISystemConfiguration createDeviceIdentifierWithPath:]
+ -[TRISystemConfiguration createPersistentDeviceIdentifier]
+ -[TRISystemConfiguration deleteDeviceIdentifierWithPath:]
+ -[TRISystemConfiguration deleteDeviceIdentifier]
+ -[TRISystemConfiguration deviceChipId]
+ -[TRISystemConfiguration deviceClass]
+ -[TRISystemConfiguration deviceHardwareModel]
+ -[TRISystemConfiguration deviceId]
+ -[TRISystemConfiguration deviceInfoForQuestion:]
+ -[TRISystemConfiguration deviceModelCode]
+ -[TRISystemConfiguration deviceSystemId]
+ -[TRISystemConfiguration enabledInputModeIdentifiers]
+ -[TRISystemConfiguration hasAne]
+ -[TRISystemConfiguration iCloudId]
+ -[TRISystemConfiguration initWithPaths:]
+ -[TRISystemConfiguration init]
+ -[TRISystemConfiguration isAutomatedTestDevice]
+ -[TRISystemConfiguration isBetaBuild]
+ -[TRISystemConfiguration isBetaUserWithIsStale:]
+ -[TRISystemConfiguration isDiagnosticsAndUsageEnabled]
+ -[TRISystemConfiguration isInternalBuild]
+ -[TRISystemConfiguration mapsBucketId]
+ -[TRISystemConfiguration mapsDeviceCountryCode]
+ -[TRISystemConfiguration marketingOSVersion]
+ -[TRISystemConfiguration osBuild]
+ -[TRISystemConfiguration osType]
+ -[TRISystemConfiguration populationType]
+ -[TRISystemConfiguration readDeviceIdentifierWithPath:]
+ -[TRISystemConfiguration reloadDeviceId]
+ -[TRISystemConfiguration reloadSystemInfo]
+ -[TRISystemConfiguration resetDeviceIdentifier]
+ -[TRISystemConfiguration setDeviceIdentifier:]
+ -[TRISystemConfiguration setDeviceIdentifier:path:]
+ -[TRISystemConfiguration siriDeviceAggregationIdRotationDate]
+ -[TRISystemConfiguration storedDeviceIdentifier]
+ -[TRISystemConfiguration systemInfo]
+ -[TRISystemConfiguration trialVersionMajor]
+ -[TRISystemConfiguration trialVersionMinor]
+ -[TRISystemConfiguration trialVersionTag]
+ -[TRISystemConfiguration userSettingsBCP47DeviceLocale]
+ -[TRISystemConfiguration userSettingsLanguageCode]
+ -[TRISystemConfiguration userSettingsRegionCode]
+ -[TRISystemConfiguration(Server) activeDictationLocales]
+ -[TRISystemCovariates _sharedCovariatesFromConfiguration:]
+ -[TRISystemCovariates _userSpecificCovariatesFromConfiguration:]
+ -[TRISystemInfo .cxx_destruct]
+ -[TRISystemInfo _getSiriDeviceAggregationIdRotationDate]
+ -[TRISystemInfo aneVersion]
+ -[TRISystemInfo appleIntelligenceState]
+ -[TRISystemInfo carrierBundleIdentifier]
+ -[TRISystemInfo carrierCountryIsoCode]
+ -[TRISystemInfo enabledInputModeIdentifiers]
+ -[TRISystemInfo encodeWithCoder:]
+ -[TRISystemInfo externalParamManager]
+ -[TRISystemInfo hasAne]
+ -[TRISystemInfo iCloudIdentifier]
+ -[TRISystemInfo initFromSystemWithFactorProvider:]
+ -[TRISystemInfo initWithCoder:]
+ -[TRISystemInfo isAutomatedTestDevice]
+ -[TRISystemInfo isDiagnosticsAndUsageEnabled]
+ -[TRISystemInfo isEnrolledInBetaProgram]
+ -[TRISystemInfo logUserKeyboardEnabledInputMode]
+ -[TRISystemInfo logUserSettingsLanguageCode]
+ -[TRISystemInfo logUserSettingsRegionCode]
+ -[TRISystemInfo mapsBucketId]
+ -[TRISystemInfo saveToFile:]
+ -[TRISystemInfo save]
+ -[TRISystemInfo setAneVersion:]
+ -[TRISystemInfo setAppleIntelligenceState:]
+ -[TRISystemInfo setCarrierBundleIdentifier:]
+ -[TRISystemInfo setCarrierCountryIsoCode:]
+ -[TRISystemInfo setEnabledInputModeIdentifiers:]
+ -[TRISystemInfo setHasAne:]
+ -[TRISystemInfo setICloudIdentifier:]
+ -[TRISystemInfo setIsAutomatedTestDevice:]
+ -[TRISystemInfo setIsDiagnosticsAndUsageEnabled:]
+ -[TRISystemInfo setIsEnrolledInBetaProgram:]
+ -[TRISystemInfo setLogUserKeyboardEnabledInputMode:]
+ -[TRISystemInfo setLogUserSettingsLanguageCode:]
+ -[TRISystemInfo setLogUserSettingsRegionCode:]
+ -[TRISystemInfo setMapsBucketId:]
+ -[TRISystemInfo setSiriDeviceAggregationIdRotationDate:]
+ -[TRISystemInfo siriDeviceAggregationIdRotationDate]
+ -[TRISystemInfoGuardedData .cxx_destruct]
+ -[TRITargetingTask _isExperimentEligibleWithArtifact:context:]
+ -[TRITaskDatabase taskTypeForTaskWithId:]
+ -[TRITaskQueue addTaskAfterOperationsFinish:]
+ -[TRIUrgentRollbackScheduler _activeExperimentDeploymentsForRollbackExperiment:deploymentIds:]
+ -[TRIUrgentRollbackScheduler _experimentRecord:matchesExperimentId:oneOfDeploymentIds:]
+ -[TRIUrgentRollbackScheduler _ineligibleExperimentDeploymentsForRollbackExperiment:deploymentIds:]
+ -[TRIXPCInternalAgentToSystemServiceListener .cxx_destruct]
+ -[TRIXPCInternalAgentToSystemServiceListener init]
+ -[TRIXPCInternalAgentToSystemServiceListener listener:shouldAcceptNewConnection:]
+ -[TRIXPCInternalAgentToSystemServiceWrapper initWithUnderlyingHandler:]
+ -[TRIXPCInternalServiceClient addWithoutRunningTask:options:error:]
+ -[TRIXPCInternalServiceClient initForTrialdSystem:]
+ -[TRIXPCInternalServiceClient performSyncXPCWithError:block:]
+ -[TRIXPCInternalServiceClient resumeTaskQueueWithError:]
+ -[TRIXPCInternalServiceClient treatmentValidForExperimentWithID:treatmentID:]
+ -[TRIXPCInternalServiceListener initWithServerContextPromise:forSystem:]
+ -[TRIXPCNamespaceManagementServiceListener initWithServerContextPromise:forSystem:]
+ -[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:deploymentEnvironment:completion:]
+ -[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:completion:]
+ -[TRIXPCStatusRequestHandler rolloutAllocationStatusWithCompletion:]
+ -[TRIXPCStatusServiceListener initWithPromise:forSystem:]
+ GCC_except_table49
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table73
+ GCC_except_table89
+ GCC_except_table99
+ OBJC_IVAR_$_TRICellularParameterGuardedData.guardedCarrierBundleIdentifier
+ OBJC_IVAR_$_TRICellularParameterGuardedData.guardedCarrierCountryIsoCode
+ OBJC_IVAR_$_TRIExternalParameterGuardedData.guardedSiriDeviceAggregationIdRotationDate
+ OBJC_IVAR_$_TRISystemInfoGuardedData.isStale
+ OBJC_IVAR_$_TRISystemInfoGuardedData.systemInfo
+ _AAErrorDomain
+ _CoreTelephonyLibrary
+ _CoreTelephonyLibraryCore.frameworkLibrary
+ _MGCopyAnswer
+ _OBJC_CLASS_$_ACAccountStore
+ _OBJC_CLASS_$_BMBiomeScheduler
+ _OBJC_CLASS_$_GEOCountryConfiguration
+ _OBJC_CLASS_$_GEOExperimentConfiguration
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSDateComponents
+ _OBJC_CLASS_$_NSLock
+ _OBJC_CLASS_$_OSASystemConfiguration
+ _OBJC_CLASS_$_PETEventTracker2
+ _OBJC_CLASS_$_TRIActiveEnvVarExperiment
+ _OBJC_CLASS_$_TRIActiveEnvVarFactorStringBuilder
+ _OBJC_CLASS_$_TRIActiveEnvVarFactorsPublisher
+ _OBJC_CLASS_$_TRIActiveEnvVarFactorsWriter
+ _OBJC_CLASS_$_TRIActiveLaunchdDeliveredExperimentsReader
+ _OBJC_CLASS_$_TRIActiveSysctlFactorsProvider
+ _OBJC_CLASS_$_TRIActiveSysctlFactorsPublisher
+ _OBJC_CLASS_$_TRIBiomeDataStreamProvider
+ _OBJC_CLASS_$_TRICellularParameterGuardedData
+ _OBJC_CLASS_$_TRICellularParameterManager
+ _OBJC_CLASS_$_TRIEagerExitManager
+ _OBJC_CLASS_$_TRIExternalParameterGuardedData
+ _OBJC_CLASS_$_TRIExternalParameterManager
+ _OBJC_CLASS_$_TRIInternalAgentToSystemServiceRequestHandler
+ _OBJC_CLASS_$_TRIKnownEnvVarFactorsReader
+ _OBJC_CLASS_$_TRILogContext
+ _OBJC_CLASS_$_TRILogEvent
+ _OBJC_CLASS_$_TRILogTime
+ _OBJC_CLASS_$_TRIMaintenanceSubTask
+ _OBJC_CLASS_$_TRIMapsBucketIdChangeProcessor
+ _OBJC_CLASS_$_TRIPETLogHandler
+ _OBJC_CLASS_$_TRIProject
+ _OBJC_CLASS_$_TRISysctlFactorLevel
+ _OBJC_CLASS_$_TRISysctlWriter
+ _OBJC_CLASS_$_TRISystemInfoGuardedData
+ _OBJC_CLASS_$_TRIXPCInternalAgentToSystemServiceListener
+ _OBJC_CLASS_$_TRIXPCInternalAgentToSystemServiceWrapper
+ _OBJC_IVAR_$_TRIActiveEnvVarExperiment._factorLevelStrings
+ _OBJC_IVAR_$_TRIActiveEnvVarExperiment._targetedBundleIds
+ _OBJC_IVAR_$_TRIActiveEnvVarFactorsPublisher._namespacesProvider
+ _OBJC_IVAR_$_TRIActiveEnvVarFactorsPublisher._retriever
+ _OBJC_IVAR_$_TRIActiveEnvVarFactorsPublisher._writer
+ _OBJC_IVAR_$_TRIActiveEnvVarFactorsWriter._paths
+ _OBJC_IVAR_$_TRIActiveLaunchdDeliveredExperimentsReader._factorLevelsRetriever
+ _OBJC_IVAR_$_TRIActiveLaunchdDeliveredExperimentsReader._namespacesProvider
+ _OBJC_IVAR_$_TRIActiveSysctlFactorsProvider._factorLevelsRetriever
+ _OBJC_IVAR_$_TRIActiveSysctlFactorsProvider._namespacesProvider
+ _OBJC_IVAR_$_TRIActiveSysctlFactorsPublisher._factorsProvider
+ _OBJC_IVAR_$_TRIActiveSysctlFactorsPublisher._sysctlWriter
+ _OBJC_IVAR_$_TRIBiomeDataStreamProvider._providerQueue
+ _OBJC_IVAR_$_TRIBiomeDataStreamProvider._shouldSubscribeWithWaking
+ _OBJC_IVAR_$_TRIBiomeDataStreamProvider._streamIdentifierstoSubscribedSinks
+ _OBJC_IVAR_$_TRICellularParameterManager._carrierBundleIdentifier
+ _OBJC_IVAR_$_TRICellularParameterManager._carrierCountryIsoCode
+ _OBJC_IVAR_$_TRICellularParameterManager._lock
+ _OBJC_IVAR_$_TRICellularParameterManager._subscriptionContext
+ _OBJC_IVAR_$_TRICellularParameterManager._telephonyClient
+ _OBJC_IVAR_$_TRIClientExperimentArtifact._forLaunchDaemon
+ _OBJC_IVAR_$_TRIClientRolloutArtifact._forLaunchDaemon
+ _OBJC_IVAR_$_TRIDServer._eagerExitManager
+ _OBJC_IVAR_$_TRIEagerExitManager._eagerExitQueue
+ _OBJC_IVAR_$_TRIEagerExitManager._eagerExitSource
+ _OBJC_IVAR_$_TRIEagerExitManager._taskQueue
+ _OBJC_IVAR_$_TRIEagerExitManager._token
+ _OBJC_IVAR_$_TRIExperimentRecord._experimentType
+ _OBJC_IVAR_$_TRIExternalParameterManager._dispatchQueue
+ _OBJC_IVAR_$_TRIExternalParameterManager._lock
+ _OBJC_IVAR_$_TRIExternalParameterManager._paramProvider
+ _OBJC_IVAR_$_TRIExternalParameterManager._plistPath
+ _OBJC_IVAR_$_TRIInternalAgentToSystemServiceRequestHandler._entitlementWitness
+ _OBJC_IVAR_$_TRIInternalAgentToSystemServiceRequestHandler._operator
+ _OBJC_IVAR_$_TRIInternalAgentToSystemServiceRequestHandler._storageManagement
+ _OBJC_IVAR_$_TRIInternalAgentToSystemServiceRequestHandler._store
+ _OBJC_IVAR_$_TRILogger._client
+ _OBJC_IVAR_$_TRILogger._logHandlers
+ _OBJC_IVAR_$_TRILogger._loggingQueue
+ _OBJC_IVAR_$_TRILogger._projectId
+ _OBJC_IVAR_$_TRIMaintenanceSubTask._block
+ _OBJC_IVAR_$_TRIMaintenanceSubTask._name
+ _OBJC_IVAR_$_TRIPostUpgradeCleanupTask._invalidExperimentDeployments
+ _OBJC_IVAR_$_TRISysctlFactorLevel._level
+ _OBJC_IVAR_$_TRISysctlFactorLevel._sysctlName
+ _OBJC_IVAR_$_TRISystemConfiguration._cachedDeviceIdentifier
+ _OBJC_IVAR_$_TRISystemConfiguration._persistentDeviceIdentifierPath
+ _OBJC_IVAR_$_TRISystemInfo._aneVersion
+ _OBJC_IVAR_$_TRISystemInfo._appleIntelligenceState
+ _OBJC_IVAR_$_TRISystemInfo._carrierBundleIdentifier
+ _OBJC_IVAR_$_TRISystemInfo._carrierCountryIsoCode
+ _OBJC_IVAR_$_TRISystemInfo._enabledInputModeIdentifiers
+ _OBJC_IVAR_$_TRISystemInfo._hasAne
+ _OBJC_IVAR_$_TRISystemInfo._iCloudIdentifier
+ _OBJC_IVAR_$_TRISystemInfo._isAutomatedTestDevice
+ _OBJC_IVAR_$_TRISystemInfo._isDiagnosticsAndUsageEnabled
+ _OBJC_IVAR_$_TRISystemInfo._isEnrolledInBetaProgram
+ _OBJC_IVAR_$_TRISystemInfo._logUserKeyboardEnabledInputMode
+ _OBJC_IVAR_$_TRISystemInfo._logUserSettingsLanguageCode
+ _OBJC_IVAR_$_TRISystemInfo._logUserSettingsRegionCode
+ _OBJC_IVAR_$_TRISystemInfo._mapsBucketId
+ _OBJC_IVAR_$_TRISystemInfo._siriDeviceAggregationIdRotationDate
+ _OBJC_IVAR_$_TRIXPCInternalAgentToSystemServiceListener._interface
+ _OBJC_IVAR_$_TRIXPCInternalAgentToSystemServiceListener._wrapper
+ _OBJC_IVAR_$_TRIXPCInternalServiceClient._trialdSystemOnly
+ _OBJC_IVAR_$_TRIXPCInternalServiceListener._serviceName
+ _OBJC_IVAR_$_TRIXPCNamespaceManagementServiceListener._serviceName
+ _OBJC_IVAR_$_TRIXPCStatusServiceListener._serviceName
+ _OBJC_METACLASS_$_TRIActiveEnvVarExperiment
+ _OBJC_METACLASS_$_TRIActiveEnvVarFactorStringBuilder
+ _OBJC_METACLASS_$_TRIActiveEnvVarFactorsPublisher
+ _OBJC_METACLASS_$_TRIActiveEnvVarFactorsWriter
+ _OBJC_METACLASS_$_TRIActiveLaunchdDeliveredExperimentsReader
+ _OBJC_METACLASS_$_TRIActiveSysctlFactorsProvider
+ _OBJC_METACLASS_$_TRIActiveSysctlFactorsPublisher
+ _OBJC_METACLASS_$_TRIBiomeDataStreamProvider
+ _OBJC_METACLASS_$_TRICKServerEnvironmentReader
+ _OBJC_METACLASS_$_TRICellularParameterGuardedData
+ _OBJC_METACLASS_$_TRICellularParameterManager
+ _OBJC_METACLASS_$_TRIEagerExitManager
+ _OBJC_METACLASS_$_TRIExternalParameterGuardedData
+ _OBJC_METACLASS_$_TRIExternalParameterManager
+ _OBJC_METACLASS_$_TRIInternalAgentToSystemServiceRequestHandler
+ _OBJC_METACLASS_$_TRIKnownEnvVarFactorsReader
+ _OBJC_METACLASS_$_TRILogger
+ _OBJC_METACLASS_$_TRIMaintenanceSubTask
+ _OBJC_METACLASS_$_TRIMapsBucketIdChangeProcessor
+ _OBJC_METACLASS_$_TRIPETLogHandler
+ _OBJC_METACLASS_$_TRISysctlFactorLevel
+ _OBJC_METACLASS_$_TRISysctlWriter
+ _OBJC_METACLASS_$_TRISystemConfiguration
+ _OBJC_METACLASS_$_TRISystemInfo
+ _OBJC_METACLASS_$_TRISystemInfoGuardedData
+ _OBJC_METACLASS_$_TRIXPCInternalAgentToSystemServiceListener
+ _OBJC_METACLASS_$_TRIXPCInternalAgentToSystemServiceWrapper
+ _TRICloudKitRecordExperimentNotification_ForLaunchDaemon
+ _TRICloudKitRecordRolloutNotification_ForLaunchDaemon
+ _TRILogCategory_Archiving.log
+ _TRILogCategory_Archiving.onceToken
+ _TRILogCategory_Backtrace.log
+ _TRILogCategory_Backtrace.onceToken
+ _TRILogCategory_ClientFramework.log
+ _TRILogCategory_ClientFramework.onceToken
+ _TRILogCategory_Server.log
+ _TRILogCategory_Server.onceToken
+ _TRILogCategory_XCTest.log
+ _TRILogCategory_XCTest.onceToken
+ _TRIPersistentActiveDictationLocales
+ _TRIPersistentMapsBucket
+ _TRIPersistentMapsDeviceCountryCode
+ _TRIPopulationOverrideKey
+ _TRISysdiagnoseKey_ActiveFactorPackSetId
+ _TRISysdiagnoseKey_AssetReference
+ _TRISysdiagnoseKey_Compatibility
+ _TRISysdiagnoseKey_CounterfactualTreatments
+ _TRISysdiagnoseKey_DeploymentId
+ _TRISysdiagnoseKey_Experiment
+ _TRISysdiagnoseKey_FactorPackId
+ _TRISysdiagnoseKey_Factors
+ _TRISysdiagnoseKey_LevelValue
+ _TRISysdiagnoseKey_Metadata
+ _TRISysdiagnoseKey_Name
+ _TRISysdiagnoseKey_Namespaces
+ _TRISysdiagnoseKey_Ncvs
+ _TRISysdiagnoseKey_Path
+ _TRISysdiagnoseKey_RampId
+ _TRISysdiagnoseKey_RolloutId
+ _TRISysdiagnoseKey_Size
+ _TRISysdiagnoseKey_Status
+ _TRISysdiagnoseKey_TargetedFactorPackSetId
+ _TRISysdiagnoseKey_TreatmentId
+ _TRISysdiagnoseKey_Type
+ __OBJC_$_CATEGORY_TRIClient_$_Logger
+ __OBJC_$_CLASS_METHODS_TRIActiveEnvVarExperiment
+ __OBJC_$_CLASS_METHODS_TRIActiveEnvVarFactorStringBuilder
+ __OBJC_$_CLASS_METHODS_TRICKServerEnvironmentReader
+ __OBJC_$_CLASS_METHODS_TRICellularParameterManager
+ __OBJC_$_CLASS_METHODS_TRIClientExperimentArtifact(Counterfactuals|FactorPacks|CloudKit)
+ __OBJC_$_CLASS_METHODS_TRIClientRolloutArtifact(Utils|CloudKit)
+ __OBJC_$_CLASS_METHODS_TRIExperimentDatabase(CountProviding|SysctlNamespacesProviding|EnvVarNamespacesProviding)
+ __OBJC_$_CLASS_METHODS_TRIKnownEnvVarFactorsReader
+ __OBJC_$_CLASS_METHODS_TRIMapsBucketIdChangeProcessor
+ __OBJC_$_CLASS_METHODS_TRISystemConfiguration(Server)
+ __OBJC_$_CLASS_METHODS_TRISystemDimensions(ServerFactory|Factory)
+ __OBJC_$_CLASS_METHODS_TRISystemInfo
+ __OBJC_$_CLASS_METHODS_TRITaskAttributionInternalInsecure(Persistance|FirstParty)
+ __OBJC_$_CLASS_PROP_LIST_TRIActiveEnvVarExperiment
+ __OBJC_$_CLASS_PROP_LIST_TRISystemInfo
+ __OBJC_$_INSTANCE_METHODS_NSDictionary(TRI|TRIDAG|TRIFunctions|TRICloudKit)
+ __OBJC_$_INSTANCE_METHODS_TRIActiveEnvVarExperiment
+ __OBJC_$_INSTANCE_METHODS_TRIActiveEnvVarFactorsPublisher
+ __OBJC_$_INSTANCE_METHODS_TRIActiveEnvVarFactorsWriter
+ __OBJC_$_INSTANCE_METHODS_TRIActiveLaunchdDeliveredExperimentsReader
+ __OBJC_$_INSTANCE_METHODS_TRIActiveSysctlFactorsProvider
+ __OBJC_$_INSTANCE_METHODS_TRIActiveSysctlFactorsPublisher
+ __OBJC_$_INSTANCE_METHODS_TRIBiomeDataStreamProvider
+ __OBJC_$_INSTANCE_METHODS_TRICellularParameterGuardedData
+ __OBJC_$_INSTANCE_METHODS_TRICellularParameterManager
+ __OBJC_$_INSTANCE_METHODS_TRIClient(Logger|Telemetry)
+ __OBJC_$_INSTANCE_METHODS_TRIClientExperimentArtifact(Counterfactuals|FactorPacks|CloudKit)
+ __OBJC_$_INSTANCE_METHODS_TRIClientRolloutArtifact(Utils|CloudKit)
+ __OBJC_$_INSTANCE_METHODS_TRIEagerExitManager
+ __OBJC_$_INSTANCE_METHODS_TRIExperimentDatabase(CountProviding|SysctlNamespacesProviding|EnvVarNamespacesProviding)
+ __OBJC_$_INSTANCE_METHODS_TRIExperimentHistoryDatabase(PostLaunchLogging|PreviousStateProviding)
+ __OBJC_$_INSTANCE_METHODS_TRIExperimentRecord(Utils|VersionedNamespaces|Counterfactuals)
+ __OBJC_$_INSTANCE_METHODS_TRIExternalParameterGuardedData
+ __OBJC_$_INSTANCE_METHODS_TRIExternalParameterManager
+ __OBJC_$_INSTANCE_METHODS_TRIInternalAgentToSystemServiceRequestHandler
+ __OBJC_$_INSTANCE_METHODS_TRILogger
+ __OBJC_$_INSTANCE_METHODS_TRIMaintenanceSubTask
+ __OBJC_$_INSTANCE_METHODS_TRIPETLogHandler
+ __OBJC_$_INSTANCE_METHODS_TRISysctlFactorLevel
+ __OBJC_$_INSTANCE_METHODS_TRISysctlWriter
+ __OBJC_$_INSTANCE_METHODS_TRISystemConfiguration(Server)
+ __OBJC_$_INSTANCE_METHODS_TRISystemInfo
+ __OBJC_$_INSTANCE_METHODS_TRISystemInfoGuardedData
+ __OBJC_$_INSTANCE_METHODS_TRITaskAttributionInternalInsecure(Persistance|FirstParty)
+ __OBJC_$_INSTANCE_METHODS_TRIXPCInternalAgentToSystemServiceListener
+ __OBJC_$_INSTANCE_METHODS_TRIXPCInternalAgentToSystemServiceWrapper
+ __OBJC_$_INSTANCE_VARIABLES_TRIActiveEnvVarExperiment
+ __OBJC_$_INSTANCE_VARIABLES_TRIActiveEnvVarFactorsPublisher
+ __OBJC_$_INSTANCE_VARIABLES_TRIActiveEnvVarFactorsWriter
+ __OBJC_$_INSTANCE_VARIABLES_TRIActiveLaunchdDeliveredExperimentsReader
+ __OBJC_$_INSTANCE_VARIABLES_TRIActiveSysctlFactorsProvider
+ __OBJC_$_INSTANCE_VARIABLES_TRIActiveSysctlFactorsPublisher
+ __OBJC_$_INSTANCE_VARIABLES_TRIBiomeDataStreamProvider
+ __OBJC_$_INSTANCE_VARIABLES_TRICellularParameterGuardedData
+ __OBJC_$_INSTANCE_VARIABLES_TRICellularParameterManager
+ __OBJC_$_INSTANCE_VARIABLES_TRIEagerExitManager
+ __OBJC_$_INSTANCE_VARIABLES_TRIExternalParameterGuardedData
+ __OBJC_$_INSTANCE_VARIABLES_TRIExternalParameterManager
+ __OBJC_$_INSTANCE_VARIABLES_TRIInternalAgentToSystemServiceRequestHandler
+ __OBJC_$_INSTANCE_VARIABLES_TRILogger
+ __OBJC_$_INSTANCE_VARIABLES_TRIMaintenanceSubTask
+ __OBJC_$_INSTANCE_VARIABLES_TRISysctlFactorLevel
+ __OBJC_$_INSTANCE_VARIABLES_TRISystemConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_TRISystemInfo
+ __OBJC_$_INSTANCE_VARIABLES_TRISystemInfoGuardedData
+ __OBJC_$_INSTANCE_VARIABLES_TRIXPCInternalAgentToSystemServiceListener
+ __OBJC_$_PROP_LIST_TRIActiveEnvVarExperiment
+ __OBJC_$_PROP_LIST_TRICellularParameterManager
+ __OBJC_$_PROP_LIST_TRIEagerExitManager
+ __OBJC_$_PROP_LIST_TRIExternalParameterManager
+ __OBJC_$_PROP_LIST_TRILogger
+ __OBJC_$_PROP_LIST_TRIMaintenanceSubTask
+ __OBJC_$_PROP_LIST_TRIPETLogHandler
+ __OBJC_$_PROP_LIST_TRISysctlFactorLevel
+ __OBJC_$_PROP_LIST_TRISysctlWriter
+ __OBJC_$_PROP_LIST_TRISystemInfo
+ __OBJC_$_PROP_LIST_TRIXPCInternalAgentToSystemServiceListener
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CoreTelephonyClientCarrierBundleDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CoreTelephonyClientDataDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CoreTelephonyClientSubscriberDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TRIActiveEnvVarNamespacesProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TRIActiveSysctlFactorsProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TRIActiveSysctlNamespacesProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TRIExternalParameterProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TRISysctlWriting
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TRIXPCInternalAgentToSystemServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreTelephonyClientCarrierBundleDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreTelephonyClientDataDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreTelephonyClientSubscriberDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TRIActiveEnvVarNamespacesProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TRIActiveSysctlFactorsProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TRIActiveSysctlNamespacesProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TRIExternalParameterProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TRISysctlWriting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TRIXPCInternalAgentToSystemServiceProtocol
+ __OBJC_$_PROTOCOL_REFS_CoreTelephonyClientCarrierBundleDelegate
+ __OBJC_$_PROTOCOL_REFS_CoreTelephonyClientDataDelegate
+ __OBJC_$_PROTOCOL_REFS_CoreTelephonyClientSubscriberDelegate
+ __OBJC_$_PROTOCOL_REFS_TRIActiveEnvVarNamespacesProviding
+ __OBJC_$_PROTOCOL_REFS_TRIActiveSysctlNamespacesProviding
+ __OBJC_$_PROTOCOL_REFS_TRISysctlWriting
+ __OBJC_CLASS_PROTOCOLS_$_TRIActiveEnvVarExperiment
+ __OBJC_CLASS_PROTOCOLS_$_TRIActiveSysctlFactorsProvider
+ __OBJC_CLASS_PROTOCOLS_$_TRIBiomeDataStreamProvider
+ __OBJC_CLASS_PROTOCOLS_$_TRICellularParameterManager
+ __OBJC_CLASS_PROTOCOLS_$_TRIExperimentDatabase(CountProviding|SysctlNamespacesProviding|EnvVarNamespacesProviding)
+ __OBJC_CLASS_PROTOCOLS_$_TRIExperimentHistoryDatabase(PostLaunchLogging|PreviousStateProviding)
+ __OBJC_CLASS_PROTOCOLS_$_TRIInternalAgentToSystemServiceRequestHandler
+ __OBJC_CLASS_PROTOCOLS_$_TRIPETLogHandler
+ __OBJC_CLASS_PROTOCOLS_$_TRISysctlWriter
+ __OBJC_CLASS_PROTOCOLS_$_TRISystemInfo
+ __OBJC_CLASS_PROTOCOLS_$_TRITaskAttributionInternalInsecure(Persistance|FirstParty)
+ __OBJC_CLASS_PROTOCOLS_$_TRIXPCInternalAgentToSystemServiceListener
+ __OBJC_CLASS_PROTOCOLS_$_TRIXPCInternalAgentToSystemServiceWrapper
+ __OBJC_CLASS_RO_$_TRIActiveEnvVarExperiment
+ __OBJC_CLASS_RO_$_TRIActiveEnvVarFactorStringBuilder
+ __OBJC_CLASS_RO_$_TRIActiveEnvVarFactorsPublisher
+ __OBJC_CLASS_RO_$_TRIActiveEnvVarFactorsWriter
+ __OBJC_CLASS_RO_$_TRIActiveLaunchdDeliveredExperimentsReader
+ __OBJC_CLASS_RO_$_TRIActiveSysctlFactorsProvider
+ __OBJC_CLASS_RO_$_TRIActiveSysctlFactorsPublisher
+ __OBJC_CLASS_RO_$_TRIBiomeDataStreamProvider
+ __OBJC_CLASS_RO_$_TRICKServerEnvironmentReader
+ __OBJC_CLASS_RO_$_TRICellularParameterGuardedData
+ __OBJC_CLASS_RO_$_TRICellularParameterManager
+ __OBJC_CLASS_RO_$_TRIEagerExitManager
+ __OBJC_CLASS_RO_$_TRIExternalParameterGuardedData
+ __OBJC_CLASS_RO_$_TRIExternalParameterManager
+ __OBJC_CLASS_RO_$_TRIInternalAgentToSystemServiceRequestHandler
+ __OBJC_CLASS_RO_$_TRIKnownEnvVarFactorsReader
+ __OBJC_CLASS_RO_$_TRILogger
+ __OBJC_CLASS_RO_$_TRIMaintenanceSubTask
+ __OBJC_CLASS_RO_$_TRIMapsBucketIdChangeProcessor
+ __OBJC_CLASS_RO_$_TRIPETLogHandler
+ __OBJC_CLASS_RO_$_TRISysctlFactorLevel
+ __OBJC_CLASS_RO_$_TRISysctlWriter
+ __OBJC_CLASS_RO_$_TRISystemConfiguration
+ __OBJC_CLASS_RO_$_TRISystemInfo
+ __OBJC_CLASS_RO_$_TRISystemInfoGuardedData
+ __OBJC_CLASS_RO_$_TRIXPCInternalAgentToSystemServiceListener
+ __OBJC_CLASS_RO_$_TRIXPCInternalAgentToSystemServiceWrapper
+ __OBJC_LABEL_PROTOCOL_$_CoreTelephonyClientCarrierBundleDelegate
+ __OBJC_LABEL_PROTOCOL_$_CoreTelephonyClientDataDelegate
+ __OBJC_LABEL_PROTOCOL_$_CoreTelephonyClientSubscriberDelegate
+ __OBJC_LABEL_PROTOCOL_$_TRIActiveEnvVarNamespacesProviding
+ __OBJC_LABEL_PROTOCOL_$_TRIActiveSysctlFactorsProviding
+ __OBJC_LABEL_PROTOCOL_$_TRIActiveSysctlNamespacesProviding
+ __OBJC_LABEL_PROTOCOL_$_TRIExternalParameterProviding
+ __OBJC_LABEL_PROTOCOL_$_TRISysctlWriting
+ __OBJC_LABEL_PROTOCOL_$_TRIXPCInternalAgentToSystemServiceProtocol
+ __OBJC_METACLASS_RO_$_TRIActiveEnvVarExperiment
+ __OBJC_METACLASS_RO_$_TRIActiveEnvVarFactorStringBuilder
+ __OBJC_METACLASS_RO_$_TRIActiveEnvVarFactorsPublisher
+ __OBJC_METACLASS_RO_$_TRIActiveEnvVarFactorsWriter
+ __OBJC_METACLASS_RO_$_TRIActiveLaunchdDeliveredExperimentsReader
+ __OBJC_METACLASS_RO_$_TRIActiveSysctlFactorsProvider
+ __OBJC_METACLASS_RO_$_TRIActiveSysctlFactorsPublisher
+ __OBJC_METACLASS_RO_$_TRIBiomeDataStreamProvider
+ __OBJC_METACLASS_RO_$_TRICKServerEnvironmentReader
+ __OBJC_METACLASS_RO_$_TRICellularParameterGuardedData
+ __OBJC_METACLASS_RO_$_TRICellularParameterManager
+ __OBJC_METACLASS_RO_$_TRIEagerExitManager
+ __OBJC_METACLASS_RO_$_TRIExternalParameterGuardedData
+ __OBJC_METACLASS_RO_$_TRIExternalParameterManager
+ __OBJC_METACLASS_RO_$_TRIInternalAgentToSystemServiceRequestHandler
+ __OBJC_METACLASS_RO_$_TRIKnownEnvVarFactorsReader
+ __OBJC_METACLASS_RO_$_TRILogger
+ __OBJC_METACLASS_RO_$_TRIMaintenanceSubTask
+ __OBJC_METACLASS_RO_$_TRIMapsBucketIdChangeProcessor
+ __OBJC_METACLASS_RO_$_TRIPETLogHandler
+ __OBJC_METACLASS_RO_$_TRISysctlFactorLevel
+ __OBJC_METACLASS_RO_$_TRISysctlWriter
+ __OBJC_METACLASS_RO_$_TRISystemConfiguration
+ __OBJC_METACLASS_RO_$_TRISystemInfo
+ __OBJC_METACLASS_RO_$_TRISystemInfoGuardedData
+ __OBJC_METACLASS_RO_$_TRIXPCInternalAgentToSystemServiceListener
+ __OBJC_METACLASS_RO_$_TRIXPCInternalAgentToSystemServiceWrapper
+ __OBJC_PROTOCOL_$_CoreTelephonyClientCarrierBundleDelegate
+ __OBJC_PROTOCOL_$_CoreTelephonyClientDataDelegate
+ __OBJC_PROTOCOL_$_CoreTelephonyClientSubscriberDelegate
+ __OBJC_PROTOCOL_$_TRIActiveEnvVarNamespacesProviding
+ __OBJC_PROTOCOL_$_TRIActiveSysctlFactorsProviding
+ __OBJC_PROTOCOL_$_TRIActiveSysctlNamespacesProviding
+ __OBJC_PROTOCOL_$_TRIExternalParameterProviding
+ __OBJC_PROTOCOL_$_TRISysctlWriting
+ __OBJC_PROTOCOL_$_TRIXPCInternalAgentToSystemServiceProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_TRIXPCInternalAgentToSystemServiceProtocol
+ ___101-[TRIFactorPackSetStorage enumerateCompatibleFactorPacksForFactorPackSet:usingLegacyPaths:withBlock:]_block_invoke.147
+ ___101-[TRIFactorPackSetStorage enumerateCompatibleFactorPacksForFactorPackSet:usingLegacyPaths:withBlock:]_block_invoke.152
+ ___101-[TRIXPCNamespaceManagementRequestHandler getSandboxExtensionTokensForIdentifierQueryWithCompletion:]_block_invoke.255
+ ___102-[TRICKNativeArtifactProvider _fetchRolloutNotificationWithRolloutId:deploymentId:options:completion:]_block_invoke.239
+ ___103-[TRIActivateTreatmentBaseTask _experimentRecord:hasConflictWithExperimentsInDatabase:conflictEndTime:]_block_invoke.39
+ ___103-[TRIActivateTreatmentBaseTask _experimentRecord:hasConflictWithExperimentsInDatabase:conflictEndTime:]_block_invoke.40
+ ___103-[TRIXPCNamespaceManagementRequestHandler setPurgeabilityLevelsForFactors:forNamespaceName:completion:]_block_invoke.221
+ ___104+[TRIClientFactorPackUtils _enumerateAssetFactorLevelsInFlatBufferStorage:trialAssetBlock:maAssetBlock:]_block_invoke.315
+ ___106-[TRIInternalAgentToSystemServiceRequestHandler getOnDemandReferenceCountsPerUserAtGlobalPath:completion:]_block_invoke
+ ___106-[TRIInternalAgentToSystemServiceRequestHandler getOnDemandReferenceCountsPerUserAtGlobalPath:completion:]_block_invoke.70
+ ___106-[TRIInternalAgentToSystemServiceRequestHandler getOnDemandReferenceCountsPerUserAtGlobalPath:completion:]_block_invoke.77
+ ___106-[TRIInternalAgentToSystemServiceRequestHandler getOnDemandReferenceCountsPerUserAtGlobalPath:completion:]_block_invoke_2
+ ___106-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:serverContext:completion:]_block_invoke
+ ___106-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:serverContext:completion:]_block_invoke.187
+ ___106-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:serverContext:completion:]_block_invoke.202
+ ___106-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:serverContext:completion:]_block_invoke_2
+ ___108-[TRICKNativeArtifactProvider fetchAssetsWithIndexes:fromTreatmentWithRecordId:options:progress:completion:]_block_invoke_2.232
+ ___108-[TRIXPCNamespaceManagementRequestHandler rejectFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke.237
+ ___108-[TRIXPCNamespaceManagementRequestHandler rejectFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke.241
+ ___108-[TRIXPCNamespaceManagementRequestHandler rejectFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke_2.242
+ ___108-[TRIXPCNamespaceManagementRequestHandler statusOfDownloadForFactors:withNamespace:factorsState:completion:]_block_invoke.247
+ ___108-[TRIXPCNamespaceManagementRequestHandler statusOfDownloadForFactors:withNamespace:factorsState:completion:]_block_invoke.252
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.396
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.403
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.408
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.418
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.405
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.410
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.420
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_3.407
+ ___109-[TRIXPCNamespaceManagementRequestHandler promoteFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke.243
+ ___109-[TRIXPCNamespaceManagementRequestHandler promoteFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke.244
+ ___109-[TRIXPCNamespaceManagementRequestHandler promoteFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke_2.245
+ ___111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.327
+ ___111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.334
+ ___111-[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:deploymentEnvironment:completion:]_block_invoke
+ ___111-[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:deploymentEnvironment:completion:]_block_invoke.58
+ ___111-[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:deploymentEnvironment:completion:]_block_invoke.63
+ ___111-[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:deploymentEnvironment:completion:]_block_invoke.84
+ ___111-[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:deploymentEnvironment:completion:]_block_invoke.90
+ ___111-[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:deploymentEnvironment:completion:]_block_invoke_2
+ ___112-[TRIInternalServiceRequestHandler experimentNotificationsWithExperimentId:cloudKitContainer:teamId:completion:]_block_invoke.54
+ ___112-[TRIInternalServiceRequestHandler experimentNotificationsWithExperimentId:cloudKitContainer:teamId:completion:]_block_invoke.82
+ ___114-[TRIXPCNamespaceManagementRequestHandler immediateDownloadForNamespaceNames:allowExpensiveNetworking:completion:]_block_invoke.205
+ ___114-[TRIXPCNamespaceManagementRequestHandler immediateDownloadForNamespaceNames:allowExpensiveNetworking:completion:]_block_invoke.207
+ ___114-[TRIXPCNamespaceManagementRequestHandler immediateDownloadForNamespaceNames:allowExpensiveNetworking:completion:]_block_invoke.214
+ ___115+[TRIExperimentPostLaunchEvent(EventFactory) allocationEventWithTriple:isDynamicEnrollment:environment:namespaces:]_block_invoke
+ ___115-[TRICKNativeArtifactProvider _fetchRecordIdsForAssetsWithIds:options:cursor:cancelableOp:resultBuffer:completion:]_block_invoke.254
+ ___115-[TRIInternalAgentToSystemServiceRequestHandler updateFactorPackForUserId:atGlobalPath:deletingFactors:completion:]_block_invoke
+ ___115-[TRIInternalAgentToSystemServiceRequestHandler updateFactorPackForUserId:atGlobalPath:deletingFactors:completion:]_block_invoke.61
+ ___116-[TRICKNativeArtifactProvider _fetchRolloutNotificationsWithCursor:options:sinceDate:namespaceNames:resultsHandler:]_block_invoke.237
+ ___116-[TRIRolloutDatabase targetDeployment:toFactorPackSetId:targetingRuleIndex:deallocatedDeployments:usingTransaction:]_block_invoke.175
+ ___117-[TRIInternalAgentToSystemServiceRequestHandler updateFactorPackForUserId:atGlobalPath:populatingFactors:completion:]_block_invoke
+ ___117-[TRIInternalAgentToSystemServiceRequestHandler updateFactorPackForUserId:atGlobalPath:populatingFactors:completion:]_block_invoke.56
+ ___118+[TRIXPCNamespaceManagementRequestHandler usingServerContext:deregisterNamespaceWithName:teamId:taskQueue:completion:]_block_invoke.324
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.532
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.535
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.544
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.545
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke_2.533
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke_2.536
+ ___118-[TRIInternalAgentToSystemServiceRequestHandler _getOnDemandReferenceCountsAtGlobalPath:onDemandFactorsPerUser:error:]_block_invoke
+ ___119-[TRICKNativeArtifactProvider fetchDiffSourceRecordIdsWithTargetAssetIds:isAcceptableSourceAssetId:options:completion:]_block_invoke.282
+ ___119-[TRICKNativeArtifactProvider fetchDiffSourceRecordIdsWithTargetAssetIds:isAcceptableSourceAssetId:options:completion:]_block_invoke.284
+ ___119-[TRIXPCNamespaceManagementRequestHandler startDownloadLevelsForFactors:withNamespace:factorsState:options:completion:]_block_invoke.184
+ ___119-[TRIXPCNamespaceManagementRequestHandler startDownloadLevelsForFactors:withNamespace:factorsState:options:completion:]_block_invoke.189
+ ___119-[TRIXPCNamespaceManagementRequestHandler startDownloadLevelsForFactors:withNamespace:factorsState:options:completion:]_block_invoke_2.190
+ ___122-[TRIXPCNamespaceManagementRequestHandler removeLevelsForFactors:withNamespace:factorsState:removeImmediately:completion:]_block_invoke.215
+ ___122-[TRIXPCNamespaceManagementRequestHandler removeLevelsForFactors:withNamespace:factorsState:removeImmediately:completion:]_block_invoke.219
+ ___122-[TRIXPCNamespaceManagementRequestHandler removeLevelsForFactors:withNamespace:factorsState:removeImmediately:completion:]_block_invoke_2.220
+ ___124-[TRIInternalAgentToSystemServiceRequestHandler migrateToGlobalAssetStoreIfNeededFromLocalStore:sourceExtension:completion:]_block_invoke
+ ___124-[TRIInternalAgentToSystemServiceRequestHandler migrateToGlobalAssetStoreIfNeededFromLocalStore:sourceExtension:completion:]_block_invoke.88
+ ___124-[TRIInternalServiceRequestHandler rolloutNotificationWithLatestDeploymentForRolloutId:cloudKitContainer:teamId:completion:]_block_invoke.85
+ ___124-[TRIInternalServiceRequestHandler rolloutNotificationWithLatestDeploymentForRolloutId:cloudKitContainer:teamId:completion:]_block_invoke.91
+ ___125-[TRIExperimentDatabase addExperimentWithExperimentDeployment:environment:type:status:startDate:endDate:namespaces:artifact:]_block_invoke.48
+ ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke.452
+ ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_2.454
+ ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_3.455
+ ___127-[TRICKNativeArtifactProvider _fetchNotificationsWithQueryType:withCursor:withNamespaceNames:sinceDate:options:resultsHandler:]_block_invoke.169
+ ___127-[TRICKNativeArtifactProvider _fetchNotificationsWithQueryType:withCursor:withNamespaceNames:sinceDate:options:resultsHandler:]_block_invoke.170
+ ___127-[TRICKNativeArtifactProvider _fetchNotificationsWithQueryType:withCursor:withNamespaceNames:sinceDate:options:resultsHandler:]_block_invoke.174
+ ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.473
+ ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.487
+ ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke_2.478
+ ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke_4
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.546
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.548
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.549
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.550
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke_2.547
+ ___129-[TRICKNativeArtifactProvider fetchExperimentNotificationsForLimitedCarryExperimentWithManager:options:rollbacksOnly:completion:]_block_invoke.197
+ ___129-[TRICKNativeArtifactProvider fetchExperimentNotificationsForLimitedCarryExperimentWithManager:options:rollbacksOnly:completion:]_block_invoke.199
+ ___129-[TRISelectRolloutNotificationListTask _processRolloutArtifact:rolloutsProcessed:remainingNamespaces:targeter:context:taskQueue:]_block_invoke.45
+ ___130-[TRICKNativeArtifactProvider _fetchExperimentsWithCursor:withNamespaceNames:sinceDate:fetchRollbacksOnly:options:resultsHandler:]_block_invoke.167
+ ___131-[TRIClientTreatment(TRIUtil) _triRequiredMAAssetsForInstallationWithAssetStore:subscriptionSettings:maProvider:aliasToUnaliasMap:]_block_invoke.310
+ ___138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke.526
+ ___138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke_2.528
+ ___139-[TRIInternalAgentToSystemServiceRequestHandler referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:sourceExtension:completion:]_block_invoke
+ ___139-[TRIInternalAgentToSystemServiceRequestHandler referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:sourceExtension:completion:]_block_invoke.45
+ ___139-[TRIInternalAgentToSystemServiceRequestHandler saveFactorPackForUserId:toGlobalPath:fromTemporaryPath:factors:sourceExtension:completion:]_block_invoke
+ ___139-[TRIInternalAgentToSystemServiceRequestHandler saveFactorPackForUserId:toGlobalPath:fromTemporaryPath:factors:sourceExtension:completion:]_block_invoke.48
+ ___146-[TRIInternalAgentToSystemServiceRequestHandler saveAssetWithIdentifier:sourcePath:flockWitness:removeSourceOnFailure:sourceExtension:completion:]_block_invoke
+ ___146-[TRIInternalAgentToSystemServiceRequestHandler saveAssetWithIdentifier:sourcePath:flockWitness:removeSourceOnFailure:sourceExtension:completion:]_block_invoke.43
+ ___148-[TRIInternalAgentToSystemServiceRequestHandler overwriteGlobalActiveFactorProvidersWithNamespaceMap:factorPackMap:rolloutDeploymentMap:completion:]_block_invoke
+ ___148-[TRIInternalAgentToSystemServiceRequestHandler overwriteGlobalActiveFactorProvidersWithNamespaceMap:factorPackMap:rolloutDeploymentMap:completion:]_block_invoke.63
+ ___151-[TRIFetchTreatmentTask _fetchAssetsWithArtifactProvider:recordId:experimentRecord:assetIndexes:downloadOptions:context:assetURLs:treatmentFetchError:]_block_invoke.368
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.494
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.496
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.500
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.495
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.502
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_3.503
+ ___154-[TRIPurgeableExperimentAndRolloutProvider _factorPackSetHasPurgeableFactorsWithFPSId:eagerFactors:overriddenFactors:purgeableNamespaces:returningAssets:]_block_invoke.63
+ ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.364
+ ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.365
+ ___158-[TRICKNativeArtifactProvider fetchDiffsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.285
+ ___158-[TRICKNativeArtifactProvider fetchDiffsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.288
+ ___159-[TRICKNativeArtifactProvider fetchAssetsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.260
+ ___159-[TRICKNativeArtifactProvider fetchAssetsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.262
+ ___159-[TRICKNativeArtifactProvider fetchAssetsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke_2.266
+ ___163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.401
+ ___163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.406
+ ___163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.413
+ ___163-[TRIXPCNamespaceManagementRequestHandler registerNamespaceWithNamespaceName:compatibilityVersion:defaultsFileURL:applicationGroup:cloudKitContainerId:completion:]_block_invoke.109
+ ___163-[TRIXPCNamespaceManagementRequestHandler registerNamespaceWithNamespaceName:compatibilityVersion:defaultsFileURL:applicationGroup:cloudKitContainerId:completion:]_block_invoke.146
+ ___163-[TRIXPCNamespaceManagementRequestHandler registerNamespaceWithNamespaceName:compatibilityVersion:defaultsFileURL:applicationGroup:cloudKitContainerId:completion:]_block_invoke_2.147
+ ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.334
+ ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.336
+ ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.342
+ ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.415
+ ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.425
+ ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.421
+ ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.428
+ ___170-[TRIRolloutDatabase deactivateDeploymentsWithRolloutId:deactivatedDeployment:deactivatedFactorPackSetId:deactivatedRampId:deactivationStateTransitions:usingTransaction:]_block_invoke.190
+ ___174-[TRIPurgeableExperimentAndRolloutProvider _purgeablesForRolloutsFromNamespaces:eagerFactors:overriddenFactors:shouldGenerateAssetPaths:purgeableExperiments:purgeableAssets:]_block_invoke.43
+ ___175-[TRIInternalAgentToSystemServiceRequestHandler collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:completion:]_block_invoke
+ ___175-[TRIInternalAgentToSystemServiceRequestHandler collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:completion:]_block_invoke.46
+ ___177-[TRIPurgeableExperimentAndRolloutProvider _purgeablesForExperimentsFromNamespaces:eagerFactors:overriddenFactors:shouldGenerateAssetPaths:purgeableExperiments:purgeableAssets:]_block_invoke.40
+ ___177-[TRIRolloutDatabase activateDeployment:withFactorPackSetId:targetingRuleIndex:deactivatedDeployments:deactivatedFactorPackSetIds:deactivationStateTransitions:usingTransaction:]_block_invoke.183
+ ___178-[TRIInternalServiceRequestHandler registerNamespaceWithNamespaceName:compatibilityVersion:defaultsFileURL:teamId:appContainerId:appContainerType:cloudKitContainerId:completion:]_block_invoke.125
+ ___179+[TRIXPCNamespaceManagementRequestHandler _immediateDownloadForNamespaceNames:usingEntitlementWitness:serverContext:taskQueue:allowExpensiveNetworking:taskAttribution:completion:]_block_invoke.378
+ ___19-[TRIDServer start]_block_invoke.376
+ ___19-[TRIDServer start]_block_invoke.377
+ ___19-[TRIDServer start]_block_invoke.381
+ ___19-[TRIDServer start]_block_invoke.385
+ ___19-[TRIDServer start]_block_invoke.393
+ ___19-[TRIDServer start]_block_invoke_2.394
+ ___24+[TRISystemInfo _hasAne]_block_invoke
+ ___257+[TRIXPCNamespaceManagementRequestHandler _startDownloadAssetIndexesByTreatment:usingEntitlementWitness:serverContext:taskQueue:experimentIds:assetIdsByFactorPack:rolloutFactorNames:rolloutDeployments:namespace:taskAttribution:factorsState:notificationKey:]_block_invoke.363
+ ___27-[TRITaskDatabase allTasks]_block_invoke.110
+ ___27-[TRITaskDatabase allTasks]_block_invoke_2.114
+ ___28+[TRISystemInfo _aneVersion]_block_invoke
+ ___30+[TRISystemInfo _mapsBucketId]_block_invoke
+ ___30-[TRIEagerExitManager dealloc]_block_invoke
+ ___31-[TRILogger _dispatchLogEvent:]_block_invoke
+ ___33-[TRISystemConfiguration osBuild]_block_invoke
+ ___34+[TRISystemInfo _isVirtualMachine]_block_invoke
+ ___34-[TRICancelableMAOperation cancel]_block_invoke.486
+ ___37-[TRISystemConfiguration deviceClass]_block_invoke
+ ___37-[TRISystemInfo externalParamManager]_block_invoke
+ ___38-[TRILogger _incrementedLogEventCount]_block_invoke
+ ___38-[TRISystemConfiguration deviceChipId]_block_invoke
+ ___40+[TRISystemConfiguration sharedInstance]_block_invoke
+ ___40-[TRISystemConfiguration deviceSystemId]_block_invoke
+ ___40-[TRITaskDatabase tasksDependentOnTask:]_block_invoke.187
+ ___41-[TRIExternalParameterManager dictionary]_block_invoke
+ ___41-[TRISystemConfiguration deviceModelCode]_block_invoke
+ ___41-[TRITaskDatabase _tasksForQuery:onPrep:]_block_invoke.138
+ ___41-[TRITaskDatabase _tasksForQuery:onPrep:]_block_invoke_2.139
+ ___41-[TRITaskDatabase taskTypeForTaskWithId:]_block_invoke
+ ___41-[TRITaskDatabase taskTypeForTaskWithId:]_block_invoke_2
+ ___41-[TRITaskDatabase taskTypeForTaskWithId:]_block_invoke_3
+ ___42-[TRIDatabase migration_addTaskCapability]_block_invoke.329
+ ___42-[TRISystemConfiguration reloadSystemInfo]_block_invoke
+ ___43+[TRISystemConfiguration _sharedSystemInfo]_block_invoke
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.409
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.419
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.426
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.432
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.452
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.485
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.488
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.489
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.420
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.427
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.433
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.438
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.453
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.490
+ ___44-[TRISystemConfiguration _updateSystemInfo:]_block_invoke
+ ___45+[TRICellularParameterManager sharedInstance]_block_invoke
+ ___45-[TRISystemConfiguration deviceHardwareModel]_block_invoke
+ ___46+[TRIXPCServices registerAgentToSystemService]_block_invoke
+ ___46-[TRIRolloutDatabase addNewRolloutWithRecord:]_block_invoke.48
+ ___46-[TRIRolloutDatabase addNewRolloutWithRecord:]_block_invoke.52
+ ___47-[TRITaskQueue _finalizeTask:withId:runResult:]_block_invoke.220
+ ___47-[TRITaskQueue _finalizeTask:withId:runResult:]_block_invoke.222
+ ___48+[TRISystemInfo _sysEnabledInputModeIdentifiers]_block_invoke
+ ___48+[TRISystemInfo _sysEnabledInputModeIdentifiers]_block_invoke_2
+ ___48-[TRIPETLogHandler logEvent:subgroupName:queue:]_block_invoke
+ ___48-[TRIPETLogHandler logEvent:subgroupName:queue:]_block_invoke_2
+ ___49-[TRISystemConfiguration _systemInfoWithIsStale:]_block_invoke
+ ___49-[TRITaskDatabase removeTaskWithId:cleanupBlock:]_block_invoke_5
+ ___50-[TRITaskDatabase directDependenciesOfTaskWithId:]_block_invoke.183
+ ___50-[TRITaskQueue _registerTaskQueueActivityForDate:]_block_invoke.293
+ ___50-[TRITaskQueue _registerTaskQueueActivityForDate:]_block_invoke.294
+ ___51+[TRIXPCServices registerTrialServicesWithPromise:]_block_invoke
+ ___51-[TRICellularParameterManager carrierBundleChange:]_block_invoke
+ ___51-[TRIXPCInternalServiceClient initForTrialdSystem:]_block_invoke
+ ___51-[TRIXPCInternalServiceClient initForTrialdSystem:]_block_invoke_2
+ ___52-[TRICellularParameterManager carrierCountryIsoCode]_block_invoke
+ ___52-[TRIMaintenanceTask runUsingContext:withTaskQueue:]_block_invoke
+ ___52-[TRIMaintenanceTask runUsingContext:withTaskQueue:]_block_invoke.89
+ ___52-[TRIMaintenanceTask runUsingContext:withTaskQueue:]_block_invoke.93
+ ___52-[TRIMaintenanceTask runUsingContext:withTaskQueue:]_block_invoke_2
+ ___52-[TRIMaintenanceTask runUsingContext:withTaskQueue:]_block_invoke_2.97
+ ___52-[TRIMaintenanceTask runUsingContext:withTaskQueue:]_block_invoke_3
+ ___52-[TRIMaintenanceTask runUsingContext:withTaskQueue:]_block_invoke_3.102
+ ___52-[TRIMaintenanceTask runUsingContext:withTaskQueue:]_block_invoke_4
+ ___52-[TRIMaintenanceTask runUsingContext:withTaskQueue:]_block_invoke_4.108
+ ___52-[TRIMaintenanceTask runUsingContext:withTaskQueue:]_block_invoke_5
+ ___52-[TRIMaintenanceTask runUsingContext:withTaskQueue:]_block_invoke_5.113
+ ___52-[TRIMaintenanceTask runUsingContext:withTaskQueue:]_block_invoke_6
+ ___52-[TRIRetargetAllTask runUsingContext:withTaskQueue:]_block_invoke.40
+ ___53+[TRIKnownEnvVarFactorsReader knownFactorsFromPaths:]_block_invoke
+ ___53-[TRIDatabase migration_dropShadowEvaluationDatabase]_block_invoke
+ ___53-[TRIMAProvider installedAssetsMatchingFullAssetIds:]_block_invoke.510
+ ___53-[TRIXPCActivityManager _registerPostUpgradeActivity]_block_invoke.361
+ ___53-[TRIXPCActivityManager _registerPostUpgradeActivity]_block_invoke.367
+ ___54-[TRICellularParameterManager carrierBundleIdentifier]_block_invoke
+ ___54-[TRIExternalParameterManager initWithProvider:paths:]_block_invoke
+ ___55-[TRIBiomeDataStreamProvider unsubscribeAllDataStreams]_block_invoke
+ ___55-[TRICellularParameterManager preferredDataSimChanged:]_block_invoke
+ ___55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.394
+ ___55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.398
+ ___56-[TRIXPCInternalServiceClient resumeTaskQueueWithError:]_block_invoke
+ ___56-[TRIXPCInternalServiceClient resumeTaskQueueWithError:]_block_invoke_2
+ ___57+[TRIXPCServices registerTrialSystemServicesWithPromise:]_block_invoke
+ ___57-[TRIAssetPurger purgeableAssetSizeForPurgeabilityLevel:]_block_invoke.119
+ ___57-[TRIDisenrollRolloutTask runUsingContext:withTaskQueue:]_block_invoke.65
+ ___57-[TRIXPCActivityManager _registerHotfixTargetingActivity]_block_invoke.379
+ ___57-[TRIXPCActivityManager _registerHotfixTargetingActivity]_block_invoke_2.380
+ ___58-[TRIActiveSysctlFactorsProvider activeSysctlFactorLevels]_block_invoke
+ ___59-[TRIActivateTreatmentTask runTaskUsingContext:experiment:]_block_invoke.171
+ ___59-[TRIActivateTreatmentTask runTaskUsingContext:experiment:]_block_invoke.173
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.459
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.484
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.503
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.505
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.500
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.506
+ ___59-[TRITaskQueue activeActivityDescriptorGrantingCapability:]_block_invoke.311
+ ___59-[TRIXPCStatusRequestHandler rolloutRecordsWithCompletion:]_block_invoke.110
+ ___59-[TRIXPCStatusRequestHandler rolloutRecordsWithCompletion:]_block_invoke.111
+ ___60-[TRIDeactivateTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.66
+ ___60-[TRIDeactivateTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.78
+ ___60-[TRIDeactivateTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.81
+ ___60-[TRIDeactivateTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.95
+ ___60-[TRIRolloutDatabase recordWithDeployment:usingTransaction:]_block_invoke.132
+ ___60-[TRIXPCActivityManager registerSetupAssistantFetchActivity]_block_invoke.376
+ ___60-[TRIXPCActivityManager registerSetupAssistantFetchActivity]_block_invoke.377
+ ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.452
+ ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.462
+ ___61-[TRIXPCInternalServiceClient performSyncXPCWithError:block:]_block_invoke
+ ___62-[TRIActiveEnvVarFactorsWriter _constructPlistForExperiments:]_block_invoke
+ ___62-[TRICellularParameterManager subscriberCountryCodeDidChange:]_block_invoke
+ ___62-[TRIInternalServiceRequestHandler taskRecordsWithCompletion:]_block_invoke.46
+ ___63-[TRISystemConfiguration _dispatchQueueForCarrierInfoGathering]_block_invoke
+ ___63-[TRITaskQueue enumerateTasksWithTagsIntersectingTagSet:block:]_block_invoke.286
+ ___64-[TRIEagerExitManager initWithExitCooldown:monitoringTaskQueue:]_block_invoke
+ ___64-[TRIInternalServiceRequestHandler setFailureInjectionDelegate:]_block_invoke.117
+ ___65-[TRIMaintenanceTask _cleanupUnusedContentWithContext:nextTasks:]_block_invoke.149
+ ___65-[TRIMaintenanceTask _cleanupUnusedContentWithContext:nextTasks:]_block_invoke.155
+ ___65-[TRIMaintenanceTask _cleanupUnusedContentWithContext:nextTasks:]_block_invoke.159
+ ___65-[TRIMaintenanceTask _cleanupUnusedContentWithContext:nextTasks:]_block_invoke.161
+ ___66-[TRIActiveLaunchdDeliveredExperimentsReader allActiveExperiments]_block_invoke
+ ___66-[TRIExternalParameterManager siriDeviceAggregationIdRotationDate]_block_invoke
+ ___66-[TRIInternalServiceRequestHandler resumeTaskQueueWithCompletion:]_block_invoke
+ ___66-[TRIInternalServiceRequestHandler resumeTaskQueueWithCompletion:]_block_invoke.108
+ ___66-[TRIInternalServiceRequestHandler resumeTaskQueueWithCompletion:]_block_invoke_2
+ ___66-[TRIInternalServiceRequestHandler submitTask:options:completion:]_block_invoke.93
+ ___67-[TRIExperimentDatabase enumerateActiveExperimentRecordsWithBlock:]_block_invoke
+ ___67-[TRIRolloutDatabase enumerateActiveRecordsUsingTransaction:block:]_block_invoke
+ ___67-[TRIXPCInternalServiceClient addWithoutRunningTask:options:error:]_block_invoke
+ ___67-[TRIXPCInternalServiceClient addWithoutRunningTask:options:error:]_block_invoke_2
+ ___68-[TRICellularParameterManager _dispatchQueueForCarrierInfoGathering]_block_invoke
+ ___68-[TRIEagerExitManager handleTaskQueueEmptyNotificationWithCooldown:]_block_invoke
+ ___68-[TRIXPCStatusRequestHandler rolloutAllocationStatusWithCompletion:]_block_invoke
+ ___69-[TRIFetchFactorPackSetTask _requiredAssetsForFactorPackSet:context:]_block_invoke.392
+ ___69-[TRITaskQueue resumeWithXPCActivityDescriptor:executeWhenSuspended:]_block_invoke.107
+ ___69-[TRITaskQueue resumeWithXPCActivityDescriptor:executeWhenSuspended:]_block_invoke.115
+ ___70-[TRISelectRolloutNotificationListTask runUsingContext:withTaskQueue:]_block_invoke.76
+ ___71-[TRIAssetPurger purgeAssetsForPurgeabilityLevel:requestedPurgeAmount:]_block_invoke.141
+ ___71-[TRICKNativeArtifactProvider fetchTreatmentWithId:options:completion:]_block_invoke.219
+ ___71-[TRIInternalServiceRequestHandler removeUnusedChannelsWithCompletion:]_block_invoke.121
+ ___72-[TRIExternalParameterManager _fetchSiriDeviceAggregationIdRotationDate]_block_invoke
+ ___72-[TRIExternalParameterManager _fetchSiriDeviceAggregationIdRotationDate]_block_invoke.33
+ ___72-[TRIExternalParameterManager _fetchSiriDeviceAggregationIdRotationDate]_block_invoke.35
+ ___72-[TRIXPCActivityManager _scheduleFetchTaskWithActivityDescriptor:label:]_block_invoke.339
+ ___73-[TRIBiomeDataStreamProvider _subscribeForStreamIdentifier:eventHandler:]_block_invoke
+ ___73-[TRIBiomeDataStreamProvider _subscribeForStreamIdentifier:eventHandler:]_block_invoke.23
+ ___73-[TRIFetchFactorPackSetTask _saveFactorPackSet:requiredAssetMap:context:]_block_invoke.450
+ ___73-[TRITaskQueue _evaluateRunConditionsWithGuardedData:shouldContinueWork:]_block_invoke.103
+ ___74-[TRIExperimentDatabase(EnvVarNamespacesProviding) activeEnvVarNamespaces]_block_invoke
+ ___74-[TRIExperimentDatabase(SysctlNamespacesProviding) activeSysctlNamespaces]_block_invoke
+ ___74-[TRIInternalServiceRequestHandler dynamicNamespaceRecordsWithCompletion:]_block_invoke.159
+ ___75-[TRICKNativeArtifactProvider fetchFactorPackSetWithId:options:completion:]_block_invoke.243
+ ___75-[TRIInternalServiceRequestHandler activeRolloutInformationWithCompletion:]_block_invoke
+ ___75-[TRIInternalServiceRequestHandler activeRolloutInformationWithCompletion:]_block_invoke.162
+ ___75-[TRIInternalServiceRequestHandler activeRolloutInformationWithCompletion:]_block_invoke_2
+ ___75-[TRIInternalServiceRequestHandler activeRolloutInformationWithCompletion:]_block_invoke_4
+ ___76-[TRIBiomeDataStreamProvider subscribeDataStreamForIdentifier:eventHandler:]_block_invoke
+ ___77-[TRIXPCInternalServiceClient treatmentValidForExperimentWithID:treatmentID:]_block_invoke
+ ___77-[TRIXPCInternalServiceClient treatmentValidForExperimentWithID:treatmentID:]_block_invoke_2
+ ___78-[TRIActiveLaunchdDeliveredExperimentsReader _factorLevelStringsForNamespace:]_block_invoke
+ ___78-[TRIInternalServiceRequestHandler isOptedOutOfExperimentationWithCompletion:]_block_invoke
+ ___78-[TRIInternalServiceRequestHandler resumeSQLiteCKDatabaseQueueWithCompletion:]_block_invoke.120
+ ___78-[TRIXPCActivityManager _scheduleMaintenanceTaskWithActivityDescriptor:label:]_block_invoke.345
+ ___79-[TRIFactorPackSetStorage migrateEligibleFactorPacksToGlobalWithServerContext:]_block_invoke.161
+ ___79-[TRIInternalServiceRequestHandler suspendSQLiteCKDatabaseQueueWithCompletion:]_block_invoke.118
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.517
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.522
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.525
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.530
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.533
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke_2.523
+ ___80-[TRIBiomeDataStreamProvider readLastDataStreamEventForIdentifier:eventHandler:]_block_invoke
+ ___80-[TRIBiomeDataStreamProvider readLastDataStreamEventForIdentifier:eventHandler:]_block_invoke.12
+ ___80-[TRIInternalServiceRequestHandler addWithoutRunningForTask:options:completion:]_block_invoke
+ ___80-[TRIInternalServiceRequestHandler addWithoutRunningForTask:options:completion:]_block_invoke.107
+ ___80-[TRIInternalServiceRequestHandler addWithoutRunningForTask:options:completion:]_block_invoke_2
+ ___80-[TRIInternalServiceRequestHandler lastFetchDateForContainer:teamId:completion:]_block_invoke.109
+ ___80-[TRIUrgentRollbackScheduler scheduleUrgentRollbackForExperiment:deploymentIds:]_block_invoke
+ ___81-[TRITaskQueue _addTask:options:guardedData:taskIdOut:accumulatedNewTaskRecords:]_block_invoke.277
+ ___81-[TRIXPCActivityManager _registerPostUpgradeActivityRequireInexpensiveNetworking]_block_invoke.368
+ ___81-[TRIXPCInternalAgentToSystemServiceListener listener:shouldAcceptNewConnection:]_block_invoke
+ ___81-[TRIXPCInternalAgentToSystemServiceListener listener:shouldAcceptNewConnection:]_block_invoke_2
+ ___81-[TRIXPCInternalAgentToSystemServiceListener listener:shouldAcceptNewConnection:]_block_invoke_3
+ ___82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.121
+ ___82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.128
+ ___82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.133
+ ___82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.140
+ ___82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke_2.130
+ ___82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke_2.135
+ ___82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke_3.132
+ ___83-[TRIDatabase migration_dropBMLTDatabasesAndShadowEvaluationRolloutsAndExperiments]_block_invoke
+ ___83-[TRIDatabase migration_dropBMLTDatabasesAndShadowEvaluationRolloutsAndExperiments]_block_invoke.347
+ ___83-[TRIDatabase migration_dropBMLTDatabasesAndShadowEvaluationRolloutsAndExperiments]_block_invoke.356
+ ___83-[TRIDatabase migration_dropBMLTDatabasesAndShadowEvaluationRolloutsAndExperiments]_block_invoke.359
+ ___83-[TRIDatabase migration_dropBMLTDatabasesAndShadowEvaluationRolloutsAndExperiments]_block_invoke.368
+ ___83-[TRIDatabase migration_dropBMLTDatabasesAndShadowEvaluationRolloutsAndExperiments]_block_invoke.371
+ ___83-[TRIExperimentDatabase _enumerateExperimentRecordsMatchingWhereClause:bind:block:]_block_invoke.146
+ ___83-[TRITaskQueue _startImmediateTasksIfNotAlreadyQueued:guardedData:didStartNewWork:]_block_invoke.250
+ ___83-[TRITaskQueue _startImmediateTasksIfNotAlreadyQueued:guardedData:didStartNewWork:]_block_invoke.251
+ ___84-[TRIInternalServiceRequestHandler setLastFetchDate:forContainer:teamId:completion:]_block_invoke.113
+ ___84-[TRIRemoteAssetStoreOperator saveFactorPackToGlobalPath:fromTemporaryPath:factors:]_block_invoke.391
+ ___85-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:completion:]_block_invoke
+ ___85-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:completion:]_block_invoke.106
+ ___85-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:completion:]_block_invoke.109
+ ___85-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:completion:]_block_invoke.93
+ ___85-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:completion:]_block_invoke_2
+ ___85-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:completion:]_block_invoke_3
+ ___87-[TRICKNativeArtifactProvider _fetchRolloutNotificationsWithCursor:options:completion:]_block_invoke.238
+ ___88-[TRIAssetStoreDatabase initWithPaths:databasePath:storageManagement:performMigrations:]_block_invoke.75
+ ___88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.355
+ ___88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.357
+ ___89-[TRIAssetStore _linkDirectoryAssetWithIdentifier:toCurrentPath:futurePath:flockWitness:]_block_invoke.386
+ ___90-[TRINamespaceResolverStorage overwriteActiveFactorProvidersUsingTransaction:fromContext:]_block_invoke.187
+ ___90-[TRINamespaceResolverStorage overwriteActiveFactorProvidersUsingTransaction:fromContext:]_block_invoke.199
+ ___90-[TRINamespaceResolverStorage overwriteActiveFactorProvidersUsingTransaction:fromContext:]_block_invoke_2.201
+ ___91-[TRIBiomeDataStreamProvider readLastDataStreamEventForIdentifier:withFilter:eventHandler:]_block_invoke
+ ___91-[TRIBiomeDataStreamProvider readLastDataStreamEventForIdentifier:withFilter:eventHandler:]_block_invoke.16
+ ___91-[TRIBiomeDataStreamProvider readLastDataStreamEventForIdentifier:withFilter:eventHandler:]_block_invoke_2
+ ___91-[TRIInternalServiceRequestHandler activeExperimentInformationWithEnvironments:completion:]_block_invoke
+ ___91-[TRIInternalServiceRequestHandler activeExperimentInformationWithEnvironments:completion:]_block_invoke_2
+ ___91-[TRIInternalServiceRequestHandler deregisterNamespaceWithNamespaceName:teamId:completion:]_block_invoke.146
+ ___91-[TRIXPCNamespaceManagementRequestHandler deregisterNamespaceWithNamespaceName:completion:]_block_invoke.149
+ ___91-[TRIXPCNamespaceManagementRequestHandler deregisterNamespaceWithNamespaceName:completion:]_block_invoke.150
+ ___91-[TRIXPCNamespaceManagementRequestHandler deregisterNamespaceWithNamespaceName:completion:]_block_invoke_2.151
+ ___92-[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]_block_invoke.229
+ ___92-[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]_block_invoke.233
+ ___92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.250
+ ___92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.253
+ ___92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.255
+ ___92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.258
+ ___92-[TRIXPCNamespaceManagementRequestHandler loadNamespaceMetadataForNamespaceName:completion:]_block_invoke.225
+ ___92-[TRIXPCNamespaceManagementRequestHandler loadNamespaceMetadataForNamespaceName:completion:]_block_invoke.229
+ ___92-[TRIXPCNamespaceManagementRequestHandler loadNamespaceMetadataForNamespaceName:completion:]_block_invoke_2.230
+ ___93-[TRIInternalServiceRequestHandler startDownloadNamespaceWithName:teamId:options:completion:]_block_invoke.156
+ ___93-[TRIInternalServiceRequestHandler treatmentValidForExperimentWithId:treatmentId:completion:]_block_invoke
+ ___93-[TRIInternalServiceRequestHandler treatmentValidForExperimentWithId:treatmentId:completion:]_block_invoke_2
+ ___93-[TRIXPCNamespaceManagementRequestHandler startDownloadNamespaceWithName:options:completion:]_block_invoke.152
+ ___93-[TRIXPCNamespaceManagementRequestHandler startDownloadNamespaceWithName:options:completion:]_block_invoke.166
+ ___93-[TRIXPCNamespaceManagementRequestHandler startDownloadNamespaceWithName:options:completion:]_block_invoke_2.167
+ ___94-[TRIUrgentRollbackScheduler _activeExperimentDeploymentsForRollbackExperiment:deploymentIds:]_block_invoke
+ ___95-[TRIClientTreatmentStorage _saveNamespacePartitionedTreatmentsForTreatment:forNamespaceNames:]_block_invoke
+ ___96-[TRICKNativeArtifactProvider _fetchExperimentWithExperimentId:deploymentId:options:completion:]_block_invoke.152
+ ___96-[TRICKNativeArtifactProvider _fetchExperimentWithExperimentId:deploymentId:options:completion:]_block_invoke.155
+ ___97-[TRIFBClientTreatmentStorage _saveNamespacePartitionedTreatmentsForTreatment:forNamespaceNames:]_block_invoke
+ ___98-[TRIUrgentRollbackScheduler _ineligibleExperimentDeploymentsForRollbackExperiment:deploymentIds:]_block_invoke
+ ___98-[TRIXPCNamespaceManagementRequestHandler setProvisionalFactorPackId:forNamespaceName:completion:]_block_invoke.231
+ ___98-[TRIXPCNamespaceManagementRequestHandler setProvisionalFactorPackId:forNamespaceName:completion:]_block_invoke.235
+ ___98-[TRIXPCNamespaceManagementRequestHandler setProvisionalFactorPackId:forNamespaceName:completion:]_block_invoke_2.236
+ ___99-[TRIInternalAgentToSystemServiceRequestHandler removeUnreferencedGlobalFactorPacksWithCompletion:]_block_invoke
+ ___99-[TRIInternalAgentToSystemServiceRequestHandler removeUnreferencedGlobalFactorPacksWithCompletion:]_block_invoke.62
+ ___AppleNeuralEngineLibraryCore_block_invoke
+ ___Block_byref_object_copy_.257
+ ___Block_byref_object_dispose_.258
+ ___CoreTelephonyLibraryCore_block_invoke
+ ___TextInputLibraryCore_block_invoke
+ ____loggingAppDomain_block_invoke
+ ___assert_rtn
+ ___block_descriptor_138_e8_32s40s48s56s64s72s80s88s96s104s112s120s128r_e64_{_PASDBTransactionCompletion_=B}16?0"_PASSqlWriteTransaction"8ls32l8s40l8r128l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8
+ ___block_descriptor_32_e24_16?0"TRIFactorLevel"8l
+ ___block_descriptor_40_e8_32bs_e22_B16?0"BMStoreEvent"8ls32l8
+ ___block_descriptor_40_e8_32bs_e22_v16?0"BMStoreEvent"8ls32l8
+ ___block_descriptor_40_e8_32bs_e23_v16?0"BPSCompletion"8ls32l8
+ ___block_descriptor_40_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32r_e34_v16?0"TRISystemInfoGuardedData"8lr32l8
+ ___block_descriptor_40_e8_32r_e41_v16?0"TRICellularParameterGuardedData"8lr32l8
+ ___block_descriptor_40_e8_32r_e41_v16?0"TRIExternalParameterGuardedData"8lr32l8
+ ___block_descriptor_40_e8_32s_e18_B16?0"NSString"8ls32l8
+ ___block_descriptor_40_e8_32s_e22_B16?0"NSDictionary"8ls32l8
+ ___block_descriptor_40_e8_32s_e25_v32?0"NSString"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e38_B24?0"NSXPCConnection"8"NSString"16ls32l8
+ ___block_descriptor_40_e8_32s_e41_v16?0"TRIExternalParameterGuardedData"8ls32l8
+ ___block_descriptor_40_e8_32s_e47_v24?0"TRIServerContext"8"<TRITaskQueuing>"16ls32l8
+ ___block_descriptor_46_e8_32s_e8_v16?0Q8ls32l8
+ ___block_descriptor_48_e5_v8?0l
+ ___block_descriptor_48_e8_32r_e34_v16?0"TRISystemInfoGuardedData"8lr32l8
+ ___block_descriptor_48_e8_32s40r_e30_v24?0"NSNumber"8"NSError"16lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e34_v16?0"TRISystemInfoGuardedData"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e41_v16?0"TRICellularParameterGuardedData"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e34_v24?0"NSDictionary"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32w_e8_v12?0i8lw32l8
+ ___block_descriptor_56_e8_32s40bs48r_e45_v32?0"CKRecordID"8"CKRecord"16"NSError"24lr48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40s48r_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e41_v16?0"<TRIXPCInternalServiceProtocol>"8ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e41_v16?0"TRIExternalParameterGuardedData"8ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e30_v24?0"NSNumber"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48s_e8_v16?0Q8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e47_v24?0"TRIServerContext"8"<TRITaskQueuing>"16lw56l8s48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r_e45_v32?0"NSString"8"TRIClientTreatment"16^B24ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e33_v24?0"TRIExperimentRecord"8^B16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_65_e8_32s40s48s56s_e8_v16?0Q8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e37_v32?0"NSString"8"NSIndexSet"16^B24lr56l8s32l8s40l8s48l8r64l8
+ ___block_descriptor_76_e8_32s40s48bs56bs_e47_v24?0"TRIServerContext"8"<TRITaskQueuing>"16ls48l8s56l8s32l8s40l8
+ ___block_descriptor_88_e8_32s40s48bs56r64r72r_e64_{_PASDBTransactionCompletion_=B}16?0"_PASSqlWriteTransaction"8ls48l8s32l8s40l8r56l8r64l8r72l8
+ ___block_literal_global.10
+ ___block_literal_global.100
+ ___block_literal_global.106
+ ___block_literal_global.107
+ ___block_literal_global.117
+ ___block_literal_global.119
+ ___block_literal_global.121
+ ___block_literal_global.123
+ ___block_literal_global.124
+ ___block_literal_global.126
+ ___block_literal_global.128
+ ___block_literal_global.13
+ ___block_literal_global.130
+ ___block_literal_global.149
+ ___block_literal_global.151
+ ___block_literal_global.154
+ ___block_literal_global.159
+ ___block_literal_global.16
+ ___block_literal_global.161
+ ___block_literal_global.172
+ ___block_literal_global.186
+ ___block_literal_global.19
+ ___block_literal_global.2
+ ___block_literal_global.201
+ ___block_literal_global.227
+ ___block_literal_global.256
+ ___block_literal_global.268
+ ___block_literal_global.270
+ ___block_literal_global.283
+ ___block_literal_global.284
+ ___block_literal_global.291
+ ___block_literal_global.293
+ ___block_literal_global.299
+ ___block_literal_global.30
+ ___block_literal_global.301
+ ___block_literal_global.311
+ ___block_literal_global.313
+ ___block_literal_global.315
+ ___block_literal_global.338
+ ___block_literal_global.343
+ ___block_literal_global.346
+ ___block_literal_global.349
+ ___block_literal_global.358
+ ___block_literal_global.370
+ ___block_literal_global.373
+ ___block_literal_global.374
+ ___block_literal_global.383
+ ___block_literal_global.384
+ ___block_literal_global.388
+ ___block_literal_global.396
+ ___block_literal_global.407
+ ___block_literal_global.422
+ ___block_literal_global.439
+ ___block_literal_global.446
+ ___block_literal_global.455
+ ___block_literal_global.457
+ ___block_literal_global.5
+ ___block_literal_global.50
+ ___block_literal_global.511
+ ___block_literal_global.515
+ ___block_literal_global.553
+ ___block_literal_global.567
+ ___block_literal_global.570
+ ___block_literal_global.7
+ ___block_literal_global.90
+ ___block_literal_global.98
+ ___getCTBundleClass_block_invoke
+ ___getCoreTelephonyClientClass_block_invoke
+ ___getTIInputModeControllerClass_block_invoke
+ ___get_ANEDeviceInfoClass_block_invoke
+ ___strlcpy_chk
+ __dispatch_source_type_timer
+ __loggingAppDomain
+ _audit_stringAppleNeuralEngine
+ _audit_stringCoreTelephony
+ _audit_stringTextInput
+ _descriptor.descriptor.205
+ _descriptor.descriptor.217
+ _descriptor.descriptor.232
+ _descriptor.descriptor.241
+ _descriptor.descriptor.278
+ _descriptor.descriptor.290
+ _descriptor.descriptor.303
+ _descriptor.descriptor.320
+ _descriptor.descriptor.327
+ _descriptor.descriptor.344
+ _descriptor.descriptor.351
+ _descriptor.descriptor.364
+ _descriptor.descriptor.371
+ _descriptor.descriptor.377
+ _descriptor.descriptor.384
+ _descriptor.descriptor.397
+ _descriptor.descriptor.404
+ _descriptor.descriptor.411
+ _descriptor.fields.218
+ _descriptor.fields.233
+ _descriptor.fields.242
+ _descriptor.fields.279
+ _descriptor.fields.291
+ _descriptor.fields.304
+ _descriptor.fields.321
+ _descriptor.fields.328
+ _descriptor.fields.345
+ _descriptor.fields.352
+ _descriptor.fields.365
+ _descriptor.fields.378
+ _descriptor.fields.385
+ _descriptor.fields.398
+ _descriptor.fields.405
+ _dispatch_assert_queue$V2
+ _dispatch_group_wait
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_source_cancel
+ _dispatch_source_set_timer
+ _dispatch_source_testcancel
+ _dispatch_time
+ _dlopenHelper$Accounts
+ _dlopenHelper$AppleAccount
+ _dlopenHelper$GeoServices
+ _dlopenHelperFlag$Accounts
+ _dlopenHelperFlag$AppleAccount
+ _dlopenHelperFlag$GeoServices
+ _dummyValue
+ _getCTBundleClass.softClass
+ _getCoreTelephonyClientClass.softClass
+ _get_ANEDeviceInfoClass
+ _gotLoadHelper_x8$_AAErrorDomain
+ _gotLoadHelper_x8$_OBJC_CLASS_$_ACAccountStore
+ _gotLoadHelper_x8$_OBJC_CLASS_$_ACXPCEventSubscriber
+ _gotLoadHelper_x8$_OBJC_CLASS_$_GEOCountryConfiguration
+ _gotLoadHelper_x8$_OBJC_CLASS_$_GEOExperimentConfiguration
+ _kAssistantDictationEnabled
+ _kKeyboardDictationLanguagesEnabledKey
+ _kKeyboardPreferenceDomain
+ _kTRISysctlExperimentMagicBundleIdentifier
+ _logEvent:subgroupName:queue:._pasOnceToken2
+ _objc_msgSend$DSLPublisher
+ _objc_msgSend$_activeExperimentDeploymentsForRollbackExperiment:deploymentIds:
+ _objc_msgSend$_aneVersion
+ _objc_msgSend$_appleIntelligenceState
+ _objc_msgSend$_carrierBundleIdentifier
+ _objc_msgSend$_carrierCountryIsoCode
+ _objc_msgSend$_checkTreatmentBasedExperimentForPurgeables:experimentAssets:experimentHasNamespaceWithEagerFactors:experimentHasPurgeableNamespace:overriddenFactors:record:shouldGenerateAssetPaths:storage:
+ _objc_msgSend$_deleteOnDemandAssetsWithFactorNames:treatment:namespace:
+ _objc_msgSend$_deleteOnDemandAssetsWithFactorNames:treatment:namespace:inUseAssetDeletionBehavior:
+ _objc_msgSend$_dispatchLogEvent:
+ _objc_msgSend$_dispatchQueueForCarrierInfoGathering
+ _objc_msgSend$_experimentRecord:matchesExperimentId:oneOfDeploymentIds:
+ _objc_msgSend$_experimentRecordsWithDeploymentEnvironments:serverContext:completion:
+ _objc_msgSend$_fetchCarrierBundleIdentifier:
+ _objc_msgSend$_fetchCarrierCountryIsoCode:
+ _objc_msgSend$_fetchSiriDeviceAggregationIdRotationDate
+ _objc_msgSend$_getLogger
+ _objc_msgSend$_getSiriDeviceAggregationIdRotationDate
+ _objc_msgSend$_handleUserSettingsNotificationWithContext:
+ _objc_msgSend$_hasAne
+ _objc_msgSend$_iCloudIdentifier
+ _objc_msgSend$_incrementedLogEventCount
+ _objc_msgSend$_ineligibleExperimentDeploymentsForRollbackExperiment:deploymentIds:
+ _objc_msgSend$_isAutomatedTestDevice
+ _objc_msgSend$_isDiagnosticsAndUsageEnabled
+ _objc_msgSend$_isExperimentEligibleWithArtifact:context:
+ _objc_msgSend$_isSeedBuild
+ _objc_msgSend$_isValidNextStateForEvent:
+ _objc_msgSend$_isVirtualMachine
+ _objc_msgSend$_levelAsString:
+ _objc_msgSend$_linkAssetWithId:treatmentId:assetStore:factor:
+ _objc_msgSend$_mapsBucketId
+ _objc_msgSend$_persistentSystemInfoPath
+ _objc_msgSend$_readParametersFromFile
+ _objc_msgSend$_readSiriDeviceAggregationIdRotationDateFromEvent:
+ _objc_msgSend$_saveNamespacePartitionedTreatmentsForTreatment:forNamespaceNames:
+ _objc_msgSend$_sharedCovariatesFromConfiguration:
+ _objc_msgSend$_sharedSystemInfo
+ _objc_msgSend$_singularAndUniqueNamespaceInRecord:alreadyMapped:
+ _objc_msgSend$_streamForIdentifier:eventHandler:
+ _objc_msgSend$_subscribeForStreamIdentifier:eventHandler:
+ _objc_msgSend$_sysEnabledInputModeIdentifiers
+ _objc_msgSend$_sysIsEnrolledInBetaProgram
+ _objc_msgSend$_systemInfoWithIsStale:
+ _objc_msgSend$_trialVersion
+ _objc_msgSend$_unsubscribeAllDataStreams
+ _objc_msgSend$_updateSystemInfo
+ _objc_msgSend$_userSpecificCovariatesFromConfiguration:
+ _objc_msgSend$_writeFactorPackToLegacyPath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:
+ _objc_msgSend$_writeIdBasedFactorPack:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:
+ _objc_msgSend$_writeParametersToFile
+ _objc_msgSend$aa_altDSID
+ _objc_msgSend$aa_primaryAppleAccount
+ _objc_msgSend$activatedEventWithExperimentRecord:
+ _objc_msgSend$activeDictationLocales
+ _objc_msgSend$activeEnvVarNamespaces
+ _objc_msgSend$activeSysctlFactorLevels
+ _objc_msgSend$activeSysctlNamespaces
+ _objc_msgSend$addNamespaceName:
+ _objc_msgSend$addTaskAfterOperationsFinish:
+ _objc_msgSend$addWithoutRunningForTask:options:completion:
+ _objc_msgSend$allocationEventWithTriple:isDynamicEnrollment:environment:namespaces:
+ _objc_msgSend$allowEnvVarDefaultLevelsDir
+ _objc_msgSend$aneSubType
+ _objc_msgSend$artifactFromCKRecordResult:withContainer:teamId:requireDeploymentId:completion:
+ _objc_msgSend$automatedDeviceGroup
+ _objc_msgSend$block
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$callerBundleId
+ _objc_msgSend$callerIsRunningFromSystemContext
+ _objc_msgSend$canonicalLanguageIdentifierFromString:
+ _objc_msgSend$context
+ _objc_msgSend$copyBundleIdentifier:bundleType:error:
+ _objc_msgSend$copyLastKnownMobileSubscriberCountryCode:error:
+ _objc_msgSend$copyMobileSubscriberIsoCountryCode:error:
+ _objc_msgSend$countryCode
+ _objc_msgSend$createDeviceIdentifierWithPath:
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$currentLocale
+ _objc_msgSend$currentPopulation
+ _objc_msgSend$dateByAddingComponents:toDate:options:
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$defaultStore
+ _objc_msgSend$deleteDeviceIdentifier
+ _objc_msgSend$deleteDeviceIdentifierWithPath:
+ _objc_msgSend$denormalizedEvent
+ _objc_msgSend$descriptor
+ _objc_msgSend$deviceChipId
+ _objc_msgSend$deviceHardwareModel
+ _objc_msgSend$deviceInfoForQuestion:
+ _objc_msgSend$deviceSystemId
+ _objc_msgSend$dictionaryWithContentsOfURL:error:
+ _objc_msgSend$dispatchTimeWithSecondsFromNow:
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$enumerateActiveExperimentRecordsWithBlock:
+ _objc_msgSend$enumerateActiveRecordsUsingTransaction:block:
+ _objc_msgSend$envVarExperimentWithTargetedBundleIds:factorLevelStrings:
+ _objc_msgSend$eventWithEventType:experimentRecord:
+ _objc_msgSend$eventWithTrackingId:projectId:
+ _objc_msgSend$exitTrialdCleanly
+ _objc_msgSend$experimentIdentifiers
+ _objc_msgSend$experimentIdentifiersWithNamespaceName:
+ _objc_msgSend$externalParamManager
+ _objc_msgSend$externalParametersFile
+ _objc_msgSend$factorProviderWithPaths:namespaceName:resolver:faultOnMissingInstalledFactors:
+ _objc_msgSend$fetchBucketID:
+ _objc_msgSend$fetchedEventWithExperimentRecord:
+ _objc_msgSend$fields
+ _objc_msgSend$filterWithIsIncluded:
+ _objc_msgSend$forLaunchDaemon
+ _objc_msgSend$getPreferredDataSubscriptionContextSync:
+ _objc_msgSend$handleTaskQueueEmptyNotificationWithCooldown:
+ _objc_msgSend$hasANE
+ _objc_msgSend$hasForLaunchDaemon
+ _objc_msgSend$hasTrialSystemTelemetry
+ _objc_msgSend$hasValidNamespacesWithError:
+ _objc_msgSend$hostingProcessIsTriald
+ _objc_msgSend$hostingProcessName
+ _objc_msgSend$iCloudIdentifier
+ _objc_msgSend$info
+ _objc_msgSend$initFromSystemWithFactorProvider:
+ _objc_msgSend$initWithActiveNamespacesProvider:factorLevelsRetriever:
+ _objc_msgSend$initWithBundleType:
+ _objc_msgSend$initWithClient:projectId:
+ _objc_msgSend$initWithDeployment:rampId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:namespaces:artifact:
+ _objc_msgSend$initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:experimentType:counterfactualTreatmentIds:
+ _objc_msgSend$initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isManuallyTargeted:artifact:experimentType:
+ _objc_msgSend$initWithExitCooldown:monitoringTaskQueue:
+ _objc_msgSend$initWithIdentifier:targetQueue:waking:
+ _objc_msgSend$initWithName:subtaskBlock:
+ _objc_msgSend$initWithProjectId:
+ _objc_msgSend$initWithPromise:forSystem:
+ _objc_msgSend$initWithProvider:paths:
+ _objc_msgSend$initWithQueue:
+ _objc_msgSend$initWithRollout:populations:deploymentDate:downloadSize:forLaunchDaemon:
+ _objc_msgSend$initWithSchemaVersion:forUser:forTrialdSystem:
+ _objc_msgSend$initWithServerContextPromise:forSystem:
+ _objc_msgSend$initWithServiceName:connectionOptions:allowlistedServerInterface:allowlistedClientInterface:serverInitiatedRequestHandler:allowSystemToUserConnection:interruptionHandler:invalidationHandler:logHandle:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$initWithSysctlFactorsProvider:sysctlWriter:
+ _objc_msgSend$initWithSysctlName:level:
+ _objc_msgSend$initWithType:experiment:treatment:rollout:factorPackSet:
+ _objc_msgSend$integerForKey:
+ _objc_msgSend$isEnrolledInBetaProgram
+ _objc_msgSend$isEqualToenvVarExperiment:
+ _objc_msgSend$json
+ _objc_msgSend$knownFactorsFromPaths:
+ _objc_msgSend$last
+ _objc_msgSend$loadSystemInfo
+ _objc_msgSend$lock
+ _objc_msgSend$logEvent:
+ _objc_msgSend$logEvent:subgroupName:queue:
+ _objc_msgSend$logEventId
+ _objc_msgSend$logMessage:
+ _objc_msgSend$logMessage:subGroup:
+ _objc_msgSend$logTimeFromDate:
+ _objc_msgSend$logUserKeyboardEnabledInputMode
+ _objc_msgSend$logUserSettingsLanguageCode
+ _objc_msgSend$logUserSettingsRegionCode
+ _objc_msgSend$logWithTrackingId:metric:dimensions:
+ _objc_msgSend$logWithTrackingId:metrics:dimensions:
+ _objc_msgSend$mapsBucketId
+ _objc_msgSend$mapsDeviceCountryCode
+ _objc_msgSend$oneofs
+ _objc_msgSend$operatingSystemVersion
+ _objc_msgSend$optInApple
+ _objc_msgSend$performSyncXPCWithError:block:
+ _objc_msgSend$persistActiveDicationLocales:
+ _objc_msgSend$persistMapsBucketId:
+ _objc_msgSend$persistMapsDeviceCountryCode:
+ _objc_msgSend$persistedActiveDicationLocales
+ _objc_msgSend$persistedMapsBucketId
+ _objc_msgSend$persistedMapsDeviceCountryCode
+ _objc_msgSend$processMapsBucketIdChangeIfNecessaryForBucketId:withServerContext:withTaskQueue:
+ _objc_msgSend$projectNameFromId:
+ _objc_msgSend$publishSysctlFactors
+ _objc_msgSend$publisher
+ _objc_msgSend$readDeviceIdentifierWithPath:
+ _objc_msgSend$readLastDataStreamEventForIdentifier:withFilter:eventHandler:
+ _objc_msgSend$registerAgentToSystemService
+ _objc_msgSend$registerTrialServicesWithPromise:
+ _objc_msgSend$requiresLogging
+ _objc_msgSend$resumeTaskQueueWithCompletion:
+ _objc_msgSend$saveToFile:
+ _objc_msgSend$setAneVersion:
+ _objc_msgSend$setAppleIntelligenceState:
+ _objc_msgSend$setCarrierBundleIdentifier:
+ _objc_msgSend$setCarrierCountryIsoCode:
+ _objc_msgSend$setClientProjectId:
+ _objc_msgSend$setDay:
+ _objc_msgSend$setDenormalizedEvent:
+ _objc_msgSend$setDeviceClass:
+ _objc_msgSend$setDeviceIdentifier:path:
+ _objc_msgSend$setDeviceLogTime:
+ _objc_msgSend$setIsAutomatedTestDevice:
+ _objc_msgSend$setLogEventId:
+ _objc_msgSend$setMlruntimeDimensions:
+ _objc_msgSend$setOsBuild:
+ _objc_msgSend$setProcessEventIndex:
+ _objc_msgSend$setProjectId:
+ _objc_msgSend$setTargetedPopulation:
+ _objc_msgSend$setTrialSystemTelemetry:
+ _objc_msgSend$setUserKeyboardEnabledInputModeIdentifiers:
+ _objc_msgSend$setUserSettingsBcp47DeviceLocale:
+ _objc_msgSend$setValue:
+ _objc_msgSend$setVersionTag:
+ _objc_msgSend$sharedConfiguration
+ _objc_msgSend$sharedPaths
+ _objc_msgSend$sinkWithCompletion:receiveInput:
+ _objc_msgSend$state
+ _objc_msgSend$storeExperimentEvent:isValidTransition:
+ _objc_msgSend$storedDeviceIdentifier
+ _objc_msgSend$streamWithIdentifier:error:
+ _objc_msgSend$stringForCurrentProcessEntitlement:
+ _objc_msgSend$subscribeOn:
+ _objc_msgSend$sysctlName
+ _objc_msgSend$systemDataFile
+ _objc_msgSend$systemInfo
+ _objc_msgSend$systemInfoFromFile:
+ _objc_msgSend$systemInteropDirectory
+ _objc_msgSend$taskTypeForTaskWithId:
+ _objc_msgSend$treatmentValidForExperimentWithId:treatmentId:completion:
+ _objc_msgSend$trialdTaskName
+ _objc_msgSend$unsubscribeAllDataStreams
+ _objc_msgSend$updateSavedTreatmentWithTreatmentId:deletingAssetsWithFactorNames:forNamespaceName:
+ _objc_msgSend$updateSavedTreatmentWithTreatmentId:deletingAssetsWithFactorNames:forNamespaceName:inUseAssetDeletionBehavior:
+ _objc_msgSend$validateBase64Signature:forDigest:
+ _objc_msgSend$validatedEnvironmentFromNumber:
+ _objc_msgSend$validatedPopulationFromNumber:
+ _objc_msgSend$writeSysctlWithName:intValue:
+ _objc_msgSend$writeToFile:atomically:encoding:error:
+ _objc_release_x7
+ _registerAgentToSystemService._pasOnceToken4
+ _registerTrialServicesWithPromise:._pasOnceToken2
+ _registerTrialSystemServicesWithPromise:._pasOnceToken3
+ _start._pasOnceToken21
+ _sysctlbyname
- +[TRIActivateTargetedBMLTDeploymentPersistedTask descriptor]
- +[TRIActivateTargetedBMLTDeploymentTask parseFromData:]
- +[TRIActivateTargetedBMLTDeploymentTask supportsSecureCoding]
- +[TRIActivateTargetedBMLTDeploymentTask taskWithBMLTDeployment:factorPackSetId:taskAttribution:]
- +[TRIActivateTargetedBMLTDeploymentTask taskWithBMLTDeployment:factorPackSetId:taskAttribution:bmltBatchNotificationIdentifier:]
- +[TRIActiveLowLevelExperiment lowLevelExperimentWithTargetedBundleIds:factorLevelStrings:]
- +[TRIActiveLowLevelExperiment supportsSecureCoding]
- +[TRIActiveLowLevelFactorStringBuilder stringForFactorLevel:]
- +[TRIBMLTTargeter _targetingErrorWithDeployment:errorType:details:]
- +[TRIBMLTTargeter targetingErrorWithDeployment:errorType:]
- +[TRIBMLTTargetingPersistedTask descriptor]
- +[TRIBMLTTargetingTask parseFromData:]
- +[TRIBMLTTargetingTask supportsSecureCoding]
- +[TRIBMLTTargetingTask taskWithBMLTDeployment:includeDependencies:taskAttribution:triggerEvent:]
- +[TRIBMLTTargetingTask taskWithBMLTDeployment:includeDependencies:taskAttribution:triggerEvent:bmltBatchNotificationIdentifier:]
- +[TRIBackgroundMLTaskRecord recordWithBmltDeployment:pluginId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:endDate:artifact:]
- +[TRICKOperationGroupFactory groupForBMLTId:]
- +[TRIClientBMLTArtifact artifactWithBackgroundTask:populations:deploymentType:deploymentDate:downloadSize:]
- +[TRIClientBMLTArtifact supportsSecureCoding]
- +[TRIClientBMLTArtifact(CloudKit) _isStructurallyValidBMLT:deployment:namespaceName:populations:deploymentType:deploymentDate:]
- +[TRIClientBMLTArtifact(CloudKit) allReferencedCKRecordKeys]
- +[TRIClientBMLTArtifact(CloudKit) artifactFromCKRecord:namespaceDescriptorProvider:error:]
- +[TRIClientBMLTArtifact(Utils) artifactWithTransientData:]
- +[TRIClientBMLTCatalogArtifact artifactWithBmltCatalog:population:]
- +[TRIClientBMLTCatalogArtifact supportsSecureCoding]
- +[TRIClientBMLTCatalogArtifact(CloudKit) _hasStructurallyValidBMLTs:population:]
- +[TRIClientBMLTCatalogArtifact(CloudKit) allReferencedCKRecordKeys]
- +[TRIClientBMLTCatalogArtifact(CloudKit) artifactFromCKRecord:error:]
- +[TRIClientExperimentArtifact(CloudKit) artifactFromCKRecordResult:withNamespaceDescriptorProvider:container:teamId:requireDeploymentId:completion:]
- +[TRIClientRolloutArtifact artifactWithRollout:populations:deploymentDate:downloadSize:]
- +[TRIContentDescriptorUnion unionWithType:experiment:treatment:rollout:factorPackSet:bmlt:]
- +[TRIContentTracker contentIdentifierForBMLTArtifactWithDeployment:]
- +[TRIDeactivateBMLTDeploymentPersistedTask descriptor]
- +[TRIDeactivateBMLTDeploymentTask parseFromData:]
- +[TRIDeactivateBMLTDeploymentTask supportsSecureCoding]
- +[TRIDeactivateBMLTDeploymentTask taskWithBMLTDeployment:triggerEvent:]
- +[TRIDeactivateBMLTDeploymentTask taskWithBMLTDeployment:triggerEvent:bmltBatchNotificationIdentifier:]
- +[TRIExperimentRecord recordWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:isManuallyTargeted:artifact:]
- +[TRIFetchBMLTNotificationsPersistedTask descriptor]
- +[TRIFetchBMLTNotificationsTask categoricalValueForBMLTNotificationEvent:]
- +[TRIFetchBMLTNotificationsTask parseFromData:]
- +[TRIFetchBMLTNotificationsTask supportsSecureCoding]
- +[TRIFetchBMLTNotificationsTask taskWithDeployment:taskAttribution:bmltBatchNotificationIdentifier:]
- +[TRIFetchBMLTNotificationsTask taskWithTaskAttribution:]
- +[TRIFetchFactorPackSetTask taskWithFactorPackSetId:taskAttribution:bmltDeployment:]
- +[TRIKnownLowLevelFactorsReader _knownFactorsFromPlistURL:]
- +[TRIKnownLowLevelFactorsReader knownFactorsFromPaths:]
- +[TRILighthouseBitacoraHandler donateTrialIdentifiers:eventType:succeeded:error:]
- +[TRILighthouseBitacoraHandler emitBMLTEventWithBMLTId:deploymentId:eventType:succeeded:]
- +[TRILighthouseBitacoraHandler emitShadowEvaluationEventWithExperimentId:deploymentId:treatmentId:eventType:succeeded:]
- +[TRIMakeDefaultPersistedTask descriptor]
- +[TRIMakeDefaultTask parseFromData:]
- +[TRIMakeDefaultTask supportsSecureCoding]
- +[TRIMakeDefaultTask taskWithExperiment:treatmentId:taskAttributing:capabilityModifier:]
- +[TRIPersistedClientBMLTArtifact descriptor]
- +[TRIRolloutRecord recordWithDeployment:rampId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:namespaces:isShadow:artifact:]
- +[TRITaskUtils _bmltStateForAnalyticsFromStatusType:]
- +[TRITaskUtils updateBMLTHistoryDatabaseWithAllocationStatus:forBMLT:deployment:fps:bmltRecord:context:]
- +[TRIXPCServices registerAllServicesWithPromise:]
- +[TRIXPCServices registerSystemService]
- -[TRIActivateTargetedBMLTDeploymentTask .cxx_destruct]
- -[TRIActivateTargetedBMLTDeploymentTask _activationTelemetryWithSuccess:bmltRecord:serverContext:]
- -[TRIActivateTargetedBMLTDeploymentTask _asPersistedTask]
- -[TRIActivateTargetedBMLTDeploymentTask _hasValidNCVForBMLT:namespaceDescriptorProvider:]
- -[TRIActivateTargetedBMLTDeploymentTask dependencies]
- -[TRIActivateTargetedBMLTDeploymentTask deployment]
- -[TRIActivateTargetedBMLTDeploymentTask description]
- -[TRIActivateTargetedBMLTDeploymentTask dimensions]
- -[TRIActivateTargetedBMLTDeploymentTask encodeWithCoder:]
- -[TRIActivateTargetedBMLTDeploymentTask factorPackSetId]
- -[TRIActivateTargetedBMLTDeploymentTask hash]
- -[TRIActivateTargetedBMLTDeploymentTask initWithCoder:]
- -[TRIActivateTargetedBMLTDeploymentTask initWithTaskDeployment:factorPackSetId:taskAttribution:bmltBatchNotificationIdentifier:]
- -[TRIActivateTargetedBMLTDeploymentTask isEqual:]
- -[TRIActivateTargetedBMLTDeploymentTask metrics]
- -[TRIActivateTargetedBMLTDeploymentTask requiredCapabilities]
- -[TRIActivateTargetedBMLTDeploymentTask runDequeueHandlerUsingContext:]
- -[TRIActivateTargetedBMLTDeploymentTask runEnqueueHandlerUsingContext:]
- -[TRIActivateTargetedBMLTDeploymentTask runUsingContext:withTaskQueue:]
- -[TRIActivateTargetedBMLTDeploymentTask serialize]
- -[TRIActivateTargetedBMLTDeploymentTask tags]
- -[TRIActivateTargetedBMLTDeploymentTask taskType]
- -[TRIActivateTargetedBMLTDeploymentTask trialSystemTelemetry]
- -[TRIActivateTargetedRolloutDeploymentTask _notifyUpdatedShadowEvaluationsWithDeployments:context:usingTransaction:]
- -[TRIActivateTreatmentBaseTask updateLoggingWithExperimentRecord:paths:trackingId:newLogTreatmentAddedOut:]
- -[TRIActivateTreatmentTask _notifyUpdatedShadowEvaluationWithExperimentRecord:context:]
- -[TRIActiveLowLevelExperiment .cxx_destruct]
- -[TRIActiveLowLevelExperiment copyWithReplacementFactorLevelStrings:]
- -[TRIActiveLowLevelExperiment copyWithReplacementTargetedBundleIds:]
- -[TRIActiveLowLevelExperiment copyWithZone:]
- -[TRIActiveLowLevelExperiment description]
- -[TRIActiveLowLevelExperiment encodeWithCoder:]
- -[TRIActiveLowLevelExperiment factorLevelStrings]
- -[TRIActiveLowLevelExperiment hash]
- -[TRIActiveLowLevelExperiment initWithCoder:]
- -[TRIActiveLowLevelExperiment initWithTargetedBundleIds:factorLevelStrings:]
- -[TRIActiveLowLevelExperiment init]
- -[TRIActiveLowLevelExperiment isEqual:]
- -[TRIActiveLowLevelExperiment isEqualTolowLevelExperiment:]
- -[TRIActiveLowLevelExperiment targetedBundleIds]
- -[TRIActiveLowLevelExperimentsReader .cxx_destruct]
- -[TRIActiveLowLevelExperimentsReader _factorLevelStringsForNamespace:]
- -[TRIActiveLowLevelExperimentsReader allActiveExperiments]
- -[TRIActiveLowLevelExperimentsReader initWithNamespacesProvider:factorLevelsRetriever:]
- -[TRIActiveLowLevelFactorsPublisher .cxx_destruct]
- -[TRIActiveLowLevelFactorsPublisher initWithNamespacesProvider:factorRetriever:writer:]
- -[TRIActiveLowLevelFactorsPublisher initWithServerContext:]
- -[TRIActiveLowLevelFactorsPublisher publishLowLevelFactors]
- -[TRIActiveLowLevelFactorsWriter .cxx_destruct]
- -[TRIActiveLowLevelFactorsWriter _constructPlistForExperiments:]
- -[TRIActiveLowLevelFactorsWriter initWithPaths:]
- -[TRIActiveLowLevelFactorsWriter writeExperiments:]
- -[TRIBMLTDeployment(Utils) shortDesc]
- -[TRIBMLTDeployment(Utils) taskTag]
- -[TRIBMLTDeploymentRefStore .cxx_destruct]
- -[TRIBMLTDeploymentRefStore hasReferenceToPath:]
- -[TRIBMLTDeploymentRefStore initWithServerContext:]
- -[TRIBMLTTargeter .cxx_destruct]
- -[TRIBMLTTargeter _evaluateExpressionForDeployment:context:assignment:fpsId:error:]
- -[TRIBMLTTargeter initWithDatabase:systemCovariateProvider:userCovariateProvider:]
- -[TRIBMLTTargeter init]
- -[TRIBMLTTargeter systemCovariateProvider]
- -[TRIBMLTTargeter targetBMLT:factorPackSetId:error:]
- -[TRIBMLTTargeter userCovariateProvider]
- -[TRIBMLTTargetingTask .cxx_destruct]
- -[TRIBMLTTargetingTask _allocationTelemetryWithEvent:factorPackSetId:bmltRecord:context:]
- -[TRIBMLTTargetingTask _asPersistedTask]
- -[TRIBMLTTargetingTask _categoricalValueForTriggerEvent:]
- -[TRIBMLTTargetingTask _targetBMLTDeployment:appendingTelemetryToSupport:backgroundMLTaskDatabase:backgroundMLTaskHistoryDatabase:targeter:reportTelemetryToServer:factorPackSetIdToActivate:wasEnrolled:shouldDisenroll:error:]
- -[TRIBMLTTargetingTask _taskResultWithStatus:wasEnrolled:reportResults:nextTasks:bmltHistoryDatabase:]
- -[TRIBMLTTargetingTask bmltDeployment]
- -[TRIBMLTTargetingTask dependencies]
- -[TRIBMLTTargetingTask description]
- -[TRIBMLTTargetingTask dimensions]
- -[TRIBMLTTargetingTask encodeWithCoder:]
- -[TRIBMLTTargetingTask hash]
- -[TRIBMLTTargetingTask initWithBMLTDeployment:includeDependencies:taskAttribution:triggerEvent:bmltBatchNotificationIdentifier:]
- -[TRIBMLTTargetingTask initWithCoder:]
- -[TRIBMLTTargetingTask isEqual:]
- -[TRIBMLTTargetingTask metrics]
- -[TRIBMLTTargetingTask runDequeueHandlerUsingContext:]
- -[TRIBMLTTargetingTask runEnqueueHandlerUsingContext:]
- -[TRIBMLTTargetingTask runUsingContext:withTaskQueue:]
- -[TRIBMLTTargetingTask serialize]
- -[TRIBMLTTargetingTask tags]
- -[TRIBMLTTargetingTask taskType]
- -[TRIBMLTTargetingTask trialSystemTelemetry]
- -[TRIBMLTTaskSupport .cxx_destruct]
- -[TRIBMLTTaskSupport addDimension:]
- -[TRIBMLTTaskSupport addMetric:]
- -[TRIBMLTTaskSupport bmltDeployment]
- -[TRIBMLTTaskSupport dimensions]
- -[TRIBMLTTaskSupport initWithBMLTDeployment:]
- -[TRIBMLTTaskSupport mergeTelemetry:]
- -[TRIBMLTTaskSupport metrics]
- -[TRIBMLTTaskSupport tags]
- -[TRIBMLTTaskSupport trialSystemTelemetry]
- -[TRIBMLTTaskSupportGuardedData .cxx_destruct]
- -[TRIBackgroundMLTaskDatabase .cxx_destruct]
- -[TRIBackgroundMLTaskDatabase _enumerateTaskRecordsMatchingWhereClause:bind:transaction:block:]
- -[TRIBackgroundMLTaskDatabase activateDeployment:withFactorPackSetId:targetingRuleIndex:usingTransaction:]
- -[TRIBackgroundMLTaskDatabase addBackgroundMLTaskWithTaskDeployment:pluginId:status:endDate:artifact:]
- -[TRIBackgroundMLTaskDatabase deactivateDeployment:usingTransaction:]
- -[TRIBackgroundMLTaskDatabase deactivateTaskDeployment:deactivatedFactorPackSetId:usingTransaction:]
- -[TRIBackgroundMLTaskDatabase enumerateActiveTasksNotInList:usingTransaction:withBlock:]
- -[TRIBackgroundMLTaskDatabase enumerateActiveTasksWithBlock:]
- -[TRIBackgroundMLTaskDatabase enumerateActiveTasksWithTransaction:block:]
- -[TRIBackgroundMLTaskDatabase enumerateTaskRecordsMatchingTaskId:transaction:block:]
- -[TRIBackgroundMLTaskDatabase enumerateTaskRecordsWithBlock:]
- -[TRIBackgroundMLTaskDatabase enumerateTaskRecordsWithTransaction:block:]
- -[TRIBackgroundMLTaskDatabase initWithDatabase:]
- -[TRIBackgroundMLTaskDatabase init]
- -[TRIBackgroundMLTaskDatabase readTransactionWithFailableBlock:]
- -[TRIBackgroundMLTaskDatabase removeRecordWithDeployment:]
- -[TRIBackgroundMLTaskDatabase setActiveFactorPackSetId:activeTargetingRuleIndex:forTaskDeployment:usingTransaction:]
- -[TRIBackgroundMLTaskDatabase setStatus:forTaskDeployment:usingTransaction:]
- -[TRIBackgroundMLTaskDatabase setTargetedFactorPackSetId:targetedTargetingRuleIndex:forTaskDeployment:usingTransaction:]
- -[TRIBackgroundMLTaskDatabase targetTaskDeployment:toFactorPackSetId:targetingRuleIndex:usingTransaction:]
- -[TRIBackgroundMLTaskDatabase taskRecordWithTaskDeployment:]
- -[TRIBackgroundMLTaskDatabase writeTransactionWithFailableBlock:]
- -[TRIBackgroundMLTaskHistoryDatabase .cxx_destruct]
- -[TRIBackgroundMLTaskHistoryDatabase _enumerateRecordsMatchingWhereClause:bind:block:]
- -[TRIBackgroundMLTaskHistoryDatabase addRecord:]
- -[TRIBackgroundMLTaskHistoryDatabase enumerateRecordsNewerThanDate:block:]
- -[TRIBackgroundMLTaskHistoryDatabase expireRecordsOlderThanDate:deletedCount:]
- -[TRIBackgroundMLTaskHistoryDatabase getAllAllocationStatusesForBMLTId:deploymentId:factorPackSetId:]
- -[TRIBackgroundMLTaskHistoryDatabase initWithDatabase:]
- -[TRIBackgroundMLTaskHistoryDatabase init]
- -[TRIBackgroundMLTaskHistoryDatabase readTransactionWithFailableBlock:]
- -[TRIBackgroundMLTaskHistoryDatabase writeTransactionWithFailableBlock:]
- -[TRIBackgroundMLTaskRecord .cxx_destruct]
- -[TRIBackgroundMLTaskRecord activeFactorPackSetId]
- -[TRIBackgroundMLTaskRecord activeTargetingRuleIndex]
- -[TRIBackgroundMLTaskRecord artifact]
- -[TRIBackgroundMLTaskRecord bmltDeployment]
- -[TRIBackgroundMLTaskRecord copyWithReplacementActiveFactorPackSetId:]
- -[TRIBackgroundMLTaskRecord copyWithReplacementActiveTargetingRuleIndex:]
- -[TRIBackgroundMLTaskRecord copyWithReplacementArtifact:]
- -[TRIBackgroundMLTaskRecord copyWithReplacementBmltDeployment:]
- -[TRIBackgroundMLTaskRecord copyWithReplacementEndDate:]
- -[TRIBackgroundMLTaskRecord copyWithReplacementPluginId:]
- -[TRIBackgroundMLTaskRecord copyWithReplacementStatus:]
- -[TRIBackgroundMLTaskRecord copyWithReplacementTargetedFactorPackSetId:]
- -[TRIBackgroundMLTaskRecord copyWithReplacementTargetedTargetingRuleIndex:]
- -[TRIBackgroundMLTaskRecord copyWithZone:]
- -[TRIBackgroundMLTaskRecord description]
- -[TRIBackgroundMLTaskRecord endDate]
- -[TRIBackgroundMLTaskRecord hash]
- -[TRIBackgroundMLTaskRecord initWithBmltDeployment:pluginId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:endDate:artifact:]
- -[TRIBackgroundMLTaskRecord init]
- -[TRIBackgroundMLTaskRecord isEqual:]
- -[TRIBackgroundMLTaskRecord isEqualToRecord:]
- -[TRIBackgroundMLTaskRecord pluginId]
- -[TRIBackgroundMLTaskRecord status]
- -[TRIBackgroundMLTaskRecord targetedFactorPackSetId]
- -[TRIBackgroundMLTaskRecord targetedTargetingRuleIndex]
- -[TRIBackgroundMLTaskRecord(Utils) isExpired]
- -[TRICKNativeArtifactProvider _fetchBMLTNotificationsWithCursor:options:completion:]
- -[TRICKNativeArtifactProvider fetchBMLTCatalogNotificationWithOptions:completion:]
- -[TRICKNativeArtifactProvider fetchBMLTNotificationWithDeployment:options:completion:]
- -[TRICKNativeArtifactProvider fetchBMLTNotificationsWithOptions:completion:]
- -[TRIClientBMLTArtifact .cxx_destruct]
- -[TRIClientBMLTArtifact backgroundTask]
- -[TRIClientBMLTArtifact copyWithReplacementBackgroundTask:]
- -[TRIClientBMLTArtifact copyWithReplacementDeploymentDate:]
- -[TRIClientBMLTArtifact copyWithReplacementDeploymentType:]
- -[TRIClientBMLTArtifact copyWithReplacementDownloadSize:]
- -[TRIClientBMLTArtifact copyWithReplacementPopulations:]
- -[TRIClientBMLTArtifact copyWithZone:]
- -[TRIClientBMLTArtifact deploymentDate]
- -[TRIClientBMLTArtifact deploymentType]
- -[TRIClientBMLTArtifact description]
- -[TRIClientBMLTArtifact downloadSize]
- -[TRIClientBMLTArtifact encodeWithCoder:]
- -[TRIClientBMLTArtifact hash]
- -[TRIClientBMLTArtifact initWithBackgroundTask:populations:deploymentType:deploymentDate:downloadSize:]
- -[TRIClientBMLTArtifact initWithCoder:]
- -[TRIClientBMLTArtifact init]
- -[TRIClientBMLTArtifact isEqual:]
- -[TRIClientBMLTArtifact isEqualToArtifact:]
- -[TRIClientBMLTArtifact populations]
- -[TRIClientBMLTArtifact(Utils) data]
- -[TRIClientBMLTArtifact(Utils) deployment]
- -[TRIClientBMLTArtifact(Utils) earliestStartDateForActivationIfInFuture]
- -[TRIClientBMLTCatalogArtifact .cxx_destruct]
- -[TRIClientBMLTCatalogArtifact bmltCatalog]
- -[TRIClientBMLTCatalogArtifact copyWithReplacementBmltCatalog:]
- -[TRIClientBMLTCatalogArtifact copyWithReplacementPopulation:]
- -[TRIClientBMLTCatalogArtifact copyWithZone:]
- -[TRIClientBMLTCatalogArtifact description]
- -[TRIClientBMLTCatalogArtifact encodeWithCoder:]
- -[TRIClientBMLTCatalogArtifact hash]
- -[TRIClientBMLTCatalogArtifact initWithBmltCatalog:population:]
- -[TRIClientBMLTCatalogArtifact initWithCoder:]
- -[TRIClientBMLTCatalogArtifact init]
- -[TRIClientBMLTCatalogArtifact isEqual:]
- -[TRIClientBMLTCatalogArtifact isEqualToArtifact:]
- -[TRIClientBMLTCatalogArtifact population]
- -[TRIClientRolloutArtifact initWithRollout:populations:deploymentDate:downloadSize:]
- -[TRIClientTreatmentStorage _defaultsAssetURLForFactor:]
- -[TRIClientTreatmentStorage _deleteOnDemandAssetsWithFactorNames:treatment:namespace:forRollouts:inUseAssetDeletionBehavior:]
- -[TRIClientTreatmentStorage _linkAssetWithId:treatmentId:assetStore:factor:forRollouts:]
- -[TRIClientTreatmentStorage _saveNamespacePartitionedTreatmentsForTreatment:forNamespaceNames:forRollouts:]
- -[TRIClientTreatmentStorage updateSavedTreatmentWithTreatmentId:deletingAssetsWithFactorNames:forNamespaceName:forRollouts:]
- -[TRIClientTreatmentStorage updateSavedTreatmentWithTreatmentId:deletingAssetsWithFactorNames:forNamespaceName:forRollouts:inUseAssetDeletionBehavior:]
- -[TRIClientTreatmentStorage urlForDefaultFactorsWithNamespaceName:]
- -[TRIContentDescriptorUnion bmlt]
- -[TRIContentDescriptorUnion copyWithReplacementBmlt:]
- -[TRIContentDescriptorUnion initWithType:experiment:treatment:rollout:factorPackSet:bmlt:]
- -[TRIDeactivateBMLTDeploymentGuardedData .cxx_destruct]
- -[TRIDeactivateBMLTDeploymentTask .cxx_destruct]
- -[TRIDeactivateBMLTDeploymentTask _asPersistedTask]
- -[TRIDeactivateBMLTDeploymentTask _deactivationTelemetryWithSuccess:bmltRecord:deactivatedFactorPackSetId:serverContext:]
- -[TRIDeactivateBMLTDeploymentTask addMetric:]
- -[TRIDeactivateBMLTDeploymentTask description]
- -[TRIDeactivateBMLTDeploymentTask dimensions]
- -[TRIDeactivateBMLTDeploymentTask encodeWithCoder:]
- -[TRIDeactivateBMLTDeploymentTask hash]
- -[TRIDeactivateBMLTDeploymentTask initWithBMLTDeployment:triggerEvent:bmltBatchNotificationIdentifier:]
- -[TRIDeactivateBMLTDeploymentTask initWithCoder:]
- -[TRIDeactivateBMLTDeploymentTask init]
- -[TRIDeactivateBMLTDeploymentTask isEqual:]
- -[TRIDeactivateBMLTDeploymentTask mergeTelemetry:]
- -[TRIDeactivateBMLTDeploymentTask metrics]
- -[TRIDeactivateBMLTDeploymentTask requiredCapabilities]
- -[TRIDeactivateBMLTDeploymentTask runUsingContext:withTaskQueue:]
- -[TRIDeactivateBMLTDeploymentTask serialize]
- -[TRIDeactivateBMLTDeploymentTask tags]
- -[TRIDeactivateBMLTDeploymentTask taskType]
- -[TRIDeactivateBMLTDeploymentTask trialSystemTelemetry]
- -[TRIDeactivateTreatmentTask _notifyUpdatedShadowEvaluationWithExperimentRecord:context:]
- -[TRIDeactivateTreatmentTask _purgeRolloutLayerIfNecessaryWithRecord:fromAppContainer:paths:]
- -[TRIExperimentBaseTask logAsRollout:]
- -[TRIExperimentDatabase enumerateActiveExperimentRecordsWithVisibility:block:]
- -[TRIExperimentDatabase(LowLevelNamespacesProviding) activeLowLevelNamespaces]
- -[TRIExperimentHistoryDatabase(PostLaunchLogging) _isPreviouslyRecordedStateForEvent:]
- -[TRIExperimentHistoryDatabase(PostLaunchLogging) storeExperimentEvent:wasNewEvent:]
- -[TRIExperimentRecord copyWithReplacementIsShadow:]
- -[TRIExperimentRecord initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:isManuallyTargeted:artifact:]
- -[TRIExperimentRecord isShadow]
- -[TRIFBClientTreatmentStorage _deleteOnDemandAssetsWithFactorNames:treatment:namespace:forRollouts:]
- -[TRIFBClientTreatmentStorage _linkAssetWithId:treatmentId:assetStore:factor:forRollouts:]
- -[TRIFBClientTreatmentStorage _saveNamespacePartitionedTreatmentsForTreatment:forNamespaceNames:forRollouts:]
- -[TRIFBClientTreatmentStorage updateSavedTreatmentWithTreatmentId:deletingAssetsWithFactorNames:forNamespaceName:forRollouts:]
- -[TRIFBClientTreatmentStorage urlForDefaultFactorsWithNamespaceName:]
- -[TRIFactorPackSetStorage enumerateFBFactorPacksForFactorPackSet:usingLegacyPaths:withBlock:]
- -[TRIFetchBMLTNotificationGuardedData .cxx_destruct]
- -[TRIFetchBMLTNotificationsTask .cxx_destruct]
- -[TRIFetchBMLTNotificationsTask _addDimension:]
- -[TRIFetchBMLTNotificationsTask _addMetric:]
- -[TRIFetchBMLTNotificationsTask _asPersistedTask]
- -[TRIFetchBMLTNotificationsTask _mlruntimeNotifiedTelemetryWithRecords:serverContext:]
- -[TRIFetchBMLTNotificationsTask _processBMLTArtifact:bmltsProcessed:deactivatedBMLTs:targeter:context:taskQueue:]
- -[TRIFetchBMLTNotificationsTask _processBMLTCatalogArtifact:deactivatedBMLTs:context:]
- -[TRIFetchBMLTNotificationsTask description]
- -[TRIFetchBMLTNotificationsTask dimensions]
- -[TRIFetchBMLTNotificationsTask encodeWithCoder:]
- -[TRIFetchBMLTNotificationsTask fetchSingleDeploymentWithContext:]
- -[TRIFetchBMLTNotificationsTask hash]
- -[TRIFetchBMLTNotificationsTask initWithCoder:]
- -[TRIFetchBMLTNotificationsTask initWithDeployment:taskAttribution:bmltBatchNotificationIdentifier:]
- -[TRIFetchBMLTNotificationsTask initWithTaskAttribution:]
- -[TRIFetchBMLTNotificationsTask isEqual:]
- -[TRIFetchBMLTNotificationsTask metrics]
- -[TRIFetchBMLTNotificationsTask requiredCapabilities]
- -[TRIFetchBMLTNotificationsTask retryCount]
- -[TRIFetchBMLTNotificationsTask runUsingContext:withTaskQueue:]
- -[TRIFetchBMLTNotificationsTask serialize]
- -[TRIFetchBMLTNotificationsTask setRetryCount:]
- -[TRIFetchBMLTNotificationsTask setWasDeferred:]
- -[TRIFetchBMLTNotificationsTask tags]
- -[TRIFetchBMLTNotificationsTask taskType]
- -[TRIFetchBMLTNotificationsTask trialSystemTelemetry]
- -[TRIFetchBMLTNotificationsTask wasDeferred]
- -[TRIFetchFactorPackSetTask _bmltFetchTelemetryIfApplicableWithSuccess:bmltRecord:serverContext:]
- -[TRIFetchFactorPackSetTask bmltDeployment]
- -[TRIFetchFactorPackSetTask incompatibleNamespaceNameForBMLT:namespaceDescriptorProvider:]
- -[TRIFetchFactorPackSetTask initWithFactorPackSetId:taskAttribution:bmltDeployment:]
- -[TRIInternalServiceRequestHandler _activeExperimentFactorLevelsForNamespaceName:]
- -[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:serverContext:completion:]
- -[TRIInternalServiceRequestHandler activeBMLTInformationWithPrivacyFilterPolicy:completion:]
- -[TRIInternalServiceRequestHandler activeExperimentInformationWithEnvironments:privacyFilterPolicy:completion:]
- -[TRIInternalServiceRequestHandler activeRolloutInformationWithPrivacyFilterPolicy:completion:]
- -[TRIInternalSystemServiceRequestHandler .cxx_destruct]
- -[TRIInternalSystemServiceRequestHandler _getOnDemandReferenceCountsAtGlobalPath:onDemandFactorsPerUser:error:]
- -[TRIInternalSystemServiceRequestHandler _updateOnDemandReferenceCountsForUser:atGlobalPath:addingFactors:removingFactors:newlyUnreferencedFactors:]
- -[TRIInternalSystemServiceRequestHandler addSymlinkFromAssetWithIdentifier:toPath:flockWitness:completion:]
- -[TRIInternalSystemServiceRequestHandler collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:completion:]
- -[TRIInternalSystemServiceRequestHandler fixFileProtectionForAssetStoreWithCompletion:]
- -[TRIInternalSystemServiceRequestHandler getOnDemandReferenceCountsPerUserAtGlobalPath:completion:]
- -[TRIInternalSystemServiceRequestHandler initWithEntitlementWitness:]
- -[TRIInternalSystemServiceRequestHandler logSystemCovariates]
- -[TRIInternalSystemServiceRequestHandler migrateToGlobalAssetStoreIfNeededFromLocalStore:sourceExtension:completion:]
- -[TRIInternalSystemServiceRequestHandler overwriteGlobalActiveFactorProvidersWithNamespaceMap:factorPackMap:rolloutDeploymentMap:completion:]
- -[TRIInternalSystemServiceRequestHandler referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:sourceExtension:completion:]
- -[TRIInternalSystemServiceRequestHandler removeAssetWithIdentifier:completion:]
- -[TRIInternalSystemServiceRequestHandler removeUnreferencedGlobalFactorPacksWithCompletion:]
- -[TRIInternalSystemServiceRequestHandler saveAssetWithIdentifier:sourcePath:flockWitness:removeSourceOnFailure:sourceExtension:completion:]
- -[TRIInternalSystemServiceRequestHandler saveFactorPackForUserId:toGlobalPath:fromTemporaryPath:factors:sourceExtension:completion:]
- -[TRIInternalSystemServiceRequestHandler updateFactorPackForUserId:atGlobalPath:deletingFactors:completion:]
- -[TRIInternalSystemServiceRequestHandler updateFactorPackForUserId:atGlobalPath:populatingFactors:completion:]
- -[TRIMLRuntimeEvaluationHistoryDatabase .cxx_destruct]
- -[TRIMLRuntimeEvaluationHistoryDatabase _enumerateRecordsMatchingWhereClause:bind:block:]
- -[TRIMLRuntimeEvaluationHistoryDatabase addRecord:usingTransaction:]
- -[TRIMLRuntimeEvaluationHistoryDatabase enumerateRecordsNewerThanDate:block:]
- -[TRIMLRuntimeEvaluationHistoryDatabase expireRecordsOlderThanDate:deletedCount:]
- -[TRIMLRuntimeEvaluationHistoryDatabase initWithDatabase:]
- -[TRIMLRuntimeEvaluationHistoryDatabase init]
- -[TRIMLRuntimeEvaluationHistoryDatabase readTransactionWithFailableBlock:]
- -[TRIMLRuntimeEvaluationHistoryDatabase writeTransactionWithFailableBlock:]
- -[TRIMaintenanceTask _handleExpiredBMLTsWithBMLTDatabase:nextTasks:]
- -[TRIMakeDefaultTask .cxx_destruct]
- -[TRIMakeDefaultTask _asPersistedTask]
- -[TRIMakeDefaultTask _nextTasksForRunStatus:]
- -[TRIMakeDefaultTask dependencies]
- -[TRIMakeDefaultTask description]
- -[TRIMakeDefaultTask encodeWithCoder:]
- -[TRIMakeDefaultTask initWithCoder:]
- -[TRIMakeDefaultTask initWithExperiment:treatmentId:taskAttributing:capabilityModifier:]
- -[TRIMakeDefaultTask makeDefaultForNamespace:experiment:context:]
- -[TRIMakeDefaultTask metrics]
- -[TRIMakeDefaultTask requiredCapabilities]
- -[TRIMakeDefaultTask retryCount]
- -[TRIMakeDefaultTask runTaskUsingContext:experiment:]
- -[TRIMakeDefaultTask serialize]
- -[TRIMakeDefaultTask setRetryCount:]
- -[TRIMakeDefaultTask setTestingIgnoreDependencies:]
- -[TRIMakeDefaultTask setWasDeferred:]
- -[TRIMakeDefaultTask taskType]
- -[TRIMakeDefaultTask testingIgnoreDependencies]
- -[TRIMakeDefaultTask wasDeferred]
- -[TRINamespaceResolverStorage _pathForBMLTDeployment:]
- -[TRINamespaceResolverStorage _removeUnreferencedBMLTDeploymentsWithRefStore:parentDir:removedCount:]
- -[TRINamespaceResolverStorage _removeUnreferencedBMLTDeploymentsWithRefStore:topLevelDir:removedCount:]
- -[TRINamespaceResolverStorage parentDirForBMLTDeployments]
- -[TRINamespaceResolverStorage pathForBMLTDeployment:]
- -[TRINamespaceResolverStorage pathForTargetedFactorPackSetWithTaskDeployment:]
- -[TRINamespaceResolverStorage removeUnreferencedBMLTDeploymentsWithServerContext:removedCount:]
- -[TRINamespaceResolverStorage rewriteBMLTDeployment:targetedFactorPackSetId:]
- -[TRIPostUpgradeCleanupTask _activeBMLTIsCompatible:upgradeNCVs:downloadNCVs:]
- -[TRIPostUpgradeCleanupTask _migrateProtobufFactorPacksToFlatbuffersUsingPaths:]
- -[TRIPostUpgradeCleanupTask _saveProtoToFlatbufferFormatWithPaths:namespaceUrl:]
- -[TRIPostUpgradeCleanupTask _validateBMLTNamespaceNCVs:downloadNCVs:context:]
- -[TRIPostUpgradeCleanupTask _validateDynamicNamespaceRolloutsWithDatabase:usingPaths:]
- -[TRIPostUpgradeCleanupTask _validateRolloutDescriptorsWithNamespaceCompatibilityVersions:usingPaths:]
- -[TRIRolloutDatabase enumerateActiveRecordsWithVisibility:usingTransaction:block:]
- -[TRIRolloutRecord copyWithReplacementIsShadow:]
- -[TRIRolloutRecord initWithDeployment:rampId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:namespaces:isShadow:artifact:]
- -[TRIRolloutRecord isShadow]
- -[TRIServerContext bmltDatabase]
- -[TRIServerContext bmltHistoryDatabase]
- -[TRIServerContext evaluationHistoryDatabase]
- -[TRITargetingTask _isRolloutV1For1PWithExperimentRecord:context:]
- -[TRIUrgentRollbackScheduler _validRollbackDeploymentsForRollbackExperiment:deploymentIds:]
- -[TRIXPCInternalServiceClient _performSyncXpcWithError:block:]
- -[TRIXPCInternalServiceClient init]
- -[TRIXPCInternalServiceListener initWithServerContextPromise:]
- -[TRIXPCInternalSystemServiceListener .cxx_destruct]
- -[TRIXPCInternalSystemServiceListener init]
- -[TRIXPCInternalSystemServiceListener listener:shouldAcceptNewConnection:]
- -[TRIXPCInternalSystemServiceWrapper initWithUnderlyingHandler:]
- -[TRIXPCNamespaceManagementServiceListener initWithServerContextPromise:]
- -[TRIXPCStatusRequestHandler activeEvaluationsForBMLTWithCompletion:]
- -[TRIXPCStatusRequestHandler activeEvaluationsForMLRuntimeWithCompletion:]
- -[TRIXPCStatusRequestHandler bmltRecordsWithCompletion:]
- -[TRIXPCStatusRequestHandler evaluationHistoryRecordsForMLRuntimeWithLimit:newerThanDate:completion:]
- -[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:privacyFilterPolicy:deploymentEnvironment:completion:]
- -[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:completion:]
- -[TRIXPCStatusRequestHandler rolloutAllocationStatusWithPrivacyFilterPolicy:completion:]
- -[TRIXPCStatusServiceListener initWithPromise:]
- GCC_except_table50
- GCC_except_table77
- GCC_except_table98
- OBJC_IVAR_$_TRIBMLTTaskSupportGuardedData.dimensions
- OBJC_IVAR_$_TRIBMLTTaskSupportGuardedData.metrics
- OBJC_IVAR_$_TRIBMLTTaskSupportGuardedData.trialSystemTelemetry
- OBJC_IVAR_$_TRIDeactivateBMLTDeploymentGuardedData.metrics
- OBJC_IVAR_$_TRIDeactivateBMLTDeploymentGuardedData.trialSystemTelemetry
- OBJC_IVAR_$_TRIExperimentBaseTaskGuardedData.logAsRollout
- OBJC_IVAR_$_TRIFetchBMLTNotificationGuardedData.dimensions
- OBJC_IVAR_$_TRIFetchBMLTNotificationGuardedData.metrics
- _LighthouseBitacoraFrameworkLibrary
- _LighthouseBitacoraFrameworkLibraryCore.frameworkLibrary
- _OBJC_CLASS_$_TRIActivateTargetedBMLTDeploymentPersistedTask
- _OBJC_CLASS_$_TRIActivateTargetedBMLTDeploymentTask
- _OBJC_CLASS_$_TRIActiveLowLevelExperiment
- _OBJC_CLASS_$_TRIActiveLowLevelExperimentsReader
- _OBJC_CLASS_$_TRIActiveLowLevelFactorStringBuilder
- _OBJC_CLASS_$_TRIActiveLowLevelFactorsPublisher
- _OBJC_CLASS_$_TRIActiveLowLevelFactorsWriter
- _OBJC_CLASS_$_TRIBMLTActiveEvaluationTuple
- _OBJC_CLASS_$_TRIBMLTDeployment
- _OBJC_CLASS_$_TRIBMLTDeploymentRefStore
- _OBJC_CLASS_$_TRIBMLTFactorsState
- _OBJC_CLASS_$_TRIBMLTTargeter
- _OBJC_CLASS_$_TRIBMLTTargetingPersistedTask
- _OBJC_CLASS_$_TRIBMLTTargetingTask
- _OBJC_CLASS_$_TRIBMLTTaskSupport
- _OBJC_CLASS_$_TRIBMLTTaskSupportGuardedData
- _OBJC_CLASS_$_TRIBackgroundMLTaskDatabase
- _OBJC_CLASS_$_TRIBackgroundMLTaskHistoryDatabase
- _OBJC_CLASS_$_TRIBackgroundMLTaskHistoryRecord
- _OBJC_CLASS_$_TRIBackgroundMLTaskRecord
- _OBJC_CLASS_$_TRIClientBMLTArtifact
- _OBJC_CLASS_$_TRIClientBMLTCatalogArtifact
- _OBJC_CLASS_$_TRIClientBackgroundMLTask
- _OBJC_CLASS_$_TRIClientBmltCatalog
- _OBJC_CLASS_$_TRIDeactivateBMLTDeploymentGuardedData
- _OBJC_CLASS_$_TRIDeactivateBMLTDeploymentPersistedTask
- _OBJC_CLASS_$_TRIDeactivateBMLTDeploymentTask
- _OBJC_CLASS_$_TRIEvaluationStatus
- _OBJC_CLASS_$_TRIExperimentFactorsState
- _OBJC_CLASS_$_TRIFactorLevel
- _OBJC_CLASS_$_TRIFetchBMLTNotificationGuardedData
- _OBJC_CLASS_$_TRIFetchBMLTNotificationsPersistedTask
- _OBJC_CLASS_$_TRIFetchBMLTNotificationsTask
- _OBJC_CLASS_$_TRIInternalSystemServiceRequestHandler
- _OBJC_CLASS_$_TRIKnownLowLevelFactorsReader
- _OBJC_CLASS_$_TRILighthouseBitacoraHandler
- _OBJC_CLASS_$_TRILogNamespace
- _OBJC_CLASS_$_TRIMLRuntimeActiveEvaluationTuple
- _OBJC_CLASS_$_TRIMLRuntimeEvaluation
- _OBJC_CLASS_$_TRIMLRuntimeEvaluationHistoryDatabase
- _OBJC_CLASS_$_TRIMLRuntimeEvaluationHistoryRecord
- _OBJC_CLASS_$_TRIMakeDefaultPersistedTask
- _OBJC_CLASS_$_TRIMakeDefaultTask
- _OBJC_CLASS_$_TRINamespaceLogPolicy
- _OBJC_CLASS_$_TRIPartialBMLTRecord
- _OBJC_CLASS_$_TRIPersistedClientBMLTArtifact
- _OBJC_CLASS_$_TRIRolloutFactorsState
- _OBJC_CLASS_$_TRITripersistedClientBmltartifactRoot
- _OBJC_CLASS_$_TRIXPCInternalSystemServiceListener
- _OBJC_CLASS_$_TRIXPCInternalSystemServiceWrapper
- _OBJC_IVAR_$_TRIActiveLowLevelExperiment._factorLevelStrings
- _OBJC_IVAR_$_TRIActiveLowLevelExperiment._targetedBundleIds
- _OBJC_IVAR_$_TRIActiveLowLevelExperimentsReader._factorLevelsRetriever
- _OBJC_IVAR_$_TRIActiveLowLevelExperimentsReader._namespacesProvider
- _OBJC_IVAR_$_TRIActiveLowLevelFactorsPublisher._namespacesProvider
- _OBJC_IVAR_$_TRIActiveLowLevelFactorsPublisher._retriever
- _OBJC_IVAR_$_TRIActiveLowLevelFactorsPublisher._writer
- _OBJC_IVAR_$_TRIActiveLowLevelFactorsWriter._paths
- _OBJC_IVAR_$_TRIBMLTDeploymentRefStore._context
- _OBJC_IVAR_$_TRIBMLTTargeter._db
- _OBJC_IVAR_$_TRIBMLTTargeter._systemCovariateProvider
- _OBJC_IVAR_$_TRIBMLTTargeter._userCovariateProvider
- _OBJC_IVAR_$_TRIBMLTTaskSupport._bmltDeployment
- _OBJC_IVAR_$_TRIBMLTTaskSupport._lock
- _OBJC_IVAR_$_TRIBackgroundMLTaskDatabase._db
- _OBJC_IVAR_$_TRIBackgroundMLTaskHistoryDatabase._db
- _OBJC_IVAR_$_TRIBackgroundMLTaskRecord._activeFactorPackSetId
- _OBJC_IVAR_$_TRIBackgroundMLTaskRecord._activeTargetingRuleIndex
- _OBJC_IVAR_$_TRIBackgroundMLTaskRecord._artifact
- _OBJC_IVAR_$_TRIBackgroundMLTaskRecord._bmltDeployment
- _OBJC_IVAR_$_TRIBackgroundMLTaskRecord._endDate
- _OBJC_IVAR_$_TRIBackgroundMLTaskRecord._pluginId
- _OBJC_IVAR_$_TRIBackgroundMLTaskRecord._status
- _OBJC_IVAR_$_TRIBackgroundMLTaskRecord._targetedFactorPackSetId
- _OBJC_IVAR_$_TRIBackgroundMLTaskRecord._targetedTargetingRuleIndex
- _OBJC_IVAR_$_TRIClientBMLTArtifact._backgroundTask
- _OBJC_IVAR_$_TRIClientBMLTArtifact._deploymentDate
- _OBJC_IVAR_$_TRIClientBMLTArtifact._deploymentType
- _OBJC_IVAR_$_TRIClientBMLTArtifact._downloadSize
- _OBJC_IVAR_$_TRIClientBMLTArtifact._populations
- _OBJC_IVAR_$_TRIClientBMLTCatalogArtifact._bmltCatalog
- _OBJC_IVAR_$_TRIClientBMLTCatalogArtifact._population
- _OBJC_IVAR_$_TRIContentDescriptorUnion._bmlt
- _OBJC_IVAR_$_TRIExperimentRecord._isShadow
- _OBJC_IVAR_$_TRIFetchBMLTNotificationsTask.retryCount
- _OBJC_IVAR_$_TRIInternalSystemServiceRequestHandler._entitlementWitness
- _OBJC_IVAR_$_TRIInternalSystemServiceRequestHandler._operator
- _OBJC_IVAR_$_TRIInternalSystemServiceRequestHandler._storageManagement
- _OBJC_IVAR_$_TRIInternalSystemServiceRequestHandler._store
- _OBJC_IVAR_$_TRIMLRuntimeEvaluationHistoryDatabase._db
- _OBJC_IVAR_$_TRIMakeDefaultTask._testingIgnoreDependencies
- _OBJC_IVAR_$_TRIMakeDefaultTask.retryCount
- _OBJC_IVAR_$_TRIMakeDefaultTask.wasDeferred
- _OBJC_IVAR_$_TRIRolloutRecord._isShadow
- _OBJC_IVAR_$_TRIServerContext._bmltDatabase
- _OBJC_IVAR_$_TRIServerContext._bmltHistoryDatabase
- _OBJC_IVAR_$_TRIServerContext._evaluationHistoryDatabase
- _OBJC_IVAR_$_TRIXPCInternalSystemServiceListener._interface
- _OBJC_IVAR_$_TRIXPCInternalSystemServiceListener._wrapper
- _OBJC_METACLASS_$_TRIActivateTargetedBMLTDeploymentPersistedTask
- _OBJC_METACLASS_$_TRIActivateTargetedBMLTDeploymentTask
- _OBJC_METACLASS_$_TRIActiveLowLevelExperiment
- _OBJC_METACLASS_$_TRIActiveLowLevelExperimentsReader
- _OBJC_METACLASS_$_TRIActiveLowLevelFactorStringBuilder
- _OBJC_METACLASS_$_TRIActiveLowLevelFactorsPublisher
- _OBJC_METACLASS_$_TRIActiveLowLevelFactorsWriter
- _OBJC_METACLASS_$_TRIBMLTDeploymentRefStore
- _OBJC_METACLASS_$_TRIBMLTTargeter
- _OBJC_METACLASS_$_TRIBMLTTargetingPersistedTask
- _OBJC_METACLASS_$_TRIBMLTTargetingTask
- _OBJC_METACLASS_$_TRIBMLTTaskSupport
- _OBJC_METACLASS_$_TRIBMLTTaskSupportGuardedData
- _OBJC_METACLASS_$_TRIBackgroundMLTaskDatabase
- _OBJC_METACLASS_$_TRIBackgroundMLTaskHistoryDatabase
- _OBJC_METACLASS_$_TRIBackgroundMLTaskRecord
- _OBJC_METACLASS_$_TRIClientBMLTArtifact
- _OBJC_METACLASS_$_TRIClientBMLTCatalogArtifact
- _OBJC_METACLASS_$_TRIDeactivateBMLTDeploymentGuardedData
- _OBJC_METACLASS_$_TRIDeactivateBMLTDeploymentPersistedTask
- _OBJC_METACLASS_$_TRIDeactivateBMLTDeploymentTask
- _OBJC_METACLASS_$_TRIFetchBMLTNotificationGuardedData
- _OBJC_METACLASS_$_TRIFetchBMLTNotificationsPersistedTask
- _OBJC_METACLASS_$_TRIFetchBMLTNotificationsTask
- _OBJC_METACLASS_$_TRIInternalSystemServiceRequestHandler
- _OBJC_METACLASS_$_TRIKnownLowLevelFactorsReader
- _OBJC_METACLASS_$_TRILighthouseBitacoraHandler
- _OBJC_METACLASS_$_TRIMLRuntimeEvaluationHistoryDatabase
- _OBJC_METACLASS_$_TRIMakeDefaultPersistedTask
- _OBJC_METACLASS_$_TRIMakeDefaultTask
- _OBJC_METACLASS_$_TRIPersistedClientBMLTArtifact
- _OBJC_METACLASS_$_TRITripersistedClientBmltartifactRoot
- _OBJC_METACLASS_$_TRIXPCInternalSystemServiceListener
- _OBJC_METACLASS_$_TRIXPCInternalSystemServiceWrapper
- _TRIBMLTTargetingPersistedTask_TriggerEvent_EnumDescriptor
- _TRIBMLTTargetingPersistedTask_TriggerEvent_EnumDescriptor.descriptor
- _TRIBMLTTargetingPersistedTask_TriggerEvent_EnumDescriptor.values
- _TRIBMLTTargetingPersistedTask_TriggerEvent_IsValidValue
- _TRICloudKitRecordBMLTCatalogNotification
- _TRICloudKitRecordBMLTCatalogNotification_CatalogDefinition
- _TRICloudKitRecordBMLTCatalogNotification_CatalogDefinitionSignature
- _TRICloudKitRecordBMLTCatalogNotification_Population
- _TRICloudKitRecordBMLTCatalogNotification_PublicCertificate
- _TRICloudKitRecordBMLTCatalogNotification_Status
- _TRICloudKitRecordBMLTNotification
- _TRICloudKitRecordBMLTNotification_BackgroundMLTaskId
- _TRICloudKitRecordBMLTNotification_DeploymentDate
- _TRICloudKitRecordBMLTNotification_DeploymentId
- _TRICloudKitRecordBMLTNotification_DeploymentType
- _TRICloudKitRecordBMLTNotification_NamespaceName
- _TRICloudKitRecordBMLTNotification_Populations
- _TRICloudKitRecordBMLTNotification_PublicCertificate
- _TRICloudKitRecordBMLTNotification_Status
- _TRICloudKitRecordBMLTNotification_TaskDefinition
- _TRICloudKitRecordBMLTNotification_TaskDefinitionSignature
- _TRIDeactivateBMLTDeploymentPersistedTask_TriggerEvent_EnumDescriptor
- _TRIDeactivateBMLTDeploymentPersistedTask_TriggerEvent_EnumDescriptor.descriptor
- _TRIDeactivateBMLTDeploymentPersistedTask_TriggerEvent_EnumDescriptor.values
- _TRIDeactivateBMLTDeploymentPersistedTask_TriggerEvent_IsValidValue
- _TRILoggedNamespaceName
- _TRIMetricName_BMLTEnumerated
- _TRIMetricName_BMLTNotification
- __OBJC_$_CATEGORY_CLASS_METHODS_TRISystemConfiguration_$_Server
- __OBJC_$_CATEGORY_CLASS_METHODS_TRISystemDimensions_$_ServerFactory
- __OBJC_$_CATEGORY_INSTANCE_METHODS_TRIBMLTDeployment_$_Utils
- __OBJC_$_CATEGORY_INSTANCE_METHODS_TRIClient_$_Telemetry
- __OBJC_$_CATEGORY_INSTANCE_METHODS_TRISystemConfiguration_$_Server
- __OBJC_$_CATEGORY_TRIBMLTDeployment_$_Utils
- __OBJC_$_CATEGORY_TRIClient_$_Telemetry
- __OBJC_$_CATEGORY_TRISystemConfiguration_$_Server
- __OBJC_$_CLASS_METHODS_TRIActivateTargetedBMLTDeploymentPersistedTask
- __OBJC_$_CLASS_METHODS_TRIActivateTargetedBMLTDeploymentTask
- __OBJC_$_CLASS_METHODS_TRIActiveLowLevelExperiment
- __OBJC_$_CLASS_METHODS_TRIActiveLowLevelFactorStringBuilder
- __OBJC_$_CLASS_METHODS_TRIBMLTTargeter
- __OBJC_$_CLASS_METHODS_TRIBMLTTargetingPersistedTask
- __OBJC_$_CLASS_METHODS_TRIBMLTTargetingTask
- __OBJC_$_CLASS_METHODS_TRIBackgroundMLTaskRecord
- __OBJC_$_CLASS_METHODS_TRIClientBMLTArtifact(Utils|CloudKit)
- __OBJC_$_CLASS_METHODS_TRIClientBMLTCatalogArtifact(CloudKit)
- __OBJC_$_CLASS_METHODS_TRIClientExperimentArtifact(FactorPacks|CloudKit|Counterfactuals)
- __OBJC_$_CLASS_METHODS_TRIClientRolloutArtifact(CloudKit|Utils)
- __OBJC_$_CLASS_METHODS_TRIDeactivateBMLTDeploymentPersistedTask
- __OBJC_$_CLASS_METHODS_TRIDeactivateBMLTDeploymentTask
- __OBJC_$_CLASS_METHODS_TRIFetchBMLTNotificationsPersistedTask
- __OBJC_$_CLASS_METHODS_TRIFetchBMLTNotificationsTask
- __OBJC_$_CLASS_METHODS_TRIKnownLowLevelFactorsReader
- __OBJC_$_CLASS_METHODS_TRILighthouseBitacoraHandler
- __OBJC_$_CLASS_METHODS_TRIMakeDefaultPersistedTask
- __OBJC_$_CLASS_METHODS_TRIMakeDefaultTask
- __OBJC_$_CLASS_METHODS_TRIPersistedClientBMLTArtifact
- __OBJC_$_CLASS_METHODS_TRITaskAttributionInternalInsecure(FirstParty|Persistance)
- __OBJC_$_CLASS_PROP_LIST_TRIActivateTargetedBMLTDeploymentTask
- __OBJC_$_CLASS_PROP_LIST_TRIActiveLowLevelExperiment
- __OBJC_$_CLASS_PROP_LIST_TRIBMLTTargetingTask
- __OBJC_$_CLASS_PROP_LIST_TRIClientBMLTArtifact
- __OBJC_$_CLASS_PROP_LIST_TRIClientBMLTCatalogArtifact
- __OBJC_$_CLASS_PROP_LIST_TRIDeactivateBMLTDeploymentTask
- __OBJC_$_CLASS_PROP_LIST_TRIFetchBMLTNotificationsTask
- __OBJC_$_CLASS_PROP_LIST_TRIMakeDefaultTask
- __OBJC_$_INSTANCE_METHODS_NSDictionary(TRI|TRIFunctions|TRIDAG|TRICloudKit)
- __OBJC_$_INSTANCE_METHODS_TRIActivateTargetedBMLTDeploymentTask
- __OBJC_$_INSTANCE_METHODS_TRIActiveLowLevelExperiment
- __OBJC_$_INSTANCE_METHODS_TRIActiveLowLevelExperimentsReader
- __OBJC_$_INSTANCE_METHODS_TRIActiveLowLevelFactorsPublisher
- __OBJC_$_INSTANCE_METHODS_TRIActiveLowLevelFactorsWriter
- __OBJC_$_INSTANCE_METHODS_TRIBMLTDeploymentRefStore
- __OBJC_$_INSTANCE_METHODS_TRIBMLTTargeter
- __OBJC_$_INSTANCE_METHODS_TRIBMLTTargetingTask
- __OBJC_$_INSTANCE_METHODS_TRIBMLTTaskSupport
- __OBJC_$_INSTANCE_METHODS_TRIBMLTTaskSupportGuardedData
- __OBJC_$_INSTANCE_METHODS_TRIBackgroundMLTaskDatabase
- __OBJC_$_INSTANCE_METHODS_TRIBackgroundMLTaskHistoryDatabase
- __OBJC_$_INSTANCE_METHODS_TRIBackgroundMLTaskRecord(Utils)
- __OBJC_$_INSTANCE_METHODS_TRIClientBMLTArtifact(Utils|CloudKit)
- __OBJC_$_INSTANCE_METHODS_TRIClientBMLTCatalogArtifact
- __OBJC_$_INSTANCE_METHODS_TRIClientExperimentArtifact(FactorPacks|CloudKit|Counterfactuals)
- __OBJC_$_INSTANCE_METHODS_TRIClientRolloutArtifact(CloudKit|Utils)
- __OBJC_$_INSTANCE_METHODS_TRIDeactivateBMLTDeploymentGuardedData
- __OBJC_$_INSTANCE_METHODS_TRIDeactivateBMLTDeploymentTask
- __OBJC_$_INSTANCE_METHODS_TRIExperimentDatabase(CountProviding|LowLevelNamespacesProviding)
- __OBJC_$_INSTANCE_METHODS_TRIExperimentHistoryDatabase(PreviousStateProviding|PostLaunchLogging)
- __OBJC_$_INSTANCE_METHODS_TRIExperimentRecord(VersionedNamespaces|Counterfactuals|Utils)
- __OBJC_$_INSTANCE_METHODS_TRIFetchBMLTNotificationGuardedData
- __OBJC_$_INSTANCE_METHODS_TRIFetchBMLTNotificationsTask
- __OBJC_$_INSTANCE_METHODS_TRIInternalSystemServiceRequestHandler
- __OBJC_$_INSTANCE_METHODS_TRIMLRuntimeEvaluationHistoryDatabase
- __OBJC_$_INSTANCE_METHODS_TRIMakeDefaultTask
- __OBJC_$_INSTANCE_METHODS_TRITaskAttributionInternalInsecure(FirstParty|Persistance)
- __OBJC_$_INSTANCE_METHODS_TRIXPCInternalSystemServiceListener
- __OBJC_$_INSTANCE_METHODS_TRIXPCInternalSystemServiceWrapper
- __OBJC_$_INSTANCE_VARIABLES_TRIActivateTargetedBMLTDeploymentTask
- __OBJC_$_INSTANCE_VARIABLES_TRIActiveLowLevelExperiment
- __OBJC_$_INSTANCE_VARIABLES_TRIActiveLowLevelExperimentsReader
- __OBJC_$_INSTANCE_VARIABLES_TRIActiveLowLevelFactorsPublisher
- __OBJC_$_INSTANCE_VARIABLES_TRIActiveLowLevelFactorsWriter
- __OBJC_$_INSTANCE_VARIABLES_TRIBMLTDeploymentRefStore
- __OBJC_$_INSTANCE_VARIABLES_TRIBMLTTargeter
- __OBJC_$_INSTANCE_VARIABLES_TRIBMLTTargetingTask
- __OBJC_$_INSTANCE_VARIABLES_TRIBMLTTaskSupport
- __OBJC_$_INSTANCE_VARIABLES_TRIBMLTTaskSupportGuardedData
- __OBJC_$_INSTANCE_VARIABLES_TRIBackgroundMLTaskDatabase
- __OBJC_$_INSTANCE_VARIABLES_TRIBackgroundMLTaskHistoryDatabase
- __OBJC_$_INSTANCE_VARIABLES_TRIBackgroundMLTaskRecord
- __OBJC_$_INSTANCE_VARIABLES_TRIClientBMLTArtifact
- __OBJC_$_INSTANCE_VARIABLES_TRIClientBMLTCatalogArtifact
- __OBJC_$_INSTANCE_VARIABLES_TRIDeactivateBMLTDeploymentGuardedData
- __OBJC_$_INSTANCE_VARIABLES_TRIDeactivateBMLTDeploymentTask
- __OBJC_$_INSTANCE_VARIABLES_TRIFetchBMLTNotificationGuardedData
- __OBJC_$_INSTANCE_VARIABLES_TRIFetchBMLTNotificationsTask
- __OBJC_$_INSTANCE_VARIABLES_TRIInternalSystemServiceRequestHandler
- __OBJC_$_INSTANCE_VARIABLES_TRIMLRuntimeEvaluationHistoryDatabase
- __OBJC_$_INSTANCE_VARIABLES_TRIMakeDefaultTask
- __OBJC_$_INSTANCE_VARIABLES_TRIXPCInternalSystemServiceListener
- __OBJC_$_PROP_LIST_TRIActivateTargetedBMLTDeploymentPersistedTask
- __OBJC_$_PROP_LIST_TRIActivateTargetedBMLTDeploymentTask
- __OBJC_$_PROP_LIST_TRIActiveLowLevelExperiment
- __OBJC_$_PROP_LIST_TRIBMLTDeployment_$_Utils
- __OBJC_$_PROP_LIST_TRIBMLTTargeter
- __OBJC_$_PROP_LIST_TRIBMLTTargetingPersistedTask
- __OBJC_$_PROP_LIST_TRIBMLTTargetingTask
- __OBJC_$_PROP_LIST_TRIBMLTTaskSupport
- __OBJC_$_PROP_LIST_TRIBackgroundMLTaskRecord
- __OBJC_$_PROP_LIST_TRIClientBMLTCatalogArtifact
- __OBJC_$_PROP_LIST_TRIDeactivateBMLTDeploymentPersistedTask
- __OBJC_$_PROP_LIST_TRIDeactivateBMLTDeploymentTask
- __OBJC_$_PROP_LIST_TRIFetchBMLTNotificationsPersistedTask
- __OBJC_$_PROP_LIST_TRIFetchBMLTNotificationsTask
- __OBJC_$_PROP_LIST_TRIMakeDefaultPersistedTask
- __OBJC_$_PROP_LIST_TRIMakeDefaultTask
- __OBJC_$_PROP_LIST_TRIPersistedClientBMLTArtifact
- __OBJC_$_PROP_LIST_TRIXPCInternalSystemServiceListener
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_TRIActiveLowLevelNamespacesProviding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_TRIXPCInternalSystemServiceProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_TRIActiveLowLevelNamespacesProviding
- __OBJC_$_PROTOCOL_METHOD_TYPES_TRIXPCInternalSystemServiceProtocol
- __OBJC_$_PROTOCOL_REFS_TRIActiveLowLevelNamespacesProviding
- __OBJC_CLASS_PROTOCOLS_$_TRIActivateTargetedBMLTDeploymentTask
- __OBJC_CLASS_PROTOCOLS_$_TRIActiveLowLevelExperiment
- __OBJC_CLASS_PROTOCOLS_$_TRIBMLTDeploymentRefStore
- __OBJC_CLASS_PROTOCOLS_$_TRIBMLTTargetingTask
- __OBJC_CLASS_PROTOCOLS_$_TRIBMLTTaskSupport
- __OBJC_CLASS_PROTOCOLS_$_TRIBackgroundMLTaskRecord
- __OBJC_CLASS_PROTOCOLS_$_TRIClientBMLTArtifact
- __OBJC_CLASS_PROTOCOLS_$_TRIClientBMLTCatalogArtifact
- __OBJC_CLASS_PROTOCOLS_$_TRIDeactivateBMLTDeploymentTask
- __OBJC_CLASS_PROTOCOLS_$_TRIExperimentDatabase(CountProviding|LowLevelNamespacesProviding)
- __OBJC_CLASS_PROTOCOLS_$_TRIExperimentHistoryDatabase(PreviousStateProviding|PostLaunchLogging)
- __OBJC_CLASS_PROTOCOLS_$_TRIFetchBMLTNotificationsTask
- __OBJC_CLASS_PROTOCOLS_$_TRIInternalSystemServiceRequestHandler
- __OBJC_CLASS_PROTOCOLS_$_TRIMakeDefaultTask
- __OBJC_CLASS_PROTOCOLS_$_TRITaskAttributionInternalInsecure(FirstParty|Persistance)
- __OBJC_CLASS_PROTOCOLS_$_TRIXPCInternalSystemServiceListener
- __OBJC_CLASS_PROTOCOLS_$_TRIXPCInternalSystemServiceWrapper
- __OBJC_CLASS_RO_$_TRIActivateTargetedBMLTDeploymentPersistedTask
- __OBJC_CLASS_RO_$_TRIActivateTargetedBMLTDeploymentTask
- __OBJC_CLASS_RO_$_TRIActiveLowLevelExperiment
- __OBJC_CLASS_RO_$_TRIActiveLowLevelExperimentsReader
- __OBJC_CLASS_RO_$_TRIActiveLowLevelFactorStringBuilder
- __OBJC_CLASS_RO_$_TRIActiveLowLevelFactorsPublisher
- __OBJC_CLASS_RO_$_TRIActiveLowLevelFactorsWriter
- __OBJC_CLASS_RO_$_TRIBMLTDeploymentRefStore
- __OBJC_CLASS_RO_$_TRIBMLTTargeter
- __OBJC_CLASS_RO_$_TRIBMLTTargetingPersistedTask
- __OBJC_CLASS_RO_$_TRIBMLTTargetingTask
- __OBJC_CLASS_RO_$_TRIBMLTTaskSupport
- __OBJC_CLASS_RO_$_TRIBMLTTaskSupportGuardedData
- __OBJC_CLASS_RO_$_TRIBackgroundMLTaskDatabase
- __OBJC_CLASS_RO_$_TRIBackgroundMLTaskHistoryDatabase
- __OBJC_CLASS_RO_$_TRIBackgroundMLTaskRecord
- __OBJC_CLASS_RO_$_TRIClientBMLTArtifact
- __OBJC_CLASS_RO_$_TRIClientBMLTCatalogArtifact
- __OBJC_CLASS_RO_$_TRIDeactivateBMLTDeploymentGuardedData
- __OBJC_CLASS_RO_$_TRIDeactivateBMLTDeploymentPersistedTask
- __OBJC_CLASS_RO_$_TRIDeactivateBMLTDeploymentTask
- __OBJC_CLASS_RO_$_TRIFetchBMLTNotificationGuardedData
- __OBJC_CLASS_RO_$_TRIFetchBMLTNotificationsPersistedTask
- __OBJC_CLASS_RO_$_TRIFetchBMLTNotificationsTask
- __OBJC_CLASS_RO_$_TRIInternalSystemServiceRequestHandler
- __OBJC_CLASS_RO_$_TRIKnownLowLevelFactorsReader
- __OBJC_CLASS_RO_$_TRILighthouseBitacoraHandler
- __OBJC_CLASS_RO_$_TRIMLRuntimeEvaluationHistoryDatabase
- __OBJC_CLASS_RO_$_TRIMakeDefaultPersistedTask
- __OBJC_CLASS_RO_$_TRIMakeDefaultTask
- __OBJC_CLASS_RO_$_TRIPersistedClientBMLTArtifact
- __OBJC_CLASS_RO_$_TRITripersistedClientBmltartifactRoot
- __OBJC_CLASS_RO_$_TRIXPCInternalSystemServiceListener
- __OBJC_CLASS_RO_$_TRIXPCInternalSystemServiceWrapper
- __OBJC_LABEL_PROTOCOL_$_TRIActiveLowLevelNamespacesProviding
- __OBJC_LABEL_PROTOCOL_$_TRIXPCInternalSystemServiceProtocol
- __OBJC_METACLASS_RO_$_TRIActivateTargetedBMLTDeploymentPersistedTask
- __OBJC_METACLASS_RO_$_TRIActivateTargetedBMLTDeploymentTask
- __OBJC_METACLASS_RO_$_TRIActiveLowLevelExperiment
- __OBJC_METACLASS_RO_$_TRIActiveLowLevelExperimentsReader
- __OBJC_METACLASS_RO_$_TRIActiveLowLevelFactorStringBuilder
- __OBJC_METACLASS_RO_$_TRIActiveLowLevelFactorsPublisher
- __OBJC_METACLASS_RO_$_TRIActiveLowLevelFactorsWriter
- __OBJC_METACLASS_RO_$_TRIBMLTDeploymentRefStore
- __OBJC_METACLASS_RO_$_TRIBMLTTargeter
- __OBJC_METACLASS_RO_$_TRIBMLTTargetingPersistedTask
- __OBJC_METACLASS_RO_$_TRIBMLTTargetingTask
- __OBJC_METACLASS_RO_$_TRIBMLTTaskSupport
- __OBJC_METACLASS_RO_$_TRIBMLTTaskSupportGuardedData
- __OBJC_METACLASS_RO_$_TRIBackgroundMLTaskDatabase
- __OBJC_METACLASS_RO_$_TRIBackgroundMLTaskHistoryDatabase
- __OBJC_METACLASS_RO_$_TRIBackgroundMLTaskRecord
- __OBJC_METACLASS_RO_$_TRIClientBMLTArtifact
- __OBJC_METACLASS_RO_$_TRIClientBMLTCatalogArtifact
- __OBJC_METACLASS_RO_$_TRIDeactivateBMLTDeploymentGuardedData
- __OBJC_METACLASS_RO_$_TRIDeactivateBMLTDeploymentPersistedTask
- __OBJC_METACLASS_RO_$_TRIDeactivateBMLTDeploymentTask
- __OBJC_METACLASS_RO_$_TRIFetchBMLTNotificationGuardedData
- __OBJC_METACLASS_RO_$_TRIFetchBMLTNotificationsPersistedTask
- __OBJC_METACLASS_RO_$_TRIFetchBMLTNotificationsTask
- __OBJC_METACLASS_RO_$_TRIInternalSystemServiceRequestHandler
- __OBJC_METACLASS_RO_$_TRIKnownLowLevelFactorsReader
- __OBJC_METACLASS_RO_$_TRILighthouseBitacoraHandler
- __OBJC_METACLASS_RO_$_TRIMLRuntimeEvaluationHistoryDatabase
- __OBJC_METACLASS_RO_$_TRIMakeDefaultPersistedTask
- __OBJC_METACLASS_RO_$_TRIMakeDefaultTask
- __OBJC_METACLASS_RO_$_TRIPersistedClientBMLTArtifact
- __OBJC_METACLASS_RO_$_TRITripersistedClientBmltartifactRoot
- __OBJC_METACLASS_RO_$_TRIXPCInternalSystemServiceListener
- __OBJC_METACLASS_RO_$_TRIXPCInternalSystemServiceWrapper
- __OBJC_PROTOCOL_$_TRIActiveLowLevelNamespacesProviding
- __OBJC_PROTOCOL_$_TRIXPCInternalSystemServiceProtocol
- __OBJC_PROTOCOL_REFERENCE_$_TRIXPCInternalSystemServiceProtocol
- ___100-[TRIBackgroundMLTaskDatabase deactivateTaskDeployment:deactivatedFactorPackSetId:usingTransaction:]_block_invoke
- ___100-[TRIBackgroundMLTaskDatabase deactivateTaskDeployment:deactivatedFactorPackSetId:usingTransaction:]_block_invoke.121
- ___100-[TRIBackgroundMLTaskDatabase deactivateTaskDeployment:deactivatedFactorPackSetId:usingTransaction:]_block_invoke_2
- ___101-[TRIBackgroundMLTaskHistoryDatabase getAllAllocationStatusesForBMLTId:deploymentId:factorPackSetId:]_block_invoke
- ___101-[TRIBackgroundMLTaskHistoryDatabase getAllAllocationStatusesForBMLTId:deploymentId:factorPackSetId:]_block_invoke_2
- ___101-[TRIBackgroundMLTaskHistoryDatabase getAllAllocationStatusesForBMLTId:deploymentId:factorPackSetId:]_block_invoke_3
- ___101-[TRIFactorPackSetStorage enumerateCompatibleFactorPacksForFactorPackSet:usingLegacyPaths:withBlock:]_block_invoke.141
- ___101-[TRIFactorPackSetStorage enumerateCompatibleFactorPacksForFactorPackSet:usingLegacyPaths:withBlock:]_block_invoke.146
- ___101-[TRINamespaceResolverStorage _removeUnreferencedBMLTDeploymentsWithRefStore:parentDir:removedCount:]_block_invoke
- ___101-[TRIXPCNamespaceManagementRequestHandler getSandboxExtensionTokensForIdentifierQueryWithCompletion:]_block_invoke.249
- ___101-[TRIXPCStatusRequestHandler evaluationHistoryRecordsForMLRuntimeWithLimit:newerThanDate:completion:]_block_invoke
- ___101-[TRIXPCStatusRequestHandler evaluationHistoryRecordsForMLRuntimeWithLimit:newerThanDate:completion:]_block_invoke.121
- ___101-[TRIXPCStatusRequestHandler evaluationHistoryRecordsForMLRuntimeWithLimit:newerThanDate:completion:]_block_invoke_2
- ___101-[TRIXPCStatusRequestHandler evaluationHistoryRecordsForMLRuntimeWithLimit:newerThanDate:completion:]_block_invoke_3
- ___101-[TRIXPCStatusRequestHandler evaluationHistoryRecordsForMLRuntimeWithLimit:newerThanDate:completion:]_block_invoke_4
- ___102-[TRIBackgroundMLTaskDatabase addBackgroundMLTaskWithTaskDeployment:pluginId:status:endDate:artifact:]_block_invoke
- ___102-[TRIBackgroundMLTaskDatabase addBackgroundMLTaskWithTaskDeployment:pluginId:status:endDate:artifact:]_block_invoke_2
- ___102-[TRICKNativeArtifactProvider _fetchRolloutNotificationWithRolloutId:deploymentId:options:completion:]_block_invoke.228
- ___103-[TRIActivateTreatmentBaseTask _experimentRecord:hasConflictWithExperimentsInDatabase:conflictEndTime:]_block_invoke.30
- ___103-[TRIActivateTreatmentBaseTask _experimentRecord:hasConflictWithExperimentsInDatabase:conflictEndTime:]_block_invoke.31
- ___103-[TRINamespaceResolverStorage _removeUnreferencedBMLTDeploymentsWithRefStore:topLevelDir:removedCount:]_block_invoke
- ___103-[TRIXPCNamespaceManagementRequestHandler setPurgeabilityLevelsForFactors:forNamespaceName:completion:]_block_invoke.215
- ___104+[TRIClientFactorPackUtils _enumerateAssetFactorLevelsInFlatBufferStorage:trialAssetBlock:maAssetBlock:]_block_invoke.303
- ___105-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:completion:]_block_invoke
- ___105-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:completion:]_block_invoke.100
- ___105-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:completion:]_block_invoke.104
- ___105-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:completion:]_block_invoke.87
- ___105-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:completion:]_block_invoke_2
- ___105-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:completion:]_block_invoke_2.103
- ___105-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:completion:]_block_invoke_3
- ___106-[TRIBackgroundMLTaskDatabase activateDeployment:withFactorPackSetId:targetingRuleIndex:usingTransaction:]_block_invoke
- ___106-[TRIBackgroundMLTaskDatabase activateDeployment:withFactorPackSetId:targetingRuleIndex:usingTransaction:]_block_invoke.117
- ___106-[TRIBackgroundMLTaskDatabase targetTaskDeployment:toFactorPackSetId:targetingRuleIndex:usingTransaction:]_block_invoke
- ___106-[TRIBackgroundMLTaskDatabase targetTaskDeployment:toFactorPackSetId:targetingRuleIndex:usingTransaction:]_block_invoke.110
- ___107-[TRIActivateTreatmentBaseTask updateLoggingWithExperimentRecord:paths:trackingId:newLogTreatmentAddedOut:]_block_invoke
- ___107-[TRIActivateTreatmentBaseTask updateLoggingWithExperimentRecord:paths:trackingId:newLogTreatmentAddedOut:]_block_invoke_2
- ___107-[TRIActivateTreatmentBaseTask updateLoggingWithExperimentRecord:paths:trackingId:newLogTreatmentAddedOut:]_block_invoke_3
- ___107-[TRIClientTreatmentStorage _saveNamespacePartitionedTreatmentsForTreatment:forNamespaceNames:forRollouts:]_block_invoke
- ___108-[TRICKNativeArtifactProvider fetchAssetsWithIndexes:fromTreatmentWithRecordId:options:progress:completion:]_block_invoke_2.221
- ___108-[TRIXPCNamespaceManagementRequestHandler rejectFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke.231
- ___108-[TRIXPCNamespaceManagementRequestHandler rejectFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke.235
- ___108-[TRIXPCNamespaceManagementRequestHandler rejectFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke_2.236
- ___108-[TRIXPCNamespaceManagementRequestHandler statusOfDownloadForFactors:withNamespace:factorsState:completion:]_block_invoke.240
- ___108-[TRIXPCNamespaceManagementRequestHandler statusOfDownloadForFactors:withNamespace:factorsState:completion:]_block_invoke.241
- ___109-[TRIFBClientTreatmentStorage _saveNamespacePartitionedTreatmentsForTreatment:forNamespaceNames:forRollouts:]_block_invoke
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.387
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.394
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.399
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.409
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.396
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.401
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.411
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_3.398
- ___109-[TRIXPCNamespaceManagementRequestHandler promoteFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke.237
- ___109-[TRIXPCNamespaceManagementRequestHandler promoteFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke.238
- ___109-[TRIXPCNamespaceManagementRequestHandler promoteFactorPackId:forNamespaceName:rolloutDeployment:completion:]_block_invoke_2.239
- ___111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.315
- ___111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.322
- ___111-[TRIInternalServiceRequestHandler activeExperimentInformationWithEnvironments:privacyFilterPolicy:completion:]_block_invoke
- ___111-[TRIInternalServiceRequestHandler activeExperimentInformationWithEnvironments:privacyFilterPolicy:completion:]_block_invoke_2
- ___111-[TRIInternalSystemServiceRequestHandler _getOnDemandReferenceCountsAtGlobalPath:onDemandFactorsPerUser:error:]_block_invoke
- ___112-[TRIInternalServiceRequestHandler experimentNotificationsWithExperimentId:cloudKitContainer:teamId:completion:]_block_invoke.45
- ___112-[TRIInternalServiceRequestHandler experimentNotificationsWithExperimentId:cloudKitContainer:teamId:completion:]_block_invoke.73
- ___113-[TRIFetchBMLTNotificationsTask _processBMLTArtifact:bmltsProcessed:deactivatedBMLTs:targeter:context:taskQueue:]_block_invoke
- ___114-[TRIXPCNamespaceManagementRequestHandler immediateDownloadForNamespaceNames:allowExpensiveNetworking:completion:]_block_invoke.199
- ___114-[TRIXPCNamespaceManagementRequestHandler immediateDownloadForNamespaceNames:allowExpensiveNetworking:completion:]_block_invoke.201
- ___114-[TRIXPCNamespaceManagementRequestHandler immediateDownloadForNamespaceNames:allowExpensiveNetworking:completion:]_block_invoke.208
- ___115-[TRICKNativeArtifactProvider _fetchRecordIdsForAssetsWithIds:options:cursor:cancelableOp:resultBuffer:completion:]_block_invoke.243
- ___116-[TRIBackgroundMLTaskDatabase setActiveFactorPackSetId:activeTargetingRuleIndex:forTaskDeployment:usingTransaction:]_block_invoke
- ___116-[TRIBackgroundMLTaskDatabase setActiveFactorPackSetId:activeTargetingRuleIndex:forTaskDeployment:usingTransaction:]_block_invoke_2
- ___116-[TRICKNativeArtifactProvider _fetchRolloutNotificationsWithCursor:options:sinceDate:namespaceNames:resultsHandler:]_block_invoke.226
- ___116-[TRIRolloutDatabase targetDeployment:toFactorPackSetId:targetingRuleIndex:deallocatedDeployments:usingTransaction:]_block_invoke.177
- ___118+[TRIXPCNamespaceManagementRequestHandler usingServerContext:deregisterNamespaceWithName:teamId:taskQueue:completion:]_block_invoke.318
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.527
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.530
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.539
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.540
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke_2.528
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke_2.531
- ___119-[TRICKNativeArtifactProvider fetchDiffSourceRecordIdsWithTargetAssetIds:isAcceptableSourceAssetId:options:completion:]_block_invoke.271
- ___119-[TRICKNativeArtifactProvider fetchDiffSourceRecordIdsWithTargetAssetIds:isAcceptableSourceAssetId:options:completion:]_block_invoke.273
- ___119-[TRIXPCNamespaceManagementRequestHandler startDownloadLevelsForFactors:withNamespace:factorsState:options:completion:]_block_invoke.178
- ___119-[TRIXPCNamespaceManagementRequestHandler startDownloadLevelsForFactors:withNamespace:factorsState:options:completion:]_block_invoke.183
- ___119-[TRIXPCNamespaceManagementRequestHandler startDownloadLevelsForFactors:withNamespace:factorsState:options:completion:]_block_invoke_2.184
- ___120-[TRIBackgroundMLTaskDatabase setTargetedFactorPackSetId:targetedTargetingRuleIndex:forTaskDeployment:usingTransaction:]_block_invoke
- ___120-[TRIBackgroundMLTaskDatabase setTargetedFactorPackSetId:targetedTargetingRuleIndex:forTaskDeployment:usingTransaction:]_block_invoke_2
- ___122-[TRIXPCNamespaceManagementRequestHandler removeLevelsForFactors:withNamespace:factorsState:removeImmediately:completion:]_block_invoke.209
- ___122-[TRIXPCNamespaceManagementRequestHandler removeLevelsForFactors:withNamespace:factorsState:removeImmediately:completion:]_block_invoke.213
- ___122-[TRIXPCNamespaceManagementRequestHandler removeLevelsForFactors:withNamespace:factorsState:removeImmediately:completion:]_block_invoke_2.214
- ___124-[TRIInternalServiceRequestHandler rolloutNotificationWithLatestDeploymentForRolloutId:cloudKitContainer:teamId:completion:]_block_invoke.76
- ___124-[TRIInternalServiceRequestHandler rolloutNotificationWithLatestDeploymentForRolloutId:cloudKitContainer:teamId:completion:]_block_invoke.82
- ___125-[TRIExperimentDatabase addExperimentWithExperimentDeployment:environment:type:status:startDate:endDate:namespaces:artifact:]_block_invoke.39
- ___126-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:serverContext:completion:]_block_invoke
- ___126-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:serverContext:completion:]_block_invoke.194
- ___126-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:serverContext:completion:]_block_invoke.209
- ___126-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:serverContext:completion:]_block_invoke_2
- ___126-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:serverContext:completion:]_block_invoke_2.215
- ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke.440
- ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_2.442
- ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_3.443
- ___127-[TRICKNativeArtifactProvider _fetchNotificationsWithQueryType:withCursor:withNamespaceNames:sinceDate:options:resultsHandler:]_block_invoke.159
- ___127-[TRICKNativeArtifactProvider _fetchNotificationsWithQueryType:withCursor:withNamespaceNames:sinceDate:options:resultsHandler:]_block_invoke.162
- ___127-[TRICKNativeArtifactProvider _fetchNotificationsWithQueryType:withCursor:withNamespaceNames:sinceDate:options:resultsHandler:]_block_invoke.166
- ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.464
- ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.472
- ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.482
- ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke_2.474
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.541
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.543
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.544
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.545
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke_2.542
- ___129-[TRICKNativeArtifactProvider fetchExperimentNotificationsForLimitedCarryExperimentWithManager:options:rollbacksOnly:completion:]_block_invoke.187
- ___129-[TRICKNativeArtifactProvider fetchExperimentNotificationsForLimitedCarryExperimentWithManager:options:rollbacksOnly:completion:]_block_invoke.188
- ___129-[TRISelectRolloutNotificationListTask _processRolloutArtifact:rolloutsProcessed:remainingNamespaces:targeter:context:taskQueue:]_block_invoke.36
- ___130-[TRICKNativeArtifactProvider _fetchExperimentsWithCursor:withNamespaceNames:sinceDate:fetchRollbacksOnly:options:resultsHandler:]_block_invoke.157
- ___131-[TRIClientTreatment(TRIUtil) _triRequiredMAAssetsForInstallationWithAssetStore:subscriptionSettings:maProvider:aliasToUnaliasMap:]_block_invoke.298
- ___131-[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:privacyFilterPolicy:deploymentEnvironment:completion:]_block_invoke
- ___131-[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:privacyFilterPolicy:deploymentEnvironment:completion:]_block_invoke.49
- ___131-[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:privacyFilterPolicy:deploymentEnvironment:completion:]_block_invoke.54
- ___131-[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:privacyFilterPolicy:deploymentEnvironment:completion:]_block_invoke.75
- ___131-[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:privacyFilterPolicy:deploymentEnvironment:completion:]_block_invoke.85
- ___131-[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:privacyFilterPolicy:deploymentEnvironment:completion:]_block_invoke_2
- ___131-[TRIXPCStatusRequestHandler experimentHistoryRecordsWithLimit:newerThanDate:privacyFilterPolicy:deploymentEnvironment:completion:]_block_invoke_2.81
- ___138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke.521
- ___138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke_2.523
- ___151-[TRIFetchTreatmentTask _fetchAssetsWithArtifactProvider:recordId:experimentRecord:assetIndexes:downloadOptions:context:assetURLs:treatmentFetchError:]_block_invoke.360
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.489
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.491
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.495
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.490
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.497
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_3.498
- ___154-[TRIPurgeableExperimentAndRolloutProvider _factorPackSetHasPurgeableFactorsWithFPSId:eagerFactors:overriddenFactors:purgeableNamespaces:returningAssets:]_block_invoke.54
- ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.349
- ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.350
- ___158-[TRICKNativeArtifactProvider fetchDiffsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.274
- ___158-[TRICKNativeArtifactProvider fetchDiffsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.277
- ___159-[TRICKNativeArtifactProvider fetchAssetsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.249
- ___159-[TRICKNativeArtifactProvider fetchAssetsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.251
- ___159-[TRICKNativeArtifactProvider fetchAssetsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke_2.255
- ___163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.399
- ___163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.404
- ___163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.410
- ___163-[TRIXPCNamespaceManagementRequestHandler registerNamespaceWithNamespaceName:compatibilityVersion:defaultsFileURL:applicationGroup:cloudKitContainerId:completion:]_block_invoke.103
- ___163-[TRIXPCNamespaceManagementRequestHandler registerNamespaceWithNamespaceName:compatibilityVersion:defaultsFileURL:applicationGroup:cloudKitContainerId:completion:]_block_invoke.140
- ___163-[TRIXPCNamespaceManagementRequestHandler registerNamespaceWithNamespaceName:compatibilityVersion:defaultsFileURL:applicationGroup:cloudKitContainerId:completion:]_block_invoke_2.141
- ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.322
- ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.324
- ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.330
- ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.410
- ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.420
- ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.416
- ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.423
- ___170-[TRIRolloutDatabase deactivateDeploymentsWithRolloutId:deactivatedDeployment:deactivatedFactorPackSetId:deactivatedRampId:deactivationStateTransitions:usingTransaction:]_block_invoke.192
- ___174-[TRIPurgeableExperimentAndRolloutProvider _purgeablesForRolloutsFromNamespaces:eagerFactors:overriddenFactors:shouldGenerateAssetPaths:purgeableExperiments:purgeableAssets:]_block_invoke.34
- ___177-[TRIPurgeableExperimentAndRolloutProvider _purgeablesForExperimentsFromNamespaces:eagerFactors:overriddenFactors:shouldGenerateAssetPaths:purgeableExperiments:purgeableAssets:]_block_invoke.31
- ___177-[TRIRolloutDatabase activateDeployment:withFactorPackSetId:targetingRuleIndex:deactivatedDeployments:deactivatedFactorPackSetIds:deactivationStateTransitions:usingTransaction:]_block_invoke.185
- ___178-[TRIInternalServiceRequestHandler registerNamespaceWithNamespaceName:compatibilityVersion:defaultsFileURL:teamId:appContainerId:appContainerType:cloudKitContainerId:completion:]_block_invoke.108
- ___179+[TRIXPCNamespaceManagementRequestHandler _immediateDownloadForNamespaceNames:usingEntitlementWitness:serverContext:taskQueue:allowExpensiveNetworking:taskAttribution:completion:]_block_invoke.376
- ___19-[TRIDServer start]_block_invoke.354
- ___19-[TRIDServer start]_block_invoke.355
- ___19-[TRIDServer start]_block_invoke.359
- ___19-[TRIDServer start]_block_invoke.363
- ___257+[TRIXPCNamespaceManagementRequestHandler _startDownloadAssetIndexesByTreatment:usingEntitlementWitness:serverContext:taskQueue:experimentIds:assetIdsByFactorPack:rolloutFactorNames:rolloutDeployments:namespace:taskAttribution:factorsState:notificationKey:]_block_invoke.359
- ___27-[TRITaskDatabase allTasks]_block_invoke.109
- ___27-[TRITaskDatabase allTasks]_block_invoke_2.113
- ___29-[TRIBMLTTaskSupport metrics]_block_invoke
- ___32-[TRIBMLTTaskSupport addMetric:]_block_invoke
- ___32-[TRIBMLTTaskSupport dimensions]_block_invoke
- ___34-[TRICancelableMAOperation cancel]_block_invoke.474
- ___35-[TRIBMLTTaskSupport addDimension:]_block_invoke
- ___35-[TRIXPCInternalServiceClient init]_block_invoke
- ___35-[TRIXPCInternalServiceClient init]_block_invoke_2
- ___36-[TRIClientBMLTArtifact(Utils) data]_block_invoke
- ___37-[TRIBMLTTaskSupport mergeTelemetry:]_block_invoke
- ___38-[TRIExperimentBaseTask logAsRollout:]_block_invoke
- ___39+[TRIXPCServices registerSystemService]_block_invoke
- ___40-[TRIFetchBMLTNotificationsTask metrics]_block_invoke
- ___40-[TRITaskDatabase tasksDependentOnTask:]_block_invoke.186
- ___41-[TRITaskDatabase _tasksForQuery:onPrep:]_block_invoke.137
- ___41-[TRITaskDatabase _tasksForQuery:onPrep:]_block_invoke_2.138
- ___42-[TRIBMLTTaskSupport trialSystemTelemetry]_block_invoke
- ___42-[TRIDatabase migration_addTaskCapability]_block_invoke.308
- ___42-[TRIDeactivateBMLTDeploymentTask metrics]_block_invoke
- ___43-[TRIFetchBMLTNotificationsTask dimensions]_block_invoke
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.381
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.391
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.398
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.410
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.441
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.392
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.399
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.411
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.442
- ___44-[TRIFetchBMLTNotificationsTask _addMetric:]_block_invoke
- ___45-[TRIDeactivateBMLTDeploymentTask addMetric:]_block_invoke
- ___46-[TRIRolloutDatabase addNewRolloutWithRecord:]_block_invoke.39
- ___46-[TRIRolloutDatabase addNewRolloutWithRecord:]_block_invoke.43
- ___47-[TRIFetchBMLTNotificationsTask _addDimension:]_block_invoke
- ___47-[TRITaskQueue _finalizeTask:withId:runResult:]_block_invoke.211
- ___47-[TRITaskQueue _finalizeTask:withId:runResult:]_block_invoke.213
- ___48-[TRIBackgroundMLTaskHistoryDatabase addRecord:]_block_invoke
- ___48-[TRIBackgroundMLTaskHistoryDatabase addRecord:]_block_invoke_2
- ___49+[TRIXPCServices registerAllServicesWithPromise:]_block_invoke
- ___50-[TRIDeactivateBMLTDeploymentTask mergeTelemetry:]_block_invoke
- ___50-[TRITaskDatabase directDependenciesOfTaskWithId:]_block_invoke.182
- ___50-[TRITaskQueue _registerTaskQueueActivityForDate:]_block_invoke.284
- ___50-[TRITaskQueue _registerTaskQueueActivityForDate:]_block_invoke.285
- ___52-[TRIPostUpgradeCleanupTask _nextTasksForRunStatus:]_block_invoke_2
- ___52-[TRIRetargetAllTask runUsingContext:withTaskQueue:]_block_invoke.33
- ___52-[TRIRetargetAllTask runUsingContext:withTaskQueue:]_block_invoke_2
- ___53-[TRIMAProvider installedAssetsMatchingFullAssetIds:]_block_invoke.498
- ___53-[TRIXPCActivityManager _registerPostUpgradeActivity]_block_invoke.340
- ___53-[TRIXPCActivityManager _registerPostUpgradeActivity]_block_invoke.346
- ___55+[TRIKnownLowLevelFactorsReader knownFactorsFromPaths:]_block_invoke
- ___55-[TRIDeactivateBMLTDeploymentTask trialSystemTelemetry]_block_invoke
- ___55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.386
- ___55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.390
- ___56-[TRISQLiteCKDatabase _valueTypesForFieldsOfRecordType:]_block_invoke_7
- ___56-[TRISQLiteCKDatabase _valueTypesForFieldsOfRecordType:]_block_invoke_8
- ___56-[TRIXPCStatusRequestHandler bmltRecordsWithCompletion:]_block_invoke
- ___56-[TRIXPCStatusRequestHandler bmltRecordsWithCompletion:]_block_invoke.141
- ___56-[TRIXPCStatusRequestHandler bmltRecordsWithCompletion:]_block_invoke.142
- ___56-[TRIXPCStatusRequestHandler bmltRecordsWithCompletion:]_block_invoke_2
- ___56-[TRIXPCStatusRequestHandler bmltRecordsWithCompletion:]_block_invoke_3
- ___57-[TRIAssetPurger purgeableAssetSizeForPurgeabilityLevel:]_block_invoke.113
- ___57-[TRIDisenrollRolloutTask runUsingContext:withTaskQueue:]_block_invoke.56
- ___57-[TRIXPCActivityManager _registerHotfixTargetingActivity]_block_invoke.357
- ___57-[TRIXPCActivityManager _registerHotfixTargetingActivity]_block_invoke_2.358
- ___58+[TRIClientBMLTArtifact(Utils) artifactWithTransientData:]_block_invoke
- ___58-[TRIActiveLowLevelExperimentsReader allActiveExperiments]_block_invoke
- ___58-[TRIBackgroundMLTaskDatabase removeRecordWithDeployment:]_block_invoke
- ___58-[TRIBackgroundMLTaskDatabase removeRecordWithDeployment:]_block_invoke_2
- ___59-[TRIActivateTreatmentTask runTaskUsingContext:experiment:]_block_invoke.170
- ___59-[TRIActivateTreatmentTask runTaskUsingContext:experiment:]_block_invoke.172
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.462
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.473
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.481
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.497
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.515
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.520
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.522
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.517
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.523
- ___59-[TRITaskQueue activeActivityDescriptorGrantingCapability:]_block_invoke.302
- ___59-[TRIXPCStatusRequestHandler rolloutRecordsWithCompletion:]_block_invoke.144
- ___59-[TRIXPCStatusRequestHandler rolloutRecordsWithCompletion:]_block_invoke.145
- ___60-[TRIBackgroundMLTaskDatabase taskRecordWithTaskDeployment:]_block_invoke
- ___60-[TRIBackgroundMLTaskDatabase taskRecordWithTaskDeployment:]_block_invoke_2
- ___60-[TRIDeactivateTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.59
- ___60-[TRIDeactivateTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.73
- ___60-[TRIDeactivateTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.77
- ___60-[TRIDeactivateTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.92
- ___60-[TRIRolloutDatabase recordWithDeployment:usingTransaction:]_block_invoke.125
- ___60-[TRIXPCActivityManager registerSetupAssistantFetchActivity]_block_invoke.354
- ___60-[TRIXPCActivityManager registerSetupAssistantFetchActivity]_block_invoke.355
- ___61-[TRIBackgroundMLTaskDatabase enumerateActiveTasksWithBlock:]_block_invoke
- ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.434
- ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.453
- ___62-[TRIInternalServiceRequestHandler taskRecordsWithCompletion:]_block_invoke.37
- ___62-[TRIXPCInternalServiceClient _performSyncXpcWithError:block:]_block_invoke
- ___63-[TRIFetchBMLTNotificationsTask runUsingContext:withTaskQueue:]_block_invoke
- ___63-[TRIFetchBMLTNotificationsTask runUsingContext:withTaskQueue:]_block_invoke.88
- ___63-[TRIFetchBMLTNotificationsTask runUsingContext:withTaskQueue:]_block_invoke.89
- ___63-[TRITaskQueue enumerateTasksWithTagsIntersectingTagSet:block:]_block_invoke.277
- ___64-[TRIInternalServiceRequestHandler setFailureInjectionDelegate:]_block_invoke.100
- ___65-[TRIDeactivateBMLTDeploymentTask runUsingContext:withTaskQueue:]_block_invoke
- ___65-[TRIMaintenanceTask _cleanupUnusedContentWithContext:nextTasks:]_block_invoke.83
- ___65-[TRIMaintenanceTask _cleanupUnusedContentWithContext:nextTasks:]_block_invoke.89
- ___65-[TRIMaintenanceTask _cleanupUnusedContentWithContext:nextTasks:]_block_invoke.91
- ___65-[TRIMaintenanceTask _cleanupUnusedContentWithContext:nextTasks:]_block_invoke.95
- ___65-[TRIMaintenanceTask _cleanupUnusedContentWithContext:nextTasks:]_block_invoke.97
- ___65-[TRIMaintenanceTask _cleanupUnusedContentWithContext:nextTasks:]_block_invoke.99
- ___65-[TRIMaintenanceTask _cleanupUnusedContentWithContext:nextTasks:]_block_invoke_2.90
- ___65-[TRIMakeDefaultTask makeDefaultForNamespace:experiment:context:]_block_invoke
- ___66-[TRIFetchBMLTNotificationsTask fetchSingleDeploymentWithContext:]_block_invoke
- ___66-[TRIFetchBMLTNotificationsTask fetchSingleDeploymentWithContext:]_block_invoke.69
- ___66-[TRIInternalServiceRequestHandler submitTask:options:completion:]_block_invoke.84
- ___68-[TRIMLRuntimeEvaluationHistoryDatabase addRecord:usingTransaction:]_block_invoke
- ___68-[TRIMLRuntimeEvaluationHistoryDatabase addRecord:usingTransaction:]_block_invoke_2
- ___68-[TRIMaintenanceTask _handleExpiredBMLTsWithBMLTDatabase:nextTasks:]_block_invoke
- ___69-[TRIBackgroundMLTaskDatabase deactivateDeployment:usingTransaction:]_block_invoke
- ___69-[TRIBackgroundMLTaskDatabase deactivateDeployment:usingTransaction:]_block_invoke_2
- ___69-[TRIFetchFactorPackSetTask _requiredAssetsForFactorPackSet:context:]_block_invoke.387
- ___69-[TRITaskQueue resumeWithXPCActivityDescriptor:executeWhenSuspended:]_block_invoke.106
- ___69-[TRITaskQueue resumeWithXPCActivityDescriptor:executeWhenSuspended:]_block_invoke.98
- ___69-[TRIXPCStatusRequestHandler activeEvaluationsForBMLTWithCompletion:]_block_invoke
- ___69-[TRIXPCStatusRequestHandler activeEvaluationsForBMLTWithCompletion:]_block_invoke.123
- ___69-[TRIXPCStatusRequestHandler activeEvaluationsForBMLTWithCompletion:]_block_invoke.128
- ___69-[TRIXPCStatusRequestHandler activeEvaluationsForBMLTWithCompletion:]_block_invoke_2
- ___69-[TRIXPCStatusRequestHandler activeEvaluationsForBMLTWithCompletion:]_block_invoke_3
- ___69-[TRIXPCStatusRequestHandler activeEvaluationsForBMLTWithCompletion:]_block_invoke_4
- ___70-[TRIActiveLowLevelExperimentsReader _factorLevelStringsForNamespace:]_block_invoke
- ___70-[TRISelectRolloutNotificationListTask runUsingContext:withTaskQueue:]_block_invoke.67
- ___71-[TRIActivateTargetedBMLTDeploymentTask runUsingContext:withTaskQueue:]_block_invoke
- ___71-[TRIActivateTargetedBMLTDeploymentTask runUsingContext:withTaskQueue:]_block_invoke.82
- ___71-[TRIAssetPurger purgeAssetsForPurgeabilityLevel:requestedPurgeAmount:]_block_invoke.135
- ___71-[TRICKNativeArtifactProvider fetchTreatmentWithId:options:completion:]_block_invoke.208
- ___71-[TRIInternalServiceRequestHandler removeUnusedChannelsWithCompletion:]_block_invoke.104
- ___72-[TRIXPCActivityManager _scheduleFetchTaskWithActivityDescriptor:label:]_block_invoke.318
- ___73-[TRIBackgroundMLTaskDatabase enumerateActiveTasksWithTransaction:block:]_block_invoke
- ___73-[TRIFetchFactorPackSetTask _saveFactorPackSet:requiredAssetMap:context:]_block_invoke.444
- ___73-[TRITaskQueue _evaluateRunConditionsWithGuardedData:shouldContinueWork:]_block_invoke.94
- ___74-[TRIBackgroundMLTaskHistoryDatabase enumerateRecordsNewerThanDate:block:]_block_invoke
- ___74-[TRIInternalServiceRequestHandler dynamicNamespaceRecordsWithCompletion:]_block_invoke.144
- ___74-[TRIXPCInternalSystemServiceListener listener:shouldAcceptNewConnection:]_block_invoke
- ___74-[TRIXPCInternalSystemServiceListener listener:shouldAcceptNewConnection:]_block_invoke_2
- ___74-[TRIXPCInternalSystemServiceListener listener:shouldAcceptNewConnection:]_block_invoke_3
- ___74-[TRIXPCStatusRequestHandler activeEvaluationsForMLRuntimeWithCompletion:]_block_invoke
- ___74-[TRIXPCStatusRequestHandler activeEvaluationsForMLRuntimeWithCompletion:]_block_invoke.105
- ___74-[TRIXPCStatusRequestHandler activeEvaluationsForMLRuntimeWithCompletion:]_block_invoke.116
- ___74-[TRIXPCStatusRequestHandler activeEvaluationsForMLRuntimeWithCompletion:]_block_invoke_2
- ___74-[TRIXPCStatusRequestHandler activeEvaluationsForMLRuntimeWithCompletion:]_block_invoke_3
- ___74-[TRIXPCStatusRequestHandler activeEvaluationsForMLRuntimeWithCompletion:]_block_invoke_4
- ___75-[TRICKNativeArtifactProvider fetchFactorPackSetWithId:options:completion:]_block_invoke.232
- ___76-[TRIBackgroundMLTaskDatabase setStatus:forTaskDeployment:usingTransaction:]_block_invoke
- ___76-[TRIBackgroundMLTaskDatabase setStatus:forTaskDeployment:usingTransaction:]_block_invoke_2
- ___77-[TRIMLRuntimeEvaluationHistoryDatabase enumerateRecordsNewerThanDate:block:]_block_invoke
- ___77-[TRIPostUpgradeCleanupTask _validateBMLTNamespaceNCVs:downloadNCVs:context:]_block_invoke
- ___78-[TRIBackgroundMLTaskHistoryDatabase expireRecordsOlderThanDate:deletedCount:]_block_invoke
- ___78-[TRIBackgroundMLTaskHistoryDatabase expireRecordsOlderThanDate:deletedCount:]_block_invoke_2
- ___78-[TRIExperimentDatabase enumerateActiveExperimentRecordsWithVisibility:block:]_block_invoke
- ___78-[TRIExperimentDatabase(LowLevelNamespacesProviding) activeLowLevelNamespaces]_block_invoke
- ___78-[TRIInternalServiceRequestHandler resumeSQLiteCKDatabaseQueueWithCompletion:]_block_invoke.103
- ___78-[TRIPostUpgradeCleanupTask _activeBMLTIsCompatible:upgradeNCVs:downloadNCVs:]_block_invoke
- ___78-[TRIXPCActivityManager _scheduleMaintenanceTaskWithActivityDescriptor:label:]_block_invoke.324
- ___79-[TRIFactorPackSetStorage migrateEligibleFactorPacksToGlobalWithServerContext:]_block_invoke.155
- ___79-[TRIInternalServiceRequestHandler suspendSQLiteCKDatabaseQueueWithCompletion:]_block_invoke.101
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.505
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.509
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.510
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.513
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.518
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke_2.511
- ___80+[TRIClientBMLTCatalogArtifact(CloudKit) _hasStructurallyValidBMLTs:population:]_block_invoke
- ___80-[TRIInternalServiceRequestHandler lastFetchDateForContainer:teamId:completion:]_block_invoke.92
- ___81-[TRIMLRuntimeEvaluationHistoryDatabase expireRecordsOlderThanDate:deletedCount:]_block_invoke
- ___81-[TRIMLRuntimeEvaluationHistoryDatabase expireRecordsOlderThanDate:deletedCount:]_block_invoke_2
- ___81-[TRITaskQueue _addTask:options:guardedData:taskIdOut:accumulatedNewTaskRecords:]_block_invoke.268
- ___81-[TRIXPCActivityManager _registerPostUpgradeActivityRequireInexpensiveNetworking]_block_invoke.347
- ___82-[TRICKNativeArtifactProvider fetchBMLTCatalogNotificationWithOptions:completion:]_block_invoke
- ___82-[TRICKNativeArtifactProvider fetchBMLTCatalogNotificationWithOptions:completion:]_block_invoke.281
- ___82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.112
- ___82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.119
- ___82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.124
- ___82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke.131
- ___82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke_2.121
- ___82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke_2.126
- ___82-[TRIFBClientTreatmentStorage _writeFactorLevelsToDisk:namespaceName:writeToPath:]_block_invoke_3.123
- ___82-[TRIInternalServiceRequestHandler _activeExperimentFactorLevelsForNamespaceName:]_block_invoke
- ___82-[TRIInternalServiceRequestHandler _activeExperimentFactorLevelsForNamespaceName:]_block_invoke_2
- ___82-[TRIInternalServiceRequestHandler _activeExperimentFactorLevelsForNamespaceName:]_block_invoke_3
- ___82-[TRIRolloutDatabase enumerateActiveRecordsWithVisibility:usingTransaction:block:]_block_invoke
- ___83-[TRIExperimentDatabase _enumerateExperimentRecordsMatchingWhereClause:bind:block:]_block_invoke.137
- ___83-[TRITaskQueue _startImmediateTasksIfNotAlreadyQueued:guardedData:didStartNewWork:]_block_invoke.241
- ___83-[TRITaskQueue _startImmediateTasksIfNotAlreadyQueued:guardedData:didStartNewWork:]_block_invoke.242
- ___84-[TRIBackgroundMLTaskDatabase enumerateTaskRecordsMatchingTaskId:transaction:block:]_block_invoke
- ___84-[TRICKNativeArtifactProvider _fetchBMLTNotificationsWithCursor:options:completion:]_block_invoke
- ___84-[TRICKNativeArtifactProvider _fetchBMLTNotificationsWithCursor:options:completion:]_block_invoke.291
- ___84-[TRIInternalServiceRequestHandler setLastFetchDate:forContainer:teamId:completion:]_block_invoke.96
- ___84-[TRIRemoteAssetStoreOperator saveFactorPackToGlobalPath:fromTemporaryPath:factors:]_block_invoke.368
- ___86-[TRIBackgroundMLTaskHistoryDatabase _enumerateRecordsMatchingWhereClause:bind:block:]_block_invoke
- ___86-[TRIBackgroundMLTaskHistoryDatabase _enumerateRecordsMatchingWhereClause:bind:block:]_block_invoke_2
- ___86-[TRICKNativeArtifactProvider fetchBMLTNotificationWithDeployment:options:completion:]_block_invoke
- ___86-[TRICKNativeArtifactProvider fetchBMLTNotificationWithDeployment:options:completion:]_block_invoke.286
- ___86-[TRIFetchBMLTNotificationsTask _processBMLTCatalogArtifact:deactivatedBMLTs:context:]_block_invoke
- ___86-[TRIFetchBMLTNotificationsTask _processBMLTCatalogArtifact:deactivatedBMLTs:context:]_block_invoke_2
- ___86-[TRIPostUpgradeCleanupTask _validateDynamicNamespaceRolloutsWithDatabase:usingPaths:]_block_invoke
- ___87-[TRICKNativeArtifactProvider _fetchRolloutNotificationsWithCursor:options:completion:]_block_invoke.227
- ___88-[TRIAssetStoreDatabase initWithPaths:databasePath:storageManagement:performMigrations:]_block_invoke.66
- ___88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.340
- ___88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.342
- ___88-[TRIBackgroundMLTaskDatabase enumerateActiveTasksNotInList:usingTransaction:withBlock:]_block_invoke
- ___88-[TRIBackgroundMLTaskDatabase enumerateActiveTasksNotInList:usingTransaction:withBlock:]_block_invoke_2
- ___88-[TRIXPCStatusRequestHandler rolloutAllocationStatusWithPrivacyFilterPolicy:completion:]_block_invoke
- ___89-[TRIActivateTargetedBMLTDeploymentTask _hasValidNCVForBMLT:namespaceDescriptorProvider:]_block_invoke
- ___89-[TRIAssetStore _linkDirectoryAssetWithIdentifier:toCurrentPath:futurePath:flockWitness:]_block_invoke.368
- ___89-[TRIMLRuntimeEvaluationHistoryDatabase _enumerateRecordsMatchingWhereClause:bind:block:]_block_invoke
- ___89-[TRIMLRuntimeEvaluationHistoryDatabase _enumerateRecordsMatchingWhereClause:bind:block:]_block_invoke_2
- ___90-[TRIFetchFactorPackSetTask incompatibleNamespaceNameForBMLT:namespaceDescriptorProvider:]_block_invoke
- ___90-[TRINamespaceResolverStorage overwriteActiveFactorProvidersUsingTransaction:fromContext:]_block_invoke.191
- ___90-[TRINamespaceResolverStorage overwriteActiveFactorProvidersUsingTransaction:fromContext:]_block_invoke.203
- ___90-[TRINamespaceResolverStorage overwriteActiveFactorProvidersUsingTransaction:fromContext:]_block_invoke_2.205
- ___91-[TRIInternalServiceRequestHandler deregisterNamespaceWithNamespaceName:teamId:completion:]_block_invoke.129
- ___91-[TRIUrgentRollbackScheduler _validRollbackDeploymentsForRollbackExperiment:deploymentIds:]_block_invoke
- ___91-[TRIXPCNamespaceManagementRequestHandler deregisterNamespaceWithNamespaceName:completion:]_block_invoke.143
- ___91-[TRIXPCNamespaceManagementRequestHandler deregisterNamespaceWithNamespaceName:completion:]_block_invoke.144
- ___91-[TRIXPCNamespaceManagementRequestHandler deregisterNamespaceWithNamespaceName:completion:]_block_invoke_2.145
- ___92-[TRIInternalServiceRequestHandler activeBMLTInformationWithPrivacyFilterPolicy:completion:]_block_invoke
- ___92-[TRIInternalServiceRequestHandler activeBMLTInformationWithPrivacyFilterPolicy:completion:]_block_invoke_2
- ___92-[TRIInternalServiceRequestHandler activeBMLTInformationWithPrivacyFilterPolicy:completion:]_block_invoke_3
- ___92-[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]_block_invoke.297
- ___92-[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]_block_invoke.301
- ___92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke
- ___92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.241
- ___92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.244
- ___92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.246
- ___92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.249
- ___92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.261
- ___92-[TRIXPCNamespaceManagementRequestHandler loadNamespaceMetadataForNamespaceName:completion:]_block_invoke.219
- ___92-[TRIXPCNamespaceManagementRequestHandler loadNamespaceMetadataForNamespaceName:completion:]_block_invoke.223
- ___92-[TRIXPCNamespaceManagementRequestHandler loadNamespaceMetadataForNamespaceName:completion:]_block_invoke_2.224
- ___93-[TRIInternalServiceRequestHandler startDownloadNamespaceWithName:teamId:options:completion:]_block_invoke.139
- ___93-[TRIXPCNamespaceManagementRequestHandler startDownloadNamespaceWithName:options:completion:]_block_invoke.146
- ___93-[TRIXPCNamespaceManagementRequestHandler startDownloadNamespaceWithName:options:completion:]_block_invoke.160
- ___93-[TRIXPCNamespaceManagementRequestHandler startDownloadNamespaceWithName:options:completion:]_block_invoke_2.161
- ___95-[TRIBackgroundMLTaskDatabase _enumerateTaskRecordsMatchingWhereClause:bind:transaction:block:]_block_invoke
- ___95-[TRIBackgroundMLTaskDatabase _enumerateTaskRecordsMatchingWhereClause:bind:transaction:block:]_block_invoke_2
- ___95-[TRIInternalServiceRequestHandler activeRolloutInformationWithPrivacyFilterPolicy:completion:]_block_invoke
- ___95-[TRIInternalServiceRequestHandler activeRolloutInformationWithPrivacyFilterPolicy:completion:]_block_invoke.147
- ___95-[TRIInternalServiceRequestHandler activeRolloutInformationWithPrivacyFilterPolicy:completion:]_block_invoke_2
- ___95-[TRIInternalServiceRequestHandler activeRolloutInformationWithPrivacyFilterPolicy:completion:]_block_invoke_4
- ___96-[TRICKNativeArtifactProvider _fetchExperimentWithExperimentId:deploymentId:options:completion:]_block_invoke.142
- ___96-[TRICKNativeArtifactProvider _fetchExperimentWithExperimentId:deploymentId:options:completion:]_block_invoke.145
- ___98-[TRIXPCNamespaceManagementRequestHandler setProvisionalFactorPackId:forNamespaceName:completion:]_block_invoke.225
- ___98-[TRIXPCNamespaceManagementRequestHandler setProvisionalFactorPackId:forNamespaceName:completion:]_block_invoke.229
- ___98-[TRIXPCNamespaceManagementRequestHandler setProvisionalFactorPackId:forNamespaceName:completion:]_block_invoke_2.230
- ___99-[TRIInternalSystemServiceRequestHandler getOnDemandReferenceCountsPerUserAtGlobalPath:completion:]_block_invoke
- ___99-[TRIInternalSystemServiceRequestHandler getOnDemandReferenceCountsPerUserAtGlobalPath:completion:]_block_invoke_2
- ___Block_byref_object_copy_.246
- ___Block_byref_object_dispose_.247
- ___LighthouseBitacoraFrameworkLibraryCore_block_invoke
- ___block_descriptor_122_e8_32s40s48s56s64s72s80s88s96s104s112r_e64_{_PASDBTransactionCompletion_=B}16?0"_PASSqlWriteTransaction"8ls32l8s40l8r112l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
- ___block_descriptor_128_e8_32s40s48s56s64s72s80s88r96r104r112r120r_e57_v40?0Q8"TRIClientBMLTArtifact"16"NSDate"24"NSError"32lr88l8r96l8r104l8s32l8s40l8s48l8s56l8s64l8s72l8r112l8r120l8s80l8
- ___block_descriptor_147_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136r_e64_{_PASDBTransactionCompletion_=B}16?0"_PASSqlWriteTransaction"8ls32l8s40l8r136l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8
- ___block_descriptor_32_e27_16?0"TRIBMLTDeployment"8l
- ___block_descriptor_32_e44_B24?0"TRIBMLTDeployment"8"NSDictionary"16l
- ___block_descriptor_32_e65_q24?0"TRIBackgroundMLTaskRecord"8"TRIBackgroundMLTaskRecord"16l
- ___block_descriptor_33_e25_B24?08"NSDictionary"16l
- ___block_descriptor_33_e42_v16?0"TRIExperimentBaseTaskGuardedData"8l
- ___block_descriptor_40_e8_32r_e36_v32?0"TRIBmltDeploymentId"8Q16^B24lr32l8
- ___block_descriptor_40_e8_32r_e39_v16?0"TRIBMLTTaskSupportGuardedData"8lr32l8
- ___block_descriptor_40_e8_32r_e39_v24?0"TRIBackgroundMLTaskRecord"8^B16lr32l8
- ___block_descriptor_40_e8_32r_e45_v16?0"TRIFetchBMLTNotificationGuardedData"8lr32l8
- ___block_descriptor_40_e8_32r_e48_v16?0"TRIDeactivateBMLTDeploymentGuardedData"8lr32l8
- ___block_descriptor_40_e8_32s_e32_B32?0"TRILogNamespace"8Q16^B24ls32l8
- ___block_descriptor_40_e8_32s_e36_v32?0"TRIBmltDeploymentId"8Q16^B24ls32l8
- ___block_descriptor_40_e8_32s_e39_v16?0"TRIBMLTTaskSupportGuardedData"8ls32l8
- ___block_descriptor_40_e8_32s_e39_v24?0"TRIBackgroundMLTaskRecord"8^B16ls32l8
- ___block_descriptor_40_e8_32s_e45_v16?0"TRIFetchBMLTNotificationGuardedData"8ls32l8
- ___block_descriptor_40_e8_32s_e48_v16?0"TRIDeactivateBMLTDeploymentGuardedData"8ls32l8
- ___block_descriptor_40_e8_32s_e52_"TRITaskRunResult"32?0i8B12"NSArray"16"NSDate"24ls32l8
- ___block_descriptor_40_e8_32s_e65_"TRITaskRunResult"32?0i8"NSArray"12B20"TRIExperimentRecord"24ls32l8
- ___block_descriptor_41_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
- ___block_descriptor_41_e8_32bs_e47_v24?0"TRIServerContext"8"<TRITaskQueuing>"16ls32l8
- ___block_descriptor_41_e8_32r_e30_v24?0"TRIRolloutRecord"8^B16lr32l8
- ___block_descriptor_41_e8_32r_e39_v24?0"TRIBackgroundMLTaskRecord"8^B16lr32l8
- ___block_descriptor_48_e8_32s40bs_e39_v24?0"TRIBackgroundMLTaskRecord"8^B16ls32l8s40l8
- ___block_descriptor_48_e8_32s40r_e39_v16?0"TRIBMLTTaskSupportGuardedData"8lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e39_v24?0"TRIBackgroundMLTaskRecord"8^B16ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e39_v24?0"TRIDynamicNamespaceRecord"8^B16ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e48_v16?0"TRIDeactivateBMLTDeploymentGuardedData"8lr40l8s32l8
- ___block_descriptor_48_e8_32s40s_e31_v32?0"TRIFactorLevel"8Q16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e39_v24?0"TRIBackgroundMLTaskRecord"8^B16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e42_v32?0"TRIBackgroundMLTaskRecord"8Q16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s_e49_v24?0"TRIMLRuntimeEvaluationHistoryRecord"8^B16ls32l8
- ___block_descriptor_56_e8_32s40bs48r_e45_v32?0"CKRecordID"8"CKRecord"16"NSError"24ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40r_e39_v24?0"TRIBackgroundMLTaskRecord"8^B16ls32l8r40l8
- ___block_descriptor_56_e8_32s40r_e64_{_PASDBTransactionCompletion_=B}16?0"_PASSqlWriteTransaction"8lr40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e35_v24?0"CKQueryCursor"8"NSError"16ls32l8s48l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e39_v24?0"TRIBackgroundMLTaskRecord"8^B16ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48r_e8_v12?0i8lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e33_v24?0"TRIExperimentRecord"8^B16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e35_v24?0"TRIFBFastFactorLevels"8^B16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e39_v24?0"TRIBackgroundMLTaskRecord"8^B16ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40bs48bs_e47_v24?0"TRIServerContext"8"<TRITaskQueuing>"16ls40l8s48l8s32l8
- ___block_descriptor_64_e8_32s40s48bs56r_e35_v24?0"CKQueryCursor"8"NSError"16lr56l8s32l8s48l8s40l8
- ___block_descriptor_64_e8_32s40s48r_e64_{_PASDBTransactionCompletion_=B}16?0"_PASSqlWriteTransaction"8lr48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56r_e64_{_PASDBTransactionCompletion_=B}16?0"_PASSqlWriteTransaction"8lr56l8s32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56s_e39_v24?0"TRIBackgroundMLTaskRecord"8^B16ls32l8s40l8s48l8s56l8
- ___block_descriptor_65_e8_32s40s48bs56bs_e47_v24?0"TRIServerContext"8"<TRITaskQueuing>"16ls48l8s56l8s32l8s40l8
- ___block_descriptor_65_e8_32s40s48r_e45_v32?0"NSString"8"TRIClientTreatment"16^B24ls32l8s40l8r48l8
- ___block_descriptor_72_e8_32s40s48bs56bs_e47_v24?0"TRIServerContext"8"<TRITaskQueuing>"16ls48l8s56l8s32l8s40l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e64_v40?0Q8"TRIClientBMLTCatalogArtifact"16"NSDate"24"NSError"32lr64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s_e29_v16?0"_PASSqliteStatement"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_76_e8_32s40s48s56s64r_e63_{_PASDBTransactionCompletion_=B}16?0"_PASSqlReadTransaction"8lr64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_77_e8_32s40s48bs56bs_e47_v24?0"TRIServerContext"8"<TRITaskQueuing>"16ls48l8s56l8s32l8s40l8
- ___block_descriptor_80_e8_32s40s48bs56bs64r_e63_{_PASDBTransactionCompletion_=B}16?0"_PASSqlReadTransaction"8ls32l8s40l8s48l8r64l8s56l8
- ___block_descriptor_80_e8_32s40s48bs56bs64r_e63_{_PASDBTransactionCompletion_=B}16?0"_PASSqlReadTransaction"8ls32l8s48l8s40l8s56l8r64l8
- ___block_descriptor_80_e8_32s40s48bs56r64r_e64_{_PASDBTransactionCompletion_=B}16?0"_PASSqlWriteTransaction"8ls48l8s32l8s40l8r56l8r64l8
- ___block_descriptor_80_e8_32s40s48r56r64r72r_e64_{_PASDBTransactionCompletion_=B}16?0"_PASSqlWriteTransaction"8ls32l8r48l8s40l8r56l8r64l8r72l8
- ___block_descriptor_80_e8_32s40s48s56s64r72r_e37_v32?0"NSString"8"NSIndexSet"16^B24lr64l8s32l8s40l8s48l8s56l8r72l8
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e64_{_PASDBTransactionCompletion_=B}16?0"_PASSqlWriteTransaction"8lr72l8s32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_88_e8_32s40s48bs56bs64r72r_e63_{_PASDBTransactionCompletion_=B}16?0"_PASSqlReadTransaction"8ls32l8s48l8s40l8s56l8r64l8r72l8
- ___block_descriptor_88_e8_32s40s48s56r64r72r_e57_v40?0Q8"TRIClientBMLTArtifact"16"NSDate"24"NSError"32ls32l8r56l8r64l8r72l8s40l8s48l8
- ___block_descriptor_88_e8_32s40s48s56s64s72r_e64_{_PASDBTransactionCompletion_=B}16?0"_PASSqlWriteTransaction"8ls32l8s40l8s48l8s56l8s64l8r72l8
- ___block_literal_global.101
- ___block_literal_global.108
- ___block_literal_global.112
- ___block_literal_global.114
- ___block_literal_global.116
- ___block_literal_global.118
- ___block_literal_global.12
- ___block_literal_global.120
- ___block_literal_global.129
- ___block_literal_global.15
- ___block_literal_global.156
- ___block_literal_global.164
- ___block_literal_global.18
- ___block_literal_global.190
- ___block_literal_global.192
- ___block_literal_global.193
- ___block_literal_global.247
- ___block_literal_global.259
- ___block_literal_global.261
- ___block_literal_global.273
- ___block_literal_global.274
- ___block_literal_global.277
- ___block_literal_global.278
- ___block_literal_global.280
- ___block_literal_global.287
- ___block_literal_global.290
- ___block_literal_global.292
- ___block_literal_global.295
- ___block_literal_global.304
- ___block_literal_global.306
- ___block_literal_global.33
- ___block_literal_global.330
- ___block_literal_global.337
- ___block_literal_global.366
- ___block_literal_global.377
- ___block_literal_global.379
- ___block_literal_global.381
- ___block_literal_global.382
- ___block_literal_global.394
- ___block_literal_global.395
- ___block_literal_global.4
- ___block_literal_global.41
- ___block_literal_global.413
- ___block_literal_global.415
- ___block_literal_global.434
- ___block_literal_global.444
- ___block_literal_global.445
- ___block_literal_global.501
- ___block_literal_global.508
- ___block_literal_global.509
- ___block_literal_global.512
- ___block_literal_global.522
- ___block_literal_global.525
- ___block_literal_global.548
- ___block_literal_global.6
- ___block_literal_global.63
- ___block_literal_global.68
- ___block_literal_global.80
- ___block_literal_global.9
- ___block_literal_global.91
- ___block_literal_global.95
- ___block_literal_global.97
- ___getLBFEventManagerClass_block_invoke
- ___getLBFTrialEventClass_block_invoke
- ___getLBFTrialIdentifiersClass_block_invoke
- ___strcpy_chk
- __namespaceDictionaryForClientSelectedNamespace
- _audit_stringLighthouseBitacoraFramework
- _categoricalValueForTriggerEvent
- _descriptor.descriptor.224
- _descriptor.descriptor.231
- _descriptor.descriptor.244
- _descriptor.descriptor.258
- _descriptor.descriptor.264
- _descriptor.descriptor.270
- _descriptor.descriptor.285
- _descriptor.descriptor.294
- _descriptor.descriptor.304
- _descriptor.descriptor.331
- _descriptor.descriptor.343
- _descriptor.descriptor.356
- _descriptor.descriptor.373
- _descriptor.descriptor.380
- _descriptor.descriptor.400
- _descriptor.descriptor.407
- _descriptor.descriptor.419
- _descriptor.descriptor.426
- _descriptor.descriptor.432
- _descriptor.descriptor.439
- _descriptor.descriptor.452
- _descriptor.descriptor.459
- _descriptor.descriptor.466
- _descriptor.fields.212
- _descriptor.fields.225
- _descriptor.fields.232
- _descriptor.fields.245
- _descriptor.fields.271
- _descriptor.fields.286
- _descriptor.fields.295
- _descriptor.fields.305
- _descriptor.fields.332
- _descriptor.fields.344
- _descriptor.fields.357
- _descriptor.fields.374
- _descriptor.fields.381
- _descriptor.fields.401
- _descriptor.fields.408
- _descriptor.fields.420
- _descriptor.fields.433
- _descriptor.fields.440
- _descriptor.fields.453
- _descriptor.fields.460
- _getLBFTrialIdentifiersClass
- _getLBFTrialIdentifiersClass.softClass
- _kTRIEvaluationStatusEntitlement
- _objc_msgSend$_activationTelemetryWithSuccess:bmltRecord:serverContext:
- _objc_msgSend$_activeBMLTIsCompatible:upgradeNCVs:downloadNCVs:
- _objc_msgSend$_activeExperimentFactorLevelsForNamespaceName:
- _objc_msgSend$_allocationTelemetryWithEvent:factorPackSetId:bmltRecord:context:
- _objc_msgSend$_bmltFetchTelemetryIfApplicableWithSuccess:bmltRecord:serverContext:
- _objc_msgSend$_bmltStateForAnalyticsFromStatusType:
- _objc_msgSend$_deactivationTelemetryWithSuccess:bmltRecord:deactivatedFactorPackSetId:serverContext:
- _objc_msgSend$_defaultsAssetURLForFactor:
- _objc_msgSend$_deleteOnDemandAssetsWithFactorNames:treatment:namespace:forRollouts:
- _objc_msgSend$_deleteOnDemandAssetsWithFactorNames:treatment:namespace:forRollouts:inUseAssetDeletionBehavior:
- _objc_msgSend$_enumerateTaskRecordsMatchingWhereClause:bind:transaction:block:
- _objc_msgSend$_evaluateExpressionForDeployment:context:assignment:fpsId:error:
- _objc_msgSend$_experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:serverContext:completion:
- _objc_msgSend$_fetchBMLTNotificationsWithCursor:options:completion:
- _objc_msgSend$_handleExpiredBMLTsWithBMLTDatabase:nextTasks:
- _objc_msgSend$_hasStructurallyValidBMLTs:population:
- _objc_msgSend$_hasValidNCVForBMLT:namespaceDescriptorProvider:
- _objc_msgSend$_isPreviouslyRecordedStateForEvent:
- _objc_msgSend$_isRolloutV1For1PWithExperimentRecord:context:
- _objc_msgSend$_isStructurallyValidBMLT:deployment:namespaceName:populations:deploymentType:deploymentDate:
- _objc_msgSend$_linkAssetWithId:treatmentId:assetStore:factor:forRollouts:
- _objc_msgSend$_migrateProtobufFactorPacksToFlatbuffersUsingPaths:
- _objc_msgSend$_mlruntimeNotifiedTelemetryWithRecords:serverContext:
- _objc_msgSend$_notifyUpdatedShadowEvaluationWithExperimentRecord:context:
- _objc_msgSend$_notifyUpdatedShadowEvaluationsWithDeployments:context:usingTransaction:
- _objc_msgSend$_pathForBMLTDeployment:
- _objc_msgSend$_performSyncXpcWithError:block:
- _objc_msgSend$_processBMLTArtifact:bmltsProcessed:deactivatedBMLTs:targeter:context:taskQueue:
- _objc_msgSend$_processBMLTCatalogArtifact:deactivatedBMLTs:context:
- _objc_msgSend$_purgeRolloutLayerIfNecessaryWithRecord:fromAppContainer:paths:
- _objc_msgSend$_saveNamespacePartitionedTreatmentsForTreatment:forNamespaceNames:forRollouts:
- _objc_msgSend$_saveProtoToFlatbufferFormatWithPaths:namespaceUrl:
- _objc_msgSend$_targetBMLTDeployment:appendingTelemetryToSupport:backgroundMLTaskDatabase:backgroundMLTaskHistoryDatabase:targeter:reportTelemetryToServer:factorPackSetIdToActivate:wasEnrolled:shouldDisenroll:error:
- _objc_msgSend$_taskResultWithStatus:wasEnrolled:reportResults:nextTasks:bmltHistoryDatabase:
- _objc_msgSend$_validRollbackDeploymentsForRollbackExperiment:deploymentIds:
- _objc_msgSend$_validateBMLTNamespaceNCVs:downloadNCVs:context:
- _objc_msgSend$_validateDynamicNamespaceRolloutsWithDatabase:usingPaths:
- _objc_msgSend$_validateRolloutDescriptorsWithNamespaceCompatibilityVersions:usingPaths:
- _objc_msgSend$activateDeployment:withFactorPackSetId:targetingRuleIndex:usingTransaction:
- _objc_msgSend$activeLowLevelNamespaces
- _objc_msgSend$addBackgroundMLTaskWithTaskDeployment:pluginId:status:endDate:artifact:
- _objc_msgSend$addNamespaceId:
- _objc_msgSend$addRecord:usingTransaction:
- _objc_msgSend$addTrialdEvent:identifiers:error:
- _objc_msgSend$allowedLowLevelDefaultLevelsDir
- _objc_msgSend$artifactFromCKRecord:error:
- _objc_msgSend$artifactFromCKRecordResult:withNamespaceDescriptorProvider:container:teamId:requireDeploymentId:completion:
- _objc_msgSend$backgroundMLTaskId
- _objc_msgSend$backgroundMlTask
- _objc_msgSend$backgroundMlTaskId
- _objc_msgSend$backgroundTask
- _objc_msgSend$bmlt
- _objc_msgSend$bmltBatchNotificationId
- _objc_msgSend$bmltCatalog
- _objc_msgSend$bmltDatabase
- _objc_msgSend$bmltDeployment
- _objc_msgSend$bmltDeploymentIdArray
- _objc_msgSend$bmltHistoryDatabase
- _objc_msgSend$bmltId
- _objc_msgSend$categoricalValueForBMLTNotificationEvent:
- _objc_msgSend$clientBackgroundMlTask
- _objc_msgSend$contentIdentifierForBMLTArtifactWithDeployment:
- _objc_msgSend$deactivateTaskDeployment:deactivatedFactorPackSetId:usingTransaction:
- _objc_msgSend$deploymentType
- _objc_msgSend$deploymentWithBackgroundMLTaskId:deploymentId:
- _objc_msgSend$donateTrialIdentifiers:eventType:succeeded:error:
- _objc_msgSend$earliestStartDateForActivationIfInFuture
- _objc_msgSend$emitBMLTEventWithBMLTId:deploymentId:eventType:succeeded:
- _objc_msgSend$emitShadowEvaluationEventWithExperimentId:deploymentId:treatmentId:eventType:succeeded:
- _objc_msgSend$ensureBMLTFields
- _objc_msgSend$enumerateActiveExperimentRecordsWithVisibility:block:
- _objc_msgSend$enumerateActiveRecordsWithVisibility:usingTransaction:block:
- _objc_msgSend$enumerateActiveTasksNotInList:usingTransaction:withBlock:
- _objc_msgSend$enumerateActiveTasksWithBlock:
- _objc_msgSend$enumerateActiveTasksWithTransaction:block:
- _objc_msgSend$enumerateFBFactorPacksForFactorPackSet:usingLegacyPaths:withBlock:
- _objc_msgSend$enumerateRecordsNewerThanDate:block:
- _objc_msgSend$enumerateTaskRecordsMatchingTaskId:transaction:block:
- _objc_msgSend$enumerateTaskRecordsWithBlock:
- _objc_msgSend$evaluation
- _objc_msgSend$evaluationHistoryDatabase
- _objc_msgSend$evaluationId
- _objc_msgSend$factorPackIdForBmltWithNamespaceName:
- _objc_msgSend$factorProviderWithNamespaceName:paths:treatmentLayer:faultOnMissingFactors:shouldLockFactorDirectory:
- _objc_msgSend$factorProviderWithPaths:namespaceName:resolver:
- _objc_msgSend$fetchBMLTCatalogNotificationWithOptions:completion:
- _objc_msgSend$fetchBMLTNotificationWithDeployment:options:completion:
- _objc_msgSend$fetchBMLTNotificationsWithOptions:completion:
- _objc_msgSend$fetchSingleDeploymentWithContext:
- _objc_msgSend$filteredArrayUsingPredicate:
- _objc_msgSend$getAllAllocationStatusesForBMLTId:deploymentId:factorPackSetId:
- _objc_msgSend$groupForBMLTId:
- _objc_msgSend$hasBackgroundMlTask
- _objc_msgSend$hasBackgroundMlTaskId
- _objc_msgSend$hasBmltBatchNotificationId
- _objc_msgSend$hasBmltId
- _objc_msgSend$hasClientBackgroundMlTask
- _objc_msgSend$hasEvaluationId
- _objc_msgSend$hasShadowEvaluation
- _objc_msgSend$hasTaskId
- _objc_msgSend$hashForFactorLevels:
- _objc_msgSend$incompatibleNamespaceNameForBMLT:namespaceDescriptorProvider:
- _objc_msgSend$initWithActivation:
- _objc_msgSend$initWithAllocation:
- _objc_msgSend$initWithBMLTDeployment:
- _objc_msgSend$initWithBMLTDeployment:includeDependencies:taskAttribution:triggerEvent:bmltBatchNotificationIdentifier:
- _objc_msgSend$initWithBMLTDeployment:triggerEvent:bmltBatchNotificationIdentifier:
- _objc_msgSend$initWithBMLTTaskID:deploymentID:
- _objc_msgSend$initWithBackgroundMLTaskId:deploymentId:
- _objc_msgSend$initWithBackgroundTask:populations:deploymentType:deploymentDate:downloadSize:
- _objc_msgSend$initWithBmlt:factorsState:
- _objc_msgSend$initWithBmltCatalog:population:
- _objc_msgSend$initWithBmltDeployment:pluginId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:endDate:artifact:
- _objc_msgSend$initWithBmltDeployment:pluginId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:endDate:namespace:
- _objc_msgSend$initWithDeactivation:
- _objc_msgSend$initWithDeployment:
- _objc_msgSend$initWithDeployment:rampId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:namespaces:isShadow:artifact:
- _objc_msgSend$initWithDeployment:taskAttribution:bmltBatchNotificationIdentifier:
- _objc_msgSend$initWithDeployment:treatmentId:
- _objc_msgSend$initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:counterfactualTreatmentIds:
- _objc_msgSend$initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:isManuallyTargeted:artifact:
- _objc_msgSend$initWithEval:factorsState:
- _objc_msgSend$initWithEvaluation:status:
- _objc_msgSend$initWithEventDate:eventType:backgroundMLTaskId:deploymentId:factorPackSetId:
- _objc_msgSend$initWithExperimentID:deploymentID:treatmentID:
- _objc_msgSend$initWithFactorPackSetId:taskAttribution:bmltDeployment:
- _objc_msgSend$initWithPromise:
- _objc_msgSend$initWithRollout:populations:deploymentDate:downloadSize:
- _objc_msgSend$initWithSchemaVersion:
- _objc_msgSend$initWithServerContextPromise:
- _objc_msgSend$initWithServiceName:allowlistedServerInterface:allowlistedClientInterface:serverInitiatedRequestHandler:allowSystemToUserConnection:interruptionHandler:invalidationHandler:logHandle:
- _objc_msgSend$initWithTaskDeployment:factorPackSetId:taskAttribution:bmltBatchNotificationIdentifier:
- _objc_msgSend$initWithType:evaluationId:date:evalState:
- _objc_msgSend$initWithType:experiment:treatment:rollout:factorPackSet:bmlt:
- _objc_msgSend$isEqualTolowLevelExperiment:
- _objc_msgSend$isExpired
- _objc_msgSend$isShadow
- _objc_msgSend$latestRolloutId
- _objc_msgSend$logAsRollout:
- _objc_msgSend$lowLevelExperimentWithTargetedBundleIds:factorLevelStrings:
- _objc_msgSend$makeDefaultForNamespace:experiment:context:
- _objc_msgSend$mlRuntime
- _objc_msgSend$namespaceDescriptorsBMLTDir
- _objc_msgSend$namespaceDescriptorsRolloutDir
- _objc_msgSend$namespaceIdFromName:
- _objc_msgSend$overlayLevelsFromFactorProvider:
- _objc_msgSend$parentDirForBMLTDeployments
- _objc_msgSend$pathForBMLTDeployment:
- _objc_msgSend$pathsForContainer:asClientProcess:
- _objc_msgSend$pluginId
- _objc_msgSend$population
- _objc_msgSend$registerAllServicesWithPromise:
- _objc_msgSend$registerSystemService
- _objc_msgSend$removeRecordWithDeployment:
- _objc_msgSend$removeTreatmentFromLayer:withNamespaceName:upgradeNCVs:
- _objc_msgSend$removeUnreferencedBMLTDeploymentsWithServerContext:removedCount:
- _objc_msgSend$rewriteBMLTDeployment:targetedFactorPackSetId:
- _objc_msgSend$rolloutCount
- _objc_msgSend$saveToPath:copyAssets:
- _objc_msgSend$seconds
- _objc_msgSend$setActiveFactorPackSetId:activeTargetingRuleIndex:forTaskDeployment:usingTransaction:
- _objc_msgSend$setBackgroundMlTask:
- _objc_msgSend$setBackgroundMlTaskId:
- _objc_msgSend$setBmltBatchNotificationId:
- _objc_msgSend$setBmltId:
- _objc_msgSend$setClientBmltFactorPackSetId:
- _objc_msgSend$setClientBmltId:
- _objc_msgSend$setClientBmltTargetingRuleGroupOrdinal:
- _objc_msgSend$setDeploymentType:
- _objc_msgSend$setEndDate:
- _objc_msgSend$setHashData:
- _objc_msgSend$setHashIncludesDefaults:
- _objc_msgSend$setIdentifyTelemetryAsV1Rollout:
- _objc_msgSend$setLatestRolloutId:
- _objc_msgSend$setRolloutCount:
- _objc_msgSend$setStatus:forTaskDeployment:usingTransaction:
- _objc_msgSend$setTargetedFactorPackSetId:targetedTargetingRuleIndex:forTaskDeployment:usingTransaction:
- _objc_msgSend$shadowEvaluation
- _objc_msgSend$sharedSystemPaths
- _objc_msgSend$shouldPrivacyFilterNamespace:policy:
- _objc_msgSend$siriUserActivitySegment
- _objc_msgSend$storeExperimentEvent:wasNewEvent:
- _objc_msgSend$targetBMLT:factorPackSetId:error:
- _objc_msgSend$targetTaskDeployment:toFactorPackSetId:targetingRuleIndex:usingTransaction:
- _objc_msgSend$taskRecordWithTaskDeployment:
- _objc_msgSend$taskWithBMLTDeployment:factorPackSetId:taskAttribution:bmltBatchNotificationIdentifier:
- _objc_msgSend$taskWithBMLTDeployment:includeDependencies:taskAttribution:triggerEvent:
- _objc_msgSend$taskWithBMLTDeployment:includeDependencies:taskAttribution:triggerEvent:bmltBatchNotificationIdentifier:
- _objc_msgSend$taskWithBMLTDeployment:triggerEvent:
- _objc_msgSend$taskWithBMLTDeployment:triggerEvent:bmltBatchNotificationIdentifier:
- _objc_msgSend$taskWithDeployment:taskAttribution:bmltBatchNotificationIdentifier:
- _objc_msgSend$taskWithFactorPackSetId:taskAttribution:bmltDeployment:
- _objc_msgSend$taskWithTaskAttribution:
- _objc_msgSend$triRemoveDirectoryForPath:isDirectory:error:
- _objc_msgSend$typeOneOfCase
- _objc_msgSend$updateBMLTHistoryDatabaseWithAllocationStatus:forBMLT:deployment:fps:bmltRecord:context:
- _objc_msgSend$updateSavedTreatmentWithTreatmentId:deletingAssetsWithFactorNames:forNamespaceName:forRollouts:
- _objc_msgSend$updateSavedTreatmentWithTreatmentId:deletingAssetsWithFactorNames:forNamespaceName:forRollouts:inUseAssetDeletionBehavior:
- _objc_msgSend$urlForDefaultFactorsWithNamespaceName:
- _registerAllServicesWithPromise:._pasOnceToken2
- _registerSystemService._pasOnceToken3
- _start._pasOnceToken20
CStrings:
+ " ALTER TABLE experiments ADD COLUMN     experimentType INTEGER NOT NULL DEFAULT 0;"
+ " INSERT INTO rolloutsV2 (     rolloutId,     deploymentId,     rampId,     status,     activeFactorPackSetId,     activeTargetingRuleIndex,     targetedFactorPackSetId,     targetedTargetingRuleIndex,     artifact ) VALUES (     :rollout_id,     :deployment_id,     :ramp_id,     :status,     :active_fp_set_id,     :active_targeting_rule_index,     :targeted_fp_set_id,     :targeted_targeting_rule_index,     :artifact );"
+ " INSERT OR IGNORE INTO experiments (     deploymentEnvironment,     experimentId,     deploymentId,     type,     status,     startSecondsFromEpoch,     endSecondsFromEpoch,     artifact,     experimentType ) VALUES (     :deployment_env,     :experiment_id,     :deployment_id,     :type,     :status,     :start_seconds,     :end_seconds,     :artifact,     :experiment_type );"
+ " SELECT     taskType FROM     tasks WHERE     rowid = :task_id LIMIT 1;"
+ " WHERE         (e.experimentId != :experiment_id OR e.deploymentId != :deployment_id)     AND e.type IN (:type_update)     AND e.status IN (:status_enroll, :status_active)     AND e.experimentType = 0     AND (             e.startSecondsFromEpoch IS NULL         OR  e.endSecondsFromEpoch IS NULL         OR  max(:start_seconds, e.startSecondsFromEpoch) < min(:end_seconds, e.endSecondsFromEpoch)     )     AND n.name IN _pas_nsarray(:namespaces)"
+ "%@ failed listening for SIGTERM"
+ "%@ failed to initialize - exiting"
+ "%@ failed to initialize server context"
+ "%@ failed to prepare storage"
+ "%@ launched"
+ "%@.log"
+ "%lld"
+ "%{public}@ %p: %s collectGarbageOlderThanNumScans:%d ignoreRecentlyCreatedAssets:%d dryRun:%d"
+ "%{public}@ %p: %s getOnDemandReferenceCountsPerUserAtGlobalPath:%@"
+ "%{public}@ %p: %s migrateToGlobalAssetStoreIfNeededFromLocalStore:%@"
+ "%{public}@ %p: %s overwriteGlobalActiveFactorProvidersWithNamespaceMap:%@ factorPackMap:%@ rolloutDeploymentMap:%@"
+ "%{public}@ %p: %s referenceMAAutoAssetWithId:%@ futurePath:%@ currentPath:%@ isFileFactor:%d"
+ "%{public}@ %p: %s removeUnreferencedGlobalFactorPacksWithCompletion"
+ "%{public}@ %p: %s saveAssetWithIdentifier:%@ sourcePath:%@ removeSourceOnFailure:%d"
+ "%{public}@ %p: %s saveFactorPackForUserId:%@ toGlobalPath:%@ fromTemporaryPath:%@ factors:%@"
+ "%{public}@ %p: %s updateFactorPackForUserId:%@ atGlobalPath:%@ deletingFactors:%@"
+ "%{public}@ %p: %s updateFactorPackForUserId:%@ atGlobalPath:%@ populatingFactors:%@"
+ "(%d) %{public}@ %p: %s addWithoutRunningForTask:%@ options:%@ completion:"
+ "(%d) %{public}@ %p: %s resumeTaskQueueWithCompletion:"
+ "-[TRIDServer _handleUserSettingsNotificationWithContext:]"
+ "-[TRIInternalServiceRequestHandler activeRolloutInformationWithCompletion:]_block_invoke"
+ "-[TRILogger initWithProjectId:]"
+ "-[TRILogger logWithTrackingId:logLevel:message:]"
+ "-[TRILogger logWithTrackingId:logLevel:message:args:]"
+ "-[TRILogger logWithTrackingId:message:]"
+ "-[TRILogger logWithTrackingId:metric:]"
+ "/System/Library/Frameworks/Accounts.framework/Accounts"
+ "/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount"
+ "/System/Library/PrivateFrameworks/GeoServices.framework/GeoServices"
+ ":experiment_type"
+ "<%@,Siri device aggregation ID rotation date:%@>"
+ "<%@,bundleId:%@,countryCode:%@>"
+ "<%@:%@,%@,%@,%@,r:%d>"
+ "<TRIActiveEnvVarExperiment | targetedBundleIds:%@ factorLevelStrings:%@>"
+ "<TRIClientRolloutArtifact | rollout:%@ populations:%@ deploymentDate:%@ downloadSize:%@ forLaunchDaemon:%@>"
+ "<TRIContentDescriptorUnion | type:%@ experiment:%@ treatment:%@ rollout:%@ factorPackSet:%@>"
+ "<TRIExperimentRecord | deploymentEnvironment:%@ experimentDeployment:%@ treatmentId:%@ factorPackSetId:%@ type:%@ status:%@ startDate:%@ endDate:%@ namespaces:%@ isManuallyTargeted:%@ artifact:%@ experimentType:%@>"
+ "<TRIRolloutRecord | deployment:%@ rampId:%@ activeFactorPackSetId:%@ activeTargetingRuleIndex:%@ targetedFactorPackSetId:%@ targetedTargetingRuleIndex:%@ status:%@ namespaces:%@ artifact:%@>"
+ "@\"<TRIActiveEnvVarNamespacesProviding>\""
+ "@\"<TRIActiveSysctlFactorsProviding>\""
+ "@\"<TRIActiveSysctlNamespacesProviding>\""
+ "@\"<TRIExternalParameterProviding>\""
+ "@\"<TRISysctlWriting>\""
+ "@\"CTXPCServiceSubscriptionContext\""
+ "@\"CoreTelephonyClient\""
+ "@\"NSObject<OS_dispatch_source>\""
+ "@\"TRIActiveEnvVarFactorsWriter\""
+ "@\"TRIEagerExitManager\""
+ "@\"TRISystemInfo\""
+ "@\"TRIXPCInternalAgentToSystemServiceWrapper\""
+ "@16@?0@\"TRIFactorLevel\"8"
+ "@24@0:8^B16"
+ "@32@0:8d16@24"
+ "@40@0:8@16B24i28@32"
+ "@44@0:8@16@24@32C40"
+ "@48@0:8@16i24@28B36@?40"
+ "@52@0:8@16@24@32Q40B48"
+ "@96@0:8i16@20@28@36i44q48@56@64@72B80@84i92"
+ "AFDictationEnablementDidChangeDarwinNotification"
+ "ALTER TABLE experiments DROP COLUMN isShadow;"
+ "ALTER TABLE rolloutsV2 DROP COLUMN isShadow;"
+ "ActiveDictationLocales"
+ "AppleKeyboardsSettingsChangedNotification"
+ "Asset store failed follow-up removal of source at path: %{public}@, error: %{public}@"
+ "Asset store failed to link %{public}@ with identifier: %{public}@ from %{public}@ to %{public}@"
+ "Asset store failed to move dir. asset from: %{public}@ to location for asset: %{public}@. %{public}@"
+ "Attempting to update System info due to cellular parameter change"
+ "B16@?0@\"BMStoreEvent\"8"
+ "B16@?0@\"NSDictionary\"8"
+ "B24@0:8^B16"
+ "B32@0:8@\"NSString\"16@\"NSString\"24"
+ "B32@0:8@\"NSString\"16q24"
+ "B32@0:8@16q24"
+ "Beginning maintenance subtask: %@"
+ "BuildVersion"
+ "CTBundle"
+ "ChipID"
+ "Class getCTBundleClass(void)_block_invoke"
+ "Class getCoreTelephonyClientClass(void)_block_invoke"
+ "Class getTIInputModeControllerClass(void)_block_invoke"
+ "Clear experiment update Biome stream if opted-out"
+ "CloudKit container environment found: %@"
+ "Compact the database"
+ "Considering potential sysctl record %@"
+ "CoreTelephonyClient"
+ "CoreTelephonyClientCarrierBundleDelegate"
+ "CoreTelephonyClientDataDelegate"
+ "CoreTelephonyClientSubscriberDelegate"
+ "DELETE FROM experiments WHERE isShadow=1;"
+ "DELETE FROM rolloutsV2 WHERE isShadow=1;"
+ "DROP TABLE IF EXISTS backgroundMlTaskHistory;"
+ "DROP TABLE IF EXISTS backgroundMlTasks;"
+ "DROP TABLE IF EXISTS mlRuntimeEvaluationStatusHistory;"
+ "DSLPublisher"
+ "Data to be persisted for Maps country code was nil, encountered: %@"
+ "Data to be persisted for dictation locales was nil"
+ "Data to be persisted for maps bucket id was nil"
+ "Deactivate expired experiments"
+ "Deal with dynamic namespaces from uninstalled apps"
+ "Deferral requested during maintenance task before running subtask: %@"
+ "DeviceChipId"
+ "DeviceHardwareModel"
+ "DeviceSystemId"
+ "Dictation Enabled"
+ "Dictation is not enabled. Returning an empty locale array."
+ "DictationLanguagesEnabled"
+ "Discovered %i experiment records for experiment with Id: %@ and error: %@"
+ "Eager exit timer already counting down, coalescing notification."
+ "Eager exit: Task queue has been empty for %f seconds. Triald is idle and will exit."
+ "Eager exit: attempting a clean exit of triald"
+ "Eager exit: task queue has %lu tasks in progress, cancelling eager exit."
+ "Encountered SQLITE_CONSTRAINT error.\n error description: %@"
+ "EnvVarNamespacesProviding"
+ "Error creating persistent identifier folder: %@"
+ "Error deleting persistent identifier file: %@"
+ "Error reading Siri.AnalyticsIdentifiers.UserAggregationId data stream %{public}@"
+ "Error writing persistent identifier: %@"
+ "Error: systemInfo is null."
+ "Experiment - Treatment -  Deployment: %@ -  %@ - %d. Ignoring metric for deactivation transition due to not having activated before."
+ "Experiment - Treatment -  Deployment: %@ -  %@ - %d. There was nothing to log for state: %d"
+ "Experiment not compatible with the namespaces on the device %{public}@."
+ "Experiment update notification missing end date. ID: %{public}@"
+ "Expire old experiment history records"
+ "Expire old rollout history records"
+ "Factory"
+ "Failed to derive file system encoding of symlin: \"%{public}@\" in managed directory: \"%{public}@\""
+ "Failed to move ineligible experiment %@.%u to finished after emergency rollback"
+ "Failed to resolve factor pack set's legacy (id-based) directory."
+ "Failed to resolve id based location for factor pack %{public}@ with namespace %{public}@."
+ "Failed to update status for experiment (%@, %@) to finished"
+ "Failed to write factor pack set to the (optional) id-based directory."
+ "Fetched Carrier bundle identifier from CoreTelephony: %{public}@"
+ "Fetched Carrier country code from CoreTelephony: %{public}@"
+ "HWModelStr"
+ "Integration test logger wrote: id %@, task name %@, to: %@"
+ "Invalid event body for Siri.AnalyticsIdentifiers.UserAggregationId data stream"
+ "Invalid type for Siri.AnalyticsIdentifiers.UserAggregationId event %@"
+ "Known factors: %@"
+ "KnownFactors"
+ "Limited Carry Profile %@ is malformed. It is providing NamespaceName and NamespaceName array."
+ "Limited Carry Profile %@ is malformed. NamespaceName and NamespaceName array are both missing."
+ "Logger"
+ "Logging log event: %@"
+ "Maps: bucket id: %@"
+ "MapsBucketId"
+ "MapsDeviceCountryCode"
+ "Marking experiment:%{public}@ as ineligible"
+ "May 24 2025"
+ "Missing serialized value for TRIClientRolloutArtifact.forLaunchDaemon"
+ "Moving inactive experiment %@.%u to finished after emergency rollback"
+ "Namespace %@ targeting bundle ids: %@ is not considered as a launchd delievered experiment due to presence of kTRISysctlExperimentMagicBundleIdentifier"
+ "NamespaceNames"
+ "No cached external parameters."
+ "No persisted Maps Bucket ID found for key: %{public}@"
+ "No persisted Maps country code found"
+ "No persisted dictation locales found"
+ "No treatment Id for experiment with experiment id: %@"
+ "Persisted Maps Bucket Id: %@"
+ "Persistent identifier file read error: %@"
+ "ProductType"
+ "Prune obsolete events from Biome stream"
+ "Publish sysctl factors"
+ "Purgeable experiment candidate has no namespace."
+ "RC_SEED_BUILD is false. Not considering device as enrolled in beta program"
+ "RC_SEED_BUILD is true. Considering device as enrolled in beta program"
+ "Reading currentEnvironment from NSUserDefaults: Development"
+ "Reading currentEnvironment from NSUserDefaults: InternalTesting"
+ "Reading currentEnvironment from NSUserDefaults: Production"
+ "Reading currentEnvironment from NSUserDefaults: SQLiteMock"
+ "Reading currentEnvironment from NSUserDefaults: UAT"
+ "Reading currentEnvironment from NSUserDefaults: Unknown"
+ "Reading currentEnvironment from NSUserDefaults: other (%@), using Unknown"
+ "Reading currentPopulation from NSUserDefaults: BETA_PROGRAM"
+ "Reading currentPopulation from NSUserDefaults: GENERAL_PUBLIC"
+ "Reading currentPopulation from NSUserDefaults: INTERNAL"
+ "Reading currentPopulation from NSUserDefaults: LIMITED_CARRY"
+ "Reading currentPopulation from NSUserDefaults: ORGANIZATION"
+ "Reading currentPopulation from NSUserDefaults: POPULATION_UNKNOWN"
+ "Reading currentPopulation from NSUserDefaults: other (%@), using POPULATION_UNKNOWN"
+ "Reading params from cache: %@"
+ "Received call for rollout notifications from triald_system on macOS, which is unsupported."
+ "Received delegate callback: carrierBundleChange"
+ "Received delegate callback: preferredDataSimChanged"
+ "Received delegate callback: subscriberCountryCodeDidChange"
+ "Record daily active experiments"
+ "Refusing to write an active factor %@ which doesn't match a pre-declared known factor."
+ "Reload envvar-based factors in launchd"
+ "Remove unused experiment info, treatments, and assets"
+ "Retargeting is being suppressed for expired and ineligible experiment: %@"
+ "Retrieved nil serialized value for nonnull TRIActiveEnvVarExperiment.factorLevelStrings"
+ "Retrieved nil serialized value for nonnull TRIActiveEnvVarExperiment.targetedBundleIds"
+ "Set sysctl named %@ to %@."
+ "Set up TRICellularParameterManager"
+ "Siri.AnalyticsIdentifiers.UserAggregationId"
+ "SiriDeviceAggregationIdRotationDate"
+ "Skipping %@ for sysctl namespace consideration because it doesn't have exactly one namespace"
+ "Skipping %@ for sysctl namespace consideration because we had no experiment definition"
+ "Skipping experiment %{public}@ while looking for purgeable experiments since its does not have assets on device"
+ "Skipping experiment %{public}@ while looking for purgeable experiments since its not active"
+ "Skipping experiment %{public}@ with no namespaces."
+ "Subscribed sink already exists. Replacing: %@"
+ "Subscribing to events from Biome stream: %@"
+ "Synchronise push connections"
+ "Synchronous XPC message failed with error %@"
+ "SysConfig is stale, leaving population unset"
+ "SysctlNamespacesProviding"
+ "System info update successful"
+ "T@\"<TRITaskQueuing>\",W,N,V_taskQueue"
+ "T@\"NSArray\",&,N,V_enabledInputModeIdentifiers"
+ "T@\"NSArray\",R,N,V_logHandlers"
+ "T@\"NSDate\",&,N,V_siriDeviceAggregationIdRotationDate"
+ "T@\"NSDate\",R,N"
+ "T@\"NSNumber\",&,N,V_mapsBucketId"
+ "T@\"NSString\",&,N,V_aneVersion"
+ "T@\"NSString\",&,N,V_carrierBundleIdentifier"
+ "T@\"NSString\",&,N,V_carrierCountryIsoCode"
+ "T@\"NSString\",&,N,V_iCloudIdentifier"
+ "T@\"NSString\",R,N,V_sysctlName"
+ "T@?,R,N,V_block"
+ "TB,N,V_forLaunchDaemon"
+ "TB,N,V_hasAne"
+ "TB,N,V_isAutomatedTestDevice"
+ "TB,N,V_isDiagnosticsAndUsageEnabled"
+ "TB,N,V_isEnrolledInBetaProgram"
+ "TB,N,V_logUserKeyboardEnabledInputMode"
+ "TB,N,V_logUserSettingsLanguageCode"
+ "TB,N,V_logUserSettingsRegionCode"
+ "TB,R,N,V_forLaunchDaemon"
+ "TIInputModeController"
+ "TRIActiveEnvVarExperiment"
+ "TRIActiveEnvVarExperimentOCNTErrorDomain"
+ "TRIActiveEnvVarFactorStringBuilder"
+ "TRIActiveEnvVarFactorStringBuilder.m"
+ "TRIActiveEnvVarFactorsPublisher"
+ "TRIActiveEnvVarFactorsWriter"
+ "TRIActiveEnvVarNamespacesProviding"
+ "TRIActiveLaunchdDeliveredExperimentsReader"
+ "TRIActiveSysctlFactorsProvider"
+ "TRIActiveSysctlFactorsProviding"
+ "TRIActiveSysctlFactorsPublisher"
+ "TRIActiveSysctlNamespacesProviding"
+ "TRIBiomeDataStreamProvider"
+ "TRICKServerEnvironmentReader"
+ "TRICellularParameterGuardedData"
+ "TRICellularParameterManager"
+ "TRICellularParameterManager failed to update system info"
+ "TRICellularParameterManager.m"
+ "TRIDServer: Maps Bucket ID changed, queueing retargeting"
+ "TRIDServer: Maps Country Code changed, queueing retargeting (%@ -> %@)"
+ "TRIDServer: Maps Experiments Change Notification received"
+ "TRIDatabase calling migration_dropBMLTDatabasesAndShadowEvaluationRolloutsAndExperiments for database version 25"
+ "TRIDatabase calling migration_dropShadowEvaluationDatabase for database version 24"
+ "TRIDatabase encountered error while dropping the backgroundMlTaskHistory table upon migration to DB version 25"
+ "TRIDatabase encountered error while dropping the backgroundMlTasks table upon migration to DB version 25"
+ "TRIDatabase encountered error while dropping the mlRuntimeEvaluationStatusHistory table upon migration to DB version 24"
+ "TRIDatabase encountered error while dropping the shadow evaluation column from the experiments table upon migration to DB version 25"
+ "TRIDatabase encountered error while dropping the shadow evaluation column from the rolloutsV2 table upon migration to DB version 25"
+ "TRIDatabase encountered error while dropping the shadow evaluation entries from the experiments table upon migration to DB version 25"
+ "TRIDatabase encountered error while dropping the shadow evaluation entries from the rolloutsV2 table upon migration to DB version 25"
+ "TRIDatabase migration_dropBMLTDatabasesAndShadowEvaluationRolloutsAndExperiments dropped the backgroundMlTaskHistory table for database version 25"
+ "TRIDatabase migration_dropBMLTDatabasesAndShadowEvaluationRolloutsAndExperiments dropped the backgroundMlTasks table for database version 25"
+ "TRIDatabase migration_dropBMLTDatabasesAndShadowEvaluationRolloutsAndExperiments dropped the shadow evaluation column from the experiments table for database version 25"
+ "TRIDatabase migration_dropBMLTDatabasesAndShadowEvaluationRolloutsAndExperiments dropped the shadow evaluation column from the rolloutsV2 table for database version 25"
+ "TRIDatabase migration_dropBMLTDatabasesAndShadowEvaluationRolloutsAndExperiments dropped the shadow evaluation entries from the experiments table for database version 25"
+ "TRIDatabase migration_dropBMLTDatabasesAndShadowEvaluationRolloutsAndExperiments dropped the shadow evaluation entries from the rolloutsV2 table for database version 25"
+ "TRIDatabase migration_dropShadowEvaluationDatabase dropped the mlRuntimeEvaluationStatusHistory table for database version 24"
+ "TRIEagerExitManager"
+ "TRIExternalParameterGuardedData"
+ "TRIExternalParameterManager"
+ "TRIExternalParameterProviding"
+ "TRIInternalAgentToSystemServiceRequestHandler"
+ "TRIKnownEnvVarFactorsReader"
+ "TRILogger"
+ "TRIMaintenanceSubTask"
+ "TRIMapsBucketIdChangeProcessor"
+ "TRIPETLogHandler"
+ "TRISysctlFactorLevel"
+ "TRISysctlWriter"
+ "TRISysctlWriting"
+ "TRISystemConfiguration"
+ "TRISystemInfo"
+ "TRISystemInfo.m"
+ "TRISystemInfoGuardedData"
+ "TRIXPCInternalAgentToSystemServiceListener"
+ "TRIXPCInternalAgentToSystemServiceProtocol"
+ "TRIXPCInternalAgentToSystemServiceWrapper"
+ "Target of reverse-link \"%{public}@\" resolves to an empty string."
+ "Task queue empty notification received. Counting down towards an eager exit (~%f seconds)."
+ "Ti,R,N,V_experimentType"
+ "Tq,N,V_appleIntelligenceState"
+ "Tq,R,N,V_level"
+ "TrialXP-"
+ "TrialXP-463"
+ "Unable to archive dictation locales from Trial persisted storage, encountered: %@"
+ "Unable to archive maps bucket id from Trial persisted storage, encountered: %@"
+ "Unable to fetch Maps Bucket Id: %{public}@"
+ "Unable to find namespace id for namespace name: %@. This is expected for self-service namespaces with exclusively namespace names"
+ "Unable to get carrier bundle identifier: %{public}@"
+ "Unable to get carrier country code: %{public}@"
+ "Unable to get last known mobile subscriber country code: %{public}@"
+ "Unable to get preferred data subscription context"
+ "Unable to get preferred data subscription context: %{public}@"
+ "Unable to load soft-linked CTBundle class"
+ "Unable to load soft-linked CoreTelephonyClient class"
+ "Unable to load soft-linked TIInputModeController class"
+ "Unable to load soft-linked _ANEDeviceInfo class"
+ "Unable to process deprecated rollout V1 experiment artifact"
+ "Unable to read 'kern.hv_vmm_present' code: %d"
+ "Unable to remove task from task table due to SQLite error: %@"
+ "Unable to set sysctl named %@ to %@. Error: %s"
+ "Unable to unarchive Maps country code from Trial persisted storage, encountered: %@"
+ "Unable to unarchive dictation locales from Trial persisted storage, encountered: %@"
+ "Unable to unarchive maps bucket id from Trial persisted storage, encountered: %@"
+ "Unable to update on-disk experiment deployment directory."
+ "Unarchived unexpected class for TRIActiveEnvVarExperiment key \"factorLevelStrings\" (expected %@, decoded %@)"
+ "Unarchived unexpected class for TRIActiveEnvVarExperiment key \"targetedBundleIds\" (expected %@, decoded %@)"
+ "UniqueDeviceID"
+ "Updating iCloudID using Alt. DSID of account: %@"
+ "User Settings notification relevancy: %d. Siri locale changed: %d, Siri enablement changed: %d Dication: %d"
+ "UserAggregationId rotation date is null, eventBody: %@"
+ "Using population override: %d"
+ "V1 Rollouts are no longer supported: %{public}@"
+ "WHERE activeFactorPackSetId IS NOT NULL"
+ "Wrote factor pack %{public}@ --> %{public}@ (legacy id-based directory)."
+ "[TRIExperimentPostLaunchEvent eventWithEventType:TRIInternalExperimentAllocationStatusTypeActivatedTreatment experimentRecord:record]"
+ "[TRIExperimentPostLaunchEvent eventWithEventType:TRIInternalExperimentAllocationStatusTypeFetchedTreatment experimentRecord:record]"
+ "_ANEDeviceInfo"
+ "__tri_sysctl_experiment"
+ "_activeExperimentDeploymentsForRollbackExperiment:deploymentIds:"
+ "_appleIntelligenceState"
+ "_block"
+ "_cachedDeviceIdentifier"
+ "_checkTreatmentBasedExperimentForPurgeables:experimentAssets:experimentHasNamespaceWithEagerFactors:experimentHasPurgeableNamespace:overriddenFactors:record:shouldGenerateAssetPaths:storage:"
+ "_deleteOnDemandAssetsWithFactorNames:treatment:namespace:"
+ "_deleteOnDemandAssetsWithFactorNames:treatment:namespace:inUseAssetDeletionBehavior:"
+ "_dispatchLogEvent:"
+ "_dispatchQueueForCarrierInfoGathering"
+ "_eagerExitManager"
+ "_eagerExitQueue"
+ "_eagerExitSource"
+ "_enabledInputModeIdentifiers"
+ "_experimentRecord:matchesExperimentId:oneOfDeploymentIds:"
+ "_experimentRecordsWithDeploymentEnvironments:serverContext:completion:"
+ "_factorsProvider"
+ "_fetchCarrierBundleIdentifier:"
+ "_fetchCarrierCountryIsoCode:"
+ "_fetchSiriDeviceAggregationIdRotationDate"
+ "_forLaunchDaemon"
+ "_getLogger"
+ "_getSiriDeviceAggregationIdRotationDate"
+ "_handleUserSettingsNotificationWithContext:"
+ "_iCloudIdentifier"
+ "_incrementedLogEventCount"
+ "_ineligibleExperimentDeploymentsForRollbackExperiment:deploymentIds:"
+ "_isAutomatedTestDevice"
+ "_isDiagnosticsAndUsageEnabled"
+ "_isEnrolledInBetaProgram"
+ "_isExperimentEligibleWithArtifact:context:"
+ "_isSeedBuild"
+ "_isValidNextStateForEvent:"
+ "_isVirtualMachine"
+ "_level"
+ "_levelAsString:"
+ "_linkAssetWithId:treatmentId:assetStore:factor:"
+ "_logHandlers"
+ "_logUserKeyboardEnabledInputMode"
+ "_logUserSettingsLanguageCode"
+ "_logUserSettingsRegionCode"
+ "_loggingQueue"
+ "_mapsBucketId"
+ "_paramProvider"
+ "_persistentDeviceIdentifierPath"
+ "_persistentSystemInfoPath"
+ "_plistPath"
+ "_projectId"
+ "_providerQueue"
+ "_readParametersFromFile"
+ "_readSiriDeviceAggregationIdRotationDateFromEvent:"
+ "_saveNamespacePartitionedTreatmentsForTreatment:forNamespaceNames:"
+ "_serviceName"
+ "_sharedCovariatesFromConfiguration:"
+ "_sharedSystemInfo"
+ "_shouldSubscribeWithWaking"
+ "_singularAndUniqueNamespaceInRecord:alreadyMapped:"
+ "_siriDeviceAggregationIdRotationDate"
+ "_streamForIdentifier:eventHandler:"
+ "_streamIdentifierstoSubscribedSinks"
+ "_subscribeForStreamIdentifier:eventHandler:"
+ "_subscriptionContext"
+ "_sysEnabledInputModeIdentifiers"
+ "_sysIsEnrolledInBetaProgram"
+ "_sysctlName"
+ "_sysctlWriter"
+ "_systemInfoWithIsStale:"
+ "_telephonyClient"
+ "_token"
+ "_trialVersion"
+ "_trialdSystemOnly"
+ "_unsubscribeAllDataStreams"
+ "_updateSystemInfo"
+ "_updateSystemInfo:"
+ "_userSpecificCovariatesFromConfiguration:"
+ "_writeFactorPackToLegacyPath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:"
+ "_writeIdBasedFactorPack:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:"
+ "_writeParametersToFile"
+ "aa_altDSID"
+ "aa_primaryAppleAccount"
+ "activatedEventWithExperimentRecord:"
+ "activeDictationLocales"
+ "activeEnvVarNamespaces"
+ "activeExperimentInformationWithEnvironments: %{public}@"
+ "activeExperimentInformationWithEnvironments:completion:"
+ "activeRolloutInformationWithCompletion:"
+ "activeSysctlFactorLevels"
+ "activeSysctlNamespaces"
+ "addNamespaceName:"
+ "addTaskAfterOperationsFinish:"
+ "addWithoutRunningForTask:options:completion:"
+ "addWithoutRunningTask:options:error:"
+ "allocationEventWithTriple:isDynamicEnrollment:environment:namespaces:"
+ "allowEnvVarDefaultLevelsDir"
+ "anbrActivationState:enabled:"
+ "anbrBitrateRecommendation:bitrate:direction:"
+ "aneSubType"
+ "application-identifier"
+ "artifactFromCKRecordResult:withContainer:teamId:requireDeploymentId:completion:"
+ "artifactWithRollout:populations:deploymentDate:downloadSize:forLaunchDaemon:"
+ "authTokenChanged:"
+ "automatedDeviceGroup"
+ "bundleIdentifier"
+ "called deprecated method %s"
+ "callerBundleId"
+ "callerIsRunningFromSystemContext"
+ "canonicalLanguageIdentifierFromString:"
+ "carrierBundleChange:"
+ "cloudIdentifier"
+ "com.apple.GeoServices.countryCodeChanged"
+ "com.apple.GeoServices.experimentsChanged"
+ "com.apple.keyboard.preferences"
+ "com.apple.trial.%@"
+ "com.apple.trial.PublishSysctlOnTrialdLaunchComplete"
+ "com.apple.trial.TrialdInitServerContextDone"
+ "com.apple.trial.biome-provider"
+ "com.apple.trial.system-config.carrier"
+ "com.apple.trial.system.status"
+ "com.apple.triald.ExternalParameterChangeQueue"
+ "com.apple.triald.persisted.Maps.BucketId"
+ "com.apple.triald.persisted.Maps.DeviceCountryCode"
+ "com.apple.triald.persisted.activeDictationLocales"
+ "com.apple.triald.population.override"
+ "com.apple.triald.system.from-agent"
+ "com.apple.triald.system.namespace-management"
+ "connectionActivationError:connection:error:"
+ "connectionAvailability:availableConnections:"
+ "connectionStateChanged:connection:dataConnectionStatusInfo:"
+ "copyBundleIdentifier:bundleType:error:"
+ "copyLastKnownMobileSubscriberCountryCode:error:"
+ "copyMobileSubscriberIsoCountryCode:error:"
+ "copyWithReplacementExperimentType:"
+ "copyWithReplacementForLaunchDaemon:"
+ "countryCode"
+ "createDeviceIdentifierWithPath:"
+ "currentCalendar"
+ "currentDataServiceDescriptorChanged:"
+ "currentDataSimChanged:"
+ "currentLocale"
+ "currentPopulation"
+ "dataRoamingSettingsChanged:status:"
+ "dataSettingsChanged:"
+ "dataStatus:dataStatusInfo:"
+ "dateByAddingComponents:toDate:options:"
+ "dateWithTimeIntervalSince1970:"
+ "decodeBoolForKey:"
+ "decodeIntegerForKey:"
+ "defaultBundleChange"
+ "defaultStore"
+ "deleteDeviceIdentifier"
+ "deleteDeviceIdentifierWithPath:"
+ "denormalizedEvent"
+ "deviceChipId"
+ "deviceHardwareModel"
+ "deviceInfoForQuestion:"
+ "deviceSystemId"
+ "dictionaryWithContentsOfURL:error:"
+ "didDetectSimDeactivation:info:"
+ "dispatchTimeWithSecondsFromNow:"
+ "effectiveFrom"
+ "encodeBool:forKey:"
+ "encodeInteger:forKey:"
+ "encodeWithCoder: enabledInputModeIdentifiers is nil"
+ "enumerateActiveExperimentRecordsWithBlock:"
+ "enumerateActiveRecordsUsingTransaction:block:"
+ "envVarExperimentWithTargetedBundleIds:factorLevelStrings:"
+ "eventWithTrackingId:projectId:"
+ "exitTrialdCleanly"
+ "experimentHistoryRecordsWithLimit:newerThanDate:deploymentEnvironment:completion:"
+ "experimentIdentifiers"
+ "experimentIdentifiersWithNamespaceName:"
+ "experimentRecordsWithDeploymentEnvironments:completion:"
+ "externalParamManager"
+ "externalParametersFile"
+ "factorProviderWithPaths:namespaceName:resolver:faultOnMissingInstalledFactors:"
+ "failed to create directory for path %@ -- %@"
+ "failed to encode system info -- %@"
+ "failed to handle sysctl publish on launch - triald failed initialization"
+ "failed to parse external parameter dictionary from file: %@ (%@)"
+ "failed to process %@ - %@ failed initialization"
+ "failed to process %@ - server context is null"
+ "failed to read system info from file %@: %@"
+ "failed to to read Biome stream: %@"
+ "failed to write system info to path %@ -- %@"
+ "fetchBucketID:"
+ "fetchedEventWithExperimentRecord:"
+ "fields"
+ "file"
+ "filterWithIsIncluded:"
+ "forLaunchDaemon"
+ "getPreferredDataSubscriptionContextSync:"
+ "guardedCarrierBundleIdentifier"
+ "guardedCarrierCountryIsoCode"
+ "guardedSiriDeviceAggregationIdRotationDate"
+ "handleTaskQueueEmptyNotificationWithCooldown:"
+ "hasANE"
+ "hasForLaunchDaemon"
+ "hasTrialSystemTelemetry"
+ "hasValidNamespacesWithError:"
+ "hostingProcessIsTriald"
+ "hostingProcessName"
+ "i24@0:8@\"NSNumber\"16"
+ "i24@0:8q16"
+ "iCloudIdentifier"
+ "iOS"
+ "info"
+ "initForTrialdSystem:"
+ "initFromSystemWithFactorProvider:"
+ "initWithActiveNamespacesProvider:factorLevelsRetriever:"
+ "initWithBundleType:"
+ "initWithClient:projectId:"
+ "initWithCoder: enabledInputModeIdentifiers is nil"
+ "initWithDeployment:rampId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:namespaces:artifact:"
+ "initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:experimentType:counterfactualTreatmentIds:"
+ "initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isManuallyTargeted:artifact:experimentType:"
+ "initWithExitCooldown:monitoringTaskQueue:"
+ "initWithIdentifier:targetQueue:waking:"
+ "initWithName:subtaskBlock:"
+ "initWithProjectId:"
+ "initWithProjectId:logHandlers:"
+ "initWithPromise:forSystem:"
+ "initWithProvider:paths:"
+ "initWithQueue:"
+ "initWithRollout:populations:deploymentDate:downloadSize:forLaunchDaemon:"
+ "initWithSchemaVersion:forUser:forTrialdSystem:"
+ "initWithServerContextPromise:forSystem:"
+ "initWithServiceName:connectionOptions:allowlistedServerInterface:allowlistedClientInterface:serverInitiatedRequestHandler:allowSystemToUserConnection:interruptionHandler:invalidationHandler:logHandle:"
+ "initWithSuiteName:"
+ "initWithSysctlFactorsProvider:sysctlWriter:"
+ "initWithSysctlName:level:"
+ "initWithType:experiment:treatment:rollout:factorPackSet:"
+ "integerForKey:"
+ "internetConnectionActivationError:"
+ "internetConnectionAvailability:"
+ "internetConnectionStateChanged:"
+ "internetDataStatus:"
+ "internetDataStatusBasic:"
+ "isBetaUser"
+ "isEnrolledInBetaProgram"
+ "isEqualToenvVarExperiment:"
+ "isOptedOutOfExperimentationWithCompletion:"
+ "isStale"
+ "issuing sandbox extension (of type: %d) for path %s"
+ "kern.hv_vmm_present"
+ "last"
+ "loadSystemInfo"
+ "logEvent:"
+ "logEventId"
+ "logMessage:"
+ "logMessage:subGroup:"
+ "logTimeFromDate:"
+ "logUserKeyboardEnabledInputMode"
+ "logUserSettingsLanguageCode"
+ "logUserSettingsRegionCode"
+ "logWithMLRuntimeDimensions:metrics:factorState:"
+ "logWithNamespaceName:metrics:dimensions:"
+ "logWithProjectNameAndTrackingId:metrics:dimensions:trialSystemTelemetry:"
+ "logWithTrackingId:logLevel:message:"
+ "logWithTrackingId:logLevel:message:args:"
+ "logWithTrackingId:message:"
+ "logWithTrackingId:metric:"
+ "logWithTrackingId:metric:dimensions:"
+ "logWithTrackingId:metrics:dimensions:"
+ "macOSLaunchDaemonExperimentation"
+ "maps: bucket id: %@"
+ "mapsBucketId"
+ "mapsBucketId != nil"
+ "mapsDeviceCountryCode"
+ "messageWithOneofField:withName:"
+ "migration_dropBMLTDatabasesAndShadowEvaluationRolloutsAndExperiments"
+ "migration_dropShadowEvaluationDatabase"
+ "none"
+ "nrSliceAppStateChanged:status:trafficDescriptors:"
+ "nrSlicedRunningAppStateChanged:"
+ "oneofs"
+ "operatingSystemVersion"
+ "operatorBundleChange:"
+ "optInApple"
+ "performSyncXPCWithError:block:"
+ "persistActiveDicationLocales:"
+ "persistMapsBucketId:"
+ "persistMapsDeviceCountryCode:"
+ "persistedActiveDicationLocales"
+ "persistedMapsBucketId"
+ "persistedMapsDeviceCountryCode"
+ "preferredDataServiceDescriptorChanged:"
+ "preferredDataSimChanged:"
+ "prlVersionDidChange:version:"
+ "processMapsBucketIdChangeIfNecessaryForBucketId:withServerContext:withTaskQueue:"
+ "projectNameFromId:"
+ "publishSysctlFactors"
+ "publisher"
+ "q24@0:8@16"
+ "readDeviceIdentifierWithPath:"
+ "readLastDataStreamEventForIdentifier:eventHandler:"
+ "readLastDataStreamEventForIdentifier:withFilter:eventHandler:"
+ "recordWithDeployment:rampId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:namespaces:artifact:"
+ "recordWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isManuallyTargeted:artifact:experimentType:"
+ "regDataModeChanged:dataMode:"
+ "registerAgentToSystemService"
+ "registerTrialServicesWithPromise:"
+ "registerTrialSystemServicesWithPromise:"
+ "reloadDeviceId"
+ "removeTaskWithId:cleanupBlock: failed to remove task with taskId %@ and type %d"
+ "removing"
+ "requiresLogging"
+ "resetDeviceIdentifier"
+ "resumeTaskQueueWithCompletion:"
+ "resumeTaskQueueWithError:"
+ "rolloutAllocationStatusWithCompletion:"
+ "saveToFile:"
+ "server context not fully initialised"
+ "serviceDisconnection:status:"
+ "servingNetworkChanged:"
+ "setAneVersion:"
+ "setAppleIntelligenceState:"
+ "setCarrierBundleIdentifier:"
+ "setCarrierCountryIsoCode:"
+ "setClientProjectId:"
+ "setDay:"
+ "setDenormalizedEvent:"
+ "setDeviceClass:"
+ "setDeviceIdentifier:"
+ "setDeviceIdentifier:path:"
+ "setDeviceLogTime:"
+ "setEnabledInputModeIdentifiers:"
+ "setForLaunchDaemon:"
+ "setHasAne:"
+ "setICloudIdentifier:"
+ "setIsAutomatedTestDevice:"
+ "setIsDiagnosticsAndUsageEnabled:"
+ "setIsEnrolledInBetaProgram:"
+ "setLogEventId:"
+ "setLogUserKeyboardEnabledInputMode:"
+ "setLogUserSettingsLanguageCode:"
+ "setLogUserSettingsRegionCode:"
+ "setMapsBucketId:"
+ "setMlruntimeDimensions:"
+ "setOsBuild:"
+ "setProcessEventIndex:"
+ "setProjectId:"
+ "setShouldSubscribeWithWaking:"
+ "setSiriDeviceAggregationIdRotationDate:"
+ "setTargetedPopulation:"
+ "setTrialSystemTelemetry:"
+ "setUserKeyboardEnabledInputModeIdentifiers:"
+ "setUserSettingsBcp47DeviceLocale:"
+ "setValue:"
+ "setVersionTag:"
+ "sharedConfiguration"
+ "sharedPaths"
+ "shortLabelsDidChange"
+ "shouldSetForLaunchDaemonFlagFromFields:experiment:error:"
+ "shouldSetForLaunchDaemonFlagFromFields:rollout:error:"
+ "simLockSaveRequestDidComplete:success:"
+ "simPinChangeRequestDidComplete:success:"
+ "simPinEntryErrorDidOccur:status:"
+ "simPukEntryErrorDidOccur:status:"
+ "simStatusDidChange:status:"
+ "sinkWithCompletion:receiveInput:"
+ "softlink:o:path:/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony"
+ "softlink:o:path:/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine"
+ "softlink:r:path:/System/Library/PrivateFrameworks/TextInput.framework/TextInput"
+ "state"
+ "storeExperimentEvent:isValidTransition:"
+ "storedDeviceIdentifier"
+ "streamWithIdentifier:error:"
+ "stringForCurrentProcessEntitlement:"
+ "subscribeDataStreamForIdentifier:eventHandler:"
+ "subscribeOn:"
+ "subscriberCountryCodeDidChange:"
+ "successfully wrote factor pack set to the (optional) id-based directory."
+ "sysctlName"
+ "systemDataFile"
+ "systemInfo"
+ "systemInfoFromFile:"
+ "systemInteropDirectory"
+ "taskTypeForTaskWithId:"
+ "tetheringStatus:"
+ "tetheringStatus:connectionType:"
+ "treatmentValidForExperimentWithID:treatmentID:"
+ "treatmentValidForExperimentWithId:treatmentId:completion:"
+ "trialdTaskName"
+ "unable to write external parameters to file %@ -- %@"
+ "unionWithType:experiment:treatment:rollout:factorPackSet:"
+ "unsubscribeAllDataStreams"
+ "unsupported experiment of type %{public}d for experiment id: %{public}@"
+ "updateSavedFactorPackWithId failed to link temp based factor pack for: name based directory (%d): %{public}@ OR identifier based directory (%d): %{public}@."
+ "updateSavedTreatmentWithTreatmentId:deletingAssetsWithFactorNames:forNamespaceName:"
+ "updateSavedTreatmentWithTreatmentId:deletingAssetsWithFactorNames:forNamespaceName:inUseAssetDeletionBehavior:"
+ "userDefaultVoiceSlotDidChange:"
+ "v16@?0@\"BMStoreEvent\"8"
+ "v16@?0@\"BPSCompletion\"8"
+ "v16@?0@\"TRICellularParameterGuardedData\"8"
+ "v16@?0@\"TRIExternalParameterGuardedData\"8"
+ "v16@?0@\"TRISystemInfoGuardedData\"8"
+ "v24@0:8@\"CTDataConnectionStatus\"16"
+ "v24@0:8@\"CTDataSettings\"16"
+ "v24@0:8@\"CTDataStatus\"16"
+ "v24@0:8@\"CTDataStatusBasic\"16"
+ "v24@0:8@\"CTServiceDescriptor\"16"
+ "v24@0:8@\"CTSlicedRunningAppInfoContainer\"16"
+ "v24@0:8@\"CTTetheringStatus\"16"
+ "v24@0:8@\"CTXPCServiceSubscriptionContext\"16"
+ "v24@?0@\"NSNumber\"8@\"NSError\"16"
+ "v28@0:8@\"CTServiceDescriptor\"16B24"
+ "v28@0:8@\"CTTetheringStatus\"16i24"
+ "v28@0:8@\"CTXPCServiceSubscriptionContext\"16B24"
+ "v28@0:8@\"CTXPCServiceSubscriptionContext\"16i24"
+ "v28@0:8@16i24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTDataStatus\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTServiceDisconnectionStatus\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTSimDeactivationInfo\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSArray\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSNumber\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSString\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16i24i28"
+ "v32@0:8@\"NSSet\"16@?<v@?@\"NSArray\">24"
+ "v32@0:8@\"NSSet\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@16i24i28"
+ "v36@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSNumber\"24i32"
+ "v36@0:8@\"CTXPCServiceSubscriptionContext\"16i24@\"CTDataConnectionStatus\"28"
+ "v36@0:8@\"NSString\"16B24@\"CTTrafficDescriptorsContainer\"28"
+ "v36@0:8@16i24@28"
+ "v40@0:8@\"NSString\"16@?<B@?@\"NSDictionary\">24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "v40@0:8@16q24@32"
+ "v44@0:8Q16@\"NSDate\"24i32@?<v@?@\"NSNumber\"@\"NSArray\"@\"NSDate\"@\"NSError\">36"
+ "v44@0:8Q16@24i32@?36"
+ "v48@0:8@16q24@32*40"
+ "v72@0:8@16@24^B32B40@44@52B60@64"
+ "validateBase64Signature:forDigest:"
+ "validatedEnvironmentFromNumber:"
+ "validatedPopulationFromNumber:"
+ "validityDays"
+ "void *CoreTelephonyLibrary(void)"
+ "void *TextInputLibrary(void)"
+ "writeSysctlWithName:intValue:"
+ "writeToFile:atomically:encoding:error:"
+ "{?=qqq}16@0:8"
+ "\xf0!"
- " DELETE FROM     backgroundMLTaskHistory WHERE         eventSecondsFromEpoch < :threshold"
- " DELETE FROM     backgroundMlTasks WHERE   backgroundMlTaskId = :background_ml_task_id     AND deploymentId = :deployment_id"
- " DELETE FROM     mlRuntimeEvaluationStatusHistory WHERE     eventSecondsFromEpoch < :threshold;"
- " INSERT INTO backgroundMlTaskHistory (     eventSecondsFromEpoch,     eventType,     backgroundMlTaskId,     deploymentId,     factorPackSetId ) VALUES (     :timestamp,     :event_type,     :background_ml_task_id,     :deployment_id,     :factor_pack_set_id );"
- " INSERT INTO rolloutsV2 (     rolloutId,     deploymentId,     rampId,     status,     isShadow,     activeFactorPackSetId,     activeTargetingRuleIndex,     targetedFactorPackSetId,     targetedTargetingRuleIndex,     artifact ) VALUES (     :rollout_id,     :deployment_id,     :ramp_id,     :status,     :is_shadow,     :active_fp_set_id,     :active_targeting_rule_index,     :targeted_fp_set_id,     :targeted_targeting_rule_index,     :artifact );"
- " INSERT OR IGNORE INTO backgroundMlTasks (     backgroundMlTaskId,     deploymentId,     pluginId,     status,     endSecondsFromEpoch,     activeFactorPackSetId,     activeTargetingRuleIndex,     targetedFactorPackSetId,     targetedTargetingRuleIndex,     artifact ) VALUES (     :background_ml_task_id,     :deployment_id,     :plugin_id,     :status,     :end_seconds,     :active_fp_set_id,     :active_targeting_rule_index,     :targeted_fp_set_id,     :targeted_targeting_rule_index,     :artifact );"
- " INSERT OR IGNORE INTO experiments (     deploymentEnvironment,     experimentId,     deploymentId,     type,     status,     startSecondsFromEpoch,     endSecondsFromEpoch,     isShadow,     artifact ) VALUES (     :deployment_env,     :experiment_id,     :deployment_id,     :type,     :status,     :start_seconds,     :end_seconds,     :is_shadow,     :artifact );"
- " INSERT OR REPLACE INTO mlRuntimeEvaluationStatusHistory (     evaluationId,     eventSecondsFromEpoch,     serializedMLRuntimeEvaluation,     serializedEvaluationStatus ) VALUES (     :evaluation_id,     :timestamp,     :eval_data,     :status_data );"
- " SELECT * FROM     backgroundMlTaskHistory %@ ORDER BY     eventSecondsFromEpoch ASC,     rowid ASC;"
- " SELECT * FROM     backgroundMlTasks as t %@ ORDER BY     endSecondsFromEpoch ASC,     rowid ASC;"
- " SELECT * FROM     mlRuntimeEvaluationStatusHistory %@ ORDER BY     eventSecondsFromEpoch ASC,     rowid ASC;"
- " UPDATE backgroundMlTasks SET         activeFactorPackSetId = :set_id,         activeTargetingRuleIndex = :rule_index WHERE     backgroundMlTaskId = :background_ml_task_id       AND deploymentId = :deployment_id;"
- " UPDATE backgroundMlTasks SET         status = :status WHERE     backgroundMlTaskId = :background_ml_task_id       AND deploymentId = :deployment_id;"
- " UPDATE backgroundMlTasks SET         targetedFactorPackSetId = :set_id,         targetedTargetingRuleIndex = :rule_index WHERE         backgroundMlTaskId = :background_ml_task_id     AND deploymentId = :deployment_id;"
- " WHERE         (e.experimentId != :experiment_id OR e.deploymentId != :deployment_id)     AND e.type IN (:type_update)     AND e.status IN (:status_enroll, :status_active)     AND e.isShadow = 0     AND (             e.startSecondsFromEpoch IS NULL         OR  e.endSecondsFromEpoch IS NULL         OR  max(:start_seconds, e.startSecondsFromEpoch) < min(:end_seconds, e.endSecondsFromEpoch)     )     AND n.name IN _pas_nsarray(:namespaces)"
- " WHERE     t.backgroundMlTaskId = :background_ml_task_id       AND t.deploymentId = :deployment_id"
- " WHERE eventSecondsFromEpoch > :threshold"
- " WHERE t.backgroundMlTaskId = :background_ml_task_id"
- "%lu BMLTs remain to be processed for notification: %@."
- "%s has empty path arg: deployment.backgroundMLTaskId"
- "%{public}@ %p: activeEvaluationsForBMLTWithCompletion: -> %{public}@"
- "%{public}@ scheduled deactivation of %u BMLTs"
- "%{public}@Enrolling in factor pack set id %{public}@ for BMLT %{public}@"
- "%{public}@Targeting resulted in the default treatment (non-enrollment) for BMLT %{public}@"
- "(%d) %{public}@ %p: %s activeEvaluationsForBMLTWithCompletion:"
- "(%d) %{public}@ %p: %s activeEvaluationsForMLRuntimeWithCompletion:"
- "(%d) %{public}@ %p: %s bmltRecordsWithCompletion:"
- "(%d) %{public}@ %p: %s evaluationHistoryRecordsForMLRuntimeWithLimit:"
- "-[TRIInternalServiceRequestHandler activeBMLTInformationWithPrivacyFilterPolicy:completion:]_block_invoke"
- "-[TRIInternalServiceRequestHandler activeRolloutInformationWithPrivacyFilterPolicy:completion:]_block_invoke"
- "-[TRINamespaceResolverStorage _pathForBMLTDeployment:]"
- "-[TRINamespaceResolverStorage rewriteBMLTDeployment:targetedFactorPackSetId:]"
- "1P v1 rollout %{public}@ is not supported in this release"
- ":background_ml_task_id"
- ":eval_data"
- ":evaluation_id"
- ":is_shadow"
- ":plugin_id"
- ":status_data"
- "<%@,r:%d>"
- "<TRIActiveLowLevelExperiment | targetedBundleIds:%@ factorLevelStrings:%@>"
- "<TRIBackgroundMLTaskRecord | bmltDeployment:%@ pluginId:%@ activeFactorPackSetId:%@ activeTargetingRuleIndex:%@ targetedFactorPackSetId:%@ targetedTargetingRuleIndex:%@ status:%@ endDate:%@ artifact:%@>"
- "<TRIClientBMLTArtifact | backgroundTask:%@ populations:%@ deploymentType:%@ deploymentDate:%@ downloadSize:%@>"
- "<TRIClientBMLTCatalogArtifact | bmltCatalog:%@ population:%@>"
- "<TRIClientRolloutArtifact | rollout:%@ populations:%@ deploymentDate:%@ downloadSize:%@>"
- "<TRIContentDescriptorUnion | type:%@ experiment:%@ treatment:%@ rollout:%@ factorPackSet:%@ bmlt:%@>"
- "<TRIExperimentRecord | deploymentEnvironment:%@ experimentDeployment:%@ treatmentId:%@ factorPackSetId:%@ type:%@ status:%@ startDate:%@ endDate:%@ namespaces:%@ isShadow:%@ isManuallyTargeted:%@ artifact:%@>"
- "<TRIRolloutRecord | deployment:%@ rampId:%@ activeFactorPackSetId:%@ activeTargetingRuleIndex:%@ targetedFactorPackSetId:%@ targetedTargetingRuleIndex:%@ status:%@ namespaces:%@ isShadow:%@ artifact:%@>"
- "<private>"
- "@\"<TRIActiveLowLevelNamespacesProviding>\""
- "@\"TRIActiveLowLevelFactorsWriter\""
- "@\"TRIBMLTDeployment\""
- "@\"TRIBMLTTaskSupport\""
- "@\"TRIBackgroundMLTaskDatabase\""
- "@\"TRIBackgroundMLTaskHistoryDatabase\""
- "@\"TRIClientBMLTArtifact\""
- "@\"TRIClientBackgroundMLTask\""
- "@\"TRIClientBmltCatalog\""
- "@\"TRIMLRuntimeEvaluationHistoryDatabase\""
- "@\"TRITaskRunResult\"32@?0i8@\"NSArray\"12B20@\"TRIExperimentRecord\"24"
- "@\"TRITaskRunResult\"32@?0i8B12@\"NSArray\"16@\"NSDate\"24"
- "@\"TRIXPCInternalSystemServiceWrapper\""
- "@16@?0@\"TRIBMLTDeployment\"8"
- "@44@0:8i16B20B24@28@36"
- "@48@0:8@16@24@32B40C44"
- "@48@0:8@16@24@32Q40"
- "@52@0:8@16@24@32@40B48"
- "@52@0:8@16B24@28Q36@44"
- "@56@0:8@16@24@32@40Q48"
- "@56@0:8@16@24i32@36B44@?48"
- "@60@0:8C16@20@28@36@44@52"
- "@92@0:8@16@24@32@40@48@56q64@72B80@84"
- "@96@0:8i16@20@28@36i44q48@56@64@72B80B84@88"
- "AND isShadow != 0"
- "AND isShadow = 0"
- "Activated BMLT deployment: %{public}@"
- "All fetched BMLTs have been processed. Sending a %s notification."
- "Apr 19 2025"
- "Attempting to deactivate treatment %@ of ROLLOUT experiment %{public}@."
- "B24@?0@\"TRIBMLTDeployment\"8@\"NSDictionary\"16"
- "B28@0:8I16@?20"
- "B32@?0@\"TRILogNamespace\"8Q16^B24"
- "B36@0:8@16i24C28B32"
- "B36@0:8I16@20@?28"
- "B40@0:8@16C24B28^@32"
- "B40@0:8@16^@24@32"
- "B44@0:8@16@24@32B40"
- "B44@0:8@16i24@28C36B40"
- "B48@0:8@16@24@32B40C44"
- "B48@0:8@16@?24@32@?40"
- "B96@0:8@16@24@32@40@48^B56^@64^B72^B80^@88"
- "BMLT"
- "BMLT %{public}@ is targeted to \"%{public}@\" (emergency disenroll!!!)."
- "BMLT %{public}@ is targeted to \"%{public}@\" (enroll with an empty factor pack set)."
- "BMLT %{public}@ is targeted to \"%{public}@\" (ignoring the deployment)."
- "BMLT %{public}@.%d contains maRefs file without DB reference."
- "BMLT %{public}@.%u has end date in the past"
- "BMLT %{public}@.%u supports namespace compatibility versions {%{public}@} for namespace \"%{public}@\", but the namespace descriptor declares download compatibility with version %u. (This is unlikely to be an issue, unless you're REALLY sure BMLT %{public}@ should be available on this device.)"
- "BMLT %{public}@.%u supports namespace compatibility versions {%{public}@} for namespace \"%{public}@\", but the namespace descriptor declares download compatibility with version %u. (This is unlikely to be an issue, unless you're REALLY sure rollout %{public}@ should be available on this device.)"
- "BMLT artifact not found"
- "BMLT artifact with id %{public}@.%d contains background ML task definition with mismatched identifier: %{public}@.%d"
- "BMLT artifact with id %{public}@.%d does not have a plausible deployment type, found nil."
- "BMLT artifact with id %{public}@.%d does not have a plausible deployment type, found: %d."
- "BMLT artifact with id %{public}@.%d has backgroundMLTaskId which is not a plausible uniqueId."
- "BMLT artifact with id %{public}@.%d has namespace name \"%{public}@\" which is not path-safe."
- "BMLT catalog artifact has backgroundMLTaskId %{public}@.%d which is not a plausible uniqueId."
- "BMLT catalog fetch failed. Notifications fetching will continue but no BMLTs will be deactivated. Error %@"
- "BMLT catalog fetch status success with %ld BMLTs to deactivate"
- "BMLT catalog fetch was asked to retry. Notifications fetching will continue but no BMLTs will be deactivated. Error %@"
- "BMLT deployment %{public}@ does not match the device NCVs. Completing task without activating deployment."
- "BMLT deployment %{public}@ ended %{public}@ and will not be exposed to MLRuntime"
- "BMLT deployment %{public}@ has already activated factor pack set %{public}@. Completing task without activating deployment again."
- "BMLT deployment %{public}@ is selected and not yet active; scheduling activation for namespaces %{public}@."
- "BMLT deployment %{public}@ was selected, but is already active. Scheduling re-activation for namespaces %{public}@"
- "BMLT fetch requested but no deployment was provided"
- "BMLT fetch status success but 0 results fetched."
- "BMLT fetch status success with %ld results"
- "BMLT identifiers missing in task definition"
- "BMLTNotification CloudKit record %@ has missing or corrupt background ML task id."
- "Bitacora error :%{private}@ for BMLT id: %{public}@ deployment:%d"
- "Bitacora error :%{private}@ for shadow evaluation with experimentId: %{public}@ deployment:%d treatment:%{public}@"
- "Cannot activate BMLT deployment %{public}@: start time %@ is in the future"
- "Cannot deactivate treatment %@ of ROLLOUT experiment %{public}@ because associated namespace %@ is not dynamic."
- "Cannot deactivate treatment %@ of ROLLOUT experiment %{public}@ because the experiment has no namespaces."
- "Cannot decode message of type %@ with field of length 0: backgroundMlTaskId"
- "Cannot decode message of type %@ with field of length 0: bmltId"
- "Cannot decode message of type %@ with missing field: backgroundMlTask"
- "Cannot decode message of type %@ with missing field: backgroundMlTaskId"
- "Cannot decode message of type %@ with missing field: bmltId"
- "Cannot retarget ROLLOUT experiment %{public}@ because associated namespace %{public}@ is not dynamic."
- "Cannot retarget experiment %{public}@ because the experiment has no namespaces."
- "Class getLBFEventManagerClass(void)_block_invoke"
- "Class getLBFTrialEventClass(void)_block_invoke"
- "Class getLBFTrialIdentifiersClass(void)_block_invoke"
- "Clearing Experiment Updates Biome Stream due to D&U opt-out"
- "CloudKit fetch of BMLT notification for %{public}@"
- "CloudKit record %@ for BMLT catalog does not have a valid signature."
- "CloudKit record %@ for BMLT catalog has missing or corrupt encoded catalog definition signature."
- "CloudKit record %@ for BMLT catalog has missing or corrupt encoded catalog definition."
- "CloudKit record %@ for BMLT catalog has missing or corrupt population value."
- "CloudKit record %@ for BMLT catalog has missing or corrupt public certificate."
- "CloudKit record %@ for BMLT catalog has unparseable BMLT catalog definition: %@"
- "CloudKit record %@ for BMLT catalog has unparseable BMLT catalog definition: %{public}@"
- "CloudKit record %@ with background ML task id %@ has missing or corrupt deployment id."
- "CloudKit record %@ with background ML task id %@.%@ does not have a valid signature."
- "CloudKit record %@ with background ML task id %@.%@ has a missing or corrupt namespace name."
- "CloudKit record %@ with background ML task id %@.%@ has missing or corrupt deployment type."
- "CloudKit record %@ with background ML task id %@.%@ has missing or corrupt encoded BMLT definition signature."
- "CloudKit record %@ with background ML task id %@.%@ has missing or corrupt encoded task definition."
- "CloudKit record %@ with background ML task id %@.%@ has missing or corrupt populations."
- "CloudKit record %@ with background ML task id %@.%@ has missing or corrupt public certificate."
- "CloudKit record %@ with background ML task id %@.%@ has unparseable background ML task definition: %@"
- "CloudKit record %@ with background ML task id %@.%@ has unreadable deploymentDate."
- "CloudKit record %@ with background ML task id %{public}@ has missing or corrupt deployment id."
- "CloudKit record %@ with background ML task id %{public}@.%@ does not have a valid signature."
- "CloudKit record %@ with background ML task id %{public}@.%@ has a missing or corrupt namespace name."
- "CloudKit record %@ with background ML task id %{public}@.%@ has missing or corrupt deployment type."
- "CloudKit record %@ with background ML task id %{public}@.%@ has missing or corrupt encoded BMLT definition signature."
- "CloudKit record %@ with background ML task id %{public}@.%@ has missing or corrupt encoded task definition."
- "CloudKit record %@ with background ML task id %{public}@.%@ has missing or corrupt populations."
- "CloudKit record %@ with background ML task id %{public}@.%@ has missing or corrupt public certificate."
- "CloudKit record %@ with background ML task id %{public}@.%@ has unparseable background ML task definition: %{public}@"
- "CloudKit record %@ with background ML task id %{public}@.%@ has unreadable deploymentDate."
- "Could not create BMLT artifact from CloudKit record %@."
- "Could not create BMLT catalog artifact from CloudKit record %@."
- "Could not remove treatment from flatbuffer storage:%@."
- "Counts for removal of unreferenced treatments from flatbuffers:%u and protobuf:%u do not match"
- "Deactivating BMLT deployment matching %{public}@: %d"
- "Decoded valid and device-compatible BMLT catalog notification. This means we are ack’ing the CK notification, not acting on it."
- "Decoded valid and device-compatible BMLT notification: %{public}@. This means we are ack’ing the CK notification, not acting on it."
- "Deferral requested before any cleaning unused content."
- "Deferral requested before any maintenance task."
- "Deferral requested before checking to see if biome should be cleared."
- "Deferral requested before compacting database."
- "Deferral requested before expiring old BMLT history records."
- "Deferral requested before expiring old ML runtime evaluation history records."
- "Deferral requested before expiring old history records."
- "Deferral requested before expiring old rollout history records."
- "Deferral requested before handling expired BMLTs."
- "Deferral requested before handling orphaned namespaces."
- "Deferral requested before pruning Biome Stream."
- "Deferral requested before publishing low level factors."
- "Deferral requested before push service sync."
- "Deferral requested before reporting experiments metric."
- "Don't know how to handle shadow evaluation on experiment deployment %{public}@ with unspecified type."
- "Don't know how to handle shadow evaluation on rollout deployment %{public}@ with unspecified type."
- "Error while iterating through rollout directory: %@"
- "Experiment deployment %{public}@ is marked as shadow but has no shadowEvaluation."
- "Experiment deployment %{public}@ is marked as shadow but it does not have ClientBackgroundMLTask."
- "Experiment is a BMLT and will not be included in MLRuntime Shadow Evaluation"
- "Experiment update notification missing endate. ID: %{public}@"
- "Expired %tu records from BMLT history."
- "Expired %tu records from MLRuntime evaluation history."
- "Failed to decode TRIPersistedClientBMLTArtifact: %{public}@"
- "Failed to deserialize MLRuntimeEvaluation: %{public}@"
- "Failed to deserialize TRIEvaluationStatus: %{public}@"
- "Failed to drop record for old rollout deployment %{public}@"
- "Failed to drop ref on experiment artifact for old rollout deployment %{public}@"
- "Failed to drop reference on artifact for BMLT %{public}@"
- "Failed to fetch factor pack set (with id:%@) for experiment (with id:%@)."
- "Failed to find the factor pack set corresponding to the experiment %@.%u, treatment %@. (This will not fail experiment targeting)."
- "Failed to parse persisted TRIClientBMLTArtifact for artifact for %{public}@.%d: %{public}@"
- "Failed to set Active status of BMLT deployment %{public}@"
- "Failed to set active FPS %{public}@ for BMLT deployment %{public}@"
- "Failed to unset targeted FPS for BMLT deployment %{public}@"
- "Failed to update BMLT history database while marking %{public}@ of fps %@ : bmlt %{public}@ : deployment %d. Note: this allocation status will not be logged to analytics."
- "FetchBMLTCatalogNotification"
- "FetchBMLTNotificationWithDeployment"
- "FetchBMLTNotificationsDateDescending"
- "Finished %{public}@ with BMLT %{public}@: %{public}@"
- "Finished fetchBMLTCatalogNotification query error %@"
- "Finished fetchBMLTNotification query for deployment %{public}@.%@ error %@"
- "Finished fetchBMLTNotifications query with %tu results cursor %@ error %{public}@"
- "Flatbuffer Storage: Factor pack set %{public}@ contains ineligible factor pack. Re-fetching factor pack to find replacement."
- "Flatbuffer Storage: Factor pack set %{public}@ is already present; skipping download of factor packs. Path: %@"
- "Flatbuffer migration for rollouts completed with status %s"
- "Flatbuffers: failed to remove descriptor from rollout layer for namespace %{public}@"
- "Found incompatible deployment type for BMLT: %{public}@"
- "From Flatbuffer storage: Factor pack set %{public}@ requires namespace %{public}@ which is not registered in Trial."
- "From flatbuffers, while deactivating ROLLOUT experiment %{public}@ treatment %@, failed to remove rollout layer for namespace %{public}@"
- "Hybrid-BMLT %{public}@ ended and will not be exposed to MLRuntime"
- "Ignoring BMLT deployment %{public}@ because BMLT task identifier %{public}@ has already been processed for namespaces %{public}@."
- "Ignoring unsupported notification of type %@ for deploymentEnvironment %@."
- "Initializing TRIDeactivateBMLTDeploymentTask with trigger event: %@"
- "Integration test logger logging to: %@"
- "Invalid JSON for BMLT content identifier: %{public}@"
- "KnownFactorLevels"
- "LBFEventManager"
- "LBFTrialEvent"
- "LBFTrialIdentifiers"
- "LowLevelNamespacesProviding"
- "Missing serialized value for TRIClientBMLTArtifact.downloadSize"
- "Namespace %{public}@ for BMLT %{public}@ is no longer download compatible. Expected NCV: %u Actual: %{public}@"
- "Namespace %{public}@ for BMLT %{public}@ is upgrade compatible. Upgrade NCVs: %@ Namespace NCVs: %{public}@"
- "Neither protobuf nor flatbuffer were found in a factor pack of FPS with id %@"
- "No valid and compatible BMLT artifact was received for %{public}@."
- "Not purging dynamic namespace for missing app container: %{public}@"
- "Note: BMLT %{public}@.%u involves namespace %{public}@ but it is not registered with Trial. Factor packs for this namespace shall not be downloaded."
- "Note: BMLT %{public}@.%u is missing a selected namespace."
- "Notifying MLRuntime of %@ shadow evaluation for rollout deployment %@."
- "Notifying MLRuntime of activated shadow evaluation for experiment deployment %{public}@."
- "Notifying MLRuntime of deactivated shadow evaluation for experiment deployment %{public}@."
- "Post-upgrade task deactivated BMLT %{public}@ since it's incompatible with existing NCVs"
- "Pruning Obsolete events from biome stream"
- "Q40@0:8@16@24@32"
- "Received BMLT catalog notification ckRecordID %@"
- "Received BMLT notification for deployment %{public}@.%@ ckRecordID %@"
- "Received BMLTNotification with CKRecordID %{public}@"
- "Received unknown event in bitacora handler."
- "Registering BMLT (single) fetch notification %{public}@"
- "Registering BMLT bulk fetch notification %{public}@ for %lu records."
- "Removed %u unreferenced BMLT deployment metadata dirs."
- "Removed %u unreferenced treatments from flatbuffers."
- "Retrieved nil serialized value for nonnull TRIActiveLowLevelExperiment.factorLevelStrings"
- "Retrieved nil serialized value for nonnull TRIActiveLowLevelExperiment.targetedBundleIds"
- "Retrieved nil serialized value for nonnull TRIClientBMLTArtifact.backgroundTask"
- "Retrieved nil serialized value for nonnull TRIClientBMLTArtifact.deploymentDate"
- "Retrieved nil serialized value for nonnull TRIClientBMLTArtifact.deploymentType"
- "Retrieved nil serialized value for nonnull TRIClientBMLTArtifact.populations"
- "Retrieved nil serialized value for nonnull TRIClientBMLTCatalogArtifact.bmltCatalog"
- "Retrieved nil serialized value for nonnull TRIClientBMLTCatalogArtifact.population"
- "Rollout deployment %@ is marked as shadow but has no shadowEvaluation."
- "Rollout deployment %{public}@ is shadow-installed, no associated activation."
- "Rollout v1 experiment %{public}@ was previously finished, still attempting re-targeting"
- "SELECT * FROM backgroundMlTaskHistory WHERE         backgroundMlTaskId = :background_ml_task_id    AND deploymentId = :deployment_id    AND factorPackSetId = :factor_pack_set_id ORDER BY rowid DESC"
- "Saving to fb based storage:%{public}@ did not match pb based storage:%{public}@"
- "SiriUserActivitySegment"
- "Skipping CloudKit fetch of BMLT notification for %{public}@: already present."
- "Skipping activations for BMLT %{public}@ due to it not being in the catalog"
- "Skipping conversion of protobuf for unrecognized id:%lld"
- "Skipping experiment %{public}@ with no namespace name."
- "Skipping inactive experiment %{public}@ while looking for purgeable experiments"
- "Skipping validation of rollout content in missing app container: %{public}@"
- "Starting flatbuffer migration for rollouts"
- "Starting rollout migration for namespace: %{private}@"
- "T@\"NSNumber\",R,N,V_deploymentType"
- "T@\"NSNumber\",R,N,V_population"
- "T@\"NSString\",R,N,V_pluginId"
- "T@\"TRIBMLTDeployment\",R,N"
- "T@\"TRIBMLTDeployment\",R,N,V_bmlt"
- "T@\"TRIBMLTDeployment\",R,N,V_bmltDeployment"
- "T@\"TRIBMLTDeployment\",R,N,V_deployment"
- "T@\"TRIBackgroundMLTaskDatabase\",R,N,V_bmltDatabase"
- "T@\"TRIBackgroundMLTaskHistoryDatabase\",R,N,V_bmltHistoryDatabase"
- "T@\"TRIClientBMLTArtifact\",R,N,V_artifact"
- "T@\"TRIClientBackgroundMLTask\",&,D,N"
- "T@\"TRIClientBackgroundMLTask\",R,N,V_backgroundTask"
- "T@\"TRIClientBmltCatalog\",R,N,V_bmltCatalog"
- "T@\"TRIMLRuntimeEvaluationHistoryDatabase\",R,N,V_evaluationHistoryDatabase"
- "TB,R,N,V_isShadow"
- "TRIAL_SYSTEM"
- "TRIActivateTargetedBMLTDeploymentPersistedTask"
- "TRIActivateTargetedBMLTDeploymentTask"
- "TRIActivateTargetedBMLTDeploymentTask.m"
- "TRIActiveLowLevelExperiment"
- "TRIActiveLowLevelExperimentOCNTErrorDomain"
- "TRIActiveLowLevelExperimentsReader"
- "TRIActiveLowLevelFactorStringBuilder"
- "TRIActiveLowLevelFactorStringBuilder.m"
- "TRIActiveLowLevelFactorsPublisher"
- "TRIActiveLowLevelFactorsWriter"
- "TRIActiveLowLevelNamespacesProviding"
- "TRIBMLTDatabase unable to activate BMLT deployment %{public}@; not found."
- "TRIBMLTDatabase unable to target BMLT deployment %{public}@; not found."
- "TRIBMLTDeploymentRefStore"
- "TRIBMLTTargeter"
- "TRIBMLTTargeter.m"
- "TRIBMLTTargetingPersistedTask"
- "TRIBMLTTargetingPersistedTask_TriggerEvent"
- "TRIBMLTTargetingTask"
- "TRIBMLTTargetingTask.m"
- "TRIBMLTTaskSupport"
- "TRIBMLTTaskSupportGuardedData"
- "TRIBackgroundMLTaskDatabase"
- "TRIBackgroundMLTaskDatabase.m"
- "TRIBackgroundMLTaskHistoryDatabase"
- "TRIBackgroundMLTaskHistoryDatabase.m"
- "TRIBackgroundMLTaskRecord"
- "TRIClientBMLTArtifact"
- "TRIClientBMLTArtifact+Utils.m"
- "TRIClientBMLTArtifactOCNTErrorDomain"
- "TRIClientBMLTCatalogArtifact"
- "TRIClientBMLTCatalogArtifactOCNTErrorDomain"
- "TRIClientBackgroundMLTask"
- "TRIClientTreatment not present for treatmentId %@"
- "TRIDeactivateBMLTDeploymentGuardedData"
- "TRIDeactivateBMLTDeploymentPersistedTask"
- "TRIDeactivateBMLTDeploymentPersistedTask_TriggerEvent"
- "TRIDeactivateBMLTDeploymentTask"
- "TRIDeactivateBMLTDeploymentTask.m"
- "TRIFetchBMLTNotificationGuardedData"
- "TRIFetchBMLTNotificationsPersistedTask"
- "TRIFetchBMLTNotificationsTask"
- "TRIFetchBMLTNotificationsTask.m"
- "TRIInternalSystemServiceRequestHandler"
- "TRIKnownLowLevelFactorsReader"
- "TRILighthouseBitacoraHandler"
- "TRILighthouseBitacoraHandler.m"
- "TRIMLRuntimeEvaluationHistoryDatabase"
- "TRIMLRuntimeEvaluationHistoryDatabase.m"
- "TRIMakeDefaultPersistedTask"
- "TRIMakeDefaultPersistedTask encodes unspecified deploymentId."
- "TRIMakeDefaultTask"
- "TRIMakeDefaultTask.m"
- "TRIMakeDefaultTask: Treatment from flatbuffers: %@ does not match treatment from protobufs: %@"
- "TRIPersistedClientBMLTArtifact"
- "TRITripersistedClientBmltartifactRoot"
- "TRIXPCInternalSystemServiceListener"
- "TRIXPCInternalSystemServiceProtocol"
- "TRIXPCInternalSystemServiceWrapper"
- "Targeting BMLT deployment %{public}@ resulted in an error"
- "Targeting error for BMLT %@: %@"
- "Targeting factor pack set id %{public}@ for BMLT %{public}@ with assignment %{public}@."
- "Targeting results in no-op for BMLT: %{public}@, skipping processing of record"
- "Terminating BMLT due to termination notification: %{public}@"
- "The BMLT database query for active BMLTs failed."
- "The calling process is missing true-valued entitlement \"%@\"."
- "The experiment database query failed."
- "The experiment database query for BMLT failed."
- "Treatment loaded from flatbuffers:%{public}@  does not match treatment loaded from pb: %{public}@ "
- "TrialXP-429.20.2"
- "TripersistedClientBmltartifact.pbobjc.m"
- "Unable to MakeDefault into missing app container: %{public}@"
- "Unable to clear record for deactivated BMLT: %{public}@"
- "Unable to decrement ref for BMLT deployment: (r: %{public}@, d: %d) in %{public}@"
- "Unable to fetch BMLT catalog notification"
- "Unable to fetch BMLT notification %{public}@: %{public}@"
- "Unable to find BMLT"
- "Unable to find BMLT ID %{public}@. Please verify BMLT id is valid."
- "Unable to find deployment to deactivate in BMLT database (for deployment: (bmlt: %{public}@, d: %d)"
- "Unable to find namespace id for namespace name: %@"
- "Unable to increment ref for BMLT deployment: (r: %{public}@, d: %d) in %{public}@"
- "Unable to load soft-linked LBFEventManager class"
- "Unable to load soft-linked LBFTrialEvent class"
- "Unable to load soft-linked LBFTrialIdentifiers class"
- "Unable to parse buffer as TRIActivateTargetedBMLTDeploymentPersistedTask: %{public}@"
- "Unable to parse buffer as TRIBMLTTargetingPersistedTask: %{public}@"
- "Unable to parse buffer as TRIDeactivateBMLTDeploymentPersistedTask: %{public}@"
- "Unable to parse buffer as TRIFetchBMLTNotificationsPersistedTask: %{public}@"
- "Unable to parse buffer as TRIMakeDefaultPersistedTask: %{public}@"
- "Unable to update BMLT %{public}@; targeted factor pack set %{public}@ is missing."
- "Unable to update on-disk experiment deployment directory, but continuing because the experiment is non-shadow."
- "Unable to update preexisting factor pack set %{public}@ for BMLT deployment %{public}@: record not found in database."
- "Unarchived unexpected class for TRIActiveLowLevelExperiment key \"factorLevelStrings\" (expected %@, decoded %@)"
- "Unarchived unexpected class for TRIActiveLowLevelExperiment key \"targetedBundleIds\" (expected %@, decoded %@)"
- "Unarchived unexpected class for TRIClientBMLTArtifact key \"deploymentDate\" (expected %@, decoded %@)"
- "Unarchived unexpected class for TRIClientBMLTArtifact key \"deploymentType\" (expected %@, decoded %@)"
- "Unarchived unexpected class for TRIClientBMLTArtifact key \"populations\" (expected %@, decoded %@)"
- "Unarchived unexpected class for TRIClientBMLTCatalogArtifact key \"population\" (expected %@, decoded %@)"
- "Unexpected NULL backgroundMLTaskId"
- "Unexpected NULL pluginId"
- "Unexpected conflict when saving BMLT to database: %{public}@"
- "Unexpected failure to find BMLT deployment %{public}@ for namespaces %{public}@."
- "Unexpected failure to lookup BMLT record for deployment %{public}@."
- "Unexpected nil app container for deactivation of ROLLOUT experiment %{public}@ treatment %@"
- "Unknown notification type for BMLT: %{public}@, deployment: %{public}d"
- "Updated treatment from fb storage: %@ does not match treatment from pb storage: %@"
- "WHERE activeFactorPackSetId IS NOT NULL %@"
- "WHERE eventSecondsFromEpoch > :threshold"
- "WHERE status = :status_active %@"
- "Warning: record for BMLT deployment %{public}@ not available; issuing incomplete telemetry."
- "Warning: unable to find TRIBackgroundMLTaskRecord for deployment %{public}@; issuing incomplete telemetry."
- "While deactivating ROLLOUT experiment %{public}@ treatment %@, failed to remove rollout layer for namespace %{public}@."
- "[NSKeyedArchiver archivedDataWithRootObject:record.status requiringSecureCoding:YES error:nil]"
- "[record.evaluation data]"
- "_activationTelemetryWithSuccess:bmltRecord:serverContext:"
- "_activeBMLTIsCompatible:upgradeNCVs:downloadNCVs:"
- "_activeExperimentFactorLevelsForNamespaceName:"
- "_allocationTelemetryWithEvent:factorPackSetId:bmltRecord:context:"
- "_backgroundTask"
- "_bmlt"
- "_bmltBatchNotificationIdentifier"
- "_bmltCatalog"
- "_bmltDatabase"
- "_bmltDeployment"
- "_bmltFetchTelemetryIfApplicableWithSuccess:bmltRecord:serverContext:"
- "_bmltHistoryDatabase"
- "_bmltStateForAnalyticsFromStatusType:"
- "_bmltSupport"
- "_deactivationTelemetryWithSuccess:bmltRecord:deactivatedFactorPackSetId:serverContext:"
- "_deleteOnDemandAssetsWithFactorNames:treatment:namespace:forRollouts:"
- "_deleteOnDemandAssetsWithFactorNames:treatment:namespace:forRollouts:inUseAssetDeletionBehavior:"
- "_deploymentType"
- "_enumerateTaskRecordsMatchingWhereClause:bind:transaction:block:"
- "_evaluateExpressionForDeployment:context:assignment:fpsId:error:"
- "_evaluationHistoryDatabase"
- "_experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:serverContext:completion:"
- "_fetchBMLTNotificationsWithCursor:options:completion:"
- "_handleExpiredBMLTsWithBMLTDatabase:nextTasks:"
- "_hasStructurallyValidBMLTs:population:"
- "_hasValidNCVForBMLT:namespaceDescriptorProvider:"
- "_invalidBMLTDeployments"
- "_isFlatbufferTreatmentReadEnabled"
- "_isFlatbufferTreatmentWriteEnabled"
- "_isPreviouslyRecordedStateForEvent:"
- "_isRolloutV1For1PWithExperimentRecord:context:"
- "_isShadow"
- "_isStructurallyValidBMLT:deployment:namespaceName:populations:deploymentType:deploymentDate:"
- "_linkAssetWithId:treatmentId:assetStore:factor:forRollouts:"
- "_migrateProtobufFactorPacksToFlatbuffersUsingPaths:"
- "_mlruntimeNotifiedTelemetryWithRecords:serverContext:"
- "_notifyUpdatedShadowEvaluationWithExperimentRecord:context:"
- "_notifyUpdatedShadowEvaluationsWithDeployments:context:usingTransaction:"
- "_pathForBMLTDeployment:"
- "_performSyncXpcWithError:block:"
- "_pluginId"
- "_population"
- "_processBMLTArtifact BMLT deployment %{public}@. bmltsProcessed %{public}@ for namespaces %{public}@."
- "_processBMLTArtifact:bmltsProcessed:deactivatedBMLTs:targeter:context:taskQueue:"
- "_processBMLTCatalogArtifact deactivating BMLT %{public}@"
- "_processBMLTCatalogArtifact:deactivatedBMLTs:context:"
- "_purgeRolloutLayerIfNecessaryWithRecord:fromAppContainer:paths:"
- "_removeUnreferencedBMLTDeploymentsWithRefStore:parentDir:removedCount:"
- "_removeUnreferencedBMLTDeploymentsWithRefStore:topLevelDir:removedCount:"
- "_saveNamespacePartitionedTreatmentsForTreatment:forNamespaceNames:forRollouts:"
- "_saveProtoToFlatbufferFormatWithPaths:namespaceUrl:"
- "_targetBMLTDeployment:appendingTelemetryToSupport:backgroundMLTaskDatabase:backgroundMLTaskHistoryDatabase:targeter:reportTelemetryToServer:factorPackSetIdToActivate:wasEnrolled:shouldDisenroll:error:"
- "_taskResultWithStatus:wasEnrolled:reportResults:nextTasks:bmltHistoryDatabase:"
- "_validRollbackDeploymentsForRollbackExperiment:deploymentIds:"
- "_validateBMLTNamespaceNCVs:downloadNCVs:context:"
- "_validateDynamicNamespaceRolloutsWithDatabase:usingPaths:"
- "_validateRolloutDescriptorsWithNamespaceCompatibilityVersions:usingPaths:"
- "activateDeployment:withFactorPackSetId:targetingRuleIndex:usingTransaction:"
- "activated"
- "activeBMLTInformationWithPrivacyFilterPolicy:completion:"
- "activeEvaluationsForBMLTWithCompletion:"
- "activeEvaluationsForMLRuntimeWithCompletion:"
- "activeExperimentInformationWithEnvironments:privacyFilterPolicy: %{public}@"
- "activeExperimentInformationWithEnvironments:privacyFilterPolicy:completion:"
- "activeLowLevelNamespaces"
- "activeRolloutInformationWithPrivacyFilterPolicy:completion:"
- "addBackgroundMLTaskWithTaskDeployment:pluginId:status:endDate:artifact:"
- "addNamespaceId:"
- "addRecord:usingTransaction:"
- "addTrialdEvent:identifiers:error:"
- "allowedLowLevelDefaultLevelsDir"
- "andClause"
- "artifactFromCKRecord:error:"
- "artifactFromCKRecordResult:withNamespaceDescriptorProvider:container:teamId:requireDeploymentId:completion:"
- "artifactWithBackgroundTask:populations:deploymentType:deploymentDate:downloadSize:"
- "artifactWithBmltCatalog:population:"
- "artifactWithRollout:populations:deploymentDate:downloadSize:"
- "assetReference"
- "backgroundMLTaskId"
- "backgroundMlTask"
- "backgroundMlTaskHistory"
- "backgroundMlTaskId"
- "backgroundTask"
- "backgroundTask != nil"
- "bmlt"
- "bmlt-%@"
- "bmlt-artifact"
- "bmlt-fetched-with-records"
- "bmlt-fetched-without-records"
- "bmlt-retargeting"
- "bmlt-routine-fetch"
- "bmlt: %{public}@, d: %d"
- "bmltBatchNotificationId"
- "bmltCatalog"
- "bmltCatalog != nil"
- "bmltDatabase"
- "bmltDatabase != nil"
- "bmltDeployment"
- "bmltDeployment != nil"
- "bmltDeployment.backgroundMLTaskId"
- "bmltDeployment.deploymentId != kTRIUnspecifiedDeploymentId"
- "bmltDeployment.hasDeploymentId"
- "bmltDeploymentIdArray"
- "bmltHistoryDatabase"
- "bmltHistoryDatabase != nil"
- "bmltId"
- "bmltRecordsWithCompletion:"
- "bmltRecordsWithCompletion: the calling process (pid %d) has ill-typed value for entitlement \"%{public}@\" (expected array)."
- "bmltRecordsWithCompletion: the calling process (pid %d) is missing entitlement \"%{public}@\"."
- "bmltRecordsWithCompletion: the calling process (pid %d) is not entitled for access to deployment environment %@."
- "bmlt_completed_fetch"
- "bmlt_enumerated"
- "bmlt_st_AC"
- "bmlt_st_AC_F"
- "bmlt_st_AL"
- "bmlt_st_AL_F"
- "bmlt_st_AL_O"
- "bmlt_st_DE"
- "bmlt_st_DE_F"
- "bmlt_st_FE"
- "bmlt_st_FE_F"
- "bmlt_st_FE_O"
- "can't save experiment %@ because shadow_evaluation is unsupported for V1 rollouts"
- "can't save rollout treatment for namespace %{public}@: factors path is nil"
- "cannot set default to treatment %@ of experiment %{public}@: failed to clean up treatment with previous compatibility version for namespace %{public}@"
- "cannot set default to treatment %@ of experiment %{public}@: incompatible version %u for namespace %{public}@ (current is %u)"
- "cannot set default to treatment %@ of experiment %{public}@: missing experiment namespace descriptor for namespace %{public}@"
- "categoricalValueForBMLTNotificationEvent:"
- "clientBackgroundMlTask"
- "com.apple.trial.MakeDefaultTaskComplete"
- "com.apple.trial.bmlt.activated"
- "com.apple.trial.shadow-evaluation.mlruntime.status-change"
- "com.apple.triald.BMLTNotification.%@"
- "compatibility"
- "container dir is nil"
- "contentIdentifierForBMLTArtifactWithDeployment:"
- "copyWithReplacementBackgroundTask:"
- "copyWithReplacementBmlt:"
- "copyWithReplacementBmltCatalog:"
- "copyWithReplacementBmltDeployment:"
- "copyWithReplacementDeploymentType:"
- "copyWithReplacementIsShadow:"
- "copyWithReplacementPluginId:"
- "copyWithReplacementPopulation:"
- "deactivateTaskDeployment:deactivatedFactorPackSetId:usingTransaction:"
- "deactivated"
- "deploymentType"
- "deploymentType != nil"
- "deploymentWithBackgroundMLTaskId:deploymentId:"
- "donateTrialIdentifiers:eventType:succeeded:error:"
- "earliestStartDateForActivationIfInFuture"
- "emitBMLTEventWithBMLTId:deploymentId:eventType:succeeded:"
- "emitShadowEvaluationEventWithExperimentId:deploymentId:treatmentId:eventType:succeeded:"
- "ensureBMLTFields"
- "enumerateActiveExperimentRecordsWithVisibility:block:"
- "enumerateActiveRecordsWithVisibility:usingTransaction:block:"
- "enumerateActiveTasksNotInList:usingTransaction:withBlock:"
- "enumerateActiveTasksWithBlock:"
- "enumerateActiveTasksWithTransaction:block:"
- "enumerateFBFactorPacksForFactorPackSet:usingLegacyPaths:withBlock:"
- "enumerateTaskRecordsMatchingTaskId:transaction:block:"
- "enumerateTaskRecordsWithBlock:"
- "enumerateTaskRecordsWithTransaction:block:"
- "error during activation of factorPackSetId {public}%@ for BMLT %{public}@: failed to update activation event database"
- "evaluation"
- "evaluationHistoryDatabase"
- "evaluationHistoryRecordsForMLRuntimeWithLimit:newerThanDate:completion:"
- "evaluationId"
- "experimentHistoryRecordsWithLimit:newerThanDate:privacyFilterPolicy:deploymentEnvironment:completion:"
- "experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:completion:"
- "factorPackIdForBmltWithNamespaceName:"
- "factorPacksExperimentsDisableOld"
- "factorPacksExperimentsRead"
- "factorPacksExperimentsWrite"
- "factorProviderWithNamespaceName:paths:treatmentLayer:faultOnMissingFactors:shouldLockFactorDirectory:"
- "factorProviderWithPaths:namespaceName:resolver:"
- "factors"
- "failed to fetch BMLT %{public}@.%@ (unknown container)"
- "failed to fetch BMLT catalog (unknown container)"
- "failed to remove descriptor from rollout layer for namespace %{public}@"
- "failed to save rollout descriptor for namespace %{public}@"
- "failed to save rollout treatment for namespace %{public}@"
- "failure"
- "fetchBMLTCatalogNotificationWithOptions:completion:"
- "fetchBMLTNotificationWithDeployment:options:completion:"
- "fetchBMLTNotificationsWithOptions:completion:"
- "fetchSingleDeploymentWithContext:"
- "filteredArrayUsingPredicate:"
- "firstNamespaceName"
- "flatbuffer storage removal of treatment did not succeed for namespace:%{public}@"
- "flatbufferTreatmentStorageRead"
- "flatbufferTreatmentStorageWrite"
- "getAllAllocationStatusesForBMLTId:deploymentId:factorPackSetId:"
- "groupForBMLTId:"
- "hasBackgroundMlTask"
- "hasBackgroundMlTaskId"
- "hasBmltBatchNotificationId"
- "hasBmltId"
- "hasClientBackgroundMlTask"
- "hasDeploymentType"
- "hasEvaluationId"
- "hasShadowEvaluation"
- "hasTaskId"
- "hashForFactorLevels:"
- "i40@0:8@16@24@32"
- "incompatibleNamespaceNameForBMLT:namespaceDescriptorProvider:"
- "ineligible  "
- "initWithActivation:"
- "initWithAllocation:"
- "initWithBMLTDeployment:"
- "initWithBMLTDeployment:includeDependencies:taskAttribution:triggerEvent:bmltBatchNotificationIdentifier:"
- "initWithBMLTDeployment:triggerEvent:bmltBatchNotificationIdentifier:"
- "initWithBMLTTaskID:deploymentID:"
- "initWithBackgroundMLTaskId:deploymentId:"
- "initWithBackgroundTask:populations:deploymentType:deploymentDate:downloadSize:"
- "initWithBmlt:factorsState:"
- "initWithBmltCatalog:population:"
- "initWithBmltDeployment:pluginId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:endDate:artifact:"
- "initWithBmltDeployment:pluginId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:endDate:namespace:"
- "initWithDeactivation:"
- "initWithDeployment:"
- "initWithDeployment:rampId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:namespaces:isShadow:artifact:"
- "initWithDeployment:taskAttribution:bmltBatchNotificationIdentifier:"
- "initWithDeployment:treatmentId:"
- "initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:counterfactualTreatmentIds:"
- "initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:isManuallyTargeted:artifact:"
- "initWithEval:factorsState:"
- "initWithEvaluation:status:"
- "initWithEventDate:eventType:backgroundMLTaskId:deploymentId:factorPackSetId:"
- "initWithExperimentID:deploymentID:treatmentID:"
- "initWithFactorPackSetId:taskAttribution:bmltDeployment:"
- "initWithPromise:"
- "initWithRollout:populations:deploymentDate:downloadSize:"
- "initWithSchemaVersion:"
- "initWithServerContextPromise:"
- "initWithServiceName:allowlistedServerInterface:allowlistedClientInterface:serverInitiatedRequestHandler:allowSystemToUserConnection:interruptionHandler:invalidationHandler:logHandle:"
- "initWithTaskDeployment:factorPackSetId:taskAttribution:bmltBatchNotificationIdentifier:"
- "initWithType:evaluationId:date:evalState:"
- "initWithType:experiment:treatment:rollout:factorPackSet:bmlt:"
- "isEqualTolowLevelExperiment:"
- "isExpired"
- "isShadow"
- "issuing extension to com.apple.trial.TrialArchivingService for %s"
- "kAFPreferencesDidChange notification relevancy: %d. Siri locale changed: %d, Siri enablement changed: %d"
- "latestRolloutId"
- "levelValue"
- "logAsRollout"
- "logAsRollout:"
- "lowLevelExperimentWithTargetedBundleIds:factorLevelStrings:"
- "makeDefaultForNamespace:experiment:context:"
- "missing BMLT assignment"
- "mlRuntime"
- "namespaceDescriptorsBMLTDir"
- "namespaceDescriptorsRolloutDir"
- "namespaceIdFromName:"
- "notify about updates to namespace %{public}@ from treatment %@ for rollout %{public}@"
- "overlayLevelsFromFactorProvider:"
- "parentDirForBMLTDeployments"
- "pathForBMLTDeployment:"
- "pathForTargetedFactorPackSetWithTaskDeployment:"
- "pathsForContainer:asClientProcess:"
- "pluginId"
- "pluginId != nil"
- "population"
- "population != nil"
- "q24@?0@\"TRIBackgroundMLTaskRecord\"8@\"TRIBackgroundMLTaskRecord\"16"
- "re-targeting ROLLOUT experiment %{public}@ with treatment %@ resulted in treatment %@"
- "read nil value for NOT NULL serializedEvaluationStatus"
- "read nil value for NOT NULL serializedMLRuntimeEvaluation"
- "recordWithBmltDeployment:pluginId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:endDate:artifact:"
- "recordWithDeployment:rampId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:namespaces:isShadow:artifact:"
- "recordWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:isManuallyTargeted:artifact:"
- "registerAllServicesWithPromise:"
- "registerSystemService"
- "removeUnreferencedBMLTDeploymentsWithServerContext:removedCount:"
- "result.backgroundTask"
- "result.backgroundTask.pluginId"
- "rewriteBMLTDeployment:targetedFactorPackSetId:"
- "rolloutAllocationStatusWithPrivacyFilterPolicy:completion:"
- "rolloutCount"
- "saveToPath:copyAssets:"
- "scheduling deactivation of BMLT %{public}@ with active factor pack set ID %@"
- "seconds"
- "selectedNamespace.name"
- "serializedEvaluationStatus"
- "serializedMLRuntimeEvaluation"
- "serverContext.client.trackingId"
- "setActiveFactorPackSetId:activeTargetingRuleIndex:forTaskDeployment:usingTransaction:"
- "setBackgroundMlTask:"
- "setBackgroundMlTaskId:"
- "setBmltBatchNotificationId:"
- "setBmltId:"
- "setClientBmltFactorPackSetId:"
- "setClientBmltId:"
- "setClientBmltTargetingRuleGroupOrdinal:"
- "setDeploymentType:"
- "setEndDate:"
- "setHashData:"
- "setHashIncludesDefaults:"
- "setLatestRolloutId:"
- "setRolloutCount:"
- "setStatus:forTaskDeployment:usingTransaction:"
- "setTargetedFactorPackSetId:targetedTargetingRuleIndex:forTaskDeployment:usingTransaction:"
- "shadowEvaluation"
- "sharedSystemPaths"
- "shouldPrivacyFilterNamespace:policy:"
- "siriUserActivitySegment"
- "softlink:r:path:/System/Library/PrivateFrameworks/LighthouseBitacoraFramework.framework/LighthouseBitacoraFramework"
- "starting %{public}@ for single deployment with BMLT %{public}@"
- "storage-rewrite-failure"
- "storeExperimentEvent:wasNewEvent:"
- "success"
- "targetBMLT:factorPackSetId:error:"
- "targetTaskDeployment:toFactorPackSetId:targetingRuleIndex:usingTransaction:"
- "taskRecordWithTaskDeployment:"
- "taskWithBMLTDeployment:factorPackSetId:taskAttribution:"
- "taskWithBMLTDeployment:factorPackSetId:taskAttribution:bmltBatchNotificationIdentifier:"
- "taskWithBMLTDeployment:includeDependencies:taskAttribution:triggerEvent:"
- "taskWithBMLTDeployment:includeDependencies:taskAttribution:triggerEvent:bmltBatchNotificationIdentifier:"
- "taskWithBMLTDeployment:triggerEvent:"
- "taskWithBMLTDeployment:triggerEvent:bmltBatchNotificationIdentifier:"
- "taskWithDeployment:taskAttribution:bmltBatchNotificationIdentifier:"
- "taskWithFactorPackSetId:taskAttribution:bmltDeployment:"
- "terminated"
- "treatment %@ of rollout %{public}@ has no factors defined"
- "treatment path is nil"
- "triald failed listening for SIGTERM"
- "triald failed to initialize - exiting"
- "triald failed to initialize server context"
- "triald failed to prepare storage"
- "triald launched"
- "typeOneOfCase"
- "unionWithType:experiment:treatment:rollout:factorPackSet:bmlt:"
- "unknown experiment type for experiment id: %{public}@"
- "updateBMLTHistoryDatabaseWithAllocationStatus:forBMLT:deployment:fps:bmltRecord:context:"
- "updateLoggingWithExperimentRecord:paths:trackingId:newLogTreatmentAddedOut:"
- "updateSavedTreatmentWithTreatmentId:deletingAssetsWithFactorNames:forNamespaceName:forRollouts:"
- "updateSavedTreatmentWithTreatmentId:deletingAssetsWithFactorNames:forNamespaceName:forRollouts:inUseAssetDeletionBehavior:"
- "updated namespace %{public}@ with hash %@"
- "updating treatments for treatmentid:%{public}@ from fb storage did not have same result as updating treatments from pb"
- "urlForDefaultFactorsWithNamespaceName:"
- "v16@?0@\"TRIBMLTTaskSupportGuardedData\"8"
- "v16@?0@\"TRIDeactivateBMLTDeploymentGuardedData\"8"
- "v16@?0@\"TRIFetchBMLTNotificationGuardedData\"8"
- "v2/bmlt"
- "v24@?0@\"TRIBackgroundMLTaskRecord\"8^B16"
- "v24@?0@\"TRIFBFastFactorLevels\"8^B16"
- "v24@?0@\"TRIMLRuntimeEvaluationHistoryRecord\"8^B16"
- "v28@0:8B16@20"
- "v28@0:8C16@?20"
- "v28@0:8C16@?<v@?@\"NSArray\"@\"NSError\">20"
- "v32@0:8@\"TRIFetchOptions\"16@?<v@?Q@\"TRIClientBMLTArtifact\"@\"NSDate\"@\"NSError\">24"
- "v32@0:8@\"TRIFetchOptions\"16@?<v@?Q@\"TRIClientBMLTCatalogArtifact\"@\"NSDate\"@\"NSError\">24"
- "v32@?0@\"TRIBackgroundMLTaskRecord\"8Q16^B24"
- "v32@?0@\"TRIBmltDeploymentId\"8Q16^B24"
- "v36@0:8@\"NSSet\"16C24@?<v@?@\"NSArray\">28"
- "v36@0:8@\"NSSet\"16C24@?<v@?@\"NSArray\"@\"NSError\">28"
- "v36@0:8@16C24@?28"
- "v36@0:8B16@20@28"
- "v40@0:8@\"TRIBMLTDeployment\"16@\"TRIFetchOptions\"24@?<v@?Q@\"TRIClientBMLTArtifact\"@\"NSDate\"@\"NSError\">32"
- "v40@0:8Q16@\"NSDate\"24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8Q16@24@?32"
- "v40@?0Q8@\"TRIClientBMLTArtifact\"16@\"NSDate\"24@\"NSError\"32"
- "v40@?0Q8@\"TRIClientBMLTCatalogArtifact\"16@\"NSDate\"24@\"NSError\"32"
- "v44@0:8@16C24@28@?36"
- "v44@0:8B16@20@28@36"
- "v44@0:8C16@20@28@36"
- "v48@0:8Q16@\"NSDate\"24C32i36@?<v@?@\"NSNumber\"@\"NSArray\"@\"NSDate\"@\"NSError\">40"
- "v48@0:8Q16@24C32i36@?40"
- "v56@0:8C16@20i28@32@40@48"
- "void *LighthouseBitacoraFrameworkLibrary(void)"
- "wasEnrolled != NULL"
- "{?=C}40@0:8@16^@24^@32"
- "{?=C}56@0:8@16@24@32^@40^@48"
- "{?=Q}56@0:8@16@24q32@40@48"
- "\xf0Q"

```
