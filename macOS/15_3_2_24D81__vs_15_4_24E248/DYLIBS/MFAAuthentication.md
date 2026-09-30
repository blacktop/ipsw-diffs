## MFAAuthentication

> `/System/Library/PrivateFrameworks/MFAAuthentication.framework/Versions/A/MFAAuthentication`

```diff

-1025.80.3.0.1
-  __TEXT.__text: 0x26f90
+1043.100.30.0.0
+  __TEXT.__text: 0x27368
   __TEXT.__auth_stubs: 0xbb0
-  __TEXT.__objc_methlist: 0x3b4
-  __TEXT.__const: 0x59c41
+  __TEXT.__objc_methlist: 0x42c
+  __TEXT.__const: 0x59c31
   __TEXT.__cstring: 0x136a
   __TEXT.__gcc_except_tab: 0x120
-  __TEXT.__oslogstring: 0x4385
+  __TEXT.__oslogstring: 0x4369
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x550
+  __TEXT.__unwind_info: 0x5e8
   __TEXT.__objc_classname: 0x6e
   __TEXT.__objc_methname: 0xf89
   __TEXT.__objc_methtype: 0x3dc
   __TEXT.__objc_stubs: 0xec0
-  __DATA_CONST.__got: 0x1f8
+  __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0x2300
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8

   __AUTH_CONST.__auth_got: 0x5e8
   __AUTH_CONST.__const: 0x750
   __AUTH_CONST.__cfstring: 0x15e0
-  __AUTH_CONST.__objc_const: 0x6e8
+  __AUTH_CONST.__objc_const: 0x608
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x140

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A791A74C-6B78-37BD-888B-DB70B6F8BBB3
-  Functions: 625
-  Symbols:   1924
-  CStrings:  935
+  UUID: B055EFC9-AF31-3544-B348-787089964F9A
+  Functions: 646
+  Symbols:   1928
+  CStrings:  934
 
Symbols:
+ +[ACCUserDefaults sharedDefaultsIapd].cold.1
+ +[ACCUserDefaults sharedDefaultsLogging].cold.1
+ +[ACCUserDefaults sharedDefaults].cold.1
+ -[MFAACertificateManager _validateCertificateChain:realtime:error:].cold.30
+ -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.23
+ -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.24
+ -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.25
+ -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.26
+ -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.27
+ MFAACreateCertificateCache.cold.4
+ MFAADeviceIdentityInitCertStates.cold.1
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ __102-[MFAACertificateManager requestMetadataForCertificate:requestedLocale:requestInfo:completionHandler:]_block_invoke.74.cold.10
+ __102-[MFAACertificateManager requestMetadataForCertificate:requestedLocale:requestInfo:completionHandler:]_block_invoke.74.cold.11
+ __102-[MFAACertificateManager requestMetadataForCertificate:requestedLocale:requestInfo:completionHandler:]_block_invoke.74.cold.7
+ __102-[MFAACertificateManager requestMetadataForCertificate:requestedLocale:requestInfo:completionHandler:]_block_invoke.74.cold.8
+ __102-[MFAACertificateManager requestMetadataForCertificate:requestedLocale:requestInfo:completionHandler:]_block_invoke.74.cold.9
+ __MergedGlobals
+ _anchorCertsForComponentAuth.cold.2
+ _findValidIndex.cold.1
+ systemInfo_isDeveloperBuild.cold.1
+ systemInfo_isInternalBuild.cold.1
- -[MFAACertificateManager _validateBAACertificateChain:error:].cold.1
- -[MFAACertificateManager _validateBAACertificateChain:error:].cold.2
- -[MFAACertificateManager _validateBAACertificateChain:error:].cold.3
- -[MFAACertificateManager _validateBAACertificateChain:error:].cold.4
- -[MFAACertificateManager _validateBAACertificateChain:error:].cold.5
- -[MFAACertificateManager _validateX509CertificateChain:anchorCerts:error:].cold.1
- -[MFAACertificateManager _validateX509CertificateChain:anchorCerts:error:].cold.2
- -[MFAACertificateManager _validateX509CertificateChain:anchorCerts:error:].cold.3
- -[MFAACertificateManager _validateX509CertificateChain:anchorCerts:error:].cold.4
- -[MFAACertificateManager verifyNonceSignature:nonce:signature:].cold.18
- MFAAVerifyPublicCertificateChain.cold.1
- MFAAVerifyPublicCertificateChain.cold.2
- MFAAVerifyPublicCertificateChain.cold.3
- MFAAVerifyPublicCertificateChain.cold.4
- MFAAVerifyPublicCertificateChain.cold.5
- MFAAVerifyPublicCertificateChain.cold.6
- __50+[MFAATokenManager isTokenValidForFeatures:token:]_block_invoke.44.cold.1
- __50+[MFAATokenManager isTokenValidForFeatures:token:]_block_invoke.44.cold.2
- __50+[MFAATokenManager isTokenValidForFeatures:token:]_block_invoke.44.cold.3
- __50+[MFAATokenManager isTokenValidForFeatures:token:]_block_invoke.44.cold.4
- __50+[MFAATokenManager isTokenValidForFeatures:token:]_block_invoke.cold.1
- __50+[MFAATokenManager isTokenValidForFeatures:token:]_block_invoke.cold.2
- __50+[MFAATokenManager isTokenValidForFeatures:token:]_block_invoke.cold.3
- __initMFAADeviceIdentity.onceToken
- _anchorCertsForBAAUser.anchorCerts
- _anchorCertsForBAAUser.onceToken
- _gSerialQueue
- _kSecKeyAlgorithmRSASignatureRaw
- mfaa_certificateManager_SWAuthCertType.cold.1
- mfaa_certificateManager_SWAuthCertType.cold.2
- mfaa_certificateManager_SWAuthCertType.cold.3
CStrings:
- "Unsupported authVerMajor %d"

```
