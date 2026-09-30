## LaunchServices

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/LaunchServices`

```diff

-1367.407.0.0.0
-  __TEXT.__text: 0x21d69c
-  __TEXT.__auth_stubs: 0x3ee0
-  __TEXT.__objc_methlist: 0xbf68
-  __TEXT.__const: 0x9e0
-  __TEXT.__cstring: 0x27d05
-  __TEXT.__oslogstring: 0x1c1dd
-  __TEXT.__gcc_except_tab: 0x2ec04
+1378.16.0.0.0
+  __TEXT.__text: 0x223f10
+  __TEXT.__auth_stubs: 0x3f00
+  __TEXT.__objc_methlist: 0xd11c
+  __TEXT.__const: 0x9f0
+  __TEXT.__cstring: 0x284e9
+  __TEXT.__oslogstring: 0x1c8cc
+  __TEXT.__gcc_except_tab: 0x2f6c8
   __TEXT.__ustring: 0x1be
   __TEXT.__dof_LSFSNode: 0x2b6
-  __TEXT.__unwind_info: 0xc188
-  __TEXT.__eh_frame: 0xc0
-  __TEXT.__objc_classname: 0x1d8b
-  __TEXT.__objc_methname: 0x1d269
-  __TEXT.__objc_methtype: 0xa1ee
-  __TEXT.__objc_stubs: 0x10120
-  __DATA_CONST.__got: 0xcd0
+  __TEXT.__unwind_info: 0xc5d8
+  __TEXT.__eh_frame: 0x60
+  __TEXT.__objc_classname: 0x1e06
+  __TEXT.__objc_methname: 0x1d891
+  __TEXT.__objc_methtype: 0xa42e
+  __TEXT.__objc_stubs: 0x10380
+  __DATA_CONST.__got: 0xcc0
   __DATA_CONST.__const: 0x3960
-  __DATA_CONST.__objc_classlist: 0x638
+  __DATA_CONST.__objc_classlist: 0x660
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6248
+  __DATA_CONST.__objc_selrefs: 0x63b8
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x4f0
+  __DATA_CONST.__objc_superrefs: 0x518
   __DATA_CONST.__objc_arraydata: 0x230
-  __AUTH_CONST.__auth_got: 0x1f88
-  __AUTH_CONST.__const: 0x9678
-  __AUTH_CONST.__cfstring: 0x1b860
-  __AUTH_CONST.__objc_const: 0x14bc0
+  __AUTH_CONST.__auth_got: 0x1f98
+  __AUTH_CONST.__const: 0x9968
+  __AUTH_CONST.__cfstring: 0x1b960
+  __AUTH_CONST.__objc_const: 0x13518
   __AUTH_CONST.__objc_intobj: 0x738
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH.__objc_data: 0x2f80
-  __AUTH.__data: 0x258
-  __DATA.__objc_ivar: 0xa90
-  __DATA.__data: 0x1478
+  __AUTH.__objc_data: 0x3110
+  __AUTH.__data: 0x260
+  __DATA.__objc_ivar: 0xacc
+  __DATA.__data: 0x14d8
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x1e10
+  __DATA.__bss: 0x2170
   __DATA.__common: 0xd
   __DATA_DIRTY.__objc_data: 0xeb0
-  __DATA_DIRTY.__data: 0x170
-  __DATA_DIRTY.__bss: 0x658
+  __DATA_DIRTY.__data: 0x110
+  __DATA_DIRTY.__bss: 0x340
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/CarbonCore.framework/Versions/A/CarbonCore

   - /usr/lib/liboah.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 0BD79215-03E1-3D88-8104-97D48BF358AF
-  Functions: 9372
-  Symbols:   21109
-  CStrings:  15762
+  UUID: 93F3AC96-ABA4-38B3-8DDF-3DF600D8606B
+  Functions: 9777
+  Symbols:   21680
+  CStrings:  15879
 
