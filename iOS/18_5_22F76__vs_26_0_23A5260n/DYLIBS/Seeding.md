## Seeding

> `/System/Library/PrivateFrameworks/Seeding.framework/Seeding`

```diff

-113.0.0.0.0
-  __TEXT.__text: 0x1eba4
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x166c
+117.0.0.0.0
+  __TEXT.__text: 0x1f1e4
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_methlist: 0x168c
   __TEXT.__const: 0x100
-  __TEXT.__gcc_except_tab: 0x5d0
-  __TEXT.__cstring: 0x20c1
-  __TEXT.__oslogstring: 0x2fe7
-  __TEXT.__unwind_info: 0x818
+  __TEXT.__gcc_except_tab: 0x5dc
+  __TEXT.__cstring: 0x2171
+  __TEXT.__oslogstring: 0x3145
+  __TEXT.__unwind_info: 0x840
   __TEXT.__objc_classname: 0x22d
-  __TEXT.__objc_methname: 0x3d1b
-  __TEXT.__objc_methtype: 0x784
-  __TEXT.__objc_stubs: 0x3ac0
+  __TEXT.__objc_methname: 0x3dba
+  __TEXT.__objc_methtype: 0x79c
+  __TEXT.__objc_stubs: 0x3ae0
   __DATA_CONST.__got: 0x288
-  __DATA_CONST.__const: 0xc40
+  __DATA_CONST.__const: 0xce8
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1110
+  __DATA_CONST.__objc_selrefs: 0x1120
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x390
-  __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x1a20
+  __AUTH_CONST.__auth_got: 0x398
+  __AUTH_CONST.__const: 0x300
+  __AUTH_CONST.__cfstring: 0x1a40
   __AUTH_CONST.__objc_const: 0x2ba0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x78

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 29409DA9-F8C8-3B66-B604-DD080188B994
-  Functions: 690
-  Symbols:   2526
-  CStrings:  1571
+  UUID: 535630E3-12AE-3BF5-8031-B91791ADFE5E
+  Functions: 696
+  Symbols:   2535
+  CStrings:  1582
 
Symbols:
+ +[SDDevice currentDevicePlatform]
+ -[SDBetaEnrollmentService queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]
+ -[SDBetaEnrollmentServiceProxy queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]
+ -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:completion:]
+ -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:completion:].cold.1
+ -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:completion:].cold.2
+ -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]
+ -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:].cold.1
+ -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:].cold.2
+ -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:].cold.3
+ -[SDBetaManager queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]
+ GCC_except_table145
+ GCC_except_table20
+ GCC_except_table27
+ GCC_except_table78
+ GCC_except_table81
+ GCC_except_table96
+ _SDTransactionCreate
+ ___100-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]_block_invoke
+ ___100-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]_block_invoke.355
+ ___100-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]_block_invoke.355.cold.1
+ ___100-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]_block_invoke.cold.1
+ ___107-[SDBetaEnrollmentService configureWithOfferProgramTokens:requireProgramToken:enrollmentPolicy:completion:]_block_invoke
+ ___109-[SDBetaEnrollmentService queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]_block_invoke
+ ___114-[SDBetaEnrollmentServiceProxy queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]_block_invoke
+ ___159-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:completion:]_block_invoke
+ ___159-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:completion:]_block_invoke.cold.1
+ ___159-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:completion:]_block_invoke.cold.2
+ ___159-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:completion:]_block_invoke.cold.3
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.597
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.598
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.598.cold.1
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.598.cold.2
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.599
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.599.cold.1
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.599.cold.2
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.599.cold.3
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.600
+ ___63-[SDBetaEnrollmentService enrollInProgramWithToken:completion:]_block_invoke
+ ___64-[SDBetaManager enrollDevice:withEnrollmentMetadata:completion:]_block_invoke.406
+ ___73-[SDBetaManager _saveAppleAccountIdentifierWithAlternateDSID:completion:]_block_invoke.456
+ ___99-[SDBetaManager queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]_block_invoke
+ ___block_descriptor_40_e8_32s_e8_v12?0B8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e8_v16?0q8ls32l8s40l8
+ ___block_descriptor_49_e8_32bs_e56_v24?0"<SDBetaEnrollmentServiceInterface>"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_66_e8_32s40bs48w_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24ls40l8s32l8w48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s64l8s56l8
+ ___block_descriptor_75_e8_32s40s48bs56r_e5_v8?0lr56l8s48l8s32l8s40l8
+ ___block_literal_global.130
+ ___block_literal_global.176
+ _objc_msgSend$_finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:completion:
+ _objc_msgSend$_queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:
+ _objc_msgSend$currentDevicePlatform
+ _objc_msgSend$queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:
+ _os_transaction_create
- -[SDBetaEnrollmentService queryProgramsForSystemAccountsWithPlatforms:completion:]
- -[SDBetaEnrollmentServiceProxy queryProgramsForSystemAccountsWithPlatforms:completion:]
- -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:completion:]
- -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:completion:].cold.1
- -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:completion:].cold.2
- -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:]
- -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:].cold.1
- -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:].cold.2
- -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:].cold.3
- GCC_except_table144
- GCC_except_table19
- GCC_except_table26
- GCC_except_table77
- GCC_except_table80
- GCC_except_table95
- ___132-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:completion:]_block_invoke
- ___132-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:completion:]_block_invoke.cold.1
- ___132-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:completion:]_block_invoke.cold.2
- ___132-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:completion:]_block_invoke.cold.3
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.592
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.593
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.593.cold.1
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.593.cold.2
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.594
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.594.cold.1
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.594.cold.2
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.594.cold.3
- ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.595
- ___64-[SDBetaManager enrollDevice:withEnrollmentMetadata:completion:]_block_invoke.403
- ___72-[SDBetaManager queryProgramsForSystemAccountsWithPlatforms:completion:]_block_invoke
- ___73-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:]_block_invoke
- ___73-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:]_block_invoke.352
- ___73-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:]_block_invoke.352.cold.1
- ___73-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:]_block_invoke.cold.1
- ___73-[SDBetaManager _saveAppleAccountIdentifierWithAlternateDSID:completion:]_block_invoke.453
- ___87-[SDBetaEnrollmentServiceProxy queryProgramsForSystemAccountsWithPlatforms:completion:]_block_invoke
- ___block_descriptor_32_e8_v12?0B8l
- ___block_descriptor_48_e8_32bs_e5_v8?0ls32l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
- ___block_descriptor_65_e8_32s40bs48w_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24ls40l8s32l8w48l8
- ___block_descriptor_74_e8_32s40s48bs56r_e5_v8?0lr56l8s48l8s32l8s40l8
- ___block_literal_global.129
- ___block_literal_global.177
- ___block_literal_global.37
- ___block_literal_global.40
- _objc_msgSend$_finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:completion:
- _objc_msgSend$_queryProgramsForSystemAccountsWithPlatforms:completion:
- _objc_msgSend$queryProgramsForSystemAccountsWithPlatforms:completion:
CStrings:
+ "%s-%s"
+ "-[SDBetaEnrollmentService getDevicesForPlatforms:completion:]"
+ "-[SDBetaEnrollmentService queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]"
+ "-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:completion:]"
+ "-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]"
+ "-[SDBetaManager queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:]"
+ "Already sent conformsToProtocol error via completion handler"
+ "Already sent remoteObjectProxyWithErrorHandler error via completion handler"
+ "Calling completion handler for betaEnrollmentProxyObjectWithCompletion with no error"
+ "Getting current program for device %{private}@"
+ "Sending conformsToProtocol error via completion handler"
+ "Sending remoteObjectProxyWithErrorHandler error via completion handler"
+ "_finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:disableBuildPrefixMatching:completion:"
+ "_queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:"
+ "currentDevicePlatform"
+ "queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:completion:"
+ "v36@0:8Q16B24@?28"
+ "v36@0:8Q16B24@?<v@?@\"NSArray\"q>28"
+ "v56@0:8Q16@24@32B40B44@?48"
- "-[SDBetaEnrollmentService queryProgramsForSystemAccountsWithPlatforms:completion:]"
- "-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:completion:]"
- "-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:]"
- "-[SDBetaManager queryProgramsForSystemAccountsWithPlatforms:completion:]"
- "Getting current program for device %{public}@"
- "_finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:shouldSavePrograms:completion:"
- "_queryProgramsForSystemAccountsWithPlatforms:completion:"
- "v32@0:8Q16@?<v@?@\"NSArray\"q>24"
- "v52@0:8Q16@24@32B40@?44"

```
