## com.apple.accessoryd.matching

> `/System/Library/UserEventPlugins/com.apple.accessoryd.matching.plugin/com.apple.accessoryd.matching`

```diff

-1043.120.6.0.0
-  __TEXT.__text: 0x36830
-  __TEXT.__auth_stubs: 0xf10
+1110.0.0.0.1
+  __TEXT.__text: 0x3861c
+  __TEXT.__auth_stubs: 0xfd0
   __TEXT.__objc_stubs: 0x47c0
   __TEXT.__objc_methlist: 0x1e84
-  __TEXT.__cstring: 0x4411
+  __TEXT.__cstring: 0x4825
   __TEXT.__objc_methname: 0x61df
   __TEXT.__objc_classname: 0x26c
   __TEXT.__objc_methtype: 0xaaa
-  __TEXT.__const: 0x120
-  __TEXT.__oslogstring: 0x3b60
+  __TEXT.__const: 0x200
+  __TEXT.__oslogstring: 0x3b88
   __TEXT.__gcc_except_tab: 0x334
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x8e8
-  __DATA.__auth_got: 0x798
-  __DATA.__got: 0x2e8
-  __DATA.__auth_ptr: 0x10
-  __DATA.__const: 0xe70
-  __DATA.__cfstring: 0x3560
+  __TEXT.__unwind_info: 0x920
+  __DATA.__auth_got: 0x7f8
+  __DATA.__got: 0x2f0
+  __DATA.__auth_ptr: 0x18
+  __DATA.__const: 0xeb0
+  __DATA.__cfstring: 0x35e0
   __DATA.__objc_classlist: 0x98
   __DATA.__objc_catlist: 0x10
   __DATA.__objc_protolist: 0x48

   __DATA.__objc_superrefs: 0x90
   __DATA.__objc_ivar: 0x2fc
   __DATA.__objc_data: 0x5f0
-  __DATA.__objc_arraydata: 0x118
+  __DATA.__objc_arraydata: 0xe8
   __DATA.__objc_arrayobj: 0x90
   __DATA.__objc_intobj: 0x60
   __DATA.__data: 0x39e
-  __DATA.__objc_dictobj: 0x50
-  __DATA.__bss: 0x1b0
-  __DATA.__common: 0x20
+  __DATA.__objc_dictobj: 0x28
+  __DATA.__bss: 0x1b8
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 1BDFF2FB-15ED-3667-A6D6-DACBD4CC9F49
-  Functions: 1244
-  Symbols:   7209
-  CStrings:  2698
+  UUID: EA7146FB-178D-328F-8A28-760258A4648B
+  Functions: 1287
+  Symbols:   7284
+  CStrings:  2741
 
Symbols:
+ _ACCUserDefaultsAccessorydDomain
+ _ACCUserDefaultsKey_DisableAuthFailureTTRForXR
+ _ACCUserDefaultsKey_DisableInductiveAuthTTR
+ _ACCUserDefaultsKey_SysdiagnoseOnInductiveCTAFailure
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
+ _SBUserNotificationHeaderGraphicIconDefinitionKey
+ __block_literal_global.286
+ __block_literal_global.288
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
+ _checkCCError
+ _crypto_decryptText
+ _crypto_decryptText_version1
+ _crypto_decryptText_version2
+ _crypto_deriveKeyAndDecryptData
+ _crypto_deriveKeyAndEncryptData
+ _crypto_encryptText
+ _crypto_encryptText_version1
+ _crypto_encryptText_version2
+ _crypto_encryptedTextLength
+ _crypto_generateKey
+ _crypto_generateKeyFromSharedInfo
+ _crypto_generateRandomSaltLazily
+ _crypto_plainTextLength
+ _generateRandom
+ _getRequirementDataSizeForVersion
+ _kCFACCUserDefaultsAccessorydDomain
+ _kCFACCUserDefaultsKey_DisableAuthFailureTTRForXR
+ _kCFACCUserDefaultsKey_DisableInductiveAuthTTR
+ _kCFACCUserDefaultsKey_SysdiagnoseOnInductiveCTAFailure
+ getRequirementDataSizeForVersion.cold.1
+ getRequirementDataSizeForVersion.cold.2
+ platform_rng.state
- _OUTLINED_FUNCTION_38
- _OUTLINED_FUNCTION_39
- __block_literal_global.274
- __block_literal_global.276
- _acm_mem_alloc
- _gAllocatedBytes
CStrings:
+ "%s: %s: CS[%u] created (flags=0x%x).\n"
+ "%s: %s: CS[%u] deleted (contextDestroyed=%s).\n"
+ "%s: %s: CoreCrypto - %s() failed, ccErr: %d.\n"
+ "%s: %s: CoreCrypto - %s() succeeded, ccErr: %d.\n"
+ "ACMContextCopyData"
+ "ACMContextCreateWithFlags"
+ "ACMRequirement - ACMRequirementDataPushButton"
+ "DisableAuthFailureTTRForXR"
+ "DisableInductiveAuthTTR"
+ "Do you want to connect %@ to this %@?"
+ "Do you want to connect the Thunderbolt accessory to this %@?"
+ "Do you want to connect the USB accessory to this %@?"
+ "Do you want to connect the accessory to this %@?"
+ "LibCall_ACMContextContainsCredentialTypeEx"
+ "LibCall_ACMContextCopyData"
+ "LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx"
+ "LibSer_ACMDeserializeEnvironmentVariableType"
+ "LibSer_ACMDeserializeSEPControlCode"
+ "LibSerialization.c"
+ "SysdiagnoseOnInductiveCTAFailure"
+ "acm_transport"
+ "cc_cmp_safe"
+ "ccgcm_finalize"
+ "ccgcm_init"
+ "ccgcm_set_iv"
+ "ccgcm_update"
+ "cchkdf"
+ "ccrng"
+ "checkCCError"
+ "com.apple.accessoryd"
+ "com.apple.graphic-icon.thunderbolt"
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
+ "platform_rng"
+ "requirement"
- "%s: %s: CS[%u] %s.\n"
- "%s: %s: CS[%u] created.\n"
- "ACMContextCreate"
- "Do you want to connect %@ to this Device?"
- "Do you want to connect the Thunderbolt accessory to this Device?"
- "Do you want to connect the USB accessory to this Device?"
- "Do you want to connect the accessory to this Device?"
- "IconConfiguration"
- "deleted"
- "destroyed"

```
