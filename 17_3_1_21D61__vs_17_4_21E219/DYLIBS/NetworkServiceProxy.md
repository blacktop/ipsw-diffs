## NetworkServiceProxy

> `/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy`

```diff

-698.60.4.0.0
-  __TEXT.__text: 0x87b8c
+702.100.16.0.1
+  __TEXT.__text: 0x891f8
   __TEXT.__auth_stubs: 0x17f0
-  __TEXT.__objc_methlist: 0x6be8
+  __TEXT.__objc_methlist: 0x6d18
   __TEXT.__const: 0x588
   __TEXT.__gcc_except_tab: 0x12f4
-  __TEXT.__cstring: 0x6519
-  __TEXT.__oslogstring: 0x75c3
-  __TEXT.__unwind_info: 0x198c
+  __TEXT.__cstring: 0x6711
+  __TEXT.__oslogstring: 0x765f
+  __TEXT.__unwind_info: 0x19a4
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x728
-  __TEXT.__objc_methname: 0x10e86
-  __TEXT.__objc_methtype: 0x1ddf
-  __TEXT.__objc_stubs: 0xbde0
+  __TEXT.__objc_classname: 0x729
+  __TEXT.__objc_methname: 0x111be
+  __TEXT.__objc_methtype: 0x1de6
+  __TEXT.__objc_stubs: 0xbf00
   __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x1600
+  __DATA_CONST.__const: 0x1618
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa2d8
-  __DATA_CONST.__objc_selrefs: 0x3c38
+  __DATA_CONST.__objc_const: 0xa458
+  __DATA_CONST.__objc_selrefs: 0x3ce8
+  __DATA_CONST.__objc_classrefs: 0x3b0
+  __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x78
   __AUTH_CONST.__const: 0x1550
-  __AUTH_CONST.__cfstring: 0x7360
+  __AUTH_CONST.__cfstring: 0x7480
   __AUTH_CONST.__objc_const: 0x1ea8
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x78

   __AUTH_CONST.__auth_got: 0xc10
   __AUTH.__objc_data: 0x1450
   __DATA.__got_weak: 0x80
-  __DATA.__objc_classrefs: 0x3a8
-  __DATA.__objc_superrefs: 0x210
-  __DATA.__objc_ivar: 0x780
+  __DATA.__objc_ivar: 0x788
   __DATA.__data: 0x408
   __DATA.__common: 0x24
   __DATA.__bss: 0x8
-  __DATA_DIRTY.__objc_ivar: 0x288
+  __DATA_DIRTY.__objc_ivar: 0x29c
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x4a8
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DEEDDC31-8B3B-3E65-A4FA-0400C46CECBC
-  Functions: 2924
-  Symbols:   9267
-  CStrings:  6326
+  UUID: 56C36F62-D4C1-389F-AC96-957944690C0C
+  Functions: 2953
+  Symbols:   9334
+  CStrings:  6386
 
Symbols:
+ +[NSPPrivacyProxyTokenInfo tokenRequestListType]
+ -[NSPConfiguration proxyConfigurationData]
+ -[NSPConfiguration setProxyConfigurationData:]
+ -[NSPPrivacyProxyObliviousHTTPConfig StringAsObliviousHTTPType:]
+ -[NSPPrivacyProxyObliviousHTTPConfig hasObliviousHTTPType]
+ -[NSPPrivacyProxyObliviousHTTPConfig obliviousHTTPTypeAsString:]
+ -[NSPPrivacyProxyObliviousHTTPConfig obliviousHTTPType]
+ -[NSPPrivacyProxyObliviousHTTPConfig setHasObliviousHTTPType:]
+ -[NSPPrivacyProxyObliviousHTTPConfig setObliviousHTTPType:]
+ -[NSPPrivacyProxyObliviousTargetInfo hasWeight]
+ -[NSPPrivacyProxyObliviousTargetInfo setHasWeight:]
+ -[NSPPrivacyProxyObliviousTargetInfo setWeight:]
+ -[NSPPrivacyProxyObliviousTargetInfo weight]
+ -[NSPPrivacyProxyProxyInfo hasTokenChallenge]
+ -[NSPPrivacyProxyProxyInfo setTokenChallenge:]
+ -[NSPPrivacyProxyProxyInfo tokenChallenge]
+ -[NSPPrivacyProxyTokenInfo addTokenRequestList:]
+ -[NSPPrivacyProxyTokenInfo clearTokenRequestLists]
+ -[NSPPrivacyProxyTokenInfo setTokenRequestLists:]
+ -[NSPPrivacyProxyTokenInfo tokenRequestListAtIndex:]
+ -[NSPPrivacyProxyTokenInfo tokenRequestListsCount]
+ -[NSPPrivacyProxyTokenInfo tokenRequestLists]
+ -[NSPPrivateAccessTokenChallenge challengeData]
+ -[NSPPrivateAccessTokenChallenge initRSABlindSignatureChallengeWithIssuerName:redemptionNonce:originNames:]
+ -[NSPPrivateAccessTokenChallenge initRateLimitedRSABlindSignatureChallengeWithIssuerName:redemptionNonce:originNames:]
+ -[NSPPrivateAccessTokenChallenge initWithType:issuerName:redemptionNonce:originNames:]
+ -[NSPPrivateAccessTokenFetcher setSystemClient:]
+ -[NSPPrivateAccessTokenFetcher systemClient]
+ _NSPPrivacyProxyConfigurationRawConfig
+ _OBJC_CLASS_$_PBDataReader
+ _OBJC_IVAR_$_NSPConfiguration._proxyConfigurationData
+ _OBJC_IVAR_$_NSPPrivateAccessTokenFetcher._systemClient
+ ___57-[NSPConfiguration incrementSessionCountersOnFirstLaunch]_block_invoke.452
+ ___70-[NSPPrivateAccessTokenFetcher fetchTokenWithQueue:completionHandler:]_block_invoke.175
+ ___block_literal_global.423
+ ___block_literal_global.439
+ ___block_literal_global.454
+ _objc_msgSend$addTokenRequestList:
+ _objc_msgSend$clearTokenRequestLists
+ _objc_msgSend$proxyConfigurationData
+ _objc_msgSend$setObliviousHTTPType:
+ _objc_msgSend$setProxyConfigurationData:
+ _objc_msgSend$setTokenChallenge:
+ _objc_msgSend$systemClient
+ _objc_msgSend$tokenRequestListAtIndex:
+ _objc_msgSend$tokenRequestListsCount
- -[NSPPrivateAccessTokenFetcher initWithChallenge:tokenPublicKey:issuerPublicKey:]
- ___57-[NSPConfiguration incrementSessionCountersOnFirstLaunch]_block_invoke.443
- ___70-[NSPPrivateAccessTokenFetcher fetchTokenWithQueue:completionHandler:]_block_invoke.169
- ___block_literal_global.414
- ___block_literal_global.430
- ___block_literal_global.445
CStrings:
+ "\x01\x11"
+ "\x01\x1f\x0f\x06\x11"
+ "\x03\x17"
+ "\x05"
+ "%s called with null (redemptionNonce.length == 32)"
+ "%s called with null issuerName"
+ "%s called with null originNames.count"
+ "%s called with null redemptionNonce"
+ "-[NSPPrivateAccessTokenChallenge initRSABlindSignatureChallengeWithIssuerName:redemptionNonce:originNames:]"
+ "-[NSPPrivateAccessTokenChallenge initRateLimitedRSABlindSignatureChallengeWithIssuerName:redemptionNonce:originNames:]"
+ "-[NSPPrivateAccessTokenChallenge initWithType:issuerName:redemptionNonce:originNames:]"
+ "CHUNKED"
+ "CONTEXT"
+ "DEFAULT"
+ "NSPServerTokenSystemClient"
+ "Proxy configuration received data"
+ "Proxy configuration stored data"
+ "ProxyConfigurationData"
+ "StringAsObliviousHTTPType:"
+ "T@\"NSData\",&,N,V_tokenChallenge"
+ "T@\"NSData\",C,V_proxyConfigurationData"
+ "T@\"NSMutableArray\",&,N,V_tokenRequestLists"
+ "T@\"NSString\",?,R,C"
+ "TB,?,N"
+ "TB,?,N,GisNetworkProvider"
+ "TB,?,N,GisNexusProvider"
+ "TB,?,N,GisSpecificUseOnly"
+ "TB,V_systemClient"
+ "Ti,N,V_obliviousHTTPType"
+ "_obliviousHTTPType"
+ "_proxyConfigurationData"
+ "_systemClient"
+ "_tokenChallenge"
+ "_tokenRequestLists"
+ "addTokenRequestList:"
+ "challengeData"
+ "clearTokenRequestLists"
+ "hasObliviousHTTPType"
+ "hasTokenChallenge"
+ "initRSABlindSignatureChallengeWithIssuerName:redemptionNonce:originNames:"
+ "initRateLimitedRSABlindSignatureChallengeWithIssuerName:redemptionNonce:originNames:"
+ "obliviousHTTPType"
+ "obliviousHTTPTypeAsString:"
+ "proxyConfigurationData"
+ "setHasObliviousHTTPType:"
+ "setObliviousHTTPType:"
+ "setProxyConfigurationData:"
+ "setSystemClient:"
+ "setTokenChallenge:"
+ "setTokenRequestLists:"
+ "systemClient"
+ "tokenChallenge"
+ "tokenRequestList"
+ "tokenRequestListAtIndex:"
+ "tokenRequestListType"
+ "tokenRequestLists"
+ "tokenRequestListsCount"
+ "{?=\"obliviousHTTPType\"b1}"
- "\x01\x1f\x0f\x05\x11"
- "\x03\x16"
- "\x04"
- "\x06"
- "TB,N,GisNetworkProvider"
- "TB,N,GisNexusProvider"
- "TB,N,GisSpecificUseOnly"
- "initWithChallenge:tokenPublicKey:issuerPublicKey:"
- "{?=\"proxyIndex\"b1}"

```
