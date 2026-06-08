## InstalledContentLibrary

> `/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary`

```diff

-1513.120.7.0.0
-  __TEXT.__text: 0xc9094
-  __TEXT.__auth_stubs: 0x1780
-  __TEXT.__objc_methlist: 0x54b4
-  __TEXT.__const: 0xf990
-  __TEXT.__cstring: 0x17c84
-  __TEXT.__gcc_except_tab: 0xc08
-  __TEXT.__oslogstring: 0x8eb
+1655.0.0.0.0
+  __TEXT.__text: 0xcdc40
+  __TEXT.__objc_methlist: 0x5a24
+  __TEXT.__const: 0xdb30
+  __TEXT.__cstring: 0x183ce
+  __TEXT.__gcc_except_tab: 0xd98
+  __TEXT.__oslogstring: 0x91f
   __TEXT.__dlopen_cstrs: 0x111
   __TEXT.__swift5_typeref: 0x30
-  __TEXT.__unwind_info: 0x18f8
-  __TEXT.__eh_frame: 0x380
-  __TEXT.__objc_classname: 0x6ce
-  __TEXT.__objc_methname: 0xf1a5
-  __TEXT.__objc_methtype: 0x1ed2
-  __TEXT.__objc_stubs: 0x8ec0
-  __DATA_CONST.__got: 0x4b8
-  __DATA_CONST.__const: 0xed0
-  __DATA_CONST.__objc_classlist: 0x208
+  __TEXT.__unwind_info: 0x1998
+  __TEXT.__eh_frame: 0x398
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1010
+  __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x80
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2dc8
+  __DATA_CONST.__objc_selrefs: 0x3050
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x170
-  __DATA_CONST.__objc_arraydata: 0xb20
-  __AUTH_CONST.__auth_got: 0xbd0
-  __AUTH_CONST.__const: 0x4b70
-  __AUTH_CONST.__cfstring: 0xcfc0
-  __AUTH_CONST.__objc_const: 0x9c38
-  __AUTH_CONST.__objc_dictobj: 0x1270
+  __DATA_CONST.__objc_superrefs: 0x190
+  __DATA_CONST.__objc_arraydata: 0xb10
+  __DATA_CONST.__got: 0x4e0
+  __AUTH_CONST.__const: 0x4d88
+  __AUTH_CONST.__cfstring: 0xd500
+  __AUTH_CONST.__objc_const: 0xa1e8
+  __AUTH_CONST.__objc_dictobj: 0x1248
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x180
-  __AUTH.__objc_data: 0x370
-  __AUTH.__data: 0xa0
-  __DATA.__objc_ivar: 0x584
-  __DATA.__data: 0xc68
-  __DATA.__bss: 0x148
-  __DATA.__common: 0xaa0
-  __DATA_DIRTY.__objc_data: 0x1180
-  __DATA_DIRTY.__data: 0x98
-  __DATA_DIRTY.__bss: 0x188
-  __DATA_DIRTY.__common: 0x8
+  __AUTH_CONST.__auth_got: 0xbf8
+  __AUTH.__objc_data: 0xe60
+  __AUTH.__data: 0x78
+  __DATA.__objc_ivar: 0x5b4
+  __DATA.__data: 0xe58
+  __DATA.__bss: 0x280
+  __DATA.__common: 0xaa4
+  __DATA_DIRTY.__objc_data: 0x780
+  __DATA_DIRTY.__data: 0x50
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 1E57C6B5-12A0-389A-9F9A-E6518B7DB998
-  Functions: 2245
-  Symbols:   6971
-  CStrings:  6397
+  UUID: 023BFA47-1894-3D72-AAA4-85D5BD559845
+  Functions: 2379
+  Symbols:   7339
+  CStrings:  3966
 
Symbols:
+ +[ICLFeatureFlags personaBundleIDRelayeringEnabled]
+ +[ICLInstallationDaemonClient sharedInstance]
+ +[MIBundleContainer _containerClassForDomain:]
+ +[MIBundleContainer appBundleContainerForIdentifier:temporary:inDomain:constructor:withError:]
+ +[MIBundleContainer enumerateAppBundleContainersInDomain:forPersona:isTransient:usingBlock:]
+ +[MIBundleContainer minimalAppBundleContainerForMetadataForIdentifier:inDomain:withError:]
+ +[MIContainer containerWithIdentifier:forPersona:ofContentClass:createIfNeeded:constructor:created:error:]
+ +[MIContainer containersForIdentifier:groupContainerIdentifier:ofContentClass:forPersona:fetchTransient:createIfNeeded:created:error:]
+ +[MIContainer enumerateContainersWithClass:forPersona:isTransient:identifiers:groupIdentifiers:usingBlock:]
+ +[MIContainer tempContainerWithIdentifier:forPersona:ofContentClass:constructor:error:]
+ +[MIDataContainer dataContainersForExecutableBundle:createIfNeeded:temporary:created:error:]
+ +[MILaunchServicesDatabaseGatherer _createDataContainersAndSetDataProtectionForBundle:forPersona:error:]
+ +[MILaunchServicesDatabaseGatherer _createPluginDataContainersForAppexBundle:forPersona:setParent:didUseProvidedPersona:containedInAppBundle:]
+ +[MILaunchServicesDatabaseGatherer _gatherPluginDataContainersForAppExtension:parentBundleID:personaUniqueStrings:parentBundleTypeIsApp:updatingAppExtensionParentID:associatedPersonas:error:]
+ +[MILaunchServicesDatabaseGatherer entryForBundle:inContainer:forPersonas:withError:]
+ +[MILaunchServicesDatabaseGatherer enumerateAppExtensionsInBundle:forPersonas:updatingAppExtensionParentID:ensureAppExtensionsAreExecutable:installProfiles:error:enumerator:]
+ +[MILaunchServicesDatabaseGatherer fetchInfoForBundle:forPersonas:inContainer:withError:]
+ +[MIMCMContainer _allContainersForIdentifiers:groupIdentifiers:contentClass:forPersona:transient:create:created:error:]
+ +[MIMCMContainer containersForBundleIdentifier:contentClass:forPersona:create:fetchTransient:created:error:]
+ +[MIMCMContainer containersForGroupIdentifier:forPersona:create:fetchTransient:created:error:]
+ +[MIPersonaAssociation sharedInstance]
+ +[MIPluginDataContainer pluginDataContainersWithIdentifier:createIfNeeded:created:error:]
+ -[ICLBundleRecord associatedPersonas]
+ -[ICLBundleRecord setAssociatedPersonas:]
+ -[ICLInstallationDaemonClient .cxx_destruct]
+ -[ICLInstallationDaemonClient _invalidateObject]
+ -[ICLInstallationDaemonClient _remoteObjectProxyWithErrorHandler:]
+ -[ICLInstallationDaemonClient _sharedConnectionWithError:]
+ -[ICLInstallationDaemonClient _synchronousRemoteObjectProxyWithErrorHandler:]
+ -[ICLInstallationDaemonClient appBundleIDsWithPersona:inDomain:error:]
+ -[ICLInstallationDaemonClient dealloc]
+ -[ICLInstallationDaemonClient personasForBuiltInBundleID:error:]
+ -[ICLInstallationDaemonClient personasForBundleID:inDomain:error:]
+ -[ICLInstallationDaemonClient setXpcConnection:]
+ -[ICLInstallationDaemonClient xpcConnection]
+ -[ICLPlaceholderRecord hasCriticalAlerts]
+ -[ICLPlaceholderRecord setHasCriticalAlerts:]
+ -[MIAppExtensionBundle _updateInfoForContainerSet:newlyCreated:error:]
+ -[MIAppExtensionBundle associatedPersonasUsingParentPersona:didUseParentPersona:error:]
+ -[MIAppExtensionBundle associatedPersonasUsingParentPersona:error:]
+ -[MIAppExtensionBundle dataContainersCreatingIfNeeded:parentPersona:makeLive:created:didUseProvidedPersona:error:]
+ -[MIAppExtensionBundle hasSystemOrAnyPersonaAssociation]
+ -[MIAppExtensionBundle setHasSystemOrAnyPersonaAssociation:]
+ -[MIAppIdentity _globalConfiguration]
+ -[MIAppIdentity _personaAssociation]
+ -[MIAppIdentity _userManagement]
+ -[MIBundle isSecondOrThirdPartyAppForDataProtection]
+ -[MIBundleContainer associatedPersonasWithError:]
+ -[MIBundleContainer initWithContainerNoBundle:error:]
+ -[MIBundleMetadata associatedPersonas]
+ -[MIBundleMetadata setAssociatedPersonas:]
+ -[MIContainer hash]
+ -[MIContainer initForTestingWithContainerURL:identifier:persona:]
+ -[MIContainer isEqual:]
+ -[MIContainer setDataProtectionClass:forSecondOrThirdPartyApp:]
+ -[MIContainerQueryResult .cxx_destruct]
+ -[MIContainerQueryResult allContainersForAllIdentifiers]
+ -[MIContainerQueryResult allContainersForIdentifier:]
+ -[MIContainerQueryResult containerForIdentifier:personaUniqueString:]
+ -[MIContainerQueryResult containersPassingTest:]
+ -[MIContainerQueryResult containers]
+ -[MIContainerQueryResult countByEnumeratingWithState:objects:count:]
+ -[MIContainerQueryResult description]
+ -[MIContainerQueryResult hash]
+ -[MIContainerQueryResult initWithContainer:]
+ -[MIContainerQueryResult initWithContainers:]
+ -[MIContainerQueryResult init]
+ -[MIContainerQueryResult isEqual:]
+ -[MIContainerQueryResult setContainers:]
+ -[MIDaemonConfiguration personaBundleIDPurgeCompleted]
+ -[MIDaemonConfiguration personaMigrationFromUMComplete]
+ -[MIDaemonConfiguration setPersonaBundleIDPurgeCompleted:]
+ -[MIDaemonConfiguration setPersonaMigrationFromUMComplete:]
+ -[MIExecutableBundle _associatedPersonasUsingParentPersona:error:]
+ -[MIExecutableBundle _dataContainersCreatingIfNeeded:forPersona:makeLive:checkIfNeeded:created:error:]
+ -[MIExecutableBundle _makeContainersLive:ifRequired:error:]
+ -[MIExecutableBundle associatedPersonasUsingParentPersona:error:]
+ -[MIExecutableBundle containerSetUsingPersonas:createBlock:created:error:]
+ -[MIExecutableBundle dataContainersCreatingIfNeeded:forPersona:makeLive:checkIfNeeded:created:error:]
+ -[MIExecutableBundle dataContainersCreatingIfNeeded:forPersona:makeLive:created:error:]
+ -[MIExtensionKitBundle _validatePresenceOfSwiftEntrySectionInExecutable:shouldHaveSwiftEntry:withError:]
+ -[MIExtensionKitBundle associatedPersonasUsingParentPersona:didUseParentPersona:error:]
+ -[MIExtensionKitBundle associatedPersonasUsingParentPersona:error:]
+ -[MIFilesystemScanner initWithScanOptions:locatingBundlesWithPersonaUniqueString:]
+ -[MIFilesystemScanner personaUniqueStringForBundles]
+ -[MIGlobalConfiguration deviceHasPersonas]
+ -[MIGlobalConfiguration isSystemPersonaAppWithBundleID:]
+ -[MIGlobalConfiguration systemPersonaBundleIDs]
+ -[MIGlobalConfiguration systemPersonaBundleIDs].cold.1
+ -[MIInstalledInfoGatherer _initWithAppExtensionBundle:inBundleIdentifier:dataContainers:associatedPersonaUniqueStrings:]
+ -[MIInstalledInfoGatherer _initWithBundleContainer:dataContainers:associatedPersonaUniqueStrings:]
+ -[MIInstalledInfoGatherer associatedPersonaUniqueStrings]
+ -[MIInstalledInfoGatherer initWithAppExtensionBundle:inBundleIdentifier:dataContainer:associatedPersonaUniqueStrings:]
+ -[MIInstalledInfoGatherer initWithAppExtensionBundle:inBundleIdentifier:dataContainers:associatedPersonaUniqueStrings:]
+ -[MIInstalledInfoGatherer initWithBundle:dataContainers:associatedPersonaUniqueStrings:]
+ -[MIInstalledInfoGatherer initWithBundleContainer:dataContainers:associatedPersonaUniqueStrings:]
+ -[MILaunchServicesDatabaseGatherer _scanAppExtensionsInBundle:inBundleContainer:personas:enumerator:error:]
+ -[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:personas:addingToBundleSet:enumeratingEntry:withError:]
+ -[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:personas:addingToBundleSet:enumeratingEntry:withError:].cold.1
+ -[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:personas:addingToBundleSet:enumeratingEntry:withError:].cold.2
+ -[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:personas:addingToBundleSet:enumeratingEntry:withError:].cold.3
+ -[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:personas:addingToBundleSet:enumeratingEntry:withError:].cold.4
+ -[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:personas:addingToBundleSet:enumeratingEntry:withError:].cold.5
+ -[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:personas:addingToBundleSet:enumeratingEntry:withError:].cold.6
+ -[MILaunchServicesDatabaseGatherer initWithOptions:personaUniqueStringForBundles:enumerator:]
+ -[MILaunchServicesDatabaseGatherer personaUniqueStringForBundles]
+ -[MILaunchServicesDatabaseGatherer scanExecutableBundle:inContainer:withError:]
+ -[MILaunchServicesDatabaseGatherer scanExecutableBundle:inContainer:withError:].cold.1
+ -[MILaunchServicesDatabaseGatherer scanExecutableBundle:inContainer:withError:].cold.2
+ -[MILaunchServicesDatabaseGatherer scanExecutableBundle:inContainer:withError:].cold.3
+ -[MIMCMContainer hash]
+ -[MIMCMContainer setDataProtectionClass:forSecondOrThirdPartyApp:error:]
+ -[MIPersonaAssociation appBundleIDsWithPersona:inDomain:error:]
+ -[MIPersonaAssociation personasForBuiltInBundleID:error:]
+ -[MIPersonaAssociation personasForBundleID:inDomain:error:]
+ -[MIPersonaAssociation personasForBundleMetadata:error:]
+ -[MIPersonaAttributes initWithPersonaString:personaType:associatedBundleIDs:dataBackedPersona:systemPersona:volumeDaemonContainer:volumeDaemonContainerSandboxExtension:]
+ -[MIPersonaAttributes isDataBackedPersona]
+ -[MIPersonaAttributes isSystemPersona]
+ -[MIPersonaContainerSet .cxx_destruct]
+ -[MIPersonaContainerSet allContainersInSafeHarbor]
+ -[MIPersonaContainerSet allContainersNotInSafeHarbor]
+ -[MIPersonaContainerSet allContainers]
+ -[MIPersonaContainerSet allPersonaUniqueStrings]
+ -[MIPersonaContainerSet containerForPersona:]
+ -[MIPersonaContainerSet containers]
+ -[MIPersonaContainerSet countByEnumeratingWithState:objects:count:]
+ -[MIPersonaContainerSet description]
+ -[MIPersonaContainerSet hash]
+ -[MIPersonaContainerSet identifier]
+ -[MIPersonaContainerSet initWithContainer:]
+ -[MIPersonaContainerSet initWithContainers:]
+ -[MIPersonaContainerSet initWithIdentifier:containerQueryResult:]
+ -[MIPersonaContainerSet isEqual:]
+ -[MIPersonaContainerSet setContainers:]
+ -[MIPluginDataContainer associatedBuiltInBundleURL]
+ -[MIPluginDataContainer didFetchSystemOrAnyPersonaMarker]
+ -[MIPluginDataContainer isSystemOrAnyPersonaExtension]
+ -[MIPluginDataContainer setAssociatedBuiltInBundleURL:]
+ -[MIPluginDataContainer setDidFetchSystemOrAnyPersonaMarker:]
+ -[MIPluginDataContainer setSystemOrAnyPersonaExtension:]
+ -[MIPluginKitBundle _getPlugInKitPersonaEntitlement:error:]
+ -[MIPluginKitBundle associatedPersonasUsingParentPersona:didUseParentPersona:error:]
+ -[MIPluginKitBundle associatedPersonasUsingParentPersona:error:]
+ -[MISignatureAgnosticHasher _hashSliceUsingFD:atOffset:withSize:machHeaderAndCommands:dictionaryKey:error:]
+ -[MIUserManagement allDataBackedPersonaUniqueStringsWithError:]
+ -[MIUserManagement allDataBackedPersonaUniqueStrings]
+ -[MIUserManagement allPersonaUniqueStringsWithError:]
+ -[MIUserManagement allPersonaVolumeDaemonContainersMapWithError:]
+ -[MIUserManagement clearLegacyBundleIDMappingWithError:]
+ -[MIUserManagement deviceHasPersonas]
+ -[MIUserManagement getPersonaVolumeDaemonContainerForUUID:containerURL:error:]
+ -[MIUserManagement legacyBundleIDMappingWithError:]
+ -[MIUserManagement personasAreKnownForUniqueStrings:error:]
+ -[MIUserManagement primaryPersonaUniqueStringWithError:]
+ -[MIUserManagement removeUnknownPersonasFromSet:error:]
+ -[MIUserManagement systemPersonaUniqueStringWithError:]
+ GCC_except_table16
+ GCC_except_table23
+ GCC_except_table29
+ GCC_except_table31
+ GCC_except_table33
+ GCC_except_table46
+ GCC_except_table52
+ GCC_except_table56
+ GCC_except_table6
+ GCC_except_table61
+ GCC_except_table75
+ GCC_except_table94
+ _CONTAINER_PERSONA_ALL_AVAILABLE
+ _MICopyPlugInKitPersonaEntitlement
+ _MIHasCriticalAlertsEntitlement
+ _MIHasExtensionKitAnyPersonaEntitlement
+ _MIHasExtensionKitSystemPersonaEntitlement
+ _MIHasWrapperBundleEntitlement
+ _MIMachOFileImageSlicesFD
+ _MIMachOFileIterateImageSlices
+ _MIMachOFileIterateImageSlicesFD
+ _MIMachOFileIterateImageVersionsFD
+ _OBJC_CLASS_$_ICLInstallationDaemonClient
+ _OBJC_CLASS_$_MIContainerQueryResult
+ _OBJC_CLASS_$_MIPersonaAssociation
+ _OBJC_CLASS_$_MIPersonaContainerSet
+ _OBJC_IVAR_$_ICLBundleRecord._associatedPersonas
+ _OBJC_IVAR_$_ICLInstallationDaemonClient._xpcConnection
+ _OBJC_IVAR_$_ICLPlaceholderRecord._hasCriticalAlerts
+ _OBJC_IVAR_$_MIAppExtensionBundle._hasSystemOrAnyPersonaAssociation
+ _OBJC_IVAR_$_MIBundleMetadata._associatedPersonas
+ _OBJC_IVAR_$_MIContainer._personaUniqueString
+ _OBJC_IVAR_$_MIContainerQueryResult._containers
+ _OBJC_IVAR_$_MIFilesystemScanner._personaUniqueStringForBundles
+ _OBJC_IVAR_$_MIGlobalConfiguration._deviceHasPersonas
+ _OBJC_IVAR_$_MIInstalledInfoGatherer._associatedPersonaUniqueStrings
+ _OBJC_IVAR_$_MILaunchServicesDatabaseGatherer._personaUniqueStringForBundles
+ _OBJC_IVAR_$_MIPersonaAttributes._isDataBackedPersona
+ _OBJC_IVAR_$_MIPersonaAttributes._isSystemPersona
+ _OBJC_IVAR_$_MIPersonaContainerSet._containers
+ _OBJC_IVAR_$_MIPersonaContainerSet._identifier
+ _OBJC_IVAR_$_MIPluginDataContainer._associatedBuiltInBundleURL
+ _OBJC_IVAR_$_MIPluginDataContainer._didFetchSystemOrAnyPersonaMarker
+ _OBJC_IVAR_$_MIPluginDataContainer._systemOrAnyPersonaExtension
+ _OBJC_IVAR_$_MIUserManagement._deviceHasPersonas
+ _OBJC_METACLASS_$_ICLInstallationDaemonClient
+ _OBJC_METACLASS_$_MIContainerQueryResult
+ _OBJC_METACLASS_$_MIPersonaAssociation
+ _OBJC_METACLASS_$_MIPersonaContainerSet
+ __DiscoverPersonas
+ __IterateImageVersions
+ __OBJC_$_CLASS_METHODS_ICLInstallationDaemonClient
+ __OBJC_$_CLASS_METHODS_MIPersonaAssociation
+ __OBJC_$_CLASS_PROP_LIST_MIDaemonConfiguration
+ __OBJC_$_CLASS_PROP_LIST_MIGlobalConfiguration
+ __OBJC_$_CLASS_PROP_LIST_MIUserManagement
+ __OBJC_$_INSTANCE_METHODS_ICLInstallationDaemonClient
+ __OBJC_$_INSTANCE_METHODS_MIContainerQueryResult
+ __OBJC_$_INSTANCE_METHODS_MIPersonaAssociation
+ __OBJC_$_INSTANCE_METHODS_MIPersonaContainerSet
+ __OBJC_$_INSTANCE_VARIABLES_ICLInstallationDaemonClient
+ __OBJC_$_INSTANCE_VARIABLES_MIContainerQueryResult
+ __OBJC_$_INSTANCE_VARIABLES_MIPersonaContainerSet
+ __OBJC_$_PROP_LIST_ICLInstallationDaemonClient
+ __OBJC_$_PROP_LIST_MIContainerQueryResult
+ __OBJC_$_PROP_LIST_MIPersonaContainerSet
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSFastEnumeration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MIPersonaAssociationLocalResolver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MIPersonaAssociationLocalResolver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSFastEnumeration
+ __OBJC_CLASS_PROTOCOLS_$_MIContainerQueryResult
+ __OBJC_CLASS_PROTOCOLS_$_MIPersonaAssociation
+ __OBJC_CLASS_PROTOCOLS_$_MIPersonaContainerSet
+ __OBJC_CLASS_RO_$_ICLInstallationDaemonClient
+ __OBJC_CLASS_RO_$_MIContainerQueryResult
+ __OBJC_CLASS_RO_$_MIPersonaAssociation
+ __OBJC_CLASS_RO_$_MIPersonaContainerSet
+ __OBJC_LABEL_PROTOCOL_$_MIPersonaAssociationLocalResolver
+ __OBJC_LABEL_PROTOCOL_$_NSFastEnumeration
+ __OBJC_METACLASS_RO_$_ICLInstallationDaemonClient
+ __OBJC_METACLASS_RO_$_MIContainerQueryResult
+ __OBJC_METACLASS_RO_$_MIPersonaAssociation
+ __OBJC_METACLASS_RO_$_MIPersonaContainerSet
+ __OBJC_PROTOCOL_$_MIPersonaAssociationLocalResolver
+ __OBJC_PROTOCOL_$_NSFastEnumeration
+ ___102-[MIExecutableBundle _dataContainersCreatingIfNeeded:forPersona:makeLive:checkIfNeeded:created:error:]_block_invoke
+ ___104-[MIExtensionKitBundle _validatePresenceOfSwiftEntrySectionInExecutable:shouldHaveSwiftEntry:withError:]_block_invoke
+ ___107+[MIContainer enumerateContainersWithClass:forPersona:isTransient:identifiers:groupIdentifiers:usingBlock:]_block_invoke
+ ___107-[MILaunchServicesDatabaseGatherer _scanAppExtensionsInBundle:inBundleContainer:personas:enumerator:error:]_block_invoke
+ ___114-[MIAppExtensionBundle dataContainersCreatingIfNeeded:parentPersona:makeLive:created:didUseProvidedPersona:error:]_block_invoke
+ ___114-[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:personas:addingToBundleSet:enumeratingEntry:withError:]_block_invoke
+ ___119+[MIMCMContainer _allContainersForIdentifiers:groupIdentifiers:contentClass:forPersona:transient:create:created:error:]_block_invoke
+ ___34+[MIUserManagement sharedInstance]_block_invoke_2
+ ___38+[MIPersonaAssociation sharedInstance]_block_invoke
+ ___45+[ICLInstallationDaemonClient sharedInstance]_block_invoke
+ ___47-[MIGlobalConfiguration systemPersonaBundleIDs]_block_invoke
+ ___51-[MIUserManagement legacyBundleIDMappingWithError:]_block_invoke
+ ___51-[MIUserManagement legacyBundleIDMappingWithError:]_block_invoke_2
+ ___51-[MIUserManagement legacyBundleIDMappingWithError:]_block_invoke_3
+ ___53-[MIContainerQueryResult allContainersForIdentifier:]_block_invoke
+ ___53-[MIUserManagement allPersonaUniqueStringsWithError:]_block_invoke
+ ___55-[MIUserManagement removeUnknownPersonasFromSet:error:]_block_invoke
+ ___55-[MIUserManagement systemPersonaUniqueStringWithError:]_block_invoke
+ ___56-[MIUserManagement clearLegacyBundleIDMappingWithError:]_block_invoke
+ ___56-[MIUserManagement clearLegacyBundleIDMappingWithError:]_block_invoke_2
+ ___56-[MIUserManagement primaryPersonaUniqueStringWithError:]_block_invoke
+ ___58-[ICLInstallationDaemonClient _sharedConnectionWithError:]_block_invoke
+ ___58-[ICLInstallationDaemonClient _sharedConnectionWithError:]_block_invoke_2
+ ___59-[MIUserManagement personasAreKnownForUniqueStrings:error:]_block_invoke
+ ___63-[MIUserManagement allDataBackedPersonaUniqueStringsWithError:]_block_invoke
+ ___63-[MIUserManagement allDataBackedPersonaUniqueStringsWithError:]_block_invoke_2
+ ___64-[ICLInstallationDaemonClient personasForBuiltInBundleID:error:]_block_invoke
+ ___64-[ICLInstallationDaemonClient personasForBuiltInBundleID:error:]_block_invoke_2
+ ___65-[MIUserManagement allPersonaVolumeDaemonContainersMapWithError:]_block_invoke
+ ___66-[ICLInstallationDaemonClient personasForBundleID:inDomain:error:]_block_invoke
+ ___66-[ICLInstallationDaemonClient personasForBundleID:inDomain:error:]_block_invoke_2
+ ___69-[MIContainerQueryResult containerForIdentifier:personaUniqueString:]_block_invoke
+ ___70-[ICLInstallationDaemonClient appBundleIDsWithPersona:inDomain:error:]_block_invoke
+ ___70-[ICLInstallationDaemonClient appBundleIDsWithPersona:inDomain:error:]_block_invoke_2
+ ___78-[MIUserManagement getPersonaVolumeDaemonContainerForUUID:containerURL:error:]_block_invoke
+ ___89+[MILaunchServicesDatabaseGatherer fetchInfoForBundle:forPersonas:inContainer:withError:]_block_invoke
+ ___90+[MIBundleContainer minimalAppBundleContainerForMetadataForIdentifier:inDomain:withError:]_block_invoke
+ ___MIMachOFileImageSlicesFD_block_invoke
+ ___MIMachOFileIterateImageSlicesFD_block_invoke
+ ___MIMachOFileIterateImageVersionsFD_block_invoke
+ ___NSArray0__struct
+ ____CopyRunnableArchNames_block_invoke
+ ____IterateImageVersions_block_invoke
+ ___block_descriptor_40_e47_"MIBundleContainer"24?0"MIMCMContainer"8^16l
+ ___block_descriptor_40_e8_32bs_e39_B36?0i8r^{mach_header=IiiIIII}12Q20Q28ls32l8
+ ___block_descriptor_40_e8_32bs_e49_v32?0"ICLBundleRecord"8"NSArray"16"NSError"24ls32l8
+ ___block_descriptor_40_e8_32s_e13_v24?0r*8^B16ls32l8
+ ___block_descriptor_40_e8_32s_e25_B24?0"MIContainer"8^B16ls32l8
+ ___block_descriptor_40_e8_32s_e31_v16?0"ICLAppExtensionRecord"8ls32l8
+ ___block_descriptor_40_e8_32s_e34_v32?0"NSString"8"NSArray"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e46_v32?0"NSString"8"MIPersonaAttributes"16^B24ls32l8
+ ___block_descriptor_41_e8_32r_e39_B36?0i8r^{mach_header=IiiIIII}12Q20Q28lr32l8
+ ___block_descriptor_41_e8_32s_e43_"MIDataContainer"32?0"NSString"8^B16^24ls32l8
+ ___block_descriptor_44_e8_32bs_e40_v40?0r^{mach_header=IiiIIII}8Q16Q24^B32ls32l8
+ ___block_descriptor_48_e8_32r40r_e27_v24?0"NSSet"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e44_v24?0"NSString"8"ICLAppExtensionRecord"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e25_B24?0"MIContainer"8^B16ls32l8s40l8
+ ___block_descriptor_56_e8_32bs40r_e24_B16?0"MIMCMContainer"8lr40l8s32l8
+ ___block_descriptor_64_e8_32s40s48r56r_e39_B36?0i8r^{mach_header=IiiIIII}12Q20Q28lr48l8s32l8s40l8r56l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0ls32l8r48l8r56l8s40l8
+ ___block_literal_global.224
+ ___block_literal_global.239
+ ___block_literal_global.561
+ _container_operation_set_data_protection
+ _macho_best_slice_in_fd
+ _macho_for_each_runnable_arch_name
+ _macho_for_each_slice_in_fd
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_allContainersForIdentifiers:groupIdentifiers:contentClass:forPersona:transient:create:created:error:
+ _objc_msgSend$_associatedPersonasUsingParentPersona:error:
+ _objc_msgSend$_containerClassForDomain:
+ _objc_msgSend$_createDataContainersAndSetDataProtectionForBundle:forPersona:error:
+ _objc_msgSend$_createPluginDataContainersForAppexBundle:forPersona:setParent:didUseProvidedPersona:containedInAppBundle:
+ _objc_msgSend$_dataContainersCreatingIfNeeded:forPersona:makeLive:checkIfNeeded:created:error:
+ _objc_msgSend$_gatherPluginDataContainersForAppExtension:parentBundleID:personaUniqueStrings:parentBundleTypeIsApp:updatingAppExtensionParentID:associatedPersonas:error:
+ _objc_msgSend$_getPlugInKitPersonaEntitlement:error:
+ _objc_msgSend$_globalConfiguration
+ _objc_msgSend$_hashSliceUsingFD:atOffset:withSize:machHeaderAndCommands:dictionaryKey:error:
+ _objc_msgSend$_initWithAppExtensionBundle:inBundleIdentifier:dataContainers:associatedPersonaUniqueStrings:
+ _objc_msgSend$_initWithBundleContainer:dataContainers:associatedPersonaUniqueStrings:
+ _objc_msgSend$_makeContainersLive:ifRequired:error:
+ _objc_msgSend$_personaAssociation
+ _objc_msgSend$_scanAppExtensionsInBundle:inBundleContainer:personas:enumerator:error:
+ _objc_msgSend$_scanBundle:inContainer:personas:addingToBundleSet:enumeratingEntry:withError:
+ _objc_msgSend$_sharedConnectionWithError:
+ _objc_msgSend$_updateInfoForContainerSet:newlyCreated:error:
+ _objc_msgSend$_userManagement
+ _objc_msgSend$_validatePresenceOfSwiftEntrySectionInExecutable:shouldHaveSwiftEntry:withError:
+ _objc_msgSend$allContainers
+ _objc_msgSend$allContainersForAllIdentifiers
+ _objc_msgSend$allContainersForIdentifier:
+ _objc_msgSend$allContainersInSafeHarbor
+ _objc_msgSend$allDataBackedPersonaUniqueStringsWithError:
+ _objc_msgSend$anyObject
+ _objc_msgSend$appBundleContainerForIdentifier:temporary:inDomain:constructor:withError:
+ _objc_msgSend$appBundleIDsWithPersona:inDomain:error:
+ _objc_msgSend$appBundleIDsWithPersona:inDomain:withCompletion:
+ _objc_msgSend$archNameString
+ _objc_msgSend$associatedPersonaUniqueStrings
+ _objc_msgSend$associatedPersonas
+ _objc_msgSend$associatedPersonasUsingParentPersona:didUseParentPersona:error:
+ _objc_msgSend$associatedPersonasUsingParentPersona:error:
+ _objc_msgSend$associatedPersonasWithError:
+ _objc_msgSend$containerForPersona:
+ _objc_msgSend$containerSetUsingPersonas:createBlock:created:error:
+ _objc_msgSend$containerWithIdentifier:forPersona:ofContentClass:createIfNeeded:constructor:created:error:
+ _objc_msgSend$containers
+ _objc_msgSend$containersForBundleIdentifier:contentClass:forPersona:create:fetchTransient:created:error:
+ _objc_msgSend$containersForGroupIdentifier:forPersona:create:fetchTransient:created:error:
+ _objc_msgSend$containersForIdentifier:groupContainerIdentifier:ofContentClass:forPersona:fetchTransient:createIfNeeded:created:error:
+ _objc_msgSend$containersPassingTest:
+ _objc_msgSend$dataContainersCreatingIfNeeded:forPersona:makeLive:created:error:
+ _objc_msgSend$dataContainersCreatingIfNeeded:parentPersona:makeLive:created:didUseProvidedPersona:error:
+ _objc_msgSend$didFetchSystemOrAnyPersonaMarker
+ _objc_msgSend$entryForBundle:inContainer:forPersonas:withError:
+ _objc_msgSend$enumerateAppExtensionsInBundle:forPersonas:updatingAppExtensionParentID:ensureAppExtensionsAreExecutable:installProfiles:error:enumerator:
+ _objc_msgSend$fileURLWithPath:isDirectory:relativeToURL:
+ _objc_msgSend$hasCriticalAlerts
+ _objc_msgSend$hasSystemOrAnyPersonaAssociation
+ _objc_msgSend$initWithAppExtensionBundle:inBundleIdentifier:dataContainers:associatedPersonaUniqueStrings:
+ _objc_msgSend$initWithBundle:dataContainers:associatedPersonaUniqueStrings:
+ _objc_msgSend$initWithBundleContainer:dataContainers:associatedPersonaUniqueStrings:
+ _objc_msgSend$initWithContainer:
+ _objc_msgSend$initWithContainerNoBundle:error:
+ _objc_msgSend$initWithContainers:
+ _objc_msgSend$initWithIdentifier:containerQueryResult:
+ _objc_msgSend$initWithOptions:personaUniqueStringForBundles:enumerator:
+ _objc_msgSend$initWithPersonaString:personaType:associatedBundleIDs:dataBackedPersona:systemPersona:volumeDaemonContainer:volumeDaemonContainerSandboxExtension:
+ _objc_msgSend$initWithScanOptions:locatingBundlesWithPersonaUniqueString:
+ _objc_msgSend$intersectSet:
+ _objc_msgSend$isDataBackedPersona
+ _objc_msgSend$isDataSeparatedPersona
+ _objc_msgSend$isSecondOrThirdPartyAppForDataProtection
+ _objc_msgSend$isSystemPersonaAppWithBundleID:
+ _objc_msgSend$local_appBundleIDsWithPersona:inDomain:error:
+ _objc_msgSend$local_personasForBuiltInBundleID:error:
+ _objc_msgSend$local_personasForBundleID:inDomain:error:
+ _objc_msgSend$minusSet:
+ _objc_msgSend$personaBundleIDMigrationCompleteWithError:
+ _objc_msgSend$personaBundleIDMigrationStartWithError:
+ _objc_msgSend$personaUniqueStringForBundles
+ _objc_msgSend$personasForBuiltInBundleID:error:
+ _objc_msgSend$personasForBuiltInBundleID:withCompletion:
+ _objc_msgSend$personasForBundleID:inDomain:error:
+ _objc_msgSend$personasForBundleID:inDomain:withCompletion:
+ _objc_msgSend$personasForBundleMetadata:error:
+ _objc_msgSend$pluginDataContainerWithIdentifier:forPersona:createIfNeeded:created:error:
+ _objc_msgSend$primaryPersonaUniqueStringWithError:
+ _objc_msgSend$removeUnknownPersonasFromSet:error:
+ _objc_msgSend$scanExecutableBundle:inContainer:withError:
+ _objc_msgSend$set
+ _objc_msgSend$setAssociatedBuiltInBundleURL:
+ _objc_msgSend$setAssociatedPersonas:
+ _objc_msgSend$setDataProtectionClass:forSecondOrThirdPartyApp:
+ _objc_msgSend$setDataProtectionClass:forSecondOrThirdPartyApp:error:
+ _objc_msgSend$setDidFetchSystemOrAnyPersonaMarker:
+ _objc_msgSend$setHasCriticalAlerts:
+ _objc_msgSend$setHasSystemOrAnyPersonaAssociation:
+ _objc_msgSend$setSystemOrAnyPersonaExtension:
+ _objc_msgSend$systemPersonaBundleIDs
+ _objc_msgSend$systemPersonaUniqueStringWithError:
+ _objc_msgSend$tempContainerWithIdentifier:forPersona:ofContentClass:constructor:error:
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x7
+ _objc_retain_x9
+ _swift_release_x20
+ _swift_release_x21
+ _swift_retain_x20
+ _systemPersonaBundleIDs.onceToken
+ _systemPersonaBundleIDs.systemBundleIDs
- +[MIContainer containersForIdentifier:groupContainerIdentifier:ofContentClass:forPersona:fetchTransient:createIfNeeded:error:]
- +[MIContainerProtectionManager defaultManager]
- +[MILaunchServicesDatabaseGatherer _createPluginDataContainerForAppexBundle:forPersona:setParent:]
- +[MILaunchServicesDatabaseGatherer entryForBundle:inContainer:forPersona:withError:]
- +[MILaunchServicesDatabaseGatherer enumerateAppExtensionsInBundle:forPersona:updatingAppExtensionParentID:ensureAppExtensionsAreExecutable:installProfiles:error:enumerator:]
- +[MILaunchServicesDatabaseGatherer fetchInfoForBundle:forPersona:inContainer:withError:]
- +[MIMCMContainer _allContainersForIdentifiers:groupIdentifiers:contentClass:forPersona:transient:create:error:]
- +[MIMCMContainer containersForBundleIdentifier:contentClass:forPersona:create:fetchTransient:error:]
- +[MIMCMContainer containersForGroupIdentifier:forPersona:create:fetchTransient:error:]
- -[MIAppExtensionBundle dataContainerCreatingIfNeeded:forPersona:makeLive:created:error:]
- -[MIAppExtensionBundle dataContainerForPersona:error:]
- -[MIContainerProtectionManager setDataProtectionOnDataContainer:forNewBundle:retryIfLocked:]
- -[MIDaemonConfiguration deviceHasPersonas]
- -[MIExtensionKitBundle _validatePresenceOfSwiftEntrySectionInFile:shouldHaveSwiftEntry:withError:]
- -[MIFilesystemScanner initWithScanOptions:]
- -[MIFilesystemScanner initWithScanOptions:personaUniqueString:]
- -[MIFilesystemScanner init]
- -[MIFilesystemScanner personaUniqueString]
- -[MIGlobalConfiguration primaryPersonaString]
- -[MIGlobalConfiguration primaryPersonaString].cold.1
- -[MIInstalledInfoGatherer _initWithAppExtensionBundle:inBundleIdentifier:dataContainers:]
- -[MIInstalledInfoGatherer _initWithBundleContainer:dataContainers:]
- -[MIInstalledInfoGatherer initWithAppExtensionBundle:inBundleIdentifier:dataContainer:]
- -[MIInstalledInfoGatherer initWithAppExtensionBundle:inBundleIdentifier:dataContainers:]
- -[MIInstalledInfoGatherer initWithBundle:dataContainer:]
- -[MIInstalledInfoGatherer initWithBundle:dataContainers:]
- -[MIInstalledInfoGatherer initWithBundleContainer:dataContainer:]
- -[MIInstalledInfoGatherer initWithBundleContainer:dataContainers:]
- -[MIInstalledInfoGatherer personaUniqueStrings]
- -[MILaunchServicesDatabaseGatherer _scanAppExtensionsInBundle:inBundleContainer:withError:]
- -[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:addingToBundleSet:enumeratingEntry:withError:]
- -[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:addingToBundleSet:enumeratingEntry:withError:].cold.1
- -[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:addingToBundleSet:enumeratingEntry:withError:].cold.2
- -[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:addingToBundleSet:enumeratingEntry:withError:].cold.3
- -[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:addingToBundleSet:enumeratingEntry:withError:].cold.4
- -[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:addingToBundleSet:enumeratingEntry:withError:].cold.5
- -[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:addingToBundleSet:enumeratingEntry:withError:].cold.6
- -[MILaunchServicesDatabaseGatherer initWithOptions:personaUniqueString:enumerator:]
- -[MILaunchServicesDatabaseGatherer personaUniqueString]
- -[MILaunchServicesDatabaseGatherer scanExecutableBundle:inContainer:forPersona:withError:]
- -[MILaunchServicesDatabaseGatherer scanExecutableBundle:inContainer:forPersona:withError:].cold.1
- -[MILaunchServicesDatabaseGatherer scanExecutableBundle:inContainer:forPersona:withError:].cold.2
- -[MILaunchServicesDatabaseGatherer scanExecutableBundle:inContainer:forPersona:withError:].cold.3
- -[MIMachOImageSlice .cxx_destruct]
- -[MIMachOImageSlice setArchNameString:]
- -[MIPersonaAttributes initWithPersonaString:personaType:associatedBundleIDs:volumeDaemonContainer:volumeDaemonContainerSandboxExtension:]
- -[MISignatureAgnosticHasher _hashSliceAtOffset:withSize:machHeaderAndCommands:dictionaryKey:error:]
- -[MISignatureAgnosticHasher dealloc]
- -[MISignatureAgnosticHasher fd]
- -[MISignatureAgnosticHasher setFd:]
- -[MIUserManagement allPersonaVolumeDaemonContainersMap]
- -[MIUserManagement bundleIDsAssociatedWithPersonaUniqueString:error:]
- -[MIUserManagement enterprisePersonaUniqueString]
- -[MIUserManagement multiPersonaSADAppBundleIDsWithError:]
- -[MIUserManagement personaForBundleID:error:]
- -[MIUserManagement personaVolumeDaemonContainerForUUID:]
- -[MIUserManagement setBundleIdentifiers:forPersonaUniqueString:error:]
- -[MIUserManagement setEnterprisePersonaUniqueString:]
- GCC_except_table15
- GCC_except_table19
- GCC_except_table22
- GCC_except_table24
- GCC_except_table30
- GCC_except_table39
- GCC_except_table45
- GCC_except_table60
- GCC_except_table66
- GCC_except_table67
- GCC_except_table79
- GCC_except_table86
- _OBJC_CLASS_$_MIContainerProtectionManager
- _OBJC_IVAR_$_MIDaemonConfiguration._deviceHasPersonas
- _OBJC_IVAR_$_MIFilesystemScanner._personaUniqueString
- _OBJC_IVAR_$_MIInstalledInfoGatherer._personaUniqueStrings
- _OBJC_IVAR_$_MILaunchServicesDatabaseGatherer._personaUniqueString
- _OBJC_IVAR_$_MIMachOImageSlice._archNameString
- _OBJC_IVAR_$_MISignatureAgnosticHasher._fd
- _OBJC_IVAR_$_MIUserManagement._enterprisePersonaUniqueString
- _OBJC_METACLASS_$_MIContainerProtectionManager
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- __AllPersonasAssociatedWithIdentifier
- __OBJC_$_CLASS_METHODS_MIContainerProtectionManager
- __OBJC_$_INSTANCE_METHODS_MIContainerProtectionManager
- __OBJC_CLASS_RO_$_MIContainerProtectionManager
- __OBJC_METACLASS_RO_$_MIContainerProtectionManager
- ___111+[MIMCMContainer _allContainersForIdentifiers:groupIdentifiers:contentClass:forPersona:transient:create:error:]_block_invoke
- ___39+[MIDaemonConfiguration sharedInstance]_block_invoke
- ___45-[MIGlobalConfiguration primaryPersonaString]_block_invoke
- ___45-[MIUserManagement personaForBundleID:error:]_block_invoke
- ___45-[MIUserManagement personaForBundleID:error:]_block_invoke_2
- ___45-[MIUserManagement systemPersonaUniqueString]_block_invoke
- ___46+[MIContainerProtectionManager defaultManager]_block_invoke
- ___46-[MIUserManagement primaryPersonaUniqueString]_block_invoke
- ___49-[MIUserManagement enterprisePersonaUniqueString]_block_invoke
- ___55-[MIUserManagement allPersonaVolumeDaemonContainersMap]_block_invoke
- ___56-[MIUserManagement personaVolumeDaemonContainerForUUID:]_block_invoke
- ___57-[MIUserManagement multiPersonaSADAppBundleIDsWithError:]_block_invoke
- ___69-[MIUserManagement bundleIDsAssociatedWithPersonaUniqueString:error:]_block_invoke
- ___88+[MILaunchServicesDatabaseGatherer fetchInfoForBundle:forPersona:inContainer:withError:]_block_invoke
- ___91-[MILaunchServicesDatabaseGatherer _scanAppExtensionsInBundle:inBundleContainer:withError:]_block_invoke
- ___92-[MIContainerProtectionManager setDataProtectionOnDataContainer:forNewBundle:retryIfLocked:]_block_invoke
- ___98-[MIExtensionKitBundle _validatePresenceOfSwiftEntrySectionInFile:shouldHaveSwiftEntry:withError:]_block_invoke
- ___MIMachOFileIterateImageVersions_block_invoke_2
- ___block_descriptor_32_e8_v16?0Q8l
- ___block_descriptor_40_e8_32bs_e37_v24?0"ICLBundleRecord"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e50_B24?0r^{fat_arch=iiIII}8r^{mach_header=IiiIIII}16ls32l8
- ___block_descriptor_40_e8_32s_e44_v24?0"NSString"8"ICLAppExtensionRecord"16ls32l8
- ___block_descriptor_41_e8_32r_e50_B24?0r^{fat_arch=iiIII}8r^{mach_header=IiiIIII}16lr32l8
- ___block_descriptor_64_e8_32s40s48r56r_e50_B24?0r^{fat_arch=iiIII}8r^{mach_header=IiiIIII}16lr48l8s32l8s40l8r56l8
- ___block_descriptor_72_e8_32s40s48r56r64r_e5_v8?0lr48l8s32l8r56l8s40l8r64l8
- ___block_descriptor_tmp
- ___block_descriptor_tmp.18
- ___block_literal_global.220
- ___block_literal_global.235
- ___block_literal_global.555
- ___get_highest_sdk_version_for_any_slice_block_invoke
- ___get_highest_sdk_version_for_any_slice_block_invoke_2
- __read_macho_header_and_load_commands
- _container_set_data_protection_for_current_user
- _get_highest_sdk_version_for_any_slice
- _objc_msgSend$_allContainersForIdentifiers:groupIdentifiers:contentClass:forPersona:transient:create:error:
- _objc_msgSend$_createPluginDataContainerForAppexBundle:forPersona:setParent:
- _objc_msgSend$_hashSliceAtOffset:withSize:machHeaderAndCommands:dictionaryKey:error:
- _objc_msgSend$_initWithAppExtensionBundle:inBundleIdentifier:dataContainers:
- _objc_msgSend$_initWithBundleContainer:dataContainers:
- _objc_msgSend$_scanAppExtensionsInBundle:inBundleContainer:withError:
- _objc_msgSend$_scanBundle:inContainer:addingToBundleSet:enumeratingEntry:withError:
- _objc_msgSend$_validatePresenceOfSwiftEntrySectionInFile:shouldHaveSwiftEntry:withError:
- _objc_msgSend$appBundleContainerForIdentifier:inDomain:withError:
- _objc_msgSend$containersForBundleIdentifier:contentClass:forPersona:create:fetchTransient:error:
- _objc_msgSend$containersForGroupIdentifier:forPersona:create:fetchTransient:error:
- _objc_msgSend$containersForIdentifier:groupContainerIdentifier:ofContentClass:forPersona:fetchTransient:createIfNeeded:error:
- _objc_msgSend$enterprisePersonaUniqueString
- _objc_msgSend$entryForBundle:inContainer:forPersona:withError:
- _objc_msgSend$enumerateAppExtensionsInBundle:forPersona:updatingAppExtensionParentID:ensureAppExtensionsAreExecutable:installProfiles:error:enumerator:
- _objc_msgSend$fd
- _objc_msgSend$initWithAppExtensionBundle:inBundleIdentifier:dataContainers:
- _objc_msgSend$initWithBundle:dataContainers:
- _objc_msgSend$initWithBundleContainer:dataContainers:
- _objc_msgSend$initWithOptions:personaUniqueString:enumerator:
- _objc_msgSend$initWithPersonaString:personaType:associatedBundleIDs:volumeDaemonContainer:volumeDaemonContainerSandboxExtension:
- _objc_msgSend$initWithScanOptions:personaUniqueString:
- _objc_msgSend$isEnterprisePersona
- _objc_msgSend$listAllPersonaWithAttributes
- _objc_msgSend$multiPersonaSADAppBundleIDsWithError:
- _objc_msgSend$personaForBundleID:error:
- _objc_msgSend$personaUniqueStrings
- _objc_msgSend$personaUniqueStringsForAppWithBundleID:error:
- _objc_msgSend$primaryPersonaString
- _objc_msgSend$primaryPersonaUniqueString
- _objc_msgSend$privateTempAppBundleContainerWithIdentifier:error:
- _objc_msgSend$scanExecutableBundle:inContainer:forPersona:withError:
- _objc_msgSend$setArchNameString:
- _objc_msgSend$setDataProtectionOnDataContainer:forNewBundle:retryIfLocked:
- _objc_msgSend$setFd:
- _objc_msgSend$systemPersonaUniqueString
- _objc_msgSend$tempAppBundleContainerWithIdentifier:error:
- _parse_macho_is_cpu_type_runnable_for_apps
- _parse_macho_is_file_runnable_for_apps
- _parse_macho_iterate_slices
- _parse_macho_iterate_slices_fd
- _pread
- _primaryPersonaString.onceToken
- _primaryPersonaString.personalPersona
- _rosetta_is_current_process_translated
- _sharedInstance.daemonConfigInstance
- _sharedInstance.daemonConfigOnceToken
- _swap_fat_arch
- _swap_fat_header
- _swap_mach_header
- _swap_mach_header_64
- _swift_retain
- _sysctlbyname
- _syslog
CStrings:
+ "#'"
+ "%@, associatedPersonas=%@"
+ "*H"
+ "+[MIBundleContainer appBundleContainerForIdentifier:temporary:inDomain:constructor:withError:]"
+ "+[MIBundleContainer enumerateAppBundleContainersInDomain:forPersona:isTransient:usingBlock:]"
+ "+[MIContainer containerWithIdentifier:forPersona:ofContentClass:createIfNeeded:constructor:created:error:]"
+ "+[MIContainer containersForIdentifier:groupContainerIdentifier:ofContentClass:forPersona:fetchTransient:createIfNeeded:created:error:]"
+ "+[MIContainer enumerateContainersWithClass:forPersona:isTransient:identifiers:groupIdentifiers:usingBlock:]_block_invoke"
+ "+[MIContainer tempContainerWithIdentifier:forPersona:ofContentClass:constructor:error:]"
+ "+[MILaunchServicesDatabaseGatherer _createDataContainersAndSetDataProtectionForBundle:forPersona:error:]"
+ "+[MILaunchServicesDatabaseGatherer _createPluginDataContainersForAppexBundle:forPersona:setParent:didUseProvidedPersona:containedInAppBundle:]"
+ "+[MILaunchServicesDatabaseGatherer _gatherPluginDataContainersForAppExtension:parentBundleID:personaUniqueStrings:parentBundleTypeIsApp:updatingAppExtensionParentID:associatedPersonas:error:]"
+ "+[MILaunchServicesDatabaseGatherer entryForBundle:inContainer:forPersonas:withError:]"
+ "+[MILaunchServicesDatabaseGatherer enumerateAppExtensionsInBundle:forPersonas:updatingAppExtensionParentID:ensureAppExtensionsAreExecutable:installProfiles:error:enumerator:]"
+ "+[MILaunchServicesDatabaseGatherer fetchInfoForBundle:forPersonas:inContainer:withError:]_block_invoke"
+ "+[MIMCMContainer _allContainersForIdentifiers:groupIdentifiers:contentClass:forPersona:transient:create:created:error:]"
+ "+[MIUserManagement sharedInstance]_block_invoke_2"
+ "-[ICLInstallationDaemonClient _sharedConnectionWithError:]"
+ "-[MIAppExtensionBundle _updateInfoForContainerSet:newlyCreated:error:]"
+ "-[MIAppExtensionBundle associatedPersonasUsingParentPersona:didUseParentPersona:error:]"
+ "-[MIAppExtensionBundle associatedPersonasUsingParentPersona:error:]"
+ "-[MIContainer setDataProtectionClass:forSecondOrThirdPartyApp:]"
+ "-[MIExecutableBundle _dataContainersCreatingIfNeeded:forPersona:makeLive:checkIfNeeded:created:error:]"
+ "-[MIExecutableBundle _makeContainersLive:ifRequired:error:]"
+ "-[MIExtensionKitBundle _validatePresenceOfSwiftEntrySectionInExecutable:shouldHaveSwiftEntry:withError:]"
+ "-[MILaunchServicesDatabaseGatherer _scanAppExtensionsInBundle:inBundleContainer:personas:enumerator:error:]_block_invoke"
+ "-[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:personas:addingToBundleSet:enumeratingEntry:withError:]"
+ "-[MILaunchServicesDatabaseGatherer initWithOptions:personaUniqueStringForBundles:enumerator:]"
+ "-[MILaunchServicesDatabaseGatherer scanExecutableBundle:inContainer:withError:]"
+ "-[MIMCMContainer setDataProtectionClass:forSecondOrThirdPartyApp:error:]"
+ "-[MIPluginDataContainer associatedBuiltInBundleURL]"
+ "-[MIPluginDataContainer isSystemOrAnyPersonaExtension]"
+ "-[MIPluginDataContainer setAssociatedBuiltInBundleURL:]"
+ "-[MIPluginDataContainer setSystemOrAnyPersonaExtension:]"
+ "-[MIPluginKitBundle associatedPersonasUsingParentPersona:didUseParentPersona:error:]"
+ "-[MISignatureAgnosticHasher _hashSliceUsingFD:atOffset:withSize:machHeaderAndCommands:dictionaryKey:error:]"
+ "-[MIUserManagement clearLegacyBundleIDMappingWithError:]_block_invoke_2"
+ "-[MIUserManagement personasAreKnownForUniqueStrings:error:]_block_invoke"
+ "-[MIUserManagement primaryPersonaUniqueStringWithError:]_block_invoke"
+ "-[MIUserManagement systemPersonaUniqueStringWithError:]_block_invoke"
+ "27.9999"
+ "<%@ status:%lu isNew:%c container:%@>"
+ "@\"MIBundleContainer\"24@?0@\"MIMCMContainer\"8^@16"
+ "@\"MIDataContainer\"32@?0@\"NSString\"8^B16^@24"
+ "Asked for data containers for %@ but none is needed."
+ "Assuming unknown built-in app %@ should be associated with primary persona"
+ "B24@?0@\"MIContainer\"8^B16"
+ "B36@?0i8r^{mach_header=IiiIIII}12Q20Q28"
+ "Client-provided persona %@ is not among available personas on the system."
+ "Could not determine architectures in the executable at \"%s\" because the file is malformed."
+ "Could not determine architectures in the executable at \"%s\" because the file is not a mach-o format file."
+ "Could not determine architectures in the executable at \"%s\"."
+ "Expected to create/fetch only one container for %@ with persona %@, but got %ld"
+ "Expected to find PERSONAL persona data container in %@"
+ "Failed to clear apps associated with persona %@"
+ "Failed to discover associated personas for bundle in container %@ : %@"
+ "Failed to discover personas for built-in app %@ : %@"
+ "Failed to fetch SYSTEM persona extension marker info from plugin data container %@: %@"
+ "Failed to fetch data containers for app extension at %@: %@; skipping it"
+ "Failed to find runnable executable slice for \"%s\". The architectures in the file could not be determined."
+ "Failed to get bundle URL for plugin data container %@: %@"
+ "Failed to get data containers for containerized app %@ for persona %@ : %@"
+ "Failed to get data containers for identifier %@ : %@"
+ "Failed to get entry for bundle %@ in %@ personas %@ : %@"
+ "Failed to get plugin data containers for app extension %@ in bundle %@ for persona %@ : %@"
+ "Failed to get primary persona unique string"
+ "Failed to get system persona unique string"
+ "Failed to iterate mach-o slices for input file: %s"
+ "Failed to locate personal persona: UserManagement returned %lu personas but none of them had isPersonalPersona = YES"
+ "Failed to locate system persona: UserManagement returned %lu personas but none of them had isSystemPersona = YES"
+ "Failed to open executable at %s"
+ "Failed to refresh persona information during init: %@"
+ "Failed to resolve persona for %@"
+ "Failed to save bundle URL on plugin data container %@: %@"
+ "Failed to scan %@ in %@ : %@"
+ "Failed to set data protection class %d on %@: %@"
+ "Failed to write SYSTEM persona extension marker on plugin data container %@: %@"
+ "Found multiple personas associated with %@; persona resolution is ambiguous. Found: %@"
+ "Found unexpected value for entitlement %@: %@; falling back to persona %@"
+ "Found unknown personas in %@ associated with %@; overriding association to %@"
+ "Found zero associated personas for app %@; assuming primary persona"
+ "Got unexpected bundle type for persona discovery: %@"
+ "HasCriticalAlerts"
+ "Ignoring app extension at %@ due to validation issue(s): %@. See previous log messages for details."
+ "InDiagnosticsMode"
+ "Installation domain %@ does not map to a container class."
+ "MIMachOFileIterateImageSlices"
+ "MIMachOFileIterateImageSlicesFD"
+ "MI_Persona_BundleID_Relayering"
+ "PersonaBundleIDMigration"
+ "PersonaBundleIDPurgeCompleteInUM"
+ "PersonaMigrationFromUMComplete"
+ "The executable at \"%s\" does not contain any code that is runnable on this device."
+ "The executable at \"%s\" does not contain code for any platform and CPU architecture combination that is runnable on this device. The executable has code for these platforms and architectures: %@. This device can run code for these architectures: %@. This device can run code for these platforms: %@"
+ "The persona unique string %@ does not correspond to any known persona on this system."
+ "Unable to get primary persona unique string from UserManagement"
+ "Unable to resolve persona for location of identity %@"
+ "Unexpectedly called base class implementation of %s"
+ "Unexpectedly was not passed personas for app bundle %@ in container %@"
+ "Unexpectedly was not passed personas when scanning appex %@ in %@"
+ "UserManagement"
+ "UserManager returned an empty persona list"
+ "[%@, %@]"
+ "_CreateErrorForMachOBestSliceEBADARCH"
+ "_DiscoverPersonas"
+ "_DiscoverPersonasForBuiltInBundle"
+ "_DiscoverPersonasFromBundleContainer"
+ "associatedPersonas"
+ "com.apple.CloudKit.ShareBear"
+ "com.apple.DocumentsApp"
+ "com.apple.MobileInstallation.AssociatedBuiltInBundleURL"
+ "com.apple.MobileInstallation.SystemOrAnyPersonaExtensionMarker"
+ "com.apple.Preferences"
+ "com.apple.developer.usernotifications.critical-alerts"
+ "com.apple.developer.wrapper-bundle"
+ "com.apple.mobilemail"
+ "com.apple.mobilenotes"
+ "com.apple.private.extensionkit.builtinanypersona"
+ "com.apple.private.extensionkit.builtinsystempersona"
+ "com.apple.private.pluginkit.persona"
+ "com.apple.siri"
+ "hasCriticalAlerts"
+ "host"
+ "macho_best_slice_in_fd failed"
+ "macho_for_each_slice_in_fd failed for %s"
+ "v16@?0@\"ICLAppExtensionRecord\"8"
+ "v24@?0@\"NSSet\"8@\"NSError\"16"
+ "v24@?0r*8^B16"
+ "v32@?0@\"ICLBundleRecord\"8@\"NSArray\"16@\"NSError\"24"
+ "v32@?0@\"NSString\"8@\"NSArray\"16^B24"
+ "v40@?0r^{mach_header=IiiIIII}8Q16Q24^B32"
+ "visionOS"
+ "visionOS Simulator"
- "#"
- "#16@0:8"
- "*G"
- "+[MIBundleContainer appBundleContainerForIdentifier:temporary:inDomain:withError:]"
- "+[MIContainer containerWithIdentifier:forPersona:ofContentClass:createIfNeeded:created:error:]"
- "+[MIContainer containersForIdentifier:groupContainerIdentifier:ofContentClass:forPersona:fetchTransient:createIfNeeded:error:]"
- "+[MIContainer tempContainerWithIdentifier:forPersona:ofContentClass:error:]"
- "+[MIDataContainer dataContainerForExecutableBundle:forPersona:createIfNeeded:temporary:created:error:]"
- "+[MILaunchServicesDatabaseGatherer _createPluginDataContainerForAppexBundle:forPersona:setParent:]"
- "+[MILaunchServicesDatabaseGatherer entryForBundle:inContainer:forPersona:withError:]"
- "+[MILaunchServicesDatabaseGatherer enumerateAppExtensionsInBundle:forPersona:updatingAppExtensionParentID:ensureAppExtensionsAreExecutable:installProfiles:error:enumerator:]"
- "+[MILaunchServicesDatabaseGatherer fetchInfoForBundle:forPersona:inContainer:withError:]_block_invoke"
- "-[MIExtensionKitBundle _validatePresenceOfSwiftEntrySectionInFile:shouldHaveSwiftEntry:withError:]"
- "-[MILaunchServicesDatabaseGatherer _scanAppExtensionsInBundle:inBundleContainer:withError:]_block_invoke"
- "-[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:addingToBundleSet:enumeratingEntry:withError:]"
- "-[MILaunchServicesDatabaseGatherer initWithOptions:personaUniqueString:enumerator:]"
- "-[MILaunchServicesDatabaseGatherer scanExecutableBundle:inContainer:forPersona:withError:]"
- "-[MISignatureAgnosticHasher _hashSliceAtOffset:withSize:machHeaderAndCommands:dictionaryKey:error:]"
- "-[MIUserManagement allPersonaVolumeDaemonContainersMap]_block_invoke"
- "-[MIUserManagement bundleIDsAssociatedWithPersonaUniqueString:error:]_block_invoke"
- "-[MIUserManagement enterprisePersonaUniqueString]_block_invoke"
- "-[MIUserManagement personaForBundleID:error:]"
- "-[MIUserManagement personaForBundleID:error:]_block_invoke_2"
- "-[MIUserManagement personaVolumeDaemonContainerForUUID:]_block_invoke"
- "-[MIUserManagement primaryPersonaUniqueString]_block_invoke"
- "-[MIUserManagement setBundleIdentifiers:forPersonaUniqueString:error:]"
- "-[MIUserManagement systemPersonaUniqueString]_block_invoke"
- ".cxx_destruct"
- "1"
- "26.9999"
- "32-bit thin matching_arch cpu_type: 0x%x cpu_subtype: 0x%x"
- "3kmXfug8VcxLI5yEmsqQKw"
- "64-bit thin matching_arch cpu_type: 0x%x cpu_subtype: 0x%x"
- "<%@ status:%lu container:%@>"
- "@\"<MIFilesystemScannerDelegate>\""
- "@\"<MILocationProtocol>\""
- "@\"<MIStagingRootProtocol>\""
- "@\"ICLSinfInfo\""
- "@\"MIAppIdentity\""
- "@\"MIBundle\""
- "@\"MIBundleContainer\""
- "@\"MIBundleMetadata\""
- "@\"MICodeSigningInfo\""
- "@\"MIEmbeddedWatchBundle\""
- "@\"MIExecutableBundle\""
- "@\"MIInstallationIdentity\""
- "@\"MIMCMContainer\""
- "@\"MIPluginKitBundle\""
- "@\"MIStashMetadata\""
- "@\"MIStoreMetadata\""
- "@\"MIStoreMetadataDistributor\""
- "@\"NSArray\""
- "@\"NSCountedSet\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8^@16"
- "@\"NSURL\""
- "@\"NSURL\"24@0:8^@16"
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8I16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@24@0:8^v16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8i16i20"
- "@24@0:8r*16"
- "@28@0:8@16B24"
- "@28@0:8@16C24"
- "@28@0:8B16^@20"
- "@28@0:8C16^@20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16Q24"
- "@32@0:8@16^@24"
- "@32@0:8Q16@24"
- "@32@0:8Q16@?24"
- "@32@0:8Q16Q24"
- "@32@0:8Q16^@24"
- "@32@0:8^Q16^@24"
- "@32@0:8^{container_object_s=}16^@24"
- "@32@0:8r*16Q24"
- "@36@0:8@16B24@?28"
- "@36@0:8@16B24^@28"
- "@36@0:8@16i24Q28"
- "@36@0:8i16i20I24I28I32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24^@32"
- "@40@0:8@16B24B28^@32"
- "@40@0:8@16I24B28^@32"
- "@40@0:8@16Q24^@32"
- "@40@0:8@16^B24^@32"
- "@40@0:8Q16@24@?32"
- "@40@0:8Q16@24^@32"
- "@40@0:8^@16Q24^@32"
- "@44@0:8@16@24B32^@36"
- "@44@0:8@16B24Q28^@36"
- "@44@0:8@16B24^B28^@36"
- "@44@0:8B16B20B24B28B32^@36"
- "@44@0:8Q16@24B32^@36"
- "@44@0:8r*16@24B32^@36"
- "@48@0:8@16@24@32^@40"
- "@48@0:8@16@24@?32^@40"
- "@48@0:8@16@24B32B36^@40"
- "@48@0:8@16@24Q32^@40"
- "@48@0:8@16@24S32i36^@40"
- "@48@0:8@16Q24@32^@40"
- "@48@0:8@16q24@32^@40"
- "@48@0:8B16@20B28^B32^@40"
- "@48@0:8^@16@24Q32^@40"
- "@52@0:8@16@24B32^B36^@44"
- "@52@0:8@16Q24@32B40^@44"
- "@52@0:8@16q24@32i40^@44"
- "@52@0:8@16q24i32@36^@44"
- "@52@0:8B16@20B28B32^B36^@44"
- "@56@0:8@16@24@32@?40^@48"
- "@56@0:8@16@24@32I40B44^@48"
- "@56@0:8@16@24B32B36^B40^@48"
- "@56@0:8@16Q24@32@40q48"
- "@56@0:8@16Q24@32B40B44^@48"
- "@56@0:8q16q24r^{mach_header=IiiIIII}32^@40^@48"
- "@56@0:8{?=[8I]}16^@48"
- "@60@0:8@16@24Q32B40^B44^@52"
- "@60@0:8Q16@24B32@36@44@?52"
- "@64@0:8@16@24Q32@40B48B52^@56"
- "@64@0:8Q16@24B32@36@44B52@?56"
- "@96@0:8@16@24@32@40@48@56Q64Q72Q80@88"
- "@?"
- "@?16@0:8"
- "Asked for data container for %@ but none is needed."
- "B"
- "B16@0:8"
- "B20@0:8i16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B24@0:8^@16"
- "B24@?0r^{fat_arch=iiIII}8r^{mach_header=IiiIIII}16"
- "B28@0:8@16B24"
- "B28@0:8B16^@20"
- "B28@0:8C16^@20"
- "B28@0:8I16^@20"
- "B28@0:8i16^@20"
- "B32@0:8@\"MIExecutableBundle\"16^@24"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B32@0:8@?16^@24"
- "B32@0:8^B16^@24"
- "B32@0:8^I16^@24"
- "B32@0:8^{container_object_s=}16^@24"
- "B32@0:8i16B20^@24"
- "B32@0:8i16i20^@24"
- "B36@0:8@16B24^@28"
- "B36@0:8@16I24^I28"
- "B36@0:8@16S24^@28"
- "B36@0:8r*16B24^@28"
- "B40@0:8@16@24^@32"
- "B40@0:8@16B24S28^@32"
- "B40@0:8@16I24I28^@32"
- "B40@0:8@16Q24^@32"
- "B40@0:8@16^i24^@32"
- "B40@0:8Q16^@24^B32"
- "B40@0:8^{?=[16C][16c][1024c]}16@24^@32"
- "B44@0:8@16@24B32^@36"
- "B44@0:8@16@24C32^@36"
- "B44@0:8@16B24B28B32^@36"
- "B44@0:8@16B24S28i32^@36"
- "B44@0:8@16B24^@28@?36"
- "B44@0:8@16Q24B32^@36"
- "B44@0:8@16S24I28I32^@36"
- "B44@0:8@16i24@?28^@36"
- "B44@0:8S16@20@28^@36"
- "B48@0:8@\"MIExecutableBundle\"16@\"MIBundleContainer\"24@\"NSString\"32^@40"
- "B48@0:8@16@24@32^@40"
- "B48@0:8@16@24Q32^@40"
- "B48@0:8@16Q24Q32^@40"
- "B48@0:8@16S24I28I32i36^@40"
- "B48@0:8@16^Q24^Q32^@40"
- "B48@0:8r*16@24@32^@40"
- "B52@0:8@16@24@32i40^@44"
- "B52@0:8@16@24B32B36B40^@44"
- "B52@0:8@16@24i32@36^@44"
- "B52@0:8@16S24I28I32i36B40^@44"
- "B56@0:8@16@24@32@40^@48"
- "B56@0:8@16I24I28B32B36^B40^@48"
- "B56@0:8r*16I24I28S32I36i40B44^@48"
- "B60@0:8@16@24B32B36B40^@44@?52"
- "B60@0:8r*16i24I28I32S36I40i44B48^@52"
- "B64@0:8@16@24@32@40@48^@56"
- "B68@0:8@16@24@32i40I44I48^B52^@60"
- "B72@0:8@16@24@32I40I44i48B52^B56^@64"
- "B72@0:8@16@24@32i40I44I48i52^B56^@64"
- "B72@0:8^@16@24{?=[8I]}32^@64"
- "BundleID %@ is associated with data separated persona %@"
- "C"
- "C16@0:8"
- "C24@0:8^@16"
- "CPU type 0x%x and subtype 0x%x are not runnable"
- "CPU type 0x%x and subtype 0x%x are runnable"
- "Can't get data container for bundle %@"
- "Can't open input file %s: %s"
- "Can't seek input file %s: %s"
- "Can't stat input file %s: %s"
- "Client provided persona %@ is not among available personas on the system"
- "Container query for %@ create: %d transient: %d with nil persona"
- "Could not determine size of %@ : %s"
- "Error calling kern.grade_cputype for CPU type 0x%x and subtype 0x%x: %s"
- "Error: Argument pointer must not be null"
- "Evaluating fat slice with cputype %d; subtype %d; offset %u; size %u; align %u"
- "Expected to read %u bytes of commands but only got %zd bytes"
- "Expected to read at least sizeof(struct mach_header) but only got %zd bytes"
- "FAT matching_arch cpu_type: 0x%x cpu_subtype: 0x%x"
- "Failed to allocate %llu bytes: %s"
- "Failed to allocate memory for fat arch(s): %s"
- "Failed to associate apps with persona %@ : %@"
- "Failed to check if cpu type is runnable"
- "Failed to determine if file matches arch for input file: %s because libparsemacho returned error code: %u"
- "Failed to find associated persona for %@ using bundle container %@ : %@. Falling back to UM for persona resolution"
- "Failed to find executable bundle in container %@. Relying on UM instead of module specific logic for persona resolution."
- "Failed to find matching arch for 32-bit Mach-O input file %s"
- "Failed to find matching arch for 64-bit Mach-O input file %s"
- "Failed to find matching arch for FAT input file %s"
- "Failed to find matching arch for input file: %s"
- "Failed to find persona %@ when checking associated bundleIDs for it"
- "Failed to get SDK version from slice in %s"
- "Failed to get data container for identifier %@ : %@"
- "Failed to get plugin data container for app extension %@ in bundle %@ for persona %@ : %@"
- "Failed to iterate macho file at %s"
- "Failed to iterate on macho slices for input file: %s"
- "Failed to open executable %@ to validate sections."
- "Failed to open executable for reading at %@ : %s"
- "Failed to open macho file at %s for reading: %s"
- "Failed to query enteprise persona string: %@"
- "Failed to query multi persona SAD apps from UserManagement"
- "Failed to query primary persona string: %@"
- "Failed to query system persona string: %@"
- "Failed to read %u bytes at offset %lld : %s"
- "Failed to read fat arch(s) from input file %s: %s"
- "Failed to read fat archs from %s : %s"
- "Failed to read fat header from input file %s: %s"
- "Failed to read fat header of %s : %s"
- "Failed to read header for file %s: %s"
- "Failed to read mach header at offset %lld : %s"
- "Failed to read mach header from input file %s: %s"
- "Failed to read macho header and load commands in %s at %u"
- "Failed to read magic from %s : %s"
- "Failed to refresh persona information: %@"
- "Fat arch %u in %s specifies offset which is beyond the end of the file"
- "File at %s is not a valid mach-o (too small to contain a valid header)"
- "File is not large enough to contain %u fat arch headers and their referenced slices."
- "File is not large enough to contain commands with length %u"
- "Got 64-bit magic but didn't read size of 64-bit mach header"
- "Got fat header with magic 0x%08x and %u archs"
- "I"
- "I16@0:8"
- "ICLAppExtensionRecord"
- "ICLAppRecord"
- "ICLBundlePersonaRecord"
- "ICLBundleRecord"
- "ICLFeatureFlags"
- "ICLFrameworkRecord"
- "ICLHelperServiceClient"
- "ICLPlaceholderRecord"
- "ICLRegistrationOptions"
- "ICLSinfInfo"
- "ICLStashedAppRecord"
- "ICLSystemAppPlaceholderRecord"
- "ICLUninstallRecord"
- "ICLWorkspace"
- "Ignoring app extension at %@ due to validation issue(s). See previous log messages for details."
- "Input path is NULL"
- "MIAppExtensionBundle"
- "MIAppIdentity"
- "MIAppIdentityPersonaResolver"
- "MIAppReferenceManager"
- "MIBundle"
- "MIBundleContainer"
- "MIBundleContainerToken"
- "MIBundleMetadata"
- "MICapabilitiesManager"
- "MICodeSigningInfo"
- "MICodeSigningVerifier"
- "MIContainer"
- "MIContainerProtectionManager"
- "MIContainerToken"
- "MIDataContainer"
- "MIDataProtectionChangeOperation"
- "MIDriverKitBundle"
- "MIEmbeddedWatchBundle"
- "MIExecutableBundle"
- "MIExtensionKitBundle"
- "MIFileManager"
- "MIFileManagerCopyfileContext"
- "MIFilesystemScanner"
- "MIFilesystemScannerDelegate"
- "MIGlobalConfiguration"
- "MIGroupContainer"
- "MIInstallationIdentity"
- "MIInstalledInfoGatherer"
- "MIKeychainAccessGroupTracker"
- "MILaunchServicesDatabaseGatherer"
- "MILocation"
- "MILocationProtocol"
- "MILocationSystemDefinedBase"
- "MIMCMContainer"
- "MIMachOFileIterateImageVersions"
- "MIMachOImageSlice"
- "MIPersonaAttributes"
- "MIPluginDataContainer"
- "MIPluginKitBundle"
- "MIRelocatedBundleContainer"
- "MISignatureAgnosticHasher"
- "MIStagingLocation"
- "MIStagingRootAbsolute"
- "MIStagingRootProtocol"
- "MIStagingRootVolumeUUID"
- "MIStashMetadata"
- "MIStashedBundleContainer"
- "MIStoreMetadata"
- "MIStoreMetadataDistributor"
- "MIStoreMetadataSubGenre"
- "MISystemAppState"
- "MITestManager"
- "MIUserManagement"
- "MI_URLByAppendingPathComponents:lastIsDirectory:"
- "MI_allAccessURLs"
- "MI_dictionaryByMergingDictionaries:"
- "MI_dictionaryWithContentsOfURL:options:error:"
- "MI_writeAtomicallyToURL:withMode:owner:group:error:"
- "MI_writeAtomicallyToURL:withMode:owner:group:protectionClass:error:"
- "MI_writeAtomicallyToURL:withMode:owner:group:protectionClass:withBarrier:error:"
- "MI_writeAtomicallyToURLMatchingCurrentFileMetadata:error:"
- "MI_writeAtomicallyToURLMatchingCurrentFileMetadata:format:error:"
- "MI_writeToURL:format:options:error:"
- "Malformed fat file: %s"
- "Mismatched cpusubtype between fat_arch and mach_header: fa: %d, mh: %d"
- "Mismatched cputype between fat_arch and mach_header: fa: %d, mh: %d"
- "MobileInstallationAdditions"
- "MobileInstallationHelperServiceProtocol"
- "MobileInstallerDelegateProtocol"
- "MobileInstallerProtocol"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Number of fat archs %u exceeds the maximum %u"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "Querying persona from UserManagement: %@"
- "SDKDictionary"
- "Slice had version 0x%08x"
- "Space required for total size of load commands (%llu) is greater than indicated size of commands (%u)."
- "T#,R"
- "T#,R,N"
- "T@\"<MIFilesystemScannerDelegate>\",W,N,V_delegate"
- "T@\"<MILocationProtocol>\",&,N,V_location"
- "T@\"<MIStagingRootProtocol>\",R,N,V_stagingRoot"
- "T@\"ICLSinfInfo\",C,N,V_sinfInfo"
- "T@\"MIAppIdentity\",C,N,V_identity"
- "T@\"MIBundle\",R,W,N,V_parentBundle"
- "T@\"MIBundleContainer\",R,N,V_bundleContainer"
- "T@\"MIBundleContainer\",W,N,V_bundleContainer"
- "T@\"MIBundleMetadata\",C,N,V_bundleMetadata"
- "T@\"MICodeSigningInfo\",&,N,V_codeSigningInfo"
- "T@\"MICodeSigningInfo\",R,N,V_signingInfo"
- "T@\"MIEmbeddedWatchBundle\",&,N,V_wk2AppBundle"
- "T@\"MIExecutableBundle\",R,N,V_builtInAppParallelPlaceholderBundle"
- "T@\"MIExecutableBundle\",R,N,V_bundle"
- "T@\"MIInstallationIdentity\",&,N,V_installationIdentity"
- "T@\"MIMCMContainer\",R,N,V_rawContainer"
- "T@\"MIPluginKitBundle\",&,N,V_watchKitPlugin"
- "T@\"MIStashMetadata\",&,N,V_stashMetadata"
- "T@\"MIStoreMetadata\",C,N,V_iTunesMetadata"
- "T@\"MIStoreMetadataDistributor\",C,N,V_distributorInfo"
- "T@\"NSArray\",&,N,V_driverKitExtensionBundles"
- "T@\"NSArray\",&,N,V_executableImageSlices"
- "T@\"NSArray\",&,N,V_extensionKitBundles"
- "T@\"NSArray\",&,N,V_frameworkBundles"
- "T@\"NSArray\",&,N,V_pluginKitBundles"
- "T@\"NSArray\",&,N,V_xpcServiceBundles"
- "T@\"NSArray\",C,N,V_categories"
- "T@\"NSArray\",C,N,V_counterpartIdentifiers"
- "T@\"NSArray\",C,N,V_driverKitExtensionURLs"
- "T@\"NSArray\",C,N,V_parentIdentifiers"
- "T@\"NSArray\",C,N,V_stashedVersions"
- "T@\"NSArray\",C,N,V_subGenres"
- "T@\"NSArray\",R,C,D,N"
- "T@\"NSArray\",R,C,N"
- "T@\"NSArray\",R,N,V_dataContainers"
- "T@\"NSArray\",R,N,V_personaUniqueStrings"
- "T@\"NSArray\",R,N,V_urls"
- "T@\"NSCountedSet\",&,N,V_refs"
- "T@\"NSData\",C,N,V_installSessionID"
- "T@\"NSData\",C,N,V_protectedMetadata"
- "T@\"NSData\",C,N,V_uniqueInstallID"
- "T@\"NSData\",R,C,N,V_launchWarningData"
- "T@\"NSData\",R,N,V_serializedContainerRepresentation"
- "T@\"NSDate\",&,N,V_dateOriginallyInstalled"
- "T@\"NSDate\",&,N,V_dateStashed"
- "T@\"NSDate\",C,N,V_installDate"
- "T@\"NSDate\",C,N,V_originalInstallDate"
- "T@\"NSDate\",C,N,V_stashOriginalInstallTimestamp"
- "T@\"NSDate\",C,N,V_stashedAtTimestamp"
- "T@\"NSDictionary\",&,N,V_personaAttributesMap"
- "T@\"NSDictionary\",&,N,V_personaVolumeUUIDToDaemonContainerMap"
- "T@\"NSDictionary\",C,N,V_entitlements"
- "T@\"NSDictionary\",C,N,V_environmentVariables"
- "T@\"NSDictionary\",C,N,V_extensionCacheEntry"
- "T@\"NSDictionary\",C,N,V_groupContainerURLs"
- "T@\"NSDictionary\",C,N,V_groupContainers"
- "T@\"NSDictionary\",C,N,V_localizedDistributorName"
- "T@\"NSDictionary\",C,N,V_nameTranscriptions"
- "T@\"NSDictionary\",C,N,V_overlaidInfoPlist"
- "T@\"NSDictionary\",C,N,V_personasRecordMap"
- "T@\"NSDictionary\",N,R"
- "T@\"NSDictionary\",R,C,N"
- "T@\"NSDictionary\",R,C,N,V_coreServicesAppBundleIDToInfoMap"
- "T@\"NSDictionary\",R,C,N,V_entitlements"
- "T@\"NSDictionary\",R,C,N,V_extensionAttributes"
- "T@\"NSDictionary\",R,C,N,V_infoPlistSubset"
- "T@\"NSDictionary\",R,C,N,V_internalAppBundleIDToInfoMap"
- "T@\"NSDictionary\",R,C,N,V_stagedSystemAppBundleIDToInfoMap"
- "T@\"NSDictionary\",R,C,N,V_systemAppBundleIDToInfoMap"
- "T@\"NSDictionary\",R,C,N,V_systemAppPlaceholderBundleIDToInfoMap"
- "T@\"NSDictionary\",R,N"
- "T@\"NSDictionary\",R,N,V_hashes"
- "T@\"NSError\",&,N,V_codeSigningInfoError"
- "T@\"NSError\",&,N,V_error"
- "T@\"NSError\",&,N,V_placeholderFailureUnderlyingError"
- "T@\"NSError\",&,N,V_wk2AppBundleError"
- "T@\"NSMutableDictionary\",&,N,V_sourceForPID"
- "T@\"NSMutableDictionary\",&,N,V_systemAppStateList"
- "T@\"NSMutableSet\",R,N,V_appExtensions"
- "T@\"NSMutableSet\",R,N,V_coreServices"
- "T@\"NSMutableSet\",R,N,V_frameworks"
- "T@\"NSMutableSet\",R,N,V_internalApps"
- "T@\"NSMutableSet\",R,N,V_systemAppPlaceholders"
- "T@\"NSMutableSet\",R,N,V_systemApps"
- "T@\"NSMutableSet\",R,N,V_userApps"
- "T@\"NSNumber\",&,N,V_DSPersonID"
- "T@\"NSNumber\",&,N,V_betaExternalVersionIdentifier"
- "T@\"NSNumber\",&,N,V_downloaderID"
- "T@\"NSNumber\",&,N,V_familyID"
- "T@\"NSNumber\",&,N,V_genreID"
- "T@\"NSNumber\",&,N,V_hasOrEverHasHadIAP"
- "T@\"NSNumber\",&,N,V_initialODRSize"
- "T@\"NSNumber\",&,N,V_itemID"
- "T@\"NSNumber\",&,N,V_purchaserID"
- "T@\"NSNumber\",&,N,V_ratingRank"
- "T@\"NSNumber\",&,N,V_softwareVersionExternalIdentifier"
- "T@\"NSNumber\",&,N,V_storefront"
- "T@\"NSNumber\",C,N,V_applicationDSID"
- "T@\"NSNumber\",C,N,V_downloaderDSID"
- "T@\"NSNumber\",C,N,V_familyID"
- "T@\"NSNumber\",C,N,V_lsInstallType"
- "T@\"NSNumber\",C,N,V_marketplaceItemID"
- "T@\"NSNumber\",C,N,V_signatureVersion"
- "T@\"NSNumber\",C,N,V_staticDiskUsage"
- "T@\"NSNumber\",R,C,N,V_signatureVersion"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_testModeQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_appStateQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_internalQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_q"
- "T@\"NSSet\",C,N,V_linkedChildBundleIDs"
- "T@\"NSSet\",R,C,N"
- "T@\"NSSet\",R,C,N,V_allFrameworksDirectories"
- "T@\"NSSet\",R,C,N,V_builtInFrameworkBundleIDs"
- "T@\"NSSet\",R,C,N,V_bundleIDs"
- "T@\"NSSet\",R,C,N,V_cryptexFrameworksDirectories"
- "T@\"NSSet\",R,C,N,V_systemAppPlaceholderAppExtensionBundleIDs"
- "T@\"NSSet\",R,C,N,V_systemAppPlaceholderBundleIDs"
- "T@\"NSSet\",R,C,N,V_systemAppPlaceholderXPCServiceBundleIDs"
- "T@\"NSSet\",R,N"
- "T@\"NSString\",&,N,V_archNameString"
- "T@\"NSString\",&,N,V_bundleID"
- "T@\"NSString\",&,N,V_identifier"
- "T@\"NSString\",&,N,V_personaUniqueString"
- "T@\"NSString\",&,N,V_relativeStagingBaseDirectory"
- "T@\"NSString\",&,N,V_systemPersonaUniqueString"
- "T@\"NSString\",&,N,V_watchKitAppExecutableHash"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_accountID"
- "T@\"NSString\",C,N,V_altDSID"
- "T@\"NSString\",C,N,V_alternateIconName"
- "T@\"NSString\",C,N,V_appManagementDomain"
- "T@\"NSString\",C,N,V_appleID"
- "T@\"NSString\",C,N,V_artistName"
- "T@\"NSString\",C,N,V_assetToken"
- "T@\"NSString\",C,N,V_betaBuildGroupID"
- "T@\"NSString\",C,N,V_bundleIdentifier"
- "T@\"NSString\",C,N,V_bundleShortVersion"
- "T@\"NSString\",C,N,V_bundleShortVersionString"
- "T@\"NSString\",C,N,V_bundleVersion"
- "T@\"NSString\",C,N,V_codeInfoIdentifier"
- "T@\"NSString\",C,N,V_developerID"
- "T@\"NSString\",C,N,V_developerName"
- "T@\"NSString\",C,N,V_distributorID"
- "T@\"NSString\",C,N,V_domain"
- "T@\"NSString\",C,N,V_enterpriseInstallURL"
- "T@\"NSString\",C,N,V_enterprisePersonaUniqueString"
- "T@\"NSString\",C,N,V_extensionOwnerBundleID"
- "T@\"NSString\",C,N,V_genre"
- "T@\"NSString\",C,N,V_iAdAttribution"
- "T@\"NSString\",C,N,V_iAdConversionDate"
- "T@\"NSString\",C,N,V_iAdImpressionDate"
- "T@\"NSString\",C,N,V_installBuildVersion"
- "T@\"NSString\",C,N,V_itemName"
- "T@\"NSString\",C,N,V_kind"
- "T@\"NSString\",C,N,V_label"
- "T@\"NSString\",C,N,V_linkedParentBundleID"
- "T@\"NSString\",C,N,V_managementDeclarationIdentifier"
- "T@\"NSString\",C,N,V_marketplaceDomain"
- "T@\"NSString\",C,N,V_md5"
- "T@\"NSString\",C,N,V_parentBundleID"
- "T@\"NSString\",C,N,V_primaryPersonaUniqueString"
- "T@\"NSString\",C,N,V_purchaseDate"
- "T@\"NSString\",C,N,V_ratingLabel"
- "T@\"NSString\",C,N,V_redownloadParams"
- "T@\"NSString\",C,N,V_referrerApp"
- "T@\"NSString\",C,N,V_referrerURL"
- "T@\"NSString\",C,N,V_releaseDate"
- "T@\"NSString\",C,N,V_shortItemName"
- "T@\"NSString\",C,N,V_signerIdentity"
- "T@\"NSString\",C,N,V_signerOrganization"
- "T@\"NSString\",C,N,V_softwareVersionBundleID"
- "T@\"NSString\",C,N,V_sourceApp"
- "T@\"NSString\",C,N,V_storeCohort"
- "T@\"NSString\",C,N,V_storefrontCountryCode"
- "T@\"NSString\",C,N,V_teamIdentifier"
- "T@\"NSString\",C,N,V_validationOverrideParentBundleID"
- "T@\"NSString\",C,N,V_variantID"
- "T@\"NSString\",C,N,V_watchKitAppExecutableHash"
- "T@\"NSString\",N,R"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_bundleName"
- "T@\"NSString\",R,C,N,V_bundleParentSubdirectory"
- "T@\"NSString\",R,C,N,V_codeInfoIdentifier"
- "T@\"NSString\",R,C,N,V_extensionPointIdentifier"
- "T@\"NSString\",R,C,N,V_identifier"
- "T@\"NSString\",R,C,N,V_parentBundleID"
- "T@\"NSString\",R,C,N,V_personaUniqueString"
- "T@\"NSString\",R,C,N,V_signerIdentity"
- "T@\"NSString\",R,C,N,V_signerOrganization"
- "T@\"NSString\",R,C,N,V_teamIdentifier"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSString\",R,N,V_owningBundleIdentifier"
- "T@\"NSString\",R,N,V_personaUniqueString"
- "T@\"NSString\",R,N,V_sectionName"
- "T@\"NSURL\",&,N,V_containerURL"
- "T@\"NSURL\",C,N,V_bundleContainerURL"
- "T@\"NSURL\",C,N,V_bundleURL"
- "T@\"NSURL\",C,N,V_dataContainerURL"
- "T@\"NSURL\",C,N,V_parallelPlaceholderURL"
- "T@\"NSURL\",C,N,V_serializedPlaceholderURL"
- "T@\"NSURL\",C,N,V_shareURL"
- "T@\"NSURL\",C,N,V_sourceURL"
- "T@\"NSURL\",C,N,V_supportPageURL"
- "T@\"NSURL\",N,R"
- "T@\"NSURL\",N,R,V_appBundleURL"
- "T@\"NSURL\",N,R,V_targetDirectoryURL"
- "T@\"NSURL\",R,C,N,V_bundleParentDirectoryURL"
- "T@\"NSURL\",R,N"
- "T@\"NSURL\",R,N,V_bundleURL"
- "T@\"NSURL\",R,N,V_containerURL"
- "T@\"NSURL\",R,N,V_daemonUserDataLibraryDirectory"
- "T@\"NSURL\",R,N,V_helperLogDirectory"
- "T@\"NSURL\",R,N,V_installcoordinationdPath"
- "T@\"NSURL\",R,N,V_installcoordinationdUserDataLibraryDirectory"
- "T@\"NSURL\",R,N,V_installdPath"
- "T@\"NSURL\",R,N,V_ixDataStorageDirectoryPath"
- "T@\"NSURL\",R,N,V_mobilePath"
- "T@\"NSURL\",R,N,V_parentBundleURL"
- "T@\"NSURL\",R,N,V_rootPath"
- "T@\"NSURL\",R,N,V_url"
- "T@\"NSURL\",R,N,V_volumeDaemonContainer"
- "T@\"NSUUID\",R,N,V_volumeUUID"
- "T@\"NSXPCConnection\",&,N,V_xpcConnection"
- "T@?,C,N,V_completionBlock"
- "T@?,R,N,V_enumerator"
- "TB,N"
- "TB,N,GisFactoryInstall,V_factoryInstall"
- "TB,N,GisGameCenterEnabled,V_gameCenterEnabled"
- "TB,N,GisLaunchProhibited,V_launchProhibited"
- "TB,N,GisPurchasedRedownload,V_purchasedRedownload"
- "TB,N,GwasErroneousContainerCleanupDone"
- "TB,N,R"
- "TB,N,V_allowAdhocSigning"
- "TB,N,V_codeSigningInfoNotAuthoritative"
- "TB,N,V_deviceBasedVPP"
- "TB,N,V_gameCenterEverEnabled"
- "TB,N,V_hasAppGroupContainers"
- "TB,N,V_hasMIDBasedSINF"
- "TB,N,V_hasMessagesExtension"
- "TB,N,V_hasParallelPlaceholder"
- "TB,N,V_hasSettingsBundle"
- "TB,N,V_hasSystemContainer"
- "TB,N,V_hasSystemGroupContainers"
- "TB,N,V_ignoreErrors"
- "TB,N,V_isAutoDownload"
- "TB,N,V_isB2BCustomApp"
- "TB,N,V_isBeta"
- "TB,N,V_isContainerized"
- "TB,N,V_isDeletable"
- "TB,N,V_isEligibleForWatchAppInstall"
- "TB,N,V_isMarketplace"
- "TB,N,V_isMissingRequiredSINF"
- "TB,N,V_isNoLongerCompatible"
- "TB,N,V_isOnDemandInstallCapable"
- "TB,N,V_isOnMountedDiskImage"
- "TB,N,V_isPlaceholder"
- "TB,N,V_isPlaceholderStatusValid"
- "TB,N,V_isResolved"
- "TB,N,V_isStagedContainer"
- "TB,N,V_isSwiftPlaygroundsApp"
- "TB,N,V_isTransient"
- "TB,N,V_isUpdatedSystemApp"
- "TB,N,V_isWebNotificationBundle"
- "TB,N,V_logResourceVerificationErrors"
- "TB,N,V_performOnlineAuthorization"
- "TB,N,V_sideLoadedDeviceBasedVPP"
- "TB,N,V_sinfDataTypeIsSet"
- "TB,N,V_skipProfileIDValidation"
- "TB,N,V_supportsAppMigration"
- "TB,N,V_validateResources"
- "TB,N,V_validateUsingDetachedSignature"
- "TB,N,V_verifyTrustCachePresence"
- "TB,R"
- "TB,R,N"
- "TB,R,N,V_allowDeletableSystemApps"
- "TB,R,N,V_allowPatchWithoutSinf"
- "TB,R,N,V_codeSigningEnforcementIsDisabled"
- "TB,R,N,V_deviceHasPersonas"
- "TB,R,N,V_hasExecutable"
- "TB,R,N,V_hasIdentifiedBundle"
- "TB,R,N,V_hasNamedSection"
- "TB,R,N,V_isNew"
- "TB,R,N,V_isPlaceholder"
- "TB,R,N,V_isSharediPad"
- "TB,R,N,V_isTransient"
- "TB,R,N,V_localSigningIsUnrestricted"
- "TB,R,N,V_requireEligibilityChecksForAppsInDevelopment"
- "TB,R,N,V_shouldUpdateAppExtensionDataContainersWithParentID"
- "TB,R,N,V_skipDeviceFamilyCheck"
- "TB,R,N,V_skipThinningCheck"
- "TC,R,N,V_bundleType"
- "TI,N,V_countOfSlicesWithNamedSection"
- "TI,N,V_minOSVersion"
- "TI,N,V_platform"
- "TI,N,V_sdkVersion"
- "TI,N,V_sinfDataType"
- "TI,N,V_targetUID"
- "TI,R,N"
- "TI,R,N,V_gid"
- "TI,R,N,V_installQOSOverride"
- "TI,R,N,V_ixDaemonGID"
- "TI,R,N,V_ixDaemonUID"
- "TI,R,N,V_platformHint"
- "TI,R,N,V_uid"
- "TQ,N,V_applicationType"
- "TQ,N,V_autoInstallOverride"
- "TQ,N,V_betaTesterType"
- "TQ,N,V_codeSignerType"
- "TQ,N,V_compatibilityState"
- "TQ,N,V_containerClass"
- "TQ,N,V_diskUsage"
- "TQ,N,V_extensionPoint"
- "TQ,N,V_installType"
- "TQ,N,V_installerEpoch"
- "TQ,N,V_lsInstallType"
- "TQ,N,V_personaGenerationIdentifier"
- "TQ,N,V_placeholderFailureReason"
- "TQ,N,V_placeholderFailureUnderlyingErrorSource"
- "TQ,N,V_profileValidationType"
- "TQ,N,V_ratingRankEligibilityDomain"
- "TQ,N,V_status"
- "TQ,N,V_testFlags"
- "TQ,R"
- "TQ,R,N"
- "TQ,R,N,V_codeSignatureVerificationState"
- "TQ,R,N,V_codeSignerType"
- "TQ,R,N,V_containerClass"
- "TQ,R,N,V_estimatedAvailableMemoryForValidation"
- "TQ,R,N,V_gatherOptions"
- "TQ,R,N,V_operationType"
- "TQ,R,N,V_options"
- "TQ,R,N,V_personaType"
- "TQ,R,N,V_profileValidationType"
- "TQ,R,N,V_signingInfoSource"
- "TQ,R,N,V_stagingContentType"
- "TQ,R,N,V_stagingSubsystem"
- "T^{__CFBundle=},R,N,V_cfBundle"
- "T^{container_object_s=},R,N,V_mcmContainer"
- "Ti,N,V_contentProtectionClass"
- "Ti,N,V_cpuSubtype"
- "Ti,N,V_cpuType"
- "Ti,N,V_fd"
- "Ti,R,N"
- "Ti,R,N,V_newClass"
- "Tq,N,R"
- "Tq,N,V_extensionHandle"
- "Tq,R,N,V_extensionHandle"
- "Tq,R,N,V_nSimultaneousInstallations"
- "Tq,R,N,V_sandboxToken"
- "T{os_unfair_lock_s=I},R,N,V_lock"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathComponent:isDirectory:"
- "URLByDeletingLastPathComponent"
- "URLByDeletingPathExtension"
- "URLByStandardizingPath"
- "URLForDirectory:inDomain:appropriateForURL:create:error:"
- "URLForLocation:isAppBundle:error:"
- "URLIsOnAttachedEntityType:at:"
- "URLWithString:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Unable to determine CPU type is runnable with error: %d"
- "Unknown binary format for input file %s."
- "Unknown binary with magic 0x%08x at %s"
- "Unknown magic in macho header at offset %llu: 0x%08x"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__CFBundle=}"
- "^{__CFBundle=}16@0:8"
- "^{container_object_s=}"
- "^{container_object_s=}16@0:8"
- "_DSPersonID"
- "_URLOfFirstBundleInDirectory:withExtension:error:"
- "_accountID"
- "_allContainersForIdentifier:persona:options:error:"
- "_allContainersForIdentifiers:groupIdentifiers:contentClass:forPersona:transient:create:error:"
- "_allFrameworksDirectories"
- "_allowAdhocSigning"
- "_allowDeletableSystemApps"
- "_allowPatchWithoutSinf"
- "_altDSID"
- "_alternateIconName"
- "_appBundleURL"
- "_appExtensions"
- "_appManagementDomain"
- "_appStateQueue"
- "_appleID"
- "_applicationDSID"
- "_applicationType"
- "_archNameString"
- "_artistName"
- "_assetToken"
- "_autoInstallOverride"
- "_betaBuildGroupID"
- "_betaExternalVersionIdentifier"
- "_betaTesterType"
- "_buildBundlePersonaRecordWithDataContainer:"
- "_builtInAppParallelPlaceholderBundle"
- "_builtInFrameworkBundleIDs"
- "_bulkSetPropertiesForPath:existingFD:UID:GID:mode:flags:dataProtectionClass:removeACL:error:"
- "_bundle"
- "_bundleContainer"
- "_bundleContainerForIdentifier:forPersona:error:"
- "_bundleContainerURL"
- "_bundleExtensionForContainerClassWithError:"
- "_bundleID"
- "_bundleIDMapForAppsInDirectory:"
- "_bundleIDMapForAppsInDirectory:loadingAdditionalKeys:"
- "_bundleIDMapForBundlesInDirectory:withExtension:"
- "_bundleIDMapForBundlesInDirectory:withExtension:loadingAdditionalKeys:"
- "_bundleIDs"
- "_bundleIdentifier"
- "_bundleMetadata"
- "_bundleName"
- "_bundleParentDirectoryURL"
- "_bundleParentSubdirectory"
- "_bundleShortVersion"
- "_bundleShortVersionString"
- "_bundleType"
- "_bundleURL"
- "_bundleVersion"
- "_categories"
- "_cfBundle"
- "_codeInfoIdentifier"
- "_codeSignatureVerificationState"
- "_codeSignerType"
- "_codeSigningEnforcementIsDisabled"
- "_codeSigningInfo"
- "_codeSigningInfoError"
- "_codeSigningInfoFromMCM"
- "_codeSigningInfoNotAuthoritative"
- "_compatibilityState"
- "_completionBlock"
- "_configureBundleWithError:"
- "_connectionToInstallationDaemonWithError:"
- "_containerClass"
- "_containerForIdentifier:contentClass:forPersona:transient:create:error:"
- "_containerURL"
- "_contentProtectionClass"
- "_copyItemAtURL:toURL:failIfSrcMissing:alwaysClone:ignoreErrors:error:"
- "_coreServices"
- "_coreServicesAppBundleIDToInfoMap"
- "_countOfSlicesWithNamedSection"
- "_counterpartIdentifiers"
- "_cpuSubtype"
- "_cpuType"
- "_createDataContainerAndSetDataProtectionForBundle:forPersona:error:"
- "_createPluginDataContainerForAppexBundle:forPersona:setParent:"
- "_cryptexFrameworksDirectories"
- "_daemonUserDataLibraryDirectory"
- "_dataContainerCreatingIfNeeded:forPersona:makeLive:checkIfNeeded:created:error:"
- "_dataContainerURL"
- "_dataContainers"
- "_dataForExtendedAttributeNamed:length:onURL:orFD:error:"
- "_dateOriginallyInstalled"
- "_dateStashed"
- "_delegate"
- "_deriveContainerStatusWithError:"
- "_developerID"
- "_developerName"
- "_deviceBasedVPP"
- "_deviceHasPersonas"
- "_discoverWatchAppBundleAsPlaceholder:error:"
- "_diskUsage"
- "_distributorID"
- "_distributorInfo"
- "_doInitWithBundleID:personaUniqueString:location:"
- "_doInitWithContainer:error:"
- "_domain"
- "_downloaderDSID"
- "_downloaderID"
- "_driverKitExtensionBundles"
- "_driverKitExtensionURLs"
- "_dynamicPropertyLock"
- "_eligiblePersonaForBundle:error:"
- "_enterpriseInstallURL"
- "_enterprisePersonaUniqueString"
- "_entitlements"
- "_enumerator"
- "_enumeratorWithContainerClass:forPersona:isTransient:identifiers:groupIdentifiers:create:usingBlock:"
- "_environmentVariables"
- "_error"
- "_estimatedAvailableMemoryForValidation"
- "_executableImageSlices"
- "_extensionAttributes"
- "_extensionCacheEntry"
- "_extensionHandle"
- "_extensionKitBundles"
- "_extensionOwnerBundleID"
- "_extensionPoint"
- "_extensionPointIdentifier"
- "_factoryInstall"
- "_familyID"
- "_fd"
- "_filterExtensionBundles:forValidationFlags:"
- "_filterExtensionBundlesNotInCacheIfNeeded:"
- "_firstAvailableParentForURL:error:"
- "_fixUpForBuiltInAppParallelPlaceholder"
- "_frameworkBundles"
- "_frameworks"
- "_gameCenterEnabled"
- "_gameCenterEverEnabled"
- "_gatherOptions"
- "_genre"
- "_genreID"
- "_getBundleRootContainsOnlyContentsDirectory:error:"
- "_getMICodeSignerTypeFromMISInfoDict:codeSignerType:profileType:error:"
- "_gid"
- "_groupContainerURLs"
- "_groupContainers"
- "_groupContainersDictionaryForPersona:"
- "_hasAppGroupContainers"
- "_hasExecutable"
- "_hasIdentifiedBundle"
- "_hasMIDBasedSINF"
- "_hasMessagesExtension"
- "_hasNamedSection"
- "_hasNoConflictWithSystemAppsForSigningInfo:error:"
- "_hasNonContainerizingEntitlement:checkSeatbeltProfiles:"
- "_hasOrEverHasHadIAP"
- "_hasParallelPlaceholder"
- "_hasResource:withExtension:"
- "_hasSettingsBundle"
- "_hasSystemContainer"
- "_hasSystemGroupContainers"
- "_hashSliceAtOffset:withSize:machHeaderAndCommands:dictionaryKey:error:"
- "_hashes"
- "_helperLogDirectory"
- "_iAdAttribution"
- "_iAdConversionDate"
- "_iAdImpressionDate"
- "_iTunesMetadata"
- "_identifier"
- "_identity"
- "_ignoreErrors"
- "_infoPlistKeysToLoad"
- "_infoPlistSubset"
- "_initWithAppExtensionBundle:inBundleIdentifier:dataContainers:"
- "_initWithBundle:dataContainers:"
- "_initWithBundleContainer:dataContainers:"
- "_initWithBundleContainer:forPersonas:"
- "_initialODRSize"
- "_insecureCachedAppIdentifierIfMarkedWithEAFlag:bundleURL:allowPlaceholders:error:"
- "_installBuildVersion"
- "_installDate"
- "_installEmbeddedProvisioningProfileAtURL:withProgress:"
- "_installQOSOverride"
- "_installSessionID"
- "_installType"
- "_installationIdentity"
- "_installcoordinationdPath"
- "_installcoordinationdUserDataLibraryDirectory"
- "_installdPath"
- "_installerEpoch"
- "_internalAppBundleIDToInfoMap"
- "_internalApps"
- "_internalQueue"
- "_invalidateObject"
- "_isAutoDownload"
- "_isB2BCustomApp"
- "_isBeta"
- "_isContainerized"
- "_isDeletable"
- "_isEligibleForWatchAppInstall"
- "_isInternalReleaseType"
- "_isMarketplace"
- "_isMinimumOSVersion:applicableToOSVersion:requiredOS:error:"
- "_isMissingRequiredSINF"
- "_isNew"
- "_isNoLongerCompatible"
- "_isOnDemandInstallCapable"
- "_isOnMountedDiskImage"
- "_isPlaceholder"
- "_isPlaceholderStatusValid"
- "_isResolved"
- "_isSharediPad"
- "_isStagedContainer"
- "_isStagedUpdateContainer:withError:"
- "_isSwiftPlaygroundsApp"
- "_isTransient"
- "_isUpdatedSystemApp"
- "_isWebNotificationBundle"
- "_itemID"
- "_itemIsType:withDescription:atURL:error:"
- "_itemName"
- "_ixDaemonGID"
- "_ixDaemonUID"
- "_ixDataStorageDirectoryPath"
- "_ixDataStorageHomeURLWithError:"
- "_keychainAccessGroupsForApp:error:"
- "_keychainAccessGroupsForBundle:error:"
- "_kind"
- "_label"
- "_launchProhibited"
- "_launchWarningData"
- "_linkedChildBundleIDs"
- "_linkedParentBundleID"
- "_loadSystemDetachedSignatureForBundleID:error:"
- "_localSigningIsUnrestricted"
- "_localizedDistributorName"
- "_location"
- "_locationClassCluster"
- "_lock"
- "_logResourceVerificationErrors"
- "_lsInstallType"
- "_managementDeclarationIdentifier"
- "_markDriverKitExtensionsExecutableInBundle:withError:"
- "_markEAFlag:forAppIdentifier:insecurelyCachedOnBundle:error:"
- "_marketplaceDomain"
- "_marketplaceItemID"
- "_mcmContainer"
- "_md5"
- "_minOSVersion"
- "_mobilePath"
- "_moveItemAtURL:toURL:failIfSrcMissing:error:"
- "_nSimultaneousInstallations"
- "_nameListForPlatformSet:"
- "_nameTranscriptions"
- "_newClass"
- "_oldCompatiblityLinkDestination"
- "_onQueue_addReferencesForBundle:error:"
- "_onQueue_clearIsRunningInTestModeForProcessWithPID:withError:"
- "_onQueue_clearTestFlags:"
- "_onQueue_discoverReferences"
- "_onQueue_refreshPersonaInformationWithError:"
- "_onQueue_removeReferencesForBundle:error:"
- "_onQueue_retrieveSystemAppStateRestoringBackedUpState:"
- "_onQueue_setIsRunningInTestModeForProcessWithPID:withError:"
- "_onQueue_setSystemAppStateList:"
- "_onQueue_setTestFlags:"
- "_onQueue_systemAppStateList"
- "_onQueue_updateReferencesWithOldBundle:newBundle:error:"
- "_operationType"
- "_options"
- "_originalInstallDate"
- "_overlaidInfoPlist"
- "_overlayDictionary:onDictionary:"
- "_owningBundleIdentifier"
- "_parallelPlaceholderURL"
- "_parentBundle"
- "_parentBundleID"
- "_parentBundleURL"
- "_parentIdentifiers"
- "_performOnlineAuthorization"
- "_performWithLaunchPersona:"
- "_personaAttributesMap"
- "_personaGenerationIdentifier"
- "_personaType"
- "_personaUniqueString"
- "_personaUniqueStrings"
- "_personaVolumeUUIDToDaemonContainerMap"
- "_personasRecordMap"
- "_placeholderFailureReason"
- "_placeholderFailureUnderlyingError"
- "_placeholderFailureUnderlyingErrorSource"
- "_platform"
- "_platformHint"
- "_pluginKitBundles"
- "_populateAppExtensionRecordValues:"
- "_populateAppRecordValues:"
- "_populateBundleRecord:error:"
- "_populateBundleRecordValues:signingInfo:error:"
- "_populatePlaceholderRecordValues:signingInfo:"
- "_primaryPersonaUniqueString"
- "_profileValidationType"
- "_protectedMetadata"
- "_purchaseDate"
- "_purchasedRedownload"
- "_purchaserID"
- "_q"
- "_ratingLabel"
- "_ratingRank"
- "_ratingRankEligibilityDomain"
- "_rawContainer"
- "_realPathForURL:allowNonExistentPathComponents:"
- "_realPathWhatExistsInPath:isDirectory:"
- "_redownloadParams"
- "_referrerApp"
- "_referrerURL"
- "_refreshContainerMetadataWithError:"
- "_refs"
- "_relativeStagingBaseDirectory"
- "_releaseDate"
- "_remoteObjectProxyWithErrorHandler:"
- "_removeACLAtPath:isDir:error:"
- "_removeGroupsWithError:error:"
- "_replaceExistingContainer:replacementReason:waitForDeletion:error:"
- "_requireEligibilityChecksForAppsInDevelopment"
- "_rootPath"
- "_runChangeOperationWasLocked:withError:"
- "_runWithLock:"
- "_sandboxEnvironmentForDataContainer:"
- "_sandboxToken"
- "_sanitizeFilePathForVarOrTmpSymlink:error:"
- "_scanAppExtensionsInBundle:inBundleContainer:withError:"
- "_scanAppsDirectory:withError:"
- "_scanBundle:inContainer:addingToBundleSet:enumeratingEntry:withError:"
- "_scanBundleContainersWithClass:withError:ignoredErrorOccurredOnOneOrMoreItems:"
- "_scanExtensionKitDirectory:withError:"
- "_scanExtensionKitLocations:withError:"
- "_scanFrameworkDirectory:withError:"
- "_scanFrameworksLocationsWithError:"
- "_sdkVersion"
- "_sectionName"
- "_serializedContainerRepresentation"
- "_serializedPlaceholderURL"
- "_setBundleParentDirectoryURL:forBundleArray:error:"
- "_setContainer:error:"
- "_setData:forExtendedAttributeNamed:onURL:orFD:error:"
- "_setForEntry:"
- "_shareURL"
- "_sharedConnection"
- "_shortItemName"
- "_shouldUpdateAppExtensionDataContainersWithParentID"
- "_sideLoadedDeviceBasedVPP"
- "_signatureVersion"
- "_signerIdentity"
- "_signerOrganization"
- "_signingInfo"
- "_signingInfoSource"
- "_sinfDataType"
- "_sinfDataTypeIsSet"
- "_sinfInfo"
- "_skipDeviceFamilyCheck"
- "_skipProfileIDValidation"
- "_skipThinningCheck"
- "_softwareVersionBundleID"
- "_softwareVersionExternalIdentifier"
- "_sourceApp"
- "_sourceForPID"
- "_sourceURL"
- "_stageURLByCopying:toItemName:inStagingDir:stagingMode:settingUID:gid:dataProtectionClass:hasSymlink:error:"
- "_stagedSystemAppBundleIDToInfoMap"
- "_stagingContentType"
- "_stagingRoot"
- "_stagingRootClassCluster"
- "_stagingSubsystem"
- "_stashMetadata"
- "_stashOriginalInstallTimestamp"
- "_stashURLForIndex:"
- "_stashedAppRecordForStashedContainer:"
- "_stashedAtTimestamp"
- "_stashedBundleContainerForIndex:error:"
- "_stashedVersions"
- "_staticDiskUsage"
- "_status"
- "_storeCohort"
- "_storefront"
- "_storefrontCountryCode"
- "_subGenres"
- "_supportPageURL"
- "_supportsAppMigration"
- "_synchronousRemoteObjectProxyWithErrorHandler:"
- "_systemAppBundleIDToInfoMap"
- "_systemAppPlaceholderAppExtensionBundleIDs"
- "_systemAppPlaceholderBundleIDToInfoMap"
- "_systemAppPlaceholderBundleIDs"
- "_systemAppPlaceholderXPCServiceBundleIDs"
- "_systemAppPlaceholders"
- "_systemAppStateFromURL:"
- "_systemAppStateList"
- "_systemApps"
- "_systemPersonaUniqueString"
- "_targetDirectoryURL"
- "_targetUID"
- "_teamIdentifier"
- "_testFlags"
- "_testModeQueue"
- "_testModeSentinelURL"
- "_traverseUntilFirstAvailableParentOfURL:withBlock:"
- "_uid"
- "_uniqueInstallID"
- "_unknownArchNameForCPUType:cpuSubtype:"
- "_url"
- "_urls"
- "_userApps"
- "_validateAppNSPrivacyTrackingDomainsWithError:"
- "_validateBundleExecutable:againstStubAt:trustedHashes:sectionName:signingIdentifier:error:"
- "_validateDelegateClassWithError:"
- "_validateExtensions:error:"
- "_validateNSExtensionWithOverlaidDictionary:error:"
- "_validatePresenceOfSwiftEntrySectionInFile:shouldHaveSwiftEntry:withError:"
- "_validateResources"
- "_validateSignatureAndCopyInfoForURL:withOptions:error:"
- "_validateStubSignature:withSigningID:error:"
- "_validateSymlink:withStartingDepth:andEndingDepth:"
- "_validateUsingDetachedSignature"
- "_validateWithError:"
- "_validateXPCServiceWithOverlaidDictionary:error:"
- "_validationOverrideParentBundleID"
- "_variantID"
- "_verifyTrustCachePresence"
- "_volumeDaemonContainer"
- "_volumeUUID"
- "_watchKitAppExecutableHash"
- "_watchKitPlugin"
- "_wk2AppBundle"
- "_wk2AppBundleError"
- "_writeRawiTunesMetadataData:error:"
- "_writeToBundle:error:"
- "_xpcConnection"
- "_xpcServiceBundles"
- "absoluteString"
- "absoluteURL"
- "aclTextFromURL:error:"
- "acquireReferenceforInstalledAppWithIdentity:inDomain:matchingInstallSessionID:completion:"
- "addDataSeparatedAppsWithBundleIDs:toPersona:withCompletion:"
- "addEntriesFromDictionary:"
- "addIdentifier:withState:"
- "addObject:"
- "addObjectsFromArray:"
- "addReferencesForBundle:error:"
- "allAppBundleContainersWithError:"
- "allContainersForAllPersonasForIdentifier:options:error:"
- "allContainersForIdentifier:persona:options:error:"
- "allExtensionKitExtensionsDirectories"
- "allFrameworksDirectories"
- "allKeys"
- "allObjects"
- "allPersonaVolumeDaemonContainersMap"
- "allStagedUpdatesWithCompletion:"
- "allStagingLocationsWithinSubsystem:completion:"
- "allValues"
- "allocWithZone:"
- "allowAdhocSigning"
- "allowDeletableSystemApps"
- "allowPatchWithoutSinf"
- "allowsAppleAppExtensionsNotInExtensionCache"
- "allowsInternalSecurityPolicy"
- "alternateThinningModelIdentifier"
- "appBundleContainerForIdentifier:inDomain:withError:"
- "appBundleContainerForIdentifier:temporary:inDomain:withError:"
- "appBundleContainerWithIdentifier:createIfNeeded:created:error:"
- "appBundleContainerWithIdentifier:forPersona:createIfNeeded:created:error:"
- "appBundleIDsOnAttachedEntityType:"
- "appBundleMetadataItemNames"
- "appBundleURL"
- "appExtensionBundlesPerformingPlatformValidation:withError:"
- "appExtensionBundlesWithError:"
- "appExtensions"
- "appInfoForBundleID:onAttachedEntityType:"
- "appReferencesEnabled"
- "appStateQueue"
- "appendFormat:"
- "appendString:"
- "archNameString"
- "array"
- "arrayByAddingObjectsFromArray:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "attachedContentPathsForEntityType:"
- "autorelease"
- "backedUpStateDirectory"
- "backupSystemAppInstallStateFilePath"
- "bestEffortRollbackSinfData:"
- "bestEffortRollbackiTunesMetadata:error:"
- "boolForKey:"
- "boolValue"
- "builtInAppParallelPlaceholderBundle"
- "builtInApplicationBundleIDs"
- "builtInExtensionKitExtensionsDirectories"
- "builtInFrameworkBundleIDs"
- "bulkSetPropertiesForPath:UID:GID:mode:flags:dataProtectionClass:removeACL:error:"
- "bulkSetPropertiesForPath:withOpenFD:UID:GID:mode:flags:dataProtectionClass:removeACL:error:"
- "bundle"
- "bundleAtURLIsPlaceholder:"
- "bundleContainer"
- "bundleForURL:error:"
- "bundleForURL:platformHint:forceAsPlaceholder:error:"
- "bundleID:isOnAttachedEntityType:"
- "bundleIDs"
- "bundleIDsAssociatedWithPersonaUniqueString:error:"
- "bundleIDsForContainerizedContentWithError:"
- "bundleInfoPlistSupportedPlatforms"
- "bundleIsInDenyList:"
- "bundleMaxLinkedSDKVersion"
- "bundleMetadata"
- "bundleMetadataURL"
- "bundleMetadataWithError:"
- "bundleName"
- "bundleParentDirectoryURL"
- "bundleParentSubdirectory"
- "bundleRecordArrayToInfoDictionaryArray:"
- "bundleRecordWithError:"
- "bundleRecordsForLaunchServicesWithWrapperURL:forBundleIdentifier:withError:"
- "bundleRecordsWithFrameworkURL:options:withError:"
- "bundleSignatureVersionWithError:"
- "bundleType"
- "bundleTypeDescription"
- "bundlesInParentBundle:overrideParentBundleIDForValidation:subDirectory:matchingPredicate:error:"
- "bundlesInParentBundle:subDirectory:matchingPredicate:error:"
- "bytes"
- "cachesDirectory"
- "cancelUpdateForStagedIdentifiers:completion:"
- "captureBundleByMoving:withError:"
- "captureStoreDataFromDirectory:doCopy:failureIsFatal:includeiTunesMetadata:withError:"
- "captureStoreDataFromDirectory:toDirectory:doCopy:failureIsFatal:includeiTunesMetadata:withError:"
- "cfBundle"
- "checkCapabilities:withOptions:completion:"
- "checkCapabilities:withOptions:error:"
- "checkExecutableExistsIfRequiredWithError:"
- "class"
- "clearExtendedAttributesAtURL:error:"
- "clearIsRunningInTestModeForProcessWithPID:withError:"
- "clearPlaceholderStatusForBundle:withError:"
- "clearStagedUpdateContainerStatusWithError:"
- "clearTestFlags:"
- "clearTestFlags:withCompletion:"
- "clearUninstalledIdentifiers:withOptions:completion:"
- "cloneContentFromStashedBundleContainer:error:"
- "cloneItemAtURL:toURL:onBehalfOf:completion:"
- "cloneSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:withCompletion:"
- "code"
- "codeSignatureVerificationState"
- "codeSigningEnforcementIsDisabled"
- "codeSigningInfo"
- "codeSigningInfoByValidatingResources:performingOnlineAuthorization:ignoringCachedSigningInfo:checkingTrustCacheIfApplicable:skippingProfileIDValidation:error:"
- "codeSigningInfoError"
- "codeSigningVerifierForBundle:"
- "companionAppIdentifier"
- "compare:options:"
- "compatibilityLinkDestination"
- "completionBlock"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "conformsToProtocol:"
- "containerForIdentifier:contentClass:forPersona:create:error:"
- "containerWithIdentifier:forPersona:ofContentClass:createIfNeeded:created:error:"
- "containerizedAppBundleRecordsForIdentity:inDomain:options:withError:"
- "containersForBundleIdentifier:contentClass:forPersona:create:fetchTransient:error:"
- "containersForContentClass:forPersona:fetchTransient:error:"
- "containersForGroupIdentifier:forPersona:create:fetchTransient:error:"
- "containersForIdentifier:groupContainerIdentifier:ofContentClass:forPersona:fetchTransient:createIfNeeded:error:"
- "containersWithClass:error:"
- "containersWithClass:personaUniqueString:error:"
- "containsDotDotPathComponents"
- "containsObject:"
- "containsString:"
- "containsValueForKey:"
- "contentProtectionClass"
- "contentsURL"
- "copy"
- "copyItemAtURL:toURL:alwaysClone:error:"
- "copyItemAtURL:toURL:error:"
- "copyItemIfExistsAtURL:toURL:error:"
- "copyItemIgnoringErrorsAtURL:toURL:error:"
- "copyVolumeInfo:forURL:error:"
- "copyWithZone:"
- "coreServices"
- "coreServicesAppBundleIDToInfoMap"
- "coreServicesDirectory"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countForObject:"
- "countOfSlicesWithNamedSection"
- "cpuSubtype"
- "cpuType"
- "createAppSnapshotWithBundleID:snapshotToURL:onlyV1AppIfPresent:placeholderOnly:completion:"
- "createDirectoryAtURL:withIntermediateDirectories:mode:class:error:"
- "createDirectoryAtURL:withIntermediateDirectories:mode:error:"
- "createRelativeDirectoryPath:inBaseDirectory:mode:class:error:"
- "createSafeHarborWithIdentifier:forPersona:containerType:andMigrateDataFrom:completion:"
- "createSymbolicLinkAtURL:withDestinationURL:error:"
- "createTemporaryDirectoryInDirectoryURL:error:"
- "cryptexAppsDirectory"
- "cryptexExtensionKitExtensionsDirectories"
- "cryptexExtensionKitExtensionsDirectory"
- "cryptexFrameworksDirectories"
- "cryptexOSDirectory"
- "currentHandler"
- "currentOSVersionForValidationUsingPlatform:withError:"
- "currentUserCachesDirectory"
- "currentUserDataDirectory"
- "currentUserInstallCoordinationCachesDirectory"
- "currentUserJournalStorageBaseURL"
- "currentUserLaunchServicesOperationLookAsideStorageBaseURL"
- "currentUserLaunchServicesOperationStorageBaseURL"
- "daemonContainerForIdentifier:personaUniqueString:error:"
- "daemonContainerForPersona:error:"
- "daemonUserDataLibraryDirectory"
- "dataContainerClass"
- "dataContainerContentClass"
- "dataContainerCreatingIfNeeded:forPersona:makeLive:created:error:"
- "dataContainerForExecutableBundle:forPersona:createIfNeeded:temporary:created:error:"
- "dataContainerForPersona:error:"
- "dataContainerRootItemNames"
- "dataContainers"
- "dataDirectory"
- "dataForExtendedAttributeNamed:length:fromFD:fdLocation:error:"
- "dataForExtendedAttributeNamed:length:fromURL:error:"
- "dataProtectionChangeOperationForURL:settingClass:changeType:"
- "dataProtectionChangeOperationForURLs:settingClass:changeType:"
- "dataProtectionClass"
- "dataProtectionClassOfItemAtURL:class:error:"
- "dataWithBytes:length:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "dataWithContentsOfURL:options:error:"
- "dataWithLength:"
- "dataWithPropertyList:format:options:error:"
- "date"
- "dateWithTimeIntervalSince1970:"
- "dealloc"
- "debugDescription"
- "debugDescriptionForItemAtURL:"
- "decodeBoolForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultCenter"
- "defaultDirectoriesForContainerType:error:"
- "defaultManager"
- "defaultWorkspace"
- "delegate"
- "delegateMessageDeliveryCompleteWithError:"
- "deleteContainers:waitForDeletion:error:"
- "denormalizedURLForCFBundleURL:"
- "description"
- "destinationOfSymbolicLinkAtURL:error:"
- "developerDirectories"
- "developerRootDirectory"
- "deviceFamilies"
- "deviceForURLOrFirstAvailableParent:error:"
- "deviceHasPersonas"
- "dictionaryRepresentation"
- "dictionaryWithCapacity:"
- "dictionaryWithContentsOfURL:"
- "dictionaryWithContentsOfURL:error:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "dieForTesting"
- "disableSystemAppDeletionCanaryFile"
- "diskUsage"
- "diskUsageForLaunchServicesWithBundleIDs:options:withError:"
- "diskUsageForURL:"
- "displayName"
- "distributorIsFirstPartyApple"
- "distributorIsThirdParty"
- "distributorNameForCurrentLocale"
- "distributorType"
- "driverKitBundlesPerformingPlatformValidation:withError:"
- "driverKitExtensionBundles"
- "driverKitExtensionBundlesWithError:"
- "emergencyOffloadVersion"
- "encodeBool:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encodedData"
- "endTestModeWithCompletion:"
- "enterprisePersonaUniqueString"
- "entryForBundle:inContainer:forPersona:withError:"
- "enumerateAppDictionary:error:"
- "enumerateAppExtensionsInBundle:forPersona:updatingAppExtensionParentID:ensureAppExtensionsAreExecutable:installProfiles:error:enumerator:"
- "enumerateBuiltInSystemContentWithBlock:error:"
- "enumerateContainersWithClass:forPersona:isTransient:identifiers:groupIdentifiers:usingBlock:"
- "enumerateCryptexContentWithBlock:error:"
- "enumerateDylibsWithBlock:"
- "enumerateExtendedAttributeNamesAtURL:includeCompression:error:enumerator:"
- "enumerateExternalVolumesWithBlock:"
- "enumerateInstalledAppsWithOptions:completion:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateURLsForItemsInDirectoryAtURL:ignoreSymlinks:withBlock:"
- "enumerator"
- "erroneousContainerCleanupDone"
- "error"
- "errorOccurred:"
- "errorWithDomain:code:userInfo:"
- "estimatedAvailableMemoryForValidation"
- "estimatedMemoryUsageToValidate"
- "exExtensionPointIdentifier"
- "executableImageSlices"
- "executableImageSlicesWithError:"
- "executableName"
- "executablePlatformsWithError:"
- "executableURL"
- "extendedAttributesFromURL:error:"
- "extendedAttributesFromURL:includeCompression:error:"
- "extensionAttributes"
- "extensionCacheEntry"
- "extensionCacheEntryWithError:"
- "extensionHandle"
- "extensionKitBundles"
- "extensionKitBundlesPerformingPlatformValidation:withError:"
- "extensionKitBundlesWithError:"
- "extensionPoint"
- "extensionPointForIdentifier:platform:"
- "extensionPointIdentifier"
- "failWithError:"
- "fairPlaySinfInfoWithError:"
- "fd"
- "fetchDiskUsageForIdentifiers:withOptions:completion:"
- "fetchInfoForBundle:forPersona:inContainer:withError:"
- "fetchInfoForContainerizedAppWithIdentity:inDomain:options:completion:"
- "fetchInfoForFrameworkAtURL:options:completion:"
- "fetchListOfAppsRequiringPreInstallConsent:"
- "fileHandleForReadingFromURL:error:"
- "fileSystemRepresentation"
- "fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "fileURLWithPathComponents:"
- "finalizeReference:completion:"
- "finalizeStagedInstallForIdentifier:returningResultInfo:completion:"
- "finishDecoding"
- "firstObject"
- "firstObjectCommonWithArray:"
- "frameworkBundles"
- "frameworkBundlesWithError:"
- "frameworks"
- "fstat of %@ failed: %s"
- "fullFidelityIconsEnabled"
- "gatherOptions"
- "getAppMetadataForApp:completion:"
- "getBytes:length:"
- "getIsBuiltForMacPlatform:error:"
- "getIsBuiltForiOSPlatform:error:"
- "getMayTargetThirdPartyExtensionPoint:withError:"
- "getPidForTestingWithCompletion:"
- "getSinfDataType:withError:"
- "getTestModeWithCompletion:"
- "getValue:forEntitlement:fromProcessWithAuditToken:error:"
- "gid"
- "groupContainerURLsForBundleIdentifier:forPersona:error:"
- "groupContainerWithIdentifier:forPersona:createIfNeeded:error:"
- "handleFailureInFunction:file:lineNumber:description:"
- "hasEAPFSVolumeSplit"
- "hasExecutable"
- "hasExecutableSliceForCPUType:subtype:error:"
- "hasExecutableSliceForPlatform:error:"
- "hasInternalContent"
- "hasNamedSection"
- "hasNoConflictsWithOtherInstalledEntitiesForSigningInfo:forPersona:error:"
- "hasOnlyAllowedWatchKitAppInfoPlistKeysForWatchKitVersion:error:"
- "hasPrefix:"
- "hasSerializedPlaceholder"
- "hasSinf"
- "hasWatchCustomNotification"
- "hasWatchGlance"
- "hash"
- "hashTableWithOptions:"
- "hashes"
- "haveUpdatedAppExtensionDataContainersWithParentID"
- "helperLogDirectory"
- "helperServiceJetsamLimit"
- "i16@0:8"
- "i24@0:8@?16"
- "i32@0:8@16@?24"
- "i32@0:8@16^@24"
- "iTunesMetadata"
- "iTunesMetadataURL"
- "iTunesMetadataWithError:"
- "identityByChangingLocation:"
- "identityForUpdateOfBundle:error:"
- "ignoreErrors"
- "infoDictionaryArrayToBundleRecordArray:"
- "infoForLaunchServicesWithWrapperURL:forBundleIdentifier:withError:"
- "infoPlistHashWithError:"
- "infoPlistSubset"
- "infoPlistURL"
- "infoValueForKey:error:"
- "init"
- "initForReadingFromData:error:"
- "initForTesting"
- "initFromPlistDictionary:error:"
- "initInternal"
- "initRequiringSecureCoding:"
- "initWithAppBundleURL:error:"
- "initWithAppBundleURLInternal:"
- "initWithAppExtensionBundle:inBundleIdentifier:dataContainer:"
- "initWithAppExtensionBundle:inBundleIdentifier:dataContainers:"
- "initWithBase64EncodedString:options:"
- "initWithBundle:"
- "initWithBundle:dataContainer:"
- "initWithBundle:dataContainers:"
- "initWithBundleContainer:dataContainer:"
- "initWithBundleContainer:dataContainers:"
- "initWithBundleContainer:forPersona:"
- "initWithBundleContainer:forPersonas:"
- "initWithBundleID:"
- "initWithBundleID:persona:"
- "initWithBundleID:personaUniqueString:location:"
- "initWithBundleIdentifier:personaUniqueString:"
- "initWithBundleIdentifier:personaUniqueString:location:"
- "initWithBundleInContainer:withExtension:error:"
- "initWithBundleInDirectory:withExtension:error:"
- "initWithBundleParentURL:parentSubdirectory:bundleName:error:"
- "initWithBundleParentURL:parentSubdirectory:bundleName:platformHint:forceAsPlaceholder:error:"
- "initWithBundleURL:error:"
- "initWithBundleURL:platformHint:forceAsPlaceholder:error:"
- "initWithBytes:length:encoding:"
- "initWithCPUType:cpuSubtype:platform:sdkVersion:minOSVersion:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithContainer:"
- "initWithContainer:error:"
- "initWithContainerURL:"
- "initWithContainerURL:expectAppWithin:error:"
- "initWithContentsOfURL:options:error:"
- "initWithData:encoding:"
- "initWithDictionary:"
- "initWithDictionaryRepresentation:"
- "initWithDictionaryRepresentation:fromSource:"
- "initWithDomain:code:userInfo:"
- "initWithExecutable:searchForSectionNamed:"
- "initWithFormat:"
- "initWithFormat:arguments:"
- "initWithGenre:genreID:"
- "initWithLegacyRecordDictionary:"
- "initWithLegacySinfInfoDictionary:"
- "initWithMachServiceName:options:"
- "initWithObjects:"
- "initWithOptions:enumerator:"
- "initWithOptions:personaUniqueString:enumerator:"
- "initWithParentBundle:parentSubdirectory:bundleName:platformHint:forceAsPlaceholder:error:"
- "initWithPersonaString:personaType:associatedBundleIDs:volumeDaemonContainer:volumeDaemonContainerSandboxExtension:"
- "initWithScanOptions:"
- "initWithScanOptions:personaUniqueString:"
- "initWithSerializedContainer:matchingWithOptions:error:"
- "initWithServiceName:"
- "initWithSessionID:uniqueID:"
- "initWithSignerIdentity:signerOrganization:codeInfoIdentifier:teamIdentifier:signatureVersion:entitlements:signerType:profileType:signingInfoSource:launchWarningData:"
- "initWithStagingRoot:relativeStagingBaseDirectory:"
- "initWithStagingSubsystem:contentType:"
- "initWithSuiteName:"
- "initWithTargetDirectoryURL:error:"
- "initWithTargetDirectoryURLInternal:"
- "initWithTargetUID:"
- "initWithToken:options:error:"
- "initWithURLs:newClass:changeType:"
- "initWithUUIDBytes:"
- "initWithVolumeUUID:stagingSubsystem:"
- "insecureCachedAppIdentifierIfAppClipForBundle:error:"
- "insecureCachedAppIdentifierIfValidatedByFreeProfileForBundle:error:"
- "installCoordinationStagingWithError:"
- "installEmbeddedProvisioningProfileWithProgress:"
- "installMacStyleEmbeddedProvisioningProfileWithProgress:"
- "installParallelPlaceholderForStagedIdentifier:fromURL:returningResultInfo:completion:"
- "installQOSOverride"
- "installSessionIDEAName"
- "installTypeFromExtendedAttributeOnBundle:error:"
- "installURL:identity:targetingDomain:options:returningResultInfo:completion:"
- "installableIfAppleAppExtensionsNotInExtensionCache"
- "installationDenylist"
- "installationIdentity"
- "installationIdentityForBundle:settingIfNotSet:error:"
- "installationIdentitySettingIfNotSet:withError:"
- "installcoordinationdPath"
- "installcoordinationdUserDataLibraryDirectory"
- "installdJetsamLimit"
- "installdLibraryPath"
- "installdPath"
- "installsAppleAppExtensionsNotInExtensionCache"
- "intValue"
- "integerForKey:"
- "interfaceWithProtocol:"
- "internalAppBundleIDToInfoMap"
- "internalApps"
- "internalAppsDirectory"
- "internalExtensionKitExtensionsDirectory"
- "internalFrameworksRootDirectory"
- "internalQueue"
- "internalRootDirectory"
- "invalidate"
- "invalidateCache"
- "invalidateReference:completion:"
- "isAppTypeBundle"
- "isApplicableToCurrentDeviceCapabilitiesWithError:"
- "isApplicableToCurrentDeviceFamilyWithError:"
- "isApplicableToCurrentOSVersionWithError:"
- "isApplicableToKnownWatchOSVersion"
- "isApplicableToOSVersion:error:"
- "isApplicableToOSVersionEarlierThan:"
- "isCompatibleWithDeviceFamily:"
- "isDataContainerEmpty:ofContainerType:completion:"
- "isEnterprisePersona"
- "isEqual:"
- "isEqualToData:"
- "isEqualToLocationSystemDefinedBase:"
- "isEqualToSet:"
- "isEqualToString:"
- "isEqualWithLocationSystemDefinedCommon:"
- "isEqualWithLocationUserDefined:"
- "isEqualWithLocationUserDefinedDirectory:"
- "isExtensionBasedWatchKitApp"
- "isExtensionlessWatchKitApp"
- "isFileProviderNonUIExtension"
- "isGameCenterEnabled"
- "isGrandfatheredNonContainerizedForSigningInfo:"
- "isKindOfClass:"
- "isKnownPersonaUniqueString:error:"
- "isLaunchProhibited"
- "isMapsGeoServicesExtension"
- "isMemberOfClass:"
- "isMessagePayloadProviderExtension"
- "isMinimumOSVersion:applicableToOSVersion:error:"
- "isNew"
- "isPersonalPersona"
- "isPlaceholderStatusValid"
- "isProxy"
- "isPurchasedRedownload"
- "isRemovableSystemApp"
- "isRestackingEnabled"
- "isRunningInTestMode:outError:"
- "isSharedIPad"
- "isSharediPad"
- "isSiriIntentsExtension"
- "isSiriIntentsUIExtension"
- "isStagedContainer"
- "isStaticContent"
- "isSubsetOfSet:"
- "isSystemPersona"
- "isWatchApp"
- "isWatchKitExtension"
- "isWatchOnlyApp"
- "itemDoesNotExistAtURL:"
- "itemDoesNotExistOrIsNotDirectoryAtURL:"
- "itemExistsAtURL:"
- "itemExistsAtURL:error:"
- "itemIsDirectoryAtURL:error:"
- "itemIsFIFOAtURL:error:"
- "itemIsFileAtURL:error:"
- "itemIsSocketAtURL:error:"
- "itemIsSymlinkAtURL:error:"
- "ixDaemonGID"
- "ixDaemonUID"
- "ixDataStorageDirectoryPath"
- "journalStorageBaseURL"
- "kern.grade_cputype"
- "lastBuildInfoFileURL"
- "lastPathComponent"
- "launchServicesOperationLookAsideStorageBaseURL"
- "launchServicesOperationStorageBaseURL"
- "launchWarningData"
- "legacyDictionary"
- "legacyRecordDictionary"
- "legacySinfInfoDictionary"
- "length"
- "linkedBundleIDsForAppIdentity:withCompletion:"
- "listAllPersonaAttributesWithError:"
- "listAllPersonaWithAttributes"
- "listSafeHarborsOfType:forPersona:withOptions:completion:"
- "localSigningIsUnrestricted"
- "locationFromPlistDictionary:error:"
- "lock"
- "logAccessPermissionsForURL:"
- "logDirectory"
- "logResourceVerificationErrors"
- "longValue"
- "lookupSystemAppStateWithOptions:completion:"
- "lookupUninstalledWithOptions:completion:"
- "lsInstallTypeWithError:"
- "makeAndSetNewInstallationIdentityWithError:"
- "makeContainerLiveReplacingContainer:reason:waitForDeletion:withError:"
- "makeContainerLiveWithError:"
- "makeExecutableWithError:"
- "makeSymlinkFromAppDataContainerToBundleForIdentifier:forPersona:completion:"
- "makeSymlinkToBundleInContainerIfNeeded:"
- "markBundleAsPlaceholder:withError:"
- "markContainerAsStagedUpdateWithError:"
- "maxLinkedSDKVersion"
- "mayContainAppExtensions"
- "mayContainFrameworks"
- "mayHaveExecutableProgram"
- "mcmContainer"
- "metadataForBundleContainerURL:error:"
- "metadataFromDictionary:"
- "metadataFromPlistAtURL:error:"
- "metadataFromPlistData:error:"
- "metadataFromURL:error:"
- "migrateMobileContentWithCompletion:"
- "migrationPlistURL"
- "minOSVersion"
- "minimumOSVersion"
- "minimumWatchOSVersionIsPreV6"
- "mobilePath"
- "modificationDateForURL:error:"
- "mountPointForURL:error:"
- "mountPointForVolumeUUID:error:"
- "moveItemAtURL:toURL:error:"
- "moveItemIfExistsAtURL:toURL:error:"
- "moveItemInStagingLocation:atRelativePath:toDestinationURL:onBehalfOf:completion:"
- "multiPersonaSADAppBundleIDsWithError:"
- "mutableBytes"
- "mutableCopy"
- "nSimultaneousInstallations"
- "needsDataContainer"
- "needsSinf"
- "new"
- "newClass"
- "newIdentityForBundle:"
- "newStashMetadata"
- "nsExtensionPointIdentifier"
- "null"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectAtIndexedSubscript:"
- "objectEnumerator"
- "objectForKeyedSubscript:"
- "oldArchiveDirectory"
- "oldDataDirectoryPath"
- "oldLoggingPath"
- "onlyHasExecutableSlicesForPlatform:error:"
- "operationType"
- "options"
- "overlaidInfoPlist"
- "overlaidInfoPlistWithError:"
- "owningBundleIdentifier"
- "packedNumberForCPUType:subtype:"
- "parentBundle"
- "parentBundleID"
- "parentBundleURL"
- "parse_macho_iterate_slices failed for %s"
- "path"
- "pathComponents"
- "pathExtension"
- "pathWithComponents:"
- "performChangeOperation"
- "performGatherWithError:"
- "performHashWithError:"
- "performOnlineAuthorization"
- "performScanWithError:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performValidationWithError:"
- "personaAttributesMap"
- "personaForBundleID:error:"
- "personaGenerationIdentifier"
- "personaGenerationIdentifierWithError:"
- "personaLayoutPathURL"
- "personaType"
- "personaTypeForPersonaUniqueString:"
- "personaUniqueStrings"
- "personaUniqueStringsForAppWithBundleID:error:"
- "personaVolumeDaemonContainerForUUID:"
- "personaVolumeUUIDToDaemonContainerMap"
- "platform"
- "platformHint"
- "plistDictionary"
- "plistDictionaryFromLocation:"
- "plistTypeName"
- "plugInsDirectoryURL"
- "pluginDataContainerWithIdentifier:forPersona:createIfNeeded:created:error:"
- "pluginKitBundles"
- "pluginKitBundlesPerformingPlatformValidation:withError:"
- "pluginKitBundlesWithError:"
- "pluginKitPluginBundleContainerWithIdentifier:createIfNeeded:created:error:"
- "postNotificationName:object:userInfo:options:"
- "primaryPersonaString"
- "primaryPersonaUniqueString"
- "privateAppBundleContainerWithIdentifier:createIfNeeded:created:error:"
- "privateTempAppBundleContainerWithIdentifier:error:"
- "privilegedResolveRootWithError:"
- "propertyListDataWithError:"
- "propertyListWithData:options:format:error:"
- "purgeContentWithError:"
- "purgeTransientBundleContainersWithError:"
- "q16@0:8"
- "raise:format:"
- "raiseExceptionWithCompletion:"
- "rawContainer"
- "reScanCoreServicesApps"
- "reScanInternalApps"
- "reScanSystemApps"
- "readDataUpToLength:error:"
- "realPathForURL:allowNonExistentPathComponents:isDirectory:error:"
- "realPathForURL:ifChildOfURL:"
- "reclaimDiskSpaceWithError:"
- "reconcile"
- "reconcileContentsOnKnownOSModules:completion:"
- "recreateDefaultStructureWithError:"
- "referenceStorageURL"
- "referencesForBundleWithIdentifier:inDomain:completion:"
- "refs"
- "regenerateDirectoryUUIDWithError:"
- "registerContentsForDiskImageAtURL:completion:"
- "registerContentsOnOSModuleAtURL:completion:"
- "registerContentsOnRoot:deferUntilNextBoot:completion:"
- "registerPlaceholderForReference:completion:"
- "registerSafeHarborAtPath:forIdentity:ofType:withOptions:completion:"
- "relativeExecutablePath"
- "relativePath"
- "release"
- "releaseTerminationAssertion"
- "remoteObjectProxyWithErrorHandler:"
- "removeContainers:waitForDeletion:error:"
- "removeDataSeparatedAppsWithBundleIDs:fromPersona:withCompletion:"
- "removeExtendedAttributeNamed:fromURL:error:"
- "removeIdentifiers:"
- "removeItemAtURL:error:"
- "removeItemAtURL:keepParent:error:"
- "removeLastObject"
- "removeObject:"
- "removeObjectForKey:"
- "removeObjectsForKeys:"
- "removeReferencesForBundle:error:"
- "removeSafeHarborForIdentity:ofType:withOptions:completion:"
- "removeSinf"
- "removeUnderlyingContainerWaitingForDeletion:error:"
- "replaceExistingContainer:error:"
- "replicateRootSinfWithError:"
- "reportProgress:"
- "requireEligibilityChecksForAppsInDevelopment"
- "resolvePersonaUsingModuleSpecificLogicWithError:"
- "resolvePersonaWithError:"
- "resolveRootWithError:"
- "resolveStagingBaseWithSandboxExtension:forVolumeUUID:withinStagingSubsystem:error:"
- "resolveStagingBaseWithSandboxExtensionForVolumeUUID:withinStagingSubsystem:completion:"
- "resolveWithError:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "revertIdentity:withOptions:completion:"
- "roleUserMigrationMarkerFilePath"
- "rootPath"
- "rootSinfURL"
- "rootSupfURL"
- "rootSuppURL"
- "sandboxToken"
- "saveBundleMetadata:withError:"
- "saveStashMetadata:withError:"
- "scanAppExtensionsInFrameworkBundle:withError:"
- "scanExecutableBundle:inContainer:forPersona:withError:"
- "sdkBuildVersion"
- "sdkBuildVersionIsAtLeast:"
- "sdkVersion"
- "sectionName"
- "secureRenameFromSourceURL:toDestinationURL:destinationStatus:error:"
- "self"
- "serializeToURL:error:"
- "setAccountID:"
- "setAllowAdhocSigning:"
- "setAltDSID:"
- "setAlternateIconName:"
- "setAppClipAppIdentifier:insecurelyCachedOnBundle:error:"
- "setAppManagementDomain:"
- "setAppleID:"
- "setApplicationDSID:"
- "setApplicationType:"
- "setArchNameString:"
- "setArtistName:"
- "setAssetToken:"
- "setAutoInstallOverride:"
- "setBetaBuildGroupID:"
- "setBetaExternalVersionIdentifier:"
- "setBetaTesterType:"
- "setBool:forKey:"
- "setBundleContainer:"
- "setBundleContainerURL:"
- "setBundleID:"
- "setBundleIdentifier:"
- "setBundleIdentifiers:forPersonaUniqueString:error:"
- "setBundleIdentifiers:forPersonaWithPersonaUniqueString:withError:"
- "setBundleMetadata:"
- "setBundleParentDirectoryURL:error:"
- "setBundleShortVersion:"
- "setBundleShortVersionString:"
- "setBundleURL:"
- "setBundleVersion:"
- "setByAddingObject:"
- "setByAddingObjectsFromSet:"
- "setCategories:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCodeInfoIdentifier:"
- "setCodeSignerType:"
- "setCodeSigningInfo:"
- "setCodeSigningInfoError:"
- "setCodeSigningInfoNotAuthoritative:"
- "setCompatibilityState:"
- "setCompletionBlock:"
- "setContainerClass:"
- "setContainerURL:"
- "setContentProtectionClass:"
- "setCountOfSlicesWithNamedSection:"
- "setCounterpartIdentifiers:"
- "setCpuSubtype:"
- "setCpuType:"
- "setDSPersonID:"
- "setData:forExtendedAttributeNamed:onFD:fdLocation:error:"
- "setData:forExtendedAttributeNamed:onURL:error:"
- "setDataContainerURL:"
- "setDataProtectionClassOfItemAtURL:toClass:ifPredicate:error:"
- "setDataProtectionOnDataContainer:forNewBundle:retryIfLocked:"
- "setDataSeparatedAppsWithBundleIDs:withPersona:withCompletion:"
- "setDateOriginallyInstalled:"
- "setDateStashed:"
- "setDelegate:"
- "setDeveloperID:"
- "setDeveloperName:"
- "setDeviceBasedVPP:"
- "setDiskUsage:"
- "setDistributorID:"
- "setDistributorInfo:"
- "setDomain:"
- "setDownloaderDSID:"
- "setDownloaderID:"
- "setDriverKitExtensionBundles:"
- "setDriverKitExtensionURLs:"
- "setEligibilityTestOverrides:withCompletion:"
- "setEnterpriseInstallURL:"
- "setEnterprisePersonaUniqueString:"
- "setEntitlements:"
- "setEnvironmentVariables:"
- "setErroneousContainerCleanupDone:"
- "setError:"
- "setExecutableImageSlices:"
- "setExtensionCacheEntry:"
- "setExtensionHandle:"
- "setExtensionKitBundles:"
- "setExtensionOwnerBundleID:"
- "setExtensionPoint:"
- "setFactoryInstall:"
- "setFamilyID:"
- "setFd:"
- "setFrameworkBundles:"
- "setGameCenterEnabled:"
- "setGameCenterEverEnabled:"
- "setGenre:"
- "setGenreID:"
- "setGroupContainerURLs:"
- "setGroupContainers:"
- "setHasAppGroupContainers:"
- "setHasMIDBasedSINF:"
- "setHasMessagesExtension:"
- "setHasOrEverHasHadIAP:"
- "setHasParallelPlaceholder:"
- "setHasSettingsBundle:"
- "setHasSystemContainer:"
- "setHasSystemGroupContainers:"
- "setHaveUpdatedAppExtensionDataContainersWithParentID:"
- "setIAdAttribution:"
- "setIAdConversionDate:"
- "setIAdImpressionDate:"
- "setITunesMetadata:"
- "setIdentifier:"
- "setIdentity:"
- "setIgnoreErrors:"
- "setInfoPlistSubsetForTesting:"
- "setInfoValue:forKey:error:"
- "setInitialODRSize:"
- "setInstallBuildVersion:"
- "setInstallDate:"
- "setInstallSessionID:"
- "setInstallType:"
- "setInstallType:inExtendedAttributeOnBundle:error:"
- "setInstallationIdentity:"
- "setInstallerEpoch:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsAutoDownload:"
- "setIsB2BCustomApp:"
- "setIsBeta:"
- "setIsContainerized:"
- "setIsDeletable:"
- "setIsEligibleForWatchAppInstall:"
- "setIsMarketplace:"
- "setIsMissingRequiredSINF:"
- "setIsNoLongerCompatible:"
- "setIsOnDemandInstallCapable:"
- "setIsOnMountedDiskImage:"
- "setIsPlaceholder:"
- "setIsPlaceholderStatusValid:"
- "setIsPlaceholderWithError:"
- "setIsResolved:"
- "setIsRunningInTestModeForProcessWithPID:withError:"
- "setIsStagedContainer:"
- "setIsSwiftPlaygroundsApp:"
- "setIsTransient:"
- "setIsUpdatedSystemApp:"
- "setIsWebNotificationBundle:"
- "setItemID:"
- "setItemName:"
- "setKind:"
- "setLabel:"
- "setLaunchProhibited:"
- "setLaunchWarningData:withError:"
- "setLaunchWarningForApp:withUniqueInstallIdentifier:warningData:completion:"
- "setLinkedChildBundleIDs:"
- "setLinkedParentBundleID:"
- "setLocalizedDistributorName:"
- "setLocation:"
- "setLogResourceVerificationErrors:"
- "setLsInstallType:"
- "setManagementDeclarationIdentifier:"
- "setMarketplaceDomain:"
- "setMarketplaceItemID:"
- "setMd5:"
- "setMinOSVersion:"
- "setModificationDateToNowForURL:error:"
- "setNameTranscriptions:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOriginalInstallDate:"
- "setOverlaidInfoPlist:"
- "setOwnerOfURL:toUID:gid:error:"
- "setOwnershipAtURL:toUID:gid:error:"
- "setParallelPlaceholderURL:"
- "setParentBundleID:"
- "setParentIdentifiers:"
- "setPerformOnlineAuthorization:"
- "setPermissionsForURL:toMode:error:"
- "setPersonaAttributesMap:"
- "setPersonaGenerationIdentifier:"
- "setPersonaUniqueString:"
- "setPersonaVolumeUUIDToDaemonContainerMap:"
- "setPersonasRecordMap:"
- "setPlaceholderFailureReason:"
- "setPlaceholderFailureUnderlyingError:"
- "setPlaceholderFailureUnderlyingErrorSource:"
- "setPlatform:"
- "setPluginKitBundles:"
- "setPrimaryPersonaUniqueString:"
- "setProfileValidationType:"
- "setProtectedMetadata:"
- "setPurchaseDate:"
- "setPurchasedRedownload:"
- "setPurchaserID:"
- "setRatingLabel:"
- "setRatingRank:"
- "setRatingRankEligibilityDomain:"
- "setRedownloadParams:"
- "setReferrerApp:"
- "setReferrerURL:"
- "setRefs:"
- "setRelativeStagingBaseDirectory:"
- "setReleaseDate:"
- "setRemoteObjectInterface:"
- "setSdkVersion:"
- "setSerializedPlaceholderURL:"
- "setShareURL:"
- "setShortItemName:"
- "setSideLoadedDeviceBasedVPP:"
- "setSignatureVersion:"
- "setSignerIdentity:"
- "setSignerOrganization:"
- "setSinfDataType:"
- "setSinfDataType:withError:"
- "setSinfDataTypeIsSet:"
- "setSinfInfo:"
- "setSkipProfileIDValidation:"
- "setSoftwareVersionBundleID:"
- "setSoftwareVersionExternalIdentifier:"
- "setSourceApp:"
- "setSourceForPID:"
- "setSourceURL:"
- "setStashMetadata:"
- "setStashOriginalInstallTimestamp:"
- "setStashedAtTimestamp:"
- "setStashedVersions:"
- "setStaticDiskUsage:"
- "setStatus:"
- "setStoreCohort:"
- "setStorefront:"
- "setStorefrontCountryCode:"
- "setSubGenres:"
- "setSupportPageURL:"
- "setSupportsAppMigration:"
- "setSystemAppMigrationComplete:"
- "setSystemAppPlaceholderBundleIDToInfoMap:"
- "setSystemAppStateList:"
- "setSystemPersonaUniqueString:"
- "setTargetUID:"
- "setTeamIdentifier:"
- "setTestFlags:"
- "setTestFlags:withCompletion:"
- "setTestModeForIdentifierPrefix:testMode:validationData:"
- "setTestModeQueue:"
- "setTestModeWithCompletion:"
- "setTestingEnabled:"
- "setUniqueInstallID:"
- "setValidateResources:"
- "setValidateUsingDetachedSignature:"
- "setValidatedByFreeProfileAppIdentifier:insecurelyCachedOnBundle:error:"
- "setValidationOverrideParentBundleID:"
- "setVariantID:"
- "setVerifyTrustCachePresence:"
- "setWatchKitAppExecutableHash:"
- "setWatchKitPlugin:"
- "setWithArray:"
- "setWithCapacity:"
- "setWithObject:"
- "setWithObjects:"
- "setWk2AppBundle:"
- "setWk2AppBundleError:"
- "setXpcConnection:"
- "setXpcServiceBundles:"
- "sharedInstance"
- "sharedList"
- "sharedManager"
- "sharedTracker"
- "shouldHaveCorrespondingDataContainer"
- "shouldUpdateAppExtensionDataContainersWithParentID"
- "signingIdentifierForAuditToken:error:"
- "signingInfo"
- "signingInfoSource"
- "sinfDataType"
- "sinfDataTypeIsSet"
- "siriIntents"
- "skipDeviceFamilyCheck"
- "skipProfileIDValidation"
- "skipThinningCheck"
- "snapshotWKAppInCompanionAppID:toURL:options:completion:"
- "sourceForPID"
- "stageInstallURL:identity:targetingDomain:withOptions:completion:"
- "stageItemAtURL:toStagingLocation:options:completion:"
- "stageURL:toItemName:inStagingDir:stagingMode:settingUID:gid:hasSymlink:error:"
- "stageURLByMoving:toItemName:inStagingDir:settingUID:gid:dataProtectionClass:breakHardlinks:hasSymlink:error:"
- "stagedSystemAppBundleIDToInfoMap"
- "stagedSystemAppsDirectory"
- "stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:completion:"
- "stagingLocationForSystemContentWithinSubsystem:completion:"
- "stagingLocationForURL:withinStagingSubsytem:usingUniqueName:completion:"
- "stagingLocationForUserContentWithinSubsystem:completion:"
- "stagingURLWithSandboxExtension:forSystemContentWithinSubsystem:error:"
- "stagingURLWithSandboxExtension:forUserContentWithinSubsystem:error:"
- "stagingURLWithSandboxExtensionForSystemContentWithinSubsystem:completion:"
- "stagingURLWithSandboxExtensionForUserContentWithinSubsystem:completion:"
- "standardInfoMapInfoPlistKeys"
- "standardizeOwnershipAtURL:toUID:GID:removeACLs:setProtectionClass:foundSymlink:error:"
- "stashBaseURL"
- "stashBundleContainerContents:error:"
- "stashMetadata"
- "stashMetadataURL"
- "stashMetadataWithError:"
- "stashedBundleContainerWithError:"
- "status"
- "storeListOfAppsRequiringPreInstallConsent:completion:"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringByDeletingLastPathComponent"
- "stringForKey:"
- "stringWithCString:encoding:"
- "stringWithFileSystemRepresentation:"
- "stringWithFileSystemRepresentation:length:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "subarrayWithRange:"
- "substringFromIndex:"
- "superclass"
- "supportedDevices"
- "supportsSecureCoding"
- "switchingPersonasEnabled"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "systemAppBundleIDToInfoMap"
- "systemAppDeletionEnabled"
- "systemAppDetachedSignaturesDirectory"
- "systemAppInstallStateFilePath"
- "systemAppMigratorHasCompleted:"
- "systemAppPlaceholderAppExtensionBundleIDs"
- "systemAppPlaceholderBundleIDToInfoMap"
- "systemAppPlaceholderBundleIDs"
- "systemAppPlaceholderXPCServiceBundleIDs"
- "systemAppPlaceholders"
- "systemAppPlaceholdersDirectory"
- "systemAppStateDictionaryRestoringBackedUpState:"
- "systemAppStateList"
- "systemApps"
- "systemAppsDirectory"
- "systemDeveloperRootDirectory"
- "systemExtensionKitExtensionsDirectory"
- "systemFrameworksRootDirectory"
- "systemPersonaUniqueString"
- "targetsAppleExtensionPoint"
- "targetsBrowserContentExtensionPoint"
- "targetsBrowserExtensionPoint"
- "targetsBrowserNetworkingExtensionPoint"
- "targetsBrowserRenderingExtensionPoint"
- "targetsDevelopmentOnlyBrowserExtensionPoint"
- "tempAppBundleContainerWithIdentifier:error:"
- "tempAppBundleContainerWithIdentifier:inDomain:withError:"
- "tempContainerWithIdentifier:forPersona:ofContentClass:error:"
- "tempPluginKitPluginBundleContainerWithIdentifier:error:"
- "testFileSentinelForSyncURL"
- "testFlags"
- "testFlagsAreSet:"
- "testModeQueue"
- "thinningMatchesCurrentDeviceWithError:"
- "thisBundleAndAllContainedBundlesWithError:"
- "transferExistingStashesFromContainer:error:"
- "transferInstallationIdentityFromBundle:error:"
- "transferOwnershipOfSandboxExtensionToCaller"
- "transientBundleCleanupEnabled"
- "transientContainerForIdentifier:contentClass:forPersona:create:error:"
- "traverseDirectoryAtURL:withBlock:"
- "triggerRegistrationForContainerizedContentForOptions:withCompletion:"
- "triggerRegistrationForContainerizedContentWithOptions:completion:"
- "triggerRegistrationForContainerizedContentWithOptions:withError:"
- "triggerRegistrationForDiskImageContentForOptions:withCompletion:"
- "triggerRegistrationForDiskImageContentWithOptions:completion:"
- "uid"
- "uninstallIdentifiers:withOptions:completion:"
- "uninstallIdentity:withOptions:completion:"
- "uninstallRecordArrayToDictionary:"
- "unionSet:"
- "uniqueInstallIDEAName"
- "unknownArchNameStringForArchName:"
- "unpackPackedCpuTypeAndSubType:cputype:subtype:"
- "unregisterContentsForDiskImageAtURL:completion:"
- "unregisterContentsOnOSModuleAtURL:completion:"
- "unregisterContentsOnRoot:deferUntilNextBoot:completion:"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "upToFirstFourBytesFromURL:error:"
- "updateAndValidateSinf:error:"
- "updateAndValidateSinf:withRollback:error:"
- "updateMCMWithCodeSigningInfoAsAdvanceCopy:withError:"
- "updatePlaceholderMetadataForApp:installType:failureReason:underlyingError:failureSource:completion:"
- "updateReferencesWithOldBundle:newBundle:error:"
- "updateSinfForIXWithIdentifier:withOptions:sinfData:completion:"
- "updateSinfWithData:error:"
- "updateSystemAppStateForIdentifier:appState:completion:"
- "updateiTunesMetadata:forAppWithIdentifier:error:"
- "updateiTunesMetadataForIXWithIdentifier:metadata:completion:"
- "url"
- "urls"
- "urlsForItemsInDirectoryAtURL:ignoringSymlinks:error:"
- "userApps"
- "userInfo"
- "userPersonaBundleIDList"
- "userPersonaType"
- "userPersonaUniqueString"
- "v16@0:8"
- "v16@?0Q8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8i16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSSet\"@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8@?<v@?i>16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v24@?0@\"ICLBundleRecord\"8@\"NSError\"16"
- "v28@0:8@16i24"
- "v32@0:8@\"ICLRegistrationOptions\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"MIAppIdentity\"16@?<v@?@\"NSSet\"@\"NSError\">24"
- "v32@0:8@\"MIAppReference\"16@?<v@?@\"LSRecordPromise\"@\"NSError\">24"
- "v32@0:8@\"MIAppReference\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@\"NSError\"24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSSet\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSSet\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"MIBundleMetadata\"@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSUUID\"@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?@\"MIStagingLocation\"@\"NSError\">24"
- "v32@0:8Q16@?<v@?@\"NSError\">24"
- "v32@0:8Q16@?<v@?@\"NSSet\"@\"NSError\">24"
- "v32@0:8Q16@?<v@?@\"NSURL\"@\"NSString\"@\"NSError\">24"
- "v36@0:8@\"NSSet\"16B24@?<v@?@\"NSError\">28"
- "v36@0:8@\"NSString\"16B24@?<v@?B@\"NSArray\"@\"LSRecordPromise\"@\"NSError\">28"
- "v36@0:8@\"NSString\"16i24@?<v@?@\"NSError\">28"
- "v36@0:8@16@24B32"
- "v36@0:8@16B24@?28"
- "v36@0:8@16i24@?28"
- "v40@0:8@\"MIAppIdentity\"16@\"NSDictionary\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"MIAppIdentity\"16@\"NSDictionary\"24@?<v@?B@\"NSArray\"@\"LSRecordPromise\"@\"NSError\">32"
- "v40@0:8@\"NSArray\"16@\"NSDictionary\"24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8@\"NSArray\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"NSArray\"16@\"NSDictionary\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSObject\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"NSSet\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"MIStoreMetadata\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16Q24@\"NSDictionary\"32"
- "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"NSURL\"16@\"NSDictionary\"24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8@\"NSURL\"16Q24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSUUID\"16Q24@?<v@?@\"NSURL\"@\"NSString\"@\"NSError\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@32"
- "v40@0:8@16Q24@?32"
- "v40@0:8@16^i24^i32"
- "v44@0:8@\"NSString\"16@\"NSURL\"24B32@?<v@?B@\"NSArray\"@\"LSRecordPromise\"@\"NSError\">36"
- "v44@0:8@16@24B32@?36"
- "v48@0:8@\"<MILocationProtocol>\"16Q24@\"NSString\"32@?<v@?@\"MIStagingLocation\"@\"NSError\">40"
- "v48@0:8@\"MIAppIdentity\"16@\"NSData\"24@\"NSData\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"MIAppIdentity\"16Q24@\"NSData\"32@?<v@?@\"MIAppReference\"@\"NSError\">40"
- "v48@0:8@\"MIAppIdentity\"16Q24@\"NSDictionary\"32@?<v@?@\"NSArray\"@\"NSError\">40"
- "v48@0:8@\"MIAppIdentity\"16Q24@\"NSDictionary\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSData\"32@?<v@?@\"ICLSinfInfo\"@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSURL\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSURL\"24@\"NSDictionary\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSURL\"24B32B36@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@\"NSURL\"16@\"MIStagingLocation\"24@\"MIInstallOptions\"32@?<v@?@\"NSURL\"B@\"NSError\">40"
- "v48@0:8@\"NSURL\"16Q24@\"NSString\"32@?<v@?@\"MIStagingLocation\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24B32B36@?40"
- "v48@0:8@16Q24@32@?40"
- "v48@0:8Q16@\"NSString\"24@\"NSDictionary\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8Q16@24@32@?40"
- "v56@0:8@\"NSString\"16@\"MIAppIdentity\"24Q32@\"NSDictionary\"40@?<v@?@\"NSError\">48"
- "v56@0:8@\"NSString\"16@\"NSString\"24Q32@\"NSURL\"40@?<v@?@\"NSError\">48"
- "v56@0:8@\"NSURL\"16@\"MIAppIdentity\"24Q32@\"MIInstallOptions\"40@?<v@?@\"MIStagedUpdateMetadata\"@\"NSError\">48"
- "v56@0:8@16@24Q32@40@?48"
- "v60@0:8@\"NSURL\"16@\"MIAppIdentity\"24Q32@\"MIInstallOptions\"40B48@?<v@?B@\"NSArray\"@\"LSRecordPromise\"@\"NSError\">52"
- "v60@0:8@16@24Q32@40B48@?52"
- "v64@0:8@\"NSString\"16Q24Q32@\"NSError\"40Q48@?<v@?@\"NSError\">56"
- "v64@0:8@16Q24Q32@40Q48@?56"
- "v72@0:8@\"NSURL\"16@\"NSURL\"24{?=[8I]}32@?<v@?@\"NSError\">64"
- "v72@0:8@16@24{?=[8I]}32@?64"
- "v80@0:8@\"MIStagingLocation\"16@\"NSString\"24@\"NSURL\"32{?=[8I]}40@?<v@?@\"NSError\">72"
- "v80@0:8@16@24@32{?=[8I]}40@?72"
- "validateAppIdentity:withError:"
- "validateAppMetadataWithError:"
- "validateBundleMetadataWithError:"
- "validateDriverKitExtensionMetadataWithError:"
- "validateExtensionKitMetadataWithError:"
- "validateHasCorrespondingEntitlements:error:"
- "validateHasNoDotInBundleIDSuffix:"
- "validatePluginKitMetadataWithError:"
- "validateResources"
- "validateSinfWithError:"
- "validateSymlinksInURLDoNotEscapeURL:error:"
- "validateURL:forLocation:error:"
- "validateUsingDetachedSignature"
- "validateWatchKitV1StubExecutableBundle:error:"
- "validateWatchKitV2StubExecutableBundle:error:"
- "validateWithURLonEmbedded:forLocation:error:"
- "validationOverrideParentBundleID"
- "verifyTrustCachePresence"
- "volumeDaemonContainer"
- "volumeUUIDForLocation:error:"
- "volumeUUIDForURL:completion:"
- "volumeUUIDForURL:error:"
- "waitForSystemAppMigratorToComplete:"
- "wasErroneousContainerCleanupDone"
- "watchKitAppBundleForWKVersionOrEarlier:error:"
- "watchKitAppExecutableHashWithError:"
- "watchKitAppRunsIndependentlyOfCompanion"
- "watchKitPlugin"
- "watchKitPluginWithError:"
- "watchKitV2AppBundleWithError:"
- "watchKitVersionWithError:"
- "wipeStagingRootAndSetUpPerUserDataDirWithCompletion:"
- "wk2AppBundle"
- "wk2AppBundleError"
- "writeToBundle:error:"
- "writeToURL:atomically:encoding:error:"
- "writeToURL:options:error:"
- "writeiTunesMetadata:error:"
- "xpcConnection"
- "xpcServiceBundles"
- "xpcServiceBundlesWithError:"
- "xrOS"
- "xrOS Simulator"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{os_unfair_lock_s=I}16@0:8"

```
