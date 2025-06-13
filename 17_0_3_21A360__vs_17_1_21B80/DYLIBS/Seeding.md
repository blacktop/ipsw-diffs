## Seeding

> `/System/Library/PrivateFrameworks/Seeding.framework/Seeding`

```diff

-88.0.0.0.0
-  __TEXT.__text: 0x1881c
-  __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_methlist: 0x1274
+89.0.0.0.0
+  __TEXT.__text: 0x19578
+  __TEXT.__auth_stubs: 0x6e0
+  __TEXT.__objc_methlist: 0x129c
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x350
-  __TEXT.__cstring: 0x16bc
-  __TEXT.__oslogstring: 0x23e4
-  __TEXT.__unwind_info: 0x680
-  __TEXT.__objc_classname: 0x200
-  __TEXT.__objc_methname: 0x35a8
-  __TEXT.__objc_methtype: 0x5ca
-  __TEXT.__objc_stubs: 0x3460
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x878
+  __TEXT.__cstring: 0x16f0
+  __TEXT.__oslogstring: 0x25af
+  __TEXT.__unwind_info: 0x6bc
+  __TEXT.__objc_classname: 0x208
+  __TEXT.__objc_methname: 0x3644
+  __TEXT.__objc_methtype: 0x5dc
+  __TEXT.__objc_stubs: 0x34c0
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__const: 0x940
   __DATA_CONST.__objc_classlist: 0xa8
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x2ac8
-  __DATA_CONST.__objc_selrefs: 0xed0
+  __DATA_CONST.__objc_selrefs: 0xee8
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__cfstring: 0x15a0
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__objc_const: 0x40
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x370
+  __AUTH_CONST.__auth_got: 0x380
   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0x1d0
   __DATA.__objc_superrefs: 0x40

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D296992D-2988-3A97-9F8F-59F24DC04958
-  Functions: 593
-  Symbols:   2242
-  CStrings:  1330
+  UUID: FF3B3EFB-9291-3D7D-B4E4-86125570888E
+  Functions: 613
+  Symbols:   2294
+  CStrings:  1350
 
Symbols:
+ -[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]
+ -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:completion:]
+ -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:completion:].cold.1
+ -[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:completion:].cold.2
+ GCC_except_table21
+ GCC_except_table68
+ GCC_except_table73
+ GCC_except_table85
+ _OBJC_CLASS_$_ACAccount
+ _OUTLINED_FUNCTION_12
+ __OBJC_$_CATEGORY_ACAccount_$_Seeding
+ __OBJC_$_INSTANCE_METHODS_ACAccount(Seeding)
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.502
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.503
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.503.cold.1
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.503.cold.2
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.504
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.504.cold.1
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.504.cold.2
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.504.cold.3
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.505
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.cold.1
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke.cold.2
+ ___57-[ACAccount(Seeding) fetchCredentialTokenWithCompletion:]_block_invoke_2
+ ___64-[SDBetaManager enrollDevice:withEnrollmentMetadata:completion:]_block_invoke.326
+ ___73-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:]_block_invoke.281
+ ___73-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:]_block_invoke.281.cold.1
+ ___73-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:]_block_invoke.281.cold.2
+ ___73-[SDBetaManager _saveAppleAccountIdentifierWithAlternateDSID:completion:]_block_invoke.369
+ ___92-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:completion:]_block_invoke
+ ___92-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:completion:]_block_invoke.cold.1
+ ___92-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:completion:]_block_invoke.cold.2
+ ___92-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:completion:]_block_invoke.cold.3
+ ___block_descriptor_40_e8_32bs_e30_v24?0"NSString"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e20_v24?0q8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSString"8"NSError"16ls40l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56s_e18_v16?0"NSString"8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.512
+ _dispatch_group_notify
+ _objc_msgSend$_finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:completion:
+ _objc_msgSend$accountStore
+ _objc_msgSend$aida_renewCredentialsForAccount:services:completion:
+ _objc_msgSend$aida_tokenForService:completionHandler:
+ _objc_msgSend$fetchCredentialTokenWithCompletion:
+ _objc_retain_x28
- -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:].cold.3
- -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:].cold.4
- -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:].cold.5
- GCC_except_table18
- GCC_except_table65
- GCC_except_table70
- GCC_except_table82
- _ACAccountTypeIdentifierAppleIDAuthentication
- ___64-[SDBetaManager enrollDevice:withEnrollmentMetadata:completion:]_block_invoke.324
- ___73-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:]_block_invoke.cold.2
- ___73-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:]_block_invoke.cold.3
- ___73-[SDBetaManager _saveAppleAccountIdentifierWithAlternateDSID:completion:]_block_invoke.367
- ___block_literal_global.500
- _objc_msgSend$accountTypeWithAccountTypeIdentifier:
- _objc_msgSend$accountsWithAccountType:
CStrings:
+ "Credential renewal failed with [%{public}@]"
+ "Credential token for FBK IDMS is nil after renewing credential"
+ "Error details: %@"
+ "Failed to get token after renewal: %{public}@"
+ "Failed to get token for FBK IDMS Service: %{public}@"
+ "Finished fetching all credential tokens"
+ "Nil credential token for FBK IDMS Service. Will renew"
+ "No credential token for account %@"
+ "Will use Seeding account"
+ "Will use iCloud account"
+ "_finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:completion:"
+ "accountStore"
+ "aida_renewCredentialsForAccount:services:completion:"
+ "aida_tokenForService:completionHandler:"
+ "fetchCredentialTokenWithCompletion:"
+ "renewal result: failed"
+ "renewal result: rejected"
+ "renewal result: renewed"
+ "renewal result: unhandled case"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v24@?0q8@\"NSError\"16"
+ "v40@0:8Q16@24@?32"
- "Credential token not available for account %@"
- "accountTypeWithAccountTypeIdentifier:"
- "accountsWithAccountType:"

```
