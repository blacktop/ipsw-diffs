## WebThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/WebThumbnailExtension.appex/WebThumbnailExtension`

```diff

-199.4.3.0.0
-  __TEXT.__text: 0x1fdc
-  __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_stubs: 0xc40
-  __TEXT.__objc_methlist: 0x280
+199.5.2.0.0
+  __TEXT.__text: 0x1d94
+  __TEXT.__auth_stubs: 0x410
+  __TEXT.__objc_stubs: 0xa00
+  __TEXT.__objc_methlist: 0x3f8
   __TEXT.__const: 0x78
-  __TEXT.__objc_methname: 0xf5d
-  __TEXT.__cstring: 0x1e2
+  __TEXT.__objc_methname: 0xd70
+  __TEXT.__cstring: 0x208
   __TEXT.__objc_classname: 0x7a
-  __TEXT.__objc_methtype: 0x537
+  __TEXT.__objc_methtype: 0x53f
   __TEXT.__oslogstring: 0x61
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__unwind_info: 0x140
-  __DATA_CONST.__auth_got: 0x1f8
-  __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x1c8
+  __TEXT.__unwind_info: 0x128
+  __DATA_CONST.__auth_got: 0x218
+  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__const: 0x160
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x988
-  __DATA.__objc_selrefs: 0x380
-  __DATA.__objc_ivar: 0x30
+  __DATA.__objc_const: 0x5a8
+  __DATA.__objc_selrefs: 0x3f0
+  __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/QuickLookSupport.framework/QuickLookSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 66
-  Symbols:   104
-  CStrings:  253
+  Functions: 58
+  Symbols:   102
+  CStrings:  229
 
Symbols:
+ _dispatch_activate
+ _dispatch_after
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
+ "\x14"
+ "@\"NSObject<OS_dispatch_queue>\""
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_afterLoadingQueue"
+ "_afterLoadingQueue"
+ "_close"
+ "afterLoadingQueue"
+ "com.apple.quicklook.thumbnailing.web.afterloading.queue"
+ "load"
+ "setAfterLoadingQueue:"
- "\x15"
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
