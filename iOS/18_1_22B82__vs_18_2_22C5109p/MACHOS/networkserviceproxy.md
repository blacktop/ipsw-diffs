## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

-834.40.4.0.0
-  __TEXT.__text: 0xb3f34
+845.0.0.0.1
+  __TEXT.__text: 0xb73a0
   __TEXT.__auth_stubs: 0x1890
-  __TEXT.__objc_stubs: 0xc600
-  __TEXT.__objc_methlist: 0x3e04
-  __TEXT.__const: 0x310
-  __TEXT.__objc_methname: 0xf477
-  __TEXT.__oslogstring: 0xf31c
-  __TEXT.__objc_classname: 0xc61
-  __TEXT.__objc_methtype: 0x2915
-  __TEXT.__gcc_except_tab: 0x4310
-  __TEXT.__cstring: 0xc264
+  __TEXT.__objc_stubs: 0xc780
+  __TEXT.__objc_methlist: 0x3e54
+  __TEXT.__const: 0x311
+  __TEXT.__objc_methname: 0xf786
+  __TEXT.__oslogstring: 0xfb2b
+  __TEXT.__objc_classname: 0xc63
+  __TEXT.__objc_methtype: 0x29e3
+  __TEXT.__gcc_except_tab: 0x431c
+  __TEXT.__cstring: 0xc72d
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__unwind_info: 0x18f8
+  __TEXT.__unwind_info: 0x1940
   __DATA_CONST.__auth_got: 0xc58
-  __DATA_CONST.__got: 0x6b0
-  __DATA_CONST.__const: 0x1f70
-  __DATA_CONST.__cfstring: 0x7ae0
+  __DATA_CONST.__got: 0x6d0
+  __DATA_CONST.__const: 0x1fc0
+  __DATA_CONST.__cfstring: 0x7d20
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x188
-  __DATA_CONST.__objc_intobj: 0x690
-  __DATA_CONST.__objc_arraydata: 0x78
-  __DATA_CONST.__objc_arrayobj: 0xc0
+  __DATA_CONST.__objc_intobj: 0x6a8
+  __DATA_CONST.__objc_arraydata: 0x88
+  __DATA_CONST.__objc_arrayobj: 0xd8
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xc918
-  __DATA.__objc_selrefs: 0x3438
-  __DATA.__objc_ivar: 0x99c
+  __DATA.__objc_const: 0xca48
+  __DATA.__objc_selrefs: 0x34c0
+  __DATA.__objc_ivar: 0x9b0
   __DATA.__objc_data: 0x1b30
   __DATA.__data: 0xc10
   __DATA.__bss: 0x1b8

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2080
-  Symbols:   625
-  CStrings:  5920
+  Functions: 2111
+  Symbols:   629
+  CStrings:  6013
 
