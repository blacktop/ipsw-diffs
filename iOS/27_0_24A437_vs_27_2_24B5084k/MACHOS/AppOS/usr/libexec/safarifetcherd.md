## safarifetcherd

> `/usr/libexec/safarifetcherd`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`

```diff

-7625.1.29.10.29
-  __TEXT.__text: 0x933c
-  __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_stubs: 0x2480
-  __TEXT.__objc_methlist: 0x1394
-  __TEXT.__gcc_except_tab: 0xb10
+7625.2.4.1.0
+  __TEXT.__text: 0x94bc
+  __TEXT.__auth_stubs: 0x800
+  __TEXT.__objc_stubs: 0x24c0
+  __TEXT.__objc_methlist: 0x149c
+  __TEXT.__gcc_except_tab: 0xb30
   __TEXT.__const: 0x98
-  __TEXT.__objc_methname: 0x54b0
   __TEXT.__cstring: 0x451
-  __TEXT.__objc_classname: 0x162
-  __TEXT.__objc_methtype: 0x251d
+  __TEXT.__objc_methname: 0x57db
+  __TEXT.__objc_classname: 0x1a9
+  __TEXT.__objc_methtype: 0x2a60
   __TEXT.__oslogstring: 0x1011
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x5c0
-  __DATA_CONST.__const: 0x328
+  __TEXT.__unwind_info: 0x5d0
+  __DATA_CONST.__const: 0x348
   __DATA_CONST.__cfstring: 0x480
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x410
-  __DATA_CONST.__got: 0x2d8
-  __DATA.__objc_const: 0x1630
-  __DATA.__objc_selrefs: 0x1190
+  __DATA_CONST.__auth_got: 0x418
+  __DATA_CONST.__got: 0x2f0
+  __DATA.__objc_const: 0x1768
+  __DATA.__objc_selrefs: 0x1210
   __DATA.__objc_ivar: 0xf8
   __DATA.__objc_data: 0x190
-  __DATA.__data: 0x368
+  __DATA.__data: 0x488
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 265
-  Symbols:   229
-  CStrings:  1023
+  Functions: 266
+  Symbols:   233
+  CStrings:  1062
 
Symbols:
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_CLASS_$_NSURLSession
+ _OBJC_CLASS_$_NSURLSessionConfiguration
+ _OBJC_CLASS_$__WKWebsiteDataStoreConfiguration
+ _objc_retain_x4
- _OBJC_CLASS_$_NSURLConnection
CStrings:
+ "@\"NSURLSessionDataTask\""
+ "NSURLSessionDataDelegate"
+ "NSURLSessionDelegate"
+ "NSURLSessionTaskDelegate"
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
+ "_dataTask"
+ "_sharedURLSession"
+ "dataTaskWithRequest:"
+ "initNonPersistentConfiguration"
+ "mainQueue"
+ "resume"
+ "safari_ephemeralSessionConfiguration"
+ "sessionWithConfiguration:delegate:delegateQueue:"
+ "setSourceApplicationBundleIdentifier:"
+ "v24@0:8@\"NSURLSession\"16"
+ "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
+ "v32@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSData\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionDownloadTask\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionStreamTask\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSError\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLSessionTaskMetrics\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@?<v@?@\"NSInputStream\">32"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSCachedURLResponse\"32@?<v@?@\"NSCachedURLResponse\">40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLResponse\"32@?<v@?q>40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLAuthenticationChallenge\"32@?<v@?q@\"NSURLCredential\">40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLRequest\"32@?<v@?q@\"NSURLRequest\">40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32@?<v@?@\"NSInputStream\">40"
+ "v48@0:8@16@24q32@?40"
+ "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32@\"NSURLRequest\"40@?<v@?@\"NSURLRequest\">48"
+ "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32q40q48"
+ "v56@0:8@16@24q32q40q48"
- "@\"NSURLConnection\""
- "_URLConnection"
- "_cancelConnectionAndFetchNextIcon"
- "cancelAuthenticationChallenge:"
- "connection:didFailWithError:"
- "connection:didReceiveAuthenticationChallenge:"
- "connection:didReceiveData:"
- "connection:didReceiveResponse:"
- "connectionDidFinishLoading:"
- "initWithRequest:delegate:"
- "nonPersistentDataStore"
- "sender"
- "useCredential:forAuthenticationChallenge:"
```
