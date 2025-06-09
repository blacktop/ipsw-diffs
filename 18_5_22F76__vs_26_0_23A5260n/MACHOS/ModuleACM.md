## ModuleACM

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/ModulePlugins/ModuleACM.bundle/ModuleACM`

```diff

-1656.120.6.0.0
-  __TEXT.__text: 0x1f728
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_stubs: 0x22e0
-  __TEXT.__objc_methlist: 0x470
-  __TEXT.__const: 0x1d8
-  __TEXT.__gcc_except_tab: 0x534
-  __TEXT.__cstring: 0x26fc
-  __TEXT.__objc_methname: 0x25a5
-  __TEXT.__oslogstring: 0xa30
+2005.0.13.0.0
+  __TEXT.__text: 0x21ec4
+  __TEXT.__auth_stubs: 0x770
+  __TEXT.__objc_stubs: 0x2520
+  __TEXT.__objc_methlist: 0x4a4
+  __TEXT.__const: 0x2b8
+  __TEXT.__gcc_except_tab: 0x544
+  __TEXT.__cstring: 0x2b3e
+  __TEXT.__objc_methname: 0x2761
+  __TEXT.__oslogstring: 0xbf3
   __TEXT.__objc_classname: 0x56
   __TEXT.__ustring: 0x1e
-  __TEXT.__objc_methtype: 0x5ee
+  __TEXT.__objc_methtype: 0x62a
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__unwind_info: 0x5d0
-  __DATA_CONST.__auth_got: 0x368
-  __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xb00
+  __TEXT.__unwind_info: 0x618
+  __DATA_CONST.__auth_got: 0x3c8
+  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__const: 0xb78
   __DATA_CONST.__cfstring: 0x1460
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_intobj: 0x510
+  __DATA_CONST.__objc_intobj: 0x4c8
   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x4f8
-  __DATA.__objc_selrefs: 0x968
+  __DATA.__objc_selrefs: 0xa18
   __DATA.__objc_ivar: 0x48
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x2
-  __DATA.__bss: 0x88
-  __DATA.__common: 0x8
+  __DATA.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
-  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A7ADFFA5-452A-3716-ABF1-6D7AA3145C85
-  Functions: 522
-  Symbols:   384
-  CStrings:  1004
+  UUID: 02C2E838-93D4-3D99-B70F-08E168C4EA9A
+  Functions: 577
+  Symbols:   424
+  CStrings:  1073
 
