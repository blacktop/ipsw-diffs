## WebProcess

> `/System/Library/AccessibilityBundles/WebProcess.axbundle/WebProcess`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x1d88
-  __TEXT.__auth_stubs: 0x2e0
+3005.16.0.0.0
+  __TEXT.__text: 0x1ee8
+  __TEXT.__auth_stubs: 0x290
   __TEXT.__objc_methlist: 0x238
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x477
+  __TEXT.__cstring: 0x4b6
   __TEXT.__oslogstring: 0x48
   __TEXT.__unwind_info: 0x130
   __TEXT.__objc_classname: 0xd1

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x348
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x178
+  __AUTH_CONST.__auth_got: 0x150
   __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0x3e0
   __AUTH_CONST.__objc_const: 0x360

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F7570D4E-BD76-3AB4-8C04-ED1802F2E8EB
+  UUID: E074FC34-8A0C-3842-81C8-2D563B87D006
   Functions: 61
-  Symbols:   332
+  Symbols:   327
   CStrings:  209
 
Symbols:
+ _objc_retain_x21
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
Functions:
~ _accessibilityLocalizedString : 156 -> 164
~ ___49+[AXWebProcessGlue accessibilityInitializeBundle]_block_invoke : 112 -> 116
~ ___49+[AXWebProcessGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 104
~ ___49+[AXWebProcessGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ ___49+[AXWebProcessGlue accessibilityInitializeBundle]_block_invoke_4 : 92 -> 100
~ +[AXWebProcessGlue _initializeAXRuntime] : 276 -> 284
~ ___40+[AXWebProcessGlue _initializeAXRuntime]_block_invoke : 112 -> 120
~ ___40+[AXWebProcessGlue _initializeAXRuntime]_block_invoke_2 : 144 -> 152
~ ___40+[AXWebProcessGlue _initializeAXRuntime]_block_invoke_3 : 140 -> 144
~ ___40+[AXWebProcessGlue _initializeAXRuntime]_block_invoke_4 : 140 -> 144
~ ___40+[AXWebProcessGlue _initializeAXRuntime]_block_invoke_5 : 180 -> 192
~ ___40+[AXWebProcessGlue _initializeAXRuntime]_block_invoke_2.349 : 168 -> 180
~ +[WKAccessibilityWebPageObjectAccessibility _accessibilityPerformValidations:] : 356 -> 364
~ -[WKAccessibilityWebPageObjectAccessibility dealloc] : 152 -> 160
~ -[WKAccessibilityWebPageObjectAccessibility _accessibilityHostPid] : 88 -> 92
~ -[WKAccessibilityWebPageObjectAccessibility _accessibilityApplication] : 108 -> 112
~ -[WKAccessibilityWebPageObjectAccessibility accessibilityHitTest:] : 116 -> 120
~ -[WKAccessibilityWebPageObjectAccessibility _enableCaching] : 128 -> 136
~ -[WKAccessibilityWebPageObjectAccessibility _disableCaching] : 128 -> 136
~ -[WKAccessibilityWebPageObjectAccessibility _accessibilityResponderElement] : 104 -> 112
~ -[WKAccessibilityWebPageObjectAccessibility _accessibilityTextViewTextOperationResponder] : 164 -> 172
~ -[WKAccessibilityWebPageObjectAccessibility _axCachedRootObject] : 64 -> 68
~ -[WKAccessibilityWebPageObjectAccessibility _axSetCachedRootObject:] : 100 -> 104
~ -[WKAccessibilityWebPageObjectAccessibility _initializeRootIfNecessary] : 172 -> 180
~ -[WKAccessibilityWebPageObjectAccessibility accessibilityElements] : 180 -> 188
~ -[WKAccessibilityWebPageObjectAccessibility accessibilityRemoteSubstituteChildren:] : 116 -> 120
~ -[WKAccessibilityWebPageObjectAccessibility _axRemoteElementRegistered:] : 468 -> 508
~ -[WKAccessibilityWebPageObjectAccessibility _axListenForRemoteElement] : 108 -> 112
~ -[WKAccessibilityWebPageObjectAccessibility _accessibilityLoadAccessibilityInformation] : 268 -> 284
~ -[WKAccessibilityWebPageObjectAccessibility setRemoteTokenData:] : 132 -> 136
~ -[WKAccessibilityWebPageObjectAccessibility accessibilityFrame] : 108 -> 112
~ -[WKAccessibilityWebPageObjectAccessibility _axUnarchivedTokenForData:] : 276 -> 284
~ -[WKNSObjectAccessibility accessibilityHitTest:] : 408 -> 416
~ -[WKNSObjectAccessibility _accessibilityFirstElementForFocusForRemoteElement] : 136 -> 148
~ -[WKNSObjectAccessibility _iosAccessibilityAttributeValue:forParameter:] : 184 -> 192
~ -[WKNSObjectAccessibility _iosAccessibilityAttributeValue:] : 316 -> 344
~ -[WKNSObjectAccessibility _iosAccessibilityPerformAction:withValue:fencePort:] : 536 -> 572
~ -[WKNSObjectAccessibility _accessibilityMoveFocusWithHeading:toElementMatchingQuery:] : 100 -> 104
~ -[WKNSObjectAccessibility _accessibilityMoveFocusWithHeading:byGroup:] : 72 -> 76
~ ___40+[AXWebProcessGlue _initializeAXRuntime]_block_invoke_5.cold.1 : 176 -> 180
CStrings:
+ "/Library/Caches/com.apple.xbs/FDBC4160-ED96-4D0B-B2D6-F3AE9446FEDF/TemporaryDirectory.FqHR68/Sources/AccessibilityBundles_Alias5/WebKitAccessibility/Accessibility/WKAccessibilityWebPageObjectAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias5/WebKitAccessibility/Accessibility/WKAccessibilityWebPageObjectAccessibility.m"

```
