## HTTPServer

> `/System/Library/PrivateFrameworks/HTTPServer.framework/Versions/A/HTTPServer`

```diff

 39.0.0.0.0
-  __TEXT.__text: 0x24ec4
+  __TEXT.__text: 0x25830
   __TEXT.__auth_stubs: 0xa20
-  __TEXT.__objc_methlist: 0x1c7c
+  __TEXT.__objc_methlist: 0x1ff4
   __TEXT.__const: 0xf8
   __TEXT.__cstring: 0x1c32
   __TEXT.__oslogstring: 0x9b2
   __TEXT.__gcc_except_tab: 0x268
-  __TEXT.__unwind_info: 0x958
+  __TEXT.__unwind_info: 0x968
   __TEXT.__objc_classname: 0x29a
   __TEXT.__objc_methname: 0x3f64
   __TEXT.__objc_methtype: 0xb56

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1458
+  __DATA_CONST.__objc_selrefs: 0x1520
   __DATA_CONST.__objc_superrefs: 0xd8
   __AUTH_CONST.__auth_got: 0x520
   __AUTH_CONST.__const: 0x5d0
   __AUTH_CONST.__cfstring: 0x1b80
-  __AUTH_CONST.__objc_const: 0x4988
+  __AUTH_CONST.__objc_const: 0x4330
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0x780
   __DATA.__objc_ivar: 0x31c

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9C3C7D67-AB80-31CF-9F7E-5D201204FCA9
-  Functions: 831
-  Symbols:   2250
+  UUID: C8D45800-C828-395F-9F36-E9C4A53CDA4D
+  Functions: 880
+  Symbols:   2303
   CStrings:  1548
 
Symbols:
+ +[HTTPConnection initialize].cold.1
+ +[HTTPServer executeBonjourBlock:].cold.2
+ -[DDAbstractLogger logFormatter].cold.1
+ -[DDAbstractLogger logFormatter].cold.2
+ -[DDAbstractLogger setLogFormatter:].cold.1
+ -[DDAbstractLogger setLogFormatter:].cold.2
+ -[DDFileLogger rollLogFile].cold.1
+ -[DDFileLogger setMaximumFileSize:].cold.1
+ -[DDFileLogger setMaximumFileSize:].cold.2
+ -[DDFileLogger setRollingFrequency:].cold.1
+ -[DDFileLogger setRollingFrequency:].cold.2
+ -[GCDAsyncReadPacket readLengthForNonTermWithHint:].cold.1
+ -[GCDAsyncReadPacket readLengthForNonTermWithHint:].cold.2
+ -[GCDAsyncReadPacket readLengthForTermWithHint:shouldPreBuffer:].cold.1
+ -[GCDAsyncReadPacket readLengthForTermWithHint:shouldPreBuffer:].cold.2
+ -[GCDAsyncReadPacket readLengthForTermWithPreBuffer:found:].cold.1
+ -[GCDAsyncReadPacket readLengthForTermWithPreBuffer:found:].cold.2
+ -[GCDAsyncReadPacket searchForTermAfterPreBuffering:].cold.1
+ -[GCDAsyncSocket closeWithError:].cold.1
+ -[GCDAsyncSocket completeCurrentRead].cold.1
+ -[GCDAsyncSocket completeCurrentWrite].cold.1
+ -[GCDAsyncSocket connectWithAddress4:address6:error:].cold.1
+ -[GCDAsyncSocket didConnect:].cold.1
+ -[GCDAsyncSocket didNotConnect:error:].cold.1
+ -[GCDAsyncSocket doReadData].cold.1
+ -[GCDAsyncSocket doReadData].cold.2
+ -[GCDAsyncSocket doWriteData].cold.2
+ -[GCDAsyncSocket flushSSLBuffers].cold.1
+ -[GCDAsyncSocket initWithDelegate:delegateQueue:socketQueue:].cold.1
+ -[GCDAsyncSocket initWithDelegate:delegateQueue:socketQueue:].cold.2
+ -[GCDAsyncSocket initWithDelegate:delegateQueue:socketQueue:].cold.3
+ -[GCDAsyncSocket lookup:didFail:].cold.1
+ -[GCDAsyncSocket lookup:didSucceedWithAddress4:address6:].cold.1
+ -[GCDAsyncSocket lookup:didSucceedWithAddress4:address6:].cold.2
+ -[GCDAsyncSocket maybeClose].cold.1
+ -[GCDAsyncSocket maybeDequeueRead].cold.1
+ -[GCDAsyncSocket maybeDequeueWrite].cold.1
+ -[GCDAsyncSocket preConnectWithInterface:error:].cold.1
+ -[HTTPConnection dateAsString:].cold.1
+ -[HTTPConnection replyToHTTPRequest].cold.2
+ -[HTTPConnection socket:didWriteDataWithTag:].cold.1
+ -[HTTPData initWithSendfile:offset:length:].cold.1
+ -[HTTPData initWithSendfile:offset:length:].cold.2
+ -[HTTPServer publishBonjour].cold.2
+ -[HTTPServer unpublishBonjour].cold.2
+ SSLReadFunction.cold.1
+ SSLWriteFunction.cold.1
+ __42-[HTTPAsyncFileResponse readDataOfLength:]_block_invoke.cold.1
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HTTPServer/CocoaHTTPServer/Core/HTTPConnection.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HTTPServer/CocoaHTTPServer/Core/HTTPServer.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HTTPServer/CocoaHTTPServer/Core/Responses/HTTPAsyncFileResponse.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HTTPServer/CocoaHTTPServer/Core/Responses/HTTPDataResponse.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HTTPServer/CocoaHTTPServer/Core/Responses/HTTPDynamicFileResponse.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HTTPServer/CocoaHTTPServer/Core/Responses/HTTPFileResponse.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HTTPServer/CocoaHTTPServer/Core/Responses/HTTPRedirectResponse.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HTTPServer/CocoaHTTPServer/Core/Responses/HTTPSendFileResponse.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/HTTPServer/CocoaHTTPServer/Core/HTTPConnection.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/HTTPServer/CocoaHTTPServer/Core/HTTPServer.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/HTTPServer/CocoaHTTPServer/Core/Responses/HTTPAsyncFileResponse.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/HTTPServer/CocoaHTTPServer/Core/Responses/HTTPDataResponse.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/HTTPServer/CocoaHTTPServer/Core/Responses/HTTPDynamicFileResponse.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/HTTPServer/CocoaHTTPServer/Core/Responses/HTTPFileResponse.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/HTTPServer/CocoaHTTPServer/Core/Responses/HTTPRedirectResponse.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/HTTPServer/CocoaHTTPServer/Core/Responses/HTTPSendFileResponse.m"

```
