## NetworkServiceProxy

> `/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy`

```diff

-896.0.0.0.1
-  __TEXT.__text: 0x48a48
+898.0.0.0.0
+  __TEXT.__text: 0x48c48
   __TEXT.__auth_stubs: 0xdb0
   __TEXT.__objc_methlist: 0x4174
   __TEXT.__const: 0x360
   __TEXT.__gcc_except_tab: 0x90
   __TEXT.__cstring: 0x4fd4
-  __TEXT.__oslogstring: 0x2c24
-  __TEXT.__unwind_info: 0xc50
+  __TEXT.__oslogstring: 0x2c53
+  __TEXT.__unwind_info: 0xc68
   __TEXT.__objc_classname: 0x4e3
-  __TEXT.__objc_methname: 0x8c49
-  __TEXT.__objc_methtype: 0x1133
+  __TEXT.__objc_methname: 0x8c6a
+  __TEXT.__objc_methtype: 0x1139
   __TEXT.__objc_stubs: 0x4e20
-  __DATA_CONST.__got: 0x380
-  __DATA_CONST.__const: 0xb18
+  __DATA_CONST.__got: 0x388
+  __DATA_CONST.__const: 0xb40
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libboringssl.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 027058CE-FDC5-3B24-8162-393ADD48F9D2
+  UUID: 04E20296-5829-359C-8167-A98A082B18D0
   Functions: 1479
-  Symbols:   4474
-  CStrings:  3390
+  Symbols:   4476
+  CStrings:  3391
 
Symbols:
+ -[NSPServerClient fetchKnownPrivateAccessTokenKeyWithFetcher:allowRetry:completionHandler:]
+ -[NSPServerClient fetchPrivateAccessTokenPairWithFetcher:allowRetry:completionHandler:]
+ -[NSPServerClient fetchPrivateAccessTokenWithFetcher:allowRetry:completionHandler:]
+ ___83-[NSPServerClient fetchPrivateAccessTokenWithFetcher:allowRetry:completionHandler:]_block_invoke
+ ___87-[NSPServerClient fetchPrivateAccessTokenPairWithFetcher:allowRetry:completionHandler:]_block_invoke
+ ___91-[NSPServerClient fetchKnownPrivateAccessTokenKeyWithFetcher:allowRetry:completionHandler:]_block_invoke
+ ___block_descriptor_57_e8_32s40s48bs_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8s48l8
+ __xpc_error_connection_invalid
+ _objc_msgSend$fetchKnownPrivateAccessTokenKeyWithFetcher:allowRetry:completionHandler:
+ _objc_msgSend$fetchPrivateAccessTokenPairWithFetcher:allowRetry:completionHandler:
+ _objc_msgSend$fetchPrivateAccessTokenWithFetcher:allowRetry:completionHandler:
- -[NSPServerClient fetchKnownPrivateAccessTokenKeyWithFetcher:completionHandler:]
- -[NSPServerClient fetchPrivateAccessTokenPairWithFetcher:completionHandler:]
- -[NSPServerClient fetchPrivateAccessTokenWithFetcher:completionHandler:]
- ___72-[NSPServerClient fetchPrivateAccessTokenWithFetcher:completionHandler:]_block_invoke
- ___76-[NSPServerClient fetchPrivateAccessTokenPairWithFetcher:completionHandler:]_block_invoke
- ___80-[NSPServerClient fetchKnownPrivateAccessTokenKeyWithFetcher:completionHandler:]_block_invoke
- _objc_msgSend$fetchKnownPrivateAccessTokenKeyWithFetcher:completionHandler:
- _objc_msgSend$fetchPrivateAccessTokenPairWithFetcher:completionHandler:
- _objc_msgSend$fetchPrivateAccessTokenWithFetcher:completionHandler:
CStrings:
+ "Token fetcher got invalid connection, retrying"
+ "fetchKnownPrivateAccessTokenKeyWithFetcher:allowRetry:completionHandler:"
+ "fetchPrivateAccessTokenPairWithFetcher:allowRetry:completionHandler:"
+ "fetchPrivateAccessTokenWithFetcher:allowRetry:completionHandler:"
+ "v36@0:8@\"NSPPrivateAccessTokenFetcher\"16B24@?<v@?@\"NSData\"@\"NSData\"@\"NSData\"@\"NSError\">28"
+ "v36@0:8@\"NSPPrivateAccessTokenFetcher\"16B24@?<v@?@\"NSData\"@\"NSError\">28"
- "fetchKnownPrivateAccessTokenKeyWithFetcher:completionHandler:"
- "fetchPrivateAccessTokenPairWithFetcher:completionHandler:"
- "fetchPrivateAccessTokenWithFetcher:completionHandler:"
- "v32@0:8@\"NSPPrivateAccessTokenFetcher\"16@?<v@?@\"NSData\"@\"NSData\"@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSPPrivateAccessTokenFetcher\"16@?<v@?@\"NSData\"@\"NSError\">24"

```
