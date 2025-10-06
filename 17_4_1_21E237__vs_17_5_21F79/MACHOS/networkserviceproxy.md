## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

-702.100.16.0.1
-  __TEXT.__text: 0x9ebac
+702.120.2.0.0
+  __TEXT.__text: 0x9f04c
   __TEXT.__auth_stubs: 0x1740
   __TEXT.__objc_stubs: 0xb8a0
   __TEXT.__objc_methlist: 0x3adc

   __TEXT.__objc_methtype: 0x26a1
   __TEXT.__const: 0x1e0
   __TEXT.__gcc_except_tab: 0x20ac
-  __TEXT.__cstring: 0xae5a
-  __TEXT.__unwind_info: 0x16f8
+  __TEXT.__cstring: 0xaee8
+  __TEXT.__unwind_info: 0x16fc
   __DATA_CONST.__auth_got: 0xbb0
   __DATA_CONST.__got: 0x278
   __DATA_CONST.__const: 0x1ab0

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BA2E001B-B21B-309E-8139-303139CE959D
+  UUID: 53AD9096-989E-3C5C-9D6C-007B3A5603A5
   Functions: 1949
   Symbols:   586
   CStrings:  6387
CStrings:
+ "-[NSPPrivacyProxyMultiHopFallbackNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopNextHopsArray:secondProxyHopNextHopsArray:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:firstProxyHopUsesX25519:secondProxyHopUsesX25519:ingressTokenAgentUUID:egressTokenAgentUUID:firstProxyHopUsesStandardToken:secondProxyHopUsesStandardToken:shouldFailOpen:allowGeohash:geohashOverride:enableDNSFilteringHint:configEpoch:]"
+ "-[NSPPrivacyProxyMultiHopNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopNextHopsArray:secondProxyHopNextHopsArray:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:firstProxyHopUsesX25519:secondProxyHopUsesX25519:ingressTokenAgentUUID:egressTokenAgentUUID:firstProxyHopUsesStandardToken:secondProxyHopUsesStandardToken:fallbackAgentUUID:shouldFailOpen:allowGeohash:geohashOverride:enableDNSFilteringHint:fallbackProxyConfigHash:configEpoch:]"
+ "-[NSPPrivacyProxyObliviousHopsFallbackNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:usesX25519:tokenAgentUUID:proxyHopUsesStandardToken:shouldFailOpen:obliviousConfig:obliviousPath:obliviousHTTPType:]"
+ "-[NSPPrivacyProxyObliviousHopsNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:usesX25519:tokenAgentUUID:proxyHopUsesStandardToken:fallbackAgentUUID:shouldFailOpen:obliviousConfig:obliviousPath:obliviousHTTPType:fallbackProxyConfigHash:]"
+ "-[NSPPrivacyProxySingleHopFallbackNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:usesX25519:tokenAgentUUID:proxyHopUsesStandardToken:shouldFailOpen:configEpoch:]"
+ "-[NSPPrivacyProxySingleHopNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:usesX25519:tokenAgentUUID:proxyHopUsesStandardToken:fallbackAgentUUID:shouldFailOpen:fallbackProxyConfigHash:configEpoch:]"
- "-[NSPPrivacyProxyMultiHopFallbackNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopNextHopsArray:secondProxyHopNextHopsArray:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:ingressTokenAgentUUID:egressTokenAgentUUID:firstProxyHopUsesStandardToken:secondProxyHopUsesStandardToken:shouldFailOpen:allowGeohash:geohashOverride:enableDNSFilteringHint:configEpoch:]"
- "-[NSPPrivacyProxyMultiHopNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopNextHopsArray:secondProxyHopNextHopsArray:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:ingressTokenAgentUUID:egressTokenAgentUUID:firstProxyHopUsesStandardToken:secondProxyHopUsesStandardToken:fallbackAgentUUID:shouldFailOpen:allowGeohash:geohashOverride:enableDNSFilteringHint:fallbackProxyConfigHash:configEpoch:]"
- "-[NSPPrivacyProxyObliviousHopsFallbackNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:tokenAgentUUID:proxyHopUsesStandardToken:shouldFailOpen:obliviousConfig:obliviousPath:obliviousHTTPType:]"
- "-[NSPPrivacyProxyObliviousHopsNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:tokenAgentUUID:proxyHopUsesStandardToken:fallbackAgentUUID:shouldFailOpen:obliviousConfig:obliviousPath:obliviousHTTPType:fallbackProxyConfigHash:]"
- "-[NSPPrivacyProxySingleHopFallbackNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:tokenAgentUUID:proxyHopUsesStandardToken:shouldFailOpen:configEpoch:]"
- "-[NSPPrivacyProxySingleHopNetworkRegistration setProxyAgentConfiguration:proxyKeyArray:proxyVersion:supportsResumption:tokenAgentUUID:proxyHopUsesStandardToken:fallbackAgentUUID:shouldFailOpen:fallbackProxyConfigHash:configEpoch:]"

```
