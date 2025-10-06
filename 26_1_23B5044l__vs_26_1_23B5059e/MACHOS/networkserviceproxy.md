## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

-919.0.0.0.0
-  __TEXT.__text: 0xb8044
-  __TEXT.__auth_stubs: 0x18f0
-  __TEXT.__objc_stubs: 0xc300
-  __TEXT.__objc_methlist: 0x4df4
-  __TEXT.__const: 0x321
+921.40.2.0.0
+  __TEXT.__text: 0xba7c4
+  __TEXT.__auth_stubs: 0x18e0
+  __TEXT.__objc_stubs: 0xc440
+  __TEXT.__objc_methlist: 0x4e6c
+  __TEXT.__const: 0x265
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__gcc_except_tab: 0x3f7c
-  __TEXT.__oslogstring: 0x10016
-  __TEXT.__cstring: 0xcf88
-  __TEXT.__objc_methname: 0xf45f
-  __TEXT.__objc_classname: 0xc7b
-  __TEXT.__objc_methtype: 0x28ee
-  __TEXT.__unwind_info: 0x1880
-  __DATA_CONST.__auth_got: 0xc88
+  __TEXT.__gcc_except_tab: 0x409c
+  __TEXT.__oslogstring: 0x10291
+  __TEXT.__cstring: 0xd36d
+  __TEXT.__objc_methname: 0xf866
+  __TEXT.__objc_classname: 0xc7f
+  __TEXT.__objc_methtype: 0x2982
+  __TEXT.__unwind_info: 0x18a8
+  __DATA_CONST.__auth_got: 0xc80
   __DATA_CONST.__got: 0x6e0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2040
+  __DATA_CONST.__const: 0x20b8
   __DATA_CONST.__cfstring: 0x81c0
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__objc_arrayobj: 0xf0
-  __DATA_CONST.__objc_intobj: 0x648
+  __DATA_CONST.__objc_intobj: 0x660
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xad68
-  __DATA.__objc_selrefs: 0x3738
-  __DATA.__objc_ivar: 0x9bc
+  __DATA.__objc_const: 0xae40
+  __DATA.__objc_selrefs: 0x37a0
+  __DATA.__objc_ivar: 0x9d0
   __DATA.__objc_data: 0x1bd0
   __DATA.__data: 0xb48
   __DATA.__bss: 0x1f0

   - /usr/lib/libmrc.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4907EDAF-7091-37BE-B821-64CAFF601795
-  Functions: 2081
-  Symbols:   634
-  CStrings:  7020
+  UUID: 5EBFEBD8-4E48-34DF-B8D0-64018657609A
+  Functions: 2098
+  Symbols:   633
+  CStrings:  7066
 
