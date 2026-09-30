## RecapPerformanceTesting

> `/System/Library/PrivateFrameworks/RecapPerformanceTesting.framework/RecapPerformanceTesting`

```diff

-49.7.0.0.0
-  __TEXT.__text: 0xda64
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x1660
-  __TEXT.__const: 0x280
-  __TEXT.__gcc_except_tab: 0x234
-  __TEXT.__cstring: 0x67e
-  __TEXT.__oslogstring: 0x1019
-  __TEXT.__unwind_info: 0x560
-  __TEXT.__objc_classname: 0x528
-  __TEXT.__objc_methname: 0x4304
-  __TEXT.__objc_methtype: 0x124a
-  __TEXT.__objc_stubs: 0x2200
-  __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x2d0
+50.0.0.0.0
+  __TEXT.__text: 0xe03c
+  __TEXT.__auth_stubs: 0x5d0
+  __TEXT.__objc_methlist: 0x1f88
+  __TEXT.__const: 0x298
+  __TEXT.__gcc_except_tab: 0x294
+  __TEXT.__cstring: 0x75b
+  __TEXT.__oslogstring: 0x11a5
+  __TEXT.__unwind_info: 0x588
+  __TEXT.__objc_classname: 0x529
+  __TEXT.__objc_methname: 0x4442
+  __TEXT.__objc_methtype: 0x1284
+  __TEXT.__objc_stubs: 0x22c0
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__const: 0x328
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xad8
+  __DATA_CONST.__objc_selrefs: 0xec0
   __DATA_CONST.__objc_superrefs: 0xc0
-  __AUTH_CONST.__auth_got: 0x2f0
+  __AUTH_CONST.__auth_got: 0x300
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x460
-  __AUTH_CONST.__objc_const: 0x8560
+  __AUTH_CONST.__cfstring: 0x4e0
+  __AUTH_CONST.__objc_const: 0x7480
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_ivar: 0x200
+  __DATA.__objc_ivar: 0x204
   __DATA.__data: 0x668
   __DATA.__bss: 0x89
   __DATA_DIRTY.__objc_data: 0x910

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
+  - /System/Library/PrivateFrameworks/SignpostCollection.framework/SignpostCollection
+  - /System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 532
-  Symbols:   702
-  CStrings:  981
+  Functions: 540
+  Symbols:   717
+  CStrings:  1000
 
Symbols:
+ _OBJC_CLASS_$_SignpostSupportObjectExtractor
+ _dispatch_async
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "\x11\x1211"
+ "/System/AppleInternal/Library/Frameworks/Recap.framework/Recap"
+ "@88@0:8@16@24{CGRect={CGPoint=dd}{CGSize=dd}}32d64q72@?80"
+ "B16@?0@\"SignpostEvent\"8"
+ "Overriding default amplitude %.1f pts with %.1f pts. This may have undefined behavior and should be avoided, when target scroll view is known."
+ "Overriding default amplitude %@ pts with %@ pts. This may have undefined behavior and should be avoided, when target scroll view is known."
+ "RPT: RPTScrollViewTestParameters failed to set up signpost monitoring with predicate: %@ - Because of: %@"
+ "RPT: RPTScrollViewTestParameters signpost received"
+ "RPT: RPTScrollViewTestParameters started monitoring for signpost with predicate: %@"
+ "RPT: RPTScrollViewTestParameters: waitForPostEventStreamDelayWithHandler: effectiveVersion=%lu, has_scrollView=%i, _scrollViewIdentifier=%@, _shouldFlick=%i"
+ "ScrollView"
+ "Scroll_Deceleration"
+ "_scrollViewIdentifier"
+ "com.apple.UIKit"
+ "completeAfterScrollEndNotification:"
+ "completeAfterScrollEndSignpost:"
+ "initWithTestName:scrollViewIdentifier:scrollBounds:scrollContentLength:direction:completionHandler:"
+ "processNotificationsWithIntervalTimeoutInSeconds:errorOut:"
+ "setEndEventProcessingBlock:"
+ "setFilterPredicateString:"
+ "stopProcessing"
+ "subsystem=='%@' AND category=='%@' AND signpostName=='%@' AND message CONTAINS 'id=%@'"
- "\"11"
- "Overriding default amplitude %.1f pts with %.1f pts. This may have undefined behaviour and should be avoided, when target scroll view is known."
- "Overriding default amplitude %@ pts with %@ pts. This may have undefined behaviour and should be avoided, when target scroll view is known."

```
