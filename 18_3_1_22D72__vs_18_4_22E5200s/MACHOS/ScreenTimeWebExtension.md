## ScreenTimeWebExtension

> `/System/Library/Frameworks/ScreenTime.framework/PlugIns/ScreenTimeWebExtension.appex/ScreenTimeWebExtension`

```diff

-537.3.3.0.0
-  __TEXT.__text: 0x104c
-  __TEXT.__auth_stubs: 0x260
-  __TEXT.__objc_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0xe8
-  __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__objc_methname: 0x7cf
-  __TEXT.__cstring: 0x6e
+537.4.14.0.0
+  __TEXT.__text: 0x12f8
+  __TEXT.__auth_stubs: 0x280
+  __TEXT.__objc_stubs: 0x6a0
+  __TEXT.__objc_methlist: 0x238
+  __TEXT.__const: 0x68
+  __TEXT.__gcc_except_tab: 0x3c
+  __TEXT.__objc_methname: 0x928
+  __TEXT.__cstring: 0xdf
   __TEXT.__oslogstring: 0x6b
   __TEXT.__objc_classname: 0x33
-  __TEXT.__objc_methtype: 0x1d7
-  __TEXT.__unwind_info: 0xd0
-  __DATA_CONST.__auth_got: 0x140
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x198
-  __DATA_CONST.__cfstring: 0x60
+  __TEXT.__objc_methtype: 0x200
+  __TEXT.__unwind_info: 0xe8
+  __DATA_CONST.__auth_got: 0x150
+  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__const: 0x1c0
+  __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x4d0
-  __DATA.__objc_selrefs: 0x1a0
-  __DATA.__objc_ivar: 0xc
+  __DATA.__objc_const: 0x2d8
+  __DATA.__objc_selrefs: 0x280
+  __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/UsageTracking.framework/UsageTracking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 29
-  Symbols:   60
-  CStrings:  124
+  Functions: 34
+  Symbols:   65
+  CStrings:  139
 
Symbols:
+ _OBJC_CLASS_$_NSAssertionHandler
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$_NSTimer
+ _arc4random_uniform
+ _objc_retain_x22
CStrings:
+ "\x04"
+ "-_reportURLIsBlocked:withDelay: must be called on the main thread"
+ "@\"NSTimer\""
+ "STWebServiceViewController.m"
+ "T@\"NSTimer\",&,V_reportURLIsBlockedTimer"
+ "_reportURLIsBlocked:withDelay:"
+ "_reportURLIsBlockedTimer"
+ "_startRecordingUsageForURL:bundleIdentifier:profileIdentifier:usageState:replyHandler:"
+ "currentHandler"
+ "handleFailureInMethod:object:file:lineNumber:description:"
+ "initWithURL:bundleIdentifier:profileIdentifier:auditToken:"
+ "invalidate"
+ "isMainThread"
+ "reportURLIsBlockedTimer"
+ "scheduledTimerWithTimeInterval:repeats:block:"
+ "setReportURLIsBlockedTimer:"
+ "setURL:bundleIdentifier:profileIdentifier:usageState:replyHandler:"
+ "v16@?0@\"NSTimer\"8"
+ "v28@0:8B16d20"
+ "v56@0:8@\"NSURL\"16@\"NSString\"24@\"NSString\"32q40@?<v@?@\"NSError\">48"
+ "v56@0:8@16@24@32q40@?48"
- "\x03"
- "_startRecordingUsageForURL:bundleIdentifier:usageState:replyHandler:"
- "initWithURL:bundleIdentifier:auditToken:"
- "setURL:bundleIdentifier:usageState:replyHandler:"
- "v48@0:8@\"NSURL\"16@\"NSString\"24q32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24q32@?40"

```
