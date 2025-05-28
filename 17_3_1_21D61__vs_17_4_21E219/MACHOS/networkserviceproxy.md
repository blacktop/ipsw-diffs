## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

-698.60.4.0.0
-  __TEXT.__text: 0x9c694
-  __TEXT.__auth_stubs: 0x1720
-  __TEXT.__objc_stubs: 0xb7c0
-  __TEXT.__objc_methlist: 0x3aac
-  __TEXT.__objc_methname: 0xe321
-  __TEXT.__oslogstring: 0xd2bc
-  __TEXT.__objc_classname: 0xc01
-  __TEXT.__objc_methtype: 0x2690
+702.100.16.0.1
+  __TEXT.__text: 0x9ebac
+  __TEXT.__auth_stubs: 0x1740
+  __TEXT.__objc_stubs: 0xb8a0
+  __TEXT.__objc_methlist: 0x3adc
+  __TEXT.__objc_methname: 0xe4df
+  __TEXT.__oslogstring: 0xd697
+  __TEXT.__objc_classname: 0xbff
+  __TEXT.__objc_methtype: 0x26a1
   __TEXT.__const: 0x1e0
-  __TEXT.__gcc_except_tab: 0x2104
-  __TEXT.__cstring: 0xa9b7
-  __TEXT.__unwind_info: 0x16fc
-  __DATA_CONST.__auth_got: 0xba0
+  __TEXT.__gcc_except_tab: 0x20ac
+  __TEXT.__cstring: 0xae5a
+  __TEXT.__unwind_info: 0x16f8
+  __DATA_CONST.__auth_got: 0xbb0
   __DATA_CONST.__got: 0x278
-  __DATA_CONST.__const: 0x1ad8
-  __DATA_CONST.__cfstring: 0x6f00
+  __DATA_CONST.__const: 0x1ab0
+  __DATA_CONST.__cfstring: 0x7020
   __DATA_CONST.__objc_classlist: 0x2a8
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x5e8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x638
+  __DATA_CONST.__objc_superrefs: 0x180
+  __DATA_CONST.__objc_intobj: 0x618
   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xc030
-  __DATA.__objc_selrefs: 0x3048
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x638
-  __DATA.__objc_superrefs: 0x188
-  __DATA.__objc_ivar: 0x920
+  __DATA.__objc_const: 0xc0a0
+  __DATA.__objc_selrefs: 0x3098
+  __DATA.__objc_ivar: 0x928
   __DATA.__objc_data: 0x1a90
   __DATA.__data: 0xbb0
   __DATA.__common: 0x8

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1941
-  Symbols:   584
-  CStrings:  5440
+  Functions: 1949
+  Symbols:   586
+  CStrings:  5490
 
