## MobileInstallation

> `/System/Library/PrivateFrameworks/MobileInstallation.framework/Versions/A/MobileInstallation`

```diff

-1378.60.22.0.0
-  __TEXT.__text: 0x18714
+1378.100.35.0.0
+  __TEXT.__text: 0x197ec
   __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0xb60
-  __TEXT.__cstring: 0x33db
-  __TEXT.__gcc_except_tab: 0x560
+  __TEXT.__objc_methlist: 0xe3c
+  __TEXT.__cstring: 0x34ea
+  __TEXT.__gcc_except_tab: 0x5b8
   __TEXT.__const: 0x30
   __TEXT.__oslogstring: 0x43
-  __TEXT.__unwind_info: 0x768
+  __TEXT.__unwind_info: 0x7c0
   __TEXT.__objc_classname: 0x166
-  __TEXT.__objc_methname: 0x35c0
-  __TEXT.__objc_methtype: 0xde1
-  __TEXT.__objc_stubs: 0x22a0
-  __DATA_CONST.__got: 0x198
-  __DATA_CONST.__const: 0x140
+  __TEXT.__objc_methname: 0x35ca
+  __TEXT.__objc_methtype: 0xe01
+  __TEXT.__objc_stubs: 0x2260
+  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__const: 0x148
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa40
+  __DATA_CONST.__objc_selrefs: 0xa70
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x68
   __AUTH_CONST.__auth_got: 0x318
-  __AUTH_CONST.__const: 0x7a0
+  __AUTH_CONST.__const: 0x800
   __AUTH_CONST.__cfstring: 0x1da0
-  __AUTH_CONST.__objc_const: 0x1a50
+  __AUTH_CONST.__objc_const: 0x1550
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x30

   - /System/Library/PrivateFrameworks/MobileSystemServices.framework/Versions/A/MobileSystemServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ED06AFD7-F9FE-380F-B477-EF0B84386642
-  Functions: 549
-  Symbols:   1256
-  CStrings:  1203
+  UUID: 8E2ABA2A-1AED-3EA0-9CB1-35085AF91AFC
+  Functions: 569
+  Symbols:   1279
+  CStrings:  1207
 
Symbols:
+ +[AITransactionLog _defaultLog].cold.1
+ +[AITransactionLog logStep:byParty:phase:success:forBundleID:persona:description:].cold.1
+ +[MIPlaceholderConstructor _infoPlistKeysToLoad].cold.1
+ -[MIInstallerClient allStagedUpdatesWithCompletion:]
+ -[MIInstallerClient cancelUpdateForStagedIdentifiers:completion:]
+ -[MIInstallerClient finalizeStagedInstallForIdentifier:returningResultInfo:completion:]
+ -[MIInstallerClient installParallelPlaceholderForStagedIdentifier:returningResultInfo:completion:]
+ GCC_except_table127
+ GCC_except_table134
+ GCC_except_table139
+ GCC_except_table142
+ GCC_except_table145
+ GCC_except_table150
+ GCC_except_table153
+ GCC_except_table156
+ GCC_except_table176
+ GCC_except_table188
+ GCC_except_table190
+ GCC_except_table196
+ GCC_except_table202
+ GCC_except_table204
+ GCC_except_table207
+ GCC_except_table213
+ GCC_except_table215
+ GCC_except_table224
+ GCC_except_table226
+ GCC_except_table228
+ GCC_except_table230
+ GCC_except_table232
+ GCC_except_table237
+ GCC_except_table239
+ GCC_except_table241
+ GCC_except_table253
+ GCC_except_table267
+ _MobileInstallationCancelUpdateForStagedIdentifiersWithError
+ _MobileInstallationGetAllStagedUpdateIdentifiers
+ _MobileInstallationInstallParallelPlaceholderForStagedUpdate
+ _MobileInstallationMakeStagedUpdateLiveForIdentifier
+ __35-[MIInstallerClient raiseException]_block_invoke.59
+ __MobileInstallationGetHelperServicePid_block_invoke.252
+ __MobileInstallationInstallApplicationWithIdentityAndAssertionBlockWithError_block_invoke.185
+ __MobileInstallationInstallApplicationWithIdentityAndAssertionBlockWithError_block_invoke.189
+ __MobileInstallationInstallApplicationWithIdentityAndAssertionBlockWithError_block_invoke_2.186
+ ___52-[MIInstallerClient allStagedUpdatesWithCompletion:]_block_invoke
+ ___52-[MIInstallerClient allStagedUpdatesWithCompletion:]_block_invoke_2
+ ___52-[MIInstallerClient allStagedUpdatesWithCompletion:]_block_invoke_3
+ ___52-[MIInstallerClient allStagedUpdatesWithCompletion:]_block_invoke_4
+ ___65-[MIInstallerClient cancelUpdateForStagedIdentifiers:completion:]_block_invoke
+ ___65-[MIInstallerClient cancelUpdateForStagedIdentifiers:completion:]_block_invoke_2
+ ___65-[MIInstallerClient cancelUpdateForStagedIdentifiers:completion:]_block_invoke_3
+ ___65-[MIInstallerClient cancelUpdateForStagedIdentifiers:completion:]_block_invoke_4
+ ___87-[MIInstallerClient finalizeStagedInstallForIdentifier:returningResultInfo:completion:]_block_invoke
+ ___87-[MIInstallerClient finalizeStagedInstallForIdentifier:returningResultInfo:completion:]_block_invoke_2
+ ___87-[MIInstallerClient finalizeStagedInstallForIdentifier:returningResultInfo:completion:]_block_invoke_3
+ ___87-[MIInstallerClient finalizeStagedInstallForIdentifier:returningResultInfo:completion:]_block_invoke_4
+ ___98-[MIInstallerClient installParallelPlaceholderForStagedIdentifier:returningResultInfo:completion:]_block_invoke
+ ___98-[MIInstallerClient installParallelPlaceholderForStagedIdentifier:returningResultInfo:completion:]_block_invoke_2
+ ___98-[MIInstallerClient installParallelPlaceholderForStagedIdentifier:returningResultInfo:completion:]_block_invoke_3
+ ___98-[MIInstallerClient installParallelPlaceholderForStagedIdentifier:returningResultInfo:completion:]_block_invoke_4
+ ___MobileInstallationCancelUpdateForStagedIdentifiersWithError_block_invoke
+ ___MobileInstallationGetAllStagedUpdateIdentifiers_block_invoke
+ ___MobileInstallationInstallParallelPlaceholderForStagedUpdate_block_invoke
+ ___MobileInstallationInstallParallelPlaceholderForStagedUpdate_block_invoke_2
+ ___MobileInstallationInstallParallelPlaceholderForStagedUpdate_block_invoke_3
+ ___MobileInstallationInstallParallelPlaceholderForStagedUpdate_block_invoke_4
+ ___MobileInstallationInstallParallelPlaceholderForStagedUpdate_block_invoke_5
+ ___MobileInstallationMakeStagedUpdateLiveForIdentifier_block_invoke
+ ___MobileInstallationMakeStagedUpdateLiveForIdentifier_block_invoke_2
+ ___MobileInstallationMakeStagedUpdateLiveForIdentifier_block_invoke_3
+ ___MobileInstallationMakeStagedUpdateLiveForIdentifier_block_invoke_4
+ ___MobileInstallationMakeStagedUpdateLiveForIdentifier_block_invoke_5
+ ___block_descriptor_48_e8_32r40r_e27_v24?0"NSSet"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e27_v24?0"NSSet"8"NSError"16l
+ __block_literal_global.53
+ _objc_msgSend$allStagedUpdatesWithCompletion:
+ _objc_msgSend$cancelUpdateForStagedIdentifiers:completion:
+ _objc_msgSend$finalizeStagedInstallForIdentifier:returningResultInfo:completion:
+ _objc_msgSend$installParallelPlaceholderForStagedIdentifier:returningResultInfo:completion:
- -[MIInstallerClient cancelUpdateForStagedUUID:completion:]
- -[MIInstallerClient finalizeStagedInstallForUUID:returningResultInfo:completion:]
- GCC_except_table117
- GCC_except_table124
- GCC_except_table129
- GCC_except_table132
- GCC_except_table135
- GCC_except_table140
- GCC_except_table143
- GCC_except_table146
- GCC_except_table166
- GCC_except_table178
- GCC_except_table180
- GCC_except_table186
- GCC_except_table189
- GCC_except_table195
- GCC_except_table197
- GCC_except_table199
- GCC_except_table206
- GCC_except_table208
- GCC_except_table210
- GCC_except_table212
- GCC_except_table214
- GCC_except_table219
- GCC_except_table221
- GCC_except_table223
- GCC_except_table249
- _MobileInstallationCancelStagedUpdateForUUIDWithError
- _MobileInstallationMakeStagedApplicationUpdateLiveForIdentityWithError
- __35-[MIInstallerClient raiseException]_block_invoke.56
- __MobileInstallationGetHelperServicePid_block_invoke.245
- __MobileInstallationInstallApplicationWithIdentityAndAssertionBlockWithError_block_invoke.180
- __MobileInstallationInstallApplicationWithIdentityAndAssertionBlockWithError_block_invoke.184
- __MobileInstallationInstallApplicationWithIdentityAndAssertionBlockWithError_block_invoke_2.181
- ___58-[MIInstallerClient cancelUpdateForStagedUUID:completion:]_block_invoke
- ___58-[MIInstallerClient cancelUpdateForStagedUUID:completion:]_block_invoke_2
- ___58-[MIInstallerClient cancelUpdateForStagedUUID:completion:]_block_invoke_3
- ___58-[MIInstallerClient cancelUpdateForStagedUUID:completion:]_block_invoke_4
- ___81-[MIInstallerClient finalizeStagedInstallForUUID:returningResultInfo:completion:]_block_invoke
- ___81-[MIInstallerClient finalizeStagedInstallForUUID:returningResultInfo:completion:]_block_invoke_2
- ___81-[MIInstallerClient finalizeStagedInstallForUUID:returningResultInfo:completion:]_block_invoke_3
- ___81-[MIInstallerClient finalizeStagedInstallForUUID:returningResultInfo:completion:]_block_invoke_4
- ___MobileInstallationCancelStagedUpdateForUUIDWithError_block_invoke
- ___MobileInstallationMakeStagedApplicationUpdateLiveForIdentityWithError_block_invoke
- ___MobileInstallationMakeStagedApplicationUpdateLiveForIdentityWithError_block_invoke_2
- ___MobileInstallationMakeStagedApplicationUpdateLiveForIdentityWithError_block_invoke_3
- ___MobileInstallationMakeStagedApplicationUpdateLiveForIdentityWithError_block_invoke_4
- ___MobileInstallationMakeStagedApplicationUpdateLiveForIdentityWithError_block_invoke_5
- __block_literal_global.50
- _objc_msgSend$cancelUpdateForStagedUUID:completion:
- _objc_msgSend$dictionaryWithContentsOfURL:
- _objc_msgSend$finalizeStagedInstallForUUID:returningResultInfo:completion:
- _objc_msgSend$itemDoesNotExistOrIsNotDirectoryAtURL:
- _objc_msgSend$itemExistsAtURL:
- _objc_msgSend$itemIsDirectoryAtURL:error:
CStrings:
+ "-[MIInstallerClient finalizeStagedInstallForIdentifier:returningResultInfo:completion:]_block_invoke_3"
+ "-[MIInstallerClient installParallelPlaceholderForStagedIdentifier:returningResultInfo:completion:]_block_invoke_3"
+ "MobileInstallationCancelUpdateForStagedIdentifiersWithError"
+ "MobileInstallationGetAllStagedUpdateIdentifiers"
+ "MobileInstallationInstallParallelPlaceholderForStagedUpdate"
+ "MobileInstallationMakeStagedUpdateLiveForIdentifier"
+ "Staged Update Placeholder"
+ "allStagedUpdatesWithCompletion:"
+ "cancelUpdateForStagedIdentifiers:completion:"
+ "finalizeStagedInstallForIdentifier:returningResultInfo:completion:"
+ "installParallelPlaceholderForStagedIdentifier:returningResultInfo:completion:"
+ "v24@0:8@?<v@?@\"NSSet\"@\"NSError\">16"
+ "v24@?0@\"NSSet\"8@\"NSError\"16"
+ "v32@0:8@\"NSSet\"16@?<v@?B@\"NSError\">24"
- "-[MIInstallerClient finalizeStagedInstallForUUID:returningResultInfo:completion:]_block_invoke_3"
- "MobileInstallationCancelStagedUpdateForUUIDWithError"
- "MobileInstallationMakeStagedApplicationUpdateLiveForIdentityWithError"
- "cancelUpdateForStagedUUID:completion:"
- "dictionaryWithContentsOfURL:"
- "finalizeStagedInstallForUUID:returningResultInfo:completion:"
- "itemDoesNotExistOrIsNotDirectoryAtURL:"
- "itemExistsAtURL:"
- "itemIsDirectoryAtURL:error:"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"

```
