## AppleMobileFileIntegrity

> `/System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity`

```diff

-938.80.6.0.0
-  __TEXT.__text: 0xac38
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x228
+938.100.82.0.0
+  __TEXT.__text: 0xb1ac
+  __TEXT.__auth_stubs: 0x7e0
+  __TEXT.__objc_methlist: 0x2ec
   __TEXT.__const: 0x1b8
-  __TEXT.__cstring: 0x1386
-  __TEXT.__oslogstring: 0xb95
+  __TEXT.__cstring: 0x1426
+  __TEXT.__oslogstring: 0xbc7
   __TEXT.__gcc_except_tab: 0x294
-  __TEXT.__unwind_info: 0x320
-  __TEXT.__objc_classname: 0x63
-  __TEXT.__objc_methname: 0x83b
-  __TEXT.__objc_methtype: 0x320
-  __TEXT.__objc_stubs: 0x980
-  __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0x7a8
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__unwind_info: 0x328
+  __TEXT.__objc_classname: 0x75
+  __TEXT.__objc_methname: 0x8e8
+  __TEXT.__objc_methtype: 0x33d
+  __TEXT.__objc_stubs: 0x9c0
+  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__const: 0x7f8
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b8
+  __DATA_CONST.__objc_selrefs: 0x2d8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x3b8
-  __AUTH_CONST.__const: 0x230
-  __AUTH_CONST.__cfstring: 0x500
-  __AUTH_CONST.__objc_const: 0x6d8
+  __AUTH_CONST.__auth_got: 0x400
+  __AUTH_CONST.__const: 0x250
+  __AUTH_CONST.__cfstring: 0x600
+  __AUTH_CONST.__objc_const: 0x628
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x3c
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x190
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 245
-  Symbols:   483
-  CStrings:  405
+  Functions: 248
+  Symbols:   499
+  CStrings:  421
 
Symbols:
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_ValidationMetrics
+ _OBJC_METACLASS_$_ValidationMetrics
+ _dispatch_async
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_queue_create
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _objc_retain_x25
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "Dropping validation metrics because queue is full"
+ "ValidationMetrics"
+ "amfid.validation.metrics"
+ "bundle_identifier"
+ "com.apple.sha1.code_directory.usage"
+ "dictionaryWithObjects:forKeys:count:"
+ "dispatchMetrics:"
+ "filename"
+ "is_apple"
+ "null"
+ "sendSHA1CodeDirectoryMetricWithFilename:withSigningID:withCDHash:withTeamID:withBundleID:withVersion:withIsApple:"
+ "signing_identifier"
+ "team_identifier"
+ "v68@0:8@16@24@32@40@48@56B64"
+ "version"

```
