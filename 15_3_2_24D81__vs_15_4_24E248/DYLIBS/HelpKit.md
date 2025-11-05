## HelpKit

> `/System/iOSSupport/System/Library/PrivateFrameworks/HelpKit.framework/Versions/A/HelpKit`

```diff

-191.0.0.0.0
-  __TEXT.__text: 0x28b74
+192.0.0.0.0
+  __TEXT.__text: 0x28a70
   __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__objc_methlist: 0x2cbc
+  __TEXT.__objc_methlist: 0x342c
   __TEXT.__const: 0xe8
   __TEXT.__gcc_except_tab: 0xc70
   __TEXT.__cstring: 0x18ce
   __TEXT.__oslogstring: 0x329
   __TEXT.__dlopen_cstrs: 0x10e
   __TEXT.__ustring: 0x82
-  __TEXT.__unwind_info: 0xa48
+  __TEXT.__unwind_info: 0xa60
   __TEXT.__objc_classname: 0x5cb
-  __TEXT.__objc_methname: 0x9776
-  __TEXT.__objc_methtype: 0x1cfb
+  __TEXT.__objc_methname: 0x97c1
+  __TEXT.__objc_methtype: 0x1d4d
   __TEXT.__objc_stubs: 0x73e0
   __DATA_CONST.__got: 0x498
   __DATA_CONST.__const: 0xea0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2300
+  __DATA_CONST.__objc_selrefs: 0x2558
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x88
   __AUTH_CONST.__auth_got: 0x388
   __AUTH_CONST.__const: 0x320
   __AUTH_CONST.__cfstring: 0x2b60
-  __AUTH_CONST.__objc_const: 0x5db0
+  __AUTH_CONST.__objc_const: 0x5080
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH.__objc_data: 0xbe0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1F3DEDF4-DE10-3F63-B437-863F06599A41
-  Functions: 1083
-  Symbols:   3151
-  CStrings:  2690
+  UUID: B88B2ECF-DE1C-3EAA-BBBD-A73198222F92
+  Functions: 1101
+  Symbols:   3169
+  CStrings:  2693
 
Symbols:
+ +[HLPAnalyticsEventController sharedInstance].cold.1
+ +[HLPCommonDefines isInternalBuild].cold.1
+ +[HLPCommonDefines isVisionOS].cold.1
+ +[HLPDataCacheController sharedInstance].cold.1
+ +[HLPFileCacheController sharedInstance].cold.1
+ +[HLPImageCacheController defaultInMemoryImageCache].cold.1
+ +[HLPImageCacheController sharedInstance].cold.1
+ +[HLPJSONCacheController sharedInstance].cold.1
+ +[HLPReachabilityManager defaultManager].cold.1
+ +[HLPStringCacheController sharedInstance].cold.1
+ +[HLPURLSessionACAuthContext defaultContext].cold.1
+ +[HLPURLSessionACAuthHandler canAuthenticateWithURLResponse:].cold.1
+ +[HLPURLSessionHandler sharedInstance].cold.1
+ +[HLPURLSessionManager defaultManager].cold.1
+ +[HLPVideoCacheController sharedInstance].cold.1
+ -[HLPHelpSearchIndexController _fetchAttributesForCSSearchQuery].cold.1
+ -[HLPHelpSearchIndexController _tokenizeSearchTerm:].cold.1
+ HLPLogForCategory.cold.2
+ __block_literal_global.54
+ _objc_msgSend$setSearchBarStyle:
- _objc_msgSend$setBackgroundImage:
CStrings:
+ "setSearchBarStyle:"
+ "v44@0:8@\"WKWebView\"16@\"WKBackForwardListItem\"24B32@?<v@?B>36"
+ "v44@0:8@16@24B32@?36"
+ "webView:shouldGoToBackForwardListItem:willUseInstantBack:completionHandler:"
- "setBackgroundImage:"

```
