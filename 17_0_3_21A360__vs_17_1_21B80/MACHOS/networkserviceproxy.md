## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

-698.0.0.0.0
-  __TEXT.__text: 0x9bba4
+698.40.5.0.0
+  __TEXT.__text: 0x9c4fc
   __TEXT.__auth_stubs: 0x1720
-  __TEXT.__objc_stubs: 0xb7e0
-  __TEXT.__objc_methlist: 0x395c
-  __TEXT.__objc_methname: 0xe337
-  __TEXT.__oslogstring: 0xd2c1
-  __TEXT.__objc_classname: 0xbd5
-  __TEXT.__objc_methtype: 0x266d
+  __TEXT.__objc_stubs: 0xb7c0
+  __TEXT.__objc_methlist: 0x3aa4
+  __TEXT.__objc_methname: 0xe321
+  __TEXT.__oslogstring: 0xd2bc
+  __TEXT.__objc_classname: 0xc01
+  __TEXT.__objc_methtype: 0x2690
   __TEXT.__const: 0x1e0
   __TEXT.__gcc_except_tab: 0x2104
-  __TEXT.__cstring: 0xa919
-  __TEXT.__unwind_info: 0x16c8
+  __TEXT.__cstring: 0xa99c
+  __TEXT.__unwind_info: 0x16fc
   __DATA_CONST.__auth_got: 0xba0
   __DATA_CONST.__got: 0x278
   __DATA_CONST.__const: 0x1ad8
-  __DATA_CONST.__cfstring: 0x6e00
-  __DATA_CONST.__objc_classlist: 0x2a0
-  __DATA_CONST.__objc_protolist: 0xf0
+  __DATA_CONST.__cfstring: 0x6ee0
+  __DATA_CONST.__objc_classlist: 0x2a8
+  __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x5d0
+  __DATA_CONST.__objc_intobj: 0x5e8
   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xbdb8
+  __DATA.__objc_const: 0xc010
   __DATA.__objc_selrefs: 0x3048
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x628
-  __DATA.__objc_superrefs: 0x180
-  __DATA.__objc_ivar: 0x900
-  __DATA.__objc_data: 0x1a40
-  __DATA.__data: 0xb50
+  __DATA.__objc_classrefs: 0x638
+  __DATA.__objc_superrefs: 0x188
+  __DATA.__objc_ivar: 0x920
+  __DATA.__objc_data: 0x1a90
+  __DATA.__data: 0xbb0
   __DATA.__common: 0x8
   __DATA.__bss: 0x198
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B8EE2162-BECA-30DD-85FD-164F9FB8EEE2
-  Functions: 1914
-  Symbols:   583
-  CStrings:  6305
+  UUID: D1E8D36E-8316-393E-9346-82EE69122967
+  Functions: 1940
+  Symbols:   584
+  CStrings:  6326
 
