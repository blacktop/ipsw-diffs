## OAuth

> `/System/Library/PrivateFrameworks/OAuth.framework/OAuth`

```diff

 32.0.0.0.0
-  __TEXT.__text: 0x10a4
-  __TEXT.__auth_stubs: 0x120
+  __TEXT.__text: 0x10a8
   __TEXT.__objc_methlist: 0x184
   __TEXT.__cstring: 0x186
   __TEXT.__ustring: 0x28
   __TEXT.__unwind_info: 0x90
-  __TEXT.__objc_classname: 0x5c
-  __TEXT.__objc_methname: 0x624
-  __TEXT.__objc_methtype: 0xbb
-  __TEXT.__objc_stubs: 0x760
-  __DATA_CONST.__got: 0x58
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x228
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x98
+  __DATA_CONST.__got: 0x58
   __AUTH_CONST.__cfstring: 0x540
   __AUTH_CONST.__objc_const: 0x410
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0xa0
   __DATA_DIRTY.__objc_data: 0x140

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4474F061-CD19-3D12-BDD0-73362D36391E
+  UUID: 7B9B0452-49AE-36AA-A986-46BEE85BB0E7
   Functions: 26
   Symbols:   191
-  CStrings:  182
+  CStrings:  82
 
Functions:
~ -[OAURLRequestSigner signedURLRequestWithRequest:applicationID:timestamp:] : 1664 -> 1668
CStrings:
- "#16@0:8"
- "@\"NSString\""
- "@\"NSString\"32@0:8@\"NSString\"16@\"NSString\"24"
- "@\"OACredential\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "@36@0:8@16@24B32"
- "@40@0:8@16@24@32"
- "HTTPBody"
- "HTTPMethod"
- "OACredential"
- "OAHMAC_SHA1Signer"
- "OAPlainTextSigner"
- "OAURLEncode"
- "OAURLRequestSigner"
- "OAuthSigner"
- "T@\"NSString\",C,N,V_consumerKey"
- "T@\"NSString\",C,N,V_consumerSecret"
- "T@\"NSString\",C,N,V_oauthToken"
- "T@\"NSString\",C,N,V_oauthTokenSecret"
- "Ti,N,V_signatureMethod"
- "URL"
- "URLWithString:"
- "_consumerKey"
- "_consumerSecret"
- "_credential"
- "_oauthToken"
- "_oauthTokenSecret"
- "_signatureMethod"
- "absoluteString"
- "addObject:"
- "allHTTPHeaderFields"
- "applyApplicationID:toRequest:containsMultiPartData:"
- "arrayByAddingObjectsFromArray:"
- "arrayWithArray:"
- "arrayWithObjects:"
- "base64EncodedStringWithOptions:"
- "bytes"
- "compare:"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "consumerKey"
- "consumerSecret"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "date"
- "dealloc"
- "i"
- "i16@0:8"
- "init"
- "initWithBytes:length:encoding:"
- "initWithCredential:"
- "initWithURL:resolvingAgainstBaseURL:"
- "isEqualToString:"
- "length"
- "mutableCopy"
- "oauthAuthorizationHeaderWithSignature:nonce:timestamp:"
- "oauthNonce"
- "oauthParametersWithNonce:timeStamp:"
- "oauthToken"
- "oauthTokenSecret"
- "oauth_urlEncodedString"
- "password"
- "query"
- "rangeOfString:"
- "rangeOfString:options:"
- "setConsumerKey:"
- "setConsumerSecret:"
- "setHTTPBody:"
- "setOauthToken:"
- "setOauthTokenSecret:"
- "setPassword:"
- "setSignatureMethod:"
- "setURL:"
- "setUser:"
- "setValue:forHTTPHeaderField:"
- "signatureForText:withKey:"
- "signatureMethod"
- "signatureMethodString"
- "signedURLRequestWithRequest:"
- "signedURLRequestWithRequest:applicationID:timestamp:"
- "signer"
- "signingKey"
- "sortedArrayUsingSelector:"
- "stringByAddingPercentEscapesUsingEncoding:"
- "stringByAppendingFormat:"
- "stringByAppendingString:"
- "stringWithFormat:"
- "substringToIndex:"
- "timeIntervalSince1970"
- "timestamp:"
- "user"
- "v16@0:8"
- "v20@0:8i16"
- "v24@0:8@16"
- "valueForHTTPHeaderField:"

```
