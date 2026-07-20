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
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-976.0.0.0.0
-  __TEXT.__text: 0xca278
+980.0.0.0.0
+  __TEXT.__text: 0xcf36c
   __TEXT.__auth_stubs: 0x1740
-  __TEXT.__objc_stubs: 0xcb00
-  __TEXT.__objc_methlist: 0x5034
-  __TEXT.__const: 0x278
+  __TEXT.__objc_stubs: 0xd080
+  __TEXT.__objc_methlist: 0x5044
+  __TEXT.__const: 0x288
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__gcc_except_tab: 0x3550
-  __TEXT.__oslogstring: 0x10f6f
-  __TEXT.__cstring: 0xdd6a
-  __TEXT.__objc_methname: 0xfe5f
+  __TEXT.__gcc_except_tab: 0x3824
+  __TEXT.__oslogstring: 0x1154c
+  __TEXT.__cstring: 0xdef9
+  __TEXT.__objc_methname: 0x10261
   __TEXT.__objc_classname: 0xc2e
-  __TEXT.__objc_methtype: 0x2a52
-  __TEXT.__unwind_info: 0x1978
-  __DATA_CONST.__const: 0x2548
-  __DATA_CONST.__cfstring: 0x8a60
+  __TEXT.__objc_methtype: 0x2a60
+  __TEXT.__unwind_info: 0x19c8
+  __DATA_CONST.__const: 0x25c0
+  __DATA_CONST.__cfstring: 0x8b20
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf0

   __DATA_CONST.__objc_intobj: 0x6d8
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0xbb0
-  __DATA_CONST.__got: 0x808
+  __DATA_CONST.__got: 0x840
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0xb0d8
-  __DATA.__objc_selrefs: 0x3970
-  __DATA.__objc_ivar: 0x9ec
+  __DATA.__objc_const: 0xb138
+  __DATA.__objc_selrefs: 0x3ac8
+  __DATA.__objc_ivar: 0x9f8
   __DATA.__objc_data: 0x1c70
   __DATA.__data: 0xb48
   __DATA.__bss: 0x218

   - /usr/lib/libmrc.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2240
-  Symbols:   611
-  CStrings:  6207
+  Functions: 2255
+  Symbols:   618
+  CStrings:  6290
 
Symbols:
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_NSPJSONWebToken
+ _OBJC_CLASS_$_NSPPrivacyProxyAggregatorRequest
+ _OBJC_CLASS_$_NSPPrivacyProxyAggregatorResponse
+ _OBJC_CLASS_$_NSPPrivacyProxyBlindRSARequests
+ _OBJC_CLASS_$_NSPPrivacyProxyCostJWTToBlindRSARequest
+ _OBJC_CLASS_$_NSValue
CStrings:
+ "%s called with null (localWaitingTokens.count > 0)"
+ "%s called with null issuer"
+ "-[NSPServer enqueuePendingTokenAggregationForCacheKey:issuer:]"
+ "?0@"
+ "@32@0:8d16@24"
+ "Adding Cost JWT %@"
+ "Aggregating %u cost tokens (total value %f) for issuer %@ via %@"
+ "Arming token aggregation timer to fire in %u seconds"
+ "Configuration has no aggregator config for issuer %@"
+ "Cost JWT bucketized_cost_unit (%.2f) exceeds maxValue (%.2f) for issuer %@"
+ "Cost JWT for issuer %@ has unexpected type for bucketized_cost_unit"
+ "Cost JWT for issuer %@ missing bucketized_cost_unit"
+ "Cost JWT for issuer %@: bucketized_cost_unit=%.2f maxValue=%.2f remainder=%.2f"
+ "Cost JWT issuer %@ has no aggregator token config"
+ "CostTokenAggregation"
+ "Could not parse aggregator URL %@"
+ "Failed to create token aggregation timer"
+ "Failed to parse cost JWT, cannot add auxiliary authentication data to cache"
+ "Failed to parse token aggregator response from %@"
+ "No aggregator service found for issuer %@"
+ "No aggregator token config found for issuer %@"
+ "Requesting %u tokens of denomination value %@ from aggregator"
+ "Saving %u activated tokens from aggregator"
+ "Sending %u auxiliary tokens from aggregator for %@"
+ "Sending auxiliary data for %@"
+ "Stale on-disk config disk version (%ld is not current); clearing etag at load to force refetch"
+ "Token aggregation timer fired"
+ "Token aggregator batch %u status: %@"
+ "Token aggregator received HTTP response code %ld for %@ with request UUID %@"
+ "Token aggregator reported %u failed cost tokens (reason %d, reusable %d)"
+ "Token aggregator request to %@ failed with error %@"
+ "Token aggregator request to %@ returned no data"
+ "Token aggregator summary for %@: aggregated %u cost JWTs (value %f); rejected %lu (reusable %lu value %f, lost %lu value %f)"
+ "TokenAggregationDate"
+ "TokenAggregatorFetch"
+ "Too few tokens to aggregate (%u/%u), skipping"
+ "_pendingTokenAggregations"
+ "_tokenAggregationDate"
+ "_tokenAggregationTimer"
+ "addBlindRSARequests:"
+ "addCostTokens:"
+ "addTokenRequests:"
+ "aggregateTokensForIssuer:forCacheKey:aggregator:aggregatorTokenConfig:attesterConfigs:completionHandler:"
+ "aggregatedCount"
+ "aggregatorServices"
+ "aggregatorTokenConfig"
+ "batchSize"
+ "blindRSAResponses"
+ "bucketized_cost_unit"
+ "com.apple.NetworkServiceProxy.AuxiliaryAuth.Aggregator"
+ "com.apple.NetworkServiceProxy.AuxiliaryAuth.OriginNeedsAggregation"
+ "com.apple.networkserviceproxy.tokenAggregationTimerFired"
+ "com.apple.networkserviceproxy.tokenAggregator"
+ "costJWTToBlindRSARequest"
+ "costJWTToBlindRSAResponse"
+ "costTokens"
+ "dataUsingEncoding:"
+ "denominationTokenConfigs"
+ "encodedString"
+ "exchangeObjectAtIndex:withObjectAtIndex:"
+ "failedCostTokens"
+ "hasAggregatedCount"
+ "hasAggregatorTokenConfig"
+ "hasCostJWTToBlindRSAResponse"
+ "hasTokenCacheConfig"
+ "indexOfObject:"
+ "initWithString:requireSignature:"
+ "isEqualToNumber:"
+ "lowWatermark"
+ "mapTableWithKeyOptions:valueOptions:"
+ "maxValue"
+ "pat_issuer"
+ "payload"
+ "rangeValue"
+ "removeObjectsInRange:"
+ "reusable"
+ "selectDenominationTokensToRequestForCostTokenTotal:denominationValues:"
+ "setAggregatedCount:"
+ "setCostJWTToBlindRSARequest:"
+ "setIssuerName:"
+ "sortUsingDescriptors:"
+ "sortedArrayUsingDescriptors:"
+ "subarrayWithRange:"
+ "tokenCacheConfig"
+ "tokenResponses"
+ "valueWithRange:"
- "%s called with null (waitingTokenList.count > 0)"
- "Configuration disk version changed, forcing a configuration fetch"
- "Sending auxiliary data with for %@"
```
