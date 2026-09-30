## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

-898.0.0.0.0
-  __TEXT.__text: 0xb377c
+902.0.0.0.1
+  __TEXT.__text: 0xb5114
   __TEXT.__auth_stubs: 0x18c0
-  __TEXT.__objc_stubs: 0xbf40
-  __TEXT.__objc_methlist: 0x4d3c
-  __TEXT.__const: 0x361
+  __TEXT.__objc_stubs: 0xc000
+  __TEXT.__objc_methlist: 0x4d84
+  __TEXT.__const: 0x321
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__gcc_except_tab: 0x3de8
-  __TEXT.__oslogstring: 0xf831
-  __TEXT.__cstring: 0xcb1a
-  __TEXT.__objc_methname: 0xf04f
+  __TEXT.__gcc_except_tab: 0x3ee4
+  __TEXT.__oslogstring: 0xfca2
+  __TEXT.__cstring: 0xccdf
+  __TEXT.__objc_methname: 0xf1e8
   __TEXT.__objc_classname: 0xc7b
-  __TEXT.__objc_methtype: 0x27df
-  __TEXT.__unwind_info: 0x1830
+  __TEXT.__objc_methtype: 0x27ee
+  __TEXT.__unwind_info: 0x1850
   __DATA_CONST.__auth_got: 0xc70
   __DATA_CONST.__got: 0x6c8
-  __DATA_CONST.__const: 0x1f30
-  __DATA_CONST.__cfstring: 0x7e40
+  __DATA_CONST.__const: 0x1f50
+  __DATA_CONST.__cfstring: 0x8100
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x188
+  __DATA_CONST.__objc_arraydata: 0xe8
+  __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_intobj: 0x648
-  __DATA_CONST.__objc_arraydata: 0x88
-  __DATA_CONST.__objc_arrayobj: 0xd8
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xac60
-  __DATA.__objc_selrefs: 0x3638
-  __DATA.__objc_ivar: 0x9a0
+  __DATA.__objc_const: 0xad50
+  __DATA.__objc_selrefs: 0x3668
+  __DATA.__objc_ivar: 0x9bc
   __DATA.__objc_data: 0x1bd0
-  __DATA.__data: 0xb58
+  __DATA.__data: 0xb48
   __DATA.__bss: 0x1f0
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libmrc.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CB9D6AC0-911F-3EA9-9B2C-3DBC7F8385DC
-  Functions: 2048
+  UUID: B9099B21-5B66-3DB2-A49D-878948E67E4F
+  Functions: 2062
   Symbols:   627
-  CStrings:  6866
+  CStrings:  6946
 
CStrings:
+ "*."
+ "@32@0:8@16^i24"
+ "Detected proxy algorithm %@ from PvD-provided proxy URL %@"
+ "Detected proxy identifier %@ from PvD-provided proxy URL %@"
+ "Ignoring proxy match dictionary, cannot understand mandatory key %@"
+ "Ignoring proxy match dictionary, not applicable for internal"
+ "Ignoring proxy match dictionary, not applicable for public"
+ "Ignoring proxy match dictionary, not applicable for seed"
+ "Internal"
+ "Invalid proxy dictionary in PvD proxies array"
+ "Invalid proxy match dictionary in PvD"
+ "Missing proxy URL in proxy dictionary in PvD proxies array"
+ "Missing proxy identifier in proxy dictionary in PvD proxies array"
+ "NOT_SET"
+ "NSPServerBootstrapDNSAgentUUID"
+ "NSPServerDNSAgentUUID"
+ "NSPServerMultiHopFallbackProxyAgentUUID"
+ "NSPServerMultiHopProxyAgentUUID"
+ "NSPServerSingleHopFallbackProxyAgentUUID"
+ "NSPServerSingleHopProxyAgentUUID"
+ "No PvD configuration or proxy identifier, ignoring"
+ "No PvD configuration, ignoring"
+ "No proxies array in PvD"
+ "No proxy URL to match to PvD, ignoring"
+ "No proxy match list in PvD, ignoring"
+ "P384"
+ "Proxy match dictionary does not include bundle IDs or match domains, ignoring"
+ "Proxy match dictionary in PvD missing proxies array"
+ "Public"
+ "Received notification that OHTTP configuration is invalid, refetching configuration"
+ "Seed"
+ "Ti,N,V_discoveredAlgorithm"
+ "Unable to match proxy \"%@\" in PvD to %@"
+ "Unable to match proxy URL \"%@\" proxyURL %@ proxyURL.host %@ in PvD to %@"
+ "X25519"
+ "X25519_MLKEM768"
+ "_bootstrapDNSAgentUUID"
+ "_discoveredAlgorithm"
+ "_dnsAgentUUID"
+ "_multiHopFallbackProxyAgentUUID"
+ "_multiHopProxyAgentUUID"
+ "_singleHopFallbackProxyAgentUUID"
+ "_singleHopProxyAgentUUID"
+ "appleTLSCurve"
+ "apple_algorithm"
+ "apple_builds"
+ "apple_bundleIDs"
+ "apple_matchExactHostnames"
+ "apple_percentEnabled"
+ "apple_supportsReverse"
+ "apple_systemProcessesOnly"
+ "com.apple.networkserviceproxy.ohttpError"
+ "discoveredAlgorithm"
+ "discoveredMapsFromPvDConfiguration:proxyIdentifier:"
+ "isKnownProxyMatchKey:"
+ "mandatory"
+ "objectFromDictionary:key:oldKey:"
+ "proxied content path [%@] updated discovered algorithm to %@ based on PvD configuration"
+ "proxyIdentifierFromPvDConfiguration:discoveredAlgorithm:"
+ "setDiscoveredAlgorithm:"
+ "setUsesClassicLoadingMode:"
+ "shouldUsePQTLSWithProxyInfo:"
- "Setting uses PQTLS on first hop!"
- "discovered"
- "discoveredMapsFromPvDConfiguration:"
- "set_usesNWLoader:"

```
