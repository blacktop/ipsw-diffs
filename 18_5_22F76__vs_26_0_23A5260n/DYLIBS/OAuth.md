## OAuth

> `/System/Library/PrivateFrameworks/OAuth.framework/OAuth`

```diff

   __TEXT.__objc_methlist: 0x184
   __TEXT.__cstring: 0x186
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0xa0
+  __TEXT.__unwind_info: 0x90
   __TEXT.__objc_classname: 0x5c
   __TEXT.__objc_methname: 0x624
   __TEXT.__objc_methtype: 0xbb

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7CDE105F-3BB4-35BE-BA24-97D4B250FC7E
+  UUID: E3E65C96-2464-3BFA-AADC-34FE8F9B5468
   Functions: 26
   Symbols:   191
   CStrings:  182
Functions:
~ -[OAURLRequestSigner signedURLRequestWithRequest:applicationID:timestamp:] -> -[OAURLRequestSigner oauthNonce] : 1664 -> 96
~ -[OAURLRequestSigner oauthNonce] -> -[OAURLRequestSigner dealloc] : 96 -> 76
~ -[OACredential setConsumerKey:] -> -[OACredential dealloc] : 8 -> 100
~ -[OAURLRequestSigner dealloc] -> -[OACredential signingKey] : 76 -> 160
~ -[OAURLRequestSigner timestamp:] -> -[OACredential setConsumerKey:] : 92 -> 8
~ -[OACredential dealloc] -> -[OACredential consumerSecret] : 100 -> 8
~ -[OACredential signingKey] -> -[OACredential setConsumerSecret:] : 160 -> 8
~ -[OACredential oauthTokenSecret] -> -[OAURLRequestSigner initWithCredential:] : 8 -> 92
~ -[OACredential setOauthTokenSecret:] -> -[OAURLRequestSigner signatureMethodString] : 8 -> 104
~ -[OAURLRequestSigner initWithCredential:] -> -[OAURLRequestSigner signer] : 92 -> 128
~ -[OAURLRequestSigner signatureMethodString] -> -[OAURLRequestSigner timestamp:] : 104 -> 92
~ -[OAURLRequestSigner signer] -> -[OAURLRequestSigner oauthParametersWithNonce:timeStamp:] : 128 -> 340
~ -[OAURLRequestSigner oauthParametersWithNonce:timeStamp:] -> -[OAURLRequestSigner oauthAuthorizationHeaderWithSignature:nonce:timestamp:] : 340 -> 476
~ -[OAURLRequestSigner oauthAuthorizationHeaderWithSignature:nonce:timestamp:] -> -[OAURLRequestSigner applyApplicationID:toRequest:containsMultiPartData:] : 476 -> 532
~ -[OAURLRequestSigner applyApplicationID:toRequest:containsMultiPartData:] -> -[OAURLRequestSigner signedURLRequestWithRequest:applicationID:timestamp:] : 532 -> 1664

```