Symbols:
+ _NSLocalizedFailureReasonErrorKey
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSPPrivacyProxyAuxiliaryAuthInfo
+ _OBJC_CLASS_$_RSABSSATokenWaitingActivation
CStrings:
+ "\x1e"
+ "%!s(MISSING) called with null (tokenRequests.count > 0)"
+ "%!s(MISSING) called with null auxiliaryData"
+ "%!s(MISSING) called with null cacheKey"
+ "%!s(MISSING) called with null label"
+ "+[NSPPrivateAccessTokenFetcher createTokenRequestsForChallenge:tokenKey:originNameKey:selectedOrigin:waitingTokens:]"
+ "+[NSPPrivateAccessTokenFetcher createWaitingTokensForChallenge:tokenKey:pairedToken:clientNonces:clientSalts:tokenCount:]"
+ "+[NSPPrivateAccessTokenFetcher fetchAuxiliaryAuthenticationDataFromCacheForType:label:cacheKey:completionHandler:]"
+ "+[NSPPrivateAccessTokenFetcher saveAuxiliaryAuthenticationDataToCache:type:forLabel:cacheKey:]"
+ "-[NSPPrivacyTokenManager fetchPrivateAccessTokenForChallenge:overrideAttester:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:]"
+ "-[NSPPrivacyTokenManager innerFetchPrivateAccessTokenForChallenge:overrideAttester:customAttester:customAttesterHeaders:tokenKey:tokenCount:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:bundleID:accessToken:longLivedToken:urlSession:extraRequestHeaders:completionHandler:]"
+ "-[NSPPrivateAccessTokenFetcher saveTokenToCache:]"
+ "?"
+ "?3P`"
+ "?6P`"
+ "@\"NSObject\""
+ "@\"NSPPrivacyProxyTokenKey\""
+ "@\"NSPPrivateAccessTokenRequest\""
+ "Cannot fetch multiple local tokens with a single token fetcher"
+ "Clearing auxiliary auth info for \"%!@(MISSING)\" in the keychain"
+ "Could not create token requests"
+ "Could not create waiting tokens"
+ "Failed to create token structure, cannot handle token response"
+ "Failed to find a known token key"
+ "Failed to generate token request"
+ "Failed to generate waiting tokens, cannot generate token request"
+ "Failed to get cache key, cannot add auxiliary authentication data to cache"
+ "Failed to get cache key, cannot fetch auxiliary authentication data from cache"
+ "Failed to get challenge, cannot add token to cache"
+ "Failed to get data, cannot add auxiliary authentication data to cache"
+ "Failed to get known type, cannot add auxiliary authentication data to cache"
+ "Failed to get known type, cannot fetch auxiliary authentication data from cache"
+ "Failed to get label, cannot add auxiliary authentication data to cache"
+ "Failed to get label, cannot fetch auxiliary authentication data from cache"
+ "Failed to get token data, cannot add token to cache"
+ "Failed to parse challenge, cannot add token to cache"
+ "Failed to process token response"
+ "Failted to activate waiting token, cannot handle token response"
+ "Generated token from response"
+ "Generated token request"
+ "Invalid parameters"
+ "Invalid state, cannot handle token response"
+ "Keychain auxiliary auth data total %!z(MISSING)u bytes, flushing keychain"
+ "Keychain auxiliary auth data total %!z(MISSING)u bytes, not flushing keychain"
+ "Missing cache key"
+ "Missing entitlement"
+ "Missing label"
+ "NSPServerAuxiliaryAuthenticationCacheKey"
+ "NSPServerAuxiliaryAuthenticationData"
+ "NSPServerAuxiliaryAuthenticationLabel"
+ "NSPServerAuxiliaryAuthenticationType"
+ "No key found"
+ "Received auxiliary data with label %!@(MISSING) for %!@(MISSING)"
+ "Received challenge for non-allowed TDM namespace: %!@(MISSING)"
+ "Saving %!l(MISSING)u auxiliary auth info entries for \"%!@(MISSING)\" in the keychain"
+ "Sending auxiliary data with for %!@(MISSING)"
+ "System client entitlement missing, cannot add auxiliary authentication data to cache"
+ "System client entitlement missing, cannot add token to cache"
+ "System client entitlement missing, cannot fetch auxiliary authentication data from cache"
+ "T@\"NSString\",&,V_auxiliaryAuthenticationCacheKey"
+ "Unknown type"
+ "Unsupported token type, cannot generate token request"
+ "_auxiliaryAuthenticationCacheKey"
+ "_waitingClientNonce"
+ "_waitingToken"
+ "_waitingTokenKey"
+ "_waitingTokenRequest"
+ "addAuxiliaryAuthenticationData:type:label:cacheKey:"
+ "addContentList:"
+ "addToken:toCacheForFetcher:"
+ "archivedDataWithRootObject for auxiliary auth info array failed with error: %!@(MISSING)"
+ "auxiliaryAuthArrays"
+ "auxiliaryAuthenticationCacheKey"
+ "com.apple.NetworkServiceProxy.AuxiliaryAuth.Attester"
+ "com.apple.NetworkServiceProxy.AuxiliaryAuth.Origin"
+ "contentLists"
+ "contentListsCount"
+ "fetchAuxiliaryAuthenticationDataFromCacheForType:label:cacheKey:completionHandler:"
+ "fetchKnownPrivateAccessTokenKeyWithFetcher:completionHandler:"
+ "fetchPrivateAccessTokenForChallenge:overrideAttester:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:"
+ "generateTokenRequestWithQueue:completionHandler:"
+ "googleapis.com"
+ "gstatic.com"
+ "handleTokenResponse:withQueue:completionHandler:"
+ "https://mask-api.icloud.com/v4_4/fetchConfigFile"
+ "initWithDomain:code:userInfo:"
+ "privacyProxyErrorDomain"
+ "saveAuxiliaryAuthenticationDataToCache:type:forLabel:cacheKey:"
+ "saveTokenToCache:"
+ "setAuxiliaryAuthArrays:"
+ "setAuxiliaryAuthenticationCacheKey:"
+ "setLabel:"
+ "trusted-compute-token-fetch.1"
+ "trusted-compute-token-fetch.2"
+ "unarchivedObjectOfClass for auxiliary auth info array failed with error: %!@(MISSING)"
+ "v32@0:8@\"NSData\"16@\"NSPPrivateAccessTokenFetcher\"24"
+ "v48@0:8@\"NSData\"16Q24@\"NSString\"32@\"NSString\"40"
+ "v48@0:8@16Q24@32@40"
+ "v48@0:8Q16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSData\"@\"NSError\">40"
- "\x19"
- "-[NSPPrivacyTokenManager fetchPrivateAccessTokenForChallenge:overrideAttester:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:]"
- "-[NSPPrivacyTokenManager innerFetchPrivateAccessTokenForChallenge:overrideAttester:customAttester:customAttesterHeaders:tokenKey:tokenCount:originNameKey:selectedOrigin:bundleID:accessToken:longLivedToken:urlSession:extraRequestHeaders:completionHandler:]"
- "?0"
- "?2P`"
- "?5P`"
- "fetchPrivateAccessTokenForChallenge:overrideAttester:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:"
- "v112@0:8@16@24@32@40@48@56@64@72@80B88B92@96@?104"

```
