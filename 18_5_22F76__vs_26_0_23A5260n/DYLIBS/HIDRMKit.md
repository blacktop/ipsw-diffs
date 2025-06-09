## HIDRMKit

> `/System/Library/PrivateFrameworks/HIDRMKit.framework/HIDRMKit`

```diff

 21.0.0.0.0
-  __TEXT.__text: 0x221f0
-  __TEXT.__auth_stubs: 0xd90
+  __TEXT.__text: 0x21c04
+  __TEXT.__auth_stubs: 0xe50
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x8d0
-  __TEXT.__cstring: 0x1e15
+  __TEXT.__const: 0x9b0
+  __TEXT.__cstring: 0x21c6
   __TEXT.__constg_swiftt: 0xa6c
   __TEXT.__swift5_typeref: 0x346
   __TEXT.__swift5_reflstr: 0x2ae

   __TEXT.__swift5_proto: 0x54
   __TEXT.__swift5_types: 0x50
   __TEXT.__swift5_capture: 0x64
-  __TEXT.__oslogstring: 0xbbe
+  __TEXT.__oslogstring: 0xbe6
   __TEXT.__gcc_except_tab: 0x10
-  __TEXT.__unwind_info: 0x5e8
-  __TEXT.__eh_frame: 0x220
+  __TEXT.__unwind_info: 0x640
+  __TEXT.__eh_frame: 0x1f8
   __TEXT.__objc_classname: 0x35
   __TEXT.__objc_methname: 0x2d8
   __TEXT.__objc_methtype: 0xad
   __DATA_CONST.__got: 0x158
-  __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x118
   __DATA_CONST.__objc_protorefs: 0x18
-  __AUTH_CONST.__auth_got: 0x6d0
-  __AUTH_CONST.__const: 0x8c0
+  __AUTH_CONST.__auth_got: 0x730
+  __AUTH_CONST.__const: 0x8e8
   __AUTH_CONST.__objc_const: 0x1040
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0xf88
-  __DATA.__data: 0x37a
-  __DATA.__bss: 0x8a0
-  __DATA.__common: 0x90
+  __DATA.__data: 0x372
+  __DATA.__bss: 0x8a8
+  __DATA.__common: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 9BC4AB14-849A-384E-AED7-59EB4F71117F
-  Functions: 675
-  Symbols:   1058
-  CStrings:  368
+  UUID: 80420B54-CEFD-3930-B5A2-6EEFE418664E
+  Functions: 718
+  Symbols:   1151
+  CStrings:  405
 
Symbols:
+ GCC_except_table21
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
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_HIDRMKit
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_HIDRMKit
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_HIDRMKit
+ _acm_mem_alloc_typed
+ _block_copy_helper.66
+ _block_descriptor.68
+ _block_destroy_helper.67
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
+ _getRequirementDataSizeForVersion.cold.1
+ _getRequirementDataSizeForVersion.cold.2
+ _objc_release_x1
+ _objc_retain_x9
+ _platform_rng.state
+ _strlen
- GCC_except_table20
- _OUTLINED_FUNCTION_38
- _OUTLINED_FUNCTION_39
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_HIDRMKit
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_HIDRMKit
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_HIDRMKit
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_HIDRMKit
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_HIDRMKit
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_HIDRMKit
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_HIDRMKit
- _acm_mem_alloc
- _block_copy_helper.67
- _block_descriptor.69
- _block_destroy_helper.68
- _gAllocatedBytes
- _objc_retain_x24
- _objc_retain_x28
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
CStrings:
+ "%s: %s: CS[%u] created (flags=0x%x).\n"
+ "%s: %s: CS[%u] deleted (contextDestroyed=%s).\n"
+ "%s: %s: CoreCrypto - %s() failed, ccErr: %d.\n"
+ "%s: %s: CoreCrypto - %s() succeeded, ccErr: %d.\n"
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
+ "acm_transport"
+ "cc_cmp_safe"
+ "ccgcm_finalize"
+ "ccgcm_init"
+ "ccgcm_set_iv"
+ "ccgcm_update"
+ "cchkdf"
+ "ccrng"
+ "checkCCError"
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
- "deleted"
- "destroyed"

```
