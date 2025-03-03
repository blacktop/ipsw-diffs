## Seeding

> `/System/Library/PrivateFrameworks/Seeding.framework/Seeding`

```diff

-107.0.0.0.0
-  __TEXT.__text: 0x1f8f4
+113.0.0.0.0
+  __TEXT.__text: 0x1eba4
   __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x15ac
-  __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x6a0
-  __TEXT.__cstring: 0x1edc
-  __TEXT.__oslogstring: 0x2e68
-  __TEXT.__unwind_info: 0x8a8
-  __TEXT.__objc_classname: 0x256
-  __TEXT.__objc_methname: 0x3eba
-  __TEXT.__objc_methtype: 0x7f9
-  __TEXT.__objc_stubs: 0x3b20
+  __TEXT.__objc_methlist: 0x166c
+  __TEXT.__const: 0x100
+  __TEXT.__gcc_except_tab: 0x5d0
+  __TEXT.__cstring: 0x20c1
+  __TEXT.__oslogstring: 0x2fe7
+  __TEXT.__unwind_info: 0x818
+  __TEXT.__objc_classname: 0x22d
+  __TEXT.__objc_methname: 0x3d1b
+  __TEXT.__objc_methtype: 0x784
+  __TEXT.__objc_stubs: 0x3ac0
   __DATA_CONST.__got: 0x288
-  __DATA_CONST.__const: 0xc70
-  __DATA_CONST.__objc_classlist: 0xc8
+  __DATA_CONST.__const: 0xc40
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10c0
-  __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x48
+  __DATA_CONST.__objc_selrefs: 0x1110
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x390
-  __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x19a0
-  __AUTH_CONST.__objc_const: 0x3bd0
+  __AUTH_CONST.__const: 0x340
+  __AUTH_CONST.__cfstring: 0x1a20
+  __AUTH_CONST.__objc_const: 0x2ba0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_ivar: 0xc4
-  __DATA.__data: 0x300
-  __DATA.__bss: 0x80
-  __DATA_DIRTY.__objc_data: 0x7d0
-  __DATA_DIRTY.__bss: 0xe8
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0xc0
+  __DATA.__data: 0x2a0
+  __DATA.__bss: 0x70
+  __DATA_DIRTY.__objc_data: 0x640
+  __DATA_DIRTY.__bss: 0xc8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 723
-  Symbols:   1005
-  CStrings:  1379
+  Functions: 690
+  Symbols:   966
+  CStrings:  1370
 
Symbols:
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_SDBetaEnrollmentService
+ _OBJC_CLASS_$_SDBetaEnrollmentServiceProxy
+ _OBJC_CLASS_$_SDMDMConfiguratorImplementation
+ _OBJC_METACLASS_$_SDBetaEnrollmentService
+ _OBJC_METACLASS_$_SDBetaEnrollmentServiceProxy
+ _OBJC_METACLASS_$_SDMDMConfiguratorImplementation
+ _SDBESEntitlementName
+ _SDBESMachServiceName
+ _SDDaemonMachService
+ _SDDaemonMachServiceEntitlement
+ _SDDaemonMachServiceOldEntitlement
+ _SDMDMConfiguratorErrorAddInvalidTokens
+ __allowListedXPCClientInterface
+ __allowListedXPCServerInterface
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
- _SDBetaEnrollmentHelperDaemonMachService
- _SDBetaEnrollmentHelperDaemonMachServiceEntitlement
- _SDHelperDaemonInterface
- _SDMachServiceName
CStrings:
+ "+[SDMDMConfiguratorImplementation conditionallyUnenrollIfNotMatchingOfferedTokensWithConfig:userIdentifier:]"
+ "+[SDMDMConfiguratorImplementation enrollWithRequireProgramToken:userIdentifier:]"
+ "+[SDMDMConfiguratorImplementation shouldReturnBecauseOfInvalidTokens:andReportErrorWith:]"
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
+ "SDBetaEnrollmentService"
+ "SDBetaEnrollmentServiceInterface"
+ "SDBetaEnrollmentServiceProxy"
+ "SDMDMConfiguratorImplementation"
+ "Saving programs"
+ "T@\"NSDate\",&,V_configurationDate"
+ "T@\"NSSet\",&,V_betaEnrollmentTokens"
+ "[%{public}s called with zero tokens"
+ "[%{public}s called with zero tokens. Will proceed"
+ "_betaEnrollmentTokens"
+ "_configurationDate"
+ "_finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:completion:"
+ "addObjectsFromArray:"
+ "betaEnrollmentProxyObjectWithCompletion:"
+ "betaEnrollmentTokens"
+ "cachePrograms:forPlatforms:"
+ "code"
+ "com.apple.betaenrollment.verify"
+ "com.apple.seeding.daemon.entitlement"
+ "com.apple.seeding.daemon.error"
+ "configurationDate"
+ "containsValueForKey:"
+ "distantPast"
+ "domain"
+ "initWithDictionary:"
+ "initWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:betaEnrollmentTokens:"
+ "intersectsSet:"
+ "isCacheValidForPlatforms:withMDMConfigurationDate:"
+ "isEqualToDate:"
+ "isMissingConfigurationDate"
+ "minusSet:"
+ "parseProgramsResponse:platforms:shouldCache:skipsBuildMatching:"
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
- "\x11"
- "+[SDMDMConfigurator setupAssistant_enrollInProgramWithMDMToken:completion:]"
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
- "@24@0:8@?16"
- "@32@0:8@16Q24"
- "Currently enrolled MDM program [%lu: %{public}@] not in offered set. Will unenroll."
- "Currently enrolled in MDM program with token [%{public}@]"
- "Deleting beta enrollment data"
- "Failed to get remote object proxy to betaenrollmentd: %{public}@."
- "Failed to get remote object proxy to root helper: %{public}@."
- "Failed to get synchronous remote object proxy to betaenrollmentd: %{public}@"
- "Failed to get synchronous remote object proxy to root helper: %{public}@."
- "Failed to remove Beta enrollment data"
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
- "T@\"NSXPCConnection\",&,V_connection"
- "Unexpected nil beta enrollment token for program %lu"
- "_allowListedXPCClientInterface"
- "_allowListedXPCServerInterface"
- "_betaEnrollmentToken"
- "_connection"
- "_finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:completion:"
- "addEntriesFromDictionary:"
- "addFBAHelpMenu:"
- "addFBASymlink:"
- "appleIDHeadersForRequest:"
- "betaProgramWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:betaEnrollmentToken:"
- "betaenrollmentd connection interrupted"
- "betaenrollmentd connection invalidated"
- "betaenrollmentdProxyObjectWithCompletion:"
- "com.apple.betaenrollmentd.verify"
- "com.apple.seeding.daemon-client"
- "connectToDaemon"
- "connection"
- "fbahelperd"
- "fbahelperd connection interrupted"
- "fbahelperd connection invalidated"
- "fetchBetaEnrollmentTokens:"
- "fetchBetaEnrollmentTokensWithError:"
- "handleResponse:forRequest:shouldRetry:"
- "hasDeviceManagementRestiction"
- "helperd-client"
- "initWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:betaEnrollmentToken:"
- "isPreReleaseInstallationAllowed"
- "isPreReleaseInstallationAllowed:"
- "remoteObjectProxy"
- "remoteObjectProxyWithCompletion:"
- "removeBetaEnrollmentData"
- "removeBetaEnrollmentData:"
- "removeFBAHelpMenu:"
- "removeSeedEnrollmentCookie:"
- "saveMDMConfiguration:withCompletion:"
- "saveMDMConfiguration:withError:"
- "savePrograms:forPlatforms:"
- "saveResponse:platforms:"
- "setBetaEnrollmentToken:"
- "setConnection:"
- "setupAssistant_enrollInProgramWithBetaEnrollmentToken:completion:"
- "setupAssistant_enrollInProgramWithMDMToken:completion:"
- "synchronousRemoteObjectProxy"
- "v16@?0@\"NSArray\"8"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?@\"NSArray\">16"
- "v24@0:8@?<v@?B>16"
- "v24@?0@\"<SDDaemonXPCServer>\"8@\"NSError\"16"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"SDMDMConfiguration\"16@?<v@?@\"NSError\">24"
- "v48@0:8@\"NSSet\"16@\"NSString\"24q32@?<v@?q>40"
- "v48@0:8Q16@24@32@?40"

```
