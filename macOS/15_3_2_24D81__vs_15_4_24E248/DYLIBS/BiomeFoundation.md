## BiomeFoundation

> `/System/Library/PrivateFrameworks/BiomeFoundation.framework/Versions/A/BiomeFoundation`

```diff

-165.7.0.0.0
-  __TEXT.__text: 0x34bfc
-  __TEXT.__auth_stubs: 0xb20
-  __TEXT.__objc_methlist: 0x2294
-  __TEXT.__const: 0x1a8
-  __TEXT.__cstring: 0x449d
-  __TEXT.__oslogstring: 0x2ece
-  __TEXT.__gcc_except_tab: 0xe04
-  __TEXT.__dlopen_cstrs: 0x22a
-  __TEXT.__unwind_info: 0xcd8
-  __TEXT.__objc_classname: 0x5dc
-  __TEXT.__objc_methname: 0x51ea
-  __TEXT.__objc_methtype: 0x1086
-  __TEXT.__objc_stubs: 0x4420
-  __DATA_CONST.__got: 0x350
-  __DATA_CONST.__const: 0x740
-  __DATA_CONST.__objc_classlist: 0x1a0
-  __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x70
+166.17.1.0.0
+  __TEXT.__text: 0x3bd14
+  __TEXT.__auth_stubs: 0xc50
+  __TEXT.__objc_methlist: 0x29b4
+  __TEXT.__const: 0x21a
+  __TEXT.__cstring: 0x4e06
+  __TEXT.__oslogstring: 0x3453
+  __TEXT.__gcc_except_tab: 0xe78
+  __TEXT.__dlopen_cstrs: 0x2d4
+  __TEXT.__constg_swiftt: 0x64
+  __TEXT.__swift5_typeref: 0x21
+  __TEXT.__swift5_reflstr: 0x2f
+  __TEXT.__swift5_fieldmd: 0x44
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__unwind_info: 0xe60
+  __TEXT.__objc_classname: 0x658
+  __TEXT.__objc_methname: 0x5965
+  __TEXT.__objc_methtype: 0x114a
+  __TEXT.__objc_stubs: 0x4a60
+  __DATA_CONST.__got: 0x388
+  __DATA_CONST.__const: 0x878
+  __DATA_CONST.__objc_classlist: 0x1c0
+  __DATA_CONST.__objc_catlist: 0x28
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15c0
-  __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x148
-  __DATA_CONST.__objc_arraydata: 0x12b0
-  __AUTH_CONST.__auth_got: 0x5a0
-  __AUTH_CONST.__const: 0x950
-  __AUTH_CONST.__cfstring: 0x50c0
-  __AUTH_CONST.__objc_const: 0x6928
-  __AUTH_CONST.__objc_intobj: 0x1b0
-  __AUTH_CONST.__objc_arrayobj: 0x588
-  __AUTH_CONST.__objc_dictobj: 0x190
-  __AUTH.__objc_data: 0x1040
-  __DATA.__objc_ivar: 0x240
-  __DATA.__data: 0x700
-  __DATA.__bss: 0x280
+  __DATA_CONST.__objc_selrefs: 0x1820
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0x160
+  __DATA_CONST.__objc_arraydata: 0x1328
+  __AUTH_CONST.__auth_got: 0x638
+  __AUTH_CONST.__const: 0xaa0
+  __AUTH_CONST.__cfstring: 0x5700
+  __AUTH_CONST.__objc_const: 0x6830
+  __AUTH_CONST.__objc_intobj: 0x1e0
+  __AUTH_CONST.__objc_arrayobj: 0x5b8
+  __AUTH_CONST.__objc_dictobj: 0x1b8
+  __AUTH.__objc_data: 0x11f0
+  __AUTH.__data: 0x28
+  __DATA.__objc_ivar: 0x280
+  __DATA.__data: 0x768
+  __DATA.__bss: 0x2d0
+  __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DC716F79-CF65-3EFE-9E03-73E6BBEF9A10
-  Functions: 1105
-  Symbols:   2918
-  CStrings:  2803
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  UUID: 4BDCDBA0-4BF7-3992-86BF-50DAA6F8C94B
+  Functions: 1250
+  Symbols:   3324
+  CStrings:  3033
 
Symbols:
+ +[BMAccessAssertionCache sharedCache].cold.1
+ +[BMAccessControlPolicy(SyncableSets) syncableSetIdentifiers]
+ +[BMAccessControlPolicy(SyncableSets) syncableSetIdentifiers].cold.1
+ +[BMAccessTracker sharedInstance].cold.1
+ +[BMDataProtection sharedInstance].cold.1
+ +[BMFileBackedCounter new]
+ +[BMFileBackedDictionary new]
+ +[BMFileManager globalWeakFileHandleCache].cold.1
+ +[BMPaths pathForSharedSyncWithAccount:domain:].cold.1
+ +[BMPaths(PrivacyUtilities) privacyPathname:].cold.1
+ +[BMPaths(Sets) allSetsResourceSpecifierWithOptions:]
+ +[BMPaths(TestingSupport_Project) setBasePathForTestingWithPath:].cold.1
+ +[BMProcess current].cold.1
+ +[BMResourceContainerAvailabilityMonitor sharedMonitor].cold.1
+ +[BMResourceContainerManager sharedInstance].cold.1
+ +[BMResourceDescriptor _illegalCharactersSet].cold.1
+ +[BMXPCConnectionFactory _configureConnection:serviceType:useCase:]
+ +[BMXPCConnectionFactory connectionToAccessServerInDomain:user:useCase:]
+ +[BMXPCConnectionFactory connectionToComputeSourceServerInDomain:user:useCase:]
+ +[BMXPCConnectionFactory connectionToFileServerInDomain:user:useCase:]
+ +[BMXPCConnectionFactory connectionToMachService:endpoint:useCase:]
+ +[BMXPCConnectionFactory defaultQueue]
+ +[BMXPCConnectionFactory defaultQueue].cold.1
+ +[BMXPCConnectionFactory delegate]
+ +[BMXPCConnectionFactory globalStrongConnectionCache]
+ +[BMXPCConnectionFactory globalStrongConnectionCache].cold.1
+ +[BMXPCConnectionFactory globalWeakConnectionCache]
+ +[BMXPCConnectionFactory globalWeakConnectionCache].cold.1
+ +[BMXPCConnectionFactory remoteObjectInterfaceForMachServiceType:]
+ +[BMXPCConnectionFactory remoteObjectInterfaceForMachServiceType:].cold.1
+ +[BMXPCConnectionFactory setDelegate:]
+ +[BMXPCListener serviceListener].cold.1
+ +[NSMapTable(Biome) unownedToStrongObjectsMapTable]
+ +[NSUUID(BMUtilities) bm_bootSessionUUID].cold.1
+ +[NSXPCConnection(BMXPCListener) bm_connectionWithPeer:queue:]
+ -[BMAccessAssertionCache _invalidateCacheIfPersonaSwitched]
+ -[BMAccessAssertionCache _sandboxExtensionWithDescriptor:extensionToken:container:path:]
+ -[BMAccessAssertionCache releaseAssertion:]
+ -[BMAccessControlPolicy allowsAccessToAllSetsWithMode:]
+ -[BMAccessControlPolicy allowsAccessToSyncMergeableDeltas]
+ -[BMAccessControlPolicy allowsConnectionToComputeSourceServiceWithDomain:]
+ -[BMAccessControlPolicy(DaemonToAgent) allowsAccessToBiomeAgentForUser:].cold.2
+ -[BMAccessServer requestEndpointForProxyingConnectionsWithReply:]
+ -[BMAccessServer requestEndpointForService:user:reply:]
+ -[BMAccessServiceListener _acceptConnection:].cold.1
+ -[BMAccessServiceListener replyToInvocation:withError:].cold.4
+ -[BMAccount initWithAltDSID:].cold.1
+ -[BMAccount initWithIdentifier:].cold.2
+ -[BMCache pruneCacheWithBlock:completion:].cold.1
+ -[BMDataProtection _registerForLockStateChanges:]
+ -[BMDataProtection _unregister:]
+ -[BMFileAttributes initWithPath:mode:protectionClass:].cold.1
+ -[BMFileBackedCounter .cxx_destruct]
+ -[BMFileBackedCounter _atomicallyCreateFileWithDictionary:error:]
+ -[BMFileBackedCounter _atomicallyCreateFileWithDictionary:error:].cold.1
+ -[BMFileBackedCounter _atomicallyCreateFileWithDictionary:error:].cold.2
+ -[BMFileBackedCounter _atomicallyWriteFileWithDictionary:error:]
+ -[BMFileBackedCounter _atomicallyWriteFileWithDictionary:error:].cold.1
+ -[BMFileBackedCounter _countFromFileDictionary:]
+ -[BMFileBackedCounter _createFileIfNotExists:]
+ -[BMFileBackedCounter _createFileIfNotExists:].cold.1
+ -[BMFileBackedCounter _decodeFileDictionary:error:]
+ -[BMFileBackedCounter _decodeFileDictionary:error:].cold.1
+ -[BMFileBackedCounter _decodeFileDictionary:error:].cold.2
+ -[BMFileBackedCounter _encodeFileDictionary:error:]
+ -[BMFileBackedCounter _encodeFileDictionary:error:].cold.1
+ -[BMFileBackedCounter _fileUUIDFromFileDictionary:]
+ -[BMFileBackedCounter _loadFileDictionary:]
+ -[BMFileBackedCounter _loadFileDictionary:].cold.1
+ -[BMFileBackedCounter _newFileDictionaryWithFileUUID:count:error:]
+ -[BMFileBackedCounter _readableFileDictionary:]
+ -[BMFileBackedCounter fileUUID]
+ -[BMFileBackedCounter incrementCount:error:]
+ -[BMFileBackedCounter incrementCount:error:].cold.1
+ -[BMFileBackedCounter initWithFilename:protectionClass:directory:domain:error:]
+ -[BMFileBackedCounter init]
+ -[BMFileBackedDictionary .cxx_destruct]
+ -[BMFileBackedDictionary _loadDictionaryOrCreate:readOnly:initialDictionary:error:]
+ -[BMFileBackedDictionary _loadDictionaryOrCreate:readOnly:initialDictionary:error:].cold.1
+ -[BMFileBackedDictionary _loadDictionaryOrCreate:readOnly:initialDictionary:error:].cold.2
+ -[BMFileBackedDictionary _loadDictionaryOrCreate:readOnly:initialDictionary:error:].cold.3
+ -[BMFileBackedDictionary _loadDictionaryOrCreate:readOnly:initialDictionary:error:].cold.4
+ -[BMFileBackedDictionary allKeys]
+ -[BMFileBackedDictionary clear:]
+ -[BMFileBackedDictionary clear:].cold.1
+ -[BMFileBackedDictionary clearObjectForKey:error:]
+ -[BMFileBackedDictionary clearObjectForKey:error:].cold.1
+ -[BMFileBackedDictionary clearObjectForKey:error:].cold.2
+ -[BMFileBackedDictionary clearObjectForKey:error:].cold.3
+ -[BMFileBackedDictionary count]
+ -[BMFileBackedDictionary description]
+ -[BMFileBackedDictionary initWithFilename:protectionClass:directory:readOnly:create:initialDictionary:error:]
+ -[BMFileBackedDictionary init]
+ -[BMFileBackedDictionary isReadOnly]
+ -[BMFileBackedDictionary mutableDictionaryForKey:error:]
+ -[BMFileBackedDictionary mutableDictionaryForKey:error:].cold.1
+ -[BMFileBackedDictionary objectForKey:]
+ -[BMFileBackedDictionary writeUpdatedObject:forKey:error:]
+ -[BMFileBackedDictionary writeUpdatedObjects:forKeys:error:]
+ -[BMFileBackedDictionary writeUpdatedObjects:forKeys:error:].cold.1
+ -[BMFileHandle nsFileHandle].cold.2
+ -[BMFileHandle overwriteWithData:error:].cold.1
+ -[BMFileHandle performWithInProcessLock:].cold.1
+ -[BMFileHandle readDataWithError:].cold.1
+ -[BMFileManager acquireLockfile:andRunBlock:].cold.3
+ -[BMFileManager changePermissionsOfFileAtPath:mode:error:].cold.2
+ -[BMFileManager contentsOfDirectoryAtPath:error:].cold.2
+ -[BMFileManager createDirectoryAtPath:error:].cold.2
+ -[BMFileManager dataWithContentsOfFileAtPath:error:].cold.2
+ -[BMFileManager fileExistsAtPath:error:].cold.2
+ -[BMFileManager fileHandleForFileAtPath:flags:protection:error:].cold.2
+ -[BMFileManager modificationTimeOfFileAtPath:error:].cold.2
+ -[BMFileManager removeDirectoryAtPath:error:].cold.2
+ -[BMFileManager removeFileAtPath:error:].cold.2
+ -[BMFileManager replaceFileAtPath:withData:protection:flags:error:]
+ -[BMFileManager replaceFileAtPath:withFileHandle:protection:flags:error:]
+ -[BMFileManager sizeOfFileAtPath:error:].cold.2
+ -[BMFileServer allowedToAccessStream:withMode:error:]
+ -[BMFileServer initWithDirectory:].cold.1
+ -[BMFileServer initWithDirectory:library:]
+ -[BMFileServer isPrimaryDaemon]
+ -[BMFileServer replaceFileAtPath:withFileHandle:protection:flags:reply:]
+ -[BMFileServer replaceFileAtPath:withFileHandle:protection:flags:reply:].cold.1
+ -[BMFileServer replaceFileAtPath:withFileHandle:protection:flags:reply:].cold.2
+ -[BMFileServer replaceFileAtPath:withFileHandle:protection:flags:reply:].cold.3
+ -[BMFileServer replaceFileAtPath:withFileHandle:protection:flags:reply:].cold.4
+ -[BMIndirectHeap initWithHeapSize:isAscending:].cold.1
+ -[BMProcessCurrent _session]
+ -[BMProcessCurrent _session].cold.1
+ -[BMProcessCurrent canAccessAppleKeyStore]
+ -[BMProcessCurrent isManagedByLaunchd].cold.1
+ -[BMProcessCurrent isManagedByRunningBoard].cold.1
+ -[BMXPCConnectionFactory .cxx_destruct]
+ -[BMXPCConnectionFactory _configureConnection:]
+ -[BMXPCConnectionFactory _connectionFlags]
+ -[BMXPCConnectionFactory _legacyUserDomainConnection]
+ -[BMXPCConnectionFactory _newConnection]
+ -[BMXPCConnectionFactory _newConnection].cold.1
+ -[BMXPCConnectionFactory _proxyConnectionThroughBiomeDaemon]
+ -[BMXPCConnectionFactory _proxyConnectionThroughBiomeDaemon].cold.1
+ -[BMXPCConnectionFactory _proxyConnectionThroughCoreDuet]
+ -[BMXPCConnectionFactory _regularConnection]
+ -[BMXPCConnectionFactory _requestConnectionFromCaller]
+ -[BMXPCConnectionFactory _requestConnectionFromCaller].cold.1
+ -[BMXPCConnectionFactory _targetUserConnection]
+ -[BMXPCConnectionFactory connectionIsCrossUser]
+ -[BMXPCConnectionFactory coreDuetMachService]
+ -[BMXPCConnectionFactory coreDuetMachService].cold.1
+ -[BMXPCConnectionFactory coreDuetMachService].cold.2
+ -[BMXPCConnectionFactory currentProcessCanDirectlyConnectCrossUser]
+ -[BMXPCConnectionFactory delegate]
+ -[BMXPCConnectionFactory initWithType:domain:user:useCase:]
+ -[BMXPCConnectionFactory machServiceName]
+ -[BMXPCConnectionFactory makeConnectionWrapper]
+ -[BMXPCConnectionFactory setDelegate:]
+ -[BMXPCConnectionFactory user]
+ -[NSXPCConnection(BiomeAccessControl) bm_accessControlPolicy]
+ -[NSXPCConnection(BiomeAccessControl) bm_connectionFlags]
+ -[NSXPCConnection(BiomeAccessControl) bm_process]
+ -[NSXPCConnection(BiomeAccessControl) setBm_accessControlPolicy:]
+ -[NSXPCConnection(BiomeAccessControl) setBm_connectionFlags:]
+ -[NSXPCConnection(BiomeUserInfo) bm_userInfo]
+ -[_BMDirectFileManager replaceFileAtPath:withData:protection:flags:error:]
+ -[_BMDirectFileManager replaceFileAtPath:withData:protection:flags:error:].cold.1
+ -[_BMDirectFileManager replaceFileAtPath:withData:protection:flags:error:].cold.2
+ -[_BMDirectFileManager replaceFileAtPath:withData:protection:flags:error:].cold.3
+ -[_BMDirectFileManager replaceFileAtPath:withData:protection:flags:error:].cold.4
+ -[_BMDirectFileManager replaceFileAtPath:withData:protection:flags:error:].cold.5
+ -[_BMDirectFileManager replaceFileAtPath:withFileHandle:protection:flags:error:]
+ -[_BMDirectFileManager replaceFileAtPath:withFileHandle:protection:flags:error:].cold.1
+ -[_BMDirectFileManager replaceFileAtPath:withFileHandle:protection:flags:error:].cold.2
+ -[_BMDirectFileManager replaceFileAtPath:withFileHandle:protection:flags:error:].cold.3
+ -[_BMDirectFileManager replaceFileAtPath:withFileHandle:protection:flags:error:].cold.4
+ -[_BMDirectFileManager replaceFileAtPath:withFileHandle:protection:flags:error:].cold.5
+ -[_BMSandboxExtension .cxx_destruct]
+ -[_BMSandboxExtension container]
+ -[_BMSandboxExtension dealloc]
+ -[_BMSandboxExtension dealloc].cold.1
+ -[_BMSandboxExtension dealloc].cold.2
+ -[_BMSandboxExtension descriptor]
+ -[_BMSandboxExtension initWithDescriptor:extensionToken:container:path:]
+ -[_BMSandboxExtension initWithDescriptor:extensionToken:container:path:].cold.1
+ -[_BMSandboxExtension initWithDescriptor:extensionToken:container:path:].cold.2
+ -[_BMSandboxExtension path]
+ -[_BMSandboxExtensionAccessAssertion .cxx_destruct]
+ -[_BMSandboxExtensionAccessAssertion container]
+ -[_BMSandboxExtensionAccessAssertion copyWithZone:]
+ -[_BMSandboxExtensionAccessAssertion dealloc]
+ -[_BMSandboxExtensionAccessAssertion descriptor]
+ -[_BMSandboxExtensionAccessAssertion hash]
+ -[_BMSandboxExtensionAccessAssertion initWithDescriptor:container:]
+ -[_BMSandboxExtensionAccessAssertion isEqual:]
+ -[_BMSandboxExtensionAccessAssertion path]
+ -[_BMXPCFileManager replaceFileAtPath:withData:protection:flags:error:]
+ -[_BMXPCFileManager replaceFileAtPath:withData:protection:flags:error:].cold.1
+ -[_BMXPCFileManager replaceFileAtPath:withFileHandle:protection:flags:error:]
+ -[_BMXPCFileManager replaceFileAtPath:withFileHandle:protection:flags:error:].cold.1
+ -[_BMXPCTransportContext connection]
+ -[_BMXPCTransportContext setConnection:]
+ BMBiomeLibraryIdentifierForLegacyName.mapping
+ BMBiomeLibraryIdentifierForLegacyName.onceToken
+ BMSyncableStreamIdentifiers.cold.1
+ BMValidatePath.cold.3
+ BMValidatePath.cold.4
+ BMWritePropertyList.cold.1
+ BMWritePropertyList.cold.2
+ CascadeSetsLibraryCore.frameworkLibrary
+ GCC_except_table30
+ GCC_except_table33
+ GCC_except_table36
+ GCC_except_table39
+ GCC_except_table42
+ GCC_except_table48
+ GCC_except_table49
+ GCC_except_table53
+ GCC_except_table60
+ OBJC_IVAR_$_BMAccessAssertionCache._assertionsMap
+ OBJC_IVAR_$_BMAccessAssertionCache._extensionCache
+ OBJC_IVAR_$_BMFileBackedCounter._domain
+ OBJC_IVAR_$_BMFileBackedCounter._fileManager
+ OBJC_IVAR_$_BMFileBackedCounter._filePath
+ OBJC_IVAR_$_BMFileBackedCounter._fileUUID
+ OBJC_IVAR_$_BMFileBackedCounter._lastObservedCount
+ OBJC_IVAR_$_BMFileBackedCounter._lockFilePath
+ OBJC_IVAR_$_BMFileBackedCounter._protectionClass
+ OBJC_IVAR_$_BMFileBackedDictionary._dictionary
+ OBJC_IVAR_$_BMFileBackedDictionary._fileURL
+ OBJC_IVAR_$_BMFileBackedDictionary._protectionClass
+ OBJC_IVAR_$_BMFileServer._library
+ OBJC_IVAR_$_BMXPCConnectionFactory._delegate
+ OBJC_IVAR_$_BMXPCConnectionFactory._domain
+ OBJC_IVAR_$_BMXPCConnectionFactory._path
+ OBJC_IVAR_$_BMXPCConnectionFactory._serviceType
+ OBJC_IVAR_$_BMXPCConnectionFactory._useCase
+ OBJC_IVAR_$_BMXPCConnectionFactory._user
+ OBJC_IVAR_$__BMSandboxExtension._container
+ OBJC_IVAR_$__BMSandboxExtension._descriptor
+ OBJC_IVAR_$__BMSandboxExtension._handle
+ OBJC_IVAR_$__BMSandboxExtension._path
+ OBJC_IVAR_$__BMSandboxExtensionAccessAssertion._container
+ OBJC_IVAR_$__BMSandboxExtensionAccessAssertion._descriptor
+ OBJC_IVAR_$__BMSandboxExtensionAccessAssertion._path
+ OBJC_IVAR_$__BMXPCTransportContext._connection
+ _$s15BiomeFoundation14ManagedSettingV12wrappedValue5namedACSb_SStcfC
+ _$s15BiomeFoundation14ManagedSettingV12wrappedValueSbvg
+ _$s15BiomeFoundation14ManagedSettingV12wrappedValueSbvpMV
+ _$s15BiomeFoundation14ManagedSettingVMF
+ _$s15BiomeFoundation14ManagedSettingVMa
+ _$s15BiomeFoundation14ManagedSettingVMf
+ _$s15BiomeFoundation14ManagedSettingVMn
+ _$s15BiomeFoundation14ManagedSettingVN
+ _$s15BiomeFoundation14ManagedSettingVWV
+ _$s15BiomeFoundation14ManagedSettingVwCP
+ _$s15BiomeFoundation14ManagedSettingVwCPTm
+ _$s15BiomeFoundation14ManagedSettingVwca
+ _$s15BiomeFoundation14ManagedSettingVwcp
+ _$s15BiomeFoundation14ManagedSettingVwet
+ _$s15BiomeFoundation14ManagedSettingVwst
+ _$s15BiomeFoundation14ManagedSettingVwta
+ _$s15BiomeFoundation14ManagedSettingVwxx
+ _$s15BiomeFoundation20ManagedConfigurationC28allowAppleIntelligenceReportSbvg
+ _$s15BiomeFoundation20ManagedConfigurationC28allowAppleIntelligenceReportSbvgTo
+ _$s15BiomeFoundation20ManagedConfigurationC28allowAppleIntelligenceReportSbvgTq
+ _$s15BiomeFoundation20ManagedConfigurationC29_allowAppleIntelligenceReport33_D8E56BE5D4BA6E2318270E282AACB2C1LLAA0C7SettingVvpWvd
+ _$s15BiomeFoundation20ManagedConfigurationC6sharedACvgZ
+ _$s15BiomeFoundation20ManagedConfigurationC6sharedACvgZTo
+ _$s15BiomeFoundation20ManagedConfigurationC6sharedACvpZ
+ _$s15BiomeFoundation20ManagedConfigurationC6shared_WZ
+ _$s15BiomeFoundation20ManagedConfigurationC6shared_Wz
+ _$s15BiomeFoundation20ManagedConfigurationCACycfC
+ _$s15BiomeFoundation20ManagedConfigurationCACycfc
+ _$s15BiomeFoundation20ManagedConfigurationCACycfcTo
+ _$s15BiomeFoundation20ManagedConfigurationCMF
+ _$s15BiomeFoundation20ManagedConfigurationCMa
+ _$s15BiomeFoundation20ManagedConfigurationCMf
+ _$s15BiomeFoundation20ManagedConfigurationCMn
+ _$s15BiomeFoundation20ManagedConfigurationCMo
+ _$s15BiomeFoundation20ManagedConfigurationCMu
+ _$s15BiomeFoundation20ManagedConfigurationCN
+ _$s15BiomeFoundation20ManagedConfigurationCfD
+ _$s15BiomeFoundation20ManagedConfigurationCfETo
+ _$s15BiomeFoundationMXM
+ _$sBOWV
+ _$sSS10FoundationE19_bridgeToObjectiveCSo8NSStringCyF
+ _BMDataFromNSUUID
+ _BMDevicePlatformFromString
+ _BMFileBackedCounterErrorDomain
+ _BMFileBackedDictionaryErrorDomain
+ _BMGetOrCreateDirectoryPath
+ _BMGetOrCreateDirectoryURL
+ _BMMachServiceNameSystemComputePublisherService
+ _BMMachServiceNameSystemComputeSourceService
+ _BMMachServiceNameUserComputePublisherService
+ _BMMachServiceNameUserComputeSourceService
+ _BMPersonaUtilitiesErrorDomain
+ _BMReadPropertyList
+ _BMRemoveItemIfExistsAtPath
+ _BMRemoveItemIfExistsAtURL
+ _BMSetError
+ _BMUseCaseMaintenance
+ _BMValidatedPathTypeResourceGeneration
+ _BMWritePropertyList
+ _CFPreferencesAppValueIsForced
+ _CFPreferencesGetAppBooleanValue
+ _NSProtocolFromString
+ _OBJC_CLASS_$_BMFileBackedCounter
+ _OBJC_CLASS_$_BMFileBackedDictionary
+ _OBJC_CLASS_$_BMXPCConnectionFactory
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$__BMManagedConfiguration
+ _OBJC_CLASS_$__BMSandboxExtension
+ _OBJC_CLASS_$__BMSandboxExtensionAccessAssertion
+ _OBJC_METACLASS_$_BMFileBackedCounter
+ _OBJC_METACLASS_$_BMFileBackedDictionary
+ _OBJC_METACLASS_$_BMXPCConnectionFactory
+ _OBJC_METACLASS_$__BMManagedConfiguration
+ _OBJC_METACLASS_$__BMSandboxExtension
+ _OBJC_METACLASS_$__BMSandboxExtensionAccessAssertion
+ __32+[_BMXPCTransport _handleEvent:]_block_invoke.cold.1
+ __32+[_BMXPCTransport _handleEvent:]_block_invoke.cold.2
+ __32+[_BMXPCTransport _handleEvent:]_block_invoke.cold.3
+ __32+[_BMXPCTransport _handleEvent:]_block_invoke.cold.4
+ __32+[_BMXPCTransport _handleEvent:]_block_invoke.cold.5
+ __47-[BMXPCConnectionFactory makeConnectionWrapper]_block_invoke.13
+ __50-[BMAccessClient(Deletions) removeResource:error:]_block_invoke.132
+ __53-[BMAccessClient requestAccessToResource:mode:error:]_block_invoke.102
+ __54-[BMXPCConnectionFactory _requestConnectionFromCaller]_block_invoke.101
+ __54-[BMXPCConnectionFactory _requestConnectionFromCaller]_block_invoke.101.cold.1
+ __54-[BMXPCConnectionFactory _requestConnectionFromCaller]_block_invoke.cold.1
+ __55-[BMAccessServer requestEndpointForService:user:reply:]_block_invoke.71
+ __57-[BMXPCConnectionFactory _proxyConnectionThroughCoreDuet]_block_invoke.97
+ __57-[BMXPCConnectionFactory _proxyConnectionThroughCoreDuet]_block_invoke.97.cold.1
+ __57-[BMXPCConnectionFactory _proxyConnectionThroughCoreDuet]_block_invoke.cold.1
+ __60-[BMXPCConnectionFactory _proxyConnectionThroughBiomeDaemon]_block_invoke.114
+ __60-[BMXPCConnectionFactory _proxyConnectionThroughBiomeDaemon]_block_invoke.114.cold.1
+ __60-[BMXPCConnectionFactory _proxyConnectionThroughBiomeDaemon]_block_invoke.cold.1
+ __65-[NSXPCConnection(BiomeAccessControl) setBm_accessControlPolicy:]_block_invoke.12
+ __69-[BMAccessClient(ConnectionProxying) requestEndpointForDomain:error:]_block_invoke.127
+ __69-[_BMXPCFileManager _fileHandleForFileAtPath:flags:protection:error:]_block_invoke.30
+ __BMNormalizedResourcesAndAccessModesListedUnderEntitlement_block_invoke.cold.1
+ __BMNormalizedResourcesAndAccessModesListedUnderEntitlement_block_invoke.cold.2
+ __BMNormalizedResourcesAndAccessModesListedUnderEntitlement_block_invoke.cold.3
+ __BMNormalizedResourcesAndAccessModesListedUnderEntitlement_block_invoke.cold.4
+ __BMResourcesAndAccessModesListedUnderEntitlement_block_invoke.319
+ __BMResourcesAndAccessModesListedUnderEntitlement_block_invoke.323
+ __BMResourcesAndAccessModesListedUnderEntitlement_block_invoke.328
+ __CLASS_METHODS__BMManagedConfiguration
+ __CLASS_PROPERTIES__BMManagedConfiguration
+ __DATA__BMManagedConfiguration
+ __INSTANCE_METHODS__BMManagedConfiguration
+ __IVARS__BMManagedConfiguration
+ __METACLASS_DATA__BMManagedConfiguration
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSMapTable_$_Biome
+ __OBJC_$_CATEGORY_NSMapTable_$_Biome
+ __OBJC_$_CATEGORY_NSXPCConnection_$_BiomeUserInfo
+ __OBJC_$_CLASS_METHODS_BMAccessControlPolicy(LegacyViewEntitlement|SyncableSets|SetStoreUpdateService|WriteService|DaemonToAgent|UseCase)
+ __OBJC_$_CLASS_METHODS_BMFileBackedCounter
+ __OBJC_$_CLASS_METHODS_BMFileBackedDictionary
+ __OBJC_$_CLASS_METHODS_BMXPCConnectionFactory
+ __OBJC_$_CLASS_METHODS_NSXPCConnection(BiomeUserInfo|BMXPCListener|BiomeAccessControl|BiomeUseCaseSupport)
+ __OBJC_$_CLASS_PROP_LIST_BMXPCConnectionFactory
+ __OBJC_$_INSTANCE_METHODS_BMAccessControlPolicy(LegacyViewEntitlement|SyncableSets|SetStoreUpdateService|WriteService|DaemonToAgent|UseCase)
+ __OBJC_$_INSTANCE_METHODS_BMFileBackedCounter
+ __OBJC_$_INSTANCE_METHODS_BMFileBackedDictionary
+ __OBJC_$_INSTANCE_METHODS_BMXPCConnectionFactory
+ __OBJC_$_INSTANCE_METHODS_NSXPCConnection(BiomeUserInfo|BMXPCListener|BiomeAccessControl|BiomeUseCaseSupport)
+ __OBJC_$_INSTANCE_METHODS__BMSandboxExtension
+ __OBJC_$_INSTANCE_METHODS__BMSandboxExtensionAccessAssertion
+ __OBJC_$_INSTANCE_VARIABLES_BMFileBackedCounter
+ __OBJC_$_INSTANCE_VARIABLES_BMFileBackedDictionary
+ __OBJC_$_INSTANCE_VARIABLES_BMXPCConnectionFactory
+ __OBJC_$_INSTANCE_VARIABLES__BMSandboxExtension
+ __OBJC_$_INSTANCE_VARIABLES__BMSandboxExtensionAccessAssertion
+ __OBJC_$_PROP_LIST_BMFileBackedCounter
+ __OBJC_$_PROP_LIST_BMXPCConnectionFactory
+ __OBJC_$_PROP_LIST__BMSandboxExtension
+ __OBJC_$_PROP_LIST__BMSandboxExtensionAccessAssertion
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BMConnectionProxyable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BMConnectionProxyable
+ __OBJC_$_PROTOCOL_REFS_BMAccessServer
+ __OBJC_CLASS_PROTOCOLS_$__BMSandboxExtensionAccessAssertion
+ __OBJC_CLASS_RO_$_BMFileBackedCounter
+ __OBJC_CLASS_RO_$_BMFileBackedDictionary
+ __OBJC_CLASS_RO_$_BMXPCConnectionFactory
+ __OBJC_CLASS_RO_$__BMSandboxExtension
+ __OBJC_CLASS_RO_$__BMSandboxExtensionAccessAssertion
+ __OBJC_LABEL_PROTOCOL_$_BMConnectionProxyable
+ __OBJC_METACLASS_RO_$_BMFileBackedCounter
+ __OBJC_METACLASS_RO_$_BMFileBackedDictionary
+ __OBJC_METACLASS_RO_$_BMXPCConnectionFactory
+ __OBJC_METACLASS_RO_$__BMSandboxExtension
+ __OBJC_METACLASS_RO_$__BMSandboxExtensionAccessAssertion
+ __OBJC_PROTOCOL_$_BMConnectionProxyable
+ __OBJC_PROTOCOL_REFERENCE_$_BMConnectionProxyable
+ __PROPERTIES__BMManagedConfiguration
+ ___28-[BMProcessCurrent _session]_block_invoke
+ ___38+[BMXPCConnectionFactory defaultQueue]_block_invoke
+ ___42-[BMProcessCurrent canAccessAppleKeyStore]_block_invoke
+ ___44-[BMFileBackedCounter incrementCount:error:]_block_invoke
+ ___46-[BMXPCConnectionWrapper _initWithConnection:]_block_invoke
+ ___47-[BMXPCConnectionFactory makeConnectionWrapper]_block_invoke
+ ___49-[BMDataProtection _registerForLockStateChanges:]_block_invoke
+ ___51+[BMXPCConnectionFactory globalWeakConnectionCache]_block_invoke
+ ___51+[BMXPCConnectionFactory globalWeakConnectionCache]_block_invoke_2
+ ___53+[BMXPCConnectionFactory globalStrongConnectionCache]_block_invoke
+ ___53+[BMXPCConnectionFactory globalStrongConnectionCache]_block_invoke_2
+ ___54-[BMXPCConnectionFactory _requestConnectionFromCaller]_block_invoke
+ ___55-[BMAccessServer requestEndpointForService:user:reply:]_block_invoke
+ ___57-[BMXPCConnectionFactory _proxyConnectionThroughCoreDuet]_block_invoke
+ ___60-[BMXPCConnectionFactory _proxyConnectionThroughBiomeDaemon]_block_invoke
+ ___61+[BMAccessControlPolicy(SyncableSets) syncableSetIdentifiers]_block_invoke
+ ___77-[_BMXPCFileManager replaceFileAtPath:withFileHandle:protection:flags:error:]_block_invoke
+ ___77-[_BMXPCFileManager replaceFileAtPath:withFileHandle:protection:flags:error:]_block_invoke_2
+ ___BMBiomeLibraryIdentifierForLegacyName_block_invoke
+ ___BMNormalizedResourcesAndAccessModesListedUnderEntitlement_block_invoke
+ ___CascadeSetsLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32s_e5_v8?0l
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0l
+ ___block_descriptor_48_e8_32s40bs_e43_v24?0"NSXPCListenerEndpoint"8"NSError"16l
+ ___block_descriptor_48_e8_32s40s_e46_v32?0"BMResourceSpecifier"8"NSNumber"16^B24l
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0l
+ ___copy_helper_block_e8_32b40w
+ ___copy_helper_block_e8_32s40r48r
+ ___destroy_helper_block_e8_32s40r48r
+ ___destroy_helper_block_e8_32s40w
+ ___getCCSetConfigurationClass_block_invoke
+ ___swift_memcpy17_8
+ ___swift_reflection_version
+ __block_literal_global.10
+ __block_literal_global.100
+ __block_literal_global.105
+ __block_literal_global.11
+ __block_literal_global.113
+ __block_literal_global.116
+ __block_literal_global.224
+ __block_literal_global.254
+ __block_literal_global.257
+ __block_literal_global.331
+ __block_literal_global.339
+ __block_literal_global.9
+ __block_literal_global.96
+ __getCCSetConfigurationClass_block_invoke.cold.1
+ __getCCSetConfigurationClass_block_invoke.cold.2
+ __os_log_default
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_BiomeFoundation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_BiomeFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_BiomeFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_BiomeFoundation
+ __swift_FORCE_LOAD_$_swiftIOKit
+ __swift_FORCE_LOAD_$_swiftIOKit_$_BiomeFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_BiomeFoundation
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_BiomeFoundation
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_BiomeFoundation
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_errno_$_BiomeFoundation
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_math_$_BiomeFoundation
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_signal_$_BiomeFoundation
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_stdio_$_BiomeFoundation
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swift_time_$_BiomeFoundation
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_BiomeFoundation
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftsys_time_$_BiomeFoundation
+ __swift_FORCE_LOAD_$_swiftunistd
+ __swift_FORCE_LOAD_$_swiftunistd_$_BiomeFoundation
+ __xpc_error_connection_interrupted
+ __xpc_error_connection_invalid
+ __xpc_error_peer_code_signing_requirement
+ __xpc_error_termination_imminent
+ _audit_stringCascadeSets
+ _bm_invoke
+ _bm_openat_dprotected.cold.2
+ _objc_allocWithZone
+ _objc_copyWeak
+ _objc_initWeak
+ _objc_msgSend$URLByDeletingLastPathComponent
+ _objc_msgSend$_atomicallyCreateFileWithDictionary:error:
+ _objc_msgSend$_atomicallyWriteFileWithDictionary:error:
+ _objc_msgSend$_configureConnection:serviceType:useCase:
+ _objc_msgSend$_countFromFileDictionary:
+ _objc_msgSend$_createFileIfNotExists:
+ _objc_msgSend$_decodeFileDictionary:error:
+ _objc_msgSend$_encodeFileDictionary:error:
+ _objc_msgSend$_fileUUIDFromFileDictionary:
+ _objc_msgSend$_invalidateCacheIfPersonaSwitched
+ _objc_msgSend$_loadDictionaryOrCreate:readOnly:initialDictionary:error:
+ _objc_msgSend$_loadFileDictionary:
+ _objc_msgSend$_newFileDictionaryWithFileUUID:count:error:
+ _objc_msgSend$_proxyConnectionThroughBiomeDaemon
+ _objc_msgSend$_readableFileDictionary:
+ _objc_msgSend$_registerForLockStateChanges:
+ _objc_msgSend$_sandboxExtensionWithDescriptor:extensionToken:container:path:
+ _objc_msgSend$_session
+ _objc_msgSend$_unregister:
+ _objc_msgSend$acquireLockfile:andRunBlock:
+ _objc_msgSend$allowAppleIntelligenceReport
+ _objc_msgSend$allowedToAccessStream:withMode:error:
+ _objc_msgSend$allowsAccessToAllSetsWithMode:
+ _objc_msgSend$allowsAccessToSyncMergeableDeltas
+ _objc_msgSend$allowsConnectionToComputeSourceServiceWithDomain:
+ _objc_msgSend$bm_accessControlPolicy
+ _objc_msgSend$bm_connectionFlags
+ _objc_msgSend$bm_connectionWithPeer:queue:
+ _objc_msgSend$bm_process
+ _objc_msgSend$bm_userInfo
+ _objc_msgSend$container
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$dataWithContentsOfURL:options:error:
+ _objc_msgSend$dataWithPropertyList:format:options:error:
+ _objc_msgSend$fileURLWithPath:relativeToURL:
+ _objc_msgSend$getArgumentTypeAtIndex:
+ _objc_msgSend$getUUIDBytes:
+ _objc_msgSend$initWithDirectory:library:
+ _objc_msgSend$initWithUUIDBytes:
+ _objc_msgSend$invalidationHandler
+ _objc_msgSend$isManagedByLaunchd
+ _objc_msgSend$isPrimaryDaemon
+ _objc_msgSend$isReadOnly
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$makeConnectionWrapper
+ _objc_msgSend$mapTableWithKeyOptions:valueOptions:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$pathIsManaged:domain:
+ _objc_msgSend$propertyListWithData:options:format:error:
+ _objc_msgSend$releaseAssertion:
+ _objc_msgSend$reliesOnDirectAccessForDomain:
+ _objc_msgSend$remoteObjectInterfaceForMachServiceType:
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$replaceFileAtPath:withData:protection:flags:error:
+ _objc_msgSend$replaceFileAtPath:withFileHandle:protection:flags:error:
+ _objc_msgSend$replaceFileAtPath:withFileHandle:protection:flags:reply:
+ _objc_msgSend$requestEndpointForProxyingConnectionsWithReply:
+ _objc_msgSend$requestEndpointForService:user:reply:
+ _objc_msgSend$setBm_accessControlPolicy:
+ _objc_msgSend$setBm_connectionFlags:
+ _objc_msgSend$setConnection:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$shared
+ _objc_msgSend$syncableSetIdentifiers
+ _objc_msgSend$unownedToStrongObjectsMapTable
+ _objc_msgSend$writeUpdatedObjects:forKeys:error:
+ _open_dprotected_np
+ _os_unfair_lock_assert_owner
+ _renameatx_np
+ _session.onceToken
+ _session.session
+ _strcasestr
+ _strchr
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_lookUpClassMethod
+ _swift_once
+ _symbolic SS
+ _symbolic Sb
+ _symbolic So8NSObjectC
+ _symbolic _____ 15BiomeFoundation14ManagedSettingV
+ _symbolic _____ 15BiomeFoundation20ManagedConfigurationC
+ _xpc_connection_copy_invalidation_reason
+ _xpc_type_get_name
+ canAccessAppleKeyStore.onceToken
+ canAccessAppleKeyStore.result
+ getCCSetConfigurationClass.softClass
+ legacyViewResourceMapper.cold.1
+ setBm_accessControlPolicy:.onceToken.11
+ syncableSetIdentifiers.identifiers
+ syncableSetIdentifiers.onceToken
- +[BMAccessConnectionFactory _configureConnection:interface:useCase:]
- +[BMAccessConnectionFactory connectionToAccessServerInDomain:user:useCase:]
- +[BMAccessConnectionFactory connectionToFileServerInDomain:user:useCase:]
- +[BMAccessConnectionFactory defaultQueue]
- +[BMAccessConnectionFactory delegate]
- +[BMAccessConnectionFactory globalStrongConnectionCache]
- +[BMAccessConnectionFactory globalWeakConnectionCache]
- +[BMAccessConnectionFactory setDelegate:]
- +[BMPaths(Sets) legacySetsRootDirectoryURL]
- +[BMPaths(Sets) legacySetsRootDirectoryURL].cold.1
- +[NSXPCConnection bm_connectionWithPeer:queue:]
- -[BMAccessAssertionCache _invalidateCacheIfPersonaSwitched:]
- -[BMAccessAssertionCache _makeAssertionWithDescriptor:extensionToken:container:path:]
- -[BMAccessConnectionFactory .cxx_destruct]
- -[BMAccessConnectionFactory _configureConnection:]
- -[BMAccessConnectionFactory _connectionFlags]
- -[BMAccessConnectionFactory _legacyUserDomainConnection]
- -[BMAccessConnectionFactory _newConnection]
- -[BMAccessConnectionFactory _proxyConnectionThroughCoreDuet]
- -[BMAccessConnectionFactory _proxyConnectionToBiomeAgentThroughBiomeDaemon]
- -[BMAccessConnectionFactory _regularConnection]
- -[BMAccessConnectionFactory _requestConnectionFromCaller]
- -[BMAccessConnectionFactory _requestConnectionFromCaller].cold.1
- -[BMAccessConnectionFactory _targetUserConnection]
- -[BMAccessConnectionFactory connectionIsCrossUser]
- -[BMAccessConnectionFactory coreDuetMachService]
- -[BMAccessConnectionFactory coreDuetMachService].cold.1
- -[BMAccessConnectionFactory coreDuetMachService].cold.2
- -[BMAccessConnectionFactory currentProcessCanDirectlyConnectCrossUser]
- -[BMAccessConnectionFactory delegate]
- -[BMAccessConnectionFactory initWithType:domain:user:useCase:]
- -[BMAccessConnectionFactory machServiceName]
- -[BMAccessConnectionFactory makeConnection]
- -[BMAccessConnectionFactory remoteObjectInterface]
- -[BMAccessConnectionFactory setDelegate:]
- -[BMAccessConnectionFactory user]
- -[BMAccessControlPolicy allowsAccessToSetsWithMode:]
- -[BMAccessControlPolicy allowsConnectionToAccessServiceWithDomain:].cold.3
- -[BMAccessControlPolicy allowsConnectionToComputeSourceService]
- -[BMAccessServer endpointForBiomeAgentOfUser:error:]
- -[BMAccessServer requestBiomeEndpointForUser:reply:]
- -[BMAccessServiceListener endpointForSystemToUserConnections]
- -[BMDataProtection registerForLockStateChanges:]
- -[BMDataProtection unregister:]
- -[BMFileManager replaceFileAtPath:withData:protection:error:]
- -[BMFileManager replaceFileAtPath:withFileHandle:protection:error:]
- -[BMFileServer entitledToAccessStream:withMode:error:]
- -[BMFileServer replaceFileAtPath:withFileHandle:protection:reply:]
- -[BMFileServer replaceFileAtPath:withFileHandle:protection:reply:].cold.1
- -[BMFileServer replaceFileAtPath:withFileHandle:protection:reply:].cold.2
- -[BMFileServer replaceFileAtPath:withFileHandle:protection:reply:].cold.3
- -[BMFileServer replaceFileAtPath:withFileHandle:protection:reply:].cold.4
- -[NSXPCConnection bm_accessControlPolicy]
- -[NSXPCConnection bm_connectionFlags]
- -[NSXPCConnection bm_process]
- -[NSXPCConnection bm_userInfo]
- -[NSXPCConnection setBm_accessControlPolicy:]
- -[NSXPCConnection setBm_connectionFlags:]
- -[_BMAccessAssertion .cxx_destruct]
- -[_BMAccessAssertion container]
- -[_BMAccessAssertion dealloc]
- -[_BMAccessAssertion dealloc].cold.1
- -[_BMAccessAssertion dealloc].cold.2
- -[_BMAccessAssertion descriptor]
- -[_BMAccessAssertion initWithDescriptor:extensionToken:container:path:]
- -[_BMAccessAssertion initWithDescriptor:extensionToken:container:path:].cold.1
- -[_BMAccessAssertion initWithDescriptor:extensionToken:container:path:].cold.2
- -[_BMAccessAssertion path]
- -[_BMDirectFileManager replaceFileAtPath:withData:protection:error:]
- -[_BMDirectFileManager replaceFileAtPath:withData:protection:error:].cold.1
- -[_BMDirectFileManager replaceFileAtPath:withData:protection:error:].cold.2
- -[_BMDirectFileManager replaceFileAtPath:withData:protection:error:].cold.3
- -[_BMDirectFileManager replaceFileAtPath:withData:protection:error:].cold.4
- -[_BMDirectFileManager replaceFileAtPath:withData:protection:error:].cold.5
- -[_BMDirectFileManager replaceFileAtPath:withFileHandle:protection:error:]
- -[_BMDirectFileManager replaceFileAtPath:withFileHandle:protection:error:].cold.1
- -[_BMDirectFileManager replaceFileAtPath:withFileHandle:protection:error:].cold.2
- -[_BMDirectFileManager replaceFileAtPath:withFileHandle:protection:error:].cold.3
- -[_BMDirectFileManager replaceFileAtPath:withFileHandle:protection:error:].cold.4
- -[_BMDirectFileManager replaceFileAtPath:withFileHandle:protection:error:].cold.5
- -[_BMXPCFileManager replaceFileAtPath:withData:protection:error:]
- -[_BMXPCFileManager replaceFileAtPath:withData:protection:error:].cold.1
- -[_BMXPCFileManager replaceFileAtPath:withFileHandle:protection:error:]
- -[_BMXPCFileManager replaceFileAtPath:withFileHandle:protection:error:].cold.1
- GCC_except_table18
- GCC_except_table25
- GCC_except_table31
- GCC_except_table41
- GCC_except_table44
- GCC_except_table50
- GCC_except_table64
- OBJC_IVAR_$_BMAccessConnectionFactory._delegate
- OBJC_IVAR_$_BMAccessConnectionFactory._domain
- OBJC_IVAR_$_BMAccessConnectionFactory._path
- OBJC_IVAR_$_BMAccessConnectionFactory._serviceType
- OBJC_IVAR_$_BMAccessConnectionFactory._useCase
- OBJC_IVAR_$_BMAccessConnectionFactory._user
- OBJC_IVAR_$_BMAccessServiceListener._systemToUserListener
- OBJC_IVAR_$__BMAccessAssertion._container
- OBJC_IVAR_$__BMAccessAssertion._descriptor
- OBJC_IVAR_$__BMAccessAssertion._handle
- OBJC_IVAR_$__BMAccessAssertion._path
- _BMExpandBiomeLibraryPremigrationIdentifiersAccessModeDictionary
- _BMExpandBiomeStreamsPremigrationIdentifiersAccessModeDictionary
- _OBJC_CLASS_$_BMAccessConnectionFactory
- _OBJC_CLASS_$__BMAccessAssertion
- _OBJC_METACLASS_$_BMAccessConnectionFactory
- _OBJC_METACLASS_$__BMAccessAssertion
- __43-[BMAccessConnectionFactory makeConnection]_block_invoke.12
- __50-[BMAccessClient(Deletions) removeResource:error:]_block_invoke.126
- __52-[BMAccessServer endpointForBiomeAgentOfUser:error:]_block_invoke.76
- __53-[BMAccessClient requestAccessToResource:mode:error:]_block_invoke.96
- __57-[BMAccessConnectionFactory _requestConnectionFromCaller]_block_invoke.94
- __57-[BMAccessConnectionFactory _requestConnectionFromCaller]_block_invoke.94.cold.1
- __57-[BMAccessConnectionFactory _requestConnectionFromCaller]_block_invoke.cold.1
- __60-[BMAccessConnectionFactory _proxyConnectionThroughCoreDuet]_block_invoke.90
- __60-[BMAccessConnectionFactory _proxyConnectionThroughCoreDuet]_block_invoke.90.cold.1
- __60-[BMAccessConnectionFactory _proxyConnectionThroughCoreDuet]_block_invoke.cold.1
- __65-[NSXPCConnection(BiomeAccessControl) setBm_accessControlPolicy:]_block_invoke.9
- __69-[BMAccessClient(ConnectionProxying) requestEndpointForDomain:error:]_block_invoke.121
- __69-[_BMXPCFileManager _fileHandleForFileAtPath:flags:protection:error:]_block_invoke.27
- __75-[BMAccessConnectionFactory _proxyConnectionToBiomeAgentThroughBiomeDaemon]_block_invoke.107
- __75-[BMAccessConnectionFactory _proxyConnectionToBiomeAgentThroughBiomeDaemon]_block_invoke.107.cold.1
- __75-[BMAccessConnectionFactory _proxyConnectionToBiomeAgentThroughBiomeDaemon]_block_invoke.cold.1
- __BMResourcesAndAccessModesListedUnderEntitlement_block_invoke.270
- __BMResourcesAndAccessModesListedUnderEntitlement_block_invoke.277
- __BMResourcesAndAccessModesListedUnderEntitlement_block_invoke.282
- __OBJC_$_CATEGORY_NSXPCConnection_$_BMXPCListener
- __OBJC_$_CLASS_METHODS_BMAccessConnectionFactory
- __OBJC_$_CLASS_METHODS_BMAccessControlPolicy(LegacyViewEntitlement|SetStoreUpdateService|WriteService|DaemonToAgent|UseCase)
- __OBJC_$_CLASS_METHODS_NSXPCConnection(BMXPCListener|BiomeUseCaseSupport)
- __OBJC_$_CLASS_PROP_LIST_BMAccessConnectionFactory
- __OBJC_$_INSTANCE_METHODS_BMAccessConnectionFactory
- __OBJC_$_INSTANCE_METHODS_BMAccessControlPolicy(LegacyViewEntitlement|SetStoreUpdateService|WriteService|DaemonToAgent|UseCase)
- __OBJC_$_INSTANCE_METHODS_NSXPCConnection(BMXPCListener|BiomeUseCaseSupport)
- __OBJC_$_INSTANCE_METHODS__BMAccessAssertion
- __OBJC_$_INSTANCE_VARIABLES_BMAccessConnectionFactory
- __OBJC_$_INSTANCE_VARIABLES__BMAccessAssertion
- __OBJC_$_PROP_LIST_BMAccessConnectionFactory
- __OBJC_$_PROP_LIST__BMAccessAssertion
- __OBJC_CLASS_PROTOCOLS_$__BMAccessAssertion
- __OBJC_CLASS_RO_$_BMAccessConnectionFactory
- __OBJC_CLASS_RO_$__BMAccessAssertion
- __OBJC_METACLASS_RO_$_BMAccessConnectionFactory
- __OBJC_METACLASS_RO_$__BMAccessAssertion
- ___35+[BMPaths _biomeUserDataDirectory:]_block_invoke
- ___41+[BMAccessConnectionFactory defaultQueue]_block_invoke
- ___42-[BMProcessCurrent isRunningInUserContext]_block_invoke
- ___43-[BMAccessConnectionFactory makeConnection]_block_invoke
- ___48-[BMDataProtection registerForLockStateChanges:]_block_invoke
- ___52-[BMAccessServer endpointForBiomeAgentOfUser:error:]_block_invoke
- ___54+[BMAccessConnectionFactory globalWeakConnectionCache]_block_invoke
- ___54+[BMAccessConnectionFactory globalWeakConnectionCache]_block_invoke_2
- ___55-[BMAccessAssertionCache assertionForAccessDescriptor:]_block_invoke
- ___56+[BMAccessConnectionFactory globalStrongConnectionCache]_block_invoke
- ___56+[BMAccessConnectionFactory globalStrongConnectionCache]_block_invoke_2
- ___57-[BMAccessConnectionFactory _requestConnectionFromCaller]_block_invoke
- ___60-[BMAccessConnectionFactory _proxyConnectionThroughCoreDuet]_block_invoke
- ___71-[_BMXPCFileManager replaceFileAtPath:withFileHandle:protection:error:]_block_invoke
- ___71-[_BMXPCFileManager replaceFileAtPath:withFileHandle:protection:error:]_block_invoke_2
- ___75-[BMAccessConnectionFactory _proxyConnectionToBiomeAgentThroughBiomeDaemon]_block_invoke
- ___91-[BMAccessAssertionCache createAssertionForAccessDescriptor:extensionToken:container:path:]_block_invoke
- ___block_descriptor_56_e8_32s40s48r_e20_v16?0"NSMapTable"8l
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e20_v16?0"NSMapTable"8l
- ___copy_helper_block_e8_32s40s48s56s64s72r
- ___destroy_helper_block_e8_32s40s48s56s64s72r
- __block_literal_global.106
- __block_literal_global.109
- __block_literal_global.216
- __block_literal_global.245
- __block_literal_global.291
- __block_literal_global.4
- __block_literal_global.7
- __block_literal_global.89
- __block_literal_global.93
- __block_literal_global.95
- _biomeUserDataDirectory:.onceToken
- _objc_msgSend$_configureConnection:interface:useCase:
- _objc_msgSend$_currentProcessIsSandboxed
- _objc_msgSend$_invalidateCacheIfPersonaSwitched:
- _objc_msgSend$_makeAssertionWithDescriptor:extensionToken:container:path:
- _objc_msgSend$_proxyConnectionToBiomeAgentThroughBiomeDaemon
- _objc_msgSend$allowsAccessToSetsWithMode:
- _objc_msgSend$allowsConnectionToComputeSourceService
- _objc_msgSend$endpointForBiomeAgentOfUser:error:
- _objc_msgSend$endpointForSystemToUserConnections
- _objc_msgSend$entitledToAccessStream:withMode:error:
- _objc_msgSend$makeConnection
- _objc_msgSend$registerForLockStateChanges:
- _objc_msgSend$remoteObjectInterface
- _objc_msgSend$replaceFileAtPath:withFileHandle:protection:error:
- _objc_msgSend$replaceFileAtPath:withFileHandle:protection:reply:
- _objc_msgSend$requestBiomeEndpointForUser:reply:
- _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
- _objc_msgSend$unregister:
- isRunningInUserContext.onceToken
- isRunningInUserContext.userContext
- setBm_accessControlPolicy:.onceToken.8
CStrings:
+ " fileBackedDictionary: %@"
+ "%@"
+ "'%@' is not present in allow-list for '%@'"
+ "-lock"
+ "-replaceFileAtPath:withFileHandle:protection:flags:reply: called with invalid path: %{private}@"
+ "-replaceFileAtPath:withFileHandle:protection:flags:reply: called with subpath: %{public}@"
+ "/System/Library/PrivateFrameworks/CascadeSets.framework/Contents/MacOS/CascadeSets"
+ "<unknown>"
+ "@\"<BMXPCConnectionFactoryDelegate>\""
+ "@\"<_BMRootLibrary>\""
+ "@\"BMFileHandle\"48@0:8@\"NSString\"16@\"BMFileHandle\"24i32i36^@40"
+ "@\"NSUUID\""
+ "@20@0:8C16"
+ "@48@0:8@16@24i32i36^@40"
+ "@52@0:8@16i24@28Q36^@44"
+ "@60@0:8@16i24@28B36B40@44^@52"
+ "AppleKeyStoreUserClient"
+ "B32@0:8^@16^@24"
+ "B40@0:8B16B20@24^@32"
+ "B48@0:8@16@24i32i36^@40"
+ "BMComputeSourceServer"
+ "BMConnectionProxyable"
+ "BMFileBackedCounter"
+ "BMFileBackedDictionary"
+ "BMFileServer.m"
+ "BMServiceDomain(%ld)"
+ "BMXPCConnectionFactory"
+ "BMXPCConnectionFactory.m"
+ "CCSetConfiguration"
+ "Class getCCSetConfigurationClass(void)_block_invoke"
+ "Client '%@' not present in allow-list for '%{public}@'"
+ "Connection to '%{public}s' encountered unknown error type %@"
+ "Connection to '%{public}s' failed peer code signing requirement"
+ "Connection to '%{public}s' interrupted"
+ "Connection to '%{public}s' invalidated: %{public}s"
+ "Connection to '%{public}s' termination imminent"
+ "Couldn't find protocol BMComputeSourceServer"
+ "Counter file replaced at path: %@ contents: %@"
+ "Creating new counter file at path: %@ contents: %@"
+ "Entitlement lists stream named '%{public}@' however no such stream was found"
+ "Expected mutable plist class (%@) but received class (%@) for object: %@ at path: %@"
+ "Failed to atomically replace counter file at path: %@"
+ "Failed to atomically replace counter file at path: %@ with error %@"
+ "Failed to construct dictionary: %@ for new counter file at path: %@"
+ "Failed to decode prior file-backed counter at path: %@ with data: %@"
+ "Failed to encode dictionary: %@ for counter file at path: %@ error: %@"
+ "Failed to open prior file-backed counter at path: %@ error: %@"
+ "Failed to read back counter file after atomic replace failed at path: %@"
+ "Failed to read prior file-backed dictionary at path: %@ error: %@"
+ "Failed to remove file-backed dictionary at path: %@"
+ "Failed to write data to handle with error %@"
+ "Failed to write removal for key: %@ reverting to prior object: %@"
+ "Failed to write updated object(s): %@ for key(s): %@ reverting to prior object(s): %@"
+ "Found prior counter file at path: %@ contents: %@"
+ "Increment failed: %@"
+ "Initializing file-backed dictionary at path: %@ with dictionary: %@"
+ "Invalid count (%@) on init for file at path: %@ from dictionary: %@"
+ "Invalid destination user"
+ "Invalid fileUUID (%@) on init for file at path: %@ from dictionary: %@"
+ "Invalid item URL: %@"
+ "Invalid key: %@"
+ "Invalid path: \"%@\""
+ "Invalid source user"
+ "Invalid {filename: %@, directory: %@}"
+ "Invalid {object: %@ key: %@}"
+ "LoginWindow"
+ "New connection to %{public}@ %{public}@"
+ "No object exists for key: %@"
+ "No prior file-backed dictionary found at path: %@"
+ "Parent directory: %@ does not exist (isDirectory: %i)"
+ "Removed object: %@ for key: %@"
+ "Sandbox"
+ "Successfully read back counter file at path: %@ contents: %@"
+ "SyncableSets"
+ "T@\"<BMXPCConnectionFactoryDelegate>\",W"
+ "T@\"<BMXPCConnectionFactoryDelegate>\",W,V_delegate"
+ "T@\"BMAccessControlPolicy\",&,N"
+ "T@\"BMProcess\",R,N"
+ "T@\"NSObject<OS_xpc_object>\",W,V_connection"
+ "T@\"NSUUID\",R,N,V_fileUUID"
+ "T@\"_BMManagedConfiguration\",N,R"
+ "TB,N,R"
+ "TQ,N"
+ "URLByDeletingLastPathComponent"
+ "Unable to locate reply block for -%{public}@, got class %{public}@"
+ "Unable to locate reply block for -%{public}@, got type %{public}s"
+ "Unexpected count: %@ (expected %@) file path: %@"
+ "Unexpected fileUUID: %@ (expected %@) file path: %@"
+ "Unexpected number of objects: %@ for keys: %@"
+ "Unexpected object: %@ for key: %@ expected: %@"
+ "Unexpected plist class (%@) of object: %@ at path: %@"
+ "Unsupported or invalid service name"
+ "Updated object(s): %@ for key(s): %@ replacing prior object(s): %@"
+ "_BMManagedConfiguration"
+ "_BMSandboxExtension"
+ "_BMSandboxExtensionAccessAssertion"
+ "_BMXPCTransport unhandled type: %s"
+ "__maintenance__"
+ "_allowAppleIntelligenceReport"
+ "_assertionsMap"
+ "_atomicallyCreateFileWithDictionary:error:"
+ "_atomicallyWriteFileWithDictionary:error:"
+ "_configureConnection:serviceType:useCase:"
+ "_countFromFileDictionary:"
+ "_createFileIfNotExists:"
+ "_decodeFileDictionary:error:"
+ "_dictionary"
+ "_encodeFileDictionary:error:"
+ "_extensionCache"
+ "_filePath"
+ "_fileURL"
+ "_fileUUID"
+ "_fileUUIDFromFileDictionary:"
+ "_invalidateCacheIfPersonaSwitched"
+ "_lastObservedCount"
+ "_library"
+ "_loadDictionaryOrCreate:readOnly:initialDictionary:error:"
+ "_loadFileDictionary:"
+ "_lockFilePath"
+ "_newFileDictionaryWithFileUUID:count:error:"
+ "_proxyConnectionThroughBiomeDaemon"
+ "_readableFileDictionary:"
+ "_registerForLockStateChanges:"
+ "_sandboxExtensionWithDescriptor:extensionToken:container:path:"
+ "_session"
+ "_unregister:"
+ "access server"
+ "allSetsResourceSpecifierWithOptions:"
+ "allowAppleIntelligenceReport"
+ "allowedToAccessStream:withMode:error:"
+ "allowsAccessToAllSetsWithMode:"
+ "allowsAccessToSyncMergeableDeltas"
+ "allowsConnectionToComputeSourceServiceWithDomain:"
+ "bm_connectionWithPeer:queue:"
+ "bm_userInfo"
+ "canAccessAppleKeyStore"
+ "clear:"
+ "clearObjectForKey:error:"
+ "com.apple.BiomeFoundation"
+ "com.apple.BiomeFoundation.FileBackedCounter"
+ "com.apple.BiomeFoundation.FileBackedDictionary"
+ "com.apple.BiomeFoundation.PersonaUtilities"
+ "com.apple.applicationaccess"
+ "com.apple.biome.compute.publisher.service"
+ "com.apple.biome.compute.publisher.service.user"
+ "com.apple.biome.compute.source"
+ "com.apple.biome.compute.source.user"
+ "com.apple.bluetoothd"
+ "com.apple.modelcatalogd"
+ "compute source server"
+ "configuration.allowedClients"
+ "connectionToComputeSourceServerInDomain:user:useCase:"
+ "connectionToMachService:endpoint:useCase:"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "current counter file UUID (%@) does not match expected (%@) at path: %@"
+ "current counter file count (%@) is less than last observed (%@) at path: %@"
+ "dataWithBytes:length:"
+ "dataWithContentsOfURL:options:error:"
+ "dataWithPropertyList:format:options:error:"
+ "file server"
+ "fileURLWithPath:relativeToURL:"
+ "fileUUID"
+ "getArgumentTypeAtIndex:"
+ "getUUIDBytes:"
+ "incrementCount:error:"
+ "initWithDirectory:library:"
+ "initWithFilename:protectionClass:directory:domain:error:"
+ "initWithFilename:protectionClass:directory:readOnly:create:initialDictionary:error:"
+ "initWithUUIDBytes:"
+ "instance: %@ is read only."
+ "invalidationHandler"
+ "iokit-open-user-client"
+ "isPrimaryDaemon"
+ "isReadOnly"
+ "lowercaseString"
+ "makeConnectionWrapper"
+ "mapTableWithKeyOptions:valueOptions:"
+ "mutableDictionaryForKey:error:"
+ "numberWithUnsignedLongLong:"
+ "object: %@ is already recorded for key: %@"
+ "propertyListWithData:options:format:error:"
+ "releaseAssertion:"
+ "remoteObjectInterfaceForMachServiceType:"
+ "remoteObjectProxyWithErrorHandler:"
+ "removeItemAtURL:error:"
+ "replaceFileAtPath:withData:protection:flags:error:"
+ "replaceFileAtPath:withFileHandle:protection:flags:error:"
+ "replaceFileAtPath:withFileHandle:protection:flags:reply:"
+ "requestEndpointForProxyingConnectionsWithReply:"
+ "requestEndpointForService:user:reply:"
+ "resourceGeneration"
+ "setBasePathForTestingWithPath: only supported for internal installs"
+ "setBm_accessControlPolicy:"
+ "setBm_connectionFlags:"
+ "setConnection:"
+ "setInvalidationHandler:"
+ "shared"
+ "softlink:r:path:/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets"
+ "syncableSetConfigurations.setIdentifier"
+ "syncableSetIdentifiers"
+ "unownedToStrongObjectsMapTable"
+ "v24@0:8@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">16"
+ "v36@0:8@\"NSString\"16I24@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">28"
+ "v36@0:8@16I24@?28"
+ "v40@0:8@16Q24@32"
+ "v48@0:8@\"NSString\"16@\"BMFileHandle\"24i32i36@?<v@?@\"BMFileHandle\"@\"NSError\">40"
+ "v48@0:8@16@24i32i36@?40"
+ "void *CascadeSetsLibrary(void)"
+ "writeUpdatedObject:forKey:error:"
+ "writeUpdatedObjects:forKeys:error:"
+ "xpc_fd_create failed: %s"
+ "{ %@: %@, %@: %@}"
- "-replaceFileAtPath:withFileHandle:protection:reply: called with invalid path: %{private}@"
- "-replaceFileAtPath:withFileHandle:protection:reply: called with subpath: %{public}@"
- "@\"<BMAccessConnectionFactoryDelegate>\""
- "@\"BMFileHandle\"44@0:8@\"NSString\"16@\"BMFileHandle\"24i32^@36"
- "@28@0:8I16^@20"
- "@44@0:8@16@24i32^@36"
- "B44@0:8@16@24i32^@36"
- "BMAccessConnectionFactory"
- "BMAccessConnectionFactory.m"
- "Count"
- "Cross-user not allowed"
- "Failed to resolve container for legacySetsRootDirectoryURL: %@"
- "Refusing connection from %{public}@(%d), wrong user"
- "Root/system processes are unable to access Biome user data directory."
- "T@\"<BMAccessConnectionFactoryDelegate>\",W"
- "T@\"<BMAccessConnectionFactoryDelegate>\",W,V_delegate"
- "Unable to locate reply block for -%@"
- "_BMAccessAssertion"
- "_configureConnection:interface:useCase:"
- "_invalidateCacheIfPersonaSwitched:"
- "_makeAssertionWithDescriptor:extensionToken:container:path:"
- "_proxyConnectionToBiomeAgentThroughBiomeDaemon"
- "_systemToUserListener"
- "allowsAccessToSetsWithMode:"
- "allowsConnectionToComputeSourceService"
- "biomed"
- "endpointForBiomeAgentOfUser:error:"
- "endpointForSystemToUserConnections"
- "entitledToAccessStream:withMode:error:"
- "legacySetsRootDirectoryURL"
- "makeConnection"
- "remoteObjectInterface"
- "replaceFileAtPath:withData:protection:error:"
- "replaceFileAtPath:withFileHandle:protection:error:"
- "replaceFileAtPath:withFileHandle:protection:reply:"
- "requestBiomeEndpointForUser:reply:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "v16@?0@\"NSMapTable\"8"
- "v28@0:8I16@?20"
- "v28@0:8I16@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">20"
- "v40@0:8@16@24@32"
- "v44@0:8@\"NSString\"16@\"BMFileHandle\"24i32@?<v@?@\"BMFileHandle\"@\"NSError\">36"
- "v44@0:8@16@24i32@?36"

```
