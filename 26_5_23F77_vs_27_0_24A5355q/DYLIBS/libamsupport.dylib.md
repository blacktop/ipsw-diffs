## libamsupport.dylib

> `/usr/lib/libamsupport.dylib`

```diff

-434.120.4.0.0
-  __TEXT.__text: 0x131f8
-  __TEXT.__auth_stubs: 0xd80
+471.0.0.0.2
+  __TEXT.__text: 0x13704
   __TEXT.__objc_methlist: 0x36c
-  __TEXT.__const: 0x8900
+  __TEXT.__const: 0xd2c0
   __TEXT.__cstring: 0x2b06
   __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__unwind_info: 0x528
-  __TEXT.__objc_classname: 0x89
-  __TEXT.__objc_methname: 0xa7d
-  __TEXT.__objc_methtype: 0x4c0
-  __TEXT.__objc_stubs: 0x7e0
-  __DATA_CONST.__got: 0x128
+  __TEXT.__unwind_info: 0x520
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x4b0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x360
+  __DATA_CONST.__objc_selrefs: 0x368
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x6d0
-  __AUTH_CONST.__const: 0x7a8
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0xa48
   __AUTH_CONST.__cfstring: 0xfa0
   __AUTH_CONST.__objc_const: 0x588
+  __AUTH_CONST.__auth_got: 0x6e8
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x1b8
   __DATA.__bss: 0x10

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /usr/lib/libReverseProxyDevice.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 201DBF8E-9C89-3BF9-852A-55C94D6A22EA
-  Functions: 522
-  Symbols:   1575
-  CStrings:  743
+  UUID: B399741E-53E3-3426-9EE7-3C7E1CF5A1F0
+  Functions: 534
+  Symbols:   1630
+  CStrings:  554
 
Symbols:
+ _AppleLocalPolicyG1HybridScheme3Sha384IM4C
+ _AppleLocalPolicyG1HybridScheme3Sha384IM4C_len
+ _AppleSecureBootG2HybridScheme3Sha384IM4C
+ _AppleSecureBootG2HybridScheme3Sha384IM4C_len
+ _AppleSecureBootGlobalG1Hybrid3Sha384IM4C
+ _AppleSecureBootGlobalG1Hybrid3Sha384IM4C_len
+ _CCMLDSA_FAULT_CANARY
+ _Cryptex1G1HybridScheme3Sha384IM4C
+ _Cryptex1G1HybridScheme3Sha384IM4C_len
+ _Cryptex1GlobalG1HybridScheme3Sha384IM4C
+ _Cryptex1GlobalG1HybridScheme3Sha384IM4C_len
+ _Img4DecodeAppleLocalPolicyG1HybridScheme3Sha384IM4C
+ _Img4DecodeAppleLocalPolicyG1HybridScheme3Sha384IM4CNoPQC
+ _Img4DecodeAppleSecureBootG2HybridScheme3Sha384IM4C
+ _Img4DecodeAppleSecureBootG2HybridScheme3Sha384IM4CNoPQC
+ _Img4DecodeAppleSecureBootGlobalG1Hybrid3Sha384IM4C
+ _Img4DecodeAppleSecureBootGlobalG1Hybrid3Sha384IM4CNoPQC
+ _Img4DecodeCryptex1G1HybridScheme3Sha384IM4C
+ _Img4DecodeCryptex1G1HybridScheme3Sha384IM4CNoPQC
+ _Img4DecodeCryptex1GlobalG1HybridScheme3Sha384IM4C
+ _Img4DecodeCryptex1GlobalG1HybridScheme3Sha384IM4CNoPQC
+ _Img4DecodeWirelessG1HybridScheme3Sha384IM4C
+ _Img4DecodeWirelessG1HybridScheme3Sha384IM4CNoPQC
+ _WirelessG1HybridScheme3Sha384IM4C
+ _WirelessG1HybridScheme3Sha384IM4C_len
+ _ccmldsa_verify_with_canary
+ _kImg4DecodeAppleLocalPolicyG1HybridScheme3Sha384IM4C
+ _kImg4DecodeAppleLocalPolicyG1HybridScheme3Sha384IM4CNoPQC
+ _kImg4DecodeAppleSecureBootG2HybridScheme3Sha384IM4C
+ _kImg4DecodeAppleSecureBootG2HybridScheme3Sha384IM4CNoPQC
+ _kImg4DecodeAppleSecureBootGlobalG1Hybrid3Sha384IM4C
+ _kImg4DecodeAppleSecureBootGlobalG1Hybrid3Sha384IM4CNoPQC
+ _kImg4DecodeCryptex1G1HybridScheme3Sha384IM4C
+ _kImg4DecodeCryptex1G1HybridScheme3Sha384IM4CNoPQC
+ _kImg4DecodeCryptex1GlobalG1HybridScheme3Sha384IM4C
+ _kImg4DecodeCryptex1GlobalG1HybridScheme3Sha384IM4CNoPQC
+ _kImg4DecodeWirelessG1HybridScheme3Sha384IM4C
+ _kImg4DecodeWirelessG1HybridScheme3Sha384IM4CNoPQC
+ _kImg4TagStr_bmcf
+ _kImg4TagStr_lpmc
+ _malloc_type_realloc
+ _objc_msgSend$set_atsTrustPolicy:
+ _objc_opt_respondsToSelector
- _img4encode_realloc
CStrings:
- "#16@0:8"
- "@\"NSCachedURLResponse\"32@0:8@\"NSURLConnection\"16@\"NSCachedURLResponse\"24"
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSInputStream\"32@0:8@\"NSURLConnection\"16@\"NSURLRequest\"24"
- "@\"NSMutableData\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"NSURLRequest\"40@0:8@\"NSURLConnection\"16@\"NSURLRequest\"24@\"NSURLResponse\"32"
- "@\"NSURLResponse\""
- "@\"NSURLSession\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@24@0:8^{__CFHTTPMessage=}16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "AMSupportOSURLConnectionDelegate"
- "AMSupportOSURLSession"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSURLConnection\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSURLConnection\"16@\"NSURLProtectionSpace\"24"
- "B32@0:8@16@24"
- "NSObject"
- "NSURLConnectionDataDelegate"
- "NSURLConnectionDelegate"
- "NSURLSessionDelegate"
- "Q16@0:8"
- "T#,R"
- "T@\"NSData\",R,N,V_data"
- "T@\"NSDictionary\",&,N,V_options"
- "T@\"NSError\",R,N,V_error"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSURLSession\",&,N,V_session"
- "TB,R,V_sslEvalFailed"
- "TQ,R"
- "Td,N,V_timeout"
- "Tf,N,V_priority"
- "URLSession:didBecomeInvalidWithError:"
- "URLSession:didReceiveChallenge:completionHandler:"
- "URLSessionDidFinishEventsForBackgroundURLSession:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_CFURLRequest"
- "_data"
- "_defaultSessionConfigurationWithIdentifier:"
- "_error"
- "_newSession"
- "_options"
- "_priority"
- "_queue"
- "_session"
- "_sslEvalFailed"
- "_timeout"
- "_urlRequestForHTTPMessage:"
- "addObject:"
- "allHeaderFields"
- "appendData:"
- "arrayWithCapacity:"
- "arrayWithObject:"
- "authenticationMethod"
- "autorelease"
- "boolValue"
- "cancelAuthenticationChallenge:"
- "class"
- "conformsToProtocol:"
- "connection:canAuthenticateAgainstProtectionSpace:"
- "connection:didCancelAuthenticationChallenge:"
- "connection:didFailWithError:"
- "connection:didReceiveAuthenticationChallenge:"
- "connection:didReceiveData:"
- "connection:didReceiveResponse:"
- "connection:didSendBodyData:totalBytesWritten:totalBytesExpectedToWrite:"
- "connection:needNewBodyStream:"
- "connection:willCacheResponse:"
- "connection:willSendRequest:redirectResponse:"
- "connection:willSendRequestForAuthenticationChallenge:"
- "connectionDidFinishLoading:"
- "connectionShouldUseCredentialStorage:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "credentialForTrust:"
- "credentialWithIdentity:certificates:persistence:"
- "currentRunLoop"
- "d"
- "d16@0:8"
- "dataTaskWithRequest:completionHandler:"
- "dataWithCapacity:"
- "dealloc"
- "debugDescription"
- "description"
- "distantFuture"
- "doubleValue"
- "ephemeralSessionConfiguration"
- "error"
- "errorWithDomain:code:userInfo:"
- "f"
- "f16@0:8"
- "floatValue"
- "hash"
- "init"
- "initWithData:Options:"
- "initWithOptions:"
- "initWithRequest:delegate:startImmediately:"
- "invalidateAndCancel"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "length"
- "localizedStringForStatusCode:"
- "member:"
- "numberWithBool:"
- "numberWithLong:"
- "objectForKey:"
- "options"
- "performDefaultHandlingForAuthenticationChallenge:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "previousFailureCount"
- "priority"
- "protectionSpace"
- "queue"
- "release"
- "requestComplete"
- "requestWithURL:cachePolicy:timeoutInterval:"
- "respondsToSelector:"
- "response"
- "resume"
- "retain"
- "retainCount"
- "runMode:beforeDate:"
- "self"
- "sendRequest:completion:"
- "sender"
- "serverTrust"
- "session"
- "sessionWithConfiguration:delegate:delegateQueue:"
- "setAllHTTPHeaderFields:"
- "setAllowsCellularAccess:"
- "setConnectionProxyDictionary:"
- "setHTTPBody:"
- "setHTTPMethod:"
- "setLength:"
- "setOptions:"
- "setPriority:"
- "setQueue:"
- "setSession:"
- "setTimeout:"
- "setTimeoutInterval:"
- "setTimeoutIntervalForRequest:"
- "setURL:"
- "set_shouldSkipPreferredClientCertificateLookup:"
- "sslEvalFailed"
- "statusCode"
- "superclass"
- "timeout"
- "useCredential:forAuthenticationChallenge:"
- "v16@0:8"
- "v20@0:8f16"
- "v24@0:8@\"NSURLConnection\"16"
- "v24@0:8@\"NSURLSession\"16"
- "v24@0:8@16"
- "v24@0:8d16"
- "v32@0:8@\"NSURLConnection\"16@\"NSData\"24"
- "v32@0:8@\"NSURLConnection\"16@\"NSError\"24"
- "v32@0:8@\"NSURLConnection\"16@\"NSURLAuthenticationChallenge\"24"
- "v32@0:8@\"NSURLConnection\"16@\"NSURLResponse\"24"
- "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
- "v32@0:8@16@24"
- "v32@0:8^{__CFHTTPMessage=}16@?24"
- "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"NSURLConnection\"16q24q32q40"
- "v48@0:8@16q24q32q40"
- "waitForResponseOrError:"
- "zone"

```
