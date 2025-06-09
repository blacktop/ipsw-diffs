## InstalledContentLibrary

> `/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary`

```diff

-1378.100.35.0.0
-  __TEXT.__text: 0xa1d30
-  __TEXT.__auth_stubs: 0x1370
-  __TEXT.__objc_methlist: 0x47b4
-  __TEXT.__const: 0xf6c0
-  __TEXT.__gcc_except_tab: 0xa8c
-  __TEXT.__cstring: 0x16159
+1513.0.8.0.2
+  __TEXT.__text: 0xb7c6c
+  __TEXT.__auth_stubs: 0x17c0
+  __TEXT.__objc_methlist: 0x5354
+  __TEXT.__const: 0xf7e0
+  __TEXT.__gcc_except_tab: 0xbc8
+  __TEXT.__cstring: 0x178ed
+  __TEXT.__oslogstring: 0x8eb
   __TEXT.__dlopen_cstrs: 0x111
-  __TEXT.__oslogstring: 0x8b6
-  __TEXT.__unwind_info: 0x13c8
-  __TEXT.__eh_frame: 0xd70
-  __TEXT.__objc_classname: 0x567
-  __TEXT.__objc_methname: 0xd1e7
-  __TEXT.__objc_methtype: 0x17f9
-  __TEXT.__objc_stubs: 0x8300
-  __DATA_CONST.__got: 0x3f8
-  __DATA_CONST.__const: 0xc48
-  __DATA_CONST.__objc_classlist: 0x1c0
+  __TEXT.__swift5_typeref: 0x30
+  __TEXT.__unwind_info: 0x16b8
+  __TEXT.__eh_frame: 0x388
+  __TEXT.__objc_classname: 0x619
+  __TEXT.__objc_methname: 0xea36
+  __TEXT.__objc_methtype: 0x1d5f
+  __TEXT.__objc_stubs: 0x8a80
+  __DATA_CONST.__got: 0x4a8
+  __DATA_CONST.__const: 0xe60
+  __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2838
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x150
-  __DATA_CONST.__objc_arraydata: 0x9c0
-  __AUTH_CONST.__auth_got: 0x9c8
-  __AUTH_CONST.__const: 0x5468
-  __AUTH_CONST.__cfstring: 0xc300
-  __AUTH_CONST.__objc_const: 0x7a48
-  __AUTH_CONST.__objc_dictobj: 0x11f8
-  __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__objc_intobj: 0xa8
-  __DATA.__objc_ivar: 0x50c
-  __DATA.__data: 0x1158
-  __DATA.__bss: 0xf0
-  __DATA.__common: 0x50
+  __DATA_CONST.__objc_selrefs: 0x2ce8
+  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x170
+  __DATA_CONST.__objc_arraydata: 0xb20
+  __AUTH_CONST.__auth_got: 0xbf0
+  __AUTH_CONST.__const: 0x5698
+  __AUTH_CONST.__cfstring: 0xcbe0
+  __AUTH_CONST.__objc_const: 0x9af8
+  __AUTH_CONST.__objc_dictobj: 0x1270
+  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH_CONST.__objc_intobj: 0x180
+  __AUTH.__objc_data: 0x370
+  __AUTH.__data: 0xc8
+  __DATA.__objc_ivar: 0x578
+  __DATA.__data: 0x9d0
+  __DATA.__bss: 0x138
+  __DATA.__common: 0xa18
   __DATA_DIRTY.__objc_data: 0x1180
   __DATA_DIRTY.__data: 0x70
-  __DATA_DIRTY.__bss: 0x190
+  __DATA_DIRTY.__bss: 0x198
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 31C9174F-9EBA-32EF-AB34-B43D58E0536C
-  Functions: 1870
-  Symbols:   6163
-  CStrings:  5829
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  UUID: 9700BE63-029C-31CF-850B-F5329EFFA402
+  Functions: 2186
+  Symbols:   6813
+  CStrings:  6299
 
Symbols:
+ +[ICLFeatureFlags switchingPersonasEnabled]
+ +[ICLHelperServiceClient sharedInstance]
+ +[MIAppIdentity _locationClassCluster]
+ +[MIBundle _infoPlistKeysToLoad]
+ +[MIBundle _infoPlistKeysToLoad].cold.1
+ +[MIBundle bundleForURL:platformHint:forceAsPlaceholder:error:]
+ +[MIMCMContainer _performWithLaunchPersona:]
+ +[MIMCMContainer daemonContainerForIdentifier:personaUniqueString:error:]
+ +[MIMCMContainer daemonContainerForPersona:error:]
+ +[MIStagingLocation _stagingRootClassCluster]
+ +[MIStagingLocation supportsSecureCoding]
+ +[MIStagingRootAbsolute supportsSecureCoding]
+ +[MIStagingRootVolumeUUID supportsSecureCoding]
+ -[ICLHelperServiceClient .cxx_destruct]
+ -[ICLHelperServiceClient _invalidateObject]
+ -[ICLHelperServiceClient _remoteObjectProxyWithErrorHandler:]
+ -[ICLHelperServiceClient _sharedConnection]
+ -[ICLHelperServiceClient _synchronousRemoteObjectProxyWithErrorHandler:]
+ -[ICLHelperServiceClient dealloc]
+ -[ICLHelperServiceClient resolveStagingBaseWithSandboxExtension:forVolumeUUID:withinStagingSubsystem:error:]
+ -[ICLHelperServiceClient setXpcConnection:]
+ -[ICLHelperServiceClient stagingURLWithSandboxExtension:forSystemContentWithinSubsystem:error:]
+ -[ICLHelperServiceClient stagingURLWithSandboxExtension:forUserContentWithinSubsystem:error:]
+ -[ICLHelperServiceClient volumeUUIDForURL:error:]
+ -[ICLHelperServiceClient xpcConnection]
+ -[ICLPlaceholderRecord setSupportsAppMigration:]
+ -[ICLPlaceholderRecord supportsAppMigration]
+ -[MIAppIdentity _doInitWithBundleID:personaUniqueString:location:]
+ -[MIAppIdentity _doInitWithBundleID:personaUniqueString:location:].cold.1
+ -[MIAppIdentity identityByChangingLocation:]
+ -[MIAppIdentity initWithBundleID:personaUniqueString:location:]
+ -[MIAppIdentity initWithBundleIdentifier:personaUniqueString:]
+ -[MIAppIdentity initWithBundleIdentifier:personaUniqueString:location:]
+ -[MIAppIdentity location]
+ -[MIAppIdentity setLocation:]
+ -[MIBundle _getBundleRootContainsOnlyContentsDirectory:error:]
+ -[MIBundle _setBundleParentDirectoryURL:forBundleArray:error:]
+ -[MIBundle bundleInfoPlistSupportedPlatforms]
+ -[MIBundle cfBundle]
+ -[MIBundle contentsURL]
+ -[MIBundle dealloc]
+ -[MIBundle denormalizedURLForCFBundleURL:]
+ -[MIBundle getIsBuiltForMacPlatform:error:]
+ -[MIBundle infoPlistHashWithError:]
+ -[MIBundle infoPlistURL]
+ -[MIBundle initWithBundleParentURL:parentSubdirectory:bundleName:platformHint:forceAsPlaceholder:error:]
+ -[MIBundle initWithBundleURL:platformHint:forceAsPlaceholder:error:]
+ -[MIBundle initWithParentBundle:parentSubdirectory:bundleName:platformHint:forceAsPlaceholder:error:]
+ -[MIBundle platformHint]
+ -[MIBundle plugInsDirectoryURL]
+ -[MIBundle setBundleParentDirectoryURL:error:]
+ -[MIBundle setInfoPlistSubsetForTesting:]
+ -[MIBundleContainer initWithContainerURL:expectAppWithin:error:]
+ -[MIDaemonConfiguration currentUserInstallCoordinationCachesDirectory]
+ -[MIDaemonConfiguration daemonUserDataLibraryDirectory].cold.1
+ -[MIDaemonConfiguration daemonUserDataLibraryDirectory].cold.2
+ -[MIDaemonConfiguration installcoordinationdUserDataLibraryDirectory]
+ -[MIDaemonConfiguration installcoordinationdUserDataLibraryDirectory].cold.1
+ -[MIDaemonConfiguration installcoordinationdUserDataLibraryDirectory].cold.2
+ -[MIExecutableBundle checkExecutableExistsIfRequiredWithError:]
+ -[MIExecutableBundle getIsBuiltForMacPlatform:error:]
+ -[MIExecutableBundle hasExecutable]
+ -[MIExecutableBundle setBundleParentDirectoryURL:error:]
+ -[MIFileManager _firstAvailableParentForURL:error:]
+ -[MIFileManager _traverseUntilFirstAvailableParentOfURL:withBlock:]
+ -[MIFileManager copyVolumeInfo:forURL:error:]
+ -[MIFileManager createRelativeDirectoryPath:inBaseDirectory:mode:class:error:]
+ -[MIFileManager enumerateExternalVolumesWithBlock:]
+ -[MIFileManager mountPointForURL:error:]
+ -[MIFileManager mountPointForVolumeUUID:error:]
+ -[MIFileManager setOwnershipAtURL:toUID:gid:error:]
+ -[MIFileManager volumeUUIDForURL:error:]
+ -[MIGlobalConfiguration _ixDataStorageHomeURLWithError:]
+ -[MIGlobalConfiguration installCoordinationStagingWithError:]
+ -[MIGlobalConfiguration installcoordinationdPath]
+ -[MIGlobalConfiguration ixDaemonGID]
+ -[MIGlobalConfiguration ixDaemonUID]
+ -[MIGlobalConfiguration ixDataStorageDirectoryPath]
+ -[MIMCMContainer _doInitWithContainer:error:].cold.1
+ -[MIMCMContainer dealloc].cold.1
+ -[MIMCMContainer sandboxToken]
+ -[MIMCMContainer transferOwnershipOfSandboxExtensionToCaller]
+ -[MIMachOImageSlice .cxx_destruct]
+ -[MIMachOImageSlice archNameString]
+ -[MIMachOImageSlice setArchNameString:]
+ -[MIPersonaAttributes dealloc]
+ -[MIPersonaAttributes dealloc].cold.1
+ -[MIPersonaAttributes extensionHandle]
+ -[MIPersonaAttributes initWithPersonaString:personaType:associatedBundleIDs:volumeDaemonContainer:volumeDaemonContainerSandboxExtension:]
+ -[MIPersonaAttributes volumeDaemonContainer]
+ -[MIStagingLocation .cxx_destruct]
+ -[MIStagingLocation copyWithZone:]
+ -[MIStagingLocation description]
+ -[MIStagingLocation encodeWithCoder:]
+ -[MIStagingLocation hash]
+ -[MIStagingLocation initWithCoder:]
+ -[MIStagingLocation initWithStagingRoot:relativeStagingBaseDirectory:]
+ -[MIStagingLocation isEqual:]
+ -[MIStagingLocation relativeStagingBaseDirectory]
+ -[MIStagingLocation resolveWithError:]
+ -[MIStagingLocation setRelativeStagingBaseDirectory:]
+ -[MIStagingLocation stagingRoot]
+ -[MIStagingRootAbsolute _runWithLock:]
+ -[MIStagingRootAbsolute copyWithZone:]
+ -[MIStagingRootAbsolute dealloc]
+ -[MIStagingRootAbsolute description]
+ -[MIStagingRootAbsolute encodeWithCoder:]
+ -[MIStagingRootAbsolute extensionHandle]
+ -[MIStagingRootAbsolute hash]
+ -[MIStagingRootAbsolute initWithCoder:]
+ -[MIStagingRootAbsolute initWithStagingSubsystem:contentType:]
+ -[MIStagingRootAbsolute isEqual:]
+ -[MIStagingRootAbsolute lock]
+ -[MIStagingRootAbsolute resolveRootWithError:]
+ -[MIStagingRootAbsolute setExtensionHandle:]
+ -[MIStagingRootAbsolute stagingContentType]
+ -[MIStagingRootAbsolute stagingSubsystem]
+ -[MIStagingRootVolumeUUID .cxx_destruct]
+ -[MIStagingRootVolumeUUID _runWithLock:]
+ -[MIStagingRootVolumeUUID copyWithZone:]
+ -[MIStagingRootVolumeUUID dealloc]
+ -[MIStagingRootVolumeUUID description]
+ -[MIStagingRootVolumeUUID encodeWithCoder:]
+ -[MIStagingRootVolumeUUID extensionHandle]
+ -[MIStagingRootVolumeUUID hash]
+ -[MIStagingRootVolumeUUID initWithCoder:]
+ -[MIStagingRootVolumeUUID initWithVolumeUUID:stagingSubsystem:]
+ -[MIStagingRootVolumeUUID isEqual:]
+ -[MIStagingRootVolumeUUID lock]
+ -[MIStagingRootVolumeUUID resolveRootWithError:]
+ -[MIStagingRootVolumeUUID setExtensionHandle:]
+ -[MIStagingRootVolumeUUID stagingSubsystem]
+ -[MIStagingRootVolumeUUID volumeUUID]
+ -[MIStoreMetadata installerEpoch]
+ -[MIStoreMetadata setInstallerEpoch:]
+ -[MIStoreMetadataDistributor betaTesterType]
+ -[MIStoreMetadataDistributor setBetaTesterType:]
+ -[MIUserManagement allPersonaVolumeDaemonContainersMap]
+ -[MIUserManagement personaVolumeDaemonContainerForUUID:]
+ -[MIUserManagement personaVolumeUUIDToDaemonContainerMap]
+ -[MIUserManagement setPersonaVolumeUUIDToDaemonContainerMap:]
+ GCC_except_table10
+ GCC_except_table105
+ GCC_except_table12
+ GCC_except_table14
+ GCC_except_table19
+ GCC_except_table20
+ GCC_except_table24
+ GCC_except_table27
+ GCC_except_table30
+ GCC_except_table32
+ GCC_except_table38
+ GCC_except_table40
+ GCC_except_table47
+ GCC_except_table54
+ GCC_except_table59
+ GCC_except_table65
+ GCC_except_table66
+ GCC_except_table69
+ GCC_except_table78
+ GCC_except_table85
+ GCC_except_table9
+ _CFBundleCopyBuiltInPlugInsURL
+ _CFBundleCopyBundleURL
+ _CFBundleCopyExecutableURL
+ _CFBundleCopySupportFilesDirectoryURL
+ _InstalledContentLibraryVersionNumber
+ _InstalledContentLibraryVersionString
+ _MIConsumeSandboxExtension
+ _MICreateCFBundle
+ _MIDeDuplicateStagingRoot
+ _MILoadInfoPlistFromBundleWithError
+ _MIReleaseSandboxExtensionHandle
+ _MIReleaseSandboxExtensionHandle.cold.1
+ _MIReleaseSandboxExtensionHandle.cold.2
+ _MIStringForStagingContentType
+ _MIStringForStagingSubsystem
+ _MobileInstallationHelperServiceProtocolInterface
+ _MobileInstallationHelperServiceProtocolInterface.lock
+ _MobileInstallationHelperServiceProtocolInterface.weakInterface
+ _OBJC_CLASS_$_ICLHelperServiceClient
+ _OBJC_CLASS_$_MILocation
+ _OBJC_CLASS_$_MILocationSystemDefinedBase
+ _OBJC_CLASS_$_MILocationSystemDefinedCommon
+ _OBJC_CLASS_$_MILocationUserDefined
+ _OBJC_CLASS_$_MILocationUserDefinedDirectory
+ _OBJC_CLASS_$_MIStagingLocation
+ _OBJC_CLASS_$_MIStagingRootAbsolute
+ _OBJC_CLASS_$_MIStagingRootVolumeUUID
+ _OBJC_IVAR_$_ICLHelperServiceClient._xpcConnection
+ _OBJC_IVAR_$_ICLPlaceholderRecord._supportsAppMigration
+ _OBJC_IVAR_$_MIAppIdentity._location
+ _OBJC_IVAR_$_MIBundle._cfBundle
+ _OBJC_IVAR_$_MIBundle._platformHint
+ _OBJC_IVAR_$_MIDaemonConfiguration._installcoordinationdUserDataLibraryDirectory
+ _OBJC_IVAR_$_MIExecutableBundle._hasExecutable
+ _OBJC_IVAR_$_MIGlobalConfiguration._dynamicPropertyLock
+ _OBJC_IVAR_$_MIGlobalConfiguration._installcoordinationdPath
+ _OBJC_IVAR_$_MIGlobalConfiguration._ixDaemonGID
+ _OBJC_IVAR_$_MIGlobalConfiguration._ixDaemonUID
+ _OBJC_IVAR_$_MIGlobalConfiguration._ixDataStorageDirectoryPath
+ _OBJC_IVAR_$_MIMCMContainer._sandboxToken
+ _OBJC_IVAR_$_MIMachOImageSlice._archNameString
+ _OBJC_IVAR_$_MIPersonaAttributes._extensionHandle
+ _OBJC_IVAR_$_MIPersonaAttributes._volumeDaemonContainer
+ _OBJC_IVAR_$_MIStagingLocation._relativeStagingBaseDirectory
+ _OBJC_IVAR_$_MIStagingLocation._stagingRoot
+ _OBJC_IVAR_$_MIStagingRootAbsolute._extensionHandle
+ _OBJC_IVAR_$_MIStagingRootAbsolute._lock
+ _OBJC_IVAR_$_MIStagingRootAbsolute._stagingContentType
+ _OBJC_IVAR_$_MIStagingRootAbsolute._stagingSubsystem
+ _OBJC_IVAR_$_MIStagingRootVolumeUUID._extensionHandle
+ _OBJC_IVAR_$_MIStagingRootVolumeUUID._lock
+ _OBJC_IVAR_$_MIStagingRootVolumeUUID._stagingSubsystem
+ _OBJC_IVAR_$_MIStagingRootVolumeUUID._volumeUUID
+ _OBJC_IVAR_$_MIStoreMetadata._installerEpoch
+ _OBJC_IVAR_$_MIStoreMetadataDistributor._betaTesterType
+ _OBJC_IVAR_$_MIUserManagement._personaVolumeUUIDToDaemonContainerMap
+ _OBJC_METACLASS_$_ICLHelperServiceClient
+ _OBJC_METACLASS_$_MILocation
+ _OBJC_METACLASS_$_MILocationSystemDefinedBase
+ _OBJC_METACLASS_$_MILocationSystemDefinedCommon
+ _OBJC_METACLASS_$_MILocationUserDefined
+ _OBJC_METACLASS_$_MILocationUserDefinedDirectory
+ _OBJC_METACLASS_$_MIStagingLocation
+ _OBJC_METACLASS_$_MIStagingRootAbsolute
+ _OBJC_METACLASS_$_MIStagingRootVolumeUUID
+ __CLASS_METHODS_MILocation
+ __CLASS_METHODS_MILocationSystemDefinedBase
+ __CLASS_PROPERTIES_MILocationSystemDefinedBase
+ __DATA_MILocation
+ __DATA_MILocationSystemDefinedBase
+ __DATA_MILocationSystemDefinedCommon
+ __DATA_MILocationUserDefined
+ __DATA_MILocationUserDefinedDirectory
+ __INSTANCE_METHODS_MILocation
+ __INSTANCE_METHODS_MILocationSystemDefinedBase
+ __IVARS_MILocationUserDefined
+ __IVARS_MILocationUserDefinedDirectory
+ __METACLASS_DATA_MILocation
+ __METACLASS_DATA_MILocationSystemDefinedBase
+ __METACLASS_DATA_MILocationSystemDefinedCommon
+ __METACLASS_DATA_MILocationUserDefined
+ __METACLASS_DATA_MILocationUserDefinedDirectory
+ __OBJC_$_CLASS_METHODS_ICLHelperServiceClient
+ __OBJC_$_CLASS_METHODS_MILocationSystemDefinedCommon(InstalledContentLibrary)
+ __OBJC_$_CLASS_METHODS_MILocationUserDefined(InstalledContentLibrary)
+ __OBJC_$_CLASS_METHODS_MILocationUserDefinedDirectory(InstalledContentLibrary)
+ __OBJC_$_CLASS_METHODS_MIStagingLocation
+ __OBJC_$_CLASS_METHODS_MIStagingRootAbsolute
+ __OBJC_$_CLASS_METHODS_MIStagingRootVolumeUUID
+ __OBJC_$_CLASS_PROP_LIST_MIStagingLocation
+ __OBJC_$_CLASS_PROP_LIST_MIStagingRootAbsolute
+ __OBJC_$_CLASS_PROP_LIST_MIStagingRootVolumeUUID
+ __OBJC_$_INSTANCE_METHODS_ICLHelperServiceClient
+ __OBJC_$_INSTANCE_METHODS_MILocationSystemDefinedCommon(InstalledContentLibrary)
+ __OBJC_$_INSTANCE_METHODS_MILocationUserDefined(InstalledContentLibrary)
+ __OBJC_$_INSTANCE_METHODS_MILocationUserDefinedDirectory(InstalledContentLibrary)
+ __OBJC_$_INSTANCE_METHODS_MIStagingLocation
+ __OBJC_$_INSTANCE_METHODS_MIStagingRootAbsolute
+ __OBJC_$_INSTANCE_METHODS_MIStagingRootVolumeUUID
+ __OBJC_$_INSTANCE_VARIABLES_ICLHelperServiceClient
+ __OBJC_$_INSTANCE_VARIABLES_MIStagingLocation
+ __OBJC_$_INSTANCE_VARIABLES_MIStagingRootAbsolute
+ __OBJC_$_INSTANCE_VARIABLES_MIStagingRootVolumeUUID
+ __OBJC_$_PROP_LIST_ICLHelperServiceClient
+ __OBJC_$_PROP_LIST_MIStagingLocation
+ __OBJC_$_PROP_LIST_MIStagingRootAbsolute
+ __OBJC_$_PROP_LIST_MIStagingRootProtocol
+ __OBJC_$_PROP_LIST_MIStagingRootVolumeUUID
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_CLASS_METHODS_MIStagingRootProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MIStagingRootProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MobileInstallationHelperServiceProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MIStagingRootProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MIStagingRootProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MobileInstallationHelperServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_MILocationProtocol
+ __OBJC_$_PROTOCOL_REFS_MIStagingRootProtocol
+ __OBJC_CLASS_PROTOCOLS_$_MIStagingLocation
+ __OBJC_CLASS_PROTOCOLS_$_MIStagingRootAbsolute
+ __OBJC_CLASS_PROTOCOLS_$_MIStagingRootVolumeUUID
+ __OBJC_CLASS_RO_$_ICLHelperServiceClient
+ __OBJC_CLASS_RO_$_MIStagingLocation
+ __OBJC_CLASS_RO_$_MIStagingRootAbsolute
+ __OBJC_CLASS_RO_$_MIStagingRootVolumeUUID
+ __OBJC_LABEL_PROTOCOL_$_MILocationProtocol
+ __OBJC_LABEL_PROTOCOL_$_MIStagingRootProtocol
+ __OBJC_LABEL_PROTOCOL_$_MobileInstallationHelperServiceProtocol
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_ICLHelperServiceClient
+ __OBJC_METACLASS_RO_$_MIStagingLocation
+ __OBJC_METACLASS_RO_$_MIStagingRootAbsolute
+ __OBJC_METACLASS_RO_$_MIStagingRootVolumeUUID
+ __OBJC_PROTOCOL_$_MILocationProtocol
+ __OBJC_PROTOCOL_$_MIStagingRootProtocol
+ __OBJC_PROTOCOL_$_MobileInstallationHelperServiceProtocol
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_REFERENCE_$_MobileInstallationHelperServiceProtocol
+ __PROTOCOLS_MILocationSystemDefinedBase
+ __PROTOCOLS_MILocationSystemDefinedBase.2
+ __PROTOCOLS_MILocationUserDefined
+ __PROTOCOLS_MILocationUserDefined.3
+ __PROTOCOLS_MILocationUserDefinedDirectory
+ __PROTOCOLS_MILocationUserDefinedDirectory.3
+ ___108-[ICLHelperServiceClient resolveStagingBaseWithSandboxExtension:forVolumeUUID:withinStagingSubsystem:error:]_block_invoke
+ ___108-[ICLHelperServiceClient resolveStagingBaseWithSandboxExtension:forVolumeUUID:withinStagingSubsystem:error:]_block_invoke_2
+ ___32+[MIBundle _infoPlistKeysToLoad]_block_invoke
+ ___40+[ICLHelperServiceClient sharedInstance]_block_invoke
+ ___43-[ICLHelperServiceClient _sharedConnection]_block_invoke
+ ___43-[ICLHelperServiceClient _sharedConnection]_block_invoke_2
+ ___46-[MIStagingRootAbsolute resolveRootWithError:]_block_invoke
+ ___47-[MIFileManager mountPointForVolumeUUID:error:]_block_invoke
+ ___48-[MIStagingRootVolumeUUID resolveRootWithError:]_block_invoke
+ ___49-[ICLHelperServiceClient volumeUUIDForURL:error:]_block_invoke
+ ___49-[ICLHelperServiceClient volumeUUIDForURL:error:]_block_invoke_2
+ ___51-[MIFileManager _firstAvailableParentForURL:error:]_block_invoke
+ ___51-[MIFileManager setOwnershipAtURL:toUID:gid:error:]_block_invoke
+ ___54-[MIUserManagement personaTypeForPersonaUniqueString:]_block_invoke
+ ___55-[MIUserManagement allPersonaVolumeDaemonContainersMap]_block_invoke
+ ___56-[MIUserManagement personaVolumeDaemonContainerForUUID:]_block_invoke
+ ___58-[MIFileManager deviceForURLOrFirstAvailableParent:error:]_block_invoke
+ ___62-[MIBundle _getBundleRootContainsOnlyContentsDirectory:error:]_block_invoke
+ ___73+[MIMCMContainer daemonContainerForIdentifier:personaUniqueString:error:]_block_invoke
+ ___93-[ICLHelperServiceClient stagingURLWithSandboxExtension:forUserContentWithinSubsystem:error:]_block_invoke
+ ___93-[ICLHelperServiceClient stagingURLWithSandboxExtension:forUserContentWithinSubsystem:error:]_block_invoke_2
+ ___95-[ICLHelperServiceClient stagingURLWithSandboxExtension:forSystemContentWithinSubsystem:error:]_block_invoke
+ ___95-[ICLHelperServiceClient stagingURLWithSandboxExtension:forSystemContentWithinSubsystem:error:]_block_invoke_2
+ ___MIDeDuplicateStagingRoot_block_invoke
+ ___block_descriptor_104_e8_32s40r48r56r64r72r_e32_B24?0^{?=Qq*Q*QIIIIIIISBC}8^B16lr40l8r48l8r56l8r64l8r72l8s32l8
+ ___block_descriptor_40_e8_32bs_e32_B24?0^{?=Qq*Q*QIIIIIIISBC}8^B16ls32l8
+ ___block_descriptor_40_e8_32r_e97_"NSError"24?0r*8^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}16lr32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_41_e8_32bs_e32_B24?0^{?=Qq*Q*QIIIIIIISBC}8^B16ls32l8
+ ___block_descriptor_48_e8_32r40r_e18_B20?0"NSURL"8C16lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e28_v24?0"NSUUID"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32r_e32_B24?0^{?=Qq*Q*QIIIIIIISBC}8^B16lr32l8
+ ___block_descriptor_48_e8_32s40r_e30_v32?0"NSURL"8"NSUUID"16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e32_B24?0^{?=Qq*Q*QIIIIIIISBC}8^B16lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_49_e8_32s40r_e32_B24?0^{?=Qq*Q*QIIIIIIISBC}8^B16lr40l8s32l8
+ ___block_descriptor_56_e8_32r40r48r_e40_v32?0"NSURL"8"NSString"16"NSError"24lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e32_B24?0^{?=Qq*Q*QIIIIIIISBC}8^B16ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_66_e8_32s40r48r_e32_B24?0^{?=Qq*Q*QIIIIIIISBC}8^B16lr40l8s32l8r48l8
+ ___block_descriptor_72_e8_32s40s48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
+ ___block_descriptor_85_e8_32s40s48s56r64r_e32_B24?0^{?=Qq*Q*QIIIIIIISBC}8^B16ls32l8s40l8s48l8r56l8r64l8
+ ___block_literal_global.124
+ ___block_literal_global.201
+ ___block_literal_global.217
+ ___block_literal_global.232
+ ___block_literal_global.333
+ ___block_literal_global.345
+ ___block_literal_global.391
+ ___block_literal_global.396
+ ___block_literal_global.568
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_reflection_version
+ __kCFBundleSupportedPlatformsKey
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_InstalledContentLibrary
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_InstalledContentLibrary
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_InstalledContentLibrary
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_InstalledContentLibrary
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_InstalledContentLibrary
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_InstalledContentLibrary
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_InstalledContentLibrary
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_InstalledContentLibrary
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_InstalledContentLibrary
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_InstalledContentLibrary
+ __swift_stdlib_reportUnimplementedInitializer
+ _betaTesterType
+ _getattrlist
+ _getmntinfo_r_np
+ _installerEpoch
+ _macho_arch_name_for_cpu_type
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend$MI_URLByAppendingPathComponents:lastIsDirectory:
+ _objc_msgSend$URLByDeletingPathExtension
+ _objc_msgSend$URLByStandardizingPath
+ _objc_msgSend$_doInitWithBundleID:personaUniqueString:location:
+ _objc_msgSend$_firstAvailableParentForURL:error:
+ _objc_msgSend$_getBundleRootContainsOnlyContentsDirectory:error:
+ _objc_msgSend$_invalidateObject
+ _objc_msgSend$_ixDataStorageHomeURLWithError:
+ _objc_msgSend$_locationClassCluster
+ _objc_msgSend$_performWithLaunchPersona:
+ _objc_msgSend$_runWithLock:
+ _objc_msgSend$_setBundleParentDirectoryURL:forBundleArray:error:
+ _objc_msgSend$_sharedConnection
+ _objc_msgSend$_stagingRootClassCluster
+ _objc_msgSend$_synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSend$_traverseUntilFirstAvailableParentOfURL:withBlock:
+ _objc_msgSend$absoluteURL
+ _objc_msgSend$betaTesterType
+ _objc_msgSend$bundleInfoPlistSupportedPlatforms
+ _objc_msgSend$contentsURL
+ _objc_msgSend$daemonContainerForIdentifier:personaUniqueString:error:
+ _objc_msgSend$daemonContainerForPersona:error:
+ _objc_msgSend$denormalizedURLForCFBundleURL:
+ _objc_msgSend$enumerateExternalVolumesWithBlock:
+ _objc_msgSend$getIsBuiltForMacPlatform:error:
+ _objc_msgSend$hasExecutable
+ _objc_msgSend$infoPlistURL
+ _objc_msgSend$initWithBundleIdentifier:personaUniqueString:
+ _objc_msgSend$initWithBundleIdentifier:personaUniqueString:location:
+ _objc_msgSend$initWithBundleParentURL:parentSubdirectory:bundleName:platformHint:forceAsPlaceholder:error:
+ _objc_msgSend$initWithBundleURL:platformHint:forceAsPlaceholder:error:
+ _objc_msgSend$initWithContainerURL:expectAppWithin:error:
+ _objc_msgSend$initWithParentBundle:parentSubdirectory:bundleName:platformHint:forceAsPlaceholder:error:
+ _objc_msgSend$initWithPersonaString:personaType:associatedBundleIDs:volumeDaemonContainer:volumeDaemonContainerSandboxExtension:
+ _objc_msgSend$initWithServiceName:
+ _objc_msgSend$initWithStagingRoot:relativeStagingBaseDirectory:
+ _objc_msgSend$initWithStagingSubsystem:contentType:
+ _objc_msgSend$initWithUUIDBytes:
+ _objc_msgSend$initWithVolumeUUID:stagingSubsystem:
+ _objc_msgSend$installcoordinationdUserDataLibraryDirectory
+ _objc_msgSend$installerEpoch
+ _objc_msgSend$location
+ _objc_msgSend$objectEnumerator
+ _objc_msgSend$personaLayoutPathURL
+ _objc_msgSend$personaVolumeUUIDToDaemonContainerMap
+ _objc_msgSend$platformHint
+ _objc_msgSend$plugInsDirectoryURL
+ _objc_msgSend$relativeStagingBaseDirectory
+ _objc_msgSend$resolveRootWithError:
+ _objc_msgSend$resolveStagingBaseWithSandboxExtension:forVolumeUUID:withinStagingSubsystem:error:
+ _objc_msgSend$resolveStagingBaseWithSandboxExtensionForVolumeUUID:withinStagingSubsystem:completion:
+ _objc_msgSend$setArchNameString:
+ _objc_msgSend$setBetaTesterType:
+ _objc_msgSend$setBundleParentDirectoryURL:error:
+ _objc_msgSend$setExtensionHandle:
+ _objc_msgSend$setInstallerEpoch:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setLocation:
+ _objc_msgSend$setSupportsAppMigration:
+ _objc_msgSend$setXpcConnection:
+ _objc_msgSend$stagingContentType
+ _objc_msgSend$stagingRoot
+ _objc_msgSend$stagingSubsystem
+ _objc_msgSend$stagingURLWithSandboxExtension:forSystemContentWithinSubsystem:error:
+ _objc_msgSend$stagingURLWithSandboxExtension:forUserContentWithinSubsystem:error:
+ _objc_msgSend$stagingURLWithSandboxExtensionForSystemContentWithinSubsystem:completion:
+ _objc_msgSend$stagingURLWithSandboxExtensionForUserContentWithinSubsystem:completion:
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_msgSend$supportsAppMigration
+ _objc_msgSend$transferOwnershipOfSandboxExtensionToCaller
+ _objc_msgSend$volumeUUID
+ _objc_msgSend$volumeUUIDForURL:completion:
+ _objc_msgSend$volumeUUIDForURL:error:
+ _objc_msgSend$xpcConnection
+ _objc_opt_self
+ _sKnownStagingRoots
+ _sLock
+ _sandbox_extension_release
+ _statfs_ext
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_deallocPartialClassInstance
+ _swift_dynamicCast
+ _swift_dynamicCastObjCClass
+ _swift_errorRelease
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release
+ _swift_retain
+ _swift_setDeallocating
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_willThrow
+ _symbolic SS_ypt
+ _symbolic _____Sg 10Foundation3URLV
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic ypSg
+ _voucher_adopt
- -[MIAppExtensionBundle setBundleParentDirectoryURL:]
- -[MIAppIdentity initWithBundleID:persona:].cold.1
- -[MIBundle _infoPlistKeysToLoad]
- -[MIBundle _infoPlistKeysToLoad].cold.1
- -[MIBundle infoPlistSubsetForTesting:]
- -[MIBundle initWithBundleParentURL:parentSubdirectory:bundleName:error:]
- -[MIBundle initWithParentBundle:parentSubdirectory:bundleName:error:]
- -[MIBundle setBundleParentDirectoryURL:]
- -[MIBundleContainer initForAppContainerWithURL:]
- -[MIDaemonConfiguration stagingRootForDevice:url:identifier:error:]
- -[MIDaemonConfiguration stagingRootForDevice:url:identifier:error:].cold.1
- -[MIDaemonConfiguration stagingRootForIdentifier:]
- -[MIDaemonConfiguration stagingRootForSystemContent]
- -[MIDaemonConfiguration stagingRootForURL:identifier:error:]
- -[MIDaemonConfiguration stagingRootForUserContent]
- -[MIEmbeddedWatchBundle initWithParentBundle:parentSubdirectory:bundleName:isPlaceholder:error:]
- -[MIEmbeddedWatchBundle isPlaceholder]
- -[MIExecutableBundle cfBundle]
- -[MIExecutableBundle dealloc]
- -[MIExecutableBundle executableExistsWithError:]
- -[MIExecutableBundle setBundleParentDirectoryURL:]
- -[MIPersonaAttributes initWithPersonaString:personaType:associatedBundleIDs:]
- GCC_except_table23
- GCC_except_table26
- GCC_except_table31
- GCC_except_table37
- GCC_except_table44
- GCC_except_table52
- GCC_except_table55
- GCC_except_table56
- GCC_except_table6
- GCC_except_table61
- GCC_except_table67
- GCC_except_table86
- GCC_except_table92
- _OBJC_IVAR_$_MIEmbeddedWatchBundle._isPlaceholder
- _OBJC_IVAR_$_MIExecutableBundle._cfBundle
- __CreateCFBundle
- __OBJC_$_INSTANCE_VARIABLES_MIEmbeddedWatchBundle
- ___32-[MIBundle _infoPlistKeysToLoad]_block_invoke
- ___55-[MIDaemonConfiguration daemonUserDataLibraryDirectory]_block_invoke
- ___55-[MIDaemonConfiguration daemonUserDataLibraryDirectory]_block_invoke.cold.1
- ___55-[MIDaemonConfiguration daemonUserDataLibraryDirectory]_block_invoke.cold.2
- ___55-[MIDaemonConfiguration daemonUserDataLibraryDirectory]_block_invoke.cold.3
- ___55-[MIDaemonConfiguration daemonUserDataLibraryDirectory]_block_invoke.cold.4
- ___55-[MIDaemonConfiguration daemonUserDataLibraryDirectory]_block_invoke.cold.5
- ___67-[MIDaemonConfiguration stagingRootForDevice:url:identifier:error:]_block_invoke
- ___block_descriptor_104_e8_32s40r48r56r64r72r_e32_B24?0^{?=Qq*Q*QQIIIIIISBC}8^B16lr40l8r48l8r56l8r64l8r72l8s32l8
- ___block_descriptor_40_e8_32bs_e32_B24?0^{?=Qq*Q*QQIIIIIISBC}8^B16ls32l8
- ___block_descriptor_41_e8_32bs_e32_B24?0^{?=Qq*Q*QQIIIIIISBC}8^B16ls32l8
- ___block_descriptor_48_e8_32s40r_e32_B24?0^{?=Qq*Q*QQIIIIIISBC}8^B16lr40l8s32l8
- ___block_descriptor_49_e8_32s40r_e32_B24?0^{?=Qq*Q*QQIIIIIISBC}8^B16lr40l8s32l8
- ___block_descriptor_56_e8_32s40s48r_e32_B24?0^{?=Qq*Q*QQIIIIIISBC}8^B16ls32l8s40l8r48l8
- ___block_descriptor_66_e8_32s40r48r_e32_B24?0^{?=Qq*Q*QQIIIIIISBC}8^B16lr40l8s32l8r48l8
- ___block_descriptor_68_e8_32s40r48r56r_e32_v32?0"NSURL"8"NSNumber"16^B24ls32l8r40l8r48l8r56l8
- ___block_descriptor_85_e8_32s40s48s56r64r_e32_B24?0^{?=Qq*Q*QQIIIIIISBC}8^B16ls32l8s40l8s48l8r56l8r64l8
- ___block_literal_global.105
- ___block_literal_global.187
- ___block_literal_global.213
- ___block_literal_global.228
- ___block_literal_global.320
- ___block_literal_global.326
- ___block_literal_global.372
- ___block_literal_global.377
- ___block_literal_global.546
- _daemonUserDataLibraryDirectory.onceToken
- _objc_msgSend$cachesDirectory
- _objc_msgSend$currentUserCachesDirectory
- _objc_msgSend$deviceForURLOrFirstAvailableParent:error:
- _objc_msgSend$hasEAPFSVolumeSplit
- _objc_msgSend$initFileURLWithFileSystemRepresentation:isDirectory:relativeToURL:
- _objc_msgSend$initForAppContainerWithURL:
- _objc_msgSend$initWithBundleID:persona:
- _objc_msgSend$initWithBundleParentURL:parentSubdirectory:bundleName:error:
- _objc_msgSend$initWithParentBundle:parentSubdirectory:bundleName:error:
- _objc_msgSend$initWithParentBundle:parentSubdirectory:bundleName:isPlaceholder:error:
- _objc_msgSend$initWithPersonaString:personaType:associatedBundleIDs:
- _objc_msgSend$setBundleParentDirectoryURL:
- _objc_msgSend$stagingRootForDevice:url:identifier:error:
- _objc_msgSend$stagingRootForSystemContent
- _objc_msgSend$stagingRootForUserContent
- _objc_release_x10
CStrings:
+ " on a volume with UUID ["
+ " that expects paths on a volume with UUID ["
+ "\""
+ "%s: Expected non-NULL extensionHandle for %@"
+ "%s: Failed to release sandbox token %lld for %@ : %s"
+ "%s: Failed to release sandbox token %lld for container %@"
+ "%s: Got daemon container at %@ for data separated persona %@ that was not on persona mount %@"
+ "(%@-%@)"
+ "(%@|%@)"
+ "-[ICLHelperServiceClient _remoteObjectProxyWithErrorHandler:]"
+ "-[ICLHelperServiceClient _synchronousRemoteObjectProxyWithErrorHandler:]"
+ "-[ICLHelperServiceClient resolveStagingBaseWithSandboxExtension:forVolumeUUID:withinStagingSubsystem:error:]_block_invoke"
+ "-[ICLHelperServiceClient stagingURLWithSandboxExtension:forSystemContentWithinSubsystem:error:]_block_invoke"
+ "-[ICLHelperServiceClient stagingURLWithSandboxExtension:forUserContentWithinSubsystem:error:]_block_invoke"
+ "-[ICLHelperServiceClient volumeUUIDForURL:error:]_block_invoke"
+ "-[MIAppIdentity _doInitWithBundleID:personaUniqueString:location:]"
+ "-[MIBundle bundleInfoPlistSupportedPlatforms]"
+ "-[MIBundle getIsBuiltForMacPlatform:error:]"
+ "-[MIBundle infoPlistHashWithError:]"
+ "-[MIBundle setBundleParentDirectoryURL:error:]"
+ "-[MIBundleContainer initWithContainerURL:expectAppWithin:error:]"
+ "-[MIDaemonConfiguration daemonUserDataLibraryDirectory]"
+ "-[MIDaemonConfiguration installcoordinationdUserDataLibraryDirectory]"
+ "-[MIExecutableBundle checkExecutableExistsIfRequiredWithError:]"
+ "-[MIExecutableBundle relativeExecutablePath]"
+ "-[MIFileManager _traverseUntilFirstAvailableParentOfURL:withBlock:]"
+ "-[MIFileManager copyVolumeInfo:forURL:error:]"
+ "-[MIFileManager deviceForURLOrFirstAvailableParent:error:]_block_invoke"
+ "-[MIFileManager enumerateExternalVolumesWithBlock:]"
+ "-[MIFileManager mountPointForURL:error:]"
+ "-[MIFileManager setOwnershipAtURL:toUID:gid:error:]_block_invoke"
+ "-[MIFileManager volumeUUIDForURL:error:]"
+ "-[MIGlobalConfiguration _ixDataStorageHomeURLWithError:]"
+ "-[MIMCMContainer dealloc]"
+ "-[MIPersonaAttributes dealloc]"
+ "-[MIStagingRootAbsolute resolveRootWithError:]_block_invoke"
+ "-[MIUserManagement allPersonaVolumeDaemonContainersMap]_block_invoke"
+ "-[MIUserManagement personaVolumeDaemonContainerForUUID:]_block_invoke"
+ "/System/Cryptexes/OS/"
+ "12.9999"
+ "@\"<MILocationProtocol>\""
+ "@\"<MIStagingRootProtocol>\""
+ "@\"NSError\"24@?0r*8^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}16"
+ "@\"NSString\"16@0:8"
+ "@\"NSURL\"24@0:8^@16"
+ "@\"NSUUID\""
+ "@\"NSXPCConnection\""
+ "@24@0:8:16"
+ "@24@0:8^v16"
+ "@32@0:8:16@24"
+ "@32@0:8Q16Q24"
+ "@40@0:8:16@24@32"
+ "@40@0:8@16I24B28^@32"
+ "@40@0:8@16^B24^@32"
+ "@40@0:8^@16Q24^@32"
+ "@48@0:8@16@24S32i36^@40"
+ "@48@0:8@16q24@32^@40"
+ "@48@0:8^@16@24Q32^@40"
+ "@52@0:8@16q24@32i40^@44"
+ "@52@0:8@16q24i32@36^@44"
+ "@56@0:8@16@24@32I40B44^@48"
+ "@56@0:8@16Q24@32@40q48"
+ "AppleTVOS"
+ "AppleTVSimulator"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@?0^{?=Qq*Q*QIIIIIIISBC}8^B16"
+ "B40@0:8^{?=[16C][16c][1024c]}16@24^@32"
+ "Consumed sandbox token %lld for container at %@"
+ "Contents"
+ "Could not get access to staging directory"
+ "Could not locate platform for %@ string value \"%@\""
+ "Couldn't get data from xattr named %s on \"%s\""
+ "Couldn't get length for xattr named %s on \"%s\""
+ "Discovered persona %@ type %lu mount %@"
+ "Expected non-NULL extensionHandle for %@"
+ "Failed to chmod %s : %s"
+ "Failed to compute hash for Info.plist at %@"
+ "Failed to construct CFBundle for moved bundle at %@: %@"
+ "Failed to construct path to installcoordinationd daemon container"
+ "Failed to construct path to installd daemon container"
+ "Failed to create an instance of MILocationUserDefined because the app bundle URL supplied was not for an app: ["
+ "Failed to determine volume UUID for daemon container for persona %@ at %@ : %@"
+ "Failed to determine volume UUID for persona volume mount %@ : %@"
+ "Failed to get Info.plist path"
+ "Failed to get XPC connection"
+ "Failed to get daemon container URL from %@"
+ "Failed to get daemon container for persona %@: %@"
+ "Failed to get group container path for group 'systemgroup.com.apple.installcoordinationd'; container_system_group_path_for_identifier returned %llu"
+ "Failed to get installcoordinationd daemon container: %@"
+ "Failed to get installd daemon container: %@"
+ "Failed to get sandbox extension for daemon container for persona %@ at %@"
+ "Failed to get sandbox extension for installcoordinationd's daemon container"
+ "Failed to get sandbox extension for installd's daemon container"
+ "Failed to read ExtensionKit based app extensions for bundle %@: %@"
+ "Failed to refresh persona information: %@"
+ "Failed to release sandbox token %lld for %@ : %s"
+ "Failed to release sandbox token %lld for container %@"
+ "Failed to resolve staging root for unknown staging content type"
+ "Got daemon container at %@ for data separated persona %@ that was not on persona mount %@"
+ "ICLHelperServiceClient"
+ "Info.plist from bundle at path %@ had none of the keys that we expect; %@"
+ "InstallCoordination"
+ "InstalledContentLibrary.MILocationSystemDefinedBase"
+ "InstalledContentLibrary.MILocationSystemDefinedCommon"
+ "InstalledContentLibrary.MILocationUserDefined"
+ "InstalledContentLibrary.MILocationUserDefinedDirectory"
+ "Invalid staging content type: %lu"
+ "Key missing or invalid type when decoding MILocationUserDefined from plist dictionary"
+ "Key missing or invalid type when decoding MILocationUserDefinedDirectory from plist dictionary"
+ "LSRequiresIPhoneOS"
+ "Lacking other hints, because the root of the bundle %@ does not have only a Contents directory, assuming this is not a MacOS app"
+ "Lacking other hints, because the root of the bundle %@ has only a Contents directory, assuming this is a MacOS app"
+ "MIConsumeSandboxExtension"
+ "MICreateCFBundle"
+ "MILoadInfoPlistFromBundleWithError"
+ "MILocation"
+ "MILocationProtocol"
+ "MILocationSystemDefinedBase"
+ "MILocationSystemDefinedBase is currently unsupported"
+ "MILocationSystemDefinedCommon"
+ "MILocationUserDefined"
+ "MILocationUserDefinedDirectory"
+ "MIReleaseSandboxExtensionHandle"
+ "MIStagingLocation"
+ "MIStagingRootAbsolute"
+ "MIStagingRootProtocol"
+ "MIStagingRootVolumeUUID"
+ "MI_ALLOW_SWITCHING_PERSONAS_ON_INTERNAL_BUILD"
+ "MacOS"
+ "MacOSX"
+ "Missing location type"
+ "MobileInstallationHelperServiceProtocol"
+ "NSObject"
+ "Proxy returned error: %@"
+ "Skipping app with no bundle executable at %@ : %@"
+ "SupportsAppMigration"
+ "T#,R"
+ "T@\"<MILocationProtocol>\",&,N,V_location"
+ "T@\"<MIStagingRootProtocol>\",R,N,V_stagingRoot"
+ "T@\"NSDictionary\",&,N,V_personaVolumeUUIDToDaemonContainerMap"
+ "T@\"NSDictionary\",N,R"
+ "T@\"NSString\",&,N,V_archNameString"
+ "T@\"NSString\",&,N,V_relativeStagingBaseDirectory"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",N,R"
+ "T@\"NSString\",R,C"
+ "T@\"NSURL\",N,R"
+ "T@\"NSURL\",N,R,V_appBundleURL"
+ "T@\"NSURL\",N,R,V_targetDirectoryURL"
+ "T@\"NSURL\",R,C,N,V_bundleParentDirectoryURL"
+ "T@\"NSURL\",R,N,V_installcoordinationdPath"
+ "T@\"NSURL\",R,N,V_installcoordinationdUserDataLibraryDirectory"
+ "T@\"NSURL\",R,N,V_ixDataStorageDirectoryPath"
+ "T@\"NSURL\",R,N,V_volumeDaemonContainer"
+ "T@\"NSUUID\",R,N,V_volumeUUID"
+ "T@\"NSXPCConnection\",&,N,V_xpcConnection"
+ "TB,N,R"
+ "TB,N,V_supportsAppMigration"
+ "TB,R,N,V_hasExecutable"
+ "TI,R,N,V_ixDaemonGID"
+ "TI,R,N,V_ixDaemonUID"
+ "TI,R,N,V_platformHint"
+ "TQ,N,V_betaTesterType"
+ "TQ,N,V_installerEpoch"
+ "TQ,R"
+ "TQ,R,N,V_stagingContentType"
+ "TQ,R,N,V_stagingSubsystem"
+ "Temporary"
+ "The appex bundle at %@ does not have a bundle executable at %@. App extensions must have an executable."
+ "This bundle does not have an executable, so executable image slices are not available."
+ "This platform does not support location type "
+ "Tq,N,R"
+ "Tq,N,V_extensionHandle"
+ "Tq,R,N,V_extensionHandle"
+ "Tq,R,N,V_sandboxToken"
+ "T{os_unfair_lock_s=I},R,N,V_lock"
+ "URLByDeletingPathExtension"
+ "URLByStandardizingPath"
+ "URLForLocation:isAppBundle:error:"
+ "Unable to compute relative executable path from base URL: \"%@\" executable URL: \"%@\""
+ "Unable to determine if bundle executable is present at \"%@\"."
+ "Unknown location type"
+ "Unknown location type ["
+ "Vv16@0:8"
+ "WatchOS"
+ "WatchSimulator"
+ "XROS"
+ "XRSimulator"
+ "[%@/%@/%@]"
+ "[f]getxattr failed for xattr named %s path %s fd %d"
+ "[f]getxattr failed to get length for xattr named %s path %s fd %d"
+ "[system-defined]"
+ "[user-defined-directory/"
+ "] does not match the expected location type "
+ "^{_NSZone=}16@0:8"
+ "_appBundleURL"
+ "_archNameString"
+ "_betaTesterType"
+ "_doInitWithBundleID:personaUniqueString:location:"
+ "_dynamicPropertyLock"
+ "_extensionHandle"
+ "_firstAvailableParentForURL:error:"
+ "_getBundleRootContainsOnlyContentsDirectory:error:"
+ "_hasExecutable"
+ "_installcoordinationdPath"
+ "_installcoordinationdUserDataLibraryDirectory"
+ "_installerEpoch"
+ "_invalidateObject"
+ "_ixDaemonGID"
+ "_ixDaemonUID"
+ "_ixDataStorageDirectoryPath"
+ "_ixDataStorageHomeURLWithError:"
+ "_location"
+ "_locationClassCluster"
+ "_lock"
+ "_performWithLaunchPersona:"
+ "_personaVolumeUUIDToDaemonContainerMap"
+ "_platformHint"
+ "_relativeStagingBaseDirectory"
+ "_remoteObjectProxyWithErrorHandler:"
+ "_runWithLock:"
+ "_sandboxToken"
+ "_setBundleParentDirectoryURL:forBundleArray:error:"
+ "_sharedConnection"
+ "_stagingContentType"
+ "_stagingRoot"
+ "_stagingRootClassCluster"
+ "_stagingSubsystem"
+ "_supportsAppMigration"
+ "_synchronousRemoteObjectProxyWithErrorHandler:"
+ "_targetDirectoryURL"
+ "_traverseUntilFirstAvailableParentOfURL:withBlock:"
+ "_volumeDaemonContainer"
+ "_volumeUUID"
+ "absoluteURL"
+ "addDataSeparatedAppsWithBundleIDs:toPersona:withCompletion:"
+ "allPersonaVolumeDaemonContainersMap"
+ "allStagingLocationsWithinSubsystem:completion:"
+ "apfs"
+ "app identity has nil location"
+ "appBundleURL"
+ "appletvos"
+ "appletvsimulator"
+ "archNameString"
+ "autorelease"
+ "betaTesterType"
+ "bundleForURL:platformHint:forceAsPlaceholder:error:"
+ "bundleInfoPlistSupportedPlatforms"
+ "checkExecutableExistsIfRequiredWithError:"
+ "class"
+ "com.apple.MobileInstallationHelperService"
+ "com.apple.app-migration"
+ "com.apple.installcoordinationd"
+ "conformsToProtocol:"
+ "contentsURL"
+ "copyVolumeInfo:forURL:error:"
+ "createAppSnapshotWithBundleID:snapshotToURL:onlyV1AppIfPresent:placeholderOnly:completion:"
+ "createRelativeDirectoryPath:inBaseDirectory:mode:class:error:"
+ "createSafeHarborWithIdentifier:forPersona:containerType:andMigrateDataFrom:completion:"
+ "createSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:withCompletion:"
+ "currentUserInstallCoordinationCachesDirectory"
+ "daemonContainerForIdentifier:personaUniqueString:error:"
+ "daemonContainerForPersona:error:"
+ "debugDescription"
+ "denormalizedURLForCFBundleURL:"
+ "driverkit"
+ "enumerateExternalVolumesWithBlock:"
+ "extensionHandle"
+ "getIsBuiltForMacPlatform:error:"
+ "getattrlist failed for %@: %s"
+ "getmntinfo_r_np failed: %s"
+ "getxattr for xattr named %s on \"%s\" returned %zd (expected %zu)"
+ "hasExecutable"
+ "iPhoneOS"
+ "iPhoneSimulator"
+ "identityByChangingLocation:"
+ "infoPlistHashWithError:"
+ "infoPlistURL"
+ "init()"
+ "init(internal:)"
+ "initFromPlistDictionary:error:"
+ "initInternal"
+ "initWithAppBundleURL:error:"
+ "initWithAppBundleURLInternal:"
+ "initWithBundleID:personaUniqueString:location:"
+ "initWithBundleIdentifier:personaUniqueString:"
+ "initWithBundleIdentifier:personaUniqueString:location:"
+ "initWithBundleParentURL:parentSubdirectory:bundleName:platformHint:forceAsPlaceholder:error:"
+ "initWithBundleURL:platformHint:forceAsPlaceholder:error:"
+ "initWithContainerURL:expectAppWithin:error:"
+ "initWithDomain:code:userInfo:"
+ "initWithParentBundle:parentSubdirectory:bundleName:platformHint:forceAsPlaceholder:error:"
+ "initWithPersonaString:personaType:associatedBundleIDs:volumeDaemonContainer:volumeDaemonContainerSandboxExtension:"
+ "initWithServiceName:"
+ "initWithStagingRoot:relativeStagingBaseDirectory:"
+ "initWithStagingSubsystem:contentType:"
+ "initWithTargetDirectoryURL:error:"
+ "initWithTargetDirectoryURLInternal:"
+ "initWithUUIDBytes:"
+ "initWithVolumeUUID:stagingSubsystem:"
+ "installCoordinationStagingWithError:"
+ "installcoordinationdPath"
+ "installcoordinationdUserDataLibraryDirectory"
+ "installerEpoch"
+ "iphoneos"
+ "iphonesimulator"
+ "isDataContainerEmpty:ofContainerType:completion:"
+ "isEqualToLocationSystemDefinedBase:"
+ "isEqualWithLocationSystemDefinedCommon:"
+ "isEqualWithLocationUserDefined:"
+ "isEqualWithLocationUserDefinedDirectory:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "ixDaemonGID"
+ "ixDaemonUID"
+ "ixDataStorageDirectoryPath"
+ "location"
+ "locationFromPlistDictionary:error:"
+ "lock"
+ "macosx"
+ "makeSymlinkFromAppDataContainerToBundleForIdentifier:forPersona:completion:"
+ "migrateMobileContentWithCompletion:"
+ "mountPointForURL:error:"
+ "mountPointForVolumeUUID:error:"
+ "moveItemInStagingLocation:atRelativePath:toDestinationURL:onBehalfOf:completion:"
+ "new"
+ "objectEnumerator"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "personaLayoutPathURL"
+ "personaVolumeDaemonContainerForUUID:"
+ "personaVolumeUUIDToDaemonContainerMap"
+ "platformHint"
+ "plistDictionary"
+ "plistDictionaryFromLocation:"
+ "plistTypeName"
+ "plugInsDirectoryURL"
+ "privilegedResolveRootWithError:"
+ "relativeStagingBaseDirectory"
+ "release"
+ "removeDataSeparatedAppsWithBundleIDs:fromPersona:withCompletion:"
+ "resolveRootWithError:"
+ "resolveStagingBaseWithSandboxExtension:forVolumeUUID:withinStagingSubsystem:error:"
+ "resolveStagingBaseWithSandboxExtensionForVolumeUUID:withinStagingSubsystem:completion:"
+ "resolveWithError:"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "sandboxToken"
+ "sandbox_extension_consume for %s failed: %s."
+ "self"
+ "setArchNameString:"
+ "setBetaTesterType:"
+ "setBundleParentDirectoryURL:error:"
+ "setDataSeparatedAppsWithBundleIDs:withPersona:withCompletion:"
+ "setExtensionHandle:"
+ "setInfoPlistSubsetForTesting:"
+ "setInstallerEpoch:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setLocation:"
+ "setOwnershipAtURL:toUID:gid:error:"
+ "setPersonaVolumeUUIDToDaemonContainerMap:"
+ "setRelativeStagingBaseDirectory:"
+ "setSupportsAppMigration:"
+ "setTestModeForIdentifierPrefix:testMode:validationData:"
+ "setTestingEnabled:"
+ "setXpcConnection:"
+ "stageItemAtURL:toStagingLocation:options:completion:"
+ "stagingContentType"
+ "stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:completion:"
+ "stagingLocationForSystemContentWithinSubsystem:completion:"
+ "stagingLocationForURL:withinStagingSubsytem:usingUniqueName:completion:"
+ "stagingLocationForUserContentWithinSubsystem:completion:"
+ "stagingRoot"
+ "stagingSubsystem"
+ "stagingURLWithSandboxExtension:forSystemContentWithinSubsystem:error:"
+ "stagingURLWithSandboxExtension:forUserContentWithinSubsystem:error:"
+ "stagingURLWithSandboxExtensionForSystemContentWithinSubsystem:completion:"
+ "stagingURLWithSandboxExtensionForUserContentWithinSubsystem:completion:"
+ "statfs failed for %@: %s"
+ "stringWithCString:encoding:"
+ "superclass"
+ "supportsAppMigration"
+ "switchingPersonasEnabled"
+ "systemgroup.com.apple.installcoordinationd"
+ "targetDirectoryURL"
+ "transferOwnershipOfSandboxExtensionToCaller"
+ "v24@0:8q16"
+ "v24@?0@\"NSUUID\"8@\"NSError\"16"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"NSUUID\"@\"NSError\">24"
+ "v32@0:8Q16@?<v@?@\"MIStagingLocation\"@\"NSError\">24"
+ "v32@0:8Q16@?<v@?@\"NSSet\"@\"NSError\">24"
+ "v32@0:8Q16@?<v@?@\"NSURL\"@\"NSString\"@\"NSError\">24"
+ "v32@?0@\"NSURL\"8@\"NSString\"16@\"NSError\"24"
+ "v32@?0@\"NSURL\"8@\"NSUUID\"16^B24"
+ "v40@0:8@\"NSSet\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16Q24@\"NSDictionary\"32"
+ "v40@0:8@\"NSURL\"16Q24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSUUID\"16Q24@?<v@?@\"NSURL\"@\"NSString\"@\"NSError\">32"
+ "v40@0:8@16Q24@32"
+ "v48@0:8@\"<MILocationProtocol>\"16Q24@\"NSString\"32@?<v@?@\"MIStagingLocation\"@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSURL\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSURL\"24B32B36@?<v@?@\"NSDictionary\"@\"NSError\">40"
+ "v48@0:8@\"NSURL\"16@\"MIStagingLocation\"24@\"MIInstallOptions\"32@?<v@?@\"NSURL\"B@\"NSError\">40"
+ "v48@0:8@\"NSURL\"16Q24@\"NSString\"32@?<v@?@\"MIStagingLocation\"@\"NSError\">40"
+ "v48@0:8@16@24B32B36@?40"
+ "v56@0:8@\"NSString\"16@\"NSString\"24Q32@\"NSURL\"40@?<v@?@\"NSError\">48"
+ "v80@0:8@\"MIStagingLocation\"16@\"NSString\"24@\"NSURL\"32{?=[8I]}40@?<v@?@\"NSError\">72"
+ "v80@0:8@16@24@32{?=[8I]}40@?72"
+ "validateURL:forLocation:error:"
+ "validateWithURLonEmbedded:forLocation:error:"
+ "volumeDaemonContainer"
+ "volumeUUID"
+ "volumeUUIDForLocation:error:"
+ "volumeUUIDForURL:completion:"
+ "volumeUUIDForURL:error:"
+ "watchos"
+ "watchsimulator"
+ "wipeStagingRootAndSetUpPerUserDataDirWithCompletion:"
+ "xattr named %s not present on \"%s\""
+ "xpcConnection"
+ "xros"
+ "xrsimulator"
+ "zone"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "{os_unfair_lock_s=I}16@0:8"
- "!'"
- "%s: Defaulting to system staging root because we could not determine the best one for %@"
- "%s: Failed to consume daemon container sandbox token: %d (%s)"
- "%s: Failed to create container query"
- "-[MIAppIdentity initWithBundleID:persona:]"
- "-[MIBundle infoPlistSubset]"
- "-[MIBundleContainer initForAppContainerWithURL:]"
- "-[MIDaemonConfiguration stagingRootForDevice:url:identifier:error:]"
- "-[MIDaemonConfiguration stagingRootForIdentifier:]"
- "-[MIExecutableBundle executableExistsWithError:]"
- "-[MIFileManager deviceForURLOrFirstAvailableParent:error:]"
- "/private/var/PersonaVolumes/"
- "/var/PersonaVolumes/"
- "11.9999"
- "@40@0:8@16Q24@32"
- "@40@0:8@16^Q24^@32"
- "@44@0:8i16@20^Q28^@36"
- "@52@0:8@16@24@32B40^@44"
- "@52@0:8@16Q24@32i40^@44"
- "@52@0:8@16Q24i32@36^@44"
- "Attr named %s not present on \"%s\""
- "B24@?0^{?=Qq*Q*QQIIIIIISBC}8^B16"
- "Consumed sandbox token %lld for container at %s"
- "Couldn't get data from EA named %s on \"%s\": %s"
- "Defaulting to system staging root because we could not determine the best one for %@"
- "Failed to chmod %@ : %s"
- "Failed to create container query"
- "Failed to execute lookup query for daemon container: %s"
- "Forcing system staging root for persona volume path %@"
- "Got NULL container path for daemon data container %s"
- "Got unknown staging root identifier: %lu"
- "Got user container URL %s from containermanagerd"
- "Info.plist loaded from %@ had no keys!"
- "MILoadInfoPlistWithError"
- "Skipping app with no bundle executable at %@"
- "T@\"NSURL\",C,N,V_bundleParentDirectoryURL"
- "[f]getxattr failed for path %s fd %d"
- "_CreateCFBundle"
- "_DaemonUserDataLibraryDirectory"
- "a"
- "com.apple.mobile.installd.staging"
- "createSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:onDevice:withCompletion:"
- "executableExistsWithError:"
- "getxattr for EA named %s on \"%s\" returned %zd (expected %zu)"
- "infoPlistSubsetForTesting:"
- "initFileURLWithFileSystemRepresentation:isDirectory:relativeToURL:"
- "initForAppContainerWithURL:"
- "initWithParentBundle:parentSubdirectory:bundleName:error:"
- "initWithParentBundle:parentSubdirectory:bundleName:isPlaceholder:error:"
- "initWithPersonaString:personaType:associatedBundleIDs:"
- "setBundleParentDirectoryURL:"
- "stagingRootForDevice:url:identifier:error:"
- "stagingRootForIdentifier:"
- "stagingRootForSystemContent"
- "stagingRootForURL:identifier:error:"
- "stagingRootForUserContent"
- "v32@?0@\"NSURL\"8@\"NSNumber\"16^B24"
- "v52@0:8@\"NSString\"16@\"NSString\"24@\"NSURL\"32i40@?<v@?@\"NSError\">44"
- "v52@0:8@16@24@32i40@?44"

```
