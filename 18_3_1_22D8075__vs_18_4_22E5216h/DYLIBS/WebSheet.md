## WebSheet

> `/System/Library/PrivateFrameworks/WebSheet.framework/WebSheet`

```diff

-290.0.0.0.0
-  __TEXT.__text: 0x60b0
+294.100.3.0.0
+  __TEXT.__text: 0x61ac
   __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_methlist: 0x644
-  __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x1086
-  __TEXT.__unwind_info: 0x238
-  __TEXT.__objc_classname: 0x152
-  __TEXT.__objc_methname: 0x2d8d
-  __TEXT.__objc_methtype: 0xfe3
-  __TEXT.__objc_stubs: 0x2340
-  __DATA_CONST.__got: 0x200
-  __DATA_CONST.__const: 0x150
+  __TEXT.__objc_methlist: 0xaf8
+  __TEXT.__const: 0x60
+  __TEXT.__cstring: 0x1084
+  __TEXT.__gcc_except_tab: 0x2c
+  __TEXT.__unwind_info: 0x248
+  __TEXT.__objc_classname: 0x151
+  __TEXT.__objc_methname: 0x2cca
+  __TEXT.__objc_methtype: 0xfdc
+  __TEXT.__objc_stubs: 0x2260
+  __DATA_CONST.__got: 0x1e8
+  __DATA_CONST.__const: 0x178
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xab8
+  __DATA_CONST.__objc_selrefs: 0xc78
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x210
+  __AUTH_CONST.__auth_got: 0x218
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x980
-  __AUTH_CONST.__objc_const: 0x1b50
+  __AUTH_CONST.__cfstring: 0x940
+  __AUTH_CONST.__objc_const: 0x1230
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0xc4
+  __DATA.__objc_ivar: 0xc8
   __DATA.__data: 0x360
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/PrivateFrameworks/WebUI.framework/WebUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 160
-  Symbols:   309
-  CStrings:  740
+  Functions: 165
+  Symbols:   313
+  CStrings:  727
 
Symbols:
+ __Block_object_dispose
+ __Unwind_Resume
+ ___objc_personality_v0
+ _objc_retain_x1
+ _objc_retain_x5
- _OBJC_CLASS_$_WebPreferences
- _OBJC_CLASS_$_WebView
- _WebKitErrorDomain
- _WebThreadCallDelegate
- _WebThreadIsCurrent
- _WebThreadLock
- _WebThreadMakeNSInvocation
CStrings:
+ "TB,N,V_carPlayAndInternet"
+ "WKDownloadDelegate"
+ "_canHandleRequest"
+ "_carPlayAndInternet"
+ "_lp_userVisibleString"
+ "carPlayAndInternet"
+ "com.apple.captive.websheet"
+ "download:decideDestinationUsingResponse:suggestedFilename:completionHandler:"
+ "download:decidePlaceholderPolicy:"
+ "download:didFailWithError:resumeData:"
+ "download:didReceiveAuthenticationChallenge:completionHandler:"
+ "download:didReceiveFinalURL:"
+ "download:didReceivePlaceholderURL:completionHandler:"
+ "download:willPerformHTTPRedirection:newRequest:decisionHandler:"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "failed to find"
+ "fileURLWithPath:"
+ "found"
+ "rangeOfString:options:"
+ "setCarPlayAndInternet:"
+ "setCarPlayAndInternetMode:"
+ "setSourceApplicationSecondaryIdentifier:"
+ "v24@0:8@\"WKDownload\"16"
+ "v32@0:8@\"WKDownload\"16@\"NSURL\"24"
+ "v32@0:8@\"WKDownload\"16@?<v@?q@\"NSURL\">24"
+ "v32@?0@8@16^B24"
+ "v40@0:8@\"WKDownload\"16@\"NSError\"24@\"NSData\"32"
+ "v40@0:8@\"WKDownload\"16@\"NSURL\"24@?<v@?>32"
+ "v40@0:8@\"WKDownload\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
+ "v48@0:8@\"WKDownload\"16@\"NSHTTPURLResponse\"24@\"NSURLRequest\"32@?<v@?q>40"
+ "v48@0:8@\"WKDownload\"16@\"NSURLResponse\"24@\"NSString\"32@?<v@?@\"NSURL\">40"
+ "v48@0:8@\"WKWebView\"16@\"WKOpenPanelParameters\"24@\"WKFrameInfo\"32@?<v@?@\"NSArray\">40"
+ "webView:runOpenPanelWithParameters:initiatedByFrame:completionHandler:"
+ "willSubmitFormValues"
+ "willSubmitFormValues: %s username/password"
- "@\"NSString\"40@0:8@\"_WKDownload\"16@\"NSString\"24^B32"
- "@40@0:8@16@24^B32"
- "B32@0:8@\"_WKDownload\"16@\"NSString\"24"
- "_WKDownloadDelegate"
- "_canHandleRequest:"
- "_download:decideDestinationWithSuggestedFilename:allowOverwrite:"
- "_download:decideDestinationWithSuggestedFilename:completionHandler:"
- "_download:didCreateDestination:"
- "_download:didFailWithError:"
- "_download:didReceiveAuthenticationChallenge:completionHandler:"
- "_download:didReceiveData:"
- "_download:didReceiveResponse:"
- "_download:didReceiveServerRedirectToURL:"
- "_download:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:"
- "_download:shouldDecodeSourceDataOfMIMEType:"
- "_downloadDidCancel:"
- "_downloadDidFinish:"
- "_downloadDidStart"
- "_downloadDidStart:"
- "_downloadProcessDidCrash:"
- "_setDownloadDelegate:"
- "_synchronizeWebStoragePolicyWithCookiePolicy"
- "_web_userVisibleString"
- "cancel"
- "configuration"
- "didReceiveData"
- "didReceiveResponse"
- "found valid credentials from values provided by willSubmitFormValues"
- "objectForKeyedSubscript:"
- "processPool"
- "setArgument:atIndex:"
- "setDatabasesEnabled:"
- "setLocalStorageEnabled:"
- "setOfflineWebApplicationCacheEnabled:"
- "setPrivateBrowsingEnabled:"
- "setStorageTrackerEnabled:"
- "standardPreferences"
- "username"
- "v24@0:8@\"_WKDownload\"16"
- "v32@0:8@\"_WKDownload\"16@\"NSError\"24"
- "v32@0:8@\"_WKDownload\"16@\"NSString\"24"
- "v32@0:8@\"_WKDownload\"16@\"NSURL\"24"
- "v32@0:8@\"_WKDownload\"16@\"NSURLResponse\"24"
- "v32@0:8@\"_WKDownload\"16Q24"
- "v40@0:8@\"_WKDownload\"16@\"NSString\"24@?<v@?B@\"NSString\">32"
- "v40@0:8@\"_WKDownload\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
- "v48@0:8@\"_WKDownload\"16Q24Q32Q40"
- "v48@0:8@16Q24Q32Q40"

```
