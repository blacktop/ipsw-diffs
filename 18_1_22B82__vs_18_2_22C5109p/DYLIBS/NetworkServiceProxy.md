## NetworkServiceProxy

> `/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy`

```diff

-834.40.4.0.0
-  __TEXT.__text: 0x93790
-  __TEXT.__auth_stubs: 0x1800
-  __TEXT.__objc_methlist: 0x7630
+845.0.0.0.1
+  __TEXT.__text: 0x999b0
+  __TEXT.__auth_stubs: 0x18f0
+  __TEXT.__objc_methlist: 0x7898
   __TEXT.__const: 0x650
   __TEXT.__gcc_except_tab: 0x1b68
-  __TEXT.__cstring: 0x6da2
-  __TEXT.__oslogstring: 0x78b3
-  __TEXT.__unwind_info: 0x1af8
-  __TEXT.__objc_classname: 0x7af
-  __TEXT.__objc_methname: 0x11eec
-  __TEXT.__objc_methtype: 0x1e9a
-  __TEXT.__objc_stubs: 0xc480
-  __DATA_CONST.__got: 0x588
-  __DATA_CONST.__const: 0x1680
-  __DATA_CONST.__objc_classlist: 0x270
+  __TEXT.__cstring: 0x72f8
+  __TEXT.__oslogstring: 0x8207
+  __TEXT.__unwind_info: 0x1bc0
+  __TEXT.__objc_classname: 0x7d0
+  __TEXT.__objc_methname: 0x1240e
+  __TEXT.__objc_methtype: 0x1f9a
+  __TEXT.__objc_stubs: 0xc760
+  __DATA_CONST.__got: 0x5c8
+  __DATA_CONST.__const: 0x16c8
+  __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3fd8
-  __DATA_CONST.__objc_superrefs: 0x238
+  __DATA_CONST.__objc_selrefs: 0x40d8
+  __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0xc18
+  __AUTH_CONST.__auth_got: 0xc90
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x1270
-  __AUTH_CONST.__cfstring: 0x7820
-  __AUTH_CONST.__objc_const: 0xcdc8
+  __AUTH_CONST.__const: 0x1290
+  __AUTH_CONST.__cfstring: 0x7940
+  __AUTH_CONST.__objc_const: 0xd0b0
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x1590
-  __DATA.__objc_ivar: 0x798
+  __AUTH.__objc_data: 0x15e0
+  __DATA.__objc_ivar: 0x7ac
   __DATA.__data: 0x3b8
   __DATA.__common: 0x24
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_ivar: 0x31c
+  __DATA_DIRTY.__objc_ivar: 0x330
   __DATA_DIRTY.__objc_data: 0x2d0
-  __DATA_DIRTY.__bss: 0x4d8
+  __DATA_DIRTY.__bss: 0x4e8
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3134
-  Symbols:   3824
-  CStrings:  5667
+  Functions: 3201
+  Symbols:   3910
+  CStrings:  5809
 
Symbols:
+ _NSPPrivacyProxyAuxiliaryAuthInfoReadFrom
+ _OBJC_CLASS_$_CKPATKeyBlinding
+ _OBJC_CLASS_$_NSPPrivacyProxyAuxiliaryAuthInfo
+ _OBJC_CLASS_$_RSABSSATokenBlinder
+ _OBJC_CLASS_$_RSABSSATokenWaitingActivation
+ _OBJC_METACLASS_$_NSPPrivacyProxyAuxiliaryAuthInfo
+ _SecKeyCopyPublicKey
+ _ccaes_gcm_decrypt_mode
+ _ccgcm_one_shot
+ _cchkdf_expand
+ _cchkdf_extract
+ _cchpke_initiator_encrypt
+ _cchpke_initiator_export
+ _cchpke_initiator_setup
+ _cchpke_params_sizeof_aead_key
+ _cchpke_params_sizeof_aead_nonce
+ _cchpke_params_sizeof_aead_tag
+ _cchpke_params_sizeof_kdf_hash
+ _cchpke_params_sizeof_kem_enc
+ _cchpke_params_x25519_AESGCM128_HKDF_SHA256
+ _ccsha256_di
- _privacyProxyErrorDomain
CStrings:
+ "\x1e"
+ "%!s(MISSING) called with null (clientNonce.length == 32)"
+ "%!s(MISSING) called with null (waitingTokens.count > 0)"
+ "%!s(MISSING) called with null auxiliaryData"
+ "%!s(MISSING) called with null blindSignature"
+ "%!s(MISSING) called with null blindedMessage"
+ "%!s(MISSING) called with null cacheKey"
+ "%!s(MISSING) called with null challenge.isSupportedTokenType"
+ "%!s(MISSING) called with null challenge.originName"
+ "%!s(MISSING) called with null challengeData"
+ "%!s(MISSING) called with null clientNonce"
+ "%!s(MISSING) called with null issuerEncapKey"
+ "%!s(MISSING) called with null label"
+ "%!s(MISSING) called with null messageToBlind"
+ "%!s(MISSING) called with null self.encryptedTokenRequest"
+ "%!s(MISSING) called with null self.ephemeralPrivateKey"
+ "%!s(MISSING) called with null self.hpkeContext"
+ "%!s(MISSING) called with null self.hpkeEnc"
+ "%!s(MISSING) called with null self.issuerEncapKeyID"
+ "%!s(MISSING) called with null self.requestKey"
+ "%!s(MISSING) called with null token"
+ "%!s(MISSING) called with null tokenBlinder"
+ "%!s(MISSING) called with null tokenRequest"
+ "%!s(MISSING) called with null waitingActivation"
+ "+[NSPPrivateAccessTokenFetcher createTokenRequestsForChallenge:tokenKey:originNameKey:selectedOrigin:waitingTokens:]"
+ "+[NSPPrivateAccessTokenFetcher createWaitingTokensForChallenge:tokenKey:pairedToken:clientNonces:clientSalts:tokenCount:]"
+ "+[NSPPrivateAccessTokenFetcher fetchAuxiliaryAuthenticationDataFromCacheForType:label:cacheKey:completionHandler:]"
+ "+[NSPPrivateAccessTokenFetcher saveAuxiliaryAuthenticationDataToCache:type:forLabel:cacheKey:]"
+ "+[NSPPrivateAccessTokenRequest messageToBlindForChallenge:clientNonce:tokenKey:]"
+ "-[NSPPrivateAccessTokenFetcher saveTokenToCache:]"
+ "-[NSPPrivateAccessTokenRequest decryptResponse:]"
+ "-[NSPPrivateAccessTokenRequest encryptTokenRequest]"
+ "-[NSPPrivateAccessTokenRequest generateRequestSignature]"
+ "-[NSPPrivateAccessTokenRequest initWithChallenge:tokenKey:originNameKey:selectedOrigin:blindedMessage:]"
+ "-[NSPPrivateAccessTokenResponse initWithChallenge:clientNonce:tokenKey:blindSignature:]"
+ "@\"NSObject\""
+ "@\"NSPPrivacyProxyTokenKey\""
+ "@\"NSPPrivateAccessTokenRequest\""
+ "AEAD %!u(MISSING) is not supported"
+ "Adding Private Access Token to cache"
+ "Adding auxiliary authentication data to cache"
+ "Cannot fetch multiple local tokens with a single token fetcher"
+ "ClientBlind"
+ "Config length is too short: %!z(MISSING)u"
+ "Could not create token requests"
+ "Could not create waiting tokens"
+ "Decrypt error: %!d(MISSING)"
+ "Encrypt error: %!d(MISSING)"
+ "Error creating encrypted token request"
+ "Export error: %!d(MISSING)"
+ "Extract error: %!d(MISSING)"
+ "Failed to create token structure, cannot handle token response"
+ "Failed to encrypt the token request"
+ "Failed to find origin name %!@(MISSING) in %!@(MISSING)"
+ "Failed to generate the request key"
+ "Failed to generate the request signature"
+ "Failed to generate token request"
+ "Failed to generate waiting tokens, cannot generate token request"
+ "Failed to parse origin name key"
+ "Failed to process token response"
+ "Failted to activate waiting token, cannot handle token response"
+ "Fetching Private Access Token key"
+ "Fetching auxiliary authentication data from cache"
+ "Generated token from response"
+ "Generated token request"
+ "HPKE"
+ "Invalid length %!z(MISSING)u"
+ "Invalid parameters"
+ "Invalid state, cannot handle token response"
+ "KDF %!u(MISSING) is not supported"
+ "KEM %!u(MISSING) is not supported"
+ "Key expand error: %!d(MISSING)"
+ "NSPPrivacyProxyAuxiliaryAuthInfo"
+ "NSPServerAuxiliaryAuthenticationCacheKey"
+ "NSPServerAuxiliaryAuthenticationData"
+ "NSPServerAuxiliaryAuthenticationLabel"
+ "NSPServerAuxiliaryAuthenticationType"
+ "Nonce expand error: %!d(MISSING)"
+ "RSABSSATokenBlinder initWithPublicKey failed with error %!@(MISSING) for %!@(MISSING)"
+ "Setup error: %!d(MISSING)"
+ "T@\"NSMutableArray\",&,N,V_auxiliaryAuthArrays"
+ "T@\"NSMutableArray\",&,N,V_contentLists"
+ "T@\"NSString\",&,N,V_label"
+ "T@\"NSString\",&,V_auxiliaryAuthenticationCacheKey"
+ "TokenRequest"
+ "TokenResponse"
+ "Unsupported token type"
+ "Unsupported token type, cannot generate token request"
+ "_auxiliaryAuthArrays"
+ "_auxiliaryAuthenticationCacheKey"
+ "_contentLists"
+ "_waitingClientNonce"
+ "_waitingToken"
+ "_waitingTokenKey"
+ "_waitingTokenRequest"
+ "activateTokenWithServerResponse:error:"
+ "addAuxiliaryAuthArray:"
+ "addAuxiliaryAuthenticationData:type:label:cacheKey:"
+ "addContentList:"
+ "addToken:toCacheForFetcher:"
+ "auxiliaryAuthArray"
+ "auxiliaryAuthArrayAtIndex:"
+ "auxiliaryAuthArrayType"
+ "auxiliaryAuthArrays"
+ "auxiliaryAuthArraysCount"
+ "auxiliaryAuthenticationCacheKey"
+ "blindPublicKey:withPrivateKey:context:error:"
+ "blindSignMessage:blindedBy:withKey:context:error:"
+ "blindedMessage"
+ "clearAuxiliaryAuthArrays"
+ "clearContentLists"
+ "compressedRepresentationFromSecKey:"
+ "contentList"
+ "contentListAtIndex:"
+ "contentListType"
+ "contentLists"
+ "contentListsCount"
+ "fetchAuxiliaryAuthenticationDataFromCacheForType:label:cacheKey:completionHandler:"
+ "fetchKnownPrivateAccessTokenKeyWithFetcher:completionHandler:"
+ "generate key: Failed to access stored client key"
+ "generate key: SecKeyCopyPublicKey failed"
+ "generate key: SecKeyCreateRandomKey failed"
+ "generate key: blindPublicKey failed: %!@(MISSING)"
+ "generate key: compressedRepresentationFromSecKey failed"
+ "generate signature: Failed to access stored client key"
+ "generate signature: SecKeyCopyExternalRepresentation failed: %!@(MISSING)"
+ "generate tokens: SecRandomCopyBytes failed"
+ "generateTokenRequestWithQueue:completionHandler:"
+ "handleTokenResponse:withQueue:completionHandler:"
+ "hasLabel"
+ "initWithPublicKey:error:"
+ "nonce"
+ "saveAuxiliaryAuthenticationDataToCache:type:forLabel:cacheKey:"
+ "saveTokenToCache:"
+ "setAuxiliaryAuthArrays:"
+ "setAuxiliaryAuthenticationCacheKey:"
+ "setContentLists:"
+ "tokenWaitingActivationWithContent:error:"
+ "v32@0:8@\"NSData\"16@\"NSPPrivateAccessTokenFetcher\"24"
+ "v48@0:8@\"NSData\"16Q24@\"NSString\"32@\"NSString\"40"
+ "v48@0:8@16Q24@32@40"
+ "v48@0:8Q16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSData\"@\"NSError\">40"
- "\x19"

```