Symbols:
+ _NSPPrivacyProxyConfigurationRawConfig
+ _nw_proxy_hop_set_use_x25519
CStrings:
+ "$2"
+ "%s called with null (clientNonceArray.count == tokenWaitingActivationList.count)"
+ "%s called with null (clientNonceArray.count >= unactivatedListFromServer.count)"
+ "%s called with null (contentArray.count == tokenCount)"
+ "%s called with null (redemptionNonce.length == 32)"
+ "%s called with null issuerName"
+ "%s called with null messageToBlind"
+ "%s called with null originNames.count"
+ "%s called with null redemptionNonce"
+ "%s called with null requestData"
+ "-[NSPPrivacyProxyMultiHopFallbackNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopNextHopsArray:secondProxyHopNextHopsArray:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:ingressTokenAgentUUID:egressTokenAgentUUID:firstProxyHopUsesStandardToken:secondProxyHopUsesStandardToken:shouldFailOpen:allowGeohash:geohashOverride:enableDNSFilteringHint:configEpoch:]"
+ "-[NSPPrivacyProxyMultiHopNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopNextHopsArray:secondProxyHopNextHopsArray:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:ingressTokenAgentUUID:egressTokenAgentUUID:firstProxyHopUsesStandardToken:secondProxyHopUsesStandardToken:fallbackAgentUUID:shouldFailOpen:allowGeohash:geohashOverride:enableDNSFilteringHint:fallbackProxyConfigHash:configEpoch:]"
+ "-[NSPPrivacyProxyObliviousHopsFallbackNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:tokenAgentUUID:proxyHopUsesStandardToken:shouldFailOpen:obliviousConfig:obliviousPath:obliviousHTTPType:]"
+ "-[NSPPrivacyProxyObliviousHopsNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:tokenAgentUUID:proxyHopUsesStandardToken:fallbackAgentUUID:shouldFailOpen:obliviousConfig:obliviousPath:obliviousHTTPType:fallbackProxyConfigHash:]"
+ "-[NSPPrivacyProxyProxiedContentFallbackNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:ingressTokenAgentUUID:egressTokenAgentUUID:firstProxyHopUsesStandardToken:secondProxyHopUsesStandardToken:]"
+ "-[NSPPrivacyProxyProxiedContentNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:ingressTokenAgentUUID:egressTokenAgentUUID:firstProxyHopUsesStandardToken:secondProxyHopUsesStandardToken:resolvedAddresses:fallbackAgentUUID:fallbackProxyConfigHash:]"
+ "-[NSPPrivacyProxySingleHopFallbackNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:tokenAgentUUID:proxyHopUsesStandardToken:shouldFailOpen:configEpoch:]"
+ "-[NSPPrivacyProxySingleHopNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:tokenAgentUUID:proxyHopUsesStandardToken:fallbackAgentUUID:shouldFailOpen:fallbackProxyConfigHash:configEpoch:]"
+ "-[NSPPrivacyTokenManager activateTokens:challenge:tokenIssuancePublicKey:clientNonceArray:unactivatedListFromServer:]"
+ "-[NSPPrivacyTokenManager fetchPrivacyTokensOnInterface:tierType:proxyURL:tokenVendor:tokenIssuancePublicKey:tokenChallenge:tokenCount:accessToken:retryAttempt:completionHandler:]"
+ "-[NSPPrivacyTokenManager fetchPrivateAccessTokenForChallenge:tokenKey:originNameKey:selectedOrigin:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:]"
+ "-[NSPPrivacyTokenManager generateTokensUsingTokenBlinder:contentArray:tokenCount:]"
+ "-[NSPPrivateAccessTokenChallenge initRSABlindSignatureChallengeWithIssuerName:redemptionNonce:originNames:]"
+ "-[NSPPrivateAccessTokenChallenge initRateLimitedRSABlindSignatureChallengeWithIssuerName:redemptionNonce:originNames:]"
+ "-[NSPPrivateAccessTokenChallenge initWithType:issuerName:redemptionNonce:originNames:]"
+ "@56@0:8@16@24i32@36@44B52"
+ "Adding %@ UUID missing from cache %@"
+ "CHUNKED"
+ "CONTEXT"
+ "Created fd %d from %d for flow divert"
+ "DEFAULT"
+ "Failed to parse token challenge for %@"
+ "NSPServerTokenSystemClient"
+ "Oblivious HTTP type"
+ "PrivateToken token="
+ "Selected oblivious target config %@ for %@"
+ "Starting and not using configuration settings on disk"
+ "Starting with configuration settings from disk"
+ "T@\"NSString\",?,R,C"
+ "TB,?,N"
+ "TB,?,N,GisNetworkProvider"
+ "TB,?,N,GisNexusProvider"
+ "TB,?,N,GisSpecificUseOnly"
+ "TB,V_systemClient"
+ "Ti,N,V_obliviousHTTPType"
+ "Token challenge changed for \"%@\", flushing tokens"
+ "Unable to dup flow divert handle %d (%d)"
+ "Unable to verify configuration signature on disk"
+ "Unmarshalled configuration length is different from received length (%lu != %lu)"
+ "_ignoreInvalidCerts"
+ "_obliviousHTTPType"
+ "_systemClient"
+ "addTokenRequestList:"
+ "application/private-token-request"
+ "application/private-token-response"
+ "challengeData"
+ "com.apple.private.network.system-token-fetch"
+ "could not extract raw configuration data"
+ "fetchPrivacyTokensOnInterface:tierType:proxyURL:tokenVendor:tokenIssuancePublicKey:tokenChallenge:tokenCount:accessToken:retryAttempt:completionHandler:"
+ "fetchPrivateAccessTokenForChallenge:tokenKey:originNameKey:selectedOrigin:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:"
+ "https://mask-api.icloud.com/v3_5/fetchConfigFile"
+ "https://mask-api.icloud.com/v3_6/fetchConfigFile"
+ "i16@0:8"
+ "initRSABlindSignatureChallengeWithIssuerName:redemptionNonce:originNames:"
+ "initRateLimitedRSABlindSignatureChallengeWithIssuerName:redemptionNonce:originNames:"
+ "initWithDelegate:obliviousConfig:obliviousHTTPType:obliviousTarget:proxyInfo:allowFailOpen:"
+ "obliviousHTTPType"
+ "obliviousPathType"
+ "proxyConfigurationData"
+ "setObliviousHTTPType:"
+ "setProxyConfigurationData:"
+ "setSystemClient:"
+ "systemClient"
+ "tokenChallenge"
+ "unable to extract wire format of configuration from signed configuration message"
+ "v88@0:8@16@24@32@40@48@56B64B68@72@?80"
+ "v96@0:8@16@24@32@40@48@56Q64@72Q80@?88"
- "\x06"
- "\x152"
- "-[NSPPrivacyProxyMultiHopFallbackNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopNextHopsArray:secondProxyHopNextHopsArray:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:ingressTokenAgentUUID:egressTokenAgentUUID:shouldFailOpen:allowGeohash:geohashOverride:enableDNSFilteringHint:configEpoch:]"
- "-[NSPPrivacyProxyMultiHopNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopNextHopsArray:secondProxyHopNextHopsArray:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:ingressTokenAgentUUID:egressTokenAgentUUID:fallbackAgentUUID:shouldFailOpen:allowGeohash:geohashOverride:enableDNSFilteringHint:fallbackProxyConfigHash:configEpoch:]"
- "-[NSPPrivacyProxyObliviousHopsFallbackNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:tokenAgentUUID:shouldFailOpen:obliviousConfig:obliviousPath:]"
- "-[NSPPrivacyProxyObliviousHopsNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:tokenAgentUUID:fallbackAgentUUID:shouldFailOpen:obliviousConfig:obliviousPath:fallbackProxyConfigHash:]"
- "-[NSPPrivacyProxyProxiedContentFallbackNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:ingressTokenAgentUUID:egressTokenAgentUUID:]"
- "-[NSPPrivacyProxyProxiedContentNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:ingressTokenAgentUUID:egressTokenAgentUUID:resolvedAddresses:fallbackAgentUUID:fallbackProxyConfigHash:]"
- "-[NSPPrivacyProxySingleHopFallbackNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:tokenAgentUUID:shouldFailOpen:configEpoch:]"
- "-[NSPPrivacyProxySingleHopNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:tokenAgentUUID:fallbackAgentUUID:shouldFailOpen:fallbackProxyConfigHash:configEpoch:]"
- "-[NSPPrivacyTokenManager fetchPrivacyTokensOnInterface:tierType:proxyURL:tokenVendor:tokenIssuancePublicKey:tokenCount:accessToken:retryAttempt:completionHandler:]"
- "-[NSPPrivacyTokenManager fetchPrivateAccessTokenForChallenge:tokenKey:originNameKey:selectedOrigin:auditToken:bundleID:allowTools:accessToken:completionHandler:]"
- "-[NSPPrivacyTokenManager generateTokensUsingTokenBlinder:tokenCount:]"
- "@52@0:8@16@24@32@40B48"
- "Dealloc: %@"
- "TB,N,GisNetworkProvider"
- "TB,N,GisNexusProvider"
- "TB,N,GisSpecificUseOnly"
- "_tokenFetchURLSession"
- "fetchPrivacyTokensOnInterface:tierType:proxyURL:tokenVendor:tokenIssuancePublicKey:tokenCount:accessToken:retryAttempt:completionHandler:"
- "fetchPrivateAccessTokenForChallenge:tokenKey:originNameKey:selectedOrigin:auditToken:bundleID:allowTools:accessToken:completionHandler:"
- "initWithChallenge:tokenPublicKey:issuerPublicKey:"
- "initWithDelegate:obliviousConfig:obliviousTarget:proxyInfo:allowFailOpen:"
- "message/token-request"
- "message/token-response"
- "v84@0:8@16@24@32@40@48@56B64@68@?76"
- "v88@0:8@16@24@32@40@48Q56@64Q72@?80"

```
