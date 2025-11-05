## Seeding

> `/System/Library/PrivateFrameworks/Seeding.framework/Versions/A/Seeding`

```diff

-107.0.0.0.0
-  __TEXT.__text: 0x23110
-  __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_methlist: 0x157c
-  __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0x684
-  __TEXT.__cstring: 0x1fc5
-  __TEXT.__oslogstring: 0x2f8a
-  __TEXT.__unwind_info: 0x8c0
-  __TEXT.__objc_classname: 0x256
-  __TEXT.__objc_methname: 0x3dc3
-  __TEXT.__objc_methtype: 0x811
-  __TEXT.__objc_stubs: 0x3be0
-  __DATA_CONST.__got: 0x2a0
-  __DATA_CONST.__const: 0x258
-  __DATA_CONST.__objc_classlist: 0xc8
+113.0.0.0.0
+  __TEXT.__text: 0x24d48
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__objc_methlist: 0x18bc
+  __TEXT.__const: 0x120
+  __TEXT.__gcc_except_tab: 0x6d0
+  __TEXT.__cstring: 0x2440
+  __TEXT.__oslogstring: 0x334a
+  __TEXT.__unwind_info: 0x930
+  __TEXT.__objc_classname: 0x280
+  __TEXT.__objc_methname: 0x3e61
+  __TEXT.__objc_methtype: 0x840
+  __TEXT.__objc_stubs: 0x3d20
+  __DATA_CONST.__got: 0x2a8
+  __DATA_CONST.__const: 0x270
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1080
+  __DATA_CONST.__objc_selrefs: 0x1160
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x2d8
-  __AUTH_CONST.__const: 0x1000
-  __AUTH_CONST.__cfstring: 0x1960
-  __AUTH_CONST.__objc_const: 0x3bd0
+  __AUTH_CONST.__auth_got: 0x2e0
+  __AUTH_CONST.__const: 0xff0
+  __AUTH_CONST.__cfstring: 0x19e0
+  __AUTH_CONST.__objc_const: 0x3618
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0xc4
+  __AUTH.__objc_data: 0x500
+  __DATA.__objc_ivar: 0xc8
   __DATA.__data: 0x300
-  __DATA.__bss: 0x178
+  __DATA.__bss: 0x188
   __DATA_DIRTY.__objc_data: 0x280
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D9AF74E2-58E8-3462-9083-A93F8EFB282C
-  Functions: 755
-  Symbols:   1962
-  CStrings:  1575
+  UUID: 5D2CED08-3954-39B6-A015-38812B62F2EC
+  Functions: 796
+  Symbols:   2017
+  CStrings:  1623
 
Symbols:
+ +[SDAnalytics deviceIdentifier].cold.1
+ +[SDBetaEnrollmentDaemon sharedInstance]
+ +[SDBetaEnrollmentDaemon sharedInstance].cold.1
+ +[SDBetaEnrollmentDaemonProxy sharedInstance]
+ +[SDBetaEnrollmentDaemonProxy sharedInstance].cold.1
+ +[SDBetaEnrollmentService sharedInstance]
+ +[SDBetaEnrollmentService sharedInstance].cold.1
+ +[SDBetaEnrollmentServiceProxy sharedInstance]
+ +[SDBetaEnrollmentServiceProxy sharedInstance].cold.1
+ +[SDBetaManager sharedManager].cold.1
+ +[SDBetaProgram isPad].cold.1
+ +[SDHTTPClient sharedInstance].cold.1
+ +[SDMDMConfiguratorImplementation applyMDMConfiguration:]
+ +[SDMDMConfiguratorImplementation conditionallyUnenrollIfNotMatchingOfferedTokensWithConfig:userIdentifier:]
+ +[SDMDMConfiguratorImplementation configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:userIdentifier:completion:]
+ +[SDMDMConfiguratorImplementation configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:userIdentifier:completion:].cold.1
+ +[SDMDMConfiguratorImplementation enrollWithRequireProgramToken:userIdentifier:]
+ +[SDMDMConfiguratorImplementation enrollWithRequireProgramToken:userIdentifier:].cold.1
+ +[SDMDMConfiguratorImplementation isBetaEnrollmentDisabled]
+ +[SDMDMConfiguratorImplementation isBetaEnrollmentDisabled].cold.1
+ +[SDMDMConfiguratorImplementation shouldReturnBecauseOfInvalidTokens:andReportErrorWith:]
+ +[SDPersistence loadMDMConfigurationWithError:].cold.4
+ +[SDSeedingLogging analyticsHandle].cold.1
+ +[SDSeedingLogging betaHandle].cold.1
+ +[SDSeedingLogging fwHandle].cold.1
+ +[SDSeedingLogging httpHandle].cold.1
+ +[SDSeedingLogging mdmHandle].cold.1
+ +[SDSeedingLogging migrateHandle].cold.1
+ +[SDSeedingLogging profileHandle].cold.1
+ -[SDBetaEnrollmentDaemon .cxx_destruct]
+ -[SDBetaEnrollmentDaemon addFBAHelpMenu:]
+ -[SDBetaEnrollmentDaemon addFBASymlink:]
+ -[SDBetaEnrollmentDaemon configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:completion:]
+ -[SDBetaEnrollmentDaemon connection]
+ -[SDBetaEnrollmentDaemon fetchBetaEnrollmentTokens:]
+ -[SDBetaEnrollmentDaemon isPreReleaseInstallationAllowed:]
+ -[SDBetaEnrollmentDaemon listener:shouldAcceptNewConnection:]
+ -[SDBetaEnrollmentDaemon listener:shouldAcceptNewConnection:].cold.1
+ -[SDBetaEnrollmentDaemon loadMDMConfigurationWithCompletion:]
+ -[SDBetaEnrollmentDaemon removeBetaEnrollmentData:]
+ -[SDBetaEnrollmentDaemon removeFBAHelpMenu:]
+ -[SDBetaEnrollmentDaemon removeSeedEnrollmentCookie:]
+ -[SDBetaEnrollmentDaemon saveMDMConfiguration:withCompletion:]
+ -[SDBetaEnrollmentDaemon setConnection:]
+ -[SDBetaEnrollmentDaemon setupAssistant_enrollInProgramWithBetaEnrollmentToken:completion:]
+ -[SDBetaEnrollmentDaemon start]
+ -[SDBetaEnrollmentDaemonProxy .cxx_destruct]
+ -[SDBetaEnrollmentDaemonProxy addFBAHelpMenu:]
+ -[SDBetaEnrollmentDaemonProxy addFBASymlink:]
+ -[SDBetaEnrollmentDaemonProxy configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:error:]
+ -[SDBetaEnrollmentDaemonProxy connectToDaemon]
+ -[SDBetaEnrollmentDaemonProxy daemonConnection]
+ -[SDBetaEnrollmentDaemonProxy fetchBetaEnrollmentTokensWithError:]
+ -[SDBetaEnrollmentDaemonProxy init]
+ -[SDBetaEnrollmentDaemonProxy isPreReleaseInstallationAllowed]
+ -[SDBetaEnrollmentDaemonProxy loadMDMConfigurationWithError:]
+ -[SDBetaEnrollmentDaemonProxy remoteObjectProxyWithCompletion:]
+ -[SDBetaEnrollmentDaemonProxy remoteObjectProxy]
+ -[SDBetaEnrollmentDaemonProxy removeBetaEnrollmentData]
+ -[SDBetaEnrollmentDaemonProxy removeFBAHelpMenu:]
+ -[SDBetaEnrollmentDaemonProxy removeSeedEnrollmentCookie:]
+ -[SDBetaEnrollmentDaemonProxy saveMDMConfiguration:withError:]
+ -[SDBetaEnrollmentDaemonProxy setDaemonConnection:]
+ -[SDBetaEnrollmentDaemonProxy setupAssistant_enrollInProgramWithBetaEnrollmentToken:completion:]
+ -[SDBetaEnrollmentDaemonProxy synchronousDaemonRemoteObjectProxyWithError:]
+ -[SDBetaEnrollmentDaemonProxy synchronousRemoteObjectProxy]
+ -[SDBetaEnrollmentService .cxx_destruct]
+ -[SDBetaEnrollmentService _connectionForPid:]
+ -[SDBetaEnrollmentService _releaseAppConnectionWithPid:]
+ -[SDBetaEnrollmentService _startListeningForProfileChanges]
+ -[SDBetaEnrollmentService _stopListeningForProfileChanges]
+ -[SDBetaEnrollmentService _storeAppConnection:]
+ -[SDBetaEnrollmentService _storeAppConnection:].cold.1
+ -[SDBetaEnrollmentService _verifyCurrentDevice]
+ -[SDBetaEnrollmentService appConnections]
+ -[SDBetaEnrollmentService canDeviceEnrollInBetaUpdates:completion:]
+ -[SDBetaEnrollmentService canFileFeedbackOnDevice:completion:]
+ -[SDBetaEnrollmentService checkIn]
+ -[SDBetaEnrollmentService configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:completion:]
+ -[SDBetaEnrollmentService configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:completion:].cold.1
+ -[SDBetaEnrollmentService dealloc]
+ -[SDBetaEnrollmentService deleteSeedingAppleAccountForDevice:completion:]
+ -[SDBetaEnrollmentService enrollDevice:inProgram:completion:]
+ -[SDBetaEnrollmentService enrollInProgramWithToken:completion:]
+ -[SDBetaEnrollmentService enrolledBetaProgramForDevice:completion:]
+ -[SDBetaEnrollmentService getCurrentDevice:]
+ -[SDBetaEnrollmentService getCurrentPrimaryAppleIDForDevice:completion:]
+ -[SDBetaEnrollmentService getCurrentSeedingAppleIDForDevice:completion:]
+ -[SDBetaEnrollmentService getDevicesForPlatforms:completion:]
+ -[SDBetaEnrollmentService invalidateDaemonCacheWithCompletion:]
+ -[SDBetaEnrollmentService isDeviceEnrolledInBetaProgram:completion:]
+ -[SDBetaEnrollmentService isDeviceUsingSeedingAppleID:completion:]
+ -[SDBetaEnrollmentService listener:shouldAcceptNewConnection:]
+ -[SDBetaEnrollmentService listener:shouldAcceptNewConnection:].cold.1
+ -[SDBetaEnrollmentService listener]
+ -[SDBetaEnrollmentService loadMDMConfigurationWithCompletion:]
+ -[SDBetaEnrollmentService loadMDMConfigurationWithCompletion:].cold.1
+ -[SDBetaEnrollmentService profileToken]
+ -[SDBetaEnrollmentService queryProgramsForSystemAccountsWithPlatforms:completion:]
+ -[SDBetaEnrollmentService remoteObjectProxyForPID:]
+ -[SDBetaEnrollmentService setAppConnections:]
+ -[SDBetaEnrollmentService setAppleAccountIdentifierFromAlternateDSID:forDevice:completion:]
+ -[SDBetaEnrollmentService setListener:]
+ -[SDBetaEnrollmentService setProfileToken:]
+ -[SDBetaEnrollmentService setUserIdentifier:]
+ -[SDBetaEnrollmentService start]
+ -[SDBetaEnrollmentService unenrollDevice:completion:]
+ -[SDBetaEnrollmentService userIdentifier]
+ -[SDBetaEnrollmentServiceProxy .cxx_destruct]
+ -[SDBetaEnrollmentServiceProxy _SDErrorForDaemonClientErrorType]
+ -[SDBetaEnrollmentServiceProxy betaEnrollmentProxyObjectWithCompletion:]
+ -[SDBetaEnrollmentServiceProxy betaEnrollmentProxyObjectWithCompletion:].cold.1
+ -[SDBetaEnrollmentServiceProxy canCurrentDeviceEnrollInBetaProgram]
+ -[SDBetaEnrollmentServiceProxy canFileFeedbackOnDevice:completion:]
+ -[SDBetaEnrollmentServiceProxy configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:error:]
+ -[SDBetaEnrollmentServiceProxy daemonConnection]
+ -[SDBetaEnrollmentServiceProxy deleteSeedingAppleAccountWithCompletion:]
+ -[SDBetaEnrollmentServiceProxy deviceAppleIDUsernameForCurrentDevice]
+ -[SDBetaEnrollmentServiceProxy enrollDevice:inProgram:completion:]
+ -[SDBetaEnrollmentServiceProxy enrollInProgramWithToken:completion:]
+ -[SDBetaEnrollmentServiceProxy enrolledBetaProgramForDevice:completion:]
+ -[SDBetaEnrollmentServiceProxy getCurrentDevice:]
+ -[SDBetaEnrollmentServiceProxy getCurrentDeviceEnrolledBetaProgramSynchronously]
+ -[SDBetaEnrollmentServiceProxy getCurrentDeviceSynchronously]
+ -[SDBetaEnrollmentServiceProxy getDevicesForPlatforms:completion:]
+ -[SDBetaEnrollmentServiceProxy init]
+ -[SDBetaEnrollmentServiceProxy initializeDaemonConnection]
+ -[SDBetaEnrollmentServiceProxy invalidateCacheWithCompletion:]
+ -[SDBetaEnrollmentServiceProxy isCurrentDeviceUsingSeedingAppleID]
+ -[SDBetaEnrollmentServiceProxy isDeviceEnrolledInBetaProgram:completion:]
+ -[SDBetaEnrollmentServiceProxy loadMDMConfigurationWithError:]
+ -[SDBetaEnrollmentServiceProxy queryProgramsForSystemAccountsWithPlatforms:completion:]
+ -[SDBetaEnrollmentServiceProxy seedingAppleIDUsernameForCurrentDevice:]
+ -[SDBetaEnrollmentServiceProxy seedingAppleIDUsernameForCurrentDevice]
+ -[SDBetaEnrollmentServiceProxy setAppleAccountIdentifierWithAlternateDSIDForCurrentDevice:completion:]
+ -[SDBetaEnrollmentServiceProxy setDaemonConnection:]
+ -[SDBetaEnrollmentServiceProxy synchronousDaemonRemoteObjectProxyWithError:]
+ -[SDBetaEnrollmentServiceProxy synchronousDaemonRemoteObjectProxyWithError:].cold.1
+ -[SDBetaEnrollmentServiceProxy synchronousDaemonRemoteObjectProxy]
+ -[SDBetaEnrollmentServiceProxy unenrollDevice:completion:]
+ -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:completion:]
+ -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:completion:].cold.1
+ -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:completion:].cold.2
+ -[SDBetaManager cachePrograms:forPlatforms:]
+ -[SDBetaManager isCacheValidForPlatforms:withMDMConfigurationDate:]
+ -[SDBetaManager parseProgramsResponse:platforms:shouldCache:skipsBuildMatching:]
+ -[SDBetaManager validateBetaEnrollmentTokens:errorHandler:]
+ -[SDBetaManager validateBetaEnrollmentTokens:errorHandler:].cold.1
+ -[SDBetaProgram betaEnrollmentTokens]
+ -[SDBetaProgram initWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:betaEnrollmentTokens:]
+ -[SDBetaProgram setBetaEnrollmentTokens:]
+ -[SDMDMConfiguration configurationDate]
+ -[SDMDMConfiguration isMissingConfigurationDate]
+ -[SDMDMConfiguration setConfigurationDate:]
+ GCC_except_table10
+ GCC_except_table117
+ GCC_except_table168
+ GCC_except_table40
+ GCC_except_table93
+ GCC_except_table98
+ Log.cold.1
+ OBJC_IVAR_$_SDBetaEnrollmentDaemon._connection
+ OBJC_IVAR_$_SDBetaEnrollmentDaemonProxy._daemonConnection
+ OBJC_IVAR_$_SDBetaEnrollmentService._appConnections
+ OBJC_IVAR_$_SDBetaEnrollmentService._listener
+ OBJC_IVAR_$_SDBetaEnrollmentService._profileToken
+ OBJC_IVAR_$_SDBetaEnrollmentService._userIdentifier
+ OBJC_IVAR_$_SDBetaEnrollmentServiceProxy._daemonConnection
+ OBJC_IVAR_$_SDBetaProgram._betaEnrollmentTokens
+ OBJC_IVAR_$_SDMDMConfiguration._configurationDate
+ SeedingDefaults.cold.1
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_SDBetaEnrollmentDaemon
+ _OBJC_CLASS_$_SDBetaEnrollmentDaemonProxy
+ _OBJC_CLASS_$_SDBetaEnrollmentService
+ _OBJC_CLASS_$_SDBetaEnrollmentServiceProxy
+ _OBJC_CLASS_$_SDMDMConfiguratorImplementation
+ _OBJC_METACLASS_$_SDBetaEnrollmentDaemon
+ _OBJC_METACLASS_$_SDBetaEnrollmentDaemonProxy
+ _OBJC_METACLASS_$_SDBetaEnrollmentService
+ _OBJC_METACLASS_$_SDBetaEnrollmentServiceProxy
+ _OBJC_METACLASS_$_SDMDMConfiguratorImplementation
+ _SDBESEntitlementName
+ _SDBESMachServiceName
+ _SDDaemonMachService
+ _SDDaemonMachServiceEntitlement
+ _SDDaemonMachServiceOldEntitlement
+ _SDMDMConfiguratorErrorAddInvalidTokens
+ __132-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:completion:]_block_invoke.cold.1
+ __132-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:completion:]_block_invoke.cold.2
+ __132-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:completion:]_block_invoke.cold.3
+ __32-[SDBetaEnrollmentService start]_block_invoke.12
+ __32-[SDBetaEnrollmentService start]_block_invoke.18
+ __32-[SDBetaEnrollmentService start]_block_invoke.cold.1
+ __32-[SDBetaEnrollmentService start]_block_invoke.cold.2
+ __34-[SDBetaEnrollmentService checkIn]_block_invoke.31
+ __45+[SDBetaManager canFileFeedbackOnThisDevice:]_block_invoke.473
+ __46-[SDBetaEnrollmentDaemonProxy connectToDaemon]_block_invoke.71
+ __46-[SDBetaEnrollmentDaemonProxy connectToDaemon]_block_invoke.71.cold.1
+ __46-[SDBetaEnrollmentDaemonProxy connectToDaemon]_block_invoke.cold.1
+ __51-[SDBetaEnrollmentService remoteObjectProxyForPID:]_block_invoke.cold.1
+ __55-[SDBetaEnrollmentDaemonProxy removeBetaEnrollmentData]_block_invoke.cold.1
+ __57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.647
+ __57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.647.cold.1
+ __57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.647.cold.2
+ __57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.648
+ __57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.648.cold.1
+ __57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.648.cold.2
+ __57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.648.cold.3
+ __57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.649
+ __58-[SDBetaEnrollmentServiceProxy initializeDaemonConnection]_block_invoke.2
+ __58-[SDBetaEnrollmentServiceProxy initializeDaemonConnection]_block_invoke.2.cold.1
+ __58-[SDBetaEnrollmentServiceProxy initializeDaemonConnection]_block_invoke.cold.1
+ __59+[SDBetaManager canFileFeedbackOnThisDeviceWithCompletion:]_block_invoke.479
+ __59-[SDBetaEnrollmentDaemonProxy synchronousRemoteObjectProxy]_block_invoke.cold.1
+ __59-[SDBetaManager validateBetaEnrollmentTokens:errorHandler:]_block_invoke.cold.1
+ __59-[SDBetaManager validateBetaEnrollmentTokens:errorHandler:]_block_invoke.cold.2
+ __61-[SDBetaEnrollmentDaemon listener:shouldAcceptNewConnection:]_block_invoke.2
+ __61-[SDBetaEnrollmentService enrollDevice:inProgram:completion:]_block_invoke.cold.1
+ __61-[SDBetaEnrollmentService enrollDevice:inProgram:completion:]_block_invoke.cold.2
+ __61-[SDBetaEnrollmentService enrollDevice:inProgram:completion:]_block_invoke.cold.3
+ __62-[SDBetaEnrollmentService listener:shouldAcceptNewConnection:]_block_invoke.22
+ __63-[SDBetaEnrollmentDaemonProxy remoteObjectProxyWithCompletion:]_block_invoke.cold.1
+ __64-[SDBetaManager enrollDevice:withEnrollmentMetadata:completion:]_block_invoke.407
+ __72-[SDBetaEnrollmentServiceProxy betaEnrollmentProxyObjectWithCompletion:]_block_invoke.cold.1
+ __73-[SDBetaManager _saveAppleAccountIdentifierWithAlternateDSID:completion:]_block_invoke.500
+ __75-[SDBetaEnrollmentDaemonProxy synchronousDaemonRemoteObjectProxyWithError:]_block_invoke.cold.1
+ __76-[SDBetaEnrollmentServiceProxy synchronousDaemonRemoteObjectProxyWithError:]_block_invoke.cold.1
+ __OBJC_$_CLASS_METHODS_SDBetaEnrollmentDaemon
+ __OBJC_$_CLASS_METHODS_SDBetaEnrollmentDaemonProxy
+ __OBJC_$_CLASS_METHODS_SDBetaEnrollmentService
+ __OBJC_$_CLASS_METHODS_SDBetaEnrollmentServiceProxy
+ __OBJC_$_CLASS_METHODS_SDMDMConfiguratorImplementation
+ __OBJC_$_INSTANCE_METHODS_SDBetaEnrollmentDaemon
+ __OBJC_$_INSTANCE_METHODS_SDBetaEnrollmentDaemonProxy
+ __OBJC_$_INSTANCE_METHODS_SDBetaEnrollmentService
+ __OBJC_$_INSTANCE_METHODS_SDBetaEnrollmentServiceProxy
+ __OBJC_$_INSTANCE_VARIABLES_SDBetaEnrollmentDaemon
+ __OBJC_$_INSTANCE_VARIABLES_SDBetaEnrollmentDaemonProxy
+ __OBJC_$_INSTANCE_VARIABLES_SDBetaEnrollmentService
+ __OBJC_$_INSTANCE_VARIABLES_SDBetaEnrollmentServiceProxy
+ __OBJC_$_PROP_LIST_SDBetaEnrollmentDaemon
+ __OBJC_$_PROP_LIST_SDBetaEnrollmentDaemonProxy
+ __OBJC_$_PROP_LIST_SDBetaEnrollmentService
+ __OBJC_$_PROP_LIST_SDBetaEnrollmentServiceProxy
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SDBetaEnrollmentDaemonInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SDBetaEnrollmentServiceInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SDBetaEnrollmentDaemonInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SDBetaEnrollmentServiceInterface
+ __OBJC_$_PROTOCOL_REFS_SDBetaEnrollmentClientInterface
+ __OBJC_$_PROTOCOL_REFS_SDBetaEnrollmentDaemonInterface
+ __OBJC_CLASS_PROTOCOLS_$_SDBetaEnrollmentDaemon
+ __OBJC_CLASS_PROTOCOLS_$_SDBetaEnrollmentDaemonProxy
+ __OBJC_CLASS_PROTOCOLS_$_SDBetaEnrollmentService
+ __OBJC_CLASS_PROTOCOLS_$_SDBetaEnrollmentServiceProxy
+ __OBJC_CLASS_RO_$_SDBetaEnrollmentDaemon
+ __OBJC_CLASS_RO_$_SDBetaEnrollmentDaemonProxy
+ __OBJC_CLASS_RO_$_SDBetaEnrollmentService
+ __OBJC_CLASS_RO_$_SDBetaEnrollmentServiceProxy
+ __OBJC_CLASS_RO_$_SDMDMConfiguratorImplementation
+ __OBJC_LABEL_PROTOCOL_$_SDBetaEnrollmentClientInterface
+ __OBJC_LABEL_PROTOCOL_$_SDBetaEnrollmentDaemonInterface
+ __OBJC_LABEL_PROTOCOL_$_SDBetaEnrollmentServiceInterface
+ __OBJC_METACLASS_RO_$_SDBetaEnrollmentDaemon
+ __OBJC_METACLASS_RO_$_SDBetaEnrollmentDaemonProxy
+ __OBJC_METACLASS_RO_$_SDBetaEnrollmentService
+ __OBJC_METACLASS_RO_$_SDBetaEnrollmentServiceProxy
+ __OBJC_METACLASS_RO_$_SDMDMConfiguratorImplementation
+ __OBJC_PROTOCOL_$_SDBetaEnrollmentClientInterface
+ __OBJC_PROTOCOL_$_SDBetaEnrollmentDaemonInterface
+ __OBJC_PROTOCOL_$_SDBetaEnrollmentServiceInterface
+ __OBJC_PROTOCOL_REFERENCE_$_SDBetaEnrollmentClientInterface
+ __OBJC_PROTOCOL_REFERENCE_$_SDBetaEnrollmentDaemonInterface
+ __OBJC_PROTOCOL_REFERENCE_$_SDBetaEnrollmentServiceInterface
+ ___102-[SDBetaEnrollmentServiceProxy setAppleAccountIdentifierWithAlternateDSIDForCurrentDevice:completion:]_block_invoke
+ ___102-[SDBetaEnrollmentServiceProxy setAppleAccountIdentifierWithAlternateDSIDForCurrentDevice:completion:]_block_invoke_2
+ ___102-[SDBetaEnrollmentServiceProxy setAppleAccountIdentifierWithAlternateDSIDForCurrentDevice:completion:]_block_invoke_3
+ ___106-[SDBetaEnrollmentDaemonProxy configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:error:]_block_invoke
+ ___107-[SDBetaEnrollmentServiceProxy configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:error:]_block_invoke
+ ___132-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:completion:]_block_invoke
+ ___32-[SDBetaEnrollmentService start]_block_invoke
+ ___34-[SDBetaEnrollmentService checkIn]_block_invoke
+ ___40+[SDBetaEnrollmentDaemon sharedInstance]_block_invoke
+ ___41+[SDBetaEnrollmentService sharedInstance]_block_invoke
+ ___44-[SDBetaEnrollmentService getCurrentDevice:]_block_invoke
+ ___45+[SDBetaEnrollmentDaemonProxy sharedInstance]_block_invoke
+ ___46+[SDBetaEnrollmentServiceProxy sharedInstance]_block_invoke
+ ___46-[SDBetaEnrollmentDaemonProxy connectToDaemon]_block_invoke
+ ___47-[SDBetaEnrollmentService _verifyCurrentDevice]_block_invoke
+ ___47-[SDBetaEnrollmentService _verifyCurrentDevice]_block_invoke_2
+ ___49-[SDBetaEnrollmentServiceProxy getCurrentDevice:]_block_invoke
+ ___51-[SDBetaEnrollmentService remoteObjectProxyForPID:]_block_invoke
+ ___53-[SDBetaEnrollmentService unenrollDevice:completion:]_block_invoke
+ ___55-[SDBetaEnrollmentDaemonProxy removeBetaEnrollmentData]_block_invoke
+ ___58-[SDBetaEnrollmentServiceProxy initializeDaemonConnection]_block_invoke
+ ___58-[SDBetaEnrollmentServiceProxy unenrollDevice:completion:]_block_invoke
+ ___59-[SDBetaEnrollmentDaemonProxy synchronousRemoteObjectProxy]_block_invoke
+ ___59-[SDBetaManager validateBetaEnrollmentTokens:errorHandler:]_block_invoke
+ ___61-[SDBetaEnrollmentDaemon listener:shouldAcceptNewConnection:]_block_invoke
+ ___61-[SDBetaEnrollmentDaemonProxy loadMDMConfigurationWithError:]_block_invoke
+ ___61-[SDBetaEnrollmentService enrollDevice:inProgram:completion:]_block_invoke
+ ___61-[SDBetaEnrollmentService getDevicesForPlatforms:completion:]_block_invoke
+ ___61-[SDBetaEnrollmentServiceProxy getCurrentDeviceSynchronously]_block_invoke
+ ___62-[SDBetaEnrollmentDaemonProxy isPreReleaseInstallationAllowed]_block_invoke
+ ___62-[SDBetaEnrollmentDaemonProxy saveMDMConfiguration:withError:]_block_invoke
+ ___62-[SDBetaEnrollmentService canFileFeedbackOnDevice:completion:]_block_invoke
+ ___62-[SDBetaEnrollmentService listener:shouldAcceptNewConnection:]_block_invoke
+ ___62-[SDBetaEnrollmentServiceProxy invalidateCacheWithCompletion:]_block_invoke
+ ___62-[SDBetaEnrollmentServiceProxy loadMDMConfigurationWithError:]_block_invoke
+ ___63-[SDBetaEnrollmentDaemonProxy remoteObjectProxyWithCompletion:]_block_invoke
+ ___66-[SDBetaEnrollmentDaemonProxy fetchBetaEnrollmentTokensWithError:]_block_invoke
+ ___66-[SDBetaEnrollmentServiceProxy enrollDevice:inProgram:completion:]_block_invoke
+ ___66-[SDBetaEnrollmentServiceProxy getDevicesForPlatforms:completion:]_block_invoke
+ ___66-[SDBetaEnrollmentServiceProxy isCurrentDeviceUsingSeedingAppleID]_block_invoke
+ ___67-[SDBetaEnrollmentService enrolledBetaProgramForDevice:completion:]_block_invoke
+ ___67-[SDBetaEnrollmentServiceProxy canCurrentDeviceEnrollInBetaProgram]_block_invoke
+ ___67-[SDBetaEnrollmentServiceProxy canFileFeedbackOnDevice:completion:]_block_invoke
+ ___68-[SDBetaEnrollmentService isDeviceEnrolledInBetaProgram:completion:]_block_invoke
+ ___68-[SDBetaEnrollmentServiceProxy enrollInProgramWithToken:completion:]_block_invoke
+ ___68-[SDBetaEnrollmentServiceProxy enrollInProgramWithToken:completion:]_block_invoke_2
+ ___69-[SDBetaEnrollmentServiceProxy deviceAppleIDUsernameForCurrentDevice]_block_invoke
+ ___70-[SDBetaEnrollmentServiceProxy seedingAppleIDUsernameForCurrentDevice]_block_invoke
+ ___71-[SDBetaEnrollmentServiceProxy seedingAppleIDUsernameForCurrentDevice:]_block_invoke
+ ___71-[SDBetaEnrollmentServiceProxy seedingAppleIDUsernameForCurrentDevice:]_block_invoke_2
+ ___71-[SDBetaEnrollmentServiceProxy seedingAppleIDUsernameForCurrentDevice:]_block_invoke_3
+ ___72-[SDBetaEnrollmentServiceProxy betaEnrollmentProxyObjectWithCompletion:]_block_invoke
+ ___72-[SDBetaEnrollmentServiceProxy deleteSeedingAppleAccountWithCompletion:]_block_invoke
+ ___72-[SDBetaEnrollmentServiceProxy deleteSeedingAppleAccountWithCompletion:]_block_invoke_2
+ ___72-[SDBetaEnrollmentServiceProxy deleteSeedingAppleAccountWithCompletion:]_block_invoke_3
+ ___72-[SDBetaEnrollmentServiceProxy enrolledBetaProgramForDevice:completion:]_block_invoke
+ ___73-[SDBetaEnrollmentService deleteSeedingAppleAccountForDevice:completion:]_block_invoke
+ ___73-[SDBetaEnrollmentServiceProxy isDeviceEnrolledInBetaProgram:completion:]_block_invoke
+ ___75-[SDBetaEnrollmentDaemonProxy synchronousDaemonRemoteObjectProxyWithError:]_block_invoke
+ ___76-[SDBetaEnrollmentServiceProxy synchronousDaemonRemoteObjectProxyWithError:]_block_invoke
+ ___80+[SDMDMConfiguratorImplementation enrollWithRequireProgramToken:userIdentifier:]_block_invoke
+ ___80-[SDBetaEnrollmentServiceProxy getCurrentDeviceEnrolledBetaProgramSynchronously]_block_invoke
+ ___87-[SDBetaEnrollmentServiceProxy queryProgramsForSystemAccountsWithPlatforms:completion:]_block_invoke
+ ___89+[SDMDMConfiguratorImplementation shouldReturnBecauseOfInvalidTokens:andReportErrorWith:]_block_invoke
+ ___91-[SDBetaEnrollmentDaemon setupAssistant_enrollInProgramWithBetaEnrollmentToken:completion:]_block_invoke
+ ___91-[SDBetaEnrollmentService setAppleAccountIdentifierFromAlternateDSID:forDevice:completion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e56_v24?0"<SDBetaEnrollmentServiceInterface>"8"NSError"16l
+ ___block_descriptor_48_e8_32bs_e56_v24?0"<SDBetaEnrollmentServiceInterface>"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e56_v24?0"<SDBetaEnrollmentServiceInterface>"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48bs_e56_v24?0"<SDBetaEnrollmentServiceInterface>"8"NSError"16l
+ ___block_descriptor_65_e8_32s40bs48w_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24l
+ ___copy_helper_block_e8_32s40b48w
+ ___destroy_helper_block_e8_32s40s48w
+ __allowListedXPCClientInterface
+ __allowListedXPCServerInterface
+ __block_literal_global.117
+ __block_literal_global.15
+ __block_literal_global.151
+ __block_literal_global.179
+ __block_literal_global.21
+ __block_literal_global.33
+ __block_literal_global.35
+ __block_literal_global.38
+ __block_literal_global.421
+ __block_literal_global.423
+ __block_literal_global.457
+ __block_literal_global.79
+ __block_literal_global.89
+ _dispatch_group_wait
+ _objc_msgSend$_finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:completion:
+ _objc_msgSend$activate
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$betaEnrollmentProxyObjectWithCompletion:
+ _objc_msgSend$betaEnrollmentTokens
+ _objc_msgSend$cachePrograms:forPlatforms:
+ _objc_msgSend$configurationDate
+ _objc_msgSend$containsValueForKey:
+ _objc_msgSend$distantPast
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$initWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:betaEnrollmentTokens:
+ _objc_msgSend$intersectsSet:
+ _objc_msgSend$isCacheValidForPlatforms:withMDMConfigurationDate:
+ _objc_msgSend$isEqualToDate:
+ _objc_msgSend$isMissingConfigurationDate
+ _objc_msgSend$minusSet:
+ _objc_msgSend$parseProgramsResponse:platforms:shouldCache:skipsBuildMatching:
+ _objc_msgSend$setBetaEnrollmentTokens:
+ _objc_msgSend$setConfigurationDate:
+ _objc_msgSend$setWithCapacity:
+ _objc_msgSend$setWithSet:
+ _objc_msgSend$shouldReturnBecauseOfInvalidTokens:andReportErrorWith:
+ _objc_msgSend$userInfo
+ _objc_msgSend$validateBetaEnrollmentTokens:errorHandler:
+ _sd_SUPreferenceManager.cold.2
- +[SDBetaEnrollmentHelper sharedInstance]
- +[SDBetaProgram betaProgramWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:betaEnrollmentToken:]
- +[SDDaemon sharedInstance]
- +[SDDaemonClient sharedInstance]
- +[SDDaemonCommon _allowListedXPCClientInterface]
- +[SDDaemonCommon _allowListedXPCServerInterface]
- +[SDMDMConfigurator enrollInProgramWithMDMToken:completion:]
- +[SDMDMConfiguratorDaemon applyMDMConfiguration:]
- +[SDMDMConfiguratorDaemon conditionallyUnenrollIfNotMatchingOfferedTokensWithConfig:userIdentifier:]
- +[SDMDMConfiguratorDaemon conditionallyUnenrollIfNotMatchingOfferedTokensWithConfig:userIdentifier:].cold.1
- +[SDMDMConfiguratorDaemon configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:userIdentifier:completion:]
- +[SDMDMConfiguratorDaemon configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:userIdentifier:completion:].cold.1
- +[SDMDMConfiguratorDaemon enrollWithRequireProgramToken:userIdentifier:]
- +[SDMDMConfiguratorDaemon enrollWithRequireProgramToken:userIdentifier:].cold.1
- +[SDMDMConfiguratorDaemon isBetaEnrollmentDisabled]
- +[SDMDMConfiguratorDaemon isBetaEnrollmentDisabled].cold.1
- -[SDBetaEnrollmentHelper .cxx_destruct]
- -[SDBetaEnrollmentHelper addFBAHelpMenu:]
- -[SDBetaEnrollmentHelper addFBASymlink:]
- -[SDBetaEnrollmentHelper connectToDaemon]
- -[SDBetaEnrollmentHelper daemonConnection]
- -[SDBetaEnrollmentHelper fetchBetaEnrollmentTokensWithError:]
- -[SDBetaEnrollmentHelper init]
- -[SDBetaEnrollmentHelper isPreReleaseInstallationAllowed]
- -[SDBetaEnrollmentHelper loadMDMConfigurationWithError:]
- -[SDBetaEnrollmentHelper remoteObjectProxyWithCompletion:]
- -[SDBetaEnrollmentHelper remoteObjectProxy]
- -[SDBetaEnrollmentHelper removeBetaEnrollmentData]
- -[SDBetaEnrollmentHelper removeFBAHelpMenu:]
- -[SDBetaEnrollmentHelper removeSeedEnrollmentCookie:]
- -[SDBetaEnrollmentHelper saveMDMConfiguration:withError:]
- -[SDBetaEnrollmentHelper setDaemonConnection:]
- -[SDBetaEnrollmentHelper setupAssistant_enrollInProgramWithBetaEnrollmentToken:completion:]
- -[SDBetaEnrollmentHelper synchronousDaemonRemoteObjectProxyWithError:]
- -[SDBetaEnrollmentHelper synchronousRemoteObjectProxy]
- -[SDBetaEnrollmentHelperDaemon .cxx_destruct]
- -[SDBetaEnrollmentHelperDaemon addFBAHelpMenu:]
- -[SDBetaEnrollmentHelperDaemon addFBASymlink:]
- -[SDBetaEnrollmentHelperDaemon connection]
- -[SDBetaEnrollmentHelperDaemon fetchBetaEnrollmentTokens:]
- -[SDBetaEnrollmentHelperDaemon isPreReleaseInstallationAllowed:]
- -[SDBetaEnrollmentHelperDaemon listener:shouldAcceptNewConnection:]
- -[SDBetaEnrollmentHelperDaemon listener:shouldAcceptNewConnection:].cold.1
- -[SDBetaEnrollmentHelperDaemon loadMDMConfigurationWithCompletion:]
- -[SDBetaEnrollmentHelperDaemon removeBetaEnrollmentData:]
- -[SDBetaEnrollmentHelperDaemon removeFBAHelpMenu:]
- -[SDBetaEnrollmentHelperDaemon removeSeedEnrollmentCookie:]
- -[SDBetaEnrollmentHelperDaemon saveMDMConfiguration:withCompletion:]
- -[SDBetaEnrollmentHelperDaemon setConnection:]
- -[SDBetaEnrollmentHelperDaemon setupAssistant_enrollInProgramWithBetaEnrollmentToken:completion:]
- -[SDBetaEnrollmentHelperDaemon start]
- -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:completion:]
- -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:completion:].cold.1
- -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:completion:].cold.2
- -[SDBetaManager savePrograms:forPlatforms:]
- -[SDBetaManager saveResponse:platforms:]
- -[SDBetaProgram betaEnrollmentToken]
- -[SDBetaProgram initWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:betaEnrollmentToken:]
- -[SDBetaProgram setBetaEnrollmentToken:]
- -[SDDaemon .cxx_destruct]
- -[SDDaemon _connectionForPid:]
- -[SDDaemon _releaseAppConnectionWithPid:]
- -[SDDaemon _startListeningForProfileChanges]
- -[SDDaemon _stopListeningForProfileChanges]
- -[SDDaemon _storeAppConnection:]
- -[SDDaemon _verifyCurrentDevice]
- -[SDDaemon appConnections]
- -[SDDaemon canDeviceEnrollInBetaUpdates:completion:]
- -[SDDaemon canFileFeedbackOnDevice:completion:]
- -[SDDaemon checkIn]
- -[SDDaemon configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:completion:]
- -[SDDaemon dealloc]
- -[SDDaemon deleteSeedingAppleAccountForDevice:completion:]
- -[SDDaemon enrollDevice:inProgram:completion:]
- -[SDDaemon enrollInProgramWithToken:completion:]
- -[SDDaemon enrolledBetaProgramForDevice:completion:]
- -[SDDaemon getCurrentDevice:]
- -[SDDaemon getCurrentPrimaryAppleIDForDevice:completion:]
- -[SDDaemon getCurrentSeedingAppleIDForDevice:completion:]
- -[SDDaemon getDevicesForPlatforms:completion:]
- -[SDDaemon invalidateDaemonCacheWithCompletion:]
- -[SDDaemon isDeviceEnrolledInBetaProgram:completion:]
- -[SDDaemon isDeviceUsingSeedingAppleID:completion:]
- -[SDDaemon listener:shouldAcceptNewConnection:]
- -[SDDaemon listener:shouldAcceptNewConnection:].cold.1
- -[SDDaemon listener]
- -[SDDaemon loadMDMConfigurationWithCompletion:]
- -[SDDaemon profileToken]
- -[SDDaemon queryProgramsForSystemAccountsWithPlatforms:completion:]
- -[SDDaemon remoteObjectProxyForPID:]
- -[SDDaemon setAppConnections:]
- -[SDDaemon setAppleAccountIdentifierFromAlternateDSID:forDevice:completion:]
- -[SDDaemon setListener:]
- -[SDDaemon setProfileToken:]
- -[SDDaemon setUserIdentifier:]
- -[SDDaemon start]
- -[SDDaemon unenrollDevice:completion:]
- -[SDDaemon userIdentifier]
- -[SDDaemonClient .cxx_destruct]
- -[SDDaemonClient _SDErrorForDaemonClientErrorType]
- -[SDDaemonClient betaenrollmentdProxyObjectWithCompletion:]
- -[SDDaemonClient betaenrollmentdProxyObjectWithCompletion:].cold.1
- -[SDDaemonClient canCurrentDeviceEnrollInBetaProgram]
- -[SDDaemonClient canFileFeedbackOnDevice:completion:]
- -[SDDaemonClient configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:error:]
- -[SDDaemonClient daemonConnection]
- -[SDDaemonClient deleteSeedingAppleAccountWithCompletion:]
- -[SDDaemonClient deviceAppleIDUsernameForCurrentDevice]
- -[SDDaemonClient enrollDevice:inProgram:completion:]
- -[SDDaemonClient enrollInProgramWithToken:completion:]
- -[SDDaemonClient enrolledBetaProgramForDevice:completion:]
- -[SDDaemonClient getCurrentDevice:]
- -[SDDaemonClient getCurrentDeviceEnrolledBetaProgramSynchronously]
- -[SDDaemonClient getCurrentDeviceSynchronously]
- -[SDDaemonClient getDevicesForPlatforms:completion:]
- -[SDDaemonClient init]
- -[SDDaemonClient initializeDaemonConnection]
- -[SDDaemonClient invalidateCacheWithCompletion:]
- -[SDDaemonClient isCurrentDeviceUsingSeedingAppleID]
- -[SDDaemonClient isDeviceEnrolledInBetaProgram:completion:]
- -[SDDaemonClient loadMDMConfigurationWithError:]
- -[SDDaemonClient queryProgramsForSystemAccountsWithPlatforms:completion:]
- -[SDDaemonClient seedingAppleIDUsernameForCurrentDevice:]
- -[SDDaemonClient seedingAppleIDUsernameForCurrentDevice]
- -[SDDaemonClient setAppleAccountIdentifierWithAlternateDSIDForCurrentDevice:completion:]
- -[SDDaemonClient setDaemonConnection:]
- -[SDDaemonClient synchronousDaemonRemoteObjectProxyWithError:]
- -[SDDaemonClient synchronousDaemonRemoteObjectProxyWithError:].cold.1
- -[SDDaemonClient synchronousDaemonRemoteObjectProxy]
- -[SDDaemonClient unenrollDevice:completion:]
- GCC_except_table114
- GCC_except_table162
- GCC_except_table23
- GCC_except_table31
- GCC_except_table90
- GCC_except_table95
- OBJC_IVAR_$_SDBetaEnrollmentHelper._daemonConnection
- OBJC_IVAR_$_SDBetaEnrollmentHelperDaemon._connection
- OBJC_IVAR_$_SDBetaProgram._betaEnrollmentToken
- OBJC_IVAR_$_SDDaemon._appConnections
- OBJC_IVAR_$_SDDaemon._listener
- OBJC_IVAR_$_SDDaemon._profileToken
- OBJC_IVAR_$_SDDaemon._userIdentifier
- OBJC_IVAR_$_SDDaemonClient._daemonConnection
- _OBJC_CLASS_$_SDBetaEnrollmentHelper
- _OBJC_CLASS_$_SDBetaEnrollmentHelperDaemon
- _OBJC_CLASS_$_SDDaemon
- _OBJC_CLASS_$_SDDaemonClient
- _OBJC_CLASS_$_SDDaemonCommon
- _OBJC_CLASS_$_SDMDMConfiguratorDaemon
- _OBJC_METACLASS_$_SDBetaEnrollmentHelper
- _OBJC_METACLASS_$_SDBetaEnrollmentHelperDaemon
- _OBJC_METACLASS_$_SDDaemon
- _OBJC_METACLASS_$_SDDaemonClient
- _OBJC_METACLASS_$_SDDaemonCommon
- _OBJC_METACLASS_$_SDMDMConfiguratorDaemon
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _SDBetaEnrollmentHelperDaemonMachService
- _SDBetaEnrollmentHelperDaemonMachServiceEntitlement
- _SDMachServiceName
- __113-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:completion:]_block_invoke.cold.1
- __113-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:completion:]_block_invoke.cold.2
- __113-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:completion:]_block_invoke.cold.3
- __17-[SDDaemon start]_block_invoke.15
- __17-[SDDaemon start]_block_invoke.21
- __17-[SDDaemon start]_block_invoke.cold.1
- __17-[SDDaemon start]_block_invoke.cold.2
- __19-[SDDaemon checkIn]_block_invoke.35
- __36-[SDDaemon remoteObjectProxyForPID:]_block_invoke.cold.1
- __41-[SDBetaEnrollmentHelper connectToDaemon]_block_invoke.66
- __41-[SDBetaEnrollmentHelper connectToDaemon]_block_invoke.66.cold.1
- __41-[SDBetaEnrollmentHelper connectToDaemon]_block_invoke.cold.1
- __44-[SDDaemonClient initializeDaemonConnection]_block_invoke.3
- __44-[SDDaemonClient initializeDaemonConnection]_block_invoke.3.cold.1
- __44-[SDDaemonClient initializeDaemonConnection]_block_invoke.cold.1
- __45+[SDBetaManager canFileFeedbackOnThisDevice:]_block_invoke.470
- __46-[SDDaemon enrollDevice:inProgram:completion:]_block_invoke.cold.1
- __46-[SDDaemon enrollDevice:inProgram:completion:]_block_invoke.cold.2
- __46-[SDDaemon enrollDevice:inProgram:completion:]_block_invoke.cold.3
- __47-[SDDaemon listener:shouldAcceptNewConnection:]_block_invoke.26
- __50-[SDBetaEnrollmentHelper removeBetaEnrollmentData]_block_invoke.cold.1
- __54-[SDBetaEnrollmentHelper synchronousRemoteObjectProxy]_block_invoke.cold.1
- __57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.640
- __57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.643
- __57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.643.cold.1
- __57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.643.cold.2
- __57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.644.cold.1
- __57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.644.cold.2
- __57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.644.cold.3
- __57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.645
- __58-[SDBetaEnrollmentHelper remoteObjectProxyWithCompletion:]_block_invoke.cold.1
- __59+[SDBetaManager canFileFeedbackOnThisDeviceWithCompletion:]_block_invoke.476
- __59-[SDDaemonClient betaenrollmentdProxyObjectWithCompletion:]_block_invoke.cold.1
- __62-[SDDaemonClient synchronousDaemonRemoteObjectProxyWithError:]_block_invoke.cold.1
- __64-[SDBetaManager enrollDevice:withEnrollmentMetadata:completion:]_block_invoke.404
- __67-[SDBetaEnrollmentHelperDaemon listener:shouldAcceptNewConnection:]_block_invoke.1
- __70-[SDBetaEnrollmentHelper synchronousDaemonRemoteObjectProxyWithError:]_block_invoke.cold.1
- __73-[SDBetaManager _saveAppleAccountIdentifierWithAlternateDSID:completion:]_block_invoke.499
- __OBJC_$_CLASS_METHODS_SDBetaEnrollmentHelper
- __OBJC_$_CLASS_METHODS_SDDaemon
- __OBJC_$_CLASS_METHODS_SDDaemonClient
- __OBJC_$_CLASS_METHODS_SDDaemonCommon
- __OBJC_$_CLASS_METHODS_SDMDMConfiguratorDaemon
- __OBJC_$_INSTANCE_METHODS_SDBetaEnrollmentHelper
- __OBJC_$_INSTANCE_METHODS_SDBetaEnrollmentHelperDaemon
- __OBJC_$_INSTANCE_METHODS_SDDaemon
- __OBJC_$_INSTANCE_METHODS_SDDaemonClient
- __OBJC_$_INSTANCE_VARIABLES_SDBetaEnrollmentHelper
- __OBJC_$_INSTANCE_VARIABLES_SDBetaEnrollmentHelperDaemon
- __OBJC_$_INSTANCE_VARIABLES_SDDaemon
- __OBJC_$_INSTANCE_VARIABLES_SDDaemonClient
- __OBJC_$_PROP_LIST_SDBetaEnrollmentHelper
- __OBJC_$_PROP_LIST_SDBetaEnrollmentHelperDaemon
- __OBJC_$_PROP_LIST_SDDaemon
- __OBJC_$_PROP_LIST_SDDaemonClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SDBetaEnrollmentHelperDaemonInterface
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SDDaemonXPCServer
- __OBJC_$_PROTOCOL_METHOD_TYPES_SDBetaEnrollmentHelperDaemonInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_SDDaemonXPCServer
- __OBJC_$_PROTOCOL_REFS_SDBetaEnrollmentHelperDaemonInterface
- __OBJC_$_PROTOCOL_REFS_SDDaemonXPCClient
- __OBJC_CLASS_PROTOCOLS_$_SDBetaEnrollmentHelper
- __OBJC_CLASS_PROTOCOLS_$_SDBetaEnrollmentHelperDaemon
- __OBJC_CLASS_PROTOCOLS_$_SDDaemon
- __OBJC_CLASS_PROTOCOLS_$_SDDaemonClient
- __OBJC_CLASS_RO_$_SDBetaEnrollmentHelper
- __OBJC_CLASS_RO_$_SDBetaEnrollmentHelperDaemon
- __OBJC_CLASS_RO_$_SDDaemon
- __OBJC_CLASS_RO_$_SDDaemonClient
- __OBJC_CLASS_RO_$_SDDaemonCommon
- __OBJC_CLASS_RO_$_SDMDMConfiguratorDaemon
- __OBJC_LABEL_PROTOCOL_$_SDBetaEnrollmentHelperDaemonInterface
- __OBJC_LABEL_PROTOCOL_$_SDDaemonXPCClient
- __OBJC_LABEL_PROTOCOL_$_SDDaemonXPCServer
- __OBJC_METACLASS_RO_$_SDBetaEnrollmentHelper
- __OBJC_METACLASS_RO_$_SDBetaEnrollmentHelperDaemon
- __OBJC_METACLASS_RO_$_SDDaemon
- __OBJC_METACLASS_RO_$_SDDaemonClient
- __OBJC_METACLASS_RO_$_SDDaemonCommon
- __OBJC_METACLASS_RO_$_SDMDMConfiguratorDaemon
- __OBJC_PROTOCOL_$_SDBetaEnrollmentHelperDaemonInterface
- __OBJC_PROTOCOL_$_SDDaemonXPCClient
- __OBJC_PROTOCOL_$_SDDaemonXPCServer
- __OBJC_PROTOCOL_REFERENCE_$_SDBetaEnrollmentHelperDaemonInterface
- __OBJC_PROTOCOL_REFERENCE_$_SDDaemonXPCClient
- __OBJC_PROTOCOL_REFERENCE_$_SDDaemonXPCServer
- ___113-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:completion:]_block_invoke
- ___17-[SDDaemon start]_block_invoke
- ___19-[SDDaemon checkIn]_block_invoke
- ___26+[SDDaemon sharedInstance]_block_invoke
- ___29-[SDDaemon getCurrentDevice:]_block_invoke
- ___32+[SDDaemonClient sharedInstance]_block_invoke
- ___32-[SDDaemon _verifyCurrentDevice]_block_invoke
- ___32-[SDDaemon _verifyCurrentDevice]_block_invoke_2
- ___35-[SDDaemonClient getCurrentDevice:]_block_invoke
- ___36-[SDDaemon remoteObjectProxyForPID:]_block_invoke
- ___38-[SDDaemon unenrollDevice:completion:]_block_invoke
- ___40+[SDBetaEnrollmentHelper sharedInstance]_block_invoke
- ___41-[SDBetaEnrollmentHelper connectToDaemon]_block_invoke
- ___44-[SDDaemonClient initializeDaemonConnection]_block_invoke
- ___44-[SDDaemonClient unenrollDevice:completion:]_block_invoke
- ___46-[SDDaemon enrollDevice:inProgram:completion:]_block_invoke
- ___46-[SDDaemon getDevicesForPlatforms:completion:]_block_invoke
- ___47-[SDDaemon canFileFeedbackOnDevice:completion:]_block_invoke
- ___47-[SDDaemon listener:shouldAcceptNewConnection:]_block_invoke
- ___47-[SDDaemonClient getCurrentDeviceSynchronously]_block_invoke
- ___48-[SDDaemonClient invalidateCacheWithCompletion:]_block_invoke
- ___48-[SDDaemonClient loadMDMConfigurationWithError:]_block_invoke
- ___50-[SDBetaEnrollmentHelper removeBetaEnrollmentData]_block_invoke
- ___52-[SDDaemon enrolledBetaProgramForDevice:completion:]_block_invoke
- ___52-[SDDaemonClient enrollDevice:inProgram:completion:]_block_invoke
- ___52-[SDDaemonClient getDevicesForPlatforms:completion:]_block_invoke
- ___52-[SDDaemonClient isCurrentDeviceUsingSeedingAppleID]_block_invoke
- ___53-[SDDaemon isDeviceEnrolledInBetaProgram:completion:]_block_invoke
- ___53-[SDDaemonClient canCurrentDeviceEnrollInBetaProgram]_block_invoke
- ___53-[SDDaemonClient canFileFeedbackOnDevice:completion:]_block_invoke
- ___54-[SDBetaEnrollmentHelper synchronousRemoteObjectProxy]_block_invoke
- ___54-[SDDaemonClient enrollInProgramWithToken:completion:]_block_invoke
- ___54-[SDDaemonClient enrollInProgramWithToken:completion:]_block_invoke_2
- ___55-[SDDaemonClient deviceAppleIDUsernameForCurrentDevice]_block_invoke
- ___56-[SDBetaEnrollmentHelper loadMDMConfigurationWithError:]_block_invoke
- ___56-[SDDaemonClient seedingAppleIDUsernameForCurrentDevice]_block_invoke
- ___57-[SDBetaEnrollmentHelper isPreReleaseInstallationAllowed]_block_invoke
- ___57-[SDBetaEnrollmentHelper saveMDMConfiguration:withError:]_block_invoke
- ___57-[SDDaemonClient seedingAppleIDUsernameForCurrentDevice:]_block_invoke
- ___57-[SDDaemonClient seedingAppleIDUsernameForCurrentDevice:]_block_invoke_2
- ___57-[SDDaemonClient seedingAppleIDUsernameForCurrentDevice:]_block_invoke_3
- ___58-[SDBetaEnrollmentHelper remoteObjectProxyWithCompletion:]_block_invoke
- ___58-[SDDaemon deleteSeedingAppleAccountForDevice:completion:]_block_invoke
- ___58-[SDDaemonClient deleteSeedingAppleAccountWithCompletion:]_block_invoke
- ___58-[SDDaemonClient deleteSeedingAppleAccountWithCompletion:]_block_invoke_2
- ___58-[SDDaemonClient deleteSeedingAppleAccountWithCompletion:]_block_invoke_3
- ___58-[SDDaemonClient enrolledBetaProgramForDevice:completion:]_block_invoke
- ___59-[SDDaemonClient betaenrollmentdProxyObjectWithCompletion:]_block_invoke
- ___59-[SDDaemonClient isDeviceEnrolledInBetaProgram:completion:]_block_invoke
- ___61-[SDBetaEnrollmentHelper fetchBetaEnrollmentTokensWithError:]_block_invoke
- ___62-[SDDaemonClient synchronousDaemonRemoteObjectProxyWithError:]_block_invoke
- ___66-[SDDaemonClient getCurrentDeviceEnrolledBetaProgramSynchronously]_block_invoke
- ___67-[SDBetaEnrollmentHelperDaemon listener:shouldAcceptNewConnection:]_block_invoke
- ___70-[SDBetaEnrollmentHelper synchronousDaemonRemoteObjectProxyWithError:]_block_invoke
- ___72+[SDMDMConfiguratorDaemon enrollWithRequireProgramToken:userIdentifier:]_block_invoke
- ___73-[SDDaemonClient queryProgramsForSystemAccountsWithPlatforms:completion:]_block_invoke
- ___76-[SDDaemon setAppleAccountIdentifierFromAlternateDSID:forDevice:completion:]_block_invoke
- ___88-[SDDaemonClient setAppleAccountIdentifierWithAlternateDSIDForCurrentDevice:completion:]_block_invoke
- ___88-[SDDaemonClient setAppleAccountIdentifierWithAlternateDSIDForCurrentDevice:completion:]_block_invoke_2
- ___88-[SDDaemonClient setAppleAccountIdentifierWithAlternateDSIDForCurrentDevice:completion:]_block_invoke_3
- ___93-[SDDaemonClient configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:error:]_block_invoke
- ___97-[SDBetaEnrollmentHelperDaemon setupAssistant_enrollInProgramWithBetaEnrollmentToken:completion:]_block_invoke
- ___block_descriptor_40_e8_32bs_e41_v24?0"<SDDaemonXPCServer>"8"NSError"16l
- ___block_descriptor_40_e8_32r_e8_v16?0q8l
- ___block_descriptor_48_e8_32bs_e41_v24?0"<SDDaemonXPCServer>"8"NSError"16l
- ___block_descriptor_48_e8_32s40bs_e41_v24?0"<SDDaemonXPCServer>"8"NSError"16l
- ___block_descriptor_56_e8_32s40s48bs_e41_v24?0"<SDDaemonXPCServer>"8"NSError"16l
- ___block_descriptor_80_e8_32s40s48s56bs64w_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24l
- ___copy_helper_block_e8_32s40s48s56b64w
- ___destroy_helper_block_e8_32s40s48s56s64w
- __block_literal_global.110
- __block_literal_global.154
- __block_literal_global.18
- __block_literal_global.184
- __block_literal_global.24
- __block_literal_global.37
- __block_literal_global.39
- __block_literal_global.418
- __block_literal_global.42
- __block_literal_global.420
- __block_literal_global.451
- __block_literal_global.69
- _objc_msgSend$_allowListedXPCClientInterface
- _objc_msgSend$_allowListedXPCServerInterface
- _objc_msgSend$_finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:completion:
- _objc_msgSend$addEntriesFromDictionary:
- _objc_msgSend$appleIDHeadersForRequest:
- _objc_msgSend$betaEnrollmentToken
- _objc_msgSend$betaProgramWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:betaEnrollmentToken:
- _objc_msgSend$betaenrollmentdProxyObjectWithCompletion:
- _objc_msgSend$handleResponse:forRequest:shouldRetry:
- _objc_msgSend$initWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:betaEnrollmentToken:
- _objc_msgSend$isCacheValidForPlatforms:
- _objc_msgSend$savePrograms:forPlatforms:
- _objc_msgSend$saveResponse:platforms:
- _objc_msgSend$setBetaEnrollmentToken:
CStrings:
+ "%{public}s: -> launch daemon"
+ "%{public}s: running as root"
+ "+[SDMDMConfiguratorImplementation conditionallyUnenrollIfNotMatchingOfferedTokensWithConfig:userIdentifier:]"
+ "+[SDMDMConfiguratorImplementation enrollWithRequireProgramToken:userIdentifier:]"
+ "+[SDMDMConfiguratorImplementation shouldReturnBecauseOfInvalidTokens:andReportErrorWith:]"
+ "-[SDBetaEnrollmentDaemon addFBAHelpMenu:]"
+ "-[SDBetaEnrollmentDaemon addFBASymlink:]"
+ "-[SDBetaEnrollmentDaemon configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:completion:]"
+ "-[SDBetaEnrollmentDaemon fetchBetaEnrollmentTokens:]"
+ "-[SDBetaEnrollmentDaemon isPreReleaseInstallationAllowed:]"
+ "-[SDBetaEnrollmentDaemon loadMDMConfigurationWithCompletion:]"
+ "-[SDBetaEnrollmentDaemon removeFBAHelpMenu:]"
+ "-[SDBetaEnrollmentDaemon removeSeedEnrollmentCookie:]"
+ "-[SDBetaEnrollmentDaemon saveMDMConfiguration:withCompletion:]"
+ "-[SDBetaEnrollmentDaemon setupAssistant_enrollInProgramWithBetaEnrollmentToken:completion:]"
+ "-[SDBetaEnrollmentService _startListeningForProfileChanges]"
+ "-[SDBetaEnrollmentService _stopListeningForProfileChanges]"
+ "-[SDBetaEnrollmentService _verifyCurrentDevice]"
+ "-[SDBetaEnrollmentService canDeviceEnrollInBetaUpdates:completion:]"
+ "-[SDBetaEnrollmentService canFileFeedbackOnDevice:completion:]"
+ "-[SDBetaEnrollmentService configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:completion:]"
+ "-[SDBetaEnrollmentService deleteSeedingAppleAccountForDevice:completion:]"
+ "-[SDBetaEnrollmentService enrollDevice:inProgram:completion:]"
+ "-[SDBetaEnrollmentService enrollInProgramWithToken:completion:]"
+ "-[SDBetaEnrollmentService enrolledBetaProgramForDevice:completion:]"
+ "-[SDBetaEnrollmentService getCurrentDevice:]"
+ "-[SDBetaEnrollmentService getCurrentPrimaryAppleIDForDevice:completion:]"
+ "-[SDBetaEnrollmentService getCurrentSeedingAppleIDForDevice:completion:]"
+ "-[SDBetaEnrollmentService invalidateDaemonCacheWithCompletion:]"
+ "-[SDBetaEnrollmentService isDeviceEnrolledInBetaProgram:completion:]"
+ "-[SDBetaEnrollmentService isDeviceUsingSeedingAppleID:completion:]"
+ "-[SDBetaEnrollmentService loadMDMConfigurationWithCompletion:]"
+ "-[SDBetaEnrollmentService queryProgramsForSystemAccountsWithPlatforms:completion:]"
+ "-[SDBetaEnrollmentService setAppleAccountIdentifierFromAlternateDSID:forDevice:completion:]"
+ "-[SDBetaEnrollmentService start]"
+ "-[SDBetaEnrollmentService unenrollDevice:completion:]"
+ "-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:completion:]"
+ "-[SDBetaManager validateBetaEnrollmentTokens:errorHandler:]"
+ "<SDBetaProgram:\n\tTitle: %@\n\tID: %ld\n\tAssetAudience: %@\n\tPlatform: %@\n\tBuildPrefix: %@\n\tAccountID: %ld\n\tBetaEnrollmentTokens: %@\n>"
+ "@40@0:8@16Q24B32B36"
+ "A client [%ld] tried to use Seeding.framework but is not entitled."
+ "B32@0:8@16@?24"
+ "B32@0:8Q16@24"
+ "Currently enrolled MDM program [%lu: %{public}@] not in offered in new configuration. Will unenroll."
+ "Currently enrolled in MDM program with BETs [%{public}@]"
+ "Failed to get remote object proxy to betaEnrollment remote process: %{public}@."
+ "Failed to get synchronous remote object proxy: %{public}@"
+ "Failed to save configuration with updated date: [%{public}@]"
+ "Found [%lu] invalid BETs"
+ "Found a betaEnrollmentProxy that does not conform to SDBetaEnrollmentServiceInterface"
+ "Found a remoteObjectProxy that does not conform to SDBetaEnrollmentServiceInterface"
+ "Given BETs fetched zero programs. (All BETs are invalid)"
+ "Ignoring offerTokens because it is not valid for this policy"
+ "Ignoring requireToken because it is not valid for this policy"
+ "Invalid BET: [%{public}@]"
+ "Invalid Beta Enrollment Token."
+ "InvalidTokens"
+ "Loaded MDM configuration: [%{public}s] with [%lu] tokens. Config date [%{public}@]"
+ "MDM configuration AlwaysOff. Returning empty set"
+ "MDM configuration invalidated local cache created on [%{public}@]. MDM applied date [%{public}@]"
+ "MDM configuration is missing configuration date. Will set to now and save it."
+ "Not saving programs at this time"
+ "Query programs endpoint failed with [%ld]"
+ "SDBetaEnrollmentClientInterface"
+ "SDBetaEnrollmentDaemon"
+ "SDBetaEnrollmentDaemonInterface"
+ "SDBetaEnrollmentDaemonProxy"
+ "SDBetaEnrollmentService"
+ "SDBetaEnrollmentServiceInterface"
+ "SDBetaEnrollmentServiceProxy"
+ "SDMDMConfiguratorImplementation"
+ "Saving programs"
+ "T@\"NSDate\",&,V_configurationDate"
+ "T@\"NSSet\",&,V_betaEnrollmentTokens"
+ "[%{public}s called with zero tokens"
+ "[%{public}s called with zero tokens. Will proceed"
+ "[%{public}s should be called on launch daemon instead"
+ "_betaEnrollmentTokens"
+ "_configurationDate"
+ "_finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:completion:"
+ "activate"
+ "addObjectsFromArray:"
+ "betaEnrollmentProxyObjectWithCompletion:"
+ "betaEnrollmentTokens"
+ "betaEnrollmentTokens -> in launch daemon"
+ "betaEnrollmentTokens -> launch daemon"
+ "cachePrograms:forPlatforms:"
+ "com.apple.betaenrollment.verify"
+ "com.apple.seeding.daemon.entitlement"
+ "com.apple.seeding.daemon.error"
+ "configurationDate"
+ "containsValueForKey:"
+ "daemon-api"
+ "distantPast"
+ "initWithDictionary:"
+ "initWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:betaEnrollmentTokens:"
+ "intersectsSet:"
+ "isCacheValidForPlatforms:withMDMConfigurationDate:"
+ "isEqualToDate:"
+ "isMissingConfigurationDate"
+ "loadMDMConfigurationWithError -> in launch daemon"
+ "loadMDMConfigurationWithError -> launch daemon"
+ "minusSet:"
+ "parseProgramsResponse:platforms:shouldCache:skipsBuildMatching:"
+ "saveMDMConfiguration -> launch daemon"
+ "saveMDMConfiguration: in launch daemon"
+ "setBetaEnrollmentTokens:"
+ "setConfigurationDate:"
+ "setWithCapacity:"
+ "setWithSet:"
+ "shouldReturnBecauseOfInvalidTokens:andReportErrorWith:"
+ "userInfo"
+ "v24@?0@\"<SDBetaEnrollmentServiceInterface>\"8@\"NSError\"16"
+ "v48@0:8@\"NSSet\"16@\"NSString\"24q32@?<v@?@\"NSError\">40"
+ "v52@0:8Q16@24@32B40@?44"
+ "validateBetaEnrollmentTokens:errorHandler:"
+ "xpc connection interrupted"
+ "xpc connection invalidated"
- "+[SDMDMConfigurator enrollInProgramWithMDMToken:completion:]"
- "+[SDMDMConfiguratorDaemon conditionallyUnenrollIfNotMatchingOfferedTokensWithConfig:userIdentifier:]"
- "+[SDMDMConfiguratorDaemon enrollWithRequireProgramToken:userIdentifier:]"
- "-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:completion:]"
- "-[SDDaemon _startListeningForProfileChanges]"
- "-[SDDaemon _stopListeningForProfileChanges]"
- "-[SDDaemon _verifyCurrentDevice]"
- "-[SDDaemon canDeviceEnrollInBetaUpdates:completion:]"
- "-[SDDaemon canFileFeedbackOnDevice:completion:]"
- "-[SDDaemon configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:completion:]"
- "-[SDDaemon deleteSeedingAppleAccountForDevice:completion:]"
- "-[SDDaemon enrollDevice:inProgram:completion:]"
- "-[SDDaemon enrollInProgramWithToken:completion:]"
- "-[SDDaemon enrolledBetaProgramForDevice:completion:]"
- "-[SDDaemon getCurrentDevice:]"
- "-[SDDaemon getCurrentPrimaryAppleIDForDevice:completion:]"
- "-[SDDaemon getCurrentSeedingAppleIDForDevice:completion:]"
- "-[SDDaemon invalidateDaemonCacheWithCompletion:]"
- "-[SDDaemon isDeviceEnrolledInBetaProgram:completion:]"
- "-[SDDaemon isDeviceUsingSeedingAppleID:completion:]"
- "-[SDDaemon loadMDMConfigurationWithCompletion:]"
- "-[SDDaemon queryProgramsForSystemAccountsWithPlatforms:completion:]"
- "-[SDDaemon setAppleAccountIdentifierFromAlternateDSID:forDevice:completion:]"
- "-[SDDaemon start]"
- "-[SDDaemon unenrollDevice:completion:]"
- "<SDBetaProgram:\n\tTitle: %@\n\tID: %ld\n\tAssetAudience: %@\n\tPlatform: %@\n\tBuildPrefix: %@\n\tAccountID: %ld\n\tBetaEnrollmentToken: %@\n>"
- "@32@0:8@16Q24"
- "Currently enrolled MDM program [%lu: %{public}@] not in offered set. Will unenroll."
- "Currently enrolled in MDM program with token [%{public}@]"
- "Failed to get remote object proxy to betaenrollmentd: %{public}@."
- "Found a betaenrollmentdProxy that does not conform to SDDaemonXPCServer"
- "Found a remoteObjectProxy that does not conform to SDDaemonXPCServer"
- "Loaded MDM configuration: [%{public}s] with [%lu] tokens"
- "Returning cached programs."
- "SDBetaEnrollmentHelper"
- "SDBetaEnrollmentHelperDaemon"
- "SDBetaEnrollmentHelperDaemonInterface"
- "SDDaemon"
- "SDDaemonClient"
- "SDDaemonCommon"
- "SDDaemonXPCClient"
- "SDDaemonXPCServer"
- "SDMDMConfiguratorDaemon"
- "T@\"NSString\",&,V_betaEnrollmentToken"
- "Unexpected nil beta enrollment token for program %lu"
- "_allowListedXPCClientInterface"
- "_allowListedXPCServerInterface"
- "_betaEnrollmentToken"
- "_finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:completion:"
- "addEntriesFromDictionary:"
- "appleIDHeadersForRequest:"
- "betaEnrollmentTokens -> helper"
- "betaEnrollmentTokens -> in helper"
- "betaProgramWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:betaEnrollmentToken:"
- "betaenrollmentdProxyObjectWithCompletion:"
- "com.apple.betaenrollmentd.verify"
- "com.apple.seeding.daemon-client"
- "enrollInProgramWithMDMToken:completion:"
- "fbahelperd"
- "fbahelperd connection interrupted"
- "fbahelperd connection invalidated"
- "handleResponse:forRequest:shouldRetry:"
- "hasDeviceManagementRestiction"
- "helperd-client"
- "initWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:betaEnrollmentToken:"
- "loadMDMConfigurationWithError -> helper"
- "loadMDMConfigurationWithError -> in helper"
- "saveMDMConfiguration -> helper"
- "saveMDMConfiguration -> in helper"
- "savePrograms:forPlatforms:"
- "saveResponse:platforms:"
- "setBetaEnrollmentToken:"
- "v24@?0@\"<SDDaemonXPCServer>\"8@\"NSError\"16"
- "v48@0:8@\"NSSet\"16@\"NSString\"24q32@?<v@?q>40"
- "v48@0:8Q16@24@32@?40"

```
