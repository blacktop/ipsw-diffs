## NetworkServiceProxy

> `/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy`

```diff

-906.0.1.0.0
-  __TEXT.__text: 0x4f288
-  __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__objc_methlist: 0x4aac
+919.0.0.0.0
+  __TEXT.__text: 0x4fcd4
+  __TEXT.__auth_stubs: 0xde0
+  __TEXT.__objc_methlist: 0x4b34
   __TEXT.__const: 0x360
   __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__cstring: 0x5199
-  __TEXT.__oslogstring: 0x2ccc
-  __TEXT.__unwind_info: 0xe38
+  __TEXT.__cstring: 0x5282
+  __TEXT.__oslogstring: 0x2e56
+  __TEXT.__unwind_info: 0xe40
   __TEXT.__objc_classname: 0x606
-  __TEXT.__objc_methname: 0x958e
-  __TEXT.__objc_methtype: 0x12d7
-  __TEXT.__objc_stubs: 0x5100
+  __TEXT.__objc_methname: 0x96d4
+  __TEXT.__objc_methtype: 0x12ea
+  __TEXT.__objc_stubs: 0x5180
   __DATA_CONST.__got: 0x3c8
-  __DATA_CONST.__const: 0xba8
+  __DATA_CONST.__const: 0xc18
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22a8
+  __DATA_CONST.__objc_selrefs: 0x22f8
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x700
+  __AUTH_CONST.__auth_got: 0x708
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x4a60
-  __AUTH_CONST.__objc_const: 0x65c8
+  __AUTH_CONST.__cfstring: 0x4b00
+  __AUTH_CONST.__objc_const: 0x6600
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0xe60
-  __DATA.__objc_ivar: 0x2c8
+  __DATA.__objc_ivar: 0x2cc
   __DATA.__data: 0x268
   __DATA.__common: 0x1
   __DATA.__bss: 0x10

   - /usr/lib/libboringssl.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3D1488DD-CE02-3BAB-883B-84850CCD7440
-  Functions: 1677
-  Symbols:   4982
-  CStrings:  3574
+  UUID: 36E58BD0-B7E3-37FC-A424-5C9DEA91A350
+  Functions: 1689
+  Symbols:   5016
+  CStrings:  3610
 
Symbols:
+ +[PrivacyProxyClient bootstrapDNSAgentUUID]
+ +[PrivacyProxyClient dnsAgentUUID]
+ +[PrivacyProxyClient getProxiedContentMapEnabledForIdentifier:queue:completionHandler:]
+ +[PrivacyProxyClient multiHopFallbackProxyAgentUUID]
+ +[PrivacyProxyClient multiHopProxyAgentUUID]
+ +[PrivacyProxyClient singleHopFallbackProxyAgentUUID]
+ +[PrivacyProxyClient singleHopProxyAgentUUID]
+ -[NSPConfiguration ignorePlatformBinary]
+ -[NSPConfiguration setIgnorePlatformBinary:]
+ -[NSPServerClient getAgentUUIDForType:]
+ _OBJC_CLASS_$_PBRequest
+ _OBJC_IVAR_$_NSPConfiguration._ignorePlatformBinary
+ _OBJC_METACLASS_$_PBRequest
+ ___87+[PrivacyProxyClient getProxiedContentMapEnabledForIdentifier:queue:completionHandler:]_block_invoke
+ ___87+[PrivacyProxyClient getProxiedContentMapEnabledForIdentifier:queue:completionHandler:]_block_invoke_2
+ ___block_descriptor_56_e8_32s40s48bs_e38_v24?0"PrivacyProxyInfo"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ _objc_msgSend$getAgentUUIDForType:
+ _objc_msgSend$getPrivacyProxyInfoWithCompletionHandler:
+ _objc_msgSend$ignorePlatformBinary
+ _objc_msgSend$setIgnorePlatformBinary:
+ _xpc_dictionary_get_uuid
CStrings:
+ "%s called with null (nonce.length == 32)"
+ "%s called with null (nonce.length == 4)"
+ "%s called with null authenticator"
+ "%s called with null identifier"
+ "%s called with null nonce"
+ "+[PrivacyProxyClient getProxiedContentMapEnabledForIdentifier:queue:completionHandler:]"
+ "-[NSPPrivateAccessTokenResponse initWithChallenge:nonce:tokenKey:authenticator:]"
+ "@\"NSUUID\"24@0:8q16"
+ "ATHM_TOKEN"
+ "ATHM_TOKEN_REQUEST"
+ "Failed to fetch agent UUID for type %lld, UUID was nil"
+ "Failed to fetch agent UUID for type %lld, message failed (%@)"
+ "Failed to fetch agent UUID for type %lld, unable to get connection"
+ "Ignore Platform Binary"
+ "IgnorePlatformBinary"
+ "Looking up agent UUID for type %lld"
+ "NSPAgentType"
+ "NSPAgentUUID"
+ "OAI_COST_JWT"
+ "Received agent UUID %@ for type %lld"
+ "TB,V_ignorePlatformBinary"
+ "_ignorePlatformBinary"
+ "bootstrapDNSAgentUUID"
+ "dnsAgentUUID"
+ "getAgentUUIDForType:"
+ "getProxiedContentMapEnabledForIdentifier:queue:completionHandler:"
+ "ignoreConfigSignature"
+ "ignorePlatformBinary"
+ "multiHopFallbackProxyAgentUUID"
+ "multiHopProxyAgentUUID"
+ "setIgnorePlatformBinary:"
+ "singleHopFallbackProxyAgentUUID"
+ "singleHopProxyAgentUUID"
+ "v24@?0@\"PrivacyProxyInfo\"8@\"NSError\"16"
- "%s called with null blindSignature"
- "-[NSPPrivateAccessTokenResponse initWithChallenge:clientNonce:tokenKey:blindSignature:]"
- "ingoreConfigSignature"
- "ingoreInvalidCerts"

```
