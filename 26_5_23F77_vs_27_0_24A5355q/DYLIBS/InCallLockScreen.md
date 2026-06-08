## InCallLockScreen

> `/System/Library/AccessibilityBundles/InCallLockScreen.axbundle/InCallLockScreen`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x434
-  __TEXT.__auth_stubs: 0xe0
+3036.2.0.0.0
+  __TEXT.__text: 0x410
   __TEXT.__objc_methlist: 0x8c
-  __TEXT.__cstring: 0x1b4
   __TEXT.__const: 0x8
+  __TEXT.__cstring: 0x1b4
   __TEXT.__unwind_info: 0x80
-  __TEXT.__objc_classname: 0x74
-  __TEXT.__objc_methname: 0x296
-  __TEXT.__objc_methtype: 0x36
-  __TEXT.__objc_stubs: 0x1a0
-  __DATA_CONST.__got: 0x28
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x78
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x1e0
   __AUTH_CONST.__objc_const: 0x1b0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
-  - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 24F3044E-8C82-3D64-ACF4-6709F2F63CC7
+  UUID: C98D861B-08ED-3E4C-9F27-6708B64B67B5
   Functions: 13
   Symbols:   86
-  CStrings:  68
+  CStrings:  37
 
Symbols:
+ ___block_literal_global.393
+ ___block_literal_global.402
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- ___block_literal_global.330
- ___block_literal_global.339
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x20
Functions:
~ +[AXInCallLockScreenGlue accessibilityInitializeBundle] : 104 -> 100
~ ___55+[AXInCallLockScreenGlue accessibilityInitializeBundle]_block_invoke_2 : 88 -> 84
~ +[PHCallParticipantsViewAccessibility _accessibilityPerformValidations:] : 316 -> 308
~ -[PHCallParticipantsViewAccessibility updateParticipantsAnimated:] : 292 -> 280
~ -[PHCallParticipantsViewAccessibility isAccessibilityElement] : 108 -> 104
~ -[PHCallParticipantsViewAccessibility _accessibilityIsDisplayedInBanner] : 80 -> 76
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXInCallLockScreenGlue"
- "B16@0:8"
- "SafeCategory"
- "__PHCallParticipantsViewAccessibility_super"
- "_accessibilityHitTestShouldFallbackToNearestChild"
- "_accessibilityIsDisplayedInBanner"
- "_accessibilityPerformValidations:"
- "accessibilityInitializeBundle"
- "accessibilityViewIsModal"
- "assistiveTouchScannerSpeechEnabled"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeBoolForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeIntegerForKey:"
- "safeUIViewForKey:"
- "safeValueForKey:"
- "safeValueForKeyPath:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "validateClass:hasInstanceMethod:withFullSignature:"

```
