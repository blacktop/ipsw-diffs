## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

-868.120.4.0.0
-  __TEXT.__text: 0xaf0b0
-  __TEXT.__auth_stubs: 0x17f0
-  __TEXT.__objc_stubs: 0xbba0
-  __TEXT.__objc_methlist: 0x4c04
+889.0.0.0.0
+  __TEXT.__text: 0xb3178
+  __TEXT.__auth_stubs: 0x1890
+  __TEXT.__objc_stubs: 0xbf20
+  __TEXT.__objc_methlist: 0x4d0c
   __TEXT.__const: 0x349
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__gcc_except_tab: 0x3c88
-  __TEXT.__oslogstring: 0xeef3
-  __TEXT.__cstring: 0xc60a
-  __TEXT.__objc_methname: 0xeb09
-  __TEXT.__objc_classname: 0xc28
-  __TEXT.__objc_methtype: 0x272b
-  __TEXT.__unwind_info: 0x1798
-  __DATA_CONST.__auth_got: 0xc08
-  __DATA_CONST.__got: 0x698
-  __DATA_CONST.__const: 0x1e08
-  __DATA_CONST.__cfstring: 0x7bc0
-  __DATA_CONST.__objc_classlist: 0x2b0
+  __TEXT.__gcc_except_tab: 0x3de8
+  __TEXT.__oslogstring: 0xf6ae
+  __TEXT.__cstring: 0xcb08
+  __TEXT.__objc_methname: 0xefce
+  __TEXT.__objc_classname: 0xc3c
+  __TEXT.__objc_methtype: 0x27d9
+  __TEXT.__unwind_info: 0x1820
+  __DATA_CONST.__auth_got: 0xc58
+  __DATA_CONST.__got: 0x6b8
+  __DATA_CONST.__const: 0x1ed0
+  __DATA_CONST.__cfstring: 0x7e40
+  __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x180
-  __DATA_CONST.__objc_intobj: 0x618
+  __DATA_CONST.__objc_superrefs: 0x188
+  __DATA_CONST.__objc_intobj: 0x648
   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__objc_arrayobj: 0xd8
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xa938
-  __DATA.__objc_selrefs: 0x3528
-  __DATA.__objc_ivar: 0x980
-  __DATA.__objc_data: 0x1ae0
+  __DATA.__objc_const: 0xab00
+  __DATA.__objc_selrefs: 0x3630
+  __DATA.__objc_ivar: 0x998
+  __DATA.__objc_data: 0x1b30
   __DATA.__data: 0xb58
   __DATA.__bss: 0x1c0
   __DATA.__common: 0x8

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/CaptiveNetwork.framework/CaptiveNetwork

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmdns.dylib
   - /usr/lib/libmrc.dylib
-  - /usr/lib/libnetwork.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D024E2B4-F065-3723-A3CD-E24010B3A75A
-  Functions: 2013
-  Symbols:   610
-  CStrings:  6719
+  UUID: 1AA7D7E7-80F1-36F1-B878-F4DE6054D5AD
+  Functions: 2042
+  Symbols:   624
+  CStrings:  6856
 
