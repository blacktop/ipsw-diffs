## AppleIDAuthSupport

> `/System/Library/PrivateFrameworks/AppleIDAuthSupport.framework/AppleIDAuthSupport`

```diff

-113.100.1.0.0
-  __TEXT.__text: 0x7d04
-  __TEXT.__auth_stubs: 0x990
+115.0.0.0.0
+  __TEXT.__text: 0x7aac
   __TEXT.__objc_methlist: 0x3ec
   __TEXT.__const: 0x9b
-  __TEXT.__cstring: 0x1185
+  __TEXT.__cstring: 0x118a
   __TEXT.__oslogstring: 0x367
-  __TEXT.__gcc_except_tab: 0x7c
+  __TEXT.__gcc_except_tab: 0x58
   __TEXT.__unwind_info: 0x1f8
-  __TEXT.__objc_classname: 0x6d
-  __TEXT.__objc_methname: 0xc2f
-  __TEXT.__objc_methtype: 0x7ac
-  __TEXT.__objc_stubs: 0x840
-  __DATA_CONST.__got: 0xb8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x320
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x360
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x4d8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x260
   __AUTH_CONST.__cfstring: 0x1660
   __AUTH_CONST.__objc_const: 0x628
+  __AUTH_CONST.__auth_got: 0x4f8
   __DATA.__objc_ivar: 0x34
   __DATA.__data: 0x180
   __DATA.__bss: 0x40

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ECAA0D9D-8B44-3B38-863E-1A5A1993210A
+  UUID: C7DC1674-88D1-3A47-A9D7-42E61E3DEA12
   Functions: 143
-  Symbols:   672
-  CStrings:  612
+  Symbols:   676
+  CStrings:  412
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x4
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
Functions:
~ _vsetError : 688 -> 696
~ -[AIASRequest initWithURL:data:clientInfo:proxiedClientInfo:companionClientInfo:appleITeamId:appleIClientId:additionalHeaders:] : 1168 -> 1104
~ ___127-[AIASRequest initWithURL:data:clientInfo:proxiedClientInfo:companionClientInfo:appleITeamId:appleIClientId:additionalHeaders:]_block_invoke : 540 -> 472
~ -[AIASRequest resume] : 68 -> 64
~ -[AIASSession init] : 128 -> 124
~ -[AIASSession getRequest:] : 216 -> 204
~ -[AIASSession requestWithURL:data:clientInfo:proxiedClientInfo:companionClientInfo:appleITeamId:appleIClientId:additionalHeaders:] : 516 -> 528
~ -[AIASSession URLSession:task:didReceiveChallenge:completionHandler:] : 1036 -> 948
~ -[AIASSession URLSession:dataTask:didReceiveData:] : 296 -> 240
~ -[AIASSession URLSession:task:didCompleteWithError:] : 672 -> 588
~ -[AIASSession invalidateAndCancel] : 152 -> 144
~ _SendRequestAndCreateResponse : 2600 -> 2464
~ _allowSkipSettingOnInternalHardware : 128 -> 124
~ _AppleIDAuthSupportCopyString : 572 -> 576
~ _GSRelease : 152 -> 176
~ _AppleIDAuthSupportCreate : 1216 -> 1172
~ _AppleIDAuthSupportSetOption : 244 -> 200
~ __AppleIDAuthSupportPBKDF2SRP : 708 -> 716
~ _AppleIDAuthSupportCopyProvidedData : 64 -> 68
~ _allowSkipSettingOnInternalHardware.cold.1 : 144 -> 100
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSError\""
- "@\"NSMutableData\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableURLRequest\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURLSession\""
- "@\"NSURLSessionDataTask\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@80@0:8@16^{__CFDictionary=}24@32@40@48@56@64@72"
- "AIASRequest"
- "AIASSession"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "NSURLSessionDataDelegate"
- "NSURLSessionDelegate"
- "NSURLSessionTaskDelegate"
- "Q16@0:8"
- "T#,R"
- "T@\"NSError\",&,V_error"
- "T@\"NSMutableData\",&,V_data"
- "T@\"NSMutableDictionary\",&,V_taskMap"
- "T@\"NSMutableURLRequest\",&,V_URLRequest"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,V_sema"
- "T@\"NSString\",&,V_networkTaskDescription"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSURLSession\",&,V_URLSession"
- "T@\"NSURLSession\",&,V_session"
- "T@\"NSURLSessionDataTask\",&,V_task"
- "TB,V_done"
- "TB,V_invalidated"
- "TB,V_success"
- "TQ,R"
- "T^{__AppleIDAuthSupportData=},V_context"
- "URLRequest"
- "URLSession"
- "URLSession:dataTask:didBecomeDownloadTask:"
- "URLSession:dataTask:didBecomeStreamTask:"
- "URLSession:dataTask:didReceiveData:"
- "URLSession:dataTask:didReceiveResponse:completionHandler:"
- "URLSession:dataTask:willCacheResponse:completionHandler:"
- "URLSession:didBecomeInvalidWithError:"
- "URLSession:didCreateTask:"
- "URLSession:didReceiveChallenge:completionHandler:"
- "URLSession:task:didCompleteWithError:"
- "URLSession:task:didFinishCollectingMetrics:"
- "URLSession:task:didReceiveChallenge:completionHandler:"
- "URLSession:task:didReceiveInformationalResponse:"
- "URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:"
- "URLSession:task:needNewBodyStream:"
- "URLSession:task:needNewBodyStreamFromOffset:completionHandler:"
- "URLSession:task:willBeginDelayedRequest:completionHandler:"
- "URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:"
- "URLSession:taskIsWaitingForConnectivity:"
- "URLSessionDidFinishEventsForBackgroundURLSession:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__AppleIDAuthSupportData=}"
- "^{__AppleIDAuthSupportData=}16@0:8"
- "_URLRequest"
- "_URLSession"
- "_context"
- "_data"
- "_done"
- "_error"
- "_invalidated"
- "_networkTaskDescription"
- "_sema"
- "_session"
- "_success"
- "_task"
- "_taskMap"
- "appendData:"
- "authenticationMethod"
- "autorelease"
- "cancel"
- "caseInsensitiveCompare:"
- "class"
- "conformsToProtocol:"
- "context"
- "copy"
- "credentialForTrust:"
- "dataTaskWithRequest:"
- "dataWithPropertyList:format:options:error:"
- "debugDescription"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "enumerateKeysAndObjectsUsingBlock:"
- "ephemeralSessionConfiguration"
- "error"
- "getRequest:"
- "hash"
- "host"
- "initWithURL:"
- "initWithURL:data:clientInfo:proxiedClientInfo:companionClientInfo:appleITeamId:appleIClientId:additionalHeaders:"
- "intValue"
- "invalidateAndCancel"
- "invalidated"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "length"
- "networkTaskDescription"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "propertyListWithData:options:format:error:"
- "protectionSpace"
- "release"
- "removeObjectForKey:"
- "requestWithURL:data:clientInfo:proxiedClientInfo:companionClientInfo:appleITeamId:appleIClientId:additionalHeaders:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "sema"
- "serverTrust"
- "session"
- "sessionWithConfiguration:delegate:delegateQueue:"
- "setContext:"
- "setData:"
- "setDone:"
- "setError:"
- "setHTTPBody:"
- "setHTTPMethod:"
- "setInvalidated:"
- "setNetworkTaskDescription:"
- "setObject:forKeyedSubscript:"
- "setSema:"
- "setSession:"
- "setSuccess:"
- "setTask:"
- "setTaskMap:"
- "setTimeoutIntervalForRequest:"
- "setTimeoutIntervalForResource:"
- "setURLRequest:"
- "setURLSession:"
- "setValue:forHTTPHeaderField:"
- "setWaitsForConnectivity:"
- "set_sourceApplicationAuditTokenData:"
- "substringToIndex:"
- "superclass"
- "task"
- "taskIdentifier"
- "taskMap"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSURLSession\"16"
- "v24@0:8@16"
- "v24@0:8^{__AppleIDAuthSupportData=}16"
- "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
- "v32@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24"
- "v32@0:8@16@24"
- "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSData\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionDownloadTask\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionStreamTask\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSError\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLSessionTaskMetrics\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@?<v@?@\"NSInputStream\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSCachedURLResponse\"32@?<v@?@\"NSCachedURLResponse\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLResponse\"32@?<v@?q>40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLAuthenticationChallenge\"32@?<v@?q@\"NSURLCredential\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLRequest\"32@?<v@?q@\"NSURLRequest\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32@?<v@?@\"NSInputStream\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24q32@?40"
- "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32@\"NSURLRequest\"40@?<v@?@\"NSURLRequest\">48"
- "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32q40q48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16@24q32q40q48"
- "valueForHTTPHeaderField:"
- "zone"

```
