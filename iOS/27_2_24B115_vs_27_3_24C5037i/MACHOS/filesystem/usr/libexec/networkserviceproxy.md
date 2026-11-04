## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-990.40.2.0.0
-  __TEXT.__text: 0xc08dc
-  __TEXT.__auth_stubs: 0x18e0
-  __TEXT.__objc_stubs: 0xd260
-  __TEXT.__objc_methlist: 0x5044
-  __TEXT.__const: 0x2a8
+990.60.10.0.1
+  __TEXT.__text: 0xc5870
+  __TEXT.__auth_stubs: 0x18f0
+  __TEXT.__objc_stubs: 0xd4c0
+  __TEXT.__objc_methlist: 0x50c4
+  __TEXT.__const: 0x2e8
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__gcc_except_tab: 0x3898
-  __TEXT.__oslogstring: 0x11885
-  __TEXT.__cstring: 0xdfec
-  __TEXT.__objc_methname: 0x10474
+  __TEXT.__gcc_except_tab: 0x39a0
+  __TEXT.__oslogstring: 0x1242a
+  __TEXT.__cstring: 0xe531
+  __TEXT.__objc_methname: 0x10979
   __TEXT.__objc_classname: 0xc2e
-  __TEXT.__objc_methtype: 0x2a77
-  __TEXT.__unwind_info: 0x1f30
-  __DATA_CONST.__const: 0x22f8
-  __DATA_CONST.__cfstring: 0x8d00
+  __TEXT.__objc_methtype: 0x2b8c
+  __TEXT.__unwind_info: 0x1fc0
+  __DATA_CONST.__const: 0x2498
+  __DATA_CONST.__cfstring: 0x8e40
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf0

   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_intobj: 0x6f0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0xc80
-  __DATA_CONST.__got: 0x848
+  __DATA_CONST.__auth_got: 0xc88
+  __DATA_CONST.__got: 0x870
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0xb1b8
-  __DATA.__objc_selrefs: 0x3b40
-  __DATA.__objc_ivar: 0xa08
+  __DATA.__objc_const: 0xb200
+  __DATA.__objc_selrefs: 0x3c00
+  __DATA.__objc_ivar: 0xa0c
   __DATA.__objc_data: 0x1c70
   __DATA.__data: 0xb48
   __DATA.__common: 0x8

   - /usr/lib/libmrc.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2162
-  Symbols:   645
-  CStrings:  6338
+  Functions: 2195
+  Symbols:   651
+  CStrings:  6440
 
