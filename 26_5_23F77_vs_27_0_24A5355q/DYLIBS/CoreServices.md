## CoreServices

> `/System/Library/Frameworks/CoreServices.framework/CoreServices`

```diff

-1444.5.2.0.0
-  __TEXT.__text: 0x1b2b80
-  __TEXT.__auth_stubs: 0x30b0
-  __TEXT.__delay_stubs: 0x40
-  __TEXT.__delay_helper: 0x180
-  __TEXT.__objc_methlist: 0xcd54
-  __TEXT.__const: 0x910
-  __TEXT.__cstring: 0x2621e
-  __TEXT.__oslogstring: 0x13c30
-  __TEXT.__gcc_except_tab: 0x27938
+1498.0.0.0.0
+  __TEXT.__text: 0x1c2910
+  __TEXT.__delay_helper: 0x1b8
+  __TEXT.__lazy_helpers: 0xa8
+  __TEXT.__objc_methlist: 0xe00c
+  __TEXT.__const: 0x950
+  __TEXT.__cstring: 0x28615
+  __TEXT.__oslogstring: 0x15cdf
+  __TEXT.__gcc_except_tab: 0x28c28
   __TEXT.__ustring: 0x23c
-  __TEXT.__unwind_info: 0xb420
-  __TEXT.__objc_classname: 0x1f0e
-  __TEXT.__objc_methname: 0x1d256
-  __TEXT.__objc_methtype: 0xaa84
-  __TEXT.__objc_stubs: 0x103c0
-  __DATA_CONST.__got: 0xa90
-  __DATA_CONST.__const: 0x6db8
-  __DATA_CONST.__objc_classlist: 0x6b8
-  __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x140
+  __TEXT.__unwind_info: 0xc418
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x7370
+  __DATA_CONST.__objc_classlist: 0x7a8
+  __DATA_CONST.__objc_catlist: 0x78
+  __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5eb0
+  __DATA_CONST.__objc_selrefs: 0x6478
   __DATA_CONST.__objc_protorefs: 0x90
-  __DATA_CONST.__objc_superrefs: 0x570
-  __DATA_CONST.__objc_arraydata: 0x188
-  __AUTH_CONST.__auth_got: 0x1878
-  __AUTH_CONST.__const: 0x3650
-  __AUTH_CONST.__cfstring: 0x16b80
-  __AUTH_CONST.__objc_const: 0x13128
-  __AUTH_CONST.__objc_intobj: 0x828
+  __DATA_CONST.__objc_superrefs: 0x638
+  __DATA_CONST.__objc_arraydata: 0x990
+  __DATA_CONST.__got: 0xaf8
+  __AUTH_CONST.__const: 0x3ad0
+  __AUTH_CONST.__cfstring: 0x17760
+  __AUTH_CONST.__objc_const: 0x154a0
+  __AUTH_CONST.__weak_auth_got: 0x18
+  __AUTH_CONST.__lazy_load_got: 0x10
+  __AUTH_CONST.__objc_intobj: 0x7f8
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_arrayobj: 0x138
-  __AUTH.__objc_data: 0x2bc0
-  __AUTH.__data: 0x318
-  __DATA.__objc_ivar: 0xab4
-  __DATA.__data: 0x12c4
-  __DATA.__bss: 0xe88
+  __AUTH_CONST.__objc_arrayobj: 0x150
+  __AUTH_CONST.__auth_got: 0x1930
+  __AUTH.__objc_data: 0x33e0
+  __AUTH.__data: 0x320
+  __DATA.__objc_ivar: 0xbcc
+  __DATA.__data: 0x15c8
+  __DATA.__bss: 0xf50
   __DATA.__common: 0x40
-  __DATA_DIRTY.__objc_data: 0x1770
-  __DATA_DIRTY.__data: 0x50
+  __DATA_DIRTY.__objc_data: 0x18b0
+  __DATA_DIRTY.__data: 0x48
   __DATA_DIRTY.__crash_info: 0x148
-  __DATA_DIRTY.__bss: 0x8c8
+  __DATA_DIRTY.__bss: 0x8d0
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
-  - /System/Library/Frameworks/FileProvider.framework/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CoreServicesStore.framework/CoreServicesStore
   - /System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary
+  - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: FF03F7E0-C808-30B3-8402-40274E666712
-  Functions: 8756
-  Symbols:   28645
-  CStrings:  13700
+  UUID: 648F31F1-E506-384A-97D9-339880DC312C
+  Functions: 9445
+  Symbols:   30693
+  CStrings:  8960
 
Symbols:
+ +[LSApplicationExtensionRecord(Enumeration) enumeratorWithExtensionPointRecord:options:allowingRestrictedForReasons:]
+ +[LSApplicationRecord(Enumeration) enumeratorForCandidateAppsIgnoringEligibilityForCategory:options:]
+ +[LSApplicationRecord(Enumeration) enumeratorForCandidateAppsIgnoringEligibilityForCategory:options:].cold.1
+ +[LSBundleDataContainerMap containerMapWithDatabase:bundleBaseData:]
+ +[LSBundleDataContainerMap containerMapWithMap:]
+ +[LSBundleDataContainerMap containerMapWithNonPersonifiedContainer:]
+ +[LSBundleDataContainerMap emptyMap]
+ +[LSBundleDataContainerMap new]
+ +[LSBundleDataContainerMap supportsSecureCoding]
+ +[LSBundleGroupContainerMap containerMapWithDatabase:bundleBaseData:]
+ +[LSBundleGroupContainerMap containerMapWithMap:]
+ +[LSBundleGroupContainerMap containerMapWithNonPersonifiedContainers:]
+ +[LSBundleGroupContainerMap new]
+ +[LSBundleGroupContainerMap supportsSecureCoding]
+ +[LSBundlePersonaRecordMap supportsSecureCoding]
+ +[LSDExtensionLaunchConfigurationStore sharedServerInstance]
+ +[LSDExtensionLaunchConfigurationStore sharedServerInstance].cold.1
+ +[LSDServerExtensionLaunchConfigurationRegistrar sharedServerInstance]
+ +[LSDServerExtensionLaunchConfigurationRegistrar sharedServerInstance].cold.1
+ +[LSDocumentProxy(Binding) _bindingEvaluatorResultFilterForContentIsManaged:sourceAuditToken:]
+ +[LSDocumentProxy(Binding) _bindingEvaluatorResultFilterForContentIsManaged:sourceAuditToken:].cold.1
+ +[LSExtensionLaunchConfiguration systemRegistrar]
+ +[LSExtensionLaunchConfiguration systemRegistrar].cold.1
+ +[LSInstallInfo supportsSecureCoding]
+ +[LSInstallInfoOverrides supportsSecureCoding]
+ +[LSTransmissibleExtensionLaunchConfiguration supportsSecureCoding]
+ +[_LSDReadClient methodWithSelectorGetsImplicitExecutionContextRead:]
+ +[_LSDReadClient methodWithSelectorGetsImplicitExecutionContextRead:].cold.1
+ +[_LSEmptyContainerMap sharedInstance]
+ +[_LSEmptyContainerMap sharedInstance].cold.1
+ +[_LSEmptyContainerMap supportsSecureCoding]
+ +[_LSEmptyGroupContainerMap sharedInstance]
+ +[_LSEmptyGroupContainerMap sharedInstance].cold.1
+ +[_LSEmptyGroupContainerMap supportsSecureCoding]
+ +[_LSLazyGroupContainerMap supportsSecureCoding]
+ +[_LSMultiContainerMap supportsSecureCoding]
+ +[_LSMultiGroupContainerMap supportsSecureCoding]
+ +[_LSPersonaDatabase _getPersonaAttributesRetryingIfNecessary]
+ +[_LSPersonaDatabase _getPersonaAttributesRetryingIfNecessary].cold.1
+ +[_LSPersonaDatabase _getPersonaAttributesRetryingIfNecessary].cold.2
+ +[_LSPersonaWithAttributes(TestingAccess) makeWithPersonaType:personaUniqueString:]
+ +[_LSSingleContainerMap singleContainerMapWithPath:]
+ +[_LSSingleContainerMap singleContainerMapWithURL:]
+ +[_LSSingleContainerMap supportsSecureCoding]
+ +[_LSSingleGroupContainerMap supportsSecureCoding]
+ -[ICLAppExtensionRecord(LSExtensions) ls_isPlugin]
+ -[ICLBundleRecord(LSExtensions) ls_isApplicationOrPlaceholder]
+ -[ICLBundleRecord(LSExtensions) ls_isPlugin]
+ -[ICLBundleRecord(LSTransitional) ls_associatedPersonasIfAvailable]
+ -[ICLBundleRecord(LSTransitional) ls_associatedPersonasIfAvailable].cold.1
+ -[ICLPlaceholderRecord(LSExtensions) ls_isApplicationOrPlaceholder]
+ -[LSAppClipMetadata _appClipPlistBooleanForKey:]
+ -[LSApplicationExtensionRecord _transitional_mayLaunchInSystemProxy]
+ -[LSApplicationExtensionRecord personaIsApplicable:]
+ -[LSApplicationExtensionRecord personaOrPrimaryPersonaPlaceholderIsApplicable:]
+ -[LSApplicationExtensionRecord(AppInstallation) isPlaceholder]
+ -[LSApplicationExtensionRecord(Restrictions) initWithBundleIdentifier:allowingRestrictedForReasons:error:]
+ -[LSApplicationRecord _LSRecord_resolve_representedBundleIdentifier]
+ -[LSApplicationRecord hasCriticalAlertsEntitlement]
+ -[LSApplicationRecord localizedNameIsActive]
+ -[LSApplicationRecord representedBundleIdentifierWithContext:tableID:unitID:unitBytes:]
+ -[LSApplicationRecord representedBundleIdentifier]
+ -[LSApplicationRecord(Identities) identities].cold.2
+ -[LSApplicationRecord(InstallMachineryPrivate) _LSRecord_resolve_isDeletableSystemApplication]
+ -[LSApplicationRecord(InstallMachineryPrivate) _LSRecord_resolve_isDeletable]
+ -[LSApplicationRecord(InstallMachineryPrivate) isDeletableSystemApplicationWithContext:tableID:unitID:unitBytes:]
+ -[LSApplicationRecord(InstallMachineryPrivate) isDeletableSystemApplication]
+ -[LSApplicationRecord(InstallMachineryPrivate) isDeletableWithContext:tableID:unitID:unitBytes:]
+ -[LSApplicationRecord(InstallMachineryPrivate) isDeletable]
+ -[LSApplicationRestrictionsManager _LSResolveIdentifiers:identifiersAreNullable:context:]
+ -[LSApplicationRestrictionsManager _LSResolveNullableIdentifiers:]
+ -[LSApplicationRestrictionsManager _LSResolveNullableIdentifiers:context:]
+ -[LSApplicationRestrictionsManager _lazyLoadRestrictionsIdentifierSet:context:getter:]
+ -[LSApplicationRestrictionsManager _lazyLoadRestrictionsIdentifierSet:identifiersAreNullable:context:getter:]
+ -[LSApplicationRestrictionsManager _rawPartnerFinancingAllowlistedBundleIDsWithContext:]
+ -[LSApplicationRestrictionsManager _rawPartnerFinancingAllowlistedBundleIDs]
+ -[LSApplicationRestrictionsManager allowlistedBundleIDsWithContext:]
+ -[LSApplicationRestrictionsManager isApplicationRestricted:checkAppStateFlags:stateProvider:]
+ -[LSApplicationRestrictionsManager isApplicationRestricted:checkBundleFlags:]
+ -[LSApplicationRestrictionsManager isPartnerFinancingAllowlistEnabled]
+ -[LSApplicationRestrictionsManager isRatingAllowed:forBundleIdentifier:stateProvider:]
+ -[LSApplicationRestrictionsManager locked_clearPartnerFinancingAllowlistedBundleIDs]
+ -[LSApplicationRestrictionsManager locked_setParentalControlsRestrictedBundleIDs:]
+ -[LSApplicationRestrictionsManager locked_setRawPartnerFinancingAllowlistedBundleIDs:]
+ -[LSApplicationRestrictionsManager parentalControlsRestrictedBundleIDsWithContext:]
+ -[LSApplicationRestrictionsManager parentalControlsRestrictedBundleIDs]
+ -[LSApplicationRestrictionsManager partnerFinancingAllowlistedBundleIDsWithContext:]
+ -[LSApplicationRestrictionsManager partnerFinancingAllowlistedBundleIDs]
+ -[LSApplicationRestrictionsManager ratingRankExceptionBundleIDsWithContext:]
+ -[LSApplicationRestrictionsManager reasonForApplicationRestriction:checkAppStateFlags:stateProvider:]
+ -[LSApplicationRestrictionsManager reasonForApplicationRestriction:checkBundleFlags:stateProvider:]
+ -[LSApplicationRestrictionsManager restrictedBundleIDsWithContext:]
+ -[LSApplicationRestrictionsManager setStateProviderProvider:]
+ -[LSApplicationRestrictionsManager setTargetResolver:]
+ -[LSApplicationRestrictionsManager snapshotStateProviderWithContext:]
+ -[LSApplicationWorkspace _LSServer_scanRestrictionAffectedBundles:]
+ -[LSApplicationWorkspace _LSServer_scanRestrictionAffectedBundlesWithContext:scanBlock:]
+ -[LSApplicationWorkspace _setPersonaUniqueStrings:forApplicationsWithBundleIdentifiers:bundlePersonaRecordMapOrNil:operationUUID:requestContext:saveObserver:error:]
+ -[LSApplicationWorkspace personaWithAttributesForPersonaUniqueStringsIfAppropriate:]
+ -[LSApplicationWorkspace personaWithAttributesForPersonaUniqueStringsIfAppropriate:].cold.1
+ -[LSApplicationWorkspace registerApplicationDictionary:withObserverNotification:].cold.1
+ -[LSApplicationWorkspace registerApplicationForRebuildWithInstallInfo:requestContext:registrationError:]
+ -[LSApplicationWorkspace registerContainerizedApplicationWithInstallInfo:operationUUID:requestContext:saveObserver:registrationError:]
+ -[LSApplicationWorkspace removeReferencesToPersonaWithUniqueString:operationUUID:requestContext:saveObserver:error:]
+ -[LSApplicationWorkspace scanForAppsWithIdentifiersInSet:]
+ -[LSApplicationWorkspace setContainersForApplicationsWithBundleIdentifiers:unbundledExtensionsWithBundleIdentifiers:fromBundlePersonaRecordMap:operationUUID:requestContext:saveObserver:error:]
+ -[LSApplicationWorkspace setPersonaUniqueStrings:forApplicationsWithBundleIdentifiers:bundlePersonaRecordMap:operationUUID:requestContext:saveObserver:error:]
+ -[LSApplicationWorkspace(PersonaNiceties) bundleIdentifiersForPersonaWithPersonaUniqueString:error:]
+ -[LSApplicationWorkspace(PersonaNiceties) bundleIdentifiersForPersonasWithType:error:]
+ -[LSAskManagerMCStateProvider isPartnerFinancingAllowlistEnabled]
+ -[LSAskManagerMCStateProvider parentalControlsRestrictedBundleIDs]
+ -[LSAskManagerMCStateProvider partnerFinancingAllowlistedBundleIDs]
+ -[LSBuiltinApplicationRegistrant initWithStrategy:operationUUID:installInfo:]
+ -[LSBuiltinPluginRegistrant initWithStrategy:operationUUID:installInfo:]
+ -[LSBuiltinPluginRegistrant runWithCompletion:].cold.1
+ -[LSBundleDataContainerMap .cxx_destruct]
+ -[LSBundleDataContainerMap _initPrivately]
+ -[LSBundleDataContainerMap allPersonaUniqueStringsOrNilForNonPersonified]
+ -[LSBundleDataContainerMap bestDataContainerForCurrentPersona]
+ -[LSBundleDataContainerMap copyWithZone:]
+ -[LSBundleDataContainerMap dataContainerURLForPersonaUniqueString:]
+ -[LSBundleDataContainerMap encodeWithCoder:]
+ -[LSBundleDataContainerMap initWithCoder:]
+ -[LSBundleDataContainerMap init]
+ -[LSBundleGroupContainerMap _initPrivately]
+ -[LSBundleGroupContainerMap copyWithZone:]
+ -[LSBundleGroupContainerMap detach]
+ -[LSBundleGroupContainerMap encodeWithCoder:]
+ -[LSBundleGroupContainerMap groupContainersForCurrentPersona]
+ -[LSBundleGroupContainerMap groupContainersForPersonaUniqueString:]
+ -[LSBundleGroupContainerMap initWithCoder:]
+ -[LSBundleGroupContainerMap init]
+ -[LSBundlePersonaAssociationResult .cxx_destruct]
+ -[LSBundlePersonaAssociationResult error]
+ -[LSBundlePersonaAssociationResult initWithSuccessfulIdentifiers:success:error:]
+ -[LSBundlePersonaAssociationResult modifiedSomeRecords]
+ -[LSBundlePersonaAssociationResult success]
+ -[LSBundlePersonaAssociationResult successfulIdentifiers]
+ -[LSBundlePersonaRecordMap .cxx_destruct]
+ -[LSBundlePersonaRecordMap addBundlePersonaRecord:forBundleWithIdentifier:personaUniqueString:]
+ -[LSBundlePersonaRecordMap addBundlePersonaRecordsForICLBundleRecords:]
+ -[LSBundlePersonaRecordMap debugDescription]
+ -[LSBundlePersonaRecordMap encodeWithCoder:]
+ -[LSBundlePersonaRecordMap initWithCoder:]
+ -[LSBundlePersonaRecordMap initWithICLBundleRecords:]
+ -[LSBundlePersonaRecordMap init]
+ -[LSBundlePersonaRecordMap(Internal) bundlePersonaRecordForBundleID:personaUniqueString:]
+ -[LSBundlePersonaRecordMap(Internal) bundlePersonaRecordForBundleID:personaUniqueString:].cold.1
+ -[LSBundlePersonaRecordMap(Internal) personaRecordsByPersonaForBundleID:]
+ -[LSBundlePersonaRecordMap(Internal) validateWithContext:personaUniqueStrings:applicationBundleIDs:error:]
+ -[LSBundleProxy _initWithBundleUnit:context:bundleType:bundleID:localizedName:bundleContainerURL:resourcesDirectoryURL:iconsDictionary:iconFileNames:version:]
+ -[LSBundleProxy _initWithBundleUnit:context:bundleType:bundleID:localizedName:bundleContainerURL:resourcesDirectoryURL:iconsDictionary:iconFileNames:version:].cold.1
+ -[LSBundleRecord _LSRecord_resolve__bundleDataContainerMapFromDatabase]
+ -[LSBundleRecord _LSRecord_resolve__rawGroupContainerURLMap]
+ -[LSBundleRecord _LSRecord_resolve_codeSigningIdentifier]
+ -[LSBundleRecord _bundleDataContainerMapFromDatabaseWithContext:tableID:unitID:unitBytes:]
+ -[LSBundleRecord _bundleDataContainerMapFromDatabase]
+ -[LSBundleRecord _cachedDataContainerURLMap]
+ -[LSBundleRecord _groupContainerURLDictFromDatabase]
+ -[LSBundleRecord _personaUniqueStringsWithDataContainersInDatabaseOrNilIfNonPersonified]
+ -[LSBundleRecord _rawGroupContainerURLMapCheckingRedaction]
+ -[LSBundleRecord _rawGroupContainerURLMapCheckingRedaction].cold.1
+ -[LSBundleRecord _rawGroupContainerURLMapWithContext:tableID:unitID:unitBytes:]
+ -[LSBundleRecord _rawGroupContainerURLMap]
+ -[LSBundleRecord _setCachedDataContainerURLMap:]
+ -[LSBundleRecord codeSigningIdentifierWithContext:tableID:unitID:unitBytes:]
+ -[LSBundleRecord codeSigningIdentifier]
+ -[LSBundleRecord(Containers) dataContainerURLForPersonaWithUniqueString:error:]
+ -[LSBundleRecord(Containers) dataContainerURLForPersonaWithUniqueString:error:].cold.1
+ -[LSBundleRecord(Containers) getGroupContainersForPersonaWithUniqueString:createIfNecessary:error:]
+ -[LSBundleRecord(Containers) getGroupContainersForPersonaWithUniqueString:createIfNecessary:error:].cold.1
+ -[LSBundleRecord(Entitlements) hasBooleanEntitlement:]
+ -[LSBundleRecord(Personas) personaOrPrimaryPersonaPlaceholderIsApplicable:]
+ -[LSBundleRecordBuilder backgroundRuntimeUsageDescription]
+ -[LSBundleRecordBuilder buildBundleData:error:].cold.1
+ -[LSBundleRecordBuilder explicitlyRestrictable]
+ -[LSBundleRecordBuilder localizedBackgroundRuntimeUsageDescription]
+ -[LSBundleRecordBuilder representedBundleID]
+ -[LSBundleRecordBuilder setAndProcessInstallInfo:]
+ -[LSBundleRecordBuilder setInstallInfo:]
+ -[LSBundleRecordBuilder setRepresentedBundleID:]
+ -[LSBundleRecordUpdater getModifiedPluginDataForPluginUnit:]
+ -[LSBundleRecordUpdater parseBundlePersonaRecordMap:error:]
+ -[LSBundleRecordUpdater removeReferencesToPersona:error:]
+ -[LSBundleSetContainersOperation .cxx_destruct]
+ -[LSBundleSetContainersOperation executeWithContext:]
+ -[LSBundleSetContainersOperation executeWithContext:].cold.1
+ -[LSBundleSetContainersOperation initWithAppBundleIdentifiers:unbundledExtensionBundleIdentifiers:bundlePersonaRecordMap:]
+ -[LSBundleSetPersonaAssociationOperation .cxx_destruct]
+ -[LSBundleSetPersonaAssociationOperation _validatePersonaRecordMapWithContext:error:]
+ -[LSBundleSetPersonaAssociationOperation executeWithContext:]
+ -[LSBundleSetPersonaAssociationOperation executeWithContext:].cold.1
+ -[LSBundleSetPersonaAssociationOperation executeWithContext:].cold.2
+ -[LSBundleSetPersonaAssociationOperation initWithBundleIdentifiers:personas:bundlePersonaRecordMap:]
+ -[LSClaimBindingBindable baseBindingEvaluatorWithAuditToken:]
+ -[LSClaimBindingBindable defaultBindOptions]
+ -[LSClaimBindingConfiguration addClaimRecordIfMissing]
+ -[LSClaimBindingConfiguration setAddClaimRecordIfMissing:]
+ -[LSClaimBindingConfiguration setPreferApple:]
+ -[LSCleanReferencesToPersonaOperation .cxx_destruct]
+ -[LSCleanReferencesToPersonaOperation initWithPersonaUniqueString:]
+ -[LSCleanReferencesToPersonaOperation preflightWithContext:error:]
+ -[LSCleanReferencesToPersonaOperation preflightWithContext:error:].cold.1
+ -[LSCleanReferencesToPersonaOperation preflightWithContext:error:].cold.2
+ -[LSContainerCache .cxx_construct]
+ -[LSContainerCache .cxx_destruct]
+ -[LSContainerCache _cacheAndSetDataContainersForContainerizedCachableAppRecords:error:]
+ -[LSContainerCache _eduModeCacheAndSetDataContainersForContainerizedCachableAppRecords:error:]
+ -[LSContainerCache _processAppDataContainersFromContainermanagerForEduModeWithIdentifiers:locked:error:]
+ -[LSContainerCache _processAppDataContainersFromContainermanagerForEduModeWithIdentifiers:locked:error:].cold.1
+ -[LSContainerCache _processAppDataContainersFromContainermanagerForInstalledApplicationsForEduModeLocked:error:]
+ -[LSContainerCache _processAppDataContainersFromContainermanagerForInstalledApplicationsForEduModeLocked:error:].cold.1
+ -[LSContainerCache _processAppDataContainersFromContainermanagerWithRequiredContainers:locked:error:]
+ -[LSContainerCache _processInDatabaseAppDataContainerWithContext:bundleUnitID:bundleDataIfAvailable:missingContainerMapForNonDatabaseRecords:locked:]
+ -[LSContainerCache _processInDatabaseAppDataContainerWithContext:bundleUnitID:bundleDataIfAvailable:missingContainerMapForNonDatabaseRecords:locked:].cold.1
+ -[LSContainerCache _processInDatabaseAppDataContainerWithContext:bundleUnitID:bundleDataIfAvailable:missingContainerMapForNonDatabaseRecords:locked:].cold.2
+ -[LSContainerCache _processInDatabaseAppDataContainerWithContext:bundleUnitID:bundleDataIfAvailable:missingContainerMapForNonDatabaseRecords:locked:].cold.3
+ -[LSContainerCache _processInDatabaseAppDataContainersWithContext:locked:]
+ -[LSContainerCache _setDataContainersOnApplicationRecordsFromCache:locked:]
+ -[LSContainerCache appDataContainerMapLocked:]
+ -[LSContainerCache cacheAndSetDataContainersForApplicationRecords:error:]
+ -[LSContainerCache cacheDataContainersForInstalledApplicationsWithError:]
+ -[LSContainerCache(Internal) forceQueryContainerManager]
+ -[LSContainerCache(Internal) setForceQueryContainerManager:]
+ -[LSDExtensionLaunchConfigurationStore .cxx_destruct]
+ -[LSDExtensionLaunchConfigurationStore _bootInfoFileURL]
+ -[LSDExtensionLaunchConfigurationStore _clearStorageDirectory]
+ -[LSDExtensionLaunchConfigurationStore _currentBootUUID]
+ -[LSDExtensionLaunchConfigurationStore _currentBootUUID].cold.1
+ -[LSDExtensionLaunchConfigurationStore _generateNonce]
+ -[LSDExtensionLaunchConfigurationStore _initializeStorage]
+ -[LSDExtensionLaunchConfigurationStore _initializeStorage].cold.1
+ -[LSDExtensionLaunchConfigurationStore _initializeStorage].cold.2
+ -[LSDExtensionLaunchConfigurationStore _initializeStorage].cold.3
+ -[LSDExtensionLaunchConfigurationStore _initializeStorage].cold.4
+ -[LSDExtensionLaunchConfigurationStore _readBootInfo]
+ -[LSDExtensionLaunchConfigurationStore _readBootInfo].cold.1
+ -[LSDExtensionLaunchConfigurationStore _readBootInfo].cold.2
+ -[LSDExtensionLaunchConfigurationStore _writeBootInfo:nonce:]
+ -[LSDExtensionLaunchConfigurationStore _writeBootInfo:nonce:].cold.1
+ -[LSDExtensionLaunchConfigurationStore _writeBootInfo:nonce:].cold.2
+ -[LSDExtensionLaunchConfigurationStore bootNonce]
+ -[LSDExtensionLaunchConfigurationStore fetchConfigurationWithUUID:error:]
+ -[LSDExtensionLaunchConfigurationStore fetchConfigurationWithUUID:error:].cold.1
+ -[LSDExtensionLaunchConfigurationStore fetchConfigurationWithUUID:error:].cold.2
+ -[LSDExtensionLaunchConfigurationStore fetchConfigurationWithUUID:error:].cold.3
+ -[LSDExtensionLaunchConfigurationStore init]
+ -[LSDExtensionLaunchConfigurationStore registerConfiguration:error:]
+ -[LSDExtensionLaunchConfigurationStore registerConfiguration:error:].cold.1
+ -[LSDExtensionLaunchConfigurationStore registerConfiguration:error:].cold.2
+ -[LSDExtensionLaunchConfigurationStore registerConfiguration:error:].cold.3
+ -[LSDExtensionLaunchConfigurationStore registerConfiguration:error:].cold.4
+ -[LSDExtensionLaunchConfigurationStore setBootNonce:]
+ -[LSDExtensionLaunchConfigurationStore storageDirectoryURL]
+ -[LSDServerExtensionLaunchConfigurationRegistrar .cxx_destruct]
+ -[LSDServerExtensionLaunchConfigurationRegistrar fetchRegisteredConfigurationWithUUID:error:]
+ -[LSDServerExtensionLaunchConfigurationRegistrar initWithResolver:store:]
+ -[LSDServerExtensionLaunchConfigurationRegistrar initWithResolver:store:].cold.1
+ -[LSDServerExtensionLaunchConfigurationRegistrar initWithResolver:store:].cold.2
+ -[LSDServerExtensionLaunchConfigurationRegistrar queue]
+ -[LSDServerExtensionLaunchConfigurationRegistrar registerTransmissibleLaunchConfiguration:forExtensionWithUUID:hostPersonaUniqueString:hostAuditToken:error:]
+ -[LSDServerExtensionLaunchConfigurationRegistrar resolver]
+ -[LSDServerExtensionLaunchConfigurationRegistrar store]
+ -[LSDatabaseRebuildContext registerBundleContainerizedICLItem:fromInstallInfo:]
+ -[LSDatabaseRebuildContext registerICLItemForSystemContent:fromInstallInfo:]
+ -[LSExtensionLaunchConfiguration .cxx_destruct]
+ -[LSExtensionLaunchConfiguration additionalConfiguration]
+ -[LSExtensionLaunchConfiguration initWithPersonaUniqueString:additionalConfiguration:]
+ -[LSExtensionLaunchConfiguration init]
+ -[LSExtensionLaunchConfiguration personaUniqueString]
+ -[LSExtensionLaunchConfigurationAppRecordWrapper .cxx_destruct]
+ -[LSExtensionLaunchConfigurationAppRecordWrapper associatedPersonas]
+ -[LSExtensionLaunchConfigurationAppRecordWrapper hasBooleanEntitlement:]
+ -[LSExtensionLaunchConfigurationAppRecordWrapper initWithAppRecord:]
+ -[LSExtensionLaunchConfigurationClientSystemRegistrar fetchRegisteredConfigurationWithUUID:additionalConfigurationClass:error:]
+ -[LSExtensionLaunchConfigurationClientSystemRegistrar registerLaunchConfiguration:forExtensionWithUUID:hostPersonaUniqueString:hostAuditToken:error:]
+ -[LSExtensionLaunchConfigurationExtensionRecordWrapper .cxx_destruct]
+ -[LSExtensionLaunchConfigurationExtensionRecordWrapper containingApplication]
+ -[LSExtensionLaunchConfigurationExtensionRecordWrapper hasBooleanEntitlement:]
+ -[LSExtensionLaunchConfigurationExtensionRecordWrapper initWithExtensionRecord:]
+ -[LSExtensionLaunchConfigurationResolutionLSDBProvoder extensionWithUUID:error:]
+ -[LSExtensionLaunchConfigurationResolver .cxx_destruct]
+ -[LSExtensionLaunchConfigurationResolver bestLaunchPersonaForExtension:hostPersona:hostAuditToken:error:]
+ -[LSExtensionLaunchConfigurationResolver initWithPersonaInfoProvider:databaseProvider:]
+ -[LSExtensionLaunchConfigurationResolver isPersona:acceptableForExtension:hostPersona:hostAuditToken:]
+ -[LSExtensionLaunchConfigurationResolver resolveConfiguration:forExtensionWithUUID:hostPersonaUniqueString:hostAuditToken:error:]
+ -[LSExtensionLaunchConfigurationResolver resolveConfiguration:forExtensionWithUUID:hostPersonaUniqueString:hostAuditToken:error:].cold.1
+ -[LSExtensionLaunchConfigurationResolver resolveConfiguration:forExtensionWithUUID:hostPersonaUniqueString:hostAuditToken:error:].cold.2
+ -[LSExtensionLaunchConfigurationResolver resolveConfiguration:forExtensionWithUUID:hostPersonaUniqueString:hostAuditToken:error:].cold.3
+ -[LSExtensionLaunchConfigurationResolver resolveConfiguration:forExtensionWithUUID:hostPersonaUniqueString:hostAuditToken:error:].cold.4
+ -[LSInstallInfo .cxx_destruct]
+ -[LSInstallInfo appOrPlaceholderRecord]
+ -[LSInstallInfo bundleRecordForBundleIdentifier:]
+ -[LSInstallInfo copyOverrides]
+ -[LSInstallInfo copyWithOverrides:]
+ -[LSInstallInfo copyWithZone:]
+ -[LSInstallInfo encodeWithCoder:]
+ -[LSInstallInfo extensionBundleRecords]
+ -[LSInstallInfo hasInfoForBundleIdentifier:]
+ -[LSInstallInfo initWithCoder:]
+ -[LSInstallInfo initWithICLBundleRecords:personasWithAttributes:]
+ -[LSInstallInfo initWithICLBundleRecords:personasWithAttributes:].cold.1
+ -[LSInstallInfo initWithICLBundleRecordsInferringPersonas:]
+ -[LSInstallInfo initWithLegacyDictionaries:personasWithAttributes:]
+ -[LSInstallInfo initWithLegacyDictionaries:personasWithAttributes:].cold.1
+ -[LSInstallInfo init]
+ -[LSInstallInfo isDowngrade]
+ -[LSInstallInfo isErsatz]
+ -[LSInstallInfo isParallelPlaceholder]
+ -[LSInstallInfo isPlaceholder]
+ -[LSInstallInfo legacyDictionaryForBundleIdentifier:]
+ -[LSInstallInfo personasWithAttributes]
+ -[LSInstallInfo pluginHasOverride]
+ -[LSInstallInfoOverrides .cxx_destruct]
+ -[LSInstallInfoOverrides copyWithZone:]
+ -[LSInstallInfoOverrides encodeWithCoder:]
+ -[LSInstallInfoOverrides initWithCoder:]
+ -[LSInstallInfoOverrides init]
+ -[LSInstallInfoOverrides isDowngrade]
+ -[LSInstallInfoOverrides isParallelPlaceholder]
+ -[LSInstallInfoOverrides isPlaceholder]
+ -[LSInstallInfoOverrides pluginHasOverride]
+ -[LSInstallInfoOverrides setIsDowngrade:]
+ -[LSInstallInfoOverrides setIsParallelPlaceholder:]
+ -[LSInstallInfoOverrides setIsPlaceholder:]
+ -[LSInstallInfoOverrides setPluginHasOverride:]
+ -[LSMIResultRegistrant initWithStrategy:operationUUID:installInfo:]
+ -[LSMIResultRegistrantTrueDatabaseContext registerBundleNodeReinitializingContext:inBundleContainer:installInfo:error:]
+ -[LSMIResultRegistrantTrueDatabaseContext registerPluginNodeReinitializingContext:installInfo:existingPlugin:error:]
+ -[LSMIResultUnregistrant initWithStrategy:operationUUID:bundleIdentifier:precondition:type:]
+ -[LSPreflightedCleanReferencesToPersonaOperation .cxx_construct]
+ -[LSPreflightedCleanReferencesToPersonaOperation .cxx_destruct]
+ -[LSPreflightedCleanReferencesToPersonaOperation executeWithContext:]
+ -[LSPreflightedCleanReferencesToPersonaOperation initWithPersonaUniqueString:affectedApps:affectedStandalonePlugins:]
+ -[LSRebuildStatisticsGatherer performContainerFixups:]
+ -[LSRebuildStatisticsGatherer registeredICLBundle:]
+ -[LSRestrictionsTargetResolver .cxx_construct]
+ -[LSRestrictionsTargetResolver .cxx_destruct]
+ -[LSRestrictionsTargetResolver resolveIdentifiers:context:]
+ -[LSStandalonePluginRecordUpdater .cxx_construct]
+ -[LSStandalonePluginRecordUpdater .cxx_destruct]
+ -[LSStandalonePluginRecordUpdater initWithDatabase:pluginUnit:pluginData:]
+ -[LSStandalonePluginRecordUpdater parseBundlePersonaRecordMap:error:]
+ -[LSStandalonePluginRecordUpdater updatePluginRecord:]
+ -[LSTransmissibleExtensionLaunchConfiguration .cxx_destruct]
+ -[LSTransmissibleExtensionLaunchConfiguration additionalConfigurationDigest]
+ -[LSTransmissibleExtensionLaunchConfiguration codedAdditionalConfiguration]
+ -[LSTransmissibleExtensionLaunchConfiguration digest]
+ -[LSTransmissibleExtensionLaunchConfiguration encodeWithCoder:]
+ -[LSTransmissibleExtensionLaunchConfiguration initWithCoder:]
+ -[LSTransmissibleExtensionLaunchConfiguration initWithPersonaUniqueString:codedAdditionalConfiguration:additionalConfigurationDigest:]
+ -[LSTransmissibleExtensionLaunchConfiguration personaUniqueString]
+ -[LSTransmissibleExtensionLaunchConfiguration(CopyChangingPersona) _copyChangingPersonaToPersona:]
+ -[LSUseValuesMCStateProvider initWithAllowlistEnabled:allowlistedBundles:partnerFinancingAllowlistedBundles:restrictedBundles:parentalControlsRestrictedBundles:ratingRankExceptions:maximumRating:]
+ -[LSUseValuesMCStateProvider isPartnerFinancingAllowlistEnabled]
+ -[LSUseValuesMCStateProvider parentalControlsRestrictedBundleIDs]
+ -[LSUseValuesMCStateProvider partnerFinancingAllowlistedBundleIDs]
+ -[LSWorkPipe .cxx_construct]
+ -[LSWorkPipe .cxx_destruct]
+ -[LSWorkPipe _racy_wasRunning]
+ -[LSWorkPipe _runWork:]
+ -[LSWorkPipe drain]
+ -[LSWorkPipe enqueueWork:]
+ -[LSWorkPipe initWithDepth:label:]
+ -[LSWorkPipe invalidate]
+ -[NSArray(LSAdditions) ls_containsStringWithPrefix:]
+ -[NSNull(NSNull_LSAdditions) ls_isNull]
+ -[NSObject(NSNull_LSAdditions) ls_isNull]
+ -[_LSAggregatePropertyList allKeys]
+ -[_LSApplicationExtensionRecordEnumerator initWithExtensionPoint:options:allowingRestrictedForReasons:]
+ -[_LSClaimBindingDocumentProxyBindable baseBindingEvaluatorWithAuditToken:]
+ -[_LSClaimBindingDocumentProxyBindable defaultBindOptions]
+ -[_LSClaimBindingDocumentProxyBindable initWithProxy:bindingStyle:]
+ -[_LSClaimBindingTypeIdentifierBindable baseBindingEvaluatorWithAuditToken:]
+ -[_LSClaimBindingURLBindable baseBindingEvaluatorWithAuditToken:]
+ -[_LSCompatibilityNothingBindable baseBindingEvaluatorWithAuditToken:]
+ -[_LSCompatibilityNothingBindable baseBindingEvaluatorWithAuditToken:].cold.1
+ -[_LSCoreTypesRecordProxy codeSigningIdentifier]
+ -[_LSDModifyClient performPostInstallationRegistration:operationUUID:reply:]
+ -[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:bundlePersonaRecordMap:operationUUID:reply:]
+ -[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:bundlePersonaRecordMap:operationUUID:reply:].cold.1
+ -[_LSDModifyClient registerBuiltinApplication:operationUUID:reply:]
+ -[_LSDModifyClient registerItemInfo:alias:diskImageAlias:bundleURL:installInfo:completionHandler:]
+ -[_LSDModifyClient removeReferencesToPersonaWithUniqueString:operationUUID:reply:]
+ -[_LSDModifyClient setContainersForApplicationsWithBundleIdentifiers:unbundledExtensionsWithBundleIdentifiers:fromBundlePersonaRecordMap:operationUUID:reply:]
+ -[_LSDReadClient fetchRegisteredConfigurationWithUUID:completion:]
+ -[_LSDReadClient getPersonalPersonaUniqueString:]
+ -[_LSDReadClient getTypeRecordForPromiseAtURL:completionHandler:]
+ -[_LSDReadClient registerExtensionLaunchConfiguration:forExtensionWithUUID:hostPersonaUniqueString:hostAuditTokenData:completion:]
+ -[_LSDRebuildClient performRebuildRegistration:reply:]
+ -[_LSDRebuildClient performRebuildRegistration:reply:].cold.1
+ -[_LSDataBackedPropertyList allKeys]
+ -[_LSDefaults baseDatabaseStoreFileName]
+ -[_LSDefaults databaseCachesContainers]
+ -[_LSDefaults databaseCachesContainers].cold.1
+ -[_LSDefaults databaseCachesContainers].cold.2
+ -[_LSDefaults deviceConfigurationUsesPersonas]
+ -[_LSDefaults extensionLaunchConfigurationsURL]
+ -[_LSDefaults sandboxExtensionForCreatedDiagnosticsStashDirectoryURLWithError:]
+ -[_LSDefaults sandboxExtensionForCreatedDiagnosticsStashDirectoryURLWithError:].cold.1
+ -[_LSDefaults sandboxExtensionForCreatedDiagnosticsStashDirectoryURLWithError:].cold.2
+ -[_LSDefaults sandboxExtensionForCreatedDiagnosticsStashDirectoryURLWithError:].cold.3
+ -[_LSDefaults sandboxExtensionForCreatedDiagnosticsStashDirectoryURLWithError:].cold.4
+ -[_LSDefaults systemDataDiagnosticsStashDirectoryURLWithError:]
+ -[_LSDefaults systemDataDiagnosticsStashDirectoryURLWithError:].cold.1
+ -[_LSDefaults systemDataDiagnosticsStashDirectoryURLWithError:].cold.2
+ -[_LSDefaults systemDataDiagnosticsStashedDatabaseURLWithError:]
+ -[_LSDictionaryBackedPropertyList allKeys]
+ -[_LSEmptyContainerMap allPersonaUniqueStringsOrNilForNonPersonified]
+ -[_LSEmptyContainerMap bestDataContainerForCurrentPersona]
+ -[_LSEmptyContainerMap copyWithZone:]
+ -[_LSEmptyContainerMap dataContainerURLForPersonaUniqueString:]
+ -[_LSEmptyContainerMap encodeWithCoder:]
+ -[_LSEmptyContainerMap initPrivate]
+ -[_LSEmptyContainerMap initWithCoder:]
+ -[_LSEmptyGroupContainerMap copyWithZone:]
+ -[_LSEmptyGroupContainerMap encodeWithCoder:]
+ -[_LSEmptyGroupContainerMap groupContainersForCurrentPersona]
+ -[_LSEmptyGroupContainerMap groupContainersForPersonaUniqueString:]
+ -[_LSEmptyGroupContainerMap initPrivate]
+ -[_LSEmptyGroupContainerMap initWithCoder:]
+ -[_LSEmptyPropertyList allKeys]
+ -[_LSInstallProgressService observerPayloadForNotification:appProxies:]
+ -[_LSLazyGroupContainerMap .cxx_destruct]
+ -[_LSLazyGroupContainerMap copyWithZone:]
+ -[_LSLazyGroupContainerMap detach]
+ -[_LSLazyGroupContainerMap encodeWithCoder:]
+ -[_LSLazyGroupContainerMap groupContainersForCurrentPersona]
+ -[_LSLazyGroupContainerMap groupContainersForCurrentPersona].cold.1
+ -[_LSLazyGroupContainerMap groupContainersForPersonaUniqueString:]
+ -[_LSLazyGroupContainerMap groupContainersForPersonaUniqueString:].cold.1
+ -[_LSLazyGroupContainerMap initWithCoder:]
+ -[_LSLazyGroupContainerMap initWithLazyPropertyList:]
+ -[_LSLazyPropertyList allKeys]
+ -[_LSMultiContainerMap .cxx_destruct]
+ -[_LSMultiContainerMap allPersonaUniqueStringsOrNilForNonPersonified]
+ -[_LSMultiContainerMap bestDataContainerForCurrentPersona]
+ -[_LSMultiContainerMap bestDataContainerForCurrentPersona].cold.1
+ -[_LSMultiContainerMap copyWithZone:]
+ -[_LSMultiContainerMap dataContainerURLForPersonaUniqueString:]
+ -[_LSMultiContainerMap dataContainerURLForPersonaUniqueString:].cold.1
+ -[_LSMultiContainerMap encodeWithCoder:]
+ -[_LSMultiContainerMap initWithCoder:]
+ -[_LSMultiContainerMap initWithMap:]
+ -[_LSMultiGroupContainerMap .cxx_destruct]
+ -[_LSMultiGroupContainerMap copyWithZone:]
+ -[_LSMultiGroupContainerMap encodeWithCoder:]
+ -[_LSMultiGroupContainerMap groupContainersForCurrentPersona]
+ -[_LSMultiGroupContainerMap groupContainersForCurrentPersona].cold.1
+ -[_LSMultiGroupContainerMap groupContainersForPersonaUniqueString:]
+ -[_LSMultiGroupContainerMap groupContainersForPersonaUniqueString:].cold.1
+ -[_LSMultiGroupContainerMap initWithCoder:]
+ -[_LSMultiGroupContainerMap initWithMap:]
+ -[_LSOpenConfiguration includeAppLinksForCallingApplication]
+ -[_LSOpenConfiguration setIncludeAppLinksForCallingApplication:]
+ -[_LSPersonaDatabase _injectPersonaWithAttributesIntoCacheIfUnknown:]
+ -[_LSPersonaDatabase getCachedBundleIDToPersonasWithAttributesMap:personaUniqueStringToPersonasMap:systemPersona:personalPersona:]
+ -[_LSPersonaDatabase getPersonalPersonaWithAttributes]
+ -[_LSPersonaDatabase getPersonalPersonaWithAttributes].cold.1
+ -[_LSPersonaDatabase getSystemPersonaWithAttributes]
+ -[_LSPersonaDatabase getSystemPersonaWithAttributes].cold.1
+ -[_LSPersonaDatabase getUncachedBundleIDToPersonasWithAttributesMap:personaUniqueStringToPersonasMap:systemPersona:personalPersona:]
+ -[_LSPersonaDatabase personaWithAttributesForPersonaUniqueString:error:]
+ -[_LSPersonaDatabase personaWithAttributesForPersonaUniqueString:error:].cold.1
+ -[_LSPersonaWithAttributes isMemberOfTypeMask:]
+ -[_LSPersonaWithAttributes(TestingAccess) indirectPersonaType]
+ -[_LSPersonaWithAttributes(TestingAccess) indirectPersonaUniqueString]
+ -[_LSPlistHint restoredKeys]
+ -[_LSSingleContainerMap .cxx_destruct]
+ -[_LSSingleContainerMap allPersonaUniqueStringsOrNilForNonPersonified]
+ -[_LSSingleContainerMap bestDataContainerForCurrentPersona]
+ -[_LSSingleContainerMap copyWithZone:]
+ -[_LSSingleContainerMap dataContainerURLForPersonaUniqueString:]
+ -[_LSSingleContainerMap encodeWithCoder:]
+ -[_LSSingleContainerMap initWithCoder:]
+ -[_LSSingleContainerMap initWithURL:]
+ -[_LSSingleGroupContainerMap .cxx_destruct]
+ -[_LSSingleGroupContainerMap copyWithZone:]
+ -[_LSSingleGroupContainerMap encodeWithCoder:]
+ -[_LSSingleGroupContainerMap groupContainersForCurrentPersona]
+ -[_LSSingleGroupContainerMap groupContainersForPersonaUniqueString:]
+ -[_LSSingleGroupContainerMap initWithCoder:]
+ -[_LSSingleGroupContainerMap initWithGroupContainers:]
+ -[_UTDeclaredTypeRecord _replacementObjectForResolvedPropertyValue:forGetter:encoder:]
+ GCC_except_table155
+ GCC_except_table156
+ GCC_except_table163
+ GCC_except_table169
+ GCC_except_table170
+ GCC_except_table171
+ GCC_except_table177
+ GCC_except_table181
+ GCC_except_table198
+ GCC_except_table200
+ GCC_except_table204
+ GCC_except_table205
+ GCC_except_table214
+ GCC_except_table221
+ GCC_except_table228
+ GCC_except_table236
+ GCC_except_table239
+ GCC_except_table240
+ GCC_except_table242
+ GCC_except_table254
+ GCC_except_table255
+ GCC_except_table264
+ GCC_except_table266
+ GCC_except_table267
+ GCC_except_table269
+ GCC_except_table271
+ GCC_except_table274
+ GCC_except_table278
+ GCC_except_table280
+ GCC_except_table281
+ GCC_except_table284
+ GCC_except_table292
+ GCC_except_table300
+ GCC_except_table305
+ GCC_except_table311
+ GCC_except_table321
+ GCC_except_table325
+ GCC_except_table326
+ GCC_except_table327
+ GCC_except_table340
+ GCC_except_table343
+ GCC_except_table349
+ GCC_except_table353
+ GCC_except_table362
+ GCC_except_table368
+ GCC_except_table372
+ GCC_except_table373
+ GCC_except_table375
+ GCC_except_table383
+ GCC_except_table388
+ GCC_except_table389
+ GCC_except_table391
+ GCC_except_table406
+ GCC_except_table407
+ GCC_except_table411
+ GCC_except_table453
+ GCC_except_table459
+ GCC_except_table463
+ GCC_except_table465
+ GCC_except_table470
+ GCC_except_table471
+ GCC_except_table474
+ GCC_except_table486
+ GCC_except_table506
+ GCC_except_table507
+ GCC_except_table510
+ GCC_except_table513
+ GCC_except_table515
+ GCC_except_table516
+ GCC_except_table550
+ _CC_SHA256_Final
+ _CC_SHA256_Init
+ _CC_SHA256_Update
+ _FPExtendBookmarkForDocumentURL$lazyAuthGOT_IA_0
+ _FPExtendBookmarkForDocumentURL$lazyAuthGOT_IA_0$loadHelper_x8
+ _FPExtendBookmarkForDocumentURL$lazyAuthGOT_IA_ad_0
+ _FPExtendBookmarkForDocumentURL$lazyLoadStub
+ _LSBundleGroupContainerNonPersonifiedKey
+ _LSIncludeAppLinksForCallingApplicationKey
+ _LSPersonaTypeForMask
+ _LSPersonaTypeForUMUserPersonaType
+ _LSPersonaTypeMaskForType
+ _LSRestrictionReasonMaskForRestrictionReason
+ _LSUMUserPersonaTypeForLSPersonaType
+ _MDTCreateCopierWithSandboxExtensionAndReturnError.cold.1
+ _MDTCreateCopierWithSandboxExtensionAndReturnError.cold.2
+ _OBJC_CLASS_$_BSProcessHandle$loadHelper_x8
+ _OBJC_CLASS_$_ICLAppRecord
+ _OBJC_CLASS_$_ICLBundlePersonaRecord
+ _OBJC_CLASS_$_ICLBundleRecord
+ _OBJC_CLASS_$_ICLPlaceholderRecord
+ _OBJC_CLASS_$_ICLSystemAppPlaceholderRecord
+ _OBJC_CLASS_$_LSBundleDataContainerMap
+ _OBJC_CLASS_$_LSBundleGroupContainerMap
+ _OBJC_CLASS_$_LSBundlePersonaAssociationResult
+ _OBJC_CLASS_$_LSBundlePersonaRecordMap
+ _OBJC_CLASS_$_LSBundleSetContainersOperation
+ _OBJC_CLASS_$_LSBundleSetPersonaAssociationOperation
+ _OBJC_CLASS_$_LSCleanReferencesToPersonaOperation
+ _OBJC_CLASS_$_LSContainerCache
+ _OBJC_CLASS_$_LSDExtensionLaunchConfigurationStore
+ _OBJC_CLASS_$_LSDServerExtensionLaunchConfigurationRegistrar
+ _OBJC_CLASS_$_LSExtensionLaunchConfiguration
+ _OBJC_CLASS_$_LSExtensionLaunchConfigurationAppRecordWrapper
+ _OBJC_CLASS_$_LSExtensionLaunchConfigurationClientSystemRegistrar
+ _OBJC_CLASS_$_LSExtensionLaunchConfigurationExtensionRecordWrapper
+ _OBJC_CLASS_$_LSExtensionLaunchConfigurationResolutionLSDBProvoder
+ _OBJC_CLASS_$_LSExtensionLaunchConfigurationResolver
+ _OBJC_CLASS_$_LSInstallInfo
+ _OBJC_CLASS_$_LSInstallInfoOverrides
+ _OBJC_CLASS_$_LSPreflightedCleanReferencesToPersonaOperation
+ _OBJC_CLASS_$_LSRestrictionsTargetResolver
+ _OBJC_CLASS_$_LSStandalonePluginRecordUpdater
+ _OBJC_CLASS_$_LSTransmissibleExtensionLaunchConfiguration
+ _OBJC_CLASS_$_LSWorkPipe
+ _OBJC_CLASS_$_MSUDataAccessor
+ _OBJC_CLASS_$_MSUDataAccessor$loadHelper_x20
+ _OBJC_CLASS_$_NSDistributedNotificationCenter
+ _OBJC_CLASS_$__LSEmptyContainerMap
+ _OBJC_CLASS_$__LSEmptyGroupContainerMap
+ _OBJC_CLASS_$__LSLazyGroupContainerMap
+ _OBJC_CLASS_$__LSMultiContainerMap
+ _OBJC_CLASS_$__LSMultiGroupContainerMap
+ _OBJC_CLASS_$__LSSingleContainerMap
+ _OBJC_CLASS_$__LSSingleGroupContainerMap
+ _OBJC_IVAR_$_LSApplicationRestrictionsManager._parentalControlsRestrictedBundleIDs
+ _OBJC_IVAR_$_LSApplicationRestrictionsManager._partnerFinancingAllowlistedBundleIDs
+ _OBJC_IVAR_$_LSApplicationRestrictionsManager._stateProviderProvider
+ _OBJC_IVAR_$_LSApplicationRestrictionsManager._targetResolver
+ _OBJC_IVAR_$_LSBuiltinApplicationRegistrant._installInfo
+ _OBJC_IVAR_$_LSBuiltinPluginRegistrant._installInfo
+ _OBJC_IVAR_$_LSBundleDataContainerMap._allPersonaUniqueStringsOrNilForNonPersonified
+ _OBJC_IVAR_$_LSBundlePersonaAssociationResult._error
+ _OBJC_IVAR_$_LSBundlePersonaAssociationResult._success
+ _OBJC_IVAR_$_LSBundlePersonaAssociationResult._successfulIdentifiers
+ _OBJC_IVAR_$_LSBundlePersonaRecordMap._recordMap
+ _OBJC_IVAR_$_LSBundleRecord.__rawGroupContainerURLs
+ _OBJC_IVAR_$_LSBundleRecord._cachedDataContainerURLMap
+ _OBJC_IVAR_$_LSBundleRecordBuilder._backgroundRuntimeUsageDescription
+ _OBJC_IVAR_$_LSBundleRecordBuilder._explicitlyRestrictable
+ _OBJC_IVAR_$_LSBundleRecordBuilder._installInfo
+ _OBJC_IVAR_$_LSBundleRecordBuilder._localizedBackgroundRuntimeUsageDescription
+ _OBJC_IVAR_$_LSBundleRecordBuilder._representedBundleID
+ _OBJC_IVAR_$_LSBundleRecordUpdater._arraysToRelease
+ _OBJC_IVAR_$_LSBundleRecordUpdater._bundleDataContainerReleaseOperations
+ _OBJC_IVAR_$_LSBundleRecordUpdater._plistsToRelease
+ _OBJC_IVAR_$_LSBundleRecordUpdater._stringsToRelease
+ _OBJC_IVAR_$_LSBundleSetContainersOperation._appBundleIDs
+ _OBJC_IVAR_$_LSBundleSetContainersOperation._bundlePersonaRecordMap
+ _OBJC_IVAR_$_LSBundleSetContainersOperation._unbundledExtensionBundleIDs
+ _OBJC_IVAR_$_LSBundleSetPersonaAssociationOperation._bundleIDs
+ _OBJC_IVAR_$_LSBundleSetPersonaAssociationOperation._bundlePersonaRecordMap
+ _OBJC_IVAR_$_LSBundleSetPersonaAssociationOperation._personas
+ _OBJC_IVAR_$_LSCleanReferencesToPersonaOperation._personaUniqueString
+ _OBJC_IVAR_$_LSContainerCache._appDataContainers
+ _OBJC_IVAR_$_LSContainerCache._containerCacheLock
+ _OBJC_IVAR_$_LSContainerCache._flags
+ _OBJC_IVAR_$_LSDExtensionLaunchConfigurationStore._bootNonce
+ _OBJC_IVAR_$_LSDServerExtensionLaunchConfigurationRegistrar._queue
+ _OBJC_IVAR_$_LSDServerExtensionLaunchConfigurationRegistrar._resolver
+ _OBJC_IVAR_$_LSDServerExtensionLaunchConfigurationRegistrar._store
+ _OBJC_IVAR_$_LSDatabaseRebuildContext._workPipe
+ _OBJC_IVAR_$_LSExtensionLaunchConfiguration._additionalConfiguration
+ _OBJC_IVAR_$_LSExtensionLaunchConfiguration._personaUniqueString
+ _OBJC_IVAR_$_LSExtensionLaunchConfigurationAppRecordWrapper._app
+ _OBJC_IVAR_$_LSExtensionLaunchConfigurationExtensionRecordWrapper._appex
+ _OBJC_IVAR_$_LSExtensionLaunchConfigurationResolver._databaseProvider
+ _OBJC_IVAR_$_LSExtensionLaunchConfigurationResolver._personaInfoProvider
+ _OBJC_IVAR_$_LSInstallInfo._bundleRecords
+ _OBJC_IVAR_$_LSInstallInfo._ersatz
+ _OBJC_IVAR_$_LSInstallInfo._overrides
+ _OBJC_IVAR_$_LSInstallInfo._personasWithAttributes
+ _OBJC_IVAR_$_LSInstallInfoOverrides._isDowngrade
+ _OBJC_IVAR_$_LSInstallInfoOverrides._isParallelPlaceholder
+ _OBJC_IVAR_$_LSInstallInfoOverrides._isPlaceholder
+ _OBJC_IVAR_$_LSInstallInfoOverrides._pluginHasOverride
+ _OBJC_IVAR_$_LSMIResultRegistrant._installInfo
+ _OBJC_IVAR_$_LSPreflightedCleanReferencesToPersonaOperation._affectedApps
+ _OBJC_IVAR_$_LSPreflightedCleanReferencesToPersonaOperation._affectedStandalonePlugins
+ _OBJC_IVAR_$_LSPreflightedCleanReferencesToPersonaOperation._personaUniqueString
+ _OBJC_IVAR_$_LSRebuildStatisticsGatherer._containerFixupScanTime
+ _OBJC_IVAR_$_LSRestrictionsTargetResolver._map
+ _OBJC_IVAR_$_LSStandalonePluginRecordUpdater._bundleDataContainerReleaseOperations
+ _OBJC_IVAR_$_LSStandalonePluginRecordUpdater._db
+ _OBJC_IVAR_$_LSStandalonePluginRecordUpdater._plistsToRelease
+ _OBJC_IVAR_$_LSStandalonePluginRecordUpdater._pluginData
+ _OBJC_IVAR_$_LSStandalonePluginRecordUpdater._pluginUnit
+ _OBJC_IVAR_$_LSTransmissibleExtensionLaunchConfiguration._additionalConfigurationDigest
+ _OBJC_IVAR_$_LSTransmissibleExtensionLaunchConfiguration._codedAdditionalConfiguration
+ _OBJC_IVAR_$_LSTransmissibleExtensionLaunchConfiguration._personaUniqueString
+ _OBJC_IVAR_$_LSUseValuesMCStateProvider._parentalControlsRestrictedBundles
+ _OBJC_IVAR_$_LSUseValuesMCStateProvider._partnerFinancingAllowlistedBundles
+ _OBJC_IVAR_$_LSWorkPipe._depth
+ _OBJC_IVAR_$_LSWorkPipe._invalidated
+ _OBJC_IVAR_$_LSWorkPipe._lock
+ _OBJC_IVAR_$_LSWorkPipe._pending
+ _OBJC_IVAR_$_LSWorkPipe._running
+ _OBJC_IVAR_$_LSWorkPipe._workQueue
+ _OBJC_IVAR_$__LSApplicationExtensionRecordEnumerator._restrictionReasonMask
+ _OBJC_IVAR_$__LSClaimBindingDocumentProxyBindable._bindingStyle
+ _OBJC_IVAR_$__LSLazyGroupContainerMap._lazyPlist
+ _OBJC_IVAR_$__LSMultiContainerMap._personaToContainerMap
+ _OBJC_IVAR_$__LSMultiGroupContainerMap._personaToGroupContainers
+ _OBJC_IVAR_$__LSOpenConfiguration._includeAppLinksForCallingApplication
+ _OBJC_IVAR_$__LSPersonaDatabase._cachedPersonaUniqueStringToPersonaWithAttributesMap
+ _OBJC_IVAR_$__LSPersonaDatabase._cachedPersonalPersona
+ _OBJC_IVAR_$__LSPersonaDatabase._cachedSystemPersona
+ _OBJC_IVAR_$__LSSingleContainerMap._containerURL
+ _OBJC_IVAR_$__LSSingleGroupContainerMap._groupContainers
+ _OBJC_METACLASS_$_LSBundleDataContainerMap
+ _OBJC_METACLASS_$_LSBundleGroupContainerMap
+ _OBJC_METACLASS_$_LSBundlePersonaAssociationResult
+ _OBJC_METACLASS_$_LSBundlePersonaRecordMap
+ _OBJC_METACLASS_$_LSBundleSetContainersOperation
+ _OBJC_METACLASS_$_LSBundleSetPersonaAssociationOperation
+ _OBJC_METACLASS_$_LSCleanReferencesToPersonaOperation
+ _OBJC_METACLASS_$_LSContainerCache
+ _OBJC_METACLASS_$_LSDExtensionLaunchConfigurationStore
+ _OBJC_METACLASS_$_LSDServerExtensionLaunchConfigurationRegistrar
+ _OBJC_METACLASS_$_LSExtensionLaunchConfiguration
+ _OBJC_METACLASS_$_LSExtensionLaunchConfigurationAppRecordWrapper
+ _OBJC_METACLASS_$_LSExtensionLaunchConfigurationClientSystemRegistrar
+ _OBJC_METACLASS_$_LSExtensionLaunchConfigurationExtensionRecordWrapper
+ _OBJC_METACLASS_$_LSExtensionLaunchConfigurationResolutionLSDBProvoder
+ _OBJC_METACLASS_$_LSExtensionLaunchConfigurationResolver
+ _OBJC_METACLASS_$_LSInstallInfo
+ _OBJC_METACLASS_$_LSInstallInfoOverrides
+ _OBJC_METACLASS_$_LSPreflightedCleanReferencesToPersonaOperation
+ _OBJC_METACLASS_$_LSRestrictionsTargetResolver
+ _OBJC_METACLASS_$_LSStandalonePluginRecordUpdater
+ _OBJC_METACLASS_$_LSTransmissibleExtensionLaunchConfiguration
+ _OBJC_METACLASS_$_LSWorkPipe
+ _OBJC_METACLASS_$__LSEmptyContainerMap
+ _OBJC_METACLASS_$__LSEmptyGroupContainerMap
+ _OBJC_METACLASS_$__LSLazyGroupContainerMap
+ _OBJC_METACLASS_$__LSMultiContainerMap
+ _OBJC_METACLASS_$__LSMultiGroupContainerMap
+ _OBJC_METACLASS_$__LSSingleContainerMap
+ _OBJC_METACLASS_$__LSSingleGroupContainerMap
+ __LSApplicationRestrictionsManagerGetSharedInstance
+ __LSApplicationRestrictionsManagerIsApplicationRestrictedCheckingBundleFlags
+ __LSAssertNotRunningInServer
+ __LSAudioUnitURLOpen
+ __LSBundleCopyPersonasWithAttributes
+ __LSCheckEntitlementForNSXPCConnectionQuiet
+ __LSContainerLog
+ __LSContainerLog.cold.1
+ __LSContainerLog.log
+ __LSContainerLog.onceToken
+ __LSCopyCacheableDataContainerMapForBundleWithIdentifier
+ __LSCopyCacheableDataContainerMapForBundleWithIdentifier.cold.1
+ __LSCopyContainerQueryPersonaForCurrentPersonaAndBundlePersonas
+ __LSCopyContainerQueryPersonaForCurrentPersonaAndBundlePersonas.cold.1
+ __LSCopyDataContainerURLFromContainermanagerForPersona
+ __LSCopyDataContainerURLFromContainermanagerForPersona.cold.1
+ __LSCopyEnvironmentVariablesFromDataContainerURL
+ __LSCopyGroupContainerIdentifiersXPCObjectFromEntitlements
+ __LSCopyGroupContainerIdentifiersXPCObjectFromEntitlements.cold.1
+ __LSCopyGroupContainerURLSFromContainermanagerForPersona
+ __LSCopyGroupContainerURLSFromContainermanagerForPersona.cold.1
+ __LSCreateRegistrationData.cold.1
+ __LSCreateRegistrationData.cold.2
+ __LSCreateRegistrationData.cold.3
+ __LSCreateRegistrationData.cold.4
+ __LSCriticalErrorLog
+ __LSCriticalErrorLog.cold.1
+ __LSCriticalErrorLog.log
+ __LSCriticalErrorLog.onceToken
+ __LSDatabaseCreateFromPersistentStore.cold.6
+ __LSDatabaseGetSeedingWorkloop
+ __LSDatabaseGetSeedingWorkloop.cold.1
+ __LSDatabaseMarkSeedingInFlight
+ __LSDatabaseNotifySeedingComplete
+ __LSDatabaseNotifySeedingComplete.cold.1
+ __LSDatabaseScheduleAfterSeeding
+ __LSDatabaseWaitForSeeding
+ __LSEntryPointLog
+ __LSEntryPointLog.cold.1
+ __LSEntryPointLog.log
+ __LSEntryPointLog.onceToken
+ __LSFindOrRegisterBundleNode.cold.2
+ __LSGetPersonalPersonaUniqueString
+ __LSGetPersonalPersonaUniqueString.cold.1
+ __LSMakeNSErrorFromContainerError
+ __LSMakeUseValuesStateProvider
+ __LSNSXPCConnectionMayMapDatabase_Cached
+ __LSPersistentIdentifierMakeForDatabase
+ __LSPersonaListHasSystemPersona
+ __LSPlistHintCopyRestoredKeys
+ __LSPostLSDistributedNotification
+ __LSPostLSDistributedNotification.cold.1
+ __LSPreferDataContainerURLFromDatabase
+ __LSPrimaryPersonaIdentifier
+ __LSServer_CleanSystemContentDatabaseForMainDatabaseUse
+ __LSShouldAbortPersonaRequest
+ __LSShouldAbortPersonaRequest.cold.1
+ __LSURLIsAudioUnitURL
+ __OBJC_$_CATEGORY_ICLAppExtensionRecord_$_LSExtensions
+ __OBJC_$_CATEGORY_ICLBundleRecord_$_LSExtensions
+ __OBJC_$_CATEGORY_ICLPlaceholderRecord_$_LSExtensions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_ICLAppExtensionRecord_$_LSExtensions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_ICLPlaceholderRecord_$_LSExtensions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSNull_$_NSNull_LSAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSObject_$_NSNull_LSAdditions
+ __OBJC_$_CATEGORY_NSNull_$_NSNull_LSAdditions
+ __OBJC_$_CATEGORY_NSObject_$_NSNull_LSAdditions
+ __OBJC_$_CLASS_METHODS_LSApplicationExtensionRecord(IconServices|Intents|Redaction|AppProtectionPrivate|AppInstallation|Restrictions|Utility|Enumeration)
+ __OBJC_$_CLASS_METHODS_LSApplicationWorkspace(DeprecatedEnumeration|DefaultApps|Marketplaces|URLQueries|DeprecatedURLQueries|OpenAdditions|LSURLOverride|PersonaNiceties)
+ __OBJC_$_CLASS_METHODS_LSBundleDataContainerMap
+ __OBJC_$_CLASS_METHODS_LSBundleGroupContainerMap
+ __OBJC_$_CLASS_METHODS_LSBundlePersonaRecordMap
+ __OBJC_$_CLASS_METHODS_LSDExtensionLaunchConfigurationStore
+ __OBJC_$_CLASS_METHODS_LSDServerExtensionLaunchConfigurationRegistrar
+ __OBJC_$_CLASS_METHODS_LSExtensionLaunchConfiguration
+ __OBJC_$_CLASS_METHODS_LSInstallInfo
+ __OBJC_$_CLASS_METHODS_LSInstallInfoOverrides
+ __OBJC_$_CLASS_METHODS_LSTransmissibleExtensionLaunchConfiguration
+ __OBJC_$_CLASS_METHODS__LSEmptyContainerMap
+ __OBJC_$_CLASS_METHODS__LSEmptyGroupContainerMap
+ __OBJC_$_CLASS_METHODS__LSLazyGroupContainerMap
+ __OBJC_$_CLASS_METHODS__LSMultiContainerMap
+ __OBJC_$_CLASS_METHODS__LSMultiGroupContainerMap
+ __OBJC_$_CLASS_METHODS__LSPersonaDatabase
+ __OBJC_$_CLASS_METHODS__LSPersonaWithAttributes(TestingAccess)
+ __OBJC_$_CLASS_METHODS__LSSingleContainerMap
+ __OBJC_$_CLASS_METHODS__LSSingleGroupContainerMap
+ __OBJC_$_CLASS_PROP_LIST_LSBundleDataContainerMap
+ __OBJC_$_CLASS_PROP_LIST_LSBundleGroupContainerMap
+ __OBJC_$_CLASS_PROP_LIST_LSBundlePersonaRecordMap
+ __OBJC_$_CLASS_PROP_LIST_LSInstallInfo
+ __OBJC_$_CLASS_PROP_LIST_LSInstallInfoOverrides
+ __OBJC_$_CLASS_PROP_LIST_LSTransmissibleExtensionLaunchConfiguration
+ __OBJC_$_INSTANCE_METHODS_ICLBundleRecord(LSExtensions|LSTransitional)
+ __OBJC_$_INSTANCE_METHODS_LSApplicationExtensionRecord(IconServices|Intents|Redaction|AppProtectionPrivate|AppInstallation|Restrictions|Utility|Enumeration)
+ __OBJC_$_INSTANCE_METHODS_LSApplicationWorkspace(DeprecatedEnumeration|DefaultApps|Marketplaces|URLQueries|DeprecatedURLQueries|OpenAdditions|LSURLOverride|PersonaNiceties)
+ __OBJC_$_INSTANCE_METHODS_LSBundleDataContainerMap
+ __OBJC_$_INSTANCE_METHODS_LSBundleGroupContainerMap
+ __OBJC_$_INSTANCE_METHODS_LSBundlePersonaAssociationResult
+ __OBJC_$_INSTANCE_METHODS_LSBundlePersonaRecordMap(Internal)
+ __OBJC_$_INSTANCE_METHODS_LSBundleSetContainersOperation
+ __OBJC_$_INSTANCE_METHODS_LSBundleSetPersonaAssociationOperation
+ __OBJC_$_INSTANCE_METHODS_LSCleanReferencesToPersonaOperation
+ __OBJC_$_INSTANCE_METHODS_LSContainerCache(Internal)
+ __OBJC_$_INSTANCE_METHODS_LSDExtensionLaunchConfigurationStore
+ __OBJC_$_INSTANCE_METHODS_LSDServerExtensionLaunchConfigurationRegistrar
+ __OBJC_$_INSTANCE_METHODS_LSExtensionLaunchConfiguration
+ __OBJC_$_INSTANCE_METHODS_LSExtensionLaunchConfigurationAppRecordWrapper
+ __OBJC_$_INSTANCE_METHODS_LSExtensionLaunchConfigurationClientSystemRegistrar
+ __OBJC_$_INSTANCE_METHODS_LSExtensionLaunchConfigurationExtensionRecordWrapper
+ __OBJC_$_INSTANCE_METHODS_LSExtensionLaunchConfigurationResolutionLSDBProvoder
+ __OBJC_$_INSTANCE_METHODS_LSExtensionLaunchConfigurationResolver
+ __OBJC_$_INSTANCE_METHODS_LSInstallInfo
+ __OBJC_$_INSTANCE_METHODS_LSInstallInfoOverrides
+ __OBJC_$_INSTANCE_METHODS_LSPreflightedCleanReferencesToPersonaOperation
+ __OBJC_$_INSTANCE_METHODS_LSRestrictionsTargetResolver
+ __OBJC_$_INSTANCE_METHODS_LSStandalonePluginRecordUpdater
+ __OBJC_$_INSTANCE_METHODS_LSTransmissibleExtensionLaunchConfiguration(CopyChangingPersona)
+ __OBJC_$_INSTANCE_METHODS_LSWorkPipe
+ __OBJC_$_INSTANCE_METHODS__LSEmptyContainerMap
+ __OBJC_$_INSTANCE_METHODS__LSEmptyGroupContainerMap
+ __OBJC_$_INSTANCE_METHODS__LSLazyGroupContainerMap
+ __OBJC_$_INSTANCE_METHODS__LSMultiContainerMap
+ __OBJC_$_INSTANCE_METHODS__LSMultiGroupContainerMap
+ __OBJC_$_INSTANCE_METHODS__LSPersonaWithAttributes(TestingAccess)
+ __OBJC_$_INSTANCE_METHODS__LSSingleContainerMap
+ __OBJC_$_INSTANCE_METHODS__LSSingleGroupContainerMap
+ __OBJC_$_INSTANCE_VARIABLES_LSBundleDataContainerMap
+ __OBJC_$_INSTANCE_VARIABLES_LSBundlePersonaAssociationResult
+ __OBJC_$_INSTANCE_VARIABLES_LSBundlePersonaRecordMap
+ __OBJC_$_INSTANCE_VARIABLES_LSBundleSetContainersOperation
+ __OBJC_$_INSTANCE_VARIABLES_LSBundleSetPersonaAssociationOperation
+ __OBJC_$_INSTANCE_VARIABLES_LSCleanReferencesToPersonaOperation
+ __OBJC_$_INSTANCE_VARIABLES_LSContainerCache
+ __OBJC_$_INSTANCE_VARIABLES_LSDExtensionLaunchConfigurationStore
+ __OBJC_$_INSTANCE_VARIABLES_LSDServerExtensionLaunchConfigurationRegistrar
+ __OBJC_$_INSTANCE_VARIABLES_LSExtensionLaunchConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_LSExtensionLaunchConfigurationAppRecordWrapper
+ __OBJC_$_INSTANCE_VARIABLES_LSExtensionLaunchConfigurationExtensionRecordWrapper
+ __OBJC_$_INSTANCE_VARIABLES_LSExtensionLaunchConfigurationResolver
+ __OBJC_$_INSTANCE_VARIABLES_LSInstallInfo
+ __OBJC_$_INSTANCE_VARIABLES_LSInstallInfoOverrides
+ __OBJC_$_INSTANCE_VARIABLES_LSPreflightedCleanReferencesToPersonaOperation
+ __OBJC_$_INSTANCE_VARIABLES_LSRestrictionsTargetResolver
+ __OBJC_$_INSTANCE_VARIABLES_LSStandalonePluginRecordUpdater
+ __OBJC_$_INSTANCE_VARIABLES_LSTransmissibleExtensionLaunchConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_LSWorkPipe
+ __OBJC_$_INSTANCE_VARIABLES__LSLazyGroupContainerMap
+ __OBJC_$_INSTANCE_VARIABLES__LSMultiContainerMap
+ __OBJC_$_INSTANCE_VARIABLES__LSMultiGroupContainerMap
+ __OBJC_$_INSTANCE_VARIABLES__LSSingleContainerMap
+ __OBJC_$_INSTANCE_VARIABLES__LSSingleGroupContainerMap
+ __OBJC_$_PROP_LIST_LSBundleDataContainerMap
+ __OBJC_$_PROP_LIST_LSBundlePersonaAssociationResult
+ __OBJC_$_PROP_LIST_LSDExtensionLaunchConfigurationStore
+ __OBJC_$_PROP_LIST_LSDServerExtensionLaunchConfigurationRegistrar
+ __OBJC_$_PROP_LIST_LSExtensionLaunchConfiguration
+ __OBJC_$_PROP_LIST_LSExtensionLaunchConfigurationAppRecordWrapper
+ __OBJC_$_PROP_LIST_LSExtensionLaunchConfigurationClientSystemRegistrar
+ __OBJC_$_PROP_LIST_LSExtensionLaunchConfigurationExtensionRecordWrapper
+ __OBJC_$_PROP_LIST_LSExtensionLaunchConfigurationResolutionLSDBProvoder
+ __OBJC_$_PROP_LIST_LSInstallInfo
+ __OBJC_$_PROP_LIST_LSInstallInfoOverrides
+ __OBJC_$_PROP_LIST_LSRestrictionsTargetResolver
+ __OBJC_$_PROP_LIST_LSTransmissibleExtensionLaunchConfiguration
+ __OBJC_$_PROP_LIST__LSPersonaDatabase
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LSDExtensionLaunchConfigurationStoring
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LSExtensionLaunchConfigurationRegistrar
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LSExtensionLaunchConfigurationResolutionApplicationExtensionRepresenting
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LSExtensionLaunchConfigurationResolutionApplicationRepresenting
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LSExtensionLaunchConfigurationResolutionBooleanEntitlementBearing
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LSExtensionLaunchConfigurationResolutionDatabaseProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LSPersonaInfoProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LSRestrictionsTargetResolving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LSDExtensionLaunchConfigurationStoring
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LSExtensionLaunchConfigurationRegistrar
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LSExtensionLaunchConfigurationResolutionApplicationExtensionRepresenting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LSExtensionLaunchConfigurationResolutionApplicationRepresenting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LSExtensionLaunchConfigurationResolutionBooleanEntitlementBearing
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LSExtensionLaunchConfigurationResolutionDatabaseProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LSPersonaInfoProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LSRestrictionsTargetResolving
+ __OBJC_$_PROTOCOL_REFS_LSDExtensionLaunchConfigurationStoring
+ __OBJC_$_PROTOCOL_REFS_LSExtensionLaunchConfigurationRegistrar
+ __OBJC_$_PROTOCOL_REFS_LSExtensionLaunchConfigurationResolutionApplicationExtensionRepresenting
+ __OBJC_$_PROTOCOL_REFS_LSExtensionLaunchConfigurationResolutionApplicationRepresenting
+ __OBJC_$_PROTOCOL_REFS_LSExtensionLaunchConfigurationResolutionBooleanEntitlementBearing
+ __OBJC_$_PROTOCOL_REFS_LSExtensionLaunchConfigurationResolutionDatabaseProviding
+ __OBJC_$_PROTOCOL_REFS_LSPersonaInfoProviding
+ __OBJC_$_PROTOCOL_REFS_LSRestrictionsTargetResolving
+ __OBJC_CLASS_PROTOCOLS_$_LSBundleDataContainerMap
+ __OBJC_CLASS_PROTOCOLS_$_LSBundleGroupContainerMap
+ __OBJC_CLASS_PROTOCOLS_$_LSBundlePersonaRecordMap
+ __OBJC_CLASS_PROTOCOLS_$_LSDExtensionLaunchConfigurationStore
+ __OBJC_CLASS_PROTOCOLS_$_LSExtensionLaunchConfigurationAppRecordWrapper
+ __OBJC_CLASS_PROTOCOLS_$_LSExtensionLaunchConfigurationClientSystemRegistrar
+ __OBJC_CLASS_PROTOCOLS_$_LSExtensionLaunchConfigurationExtensionRecordWrapper
+ __OBJC_CLASS_PROTOCOLS_$_LSExtensionLaunchConfigurationResolutionLSDBProvoder
+ __OBJC_CLASS_PROTOCOLS_$_LSInstallInfo
+ __OBJC_CLASS_PROTOCOLS_$_LSInstallInfoOverrides
+ __OBJC_CLASS_PROTOCOLS_$_LSRestrictionsTargetResolver
+ __OBJC_CLASS_PROTOCOLS_$_LSTransmissibleExtensionLaunchConfiguration
+ __OBJC_CLASS_PROTOCOLS_$__LSPersonaDatabase
+ __OBJC_CLASS_RO_$_LSBundleDataContainerMap
+ __OBJC_CLASS_RO_$_LSBundleGroupContainerMap
+ __OBJC_CLASS_RO_$_LSBundlePersonaAssociationResult
+ __OBJC_CLASS_RO_$_LSBundlePersonaRecordMap
+ __OBJC_CLASS_RO_$_LSBundleSetContainersOperation
+ __OBJC_CLASS_RO_$_LSBundleSetPersonaAssociationOperation
+ __OBJC_CLASS_RO_$_LSCleanReferencesToPersonaOperation
+ __OBJC_CLASS_RO_$_LSContainerCache
+ __OBJC_CLASS_RO_$_LSDExtensionLaunchConfigurationStore
+ __OBJC_CLASS_RO_$_LSDServerExtensionLaunchConfigurationRegistrar
+ __OBJC_CLASS_RO_$_LSExtensionLaunchConfiguration
+ __OBJC_CLASS_RO_$_LSExtensionLaunchConfigurationAppRecordWrapper
+ __OBJC_CLASS_RO_$_LSExtensionLaunchConfigurationClientSystemRegistrar
+ __OBJC_CLASS_RO_$_LSExtensionLaunchConfigurationExtensionRecordWrapper
+ __OBJC_CLASS_RO_$_LSExtensionLaunchConfigurationResolutionLSDBProvoder
+ __OBJC_CLASS_RO_$_LSExtensionLaunchConfigurationResolver
+ __OBJC_CLASS_RO_$_LSInstallInfo
+ __OBJC_CLASS_RO_$_LSInstallInfoOverrides
+ __OBJC_CLASS_RO_$_LSPreflightedCleanReferencesToPersonaOperation
+ __OBJC_CLASS_RO_$_LSRestrictionsTargetResolver
+ __OBJC_CLASS_RO_$_LSStandalonePluginRecordUpdater
+ __OBJC_CLASS_RO_$_LSTransmissibleExtensionLaunchConfiguration
+ __OBJC_CLASS_RO_$_LSWorkPipe
+ __OBJC_CLASS_RO_$__LSEmptyContainerMap
+ __OBJC_CLASS_RO_$__LSEmptyGroupContainerMap
+ __OBJC_CLASS_RO_$__LSLazyGroupContainerMap
+ __OBJC_CLASS_RO_$__LSMultiContainerMap
+ __OBJC_CLASS_RO_$__LSMultiGroupContainerMap
+ __OBJC_CLASS_RO_$__LSSingleContainerMap
+ __OBJC_CLASS_RO_$__LSSingleGroupContainerMap
+ __OBJC_LABEL_PROTOCOL_$_LSDExtensionLaunchConfigurationStoring
+ __OBJC_LABEL_PROTOCOL_$_LSExtensionLaunchConfigurationRegistrar
+ __OBJC_LABEL_PROTOCOL_$_LSExtensionLaunchConfigurationResolutionApplicationExtensionRepresenting
+ __OBJC_LABEL_PROTOCOL_$_LSExtensionLaunchConfigurationResolutionApplicationRepresenting
+ __OBJC_LABEL_PROTOCOL_$_LSExtensionLaunchConfigurationResolutionBooleanEntitlementBearing
+ __OBJC_LABEL_PROTOCOL_$_LSExtensionLaunchConfigurationResolutionDatabaseProviding
+ __OBJC_LABEL_PROTOCOL_$_LSPersonaInfoProviding
+ __OBJC_LABEL_PROTOCOL_$_LSRestrictionsTargetResolving
+ __OBJC_METACLASS_RO_$_LSBundleDataContainerMap
+ __OBJC_METACLASS_RO_$_LSBundleGroupContainerMap
+ __OBJC_METACLASS_RO_$_LSBundlePersonaAssociationResult
+ __OBJC_METACLASS_RO_$_LSBundlePersonaRecordMap
+ __OBJC_METACLASS_RO_$_LSBundleSetContainersOperation
+ __OBJC_METACLASS_RO_$_LSBundleSetPersonaAssociationOperation
+ __OBJC_METACLASS_RO_$_LSCleanReferencesToPersonaOperation
+ __OBJC_METACLASS_RO_$_LSContainerCache
+ __OBJC_METACLASS_RO_$_LSDExtensionLaunchConfigurationStore
+ __OBJC_METACLASS_RO_$_LSDServerExtensionLaunchConfigurationRegistrar
+ __OBJC_METACLASS_RO_$_LSExtensionLaunchConfiguration
+ __OBJC_METACLASS_RO_$_LSExtensionLaunchConfigurationAppRecordWrapper
+ __OBJC_METACLASS_RO_$_LSExtensionLaunchConfigurationClientSystemRegistrar
+ __OBJC_METACLASS_RO_$_LSExtensionLaunchConfigurationExtensionRecordWrapper
+ __OBJC_METACLASS_RO_$_LSExtensionLaunchConfigurationResolutionLSDBProvoder
+ __OBJC_METACLASS_RO_$_LSExtensionLaunchConfigurationResolver
+ __OBJC_METACLASS_RO_$_LSInstallInfo
+ __OBJC_METACLASS_RO_$_LSInstallInfoOverrides
+ __OBJC_METACLASS_RO_$_LSPreflightedCleanReferencesToPersonaOperation
+ __OBJC_METACLASS_RO_$_LSRestrictionsTargetResolver
+ __OBJC_METACLASS_RO_$_LSStandalonePluginRecordUpdater
+ __OBJC_METACLASS_RO_$_LSTransmissibleExtensionLaunchConfiguration
+ __OBJC_METACLASS_RO_$_LSWorkPipe
+ __OBJC_METACLASS_RO_$__LSEmptyContainerMap
+ __OBJC_METACLASS_RO_$__LSEmptyGroupContainerMap
+ __OBJC_METACLASS_RO_$__LSLazyGroupContainerMap
+ __OBJC_METACLASS_RO_$__LSMultiContainerMap
+ __OBJC_METACLASS_RO_$__LSMultiGroupContainerMap
+ __OBJC_METACLASS_RO_$__LSSingleContainerMap
+ __OBJC_METACLASS_RO_$__LSSingleGroupContainerMap
+ __OBJC_PROTOCOL_$_LSDExtensionLaunchConfigurationStoring
+ __OBJC_PROTOCOL_$_LSExtensionLaunchConfigurationRegistrar
+ __OBJC_PROTOCOL_$_LSExtensionLaunchConfigurationResolutionApplicationExtensionRepresenting
+ __OBJC_PROTOCOL_$_LSExtensionLaunchConfigurationResolutionApplicationRepresenting
+ __OBJC_PROTOCOL_$_LSExtensionLaunchConfigurationResolutionBooleanEntitlementBearing
+ __OBJC_PROTOCOL_$_LSExtensionLaunchConfigurationResolutionDatabaseProviding
+ __OBJC_PROTOCOL_$_LSPersonaInfoProviding
+ __OBJC_PROTOCOL_$_LSRestrictionsTargetResolving
+ __Z37_LSPluginParentRestrictionMatchesMaskP11_LSDatabasePK12LSPluginDatam
+ __Z69__LS_CANNOT_REALIZE_UTTYPE_DECLARING_BUNDLE_RECORD_FROM_APP_SANDBOX__P12UTTypeRecord
+ __ZL17_LSRegisterPluginP11_LSDatabaseP13LSInstallInfoRK12LSPluginInfoPK14__CFDictionaryPK10__CFStringSB_S8_jPj
+ __ZL17_LSRegisterPluginP11_LSDatabaseP13LSInstallInfoRK12LSPluginInfoPK14__CFDictionaryPK10__CFStringSB_S8_jPj.cold.1
+ __ZL17_LSRegisterPluginP11_LSDatabaseP13LSInstallInfoRK12LSPluginInfoPK14__CFDictionaryPK10__CFStringSB_S8_jPj.cold.2
+ __ZL17_LSRegisterPluginP11_LSDatabaseP13LSInstallInfoRK12LSPluginInfoPK14__CFDictionaryPK10__CFStringSB_S8_jPj.cold.3
+ __ZL21_LSRegisterBundleNodeP9LSContextjP6FSNodeS2_jP13LSInstallInfoPPK9__CFArrayPhPjPU15__autoreleasingP7NSError
+ __ZL21_seedingInFlightCount
+ __ZL23_LSDispatchRegistrationP9LSContextPKcPK18LSRegistrationInfoP6NSDataS7_PK7__CFURLP13LSInstallInfoPjPPK9__CFArrayPh
+ __ZL23pluginsUnitIDsForBundleP9LSContextPK12LSBundleData
+ __ZL24_LSRegisterDirectoryNodeP9LSContextP6FSNodeS2_PK18LSRegistrationInfoP6NSDataP13LSInstallInfoPPK9__CFArrayPhPj
+ __ZL32_LSGetCurrentPersonaUniqueStringv
+ __ZL35_LSSwizzleBundleIdentifierForLaunchPU15__autoreleasingP8NSStringPU15__autoreleasingP7NSError
+ __ZL35getAffectedBundleInfoForIdentifiersP9LSContextP12NSEnumeratorIP8NSStringEPU15__autoreleasingP7NSError
+ __ZL36_LSServerCreateBundleDataAndRegisterP9LSContextP18LSRegistrationInfoP6NSDataPK7__CFURLP13LSInstallInfoPjPPK9__CFArrayPh
+ __ZL37_LSOpenOperationCanOpenPrivateSchemesP15NSXPCConnectionP5NSURLP12NSDictionary
+ __ZL40initFBSDisplayLayoutMonitorConfigurationv
+ __ZL41_LSCreateRegistrationDataForDirectoryNodeP9LSContextP18LSRegistrationInfoPK7__CFURLP17_LSBundleProviderP6FSNodeP13LSInstallInfoPPK9__CFArray
+ __ZL41_LSCreateRegistrationDataForDirectoryNodeP9LSContextP18LSRegistrationInfoPK7__CFURLP17_LSBundleProviderP6FSNodeP13LSInstallInfoPPK9__CFArray.cold.1
+ __ZL41_LSCreateRegistrationDataForDirectoryNodeP9LSContextP18LSRegistrationInfoPK7__CFURLP17_LSBundleProviderP6FSNodeP13LSInstallInfoPPK9__CFArray.cold.2
+ __ZL41_LSCreateRegistrationDataForDirectoryNodeP9LSContextP18LSRegistrationInfoPK7__CFURLP17_LSBundleProviderP6FSNodeP13LSInstallInfoPPK9__CFArray.cold.3
+ __ZL41_LSCreateRegistrationDataForDirectoryNodeP9LSContextP18LSRegistrationInfoPK7__CFURLP17_LSBundleProviderP6FSNodeP13LSInstallInfoPPK9__CFArray.cold.4
+ __ZL41classFBSDisplayLayoutMonitorConfiguration
+ __ZL44FBSDisplayLayoutMonitorConfigurationFunctionv
+ __ZL44getFBSDisplayLayoutMonitorConfigurationClass
+ __ZL54sendPersonaChangedNotificationsForAppBundleIdentifiersP9LSContextP5NSSetIP8NSStringE
+ __ZN14LaunchServices10BaseBundle20DataContainerContext4Path6createEP11_LSDatabaseP8NSString
+ __ZN14LaunchServices10BaseBundle20DataContainerContext4Path7disposeEP11_LSDatabase
+ __ZN14LaunchServices10BaseBundle20DataContainerContext5Paths6createEP11_LSDatabaseP12NSDictionaryIP8NSStringP5NSURLE
+ __ZN14LaunchServices10BaseBundle20DataContainerContext5Paths7disposeEP11_LSDatabase
+ __ZN14LaunchServices10BaseBundle28DataContainerWritableContext13removePersonaEP11_LSDatabaseP8NSString
+ __ZN14LaunchServices10BaseBundle28DataContainerWritableContext23createAndAssignMultipleEP11_LSDatabaseP12NSDictionaryIP8NSStringP5NSURLEPU15__autoreleasingP7NSError
+ __ZN14LaunchServices10BaseBundle28DataContainerWritableContext23createAndAssignSingularEP11_LSDatabaseP5NSURLPU15__autoreleasingP7NSError
+ __ZN14LaunchServices10BaseBundle28DataContainerWritableContext23createAndAssignSingularEP11_LSDatabaseP8NSString
+ __ZN14LaunchServices10BaseBundle28DataContainerWritableContext28createAndAssignFromICLRecordEP11_LSDatabaseP15ICLBundleRecordPU15__autoreleasingP7NSError
+ __ZN14LaunchServices10BaseBundle28DataContainerWritableContext41createAndAssignFromBundlePersonaRecordMapEP11_LSDatabaseP12NSDictionaryIP8NSStringP22ICLBundlePersonaRecordEPU15__autoreleasingP7NSError
+ __ZN14LaunchServices10BaseBundle28DataContainerWritableContext7disposeEP11_LSDatabase
+ __ZN14LaunchServices10BaseBundle29GroupContainerWritableContext13removePersonaEP11_LSDatabaseP8NSString
+ __ZN14LaunchServices10BaseBundle29GroupContainerWritableContext27pathifyGroupContainerURLMapEP12NSDictionaryIP8NSStringP5NSURLE
+ __ZN14LaunchServices10BaseBundle29GroupContainerWritableContext28createAndAssignFromICLRecordEP11_LSDatabaseP15ICLBundleRecordPU15__autoreleasingP7NSError
+ __ZN14LaunchServices10BaseBundle29GroupContainerWritableContext32createAndAssignFromRawDictionaryEP11_LSDatabaseP12NSDictionaryIP8NSStringPS4_IS6_S6_EE
+ __ZN14LaunchServices10BaseBundle29GroupContainerWritableContext41createAndAssignFromBundlePersonaRecordMapEP11_LSDatabaseP12NSDictionaryIP8NSStringP22ICLBundlePersonaRecordEPU15__autoreleasingP7NSError
+ __ZN14LaunchServices10BaseBundle31_LSCleanDataContainerForPersonaEP11_LSDatabaseP16LSBundleBaseDataP8NSStringRNSt3__16vectorINS0_35BundleDataContainerReleaseOperationENS7_9allocatorIS9_EEEE
+ __ZN14LaunchServices10BaseBundle31_LSCleanDataContainerForPersonaEP11_LSDatabaseP16LSBundleBaseDataP8NSStringRNSt3__16vectorINS0_35BundleDataContainerReleaseOperationENS7_9allocatorIS9_EEEE.cold.1
+ __ZN14LaunchServices10BaseBundle32_LSUpdateDataContainersForBundleEP11_LSDatabaseP16LSBundleBaseDataP24LSBundlePersonaRecordMapRNSt3__16vectorINS0_35BundleDataContainerReleaseOperationENS7_9allocatorIS9_EEEERNS8_IjNSA_IjEEEE
+ __ZN14LaunchServices10BaseBundle32_LSUpdateDataContainersForBundleEP11_LSDatabaseP16LSBundleBaseDataP24LSBundlePersonaRecordMapRNSt3__16vectorINS0_35BundleDataContainerReleaseOperationENS7_9allocatorIS9_EEEERNS8_IjNSA_IjEEEE.cold.1
+ __ZN14LaunchServices10BaseBundle33_LSCleanGroupContainersForPersonaEP11_LSDatabaseP16LSBundleBaseDataP8NSStringRNSt3__16vectorIjNS7_9allocatorIjEEEE
+ __ZN14LaunchServices10BaseBundle33_LSCleanGroupContainersForPersonaEP11_LSDatabaseP16LSBundleBaseDataP8NSStringRNSt3__16vectorIjNS7_9allocatorIjEEEE.cold.1
+ __ZN14LaunchServices10BaseBundle35BundleDataContainerReleaseOperationclEP11_LSDatabase
+ __ZN14LaunchServices14ContainerCacheL17indexContainerMapERNSt3__113unordered_mapINS0_18PersonaAndPlatformEU8__strongP19NSMutableDictionaryIP8NSStringP5NSURLENS0_22PersonaAndPlatformHashENS1_8equal_toIS3_EENS1_9allocatorINS1_4pairIKS3_SB_EEEEEERSH_
+ __ZN14LaunchServices19URLPropertyProviderL38prepareBinaryCompatibilityWarningValueERNS_8Database7ContextEPU34objcproto23FSNodePropertyProviding11objc_objectP11__FileCachePK10__CFStringPNS0_5StateEPU15__autoreleasingP7NSError
+ __ZN14LaunchServices19URLPropertyProviderL38prepareBinaryCompatibilityWarningValueERNS_8Database7ContextEPU34objcproto23FSNodePropertyProviding11objc_objectP11__FileCachePK10__CFStringPNS0_5StateEPU15__autoreleasingP7NSError.cold.1
+ __ZN14LaunchServices23SetStrongBindingForNodeERNS_8Database7ContextEP6FSNodejS4_PU15__autoreleasingP7NSError.cold.1
+ __ZN14LaunchServices23SetStrongBindingForNodeERNS_8Database7ContextEP6FSNodejS4_PU15__autoreleasingP7NSError.cold.2
+ __ZN14LaunchServices3$_88__invokeEv
+ __ZN14LaunchServices6RecordL29cachedDataContainerURLMapLockE
+ __ZN26CachedRepresentedBundleMap10getUpdatedEP9LSContext
+ __ZN26CachedRepresentedBundleMap14mapFromContextEP9LSContext
+ __ZN26CachedRepresentedBundleMap7currentEP9LSContext
+ __ZN26CachedRepresentedBundleMapC2EP9LSContext
+ __ZNK10LSDBHeader12getModelCodeEv
+ __ZNK10LSDBHeader15getBuildVersionEv
+ __ZNK10LSDBHeader17getCryptexVersionEv
+ __ZNK14LaunchServices10BaseBundle20DataContainerContext5Paths17enumerateResolvedIU8__strongU13block_pointerFvP8NSStringS5_PhEEEvP11_LSDatabaseRKT_
+ __ZNK14LaunchServices10BaseBundle20DataContainerContext5Paths17enumerateResolvedIZNS0_28DataContainerWritableContext13removePersonaEP11_LSDatabaseP8NSStringEUlS8_S8_PhE_EEvS6_RKT_
+ __ZNK14LaunchServices13objc_equal_toIU8__strongP8NSStringS3_EclES2_S2_
+ __ZNKSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore removeEntriesForBundleIdentifier:]E3$_2FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EE7__cloneEPNS0_6__baseIS5_EE
+ __ZNKSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore removeEntriesForBundleIdentifier:]E3$_2FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore setEntry:forApplication:category:]E3$_1FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EE7__cloneEPNS0_6__baseIS5_EE
+ __ZNKSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore setEntry:forApplication:category:]E3$_1FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EE7__cloneEv
+ __ZNKSt3__111__copy_implclB9fqn220100IPKN14LaunchServices17BindingEvaluation15ExtendedBindingES6_PS4_Li0EEENS_4pairIT_T1_EES9_T0_SA_
+ __ZNKSt3__111__copy_implclB9fqn220100IPKjS3_NS_20back_insert_iteratorINS_6vectorIjNS_9allocatorIjEEEEEELi0EEENS_4pairIT_T1_EESB_T0_SC_
+ __ZNKSt3__111__copy_implclB9fqn220100IPN14LaunchServices17BindingEvaluation15ExtendedBindingES5_S5_Li0EEENS_4pairIT_T1_EES7_T0_S8_
+ __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB9fqn220100IPN14LaunchServices17BindingEvaluation15ExtendedBindingES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
+ __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB9fqn220100IPU6__weakP8LSRecordS7_S7_EENS_4pairIT_T1_EES9_T0_SA_
+ __ZNKSt3__112__hash_tableINS_17__hash_value_typeIj38_LSDatabaseTableVisualizationFunctionsEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS7_SB_S9_EENS_9allocatorIS7_EEE4findIjEENS_21__hash_const_iteratorIPNS_11__hash_nodeIS3_PvEEEERKT_
+ __ZNKSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_mapIjbNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjbEEEEEEEENS_22__unordered_map_hasherIjNS8_IS9_SC_EES4_S6_EENS_21__unordered_map_equalIjSF_S6_S4_EENS7_ISF_EEE4findIjEENS_21__hash_const_iteratorIPNS_11__hash_nodeISD_PvEEEERKT_
+ __ZNKSt3__112__hash_tableINS_17__hash_value_typeIjbEENS_22__unordered_map_hasherIjNS_4pairIKjbEENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS6_SA_S8_EENS_9allocatorIS6_EEE4findIjEENS_21__hash_const_iteratorIPNS_11__hash_nodeIS2_PvEEEERKT_
+ __ZNKSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjNS_4pairIKjjEENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS6_SA_S8_EENS_9allocatorIS6_EEE4findIjEENS_21__hash_const_iteratorIPNS_11__hash_nodeIS2_PvEEEERKT_
+ __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE4viewB9fqn220100Ev
+ __ZNKSt3__116__variant_detail12__visitation9__variant15__value_visitorIZN14LaunchServices20AppRecordEnumeration32VolumeContainerResolutionAdapter7resolveEP9LSContextEUlRKT_E_EclB9fqn220100IJRNS0_5__altILm1EU8__strongP5NSURLEEEEEDcDpOT_
+ __ZNKSt3__116__variant_detail12__visitation9__variant15__value_visitorIZN14LaunchServices20AppRecordEnumeration32VolumeContainerResolutionAdapter7resolveEP9LSContextEUlRKT_E_EclB9fqn220100IJRNS0_5__altILm2EU8__strongP7NSErrorEEEEEDcDpOT_
+ __ZNKSt3__120__move_backward_implINS_17_ClassicAlgPolicyEEclB9fqn220100IP9LSBindingS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
+ __ZNKSt3__120__move_backward_implINS_17_ClassicAlgPolicyEEclB9fqn220100IPN14LaunchServices17BindingEvaluation15ExtendedBindingES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
+ __ZNKSt3__120__move_backward_implINS_17_ClassicAlgPolicyEEclB9fqn220100IPU6__weakP8LSRecordS7_S7_EENS_4pairIT_T1_EES9_T0_SA_
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9fqn220100EPKvm
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB9fqn220100ERKS6_S9_
+ __ZNSt3__110__function12__value_funcIFN14LaunchServices23LSDefaultAppsExtraStateENS_8optionalIS3_EEP7NSErrorEED2B9fqn220100Ev
+ __ZNSt3__110__function12__value_funcIFP11objc_objectS3_P7NSErrorEED2B9fqn220100Ev
+ __ZNSt3__110__function12__value_funcIFbP11objc_objectEEC2B9fqn220100EOS5_
+ __ZNSt3__110__function12__value_funcIFbP11objc_objectEED2B9fqn220100Ev
+ __ZNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore removeEntriesForBundleIdentifier:]E3$_2FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore removeEntriesForBundleIdentifier:]E3$_2FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EE7destroyEv
+ __ZNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore removeEntriesForBundleIdentifier:]E3$_2FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EED0Ev
+ __ZNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore removeEntriesForBundleIdentifier:]E3$_2FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EED1Ev
+ __ZNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore removeEntriesForBundleIdentifier:]E3$_2FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EEclEOS4_
+ __ZNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore setEntry:forApplication:category:]E3$_1FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore setEntry:forApplication:category:]E3$_1FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EE7destroyEv
+ __ZNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore setEntry:forApplication:category:]E3$_1FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EED0Ev
+ __ZNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore setEntry:forApplication:category:]E3$_1FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EED1Ev
+ __ZNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore setEntry:forApplication:category:]E3$_1FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EEclEOS4_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEEPvEENS_22__hash_node_destructorINS_9allocatorISA_EEEEED1B9fqn220100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIPKvU8__strongP5NSSetIP10objc_classEEEPvEENS_22__hash_node_destructorINS_9allocatorISD_EEEEED1B9fqn220100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS_13unordered_mapIjbNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjbEEEEEEEEPvEENS_22__hash_node_destructorINS8_ISG_EEEEED1B9fqn220100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEEPvEENS_22__hash_node_destructorINS8_ISD_EEEEED1B9fqn220100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjU8__strongP19LSApplicationRecordEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEED1B9fqn220100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjU8__strongP8NSStringEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEED1B9fqn220100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyN14LaunchServices11OpenStaging20StagingDirectoryInfoEEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEED1B9fqn220100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeIjPvEENS_22__hash_node_destructorIN14LaunchServices19MallocZoneAllocatorIS3_NS5_17BindingEvaluation17BindingMallocZoneEEEEEE5resetB9fqn220100EPS3_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeI23os_eligibility_domain_tN14LaunchServices7notifyd11NotifyTokenEEEPvEENS_22__tree_node_destructorINS_9allocatorIS9_EEEEED1B9fqn220100Ev
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIjU8__strongP8NSStringEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEED1B9fqn220100Ev
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeImU8__strongU13block_pointerFvvEEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEED1B9fqn220100Ev
+ __ZNSt3__111__find_loopB9fqn220100IPU6__weakP8LSRecordS4_DnNS_10__identityEEET_S6_T0_RKT1_RT2_
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZ69+[_LSDReadClient methodWithSelectorGetsImplicitExecutionContextRead:]E3$_1PP13objc_selectorLb0EEEvT1_S7_T0_NS_15iterator_traitsIS7_E15difference_typeEb
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZ87+[LSApplicationRecord(UserActivity) applicationRecordsForUserActivityType:limit:error:]E3$_1PNS_4pairIjPK12LSBundleDataEELb0EEEvT1_SA_T0_NS_15iterator_traitsISA_E15difference_typeEb
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]E3$_2PjLb0EEEvT1_S5_T0_NS_15iterator_traitsIS5_E15difference_typeEb
+ __ZNSt3__111__sift_downB9fqn220100INS_17_ClassicAlgPolicyELb0ERZN14LaunchServices17BindingEvaluationL4sortERNS3_5StateEE3$_0NS_11__wrap_iterIPNS3_15ExtendedBindingEEEEEvT2_OT1_NS_15iterator_traitsISC_E15difference_typeESH_
+ __ZNSt3__112__destroy_atB9fqn220100IN14LaunchServices30FeatureFlagPredicateEvaluation20FeatureFlagSpecifierEEEvPT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI12LSSessionKey31LSQuickSessionAvailabilityStateEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S3_EE18LSSessionKeyHasher22LSSessionKeyComparatorEENS_21__unordered_map_equalIS2_S8_SA_S9_EENS_9allocatorIS8_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI12LSSessionKey31LSQuickSessionAvailabilityStateEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S3_EE18LSSessionKeyHasher22LSSessionKeyComparatorEENS_21__unordered_map_equalIS2_S8_SA_S9_EENS_9allocatorIS8_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI12LSSessionKeyP9LSSessionEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S4_EE18LSSessionKeyHasher22LSSessionKeyComparatorEENS_21__unordered_map_equalIS2_S9_SB_SA_EENS_9allocatorIS9_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI12LSSessionKeyP9LSSessionEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S4_EE18LSSessionKeyHasher22LSSessionKeyComparatorEENS_21__unordered_map_equalIS2_S9_SB_SA_EENS_9allocatorIS9_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN14LaunchServices14ContainerCache18PersonaAndPlatformENS_6vectorIU8__strongP8NSStringNS_9allocatorIS8_EEEEEENS_22__unordered_map_hasherIS4_NS_4pairIKS4_SB_EENS3_22PersonaAndPlatformHashENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_SG_SJ_SH_EENS9_ISG_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN14LaunchServices14ContainerCache18PersonaAndPlatformENS_6vectorIU8__strongP8NSStringNS_9allocatorIS8_EEEEEENS_22__unordered_map_hasherIS4_NS_4pairIKS4_SB_EENS3_22PersonaAndPlatformHashENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_SG_SJ_SH_EENS9_ISG_EEE16__copy_constructB9fqn220100EPNS_16__hash_node_baseIPNS_11__hash_nodeISC_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN14LaunchServices14ContainerCache18PersonaAndPlatformENS_6vectorIU8__strongP8NSStringNS_9allocatorIS8_EEEEEENS_22__unordered_map_hasherIS4_NS_4pairIKS4_SB_EENS3_22PersonaAndPlatformHashENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_SG_SJ_SH_EENS9_ISG_EEE16__copy_constructB9fqn220100EPNS_16__hash_node_baseIPNS_11__hash_nodeISC_PvEEEESV_m
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN14LaunchServices14ContainerCache18PersonaAndPlatformENS_6vectorIU8__strongP8NSStringNS_9allocatorIS8_EEEEEENS_22__unordered_map_hasherIS4_NS_4pairIKS4_SB_EENS3_22PersonaAndPlatformHashENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_SG_SJ_SH_EENS9_ISG_EEE17__deallocate_nodeB9fqn220100EPNS_11__hash_nodeISC_PvEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN14LaunchServices14ContainerCache18PersonaAndPlatformENS_6vectorIU8__strongP8NSStringNS_9allocatorIS8_EEEEEENS_22__unordered_map_hasherIS4_NS_4pairIKS4_SB_EENS3_22PersonaAndPlatformHashENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_SG_SJ_SH_EENS9_ISG_EEE21__construct_node_hashIJRSG_EEENS_10unique_ptrINS_11__hash_nodeISC_PvEENS_22__hash_node_destructorINS9_ISU_EEEEEEmDpOT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN14LaunchServices14ContainerCache18PersonaAndPlatformENS_6vectorIU8__strongP8NSStringNS_9allocatorIS8_EEEEEENS_22__unordered_map_hasherIS4_NS_4pairIKS4_SB_EENS3_22PersonaAndPlatformHashENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_SG_SJ_SH_EENS9_ISG_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN14LaunchServices14ContainerCache18PersonaAndPlatformENS_6vectorIU8__strongP8NSStringNS_9allocatorIS8_EEEEEENS_22__unordered_map_hasherIS4_NS_4pairIKS4_SB_EENS3_22PersonaAndPlatformHashENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_SG_SJ_SH_EENS9_ISG_EEEC2EOSO_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN14LaunchServices14ContainerCache18PersonaAndPlatformENS_6vectorIU8__strongP8NSStringNS_9allocatorIS8_EEEEEENS_22__unordered_map_hasherIS4_NS_4pairIKS4_SB_EENS3_22PersonaAndPlatformHashENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_SG_SJ_SH_EENS9_ISG_EEEC2ERKSO_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN14LaunchServices14ContainerCache18PersonaAndPlatformENS_6vectorIU8__strongP8NSStringNS_9allocatorIS8_EEEEEENS_22__unordered_map_hasherIS4_NS_4pairIKS4_SB_EENS3_22PersonaAndPlatformHashENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_SG_SJ_SH_EENS9_ISG_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN14LaunchServices14ContainerCache18PersonaAndPlatformEU8__strongP19NSMutableDictionaryIP8NSStringP5NSURLEEENS_22__unordered_map_hasherIS4_NS_4pairIKS4_SC_EENS3_22PersonaAndPlatformHashENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_SH_SK_SI_EENS_9allocatorISH_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN14LaunchServices14ContainerCache18PersonaAndPlatformEU8__strongP19NSMutableDictionaryIP8NSStringP5NSURLEEENS_22__unordered_map_hasherIS4_NS_4pairIKS4_SC_EENS3_22PersonaAndPlatformHashENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_SH_SK_SI_EENS_9allocatorISH_EEE17__deallocate_nodeB9fqn220100EPNS_11__hash_nodeISD_PvEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN14LaunchServices14ContainerCache18PersonaAndPlatformEU8__strongP19NSMutableDictionaryIP8NSStringP5NSURLEEENS_22__unordered_map_hasherIS4_NS_4pairIKS4_SC_EENS3_22PersonaAndPlatformHashENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_SH_SK_SI_EENS_9allocatorISH_EEE4findIS4_EENS_15__hash_iteratorIPNS_11__hash_nodeISD_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN14LaunchServices14ContainerCache18PersonaAndPlatformEU8__strongP19NSMutableDictionaryIP8NSStringP5NSURLEEENS_22__unordered_map_hasherIS4_NS_4pairIKS4_SC_EENS3_22PersonaAndPlatformHashENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_SH_SK_SI_EENS_9allocatorISH_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN14LaunchServices14ContainerCache18PersonaAndPlatformEU8__strongP19NSMutableDictionaryIP8NSStringP5NSURLEEENS_22__unordered_map_hasherIS4_NS_4pairIKS4_SC_EENS3_22PersonaAndPlatformHashENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_SH_SK_SI_EENS_9allocatorISH_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selector18FSSelectorCategoryEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S4_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_S9_SD_SB_EENS_9allocatorIS9_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selector18FSSelectorCategoryEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S4_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_S9_SD_SB_EENS_9allocatorIS9_EEE4findIS3_EENS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selector18FSSelectorCategoryEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S4_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_S9_SD_SB_EENS_9allocatorIS9_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SB_SF_SD_EENS_9allocatorISB_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SB_SF_SD_EENS_9allocatorISB_EEE14__erase_uniqueIS3_EEmRKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SB_SF_SD_EENS_9allocatorISB_EEE16__copy_constructB9fqn220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS7_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SB_SF_SD_EENS_9allocatorISB_EEE16__copy_constructB9fqn220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS7_PvEEEESS_m
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SB_SF_SD_EENS_9allocatorISB_EEE22__deallocate_node_listB9fqn220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS7_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SB_SF_SD_EENS_9allocatorISB_EEE4findIS3_EENS_15__hash_iteratorIPNS_11__hash_nodeIS7_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SB_SF_SD_EENS_9allocatorISB_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS7_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SB_SF_SD_EENS_9allocatorISB_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS7_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SB_SF_SD_EENS_9allocatorISB_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SB_SF_SD_EENS_9allocatorISB_EEEC2ERKSL_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SB_SF_SD_EENS_9allocatorISB_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIP17_opaque_pthread_tNS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SC_SG_SE_EENS_9allocatorISC_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIP17_opaque_pthread_tNS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SC_SG_SE_EENS_9allocatorISC_EEE14__erase_uniqueIS3_EEmRKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIP17_opaque_pthread_tNS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SC_SG_SE_EENS_9allocatorISC_EEE4findIS3_EENS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIP17_opaque_pthread_tNS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SC_SG_SE_EENS_9allocatorISC_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS8_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIP17_opaque_pthread_tNS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SC_SG_SE_EENS_9allocatorISC_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS8_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIP17_opaque_pthread_tNS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SC_SG_SE_EENS_9allocatorISC_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIP17_opaque_pthread_tNS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SC_SG_SE_EENS_9allocatorISC_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvNS_6vectorINS_4pairIP13objc_selectorPFvP11objc_objectS7_EEENS_9allocatorISC_EEEEEENS_22__unordered_map_hasherIS3_NS5_IKS3_SF_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SJ_SN_SL_EENSD_ISJ_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvNS_6vectorINS_4pairIP13objc_selectorPFvP11objc_objectS7_EEENS_9allocatorISC_EEEEEENS_22__unordered_map_hasherIS3_NS5_IKS3_SF_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SJ_SN_SL_EENSD_ISJ_EEE4findIS3_EENS_15__hash_iteratorIPNS_11__hash_nodeISG_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvNS_6vectorINS_4pairIP13objc_selectorPFvP11objc_objectS7_EEENS_9allocatorISC_EEEEEENS_22__unordered_map_hasherIS3_NS5_IKS3_SF_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SJ_SN_SL_EENSD_ISJ_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvU8__strongP5NSSetIP10objc_classEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S9_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SE_SI_SG_EENS_9allocatorISE_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvU8__strongP5NSSetIP10objc_classEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S9_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SE_SI_SG_EENS_9allocatorISE_EEE4findIS3_EENS_15__hash_iteratorIPNS_11__hash_nodeISA_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvU8__strongP5NSSetIP10objc_classEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S9_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SE_SI_SG_EENS_9allocatorISE_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj12LSPluginDataEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS7_SB_S9_EENS_9allocatorIS7_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj12LSPluginDataEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS7_SB_S9_EENS_9allocatorIS7_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj12LSPluginDataEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS7_SB_S9_EENS_9allocatorIS7_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj12LSPluginDataEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS7_SB_S9_EENS_9allocatorIS7_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj37LSApplicationRecordUpdateAvailabilityEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS7_SB_S9_EENS_9allocatorIS7_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj37LSApplicationRecordUpdateAvailabilityEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS7_SB_S9_EENS_9allocatorIS7_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj37LSApplicationRecordUpdateAvailabilityEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS7_SB_S9_EENS_9allocatorIS7_EEEC2EOSH_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj37LSApplicationRecordUpdateAvailabilityEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS7_SB_S9_EENS_9allocatorIS7_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj38_LSDatabaseTableVisualizationFunctionsEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS7_SB_S9_EENS_9allocatorIS7_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj38_LSDatabaseTableVisualizationFunctionsEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS7_SB_S9_EENS_9allocatorIS7_EEE16__copy_constructB9fqn220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS3_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj38_LSDatabaseTableVisualizationFunctionsEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS7_SB_S9_EENS_9allocatorIS7_EEE16__copy_constructB9fqn220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS3_PvEEEESO_m
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj38_LSDatabaseTableVisualizationFunctionsEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS7_SB_S9_EENS_9allocatorIS7_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj38_LSDatabaseTableVisualizationFunctionsEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS7_SB_S9_EENS_9allocatorIS7_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj38_LSDatabaseTableVisualizationFunctionsEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS7_SB_S9_EENS_9allocatorIS7_EEEC2ERKSH_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj38_LSDatabaseTableVisualizationFunctionsEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS7_SB_S9_EENS_9allocatorIS7_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_mapIjbNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjbEEEEEEEENS_22__unordered_map_hasherIjNS8_IS9_SC_EES4_S6_EENS_21__unordered_map_equalIjSF_S6_S4_EENS7_ISF_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_mapIjbNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjbEEEEEEEENS_22__unordered_map_hasherIjNS8_IS9_SC_EES4_S6_EENS_21__unordered_map_equalIjSF_S6_S4_EENS7_ISF_EEE13__move_assignERSK_NS_17integral_constantIbLb1EEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_mapIjbNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjbEEEEEEEENS_22__unordered_map_hasherIjNS8_IS9_SC_EES4_S6_EENS_21__unordered_map_equalIjSF_S6_S4_EENS7_ISF_EEE22__deallocate_node_listB9fqn220100EPNS_16__hash_node_baseIPNS_11__hash_nodeISD_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_mapIjbNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjbEEEEEEEENS_22__unordered_map_hasherIjNS8_IS9_SC_EES4_S6_EENS_21__unordered_map_equalIjSF_S6_S4_EENS7_ISF_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_mapIjbNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjbEEEEEEEENS_22__unordered_map_hasherIjNS8_IS9_SC_EES4_S6_EENS_21__unordered_map_equalIjSF_S6_S4_EENS7_ISF_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_mapIjbNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjbEEEEEEEENS_22__unordered_map_hasherIjNS8_IS9_SC_EES4_S6_EENS_21__unordered_map_equalIjSF_S6_S4_EENS7_ISF_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEENS_22__unordered_map_hasherIjNS_4pairIKjS9_EES4_S6_EENS_21__unordered_map_equalIjSE_S6_S4_EENS7_ISE_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEENS_22__unordered_map_hasherIjNS_4pairIKjS9_EES4_S6_EENS_21__unordered_map_equalIjSE_S6_S4_EENS7_ISE_EEE22__deallocate_node_listB9fqn220100EPNS_16__hash_node_baseIPNS_11__hash_nodeISA_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEENS_22__unordered_map_hasherIjNS_4pairIKjS9_EES4_S6_EENS_21__unordered_map_equalIjSE_S6_S4_EENS7_ISE_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeISA_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEENS_22__unordered_map_hasherIjNS_4pairIKjS9_EES4_S6_EENS_21__unordered_map_equalIjSE_S6_S4_EENS7_ISE_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEENS_22__unordered_map_hasherIjNS_4pairIKjS9_EES4_S6_EENS_21__unordered_map_equalIjSE_S6_S4_EENS7_ISE_EEEC2EOSJ_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEENS_22__unordered_map_hasherIjNS_4pairIKjS9_EES4_S6_EENS_21__unordered_map_equalIjSE_S6_S4_EENS7_ISE_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP19LSApplicationRecordEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS9_SD_SB_EENS_9allocatorIS9_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP19LSApplicationRecordEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS9_SD_SB_EENS_9allocatorIS9_EEE22__deallocate_node_listB9fqn220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS5_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP19LSApplicationRecordEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS9_SD_SB_EENS_9allocatorIS9_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP19LSApplicationRecordEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS9_SD_SB_EENS_9allocatorIS9_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP19LSApplicationRecordEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS9_SD_SB_EENS_9allocatorIS9_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP8NSStringEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS9_SD_SB_EENS_9allocatorIS9_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP8NSStringEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS9_SD_SB_EENS_9allocatorIS9_EEE22__deallocate_node_listB9fqn220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS5_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP8NSStringEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS9_SD_SB_EENS_9allocatorIS9_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP8NSStringEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS9_SD_SB_EENS_9allocatorIS9_EEEC2EOSJ_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP8NSStringEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS9_SD_SB_EENS_9allocatorIS9_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjbEENS_22__unordered_map_hasherIjNS_4pairIKjbEENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS6_SA_S8_EENS_9allocatorIS6_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjbEENS_22__unordered_map_hasherIjNS_4pairIKjbEENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS6_SA_S8_EENS_9allocatorIS6_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjbEENS_22__unordered_map_hasherIjNS_4pairIKjbEENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS6_SA_S8_EENS_9allocatorIS6_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjNS_4pairIKjjEENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS6_SA_S8_EENS_9allocatorIS6_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjNS_4pairIKjjEENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS6_SA_S8_EENS_9allocatorIS6_EEE13__move_assignERSG_NS_17integral_constantIbLb1EEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjNS_4pairIKjjEENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS6_SA_S8_EENS_9allocatorIS6_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjNS_4pairIKjjEENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS6_SA_S8_EENS_9allocatorIS6_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjNS_4pairIKjjEENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS6_SA_S8_EENS_9allocatorIS6_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN14LaunchServices11OpenStaging20StagingDirectoryInfoEEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS9_SD_SB_EENS_9allocatorIS9_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN14LaunchServices11OpenStaging20StagingDirectoryInfoEEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS9_SD_SB_EENS_9allocatorIS9_EEE22__deallocate_node_listB9fqn220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS5_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN14LaunchServices11OpenStaging20StagingDirectoryInfoEEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS9_SD_SB_EENS_9allocatorIS9_EEE4findIyEENS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN14LaunchServices11OpenStaging20StagingDirectoryInfoEEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS9_SD_SB_EENS_9allocatorIS9_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS5_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN14LaunchServices11OpenStaging20StagingDirectoryInfoEEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS9_SD_SB_EENS_9allocatorIS9_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS5_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN14LaunchServices11OpenStaging20StagingDirectoryInfoEEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS9_SD_SB_EENS_9allocatorIS9_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN14LaunchServices11OpenStaging20StagingDirectoryInfoEEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS9_SD_SB_EENS_9allocatorIS9_EEED2Ev
+ __ZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEEN14LaunchServices19MallocZoneAllocatorIjNS5_17BindingEvaluation17BindingMallocZoneEEEE22__deallocate_node_listB9fqn220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIjPvEEEE
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE22__init_internal_bufferB9fqn220100Em
+ __ZNSt3__113__tree_removeB9fqn220100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__113unordered_mapIPK20LSExtensionPointDatajZ27_LSEnumerateExtensionPointsE30_LSExtensionPointCxxComparatorS4_NS_9allocatorINS_4pairIKS3_jEEEEED1B9fqn220100Ev
+ __ZNSt3__113unordered_mapIyN14LaunchServices11OpenStaging20StagingDirectoryInfoENS_4hashIyEENS_8equal_toIyEENS_9allocatorINS_4pairIKyS3_EEEEE16insert_or_assignB9fqn220100IS3_EENS9_INS_19__hash_map_iteratorINS_15__hash_iteratorIPNS_11__hash_nodeINS_17__hash_value_typeIyS3_EEPvEEEEEEbEERSA_OT_
+ __ZNSt3__114__split_bufferI9LSBindingRNS_9allocatorIS1_EEE17__destruct_at_endB9fqn220100EPS1_
+ __ZNSt3__114__split_bufferIN14LaunchServices17BindingEvaluation15ExtendedBindingERNS1_19MallocZoneAllocatorIS3_NS2_17BindingMallocZoneEEEE28__construct_at_end_with_sizeINS_11__wrap_iterIPS3_EEEEvT_m
+ __ZNSt3__114__split_bufferIN14LaunchServices17BindingEvaluation15ExtendedBindingERNS1_19MallocZoneAllocatorIS3_NS2_17BindingMallocZoneEEEE5clearB9fqn220100Ev
+ __ZNSt3__114__split_bufferINS_10shared_ptrIN14LaunchServices16PerThreadContextEEERNS_9allocatorIS4_EEE5clearB9fqn220100Ev
+ __ZNSt3__114__split_bufferINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEERNS_9allocatorISD_EEE17__destruct_at_endB9fqn220100EPSD_
+ __ZNSt3__114__split_bufferIU8__strongPU24objcproto13OS_xpc_object8NSObjectRNS_9allocatorIS4_EEED2Ev
+ __ZNSt3__115allocate_sharedB9fqn220100INS_6vectorINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEENS_9allocatorISE_EEEENSF_ISH_EEJRKSH_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB9fqn220100Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B9fqn220100Ej
+ __ZNSt3__116__if_likely_elseB9fqn220100IZNS_6vectorINS_4pairIP13objc_selectorPFvP11objc_objectS4_EEENS_9allocatorIS9_EEE12emplace_backIJRS4_S8_EEERS9_DpOT_EUlvE_ZNSD_IJSE_S8_EEESF_SI_EUlvE0_EEvbT_T0_
+ __ZNSt3__116__if_likely_elseB9fqn220100IZNS_6vectorINS_4pairIP13objc_selectorPFvP11objc_objectS4_EEENS_9allocatorIS9_EEE12emplace_backIJRS4_S8_EEERS9_DpOT_EUlvE_ZNSD_IJSE_S8_EEESF_SI_EUlvE0_EEvbT_T0_.cold.1
+ __ZNSt3__116__if_likely_elseB9fqn220100IZNS_6vectorINS_4pairIjPK12LSBundleDataEENS_9allocatorIS6_EEE12emplace_backIJRjRS5_EEERS6_DpOT_EUlvE_ZNSA_IJSB_SC_EEESD_SG_EUlvE0_EEvbT_T0_
+ __ZNSt3__116__if_likely_elseB9fqn220100IZNS_6vectorINS_4pairIjPK12LSBundleDataEENS_9allocatorIS6_EEE12emplace_backIJRjRS5_EEERS6_DpOT_EUlvE_ZNSA_IJSB_SC_EEESD_SG_EUlvE0_EEvbT_T0_.cold.1
+ __ZNSt3__116__if_likely_elseB9fqn220100IZNS_6vectorINS_4pairIjU8__strongP6NSUUIDEENS_9allocatorIS6_EEE12emplace_backIJS6_EEERS6_DpOT_EUlvE_ZNSA_IJS6_EEESB_SE_EUlvE0_EEvbT_T0_
+ __ZNSt3__116__if_likely_elseB9fqn220100IZNS_6vectorINS_4pairIjU8__strongP6NSUUIDEENS_9allocatorIS6_EEE12emplace_backIJS6_EEERS6_DpOT_EUlvE_ZNSA_IJS6_EEESB_SE_EUlvE0_EEvbT_T0_.cold.1
+ __ZNSt3__116__if_likely_elseB9fqn220100IZNS_6vectorINS_5tupleIJU8__strongP8NSStringjEEENS_9allocatorIS6_EEE12emplace_backIJS6_EEERS6_DpOT_EUlvE_ZNSA_IJS6_EEESB_SE_EUlvE0_EEvbT_T0_
+ __ZNSt3__116__if_likely_elseB9fqn220100IZNS_6vectorINS_5tupleIJU8__strongP8NSStringjEEENS_9allocatorIS6_EEE12emplace_backIJS6_EEERS6_DpOT_EUlvE_ZNSA_IJS6_EEESB_SE_EUlvE0_EEvbT_T0_.cold.1
+ __ZNSt3__116__pad_and_outputB9fqn220100IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__116__variant_detail12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE12__assign_altB9fqn220100ILm1ES5_RU8__strongKS4_EEvRNS0_5__altIXT_ET0_EEOT1_
+ __ZNSt3__116__variant_detail12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE12__assign_altB9fqn220100ILm2ES8_RU8__strongKS7_EEvRNS0_5__altIXT_ET0_EEOT1_
+ __ZNSt3__116__variant_detail12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE16__generic_assignB9fqn220100IRKNS0_17__copy_assignmentIS9_LNS0_6_TraitE1EEEEEvOT_
+ __ZNSt3__116__variant_detail12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE9__emplaceB9fqn220100ILm1EJRU8__strongKS4_EEERDaDpOT0_
+ __ZNSt3__116__variant_detail12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE9__emplaceB9fqn220100ILm2EJRU8__strongKS7_EEERDaDpOT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB9fqn220100IONS1_9__variant15__value_visitorIZN14LaunchServices10BaseBundle35BundleDataContainerReleaseOperationclEP11_LSDatabaseEUlT_E_EEJRNS0_6__baseILNS0_6_TraitE0EJNS_9monostateENS9_20DataContainerContext4PathENSK_5PathsEEEEEEEDcSD_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB9fqn220100IONS1_9__variant15__value_visitorIZN14LaunchServices20AppRecordEnumeration32VolumeContainerResolutionAdapter7resolveEP9LSContextEUlRKT_E_EEJRNS0_6__baseILNS0_6_TraitE1EJjU8__strongP5NSURLU8__strongP7NSErrorEEEEEEDcSD_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB9fqn220100IOZNS0_6__dtorINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEELNS0_6_TraitE1EE9__destroyB9fqn220100EvEUlRT_E_JRNS0_6__baseILSF_1EJjSA_SD_EEEEEEDcSH_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0ELm0EEE10__dispatchB9fqn220100IOZNS0_12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE16__generic_assignB9fqn220100IRKNS0_17__copy_assignmentISE_LNS0_6_TraitE1EEEEEvOT_EUlRSM_OT0_E_JRNS0_6__baseILSI_1EJjSA_SD_EEERKSU_EEEDcSM_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB9fqn220100IONS1_9__variant15__value_visitorIZN14LaunchServices10BaseBundle35BundleDataContainerReleaseOperationclEP11_LSDatabaseEUlT_E_EEJRNS0_6__baseILNS0_6_TraitE0EJNS_9monostateENS9_20DataContainerContext4PathENSK_5PathsEEEEEEEDcSD_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB9fqn220100IONS1_9__variant15__value_visitorIZN14LaunchServices20AppRecordEnumeration32VolumeContainerResolutionAdapter7resolveEP9LSContextEUlRKT_E_EEJRNS0_6__baseILNS0_6_TraitE1EJjU8__strongP5NSURLU8__strongP7NSErrorEEEEEEDcSD_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB9fqn220100IOZNS0_6__dtorINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEELNS0_6_TraitE1EE9__destroyB9fqn220100EvEUlRT_E_JRNS0_6__baseILSF_1EJjSA_SD_EEEEEEDcSH_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1ELm1EEE10__dispatchB9fqn220100IOZNS0_12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE16__generic_assignB9fqn220100IRKNS0_17__copy_assignmentISE_LNS0_6_TraitE1EEEEEvOT_EUlRSM_OT0_E_JRNS0_6__baseILSI_1EJjSA_SD_EEERKSU_EEEDcSM_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB9fqn220100IONS1_9__variant15__value_visitorIZN14LaunchServices10BaseBundle35BundleDataContainerReleaseOperationclEP11_LSDatabaseEUlT_E_EEJRNS0_6__baseILNS0_6_TraitE0EJNS_9monostateENS9_20DataContainerContext4PathENSK_5PathsEEEEEEEDcSD_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB9fqn220100IONS1_9__variant15__value_visitorIZN14LaunchServices20AppRecordEnumeration32VolumeContainerResolutionAdapter7resolveEP9LSContextEUlRKT_E_EEJRNS0_6__baseILNS0_6_TraitE1EJjU8__strongP5NSURLU8__strongP7NSErrorEEEEEEDcSD_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB9fqn220100IOZNS0_6__dtorINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEELNS0_6_TraitE1EE9__destroyB9fqn220100EvEUlRT_E_JRNS0_6__baseILSF_1EJjSA_SD_EEEEEEDcSH_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2ELm2EEE10__dispatchB9fqn220100IOZNS0_12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE16__generic_assignB9fqn220100IRKNS0_17__copy_assignmentISE_LNS0_6_TraitE1EEEEEvOT_EUlRSM_OT0_E_JRNS0_6__baseILSI_1EJjSA_SD_EEERKSU_EEEDcSM_DpT0_
+ __ZNSt3__116__variant_detail12__visitation9__variant13__visit_valueB9fqn220100IZN14LaunchServices20AppRecordEnumeration32VolumeContainerResolutionAdapter7resolveEP9LSContextEUlRKT_E_JRNS_7variantIJjU8__strongP5NSURLU8__strongP7NSErrorEEEEEEDcOS9_DpOT0_
+ __ZNSt3__116allocator_traitsIN14LaunchServices19MallocZoneAllocatorINS1_17BindingEvaluation15ExtendedBindingENS3_17BindingMallocZoneEEEE7destroyB9fqn220100IS4_Li0EEEvRS6_PT_
+ __ZNSt3__116allocator_traitsIN14LaunchServices19MallocZoneAllocatorINS1_17BindingEvaluation15ExtendedBindingENS3_17BindingMallocZoneEEEE9constructB9fqn220100IS4_JRKS4_ELi0EEEvRS6_PT_DpOT0_
+ __ZNSt3__116allocator_traitsIN14LaunchServices19MallocZoneAllocatorINS1_17BindingEvaluation15ExtendedBindingENS3_17BindingMallocZoneEEEE9constructB9fqn220100IS4_JS4_ELi0EEEvRS6_PT_DpOT0_
+ __ZNSt3__119__allocator_destroyB9fqn220100INS_9allocatorI9LSBindingEEPS2_S4_EEvRT_T0_T1_
+ __ZNSt3__119__allocator_destroyB9fqn220100INS_9allocatorINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEEEEPSE_SG_EEvRT_T0_T1_
+ __ZNSt3__119__shared_weak_count16__release_sharedB9fqn220100Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9fqn220100Ev
+ __ZNSt3__120__optional_copy_baseIN14LaunchServices16BindingEvaluatorELb0EEC2B9fqn220100ERKS3_
+ __ZNSt3__120__shared_ptr_emplaceINS_6vectorINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEENS_9allocatorISE_EEEENSF_ISH_EEEC2B9fqn220100IJRKSH_ESI_Li0EEESI_DpOT_
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B9fqn220100EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B9fqn220100EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B9fqn220100EPKcm
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPvEEEEEclB9fqn220100EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIN14LaunchServices14ContainerCache18PersonaAndPlatformENS_6vectorIU8__strongP8NSStringNS1_ISA_EEEEEEPvEEEEEclB9fqn220100EPSF_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIN14LaunchServices14ContainerCache18PersonaAndPlatformEU8__strongP19NSMutableDictionaryIP8NSStringP5NSURLEEEPvEEEEEclB9fqn220100EPSH_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIP17_opaque_pthread_tNS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEEPvEEEEEclB9fqn220100EPSC_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIPKvNS_6vectorINS_4pairIP13objc_selectorPFvP11objc_objectS9_EEENS1_ISE_EEEEEEPvEEEEEclB9fqn220100EPSJ_
+ __ZNSt3__123__optional_storage_baseI9LSBindingLb0EE13__assign_fromB9fqn220100INS_27__optional_move_assign_baseIS1_Lb0EEEEEvOT_
+ __ZNSt3__123__optional_storage_baseIN14LaunchServices13TypeEvaluator6ResultELb0EE13__assign_fromB9fqn220100INS_27__optional_move_assign_baseIS3_Lb0EEEEEvOT_
+ __ZNSt3__123__optional_storage_baseIU8__strongP12NSDictionaryIP8NSStringP11objc_objectELb0EE13__assign_fromB9fqn220100INS_27__optional_move_assign_baseIS8_Lb0EEEEEvOT_
+ __ZNSt3__123__optional_storage_baseIU8__strongP8NSStringLb0EE13__assign_fromB9fqn220100INS_27__optional_move_assign_baseIS3_Lb0EEEEEvOT_
+ __ZNSt3__124__put_character_sequenceB9fqn220100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__125__throw_bad_function_callB9fqn220100Ev
+ __ZNSt3__126__throw_bad_variant_accessB9fqn220100Ev
+ __ZNSt3__127__insertion_sort_incompleteB9fqn220100INS_17_ClassicAlgPolicyERZ69+[_LSDReadClient methodWithSelectorGetsImplicitExecutionContextRead:]E3$_1PP13objc_selectorEEbT1_S7_T0_
+ __ZNSt3__127__insertion_sort_incompleteB9fqn220100INS_17_ClassicAlgPolicyERZ87+[LSApplicationRecord(UserActivity) applicationRecordsForUserActivityType:limit:error:]E3$_1PNS_4pairIjPK12LSBundleDataEEEEbT1_SA_T0_
+ __ZNSt3__127__insertion_sort_incompleteB9fqn220100INS_17_ClassicAlgPolicyERZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]E3$_2PjEEbT1_S5_T0_
+ __ZNSt3__127__insertion_sort_incompleteB9fqn220100INS_17_ClassicAlgPolicyERZL33_LSBundleCopyArchitectures_CommonPK12LSBundleDataP7NSArrayIP8NSStringEE3$_0P11LSSliceDataEEbT1_SE_T0_
+ __ZNSt3__127__throw_bad_optional_accessB9fqn220100Ev
+ __ZNSt3__127__tree_balance_after_insertB9fqn220100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__134__uninitialized_allocator_relocateB9fqn220100IN14LaunchServices19MallocZoneAllocatorINS1_17BindingEvaluation15ExtendedBindingENS3_17BindingMallocZoneEEEPS4_EEvRT_T0_SA_SA_
+ __ZNSt3__134__uninitialized_allocator_relocateB9fqn220100INS_9allocatorI9LSBindingEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__134__uninitialized_allocator_relocateB9fqn220100INS_9allocatorINS_4pairIU8__strongP8NSStringN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder20ProtoLocalizedStringEEEEEPSA_EEvRT_T0_SF_SF_
+ __ZNSt3__134__uninitialized_allocator_relocateB9fqn220100INS_9allocatorIU6__weakP8LSRecordEEPS4_EEvRT_T0_S9_S9_
+ __ZNSt3__135__uninitialized_allocator_copy_implB9fqn220100IN14LaunchServices19MallocZoneAllocatorINS1_17BindingEvaluation15ExtendedBindingENS3_17BindingMallocZoneEEEPS4_S7_S7_EET2_RT_T0_T1_S8_
+ __ZNSt3__135__uninitialized_allocator_copy_implB9fqn220100INS_9allocatorI9LSBindingEEPN14LaunchServices17BindingEvaluation15ExtendedBindingES7_PS2_EET2_RT_T0_T1_S9_
+ __ZNSt3__135__uninitialized_allocator_copy_implB9fqn220100INS_9allocatorINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEEEEPSE_SG_SG_EET2_RT_T0_T1_SH_
+ __ZNSt3__13mapI23os_eligibility_domain_t23os_eligibility_answer_tNS_4lessIS1_EENS_9allocatorINS_4pairIKS1_S2_EEEEE6insertB9fqn220100INS6_IS1_S2_EELi0EEENS6_INS_14__map_iteratorINS_15__tree_iteratorINS_12__value_typeIS1_S2_EEPNS_11__tree_nodeISG_PvEElEEEEbEEOT_
+ __ZNSt3__13mapI23os_eligibility_domain_tN14LaunchServices7notifyd11NotifyTokenENS_4lessIS1_EENS_9allocatorINS_4pairIKS1_S4_EEEEE7emplaceB9fqn220100IJNS8_IS1_S4_EEEEENS8_INS_14__map_iteratorINS_15__tree_iteratorINS_12__value_typeIS1_S4_EEPNS_11__tree_nodeISI_PvEElEEEEbEEDpOT_
+ __ZNSt3__13mapI23os_eligibility_domain_tNS_6vectorI23os_eligibility_answer_tNS_9allocatorIS3_EEEENS_4lessIS1_EENS4_INS_4pairIKS1_S6_EEEEE7emplaceB9fqn220100IJRS1_S6_EEENS9_INS_14__map_iteratorINS_15__tree_iteratorINS_12__value_typeIS1_S6_EEPNS_11__tree_nodeISJ_PvEElEEEEbEEDpOT_
+ __ZNSt3__13mapIjU8__strongP8NSStringNS_4lessIjEENS_9allocatorINS_4pairIKjS3_EEEEE6insertB9fqn220100INS7_IjS3_EELi0EEENS7_INS_14__map_iteratorINS_15__tree_iteratorINS_12__value_typeIjS3_EEPNS_11__tree_nodeISH_PvEElEEEEbEEOT_
+ __ZNSt3__13mapImU8__strongU13block_pointerFvvENS_4lessImEENS_9allocatorINS_4pairIKmS3_EEEEE6insertB9fqn220100INS7_ImU8__strongP11objc_objectEELi0EEENS7_INS_14__map_iteratorINS_15__tree_iteratorINS_12__value_typeImS3_EEPNS_11__tree_nodeISK_PvEElEEEEbEEOT_
+ __ZNSt3__14pairIKN14LaunchServices14ContainerCache18PersonaAndPlatformENS_6vectorIU8__strongP8NSStringNS_9allocatorIS8_EEEEEC2B9fqn220100IS4_SB_Li0EEERNS0_IT_T0_EE
+ __ZNSt3__14swapB9fqn220100IN14LaunchServices17BindingEvaluation15ExtendedBindingEEENS_9enable_ifIXaasr21is_move_constructibleIT_EE5valuesr18is_move_assignableIS5_EE5valueEvE4typeERS5_S8_
+ __ZNSt3__15arrayIU8__strongP8NSStringLm6EED1Ev
+ __ZNSt3__16__treeINS_12__value_typeI23os_eligibility_domain_t23os_eligibility_answer_tEENS_19__map_value_compareIS2_NS_4pairIKS2_S3_EENS_4lessIS2_EEEENS_9allocatorIS8_EEE14__tree_deleterclB9fqn220100EPNS_11__tree_nodeIS4_PvEE
+ __ZNSt3__16__treeINS_12__value_typeI23os_eligibility_domain_t23os_eligibility_answer_tEENS_19__map_value_compareIS2_NS_4pairIKS2_S3_EENS_4lessIS2_EEEENS_9allocatorIS8_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSJ_SJ_
+ __ZNSt3__16__treeINS_12__value_typeI23os_eligibility_domain_tN14LaunchServices7notifyd11NotifyTokenEEENS_19__map_value_compareIS2_NS_4pairIKS2_S5_EENS_4lessIS2_EEEENS_9allocatorISA_EEE14__tree_deleterclB9fqn220100EPNS_11__tree_nodeIS6_PvEE
+ __ZNSt3__16__treeINS_12__value_typeI23os_eligibility_domain_tN14LaunchServices7notifyd11NotifyTokenEEENS_19__map_value_compareIS2_NS_4pairIKS2_S5_EENS_4lessIS2_EEEENS_9allocatorISA_EEE16__construct_nodeIJNS8_IS2_S5_EEEEENS_10unique_ptrINS_11__tree_nodeIS6_PvEENS_22__tree_node_destructorINSE_ISM_EEEEEEDpOT_
+ __ZNSt3__16__treeINS_12__value_typeI23os_eligibility_domain_tN14LaunchServices7notifyd11NotifyTokenEEENS_19__map_value_compareIS2_NS_4pairIKS2_S5_EENS_4lessIS2_EEEENS_9allocatorISA_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSL_SL_
+ __ZNSt3__16__treeINS_12__value_typeI23os_eligibility_domain_tNS_6vectorI23os_eligibility_answer_tNS_9allocatorIS4_EEEEEENS_19__map_value_compareIS2_NS_4pairIKS2_S7_EENS_4lessIS2_EEEENS5_ISC_EEE14__tree_deleterclB9fqn220100EPNS_11__tree_nodeIS8_PvEE
+ __ZNSt3__16__treeINS_12__value_typeI23os_eligibility_domain_tNS_6vectorI23os_eligibility_answer_tNS_9allocatorIS4_EEEEEENS_19__map_value_compareIS2_NS_4pairIKS2_S7_EENS_4lessIS2_EEEENS5_ISC_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSM_SM_
+ __ZNSt3__16__treeINS_12__value_typeIjU8__strongP8NSStringEENS_19__map_value_compareIjNS_4pairIKjS4_EENS_4lessIjEEEENS_9allocatorIS9_EEE14__tree_deleterclB9fqn220100EPNS_11__tree_nodeIS5_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIjU8__strongP8NSStringEENS_19__map_value_compareIjNS_4pairIKjS4_EENS_4lessIjEEEENS_9allocatorIS9_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSK_SK_
+ __ZNSt3__16__treeINS_12__value_typeImU8__strongU13block_pointerFvvEEENS_19__map_value_compareImNS_4pairIKmS4_EENS_4lessImEEEENS_9allocatorIS9_EEE14__erase_uniqueImEEmRKT_
+ __ZNSt3__16__treeINS_12__value_typeImU8__strongU13block_pointerFvvEEENS_19__map_value_compareImNS_4pairIKmS4_EENS_4lessImEEEENS_9allocatorIS9_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSK_SK_
+ __ZNSt3__16__treeINS_12__value_typeImU8__strongU13block_pointerFvvEEENS_19__map_value_compareImNS_4pairIKmS4_EENS_4lessImEEEENS_9allocatorIS9_EEE21__remove_node_pointerEPNS_11__tree_nodeIS5_PvEE
+ __ZNSt3__16__treeINS_12__value_typeImU8__strongU13block_pointerFvvEEENS_19__map_value_compareImNS_4pairIKmS4_EENS_4lessImEEEENS_9allocatorIS9_EEE5eraseENS_21__tree_const_iteratorIS5_PNS_11__tree_nodeIS5_PvEElEE
+ __ZNSt3__16removeB9fqn220100INS_11__wrap_iterIPU6__weakP8LSRecordEEDnEET_S7_S7_RKT0_
+ __ZNSt3__16vectorI11LSSliceDataNS_9allocatorIS1_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorI11LSSliceDataNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI13LSBundleClassNS_9allocatorIS1_EEE11__vallocateB9fqn220100Em
+ __ZNSt3__16vectorI13LSBundleClassNS_9allocatorIS1_EEE18__assign_with_sizeB9fqn220100INS_17_ClassicAlgPolicyEPKS1_S8_EEvT0_T1_l
+ __ZNSt3__16vectorI13LSBundleClassNS_9allocatorIS1_EEE18__assign_with_sizeB9fqn220100INS_17_ClassicAlgPolicyEPS1_S7_EEvT0_T1_l
+ __ZNSt3__16vectorI13LSBundleClassNS_9allocatorIS1_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorI13LSBundleClassNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI13LSBundleClassNS_9allocatorIS1_EEEC2B9fqn220100ERKS4_
+ __ZNSt3__16vectorI13LSPersonaTypeNS_9allocatorIS1_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorI13LSPersonaTypeNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI23os_eligibility_answer_tNS_9allocatorIS1_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorI23os_eligibility_answer_tNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI8_NSRangeNS_9allocatorIS1_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorI8_NSRangeNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI9LSBindingNS_9allocatorIS1_EEE16__destroy_vectorclB9fqn220100Ev
+ __ZNSt3__16vectorI9LSBindingNS_9allocatorIS1_EEE18__insert_with_sizeB9fqn220100INS_17_ClassicAlgPolicyENS_11__wrap_iterIPN14LaunchServices17BindingEvaluation15ExtendedBindingEEESC_EENS7_IPS1_EENS7_IPKS1_EET0_T1_l
+ __ZNSt3__16vectorI9LSBindingNS_9allocatorIS1_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorI9LSBindingNS_9allocatorIS1_EEE27__insert_assign_n_uncheckedB9fqn220100INS_17_ClassicAlgPolicyENS_11__wrap_iterIPN14LaunchServices17BindingEvaluation15ExtendedBindingEEELi0EEEvT0_lPS1_
+ __ZNSt3__16vectorI9LSBindingNS_9allocatorIS1_EEE5clearB9fqn220100Ev
+ __ZNSt3__16vectorIN14LaunchServices10BaseBundle35BundleDataContainerReleaseOperationENS_9allocatorIS3_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIN14LaunchServices10BaseBundle35BundleDataContainerReleaseOperationENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorIN14LaunchServices10BaseBundle35BundleDataContainerReleaseOperationENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS1_19MallocZoneAllocatorIS3_NS2_17BindingMallocZoneEEEE11__vallocateB9fqn220100Em
+ __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS1_19MallocZoneAllocatorIS3_NS2_17BindingMallocZoneEEEE16__destroy_vectorclB9fqn220100Ev
+ __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS1_19MallocZoneAllocatorIS3_NS2_17BindingMallocZoneEEEE16__init_with_sizeB9fqn220100INS_11__wrap_iterIPKS3_EESC_EEvT_T0_m
+ __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS1_19MallocZoneAllocatorIS3_NS2_17BindingMallocZoneEEEE18__assign_with_sizeB9fqn220100INS_17_ClassicAlgPolicyEPKS3_SB_EEvT0_T1_l
+ __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS1_19MallocZoneAllocatorIS3_NS2_17BindingMallocZoneEEEE18__insert_with_sizeB9fqn220100INS_17_ClassicAlgPolicyENS_11__wrap_iterIPS3_EESC_EESC_NSA_IPKS3_EET0_T1_l
+ __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS1_19MallocZoneAllocatorIS3_NS2_17BindingMallocZoneEEEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS1_19MallocZoneAllocatorIS3_NS2_17BindingMallocZoneEEEE9push_backB9fqn220100ERKS3_
+ __ZNSt3__16vectorIN14LaunchServices30FeatureFlagPredicateEvaluation20FeatureFlagSpecifierENS_9allocatorIS3_EEE16__destroy_vectorclB9fqn220100Ev
+ __ZNSt3__16vectorIN14LaunchServices30FeatureFlagPredicateEvaluation20FeatureFlagSpecifierENS_9allocatorIS3_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIN14LaunchServices30FeatureFlagPredicateEvaluation20FeatureFlagSpecifierENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorIN14LaunchServices5Types41EnumeratedTypeUnitOrDynamicTypeIdentifierENS_9allocatorIS3_EEE16__destroy_vectorclB9fqn220100Ev
+ __ZNSt3__16vectorIN14LaunchServices5Types41EnumeratedTypeUnitOrDynamicTypeIdentifierENS_9allocatorIS3_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIN14LaunchServices5Types41EnumeratedTypeUnitOrDynamicTypeIdentifierENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorIN14LaunchServices5Types41EnumeratedTypeUnitOrDynamicTypeIdentifierENS_9allocatorIS3_EEE9push_backB9fqn220100ERKS3_
+ __ZNSt3__16vectorINS_10shared_ptrIN14LaunchServices16PerThreadContextEEENS_9allocatorIS4_EEE16__destroy_vectorclB9fqn220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN14LaunchServices16PerThreadContextEEENS_9allocatorIS4_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN14LaunchServices16PerThreadContextEEENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJRKS4_EEEPS4_DpOT_
+ __ZNSt3__16vectorINS_10shared_ptrIN14LaunchServices16PerThreadContextEEENS_9allocatorIS4_EEE5clearB9fqn220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN14LaunchServices16PerThreadContextEEENS_9allocatorIS4_EEE9push_backB9fqn220100ERKS4_
+ __ZNSt3__16vectorINS_4pairIP13objc_selectorPFvP11objc_objectS3_EEENS_9allocatorIS8_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorINS_4pairIP13objc_selectorPFvP11objc_objectS3_EEENS_9allocatorIS8_EEE24__emplace_back_slow_pathIJRS3_S7_EEEPS8_DpOT_
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder20ProtoLocalizedStringEEENS_9allocatorIS9_EEE16__destroy_vectorclB9fqn220100Ev
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder20ProtoLocalizedStringEEENS_9allocatorIS9_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder20ProtoLocalizedStringEEENS_9allocatorIS9_EEE5clearB9fqn220100Ev
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder20ProtoLocalizedStringEEENS_9allocatorIS9_EEE9push_backB9fqn220100EOS9_
+ __ZNSt3__16vectorINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEENS_9allocatorISD_EEE11__vallocateB9fqn220100Em
+ __ZNSt3__16vectorINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEENS_9allocatorISD_EEE16__destroy_vectorclB9fqn220100Ev
+ __ZNSt3__16vectorINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEENS_9allocatorISD_EEE16__init_with_sizeB9fqn220100IPSD_SI_EEvT_T0_m
+ __ZNSt3__16vectorINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEENS_9allocatorISD_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEENS_9allocatorISD_EEE24__emplace_back_slow_pathIJU8__strongP11objc_objectRSC_EEEPSD_DpOT_
+ __ZNSt3__16vectorINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEENS_9allocatorISD_EEE5clearB9fqn220100Ev
+ __ZNSt3__16vectorINS_4pairIjPK12LSBundleDataEENS_9allocatorIS5_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorINS_4pairIjPK12LSBundleDataEENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJRjRS4_EEEPS5_DpOT_
+ __ZNSt3__16vectorINS_4pairIjU8__strongP6FSNodeEENS_9allocatorIS5_EEE16__destroy_vectorclB9fqn220100Ev
+ __ZNSt3__16vectorINS_4pairIjU8__strongP6FSNodeEENS_9allocatorIS5_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorINS_4pairIjU8__strongP6FSNodeEENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJRjRS4_EEEPS5_DpOT_
+ __ZNSt3__16vectorINS_4pairIjU8__strongP6NSUUIDEENS_9allocatorIS5_EEE16__destroy_vectorclB9fqn220100Ev
+ __ZNSt3__16vectorINS_4pairIjU8__strongP6NSUUIDEENS_9allocatorIS5_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorINS_4pairIjU8__strongP6NSUUIDEENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJS5_EEEPS5_DpOT_
+ __ZNSt3__16vectorINS_5tupleIJU8__strongP8NSStringjEEENS_9allocatorIS5_EEE11__vallocateB9fqn220100Em
+ __ZNSt3__16vectorINS_5tupleIJU8__strongP8NSStringjEEENS_9allocatorIS5_EEE13__vdeallocateEv
+ __ZNSt3__16vectorINS_5tupleIJU8__strongP8NSStringjEEENS_9allocatorIS5_EEE16__destroy_vectorclB9fqn220100Ev
+ __ZNSt3__16vectorINS_5tupleIJU8__strongP8NSStringjEEENS_9allocatorIS5_EEE16__init_with_sizeB9fqn220100IPS5_SA_EEvT_T0_m
+ __ZNSt3__16vectorINS_5tupleIJU8__strongP8NSStringjEEENS_9allocatorIS5_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorINS_5tupleIJU8__strongP8NSStringjEEENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJS5_EEEPS5_DpOT_
+ __ZNSt3__16vectorINS_5tupleIJU8__strongP8NSStringjEEENS_9allocatorIS5_EEE9push_backB9fqn220100EOS5_
+ __ZNSt3__16vectorIP8LSRecordNS_9allocatorIS3_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIPK10__CFStringNS_9allocatorIS3_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIPK10__CFStringNS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE11__vallocateB9fqn220100Em
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIPvNS_9allocatorIS1_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIPvNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorIPvNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE11__vallocateB9fqn220100Em
+ __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE16__destroy_vectorclB9fqn220100Ev
+ __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE16__init_with_sizeB9fqn220100IPKS2_S9_EEvT_T0_m
+ __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE16__init_with_sizeB9fqn220100IPS3_S8_EEvT_T0_m
+ __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE18__insert_with_sizeB9fqn220100INS_17_ClassicAlgPolicyEPKS2_SA_EENS_11__wrap_iterIPS3_EENSB_IPU6__weakKS2_EET0_T1_l
+ __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE27__insert_assign_n_uncheckedB9fqn220100INS_17_ClassicAlgPolicyEPKS2_Li0EEEvT0_lPS3_
+ __ZNSt3__16vectorIU8__strongP19LSApplicationRecordNS_9allocatorIS3_EEE16__destroy_vectorclB9fqn220100Ev
+ __ZNSt3__16vectorIU8__strongP19LSApplicationRecordNS_9allocatorIS3_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIU8__strongP19LSApplicationRecordNS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEE11__vallocateB9fqn220100Em
+ __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEE16__destroy_vectorclB9fqn220100Ev
+ __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEE16__init_with_sizeB9fqn220100IPS3_S8_EEvT_T0_m
+ __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRU8__strongKS2_EEEPS3_DpOT_
+ __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEE7reserveEm
+ __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEE9push_backB9fqn220100ERU8__strongKS2_
+ __ZNSt3__16vectorIU8__strongPU24objcproto13OS_xpc_object8NSObjectNS_9allocatorIS4_EEE16__destroy_vectorclB9fqn220100Ev
+ __ZNSt3__16vectorIU8__strongPU24objcproto13OS_xpc_object8NSObjectNS_9allocatorIS4_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIU8__strongPU24objcproto13OS_xpc_object8NSObjectNS_9allocatorIS4_EEE24__emplace_back_slow_pathIJS4_EEEPS4_DpOT_
+ __ZNSt3__16vectorIU8__strongPU24objcproto13OS_xpc_object8NSObjectNS_9allocatorIS4_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS4_RS6_EE
+ __ZNSt3__16vectorIU8__strongPU24objcproto13OS_xpc_object8NSObjectNS_9allocatorIS4_EEE7reserveEm
+ __ZNSt3__16vectorIU8__strongU13block_pointerFvbP11_LSDatabaseP7NSErrorENS_9allocatorIS7_EEE16__destroy_vectorclB9fqn220100Ev
+ __ZNSt3__16vectorIU8__strongU13block_pointerFvbP11_LSDatabaseP7NSErrorENS_9allocatorIS7_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIU8__strongU13block_pointerFvbP11_LSDatabaseP7NSErrorENS_9allocatorIS7_EEE24__emplace_back_slow_pathIJS7_EEEPS7_DpOT_
+ __ZNSt3__16vectorIU8__strongU13block_pointerFvvENS_9allocatorIS3_EEE11__vallocateB9fqn220100Em
+ __ZNSt3__16vectorIU8__strongU13block_pointerFvvENS_9allocatorIS3_EEE16__destroy_vectorclB9fqn220100Ev
+ __ZNSt3__16vectorIU8__strongU13block_pointerFvvENS_9allocatorIS3_EEE16__init_with_sizeB9fqn220100IPS3_S8_EEvT_T0_m
+ __ZNSt3__16vectorIU8__strongU13block_pointerFvvENS_9allocatorIS3_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIU8__strongU13block_pointerFvvENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRU8__strongKS2_EEEPS3_DpOT_
+ __ZNSt3__16vectorIU8__strongU13block_pointerFvvENS_9allocatorIS3_EEE9push_backB9fqn220100ERU8__strongKS2_
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE24__emplace_back_slow_pathIJRKcEEEPcDpOT_
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE24__emplace_back_slow_pathIJcEEEPcDpOT_
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB9fqn220100Em
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE11__vallocateB9fqn220100Em
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE18__assign_with_sizeB9fqn220100INS_17_ClassicAlgPolicyEPjS6_EEvT0_T1_l
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE18__insert_with_sizeB9fqn220100INS_17_ClassicAlgPolicyENS_11__wrap_iterIPjEES8_EES8_NS6_IPKjEET0_T1_l
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE24__emplace_back_slow_pathIJRKjEEEPjDpOT_
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE24__emplace_back_slow_pathIJRjEEEPjDpOT_
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE24__emplace_back_slow_pathIJjEEEPjDpOT_
+ __ZNSt3__16vectorIjNS_9allocatorIjEEEC2B9fqn220100ERKS3_
+ __ZNSt3__16vectorItNS_9allocatorItEEE11__vallocateB9fqn220100Em
+ __ZNSt3__16vectorItNS_9allocatorItEEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__17__sort3B9fqn220100INS_17_ClassicAlgPolicyERZ87+[LSApplicationRecord(UserActivity) applicationRecordsForUserActivityType:limit:error:]E3$_1PNS_4pairIjPK12LSBundleDataEELi0EEEbT1_SA_SA_T0_
+ __ZNSt3__17__sort3B9fqn220100INS_17_ClassicAlgPolicyERZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]E3$_2PjLi0EEEbT1_S5_S5_T0_
+ __ZNSt3__17__sort4B9fqn220100INS_17_ClassicAlgPolicyERZ87+[LSApplicationRecord(UserActivity) applicationRecordsForUserActivityType:limit:error:]E3$_1PNS_4pairIjPK12LSBundleDataEELi0EEEvT1_SA_SA_SA_T0_
+ __ZNSt3__17__sort4B9fqn220100INS_17_ClassicAlgPolicyERZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]E3$_2PjLi0EEEvT1_S5_S5_S5_T0_
+ __ZNSt3__17__sort4B9fqn220100INS_17_ClassicAlgPolicyERZL33_LSBundleCopyArchitectures_CommonPK12LSBundleDataP7NSArrayIP8NSStringEE3$_0P11LSSliceDataLi0EEEvT1_SE_SE_SE_T0_
+ __ZNSt3__17__sort5B9fqn220100INS_17_ClassicAlgPolicyERZ87+[LSApplicationRecord(UserActivity) applicationRecordsForUserActivityType:limit:error:]E3$_1PNS_4pairIjPK12LSBundleDataEELi0EEEvT1_SA_SA_SA_SA_T0_
+ __ZNSt3__17__sort5B9fqn220100INS_17_ClassicAlgPolicyERZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]E3$_2PjLi0EEEvT1_S5_S5_S5_S5_T0_
+ __ZNSt3__17__sort5B9fqn220100INS_17_ClassicAlgPolicyERZL33_LSBundleCopyArchitectures_CommonPK12LSBundleDataP7NSArrayIP8NSStringEE3$_0P11LSSliceDataLi0EEEvT1_SE_SE_SE_SE_T0_
+ __ZNSt3__18__any_ofB9fqn220100INS_11__wrap_iterIPKN14LaunchServices30FeatureFlagPredicateEvaluation20FeatureFlagSpecifierEEES7_NS_10__identityEZNS_8__all_ofB9fqn220100IS7_S7_S8_ZNKS3_9Predicate8evaluateEPU32objcproto21LSFeatureFlagResolver11objc_objectEUlRS5_E_EEbT_T0_RT2_RT1_EUlSD_E_EEbSF_SG_SI_SK_
+ __ZNSt3__18__invokeB9fqn220100IJZNS_16__variant_detail12__assignmentINS1_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE16__generic_assignB9fqn220100IRKNS1_17__copy_assignmentISA_LNS1_6_TraitE1EEEEEvOT_EUlRSI_OT0_E_RNS1_5__altILm0EjEERKSP_EEENS_20__invoke_result_implIvJDpT_EE4typeEDpOSU_
+ __ZNSt3__18optionalI9LSBindingEaSB9fqn220100IRKN14LaunchServices17BindingEvaluation15ExtendedBindingELi0EEERS2_OT_
+ __ZNSt3__18optionalI9LSBindingEaSB9fqn220100IS1_Li0EEERS2_OT_
+ __ZNSt3__18optionalIN14LaunchServices11OpenStaging20StagingDirectoryInfoEE7emplaceB9fqn220100IJRU8__strongP8NSStringRU8__strongP6FSNodeRxELi0EEERS3_DpOT_
+ __ZNSt3__18optionalIN14LaunchServices16BindingEvaluatorEEaSB9fqn220100IS2_Li0EEERS3_OT_
+ __ZNSt3__18optionalIN14LaunchServices16EligibilityCache11NotifyStateEE7emplaceB9fqn220100IJU8__strongU13block_pointerFvvEELi0EEERS3_DpOT_
+ __ZNSt3__18optionalIN14LaunchServices30EligibilityPredicateEvaluation9PredicateEE7emplaceB9fqn220100IJS3_ELi0EEERS3_DpOT_
+ __ZNSt3__18optionalIN14LaunchServices30FeatureFlagPredicateEvaluation9PredicateEE7emplaceB9fqn220100IJS3_ELi0EEERS3_DpOT_
+ __ZNSt3__18optionalIU8__strongP7NSErrorEaSB9fqn220100IRS3_Li0EEERS4_OT_
+ __ZNSt3__19__sift_upB9fqn220100INS_17_ClassicAlgPolicyERZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]E3$_2PjEEvT1_S5_OT0_NS_15iterator_traitsIS5_E15difference_typeE
+ __ZNSt3__19allocatorI11LSSliceDataE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorI13LSBundleClassE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorI13LSPersonaTypeE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorI23os_eligibility_answer_tE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorI8_NSRangeE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorI9LSBindingE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorIN14LaunchServices10BaseBundle35BundleDataContainerReleaseOperationEE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorIN14LaunchServices30FeatureFlagPredicateEvaluation20FeatureFlagSpecifierEE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorIN14LaunchServices5Types41EnumeratedTypeUnitOrDynamicTypeIdentifierEE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorINS_10shared_ptrIN14LaunchServices16PerThreadContextEEEE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorINS_4pairIP13objc_selectorPFvP11objc_objectS3_EEEE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorINS_4pairIU8__strongP8NSStringN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder20ProtoLocalizedStringEEEE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEEE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorINS_4pairIjPK12LSBundleDataEEE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorINS_4pairIjU8__strongP6FSNodeEEE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorINS_4pairIjU8__strongP6NSUUIDEEE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorINS_5tupleIJU8__strongP8NSStringjEEEE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorIP8LSRecordE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorIPK10__CFStringE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorIPKcE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorIPKvE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorIPvE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorIU6__weakP8LSRecordE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorIU8__strongP19LSApplicationRecordE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorIU8__strongP8NSStringE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorIU8__strongPU24objcproto13OS_xpc_object8NSObjectE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorIU8__strongU13block_pointerFvbP11_LSDatabaseP7NSErrorEE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorIU8__strongU13block_pointerFvvEE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorIiE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorIjE17allocate_at_leastB9fqn220100Em
+ __ZNSt3__19allocatorItE17allocate_at_leastB9fqn220100Em
+ __ZSt28__throw_bad_array_new_lengthB9fqn220100v
+ __ZTVNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore removeEntriesForBundleIdentifier:]E3$_2FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EEE
+ __ZTVNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore setEntry:forApplication:category:]E3$_1FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EEE
+ __ZZ29_LSDatabaseGetSeedingWorkloopE4once
+ __ZZ29_LSDatabaseGetSeedingWorkloopE8workloop
+ __ZZ33_LSGetPersonalPersonaUniqueStringE12uniqueString
+ __ZZ33_LSGetPersonalPersonaUniqueStringE1m
+ __ZZ38+[_LSEmptyContainerMap sharedInstance]E8instance
+ __ZZ38+[_LSEmptyContainerMap sharedInstance]E9onceToken
+ __ZZ39_LSNSXPCConnectionMayMapDatabase_CachedE8cacheKey
+ __ZZ43+[_LSEmptyGroupContainerMap sharedInstance]E8instance
+ __ZZ43+[_LSEmptyGroupContainerMap sharedInstance]E9onceToken
+ __ZZ48+[LSBundleRecord _getBundleRecordFinderForNode:]EN3$_38__invokeERN14LaunchServices8Database7ContextEP6FSNodePU15__autoreleasingP7NSError
+ __ZZ69+[_LSDReadClient methodWithSelectorGetsImplicitExecutionContextRead:]E7selList
+ __ZZ69+[_LSDReadClient methodWithSelectorGetsImplicitExecutionContextRead:]E9onceToken
+ __ZZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]EN3$_115getAndCacheNameEj
+ __ZZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]EN3$_115getAndCacheNameEj.cold.1
+ __ZZL23_LSOpenOperationPerformP5NSURLP12NSFileHandleP8NSStringbS4_P12NSDictionaryIS4_P11objc_objectES9_PU42objcproto31LSOpenResourceOperationDelegate11objc_objectP15NSXPCConnectionU13block_pointerFvbP7NSErrorEE5sOnce
+ __ZZL35_LSDyldSaysCPUTypeSubtypeIsRunnableiiE9archNames
+ __ZZL35_LSDyldSaysCPUTypeSubtypeIsRunnableiiE9onceToken
+ __ZZL35enumerateProductPlatformKeySuffixesIU8__strongP12NSDictionaryIP8NSStringP11objc_objectEZ53-[_LSStringsFileContent subscriptLoctableWithLocale:]E3$_2ENSt3__18optionalIT_EES2_RKT0_E25platformThenProductSuffix
+ __ZZL35enumerateProductPlatformKeySuffixesIU8__strongP12NSDictionaryIP8NSStringP11objc_objectEZ53-[_LSStringsFileContent subscriptLoctableWithLocale:]E3$_2ENSt3__18optionalIT_EES2_RKT0_E25productThenPlatformSuffix
+ __ZZL35enumerateProductPlatformKeySuffixesIU8__strongP12NSDictionaryIP8NSStringP11objc_objectEZ53-[_LSStringsFileContent subscriptLoctableWithLocale:]E3$_2ENSt3__18optionalIT_EES2_RKT0_E9onceToken
+ __ZZL35enumerateProductPlatformKeySuffixesIU8__strongP8NSStringZ60-[_LSStringsFileContent _queryLoadedPlist:forRawKey:locale:]E3$_3ENSt3__18optionalIT_EES1_RKT0_E25platformThenProductSuffix
+ __ZZL35enumerateProductPlatformKeySuffixesIU8__strongP8NSStringZ60-[_LSStringsFileContent _queryLoadedPlist:forRawKey:locale:]E3$_3ENSt3__18optionalIT_EES1_RKT0_E25productThenPlatformSuffix
+ __ZZL35enumerateProductPlatformKeySuffixesIU8__strongP8NSStringZ60-[_LSStringsFileContent _queryLoadedPlist:forRawKey:locale:]E3$_3ENSt3__18optionalIT_EES1_RKT0_E9onceToken
+ __ZZL50_LSRestrictIdentifierAccessForTypeAndXPCConnection23_LSDeviceIdentifierTypeP15NSXPCConnectionE15denialFunctions
+ __ZZL50_LSRestrictIdentifierAccessForTypeAndXPCConnection23_LSDeviceIdentifierTypeP15NSXPCConnectionENUlS1_S_E0_8__invokeES1_S_
+ __ZZL50_LSRestrictIdentifierAccessForTypeAndXPCConnection23_LSDeviceIdentifierTypeP15NSXPCConnectionENUlS1_S_E1_8__invokeES1_S_
+ __ZZL50_LSRestrictIdentifierAccessForTypeAndXPCConnection23_LSDeviceIdentifierTypeP15NSXPCConnectionENUlS1_S_E_8__invokeES1_S_
+ __ZZN14LaunchServices10BaseBundle28DataContainerWritableContext13removePersonaEP11_LSDatabaseP8NSStringENKUlS5_S5_PhE_clES5_S5_S6_
+ __ZZNSt3__112__hash_tableINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4hashIS6_EENS_8equal_toIS6_EENS4_IS6_EEE16__emplace_uniqueB9fqn220100IJS6_EEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEEDpOT_ENKUlRKS6_OS6_E_clESQ_SR_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeI12LSSessionKey31LSQuickSessionAvailabilityStateEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S3_EE18LSSessionKeyHasher22LSSessionKeyComparatorEENS_21__unordered_map_equalIS2_S8_SA_S9_EENS_9allocatorIS8_EEE16__emplace_uniqueB9fqn220100IJRKNS_21piecewise_construct_tENS_5tupleIJOS2_EEENSL_IJEEEEEENS6_INS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEEbEEDpOT_ENKUlRS7_SK_OSN_OSO_E_clESZ_SK_S10_S11_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeI12LSSessionKeyP9LSSessionEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S4_EE18LSSessionKeyHasher22LSSessionKeyComparatorEENS_21__unordered_map_equalIS2_S9_SB_SA_EENS_9allocatorIS9_EEE16__emplace_uniqueB9fqn220100IJRKNS_21piecewise_construct_tENS_5tupleIJRS8_EEENSM_IJEEEEEENS7_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEEDpOT_ENKUlSN_SL_OSO_OSP_E_clESN_SL_S10_S11_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIN14LaunchServices14ContainerCache18PersonaAndPlatformENS_6vectorIU8__strongP8NSStringNS_9allocatorIS8_EEEEEENS_22__unordered_map_hasherIS4_NS_4pairIKS4_SB_EENS3_22PersonaAndPlatformHashENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_SG_SJ_SH_EENS9_ISG_EEE16__emplace_uniqueB9fqn220100IJRKNS_21piecewise_construct_tENS_5tupleIJOS4_EEENST_IJEEEEEENSE_INS_15__hash_iteratorIPNS_11__hash_nodeISC_PvEEEEbEEDpOT_ENKUlRSF_SS_OSV_OSW_E_clES17_SS_S18_S19_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIN14LaunchServices14ContainerCache18PersonaAndPlatformEU8__strongP19NSMutableDictionaryIP8NSStringP5NSURLEEENS_22__unordered_map_hasherIS4_NS_4pairIKS4_SC_EENS3_22PersonaAndPlatformHashENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_SH_SK_SI_EENS_9allocatorISH_EEE16__emplace_uniqueB9fqn220100IJNSF_IS4_SC_EEEEENSF_INS_15__hash_iteratorIPNS_11__hash_nodeISD_PvEEEEbEEDpOT_ENKUlRSG_OSS_E_clES13_S14_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selector18FSSelectorCategoryEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S4_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_S9_SD_SB_EENS_9allocatorIS9_EEE16__emplace_uniqueB9fqn220100IJNS7_IS3_S4_EEEEENS7_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEEDpOT_ENKUlRS8_OSL_E_clESW_SX_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SB_SF_SD_EENS_9allocatorISB_EEE16__emplace_uniqueB9fqn220100IJRS3_RU8__strongKS5_EEENS9_INS_15__hash_iteratorIPNS_11__hash_nodeIS7_PvEEEEbEEDpOT_ENKUlRSA_SN_SP_E_clES10_SN_SP_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SB_SF_SD_EENS_9allocatorISB_EEE16__emplace_uniqueB9fqn220100IJS3_DnEEENS9_INS_15__hash_iteratorIPNS_11__hash_nodeIS7_PvEEEEbEEDpOT_ENKUlRSA_OS3_ODnE_clESX_SY_SZ_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SB_SF_SD_EENS_9allocatorISB_EEE16__emplace_uniqueB9fqn220100IJS3_RU8__strongKS5_EEENS9_INS_15__hash_iteratorIPNS_11__hash_nodeIS7_PvEEEEbEEDpOT_ENKUlRSA_OS3_SO_E_clESZ_S10_SO_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIP17_opaque_pthread_tNS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SC_SG_SE_EENS_9allocatorISC_EEE16__emplace_uniqueB9fqn220100IJRKNS_21piecewise_construct_tENS_5tupleIJOS3_EEENSR_IJOS7_EEEEEENSA_INS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEEbEEDpOT_ENKUlRSB_SQ_OST_OSV_E_clES16_SQ_S17_S18_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIPKvNS_6vectorINS_4pairIP13objc_selectorPFvP11objc_objectS7_EEENS_9allocatorISC_EEEEEENS_22__unordered_map_hasherIS3_NS5_IKS3_SF_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SJ_SN_SL_EENSD_ISJ_EEE16__emplace_uniqueB9fqn220100IJS3_SF_EEENS5_INS_15__hash_iteratorIPNS_11__hash_nodeISG_PvEEEEbEEDpOT_ENKUlRSI_OS3_OSF_E_clES14_S15_S16_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIPKvU8__strongP5NSSetIP10objc_classEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S9_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SE_SI_SG_EENS_9allocatorISE_EEE16__emplace_uniqueB9fqn220100IJS3_RS9_EEENSC_INS_15__hash_iteratorIPNS_11__hash_nodeISA_PvEEEEbEEDpOT_ENKUlRSD_OS3_SQ_E_clES11_S12_SQ_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIj12LSPluginDataEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS7_SB_S9_EENS_9allocatorIS7_EEE16__emplace_uniqueB9fqn220100IJNS5_IjS2_EEEEENS5_INS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEEDpOT_ENKUlRS6_OSJ_E_clESU_SV_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIj37LSApplicationRecordUpdateAvailabilityEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS7_SB_S9_EENS_9allocatorIS7_EEE16__emplace_uniqueB9fqn220100IJRjS2_EEENS5_INS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEEDpOT_ENKUlRS6_SJ_OS2_E_clESU_SJ_SV_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIj38_LSDatabaseTableVisualizationFunctionsEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS7_SB_S9_EENS_9allocatorIS7_EEE16__emplace_uniqueB9fqn220100IJRKNS_21piecewise_construct_tENS_5tupleIJOjEEENSM_IJEEEEEENS5_INS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEEDpOT_ENKUlRS6_SL_OSO_OSP_E_clES10_SL_S11_S12_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIj38_LSDatabaseTableVisualizationFunctionsEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS7_SB_S9_EENS_9allocatorIS7_EEE16__emplace_uniqueB9fqn220100IJRKNS_21piecewise_construct_tENS_5tupleIJRS6_EEENSM_IJEEEEEENS5_INS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEEDpOT_ENKUlSN_SL_OSO_OSP_E_clESN_SL_S10_S11_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_mapIjbNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjbEEEEEEEENS_22__unordered_map_hasherIjNS8_IS9_SC_EES4_S6_EENS_21__unordered_map_equalIjSF_S6_S4_EENS7_ISF_EEE16__emplace_uniqueB9fqn220100IJRKNS_21piecewise_construct_tENS_5tupleIJRS9_EEENSP_IJEEEEEENS8_INS_15__hash_iteratorIPNS_11__hash_nodeISD_PvEEEEbEEDpOT_ENKUlSQ_SO_OSR_OSS_E_clESQ_SO_S13_S14_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEENS_22__unordered_map_hasherIjNS_4pairIKjS9_EES4_S6_EENS_21__unordered_map_equalIjSE_S6_S4_EENS7_ISE_EEE16__emplace_uniqueB9fqn220100IJRKNS_21piecewise_construct_tENS_5tupleIJRSD_EEENSO_IJEEEEEENSC_INS_15__hash_iteratorIPNS_11__hash_nodeISA_PvEEEEbEEDpOT_ENKUlSP_SN_OSQ_OSR_E_clESP_SN_S12_S13_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP19LSApplicationRecordEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS9_SD_SB_EENS_9allocatorIS9_EEE16__emplace_uniqueB9fqn220100IJNS7_IjS4_EEEEENS7_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEEDpOT_ENKUlRS8_OSL_E_clESW_SX_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP8NSStringEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS9_SD_SB_EENS_9allocatorIS9_EEE16__emplace_uniqueB9fqn220100IJRKNS_21piecewise_construct_tENS_5tupleIJRS8_EEENSO_IJEEEEEENS7_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEEDpOT_ENKUlSP_SN_OSQ_OSR_E_clESP_SN_S12_S13_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIjbEENS_22__unordered_map_hasherIjNS_4pairIKjbEENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS6_SA_S8_EENS_9allocatorIS6_EEE16__emplace_uniqueB9fqn220100IJRKNS_21piecewise_construct_tENS_5tupleIJRS5_EEENSL_IJEEEEEENS4_INS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEEDpOT_ENKUlSM_SK_OSN_OSO_E_clESM_SK_SZ_S10_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjNS_4pairIKjjEENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS6_SA_S8_EENS_9allocatorIS6_EEE16__emplace_uniqueB9fqn220100IJRS5_RjEEENS4_INS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEEDpOT_ENKUlSI_SI_SJ_E_clESI_SI_SJ_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIyN14LaunchServices11OpenStaging20StagingDirectoryInfoEEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS9_SD_SB_EENS_9allocatorIS9_EEE16__emplace_uniqueB9fqn220100IJRS8_S4_EEENS7_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEEDpOT_ENKUlSL_SL_OS4_E_clESL_SL_SW_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIyN14LaunchServices11OpenStaging20StagingDirectoryInfoEEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS9_SD_SB_EENS_9allocatorIS9_EEE16__emplace_uniqueB9fqn220100IJRyS4_EEENS7_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEEDpOT_ENKUlRS8_SL_OS4_E_clESW_SL_SX_
+ __ZZNSt3__112__hash_tableIP13objc_selectorNS_4hashIS2_EENS_8equal_toIS2_EENS_9allocatorIS2_EEE16__emplace_uniqueB9fqn220100IJRKS2_EEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEEDpOT_ENKUlSC_SC_E_clESC_SC_
+ __ZZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEEN14LaunchServices19MallocZoneAllocatorIjNS5_17BindingEvaluation17BindingMallocZoneEEEE16__emplace_uniqueB9fqn220100IJRKjEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIjPvEEEEbEEDpOT_ENKUlSD_SD_E_clESD_SD_
+ __ZZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEE16__emplace_uniqueB9fqn220100IJRKjEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIjPvEEEEbEEDpOT_ENKUlSA_SA_E_clESA_SA_
+ __ZZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEE16__emplace_uniqueB9fqn220100IJRjEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIjPvEEEEbEEDpOT_ENKUlRKjS9_E_clESM_S9_
+ ___100-[LSApplicationWorkspace(PersonaNiceties) bundleIdentifiersForPersonaWithPersonaUniqueString:error:]_block_invoke
+ ___100-[LSApplicationWorkspace(PersonaNiceties) bundleIdentifiersForPersonaWithPersonaUniqueString:error:]_block_invoke_2
+ ___101-[_LSInstallProgressService createInstallProgressForApplication:withPhase:andPublishingString:reply:]_block_invoke.268
+ ___104-[LSApplicationWorkspace registerApplicationForRebuildWithInstallInfo:requestContext:registrationError:]_block_invoke
+ ___104-[LSApplicationWorkspace registerApplicationForRebuildWithInstallInfo:requestContext:registrationError:]_block_invoke_2
+ ___105-[LSExtensionLaunchConfigurationResolver bestLaunchPersonaForExtension:hostPersona:hostAuditToken:error:]_block_invoke
+ ___109-[LSApplicationRestrictionsManager _lazyLoadRestrictionsIdentifierSet:identifiersAreNullable:context:getter:]_block_invoke
+ ___109-[LSApplicationRestrictionsManager _lazyLoadRestrictionsIdentifierSet:identifiersAreNullable:context:getter:]_block_invoke.110
+ ___109-[LSApplicationRestrictionsManager _lazyLoadRestrictionsIdentifierSet:identifiersAreNullable:context:getter:]_block_invoke_2
+ ___109-[LSApplicationRestrictionsManager _lazyLoadRestrictionsIdentifierSet:identifiersAreNullable:context:getter:]_block_invoke_3
+ ___109-[LSApplicationRestrictionsManager _lazyLoadRestrictionsIdentifierSet:identifiersAreNullable:context:getter:]_block_invoke_3.cold.1
+ ___111-[_LSCanOpenURLManager(PrivateSchemeChecking) legacy_isBundleID:bundleData:context:allowedToCheckScheme:error:]_block_invoke.73
+ ___116-[LSApplicationWorkspace removeReferencesToPersonaWithUniqueString:operationUUID:requestContext:saveObserver:error:]_block_invoke
+ ___116-[LSApplicationWorkspace removeReferencesToPersonaWithUniqueString:operationUUID:requestContext:saveObserver:error:]_block_invoke_2
+ ___120-[_LSDDeviceIdentifierClient getClientProcessVendorNameBundleIdentifierAndRestrictedIDAccessWithType:completionHandler:]_block_invoke.54
+ ___121-[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:bundlePersonaRecordMap:operationUUID:reply:]_block_invoke
+ ___121-[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:bundlePersonaRecordMap:operationUUID:reply:]_block_invoke.297
+ ___121-[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:bundlePersonaRecordMap:operationUUID:reply:]_block_invoke.cold.1
+ ___127-[LSExtensionLaunchConfigurationClientSystemRegistrar fetchRegisteredConfigurationWithUUID:additionalConfigurationClass:error:]_block_invoke
+ ___127-[LSExtensionLaunchConfigurationClientSystemRegistrar fetchRegisteredConfigurationWithUUID:additionalConfigurationClass:error:]_block_invoke_2
+ ___127-[LSExtensionLaunchConfigurationClientSystemRegistrar fetchRegisteredConfigurationWithUUID:additionalConfigurationClass:error:]_block_invoke_2.cold.1
+ ___127-[LSExtensionLaunchConfigurationClientSystemRegistrar fetchRegisteredConfigurationWithUUID:additionalConfigurationClass:error:]_block_invoke_2.cold.2
+ ___134-[LSApplicationWorkspace registerContainerizedApplicationWithInstallInfo:operationUUID:requestContext:saveObserver:registrationError:]_block_invoke
+ ___134-[LSApplicationWorkspace registerContainerizedApplicationWithInstallInfo:operationUUID:requestContext:saveObserver:registrationError:]_block_invoke_2
+ ___149-[LSExtensionLaunchConfigurationClientSystemRegistrar registerLaunchConfiguration:forExtensionWithUUID:hostPersonaUniqueString:hostAuditToken:error:]_block_invoke
+ ___149-[LSExtensionLaunchConfigurationClientSystemRegistrar registerLaunchConfiguration:forExtensionWithUUID:hostPersonaUniqueString:hostAuditToken:error:]_block_invoke_2
+ ___157-[LSDServerExtensionLaunchConfigurationRegistrar registerTransmissibleLaunchConfiguration:forExtensionWithUUID:hostPersonaUniqueString:hostAuditToken:error:]_block_invoke
+ ___157-[LSDServerExtensionLaunchConfigurationRegistrar registerTransmissibleLaunchConfiguration:forExtensionWithUUID:hostPersonaUniqueString:hostAuditToken:error:]_block_invoke_2
+ ___158-[LSBundleProxy _initWithBundleUnit:context:bundleType:bundleID:localizedName:bundleContainerURL:resourcesDirectoryURL:iconsDictionary:iconFileNames:version:]_block_invoke
+ ___158-[_LSDModifyClient setContainersForApplicationsWithBundleIdentifiers:unbundledExtensionsWithBundleIdentifiers:fromBundlePersonaRecordMap:operationUUID:reply:]_block_invoke
+ ___158-[_LSDModifyClient setContainersForApplicationsWithBundleIdentifiers:unbundledExtensionsWithBundleIdentifiers:fromBundlePersonaRecordMap:operationUUID:reply:]_block_invoke.301
+ ___158-[_LSDModifyClient setContainersForApplicationsWithBundleIdentifiers:unbundledExtensionsWithBundleIdentifiers:fromBundlePersonaRecordMap:operationUUID:reply:]_block_invoke.cold.1
+ ___164-[LSApplicationWorkspace _setPersonaUniqueStrings:forApplicationsWithBundleIdentifiers:bundlePersonaRecordMapOrNil:operationUUID:requestContext:saveObserver:error:]_block_invoke
+ ___164-[LSApplicationWorkspace _setPersonaUniqueStrings:forApplicationsWithBundleIdentifiers:bundlePersonaRecordMapOrNil:operationUUID:requestContext:saveObserver:error:]_block_invoke_2
+ ___19-[LSWorkPipe drain]_block_invoke
+ ___192-[LSApplicationWorkspace setContainersForApplicationsWithBundleIdentifiers:unbundledExtensionsWithBundleIdentifiers:fromBundlePersonaRecordMap:operationUUID:requestContext:saveObserver:error:]_block_invoke
+ ___192-[LSApplicationWorkspace setContainersForApplicationsWithBundleIdentifiers:unbundledExtensionsWithBundleIdentifiers:fromBundlePersonaRecordMap:operationUUID:requestContext:saveObserver:error:]_block_invoke_2
+ ___23-[LSWorkPipe _runWork:]_block_invoke
+ ___24-[LSWorkPipe invalidate]_block_invoke
+ ___26-[LSWorkPipe enqueueWork:]_block_invoke
+ ___26-[LSWorkPipe enqueueWork:]_block_invoke_2
+ ___37-[LSSettingsStore addChangeObserver:]_block_invoke.40
+ ___38+[_LSEmptyContainerMap sharedInstance]_block_invoke
+ ___39-[LSInstallInfo extensionBundleRecords]_block_invoke
+ ___39-[_LSPersonaDatabase personasWithType:]_block_invoke
+ ___42-[LSDocumentProxy(Binding) _boundIconInfo]_block_invoke.157
+ ___42-[LSMIResultRegistrant runWithCompletion:]_block_invoke.85
+ ___43+[_LSEmptyGroupContainerMap sharedInstance]_block_invoke
+ ___44-[LSBundleRecord _cachedDataContainerURLMap]_block_invoke
+ ___44-[LSMIResultUnregistrant runWithCompletion:]_block_invoke.114
+ ___45-[LSApplicationWorkspace establishConnection]_block_invoke.176
+ ___45-[LSApplicationWorkspace establishConnection]_block_invoke.179
+ ___45-[LSApplicationWorkspace establishConnection]_block_invoke.184
+ ___45-[LSApplicationWorkspace establishConnection]_block_invoke.190
+ ___45-[LSApplicationWorkspace establishConnection]_block_invoke.196
+ ___45-[LSApplicationWorkspace establishConnection]_block_invoke_2.187
+ ___45-[LSBundleRecordUpdater parsePersonas:error:]_block_invoke.cold.1
+ ___46-[LSRebuildStatisticsGatherer submitAnalytics]_block_invoke.2
+ ___47-[LSBundleRecordBuilder buildBundleData:error:]_block_invoke.721
+ ___47-[LSByURLBundleUnregistrant runWithCompletion:]_block_invoke.132
+ ___47-[LSByURLPluginUnregistrant runWithCompletion:]_block_invoke.149
+ ___48+[UTTypeRecord typeRecordForPromiseAtURL:error:]_block_invoke
+ ___48+[UTTypeRecord typeRecordForPromiseAtURL:error:]_block_invoke_2
+ ___48-[LSDatabaseBuilder createAndSeedLocalDatabase:]_block_invoke.3
+ ___48-[LSDatabaseBuilder createAndSeedLocalDatabase:]_block_invoke.6
+ ___48-[LSDatabaseBuilder createAndSeedLocalDatabase:]_block_invoke_2
+ ___48-[LSDatabaseBuilder createAndSeedLocalDatabase:]_block_invoke_2.7
+ ___48-[LSDatabaseBuilder createAndSeedLocalDatabase:]_block_invoke_2.cold.1
+ ___48-[LSDatabaseBuilder createAndSeedLocalDatabase:]_block_invoke_3
+ ___48-[LSDatabaseBuilder seedCryptexContentIfNeeded:]_block_invoke_2
+ ___49+[LSExtensionLaunchConfiguration systemRegistrar]_block_invoke
+ ___49-[_LSDReadClient getPersonalPersonaUniqueString:]_block_invoke
+ ___50-[_LSDiskUsage(Private) fetchClientSideWithError:]_block_invoke.144
+ ___51-[LSApplicationWorkspace deviceIdentifierForVendor]_block_invoke.366
+ ___51-[LSApplicationWorkspace deviceIdentifierForVendor]_block_invoke.366.cold.1
+ ___52-[_LSInstallProgressService restoreInactiveInstalls]_block_invoke.216
+ ___52-[_LSInstallProgressService restoreInactiveInstalls]_block_invoke.216.cold.1
+ ___54-[_LSClientSettingsStore resetUserElectionsWithError:]_block_invoke.222
+ ___54-[_LSClientSettingsStore resetUserElectionsWithError:]_block_invoke.222.cold.1
+ ___54-[_LSClientSettingsStore userElectionForExtensionKey:]_block_invoke.219
+ ___54-[_LSClientSettingsStore userElectionForExtensionKey:]_block_invoke.219.cold.1
+ ___55-[LSApplicationWorkspace _LSPrivateNoteMigratorRunning]_block_invoke.392
+ ___55-[LSApplicationWorkspace _LSPrivateNoteMigratorRunning]_block_invoke.392.cold.1
+ ___55-[LSApplicationWorkspace scanForForDeletableSystemApps]_block_invoke.cold.1
+ ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.636
+ ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.636.cold.1
+ ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.637
+ ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.637.cold.1
+ ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.637.cold.2
+ ___56-[LSApplicationWorkspace deviceIdentifierForAdvertising]_block_invoke.363
+ ___56-[LSApplicationWorkspace deviceIdentifierForAdvertising]_block_invoke.363.cold.1
+ ___57-[LSBundleRecordUpdater removeReferencesToPersona:error:]_block_invoke
+ ___57-[LSBundleRecordUpdater removeReferencesToPersona:error:]_block_invoke_2
+ ___57-[LSBundleRecordUpdater removeReferencesToPersona:error:]_block_invoke_3
+ ___58-[LSApplicationRestrictionsManager _LSResolveIdentifiers:]_block_invoke
+ ___58-[LSApplicationRestrictionsManager _LSResolveIdentifiers:]_block_invoke.106
+ ___58-[LSApplicationRestrictionsManager _LSResolveIdentifiers:]_block_invoke.cold.1
+ ___58-[LSApplicationWorkspace scanForAppsWithIdentifiersInSet:]_block_invoke
+ ___58-[LSApplicationWorkspace scanForAppsWithIdentifiersInSet:]_block_invoke.cold.1
+ ___59-[LSBundleRecordUpdater parseBundlePersonaRecordMap:error:]_block_invoke
+ ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.302
+ ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.305
+ ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.308
+ ___59-[_LSXPCQueryResolver _resolveQueries:XPCConnection:error:]_block_invoke.136
+ ___59-[_LSXPCQueryResolver _resolveQueries:XPCConnection:error:]_block_invoke.136.cold.1
+ ___60+[LSDExtensionLaunchConfigurationStore sharedServerInstance]_block_invoke
+ ___60-[LSApplicationRestrictionsManager beginListeningForChanges]_block_invoke.125
+ ___61-[LSSystemExtensionPointRefreshRegistrant runWithCompletion:]_block_invoke.190
+ ___62-[LSDExtensionLaunchConfigurationStore _clearStorageDirectory]_block_invoke
+ ___62-[LSDExtensionLaunchConfigurationStore _clearStorageDirectory]_block_invoke.cold.1
+ ___64-[_LSClientSettingsStore setUserElection:forExtensionKey:error:]_block_invoke.221
+ ___64-[_LSClientSettingsStore setUserElection:forExtensionKey:error:]_block_invoke.221.cold.1
+ ___64-[_LSInstallProgressService loadJournalledNotificationsFromDisk]_block_invoke.344
+ ___65-[_LSClientSettingsStore __internalQueue_xpcConnectionWithError:]_block_invoke.216
+ ___65-[_LSClientSettingsStore __internalQueue_xpcConnectionWithError:]_block_invoke.216.cold.1
+ ___65-[_LSClientSettingsStore __internalQueue_xpcConnectionWithError:]_block_invoke.218
+ ___66-[LSApplicationWorkspace installProgressForApplication:withPhase:]_block_invoke.375
+ ___67-[ICLBundleRecord(LSTransitional) ls_associatedPersonasIfAvailable]_block_invoke
+ ___67-[LSApplicationRecord(UniqueIdentifiers) deviceIdentifierForVendor]_block_invoke.503
+ ___67-[LSApplicationRestrictionsManager restrictedBundleIDsWithContext:]_block_invoke
+ ___67-[LSApplicationWorkspace _LSServer_scanRestrictionAffectedBundles:]_block_invoke
+ ___67-[LSApplicationWorkspace _LSServer_scanRestrictionAffectedBundles:]_block_invoke.cold.1
+ ___67-[_LSDModifyClient registerBuiltinApplication:operationUUID:reply:]_block_invoke
+ ___68-[LSApplicationRestrictionsManager allowlistedBundleIDsWithContext:]_block_invoke
+ ___68-[LSApplicationRestrictionsManager handleMCEffectiveSettingsChanged]_block_invoke.133
+ ___68-[LSApplicationRestrictionsManager handleMCEffectiveSettingsChanged]_block_invoke.134
+ ___68-[LSApplicationWorkspace urlContainsDeviceIdentifierForAdvertising:]_block_invoke.367
+ ___68-[LSApplicationWorkspaceRemoteObserver applicationInstallsDidStart:]_block_invoke.758
+ ___69+[_LSDReadClient methodWithSelectorGetsImplicitExecutionContextRead:]_block_invoke
+ ___69-[LSApplicationWorkspace installProgressForBundleID:makeSynchronous:]_block_invoke.370
+ ___69-[LSApplicationWorkspace installProgressForBundleID:makeSynchronous:]_block_invoke.371
+ ___69-[LSApplicationWorkspace installProgressForBundleID:makeSynchronous:]_block_invoke.372
+ ___70+[LSDServerExtensionLaunchConfigurationRegistrar sharedServerInstance]_block_invoke
+ ___71-[LSBundlePersonaRecordMap addBundlePersonaRecordsForICLBundleRecords:]_block_invoke
+ ___72-[LSApplicationRecord(UniqueIdentifiers) deviceIdentifierForAdvertising]_block_invoke.505
+ ___73-[LSApplicationRestrictionsManager _pruneObsoleteTrustedSignerIdentities]_block_invoke.135
+ ___73-[LSContainerCache cacheAndSetDataContainersForApplicationRecords:error:]_block_invoke
+ ___74-[LSContainerCache _processInDatabaseAppDataContainersWithContext:locked:]_block_invoke
+ ___74-[UTTypeRecord _enumerateRelatedTypesWithMaximumDegreeOfSeparation:block:]_block_invoke.32
+ ___74-[UTTypeRecord _enumerateRelatedTypesWithMaximumDegreeOfSeparation:block:]_block_invoke.32.cold.1
+ ___75-[LSBundleRecord(Personas) personaOrPrimaryPersonaPlaceholderIsApplicable:]_block_invoke
+ ___75-[LSContainerCache _setDataContainersOnApplicationRecordsFromCache:locked:]_block_invoke
+ ___75-[LSContainerCache _setDataContainersOnApplicationRecordsFromCache:locked:]_block_invoke_2
+ ___75-[_LSDModifyClient unregisterApplicationsAtMountPoint:operationUUID:reply:]_block_invoke.255
+ ___75-[_LSDModifyClient unregisterApplicationsAtMountPoint:operationUUID:reply:]_block_invoke.260
+ ___76-[LSApplicationRestrictionsManager ratingRankExceptionBundleIDsWithContext:]_block_invoke
+ ___76-[_LSDModifyClient performPostInstallationRegistration:operationUUID:reply:]_block_invoke
+ ___76-[_LSDModifyClient performPostInstallationRegistration:operationUUID:reply:]_block_invoke_2
+ ___76-[_LSInstallProgressService addSendNotificationFenceWithTimeout:fenceBlock:]_block_invoke.339
+ ___78-[LSApplicationRecord(AlternateIcons) setAlternateIconName:completionHandler:]_block_invoke.627
+ ___78-[LSApplicationRecord(AlternateIcons) setAlternateIconName:completionHandler:]_block_invoke.627.cold.1
+ ___79-[_LSDefaults sandboxExtensionForCreatedDiagnosticsStashDirectoryURLWithError:]_block_invoke
+ ___79-[_LSDefaults sandboxExtensionForCreatedDiagnosticsStashDirectoryURLWithError:]_block_invoke.cold.1
+ ___79-[_LSInstallProgressService sendNotification:forAppProxies:Plugins:completion:]_block_invoke.324
+ ___82-[_LSDModifyClient removeReferencesToPersonaWithUniqueString:operationUUID:reply:]_block_invoke
+ ___82-[_LSDModifyClient removeReferencesToPersonaWithUniqueString:operationUUID:reply:]_block_invoke.299
+ ___83-[LSApplicationRestrictionsManager parentalControlsRestrictedBundleIDsWithContext:]_block_invoke
+ ___83-[LSApplicationWorkspace scanForApplicationStateChangesFromRank:toRank:exceptions:]_block_invoke.cold.1
+ ___84-[_LSDModifyClient setPreferenceValue:forKey:forApplicationAtURL:completionHandler:]_block_invoke.288
+ ___86-[LSApplicationRecord(AlternateIcons) setAlternateIconNameSilently:completionHandler:]_block_invoke.634
+ ___86-[LSApplicationRecord(AlternateIcons) setAlternateIconNameSilently:completionHandler:]_block_invoke.634.cold.1
+ ___86-[LSApplicationWorkspace(PersonaNiceties) bundleIdentifiersForPersonasWithType:error:]_block_invoke
+ ___86-[LSApplicationWorkspace(PersonaNiceties) bundleIdentifiersForPersonasWithType:error:]_block_invoke_2
+ ___87-[LSContainerCache _cacheAndSetDataContainersForContainerizedCachableAppRecords:error:]_block_invoke
+ ___88-[LSApplicationRestrictionsManager _rawPartnerFinancingAllowlistedBundleIDsWithContext:]_block_invoke
+ ___88-[LSApplicationWorkspace _LSServer_scanRestrictionAffectedBundlesWithContext:scanBlock:]_block_invoke
+ ___89-[LSApplicationRestrictionsManager scanForMissedNotificationsForImportantAppsIfNecessary]_block_invoke.124
+ ___93-[LSDServerExtensionLaunchConfigurationRegistrar fetchRegisteredConfigurationWithUUID:error:]_block_invoke
+ ___94+[LSDocumentProxy(Binding) _bindingEvaluatorResultFilterForContentIsManaged:sourceAuditToken:]_block_invoke
+ ___94+[LSDocumentProxy(Binding) _bindingEvaluatorResultFilterForContentIsManaged:sourceAuditToken:]_block_invoke.138
+ ___94+[LSDocumentProxy(Binding) _bindingEvaluatorResultFilterForContentIsManaged:sourceAuditToken:]_block_invoke.140
+ ___95-[LSApplicationWorkspace _LSPrivateRebuildApplicationDatabasesForSystemApps:internal:user:uid:]_block_invoke.387
+ ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.307
+ ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.307.cold.1
+ ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.308
+ ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.308.cold.1
+ ___98-[_LSDModifyClient registerItemInfo:alias:diskImageAlias:bundleURL:installInfo:completionHandler:]_block_invoke
+ ___98-[_LSDModifyClient registerItemInfo:alias:diskImageAlias:bundleURL:installInfo:completionHandler:]_block_invoke.174
+ ___Block_byref_object_copy_.1013
+ ___Block_byref_object_copy_.106
+ ___Block_byref_object_copy_.109
+ ___Block_byref_object_copy_.1191
+ ___Block_byref_object_copy_.129
+ ___Block_byref_object_copy_.141
+ ___Block_byref_object_copy_.163
+ ___Block_byref_object_copy_.168
+ ___Block_byref_object_copy_.171
+ ___Block_byref_object_copy_.24
+ ___Block_byref_object_copy_.259
+ ___Block_byref_object_copy_.267
+ ___Block_byref_object_copy_.337
+ ___Block_byref_object_copy_.363
+ ___Block_byref_object_copy_.682
+ ___Block_byref_object_dispose_.1014
+ ___Block_byref_object_dispose_.107
+ ___Block_byref_object_dispose_.110
+ ___Block_byref_object_dispose_.1192
+ ___Block_byref_object_dispose_.130
+ ___Block_byref_object_dispose_.142
+ ___Block_byref_object_dispose_.164
+ ___Block_byref_object_dispose_.169
+ ___Block_byref_object_dispose_.172
+ ___Block_byref_object_dispose_.25
+ ___Block_byref_object_dispose_.260
+ ___Block_byref_object_dispose_.268
+ ___Block_byref_object_dispose_.338
+ ___Block_byref_object_dispose_.364
+ ___Block_byref_object_dispose_.683
+ ___MDTCopierFinalize.cold.1
+ ___MDTCopierFinalize.cold.2
+ ____LSBundleCopyPersonasWithAttributes_block_invoke
+ ____LSContainerLog_block_invoke
+ ____LSCopyContainerQueryPersonaForCurrentPersonaAndBundlePersonas_block_invoke
+ ____LSCopyGroupContainerIdentifiersXPCObjectFromEntitlements_block_invoke
+ ____LSCopyGroupContainerURLSFromContainermanagerForPersona_block_invoke
+ ____LSCopySystemContentDatabaseToDiagnosticsStash_block_invoke
+ ____LSCopySystemContentDatabaseToDiagnosticsStash_block_invoke.cold.1
+ ____LSCopySystemContentDatabaseToDiagnosticsStash_block_invoke.cold.2
+ ____LSCopySystemContentDatabaseToDiagnosticsStash_block_invoke.cold.3
+ ____LSCopySystemContentDatabaseToDiagnosticsStash_block_invoke.cold.4
+ ____LSCopySystemContentDatabaseToDiagnosticsStash_block_invoke.cold.5
+ ____LSCopySystemContentDatabaseToDiagnosticsStash_block_invoke.cold.6
+ ____LSCriticalErrorLog_block_invoke
+ ____LSDatabaseGetSeedingWorkloop_block_invoke
+ ____LSDatabaseScheduleAfterSeeding_block_invoke
+ ____LSDatabaseWaitForSeeding_block_invoke
+ ____LSDatabaseWaitForSeeding_block_invoke.cold.1
+ ____LSEntryPointLog_block_invoke
+ ____LSGetPersonalPersonaUniqueString_block_invoke
+ ____LSGetPersonalPersonaUniqueString_block_invoke_2
+ ____LSPersonaListHasSystemPersona_block_invoke
+ ____LSResetServer_block_invoke.130
+ ____LSResetServer_block_invoke.130.cold.1
+ ____LSServer_CleanSystemContentDatabaseForMainDatabaseUse_block_invoke
+ ____LSServer_CleanSystemContentDatabaseForMainDatabaseUse_block_invoke.957
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.945
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.949
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.949.cold.1
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.949.cold.2
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.952.cold.1
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.954
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.955
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.947
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.953
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.cold.3
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.cold.4
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_3
+ ____LSServer_PerformExternalRebuildRegistration_block_invoke
+ ____LSServer_PerformOpenOperation_block_invoke_3.cold.4
+ ____LSServer_RebuildApplicationDatabases_block_invoke_5
+ ____LSServer_RefreshContentInFrameworkAtURL_block_invoke.115
+ ____LSServer_SyncWithMobileInstallation_block_invoke.1015
+ ____LSServer_SyncWithMobileInstallation_block_invoke.1016
+ ____LSServer_SyncWithMobileInstallation_block_invoke_2.1017
+ ____LSServer_SyncWithMobileInstallation_block_invoke_2.1017.cold.1
+ ____LSServer_SyncWithMobileInstallation_block_invoke_2.1017.cold.2
+ ____LSServer_SyncWithMobileInstallation_block_invoke_2.cold.1
+ ____LSUnregisterBundle_block_invoke.154
+ ____ZL16getPropertyTablev_block_invoke.cold.12
+ ____ZL17_LSRegisterPluginP11_LSDatabaseP13LSInstallInfoRK12LSPluginInfoPK14__CFDictionaryPK10__CFStringSB_S8_jPj_block_invoke
+ ____ZL23_LSOpenOperationPerformP5NSURLP12NSFileHandleP8NSStringbS4_P12NSDictionaryIS4_P11objc_objectES9_PU42objcproto31LSOpenResourceOperationDelegate11objc_objectP15NSXPCConnectionU13block_pointerFvbP7NSErrorE_block_invoke.114
+ ____ZL23_LSOpenOperationPerformP5NSURLP12NSFileHandleP8NSStringbS4_P12NSDictionaryIS4_P11objc_objectES9_PU42objcproto31LSOpenResourceOperationDelegate11objc_objectP15NSXPCConnectionU13block_pointerFvbP7NSErrorE_block_invoke.115.cold.1
+ ____ZL23_LSOpenOperationPerformP5NSURLP12NSFileHandleP8NSStringbS4_P12NSDictionaryIS4_P11objc_objectES9_PU42objcproto31LSOpenResourceOperationDelegate11objc_objectP15NSXPCConnectionU13block_pointerFvbP7NSErrorE_block_invoke.117
+ ____ZL23_LSUpdateDefaultHandlerP18LSApplicationProxyP5NSURL_block_invoke.151
+ ____ZL23_LSUpdateDefaultHandlerP18LSApplicationProxyP5NSURL_block_invoke.151.cold.1
+ ____ZL25_LSPluginRegisterWithInfoP11_LSDatabasePK14__CFDictionaryPK10__CFStringP13LSInstallInfoPS1_jj_block_invoke
+ ____ZL25_LSPluginRegisterWithInfoP11_LSDatabasePK14__CFDictionaryPK10__CFStringP13LSInstallInfoPS1_jj_block_invoke_2
+ ____ZL25getAppsReferencingPersonaP9LSContextP8NSString_block_invoke
+ ____ZL25getAppsReferencingPersonaP9LSContextP8NSString_block_invoke_2
+ ____ZL26_LSArmSaveTimerWithTimeouthdU13block_pointerFvbP11_LSDatabaseP7NSErrorE_block_invoke.391
+ ____ZL28validateBundlePersonaRemovalP9LSContextjP8NSStringPU15__autoreleasingP7NSError_block_invoke
+ ____ZL29pluginKitUserElectionStoreURLv_block_invoke.252
+ ____ZL29pluginKitUserElectionStoreURLv_block_invoke.252.cold.1
+ ____ZL29pluginKitUserElectionStoreURLv_block_invoke.252.cold.2
+ ____ZL29pluginKitUserElectionStoreURLv_block_invoke.cold.2
+ ____ZL29pluginKitUserElectionStoreURLv_block_invoke.cold.3
+ ____ZL34LSCheckDatabaseAvailableWithServerP17_LSDServiceDomain_block_invoke.378
+ ____ZL34_LSCreateRegistrationDataForBundleP9LSContextP18LSRegistrationInfoPK7__CFURLP13LSInstallInfoPPK9__CFArray_block_invoke
+ ____ZL35_LSDyldSaysCPUTypeSubtypeIsRunnableii_block_invoke
+ ____ZL35_LSDyldSaysCPUTypeSubtypeIsRunnableii_block_invoke_2
+ ____ZL35enumerateProductPlatformKeySuffixesIU8__strongP12NSDictionaryIP8NSStringP11objc_objectEZ53-[_LSStringsFileContent subscriptLoctableWithLocale:]E3$_2ENSt3__18optionalIT_EES2_RKT0__block_invoke
+ ____ZL35enumerateProductPlatformKeySuffixesIU8__strongP8NSStringZ60-[_LSStringsFileContent _queryLoadedPlist:forRawKey:locale:]E3$_3ENSt3__18optionalIT_EES1_RKT0__block_invoke
+ ____ZL38getStandalonePluginsReferencingPersonaP9LSContextP8NSString_block_invoke
+ ____ZL45_processAppDataContainersFromContainermanagerINSt3__111__wrap_iterIPU8__strongKP8NSStringEEEbNS0_8optionalIN14LaunchServices14ContainerCache18PersonaAndPlatformEEET_SC_RNS0_13unordered_mapISA_U8__strongP19NSMutableDictionaryIS3_P5NSURLENS9_22PersonaAndPlatformHashENS0_8equal_toISA_EENS0_9allocatorINS0_4pairIKSA_SJ_EEEEEEPU15__autoreleasingP7NSError_block_invoke
+ ____ZL45_processAppDataContainersFromContainermanagerINSt3__111__wrap_iterIPU8__strongP8NSStringEEEbNS0_8optionalIN14LaunchServices14ContainerCache18PersonaAndPlatformEEET_SC_RNS0_13unordered_mapISA_U8__strongP19NSMutableDictionaryIS3_P5NSURLENS9_22PersonaAndPlatformHashENS0_8equal_toISA_EENS0_9allocatorINS0_4pairIKSA_SJ_EEEEEEPU15__autoreleasingP7NSError_block_invoke
+ ____ZL45_processAppDataContainersFromContainermanagerIPP8NSStringEbNSt3__18optionalIN14LaunchServices14ContainerCache18PersonaAndPlatformEEET_SA_RNS4_13unordered_mapIS8_U8__strongP19NSMutableDictionaryIS1_P5NSURLENS7_22PersonaAndPlatformHashENS4_8equal_toIS8_EENS4_9allocatorINS4_4pairIKS8_SH_EEEEEEPU15__autoreleasingP7NSError_block_invoke
+ ____ZL54sendPersonaChangedNotificationsForAppBundleIdentifiersP9LSContextP5NSSetIP8NSStringE_block_invoke
+ ____ZL78_LSGetDefaultPreferredLocalizationsWithFallbackForImproperlyLocalizedProcessesv_block_invoke.42
+ ____ZN14LaunchServices10BaseBundle20DataContainerContext5Paths6createEP11_LSDatabaseP12NSDictionaryIP8NSStringP5NSURLE_block_invoke
+ ____ZN14LaunchServices10BaseBundle28DataContainerWritableContext41createAndAssignFromBundlePersonaRecordMapEP11_LSDatabaseP12NSDictionaryIP8NSStringP22ICLBundlePersonaRecordEPU15__autoreleasingP7NSError_block_invoke
+ ____ZN14LaunchServices10BaseBundle29GroupContainerWritableContext27pathifyGroupContainerURLMapEP12NSDictionaryIP8NSStringP5NSURLE_block_invoke
+ ____ZN14LaunchServices10BaseBundle29GroupContainerWritableContext27pathifyGroupContainerURLMapEP12NSDictionaryIP8NSStringP5NSURLE_block_invoke.cold.1
+ ____ZN14LaunchServices10BaseBundle29GroupContainerWritableContext41createAndAssignFromBundlePersonaRecordMapEP11_LSDatabaseP12NSDictionaryIP8NSStringP22ICLBundlePersonaRecordEPU15__autoreleasingP7NSError_block_invoke
+ ____ZN14LaunchServices10BaseBundle32_LSUpdateDataContainersForBundleEP11_LSDatabaseP16LSBundleBaseDataP24LSBundlePersonaRecordMapRNSt3__16vectorINS0_35BundleDataContainerReleaseOperationENS7_9allocatorIS9_EEEERNS8_IjNSA_IjEEEE_block_invoke
+ ____ZN14LaunchServices10BaseBundle32_LSUpdateDataContainersForBundleEP11_LSDatabaseP16LSBundleBaseDataP24LSBundlePersonaRecordMapRNSt3__16vectorINS0_35BundleDataContainerReleaseOperationENS7_9allocatorIS9_EEEERNS8_IjNSA_IjEEEE_block_invoke_2
+ ____ZN14LaunchServices10BaseBundle32_LSUpdateDataContainersForBundleEP11_LSDatabaseP16LSBundleBaseDataP24LSBundlePersonaRecordMapRNSt3__16vectorINS0_35BundleDataContainerReleaseOperationENS7_9allocatorIS9_EEEERNS8_IjNSA_IjEEEE_block_invoke_2.cold.1
+ ____ZN14LaunchServices12HandlerPrefsL7displayEP9LSContextjjP29CSStoreAttributedStringWriter_block_invoke
+ ____ZN14LaunchServices12URLOverridesL20getURLOverrideCommonEP5NSURL_block_invoke.232
+ ____ZN14LaunchServices12URLOverridesL20getURLOverrideCommonEP5NSURL_block_invoke.232.cold.1
+ ____ZN14LaunchServices12URLOverridesL20getURLOverrideCommonEP5NSURL_block_invoke.232.cold.2
+ ____ZN14LaunchServices19URLPropertyProviderL43beginTranslatingHiddenBySystemNotificationsEv_block_invoke.72
+ ____ZN14LaunchServices19URLPropertyProviderL43beginTranslatingHiddenBySystemNotificationsEv_block_invoke.78
+ ____ZN26CachedRepresentedBundleMap14mapFromContextEP9LSContext_block_invoke
+ ____ZNK14LaunchServices10BaseBundle20DataContainerContext5Paths17enumerateResolvedIU8__strongU13block_pointerFvP8NSStringS5_PhEEEvP11_LSDatabaseRKT__block_invoke
+ ____ZNK14LaunchServices10BaseBundle20DataContainerContext5Paths17enumerateResolvedIZNS0_28DataContainerWritableContext13removePersonaEP11_LSDatabaseP8NSStringEUlS8_S8_PhE_EEvS6_RKT__block_invoke
+ ____ZNK14LaunchServices10BaseBundle20DataContainerContext5Paths17enumerateResolvedIZZ149-[LSContainerCache _processInDatabaseAppDataContainerWithContext:bundleUnitID:bundleDataIfAvailable:missingContainerMapForNonDatabaseRecords:locked:]ENK3$_2clIS2_EEDaRKT_EUlP8NSStringSB_PhE_EEvP11_LSDatabaseS9__block_invoke
+ ____ZZ31-[LSRecord compatibilityObject]ENK3$_1clEP9LSContextjjPKv_block_invoke
+ ____ZZ33_LSBundleBaseDataWriteDescriptionENK3$_0clIN14LaunchServices10BaseBundle20DataContainerContext5PathsEEEDaRKT__block_invoke
+ ____ZZ68+[LSBundleDataContainerMap containerMapWithDatabase:bundleBaseData:]ENK3$_1clIN14LaunchServices10BaseBundle20DataContainerContext5PathsEEEDaRKT__block_invoke
+ ____getBlockToUpdateBundleRecordFromMIAndNotifyIfChanged_block_invoke.cold.1
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_32_e13_v24?0r*8^B16l
+ ___block_descriptor_32_e25_B16?0"ICLBundleRecord"8l
+ ___block_descriptor_32_e383_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20l
+ ___block_descriptor_32_e41_B32?0"_LSPersonaWithAttributes"8Q16^B24l
+ ___block_descriptor_32_e51_v32?0"NSNumber"8"_LSLocalizedStringRecord"16^B24l
+ ___block_descriptor_32_e63_q24?0"_LSPersonaWithAttributes"8"_LSPersonaWithAttributes"16l
+ ___block_descriptor_32_e92_v32?0"FBSDisplayLayoutMonitor"8"FBSDisplayLayout"16"FBSDisplayLayoutTransitionContext"24l
+ ___block_descriptor_40_e34_v32?0"NSString"8"NSString"16*24ls32l8
+ ___block_descriptor_40_e8_32bs_e42_v24?0"LSDBExecutionContext"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e29_B16?0^{container_object_s=}8ls32l8
+ ___block_descriptor_40_ea8_32r_e30_v24?0"NSString"8"NSError"16lr32l8
+ ___block_descriptor_40_ea8_32s_e31_"LSBundleDataContainerMap"8?0ls32l8
+ ___block_descriptor_40_ea8_32s_e32_v32?0"NSString"8"NSURL"16^B24ls32l8
+ ___block_descriptor_40_ea8_32s_e34_v32?0"NSString"8"NSString"16*24ls32l8
+ ___block_descriptor_40_ea8_32s_e383_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20ls32l8
+ ___block_descriptor_40_ea8_32s_e383_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20ls32l8
+ ___block_descriptor_40_ea8_32s_e49_v32?0"NSString"8"ICLBundlePersonaRecord"16^B24ls32l8
+ ___block_descriptor_44_e383_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20l
+ ___block_descriptor_48_e8_32bs40bs_e12_"NSSet"8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32bs40r_e42_v24?0"LSDBExecutionContext"8"NSError"16lr40l8s32l8
+ ___block_descriptor_48_e8_32bs_e19_v32?0I8r^v12I20*24ls32l8
+ ___block_descriptor_48_e8_32r40r_e28_v24?0"NSUUID"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32r_e14_v24?0I8I12*16lr32l8
+ ___block_descriptor_48_e8_32s40s_e383_v28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e49_v32?0"NSString"8"ICLBundlePersonaRecord"16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_ea8_32bs_e196_v28?0"NSString"8I16r^{LSPluginData={LSBundleBaseData=IIIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20ls32l8
+ ___block_descriptor_48_ea8_32bs_e380_v28?0"NSString"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20ls32l8
+ ___block_descriptor_48_ea8_32r40r_e34_v24?0"UTTypeRecord"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_ea8_32s40bs_e41_v32?0"_LSPersonaWithAttributes"8Q16^B24ls40l8s32l8
+ ___block_descriptor_48_ea8_32s40s_e49_v32?0"NSString"8"ICLBundlePersonaRecord"16^B24ls32l8s40l8
+ ___block_descriptor_48_ea8_32s_e19_v32?0I8r^v12I20*24ls32l8
+ ___block_descriptor_48_ea8_32s_e41_B32?0"_LSPersonaWithAttributes"8Q16^B24ls32l8
+ ___block_descriptor_48_ea8_32s_e51_v32?0"NSString"8"_LSPersonaWithAttributes"16^B24ls32l8
+ ___block_descriptor_49_e8_32s40bs_e28_"NSSet"16?0^{LSContext=}8ls40l8s32l8
+ ___block_descriptor_52_e8_32s40n6_8_8_s0_e19_v32?0I8r^v12I20*24l
+ ___block_descriptor_52_e8_32s40n6_8_8_s0_e383_v28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20l
+ ___block_descriptor_52_ea8_32s_e370_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}12*20ls32l8
+ ___block_descriptor_56_e8_32bs40r48r_e37_v24?0"ICLBundleRecord"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s48n6_8_8_s0_e19_v32?0I8r^v12I20*24l
+ ___block_descriptor_56_ea8_32bs40bs_e370_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}12*20ls32l8s40l8
+ ___block_descriptor_56_ea8_32r40r_e370_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}12*20lr32l8r40l8
+ ___block_descriptor_56_ea8_32s40bs_e370_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}12*20ls32l8s40l8
+ ___block_descriptor_56_ea8_32s40r48r_e42_v24?0"LSDBExecutionContext"8"NSError"16ls32l8r40l8r48l8
+ ___block_descriptor_56_ea8_32s40r_e19_v32?0I8r^v12I20*24ls32l8r40l8
+ ___block_descriptor_56_ea8_32s40s_e30_v24?0{PersonaAndPlatform=I}8ls32l8s40l8
+ ___block_descriptor_56_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_57_e8_32s40bs_e52_"NSObject<NSCoding><NSCopying><NSSecureCoding>"8?0ls40l8s32l8
+ ___block_descriptor_58_e8_32s40r48r_e5_v8?0lr40l8r48l8s32l8
+ ___block_descriptor_60_e8_32s40n6_8_8_s0_e14_v24?0I8I12*16l
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_ea8_32s40r_e19_v32?0I8r^v12I20*24lr40l8s32l8
+ ___block_descriptor_64_ea8_32s40r_e19_v32?0I8r^v12I20*24ls32l8r40l8
+ ___block_descriptor_64_ea8_32s40s48r56r_e42_v24?0"LSDBExecutionContext"8"NSError"16ls32l8s40l8r48l8r56l8
+ ___block_descriptor_64_ea8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
+ ___block_descriptor_64_ea8_32s40s48s56r_e14_v24?0I8I12*16ls32l8s40l8r56l8s48l8
+ ___block_descriptor_67_ea8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32bs40r48r_e370_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}12*20ls32l8r40l8r48l8
+ ___block_descriptor_72_e8_32s40r48r_e65_v24?0"LSTransmissibleExtensionLaunchConfiguration"8"NSError"16lr40l8s32l8u64l8r48l8
+ ___block_descriptor_72_ea8_32r40c77_ZTSNSt3__18optionalIN14LaunchServices14ContainerCache18PersonaAndPlatformEEE_e29_B16?0^{container_object_s=}8l
+ ___block_descriptor_72_ea8_32s40r48r_e32_v32?0"NSString"8"NSURL"16^B24ls32l8r40l8r48l8
+ ___block_descriptor_72_ea8_32s40s48r_e370_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}12*20ls32l8s40l8r48l8
+ ___block_descriptor_72_ea8_32s40s48s56r64r_e48_v16?0"<LSRegistrantDatabaseContextProviding>"8lr56l8s32l8s40l8r64l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64n6_8_8_s0_e383_v28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20l
+ ___block_descriptor_80_ea8_32s40s48s56s64bs72r_e48_v16?0"<LSRegistrantDatabaseContextProviding>"8lr72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64r72r_e42_v24?0"LSDBExecutionContext"8"NSError"16lr64l8s32l8s40l8s48l8s56l8r72l8
+ ___block_descriptor_88_e8_32s40s48s56s64r72r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8r72l8
+ ___block_descriptor_88_ea8_32s40s48s56s64s72r80r_e42_v24?0"LSDBExecutionContext"8"NSError"16ls32l8s40l8s48l8s56l8s64l8r72l8r80l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72r80r88r_e42_v24?0"LSDBExecutionContext"8"NSError"16lr72l8s32l8s40l8s48l8s56l8s64l8r80l8r88l8
+ ___block_descriptor_99_ea8_32s40s48s56s64s72s80s88bs_e48_v16?0"<LSRegistrantDatabaseContextProviding>"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_literal_global.1092
+ ___block_literal_global.110
+ ___block_literal_global.1115
+ ___block_literal_global.1138
+ ___block_literal_global.1141
+ ___block_literal_global.115
+ ___block_literal_global.117
+ ___block_literal_global.1176
+ ___block_literal_global.119
+ ___block_literal_global.125
+ ___block_literal_global.133
+ ___block_literal_global.139
+ ___block_literal_global.140
+ ___block_literal_global.145
+ ___block_literal_global.150
+ ___block_literal_global.161
+ ___block_literal_global.163
+ ___block_literal_global.165
+ ___block_literal_global.168
+ ___block_literal_global.17
+ ___block_literal_global.170
+ ___block_literal_global.178
+ ___block_literal_global.183
+ ___block_literal_global.186
+ ___block_literal_global.189
+ ___block_literal_global.20
+ ___block_literal_global.201
+ ___block_literal_global.203
+ ___block_literal_global.204
+ ___block_literal_global.206
+ ___block_literal_global.209
+ ___block_literal_global.213
+ ___block_literal_global.219
+ ___block_literal_global.229
+ ___block_literal_global.231
+ ___block_literal_global.235
+ ___block_literal_global.236
+ ___block_literal_global.237
+ ___block_literal_global.239
+ ___block_literal_global.242
+ ___block_literal_global.244
+ ___block_literal_global.245
+ ___block_literal_global.249
+ ___block_literal_global.252
+ ___block_literal_global.254
+ ___block_literal_global.262
+ ___block_literal_global.264
+ ___block_literal_global.266
+ ___block_literal_global.274
+ ___block_literal_global.280
+ ___block_literal_global.297
+ ___block_literal_global.30
+ ___block_literal_global.304
+ ___block_literal_global.307
+ ___block_literal_global.315
+ ___block_literal_global.328
+ ___block_literal_global.343
+ ___block_literal_global.347
+ ___block_literal_global.36
+ ___block_literal_global.377
+ ___block_literal_global.383
+ ___block_literal_global.385
+ ___block_literal_global.386
+ ___block_literal_global.394
+ ___block_literal_global.414
+ ___block_literal_global.416
+ ___block_literal_global.427
+ ___block_literal_global.464
+ ___block_literal_global.478
+ ___block_literal_global.496
+ ___block_literal_global.497
+ ___block_literal_global.500
+ ___block_literal_global.502
+ ___block_literal_global.548
+ ___block_literal_global.555
+ ___block_literal_global.556
+ ___block_literal_global.569
+ ___block_literal_global.61
+ ___block_literal_global.624
+ ___block_literal_global.63
+ ___block_literal_global.642
+ ___block_literal_global.657
+ ___block_literal_global.66
+ ___block_literal_global.674
+ ___block_literal_global.73
+ ___block_literal_global.80
+ ___block_literal_global.89
+ ___block_literal_global.951
+ ___block_literal_global.959
+ ___block_literal_global.989
+ ___copy_helper_block_e8_48n6_8_8_s0
+ ___copy_helper_block_e8_64n6_8_8_s0
+ ___copy_helper_block_ea8_40c77_ZTSNSt3__18optionalIN14LaunchServices14ContainerCache18PersonaAndPlatformEEE
+ ___destroy_helper_block_e8_48n4_8_s0
+ ___destroy_helper_block_e8_64n4_8_s0
+ ___destroy_helper_block_ea8_40c77_ZTSNSt3__18optionalIN14LaunchServices14ContainerCache18PersonaAndPlatformEEE
+ ___mdt_client_log_block_invoke
+ ___registerForRebuildWithRepresentativeBundleAndInstallInfo_block_invoke
+ ___registerForRebuildWithRepresentativeBundleAndInstallInfo_block_invoke.cold.1
+ __dyld_lazy_load
+ __kLSURLApplicationBinaryCompatibilityLocalizedWarningKey
+ __os_signpost_emit_with_name_impl
+ __registerMIPluginWithInstallInfo
+ __registerMIPluginWithInstallInfo.cold.1
+ __xpc_type_error
+ _arc4random_buf
+ _container_error_get_type
+ _container_get_identifier
+ _container_query_iterate_results_sync
+ _container_query_operation_set_platform
+ _container_query_set_identifiers
+ _container_query_set_include_other_owners
+ _container_query_set_transient
+ _dispatch_async_and_wait
+ _dispatch_workloop_create
+ _dlopenHelper$MSUDataAccessor
+ _dlopenHelperFlag$MSUDataAccessor
+ _ffsctl
+ _initMobileInstallationEnumerateAllInstalledItemBundleRecords
+ _kLSBetaAppEntitlement
+ _kLSDefinesExtensionPointEntitlement
+ _kLSExtensionCrossPersonaLaunchEntitlement
+ _kLSExtensionRunInAnyPersonaEntitlement
+ _kLSExtensionRunInSystemPersonaEntitlement
+ _kLSGameCenterEnabledEntitlement
+ _kLSIsEligibilityCheckedBrowserEngineEmbedderEntitlement
+ _kLSIsEligibilityCheckedBrowserEntitlement
+ _kLSMediaCastingEntitlement
+ _kLSRepresentedBundleIDEntitlement
+ _lazyLoadFlag$FileProvider
+ _ls_associatedPersonasIfAvailable.onceToken
+ _ls_associatedPersonasIfAvailable.responds
+ _macho_arch_name_for_cpu_type
+ _macho_for_each_runnable_arch_name
+ _mdt_client_log.log
+ _mdt_client_log.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_LSServer_scanRestrictionAffectedBundles:
+ _objc_msgSend$_LSServer_scanRestrictionAffectedBundlesWithContext:scanBlock:
+ _objc_msgSend$_LS_frameworkFileManager
+ _objc_msgSend$_bindingEvaluatorResultFilterForContentIsManaged:sourceAuditToken:
+ _objc_msgSend$_bootInfoFileURL
+ _objc_msgSend$_bundleDataContainerMapFromDatabase
+ _objc_msgSend$_cacheAndSetDataContainersForContainerizedCachableAppRecords:error:
+ _objc_msgSend$_cachedDataContainerURLMap
+ _objc_msgSend$_clearStorageDirectory
+ _objc_msgSend$_copyChangingPersonaToPersona:
+ _objc_msgSend$_currentBootUUID
+ _objc_msgSend$_eduModeCacheAndSetDataContainersForContainerizedCachableAppRecords:error:
+ _objc_msgSend$_generateNonce
+ _objc_msgSend$_groupContainerURLDictFromDatabase
+ _objc_msgSend$_initializeStorage
+ _objc_msgSend$_injectPersonaWithAttributesIntoCacheIfUnknown:
+ _objc_msgSend$_processAppDataContainersFromContainermanagerForEduModeWithIdentifiers:locked:error:
+ _objc_msgSend$_processAppDataContainersFromContainermanagerForInstalledApplicationsForEduModeLocked:error:
+ _objc_msgSend$_processAppDataContainersFromContainermanagerWithRequiredContainers:locked:error:
+ _objc_msgSend$_processInDatabaseAppDataContainerWithContext:bundleUnitID:bundleDataIfAvailable:missingContainerMapForNonDatabaseRecords:locked:
+ _objc_msgSend$_processInDatabaseAppDataContainersWithContext:locked:
+ _objc_msgSend$_racy_wasRunning
+ _objc_msgSend$_rawGroupContainerURLMap
+ _objc_msgSend$_rawGroupContainerURLMapCheckingRedaction
+ _objc_msgSend$_rawPartnerFinancingAllowlistedBundleIDs
+ _objc_msgSend$_readBootInfo
+ _objc_msgSend$_runWork:
+ _objc_msgSend$_setCachedDataContainerURLMap:
+ _objc_msgSend$_setDataContainersOnApplicationRecordsFromCache:locked:
+ _objc_msgSend$_writeBootInfo:nonce:
+ _objc_msgSend$addBundlePersonaRecord:forBundleWithIdentifier:personaUniqueString:
+ _objc_msgSend$addBundlePersonaRecordsForICLBundleRecords:
+ _objc_msgSend$additionalConfiguration
+ _objc_msgSend$additionalConfigurationDigest
+ _objc_msgSend$allPersonaUniqueStringsOrNilForNonPersonified
+ _objc_msgSend$allowedPartnerFinancingAppBundleIDs
+ _objc_msgSend$appDataContainerMapLocked:
+ _objc_msgSend$appOrPlaceholderRecord
+ _objc_msgSend$backlightState
+ _objc_msgSend$baseBindingEvaluatorWithAuditToken:
+ _objc_msgSend$baseDatabaseStoreFileName
+ _objc_msgSend$bestDataContainerForCurrentPersona
+ _objc_msgSend$bestLaunchPersonaForExtension:hostPersona:hostAuditToken:error:
+ _objc_msgSend$bootNonce
+ _objc_msgSend$bundleRecordForBundleIdentifier:
+ _objc_msgSend$claimBindingsWithConfiguration:error:
+ _objc_msgSend$claimRecord
+ _objc_msgSend$codeSigningIdentifier
+ _objc_msgSend$codedAdditionalConfiguration
+ _objc_msgSend$configurationForDefaultMainDisplayMonitor
+ _objc_msgSend$containerMapWithDatabase:bundleBaseData:
+ _objc_msgSend$containerMapWithMap:
+ _objc_msgSend$containerMapWithNonPersonifiedContainer:
+ _objc_msgSend$containingApplication
+ _objc_msgSend$copyOverrides
+ _objc_msgSend$copyPathForPersistentData:error:
+ _objc_msgSend$copyWithOverrides:
+ _objc_msgSend$dataContainerURLForPersonaUniqueString:
+ _objc_msgSend$databaseCachesContainers
+ _objc_msgSend$defaultBindOptions
+ _objc_msgSend$deviceConfigurationUsesPersonas
+ _objc_msgSend$digest
+ _objc_msgSend$drain
+ _objc_msgSend$enqueueWork:
+ _objc_msgSend$executeWithContext:
+ _objc_msgSend$extensionBundleRecords
+ _objc_msgSend$extensionLaunchConfigurationsURL
+ _objc_msgSend$extensionWithUUID:error:
+ _objc_msgSend$fetchConfigurationWithUUID:error:
+ _objc_msgSend$fetchRegisteredConfigurationWithUUID:completion:
+ _objc_msgSend$fetchRegisteredConfigurationWithUUID:error:
+ _objc_msgSend$getCachedBundleIDToPersonasWithAttributesMap:personaUniqueStringToPersonasMap:systemPersona:personalPersona:
+ _objc_msgSend$getModifiedPluginDataForPluginUnit:
+ _objc_msgSend$getPersonalPersonaUniqueString:
+ _objc_msgSend$getPersonalPersonaWithAttributes
+ _objc_msgSend$getSystemPersonaWithAttributes
+ _objc_msgSend$getTypeRecordForPromiseAtURL:completionHandler:
+ _objc_msgSend$getUncachedBundleIDToPersonasWithAttributesMap:personaUniqueStringToPersonasMap:systemPersona:personalPersona:
+ _objc_msgSend$groupContainers
+ _objc_msgSend$groupContainersForCurrentPersona
+ _objc_msgSend$groupContainersForPersonaUniqueString:
+ _objc_msgSend$hasBooleanEntitlement:
+ _objc_msgSend$includeAppLinksForCallingApplication
+ _objc_msgSend$indexOfObjectPassingTest:
+ _objc_msgSend$initPrivate
+ _objc_msgSend$initWithAppBundleIdentifiers:unbundledExtensionBundleIdentifiers:bundlePersonaRecordMap:
+ _objc_msgSend$initWithAppRecord:
+ _objc_msgSend$initWithBundleIdentifiers:personas:bundlePersonaRecordMap:
+ _objc_msgSend$initWithDatabase:pluginUnit:pluginData:
+ _objc_msgSend$initWithDepth:label:
+ _objc_msgSend$initWithExtensionPoint:options:allowingRestrictedForReasons:
+ _objc_msgSend$initWithExtensionRecord:
+ _objc_msgSend$initWithGroupContainers:
+ _objc_msgSend$initWithICLBundleRecords:personasWithAttributes:
+ _objc_msgSend$initWithICLBundleRecordsInferringPersonas:
+ _objc_msgSend$initWithLazyPropertyList:
+ _objc_msgSend$initWithLegacyDictionaries:personasWithAttributes:
+ _objc_msgSend$initWithLegacyRecordDictionary:
+ _objc_msgSend$initWithMap:
+ _objc_msgSend$initWithPersonaInfoProvider:databaseProvider:
+ _objc_msgSend$initWithPersonaUniqueString:
+ _objc_msgSend$initWithPersonaUniqueString:additionalConfiguration:
+ _objc_msgSend$initWithPersonaUniqueString:affectedApps:affectedStandalonePlugins:
+ _objc_msgSend$initWithPersonaUniqueString:codedAdditionalConfiguration:additionalConfigurationDigest:
+ _objc_msgSend$initWithProxy:bindingStyle:
+ _objc_msgSend$initWithResolver:store:
+ _objc_msgSend$initWithStrategy:operationUUID:bundleIdentifier:precondition:type:
+ _objc_msgSend$initWithStrategy:operationUUID:installInfo:
+ _objc_msgSend$initWithSuccessfulIdentifiers:success:error:
+ _objc_msgSend$initWithUUID:error:
+ _objc_msgSend$isContainerized
+ _objc_msgSend$isDowngrade
+ _objc_msgSend$isGuestPersona
+ _objc_msgSend$isParallelPlaceholder
+ _objc_msgSend$isPartnerFinancingAllowlistEnabled
+ _objc_msgSend$isPersona:acceptableForExtension:hostPersona:hostAuditToken:
+ _objc_msgSend$launchRestrictedAppBundleIDs
+ _objc_msgSend$legacyDictionaryForBundleIdentifier:
+ _objc_msgSend$localizedNameIsActive
+ _objc_msgSend$lsInstallType
+ _objc_msgSend$ls_associatedPersonasIfAvailable
+ _objc_msgSend$ls_isApplicationOrPlaceholder
+ _objc_msgSend$ls_isNull
+ _objc_msgSend$ls_isPlugin
+ _objc_msgSend$modifiedSomeRecords
+ _objc_msgSend$monitorWithConfiguration:
+ _objc_msgSend$observerPayloadForNotification:appProxies:
+ _objc_msgSend$parallelPlaceholderURL
+ _objc_msgSend$parentalControlsRestrictedBundleIDs
+ _objc_msgSend$parseBundlePersonaRecordMap:error:
+ _objc_msgSend$partnerFinancingAllowlistedBundleIDs
+ _objc_msgSend$performPostInstallationRegistration:operationUUID:reply:
+ _objc_msgSend$performRebuildRegistration:reply:
+ _objc_msgSend$performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:bundlePersonaRecordMap:operationUUID:reply:
+ _objc_msgSend$personaIsApplicable:
+ _objc_msgSend$personaOrPrimaryPersonaPlaceholderIsApplicable:
+ _objc_msgSend$personaRecordsByPersonaForBundleID:
+ _objc_msgSend$personaUniqueString
+ _objc_msgSend$personaWithAttributesForPersonaUniqueString:error:
+ _objc_msgSend$personaWithAttributesForPersonaUniqueStringsIfAppropriate:
+ _objc_msgSend$personasRecordMap
+ _objc_msgSend$personasWithAttributes
+ _objc_msgSend$personasWithAttributesForPersonaUniqueStrings:error:
+ _objc_msgSend$pluginHasOverride
+ _objc_msgSend$postNotificationName:object:userInfo:audience:entitlement:options:error:
+ _objc_msgSend$preflightWithContext:error:
+ _objc_msgSend$registerApplicationForRebuildWithInstallInfo:requestContext:registrationError:
+ _objc_msgSend$registerBuiltinApplication:operationUUID:reply:
+ _objc_msgSend$registerBundleNodeReinitializingContext:inBundleContainer:installInfo:error:
+ _objc_msgSend$registerConfiguration:error:
+ _objc_msgSend$registerContainerizedApplicationWithInstallInfo:operationUUID:requestContext:saveObserver:registrationError:
+ _objc_msgSend$registerExtensionLaunchConfiguration:forExtensionWithUUID:hostPersonaUniqueString:hostAuditTokenData:completion:
+ _objc_msgSend$registerItemInfo:alias:diskImageAlias:bundleURL:installInfo:completionHandler:
+ _objc_msgSend$registerPluginNodeReinitializingContext:installInfo:existingPlugin:error:
+ _objc_msgSend$registerTransmissibleLaunchConfiguration:forExtensionWithUUID:hostPersonaUniqueString:hostAuditToken:error:
+ _objc_msgSend$removeReferencesToPersona:error:
+ _objc_msgSend$removeReferencesToPersonaWithUniqueString:operationUUID:reply:
+ _objc_msgSend$representedBundleIdentifier
+ _objc_msgSend$resolveConfiguration:forExtensionWithUUID:hostPersonaUniqueString:hostAuditToken:error:
+ _objc_msgSend$resolveIdentifiers:context:
+ _objc_msgSend$resolver
+ _objc_msgSend$restoredKeys
+ _objc_msgSend$restrictionReason
+ _objc_msgSend$sandboxExtensionForCreatedDiagnosticsStashDirectoryURLWithError:
+ _objc_msgSend$scanForAppsWithIdentifiersInSet:
+ _objc_msgSend$setAndProcessInstallInfo:
+ _objc_msgSend$setBootNonce:
+ _objc_msgSend$setBundleClassMask:
+ _objc_msgSend$setContainersForApplicationsWithBundleIdentifiers:unbundledExtensionsWithBundleIdentifiers:fromBundlePersonaRecordMap:operationUUID:reply:
+ _objc_msgSend$setIgnoreStrongBindingPreferences:
+ _objc_msgSend$setIgnoreWeakBindingPreferences:
+ _objc_msgSend$setInstallInfo:
+ _objc_msgSend$setIsDowngrade:
+ _objc_msgSend$setIsParallelPlaceholder:
+ _objc_msgSend$setIsPlaceholder:
+ _objc_msgSend$setPluginHasOverride:
+ _objc_msgSend$setTransitionHandler:
+ _objc_msgSend$sharedDataAccessor
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$stateProviderForRestrictionsManager:
+ _objc_msgSend$storageDirectoryURL
+ _objc_msgSend$store
+ _objc_msgSend$success
+ _objc_msgSend$systemDataDiagnosticsStashDirectoryURLWithError:
+ _objc_msgSend$systemDataDiagnosticsStashedDatabaseURLWithError:
+ _objc_msgSend$triggerRegistrationForContainerizedContentWithOptions:withError:
+ _objc_msgSend$typeRecordForPromiseAtURL:error:
+ _objc_msgSend$updatePluginRecord:
+ _objc_msgSend$validateWithContext:personaUniqueStrings:applicationBundleIDs:error:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x10
+ _objc_retain_x7
+ _os_signpost_enabled
+ _os_signpost_id_generate
+ _preferredLocalizations.once.251
+ _registerApplicationWithICLRecord
+ _registerApplicationWithICLRecord.cold.1
+ _registerApplicationWithICLRecord.cold.2
+ _registerApplicationWithICLRecord.cold.3
+ _registerForRebuildWithRepresentativeBundleAndInstallInfo
+ _sched_yield
+ _sharedServerInstance.onceToken
+ _sharedServerInstance.sharedInstance
+ _softLinkMobileInstallationEnumerateAllInstalledItemBundleRecords
+ _systemRegistrar.onceToken
+ _systemRegistrar.systemRegistrar
+ _xpc_array_create
+ _xpc_connection_cancel
+ _xpc_connection_create_mach_service
+ _xpc_connection_resume
+ _xpc_connection_send_message_with_reply_sync
+ _xpc_connection_set_event_handler
+ _xpc_dictionary_get_int64
+ _xpc_string_create
- +[LSApplicationRecord(Identities) personalPersonaAttributes]
- +[LSApplicationRecord(Identities) personalPersonaAttributes].cold.1
- +[LSApplicationRecord(Redaction) redactedProperties]
- +[LSDocumentProxy(Binding) _bindingEvaluatorResultFilterForBindingStyle:contentIsManaged:sourceAuditToken:]
- +[LSDocumentProxy(Binding) _bindingEvaluatorResultFilterForBindingStyle:contentIsManaged:sourceAuditToken:].cold.1
- -[LSApplicationRecord _LSRecord_resolve__rawEnvironmentVariables]
- -[LSApplicationRecord _LSRecord_resolve_isDeletableSystemApplication]
- -[LSApplicationRecord _LSRecord_resolve_isDeletable]
- -[LSApplicationRecord _rawEnvironmentVariablesWithContext:tableID:unitID:unitBytes:]
- -[LSApplicationRecord _rawEnvironmentVariables]
- -[LSApplicationRecord additionalEnvironmentVariables].cold.1
- -[LSApplicationRecord additionalEnvironmentVariables].cold.2
- -[LSApplicationRecord isDeletableSystemApplicationWithContext:tableID:unitID:unitBytes:]
- -[LSApplicationRecord isDeletableSystemApplication]
- -[LSApplicationRecord isDeletableWithContext:tableID:unitID:unitBytes:]
- -[LSApplicationRecord isDeletable]
- -[LSApplicationRestrictionsManager isApplicationRestricted:checkFlags:]
- -[LSApplicationRestrictionsManager isApplicationRestricted:checkFlags:stateProvider:]
- -[LSApplicationRestrictionsManager reasonForApplicationRestriction:checkFlags:stateProvider:]
- -[LSApplicationWorkspace registerApplicationForRebuildWithInfoDictionaries:personaUniqueStrings:requestContext:registrationError:]
- -[LSApplicationWorkspace registerContainerizedApplicationWithInfoDictionaries:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:]
- -[LSApplicationWorkspace scanForAppsInRatingRankExceptionsList:]
- -[LSBuiltinApplicationRegistrant initWithStrategy:operationUUID:itemInfoDict:personas:]
- -[LSBuiltinPluginRegistrant initWithStrategy:operationUUID:itemInfoDict:]
- -[LSBundleProxy _initWithBundleUnit:context:bundleType:bundleID:localizedName:bundleContainerURL:dataContainerURL:resourcesDirectoryURL:iconsDictionary:iconFileNames:version:]
- -[LSBundleProxy _initWithBundleUnit:context:bundleType:bundleID:localizedName:bundleContainerURL:dataContainerURL:resourcesDirectoryURL:iconsDictionary:iconFileNames:version:].cold.1
- -[LSBundleRecord _LSRecord_resolve__dataContainerURLFromDatabase]
- -[LSBundleRecord _LSRecord_resolve__rawGroupContainerURLs]
- -[LSBundleRecord _cachedDataContainerURL]
- -[LSBundleRecord _dataContainerURLFromDatabaseWithContext:tableID:unitID:unitBytes:]
- -[LSBundleRecord _dataContainerURLFromDatabase]
- -[LSBundleRecord _rawGroupContainerURLsCheckingRedaction]
- -[LSBundleRecord _rawGroupContainerURLsCheckingRedaction].cold.1
- -[LSBundleRecord _rawGroupContainerURLsWithContext:tableID:unitID:unitBytes:]
- -[LSBundleRecord(Containers) getDataContainerURL:error:].cold.2
- -[LSBundleRecordBuilder dataContainerURL]
- -[LSBundleRecordBuilder groupContainers]
- -[LSBundleRecordBuilder pluginMIDicts]
- -[LSBundleRecordBuilder sandboxEnvironmentVariables]
- -[LSClaimBindingBindable baseBindingEvaluatorWithBindingStyle:auditToken:]
- -[LSDatabaseRebuildContext registerItems:]
- -[LSDocumentProxy uniqueIdentifier]
- -[LSMIResultRegistrant initWithContext:operationUUID:itemInfoDict:personas:]
- -[LSMIResultRegistrantTrueDatabaseContext registerBundleNodeReinitializingContext:inBundleContainer:installDictionary:personasWithAttributes:error:]
- -[LSMIResultRegistrantTrueDatabaseContext registerPluginNodeReinitializingContext:installDictionary:existingPlugin:error:]
- -[LSMIResultUnregistrant initWithContext:operationUUID:bundleIdentifier:precondition:type:]
- -[LSRebuildStatisticsGatherer registeredBundleOfType:]
- -[LSRecordBuilder parseInfoPlist:]
- -[LSRecordBuilder parseInstallationInfo:]
- -[LSRecordBuilder parseiTunesMetadata:]
- -[LSResourceProxy uniqueIdentifier]
- -[LSUseValuesMCStateProvider initWithAllowlistEnabled:allowlistedBundles:restrictedBundles:ratingRankExceptions:maximumRating:]
- -[_LSBoundIconInfo setDataContainerURL:]
- -[_LSClaimBindingDocumentProxyBindable baseBindingEvaluatorWithBindingStyle:auditToken:]
- -[_LSClaimBindingTypeIdentifierBindable baseBindingEvaluatorWithBindingStyle:auditToken:]
- -[_LSClaimBindingURLBindable baseBindingEvaluatorWithBindingStyle:auditToken:]
- -[_LSCompatibilityNothingBindable baseBindingEvaluatorWithBindingStyle:auditToken:]
- -[_LSCompatibilityNothingBindable baseBindingEvaluatorWithBindingStyle:auditToken:].cold.1
- -[_LSDModifyClient performPostInstallationRegistration:personaUniqueStrings:operationUUID:reply:]
- -[_LSDModifyClient performPostInstallationRegistration:personaUniqueStrings:operationUUID:reply:].cold.1
- -[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:operationUUID:reply:]
- -[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:operationUUID:reply:].cold.1
- -[_LSDModifyClient registerBuiltinApplication:personaUniqueStrings:operationUUID:reply:]
- -[_LSDModifyClient registerBuiltinApplication:personaUniqueStrings:operationUUID:reply:].cold.1
- -[_LSDModifyClient registerItemInfo:alias:diskImageAlias:bundleURL:installationPlist:completionHandler:]
- -[_LSDRebuildClient performRebuildRegistration:personaUniqueStrings:reply:]
- -[_LSDRebuildClient performRebuildRegistration:personaUniqueStrings:reply:].cold.1
- -[_LSDRebuildClient performRebuildRegistration:personaUniqueStrings:reply:].cold.2
- -[_LSPersonaDatabase _getPersonaAttributesRetryingIfNecessary]
- -[_LSPersonaDatabase _getPersonaAttributesRetryingIfNecessary].cold.1
- -[_LSPersonaDatabase _getPersonaAttributesRetryingIfNecessary].cold.2
- -[_LSPersonaDatabase getCachedBundleIDToPersonasWithAttributesMap:systemPersonaUniqueString:personalPersonaUniqueString:]
- -[_LSPersonaDatabase getUncachedBundleIDToPersonasWithAttributesMap:systemPersonaUniqueString:personalPersonaUniqueString:]
- GCC_except_table135
- GCC_except_table203
- GCC_except_table208
- GCC_except_table209
- GCC_except_table210
- GCC_except_table213
- GCC_except_table216
- GCC_except_table219
- GCC_except_table226
- GCC_except_table229
- GCC_except_table237
- GCC_except_table247
- GCC_except_table248
- GCC_except_table250
- GCC_except_table253
- GCC_except_table260
- GCC_except_table261
- GCC_except_table263
- GCC_except_table272
- GCC_except_table275
- GCC_except_table282
- GCC_except_table287
- GCC_except_table293
- GCC_except_table294
- GCC_except_table296
- GCC_except_table301
- GCC_except_table307
- GCC_except_table308
- GCC_except_table312
- GCC_except_table318
- GCC_except_table328
- GCC_except_table332
- GCC_except_table333
- GCC_except_table334
- GCC_except_table345
- GCC_except_table347
- GCC_except_table350
- GCC_except_table352
- GCC_except_table356
- GCC_except_table358
- GCC_except_table360
- GCC_except_table377
- GCC_except_table378
- GCC_except_table386
- GCC_except_table393
- GCC_except_table394
- GCC_except_table396
- GCC_except_table397
- GCC_except_table410
- GCC_except_table413
- GCC_except_table417
- GCC_except_table435
- GCC_except_table441
- GCC_except_table449
- GCC_except_table451
- GCC_except_table455
- GCC_except_table456
- GCC_except_table488
- GCC_except_table489
- GCC_except_table492
- GCC_except_table495
- GCC_except_table497
- GCC_except_table498
- _CC_MD5
- _CFSetGetTypeID
- _ExtensionFoundationLibrary.frameworkLibrary
- _FPExtendBookmarkForDocumentURL$delayInitStub
- _OBJC_IVAR_$_LSBuiltinApplicationRegistrant._miDict
- _OBJC_IVAR_$_LSBuiltinApplicationRegistrant._personas
- _OBJC_IVAR_$_LSBuiltinPluginRegistrant._miDict
- _OBJC_IVAR_$_LSBundleRecord._cachedDataContainerURL
- _OBJC_IVAR_$_LSBundleRecordBuilder._dataContainerURL
- _OBJC_IVAR_$_LSBundleRecordBuilder._groupContainers
- _OBJC_IVAR_$_LSBundleRecordBuilder._pluginMIDicts
- _OBJC_IVAR_$_LSBundleRecordBuilder._sandboxEnvironmentVariables
- _OBJC_IVAR_$_LSClaimBindingConfiguration._bindingStyle
- _OBJC_IVAR_$_LSMIResultRegistrant._miDict
- _OBJC_IVAR_$_LSMIResultRegistrant._personas
- _OBJC_IVAR_$__LSBoundIconInfo._dataContainerURL
- _OBJC_IVAR_$__LSPersonaDatabase._cachedPersonalPersonaUniqueString
- _OBJC_IVAR_$__LSPersonaDatabase._cachedSystemPersonaUniqueString
- _OUTLINED_FUNCTION_27
- _OUTLINED_FUNCTION_28
- _OUTLINED_FUNCTION_29
- _OUTLINED_FUNCTION_30
- _OUTLINED_FUNCTION_31
- __LSApplicationRestrictionsManagerIsApplicationRestrictedCheckingFlags
- __LSCopyDataContainerURLFromContainermanager
- __LSCopyDataContainerURLFromContainermanager.cold.1
- __LSCopyEnvironmentVariablesFromContainermanager
- __LSCopyEnvironmentVariablesFromContainermanager.cold.1
- __LSCopyGroupContainerIdentifiersFromEntitlements.cold.1
- __LSCopyGroupContainerURLSFromContainermanager
- __LSCopyGroupContainerURLSFromContainermanager.cold.1
- __LSCopyRationalizedEnvironmentVariablesDict
- __LSDatabaseGetSeedingGroup
- __LSDatabaseGetSeedingGroup.cold.1
- __LSGetCollapsedMIDictionaryForAppAndContentsDictionaries
- __LSPersonaWithAttributesPersonaUniqueString
- __LSServer_LSRegisterICLItem
- __LSServer_PerformExternalRebuildRegistration.cold.2
- __LSShouldFetchContainersFromContainermanagerForPersona
- __LSShouldFetchContainersFromContainermanagerForPersona.cold.1
- __LSShouldFetchContainersFromContainermanagerForPersona.cold.2
- __OBJC_$_CLASS_METHODS_LSApplicationExtensionRecord(IconServices|Intents|Redaction|AppProtectionPrivate|Utility|Enumeration)
- __OBJC_$_CLASS_METHODS_LSApplicationWorkspace(DeprecatedEnumeration|DefaultApps|Marketplaces|URLQueries|DeprecatedURLQueries|OpenAdditions|LSURLOverride)
- __OBJC_$_CLASS_METHODS__LSPersonaWithAttributes
- __OBJC_$_INSTANCE_METHODS_LSApplicationExtensionRecord(IconServices|Intents|Redaction|AppProtectionPrivate|Utility|Enumeration)
- __OBJC_$_INSTANCE_METHODS_LSApplicationWorkspace(DeprecatedEnumeration|DefaultApps|Marketplaces|URLQueries|DeprecatedURLQueries|OpenAdditions|LSURLOverride)
- __OBJC_$_INSTANCE_METHODS__LSPersonaWithAttributes
- __Z19_LSAudioUnitURLOpenP5NSURL
- __ZGVZZL37_LSSchemeApprovalGetBouncebackHistoryvEUb_E14backlightToken
- __ZL17_LSRegisterPluginP11_LSDatabaseRK12LSPluginInfoPK14__CFDictionaryPK10__CFStringS9_S6_jPj
- __ZL17_LSRegisterPluginP11_LSDatabaseRK12LSPluginInfoPK14__CFDictionaryPK10__CFStringS9_S6_jPj.cold.1
- __ZL17_LSRegisterPluginP11_LSDatabaseRK12LSPluginInfoPK14__CFDictionaryPK10__CFStringS9_S6_jPj.cold.2
- __ZL21_LSRegisterBundleNodeP9LSContextjP6FSNodeS2_jPK14__CFDictionaryPPK9__CFArrayPhPjPU15__autoreleasingP7NSError
- __ZL23_LSDispatchRegistrationP9LSContextPKcPK18LSRegistrationInfoP6NSDataS7_PK7__CFURLPK14__CFDictionaryPjPPK9__CFArrayPh
- __ZL24_LSRegisterDirectoryNodeP9LSContextP6FSNodeS2_PK18LSRegistrationInfoP6NSDataPK14__CFDictionaryPPK9__CFArrayPhPj
- __ZL36_LSServerCreateBundleDataAndRegisterP9LSContextP18LSRegistrationInfoP6NSDataPK7__CFURLPK14__CFDictionaryPjPPK9__CFArrayPh
- __ZL39_LSSchemeApprovalClearBouncebackHistoryv
- __ZL41_LSCreateRegistrationDataForDirectoryNodeP9LSContextP18LSRegistrationInfoPK7__CFURLP17_LSBundleProviderP6FSNodePK14__CFDictionaryPPK9__CFArray
- __ZL41_LSCreateRegistrationDataForDirectoryNodeP9LSContextP18LSRegistrationInfoPK7__CFURLP17_LSBundleProviderP6FSNodePK14__CFDictionaryPPK9__CFArray.cold.1
- __ZL41_LSCreateRegistrationDataForDirectoryNodeP9LSContextP18LSRegistrationInfoPK7__CFURLP17_LSBundleProviderP6FSNodePK14__CFDictionaryPPK9__CFArray.cold.2
- __ZL41_LSCreateRegistrationDataForDirectoryNodeP9LSContextP18LSRegistrationInfoPK7__CFURLP17_LSBundleProviderP6FSNodePK14__CFDictionaryPPK9__CFArray.cold.3
- __ZL41_LSCreateRegistrationDataForDirectoryNodeP9LSContextP18LSRegistrationInfoPK7__CFURLP17_LSBundleProviderP6FSNodePK14__CFDictionaryPPK9__CFArray.cold.4
- __ZL59initMobileInstallationEnumerateAllInstalledItemDictionariesP12NSDictionaryU13block_pointerFvPS_IP8NSStringP11objc_objectEP7NSErrorE
- __ZL63softLinkMobileInstallationEnumerateAllInstalledItemDictionaries
- __ZN14LaunchServices3$_78__invokeEv
- __ZN14LaunchServices6RecordL26cachedDataContainerURLLockE
- __ZNKSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore removeEntriesForBundleIdentifier:]E3$_1FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EE7__cloneEPNS0_6__baseIS5_EE
- __ZNKSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore removeEntriesForBundleIdentifier:]E3$_1FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore setEntry:forApplication:category:]E3$_0FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EE7__cloneEPNS0_6__baseIS5_EE
- __ZNKSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore setEntry:forApplication:category:]E3$_0FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EE7__cloneEv
- __ZNKSt3__111__copy_implclB9nqn210106IPKN14LaunchServices17BindingEvaluation15ExtendedBindingES6_PS4_EENS_4pairIT_T1_EES9_T0_SA_
- __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB9nqn210106IPN14LaunchServices17BindingEvaluation15ExtendedBindingES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
- __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB9nqn210106IPU6__weakP8LSRecordS7_S7_EENS_4pairIT_T1_EES9_T0_SA_
- __ZNKSt3__112__hash_tableINS_17__hash_value_typeIj38_LSDatabaseTableVisualizationFunctionsEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SB_S9_Lb1EEENS_9allocatorIS7_EEE4findIjEENS_21__hash_const_iteratorIPNS_11__hash_nodeIS3_PvEEEERKT_
- __ZNKSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_mapIjbNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjbEEEEEEEENS_22__unordered_map_hasherIjNS8_IS9_SC_EES4_S6_Lb1EEENS_21__unordered_map_equalIjSF_S6_S4_Lb1EEENS7_ISF_EEE4findIjEENS_21__hash_const_iteratorIPNS_11__hash_nodeISD_PvEEEERKT_
- __ZNKSt3__112__hash_tableINS_17__hash_value_typeIjbEENS_22__unordered_map_hasherIjNS_4pairIKjbEENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE4findIjEENS_21__hash_const_iteratorIPNS_11__hash_nodeIS2_PvEEEERKT_
- __ZNKSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjNS_4pairIKjjEENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE4findIjEENS_21__hash_const_iteratorIPNS_11__hash_nodeIS2_PvEEEERKT_
- __ZNKSt3__116__variant_detail12__visitation9__variant15__value_visitorIZN14LaunchServices20AppRecordEnumeration32VolumeContainerResolutionAdapter7resolveEP9LSContextEUlRKT_E_EclB9nqn210106IJRNS0_5__altILm1EU8__strongP5NSURLEEEEEDcDpOT_
- __ZNKSt3__116__variant_detail12__visitation9__variant15__value_visitorIZN14LaunchServices20AppRecordEnumeration32VolumeContainerResolutionAdapter7resolveEP9LSContextEUlRKT_E_EclB9nqn210106IJRNS0_5__altILm2EU8__strongP7NSErrorEEEEEDcDpOT_
- __ZNKSt3__120__move_backward_implINS_17_ClassicAlgPolicyEEclB9nqn210106IP9LSBindingS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
- __ZNKSt3__120__move_backward_implINS_17_ClassicAlgPolicyEEclB9nqn210106IPN14LaunchServices17BindingEvaluation15ExtendedBindingES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
- __ZNKSt3__120__move_backward_implINS_17_ClassicAlgPolicyEEclB9nqn210106IPU6__weakP8LSRecordS7_S7_EENS_4pairIT_T1_EES9_T0_SA_
- __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9nqn210106EPKvm
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB9nqn210106ERKS6_S9_
- __ZNSt3__110__function12__value_funcIFN14LaunchServices23LSDefaultAppsExtraStateENS_8optionalIS3_EEP7NSErrorEED2B9nqn210106Ev
- __ZNSt3__110__function12__value_funcIFP11objc_objectS3_P7NSErrorEED2B9nqn210106Ev
- __ZNSt3__110__function12__value_funcIFbP11objc_objectEEC2B9nqn210106EOS5_
- __ZNSt3__110__function12__value_funcIFbP11objc_objectEED2B9nqn210106Ev
- __ZNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore removeEntriesForBundleIdentifier:]E3$_1FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore removeEntriesForBundleIdentifier:]E3$_1FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EE7destroyEv
- __ZNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore removeEntriesForBundleIdentifier:]E3$_1FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EED0Ev
- __ZNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore removeEntriesForBundleIdentifier:]E3$_1FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EED1Ev
- __ZNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore removeEntriesForBundleIdentifier:]E3$_1FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EEclEOS4_
- __ZNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore setEntry:forApplication:category:]E3$_0FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore setEntry:forApplication:category:]E3$_0FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EE7destroyEv
- __ZNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore setEntry:forApplication:category:]E3$_0FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EED0Ev
- __ZNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore setEntry:forApplication:category:]E3$_0FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EED1Ev
- __ZNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore setEntry:forApplication:category:]E3$_0FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EEclEOS4_
- __ZNSt3__110unique_ptrIA_PNS_16__hash_node_baseIPNS_11__hash_nodeIjPvEEEENS_25__bucket_list_deallocatorIN14LaunchServices19MallocZoneAllocatorIS7_NSA_17BindingEvaluation17BindingMallocZoneEEEEEE5resetB9nqn210106IPS7_Li0EEEvT_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEEPvEENS_22__hash_node_destructorINS_9allocatorISA_EEEEED1B9nqn210106Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIPKvU8__strongP5NSSetIP10objc_classEEEPvEENS_22__hash_node_destructorINS_9allocatorISD_EEEEED1B9nqn210106Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS_13unordered_mapIjbNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjbEEEEEEEEPvEENS_22__hash_node_destructorINS8_ISG_EEEEED1B9nqn210106Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEEPvEENS_22__hash_node_destructorINS8_ISD_EEEEED1B9nqn210106Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjU8__strongP19LSApplicationRecordEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEED1B9nqn210106Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjU8__strongP8NSStringEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEED1B9nqn210106Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyN14LaunchServices11OpenStaging20StagingDirectoryInfoEEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEED1B9nqn210106Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeIjPvEENS_22__hash_node_destructorIN14LaunchServices19MallocZoneAllocatorIS3_NS5_17BindingEvaluation17BindingMallocZoneEEEEEE5resetB9nqn210106EPS3_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeI23os_eligibility_domain_tN14LaunchServices7notifyd11NotifyTokenEEEPvEENS_22__tree_node_destructorINS_9allocatorIS9_EEEEED1B9nqn210106Ev
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIjU8__strongP8NSStringEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEED1B9nqn210106Ev
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeImU8__strongU13block_pointerFvvEEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEED1B9nqn210106Ev
- __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZ87+[LSApplicationRecord(UserActivity) applicationRecordsForUserActivityType:limit:error:]E3$_0PNS_4pairIjPK12LSBundleDataEELb0EEEvT1_SA_T0_NS_15iterator_traitsISA_E15difference_typeEb
- __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]E3$_1PjLb0EEEvT1_S5_T0_NS_15iterator_traitsIS5_E15difference_typeEb
- __ZNSt3__111__sift_downB9nqn210106INS_17_ClassicAlgPolicyERZN14LaunchServices17BindingEvaluationL4sortERNS3_5StateEE3$_0NS_11__wrap_iterIPNS3_15ExtendedBindingEEEEEvT1_OT0_NS_15iterator_traitsISC_E15difference_typeESC_
- __ZNSt3__112__destroy_atB9nqn210106IN14LaunchServices30FeatureFlagPredicateEvaluation20FeatureFlagSpecifierELi0EEEvPT_
- __ZNSt3__112__hash_tableINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4hashIS6_EENS_8equal_toIS6_EENS4_IS6_EEE25__emplace_unique_key_argsIS6_JS6_EEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI12LSSessionKey31LSQuickSessionAvailabilityStateEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S3_EE18LSSessionKeyHasher22LSSessionKeyComparatorLb1EEENS_21__unordered_map_equalIS2_S8_SA_S9_Lb1EEENS_9allocatorIS8_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI12LSSessionKey31LSQuickSessionAvailabilityStateEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S3_EE18LSSessionKeyHasher22LSSessionKeyComparatorLb1EEENS_21__unordered_map_equalIS2_S8_SA_S9_Lb1EEENS_9allocatorIS8_EEE25__emplace_unique_key_argsIS2_JRKNS_21piecewise_construct_tENS_5tupleIJOS2_EEENSL_IJEEEEEENS6_INS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI12LSSessionKey31LSQuickSessionAvailabilityStateEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S3_EE18LSSessionKeyHasher22LSSessionKeyComparatorLb1EEENS_21__unordered_map_equalIS2_S8_SA_S9_Lb1EEENS_9allocatorIS8_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI12LSSessionKeyP9LSSessionEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S4_EE18LSSessionKeyHasher22LSSessionKeyComparatorLb1EEENS_21__unordered_map_equalIS2_S9_SB_SA_Lb1EEENS_9allocatorIS9_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI12LSSessionKeyP9LSSessionEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S4_EE18LSSessionKeyHasher22LSSessionKeyComparatorLb1EEENS_21__unordered_map_equalIS2_S9_SB_SA_Lb1EEENS_9allocatorIS9_EEE25__emplace_unique_key_argsIS2_JRKNS_21piecewise_construct_tENS_5tupleIJRS8_EEENSM_IJEEEEEENS7_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI12LSSessionKeyP9LSSessionEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S4_EE18LSSessionKeyHasher22LSSessionKeyComparatorLb1EEENS_21__unordered_map_equalIS2_S9_SB_SA_Lb1EEENS_9allocatorIS9_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selector18FSSelectorCategoryEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S4_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S9_SD_SB_Lb1EEENS_9allocatorIS9_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selector18FSSelectorCategoryEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S4_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S9_SD_SB_Lb1EEENS_9allocatorIS9_EEE25__emplace_unique_key_argsIS3_JNS7_IS3_S4_EEEEENS7_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selector18FSSelectorCategoryEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S4_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S9_SD_SB_Lb1EEENS_9allocatorIS9_EEE4findIS3_EENS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selector18FSSelectorCategoryEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S4_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S9_SD_SB_Lb1EEENS_9allocatorIS9_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SB_SF_SD_Lb1EEENS_9allocatorISB_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SB_SF_SD_Lb1EEENS_9allocatorISB_EEE14__erase_uniqueIS3_EEmRKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SB_SF_SD_Lb1EEENS_9allocatorISB_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS7_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SB_SF_SD_Lb1EEENS_9allocatorISB_EEE25__emplace_unique_key_argsIS3_JRKSB_EEENS9_INS_15__hash_iteratorIPNS_11__hash_nodeIS7_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SB_SF_SD_Lb1EEENS_9allocatorISB_EEE25__emplace_unique_key_argsIS3_JRS3_RU8__strongKS5_EEENS9_INS_15__hash_iteratorIPNS_11__hash_nodeIS7_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SB_SF_SD_Lb1EEENS_9allocatorISB_EEE25__emplace_unique_key_argsIS3_JS3_DnEEENS9_INS_15__hash_iteratorIPNS_11__hash_nodeIS7_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SB_SF_SD_Lb1EEENS_9allocatorISB_EEE25__emplace_unique_key_argsIS3_JS3_RU8__strongKS5_EEENS9_INS_15__hash_iteratorIPNS_11__hash_nodeIS7_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SB_SF_SD_Lb1EEENS_9allocatorISB_EEE4findIS3_EENS_15__hash_iteratorIPNS_11__hash_nodeIS7_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SB_SF_SD_Lb1EEENS_9allocatorISB_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS7_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SB_SF_SD_Lb1EEENS_9allocatorISB_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP13objc_selectorU8__strongP11objc_objectEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SB_SF_SD_Lb1EEENS_9allocatorISB_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP17_opaque_pthread_tNS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SC_SG_SE_Lb1EEENS_9allocatorISC_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP17_opaque_pthread_tNS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SC_SG_SE_Lb1EEENS_9allocatorISC_EEE14__erase_uniqueIS3_EEmRKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP17_opaque_pthread_tNS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SC_SG_SE_Lb1EEENS_9allocatorISC_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS8_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP17_opaque_pthread_tNS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SC_SG_SE_Lb1EEENS_9allocatorISC_EEE25__emplace_unique_key_argsIS3_JRKNS_21piecewise_construct_tENS_5tupleIJOS3_EEENSR_IJOS7_EEEEEENSA_INS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP17_opaque_pthread_tNS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SC_SG_SE_Lb1EEENS_9allocatorISC_EEE4findIS3_EENS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP17_opaque_pthread_tNS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SC_SG_SE_Lb1EEENS_9allocatorISC_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS8_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP17_opaque_pthread_tNS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SC_SG_SE_Lb1EEENS_9allocatorISC_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS8_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP17_opaque_pthread_tNS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SC_SG_SE_Lb1EEENS_9allocatorISC_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIP17_opaque_pthread_tNS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SC_SG_SE_Lb1EEENS_9allocatorISC_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvNS_6vectorINS_4pairIP13objc_selectorPFvP11objc_objectS7_EEENS_9allocatorISC_EEEEEENS_22__unordered_map_hasherIS3_NS5_IKS3_SF_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SJ_SN_SL_Lb1EEENSD_ISJ_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvNS_6vectorINS_4pairIP13objc_selectorPFvP11objc_objectS7_EEENS_9allocatorISC_EEEEEENS_22__unordered_map_hasherIS3_NS5_IKS3_SF_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SJ_SN_SL_Lb1EEENSD_ISJ_EEE25__emplace_unique_key_argsIS3_JS3_SF_EEENS5_INS_15__hash_iteratorIPNS_11__hash_nodeISG_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvNS_6vectorINS_4pairIP13objc_selectorPFvP11objc_objectS7_EEENS_9allocatorISC_EEEEEENS_22__unordered_map_hasherIS3_NS5_IKS3_SF_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SJ_SN_SL_Lb1EEENSD_ISJ_EEE4findIS3_EENS_15__hash_iteratorIPNS_11__hash_nodeISG_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvNS_6vectorINS_4pairIP13objc_selectorPFvP11objc_objectS7_EEENS_9allocatorISC_EEEEEENS_22__unordered_map_hasherIS3_NS5_IKS3_SF_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SJ_SN_SL_Lb1EEENSD_ISJ_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvU8__strongP5NSSetIP10objc_classEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S9_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SE_SI_SG_Lb1EEENS_9allocatorISE_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvU8__strongP5NSSetIP10objc_classEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S9_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SE_SI_SG_Lb1EEENS_9allocatorISE_EEE25__emplace_unique_key_argsIS3_JS3_RS9_EEENSC_INS_15__hash_iteratorIPNS_11__hash_nodeISA_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvU8__strongP5NSSetIP10objc_classEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S9_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SE_SI_SG_Lb1EEENS_9allocatorISE_EEE4findIS3_EENS_15__hash_iteratorIPNS_11__hash_nodeISA_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvU8__strongP5NSSetIP10objc_classEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S9_EENS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_SE_SI_SG_Lb1EEENS_9allocatorISE_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIj12LSPluginDataEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SB_S9_Lb1EEENS_9allocatorIS7_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIj12LSPluginDataEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SB_S9_Lb1EEENS_9allocatorIS7_EEE25__emplace_unique_key_argsIjJNS5_IjS2_EEEEENS5_INS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIj12LSPluginDataEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SB_S9_Lb1EEENS_9allocatorIS7_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIj12LSPluginDataEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SB_S9_Lb1EEENS_9allocatorIS7_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIj12LSPluginDataEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SB_S9_Lb1EEENS_9allocatorIS7_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIj37LSApplicationRecordUpdateAvailabilityEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SB_S9_Lb1EEENS_9allocatorIS7_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIj37LSApplicationRecordUpdateAvailabilityEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SB_S9_Lb1EEENS_9allocatorIS7_EEE25__emplace_unique_key_argsIjJRjS2_EEENS5_INS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIj37LSApplicationRecordUpdateAvailabilityEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SB_S9_Lb1EEENS_9allocatorIS7_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIj37LSApplicationRecordUpdateAvailabilityEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SB_S9_Lb1EEENS_9allocatorIS7_EEEC2EOSH_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIj37LSApplicationRecordUpdateAvailabilityEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SB_S9_Lb1EEENS_9allocatorIS7_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIj38_LSDatabaseTableVisualizationFunctionsEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SB_S9_Lb1EEENS_9allocatorIS7_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIj38_LSDatabaseTableVisualizationFunctionsEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SB_S9_Lb1EEENS_9allocatorIS7_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJOjEEENSM_IJEEEEEENS5_INS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIj38_LSDatabaseTableVisualizationFunctionsEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SB_S9_Lb1EEENS_9allocatorIS7_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRS6_EEENSM_IJEEEEEENS5_INS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIj38_LSDatabaseTableVisualizationFunctionsEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SB_S9_Lb1EEENS_9allocatorIS7_EEE25__emplace_unique_key_argsIjJRKS7_EEENS5_INS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIj38_LSDatabaseTableVisualizationFunctionsEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SB_S9_Lb1EEENS_9allocatorIS7_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIj38_LSDatabaseTableVisualizationFunctionsEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SB_S9_Lb1EEENS_9allocatorIS7_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIj38_LSDatabaseTableVisualizationFunctionsEENS_22__unordered_map_hasherIjNS_4pairIKjS2_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SB_S9_Lb1EEENS_9allocatorIS7_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_mapIjbNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjbEEEEEEEENS_22__unordered_map_hasherIjNS8_IS9_SC_EES4_S6_Lb1EEENS_21__unordered_map_equalIjSF_S6_S4_Lb1EEENS7_ISF_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_mapIjbNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjbEEEEEEEENS_22__unordered_map_hasherIjNS8_IS9_SC_EES4_S6_Lb1EEENS_21__unordered_map_equalIjSF_S6_S4_Lb1EEENS7_ISF_EEE13__move_assignERSK_NS_17integral_constantIbLb1EEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_mapIjbNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjbEEEEEEEENS_22__unordered_map_hasherIjNS8_IS9_SC_EES4_S6_Lb1EEENS_21__unordered_map_equalIjSF_S6_S4_Lb1EEENS7_ISF_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeISD_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_mapIjbNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjbEEEEEEEENS_22__unordered_map_hasherIjNS8_IS9_SC_EES4_S6_Lb1EEENS_21__unordered_map_equalIjSF_S6_S4_Lb1EEENS7_ISF_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRS9_EEENSP_IJEEEEEENS8_INS_15__hash_iteratorIPNS_11__hash_nodeISD_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_mapIjbNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjbEEEEEEEENS_22__unordered_map_hasherIjNS8_IS9_SC_EES4_S6_Lb1EEENS_21__unordered_map_equalIjSF_S6_S4_Lb1EEENS7_ISF_EEE5clearEv
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_mapIjbNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjbEEEEEEEENS_22__unordered_map_hasherIjNS8_IS9_SC_EES4_S6_Lb1EEENS_21__unordered_map_equalIjSF_S6_S4_Lb1EEENS7_ISF_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_mapIjbNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjbEEEEEEEENS_22__unordered_map_hasherIjNS8_IS9_SC_EES4_S6_Lb1EEENS_21__unordered_map_equalIjSF_S6_S4_Lb1EEENS7_ISF_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEENS_22__unordered_map_hasherIjNS_4pairIKjS9_EES4_S6_Lb1EEENS_21__unordered_map_equalIjSE_S6_S4_Lb1EEENS7_ISE_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEENS_22__unordered_map_hasherIjNS_4pairIKjS9_EES4_S6_Lb1EEENS_21__unordered_map_equalIjSE_S6_S4_Lb1EEENS7_ISE_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeISA_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEENS_22__unordered_map_hasherIjNS_4pairIKjS9_EES4_S6_Lb1EEENS_21__unordered_map_equalIjSE_S6_S4_Lb1EEENS7_ISE_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRSD_EEENSO_IJEEEEEENSC_INS_15__hash_iteratorIPNS_11__hash_nodeISA_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEENS_22__unordered_map_hasherIjNS_4pairIKjS9_EES4_S6_Lb1EEENS_21__unordered_map_equalIjSE_S6_S4_Lb1EEENS7_ISE_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeISA_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEENS_22__unordered_map_hasherIjNS_4pairIKjS9_EES4_S6_Lb1EEENS_21__unordered_map_equalIjSE_S6_S4_Lb1EEENS7_ISE_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEENS_22__unordered_map_hasherIjNS_4pairIKjS9_EES4_S6_Lb1EEENS_21__unordered_map_equalIjSE_S6_S4_Lb1EEENS7_ISE_EEEC2EOSJ_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEENS_22__unordered_map_hasherIjNS_4pairIKjS9_EES4_S6_Lb1EEENS_21__unordered_map_equalIjSE_S6_S4_Lb1EEENS7_ISE_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP19LSApplicationRecordEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP19LSApplicationRecordEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS5_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP19LSApplicationRecordEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE25__emplace_unique_key_argsIjJNS7_IjS4_EEEEENS7_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP19LSApplicationRecordEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP19LSApplicationRecordEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP19LSApplicationRecordEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS9_SD_SB_Lb1EEENS_9allocatorIS9_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP8NSStringEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP8NSStringEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS5_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP8NSStringEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRS8_EEENSO_IJEEEEEENS7_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP8NSStringEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP8NSStringEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS9_SD_SB_Lb1EEENS_9allocatorIS9_EEEC2EOSJ_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP8NSStringEENS_22__unordered_map_hasherIjNS_4pairIKjS4_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS9_SD_SB_Lb1EEENS_9allocatorIS9_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjbEENS_22__unordered_map_hasherIjNS_4pairIKjbEENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjbEENS_22__unordered_map_hasherIjNS_4pairIKjbEENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRS5_EEENSL_IJEEEEEENS4_INS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjbEENS_22__unordered_map_hasherIjNS_4pairIKjbEENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjbEENS_22__unordered_map_hasherIjNS_4pairIKjbEENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SA_S8_Lb1EEENS_9allocatorIS6_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjNS_4pairIKjjEENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjNS_4pairIKjjEENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE13__move_assignERSG_NS_17integral_constantIbLb1EEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjNS_4pairIKjjEENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIjJRS5_RjEEENS4_INS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjNS_4pairIKjjEENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE5clearEv
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjNS_4pairIKjjEENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjNS_4pairIKjjEENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SA_S8_Lb1EEENS_9allocatorIS6_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN14LaunchServices11OpenStaging20StagingDirectoryInfoEEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN14LaunchServices11OpenStaging20StagingDirectoryInfoEEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS5_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN14LaunchServices11OpenStaging20StagingDirectoryInfoEEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE25__emplace_unique_key_argsIyJRS8_S4_EEENS7_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN14LaunchServices11OpenStaging20StagingDirectoryInfoEEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE25__emplace_unique_key_argsIyJRyS4_EEENS7_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN14LaunchServices11OpenStaging20StagingDirectoryInfoEEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE4findIyEENS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN14LaunchServices11OpenStaging20StagingDirectoryInfoEEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS5_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN14LaunchServices11OpenStaging20StagingDirectoryInfoEEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN14LaunchServices11OpenStaging20StagingDirectoryInfoEEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS9_SD_SB_Lb1EEENS_9allocatorIS9_EEED2Ev
- __ZNSt3__112__hash_tableIP13objc_selectorNS_4hashIS2_EENS_8equal_toIS2_EENS_9allocatorIS2_EEE25__emplace_unique_key_argsIS2_JRKS2_EEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEEN14LaunchServices19MallocZoneAllocatorIjNS5_17BindingEvaluation17BindingMallocZoneEEEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIjPvEEEE
- __ZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEEN14LaunchServices19MallocZoneAllocatorIjNS5_17BindingEvaluation17BindingMallocZoneEEEE25__emplace_unique_key_argsIjJRKjEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIjPvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEE25__emplace_unique_key_argsIjJRKjEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIjPvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEE25__emplace_unique_key_argsIjJRjEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIjPvEEEEbEERKT_DpOT0_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqn210106ILi0EEEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqn210106INS_17basic_string_viewIcS2_EELi0EEERKT_
- __ZNSt3__113__tree_removeB9nqn210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__113unordered_mapIP13objc_selectorU8__strongP11objc_objectNS_4hashIS2_EENS_8equal_toIS2_EENS_9allocatorINS_4pairIKS2_S5_EEEEEC2ERKSF_
- __ZNSt3__113unordered_mapIPK20LSExtensionPointDatajZ27_LSEnumerateExtensionPointsE30_LSExtensionPointCxxComparatorS4_NS_9allocatorINS_4pairIKS3_jEEEEED1B9nqn210106Ev
- __ZNSt3__113unordered_mapIj38_LSDatabaseTableVisualizationFunctionsNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjS1_EEEEEC2ERKSB_
- __ZNSt3__113unordered_mapIyN14LaunchServices11OpenStaging20StagingDirectoryInfoENS_4hashIyEENS_8equal_toIyEENS_9allocatorINS_4pairIKyS3_EEEEE16insert_or_assignB9nqn210106IS3_EENS9_INS_19__hash_map_iteratorINS_15__hash_iteratorIPNS_11__hash_nodeINS_17__hash_value_typeIyS3_EEPvEEEEEEbEERSA_OT_
- __ZNSt3__114__split_bufferI9LSBindingRNS_9allocatorIS1_EEE17__destruct_at_endB9nqn210106EPS1_
- __ZNSt3__114__split_bufferIN14LaunchServices17BindingEvaluation15ExtendedBindingERNS1_19MallocZoneAllocatorIS3_NS2_17BindingMallocZoneEEEE5clearB9nqn210106Ev
- __ZNSt3__114__split_bufferINS_10shared_ptrIN14LaunchServices16PerThreadContextEEERNS_9allocatorIS4_EEE5clearB9nqn210106Ev
- __ZNSt3__114__split_bufferINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEERNS_9allocatorISD_EEE17__destruct_at_endB9nqn210106EPSD_
- __ZNSt3__115allocate_sharedB9nqn210106INS_6vectorINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEENS_9allocatorISE_EEEENSF_ISH_EEJRKSH_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB9nqn210106Ev
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B9nqn210106Ej
- __ZNSt3__116__pad_and_outputB9nqn210106IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__116__variant_detail12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE12__assign_altB9nqn210106ILm1ES5_RU8__strongKS4_EEvRNS0_5__altIXT_ET0_EEOT1_
- __ZNSt3__116__variant_detail12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE12__assign_altB9nqn210106ILm2ES8_RU8__strongKS7_EEvRNS0_5__altIXT_ET0_EEOT1_
- __ZNSt3__116__variant_detail12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE16__generic_assignB9nqn210106IRKNS0_17__copy_assignmentIS9_LNS0_6_TraitE1EEEEEvOT_
- __ZNSt3__116__variant_detail12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE9__emplaceB9nqn210106ILm1EJRU8__strongKS4_EEERDaDpOT0_
- __ZNSt3__116__variant_detail12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE9__emplaceB9nqn210106ILm2EJRU8__strongKS7_EEERDaDpOT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB9nqn210106IONS1_9__variant15__value_visitorIZN14LaunchServices20AppRecordEnumeration32VolumeContainerResolutionAdapter7resolveEP9LSContextEUlRKT_E_EEJRNS0_6__baseILNS0_6_TraitE1EJjU8__strongP5NSURLU8__strongP7NSErrorEEEEEEDcSD_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB9nqn210106IOZNS0_6__dtorINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEELNS0_6_TraitE1EE9__destroyB9nqn210106EvEUlRT_E_JRNS0_6__baseILSF_1EJjSA_SD_EEEEEEDcSH_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0ELm0EEE10__dispatchB9nqn210106IOZNS0_12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE16__generic_assignB9nqn210106IRKNS0_17__copy_assignmentISE_LNS0_6_TraitE1EEEEEvOT_EUlRSM_OT0_E_JRNS0_6__baseILSI_1EJjSA_SD_EEERKSU_EEEDcSM_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB9nqn210106IONS1_9__variant15__value_visitorIZN14LaunchServices20AppRecordEnumeration32VolumeContainerResolutionAdapter7resolveEP9LSContextEUlRKT_E_EEJRNS0_6__baseILNS0_6_TraitE1EJjU8__strongP5NSURLU8__strongP7NSErrorEEEEEEDcSD_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB9nqn210106IOZNS0_6__dtorINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEELNS0_6_TraitE1EE9__destroyB9nqn210106EvEUlRT_E_JRNS0_6__baseILSF_1EJjSA_SD_EEEEEEDcSH_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1ELm1EEE10__dispatchB9nqn210106IOZNS0_12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE16__generic_assignB9nqn210106IRKNS0_17__copy_assignmentISE_LNS0_6_TraitE1EEEEEvOT_EUlRSM_OT0_E_JRNS0_6__baseILSI_1EJjSA_SD_EEERKSU_EEEDcSM_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB9nqn210106IONS1_9__variant15__value_visitorIZN14LaunchServices20AppRecordEnumeration32VolumeContainerResolutionAdapter7resolveEP9LSContextEUlRKT_E_EEJRNS0_6__baseILNS0_6_TraitE1EJjU8__strongP5NSURLU8__strongP7NSErrorEEEEEEDcSD_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB9nqn210106IOZNS0_6__dtorINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEELNS0_6_TraitE1EE9__destroyB9nqn210106EvEUlRT_E_JRNS0_6__baseILSF_1EJjSA_SD_EEEEEEDcSH_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2ELm2EEE10__dispatchB9nqn210106IOZNS0_12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE16__generic_assignB9nqn210106IRKNS0_17__copy_assignmentISE_LNS0_6_TraitE1EEEEEvOT_EUlRSM_OT0_E_JRNS0_6__baseILSI_1EJjSA_SD_EEERKSU_EEEDcSM_DpT0_
- __ZNSt3__116__variant_detail12__visitation9__variant13__visit_valueB9nqn210106IZN14LaunchServices20AppRecordEnumeration32VolumeContainerResolutionAdapter7resolveEP9LSContextEUlRKT_E_JRNS_7variantIJjU8__strongP5NSURLU8__strongP7NSErrorEEEEEEDcOS9_DpOT0_
- __ZNSt3__116allocator_traitsIN14LaunchServices19MallocZoneAllocatorINS1_17BindingEvaluation15ExtendedBindingENS3_17BindingMallocZoneEEEE7destroyB9nqn210106IS4_Li0EEEvRS6_PT_
- __ZNSt3__116allocator_traitsIN14LaunchServices19MallocZoneAllocatorINS1_17BindingEvaluation15ExtendedBindingENS3_17BindingMallocZoneEEEE9constructB9nqn210106IS4_JRKS4_ELi0EEEvRS6_PT_DpOT0_
- __ZNSt3__116allocator_traitsIN14LaunchServices19MallocZoneAllocatorINS1_17BindingEvaluation15ExtendedBindingENS3_17BindingMallocZoneEEEE9constructB9nqn210106IS4_JRS4_ELi0EEEvRS6_PT_DpOT0_
- __ZNSt3__116allocator_traitsIN14LaunchServices19MallocZoneAllocatorINS1_17BindingEvaluation15ExtendedBindingENS3_17BindingMallocZoneEEEE9constructB9nqn210106IS4_JS4_ELi0EEEvRS6_PT_DpOT0_
- __ZNSt3__119__allocator_destroyB9nqn210106INS_9allocatorI9LSBindingEEPS2_S4_EEvRT_T0_T1_
- __ZNSt3__119__allocator_destroyB9nqn210106INS_9allocatorINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEEEEPSE_SG_EEvRT_T0_T1_
- __ZNSt3__119__shared_weak_count16__release_sharedB9nqn210106Ev
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqn210106Ev
- __ZNSt3__120__optional_copy_baseIN14LaunchServices16BindingEvaluatorELb0EEC2B9nqn210106ERKS3_
- __ZNSt3__120__shared_ptr_emplaceINS_6vectorINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEENS_9allocatorISE_EEEENSF_ISH_EEEC2B9nqn210106IJRKSH_ESI_Li0EEESI_DpOT_
- __ZNSt3__120back_insert_iteratorINS_6vectorIjNS_9allocatorIjEEEEEaSB9nqn210106EOj
- __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B9nqn210106EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B9nqn210106EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B9nqn210106EPKcm
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPvEEEEEclB9nqn210106EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIP17_opaque_pthread_tNS_10shared_ptrIN14LaunchServices16PerThreadContextEEEEEPvEEEEEclB9nqn210106EPSC_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIPKvNS_6vectorINS_4pairIP13objc_selectorPFvP11objc_objectS9_EEENS1_ISE_EEEEEEPvEEEEEclB9nqn210106EPSJ_
- __ZNSt3__123__optional_storage_baseI9LSBindingLb0EE13__assign_fromB9nqn210106INS_27__optional_move_assign_baseIS1_Lb0EEEEEvOT_
- __ZNSt3__123__optional_storage_baseIN14LaunchServices13TypeEvaluator6ResultELb0EE13__assign_fromB9nqn210106INS_27__optional_move_assign_baseIS3_Lb0EEEEEvOT_
- __ZNSt3__123__optional_storage_baseIU8__strongP12NSDictionaryIP8NSStringP11objc_objectELb0EE13__assign_fromB9nqn210106INS_27__optional_move_assign_baseIS8_Lb0EEEEEvOT_
- __ZNSt3__123__optional_storage_baseIU8__strongP8NSStringLb0EE13__assign_fromB9nqn210106INS_27__optional_move_assign_baseIS3_Lb0EEEEEvOT_
- __ZNSt3__124__put_character_sequenceB9nqn210106IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__125__throw_bad_function_callB9nqn210106Ev
- __ZNSt3__126__throw_bad_variant_accessB9nqn210106Ev
- __ZNSt3__127__insertion_sort_incompleteB9nqn210106INS_17_ClassicAlgPolicyERZ87+[LSApplicationRecord(UserActivity) applicationRecordsForUserActivityType:limit:error:]E3$_0PNS_4pairIjPK12LSBundleDataEEEEbT1_SA_T0_
- __ZNSt3__127__insertion_sort_incompleteB9nqn210106INS_17_ClassicAlgPolicyERZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]E3$_1PjEEbT1_S5_T0_
- __ZNSt3__127__insertion_sort_incompleteB9nqn210106INS_17_ClassicAlgPolicyERZL33_LSBundleCopyArchitectures_CommonPK12LSBundleDataP7NSArrayIP8NSStringEE3$_0P11LSSliceDataEEbT1_SE_T0_
- __ZNSt3__127__throw_bad_optional_accessB9nqn210106Ev
- __ZNSt3__127__tree_balance_after_insertB9nqn210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__134__uninitialized_allocator_relocateB9nqn210106IN14LaunchServices19MallocZoneAllocatorINS1_17BindingEvaluation15ExtendedBindingENS3_17BindingMallocZoneEEEPS4_EEvRT_T0_SA_SA_
- __ZNSt3__134__uninitialized_allocator_relocateB9nqn210106INS_9allocatorI9LSBindingEEPS2_EEvRT_T0_S7_S7_
- __ZNSt3__134__uninitialized_allocator_relocateB9nqn210106INS_9allocatorINS_4pairIU8__strongP8NSStringN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder20ProtoLocalizedStringEEEEEPSA_EEvRT_T0_SF_SF_
- __ZNSt3__134__uninitialized_allocator_relocateB9nqn210106INS_9allocatorIU6__weakP8LSRecordEEPS4_EEvRT_T0_S9_S9_
- __ZNSt3__135__uninitialized_allocator_copy_implB9nqn210106INS_9allocatorI9LSBindingEEPN14LaunchServices17BindingEvaluation15ExtendedBindingES7_PS2_EET2_RT_T0_T1_S9_
- __ZNSt3__135__uninitialized_allocator_copy_implB9nqn210106INS_9allocatorINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEEEEPSE_SG_SG_EET2_RT_T0_T1_SH_
- __ZNSt3__14swapB9nqn210106IN14LaunchServices17BindingEvaluation15ExtendedBindingEEENS_9enable_ifIXaasr21is_move_constructibleIT_EE5valuesr18is_move_assignableIS5_EE5valueEvE4typeERS5_S8_
- __ZNSt3__15arrayIU8__strongP8NSStringLm5EED1Ev
- __ZNSt3__16__findB9nqn210106IPU6__weakP8LSRecordS4_DnNS_10__identityEEET_S6_T0_RKT1_RT2_
- __ZNSt3__16__treeINS_12__value_typeI23os_eligibility_domain_t23os_eligibility_answer_tEENS_19__map_value_compareIS2_NS_4pairIKS2_S3_EENS_4lessIS2_EELb1EEENS_9allocatorIS8_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSJ_SJ_
- __ZNSt3__16__treeINS_12__value_typeI23os_eligibility_domain_t23os_eligibility_answer_tEENS_19__map_value_compareIS2_NS_4pairIKS2_S3_EENS_4lessIS2_EELb1EEENS_9allocatorIS8_EEE25__emplace_unique_key_argsIS2_JNS6_IS2_S3_EEEEENS6_INS_15__tree_iteratorIS4_PNS_11__tree_nodeIS4_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeI23os_eligibility_domain_t23os_eligibility_answer_tEENS_19__map_value_compareIS2_NS_4pairIKS2_S3_EENS_4lessIS2_EELb1EEENS_9allocatorIS8_EEE7destroyEPNS_11__tree_nodeIS4_PvEE
- __ZNSt3__16__treeINS_12__value_typeI23os_eligibility_domain_tN14LaunchServices7notifyd11NotifyTokenEEENS_19__map_value_compareIS2_NS_4pairIKS2_S5_EENS_4lessIS2_EELb1EEENS_9allocatorISA_EEE16__construct_nodeIJNS8_IS2_S5_EEEEENS_10unique_ptrINS_11__tree_nodeIS6_PvEENS_22__tree_node_destructorINSE_ISM_EEEEEEDpOT_
- __ZNSt3__16__treeINS_12__value_typeI23os_eligibility_domain_tN14LaunchServices7notifyd11NotifyTokenEEENS_19__map_value_compareIS2_NS_4pairIKS2_S5_EENS_4lessIS2_EELb1EEENS_9allocatorISA_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSL_SL_
- __ZNSt3__16__treeINS_12__value_typeI23os_eligibility_domain_tN14LaunchServices7notifyd11NotifyTokenEEENS_19__map_value_compareIS2_NS_4pairIKS2_S5_EENS_4lessIS2_EELb1EEENS_9allocatorISA_EEE25__emplace_unique_key_argsIS2_JNS8_IS2_S5_EEEEENS8_INS_15__tree_iteratorIS6_PNS_11__tree_nodeIS6_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeI23os_eligibility_domain_tN14LaunchServices7notifyd11NotifyTokenEEENS_19__map_value_compareIS2_NS_4pairIKS2_S5_EENS_4lessIS2_EELb1EEENS_9allocatorISA_EEE7destroyEPNS_11__tree_nodeIS6_PvEE
- __ZNSt3__16__treeINS_12__value_typeI23os_eligibility_domain_tNS_6vectorI23os_eligibility_answer_tNS_9allocatorIS4_EEEEEENS_19__map_value_compareIS2_NS_4pairIKS2_S7_EENS_4lessIS2_EELb1EEENS5_ISC_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSM_SM_
- __ZNSt3__16__treeINS_12__value_typeI23os_eligibility_domain_tNS_6vectorI23os_eligibility_answer_tNS_9allocatorIS4_EEEEEENS_19__map_value_compareIS2_NS_4pairIKS2_S7_EENS_4lessIS2_EELb1EEENS5_ISC_EEE25__emplace_unique_key_argsIS2_JRS2_S7_EEENSA_INS_15__tree_iteratorIS8_PNS_11__tree_nodeIS8_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeI23os_eligibility_domain_tNS_6vectorI23os_eligibility_answer_tNS_9allocatorIS4_EEEEEENS_19__map_value_compareIS2_NS_4pairIKS2_S7_EENS_4lessIS2_EELb1EEENS5_ISC_EEE7destroyEPNS_11__tree_nodeIS8_PvEE
- __ZNSt3__16__treeINS_12__value_typeIjU8__strongP8NSStringEENS_19__map_value_compareIjNS_4pairIKjS4_EENS_4lessIjEELb1EEENS_9allocatorIS9_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSK_SK_
- __ZNSt3__16__treeINS_12__value_typeIjU8__strongP8NSStringEENS_19__map_value_compareIjNS_4pairIKjS4_EENS_4lessIjEELb1EEENS_9allocatorIS9_EEE25__emplace_unique_key_argsIjJNS7_IjS4_EEEEENS7_INS_15__tree_iteratorIS5_PNS_11__tree_nodeIS5_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeIjU8__strongP8NSStringEENS_19__map_value_compareIjNS_4pairIKjS4_EENS_4lessIjEELb1EEENS_9allocatorIS9_EEE7destroyEPNS_11__tree_nodeIS5_PvEE
- __ZNSt3__16__treeINS_12__value_typeImU8__strongU13block_pointerFvvEEENS_19__map_value_compareImNS_4pairIKmS4_EENS_4lessImEELb1EEENS_9allocatorIS9_EEE14__erase_uniqueImEEmRKT_
- __ZNSt3__16__treeINS_12__value_typeImU8__strongU13block_pointerFvvEEENS_19__map_value_compareImNS_4pairIKmS4_EENS_4lessImEELb1EEENS_9allocatorIS9_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSK_SK_
- __ZNSt3__16__treeINS_12__value_typeImU8__strongU13block_pointerFvvEEENS_19__map_value_compareImNS_4pairIKmS4_EENS_4lessImEELb1EEENS_9allocatorIS9_EEE21__remove_node_pointerEPNS_11__tree_nodeIS5_PvEE
- __ZNSt3__16__treeINS_12__value_typeImU8__strongU13block_pointerFvvEEENS_19__map_value_compareImNS_4pairIKmS4_EENS_4lessImEELb1EEENS_9allocatorIS9_EEE25__emplace_unique_key_argsImJNS7_ImU8__strongP11objc_objectEEEEENS7_INS_15__tree_iteratorIS5_PNS_11__tree_nodeIS5_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeImU8__strongU13block_pointerFvvEEENS_19__map_value_compareImNS_4pairIKmS4_EENS_4lessImEELb1EEENS_9allocatorIS9_EEE5eraseENS_21__tree_const_iteratorIS5_PNS_11__tree_nodeIS5_PvEElEE
- __ZNSt3__16removeB9nqn210106INS_11__wrap_iterIPU6__weakP8LSRecordEEDnEET_S7_S7_RKT0_
- __ZNSt3__16vectorI11LSSliceDataNS_9allocatorIS1_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorI13LSBundleClassNS_9allocatorIS1_EEE11__vallocateB9nqn210106Em
- __ZNSt3__16vectorI13LSBundleClassNS_9allocatorIS1_EEE18__assign_with_sizeB9nqn210106IPKS1_S7_EEvT_T0_l
- __ZNSt3__16vectorI13LSBundleClassNS_9allocatorIS1_EEE18__assign_with_sizeB9nqn210106IPS1_S6_EEvT_T0_l
- __ZNSt3__16vectorI13LSBundleClassNS_9allocatorIS1_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorI13LSBundleClassNS_9allocatorIS1_EEE9push_backB9nqn210106EOS1_
- __ZNSt3__16vectorI13LSBundleClassNS_9allocatorIS1_EEEC2B9nqn210106ERKS4_
- __ZNSt3__16vectorI13LSPersonaTypeNS_9allocatorIS1_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorI23os_eligibility_answer_tNS_9allocatorIS1_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorI8_NSRangeNS_9allocatorIS1_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorI9LSBindingNS_9allocatorIS1_EEE16__destroy_vectorclB9nqn210106Ev
- __ZNSt3__16vectorI9LSBindingNS_9allocatorIS1_EEE18__insert_with_sizeB9nqn210106INS_11__wrap_iterIPN14LaunchServices17BindingEvaluation15ExtendedBindingEEESB_EENS6_IPS1_EENS6_IPKS1_EET_T0_l
- __ZNSt3__16vectorI9LSBindingNS_9allocatorIS1_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorI9LSBindingNS_9allocatorIS1_EEE27__insert_assign_n_uncheckedB9nqn210106INS_11__wrap_iterIPN14LaunchServices17BindingEvaluation15ExtendedBindingEEELi0EEEvT_lPS1_
- __ZNSt3__16vectorI9LSBindingNS_9allocatorIS1_EEE5clearB9nqn210106Ev
- __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS1_19MallocZoneAllocatorIS3_NS2_17BindingMallocZoneEEEE11__vallocateB9nqn210106Em
- __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS1_19MallocZoneAllocatorIS3_NS2_17BindingMallocZoneEEEE16__destroy_vectorclB9nqn210106Ev
- __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS1_19MallocZoneAllocatorIS3_NS2_17BindingMallocZoneEEEE16__init_with_sizeB9nqn210106INS_11__wrap_iterIPKS3_EESC_EEvT_T0_m
- __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS1_19MallocZoneAllocatorIS3_NS2_17BindingMallocZoneEEEE18__assign_with_sizeB9nqn210106IPKS3_SA_EEvT_T0_l
- __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS1_19MallocZoneAllocatorIS3_NS2_17BindingMallocZoneEEEE18__insert_with_sizeB9nqn210106INS_11__wrap_iterIPS3_EESB_EESB_NS9_IPKS3_EET_T0_l
- __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS1_19MallocZoneAllocatorIS3_NS2_17BindingMallocZoneEEEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS1_19MallocZoneAllocatorIS3_NS2_17BindingMallocZoneEEEE27__insert_assign_n_uncheckedB9nqn210106INS_11__wrap_iterIPS3_EELi0EEEvT_lSA_
- __ZNSt3__16vectorIN14LaunchServices17BindingEvaluation15ExtendedBindingENS1_19MallocZoneAllocatorIS3_NS2_17BindingMallocZoneEEEE9push_backB9nqn210106ERKS3_
- __ZNSt3__16vectorIN14LaunchServices30FeatureFlagPredicateEvaluation20FeatureFlagSpecifierENS_9allocatorIS3_EEE16__destroy_vectorclB9nqn210106Ev
- __ZNSt3__16vectorIN14LaunchServices30FeatureFlagPredicateEvaluation20FeatureFlagSpecifierENS_9allocatorIS3_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorIN14LaunchServices5Types41EnumeratedTypeUnitOrDynamicTypeIdentifierENS_9allocatorIS3_EEE16__destroy_vectorclB9nqn210106Ev
- __ZNSt3__16vectorIN14LaunchServices5Types41EnumeratedTypeUnitOrDynamicTypeIdentifierENS_9allocatorIS3_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorIN14LaunchServices5Types41EnumeratedTypeUnitOrDynamicTypeIdentifierENS_9allocatorIS3_EEE9push_backB9nqn210106ERKS3_
- __ZNSt3__16vectorINS_10shared_ptrIN14LaunchServices16PerThreadContextEEENS_9allocatorIS4_EEE16__destroy_vectorclB9nqn210106Ev
- __ZNSt3__16vectorINS_10shared_ptrIN14LaunchServices16PerThreadContextEEENS_9allocatorIS4_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorINS_10shared_ptrIN14LaunchServices16PerThreadContextEEENS_9allocatorIS4_EEE5clearB9nqn210106Ev
- __ZNSt3__16vectorINS_10shared_ptrIN14LaunchServices16PerThreadContextEEENS_9allocatorIS4_EEE9push_backB9nqn210106ERKS4_
- __ZNSt3__16vectorINS_4pairIP13objc_selectorPFvP11objc_objectS3_EEENS_9allocatorIS8_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder20ProtoLocalizedStringEEENS_9allocatorIS9_EEE16__destroy_vectorclB9nqn210106Ev
- __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder20ProtoLocalizedStringEEENS_9allocatorIS9_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder20ProtoLocalizedStringEEENS_9allocatorIS9_EEE5clearB9nqn210106Ev
- __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder20ProtoLocalizedStringEEENS_9allocatorIS9_EEE9push_backB9nqn210106EOS9_
- __ZNSt3__16vectorINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEENS_9allocatorISD_EEE11__vallocateB9nqn210106Em
- __ZNSt3__16vectorINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEENS_9allocatorISD_EEE16__destroy_vectorclB9nqn210106Ev
- __ZNSt3__16vectorINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEENS_9allocatorISD_EEE16__init_with_sizeB9nqn210106IPSD_SI_EEvT_T0_m
- __ZNSt3__16vectorINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEENS_9allocatorISD_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEENS_9allocatorISD_EEE5clearB9nqn210106Ev
- __ZNSt3__16vectorINS_4pairIjPK12LSBundleDataEENS_9allocatorIS5_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorINS_4pairIjU8__strongP6FSNodeEENS_9allocatorIS5_EEE16__destroy_vectorclB9nqn210106Ev
- __ZNSt3__16vectorINS_4pairIjU8__strongP6FSNodeEENS_9allocatorIS5_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorINS_4pairIjU8__strongP6NSUUIDEENS_9allocatorIS5_EEE16__destroy_vectorclB9nqn210106Ev
- __ZNSt3__16vectorINS_4pairIjU8__strongP6NSUUIDEENS_9allocatorIS5_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorINS_4pairIjU8__strongP6NSUUIDEENS_9allocatorIS5_EEE9push_backB9nqn210106EOS5_
- __ZNSt3__16vectorINS_5tupleIJU8__strongP8NSStringjEEENS_9allocatorIS5_EEE16__destroy_vectorclB9nqn210106Ev
- __ZNSt3__16vectorINS_5tupleIJU8__strongP8NSStringjEEENS_9allocatorIS5_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorINS_5tupleIJU8__strongP8NSStringjEEENS_9allocatorIS5_EEE9push_backB9nqn210106EOS5_
- __ZNSt3__16vectorIP8LSRecordNS_9allocatorIS3_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorIP8LSRecordNS_9allocatorIS3_EEE8__appendEmRKS2_
- __ZNSt3__16vectorIPK10__CFStringNS_9allocatorIS3_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE11__vallocateB9nqn210106Em
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorIPvNS_9allocatorIS1_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorIPvNS_9allocatorIS1_EEE8__appendEm
- __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE11__vallocateB9nqn210106Em
- __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE16__destroy_vectorclB9nqn210106Ev
- __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE16__init_with_sizeB9nqn210106IPKS2_S9_EEvT_T0_m
- __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE16__init_with_sizeB9nqn210106IPS3_S8_EEvT_T0_m
- __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE18__insert_with_sizeB9nqn210106IPKS2_S9_EENS_11__wrap_iterIPS3_EENSA_IPU6__weakKS2_EET_T0_l
- __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorIU6__weakP8LSRecordNS_9allocatorIS3_EEE27__insert_assign_n_uncheckedB9nqn210106IPKS2_Li0EEEvT_lPS3_
- __ZNSt3__16vectorIU8__strongP19LSApplicationRecordNS_9allocatorIS3_EEE16__destroy_vectorclB9nqn210106Ev
- __ZNSt3__16vectorIU8__strongP19LSApplicationRecordNS_9allocatorIS3_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEE16__destroy_vectorclB9nqn210106Ev
- __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorIU8__strongU13block_pointerFvbP11_LSDatabaseP7NSErrorENS_9allocatorIS7_EEE16__destroy_vectorclB9nqn210106Ev
- __ZNSt3__16vectorIU8__strongU13block_pointerFvbP11_LSDatabaseP7NSErrorENS_9allocatorIS7_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorIU8__strongU13block_pointerFvvENS_9allocatorIS3_EEE11__vallocateB9nqn210106Em
- __ZNSt3__16vectorIU8__strongU13block_pointerFvvENS_9allocatorIS3_EEE16__destroy_vectorclB9nqn210106Ev
- __ZNSt3__16vectorIU8__strongU13block_pointerFvvENS_9allocatorIS3_EEE16__init_with_sizeB9nqn210106IPS3_S8_EEvT_T0_m
- __ZNSt3__16vectorIU8__strongU13block_pointerFvvENS_9allocatorIS3_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorIU8__strongU13block_pointerFvvENS_9allocatorIS3_EEE9push_backB9nqn210106ERU8__strongKS2_
- __ZNSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorIcNS_9allocatorIcEEE9push_backB9nqn210106EOc
- __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB9nqn210106Em
- __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorIiNS_9allocatorIiEEE8__appendEm
- __ZNSt3__16vectorIjNS_9allocatorIjEEE11__vallocateB9nqn210106Em
- __ZNSt3__16vectorIjNS_9allocatorIjEEE18__assign_with_sizeB9nqn210106IPjS5_EEvT_T0_l
- __ZNSt3__16vectorIjNS_9allocatorIjEEE18__insert_with_sizeB9nqn210106INS_11__wrap_iterIPjEES7_EES7_NS5_IPKjEET_T0_l
- __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorIjNS_9allocatorIjEEE9push_backB9nqn210106EOj
- __ZNSt3__16vectorIjNS_9allocatorIjEEE9push_backB9nqn210106ERKj
- __ZNSt3__16vectorIjNS_9allocatorIjEEEC2B9nqn210106ERKS3_
- __ZNSt3__16vectorItNS_9allocatorItEEE11__vallocateB9nqn210106Em
- __ZNSt3__16vectorItNS_9allocatorItEEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__17__sort3B9nqn210106INS_17_ClassicAlgPolicyERZ87+[LSApplicationRecord(UserActivity) applicationRecordsForUserActivityType:limit:error:]E3$_0PNS_4pairIjPK12LSBundleDataEELi0EEEbT1_SA_SA_T0_
- __ZNSt3__17__sort3B9nqn210106INS_17_ClassicAlgPolicyERZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]E3$_1PjLi0EEEbT1_S5_S5_T0_
- __ZNSt3__17__sort4B9nqn210106INS_17_ClassicAlgPolicyERZ87+[LSApplicationRecord(UserActivity) applicationRecordsForUserActivityType:limit:error:]E3$_0PNS_4pairIjPK12LSBundleDataEELi0EEEvT1_SA_SA_SA_T0_
- __ZNSt3__17__sort4B9nqn210106INS_17_ClassicAlgPolicyERZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]E3$_1PjLi0EEEvT1_S5_S5_S5_T0_
- __ZNSt3__17__sort4B9nqn210106INS_17_ClassicAlgPolicyERZL33_LSBundleCopyArchitectures_CommonPK12LSBundleDataP7NSArrayIP8NSStringEE3$_0P11LSSliceDataLi0EEEvT1_SE_SE_SE_T0_
- __ZNSt3__17__sort5B9nqn210106INS_17_ClassicAlgPolicyERZ87+[LSApplicationRecord(UserActivity) applicationRecordsForUserActivityType:limit:error:]E3$_0PNS_4pairIjPK12LSBundleDataEELi0EEEvT1_SA_SA_SA_SA_T0_
- __ZNSt3__17__sort5B9nqn210106INS_17_ClassicAlgPolicyERZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]E3$_1PjLi0EEEvT1_S5_S5_S5_S5_T0_
- __ZNSt3__17__sort5B9nqn210106INS_17_ClassicAlgPolicyERZL33_LSBundleCopyArchitectures_CommonPK12LSBundleDataP7NSArrayIP8NSStringEE3$_0P11LSSliceDataLi0EEEvT1_SE_SE_SE_SE_T0_
- __ZNSt3__18__invokeB9nqn210106IJZNS_16__variant_detail12__assignmentINS1_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE16__generic_assignB9nqn210106IRKNS1_17__copy_assignmentISA_LNS1_6_TraitE1EEEEEvOT_EUlRSI_OT0_E_RNS1_5__altILm0EjEERKSP_EEENS_20__invoke_result_implIvJDpT_EE4typeEDpOSU_
- __ZNSt3__18optionalI9LSBindingEaSB9nqn210106IRKN14LaunchServices17BindingEvaluation15ExtendedBindingELi0EEERS2_OT_
- __ZNSt3__18optionalI9LSBindingEaSB9nqn210106IS1_Li0EEERS2_OT_
- __ZNSt3__18optionalIN14LaunchServices11OpenStaging20StagingDirectoryInfoEE7emplaceB9nqn210106IJRU8__strongP8NSStringRU8__strongP6FSNodeRxELi0EEERS3_DpOT_
- __ZNSt3__18optionalIN14LaunchServices16BindingEvaluatorEEaSB9nqn210106IS2_Li0EEERS3_OT_
- __ZNSt3__18optionalIN14LaunchServices16EligibilityCache11NotifyStateEE7emplaceB9nqn210106IJU8__strongU13block_pointerFvvEELi0EEERS3_DpOT_
- __ZNSt3__18optionalIN14LaunchServices30EligibilityPredicateEvaluation9PredicateEE7emplaceB9nqn210106IJS3_ELi0EEERS3_DpOT_
- __ZNSt3__18optionalIN14LaunchServices30FeatureFlagPredicateEvaluation9PredicateEE7emplaceB9nqn210106IJS3_ELi0EEERS3_DpOT_
- __ZNSt3__18optionalIU8__strongP7NSErrorEaSB9nqn210106IRS3_Li0EEERS4_OT_
- __ZNSt3__19allocatorI11LSSliceDataE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorI13LSBundleClassE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorI13LSPersonaTypeE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorI23os_eligibility_answer_tE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorI8_NSRangeE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorI9LSBindingE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorIN14LaunchServices30FeatureFlagPredicateEvaluation20FeatureFlagSpecifierEE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorIN14LaunchServices5Types41EnumeratedTypeUnitOrDynamicTypeIdentifierEE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorINS_10shared_ptrIN14LaunchServices16PerThreadContextEEEE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorINS_4pairIP13objc_selectorPFvP11objc_objectS3_EEEE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorINS_4pairIU8__strongP8NSStringN14LaunchServices10BaseBundle43ContextualUsageDescriptionDictionaryBuilder20ProtoLocalizedStringEEEE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorINS_4pairIU8__strongU13block_pointerFbP9LSContextRK9LSBindingEU8__strongP8NSStringEEE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorINS_4pairIjPK12LSBundleDataEEE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorINS_4pairIjU8__strongP6FSNodeEEE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorINS_4pairIjU8__strongP6NSUUIDEEE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorINS_5tupleIJU8__strongP8NSStringjEEEE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorIP8LSRecordE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorIPK10__CFStringE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorIPKvE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorIPvE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorIU6__weakP8LSRecordE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorIU8__strongP19LSApplicationRecordE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorIU8__strongP8NSStringE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorIU8__strongU13block_pointerFvbP11_LSDatabaseP7NSErrorEE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorIU8__strongU13block_pointerFvvEE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorIiE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorIjE17allocate_at_leastB9nqn210106Em
- __ZNSt3__19allocatorItE17allocate_at_leastB9nqn210106Em
- __ZSt28__throw_bad_array_new_lengthB9nqn210106v
- __ZTVNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore removeEntriesForBundleIdentifier:]E3$_1FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EEE
- __ZTVNSt3__110__function6__funcIZ77-[LSDefaultApplicationQueryServerDatastore setEntry:forApplication:category:]E3$_0FN12_GLOBAL__N_130LSDefaultApplicationQueryStateES4_EEE
- __ZZ26_LSDatabaseGetSeedingGroupE12seedingGroup
- __ZZ26_LSDatabaseGetSeedingGroupE4once
- __ZZ48+[LSBundleRecord _getBundleRecordFinderForNode:]EN3$_08__invokeERN14LaunchServices8Database7ContextEP6FSNodePU15__autoreleasingP7NSError
- __ZZ52+[LSApplicationRecord(Redaction) redactedProperties]E10properties
- __ZZ52+[LSApplicationRecord(Redaction) redactedProperties]E4once
- __ZZ60+[LSApplicationRecord(Identities) personalPersonaAttributes]E4once
- __ZZ60+[LSApplicationRecord(Identities) personalPersonaAttributes]E6result
- __ZZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]EN3$_015getAndCacheNameEj
- __ZZ98+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]EN3$_015getAndCacheNameEj.cold.1
- __ZZL35enumerateProductPlatformKeySuffixesIU8__strongP12NSDictionaryIP8NSStringP11objc_objectEZ53-[_LSStringsFileContent subscriptLoctableWithLocale:]E3$_1ENSt3__18optionalIT_EES2_RKT0_E25platformThenProductSuffix
- __ZZL35enumerateProductPlatformKeySuffixesIU8__strongP12NSDictionaryIP8NSStringP11objc_objectEZ53-[_LSStringsFileContent subscriptLoctableWithLocale:]E3$_1ENSt3__18optionalIT_EES2_RKT0_E25productThenPlatformSuffix
- __ZZL35enumerateProductPlatformKeySuffixesIU8__strongP12NSDictionaryIP8NSStringP11objc_objectEZ53-[_LSStringsFileContent subscriptLoctableWithLocale:]E3$_1ENSt3__18optionalIT_EES2_RKT0_E9onceToken
- __ZZL35enumerateProductPlatformKeySuffixesIU8__strongP8NSStringZ60-[_LSStringsFileContent _queryLoadedPlist:forRawKey:locale:]E3$_2ENSt3__18optionalIT_EES1_RKT0_E25platformThenProductSuffix
- __ZZL35enumerateProductPlatformKeySuffixesIU8__strongP8NSStringZ60-[_LSStringsFileContent _queryLoadedPlist:forRawKey:locale:]E3$_2ENSt3__18optionalIT_EES1_RKT0_E25productThenPlatformSuffix
- __ZZL35enumerateProductPlatformKeySuffixesIU8__strongP8NSStringZ60-[_LSStringsFileContent _queryLoadedPlist:forRawKey:locale:]E3$_2ENSt3__18optionalIT_EES1_RKT0_E9onceToken
- __ZZZL37_LSSchemeApprovalGetBouncebackHistoryvEUb_E14backlightToken
- ___101-[_LSInstallProgressService createInstallProgressForApplication:withPhase:andPublishingString:reply:]_block_invoke.269
- ___104-[_LSDModifyClient registerItemInfo:alias:diskImageAlias:bundleURL:installationPlist:completionHandler:]_block_invoke
- ___104-[_LSDModifyClient registerItemInfo:alias:diskImageAlias:bundleURL:installationPlist:completionHandler:]_block_invoke.168
- ___107+[LSDocumentProxy(Binding) _bindingEvaluatorResultFilterForBindingStyle:contentIsManaged:sourceAuditToken:]_block_invoke
- ___107+[LSDocumentProxy(Binding) _bindingEvaluatorResultFilterForBindingStyle:contentIsManaged:sourceAuditToken:]_block_invoke.142
- ___107+[LSDocumentProxy(Binding) _bindingEvaluatorResultFilterForBindingStyle:contentIsManaged:sourceAuditToken:]_block_invoke.144
- ___111-[_LSCanOpenURLManager(PrivateSchemeChecking) legacy_isBundleID:bundleData:context:allowedToCheckScheme:error:]_block_invoke.74
- ___120-[_LSDDeviceIdentifierClient getClientProcessVendorNameBundleIdentifierAndRestrictedIDAccessWithType:completionHandler:]_block_invoke.56
- ___130-[LSApplicationWorkspace registerApplicationForRebuildWithInfoDictionaries:personaUniqueStrings:requestContext:registrationError:]_block_invoke
- ___130-[LSApplicationWorkspace registerApplicationForRebuildWithInfoDictionaries:personaUniqueStrings:requestContext:registrationError:]_block_invoke_2
- ___135-[LSApplicationWorkspace setPersonaUniqueStrings:forApplicationsWithBundleIdentifiers:operationUUID:requestContext:saveObserver:error:]_block_invoke
- ___135-[LSApplicationWorkspace setPersonaUniqueStrings:forApplicationsWithBundleIdentifiers:operationUUID:requestContext:saveObserver:error:]_block_invoke_2
- ___160-[LSApplicationWorkspace registerContainerizedApplicationWithInfoDictionaries:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:]_block_invoke
- ___160-[LSApplicationWorkspace registerContainerizedApplicationWithInfoDictionaries:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:]_block_invoke_2
- ___175-[LSBundleProxy _initWithBundleUnit:context:bundleType:bundleID:localizedName:bundleContainerURL:dataContainerURL:resourcesDirectoryURL:iconsDictionary:iconFileNames:version:]_block_invoke
- ___37-[LSSettingsStore addChangeObserver:]_block_invoke.41
- ___42-[LSDocumentProxy(Binding) _boundIconInfo]_block_invoke.161
- ___42-[LSMIResultRegistrant runWithCompletion:]_block_invoke.107
- ___44-[LSMIResultUnregistrant runWithCompletion:]_block_invoke.141
- ___45-[LSApplicationWorkspace establishConnection]_block_invoke.189
- ___45-[LSApplicationWorkspace establishConnection]_block_invoke.192
- ___45-[LSApplicationWorkspace establishConnection]_block_invoke.197
- ___45-[LSApplicationWorkspace establishConnection]_block_invoke.203
- ___45-[LSApplicationWorkspace establishConnection]_block_invoke.209
- ___45-[LSApplicationWorkspace establishConnection]_block_invoke_2.200
- ___46-[LSRebuildStatisticsGatherer submitAnalytics]_block_invoke.21
- ___47-[LSBundleRecordBuilder buildBundleData:error:]_block_invoke.712
- ___47-[LSByURLBundleUnregistrant runWithCompletion:]_block_invoke.159
- ___47-[LSByURLPluginUnregistrant runWithCompletion:]_block_invoke.177
- ___48-[LSDatabaseBuilder createAndSeedLocalDatabase:]_block_invoke.1
- ___48-[LSDatabaseBuilder createAndSeedLocalDatabase:]_block_invoke.cold.1
- ___50-[_LSDiskUsage(Private) fetchClientSideWithError:]_block_invoke.145
- ___51-[LSApplicationWorkspace deviceIdentifierForVendor]_block_invoke.376
- ___51-[LSApplicationWorkspace deviceIdentifierForVendor]_block_invoke.376.cold.1
- ___52+[LSApplicationRecord(Redaction) redactedProperties]_block_invoke
- ___52-[_LSInstallProgressService restoreInactiveInstalls]_block_invoke.217
- ___52-[_LSInstallProgressService restoreInactiveInstalls]_block_invoke.217.cold.1
- ___54-[_LSClientSettingsStore resetUserElectionsWithError:]_block_invoke.223
- ___54-[_LSClientSettingsStore resetUserElectionsWithError:]_block_invoke.223.cold.1
- ___54-[_LSClientSettingsStore userElectionForExtensionKey:]_block_invoke.220
- ___54-[_LSClientSettingsStore userElectionForExtensionKey:]_block_invoke.220.cold.1
- ___55-[LSApplicationRestrictionsManager restrictedBundleIDs]_block_invoke
- ___55-[LSApplicationWorkspace _LSPrivateNoteMigratorRunning]_block_invoke.402
- ___55-[LSApplicationWorkspace _LSPrivateNoteMigratorRunning]_block_invoke.402.cold.1
- ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.648
- ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.648.cold.1
- ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.649
- ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.649.cold.1
- ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.649.cold.2
- ___56-[LSApplicationRestrictionsManager allowlistedBundleIDs]_block_invoke
- ___56-[LSApplicationWorkspace deviceIdentifierForAdvertising]_block_invoke.373
- ___56-[LSApplicationWorkspace deviceIdentifierForAdvertising]_block_invoke.373.cold.1
- ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.309
- ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.312
- ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.315
- ___59-[_LSXPCQueryResolver _resolveQueries:XPCConnection:error:]_block_invoke.137
- ___59-[_LSXPCQueryResolver _resolveQueries:XPCConnection:error:]_block_invoke.137.cold.1
- ___60+[LSApplicationRecord(Identities) personalPersonaAttributes]_block_invoke
- ___60-[LSApplicationRestrictionsManager beginListeningForChanges]_block_invoke.114
- ___61-[LSSystemExtensionPointRefreshRegistrant runWithCompletion:]_block_invoke.217
- ___64-[LSApplicationRestrictionsManager ratingRankExceptionBundleIDs]_block_invoke
- ___64-[LSApplicationWorkspace scanForAppsInRatingRankExceptionsList:]_block_invoke
- ___64-[LSApplicationWorkspace scanForAppsInRatingRankExceptionsList:]_block_invoke.cold.1
- ___64-[_LSClientSettingsStore setUserElection:forExtensionKey:error:]_block_invoke.222
- ___64-[_LSClientSettingsStore setUserElection:forExtensionKey:error:]_block_invoke.222.cold.1
- ___64-[_LSInstallProgressService loadJournalledNotificationsFromDisk]_block_invoke.342
- ___65-[_LSClientSettingsStore __internalQueue_xpcConnectionWithError:]_block_invoke.217
- ___65-[_LSClientSettingsStore __internalQueue_xpcConnectionWithError:]_block_invoke.217.cold.1
- ___65-[_LSClientSettingsStore __internalQueue_xpcConnectionWithError:]_block_invoke.219
- ___66-[LSApplicationWorkspace installProgressForApplication:withPhase:]_block_invoke.385
- ___67-[LSApplicationRecord(UniqueIdentifiers) deviceIdentifierForVendor]_block_invoke.517
- ___68-[LSApplicationRestrictionsManager handleMCEffectiveSettingsChanged]_block_invoke.122
- ___68-[LSApplicationRestrictionsManager handleMCEffectiveSettingsChanged]_block_invoke.123
- ___68-[LSApplicationWorkspace urlContainsDeviceIdentifierForAdvertising:]_block_invoke.377
- ___68-[LSApplicationWorkspaceRemoteObserver applicationInstallsDidStart:]_block_invoke.760
- ___69-[LSApplicationWorkspace installProgressForBundleID:makeSynchronous:]_block_invoke.380
- ___69-[LSApplicationWorkspace installProgressForBundleID:makeSynchronous:]_block_invoke.381
- ___69-[LSApplicationWorkspace installProgressForBundleID:makeSynchronous:]_block_invoke.382
- ___70-[LSApplicationWorkspace scanForApplicationStateChangesWithAllowlist:]_block_invoke_2
- ___72-[LSApplicationRecord(UniqueIdentifiers) deviceIdentifierForAdvertising]_block_invoke.519
- ___73-[LSApplicationRestrictionsManager _pruneObsoleteTrustedSignerIdentities]_block_invoke.124
- ___74-[UTTypeRecord _enumerateRelatedTypesWithMaximumDegreeOfSeparation:block:]_block_invoke.30
- ___74-[UTTypeRecord _enumerateRelatedTypesWithMaximumDegreeOfSeparation:block:]_block_invoke.30.cold.1
- ___75-[_LSDModifyClient unregisterApplicationsAtMountPoint:operationUUID:reply:]_block_invoke.249
- ___75-[_LSDModifyClient unregisterApplicationsAtMountPoint:operationUUID:reply:]_block_invoke.254
- ___76-[_LSInstallProgressService addSendNotificationFenceWithTimeout:fenceBlock:]_block_invoke.337
- ___78-[LSApplicationRecord(AlternateIcons) setAlternateIconName:completionHandler:]_block_invoke.639
- ___78-[LSApplicationRecord(AlternateIcons) setAlternateIconName:completionHandler:]_block_invoke.639.cold.1
- ___79-[_LSInstallProgressService sendNotification:forAppProxies:Plugins:completion:]_block_invoke.322
- ___83-[LSApplicationRecord _personasWithAttributesWithContext:tableID:unitID:unitBytes:]_block_invoke
- ___84-[_LSDModifyClient setPreferenceValue:forKey:forApplicationAtURL:completionHandler:]_block_invoke.289
- ___85-[LSApplicationRecord(Localization) localizedNameWithContext:preferredLocalizations:]_block_invoke
- ___85-[LSApplicationRecord(Localization) localizedNameWithContext:preferredLocalizations:]_block_invoke_2
- ___85-[LSApplicationRecord(Localization) localizedNameWithContext:preferredLocalizations:]_block_invoke_3
- ___86-[LSApplicationRecord(AlternateIcons) setAlternateIconNameSilently:completionHandler:]_block_invoke.646
- ___86-[LSApplicationRecord(AlternateIcons) setAlternateIconNameSilently:completionHandler:]_block_invoke.646.cold.1
- ___88-[_LSDModifyClient registerBuiltinApplication:personaUniqueStrings:operationUUID:reply:]_block_invoke
- ___88-[_LSDModifyClient registerBuiltinApplication:personaUniqueStrings:operationUUID:reply:]_block_invoke.cold.1
- ___89-[LSApplicationRestrictionsManager scanForMissedNotificationsForImportantAppsIfNecessary]_block_invoke.113
- ___95-[LSApplicationWorkspace _LSPrivateRebuildApplicationDatabasesForSystemApps:internal:user:uid:]_block_invoke.397
- ___97-[_LSDModifyClient performPostInstallationRegistration:personaUniqueStrings:operationUUID:reply:]_block_invoke
- ___97-[_LSDModifyClient performPostInstallationRegistration:personaUniqueStrings:operationUUID:reply:]_block_invoke.cold.1
- ___97-[_LSDModifyClient performPostInstallationRegistration:personaUniqueStrings:operationUUID:reply:]_block_invoke_2
- ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.319
- ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.319.cold.1
- ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.320
- ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.320.cold.1
- ___98-[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:operationUUID:reply:]_block_invoke
- ___98-[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:operationUUID:reply:]_block_invoke.308
- ___98-[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:operationUUID:reply:]_block_invoke.cold.1
- ___98-[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:operationUUID:reply:]_block_invoke.cold.2
- ___Block_byref_object_copy_.1018
- ___Block_byref_object_copy_.1200
- ___Block_byref_object_copy_.134
- ___Block_byref_object_copy_.136
- ___Block_byref_object_copy_.142
- ___Block_byref_object_copy_.162
- ___Block_byref_object_copy_.165
- ___Block_byref_object_copy_.198
- ___Block_byref_object_copy_.23
- ___Block_byref_object_copy_.260
- ___Block_byref_object_copy_.28
- ___Block_byref_object_copy_.286
- ___Block_byref_object_copy_.335
- ___Block_byref_object_copy_.367
- ___Block_byref_object_copy_.388
- ___Block_byref_object_copy_.623
- ___Block_byref_object_copy_.694
- ___Block_byref_object_copy_.80
- ___Block_byref_object_dispose_.1019
- ___Block_byref_object_dispose_.1201
- ___Block_byref_object_dispose_.135
- ___Block_byref_object_dispose_.137
- ___Block_byref_object_dispose_.143
- ___Block_byref_object_dispose_.163
- ___Block_byref_object_dispose_.166
- ___Block_byref_object_dispose_.199
- ___Block_byref_object_dispose_.24
- ___Block_byref_object_dispose_.261
- ___Block_byref_object_dispose_.287
- ___Block_byref_object_dispose_.29
- ___Block_byref_object_dispose_.336
- ___Block_byref_object_dispose_.368
- ___Block_byref_object_dispose_.389
- ___Block_byref_object_dispose_.624
- ___Block_byref_object_dispose_.695
- ___Block_byref_object_dispose_.81
- ____LSCopyGroupContainerIdentifiersFromEntitlements_block_invoke
- ____LSCopyRationalizedEnvironmentVariablesDict_block_invoke
- ____LSDatabaseGetSeedingGroup_block_invoke
- ____LSGetCollapsedMIDictionaryForAppAndContentsDictionaries_block_invoke
- ____LSGetCollapsedMIDictionaryForAppAndContentsDictionaries_block_invoke_2
- ____LSResetServer_block_invoke.127
- ____LSResetServer_block_invoke.127.cold.1
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.946
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.946.cold.1
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.950
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.950.cold.1
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.953
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.948
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.951
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.955
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.955.cold.1
- ____LSServer_RefreshContentInFrameworkAtURL_block_invoke_2
- ____LSServer_SyncWithMobileInstallation_block_invoke.1020
- ____LSServer_SyncWithMobileInstallation_block_invoke_2.1021
- ____LSServer_SyncWithMobileInstallation_block_invoke_3.cold.1
- ____LSServer_SyncWithMobileInstallation_block_invoke_3.cold.2
- ____LSServer_SyncWithMobileInstallation_block_invoke_6
- ____LSUnregisterBundle_block_invoke.186
- ____ZL17_LSRegisterPluginP11_LSDatabaseRK12LSPluginInfoPK14__CFDictionaryPK10__CFStringS9_S6_jPj_block_invoke
- ____ZL23_LSOpenOperationPerformP5NSURLP12NSFileHandleP8NSStringbS4_P12NSDictionaryIS4_P11objc_objectES9_PU42objcproto31LSOpenResourceOperationDelegate11objc_objectP15NSXPCConnectionU13block_pointerFvbP7NSErrorE_block_invoke.116
- ____ZL23_LSOpenOperationPerformP5NSURLP12NSFileHandleP8NSStringbS4_P12NSDictionaryIS4_P11objc_objectES9_PU42objcproto31LSOpenResourceOperationDelegate11objc_objectP15NSXPCConnectionU13block_pointerFvbP7NSErrorE_block_invoke.116.cold.1
- ____ZL23_LSUpdateDefaultHandlerP18LSApplicationProxyP5NSURL_block_invoke.160
- ____ZL23_LSUpdateDefaultHandlerP18LSApplicationProxyP5NSURL_block_invoke.160.cold.1
- ____ZL25_LSPluginRegisterWithInfoP11_LSDatabasePK14__CFDictionaryS3_hPS1_jj_block_invoke
- ____ZL25_LSPluginRegisterWithInfoP11_LSDatabasePK14__CFDictionaryS3_hPS1_jj_block_invoke_2
- ____ZL26_LSArmSaveTimerWithTimeouthdU13block_pointerFvbP11_LSDatabaseP7NSErrorE_block_invoke.394
- ____ZL29pluginKitUserElectionStoreURLv_block_invoke.250
- ____ZL29pluginKitUserElectionStoreURLv_block_invoke.250.cold.1
- ____ZL29pluginKitUserElectionStoreURLv_block_invoke.250.cold.2
- ____ZL31createInstallationDictForPluginPK10__CFString_block_invoke
- ____ZL34LSCheckDatabaseAvailableWithServerP17_LSDServiceDomain_block_invoke.382
- ____ZL34_LSCreateRegistrationDataForBundleP9LSContextP18LSRegistrationInfoPK7__CFURLPK14__CFDictionaryPPK9__CFArray_block_invoke
- ____ZL35enumerateProductPlatformKeySuffixesIU8__strongP12NSDictionaryIP8NSStringP11objc_objectEZ53-[_LSStringsFileContent subscriptLoctableWithLocale:]E3$_1ENSt3__18optionalIT_EES2_RKT0__block_invoke
- ____ZL35enumerateProductPlatformKeySuffixesIU8__strongP8NSStringZ60-[_LSStringsFileContent _queryLoadedPlist:forRawKey:locale:]E3$_2ENSt3__18optionalIT_EES1_RKT0__block_invoke
- ____ZL37_LSSchemeApprovalGetBouncebackHistoryv_block_invoke.cold.1
- ____ZL37_LSSchemeApprovalGetBouncebackHistoryv_block_invoke_3
- ____ZL41_LSSystemContentDatabaseSanitizeForExportP11_LSDatabase_block_invoke.cold.2
- ____ZL41_LSSystemContentDatabaseSanitizeForExportP11_LSDatabase_block_invoke.cold.3
- ____ZL41_LSSystemContentDatabaseSanitizeForExportP11_LSDatabase_block_invoke_2.cold.2
- ____ZL45sendPersonaChangedNotificationsForIdentifiersP9LSContextP5NSSetIP8NSStringE_block_invoke
- ____ZL78_LSGetDefaultPreferredLocalizationsWithFallbackForImproperlyLocalizedProcessesv_block_invoke.43
- ____ZN14LaunchServices12URLOverridesL20getURLOverrideCommonEP5NSURL_block_invoke.233
- ____ZN14LaunchServices12URLOverridesL20getURLOverrideCommonEP5NSURL_block_invoke.233.cold.1
- ____ZN14LaunchServices12URLOverridesL20getURLOverrideCommonEP5NSURL_block_invoke.233.cold.2
- ____ZN14LaunchServices19URLPropertyProviderL43beginTranslatingHiddenBySystemNotificationsEv_block_invoke.63
- ____ZN14LaunchServices19URLPropertyProviderL43beginTranslatingHiddenBySystemNotificationsEv_block_invoke.69
- ____ZZ31-[LSRecord compatibilityObject]ENK3$_0clEP9LSContextjjPKv_block_invoke
- ___block_descriptor_114_ea8_32s40s48s56s64s72s80s88s96s104bs_e48_v16?0"<LSRegistrantDatabaseContextProviding>"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
- ___block_descriptor_32_e25_v32?0"NSNumber"816^B24l
- ___block_descriptor_32_e26_v16?0"FBSDisplayLayout"8l
- ___block_descriptor_32_e379_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20l
- ___block_descriptor_40_ea8_32s_e379_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20ls32l8
- ___block_descriptor_40_ea8_32s_e379_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20ls32l8
- ___block_descriptor_44_e379_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20l
- ___block_descriptor_48_e8_32s40s_e27_v24?0"LSBundleProxy"8^B16ls32l8s40l8
- ___block_descriptor_48_ea8_32bs_e196_v28?0"NSString"8I16r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20ls32l8
- ___block_descriptor_48_ea8_32bs_e376_v28?0"NSString"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20ls32l8
- ___block_descriptor_48_ea8_32r40r_e29_v32?0"NSDictionary"8Q16^B24lr32l8r40l8
- ___block_descriptor_48_ea8_32rc_e34_v24?0"NSDictionary"8"NSError"16lr32l8
- ___block_descriptor_52_ea8_32s_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20ls32l8
- ___block_descriptor_56_e8_32bs40r48r_e34_v24?0"NSDictionary"8"NSError"16lr40l8r48l8s32l8
- ___block_descriptor_56_e8_32s40s48r_e17_v16?0"NSError"8lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e42_v24?0"LSDBExecutionContext"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_56_ea8_32bs40bs_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20ls32l8s40l8
- ___block_descriptor_56_ea8_32r40r_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20lr32l8r40l8
- ___block_descriptor_56_ea8_32s40bs_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20ls32l8s40l8
- ___block_descriptor_56_ea8_32s40r48r_e19_v32?0I8r^v12I20*24lr40l8s32l8r48l8
- ___block_descriptor_64_e8_32s40s48s56s_e27_v24?0"LSBundleProxy"8^B16ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_ea8_32s40s48s56r_e32_v32?0^{LSContext=}8I16I20r^v24lr56l8s32l8s40l8s48l8
- ___block_descriptor_64_ea8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
- ___block_descriptor_72_e8_32bs40r48r_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20ls32l8r40l8r48l8
- ___block_descriptor_72_ea8_32s40s48r_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20ls32l8s40l8r48l8
- ___block_descriptor_72_ea8_32s40s48s56s64bs_e48_v16?0?<v?"<_LSPendingSaveToken>""NSError">8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_72_ea8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
- ___block_descriptor_74_ea8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_76_ea8_32s40s48s56r_e5_v8?0lr56l8s32l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56r64r72r_e42_v24?0"LSDBExecutionContext"8"NSError"16ls32l8r56l8s40l8s48l8r64l8r72l8
- ___block_descriptor_80_ea8_32s40s48s56s64r72r_e42_v24?0"LSDBExecutionContext"8"NSError"16ls32l8s40l8s48l8s56l8r64l8r72l8
- ___block_descriptor_80_ea8_32s40s48s56s64r72r_e48_v16?0"<LSRegistrantDatabaseContextProviding>"8lr64l8s32l8s40l8s48l8r72l8s56l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_88_ea8_32s40s48s56s64s72bs80r_e48_v16?0"<LSRegistrantDatabaseContextProviding>"8lr80l8s32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.1105
- ___block_literal_global.111
- ___block_literal_global.1128
- ___block_literal_global.1155
- ___block_literal_global.1157
- ___block_literal_global.116
- ___block_literal_global.1168
- ___block_literal_global.118
- ___block_literal_global.120
- ___block_literal_global.126
- ___block_literal_global.130
- ___block_literal_global.136
- ___block_literal_global.138
- ___block_literal_global.148
- ___block_literal_global.153
- ___block_literal_global.156
- ___block_literal_global.166
- ___block_literal_global.171
- ___block_literal_global.173
- ___block_literal_global.177
- ___block_literal_global.191
- ___block_literal_global.194
- ___block_literal_global.196
- ___block_literal_global.202
- ___block_literal_global.205
- ___block_literal_global.207
- ___block_literal_global.210
- ___block_literal_global.220
- ___block_literal_global.222
- ___block_literal_global.224
- ___block_literal_global.228
- ___block_literal_global.230
- ___block_literal_global.238
- ___block_literal_global.243
- ___block_literal_global.246
- ___block_literal_global.250
- ___block_literal_global.255
- ___block_literal_global.259
- ___block_literal_global.271
- ___block_literal_global.276
- ___block_literal_global.278
- ___block_literal_global.29
- ___block_literal_global.296
- ___block_literal_global.309
- ___block_literal_global.311
- ___block_literal_global.314
- ___block_literal_global.317
- ___block_literal_global.335
- ___block_literal_global.341
- ___block_literal_global.342
- ___block_literal_global.345
- ___block_literal_global.35
- ___block_literal_global.381
- ___block_literal_global.389
- ___block_literal_global.393
- ___block_literal_global.396
- ___block_literal_global.401
- ___block_literal_global.404
- ___block_literal_global.417
- ___block_literal_global.428
- ___block_literal_global.437
- ___block_literal_global.448
- ___block_literal_global.451
- ___block_literal_global.469
- ___block_literal_global.470
- ___block_literal_global.473
- ___block_literal_global.527
- ___block_literal_global.552
- ___block_literal_global.557
- ___block_literal_global.586
- ___block_literal_global.59
- ___block_literal_global.636
- ___block_literal_global.64
- ___block_literal_global.645
- ___block_literal_global.65
- ___block_literal_global.659
- ___block_literal_global.678
- ___block_literal_global.68
- ___block_literal_global.71
- ___block_literal_global.77
- ___block_literal_global.90
- ___block_literal_global.960
- ___block_literal_global.999
- ___registerSingleMIDict_block_invoke
- ___registerSingleMIDict_block_invoke.cold.1
- __kCFURLVolumeIDKey
- __registerMIPluginDictionary
- __registerMIPluginDictionary.cold.1
- _audit_token_to_au32
- _container_create_or_lookup_app_group_paths_for_platform
- _container_create_or_lookup_path_for_current_user
- _container_create_or_lookup_path_for_platform
- _dlopenHelper$FileProvider
- _dlopenHelperFlag$FileProvider
- _gotLoadHelper_x8$_OBJC_CLASS_$_BSProcessHandle
- _initMobileInstallationEnumerateAllInstalledItemDictionaries
- _init_EXStartService
- _objc_msgSend$_LSResolveIdentifiers:
- _objc_msgSend$_LSResolveIdentifiers:context:
- _objc_msgSend$_bindingEvaluatorResultFilterForBindingStyle:contentIsManaged:sourceAuditToken:
- _objc_msgSend$_cachedDataContainerURL
- _objc_msgSend$_dataContainerURLFromDatabase
- _objc_msgSend$_rawEnvironmentVariables
- _objc_msgSend$_rawGroupContainerURLs
- _objc_msgSend$_rawGroupContainerURLsCheckingRedaction
- _objc_msgSend$applicationForOpeningResource:
- _objc_msgSend$baseBindingEvaluatorWithBindingStyle:auditToken:
- _objc_msgSend$enumerateApplicationsOfType:block:
- _objc_msgSend$enumerateBundlesOfType:block:
- _objc_msgSend$getCachedBundleIDToPersonasWithAttributesMap:systemPersonaUniqueString:personalPersonaUniqueString:
- _objc_msgSend$getUncachedBundleIDToPersonasWithAttributesMap:systemPersonaUniqueString:personalPersonaUniqueString:
- _objc_msgSend$initFileURLWithPath:
- _objc_msgSend$initWithContext:operationUUID:bundleIdentifier:precondition:type:
- _objc_msgSend$initWithContext:operationUUID:itemInfoDict:personas:
- _objc_msgSend$initWithDisplayType:handler:
- _objc_msgSend$initWithDocumentProxy:
- _objc_msgSend$initWithStrategy:operationUUID:itemInfoDict:
- _objc_msgSend$initWithStrategy:operationUUID:itemInfoDict:personas:
- _objc_msgSend$isAlwaysAvailable
- _objc_msgSend$isDeletableIgnoringRestrictions
- _objc_msgSend$listAllPersonaWithAttributes
- _objc_msgSend$performPostInstallationRegistration:personaUniqueStrings:operationUUID:reply:
- _objc_msgSend$performRebuildRegistration:personaUniqueStrings:reply:
- _objc_msgSend$performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:operationUUID:reply:
- _objc_msgSend$personaAttributesForPersonaType:
- _objc_msgSend$personalPersonaAttributes
- _objc_msgSend$registerApplicationForRebuildWithInfoDictionaries:personaUniqueStrings:requestContext:registrationError:
- _objc_msgSend$registerBuiltinApplication:personaUniqueStrings:operationUUID:reply:
- _objc_msgSend$registerBundleNodeReinitializingContext:inBundleContainer:installDictionary:personasWithAttributes:error:
- _objc_msgSend$registerContainerizedApplicationWithInfoDictionaries:operationUUID:requestContext:saveObserver:registrationError:
- _objc_msgSend$registerContainerizedApplicationWithInfoDictionaries:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:
- _objc_msgSend$registerItemInfo:alias:diskImageAlias:bundleURL:installationPlist:completionHandler:
- _objc_msgSend$registerPluginNodeReinitializingContext:installDictionary:existingPlugin:error:
- _objc_msgSend$scanForAppsInRatingRankExceptionsList:
- _objc_msgSend$schemeTypeOfScheme:
- _objc_msgSend$sendNotification:forApplications:withPlugins:
- _objc_msgSend$triggerRegistrationForContainerizedContentWithOptions:completion:
- _preferredLocalizations.once.248
- _registerApplicationWithDictionary
- _registerApplicationWithDictionary.cold.1
- _registerApplicationWithDictionary.cold.2
- _softLinkMobileInstallationEnumerateAllInstalledItemDictionaries
- _softLink_EXStartService
CStrings:
+ "#LSDatabaseBuilder allowing use of diagnostics stash"
+ "%s: Failed to archive configuration: %{public}@"
+ "%s: Failed to deserialize boot info plist: %{public}@"
+ "%s: Failed to read boot info file: %{public}@"
+ "%s: Failed to read configuration file %{public}@: %{public}@"
+ "%s: Failed to serialize boot info plist: %{public}@"
+ "%s: Failed to write boot info file: %{public}@"
+ "%s: Failed to write launch configuration file to %@: %{public}@"
+ "%s: Registered configuration with UUID %{public}@"
+ "%s: could not enumerate at %@: %@"
+ "%s: unable to remove %@: %@"
+ "%sset strong binding for %{private}@: %{private}@ bind opts %#lx"
+ "%{public}s(%{private}@ update=%{BOOL}d)"
+ "%{public}s() => %{public}d"
+ "%{public}s: Boot UUID changed from %{public}@ to %{public}@, clearing storage"
+ "%{public}s: Boot UUID matches, storage is valid"
+ "%{public}s: Configuration %@ already exists"
+ "%{public}s: Failed to create storage directory: %{public}@"
+ "%{public}s: Failed to generate nonce"
+ "%{public}s: Failed to get boot UUID: %{darwin.errno}d"
+ "%{public}s: Failed to get current boot UUID, cannot validate storage"
+ "%{public}s: Failed to unarchive configuration: %{public}@"
+ "%{public}s: Failed to write boot info"
+ "%{public}s: Fetched configuration with UUID %{public}@"
+ "%{public}s: Invalid nonce in boot info, reinitializing"
+ "%{public}s: No saved boot UUID, initializing storage"
+ "%{public}s: Wrote boot info with UUID %{public}@"
+ "(none available)"
+ "(restricted %d)"
+ "+[LSApplicationRecord(Enumeration) enumeratorForCandidateAppsIgnoringEligibilityForCategory:options:]"
+ "+[LSDExtensionLaunchConfigurationStore sharedServerInstance]"
+ "+[LSDServerExtensionLaunchConfigurationRegistrar sharedServerInstance]"
+ "+[LSExtensionLaunchConfiguration systemRegistrar]"
+ "+[_LSPersonaDatabase _getPersonaAttributesRetryingIfNecessary]"
+ "-[LSApplicationExtensionRecord(Restrictions) initWithBundleIdentifier:allowingRestrictedForReasons:error:]"
+ "-[LSApplicationRecord(Identities) identities]"
+ "-[LSApplicationRestrictionsManager _LSResolveIdentifiers:]_block_invoke"
+ "-[LSApplicationRestrictionsManager _lazyLoadRestrictionsIdentifierSet:identifiersAreNullable:context:getter:]_block_invoke"
+ "-[LSApplicationWorkspace scanForAppsWithIdentifiersInSet:]_block_invoke"
+ "-[LSBundleRecord(Containers) dataContainerURLForPersonaWithUniqueString:error:]"
+ "-[LSBundleRecord(Containers) getGroupContainersForPersonaWithUniqueString:createIfNecessary:error:]"
+ "-[LSBundleSetContainersOperation executeWithContext:]"
+ "-[LSDExtensionLaunchConfigurationStore _clearStorageDirectory]"
+ "-[LSDExtensionLaunchConfigurationStore _clearStorageDirectory]_block_invoke"
+ "-[LSDExtensionLaunchConfigurationStore _currentBootUUID]"
+ "-[LSDExtensionLaunchConfigurationStore _initializeStorage]"
+ "-[LSDExtensionLaunchConfigurationStore _readBootInfo]"
+ "-[LSDExtensionLaunchConfigurationStore _writeBootInfo:nonce:]"
+ "-[LSDExtensionLaunchConfigurationStore fetchConfigurationWithUUID:error:]"
+ "-[LSDExtensionLaunchConfigurationStore registerConfiguration:error:]"
+ "-[LSExtensionLaunchConfigurationClientSystemRegistrar fetchRegisteredConfigurationWithUUID:additionalConfigurationClass:error:]_block_invoke_2"
+ "-[LSExtensionLaunchConfigurationResolver bestLaunchPersonaForExtension:hostPersona:hostAuditToken:error:]"
+ "-[LSExtensionLaunchConfigurationResolver resolveConfiguration:forExtensionWithUUID:hostPersonaUniqueString:hostAuditToken:error:]"
+ "-[LSMIResultRegistrantTrueDatabaseContext registerBundleNodeReinitializingContext:inBundleContainer:installInfo:error:]"
+ "-[LSWorkPipe enqueueWork:]"
+ "-[LSWorkPipe initWithDepth:label:]"
+ "-[_LSDModifyClient performPostInstallationRegistration:operationUUID:reply:]"
+ "-[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:bundlePersonaRecordMap:operationUUID:reply:]"
+ "-[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:bundlePersonaRecordMap:operationUUID:reply:]_block_invoke"
+ "-[_LSDModifyClient registerBuiltinApplication:operationUUID:reply:]"
+ "-[_LSDModifyClient registerItemInfo:alias:diskImageAlias:bundleURL:installInfo:completionHandler:]"
+ "-[_LSDModifyClient removeReferencesToPersonaWithUniqueString:operationUUID:reply:]"
+ "-[_LSDModifyClient removeReferencesToPersonaWithUniqueString:operationUUID:reply:]_block_invoke"
+ "-[_LSDModifyClient setContainersForApplicationsWithBundleIdentifiers:unbundledExtensionsWithBundleIdentifiers:fromBundlePersonaRecordMap:operationUUID:reply:]"
+ "-[_LSDModifyClient setContainersForApplicationsWithBundleIdentifiers:unbundledExtensionsWithBundleIdentifiers:fromBundlePersonaRecordMap:operationUUID:reply:]_block_invoke"
+ "-[_LSDReadClient fetchRegisteredConfigurationWithUUID:completion:]"
+ "-[_LSDReadClient getPersonalPersonaUniqueString:]"
+ "-[_LSDReadClient getPersonalPersonaUniqueString:]_block_invoke"
+ "-[_LSDReadClient getTypeRecordForPromiseAtURL:completionHandler:]"
+ "-[_LSDefaults sandboxExtensionForCreatedDiagnosticsStashDirectoryURLWithError:]"
+ "-[_LSDefaults systemDataDiagnosticsStashDirectoryURLWithError:]"
+ "-[_LSPersonaDatabase personaWithAttributesForPersonaUniqueString:error:]"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Database/LSBundleBase.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Database/LSBundleBase.mm"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSExtensionLaunchConfiguration.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSExtensionLaunchConfigurationResolver.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPersonaAssociationMutation.mm"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreServices/LaunchServices.subprj/Source/Util/LSDefaults.m"
+ "/Library/Developer/"
+ "/System/Library/ExtensionKit/Extensions/"
+ "/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor"
+ "0 0"
+ "0A `"
+ "<%@ %p %@>"
+ "<LSSliceInfo: t=%#x s=%#x>"
+ "@\"LSBundleDataContainerMap\"8@?0"
+ "@\"NSObject<NSCoding><NSCopying><NSSecureCoding>\"8@?0"
+ "@\"NSSet\"16@?0^{LSContext=@}8"
+ "Additional configuration digest of %@ must be non-nil and 64 bytes or fewer"
+ "App %@ on affected list does not appear to be installed (this may be expected): %@"
+ "B16@?0^{container_object_s=}8"
+ "B28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20"
+ "B28@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20"
+ "B32@?0@\"_LSPersonaWithAttributes\"8Q16^B24"
+ "BGRuntimeUsage"
+ "Boot nonce must be initialized"
+ "BootInfo.plist"
+ "BootUUID"
+ "Bundle unit %llx not found"
+ "Bundle unit %llx went missing during persona removal!"
+ "Caching data containers for all installed applications"
+ "Cannot register app extension %@ without MobileInstallation data. Installation info was NULL"
+ "Cannot remove persona %@ from bundle %@ as it would leave the bundle with no personas"
+ "Cannot remove persona %@ from plugin %@ as it would leave the plugin with no data containers"
+ "Client"
+ "Configuration had additional configuration but no class was provided"
+ "Configuration had no additional configuration but class to decode was provided"
+ "Configuration must not be nil"
+ "Copy call failed"
+ "Copy object finalize"
+ "Could not connect to database in %s: %@; resolving identifiers will only consult ManagedConfiguration"
+ "Could not connect to database to GC after system content scan! %@"
+ "Could not ensure container directory exists for diagnostics database: %@"
+ "Could not set strong binding for %{private}@: %@"
+ "Couldn't connect to database to scan for bundles affected by restrictions: %@"
+ "Couldn't fetch from containermanager: %@"
+ "Couldn't find personal persona unique string?"
+ "Couldn't get database to scan for deletable system apps: %@"
+ "Couldn't get database to scan for rating rank changes: %@"
+ "Current persona is of type %ld for system persona app, which is ambiguous"
+ "DiagnosticsSupport"
+ "Enumerated %zu containers from containermanager"
+ "Enumerating system content with ICL to update containers"
+ "Error enumerating content syncing with MI: %@"
+ "Expected an ICL record to register an app on this platform! Continuing and hoping for the best..."
+ "ExtensionLaunchConfigurations"
+ "FBSDisplayLayoutMonitorConfiguration"
+ "FPExtendBookmarkForDocumentURL() weak link failed."
+ "Failed to create container query"
+ "Failed to enumerate diagnostics stash directory at %@: %@"
+ "Failed to get diagnostics stash directory: %@"
+ "Failed to get diagnostics stash location for copy: %@"
+ "Failed to get storage container: error=%s"
+ "Failed to get system content database URL for copy"
+ "Failed to post distributed notification %@: %@"
+ "Failed to remove existing .csstore file at %@: %@"
+ "Filtered to %zu containerized and cacheable applications"
+ "GC after system content scan failed!"
+ "Garbage collecting database after system content scan."
+ "GuestType"
+ "HasCriticalAlerts"
+ "ICLBundleRecord created from legacy dictionary has no bundle identifier, ignoring"
+ "ICLBundleRecord has no bundle identifier, ignoring"
+ "Install info is for a parallel placeholder but app record is not an ICLAppRecord! %@ %@"
+ "InstalledContentLibrary"
+ "LSBundleBase.h"
+ "LSBundleDataContainer.mm"
+ "LSBundlePersonaRecordMap.m"
+ "LSDExtensionLaunchConfigurationStore.m"
+ "LSDServerExtensionLaunchConfigurationRegistrar.m"
+ "LSDocumentMayBeExecuted"
+ "LSExplicitlyRestrictable"
+ "LSExtensionLaunchConfiguration.m"
+ "LSExtensionLaunchConfigurationResolver.m"
+ "LSIncludeAppLinksForCallingApplicationKey"
+ "LSLaunchDAllowMultipleInstances"
+ "LSPersistentIdentifier _LSPersistentIdentifierMakeForDatabase(LSContext * _Nonnull)"
+ "LSRegisterURL"
+ "LSSynchronization.mm"
+ "LSWrappedContainerManagerDomain"
+ "MI_Persona_BundleID_Relayering"
+ "MSU is not available"
+ "MobileInstallationEnumerateAllInstalledItemBundleRecords"
+ "Must never call %s from within the Launch Services daemon."
+ "NSBackgroundActivityUsageDescription"
+ "NSURL *pluginKitUserElectionStoreURL()_block_invoke"
+ "No bundle identifier available. "
+ "No class for legacy dictionary with type %@ identifier %@, ignoring"
+ "No concrete persona found for system persona app."
+ "No context available, populating %zu records directly from containermanager"
+ "No known standalone plugin for %@"
+ "No path available."
+ "No personal persona in UM! Things will go badly."
+ "No system persona in UM! Things will go badly."
+ "No url available."
+ "Nonce"
+ "Not all persona removals were successful, but %zu were"
+ "Not all persona updates were successful, but %zu were"
+ "OSStatus _LSServer_RegisterItemInfo(const LSRegistrationInfo *__strong, NSData *__strong, CFDictionaryRef, LSInstallInfo *__strong, CSStoreUnitID *, CSStoreUnitID *, Boolean *, CFStringRef *)"
+ "Parental controls restricted list changed to %@, affected identifiers: %@"
+ "Plugin for %@ is not standalone"
+ "Plugin unit %llx does not have multiple containers"
+ "Plugin unit %llx not found"
+ "Plugin unit %llx went missing during persona removal!"
+ "Preflight successful for removing persona %@: %zu apps, %zu standalone plugins"
+ "Removed existing .csstore file from diagnostics stash: %@"
+ "Request for identifier of type %d from process %d is denied."
+ "Resolver must not be nil"
+ "Rolling UUID on %@ during persona removal and marking not eligible for redaction"
+ "Rosetta Warning Message"
+ "SBRepresentedBundleIdentifier"
+ "Server must return either configuration or error"
+ "Setting cached data containers for %zu applications"
+ "Store must not be nil"
+ "This process has made an attempt to fetch the declaring bundle record for a Uniform Type (%@) but cannot do so from the app sandbox. Break on __LS_CANNOT_REALIZE_UTTYPE_DECLARING_BUNDLE_RECORD_FROM_APP_SANDBOX__ to debug."
+ "URL scheme"
+ "UUID must not be nil"
+ "Unknown persona with unique string %@ has alarming type %d!"
+ "Unsetting redactable for unit %llx during persona removal"
+ "Workloop seeding sync completed, seeding in-flight count: %d"
+ "You cannot use -[LSApplicationWorkspace registerApplicationDictionary:] to register applications anymore. These interfaces have been deprecated for years."
+ "_LSCopyDataContainerURLFromContainermanagerForPersona"
+ "_LSCopyGroupContainerURLSFromContainermanagerForPersona"
+ "_LSDatabaseCreateFromDiagnosticsStash failed with error %{public}@"
+ "_LSIsNonFileURLOpenRequestValid"
+ "_LSMakeNSErrorFromContainerError"
+ "_LSShouldAbortPersonaRequest"
+ "__NO_PERSONA__"
+ "_bundleDataContainerMapFromDatabase"
+ "_kLSURLApplicationBinaryCompatibilityLocalizedWarningKey"
+ "_rawGroupContainerURLMap"
+ "additionalConfigurationDigest"
+ "all personas and platforms"
+ "ambiguous container query from legacy SPI! bundle personas are %@, current persona is %@, picking %@ as query persona"
+ "asked to validate: %@ with persona unique strings %@ for map %@"
+ "baseData"
+ "begin sanitize system content database"
+ "bluetooth product ID (?)"
+ "bogus app record: must be full app"
+ "bogus category %llu"
+ "bogus input persona for input appex"
+ "bundle not associated with personal persona"
+ "bundle unit %llx has no personas in database?"
+ "bundleRecords"
+ "cachedDataContainerURLMap"
+ "can't remove last persona from data container mapping"
+ "can't remove last persona from group container mapping"
+ "codedAdditionalConfiguration"
+ "com.apple.CoreServices.fshelper"
+ "com.apple.developer.media-device-extension"
+ "com.apple.launchservices.extension-launch-configuration.registrar"
+ "com.apple.launchservices.primary-persona"
+ "com.apple.launchservices.rebuildWorkPipe"
+ "com.apple.launchservices.stash-system-content-database"
+ "com.apple.lsd.seeding"
+ "com.apple.lsd.waiting_queue"
+ "com.apple.mobile.MobileDataTrasit"
+ "com.apple.private.extensionkit.builtinanypersona"
+ "com.apple.private.extensionkit.builtinsystempersona"
+ "com.apple.private.extensionkit.crossPersonaLaunch"
+ "com.apple.private.representedBundleIdentifier"
+ "com.apple.usermanagerd.persona.fetch"
+ "command"
+ "container iteration failed but no error from containermanager"
+ "containerFixupScanTime"
+ "containers"
+ "could not canonicalize URL %@: %@"
+ "could not clean data container for persona: %@"
+ "could not clean group containers for persona: %@"
+ "could not connect to database in %s! %@"
+ "could not consume sandbox extension for pluginkit elections store URL: %{darwin.errno}d"
+ "could not copy: %{darwin.errno}d"
+ "could not find library for URL %@"
+ "could not find standalone plugin %@: %@"
+ "could not get affected bundle info for container update: %@"
+ "could not get affected bundle info for persona change: %@"
+ "could not get data container URL for containerized edu mode app: %@"
+ "could not get path for URL URL %@: %@"
+ "could not get personal persona in ambiguous persona situation"
+ "could not register extension launch configuration: %@"
+ "could not remove persona %@ from %@ (bundle unit %llx): %@"
+ "could not remove persona %@ from plugin %@ (unit %llx): %@"
+ "could not resolve _LSPrimaryPersonaIdentifier to personal persona"
+ "could not set diagnostics cache database purchable: %{darwin.errno}d"
+ "could not set diagnostics cache database purchable: could not open database file: %{darwin.errno}d"
+ "could not update containers for %@ (bundle unit %llx): %@"
+ "could not update containers for standalone plugin %@ (unit %llx): %@"
+ "couldn't consume sandbox extension to diagnostics directory: %{darwin.errno}d"
+ "couldn't create group container map: %@"
+ "couldn't create singular container entry for bundle! %@"
+ "couldn't find bundle to check persona association"
+ "couldn't get ICL extension record from dict %@"
+ "couldn't get file system representation of %@!"
+ "couldn't get host persona with attributes for purported host persona unique string %@, is it of a strange type?"
+ "couldn't get personal persona in fallback path in %s: %@"
+ "couldn't get personal persona unique string in this process: %@"
+ "couldn't infer personas from ICL bundle record %@! %@"
+ "couldn't make string for key %llx or value %llx in %s"
+ "couldn't process unit %llx for cache because we couldn't find its bundle record"
+ "couldn't reach %@: %@"
+ "createAndAssignSingular"
+ "create_block_invoke"
+ "critical"
+ "critical-alerts"
+ "dataContainer."
+ "database created from diagnostics stash, cleaning"
+ "depth > 0"
+ "diagnostics stash: couldn't get database URL: %@"
+ "diagnostics stash: couldn't get database node: %@"
+ "diagnostics stash: couldn't get database store: %@"
+ "digest mismatch fetching extension launch configuration"
+ "draining outstanding containerized content"
+ "end sanitize system content database"
+ "enqueueing work on invalidated lane!"
+ "entrypoint"
+ "ersatz"
+ "exactly one of result %@ or error %@ must be nonnil"
+ "executable-document"
+ "expected one app extension record, had %zu"
+ "extension UUID must not be nil"
+ "failed to create XPC connection to %s"
+ "fshelper XPC reply error: %@"
+ "fshelper XPC reply was not a dictionary or error?"
+ "fshelper returned error status: %lld"
+ "got a container, asked for it to include a path, but it didn't have one?"
+ "got container but no path"
+ "handleMCEffectiveSettingsChanged/Found affected apps"
+ "has-multiple-containers"
+ "inDB"
+ "includeAppLinksForCallingApplication"
+ "invalid plugin: %@"
+ "is-placeholder-plugin"
+ "isDowngrade"
+ "isParallelPlaceholder"
+ "kern.bootsessionuuid"
+ "label != NULL"
+ "launchd-allows-multiple-instances"
+ "lazyPlist"
+ "loaded database from diagnostics stash"
+ "map"
+ "missing path in data container URL"
+ "missing persona unique string"
+ "need that database"
+ "no acceptable persona available"
+ "no app or placeholder record when enumerating bundle %@ of type %d! ignoring. record: %@"
+ "no bundleid %@ or personaUniqueString %@"
+ "no container but no error from containermanager"
+ "no install info, bundle at %@ will not be registered"
+ "no parallel placeholder URL for %@ %@ but install info is %@!"
+ "no path from containermanager"
+ "no path in data container URL"
+ "no personal persona in %s? Huh?"
+ "no personal persona!?"
+ "no sandbox extension provided by containermanager"
+ "not using data container URL from database for unit %llx"
+ "operation %@ attempting to remove references to persona %@ from pid %ld"
+ "operation %@ attempting to set containers for appBundleIDs %@ unbundledExtensions %@ from pid %ld"
+ "operation %@: Not all container updates were successful, but some were, so arming save timer"
+ "operation %@: Not all persona reference removals were successful, but some were, so arming save timer"
+ "operation %@: Not all persona updates were successful, but some were, so arming save timer"
+ "operation %@: Save after remove references to persona %@ attempted: %d save error: %@"
+ "operation %@: Save after set containers for apps %@ attempted: %d save error: %@"
+ "operation %@: container-update succeeded"
+ "operation %@: remove reference to persona %@ success"
+ "overrides"
+ "parent app is restricted"
+ "persona %@ platform %d"
+ "persona record map validation failed: %@"
+ "personaMap"
+ "personasWithAttributes"
+ "pluginHasOverride"
+ "preflight failed for app %@: %@"
+ "preflight failed for plugin %@: %@"
+ "prepareBinaryCompatibilityWarningValue"
+ "q24@?0@\"_LSPersonaWithAttributes\"8@\"_LSPersonaWithAttributes\"16"
+ "querying MCM for container for %@, class %llx, platform %lu, persona %@"
+ "querying MCM for group containers for %@, platform %lu, persona %@"
+ "querying for all containers for %{public}@"
+ "querying for containers for %zu identifiers for %{public}@"
+ "recordMap"
+ "registered extension launch configuration %@"
+ "removePersona"
+ "represented bundle"
+ "restricted_distributed_notifications"
+ "result: %@ options: %lx"
+ "sandbox_extension"
+ "seeding in-flight counter underflow (%d)"
+ "send applicationStateDidChange:"
+ "set data containers on %zu of %zu input app records"
+ "should have an error on failure path!"
+ "stash_system_content_database_to_diagnostics"
+ "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /Library/Caches/com.apple.xbs/E6FADEB6-4B69-4DE2-AB24-1EBF9D5B330C/TemporaryDirectory.isfGeA/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1477:63)]"
+ "status"
+ "std::expected<BundleDataContainerReleaseOperation, NSError *> LaunchServices::DataContainerWritableContext::removePersona(__strong LSDatabaseRef, NSString *__strong)"
+ "strong binding for %{private}@ is not allowed: %@"
+ "swizzling %@ for %@ in open"
+ "un-"
+ "unable to annotate persona strings list to types! Will have to fall back to checking in lsd! %@"
+ "unable to find plugin with unit id %llx"
+ "unable to find plugin with unit id %llx during persona removal"
+ "unable to get preboot volume path: %@"
+ "unable to locate user container: error %s"
+ "unexpected event on fshelper XPC connection: %@"
+ "using current persona %@ as container query persona for bundle with system persona"
+ "using data container URL(s) from database for unit %llx"
+ "v24@?0@\"ICLBundleRecord\"8@\"NSError\"16"
+ "v24@?0@\"LSTransmissibleExtensionLaunchConfiguration\"8@\"NSError\"16"
+ "v24@?0@\"NSUUID\"8@\"NSError\"16"
+ "v24@?0@\"UTTypeRecord\"8@\"NSError\"16"
+ "v24@?0r*8^B16"
+ "v24@?0{PersonaAndPlatform=@I}8"
+ "v28@?0@\"NSString\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20"
+ "v28@?0@\"NSString\"8I16r^{LSPluginData={LSBundleBaseData=IIIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20"
+ "v28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20"
+ "v28@?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}12*20"
+ "v32@?0@\"FBSDisplayLayoutMonitor\"8@\"FBSDisplayLayout\"16@\"FBSDisplayLayoutTransitionContext\"24"
+ "v32@?0@\"NSNumber\"8@\"_LSLocalizedStringRecord\"16^B24"
+ "v32@?0@\"NSString\"8@\"ICLBundlePersonaRecord\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSString\"16*24"
+ "v32@?0@\"NSString\"8@\"NSURL\"16^B24"
+ "v32@?0@\"NSString\"8@\"_LSPersonaWithAttributes\"16^B24"
+ "v32@?0@\"_LSPersonaWithAttributes\"8Q16^B24"
+ "validateBundlePersonaRemoval"
+ "validatePluginPersonaRemoval"
+ "void LaunchServices::UTTypeEnumerateFlavoredDisplayNames(__strong LSDatabaseRef, const _UTTypeData *, const F &) [F = (lambda at /Library/Caches/com.apple.xbs/E6FADEB6-4B69-4DE2-AB24-1EBF9D5B330C/TemporaryDirectory.isfGeA/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Database/UTTypeCore.mm:159:55)]"
+ "void _LSAssertNotRunningInServer(const char *)"
+ "warning: no persona provided for bundle registration of %@"
+ "work != nil"
+ "wrong number of appex records"
+ "xpc_object_t  _Nonnull _LSCopyGroupContainerIdentifiersXPCObjectFromEntitlements(NSString *__strong _Nonnull, LSPropertyList *__strong _Nonnull)"
+ "\x91"
- "#16@0:8"
- "%zu items were provided to be registered; exactly 1 must be specified"
- "(restricted)"
- "-[LSApplicationWorkspace scanForAppsInRatingRankExceptionsList:]_block_invoke"
- "-[LSMIResultRegistrantTrueDatabaseContext registerBundleNodeReinitializingContext:inBundleContainer:installDictionary:personasWithAttributes:error:]"
- "-[_LSDModifyClient performPostInstallationRegistration:personaUniqueStrings:operationUUID:reply:]"
- "-[_LSDModifyClient performPostInstallationRegistration:personaUniqueStrings:operationUUID:reply:]_block_invoke"
- "-[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:operationUUID:reply:]"
- "-[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:operationUUID:reply:]_block_invoke"
- "-[_LSDModifyClient registerBuiltinApplication:personaUniqueStrings:operationUUID:reply:]"
- "-[_LSDModifyClient registerBuiltinApplication:personaUniqueStrings:operationUUID:reply:]_block_invoke"
- "-[_LSDModifyClient registerItemInfo:alias:diskImageAlias:bundleURL:installationPlist:completionHandler:]"
- "-[_LSPersonaDatabase _getPersonaAttributesRetryingIfNecessary]"
- "-[_LSPersonaDatabase personasWithAttributesForPersonaUniqueStrings:error:]"
- ".cxx_construct"
- ".cxx_destruct"
- "/System/Library/Frameworks/FileProvider.framework/FileProvider"
- ":16@0:8"
- ":20@0:8i16"
- "<LSSliceInfo@%p: t=%#x s=%#x>"
- "@\"<LSDefaultApplicationQueryDatastore>\""
- "@\"<LSDefaultApplicationQueryDefaultAppEvaluator>\""
- "@\"<LSDomainEligibilityResolver>\""
- "@\"<LSFeatureFlagResolver>\""
- "@\"<LSObserverDelegate>\""
- "@\"<LSOpenResourceOperationDelegate>\""
- "@\"<LSOpenStagingDirectoryManagerIOPersonality>\""
- "@\"<LSRatingRankEligibilityMonitorDelegate>\""
- "@\"<LSRegistrantDatabaseContext>\"24@0:8^@16"
- "@\"<LSRegistrantStrategy>\""
- "@\"<LSResultRegistrantNotificationJournaller>\"28@0:8@\"NSString\"16B24"
- "@\"<NSObject>\""
- "@\"BSServiceConnectionEndpoint\""
- "@\"FSMimic\""
- "@\"FSNode\""
- "@\"FSNode\"32@0:8@\"NSURL\"16^@24"
- "@\"LSApplicationExtensionRecord\""
- "@\"LSApplicationIdentity\""
- "@\"LSApplicationProxy\""
- "@\"LSApplicationRecord\""
- "@\"LSApplicationRecord\"28@0:8I16^@20"
- "@\"LSApplicationRestrictionsManager\""
- "@\"LSBundleProxy\""
- "@\"LSBundleRecord\""
- "@\"LSClaimBindingBindable\""
- "@\"LSClaimBindingConfiguration\""
- "@\"LSClaimRecord\""
- "@\"LSDefaultApplicationQueryEntry\"32@0:8@\"LSApplicationRecord\"16Q24"
- "@\"LSDocumentProxy\""
- "@\"LSExtensionPointRecord\""
- "@\"LSIconAlertManager\""
- "@\"LSInstallProgressList\""
- "@\"LSPrecondition\""
- "@\"LSPropertyList\""
- "@\"LSRebuildStatisticsGatherer\""
- "@\"LSRegistrationInfo\""
- "@\"LSSettingsStoreConfiguration\""
- "@\"MIStoreMetadataDistributor\""
- "@\"MOEffectiveSettings\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSDictionary\"24@0:8^@16"
- "@\"NSDictionary\"40@0:8@\"NSSet\"16@\"NSXPCConnection\"24^@32"
- "@\"NSEnumerator\""
- "@\"NSError\""
- "@\"NSHashTable\""
- "@\"NSMapTable\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableOrderedSet\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSNumber\"16@0:8"
- "@\"NSNumber\"32@0:8Q16^@24"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSOperation\""
- "@\"NSOperationQueue\""
- "@\"NSSet\""
- "@\"NSSet\"16@0:8"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8^@16"
- "@\"NSTimer\""
- "@\"NSURL\""
- "@\"NSURL\"16@0:8"
- "@\"NSURL\"24@0:8Q16"
- "@\"NSURLComponents\""
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@\"NSXPCListener\""
- "@\"NSXPCListenerEndpoint\""
- "@\"NSXPCListenerEndpoint\"16@0:8"
- "@\"UISClickAttribution\""
- "@\"UISPasteSharingToken\""
- "@\"UTTypeRecord\""
- "@\"_LSAppLinkOpenState\""
- "@\"_LSApplicationRecordEnumerator\""
- "@\"_LSApplicationSensitiveDataProxy\""
- "@\"_LSBoundIconInfo\""
- "@\"_LSBundleProvider\""
- "@\"_LSDatabase\""
- "@\"_LSLazyPropertyList\""
- "@\"_LSLocalQueryResolver\""
- "@\"_LSOpenConfiguration\""
- "@\"_LSPlistHint\""
- "@\"_LSStringsFileContent\""
- "@\"_SWCServiceDetails\""
- "@100@0:8I16^{LSContext=@}20Q28@36@44@52@60@68@76@84@92"
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8I16"
- "@20@0:8S16"
- "@20@0:8i16"
- "@24@0:8#16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@\"NSString\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8B16B20"
- "@24@0:8Q16"
- "@24@0:8S16B20"
- "@24@0:8^@16"
- "@24@0:8^v16"
- "@24@0:8^{Context=^{LSContext}{LSContext=@}B@}16"
- "@24@0:8^{LSContext=@}16"
- "@24@0:8^{State=@BBBBBB}16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8^{__CFBundle=}16"
- "@24@0:8i16i20"
- "@24@0:8q16"
- "@24@0:8r*16"
- "@24@0:8{LSSessionKey=IB}16"
- "@24@0:8{LSSliceData=ii}16"
- "@28@0:8@16B24"
- "@28@0:8@16C24"
- "@28@0:8@16I24"
- "@28@0:8@16i24"
- "@28@0:8B16@20"
- "@28@0:8B16^@20"
- "@28@0:8C16^@20"
- "@28@0:8I16@\"<LSRegistrantDatabaseContext>\"20"
- "@28@0:8I16@20"
- "@28@0:8I16Q20"
- "@28@0:8I16^@20"
- "@28@0:8I16^{LSContext=@}20"
- "@28@0:8^{LSContext=@}16I24"
- "@32@0:8#16#24"
- "@32@0:8#16@24"
- "@32@0:8:16@24"
- "@32@0:8@16#24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16I24I28"
- "@32@0:8@16Q24"
- "@32@0:8@16^@24"
- "@32@0:8@16^B24"
- "@32@0:8@16^{LSContext=@}24"
- "@32@0:8@16^{LSSessionKey=IB}24"
- "@32@0:8@16q24"
- "@32@0:8@16r^{?=[8I]}24"
- "@32@0:8Q16@24"
- "@32@0:8Q16Q24"
- "@32@0:8Q16^@24"
- "@32@0:8^B16@24"
- "@32@0:8^^v16Q24"
- "@32@0:8^{Context=^{LSContext}{LSContext=@}B@}16@24"
- "@32@0:8^{LSContext=@}16@24"
- "@32@0:8^{LSContext=@}16I24I28"
- "@32@0:8^{LSContext=@}16^@24"
- "@32@0:8^{LSContext=@}16r^v24"
- "@32@0:8^{LSContext=@}16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}24"
- "@32@0:8^{__CFBundle=}16@24"
- "@32@0:8i16@20B28"
- "@32@0:8i16I20^@24"
- "@32@0:8q16^@24"
- "@32@0:8r^v16^@24"
- "@32@0:8r^v16r^{LSBinding=I^{LSBundleData}I^{?}@@Q}24"
- "@36@0:8@16@24B32"
- "@36@0:8@16B24^@28"
- "@36@0:8@16B24r^{?=[8I]}28"
- "@36@0:8@16C24@28"
- "@36@0:8@16I24^@28"
- "@36@0:8@16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
- "@36@0:8@16Q24B32"
- "@36@0:8@16Q24I32"
- "@36@0:8@16i24^@28"
- "@36@0:8C16@20^@28"
- "@36@0:8I16^{LSContext=@}20@28"
- "@36@0:8^{LSContext=@}16@24B32"
- "@36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
- "@36@0:8^{__CFBundle=}16@24B32"
- "@36@0:8r*16I24^@28"
- "@40@0:8#16#24@32"
- "@40@0:8#16@24@32"
- "@40@0:8#16@24^@32"
- "@40@0:8:16@24@32"
- "@40@0:8@16#24#32"
- "@40@0:8@16#24Q32"
- "@40@0:8@16:24@32"
- "@40@0:8@16@24#32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24B32B36"
- "@40@0:8@16@24Q32"
- "@40@0:8@16@24^@32"
- "@40@0:8@16@24^{LSContext=@}32"
- "@40@0:8@16B24@28B36"
- "@40@0:8@16B24I28^@32"
- "@40@0:8@16Q24@?32"
- "@40@0:8@16Q24Q32"
- "@40@0:8@16Q24^@32"
- "@40@0:8@16^@24^@32"
- "@40@0:8@16^{__CFBundle=}24@32"
- "@40@0:8@16q24^@32"
- "@40@0:8I16^{LSContext=@}20@28B36"
- "@40@0:8Q16@24@32"
- "@40@0:8Q16@24^@32"
- "@40@0:8^{Context=^{LSContext}{LSContext=@}B@}16@24^@32"
- "@40@0:8^{LSContext=@}16@24Q32"
- "@40@0:8^{LSContext=@}16@24^@32"
- "@40@0:8^{LSContext=@}16I24I28r^v32"
- "@40@0:8^{LSContext=@}16I24I28r^{?=IIIIiII[8I]IIIIIIIII}32"
- "@40@0:8^{LSContext=@}16I24I28r^{?=IIIsSIII[8I]III}32"
- "@40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}32"
- "@40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
- "@40@0:8^{LSContext=@}16I24I28r^{LSExtensionPointData=iI{LSVersionNumber=[32C]}IIIIIIIQ}32"
- "@40@0:8^{LSContext=@}16I24I28r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}32"
- "@40@0:8^{LSContext=@}16I24I28r^{LocalizedString=II{Flags=b1b1}}32"
- "@40@0:8^{LSContext=@}16r^{LSPersistentIdentifierData=C[3C]II[16C][0c]}24Q32"
- "@40@0:8i16@20B28@32"
- "@44@0:8@16@24@32B40"
- "@44@0:8@16B24@28^@36"
- "@44@0:8@16I24@28^@36"
- "@44@0:8@16Q24B32^@36"
- "@44@0:8@16Q24I32@?36"
- "@44@0:8B16^{LSContext=@}20I28I32r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}36"
- "@44@0:8B16^{LSContext=@}20I28I32r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}36"
- "@44@0:8C16Q20@28^@36"
- "@44@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20@28^@36"
- "@44@0:8Q16Q24Q32B40"
- "@44@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28^@36"
- "@44@0:8^{LSContext=@}16I24r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}28^@36"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24@32@?40"
- "@48@0:8@16@24@32Q40"
- "@48@0:8@16@24@32r^{?=[8I]}40"
- "@48@0:8@16@24^B32^@40"
- "@48@0:8@16@24q32q40"
- "@48@0:8@16^{LSContext=@}24Q32^@40"
- "@48@0:8@16q24q32Q40"
- "@48@0:8^{LSContext=@}16I24@28@36B44"
- "@48@0:8^{LSContext=@}16Q24r^I32Q40"
- "@48@0:8{?=[8I]}16"
- "@52@0:8@16@24@32@40I48"
- "@52@0:8@16@24@32B40r^{?=[8I]}44"
- "@52@0:8@16@24@32I40^@44"
- "@52@0:8@16Q24i32Q36Q44"
- "@52@0:8C16@20Q28@36^@44"
- "@52@0:8^{Context=^{LSContext}{LSContext=@}B@}16I24r^I28@36^@44"
- "@52@0:8^{LSContext=@}16I24r^I28@36^@44"
- "@52@0:8^{LSContext=@}16I24r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}28@36^@44"
- "@56@0:8@16@24@32@40@48"
- "@56@0:8@16@24@32@40^@48"
- "@56@0:8@16Q24@32^B40^@48"
- "@56@0:8@16^{LSContext=@}24Q32@40^@48"
- "@56@0:8B16C20@24Q32@40^@48"
- "@56@0:8Q16Q24@32B40I44^@48"
- "@56@0:8^{Context=^{LSContext}{LSContext=@}B@}16@24B32r^I36@44B52"
- "@56@0:8^{LSContext=@}16@24@32Q40Q48"
- "@56@0:8^{LSContext=@}16r^{LSBinding=I^{LSBundleData}I^{?}@@Q}24^@32@40^@48"
- "@56@0:8{?=[8I]}16^@48"
- "@60@0:8@16@24@32@40B48r^{?=[8I]}52"
- "@60@0:8@16@24@32B40@44@52"
- "@60@0:8@16@24@32^{LSContext=@}40B48^@52"
- "@60@0:8Q16@24B32@36@44^I52"
- "@60@0:8^{Context=^{LSContext}{LSContext=@}B@}16I24r^I28@36@44^@52"
- "@60@0:8^{LSContext=@}16I24r^I28@36@44^@52"
- "@60@0:8{?=[8I]}16C48^@52"
- "@64@0:8@16@24@32@40@48@56"
- "@64@0:8@16@24@32@40@48^@56"
- "@64@0:8@16@24^{LSContext=@}32I40I44r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}48^@56"
- "@68@0:8@16@24@32B40@44@52@60"
- "@68@0:8@16@24@32I40^{LSContext=@}44B52B56^@60"
- "@72@0:8@16@24@32@40@48@56^@64"
- "@72@0:8@16@24q32B40Q44B52^{LSContext=@}56^@64"
- "@76@0:8@16@24@32B40r^{?=[8I]}44@52@60@68"
- "@?"
- "@?16@0:8"
- "@?28@0:8I16^@20"
- "@?32@0:8C16B20r^{?=[8I]}24"
- "@?36@0:8@16I24^@28"
- "@?<v@?@>28@0:8I16^@20"
- "@?<v@?@>36@0:8@\"NSString\"16I24^@28"
- "AB"
- "ARKit"
- "AVCHDCollection"
- "AlternateIcons"
- "AlternateIconsInternal"
- "App %@ on rating rank exceptions list does not appear to be installed (this may be expected): %@"
- "AppProtectionPrivate"
- "AppWrappers"
- "B"
- "B16@0:8"
- "B20@0:8I16"
- "B20@0:8i16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSString\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8@?16"
- "B24@0:8I16I20"
- "B24@0:8Q16"
- "B24@0:8^@16"
- "B24@0:8^B16"
- "B24@0:8^q16"
- "B24@0:8^{Context=^{LSContext}{LSContext=@}B@}16"
- "B24@0:8^{LSContext=@}16"
- "B24@0:8q16"
- "B24@0:8r^{?=[8I]}16"
- "B28@0:8@16B24"
- "B28@0:8@16I24"
- "B28@0:8@16i24"
- "B28@0:8B16B20B24"
- "B28@0:8B16^@20"
- "B28@0:8I16^@20"
- "B28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20"
- "B28@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20"
- "B32@0:8:16@24"
- "B32@0:8:16^@24"
- "B32@0:8@\"NSString\"16@\"FSNode\"24"
- "B32@0:8@\"NSString\"16^@24"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "B32@0:8@16Q24"
- "B32@0:8@16^@24"
- "B32@0:8@16r^{?=[8I]}24"
- "B32@0:8Q16@24"
- "B32@0:8Q16^@24"
- "B32@0:8[1024c]16@24"
- "B32@0:8[1024c]16^@24"
- "B32@0:8^(?=[32C]{?={FileInfo=IIS{Point=ss}S}[16C]}{?={FolderInfo={Rect=ssss}S{Point=ss}S}[16C]})16^@24"
- "B32@0:8^@16@24"
- "B32@0:8^@16^@24"
- "B32@0:8^I16^@24"
- "B32@0:8^Q16^@24"
- "B32@0:8^d16^@24"
- "B32@0:8^i16^@24"
- "B32@0:8^{Context=^{LSContext}{LSContext=@}B@}16@24"
- "B32@0:8^{LSContext=@}16^@24"
- "B32@0:8^{fsid=[2i]}16^@24"
- "B32@0:8d16@?24"
- "B32@0:8r*16r*24"
- "B32@0:8r^(?=[32C]{?={FileInfo=IIS{Point=ss}S}[16C]}{?={FolderInfo={Rect=ssss}S{Point=ss}S}[16C]})16^@24"
- "B36@0:8:16@24B32"
- "B36@0:8@16B24^@28"
- "B36@0:8B16B20B24^I28"
- "B36@0:8C16@20^@28"
- "B36@0:8I16Q20^@28"
- "B36@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20^{LSContext=@}28"
- "B36@0:8I16r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20@28"
- "B36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
- "B40@0:8@16@24@32"
- "B40@0:8@16@24@?32"
- "B40@0:8@16@24^@32"
- "B40@0:8@16@?24^@32"
- "B40@0:8@16Q24^@32"
- "B40@0:8@16^Q24^@32"
- "B40@0:8@16r^{?=[8I]}24r*32"
- "B40@0:8I16r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20I28^{LSContext=@}32"
- "B40@0:8^@16@\"NSString\"24^@32"
- "B40@0:8^@16@24^@32"
- "B40@0:8^@16Q24^{LSContext=@}32"
- "B40@0:8^I16^I24^@32"
- "B40@0:8^I16^{LSContext=@}24^@32"
- "B40@0:8^Q16@24^@32"
- "B40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
- "B40@0:8q16@24^@32"
- "B44@0:8@\"FSNode\"16@\"NSDictionary\"24I32^@36"
- "B44@0:8@16@24C32^@36"
- "B44@0:8@16@24I32^@36"
- "B44@0:8@16@24i32^@36"
- "B44@0:8I16@20@28^@36"
- "B44@0:8^@16@\"NSString\"24C32^@36"
- "B44@0:8^@16@24C32^@36"
- "B48@0:8@16@24@32@40"
- "B48@0:8@16@24@32^@40"
- "B48@0:8@16@24^@32@?40"
- "B48@0:8@16B24B28@32^@40"
- "B48@0:8^I16r^^{LSBundleData}24^{LSContext=@}32@40"
- "B48@0:8{?=[8I]}16"
- "B52@0:8@\"NSString\"16I24@\"NSDictionary\"28@\"NSURL\"36^@44"
- "B52@0:8@16I24@28@36^@44"
- "B52@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20^{LSContext=@}28@36^@44"
- "B56@0:8@16@24@32@40^@48"
- "B56@0:8@16@24^@32^@40@?48"
- "B60@0:8@16@24I32@36@44^@52"
- "B60@0:8^@16^@24I32r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}36@44^@52"
- "B64@0:8@16@24@32@40@48^@56"
- "B64@0:8@16Q24Q32@40Q48^@56"
- "B68@0:8@16@24I32@36@44@52^@60"
- "B68@0:8^@16^@24@32@40@48I56^@60"
- "B72@0:8@16@24@32@40@48@56^@64"
- "B72@0:8@16@24@32Q40Q48@56^@64"
- "B76@0:8@16@24@32@40i48@52^@60^@68"
- "BUIPrivate"
- "BindingEvaluator"
- "BookmarkData"
- "BrowserSettings"
- "C"
- "C16@0:8"
- "C24@0:8@16"
- "C32@0:8@16@24"
- "C32@0:8@16^@24"
- "C40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}32"
- "C40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
- "CSStoreViewerAdditions"
- "CannedConfigurations"
- "Cannot register app extension %@ without MobileInstallation data. Installation dictionary was NULL"
- "ClaimBindingConfiguration"
- "ConstructForAnyFile"
- "ContainerManager error fetching data container for %{private}@: %llu %{public}s"
- "ContainerManager error fetching group containers for %{private}@: %llu %{public}s"
- "ContainerManager error populating env variables for %{private}@: %llu %{public}s"
- "Containers"
- "ContainingBundleIdentifier"
- "Conveniences"
- "Could not look up personas given unique strings %@: %@"
- "Couldn't copy data container alias %lu for bundle %lu: %@"
- "DYLD"
- "DefaultApps"
- "DeprecatedEnumeration"
- "DeprecatedURLQueries"
- "Diagnostic"
- "Enumeration"
- "EnvironmentVariables"
- "Error determining whether or not to fetch from container manager %@"
- "Expected a container but did not have one from MobileInstallation; must call out to MCM"
- "ExtendedAttributes"
- "ExtensionHiding"
- "FSMimic"
- "FSMimicPopulator"
- "FSNodePropertyProviding"
- "Failed to create application proxy for %@, regustration result was %d"
- "Failed to get storage container: error=%llu"
- "FinderInfo"
- "ForIconServicesOnly"
- "ForRunningBoardOnly"
- "Functions"
- "Gaming"
- "GroupContainers"
- "HMACSecret"
- "I16@0:8"
- "I20@0:8I16"
- "I32@0:8@\"FSNode\"16^@24"
- "I32@0:8@16^@24"
- "I32@0:8@16^{LSContext=@}24"
- "I40@0:8^{LSContext=@}16I24I28r^{?=IIIIiII[8I]IIIIIIIII}32"
- "I40@0:8^{LSContext=@}16I24I28r^{?=IIIsSIII[8I]III}32"
- "I40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}32"
- "I40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
- "I40@0:8^{LSContext=@}16I24I28r^{LSExtensionPointData=iI{LSVersionNumber=[32C]}IIIIIIIQ}32"
- "I40@0:8^{LSContext=@}16I24I28r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}32"
- "I52@0:8@\"FSNode\"16B24@\"NSDictionary\"28@\"NSSet\"36^@44"
- "I52@0:8@16B24@28@36^@44"
- "IOQueue"
- "IconServices"
- "Identities"
- "IndirectAccess"
- "InfoPlistRarities"
- "InstallMachineryPrivate"
- "InternalLocalization"
- "JSONObjectWithData:options:error:"
- "JournalApp"
- "LSATTrackingEnforcementManager"
- "LSAdditions"
- "LSAltIconManager"
- "LSAppClipMetadata"
- "LSAppDowngrade"
- "LSAppLink"
- "LSAppRemovalServiceProtocol"
- "LSApplicationExtensionRecord"
- "LSApplicationIdentity"
- "LSApplicationIdentityEnumerator"
- "LSApplicationIdentityMigrationResult"
- "LSApplicationIdentityMigrator"
- "LSApplicationProxy"
- "LSApplicationRecord"
- "LSApplicationRestrictionsManager"
- "LSApplicationWorkspace"
- "LSApplicationWorkspaceObserver"
- "LSApplicationWorkspaceObserverProtocol"
- "LSApplicationWorkspaceRemoteObserver"
- "LSAskManagerMCStateProvider"
- "LSBuiltinApplicationRegistrant"
- "LSBuiltinPluginRegistrant"
- "LSBundleDataPredicate"
- "LSBundleDataPredicateEvaluator"
- "LSBundleIdentity"
- "LSBundleInfoCachedValues"
- "LSBundleProxy"
- "LSBundleRecord"
- "LSBundleRecordBuilder"
- "LSBundleRecordUpdater"
- "LSBundleRegistrationStatePrecondition"
- "LSBundleURLRelationshipPrecondition"
- "LSByURLBundleUnregistrant"
- "LSByURLPluginUnregistrant"
- "LSClaimBinding"
- "LSClaimBindingBindable"
- "LSClaimBindingConfiguration"
- "LSClaimRecord"
- "LSDBExecutionContext"
- "LSDPluginManager"
- "LSDPluginProtocol"
- "LSDPluginServiceProtocol"
- "LSDatabase"
- "LSDatabaseBlockingFetchClient"
- "LSDatabaseBlockingFetchProtocol"
- "LSDatabaseBlockingFetchServer"
- "LSDatabaseBuilder"
- "LSDatabaseContext"
- "LSDatabaseRebuildContext"
- "LSDatabaseUnits"
- "LSDebuggingAdditions"
- "LSDefaultApplicationQueryBackend"
- "LSDefaultApplicationQueryDatabaseDefaultAppEvaluator"
- "LSDefaultApplicationQueryDatastore"
- "LSDefaultApplicationQueryDefaultAppEvaluator"
- "LSDefaultApplicationQueryEntry"
- "LSDefaultApplicationQueryResult"
- "LSDefaultApplicationQueryServerDatastore"
- "LSDefaultApplicationQueryUnrestrictedBehavior"
- "LSDetachable"
- "LSDocumentProxy"
- "LSDomainEligibilityResolver"
- "LSEligibilityCacheEligibilityResolver"
- "LSEligibilityPredicate"
- "LSEligibilityPredicateEvaluator"
- "LSEnumerator"
- "LSExtensionPoint"
- "LSExtensionPointRecord"
- "LSFeatureFlagPredicate"
- "LSFeatureFlagPredicateEvaluator"
- "LSFeatureFlagResolver"
- "LSHRNSupport"
- "LSHasOverride"
- "LSIconAlertManager"
- "LSIconChangeAlertToken"
- "LSIconResourceLocator"
- "LSInstallProgressAdditions"
- "LSInstallProgressList"
- "LSInstallProgressObserver"
- "LSInstallProgressProtocol"
- "LSInternalCachingEvaluator"
- "LSInternalWorkspaceObserverProtocol"
- "LSMCStateProvider"
- "LSMIResultRegistrant"
- "LSMIResultRegistrantServerDatabaseContextProviding"
- "LSMIResultRegistrantTrueDatabaseContext"
- "LSMIResultUnregistrant"
- "LSMacApplicationIdentityBookmark"
- "LSMarketplacesPreferences"
- "LSNormalizePluginDictionary"
- "LSObserver"
- "LSObserverAdditions"
- "LSOpenResourceOperationDelegate"
- "LSOpenStagingDirectoryManager"
- "LSOpenStagingDirectoryManagerIOPersonality"
- "LSOperationRequestContext"
- "LSPersonaUniqueStrings"
- "LSPlugInKitProxy"
- "LSPlugInQuery"
- "LSPlugInQueryAll"
- "LSPlugInQueryAllUnits"
- "LSPlugInQueryAllUnitsResult"
- "LSPlugInQueryWithIdentifier"
- "LSPlugInQueryWithQueryDictionary"
- "LSPlugInQueryWithURL"
- "LSPlugInQueryWithUnits"
- "LSPluginQueryAdditions"
- "LSPluginSDKResolutionAdditions"
- "LSPrecondition"
- "LSPreferredLocalizations"
- "LSProgressNotificationTimer"
- "LSPropertyList"
- "LSRatingRankEligibilityMonitor"
- "LSRatingRankEligibilityMonitorDelegate"
- "LSRebuildStatisticsGatherer"
- "LSRecord"
- "LSRecordAccess"
- "LSRecordBuilder"
- "LSRecordBuilderAdditions"
- "LSRecordPromise"
- "LSRegistrantDatabaseContext"
- "LSRegistrantDatabaseContextProviding"
- "LSRegistrantServerStrategy"
- "LSRegistrantStrategy"
- "LSRegistrationInfo"
- "LSResourceProxy"
- "LSServerOpenStagingIOPersonality"
- "LSSettingsStore"
- "LSSettingsStoreConfiguration"
- "LSSliceInfo"
- "LSSpotlightAction"
- "LSStashedAppMetadata"
- "LSSystemBundleIdentity"
- "LSSystemExtensionPointRefreshRegistrant"
- "LSURLOverride"
- "LSURLOverrideAdditions"
- "LSUseValuesMCStateProvider"
- "LSVPNPluginProxy"
- "LSVisualOrderingAdditions"
- "LSiTunesMetadata"
- "LaunchServicesAdditions"
- "Localization"
- "LocalizedName"
- "MCSetUnionRestriction:values:"
- "Marketplaces"
- "Missing path"
- "MobileInstall"
- "MobileInstallation"
- "MobileInstallationEnumerateAllInstalledItemDictionaries"
- "Multiuser"
- "NSCoding"
- "NSCopying"
- "NSDiscardableContent"
- "NSMutableCopying"
- "NSObject"
- "NSSecureCoding"
- "NSSet<NSString *> * _Nonnull _LSCopyGroupContainerIdentifiersFromEntitlements(NSString *__strong _Nonnull, LSPropertyList *__strong _Nonnull)"
- "NSStringFromLSInstallPhase:"
- "NSStringFromLSInstallState:"
- "NSStringFromLSInstallType:"
- "NSXPCListenerDelegate"
- "No active persona/ system persona detected for system persona app"
- "No bundle identifier provided. "
- "No path provided."
- "ODRConnection"
- "ODRDiskUsage"
- "ODRLaunchServicesProtocol"
- "ODRUsageForBundleIdentifier:error:"
- "OSStatus _LSServer_RegisterItemInfo(const LSRegistrationInfo *__strong, NSData *__strong, CFDictionaryRef, CFDictionaryRef, CSStoreUnitID *, CSStoreUnitID *, Boolean *, CFStringRef *)"
- "OpenAdditions"
- "OpenStrategy"
- "ParallelPlaceholderPath"
- "Personas"
- "PluginOwnerBundleID"
- "Private"
- "PrivateSchemeChecking"
- "Q16@0:8"
- "Q24@0:8@16"
- "Q40@0:8^{?=Q^@^Q[5Q]}16^@24Q32"
- "Q40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
- "QueryResolution"
- "RTL"
- "RatingRankMonitorDelegate"
- "Redaction"
- "Request for IDFA/IDFV from a process that has entitlement %{public}@; ignoring."
- "S"
- "S16@0:8"
- "SDKDictionary"
- "SDKDictionaryWithContext:tableID:unitID:unitBytes:"
- "SPIForSettings"
- "SandboxChecks"
- "ScopedAccess"
- "SubclassResponsibilities"
- "Subclasses must implement -uniqueIdentifier"
- "SubclassesCanOverride"
- "SubclassesShouldOverride"
- "SystemFolderNames"
- "T#,R"
- "T:,V_appObserverSelector"
- "T@\"<LSIconResourceLocator>\",R,N"
- "T@\"<LSObserverDelegate>\",W"
- "T@\"<_LSQueryResolving>\",R,D"
- "T@\"BSServiceConnectionEndpoint\",&,N,V_targetConnectionEndpoint"
- "T@\"BSServiceConnectionEndpoint\",&,V_targetServiceConnectionEndpoint"
- "T@\"FSMimic\",R,N,V_mimic"
- "T@\"FSNode\",R,N,V_node"
- "T@\"LSAppClipMetadata\",R"
- "T@\"LSApplicationProxy\",R,D,N"
- "T@\"LSApplicationProxy\",R,V_targetApplicationProxy"
- "T@\"LSApplicationRecord\",&,V_parentApplicationRecord"
- "T@\"LSApplicationRecord\",&,V_targetApplicationRecord"
- "T@\"LSApplicationRecord\",R"
- "T@\"LSApplicationRecord\",R,N"
- "T@\"LSBundleProxy\",R,D,N"
- "T@\"LSBundleProxy\",R,N,V_containingBundle"
- "T@\"LSBundleRecord\",R"
- "T@\"LSBundleRecord\",R,N"
- "T@\"LSBundleRecord\",R,N,V_realRecord"
- "T@\"LSBundleRecord\",R,V_bundleRecord"
- "T@\"LSClaimBindingConfiguration\",R,N,V_bindingConfiguration"
- "T@\"LSClaimRecord\",R,V_claimRecord"
- "T@\"LSDatabaseContext\",R"
- "T@\"LSDocumentProxy\",R,D"
- "T@\"LSExtensionPoint\",R,D,N"
- "T@\"LSExtensionPoint\",R,N"
- "T@\"LSExtensionPointRecord\",&"
- "T@\"LSExtensionPointRecord\",R"
- "T@\"LSInstallProgressList\",R,V_observedInstallProgresses"
- "T@\"LSPlugInKitProxy\",R,N"
- "T@\"LSPropertyList\",R"
- "T@\"LSSettingsStoreConfiguration\",&,N,V_configuration"
- "T@\"LSStashedAppMetadata\",R"
- "T@\"LSiTunesMetadata\",R"
- "T@\"MIStoreMetadataDistributor\",R,N"
- "T@\"MOEffectiveSettings\",&,V_effectiveSettings"
- "T@\"NSArray\",&,Sls_setPreferredLocalizations:"
- "T@\"NSArray\",C,D"
- "T@\"NSArray\",C,N,V_machOUUIDs"
- "T@\"NSArray\",C,N,V_preferredMarketplaces"
- "T@\"NSArray\",R"
- "T@\"NSArray\",R,D"
- "T@\"NSArray\",R,D,N"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_URLClaims"
- "T@\"NSArray\",R,N,V_activityTypes"
- "T@\"NSArray\",R,N,V_bgPermittedIdentifiers"
- "T@\"NSArray\",R,N,V_bundleIDs"
- "T@\"NSArray\",R,N,V_bundlePersonas"
- "T@\"NSArray\",R,N,V_carPlayInstrumentClusterURLSchemes"
- "T@\"NSArray\",R,N,V_deviceFamily"
- "T@\"NSArray\",R,N,V_documentClaims"
- "T@\"NSArray\",R,N,V_driverExtensionPaths"
- "T@\"NSArray\",R,N,V_exportedTypes"
- "T@\"NSArray\",R,N,V_iconFileNames"
- "T@\"NSArray\",R,N,V_importedTypes"
- "T@\"NSArray\",R,N,V_libraryItems"
- "T@\"NSArray\",R,N,V_machOUUIDs"
- "T@\"NSArray\",R,N,V_parentApplicationIdentifiers"
- "T@\"NSArray\",R,N,V_pluginUnits"
- "T@\"NSArray\",R,N,V_proxies"
- "T@\"NSArray\",R,N,V_queriableSchemes"
- "T@\"NSArray\",R,N,V_slices"
- "T@\"NSArray\",R,N,V_subgenres"
- "T@\"NSArray\",R,N,V_supportedComplicationFamilies"
- "T@\"NSArray\",R,N,V_windowOpenDates"
- "T@\"NSArray\",R,V__personasWithAttributes"
- "T@\"NSArray\",R,V_parentApplicationIdentifiers"
- "T@\"NSData\",R"
- "T@\"NSDate\",&,N,V_lastFiredDate"
- "T@\"NSDate\",R"
- "T@\"NSDate\",R,N"
- "T@\"NSDate\",R,N,V_referenceDate"
- "T@\"NSDate\",R,N,V_refreshAfter"
- "T@\"NSDate\",R,N,V_refreshDate"
- "T@\"NSDate\",R,N,V_registrationDate"
- "T@\"NSDate\",R,V_dateOriginallyInstalled"
- "T@\"NSDate\",R,V_dateStashed"
- "T@\"NSDictionary\",&,N"
- "T@\"NSDictionary\",&,V_pluginsByBundleIentifier"
- "T@\"NSDictionary\",C,N,V_frontBoardOptions"
- "T@\"NSDictionary\",C,V_browserState"
- "T@\"NSDictionary\",C,V_launchOptions"
- "T@\"NSDictionary\",R"
- "T@\"NSDictionary\",R,D,N"
- "T@\"NSDictionary\",R,N"
- "T@\"NSDictionary\",R,N,V_distributorInfo"
- "T@\"NSDictionary\",R,N,V_entitlements"
- "T@\"NSDictionary\",R,N,V_extensionSDK"
- "T@\"NSDictionary\",R,N,V_groupContainers"
- "T@\"NSDictionary\",R,N,V_iconsDict"
- "T@\"NSDictionary\",R,N,V_intentDefinitionURLs"
- "T@\"NSDictionary\",R,N,V_localizedIdentityUsageDescription"
- "T@\"NSDictionary\",R,N,V_localizedMicrophoneUsageDescription"
- "T@\"NSDictionary\",R,N,V_localizedNames"
- "T@\"NSDictionary\",R,N,V_localizedShortNames"
- "T@\"NSDictionary\",R,N,V_localizedStrings"
- "T@\"NSDictionary\",R,N,V_options"
- "T@\"NSDictionary\",R,N,V_pluginMIDicts"
- "T@\"NSDictionary\",R,N,V_pluginPlists"
- "T@\"NSDictionary\",R,N,V_sandboxEnvironmentVariables"
- "T@\"NSDictionary\",R,N,V_stashedAppInfo"
- "T@\"NSDictionary\",R,N,V_unlocalizedNamesWithContext"
- "T@\"NSDictionary\",R,N,V_values"
- "T@\"NSDictionary\",R,V_mobileInstallIDs"
- "T@\"NSError\",&,N,V_error"
- "T@\"NSError\",&,V_error"
- "T@\"NSMutableDictionary\",R,V_createdInstallProgresses"
- "T@\"NSMutableSet\",&,N,V_applications"
- "T@\"NSMutableSet\",R,N,V_counterpartAppBundleIDs"
- "T@\"NSMutableSet\",R,N,V_equivalentBundleIDs"
- "T@\"NSMutableSet\",R,V_observerSet"
- "T@\"NSNumber\",&,V_targetUserID"
- "T@\"NSNumber\",R"
- "T@\"NSNumber\",R,D,N"
- "T@\"NSNumber\",R,N"
- "T@\"NSNumber\",R,N,V_compatibilityState"
- "T@\"NSNumber\",R,N,V_directoryClass"
- "T@\"NSNumber\",R,N,V_downloaderDSID"
- "T@\"NSNumber\",R,N,V_familyID"
- "T@\"NSNumber\",R,N,V_genreID"
- "T@\"NSNumber\",R,N,V_installFailureReason"
- "T@\"NSNumber\",R,N,V_installType"
- "T@\"NSNumber\",R,N,V_itemID"
- "T@\"NSNumber\",R,N,V_purchaserDSID"
- "T@\"NSNumber\",R,N,V_ratingRank"
- "T@\"NSNumber\",R,N,V_ratingRankEligibilityDomain"
- "T@\"NSNumber\",R,N,V_staticDiskUsage"
- "T@\"NSNumber\",R,N,V_storefront"
- "T@\"NSNumber\",R,N,V_versionID"
- "T@\"NSNumber\",R,V_signatureVersion"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_internalQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R"
- "T@\"NSObject<OS_dispatch_queue>\",R,V_internalQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,V_observerQueue"
- "T@\"NSOperationQueue\",&"
- "T@\"NSOrderedSet\",R"
- "T@\"NSPredicate\",C,N"
- "T@\"NSProgress\",R,N"
- "T@\"NSSet\",R"
- "T@\"NSSet\",R,N"
- "T@\"NSSet\",R,N,V_keys"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,D"
- "T@\"NSString\",C,D,N"
- "T@\"NSString\",C,N,S_setLocalizedName:,V_localizedName"
- "T@\"NSString\",C,N,SsetSDKVersion:,V_sdkVersion"
- "T@\"NSString\",C,N,V_applicationIdentifier"
- "T@\"NSString\",C,V_bundleIdentifier"
- "T@\"NSString\",C,V_name"
- "T@\"NSString\",R"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_bundleIdentifier"
- "T@\"NSString\",R,C,N,V_identifier"
- "T@\"NSString\",R,D"
- "T@\"NSString\",R,D,N"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_MIMEType"
- "T@\"NSString\",R,N,V_alternatePrimaryIconName"
- "T@\"NSString\",R,N,V_appStoreToolsBuildVersion"
- "T@\"NSString\",R,N,V_appType"
- "T@\"NSString\",R,N,V_appVariant"
- "T@\"NSString\",R,N,V_applicationManagementDomain"
- "T@\"NSString\",R,N,V_artistName"
- "T@\"NSString\",R,N,V_bundleExecutable"
- "T@\"NSString\",R,N,V_bundleID"
- "T@\"NSString\",R,N,V_bundleIdentifier"
- "T@\"NSString\",R,N,V_bundleName"
- "T@\"NSString\",R,N,V_bundleVersion"
- "T@\"NSString\",R,N,V_categoryType"
- "T@\"NSString\",R,N,V_codeInfoIdentifier"
- "T@\"NSString\",R,N,V_complicationPrincipalClass"
- "T@\"NSString\",R,N,V_displayName"
- "T@\"NSString\",R,N,V_execPath"
- "T@\"NSString\",R,N,V_genre"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSString\",R,N,V_identityString"
- "T@\"NSString\",R,N,V_identityUsageDescription"
- "T@\"NSString\",R,N,V_itemName"
- "T@\"NSString\",R,N,V_libraryPath"
- "T@\"NSString\",R,N,V_linkedParentBundleID"
- "T@\"NSString\",R,N,V_managementDeclarationIdentifier"
- "T@\"NSString\",R,N,V_maxSystemVersion"
- "T@\"NSString\",R,N,V_microphoneUsageDescription"
- "T@\"NSString\",R,N,V_minSystemVersion"
- "T@\"NSString\",R,N,V_name"
- "T@\"NSString\",R,N,V_originalIdentifier"
- "T@\"NSString\",R,N,V_personaUniqueString"
- "T@\"NSString\",R,N,V_pluginIdentifier"
- "T@\"NSString\",R,N,V_primaryIconName"
- "T@\"NSString\",R,N,V_protocol"
- "T@\"NSString\",R,N,V_ratingLabel"
- "T@\"NSString\",R,N,V_sdkVersion"
- "T@\"NSString\",R,N,V_secondCategoryType"
- "T@\"NSString\",R,N,V_serializedPlaceholderPath"
- "T@\"NSString\",R,N,V_shortDisplayName"
- "T@\"NSString\",R,N,V_shortVersionString"
- "T@\"NSString\",R,N,V_signerIdentity"
- "T@\"NSString\",R,N,V_signerOrganization"
- "T@\"NSString\",R,N,V_sourceApp"
- "T@\"NSString\",R,N,V_sourceAppBundleID"
- "T@\"NSString\",R,N,V_storeCohort"
- "T@\"NSString\",R,N,V_symbolImageName"
- "T@\"NSString\",R,N,V_teamID"
- "T@\"NSString\",R,N,V_type"
- "T@\"NSString\",R,N,V_typeIdentifier"
- "T@\"NSString\",R,N,V_unlocalizedTitle"
- "T@\"NSString\",R,N,V_variantID"
- "T@\"NSString\",R,N,V_vendorName"
- "T@\"NSString\",R,N,V_version"
- "T@\"NSString\",R,N,V_watchKitVersion"
- "T@\"NSString\",R,V_bundleIdentifier"
- "T@\"NSString\",R,V_bundleShortVersion"
- "T@\"NSString\",R,V_exactBundleVersion"
- "T@\"NSString\",R,V_personaUniqueString"
- "T@\"NSString\",R,V_signerOrganization"
- "T@\"NSTimer\",&,N,V_timer"
- "T@\"NSURL\",&,N,V_destURL"
- "T@\"NSURL\",&,N,V_resourcesDirectoryURL"
- "T@\"NSURL\",C,N,V_referrerURL"
- "T@\"NSURL\",C,V_URL"
- "T@\"NSURL\",R"
- "T@\"NSURL\",R,C,N,V_URL"
- "T@\"NSURL\",R,C,N,V_overrideURL"
- "T@\"NSURL\",R,D"
- "T@\"NSURL\",R,D,N"
- "T@\"NSURL\",R,N"
- "T@\"NSURL\",R,N,V_URL"
- "T@\"NSURL\",R,N,V_bundleContainerURL"
- "T@\"NSURL\",R,N,V_bundleURL"
- "T@\"NSURL\",R,N,V_dataContainerURL"
- "T@\"NSURL\",R,N,V_originalURL"
- "T@\"NSURLComponents\",&,V_URLComponents"
- "T@\"NSUUID\",&,N,V_uuid"
- "T@\"NSUUID\",R"
- "T@\"NSUUID\",R,D,N"
- "T@\"NSUUID\",R,N"
- "T@\"NSUUID\",R,N,V_cacheGUID"
- "T@\"NSUUID\",R,N,V_dbUUID"
- "T@\"NSUUID\",R,N,V_pluginUUID"
- "T@\"NSXPCConnection\",&,N"
- "T@\"NSXPCConnection\",&,V_clientXPCConnection"
- "T@\"NSXPCConnection\",R,&,V_XPCConnection"
- "T@\"NSXPCConnection\",W,N,V_connection"
- "T@\"NSXPCListener\",&,V_listener"
- "T@\"NSXPCListener\",R,V_listener"
- "T@\"NSXPCListenerEndpoint\",R,V_endpoint"
- "T@\"UISClickAttribution\",&,N,V_clickAttribution"
- "T@\"UISPasteSharingToken\",&,N,V_pasteSharingToken"
- "T@\"UTTypeRecord\",R,V_typeRecord"
- "T@\"_LSAppLinkOpenState\",&,V_state"
- "T@\"_LSApplicationSensitiveDataProxy\",R,V_sensitiveDataProxy"
- "T@\"_LSApplicationState\",R"
- "T@\"_LSApplicationState\",R,N"
- "T@\"_LSBoundIconInfo\",&,N,S_setBoundIconInfo:,V__boundIconInfo"
- "T@\"_LSBundleProvider\",R,&,V_bundleProvider"
- "T@\"_LSCanOpenURLManager\",R"
- "T@\"_LSDiskUsage\",R"
- "T@\"_LSDiskUsage\",R,D,N"
- "T@\"_LSLazyPropertyList\",C,N,S_setEntitlements:,V__entitlements"
- "T@\"_LSLazyPropertyList\",C,N,S_setEnvironmentVariables:,V__environmentVariables"
- "T@\"_LSLazyPropertyList\",C,N,S_setIconsDictionary:,V__iconsDictionary"
- "T@\"_LSLazyPropertyList\",C,N,S_setInfoDictionary:,V__infoDictionary"
- "T@\"_LSLazyPropertyList\",R"
- "T@\"_LSLocalizedStringRecord\",R"
- "T@\"_LSOpenConfiguration\",&,V_openConfiguration"
- "T@\"_LSStringLocalizer\",R"
- "T@\"_SWCServiceDetails\",&,N,V_serviceDetails"
- "T@,&,V_result"
- "T@,R,&,N,V_propertyList"
- "T@,R,D,N"
- "T@,R,N"
- "T@?,C,N"
- "T@?,C,N,V_errorHandler"
- "TB,D"
- "TB,D,N,GisEnabled"
- "TB,GisLightweightSystemServer,V_isLightweightSystemServer"
- "TB,GisObservinglsd,V_observinglsd"
- "TB,GisServer,V_isServer"
- "TB,N"
- "TB,N,G_isShared,S_setShared:"
- "TB,N,GisLegacy,V_legacy"
- "TB,N,GisSensitive,V_sensitive"
- "TB,N,V_allowURLOverrides"
- "TB,N,V_ignoreAppLinkEnabledProperty"
- "TB,N,V_shouldSetHandlerOnDocumentOpen"
- "TB,N,V_useOneTapOpenBehavior"
- "TB,N,V_userInitiatedUninstall"
- "TB,N,V_yieldClaimBindings"
- "TB,R"
- "TB,R,D"
- "TB,R,D,GisFreeProfileValidated"
- "TB,R,D,GisProfileValidated"
- "TB,R,D,GisRegionChina"
- "TB,R,D,GisSystemServer"
- "TB,R,D,GisUPPValidated"
- "TB,R,D,GisUserServer"
- "TB,R,D,N"
- "TB,R,D,N,GisAdHocCodeSigned"
- "TB,R,D,N,GisAliasFile"
- "TB,R,D,N,GisAppStoreVendable"
- "TB,R,D,N,GisArcadeApp"
- "TB,R,D,N,GisBusyDirectory"
- "TB,R,D,N,GisDeletable"
- "TB,R,D,N,GisDirectory"
- "TB,R,D,N,GisExecutable"
- "TB,R,D,N,GisExecutableModeFile"
- "TB,R,D,N,GisHidden"
- "TB,R,D,N,GisLaunchProhibited"
- "TB,R,D,N,GisMountTrigger"
- "TB,R,D,N,GisOnDiskImage"
- "TB,R,D,N,GisOnLocalVolume"
- "TB,R,D,N,GisOpenWindowGroupFull"
- "TB,R,D,N,GisRegularFile"
- "TB,R,D,N,GisResolvable"
- "TB,R,D,N,GisSecuredSystemContent"
- "TB,R,D,N,GisSideFault"
- "TB,R,D,N,GisSymbolicLink"
- "TB,R,D,N,GisVolume"
- "TB,R,G_isVocabularyType"
- "TB,R,GisAVCHDCollection"
- "TB,R,GisAccessing"
- "TB,R,GisActive"
- "TB,R,GisAdHocCodeSigned"
- "TB,R,GisArcadeApp"
- "TB,R,GisBeta"
- "TB,R,GisContainerized"
- "TB,R,GisCoreType"
- "TB,R,GisDeclared"
- "TB,R,GisDeletable"
- "TB,R,GisDeletableSystemApplication"
- "TB,R,GisDynamic"
- "TB,R,GisEligibleMailClient"
- "TB,R,GisEligibleWebBrowser"
- "TB,R,GisEnabled"
- "TB,R,GisExported"
- "TB,R,GisFileSharingEnabled"
- "TB,R,GisFreeProfileValidated"
- "TB,R,GisGameCenterEnabled"
- "TB,R,GisImageOrVideo"
- "TB,R,GisImported"
- "TB,R,GisInEducationMode,V_inEducationMode"
- "TB,R,GisInPublicDomain"
- "TB,R,GisInSyncBubble,V_inSyncBubble"
- "TB,R,GisLaunchDisabled"
- "TB,R,GisLaunchProhibited"
- "TB,R,GisMailClient"
- "TB,R,GisPlaceholder"
- "TB,R,GisProfileValidated"
- "TB,R,GisRemovableByInstallMachinery"
- "TB,R,GisSwiftPlaygroundsApp"
- "TB,R,GisSystemPlaceholder"
- "TB,R,GisTrustedForBinding"
- "TB,R,GisUPPValidated"
- "TB,R,GisUpdate"
- "TB,R,GisUsingEphemeralStorage,V_usingEphemeralStorage"
- "TB,R,GisWatchOnly"
- "TB,R,GisWebApp"
- "TB,R,GisWebAppPlaceholder"
- "TB,R,GisWebBrowser"
- "TB,R,GisWildcard"
- "TB,R,GisWrapped"
- "TB,R,GisWrapper"
- "TB,R,GisiWorkURL"
- "TB,R,GwasBuiltWithThreadSanitizer"
- "TB,R,GwasRenamed"
- "TB,R,N"
- "TB,R,N,GareEnabledByDefault"
- "TB,R,N,GisAliasFile"
- "TB,R,N,GisAlwaysAvailable"
- "TB,R,N,GisAppStoreVendable"
- "TB,R,N,GisAppUpdate"
- "TB,R,N,GisAppleInternal,V_appleInternal"
- "TB,R,N,GisBetaApp"
- "TB,R,N,GisBlocked"
- "TB,R,N,GisBusyDirectory"
- "TB,R,N,GisContainerized,V_containerized"
- "TB,R,N,GisContentManaged,V_isContentManaged"
- "TB,R,N,GisDefaultForCategory,V_defaultForCategory"
- "TB,R,N,GisDeviceBasedVPP"
- "TB,R,N,GisDeviceBasedVPP,V_deviceBasedVPP"
- "TB,R,N,GisDirectory"
- "TB,R,N,GisDowngraded"
- "TB,R,N,GisExecutable"
- "TB,R,N,GisExecutableModeFile"
- "TB,R,N,GisGameCenterEnabled"
- "TB,R,N,GisGameCenterEnabled,V_gameCenterEnabled"
- "TB,R,N,GisHidden"
- "TB,R,N,GisInXCTestRigInsecure,V_inXCTestRigInsecure"
- "TB,R,N,GisInstalled"
- "TB,R,N,GisMountTrigger"
- "TB,R,N,GisNewsstandApp"
- "TB,R,N,GisOnDiskImage"
- "TB,R,N,GisOnLocalVolume"
- "TB,R,N,GisOnSystemPartition,V_onSystemPartition"
- "TB,R,N,GisPlaceholder"
- "TB,R,N,GisPurchasedReDownload"
- "TB,R,N,GisPurchasedRedownload,V_purchasedRedownload"
- "TB,R,N,GisRegularFile"
- "TB,R,N,GisRemoveableSystemApp"
- "TB,R,N,GisRemovedSystemApp"
- "TB,R,N,GisResolvable"
- "TB,R,N,GisRestricted"
- "TB,R,N,GisSecuredSystemContent"
- "TB,R,N,GisSideFault"
- "TB,R,N,GisStandaloneWatchApp"
- "TB,R,N,GisSymbolicLink"
- "TB,R,N,GisValid"
- "TB,R,N,GisVolume"
- "TB,R,N,GisWatchKitApp"
- "TB,R,N,GisWhitelisted"
- "TB,R,N,GwasGameCenterEverEnabled,V_gameCenterEverEnabled"
- "TB,R,N,V_containerized"
- "TB,R,N,V_didRefresh"
- "TB,R,N,V_foundBackingBundle"
- "TB,R,N,V_includePlugins"
- "TB,R,N,V_isPlaceholder"
- "TB,R,N,V_plugins"
- "TB,R,N,V_registerChildItemsTrusted"
- "TB,R,N,V_webNotificationPlaceholder"
- "TB,R,V_hasPersistentPreferences"
- "TB,V_callCompletionHandlerWhenFullyComplete"
- "TB,V_hasServer"
- "TB,V_includeLinksForCallingApplication"
- "TC,N,V_profileValidationState"
- "TC,N,V_retries"
- "TC,R"
- "TCCPolicy"
- "TCCPolicyWithContext:tableID:unitID:unitBytes:"
- "TI,N,V_previousInstallType"
- "TI,N,Vaction"
- "TI,N,Vversion"
- "TI,R"
- "TI,R,N,V_plistFlags"
- "TI,V_bundleClass"
- "TQ,N"
- "TQ,N,S_setCompatibilityState:,V_compatibilityState"
- "TQ,N,Sls_setExpectedFinalInstallPhase:"
- "TQ,N,V_sequenceNumber"
- "TQ,R"
- "TQ,R,D,N"
- "TQ,R,N"
- "TQ,R,N,V_betaVersionIdentifier"
- "TQ,R,N,V_bundleFlags"
- "TQ,R,N,V_genreIdentifier"
- "TQ,R,N,V_personaType"
- "TQ,R,N,V_ratingRank"
- "TQ,R,N,V_sequenceNumber"
- "TQ,R,N,V_storeFront"
- "TQ,R,N,V_storeItemIdentifier"
- "TQ,R,N,V_type"
- "TQ,R,N,V_versionIdentifier"
- "TQ,R,V_provenance"
- "TQ,V_limit"
- "TS,R"
- "T^v,R"
- "T^{LSContext=@},R"
- "T^{sqlite3=},N,V_database"
- "Tc,R"
- "Td,R"
- "Td,R,N,V_latency"
- "Td,R,N,V_minInterval"
- "Testing"
- "Tests"
- "Ti,N,V_callbackType"
- "Ti,R"
- "Ti,R,N"
- "Ti,R,N,V_notification"
- "Ti,R,N,V_subtype"
- "Ti,R,N,V_type"
- "Tq,D"
- "Tq,R"
- "Tq,R,N"
- "Tr^{?=[8I]},N"
- "Tr^{?=[8I]},R,D,N"
- "Tr^{?=[8I]},R,N"
- "Transitional"
- "T{LSBinding=I^{LSBundleData}I^{?}@@Q},R,V_binding"
- "T{LSBundleBaseFlags=b1b1b1b1b1b1b1},R"
- "T{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1},R"
- "T{LSVersionNumber=[32C]},R"
- "T{LSVersionNumber=[32C]},R,N"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathComponent:isDirectory:"
- "URLByAppendingPathExtension:"
- "URLByDeletingLastPathComponent"
- "URLByDeletingPathExtension"
- "URLByResolvingAliasFileAtURL:options:error:"
- "URLByResolvingSymlinksInPath"
- "URLClaims"
- "URLComponents"
- "URLComponentsAreValidForAppLinks:error:"
- "URLForDirectory:inDomain:appropriateForURL:create:error:"
- "URLForKey:"
- "URLForUnit:inTable:"
- "URLOfDefaultAppForCategory:"
- "URLOverrideForNewsURL:"
- "URLOverrideForURL:"
- "URLQueries"
- "URLSchemes"
- "URLSchemesWithContext:tableID:unitID:unitBytes:"
- "URLWithString:"
- "URLsForDirectory:inDomains:"
- "UTF8String"
- "UTTypeRecord"
- "UUIDString"
- "Unimplemented exception"
- "UniqueIdentifiers"
- "UserActivity"
- "Utility"
- "VPNPluginProxyForIdentifier:"
- "VPNPluginProxyForIdentifier:withContext:"
- "VPNPlugins"
- "VPNPluginsWithContext:tableID:unitID:unitBytes:"
- "Vv16@0:8"
- "WKBackgroundModes"
- "WebKitChangeTracking"
- "XPCConnection"
- "XPCConnectionIsAlwaysPrivileged"
- "XPCConnectionToService"
- "XPCInterface"
- "XPCListenerEndpoint"
- "^v"
- "^v16@0:8"
- "^v24@0:8^@16"
- "^{?=[8I]}"
- "^{LSContext=@}16@0:8"
- "^{PerThreadContext=@@BB{unfair_lock_mutex=I}}16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__CFBundle=}16@0:8"
- "^{__CFBundle=}24@0:8^@16"
- "^{__CFBundle=}28@0:8B16@20"
- "^{__CSStore=}"
- "^{__CSStoreAccessContext=}"
- "^{sqlite3=}"
- "^{sqlite3=}16@0:8"
- "_DYLD_CLOSURE_HOME"
- "_EXStartService"
- "_HMAC"
- "_LSAggregatePropertyList"
- "_LSAppLinkOpenState"
- "_LSAppLinkPlugIn"
- "_LSAppToUnregister"
- "_LSApplicationExtensionRecordEnumerator"
- "_LSApplicationIsInstalledQuery"
- "_LSApplicationProxiesOfTypeQuery"
- "_LSApplicationProxiesWithFlagsQuery"
- "_LSApplicationProxyEnumerator"
- "_LSApplicationProxyForIdentifierQuery"
- "_LSApplicationRecordEnumerator"
- "_LSApplicationRecordSpecificUnitsEnumerator"
- "_LSApplicationRecordsWithinDirectoryEnumerator"
- "_LSApplicationSensitiveDataProxy"
- "_LSApplicationState"
- "_LSApplyRestrictedSet:forRestriction:"
- "_LSAvailableApplicationsForURLQuery"
- "_LSBindingForLog"
- "_LSBoundIconInfo"
- "_LSBundleFlagMap"
- "_LSBundleIDValidationToken"
- "_LSBundleIdentifierAndType"
- "_LSBundleProvider"
- "_LSBundleProxiesOfTypeQuery"
- "_LSBundleQuery"
- "_LSCanOpenURLManager"
- "_LSChangeObserver"
- "_LSClaimBindingDocumentProxyBindable"
- "_LSClaimBindingTypeIdentifierBindable"
- "_LSClaimBindingURLBindable"
- "_LSClearSchemaCaches"
- "_LSClientSettingsStore"
- "_LSCompatibilityNothingBindable"
- "_LSCoreTypesRecordProxy"
- "_LSCurrentBundleProxyQuery"
- "_LSDAppProtectionAccessManager"
- "_LSDAppProtectionClient"
- "_LSDAppProtectionProtocol"
- "_LSDBEnumerator"
- "_LSDClient"
- "_LSDDeviceIdentifierClient"
- "_LSDDeviceIdentifierProtocol"
- "_LSDIconClient"
- "_LSDIconServiceProtocol"
- "_LSDModificationPendingSaveToken"
- "_LSDModifyClient"
- "_LSDModifyProtocol"
- "_LSDOpenClient"
- "_LSDOpenProtocol"
- "_LSDReadClient"
- "_LSDReadProtocol"
- "_LSDRebuildClient"
- "_LSDRebuildServiceProtocol"
- "_LSDServiceDomain"
- "_LSDataBackedPropertyList"
- "_LSDatabase"
- "_LSDefaultFeatureFlagResolver"
- "_LSDefaults"
- "_LSDescription"
- "_LSDeviceIdentifierCache"
- "_LSDeviceIdentifierManager"
- "_LSDictionaryBackedPropertyList"
- "_LSDiskUsage"
- "_LSDispatchWithTimeoutResult"
- "_LSDisplayNameConstructor"
- "_LSDocumentProxyBindingQuery"
- "_LSEligibilityListenerNotificationToken"
- "_LSEmptyEnumerator"
- "_LSEmptyPropertyList"
- "_LSEnumeratedBundleInfo"
- "_LSErrorEnumerator"
- "_LSExtensionPointEnumerator"
- "_LSExtensionPointRecordEnumerator"
- "_LSFailedToOpenURL:withBundle:"
- "_LSFindPlaceholderApplications"
- "_LSInProcessSettingsStore"
- "_LSInstallNotificationJournaller"
- "_LSInstallProgressService"
- "_LSJournalledNotification"
- "_LSKeyTypeMap"
- "_LSLazyPropertyList"
- "_LSLinkedChildApplicationRecordEnumerator"
- "_LSLocalQueryResolver"
- "_LSLocalizedStringRecord"
- "_LSOpenConfiguration"
- "_LSOpenCopierContext"
- "_LSOpenResourceOperationDelegateWrapper"
- "_LSPendingSaveToken"
- "_LSPersonaDatabase"
- "_LSPersonaWithAttributes"
- "_LSPlistHint"
- "_LSPlistRaritiesMap"
- "_LSPlugInPropertyList"
- "_LSPlugInProxyEnumerator"
- "_LSPrivateAskLSDToExitSafely:completionHandler:"
- "_LSPrivateDatabaseNeedsRebuild"
- "_LSPrivateNoteMigratorRunning"
- "_LSPrivateRebuildApplicationDatabasesForSystemApps:internal:user:"
- "_LSPrivateRebuildApplicationDatabasesForSystemApps:internal:user:uid:"
- "_LSPrivateRebuildDatabaseAtNextRestart:"
- "_LSPrivateRemovedSystemAppIdentifiers"
- "_LSPrivateSetRemovedSystemAppIdentifiers:"
- "_LSPrivateSyncWithMobileInstallation"
- "_LSPrivateUpdateAppRemovalRestrictions"
- "_LSQuery"
- "_LSQueryContext"
- "_LSQueryResolving"
- "_LSQueryResult"
- "_LSQueryResultWithPropertyList"
- "_LSRecordEnumerator"
- "_LSRecord_resolve_SDKDictionary"
- "_LSRecord_resolve_TCCPolicy"
- "_LSRecord_resolve_URLSchemes"
- "_LSRecord_resolve_VPNPlugins"
- "_LSRecord_resolve__allUnsanitizedStringValues"
- "_LSRecord_resolve__baseFlags"
- "_LSRecord_resolve__bundleModTime"
- "_LSRecord_resolve__bundleVersion"
- "_LSRecord_resolve__claimingBundleRecord"
- "_LSRecord_resolve__containingBundleRecord"
- "_LSRecord_resolve__contextualFeatureUsageDescriptions"
- "_LSRecord_resolve__dataContainerURLFromDatabase"
- "_LSRecord_resolve__declaringBundleBookmark"
- "_LSRecord_resolve__declaringBundleRecord"
- "_LSRecord_resolve__defaultCategoryTypeIdentifiers"
- "_LSRecord_resolve__delegatePath"
- "_LSRecord_resolve__deviceIdentifierVendorName"
- "_LSRecord_resolve__iconFileNames"
- "_LSRecord_resolve__linkedParentApplicationBundleID"
- "_LSRecord_resolve__localizedDescription"
- "_LSRecord_resolve__localizedName"
- "_LSRecord_resolve__localizedNamesWithContext"
- "_LSRecord_resolve__localizedShortName"
- "_LSRecord_resolve__missingBundleLocs"
- "_LSRecord_resolve__personasWithAttributes"
- "_LSRecord_resolve__preferredLaunchArchitecture"
- "_LSRecord_resolve__profileValidationState"
- "_LSRecord_resolve__rawBundleFlags"
- "_LSRecord_resolve__rawEnvironmentVariables"
- "_LSRecord_resolve__rawFlags"
- "_LSRecord_resolve__rawGroupContainerURLs"
- "_LSRecord_resolve__rawIconDictionary"
- "_LSRecord_resolve__rawIconFlags"
- "_LSRecord_resolve__rawMoreFlags"
- "_LSRecord_resolve__rawPlistFlags"
- "_LSRecord_resolve__referenceAccessoryPath"
- "_LSRecord_resolve_appClipMetadata"
- "_LSRecord_resolve_appProtectionEffectiveContainer"
- "_LSRecord_resolve_appProtectionHidden"
- "_LSRecord_resolve_appProtectionLocked"
- "_LSRecord_resolve_appStoreToolsBuildVersion"
- "_LSRecord_resolve_appTags"
- "_LSRecord_resolve_applicationExtensionRecords"
- "_LSRecord_resolve_applicationState"
- "_LSRecord_resolve_audioComponents"
- "_LSRecord_resolve_backgroundTaskSchedulerPermittedIdentifiers"
- "_LSRecord_resolve_bundleContainerURL"
- "_LSRecord_resolve_carPlayInstrumentClusterURLSchemes"
- "_LSRecord_resolve_claimRecords"
- "_LSRecord_resolve_codeSignatureVersion"
- "_LSRecord_resolve_companionBundleIdentifier"
- "_LSRecord_resolve_compatibilityState"
- "_LSRecord_resolve_counterpartIdentifiers"
- "_LSRecord_resolve_declaration"
- "_LSRecord_resolve_developerType"
- "_LSRecord_resolve_deviceFamilies"
- "_LSRecord_resolve_directionsModes"
- "_LSRecord_resolve_diskUsage"
- "_LSRecord_resolve_driverExtensionPaths"
- "_LSRecord_resolve_effectiveBundleIdentifier"
- "_LSRecord_resolve_entitlements"
- "_LSRecord_resolve_equivalentBundleIdentifiers"
- "_LSRecord_resolve_exactBundleVersion"
- "_LSRecord_resolve_execSDKVersion"
- "_LSRecord_resolve_executableURL"
- "_LSRecord_resolve_exportedTypeRecords"
- "_LSRecord_resolve_extensionPointRecord"
- "_LSRecord_resolve_extensionPointRecords"
- "_LSRecord_resolve_extensionPointType"
- "_LSRecord_resolve_externalAccessoryProtocols"
- "_LSRecord_resolve_handlerRank"
- "_LSRecord_resolve_iTunesMetadata"
- "_LSRecord_resolve_iconDictionary"
- "_LSRecord_resolve_iconResourceBundleURL"
- "_LSRecord_resolve_identifier"
- "_LSRecord_resolve_importedTypeRecords"
- "_LSRecord_resolve_infoDictionary"
- "_LSRecord_resolve_installSessionIdentifier"
- "_LSRecord_resolve_installType"
- "_LSRecord_resolve_intentDefinitionURLs"
- "_LSRecord_resolve_isAppStoreVendable"
- "_LSRecord_resolve_isAppleInternal"
- "_LSRecord_resolve_isDeletable"
- "_LSRecord_resolve_isDeletableSystemApplication"
- "_LSRecord_resolve_isLinkEnabled"
- "_LSRecord_resolve_isSystemPlaceholder"
- "_LSRecord_resolve_machOUUIDs"
- "_LSRecord_resolve_managementDomain"
- "_LSRecord_resolve_maximumSystemVersion"
- "_LSRecord_resolve_minimumSystemVersion"
- "_LSRecord_resolve_name"
- "_LSRecord_resolve_parentAppRecord"
- "_LSRecord_resolve_parentTypeIdentifiers"
- "_LSRecord_resolve_pedigree"
- "_LSRecord_resolve_placeholderFailureReason"
- "_LSRecord_resolve_platform"
- "_LSRecord_resolve_pluginFlags"
- "_LSRecord_resolve_referenceURL"
- "_LSRecord_resolve_registrationDate"
- "_LSRecord_resolve_regulatoryPrivacyDisclosureVersion"
- "_LSRecord_resolve_requiredDeviceCapabilities"
- "_LSRecord_resolve_role"
- "_LSRecord_resolve_sensitiveDataProxy"
- "_LSRecord_resolve_serializedPlaceholderURL"
- "_LSRecord_resolve_shortVersionString"
- "_LSRecord_resolve_signerIdentity"
- "_LSRecord_resolve_signerOrganization"
- "_LSRecord_resolve_stashedAppMetadata"
- "_LSRecord_resolve_staticShortcutItems"
- "_LSRecord_resolve_supportedGameControllers"
- "_LSRecord_resolve_tagSpecification"
- "_LSRecord_resolve_teamIdentifier"
- "_LSRecord_resolve_typeForInstallMachinery"
- "_LSRecord_resolve_typeIdentifiers"
- "_LSRecord_resolve_uniqueIdentifier"
- "_LSRecord_resolve_uniqueInstallIdentifier"
- "_LSRecord_resolve_userActivityTypes"
- "_LSRecord_resolve_version"
- "_LSRegistrationNotificationJournaller"
- "_LSRemotePlaceholderEnumerator"
- "_LSResolveIdentifiers:"
- "_LSResolveIdentifiers:context:"
- "_LSResume"
- "_LSServerSettingsStore"
- "_LSServerSettingsStoreXPCProtocol"
- "_LSSettingStoreChangeObserver"
- "_LSSharedWebCredentialsAppLink"
- "_LSSharedWebCredentialsAppLinkPlugIn"
- "_LSShouldFetchContainersFromContainermanagerForPersona"
- "_LSSpringBoardCall"
- "_LSStackBacktrace"
- "_LSStartupJournalledDatabaseRebuiltNotification"
- "_LSStartupJournalledInstallNotification"
- "_LSStartupJournalledNotification"
- "_LSStringLocalizer"
- "_LSStringsFileContent"
- "_LSSynthesizedExtensionPointRecord"
- "_LSTypeEnumerator"
- "_LSURLOverride"
- "_LSValidationToken"
- "_LSXPCQueryResolver"
- "_LS_BoolForKey:"
- "_LS_UUIDWithData:digestType:"
- "_LS_frameworkFileManager"
- "_LS_integerForKey:"
- "_LS_nullUUID"
- "_MCProfileConnection"
- "_MCRestrictionManager"
- "_MIMEType"
- "_SWCSettingsReturningError:"
- "_SWCSettingsWithApplicationIdentifier:error:"
- "_SWCSpecifierForSettings"
- "_SWCSpecifierForSettingsWithApplicationIdentifier:"
- "_URL"
- "_URLClaims"
- "_URLComponents"
- "_URLIsValidForAppLinks:error:"
- "_UTDeclaredTypeRecord"
- "_UTDynamicTypeRecord"
- "_UTUndeclaredTypeRecord"
- "_XPCConnection"
- "__LSRECORD_NULL_PLACEHOLDER__"
- "__boundIconInfo"
- "__entitlements"
- "__environmentVariables"
- "__iconsDictionary"
- "__infoDictionary"
- "__internalQueue_xpcConnectionWithError:"
- "__isDirectlyOneTapOpenable"
- "__personasWithAttributes"
- "_activeTokens"
- "_activityTypes"
- "_addClaimRecordIfMissing"
- "_addSubscriberForCategory:usingPublishingHandler:"
- "_advertiserIdentifier"
- "_alertManager"
- "_allUnsanitizedStringValues"
- "_allUnsanitizedStringValuesWithContext:tableID:unitID:unitBytes:"
- "_allowURLOverrides"
- "_allowlistEnabled"
- "_allowlistState"
- "_allowlistedBundleIDs"
- "_allowlistedBundles"
- "_alternateIconQueue"
- "_alternatePrimaryIconName"
- "_appClipPlist"
- "_appLinkWithURL:applicationRecord:plugInClass:"
- "_appLinksWithState:context:limit:URLComponents:error:"
- "_appLinksWithState:context:limit:error:"
- "_appObserverSelector"
- "_appStoreToolsBuildVersion"
- "_appType"
- "_appVariant"
- "_appexRecord"
- "_appleInternal"
- "_applicationDSID"
- "_applicationIdentifier"
- "_applicationManagementDomain"
- "_applicationRecordWithContext:bundleIdentifierOrUnit:"
- "_applications"
- "_areAppLinksEnabledForServiceDetails:cachedSettings:"
- "_artistName"
- "_attributedDescription"
- "_auditToken"
- "_badge"
- "_baseBindingEvaluatorForBindableWithAuditToken:"
- "_baseFlags"
- "_baseFlagsWithContext:tableID:unitID:unitBytes:"
- "_baseName"
- "_baseProperties"
- "_baseSystemContainerURL"
- "_betaVersionIdentifier"
- "_bgPermittedIdentifiers"
- "_bindable"
- "_binding"
- "_bindingConfiguration"
- "_bindingEvaluatorResultFilterForBindingStyle:contentIsManaged:sourceAuditToken:"
- "_bindingMap"
- "_bindingStyle"
- "_boundIconInfo"
- "_browserState"
- "_bundleAlias"
- "_bundleClass"
- "_bundleClassMask"
- "_bundleContainerURL"
- "_bundleData"
- "_bundleExecutable"
- "_bundleFlags"
- "_bundleID"
- "_bundleIdentifier"
- "_bundleIdentifiersOrUnits"
- "_bundleLocalizations"
- "_bundleLocalizationsWithDefaultPrefLocs"
- "_bundleModTime"
- "_bundleModTimeWithContext:tableID:unitID:unitBytes:"
- "_bundleName"
- "_bundlePersonas"
- "_bundleProvider"
- "_bundleRecord"
- "_bundleRecordForAuditToken:checkNSBundleMainBundle:error:"
- "_bundleShortVersion"
- "_bundleURL"
- "_bundleVersion"
- "_bundleVersionWithContext:tableID:unitID:unitBytes:"
- "_cache"
- "_cacheExpiration"
- "_cacheGUID"
- "_cacheKey"
- "_cachedBundleIDToPersonasMap"
- "_cachedDataContainerURL"
- "_cachedPersonalPersonaUniqueString"
- "_cachedSystemMode"
- "_cachedSystemPersonaUniqueString"
- "_cachedValues"
- "_cachedValuesAreComplete"
- "_callCompletionHandlerWhenFullyComplete"
- "_callbackType"
- "_canOpenURLsMap"
- "_canOpenURLsMapQueue"
- "_canRegisterOrUnregisterURL:withOptions:"
- "_canResolveLocallyWithoutMappingDatabase"
- "_canUseFileCache"
- "_carPlayInstrumentClusterURLSchemes"
- "_categoryType"
- "_changeObserver"
- "_checkNotRedacted"
- "_claimBindingsForBindingEvaluator:error:"
- "_claimRecord"
- "_claimingBundleRecord"
- "_claimingBundleRecordWithContext:tableID:unitID:unitBytes:"
- "_clickAttribution"
- "_clientMap"
- "_clientMapMutex"
- "_clientXPCConnection"
- "_codeInfoIdentifier"
- "_commonInfoPlistEntries"
- "_compatibilityObjectWithContext:tableID:unitID:unitBytes:"
- "_compatibilityState"
- "_complicationPrincipalClass"
- "_configuration"
- "_configureCallbacks"
- "_connection"
- "_constantTypeForURLPropertyProviderWithIdentifier:"
- "_containerClass"
- "_containerURL"
- "_containerized"
- "_containerizedContentScanTime"
- "_containingBundle"
- "_containingBundleRecord"
- "_containingBundleRecordWithContext:tableID:unitID:unitBytes:"
- "_context"
- "_contextualFeatureUsageDescriptions"
- "_contextualFeatureUsageDescriptionsWithContext:tableID:unitID:unitBytes:"
- "_contextualIdentityUsageDescriptions"
- "_counterpartAppBundleIDs"
- "_createPostflightedApplicationRecordWithContext:bundleUnit:bundleData:"
- "_createUserActivityDataWithOptions:completionHandler:"
- "_createdInstallProgresses"
- "_creator"
- "_cryptexContentScanTime"
- "_ctx"
- "_ctxError"
- "_currentDisplayGamut"
- "_currentRecord"
- "_currentRecordIdentitiesEnumerator"
- "_darwinNotificationNames"
- "_darwinNotificationNamesLock"
- "_darwinNotificationNamesUID"
- "_dataContainerURL"
- "_dataContainerURLFromDatabase"
- "_dataContainerURLFromDatabaseWithContext:tableID:unitID:unitBytes:"
- "_database"
- "_databaseLeftWritable"
- "_databaseLock"
- "_datastore"
- "_dateOriginallyInstalled"
- "_dateStashed"
- "_db"
- "_dbCloseTimer"
- "_dbLock"
- "_dbUUID"
- "_declaringBundleBookmark"
- "_declaringBundleBookmarkWithContext:tableID:unitID:unitBytes:"
- "_declaringBundleRecord"
- "_declaringBundleRecordWithContext:tableID:unitID:unitBytes:"
- "_defaultAppEvaluator"
- "_defaultAppQueue"
- "_defaultCategoryTypeIdentifiers"
- "_defaultCategoryTypeIdentifiersWithContext:tableID:unitID:unitBytes:"
- "_defaultForCategory"
- "_delegate"
- "_delegatePath"
- "_delegatePathWithContext:tableID:unitID:unitBytes:"
- "_description"
- "_destURL"
- "_detachFromContext:tableID:unitID:unitBytes:"
- "_determineMatchingApplicationBundleIdentifierWithOptions:"
- "_deviceBasedVPP"
- "_deviceFamily"
- "_deviceIdentifierVendorName"
- "_deviceIdentifierVendorNameWithContext:tableID:unitID:unitBytes:"
- "_didRefresh"
- "_directoryClass"
- "_directoryURL"
- "_discardableContentCounter"
- "_dispatchQueue"
- "_displayName"
- "_distributorInfo"
- "_documentAllowOverride"
- "_documentClaims"
- "_documentProxy"
- "_downloaderDSID"
- "_driverExtensionPaths"
- "_effectiveSettings"
- "_endpoint"
- "_entitlements"
- "_enumerateAllBundles"
- "_enumerateRelatedTypeStructuresWithContext:unitID:maximumDegreeOfSeparation:block:"
- "_enumerateRelatedTypeUnitsOrDynamicIdsWithContext:unitID:maximumDegreeOfSeparation:block:"
- "_enumerateRelatedTypesWithMaximumDegreeOfSeparation:block:"
- "_enumerateResolvedResultsOfQuery:XPCConnection:withBlock:"
- "_enumerateWithXPCConnection:block:"
- "_enumerationOptions"
- "_environmentVariables"
- "_equivalentBundleIDs"
- "_error"
- "_errorHandler"
- "_evaluatePluginNoIO:data:extensionPointID:context:"
- "_exactBundleVersion"
- "_execPath"
- "_expensiveDictionaryRepresentation"
- "_exportedTypes"
- "_extantTokens"
- "_extension"
- "_extensionIDs"
- "_extensionIdentifiers"
- "_extensionPointID"
- "_extensionPointIdentifiers"
- "_extensionPointRecord"
- "_extensionSDK"
- "_fallbackLocalizedName"
- "_familyID"
- "_fetchWithXPCConnection:error:"
- "_fileNames"
- "_filter"
- "_filterBlock"
- "_filteringOptions"
- "_flags"
- "_forManualRebuild"
- "_foundBackingBundle"
- "_frames"
- "_frontBoardOptions"
- "_fullAppInstalled"
- "_gameCenterEnabled"
- "_gameCenterEverEnabled"
- "_genre"
- "_genreID"
- "_genreIdentifier"
- "_getBundleIdentifierForBundleAtURL:invokeUpdateBlockAndReregister:error:"
- "_getExtensionPointID:context:error:"
- "_getGroupContainersCreatingIfNecessary:checkNonContainerizedBundles:"
- "_getObject:atIndex:context:"
- "_getPersonaAttributesRetryingIfNecessary"
- "_getPreferredIconNameForIdentifier:"
- "_getPropertyList:"
- "_getRedactedPluginProxy:appexRecord:UUID:node:bundleIdentifier:platform:error:"
- "_getValue:forPropertyListKey:"
- "_groupContainers"
- "_hadBiDiControlCharacter"
- "_hadColonInFSName"
- "_hadForbiddenCharacter"
- "_hadNonASCIICharacter"
- "_handlerRank"
- "_hasAssociatedPersonas"
- "_hasBeenPresented"
- "_hasContext"
- "_hasFiredErrorHandler"
- "_hasOutstandingTokenForIdentity:"
- "_hasPersistentPreferences"
- "_hasPrepared"
- "_hasReachedEnd"
- "_hasReferringAliasNode"
- "_hasServer"
- "_hasTriedToPrepare"
- "_hfsCreator"
- "_hfsType"
- "_hmacSecret"
- "_iconFileNames"
- "_iconFileNamesWithContext:tableID:unitID:unitBytes:"
- "_iconFlags"
- "_iconsDict"
- "_iconsDictionary"
- "_identifier"
- "_identifiers"
- "_identifiersFileURL"
- "_identity"
- "_identityBookmark"
- "_identityString"
- "_identityUsageDescription"
- "_ifAttached:else:"
- "_ignoreAppLinkEnabledProperty"
- "_importedTypes"
- "_inEducationMode"
- "_inSyncBubble"
- "_inXCTestRigInsecure"
- "_inactiveInstalls"
- "_includeLinksForCallingApplication"
- "_index"
- "_infoDictionary"
- "_infoPlist"
- "_init"
- "_initInvalid"
- "_initProtected"
- "_initWithApplicationRecord:parentApplicationIdentifiers:appClipPlist:"
- "_initWithBindingEvaluator:error:"
- "_initWithBundleIdentifier:alreadyKnownUsage:validationToken:"
- "_initWithBundleIdentifier:placeholder:error:"
- "_initWithBundleIdentifier:withContext:"
- "_initWithBundleUnit:context:bundleIdentifier:"
- "_initWithBundleUnit:context:bundleType:bundleID:localizedName:bundleContainerURL:dataContainerURL:resourcesDirectoryURL:iconsDictionary:iconFileNames:version:"
- "_initWithClaimRecord:typeRecord:bundleRecord:provenance:"
- "_initWithContext:"
- "_initWithContext:binding:coreTypesBundleRecord:typeRecord:error:"
- "_initWithContext:bundleData:"
- "_initWithContext:bundleID:bundleData:error:"
- "_initWithContext:bundleUnit:applicationRecord:bundleID:resolveAndDetach:"
- "_initWithContext:dynamicUTI:"
- "_initWithContext:identifier:"
- "_initWithContext:persistentIdentifier:"
- "_initWithContext:persistentIdentifierData:length:"
- "_initWithContext:pluginID:pluginData:error:"
- "_initWithContext:pluginID:pluginData:extensionPointRecord:error:"
- "_initWithContext:tableID:unitID:"
- "_initWithContext:unitID:"
- "_initWithIdentifier:inMap:"
- "_initWithIdentifier:unlocalizedTitle:symbolImageName:"
- "_initWithKeys:forDictionary:"
- "_initWithLocalizedName:"
- "_initWithNode:bundleIdentifier:context:tableID:unitID:bundleBaseData:error:"
- "_initWithNode:bundleIdentifier:placeholderBehavior:systemPlaceholder:itemID:forceInBundleContainer:context:error:"
- "_initWithPlugin:andContext:applicationExtensionRecord:resolveAndDetach:"
- "_initWithQueryDictionary:applyFilter:"
- "_initWithRecord:"
- "_initWithRecord:resolveAndDetach:"
- "_initWithURL:"
- "_initWithUUID:bundleIdentifier:pluginIdentifier:effectiveIdentifier:version:bundleURL:"
- "_initWithUUID:node:bundleIdentifier:context:requireValid:error:"
- "_initWithUUID:node:bundleIdentifier:platform:context:requireValid:allowRedacted:error:"
- "_inode"
- "_installControlsQueue"
- "_installFailureReason"
- "_installIndexes"
- "_installType"
- "_installTypes"
- "_intentDefinitionURLs"
- "_intentionallyInvalid"
- "_intentsArrayForKey:"
- "_internalQueue"
- "_internalQueue_initializeDatabase"
- "_internalQueue_insertIdentifier:userElection:"
- "_internalQueue_insertIdentifier:userElection:timestamp:"
- "_internalQueue_loadDatabase"
- "_internalQueue_loadPluginKitDatabase"
- "_internalQueue_purgeDatabase"
- "_internalQueue_resetUserElection"
- "_internalQueue_selectUserElectionForIdentifier:"
- "_ioPersonality"
- "_ioQueue"
- "_isApp:defaultForCategory:"
- "_isApplication"
- "_isContentManaged"
- "_isDirectory"
- "_isFolder"
- "_isInitialized"
- "_isLightweightSystemServer"
- "_isOneTapOpenable"
- "_isPlaceholder"
- "_isServer"
- "_isShared"
- "_isVocabularyType"
- "_itemFlags"
- "_itemID"
- "_itemName"
- "_ivarLock"
- "_ivarQueue"
- "_journalledNotificationsToReplay"
- "_keys"
- "_keysAreCompacted"
- "_knownSystemAppDeletionState"
- "_lastFastObject"
- "_lastFiredDate"
- "_lastObservedError"
- "_latency"
- "_launchOptions"
- "_legacy"
- "_libraryItems"
- "_libraryPath"
- "_limit"
- "_linkedParentApplicationBundleID"
- "_linkedParentApplicationBundleIDWithContext:tableID:unitID:unitBytes:"
- "_linkedParentBundleID"
- "_listener"
- "_loadRealRecord"
- "_localResolver"
- "_localizedContextualIdentityUsageDescriptions"
- "_localizedDescription"
- "_localizedDescriptionWithContext:tableID:unitID:unitBytes:"
- "_localizedIdentityUsageDescription"
- "_localizedMicrophoneUsageDescription"
- "_localizedName"
- "_localizedNameWithContext:tableID:unitID:unitBytes:"
- "_localizedNameWithPreferredLocalizations:useShortNameOnly:"
- "_localizedNames"
- "_localizedNamesWithContext"
- "_localizedNamesWithContextWithContext:tableID:unitID:unitBytes:"
- "_localizedShort:nameWithContext:tableID:unitID:bundleData:"
- "_localizedShortName"
- "_localizedShortNameWithContext:tableID:unitID:unitBytes:"
- "_localizedShortNames"
- "_localizedStrings"
- "_lock"
- "_locked_stagingDirectoryForKey:"
- "_locked_updatePersonaStagingDirectories"
- "_loctable"
- "_lsPing:reply:"
- "_ls_normalizedPluginPlist"
- "_machOUUIDs"
- "_mainStagingDirectoryKey"
- "_maintenanceQueue"
- "_managedPersonas"
- "_managementDeclarationIdentifier"
- "_manager"
- "_maxSystemVersion"
- "_maximumNumericHandlerRank"
- "_maximumRating"
- "_mergeLock"
- "_mergedPlist"
- "_miDict"
- "_microphoneUsageDescription"
- "_migratedIdentities"
- "_migratorRunning"
- "_mimic"
- "_minInterval"
- "_minSystemVersion"
- "_minSystemVersionPlatform"
- "_minimumNumericHandlerRank"
- "_missingBundleLocs"
- "_missingBundleLocsWithContext:tableID:unitID:unitBytes:"
- "_mobileInstallIDs"
- "_modifiedPlugins"
- "_moreFlags"
- "_mutex"
- "_name"
- "_newRatingRank"
- "_node"
- "_nonce"
- "_numApplications"
- "_numPlugins"
- "_observedInstallProgresses"
- "_observerQueue"
- "_observerSet"
- "_observers"
- "_observersQueue"
- "_observing"
- "_observinglsd"
- "_oldRatingRank"
- "_onSystemPartition"
- "_onlyCryptexContent"
- "_openAppLink:state:completionHandler:"
- "_openConfiguration"
- "_openUserActivity:orUserActivityUUID:activityTypeForUUID:withApplicationProxy:options:completionHandler:"
- "_openWithAppLink:state:completionHandler:"
- "_operation"
- "_orderedInstalls"
- "_originalIdentifier"
- "_originalName"
- "_originalURL"
- "_overriddenPlugins"
- "_overrideURL"
- "_owner"
- "_parentApplicationIdentifiers"
- "_parentApplicationRecord"
- "_parentBundleID"
- "_pasteSharingToken"
- "_payload"
- "_perThreadContexts"
- "_perThreadContextsLock"
- "_perThreadContextsLock_createPerThreadContextForThisThread"
- "_perThreadContextsLock_destroyPerThreadContextForThisThread"
- "_perThreadContextsLock_findPerThreadContextForThisThread"
- "_perThreadContextsLock_findPerThreadContextForThisThreadIfExists"
- "_perUserEntropy"
- "_performBlockWithContext:"
- "_persistentIdentifierWithContext:tableID:unitID:unitBytes:"
- "_personaGeneration"
- "_personaType"
- "_personaUniqueString"
- "_personas"
- "_personasWithAttributes"
- "_personasWithAttributesWithContext:tableID:unitID:unitBytes:"
- "_pi"
- "_placeholder"
- "_placeholderFetchBehavior"
- "_placeholderIconUpdatedForApp:"
- "_placeholderInstalled"
- "_placeholdersUninstalled:"
- "_platform"
- "_plist"
- "_plistContentFlags"
- "_plistFlags"
- "_plistHint"
- "_plistRarities"
- "_plists"
- "_plugInKitPlugins"
- "_pluginFlags"
- "_pluginIdentifier"
- "_pluginMIDicts"
- "_pluginPlists"
- "_pluginUUID"
- "_pluginUnits"
- "_plugins"
- "_pluginsByBundleIentifier"
- "_precondition"
- "_predicate"
- "_preferredLaunchArchitecture"
- "_preferredLaunchArchitectureWithContext:tableID:unitID:unitBytes:"
- "_preferredMarketplaces"
- "_preflightPathOfBundleWithContext:bundleUnit:bundleData:"
- "_prepareApplicationProxiesForNotification:identifiers:withPlugins:"
- "_prepareProxyForNotificationByBundleUnit:context:"
- "_prepareWithContext:error:"
- "_prerendered"
- "_previousInstallType"
- "_primaryIconName"
- "_privateDocumentFileNamesAsCacheKey"
- "_profileValidationState"
- "_profileValidationStateWithContext:tableID:unitID:unitBytes:"
- "_progressProportions"
- "_progressProportionsLock"
- "_progressProportionsSaveTimerSource"
- "_progressSubscriptionsQueue"
- "_progresses"
- "_propertyClasses"
- "_propertyClassesForCoding"
- "_propertyList"
- "_protocol"
- "_provenance"
- "_provider"
- "_proxies"
- "_proxy"
- "_pruneObsoleteTrustedSignerIdentities"
- "_publish"
- "_publishingStrings"
- "_purchasedRedownload"
- "_purchaserDSID"
- "_queriableSchemes"
- "_queryDict"
- "_queryDictionary"
- "_queue"
- "_ratingLabel"
- "_ratingRank"
- "_ratingRankEligibilityDomain"
- "_ratingRankExceptionBundleIDs"
- "_rawBundleFlags"
- "_rawBundleFlagsWithContext:tableID:unitID:unitBytes:"
- "_rawEnvironmentVariables"
- "_rawEnvironmentVariablesWithContext:tableID:unitID:unitBytes:"
- "_rawFlags"
- "_rawFlagsWithContext:tableID:unitID:unitBytes:"
- "_rawGroupContainerURLs"
- "_rawGroupContainerURLsCheckingRedaction"
- "_rawGroupContainerURLsWithContext:tableID:unitID:unitBytes:"
- "_rawIconDictionary"
- "_rawIconDictionaryWithContext:tableID:unitID:unitBytes:"
- "_rawIconFlags"
- "_rawIconFlagsWithContext:tableID:unitID:unitBytes:"
- "_rawMoreFlags"
- "_rawMoreFlagsWithContext:tableID:unitID:unitBytes:"
- "_rawPlistData"
- "_rawPlistFlags"
- "_rawPlistFlagsWithContext:tableID:unitID:unitBytes:"
- "_readAccessContext"
- "_realRecord"
- "_rebuildError"
- "_rebuildReasonFlags"
- "_record"
- "_recordEnumerator"
- "_redacted"
- "_referenceAccessoryPath"
- "_referenceAccessoryPathWithContext:tableID:unitID:unitBytes:"
- "_referenceAccessoryURLNoConformances"
- "_referenceDate"
- "_referrerURL"
- "_refreshAfter"
- "_refreshDate"
- "_registerChildItemsTrusted"
- "_registrationDate"
- "_registrationInfo"
- "_relativePathsThatExist"
- "_remoteObserver"
- "_remoteResolutionIsExpensive"
- "_removeExtantToken:"
- "_removeResolvedPropertyValueForGetter:"
- "_removeSubscriber:"
- "_replacementObjectForResolvedPropertyValue:forGetter:encoder:"
- "_replayingJournalToNewClients"
- "_replyWithError:onQueue:block:"
- "_requiredRelationship"
- "_requiresDatabaseMappingEntitlement"
- "_resolveAllProperties"
- "_resolveQueries:XPCConnection:error:"
- "_resolvedDomainUID"
- "_resolvedNodeFromAliasFile:flags:error:"
- "_resolvedProperties"
- "_resolvedPropertyValueForGetter:"
- "_resolvedPropertyValueForGetter:nullPlaceholder:"
- "_resolvedURLFromAliasFile:flags:error:"
- "_resolver"
- "_resolvingMethods"
- "_resourceValues"
- "_resourcesDirectoryURL"
- "_restrictedBundleIDs"
- "_restrictedBundles"
- "_restrictionsAccessLock"
- "_result"
- "_retries"
- "_running"
- "_sandboxEnvironmentVariables"
- "_saveError"
- "_saveFlag"
- "_schema"
- "_schemeIfNotFileURL"
- "_sdkPlist"
- "_sdkVersion"
- "_sdkVersionNumber"
- "_secondCategoryType"
- "_sensitive"
- "_sensitiveDataProxy"
- "_sequenceNumber"
- "_serializedPlaceholderPath"
- "_serverQueue"
- "_server_newsWidgetIsRestricted"
- "_serviceDetails"
- "_setAlternateIconName:forIdentifier:withIconsDictionary:error:"
- "_setBoundIconInfo:"
- "_setCompatibilityState:"
- "_setEntitlements:"
- "_setEnvironmentVariables:"
- "_setFileNameLocalizationEnabled:"
- "_setIconsDictionary:"
- "_setInfoDictionary:"
- "_setLocalizedName:"
- "_setPreferredIconName:forIdentifier:"
- "_setQueue:"
- "_setResolvedPropertyValue:forGetter:"
- "_setSWCSetting:forKey:error:"
- "_setSWCSetting:forKey:withApplicationIdentifier:error:"
- "_setShared:"
- "_shared"
- "_sharedCaches"
- "_shortDisplayName"
- "_shortVersionString"
- "_shouldBeDeletedOnOpen"
- "_shouldSetHandlerOnDocumentOpen"
- "_shouldURLPropertyProviderEncodeTypeRecord"
- "_signatureVersion"
- "_signerIdentity"
- "_signerIdentitySyncQueue"
- "_signerIdentitySyncSource"
- "_signerOrganization"
- "_slices"
- "_sourceApp"
- "_sourceAppBundleID"
- "_sourceAuditToken"
- "_specifierType"
- "_stagingDirectoryForKeyRefreshingIfNecessary:"
- "_stagingDirectoryInfoMap"
- "_startupJournalledNotifications"
- "_stashedAppInfo"
- "_state"
- "_stateFlags"
- "_staticDiskUsage"
- "_statsGatherer"
- "_store"
- "_storeCohort"
- "_storeFront"
- "_storeItemIdentifier"
- "_storefront"
- "_strategy"
- "_stringLocalizerForTable:"
- "_stringsContent"
- "_stringsFile"
- "_stringsFileContent"
- "_subgenres"
- "_subscriptions"
- "_subtype"
- "_supportedComplicationFamilies"
- "_supportedGameControllers"
- "_symbolImageName"
- "_synthesizedExtensionPointWithIdentifier:"
- "_systemContainerURL"
- "_systemContentSaveTime"
- "_systemContentScanTime"
- "_systemGroupContainerURL"
- "_systemMode"
- "_systemModeMutex"
- "_tableID"
- "_targetApplicationProxy"
- "_targetApplicationRecord"
- "_targetConnectionEndpoint"
- "_targetServiceConnectionEndpoint"
- "_targetUserID"
- "_teamID"
- "_teamIdentifier"
- "_tearDownCallbacks"
- "_timer"
- "_totalRebuildTime"
- "_type"
- "_typeForURLPropertyProviderWithTypeRecord:"
- "_typeIDs"
- "_typeIdentifier"
- "_typeIdentifier:conformsToTypeIdentifier:"
- "_typeOfCurrentDevice"
- "_typeRecord"
- "_typeRecordWithContext:forPromiseAtNode:error:"
- "_typeRecordWithContext:forPromiseResourceValues:error:"
- "_typeRecordWithContext:identifier:allowUndeclared:"
- "_typeRecordWithIdentifier:allowUndeclared:"
- "_typeWithDeviceModelCode:"
- "_typeWithDeviceModelCode:enclosureColor:"
- "_uncachedCalloutLock"
- "_uniqueIdentifier"
- "_unitID"
- "_unitIDs"
- "_units"
- "_unlocalizedInfoPlistStrings"
- "_unlocalizedNamesWithContext"
- "_unlocalizedTitle"
- "_unpublish"
- "_url"
- "_usage"
- "_useOneTapOpenBehavior"
- "_userActivityWithState:error:"
- "_userContainerURL"
- "_userInitiatedUninstall"
- "_userManagementGenerationNumber"
- "_userRequested"
- "_usesSystemPersona"
- "_usingEphemeralStorage"
- "_usingNetwork"
- "_uuid"
- "_validationState"
- "_validationToken"
- "_valueForEqualityTesting"
- "_values"
- "_variantID"
- "_vendorIdentifierSeed"
- "_vendorName"
- "_version"
- "_versionID"
- "_versionIdentifier"
- "_volumeContainerAdapter"
- "_waiters"
- "_wantsHiddenExtension"
- "_watchKitVersion"
- "_weakClaimingBundleRecord"
- "_weakContainingBundleRecord"
- "_weakDeclaringBundleRecord"
- "_webNotificationPlaceholder"
- "_windowOpenDates"
- "_writeAccessContext"
- "_writeJournalUnconditionally"
- "_xpcConnection"
- "_yieldClaimBindings"
- "abortIfMayNotMapDatabase"
- "absoluteString"
- "absoluteURL"
- "accentColorName"
- "accessContext"
- "accessCurrentUserSessionUsingBlock:"
- "accessSystemScopeUsingBlock:"
- "accessUsingBlock:"
- "accessWithOptions:usingBlock:"
- "accessWithUserID:options:usingBlock:"
- "accessWithUserID:usingBlock:"
- "accessing"
- "acquireDatabase"
- "activateBindings:unitID:bundleData:"
- "activeManagedConfigurationRestrictionUUIDs"
- "activityType"
- "actuallyOverridesDMFObserverMethod"
- "adHocCodeSigned"
- "addApplication:"
- "addAttribute:value:range:"
- "addBarrierBlock:"
- "addBundleFlag:"
- "addChangeObserver:"
- "addCharactersInRange:"
- "addContextualUsageDescriptionValuesToLocalizedKeys:fromInfoDictionary:"
- "addDatabaseChangeObserver4WebKit:"
- "addEntriesFromDictionary:"
- "addExecutionBlock:"
- "addIconFlag:"
- "addItemInfoFlag:"
- "addLocalObserver:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver"
- "addObserver:"
- "addObserver:forKeyPath:options:context:"
- "addObserver:selector:name:object:"
- "addObserverForName:object:queue:usingBlock:"
- "addOperationWithBlock:"
- "addOverrideBlock:"
- "addPlistFlag:"
- "addPointer:"
- "addSendNotificationFenceWithTimeout:fenceBlock:"
- "addSubscriber:forPublishingKey:andBundleID:"
- "addTimer:forMode:"
- "additionalEnvironmentVariables"
- "afterAppLinksBecomeAvailableForURL:limit:performBlock:"
- "aliasFile"
- "allApplications"
- "allIdentifiersNotDispatched"
- "allInstalledApplications"
- "allKeys"
- "allObjects"
- "allStringValues"
- "allValues"
- "allocWithZone:"
- "allowNoneHandlerRank"
- "allowWildcardClaims"
- "allowedOpenInAppBundleIDsAfterApplyingFilterToAppBundleIDs:originatingAppBundleID:originatingAccountIsManaged:"
- "allowlistedBundleIDs"
- "allowsAlternateIcons"
- "alphanumericCharacterSet"
- "alternateIconName"
- "alternateIconNameForIdentifier:error:"
- "alternatePrimaryIconName"
- "alwaysAllowedBundleIdentifiers"
- "alwaysAvailable"
- "alwaysUseDebugOpenWithMenus"
- "anonymousListener"
- "appClipMetadata"
- "appClipMetadataWithContext:tableID:unitID:unitBytes:"
- "appIDPrefix"
- "appLinksWithContext:error:"
- "appLinksWithContext:forSWCResults:"
- "appLinksWithURL:limit:error:"
- "appLinksWithURL:limit:includeLinksForCurrentApplication:error:"
- "appMarketplacesPreferencesStateURL"
- "appObserverSelector"
- "appProtectionEffectiveContainerWithContext:tableID:unitID:unitBytes:"
- "appProtectionHidden"
- "appProtectionHiddenWithContext:tableID:unitID:unitBytes:"
- "appProtectionLocked"
- "appProtectionLockedWithContext:tableID:unitID:unitBytes:"
- "appProtectionStoreFileURL"
- "appState"
- "appStoreReceiptName"
- "appStoreReceiptURL"
- "appStoreToolsBuildVersion"
- "appStoreToolsBuildVersionWithContext:tableID:unitID:unitBytes:"
- "appStoreVendable"
- "appTags"
- "appTagsWithContext:tableID:unitID:unitBytes:"
- "appType"
- "appUpdate"
- "appWhitelistState"
- "appendBytes:length:"
- "appendCharacters:length:"
- "appendData:"
- "appendFormat:"
- "appendString:"
- "appexRecordsForUnitIDsWithContext:unitIDs:"
- "appleInternal"
- "applicableForCurrentDatabase"
- "applicationDownloaderDSID"
- "applicationExtensionRecords"
- "applicationExtensionRecordsForUUIDs:outContainingBundleRecords:error:"
- "applicationExtensionRecordsWithContext:tableID:unitID:unitBytes:"
- "applicationFamilyID"
- "applicationForOpeningResource:"
- "applicationForUserActivityDomainName:"
- "applicationForUserActivityType:"
- "applicationHasMIDBasedSINF"
- "applicationIconDidChange:"
- "applicationIdentifierPrefix"
- "applicationInstallsArePrioritized:arePaused:"
- "applicationInstallsDidCancel:"
- "applicationInstallsDidChange:"
- "applicationInstallsDidPause:"
- "applicationInstallsDidPrioritize:"
- "applicationInstallsDidResume:"
- "applicationInstallsDidStart:"
- "applicationInstallsDidUpdateIcon:"
- "applicationIsInstalled:"
- "applicationManagementDomain"
- "applicationMissingRequiredSINF"
- "applicationProxiesWithPlistFlags:bundleFlags:"
- "applicationProxyForBundleType:identifier:isCompanion:URL:itemID:bundleUnit:"
- "applicationProxyForBundleURL:"
- "applicationProxyForCompanionIdentifier:"
- "applicationProxyForIdentifier:"
- "applicationProxyForIdentifier:placeholder:"
- "applicationProxyForIdentifier:withContext:"
- "applicationProxyForItemID:"
- "applicationProxyForSystemPlaceholder:"
- "applicationProxyWithBundleUnitID:withContext:"
- "applicationRecordsForUserActivityDomainName:limit:error:"
- "applicationRecordsForUserActivityType:limit:error:"
- "applicationState"
- "applicationStateDidChange:"
- "applicationStateWithContext:tableID:unitID:unitBytes:"
- "applicationType"
- "applicationVariant"
- "applications"
- "applicationsAvailableForHandlingURLScheme:"
- "applicationsAvailableForOpeningByDraggingAndDroppingWithError:"
- "applicationsAvailableForOpeningDocument:"
- "applicationsAvailableForOpeningFromAirDropWithError:"
- "applicationsAvailableForOpeningURL:"
- "applicationsAvailableForOpeningURL:legacySPI:"
- "applicationsAvailableForOpeningWithError:"
- "applicationsAvailableForOpeningWithHandlerRanks:error:"
- "applicationsAvailableForOpeningWithStyle:limit:XPCConnection:error:"
- "applicationsDidChangePersonas:"
- "applicationsDidFailToInstall:"
- "applicationsDidFailToUninstall:"
- "applicationsDidInstall:"
- "applicationsDidUninstall:"
- "applicationsDidUpdateMetadata:"
- "applicationsForUserActivityType:"
- "applicationsForUserActivityType:limit:"
- "applicationsOfType:"
- "applicationsOrClaimBindings:availableForOpeningWithStyle:handlerRank:limit:XPCConnection:error:"
- "applicationsWillInstall:"
- "applicationsWillUninstall:"
- "applicationsWithAudioComponents"
- "applicationsWithUIBackgroundModes"
- "applicationsWithVPNPlugins"
- "applyPerUserEntropyNotDispatched:type:"
- "applyRestrictionDictionary:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:"
- "appsRatingExemptedBundleIDs"
- "arcadeApp"
- "archivedDataWithRootObject:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "areEnabledByDefault"
- "armSaveTimerIfNecessary:"
- "array"
- "arrayByAddingObject:"
- "arrayByAddingObjectsFromArray:"
- "arrayByFilteringLaunchProhibitedAppsFrom:"
- "arrayForKey:"
- "arrayForKey:withValuesOfClass:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "askedForMissingResourceKey:"
- "askedForMissingSelector:"
- "assertNotActiveForThisThread"
- "associatedPersonas"
- "attributedString"
- "attributedSubstringFromRange:"
- "audioComponents"
- "audioComponentsWithContext:tableID:unitID:unitBytes:"
- "auditTokenHasReadAccess:"
- "auditTokenHasWriteAccess:"
- "autorelease"
- "availableClaimBindingsForMode:error:"
- "availableClaimBindingsForMode:handlerRank:error:"
- "availableClaimBindingsReturningError:"
- "awakeAfterUsingCoder:"
- "b1"
- "b14"
- "b16"
- "b2"
- "backgroundTaskSchedulerPermittedIdentifiers"
- "backgroundTaskSchedulerPermittedIdentifiersWithContext:tableID:unitID:unitBytes:"
- "backtraceString"
- "bad registration input"
- "baseBindingEvaluatorWithBindingStyle:auditToken:"
- "basePropertyClasses"
- "baseURL"
- "beginBitfieldFlags:"
- "beginContentAccess"
- "beginFlags:flags:"
- "beginListening"
- "beginModificationOperation"
- "beginProvidingVisualizationArchivesWithMachServiceName:queue:creatingVisualizersWithBlock:"
- "bestMigratedIdentityForIdentity:"
- "beta"
- "betaApp"
- "bgPermittedIdentifiers"
- "bindableWithDocumentProxy:"
- "bindableWithTypeIdentifier:"
- "bindableWithURL:"
- "bindingConfigurationForDocument:style:handlerRank:"
- "bindingEvaluatorForAuditToken:"
- "bindingEvaluatorForIconInfo"
- "bindingEvaluatorForScheme:"
- "bindingWithContext:forServiceDetails:callingBundleIdentifier:"
- "block"
- "blockOperationWithBlock:"
- "blocked"
- "bluetooth product ID (?)URL scheme"
- "bookmarkDataRelativeToNode:error:"
- "bookmarkDataWithOptions:relativeToNode:error:"
- "booksStoreAuthorizationURL:"
- "boolForKey:"
- "boolValue"
- "bootstrapBaseStagingDirectoryNode:error:"
- "boundIconIsBadge"
- "boundIconsDictionary"
- "browserSettings"
- "buildBundleData:error:"
- "builtWithThreadSanitizer"
- "bundle has no personas in database?"
- "bundle:reason:"
- "bundleContainerURLWithContext:tableID:unitID:unitBytes:"
- "bundleForClass:"
- "bundleIconsDictionary"
- "bundleIdentifierForIdentityString:error:"
- "bundleIdentifierWithContext:error:"
- "bundleIdentifierWithError:"
- "bundleIdentifiersForMachOUUIDs:error:"
- "bundleIdentityForIdentityString:"
- "bundleInfoDictionaryWithError:"
- "bundleInode"
- "bundleMetadataReturningError:"
- "bundleModTime"
- "bundleName"
- "bundlePath"
- "bundleProvider"
- "bundleProxyForCurrentProcess"
- "bundleProxyForIdentifier:"
- "bundleProxyForURL:"
- "bundleProxyForURL:error:"
- "bundleProxyWithAuditToken:error:"
- "bundleRecordForAuditToken:error:"
- "bundleRecordForCurrentProcess"
- "bundleRecordWithApplicationIdentifier:error:"
- "bundleRecordWithBundleIdentifier:allowPlaceholder:error:"
- "bundleType"
- "bundleUnitMeetsRequirements:bundleData:context:"
- "bundleVersionWithContext:tableID:unitID:unitBytes:"
- "bundleWithIdentifier:"
- "bundleWithPath:"
- "bundleWithURL:"
- "bundlesWithIdentifiers:ratingRankEligibilityChanged:monitor:"
- "busyDirectory"
- "bytes"
- "bytesUsedForApplicationWithBundleID:replyBlock:"
- "c16@0:8"
- "c40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
- "cStringUsingEncoding:"
- "cacheForPersona:"
- "cacheInterval"
- "cachedDataContainerURL"
- "calculateSetDifference:and:"
- "callCompletionHandlerWhenFullyComplete"
- "callSpringBoardWithCompletionHandler:"
- "callWithCompletionHandler:"
- "callbackQueue"
- "callbackType"
- "callingBundleIdentifier"
- "canAccess"
- "canAccessAdvertisingIdentifier"
- "canAccessURL:fromSandboxWithAuditToken:operation:"
- "canAccessURL:withAuditToken:operation:"
- "canChangeDefaultAppForCategory:"
- "canHandleURLComponents:"
- "canHandleWebAuthentication"
- "canInstantiateFromDatabase"
- "canIssueIO"
- "canOpenURL:publicSchemes:privateSchemes:XPCConnection:error:"
- "canOpenURL:publicSchemes:privateSchemes:completionHandler:"
- "canReadFromSandboxWithAuditToken:"
- "canReadMetadataFromSandboxWithAuditToken:"
- "canReadMetadataOfURL:fromSandboxWithAuditToken:"
- "canReadMetadataOfURL:withAuditToken:"
- "canReadMetadataWithAuditToken:"
- "canReadURL:fromSandboxWithAuditToken:"
- "canReadURL:withAuditToken:"
- "canReadWithAuditToken:"
- "canRegisterContainer"
- "canRegisterURL:withOptions:"
- "canSetExtensionHiddenWithContext:"
- "canUnregisterWithOptions:"
- "canWriteFromSandboxWithAuditToken:"
- "canWriteURL:fromSandboxWithAuditToken:"
- "canWriteURL:withAuditToken:"
- "canWriteWithAuditToken:"
- "canonical:pathWithError:"
- "canonicalExecutablePath"
- "canonicalPathWithError:"
- "capitalizedString"
- "carPlayInstrumentClusterURLSchemes"
- "carPlayInstrumentClusterURLSchemesWithContext:tableID:unitID:unitBytes:"
- "caseInsensitiveCompare:"
- "categoryType"
- "categoryTypesWithError:"
- "cfBundleRef"
- "cfBundleRef:reason:"
- "changeIconWithAlertForApplicationIdentity:withIconsDictionary:toAlternateIconName:completion:"
- "characterAtIndex:"
- "characterIsMember:"
- "checkNeedsUpdateForiTunesMetadata:SINFo:placeholderMetadata:"
- "checkResourceIsReachableAndReturnError:"
- "checkSelectors"
- "childNodeWithRelativePath:flags:error:"
- "childNodeWithRelativePathExists:"
- "childProgressForBundleID:andPhase:"
- "childTypeIdentifiers"
- "childUnit:table:unit:"
- "childUnit:unit:"
- "claimBindingsAvailableForOpeningWithStyle:handlerRank:limit:XPCConnection:error:"
- "claimBindingsWithConfiguration:error:"
- "claimBindingsWithTypeIdentifier:error:"
- "claimBindingsWithURL:error:"
- "claimRecords"
- "claimRecordsWithContext:tableID:unitID:unitBytes:"
- "claimedDocumentContentTypes"
- "claimedURLSchemes"
- "claimingBundleRecord"
- "classFallbacksForKeyedArchiver"
- "classForCoder"
- "classForKeyedArchiver"
- "classForKeyedUnarchiver"
- "classVersion"
- "classesWithNameForXCTests:"
- "cleanSecondaryExtension:"
- "cleanupDeletedApplication:"
- "clear"
- "clearAdvertisingIdentifier"
- "clearAllIdentifiersOfType:"
- "clearAllValues"
- "clearAlternateNameForBundleIdentifier:validationDictionary:"
- "clearBundleProxyForCurrentProcess"
- "clearCaches"
- "clearCreatedProgressForBundleID:"
- "clearIdentifiersForUninstallationWithContext:bundleUnit:bundleData:"
- "clearIdentifiersForUninstallationWithVendorName:bundleIdentifier:"
- "clearURLPropertyCacheIfStale"
- "clientBorn:forNewConnection:"
- "clientClass"
- "clientForConnection:"
- "clientHasMIEntitlement:"
- "clientIsEntitledForEmbeddedRegistrationOperations"
- "clientXPCConnection"
- "closeAndReturnError:"
- "coalesceProportionsSave"
- "coalescingFlag"
- "code"
- "codeInfoIdentifier"
- "codeSignatureVersion"
- "codeSignatureVersionWithContext:tableID:unitID:unitBytes:"
- "com.apple.backboardd.backlight.changed"
- "combineBaseName:extension:"
- "commitReturningError:"
- "commonClientOpenURL:options:configuration:synchronous:completionHandler:"
- "companionApplicationIdentifier"
- "companionBundleIdentifier"
- "companionBundleIdentifierWithContext:tableID:unitID:unitBytes:"
- "compare:"
- "compare:options:"
- "compare:options:range:"
- "compareBookmarkData:toBookmarkData:"
- "compatibilityObject"
- "compatibilityStateWithContext:tableID:unitID:unitBytes:"
- "complicationPrincipalClass"
- "complicationPrincipalClassName"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "concatenateBaseName:andExtension:"
- "concurrentInstallOperations"
- "configuration"
- "conformsToOverridePatternWithKey:"
- "conformsToProtocol:"
- "conformsToTypeIdentifier:"
- "conformsToTypeRecord:"
- "connection"
- "connection:handleInvocation:isReply:"
- "connectionType"
- "connectionWasInvalidated:"
- "containerOwnerApplicationIdentifier"
- "containerized"
- "containerizedBundleExistsForIdentifier:"
- "containingBundleIdentifiersForPlugInBundleIdentifiers:error:"
- "containingBundleRecord"
- "containsObject:"
- "containsString:"
- "contentsAtPath:"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "contextPointer"
- "controlCharacterSet"
- "copy"
- "copyCFBundleWithError:"
- "copyItemAtURL:toURL:error:"
- "copySchemesMap"
- "copyWithZone:"
- "coreType"
- "coreTypesBundleRecord"
- "coreTypesLocalizer"
- "correspondingApplicationExtensionRecord"
- "correspondingApplicationRecord"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countForObject:"
- "counterpartAppBundleIDs"
- "counterpartIdentifiers"
- "counterpartIdentifiersWithContext:tableID:unitID:unitBytes:"
- "createAndSeedLocalDatabase:"
- "createDeviceIdentifierWithVendorName:bundleIdentifier:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "createFromPlistRepresentation:"
- "createInstallJournalDirectoryIfRequired"
- "createInstallProgressForApplication:withPhase:andPublishingString:reply:"
- "createRepresentingProxy:"
- "createRepresentingRecord:"
- "createdInstallProgresses"
- "cs_rangesMatchingPredicate:"
- "cs_writeToFileHandle:"
- "currentBundleProxyQuery"
- "currentConnection"
- "currentHandler"
- "currentIdentityClass"
- "currentObserverCount"
- "currentPersistentIdentifier"
- "currentPersona"
- "currentPreferencesWithError:"
- "currentProcessHasReadAccess"
- "currentProcessHasWriteAccess"
- "currentProcessServicesDefaultShellEndpoint"
- "currentSchemaVersion"
- "currentThread"
- "d"
- "d16@0:8"
- "darwinNotificationNameForBaseName:optionalSessionKey:"
- "dataContainerURL"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "dataWithCapacity:"
- "dataWithContentsOfURL:"
- "dataWithContentsOfURL:options:error:"
- "dataWithContentsOfURL:options:maxLength:error:"
- "dataWithJSONObject:options:error:"
- "dataWithLength:"
- "dataWithPropertyList:format:options:error:"
- "database"
- "databaseContainerDirectoryURL"
- "databaseContainerURL"
- "databaseContainerURLWithUID:"
- "databaseContextWithError:"
- "databaseSaveInterval"
- "databaseSaveLatency"
- "databaseStoreFileMode"
- "databaseStoreFileURL"
- "databaseStoreFileURLWithUID:"
- "databaseUUID"
- "databaseUpdateNotificationNameForSessionKey:"
- "databaseWasRebuilt"
- "date"
- "dateByAddingTimeInterval:"
- "dateWithTimeIntervalSince1970:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "dbRecoveryFileURL"
- "dbRemoveDBOnStartupURL"
- "dbSentinelFileURL"
- "dbSyncInterruptedFileURL"
- "dealloc"
- "debugDescription"
- "declaration"
- "declarationWithContext:tableID:unitID:unitBytes:"
- "declared"
- "declaringBundleRecord"
- "decodeBoolForKey:"
- "decodeDoubleForKey:"
- "decodeInt32ForKey:"
- "decodeInt64ForKey:"
- "decodeIntForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decodePropertyListForKey:"
- "defaultAppQueryStateURL"
- "defaultApplicationForCategory:error:"
- "defaultCenter"
- "defaultContext"
- "defaultEvaluator"
- "defaultManager"
- "defaultResolver"
- "defaultServiceDomainIndirect"
- "defaultShareModeCollaboration"
- "defaultStringValue"
- "defaultWorkspace"
- "defaultsToPrivateAlwaysOnDisplayTreatment"
- "deletable"
- "deletableSystemApplication"
- "deleteCharactersInRange:"
- "description"
- "descriptionOfUnit:inTable:"
- "destURL"
- "detach"
- "detachAndSendNotification:forApplicationExtensionRecords:"
- "detachNewThreadWithBlock:"
- "developerType"
- "developerTypeWithContext:tableID:unitID:unitBytes:"
- "deviceConfiguredForHRN"
- "deviceFamilies"
- "deviceFamiliesWithContext:tableID:unitID:unitBytes:"
- "deviceFamily"
- "deviceIdentifierForAdvertising"
- "deviceIdentifierForVendor"
- "deviceIdentifierForVendorSeedData"
- "deviceIdentifierVendorSeed"
- "deviceManagementPolicy"
- "deviceManagementPolicyDidChange:"
- "deviceUnlockedSinceBoot"
- "dictionary"
- "dictionaryForKey:"
- "dictionaryForKey:valuesOfClass:"
- "dictionaryWithCapacity:"
- "dictionaryWithContentsOfURL:"
- "dictionaryWithContentsOfURL:error:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithValuesForKeys:"
- "didHandleInvocation:isReply:"
- "directionsApplications"
- "directionsModes"
- "directionsModesWithContext:tableID:unitID:unitBytes:"
- "directlySendNotification:withProxies:toObserver:"
- "directlySendNotification:withProxies:toObserverProxy:"
- "directoryClass"
- "discardContentIfPossible"
- "discardProportionsForBundleID:"
- "diskImageURLWithFlags:error:"
- "diskUsage"
- "diskUsageWithContext:tableID:unitID:unitBytes:"
- "dispatchJournalledNotificationsToConnectedClients"
- "dispatchJournalledNotificationsToObserver:"
- "dispatchQueue"
- "dispatchToObserver:forInstallProgressService:"
- "displayNameConstructorWithContext:bundle:bundleClass:node:preferredLocalizations:error:"
- "displayNameConstructorWithContext:node:error:"
- "displayNameConstructorWithContextIfNeeded:bundle:bundleClass:node:preferredLocalizations:error:"
- "displayNameConstructorWithContextIfNeeded:node:error:"
- "displayNameConstructorsWithContext:bundle:bundleClass:node:error:"
- "displayNameConstructorsWithContext:node:error:"
- "displayNameConstructorsWithContextIfNeeded:bundle:bundleClass:node:error:"
- "displayNameConstructorsWithContextIfNeeded:node:error:"
- "displayOrderEnumeratorForViableDefaultAppsForCategory:options:"
- "distributorID"
- "doTokenizedRegistrationTaskWithName:xpcReply:work:"
- "documentClaims"
- "documentProxyForName:type:MIMEType:"
- "documentProxyForName:type:MIMEType:isContentManaged:sourceAuditToken:"
- "documentProxyForName:type:MIMEType:managedSourceAuditToken:"
- "documentProxyForName:type:MIMEType:sourceIsManaged:"
- "documentProxyForURL:"
- "documentProxyForURL:isContentManaged:sourceAuditToken:"
- "documentProxyForURL:managedSourceAuditToken:"
- "documentProxyForURL:sourceIsManaged:"
- "doesNotRecognizeSelector:"
- "domain"
- "don't know how to register %@ yet"
- "doubleValue"
- "downgradeApplicationToPlaceholder:withOptions:error:"
- "downgraded"
- "driverExtensionPaths"
- "driverExtensionPathsWithContext:tableID:unitID:unitBytes:"
- "dynamicDiskUsage"
- "dynamicUsage"
- "effectiveBoolValueForSetting:"
- "effectiveBundleIdentifierWithContext:tableID:unitID:unitBytes:"
- "effectiveSettings"
- "effectiveValueForSetting:"
- "effectiveWhitelistedAppBundleIDs"
- "elements"
- "eligibilityDeletionDomain"
- "eligibilityForDomain:error:"
- "eligibleForRedaction"
- "eligibleMailClient"
- "eligibleWebBrowser"
- "emptyPrecondition"
- "enabled"
- "enabledByDefault"
- "encodeBool:forKey:"
- "encodeDouble:forKey:"
- "encodeInt32:forKey:"
- "encodeInt64:forKey:"
- "encodeInt:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endContentAccess"
- "endFlags"
- "endModificationOperation"
- "endpointForServiceIdentifier:reply:"
- "entitlementValueForKey:ofClass:"
- "entitlementValueForKey:ofClass:valuesOfClass:"
- "entitlementValuesForKeys:"
- "entitlementsWithContext:tableID:unitID:unitBytes:"
- "entityExists"
- "entryForApplication:category:"
- "enumerateApplicationsOfType:block:"
- "enumerateApplicationsOfType:legacySPI:block:"
- "enumerateBindingsWithContext:forSWCResults:block:"
- "enumerateBuiltInSystemContentWithBlock:error:"
- "enumerateBundlesOfType:block:"
- "enumerateBundlesOfType:legacySPI:block:"
- "enumerateBundlesOfType:usingBlock:"
- "enumerateChildTypesWithBlock:"
- "enumerateCryptexContentWithBlock:error:"
- "enumerateDescendantsWithBlock:"
- "enumerateExtensionPointRecords:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateKeysAndObjectsWithOptions:usingBlock:"
- "enumerateLocalizedStringsForKeys:usingBlock:"
- "enumerateLocalizedStringsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "enumerateParentTypesWithBlock:"
- "enumeratePedigreeWithBlock:"
- "enumeratePluginsMatchingQuery:withBlock:"
- "enumerateResolvedResultsOfQuery:withBlock:"
- "enumerateSystemEXExtensionPoints:"
- "enumerateValuesForTitlesInDescription:block:"
- "enumerator"
- "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
- "enumeratorForApplicationProxiesWithOptions:"
- "enumeratorForApplicationsOnSameVolumeWithinDirectoryAtURL:enumerationOptions:filteringOptions:"
- "enumeratorForExtensionPointIdentifier:"
- "enumeratorForPlugInKitProxiesWithExtensionPoint:options:"
- "enumeratorForPlugInKitProxiesWithExtensionPoint:options:filter:"
- "enumeratorForViableDefaultAppsForCategory:options:"
- "enumeratorOnVolumeAtURL:options:"
- "enumeratorWithExtensionPointRecord:options:"
- "enumeratorWithOptions:"
- "enumeratorWithParentApplicationRecord:"
- "environment"
- "environmentVariables"
- "equivalentBundleIDs"
- "equivalentBundleIdentifiers"
- "equivalentBundleIdentifiersWithContext:tableID:unitID:unitBytes:"
- "errorHandler"
- "errorWithDomain:code:userInfo:"
- "establishConnection"
- "evaluateBundle:bundleData:database:error:"
- "evaluatePredicate:"
- "evaluatePredicate:error:"
- "evaluateWithDomainEligibilityResolver:error:"
- "evaluateWithFeatureFlagResolver:"
- "evaluateWithObject:"
- "exactBundleVersionWithContext:tableID:unitID:unitBytes:"
- "exceptionWithName:reason:userInfo:"
- "execPath"
- "execSDKVersion"
- "execSDKVersionWithContext:tableID:unitID:unitBytes:"
- "executableInode"
- "executableModDate"
- "executableModeFile"
- "executableURL"
- "executableURLWithContext:tableID:unitID:unitBytes:"
- "exported:typesWithContext:tableID:unitID:unitBytes:"
- "exportedTypeRecords"
- "exportedTypeRecordsWithContext:tableID:unitID:unitBytes:"
- "exportedTypes"
- "extendedAttributeWithName:options:error:"
- "extensionPoint"
- "extensionPointDefinitionEnumerator"
- "extensionPointForIdentifier:"
- "extensionPointForIdentifier:platform:"
- "extensionPointRecord"
- "extensionPointRecordForCurrentProcess"
- "extensionPointRecordForIdentifier:platform:error:"
- "extensionPointRecordWithContext:tableID:unitID:unitBytes:"
- "extensionPointRecords"
- "extensionPointRecordsWithContext:tableID:unitID:unitBytes:"
- "extensionPointType"
- "extensionPointTypeWithContext:tableID:unitID:unitBytes:"
- "extensionSDK"
- "extensionWithError:"
- "externalAccessoryProtocols"
- "externalAccessoryProtocolsWithContext:tableID:unitID:unitBytes:"
- "externalVersionIdentifier"
- "extractUUIDForKey:"
- "failWithError:"
- "failedToOpenApplication:withURL:completionHandler:"
- "featureFlagPredicateForBundle:bundleData:database:error:"
- "fetchClientSideWithError:"
- "fetchServerSideWithConnection:error:"
- "fileDescriptor"
- "fileExistsAtPath:"
- "fileExistsAtPath:isDirectory:"
- "filePathURL"
- "fileSharingEnabled"
- "fileSystemRepresentation"
- "fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "filter"
- "filteredArrayUsingPredicate:"
- "finalInstallPhaseForAppProxy:"
- "findAppBundleForExecutableURL:withContext:"
- "findApplicationBundleAtNode:error:"
- "findApplicationBundleID:bundleData:context:forXPCConnection:"
- "findApplicationRecordFetchingPlaceholder:error:"
- "findApplicationRecordWithError:"
- "findContainerizedRecordForBundleUnit:error:"
- "findKeysToLocalizeInInfoDictionary:forArrayKey:stringKeys:localizedKeys:"
- "findPluginAtNode:error:"
- "finishWriting"
- "firstObject"
- "flag:name:"
- "flag:name:color:"
- "flushModificationState"
- "fmfURL"
- "fmfURL:"
- "fmipURL"
- "fmipURL:"
- "forceDatabaseSaveForTestingWithError:"
- "forceSaveForTestingWithCompletion:"
- "formUnionWithCharacterSet:"
- "forwardInvocation:"
- "forwardingTargetForSelector:"
- "foundBackingBundle"
- "fragment"
- "freeProfileValidated"
- "fulfillReturningError:"
- "fullBundleExistsForIdentifier:matchingNode:"
- "garbageCollectDatabaseWithCompletionHandler:"
- "garbageCollectDatabaseWithError:"
- "gatherLocalizedStringsForCFBundle:infoDictionary:domains:delegatesMightBeMainBundle:legacyLocalizationList:"
- "gatherLocalizedStringsForCFBundle:infoDictionary:domains:legacyLocalizationList:"
- "gatherLocalizedStringsForLSBundleProvider:infoDictionary:domains:delegatesMightBeMainBundle:legacyLocalizationList:"
- "generateIdentifiersForInstallationWithContext:bundleUnit:bundleData:"
- "generateIdentifiersWithVendorName:bundleIdentifier:"
- "generatePerUserEntropyIfNeededNotDispatched"
- "generateSomePerUserEntropyNotDispatched"
- "getAllUserActivityTypesAndDomainNamesWithCompletionHandler:"
- "getAlternateIconNameForIdentifier:reply:"
- "getAppLinkWithURL:completionHandler:"
- "getAppLinksWithURL:completionHandler:"
- "getApplicationCategoryIdentifiersSetWithCompletionHandler:"
- "getApplicationExtensionDiagnosticDescriptionWithError:"
- "getBoundIconInfoForDocumentProxy:completionHandler:"
- "getBundleIDToPersonasWithAttributesMap"
- "getBundleMetadata"
- "getBundleProxyForCurrentProcessWithCompletionHandler:"
- "getBundleRecordForCoreTypesWithCompletionHandler:"
- "getBundleRecordForCurrentProcessWithCompletionHandler:"
- "getBytes:length:"
- "getBytes:maxLength:usedLength:encoding:options:range:remainingRange:"
- "getBytes:range:"
- "getCString:maxLength:encoding:"
- "getCachedBundleIDToPersonasWithAttributesMap:systemPersonaUniqueString:personalPersonaUniqueString:"
- "getCachedResourceValueIfPresent:forKey:error:"
- "getCharacters:range:"
- "getClaimedActivityTypes:domains:"
- "getClientProcessVendorNameBundleIdentifierAndRestrictedIDAccessWithType:completionHandler:"
- "getContentModificationDate:error:"
- "getCreationDate:error:"
- "getCurrentApplicationDefaultInfoForCategory:completion:"
- "getDataContainerURL:error:"
- "getDefaultApplicationCategories:withCurrentDefaultApplication:error:"
- "getDeviceManagementPolicyWithCompletionHandler:"
- "getDeviceNumber:error:"
- "getDeviceRefNum:error:"
- "getDiskUsage:completionHandler:"
- "getEligibilityAnswerForDomain:withCompletionHandler:"
- "getEndpoint"
- "getExtensionPointRecordForCurrentProcessWithCompletionHandler:"
- "getExtensionPointRecordWithIdentifier:platform:completionHandler:"
- "getExtensionRange:secondaryExtensionRange:fromFileName:considerConfusables:"
- "getFSID:error:"
- "getFileIdentifier:error:"
- "getFileSystemRepresentation:error:"
- "getFileSystemRepresentation:forBookmarkData:"
- "getFileSystemRepresentation:maxLength:"
- "getFinderInfo:error:"
- "getGenericTranslocationTargetURL:error:"
- "getGroupContainersCreatingIfNecessary:"
- "getHFSType:creator:error:"
- "getHasEverChangedPreferredAppForCategory:completion:"
- "getHiddenApplicationsWithCompletion:"
- "getIdentifierOfType:completionHandler:"
- "getIdentifierOfType:vendorName:bundleIdentifier:completionHandler:"
- "getInodeNumber:error:"
- "getInstallationPredicate:uninstallationPredicate:forBundle:bundleData:database:error:"
- "getIsDirectory_NoIO:"
- "getIsURL:alwaysCheckable:hasHandler:"
- "getKernelPackageExtensionsWithCompletionHandler:"
- "getKnowledgeUUID:andSequenceNumber:"
- "getKnowledgeUUIDAndSequenceNumberWithCompletionHandler:"
- "getLength:error:"
- "getLockedApplicationsWithCompletion:"
- "getMaxProgressPhaseUnitsForLoading:restoring:installing:essentialAssets:forAppProxy:"
- "getObjects:range:"
- "getOwnerUID:error:"
- "getPreferencesWithCompletionHandler:"
- "getPreferredAppMarketplacesWithCompletion:"
- "getPreferredAppMarketplacesWithError:"
- "getRedactedAppexRecordForSystemAppexWithUUID:node:bundleIdentifier:platform:completionHandler:"
- "getRedactedPluginProxyForSystemAppexWithUUID:node:bundleIdentifier:platform:completionHandler:"
- "getRelatedTypesOfTypeWithIdentifier:maximumDegreeOfSeparation:completionHandler:"
- "getRelationship:ofDirectoryAtURL:toItemAtURL:error:"
- "getResourceValue:forKey:error:"
- "getResourceValue:forKey:options:error:"
- "getResourceValuesForKeys:mimic:preferredLocalizations:completionHandler:"
- "getServerStatusWithCompletionHandler:"
- "getServerStoreBlockingWithCompletionHandler:"
- "getServerStoreNonBlockingWithCompletionHandler:"
- "getSessionLanguagesForImproperlyLocalizedProcessWithCompletionHandler:"
- "getSettingsStoreConfigurationWithCompletionHandler:"
- "getSystemContentDatabaseObject4WebKit:"
- "getSystemContentStoreWithCompletionHandler:"
- "getSystemModeWithCompletionHandler:"
- "getTemporaryResourceValue:forKey:"
- "getTransformedBaseName:extension:needsBiDiControlCharacters:"
- "getTypeRecordForImportedTypeWithIdentifier:conformingToIdentifier:completionHandler:"
- "getTypeRecordWithIdentifier:allowUndeclared:completionHandler:"
- "getTypeRecordWithTag:ofClass:conformingToIdentifier:completionHandler:"
- "getTypeRecordsWithIdentifiers:completionHandler:"
- "getTypeRecordsWithTag:ofClass:conformingToIdentifier:completionHandler:"
- "getURLOverrideForURL:completionHandler:"
- "getUUIDBytes:"
- "getUncachedBundleIDToPersonasWithAttributesMap:systemPersonaUniqueString:personalPersonaUniqueString:"
- "getUnlocalizedBaseName:extension:requiresAdditionalBiDiControlCharacters:"
- "getValue:size:"
- "getVolumeIdentifier:error:"
- "getVolumeIdentifier:forBookmarkData:error:"
- "getWhetherTypeIdentifier:conformsToTypeIdentifier:completionHandler:"
- "getWriterBundleIdentifier:error:"
- "getiCloudHostNamesWithCompletionHandler:"
- "groupContainerIdentifiers"
- "groupContainerURLs"
- "handleFailureInFunction:file:lineNumber:description:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "handleSystemModeChangeTo:"
- "handleXPCInvocation:isReply:"
- "handlerRank"
- "handlerRankOfClaimForContentType:"
- "handlerRankWithContext:tableID:unitID:unitBytes:"
- "hasComplication"
- "hasCustomNotification"
- "hasDatabaseAccess"
- "hasDirectoryPath"
- "hasEntitlementToClearAllIdentifiersOfType:"
- "hasGlance"
- "hasHiddenExtension"
- "hasLocalizedUsageDescriptionForFeature:contextKey:"
- "hasMIDBasedSINF"
- "hasObjectValueForSelector:"
- "hasPackageBit"
- "hasParallelPlaceholder"
- "hasPersistentPreferences"
- "hasPrefix:"
- "hasResourceValueForKey:"
- "hasServer"
- "hasSettingsBundle"
- "hasSuffix:"
- "hasUninstallEntitlement"
- "hash"
- "helperPlaceholdersInstalled:"
- "helperPlaceholdersUninstalled:"
- "hiddenApplicationsForLSDUseOnly"
- "honorPreferenceForNoHandler"
- "host"
- "i16@0:8"
- "i24@0:8Q16"
- "i32@0:8@16^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}24"
- "i36@0:8@16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
- "i40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
- "iCloudEmailPrefsURL"
- "iCloudEmailPrefsURL:"
- "iCloudFamilyURL:"
- "iCloudSchoolworkURL:"
- "iCloudSharingURL"
- "iCloudSharingURL_noFragment"
- "iTunesMetadataWithContext:tableID:unitID:unitBytes:"
- "iTunesStoreURL"
- "iTunesStoreURL:"
- "iWorkApplicationName"
- "iWorkDocumentName"
- "iWorkURL"
- "iconChangeAlertTokenForIdentity:error:"
- "iconDataForStyle:width:height:options:"
- "iconDataForVariant:"
- "iconDataForVariant:withOptions:"
- "iconDictionary"
- "iconDictionaryWithContext:tableID:unitID:unitBytes:"
- "iconFileNames"
- "iconIsPrerendered"
- "iconResourceBundleURL"
- "iconResourceBundleURLWithContext:tableID:unitID:unitBytes:"
- "iconResourceLocator"
- "iconUsesAssetCatalog"
- "iconsDict"
- "iconsDictionaryFromDict:"
- "identifierForCurrentProcess"
- "identifierWithContext:tableID:unitID:unitBytes:"
- "identifiersFileURL"
- "identifiersOfTypeNotDispatched:"
- "identities"
- "identity"
- "identityStringsForApplicationWithBundleIdentifier:error:"
- "identityUsageDescription"
- "ignoreOpenStrategy"
- "ignoreStrongBindingPreferences"
- "ignoreWeakBindingPreferences"
- "illegalCharacterSet"
- "imageOrVideo"
- "importedTypeRecords"
- "importedTypeRecordsWithContext:tableID:unitID:unitBytes:"
- "importedTypes"
- "inEducationMode"
- "inPublicDomain"
- "inSyncBubble"
- "inXCTestRigInsecure"
- "includePlugins"
- "indexOfObject:"
- "infoDictionaryWithContext:tableID:unitID:unitBytes:"
- "init"
- "initByResolvingBookmarkData:options:relativeToNode:bookmarkDataIsStale:error:"
- "initByResolvingBookmarkData:relativeToNode:bookmarkDataIsStale:error:"
- "initContentBitsWithDisplayName:treatAsFSName:"
- "initFileURLWithFileSystemRepresentation:isDirectory:relativeToURL:"
- "initFileURLWithPath:"
- "initFileURLWithPath:isDirectory:"
- "initFileURLWithPath:isDirectory:relativeToURL:"
- "initForBundleWithIdentifier:placeholderInstalled:fullApplicationInstalled:"
- "initForInstallMachineryWithBundleIdentifier:error:"
- "initForInstallMachineryWithBundleIdentifier:placeholder:error:"
- "initForRecord:personaWithAttributes:"
- "initNamePartsWithDisplayName:"
- "initNodeBitsWithContextIfNeeded:node:isDirectory:bundleClass:"
- "initPrivately"
- "initWithActivityType:"
- "initWithAppEnumerationOptions:"
- "initWithApplicationDSID:downloaderDSID:familyID:isRedacted:"
- "initWithArray:"
- "initWithBacktrace"
- "initWithBindable:"
- "initWithBindingConfiguration:"
- "initWithBundleID:isPlaceholder:"
- "initWithBundleID:type:"
- "initWithBundleIdentifier:"
- "initWithBundleIdentifier:URL:personaUniqueString:personaType:"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "initWithBundleIdentifier:allowPlaceholder:personaUniqueString:error:"
- "initWithBundleIdentifier:error:"
- "initWithBundleIdentifier:fetchingPlaceholder:error:"
- "initWithBundleIdentifier:preferPlaceholder:"
- "initWithBundleIdentifier:requireValid:error:"
- "initWithBundleIdentifier:requireValid:platform:error:"
- "initWithBundleIdentifier:sdkDictionary:entitlements:"
- "initWithBundleIdentifier:stateFlags:ratingRank:ratingRankEligibilityDomain:installType:"
- "initWithBundleIdentifierOfCompanionApplication:error:"
- "initWithBundleIdentifierOfSystemPlaceholder:error:"
- "initWithBundleProvider:stringsFile:legacyLocalizationList:"
- "initWithBundleURL:stringsFile:"
- "initWithBundleURL:stringsFile:checkMainBundle:legacyLocalizationList:"
- "initWithBundleURL:stringsFile:legacyLocalizationList:"
- "initWithBytes:length:"
- "initWithBytes:length:encoding:"
- "initWithBytes:objCType:"
- "initWithBytesNoCopy:length:deallocator:"
- "initWithBytesNoCopy:length:encoding:freeWhenDone:"
- "initWithBytesNoCopy:length:freeWhenDone:"
- "initWithCFBundle:"
- "initWithCFBundle:stringsFile:"
- "initWithCFBundle:stringsFile:legacyLocalizationList:"
- "initWithCapacity:"
- "initWithCharacters:length:"
- "initWithCoder:"
- "initWithConfiguration:error:"
- "initWithConfigurationString:flags:error:"
- "initWithConnection:"
- "initWithContentsOfFile:"
- "initWithContentsOfURL:"
- "initWithContentsOfURL:error:"
- "initWithContentsOfURL:options:error:"
- "initWithContext:bundleUnit:bundleData:"
- "initWithContext:directoryURL:volumeURL:enumerationOptions:filteringOptions:"
- "initWithContext:operationUUID:bundleIdentifier:precondition:type:"
- "initWithContext:operationUUID:itemInfoDict:personas:"
- "initWithContext:options:unitIDs:unitCount:"
- "initWithContext:parentBundleID:options:"
- "initWithContext:unitID:"
- "initWithContext:volumeURL:options:"
- "initWithContextIfNeeded:node:isDirectory:bundleClass:desiredDisplayName:treatAsFSName:"
- "initWithData:encoding:"
- "initWithDatabase:"
- "initWithDatabase:bundleUnit:bundleData:"
- "initWithDatabase:bundleUnit:delegate:"
- "initWithDatabase:pluginUnit:"
- "initWithDatastore:defaultAppEvaluator:"
- "initWithDictionary:"
- "initWithDictionary:copyItems:"
- "initWithDictionary:error:"
- "initWithDirectory:inDomain:lastPathComponent:createIntermediateDirectories:flags:error:"
- "initWithDisplayType:handler:"
- "initWithDocumentProxy:"
- "initWithDocumentProxy:bindingStyle:"
- "initWithDocumentProxy:style:handlerRank:"
- "initWithDomain:code:userInfo:"
- "initWithEligibilityCache:"
- "initWithEndpoint:"
- "initWithExtensionPoint:options:"
- "initWithExtensionPointIdentifier:"
- "initWithExtensionPointIdentifier:options:"
- "initWithExtensionPointIdentifier:options:filter:"
- "initWithExtensionPointIdentifier:options:platform:"
- "initWithExtensionPointIdentifier:options:platform:filter:"
- "initWithFileDescriptor:closeOnDealloc:"
- "initWithFileSystemRepresentation:flags:error:"
- "initWithFireDate:interval:target:selector:userInfo:repeats:"
- "initWithFormat:"
- "initWithFormat:arguments:"
- "initWithFrames:count:"
- "initWithIOPersonality:"
- "initWithIOQueue:"
- "initWithIdentifier:"
- "initWithIdentifier:error:"
- "initWithIdentifier:parentAppRecord:error:"
- "initWithIdentifier:platform:error:"
- "initWithIdentifier:platform:parentAppRecord:error:"
- "initWithIdentity:manager:"
- "initWithIdentityBookmark:identityString:personaUniqueString:personaType:"
- "initWithIdentityString:"
- "initWithIdentityString:parsedIdentityStringDictionary:error:"
- "initWithIdentityString:personaUniqueString:personaType:"
- "initWithInfoPlist:SDKPlist:"
- "initWithLazyPropertyLists:"
- "initWithListenerEndpoint:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "initWithName:object:userInfo:"
- "initWithNode:"
- "initWithNotification:appProxies:plugins:"
- "initWithNotification:bundleIDs:plugins:options:"
- "initWithObjects:"
- "initWithObjects:count:"
- "initWithOperation:wrappedDelegate:"
- "initWithOptions:"
- "initWithOriginalURL:"
- "initWithOriginalURL:checkingForAvailableApplications:"
- "initWithParent:bundleID:andPhase:"
- "initWithParent:userInfo:"
- "initWithPath:flags:error:"
- "initWithPayload:"
- "initWithPersistentIdentifier:"
- "initWithPersona:"
- "initWithPlugInUnits:forDatabaseWithUUID:"
- "initWithPolicyChangeHandler:"
- "initWithPreparationError:"
- "initWithPrimaryBundleID:operation:"
- "initWithPrimaryBundleID:placeholder:"
- "initWithPropertyList:"
- "initWithPropertyListData:"
- "initWithQueue:"
- "initWithRecord:error:"
- "initWithReferenceDate:didRefresh:refreshAfter:defaultForCategory:"
- "initWithRemotePlaceholderBundleIdentifier:error:"
- "initWithResolver:"
- "initWithServiceType:applicationIdentifier:domain:"
- "initWithSettings:"
- "initWithSliceDescData:"
- "initWithState:binding:"
- "initWithStatsGatherer:"
- "initWithStore:"
- "initWithStore:useStandardTableFunctions:"
- "initWithStoreItemIdentifier:error:"
- "initWithStrategy:operationUUID:"
- "initWithStrategy:operationUUID:URL:"
- "initWithStrategy:operationUUID:itemInfoDict:"
- "initWithStrategy:operationUUID:itemInfoDict:personas:"
- "initWithString:"
- "initWithString:relativeToURL:"
- "initWithTargetUID:"
- "initWithTimeIntervalSinceReferenceDate:"
- "initWithType:subtype:"
- "initWithTypeIdentifier:"
- "initWithTypeIdentifier:error:"
- "initWithURL:"
- "initWithURL:allowPlaceholder:error:"
- "initWithURL:bundleIdentifier:placeholderFetchBehavior:requiredRelationship:"
- "initWithURL:error:"
- "initWithURL:fetchingPlaceholder:error:"
- "initWithURL:flags:error:"
- "initWithURL:name:type:MIMEType:isContentManaged:sourceAuditToken:"
- "initWithURL:requireValid:error:"
- "initWithURL:resolvingAgainstBaseURL:"
- "initWithURL:useCacheIfPossible:"
- "initWithUTF8String:"
- "initWithUUID:"
- "initWithUUID:error:"
- "initWithUUID:requireValid:error:"
- "initWithUUIDBytes:"
- "initWithUUIDString:"
- "initWithValidatedPlist:"
- "initWithVisualizer:fileHandle:closeWhenDone:error:"
- "initWithWindowOpenDate:refreshDate:defaultForCategory:"
- "initWithWindowOpenDates:refreshDate:defaultForCategory:"
- "initWithXPCConnection:"
- "initWithXPCListener:"
- "initialize"
- "initiateProgressForApp:withType:"
- "insertCompleteNameBiDiControlCharacters:"
- "insertNameComponentBiDiControlCharacters:"
- "insertObject:atIndex:"
- "installApplication:atURL:withOptions:installType:reply:"
- "installApplication:withOptions:"
- "installApplication:withOptions:error:"
- "installApplication:withOptions:error:usingBlock:"
- "installContainerizedApplicationArtifactAtURL:withOptions:error:progressBlock:"
- "installContainerizedApplicationArtifactAtURL:withOptions:returningRecordPromise:error:progressBlock:"
- "installFailureReason"
- "installJournalDirectoryURL"
- "installOperation"
- "installPhaseFinishedForProgress:"
- "installPhaseString"
- "installProgress"
- "installProgressForApplication:withPhase:"
- "installProgressForBundleID:makeSynchronous:"
- "installProgressSync"
- "installSessionIdentifier"
- "installSessionIdentifierWithContext:tableID:unitID:unitBytes:"
- "installTypeWithContext:tableID:unitID:unitBytes:"
- "installationEndedForApplication:withState:"
- "installationFailedForApplication:"
- "installationFailedForApplication:reply:"
- "installedPlugins"
- "instanceMethodSignatureForSelector:"
- "instancesRespondToSelector:"
- "intValue"
- "integerValue"
- "intentDefinitionURLs"
- "intentDefinitionURLsWithContext:tableID:unitID:unitBytes:"
- "intentsRestrictedWhileLocked"
- "intentsRestrictedWhileProtectedDataUnavailable"
- "interfaceWithProtocol:"
- "internalCanOpenURL:publicSchemes:privateSchemes:XPCConnection:error:"
- "internalQueue"
- "intersectSet:"
- "intersectsSet:"
- "invalidate"
- "invalidateCache"
- "invalidateIconCache:"
- "invalidateRestrictions"
- "invalidateSettings"
- "invoke"
- "invokeServiceInvocation:isReply:"
- "isAVCHDCollection"
- "isAccessing"
- "isActive"
- "isAdHocCodeSigned"
- "isAliasFile"
- "isAllowlistEnabled"
- "isAlwaysAvailable"
- "isAlwaysEnabled"
- "isAnyRegisteredApplicationInstalledFromDistributorOrWeb"
- "isAppStoreVendable"
- "isAppStoreVendableWithContext:tableID:unitID:unitBytes:"
- "isAppUpdate"
- "isAppleInternal"
- "isAppleInternalWithContext:tableID:unitID:unitBytes:"
- "isApplicationAvailableToOpenURL:error:"
- "isApplicationAvailableToOpenURL:includePrivateURLSchemes:error:"
- "isApplicationAvailableToOpenURLCommon:includePrivateURLSchemes:error:"
- "isApplicationEligibleForReadOnlyDocumentOpenBehavior:"
- "isApplicationRegisteredWithbundleID:placeholder:"
- "isApproved"
- "isArcadeApp"
- "isBeta"
- "isBetaApp"
- "isBindingMapValid"
- "isBookmarkDataFull:"
- "isBundleEligibleForOpenDocumentViaOpenURL:"
- "isBundleID:bundleData:context:allowedToCheckScheme:error:"
- "isBusyDirectory"
- "isCancellable"
- "isChildOfTypeIdentifier:"
- "isContentDiscarded"
- "isContentManaged"
- "isCoreType"
- "isCurrentProcessAnApplicationExtension"
- "isCurrentProcessEligibleForOpenDocumentViaOpenURL"
- "isCurrentProcessEligibleForReadOnlyDocumentOpenBehavior"
- "isDataContainer"
- "isDeclared"
- "isDefaultForCategory"
- "isDefaultPersona"
- "isDeletable"
- "isDeletableIgnoringRestrictions"
- "isDeletableSystemApplication"
- "isDeletableSystemApplicationWithContext:tableID:unitID:unitBytes:"
- "isDeletableWithContext:tableID:unitID:unitBytes:"
- "isDeviceBasedVPP"
- "isDowngraded"
- "isDynamic"
- "isEligibleForWatchAppInstall"
- "isEligibleMailClient"
- "isEligibleWebBrowser"
- "isEnabled"
- "isEnabledByDefault"
- "isEnterprisePersona"
- "isEqual:"
- "isEqualToNumber:"
- "isEqualToSpotlightAction:"
- "isEqualToString:"
- "isExecutable"
- "isExecutableModeFile"
- "isExported"
- "isFeature:enabledInDomain:"
- "isFeatureAllowed:"
- "isFileReferenceURL"
- "isFileSharingEnabled"
- "isFileURL"
- "isForManualRebuild"
- "isForcedForRemoteUpdates"
- "isForcedForXCTesting"
- "isFreeProfileValidated"
- "isGameCenterEnabled"
- "isHidden"
- "isImageOrVideo"
- "isImported"
- "isInEducationMode"
- "isInPublicDomain"
- "isInSyncBubble"
- "isInTrash"
- "isInXCTestRigInsecure"
- "isInstalledFromDistributorOrWeb"
- "isKindOfClass:"
- "isLaunchDisabled"
- "isLaunchProhibited"
- "isLegacy"
- "isLightweightSystemServer"
- "isLinkEnabled"
- "isLinkEnabledWithContext:tableID:unitID:unitBytes:"
- "isMailClient"
- "isMainThread"
- "isManagedAppDistributor"
- "isMemberOfClass:"
- "isMet"
- "isMountTrigger"
- "isMultiUser"
- "isNewsstandApp"
- "isObservinglsd"
- "isOnDiskImage"
- "isOnLocalVolume"
- "isOnTimeMachineVolume"
- "isOpenInRestrictionInEffect"
- "isOpenWindowGroupFull"
- "isPausable"
- "isPersonalPersona"
- "isPrioritizable"
- "isProfileValidated"
- "isProxy"
- "isPurchasedReDownload"
- "isPurchasedRedownload"
- "isRedacted"
- "isRegionChina"
- "isRegularFile"
- "isRemovableByInstallMachinery"
- "isRemoveableSystemApp"
- "isRemovedSystemApp"
- "isResolvable"
- "isRestrictedWithStateProvider:"
- "isSecuredSystemContent"
- "isSensitive"
- "isServer"
- "isSharedIPad"
- "isSideFault"
- "isStandaloneWatchApp"
- "isStringNaturallyRTL:"
- "isSubclassOfClass:"
- "isSubsetOfSet:"
- "isSwiftPlaygroundsApp"
- "isSymbolicLink"
- "isSystemPersona"
- "isSystemPlaceholder"
- "isSystemPlaceholderWithContext:tableID:unitID:unitBytes:"
- "isSystemServer"
- "isTemplateApplication"
- "isTemplateProxyApplication"
- "isTrashFolder"
- "isTrustedForBinding"
- "isUIApplicationElement"
- "isUPPValidated"
- "isUpdate"
- "isUpdating"
- "isUserServer"
- "isUsingEphemeralStorage"
- "isValidAlternateIcon:forIconsDict:"
- "isVersion:greaterThanOrEqualToVersion:"
- "isVolume"
- "isWatchKitApp"
- "isWatchOnly"
- "isWebApp"
- "isWebAppPlaceholder"
- "isWebBrowser"
- "isWhitelisted"
- "isWildcard"
- "isWrapped"
- "isWrapper"
- "isXPCConnection:allowedToCheckScheme:error:"
- "isiWorkURL"
- "issueSandboxExceptionsIfMayNotMapDatabase"
- "jobLabel"
- "journalNotificationURLFormatString"
- "journalURL"
- "journalledNotifications"
- "keyPathsForValuesAffectingInstallPhase"
- "keyPathsForValuesAffectingInstallState"
- "keynoteLiveURL"
- "keynoteLiveURL:"
- "keynoteLiveURL_noFragment"
- "keynoteLiveURL_noFragment:"
- "lastFiredDate"
- "lastObject"
- "lastPathComponent"
- "latency"
- "launchDisabled"
- "launchOptions"
- "launchProhibited"
- "layoutRole"
- "lazyPropertyListWithContext:unit:"
- "lazyPropertyListWithDatabase:unit:"
- "legacy"
- "legacyApplicationProxiesListWithType:"
- "legacyRecordDictionary"
- "legacy_isBundleID:bundleData:context:allowedToCheckScheme:error:"
- "length"
- "libraryItems"
- "libraryPath"
- "lieWithCompletionHandler:"
- "lightweightSystemServer"
- "limit"
- "link:unit:"
- "link:unit:linkedText:"
- "linkURL:"
- "linkURL:linkedText:"
- "linkedChildApplicationRecordEnumeratorWithOptions:"
- "linkedParentApplication"
- "linkedParentBundleID"
- "listAllPersonaAttributesWithError:"
- "listAllPersonaWithAttributes"
- "listener"
- "listener:shouldAcceptNewConnection:"
- "loadAndReturnError:"
- "loadJournalledNotificationsFromDisk"
- "loadPluginsAtURL:"
- "loadProportions"
- "localObservers"
- "localizedDescription"
- "localizedDescriptionDictionary"
- "localizedDescriptionWithPreferredLocalizations:"
- "localizedIdentityUsageDescription"
- "localizedMicrophoneUsageDescription"
- "localizedNameForContext:"
- "localizedNameForContext:preferredLocalizations:"
- "localizedNameForContext:preferredLocalizations:useShortNameOnly:"
- "localizedNameWithContext:"
- "localizedNameWithContext:preferredLocalizations:"
- "localizedNameWithPreferredLocalizations:"
- "localizedNameWithPreferredLocalizations:useShortNameOnly:"
- "localizedShortNameWithPreferredLocalizations:"
- "localizedStandardCompare:"
- "localizedStringDictionaryWithString:defaultValue:"
- "localizedStringForCanonicalString:preferredLocalizations:context:"
- "localizedStringWithString:inBundle:localeCode:"
- "localizedStringWithString:inBundle:preferredLocalizations:"
- "localizedStringWithString:preferredLocalizations:"
- "localizedStrings"
- "localizedStringsForCanonicalString:context:"
- "localizedStringsWithStrings:preferredLocalizations:"
- "localizedUsageDescriptionForFeature:"
- "localizedUsageDescriptionForFeature:contextKey:"
- "localizedUsageDescriptionForFeature:contextKey:preferredLocalizations:"
- "localizedUsageDescriptionForFeature:preferredLocalizations:"
- "localizedValuesForKeys:fromTable:"
- "lock"
- "lockedApplicationsForLSDUseOnly"
- "logStep:byParty:phase:success:forBundleID:description:"
- "longCharacterIsMember:"
- "longLongValue"
- "longValue"
- "ls_caseInsensitiveContainsString:"
- "ls_cleanForPluginQuery"
- "ls_decodeArrayWithValuesOfClass:forKey:"
- "ls_decodeDictionaryWithKeysOfClass:valuesOfClass:forKey:"
- "ls_decodeDictionaryWithKeysOfClass:valuesOfClasses:forKey:"
- "ls_decodeObjectOfClass:forKey:"
- "ls_decodeObjectOfClasses:forKey:"
- "ls_decodeSetWithValuesOfClass:forKey:"
- "ls_expectedFinalInstallPhase"
- "ls_fixupExtensionPointIdentifierKey"
- "ls_hashQuery"
- "ls_injectUTTypeWithDeclaration:inDatabase:error:"
- "ls_insertExtensionPointVersion:"
- "ls_matchesForPluginQuery:"
- "ls_matchesStringForPluginQuery:"
- "ls_parseQueryForIdentifiers:"
- "ls_preferredLocalizations"
- "ls_resetTestingDatabase"
- "ls_resolvePlugInKitInfoPlistWithDictionary:"
- "ls_setExpectedFinalInstallPhase:"
- "ls_setPreferredLocalizations:"
- "ls_testWithCleanDatabaseWithError:"
- "ls_unarchivedObjectOfClass:fromData:error:"
- "ls_visuallyOrderCharactersReturningError:"
- "machOUUIDsForBundleIdentifiers:error:"
- "machOUUIDsWithContext:tableID:unitID:unitBytes:"
- "mailClient"
- "mainBundle"
- "mainDataVolumeStagingURLWithError:"
- "mainRunLoop"
- "mainSystemContainerURL"
- "mainUserContainerURL"
- "makeStagingDirectoryNodeInContainer:error:"
- "managedPersonas"
- "managedSourceAuditToken"
- "managementDomain"
- "managementDomainWithContext:tableID:unitID:unitBytes:"
- "mapBundleIdentifiers:orMachOUUIDs:completionHandler:"
- "mapPlugInBundleIdentifiersToContainingBundleIdentifiers:completionHandler:"
- "mapsURL"
- "markLocalizationsStoredInDatabase"
- "matchesPlugin:pluginData:withDatabase:"
- "maxSystemVersion"
- "maximumHandlerRank"
- "maximumRating"
- "maximumSystemVersion"
- "maximumSystemVersionWithContext:tableID:unitID:unitBytes:"
- "mayBeBUIVisible"
- "mayHideExtensionWithContextIfNeeded:"
- "mayProcessWithAuditTokenMapDatabase:"
- "member:"
- "messageObserversWithSelector:"
- "messageObserversWithSelector:andApps:"
- "messageObserversWithSelector:andApps:filterLaunchProhibited:"
- "methodSignatureForSelector:"
- "microphoneUsageDescription"
- "migrateIdentities:error:"
- "migrateIdentity:error:"
- "migratedIdentitiesForIdentity:"
- "mimic"
- "minInterval"
- "minSystemVersion"
- "minimumHandlerRank"
- "minimumSystemVersion"
- "minimumSystemVersionWithContext:tableID:unitID:unitBytes:"
- "minusSet:"
- "missingFlag:name:"
- "missingFlag:name:color:"
- "missingLocalizationPlaceholder"
- "missingRequiredSINF"
- "mobileInstallIDs"
- "mobileInstallationQueue"
- "modifyPreferencesWithBlock:"
- "mountTrigger"
- "mutableBytes"
- "mutableCopy"
- "mutableCopyWithZone:"
- "nameForBookmarkData:error:"
- "nameWithContext:tableID:unitID:unitBytes:"
- "nameWithError:"
- "needsMigration"
- "needsUpdate"
- "networkUsageChanged:"
- "new"
- "newFrameworkBundleLocalizer"
- "newWithStore:buffer:"
- "newestWindowOpenDate"
- "newlineCharacterSet"
- "newsstandApp"
- "nextObject"
- "noteExtantChildNodeWithRelativePath:"
- "noteMigratorRunningWithReply:"
- "noteRestrictionsUpdateForOpensWithCompletion:"
- "notification"
- "notificationJournallerForBundleIdentifier:registeringPlaceholder:"
- "notificationTypeForOperation:"
- "notifyObservers:withApplications:"
- "notifyToken"
- "now"
- "nsExtensionUsesLSSettingsStore"
- "null"
- "numberForKey:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLongLong:"
- "numberWithUnsignedChar:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLong:"
- "numberWithUnsignedLongLong:"
- "numberWithUnsignedShort:"
- "objCType"
- "object"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectEnumerator"
- "objectForInfoDictionaryKey:"
- "objectForInfoDictionaryKey:ofClass:"
- "objectForInfoDictionaryKey:ofClass:inScope:"
- "objectForInfoDictionaryKey:ofClass:valuesOfClass:"
- "objectForKey:"
- "objectForKey:checkingKeyClass:checkingValueClass:"
- "objectForKey:ofClass:"
- "objectForKey:ofClass:valuesOfClass:"
- "objectForKey:ofType:"
- "objectForKeyedSubscript:"
- "objectsForInfoDictionaryKeys:"
- "objectsForKeys:"
- "objectsPassingTest:"
- "observeDatabaseChange4WebKit:"
- "observeValueForKeyPath:ofObject:change:context:"
- "observedInstallProgresses"
- "observerDidObserveDatabaseChange:"
- "observerProxy"
- "observerQueue"
- "observerSelectorForNotification:"
- "observerSet"
- "observinglsd"
- "oldestWindowOpenDate"
- "onDemandResourcesUsage"
- "onDiskImage"
- "onLocalVolume"
- "onSystemPartition"
- "oneTapOpenClaimBindingConfigurationForBindable:"
- "openAppLink:state:completionHandler:"
- "openApplication:withOptions:clientHandle:completion:"
- "openApplicationWithBundleID:"
- "openApplicationWithBundleIdentifier:configuration:completionHandler:"
- "openApplicationWithBundleIdentifier:usingConfiguration:completionHandler:"
- "openApplicationWithIdentifier:options:useClientProcessHandle:completionHandler:"
- "openInWebBrowser:setAppropriateOpenStrategyAndWebBrowserState:completionHandler:"
- "openInWebBrowser:setOpenStrategy:webBrowserState:completionHandler:"
- "openInWebBrowser:setOpenStrategy:webBrowserState:configuration:completionHandler:"
- "openResourceOperation:didFailWithError:"
- "openResourceOperation:didFinishCopyingResource:"
- "openResourceOperationDidComplete:"
- "openSensitiveURL:withOptions:"
- "openSensitiveURL:withOptions:error:"
- "openStrategy"
- "openURL:"
- "openURL:configuration:completionHandler:"
- "openURL:configuration:error:"
- "openURL:fileHandle:options:completionHandler:"
- "openURL:withOptions:"
- "openURL:withOptions:error:"
- "openUserActivity:usingApplicationRecord:configuration:completionHandler:"
- "openUserActivity:withApplicationProxy:completionHandler:"
- "openUserActivity:withApplicationProxy:options:completionHandler:"
- "openUserActivityWithUUID:activityType:usingApplicationRecord:configuration:completionHandler:"
- "openUserActivityWithUniqueIdentifier:activityData:activityType:bundleIdentifier:options:completionHandler:"
- "openWindowGroupFull"
- "openWithCompletionHandler:"
- "openWithConfiguration:completionHandler:"
- "openWithURL:completionHandler:"
- "openWithURL:configuration:completionHandler:"
- "operation %@: Not all persona updates were successful, but %zu were, so arming save timer"
- "operation %@: could not get affected bundle info for persona change: %@"
- "operationToOpenResource:usingApplication:uniqueDocumentIdentifier:isContentManaged:sourceAuditToken:userInfo:configuration:delegate:"
- "operationToOpenResource:usingApplication:uniqueDocumentIdentifier:isContentManaged:sourceAuditToken:userInfo:options:delegate:"
- "operationToOpenResource:usingApplication:uniqueDocumentIdentifier:sourceIsManaged:userInfo:delegate:"
- "operationToOpenResource:usingApplication:uniqueDocumentIdentifier:sourceIsManaged:userInfo:options:delegate:"
- "operationToOpenResource:usingApplication:uniqueDocumentIdentifier:userInfo:"
- "operationToOpenResource:usingApplication:uniqueDocumentIdentifier:userInfo:delegate:"
- "operationToOpenResource:usingApplication:userInfo:"
- "operationWithUUID:didFailToSaveWithError:"
- "operationWithUUIDWasSaved:"
- "optionsFromOpenConfiguration:"
- "optionsWithDictionary:"
- "optsOutOfAppProtectionShield"
- "originalInstallType"
- "originalURL"
- "overrideURL"
- "parentAppRecord"
- "parentAppRecordWithContext:tableID:unitID:unitBytes:"
- "parentApplicationRecord"
- "parentProgressForApplication:andPhase:isActive:"
- "parentTypeIdentifiers"
- "parentTypeIdentifiersWithContext:tableID:unitID:unitBytes:"
- "parseActivityTypesFromDictionary:"
- "parseArchitecturesFromDict:"
- "parseDeviceFamilyFromDict:"
- "parseDocumentClaimsFromDict:"
- "parseIconFilenamesFromDict:forPlatform:"
- "parseInfoPlist:"
- "parseInstallationInfo:"
- "parseNSExtensionSDKDefinitionsFromDictionary:"
- "parsePersonas:error:"
- "parsePlaceholderMetadata:"
- "parseSINFDictionary:"
- "parseURLClaimsFromDict:"
- "parseiTunesMetadata:"
- "pathComponents"
- "pathExtension"
- "pathForBookmarkData:error:"
- "pathForResource:ofType:"
- "pathWithError:"
- "pause"
- "pedigree"
- "pedigreeWithContext:tableID:unitID:unitBytes:"
- "performJournalRecovery"
- "performOpenOperationWithURL:fileHandle:bundleIdentifier:documentIdentifier:isContentManaged:sourceAuditToken:userInfo:options:delegate:completionHandler:"
- "performPostInstallationRegistration:personaUniqueStrings:operationUUID:reply:"
- "performPostUninstallationUnregistrationOfBundleID:operationUUID:unregisterType:precondition:reply:"
- "performRebuildRegistration:personaUniqueStrings:reply:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:operationUUID:reply:"
- "persona with type %d did not have a persona unique string, ignoring!"
- "personaAttributesForPersonaType:"
- "personaAttributesForPersonaUniqueString:withError:"
- "personaGenerationIdentifierWithError:"
- "personaIsApplicable:"
- "personaWithUniqueString:getPersonaType:error:"
- "personalPersonaAttributes"
- "photosURL"
- "pid"
- "placeholderApplications"
- "placeholderFailureReason"
- "placeholderFailureReasonWithContext:tableID:unitID:unitBytes:"
- "placeholderInstalledForIdentifier:filterDowngrades:"
- "platformWithContext:tableID:unitID:unitBytes:"
- "plistRepresentation"
- "plugInClasses"
- "plugInKitPlugins"
- "plugInKitProxyForPlugin:withContext:"
- "plugInKitProxyForPlugin:withContext:applicationExtensionRecord:resolveAndDetach:"
- "plugInKitProxyForUUID:bundleIdentifier:pluginIdentifier:effectiveIdentifier:version:bundleURL:"
- "pluginCanProvideIcon"
- "pluginDataForPlugin:"
- "pluginFlags"
- "pluginFlagsWithContext:tableID:unitID:unitBytes:"
- "pluginKitDictionary"
- "pluginKitProxyForIdentifier:"
- "pluginKitProxyForURL:"
- "pluginKitProxyForUUID:"
- "pluginMIDicts"
- "pluginPlists"
- "pluginQuery"
- "pluginQueryWithIdentifier:"
- "pluginQueryWithQueryDictionary:applyFilter:"
- "pluginQueryWithURL:"
- "pluginQueryWithUUID:"
- "plugins"
- "pluginsByBundleIentifier"
- "pluginsDidInstall:"
- "pluginsDidUninstall:"
- "pluginsMatchingQuery:applyFilter:"
- "pluginsWillUninstall:"
- "pluginsWithIdentifiers:protocols:version:"
- "pluginsWithIdentifiers:protocols:version:applyFilter:"
- "pluginsWithIdentifiers:protocols:version:withFilter:"
- "pointerAtIndex:"
- "populateHFSTypeAndCreatorWithError:"
- "populateHasChildNodeWithRelativePath:"
- "populateSimpleSelector:error:"
- "populateValueForKey:error:"
- "port"
- "postNotificationName:object:"
- "postSettingsChangeNotification"
- "preSydroFSecurePreferencesFileURL"
- "preUnregistrationContextForBundleIdentifier:"
- "preUnregistrationContextForBundleUnit:context:"
- "prebootVolumeNode"
- "preconditionCheckingRelationshipToURL:ofBundleWithIdentifier:placeholderFetchBehavior:requiredRelationship:"
- "predicate"
- "predicateWithBlock:"
- "predicateWithFormat:"
- "predicateWithValue:"
- "preferenceSetDateForDefaultAppCategory:error:"
- "preferencesFileChangeNotificationName"
- "preferencesFileURL"
- "preferencesUpdateNotificationName"
- "preferredArchitecture"
- "preferredLanguages"
- "preferredLocalizations"
- "preferredLocalizationsForXCTests"
- "preferredTagOfClass:"
- "prepareForReuse"
- "prepareMimicWithPopulator:error:"
- "presentWithCompletion:"
- "previousInstallType"
- "prewarm"
- "primaryBundleID"
- "primaryIconDataForVariant:"
- "primaryIconName"
- "principalClass"
- "privacyTrackingDomains"
- "privateURLSchemes"
- "processHandle"
- "processHandleForNSXPCConnection:"
- "processIdentifier"
- "profileValidated"
- "profileValidationState"
- "progressForBundleID:"
- "progressProportionsForBundleID:"
- "progressProportionsStateURL"
- "progressQueue"
- "promptAndCallSpringBoardWithCompletionHandler:"
- "propertyListCachingStrategy"
- "propertyListWithClass:"
- "propertyListWithClass:valuesOfClass:"
- "propertyListWithContentsOfURL:options:error:"
- "propertyListWithData:"
- "propertyListWithData:options:format:error:"
- "propertyListWithDictionary:"
- "propertyQueue"
- "provider"
- "proxies"
- "proxyUIDForCurrentEffectiveUID"
- "proxyUIDForUID:"
- "publicURLSchemes"
- "publishingKeyForApp:withPhase:"
- "purchasedReDownload"
- "purchaserDSID"
- "q16@0:8"
- "q24@0:8@16"
- "queriableSchemes"
- "queriedSchemesMapFileURL"
- "queryForApplicationsAvailableForOpeningURL:"
- "queryItemWithName:value:"
- "queryItems"
- "queryResultForCategory:error:"
- "queryWithBundleIdentifier:"
- "queryWithIdentifier:"
- "queryWithPlistFlags:bundleFlags:"
- "queryWithType:"
- "querying MCM for container for %@, class %llx, platform %lu"
- "querying MCM for environment for %@, class %llx, platform %lu"
- "queue"
- "r^v16@0:8"
- "r^{?=[8I]}16@0:8"
- "r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20@0:8I16"
- "raise:format:"
- "rangeOfCharacterFromSet:"
- "rangeOfFirstMatchInString:options:range:"
- "rangeOfString:"
- "rangeOfString:options:"
- "rangeValue"
- "ratingRankExceptionBundleIDs"
- "rawValues"
- "readFromDBWithError:"
- "rebuildApplicationDatabasesForSystem:internal:user:completionHandler:"
- "rebuildDatabaseContentForFrameworkAtURL:completionHandler:"
- "rebuildInstallIndexes"
- "recordBuilderForType:"
- "recordForUnredactingWithContext:error:"
- "redact"
- "redactedAppexRecordWithUUID:node:bundleIdentifier:platform:error:"
- "redactedDescription"
- "redactedProperties"
- "referenceAccessoryURL"
- "referenceURL"
- "referenceURLWithContext:tableID:unitID:unitBytes:"
- "refreshContentInFrameworkAtURL:reply:"
- "refreshDate"
- "refreshExtensionPointsWithOperationUUID:reply:"
- "refreshFromUserManagementIfNecessary"
- "refreshQueryResultForApplication:category:"
- "refreshUnbundledSystemExtensionPointsWithOperationUUID:requestContext:saveObserver:registrationError:"
- "regionChina"
- "registerApplication:"
- "registerApplicationDictionary:"
- "registerApplicationDictionary:withObserverNotification:"
- "registerApplicationForRebuildWithInfoDictionaries:personaUniqueStrings:requestContext:registrationError:"
- "registerApplicationForRebuildWithInfoDictionaries:requestContext:registrationError:"
- "registerApplicationForRebuildWithInstallationRecord:extensionInstallationRecords:personaUniqueStrings:requestContext:registrationError:"
- "registerBuiltinAppex:operationUUID:reply:"
- "registerBuiltinApplication:personaUniqueStrings:operationUUID:reply:"
- "registerBuiltinApplicationWithInstallationRecord:extensionInstallationRecords:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:"
- "registerBuiltinStandaloneExtension:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:"
- "registerBundleNodeReinitializingContext:inBundleContainer:installDictionary:personasWithAttributes:error:"
- "registerBundleRecord:error:"
- "registerChildItemsTrusted"
- "registerContainerURL:completionHandler:"
- "registerContainerizedApplicationWithInfoDictionaries:operationUUID:requestContext:saveObserver:registrationError:"
- "registerContainerizedApplicationWithInfoDictionaries:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:"
- "registerContainerizedApplicationWithInstallationRecord:extensionInstallationRecords:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:"
- "registerExtensionPoint:platform:declaringURL:withInfo:completionHandler:"
- "registerItemInfo:alias:diskImageAlias:bundleURL:installationPlist:completionHandler:"
- "registerNonBundledExtensionPointWithIdentifier:platform:SDKDict:url:error:"
- "registerPlugin:"
- "registerPluginNodeReinitializingContext:installDictionary:existingPlugin:error:"
- "registerQueriableSchemes:bundleData:"
- "registeredDate"
- "registrationDateWithContext:tableID:unitID:unitBytes:"
- "registrationStatePreconditionForBundleWithIdentifier:placeholderInstalled:fullApplicationInstalled:"
- "regularExpressionWithPattern:options:error:"
- "regularFile"
- "regulatoryPrivacyDisclosureVersion"
- "regulatoryPrivacyDisclosureVersionWithContext:tableID:unitID:unitBytes:"
- "relativePathToFullPath:fromBasePath:"
- "relativeString"
- "relaxApplicationTypeRequirements:forApplicationRecord:completionHandler:"
- "relaxApplicationTypeRequirements:forBundleIdentifier:completionHandler:"
- "release"
- "releaseObservedDatabase4WebKit"
- "remoteObjectProxyWithErrorHandler:"
- "remoteObserver"
- "remotePlaceholderEnumerator"
- "removableByInstallMachinery"
- "removeAllCachedResourceValues"
- "removeAllCachedUsageValues"
- "removeAllDefaultApplicationPreferencesWithCompletionHandler:"
- "removeAllHandlerPrefsForBundleID:completionHandler:"
- "removeAllHandlersWithCompletionHandler:"
- "removeAllObjects"
- "removeAllOverrideBlocks"
- "removeAllSettingsReturningError:"
- "removeAppWithReply:"
- "removeApplication:"
- "removeCachedResourceValueForKey:"
- "removeChangeObserver:"
- "removeDatabaseChangeObserver4WebKit:"
- "removeDatabaseStoreOnNextOpportunity:"
- "removeDeviceIdentifierForVendorName:bundleIdentifier:"
- "removeEntriesForBundleIdentifier:"
- "removeHandlerForContentType:roles:completionHandler:"
- "removeHandlerForURLScheme:completionHandler:"
- "removeItemAtURL:error:"
- "removeJournalAfterNotificationFence"
- "removeJournalFile"
- "removeLastObject"
- "removeLocalObserver:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObjectIdenticalTo:"
- "removeObjectsForKeys:serviceSpecifier:error:"
- "removeObjectsForKeys:serviceType:error:"
- "removeObjectsInRange:"
- "removeObserver"
- "removeObserver:"
- "removeObserver:forKeyPath:"
- "removeProgressForBundleID:"
- "removeSettingsReturningError:"
- "removeSubscriberForPublishingKey:andBundleID:"
- "removeableSystemApp"
- "removedSystemApp"
- "removedSystemAppBundleIDs"
- "removedSystemApplications"
- "renamed"
- "replaceCharactersInRange:withCharacters:length:"
- "replaceObjectAtIndex:withObject:"
- "replacementObjectForCoder:"
- "replacementObjectForKeyedArchiver:"
- "replacementObjectForXPCConnection:encoder:object:"
- "requestLSDExitSafely:completionHandler:"
- "requestPoliciesForBundleIdentifiers:completionHandler:"
- "requestPoliciesForBundleIdentifiers:withError:"
- "requireOpenInPlace"
- "requiredDeviceCapabilities"
- "requiredDeviceCapabilitiesWithContext:tableID:unitID:unitBytes:"
- "requiresNativeExecution"
- "requiresPostProcessing"
- "resetPlatformFlag"
- "resetSchemeQueryLimitForApplicationWithIdentifier:"
- "resetServerStoreWithCompletionHandler:"
- "resetUserElectionsWithError:"
- "resetUserElectionsWithReply:"
- "resolvable"
- "resolveAllPropertiesAndDetachOnQueue:"
- "resolveAllPropertiesOfRecords:andDetachOnQueue:"
- "resolveAllPropertiesOfRecords:count:andDetachOnQueue:"
- "resolveExpensiveQueryRemotelyUsingResolver:error:"
- "resolveExpensiveRemoteQueriesInSet:XPCConnection:error:"
- "resolveQueries:error:"
- "resolveQueries:legacySPI:completionHandler:"
- "resolveWhatWeCanLocallyWithQueries:XPCConnection:error:"
- "resolvedDomainUID"
- "resolvedNodeWithFlags:error:"
- "resourceValueClassesWithNull"
- "resourceValuesForKeys:error:"
- "respondsToSelector:"
- "restoreInactiveInstalls"
- "restoreSystemApplication:"
- "restricted"
- "restrictedAppBundleIDsExcludingRemovedSystemApps"
- "restrictedBundleIDs"
- "restrictionReason"
- "restrictionReasonWithStateProvider:"
- "result"
- "resume"
- "retain"
- "retainCount"
- "reverseObjectEnumerator"
- "revertContainerizedApplicationWithIdentifier:options:error:progressBlock:"
- "revertContainerizedApplicationWithIdentifier:options:returningRecordPromise:error:progressBlock:"
- "role"
- "roleWithContext:tableID:unitID:unitBytes:"
- "rootVolumeNode"
- "runPostProcessingForBundleID:success:isSystemApp:isPlaceholder:registeredBothFullAppAndPlaceholder:notificationJournaller:"
- "runSyncBlockInWriteContext:"
- "runWithCompletion:"
- "runsIndependentlyOfCompanionApp"
- "sandboxEnvironmentVariables"
- "sanitizeString:"
- "save"
- "saveDidHappen:error:"
- "saveProportions"
- "scanForApplicationStateChangesFromRank:toRank:exceptions:"
- "scanForApplicationStateChangesWithAllowlist:"
- "scanForAppsInRatingRankExceptionsList:"
- "scanForForDeletableSystemApps"
- "schemeQueryLimit"
- "schemeTypeOfScheme:"
- "sdkEntry"
- "secondCategoryType"
- "securePreferencesFileURL"
- "securedSystemContent"
- "seedCryptexContentIfNeeded:"
- "selector"
- "self"
- "sendApplicationStateChangedNotificationsFor:stateProvider:completion:"
- "sendDatabaseRebuiltNotification"
- "sendDatabaseRebuiltNotificationToObserver:"
- "sendExtensionNotificationsForExtensionBundleIdentifier:changingRestrictionStateTo:"
- "sendExtensionNotificationsForSystemModeChangeFrom:to:"
- "sendMessage:"
- "sendNetworkUsageChangedNotification"
- "sendNotification:ForPlugins:"
- "sendNotification:forAppProxies:Plugins:completion:"
- "sendNotification:forApplicationWithBundleIdentifier:completion:"
- "sendNotification:forApplications:withPlugins:"
- "sendNotification:forApps:withPlugins:"
- "sendNotification:forApps:withPlugins:completion:"
- "sendNotification:forApps:withPlugins:options:"
- "sendNotificationOfType:forApplicationWithBundleIdentifier:requestContext:error:"
- "sendPluginNotificationsFor:notification:"
- "sensitiveDataProxy"
- "sensitiveDataProxyWithContext:tableID:unitID:unitBytes:"
- "separatorForTitle:separator:"
- "serializedPlaceholderPath"
- "serializedPlaceholderURL"
- "serializedPlaceholderURLWithContext:tableID:unitID:unitBytes:"
- "server"
- "serviceDetailsWithServiceSpecifier:URLComponents:limit:auditToken:error:"
- "serviceDetailsWithServiceSpecifier:URLComponents:limit:error:"
- "serviceDetailsWithServiceSpecifier:error:"
- "serviceNameForConnectionType:"
- "serviceNameForConnectionType:lightweightSystemService:"
- "serviceRecords"
- "serviceSelectorRequiresDatabaseContext:"
- "serviceSettingsWithServiceSpecifier:error:"
- "serviceSpecifier"
- "serviceSpecifiersWithEntitlementValue:serviceType:error:"
- "serviceWithDefaultShellEndpoint"
- "serviceWithEndpoint:"
- "sessionKey"
- "set"
- "setAction:"
- "setActivationRecordOverride:"
- "setActivationRecordOverrideNil"
- "setAddClaimRecordIfMissing:"
- "setAllowNoneHandlerRank:"
- "setAllowURLOverrides:"
- "setAllowWildcardClaims:"
- "setAlternateIconName:completionHandler:"
- "setAlternateIconName:forIdentifier:iconsDictionary:reply:"
- "setAlternateIconName:withResult:"
- "setAlternateIconNameForCurrentApplication:completionHandler:"
- "setAlternateIconNameSilently:completionHandler:"
- "setAppObserverSelector:"
- "setApplicationIdentifier:"
- "setApplications:"
- "setArray:"
- "setAttributes:ofItemAtPath:error:"
- "setAuditToken:"
- "setBlockingIsForManualRebuild:"
- "setBrowserSettings:"
- "setBrowserSettings:error:"
- "setBrowserState:"
- "setBundleClass:"
- "setBundleClassMask:"
- "setBundleIdentifier:"
- "setByAddingObject:"
- "setByAddingObjectsFromArray:"
- "setCallCompletionHandlerWhenFullyComplete:"
- "setCallbackType:"
- "setCancellable:"
- "setCancellationHandler:"
- "setClass:forSelector:argumentIndex:ofReply:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setClickAttribution:"
- "setClientXPCConnection:"
- "setCommonInfoPlistKeysFromDictionary:"
- "setCompletedUnitCount:"
- "setConfiguration:"
- "setConnection:"
- "setDatabase:"
- "setDatabaseIsSeeded:completionHandler:"
- "setDefaultApplicationForCategory:toApplicationRecord:completionHandler:"
- "setDefaultHandlerForTypeRecord:toApplicationRecord:completionHandler:"
- "setDefaultMailClientToApplicationRecord:completionHandler:"
- "setDefaultURLHandlerForScheme:to:completion:"
- "setDefaultWebBrowserToApplicationRecord:completionHandler:"
- "setDelegate:"
- "setDestURL:"
- "setEffectiveSettings:"
- "setElidesEmptyValues:"
- "setEnabled:"
- "setEnabled:error:"
- "setEntry:forApplication:category:"
- "setError:"
- "setErrorHandler:"
- "setExportedInterface:"
- "setExportedObject:"
- "setExtendedAttribute:name:options:error:"
- "setExtensionPointRecordForCurrentProcess:"
- "setFeatureFlagOverride:"
- "setFilter:"
- "setFinderInfo:error:"
- "setFlagsFromDictionary:"
- "setFragment:"
- "setFrontBoardOptions:"
- "setFunctions:forTable:"
- "setGetDescription:"
- "setGetSummary:"
- "setHFSType:creator:"
- "setHFSTypesUnavailable"
- "setHandler:version:forURLScheme:completionHandler:"
- "setHandler:version:roles:forContentType:completionHandler:"
- "setHasServer:"
- "setHiddenApplications:completion:"
- "setHonorPreferenceForNoHandler:"
- "setHost:"
- "setIgnoreAppLinkEnabledProperty:"
- "setIgnoreOpenStrategy:"
- "setIgnoreStrongBindingPreferences:"
- "setIgnoreWeakBindingPreferences:"
- "setIncludeLinksForCallingApplication:"
- "setInsertsNewlines:"
- "setInstallPhase:"
- "setInstallState:"
- "setInterface:forSelector:argumentIndex:ofReply:"
- "setInternalQueue:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setLastFiredDate:"
- "setLaunchOptions:"
- "setLegacy:"
- "setLightweightSystemServer:"
- "setLimit:"
- "setListener:"
- "setLockedApplications:completion:"
- "setMachOUUIDs:"
- "setMaximumHandlerRank:"
- "setMinimumHandlerRank:"
- "setName:"
- "setObject:atIndexedSubscript:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setObjectValue:forSelector:"
- "setObservinglsd:"
- "setOpenConfiguration:"
- "setOpenStrategy:"
- "setParentApplicationRecord:"
- "setPasteSharingToken:"
- "setPath:"
- "setPausable:"
- "setPersonaUniqueStrings:forApplicationWithBundleIdentifier:operationUUID:requestContext:saveObserver:error:"
- "setPersonaUniqueStrings:forApplicationsWithBundleIdentifiers:operationUUID:requestContext:saveObserver:error:"
- "setPluginsByBundleIentifier:"
- "setPredicate:"
- "setPreferenceForNoHandlerForCategory:completionHandler:"
- "setPreferenceValue:forKey:forApplicationAtURL:completionHandler:"
- "setPreferenceValueForCallingApplication:forKey:completionHandler:"
- "setPreferredAppMarketplaces:completion:"
- "setPreferredAppMarketplaces:error:"
- "setPreferredLocalizationsForXCTests:"
- "setPreferredMarketplaces:"
- "setPreviousInstallType:"
- "setPrimaryBundleID:"
- "setPrioritizable:"
- "setProfileValidationState:"
- "setProgress:forBundleID:"
- "setProgressProportionsByPhase:forInstallOfApplicationWithIdentifier:completion:"
- "setProgressProportionsByPhase:forInstallOfApplicationWithIdentifier:error:"
- "setPropertyListCachingStrategy:"
- "setQuery:"
- "setQueryItems:"
- "setQueue:"
- "setRaritiesFromDictionary:"
- "setReferrerURL:"
- "setReferringAliasNode:"
- "setRegistrationInfo:alias:"
- "setRemoteObjectInterface:"
- "setRequireOpenInPlace:"
- "setResourceValue:forKey:"
- "setResourceValue:forKey:error:"
- "setResourceValue:forKey:options:error:"
- "setResourceValues:error:"
- "setResourcesDirectoryURL:"
- "setResult:"
- "setRetries:"
- "setSDKVersion:"
- "setScheme:"
- "setSeedingComplete:"
- "setSensitive:"
- "setSequenceNumber:"
- "setServer:"
- "setServerDatabase:"
- "setServiceDetails:"
- "setSettingsSwitchState:forApplicationIdentifier:error:"
- "setShouldSetHandlerOnDocumentOpen:"
- "setShowAllExtensions:"
- "setSimulateLimitedMappingForXCTests:"
- "setState:"
- "setSuffixForRemoteXCTests:"
- "setTarget:"
- "setTargetApplicationRecord:"
- "setTargetConnectionEndpoint:"
- "setTargetServiceConnectionEndpoint:"
- "setTargetUserID:"
- "setTemporaryResourceValue:forKey:"
- "setTimer:"
- "setTotalUnitCount:"
- "setTrustedCodeSigningIdentities:"
- "setURL:"
- "setURLComponents:"
- "setUnitDescriptionPredicate:"
- "setUpdateAvailabilities:completionHandler:"
- "setUpdateAvailability:completionHandler:"
- "setUpdateAvailabilityForApplicationsWithBundleIdentifiers:completionHandler:"
- "setUseMacOverrides:"
- "setUseOneTapOpenBehavior:"
- "setUserElection:forExtensionKey:error:"
- "setUserElection:forExtensionKey:reply:"
- "setUserInfoObject:forKey:"
- "setUserInitiatedUninstall:"
- "setUuid:"
- "setValue:forKey:"
- "setVersion:"
- "setVisualizer:"
- "setWebpageURL:"
- "setWithArray:"
- "setWithCapacity:"
- "setWithObject:"
- "setWithObjects:"
- "setXPCConnection:"
- "setYieldClaimBindings:"
- "set_universalLink:"
- "settingsStoreConfigurationForProcessWithAuditToken:"
- "settingsStoreFileURL"
- "settingsSwitchStateForApplicationIdentifier:"
- "settingsUpdateNotificationNameForUserID:"
- "sharedCachingEligibilityPredicateEvaluator"
- "sharedConnection"
- "sharedDatabaseContext"
- "sharedInstance"
- "sharedManager"
- "sharedNotification"
- "sharedServerInstance"
- "sharedUsage"
- "shortDisplayName"
- "shortVersionString"
- "shortVersionStringWithContext:tableID:unitID:unitBytes:"
- "shouldEnforceTrackingWithReasonCode:"
- "shouldExpectEntityToExist"
- "shouldJournalNotificationType:"
- "shouldShowSecurityPromptsOnSignIn"
- "shouldSkipWatchAppInstall"
- "showAllExtensions"
- "showExtensionWithContextIfNeeded:asIfShowingAllExtensions:"
- "showIconChangeAlertForApplicationWithIdentity:completion:"
- "sideFault"
- "sideFaultResourceValuesWithError:"
- "signatureVersion"
- "signerIdentity"
- "signerIdentityWithContext:tableID:unitID:unitBytes:"
- "signerOrganizationWithContext:tableID:unitID:unitBytes:"
- "simulateLimitedMappingForXCTests"
- "simulatorRootURL"
- "simulatorRuntimeBuildVersion"
- "simulatorRuntimeVersion"
- "siriActionDefinitionURLs"
- "sliceValue"
- "sort:pluginIDs:andYield:context:"
- "sortUsingComparator:"
- "sortUsingSelector:"
- "sortedArrayUsingSelector:"
- "sourceAppIdentifier"
- "sourceIsManaged"
- "specialAppEligibilityStateURL"
- "spotlightActions"
- "springBoardDeadlockPreventionQueue"
- "springBoardQueue"
- "stagingDirectoryForCloningFileHandle:error:"
- "stagingDirectoryForCloningURL:error:"
- "stagingDirectoryInfoForPersonaUniqueString:error:"
- "stagingDirectoryKeyForFileHandle:error:"
- "stagingDirectoryKeyForNode:error:"
- "standaloneWatchApp"
- "standardUserDefaults"
- "start"
- "startAccessingCurrentUserSessionReturningError:"
- "startAccessingReturningError:"
- "startAccessingSystemScopeReturningError:"
- "startAccessingWithOptions:error:"
- "startAccessingWithUserID:error:"
- "startAccessingWithUserID:options:error:"
- "startObserving"
- "startPlugins"
- "startRunningIfNecessary"
- "stashedAppInfo"
- "stashedAppMetadata"
- "stashedAppMetadataWithContext:tableID:unitID:unitBytes:"
- "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /Library/Caches/com.apple.xbs/CF4B8982-1BF8-4E04-99AB-9E38C33AD534/TemporaryDirectory.PH9c0s/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1433:63)]"
- "staticDiskUsage"
- "staticShortcutItems"
- "staticShortcutItemsWithContext:tableID:unitID:unitBytes:"
- "staticUsage"
- "stopAccessing"
- "stopObserving"
- "stopTimer"
- "storeCohortMetadata"
- "storeCohortWithError:"
- "storefront"
- "string"
- "stringByAppendingFormat:"
- "stringByAppendingPathComponent:"
- "stringByAppendingPathExtension:"
- "stringByAppendingPathExtensionForType:"
- "stringByAppendingString:"
- "stringByDeletingLastPathComponent"
- "stringByDeletingPathExtension"
- "stringByReplacingCharactersInRange:withString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringForKey:"
- "stringValue"
- "stringValueWithPreferredLocalizations:"
- "stringWithCapacity:"
- "stringWithCharacters:length:"
- "stringWithFileSystemRepresentation:length:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "strongObjectsPointerArray"
- "strongToStrongObjectsMapTable"
- "subarrayWithRange:"
- "subscriberForBundleID:andPublishingKey:"
- "substringFromIndex:"
- "substringToIndex:"
- "substringWithRange:"
- "suffixForRemoteXCTests"
- "superclass"
- "supportedComplicationFamilies"
- "supportedDefaultAppCategories"
- "supportedGameControllers"
- "supportedGameControllersWithContext:tableID:unitID:unitBytes:"
- "supportedIntentMediaCategories"
- "supportedIntents"
- "supportedLiveActivityLaunchAttributeTypes"
- "supportsAlternateIconNames"
- "supportsAlwaysOnDisplay"
- "supportsAudiobooks"
- "supportsCarPlayDashboardScene"
- "supportsCarPlayInstrumentClusterScene"
- "supportsControllerUserInteraction"
- "supportsDataExport"
- "supportsExternallyPlayableContent"
- "supportsGameMode"
- "supportsLiveActivities"
- "supportsLiveActivitiesFrequentUpdates"
- "supportsMultiwindow"
- "supportsNowPlaying"
- "supportsODR"
- "supportsOnDemandResources"
- "supportsOpenInPlace"
- "supportsPurgeableLocalStorage"
- "supportsSecureCoding"
- "supportsSessions"
- "supportsSpotlightQueryContinuation"
- "swiftPlaygroundsApp"
- "swift_firstWhere:"
- "swift_forEach:"
- "symbolicLink"
- "syncObserverProxy"
- "syncWithMI:"
- "synchronizeWithMobileInstallation"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "synthesizedPreliminaryJournalledNotifications"
- "systemContainerBaseURL"
- "systemContainerURL"
- "systemContentDatabaseStoreFileURL"
- "systemContentDatabaseStoreFileURLWithUID:"
- "systemDataVolumeNode"
- "systemGroupContainerURL"
- "systemMode"
- "systemPlaceholder"
- "systemPlaceholderEnumerator"
- "systemServer"
- "tagSpecification"
- "tagSpecificationWithContext:tableID:unitID:unitBytes:"
- "targetServiceConnectionEndpoint"
- "targetUserID"
- "teamIdentifier"
- "teamIdentifierWithContext:tableID:unitID:unitBytes:"
- "temporaryDirectory"
- "temporaryDirectoryNodeWithFlags:error:"
- "timeIntervalSince1970"
- "timeIntervalSinceDate:"
- "timeIntervalSinceReferenceDate"
- "timer"
- "timestamp"
- "toPlist"
- "transformBeforeCombining:needsBiDiControlCharacters:"
- "triggerRegistrationForContainerizedContentWithOptions:completion:"
- "truncate:queriableSchemesIfNeeded:"
- "trustedCDHashes"
- "trustedCodeSigningIdentities"
- "trustedForBinding"
- "typeForInstallMachinery"
- "typeForInstallMachineryWithContext:tableID:unitID:unitBytes:"
- "typeIdentifiers"
- "typeIdentifiersWithContext:tableID:unitID:unitBytes:"
- "typeRecordForImportedTypeWithIdentifier:conformingToIdentifier:"
- "typeRecordForPromiseAtURL:error:"
- "typeRecordWithError:"
- "typeRecordWithIdentifier:"
- "typeRecordWithPotentiallyUndeclaredIdentifier:"
- "typeRecordWithTag:ofClass:"
- "typeRecordWithTag:ofClass:conformingToIdentifier:"
- "typeRecordWithTag:ofClass:conformingToTypeRecord:"
- "typeRecordsWithIdentifiers:"
- "typeRecordsWithTag:ofClass:"
- "typeRecordsWithTag:ofClass:conformingToIdentifier:"
- "typeRecordsWithTag:ofClass:conformingToTypeRecord:"
- "typeWithIdentifier:"
- "uid"
- "unable to locate user container: error %llu"
- "unarchivedObjectOfClass:fromData:error:"
- "unarchivedObjectOfClasses:fromData:error:"
- "uncheckedObjectsForKeys:"
- "uninstallApplication:withOptions:"
- "uninstallApplication:withOptions:error:usingBlock:"
- "uninstallApplication:withOptions:uninstallType:reply:"
- "uninstallApplication:withOptions:usingBlock:"
- "uninstallContainerizedApplicationWithIdentifier:options:error:progressBlock:"
- "unionSet:"
- "uniqueIdentifierWithContext:tableID:unitID:unitBytes:"
- "uniqueInstallIdentifier"
- "uniqueInstallIdentifierWithContext:tableID:unitID:unitBytes:"
- "unlocalizedNameWithContext:"
- "unlocalizedNameWithContext:asIfShowingAllExtensions:"
- "unlocalizedNameWithContextIfNeeded:"
- "unlocalizedNameWithContextIfNeeded:asIfShowingAllExtensions:"
- "unlocalizedNamesWithContext"
- "unlock"
- "unredactWithError:"
- "unregisterApplication:"
- "unregisterApplicationAtURL:operationUUID:reply:"
- "unregisterApplicationBundleByUnit:error:"
- "unregisterApplicationWithBundleIdentifier:type:error:"
- "unregisterApplicationsAtMountPoint:operationUUID:reply:"
- "unregisterApplicationsAtMountPoint:operationUUID:saveObserver:requestContext:"
- "unregisterBuiltinApplicationAtURL:operationUUID:requestContext:saveObserver:error:"
- "unregisterBuiltinStandaloneExtensionAtURL:operationUUID:requestContext:saveObserver:error:"
- "unregisterBundleUnit:options:completionHandler:"
- "unregisterContainerizedApplicationWithBundleIdentifier:operationUUID:unregistrationOperation:precondition:requestContext:saveObserver:unregistrationError:"
- "unregisterContainerizedApplicationWithBundleIdentifier:operationUUID:unregistrationOperation:requestContext:saveObserver:unregistrationError:"
- "unregisterExtensionPoint:platform:withVersion:parentBundleUnit:completionHandler:"
- "unregisterNonBundledExtensionPointWithIdentifier:error:"
- "unregisterPlugin:"
- "unregisterPluginAtURL:operationUUID:reply:"
- "unregisterPluginBundleByUnit:error:"
- "unremappableDatabaseStoreFileURL"
- "unrestrictedApplications"
- "unsignedCharValue"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "unsignedLongValue"
- "update"
- "updateAvailability"
- "updateBundleRecord:"
- "updateContainerUnit:completionHandler:"
- "updatePlaceholderMetadataForApp:installType:failure:underlyingError:source:outError:"
- "updatePlaceholderMetadataForApplicationWithIdentifier:operationUUID:requestContext:installType:failure:saveObserver:error:"
- "updatePlaceholderWithBundleIdentifier:withInstallType:error:"
- "updateRecordForApp:withSINF:iTunesMetadata:placeholderMetadata:sendNotification:operationUUID:outSaveToken:error:"
- "updateRecordForApp:withSINF:iTunesMetadata:placeholderMetadata:sendNotification:operationUUID:returnSaveToken:completionHandler:"
- "updateRestrictionKnowledgeWithCompletionHandler:"
- "updateSINFMetadataForApplicationWithIdentifier:operationUUID:requestContext:parsedSINFInfo:saveObserver:error:"
- "updateSINFWithData:forApplication:options:error:"
- "updateSINFWithData:forApplicationAtURL:error:"
- "updatedEntryRotatingInWindowOpenDate:refreshDate:defaultForCategory:"
- "updatedEntryWithRefreshDate:defaultForCategory:"
- "updateiTunesMetadataForApplicationWithIdentifier:operationUUID:requestContext:metadataPlist:saveObserver:error:"
- "updateiTunesMetadataWithData:forApplication:options:error:"
- "updateiTunesMetadataWithData:forApplicationAtURL:error:"
- "urlContainsDeviceIdentifierForAdvertising:"
- "urlContainsDeviceIdentifierForAdvertising:completionHandler:"
- "usageFromMobileInstallationForBundleIdentifier:error:"
- "useLegacyLocalizationListForPlatform:sdkVersion:"
- "userActivityTypes"
- "userActivityTypesWithContext:tableID:unitID:unitBytes:"
- "userContainerURL"
- "userDataVolumeNode"
- "userElectionForExtensionKey:"
- "userElectionForExtensionKey:reply:"
- "userInfo"
- "userInitiatedUninstall"
- "userPersonaBundleIDList"
- "userPersonaType"
- "userPersonaUniqueString"
- "userPreferencesURL"
- "userServer"
- "usingCachedItem"
- "usingEphemeralStorage"
- "v16@0:8"
- "v16@?0@\"FBSDisplayLayout\"8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v20@0:8I16"
- "v20@0:8i16"
- "v24@0:8:16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSOperation\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"<EXExtensionPoint>\"^B>16"
- "v24@0:8@?<v@?@\"<LSRegistrantDatabaseContextProviding>\">16"
- "v24@0:8@?<v@?@\"LSBundleProxy\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"LSBundleRecord\">16"
- "v24@0:8@?<v@?@\"LSBundleRecord\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"LSExtensionPointRecord\">16"
- "v24@0:8@?<v@?@\"LSExtensionPointRecord\"^B>16"
- "v24@0:8@?<v@?@\"LSSettingsStoreConfiguration\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSArray\">16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSSet\">16"
- "v24@0:8@?<v@?@\"NSSet\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSSet\"@\"NSSet\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSString\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSUUID\"@\"NSNumber\">16"
- "v24@0:8@?<v@?@@\"FSNode\"@\"NSError\">16"
- "v24@0:8@?<v@?@@\"FSNode\"@\"NSXPCListenerEndpoint\"B@\"NSError\">16"
- "v24@0:8@?<v@?B@\"<LSRegistrantDatabaseContext>\"@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8@?<v@?I>16"
- "v24@0:8I16I20"
- "v24@0:8Q16"
- "v24@0:8^B16"
- "v24@0:8^v16"
- "v24@0:8^{sqlite3=}16"
- "v24@0:8q16"
- "v24@0:8r^{?=[8I]}16"
- "v28@0:8@16B24"
- "v28@0:8@16C24"
- "v28@0:8@16I24"
- "v28@0:8B16@20"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?B@\"NSError\">20"
- "v28@0:8I16@?20"
- "v28@0:8I16@?<v@?@\"NSData\"@\"NSError\">20"
- "v28@?0@\"NSString\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20"
- "v28@?0@\"NSString\"8I16r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20"
- "v28@?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20"
- "v32@0:8@\"LSDocumentProxy\"16@?<v@?@\"_LSBoundIconInfo\"@\"NSError\">24"
- "v32@0:8@\"LSInstallProgressObserver\"16@\"_LSInstallProgressService\"24"
- "v32@0:8@\"NSArray\"16@\"NSArray\"24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSOperation\"16@\"NSError\"24"
- "v32@0:8@\"NSOperation\"16@\"NSURL\"24"
- "v32@0:8@\"NSSet\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@\"NSSet\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSXPCListenerEndpoint\">24"
- "v32@0:8@\"NSString\"16@?<v@?B>24"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?C@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?q@\"NSError\">24"
- "v32@0:8@\"NSString\"16Q24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSURL\"@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?I@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"<_LSPendingSaveToken>\"@\"NSError\">24"
- "v32@0:8@\"_LSDiskUsage\"16@?<v@?@\"_LSDiskUsage\"@\"NSError\">24"
- "v32@0:8@16:24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8@?16@?24"
- "v32@0:8I16I20@?24"
- "v32@0:8I16I20@?<v@?B@\"NSError\">24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?@\"LSDefaultApplicationQueryResult\"@\"NSError\">24"
- "v32@0:8Q16@?<v@?@\"NSNumber\"@\"NSError\">24"
- "v32@0:8^@16^@24"
- "v32@0:8d16@?24"
- "v32@0:8d16@?<v@?B@\"NSError\">24"
- "v32@0:8i16@\"NSArray\"20B28"
- "v32@0:8i16@20B28"
- "v32@0:8q16@?24"
- "v32@0:8q16@?<v@?@\"NSUUID\">24"
- "v32@?0@\"NSDictionary\"8Q16^B24"
- "v32@?0@\"NSNumber\"8@16^B24"
- "v36@0:8@\"NSSet\"16B24@?<v@?@\"NSDictionary\"@\"NSError\">28"
- "v36@0:8@\"NSString\"16B24@?<v@?@\"UTTypeRecord\">28"
- "v36@0:8@\"NSString\"16I24@?<v@?@\"LSExtensionPointRecord\"@\"NSError\">28"
- "v36@0:8@\"NSString\"16I24@?<v@?B@\"NSError\">28"
- "v36@0:8@16@24B32"
- "v36@0:8@16B24@?28"
- "v36@0:8@16C24d28"
- "v36@0:8@16I24@?28"
- "v36@0:8B16@\"NSString\"20@?<v@?B@\"NSError\">28"
- "v36@0:8B16@20@?28"
- "v36@0:8B16B20B24@?28"
- "v36@0:8B16B20B24@?<v@?B@\"NSError\">28"
- "v36@0:8C16@\"NSString\"20@?<v@?@\"NSError\">28"
- "v36@0:8C16@20@?28"
- "v36@0:8I16Q20@?28"
- "v36@0:8Q16B24@?28"
- "v36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
- "v36@0:8i16@\"NSString\"20@?<v@?@\"NSError\">28"
- "v36@0:8i16@20@28"
- "v36@0:8i16@20@?28"
- "v40@0:8@\"LSAppLink\"16@\"_LSAppLinkOpenState\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"LSDefaultApplicationQueryEntry\"16@\"LSApplicationRecord\"24Q32"
- "v40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSDictionary\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSDictionary\"16@\"NSUUID\"24@?<v@?@\"<_LSPendingSaveToken>\"@\"NSError\">32"
- "v40@0:8@\"NSSet\"16@\"NSSet\"24@?<v@?@\"NSArray\"@\"NSArray\"@\"NSError\">32"
- "v40@0:8@\"NSSet\"16Q24@\"LSRatingRankEligibilityMonitor\"32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"UTTypeRecord\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?B>32"
- "v40@0:8@\"NSString\"16@\"NSURL\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSString\"16q24@?<v@?@\"NSArray\"@\"NSArray\"@\"NSError\">32"
- "v40@0:8@\"NSURL\"16@\"NSUUID\"24@?<v@?@\"<_LSPendingSaveToken>\"@\"NSError\">32"
- "v40@0:8@\"NSURL\"16B24B28@?<v@?B@\"NSError\">32"
- "v40@0:8@\"_LSQuery\"16@\"NSXPCConnection\"24@?<v@?@\"_LSQueryResult\"@\"NSError\"^B>32"
- "v40@0:8@16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@24Q32"
- "v40@0:8@16@?24@?32"
- "v40@0:8@16B24B28@?32"
- "v40@0:8@16Q24@32"
- "v40@0:8@16Q24@?32"
- "v40@0:8@16^B24^B32"
- "v40@0:8@16q24@?32"
- "v40@0:8Q16@24@?32"
- "v40@0:8^@16^@24[2B]32"
- "v40@0:8^@16^@24^@32"
- "v40@0:8^@16^@24^B32"
- "v40@0:8^{LSContext=@}16@24@?32"
- "v40@0:8^{LSContext=@}16I24I28r^v32"
- "v40@0:8^{__CFBundle=}16@24I32B36"
- "v40@0:8i16@20B28@32"
- "v40@0:8i16@20B28@?32"
- "v40@0:8r^@16Q24@32"
- "v40@0:8r^v16^{LSContext=@}24@?32"
- "v44@0:8@\"NSString\"16@\"NSDictionary\"24B32@?<v@?B@\"NSError\">36"
- "v44@0:8@16@24B32@?36"
- "v44@0:8@16@24I32B36B40"
- "v44@0:8B16@20@?28^{LSContext=@}36"
- "v44@0:8B16q20@28@?36"
- "v44@0:8^{Context=^{LSContext}{LSContext=@}B@}16@24B32r^I36"
- "v44@0:8^{LSContext=@}16I24q28@?36"
- "v44@0:8^{_NSRange=QQ}16^{_NSRange=QQ}24@32B40"
- "v44@0:8^{__CFBundle=}16@24I32B36B40"
- "v48@0:8@\"LSApplicationProxy\"16Q24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSArray\"16@\"NSArray\"24@\"NSUUID\"32@?<v@?@\"<_LSPendingSaveToken>\"@\"NSError\">40"
- "v48@0:8@\"NSArray\"16@\"NSArray\"24@\"NSUUID\"32@?<v@?@\"LSRecordPromise\"@\"<_LSPendingSaveToken>\"@\"NSError\">40"
- "v48@0:8@\"NSSet\"16@\"FSMimic\"24@\"NSArray\"32@?<v@?@\"NSDictionary\"@\"NSSet\"@\"NSError\">40"
- "v48@0:8@\"NSSet\"16@\"NSSet\"24@\"NSUUID\"32@?<v@?@\"<_LSPendingSaveToken>\"@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSDictionary\"24Q32@?<v@?@\"NSArray\"@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?B@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSArray\">40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"UTTypeRecord\">40"
- "v48@0:8@\"NSString\"16I24@\"NSString\"28I36@?<v@?B@\"NSError\">40"
- "v48@0:8@\"NSURL\"16@\"NSFileHandle\"24@\"NSDictionary\"32@?<v@?B@\"NSError\">40"
- "v48@0:8@16@\"NSString\"24@\"NSURL\"32@?<v@?B@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24@32^v40"
- "v48@0:8@16@24Q32@?40"
- "v48@0:8@16B24B28B32B36@40"
- "v48@0:8@16I24@28I36@?40"
- "v48@0:8@16Q24@32@?40"
- "v48@0:8@16^{__CFString=}24@32@40"
- "v48@0:8q16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSUUID\">40"
- "v48@0:8q16@24@32@?40"
- "v52@0:8@\"NSString\"16@\"NSUUID\"24I32@\"LSPrecondition\"36@?<v@?@\"<_LSPendingSaveToken>\"@\"NSError\">44"
- "v52@0:8@\"NSString\"16I24@\"NSURL\"28@\"NSDictionary\"36@?<v@?B@\"NSError\">44"
- "v52@0:8@\"NSUUID\"16@\"FSNode\"24@\"NSString\"32I40@?<v@?@\"LSApplicationExtensionRecord\"@\"NSError\">44"
- "v52@0:8@\"NSUUID\"16@\"FSNode\"24@\"NSString\"32I40@?<v@?@\"LSPlugInKitProxy\"@\"NSError\">44"
- "v52@0:8@16@24@32B40@?44"
- "v52@0:8@16@24@32I40@?44"
- "v52@0:8@16@24I32@36@?44"
- "v52@0:8@16I24@28@36@?44"
- "v52@0:8B16q20@28@36@?44"
- "v56@0:8@\"NSString\"16@\"NSURL\"24@\"NSDictionary\"32Q40@?<v@?@\"NSArray\"@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16@24@32Q40@?48"
- "v56@0:8@16{LSVersionNumber=[32C]}24"
- "v56@0:8^i16^i24^i32^i40@48"
- "v64@0:8@\"LSRegistrationInfo\"16@\"NSData\"24@\"NSData\"32@\"NSURL\"40@\"NSDictionary\"48@?<v@?BI@\"NSArray\"B@\"NSError\">56"
- "v64@0:8@\"NSUUID\"16@\"NSData\"24@\"NSString\"32@\"NSString\"40@\"NSDictionary\"48@?<v@?B@\"NSError\">56"
- "v64@0:8@16@24@32@40@48@?56"
- "v72@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSDictionary\"32@\"NSDictionary\"40i48@\"NSUUID\"52B60@?<v@?B@\"<_LSPendingSaveToken>\"@\"NSError\">64"
- "v72@0:8@\"NSString\"16{LSVersionNumber=[32C]}24@\"NSString\"56@?<v@?B@\"NSError\">64"
- "v72@0:8@16@24@32@40i48@52B60@?64"
- "v72@0:8@16{LSVersionNumber=[32C]}24@56@?64"
- "v76@0:8@\"NSString\"16{LSVersionNumber=[32C]}24I56@\"NSString\"60@?<v@?B@\"NSError\">68"
- "v76@0:8@16{LSVersionNumber=[32C]}24I56@60@?68"
- "v92@0:8@\"NSURL\"16@\"NSFileHandle\"24@\"NSString\"32@\"NSString\"40B48r^{?=[8I]}52@\"NSDictionary\"60@\"NSDictionary\"68@\"<LSOpenResourceOperationDelegate>\"76@?<v@?B@\"NSError\">84"
- "v92@0:8@16@24@32@40B48r^{?=[8I]}52@60@68@76@?84"
- "valid"
- "valueForEntitlement:"
- "valueForKey:"
- "valueForUndefinedKey:"
- "vendorIDFromVendorName:seedData:error:"
- "vendorName"
- "vendorNameForDeviceIdentifiersWithContext:bundleUnit:bundleData:"
- "versionWithContext:tableID:unitID:unitBytes:"
- "visualizer"
- "visualizerURL"
- "vocabularyType"
- "void LaunchServices::UTTypeEnumerateFlavoredDisplayNames(__strong LSDatabaseRef, const _UTTypeData *, const F &) [F = (lambda at /Library/Caches/com.apple.xbs/CF4B8982-1BF8-4E04-99AB-9E38C33AD534/TemporaryDirectory.PH9c0s/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Database/UTTypeCore.mm:159:55)]"
- "volumeNodeWithFlags:error:"
- "waitForResult:"
- "waitForSiteApprovalWithCompletionHandler:"
- "wantsEphemeralNotifications"
- "wantsHiddenExtension"
- "wantsLocationConfirmation"
- "wasBuiltWithThreadSanitizer"
- "wasGameCenterEverEnabled"
- "wasRenamed"
- "watchKitApp"
- "watchKitApplicationTintColorName"
- "watchKitApplicationType"
- "watchKitVersion"
- "watchOS"
- "watchOnly"
- "weakObjectsHashTable"
- "webApp"
- "webAppPlaceholder"
- "webBrowser"
- "webNotificationPlaceholder"
- "webpageURL"
- "whitelisted"
- "whitespaceCharacterSet"
- "willHandleInvocation:isReply:"
- "windowOpenDates"
- "withAppliedAttribute:value:block:"
- "withReferenceToUnit:unit:block:"
- "withStatsGatherer:runWithRebuildContext:"
- "withTextColor:backgroundColor:block:"
- "withTextColor:block:"
- "withWarningColors:"
- "wrapped"
- "wrapper"
- "write:"
- "write:array:"
- "write:arrayID:"
- "write:arrayIDs:count:"
- "write:arrayStringID:"
- "write:bool:"
- "write:directoryClass:"
- "write:format:"
- "write:iNode:"
- "write:interval:"
- "write:number:"
- "write:platform:"
- "write:string:"
- "write:stringID:"
- "write:version:"
- "writeAllUnitsInTable:block:"
- "writeArray:"
- "writeAttributedString:"
- "writeData:error:"
- "writeFinalJournal"
- "writeFormat:"
- "writePreliminaryJournal"
- "writeSchemesMap"
- "writeSeparator"
- "writeToDB:"
- "writeToURL:atomically:"
- "writeToURL:error:"
- "writeToURL:options:error:"
- "wrong number of items provided for registration, rejecting"
- "yieldBundles:context:block:"
- "zone"
- "{?=\"HFSTypesSet\"b1\"HFSTypesUnavailable\"b1}"
- "{?=\"allowWildcardClaims\"b1\"ignoreStrongBindingPreferences\"b1\"ignoreWeakBindingPreferences\"b1\"requireOpenInPlace\"b1\"honorPreferenceForNoHandler\"b1}"
- "{?=\"hasLookedForLoctable\"b1\"isInfoPlist\"b1}"
- "{?=\"redacted\"b1}"
- "{?=\"val\"[8I]}"
- "{?=\"wasResumed\"b1\"wasInvalidated\"b1}"
- "{BindingEvaluator=@@@@@@{LSVersionNumber=[32C]}@BBQII{vector<LSBundleClass, std::allocator<LSBundleClass>>=^I^I{?=^I}}@?@@?@@?}16@0:8"
- "{BindingEvaluator=@@@@@@{LSVersionNumber=[32C]}@BBQII{vector<LSBundleClass, std::allocator<LSBundleClass>>=^I^I{?=^I}}@?@@?@@?}24@0:8@16"
- "{BindingEvaluator=@@@@@@{LSVersionNumber=[32C]}@BBQII{vector<LSBundleClass, std::allocator<LSBundleClass>>=^I^I{?=^I}}@?@@?@@?}24@0:8r^{?=[8I]}16"
- "{BindingEvaluator=@@@@@@{LSVersionNumber=[32C]}@BBQII{vector<LSBundleClass, std::allocator<LSBundleClass>>=^I^I{?=^I}}@?@@?@@?}28@0:8C16r^{?=[8I]}20"
- "{CFReleaser<__CSStoreAccessContext *>=\"fItem\"^{__CSStoreAccessContext}}"
- "{Context=\"_contextPointer\"^{LSContext}\"_contextStorage\"{LSContext=\"db\"@\"_LSDatabase\"}\"_created\"B\"_error\"@\"NSError\"}"
- "{DelayedInitable<LaunchServices::Predicate>=\"_storage\"{optional<LaunchServices::Predicate>=\"\"(?=\"__null_state_\"c\"__val_\"{Predicate=\"_match_map\"{map<os_eligibility_domain_t, std::vector<os_eligibility_answer_t>, std::less<os_eligibility_domain_t>, std::allocator<std::pair<const os_eligibility_domain_t, std::vector<os_eligibility_answer_t>>>>=\"__tree_\"{__tree<std::__value_type<os_eligibility_domain_t, std::vector<os_eligibility_answer_t>>, std::__map_value_compare<os_eligibility_domain_t, std::pair<const os_eligibility_domain_t, std::vector<os_eligibility_answer_t>>, std::less<os_eligibility_domain_t>>, std::allocator<std::pair<const os_eligibility_domain_t, std::vector<os_eligibility_answer_t>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}})\"__engaged_\"B}}"
- "{DelayedInitable<LaunchServices::Predicate>=\"_storage\"{optional<LaunchServices::Predicate>=\"\"(?=\"__null_state_\"c\"__val_\"{Predicate=\"_requiredFeatures\"{vector<LaunchServices::FeatureFlagSpecifier, std::allocator<LaunchServices::FeatureFlagSpecifier>>=\"__begin_\"^{FeatureFlagSpecifier}\"__end_\"^{FeatureFlagSpecifier}\"\"{?=\"__cap_\"^{FeatureFlagSpecifier}}}\"_antiRequiredFeatures\"{vector<LaunchServices::FeatureFlagSpecifier, std::allocator<LaunchServices::FeatureFlagSpecifier>>=\"__begin_\"^{FeatureFlagSpecifier}\"__end_\"^{FeatureFlagSpecifier}\"\"{?=\"__cap_\"^{FeatureFlagSpecifier}}}})\"__engaged_\"B}}"
- "{LSBinding=\"bundle\"I\"bundleData\"^{LSBundleData}\"claim\"I\"claimData\"^{?}\"userInfo\"@\"reason\"@\"NSString\"\"provenance\"Q}"
- "{LSBinding=I^{LSBundleData}I^{?}@@Q}16@0:8"
- "{LSBundleBaseFlags=\"appleInternal\"b1\"requiresObjCGarbageCollection\"b1\"builtWithTSan\"b1\"isLinkEnabled\"b1\"isSecuredSystemContent\"b1\"redactable\"b1\"_reserved\"b1}"
- "{LSBundleBaseFlags=b1b1b1b1b1b1b1}16@0:8"
- "{LSBundleBaseFlags=b1b1b1b1b1b1b1}40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}32"
- "{LSBundleData=\"base\"{LSBundleBaseData=\"bookmark\"I\"container\"I\"execPath\"I\"exactIdentifier\"I\"teamID\"I\"platform\"I\"registrationTime\"i\"version\"{LSVersionNumber=\"_opaque\"[32C]}\"execSDKVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"machOUUIDs\"I\"dataContainerAlias\"I\"bundleName\"I\"localizedShortDisplayName\"I\"displayName\"I\"localizedDisplayName\"I\"contextualUsageDescriptions\"I\"codeInfoIdentifier\"I\"signerOrganization\"I\"signerIdentity\"I\"infoDictionary\"I\"entitlements\"I\"groupContainers\"I\"containingDirectoryClass\"C\"profileValidationState\"C\"intentDefinitionURLs\"I\"_sliceMask\"S\"signatureVersion\"I\"flags\"{LSBundleBaseFlags=\"appleInternal\"b1\"requiresObjCGarbageCollection\"b1\"builtWithTSan\"b1\"isLinkEnabled\"b1\"isSecuredSystemContent\"b1\"redactable\"b1\"_reserved\"b1}}\"_clas\"I\"_bundleFlags\"Q\"_plistContentFlags\"I\"_itemFlags\"I\"_iconFlags\"C\"moreFlags\"{LSBundleMoreFlags=\"isWebBrowser\"b1\"isMailClient\"b1\"supportsControllerUserInteraction\"b1\"supportsSpotlightQueryContinuation\"b1\"supportsSpotlightActions\"b1\"isCodeSigningInfoNotAuthoritative\"b1\"applicationQueriesSchemesTooBig\"b1\"isUpdateAvailable\"b1\"isPlaygroundsApp\"b1\"supportsAlwaysOnDisplay\"b1\"defaultsToPrivateAlwaysOnDisplayTreatment\"b1\"supportsLiveActivities\"b1\"supportsLiveActivitiesFrequentUpdates\"b1\"requiresPostprocessing\"b1\"hasShellRole\"b1\"requiresSecureLaunch\"b1\"eligibleForWatchAppInstall\"b1\"isEligibilityCheckedBrowser\"b1\"isEligibilityCheckedBrowserEngineEmbedder\"b1\"isManagedAppDistributor\"b1\"isHiddenByAppProtection\"b1\"isLockedByAppProtection\"b1\"supportsDataExport\"b1\"hasSupportsGameModeKey\"b1\"supportsGameMode\"b1\"isOnCryptex\"b1}\"_hfsType\"I\"_mtime\"i\"minSystemVersionPlatform\"I\"_minSystemVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"_maxSystemVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"appStoreToolsBuildVersion\"I\"sequenceNumber\"Q\"compatibilityState\"Q\"itemID\"Q\"deviceFamilies\"I\"identifier\"I\"counterpartIdentifiers\"I\"equivalentBundleIdentifiers\"I\"categoryType\"I\"secondaryCategoryType\"I\"filename\"I\"bundleVersion\"I\"shortVersionString\"I\"installType\"I\"installFailureReason\"Q\"vendorName\"I\"appType\"I\"staticDiskUsage\"Q\"purchaserDSID\"Q\"downloaderDSID\"Q\"familyID\"Q\"itemName\"I\"storefront\"Q\"versionIdentifier\"Q\"sourceAppBundleID\"I\"appVariant\"I\"managementDeclarationIdentifier\"I\"ratingRank\"Q\"ratingLabel\"I\"genreID\"Q\"genre\"I\"distributorInfo\"I\"ratingRankEligibilityDomain\"Q\"primaryIconName\"I\"alternatePrimaryIconName\"I\"iconsDict\"I\"iconFileNames\"I\"libraryPath\"I\"libraryItems\"I\"claims\"I\"types\"I\"plugins\"I\"driverExtensions\"I\"extensionPoints\"I\"activityTypes\"I\"queriableSchemes\"I\"bgPermittedIDs\"I\"carPlayInstrumentClusterURLSchemes\"I\"appContainerAlias\"I\"revision\"C\"retries\"C\"_reserved4\"C\"sandboxEnvironmentVariables\"I\"localizedNameWithContext\"[1I]\"bundlePersonas\"I\"bundlePersonaTypes\"I\"appClipFields\"{LSAppClipFields=\"parentAppIDs\"I}\"recordModificationTime\"i\"supportedGameControllers\"I\"mobileInstallIDs\"I\"applicationManagementDomain\"I\"stashedAppDict\"I\"linkedParentBundleIdentifier\"I\"serializedPlaceholderPath\"I\"_reserved5\"I}"
- "{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32@0:8@16^@24"
- "{LSBundleMoreFlags=\"isWebBrowser\"b1\"isMailClient\"b1\"supportsControllerUserInteraction\"b1\"supportsSpotlightQueryContinuation\"b1\"supportsSpotlightActions\"b1\"isCodeSigningInfoNotAuthoritative\"b1\"applicationQueriesSchemesTooBig\"b1\"isUpdateAvailable\"b1\"isPlaygroundsApp\"b1\"supportsAlwaysOnDisplay\"b1\"defaultsToPrivateAlwaysOnDisplayTreatment\"b1\"supportsLiveActivities\"b1\"supportsLiveActivitiesFrequentUpdates\"b1\"requiresPostprocessing\"b1\"hasShellRole\"b1\"requiresSecureLaunch\"b1\"eligibleForWatchAppInstall\"b1\"isEligibilityCheckedBrowser\"b1\"isEligibilityCheckedBrowserEngineEmbedder\"b1\"isManagedAppDistributor\"b1\"isHiddenByAppProtection\"b1\"isLockedByAppProtection\"b1\"supportsDataExport\"b1\"hasSupportsGameModeKey\"b1\"supportsGameMode\"b1\"isOnCryptex\"b1}"
- "{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16@0:8"
- "{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
- "{LSContext=\"db\"@\"_LSDatabase\"}"
- "{LSSchema=\"headerTable\"I\"bundleTable\"I\"claimTable\"I\"serviceTable\"I\"utypeTable\"I\"bindableKeyMap\"{?=\"map\"{CSMap=\"table\"I\"cb\"{CSMapCallbacks=\"retainKey\"^?\"releaseKey\"^?\"getKeyHash\"^?\"keyMatchesData\"^?\"retainValue\"^?\"releaseValue\"^?}\"context\"^{CSMapContext}\"_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"_generation\"I\"_header\"^{_CSMapHeader}\"_keys\"^I\"_values\"^I}}\"bindingMaps\"[14{?=\"map\"{CSMap=\"table\"I\"cb\"{CSMapCallbacks=\"retainKey\"^?\"releaseKey\"^?\"getKeyHash\"^?\"keyMatchesData\"^?\"retainValue\"^?\"releaseValue\"^?}\"context\"^{CSMapContext}\"_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"_generation\"I\"_header\"^{_CSMapHeader}\"_keys\"^I\"_values\"^I}\"bindingClass\"I\"isCaseInsensitive\"C}]\"handlerPrefTable\"I\"containerTable\"I\"aliasTable\"I\"pluginTable\"I\"extensionPointTable\"I\"bindingListTable\"I\"propertyListTable\"I\"localizedStringTable\"I\"canonicalStringTable\"I\"_cache\"^{_LSSchemaCache}}"
- "{LSSessionKey=\"uid\"I\"systemSession\"B}"
- "{LSSliceData=ii}16@0:8"
- "{LSVersionNumber=\"_opaque\"[32C]}"
- "{LSVersionNumber=[32C]}16@0:8"
- "{LSVersionNumber=[32C]}40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}32"
- "{NotifyToken=\"rawValue\"{atomic<int>=\"__a_\"{__cxx_atomic_impl<int, std::__cxx_atomic_base_impl<int>>=\"__a_value\"Ai}}}"
- "{VolumeContainerResolutionAdapter=\"volumeURLOrContainerOrError\"{variant<unsigned int, NSURL *, NSError *>=\"__impl_\"{__impl<unsigned int, NSURL *, NSError *>=\"__data\"(__union<std::__variant_detail::_Trait::_Available, 0UL, unsigned int, NSURL *, NSError *>=\"__dummy\"c\"__head\"{__alt<0UL, unsigned int>=\"__value\"I}\"__tail\"(__union<std::__variant_detail::_Trait::_Available, 1UL, NSURL *, NSError *>=\"__dummy\"c\"__head\"{__alt<1UL, NSURL *>=\"__value\"@\"NSURL\"}\"__tail\"(__union<std::__variant_detail::_Trait::_Available, 2UL, NSError *>=\"__dummy\"c\"__head\"{__alt<2UL, NSError *>=\"__value\"@\"NSError\"}\"__tail\"(__union<std::__variant_detail::_Trait::_Available, 3UL>=))))\"__index\"I}}}"
- "{atomic<bool>=\"__a_\"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>=\"__a_value\"AB}}"
- "{expected<LSApplicationRecord *, NSError *>={__conditional_no_unique_address<true, std::__expected_base<LSApplicationRecord *, NSError *>::__repr>={__repr={__conditional_no_unique_address<false, std::__expected_base<LSApplicationRecord *, NSError *>::__union_t>=(__union_t=@@)}B}}}36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
- "{map<os_eligibility_domain_t, LaunchServices::NotifyToken, std::less<os_eligibility_domain_t>, std::allocator<std::pair<const os_eligibility_domain_t, LaunchServices::NotifyToken>>>=\"__tree_\"{__tree<std::__value_type<os_eligibility_domain_t, LaunchServices::NotifyToken>, std::__map_value_compare<os_eligibility_domain_t, std::pair<const os_eligibility_domain_t, LaunchServices::NotifyToken>, std::less<os_eligibility_domain_t>>, std::allocator<std::pair<const os_eligibility_domain_t, LaunchServices::NotifyToken>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
- "{optional<LSBinding>=(?=c{LSBinding=I^{LSBundleData}I^{?}@@Q})B}40@0:8^{LSContext=@}16@24@32"
- "{optional<LaunchServices::StagingDirectoryInfo>=(?=c{StagingDirectoryInfo=@@i})B}32@0:8@\"NSString\"16^@24"
- "{optional<LaunchServices::StagingDirectoryInfo>=(?=c{StagingDirectoryInfo=@@i})B}32@0:8@16^@24"
- "{optional<NSError *>=\"\"(?=\"__null_state_\"c\"__val_\"@\"NSError\")\"__engaged_\"B}"
- "{optional<NSString *>=\"\"(?=\"__null_state_\"c\"__val_\"@\"NSString\")\"__engaged_\"B}"
- "{optional<audit_token_t>=\"\"(?=\"__null_state_\"c\"__val_\"{?=\"val\"[8I]})\"__engaged_\"B}"
- "{optional<unsigned int>=\"\"(?=\"__null_state_\"c\"__val_\"I)\"__engaged_\"B}"
- "{optional<unsigned long long>=\"\"(?=\"__null_state_\"c\"__val_\"Q)\"__engaged_\"B}"
- "{optional<unsigned long long>=(?=cQ)B}32@0:8@\"FSNode\"16^@24"
- "{optional<unsigned long long>=(?=cQ)B}32@0:8@\"NSFileHandle\"16^@24"
- "{optional<unsigned long long>=(?=cQ)B}32@0:8@16^@24"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{unfair_lock_mutex=\"_os_unfair_lock_opaque\"I}"
- "{unordered_map<_opaque_pthread_t *, std::shared_ptr<LaunchServices::PerThreadContext>, std::hash<_opaque_pthread_t *>, std::equal_to<_opaque_pthread_t *>, std::allocator<std::pair<_opaque_pthread_t *const, std::shared_ptr<LaunchServices::PerThreadContext>>>>=\"__table_\"{__hash_table<std::__hash_value_type<_opaque_pthread_t *, std::shared_ptr<LaunchServices::PerThreadContext>>, std::__unordered_map_hasher<_opaque_pthread_t *, std::pair<_opaque_pthread_t *const, std::shared_ptr<LaunchServices::PerThreadContext>>, std::hash<_opaque_pthread_t *>, std::equal_to<_opaque_pthread_t *>>, std::__unordered_map_equal<_opaque_pthread_t *, std::pair<_opaque_pthread_t *const, std::shared_ptr<LaunchServices::PerThreadContext>>, std::equal_to<_opaque_pthread_t *>, std::hash<_opaque_pthread_t *>>, std::allocator<std::pair<_opaque_pthread_t *const, std::shared_ptr<LaunchServices::PerThreadContext>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<_opaque_pthread_t *, std::shared_ptr<LaunchServices::PerThreadContext>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<_opaque_pthread_t *, std::shared_ptr<LaunchServices::PerThreadContext>>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<_opaque_pthread_t *, std::shared_ptr<LaunchServices::PerThreadContext>>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<_opaque_pthread_t *, std::shared_ptr<LaunchServices::PerThreadContext>>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{unordered_map<unsigned int, LSPluginData, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, LSPluginData>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, LSPluginData>, std::__unordered_map_hasher<unsigned int, std::pair<const unsigned int, LSPluginData>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::pair<const unsigned int, LSPluginData>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::pair<const unsigned int, LSPluginData>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, LSPluginData>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, LSPluginData>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, LSPluginData>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, LSPluginData>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{unordered_map<unsigned long long, LaunchServices::StagingDirectoryInfo, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, LaunchServices::StagingDirectoryInfo>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, LaunchServices::StagingDirectoryInfo>, std::__unordered_map_hasher<unsigned long long, std::pair<const unsigned long long, LaunchServices::StagingDirectoryInfo>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::pair<const unsigned long long, LaunchServices::StagingDirectoryInfo>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::pair<const unsigned long long, LaunchServices::StagingDirectoryInfo>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, LaunchServices::StagingDirectoryInfo>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, LaunchServices::StagingDirectoryInfo>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, LaunchServices::StagingDirectoryInfo>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, LaunchServices::StagingDirectoryInfo>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"\"{?=\"__cap_\"^I}}"
- "{vector<void *, std::allocator<void *>>=\"__begin_\"^^v\"__end_\"^^v\"\"{?=\"__cap_\"^^v}}"
- "\x81"

```
