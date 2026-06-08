## Bridge

> `/System/Library/AccessibilityBundles/Bridge.axbundle/Bridge`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x3034
-  __TEXT.__auth_stubs: 0x240
+3036.2.0.0.0
+  __TEXT.__text: 0x2e40
   __TEXT.__objc_methlist: 0x854
-  __TEXT.__cstring: 0xc7e
   __TEXT.__const: 0x8
-  __TEXT.__gcc_except_tab: 0x28
+  __TEXT.__gcc_except_tab: 0x30
+  __TEXT.__cstring: 0xc7e
   __TEXT.__unwind_info: 0x1c8
-  __TEXT.__objc_classname: 0x888
-  __TEXT.__objc_methname: 0x77d
-  __TEXT.__objc_methtype: 0xc7
-  __TEXT.__objc_stubs: 0x700
-  __DATA_CONST.__got: 0xd0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x280
   __DATA_CONST.__objc_superrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x130
+  __DATA_CONST.__got: 0xd0
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x1020
   __AUTH_CONST.__objc_const: 0x1cf0
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xff0
   __DATA.__bss: 0x9
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 73A0DDA5-6D12-398B-9E71-982AEAA551E2
-  Functions: 145
-  Symbols:   689
-  CStrings:  417
+  UUID: A4996E7F-F819-3000-84F2-86180ECA5BEC
+  Functions: 146
+  Symbols:   693
+  CStrings:  272
 
