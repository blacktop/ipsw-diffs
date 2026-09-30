## Seeding

> `/System/Library/PrivateFrameworks/Seeding.framework/Seeding`

```diff

-117.0.0.0.0
-  __TEXT.__text: 0x1f1e4
-  __TEXT.__auth_stubs: 0x710
-  __TEXT.__objc_methlist: 0x168c
+119.0.0.0.0
+  __TEXT.__text: 0x1f4c0
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__objc_methlist: 0x16a4
   __TEXT.__const: 0x100
   __TEXT.__gcc_except_tab: 0x5dc
-  __TEXT.__cstring: 0x2171
+  __TEXT.__cstring: 0x21cb
   __TEXT.__oslogstring: 0x3145
-  __TEXT.__unwind_info: 0x840
-  __TEXT.__objc_classname: 0x22d
-  __TEXT.__objc_methname: 0x3dba
-  __TEXT.__objc_methtype: 0x79c
-  __TEXT.__objc_stubs: 0x3ae0
-  __DATA_CONST.__got: 0x288
+  __TEXT.__unwind_info: 0x850
+  __TEXT.__objc_classname: 0x23d
+  __TEXT.__objc_methname: 0x3f55
+  __TEXT.__objc_methtype: 0x812
+  __TEXT.__objc_stubs: 0x3be0
+  __DATA_CONST.__got: 0x2a0
   __DATA_CONST.__const: 0xce8
-  __DATA_CONST.__objc_classlist: 0xb0
+  __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1120
+  __DATA_CONST.__objc_selrefs: 0x1168
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x398
+  __AUTH_CONST.__auth_got: 0x3a0
   __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x1a40
-  __AUTH_CONST.__objc_const: 0x2ba0
+  __AUTH_CONST.__cfstring: 0x1a80
+  __AUTH_CONST.__objc_const: 0x2c30
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0xa0
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0xc0
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x70
-  __DATA_DIRTY.__objc_data: 0x640
+  __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__bss: 0xc8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 39FAE4FB-A843-3C9D-B401-5FEDF0D4EAEA
-  Functions: 696
-  Symbols:   2535
-  CStrings:  1582
+  UUID: AB67381B-8EE3-3A09-8B85-1D791A9E09A4
+  Functions: 697
+  Symbols:   2553
+  CStrings:  1600
 
Symbols:
+ +[SDLanguageUtils languageHeaderCode]
+ +[SDMDMConfiguratorImplementation configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:userIdentifier:language:completion:]
+ +[SDMDMConfiguratorImplementation configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:userIdentifier:language:completion:].cold.1
+ +[SDMDMConfiguratorImplementation enrollWithRequireProgramToken:language:userIdentifier:]
+ +[SDMDMConfiguratorImplementation enrollWithRequireProgramToken:language:userIdentifier:].cold.1
+ -[SDBetaEnrollmentService configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:language:completion:]
+ -[SDBetaEnrollmentService enrollInProgramWithToken:language:completion:]
+ -[SDBetaEnrollmentService queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:language:completion:]
+ -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:language:completion:]
+ -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:language:completion:].cold.1
+ -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:language:completion:].cold.2
+ -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:language:completion:]
+ -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:language:completion:].cold.1
+ -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:language:completion:].cold.2
+ -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:language:completion:].cold.3
+ -[SDBetaManager enrollInProgramWithToken:userIdentifier:language:completion:]
+ -[SDBetaManager enrollInProgramWithToken:userIdentifier:language:shouldSaveToken:completion:]
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_SDLanguageUtils
+ _OBJC_METACLASS_$_SDLanguageUtils
+ __OBJC_$_CLASS_METHODS_SDLanguageUtils
+ __OBJC_CLASS_RO_$_SDLanguageUtils
+ __OBJC_METACLASS_RO_$_SDLanguageUtils
+ ___109-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:language:completion:]_block_invoke
+ ___109-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:language:completion:]_block_invoke.358
+ ___109-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:language:completion:]_block_invoke.358.cold.1
+ ___109-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:language:completion:]_block_invoke.cold.1
+ ___116-[SDBetaEnrollmentService configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:language:completion:]_block_invoke
+ ___118-[SDBetaEnrollmentService queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:language:completion:]_block_invoke
+ ___168-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:language:completion:]_block_invoke
+ ___168-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:language:completion:]_block_invoke.cold.1
+ ___168-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:language:completion:]_block_invoke.cold.2
+ ___168-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:language:completion:]_block_invoke.cold.3
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.605
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.606
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.606.cold.1
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.606.cold.2
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.607
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.607.cold.1
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.607.cold.2
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.607.cold.3
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.608
+ ___64-[SDBetaManager enrollDevice:withEnrollmentMetadata:completion:]_block_invoke.412
+ ___72-[SDBetaEnrollmentService enrollInProgramWithToken:language:completion:]_block_invoke
+ ___73-[SDBetaManager _saveAppleAccountIdentifierWithAlternateDSID:completion:]_block_invoke.462
+ ___89+[SDMDMConfiguratorImplementation enrollWithRequireProgramToken:language:userIdentifier:]_block_invoke
+ ___93-[SDBetaManager enrollInProgramWithToken:userIdentifier:language:shouldSaveToken:completion:]_block_invoke
+ ___93-[SDBetaManager enrollInProgramWithToken:userIdentifier:language:shouldSaveToken:completion:]_block_invoke.cold.1
+ ___93-[SDBetaManager enrollInProgramWithToken:userIdentifier:language:shouldSaveToken:completion:]_block_invoke.cold.2
+ ___93-[SDBetaManager enrollInProgramWithToken:userIdentifier:language:shouldSaveToken:completion:]_block_invoke.cold.3
+ ___block_descriptor_83_e8_32s40s48s56bs64r_e5_v8?0lr64l8s56l8s32l8s40l8s48l8
+ ___block_literal_global.134
+ ___block_literal_global.178
+ _objc_msgSend$_finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:language:completion:
+ _objc_msgSend$_queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:language:completion:
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:userIdentifier:language:completion:
+ _objc_msgSend$enrollInProgramWithToken:language:completion:
+ _objc_msgSend$enrollInProgramWithToken:userIdentifier:language:completion:
+ _objc_msgSend$enrollInProgramWithToken:userIdentifier:language:shouldSaveToken:completion:
+ _objc_msgSend$enrollWithRequireProgramToken:language:userIdentifier:
+ _objc_msgSend$languageHeaderCode
+ _objc_msgSend$minimizedLanguagesFromLanguages:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$preferredLanguages
+ _objc_msgSend$queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:language:completion:
+ _objc_msgSend$stringWithString:
+ _objc_retain_x6
- +[SDMDMConfiguratorImplementation configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:userIdentifier:completion:]
- +[SDMDMConfiguratorImplementation configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:userIdentifier:completion:].cold.1
- +[SDMDMConfiguratorImplementation enrollWithRequireProgramToken:userIdentifier:]
- +[SDMDMConfiguratorImplementation enrollWithRequireProgramToken:userIdentifier:].cold.1
- -[SDBetaEnrollmentService configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:completion:]
- -[SDBetaEnrollmentService enrollInProgramWithToken:completion:]
- -[SDBetaEnrollmentService queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]
- -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:completion:]
- -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:completion:].cold.1
- -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:completion:].cold.2
- -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]
- -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:].cold.1
- -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:].cold.2
- -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:].cold.3
- -[SDBetaManager enrollInProgramWithToken:userIdentifier:completion:]
- -[SDBetaManager enrollInProgramWithToken:userIdentifier:shouldSaveToken:completion:]
- ___100-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]_block_invoke
- ___100-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]_block_invoke.355
- ___100-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]_block_invoke.355.cold.1
- ___100-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]_block_invoke.cold.1
- ___107-[SDBetaEnrollmentService configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:completion:]_block_invoke
- ___109-[SDBetaEnrollmentService queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]_block_invoke
- ___159-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:completion:]_block_invoke
- ___159-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:completion:]_block_invoke.cold.1
- ___159-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:completion:]_block_invoke.cold.2
- ___159-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:completion:]_block_invoke.cold.3
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.597
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.598
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.598.cold.1
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.598.cold.2
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.599
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.599.cold.1
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.599.cold.2
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.599.cold.3
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.600
- ___63-[SDBetaEnrollmentService enrollInProgramWithToken:completion:]_block_invoke
- ___64-[SDBetaManager enrollDevice:withEnrollmentMetadata:completion:]_block_invoke.406
- ___73-[SDBetaManager _saveAppleAccountIdentifierWithAlternateDSID:completion:]_block_invoke.456
- ___80+[SDMDMConfiguratorImplementation enrollWithRequireProgramToken:userIdentifier:]_block_invoke
- ___84-[SDBetaManager enrollInProgramWithToken:userIdentifier:shouldSaveToken:completion:]_block_invoke
- ___84-[SDBetaManager enrollInProgramWithToken:userIdentifier:shouldSaveToken:completion:]_block_invoke.cold.1
- ___84-[SDBetaManager enrollInProgramWithToken:userIdentifier:shouldSaveToken:completion:]_block_invoke.cold.2
- ___84-[SDBetaManager enrollInProgramWithToken:userIdentifier:shouldSaveToken:completion:]_block_invoke.cold.3
- ___block_descriptor_75_e8_32s40s48bs56r_e5_v8?0lr56l8s48l8s32l8s40l8
- ___block_literal_global.130
- ___block_literal_global.176
- _objc_msgSend$_finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:completion:
- _objc_msgSend$_queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:
- _objc_msgSend$configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:userIdentifier:completion:
- _objc_msgSend$enrollInProgramWithToken:userIdentifier:completion:
- _objc_msgSend$enrollInProgramWithToken:userIdentifier:shouldSaveToken:completion:
- _objc_msgSend$enrollWithRequireProgramToken:userIdentifier:
CStrings:
+ "+[SDMDMConfiguratorImplementation enrollWithRequireProgramToken:language:userIdentifier:]"
+ ",%@;q=0.%u"
+ "-[SDBetaEnrollmentService configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:language:completion:]"
+ "-[SDBetaEnrollmentService enrollInProgramWithToken:language:completion:]"
+ "-[SDBetaEnrollmentService queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:language:completion:]"
+ "-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:language:completion:]"
+ "-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:language:completion:]"
+ "-[SDBetaManager enrollInProgramWithToken:userIdentifier:language:shouldSaveToken:completion:]"
+ "Accept-Language"
+ "SDLanguageUtils"
+ "_finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:language:completion:"
+ "_queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:language:completion:"
+ "appendFormat:"
+ "configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:language:completion:"
+ "configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:userIdentifier:language:completion:"
+ "enrollInProgramWithToken:language:completion:"
+ "enrollInProgramWithToken:userIdentifier:language:completion:"
+ "enrollInProgramWithToken:userIdentifier:language:shouldSaveToken:completion:"
+ "enrollWithRequireProgramToken:language:userIdentifier:"
+ "languageHeaderCode"
+ "minimizedLanguagesFromLanguages:"
+ "objectAtIndexedSubscript:"
+ "preferredLanguages"
+ "q40@0:8@16@24@32"
+ "queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:language:completion:"
+ "stringWithString:"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?q>32"
+ "v44@0:8Q16B24@\"NSString\"28@?<v@?@\"NSArray\"q>36"
+ "v44@0:8Q16B24@28@?36"
+ "v48@0:8@16@24@32@?40"
+ "v52@0:8@16@24@32B40@?44"
+ "v64@0:8@16@24q32@40@48@?56"
+ "v64@0:8Q16@24@32B40B44@48@?56"
- "+[SDMDMConfiguratorImplementation enrollWithRequireProgramToken:userIdentifier:]"
- "-[SDBetaEnrollmentService configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:completion:]"
- "-[SDBetaEnrollmentService enrollInProgramWithToken:completion:]"
- "-[SDBetaEnrollmentService queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]"
- "-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:completion:]"
- "-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]"
- "-[SDBetaManager enrollInProgramWithToken:userIdentifier:shouldSaveToken:completion:]"
- "_finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:completion:"
- "_queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:"
- "configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:userIdentifier:completion:"
- "enrollInProgramWithToken:userIdentifier:completion:"
- "enrollInProgramWithToken:userIdentifier:shouldSaveToken:completion:"
- "enrollWithRequireProgramToken:userIdentifier:"
- "v32@0:8@\"NSString\"16@?<v@?q>24"
- "v36@0:8Q16B24@?<v@?@\"NSArray\"q>28"
- "v44@0:8@16@24B32@?36"
- "v56@0:8Q16@24@32B40B44@?48"

```
