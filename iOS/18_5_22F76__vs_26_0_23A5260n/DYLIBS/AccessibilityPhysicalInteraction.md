## AccessibilityPhysicalInteraction

> `/System/Library/PrivateFrameworks/AccessibilityPhysicalInteraction.framework/AccessibilityPhysicalInteraction`

```diff

-3148.15.26.0.0
-  __TEXT.__text: 0x10c2c
-  __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_methlist: 0x188c
+3180.6.1.0.0
+  __TEXT.__text: 0x112ec
+  __TEXT.__auth_stubs: 0xb60
+  __TEXT.__objc_methlist: 0x1924
   __TEXT.__const: 0x2b2
   __TEXT.__gcc_except_tab: 0x190
-  __TEXT.__cstring: 0x651
-  __TEXT.__oslogstring: 0x3f1
+  __TEXT.__cstring: 0x6a8
+  __TEXT.__oslogstring: 0x455
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x610
+  __TEXT.__unwind_info: 0x638
   __TEXT.__objc_classname: 0x261
-  __TEXT.__objc_methname: 0x40dd
+  __TEXT.__objc_methname: 0x430d
   __TEXT.__objc_methtype: 0xaf3
-  __TEXT.__objc_stubs: 0x3fa0
-  __DATA_CONST.__got: 0x4c8
-  __DATA_CONST.__const: 0x620
+  __TEXT.__objc_stubs: 0x4120
+  __DATA_CONST.__got: 0x4d8
+  __DATA_CONST.__const: 0x628
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1360
+  __DATA_CONST.__objc_selrefs: 0x1400
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x5b8
+  __AUTH_CONST.__auth_got: 0x5c0
   __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x5c0
-  __AUTH_CONST.__objc_const: 0x1cf8
+  __AUTH_CONST.__cfstring: 0x6a0
+  __AUTH_CONST.__objc_const: 0x1d78
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0x148
+  __DATA.__objc_ivar: 0x154
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SpeakThisServices.framework/SpeakThisServices
   - /System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/ZoomServices.framework/ZoomServices
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libCTGreenTeaLogger.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 36C1D674-4F68-3735-A6AA-0D54EF2B8E96
-  Functions: 557
-  Symbols:   2326
-  CStrings:  1044
+  UUID: 0EDCE64B-E5E0-3EA4-BBCC-7ABBDEA62BA6
+  Functions: 573
+  Symbols:   2369
+  CStrings:  1086
 
Symbols:
+ -[AXPIFingerController cancelGestureWithCompletion:]
+ -[AXPIFingerController continueWithGesture:]
+ -[AXPIFingerController endGestureWithCompletion:]
+ -[AXPIFingerController eventSenderServiceID]
+ -[AXPIFingerController isPerformingMultiStepGesture]
+ -[AXPIFingerController setEventSenderServiceID:]
+ -[AXPIFingerController startGesture:]
+ -[AXPIFingerEventSender performCancelWithTouches:]
+ -[AXPIFingerEventSender performCancelWithTouchesByFingerIdentifier:]
+ -[AXPISystemActionHelper _sendShakeEvent:]
+ -[AXPISystemActionHelper activateMagnifierAskQuestion]
+ -[AXPISystemActionHelper launchAccessibilityReader]
+ -[AXPISystemActionHelper launchMagnifierWithURL:]
+ GCC_except_table108
+ GCC_except_table24
+ _AXAssistiveTouchIconTypeAccessibilityReader
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_IVAR_$_AXPIFingerController._eventSenderServiceID
+ _OBJC_IVAR_$_AXPIFingerController._isGestureSuccessful
+ _OBJC_IVAR_$_AXPIFingerController._isPerformingMultiStepGesture
+ __AXSClarityBoardEnabled
+ ___31-[AXPISystemActionHelper shake]_block_invoke_2
+ ___42-[AXPISystemActionHelper _sendShakeEvent:]_block_invoke
+ ___49-[AXPISystemActionHelper launchMagnifierWithURL:]_block_invoke
+ ___51-[AXPISystemActionHelper launchAccessibilityReader]_block_invoke
+ ___68-[AXPISystemActionHelper performSysdiagnoseWithStatusUpdateHandler:]_block_invoke.390
+ ___68-[AXPISystemActionHelper performSysdiagnoseWithStatusUpdateHandler:]_block_invoke.397
+ ___68-[AXPISystemActionHelper performSysdiagnoseWithStatusUpdateHandler:]_block_invoke.402
+ ___68-[AXPISystemActionHelper performSysdiagnoseWithStatusUpdateHandler:]_block_invoke.417
+ ___68-[AXPISystemActionHelper performSysdiagnoseWithStatusUpdateHandler:]_block_invoke.417.cold.1
+ ___68-[AXPISystemActionHelper performSysdiagnoseWithStatusUpdateHandler:]_block_invoke.417.cold.2
+ ___68-[AXPISystemActionHelper performSysdiagnoseWithStatusUpdateHandler:]_block_invoke.418
+ ___68-[AXPISystemActionHelper performSysdiagnoseWithStatusUpdateHandler:]_block_invoke_2.398
+ ___68-[AXPISystemActionHelper performSysdiagnoseWithStatusUpdateHandler:]_block_invoke_2.406
+ ___block_descriptor_45_e8_32s_e5_v8?0ls32l8
+ ___block_literal_global.282
+ ___block_literal_global.283
+ ___block_literal_global.370
+ ___block_literal_global.377
+ ___block_literal_global.388
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftMLCompute_$_AccessibilityPhysicalInteraction
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_AccessibilityPhysicalInteraction
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_AccessibilityPhysicalInteraction
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_AccessibilityPhysicalInteraction
+ _objc_msgSend$URL
+ _objc_msgSend$_sendShakeEvent:
+ _objc_msgSend$assistiveTouchHeadTrackingEnabled
+ _objc_msgSend$eventService
+ _objc_msgSend$focusedApps
+ _objc_msgSend$launchAccessibilityReader
+ _objc_msgSend$launchMagnifierWithURL:
+ _objc_msgSend$performCancelWithTouchesByFingerIdentifier:
+ _objc_msgSend$serviceID
+ _objc_msgSend$setHost:
+ _objc_msgSend$setQuery:
+ _objc_msgSend$setScheme:
- GCC_except_table103
- GCC_except_table22
- ___47-[AXPISystemActionHelper activateDetectionMode]_block_invoke
- ___68-[AXPISystemActionHelper performSysdiagnoseWithStatusUpdateHandler:]_block_invoke.377
- ___68-[AXPISystemActionHelper performSysdiagnoseWithStatusUpdateHandler:]_block_invoke.384
- ___68-[AXPISystemActionHelper performSysdiagnoseWithStatusUpdateHandler:]_block_invoke.389
- ___68-[AXPISystemActionHelper performSysdiagnoseWithStatusUpdateHandler:]_block_invoke.404
- ___68-[AXPISystemActionHelper performSysdiagnoseWithStatusUpdateHandler:]_block_invoke.404.cold.1
- ___68-[AXPISystemActionHelper performSysdiagnoseWithStatusUpdateHandler:]_block_invoke.404.cold.2
- ___68-[AXPISystemActionHelper performSysdiagnoseWithStatusUpdateHandler:]_block_invoke.405
- ___68-[AXPISystemActionHelper performSysdiagnoseWithStatusUpdateHandler:]_block_invoke_2.385
- ___68-[AXPISystemActionHelper performSysdiagnoseWithStatusUpdateHandler:]_block_invoke_2.393
- ___block_literal_global.279
- ___block_literal_global.280
- ___block_literal_global.357
- ___block_literal_global.364
- ___block_literal_global.375
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swiftDataDetection_$_AccessibilityPhysicalInteraction
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_AccessibilityPhysicalInteraction
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_AccessibilityPhysicalInteraction
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_AccessibilityPhysicalInteraction
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_AccessibilityPhysicalInteraction
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_AccessibilityPhysicalInteraction
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_AccessibilityPhysicalInteraction
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_AccessibilityPhysicalInteraction
CStrings:
+ "After opening URL : apple-axreader://"
+ "Before opening URL : apple-axreader://"
+ "Parameterized URL : %@"
+ "TB,R,N,V_isPerformingMultiStepGesture"
+ "TQ,N,V_eventSenderServiceID"
+ "URL"
+ "_eventSenderServiceID"
+ "_isGestureSuccessful"
+ "_isPerformingMultiStepGesture"
+ "_sendShakeEvent:"
+ "activateMagnifierAskQuestion"
+ "apple-axreader"
+ "apple-axreader://"
+ "apple-magnifier://askQuestion"
+ "assistiveTouchHeadTrackingEnabled"
+ "back"
+ "bundleID=%@"
+ "camera://configuration?capturemode=photo&capturedevice=%@"
+ "cancelGestureWithCompletion:"
+ "continueWithGesture:"
+ "endGestureWithCompletion:"
+ "eventSenderServiceID"
+ "focusedApps"
+ "front"
+ "isPerformingMultiStepGesture"
+ "launchAccessibilityReader"
+ "launchMagnifierWithURL:"
+ "new"
+ "performCancelWithTouches:"
+ "performCancelWithTouchesByFingerIdentifier:"
+ "serviceID"
+ "setEventSenderServiceID:"
+ "setHost:"
+ "setQuery:"
+ "setScheme:"
+ "startGesture:"
+ "\xb1"
- "camera://configuration?capturemode=photo&capturedevice=front"
- "\xa1"

```