Symbols:
+ GCC_except_table100
+ ___block_literal_global.351
+ ___block_literal_global.357
+ ___block_literal_global.430
+ ___block_literal_global.432
+ ___block_literal_global.434
+ ___block_literal_global.436
+ ___block_literal_global.442
+ ___block_literal_global.444
+ _localizedString
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- GCC_except_table3
- ___block_literal_global.330
- ___block_literal_global.336
- ___block_literal_global.409
- ___block_literal_global.411
- ___block_literal_global.413
- ___block_literal_global.415
- ___block_literal_global.421
- ___block_literal_global.423
- _objc_retain_x19
Functions:
~ -[COSSOSTriggerAnimationCellAccessibility accessibilityLabel] : 12 -> 16
~ ___45+[AXBridgeGlue accessibilityInitializeBundle]_block_invoke : 112 -> 108
~ ___45+[AXBridgeGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 96
~ ___45+[AXBridgeGlue accessibilityInitializeBundle]_block_invoke_4 : 520 -> 512
~ +[AXBridgeGlue _handleNanoETSettings] : 92 -> 88
~ ___37+[AXBridgeGlue _handleNanoETSettings]_block_invoke_2 : 108 -> 104
~ ___37+[AXBridgeGlue _handleNanoETSettings]_block_invoke_4 : 100 -> 96
~ +[NSString(AXBridgePriv) _accessibilitySetLastDrawnString:] : 160 -> 152
~ _accessibilityLocalizedStringWithFallback : 284 -> 4
+ _localizedString
~ +[COSActiveWatchCellAccessibility _accessibilityPerformValidations:] : 132 -> 124
~ -[COSActiveWatchCellAccessibility accessibilityLabel] : 208 -> 188
~ -[COSActiveWatchCellAccessibility accessibilityIdentifier] : 116 -> 108
~ +[COSFeatureHighlightRowViewAccessibility _accessibilityPerformValidations:] : 140 -> 128
~ -[COSFeatureHighlightRowViewAccessibility accessibilityLabel] : 208 -> 188
~ -[COSFaceGalleryHeaderViewAccessibility accessibilityElements] : 176 -> 168
~ +[COSGetStartedViewControllerAccessibility _accessibilityPerformValidations:] : 252 -> 240
~ -[COSGetStartedViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 280 -> 268
~ +[COSBuddyNavigationControllerAccessibility _accessibilityPerformValidations:] : 136 -> 128
~ -[COSBuddyNavigationControllerAccessibility _accessibilityLoadAccessibilityInformation] : 112 -> 108
~ +[COSInstallSpinnerButtonAccessibility _accessibilityPerformValidations:] : 196 -> 188
~ -[COSInstallSpinnerButtonAccessibility accessibilityValue] : 264 -> 244
~ +[COSHeadphoneLevelLimitSliderCellAccessibility _accessibilityPerformValidations:] : 128 -> 120
~ -[COSHeadphoneLevelLimitSliderCellAccessibility accessibilityValue] : 236 -> 228
~ -[COSHeadphoneLevelLimitSliderCellAccessibility accessibilityLabel] : 12 -> 16
~ +[COSManualFlowViewAccessibility _accessibilityPerformValidations:] : 132 -> 124
~ -[COSManualFlowViewAccessibility _accessibilityLoadAccessibilityInformation] : 156 -> 148
~ +[COSPairedDeviceListTableCellAccessibility _accessibilityPerformValidations:] : 248 -> 240
~ -[COSPairedDeviceListTableCellAccessibility accessibilityLabel] : 272 -> 244
~ -[COSPairedDeviceListTableCellAccessibility accessibilityIdentifier] : 116 -> 108
~ -[COSPairedDeviceListTableCellAccessibility accessibilityActivationPoint] : 84 -> 80
~ -[COSPairedDeviceListTableCellAccessibility accessibilityTraits] : 244 -> 236
~ -[COSPasscodeAdvancedViewControllerAccessibility _accessibilityLabelForWatchView] : 12 -> 16
~ -[COSPasscodeChoiceViewControllerAccessibility _accessibilityLabelForWatchView] : 12 -> 16
~ +[COSPasskeyEntryViewControllerAccessibility _accessibilityPerformValidations:] : 200 -> 192
~ -[COSPasskeyEntryViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 196 -> 192
~ -[COSPasskeyEntryViewControllerAccessibility textDidChange:] : 524 -> 500
~ -[COSSecurePairingHeaderAccessibility initWithFrame:] : 84 -> 80
~ +[COSSetupControllerAccessibility _accessibilityPerformValidations:] : 152 -> 140
~ -[COSSetupControllerAccessibility buddyControllerHold:beforePresentingBuddyController:] : 312 -> 296
~ -[COSSetupControllerAccessibility blockGoingBackFromCurrentController] : 332 -> 308
~ +[COSSetupFinishedViewControllerAccessibility _accessibilityPerformValidations:] : 220 -> 212
~ -[COSSetupFinishedViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 420 -> 412
~ ___89-[COSSetupFinishedViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 424 -> 392
~ -[COSUnifiedOptinFYIViewControllerAccessibility _accessibilityLabelForWatchView] : 12 -> 16
~ +[CheckmarkChoiceViewAccessibility _accessibilityPerformValidations:] : 132 -> 124
~ -[CheckmarkChoiceViewAccessibility accessibilityTraits] : 248 -> 236
~ +[COSUnlockPlaceholderViewControllerAccessibility _accessibilityPerformValidations:] : 152 -> 144
~ +[COSHelloAppleWatchViewControllerAccessibility _accessibilityPerformValidations:] : 128 -> 120
~ -[COSHelloAppleWatchViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 196 -> 192
~ +[COSDiscoverCellAccessibility _accessibilityPerformValidations:] : 132 -> 124
~ -[COSDiscoverCellAccessibility accessibilityValue] : 168 -> 156
~ -[COSDiscoverCellAccessibility _hasArrowUnicodeInSubtitleLabel] : 196 -> 184
~ -[BridgeUIButtonAccessibility setImage:forState:] : 132 -> 128
~ -[COSSecurePairingViewControllerAccessibility tableView:cellForRowAtIndexPath:] : 220 -> 204
CStrings:
- "#16@0:8"
- "@16@0:8"
- "@32@0:8@16@24"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "AXBridgeGlue"
- "AXBridgePriv"
- "B16@0:8"
- "COSActiveWatchCellAccessibility"
- "ETSettingsControllerAccessibility"
- "Q16@0:8"
- "SafeCategory"
- "__BridgeNSStringAccessibility_super"
- "__BridgeUIButtonAccessibility_super"
- "__COSActiveWatchCellAccessibility_super"
- "__COSBuddyNavigationControllerAccessibility_super"
- "__COSDiscoverCellAccessibility_super"
- "__COSFaceGalleryHeaderViewAccessibility_super"
- "__COSFeatureHighlightRowViewAccessibility_super"
- "__COSGetStartedViewControllerAccessibility_super"
- "__COSHeadphoneLevelLimitSliderCellAccessibility_super"
- "__COSHelloAppleWatchViewControllerAccessibility_super"
- "__COSInstallSpinnerButtonAccessibility_super"
- "__COSManualFlowViewAccessibility_super"
- "__COSPairedDeviceListTableCellAccessibility_super"
- "__COSPasscodeAdvancedViewControllerAccessibility_super"
- "__COSPasscodeChoiceViewControllerAccessibility_super"
- "__COSPasskeyEntryViewControllerAccessibility_super"
- "__COSSOSTriggerAnimationCellAccessibility_super"
- "__COSSecurePairingHeaderAccessibility_super"
- "__COSSecurePairingViewControllerAccessibility_super"
- "__COSSetupControllerAccessibility_super"
- "__COSSetupFinishedViewControllerAccessibility_super"
- "__COSUnifiedOptinFYIViewControllerAccessibility_super"
- "__COSUnlockPlaceholderViewControllerAccessibility_super"
- "__CheckmarkChoiceViewAccessibility_super"
- "__ETSettingsControllerAccessibility_super"
- "_accessibilityBoolValueForKey:"
- "_accessibilityLabelForWatchView"
- "_accessibilityLastDrawnString"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_accessibilitySetLastDrawnString:"
- "_accessibilitySetUserDefinedMediaAnalysisOptions:"
- "_accessibilityStringForLabelKeyValues:"
- "_axAnnotateHeaderLabel"
- "_handleNanoETSettings"
- "_hasArrowUnicodeInSubtitleLabel"
- "_setAccessibilityValueBlock:"
- "accessibilityActivationPoint"
- "accessibilityBundles"
- "accessibilityElements"
- "accessibilityHint"
- "accessibilityIdentifier"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityTraits"
- "accessibilityValue"
- "addHandler:forBundleName:"
- "addObject:"
- "arrayWithObjects:count:"
- "buddyControllerHold:beforePresentingBuddyController:"
- "bundleForClass:"
- "characterAtIndex:"
- "componentsJoinedByString:"
- "count"
- "doubleValue"
- "drawInRect:withAttributes:"
- "image"
- "initWithFrame:"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "isHidden"
- "lastObject"
- "leftBarButtonItem"
- "length"
- "localizedStringForKey:value:table:"
- "navigationBar"
- "navigationItem"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "rightBarButtonItem"
- "safeBoolForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeUIViewForKey:"
- "safeValueForKey:"
- "setAccessibilityIdentifier:"
- "setAccessibilityLabel:"
- "setAccessibilityTraits:"
- "setAttribute:forKey:"
- "setDebugBuild:"
- "setImage:forState:"
- "setIsAccessibilityElement:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "stringByReplacingCharactersInRange:withString:"
- "stringWithFormat:"
- "stringWithString:"
- "substringWithRange:"
- "tableView:cellForRowAtIndexPath:"
- "text"
- "textLabel"
- "topItem"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@16@24"
- "v32@0:8@16Q24"
- "v56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48"
- "validateClass:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:isKindOfClass:"
- "viewControllers"
- "{CGPoint=dd}16@0:8"

```
