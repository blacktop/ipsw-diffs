## XPCAcmeService

> `/System/Library/Frameworks/Security.framework/Versions/Current/XPCServices/XPCAcmeService.xpc/Contents/MacOS/XPCAcmeService`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`

```diff

-62460.0.55.0.1
-  __TEXT.__text: 0x3d40
-  __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_stubs: 0x3c0
-  __TEXT.__objc_methlist: 0x8c
-  __TEXT.__const: 0xd8
+62460.1.2.0.0
+  __TEXT.__text: 0x41e0
+  __TEXT.__auth_stubs: 0x8d0
+  __TEXT.__objc_stubs: 0x600
+  __TEXT.__objc_methlist: 0x28c
+  __TEXT.__const: 0xd0
   __TEXT.__gcc_except_tab: 0xb4
-  __TEXT.__cstring: 0x37f
-  __TEXT.__objc_methname: 0x2db
-  __TEXT.__objc_classname: 0xb
-  __TEXT.__objc_methtype: 0x65
+  __TEXT.__cstring: 0x392
+  __TEXT.__objc_methname: 0x8cb
+  __TEXT.__objc_classname: 0x75
+  __TEXT.__objc_methtype: 0x6c4
   __TEXT.__oslogstring: 0x209
   __TEXT.__unwind_info: 0x160
-  __DATA_CONST.__const: 0x260
-  __DATA_CONST.__cfstring: 0x2a0
-  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__const: 0x230
+  __DATA_CONST.__cfstring: 0x320
+  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x4a0
-  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__auth_got: 0x478
+  __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x130
-  __DATA.__objc_selrefs: 0x120
-  __DATA.__objc_ivar: 0xc
-  __DATA.__objc_data: 0x50
-  __DATA.__data: 0x40
+  __DATA.__objc_const: 0x3f0
+  __DATA.__objc_selrefs: 0x2c8
+  __DATA.__objc_ivar: 0x14
+  __DATA.__objc_data: 0xa0
+  __DATA.__data: 0x1c0
   __DATA.__bss: 0x38
+  - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/Versions/A/CrashReporterSupport
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 71
-  Symbols:   191
-  CStrings:  115
+  Functions: 66
+  Symbols:   189
+  CStrings:  225
 