Symbols:
+ +[FSMimic basePropertyClasses].cold.1
+ +[FSMimic resourceValueClassesWithNull].cold.1
+ +[FSNode looksLikeTrashFolderName:].cold.1
+ +[FSNode prebootVolumeNode].cold.1
+ +[FSNode rootVolumeNode].cold.1
+ +[FSNode(BookmarkData) bookmarkDataPropertiesToInclude].cold.1
+ +[FSNode(InternetLocatorFiles) validURLSchemesForInternetLocatorFileExtension:].cold.1
+ +[FSNode(ResourceFork) openResourceFilesMap].cold.1
+ +[LSAppLink(Internal) _dispatchQueue].cold.1
+ +[LSApplicationRecord(AlternateIcons) _alternateIconQueue].cold.1
+ +[LSApplicationRestrictionsManager sharedInstance].cold.1
+ +[LSApplicationWorkspace _remoteObserver].cold.1
+ +[LSApplicationWorkspace callbackQueue].cold.1
+ +[LSApplicationWorkspace(DefaultApps) _defaultAppQueue].cold.1
+ +[LSBundleRecord _bundleRecordForAuditToken:checkNSBundleMainBundle:error:].cold.1
+ +[LSBundleRecord _bundleRecordForAuditToken:checkNSBundleMainBundle:error:].cold.2
+ +[LSBundleRecord(Redaction) redactedProperties].cold.1
+ +[LSCodeEvaluationClientManager sharedManager].cold.1
+ +[LSDBExecutionContext sharedServerInstance].cold.1
+ +[LSDPluginManager sharedInstance].cold.1
+ +[LSDatabaseBuilder searchPathsForDomain:].cold.1
+ +[LSDatabaseContext sharedDatabaseContext].cold.1
+ +[LSEligibilityPredicateEvaluator(LSInternalCachingEvaluator) sharedCachingEligibilityPredicateEvaluator].cold.1
+ +[LSFeatureFlagPredicateEvaluator defaultEvaluator].cold.1
+ +[LSIconResource _resourceForType:].cold.2
+ +[LSIconResource _resourceForURL:].cold.2
+ +[LSIconResource(LSBinding) _isNetBoot].cold.1
+ +[LSIconResource(LSBinding) _kextInfoURLResourcePropertyKeys].cold.1
+ +[LSIconResource(LSBinding) _resourceWithURL:context:].cold.2
+ +[LSIconResource(LSBinding) _volumeURLResourcePropertyKeys].cold.1
+ +[LSPrecondition emptyPrecondition].cold.1
+ +[LSSettingsStore sharedInstance].cold.1
+ +[NSFileManager(LaunchServicesAdditions) _LS_frameworkFileManager].cold.1
+ +[_LSApplicationProxyForIdentifierQuery alwaysAllowedBundleIdentifiers].cold.1
+ +[_LSDDeviceIdentifierService getBaseSecretCommonQueryDictionary].cold.1
+ +[_LSDDisseminationClientImplementation sharedInstance].cold.1
+ +[_LSDModifyService dispatchQueue].cold.1
+ +[_LSDServiceDomain defaultServiceDomain].cold.1
+ +[_LSDServiceDomain systemSessionDomain].cold.1
+ +[_LSDTrustedSignatureService dispatchQueue].cold.1
+ +[_LSDefaultFeatureFlagResolver sharedInstance].cold.1
+ +[_LSDefaults sharedInstance].cold.1
+ +[_LSDiskUsage(Internal) _serverQueue].cold.1
+ +[_LSDiskUsage(Private) propertyQueue].cold.1
+ +[_LSDisplayNameConstructor(ExtensionHiding) showAllExtensions].cold.1
+ +[_LSEmptyPropertyList sharedInstance].cold.1
+ +[_LSExceptions allowInternallyBlockedApps].cold.1
+ +[_LSExceptions initialize].cold.1
+ +[_LSPersonaDatabase sharedInstance].cold.1
+ +[_LSQueryContext defaultContext].cold.1
+ +[_LSRemoteOpenCall canInvokeLocally].cold.1
+ +[_LSRemoteOpenCall canInvokeLocally].cold.2
+ +[_LSRemoteOpenCall canInvokeLocally].cold.3
+ +[_LSRemoteOpenCall canInvokeRemotely].cold.1
+ +[_LSStringLocalizer coreTypesLocalizer].cold.1
+ +[_LSStringLocalizer missingLocalizationPlaceholder].cold.1
+ +[_LSStringsFileContent IOQueue].cold.1
+ +[_LSTemplateApplication frameworkVersionForDataVaultVersion].cold.1
+ +[_LSTemplateApplicationActionsManagerListener sharedListener].cold.1
+ +[_LSTrustedSignature(Private) secret].cold.1
+ -[FSNode clearURLPropertyCacheIfStale].cold.1
+ -[FSNode copyWithZone:].cold.1
+ -[FSNode getHFSType:creator:error:].cold.1
+ -[FSNode initWithURL:flags:error:].cold.1
+ -[FSNode(InternetLocatorFiles) internetLocatorTypeInfoForExtension:fileType:].cold.1
+ -[FSNode(InternetLocatorFiles) internetLocatorTypeInfoForExtension:fileType:].cold.2
+ -[FSNode(InternetLocatorFiles) internetLocatorTypeInfoForScheme:].cold.1
+ -[LSApplicationProxy _initWithBundleUnit:context:bundleIdentifier:].cold.1
+ -[LSApplicationProxy forwardingTargetForSelector:].cold.1
+ -[LSApplicationProxy handlerRankOfClaimForContentType:].cold.1
+ -[LSApplicationRecord _initWithNode:bundleIdentifier:placeholderBehavior:systemPlaceholder:itemID:forceInBundleContainer:context:error:].cold.1
+ -[LSApplicationWorkspace _MICallbackQueue].cold.1
+ -[LSApplicationWorkspace _openUserActivity:orUserActivityUUID:activityTypeForUUID:withApplicationProxy:options:completionHandler:].cold.1
+ -[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:].cold.2
+ -[LSApplicationWorkspace isVersion:greaterThanOrEqualToVersion:].cold.1
+ -[LSApplicationWorkspace isVersion:greaterThanOrEqualToVersion:].cold.2
+ -[LSApplicationWorkspace openUserActivity:usingApplicationRecord:configuration:completionHandler:].cold.1
+ -[LSApplicationWorkspace openUserActivityWithUUID:activityType:usingApplicationRecord:configuration:completionHandler:].cold.1
+ -[LSApplicationWorkspace openUserActivityWithUUID:activityType:usingApplicationRecord:configuration:completionHandler:].cold.2
+ -[LSApplicationWorkspace openUserActivityWithUUID:activityType:usingApplicationRecord:configuration:completionHandler:].cold.3
+ -[LSApplicationWorkspace refreshUnbundledSystemExtensionPointsWithOperationUUID:requestContext:saveObserver:registrationError:]
+ -[LSApplicationWorkspace registerBuiltinApplicationWithInstallationRecord:extensionInstallationRecords:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:]
+ -[LSApplicationWorkspace registerBuiltinStandaloneExtension:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:]
+ -[LSApplicationWorkspace unregisterBuiltinApplicationAtURL:operationUUID:requestContext:saveObserver:error:]
+ -[LSApplicationWorkspace unregisterBuiltinStandaloneExtensionAtURL:operationUUID:requestContext:saveObserver:error:]
+ -[LSBuiltinApplicationRegistrant .cxx_destruct]
+ -[LSBuiltinApplicationRegistrant initWithStrategy:operationUUID:itemInfoDict:personas:]
+ -[LSBuiltinApplicationRegistrant runWithCompletion:]
+ -[LSBuiltinPluginRegistrant .cxx_destruct]
+ -[LSBuiltinPluginRegistrant initWithStrategy:operationUUID:itemInfoDict:]
+ -[LSBuiltinPluginRegistrant runWithCompletion:]
+ -[LSBundleInfoCachedValues URLForKey:].cold.1
+ -[LSBundleInfoCachedValues _initWithKeys:forDictionary:].cold.1
+ -[LSBundleInfoCachedValues arrayForKey:withValuesOfClass:].cold.1
+ -[LSBundleInfoCachedValues boolForKey:].cold.1
+ -[LSBundleInfoCachedValues dictionaryForKey:valuesOfClass:].cold.1
+ -[LSBundleInfoCachedValues numberForKey:].cold.1
+ -[LSBundleInfoCachedValues objectForKey:ofType:].cold.1
+ -[LSBundleInfoCachedValues stringForKey:].cold.1
+ -[LSBundleProxy entitlementValueForKey:ofClass:valuesOfClass:].cold.1
+ -[LSBundleProxy entitlementValuesForKeys:].cold.1
+ -[LSBundleProxy localizedValuesForKeys:fromTable:].cold.1
+ -[LSBundleProxy objectForInfoDictionaryKey:ofClass:valuesOfClass:].cold.1
+ -[LSBundleProxy objectsForInfoDictionaryKeys:].cold.1
+ -[LSBundleRecordBuilder _LSBundleFlagMap].cold.1
+ -[LSBundleRecordBuilder _LSKeyTypeMap].cold.1
+ -[LSBundleRecordBuilder _LSPlistRaritiesMap].cold.1
+ -[LSByURLBundleUnregistrant .cxx_destruct]
+ -[LSByURLBundleUnregistrant initWithStrategy:operationUUID:URL:]
+ -[LSByURLBundleUnregistrant runWithCompletion:]
+ -[LSByURLPluginUnregistrant .cxx_destruct]
+ -[LSByURLPluginUnregistrant initWithStrategy:operationUUID:URL:]
+ -[LSByURLPluginUnregistrant runWithCompletion:]
+ -[LSCodeEvaluation _setCompletedUnits:].cold.2
+ -[LSCodeEvaluation _setTotalUnits:].cold.2
+ -[LSCodeEvaluation ejectVolume].cold.1
+ -[LSCodeEvaluation finish].cold.2
+ -[LSCodeEvaluation moveItemToTrashWithReply:].cold.1
+ -[LSCodeEvaluation moveItemToTrash].cold.1
+ -[LSCodeEvaluation presentPromptOfType:options:completion:].cold.2
+ -[LSCodeEvaluation presentPromptOfType:options:completion:].cold.3
+ -[LSCodeEvaluation registerWithLaunchServices].cold.2
+ -[LSCodeEvaluation restoreOriginalNameAndIcon].cold.1
+ -[LSCodeEvaluation setQuarantineFlags:clearFlags:].cold.1
+ -[LSCodeEvaluation showInFinder].cold.1
+ -[LSCodeEvaluation showInTestFlight].cold.1
+ -[LSCodeEvaluation showOrigin].cold.1
+ -[LSCodeEvaluation showSecurityPreferencesAnchor:].cold.1
+ -[LSCodeEvaluation startWithCancellationHandler:].cold.2
+ -[LSCodeEvaluationClientManager _checkAllowed32BitHostProcess:].cold.1
+ -[LSCodeEvaluationClientManager presentPromptOfType:options:info:completion:].cold.1
+ -[LSDatabaseBlockingFetchClient getServerStoreBlockingWithCompletionHandler:].cold.1
+ -[LSDefaultApplicationQueryEntry initWithWindowOpenDates:refreshDate:defaultForCategory:]
+ -[LSDefaultApplicationQueryEntry isOpenWindowGroupFull]
+ -[LSDefaultApplicationQueryEntry newestWindowOpenDate]
+ -[LSDefaultApplicationQueryEntry oldestWindowOpenDate]
+ -[LSDefaultApplicationQueryEntry updatedEntryRotatingInWindowOpenDate:refreshDate:defaultForCategory:]
+ -[LSDefaultApplicationQueryEntry updatedEntryWithRefreshDate:defaultForCategory:]
+ -[LSDefaultApplicationQueryEntry windowOpenDates]
+ -[LSDefaultApplicationQueryServerDatastore entryForApplication:category:].cold.1
+ -[LSDefaultApplicationQueryServerDatastore removeEntriesForBundleIdentifier:].cold.2
+ -[LSDefaultApplicationQueryServerDatastore setEntry:forApplication:category:].cold.2
+ -[LSDocumentProxy isImageOrVideo].cold.1
+ -[LSMIResultRegistrantTrueDatabaseContext containerizedBundleExistsForIdentifier:]
+ -[LSMIResultRegistrantTrueDatabaseContext contextPointer]
+ -[LSMIResultRegistrantTrueDatabaseContext enumerateExtensionPointRecords:]
+ -[LSMIResultRegistrantTrueDatabaseContext findApplicationBundleAtNode:error:]
+ -[LSMIResultRegistrantTrueDatabaseContext findPluginAtNode:error:]
+ -[LSMIResultRegistrantTrueDatabaseContext pluginDataForPlugin:]
+ -[LSMIResultRegistrantTrueDatabaseContext registerBundleNodeReinitializingContext:inBundleContainer:installDictionary:personasWithAttributes:error:]
+ -[LSMIResultRegistrantTrueDatabaseContext registerNonBundledExtensionPointWithIdentifier:platform:SDKDict:url:error:]
+ -[LSMIResultRegistrantTrueDatabaseContext registerPluginNodeReinitializingContext:installDictionary:existingPlugin:error:]
+ -[LSMIResultRegistrantTrueDatabaseContext unregisterApplicationBundleByUnit:error:]
+ -[LSMIResultRegistrantTrueDatabaseContext unregisterApplicationBundleByUnit:error:].cold.1
+ -[LSMIResultRegistrantTrueDatabaseContext unregisterNonBundledExtensionPointWithIdentifier:error:]
+ -[LSMIResultRegistrantTrueDatabaseContext unregisterPluginBundleByUnit:error:]
+ -[LSPlugInQuery _init].cold.1
+ -[LSPlugInQuery sort:pluginIDs:andYield:context:].cold.1
+ -[LSPlugInQuery sort:pluginIDs:andYield:context:].cold.2
+ -[LSPlugInQuery sort:pluginIDs:andYield:context:].cold.3
+ -[LSRecord(SubclassResponsibilities) _replacementObjectForResolvedPropertyValue:forGetter:encoder:].cold.1
+ -[LSRegistrantServerStrategy beginModificationOperation]
+ -[LSRegistrantServerStrategy endModificationOperation]
+ -[LSRegistrantServerStrategy enumerateSystemEXExtensionPoints:]
+ -[LSRegistrantServerStrategy flushModificationState]
+ -[LSRegistrantServerStrategy notificationJournallerForBundleIdentifier:registeringPlaceholder:]
+ -[LSRegistrantServerStrategy preUnregistrationContextForBundleIdentifier:]
+ -[LSRegistrantServerStrategy preUnregistrationContextForBundleUnit:context:]
+ -[LSRegistrantServerStrategy runSyncBlockInWriteContext:]
+ -[LSSystemExtensionPointRefreshRegistrant .cxx_destruct]
+ -[LSSystemExtensionPointRefreshRegistrant initWithStrategy:operationUUID:]
+ -[LSSystemExtensionPointRefreshRegistrant runWithCompletion:]
+ -[_LSDModifyClient clientIsEntitledForEmbeddedRegistrationOperations]
+ -[_LSDatabase isSeeded].cold.1
+ -[_LSDefaults classesWithNameForXCTests:].cold.1
+ -[_LSDefaults currentSchemaVersion].cold.1
+ -[_LSDefaults init].cold.1
+ -[_LSDefaults init].cold.2
+ -[_LSDefaults init].cold.3
+ -[_LSDefaults init].cold.4
+ -[_LSDefaults isRegionChina].cold.1
+ -[_LSDefaults preferredLocalizations].cold.1
+ -[_LSDefaults preferredLocalizations].cold.2
+ -[_LSDefaults simulatorRootURL].cold.1
+ -[_LSDefaults simulatorRuntimeBuildVersion].cold.1
+ -[_LSDefaults simulatorRuntimeVersion].cold.1
+ -[_LSDisplayNameConstructor(Private) cleanSecondaryExtension:].cold.1
+ -[_LSExceptions applyToInfoDictionary:].cold.1
+ -[_LSExceptions(Private) platformMatchesExceptionsDictionary:].cold.1
+ -[_LSOpen2Options initWithCoder:].cold.1
+ -[_LSServerSettingsStore _internalQueue_loadPluginKitDatabase].cold.2
+ -[_LSStringLocalizer enumerateLocalizedStringsForKeys:usingBlock:].cold.1
+ -[_LSStringLocalizer enumerateLocalizedStringsForKeys:usingBlock:].cold.2
+ -[_LSStringLocalizer(Private) localizedStringWithString:inBundle:localeCode:].cold.1
+ -[_LSStringLocalizer(Private) localizedStringWithString:inBundle:localeCode:].cold.2
+ -[_LSStringsFileContent _queryLoadedPlist:forRawKey:locale:].cold.1
+ -[_LSStringsFileContent subscriptLoctableWithLocale:].cold.1
+ -[_LSStringsFileContent uncheckedObjectsForKeys:forLocaleCode:fromBundle:cacheLocalizations:].cold.1
+ -[_LSTemplateApplication markAsImmutable:options:error:].cold.1
+ GCC_except_table184
+ GCC_except_table191
+ GCC_except_table206
+ GCC_except_table244
+ GCC_except_table247
+ GCC_except_table264
+ GCC_except_table265
+ GCC_except_table266
+ GCC_except_table325
+ GCC_except_table326
+ GCC_except_table327
+ GCC_except_table341
+ LSDatabaseBlockingFetchInterface.cold.1
+ LSInit.cold.1
+ OBJC_IVAR_$_LSBuiltinApplicationRegistrant._miDict
+ OBJC_IVAR_$_LSBuiltinApplicationRegistrant._personas
+ OBJC_IVAR_$_LSBuiltinApplicationRegistrant._strategy
+ OBJC_IVAR_$_LSBuiltinApplicationRegistrant._uuid
+ OBJC_IVAR_$_LSBuiltinPluginRegistrant._miDict
+ OBJC_IVAR_$_LSBuiltinPluginRegistrant._strategy
+ OBJC_IVAR_$_LSBuiltinPluginRegistrant._uuid
+ OBJC_IVAR_$_LSByURLBundleUnregistrant._strategy
+ OBJC_IVAR_$_LSByURLBundleUnregistrant._url
+ OBJC_IVAR_$_LSByURLBundleUnregistrant._uuid
+ OBJC_IVAR_$_LSByURLPluginUnregistrant._strategy
+ OBJC_IVAR_$_LSByURLPluginUnregistrant._url
+ OBJC_IVAR_$_LSByURLPluginUnregistrant._uuid
+ OBJC_IVAR_$_LSDefaultApplicationQueryEntry._windowOpenDates
+ OBJC_IVAR_$_LSSystemExtensionPointRefreshRegistrant._strategy
+ OBJC_IVAR_$_LSSystemExtensionPointRefreshRegistrant._uuid
+ XCFURLEnumerate.cold.1
+ XCFURLEnumerate.cold.2
+ XNSGetPropertyListClasses.cold.1
+ _LSAgentSetConnection.cold.1
+ _LSAppCheckInLog.cold.1
+ _LSApplicationCheckIn.cold.11
+ _LSApplicationCheckIn.cold.12
+ _LSApplicationCheckIn.cold.13
+ _LSApplicationCheckIn.cold.14
+ _LSApplicationCheckIn.cold.15
+ _LSApplicationCheckIn.cold.16
+ _LSBindingGetTypeID.cold.1
+ _LSBindingLog.cold.1
+ _LSBundleInfoPlistKeyIsCommon.cold.1
+ _LSCSUILog.cold.1
+ _LSCanApplicationHandlePasteboardItems.cold.1
+ _LSCanUseDMF.cold.1
+ _LSCheckEntitlementForSelf.cold.1
+ _LSCheckLSDServiceAccessForAuditToken.cold.1
+ _LSCheckMachPortAccessForAuditToken.cold.1
+ _LSClientSideReconnectionPhase1.cold.1
+ _LSCommonOpenApplicationWithBundleIdentifier.cold.1
+ _LSContextDestroy.cold.1
+ _LSContextObserveChange.cold.1
+ _LSContextReleaseObservedChange.cold.1
+ _LSCopyApplicationInformationItem.cold.1
+ _LSCopyGroupContainerIdentifiersFromEntitlements.cold.1
+ _LSCopyServerStore.cold.4
+ _LSCurrentProcessMayMapDatabase.cold.1
+ _LSDDisseminationClientInterface.cold.1
+ _LSDDisseminationServerInterface.cold.1
+ _LSDServiceGetXPCConnection.cold.1
+ _LSDServiceStartAllServices.cold.1
+ _LSDataSeparationLog.cold.1
+ _LSDatabaseGetInstallingGroup.cold.1
+ _LSDatabaseGetLog.cold.1
+ _LSDatabaseGetMobileInstallSyncupGroup.cold.1
+ _LSDatabaseGetNoServerLock.cold.1
+ _LSDatabaseGetSeedingGroup.cold.1
+ _LSDefaultAppCategoryGetInfoForSubordinateClaim
+ _LSDefaultAppCategoryGetInfoForTypeIdentifierOrSubordinateTypeIdentifier
+ _LSDefaultLog.cold.1
+ _LSDisseminationLog.cold.1
+ _LSExtensionsLog.cold.1
+ _LSFindOrRegisterBundleNodeInBackground.cold.1
+ _LSGetApplicationLaunchServicesServerConnectionStatusFlags.cold.1
+ _LSGetAuditTokenForSelf.cold.1
+ _LSGetBundle.cold.1
+ _LSGetCPUArchitecture.cold.1
+ _LSGetCPUType.cold.1
+ _LSGetCurrentActivationToken.cold.1
+ _LSGetCurrentSystemBuildVersionString.cold.1
+ _LSGetCurrentSystemIOSSupportVersion.cold.1
+ _LSGetCurrentSystemVersion.cold.1
+ _LSGetEntitlementForSelf.cold.1
+ _LSGetFrontBoardOptionsDictionaryClasses.cold.1
+ _LSGetLSTemplateApplicationCreationInterface.cold.1
+ _LSGetMachTimebase.cold.1
+ _LSGetMainBundleURL.cold.1
+ _LSGetPluginNotificationAndIconCacheQueue.cold.1
+ _LSGetProductNameSuffix.cold.1
+ _LSHandlePasteboardItems.cold.2
+ _LSInstallLog.cold.1
+ _LSIsAgent.cold.1
+ _LSIsCPUTypeSubtypeRunnable.cold.1
+ _LSIsCPUTypeSubtypeRunnable.cold.2
+ _LSIsCPUTypeSubtypeRunnable.cold.3
+ _LSIsCurrentProcessSandboxed.cold.1
+ _LSIsCurrentProcessSandboxed.cold.2
+ _LSIsCurrentProcessSandboxed.cold.3
+ _LSLogAppRecordInitsForDataSeparation.cold.1
+ _LSOpenLog.cold.1
+ _LSOpenStuffCallLocal.cold.10
+ _LSOpenStuffCallLocal.cold.11
+ _LSOpenStuffCallLocal.cold.12
+ _LSOpenStuffWithPreSanitizedURLs.cold.4
+ _LSPlatformSupportsHaswell.cold.1
+ _LSProgressLog.cold.1
+ _LSReCheckinApplication.cold.1
+ _LSReCheckinApplication.cold.2
+ _LSRecordLog.cold.1
+ _LSRegisterFilePropertyProvider.cold.1
+ _LSRegistrationLog.cold.1
+ _LSServerBundleRegistration.cold.1
+ _LSServer_GetIOQueue.cold.1
+ _LSServer_ScheduleContainerRemovalTimer.cold.1
+ _LSSetApplicationLaunchServicesServerConnectionStatus.cold.1
+ _LSSetCurrentProcessMayMapDatabase.cold.1
+ _LSSetDefaultXPCConnection.cold.1
+ _LSSetProcessQuarantineProperties.cold.1
+ _LSSetUpClientSideReconnectionServices.cold.1
+ _LSSharedMemoryGetTypeID.cold.1
+ _LSStartDisseminationClientServiceIfNecessary.cold.1
+ _LSStartDisseminationServerIfNecessary.cold.1
+ _LSTemplateAppLog.cold.1
+ _LSTranslocateCoreAnalyticsAppLaunch.cold.1
+ _LSVersionNumberGetCurrentSystemVersion.cold.1
+ _LSWriteApplicationPlaceholderToURL.cold.1
+ _MergedGlobals.46
+ _OBJC_CLASS_$_LSBuiltinApplicationRegistrant
+ _OBJC_CLASS_$_LSBuiltinPluginRegistrant
+ _OBJC_CLASS_$_LSByURLBundleUnregistrant
+ _OBJC_CLASS_$_LSByURLPluginUnregistrant
+ _OBJC_CLASS_$_LSRegistrantServerStrategy
+ _OBJC_CLASS_$_LSSystemExtensionPointRefreshRegistrant
+ _OBJC_METACLASS_$_LSBuiltinApplicationRegistrant
+ _OBJC_METACLASS_$_LSBuiltinPluginRegistrant
+ _OBJC_METACLASS_$_LSByURLBundleUnregistrant
+ _OBJC_METACLASS_$_LSByURLPluginUnregistrant
+ _OBJC_METACLASS_$_LSRegistrantServerStrategy
+ _OBJC_METACLASS_$_LSSystemExtensionPointRefreshRegistrant
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _XCFRelease.cold.1
+ _XCFRetain.cold.1
+ _Z16notificationsLogv.cold.1
+ _Z17GetOurLSSessionIDv.cold.1
+ _Z19IsLSServerConnected11LSSessionIDb.cold.1
+ _Z20NormalizeLSSessionID11LSSessionID.cold.1
+ _Z20NormalizeLSSessionID11LSSessionID.cold.2
+ _Z24clientIsAllowedToConnectPK14__CFDictionary.cold.1
+ _Z28GetOurLSSessionAttributeBitsv.cold.1
+ _Z33availabilityStateForServiceDomainP17_LSDServiceDomain.cold.1
+ _Z36CFTypeGetAsLSNotificationReceiverRefPKv.cold.1
+ _Z60CopyLSApplicationInformationKeysAcceptedFromSandboxedClientsv.cold.1
+ _Z6casLogv.cold.1
+ _Z8lsCASLogi.cold.1
+ _Z9IsNetBootv.cold.1
+ _ZL11_LSErrorLogv.cold.1
+ _ZL13ApplyScanPathP8NSStringRNSt3__113unordered_setINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS1_4hashIS8_EENS1_8equal_toIS8_EENS6_IS8_EEEEj.cold.1
+ _ZL13_LSGetSession12LSSessionKey.cold.1
+ _ZL15_LSGetStoreNodev.cold.1
+ _ZL16connectedClientsv.cold.1
+ _ZL17GetQuarantineTypej.cold.1
+ _ZL18_LSSetCrashMessageP8NSString.cold.1
+ _ZL18categorizeSelectorP13objc_selector.cold.1
+ _ZL19processManagerFrontv.cold.1
+ _ZL19setSavedSessionInfoPv.cold.1
+ _ZL20_LSContextInitCommonP9LSContextP17_LSDServiceDomainmPU15__autoreleasingP7NSError.cold.4
+ _ZL20_LSContextInitCommonP9LSContextP17_LSDServiceDomainmPU15__autoreleasingP7NSError.cold.5
+ _ZL20_LSContextInitCommonP9LSContextP17_LSDServiceDomainmPU15__autoreleasingP7NSError.cold.6
+ _ZL20_LSHoistLibraryItemsP9LSContextP16_LSHoistingState.cold.1
+ _ZL20_LSOpenAsyncCommonCFPKvPK9__CFArrayPK7__CFURLPK7__LSASNP15_LSOpen2OptionsU13block_pointerFvS9_hP9__CFErrorE.cold.1
+ _ZL22launchThruRunningboardP18RBSProcessIdentityP8NSStringS2_S2_PK7__LSASNP7NSArrayIS2_EP12NSDictionaryPS6_IP11LSSliceInfoEPK15_LSOpen2OptionsP8NSNumberiP18RBSDomainAttributeSA_hPU15__autoreleasingP12RBSAssertionPU15__autoreleasingP7NSError.cold.1
+ _ZL22launchThruRunningboardP18RBSProcessIdentityP8NSStringS2_S2_PK7__LSASNP7NSArrayIS2_EP12NSDictionaryPS6_IP11LSSliceInfoEPK15_LSOpen2OptionsP8NSNumberiP18RBSDomainAttributeSA_hPU15__autoreleasingP12RBSAssertionPU15__autoreleasingP7NSError.cold.2
+ _ZL23getNeedsRegistrationLogv.cold.1
+ _ZL24_LSGetDispatchTokenQueuev.cold.1
+ _ZL24_LSPlistGetCommonStringsv.cold.1
+ _ZL24registrationCleanupQueuev.cold.1
+ _ZL25_LSLaunchWithRunningboardP9LSContextP6FSNodejPvPK9__CFArrayPK6AEDescS9_P7NSArrayIP11LSSliceInfoEPK14__CFDictionaryjPK13audit_token_tPK15_LSOpen2OptionsP19ProcessSerialNumberPU15__autoreleasingP7NSError.cold.1
+ _ZL25_LSLaunchWithRunningboardP9LSContextP6FSNodejPvPK9__CFArrayPK6AEDescS9_P7NSArrayIP11LSSliceInfoEPK14__CFDictionaryjPK13audit_token_tPK15_LSOpen2OptionsP19ProcessSerialNumberPU15__autoreleasingP7NSError.cold.2
+ _ZL25_LSLaunchWithRunningboardP9LSContextP6FSNodejPvPK9__CFArrayPK6AEDescS9_P7NSArrayIP11LSSliceInfoEPK14__CFDictionaryjPK13audit_token_tPK15_LSOpen2OptionsP19ProcessSerialNumberPU15__autoreleasingP7NSError.cold.3
+ _ZL25_disseminationClientQueuev.cold.1
+ _ZL25disseminationServiceQueuev.cold.1
+ _ZL25pendingSaveTokenInterfacev.cold.1
+ _ZL26getRBSProcessIdentityClassv.cold.1
+ _ZL27_LSGetContainerCleanupQueuev.cold.1
+ _ZL28_LSDNCGetForbiddenCharactersj.cold.1
+ _ZL32_LSTrustedSignatureGetTrimTimingv.cold.1
+ _ZL34_LSDNCGetExactConfusableCharactersv.cold.1
+ _ZL34_LSHandlePasteboard_PBItemsApplierPK29CFPasteboardApplyFunctionDataPv.cold.1
+ _ZL34_LSHandlePasteboard_PBItemsApplierPK29CFPasteboardApplyFunctionDataPv.cold.2
+ _ZL36_LSPlistLookUpCompactedStringByIndexm.cold.1
+ _ZL36_LSPlistLookUpIndexOfCompactedStringP8NSString.cold.1
+ _ZL36allocateFileQuarantineWithPropertiesPK14__CFDictionary.cold.1
+ _ZL36allocateFileQuarantineWithPropertiesPK14__CFDictionary.cold.2
+ _ZL39getLocallyLaunchedApplicationsDispatchQv.cold.1
+ _ZL41_LSCreateRegistrationDataForDirectoryNodeP9LSContextP18LSRegistrationInfoPK7__CFURLP17_LSBundleProviderP6FSNodePK14__CFDictionaryPPK9__CFArray.cold.1
+ _ZL41_LSCreateRegistrationDataForDirectoryNodeP9LSContextP18LSRegistrationInfoPK7__CFURLP17_LSBundleProviderP6FSNodePK14__CFDictionaryPPK9__CFArray.cold.2
+ _ZL42getIsCurrentThreadInLSContextInitReferencev.cold.1
+ _ZL49_LSCopyApplicationInformationItemFromSharedMemoryPK20__LSSharedMemoryPagePK7__LSASNPKvPS6_.cold.1
+ _ZL59_LSCopySniffedExtensionAndTypeIdentifierForSniffedExtensionPK10__CFStringhPS1_S2_.cold.1
+ _ZL9getLibIDsv.cold.1
+ _ZN13VolumeBinding20GetTypeFromVolumeURLEPK7__CFURLPK14__CFDictionaryPb.cold.1
+ _ZN13VolumeBinding23CopyKextIconInfoFromURLEPK7__CFURLPPK10__CFStringS6_.cold.1
+ _ZN13VolumeBinding25GetVolumePropertyFlagKeysEv.cold.1
+ _ZN13VolumeBinding26CopyResourceURLForKextIconEPK10__CFStringS2_.cold.1
+ _ZN13VolumeBinding28CopyKextIconInfoFromDeviceIDEPKcPPK10__CFStringS5_.cold.1
+ _ZN14BindingManager13FindAndRetainEP13OpaqueIconRef.cold.1
+ _ZN14BindingManager14FindAndReleaseEP13OpaqueIconRef.cold.1
+ _ZN14BindingManager14FindOrRegisterEP7Bindingb.cold.1
+ _ZN14BindingManager21FindAndGetRetainCountEP13OpaqueIconRef.cold.1
+ _ZN14BindingManager6RetainEP7Bindingb.cold.1
+ _ZN14BindingManager7ReleaseEP7Bindingb.cold.1
+ _ZN14LSCrashMessageC2EP8NSString.cold.1
+ _ZN14LSCrashMessageD2Ev.cold.1
+ _ZN14LaunchServices10DMFSupportL10getMonitorEb.cold.1
+ _ZN14LaunchServices10DMFSupportL10getMonitorEb.cold.2
+ _ZN14LaunchServices10DMFSupportL6getLogEv.cold.1
+ _ZN14LaunchServices12OpenWithMenuL15getOpenWithMenuERNS0_5StateEPU15__autoreleasingP7NSError.cold.15
+ _ZN14LaunchServices12OpenWithMenuL6getLogEv.cold.1
+ _ZN14LaunchServices12PrefsStorage26_GetCurrentArchitectureKeyEv.cold.1
+ _ZN14LaunchServices12PrefsStorage7_GetLogEv.cold.1
+ _ZN14LaunchServices12PrefsStorage9GetSharedEv.cold.1
+ _ZN14LaunchServices12URLOverridesL6getLogEv.cold.1
+ _ZN14LaunchServices14BundleWrappersL12LSWrapperLogEv.cold.1
+ _ZN14LaunchServices14TypeEvaluationL12runEvaluatorEP9LSContextRKNS_13TypeEvaluatorEPU15__autoreleasingP7NSError.cold.1
+ _ZN14LaunchServices14TypeEvaluationL12runEvaluatorEP9LSContextRKNS_13TypeEvaluatorEPU15__autoreleasingP7NSError.cold.2
+ _ZN14LaunchServices15DatabaseContextL26getPerThreadStateReferenceEv.cold.1
+ _ZN14LaunchServices15DatabaseContextL6getLogEv.cold.1
+ _ZN14LaunchServices16EligibilityCache16getCallbackQueueEv.cold.1
+ _ZN14LaunchServices16EligibilityCache19getNotifyStateQueueEv.cold.1
+ _ZN14LaunchServices16EligibilityCache30eligibleForDomainFailingClosedE23os_eligibility_domain_t.cold.1
+ _ZN14LaunchServices16EligibilityCache6sharedEv.cold.1
+ _ZN14LaunchServices17BindingEvaluation5StateC2EP9LSContextRKNS_16BindingEvaluatorE.cold.1
+ _ZN14LaunchServices17BindingEvaluationL12runEvaluatorERNS0_5StateEPU15__autoreleasingP7NSError.cold.1
+ _ZN14LaunchServices17BindingEvaluationL12runEvaluatorERNS0_5StateEPU15__autoreleasingP7NSError.cold.2
+ _ZN14LaunchServices19PrefsCapabilityInfo9EnumerateEU13block_pointerFvRKS0_PbE.cold.1
+ _ZN14LaunchServices19URLPropertyProviderL14getUTTypeClassEv.cold.1
+ _ZN14LaunchServices19URLPropertyProviderL28prepareIsHiddenBySystemValueERNS_8Database7ContextEPU34objcproto23FSNodePropertyProviding11objc_objectP11__FileCachePK10__CFStringPNS0_5StateEPU15__autoreleasingP7NSError.cold.1
+ _ZN14LaunchServices19URLPropertyProviderL28prepareIsHiddenBySystemValueERNS_8Database7ContextEPU34objcproto23FSNodePropertyProviding11objc_objectP11__FileCachePK10__CFStringPNS0_5StateEPU15__autoreleasingP7NSError.cold.2
+ _ZN14LaunchServices20PersistentIdentifierL6getLogEv.cold.1
+ _ZN14LaunchServices6RecordL18getNullPlaceholderEv.cold.1
+ _ZN14LaunchServices8XCSelectL32getSelectedDeveloperDirectoryURLEv.cold.1
+ _ZN14LaunchServicesL35getLocalizedKindStringWithEvaluatorEP9LSContextP7NSArrayIP8NSStringERKNS_16BindingEvaluatorEhPU15__autoreleasingP7NSError.cold.1
+ _ZN14_LSPreferences4WithEPKNS_15SecurityContextEU13block_pointerFvPKvE.cold.1
+ _ZN16BindingBlueprint17copyURLPropertiesEPK7__CFURL.cold.2
+ _ZN16BindingBlueprint27initializeSpecialFolderTypeEPK7__CFURLPK14__CFDictionary.cold.1
+ _ZN16BindingBlueprint27initializeSpecialFolderTypeEPK7__CFURLPK14__CFDictionary.cold.2
+ _ZN16BindingBlueprintC2EPK8__CFData.cold.1
+ _ZN16LSBundleProvider21bootCacheInfoProviderEb.cold.1
+ _ZN18LSSharedMemoryPage16CopyForSessionIDE11LSSessionIDb.cold.1
+ _ZN18LSSharedMemoryPage16CopyForSessionIDE11LSSessionIDb.cold.2
+ _ZN18LSSharedMemoryPage16CopyForSessionIDE11LSSessionIDb.cold.3
+ _ZN18LSSharedMemoryPage27GetUIPresentationModeStringEj.cold.1
+ _ZN18LSSharedMemoryPage33InvalidateCachedSharedMemoryPagesE11LSSessionID.cold.1
+ _ZN18LSSharedMemoryPagenwEmPK13__CFAllocator.cold.1
+ _ZN22LSNotificationReceiver18CreateNotificationEPK13__CFAllocator11LSSessionIDP16dispatch_queue_sU13block_pointerFv18LSNotificationCodedPKvPK7__LSASNS3_S8_E.cold.1
+ _ZN22LSNotificationReceiver18DeleteNotificationEPKv.cold.1
+ _ZN22LSNotificationReceiver20ReEstablishListenersEb.cold.1
+ _ZN22LSNotificationReceiver23ReleaseAllNotificationsEv.cold.1
+ _ZN22LSNotificationReceiver23ReleaseAllNotificationsEv.cold.2
+ _ZN22LSNotificationReceiver32CopyNotificationInformationForIDEPKv.cold.1
+ _ZN22LSNotificationReceiver6modifyEmPK18LSNotificationCodemS2_PKvS4_.cold.1
+ _ZN22LSNotificationReceivernwEmPK13__CFAllocator.cold.1
+ _ZN26LSClientToServerConnection21setupServerConnectionEiPK14__CFDictionary.cold.1
+ _ZN26LSClientToServerConnection21setupServerConnectionEiPK14__CFDictionary.cold.2
+ _ZN26LSClientToServerConnection21setupServerConnectionEiPK14__CFDictionary.cold.3
+ _ZN26LSClientToServerConnection21setupServerConnectionEiPK14__CFDictionary.cold.4
+ _ZN26LSClientToServerConnectionC2EiPK14__CFDictionary.cold.1
+ __28-[_LSDefaults isRegionChina]_block_invoke.cold.4
+ __47-[LSByURLBundleUnregistrant runWithCompletion:]_block_invoke.159
+ __47-[LSByURLPluginUnregistrant runWithCompletion:]_block_invoke.179
+ __48-[LSDatabaseBuilder createAndSeedLocalDatabase:]_block_invoke.2
+ __48-[LSDatabaseBuilder createAndSeedLocalDatabase:]_block_invoke.4
+ __54-[LSDatabaseBuilder scanAndRegisterSpotlightContents:]_block_invoke.35
+ __61-[LSSystemExtensionPointRefreshRegistrant runWithCompletion:]_block_invoke.221
+ __61-[LSSystemExtensionPointRefreshRegistrant runWithCompletion:]_block_invoke.225
+ __63-[LSApplicationWorkspaceRemoteObserver applicationsDidInstall:]_block_invoke.cold.1
+ __63-[LSApplicationWorkspaceRemoteObserver applicationsDidInstall:]_block_invoke.cold.2
+ __65+[_LSTrustedSignatureDatabase(Database) scheduleDatabaseTrimming]_block_invoke.cold.1
+ __66-[_LSLocalizedStringRecord stringValueWithPreferredLocalizations:]_block_invoke.1.cold.3
+ __68-[LSApplicationWorkspaceRemoteObserver applicationInstallsDidStart:]_block_invoke.659
+ __83-[_LSDisplayNameConstructor(Private) initContentBitsWithDisplayName:treatAsFSName:]_block_invoke.cold.1
+ __83-[_LSDisplayNameConstructor(Private) initContentBitsWithDisplayName:treatAsFSName:]_block_invoke.cold.2
+ __Block_byref_object_copy_.301
+ __Block_byref_object_copy_.330
+ __Block_byref_object_copy_.341
+ __Block_byref_object_copy_.46
+ __Block_byref_object_copy_.835
+ __Block_byref_object_copy_.984
+ __Block_byref_object_dispose_.302
+ __Block_byref_object_dispose_.331
+ __Block_byref_object_dispose_.342
+ __Block_byref_object_dispose_.47
+ __Block_byref_object_dispose_.836
+ __Block_byref_object_dispose_.985
+ __LSDefaultsGetSharedInstance.cold.1
+ __LSFaultForPluginQuery
+ __LSUnregisterAppByUnit
+ __MergedGlobals
+ __OBJC_$_INSTANCE_METHODS_LSBuiltinApplicationRegistrant
+ __OBJC_$_INSTANCE_METHODS_LSBuiltinPluginRegistrant
+ __OBJC_$_INSTANCE_METHODS_LSByURLBundleUnregistrant
+ __OBJC_$_INSTANCE_METHODS_LSByURLPluginUnregistrant
+ __OBJC_$_INSTANCE_METHODS_LSRegistrantServerStrategy
+ __OBJC_$_INSTANCE_METHODS_LSSystemExtensionPointRefreshRegistrant
+ __OBJC_$_INSTANCE_VARIABLES_LSBuiltinApplicationRegistrant
+ __OBJC_$_INSTANCE_VARIABLES_LSBuiltinPluginRegistrant
+ __OBJC_$_INSTANCE_VARIABLES_LSByURLBundleUnregistrant
+ __OBJC_$_INSTANCE_VARIABLES_LSByURLPluginUnregistrant
+ __OBJC_$_INSTANCE_VARIABLES_LSSystemExtensionPointRefreshRegistrant
+ __OBJC_$_PROP_LIST_LSRegistrantServerStrategy
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LSRegistrantDatabaseContext
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LSRegistrantDatabaseContextProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LSRegistrantStrategy
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LSRegistrantDatabaseContext
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LSRegistrantDatabaseContextProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LSRegistrantStrategy
+ __OBJC_$_PROTOCOL_REFS_LSRegistrantDatabaseContext
+ __OBJC_$_PROTOCOL_REFS_LSRegistrantDatabaseContextProviding
+ __OBJC_$_PROTOCOL_REFS_LSRegistrantStrategy
+ __OBJC_CLASS_PROTOCOLS_$_LSRegistrantServerStrategy
+ __OBJC_CLASS_RO_$_LSBuiltinApplicationRegistrant
+ __OBJC_CLASS_RO_$_LSBuiltinPluginRegistrant
+ __OBJC_CLASS_RO_$_LSByURLBundleUnregistrant
+ __OBJC_CLASS_RO_$_LSByURLPluginUnregistrant
+ __OBJC_CLASS_RO_$_LSRegistrantServerStrategy
+ __OBJC_CLASS_RO_$_LSSystemExtensionPointRefreshRegistrant
+ __OBJC_LABEL_PROTOCOL_$_LSRegistrantDatabaseContext
+ __OBJC_LABEL_PROTOCOL_$_LSRegistrantDatabaseContextProviding
+ __OBJC_LABEL_PROTOCOL_$_LSRegistrantStrategy
+ __OBJC_METACLASS_RO_$_LSBuiltinApplicationRegistrant
+ __OBJC_METACLASS_RO_$_LSBuiltinPluginRegistrant
+ __OBJC_METACLASS_RO_$_LSByURLBundleUnregistrant
+ __OBJC_METACLASS_RO_$_LSByURLPluginUnregistrant
+ __OBJC_METACLASS_RO_$_LSRegistrantServerStrategy
+ __OBJC_METACLASS_RO_$_LSSystemExtensionPointRefreshRegistrant
+ __OBJC_PROTOCOL_$_LSRegistrantDatabaseContext
+ __OBJC_PROTOCOL_$_LSRegistrantDatabaseContextProviding
+ __OBJC_PROTOCOL_$_LSRegistrantStrategy
+ __Z28CFDictionaryGetValueAsNumberPK14__CFDictionaryPKv
+ __ZL36appMayTreatUnclaimedDocumentUnsafelyP9LSContextjPK12LSBundleDataP6FSNode
+ __ZN14LaunchServices16EligibilityCache30eligibleForDomainFailingClosedE23os_eligibility_domain_t
+ __ZN14LaunchServices17BindingEvaluation25BindingEligibilityChecker43eligibleToAddWeakBindingForDefaultAppClaimsERKNS0_5StateE
+ __ZN14LaunchServices17BindingEvaluationL28defaultAppCategoryBeingBoundERKNS0_5StateE
+ __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8nn190102INS_13move_iteratorINS_11__wrap_iterIPN14LaunchServices17BindingEvaluation15ExtendedBindingEEEEESB_S9_EENS_4pairIT_T1_EESD_T0_SE_
+ __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8nn190102INS_21__tree_const_iteratorIN14LaunchServices12OpenWithMenu10BundleInfoEPNS_11__tree_nodeIS7_PvEElEESC_PS7_EENS_4pairIT_T1_EESF_T0_SG_
+ __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8nn190102IPN14LaunchServices17BindingEvaluation15ExtendedBindingES7_P9LSBindingEENS_4pairIT_T1_EESB_T0_SC_
+ __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8nn190102IPN14LaunchServices17BindingEvaluation15ExtendedBindingES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
+ __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB8nn190102INS_16reverse_iteratorIPN14LaunchServices12OpenWithMenu10BundleInfoEEES9_NS4_INS_11__wrap_iterIS8_EEEEEENS_4pairIT_T1_EESE_T0_SF_
+ __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB8nn190102IP9LSBindingS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
+ __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB8nn190102IPN14LaunchServices12OpenWithMenu10BundleInfoES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
+ __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB8nn190102IPN14LaunchServices17BindingEvaluation15ExtendedBindingES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
+ __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB8nn190102IPU6__weakP8LSRecordS7_S7_EENS_4pairIT_T1_EES9_T0_SA_
+ __ZNKSt3__114default_deleteIN14LaunchServices12OpenWithMenu5StateEEclB8nn190102EPS3_
+ __ZNKSt3__120__move_backward_implINS_17_ClassicAlgPolicyEEclB8nn190102IP9LSBindingS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
+ __ZNKSt3__120__move_backward_implINS_17_ClassicAlgPolicyEEclB8nn190102IPN14LaunchServices12OpenWithMenu10BundleInfoES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
+ __ZNKSt3__120__move_backward_implINS_17_ClassicAlgPolicyEEclB8nn190102IPN14LaunchServices17BindingEvaluation15ExtendedBindingES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
+ __ZNKSt3__120__move_backward_implINS_17_ClassicAlgPolicyEEclB8nn190102IPU6__weakP8LSRecordS7_S7_EENS_4pairIT_T1_EES9_T0_SA_
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8nn190102EPKvm
+ __ZNKSt3__16__lessIvvEclB8nn190102INS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES8_EEbRKT_RKT0_
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8nn190102ERKS6_S9_
+ __ZNSt3__110__function12__value_funcIFP11objc_objectS3_P7NSErrorEED2B8nn190102Ev
+ __ZNSt3__110__function12__value_funcIFbP11objc_objectEED2B8nn190102Ev
+ __ZNSt3__110unique_ptrIA_PNS_16__hash_node_baseIPNS_11__hash_nodeIiPvEEEENS_25__bucket_list_deallocatorINS_3pmr21polymorphic_allocatorIS7_EEEEED2B8nn190102Ev
+ __ZNSt3__110unique_ptrIA_PNS_16__hash_node_baseIPNS_11__hash_nodeIjPvEEEENS_25__bucket_list_deallocatorINS_3pmr21polymorphic_allocatorIS7_EEEEED2B8nn190102Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEEPvEENS_22__hash_node_destructorINS_9allocatorISA_EEEEE5resetB8nn190102EPSA_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIP27OpaqueMappedResourceFileRefU8__strongP6NSDataEEPvEENS_22__hash_node_destructorINS_9allocatorISA_EEEEE5resetB8nn190102EPSA_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIPKvU8__strongP5NSSetIP10objc_classEEEPvEENS_22__hash_node_destructorINS_9allocatorISD_EEEEE5resetB8nn190102EPSD_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS_13unordered_mapIjbNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjbEEEEEEEEPvEENS_22__hash_node_destructorINS8_ISG_EEEEE5resetB8nn190102EPSG_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEEPvEENS_22__hash_node_destructorINS8_ISD_EEEEE5resetB8nn190102EPSD_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjU8__strongP19LSApplicationRecordEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8nn190102EPS8_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjU8__strongP6FSNodeEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8nn190102EPS8_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjU8__strongP8NSStringEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8nn190102EPS8_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIiU8__strongPU29objcproto18OS_dispatch_source8NSObjectEEPvEENS_22__tree_node_destructorINS_9allocatorIS9_EEEEE5resetB8nn190102EPS9_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIjU8__strongP8NSStringEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEE5resetB8nn190102EPS8_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeImU8__strongU13block_pointerFvvEEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEE5resetB8nn190102EPS8_
+ __ZNSt3__111__sift_downB8nn190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEvT1_OT0_NS_15iterator_traitsISC_E15difference_typeESC_
+ __ZNSt3__111__sift_downB8nn190102INS_17_ClassicAlgPolicyERU13block_pointerFbRKPKvS5_EPS3_EEvT1_OT0_NS_15iterator_traitsISA_E15difference_typeESA_
+ __ZNSt3__111__sift_downB8nn190102INS_17_ClassicAlgPolicyERZN14LaunchServices17BindingEvaluationL4sortERNS3_5StateEE3$_0NS_11__wrap_iterIPNS3_15ExtendedBindingEEEEEvT1_OT0_NS_15iterator_traitsISC_E15difference_typeESC_
+ __ZNSt3__112__destroy_atB8nn190102IN14LaunchServices12OpenWithMenu10BundleInfoELi0EEEvPT_
+ __ZNSt3__112__destruct_n9__processB8nn190102IN14LaunchServices12OpenWithMenu10BundleInfoEEEvPT_NS_17integral_constantIbLb0EEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIiP8os_log_sEENS_22__unordered_map_hasherIiS4_NS_4hashIiEENS_8equal_toIiEELb1EEENS_21__unordered_map_equalIiS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_performB8nn190102EPNS_11__hash_nodeIS4_PvEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIiP8os_log_sEENS_22__unordered_map_hasherIiS4_NS_4hashIiEENS_8equal_toIiEELb1EEENS_21__unordered_map_equalIiS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_prepareB8nn190102EmRS4_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn190102Emc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn190102ILi0EEEPKc
+ __ZNSt3__113__tree_removeB8nn190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__113unordered_mapIPK20LSExtensionPointDatajZ27_LSEnumerateExtensionPointsE30_LSExtensionPointCxxComparatorS4_NS_9allocatorINS_4pairIKS3_jEEEEED1B8nn190102Ev
+ __ZNSt3__114__construct_atB8nn190102IN14LaunchServices12OpenWithMenu10BundleInfoEJS3_EPS3_EEPT_S6_DpOT0_
+ __ZNSt3__114__split_bufferI9LSBindingRNS_9allocatorIS1_EEE17__destruct_at_endB8nn190102EPS1_
+ __ZNSt3__114__split_bufferI9LSBindingRNS_9allocatorIS1_EEE9push_backB8nn190102ERKS1_
+ __ZNSt3__114__split_bufferIN14LaunchServices12OpenWithMenu10BundleInfoERNS_9allocatorIS3_EEE5clearB8nn190102Ev
+ __ZNSt3__114__split_bufferIN14LaunchServices12OpenWithMenu4ItemERNS_9allocatorIS3_EEE5clearB8nn190102Ev
+ __ZNSt3__114__split_bufferIN14LaunchServices17BindingEvaluation15ExtendedBindingERNS_3pmr21polymorphic_allocatorIS3_EEE5clearB8nn190102Ev
+ __ZNSt3__114__split_bufferIN14LaunchServices17BindingEvaluation15ExtendedBindingERNS_3pmr21polymorphic_allocatorIS3_EEE9push_backB8nn190102ERKS3_
+ __ZNSt3__114__split_bufferIN14LaunchServices30FeatureFlagPredicateEvaluation20FeatureFlagSpecifierERNS_9allocatorIS3_EEE5clearB8nn190102Ev
+ __ZNSt3__114__split_bufferINS_10shared_ptrIN14LaunchServices16PerThreadContextEEERNS_9allocatorIS4_EEE5clearB8nn190102Ev
+ __ZNSt3__114__split_bufferINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERNS4_IS6_EEE17__destruct_at_endB8nn190102EPS6_
+ __ZNSt3__114__split_bufferINS_4pairIU8__strongP8NSStringU8__strongP10NSMenuItemEERNS_9allocatorIS8_EEE17__destruct_at_endB8nn190102EPS8_
+ __ZNSt3__116__insertion_sortB8nn190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEvT1_SC_T0_
+ __ZNSt3__116__insertion_sortB8nn190102INS_17_ClassicAlgPolicyERU13block_pointerFbRKPKvS5_EPS3_EEvT1_SA_T0_
+ __ZNSt3__116__insertion_sortB8nn190102INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRKN14LaunchServices12OpenWithMenu10BundleInfoES6_ENS_11__wrap_iterIPS4_EEEEvT1_SE_T0_
+ __ZNSt3__116__pad_and_outputB8nn190102IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__116__rotate_forwardB8nn190102INS_17_ClassicAlgPolicyENS_11__wrap_iterIPN14LaunchServices12OpenWithMenu10BundleInfoEEEEET0_S8_S8_S8_
+ __ZNSt3__117__floyd_sift_downB8nn190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEET1_SC_OT0_NS_15iterator_traitsISC_E15difference_typeE
+ __ZNSt3__117__floyd_sift_downB8nn190102INS_17_ClassicAlgPolicyERU13block_pointerFbRKPKvS5_EPS3_EET1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
+ __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8nn190102Ev
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI11LSSliceDataEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI13LSBundleClassEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI13LSPersonaTypeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI19ProcessSerialNumberEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI23os_eligibility_answer_tEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI8_NSRangeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI9LSBindingEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN14LaunchServices12OpenWithMenu10BundleInfoEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN14LaunchServices12OpenWithMenu4ItemEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN14LaunchServices19URLPropertyProvider12FilePropertyEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN14LaunchServices30FeatureFlagPredicateEvaluation20FeatureFlagSpecifierEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN14LaunchServices5Types41EnumeratedTypeUnitOrDynamicTypeIdentifierEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_4pairIP13objc_selectorPFvP11objc_objectS4_EEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_4pairIU8__strongP8NSStringU8__strongP10NSMenuItemEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_4pairIjPK12LSBundleDataEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_4pairIjU8__strongP6NSUUIDEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIP7BindingEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIP8LSRecordEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIPK10__CFStringEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIPK7__LSASNEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIPiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIPvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIU6__weakP8LSRecordEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIU8__strongP19LSApplicationRecordEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIU8__strongP8NSStringEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIU8__strongU13block_pointerFvbP11_LSDatabaseP7NSErrorEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIU8__strongU13block_pointerFvvEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorItEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__merge_move_assignB8nn190102INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRKN14LaunchServices12OpenWithMenu10BundleInfoES6_EPS4_SB_NS_11__wrap_iterISB_EEEEvT1_SE_T2_SF_T3_T0_
+ __ZNSt3__119__partial_sort_implB8nn190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEESB_EET1_SC_SC_T2_OT0_
+ __ZNSt3__119__partial_sort_implB8nn190102INS_17_ClassicAlgPolicyERU13block_pointerFbRKPKvS5_EPS3_S9_EET1_SA_SA_T2_OT0_
+ __ZNSt3__119__shared_weak_count16__release_sharedB8nn190102Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8nn190102Ev
+ __ZNSt3__120__half_inplace_mergeB8nn190102INS_17_ClassicAlgPolicyENS_8__invertIRU8__strongU13block_pointerFbRKN14LaunchServices12OpenWithMenu10BundleInfoES7_EEENS_16reverse_iteratorIPS5_EESF_NSD_INS_11__wrap_iterISE_EEEESI_SI_EEvT1_T2_T3_T4_T5_OT0_
+ __ZNSt3__120__half_inplace_mergeB8nn190102INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRKN14LaunchServices12OpenWithMenu10BundleInfoES6_EPS4_SB_NS_11__wrap_iterISB_EESD_SD_EEvT1_T2_T3_T4_T5_OT0_
+ __ZNSt3__120back_insert_iteratorINS_6vectorIjNS_9allocatorIjEEEEEaSB8nn190102EOj
+ __ZNSt3__120back_insert_iteratorINS_6vectorIjNS_9allocatorIjEEEEEaSB8nn190102ERKj
+ __ZNSt3__120get_temporary_bufferB8nn190102IN14LaunchServices12OpenWithMenu10BundleInfoEEENS_4pairIPT_lEEl
+ __ZNSt3__121__insertion_sort_moveB8nn190102INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRKN14LaunchServices12OpenWithMenu10BundleInfoES6_ENS_11__wrap_iterIPS4_EEEEvT1_SE_PNS_15iterator_traitsISE_E10value_typeET0_
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B8nn190102EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B8nn190102EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B8nn190102EPKcm
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPvEEEEEclB8nn190102EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE13_LSPathBucketEEPvEEEEEclB8nn190102EPSC_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIP17_opaque_pthread_tNS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEEPvEEEEEclB8nn190102EPSC_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIPKv9LSBindingEEPvEEEEEclB8nn190102EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIPKvNS_6vectorINS_4pairIP13objc_selectorPFvP11objc_objectS9_EEENS1_ISE_EEEEEEPvEEEEEclB8nn190102EPSJ_
+ __ZNSt3__122__libcpp_verbose_abortEPKcz
+ __ZNSt3__122__merge_move_constructB8nn190102INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRKN14LaunchServices12OpenWithMenu10BundleInfoES6_ENS_11__wrap_iterIPS4_EESD_EEvT1_SE_T2_SF_PNS_15iterator_traitsISE_E10value_typeET0_
+ __ZNSt3__123__optional_storage_baseI9LSBindingLb0EE13__assign_fromB8nn190102INS_27__optional_move_assign_baseIS1_Lb0EEEEEvOT_
+ __ZNSt3__123__optional_storage_baseIN14LaunchServices12OpenWithMenu10BundleInfoELb0EE13__assign_fromB8nn190102INS_27__optional_move_assign_baseIS3_Lb0EEEEEvOT_
+ __ZNSt3__123__optional_storage_baseIN14LaunchServices13TypeEvaluator6ResultELb0EE13__assign_fromB8nn190102INS_27__optional_move_assign_baseIS3_Lb0EEEEEvOT_
+ __ZNSt3__123__optional_storage_baseIU8__strongP12NSDictionaryIP8NSStringP11objc_objectELb0EE13__assign_fromB8nn190102INS_27__optional_move_assign_baseIS8_Lb0EEEEEvOT_
+ __ZNSt3__123__optional_storage_baseIU8__strongP8NSStringLb0EE13__assign_fromB8nn190102INS_27__optional_move_assign_baseIS3_Lb0EEEEEvOT_
+ __ZNSt3__124__buffered_inplace_mergeB8nn190102INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRKN14LaunchServices12OpenWithMenu10BundleInfoES6_ENS_11__wrap_iterIPS4_EEEEvT1_SE_SE_OT0_NS_15iterator_traitsISE_E15difference_typeESJ_PNSI_10value_typeE
+ __ZNSt3__124__optional_destruct_baseI9LSBindingLb0EE5resetB8nn190102Ev
+ __ZNSt3__124__optional_destruct_baseI9LSBindingLb0EED2B8nn190102Ev
+ __ZNSt3__124__optional_destruct_baseIN14LaunchServices12OpenWithMenu10BundleInfoELb0EE5resetB8nn190102Ev
+ __ZNSt3__124__optional_destruct_baseIN14LaunchServices12OpenWithMenu10BundleInfoELb0EED2B8nn190102Ev
+ __ZNSt3__124__optional_destruct_baseIN14LaunchServices14BundleWrappers28BundleWrapperUpdateOperationELb0EE5resetB8nn190102Ev
+ __ZNSt3__124__optional_destruct_baseIN14LaunchServices14BundleWrappers28BundleWrapperUpdateOperationELb0EED2B8nn190102Ev
+ __ZNSt3__124__optional_destruct_baseIN14LaunchServices16EligibilityCache11NotifyStateELb0EE5resetB8nn190102Ev
+ __ZNSt3__124__optional_destruct_baseIN14LaunchServices30FeatureFlagPredicateEvaluation20FeatureFlagSpecifierELb0EED2B8nn190102Ev
+ __ZNSt3__124__optional_destruct_baseIN14LaunchServices30FeatureFlagPredicateEvaluation9PredicateELb0EE5resetB8nn190102Ev
+ __ZNSt3__124__optional_destruct_baseIN14LaunchServices30FeatureFlagPredicateEvaluation9PredicateELb0EED2B8nn190102Ev
+ __ZNSt3__124__put_character_sequenceB8nn190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__124__sort5_maybe_branchlessB8nn190102INS_17_ClassicAlgPolicyERZ87+[LSApplicationRecord(UserActivity) applicationRecordsForUserActivityType:limit:error:]E3$_0PNS_4pairIjPK12LSBundleDataEELi0EEEvT1_SA_SA_SA_SA_T0_
+ __ZNSt3__124__sort5_maybe_branchlessB8nn190102INS_17_ClassicAlgPolicyERZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]E3$_1PjLi0EEEvT1_S5_S5_S5_S5_T0_
+ __ZNSt3__124__sort5_maybe_branchlessB8nn190102INS_17_ClassicAlgPolicyERZL33_LSBundleCopyArchitectures_CommonPK12LSBundleDataP7NSArrayIP8NSStringEE3$_0P11LSSliceDataLi0EEEvT1_SE_SE_SE_SE_T0_
+ __ZNSt3__125__throw_bad_function_callB8nn190102Ev
+ __ZNSt3__126__insertion_sort_unguardedB8nn190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEvT1_SC_T0_
+ __ZNSt3__126__insertion_sort_unguardedB8nn190102INS_17_ClassicAlgPolicyERU13block_pointerFbRKPKvS5_EPS3_EEvT1_SA_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8nn190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEbT1_SC_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8nn190102INS_17_ClassicAlgPolicyERU13block_pointerFbRKPKvS5_EPS3_EEbT1_SA_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8nn190102INS_17_ClassicAlgPolicyERZ87+[LSApplicationRecord(UserActivity) applicationRecordsForUserActivityType:limit:error:]E3$_0PNS_4pairIjPK12LSBundleDataEEEEbT1_SA_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8nn190102INS_17_ClassicAlgPolicyERZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]E3$_1PjEEbT1_S5_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8nn190102INS_17_ClassicAlgPolicyERZL33_LSBundleCopyArchitectures_CommonPK12LSBundleDataP7NSArrayIP8NSStringEE3$_0P11LSSliceDataEEbT1_SE_T0_
+ __ZNSt3__127__throw_bad_optional_accessB8nn190102Ev
+ __ZNSt3__127__tree_balance_after_insertB8nn190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__131__partition_with_equals_on_leftB8nn190102INS_17_ClassicAlgPolicyEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERNS_6__lessIvvEEEET0_SC_SC_T1_
+ __ZNSt3__131__partition_with_equals_on_leftB8nn190102INS_17_ClassicAlgPolicyEPPKvRU13block_pointerFbRKS3_S6_EEET0_SA_SA_T1_
+ __ZNSt3__132__partition_with_equals_on_rightB8nn190102INS_17_ClassicAlgPolicyEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERNS_6__lessIvvEEEENS_4pairIT0_bEESD_SD_T1_
+ __ZNSt3__132__partition_with_equals_on_rightB8nn190102INS_17_ClassicAlgPolicyEPPKvRU13block_pointerFbRKS3_S6_EEENS_4pairIT0_bEESB_SB_T1_
+ __ZNSt3__134__uninitialized_allocator_relocateB8nn190102INS_3pmr21polymorphic_allocatorIN14LaunchServices17BindingEvaluation15ExtendedBindingEEES5_EEvRT_PT0_SA_SA_
+ __ZNSt3__134__uninitialized_allocator_relocateB8nn190102INS_9allocatorIU6__weakP8LSRecordEES4_EEvRT_PT0_S9_S9_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8nn190102INS_3pmr21polymorphic_allocatorIN14LaunchServices17BindingEvaluation15ExtendedBindingEEENS_13move_iteratorINS_11__wrap_iterIPS5_EEEESB_S9_EET2_RT_T0_T1_SC_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8nn190102INS_9allocatorI26_FSInternetLocatorTypeInfoEEPKS2_S5_PS2_EET2_RT_T0_T1_S7_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8nn190102INS_9allocatorI9LSBindingEEPN14LaunchServices17BindingEvaluation15ExtendedBindingES7_PS2_EET2_RT_T0_T1_S9_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8nn190102INS_9allocatorIN14LaunchServices12OpenWithMenu10BundleInfoEEENS_21__tree_const_iteratorIS4_PNS_11__tree_nodeIS4_PvEElEESB_PS4_EET2_RT_T0_T1_SD_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8nn190102INS_9allocatorIN14LaunchServices19PrefsCapabilityInfoEEEPKS3_S6_PS3_EET2_RT_T0_T1_S8_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8nn190102INS_9allocatorINS_4pairIU8__strongP8NSStringU8__strongP10NSMenuItemEEEEPS9_SB_SB_EET2_RT_T0_T1_SC_
+ __ZNSt3__13pmr21polymorphic_allocatorIN14LaunchServices17BindingEvaluation15ExtendedBindingEE7destroyB8nn190102IS4_EEvPT_
+ __ZNSt3__13pmr21polymorphic_allocatorIN14LaunchServices17BindingEvaluation15ExtendedBindingEE8allocateB8nn190102Em
+ __ZNSt3__13pmr21polymorphic_allocatorIN14LaunchServices17BindingEvaluation15ExtendedBindingEE9constructB8nn190102IS4_JRKS4_EEEvPT_DpOT0_
+ __ZNSt3__13pmr21polymorphic_allocatorIN14LaunchServices17BindingEvaluation15ExtendedBindingEE9constructB8nn190102IS4_JRS4_EEEvPT_DpOT0_
+ __ZNSt3__13pmr21polymorphic_allocatorIPNS_16__hash_node_baseIPNS_11__hash_nodeIiPvEEEEE8allocateB8nn190102Em
+ __ZNSt3__13pmr21polymorphic_allocatorIPNS_16__hash_node_baseIPNS_11__hash_nodeIjPvEEEEE8allocateB8nn190102Em
+ __ZNSt3__14sortB8nn190102INS_11__wrap_iterIPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEEEvT_SA_
+ __ZNSt3__14sortB8nn190102INS_11__wrap_iterIPPKvEEU13block_pointerFbRKS3_S7_EEEvT_SA_T0_
+ __ZNSt3__14swapB8nn190102IN14LaunchServices12OpenWithMenu10BundleInfoEEENS_9enable_ifIXaasr21is_move_constructibleIT_EE5valuesr18is_move_assignableIS5_EE5valueEvE4typeERS5_S8_
+ __ZNSt3__14swapB8nn190102IN14LaunchServices17BindingEvaluation15ExtendedBindingEEENS_9enable_ifIXaasr21is_move_constructibleIT_EE5valuesr18is_move_assignableIS5_EE5valueEvE4typeERS5_S8_
+ __ZNSt3__15dequeIiNS_9allocatorIiEEE26__maybe_remove_front_spareB8nn190102Eb
+ __ZNSt3__16__findB8nn190102IPU6__weakP8LSRecordS4_DnNS_10__identityEEET_S6_T0_RKT1_RT2_
+ __ZNSt3__16removeB8nn190102INS_11__wrap_iterIPU6__weakP8LSRecordEEDnEET_S7_S7_RKT0_
+ __ZNSt3__16vectorI13LSBundleClassNS_9allocatorIS1_EEE11__vallocateB8nn190102Em
+ __ZNSt3__16vectorI13LSBundleClassNS_9allocatorIS1_EEE18__assign_with_sizeB8nn190102IPKS1_S7_EEvT_T0_l
+ __ZNSt3__16vectorI13LSBundleClassNS_9allocatorIS1_EEE18__assign_with_sizeB8nn190102IPS1_S6_EEvT_T0_l
+ __ZNSt3__16vectorI19ProcessSerialNumberNS_9allocatorIS1_EEE11__vallocateB8nn190102Em
+ __ZNSt3__16vectorI19ProcessSerialNumberNS_9allocatorIS1_EEE18__assign_with_sizeB8nn190102IPS1_S6_EEvT_T0_l
+ __ZNSt3__16vectorI9LSBindingNS_9allocatorIS1_EEE16__destroy_vectorclB8nn190102Ev
+ __ZNSt3__16vectorI9LSBindingNS_9allocatorIS1_EEE18__insert_with_sizeB8nn190102INS_11__wrap_iterIPN14LaunchServices17BindingEvaluation15ExtendedBindingEEESB_EENS6_IPS1_EENS6_IPKS1_EET_T0_l
+ __ZNSt3__16vectorI9LSBindingNS_9allocatorIS1_EEE22__base_destruct_at_endB8nn190102EPS1_
+ __ZNSt3__16vectorIN14LaunchServices12OpenWithMenu10BundleInfoENS_9allocatorIS3_EEE16__destroy_vectorclB8nn190102Ev
+ __ZNSt3__16vectorIN14LaunchServices12OpenWithMenu10BundleInfoENS_9allocatorIS3_EEE18__insert_with_sizeB8nn190102INS_21__tree_const_iteratorIS3_PNS_11__tree_nodeIS3_PvEElEESD_EENS_11__wrap_iterIPS3_EENSE_IPKS3_EET_T0_l
+ __ZNSt3__16vectorIN14LaunchServices12OpenWithMenu4ItemENS_9allocatorIS3_EEE11__vallocateB8nn190102Em
+ __ZNSt3__16vectorIN14LaunchServices12OpenWithMenu4ItemENS_9allocatorIS3_EEE16__destroy_vectorclB8nn190102Ev
+ __ZNSt3__16vectorIN14LaunchServices12OpenWithMenu4ItemENS_9allocatorIS3_EEE16__init_with_sizeB8nn190102IPS3_S8_EEvT_T0_m
+ __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS_3pmr21polymorphic_allocatorIS3_EEE11__vallocateB8nn190102Em
+ __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS_3pmr21polymorphic_allocatorIS3_EEE16__destroy_vectorclB8nn190102Ev
+ __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS_3pmr21polymorphic_allocatorIS3_EEE18__assign_with_sizeB8nn190102INS_13move_iteratorINS_11__wrap_iterIPS3_EEEESD_EEvT_T0_l
+ __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS_3pmr21polymorphic_allocatorIS3_EEE18__insert_with_sizeB8nn190102INS_11__wrap_iterIPS3_EESB_EESB_NS9_IPKS3_EET_T0_l
+ __ZNSt3__16vectorIN14LaunchServices30FeatureFlagPredicateEvaluation20FeatureFlagSpecifierENS_9allocatorIS3_EEE16__destroy_vectorclB8nn190102Ev
+ __ZNSt3__16vectorIN14LaunchServices30FeatureFlagPredicateEvaluation20FeatureFlagSpecifierENS_9allocatorIS3_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS3_RS5_EE
+ __ZNSt3__16vectorIN14LaunchServices5Types41EnumeratedTypeUnitOrDynamicTypeIdentifierENS_9allocatorIS3_EEE16__destroy_vectorclB8nn190102Ev
+ __ZNSt3__16vectorIN14LaunchServices5Types41EnumeratedTypeUnitOrDynamicTypeIdentifierENS_9allocatorIS3_EEE9push_backB8nn190102ERKS3_
+ __ZNSt3__16vectorINS_10shared_ptrIN14LaunchServices16PerThreadContextEEENS_9allocatorIS4_EEE16__destroy_vectorclB8nn190102Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN14LaunchServices16PerThreadContextEEENS_9allocatorIS4_EEE7__clearB8nn190102Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB8nn190102Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE7__clearB8nn190102Ev
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP10NSMenuItemEENS_9allocatorIS8_EEE11__vallocateB8nn190102Em
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP10NSMenuItemEENS_9allocatorIS8_EEE12emplace_backIJRU8__strongKS3_RS7_EEERS8_DpOT_
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP10NSMenuItemEENS_9allocatorIS8_EEE16__destroy_vectorclB8nn190102Ev
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP10NSMenuItemEENS_9allocatorIS8_EEE16__init_with_sizeB8nn190102IPS8_SD_EEvT_T0_m
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP10NSMenuItemEENS_9allocatorIS8_EEE22__base_destruct_at_endB8nn190102EPS8_
+ __ZNSt3__16vectorINS_4pairIjU8__strongP6NSUUIDEENS_9allocatorIS5_EEE16__destroy_vectorclB8nn190102Ev
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE11__vallocateB8nn190102Em
+ __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE11__vallocateB8nn190102Em
+ __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE16__destroy_vectorclB8nn190102Ev
+ __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE16__init_with_sizeB8nn190102IPKS2_S9_EEvT_T0_m
+ __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE16__init_with_sizeB8nn190102IPS3_S8_EEvT_T0_m
+ __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE18__insert_with_sizeB8nn190102IPKS2_S9_EENS_11__wrap_iterIPS3_EENSA_IPU6__weakKS2_EET_T0_l
+ __ZNSt3__16vectorIU8__strongP19LSApplicationRecordNS_9allocatorIS3_EEE16__destroy_vectorclB8nn190102Ev
+ __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEE16__destroy_vectorclB8nn190102Ev
+ __ZNSt3__16vectorIU8__strongU13block_pointerFvbP11_LSDatabaseP7NSErrorENS_9allocatorIS7_EEE16__destroy_vectorclB8nn190102Ev
+ __ZNSt3__16vectorIU8__strongU13block_pointerFvvENS_9allocatorIS3_EEE11__vallocateB8nn190102Em
+ __ZNSt3__16vectorIU8__strongU13block_pointerFvvENS_9allocatorIS3_EEE16__destroy_vectorclB8nn190102Ev
+ __ZNSt3__16vectorIU8__strongU13block_pointerFvvENS_9allocatorIS3_EEE16__init_with_sizeB8nn190102IPS3_S8_EEvT_T0_m
+ __ZNSt3__16vectorIU8__strongU13block_pointerFvvENS_9allocatorIS3_EEE9push_backB8nn190102ERU8__strongKS2_
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB8nn190102Em
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE11__vallocateB8nn190102Em
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE18__assign_with_sizeB8nn190102IPjS5_EEvT_T0_l
+ __ZNSt3__16vectorItNS_9allocatorItEEE11__vallocateB8nn190102Em
+ __ZNSt3__17__sort3B8nn190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEjT1_SC_SC_T0_
+ __ZNSt3__17__sort3B8nn190102INS_17_ClassicAlgPolicyERU13block_pointerFbRKPKvS5_EPS3_EEjT1_SA_SA_T0_
+ __ZNSt3__17__sort3B8nn190102INS_17_ClassicAlgPolicyERZ87+[LSApplicationRecord(UserActivity) applicationRecordsForUserActivityType:limit:error:]E3$_0PNS_4pairIjPK12LSBundleDataEEEEjT1_SA_SA_T0_
+ __ZNSt3__17__sort3B8nn190102INS_17_ClassicAlgPolicyERZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]E3$_1PjEEjT1_S5_S5_T0_
+ __ZNSt3__17__sort3B8nn190102INS_17_ClassicAlgPolicyERZL33_LSBundleCopyArchitectures_CommonPK12LSBundleDataP7NSArrayIP8NSStringEE3$_0P11LSSliceDataEEjT1_SE_SE_T0_
+ __ZNSt3__17__sort4B8nn190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEvT1_SC_SC_SC_T0_
+ __ZNSt3__17__sort4B8nn190102INS_17_ClassicAlgPolicyERU13block_pointerFbRKPKvS5_EPS3_EEvT1_SA_SA_SA_T0_
+ __ZNSt3__17__sort4B8nn190102INS_17_ClassicAlgPolicyERZ87+[LSApplicationRecord(UserActivity) applicationRecordsForUserActivityType:limit:error:]E3$_0PNS_4pairIjPK12LSBundleDataEEEEvT1_SA_SA_SA_T0_
+ __ZNSt3__17__sort4B8nn190102INS_17_ClassicAlgPolicyERZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]E3$_1PjEEvT1_S5_S5_S5_T0_
+ __ZNSt3__17__sort4B8nn190102INS_17_ClassicAlgPolicyERZL33_LSBundleCopyArchitectures_CommonPK12LSBundleDataP7NSArrayIP8NSStringEE3$_0P11LSSliceDataEEvT1_SE_SE_SE_T0_
+ __ZNSt3__17__sort5B8nn190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEvT1_SC_SC_SC_SC_T0_
+ __ZNSt3__17__sort5B8nn190102INS_17_ClassicAlgPolicyERU13block_pointerFbRKPKvS5_EPS3_EEvT1_SA_SA_SA_SA_T0_
+ __ZNSt3__18optionalI9LSBindingEaSB8nn190102IRKN14LaunchServices17BindingEvaluation15ExtendedBindingEvEERS2_OT_
+ __ZNSt3__18optionalI9LSBindingEaSB8nn190102IRS1_vEERS2_OT_
+ __ZNSt3__18optionalIN14LaunchServices12OpenWithMenu10BundleInfoEEaSB8nn190102IS3_vEERS4_OT_
+ __ZNSt3__18optionalIN14LaunchServices16BindingEvaluatorEEaSB8nn190102IS2_vEERS3_OT_
+ __ZNSt3__18optionalIN14LaunchServices30EligibilityPredicateEvaluation9PredicateEE7emplaceB8nn190102IJS3_EvEERS3_DpOT_
+ __ZNSt3__18optionalIN14LaunchServices30FeatureFlagPredicateEvaluation9PredicateEE7emplaceB8nn190102IJS3_EvEERS3_DpOT_
+ __ZNSt3__18optionalIU8__strongP7NSErrorEaSB8nn190102IRS3_vEERS4_OT_
+ __ZNSt3__19__advanceB8nn190102INS_21__tree_const_iteratorIN14LaunchServices12OpenWithMenu10BundleInfoEPNS_11__tree_nodeIS4_PvEElEEEEvRT_NS_15iterator_traitsISA_E15difference_typeENS_26bidirectional_iterator_tagE
+ __ZNSt3__19__sift_upB8nn190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEvT1_SC_OT0_NS_15iterator_traitsISC_E15difference_typeE
+ __ZNSt3__19__sift_upB8nn190102INS_17_ClassicAlgPolicyERU13block_pointerFbRKPKvS5_EPS3_EEvT1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
+ __ZNSt3__19allocatorIN14LaunchServices12OpenWithMenu10BundleInfoEE7destroyB8nn190102EPS3_
+ __ZNSt3__19allocatorIN14LaunchServices12OpenWithMenu10BundleInfoEE9constructB8nn190102IS3_JRKS3_EEEvPT_DpOT0_
+ __ZNSt3__19allocatorIN14LaunchServices12OpenWithMenu10BundleInfoEE9constructB8nn190102IS3_JS3_EEEvPT_DpOT0_
+ __ZNSt3__19allocatorIN14LaunchServices12OpenWithMenu4ItemEE7destroyB8nn190102EPS3_
+ __ZNSt3__19allocatorIN14LaunchServices12OpenWithMenu4ItemEE9constructB8nn190102IS3_JRS3_EEEvPT_DpOT0_
+ __ZNSt3__19allocatorIN14LaunchServices30FeatureFlagPredicateEvaluation20FeatureFlagSpecifierEE7destroyB8nn190102EPS3_
+ __ZNSt3__19allocatorINS_11__tree_nodeIN14LaunchServices12OpenWithMenu10BundleInfoEPvEEE9constructB8nn190102IS4_JRKS4_EEEvPT_DpOT0_
+ __ZNSt3__19basic_iosIcNS_11char_traitsIcEEE5imbueB8nn190102ERKNS_6localeE
+ __ZNSt3__1lsB8nn190102INS_11char_traitsIcEEEERNS_13basic_ostreamIcT_EES6_RKNS_8__iom_t4IcEE
+ __ZSt28__throw_bad_array_new_lengthB8nn190102v
+ __ZZL35enumerateProductPlatformKeySuffixesIU8__strongP12NSDictionaryIP8NSStringP11objc_objectEZ53-[_LSStringsFileContent subscriptLoctableWithLocale:]E3$_1ENSt3__18optionalIT_EES2_RKT0_E25platformThenProductSuffix
+ __ZZL35enumerateProductPlatformKeySuffixesIU8__strongP12NSDictionaryIP8NSStringP11objc_objectEZ53-[_LSStringsFileContent subscriptLoctableWithLocale:]E3$_1ENSt3__18optionalIT_EES2_RKT0_E25productThenPlatformSuffix
+ __ZZL35enumerateProductPlatformKeySuffixesIU8__strongP12NSDictionaryIP8NSStringP11objc_objectEZ53-[_LSStringsFileContent subscriptLoctableWithLocale:]E3$_1ENSt3__18optionalIT_EES2_RKT0_E9onceToken
+ __ZZL35enumerateProductPlatformKeySuffixesIU8__strongP8NSStringZ60-[_LSStringsFileContent _queryLoadedPlist:forRawKey:locale:]E3$_2ENSt3__18optionalIT_EES1_RKT0_E25platformThenProductSuffix
+ __ZZL35enumerateProductPlatformKeySuffixesIU8__strongP8NSStringZ60-[_LSStringsFileContent _queryLoadedPlist:forRawKey:locale:]E3$_2ENSt3__18optionalIT_EES1_RKT0_E25productThenPlatformSuffix
+ __ZZL35enumerateProductPlatformKeySuffixesIU8__strongP8NSStringZ60-[_LSStringsFileContent _queryLoadedPlist:forRawKey:locale:]E3$_2ENSt3__18optionalIT_EES1_RKT0_E9onceToken
+ __ZZL35enumerateProductPlatformKeySuffixesIU8__strongP8NSStringZL46checkPlatformKeysForKeysForSubscriptedLoctableP5NSSetIS1_EP12NSDictionaryIS1_P11objc_objectEE3$_0ENSt3__18optionalIT_EES1_RKT0_E25platformThenProductSuffix
+ __ZZL35enumerateProductPlatformKeySuffixesIU8__strongP8NSStringZL46checkPlatformKeysForKeysForSubscriptedLoctableP5NSSetIS1_EP12NSDictionaryIS1_P11objc_objectEE3$_0ENSt3__18optionalIT_EES1_RKT0_E25productThenPlatformSuffix
+ __ZZL35enumerateProductPlatformKeySuffixesIU8__strongP8NSStringZL46checkPlatformKeysForKeysForSubscriptedLoctableP5NSSetIS1_EP12NSDictionaryIS1_P11objc_objectEE3$_0ENSt3__18optionalIT_EES1_RKT0_E9onceToken
+ ___35-[_LSDefaults currentSchemaVersion]_block_invoke
+ ___47-[LSBuiltinPluginRegistrant runWithCompletion:]_block_invoke
+ ___47-[LSBuiltinPluginRegistrant runWithCompletion:]_block_invoke_2
+ ___47-[LSBuiltinPluginRegistrant runWithCompletion:]_block_invoke_3
+ ___47-[LSByURLBundleUnregistrant runWithCompletion:]_block_invoke
+ ___47-[LSByURLPluginUnregistrant runWithCompletion:]_block_invoke
+ ___52-[LSBuiltinApplicationRegistrant runWithCompletion:]_block_invoke
+ ___52-[LSBuiltinApplicationRegistrant runWithCompletion:]_block_invoke_2
+ ___57-[LSRegistrantServerStrategy runSyncBlockInWriteContext:]_block_invoke
+ ___61-[LSSystemExtensionPointRefreshRegistrant runWithCompletion:]_block_invoke
+ ___61-[LSSystemExtensionPointRefreshRegistrant runWithCompletion:]_block_invoke_2
+ ___74-[LSMIResultRegistrantTrueDatabaseContext enumerateExtensionPointRecords:]_block_invoke
+ ___82-[LSMIResultRegistrantTrueDatabaseContext containerizedBundleExistsForIdentifier:]_block_invoke
+ ___98-[LSMIResultRegistrantTrueDatabaseContext unregisterNonBundledExtensionPointWithIdentifier:error:]_block_invoke
+ ___LSClientSideRegisterAsReconnectionHelper_block_invoke.4.cold.1
+ ___LSClientSideRegisterAsReconnectionHelper_block_invoke_2.cold.1
+ ___LSClientSideRegisterAsReconnectionHelper_block_invoke_2.cold.2
+ ___LSDefaultsAllowClientSideDatabaseCreation_block_invoke.cold.1
+ ___LSDefaultsInXCTestRigInsecure_block_invoke.cold.1
+ ___LSGetCPUArchitecture_block_invoke.cold.1
+ ___LSGetProductNameSuffix_block_invoke.cold.1
+ ___LSIsCurrentProcessSandboxed_block_invoke.cold.1
+ ___LSServer_SyncWithMobileInstallation_block_invoke.837
+ ___LSServer_SyncWithMobileInstallation_block_invoke.839
+ ___LSServer_SyncWithMobileInstallation_block_invoke.851
+ ___LSServer_SyncWithMobileInstallation_block_invoke.851.cold.1
+ ___LSServer_SyncWithMobileInstallation_block_invoke.851.cold.2
+ ___LSServer_SyncWithMobileInstallation_block_invoke.852
+ ___LSServer_SyncWithMobileInstallation_block_invoke.855
+ ___LSServer_SyncWithMobileInstallation_block_invoke_2.856
+ ___Z24clientIsAllowedToConnectPK14__CFDictionary_block_invoke.cold.3
+ ___ZL16getPropertyTablev_block_invoke.cold.1
+ ___ZL16getPropertyTablev_block_invoke.cold.10
+ ___ZL16getPropertyTablev_block_invoke.cold.11
+ ___ZL16getPropertyTablev_block_invoke.cold.12
+ ___ZL16getPropertyTablev_block_invoke.cold.13
+ ___ZL16getPropertyTablev_block_invoke.cold.14
+ ___ZL16getPropertyTablev_block_invoke.cold.15
+ ___ZL16getPropertyTablev_block_invoke.cold.2
+ ___ZL16getPropertyTablev_block_invoke.cold.3
+ ___ZL16getPropertyTablev_block_invoke.cold.4
+ ___ZL16getPropertyTablev_block_invoke.cold.5
+ ___ZL16getPropertyTablev_block_invoke.cold.6
+ ___ZL16getPropertyTablev_block_invoke.cold.7
+ ___ZL16getPropertyTablev_block_invoke.cold.8
+ ___ZL16getPropertyTablev_block_invoke.cold.9
+ ___ZL25createListeningConnectionv_block_invoke.32.cold.2
+ ___ZL27GetiCloudDriveDirectoryPathv_block_invoke.cold.1
+ ___ZL27_LSDNCGetExtensionSkeletonsP9LSContextRP13USpoofChecker_block_invoke.241
+ ___ZL27_LSDNCGetExtensionSkeletonsP9LSContextRP13USpoofChecker_block_invoke.245
+ ___ZL28connectionCacheHasConnectioni_block_invoke.cold.1
+ ___ZL34_LSDatabasePostChangeNotificationsP11_LSDatabase_block_invoke.cold.1
+ ___ZL41lsEnvironmentVariableRequiresSecureLaunchP12NSDictionary_block_invoke.cold.1
+ ___ZL51shouldThisProcessLogAboutBeingUnableToConnectToCSUIv_block_invoke.cold.1
+ ___ZN13LSHandlerPref4SaveEP11_LSDatabase_block_invoke.cold.1
+ ___ZN13VolumeBinding20GetSystemIconsBundleEv_block_invoke.cold.1
+ ___ZN14LaunchServices17BindingEvaluationL27insertSelectedDeveloperToolERNS0_5StateE_block_invoke.224
+ ___ZN14LaunchServices7BundlesL7displayEP9LSContextjjPNS_10DumpWriterE_block_invoke.376
+ ___ZN14LaunchServices7BundlesL7displayEP9LSContextjjPNS_10DumpWriterE_block_invoke.663
+ ___ZN14LaunchServices7BundlesL7displayEP9LSContextjjPNS_10DumpWriterE_block_invoke_2.665
+ ___ZN14LaunchServices7BundlesL7displayEP9LSContextjjPNS_10DumpWriterE_block_invoke_3.666
+ ___ZN18LSSharedMemoryPage16CopyForSessionIDE11LSSessionIDb_block_invoke.5.cold.2
+ ___ZN18LSSharedMemoryPage16CopyForSessionIDE11LSSessionIDb_block_invoke.9.cold.1
+ ___ZN18LSSharedMemoryPage16CopyForSessionIDE11LSSessionIDb_block_invoke.9.cold.2
+ ___ZN18LSSharedMemoryPage16CopyForSessionIDE11LSSessionIDb_block_invoke.cold.1
+ ___ZN18LSSharedMemoryPage16CopyForSessionIDE11LSSessionIDb_block_invoke.cold.2
+ ___ZN18LSSharedMemoryPage16CopyForSessionIDE11LSSessionIDb_block_invoke.cold.3
+ ___ZN18LSSharedMemoryPage16CopyForSessionIDE11LSSessionIDb_block_invoke_2.cold.2
+ ___ZN18LSSharedMemoryPage33InvalidateCachedSharedMemoryPagesE11LSSessionID_block_invoke.cold.1
+ ___ZN18LSSharedMemoryPage33InvalidateCachedSharedMemoryPagesE11LSSessionID_block_invoke.cold.2
+ ___ZN22LSNotificationReceiver18CreateNotificationEPK13__CFAllocator11LSSessionIDP16dispatch_queue_sU13block_pointerFv18LSNotificationCodedPKvPK7__LSASNS3_S8_E_block_invoke.cold.2
+ ___ZN22LSNotificationReceiver18DeleteNotificationEPKv_block_invoke.cold.1
+ ___ZN22LSNotificationReceiver20ReEstablishListenersEb_block_invoke.cold.1
+ ___ZN22LSNotificationReceiver20ReEstablishListenersEb_block_invoke.cold.2
+ ___ZN22LSNotificationReceiver23ReleaseAllNotificationsEv_block_invoke.cold.1
+ ___ZN22LSNotificationReceiver23ReleaseAllNotificationsEv_block_invoke.cold.2
+ ___ZN22LSNotificationReceiver23getNotificationListenerEb_block_invoke.cold.1
+ ___ZN22LSNotificationReceiver23getNotificationListenerEb_block_invoke_2.cold.1
+ ___ZN22LSNotificationReceiver32CopyNotificationInformationForIDEPKv_block_invoke.cold.1
+ ___ZN26LSClientToServerConnection21setupServerConnectionEiPK14__CFDictionary_block_invoke.35
+ ___ZN26LSClientToServerConnection21setupServerConnectionEiPK14__CFDictionary_block_invoke.35.cold.1
+ ____ZL26searchForUnsafeLegacyClaimP9LSContextjjPK14__CFDictionary_block_invoke
+ ____ZL35enumerateProductPlatformKeySuffixesIU8__strongP12NSDictionaryIP8NSStringP11objc_objectEZ53-[_LSStringsFileContent subscriptLoctableWithLocale:]E3$_1ENSt3__18optionalIT_EES2_RKT0__block_invoke
+ ____ZL35enumerateProductPlatformKeySuffixesIU8__strongP8NSStringZ60-[_LSStringsFileContent _queryLoadedPlist:forRawKey:locale:]E3$_2ENSt3__18optionalIT_EES1_RKT0__block_invoke
+ ____ZL35enumerateProductPlatformKeySuffixesIU8__strongP8NSStringZL46checkPlatformKeysForKeysForSubscriptedLoctableP5NSSetIS1_EP12NSDictionaryIS1_P11objc_objectEE3$_0ENSt3__18optionalIT_EES1_RKT0__block_invoke
+ ____ZL36appMayTreatUnclaimedDocumentUnsafelyP9LSContextjPK12LSBundleDataP6FSNode_block_invoke
+ ____ZL36appMayTreatUnclaimedDocumentUnsafelyP9LSContextjPK12LSBundleDataP6FSNode_block_invoke_2
+ ___block_descriptor_114_ea8_32s40s48s56s64s72s80s88s96s104bs_e48_v16?0"<LSRegistrantDatabaseContextProviding>"8l
+ ___block_descriptor_40_e111_v24?0r^{LSDefaultAppCategoryInfo=Q^{__CFString}^{__CFString}Q^?^{LSDefaultAppCategorySubordinateClaim}QB}8^B16l
+ ___block_descriptor_40_ea8_32r_e18_v16?0"NSString"8l
+ ___block_descriptor_40_ea8_32r_e54_v28?0B8"<LSRegistrantDatabaseContext>"12"NSError"20l
+ ___block_descriptor_40_ea8_32s_e36_v24?0"LSExtensionPointRecord"8^B16l
+ ___block_descriptor_44_ea8_32s_e54_v28?0B8"<LSRegistrantDatabaseContext>"12"NSError"20l
+ ___block_descriptor_48_ea8_32s40r_e54_v28?0B8"<LSRegistrantDatabaseContext>"12"NSError"20l
+ ___block_descriptor_52_ea8_32r_e59_v40?0^{__CFURLEnumerator=}8^{__CFURL=}16^{__CFError=}24*32l
+ ___block_descriptor_52_ea8_32s40r_e54_v28?0B8"<LSRegistrantDatabaseContext>"12"NSError"20l
+ ___block_descriptor_52_ea8_32s40s_e54_v28?0B8"<LSRegistrantDatabaseContext>"12"NSError"20l
+ ___block_descriptor_56_ea8_32s40bs_e19_v32?0I8r^v12I20*24l
+ ___block_descriptor_56_ea8_32s40r48r_e48_v16?0"<LSRegistrantDatabaseContextProviding>"8l
+ ___block_descriptor_64_ea8_32s40r48r56r_e48_v16?0"<LSRegistrantDatabaseContextProviding>"8l
+ ___block_descriptor_64_ea8_32s40s48r56r_e48_v16?0"<LSRegistrantDatabaseContextProviding>"8l
+ ___block_descriptor_80_ea8_32s40s48r56r64r72r_e32_v24?0"<EXExtensionPoint>"8^B16l
+ ___block_descriptor_80_ea8_32s40s48r56r64r72r_e48_v16?0"<LSRegistrantDatabaseContextProviding>"8l
+ ___block_descriptor_80_ea8_32s40s48s56s64r72r_e48_v16?0"<LSRegistrantDatabaseContextProviding>"8l
+ ___block_descriptor_88_ea8_32s40s48s56s64s72bs80r_e48_v16?0"<LSRegistrantDatabaseContextProviding>"8l
+ ___copy_helper_block_ea8_32s40s48r56r64r72r
+ ___copy_helper_block_ea8_32s40s48s56s64r72r
+ ___copy_helper_block_ea8_32s40s48s56s64s72b80r
+ ___destroy_helper_block_ea8_32s40s48r56r64r72r
+ ___destroy_helper_block_ea8_32s40s48s56s64s72s80r
+ ___uninstallMIBundlesNotInSet_block_invoke.cold.1
+ __block_descriptor_tmp.50
+ __block_descriptor_tmp.54
+ __block_descriptor_tmp.57
+ __block_descriptor_tmp.61
+ __block_descriptor_tmp.65
+ __block_descriptor_tmp.72
+ __block_descriptor_tmp.78
+ __block_literal_global.211
+ __block_literal_global.213
+ __block_literal_global.223
+ __block_literal_global.224
+ __block_literal_global.226
+ __block_literal_global.228
+ __block_literal_global.232
+ __block_literal_global.245
+ __block_literal_global.278
+ __block_literal_global.283
+ __block_literal_global.296
+ __block_literal_global.357
+ __block_literal_global.406
+ __block_literal_global.431
+ __block_literal_global.435
+ __block_literal_global.438
+ __block_literal_global.52
+ __block_literal_global.564
+ __block_literal_global.583
+ __block_literal_global.595
+ __block_literal_global.602
+ __block_literal_global.63
+ __block_literal_global.64
+ __block_literal_global.67
+ __block_literal_global.71
+ __block_literal_global.74
+ __block_literal_global.858
+ __block_literal_global.922
+ __block_literal_global.951
+ __block_literal_global.953
+ __block_literal_global.969
+ _log.cold.1
+ _objc_msgSend$clientIsEntitledForEmbeddedRegistrationOperations
+ _objc_msgSend$containerizedBundleExistsForIdentifier:
+ _objc_msgSend$contextPointer
+ _objc_msgSend$enumerateExtensionPointRecords:
+ _objc_msgSend$enumerateSystemEXExtensionPoints:
+ _objc_msgSend$findApplicationBundleAtNode:error:
+ _objc_msgSend$findPluginAtNode:error:
+ _objc_msgSend$initWithWindowOpenDates:refreshDate:defaultForCategory:
+ _objc_msgSend$isOpenWindowGroupFull
+ _objc_msgSend$newestWindowOpenDate
+ _objc_msgSend$oldestWindowOpenDate
+ _objc_msgSend$pluginDataForPlugin:
+ _objc_msgSend$preUnregistrationContextForBundleUnit:context:
+ _objc_msgSend$registerBundleNodeReinitializingContext:inBundleContainer:installDictionary:personasWithAttributes:error:
+ _objc_msgSend$registerNonBundledExtensionPointWithIdentifier:platform:SDKDict:url:error:
+ _objc_msgSend$registerPluginNodeReinitializingContext:installDictionary:existingPlugin:error:
+ _objc_msgSend$unregisterApplicationBundleByUnit:error:
+ _objc_msgSend$unregisterNonBundledExtensionPointWithIdentifier:error:
+ _objc_msgSend$unregisterPluginBundleByUnit:error:
+ _objc_msgSend$updatedEntryRotatingInWindowOpenDate:refreshDate:defaultForCategory:
+ _objc_msgSend$updatedEntryWithRefreshDate:defaultForCategory:
+ _objc_msgSend$windowOpenDates
+ _os_variant_is_darwinos
+ currentSchemaVersion.sOnce
+ currentSchemaVersion.sResult
+ mutateSubscriberCountForNotificationName.cold.1
+ preferredLocalizations.once.221
+ registerApplicationWithDictionary.cold.1
+ registerApplicationWithDictionary.cold.2
- -[LSDefaultApplicationQueryEntry windowOpenDate]
- -[LSMIRegistrantServerStrategy beginModificationOperation]
- -[LSMIRegistrantServerStrategy endModificationOperation]
- -[LSMIRegistrantServerStrategy flushModificationState]
- -[LSMIRegistrantServerStrategy notificationJournallerForBundleIdentifier:registeringPlaceholder:]
- -[LSMIRegistrantServerStrategy preUnregistrationContextForBundleIdentifier:]
- -[LSMIRegistrantServerStrategy runSyncBlockInWriteContext:]
- -[LSMIResultRegistrantTrueDatabaseContext findOrRegisterContainerizedNodeReinitializingContext:installDictionary:personasWithAttributes:error:]
- -[_LSDModifyClient clientIsEntitledForPostInstallationOperations]
- GCC_except_table148
- GCC_except_table186
- GCC_except_table187
- GCC_except_table190
- GCC_except_table204
- GCC_except_table241
- GCC_except_table258
- GCC_except_table261
- GCC_except_table321
- GCC_except_table324
- OBJC_IVAR_$_LSDefaultApplicationQueryEntry._windowOpenDate
- _LSCopyApplicationArrayInFrontToBackOrder.cold.1
- _LSCopyApplicationArrayInFrontToBackOrder.cold.2
- _LSCopyApplicationInformation.cold.1
- _LSDefaultAppCategoryGetInfoForPreferenceSet
- _LSKillApplication.cold.1
- _LSKillApplication.cold.2
- _LSScheduleNotificationOnQueueWithBlock.cold.1
- _LSSetApplicationInformation.cold.1
- _OBJC_CLASS_$_LSMIRegistrantServerStrategy
- _OBJC_METACLASS_$_LSMIRegistrantServerStrategy
- _ZL20CopyApplicationArray11LSSessionIDbPPK9__CFArrayPj.cold.1
- _ZL20CopyApplicationArray11LSSessionIDbPPK9__CFArrayPj.cold.2
- _ZL20CopyApplicationArray11LSSessionIDbPPK9__CFArrayPj.cold.3
- _ZL45_LSDatabaseCreateSnapshotAgainstAccessContextP11_LSDatabaseP22__CSStoreAccessContextPU15__autoreleasingP7NSError.cold.1
- __48-[LSDatabaseBuilder createAndSeedLocalDatabase:]_block_invoke_2.2
- __54-[LSDatabaseBuilder scanAndRegisterSpotlightContents:]_block_invoke.34
- __68-[LSApplicationWorkspaceRemoteObserver applicationInstallsDidStart:]_block_invoke.653
- __Block_byref_object_copy_.325
- __Block_byref_object_copy_.336
- __Block_byref_object_copy_.829
- __Block_byref_object_copy_.978
- __Block_byref_object_dispose_.326
- __Block_byref_object_dispose_.337
- __Block_byref_object_dispose_.830
- __Block_byref_object_dispose_.979
- __JLIsRuntimeInstalledFunc
- __JLRequestRuntimeInstallFunc
- __OBJC_$_INSTANCE_METHODS_LSMIRegistrantServerStrategy
- __OBJC_$_PROP_LIST_LSMIRegistrantServerStrategy
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LSMIResultRegistrantDatabaseContext
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LSMIResultRegistrantDatabaseContextProviding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LSMIResultRegistrantStrategy
- __OBJC_$_PROTOCOL_METHOD_TYPES_LSMIResultRegistrantDatabaseContext
- __OBJC_$_PROTOCOL_METHOD_TYPES_LSMIResultRegistrantDatabaseContextProviding
- __OBJC_$_PROTOCOL_METHOD_TYPES_LSMIResultRegistrantStrategy
- __OBJC_$_PROTOCOL_REFS_LSMIResultRegistrantDatabaseContext
- __OBJC_$_PROTOCOL_REFS_LSMIResultRegistrantDatabaseContextProviding
- __OBJC_$_PROTOCOL_REFS_LSMIResultRegistrantStrategy
- __OBJC_CLASS_PROTOCOLS_$_LSMIRegistrantServerStrategy
- __OBJC_CLASS_RO_$_LSMIRegistrantServerStrategy
- __OBJC_LABEL_PROTOCOL_$_LSMIResultRegistrantDatabaseContext
- __OBJC_LABEL_PROTOCOL_$_LSMIResultRegistrantDatabaseContextProviding
- __OBJC_LABEL_PROTOCOL_$_LSMIResultRegistrantStrategy
- __OBJC_METACLASS_RO_$_LSMIRegistrantServerStrategy
- __OBJC_PROTOCOL_$_LSMIResultRegistrantDatabaseContext
- __OBJC_PROTOCOL_$_LSMIResultRegistrantDatabaseContextProviding
- __OBJC_PROTOCOL_$_LSMIResultRegistrantStrategy
- __ZGVZ39-[_LSExceptions applyToInfoDictionary:]E9mergeKeys
- __ZGVZL17GetQuarantineTypejE15quarantineTypes
- __ZGVZL24once_createPropertyTablevE18baseDependencyKeys
- __ZGVZL24once_createPropertyTablevE19typeDescriptionKeys
- __ZGVZL24once_createPropertyTablevE21bindingDependencyKeys
- __ZGVZL24once_createPropertyTablevE23genericSafeApertureKeys
- __ZGVZL24once_createPropertyTablevE24volLocNameDependencyKeys
- __ZGVZL24once_createPropertyTablevE25canSetHiddenExtensionKeys
- __ZGVZL24once_createPropertyTablevE25distinctLocalizedNameKeys
- __ZGVZL24once_createPropertyTablevE27appCapabilityDependencyKeys
- __ZGVZL24once_createPropertyTablevE27appCategoriesDependencyKeys
- __ZGVZL24once_createPropertyTablevE27architecturesDependencyKeys
- __ZGVZL24once_createPropertyTablevE27isApplicationDependencyKeys
- __ZGVZL24once_createPropertyTablevE27strongBindingDependencyKeys
- __ZGVZL24once_createPropertyTablevE27volQuarantineDependencyKeys
- __ZGVZL24once_createPropertyTablevE28hiddenBySystemDependencyKeys
- __ZGVZL24once_createPropertyTablevE33canSetStrongBindingDependencyKeys
- __ZGVZL49_LSCopyApplicationInformationItemFromSharedMemoryPK20__LSSharedMemoryPagePK7__LSASNPKvPS6_E50sApplicationInformationRetrievableFromSharedMemory
- __ZGVZL53_LSCopyMetaApplicationInformationItemFromSharedMemoryPK20__LSSharedMemoryPagePKvRbE43sMetaInformationRetrievableFromSharedMemory
- __ZGVZL9getLibIDsvE7klibIDs
- __ZGVZN14LaunchServices17BindingEvaluationL12runEvaluatorERNS0_5StateEPU15__autoreleasingP7NSErrorE7options
- __ZGVZN17QuarantineEventDB18setEventPropertiesEPK14__CFDictionaryE8propKeys
- __ZGVZZ65+[_LSTrustedSignatureDatabase(Database) scheduleDatabaseTrimming]EUb_E8interval
- __ZL20sApplicationInfoLock
- __ZL24sApplicationInfoLockOnce
- __ZL24sOurNormalizedPSNLowHalf
- __ZL33sCachedApplicationInformationOnce
- __ZL35softLinkLSSharedFileListSetProperty
- __ZL36sCurrentApplicationHasSignalledReady
- __ZL36softLinkLSSharedFileListCopyProperty
- __ZL36softLinkLSSharedFileListCopySnapshot
- __ZL40getkLSSharedFileListRecentItemsMaxAmount
- __ZL40softLink_LSSharedFileListItemCopyBinding
- __ZL41softLinkLSSharedFileListItemCopyAliasData
- __ZL42sBringApplicationForwardAtSignalTimeASNRef
- __ZL43softLinkLSSharedFileListItemCopyDisplayName
- __ZL44softLinkLSSharedFileListItemCopyBookmarkData
- __ZN14LaunchServices17BindingEvaluationL14compareVendorsERNS0_5StateERKNS0_15ExtendedBindingES5_
- __ZN14LaunchServices19URLPropertyProvider5StateD1Ev
- __ZNK14LaunchServices17BindingEvaluation5State19inXCTestRigInsecureEv
- __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB8nn180100INS_13move_iteratorINS_11__wrap_iterIPN14LaunchServices17BindingEvaluation15ExtendedBindingEEEEESB_S9_EENS_4pairIT_T1_EESD_T0_SE_
- __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB8nn180100INS_21__tree_const_iteratorIN14LaunchServices12OpenWithMenu10BundleInfoEPNS_11__tree_nodeIS7_PvEElEESC_PS7_EENS_4pairIT_T1_EESF_T0_SG_
- __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB8nn180100IPN14LaunchServices17BindingEvaluation15ExtendedBindingES7_P9LSBindingEENS_4pairIT_T1_EESB_T0_SC_
- __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB8nn180100IPN14LaunchServices17BindingEvaluation15ExtendedBindingES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
- __ZNKSt3__111__move_loopINS_17_ClassicAlgPolicyEEclB8nn180100INS_16reverse_iteratorIPN14LaunchServices12OpenWithMenu10BundleInfoEEES9_NS4_INS_11__wrap_iterIS8_EEEEEENS_4pairIT_T1_EESE_T0_SF_
- __ZNKSt3__111__move_loopINS_17_ClassicAlgPolicyEEclB8nn180100IP9LSBindingS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
- __ZNKSt3__111__move_loopINS_17_ClassicAlgPolicyEEclB8nn180100IPN14LaunchServices12OpenWithMenu10BundleInfoES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
- __ZNKSt3__111__move_loopINS_17_ClassicAlgPolicyEEclB8nn180100IPN14LaunchServices17BindingEvaluation15ExtendedBindingES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
- __ZNKSt3__111__move_loopINS_17_ClassicAlgPolicyEEclB8nn180100IPU6__weakP8LSRecordS7_S7_EENS_4pairIT_T1_EES9_T0_SA_
- __ZNKSt3__114default_deleteIN14LaunchServices12OpenWithMenu5StateEEclB8nn180100EPS3_
- __ZNKSt3__120__move_backward_loopINS_17_ClassicAlgPolicyEEclB8nn180100IP9LSBindingS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
- __ZNKSt3__120__move_backward_loopINS_17_ClassicAlgPolicyEEclB8nn180100IPN14LaunchServices12OpenWithMenu10BundleInfoES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
- __ZNKSt3__120__move_backward_loopINS_17_ClassicAlgPolicyEEclB8nn180100IPN14LaunchServices17BindingEvaluation15ExtendedBindingES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
- __ZNKSt3__120__move_backward_loopINS_17_ClassicAlgPolicyEEclB8nn180100IPU6__weakP8LSRecordS7_S7_EENS_4pairIT_T1_EES9_T0_SA_
- __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8nn180100EPKvm
- __ZNKSt3__16__lessIvvEclB8nn180100INS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES8_EEbRKT_RKT0_
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8nn180100ERKS6_S9_
- __ZNSt3__110__function12__value_funcIFP11objc_objectS3_P7NSErrorEED2B8nn180100Ev
- __ZNSt3__110__function12__value_funcIFbP11objc_objectEED2B8nn180100Ev
- __ZNSt3__110unique_ptrIA_PNS_16__hash_node_baseIPNS_11__hash_nodeIiPvEEEENS_25__bucket_list_deallocatorINS_3pmr21polymorphic_allocatorIS7_EEEEED2B8nn180100Ev
- __ZNSt3__110unique_ptrIA_PNS_16__hash_node_baseIPNS_11__hash_nodeIjPvEEEENS_25__bucket_list_deallocatorINS_3pmr21polymorphic_allocatorIS7_EEEEED2B8nn180100Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS_13unordered_mapIjbNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjbEEEEEEEEPvEENS_22__hash_node_destructorINS8_ISG_EEEEE5resetB8nn180100EPSG_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEEPvEENS_22__hash_node_destructorINS8_ISD_EEEEE5resetB8nn180100EPSD_
- __ZNSt3__110unique_ptrINS_11__tree_nodeIN14LaunchServices12OpenWithMenu10BundleInfoEPvEENS_22__tree_node_destructorINS_9allocatorIS6_EEEEE5resetB8nn180100EPS6_
- __ZNSt3__111__find_implB8nn180100IPU6__weakP8LSRecordS4_DnNS_10__identityEEET_S6_T0_RKT1_RT2_
- __ZNSt3__111__sift_downB8nn180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEvT1_OT0_NS_15iterator_traitsISC_E15difference_typeESC_
- __ZNSt3__111__sift_downB8nn180100INS_17_ClassicAlgPolicyERU13block_pointerFbRKPKvS5_EPS3_EEvT1_OT0_NS_15iterator_traitsISA_E15difference_typeESA_
- __ZNSt3__111__sift_downB8nn180100INS_17_ClassicAlgPolicyERZN14LaunchServices17BindingEvaluationL4sortERNS3_5StateEE3$_0NS_11__wrap_iterIPNS3_15ExtendedBindingEEEEEvT1_OT0_NS_15iterator_traitsISC_E15difference_typeESC_
- __ZNSt3__112__destroy_atB8nn180100IN14LaunchServices12OpenWithMenu10BundleInfoELi0EEEvPT_
- __ZNSt3__112__destruct_n9__processB8nn180100IN14LaunchServices12OpenWithMenu10BundleInfoEEEvPT_NS_17integral_constantIbLb0EEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_S7_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S7_SC_SA_Lb1EEENS_9allocatorIS7_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS7_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP27OpaqueMappedResourceFileRefU8__strongP6NSDataEENS_22__unordered_map_hasherIS3_S7_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S7_SC_SA_Lb1EEENS_9allocatorIS7_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS7_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIiP8os_log_sEENS_22__unordered_map_hasherIiS4_NS_4hashIiEENS_8equal_toIiEELb1EEENS_21__unordered_map_equalIiS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_performB8nn180100EPNS_11__hash_nodeIS4_PvEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIiP8os_log_sEENS_22__unordered_map_hasherIiS4_NS_4hashIiEENS_8equal_toIiEELb1EEENS_21__unordered_map_equalIiS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_prepareB8nn180100EmRS4_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP6FSNodeEENS_22__unordered_map_hasherIjS5_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS5_SA_S8_Lb1EEENS_9allocatorIS5_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS5_PvEEEE
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn180100Emc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn180100ILi0EEEPKc
- __ZNSt3__113__tree_removeB8nn180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__113unordered_mapIPK20LSExtensionPointDatajZ27_LSEnumerateExtensionPointsE30_LSExtensionPointCxxComparatorS4_NS_9allocatorINS_4pairIKS3_jEEEEED1B8nn180100Ev
- __ZNSt3__114__construct_atB8nn180100IN14LaunchServices12OpenWithMenu10BundleInfoEJS3_EPS3_EEPT_S6_DpOT0_
- __ZNSt3__114__split_bufferI9LSBindingRNS_9allocatorIS1_EEE17__destruct_at_endB8nn180100EPS1_
- __ZNSt3__114__split_bufferI9LSBindingRNS_9allocatorIS1_EEE9push_backB8nn180100ERKS1_
- __ZNSt3__114__split_bufferIN14LaunchServices12OpenWithMenu10BundleInfoERNS_9allocatorIS3_EEE5clearB8nn180100Ev
- __ZNSt3__114__split_bufferIN14LaunchServices12OpenWithMenu4ItemERNS_9allocatorIS3_EEE5clearB8nn180100Ev
- __ZNSt3__114__split_bufferIN14LaunchServices17BindingEvaluation15ExtendedBindingERNS_3pmr21polymorphic_allocatorIS3_EEE5clearB8nn180100Ev
- __ZNSt3__114__split_bufferIN14LaunchServices17BindingEvaluation15ExtendedBindingERNS_3pmr21polymorphic_allocatorIS3_EEE9push_backB8nn180100ERKS3_
- __ZNSt3__114__split_bufferIN14LaunchServices30FeatureFlagPredicateEvaluation20FeatureFlagSpecifierERNS_9allocatorIS3_EEE5clearB8nn180100Ev
- __ZNSt3__114__split_bufferINS_10shared_ptrIN14LaunchServices16PerThreadContextEEERNS_9allocatorIS4_EEE5clearB8nn180100Ev
- __ZNSt3__114__split_bufferINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERNS4_IS6_EEE17__destruct_at_endB8nn180100EPS6_
- __ZNSt3__114__split_bufferINS_4pairIU8__strongP8NSStringU8__strongP10NSMenuItemEERNS_9allocatorIS8_EEE17__destruct_at_endB8nn180100EPS8_
- __ZNSt3__116__insertion_sortB8nn180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEvT1_SC_T0_
- __ZNSt3__116__insertion_sortB8nn180100INS_17_ClassicAlgPolicyERU13block_pointerFbRKPKvS5_EPS3_EEvT1_SA_T0_
- __ZNSt3__116__insertion_sortB8nn180100INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRKN14LaunchServices12OpenWithMenu10BundleInfoES6_ENS_11__wrap_iterIPS4_EEEEvT1_SE_T0_
- __ZNSt3__116__pad_and_outputB8nn180100IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__116__rotate_forwardB8nn180100INS_17_ClassicAlgPolicyENS_11__wrap_iterIPN14LaunchServices12OpenWithMenu10BundleInfoEEEEET0_S8_S8_S8_
- __ZNSt3__117__floyd_sift_downB8nn180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEET1_SC_OT0_NS_15iterator_traitsISC_E15difference_typeE
- __ZNSt3__117__floyd_sift_downB8nn180100INS_17_ClassicAlgPolicyERU13block_pointerFbRKPKvS5_EPS3_EET1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
- __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8nn180100Ev
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorI11LSSliceDataEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorI13LSBundleClassEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorI13LSPersonaTypeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorI19ProcessSerialNumberEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorI23os_eligibility_answer_tEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorI8_NSRangeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorI9LSBindingEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorIN14LaunchServices12OpenWithMenu10BundleInfoEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorIN14LaunchServices12OpenWithMenu4ItemEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorIN14LaunchServices19URLPropertyProvider12FilePropertyEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorIN14LaunchServices30FeatureFlagPredicateEvaluation20FeatureFlagSpecifierEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorIN14LaunchServices5Types41EnumeratedTypeUnitOrDynamicTypeIdentifierEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorINS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorINS_4pairIP13objc_selectorPFvP11objc_objectS4_EEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorINS_4pairIU8__strongP8NSStringU8__strongP10NSMenuItemEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorINS_4pairIjPK12LSBundleDataEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorINS_4pairIjU8__strongP6NSUUIDEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorIP7BindingEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorIP8LSRecordEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorIPK10__CFStringEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorIPK7__LSASNEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorIPiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorIPvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorIU6__weakP8LSRecordEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorIU8__strongP19LSApplicationRecordEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorIU8__strongP8NSStringEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorIU8__strongU13block_pointerFvbP11_LSDatabaseP7NSErrorEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorIU8__strongU13block_pointerFvvEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorItEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__merge_move_assignB8nn180100INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRKN14LaunchServices12OpenWithMenu10BundleInfoES6_EPS4_SB_NS_11__wrap_iterISB_EEEEvT1_SE_T2_SF_T3_T0_
- __ZNSt3__119__partial_sort_implB8nn180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEESB_EET1_SC_SC_T2_OT0_
- __ZNSt3__119__partial_sort_implB8nn180100INS_17_ClassicAlgPolicyERU13block_pointerFbRKPKvS5_EPS3_S9_EET1_SA_SA_T2_OT0_
- __ZNSt3__119__shared_weak_count16__release_sharedB8nn180100Ev
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8nn180100Ev
- __ZNSt3__120__half_inplace_mergeB8nn180100INS_17_ClassicAlgPolicyENS_8__invertIRU8__strongU13block_pointerFbRKN14LaunchServices12OpenWithMenu10BundleInfoES7_EEENS_16reverse_iteratorIPS5_EESF_NSD_INS_11__wrap_iterISE_EEEESI_SI_EEvT1_T2_T3_T4_T5_OT0_
- __ZNSt3__120__half_inplace_mergeB8nn180100INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRKN14LaunchServices12OpenWithMenu10BundleInfoES6_EPS4_SB_NS_11__wrap_iterISB_EESD_SD_EEvT1_T2_T3_T4_T5_OT0_
- __ZNSt3__120back_insert_iteratorINS_6vectorIjNS_9allocatorIjEEEEEaSB8nn180100EOj
- __ZNSt3__120back_insert_iteratorINS_6vectorIjNS_9allocatorIjEEEEEaSB8nn180100ERKj
- __ZNSt3__120get_temporary_bufferB8nn180100IN14LaunchServices12OpenWithMenu10BundleInfoEEENS_4pairIPT_lEEl
- __ZNSt3__121__insertion_sort_moveB8nn180100INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRKN14LaunchServices12OpenWithMenu10BundleInfoES6_ENS_11__wrap_iterIPS4_EEEEvT1_SE_PNS_15iterator_traitsISE_E10value_typeET0_
- __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B8nn180100EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B8nn180100EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B8nn180100EPKcm
- __ZNSt3__121__unwrap_and_dispatchB8nn180100INS_10__overloadINS_11__copy_loopINS_17_ClassicAlgPolicyEEENS_14__copy_trivialEEEPKP8LSRecordSA_PU6__weakS8_Li0EEENS_4pairIT0_T2_EESE_T1_SF_
- __ZNSt3__121__unwrap_and_dispatchB8nn180100INS_10__overloadINS_11__copy_loopINS_17_ClassicAlgPolicyEEENS_14__copy_trivialEEEPKjS8_NS_20back_insert_iteratorINS_6vectorIjNS_9allocatorIjEEEEEELi0EEENS_4pairIT0_T2_EESG_T1_SH_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPvEEEEEclB8nn180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE13_LSPathBucketEEPvEEEEEclB8nn180100EPSC_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEEPvEEEEEclB8nn180100EPSB_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIP17_opaque_pthread_tNS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEEPvEEEEEclB8nn180100EPSC_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIP27OpaqueMappedResourceFileRefU8__strongP6NSDataEEPvEEEEEclB8nn180100EPSB_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIPKv9LSBindingEEPvEEEEEclB8nn180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIPKvNS_6vectorINS_4pairIP13objc_selectorPFvP11objc_objectS9_EEENS1_ISE_EEEEEEPvEEEEEclB8nn180100EPSJ_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIPKvU8__strongP5NSSetIP10objc_classEEEPvEEEEEclB8nn180100EPSE_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIjU8__strongP19LSApplicationRecordEEPvEEEEEclB8nn180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIjU8__strongP6FSNodeEEPvEEEEEclB8nn180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIjU8__strongP8NSStringEEPvEEEEEclB8nn180100EPS9_
- __ZNSt3__122__merge_move_constructB8nn180100INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRKN14LaunchServices12OpenWithMenu10BundleInfoES6_ENS_11__wrap_iterIPS4_EESD_EEvT1_SE_T2_SF_PNS_15iterator_traitsISE_E10value_typeET0_
- __ZNSt3__123__optional_storage_baseI9LSBindingLb0EE13__assign_fromB8nn180100INS_27__optional_move_assign_baseIS1_Lb0EEEEEvOT_
- __ZNSt3__123__optional_storage_baseIN14LaunchServices12OpenWithMenu10BundleInfoELb0EE13__assign_fromB8nn180100INS_27__optional_move_assign_baseIS3_Lb0EEEEEvOT_
- __ZNSt3__123__optional_storage_baseIN14LaunchServices13TypeEvaluator6ResultELb0EE13__assign_fromB8nn180100INS_27__optional_move_assign_baseIS3_Lb0EEEEEvOT_
- __ZNSt3__124__buffered_inplace_mergeB8nn180100INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRKN14LaunchServices12OpenWithMenu10BundleInfoES6_ENS_11__wrap_iterIPS4_EEEEvT1_SE_SE_OT0_NS_15iterator_traitsISE_E15difference_typeESJ_PNSI_10value_typeE
- __ZNSt3__124__optional_destruct_baseI9LSBindingLb0EE5resetB8nn180100Ev
- __ZNSt3__124__optional_destruct_baseI9LSBindingLb0EED2B8nn180100Ev
- __ZNSt3__124__optional_destruct_baseIN14LaunchServices12OpenWithMenu10BundleInfoELb0EE5resetB8nn180100Ev
- __ZNSt3__124__optional_destruct_baseIN14LaunchServices12OpenWithMenu10BundleInfoELb0EED2B8nn180100Ev
- __ZNSt3__124__optional_destruct_baseIN14LaunchServices14BundleWrappers28BundleWrapperUpdateOperationELb0EE5resetB8nn180100Ev
- __ZNSt3__124__optional_destruct_baseIN14LaunchServices14BundleWrappers28BundleWrapperUpdateOperationELb0EED2B8nn180100Ev
- __ZNSt3__124__optional_destruct_baseIN14LaunchServices16EligibilityCache11NotifyStateELb0EE5resetB8nn180100Ev
- __ZNSt3__124__optional_destruct_baseIN14LaunchServices30FeatureFlagPredicateEvaluation20FeatureFlagSpecifierELb0EED2B8nn180100Ev
- __ZNSt3__124__optional_destruct_baseIN14LaunchServices30FeatureFlagPredicateEvaluation9PredicateELb0EE5resetB8nn180100Ev
- __ZNSt3__124__optional_destruct_baseIN14LaunchServices30FeatureFlagPredicateEvaluation9PredicateELb0EED2B8nn180100Ev
- __ZNSt3__124__put_character_sequenceB8nn180100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__124__sort5_maybe_branchlessB8nn180100INS_17_ClassicAlgPolicyERZ87+[LSApplicationRecord(UserActivity) applicationRecordsForUserActivityType:limit:error:]E3$_0PNS_4pairIjPK12LSBundleDataEELi0EEEvT1_SA_SA_SA_SA_T0_
- __ZNSt3__124__sort5_maybe_branchlessB8nn180100INS_17_ClassicAlgPolicyERZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]E3$_1PjLi0EEEvT1_S5_S5_S5_S5_T0_
- __ZNSt3__124__sort5_maybe_branchlessB8nn180100INS_17_ClassicAlgPolicyERZL33_LSBundleCopyArchitectures_CommonPK12LSBundleDataP7NSArrayIP8NSStringEE3$_0P11LSSliceDataLi0EEEvT1_SE_SE_SE_SE_T0_
- __ZNSt3__125__throw_bad_function_callB8nn180100Ev
- __ZNSt3__126__insertion_sort_unguardedB8nn180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEvT1_SC_T0_
- __ZNSt3__126__insertion_sort_unguardedB8nn180100INS_17_ClassicAlgPolicyERU13block_pointerFbRKPKvS5_EPS3_EEvT1_SA_T0_
- __ZNSt3__127__insertion_sort_incompleteB8nn180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEbT1_SC_T0_
- __ZNSt3__127__insertion_sort_incompleteB8nn180100INS_17_ClassicAlgPolicyERU13block_pointerFbRKPKvS5_EPS3_EEbT1_SA_T0_
- __ZNSt3__127__insertion_sort_incompleteB8nn180100INS_17_ClassicAlgPolicyERZ87+[LSApplicationRecord(UserActivity) applicationRecordsForUserActivityType:limit:error:]E3$_0PNS_4pairIjPK12LSBundleDataEEEEbT1_SA_T0_
- __ZNSt3__127__insertion_sort_incompleteB8nn180100INS_17_ClassicAlgPolicyERZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]E3$_1PjEEbT1_S5_T0_
- __ZNSt3__127__insertion_sort_incompleteB8nn180100INS_17_ClassicAlgPolicyERZL33_LSBundleCopyArchitectures_CommonPK12LSBundleDataP7NSArrayIP8NSStringEE3$_0P11LSSliceDataEEbT1_SE_T0_
- __ZNSt3__127__throw_bad_optional_accessB8nn180100Ev
- __ZNSt3__127__tree_balance_after_insertB8nn180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__130__uninitialized_allocator_copyB8nn180100INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEPKS6_S9_PS6_EET2_RT_T0_T1_SB_
- __ZNSt3__131__partition_with_equals_on_leftB8nn180100INS_17_ClassicAlgPolicyEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERNS_6__lessIvvEEEET0_SC_SC_T1_
- __ZNSt3__131__partition_with_equals_on_leftB8nn180100INS_17_ClassicAlgPolicyEPPKvRU13block_pointerFbRKS3_S6_EEET0_SA_SA_T1_
- __ZNSt3__132__partition_with_equals_on_rightB8nn180100INS_17_ClassicAlgPolicyEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERNS_6__lessIvvEEEENS_4pairIT0_bEESD_SD_T1_
- __ZNSt3__132__partition_with_equals_on_rightB8nn180100INS_17_ClassicAlgPolicyEPPKvRU13block_pointerFbRKS3_S6_EEENS_4pairIT0_bEESB_SB_T1_
- __ZNSt3__135__uninitialized_allocator_copy_implB8nn180100INS_3pmr21polymorphic_allocatorIN14LaunchServices17BindingEvaluation15ExtendedBindingEEENS_13move_iteratorINS_11__wrap_iterIPS5_EEEESB_S9_EET2_RT_T0_T1_SC_
- __ZNSt3__135__uninitialized_allocator_copy_implB8nn180100INS_9allocatorI26_FSInternetLocatorTypeInfoEEPKS2_S5_PS2_EET2_RT_T0_T1_S7_
- __ZNSt3__135__uninitialized_allocator_copy_implB8nn180100INS_9allocatorI9LSBindingEEPN14LaunchServices17BindingEvaluation15ExtendedBindingES7_PS2_EET2_RT_T0_T1_S9_
- __ZNSt3__135__uninitialized_allocator_copy_implB8nn180100INS_9allocatorIN14LaunchServices12OpenWithMenu10BundleInfoEEENS_21__tree_const_iteratorIS4_PNS_11__tree_nodeIS4_PvEElEESB_PS4_EET2_RT_T0_T1_SD_
- __ZNSt3__135__uninitialized_allocator_copy_implB8nn180100INS_9allocatorIN14LaunchServices19PrefsCapabilityInfoEEEPKS3_S6_PS3_EET2_RT_T0_T1_S8_
- __ZNSt3__135__uninitialized_allocator_copy_implB8nn180100INS_9allocatorINS_4pairIU8__strongP8NSStringU8__strongP10NSMenuItemEEEEPS9_SB_SB_EET2_RT_T0_T1_SC_
- __ZNSt3__13pmr21polymorphic_allocatorIN14LaunchServices17BindingEvaluation15ExtendedBindingEE7destroyB8nn180100IS4_EEvPT_
- __ZNSt3__13pmr21polymorphic_allocatorIN14LaunchServices17BindingEvaluation15ExtendedBindingEE8allocateB8nn180100Em
- __ZNSt3__13pmr21polymorphic_allocatorIN14LaunchServices17BindingEvaluation15ExtendedBindingEE9constructB8nn180100IS4_JRKS4_EEEvPT_DpOT0_
- __ZNSt3__13pmr21polymorphic_allocatorIN14LaunchServices17BindingEvaluation15ExtendedBindingEE9constructB8nn180100IS4_JRS4_EEEvPT_DpOT0_
- __ZNSt3__13pmr21polymorphic_allocatorIPNS_16__hash_node_baseIPNS_11__hash_nodeIiPvEEEEE8allocateB8nn180100Em
- __ZNSt3__13pmr21polymorphic_allocatorIPNS_16__hash_node_baseIPNS_11__hash_nodeIjPvEEEEE8allocateB8nn180100Em
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8nn180100INS_3pmr21polymorphic_allocatorIN14LaunchServices17BindingEvaluation15ExtendedBindingEEENS_16reverse_iteratorIPS5_EES9_S9_EET2_RT_T0_T1_SA_
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8nn180100INS_3pmr21polymorphic_allocatorIN14LaunchServices17BindingEvaluation15ExtendedBindingEEEPS5_S7_S7_EET2_RT_T0_T1_S8_
- __ZNSt3__14sortB8nn180100INS_11__wrap_iterIPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEEEvT_SA_
- __ZNSt3__14sortB8nn180100INS_11__wrap_iterIPPKvEEU13block_pointerFbRKS3_S7_EEEvT_SA_T0_
- __ZNSt3__14swapB8nn180100IN14LaunchServices12OpenWithMenu10BundleInfoEEENS_9enable_ifIXaasr21is_move_constructibleIT_EE5valuesr18is_move_assignableIS5_EE5valueEvE4typeERS5_S8_
- __ZNSt3__14swapB8nn180100IN14LaunchServices17BindingEvaluation15ExtendedBindingEEENS_9enable_ifIXaasr21is_move_constructibleIT_EE5valuesr18is_move_assignableIS5_EE5valueEvE4typeERS5_S8_
- __ZNSt3__15dequeIiNS_9allocatorIiEEE26__maybe_remove_front_spareB8nn180100Eb
- __ZNSt3__16removeB8nn180100INS_11__wrap_iterIPU6__weakP8LSRecordEEDnEET_S7_S7_RKT0_
- __ZNSt3__16vectorI13LSBundleClassNS_9allocatorIS1_EEE11__vallocateB8nn180100Em
- __ZNSt3__16vectorI13LSBundleClassNS_9allocatorIS1_EEE18__assign_with_sizeB8nn180100IPKS1_S7_EEvT_T0_l
- __ZNSt3__16vectorI13LSBundleClassNS_9allocatorIS1_EEE18__assign_with_sizeB8nn180100IPS1_S6_EEvT_T0_l
- __ZNSt3__16vectorI19ProcessSerialNumberNS_9allocatorIS1_EEE11__vallocateB8nn180100Em
- __ZNSt3__16vectorI19ProcessSerialNumberNS_9allocatorIS1_EEE18__assign_with_sizeB8nn180100IPS1_S6_EEvT_T0_l
- __ZNSt3__16vectorI9LSBindingNS_9allocatorIS1_EEE16__destroy_vectorclB8nn180100Ev
- __ZNSt3__16vectorI9LSBindingNS_9allocatorIS1_EEE18__insert_with_sizeB8nn180100INS_11__wrap_iterIPN14LaunchServices17BindingEvaluation15ExtendedBindingEEESB_EENS6_IPS1_EENS6_IPKS1_EET_T0_l
- __ZNSt3__16vectorI9LSBindingNS_9allocatorIS1_EEE22__base_destruct_at_endB8nn180100EPS1_
- __ZNSt3__16vectorI9LSBindingNS_9allocatorIS1_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS1_RS3_EE
- __ZNSt3__16vectorI9LSBindingNS_9allocatorIS1_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS1_RS3_EEPS1_
- __ZNSt3__16vectorI9LSBindingNS_9allocatorIS1_EEE9push_backB8nn180100EOS1_
- __ZNSt3__16vectorIN14LaunchServices12OpenWithMenu10BundleInfoENS_9allocatorIS3_EEE16__destroy_vectorclB8nn180100Ev
- __ZNSt3__16vectorIN14LaunchServices12OpenWithMenu10BundleInfoENS_9allocatorIS3_EEE18__insert_with_sizeB8nn180100INS_21__tree_const_iteratorIS3_PNS_11__tree_nodeIS3_PvEElEESD_EENS_11__wrap_iterIPS3_EENSE_IPKS3_EET_T0_l
- __ZNSt3__16vectorIN14LaunchServices12OpenWithMenu10BundleInfoENS_9allocatorIS3_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS3_RS5_EE
- __ZNSt3__16vectorIN14LaunchServices12OpenWithMenu10BundleInfoENS_9allocatorIS3_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS3_RS5_EEPS3_
- __ZNSt3__16vectorIN14LaunchServices12OpenWithMenu4ItemENS_9allocatorIS3_EEE11__vallocateB8nn180100Em
- __ZNSt3__16vectorIN14LaunchServices12OpenWithMenu4ItemENS_9allocatorIS3_EEE16__destroy_vectorclB8nn180100Ev
- __ZNSt3__16vectorIN14LaunchServices12OpenWithMenu4ItemENS_9allocatorIS3_EEE16__init_with_sizeB8nn180100IPS3_S8_EEvT_T0_m
- __ZNSt3__16vectorIN14LaunchServices12OpenWithMenu4ItemENS_9allocatorIS3_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS3_RS5_EE
- __ZNSt3__16vectorIN14LaunchServices12OpenWithMenu4ItemENS_9allocatorIS3_EEE9push_backB8nn180100EOS3_
- __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS_3pmr21polymorphic_allocatorIS3_EEE11__vallocateB8nn180100Em
- __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS_3pmr21polymorphic_allocatorIS3_EEE16__destroy_vectorclB8nn180100Ev
- __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS_3pmr21polymorphic_allocatorIS3_EEE18__assign_with_sizeB8nn180100INS_13move_iteratorINS_11__wrap_iterIPS3_EEEESD_EEvT_T0_l
- __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS_3pmr21polymorphic_allocatorIS3_EEE18__construct_at_endINS_11__wrap_iterIPS3_EESB_EEvT_T0_m
- __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS_3pmr21polymorphic_allocatorIS3_EEE18__insert_with_sizeB8nn180100INS_11__wrap_iterIPS3_EESB_EESB_NS9_IPKS3_EET_T0_l
- __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS_3pmr21polymorphic_allocatorIS3_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS3_RS6_EE
- __ZNSt3__16vectorIN14LaunchServices30FeatureFlagPredicateEvaluation20FeatureFlagSpecifierENS_9allocatorIS3_EEE16__destroy_vectorclB8nn180100Ev
- __ZNSt3__16vectorIN14LaunchServices5Types41EnumeratedTypeUnitOrDynamicTypeIdentifierENS_9allocatorIS3_EEE16__destroy_vectorclB8nn180100Ev
- __ZNSt3__16vectorIN14LaunchServices5Types41EnumeratedTypeUnitOrDynamicTypeIdentifierENS_9allocatorIS3_EEE9push_backB8nn180100ERKS3_
- __ZNSt3__16vectorINS_10shared_ptrIN14LaunchServices16PerThreadContextEEENS_9allocatorIS4_EEE16__destroy_vectorclB8nn180100Ev
- __ZNSt3__16vectorINS_10shared_ptrIN14LaunchServices16PerThreadContextEEENS_9allocatorIS4_EEE7__clearB8nn180100Ev
- __ZNSt3__16vectorINS_10shared_ptrIN14LaunchServices16PerThreadContextEEENS_9allocatorIS4_EEE9push_backB8nn180100ERKS4_
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB8nn180100Ev
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE7__clearB8nn180100Ev
- __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP10NSMenuItemEENS_9allocatorIS8_EEE11__vallocateB8nn180100Em
- __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP10NSMenuItemEENS_9allocatorIS8_EEE16__destroy_vectorclB8nn180100Ev
- __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP10NSMenuItemEENS_9allocatorIS8_EEE16__init_with_sizeB8nn180100IPS8_SD_EEvT_T0_m
- __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP10NSMenuItemEENS_9allocatorIS8_EEE22__base_destruct_at_endB8nn180100EPS8_
- __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP10NSMenuItemEENS_9allocatorIS8_EEE24__emplace_back_slow_pathIJRU8__strongKS3_RS7_EEEPS8_DpOT_
- __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP10NSMenuItemEENS_9allocatorIS8_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS8_RSA_EE
- __ZNSt3__16vectorINS_4pairIjU8__strongP6NSUUIDEENS_9allocatorIS5_EEE16__destroy_vectorclB8nn180100Ev
- __ZNSt3__16vectorIP7BindingNS_9allocatorIS2_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS2_RS4_EEPS2_
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE11__vallocateB8nn180100Em
- __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE11__vallocateB8nn180100Em
- __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE16__destroy_vectorclB8nn180100Ev
- __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE16__init_with_sizeB8nn180100IPKS2_S9_EEvT_T0_m
- __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE16__init_with_sizeB8nn180100IPS3_S8_EEvT_T0_m
- __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE18__insert_with_sizeB8nn180100IPKS2_S9_EENS_11__wrap_iterIPS3_EENSA_IPU6__weakKS2_EET_T0_l
- __ZNSt3__16vectorIU8__strongP19LSApplicationRecordNS_9allocatorIS3_EEE12emplace_backIJRS3_EEES8_DpOT_
- __ZNSt3__16vectorIU8__strongP19LSApplicationRecordNS_9allocatorIS3_EEE16__destroy_vectorclB8nn180100Ev
- __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEE16__destroy_vectorclB8nn180100Ev
- __ZNSt3__16vectorIU8__strongU13block_pointerFvbP11_LSDatabaseP7NSErrorENS_9allocatorIS7_EEE16__destroy_vectorclB8nn180100Ev
- __ZNSt3__16vectorIU8__strongU13block_pointerFvvENS_9allocatorIS3_EEE11__vallocateB8nn180100Em
- __ZNSt3__16vectorIU8__strongU13block_pointerFvvENS_9allocatorIS3_EEE16__destroy_vectorclB8nn180100Ev
- __ZNSt3__16vectorIU8__strongU13block_pointerFvvENS_9allocatorIS3_EEE16__init_with_sizeB8nn180100IPS3_S8_EEvT_T0_m
- __ZNSt3__16vectorIU8__strongU13block_pointerFvvENS_9allocatorIS3_EEE9push_backB8nn180100ERU8__strongKS2_
- __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB8nn180100Em
- __ZNSt3__16vectorIjNS_9allocatorIjEEE11__vallocateB8nn180100Em
- __ZNSt3__16vectorIjNS_9allocatorIjEEE18__assign_with_sizeB8nn180100IPjS5_EEvT_T0_l
- __ZNSt3__16vectorItNS_9allocatorItEEE11__vallocateB8nn180100Em
- __ZNSt3__17__sort3B8nn180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEjT1_SC_SC_T0_
- __ZNSt3__17__sort3B8nn180100INS_17_ClassicAlgPolicyERU13block_pointerFbRKPKvS5_EPS3_EEjT1_SA_SA_T0_
- __ZNSt3__17__sort3B8nn180100INS_17_ClassicAlgPolicyERZ87+[LSApplicationRecord(UserActivity) applicationRecordsForUserActivityType:limit:error:]E3$_0PNS_4pairIjPK12LSBundleDataEEEEjT1_SA_SA_T0_
- __ZNSt3__17__sort3B8nn180100INS_17_ClassicAlgPolicyERZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]E3$_1PjEEjT1_S5_S5_T0_
- __ZNSt3__17__sort3B8nn180100INS_17_ClassicAlgPolicyERZL33_LSBundleCopyArchitectures_CommonPK12LSBundleDataP7NSArrayIP8NSStringEE3$_0P11LSSliceDataEEjT1_SE_SE_T0_
- __ZNSt3__17__sort4B8nn180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEvT1_SC_SC_SC_T0_
- __ZNSt3__17__sort4B8nn180100INS_17_ClassicAlgPolicyERU13block_pointerFbRKPKvS5_EPS3_EEvT1_SA_SA_SA_T0_
- __ZNSt3__17__sort4B8nn180100INS_17_ClassicAlgPolicyERZ87+[LSApplicationRecord(UserActivity) applicationRecordsForUserActivityType:limit:error:]E3$_0PNS_4pairIjPK12LSBundleDataEEEEvT1_SA_SA_SA_T0_
- __ZNSt3__17__sort4B8nn180100INS_17_ClassicAlgPolicyERZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]E3$_1PjEEvT1_S5_S5_S5_T0_
- __ZNSt3__17__sort4B8nn180100INS_17_ClassicAlgPolicyERZL33_LSBundleCopyArchitectures_CommonPK12LSBundleDataP7NSArrayIP8NSStringEE3$_0P11LSSliceDataEEvT1_SE_SE_SE_T0_
- __ZNSt3__17__sort5B8nn180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEvT1_SC_SC_SC_SC_T0_
- __ZNSt3__17__sort5B8nn180100INS_17_ClassicAlgPolicyERU13block_pointerFbRKPKvS5_EPS3_EEvT1_SA_SA_SA_SA_T0_
- __ZNSt3__18optionalI9LSBindingEaSB8nn180100IRKN14LaunchServices17BindingEvaluation15ExtendedBindingEvEERS2_OT_
- __ZNSt3__18optionalI9LSBindingEaSB8nn180100IRS1_vEERS2_OT_
- __ZNSt3__18optionalIN14LaunchServices12OpenWithMenu10BundleInfoEEaSB8nn180100IS3_vEERS4_OT_
- __ZNSt3__18optionalIN14LaunchServices16BindingEvaluatorEEaSB8nn180100IS2_vEERS3_OT_
- __ZNSt3__18optionalIN14LaunchServices30EligibilityPredicateEvaluation9PredicateEE7emplaceB8nn180100IJS3_EvEERS3_DpOT_
- __ZNSt3__18optionalIN14LaunchServices30FeatureFlagPredicateEvaluation9PredicateEE7emplaceB8nn180100IJS3_EvEERS3_DpOT_
- __ZNSt3__18optionalIU8__strongP7NSErrorEaSB8nn180100IRS3_vEERS4_OT_
- __ZNSt3__19__advanceB8nn180100INS_21__tree_const_iteratorIN14LaunchServices12OpenWithMenu10BundleInfoEPNS_11__tree_nodeIS4_PvEElEEEEvRT_NS_15iterator_traitsISA_E15difference_typeENS_26bidirectional_iterator_tagE
- __ZNSt3__19__sift_upB8nn180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEvT1_SC_OT0_NS_15iterator_traitsISC_E15difference_typeE
- __ZNSt3__19__sift_upB8nn180100INS_17_ClassicAlgPolicyERU13block_pointerFbRKPKvS5_EPS3_EEvT1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
- __ZNSt3__19allocatorIN14LaunchServices12OpenWithMenu10BundleInfoEE7destroyB8nn180100EPS3_
- __ZNSt3__19allocatorIN14LaunchServices12OpenWithMenu10BundleInfoEE9constructB8nn180100IS3_JRKS3_EEEvPT_DpOT0_
- __ZNSt3__19allocatorIN14LaunchServices12OpenWithMenu10BundleInfoEE9constructB8nn180100IS3_JS3_EEEvPT_DpOT0_
- __ZNSt3__19allocatorIN14LaunchServices12OpenWithMenu4ItemEE7destroyB8nn180100EPS3_
- __ZNSt3__19allocatorIN14LaunchServices12OpenWithMenu4ItemEE9constructB8nn180100IS3_JRS3_EEEvPT_DpOT0_
- __ZNSt3__19allocatorIN14LaunchServices30FeatureFlagPredicateEvaluation20FeatureFlagSpecifierEE7destroyB8nn180100EPS3_
- __ZNSt3__19allocatorINS_11__tree_nodeIN14LaunchServices12OpenWithMenu10BundleInfoEPvEEE9constructB8nn180100IS4_JRKS4_EEEvPT_DpOT0_
- __ZNSt3__19basic_iosIcNS_11char_traitsIcEEE5imbueB8nn180100ERKNS_6localeE
- __ZNSt3__1lsB8nn180100INS_11char_traitsIcEEEERNS_13basic_ostreamIcT_EES6_RKNS_8__iom_t4IcEE
- __ZSt28__throw_bad_array_new_lengthB8nn180100v
- __ZZ23_LSCopyFrontApplicationE5sLock
- __ZZ23_LSCopyFrontApplicationE6sValue
- __ZZ26_LSCopyAllApplicationArrayE29sCachedAllApplicationArrayRef
- __ZZ26_LSCopyAllApplicationArrayE30sCachedAllApplicationArraySeed
- __ZZ30_LSCopyRunningApplicationArrayE33sCachedRunningApplicationArrayRef
- __ZZ30_LSCopyRunningApplicationArrayE34sCachedRunningApplicationArraySeed
- __ZZ39-[_LSExceptions applyToInfoDictionary:]E9mergeKeys
- __ZZ41_LSCopyApplicationArrayInFrontToBackOrderE28sVisibleApplicationArrayLock
- __ZZ41_LSCopyApplicationArrayInFrontToBackOrderE32sVisibleApplicationArrayLockOnce
- __ZZ41_LSCopyApplicationArrayInFrontToBackOrderE33sCachedVisibleApplicationArrayRef
- __ZZ41_LSCopyApplicationArrayInFrontToBackOrderE34sCachedVisibleApplicationArraySeed
- __ZZL17GetQuarantineTypejE15quarantineTypes
- __ZZL20CopyApplicationArray11LSSessionIDbPPK9__CFArrayPjE21sApplicationArrayLock
- __ZZL20CopyApplicationArray11LSSessionIDbPPK9__CFArrayPjE25sApplicationArrayLockOnce
- __ZZL22getLSRegistrationQueuevE5sOnce
- __ZZL22getLSRegistrationQueuevE6sQueue
- __ZZL24once_createPropertyTablevE18baseDependencyKeys
- __ZZL24once_createPropertyTablevE19typeDescriptionKeys
- __ZZL24once_createPropertyTablevE21bindingDependencyKeys
- __ZZL24once_createPropertyTablevE23genericSafeApertureKeys
- __ZZL24once_createPropertyTablevE24volLocNameDependencyKeys
- __ZZL24once_createPropertyTablevE25canSetHiddenExtensionKeys
- __ZZL24once_createPropertyTablevE25distinctLocalizedNameKeys
- __ZZL24once_createPropertyTablevE27appCapabilityDependencyKeys
- __ZZL24once_createPropertyTablevE27appCategoriesDependencyKeys
- __ZZL24once_createPropertyTablevE27architecturesDependencyKeys
- __ZZL24once_createPropertyTablevE27isApplicationDependencyKeys
- __ZZL24once_createPropertyTablevE27strongBindingDependencyKeys
- __ZZL24once_createPropertyTablevE27volQuarantineDependencyKeys
- __ZZL24once_createPropertyTablevE28hiddenBySystemDependencyKeys
- __ZZL24once_createPropertyTablevE33canSetStrongBindingDependencyKeys
- __ZZL49_LSCopyApplicationInformationItemFromSharedMemoryPK20__LSSharedMemoryPagePK7__LSASNPKvPS6_E50sApplicationInformationRetrievableFromSharedMemory
- __ZZL53_LSCopyMetaApplicationInformationItemFromSharedMemoryPK20__LSSharedMemoryPagePKvRbE43sMetaInformationRetrievableFromSharedMemory
- __ZZL9getLibIDsvE7klibIDs
- __ZZN14LaunchServices17BindingEvaluationL12runEvaluatorERNS0_5StateEPU15__autoreleasingP7NSErrorE7options
- __ZZN14LaunchServices17BindingEvaluationL4sortERNS0_5StateEENK3$_0clERKNS0_15ExtendedBindingES6_
- __ZZN17QuarantineEventDB18setEventPropertiesEPK14__CFDictionaryE8propKeys
- __ZZZ65+[_LSTrustedSignatureDatabase(Database) scheduleDatabaseTrimming]EUb_E8interval
- ___48-[LSDatabaseBuilder createAndSeedLocalDatabase:]_block_invoke_2
- ___59-[LSMIRegistrantServerStrategy runSyncBlockInWriteContext:]_block_invoke
- ___LSServer_SyncWithMobileInstallation_block_invoke.831
- ___LSServer_SyncWithMobileInstallation_block_invoke.833
- ___LSServer_SyncWithMobileInstallation_block_invoke.845
- ___LSServer_SyncWithMobileInstallation_block_invoke.845.cold.1
- ___LSServer_SyncWithMobileInstallation_block_invoke.845.cold.2
- ___LSServer_SyncWithMobileInstallation_block_invoke.846
- ___LSServer_SyncWithMobileInstallation_block_invoke.849
- ___LSServer_SyncWithMobileInstallation_block_invoke_2.850
- ___ZL27_LSDNCGetExtensionSkeletonsP9LSContextRP13USpoofChecker_block_invoke.240
- ___ZL27_LSDNCGetExtensionSkeletonsP9LSContextRP13USpoofChecker_block_invoke.244
- ___ZN14LaunchServices17BindingEvaluationL27insertSelectedDeveloperToolERNS0_5StateE_block_invoke.223
- ___ZN14LaunchServices7BundlesL7displayEP9LSContextjjPNS_10DumpWriterE_block_invoke.371
- ___ZN14LaunchServices7BundlesL7displayEP9LSContextjjPNS_10DumpWriterE_block_invoke.658
- ___ZN14LaunchServices7BundlesL7displayEP9LSContextjjPNS_10DumpWriterE_block_invoke_2.660
- ___ZN14LaunchServices7BundlesL7displayEP9LSContextjjPNS_10DumpWriterE_block_invoke_3.661
- ___ZN26LSClientToServerConnection21setupServerConnectionEiPK14__CFDictionary_block_invoke.34
- ___ZN26LSClientToServerConnection21setupServerConnectionEiPK14__CFDictionary_block_invoke.34.cold.1
- ___block_descriptor_114_ea8_32s40s48s56s64s72s80s88s96s104bs_e56_v16?0"<LSMIResultRegistrantDatabaseContextProviding>"8l
- ___block_descriptor_40_e110_v24?0r^{LSDefaultAppCategoryInfo=Q^{__CFString}^{__CFString}Q^?^{LSDefaultAppCategorySubordinateClaim}Q}8^B16l
- ___block_descriptor_44_ea8_32r_e59_v40?0^{__CFURLEnumerator=}8^{__CFURL=}16^{__CFError=}24*32l
- ___block_descriptor_44_ea8_32s_e62_v28?0B8"<LSMIResultRegistrantDatabaseContext>"12"NSError"20l
- ___block_descriptor_48_ea8_32s40r_e62_v28?0B8"<LSMIResultRegistrantDatabaseContext>"12"NSError"20l
- ___block_descriptor_64_ea8_32s40r48r56r_e56_v16?0"<LSMIResultRegistrantDatabaseContextProviding>"8l
- __block_descriptor_tmp.35
- __block_descriptor_tmp.60
- __block_descriptor_tmp.64
- __block_descriptor_tmp.67
- __block_descriptor_tmp.77
- __block_literal_global.208
- __block_literal_global.218
- __block_literal_global.227
- __block_literal_global.241
- __block_literal_global.402
- __block_literal_global.429
- __block_literal_global.433
- __block_literal_global.436
- __block_literal_global.558
- __block_literal_global.577
- __block_literal_global.594
- __block_literal_global.596
- __block_literal_global.62
- __block_literal_global.65
- __block_literal_global.69
- __block_literal_global.852
- __block_literal_global.89
- __block_literal_global.916
- __block_literal_global.945
- __block_literal_global.947
- __block_literal_global.963
- _gJavaLaunchingFrameworkHandle
- _objc_msgSend$clientIsEntitledForPostInstallationOperations
- _objc_msgSend$findOrRegisterContainerizedNodeReinitializingContext:installDictionary:personasWithAttributes:error:
- _objc_msgSend$windowOpenDate
- preferredLocalizations.once.219
CStrings:
+ "#LSDatabaseBuilder %s has alredy been visited"
+ "#LSDatabaseBuilder Failed to read database from disk and couldn't create new one: %{public}@"
+ "#LSDatabaseBuilder Saved system content database to %@"
+ "#LSDatabaseBuilder Seeding database with UID: %d, EUID %d"
+ "#LSDatabaseBuilder could not write out system content database! %@"
+ "#LSDatabaseBuilder error %@ registering %@"
+ "#LSDatabaseBuilder error %d registering library %@"
+ "#LSDatabaseBuilder error %d registering plugin %@"
+ "#LSDatabaseBuilder examining recursive path %s"
+ "#LSDatabaseBuilder gc and save"
+ "#LSDatabaseBuilder processing %s"
+ "#LSDatabaseBuilder register apps"
+ "#LSDatabaseBuilder register libraries"
+ "#LSDatabaseBuilder register network volumes"
+ "#LSDatabaseBuilder register remote placeholders"
+ "#LSDatabaseBuilder register spotlight contents"
+ "#LSDatabaseBuilder registered %@"
+ "#LSDatabaseBuilder registered library %@"
+ "#LSDatabaseBuilder registered plugin %@"
+ "#LSDatabaseBuilder set package extensions"
+ "#LSDatabaseBuilder set seeding complete"
+ "#LSDatabaseBuilder sync with MI"
+ "%s: currently not eligible for %llu (answer %d)"
+ "-[LSApplicationWorkspace refreshUnbundledSystemExtensionPointsWithOperationUUID:requestContext:saveObserver:registrationError:]"
+ "-[LSApplicationWorkspace registerBuiltinApplicationWithInstallationRecord:extensionInstallationRecords:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:]"
+ "-[LSApplicationWorkspace registerBuiltinStandaloneExtension:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:]"
+ "-[LSApplicationWorkspace unregisterBuiltinApplicationAtURL:operationUUID:requestContext:saveObserver:error:]"
+ "-[LSApplicationWorkspace unregisterBuiltinStandaloneExtensionAtURL:operationUUID:requestContext:saveObserver:error:]"
+ "-[LSBuiltinApplicationRegistrant runWithCompletion:]"
+ "-[LSBuiltinApplicationRegistrant runWithCompletion:]_block_invoke"
+ "-[LSBuiltinPluginRegistrant runWithCompletion:]"
+ "-[LSBuiltinPluginRegistrant runWithCompletion:]_block_invoke"
+ "-[LSByURLBundleUnregistrant runWithCompletion:]_block_invoke"
+ "-[LSByURLPluginUnregistrant runWithCompletion:]_block_invoke"
+ "-[LSMIResultRegistrantTrueDatabaseContext findApplicationBundleAtNode:error:]"
+ "-[LSMIResultRegistrantTrueDatabaseContext registerBundleNodeReinitializingContext:inBundleContainer:installDictionary:personasWithAttributes:error:]"
+ "-[LSMIResultRegistrantTrueDatabaseContext registerNonBundledExtensionPointWithIdentifier:platform:SDKDict:url:error:]"
+ "-[LSMIResultRegistrantTrueDatabaseContext unregisterApplicationBundleByUnit:error:]"
+ "-[LSMIResultRegistrantTrueDatabaseContext unregisterPluginBundleByUnit:error:]"
+ "-[LSSystemExtensionPointRefreshRegistrant runWithCompletion:]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/TemplateApplications/LSTemplateApplicationCreation.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/TemplateApplications/LSTemplateApplicationLaunch.mm"
+ "@\"<LSRegistrantDatabaseContext>\"24@0:8^@16"
+ "@\"<LSRegistrantStrategy>\""
+ "@28@0:8I16@\"<LSRegistrantDatabaseContext>\"20"
+ "@?28@0:8I16^@20"
+ "@?<v@?@>28@0:8I16^@20"
+ "B32@0:8@\"NSString\"16^@24"
+ "B44@0:8@\"FSNode\"16@\"NSDictionary\"24I32^@36"
+ "B44@0:8@16@24I32^@36"
+ "B52@0:8@\"NSString\"16I24@\"NSDictionary\"28@\"NSURL\"36^@44"
+ "B52@0:8@16I24@28@36^@44"
+ "B72@0:8@16@24@32@40@48@56^@64"
+ "Cannot register parallel placeholders or standalone placeholders with this interface."
+ "Couldn't get answer for domain %llu: %@"
+ "Don't add weak binding (ineligible)"
+ "I32@0:8@\"FSNode\"16^@24"
+ "I52@0:8@\"FSNode\"16B24@\"NSDictionary\"28@\"NSSet\"36^@44"
+ "I52@0:8@16B24@28@36^@44"
+ "LSBuiltinApplicationRegistrant"
+ "LSBuiltinPluginRegistrant"
+ "LSByURLBundleUnregistrant"
+ "LSByURLPluginUnregistrant"
+ "LSDefaultApplicationQueryBackend.mm"
+ "LSRegistrantDatabaseContext"
+ "LSRegistrantDatabaseContextProviding"
+ "LSRegistrantServerStrategy"
+ "LSRegistrantStrategy"
+ "LSRegistrants.mm"
+ "LSSystemExtensionPointRefreshRegistrant"
+ "LaunchServices database schema version: %{public}ld"
+ "Missing path"
+ "Registered %zu EPs, new: %@ obsolete: %@"
+ "Save after registration for refresh extension points, save attempted %d error %@"
+ "Save after registration for register builtin plugin url %@ (unit %llx) attempted: %d save error: %@"
+ "Save after unregistration for plugin url %@ (unit %llx) attempted: %d save error: %@"
+ "Save after unregistration for register builtin app url %@ (unit %llx) attempted: %d save error: %@"
+ "Save after unregistration for url %@ (unit %llx) attempted: %d save error: %@"
+ "T@\"NSArray\",R,N,V_windowOpenDates"
+ "TB,R,D,N,GisOpenWindowGroupFull"
+ "T^{LSContext=@},R"
+ "Unable to unregister obsolete EP %@: %@"
+ "Unregister bundle by URL start: %@"
+ "Unregister plugin by URL start: %@"
+ "Will unregister app by unit (0x%llx), removingPlaceholder: %d removingSystemPlaceholder: %d foundParallelBundle: %d"
+ "^{LSContext=@}16@0:8"
+ "_LSUnregisterAppByUnit"
+ "_windowOpenDates"
+ "app in container"
+ "bad_function_call was thrown in -fno-exceptions mode"
+ "bad_optional_access was thrown in -fno-exceptions mode"
+ "clientIsEntitledForEmbeddedRegistrationOperations"
+ "com.apple.launchservices.coreapplicationservices"
+ "containerizedBundleExistsForIdentifier:"
+ "contextPointer"
+ "could not register EP %@ at %@: %@"
+ "couldn't find bundle for unit %llx, but we should have it in this flow!"
+ "darwinOS doesn't support launchservicesd, so many application-related functions do not work."
+ "eligibleForDomainFailingClosed"
+ "enumerateExtensionPointRecords:"
+ "enumerateSystemEXExtensionPoints:"
+ "findApplicationBundleAtNode:error:"
+ "findPluginAtNode:error:"
+ "have error even though we succeeded!? %@"
+ "initWithStrategy:operationUUID:"
+ "initWithStrategy:operationUUID:URL:"
+ "initWithStrategy:operationUUID:itemInfoDict:"
+ "initWithStrategy:operationUUID:itemInfoDict:personas:"
+ "initWithWindowOpenDates:refreshDate:defaultForCategory:"
+ "isOpenWindowGroupFull"
+ "must have at least one known window"
+ "newestWindowOpenDate"
+ "oldestWindowOpenDate"
+ "openWindowGroupFull"
+ "plugin is in an app"
+ "pluginDataForPlugin:"
+ "preUnregistrationContextForBundleUnit:context:"
+ "r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCIS{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}III}20@0:8I16"
+ "refreshUnbundledSystemExtensionPointsWithOperationUUID:requestContext:saveObserver:registrationError:"
+ "registerBuiltinApplicationWithInstallationRecord:extensionInstallationRecords:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:"
+ "registerBuiltinStandaloneExtension:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:"
+ "registerBundleNodeReinitializingContext:inBundleContainer:installDictionary:personasWithAttributes:error:"
+ "registerNonBundledExtensionPointWithIdentifier:platform:SDKDict:url:error:"
+ "registerPluginNodeReinitializingContext:installDictionary:existingPlugin:error:"
+ "stale windows, returning %@"
+ "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1355:63)]"
+ "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1386:65)]"
+ "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1393:65)]"
+ "static id LaunchServices::PrefsStorage::_GetValueInPrefsArrayWithPredicate(NSArray *__strong, __unsafe_unretained Class, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1386:65)]"
+ "static id LaunchServices::PrefsStorage::_GetValueInPrefsArrayWithPredicate(NSArray *__strong, __unsafe_unretained Class, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1393:65)]"
+ "unregisterApplicationBundleByUnit:error:"
+ "unregisterBuiltinApplicationAtURL:operationUUID:requestContext:saveObserver:error:"
+ "unregisterBuiltinStandaloneExtensionAtURL:operationUUID:requestContext:saveObserver:error:"
+ "unregisterNonBundledExtensionPointWithIdentifier:error:"
+ "unregisterPluginBundleByUnit:error:"
+ "updatedEntryRotatingInWindowOpenDate:refreshDate:defaultForCategory:"
+ "updatedEntryWithRefreshDate:defaultForCategory:"
+ "v16@?0@\"<LSRegistrantDatabaseContextProviding>\"8"
+ "v24@0:8@?<v@?@\"<EXExtensionPoint>\"^B>16"
+ "v24@0:8@?<v@?@\"<LSRegistrantDatabaseContextProviding>\">16"
+ "v24@0:8@?<v@?@\"LSExtensionPointRecord\"^B>16"
+ "v24@0:8@?<v@?B@\"<LSRegistrantDatabaseContext>\"@\"NSError\">16"
+ "v24@?0@\"<EXExtensionPoint>\"8^B16"
+ "v24@?0@\"LSExtensionPointRecord\"8^B16"
+ "v24@?0r^{LSDefaultAppCategoryInfo=Q^{__CFString}^{__CFString}Q^?^{LSDefaultAppCategorySubordinateClaim}QB}8^B16"
+ "v28@?0B8@\"<LSRegistrantDatabaseContext>\"12@\"NSError\"20"
+ "window open dates %@"
+ "windowOpenDates"
+ "{?=\"hasLookedForLoctable\"b1\"isInfoPlist\"b1}"
- "%@%@%@"
- "-[LSMIResultRegistrantTrueDatabaseContext findOrRegisterContainerizedNodeReinitializingContext:installDictionary:personasWithAttributes:error:]"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/TemplateApplications/LSTemplateApplicationCreation.mm"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/TemplateApplications/LSTemplateApplicationLaunch.mm"
- "@\"<LSMIResultRegistrantDatabaseContext>\"24@0:8^@16"
- "@\"<LSMIResultRegistrantStrategy>\""
- "I48@0:8@\"FSNode\"16@\"NSDictionary\"24@\"NSSet\"32^@40"
- "I48@0:8@16@24@32^@40"
- "LSDatabaseBuilder: Failed to read database from disk and couldn't create new one: %{public}@"
- "LSDatabaseBuilder: Seeding database with UID: %d, EUID %d"
- "LSDatabaseBuilder: error %d registering plugin %@"
- "LSDatabaseBuilder: registered plugin %@"
- "LSMIRegistrantServerStrategy"
- "LSMIResultRegistrantDatabaseContext"
- "LSMIResultRegistrantDatabaseContextProviding"
- "LSMIResultRegistrantStrategy"
- "Saved system content database to %@"
- "T@\"NSDate\",R,N,V_windowOpenDate"
- "^I"
- "^Q"
- "^d"
- "_windowOpenDate"
- "clientIsEntitledForPostInstallationOperations"
- "could not write out system content database! %@"
- "findOrRegisterContainerizedNodeReinitializingContext:installDictionary:personasWithAttributes:error:"
- "stale window, returning %@"
- "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1355:63)]"
- "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1386:65)]"
- "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1393:65)]"
- "static id LaunchServices::PrefsStorage::_GetValueInPrefsArrayWithPredicate(NSArray *__strong, __unsafe_unretained Class, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1386:65)]"
- "static id LaunchServices::PrefsStorage::_GetValueInPrefsArrayWithPredicate(NSArray *__strong, __unsafe_unretained Class, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1393:65)]"
- "v16@?0@\"<LSMIResultRegistrantDatabaseContextProviding>\"8"
- "v24@0:8@?<v@?@\"<LSMIResultRegistrantDatabaseContextProviding>\">16"
- "v24@0:8@?<v@?B@\"<LSMIResultRegistrantDatabaseContext>\"@\"NSError\">16"
- "v24@?0r^{LSDefaultAppCategoryInfo=Q^{__CFString}^{__CFString}Q^?^{LSDefaultAppCategorySubordinateClaim}Q}8^B16"
- "v28@?0B8@\"<LSMIResultRegistrantDatabaseContext>\"12@\"NSError\"20"
- "window open date %@"
- "windowOpenDate"
- "{?=\"hasLookedForLoctable\"b1}"

```
