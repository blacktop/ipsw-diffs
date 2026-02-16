## WebSheet

> `/System/Library/PrivateFrameworks/WebSheet.framework/WebSheet`

```diff

-320.60.1.0.0
-  __TEXT.__text: 0x7448
-  __TEXT.__auth_stubs: 0x430
+320.100.6.0.0
+  __TEXT.__text: 0x7f84
+  __TEXT.__auth_stubs: 0x460
   __TEXT.__objc_methlist: 0xc40
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x151a
+  __TEXT.__cstring: 0x1553
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__unwind_info: 0x270
+  __TEXT.__unwind_info: 0x298
   __TEXT.__objc_classname: 0x1a9
-  __TEXT.__objc_methname: 0x341c
-  __TEXT.__objc_methtype: 0x137c
-  __TEXT.__objc_stubs: 0x26a0
-  __DATA_CONST.__got: 0x250
-  __DATA_CONST.__const: 0x208
+  __TEXT.__objc_methname: 0x351e
+  __TEXT.__objc_methtype: 0x1421
+  __TEXT.__objc_stubs: 0x2780
+  __DATA_CONST.__got: 0x268
+  __DATA_CONST.__const: 0x280
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdf0
+  __DATA_CONST.__objc_selrefs: 0xe30
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x228
+  __AUTH_CONST.__auth_got: 0x240
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0xb00
-  __AUTH_CONST.__objc_const: 0x14d8
+  __AUTH_CONST.__cfstring: 0xb20
+  __AUTH_CONST.__objc_const: 0x14d0
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0xe8
   __DATA.__data: 0x3c0

   - /System/Library/PrivateFrameworks/WebUI.framework/WebUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 155CC0F8-A261-3475-9AA0-2BEC9A245D01
-  Functions: 181
-  Symbols:   1014
-  CStrings:  911
+  UUID: 40D7E8B6-CB7C-3ED3-9EFF-B47FBD43D644
+  Functions: 188
+  Symbols:   1044
+  CStrings:  923
 
Symbols:
+ -[WSWebSheetView updateTrustAnalytics:]
+ GCC_except_table118
+ _CFRetain
+ _OBJC_CLASS_$_CertUIPrompt
+ _OBJC_CLASS_$_CertUITrustManager
+ _OBJC_IVAR_$_WSWebSheetView._trustPromptInProgress
+ ___39-[WSWebSheetView updateTrustAnalytics:]_block_invoke
+ ___78-[WSWebSheetView webView:didReceiveAuthenticationChallenge:completionHandler:]_block_invoke_3
+ ___78-[WSWebSheetView webView:didReceiveAuthenticationChallenge:completionHandler:]_block_invoke_4
+ ___78-[WSWebSheetView webView:didReceiveAuthenticationChallenge:completionHandler:]_block_invoke_5
+ ___78-[WSWebSheetView webView:didReceiveAuthenticationChallenge:completionHandler:]_block_invoke_6
+ ___78-[WSWebSheetView webView:didReceiveAuthenticationChallenge:completionHandler:]_block_invoke_7
+ ___78-[WSWebSheetView webView:didReceiveAuthenticationChallenge:completionHandler:]_block_invoke_8
+ ___78-[WSWebSheetView webView:didReceiveAuthenticationChallenge:completionHandler:]_block_invoke_9
+ ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e8_v12?0i8ls32l8s48l8s40l8
+ ___block_literal_global.133
+ ___block_literal_global.223
+ ___block_literal_global.228
+ ___block_literal_global.349
+ ___block_literal_global.391
+ ___block_literal_global.777
+ _dispatch_sync
+ _kCertUIServiceTypeHTTPS
+ _objc_msgSend$actionForSSLTrust:hostname:service:
+ _objc_msgSend$addSSLTrust:hostname:service:
+ _objc_msgSend$defaultTrustManager
+ _objc_msgSend$defaultWebpagePreferences
+ _objc_msgSend$setHost:
+ _objc_msgSend$setSecurityRestrictionMode:
+ _objc_msgSend$setService:
+ _objc_msgSend$setTrust:
+ _objc_msgSend$showPromptWithResponseBlock:
+ _objc_msgSend$updateTrustAnalytics:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x28
- -[WSWebSheetView isCertTrustDone]
- -[WSWebSheetView setIsCertTrustDone:]
- GCC_except_table109
- _OBJC_IVAR_$_WSWebSheetView._isCertTrustDone
- ___block_descriptor_57_e8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_literal_global.135
- ___block_literal_global.225
- ___block_literal_global.230
- ___block_literal_global.345
- ___block_literal_global.387
- ___block_literal_global.773
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_handleCertificateError:newhost:
- _objc_msgSend$_precheckTrustForServerCertificate:host:
- _objc_msgSend$setJITEnabled:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x24
CStrings:
+ "_trustPromptInProgress"
+ "_webView:willSubmitFormValues:frameInfo:sourceFrameInfo:userObject:requestURL:method:submissionHandler:"
+ "actionForSSLTrust:hostname:service:"
+ "addSSLTrust:hostname:service:"
+ "defaultTrustManager"
+ "defaultWebpagePreferences"
+ "setHost:"
+ "setSecurityRestrictionMode:"
+ "setService:"
+ "setTrust:"
+ "showPromptWithResponseBlock:"
+ "updateTrustAnalytics:"
+ "user's trust is required for [%@]'s certificate"
+ "v12@?0i8"
+ "v80@0:8@\"WKWebView\"16@\"NSDictionary\"24@\"WKFrameInfo\"32@\"WKFrameInfo\"40@\"NSObject<NSSecureCoding>\"48@\"NSURL\"56@\"NSString\"64@?<v@?>72"
+ "v80@0:8@16@24@32@40@48@56@64@?72"
- "TB,N,V_isCertTrustDone"
- "_isCertTrustDone"
- "isCertTrustDone"
- "setIsCertTrustDone:"
- "setJITEnabled:"

```
