## NetworkServiceProxy

> `/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy`

```diff

-919.0.0.0.0
-  __TEXT.__text: 0x4fcd4
-  __TEXT.__auth_stubs: 0xde0
-  __TEXT.__objc_methlist: 0x4b34
+921.40.2.0.0
+  __TEXT.__text: 0x51d44
+  __TEXT.__auth_stubs: 0xd50
+  __TEXT.__objc_methlist: 0x4c34
   __TEXT.__const: 0x360
   __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__cstring: 0x5282
-  __TEXT.__oslogstring: 0x2e56
-  __TEXT.__unwind_info: 0xe40
-  __TEXT.__objc_classname: 0x606
-  __TEXT.__objc_methname: 0x96d4
-  __TEXT.__objc_methtype: 0x12ea
-  __TEXT.__objc_stubs: 0x5180
-  __DATA_CONST.__got: 0x3c8
-  __DATA_CONST.__const: 0xc18
+  __TEXT.__cstring: 0x5619
+  __TEXT.__oslogstring: 0x305e
+  __TEXT.__unwind_info: 0xe58
+  __TEXT.__objc_classname: 0x607
+  __TEXT.__objc_methname: 0x9aaa
+  __TEXT.__objc_methtype: 0x1391
+  __TEXT.__objc_stubs: 0x53a0
+  __DATA_CONST.__got: 0x3d8
+  __DATA_CONST.__const: 0xc40
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22f8
+  __DATA_CONST.__objc_selrefs: 0x23b8
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x708
+  __AUTH_CONST.__auth_got: 0x6c0
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x4b00
-  __AUTH_CONST.__objc_const: 0x6600
+  __AUTH_CONST.__cfstring: 0x4b20
+  __AUTH_CONST.__objc_const: 0x6798
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0xe60
-  __DATA.__objc_ivar: 0x2cc
+  __DATA.__objc_ivar: 0x2e0
   __DATA.__data: 0x268
   __DATA.__common: 0x1
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_ivar: 0x234
+  __DATA_DIRTY.__objc_ivar: 0x240
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0xa8
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/libboringssl.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 36E58BD0-B7E3-37FC-A424-5C9DEA91A350
-  Functions: 1689
-  Symbols:   5016
-  CStrings:  3610
+  UUID: 3912FFE1-2BE7-3360-B676-B88827BCE9F5
+  Functions: 1710
+  Symbols:   5074
+  CStrings:  3662
 
Symbols:
+ -[NSPPrivacyProxyProxyInfo hasProxyIndex]
+ -[NSPPrivacyProxyProxyInfo proxyIndex]
+ -[NSPPrivacyProxyProxyInfo setHasProxyIndex:]
+ -[NSPPrivacyProxyProxyInfo setProxyIndex:]
+ -[NSPPrivacyProxyTokenKey hasMetadataSize]
+ -[NSPPrivacyProxyTokenKey hasTokenType]
+ -[NSPPrivacyProxyTokenKey metadataSize]
+ -[NSPPrivacyProxyTokenKey setHasMetadataSize:]
+ -[NSPPrivacyProxyTokenKey setHasTokenType:]
+ -[NSPPrivacyProxyTokenKey setMetadataSize:]
+ -[NSPPrivacyProxyTokenKey setTokenType:]
+ -[NSPPrivacyProxyTokenKey tokenType]
+ -[NSPPrivateAccessTokenChallenge challengeDataForTokenType:issuerName:redemptionContext:originInfo:credentialContext:]
+ -[NSPPrivateAccessTokenChallenge credentialContext]
+ -[NSPPrivateAccessTokenChallenge initARCChallengeWithIssuerName:redemptionContext:originNames:credentialContext:]
+ -[NSPPrivateAccessTokenChallenge initWithType:issuerName:redemptionContext:originNames:credentialContext:]
+ -[NSPPrivateAccessTokenChallenge redemptionContext]
+ -[NSPPrivateAccessTokenFetcher fetchTokenAndAuxiliaryAuthenticationWithQueue:completionHandler:]
+ -[NSPPrivateAccessTokenFetcher initWithChallenge:tokenKey:auxiliaryAuthenticationChallenge:auxiliaryAuthenticationKey:auxiliaryAuthenticationLabel:]
+ -[NSPPrivateAccessTokenFetcher metadataSize]
+ -[NSPPrivateAccessTokenFetcher setMetadataSize:]
+ -[NSPPrivateAccessTokenRequest initWithChallenge:tokenKey:tokenKeyID:originNameKey:selectedOrigin:blindedMessage:]
+ -[NSPPrivateAccessTokenResponse initWithChallenge:nonce:tokenKey:keyID:authenticator:]
+ -[NSPServerClient fetchPrivateAccessTokenAndAuxAuthWithFetcher:allowRetry:completionHandler:]
+ _OBJC_CLASS_$_ARCAwaitingActivation
+ _OBJC_CLASS_$_ATHMAwaitingActivation
+ _OBJC_IVAR_$_NSPPrivateAccessTokenChallenge._credentialContext
+ _OBJC_IVAR_$_NSPPrivateAccessTokenChallenge._redemptionContext
+ _OBJC_IVAR_$_NSPPrivateAccessTokenFetcher._auxiliaryAuthenticationChallengeData
+ _OBJC_IVAR_$_NSPPrivateAccessTokenFetcher._auxiliaryAuthenticationKey
+ _OBJC_IVAR_$_NSPPrivateAccessTokenFetcher._auxiliaryAuthenticationLabel
+ _OBJC_IVAR_$_NSPPrivateAccessTokenFetcher._metadataSize
+ ___70-[NSPPrivateAccessTokenFetcher fetchTokenWithQueue:completionHandler:]_block_invoke.171
+ ___74-[NSPPrivateAccessTokenFetcher fetchTokenPairWithQueue:completionHandler:]_block_invoke.173
+ ___80-[NSPPrivateAccessTokenFetcher fetchLinkedTokenPairWithQueue:completionHandler:]_block_invoke.175
+ ___80-[NSPPrivateAccessTokenFetcher handleTokenResponse:withQueue:completionHandler:]_block_invoke.209
+ ___83-[NSPPrivateAccessTokenFetcher checkRemainingCostQuotaWithQueue:completionHandler:]_block_invoke.210
+ ___87-[NSPPrivateAccessTokenFetcher generateTokenRequestForKey:withQueue:completionHandler:]_block_invoke.194
+ ___87-[NSPPrivateAccessTokenFetcher generateTokenRequestForKey:withQueue:completionHandler:]_block_invoke.198
+ ___93-[NSPServerClient fetchPrivateAccessTokenAndAuxAuthWithFetcher:allowRetry:completionHandler:]_block_invoke
+ ___96-[NSPPrivateAccessTokenFetcher fetchTokenAndAuxiliaryAuthenticationWithQueue:completionHandler:]_block_invoke
+ ___96-[NSPPrivateAccessTokenFetcher fetchTokenAndAuxiliaryAuthenticationWithQueue:completionHandler:]_block_invoke.176
+ ___block_descriptor_48_e8_32s40bs_e39_v32?0"NSData"8"NSData"16"NSError"24ls32l8s40l8
+ _objc_msgSend$activateWithResponseData:error:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$credentialContext
+ _objc_msgSend$fetchPrivateAccessTokenAndAuxAuthWithFetcher:allowRetry:completionHandler:
+ _objc_msgSend$getCredentialDataError:
+ _objc_msgSend$initWithKeyCommitmentsData:nbuckets:deploymentID:error:
+ _objc_msgSend$initWithRequestContext:serverPublicKey:error:
+ _objc_msgSend$keyId
+ _objc_msgSend$metadataSize
+ _objc_msgSend$presentationData
+ _objc_msgSend$redemptionContext
+ _objc_msgSend$requestData
+ _objc_msgSend$setMetadataSize:
+ _objc_msgSend$setTokenType:
+ _objc_msgSend$subdataWithRange:
+ _objc_msgSend$tokenContent
+ _objc_msgSend$verifyAndGetKeyIDFromKeyCommitmentsData:numBuckets:deploymentID:
- -[NSPPrivateAccessTokenChallenge challengeDataForTokenType:issuerName:redemptionNonce:originInfo:]
- -[NSPPrivateAccessTokenChallenge initWithType:issuerName:redemptionNonce:originNames:]
- -[NSPPrivateAccessTokenRequest initWithChallenge:tokenKey:originNameKey:selectedOrigin:blindedMessage:]
- _OBJC_IVAR_$_NSPPrivateAccessTokenChallenge._redemptionNonce
- ___70-[NSPPrivateAccessTokenFetcher fetchTokenWithQueue:completionHandler:]_block_invoke.164
- ___74-[NSPPrivateAccessTokenFetcher fetchTokenPairWithQueue:completionHandler:]_block_invoke.166
- ___80-[NSPPrivateAccessTokenFetcher fetchLinkedTokenPairWithQueue:completionHandler:]_block_invoke.168
- ___80-[NSPPrivateAccessTokenFetcher handleTokenResponse:withQueue:completionHandler:]_block_invoke.196
- ___80-[NSPPrivateAccessTokenFetcher handleTokenResponse:withQueue:completionHandler:]_block_invoke.198
- ___80-[NSPPrivateAccessTokenFetcher handleTokenResponse:withQueue:completionHandler:]_block_invoke.202
- ___83-[NSPPrivateAccessTokenFetcher checkRemainingCostQuotaWithQueue:completionHandler:]_block_invoke.203
- ___87-[NSPPrivateAccessTokenFetcher generateTokenRequestForKey:withQueue:completionHandler:]_block_invoke.181
- ___87-[NSPPrivateAccessTokenFetcher generateTokenRequestForKey:withQueue:completionHandler:]_block_invoke.185
- ___87-[NSPPrivateAccessTokenFetcher generateTokenRequestForKey:withQueue:completionHandler:]_block_invoke.189
- _ccaes_gcm_decrypt_mode
- _ccgcm_one_shot
- _cchkdf_expand
- _cchkdf_extract
- _cchpke_initiator_export
- _cchpke_params_sizeof_aead_key
- _cchpke_params_sizeof_aead_nonce
- _cchpke_params_sizeof_kdf_hash
- _ccsha256_di
CStrings:
+ "%s called with null (clientNonceArray.count == tokenWaitingActivationList.count)"
+ "%s called with null (clientNonceArray.count >= unactivatedListFromServer.count)"
+ "%s called with null (contentArray.count == tokenCount)"
+ "%s called with null (credentialContext.length == 32)"
+ "%s called with null (redemptionContext.length == 32)"
+ "%s called with null (waitingTokenList.count > 0)"
+ "%s called with null activation"
+ "%s called with null auxiliaryAuthenticationChallenge"
+ "%s called with null keyIDData"
+ "%s called with null self.isARC"
+ "%s called with null waitingTokenList"
+ ")!"
+ "+[NSPPrivateAccessTokenFetcher activateTokens:challenge:tokenKey:clientNonceArray:unactivatedListFromServer:]"
+ "+[NSPPrivateAccessTokenFetcher createARCTokenRequestsWithChallenge:tokenKey:waitingTokenList:]"
+ "+[NSPPrivateAccessTokenFetcher createATHMTokenRequestsWithChallenge:tokenKey:tokenCount:waitingTokenList:]"
+ "+[NSPPrivateAccessTokenFetcher createBlindRSATokenRequestsWithChallenge:tokenKey:tokenCount:originNameKey:selectedOrigin:waitingTokenList:clientNonceArray:clientSaltArray:longLivedToken:]"
+ "+[NSPPrivateAccessTokenFetcher generateTokensUsingTokenBlinder:contentArray:waitingTokenList:tokenCount:]"
+ "-[NSPPrivateAccessTokenChallenge credentialRequestContextForKeyID:]"
+ "-[NSPPrivateAccessTokenChallenge initARCChallengeWithIssuerName:redemptionContext:originNames:credentialContext:]"
+ "-[NSPPrivateAccessTokenChallenge initWithType:issuerName:redemptionContext:originNames:credentialContext:]"
+ "-[NSPPrivateAccessTokenFetcher fetchTokenAndAuxiliaryAuthenticationWithQueue:completionHandler:]"
+ "-[NSPPrivateAccessTokenFetcher initWithChallenge:tokenKey:auxiliaryAuthenticationChallenge:auxiliaryAuthenticationKey:auxiliaryAuthenticationLabel:]"
+ "-[NSPPrivateAccessTokenRequest initWithChallenge:tokenKey:tokenKeyID:originNameKey:selectedOrigin:blindedMessage:]"
+ "-[NSPPrivateAccessTokenResponse initWithChallenge:nonce:tokenKey:keyID:authenticator:]"
+ "@48@0:8@16@24@32@40"
+ "@56@0:8@16@24@32@40@48"
+ "ATHM_TOKEN_REQUEST_RESPONSE"
+ "Challenges not found"
+ "Failed to fetch private access token and auxiliary authentication: %@"
+ "Fetching Private Access Token and Auxiliary Authentication"
+ "Invalid credential context"
+ "Invalid credential context length %u"
+ "Invalid credential context length %u, cannot fit in %zu"
+ "More unactivated tokens than waiting tokens (%lu != %lu)"
+ "NSPServerAuxiliaryAuthenticationChallenge"
+ "NSPServerHasAuxiliaryAuthenticationChallenges"
+ "NSPServerPrivateAccessTokenMetadataSize"
+ "TI,N,V_metadataSize"
+ "TI,N,V_tokenType"
+ "TI,V_metadataSize"
+ "_auxiliaryAuthenticationChallengeData"
+ "_auxiliaryAuthenticationKey"
+ "_auxiliaryAuthenticationLabel"
+ "_credentialContext"
+ "_metadataSize"
+ "_redemptionContext"
+ "activateToken failed with error %@"
+ "activateWithResponseData failed with error %@"
+ "activateWithResponseData:error:"
+ "arrayWithObjects:count:"
+ "credentialContext"
+ "fetchPrivateAccessTokenAndAuxAuthWithFetcher:allowRetry:completionHandler:"
+ "fetchTokenAndAuxiliaryAuthenticationWithQueue:completionHandler:"
+ "getCredentialDataError:"
+ "hasMetadataSize"
+ "hasTokenType"
+ "initARCChallengeWithIssuerName:redemptionContext:originNames:credentialContext:"
+ "initWithChallenge:tokenKey:auxiliaryAuthenticationChallenge:auxiliaryAuthenticationKey:auxiliaryAuthenticationLabel:"
+ "initWithKeyCommitmentsData:nbuckets:deploymentID:error:"
+ "initWithRequestContext:serverPublicKey:error:"
+ "keyId"
+ "metadataSize"
+ "presentationData"
+ "redemptionContext"
+ "requestData"
+ "setHasMetadataSize:"
+ "setHasTokenType:"
+ "setMetadataSize:"
+ "setTokenType:"
+ "subdataWithRange:"
+ "tokenContent"
+ "tokenWaitingActivationWithContent failed with error %@"
+ "v32@?0@\"NSData\"8@\"NSData\"16@\"NSError\"24"
+ "v36@0:8@\"NSPPrivateAccessTokenFetcher\"16B24@?<v@?@\"NSData\"@\"NSData\"@\"NSError\">28"
+ "verifyAndGetKeyIDFromKeyCommitmentsData:numBuckets:deploymentID:"
+ "{?=\"algorithm\"b1\"proxyIndex\"b1\"fallbackSupportsUDPProxying\"b1\"supportsFallback\"b1\"supportsResumption\"b1}"
+ "{?=\"expiration\"b1\"rotation\"b1\"metadataSize\"b1\"tokenType\"b1}"
- "%s called with null (redemptionNonce.length == 32)"
- "%s called with null (waitingTokens.count > 0)"
- "%s called with null self.hpkeContext"
- "%s called with null self.hpkeEnc"
- "(!"
- "+[NSPPrivateAccessTokenFetcher createTokenRequestsForChallenge:tokenKey:originNameKey:selectedOrigin:waitingTokens:]"
- "+[NSPPrivateAccessTokenFetcher createWaitingTokensForChallenge:tokenKey:pairedToken:clientNonces:clientSalts:tokenCount:]"
- "-[NSPPrivateAccessTokenChallenge initWithType:issuerName:redemptionNonce:originNames:]"
- "-[NSPPrivateAccessTokenRequest decryptResponse:]"
- "-[NSPPrivateAccessTokenRequest initWithChallenge:tokenKey:originNameKey:selectedOrigin:blindedMessage:]"
- "-[NSPPrivateAccessTokenResponse initWithChallenge:nonce:tokenKey:authenticator:]"
- "ATHM_TOKEN_REQUEST"
- "Could not create waiting tokens"
- "Decrypt error: %d"
- "Export error: %d"
- "Extract error: %d"
- "Failed to create token structure, cannot handle token response"
- "Failed to generate waiting tokens, cannot generate token request"
- "Failed to process token response"
- "Failted to activate waiting token, cannot handle token response"
- "Invalid length %zu"
- "Key expand error: %d"
- "Nonce expand error: %d"
- "TokenResponse"
- "_redemptionNonce"
- "nonce"
- "{?=\"algorithm\"b1\"fallbackSupportsUDPProxying\"b1\"supportsFallback\"b1\"supportsResumption\"b1}"
- "{?=\"expiration\"b1\"rotation\"b1}"

```
