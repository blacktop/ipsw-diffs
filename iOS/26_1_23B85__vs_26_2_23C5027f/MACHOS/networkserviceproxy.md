## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

-921.40.2.0.1
-  __TEXT.__text: 0xba768
+921.60.3.502.1
+  __TEXT.__text: 0xba93c
   __TEXT.__auth_stubs: 0x18e0
-  __TEXT.__objc_stubs: 0xc440
+  __TEXT.__objc_stubs: 0xc480
   __TEXT.__objc_methlist: 0x4e6c
   __TEXT.__const: 0x265
   __TEXT.__dlopen_cstrs: 0x64
   __TEXT.__gcc_except_tab: 0x409c
-  __TEXT.__oslogstring: 0x10258
-  __TEXT.__cstring: 0xd368
-  __TEXT.__objc_methname: 0xf866
+  __TEXT.__oslogstring: 0x10291
+  __TEXT.__cstring: 0xd3a9
+  __TEXT.__objc_methname: 0xf884
   __TEXT.__objc_classname: 0xc7f
-  __TEXT.__objc_methtype: 0x2982
-  __TEXT.__unwind_info: 0x18a8
+  __TEXT.__objc_methtype: 0x29cb
+  __TEXT.__unwind_info: 0x18b0
   __DATA_CONST.__auth_got: 0xc80
   __DATA_CONST.__got: 0x6e0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x20b8
-  __DATA_CONST.__cfstring: 0x81a0
+  __DATA_CONST.__cfstring: 0x81c0
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf0

   __DATA_CONST.__objc_intobj: 0x660
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0xae40
-  __DATA.__objc_selrefs: 0x37a0
+  __DATA.__objc_selrefs: 0x37b0
   __DATA.__objc_ivar: 0x9d0
   __DATA.__objc_data: 0x1bd0
   __DATA.__data: 0xb48

   - /usr/lib/libmrc.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8EADE414-5361-3305-9348-7DFF1C7CD2B0
+  UUID: BCAACECF-90C0-3BD5-A86C-A500B4D2AF05
   Functions: 2098
   Symbols:   633
-  CStrings:  7063
+  CStrings:  7070
 
Functions:
~ sub_10000dcc8 : 816 -> 844
~ sub_1000110e4 -> sub_100011100 : 3060 -> 3144
~ sub_100012de8 -> sub_100012e58 : 2300 -> 2356
~ sub_1000136e4 -> sub_10001378c : 1432 -> 1464
~ sub_10004648c -> sub_100046554 : 2752 -> 2768
~ sub_100047014 -> sub_1000470ec : 2080 -> 2096
~ sub_10005bb10 -> sub_10005bbf8 : 312 -> 452
~ sub_10008b470 -> sub_10008b5e4 : 20456 -> 20488
~ sub_1000ba188 -> sub_1000ba31c : 1036 -> 984
~ sub_1000ba7cc -> sub_1000ba92c : 464 -> 516
~ sub_1000baa7c -> sub_1000bac10 : 208 -> 272
CStrings:
+ "-[NSPPrivacyProxyProxiedContentFallbackNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:ingressTokenAgentUUID:egressTokenAgentUUID:firstProxyHopUsesStandardToken:secondProxyHopUsesStandardToken:isPrivacyProxy:allowFailover:]"
+ "-[NSPPrivacyProxyProxiedContentNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:firstProxyHopUsesPQTLS:secondProxyHopUsesPQTLS:ingressTokenAgentUUID:egressTokenAgentUUID:firstProxyHopUsesStandardToken:secondProxyHopUsesStandardToken:resolvedAddresses:fallbackAgentUUID:fallbackProxyConfigHash:isPrivacyProxy:allowFailover:]"
+ "Ignoring proxy match dictionary, not applicable for seed"
+ "Seed"
+ "allowFailover"
+ "hasMetadataSize"
+ "v28@?0@\"NSData\"8I16@\"NSError\"20"
+ "v36@0:8@\"NSPPrivateAccessTokenFetcher\"16B24@?<v@?@\"NSData\"I@\"NSError\">28"
- "-[NSPPrivacyProxyProxiedContentFallbackNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:ingressTokenAgentUUID:egressTokenAgentUUID:firstProxyHopUsesStandardToken:secondProxyHopUsesStandardToken:isPrivacyProxy:]"
- "-[NSPPrivacyProxyProxiedContentNetworkRegistration setProxyAgentConfiguration:secondProxyHopURL:firstProxyHopKeyArray:secondProxyHopKeyArray:firstProxyHopVersion:secondProxyHopVersion:firstProxyHopSupportsResumption:secondProxyHopSupportsResumption:firstProxyHopUsesPQTLS:secondProxyHopUsesPQTLS:ingressTokenAgentUUID:egressTokenAgentUUID:firstProxyHopUsesStandardToken:secondProxyHopUsesStandardToken:resolvedAddresses:fallbackAgentUUID:fallbackProxyConfigHash:isPrivacyProxy:]"

```
