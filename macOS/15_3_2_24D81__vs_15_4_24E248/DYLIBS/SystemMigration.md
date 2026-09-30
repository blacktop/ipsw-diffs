## SystemMigration

> `/System/Library/PrivateFrameworks/SystemMigration.framework/Versions/A/SystemMigration`

```diff

-5713.60.15.0.0
-  __TEXT.__text: 0x116f64
-  __TEXT.__auth_stubs: 0x1280
-  __TEXT.__objc_methlist: 0xf3d0
-  __TEXT.__const: 0x168
-  __TEXT.__gcc_except_tab: 0x3a70
-  __TEXT.__cstring: 0x26f10
+5739.100.175.0.0
+  __TEXT.__text: 0x106b3c
+  __TEXT.__auth_stubs: 0x11f0
+  __TEXT.__objc_methlist: 0xff20
+  __TEXT.__const: 0x178
+  __TEXT.__gcc_except_tab: 0x352c
+  __TEXT.__cstring: 0x212b0
   __TEXT.__oslogstring: 0x392
-  __TEXT.__ustring: 0x36c
-  __TEXT.__unwind_info: 0x3248
-  __TEXT.__objc_classname: 0x1752
-  __TEXT.__objc_methname: 0x24872
-  __TEXT.__objc_methtype: 0x2e61
-  __TEXT.__objc_stubs: 0x1c6c0
-  __DATA_CONST.__got: 0xec8
-  __DATA_CONST.__const: 0x948
-  __DATA_CONST.__objc_classlist: 0x5d0
+  __TEXT.__ustring: 0x364
+  __TEXT.__unwind_info: 0x3020
+  __TEXT.__objc_classname: 0x15f4
+  __TEXT.__objc_methname: 0x23fd9
+  __TEXT.__objc_methtype: 0x2ccf
+  __TEXT.__objc_stubs: 0x1bce0
+  __DATA_CONST.__got: 0xeb0
+  __DATA_CONST.__const: 0xb20
+  __DATA_CONST.__objc_classlist: 0x580
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x188
+  __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8120
+  __DATA_CONST.__objc_selrefs: 0x8028
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA_CONST.__objc_superrefs: 0x4c0
-  __DATA_CONST.__objc_arraydata: 0xd28
-  __AUTH_CONST.__auth_got: 0x958
-  __AUTH_CONST.__const: 0x1b10
-  __AUTH_CONST.__cfstring: 0x1b8c0
-  __AUTH_CONST.__objc_const: 0x191c8
-  __AUTH_CONST.__objc_intobj: 0x6c0
-  __AUTH_CONST.__objc_arrayobj: 0x420
-  __AUTH_CONST.__objc_doubleobj: 0x10
+  __DATA_CONST.__objc_superrefs: 0x498
+  __DATA_CONST.__objc_arraydata: 0x5a8
+  __AUTH_CONST.__auth_got: 0x910
+  __AUTH_CONST.__const: 0x1b00
+  __AUTH_CONST.__cfstring: 0x18700
+  __AUTH_CONST.__objc_const: 0x16378
+  __AUTH_CONST.__objc_intobj: 0x6d8
+  __AUTH_CONST.__objc_arrayobj: 0x408
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0x3a20
-  __DATA.__objc_ivar: 0x123c
-  __DATA.__data: 0x1308
-  __DATA.__bss: 0x1a0
+  __AUTH.__objc_data: 0x3700
+  __DATA.__objc_ivar: 0x11dc
+  __DATA.__data: 0x12a8
+  __DATA.__bss: 0x168
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/Bom.framework/Versions/A/Bom
   - /System/Library/PrivateFrameworks/CacheDelete.framework/Versions/A/CacheDelete
   - /System/Library/PrivateFrameworks/ConfigurationProfiles.framework/Versions/A/ConfigurationProfiles
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/DesktopServicesPriv
   - /System/Library/PrivateFrameworks/DiskImages.framework/Versions/A/DiskImages
   - /System/Library/PrivateFrameworks/DiskManagement.framework/Versions/A/DiskManagement

   - /usr/lib/libfakelink.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libodfde.dylib
-  - /usr/lib/libsqlite3.dylib
-  UUID: DBA7305B-4817-326D-9E39-9819BACD8B3C
-  Functions: 5692
-  Symbols:   13252
-  CStrings:  14656
+  - /usr/lib/libprequelite.dylib
+  UUID: 68FBC160-8067-3CA1-8DAB-BEEA297A452B
+  Functions: 5474
+  Symbols:   12905
+  CStrings:  13689
 
Symbols:
+ +[NSURL(SMTMExtensions) serverURLForNetworkMountPoint:].cold.1
+ +[SMConfMigrator confMigratorDictionary].cold.1
+ +[SMEngineProgress sharedEngineProgress].cold.1
+ +[SMEngineStep finalSizeAndCount:withFileGroupings:withUsersToTransfer:]
+ +[SMEngineStep findStepOfClass:inSteps:]
+ +[SMManager sharedManager].cold.1
+ +[SMMessageTracing sharedInstance].cold.1
+ +[SMMigrateFilesStep finalSizeAndCount:withFileGroupings:withUsersToTransfer:]
+ +[SMMigrateFilesStep shouldCopyNonSystemReceiptsForUpgrade]
+ +[SMMigrateUserHomesStep copiesHomeDirectoriesForRequest:]
+ +[SMMigrateUserHomesStep finalSizeAndCount:withFileGroupings:withUsersToTransfer:]
+ +[SMMigrateUserHomesStep shouldMigrateUserDataForUser:]
+ +[SMMigrationRequest performSecurityOperation:].cold.1
+ +[SMODDBAccess sharedDBToPathMap].cold.1
+ +[SMODDBAccess sharedQueue].cold.1
+ +[SMPatherRule stringFromContext:]
+ +[SMPatherRule stringFromType:]
+ +[SMPaths pathOverridesPlistPath].cold.1
+ +[SMPaths userDataCategories].cold.1
+ +[SMQuarantineManager sharedManager].cold.1
+ +[SMRunEventHandler sharedInstance]
+ +[SMSandboxTools cleanupSandboxForSystem:atPath:sandBoxPath:].cold.1
+ +[SMSystemRule stringFromActionType:]
+ +[SMSystemRule stringFromContext:]
+ +[SMSystemScanner sharedScanner].cold.1
+ +[SMSystemScanner_Client sharedScannerClient].cold.1
+ +[SMWindowsUser_Daemon randomImageData].cold.1
+ +[SystemMigrationDaemon sharedDaemon].cold.1
+ -[SMCommitDeferredSandboxStep postProcess]
+ -[SMCustomizeTree_Client observeValueForKeyPath:ofObject:change:context:].cold.1
+ -[SMDProgress_XPCClientConnection isCombinedSoftwareUpdateAndMigration:]
+ -[SMEngine .cxx_destruct]
+ -[SMEngine _engineStepPhaseToString:]
+ -[SMEngine acceptNewMigrationRequest:]
+ -[SMEngine acknowledgeCompletedRequest]
+ -[SMEngine addDelegate:]
+ -[SMEngine addRootUserToUsersToTransferInMigrationRequest]
+ -[SMEngine aggregateEngineErrorsAndWarnings]
+ -[SMEngine awaitSystemAvailability]
+ -[SMEngine copyCompletedForPath:]
+ -[SMEngine copyWasCompletedForPath:]
+ -[SMEngine dealloc]
+ -[SMEngine delegate]
+ -[SMEngine deletedBytes]
+ -[SMEngine description]
+ -[SMEngine doneWithCurrentRequest]
+ -[SMEngine enginePhase]
+ -[SMEngine enginePropertiesQueue]
+ -[SMEngine engineQueue]
+ -[SMEngine engineShouldContinue]
+ -[SMEngine engineSourceSystemAvailable]
+ -[SMEngine engineStepsForCurrentMigration]
+ -[SMEngine engineSteps]
+ -[SMEngine engineWaitingForPathing]
+ -[SMEngine ensureSourceIsMounted]
+ -[SMEngine errorWithMessage:]
+ -[SMEngine errorWithMessage:underlyingError:]
+ -[SMEngine error]
+ -[SMEngine fdeNeedsToBeReeanbled]
+ -[SMEngine finalizeAndSendTelemetry]
+ -[SMEngine finally]
+ -[SMEngine finishedBytes]
+ -[SMEngine gatherCompletionMessageTracerData]
+ -[SMEngine getCurrentSystemFromScanner]
+ -[SMEngine init]
+ -[SMEngine isEngineState:]
+ -[SMEngine messageTraceCancellation]
+ -[SMEngine messageTraceStateCompletion]
+ -[SMEngine migrationRequest]
+ -[SMEngine notEnoughFreeSpaceOnTargetError]
+ -[SMEngine observeValueForKeyPath:ofObject:change:context:]
+ -[SMEngine pathingProgressFormatKey:arguments:]
+ -[SMEngine pathingStartTime]
+ -[SMEngine pathsInSandbox]
+ -[SMEngine predetermineTranslatedUIDs]
+ -[SMEngine printEngineDescription]
+ -[SMEngine processAnalyticsData]
+ -[SMEngine processErrors]
+ -[SMEngine requestedDaemonScannerState]
+ -[SMEngine runEngineSteps]
+ -[SMEngine runEngine]
+ -[SMEngine runPather]
+ -[SMEngine run]
+ -[SMEngine saveFinalMigrationDetailsToTheRequestBeforeWeReboot]
+ -[SMEngine setDelegate:]
+ -[SMEngine setDeletedBytes:]
+ -[SMEngine setEnginePhase:]
+ -[SMEngine setEnginePropertiesQueue:]
+ -[SMEngine setEngineQueue:]
+ -[SMEngine setEngineSteps:]
+ -[SMEngine setEngineStepsForCurrentMigration:]
+ -[SMEngine setEngineSteps]
+ -[SMEngine setEngineWaitingForPathing:]
+ -[SMEngine setError:]
+ -[SMEngine setFinishedBytes:]
+ -[SMEngine setMigrationRequest:]
+ -[SMEngine setPathingStartTime:]
+ -[SMEngine setPathsInSandbox:]
+ -[SMEngine setRequestedDaemonScannerState:]
+ -[SMEngine setStartTime:]
+ -[SMEngine setState:]
+ -[SMEngine setTimeDelayedByPathing:]
+ -[SMEngine setTotalBytes:]
+ -[SMEngine setTracingUUID:]
+ -[SMEngine setupEngineBeforeRunningSteps]
+ -[SMEngine setupForDataTransfer]
+ -[SMEngine setupMessageTracing]
+ -[SMEngine shouldContinueSteps]
+ -[SMEngine spaceIsSufficient]
+ -[SMEngine startTime]
+ -[SMEngine startupNewRequest]
+ -[SMEngine state]
+ -[SMEngine stepError:exception:phase:]
+ -[SMEngine stopAllSteps]
+ -[SMEngine stopOrSuspend:]
+ -[SMEngine stop]
+ -[SMEngine suspend]
+ -[SMEngine systemScannerAddedSystem:]
+ -[SMEngine systemScannerRemovedSystem:]
+ -[SMEngine systemScannerSystemChanged:onSystem:]
+ -[SMEngine systemsAreAvailable]
+ -[SMEngine timeDelayedByPathing]
+ -[SMEngine totalBytes]
+ -[SMEngine tracingUUID]
+ -[SMEngine updateUsersToTransferInMigrationRequest]
+ -[SMEngine useSandbox]
+ -[SMEngine userCanceledError]
+ -[SMEngine waitIfSuspended:sourceDisappeared:]
+ -[SMEngineStep .cxx_destruct]
+ -[SMEngineStep addProgress:forKey:]
+ -[SMEngineStep cancel]
+ -[SMEngineStep completedFileCount]
+ -[SMEngineStep completedSize]
+ -[SMEngineStep copyFailedToCopyFile:shouldReportError:]
+ -[SMEngineStep deletedSize]
+ -[SMEngineStep engineStepSupportsResumption]
+ -[SMEngineStep engine]
+ -[SMEngineStep errorWithMessage:code:]
+ -[SMEngineStep errorWithMessage:code:underlyingError:]
+ -[SMEngineStep errors]
+ -[SMEngineStep fatalErrorWithMessage:]
+ -[SMEngineStep fatalErrorWithMessage:underlyingError:]
+ -[SMEngineStep hasProgressForKey:]
+ -[SMEngineStep initWithEngine:]
+ -[SMEngineStep lastCompletedPhase]
+ -[SMEngineStep postProcess]
+ -[SMEngineStep prepare]
+ -[SMEngineStep process]
+ -[SMEngineStep progressArrayForKey:]
+ -[SMEngineStep progressCompletedForKey:]
+ -[SMEngineStep progressDictionaryForKey:]
+ -[SMEngineStep progressForKey:]
+ -[SMEngineStep resumeProcess]
+ -[SMEngineStep setCompletedFileCount:]
+ -[SMEngineStep setCompletedSize:]
+ -[SMEngineStep setDeletedSize:]
+ -[SMEngineStep setEngine:]
+ -[SMEngineStep setErrors:]
+ -[SMEngineStep setLastCompletedPhase:]
+ -[SMEngineStep setProgress:forKey:]
+ -[SMEngineStep setTotalFileCount:]
+ -[SMEngineStep setTotalSize:]
+ -[SMEngineStep setWarnings:]
+ -[SMEngineStep totalFileCount]
+ -[SMEngineStep totalSize]
+ -[SMEngineStep warningWithMessage:]
+ -[SMEngineStep warningWithMessage:underlyingError:]
+ -[SMEngineStep warnings]
+ -[SMMigrateFilesStep .cxx_destruct]
+ -[SMMigrateFilesStep _runCopier]
+ -[SMMigrateFilesStep cancel]
+ -[SMMigrateFilesStep copierFailed:error:]
+ -[SMMigrateFilesStep copyEngineShouldContinueByFastChecking:]
+ -[SMMigrateFilesStep copyPaths]
+ -[SMMigrateFilesStep dedupeWallpaper]
+ -[SMMigrateFilesStep engineStepSupportsResumption]
+ -[SMMigrateFilesStep fileCopyEngine]
+ -[SMMigrateFilesStep kextCacheNeedsUpdate]
+ -[SMMigrateFilesStep postProcess]
+ -[SMMigrateFilesStep prelimFileCount]
+ -[SMMigrateFilesStep preliminarySize:andCount:forPathGroup:]
+ -[SMMigrateFilesStep prepare]
+ -[SMMigrateFilesStep process]
+ -[SMMigrateFilesStep resumeProcess]
+ -[SMMigrateFilesStep setFileCopyEngine:]
+ -[SMMigrateFilesStep setKextCacheNeedsUpdate:]
+ -[SMMigrateFilesStep setPrelimFileCount:]
+ -[SMMigrateFilesStep setupCopiesForFileGroups]
+ -[SMMigrateFilesStep setupCopyNonSystemReceiptsForUpgrade]
+ -[SMMigrateFilesStep setupFileCopyEngine]
+ -[SMMigrateGroupsStep createGroup:inDB:]
+ -[SMMigrateGroupsStep createGroupsInDB:]
+ -[SMMigrateGroupsStep deleteGroup:inDB:]
+ -[SMMigrateGroupsStep migrateGroups]
+ -[SMMigrateGroupsStep postProcess]
+ -[SMMigrateSystemInfoStep .cxx_destruct]
+ -[SMMigrateSystemInfoStep allRuleGroups]
+ -[SMMigrateSystemInfoStep confMigrator]
+ -[SMMigrateSystemInfoStep copierFailed:error:]
+ -[SMMigrateSystemInfoStep copyEngineShouldContinueByFastChecking:]
+ -[SMMigrateSystemInfoStep copyIgnorePremissionsSettings]
+ -[SMMigrateSystemInfoStep copyMachineSettings]
+ -[SMMigrateSystemInfoStep copyNetworkSettings]
+ -[SMMigrateSystemInfoStep copyPaths]
+ -[SMMigrateSystemInfoStep copyRemoteManagementSettings]
+ -[SMMigrateSystemInfoStep copySystemSettings]
+ -[SMMigrateSystemInfoStep copyTimeZone]
+ -[SMMigrateSystemInfoStep copyVirtualMemorySettings]
+ -[SMMigrateSystemInfoStep description]
+ -[SMMigrateSystemInfoStep fileCopyEngine]
+ -[SMMigrateSystemInfoStep finishKerberosSetup]
+ -[SMMigrateSystemInfoStep getLastModifiedDate:]
+ -[SMMigrateSystemInfoStep initWithEngine:]
+ -[SMMigrateSystemInfoStep isHostconfigServiceEnabledOnSourceSystem:]
+ -[SMMigrateSystemInfoStep migrateDirectoryServicesDatabase]
+ -[SMMigrateSystemInfoStep migrateGlobalPreferences]
+ -[SMMigrateSystemInfoStep migrateLockdownModeSetting]
+ -[SMMigrateSystemInfoStep migrateNetworkSettings]
+ -[SMMigrateSystemInfoStep onlyUpdateSystemSettings]
+ -[SMMigrateSystemInfoStep postProcess]
+ -[SMMigrateSystemInfoStep prepareForServerMigration]
+ -[SMMigrateSystemInfoStep prepareKerberosAndServerMigration]
+ -[SMMigrateSystemInfoStep prepare]
+ -[SMMigrateSystemInfoStep process]
+ -[SMMigrateSystemInfoStep repairDatavaultPermissions]
+ -[SMMigrateSystemInfoStep repairTimezonePermissions]
+ -[SMMigrateSystemInfoStep rulesEngineDBClient]
+ -[SMMigrateSystemInfoStep rulesEngineRuleHandler]
+ -[SMMigrateSystemInfoStep setAllRuleGroups:]
+ -[SMMigrateSystemInfoStep setConfMigrator:]
+ -[SMMigrateSystemInfoStep setFileCopyEngine:]
+ -[SMMigrateSystemInfoStep setOnlyUpdateSystemSettings:]
+ -[SMMigrateSystemInfoStep setRulesEngineDBClient:]
+ -[SMMigrateSystemInfoStep setRulesEngineRuleHandler:]
+ -[SMMigrateSystemInfoStep setSettingsCopiers:]
+ -[SMMigrateSystemInfoStep settingsCopiers]
+ -[SMMigrateSystemInfoStep setupFileCopyEngine]
+ -[SMMigrateSystemInfoStep setupKerberos]
+ -[SMMigrateUserHomesStep .cxx_destruct]
+ -[SMMigrateUserHomesStep applyUserTemplateForCopier:]
+ -[SMMigrateUserHomesStep cancel]
+ -[SMMigrateUserHomesStep copierFailed:error:]
+ -[SMMigrateUserHomesStep copierSuceeded:]
+ -[SMMigrateUserHomesStep copiesHomeDirectories]
+ -[SMMigrateUserHomesStep copyEngineShouldContinueByFastChecking:]
+ -[SMMigrateUserHomesStep copyPaths]
+ -[SMMigrateUserHomesStep createComprehensiveCopierForUser:relativeTargetHome:]
+ -[SMMigrateUserHomesStep createCopierForUser:relativeTargetHome:]
+ -[SMMigrateUserHomesStep createHomeDirectoryCopiersForUsers]
+ -[SMMigrateUserHomesStep deletedUsersHomeDirectories]
+ -[SMMigrateUserHomesStep description]
+ -[SMMigrateUserHomesStep engineStepSupportsResumption]
+ -[SMMigrateUserHomesStep fileCopyEngine]
+ -[SMMigrateUserHomesStep postProcess]
+ -[SMMigrateUserHomesStep prepare]
+ -[SMMigrateUserHomesStep processError]
+ -[SMMigrateUserHomesStep process]
+ -[SMMigrateUserHomesStep relativeDestinationUserHomeForUser:]
+ -[SMMigrateUserHomesStep relativeDestinationUserHomeForUserDict:]
+ -[SMMigrateUserHomesStep resumeProcess]
+ -[SMMigrateUserHomesStep runCopier]
+ -[SMMigrateUserHomesStep setFileCopyEngine:]
+ -[SMMigrateUserHomesStep setProcessError:]
+ -[SMMigrateUserHomesStep setUsersToReplace:]
+ -[SMMigrateUserHomesStep setupFileCopyEngine]
+ -[SMMigrateUserHomesStep setupUsersToReplace]
+ -[SMMigrateUserHomesStep usersToReplace]
+ -[SMPatherRule .cxx_destruct]
+ -[SMPatherRule contextFromString:]
+ -[SMPatherRule context]
+ -[SMPatherRule initWithRow:]
+ -[SMPatherRule path]
+ -[SMPatherRule ruleID]
+ -[SMPatherRule typeFromString:]
+ -[SMPatherRule type]
+ -[SMPaths rulesEngineDBClient]
+ -[SMPaths rulesEngineRuleHandler]
+ -[SMPaths setRulesEngineDBClient:]
+ -[SMPaths setRulesEngineRuleHandler:]
+ -[SMProgress_Client isCombinedSoftwareUpdateAndMigration]
+ -[SMRulesEngineDBClient .cxx_destruct]
+ -[SMRulesEngineDBClient connection]
+ -[SMRulesEngineDBClient dealloc]
+ -[SMRulesEngineDBClient getAllPluginPaths]
+ -[SMRulesEngineDBClient getArgumentsByRuleIDSortByArgumentOrder:]
+ -[SMRulesEngineDBClient getChecksumsByFilePath:]
+ -[SMRulesEngineDBClient getPatherRulesByType:]
+ -[SMRulesEngineDBClient getRulesByActionType:]
+ -[SMRulesEngineDBClient getRulesByRuleGroup:]
+ -[SMRulesEngineDBClient init]
+ -[SMRulesEngineDBClient resultSetToSMPatherRule:]
+ -[SMRulesEngineDBClient resultSetToSMSystemRule:]
+ -[SMRulesEngineDBClient setConnection:]
+ -[SMRulesEngineRuleHandler .cxx_destruct]
+ -[SMRulesEngineRuleHandler _destination]
+ -[SMRulesEngineRuleHandler _migrationRequestType]
+ -[SMRulesEngineRuleHandler _source]
+ -[SMRulesEngineRuleHandler clearFirmlinkPathContents:]
+ -[SMRulesEngineRuleHandler copyFirmlinkContents:newPath:]
+ -[SMRulesEngineRuleHandler executeCopyRule:]
+ -[SMRulesEngineRuleHandler executeRule:]
+ -[SMRulesEngineRuleHandler executeToolAtPath:withArguments:andCopyPath:usingDeferral:allowSIP:]
+ -[SMRulesEngineRuleHandler executeToolPathRule:]
+ -[SMRulesEngineRuleHandler generateLegacyServerRulesFromPatherForUnreachablePaths:]
+ -[SMRulesEngineRuleHandler generateTargetPath:]
+ -[SMRulesEngineRuleHandler generatedLegacyServerRules]
+ -[SMRulesEngineRuleHandler initWithSource:destination:]
+ -[SMRulesEngineRuleHandler isApplicableInCurrentBootStage:]
+ -[SMRulesEngineRuleHandler isApplicableRuleForCurrentMigrationType:]
+ -[SMRulesEngineRuleHandler isDeferredCopy:]
+ -[SMRulesEngineRuleHandler isPathFirmlink:]
+ -[SMRulesEngineRuleHandler isPathingRuleApplicableForContext:]
+ -[SMRulesEngineRuleHandler isRuleApplicable:]
+ -[SMRulesEngineRuleHandler isRuleApplicableForContext:]
+ -[SMRulesEngineRuleHandler isRuleApplicableForPather:]
+ -[SMRulesEngineRuleHandler isSkipLegacyRuleInLegacy:]
+ -[SMRulesEngineRuleHandler isSourceLessThanMaximumVersionAllowed:]
+ -[SMRulesEngineRuleHandler isSourceMoreThanMinimumVersionAllowed:]
+ -[SMRulesEngineRuleHandler isSourcePathAppleShippedDefault:]
+ -[SMRulesEngineRuleHandler isSourcePathPresentInSource:]
+ -[SMRulesEngineRuleHandler longTermDestinationSystemIdentifier]
+ -[SMRulesEngineRuleHandler longTermSourceSystemIdentifier]
+ -[SMRulesEngineRuleHandler processRuleGroup:]
+ -[SMRulesEngineRuleHandler renameConflictingPathOnTarget:fullTargetPath:targetPath:deferredCopy:]
+ -[SMRulesEngineRuleHandler rulesEngineDBClient]
+ -[SMRulesEngineRuleHandler setGeneratedLegacyServerRules:]
+ -[SMRulesEngineRuleHandler setLongTermDestinationSystemIdentifier:]
+ -[SMRulesEngineRuleHandler setLongTermSourceSystemIdentifier:]
+ -[SMRulesEngineRuleHandler setRulesEngineDBClient:]
+ -[SMRulesEngineRuleHandler sourceVersion]
+ -[SMRulesEngineRuleHandler stringBySubstitutingEnvironmentVariablesInString:environment:]
+ -[SMRunEventHandler .cxx_destruct]
+ -[SMRunEventHandler addDuration:forStep:]
+ -[SMRunEventHandler generateStateTrackerKeyForStep:phase:]
+ -[SMRunEventHandler getPayloadDictionary]
+ -[SMRunEventHandler getRunType:]
+ -[SMRunEventHandler init]
+ -[SMRunEventHandler payloadKeyForStepDuration:]
+ -[SMRunEventHandler payload]
+ -[SMRunEventHandler recordCompletion]
+ -[SMRunEventHandler recordDataSize:]
+ -[SMRunEventHandler recordDisconnect]
+ -[SMRunEventHandler recordError:errorCode:]
+ -[SMRunEventHandler recordFatalFailure]
+ -[SMRunEventHandler recordInitialConnectionType:]
+ -[SMRunEventHandler recordPathingDuration:]
+ -[SMRunEventHandler recordStop]
+ -[SMRunEventHandler recordSuccess]
+ -[SMRunEventHandler recordSuspend]
+ -[SMRunEventHandler recordTotalDuration:]
+ -[SMRunEventHandler sendEvent]
+ -[SMRunEventHandler setGeneralKeys:]
+ -[SMRunEventHandler setPayload:]
+ -[SMRunEventHandler setStateTracker:phase:]
+ -[SMRunEventHandler stringForPhase:]
+ -[SMRunEventPayload .cxx_destruct]
+ -[SMRunEventPayload AttemptPeerToPeerStepDuration]
+ -[SMRunEventPayload CommitDeferredSandboxStepDuration]
+ -[SMRunEventPayload MigrateAutoLoginUserStepDuration]
+ -[SMRunEventPayload MigrateFilesStepDuration]
+ -[SMRunEventPayload MigrateGroupsStepDuration]
+ -[SMRunEventPayload MigrateGuestAccountStepDuration]
+ -[SMRunEventPayload MigrateSystemInfoStepDuration]
+ -[SMRunEventPayload MigrateUserAccountsStepDuration]
+ -[SMRunEventPayload MigrateUserHomesStepDuration]
+ -[SMRunEventPayload ShoveStepDuration]
+ -[SMRunEventPayload dataSize]
+ -[SMRunEventPayload disconnectCount]
+ -[SMRunEventPayload errorString]
+ -[SMRunEventPayload init]
+ -[SMRunEventPayload initialConnectionType]
+ -[SMRunEventPayload isCompleted]
+ -[SMRunEventPayload isFatalFailure]
+ -[SMRunEventPayload isPreReboot]
+ -[SMRunEventPayload isSuccess]
+ -[SMRunEventPayload pathingDuration]
+ -[SMRunEventPayload runType]
+ -[SMRunEventPayload sessionID]
+ -[SMRunEventPayload setAttemptPeerToPeerStepDuration:]
+ -[SMRunEventPayload setCommitDeferredSandboxStepDuration:]
+ -[SMRunEventPayload setDataSize:]
+ -[SMRunEventPayload setDisconnectCount:]
+ -[SMRunEventPayload setErrorString:]
+ -[SMRunEventPayload setInitialConnectionType:]
+ -[SMRunEventPayload setIsCompleted:]
+ -[SMRunEventPayload setIsFatalFailure:]
+ -[SMRunEventPayload setIsPreReboot:]
+ -[SMRunEventPayload setIsSuccess:]
+ -[SMRunEventPayload setMigrateAutoLoginUserStepDuration:]
+ -[SMRunEventPayload setMigrateFilesStepDuration:]
+ -[SMRunEventPayload setMigrateGroupsStepDuration:]
+ -[SMRunEventPayload setMigrateGuestAccountStepDuration:]
+ -[SMRunEventPayload setMigrateSystemInfoStepDuration:]
+ -[SMRunEventPayload setMigrateUserAccountsStepDuration:]
+ -[SMRunEventPayload setMigrateUserHomesStepDuration:]
+ -[SMRunEventPayload setPathingDuration:]
+ -[SMRunEventPayload setRunType:]
+ -[SMRunEventPayload setSessionID:]
+ -[SMRunEventPayload setShoveStepDuration:]
+ -[SMRunEventPayload setSourceModel:]
+ -[SMRunEventPayload setSourceVersion:]
+ -[SMRunEventPayload setStateTracker:]
+ -[SMRunEventPayload setStopRequested:]
+ -[SMRunEventPayload setSuspendCount:]
+ -[SMRunEventPayload setTotalDuration:]
+ -[SMRunEventPayload sourceModel]
+ -[SMRunEventPayload sourceVersion]
+ -[SMRunEventPayload stateTracker]
+ -[SMRunEventPayload stopRequested]
+ -[SMRunEventPayload suspendCount]
+ -[SMRunEventPayload totalDuration]
+ -[SMShoveStep process]
+ -[SMStopwatch elapsedTime]
+ -[SMStopwatch isRunning]
+ -[SMStopwatch setIsRunning:]
+ -[SMStopwatch setStartTime:]
+ -[SMStopwatch startTime]
+ -[SMStopwatch start]
+ -[SMStopwatch stop]
+ -[SMSystemRule initWithUnreachableLegacyPath:]
+ -[SMSystem_Daemon_RemoteDiskShare mountNetAuth:].cold.1
+ -[SMSystem_Daemon_RemoteTMDiskShare mountNetAuth:].cold.1
+ -[SMSystem_Daemon_RemoteTMDiskShare mountNetAuth:].cold.2
+ -[SMWindowsImportUserDataStep initWithEngine:map:]
+ -[SMWindowsMigrateComponentStep initWithEngine:map:]
+ -[SMWindowsMigrateUserAccountsStep initWithEngine:map:]
+ GCC_except_table161
+ GCC_except_table24
+ GCC_except_table61
+ GCC_except_table71
+ GCC_except_table74
+ OBJC_IVAR_$_SMEngine._delegate
+ OBJC_IVAR_$_SMEngine._deletedBytes
+ OBJC_IVAR_$_SMEngine._enginePhase
+ OBJC_IVAR_$_SMEngine._enginePropertiesQueue
+ OBJC_IVAR_$_SMEngine._engineQueue
+ OBJC_IVAR_$_SMEngine._engineSteps
+ OBJC_IVAR_$_SMEngine._engineStepsForCurrentMigration
+ OBJC_IVAR_$_SMEngine._engineWaitingForPathing
+ OBJC_IVAR_$_SMEngine._error
+ OBJC_IVAR_$_SMEngine._finishedBytes
+ OBJC_IVAR_$_SMEngine._migrationRequest
+ OBJC_IVAR_$_SMEngine._pathingStartTime
+ OBJC_IVAR_$_SMEngine._pathsInSandbox
+ OBJC_IVAR_$_SMEngine._requestedDaemonScannerState
+ OBJC_IVAR_$_SMEngine._startTime
+ OBJC_IVAR_$_SMEngine._state
+ OBJC_IVAR_$_SMEngine._timeDelayedByPathing
+ OBJC_IVAR_$_SMEngine._totalBytes
+ OBJC_IVAR_$_SMEngine._tracingUUID
+ OBJC_IVAR_$_SMEngineStep._completedFileCount
+ OBJC_IVAR_$_SMEngineStep._completedSize
+ OBJC_IVAR_$_SMEngineStep._deletedSize
+ OBJC_IVAR_$_SMEngineStep._errors
+ OBJC_IVAR_$_SMEngineStep._lastCompletedPhase
+ OBJC_IVAR_$_SMEngineStep._totalFileCount
+ OBJC_IVAR_$_SMEngineStep._totalSize
+ OBJC_IVAR_$_SMEngineStep._warnings
+ OBJC_IVAR_$_SMEngineStep.engine
+ OBJC_IVAR_$_SMMigrateFilesStep._fileCopyEngine
+ OBJC_IVAR_$_SMMigrateFilesStep._kextCacheNeedsUpdate
+ OBJC_IVAR_$_SMMigrateFilesStep._prelimFileCount
+ OBJC_IVAR_$_SMMigrateSystemInfoStep._allRuleGroups
+ OBJC_IVAR_$_SMMigrateSystemInfoStep._confMigrator
+ OBJC_IVAR_$_SMMigrateSystemInfoStep._fileCopyEngine
+ OBJC_IVAR_$_SMMigrateSystemInfoStep._onlyUpdateSystemSettings
+ OBJC_IVAR_$_SMMigrateSystemInfoStep._rulesEngineDBClient
+ OBJC_IVAR_$_SMMigrateSystemInfoStep._rulesEngineRuleHandler
+ OBJC_IVAR_$_SMMigrateSystemInfoStep._settingsCopiers
+ OBJC_IVAR_$_SMMigrateUserHomesStep._fileCopyEngine
+ OBJC_IVAR_$_SMMigrateUserHomesStep._processError
+ OBJC_IVAR_$_SMMigrateUserHomesStep._usersToReplace
+ OBJC_IVAR_$_SMPatherRule._context
+ OBJC_IVAR_$_SMPatherRule._path
+ OBJC_IVAR_$_SMPatherRule._ruleID
+ OBJC_IVAR_$_SMPatherRule._type
+ OBJC_IVAR_$_SMPaths._rulesEngineDBClient
+ OBJC_IVAR_$_SMPaths._rulesEngineRuleHandler
+ OBJC_IVAR_$_SMRulesEngineDBClient._connection
+ OBJC_IVAR_$_SMRulesEngineRuleHandler._generatedLegacyServerRules
+ OBJC_IVAR_$_SMRulesEngineRuleHandler._longTermDestinationSystemIdentifier
+ OBJC_IVAR_$_SMRulesEngineRuleHandler._longTermSourceSystemIdentifier
+ OBJC_IVAR_$_SMRulesEngineRuleHandler._rulesEngineDBClient
+ OBJC_IVAR_$_SMRunEventHandler._payload
+ OBJC_IVAR_$_SMRunEventPayload._AttemptPeerToPeerStepDuration
+ OBJC_IVAR_$_SMRunEventPayload._CommitDeferredSandboxStepDuration
+ OBJC_IVAR_$_SMRunEventPayload._MigrateAutoLoginUserStepDuration
+ OBJC_IVAR_$_SMRunEventPayload._MigrateFilesStepDuration
+ OBJC_IVAR_$_SMRunEventPayload._MigrateGroupsStepDuration
+ OBJC_IVAR_$_SMRunEventPayload._MigrateGuestAccountStepDuration
+ OBJC_IVAR_$_SMRunEventPayload._MigrateSystemInfoStepDuration
+ OBJC_IVAR_$_SMRunEventPayload._MigrateUserAccountsStepDuration
+ OBJC_IVAR_$_SMRunEventPayload._MigrateUserHomesStepDuration
+ OBJC_IVAR_$_SMRunEventPayload._ShoveStepDuration
+ OBJC_IVAR_$_SMRunEventPayload._dataSize
+ OBJC_IVAR_$_SMRunEventPayload._disconnectCount
+ OBJC_IVAR_$_SMRunEventPayload._errorString
+ OBJC_IVAR_$_SMRunEventPayload._initialConnectionType
+ OBJC_IVAR_$_SMRunEventPayload._isCompleted
+ OBJC_IVAR_$_SMRunEventPayload._isFatalFailure
+ OBJC_IVAR_$_SMRunEventPayload._isPreReboot
+ OBJC_IVAR_$_SMRunEventPayload._isSuccess
+ OBJC_IVAR_$_SMRunEventPayload._pathingDuration
+ OBJC_IVAR_$_SMRunEventPayload._runType
+ OBJC_IVAR_$_SMRunEventPayload._sessionID
+ OBJC_IVAR_$_SMRunEventPayload._sourceModel
+ OBJC_IVAR_$_SMRunEventPayload._sourceVersion
+ OBJC_IVAR_$_SMRunEventPayload._stateTracker
+ OBJC_IVAR_$_SMRunEventPayload._stopRequested
+ OBJC_IVAR_$_SMRunEventPayload._suspendCount
+ OBJC_IVAR_$_SMRunEventPayload._totalDuration
+ OBJC_IVAR_$_SMStopwatch._isRunning
+ OBJC_IVAR_$_SMStopwatch._startTime
+ _AnalyticsSendEvent
+ _CFAbsoluteTimeGetCurrent
+ _NSSelectorFromString
+ _OBJC_CLASS_$_PQLConnection
+ _OBJC_CLASS_$_SMCommitDeferredSandboxStep
+ _OBJC_CLASS_$_SMEngine
+ _OBJC_CLASS_$_SMEngineStep
+ _OBJC_CLASS_$_SMMigrateFilesStep
+ _OBJC_CLASS_$_SMMigrateGroupsStep
+ _OBJC_CLASS_$_SMMigrateSystemInfoStep
+ _OBJC_CLASS_$_SMMigrateUserHomesStep
+ _OBJC_CLASS_$_SMPatherRule
+ _OBJC_CLASS_$_SMRulesEngineDBClient
+ _OBJC_CLASS_$_SMRulesEngineRuleHandler
+ _OBJC_CLASS_$_SMRunEventHandler
+ _OBJC_CLASS_$_SMRunEventPayload
+ _OBJC_CLASS_$_SMShoveStep
+ _OBJC_CLASS_$_SMStopwatch
+ _OBJC_CLASS_$_SMSystemRulePlugin
+ _OBJC_METACLASS_$_SMCommitDeferredSandboxStep
+ _OBJC_METACLASS_$_SMEngine
+ _OBJC_METACLASS_$_SMEngineStep
+ _OBJC_METACLASS_$_SMMigrateFilesStep
+ _OBJC_METACLASS_$_SMMigrateGroupsStep
+ _OBJC_METACLASS_$_SMMigrateSystemInfoStep
+ _OBJC_METACLASS_$_SMMigrateUserHomesStep
+ _OBJC_METACLASS_$_SMPatherRule
+ _OBJC_METACLASS_$_SMRulesEngineDBClient
+ _OBJC_METACLASS_$_SMRulesEngineRuleHandler
+ _OBJC_METACLASS_$_SMRunEventHandler
+ _OBJC_METACLASS_$_SMRunEventPayload
+ _OBJC_METACLASS_$_SMShoveStep
+ _OBJC_METACLASS_$_SMStopwatch
+ _OBJC_METACLASS_$_SMSystemRulePlugin
+ _SMAttemptPeerToPeerStepDurationKey
+ _SMCommitDeferredSandboxStepDurationKey
+ _SMDataSizeKey
+ _SMDisconnectCountKey
+ _SMEngineErrorDomain
+ _SMErrorStringKey
+ _SMInitialConnectionTypeKey
+ _SMIsCompletedKey
+ _SMIsFatalFailureKey
+ _SMIsPreRebootKey
+ _SMIsSuccessKey
+ _SMMigrateAutoLoginUserStepDurationKey
+ _SMMigrateFilesStepDurationKey
+ _SMMigrateGroupsStepDurationKey
+ _SMMigrateGuestAccountStepDurationKey
+ _SMMigrateSystemInfoStepDurationKey
+ _SMMigrateUserAccountsStepDurationKey
+ _SMMigrateUserHomesStepDurationKey
+ _SMPathingDurationKey
+ _SMRunTypeKey
+ _SMSessionIDKey
+ _SMShoveStepDurationKey
+ _SMSourceModelKey
+ _SMSourceVersionKey
+ _SMStateTrackerKey
+ _SMStopRequestedKey
+ _SMSuspendCountKey
+ _SMTotalDurationKey
+ __113-[MigrationHelper_Client encryptDiskWithiCloudUser:iCloudPassword:localUser:localPassword:andBag:returningError:]_block_invoke.50
+ __19-[SMCopyEngine run]_block_invoke.52
+ __21-[SMEngine setState:]_block_invoke.37
+ __27-[SMPaths loadAllFakelinks]_block_invoke.290
+ __30-[SMPaths enumerateFilesystem]_block_invoke.356
+ __31-[SMEngine systemsAreAvailable]_block_invoke.143
+ __38-[SMEngine acceptNewMigrationRequest:]_block_invoke.177
+ __39-[SMEngine systemScannerRemovedSystem:]_block_invoke.98
+ __46-[SMSystemScanner changeScanningStateFrom:to:]_block_invoke.cold.1
+ __67-[MigrationHelper_Client doImportWithParameters:desktopPictureURL:]_block_invoke.48
+ __70-[SMUIDGIDTranslator translatedUID:andGID:forOldUID:andOldGID:ofType:]_block_invoke.cold.1
+ __71+[SMSandboxTools shoveSandboxAtPath:sandBoxPath:destinationPath:error:]_block_invoke.74
+ __OBJC_$_CLASS_METHODS_SMEngineStep
+ __OBJC_$_CLASS_METHODS_SMMigrateFilesStep
+ __OBJC_$_CLASS_METHODS_SMMigrateUserHomesStep
+ __OBJC_$_CLASS_METHODS_SMPatherRule
+ __OBJC_$_CLASS_METHODS_SMRunEventHandler
+ __OBJC_$_INSTANCE_METHODS_SMCommitDeferredSandboxStep
+ __OBJC_$_INSTANCE_METHODS_SMEngine
+ __OBJC_$_INSTANCE_METHODS_SMEngineStep
+ __OBJC_$_INSTANCE_METHODS_SMMigrateFilesStep
+ __OBJC_$_INSTANCE_METHODS_SMMigrateGroupsStep
+ __OBJC_$_INSTANCE_METHODS_SMMigrateSystemInfoStep
+ __OBJC_$_INSTANCE_METHODS_SMMigrateUserHomesStep
+ __OBJC_$_INSTANCE_METHODS_SMPatherRule
+ __OBJC_$_INSTANCE_METHODS_SMRulesEngineDBClient
+ __OBJC_$_INSTANCE_METHODS_SMRulesEngineRuleHandler
+ __OBJC_$_INSTANCE_METHODS_SMRunEventHandler
+ __OBJC_$_INSTANCE_METHODS_SMRunEventPayload
+ __OBJC_$_INSTANCE_METHODS_SMShoveStep
+ __OBJC_$_INSTANCE_METHODS_SMStopwatch
+ __OBJC_$_INSTANCE_VARIABLES_SMEngine
+ __OBJC_$_INSTANCE_VARIABLES_SMEngineStep
+ __OBJC_$_INSTANCE_VARIABLES_SMMigrateFilesStep
+ __OBJC_$_INSTANCE_VARIABLES_SMMigrateSystemInfoStep
+ __OBJC_$_INSTANCE_VARIABLES_SMMigrateUserHomesStep
+ __OBJC_$_INSTANCE_VARIABLES_SMPatherRule
+ __OBJC_$_INSTANCE_VARIABLES_SMRulesEngineDBClient
+ __OBJC_$_INSTANCE_VARIABLES_SMRulesEngineRuleHandler
+ __OBJC_$_INSTANCE_VARIABLES_SMRunEventHandler
+ __OBJC_$_INSTANCE_VARIABLES_SMRunEventPayload
+ __OBJC_$_INSTANCE_VARIABLES_SMStopwatch
+ __OBJC_$_PROP_LIST_SMEngine
+ __OBJC_$_PROP_LIST_SMEngineStep
+ __OBJC_$_PROP_LIST_SMMigrateFilesStep
+ __OBJC_$_PROP_LIST_SMMigrateSystemInfoStep
+ __OBJC_$_PROP_LIST_SMMigrateUserHomesStep
+ __OBJC_$_PROP_LIST_SMPatherRule
+ __OBJC_$_PROP_LIST_SMRulesEngineDBClient
+ __OBJC_$_PROP_LIST_SMRulesEngineRuleHandler
+ __OBJC_$_PROP_LIST_SMRunEventHandler
+ __OBJC_$_PROP_LIST_SMRunEventPayload
+ __OBJC_$_PROP_LIST_SMStopwatch
+ __OBJC_CLASS_PROTOCOLS_$_SMEngine
+ __OBJC_CLASS_PROTOCOLS_$_SMEngineStep
+ __OBJC_CLASS_PROTOCOLS_$_SMMigrateFilesStep
+ __OBJC_CLASS_PROTOCOLS_$_SMMigrateSystemInfoStep
+ __OBJC_CLASS_PROTOCOLS_$_SMMigrateUserHomesStep
+ __OBJC_CLASS_RO_$_SMCommitDeferredSandboxStep
+ __OBJC_CLASS_RO_$_SMEngine
+ __OBJC_CLASS_RO_$_SMEngineStep
+ __OBJC_CLASS_RO_$_SMMigrateFilesStep
+ __OBJC_CLASS_RO_$_SMMigrateGroupsStep
+ __OBJC_CLASS_RO_$_SMMigrateSystemInfoStep
+ __OBJC_CLASS_RO_$_SMMigrateUserHomesStep
+ __OBJC_CLASS_RO_$_SMPatherRule
+ __OBJC_CLASS_RO_$_SMRulesEngineDBClient
+ __OBJC_CLASS_RO_$_SMRulesEngineRuleHandler
+ __OBJC_CLASS_RO_$_SMRunEventHandler
+ __OBJC_CLASS_RO_$_SMRunEventPayload
+ __OBJC_CLASS_RO_$_SMShoveStep
+ __OBJC_CLASS_RO_$_SMStopwatch
+ __OBJC_CLASS_RO_$_SMSystemRulePlugin
+ __OBJC_METACLASS_RO_$_SMCommitDeferredSandboxStep
+ __OBJC_METACLASS_RO_$_SMEngine
+ __OBJC_METACLASS_RO_$_SMEngineStep
+ __OBJC_METACLASS_RO_$_SMMigrateFilesStep
+ __OBJC_METACLASS_RO_$_SMMigrateGroupsStep
+ __OBJC_METACLASS_RO_$_SMMigrateSystemInfoStep
+ __OBJC_METACLASS_RO_$_SMMigrateUserHomesStep
+ __OBJC_METACLASS_RO_$_SMPatherRule
+ __OBJC_METACLASS_RO_$_SMRulesEngineDBClient
+ __OBJC_METACLASS_RO_$_SMRulesEngineRuleHandler
+ __OBJC_METACLASS_RO_$_SMRunEventHandler
+ __OBJC_METACLASS_RO_$_SMRunEventPayload
+ __OBJC_METACLASS_RO_$_SMShoveStep
+ __OBJC_METACLASS_RO_$_SMStopwatch
+ __OBJC_METACLASS_RO_$_SMSystemRulePlugin
+ ___15-[SMEngine run]_block_invoke
+ ___15-[SMEngine run]_block_invoke_2
+ ___17-[SMEngine state]_block_invoke
+ ___19-[SMEngine finally]_block_invoke
+ ___21-[SMEngine runEngine]_block_invoke
+ ___21-[SMEngine setState:]_block_invoke
+ ___21-[SMEngine setState:]_block_invoke_2
+ ___23-[SMEngine enginePhase]_block_invoke
+ ___25-[SMEngine processErrors]_block_invoke
+ ___27-[SMEngine setEnginePhase:]_block_invoke
+ ___29-[SMEngine startupNewRequest]_block_invoke
+ ___31-[SMEngine systemsAreAvailable]_block_invoke
+ ___31-[SMEngine systemsAreAvailable]_block_invoke_2
+ ___31-[SMEngine systemsAreAvailable]_block_invoke_3
+ ___31-[SMPaths pathOverridesOfType:]_block_invoke
+ ___32-[SMEngine setupForDataTransfer]_block_invoke
+ ___33-[SMEngine ensureSourceIsMounted]_block_invoke
+ ___35+[SMRunEventHandler sharedInstance]_block_invoke
+ ___35-[SMEngine awaitSystemAvailability]_block_invoke
+ ___35-[SMPaths allConfMigratorCopyPaths]_block_invoke
+ ___35-[SMPaths allConfMigratorKeepPaths]_block_invoke
+ ___35-[SMPaths allConfMigratorKillPaths]_block_invoke
+ ___35-[SMPaths allConfMigratorToolPaths]_block_invoke
+ ___35-[SMPaths allConfMigratorToolPaths]_block_invoke_2
+ ___35-[SMPaths allConfMigratorUserPaths]_block_invoke
+ ___37-[SMEngine systemScannerAddedSystem:]_block_invoke
+ ___37-[SMMigrateFilesStep dedupeWallpaper]_block_invoke
+ ___37-[SMMigrateFilesStep dedupeWallpaper]_block_invoke_2
+ ___38-[SMEngine acceptNewMigrationRequest:]_block_invoke
+ ___38-[SMMigrateSystemInfoStep postProcess]_block_invoke
+ ___39-[SMEngine systemScannerRemovedSystem:]_block_invoke
+ ___44-[SMEngine aggregateEngineErrorsAndWarnings]_block_invoke
+ ___44-[SMEngine aggregateEngineErrorsAndWarnings]_block_invoke_2
+ ___44-[SMEngine aggregateEngineErrorsAndWarnings]_block_invoke_3
+ ___44-[SMEngine aggregateEngineErrorsAndWarnings]_block_invoke_4
+ ___46-[SMMigrateFilesStep setupCopiesForFileGroups]_block_invoke
+ ___48-[SMEngine systemScannerSystemChanged:onSystem:]_block_invoke
+ ___52-[SMMigrateSystemInfoStep repairTimezonePermissions]_block_invoke
+ ___57-[SMProgress_Client isCombinedSoftwareUpdateAndMigration]_block_invoke
+ ___78+[SMMigrateFilesStep finalSizeAndCount:withFileGroupings:withUsersToTransfer:]_block_invoke
+ ___block_descriptor_32_e39_B24?0"SMSystemRule"8"NSDictionary"16l
+ ___block_descriptor_32_e39_q24?0"SMEngineStep"8"SMEngineStep"16l
+ ___block_descriptor_40_e8_32s_e39_B24?0"SMPatherRule"8"NSDictionary"16l
+ ___block_descriptor_40_e8_32s_e39_B24?0"SMSystemRule"8"NSDictionary"16l
+ ___sortStepsAccordingToOrder_block_invoke
+ __block_literal_global.158
+ __block_literal_global.259
+ __block_literal_global.35
+ __block_literal_global.41
+ __block_literal_global.46
+ __block_literal_global.95
+ _class_getName
+ _generateMachineSettingsStep
+ _generateStepsForEngineForMac
+ _generateStepsForEngineForWindows
+ _kCFURLFileIdentifierKey
+ _objc_msgSend$AttemptPeerToPeerStepDuration
+ _objc_msgSend$CommitDeferredSandboxStepDuration
+ _objc_msgSend$MigrateAutoLoginUserStepDuration
+ _objc_msgSend$MigrateFilesStepDuration
+ _objc_msgSend$MigrateGroupsStepDuration
+ _objc_msgSend$MigrateGuestAccountStepDuration
+ _objc_msgSend$MigrateSystemInfoStepDuration
+ _objc_msgSend$MigrateUserAccountsStepDuration
+ _objc_msgSend$MigrateUserHomesStepDuration
+ _objc_msgSend$ShoveStepDuration
+ _objc_msgSend$_engineStepPhaseToString:
+ _objc_msgSend$addDuration:forStep:
+ _objc_msgSend$close:
+ _objc_msgSend$dataSize
+ _objc_msgSend$disconnectCount
+ _objc_msgSend$diskImagesInDirectory:qos:error:
+ _objc_msgSend$elapsedTime
+ _objc_msgSend$executeCopyRule:
+ _objc_msgSend$executeRule:
+ _objc_msgSend$executeToolPathRule:
+ _objc_msgSend$fetch:
+ _objc_msgSend$finalizeAndSendTelemetry
+ _objc_msgSend$generateLegacyServerRulesFromPatherForUnreachablePaths:
+ _objc_msgSend$generateStateTrackerKeyForStep:phase:
+ _objc_msgSend$generateTargetPath:
+ _objc_msgSend$generatedLegacyServerRules
+ _objc_msgSend$getPatherRulesByType:
+ _objc_msgSend$getPayloadDictionary
+ _objc_msgSend$getRulesByActionType:
+ _objc_msgSend$getRunType:
+ _objc_msgSend$initWithEngine:map:
+ _objc_msgSend$initWithUnreachableLegacyPath:
+ _objc_msgSend$initialConnectionType
+ _objc_msgSend$instancesRespondToSelector:
+ _objc_msgSend$intAtIndex:
+ _objc_msgSend$isApplicableRuleForCurrentMigrationType:
+ _objc_msgSend$isCombinedSoftwareUpdateAndMigration:
+ _objc_msgSend$isCompleted
+ _objc_msgSend$isDeferredCopy:
+ _objc_msgSend$isFatalFailure
+ _objc_msgSend$isPathPlatformBinary
+ _objc_msgSend$isPathingRuleApplicableForContext:
+ _objc_msgSend$isPreReboot
+ _objc_msgSend$isRuleApplicableForContext:
+ _objc_msgSend$isRuleApplicableForPather:
+ _objc_msgSend$isSourcePathAppleShippedDefault:
+ _objc_msgSend$isSourcePathPresentInSource:
+ _objc_msgSend$isSuccess
+ _objc_msgSend$longLongAtIndex:
+ _objc_msgSend$next
+ _objc_msgSend$openAtURL:withFlags:error:
+ _objc_msgSend$pathingDuration
+ _objc_msgSend$payloadKeyForStepDuration:
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$prepareKerberosAndServerMigration
+ _objc_msgSend$printEngineDescription
+ _objc_msgSend$processRuleGroup:
+ _objc_msgSend$recordCompletion
+ _objc_msgSend$recordDataSize:
+ _objc_msgSend$recordDisconnect
+ _objc_msgSend$recordError:errorCode:
+ _objc_msgSend$recordFatalFailure
+ _objc_msgSend$recordInitialConnectionType:
+ _objc_msgSend$recordPathingDuration:
+ _objc_msgSend$recordStop
+ _objc_msgSend$recordSuccess
+ _objc_msgSend$recordSuspend
+ _objc_msgSend$recordTotalDuration:
+ _objc_msgSend$renameConflictingPathOnTarget:fullTargetPath:targetPath:deferredCopy:
+ _objc_msgSend$resultSetToSMPatherRule:
+ _objc_msgSend$resultSetToSMSystemRule:
+ _objc_msgSend$rulesEngineDBClient
+ _objc_msgSend$rulesEngineRuleHandler
+ _objc_msgSend$runEngineSteps
+ _objc_msgSend$runPather
+ _objc_msgSend$runType
+ _objc_msgSend$sendEvent
+ _objc_msgSend$sessionID
+ _objc_msgSend$setDataSize:
+ _objc_msgSend$setDisconnectCount:
+ _objc_msgSend$setEngineSteps
+ _objc_msgSend$setGeneralKeys:
+ _objc_msgSend$setGeneratedLegacyServerRules:
+ _objc_msgSend$setInitialConnectionType:
+ _objc_msgSend$setIsCompleted:
+ _objc_msgSend$setIsFatalFailure:
+ _objc_msgSend$setIsPreReboot:
+ _objc_msgSend$setIsRunning:
+ _objc_msgSend$setIsSuccess:
+ _objc_msgSend$setPathingDuration:
+ _objc_msgSend$setRulesEngineDBClient:
+ _objc_msgSend$setRulesEngineRuleHandler:
+ _objc_msgSend$setRunType:
+ _objc_msgSend$setSourceModel:
+ _objc_msgSend$setSourceVersion:
+ _objc_msgSend$setStateTracker:
+ _objc_msgSend$setStateTracker:phase:
+ _objc_msgSend$setStopRequested:
+ _objc_msgSend$setSuspendCount:
+ _objc_msgSend$setTotalDuration:
+ _objc_msgSend$setupEngineBeforeRunningSteps
+ _objc_msgSend$setupForDataTransfer
+ _objc_msgSend$shouldContinueSteps
+ _objc_msgSend$sourceModel
+ _objc_msgSend$stateTracker
+ _objc_msgSend$stopRequested
+ _objc_msgSend$stringAtIndex:
+ _objc_msgSend$stringFromActionType:
+ _objc_msgSend$stringFromType:
+ _objc_msgSend$suspendCount
+ _objc_msgSend$totalDuration
+ _objc_msgSend$typeFromString:
+ _os_variant_has_internal_ui
+ _sortStepsAccordingToOrder
+ sharedInstance.sharedInstance
- +[NSProcessInfo(PIDByName) lookupProcessIdentifierByName:]
- +[SMConfMigratorAllowlist allowlist]
- +[SMConfMigratorAllowlist initialize]
- +[SMConfMigratorAllowlist isAllowed:]
- +[SMConfMigratorBundle bundleComponentVersion:]
- +[SMConfMigratorBundle isBundle:]
- +[SMConfMigratorBundle isNewerBundle:thanBundle:]
- +[SMConfMigratorRules initialize]
- +[SMConfMigratorRules rules]
- +[SMMigrateFiles finalSizeAndCount:withFileGroupings:withUsersToTransfer:]
- +[SMMigrateFiles shouldCopyNonSystemReceiptsForUpgrade]
- +[SMMigrateUserDataStep copiesHomeDirectoriesForRequest:]
- +[SMMigrateUserDataStep finalSizeAndCount:withFileGroupings:withUsersToTransfer:]
- +[SMMigrateUserDataStep shouldMigrateUserDataForUser:]
- +[SMMigrateUserToolBox verifyAndCreateIAUserWithPassword:]
- +[SMMigrationEngineStep finalSizeAndCount:withFileGroupings:withUsersToTransfer:]
- +[SMMigrationEngineStep findStepOfClass:inSteps:]
- +[SMMigrationEngineStep stringForPhase:]
- +[SMMigrationReport sharedReport]
- +[SMPathGroups applicationGroupBundlesToLocalizeFromPather:]
- +[SMPaths platformBinaryExceptions]
- +[SMSandboxTools shoveSandboxAtPath:sandBoxPath:error:]
- +[SMSystemRuleClient sharedClient]
- +[SMUserConflictResolver _findNextNumberAbove:inSet:]
- -[SMAttemptPeerToPeerStep estimatedTimeToCompletePhase:]
- -[SMCommitDeferredSandboxElement estimatedTimeToComplete]
- -[SMCommitDeferredSandboxElement run]
- -[SMConfMigrator migrateAllSettingsWithGroupName2:]
- -[SMConfMigrator migrateWithRule2:]
- -[SMConfMigrator parentProgressPendingUnits]
- -[SMConfMigrator parentProgress]
- -[SMConfMigrator setParentProgress:]
- -[SMConfMigrator setParentProgressPendingUnits:]
- -[SMConfMigratorCopyRule defaultedCopyRule]
- -[SMConfMigratorCopyRule initWithPath:]
- -[SMConfMigratorRunToolRule initWithPath:arguments:runsAfterRestart:]
- -[SMConfMigratorUserPathRule initWithPath:]
- -[SMCopyEngine estimatedTimeRemaining]
- -[SMCopyEngine estimatedTimeToComplete]
- -[SMCopyEngine parentProgressPendingUnits]
- -[SMCopyEngine parentProgress]
- -[SMCopyEngine progressString]
- -[SMCopyEngine progress]
- -[SMCopyEngine setParentProgress:]
- -[SMCopyEngine setParentProgressPendingUnits:]
- -[SMCopyEngine setProgress:]
- -[SMCopyEngine setProgressString:]
- -[SMCopyEngineCopier parentProgressPendingUnits]
- -[SMCopyEngineCopier parentProgress]
- -[SMCopyEngineCopier progressString]
- -[SMCopyEngineCopier progress]
- -[SMCopyEngineCopier setParentProgress:]
- -[SMCopyEngineCopier setParentProgressPendingUnits:]
- -[SMCopyEngineCopier setProgress:]
- -[SMCopyEngineCopier setProgressString:]
- -[SMCopyEngineFileCopier hasExcludedPaths]
- -[SMDProgress_XPCClientConnection verifyAndCreateIAUserWithPassword:andReplyBlock:]
- -[SMMigrateEngine .cxx_destruct]
- -[SMMigrateEngine absoluteParentProgress]
- -[SMMigrateEngine acceptNewMigrationRequest:]
- -[SMMigrateEngine acknowledgeCompletedRequest]
- -[SMMigrateEngine addDelegate:]
- -[SMMigrateEngine addElement:]
- -[SMMigrateEngine addRootUserToUsersToTransferInMigrationRequest]
- -[SMMigrateEngine aggregateEngineErrorsAndWarnings]
- -[SMMigrateEngine awaitSystemAvailability]
- -[SMMigrateEngine completedFilesWereShoved]
- -[SMMigrateEngine copyCompletedForPath:]
- -[SMMigrateEngine copyWasCompletedForPath:]
- -[SMMigrateEngine dealloc]
- -[SMMigrateEngine delegate]
- -[SMMigrateEngine deletedBytes]
- -[SMMigrateEngine description]
- -[SMMigrateEngine doneWithCurrentRequest]
- -[SMMigrateEngine elementsShouldContinue]
- -[SMMigrateEngine engineElements]
- -[SMMigrateEngine enginePhase]
- -[SMMigrateEngine enginePropertiesQueue]
- -[SMMigrateEngine engineQueue]
- -[SMMigrateEngine engineShouldContinue]
- -[SMMigrateEngine engineSourceSystemAvailable]
- -[SMMigrateEngine engineStepsForCurrentMigration]
- -[SMMigrateEngine engineSteps]
- -[SMMigrateEngine engineWaitingForPathing]
- -[SMMigrateEngine ensureSourceIsMounted]
- -[SMMigrateEngine errorWithMessage:]
- -[SMMigrateEngine errorWithMessage:underlyingError:]
- -[SMMigrateEngine error]
- -[SMMigrateEngine estimatedTimeRemaining]
- -[SMMigrateEngine estimatedTimeToComplete]
- -[SMMigrateEngine estimatedTotalTime]
- -[SMMigrateEngine extraTimeRemaining]
- -[SMMigrateEngine fdeNeedsToBeReeanbled]
- -[SMMigrateEngine finalSizeAndCountForMigrationRequest:]
- -[SMMigrateEngine finally]
- -[SMMigrateEngine finishedBytes]
- -[SMMigrateEngine gatherCompletionMessageTracerData]
- -[SMMigrateEngine generateEngineElements]
- -[SMMigrateEngine generateEngineSteps]
- -[SMMigrateEngine getCurrentSystemFromScanner]
- -[SMMigrateEngine init]
- -[SMMigrateEngine isEngineState:]
- -[SMMigrateEngine lastProgressLog]
- -[SMMigrateEngine lastProgressPercentComplete]
- -[SMMigrateEngine lastProgressUpdate]
- -[SMMigrateEngine lastReportedTimeRemaining]
- -[SMMigrateEngine lastReportedTransferRate]
- -[SMMigrateEngine lastTimeRemainingUpdate]
- -[SMMigrateEngine messageTraceCancellation]
- -[SMMigrateEngine messageTraceStateCompletion]
- -[SMMigrateEngine migrateProgressKey:arguments:forMigrateStep:]
- -[SMMigrateEngine migrateProgressString:forMigrateStep:]
- -[SMMigrateEngine migrationElementsProgressPercentage]
- -[SMMigrateEngine migrationRequest]
- -[SMMigrateEngine notEnoughFreeSpaceOnTargetError]
- -[SMMigrateEngine observeValueForKeyPath:ofObject:change:context:]
- -[SMMigrateEngine oneMinuteRemainingTime]
- -[SMMigrateEngine pathingProgressFormatKey:arguments:]
- -[SMMigrateEngine pathingStartTime]
- -[SMMigrateEngine pathsInSandbox]
- -[SMMigrateEngine predetermineTranslatedUIDs]
- -[SMMigrateEngine prepare]
- -[SMMigrateEngine prettyPrintEngineSteps]
- -[SMMigrateEngine processAnalyticsData]
- -[SMMigrateEngine processErrors]
- -[SMMigrateEngine process]
- -[SMMigrateEngine progressUpdateLock]
- -[SMMigrateEngine recordedOneMinuteRemainingTime]
- -[SMMigrateEngine removeDelegate:]
- -[SMMigrateEngine reportProgress]
- -[SMMigrateEngine reportTimeRemaining]
- -[SMMigrateEngine requestedDaemonScannerState]
- -[SMMigrateEngine runEngine]
- -[SMMigrateEngine runStepPrepare]
- -[SMMigrateEngine run]
- -[SMMigrateEngine saveFinalMigrationDetailsToTheRequestBeforeWeReboot]
- -[SMMigrateEngine setAbsoluteParentProgress:]
- -[SMMigrateEngine setDelegate:]
- -[SMMigrateEngine setDeletedBytes:]
- -[SMMigrateEngine setEngineElements:]
- -[SMMigrateEngine setEnginePhase:]
- -[SMMigrateEngine setEnginePropertiesQueue:]
- -[SMMigrateEngine setEngineQueue:]
- -[SMMigrateEngine setEngineSteps:]
- -[SMMigrateEngine setEngineStepsForCurrentMigration:]
- -[SMMigrateEngine setEngineWaitingForPathing:]
- -[SMMigrateEngine setError:]
- -[SMMigrateEngine setEstimatedTotalTime:]
- -[SMMigrateEngine setExtraTimeRemaining:]
- -[SMMigrateEngine setFinishedBytes:]
- -[SMMigrateEngine setLastProgressLog:]
- -[SMMigrateEngine setLastProgressPercentComplete:]
- -[SMMigrateEngine setLastProgressUpdate:]
- -[SMMigrateEngine setLastReportedTimeRemaining:]
- -[SMMigrateEngine setLastReportedTransferRate:]
- -[SMMigrateEngine setLastTimeRemainingUpdate:]
- -[SMMigrateEngine setMigrationElementsProgressPercentage:]
- -[SMMigrateEngine setMigrationRequest:]
- -[SMMigrateEngine setOneMinuteRemainingTime:]
- -[SMMigrateEngine setPathingStartTime:]
- -[SMMigrateEngine setPathsInSandbox:]
- -[SMMigrateEngine setProgressUpdateLock:]
- -[SMMigrateEngine setRecordedOneMinuteRemainingTime:]
- -[SMMigrateEngine setReportTimeRemaining:]
- -[SMMigrateEngine setRequestedDaemonScannerState:]
- -[SMMigrateEngine setStartTime:]
- -[SMMigrateEngine setState:]
- -[SMMigrateEngine setTimeDelayedByPathing:]
- -[SMMigrateEngine setTotalBytes:]
- -[SMMigrateEngine setTracingUUID:]
- -[SMMigrateEngine setupMessageTracing]
- -[SMMigrateEngine shoveCompletedSuccessfully]
- -[SMMigrateEngine shoveFailed]
- -[SMMigrateEngine smoothTimeRemaining:]
- -[SMMigrateEngine spaceIsSufficient]
- -[SMMigrateEngine startTime]
- -[SMMigrateEngine startupNewRequest]
- -[SMMigrateEngine state]
- -[SMMigrateEngine stepError:exception:phase:]
- -[SMMigrateEngine stopAllSteps]
- -[SMMigrateEngine stopOrSuspend:]
- -[SMMigrateEngine stop]
- -[SMMigrateEngine suspend]
- -[SMMigrateEngine systemScannerAddedSystem:]
- -[SMMigrateEngine systemScannerRemovedSystem:]
- -[SMMigrateEngine systemScannerSystemChanged:onSystem:]
- -[SMMigrateEngine systemsAreAvailable]
- -[SMMigrateEngine timeDelayedByPathing]
- -[SMMigrateEngine timeRemainingChangedForStep:]
- -[SMMigrateEngine totalBytes]
- -[SMMigrateEngine tracingUUID]
- -[SMMigrateEngine transferRateChanged:forStep:]
- -[SMMigrateEngine updateEngineForEngineSteps]
- -[SMMigrateEngine updateTimeRemaining]
- -[SMMigrateEngine updateTransferRate:]
- -[SMMigrateEngine updateUsersToTransferInMigrationRequest]
- -[SMMigrateEngine useSandbox]
- -[SMMigrateEngine userCanceledError]
- -[SMMigrateEngine waitIfSuspended:sourceDisappeared:]
- -[SMMigrateFiles .cxx_destruct]
- -[SMMigrateFiles _runCopier]
- -[SMMigrateFiles cancel]
- -[SMMigrateFiles copierFailed:error:]
- -[SMMigrateFiles copyEngineShouldContinueByFastChecking:]
- -[SMMigrateFiles copyPaths]
- -[SMMigrateFiles dedupeWallpaper]
- -[SMMigrateFiles description]
- -[SMMigrateFiles engineStepSupportsResumption]
- -[SMMigrateFiles estimatedTimeRemainingChanged:]
- -[SMMigrateFiles estimatedTimeRemainingForPhase:]
- -[SMMigrateFiles estimatedTimeToCompletePhase:]
- -[SMMigrateFiles fileCopyEngine]
- -[SMMigrateFiles kextCacheNeedsUpdate]
- -[SMMigrateFiles localizeFoldersForApplications]
- -[SMMigrateFiles observeValueForKeyPath:ofObject:change:context:]
- -[SMMigrateFiles postProcess]
- -[SMMigrateFiles prelimFileCount]
- -[SMMigrateFiles preliminarySize:andCount:forPathGroup:]
- -[SMMigrateFiles prepare]
- -[SMMigrateFiles process]
- -[SMMigrateFiles resumeProcess]
- -[SMMigrateFiles setEngine:]
- -[SMMigrateFiles setFileCopyEngine:]
- -[SMMigrateFiles setKextCacheNeedsUpdate:]
- -[SMMigrateFiles setPrelimFileCount:]
- -[SMMigrateFiles setupCopiesForFileGroups]
- -[SMMigrateFiles setupCopyNonSystemReceiptsForUpgrade]
- -[SMMigrateFiles setupFileCopyEngine]
- -[SMMigrateFiles transferRateChanged:]
- -[SMMigrateGroups createGroup:inDB:]
- -[SMMigrateGroups createGroupsInDB:]
- -[SMMigrateGroups deleteGroup:inDB:]
- -[SMMigrateGroups estimatedTimeToCompletePhase:]
- -[SMMigrateGroups migrateGroups]
- -[SMMigrateGroups postProcess]
- -[SMMigrateGuestAccountStep estimatedTimeToCompletePhase:]
- -[SMMigrateSystemInfo .cxx_destruct]
- -[SMMigrateSystemInfo allRuleGroups]
- -[SMMigrateSystemInfo confMigrator]
- -[SMMigrateSystemInfo copierFailed:error:]
- -[SMMigrateSystemInfo copyEngineShouldContinueByFastChecking:]
- -[SMMigrateSystemInfo copyIgnorePremissionsSettings]
- -[SMMigrateSystemInfo copyMachineSettings]
- -[SMMigrateSystemInfo copyNetworkSettings]
- -[SMMigrateSystemInfo copyPaths]
- -[SMMigrateSystemInfo copyRemoteManagementSettings]
- -[SMMigrateSystemInfo copySystemSettings]
- -[SMMigrateSystemInfo copyTimeZone]
- -[SMMigrateSystemInfo copyVirtualMemorySettings]
- -[SMMigrateSystemInfo deferCopyPath:sourceSystem:targetSystme:]
- -[SMMigrateSystemInfo description]
- -[SMMigrateSystemInfo estimatedTimeRemainingChanged:]
- -[SMMigrateSystemInfo estimatedTimeRemainingForPhase:]
- -[SMMigrateSystemInfo estimatedTimeToCompletePhase:]
- -[SMMigrateSystemInfo fileCopyEngine]
- -[SMMigrateSystemInfo finishKerberosSetup]
- -[SMMigrateSystemInfo getLastModifiedDate:]
- -[SMMigrateSystemInfo init]
- -[SMMigrateSystemInfo isHostconfigServiceEnabledOnSourceSystem:]
- -[SMMigrateSystemInfo migrateDirectoryServicesDatabase]
- -[SMMigrateSystemInfo migrateGlobalPreferences]
- -[SMMigrateSystemInfo migrateLockdownModeSetting]
- -[SMMigrateSystemInfo migrateNetworkSettings]
- -[SMMigrateSystemInfo onlyUpdateSystemSettings]
- -[SMMigrateSystemInfo postProcess]
- -[SMMigrateSystemInfo preProcess]
- -[SMMigrateSystemInfo prepareForServerMigration]
- -[SMMigrateSystemInfo prepare]
- -[SMMigrateSystemInfo process]
- -[SMMigrateSystemInfo repairDatavaultPermissions]
- -[SMMigrateSystemInfo repairTimezonePermissions]
- -[SMMigrateSystemInfo runOpenDirectoryMigrationTool]
- -[SMMigrateSystemInfo setAllRuleGroups:]
- -[SMMigrateSystemInfo setConfMigrator:]
- -[SMMigrateSystemInfo setEngine:]
- -[SMMigrateSystemInfo setFileCopyEngine:]
- -[SMMigrateSystemInfo setOnlyUpdateSystemSettings:]
- -[SMMigrateSystemInfo setSettingsCopiers:]
- -[SMMigrateSystemInfo settingsCopiers]
- -[SMMigrateSystemInfo setupFileCopyEngine]
- -[SMMigrateSystemInfo setupKerberos]
- -[SMMigrateSystemInfo transferRateChanged:]
- -[SMMigrateUserAccountsStep estimatedTimeToCompletePhase:]
- -[SMMigrateUserAccountsStep setEngine:]
- -[SMMigrateUserDataStep .cxx_destruct]
- -[SMMigrateUserDataStep applyUserTemplateForCopier:]
- -[SMMigrateUserDataStep cancel]
- -[SMMigrateUserDataStep copierFailed:error:]
- -[SMMigrateUserDataStep copierSuceeded:]
- -[SMMigrateUserDataStep copiesHomeDirectories]
- -[SMMigrateUserDataStep copyEngineShouldContinueByFastChecking:]
- -[SMMigrateUserDataStep copyPaths]
- -[SMMigrateUserDataStep createComprehensiveCopierForUser:relativeTargetHome:]
- -[SMMigrateUserDataStep createCopierForUser:relativeTargetHome:]
- -[SMMigrateUserDataStep createHomeDirectoryCopiersForUsers]
- -[SMMigrateUserDataStep deletedUsersHomeDirectories]
- -[SMMigrateUserDataStep description]
- -[SMMigrateUserDataStep engineStepSupportsResumption]
- -[SMMigrateUserDataStep estimatedTimeRemainingChanged:]
- -[SMMigrateUserDataStep estimatedTimeRemainingForPhase:]
- -[SMMigrateUserDataStep estimatedTimeToCompletePhase:]
- -[SMMigrateUserDataStep fileCopyEngine]
- -[SMMigrateUserDataStep observeValueForKeyPath:ofObject:change:context:]
- -[SMMigrateUserDataStep postProcess]
- -[SMMigrateUserDataStep prepare]
- -[SMMigrateUserDataStep processError]
- -[SMMigrateUserDataStep process]
- -[SMMigrateUserDataStep relativeDestinationUserHomeForUser:]
- -[SMMigrateUserDataStep relativeDestinationUserHomeForUserDict:]
- -[SMMigrateUserDataStep resumeProcess]
- -[SMMigrateUserDataStep runCopier]
- -[SMMigrateUserDataStep setEngine:]
- -[SMMigrateUserDataStep setFileCopyEngine:]
- -[SMMigrateUserDataStep setProcessError:]
- -[SMMigrateUserDataStep setUsersToReplace:]
- -[SMMigrateUserDataStep setupFileCopyEngine]
- -[SMMigrateUserDataStep setupUsersToReplace]
- -[SMMigrateUserDataStep transferRateChanged:]
- -[SMMigrateUserDataStep usersToReplace]
- -[SMMigrationActivity .cxx_destruct]
- -[SMMigrationActivity activityLength]
- -[SMMigrationActivity addChildActivity:]
- -[SMMigrationActivity childActivitiesQueue]
- -[SMMigrationActivity childActivities]
- -[SMMigrationActivity description]
- -[SMMigrationActivity detail]
- -[SMMigrationActivity endDate]
- -[SMMigrationActivity estimatedDuration]
- -[SMMigrationActivity finish]
- -[SMMigrationActivity hasFinished]
- -[SMMigrationActivity hasStarted]
- -[SMMigrationActivity initWithName:]
- -[SMMigrationActivity initWithName:detail:]
- -[SMMigrationActivity init]
- -[SMMigrationActivity name]
- -[SMMigrationActivity setChildActivities:]
- -[SMMigrationActivity setChildActivitiesQueue:]
- -[SMMigrationActivity setDetail:]
- -[SMMigrationActivity setEndDate:]
- -[SMMigrationActivity setEstimatedDuration:]
- -[SMMigrationActivity setName:]
- -[SMMigrationActivity setSize:]
- -[SMMigrationActivity setStartDate:]
- -[SMMigrationActivity size]
- -[SMMigrationActivity startDate]
- -[SMMigrationActivity start]
- -[SMMigrationEngineElement .cxx_destruct]
- -[SMMigrationEngineElement calculateProgressPercentages:]
- -[SMMigrationEngineElement completedSize]
- -[SMMigrationEngineElement description]
- -[SMMigrationEngineElement elementSupportsResuming]
- -[SMMigrationEngineElement engine]
- -[SMMigrationEngineElement estimateTimeRemaining]
- -[SMMigrationEngineElement estimatedTimeToComplete]
- -[SMMigrationEngineElement hasRan]
- -[SMMigrationEngineElement initWithEngine:]
- -[SMMigrationEngineElement initialTimeEstimate]
- -[SMMigrationEngineElement parentProgress]
- -[SMMigrationEngineElement progressPercentage]
- -[SMMigrationEngineElement progress]
- -[SMMigrationEngineElement resume]
- -[SMMigrationEngineElement run]
- -[SMMigrationEngineElement setEngine:]
- -[SMMigrationEngineElement setHasRan:]
- -[SMMigrationEngineElement setInitialTimeEstimate:]
- -[SMMigrationEngineElement setParentProgress:]
- -[SMMigrationEngineElement setProgress:]
- -[SMMigrationEngineElement setProgressPercentage:]
- -[SMMigrationEngineElement shouldContinue]
- -[SMMigrationEngineStep .cxx_destruct]
- -[SMMigrationEngineStep addProgress:forKey:]
- -[SMMigrationEngineStep cancel]
- -[SMMigrationEngineStep completedFileCount]
- -[SMMigrationEngineStep completedSize]
- -[SMMigrationEngineStep copyFailedToCopyFile:shouldReportError:]
- -[SMMigrationEngineStep copyPaths]
- -[SMMigrationEngineStep deletedSize]
- -[SMMigrationEngineStep engineStepSupportsResumption]
- -[SMMigrationEngineStep engine]
- -[SMMigrationEngineStep errorWithMessage:code:]
- -[SMMigrationEngineStep errorWithMessage:code:underlyingError:]
- -[SMMigrationEngineStep errors]
- -[SMMigrationEngineStep estimateTimeRemaining]
- -[SMMigrationEngineStep estimatedTimeRemainingAfterPhase:]
- -[SMMigrationEngineStep estimatedTimeRemainingForPhase:]
- -[SMMigrationEngineStep estimatedTimeToCompletePhase:]
- -[SMMigrationEngineStep estimatedTimeToComplete]
- -[SMMigrationEngineStep fatalErrorWithMessage:]
- -[SMMigrationEngineStep fatalErrorWithMessage:underlyingError:]
- -[SMMigrationEngineStep hasProgressForKey:]
- -[SMMigrationEngineStep init]
- -[SMMigrationEngineStep lastCompletedPhase]
- -[SMMigrationEngineStep parentProgress]
- -[SMMigrationEngineStep postProcess]
- -[SMMigrationEngineStep preProcess]
- -[SMMigrationEngineStep preShove]
- -[SMMigrationEngineStep prepare]
- -[SMMigrationEngineStep process]
- -[SMMigrationEngineStep progressArrayForKey:]
- -[SMMigrationEngineStep progressCompletedForKey:]
- -[SMMigrationEngineStep progressDictionaryForKey:]
- -[SMMigrationEngineStep progressForKey:]
- -[SMMigrationEngineStep progressPercentageForPhase:]
- -[SMMigrationEngineStep progressPercentages]
- -[SMMigrationEngineStep progress]
- -[SMMigrationEngineStep resumeProcess]
- -[SMMigrationEngineStep setCompletedFileCount:]
- -[SMMigrationEngineStep setCompletedSize:]
- -[SMMigrationEngineStep setDeletedSize:]
- -[SMMigrationEngineStep setEngine:]
- -[SMMigrationEngineStep setErrors:]
- -[SMMigrationEngineStep setLastCompletedPhase:]
- -[SMMigrationEngineStep setParentProgress:]
- -[SMMigrationEngineStep setProgress:]
- -[SMMigrationEngineStep setProgress:forKey:]
- -[SMMigrationEngineStep setProgressPercentage:forPhase:]
- -[SMMigrationEngineStep setProgressPercentages:]
- -[SMMigrationEngineStep setTotalFileCount:]
- -[SMMigrationEngineStep setTotalSize:]
- -[SMMigrationEngineStep setWarnings:]
- -[SMMigrationEngineStep totalFileCount]
- -[SMMigrationEngineStep totalSize]
- -[SMMigrationEngineStep warningWithMessage:]
- -[SMMigrationEngineStep warningWithMessage:underlyingError:]
- -[SMMigrationEngineStep warnings]
- -[SMMigrationEngineStep(Sorting) compare:]
- -[SMMigrationEngineStep(Sorting) sortOrder]
- -[SMMigrationIncompatibleApplicationsList .cxx_destruct]
- -[SMMigrationIncompatibleApplicationsList isPathInIncompatibleApplicationsList:]
- -[SMMigrationIncompatibleApplicationsList loadPlist:]
- -[SMMigrationIncompatibleApplicationsList prepareIncompatibleApplicationsList:forSMSystem:]
- -[SMMigrationKernelManagementUtilityElement estimateTimeRemaining]
- -[SMMigrationKernelManagementUtilityElement estimatedTimeToComplete]
- -[SMMigrationKernelManagementUtilityElement run]
- -[SMMigrationReport .cxx_destruct]
- -[SMMigrationReport activities]
- -[SMMigrationReport activityQueue]
- -[SMMigrationReport addActivity:]
- -[SMMigrationReport description]
- -[SMMigrationReport init]
- -[SMMigrationReport lastProgressEntry]
- -[SMMigrationReport migrationRequest]
- -[SMMigrationReport note:]
- -[SMMigrationReport noteQueue]
- -[SMMigrationReport notes]
- -[SMMigrationReport progressEntries]
- -[SMMigrationReport progressQueue]
- -[SMMigrationReport progressTimer]
- -[SMMigrationReport recordProgressPercentComplete:timeRemaining:transferRate:]
- -[SMMigrationReport saveProgressReport:]
- -[SMMigrationReport setActivities:]
- -[SMMigrationReport setActivityQueue:]
- -[SMMigrationReport setLastProgressEntry:]
- -[SMMigrationReport setMigrationRequest:]
- -[SMMigrationReport setNoteQueue:]
- -[SMMigrationReport setNotes:]
- -[SMMigrationReport setProgressEntries:]
- -[SMMigrationReport setProgressQueue:]
- -[SMMigrationReport setProgressTimer:]
- -[SMMigrationShoveElement .cxx_destruct]
- -[SMMigrationShoveElement delegate]
- -[SMMigrationShoveElement estimatedTimeToComplete]
- -[SMMigrationShoveElement run]
- -[SMMigrationShoveElement setDelegate:]
- -[SMMigrationStepElement .cxx_destruct]
- -[SMMigrationStepElement calculateProgressPercentages:]
- -[SMMigrationStepElement completedSize]
- -[SMMigrationStepElement description]
- -[SMMigrationStepElement elementSupportsResuming]
- -[SMMigrationStepElement errorWithMessage:]
- -[SMMigrationStepElement estimateTimeRemaining]
- -[SMMigrationStepElement estimatedTimeToComplete]
- -[SMMigrationStepElement initWithEngine:steps:phase:]
- -[SMMigrationStepElement phaseNameForPhase:]
- -[SMMigrationStepElement phase]
- -[SMMigrationStepElement run]
- -[SMMigrationStepElement setPhase:]
- -[SMMigrationStepElement setProgressPortionsForStep:]
- -[SMMigrationStepElement setStepFinishedBytes:]
- -[SMMigrationStepElement setSteps:]
- -[SMMigrationStepElement stepErrorWithException:]
- -[SMMigrationStepElement stepFinishedBytes]
- -[SMMigrationStepElement steps]
- -[SMMigrationUpdateKextCacheElement estimatedTimeToComplete]
- -[SMMigrationUpdateKextCacheElement run]
- -[SMPaths setSystemRuleHandler:]
- -[SMPaths systemRuleHandler]
- -[SMPathsDirectoryClassifier addBundle:atLocation:withStats:]
- -[SMProgressEntry .cxx_destruct]
- -[SMProgressEntry date]
- -[SMProgressEntry percentComplete]
- -[SMProgressEntry setDate:]
- -[SMProgressEntry setPercentComplete:]
- -[SMProgressEntry setTimeRemaining:]
- -[SMProgressEntry setTransferRate:]
- -[SMProgressEntry timeRemaining]
- -[SMProgressEntry transferRate]
- -[SMProgress_Client verifyAndCreateIAUserWithPassword:]
- -[SMReportNote .cxx_destruct]
- -[SMReportNote count]
- -[SMReportNote datesSeen]
- -[SMReportNote description]
- -[SMReportNote increment]
- -[SMReportNote initWithMessage:]
- -[SMReportNote note]
- -[SMReportNote setCount:]
- -[SMReportNote setDatesSeen:]
- -[SMSystemRule initWithAllowlistPath:]
- -[SMSystemRuleClient dealloc]
- -[SMSystemRuleClient dictionaryFromStatement:]
- -[SMSystemRuleClient executeQuery:]
- -[SMSystemRuleClient getAllRules]
- -[SMSystemRuleClient getArgumentsByRuleIDSortByArgumentOrder:]
- -[SMSystemRuleClient getChecksumsByFilePath:]
- -[SMSystemRuleClient getRuleByID:]
- -[SMSystemRuleClient getRulesByRuleGroup:]
- -[SMSystemRuleClient openDatabase]
- -[SMSystemRuleClient valueForColumnAtIndex:statement:type:]
- -[SMSystemRuleHandler .cxx_destruct]
- -[SMSystemRuleHandler _destination]
- -[SMSystemRuleHandler _migrationRequestType]
- -[SMSystemRuleHandler _source]
- -[SMSystemRuleHandler clearFirmlinkPathContents:]
- -[SMSystemRuleHandler copyFirmlinkContents:newPath:]
- -[SMSystemRuleHandler generateDestinationPath:]
- -[SMSystemRuleHandler initWithSource:destination:]
- -[SMSystemRuleHandler isApplicableInCurrentBootStage:]
- -[SMSystemRuleHandler isApplicableRuleContext:]
- -[SMSystemRuleHandler isCopyRuleApplicable:]
- -[SMSystemRuleHandler isCopyableBecauseDestinationDoesNotExist:]
- -[SMSystemRuleHandler isPathFirmlink:]
- -[SMSystemRuleHandler isRuleApplicable:]
- -[SMSystemRuleHandler isSkipLegacyRuleInLegacy:]
- -[SMSystemRuleHandler isSourceLessThanMaximumVersionAllowed:]
- -[SMSystemRuleHandler isSourceMoreThanMinimumVersionAllowed:]
- -[SMSystemRuleHandler isSourcePathAppleShippedDefault:]
- -[SMSystemRuleHandler isSourcePathPresentInSource:]
- -[SMSystemRuleHandler longTermDestinationSystemIdentifier]
- -[SMSystemRuleHandler longTermSourceSystemIdentifier]
- -[SMSystemRuleHandler setLongTermDestinationSystemIdentifier:]
- -[SMSystemRuleHandler setLongTermSourceSystemIdentifier:]
- -[SMSystemRuleHandler sourceVersion]
- -[SMSystem_Daemon generateAppsFileStep:]
- -[SMSystem_Daemon generateAutoLoginUserStep:]
- -[SMSystem_Daemon generateMachineSettingsStep:shouldSetOnlyUpdateSystemSettings:]
- -[SMSystem_Daemon generateMigrateGuestAccountStep:]
- -[SMSystem_Daemon generatePeerToPeerStep:]
- -[SMSystem_Daemon generateStepsForEngine:withRequestType:mustGenerateUserStep:mustGenerateEnterpriseFilesStep:mustGenerateMachineSettingsStep:mustGenerateGuestStep:mustGenerateAppsFileStep:]
- -[SMSystem_Daemon generateUsersStep:]
- -[SMSystem_Daemon_Windows generateEnterpriseMigrateFilesStep:]
- -[SMSystem_Daemon_Windows generateMachineSettingsStep:withMacPathMap:]
- -[SMSystem_Daemon_Windows generateStepsForEngine:withRequestType:mustGenerateUserStep:mustGenerateEnterpriseFilesStep:mustGenerateMachineSettingsStep:mustGenerateGuestStep:mustGenerateAppsFileStep:]
- -[SMSystem_Daemon_Windows generateUsersStep:withMacPathMap:]
- -[SMWindowsImportUserDataStep estimatedTimeToCompletePhase:]
- -[SMWindowsImportUserDataStep initWithPathMap:]
- -[SMWindowsMigrateComponentStep estimatedTimeRemainingChanged:]
- -[SMWindowsMigrateComponentStep estimatedTimeRemainingForPhase:]
- -[SMWindowsMigrateComponentStep estimatedTimeToCompletePhase:]
- -[SMWindowsMigrateComponentStep initWithPathMap:]
- -[SMWindowsMigrateComponentStep observeValueForKeyPath:ofObject:change:context:]
- -[SMWindowsMigrateComponentStep transferRateChanged:]
- -[SMWindowsMigrateFilesStep estimatedTimeRemainingChanged:]
- -[SMWindowsMigrateFilesStep estimatedTimeRemainingForPhase:]
- -[SMWindowsMigrateFilesStep estimatedTimeToCompletePhase:]
- -[SMWindowsMigrateFilesStep observeValueForKeyPath:ofObject:change:context:]
- -[SMWindowsMigrateFilesStep setEngine:]
- -[SMWindowsMigrateFilesStep transferRateChanged:]
- -[SMWindowsMigrateUserAccountsStep estimatedTimeToCompletePhase:]
- -[SMWindowsMigrateUserAccountsStep initWithPathMap:]
- GCC_except_table108
- GCC_except_table21
- GCC_except_table223
- GCC_except_table28
- GCC_except_table33
- GCC_except_table35
- GCC_except_table65
- GCC_except_table66
- GCC_except_table69
- GCC_except_table73
- GCC_except_table88
- OBJC_IVAR_$_SMConfMigrator._parentProgress
- OBJC_IVAR_$_SMConfMigrator._parentProgressPendingUnits
- OBJC_IVAR_$_SMCopyEngine._parentProgress
- OBJC_IVAR_$_SMCopyEngine._parentProgressPendingUnits
- OBJC_IVAR_$_SMCopyEngine._progress
- OBJC_IVAR_$_SMCopyEngine._progressString
- OBJC_IVAR_$_SMCopyEngineCopier._parentProgress
- OBJC_IVAR_$_SMCopyEngineCopier._parentProgressPendingUnits
- OBJC_IVAR_$_SMCopyEngineCopier._progress
- OBJC_IVAR_$_SMCopyEngineCopier._progressString
- OBJC_IVAR_$_SMMigrateEngine._absoluteParentProgress
- OBJC_IVAR_$_SMMigrateEngine._delegate
- OBJC_IVAR_$_SMMigrateEngine._deletedBytes
- OBJC_IVAR_$_SMMigrateEngine._engineElements
- OBJC_IVAR_$_SMMigrateEngine._enginePhase
- OBJC_IVAR_$_SMMigrateEngine._enginePropertiesQueue
- OBJC_IVAR_$_SMMigrateEngine._engineQueue
- OBJC_IVAR_$_SMMigrateEngine._engineSteps
- OBJC_IVAR_$_SMMigrateEngine._engineStepsForCurrentMigration
- OBJC_IVAR_$_SMMigrateEngine._engineWaitingForPathing
- OBJC_IVAR_$_SMMigrateEngine._error
- OBJC_IVAR_$_SMMigrateEngine._estimatedTotalTime
- OBJC_IVAR_$_SMMigrateEngine._extraTimeRemaining
- OBJC_IVAR_$_SMMigrateEngine._finishedBytes
- OBJC_IVAR_$_SMMigrateEngine._lastProgressLog
- OBJC_IVAR_$_SMMigrateEngine._lastProgressPercentComplete
- OBJC_IVAR_$_SMMigrateEngine._lastProgressUpdate
- OBJC_IVAR_$_SMMigrateEngine._lastReportedTimeRemaining
- OBJC_IVAR_$_SMMigrateEngine._lastReportedTransferRate
- OBJC_IVAR_$_SMMigrateEngine._lastTimeRemainingUpdate
- OBJC_IVAR_$_SMMigrateEngine._migrationElementsProgressPercentage
- OBJC_IVAR_$_SMMigrateEngine._migrationRequest
- OBJC_IVAR_$_SMMigrateEngine._oneMinuteRemainingTime
- OBJC_IVAR_$_SMMigrateEngine._pathingStartTime
- OBJC_IVAR_$_SMMigrateEngine._pathsInSandbox
- OBJC_IVAR_$_SMMigrateEngine._progressUpdateLock
- OBJC_IVAR_$_SMMigrateEngine._recordedOneMinuteRemainingTime
- OBJC_IVAR_$_SMMigrateEngine._reportTimeRemaining
- OBJC_IVAR_$_SMMigrateEngine._requestedDaemonScannerState
- OBJC_IVAR_$_SMMigrateEngine._startTime
- OBJC_IVAR_$_SMMigrateEngine._state
- OBJC_IVAR_$_SMMigrateEngine._timeDelayedByPathing
- OBJC_IVAR_$_SMMigrateEngine._totalBytes
- OBJC_IVAR_$_SMMigrateEngine._tracingUUID
- OBJC_IVAR_$_SMMigrateFiles._fileCopyEngine
- OBJC_IVAR_$_SMMigrateFiles._kextCacheNeedsUpdate
- OBJC_IVAR_$_SMMigrateFiles._prelimFileCount
- OBJC_IVAR_$_SMMigrateSystemInfo._allRuleGroups
- OBJC_IVAR_$_SMMigrateSystemInfo._confMigrator
- OBJC_IVAR_$_SMMigrateSystemInfo._fileCopyEngine
- OBJC_IVAR_$_SMMigrateSystemInfo._onlyUpdateSystemSettings
- OBJC_IVAR_$_SMMigrateSystemInfo._settingsCopiers
- OBJC_IVAR_$_SMMigrateUserDataStep._fileCopyEngine
- OBJC_IVAR_$_SMMigrateUserDataStep._processError
- OBJC_IVAR_$_SMMigrateUserDataStep._usersToReplace
- OBJC_IVAR_$_SMMigrationActivity._childActivities
- OBJC_IVAR_$_SMMigrationActivity._childActivitiesQueue
- OBJC_IVAR_$_SMMigrationActivity._detail
- OBJC_IVAR_$_SMMigrationActivity._endDate
- OBJC_IVAR_$_SMMigrationActivity._estimatedDuration
- OBJC_IVAR_$_SMMigrationActivity._name
- OBJC_IVAR_$_SMMigrationActivity._size
- OBJC_IVAR_$_SMMigrationActivity._startDate
- OBJC_IVAR_$_SMMigrationEngineElement._engine
- OBJC_IVAR_$_SMMigrationEngineElement._hasRan
- OBJC_IVAR_$_SMMigrationEngineElement._initialTimeEstimate
- OBJC_IVAR_$_SMMigrationEngineElement._parentProgress
- OBJC_IVAR_$_SMMigrationEngineElement._progress
- OBJC_IVAR_$_SMMigrationEngineElement._progressPercentage
- OBJC_IVAR_$_SMMigrationEngineStep._completedFileCount
- OBJC_IVAR_$_SMMigrationEngineStep._completedSize
- OBJC_IVAR_$_SMMigrationEngineStep._deletedSize
- OBJC_IVAR_$_SMMigrationEngineStep._errors
- OBJC_IVAR_$_SMMigrationEngineStep._lastCompletedPhase
- OBJC_IVAR_$_SMMigrationEngineStep._parentProgress
- OBJC_IVAR_$_SMMigrationEngineStep._progress
- OBJC_IVAR_$_SMMigrationEngineStep._progressPercentages
- OBJC_IVAR_$_SMMigrationEngineStep._totalFileCount
- OBJC_IVAR_$_SMMigrationEngineStep._totalSize
- OBJC_IVAR_$_SMMigrationEngineStep._warnings
- OBJC_IVAR_$_SMMigrationEngineStep.engine
- OBJC_IVAR_$_SMMigrationIncompatibleApplicationsList.iaList
- OBJC_IVAR_$_SMMigrationIncompatibleApplicationsList.systemRootPath
- OBJC_IVAR_$_SMMigrationReport._activities
- OBJC_IVAR_$_SMMigrationReport._activityQueue
- OBJC_IVAR_$_SMMigrationReport._lastProgressEntry
- OBJC_IVAR_$_SMMigrationReport._migrationRequest
- OBJC_IVAR_$_SMMigrationReport._noteQueue
- OBJC_IVAR_$_SMMigrationReport._notes
- OBJC_IVAR_$_SMMigrationReport._progressEntries
- OBJC_IVAR_$_SMMigrationReport._progressQueue
- OBJC_IVAR_$_SMMigrationReport._progressTimer
- OBJC_IVAR_$_SMMigrationShoveElement._delegate
- OBJC_IVAR_$_SMMigrationStepElement._phase
- OBJC_IVAR_$_SMMigrationStepElement._stepFinishedBytes
- OBJC_IVAR_$_SMMigrationStepElement._steps
- OBJC_IVAR_$_SMPaths._systemRuleHandler
- OBJC_IVAR_$_SMProgressEntry._date
- OBJC_IVAR_$_SMProgressEntry._percentComplete
- OBJC_IVAR_$_SMProgressEntry._timeRemaining
- OBJC_IVAR_$_SMProgressEntry._transferRate
- OBJC_IVAR_$_SMReportNote.count
- OBJC_IVAR_$_SMReportNote.datesSeen
- OBJC_IVAR_$_SMReportNote.note
- OBJC_IVAR_$_SMSystemRuleHandler._longTermDestinationSystemIdentifier
- OBJC_IVAR_$_SMSystemRuleHandler._longTermSourceSystemIdentifier
- _CFBundleGetInfoDictionary
- _OBJC_CLASS_$_NSConstantDoubleNumber
- _OBJC_CLASS_$_NSProgress
- _OBJC_CLASS_$_SMCommitDeferredSandboxElement
- _OBJC_CLASS_$_SMConfMigratorAllowlist
- _OBJC_CLASS_$_SMConfMigratorBundle
- _OBJC_CLASS_$_SMConfMigratorCopyRule
- _OBJC_CLASS_$_SMConfMigratorRules
- _OBJC_CLASS_$_SMConfMigratorRunToolRule
- _OBJC_CLASS_$_SMConfMigratorUserPathRule
- _OBJC_CLASS_$_SMMigrateEngine
- _OBJC_CLASS_$_SMMigrateFiles
- _OBJC_CLASS_$_SMMigrateGroups
- _OBJC_CLASS_$_SMMigrateSystemInfo
- _OBJC_CLASS_$_SMMigrateUserDataStep
- _OBJC_CLASS_$_SMMigrationActivity
- _OBJC_CLASS_$_SMMigrationEngineElement
- _OBJC_CLASS_$_SMMigrationEngineStep
- _OBJC_CLASS_$_SMMigrationIncompatibleApplicationsList
- _OBJC_CLASS_$_SMMigrationKernelManagementUtilityElement
- _OBJC_CLASS_$_SMMigrationReport
- _OBJC_CLASS_$_SMMigrationShoveElement
- _OBJC_CLASS_$_SMMigrationStepElement
- _OBJC_CLASS_$_SMMigrationUpdateKextCacheElement
- _OBJC_CLASS_$_SMProgressEntry
- _OBJC_CLASS_$_SMReportNote
- _OBJC_CLASS_$_SMSystemRuleClient
- _OBJC_CLASS_$_SMSystemRuleHandler
- _OBJC_METACLASS_$_SMCommitDeferredSandboxElement
- _OBJC_METACLASS_$_SMConfMigratorAllowlist
- _OBJC_METACLASS_$_SMConfMigratorBundle
- _OBJC_METACLASS_$_SMConfMigratorCopyRule
- _OBJC_METACLASS_$_SMConfMigratorRules
- _OBJC_METACLASS_$_SMConfMigratorRunToolRule
- _OBJC_METACLASS_$_SMConfMigratorUserPathRule
- _OBJC_METACLASS_$_SMMigrateEngine
- _OBJC_METACLASS_$_SMMigrateFiles
- _OBJC_METACLASS_$_SMMigrateGroups
- _OBJC_METACLASS_$_SMMigrateSystemInfo
- _OBJC_METACLASS_$_SMMigrateUserDataStep
- _OBJC_METACLASS_$_SMMigrationActivity
- _OBJC_METACLASS_$_SMMigrationEngineElement
- _OBJC_METACLASS_$_SMMigrationEngineStep
- _OBJC_METACLASS_$_SMMigrationIncompatibleApplicationsList
- _OBJC_METACLASS_$_SMMigrationKernelManagementUtilityElement
- _OBJC_METACLASS_$_SMMigrationReport
- _OBJC_METACLASS_$_SMMigrationShoveElement
- _OBJC_METACLASS_$_SMMigrationStepElement
- _OBJC_METACLASS_$_SMMigrationUpdateKextCacheElement
- _OBJC_METACLASS_$_SMProgressEntry
- _OBJC_METACLASS_$_SMReportNote
- _OBJC_METACLASS_$_SMSystemRuleClient
- _OBJC_METACLASS_$_SMSystemRuleHandler
- _SMMigrateEngineErrorDomain
- __113-[MigrationHelper_Client encryptDiskWithiCloudUser:iCloudPassword:localUser:localPassword:andBag:returningError:]_block_invoke.47
- __19-[SMCopyEngine run]_block_invoke.53
- __19-[SMCopyEngine run]_block_invoke.74
- __19-[SMCopyEngine run]_block_invoke.78
- __26-[SMMigrateEngine process]_block_invoke.341
- __26-[SMMigrateEngine process]_block_invoke.369
- __27-[SMPaths loadAllFakelinks]_block_invoke.308
- __28-[SMMigrateEngine setState:]_block_invoke.57
- __29-[SMMigrateFiles postProcess]_block_invoke.44
- __29-[SMMigrateFiles postProcess]_block_invoke.50
- __29-[SMMigrationStepElement run]_block_invoke.61
- __29-[SMMigrationStepElement run]_block_invoke.68
- __29-[SMMigrationStepElement run]_block_invoke.72
- __30-[SMPaths enumerateFilesystem]_block_invoke.389
- __32-[SMMigrationReport description]_block_invoke.34
- __34-[SMMigrateSystemInfo postProcess]_block_invoke.51
- __34-[SMMigrateSystemInfo postProcess]_block_invoke.57
- __38-[SMMigrateEngine systemsAreAvailable]_block_invoke.168
- __42-[SMCopyEngineCopier sizeCompletedUpdate:]_block_invoke.82
- __42-[SMMigrateSystemInfo copyMachineSettings]_block_invoke.121
- __45-[SMMigrateEngine acceptNewMigrationRequest:]_block_invoke.204
- __46-[SMMigrateEngine systemScannerRemovedSystem:]_block_invoke.117
- __67-[MigrationHelper_Client doImportWithParameters:desktopPictureURL:]_block_invoke.45
- __71+[SMSandboxTools shoveSandboxAtPath:sandBoxPath:destinationPath:error:]_block_invoke.77
- __OBJC_$_CLASS_METHODS_SMConfMigratorAllowlist
- __OBJC_$_CLASS_METHODS_SMConfMigratorBundle
- __OBJC_$_CLASS_METHODS_SMConfMigratorRules
- __OBJC_$_CLASS_METHODS_SMMigrateFiles
- __OBJC_$_CLASS_METHODS_SMMigrateUserDataStep
- __OBJC_$_CLASS_METHODS_SMMigrationEngineStep
- __OBJC_$_CLASS_METHODS_SMMigrationReport
- __OBJC_$_CLASS_METHODS_SMSystemRuleClient
- __OBJC_$_INSTANCE_METHODS_SMCommitDeferredSandboxElement
- __OBJC_$_INSTANCE_METHODS_SMConfMigratorCopyRule
- __OBJC_$_INSTANCE_METHODS_SMConfMigratorRunToolRule
- __OBJC_$_INSTANCE_METHODS_SMConfMigratorUserPathRule
- __OBJC_$_INSTANCE_METHODS_SMMigrateEngine
- __OBJC_$_INSTANCE_METHODS_SMMigrateFiles
- __OBJC_$_INSTANCE_METHODS_SMMigrateGroups
- __OBJC_$_INSTANCE_METHODS_SMMigrateSystemInfo
- __OBJC_$_INSTANCE_METHODS_SMMigrateUserDataStep
- __OBJC_$_INSTANCE_METHODS_SMMigrationActivity
- __OBJC_$_INSTANCE_METHODS_SMMigrationEngineElement
- __OBJC_$_INSTANCE_METHODS_SMMigrationEngineStep(Sorting)
- __OBJC_$_INSTANCE_METHODS_SMMigrationIncompatibleApplicationsList
- __OBJC_$_INSTANCE_METHODS_SMMigrationKernelManagementUtilityElement
- __OBJC_$_INSTANCE_METHODS_SMMigrationReport
- __OBJC_$_INSTANCE_METHODS_SMMigrationShoveElement
- __OBJC_$_INSTANCE_METHODS_SMMigrationStepElement
- __OBJC_$_INSTANCE_METHODS_SMMigrationUpdateKextCacheElement
- __OBJC_$_INSTANCE_METHODS_SMProgressEntry
- __OBJC_$_INSTANCE_METHODS_SMReportNote
- __OBJC_$_INSTANCE_METHODS_SMSystemRuleClient
- __OBJC_$_INSTANCE_METHODS_SMSystemRuleHandler
- __OBJC_$_INSTANCE_VARIABLES_SMMigrateEngine
- __OBJC_$_INSTANCE_VARIABLES_SMMigrateFiles
- __OBJC_$_INSTANCE_VARIABLES_SMMigrateSystemInfo
- __OBJC_$_INSTANCE_VARIABLES_SMMigrateUserDataStep
- __OBJC_$_INSTANCE_VARIABLES_SMMigrationActivity
- __OBJC_$_INSTANCE_VARIABLES_SMMigrationEngineElement
- __OBJC_$_INSTANCE_VARIABLES_SMMigrationEngineStep
- __OBJC_$_INSTANCE_VARIABLES_SMMigrationIncompatibleApplicationsList
- __OBJC_$_INSTANCE_VARIABLES_SMMigrationReport
- __OBJC_$_INSTANCE_VARIABLES_SMMigrationShoveElement
- __OBJC_$_INSTANCE_VARIABLES_SMMigrationStepElement
- __OBJC_$_INSTANCE_VARIABLES_SMProgressEntry
- __OBJC_$_INSTANCE_VARIABLES_SMReportNote
- __OBJC_$_INSTANCE_VARIABLES_SMSystemRuleHandler
- __OBJC_$_PROP_LIST_SMMigrateEngine
- __OBJC_$_PROP_LIST_SMMigrateFiles
- __OBJC_$_PROP_LIST_SMMigrateSystemInfo
- __OBJC_$_PROP_LIST_SMMigrateUserDataStep
- __OBJC_$_PROP_LIST_SMMigrationActivity
- __OBJC_$_PROP_LIST_SMMigrationEngineElement
- __OBJC_$_PROP_LIST_SMMigrationEngineStep
- __OBJC_$_PROP_LIST_SMMigrationReport
- __OBJC_$_PROP_LIST_SMMigrationShoveElement
- __OBJC_$_PROP_LIST_SMMigrationStepElement
- __OBJC_$_PROP_LIST_SMProgressEntry
- __OBJC_$_PROP_LIST_SMReportNote
- __OBJC_$_PROP_LIST_SMSystemRuleHandler
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SMMigrationEngineProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_SMMigrationEngineProtocol
- __OBJC_$_PROTOCOL_REFS_SMMigrationEngineProtocol
- __OBJC_CLASS_PROTOCOLS_$_SMMigrateEngine
- __OBJC_CLASS_PROTOCOLS_$_SMMigrateFiles
- __OBJC_CLASS_PROTOCOLS_$_SMMigrateSystemInfo
- __OBJC_CLASS_PROTOCOLS_$_SMMigrateUserDataStep
- __OBJC_CLASS_PROTOCOLS_$_SMMigrationEngineStep
- __OBJC_CLASS_RO_$_SMCommitDeferredSandboxElement
- __OBJC_CLASS_RO_$_SMConfMigratorAllowlist
- __OBJC_CLASS_RO_$_SMConfMigratorBundle
- __OBJC_CLASS_RO_$_SMConfMigratorCopyRule
- __OBJC_CLASS_RO_$_SMConfMigratorRules
- __OBJC_CLASS_RO_$_SMConfMigratorRunToolRule
- __OBJC_CLASS_RO_$_SMConfMigratorUserPathRule
- __OBJC_CLASS_RO_$_SMMigrateEngine
- __OBJC_CLASS_RO_$_SMMigrateFiles
- __OBJC_CLASS_RO_$_SMMigrateGroups
- __OBJC_CLASS_RO_$_SMMigrateSystemInfo
- __OBJC_CLASS_RO_$_SMMigrateUserDataStep
- __OBJC_CLASS_RO_$_SMMigrationActivity
- __OBJC_CLASS_RO_$_SMMigrationEngineElement
- __OBJC_CLASS_RO_$_SMMigrationEngineStep
- __OBJC_CLASS_RO_$_SMMigrationIncompatibleApplicationsList
- __OBJC_CLASS_RO_$_SMMigrationKernelManagementUtilityElement
- __OBJC_CLASS_RO_$_SMMigrationReport
- __OBJC_CLASS_RO_$_SMMigrationShoveElement
- __OBJC_CLASS_RO_$_SMMigrationStepElement
- __OBJC_CLASS_RO_$_SMMigrationUpdateKextCacheElement
- __OBJC_CLASS_RO_$_SMProgressEntry
- __OBJC_CLASS_RO_$_SMReportNote
- __OBJC_CLASS_RO_$_SMSystemRuleClient
- __OBJC_CLASS_RO_$_SMSystemRuleHandler
- __OBJC_LABEL_PROTOCOL_$_SMMigrationEngineProtocol
- __OBJC_METACLASS_RO_$_SMCommitDeferredSandboxElement
- __OBJC_METACLASS_RO_$_SMConfMigratorAllowlist
- __OBJC_METACLASS_RO_$_SMConfMigratorBundle
- __OBJC_METACLASS_RO_$_SMConfMigratorCopyRule
- __OBJC_METACLASS_RO_$_SMConfMigratorRules
- __OBJC_METACLASS_RO_$_SMConfMigratorRunToolRule
- __OBJC_METACLASS_RO_$_SMConfMigratorUserPathRule
- __OBJC_METACLASS_RO_$_SMMigrateEngine
- __OBJC_METACLASS_RO_$_SMMigrateFiles
- __OBJC_METACLASS_RO_$_SMMigrateGroups
- __OBJC_METACLASS_RO_$_SMMigrateSystemInfo
- __OBJC_METACLASS_RO_$_SMMigrateUserDataStep
- __OBJC_METACLASS_RO_$_SMMigrationActivity
- __OBJC_METACLASS_RO_$_SMMigrationEngineElement
- __OBJC_METACLASS_RO_$_SMMigrationEngineStep
- __OBJC_METACLASS_RO_$_SMMigrationIncompatibleApplicationsList
- __OBJC_METACLASS_RO_$_SMMigrationKernelManagementUtilityElement
- __OBJC_METACLASS_RO_$_SMMigrationReport
- __OBJC_METACLASS_RO_$_SMMigrationShoveElement
- __OBJC_METACLASS_RO_$_SMMigrationStepElement
- __OBJC_METACLASS_RO_$_SMMigrationUpdateKextCacheElement
- __OBJC_METACLASS_RO_$_SMProgressEntry
- __OBJC_METACLASS_RO_$_SMReportNote
- __OBJC_METACLASS_RO_$_SMSystemRuleClient
- __OBJC_METACLASS_RO_$_SMSystemRuleHandler
- __OBJC_PROTOCOL_$_SMMigrationEngineProtocol
- ___22-[SMMigrateEngine run]_block_invoke
- ___22-[SMMigrateEngine run]_block_invoke_2
- ___24-[SMMigrateEngine state]_block_invoke
- ___26-[SMMigrateEngine finally]_block_invoke
- ___26-[SMMigrateEngine finally]_block_invoke_2
- ___26-[SMMigrateEngine process]_block_invoke
- ___26-[SMMigrateEngine process]_block_invoke_2
- ___26-[SMMigrationReport note:]_block_invoke
- ___28-[SMMigrateEngine runEngine]_block_invoke
- ___28-[SMMigrateEngine runEngine]_block_invoke_2
- ___28-[SMMigrateEngine runEngine]_block_invoke_3
- ___28-[SMMigrateEngine runEngine]_block_invoke_4
- ___28-[SMMigrateEngine setState:]_block_invoke
- ___28-[SMMigrateEngine setState:]_block_invoke_2
- ___29-[SMMigrateFiles postProcess]_block_invoke
- ___29-[SMMigrateFiles postProcess]_block_invoke_2
- ___29-[SMMigrationStepElement run]_block_invoke
- ___30-[SMMigrateEngine addElement:]_block_invoke
- ___30-[SMMigrateEngine enginePhase]_block_invoke
- ___32-[SMMigrateEngine processErrors]_block_invoke
- ___32-[SMMigrationReport description]_block_invoke
- ___33+[SMMigrationReport sharedReport]_block_invoke
- ___33-[SMMigrateEngine reportProgress]_block_invoke
- ___33-[SMMigrateEngine runStepPrepare]_block_invoke
- ___33-[SMMigrateEngine runStepPrepare]_block_invoke_2
- ___33-[SMMigrateEngine runStepPrepare]_block_invoke_3
- ___33-[SMMigrateEngine runStepPrepare]_block_invoke_4
- ___33-[SMMigrateEngine runStepPrepare]_block_invoke_5
- ___33-[SMMigrateFiles dedupeWallpaper]_block_invoke
- ___33-[SMMigrateFiles dedupeWallpaper]_block_invoke_2
- ___33-[SMMigrationActivity hasStarted]_block_invoke
- ___33-[SMMigrationReport addActivity:]_block_invoke
- ___34+[SMSystemRuleClient sharedClient]_block_invoke
- ___34-[SMMigrateEngine setEnginePhase:]_block_invoke
- ___34-[SMMigrateSystemInfo postProcess]_block_invoke
- ___34-[SMMigrateSystemInfo postProcess]_block_invoke_2
- ___34-[SMMigrateSystemInfo postProcess]_block_invoke_3
- ___34-[SMMigrateSystemInfo postProcess]_block_invoke_4
- ___34-[SMMigrateSystemInfo postProcess]_block_invoke_5
- ___34-[SMMigrationActivity description]_block_invoke
- ___34-[SMMigrationActivity description]_block_invoke_2
- ___34-[SMMigrationActivity hasFinished]_block_invoke
- ___35+[SMPaths platformBinaryExceptions]_block_invoke
- ___36-[SMMigrateEngine startupNewRequest]_block_invoke
- ___37-[SMMigrationActivity activityLength]_block_invoke
- ___38-[SMMigrateEngine generateEngineSteps]_block_invoke
- ___38-[SMMigrateEngine systemsAreAvailable]_block_invoke
- ___38-[SMMigrateEngine systemsAreAvailable]_block_invoke_2
- ___38-[SMMigrateEngine systemsAreAvailable]_block_invoke_3
- ___39-[SMCopyEngine estimatedTimeToComplete]_block_invoke
- ___40-[SMMigrateEngine ensureSourceIsMounted]_block_invoke
- ___40-[SMMigrationActivity addChildActivity:]_block_invoke
- ___40-[SMMigrationReport saveProgressReport:]_block_invoke
- ___42-[SMMigrateEngine awaitSystemAvailability]_block_invoke
- ___42-[SMMigrateFiles setupCopiesForFileGroups]_block_invoke
- ___42-[SMMigrateSystemInfo copyMachineSettings]_block_invoke
- ___42-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_10
- ___42-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_11
- ___42-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_12
- ___42-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_13
- ___42-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_2
- ___42-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_3
- ___42-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_4
- ___42-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_5
- ___42-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_6
- ___42-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_7
- ___42-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_8
- ___42-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_9
- ___42-[SMMigrateSystemInfo copyNetworkSettings]_block_invoke
- ___42-[SMMigrateSystemInfo copyNetworkSettings]_block_invoke_2
- ___42-[SMMigrateSystemInfo copyNetworkSettings]_block_invoke_3
- ___42-[SMMigrateSystemInfo copyNetworkSettings]_block_invoke_4
- ___44-[SMMigrateEngine systemScannerAddedSystem:]_block_invoke
- ___45-[SMMigrateEngine acceptNewMigrationRequest:]_block_invoke
- ___46-[SMCopyEngineCopier finallyWithErrorOccured:]_block_invoke
- ___46-[SMMigrateEngine systemScannerRemovedSystem:]_block_invoke
- ___47-[SMCopyEngineCopier preProcessReturningError:]_block_invoke
- ___48-[SMMigrateSystemInfo repairTimezonePermissions]_block_invoke
- ___51-[SMMigrateEngine aggregateEngineErrorsAndWarnings]_block_invoke
- ___51-[SMMigrateEngine aggregateEngineErrorsAndWarnings]_block_invoke_2
- ___51-[SMMigrateEngine aggregateEngineErrorsAndWarnings]_block_invoke_3
- ___51-[SMMigrateEngine aggregateEngineErrorsAndWarnings]_block_invoke_4
- ___55-[SMMigrateEngine systemScannerSystemChanged:onSystem:]_block_invoke
- ___55-[SMProgress_Client verifyAndCreateIAUserWithPassword:]_block_invoke
- ___74+[SMMigrateFiles finalSizeAndCount:withFileGroupings:withUsersToTransfer:]_block_invoke
- ___78-[SMMigrationReport recordProgressPercentComplete:timeRemaining:transferRate:]_block_invoke
- ___78-[SMMigrationReport recordProgressPercentComplete:timeRemaining:transferRate:]_block_invoke_2
- ___block_descriptor_57_e8_32s40s_e5_v8?0l
- ___block_descriptor_64_e8_32s40s48s_e5_v8?0l
- ___block_descriptor_65_e8_32s40s48r_e5_v8?0l
- __block_literal_global.140
- __block_literal_global.32
- __block_literal_global.38
- __block_literal_global.43
- __block_literal_global.71
- __kCFURLInodeNumberKey
- _allowlist
- _database
- _dispatch_suspend
- _objc_msgSend$SM_bundleIsPlatformBinary
- _objc_msgSend$absoluteParentProgress
- _objc_msgSend$activities
- _objc_msgSend$activityLength
- _objc_msgSend$activityQueue
- _objc_msgSend$addActivity:
- _objc_msgSend$addChild:withPendingUnitCount:
- _objc_msgSend$addChildActivity:
- _objc_msgSend$addElement:
- _objc_msgSend$allowlist
- _objc_msgSend$applicationGroupBundlesToLocalizeFromPather:
- _objc_msgSend$bundleComponentVersion:
- _objc_msgSend$calculateProgressPercentages:
- _objc_msgSend$childActivities
- _objc_msgSend$childActivitiesQueue
- _objc_msgSend$completedFilesWereShoved
- _objc_msgSend$completedUnitCount
- _objc_msgSend$defaultHomeDirectory
- _objc_msgSend$detail
- _objc_msgSend$dictionaryFromStatement:
- _objc_msgSend$diskImagesInDirectory:error:
- _objc_msgSend$elementSupportsResuming
- _objc_msgSend$elementsShouldContinue
- _objc_msgSend$endDate
- _objc_msgSend$engineElements
- _objc_msgSend$estimateTimeRemaining
- _objc_msgSend$estimatedDuration
- _objc_msgSend$estimatedTimeRemaining
- _objc_msgSend$estimatedTimeRemainingAfterPhase:
- _objc_msgSend$estimatedTimeRemainingChanged:
- _objc_msgSend$estimatedTimeRemainingForPhase:
- _objc_msgSend$estimatedTimeToComplete
- _objc_msgSend$estimatedTimeToCompletePhase:
- _objc_msgSend$estimatedTotalTime
- _objc_msgSend$executeQuery:
- _objc_msgSend$extraTimeRemaining
- _objc_msgSend$fileHandleForWritingToURL:error:
- _objc_msgSend$finalSizeAndCountWithFileGroupings:withUsersToTransfer:
- _objc_msgSend$finish
- _objc_msgSend$fractionCompleted
- _objc_msgSend$generateAppsFileStep:
- _objc_msgSend$generateAutoLoginUserStep:
- _objc_msgSend$generateEngineElements
- _objc_msgSend$generateEngineSteps
- _objc_msgSend$generateEnterpriseMigrateFilesStep:
- _objc_msgSend$generateMachineSettingsStep:shouldSetOnlyUpdateSystemSettings:
- _objc_msgSend$generateMachineSettingsStep:withMacPathMap:
- _objc_msgSend$generateMigrateGuestAccountStep:
- _objc_msgSend$generatePeerToPeerStep:
- _objc_msgSend$generateStepsForEngine:withRequestType:mustGenerateUserStep:mustGenerateEnterpriseFilesStep:mustGenerateMachineSettingsStep:mustGenerateGuestStep:mustGenerateAppsFileStep:
- _objc_msgSend$generateUsersStep:
- _objc_msgSend$generateUsersStep:withMacPathMap:
- _objc_msgSend$hasFinished
- _objc_msgSend$hasRan
- _objc_msgSend$hasStarted
- _objc_msgSend$hexToData:
- _objc_msgSend$homeDirectory
- _objc_msgSend$increment
- _objc_msgSend$initWithAllowlistPath:
- _objc_msgSend$initWithEngine:steps:phase:
- _objc_msgSend$initWithMessage:
- _objc_msgSend$initWithName:
- _objc_msgSend$initWithParent:userInfo:
- _objc_msgSend$initWithPathMap:
- _objc_msgSend$initialTimeEstimate
- _objc_msgSend$isAllowed:
- _objc_msgSend$isApplicableRuleContext:
- _objc_msgSend$isBundle:
- _objc_msgSend$isNewerBundle:thanBundle:
- _objc_msgSend$lastCompletedPhase
- _objc_msgSend$lastProgressEntry
- _objc_msgSend$lastProgressLog
- _objc_msgSend$lastProgressPercentComplete
- _objc_msgSend$lastReportedTimeRemaining
- _objc_msgSend$lastReportedTransferRate
- _objc_msgSend$lastTimeRemainingUpdate
- _objc_msgSend$latestTimeEstimateFromOldProgress:
- _objc_msgSend$loadPlist:
- _objc_msgSend$localizeFoldersForApplications
- _objc_msgSend$localizeParentFolderForBundleWithURL:
- _objc_msgSend$migrateAllSettingsWithGroupName2:
- _objc_msgSend$migrateProgressKey:arguments:forMigrateStep:
- _objc_msgSend$migrateProgressString:forMigrateStep:
- _objc_msgSend$migrateWithRule2:
- _objc_msgSend$migrationElementsProgressPercentage
- _objc_msgSend$note:
- _objc_msgSend$noteQueue
- _objc_msgSend$notes
- _objc_msgSend$oneMinuteRemainingTime
- _objc_msgSend$parentProgress
- _objc_msgSend$parentProgressPendingUnits
- _objc_msgSend$percentComplete
- _objc_msgSend$phase
- _objc_msgSend$phaseNameForPhase:
- _objc_msgSend$platformBinaryExceptions
- _objc_msgSend$preProcess
- _objc_msgSend$preShove
- _objc_msgSend$prettyPrintEngineSteps
- _objc_msgSend$progress
- _objc_msgSend$progressEntries
- _objc_msgSend$progressPercentage
- _objc_msgSend$progressPercentageForPhase:
- _objc_msgSend$progressPercentages
- _objc_msgSend$progressString
- _objc_msgSend$progressUpdateLock
- _objc_msgSend$progressWithTotalUnitCount:
- _objc_msgSend$recordProgressPercentComplete:timeRemaining:transferRate:
- _objc_msgSend$recordedOneMinuteRemainingTime
- _objc_msgSend$removeDelegate:
- _objc_msgSend$reportProgress
- _objc_msgSend$reportTimeRemaining
- _objc_msgSend$rules
- _objc_msgSend$runOpenDirectoryMigrationTool
- _objc_msgSend$runStepPrepare
- _objc_msgSend$saveProgressReport:
- _objc_msgSend$setAbsoluteParentProgress:
- _objc_msgSend$setActivities:
- _objc_msgSend$setActivityQueue:
- _objc_msgSend$setChildActivities:
- _objc_msgSend$setChildActivitiesQueue:
- _objc_msgSend$setCompletedUnitCount:
- _objc_msgSend$setDate:
- _objc_msgSend$setDetail:
- _objc_msgSend$setEndDate:
- _objc_msgSend$setEngineElements:
- _objc_msgSend$setEstimatedDuration:
- _objc_msgSend$setEstimatedTimeRemaining:
- _objc_msgSend$setEstimatedTimeToComplete:
- _objc_msgSend$setEstimatedTotalTime:
- _objc_msgSend$setExtraTimeRemaining:
- _objc_msgSend$setFractionCompleted:
- _objc_msgSend$setHasRan:
- _objc_msgSend$setHint:
- _objc_msgSend$setInitialTimeEstimate:
- _objc_msgSend$setIsParentExpectingProgress:
- _objc_msgSend$setLastProgressEntry:
- _objc_msgSend$setLastProgressLog:
- _objc_msgSend$setLastProgressPercentComplete:
- _objc_msgSend$setLastReportedTimeRemaining:
- _objc_msgSend$setLastReportedTransferRate:
- _objc_msgSend$setLastTimeRemainingUpdate:
- _objc_msgSend$setMigrationElementsProgressPercentage:
- _objc_msgSend$setNoteQueue:
- _objc_msgSend$setNotes:
- _objc_msgSend$setOneMinuteRemainingTime:
- _objc_msgSend$setParentProgress:
- _objc_msgSend$setParentProgressPendingUnits:
- _objc_msgSend$setParentProgressQueue:
- _objc_msgSend$setPercentComplete:
- _objc_msgSend$setPhase:
- _objc_msgSend$setProgress:
- _objc_msgSend$setProgressEntries:
- _objc_msgSend$setProgressPercentage:
- _objc_msgSend$setProgressPercentage:forPhase:
- _objc_msgSend$setProgressPercentages:
- _objc_msgSend$setProgressPortionsForStep:
- _objc_msgSend$setProgressString:
- _objc_msgSend$setProgressUpdateLock:
- _objc_msgSend$setRecordedOneMinuteRemainingTime:
- _objc_msgSend$setReportTimeRemaining:
- _objc_msgSend$setStartDate:
- _objc_msgSend$setStepFinishedBytes:
- _objc_msgSend$setSteps:
- _objc_msgSend$setSystemRuleHandler:
- _objc_msgSend$setTotalUnitCount:
- _objc_msgSend$sharedClient
- _objc_msgSend$sharedReport
- _objc_msgSend$shoveCompletedSuccessfully
- _objc_msgSend$shoveFailed
- _objc_msgSend$shoveSandboxAtPath:sandBoxPath:error:
- _objc_msgSend$smoothTimeRemaining:
- _objc_msgSend$sortOrder
- _objc_msgSend$sortUsingSelector:
- _objc_msgSend$startDate
- _objc_msgSend$stepErrorWithException:
- _objc_msgSend$stepFinishedBytes
- _objc_msgSend$steps
- _objc_msgSend$synchronizeFile
- _objc_msgSend$systemRuleHandler
- _objc_msgSend$timeIntervalSinceDate:
- _objc_msgSend$timeRemaining
- _objc_msgSend$timeRemainingChangedForStep:
- _objc_msgSend$totalUnitCount
- _objc_msgSend$transferRateChanged:forStep:
- _objc_msgSend$tryLock
- _objc_msgSend$updateEngineForEngineSteps
- _objc_msgSend$updateTimeRemaining
- _objc_msgSend$updateTransferRate:
- _objc_msgSend$valueForColumnAtIndex:statement:type:
- _objc_msgSend$verifyAndCreateIAUserWithPassword:
- _objc_msgSend$verifyAndCreateIAUserWithPassword:andReplyBlock:
- _rules
- _sqlite3_close
- _sqlite3_column_count
- _sqlite3_column_decltype
- _sqlite3_column_int
- _sqlite3_column_int64
- _sqlite3_column_name
- _sqlite3_column_text
- _sqlite3_errmsg
- _sqlite3_finalize
- _sqlite3_open
- _sqlite3_prepare_v2
- _sqlite3_step
- platformBinaryExceptions.pbExceptionsOnce
- platformBinaryExceptions.platformBinaryExceptions
- sharedClient.onceToken
- sharedClient.sharedManager
- sharedReport.onceToken
- sharedReport.progressReport
CStrings:
+ "!Q"
+ "%@ (%2.2f MB)\n"
+ "%@ because target bundle is older"
+ "%@ because target bundle is older."
+ "%@Duration"
+ "%s: %@ -> %@ (%@ - %@)"
+ "%s: %@ -> %@ (%@) - No Engine Yet"
+ "&"
+ ",%@"
+ "-[SMCopyEngineNetworkCopier bomCopierEncounteredFatalFileError:atPath:error:]"
+ "-[SMEngine acceptNewMigrationRequest:]"
+ "-[SMEngine acknowledgeCompletedRequest]"
+ "-[SMEngine awaitSystemAvailability]_block_invoke"
+ "-[SMEngine doneWithCurrentRequest]"
+ "-[SMEngine engineSourceSystemAvailable]"
+ "-[SMEngine ensureSourceIsMounted]"
+ "-[SMEngine finally]"
+ "-[SMEngine finally]_block_invoke"
+ "-[SMEngine observeValueForKeyPath:ofObject:change:context:]"
+ "-[SMEngine predetermineTranslatedUIDs]"
+ "-[SMEngine printEngineDescription]"
+ "-[SMEngine processAnalyticsData]"
+ "-[SMEngine processErrors]"
+ "-[SMEngine runEngineSteps]"
+ "-[SMEngine runPather]"
+ "-[SMEngine run]_block_invoke"
+ "-[SMEngine run]_block_invoke_2"
+ "-[SMEngine setEngineSteps]"
+ "-[SMEngine setState:]"
+ "-[SMEngine setupForDataTransfer]"
+ "-[SMEngine spaceIsSufficient]"
+ "-[SMEngine startupNewRequest]"
+ "-[SMEngine stop]"
+ "-[SMEngine suspend]"
+ "-[SMEngine systemScannerAddedSystem:]_block_invoke"
+ "-[SMEngine systemScannerRemovedSystem:]"
+ "-[SMEngine systemsAreAvailable]_block_invoke"
+ "-[SMEngineStep copyFailedToCopyFile:shouldReportError:]"
+ "-[SMMigrateFilesStep copierFailed:error:]"
+ "-[SMMigrateFilesStep dedupeWallpaper]"
+ "-[SMMigrateFilesStep dedupeWallpaper]_block_invoke"
+ "-[SMMigrateFilesStep dedupeWallpaper]_block_invoke_2"
+ "-[SMMigrateFilesStep postProcess]"
+ "-[SMMigrateFilesStep setupCopiesForFileGroups]"
+ "-[SMMigrateFilesStep setupCopyNonSystemReceiptsForUpgrade]"
+ "-[SMMigrateGroupsStep createGroup:inDB:]"
+ "-[SMMigrateGroupsStep createGroupsInDB:]"
+ "-[SMMigrateGroupsStep deleteGroup:inDB:]"
+ "-[SMMigrateGroupsStep migrateGroups]"
+ "-[SMMigrateGroupsStep postProcess]"
+ "-[SMMigrateSystemInfoStep copierFailed:error:]"
+ "-[SMMigrateSystemInfoStep copyIgnorePremissionsSettings]"
+ "-[SMMigrateSystemInfoStep copyMachineSettings]"
+ "-[SMMigrateSystemInfoStep copyNetworkSettings]"
+ "-[SMMigrateSystemInfoStep copyRemoteManagementSettings]"
+ "-[SMMigrateSystemInfoStep copyTimeZone]"
+ "-[SMMigrateSystemInfoStep copyVirtualMemorySettings]"
+ "-[SMMigrateSystemInfoStep finishKerberosSetup]"
+ "-[SMMigrateSystemInfoStep getLastModifiedDate:]"
+ "-[SMMigrateSystemInfoStep migrateDirectoryServicesDatabase]"
+ "-[SMMigrateSystemInfoStep migrateGlobalPreferences]"
+ "-[SMMigrateSystemInfoStep migrateLockdownModeSetting]"
+ "-[SMMigrateSystemInfoStep migrateNetworkSettings]"
+ "-[SMMigrateSystemInfoStep postProcess]"
+ "-[SMMigrateSystemInfoStep prepareForServerMigration]"
+ "-[SMMigrateSystemInfoStep process]"
+ "-[SMMigrateSystemInfoStep repairDatavaultPermissions]"
+ "-[SMMigrateSystemInfoStep repairTimezonePermissions]"
+ "-[SMMigrateSystemInfoStep setupKerberos]"
+ "-[SMMigrateUserHomesStep copierFailed:error:]"
+ "-[SMMigrateUserHomesStep createComprehensiveCopierForUser:relativeTargetHome:]"
+ "-[SMMigrateUserHomesStep createHomeDirectoryCopiersForUsers]"
+ "-[SMMigrateUserHomesStep postProcess]"
+ "-[SMMigrateUserHomesStep relativeDestinationUserHomeForUser:]"
+ "-[SMMigrateUserHomesStep runCopier]"
+ "-[SMPaths allConfMigratorKillPaths]"
+ "-[SMRulesEngineDBClient dealloc]"
+ "-[SMRulesEngineDBClient init]"
+ "-[SMRulesEngineRuleHandler clearFirmlinkPathContents:]"
+ "-[SMRulesEngineRuleHandler copyFirmlinkContents:newPath:]"
+ "-[SMRulesEngineRuleHandler executeCopyRule:]"
+ "-[SMRulesEngineRuleHandler executeRule:]"
+ "-[SMRulesEngineRuleHandler executeToolAtPath:withArguments:andCopyPath:usingDeferral:allowSIP:]"
+ "-[SMRulesEngineRuleHandler executeToolPathRule:]"
+ "-[SMRulesEngineRuleHandler generateLegacyServerRulesFromPatherForUnreachablePaths:]"
+ "-[SMRulesEngineRuleHandler isApplicableInCurrentBootStage:]"
+ "-[SMRulesEngineRuleHandler isRuleApplicableForContext:]"
+ "-[SMRulesEngineRuleHandler isSkipLegacyRuleInLegacy:]"
+ "-[SMRulesEngineRuleHandler isSourceLessThanMaximumVersionAllowed:]"
+ "-[SMRulesEngineRuleHandler isSourceMoreThanMinimumVersionAllowed:]"
+ "-[SMRulesEngineRuleHandler processRuleGroup:]"
+ "-[SMRulesEngineRuleHandler renameConflictingPathOnTarget:fullTargetPath:targetPath:deferredCopy:]"
+ "-[SMRunEventHandler addDuration:forStep:]"
+ "-[SMRunEventHandler sendEvent]"
+ "-[SMShoveStep process]"
+ "=== Engine Steps (%@) ===\n"
+ "@\"PQLConnection\""
+ "@\"SMEngine\""
+ "@\"SMRulesEngineDBClient\""
+ "@\"SMRulesEngineRuleHandler\""
+ "@\"SMRunEventPayload\""
+ "A non-overwrite rule with a conflicting file on target, looking to resolve this...."
+ "AdditionalSystemPath"
+ "AttemptPeerToPeerStepDuration"
+ "B24@?0@\"SMPatherRule\"8@\"NSDictionary\"16"
+ "B24@?0@\"SMSystemRule\"8@\"NSDictionary\"16"
+ "Backup"
+ "Beginning user home scan in %@"
+ "Cannot generate engine steps, migrationRequest is nil."
+ "CommitDeferredSandboxStepDuration"
+ "Completed user home scan in %@"
+ "Connection did not gracefully close. Error description: %@"
+ "Copier: %@ %@ (%@ - %@)"
+ "Copier: %@ %@ (%@) - No Engine Yet"
+ "Copier: %@ -> %@ (%@ - %@)"
+ "Copier: %@ -> %@ (%@) - No Engine Yet"
+ "Couldn't create parent path %@"
+ "Created parent path %@"
+ "Customer build: opening up regular rules engine database."
+ "DataSize"
+ "Detected platform binary in sandbox. Removing %@"
+ "DisconnectCount"
+ "DoNotSearch"
+ "Engine source disappeared in %@ (%@). Restarting step..."
+ "Engine startup: APFS Data and System Mounted: %d"
+ "Engine startup: Current request is done. Awaiting acknowldgement from client."
+ "Engine startup: Current request requires a reboot before continuing."
+ "Engine startup: Desired Source LTID: %@"
+ "Engine startup: Desired Target LTID: %@"
+ "Engine startup: Entering post-reboot phase."
+ "Engine startup: Match for source system has a paired data volume but it's not unlocked/mounted. Ignoring source..."
+ "Engine startup: Match for source system has appeared."
+ "Engine startup: Match for source system has disappeared."
+ "Engine startup: Match for target system has appeared."
+ "Engine startup: Match for target system has disappeared."
+ "Engine startup: Target system has a paired data volume but it's not unlocked/mounted. Ignoring target..."
+ "Engine startup: Using current system at / as target for post reboot phase."
+ "Engine startup: Using current system at / to standin for empty target."
+ "Engine startup: Waiting for source and target systems to be available."
+ "Engine was suspended in %@ (%@). Restarting step..."
+ "Error determining preliminary UIDs: %@"
+ "Error opening rules engine database. Error description: %@"
+ "ErrorString"
+ "Errors reported during %@ (%@): %@"
+ "Exception thrown during %@ (%@): %@:%@"
+ "Executing rule: %@"
+ "Failed to initialize SMSystem_Daemon_SKDiskBased."
+ "Failed to process user home in %@: %@"
+ "File does not exist on source."
+ "First, removing any pre-existing files at %@"
+ "IgnoreSIP"
+ "InitialConnectionType"
+ "Install"
+ "Internal build: opening up internal rules engine database."
+ "IsCompleted"
+ "IsFatalFailure"
+ "IsPreReboot"
+ "IsSuccess"
+ "Kill paths: %@"
+ "Local"
+ "MigrateAutoLoginUserStepDuration"
+ "MigrateFilesStepDuration"
+ "MigrateGroupsStepDuration"
+ "MigrateGuestAccountStepDuration"
+ "MigrateSystemInfoStepDuration"
+ "MigrateUserAccountsStepDuration"
+ "MigrateUserHomesStepDuration"
+ "Migrating due to multiple bundles existing with this ID on the target system"
+ "Migrating since no bundle exists at that target path."
+ "Migrating since no target bundle with this ID exists."
+ "MixedLegacyServer"
+ "No action"
+ "Not a deferredCopy: Going to move %@ to %@."
+ "Not copying since source's version is the Apple-shipped default."
+ "Overwriting %@ (moving aside existing as ~%@)"
+ "PostProcess"
+ "Prepare"
+ "Preserve"
+ "Processing rule group: %@"
+ "ROSVRedirect"
+ "Rule applies for any servers but the source is none of the following: self-contained server, legacy server, mixed legacy."
+ "Rule applies for installs but the current request is not an upgrade."
+ "Rule applies for legacy servers but the source request is not a legacy server."
+ "Rule applies for migrations but the current request is an upgrade/update."
+ "Rule applies for mixed legacy servers but the source request is neither a legacy nor a mixed legacy server."
+ "Rule applies for modern servers but the source is neither a self-contained nor a mixed legacy server."
+ "Rule applies for updates but the current request is not an update."
+ "Rule can only run after %@, sourceVersion is %@"
+ "Rule can only run before %@, sourceVersion is %@"
+ "Rule is to be skipped in legacy server installs."
+ "Rule not applicable: %@"
+ "Rule only runs post-reboot but request state is in pre-reboot."
+ "Rule only runs pre-reboot but request state is in post-reboot."
+ "RunType"
+ "Running step %@ (%@)"
+ "SELECT * FROM patherRule WHERE type = %@"
+ "SELECT * FROM systemRule WHERE actionType = %@"
+ "SELECT * FROM systemRule WHERE ruleGroup = %@"
+ "SELECT checksum FROM fileChecksum WHERE filePath = %@"
+ "SELECT toolPath FROM systemRule WHERE actionType = %@"
+ "SM"
+ "SMCommitDeferredSandboxStep"
+ "SMEngine"
+ "SMEngineErrorDomain"
+ "SMEngineStep"
+ "SMMigrateFilesStep"
+ "SMMigrateGroupsStep"
+ "SMMigrateSystemInfoStep"
+ "SMMigrateUserHomesStep"
+ "SMPatherRule"
+ "SMRulesEngineDBClient"
+ "SMRulesEngineRuleHandler"
+ "SMRunEventHandler"
+ "SMRunEventPayload"
+ "SMShoveStep"
+ "SMStopwatch"
+ "SMSystemRulePlugin"
+ "SessionID"
+ "Shove failed but error was not retrieved."
+ "ShoveStepDuration"
+ "ShoveStepDurationKey"
+ "Shoved failed but error did not have list of failed files."
+ "Skipping because target resource is not a bundle."
+ "Skipping due to App Store receipt in target bundle."
+ "SourceModel"
+ "StateTracker"
+ "StopRequested"
+ "Successfully copied firmlink contents."
+ "Successfully initialized SMSystem_Daemon_SKDiskBased from mountpoint %@"
+ "SuspendCount"
+ "SystemCache"
+ "T@\"NSArray\",&,V_generatedLegacyServerRules"
+ "T@\"NSString\",C,N,V_errorString"
+ "T@\"NSString\",C,N,V_initialConnectionType"
+ "T@\"NSString\",C,N,V_runType"
+ "T@\"NSString\",C,N,V_sourceModel"
+ "T@\"NSString\",C,N,V_sourceVersion"
+ "T@\"NSString\",C,N,V_stateTracker"
+ "T@\"PQLConnection\",&,N,V_connection"
+ "T@\"SMEngine\",&,V_engine"
+ "T@\"SMEngine\",W,V_engine"
+ "T@\"SMEngine\",W,Vengine"
+ "T@\"SMRulesEngineDBClient\",&,N,V_rulesEngineDBClient"
+ "T@\"SMRulesEngineDBClient\",&,V_rulesEngineDBClient"
+ "T@\"SMRulesEngineRuleHandler\",&,N,V_rulesEngineRuleHandler"
+ "T@\"SMRulesEngineRuleHandler\",&,V_rulesEngineRuleHandler"
+ "T@\"SMRunEventPayload\",&,N,V_payload"
+ "TB,N,V_isCompleted"
+ "TB,N,V_isFatalFailure"
+ "TB,N,V_isPreReboot"
+ "TB,N,V_isRunning"
+ "TB,N,V_isSuccess"
+ "TB,N,V_stopRequested"
+ "TI,N,V_sessionID"
+ "TQ,N,V_dataSize"
+ "Target exists, will not copy %@ -> %@."
+ "Td,N,V_AttemptPeerToPeerStepDuration"
+ "Td,N,V_CommitDeferredSandboxStepDuration"
+ "Td,N,V_MigrateAutoLoginUserStepDuration"
+ "Td,N,V_MigrateFilesStepDuration"
+ "Td,N,V_MigrateGroupsStepDuration"
+ "Td,N,V_MigrateGuestAccountStepDuration"
+ "Td,N,V_MigrateSystemInfoStepDuration"
+ "Td,N,V_MigrateUserAccountsStepDuration"
+ "Td,N,V_MigrateUserHomesStepDuration"
+ "Td,N,V_ShoveStepDuration"
+ "Td,N,V_pathingDuration"
+ "Td,N,V_startTime"
+ "Td,N,V_totalDuration"
+ "Total Size: %2.2f MB\n"
+ "Tq,N,V_disconnectCount"
+ "Tq,N,V_suspendCount"
+ "Tq,R,N,V_type"
+ "Unknown rule context."
+ "Update"
+ "User may have forced a shutdown on machine."
+ "WiFi"
+ "[%s %ld] "
+ "[%s] Couldn't create sandbox at path : %@, %@"
+ "[%s] Couldn't remove exisiting sandbox at path : %@, %@"
+ "[%s] Couldn't set correct attributes on \"Cleanup At Startup\". Spotlight may not index during migration."
+ "[%s] Deleted conflicting bundle prior to shove: %@"
+ "[%s] Existing sandbox at path : %@, %2.2f MB"
+ "[%s] No system at path : %@"
+ "[%s] Shove failed: %@\n%@"
+ "[%s] Shoving %@ -> %@."
+ "[%s] Successfully shoved with soft errors: %@"
+ "[%s] Unable to delete conflicting bundle prior to shove: %@ (Error: %@)"
+ "[COPY FAILED] Failed to copy %@ to %@: %@"
+ "[COPY FAILED] Failed to defer copy %@ to %@"
+ "[COPY FAILED] Firmlink's content could not be copied."
+ "[COPY SUCCESS] Copied %@ to %@"
+ "[COPY SUCCESS] Defer copied %@ to %@"
+ "[Pather] Bundle check for %@: "
+ "[Pather] Detected non-regular file, avoiding: %@"
+ "[Pather] Found %lu system files, %lu out-of-band update files, %lu incompatible software paths, %lu firmlinked paths"
+ "[Pather] Found Rosetta receipt on source, classifying as user non-system receipt: %@"
+ "[Pather] Found Rosetta receipt on source, classifying as user system receipt: %@"
+ "[Pather] Found system receipt on source, copying over: %@"
+ "[Pather] Missing essential set of receipts."
+ "[Pather] Receipt failure: Filesystem is not active or has no root!"
+ "[Pather] cannot be initialized with undefined Request Type!"
+ "[Pathing Report] %@"
+ "[SMCopyEngineNopCopier] %@ %@ -> %@ (w/ flags %@)"
+ "[SMCopyEngineNopCopier] Adding '%@' to the force retry list."
+ "[SMCopyEngineNopCopier] Copying (unable to determine source relative path): %@"
+ "[SMCopyEngineNopCopier] Error %ld while copying %@ -> %@ (%@)"
+ "[SMCopyEngineNopCopier] Error %ld while copying %@ to %@ (%@)"
+ "[SMCopyEngineNopCopier] Failed to create the final destination (%@). %@"
+ "[SMCopyEngineNopCopier] Failed to delete destination sandbox. %@"
+ "[SMCopyEngineNopCopier] Failed to get attributes of the source path. (%@). %@"
+ "[SMCopyEngineNopCopier] Failed to set source attributes onto the final destination (%@). %@"
+ "[SMCopyEngineNopCopier] Moving %@ failed, clearing flags and trying again"
+ "[SMCopyEngineNopCopier] Node operation failed with %d."
+ "[SMCopyEngineNopCopier] Please File a Bug: Failed to gather path relative to mountpoint for source %@."
+ "[SMCopyEngineNopCopier] Please File a Bug: Source does not exist %@ -> %@"
+ "[SMCopyEngineNopCopier] Please File a Bug: couldn't construct URL for %@"
+ "[SMCopyEngineNopCopier] Please File a Bug: source or Destination not specified %@ -> %@"
+ "[SMCopyEngineNopCopier] Recopying (Partially Copied from Failed List): %@"
+ "[SMCopyEngineNopCopier] Recopying (partially copied from failed list): %@"
+ "[SMCopyEngineNopCopier] Recopying (partially copied): %@"
+ "[SMCopyEngineNopCopier] Root privilege when performing a backup or migrate operation."
+ "[SMCopyEngineNopCopier] Shove exited non-zero. Exit Status:%d"
+ "[SMCopyEngineNopCopier] Shove log: %@"
+ "[SMCopyEngineNopCopier] Skipping (Already Copied): %@"
+ "[SMCopyEngineNopCopier] Skipping (already copied): %@"
+ "[SMCopyEngineNopCopier] Source is a file and stat'ing it failed. (%@). %s"
+ "[SMCopyEngineNopCopier] Successfully moved %@, restoring flags at %@"
+ "[SMCopyEngineNopCopier] The destination is a file in folder copying mode, we tried deleting it but failed. (%@). %@"
+ "[SMCopyEngineNopCopier] The destination sandbox already exists and we were unable to delete it (%@). %@"
+ "[SMEngine] Done with current request"
+ "[SMEngine] Running pather..."
+ "[SMEngine] Source system not mounted, setting sourceSystem to nil."
+ "[SMEngine] Stopping..."
+ "[SMEngine] Suspending..."
+ "[SMManager] %@: Case Sensitive filesystem, while / is not."
+ "[SMManager] %@: CoreStorage Booter."
+ "[SMManager] %@: DSDB found."
+ "[SMManager] %@: Missing SystemVersion.plist"
+ "[SMManager] %@: Missing template receipt data"
+ "[SMManager] %@: No DirectoryServices database."
+ "[SMManager] %@: Not Case Sensitive filesystem, while / is."
+ "[SMManager] %@: Server installation."
+ "[SMManager] %@: System appears to be install media. Found these paths: %@"
+ "[SMManager] %@: System appears to be install partition."
+ "[SMManager] %@: The system appears to be damaged, since no local user database was found!"
+ "[SMManager] (vlb) Valid Light Backup"
+ "[SMManager] (vlb) has system version %@"
+ "[SMManager] (vlb) missing dslocal %@"
+ "[SMManager] Source too new: Source version: %@, Destination version: %@.%@"
+ "[SMManager] Source too old: Source version: %@"
+ "[SMRunEventHandler] Sending telemetry:\n%@"
+ "[SMRunEventHandler] Untracked engine step: %@"
+ "[System Defense] %@ -> Root? %@. Direct DV Enumeration? %@."
+ "[System Defense] Cannot target read-only location %@"
+ "[System Defense] Could not find a disk for path (possibly a broken symlink?) %@"
+ "[System Defense] Given targetDisk: %@ Role: %@"
+ "[System Defense] Hole-punching System Defense due to System Integrity Protection override for %@"
+ "[System Defense] Hole-punching System Integrity Protection due to SIP override for %@"
+ "[System Defense] Hole-punching System Integrity Protection during Upgrade or Update for %@"
+ "[System Defense] Initially redirected Root-destined path to Data Volume root: %@ -> %@"
+ "[System Defense] ROSV Permission denied. Input path: (%@) After Redirections path: (%@) Full Intended path: (%@), Symlink Expanded: (%@), Target System: (%@), TSFS Type: (%@), TS Root: (%@)"
+ "[System Defense] Redirecting read-only target %@ to %@"
+ "[System Defense] rootless_preflight rejected path: %@"
+ "_AttemptPeerToPeerStepDuration"
+ "_CommitDeferredSandboxStepDuration"
+ "_MigrateAutoLoginUserStepDuration"
+ "_MigrateFilesStepDuration"
+ "_MigrateGroupsStepDuration"
+ "_MigrateGuestAccountStepDuration"
+ "_MigrateSystemInfoStepDuration"
+ "_MigrateUserAccountsStepDuration"
+ "_MigrateUserHomesStepDuration"
+ "_ShoveStepDuration"
+ "_dataSize"
+ "_disconnectCount"
+ "_engineStepPhaseToString:"
+ "_generatedLegacyServerRules"
+ "_initialConnectionType"
+ "_isCompleted"
+ "_isFatalFailure"
+ "_isPreReboot"
+ "_isRunning"
+ "_isSuccess"
+ "_pathingDuration"
+ "_payload"
+ "_rulesEngineDBClient"
+ "_rulesEngineRuleHandler"
+ "_runType"
+ "_sessionID"
+ "_sourceModel"
+ "_sourceVersion"
+ "_stateTracker"
+ "_stopRequested"
+ "_suspendCount"
+ "_totalDuration"
+ "addDuration:forStep:"
+ "close:"
+ "com.apple.massStorage.SystemMigration.Run"
+ "dataSize"
+ "deferredCopy: Going to copy %@ to %@."
+ "disconnectCount"
+ "diskImagesInDirectory:qos:error:"
+ "elapsedTime"
+ "ensureSourceMounted: Source is mounted but its data/system pair not both mounted."
+ "executeCopyRule:"
+ "executeRule:"
+ "executeToolPathRule:"
+ "fetch:"
+ "finalizeAndSendTelemetry"
+ "generateLegacyServerRulesFromPatherForUnreachablePaths:"
+ "generateStateTrackerKeyForStep:phase:"
+ "generateTargetPath:"
+ "generatedLegacyServerRules"
+ "getAllPluginPaths"
+ "getPatherRulesByType:"
+ "getPayloadDictionary"
+ "getRulesByActionType:"
+ "getRunType:"
+ "initWithEngine:map:"
+ "initWithUnreachableLegacyPath:"
+ "initialConnectionType"
+ "instancesRespondToSelector:"
+ "intAtIndex:"
+ "isApplicableRuleForCurrentMigrationType:"
+ "isCombinedSoftwareUpdateAndMigration:"
+ "isCompleted"
+ "isDeferredCopy:"
+ "isFatalFailure"
+ "isPathPlatformBinary"
+ "isPathingRuleApplicableForContext:"
+ "isPreReboot"
+ "isRuleApplicableForContext:"
+ "isRuleApplicableForPather:"
+ "isSuccess"
+ "longLongAtIndex:"
+ "next"
+ "no target bundle exists"
+ "openAtURL:withFlags:error:"
+ "pathingDuration"
+ "payload"
+ "payloadKeyForStepDuration:"
+ "predicateWithBlock:"
+ "prepareKerberosAndServerMigration"
+ "printEngineDescription"
+ "processRuleGroup:"
+ "q24@?0@\"SMEngineStep\"8@\"SMEngineStep\"16"
+ "recordCompletion"
+ "recordDataSize:"
+ "recordDisconnect"
+ "recordError:errorCode:"
+ "recordFatalFailure"
+ "recordInitialConnectionType:"
+ "recordPathingDuration:"
+ "recordStop"
+ "recordSuccess"
+ "recordSuspend"
+ "recordTotalDuration:"
+ "renameConflictingPathOnTarget:fullTargetPath:targetPath:deferredCopy:"
+ "resultSetToSMPatherRule:"
+ "resultSetToSMSystemRule:"
+ "rulesEngineDBClient"
+ "rulesEngineRuleHandler"
+ "runEngineSteps"
+ "runPather"
+ "runType"
+ "sendEvent"
+ "sessionID"
+ "setAttemptPeerToPeerStepDuration:"
+ "setCommitDeferredSandboxStepDuration:"
+ "setDataSize:"
+ "setDisconnectCount:"
+ "setEngineSteps"
+ "setGeneralKeys:"
+ "setGeneratedLegacyServerRules:"
+ "setInitialConnectionType:"
+ "setIsCompleted:"
+ "setIsFatalFailure:"
+ "setIsPreReboot:"
+ "setIsRunning:"
+ "setIsSuccess:"
+ "setMigrateAutoLoginUserStepDuration:"
+ "setMigrateFilesStepDuration:"
+ "setMigrateGroupsStepDuration:"
+ "setMigrateGuestAccountStepDuration:"
+ "setMigrateSystemInfoStepDuration:"
+ "setMigrateUserAccountsStepDuration:"
+ "setMigrateUserHomesStepDuration:"
+ "setPathingDuration:"
+ "setPayload:"
+ "setRulesEngineDBClient:"
+ "setRulesEngineRuleHandler:"
+ "setRunType:"
+ "setSessionID:"
+ "setShoveStepDuration:"
+ "setSourceModel:"
+ "setSourceVersion:"
+ "setStateTracker:"
+ "setStateTracker:phase:"
+ "setStopRequested:"
+ "setSuspendCount:"
+ "setTotalDuration:"
+ "setupEngineBeforeRunningSteps"
+ "setupForDataTransfer"
+ "shouldContinueSteps"
+ "sourceModel"
+ "stateTracker"
+ "stopRequested"
+ "stringAtIndex:"
+ "stringFromActionType:"
+ "stringFromContext:"
+ "stringFromType:"
+ "suspendCount"
+ "target resource is a bundle"
+ "target resource is not a bundle"
+ "totalDuration"
+ "typeFromString:"
+ "updateUserAccountWithReply:"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v32@0:8@16q24"
+ "{%@,%ld}"
+ "\xc1"
- "\t"
- "\n\t - %@"
- "\n%@\n\n"
- "\n=== End ===\n"
- "\nActivities (%ld):\n"
- "\nNotes (%ld):\n"
- "\nTotal Time: %.2fs"
- "   (I) Move of %@ successful: restoring flags at %@"
- "   (I) Move of locked %@ failed: clearing flags and trying again"
- " (%.2f MB/s)"
- " (Initial Estimate: %.2fs)"
- " (completed"
- " (estimated %f seconds to complete; %f seconds remaining"
- " - %.2f MB"
- " - %@\n"
- " - %@ (estimated %f seconds to complete; estimated %f seconds remaining; %.2f%% of element)\n"
- " Initial Estimate: %.2fs"
- "!T"
- "\"%@\" occurred %ldx"
- "###################################"
- "%.2f percent complete; Current Time Remaining Estimate: %.2f seconds; Raw Time Remaining Estimate: %.2f seconds; Extra Time: %.2f seconds"
- "%@\n"
- "%@ (%.2f%%)"
- "%@ - %@ (%.2f%%)"
- "%@ - Prepare"
- "%@ due to version comparison (local bundle is at %@)."
- "%@ due to version comparison (local exists at same path)."
- "%@ due to version comparison."
- "%@, %0.2f, %0.2f, %0.2f\n"
- "%@s (%ld steps for %@):\n"
- "%ld receipts found."
- "%ld: %@ (%2.2f MB)\n"
- "(Node Error): Adding '%@' to the force retry list."
- "(Node Error): Error %ld while copying %@ to %@ (%@)"
- "(NodeOp) %@ \"%@\" -> \"%@\" Final name: \"%@\" (Flags used: %@)"
- "(SB) Couldn't create sandbox at path : %@, %@"
- "(SB) Couldn't remove exisiting sandbox at path : %@, %@"
- "(SB) Couldn't set correct attributes on \"Cleanup At Startup\". Spotlight may not index during migration."
- "(SB) Deleted conflicting bundle prior to shove: %@"
- "(SB) Existing sandbox at path : %@, %2.2f MB"
- "(SB) No system at path : %@"
- "(SB) Unable to delete conflicting bundle prior to shove: %@ (Error: %@)"
- "+[SMConfMigratorBundle isNewerBundle:thanBundle:]"
- "+[SMMigrateUserToolBox verifyAndCreateIAUserWithPassword:]"
- "-[SMConfMigrator migrateAllSettingsWithGroupName2:]"
- "-[SMConfMigrator migrateWithRule2:]"
- "-[SMCopyEngine estimatedTimeToComplete]"
- "-[SMCopyEngine run]_block_invoke"
- "-[SMCopyEngineCopier finallyWithErrorOccured:]_block_invoke"
- "-[SMCopyEngineCopier preProcessReturningError:]_block_invoke"
- "-[SMMacUser_Daemon statsForHomeDirectoryWithPather:]"
- "-[SMMigrateEngine acceptNewMigrationRequest:]"
- "-[SMMigrateEngine acknowledgeCompletedRequest]"
- "-[SMMigrateEngine awaitSystemAvailability]_block_invoke"
- "-[SMMigrateEngine doneWithCurrentRequest]"
- "-[SMMigrateEngine engineSourceSystemAvailable]"
- "-[SMMigrateEngine ensureSourceIsMounted]"
- "-[SMMigrateEngine finalSizeAndCountForMigrationRequest:]"
- "-[SMMigrateEngine finally]"
- "-[SMMigrateEngine finally]_block_invoke"
- "-[SMMigrateEngine finally]_block_invoke_2"
- "-[SMMigrateEngine generateEngineElements]"
- "-[SMMigrateEngine generateEngineSteps]_block_invoke"
- "-[SMMigrateEngine migrateProgressString:forMigrateStep:]"
- "-[SMMigrateEngine observeValueForKeyPath:ofObject:change:context:]"
- "-[SMMigrateEngine predetermineTranslatedUIDs]"
- "-[SMMigrateEngine prepare]"
- "-[SMMigrateEngine prettyPrintEngineSteps]"
- "-[SMMigrateEngine processAnalyticsData]"
- "-[SMMigrateEngine processErrors]"
- "-[SMMigrateEngine process]"
- "-[SMMigrateEngine process]_block_invoke"
- "-[SMMigrateEngine process]_block_invoke_2"
- "-[SMMigrateEngine reportProgress]_block_invoke"
- "-[SMMigrateEngine runEngine]"
- "-[SMMigrateEngine runEngine]_block_invoke_2"
- "-[SMMigrateEngine runEngine]_block_invoke_3"
- "-[SMMigrateEngine runEngine]_block_invoke_4"
- "-[SMMigrateEngine runStepPrepare]"
- "-[SMMigrateEngine runStepPrepare]_block_invoke"
- "-[SMMigrateEngine runStepPrepare]_block_invoke_2"
- "-[SMMigrateEngine runStepPrepare]_block_invoke_3"
- "-[SMMigrateEngine runStepPrepare]_block_invoke_4"
- "-[SMMigrateEngine runStepPrepare]_block_invoke_5"
- "-[SMMigrateEngine run]_block_invoke"
- "-[SMMigrateEngine run]_block_invoke_2"
- "-[SMMigrateEngine setState:]"
- "-[SMMigrateEngine smoothTimeRemaining:]"
- "-[SMMigrateEngine spaceIsSufficient]"
- "-[SMMigrateEngine startupNewRequest]"
- "-[SMMigrateEngine stop]"
- "-[SMMigrateEngine suspend]"
- "-[SMMigrateEngine systemScannerAddedSystem:]_block_invoke"
- "-[SMMigrateEngine systemScannerRemovedSystem:]"
- "-[SMMigrateEngine systemsAreAvailable]"
- "-[SMMigrateEngine systemsAreAvailable]_block_invoke"
- "-[SMMigrateFiles _runCopier]"
- "-[SMMigrateFiles copierFailed:error:]"
- "-[SMMigrateFiles dedupeWallpaper]"
- "-[SMMigrateFiles dedupeWallpaper]_block_invoke"
- "-[SMMigrateFiles dedupeWallpaper]_block_invoke_2"
- "-[SMMigrateFiles postProcess]"
- "-[SMMigrateFiles postProcess]_block_invoke"
- "-[SMMigrateFiles postProcess]_block_invoke_2"
- "-[SMMigrateFiles setupCopiesForFileGroups]"
- "-[SMMigrateFiles setupCopyNonSystemReceiptsForUpgrade]"
- "-[SMMigrateGroups createGroup:inDB:]"
- "-[SMMigrateGroups createGroupsInDB:]"
- "-[SMMigrateGroups deleteGroup:inDB:]"
- "-[SMMigrateGroups migrateGroups]"
- "-[SMMigrateGroups postProcess]"
- "-[SMMigrateSystemInfo copierFailed:error:]"
- "-[SMMigrateSystemInfo copyIgnorePremissionsSettings]"
- "-[SMMigrateSystemInfo copyMachineSettings]"
- "-[SMMigrateSystemInfo copyMachineSettings]_block_invoke"
- "-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_10"
- "-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_11"
- "-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_12"
- "-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_13"
- "-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_2"
- "-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_3"
- "-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_4"
- "-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_5"
- "-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_6"
- "-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_7"
- "-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_8"
- "-[SMMigrateSystemInfo copyMachineSettings]_block_invoke_9"
- "-[SMMigrateSystemInfo copyNetworkSettings]"
- "-[SMMigrateSystemInfo copyNetworkSettings]_block_invoke"
- "-[SMMigrateSystemInfo copyNetworkSettings]_block_invoke_2"
- "-[SMMigrateSystemInfo copyNetworkSettings]_block_invoke_3"
- "-[SMMigrateSystemInfo copyNetworkSettings]_block_invoke_4"
- "-[SMMigrateSystemInfo copyRemoteManagementSettings]"
- "-[SMMigrateSystemInfo copyTimeZone]"
- "-[SMMigrateSystemInfo copyVirtualMemorySettings]"
- "-[SMMigrateSystemInfo deferCopyPath:sourceSystem:targetSystme:]"
- "-[SMMigrateSystemInfo finishKerberosSetup]"
- "-[SMMigrateSystemInfo getLastModifiedDate:]"
- "-[SMMigrateSystemInfo migrateDirectoryServicesDatabase]"
- "-[SMMigrateSystemInfo migrateGlobalPreferences]"
- "-[SMMigrateSystemInfo migrateLockdownModeSetting]"
- "-[SMMigrateSystemInfo migrateNetworkSettings]"
- "-[SMMigrateSystemInfo postProcess]"
- "-[SMMigrateSystemInfo postProcess]_block_invoke"
- "-[SMMigrateSystemInfo postProcess]_block_invoke_2"
- "-[SMMigrateSystemInfo postProcess]_block_invoke_3"
- "-[SMMigrateSystemInfo postProcess]_block_invoke_5"
- "-[SMMigrateSystemInfo prepareForServerMigration]"
- "-[SMMigrateSystemInfo process]"
- "-[SMMigrateSystemInfo repairDatavaultPermissions]"
- "-[SMMigrateSystemInfo repairTimezonePermissions]"
- "-[SMMigrateSystemInfo setupKerberos]"
- "-[SMMigrateUserDataStep copierFailed:error:]"
- "-[SMMigrateUserDataStep createComprehensiveCopierForUser:relativeTargetHome:]"
- "-[SMMigrateUserDataStep createHomeDirectoryCopiersForUsers]"
- "-[SMMigrateUserDataStep postProcess]"
- "-[SMMigrateUserDataStep relativeDestinationUserHomeForUser:]"
- "-[SMMigrateUserDataStep runCopier]"
- "-[SMMigrationEngineStep copyFailedToCopyFile:shouldReportError:]"
- "-[SMMigrationIncompatibleApplicationsList loadPlist:]"
- "-[SMMigrationIncompatibleApplicationsList prepareIncompatibleApplicationsList:forSMSystem:]"
- "-[SMMigrationKernelManagementUtilityElement run]"
- "-[SMMigrationShoveElement run]"
- "-[SMMigrationStepElement run]"
- "-[SMMigrationStepElement run]_block_invoke"
- "-[SMPaths loadAllFakelinks]"
- "-[SMPathsDirectoryClassifier addBundle:atLocation:withStats:isPlatformBinary:]"
- "-[SMSystemRuleClient executeQuery:]"
- "-[SMSystemRuleClient openDatabase]"
- "-[SMSystemRuleHandler clearFirmlinkPathContents:]"
- "-[SMSystemRuleHandler copyFirmlinkContents:newPath:]"
- "-[SMSystemRuleHandler generateDestinationPath:]"
- "-[SMSystemRuleHandler isApplicableInCurrentBootStage:]"
- "-[SMSystemRuleHandler isApplicableRuleContext:]"
- "-[SMSystemRuleHandler isSkipLegacyRuleInLegacy:]"
- "-[SMSystemRuleHandler isSourceLessThanMaximumVersionAllowed:]"
- "-[SMSystemRuleHandler isSourceMoreThanMinimumVersionAllowed:]"
- "-[SMSystemRuleHandler isSourcePathAppleShippedDefault:]"
- "-[SMWindowsMigrateComponentStep process]"
- "-[SMWindowsMigrateFilesStep process]"
- "-orig"
- "-source"
- "-target"
- "/Applications/Server.app/"
- "/Library/Application Support/App Store/adoption.plist"
- "/Library/Developer/XcodeSever"
- "/Library/Frameworks/HPDeviceModel.framework"
- "/Library/Frameworks/HPPml.framework"
- "/Library/Frameworks/HPServicesInterface.framework"
- "/Library/Frameworks/HPSmartPrint.framework"
- "/Library/Frameworks/JavaMonitorSupport.framework"
- "/Library/Internet Plug-Ins/Flash Player.plugin/"
- "/Library/LaunchDaemons/com.barebones.bbedit.plist"
- "/Library/Preferences/Audio/com.apple.audio.DeviceSettings.plist"
- "/Library/Preferences/Audio/com.apple.audio.SystemSettings.plist"
- "/Library/Preferences/DirectoryService/"
- "/Library/Preferences/OpenDirectory/"
- "/Library/Preferences/SystemConfiguration/com.apple.network.eapolclient.configuration.plist"
- "/Library/Preferences/com.apple.alf.plist"
- "/Library/Preferences/com.apple.audio.DeviceSettings.plist"
- "/Library/Preferences/com.apple.audio.SystemSettings.plist"
- "/Library/Preferences/com.apple.pcastagentd.plist"
- "/Library/Preferences/com.apple.windowserver.plist"
- "/Library/PrivilegedHelperTools/com.barebones.bbedit"
- "/Library/Scripts/Address Book Scripts/Address Importers/Entourage.scpt"
- "/Library/Scripts/Address Book Scripts/Address Importers/Eudora.scpt"
- "/Library/Scripts/Address Book Scripts/Address Importers/Tab Delimited Text File.scpt"
- "/Library/Scripts/Address Book Scripts/Helper Scripts/Entourage.scpt"
- "/Library/Scripts/Address Book Scripts/Helper Scripts/Eudora.scpt"
- "/Library/Scripts/Address Book Scripts/Helper Scripts/Import Helper.scpt"
- "/Library/Scripts/Address Book Scripts/Helper Scripts/Outlook Express.scpt"
- "/Library/Scripts/Address Book Scripts/Import Addresses.scpt"
- "/Library/Scripts/Basics/AppleScript Help.scpt"
- "/Library/Scripts/Basics/AppleScript Website.scpt"
- "/Library/Scripts/Basics/Open Script Editor.scpt"
- "/Library/Scripts/Finder Scripts/About Finder Scripts....scpt"
- "/Library/Scripts/Finder Scripts/Add to File Names.scpt"
- "/Library/Scripts/Finder Scripts/Add to Folder Names.scpt"
- "/Library/Scripts/Finder Scripts/Change Case of Item Names.scpt"
- "/Library/Scripts/Finder Scripts/Finder Windows - Hide All.scpt"
- "/Library/Scripts/Finder Scripts/Finder Windows - Show All.scpt"
- "/Library/Scripts/Finder Scripts/Replace Text in Item Names.scpt"
- "/Library/Scripts/Finder Scripts/Switch to Finder.scpt"
- "/Library/Scripts/Finder Scripts/Trim File Names.scpt"
- "/Library/Scripts/Finder Scripts/Trim Folder Names.scpt"
- "/Library/Scripts/Folder Action Scripts/Image - Add Icon.scpt"
- "/Library/Scripts/Folder Action Scripts/Image - Duplicate as JPEG.scpt"
- "/Library/Scripts/Folder Action Scripts/Image - Duplicate as PNG.scpt"
- "/Library/Scripts/Folder Action Scripts/Image - Duplicate as TIFF.scpt"
- "/Library/Scripts/Folder Action Scripts/Image - Flip Horizontal.scpt"
- "/Library/Scripts/Folder Action Scripts/Image - Flip Vertical.scpt"
- "/Library/Scripts/Folder Action Scripts/Image - Info to Comment.scpt"
- "/Library/Scripts/Folder Action Scripts/Image - Rotate Left.scpt"
- "/Library/Scripts/Folder Action Scripts/Image - Rotate Right.scpt"
- "/Library/Scripts/Folder Action Scripts/add - new item alert.scpt"
- "/Library/Scripts/Folder Action Scripts/close - close sub-folders.scpt"
- "/Library/Scripts/Folder Action Scripts/convert - PostScript to PDF.scpt"
- "/Library/Scripts/Folder Action Scripts/open - show comments in dialog.scpt"
- "/Library/Scripts/Folder Actions/Attach Script to Folder.scpt"
- "/Library/Scripts/Folder Actions/Disable Folder Actions.scpt"
- "/Library/Scripts/Folder Actions/Enable Folder Actions.scpt"
- "/Library/Scripts/Folder Actions/Remove Folder Actions.scpt"
- "/Library/Scripts/Font Book/Create Font Sample.scpt"
- "/Library/Scripts/Font Book/Create Italic collection.scpt"
- "/Library/Scripts/Font Book/Create collection from/Copyright.scpt"
- "/Library/Scripts/Font Book/Create collection from/Font type.scpt"
- "/Library/Scripts/Font Book/Create collection from/Style name.scpt"
- "/Library/Scripts/Font Book/Delete empty collections.scpt"
- "/Library/Scripts/FontSync Scripts/Create FontSync Profile.scpt"
- "/Library/Scripts/FontSync Scripts/Match FontSync Profiles.scpt"
- "/Library/Scripts/Info Scripts/Current Date & Time.scpt"
- "/Library/Scripts/Info Scripts/Font Sampler.scpt"
- "/Library/Scripts/Internet Services/About Internet Services Scripts....scpt"
- "/Library/Scripts/Internet Services/Current Temperature by Zipcode.scpt"
- "/Library/Scripts/Internet Services/Stock Quote.scpt"
- "/Library/Scripts/Navigation Scripts/New Applications Window.scpt"
- "/Library/Scripts/Navigation Scripts/New Documents Window.scpt"
- "/Library/Scripts/Navigation Scripts/New Favorites Window.scpt"
- "/Library/Scripts/Navigation Scripts/New Home Window.scpt"
- "/Library/Scripts/Navigation Scripts/Open Special Folder.scpt"
- "/Library/Scripts/Printing Scripts/About \"Convert\" Scripts.scpt"
- "/Library/Scripts/Printing Scripts/About \"Print Window\" Scripts.scpt"
- "/Library/Scripts/Printing Scripts/Convert To PDF.scpt"
- "/Library/Scripts/Printing Scripts/Convert To PostScript.scpt"
- "/Library/Scripts/Printing Scripts/Print Window With Subfolders.scpt"
- "/Library/Scripts/Printing Scripts/Print Window.scpt"
- "/Library/Scripts/Script Editor Scripts/About these scripts....scpt"
- "/Library/Scripts/Script Editor Scripts/Action Clauses/Ignoring App Responses.scpt"
- "/Library/Scripts/Script Editor Scripts/Action Clauses/Timeout Clause.scpt"
- "/Library/Scripts/Script Editor Scripts/Action Clauses/Transaction Clause.scpt"
- "/Library/Scripts/Script Editor Scripts/Comment Tags.scpt"
- "/Library/Scripts/Script Editor Scripts/Conditionals/Condition for Each List Item.scpt"
- "/Library/Scripts/Script Editor Scripts/Conditionals/if-then ... else <selection> end.scpt"
- "/Library/Scripts/Script Editor Scripts/Conditionals/if-then <selection> else ... end.scpt"
- "/Library/Scripts/Script Editor Scripts/Conditionals/if-then <selection> end.scpt"
- "/Library/Scripts/Script Editor Scripts/Dialogs/Dialog - 1 Btn Cancel.scpt"
- "/Library/Scripts/Script Editor Scripts/Dialogs/Dialog - 1 Btn OK.scpt"
- "/Library/Scripts/Script Editor Scripts/Dialogs/Dialog - 1 Btn.scpt"
- "/Library/Scripts/Script Editor Scripts/Dialogs/Dialog - 2 Btn.scpt"
- "/Library/Scripts/Script Editor Scripts/Dialogs/Dialog - 2 Btns 2 Actions.scpt"
- "/Library/Scripts/Script Editor Scripts/Dialogs/Dialog - 3 Btn.scpt"
- "/Library/Scripts/Script Editor Scripts/Dialogs/Dialog - 3 Btns 2 Actions.scpt"
- "/Library/Scripts/Script Editor Scripts/Dialogs/Dialog - 3 Btns 3 Actions.scpt"
- "/Library/Scripts/Script Editor Scripts/Dialogs/Text Input - 1 Btn.scpt"
- "/Library/Scripts/Script Editor Scripts/Dialogs/Text Input - 2 Btns.scpt"
- "/Library/Scripts/Script Editor Scripts/Dialogs/Text Input - 3 Btns.scpt"
- "/Library/Scripts/Script Editor Scripts/Error Handlers/Message and Cancel.scpt"
- "/Library/Scripts/Script Editor Scripts/Error Handlers/Message and OK.scpt"
- "/Library/Scripts/Script Editor Scripts/Error Handlers/Message and Return.scpt"
- "/Library/Scripts/Script Editor Scripts/Error Handlers/Message if not Cancel.scpt"
- "/Library/Scripts/Script Editor Scripts/Error Handlers/No Message.scpt"
- "/Library/Scripts/Script Editor Scripts/Error Handlers/Write Error to Log.scpt"
- "/Library/Scripts/Script Editor Scripts/Folder Actions Handlers/Adding To Folder.scpt"
- "/Library/Scripts/Script Editor Scripts/Folder Actions Handlers/Closing Folder Window.scpt"
- "/Library/Scripts/Script Editor Scripts/Folder Actions Handlers/Moving Folder Window.scpt"
- "/Library/Scripts/Script Editor Scripts/Folder Actions Handlers/Opening Folder.scpt"
- "/Library/Scripts/Script Editor Scripts/Folder Actions Handlers/Removing Folder Items.scpt"
- "/Library/Scripts/Script Editor Scripts/Image Manipulation/Resize.scpt"
- "/Library/Scripts/Script Editor Scripts/Image Manipulation/Rotate Clockwise.scpt"
- "/Library/Scripts/Script Editor Scripts/Image Manipulation/Rotate Counter-Clockwise.scpt"
- "/Library/Scripts/Script Editor Scripts/Image Manipulation/Scale.scpt"
- "/Library/Scripts/Script Editor Scripts/Iterate Items/Files of Chosen Folder.scpt"
- "/Library/Scripts/Script Editor Scripts/Iterate Items/Images of Chosen Folder.scpt"
- "/Library/Scripts/Script Editor Scripts/Iterate Items/Items of Finder Selection.scpt"
- "/Library/Scripts/Script Editor Scripts/Repeat Routines/Process Every Item.scpt"
- "/Library/Scripts/Script Editor Scripts/Repeat Routines/Special Case First & Last.scpt"
- "/Library/Scripts/Script Editor Scripts/Repeat Routines/Special Case First Item.scpt"
- "/Library/Scripts/Script Editor Scripts/Repeat Routines/Special Case Last Item.scpt"
- "/Library/Scripts/Script Editor Scripts/String Comparison/Considering Clause.scpt"
- "/Library/Scripts/Script Editor Scripts/String Comparison/Ignoring Clause.scpt"
- "/Library/Scripts/Script Editor Scripts/Tell Blocks/Tell \"Finder\".scpt"
- "/Library/Scripts/Script Editor Scripts/Tell Blocks/Tell \"System Events\".scpt"
- "/Library/Scripts/Script Editor Scripts/Tell Blocks/Tell Application.scpt"
- "/Library/Scripts/Script Editor Scripts/Tell Blocks/Using Terms Clause.scpt"
- "/Library/Scripts/Sherlock Scripts/Search Internet.scpt"
- "/Library/Scripts/URLs/Apple Store.scpt"
- "/Library/Scripts/URLs/AppleScript Related Sites/AppleScript Sourcebook.scpt"
- "/Library/Scripts/URLs/AppleScript Related Sites/AppleScript Website.scpt"
- "/Library/Scripts/URLs/AppleScript Related Sites/MacScripter.net.scpt"
- "/Library/Scripts/URLs/CNN.scpt"
- "/Library/Scripts/URLs/Download Weather Map.scpt"
- "/Library/Scripts/URLs/MacWeek.scpt"
- "/Library/Scripts/URLs/Macintouch.scpt"
- "/Library/Tomcat/webapps/axis"
- "/Library/User Pictures/Animals/Butterfly.tif"
- "/Library/User Pictures/Animals/Cat.tif"
- "/Library/User Pictures/Animals/Cheetah.tif"
- "/Library/User Pictures/Animals/Dog.tif"
- "/Library/User Pictures/Animals/Dragonfly.tif"
- "/Library/User Pictures/Animals/Gold Fish.tif"
- "/Library/User Pictures/Animals/Jaguar.tif"
- "/Library/User Pictures/Animals/Lion.tif"
- "/Library/User Pictures/Flowers/Tulip.tif"
- "/Library/User Pictures/Fun/Beach Ball.tif"
- "/Library/User Pictures/Fun/Caduceus.tif"
- "/Library/User Pictures/Fun/Chess.tif"
- "/Library/User Pictures/Fun/Cupcake.tif"
- "/Library/User Pictures/Fun/Flippers.tif"
- "/Library/User Pictures/Fun/Gearshift.tif"
- "/Library/User Pictures/Fun/Movie Star.tif"
- "/Library/User Pictures/Fun/Orange.tif"
- "/Library/User Pictures/Fun/Painter's Palette.tif"
- "/Library/User Pictures/Fun/Pizza.tif"
- "/Library/User Pictures/Fun/Robot.tif"
- "/Library/User Pictures/Fun/Rocket.tif"
- "/Library/User Pictures/Nature/Shell.tif"
- "/Library/WebObjects"
- "/System/Library/Assets/"
- "/System/Library/Axis"
- "/System/Library/Extensions/EPSONUSBPrintClass.kext"
- "/System/Library/Extensions/JMicronATA.kext"
- "/System/Library/Frameworks/JavaDTWGeneration.framework"
- "/System/Library/Frameworks/JavaDirectToWeb.framework"
- "/System/Library/Frameworks/JavaEOAccess.framework"
- "/System/Library/Frameworks/JavaEOApplication.framework"
- "/System/Library/Frameworks/JavaEOControl.framework"
- "/System/Library/Frameworks/JavaEODistribution.framework"
- "/System/Library/Frameworks/JavaEOGeneration.framework"
- "/System/Library/Frameworks/JavaEOInterface.framework"
- "/System/Library/Frameworks/JavaEOInterfaceSwing.framework"
- "/System/Library/Frameworks/JavaEOProject.framework"
- "/System/Library/Frameworks/JavaEORuleSystem.framework"
- "/System/Library/Frameworks/JavaEOTool.framework"
- "/System/Library/Frameworks/JavaFoundation.framework"
- "/System/Library/Frameworks/JavaJDBCAdaptor.framework"
- "/System/Library/Frameworks/JavaJNDIAdaptor.framework"
- "/System/Library/Frameworks/JavaWOExtensions.framework"
- "/System/Library/Frameworks/JavaWOJSPServlet.framework"
- "/System/Library/Frameworks/JavaWebObjects.framework"
- "/System/Library/Frameworks/JavaWebServicesClient.framework"
- "/System/Library/Frameworks/JavaWebServicesGeneration.framework"
- "/System/Library/Frameworks/JavaWebServicesSupport.framework"
- "/System/Library/Frameworks/JavaXML.framework"
- "/System/Library/Frameworks/OpenDirectory.framework/odmigrationtool"
- "/System/Library/Java/wojavaclient.jar"
- "/System/Library/PreinstalledAssets/"
- "/System/Library/PreinstalledAssetsV2/"
- "/System/Library/Speech/"
- "/System/Library/WebObjects"
- "/private/etc/authorization"
- "/private/etc/certificates/"
- "/private/etc/csh.cshrc"
- "/private/etc/csh.login"
- "/private/etc/csh.logout"
- "/private/etc/defaultdomain"
- "/private/etc/exports"
- "/private/etc/find.codes"
- "/private/etc/gettytab"
- "/private/etc/openldap/ldap.conf"
- "/private/etc/pam.d/prl_disp_service"
- "/private/etc/paths"
- "/private/etc/pear.conf"
- "/private/etc/profile"
- "/private/etc/shells"
- "/private/var/db/.AccessibilityAPIEnabled"
- "/private/var/db/.TimeMachine.Cookie"
- "/private/var/db/.com.apple.iokit.graphics"
- "/private/var/db/.sp_visible"
- "/private/var/db/KernelExtensionManagement/"
- "/private/var/db/RemoteManagement/"
- "/private/var/db/bluetoothEnabled"
- "/private/var/db/gkopaque.bundle/"
- "/usr/bin/cups-calibrate"
- "/usr/bin/escputil"
- "/usr/bin/kmutil"
- "/usr/lib/libgutenprint.2.0.3.dylib"
- "/usr/libexec/cups/backend/epsonfirewire"
- "/usr/libexec/cups/driver/gutenprint.5.2"
- "/usr/libexec/cups/filter/commandtocanon"
- "/usr/libexec/cups/filter/commandtoepson"
- "/usr/libexec/cups/filter/rastertogutenprint.5.2"
- "/usr/sbin/cups-genppd.5.2"
- "/usr/sbin/cups-genppdupdate"
- "/usr/share/cups/calibrate.ppm"
- "/usr/share/gutenprint/"
- "/usr/share/locale/cs/gutenprint_cs.po"
- "/usr/share/locale/da/gutenprint_da.po"
- "/usr/share/locale/de/gutenprint_de.po"
- "/usr/share/locale/el/gutenprint_el.po"
- "/usr/share/locale/en_GB/gutenprint_en_GB.po"
- "/usr/share/locale/es/gutenprint_es.po"
- "/usr/share/locale/fr/gutenprint_fr.po"
- "/usr/share/locale/hu/gutenprint_hu.po"
- "/usr/share/locale/it/gutenprint_it.po"
- "/usr/share/locale/ja/gutenprint_ja.po"
- "/usr/share/locale/nb/gutenprint_nb.po"
- "/usr/share/locale/nl/gutenprint_nl.po"
- "/usr/share/locale/pl/gutenprint_pl.po"
- "/usr/share/locale/pt/gutenprint_pt.po"
- "/usr/share/locale/sk/gutenprint_sk.po"
- "/usr/share/locale/zh_TW/gutenprint_zh_TW.po"
- "/usr/share/man/man1/escputil.1.gz"
- "/usr/share/man/man8/cups-calibrate.8.gz"
- "/usr/share/man/man8/cups-genppd.5.2.8.gz"
- "/usr/share/man/man8/cups-genppdupdate.8.gz"
- "331BB104B13265802FC130A8AC28927CFF1CC3F0D502D0B0DE25A8D6F87D3528"
- "39D1F9F58B7507EEDA6828720DCA4E2803053FCB527AFCA4933B930B74DDF12C6EEB8075B71AFB6D6C677E"
- "42D0D896FDC8C4BDEEE6071C32EC091C006DF69C1E2EF24E45CC955595A7F25C7954CE04641DB0604AF9C4F1A7BCCA5DEB8C98F63BF9AD3B39D3C1939E71F9772EE2C13242C386EF8EA0BD97F7D9DB04F208D1C8C2959449C6A5D47F34"
- ": %.2fs"
- ": %@"
- ": Incomplete"
- "; %.2f%% of total engine progress"
- "; %.2f%% of total engine progress)"
- "=== Generated SMMigrate Engine (%@) ===\n"
- "@\"NSMutableOrderedSet\""
- "@\"NSObject<SMShoveElementDelegate>\""
- "@\"NSProgress\""
- "@\"SMMigrateEngine\""
- "@\"SMProgressEntry\""
- "@\"SMSystemRuleHandler\""
- "@24@0:8^{sqlite3_stmt=}16"
- "@28@0:8i16@20"
- "@36@0:8i16^{sqlite3_stmt=}20@28"
- "@52@0:8Q16Q24B32B36B40B44B48"
- "AwaitingReboot"
- "B45934C492D902004490F765BF6DBAF70629C86321100A24CB32DD62CAB9AE0E4164B40494A8487F9E79B60102E0C4DB7583A8D70ADD5202DBC0A135F0B3E428B74A4ACECB7A35C32B24F98D"
- "BIGINT"
- "Beginning user home scan in \"%@\""
- "CDE31E0EC933D9E8EA5D91C224D940C384148DE1A9B5A7A00A71390FC6FE6C427E3D6DA2D7CC9073045B74B7DD351C51E448D904C72F674AA63CC4CC9845694092FC95AA5164C7A21ABE42D9E51FE1AE0C46638E2996199791"
- "COPYING_OWNED_COMPONENT"
- "COPYING_SYSTEM_COMPONENT"
- "CREATING_USER"
- "Calculate home dir size of user: %@"
- "Cannot calculate size/count of Engine steps - request [%@]"
- "Cannot calculate size/count of Engine steps - request's source system [%@]"
- "Cannot calculate size/count of Engine steps - request's type [%lu]"
- "Cannot generate Engine steps - request [%@]"
- "Cannot generate Engine steps - request's source system [%@]"
- "Cannot generate Engine steps - request's type [%lu]"
- "Completed"
- "Completed user home scan in \"%@\""
- "Considering Migration of Bundle ID \"%@\" Location \"%@\": "
- "Copy: %@ %@ (%@ - %@)"
- "Copy: %@ %@ (%@) - No Engine Yet"
- "Copy: %@ -> %@ (%@ - %@)"
- "Copy: %@ -> %@ (%@) - No Engine Yet"
- "Could not create user record"
- "Couldn't find/initialize current system!!"
- "Creating very first disk of type [SKDiskBased] with mountpoint [/]"
- "Customer build: opening %@."
- "Detected %lu incompatible software paths"
- "Detected %lu out-of-band update files"
- "Detected Platform Binary in Sandbox (Old Network source?). Removing %@"
- "Detected user may have force-shutdown the machine."
- "Determining user's home directory: %@"
- "Done rebuilding KMU Cache!"
- "ERROR : Couldn't create `%@' (%@) : `%@'"
- "ERROR: %@\n%@"
- "ERROR: Shove soft errors reported: Contents - [%@]"
- "Element: %@"
- "Engine %@ during preprocess. Restarting Preprocess..."
- "Engine Startup: APFS Data and System Mounted: %d"
- "Engine Startup: Assigning the migration request's source system to nil since its not mounted."
- "Engine Startup: Match for source system has a paired data volume but it's not unlocked/mounted. Ignoring source..."
- "Engine Startup: Match for source system has appeared."
- "Engine Startup: Match for source system has disappeared."
- "Engine Startup: Match for target system has appeared."
- "Engine Startup: Match for target system has disappeared."
- "Engine Startup: Target system has a paired data volume but it's not unlocked/mounted. Ignoring target..."
- "Engine is done with current request"
- "Engine is waiting for pathing, filesystem will be classified."
- "Engine source disappeared in %@ phase of step %@. Restarting step..."
- "Engine steps generated in order:\n"
- "Engine was suspended in %@ phase of step %@. Restarting step..."
- "Engine: Startup: Current request is done. Awaiting acknowldgement from client."
- "Engine: Startup: Current request requires a reboot before continuing."
- "Engine: Startup: Desired Source LTID: %@"
- "Engine: Startup: Desired Target LTID: %@"
- "Engine: Startup: Entering post-reboot phase."
- "Engine: Startup: Source and Target systems are now available."
- "Engine: Startup: Source system is not be mounted when we entered [... systemsAreAvailable]."
- "Engine: Startup: Using current system at / as target for post reboot phase."
- "Engine: Startup: Using current system at / to standin for empty target."
- "Engine: Startup: Waiting for source and target systems to be available."
- "Error copying %@ to %@: %@"
- "Error deferring copy of %@ to %@"
- "Error determining preliminary UIDs!, %@"
- "Errors reported during the %@ stage of step %@: %@"
- "Errors reported during the preparing stage of step %@: %@"
- "Estimated %f seconds to complete; %f seconds remaining"
- "Exception thrown during %@"
- "Exception thrown during %@ phase of step %@ - %@:%@"
- "Exception thrown during prepare stage of step %@ - %@:%@"
- "Exception thrown during preparing"
- "FILES_COPYING_FROM_APP_FOLDER"
- "FILES_COPYING_FROM_PRINTER_FOLDER"
- "FILES_COPYING_FROM_SYSTEM"
- "FILES_PREPARE_FINDING_SYS_DOCS"
- "Failed rebuilding KMU Cache!"
- "Failed to commit user creation changes."
- "Failed to defer copy %@ to %@"
- "Failed to execute query: %@. Error code: %d, Error message: %s"
- "Failed to grant newly created user SecureToken."
- "Failed to obtain OD node."
- "Failed to process user home in \"%@\": %@"
- "Failed to switch to Soft-AP"
- "Failed to verify the user's password"
- "Fatal Node Operation Error"
- "Final progress updated:\n%@"
- "Finding system receipts at %@"
- "Firmlinks: Loaded %lu firmlinks"
- "Firmlinks: Loading firmlink manifest"
- "Firmlinks: Manifest found at: %@"
- "Found %lu Firmlinked paths"
- "HH:mm:ss"
- "IMPORTING_USER_DATA"
- "INTEGER"
- "Ignoring empty progress string reported from %@"
- "Increasing time estimate decrease; migration is proceeding faster (%.2f seconds)"
- "Internal build: opening %@."
- "Invalid Phase"
- "KnownChecksums"
- "LLL dd HH:mm:ss"
- "MA/MB"
- "MIG_BLACK_LIST: (ERROR) -> Can't read %@, black list is disabled...."
- "MIG_BLACK_LIST: (WARN) -> Path set more than once %@"
- "MIG_BLACK_LIST: (WARN) -> Useless dictionary with no path set ! %@"
- "Migrate Engine Cleanup"
- "Migrate Files process: Starting running of copy engine"
- "Migrate SystemInfo process: Starting running of copy engine"
- "Migrate engine failed during processing."
- "Migrate engine was stopped because pre-processing failed."
- "Migrate engine was stopped before pre-processing."
- "Migrate engine: Stopping"
- "Migrate engine: Suspending"
- "Migrating due to multiple bundles existing with this ID on the local system"
- "Migrating since no bundle exists at that local path."
- "Migrating since no local bundle with this ID exists."
- "Migration Report:\n\n"
- "Migration copied %2.2f MB of %2.2f MB at a rate of %2.2f MB/s overall"
- "Migration element %@ failed: %@"
- "Migration progress surpassed %lld."
- "Migration took %f seconds long (original estimation: %f seconds)."
- "Missing essential set of receipts!"
- "No action (id=%ld)"
- "No activities.\n"
- "No database file found."
- "No notes.\n"
- "Node Operation failed with %d."
- "Non-Fatal BOM Error"
- "Not Shoving Sandbox because it was deleted: %@"
- "Notified user Spotlight was slow"
- "Pather cannot be initialized with undefined Request Type!"
- "Pather: Detected non-regular file, avoiding: \"%@\""
- "Pather: Platform Binary detected on source, treating as system file: \"%@\""
- "Pathing Report: %@"
- "Plist is empty."
- "Plist is missing."
- "PostReboot"
- "Pre-Process"
- "Pre-Shove"
- "Pre-processing"
- "Prefetched data on %lu system files"
- "Preparing"
- "Progress info: Copier progress added [Expected: 100 - (4 | 25, 25, 25, 20)]: \n%@"
- "Progress info: Copier progress finish confirmed: \n%@"
- "Progress info: Copier progress updated: \n%@"
- "Progress info: Copy Engine progress added [Expected: %ld - (%lu | 1 unit each)]: \n%@"
- "Progress info: Copy Engine progress added [Expected: 100 - (%lu | %@)]: \n%@"
- "Progress info: Copy Engine progress finish confirmed:\n%@"
- "Progress info: Copy Engine progress updated:\n%@"
- "Progress info: Engine elements-run progress added [Expected: %ld - (%lu | %@)]: \n%@"
- "Progress info: Engine elements-run progress finish confirmed: \n%@"
- "Progress info: Engine elements-run progress updated (last element run- %@): \n%@"
- "Progress info: Engine prepare progress added [Expected: %lu - (%lu | 1 unit each)]: \n%@"
- "Progress info: Engine prepare progress finish confirmed: \n%@"
- "Progress info: Engine prepare progress updated: \n%@"
- "Progress info: Engine progress: final complete comfirmed: \n%@"
- "Progress info: Engine progress: prepare complete comfirmed: \n%@"
- "Progress info: Engine progress: processing complete comfirmed: \n%@"
- "Progress info: Engine progress: total units set: \n%@"
- "Progress info: MigrateFiles postprocess progress added [Expected: 3 - (3 | 1 unit each)]: \n%@"
- "Progress info: MigrateFiles postprocess progress finish confirmed: \n%@"
- "Progress info: MigrateFiles postprocess progress updated: \n%@"
- "Progress info: Step (phase: %@) progress added [Expected: 100 - (%lu | %@)]: \n%@"
- "Progress info: Step (phase: %@) progress finish confirmed: \n%@"
- "Progress info: Step (phase: %@) progress updated: \n%@"
- "Progress info: SystemInfo postprocess progress added [Expected: 5 - (5 | 1 unit each)]: \n%@"
- "Progress info: SystemInfo postprocess progress finish confirmed: \n%@"
- "Progress info: SystemInfo postprocess progress updated: \n%@"
- "Progress info: SystemInfo postprocess: Copy machine settings finish confirmed: \n%@"
- "Progress info: SystemInfo postprocess: Copy machine settings progress added [Expected: 3 - (3 | 1 unit each)]: \n%@"
- "Progress info: SystemInfo postprocess: Copy machine settings progress added [Expected: 9 - (9 | 1 unit each)]: \n%@"
- "Progress info: SystemInfo postprocess: Copy machine settings updated: \n%@"
- "Progress info: SystemInfo postprocess: Copy network settings progress added [Expected: 2 - (2 | 1 unit each)]: \n%@"
- "Progress info: SystemInfo postprocess: Copy network settings progress finish confirmed: \n%@"
- "Progress info: SystemInfo postprocess: Copy network settings progress updated: \n%@"
- "ProgressReport%@.csv"
- "Q24@0:8^Q16"
- "Rebuilding KMU Cache..."
- "Receipt failure: Filesystem is not active or has no root!"
- "Reclaim Purgable Space"
- "Rosetta Status: Found Rosetta receipt (%@), classifying as System content."
- "Rosetta Status: Found Rosetta receipt (%@), classifying as User content."
- "Rule destination changed due to SIP Check; possibly malicious symlink? (%@ -> %@)"
- "Rule destination restored because it is allowed. path=%@"
- "Rule rejected by handler."
- "SELECT * FROM rule"
- "SELECT * FROM rule WHERE id = %ld"
- "SELECT * FROM rule WHERE ruleGroup = \"%@\""
- "SELECT checksum FROM fileChecksum WHERE filePath = '%@'"
- "SMCommitDeferredSandboxElement"
- "SMConfMigratorAllowlist"
- "SMConfMigratorBundle"
- "SMConfMigratorCopyRule"
- "SMConfMigratorRules"
- "SMConfMigratorRunToolRule"
- "SMConfMigratorUserPathRule"
- "SMCopyEngineNopCopier: (Shove Log): %@"
- "SMCopyEngineNopCopier: Copying (Unable to determine source relative path): %@"
- "SMCopyEngineNopCopier: Error %ld while copying %@ -> %@ (%@)"
- "SMCopyEngineNopCopier: Failed to create the final destination (%@). %@"
- "SMCopyEngineNopCopier: Failed to delete destination sandbox. %@"
- "SMCopyEngineNopCopier: Failed to get attributes of the source path. (%@). %@"
- "SMCopyEngineNopCopier: Failed to set source attributes onto the final destination (%@). %@"
- "SMCopyEngineNopCopier: Please File a Bug: Failed to gather path relative to mountpoint for source %@."
- "SMCopyEngineNopCopier: Please File a Bug: Source does not exist %@ -> %@"
- "SMCopyEngineNopCopier: Please File a Bug: couldn't construct URL for %@"
- "SMCopyEngineNopCopier: Please File a Bug: source or Destination not specified %@ -> %@"
- "SMCopyEngineNopCopier: Recopying (Partially Copied from Failed List): %@"
- "SMCopyEngineNopCopier: Recopying (Partially Copied): %@"
- "SMCopyEngineNopCopier: Root privilege when performing a backup or migrate operation."
- "SMCopyEngineNopCopier: Shove exited non-zero. Exit Status:%d"
- "SMCopyEngineNopCopier: Skipping (Already Copied): %@"
- "SMCopyEngineNopCopier: Source is a file and stat'ing it failed. (%@). %s"
- "SMCopyEngineNopCopier: The destination is a file in folder copying mode, we tried deleting it but failed. (%@). %@"
- "SMCopyEngineNopCopier: The destination sandbox already exists and we were unable to delete it (%@). %@"
- "SMMigrateEngine"
- "SMMigrateEngine(EnsureSourceMounted): Source is mounted but its data/system pair not both mounted."
- "SMMigrateEngineErrorDomain"
- "SMMigrateFiles"
- "SMMigrateGroups"
- "SMMigrateSystemInfo"
- "SMMigrateUserDataStep"
- "SMMigrationActivity"
- "SMMigrationEngineElement"
- "SMMigrationEngineProtocol"
- "SMMigrationEngineStep"
- "SMMigrationIncompatibleApplicationsList"
- "SMMigrationKernelManagementUtilityElement"
- "SMMigrationReport"
- "SMMigrationShoveElement"
- "SMMigrationStepElement"
- "SMMigrationStepElementError"
- "SMMigrationUpdateKextCacheElement"
- "SMProgressEntry"
- "SMReportNote"
- "SMSystemRuleClient"
- "SMSystemRuleHandler"
- "SM_bundleIsPlatformBinary"
- "SYSTEMINFO_MIGRATE_NETCFG"
- "SYSTEMINFO_MIGRATE_SYSPREFS"
- "SYSTEMINFO_MIGRATE_TIMEZONE"
- "SYSTEMINFO_UPDATE_SYSPREFS"
- "Sandbox Shove Failed"
- "Shove failed and we retrieved the error, but it had no list of failed files"
- "Shove failed but we failed to retrieve the error"
- "Shoving Sandbox %@ -> %@."
- "Skipping because local resource is not a bundle."
- "Skipping due to App Store receipt in local bundle."
- "Slowing down time estimate decrease; migration is proceeding slower (%.2f seconds)"
- "Smoothed Time Estimate to %.2f seconds from raw %.2f seconds (extra time %.2f seconds)"
- "Sorting"
- "Source System:\n%@\nTarget System:\n%@\n"
- "Starting Migration With Request : %@"
- "Starting running of copier #%llu"
- "Starting running of element %d: %@"
- "Starting running of step %d: %@ (Phase: %@)"
- "Step: %@ (Phase: %@)"
- "Successfully authenticated admin"
- "Successfully created IA user + home directory: %@"
- "Successfully created IA user but not home directory: %@"
- "Successfully created IA user: %@"
- "Synthetic Symlinks: Loaded %lu directories"
- "Synthetic Symlinks: Loaded %lu symlinks"
- "Synthetic Symlinks: Manifest found at: %@"
- "System Defense: %@ -> Root? %@. Direct DV Enumeration? %@."
- "System Defense: Cannot target read-only location %@"
- "System Defense: Could not find a disk for path (possibly a broken symlink?) %@"
- "System Defense: Given targetDisk: %@ Role: %@"
- "System Defense: Hole-punching System Defense due to System Integrity Protection override for %@"
- "System Defense: Hole-punching System Integrity Protection due to Migration Data override for %@"
- "System Defense: Hole-punching System Integrity Protection during Upgrade or Update for %@"
- "System Defense: Initially redirected Root-destined path to Data Volume root: %@ -> %@"
- "System Defense: ROSV Permission denied. Input path: (%@) After Redirections path: (%@) Full Intended path: (%@), Symlink Expanded: (%@), Target System: (%@), TSFS Type: (%@), TS Root: (%@)"
- "System Defense: Redirecting read-only target %@ to %@"
- "System Defense: rootless_preflight rejected path: %@"
- "T@\"NSArray\",W,V_steps"
- "T@\"NSDate\",&,V_date"
- "T@\"NSDate\",&,V_endDate"
- "T@\"NSDate\",&,V_lastProgressLog"
- "T@\"NSDate\",&,V_lastProgressUpdate"
- "T@\"NSDate\",&,V_lastTimeRemainingUpdate"
- "T@\"NSDate\",&,V_startDate"
- "T@\"NSLock\",&,V_progressUpdateLock"
- "T@\"NSMutableArray\",&,V_childActivities"
- "T@\"NSMutableArray\",&,V_engineElements"
- "T@\"NSMutableArray\",&,V_migrationElementsProgressPercentage"
- "T@\"NSMutableArray\",&,V_progressEntries"
- "T@\"NSMutableArray\",&,VdatesSeen"
- "T@\"NSMutableDictionary\",&,V_notes"
- "T@\"NSMutableDictionary\",&,V_progressPercentages"
- "T@\"NSMutableOrderedSet\",&,V_activities"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_activityQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_childActivitiesQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_noteQueue"
- "T@\"NSObject<SMShoveElementDelegate>\",W,V_delegate"
- "T@\"NSProgress\",&,V_absoluteParentProgress"
- "T@\"NSProgress\",&,V_parentProgress"
- "T@\"NSProgress\",&,V_progress"
- "T@\"NSString\",&,V_detail"
- "T@\"NSString\",&,V_progressString"
- "T@\"NSString\",R,Vnote"
- "T@\"SMMigrateEngine\",&,V_engine"
- "T@\"SMMigrateEngine\",W,V_engine"
- "T@\"SMMigrateEngine\",W,Vengine"
- "T@\"SMProgressEntry\",&,V_lastProgressEntry"
- "T@\"SMSystemRuleHandler\",&,N,V_systemRuleHandler"
- "TB,V_hasRan"
- "TB,V_recordedOneMinuteRemainingTime"
- "TB,V_reportTimeRemaining"
- "TEXT"
- "TQ,V_phase"
- "TQ,V_stepFinishedBytes"
- "TQ,Vcount"
- "Td,V_estimatedDuration"
- "Td,V_estimatedTotalTime"
- "Td,V_extraTimeRemaining"
- "Td,V_initialTimeEstimate"
- "Td,V_lastProgressPercentComplete"
- "Td,V_lastReportedTimeRemaining"
- "Td,V_lastReportedTransferRate"
- "Td,V_oneMinuteRemainingTime"
- "Td,V_parentProgressPendingUnits"
- "Td,V_percentComplete"
- "Td,V_progressPercentage"
- "Td,V_timeRemaining"
- "The %@ while running element %d: %@. Restarting element..."
- "The %@ while running element %d: %@. The element supports resuming. Resuming element..."
- "Time Estimate Difference: %.2f seconds vs Actual Time Difference: %.2f seconds"
- "Time estimate jumped to longer time estimate"
- "Time estimate jumped to shorter time estimate"
- "Time since reporting one minute remaining: %f"
- "Time, Percent Complete, Time Remaining (seconds), Transfer Rate (bytes per second)\n"
- "Total Size %2.2f MB\n\n"
- "Total Time: %.2fs\n"
- "Traditional"
- "Transfer rate from transfer rate history is not positive!"
- "UID/GID translation table: %@"
- "USERINFO_COPYING_USER_DATA"
- "USERINFO_PREPARE_MIGRATE_USERS"
- "USERINFO_PREPARE_USER_COPIES"
- "UUID: %@\n"
- "Unable to set progress percentage for unknown phase."
- "Unsuccessful in authenticating admin (New user will be created, but not home directory)"
- "Unsuccessful in authenticating admin (New user will be created, but not home directory): %@"
- "V %@: DSDB found."
- "V (vlb) Valid Light Backup"
- "WAITING_FOR_SPOTLIGHT"
- "WARNING : ensureParentPathExists: Created  `%@' w/ %@"
- "Windows Migrate Files process: Starting running of copy engine"
- "WindowsMigrateComponent process: Starting running of copy engine"
- "X %@: Case Sensitive filesystem, while / is not."
- "X %@: CoreStorage Booter."
- "X %@: Missing SystemVersion.plist"
- "X %@: Missing template receipt data"
- "X %@: No DirectoryServices database."
- "X %@: Not Case Sensitive filesystem, while / is."
- "X %@: Server installation."
- "X %@: System appears to be install media. Found these paths: %@"
- "X %@: System appears to be install partition."
- "X %@: The system appears to be damaged, since no local user database was found!"
- "X (vlb) has system version %@"
- "X (vlb) missing dslocal %@"
- "X Source too new: Source version: %@, Destination version: %@.%@"
- "X Source too old: Source version: %@"
- "[REJECT]: Rule applies for any servers but the source is none of the following: self-contained server, legacy server, mixed legacy."
- "[REJECT]: Rule applies for installs but the current request is not an upgrade."
- "[REJECT]: Rule applies for legacy servers but the source request is not a legacy server."
- "[REJECT]: Rule applies for migrations but the current request is an upgrade/update."
- "[REJECT]: Rule applies for mixed legacy servers but the source request is neither a legacy nor a mixed legacy server."
- "[REJECT]: Rule applies for modern servers but the source is neither a self-contained nor a mixed legacy server."
- "[REJECT]: Rule applies for updates but the current request is not an update."
- "[REJECT]: Rule can only run after %@, sourceVersion is %@"
- "[REJECT]: Rule can only run before %@, sourceVersion is %@"
- "[REJECT]: Rule is to be skipped in legacy server installs."
- "[REJECT]: Rule only runs post-reboot but request state is in pre-reboot."
- "[REJECT]: Rule only runs pre-reboot but request state is in post-reboot."
- "[REJECT]: Unknown rule context."
- "_absoluteParentProgress"
- "_activities"
- "_activityQueue"
- "_childActivities"
- "_childActivitiesQueue"
- "_date"
- "_detail"
- "_endDate"
- "_engineElements"
- "_estimatedDuration"
- "_estimatedTotalTime"
- "_extraTimeRemaining"
- "_findNextNumberAbove:inSet:"
- "_hasRan"
- "_initialTimeEstimate"
- "_lastProgressEntry"
- "_lastProgressLog"
- "_lastProgressPercentComplete"
- "_lastReportedTimeRemaining"
- "_lastReportedTransferRate"
- "_lastTimeRemainingUpdate"
- "_migrationElementsProgressPercentage"
- "_noteQueue"
- "_notes"
- "_oneMinuteRemainingTime"
- "_parentProgress"
- "_parentProgressPendingUnits"
- "_percentComplete"
- "_phase"
- "_progress"
- "_progressEntries"
- "_progressPercentage"
- "_progressPercentages"
- "_progressString"
- "_progressUpdateLock"
- "_recordedOneMinuteRemainingTime"
- "_reportTimeRemaining"
- "_startDate"
- "_stepFinishedBytes"
- "_steps"
- "_systemRuleHandler"
- "_timeRemaining"
- "absoluteParentProgress"
- "activities"
- "activityLength"
- "activityQueue"
- "addActivity:"
- "addBundle:atLocation:withStats:"
- "addChild:withPendingUnitCount:"
- "addChildActivity:"
- "addElement:"
- "allowlist"
- "app"
- "applicationGroupBundlesToLocalizeFromPather:"
- "argument"
- "bundleComponentVersion:"
- "calculateProgressPercentages:"
- "checksum"
- "childActivities"
- "childActivitiesQueue"
- "com.apple.installandsetup.progressreport.activity.complex"
- "com.apple.installandsetup.report.activity"
- "com.apple.installandsetup.report.note"
- "com.apple.installandsetup.report.progress"
- "com.apple.installandsetup.systemmigration.activity"
- "completedFilesWereShoved"
- "completedUnitCount"
- "d24@0:8Q16"
- "d24@0:8d16"
- "datesSeen"
- "defaultHomeDirectory"
- "deferCopyPath:sourceSystem:targetSystme:"
- "detail"
- "dictionaryFromStatement:"
- "did check a bundle version. current_bundle=%@, current_version=%@ newer_bundle=%@, newer_version=%@"
- "did determine whether app bundle path exists or not. path=%@"
- "did determine whether it will overwrite or not. overwrite=%d, path=%@"
- "did skip a bundle because a newer version is already installed. path=%@"
- "diskImagesInDirectory:error:"
- "elementSupportsResuming"
- "elementsShouldContinue"
- "endDate"
- "engineElements"
- "estimateTimeRemaining"
- "estimatedDuration"
- "estimatedTimeRemainingAfterPhase:"
- "estimatedTimeRemainingForPhase:"
- "estimatedTimeToComplete"
- "estimatedTimeToCompletePhase:"
- "estimatedTotalTime"
- "executeQuery:"
- "extraTimeRemaining"
- "fileHandleForWritingToURL:error:"
- "finalSizeAndCountForMigrationRequest:"
- "finish"
- "generateAppsFileStep:"
- "generateAutoLoginUserStep:"
- "generateDestinationPath:"
- "generateEngineElements"
- "generateEngineSteps"
- "generateEnterpriseMigrateFilesStep:"
- "generateMachineSettingsStep:shouldSetOnlyUpdateSystemSettings:"
- "generateMachineSettingsStep:withMacPathMap:"
- "generateMigrateGuestAccountStep:"
- "generatePeerToPeerStep:"
- "generateStepsForEngine:withRequestType:mustGenerateUserStep:mustGenerateEnterpriseFilesStep:mustGenerateMachineSettingsStep:mustGenerateGuestStep:mustGenerateAppsFileStep:"
- "generateUsersStep:"
- "generateUsersStep:withMacPathMap:"
- "getAllRules"
- "getRuleByID:"
- "hasExcludedPaths"
- "hasFinished"
- "hasRan"
- "hasStarted"
- "homeDirectory"
- "iaList"
- "increment"
- "initWithAllowlistPath:"
- "initWithEngine:steps:phase:"
- "initWithMessage:"
- "initWithName:"
- "initWithName:detail:"
- "initWithParent:userInfo:"
- "initWithPath:arguments:runsAfterRestart:"
- "initWithPathMap:"
- "initialTimeEstimate"
- "isAllowed:"
- "isApplicableRuleContext:"
- "isBundle:"
- "isCopyRuleApplicable:"
- "isCopyableBecauseDestinationDoesNotExist:"
- "isNewerBundle:thanBundle:"
- "lastProgressEntry"
- "lastProgressLog"
- "lastProgressPercentComplete"
- "lastReportedTimeRemaining"
- "lastReportedTransferRate"
- "lastTimeRemainingUpdate"
- "loadPlist:"
- "local resource is a bundle"
- "local resource is not a bundle"
- "localizeFoldersForApplications"
- "localizeParentFolderForBundleWithURL:"
- "lookupProcessIdentifierByName:"
- "migrate"
- "migrateAllSettingsWithGroupName2:"
- "migrateProgressKey:arguments:forMigrateStep:"
- "migrateProgressString:forMigrateStep:"
- "migrateWithRule2:"
- "migrationElementsProgressPercentage"
- "no local bundle exists"
- "note"
- "note:"
- "noteQueue"
- "notes"
- "oneMinuteRemainingTime"
- "parentProgress"
- "parentProgressPendingUnits"
- "phase"
- "phaseNameForPhase:"
- "platformBinaryExceptions"
- "preProcess"
- "preShove"
- "prepareIncompatibleApplicationsList:forSMSystem:"
- "prettyPrintEngineSteps"
- "progress"
- "progressEntries"
- "progressPercentage"
- "progressPercentageForPhase:"
- "progressPercentages"
- "progressString"
- "progressUpdateLock"
- "progressWithTotalUnitCount:"
- "recordProgressPercentComplete:timeRemaining:transferRate:"
- "recordedOneMinuteRemainingTime"
- "reportProgress"
- "reportTimeRemaining"
- "rules"
- "runOpenDirectoryMigrationTool"
- "runStepPrepare"
- "saveProgressReport:"
- "setAbsoluteParentProgress:"
- "setActivities:"
- "setActivityQueue:"
- "setChildActivities:"
- "setChildActivitiesQueue:"
- "setCompletedUnitCount:"
- "setDate:"
- "setDatesSeen:"
- "setDetail:"
- "setEndDate:"
- "setEngineElements:"
- "setEstimatedDuration:"
- "setEstimatedTimeToComplete:"
- "setEstimatedTotalTime:"
- "setExtraTimeRemaining:"
- "setHasRan:"
- "setHint:"
- "setInitialTimeEstimate:"
- "setLastProgressEntry:"
- "setLastProgressLog:"
- "setLastProgressPercentComplete:"
- "setLastReportedTimeRemaining:"
- "setLastReportedTransferRate:"
- "setLastTimeRemainingUpdate:"
- "setMigrationElementsProgressPercentage:"
- "setNoteQueue:"
- "setNotes:"
- "setOneMinuteRemainingTime:"
- "setParentProgress:"
- "setParentProgressPendingUnits:"
- "setParentProgressQueue:"
- "setPercentComplete:"
- "setPhase:"
- "setProgress:"
- "setProgressEntries:"
- "setProgressPercentage:"
- "setProgressPercentage:forPhase:"
- "setProgressPercentages:"
- "setProgressPortionsForStep:"
- "setProgressString:"
- "setProgressUpdateLock:"
- "setRecordedOneMinuteRemainingTime:"
- "setReportTimeRemaining:"
- "setStartDate:"
- "setStepFinishedBytes:"
- "setSteps:"
- "setSystemRuleHandler:"
- "setTotalUnitCount:"
- "sharedClient"
- "sharedReport"
- "shoveCompletedSuccessfully"
- "shoveFailed"
- "shoveSandboxAtPath:sandBoxPath:error:"
- "smoothTimeRemaining:"
- "sortUsingSelector:"
- "source disappeared"
- "source was suspended"
- "startDate"
- "stepErrorWithException:"
- "stepFinishedBytes"
- "steps"
- "synchronizeFile"
- "systemRootPath"
- "systemRuleHandler"
- "timeIntervalSinceDate:"
- "timeRemaining"
- "timeRemainingChangedForStep:"
- "totalUnitCount"
- "transferRateChanged:forStep:"
- "tryLock"
- "updateEngineForEngineSteps"
- "updateTimeRemaining"
- "updateTransferRate:"
- "v24@0:8@\"SMMigrationEngineStep\"16"
- "v28@0:8^@16B24"
- "v32@0:8@\"NSString\"16@\"SMMigrationEngineStep\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8^@16@24"
- "v32@0:8d16@\"SMMigrationEngineStep\"24"
- "v32@0:8d16Q24"
- "v40@0:8@\"NSString\"16@\"NSArray\"24@\"SMMigrationEngineStep\"32"
- "v40@0:8d16d24d32"
- "valueForColumnAtIndex:statement:type:"
- "verifyAndCreateIAUserWithPassword:"
- "verifyAndCreateIAUserWithPassword:andReplyBlock:"
- "was suspended"
- "will check app bundle. path=%@"

```
