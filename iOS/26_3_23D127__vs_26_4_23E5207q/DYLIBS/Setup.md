## Setup

> `/System/Library/AccessibilityBundles/Setup.axbundle/Setup`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x5510
-  __TEXT.__auth_stubs: 0x360
+3005.16.0.0.0
+  __TEXT.__text: 0x58dc
+  __TEXT.__auth_stubs: 0x310
   __TEXT.__objc_methlist: 0x9e4
   __TEXT.__cstring: 0x10b1
   __TEXT.__const: 0x30

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x490
   __DATA_CONST.__objc_superrefs: 0xc0
-  __AUTH_CONST.__auth_got: 0x1c0
+  __AUTH_CONST.__auth_got: 0x198
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__cfstring: 0x1560
   __AUTH_CONST.__objc_const: 0x2130

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 116C3FFF-E3A1-320D-82F2-340620CE9D03
+  UUID: CA27234C-B0E1-3587-9BBF-5B6EAAC5371E
   Functions: 185
-  Symbols:   896
+  Symbols:   891
   CStrings:  592
 
Symbols:
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x5
- _objc_retain_x8
Functions:
~ _accessibilityLocalizedString : 156 -> 164
~ _AXAttributedStringForLanguage : 232 -> 240
~ +[AXSetupGlue accessibilityInitializeBundle] : 360 -> 384
~ ___44+[AXSetupGlue accessibilityInitializeBundle]_block_invoke : 460 -> 464
~ ___44+[AXSetupGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ ___44+[AXSetupGlue accessibilityInitializeBundle]_block_invoke_4 : 612 -> 620
~ ___44+[AXSetupGlue accessibilityInitializeBundle]_block_invoke_6 : 136 -> 144
~ ___44+[AXSetupGlue accessibilityInitializeBundle]_block_invoke_8 : 136 -> 144
~ ___44+[AXSetupGlue accessibilityInitializeBundle]_block_invoke_10 : 136 -> 144
~ ___44+[AXSetupGlue accessibilityInitializeBundle]_block_invoke_12 : 136 -> 144
~ ___44+[AXSetupGlue accessibilityInitializeBundle]_block_invoke_14 : 136 -> 144
~ +[BYBuddySafetyAndHandlingViewControllerProviderAccessibility _accessibilityPerformValidations:] : 152 -> 160
~ -[BYBuddySafetyAndHandlingViewControllerProviderAccessibility makeViewController] : 216 -> 236
~ -[BuddyPosedDeviceSelectionItemViewAccessibility accessibilityActivationPoint] : 80 -> 84
~ +[BuddyAccessibilityUtilitiesAccessibility _accessibilityPerformValidations:] : 144 -> 152
~ +[BuddyAccessibilityUtilitiesAccessibility navigationBarButton] : 128 -> 136
~ +[BuddyAccessibilityUtilitiesAccessibility navigationBarButtonItemWithTarget:selector:] : 128 -> 136
~ +[LabeledSliderAccessibility _accessibilityPerformValidations:] : 120 -> 128
~ -[LabeledSliderAccessibility _accessibilityLabeledSliderValue] : 120 -> 124
~ -[LabeledSliderAccessibility _accessibilityReportModeChanged] : 376 -> 388
~ -[LabeledSliderAccessibility accessibilityValue] : 240 -> 256
~ +[BuddyExpressSetupFeatureCardPrimaryCellAccessibility _accessibilityPerformValidations:] : 200 -> 208
~ +[BuddyExpressSetupFeatureCardCellAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ +[BuddySceneDelegateAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ +[BFFProximityVisualPairingViewControllerAccessibility _accessibilityPerformValidations:] : 120 -> 128
~ -[BFFProximityVisualPairingViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 140 -> 148
~ -[BuddyAppleIDServiceViewAccessibility accessibilityLabel] : 84 -> 92
~ +[BuddyFinishedControllerAccessibility _accessibilityPerformValidations:] : 116 -> 124
~ -[BuddyFinishedControllerAccessibility _accessibilityLoadAccessibilityInformation] : 232 -> 240
~ +[BuddyPosedDeviceSelectionViewAccessibility _accessibilityPerformValidations:] : 240 -> 252
~ -[BuddyPosedDeviceSelectionViewAccessibility _accessibilityLoadAccessibilityInformation] : 580 -> 592
~ +[BuddyLanguageControllerAccessibility _accessibilityPerformValidations:] : 252 -> 260
~ -[BuddyLanguageControllerAccessibility _accessibilityLoadAccessibilityInformation] : 100 -> 104
~ -[BuddyLanguageControllerAccessibility _selectLanguage:] : 252 -> 272
~ -[BuddyLanguageControllerAccessibility tableView:cellForRowAtIndexPath:] : 588 -> 600
~ ___72-[BuddyLanguageControllerAccessibility tableView:cellForRowAtIndexPath:]_block_invoke : 224 -> 240
~ +[BuddyLocaleControllerAccessibility _accessibilityPerformValidations:] : 380 -> 388
~ -[BuddyLocaleControllerAccessibility setLanguage:] : 228 -> 240
~ -[BuddyLocaleControllerAccessibility tableView:cellForRowAtIndexPath:] : 532 -> 568
~ -[BuddyLocaleControllerAccessibility _accessibilitySelectedLanguage] : 160 -> 168
~ -[BuddyLocaleControllerAccessibility _accessibilityUpdateLanguageOnLabel:] : 152 -> 172
~ +[BuddyNavigationFlowControllerAccessibility _accessibilityPerformValidations:] : 280 -> 288
~ -[BuddyNavigationFlowControllerAccessibility accessibilityIdentifier] : 356 -> 380
~ ___133-[BuddyNavigationFlowControllerAccessibility _presentViewControllerForBuddyController:animated:willPresentViewController:completion:]_block_invoke : 216 -> 220
~ -[BuddyNavigationFlowControllerAccessibility _accessibilityMarkMainNavBar] : 180 -> 192
~ -[BuddyNavigationFlowControllerAccessibility wifiController] : 156 -> 164
~ -[BuddyProximitySetupControllerAccessibility _accessibilityLoadAccessibilityInformation] : 200 -> 216
~ +[BuddyTableViewControllerAccessibility _accessibilityPerformValidations:] : 124 -> 136
~ -[BuddyTableViewControllerAccessibility _accessibilityMarkTableViewAsNotAXElement] : 156 -> 164
~ -[BuddyTableViewControllerAccessibility init] : 208 -> 220
~ +[CDPRemoteDeviceSecretValidatorAccessibility__CoreCDPUI__Setup _accessibilityPerformValidations:] : 136 -> 144
~ -[CDPRemoteDeviceSecretValidatorAccessibility__CoreCDPUI__Setup initWithContext:validator:] : 236 -> 228
~ +[CDPRemoteSecretEntryViewControllerAccessibility__Setup__CoreCDPUI _accessibilityPerformValidations:] : 204 -> 212
~ -[CDPRemoteSecretEntryViewControllerAccessibility__Setup__CoreCDPUI(AXPriv) accessibilityShowsEscapeOffer] : 148 -> 156
~ -[SetupChoiceControllerAccessibility tableView:cellForRowAtIndexPath:] : 324 -> 336
~ +[SetupControllerAccessibility _accessibilityPerformValidations:] : 264 -> 276
~ -[SetupControllerAccessibility accessibilityIdentifier] : 380 -> 408
~ -[SetupControllerAccessibility _accessibilityMarkMainNavBar] : 180 -> 192
~ -[SetupControllerAccessibility _showModalWiFiSettings] : 292 -> 316
~ +[UIBuddyApplicationAccessibility _accessibilityPerformValidations:] : 264 -> 276
~ -[UIBuddyApplicationAccessibility _accessibilityLoadAccessibilityInformation] : 192 -> 200
~ -[UIBuddyApplicationAccessibility _accessibilityFinishSetupIfAppropriate] : 420 -> 440
~ ___73-[UIBuddyApplicationAccessibility _accessibilityFinishSetupIfAppropriate]_block_invoke : 184 -> 196
~ -[UIBuddyApplicationAccessibility _accessibilityCanRequestSetupControllerSafely] : 360 -> 368
~ -[BuddyUIImageViewAccessibility isAccessibilityElement] : 120 -> 124
~ -[BuddyUIImageViewAccessibility accessibilityLabel] : 144 -> 156
~ +[BuddyUIViewAccessibility _accessibilityPerformValidations:] : 84 -> 92
~ -[BuddyUIViewAccessibility _accessibilityHitTest:withEvent:] : 500 -> 524
~ +[BuddyUITableViewAccessibility _accessibilityPerformValidations:] : 136 -> 144
~ -[BuddyUITableViewAccessibility isAccessibilityElement] : 220 -> 228
~ -[BuddyUITableViewAccessibility _axSortedAccessibleSubviews] : 92 -> 100
~ -[BuddyUITableViewAccessibility _axChoiceController] : 116 -> 120
~ -[BuddyUITableViewAccessibility _axPrimaryChoiceButton] : 84 -> 92
~ -[BuddyUITableViewAccessibility _axSecondaryChoiceButton] : 84 -> 92
~ -[BuddyUITableViewAccessibility accessibilityElementCount] : 220 -> 236
~ -[BuddyUITableViewAccessibility _accessibilityScannerGroupElements] : 204 -> 220
~ -[BuddyUITableViewAccessibility accessibilityElementAtIndex:] : 332 -> 364
~ -[BuddyUITableViewAccessibility indexOfAccessibilityElement:] : 308 -> 324
~ -[BuddyUITableViewAccessibility _accessibilitySupplementaryHeaderViews] : 140 -> 148
~ -[BuddyUITableViewAccessibility accessibilityFrame] : 284 -> 292
~ -[BuddyUINavigationBarAccessibility accessibilityIdentifier] : 960 -> 1028
~ -[BuddyUILabelAccessibility isAccessibilityElement] : 172 -> 184
~ -[BuddyAppleIDTableHeaderViewAccessibility initWithFrame:] : 172 -> 180

```
