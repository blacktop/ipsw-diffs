## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

-921.60.5.0.0
-  __TEXT.__text: 0xba8e8
-  __TEXT.__auth_stubs: 0x18e0
-  __TEXT.__objc_stubs: 0xc480
-  __TEXT.__objc_methlist: 0x4e6c
-  __TEXT.__const: 0x265
+921.100.18.0.0
+  __TEXT.__text: 0xc2cd0
+  __TEXT.__auth_stubs: 0x1870
+  __TEXT.__objc_stubs: 0xc540
+  __TEXT.__objc_methlist: 0x4e74
+  __TEXT.__const: 0x275
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__gcc_except_tab: 0x409c
-  __TEXT.__oslogstring: 0x10258
-  __TEXT.__cstring: 0xd3a4
-  __TEXT.__objc_methname: 0xf884
-  __TEXT.__objc_classname: 0xc7f
-  __TEXT.__objc_methtype: 0x29cb
-  __TEXT.__unwind_info: 0x18b0
-  __DATA_CONST.__auth_got: 0xc80
-  __DATA_CONST.__got: 0x6e0
+  __TEXT.__gcc_except_tab: 0x3f08
+  __TEXT.__oslogstring: 0x10905
+  __TEXT.__cstring: 0xd4a7
+  __TEXT.__objc_methname: 0xf974
+  __TEXT.__objc_classname: 0xc81
+  __TEXT.__objc_methtype: 0x2a19
+  __TEXT.__unwind_info: 0x1ab0
+  __DATA_CONST.__auth_got: 0xc48
+  __DATA_CONST.__got: 0x6e8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x20b8
-  __DATA_CONST.__cfstring: 0x81a0
+  __DATA_CONST.__const: 0x20e8
+  __DATA_CONST.__cfstring: 0x8320
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf0

   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__objc_arrayobj: 0xf0
-  __DATA_CONST.__objc_intobj: 0x660
+  __DATA_CONST.__objc_intobj: 0x678
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xae40
-  __DATA.__objc_selrefs: 0x37b0
-  __DATA.__objc_ivar: 0x9d0
+  __DATA.__objc_const: 0xaee8
+  __DATA.__objc_selrefs: 0x37e8
+  __DATA.__objc_ivar: 0x9e4
   __DATA.__objc_data: 0x1bd0
   __DATA.__data: 0xb48
   __DATA.__bss: 0x1f0

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy
+  - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /usr/lib/libmrc.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9A6D6CB0-587A-348C-AC46-26FAF0A6DCC8
-  Functions: 2098
-  Symbols:   633
-  CStrings:  7067
+  UUID: DA5E0F77-4B3C-39D0-A37F-93C93321D48B
+  Functions: 2102
+  Symbols:   627
+  CStrings:  7131
 
Symbols:
+ _OBJC_CLASS_$_OSASystemConfiguration
- _objc_claimAutoreleasedReturnValue
- _objc_release_x10
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "%s called with null (prober == self.edgePathProber)"
+ "-[NSPPrivacyProxyAgentManager probeFailed:]"
+ "-[NSPPrivacyProxyAgentManager updateProxyInfo:resolverInfo:proxyPathList:fallbackProxyPathList:obliviousConfigs:proxiedContentMaps:edgeProbeConfig:]"
+ "5\"A"
+ "<default>"
+ "<none>"
+ "@\"NSPPrivacyProxyEdgeProbeConfig\""
+ "Cache miss: No cached OTT for \"%@\", fetching new token"
+ "Cached OTT count (%u) at/below low water mark (%u) for \"%@\", fetching %u extra tokens"
+ "Cached one-time token from keychain for \"%@\" has non-matching key, but not expired (%@). Returning token."
+ "Cached one-time tokens for %@ are always expected to have an expiration, flushing one-time tokens"
+ "Edge path prober"
+ "Edge probe trigger evaluation: enabled=%d, skipping (disabled or cooldown active)"
+ "Edge probe trigger evaluation: enabled=YES, cooldown_cleared=%d, denominator=%u, will_probe=%d"
+ "EdgeMap"
+ "EdgeMapping"
+ "EdgeProbeConfig ingested: enabled=%d, url=%@, probeDenominator=%u (%.4f%%)"
+ "EdgeProbeConfig ingested: nil (edge probing disabled)"
+ "Expiring %lu tokens from %@, last expiration is %llu / %@"
+ "Failed to get challenge, cannot flush tokens from cache"
+ "Failed to parse one time token challenge, cannot flush tokens from cache"
+ "Failed to parse token challenge, cannot flush tokens from cache"
+ "Fetched one-time tokens for \"%@\" (count=%lu, salt=%@, expiration=%@)"
+ "Flushed OTTs from cache for issuer name \"%@\""
+ "Flushed tokens from cache for issuer name \"%@\""
+ "Ignoring proxy match dictionary, not applicable for seed"
+ "Probing(%@): Edge path probe exceeded failure threshold (%lu failures)"
+ "Probing(%@): Edge path probe received server error"
+ "Probing(%@): Edge path probe redirected"
+ "Probing(%@): Edge path probe successful %lu times"
+ "Received %u/%u/%u tokens from %@ (expirations: key = %llu, token = %llu)"
+ "Received cached one-time token%{public}s from keychain for \"%@\" with expiration %@"
+ "Saved OTT to cached based on client API call for account \"%@\" with expiration %@"
+ "Seed"
+ "Sending header %@ with value %@ for configuration fetch"
+ "Skipping error-triggered config refresh, last refresh was %.0f seconds ago (minimum 300 seconds)"
+ "System client entitlement missing, cannot flush tokens from cache"
+ "_edgePathProber"
+ "_edgeProbeConfig"
+ "_edgeProbeURL"
+ "_lastEdgeProbeStartDate"
+ "_lastErrorTriggeredConfigRefreshDate"
+ "_proberType"
+ "absent"
+ "apple-automateddevicegroup"
+ "automatedDeviceGroup"
+ "edge probe config updated: enabled=%d, url=%@, probeDenominator=%u"
+ "edgeProbeConfig"
+ "flushTokensFromCacheForFetcher:"
+ "hasProbeDenominator"
+ "hasUrl"
+ "http://probe.icloud.com"
+ "https://mask-api.icloud.com/v5_2/fetchConfigFile"
+ "present"
+ "probeDenominator"
+ "proxyAgentEdgePathProber"
+ "updateProxyInfo:resolverInfo:proxyPathList:fallbackProxyPathList:obliviousConfigs:proxiedContentMaps:edgeProbeConfig:"
+ "url"
+ "v24@0:8@\"NSPPrivateAccessTokenFetcher\"16"
+ "v72@0:8@16@24@32@40@48@56@64"
- "%\""
- "-[NSPPrivacyProxyAgentManager updateProxyInfo:resolverInfo:proxyPathList:fallbackProxyPathList:obliviousConfigs:proxiedContentMaps:]"
- "Cached one-time token from keychain for \"%@\" has non-matching key, but not expired. Returning token."
- "Received %u/%u/%u tokens from %@"
- "Received cached one-time token%{public}s from keychain for \"%@\""
- "_proxyProber"
- "updateProxyInfo:resolverInfo:proxyPathList:fallbackProxyPathList:obliviousConfigs:proxiedContentMaps:"
- "v64@0:8@16@24@32@40@48@56"

```
