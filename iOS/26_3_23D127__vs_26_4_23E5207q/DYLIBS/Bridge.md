## Bridge

> `/System/Library/AccessibilityBundles/Bridge.axbundle/Bridge`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x2dfc
-  __TEXT.__auth_stubs: 0x270
+3005.16.0.0.0
+  __TEXT.__text: 0x3034
+  __TEXT.__auth_stubs: 0x240
   __TEXT.__objc_methlist: 0x854
   __TEXT.__cstring: 0xc7e
   __TEXT.__const: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x280
   __DATA_CONST.__objc_superrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x148
+  __AUTH_CONST.__auth_got: 0x130
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x1020
   __AUTH_CONST.__objc_const: 0x1cf0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EDA333A2-AC4A-38FF-82B7-B8E74CF7BDD8
+  UUID: 54C81A1F-892D-34A2-8F2A-05A78622E5AF
   Functions: 145
-  Symbols:   692
+  Symbols:   689
   CStrings:  417
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x21
Functions:
~ ___45+[AXBridgeGlue accessibilityInitializeBundle]_block_invoke : 108 -> 112
~ ___45+[AXBridgeGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ ___45+[AXBridgeGlue accessibilityInitializeBundle]_block_invoke_4 : 512 -> 520
~ +[AXBridgeGlue _handleNanoETSettings] : 88 -> 92
~ ___37+[AXBridgeGlue _handleNanoETSettings]_block_invoke_2 : 104 -> 108
~ ___37+[AXBridgeGlue _handleNanoETSettings]_block_invoke_4 : 96 -> 100
~ +[NSString(AXBridgePriv) _accessibilitySetLastDrawnString:] : 152 -> 160
~ _accessibilityLocalizedStringWithFallback : 280 -> 284
~ +[COSActiveWatchCellAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[COSActiveWatchCellAccessibility accessibilityLabel] : 188 -> 208
~ -[COSActiveWatchCellAccessibility accessibilityIdentifier] : 108 -> 116
~ +[COSFeatureHighlightRowViewAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[COSFeatureHighlightRowViewAccessibility accessibilityLabel] : 188 -> 208
~ -[COSFaceGalleryHeaderViewAccessibility accessibilityElements] : 168 -> 176
~ +[COSGetStartedViewControllerAccessibility _accessibilityPerformValidations:] : 240 -> 252
~ -[COSGetStartedViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 260 -> 280
~ +[COSBuddyNavigationControllerAccessibility _accessibilityPerformValidations:] : 128 -> 136
~ -[COSBuddyNavigationControllerAccessibility _accessibilityLoadAccessibilityInformation] : 108 -> 112
~ +[COSInstallSpinnerButtonAccessibility _accessibilityPerformValidations:] : 188 -> 196
~ -[COSInstallSpinnerButtonAccessibility accessibilityValue] : 248 -> 264
~ -[COSInstallSpinnerButtonAccessibility accessibilityLabel] : 124 -> 132
~ +[COSHeadphoneLevelLimitSliderCellAccessibility _accessibilityPerformValidations:] : 120 -> 128
~ -[COSHeadphoneLevelLimitSliderCellAccessibility accessibilityValue] : 220 -> 236
~ +[COSManualFlowViewAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[COSManualFlowViewAccessibility _accessibilityLoadAccessibilityInformation] : 148 -> 156
~ +[COSPairedDeviceListTableCellAccessibility _accessibilityPerformValidations:] : 240 -> 248
~ -[COSPairedDeviceListTableCellAccessibility accessibilityLabel] : 244 -> 272
~ -[COSPairedDeviceListTableCellAccessibility accessibilityIdentifier] : 108 -> 116
~ -[COSPairedDeviceListTableCellAccessibility accessibilityActivationPoint] : 80 -> 84
~ -[COSPairedDeviceListTableCellAccessibility accessibilityTraits] : 236 -> 244
~ +[COSPasskeyEntryViewControllerAccessibility _accessibilityPerformValidations:] : 192 -> 200
~ -[COSPasskeyEntryViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 184 -> 196
~ -[COSPasskeyEntryViewControllerAccessibility textDidChange:] : 492 -> 524
~ -[COSSecurePairingHeaderAccessibility _axAnnotateHeaderLabel] : 112 -> 120
~ +[COSSetupControllerAccessibility _accessibilityPerformValidations:] : 140 -> 152
~ -[COSSetupControllerAccessibility buddyControllerHold:beforePresentingBuddyController:] : 296 -> 312
~ -[COSSetupControllerAccessibility blockGoingBackFromCurrentController] : 308 -> 332
~ +[COSSetupFinishedViewControllerAccessibility _accessibilityPerformValidations:] : 212 -> 220
~ -[COSSetupFinishedViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 408 -> 420
~ ___89-[COSSetupFinishedViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 392 -> 424
~ +[CheckmarkChoiceViewAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[CheckmarkChoiceViewAccessibility accessibilityTraits] : 236 -> 248
~ +[COSUnlockPlaceholderViewControllerAccessibility _accessibilityPerformValidations:] : 144 -> 152
~ -[COSUnlockPlaceholderViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 128 -> 136
~ +[COSHelloAppleWatchViewControllerAccessibility _accessibilityPerformValidations:] : 120 -> 128
~ -[COSHelloAppleWatchViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 184 -> 196
~ +[COSDiscoverCellAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[COSDiscoverCellAccessibility accessibilityValue] : 156 -> 168
~ -[COSDiscoverCellAccessibility accessibilityHint] : 116 -> 124
~ -[COSDiscoverCellAccessibility _hasArrowUnicodeInSubtitleLabel] : 184 -> 196
~ -[BridgeUIButtonAccessibility setImage:forState:] : 128 -> 132
~ -[COSSecurePairingViewControllerAccessibility tableView:cellForRowAtIndexPath:] : 204 -> 220

```
