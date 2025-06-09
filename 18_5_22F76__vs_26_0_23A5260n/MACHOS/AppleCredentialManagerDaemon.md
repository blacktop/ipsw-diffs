## AppleCredentialManagerDaemon

> `/System/Library/PrivateFrameworks/AppleCredentialManager.framework/AppleCredentialManagerDaemon`

```diff

-758.120.3.0.0
-  __TEXT.__text: 0x128bc
-  __TEXT.__auth_stubs: 0x3f0
+864.0.3.0.0
+  __TEXT.__text: 0x1461c
+  __TEXT.__auth_stubs: 0x4c0
   __TEXT.__objc_stubs: 0x4c0
   __TEXT.__objc_methlist: 0x134
   __TEXT.__objc_methname: 0x3cd
   __TEXT.__objc_classname: 0x2f
   __TEXT.__objc_methtype: 0x92
-  __TEXT.__const: 0x30
-  __TEXT.__cstring: 0x2191
-  __TEXT.__oslogstring: 0x580
-  __TEXT.__unwind_info: 0x300
-  __DATA_CONST.__auth_got: 0x200
+  __TEXT.__const: 0x110
+  __TEXT.__cstring: 0x253c
+  __TEXT.__oslogstring: 0x5a8
+  __TEXT.__unwind_info: 0x328
+  __DATA_CONST.__auth_got: 0x268
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x138
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x10

   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x3
-  __DATA.__bss: 0x48
-  __DATA.__common: 0x8
+  __DATA.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 02CFE1F4-D708-3872-8BA5-6F127D859120
-  Functions: 380
-  Symbols:   88
-  CStrings:  350
+  UUID: BA20A69C-6478-318D-B586-93363051EBD9
+  Functions: 423
+  Symbols:   101
+  CStrings:  385
 
Symbols:
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
+ _strlen
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
