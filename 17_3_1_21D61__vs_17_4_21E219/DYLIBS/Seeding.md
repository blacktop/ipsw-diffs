## Seeding

> `/System/Library/PrivateFrameworks/Seeding.framework/Seeding`

```diff

-90.0.0.0.0
-  __TEXT.__text: 0x19600
+93.0.0.0.0
+  __TEXT.__text: 0x1add4
   __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0x129c
+  __TEXT.__objc_methlist: 0x1370
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x350
-  __TEXT.__cstring: 0x16f0
-  __TEXT.__oslogstring: 0x25af
-  __TEXT.__unwind_info: 0x6c0
-  __TEXT.__objc_classname: 0x208
-  __TEXT.__objc_methname: 0x3644
-  __TEXT.__objc_methtype: 0x5dc
-  __TEXT.__objc_stubs: 0x34c0
+  __TEXT.__gcc_except_tab: 0x354
+  __TEXT.__cstring: 0x193b
+  __TEXT.__oslogstring: 0x2782
+  __TEXT.__unwind_info: 0x708
+  __TEXT.__objc_classname: 0x229
+  __TEXT.__objc_methname: 0x3900
+  __TEXT.__objc_methtype: 0x636
+  __TEXT.__objc_stubs: 0x3680
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x940
-  __DATA_CONST.__objc_classlist: 0xa8
+  __DATA_CONST.__const: 0x9c0
+  __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2ac8
-  __DATA_CONST.__objc_selrefs: 0xee8
+  __DATA_CONST.__objc_const: 0x2c18
+  __DATA_CONST.__objc_selrefs: 0xf70
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x1e0
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__cfstring: 0x15a0
-  __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__objc_const: 0x40
-  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__cfstring: 0x1800
+  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__objc_const: 0xd0
+  __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0x380
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x1d0
-  __DATA.__objc_superrefs: 0x40
-  __DATA.__objc_ivar: 0xb0
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0xb4
   __DATA.__data: 0x300
-  __DATA.__bss: 0x70
+  __DATA.__bss: 0x78
   __DATA_DIRTY.__const: 0x260
   __DATA_DIRTY.__objc_const: 0x870
   __DATA_DIRTY.__objc_data: 0x690
-  __DATA_DIRTY.__bss: 0xd0
+  __DATA_DIRTY.__bss: 0xd8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 613
-  Symbols:   2294
-  CStrings:  1177
+  Functions: 640
+  Symbols:   2376
+  CStrings:  1237
 
Symbols:
+ +[SDBetaProgram betaProgramWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:betaEnrollmentToken:]
+ +[SDDevice deriveMacDeviceClassForProductType:]
+ +[SDMDMConfigurator enrollInProgramWithMDMToken:completion:]
+ +[SDMDMConfigurator setupAssistant_enrollInProgramWithMDMToken:completion:]
+ +[SDPersistence betaEnrollmentTokens]
+ +[SDPersistence saveBetaEnrollmentTokens:]
+ -[SDBetaEnrollmentHelper remoteObjectProxyWithCompletion:]
+ -[SDBetaEnrollmentHelper setupAssistant_enrollInProgramWithBetaEnrollmentToken:completion:]
+ -[SDBetaEnrollmentHelperDaemon setupAssistant_enrollInProgramWithBetaEnrollmentToken:completion:]
+ -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:completion:]
+ -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:completion:].cold.1
+ -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:completion:].cold.2
+ -[SDBetaManager enrollInProgramWithToken:completion:]
+ -[SDBetaManager seedingAppleIDUsernameForCurrentDeviceWithCompletion:]
+ -[SDBetaProgram betaEnrollmentToken]
+ -[SDBetaProgram initWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:betaEnrollmentToken:]
+ -[SDBetaProgram isMDMProgram]
+ -[SDBetaProgram setBetaEnrollmentToken:]
+ -[SDDaemon enrollInProgramWithToken:completion:]
+ -[SDDaemonClient daemonRemoteObjectProxyWithCompletion:]
+ -[SDDaemonClient enrollInProgramWithToken:completion:]
+ -[SDDaemonClient seedingAppleIDUsernameForCurrentDevice:]
+ GCC_except_table20
+ GCC_except_table24
+ GCC_except_table28
+ GCC_except_table33
+ GCC_except_table41
+ GCC_except_table67
+ GCC_except_table72
+ GCC_except_table86
+ _NilIfNSNull
+ _OBJC_CLASS_$_SDMDMConfigurator
+ _OBJC_CLASS_$_SDPersistence
+ _OBJC_CLASS_$_UTType
+ _OBJC_IVAR_$_SDBetaProgram._betaEnrollmentToken
+ _OBJC_METACLASS_$_SDMDMConfigurator
+ _OBJC_METACLASS_$_SDPersistence
+ _OUTLINED_FUNCTION_13
+ _SDBetaEnrollmentTokensKey
+ _SDMDMConfiguratorErrorWithType
+ _SDStringForPlatform
+ __OBJC_$_CLASS_METHODS_SDMDMConfigurator
+ __OBJC_$_CLASS_METHODS_SDPersistence
+ __OBJC_CLASS_RO_$_SDMDMConfigurator
+ __OBJC_CLASS_RO_$_SDPersistence
+ __OBJC_METACLASS_RO_$_SDMDMConfigurator
+ __OBJC_METACLASS_RO_$_SDPersistence
+ ___113-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:completion:]_block_invoke
+ ___113-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:completion:]_block_invoke.cold.1
+ ___113-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:completion:]_block_invoke.cold.2
+ ___113-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:completion:]_block_invoke.cold.3
+ ___41-[SDBetaEnrollmentHelper connectToDaemon]_block_invoke.56
+ ___41-[SDBetaEnrollmentHelper connectToDaemon]_block_invoke.56.cold.1
+ ___53-[SDBetaManager enrollInProgramWithToken:completion:]_block_invoke
+ ___53-[SDBetaManager enrollInProgramWithToken:completion:]_block_invoke.cold.1
+ ___53-[SDBetaManager enrollInProgramWithToken:completion:]_block_invoke.cold.2
+ ___53-[SDBetaManager enrollInProgramWithToken:completion:]_block_invoke.cold.3
+ ___54-[SDDaemonClient enrollInProgramWithToken:completion:]_block_invoke
+ ___56-[SDDaemonClient daemonRemoteObjectProxyWithCompletion:]_block_invoke
+ ___56-[SDDaemonClient daemonRemoteObjectProxyWithCompletion:]_block_invoke.cold.1
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.539
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.540
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.540.cold.1
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.540.cold.2
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.541
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.541.cold.1
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.541.cold.2
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.541.cold.3
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.542
+ ___57-[SDDaemonClient seedingAppleIDUsernameForCurrentDevice:]_block_invoke
+ ___57-[SDDaemonClient seedingAppleIDUsernameForCurrentDevice:]_block_invoke_2
+ ___58-[SDBetaEnrollmentHelper remoteObjectProxyWithCompletion:]_block_invoke
+ ___58-[SDBetaEnrollmentHelper remoteObjectProxyWithCompletion:]_block_invoke.cold.1
+ ___64-[SDBetaManager enrollDevice:withEnrollmentMetadata:completion:]_block_invoke.357
+ ___67-[SDBetaEnrollmentHelperDaemon listener:shouldAcceptNewConnection:]_block_invoke.54
+ ___73-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:]_block_invoke.305
+ ___73-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:]_block_invoke.305.cold.1
+ ___73-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:]_block_invoke.305.cold.2
+ ___73-[SDBetaManager _saveAppleAccountIdentifierWithAlternateDSID:completion:]_block_invoke.404
+ ___97-[SDBetaEnrollmentHelperDaemon setupAssistant_enrollInProgramWithBetaEnrollmentToken:completion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e18_v16?0"NSString"8ls32l8
+ ___block_descriptor_40_e8_32bs_e8_v16?0q8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e20_v24?0"NSArray"8q16ls32l8s40l8
+ ___block_literal_global.165
+ ___block_literal_global.59
+ ___block_literal_global.62
+ ___block_literal_global.88
+ ___block_literal_global.95
+ _objc_msgSend$_finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:completion:
+ _objc_msgSend$_typeWithDeviceModelCode:
+ _objc_msgSend$allObjects
+ _objc_msgSend$arrayForKey:
+ _objc_msgSend$betaEnrollmentToken
+ _objc_msgSend$betaEnrollmentTokens
+ _objc_msgSend$betaProgramWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:betaEnrollmentToken:
+ _objc_msgSend$daemonRemoteObjectProxyWithCompletion:
+ _objc_msgSend$deriveMacDeviceClassForProductType:
+ _objc_msgSend$enrollInProgramWithToken:completion:
+ _objc_msgSend$initWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:betaEnrollmentToken:
+ _objc_msgSend$isMDMProgram
+ _objc_msgSend$remoteObjectProxyWithCompletion:
+ _objc_msgSend$saveBetaEnrollmentTokens:
+ _objc_msgSend$seedingAppleIDUsernameForCurrentDevice:
+ _objc_msgSend$setBetaEnrollmentToken:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$setupAssistant_enrollInProgramWithBetaEnrollmentToken:completion:
- +[SDBetaProgram betaProgramWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:]
- +[SDBetaProgram nilIfNSNull:]
- +[SDProfileUtilities removeSeedingProfile].cold.1
- -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:completion:]
- -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:completion:].cold.1
- -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:completion:].cold.2
- -[SDBetaManager _unenrollFromBetaProgramWithUserIdentifier:].cold.2
- -[SDBetaProgram initWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:]
- GCC_except_table12
- GCC_except_table19
- GCC_except_table21
- GCC_except_table23
- GCC_except_table27
- GCC_except_table29
- GCC_except_table37
- GCC_except_table68
- GCC_except_table73
- GCC_except_table85
- ___41-[SDBetaEnrollmentHelper connectToDaemon]_block_invoke.52
- ___41-[SDBetaEnrollmentHelper connectToDaemon]_block_invoke.52.cold.1
- ___41-[SDDaemonClient daemonRemoteObjectProxy]_block_invoke
- ___41-[SDDaemonClient daemonRemoteObjectProxy]_block_invoke.cold.1
- ___43-[SDBetaEnrollmentHelper remoteObjectProxy]_block_invoke
- ___43-[SDBetaEnrollmentHelper remoteObjectProxy]_block_invoke.cold.1
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.505
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.506
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.506.cold.1
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.506.cold.2
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.507
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.507.cold.1
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.507.cold.2
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.507.cold.3
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.508
- ___64-[SDBetaManager enrollDevice:withEnrollmentMetadata:completion:]_block_invoke.326
- ___67-[SDBetaEnrollmentHelperDaemon listener:shouldAcceptNewConnection:]_block_invoke.50
- ___73-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:]_block_invoke.281
- ___73-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:]_block_invoke.281.cold.1
- ___73-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:]_block_invoke.281.cold.2
- ___73-[SDBetaManager _saveAppleAccountIdentifierWithAlternateDSID:completion:]_block_invoke.372
- ___92-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:completion:]_block_invoke
- ___92-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:completion:]_block_invoke.cold.1
- ___92-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:completion:]_block_invoke.cold.2
- ___92-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:completion:]_block_invoke.cold.3
- ___block_literal_global.162
- ___block_literal_global.515
- ___block_literal_global.55
- ___block_literal_global.57
- ___block_literal_global.60
- ___block_literal_global.8
- ___block_literal_global.84
- ___block_literal_global.91
- _objc_msgSend$_finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:completion:
- _objc_msgSend$betaProgramWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:
- _objc_msgSend$initWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:
- _objc_msgSend$nilIfNSNull:
CStrings:
+ "\x11\x15\x11\x11"
+ "+[SDMDMConfigurator enrollInProgramWithMDMToken:completion:]"
+ "+[SDMDMConfigurator setupAssistant_enrollInProgramWithMDMToken:completion:]"
+ "-[SDBetaManager enrollInProgramWithToken:completion:]"
+ "-[SDBetaManager seedingAppleIDUsernameForCurrentDeviceWithCompletion:]"
+ "-[SDDaemon enrollInProgramWithToken:completion:]"
+ "<SDBetaProgram:\n\tTitle: %@\n\tID: %ld\n\tAssetAudience: %@\n\tPlatform: %@\n\tBuildPrefix: %@\n\tAccountID: %ld\n\tBetaEnrollmentToken: %@\n>"
+ "<SDBetaProgram: %@, ID: %ld MDM? %i>"
+ "@112@0:8q16@24@32@40@48@56@64@72Q80@88q96@104"
+ "@24@0:8@?16"
+ "Accept"
+ "BetaEnrollmentToken"
+ "Catalog [%lu] for token [%{private}@] has platform [%{public}@] and does not match this device. Will not enroll"
+ "EnrollmentTokens"
+ "Failed to get remote object proxy to root helper: %{public}@."
+ "Failed to get synchronous remote object proxy to root helper: %{public}@."
+ "JSON response: %{private}@"
+ "Loaded program [%{public}@ - %lu] assetAudience: [%{public}@]"
+ "Mac"
+ "MacStudio"
+ "More than one program retuned for token [%{private}@]. Will use first"
+ "No Beta Enrollment Tokens saved"
+ "No Mac product mapping for [%{public}@]"
+ "No programs found for token [%{private}@]"
+ "Querying programs"
+ "Querying programs with [%ld] Beta Enrollment Tokens"
+ "SDMDMConfigurator"
+ "SDPersistence"
+ "T@\"NSString\",&,N,V_betaEnrollmentToken"
+ "T@\"NSString\",?,R,C"
+ "[%{public}s token [%{private}@]"
+ "_betaEnrollmentToken"
+ "_finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:completion:"
+ "_typeWithDeviceModelCode:"
+ "allObjects"
+ "arrayForKey:"
+ "betaEnrollmentToken"
+ "betaEnrollmentTokens"
+ "betaProgramWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:betaEnrollmentToken:"
+ "beta_enrollment_tokens"
+ "com.apple."
+ "com.apple.seeding.mdm-configurator"
+ "daemonRemoteObjectProxyWithCompletion:"
+ "deriveMacDeviceClassForProductType:"
+ "enrollInProgramWithMDMToken:completion:"
+ "enrollInProgramWithToken:completion:"
+ "imac"
+ "initWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:betaEnrollmentToken:"
+ "isMDMProgram"
+ "macbook"
+ "macbookair"
+ "macbookpro"
+ "macmini"
+ "macpro"
+ "macstudio"
+ "mdm"
+ "provided_by"
+ "remoteObjectProxyWithCompletion:"
+ "saveBetaEnrollmentTokens:"
+ "seedingAppleIDUsernameForCurrentDevice:"
+ "seedingAppleIDUsernameForCurrentDeviceWithCompletion:"
+ "setBetaEnrollmentToken:"
+ "setWithArray:"
+ "setupAssistant_enrollInProgramWithBetaEnrollmentToken:completion:"
+ "setupAssistant_enrollInProgramWithMDMToken:completion:"
+ "type"
+ "v16@?0q8"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?q>24"
+ "v48@0:8Q16@24@32@?40"
- "\x11\x15\x11"
- "<SDBetaProgram:\n\tTitle: %@\n\tID: %ld\n\tAssetAudience: %@\n\tPlatform: %@\n\tBuildPrefix: %@\n\tAccountID: %ld\n>"
- "<SDBetaProgram: %@, ID: %ld>"
- "@104@0:8q16@24@32@40@48@56@64@72Q80@88q96"
- "Failed to get remote object proxy to helperd: %{public}@."
- "Failed to get synchronous remote object proxy to helperd: %{public}@."
- "JSON response:   %{public}@"
- "_finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:completion:"
- "betaProgramWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:"
- "initWithID:title:program:catalog:assetUpdate:assetBrain:assetAudience:legalDocs:platform:buildPrefix:accountID:"
- "nilIfNSNull:"
- "v40@0:8Q16@24@?32"

```