Symbols:
+ _OBJC_CLASS_$_NSPPrivacyProxyTransparencyCostTokenEntry
+ _OBJC_CLASS_$_SWTransparencyOperationConfiguration
+ _SecKeyCreateFromSubjectPublicKeyInfoData
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _kSecAttrAccount
+ _kSecAttrModificationDate
+ _kSecValueData
+ _xpc_dictionary_send_reply
- _deviceClassIsHomepod
- _xpc_transaction_exit_clean
CStrings:
+ "%s called with null jwt"
+ "+[NSPPrivateAccessTokenCache addTokensToCacheForChallenge:tokens:expirationTime:]"
+ "+[NSPPrivateAccessTokenCache tokenCountInCacheForChallenge:tokenKeys:]"
+ "-[NSPPrivacyTokenManager cachedTokenCountForChallenge:overrideAttester:supportsTokenUsageFeedback:tokenKey:]"
+ "-[NSPPrivacyTokenManager fetchPairedPrivateAccessTokensForChallenge:overrideAttester:configurationFetchDate:configurationETag:tokenKey:originNameKey:selectedOrigin:pairedChallenge:overridePairedAttester:pairedTokenKey:auditToken:bundleID:allowTools:systemTokenClient:fetchFromServerOnlyOncePerDay:accessToken:completionHandler:]"
+ "-[NSPPrivacyTokenManager fetchPrivateAccessTokenForChallenge:overrideAttester:configurationFetchDate:configurationETag:validateTransparency:supportsTokenUsageFeedback:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:rateLimit:auditToken:bundleID:allowTools:systemTokenClient:fetchFromServerOnlyOncePerDay:useOneTimeTokenBatchSize:accessToken:completionHandler:]"
+ "-[NSPPrivacyTokenManager fetchPrivateAccessTokenForChallenge:overrideAttester:supportsTokenUsageFeedback:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthChallenge:auxiliaryAuthKey:auxiliaryAuthLabel:auxiliaryAuthInfoCacheKey:rateLimit:auditToken:bundleID:fetchFromServerOnlyOncePerDay:accessToken:completionHandler:]"
+ "-[NSPPrivacyTokenManager hasFetchedTokensFromServerTodayForIssuerName:]"
+ "-[NSPPrivacyTokenManager recordServerTokenFetchForIssuerName:]"
+ "-[NSPPrivacyTokenManager validateCostJWT:costTokenKeyEntries:completion:]"
+ "-[NSPPrivateAccessTokenFetcher getCachedTokenCountWithQueue:completionHandler:]"
+ "-[NSPPrivateAccessTokenFetcher prewarmTokenCacheToSize:withQueue:completionHandler:]"
+ "Aggregated tokens for %@ exceed storage limit, deferring aggregation"
+ "Already fetched tokens from a server today"
+ "B32@?0@\"NSObject\"8Q16^B24"
+ "Cannot fetch token and auxiliary auth for %@, already fetched from a server today"
+ "Cannot fetch token for %@, already fetched from a server today and no cached token is available"
+ "Cannot fetch token pair for %@ / %@, already fetched from a server today and no cached tokens are available"
+ "Cannot prewarm private access token cache, no attester URL"
+ "Cannot prewarm private access token cache, no challenge"
+ "Cannot prewarm private access token cache, token type %u is not cachable"
+ "Configuration has no cost token keys for issuer %@, allowing since feature flag is not enabled"
+ "Configuration has no cost token keys for issuer %@, blocking"
+ "Cost JWT for issuer %@ was not validated (error %ld)"
+ "Cost JWT signature did not verify with any of the %u published cost token keys, allowing since feature flag is not enabled"
+ "Cost JWT signature did not verify with any of the %u published cost token keys, blocking"
+ "Cost JWT signature verified with cost token key %u of %u"
+ "Cost token key does not have transparency proof, blocking"
+ "Cost token key not validated by transparency (error %@), allowing since feature flag is not enabled"
+ "Cost token key not validated by transparency (error %@), blocking"
+ "Cost token key validated by transparency, allowing"
+ "Delegation entitlement missing, cannot get token cache count"
+ "Delegation entitlement missing, cannot prewarm token cache"
+ "Dropping cost token for issuer %@, it was not signed by a cost token key published in transparency"
+ "Evicting keychain %@ item for \"%@\" with entries lacking expiration, last modified %.1f days ago"
+ "Failed to create cost token public key from transparency blob"
+ "Failed to get cached token count: %@"
+ "Failed to get challenge, cannot get token cache count"
+ "Failed to get challenge, cannot prewarm token cache"
+ "Failed to parse token challenge, cannot prewarm token cache"
+ "Failed to parse transparency blob for cost token keys"
+ "Failed to prewarm token cache"
+ "Failed to prewarm token cache: %@"
+ "Failed to write daily token fetch date for %@ to preference file"
+ "I44@0:8@16@24B32@36"
+ "Ignoring proxy match dictionary, not applicable for seed"
+ "Invalid config dates"
+ "Invalid desired cache size"
+ "Keychain %@ pruning complete: %u items pruned, %u expired items removed, %u stale items evicted, %zu -> %zu bytes"
+ "Keychain %@ still exceeds limit with unexpired entries, leaving remaining entries"
+ "Keychain %@ total %zu bytes across %lu accounts, removing expired entries"
+ "Keychain %@ total %zu bytes, not pruning"
+ "Keychain auxiliary auth data for \"%@\" total %zu bytes, exceeds limit"
+ "Keychain auxiliary auth data for \"%@\" total %zu bytes, within limit"
+ "Missing challenge"
+ "NSPCostTokenKey"
+ "NSPDailyServerTokenFetchDates"
+ "NSPObliviousConfig"
+ "NSPServerPrivateAccessTokenCacheCount"
+ "NSPServerPrivateAccessTokenDesiredCacheCount"
+ "NSPServerPrivateAccessTokenFetchedCount"
+ "NSPServerTokenFetchOnlyOncePerDay"
+ "NSPTokenKeys"
+ "No desired cache size, cannot prewarm token cache"
+ "No key found in configuration for issuer name, cannot prewarm token cache"
+ "No token key found"
+ "Not fetching extra one-time tokens for %@, already fetched from a server today"
+ "Not fetching extra tokens for %@, already fetched from a server today"
+ "Not prewarming token cache for %@, %u cached tokens already meets the desired size of %u"
+ "Not prewarming token cache for %@, %u cached tokens is above the low water mark of %u"
+ "Not prewarming token cache for %@, already fetched from a server today"
+ "Not prewarming token cache for %@, tokens are already being fetched"
+ "Prewarming Private Access Token cache to %u tokens"
+ "Prewarming not supported for ARC and ATHM"
+ "Prewarming token cache for %@, fetching %u tokens (%u cached, low water mark %u, desired size %u)"
+ "PrivateAccessTokenPrewarm"
+ "Received clock set notification"
+ "Removed %lu expired entries from keychain %@ item for \"%@\""
+ "Removing expired keychain %@ item for \"%@\""
+ "Removing undecodable keychain %@ item for \"%@\""
+ "Seed"
+ "System client entitlement missing, cannot get token cache count"
+ "System client entitlement missing, cannot prewarm token cache"
+ "TB,V_fetchFromServerOnlyOncePerDay"
+ "Token cache for issuer name \"%@\" holds %u tokens"
+ "Transparency blob for cost token keys has no public key"
+ "_fetchFromServerOnlyOncePerDay"
+ "archivedDataWithRootObject for pruned keychain %@ item failed with error: %@"
+ "cachedTokenCountForChallenge:overrideAttester:supportsTokenUsageFeedback:tokenKey:"
+ "com.apple.networkserviceproxy.prewarmprivateaccesstokens"
+ "com.apple.networkserviceproxy.validateCostTokenKey"
+ "com.apple.system.clock_set"
+ "copyAllItemsFromKeychainWithIdentifier:"
+ "costTokenKeyConfig"
+ "entries"
+ "fetchFromServerOnlyOncePerDay"
+ "fetchPairedPrivateAccessTokensForChallenge:overrideAttester:configurationFetchDate:configurationETag:tokenKey:originNameKey:selectedOrigin:pairedChallenge:overridePairedAttester:pairedTokenKey:auditToken:bundleID:allowTools:systemTokenClient:fetchFromServerOnlyOncePerDay:accessToken:completionHandler:"
+ "fetchPrivateAccessTokenForChallenge:overrideAttester:configurationFetchDate:configurationETag:validateTransparency:supportsTokenUsageFeedback:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:rateLimit:auditToken:bundleID:allowTools:systemTokenClient:fetchFromServerOnlyOncePerDay:useOneTimeTokenBatchSize:accessToken:completionHandler:"
+ "fetchPrivateAccessTokenForChallenge:overrideAttester:supportsTokenUsageFeedback:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthChallenge:auxiliaryAuthKey:auxiliaryAuthLabel:auxiliaryAuthInfoCacheKey:rateLimit:auditToken:bundleID:fetchFromServerOnlyOncePerDay:accessToken:completionHandler:"
+ "getCachedTokenCountForFetcher:allowRetry:completionHandler:"
+ "getCachedTokenCountWithQueue:completionHandler:"
+ "hasCostTokenKeyConfig"
+ "hasPublicKey"
+ "indexesOfObjectsPassingTest:"
+ "initWithName:"
+ "isDateInToday:"
+ "prewarmPrivateAccessTokenCacheForChallenge:overrideAttester:configurationFetchDate:configurationETag:validateTransparency:supportsTokenUsageFeedback:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:auditToken:bundleID:fetchFromServerOnlyOncePerDay:useOneTimeTokenBatchSize:accessToken:desiredCacheSize:completionHandler:"
+ "prewarmTokenCacheForFetcher:"
+ "prewarmTokenCacheForFetcher:desiredCacheSize:allowRetry:completionHandler:"
+ "prewarmTokenCacheToSize:withQueue:completionHandler:"
+ "publicKey"
+ "q24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
+ "reevaluateObliviousPaths"
+ "removeObjectsAtIndexes:"
+ "setFetchFromServerOnlyOncePerDay:"
+ "setTimeout:"
+ "totalDataInKeychainWithIdentifier:accountName:"
+ "transparencyEntry"
+ "v140@0:8@16@24@32@40@48@56@64@72@80@88@96@104B112B116B120@124@?132"
+ "v148@0:8@16@24@32@40B48B52@56@64@72@80@88@96@104@112B120B124@128I136@?140"
+ "v148@0:8@16@24B32@36@44@52@60@68@76@84@92@100I108@112@120B128@132@?140"
+ "v156@0:8@16@24@32@40B48B52@56@64@72@80@88@96I104@108@116B124B128B132B136@140@?148"
+ "v20@?0I8@\"NSError\"12"
+ "v24@?0@\"NSArray\"8@\"NSDate\"16"
+ "v24@?0I8I12@\"NSError\"16"
+ "v24@?0I8I12q16"
+ "v36@0:8@\"NSPPrivateAccessTokenFetcher\"16B24@?<v@?I@\"NSError\">28"
+ "v36@0:8I16@20@?28"
+ "v40@0:8@\"NSPPrivateAccessTokenFetcher\"16I24B28@?<v@?II@\"NSError\">32"
+ "v40@0:8@16I24B28@?32"
+ "validateCostJWT:costTokenKeyEntries:completion:"
+ "verifyExpiringProofs:forObject:configuration:completion:"
+ "verifyWithKey:"
- "-[NSPPrivacyTokenManager fetchPairedPrivateAccessTokensForChallenge:overrideAttester:configurationFetchDate:configurationETag:tokenKey:originNameKey:selectedOrigin:pairedChallenge:overridePairedAttester:pairedTokenKey:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:]"
- "-[NSPPrivacyTokenManager fetchPrivateAccessTokenForChallenge:overrideAttester:configurationFetchDate:configurationETag:validateTransparency:supportsTokenUsageFeedback:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:rateLimit:auditToken:bundleID:allowTools:systemTokenClient:useOneTimeTokenBatchSize:accessToken:completionHandler:]"
- "-[NSPPrivacyTokenManager fetchPrivateAccessTokenForChallenge:overrideAttester:supportsTokenUsageFeedback:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthChallenge:auxiliaryAuthKey:auxiliaryAuthLabel:auxiliaryAuthInfoCacheKey:rateLimit:auditToken:bundleID:accessToken:completionHandler:]"
- "ConfigFetchOnNetworkChange"
- "Failed subscription check after %u attempts"
- "Ignoring proxy match dictionary, not applicable for internal"
- "Ignoring proxy match dictionary, not applicable for public"
- "Internal"
- "Keychain auxiliary auth data total %zu bytes, flushing keychain"
- "Keychain auxiliary auth data total %zu bytes, not flushing keychain"
- "Keychain one-time tokens total %zu bytes, flushing keychain"
- "Keychain one-time tokens total %zu bytes, not flushing keychain"
- "Keychain tokens total %zu bytes, flushing keychain"
- "Keychain tokens total %zu bytes, not flushing keychain"
- "Public"
- "Requesting clean exit after client request"
- "Requesting clean exit after client token request"
- "Requesting clean exit after daily stats event"
- "Requesting clean exit after publish stats activity"
- "Requesting clean exit after refresh activity"
- "Retry: checking subscription after %lu seconds"
- "Subscription check retry timer fired"
- "com.apple.networkserviceproxy.subscriptionCheck"
- "fetchPairedPrivateAccessTokensForChallenge:overrideAttester:configurationFetchDate:configurationETag:tokenKey:originNameKey:selectedOrigin:pairedChallenge:overridePairedAttester:pairedTokenKey:auditToken:bundleID:allowTools:systemTokenClient:accessToken:completionHandler:"
- "fetchPrivateAccessTokenForChallenge:overrideAttester:configurationFetchDate:configurationETag:validateTransparency:supportsTokenUsageFeedback:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthInfoCacheKey:rateLimit:auditToken:bundleID:allowTools:systemTokenClient:useOneTimeTokenBatchSize:accessToken:completionHandler:"
- "fetchPrivateAccessTokenForChallenge:overrideAttester:supportsTokenUsageFeedback:customAttester:customAttesterHeaders:tokenKey:originNameKey:selectedOrigin:auxiliaryAuthChallenge:auxiliaryAuthKey:auxiliaryAuthLabel:auxiliaryAuthInfoCacheKey:rateLimit:auditToken:bundleID:accessToken:completionHandler:"
- "totalDataInKeychainWithIdentifier:"
- "v136@0:8@16@24@32@40@48@56@64@72@80@88@96@104B112B116@120@?128"
- "v144@0:8@16@24B32@36@44@52@60@68@76@84@92@100I108@112@120@128@?136"
- "v152@0:8@16@24@32@40B48B52@56@64@72@80@88@96I104@108@116B124B128B132@136@?144"
- "verifyExpiringProofs:for:completion:"
```
