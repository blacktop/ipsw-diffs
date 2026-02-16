## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`

```diff

-416.325.4.0.0
-  __TEXT.__text: 0x52334
-  __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__objc_methlist: 0x3954
-  __TEXT.__const: 0x1324
-  __TEXT.__gcc_except_tab: 0x125c
-  __TEXT.__oslogstring: 0x8da1
-  __TEXT.__cstring: 0x5b99
+416.475.8.0.0
+  __TEXT.__text: 0x51bb8
+  __TEXT.__auth_stubs: 0x1020
+  __TEXT.__objc_methlist: 0x39e4
+  __TEXT.__const: 0x139c
+  __TEXT.__gcc_except_tab: 0x131c
+  __TEXT.__oslogstring: 0x9085
+  __TEXT.__cstring: 0x60f4
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x1550
-  __TEXT.__objc_classname: 0x719
-  __TEXT.__objc_methname: 0x8f7b
-  __TEXT.__objc_methtype: 0x1b9a
-  __TEXT.__objc_stubs: 0x4ee0
+  __TEXT.__unwind_info: 0x1688
+  __TEXT.__objc_classname: 0x71d
+  __TEXT.__objc_methname: 0x9156
+  __TEXT.__objc_methtype: 0x1bde
+  __TEXT.__objc_stubs: 0x4f60
   __DATA_CONST.__got: 0x4e0
-  __DATA_CONST.__const: 0x2ec8
+  __DATA_CONST.__const: 0x2f90
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2128
+  __DATA_CONST.__objc_selrefs: 0x2180
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x860
-  __AUTH_CONST.__const: 0x5b0
-  __AUTH_CONST.__cfstring: 0x3b80
-  __AUTH_CONST.__objc_const: 0x86f0
+  __AUTH_CONST.__auth_got: 0x820
+  __AUTH_CONST.__const: 0x610
+  __AUTH_CONST.__cfstring: 0x3bc0
+  __AUTH_CONST.__objc_const: 0x8778
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_ivar: 0x2ec
-  __DATA.__data: 0x1110
-  __DATA.__bss: 0x109
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x2f4
+  __DATA.__data: 0x1118
+  __DATA.__bss: 0x121
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x9b0
+  __DATA_DIRTY.__objc_data: 0x1040
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 334538B9-90A3-3D4B-BC4D-519206C584AA
-  Functions: 2276
-  Symbols:   7596
-  CStrings:  3743
+  UUID: 05431301-C68E-35B6-BD27-25284A538BA7
+  Functions: 2341
+  Symbols:   7838
+  CStrings:  3802
 
Symbols:
+ +[CDPUtilities isDBRTwoEnabled]
+ +[CDPUtilities isDBRTwoEnabled].cold.1
+ -[CDPContext interactiveAuthForceModalPresentation]
+ -[CDPContext setInteractiveAuthForceModalPresentation:]
+ -[CDPContext setSrpVerifier:]
+ -[CDPContext srpVerifier]
+ -[CDPProtectedCloudStorageProxyImpl generatePDPBlob:completion:]
+ -[CDPProtectedCloudStorageProxyImpl generatePDPBlob:completion:].cold.1
+ -[CDPProtectedCloudStorageProxyImpl healBrokenADPEnablementWithAccountIdentifier:parameters:completion:]
+ -[CDPProtectedCloudStorageProxyImpl healBrokenADPEnablementWithAccountIdentifier:parameters:completion:].cold.1
+ -[CDPProtectedCloudStorageProxyImpl healBrokenADPEnablementWithAccountIdentifier:parameters:completion:].cold.2
+ -[CDPProtectedCloudStorageProxyImpl pdpPCSDBRRepairIdentities:completion:]
+ -[CDPStateController _performPDPBlobGenerationWithCompletionHandler:]
+ -[CDPStateController generatePDPBlobWithCompletion:]
+ -[NSError(PDP) cdp_isPDPPasswordRequiredError]
+ GCC_except_table103
+ GCC_except_table106
+ GCC_except_table110
+ GCC_except_table122
+ GCC_except_table130
+ GCC_except_table141
+ GCC_except_table144
+ GCC_except_table147
+ GCC_except_table149
+ GCC_except_table152
+ GCC_except_table155
+ GCC_except_table24
+ GCC_except_table33
+ GCC_except_table53
+ GCC_except_table57
+ GCC_except_table67
+ GCC_except_table70
+ GCC_except_table73
+ GCC_except_table77
+ GCC_except_table81
+ GCC_except_table85
+ GCC_except_table89
+ GCC_except_table93
+ GCC_except_table96
+ GCC_except_table99
+ _OBJC_IVAR_$_CDPContext._interactiveAuthForceModalPresentation
+ _OBJC_IVAR_$_CDPContext._srpVerifier
+ _OUTLINED_FUNCTION_76
+ _OUTLINED_FUNCTION_77
+ _OUTLINED_FUNCTION_78
+ _OUTLINED_FUNCTION_79
+ _OUTLINED_FUNCTION_80
+ _OUTLINED_FUNCTION_81
+ _OUTLINED_FUNCTION_82
+ _OUTLINED_FUNCTION_83
+ _OUTLINED_FUNCTION_84
+ _OUTLINED_FUNCTION_85
+ _OUTLINED_FUNCTION_86
+ _OUTLINED_FUNCTION_87
+ _OUTLINED_FUNCTION_88
+ _OUTLINED_FUNCTION_89
+ _PCSDBRRepairIdentities
+ _PCSGenerateDBRBlob
+ _ProtectedCloudStorageLibrary
+ __OBJC_$_INSTANCE_METHODS_NSError(CoreCDP|PDP|CDP)
+ ___31+[CDPUtilities isDBRTwoEnabled]_block_invoke
+ ___31+[CDPUtilities isDBRTwoEnabled]_block_invoke.cold.1
+ ___46-[NSError(PDP) cdp_isPDPPasswordRequiredError]_block_invoke
+ ___48-[CDPStateController generateRandomRecoveryKey:]_block_invoke.65
+ ___49-[CDPStateController deleteRecoveryKeyWithError:]_block_invoke.56
+ ___52-[CDPStateController generatePDPBlobWithCompletion:]_block_invoke
+ ___52-[CDPStateController generatePDPBlobWithCompletion:]_block_invoke.43
+ ___52-[CDPStateController generatePDPBlobWithCompletion:]_block_invoke_2
+ ___52-[CDPStateController generatePDPBlobWithCompletion:]_block_invoke_3
+ ___52-[CDPStateController generatePDPBlobWithCompletion:]_block_invoke_4
+ ___54-[CDPStateController isRecoveryKeyAvailableWithError:]_block_invoke.57
+ ___59-[CDPStateController isRecoveryKeyAvailableWithCompletion:]_block_invoke.58
+ ___60-[CDPStateController isWalrusRecoveryKeyAvailableWithError:]_block_invoke.60
+ ___64-[CDPProtectedCloudStorageProxyImpl generatePDPBlob:completion:]_block_invoke
+ ___65-[CDPStateController isWalrusRecoveryKeyAvailableWithCompletion:]_block_invoke.61
+ ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.44
+ ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.44.cold.1
+ ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.45
+ ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.45.cold.1
+ ___66-[CDPStateController startSilentEscrowRecordRepairWithCompletion:]_block_invoke.81
+ ___66-[CDPStateController validatePDPIdentitiesWithContext:completion:]_block_invoke.87
+ ___66-[CDPStateController validatePDPIdentitiesWithContext:completion:]_block_invoke.87.cold.1
+ ___67-[CDPStateController createPDPLivenessDictionaryWithContext:error:]_block_invoke.89
+ ___68-[CDPStateController performSilentEscrowRecordRepairWithCompletion:]_block_invoke.82
+ ___68-[CDPStateController shouldPerformRepairWithOptionForceFetch:error:]_block_invoke.46
+ ___69-[CDPStateController _performPDPBlobGenerationWithCompletionHandler:]_block_invoke
+ ___69-[CDPStateController _performPDPBlobGenerationWithCompletionHandler:]_block_invoke_2
+ ___69-[CDPStateController _performPDPBlobGenerationWithCompletionHandler:]_block_invoke_2.cold.1
+ ___69-[CDPStateController authenticateAndDeleteRecoveryKeyWithCompletion:]_block_invoke.53
+ ___69-[CDPStateController authenticateAndDeleteRecoveryKeyWithCompletion:]_block_invoke.53.cold.1
+ ___70-[CDPStateController generateEscrowRecordReportUsingCache:completion:]_block_invoke.49
+ ___72-[CDPStateController anyRecoveryKeysAreOctagonDistrustedWithCompletion:]_block_invoke.64
+ ___74-[CDPProtectedCloudStorageProxyImpl pdpPCSDBRRepairIdentities:completion:]_block_invoke
+ ___74-[CDPStateController authenticateAndGenerateNewRecoveryKeyWithCompletion:]_block_invoke.51
+ ___74-[CDPStateController authenticateAndGenerateNewRecoveryKeyWithCompletion:]_block_invoke.51.cold.1
+ ___74-[CDPStateController updateLastSilentEscrowRecordRepairAttemptDate:error:]_block_invoke.83
+ ___76-[CDPStateController shouldPerformSilentEscrowRecordRepairUsingCache:error:]_block_invoke.79
+ ___81-[CDPStateController shouldPerformAuthenticatedRepairWithOptionForceFetch:error:]_block_invoke.47
+ ___81-[CDPStateController shouldPerformSilentEscrowRecordRepairUsingCache:completion:]_block_invoke.80
+ ___82-[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]_block_invoke.91
+ ___82-[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]_block_invoke.91.cold.1
+ ___82-[CDPStateController verifyRecoveryKeyObservingSystemsHaveMatchingStateWithError:]_block_invoke.62
+ ___block_descriptor_48_e8_32bs40r_e30_v24?0"NSString"8"NSError"16lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e25_v16?0?<v?"NSError">8ls32l8r40l8
+ ___block_descriptor_56_e8_32bs_e28_v24?0"NSData"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32bs40r_e20_v24?08"NSError"16lr40l8s32l8
+ ___block_descriptor_tmp.181
+ ___block_literal_global.103
+ ___block_literal_global.176
+ ___block_literal_global.183
+ ___block_literal_global.42
+ ___block_literal_global.83
+ ___block_literal_global.85
+ ___der_key_keybag_type
+ ___getPCSAccountHealWalrusStateSymbolLoc_block_invoke
+ _akstest_new_ekwk.cold.1
+ _akstest_new_key.cold.1
+ _akstest_unwrap_ek.cold.1
+ _akstest_unwrap_key.cold.1
+ _der_key_keybag_type
+ _getPCSAccountHealWalrusStateSymbolLoc.ptr
+ _isDBRTwoEnabled.enabled
+ _isDBRTwoEnabled.once
+ _kCDPAnalyticsADPHealingEvent
+ _objc_msgSend$_performPDPBlobGenerationWithCompletionHandler:
+ _objc_msgSend$base64Encoding
+ _objc_msgSend$cdp_anyDescendantErrorDownToMaxDepth:matchesPredicate:
+ _objc_msgSend$generatePDPBlobWithContext:completion:
- +[CDPFollowUpContext contextForCDPPDPStateRepair]
- +[CDPFollowUpContext contextForCDPPDPStateRepair].cold.1
- -[CDPProtectedCloudStorageProxyImpl pdpPCSGuitarfishRepairIdentities:completion:]
- GCC_except_table101
- GCC_except_table104
- GCC_except_table108
- GCC_except_table121
- GCC_except_table123
- GCC_except_table129
- GCC_except_table140
- GCC_except_table143
- GCC_except_table146
- GCC_except_table26
- GCC_except_table52
- GCC_except_table55
- GCC_except_table58
- GCC_except_table68
- GCC_except_table72
- GCC_except_table76
- GCC_except_table80
- GCC_except_table84
- GCC_except_table87
- GCC_except_table90
- GCC_except_table94
- GCC_except_table97
- _CDP_FOLLOWUP_CDP_PDP_REPAIR
- _PCSGuitarfishRepairIdentities
- __OBJC_$_INSTANCE_METHODS_NSError(CoreCDP|CDP)
- ___48-[CDPStateController generateRandomRecoveryKey:]_block_invoke.61
- ___49-[CDPStateController deleteRecoveryKeyWithError:]_block_invoke.52
- ___54-[CDPStateController isRecoveryKeyAvailableWithError:]_block_invoke.53
- ___59-[CDPStateController isRecoveryKeyAvailableWithCompletion:]_block_invoke.54
- ___60-[CDPStateController isWalrusRecoveryKeyAvailableWithError:]_block_invoke.56
- ___65-[CDPStateController isWalrusRecoveryKeyAvailableWithCompletion:]_block_invoke.57
- ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.40
- ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.40.cold.1
- ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.41
- ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.41.cold.1
- ___66-[CDPStateController startSilentEscrowRecordRepairWithCompletion:]_block_invoke.78
- ___66-[CDPStateController validatePDPIdentitiesWithContext:completion:]_block_invoke.84
- ___66-[CDPStateController validatePDPIdentitiesWithContext:completion:]_block_invoke.84.cold.1
- ___67-[CDPStateController createPDPLivenessDictionaryWithContext:error:]_block_invoke.86
- ___68-[CDPStateController performSilentEscrowRecordRepairWithCompletion:]_block_invoke.79
- ___68-[CDPStateController shouldPerformRepairWithOptionForceFetch:error:]_block_invoke.42
- ___69-[CDPStateController authenticateAndDeleteRecoveryKeyWithCompletion:]_block_invoke.49
- ___69-[CDPStateController authenticateAndDeleteRecoveryKeyWithCompletion:]_block_invoke.49.cold.1
- ___70-[CDPStateController generateEscrowRecordReportUsingCache:completion:]_block_invoke.45
- ___72-[CDPStateController anyRecoveryKeysAreOctagonDistrustedWithCompletion:]_block_invoke.60
- ___74-[CDPStateController authenticateAndGenerateNewRecoveryKeyWithCompletion:]_block_invoke.47
- ___74-[CDPStateController authenticateAndGenerateNewRecoveryKeyWithCompletion:]_block_invoke.47.cold.1
- ___74-[CDPStateController updateLastSilentEscrowRecordRepairAttemptDate:error:]_block_invoke.80
- ___76-[CDPStateController shouldPerformSilentEscrowRecordRepairUsingCache:error:]_block_invoke.76
- ___81-[CDPProtectedCloudStorageProxyImpl pdpPCSGuitarfishRepairIdentities:completion:]_block_invoke
- ___81-[CDPStateController shouldPerformAuthenticatedRepairWithOptionForceFetch:error:]_block_invoke.43
- ___81-[CDPStateController shouldPerformSilentEscrowRecordRepairUsingCache:completion:]_block_invoke.77
- ___82-[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]_block_invoke.88
- ___82-[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]_block_invoke.88.cold.1
- ___82-[CDPStateController verifyRecoveryKeyObservingSystemsHaveMatchingStateWithError:]_block_invoke.58
- ___block_descriptor_tmp.170
- ___block_literal_global.170
- ___block_literal_global.172
- ___block_literal_global.82
- ___block_literal_global.87
- _copy_raw_secret
- _fv_init_cred_from_secret
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "\tInteractiveAuthForceModalPresentation: %d\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestCheckClass failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestLastUser failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEKWK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewKey failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestRewrapEK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapEK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapKey failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected output count %u (expected: 1)%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected output count %u (expected: 3)%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unpack data failed%s\n"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/backup_serialize.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/shared_crypto.c"
+ "ADPHealingPCS"
+ "BEGIN [%lld]: ADPHealingPCS  enableTelemetry=YES "
+ "BEGIN [%lld]: GeneratePDPBlob  enableTelemetry=YES "
+ "BEGIN [%lld]: GeneratePDPBlobPCS  enableTelemetry=YES "
+ "CloudServices"
+ "CloudServices/DBR_TWO = %{BOOL}d"
+ "DBR_TWO"
+ "END [%lld] %fs: ADPHealingPCS  Error=%{public,signpost.telemetry:number1,name=Error}d "
+ "END [%lld] %fs: GeneratePDPBlob  Error=%{public,signpost.telemetry:number1,name=Error}d "
+ "END [%lld] %fs: GeneratePDPBlobPCS  Error=%{public,signpost.telemetry:number1,name=Error}d "
+ "GeneratePDPBlob"
+ "GeneratePDPBlobPCS"
+ "PCSAccountHealWalrusState"
+ "PDP"
+ "PDP blob generation completed with blob length=%lu error=%@"
+ "Requesting PDP blob generation..."
+ "T@\"NSData\",C,N,V_srpVerifier"
+ "TB,N,V_interactiveAuthForceModalPresentation"
+ "XPC Error while generating PDP blob: %@"
+ "_interactiveAuthForceModalPresentation"
+ "_performPDPBlobGenerationWithCompletionHandler:"
+ "_srpVerifier"
+ "akstest_check_class"
+ "akstest_last_user"
+ "akstest_new_ek"
+ "akstest_new_ekwk"
+ "akstest_new_key"
+ "akstest_rewrap_ek"
+ "akstest_unwrap_ek"
+ "akstest_unwrap_key"
+ "base64Encoding"
+ "cdp/pdp-blob-generation"
+ "cdp_isPDPPasswordRequiredError"
+ "com.apple.corecdp.adp.healing"
+ "generatePDPBlob called with parameters: %@"
+ "generatePDPBlob:completion:"
+ "generatePDPBlobWithCompletion:"
+ "generatePDPBlobWithContext:completion:"
+ "healBrokenADPEnablement called with accountIdentifier: %@, parameters: %@"
+ "healBrokenADPEnablementWithAccountIdentifier:parameters:completion:"
+ "interactiveAuthForceModalPresentation"
+ "isDBRTwoEnabled"
+ "pdpPCSDBRRepairIdentities:completion:"
+ "setInteractiveAuthForceModalPresentation:"
+ "setSrpVerifier:"
+ "srpVerifier"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?B@\"NSError\">32"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/backup_serialize.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/shared_crypto.c"
- "Creating context for CDP & PDP Repair CFU"
- "contextForCDPPDPStateRepair"
- "kCDPPDPStateRepair"
- "pdpPCSGuitarfishRepairIdentities:completion:"
- "v32@0:8@\"NSDictionary\"16@?<v@?Q@\"NSError\">24"

```
