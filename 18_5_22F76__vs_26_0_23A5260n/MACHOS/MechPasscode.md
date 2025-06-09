## MechPasscode

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPasscode.bundle/MechPasscode`

```diff

-1656.120.6.0.0
-  __TEXT.__text: 0x131a4
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0x288
-  __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x1c19
-  __TEXT.__objc_methname: 0xaf2
-  __TEXT.__oslogstring: 0x375
+2005.0.13.0.0
+  __TEXT.__text: 0x150cc
+  __TEXT.__auth_stubs: 0x4e0
+  __TEXT.__objc_stubs: 0xd20
+  __TEXT.__objc_methlist: 0x290
+  __TEXT.__const: 0x198
+  __TEXT.__cstring: 0x1ff7
+  __TEXT.__objc_methname: 0xb5e
+  __TEXT.__oslogstring: 0x39d
   __TEXT.__objc_classname: 0x60
-  __TEXT.__objc_methtype: 0x190
+  __TEXT.__objc_methtype: 0x19b
   __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__unwind_info: 0x380
-  __DATA_CONST.__auth_got: 0x218
-  __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1d8
+  __TEXT.__unwind_info: 0x3b0
+  __DATA_CONST.__auth_got: 0x280
+  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__const: 0x200
   __DATA_CONST.__cfstring: 0x2c0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x8

   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0xc0
   __DATA.__objc_const: 0x498
-  __DATA.__objc_selrefs: 0x388
+  __DATA.__objc_selrefs: 0x3d8
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x6a
-  __DATA.__bss: 0x70
-  __DATA.__common: 0x8
+  __DATA.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 123C4E66-EFEF-3EC7-85EF-DC5547EFAE3C
-  Functions: 394
-  Symbols:   302
-  CStrings:  435
+  UUID: 0EF3F764-1037-3DC6-A55F-1A53FB72456C
+  Functions: 439
+  Symbols:   339
+  CStrings:  484
 
Symbols:
+ _ACMContextCopyData
+ _ACMContextCreateWithFlags
+ _ACMDecryptData
+ _ACMDecryptDataEx
+ _ACMEncryptData
+ _ACMEncryptDataEx
+ _LibCall_ACMContextContainsCredentialTypeEx
+ _LibCall_ACMContextCopyData
+ _LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx
+ _LibSer_ACMDeserializeEnvironmentVariableType
+ _LibSer_ACMDeserializeSEPControlCode
+ _LibSer_GetSerializedContainsCredential_GetSize
+ _LibSer_GetSerializedContainsCredential_Serialize
+ _OBJC_CLASS_$_LACACMHelper
+ _OBJC_CLASS_$_LACInternalInfoParser
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
- _OBJC_CLASS_$_LAACMHelper
- _acm_mem_alloc
- _gAllocatedBytes
CStrings:
+ "%s: %s: CS[%u] created (flags=0x%x).\n"
+ "%s: %s: CS[%u] deleted (contextDestroyed=%s).\n"
+ "%s: %s: CoreCrypto - %s() failed, ccErr: %d.\n"
+ "%s: %s: CoreCrypto - %s() succeeded, ccErr: %d.\n"
+ "@\"LACMutablePasscodeVerificationRequest\"8@?0"
+ "ACMContextCopyData"
+ "ACMContextCreateWithFlags"
+ "ACMRequirement - ACMRequirementDataPushButton"
+ "LibCall_ACMContextContainsCredentialTypeEx"
+ "LibCall_ACMContextCopyData"
+ "LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx"
+ "LibSer_ACMDeserializeEnvironmentVariableType"
+ "LibSer_ACMDeserializeSEPControlCode"
+ "LibSerialization.c"
+ "NO"
+ "YES"
+ "_allowsPasscodeFallback:"
+ "_verifyPasscode:"
+ "acm_transport"
+ "allowsAuthenticationFallbacks"
+ "auditToken"
+ "cc_cmp_safe"
+ "ccgcm_finalize"
+ "ccgcm_init"
+ "ccgcm_set_iv"
+ "ccgcm_update"
+ "cchkdf"
+ "ccrng"
+ "checkCCError"
+ "client"
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
+ "false"
+ "generateRandom"
+ "getRequirementDataSizeForVersion"
+ "initWithInternalInfo:"
+ "initWithPasscode:acmContext:rawAuditToken:"
+ "platform_rng"
+ "q24@0:8@16"
+ "requirement"
+ "setBioLockoutRecovery:"
+ "setOptions:"
+ "setPolicy:"
+ "setUserId:"
+ "userId"
+ "verifyPasscode:"
- "%s: %s: CS[%u] %s.\n"
- "%s: %s: CS[%u] created.\n"
- "ACMContextCreate"
- "_isInFamiliarLocationWithError:"
- "deleted"
- "destroyed"
- "inFamiliarLocation"
- "verifyPasswordUsingAKS:acmContext:userId:policy:options:bioLockoutRecovery:"

```
