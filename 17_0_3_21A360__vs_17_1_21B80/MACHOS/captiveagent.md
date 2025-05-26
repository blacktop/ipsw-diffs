## captiveagent

> `/usr/libexec/captiveagent`

```diff

-457.0.0.0.0
-  __TEXT.__text: 0x989c
+461.40.3.0.0
+  __TEXT.__text: 0x97dc
   __TEXT.__auth_stubs: 0xa80
-  __TEXT.__objc_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0x2fc
-  __TEXT.__const: 0xce
-  __TEXT.__cstring: 0x6ff
-  __TEXT.__oslogstring: 0xefc
-  __TEXT.__gcc_except_tab: 0xe4
-  __TEXT.__objc_methname: 0xe17
+  __TEXT.__objc_stubs: 0xa80
+  __TEXT.__objc_methlist: 0x31c
+  __TEXT.__const: 0xd6
+  __TEXT.__cstring: 0x717
+  __TEXT.__oslogstring: 0xed0
+  __TEXT.__gcc_except_tab: 0xc4
+  __TEXT.__objc_methname: 0xe55
   __TEXT.__objc_classname: 0x76
-  __TEXT.__objc_methtype: 0x762
-  __TEXT.__unwind_info: 0x258
+  __TEXT.__objc_methtype: 0x759
+  __TEXT.__unwind_info: 0x254
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x558
   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__const: 0x358
-  __DATA_CONST.__cfstring: 0x5c0
+  __DATA_CONST.__cfstring: 0x600
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xaf0
-  __DATA.__objc_selrefs: 0x2e8
-  __DATA.__objc_classrefs: 0x60
+  __DATA.__objc_const: 0xab0
+  __DATA.__objc_selrefs: 0x320
+  __DATA.__objc_classrefs: 0x80
   __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_ivar: 0x54
+  __DATA.__objc_ivar: 0x4c
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x248
+  __DATA.__data: 0x270
   __DATA.__bss: 0x8
   __DATA.__common: 0x1
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 155
-  Symbols:   219
-  CStrings:  458
+  Functions: 156
+  Symbols:   223
+  CStrings:  463
 
Symbols:
+ _NSURLAuthenticationMethodOAuthBearerToken
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSNumber
- _NSURLAuthenticationMethodOAuth
CStrings:
+ "%@ didCompleteWithError"
+ "%@ didReceiveData"
+ "%@ didReceiveResponse"
+ "%@ handleTaskCompletion: did not receive data"
+ "%@ handleTaskCompletion: received non-zero data"
+ "%@ login data task received response with unexpected status code"
+ "%@ task found location without https scheme"
+ "%@ task received HTTP Redirect with location header: [%@]"
+ "%@ task received HTTP Redirect without location header"
+ "%@ token authentication failed"
+ "%@ willPerformHTTPRedirection"
+ "@\"NSMutableData\""
+ "AccessToken"
+ "AccessTokenUsed"
+ "JSON parsing failed, error: %@"
+ "T@\"NSMutableData\",&,N,V_receivedData"
+ "Token Authentication Result : %{public}@"
+ "Token Authentication server sent : %{public}@"
+ "WebSheetRequired"
+ "_receivedData"
+ "access_token"
+ "appendData:"
+ "authResult:"
+ "dataUsingEncoding:"
+ "handleAuthenticationChallenge:task:completionHandler:"
+ "handleChallengeResponse:"
+ "handleRedirectResponse:"
+ "handleResponse:result:"
+ "handleTaskCompletion"
+ "initWithData:encoding:"
+ "numberWithBool:"
+ "receivedData"
+ "setObject:forKeyedSubscript:"
+ "setReceivedData:"
+ "set_enableOAuthBearerTokenChallenges:"
+ "token authenticator provided response with result code: %u"
+ "tokenAuthServerDiscoveryURL"
+ "tos_acceptance_required"
- "%@ Discovery task received response with Location header: %@"
- "%@ Discovery task received response with status code: [%ld]"
- "%@ _handleTaskCompletion"
- "%@ didCompleteWithError for %s task"
- "%@ discovery data task found location without https scheme"
- "%@ discovery data task received response with location header: [%@]"
- "%@ discovery data task received response without location header"
- "%@ discovery task completed"
- "%@ login data task completed receiving challenege"
- "%@ login data task completed token authentication"
- "%@ login data task did not receive response with Unauthorized status code"
- "%@ starting discovery data task"
- "Authorization"
- "Bearer %@"
- "T@\"NSURLSessionDataTask\",&,N,V_discoveryDataTask"
- "TokenAuthLoginURL"
- "_challengeReceived"
- "_discoveryDataTask"
- "_discoveryInProgress"
- "_handleAuthenticationChallenge:task:completionHandler:"
- "_handleTaskCompletion"
- "base64EncodedStringWithOptions:"
- "discoverLoginURL"
- "discovery"
- "discoveryDataTask"
- "handleRedirectResponse:canFollow:"
- "handleResponse:"
- "login:"
- "setDiscoveryDataTask:"
- "stringWithFormat:"
- "token authenticator provided response result code: %u"
- "v20@0:8B16"
- "v32@0:8@16^B24"

```
