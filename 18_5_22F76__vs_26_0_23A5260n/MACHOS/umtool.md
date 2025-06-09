## umtool

> `/usr/bin/umtool`

```diff

-417.100.1.0.0
-  __TEXT.__text: 0x47a4
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_stubs: 0x10c0
-  __TEXT.__objc_methlist: 0x340
-  __TEXT.__const: 0x48
-  __TEXT.__cstring: 0xcab
+452.0.0.0.0
+  __TEXT.__text: 0x16344
+  __TEXT.__auth_stubs: 0x520
+  __TEXT.__objc_stubs: 0x10e0
+  __TEXT.__objc_methlist: 0x358
+  __TEXT.__const: 0x148
+  __TEXT.__cstring: 0x2810
   __TEXT.__objc_classname: 0x4f
-  __TEXT.__objc_methname: 0xaf8
+  __TEXT.__objc_methname: 0xb37
   __TEXT.__objc_methtype: 0xb3
-  __TEXT.__gcc_except_tab: 0x10c
-  __TEXT.__unwind_info: 0x128
-  __DATA_CONST.__auth_got: 0x1b8
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0xd0
-  __DATA_CONST.__cfstring: 0x1440
+  __TEXT.__gcc_except_tab: 0x150
+  __TEXT.__oslogstring: 0x190
+  __TEXT.__unwind_info: 0x3a8
+  __DATA_CONST.__auth_got: 0x2a0
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__const: 0xf8
+  __DATA_CONST.__cfstring: 0x1460
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0xa0
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA.__objc_const: 0x438
-  __DATA.__objc_selrefs: 0x4d8
+  __DATA.__objc_selrefs: 0x4f0
   __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x68
-  __DATA.__bss: 0x28
+  __DATA.__data: 0x6a
+  __DATA.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 87EB476E-0B5D-3866-8CEB-5E4F15D1DCFA
-  Functions: 66
-  Symbols:   80
-  CStrings:  509
+  UUID: 755558AA-EAB3-3726-A897-B1631A279976
+  Functions: 443
+  Symbols:   114
+  CStrings:  740
 
Symbols:
+ _IOConnectCallScalarMethod
+ _IOConnectCallStructMethod
+ _IOObjectRelease
+ _IOServiceGetMatchingService
+ _IOServiceMatching
+ _IOServiceOpen
+ _OBJC_CLASS_$_NSData
+ ___assert_rtn
+ ___chkstk_darwin
+ ___memcpy_chk
+ __os_log_default
+ __os_log_impl
+ _cc_clear
+ _cc_cmp_safe
+ _ccaes_gcm_decrypt_mode
+ _ccaes_gcm_encrypt_mode
+ _ccgcm_context_size
+ _ccgcm_finalize
+ _ccgcm_init
+ _ccgcm_set_iv
+ _ccgcm_update
+ _cchkdf
+ _ccrng
+ _ccsha256_di
+ _kIOMasterPortDefault
+ _mach_task_self_
+ _malloc_type_calloc
+ _memcmp
+ _memcpy
+ _memset_s
+ _objc_release_x1
+ _os_log_type_enabled
+ _strlen
+ _strnlen
CStrings:
+ "%02x "
+ "%s: %s (len=%u): acl:"
+ "%s: %s (len=%u): operation:"
+ "%s: %s: CS[%u] acquired.\n"
+ "%s: %s: CS[%u] created (flags=0x%x).\n"
+ "%s: %s: CS[%u] deleted (contextDestroyed=%s).\n"
+ "%s: %s: CoreCrypto - %s() failed, ccErr: %d.\n"
+ "%s: %s: CoreCrypto - %s() succeeded, ccErr: %d.\n"
+ "%s: %s: acl = %p, aclLength = %zu.\n"
+ "%s: %s: called.\n"
+ "%s: %s: cmd(%u) on CS[%u] -> err 0x%x (%d).\n"
+ "%s: %s: cmd(%u) on CS[%u] -> ok.\n"
+ "%s: %s: command = %u.\n"
+ "%s: %s: constraintState = %p.\n"
+ "%s: %s: context = %p.\n"
+ "%s: %s: log level set to %d.\n"
+ "%s: %s: maxGlobalCredentialAge = %u.\n"
+ "%s: %s: mem: type=%s ptr=%p size=%u (total=%u raw=%u data=%u types=%u) %s:%d (%s).\n"
+ "%s: %s: operation = %p, operationLength = %zu.\n"
+ "%s: %s: parameters = %p, parameterCount = %u.\n"
+ "%s: %s: requirePasscode = %p.\n"
+ "%s: %s: returning, -> ctx = %p.\n"
+ "%s: %s: returning, err = %ld, code=%u.\n"
+ "%s: %s: returning, err = %ld, var=%u.\n"
+ "%s: %s: returning, err = %ld.\n"
+ "%s: %s: returning.\n"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "0123456789abcdef"
+ "<data>"
+ "ACM"
+ "ACMContextAddCredential"
+ "ACMContextAddCredentialWithScope"
+ "ACMContextContainsCredentialType"
+ "ACMContextContainsCredentialTypeEx"
+ "ACMContextContainsPassphraseCredentialWithPurpose"
+ "ACMContextCopyData"
+ "ACMContextCreateWithExternalForm"
+ "ACMContextCreateWithFlags"
+ "ACMContextCredentialGetProperty"
+ "ACMContextDelete"
+ "ACMContextGetData"
+ "ACMContextGetDataEx"
+ "ACMContextGetDataProperty"
+ "ACMContextGetExternalForm"
+ "ACMContextGetInfo"
+ "ACMContextRemoveCredentialsByType"
+ "ACMContextRemoveCredentialsByTypeAndScope"
+ "ACMContextRemoveCredentialsByValue"
+ "ACMContextRemoveCredentialsByValueAndScope"
+ "ACMContextRemovePassphraseCredentialsByPurposeAndScope"
+ "ACMContextReplacePassphraseCredentialsWithScope"
+ "ACMContextSetData"
+ "ACMContextSetDataEx"
+ "ACMContextVerifyPolicy"
+ "ACMContextVerifyPolicyEx"
+ "ACMContextVerifyPolicyWithPreflight"
+ "ACMCredential"
+ "ACMCredential - ACMCredentialDataAP"
+ "ACMCredential - ACMCredentialDataBiometryMatchAttempted"
+ "ACMCredential - ACMCredentialDataBiometryMatched"
+ "ACMCredential - ACMCredentialDataContinuityUnlock"
+ "ACMCredential - ACMCredentialDataKextDenyList"
+ "ACMCredential - ACMCredentialDataPasscodeValidated"
+ "ACMCredential - ACMCredentialDataPasscodeValidated2"
+ "ACMCredential - ACMCredentialDataPassphraseEntered"
+ "ACMCredential - ACMCredentialDataPassphraseExtractable"
+ "ACMCredential - ACMCredentialDataSecureIntent"
+ "ACMCredential - ACMCredentialDataSignature"
+ "ACMCredential - ACMCredentialDataUserOutputDisplayed"
+ "ACMCredentialGetProperty"
+ "ACMGetAclAuthMethod"
+ "ACMGetEnvironmentVariable"
+ "ACMGlobalContextAddCredential"
+ "ACMGlobalContextCredentialGetProperty"
+ "ACMGlobalContextRemoveCredentialsByType"
+ "ACMGlobalContextVerifyPolicy"
+ "ACMHandleWithPayload"
+ "ACMKernelControl"
+ "ACMLib"
+ "ACMParseAclAndCopyConstraintCharacteristics"
+ "ACMRequirement"
+ "ACMRequirement - ACMRequirementDataAP"
+ "ACMRequirement - ACMRequirementDataAccessGroups"
+ "ACMRequirement - ACMRequirementDataAnd"
+ "ACMRequirement - ACMRequirementDataBiometryMatchAttempted"
+ "ACMRequirement - ACMRequirementDataBiometryMatched"
+ "ACMRequirement - ACMRequirementDataBiometryMatchedWithAttributes"
+ "ACMRequirement - ACMRequirementDataKeyRef"
+ "ACMRequirement - ACMRequirementDataKofN"
+ "ACMRequirement - ACMRequirementDataKofNWithAttributes"
+ "ACMRequirement - ACMRequirementDataOr"
+ "ACMRequirement - ACMRequirementDataPasscodeValidated"
+ "ACMRequirement - ACMRequirementDataPasscodeValidatedWithAttributes"
+ "ACMRequirement - ACMRequirementDataPassphraseEntered"
+ "ACMRequirement - ACMRequirementDataPushButton"
+ "ACMRequirement - ACMRequirementDataPushButtonWithAttributes"
+ "ACMRequirement - ACMRequirementDataRatchet"
+ "ACMRequirement - ACMRequirementDataSecureIntent"
+ "ACMRequirement - ACMRequirementDataSecureStateWithAttributes"
+ "ACMRequirement - ACMRequirementDataUserOutputDisplayed"
+ "ACMRequirementGetProperties"
+ "ACMRequirementGetProperty"
+ "ACMRequirementGetSubrequirements"
+ "ACMSetEnvironmentVariable"
+ "ACMSetEnvironmentVariableWithAccessPolicy"
+ "AppleCredentialManager"
+ "CommonUtil.c"
+ "DeallocCredentialList"
+ "DeserializeCredentialList"
+ "DeserializeProcessAcl"
+ "DeserializeVerifyAclConstraint"
+ "DeserializeVerifyPolicy"
+ "LibCall.c"
+ "LibCall_ACMContexAddCredentialWithScope"
+ "LibCall_ACMContexRemoveCredentialsByTypeAndScope"
+ "LibCall_ACMContextContainsCredentialTypeEx"
+ "LibCall_ACMContextCopyData"
+ "LibCall_ACMContextCreate"
+ "LibCall_ACMContextCreateWithExternalForm"
+ "LibCall_ACMContextCredentialGetProperty"
+ "LibCall_ACMContextDelete"
+ "LibCall_ACMContextGetData"
+ "LibCall_ACMContextGetInfo"
+ "LibCall_ACMContextLoadFromImage"
+ "LibCall_ACMContextRemoveCredentialsByValueAndScope"
+ "LibCall_ACMContextSetData"
+ "LibCall_ACMContextUnloadToImage"
+ "LibCall_ACMContextUnloadToImage_Block"
+ "LibCall_ACMContextVerifyPolicyAndCopyRequirementEx"
+ "LibCall_ACMContextVerifyPolicyEx"
+ "LibCall_ACMContextVerifyPolicyEx_Block"
+ "LibCall_ACMContextVerifyPolicyWithPreflight_Block"
+ "LibCall_ACMGetAclAuthMethod_Block"
+ "LibCall_ACMGetEnvironmentVariable"
+ "LibCall_ACMGetEnvironmentVariable_Block"
+ "LibCall_ACMGlobalContextCredentialGetProperty"
+ "LibCall_ACMGlobalContextCredentialGetProperty_Block"
+ "LibCall_ACMGlobalContextVerifyPolicyEx"
+ "LibCall_ACMGlobalContextVerifyPolicy_Block"
+ "LibCall_ACMKernDoubleClickNotify"
+ "LibCall_ACMKernelControl"
+ "LibCall_ACMKernelControl_Block"
+ "LibCall_ACMPing"
+ "LibCall_ACMPublishTrustedAccessories"
+ "LibCall_ACMRequirementDelete"
+ "LibCall_ACMSEPControl"
+ "LibCall_ACMSEPControl_Block"
+ "LibCall_ACMSecContextGetUnlockSecret"
+ "LibCall_ACMSecContextVerifyAclConstraintAndCopyRequirement"
+ "LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx"
+ "LibCall_ACMSecCredentialProviderEnrollmentStateChangedForUser"
+ "LibCall_ACMSecSetBiometryAvailability"
+ "LibCall_ACMSecSetBuiltinBiometry"
+ "LibCall_ACMSetEnvironmentVariable"
+ "LibCall_ACMTRMLoadState"
+ "LibCall_ACMTRMLoadState_Block"
+ "LibCall_ACMTRMSaveState"
+ "LibCall_BuildCommand"
+ "LibSer_ACMDeserializeEnvironmentVariableType"
+ "LibSer_ACMDeserializeSEPControlCode"
+ "LibSerialization.c"
+ "NO"
+ "NULL"
+ "Util_AllocCredential"
+ "Util_AllocRequirement"
+ "Util_CreateRequirement"
+ "Util_DeallocCredential"
+ "Util_DeallocRequirement"
+ "Util_ReadFromBuffer"
+ "Util_SafeDeallocParameters"
+ "Util_WriteToBuffer"
+ "Util_hexDumpToStrHelper"
+ "YES"
+ "aclRequiresPasscodeInternal"
+ "acm_mem_alloc_info"
+ "acm_mem_free_info"
+ "acm_transport"
+ "array of ACMCredentialRef"
+ "array of ACMParameter"
+ "cc_cmp_safe"
+ "ccgcm_finalize"
+ "ccgcm_init"
+ "ccgcm_set_iv"
+ "ccgcm_update"
+ "cchkdf"
+ "ccrng"
+ "checkCCError"
+ "commandCursor == commandBuffer + sizeof(commandBuffer)"
+ "crypto_decryptText"
+ "crypto_decryptText_version1"
+ "crypto_decryptText_version2"
+ "crypto_deriveKeyAndDecryptData"
+ "crypto_deriveKeyAndEncryptData"
+ "crypto_encryptText"
+ "crypto_encryptText_version1"
+ "crypto_encryptText_version2"
+ "crypto_generateKey"
+ "crypto_generateKeyFromSharedInfo"
+ "crypto_generateKeyFromSharedInfo_version1"
+ "crypto_generateKeyFromSharedInfo_version2"
+ "crypto_generateRandomSaltLazily"
+ "deserializeParameters"
+ "dst || !dstCapacity"
+ "generateRandom"
+ "getACMNilPasscodeData"
+ "getACMPasscodeData"
+ "getLengthOfParameters"
+ "getRequirementDataSizeForVersion"
+ "init"
+ "initWithBytes:length:"
+ "ioKitTransport"
+ "performCommand"
+ "platform_rng"
+ "processAclCommandInternal"
+ "processAclInternal"
+ "quiet"
+ "requirement"
+ "serializeParameters"
+ "src || !srcLen"
+ "updateLogLevelFromKext"
+ "v24@?0r^v8Q16"
+ "verifyAclConstraintForOperationCommandInternal"
+ "verifyAclConstraintInternal"

```