Symbols:
+ _ACMContextCopyData
+ _ACMContextCreateWithFlags
+ _ACMDecryptData
+ _ACMDecryptDataEx
+ _ACMEncryptData
+ _ACMEncryptDataEx
+ _LACEntitlementExtractCredential
+ _LACEntitlementPasscodeServices
+ _LACEntitlementSaveExtractableCredential
+ _LACErrorCodeDenied
+ _LibCall_ACMContextContainsCredentialTypeEx
+ _LibCall_ACMContextCopyData
+ _LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx
+ _LibSer_ACMDeserializeEnvironmentVariableType
+ _LibSer_ACMDeserializeSEPControlCode
+ _LibSer_GetSerializedContainsCredential_GetSize
+ _LibSer_GetSerializedContainsCredential_Serialize
+ _OBJC_CLASS_$_LACACMHelper
+ _OBJC_CLASS_$_LACACMPoolsInfo
+ _OBJC_CLASS_$_LACContextCredentialCoder
+ _OBJC_CLASS_$_LACFlags
+ _OBJC_CLASS_$_LACManagedACMParameters
+ _OBJC_CLASS_$_LACMutablePasscodeVerificationRequest
+ _OBJC_CLASS_$_LACPasscodeHelper
+ _acm_mem_alloc_typed
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
+ _crypto_decryptText
+ _crypto_deriveKeyAndDecryptData
+ _crypto_deriveKeyAndEncryptData
+ _crypto_encryptText
+ _crypto_encryptedTextLength
+ _crypto_generateKey
+ _crypto_generateKeyFromSharedInfo
+ _crypto_generateRandomSaltLazily
+ _crypto_plainTextLength
+ _strlen
- _LACDTBiometryWatchdogGlobalFallbackTime
- _LACPolicyLocationBasedTrustComputer
- _OBJC_CLASS_$_LAACMHelper
- _OBJC_CLASS_$_LACLocalizationUtils
- _OBJC_CLASS_$_LAManagedACMParameters
- _acm_mem_alloc
- _gAllocatedBytes
CStrings:
+ "%s: %s: CS[%u] created (flags=0x%x).\n"
+ "%s: %s: CS[%u] deleted (contextDestroyed=%s).\n"
+ "%s: %s: CoreCrypto - %s() failed, ccErr: %d.\n"
+ "%s: %s: CoreCrypto - %s() succeeded, ccErr: %d.\n"
+ "@\"LACACMHelper\""
+ "@\"LACMutablePasscodeVerificationRequest\"8@?0"
+ "@\"LACSecureData\"8@?0"
+ "@36@0:8^{__ACMHandle=}16B24q28"
+ "@44@0:8^{__ACMHandle=}16B24q28@36"
+ "ACMContextCopyData"
+ "ACMContextCreateWithFlags"
+ "ACMRequirement - ACMRequirementDataPushButton"
+ "Disposable pool has no free slots: %{public}@"
+ "Extracting a LACredentialTypeExtractablePassword will require the '%@' entitlement in Luckier (rdar://140411675)"
+ "LAContext allocations exceeded non-disposable pool size"
+ "LibCall_ACMContextContainsCredentialTypeEx"
+ "LibCall_ACMContextCopyData"
+ "LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx"
+ "LibSer_ACMDeserializeEnvironmentVariableType"
+ "LibSer_ACMDeserializeSEPControlCode"
+ "LibSerialization.c"
+ "Missing required credential entitlements"
+ "NO"
+ "No free slots for a new LAContext in the non-disposable pool: %{public}@"
+ "Stashing a LACredentialTypeExtractablePassword will require the '%@' entitlement in Luckier (rdar://140411675)"
+ "Untracking proxy:%{public}@ from plugin:%{public}@[%u] (%{public}@)"
+ "YES"
+ "_pluginForACMContext:contextOwner:flags:"
+ "acm_transport"
+ "cc_cmp_safe"
+ "ccgcm_finalize"
+ "ccgcm_init"
+ "ccgcm_set_iv"
+ "ccgcm_update"
+ "cchkdf"
+ "ccrng"
+ "checkCCError"
+ "checkCredentialRequiresEncoding:"
+ "cleanup"
+ "com.apple.private.LocalAuthentication.PasscodeStashSecret"
+ "contextPluginWithExternalizedContext:flags:reply:"
+ "credentialEncodingSeedWithReply:"
+ "credentialsUUIDWithOriginator:reply:"
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
+ "data"
+ "dataWithType:encoded:error:"
+ "dataWithType:error:"
+ "disposable"
+ "disposablePool"
+ "false"
+ "featureFlagExtractableCredentialProtectionEnabled"
+ "freeForLA"
+ "generateRandom"
+ "getRequirementDataSizeForVersion"
+ "getUUIDBytes:"
+ "hasDataWithType:error:"
+ "initWithACMContext:contextOwner:flags:module:"
+ "initWithContextOwner:underlyingPtr:flags:moduleRef:"
+ "initWithPasscode:acmContext:rawAuditToken:"
+ "isDTOPolicy:options:"
+ "isPurposeSecureUIRecording"
+ "nonDisposablePool"
+ "platform_rng"
+ "requirement"
+ "reservedForLA"
+ "setBioLockoutRecovery:"
+ "setCredentialsUUID:originator:reply:"
+ "setData:type:encoded:error:"
+ "setOptions:"
+ "setPolicy:"
+ "setSecretForPasscodeStash:error:"
+ "setUserId:"
+ "untrackProxy:fromPlugin:reason:"
+ "v40@0:8@16@24@32"
+ "v40@0:8@16@24@?32"
+ "v40@0:8@16q24@?32"
+ "verifyPasscode:"
- "%s: %s: CS[%u] %s.\n"
- "%s: %s: CS[%u] created.\n"
- "@\"LAACMHelper\""
- "@28@0:8^{__ACMHandle=}16B24"
- "@36@0:8^{__ACMHandle=}16B24@28"
- "ACMContextCreate"
- "AUTHENTICATE_TO_RETRY_FACE_ID"
- "AUTHENTICATE_TO_RETRY_TOUCH_ID"
- "Enter Passcode"
- "_pluginForACMContext:contextOwner:"
- "addExtractablePassphrase:scope:error:"
- "contextPluginWithExternalizedContext:reply:"
- "credentialOfType:property:error:"
- "deleted"
- "destroyed"
- "encodeLocalizationKey:"
- "initWithACMContext:contextOwner:module:"
- "initWithContextOwner:underlyingPtr:moduleRef:"
- "isLocationBasedPolicy:"
- "verifyPasswordUsingAKS:acmContext:userId:policy:options:bioLockoutRecovery:"

```
