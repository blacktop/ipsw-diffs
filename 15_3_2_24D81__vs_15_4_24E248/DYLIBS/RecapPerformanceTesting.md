## RecapPerformanceTesting

> `/System/iOSSupport/System/Library/PrivateFrameworks/RecapPerformanceTesting.framework/Versions/A/RecapPerformanceTesting`

```diff

-49.7.0.0.0
-  __TEXT.__text: 0xd9dc
-  __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_methlist: 0x1660
-  __TEXT.__const: 0x290
-  __TEXT.__gcc_except_tab: 0x234
-  __TEXT.__cstring: 0x6b2
-  __TEXT.__oslogstring: 0x1019
-  __TEXT.__unwind_info: 0x530
-  __TEXT.__objc_classname: 0x528
-  __TEXT.__objc_methname: 0x4309
-  __TEXT.__objc_methtype: 0x124a
-  __TEXT.__objc_stubs: 0x21e0
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x2d0
+50.0.0.0.0
+  __TEXT.__text: 0xdfc4
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__objc_methlist: 0x1f88
+  __TEXT.__const: 0x288
+  __TEXT.__gcc_except_tab: 0x294
+  __TEXT.__cstring: 0x78f
+  __TEXT.__oslogstring: 0x11a5
+  __TEXT.__unwind_info: 0x548
+  __TEXT.__objc_classname: 0x529
+  __TEXT.__objc_methname: 0x4447
+  __TEXT.__objc_methtype: 0x1284
+  __TEXT.__objc_stubs: 0x22a0
+  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__const: 0x328
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xad8
+  __DATA_CONST.__objc_selrefs: 0xec0
   __DATA_CONST.__objc_superrefs: 0xc0
-  __AUTH_CONST.__auth_got: 0x300
+  __AUTH_CONST.__auth_got: 0x310
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x4c0
-  __AUTH_CONST.__objc_const: 0x8560
+  __AUTH_CONST.__cfstring: 0x540
+  __AUTH_CONST.__objc_const: 0x7480
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x910
-  __DATA.__objc_ivar: 0x200
+  __DATA.__objc_ivar: 0x204
   __DATA.__data: 0x668
   __DATA.__bss: 0x89
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
   - /System/Library/PrivateFrameworks/BaseBoard.framework/Versions/A/BaseBoard
+  - /System/Library/PrivateFrameworks/SignpostCollection.framework/Versions/A/SignpostCollection
+  - /System/Library/PrivateFrameworks/SignpostSupport.framework/Versions/A/SignpostSupport
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/iOSSupport/System/Library/Frameworks/UIKit.framework/Versions/A/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C3AEC728-E438-3EA9-906A-4F91C4C7C730
-  Functions: 532
-  Symbols:   1591
-  CStrings:  1007
+  UUID: D0E1E1DD-7C67-318F-93B8-ADD986B4DCCD
+  Functions: 540
+  Symbols:   1616
+  CStrings:  1029
 
Symbols:
+ +[RPTCoordinateSpaceConverter identityConverter].cold.1
+ +[RPTInteractionOptions defaultForPlatform].cold.1
+ +[RPTSettings processEnvironment].cold.1
+ -[RPTScrollViewTestParameters completeAfterScrollEndNotification:]
+ -[RPTScrollViewTestParameters completeAfterScrollEndSignpost:]
+ -[RPTScrollViewTestParameters completeAfterScrollEndSignpost:].cold.1
+ -[RPTScrollViewTestParameters effectiveVersion].cold.1
+ -[RPTScrollViewTestParameters initWithTestName:scrollViewIdentifier:scrollBounds:scrollContentLength:direction:completionHandler:]
+ GCC_except_table19
+ OBJC_IVAR_$_RPTScrollViewTestParameters._scrollViewIdentifier
+ RPTLogTestRunning.cold.1
+ _OBJC_CLASS_$_SignpostSupportObjectExtractor
+ __62-[RPTScrollViewTestParameters completeAfterScrollEndSignpost:]_block_invoke.26
+ ___62-[RPTScrollViewTestParameters completeAfterScrollEndSignpost:]_block_invoke
+ ___66-[RPTScrollViewTestParameters completeAfterScrollEndNotification:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32bs40r_e23_B16?0"SignpostEvent"8lr40l8s32l8
+ _dispatch_async
+ _objc_msgSend$completeAfterScrollEndNotification:
+ _objc_msgSend$completeAfterScrollEndSignpost:
+ _objc_msgSend$processNotificationsWithIntervalTimeoutInSeconds:errorOut:
+ _objc_msgSend$setEndEventProcessingBlock:
+ _objc_msgSend$setFilterPredicateString:
+ _objc_msgSend$stopProcessing
+ _objc_retainAutoreleasedReturnValue
+ makeRCPPlayerPlaybackOptions.cold.1
- ___70-[RPTScrollViewTestParameters waitForPostEventStreamDelayWithHandler:]_block_invoke
CStrings:
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
