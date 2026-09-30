## NetworkServiceProxy

> `/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy`

```diff

-868.120.4.0.0
-  __TEXT.__text: 0x46be0
-  __TEXT.__auth_stubs: 0xda0
-  __TEXT.__objc_methlist: 0x4104
+889.0.0.0.0
+  __TEXT.__text: 0x48a48
+  __TEXT.__auth_stubs: 0xdb0
+  __TEXT.__objc_methlist: 0x4174
   __TEXT.__const: 0x360
   __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__cstring: 0x4e56
-  __TEXT.__oslogstring: 0x2b73
+  __TEXT.__cstring: 0x4fd4
+  __TEXT.__oslogstring: 0x2c24
   __TEXT.__unwind_info: 0xc50
   __TEXT.__objc_classname: 0x4e3
-  __TEXT.__objc_methname: 0x8ad9
-  __TEXT.__objc_methtype: 0x10c1
-  __TEXT.__objc_stubs: 0x4d00
-  __DATA_CONST.__got: 0x3a0
-  __DATA_CONST.__const: 0xac0
+  __TEXT.__objc_methname: 0x8c49
+  __TEXT.__objc_methtype: 0x1133
+  __TEXT.__objc_stubs: 0x4e20
+  __DATA_CONST.__got: 0x380
+  __DATA_CONST.__const: 0xb18
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fe0
+  __DATA_CONST.__objc_selrefs: 0x2048
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x6e8
+  __AUTH_CONST.__auth_got: 0x6f0
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x47a0
-  __AUTH_CONST.__objc_const: 0x58b8
+  __AUTH_CONST.__cfstring: 0x47e0
+  __AUTH_CONST.__objc_const: 0x58f0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0xaf0
-  __DATA.__objc_ivar: 0x2a0
+  __AUTH.__objc_data: 0xb40
+  __DATA.__objc_ivar: 0x2b0
   __DATA.__data: 0x268
   __DATA.__common: 0x1
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_ivar: 0x1f0
-  __DATA_DIRTY.__objc_data: 0x1e0
+  __DATA_DIRTY.__objc_ivar: 0x1e4
+  __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0xa8
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libboringssl.dylib
   - /usr/lib/libc++.1.dylib
-  - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4C081361-8E29-30BC-8BD6-845E3A57A3C7
-  Functions: 1470
-  Symbols:   4445
-  CStrings:  3357
+  UUID: 91AFEFDE-5F81-35B7-B6C9-195CA36E3470
+  Functions: 1479
+  Symbols:   4474
+  CStrings:  3390
 
Symbols:
+ +[NSPConfiguration fetchDate:isWithinStart:end:etag:]
+ +[PrivacyProxyClient configurationFetch:completionHandler:]
+ -[NSPPrivateAccessTokenChallenge initARCChallengeWithIssuerName:]
+ -[NSPPrivateAccessTokenChallenge initATHMChallengeWithIssuerName:]
+ -[NSPPrivateAccessTokenFetcher rateLimit]
+ -[NSPPrivateAccessTokenFetcher saveOneTimeTokenToCache:oneTimeTokenSalt:longLivedToken:]
+ -[NSPPrivateAccessTokenFetcher setRateLimit:]
+ -[NSPServerClient addOneTimeToken:oneTimeTokenSalt:longLivedToken:toCacheForFetcher:]
+ _OBJC_IVAR_$_NSPPrivacyProxyBAAValidation._baaSignature
+ _OBJC_IVAR_$_NSPPrivacyProxyBAAValidation._intermediateCertificate
+ _OBJC_IVAR_$_NSPPrivacyProxyBAAValidation._leafCertificate
+ _OBJC_IVAR_$_NSPPrivateAccessTokenFetcher._rateLimit
+ ___59+[PrivacyProxyClient configurationFetch:completionHandler:]_block_invoke
+ ___59+[PrivacyProxyClient configurationFetch:completionHandler:]_block_invoke_2
+ ___70-[NSPPrivateAccessTokenFetcher fetchTokenWithQueue:completionHandler:]_block_invoke.164
+ ___74-[NSPPrivateAccessTokenFetcher fetchTokenPairWithQueue:completionHandler:]_block_invoke.166
+ ___80-[NSPPrivateAccessTokenFetcher fetchLinkedTokenPairWithQueue:completionHandler:]_block_invoke.168
+ ___80-[NSPPrivateAccessTokenFetcher handleTokenResponse:withQueue:completionHandler:]_block_invoke.198
+ ___80-[NSPPrivateAccessTokenFetcher handleTokenResponse:withQueue:completionHandler:]_block_invoke.202
+ ___87-[NSPPrivateAccessTokenFetcher generateTokenRequestForKey:withQueue:completionHandler:]_block_invoke.181
+ ___87-[NSPPrivateAccessTokenFetcher generateTokenRequestForKey:withQueue:completionHandler:]_block_invoke.185
+ ___87-[NSPPrivateAccessTokenFetcher generateTokenRequestForKey:withQueue:completionHandler:]_block_invoke.189
+ ___block_descriptor_41_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e8_v12?0B8ls32l8s40l8
+ _objc_msgSend$_setError
+ _objc_msgSend$addOneTimeToken:oneTimeTokenSalt:longLivedToken:toCacheForFetcher:
+ _objc_msgSend$fetchDate:isWithinStart:end:etag:
+ _objc_msgSend$fetchNewConfigurationWithCompletionHandler:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$position
+ _objc_msgSend$rateLimit
+ _objc_msgSend$setPosition:
+ _objc_retain_x27
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- ___70-[NSPPrivateAccessTokenFetcher fetchTokenWithQueue:completionHandler:]_block_invoke.162
- ___74-[NSPPrivateAccessTokenFetcher fetchTokenPairWithQueue:completionHandler:]_block_invoke.164
- ___80-[NSPPrivateAccessTokenFetcher fetchLinkedTokenPairWithQueue:completionHandler:]_block_invoke.166
- ___80-[NSPPrivateAccessTokenFetcher handleTokenResponse:withQueue:completionHandler:]_block_invoke.194
- ___80-[NSPPrivateAccessTokenFetcher handleTokenResponse:withQueue:completionHandler:]_block_invoke.200
- ___87-[NSPPrivateAccessTokenFetcher generateTokenRequestForKey:withQueue:completionHandler:]_block_invoke.179
- ___87-[NSPPrivateAccessTokenFetcher generateTokenRequestForKey:withQueue:completionHandler:]_block_invoke.183
- ___87-[NSPPrivateAccessTokenFetcher generateTokenRequestForKey:withQueue:completionHandler:]_block_invoke.187
- _set_nsobject_in_xpc_object
CStrings:
+ "%s called with null challenge.isBlindRSA"
+ "%s called with null longLivedToken"
+ "%s called with null oneTimeToken"
+ "%s called with null oneTimeTokenSalt"
+ "+[PrivacyProxyClient configurationFetch:completionHandler:]"
+ "-[NSPPrivateAccessTokenChallenge initARCChallengeWithIssuerName:]"
+ "-[NSPPrivateAccessTokenChallenge initATHMChallengeWithIssuerName:]"
+ "-[NSPPrivateAccessTokenFetcher saveOneTimeTokenToCache:oneTimeTokenSalt:longLivedToken:]"
+ "Adding One Time Token to cache"
+ "B48@0:8@16@24@32@40"
+ "NSPServerPrivateAccessTokenRateLimit"
+ "PODCASTS_LINK_PRESENTATION"
+ "Podcasts Link Presentation"
+ "TI,V_rateLimit"
+ "_rateLimit"
+ "_setError"
+ "addOneTimeToken:oneTimeTokenSalt:longLivedToken:toCacheForFetcher:"
+ "configurationFetch:completionHandler:"
+ "fetchDate:isWithinStart:end:etag:"
+ "getBytes:range:"
+ "hasError"
+ "initARCChallengeWithIssuerName:"
+ "initATHMChallengeWithIssuerName:"
+ "position"
+ "rateLimit"
+ "saveOneTimeTokenToCache:oneTimeTokenSalt:longLivedToken:"
+ "setPosition:"
+ "setRateLimit:"
+ "v12@?0B8"
+ "v48@0:8@\"NSData\"16@\"NSData\"24@\"NSData\"32@\"NSPPrivateAccessTokenFetcher\"40"
+ "v48@0:8@16@24@32@40"

```
