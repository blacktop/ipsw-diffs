## XPCTimeStampingService

> `/System/Library/Frameworks/Security.framework/Versions/A/XPCServices/XPCTimeStampingService.xpc/Contents/MacOS/XPCTimeStampingService`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_superrefs`

```diff

-62460.0.55.0.1
-  __TEXT.__text: 0xa80
-  __TEXT.__auth_stubs: 0x2a0
-  __TEXT.__objc_stubs: 0x260
-  __TEXT.__objc_methlist: 0x98
+62460.1.2.0.0
+  __TEXT.__text: 0x11b0
+  __TEXT.__auth_stubs: 0x3a0
+  __TEXT.__objc_stubs: 0x4e0
+  __TEXT.__objc_methlist: 0x28c
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x24
-  __TEXT.__cstring: 0x155
-  __TEXT.__objc_methname: 0x1d3
-  __TEXT.__objc_classname: 0x10
-  __TEXT.__objc_methtype: 0x54
-  __TEXT.__unwind_info: 0xb0
-  __DATA_CONST.__const: 0x90
-  __DATA_CONST.__cfstring: 0xa0
-  __DATA_CONST.__objc_classlist: 0x8
+  __TEXT.__gcc_except_tab: 0x28
+  __TEXT.__cstring: 0x2c0
+  __TEXT.__oslogstring: 0x87
+  __TEXT.__objc_methname: 0x7fe
+  __TEXT.__objc_classname: 0x7a
+  __TEXT.__objc_methtype: 0x6c4
+  __TEXT.__unwind_info: 0xc0
+  __DATA_CONST.__const: 0x60
+  __DATA_CONST.__cfstring: 0x120
+  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x160
-  __DATA_CONST.__got: 0x68
-  __DATA.__objc_const: 0x130
-  __DATA.__objc_selrefs: 0xd0
-  __DATA.__objc_ivar: 0xc
-  __DATA.__objc_data: 0x50
+  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__auth_got: 0x1e0
+  __DATA_CONST.__got: 0xa0
+  __DATA.__objc_const: 0x3f0
+  __DATA.__objc_selrefs: 0x280
+  __DATA.__objc_ivar: 0x14
+  __DATA.__objc_data: 0xa0
+  __DATA.__data: 0x180
+  - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 25
-  Symbols:   66
-  CStrings:  53
+  Functions: 20
+  Symbols:   90
+  CStrings:  176
 
Symbols:
+ _NSURLErrorDomain
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLSession
+ _OBJC_CLASS_$_NSURLSessionConfiguration
+ _OBJC_CLASS_$__NSHSTSStorage
+ ___error
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __os_log_debug_impl
+ __os_log_default
+ __os_log_error_impl
+ __set_user_dir_suffix
+ _audit_token_to_pid
+ _bzero
+ _confstr
+ _exit
+ _free
+ _getenv
+ _getpwuid
+ _getuid
+ _mkdir
+ _objc_autorelease
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _os_log_type_enabled
+ _realpath$DARWIN_EXTSN
+ _sandbox_init_with_parameters
+ _strerror
+ _syslog$DARWIN_EXTSN
- _OBJC_CLASS_$_NSOperationQueue
- _OBJC_CLASS_$_NSURLConnection
- _dispatch_async
- _dispatch_get_global_queue
- _objc_destroyWeak
- _objc_getProperty
- _objc_loadWeak
- _objc_setProperty_atomic
- _objc_storeWeak
CStrings:
+ "#16@0:8"
+ "$HOME not set, falling back to using getpwuid"
+ "@\"NSMutableData\""
+ "@\"NSString\"16@0:8"
+ "@\"NSURLResponse\""
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@32@0:8Q16@?24"
+ "@40@0:8:16@24@32"
+ "@40@0:8r*16Q24^@32"
+ "@?"
+ "B"
+ "B16@0:8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "B32@0:8@16Q24"
+ "Failed to enter XPCTimeStampingService sandbox: %s"
+ "HOME"
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
+ "TimeStampSessionDelegate"
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
+ "User-Agent"
+ "Vv16@0:8"
+ "^{_NSZone=}16@0:8"
+ "_DARWIN_CACHE_DIR"
+ "_HOME"
+ "_TMPDIR"
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
+ "com.apple.security.XPCTimeStampingService"
+ "com.apple.security.tsaclient/1.0"
+ "componentsWithString:"
+ "conformsToProtocol:"
+ "copy"
+ "dataTaskWithRequest:"
+ "debugDescription"
+ "domain"
+ "ephemeralSessionConfiguration"
+ "errorWithDomain:code:userInfo:"
+ "failed to get passwd entry for uid %u"
+ "failed to initialize cache directory (%d): %s"
+ "failed to initialize temporary directory (%d): %s"
+ "failed to resolve cache directory (%d): %s"
+ "failed to resolve home directory: %{darwin.errno}d"
+ "failed to resolve temporary directory (%d): %s"
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
+ "isEqualToString:"
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
+ "v40@0:8@16@24@32"
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
- ".cxx_destruct"
- "@"
- "@\"NSMutableURLRequest\""
- "@\"NSURL\""
- "@24@0:8@16"
- "T@,&,Vurl"
- "T@,&,VurlRequest"
- "T@,W,Vdelegate"
- "TimeStampClient"
- "delegate"
- "initWithString:"
- "initWithURLString:"
- "post:"
- "sendAsynchronousRequest:queue:completionHandler:"
- "setDelegate:"
- "setUrl:"
- "setUrlRequest:"
- "start3:"
- "stringByAddingPercentEscapesUsingEncoding:"
- "url"
- "urlRequest"
- "v24@0:8@?16"
- "v8@?0"
```