Symbols:
+ _OBJC_CLASS_$_ARCAwaitingActivation
+ _OBJC_CLASS_$_ARCCredential
+ _OBJC_CLASS_$_ATHMAwaitingActivation
+ __dispatch_data_empty
+ _nw_content_context_copy_protocol_metadata
+ _nw_http_fields_access_value_by_name
+ _nw_http_metadata_copy_response
+ _nw_http_response_copy_header_fields
+ _nw_http_response_get_status_code
+ _nw_parameters_copy
+ _nw_protocol_copy_http_definition
+ _nw_protocol_definition_get_identifier
+ _nw_protocol_options_copy_definition
+ _nw_protocol_stack_remove_protocol
CStrings:
+ "%s called with null (waitingTokenList.count > 0)"
+ "%s called with null activation"
+ "%s called with null challenge.isBlindRSA"
+ "%s called with null longLivedToken"
+ "%s called with null oneTimeToken"
+ "%s called with null oneTimeTokenSalt"
+ "%s called with null tokenRequests"
+ "%s called with null waitingTokenList"
+ "+[NSPPrivateAccessTokenCache copyCredentialDataFromCacheForChallenge:keyID:]"
+ "-%@"
+ "-[NSPPrivacyTokenManager createARCTokenRequestsWithChallenge:tokenKey:waitingTokenList:]"
+ "-[NSPPrivacyTokenManager createATHMTokenRequestsWithChallenge:tokenKey:tokenCount:waitingTokenList:]"
+ "-[NSPPrivacyTokenManager createBlindRSATokenRequestsWithChallenge:tokenKey:tokenCount:originNameKey:selectedOrigin:waitingTokenList:clientNonceArray:clientSaltArray:longLivedToken:]"
+ "-[NSPPrivacyTokenManager fetchPairedPrivateAccessTokensForChallenge:overrideAttester:configurationFetchDate:configurationETag:tokenKey:originNameKey:selectedOrigin:pairedChallenge:overridePairedAttester:pairedTokenKey:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:]"
+ "-[NSPPrivacyTokenManager fetchPrivateAccessTokenForChallenge:overrideAttester:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:rateLimit:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:]"
+ "-[NSPPrivacyTokenManager generateTokensUsingTokenBlinder:contentArray:waitingTokenList:tokenCount:]"
+ "-[NSPPrivateAccessTokenChallenge initARCChallengeWithIssuerName:]"
+ "-[NSPPrivateAccessTokenChallenge initATHMChallengeWithIssuerName:]"
+ "-[NSPPrivateAccessTokenFetcher saveOneTimeTokenToCache:oneTimeTokenSalt:longLivedToken:]"
+ "@24@0:8r*16"
+ "Aggregate proxied content maps: %@"
+ "Built token fetch URL %@ with client-info \"%@\""
+ "Cached credential from keychain for \"%@\" has expired, flushing"
+ "Cached credential from keychain for \"%@\" non-matching key ID, flushing"
+ "Cannot manually add ARC token to cache"
+ "Failed to access credential from cached data (%@)"
+ "Failed to find one time token key, cannot add token to cache"
+ "Failed to generate credential data to save (%@)"
+ "Failed to generate presentation from cached challenge (%@)"
+ "Failed to get ARC presentation"
+ "Failed to get long lived token, cannot add token to cache"
+ "Failed to get one time token challenge data, cannot add token to cache"
+ "Failed to get one time token salt, cannot add token to cache"
+ "Failed to parse long lived token challenge, cannot add token to cache"
+ "Failed to parse one time token challenge, cannot add token to cache"
+ "Generated ARC presentation"
+ "I"
+ "I16@0:8"
+ "Invalid ARC rate limit"
+ "Invalid rate limit for ARC credential, cannot be 0"
+ "Key does not match one time token, cannot add token to cache"
+ "NSPCachedCredential"
+ "NSPServerPrivateAccessTokenRateLimit"
+ "Parsed discovered proxied content map: %@"
+ "PodcastsLinkPresentationEnabled"
+ "PvD JSON content: %@"
+ "PvD Request"
+ "PvD fetch for proxied content map to %@ received PvD JSON"
+ "PvD fetch for proxied content map to %@ received malformed PvD JSON: %@"
+ "PvD fetch for proxied content map to %@ received no HTTP metadata"
+ "PvD fetch for proxied content map to %@ received no PvD JSON (status %u)"
+ "PvD fetch for proxied content map to %@ received no response, error %@"
+ "Received cached credential from keychain for \"%@\""
+ "Saving credential for \"%@\" in the keychain"
+ "Sending request for %@ with client-info \"%@\""
+ "T@\"NSMutableArray\",&,N,V_discoveredMaps"
+ "TB,N,V_podcastsLinkPresentationEnabled"
+ "TI,V_rateLimit"
+ "_credentialData"
+ "_discoveredMaps"
+ "_keyID"
+ "_podcastsLinkPresentationEnabled"
+ "_rateLimit"
+ "_setPrivacyProxyFailClosed:"
+ "activateWithResponseData failed with error %@"
+ "activateWithResponseData:error:"
+ "activateWithResponseData:nbuckets:error:"
+ "addOneTimeToken:oneTimeTokenSalt:longLivedToken:toCacheForFetcher:"
+ "aggregateMaps"
+ "appleBundleIDs"
+ "appleMatchExactHostnames"
+ "applePercentEnabled"
+ "appleSupportsReverse"
+ "appleSystemProcessesOnly"
+ "application/pvd+json"
+ "arc-%@"
+ "archivedDataWithRootObject for credential data failed with error: %@"
+ "base64EncodedStringWithOptions:"
+ "com.apple.NetworkServiceProxy.PrivateAccessTokens.Credentials"
+ "com.apple.podcasts.link-presentation"
+ "createPvDRequestForName:"
+ "credentialData"
+ "discovered"
+ "discoveredMaps"
+ "discoveredMapsFromPvDConfiguration:"
+ "domains"
+ "fetchDate:isWithinStart:end:etag:"
+ "fetchPairedPrivateAccessTokensForChallenge:overrideAttester:configurationFetchDate:configurationETag:tokenKey:originNameKey:selectedOrigin:pairedChallenge:overridePairedAttester:pairedTokenKey:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:"
+ "fetchPrivateAccessTokenForChallenge:overrideAttester:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:rateLimit:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:"
+ "getCredentialDataError:"
+ "https://%s/.well-known/pvd"
+ "https://mask-api.icloud.com/v5_0/fetchConfigFile"
+ "initARCChallengeWithIssuerName:"
+ "initATHMChallengeWithIssuerName:"
+ "initWithCredentialData:error:"
+ "initWithKeyCommitmentsData:error:"
+ "initWithRequestContext:serverPublicKey:error:"
+ "podcastsLinkPresentationEnabled"
+ "presentWithPresentationContext:presentationLimit:error:"
+ "presentationData"
+ "proxied content path [%@] updated discovered maps based on PvD configuration"
+ "proxy-match"
+ "proxyPathDiscoveredMaps"
+ "rateLimit"
+ "requestData"
+ "saveOneTimeTokenToCache:oneTimeTokenSalt:longLivedToken:"
+ "setDiscoveredMaps:"
+ "setHostnames:"
+ "setIdentifier:"
+ "setMatchExactHostnames:"
+ "setPercentEnabled:"
+ "setPodcastsLinkPresentationEnabled:"
+ "setProcesses:"
+ "setRateLimit:"
+ "setSupportsReverseProxying:"
+ "setSystemProcessOnly:"
+ "startDoHConnectionForSessionTicketsWithEndpoint:parameters:dohQueryType:completionHandler:"
+ "startPvDConnectionForSessionTicketsWithEndpoint:parameters:completionHandler:"
+ "token activation failed"
+ "tokenKeyID"
+ "unarchivedObjectOfClass for credential data failed with error: %@"
+ "v124@0:8@16@24@32@40@48@56@64@72I80@84@92B100B104@108@?116"
+ "v136@0:8@16@24@32@40@48@56@64@72@80@88@96@104B112B116@120@?128"
+ "v16@?0r*8"
+ "v20@0:8I16"
+ "v48@0:8@\"NSData\"16@\"NSData\"24@\"NSData\"32@\"NSPPrivateAccessTokenFetcher\"40"
- "%s called with null (tokenRequests.count > 0)"
- "+"
- "-[NSPPrivacyTokenManager fetchPairedPrivateAccessTokensForChallenge:overrideAttester:tokenKey:originNameKey:selectedOrigin:pairedChallenge:overridePairedAttester:pairedTokenKey:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:]"
- "-[NSPPrivacyTokenManager fetchPrivateAccessTokenForChallenge:overrideAttester:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:]"
- "-[NSPPrivacyTokenManager generateTokensUsingTokenBlinder:contentArray:tokenCount:]"
- "Challenge response creation failed"
- "fetchPairedPrivateAccessTokensForChallenge:overrideAttester:tokenKey:originNameKey:selectedOrigin:pairedChallenge:overridePairedAttester:pairedTokenKey:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:"
- "fetchPrivateAccessTokenForChallenge:overrideAttester:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:"
- "startConnectionForSessionTicketsWithEndpoint:parameters:dohQueryType:completionHandler:"
- "v120@0:8@16@24@32@40@48@56@64@72@80@88B96B100@104@?112"

```