Symbols:
+ _OBJC_CLASS_$_NSPPrivacyProxyObliviousTargetInfo
CStrings:
+ "\"\x16"
+ "&\x1c\x1f\t\xb2\x12"
+ "'"
+ "-[NSPObliviousPath matchIngress:]"
+ "-[NSPObliviousPath resetFallbackProxyAgent]"
+ "-[NSPObliviousPath resetQUICProxyAgentForceUpdateDelegate:]"
+ "-[NSPProxyPath initWithDelegate:ingressProxy:egressProxy:proxyPathWeight:allowFallback:fallbackToQUIC:forceFallback:allowFailOpen:geohashSharingEnabled:configEpoch:networkCharacteristics:]"
+ "-[NSPQuicProxyPath initWithDelegate:ingressProxy:egressProxy:proxyPathWeight:allowFallback:fallbackToQUIC:forceFallback:allowFailOpen:geohashSharingEnabled:configEpoch:networkCharacteristics:]"
+ "@\"<NSPObliviousPathDelegate>\""
+ "@\"NSPPrivacyProxyObliviousTargetInfo\""
+ "@52@0:8@16@24@32@40B48"
+ "@84@0:8@16@24@32Q40B48B52B56B60B64@68@76"
+ "NSPObliviousPath"
+ "NSPObliviousPathDelegate"
+ "Oblivious paths"
+ "Oblivious target"
+ "Received error (%d) from %s for oblivious %@ agent on interface %@"
+ "Setting up oblivious path (%@)"
+ "T@\"<NSPObliviousPathDelegate>\",W,V_delegate"
+ "T@\"NSData\",&,N,V_obliviousConfig"
+ "T@\"NSPPrivacyProxyObliviousTargetInfo\",&,N,V_obliviousTarget"
+ "T@\"NSPProxyTokenInfo\",&,N,V_proxyInfo"
+ "TB,N,V_obliviousAgentRegistered"
+ "Token fetch for Oblivious[%@] %@"
+ "_obliviousAgentRegistered"
+ "_obliviousConfig"
+ "_obliviousPaths"
+ "_obliviousTarget"
+ "https://mask-api.icloud.com/v3_4/fetchConfigFile"
+ "initWithDelegate:ingressProxy:egressProxy:proxyPathWeight:allowFallback:fallbackToQUIC:forceFallback:allowFailOpen:geohashSharingEnabled:configEpoch:networkCharacteristics:"
+ "initWithDelegate:obliviousConfig:obliviousTarget:proxyInfo:allowFailOpen:"
+ "matchExactHostnames"
+ "oblivious path [%@] is ready"
+ "oblivious path is not ready due to insufficient ingress proxy tokens (cache+agent: %lu) for [%@], (ingress proxy low-water mark: %lu)"
+ "obliviousAgentRegistered"
+ "obliviousConfig"
+ "obliviousPathAllowFailOpen"
+ "obliviousPathConfig"
+ "obliviousPathFallbackAgentUUID"
+ "obliviousPathProxy"
+ "obliviousPathQUICAgentUUID"
+ "obliviousPathTarget"
+ "obliviousTarget"
+ "proxyAgentObliviousPaths"
+ "setObliviousAgentRegistered:"
+ "setObliviousConfig:"
+ "setObliviousTarget:"
+ "setProxyInfo:"
+ "updateIngressProxy:egressProxy:proxyPathWeight:"
+ "updateProxyInfo self.obliviousConfigs %@"
+ "v32@0:8@\"NSPObliviousPath\"16@\"NSString\"24"
+ "v40@0:8@\"NSPObliviousPath\"16@\"NSString\"24@\"NSUUID\"32"
+ "v40@0:8@16@24Q32"
- "#\x18"
- "&\x1c\x1f\b\xb2\x12"
- "-[NSPFallbackProxyPath resetObliviousHopProxyAgents]"
- "-[NSPProxyPath initWithDelegate:ingressProxy:egressProxy:proxyPathWeight:obliviousConfigs:allowFallback:fallbackToQUIC:forceFallback:allowFailOpen:geohashSharingEnabled:configEpoch:networkCharacteristics:]"
- "-[NSPProxyPath resetObliviousHopProxyAgents]"
- "-[NSPQuicProxyPath initWithDelegate:ingressProxy:egressProxy:proxyPathWeight:obliviousConfigs:allowFallback:fallbackToQUIC:forceFallback:allowFailOpen:geohashSharingEnabled:configEpoch:networkCharacteristics:]"
- "-[NSPQuicProxyPath resetObliviousHopProxyAgents]"
- "@\"NSData\"24@0:8@\"NSString\"16"
- "@\"NSUUID\"24@0:8@\"NSString\"16"
- "@92@0:8@16@24@32Q40@48B56B60B64B68B72@76@84"
- "No target host for oblivious config, skipping"
- "Oblivious UUID for %@ present without registration"
- "Oblivious agent UUIDs"
- "Oblivious agents should not be set for preferred paths"
- "Oblivious target host %@ already covered, skipping"
- "Proxy index %u not valid for ingress proxy %@, skipping"
- "T@\"NSArray\",&,N,V_obliviousConfigs"
- "T@\"NSMutableDictionary\",&,N,V_obliviousAgentUUIDs"
- "T@\"NSMutableDictionary\",&,N,V_obliviousHopRegistrations"
- "Tearing down oblivious agent for %@"
- "Tearing down oblivious fallback agent for %@"
- "_obliviousAgentUUIDs"
- "_obliviousHopRegistrations"
- "initWithDelegate:ingressProxy:egressProxy:proxyPathWeight:obliviousConfigs:allowFallback:fallbackToQUIC:forceFallback:allowFailOpen:geohashSharingEnabled:configEpoch:networkCharacteristics:"
- "obliviousAgentUUIDs"
- "obliviousHopAgentUUIDForHostname:"
- "obliviousHopConfigHashForHostname:"
- "obliviousHopFallbackProxyAgentUUIDForHostname:"
- "obliviousHopFallbackProxyConfigHashForHostname:"
- "obliviousHopRegistrations"
- "proxyPathObliviousAgentUUIDs"
- "proxyPathObliviousConfigs"
- "resetObliviousHopProxyAgents"
- "setObliviousAgentUUIDs:"
- "setObliviousConfigs:"
- "setObliviousHopRegistrations:"
- "updateIngressProxy:egressProxy:proxyPathWeight:obliviousConfigs:"
- "v32@0:8@\"NSPProxyPath\"16@\"NSString\"24"
- "v40@0:8@\"NSPProxyPath\"16@\"NSString\"24@\"NSUUID\"32"
- "v48@0:8@16@24Q32@40"

```
