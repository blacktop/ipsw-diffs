## WebThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/WebThumbnailExtension.appex/Contents/MacOS/WebThumbnailExtension`

```diff

-199.4.3.0.0
-  __TEXT.__text: 0x2590
-  __TEXT.__auth_stubs: 0x280
-  __TEXT.__objc_stubs: 0xce0
-  __TEXT.__objc_methlist: 0x280
+199.5.3.0.0
+  __TEXT.__text: 0x2464
+  __TEXT.__auth_stubs: 0x2e0
+  __TEXT.__objc_stubs: 0xaa0
+  __TEXT.__objc_methlist: 0x408
   __TEXT.__const: 0x78
-  __TEXT.__objc_methname: 0xf89
-  __TEXT.__cstring: 0x1ed
+  __TEXT.__objc_methname: 0xde8
+  __TEXT.__cstring: 0x213
   __TEXT.__objc_classname: 0x7a
-  __TEXT.__objc_methtype: 0x537
+  __TEXT.__objc_methtype: 0x591
   __TEXT.__oslogstring: 0x61
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__unwind_info: 0x148
-  __DATA_CONST.__auth_got: 0x150
-  __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x240
+  __TEXT.__unwind_info: 0x138
+  __DATA_CONST.__auth_got: 0x180
+  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x988
-  __DATA.__objc_selrefs: 0x3a8
-  __DATA.__objc_ivar: 0x30
+  __DATA.__objc_const: 0x5b0
+  __DATA.__objc_selrefs: 0x420
+  __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x120
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /System/Library/PrivateFrameworks/QuickLookSupport.framework/Versions/A/QuickLookSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E7C1BB4E-3F9B-30CA-8422-D940CFDA1778
-  Functions: 76
-  Symbols:   84
-  CStrings:  265
+  UUID: 9D4D1F24-6547-3242-86F6-9D17FA1C6F0A
+  Functions: 70
+  Symbols:   85
+  CStrings:  244
 
Symbols:
+ _QLThumbnailErrorDomain
+ _dispatch_activate
+ _dispatch_after
+ _dispatch_block_cancel
+ _dispatch_block_create
+ _dispatch_queue_attr_make_initially_inactive
+ _dispatch_queue_create_with_target$V2
+ _dispatch_time
- _NSCocoaErrorDomain
- _NSRunLoopCommonModes
- _OBJC_CLASS_$_NSDate
- _OBJC_CLASS_$_NSRunLoop
- _OBJC_CLASS_$_NSTimer
- __NSConcreteGlobalBlock
- _objc_setProperty_atomic_copy
CStrings:
+ "@\"NSObject<OS_dispatch_queue>\""
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_afterLoadingQueue"
+ "_afterLoadingQueue"
+ "_close"
+ "afterLoadingQueue"
+ "com.apple.quicklook.thumbnailing.web.afterloading.queue"
+ "load"
+ "setAfterLoadingQueue:"
+ "v44@0:8@\"WKWebView\"16@\"WKBackForwardListItem\"24B32@?<v@?B>36"
+ "v44@0:8@16@24B32@?36"
+ "webView:shouldGoToBackForwardListItem:willUseInstantBack:completionHandler:"
- "@\"NSTimer\""
- "@?"
- "@?16@0:8"
- "T@\"NSTimer\",&,V_loadingTimeoutTimer"
- "T@?,C,V_loadCompletion"
- "TB,V_startedLoad"
- "_configureWebView"
- "_loadCompletion"
- "_loadingTimeoutTimer"
- "_setupLoadTimeoutTimer"
- "_startedLoad"
- "_teardownLoadTimeoutTimer"
- "_webPageLoadingTimedOut:"
- "addTimer:forMode:"
- "allWebsiteDataTypes"
- "configuration"
- "currentRunLoop"
- "dateWithTimeIntervalSinceNow:"
- "distantPast"
- "initWithFireDate:interval:target:selector:userInfo:repeats:"
- "invalidate"
- "load:"
- "loadCompletion"
- "loadingTimeoutTimer"
- "removeDataOfTypes:modifiedSince:completionHandler:"
- "setJavaScriptCanOpenWindowsAutomatically:"
- "setLoadCompletion:"
- "setLoadingTimeoutTimer:"
- "setStartedLoad:"
- "startedLoad"
- "v16@?0@\"NSError\"8"
- "websiteDataStore"

```