Symbols:
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLSession
+ _OBJC_CLASS_$_NSURLSessionConfiguration
+ _OBJC_CLASS_$__NSHSTSStorage
+ _audit_token_to_pid
+ _objc_autorelease
- _OBJC_CLASS_$_NSOperationQueue
- _OBJC_CLASS_$_NSURLConnection
- _dispatch_async
- _objc_alloc_init
- _objc_destroyWeak
- _objc_getProperty
- _objc_loadWeakRetained
- _objc_setProperty_atomic
- _objc_storeWeak
CStrings:
+ "#16@0:8"
+ "@\"NSMutableData\""
+ "@\"NSString\"16@0:8"
+ "@\"NSURLResponse\""
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@32@0:8Q16@?24"
+ "@40@0:8:16@24@32"
+ "@40@0:8r*16Q24^@32"
+ "@?"
+ "AcmeSessionDelegate"
+ "B"
+ "B16@0:8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "B32@0:8@16Q24"
+ "GET"
+ "HEAD"
+ "NSObject"
+ "NSURLSessionDataDelegate"
+ "NSURLSessionDelegate"
+ "NSURLSessionTaskDelegate"
+ "Q"
+ "Q16@0:8"
+ "SecXPCNetworkURL"
+ "T#,R"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "TQ,R"
+ "URL"
+ "URLSession:dataTask:didBecomeDownloadTask:"
+ "URLSession:dataTask:didBecomeStreamTask:"
+ "URLSession:dataTask:didReceiveData:"
+ "URLSession:dataTask:didReceiveResponse:completionHandler:"
+ "URLSession:dataTask:willCacheResponse:completionHandler:"
+ "URLSession:didBecomeInvalidWithError:"
+ "URLSession:didCreateTask:"
+ "URLSession:didReceiveChallenge:completionHandler:"
+ "URLSession:task:didCompleteWithError:"
+ "URLSession:task:didFinishCollectingMetrics:"
+ "URLSession:task:didReceiveChallenge:completionHandler:"
+ "URLSession:task:didReceiveInformationalResponse:"
+ "URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:"
+ "URLSession:task:needNewBodyStream:"
+ "URLSession:task:needNewBodyStreamFromOffset:completionHandler:"
+ "URLSession:task:willBeginDelayedRequest:completionHandler:"
+ "URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:"
+ "URLSession:taskIsWaitingForConnectivity:"
+ "URLSessionDidFinishEventsForBackgroundURLSession:"
+ "URLWithString:"
+ "Vv16@0:8"
+ "^{_NSZone=}16@0:8"
+ "_completion"
+ "_data"
+ "_exceededCap"
+ "_maxBytes"
+ "_response"
+ "allowedURLFromCString:options:error:"
+ "appendData:"
+ "autorelease"
+ "cancel"
+ "class"
+ "componentsWithString:"
+ "conformsToProtocol:"
+ "copy"
+ "data"
+ "dataTaskWithRequest:"
+ "debugDescription"
+ "ephemeralSessionConfiguration"
+ "finishTasksAndInvalidate"
+ "hash"
+ "host"
+ "http"
+ "https"
+ "initInMemoryStore"
+ "initWithMaxBytes:callback:"
+ "initWithUTF8String:"
+ "isAllowedURL:options:"
+ "isEqual:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "lowercaseString"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "release"
+ "respondsToSelector:"
+ "resume"
+ "retain"
+ "retainCount"
+ "scheme"
+ "scheme:isAllowedByOptions:"
+ "self"
+ "sessionWithConfiguration:delegate:delegateQueue:"
+ "setError:code:"
+ "setHTTPAdditionalHeaders:"
+ "setHTTPCookieStorage:"
+ "setURLCache:"
+ "setURLCredentialStorage:"
+ "set_hstsStorage:"
+ "superclass"
+ "v24@0:8@\"NSURLSession\"16"
+ "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
+ "v32@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24"
+ "v32@0:8@16@24"
+ "v32@0:8^@16q24"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSData\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionDownloadTask\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionStreamTask\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSError\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLSessionTaskMetrics\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@?<v@?@\"NSInputStream\">32"
+ "v40@0:8@16@24@?32"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSCachedURLResponse\"32@?<v@?@\"NSCachedURLResponse\">40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLResponse\"32@?<v@?q>40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLAuthenticationChallenge\"32@?<v@?q@\"NSURLCredential\">40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLRequest\"32@?<v@?q@\"NSURLRequest\">40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32@?<v@?@\"NSInputStream\">40"
+ "v48@0:8@16@24@32@?40"
+ "v48@0:8@16@24q32@?40"
+ "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32@\"NSURLRequest\"40@?<v@?@\"NSURLRequest\">48"
+ "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32q40q48"
+ "v56@0:8@16@24@32@40@?48"
+ "v56@0:8@16@24q32q40q48"
+ "zone"
- "@"
- "@\"NSMutableURLRequest\""
- "@\"NSURL\""
- "@24@0:8@16"
- "AcmeClient"
- "T@,&,Vurl"
- "T@,&,VurlRequest"
- "T@,W,Vdelegate"
- "delegate"
- "initWithString:"
- "initWithURLString:"
- "post:withMethod:contentType:"
- "sendAsynchronousRequest:queue:completionHandler:"
- "setDelegate:"
- "setUrl:"
- "setUrlRequest:"
- "start3:"
- "stringByAddingPercentEscapesUsingEncoding:"
- "urlRequest"
- "v24@0:8@?16"
```