Symbols:
- _objc_retain_x10
CStrings:
+ "%s called with null (credentialContext.length == 32)"
+ "%s called with null (redemptionContext.length == 32)"
+ "%s called with null auxiliaryAuthChallenge"
+ "%s called with null auxiliaryAuthenticationChallenge"
+ "%s called with null keyIDData"
+ "%s called with null self.isARC"
+ ")!"
+ "+[NSPPrivateAccessTokenFetcher activateTokens:challenge:tokenKey:clientNonceArray:unactivatedListFromServer:]"
+ "+[NSPPrivateAccessTokenFetcher createARCTokenRequestsWithChallenge:tokenKey:waitingTokenList:]"
+ "+[NSPPrivateAccessTokenFetcher createATHMTokenRequestsWithChallenge:tokenKey:tokenCount:waitingTokenList:]"
+ "+[NSPPrivateAccessTokenFetcher createBlindRSATokenRequestsWithChallenge:tokenKey:tokenCount:originNameKey:selectedOrigin:waitingTokenList:clientNonceArray:clientSaltArray:longLivedToken:]"
+ "+[NSPPrivateAccessTokenFetcher generateTokensUsingTokenBlinder:contentArray:waitingTokenList:tokenCount:]"
+ "-[NSPPrivacyTokenManager fetchPrivateAccessTokenForChallenge:overrideAttester:supportsTokenUsageFeedback:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthChallenge:auxiliaryAuthKey:auxiliaryAuthLabel:auxiliaryAuthInfoCacheKey:rateLimit:auditToken:bundleID:accessToken:completionHandler:]"
+ "-[NSPPrivacyTokenManager innerFetchPrivateAccessTokenForChallenge:overrideAttester:customAttester:customAttesterHeaders:tokenKey:tokenCount:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:auxiliaryAuthRequest:bundleID:accessToken:longLivedToken:urlSession:extraRequestHeaders:completionHandler:]"
+ "-[NSPPrivateAccessTokenChallenge credentialRequestContextForKeyID:]"
+ "-[NSPPrivateAccessTokenChallenge initARCChallengeWithIssuerName:redemptionContext:originNames:credentialContext:]"
+ "-[NSPPrivateAccessTokenChallenge initWithType:issuerName:redemptionContext:originNames:credentialContext:]"
+ "-[NSPPrivateAccessTokenChallenge presentationRequestContextForKeyID:]"
+ "-[NSPPrivateAccessTokenFetcher fetchTokenAndAuxiliaryAuthenticationWithQueue:completionHandler:]"
+ "-[NSPPrivateAccessTokenFetcher initWithChallenge:tokenKey:auxiliaryAuthenticationChallenge:auxiliaryAuthenticationKey:auxiliaryAuthenticationLabel:]"
+ "-[NSPPrivateAccessTokenRequest initWithChallenge:tokenKey:tokenKeyID:originNameKey:selectedOrigin:blindedMessage:]"
+ "-[NSPPrivateAccessTokenResponse initWithChallenge:nonce:tokenKey:keyID:authenticator:]"
+ "?0"
+ "?2"
+ "?4P`"
+ "?7P`"
+ "ARC credentials not currently supported with auxiliary auth"
+ "Auxiliary auth challenge must be ATHM"
+ "Failed to activate auxiliary auth response"
+ "Failed to create auxiliary auth request"
+ "Failed to fetch private access token and auxiliary authentication: %@"
+ "Failed to find a matching key for %@ (type %u)"
+ "Generated ARC presentation (%d remaining for this context)"
+ "Invalid auxiliary auth type"
+ "Invalid credential context"
+ "Invalid credential context length %u"
+ "Invalid credential context length %u, cannot fit in %zu"
+ "Invalid number of challenges for paired tokens (%zu)"
+ "Invalid number of challenges for token with auth aux request (%zu)"
+ "NSPServerAuxiliaryAuthenticationChallenge"
+ "NSPServerHasAuxiliaryAuthenticationChallenges"
+ "NSPServerPrivateAccessTokenMetadataSize"
+ "Received auxiliary response with label %@ for %@"
+ "Resuming token fetch, received notification on token for %@"
+ "TI,V_metadataSize"
+ "_auxiliaryAuthenticationChallengeData"
+ "_auxiliaryAuthenticationKey"
+ "_auxiliaryAuthenticationLabel"
+ "_credentialContext"
+ "_metadataSize"
+ "_redemptionContext"
+ "activateToken failed with error %@"
+ "addAuxiliaryAuthArray:"
+ "credentialContext"
+ "fetchPrivateAccessTokenAndAuxAuthWithFetcher:allowRetry:completionHandler:"
+ "fetchPrivateAccessTokenForChallenge:overrideAttester:supportsTokenUsageFeedback:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthChallenge:auxiliaryAuthKey:auxiliaryAuthLabel:auxiliaryAuthInfoCacheKey:rateLimit:auditToken:bundleID:accessToken:completionHandler:"
+ "fetchTokenAndAuxiliaryAuthenticationWithQueue:completionHandler:"
+ "getRemainingPresentationCountWithPresentationContext:presentationLimit:error:"
+ "hasTokenType"
+ "https://mask-api.icloud.com/v5_1/fetchConfigFile"
+ "initARCChallengeWithIssuerName:redemptionContext:originNames:credentialContext:"
+ "initWithChallenge:tokenKey:auxiliaryAuthenticationChallenge:auxiliaryAuthenticationKey:auxiliaryAuthenticationLabel:"
+ "initWithKeyCommitmentsData:nbuckets:deploymentID:error:"
+ "metadataSize"
+ "redemptionContext"
+ "setMetadataSize:"
+ "subdataWithRange:"
+ "v144@0:8@16@24B32@36@44@52@60@68@76@84@92@100I108@112@120@128@?136"
+ "v32@?0@\"NSData\"8@\"NSData\"16@\"NSError\"24"
+ "v36@0:8@\"NSPPrivateAccessTokenFetcher\"16B24@?<v@?@\"NSData\"@\"NSData\"@\"NSError\">28"
+ "v48@?0@\"NSData\"8@\"NSData\"16q24@\"NSString\"32@\"NSString\"40"
+ "v72@?0@\"NSArray\"8@\"NSArray\"16@\"NSArray\"24@\"NSDate\"32@\"NSDictionary\"40q48@\"NSString\"56@\"NSString\"64"
+ "verifyAndGetKeyIDFromKeyCommitmentsData:numBuckets:deploymentID:"
- "%s called with null (redemptionNonce.length == 32)"
- "%s called with null (waitingTokens.count > 0)"
- "(!"
- "+[NSPPrivateAccessTokenFetcher createTokenRequestsForChallenge:tokenKey:originNameKey:selectedOrigin:waitingTokens:]"
- "+[NSPPrivateAccessTokenFetcher createWaitingTokensForChallenge:tokenKey:pairedToken:clientNonces:clientSalts:tokenCount:]"
- "-[NSPPrivacyTokenManager activateTokens:challenge:tokenIssuancePublicKey:clientNonceArray:unactivatedListFromServer:]"
- "-[NSPPrivacyTokenManager createARCTokenRequestsWithChallenge:tokenKey:waitingTokenList:]"
- "-[NSPPrivacyTokenManager createATHMTokenRequestsWithChallenge:tokenKey:tokenCount:waitingTokenList:]"
- "-[NSPPrivacyTokenManager createBlindRSATokenRequestsWithChallenge:tokenKey:tokenCount:originNameKey:selectedOrigin:waitingTokenList:clientNonceArray:clientSaltArray:longLivedToken:]"
- "-[NSPPrivacyTokenManager innerFetchPrivateAccessTokenForChallenge:overrideAttester:customAttester:customAttesterHeaders:tokenKey:tokenCount:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:bundleID:accessToken:longLivedToken:urlSession:extraRequestHeaders:completionHandler:]"
- "-[NSPPrivateAccessTokenChallenge initWithType:issuerName:redemptionNonce:originNames:]"
- "-[NSPPrivateAccessTokenRequest initWithChallenge:tokenKey:originNameKey:selectedOrigin:blindedMessage:]"
- "-[NSPPrivateAccessTokenResponse initWithChallenge:nonce:tokenKey:authenticator:]"
- "?3P`"
- "?6P`"
- "Configuration does not support paired access token requests"
- "Could not create waiting tokens"
- "Failed to create token structure, cannot handle token response"
- "Failed to generate waiting tokens, cannot generate token request"
- "Failed to process token response"
- "Failted to activate waiting token, cannot handle token response"
- "Generated ARC presentation"
- "Paired token issuance server error"
- "_redemptionNonce"
- "activateTokenWithServerResponse failed with error %@"
- "activateWithResponseData:nbuckets:error:"
- "initWithKeyCommitmentsData:error:"
- "v64@?0@\"NSArray\"8@\"NSArray\"16@\"NSDate\"24@\"NSDictionary\"32q40@\"NSString\"48@\"NSString\"56"

```
