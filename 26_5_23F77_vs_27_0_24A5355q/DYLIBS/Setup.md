## Setup

> `/System/Library/AccessibilityBundles/Setup.axbundle/Setup`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x58dc
-  __TEXT.__auth_stubs: 0x310
-  __TEXT.__objc_methlist: 0x9e4
-  __TEXT.__cstring: 0x10b1
-  __TEXT.__const: 0x30
+3036.2.0.0.0
+  __TEXT.__text: 0x55bc
+  __TEXT.__objc_methlist: 0xa44
+  __TEXT.__const: 0x28
   __TEXT.__gcc_except_tab: 0x2c
+  __TEXT.__cstring: 0x10ed
   __TEXT.__oslogstring: 0xed
-  __TEXT.__unwind_info: 0x288
-  __TEXT.__objc_classname: 0xa12
-  __TEXT.__objc_methname: 0xf16
-  __TEXT.__objc_methtype: 0x138
-  __TEXT.__objc_stubs: 0xde0
-  __DATA_CONST.__got: 0x100
+  __TEXT.__unwind_info: 0x290
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x150
-  __DATA_CONST.__objc_classlist: 0x1d8
+  __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x490
-  __DATA_CONST.__objc_superrefs: 0xc0
-  __AUTH_CONST.__auth_got: 0x198
+  __DATA_CONST.__objc_selrefs: 0x4a8
+  __DATA_CONST.__objc_superrefs: 0xc8
+  __DATA_CONST.__got: 0x100
   __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x1560
-  __AUTH_CONST.__objc_const: 0x2130
+  __AUTH_CONST.__cfstring: 0x15a0
+  __AUTH_CONST.__objc_const: 0x2250
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x1270
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x1310
   __DATA.__common: 0x8
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FD6B93CB-6F1E-39B8-AE5A-74CAAA7CFF97
-  Functions: 185
-  Symbols:   891
-  CStrings:  592
+  UUID: EF9B6CA0-F942-38D3-BB18-4B67DD438463
+  Functions: 190
+  Symbols:   919
+  CStrings:  369
 
Symbols:
+ +[BuddyAppearanceControllerAccessibility _accessibilityPerformValidations:]
+ +[BuddyAppearanceControllerAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[BuddyAppearanceControllerAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[BuddyAppearanceControllerAccessibility _accessibilityHideAnimationView]
+ -[BuddyAppearanceControllerAccessibility _accessibilityLoadAccessibilityInformation]
+ -[BuddyAppearanceControllerAccessibility viewDidAppear:]
+ GCC_except_table151
+ GCC_except_table91
+ _OBJC_CLASS_$_BuddyAppearanceControllerAccessibility
+ _OBJC_CLASS_$___BuddyAppearanceControllerAccessibility_super
+ _OBJC_METACLASS_$_BuddyAppearanceControllerAccessibility
+ _OBJC_METACLASS_$___BuddyAppearanceControllerAccessibility_super
+ __OBJC_$_CLASS_METHODS_BuddyAppearanceControllerAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_BuddyAppearanceControllerAccessibility
+ __OBJC_CLASS_RO_$_BuddyAppearanceControllerAccessibility
+ __OBJC_CLASS_RO_$___BuddyAppearanceControllerAccessibility_super
+ __OBJC_METACLASS_RO_$_BuddyAppearanceControllerAccessibility
+ __OBJC_METACLASS_RO_$___BuddyAppearanceControllerAccessibility_super
+ ___block_literal_global.428
+ ___block_literal_global.437
+ ___block_literal_global.440
+ ___block_literal_global.534
+ ___block_literal_global.544
+ ___block_literal_global.546
+ ___block_literal_global.554
+ ___block_literal_global.556
+ ___block_literal_global.564
+ ___block_literal_global.566
+ ___block_literal_global.574
+ ___block_literal_global.576
+ ___block_literal_global.825
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_accessibilityHideAnimationView
+ _objc_msgSend$image
+ _objc_msgSend$setAccessibilityElementsHidden:
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x5
+ _objc_retain_x8
- -[BuddyUITableViewAccessibility _axChoiceController].cold.1
- GCC_except_table5
- ___block_literal_global.407
- ___block_literal_global.416
- ___block_literal_global.419
- ___block_literal_global.508
- ___block_literal_global.510
- ___block_literal_global.520
- ___block_literal_global.522
- ___block_literal_global.530
- ___block_literal_global.540
- ___block_literal_global.542
- ___block_literal_global.550
- ___block_literal_global.552
CStrings:
+ "BuddyAppearanceControllerAccessibility"
+ "animationViewWrapper"
- "#16@0:8"
- "@16@0:8"
- "@24@0:8q16"
- "@32@0:8@16:24"
- "@32@0:8@16@24"
- "@40@0:8{CGPoint=dd}16@32"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "AXPriv"
- "AXSetupGlue"
- "ActivationControllerAccessibility"
- "B16@0:8"
- "B32@0:8i16@20I28"
- "SafeCategory"
- "__ActivationControllerAccessibility_super"
- "__BFFProximityVisualPairingViewControllerAccessibility_super"
- "__BYBuddySafetyAndHandlingViewControllerProviderAccessibility_super"
- "__BuddyAccessibilityUtilitiesAccessibility_super"
- "__BuddyAppearanceCheckBoxViewAccessibility_super"
- "__BuddyAppleIDServiceViewAccessibility_super"
- "__BuddyAppleIDTableHeaderViewAccessibility_super"
- "__BuddyExpressSetupFeatureCardCellAccessibility_super"
- "__BuddyExpressSetupFeatureCardPrimaryCellAccessibility_super"
- "__BuddyFinishedControllerAccessibility_super"
- "__BuddyLanguageControllerAccessibility_super"
- "__BuddyLocaleControllerAccessibility_super"
- "__BuddyNavigationFlowControllerAccessibility_super"
- "__BuddyPosedDeviceSelectionItemViewAccessibility_super"
- "__BuddyPosedDeviceSelectionViewAccessibility_super"
- "__BuddyProximitySetupControllerAccessibility_super"
- "__BuddySceneDelegateAccessibility_super"
- "__BuddyTableViewControllerAccessibility_super"
- "__BuddyUIImageViewAccessibility_super"
- "__BuddyUILabelAccessibility_super"
- "__BuddyUINavigationBarAccessibility_super"
- "__BuddyUITableViewAccessibility_super"
- "__BuddyUIViewAccessibility_super"
- "__CDPRemoteDeviceSecretValidatorAccessibility__CoreCDPUI__Setup_super"
- "__CDPRemoteSecretEntryViewControllerAccessibility__Setup__CoreCDPUI_super"
- "__LabeledSliderAccessibility_super"
- "__SetupChoiceControllerAccessibility_super"
- "__SetupControllerAccessibility_super"
- "__UIBuddyApplicationAccessibility_super"
- "_accessibilityCanRequestSetupControllerSafely"
- "_accessibilityDescendantOfType:"
- "_accessibilityExpandedStatus"
- "_accessibilityFinishSetupIfAppropriate"
- "_accessibilityHitTest:withEvent:"
- "_accessibilityIncreaseAmount:"
- "_accessibilityLabeledSliderValue"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityMarkMainNavBar"
- "_accessibilityMarkTableViewAsNotAXElement"
- "_accessibilityPerformValidations:"
- "_accessibilityReportModeChanged"
- "_accessibilityScannerGroupElements"
- "_accessibilitySelectedLanguage"
- "_accessibilitySetUnsignedIntegerValue:forKey:"
- "_accessibilitySetUserDefinedMediaAnalysisOptions:"
- "_accessibilityStringForLabelKeyValues:"
- "_accessibilitySupplementaryHeaderViews"
- "_accessibilityUnsignedIntegerValueForKey:"
- "_accessibilityUpdateLanguageOnLabel:"
- "_axChoiceController"
- "_axPrimaryChoiceButton"
- "_axSecondaryChoiceButton"
- "_axSortedAccessibleSubviews"
- "_iosAccessibilityPerformAction:withValue:fencePort:"
- "_iosAccessibilitySetValue:forAttribute:"
- "accessibilityActivationPoint"
- "accessibilityCompareGeometry:"
- "accessibilityDecrement"
- "accessibilityElementAtIndex:"
- "accessibilityElementCount"
- "accessibilityFrame"
- "accessibilityIdentification"
- "accessibilityIdentifier"
- "accessibilityIncrement"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityRespondsToUserInteraction"
- "accessibilitySetIdentification:"
- "accessibilityShowsEscapeOffer"
- "accessibilityTraits"
- "accessibilityValue"
- "addHandler:forFramework:"
- "allObjects"
- "allTargets"
- "arrayWithObjects:count:"
- "axAttributedStringWithString:"
- "backButtonTitle"
- "bounds"
- "bundleWithIdentifier:"
- "bundleWithPath:"
- "componentsSeparatedByString:"
- "connectedScenes"
- "convertPoint:toView:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d20@0:8B16"
- "existingBackButtonView"
- "f16@0:8"
- "firstObject"
- "hasPrefix:"
- "indexOfAccessibilityElement:"
- "indexOfObject:"
- "init"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "isEqualToString:"
- "lastObject"
- "length"
- "load"
- "loadAccessibilityBundleForBundle:didLoadCallback:"
- "loadAccessibilityBundleForBundle:didLoadCallback:force:loadAllAccessibilityInfo:"
- "loadView"
- "localizedStringForKey:value:table:"
- "lowercaseString"
- "makeViewController"
- "navigationBar"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "q16@0:8"
- "q24@0:8@16"
- "reloadData"
- "reverseObjectEnumerator"
- "rightBarButtonItem"
- "row"
- "safeArrayForKey:"
- "safeBoolForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeStringForKey:"
- "safeSwiftArrayForKey:"
- "safeSwiftValueForKey:"
- "safeUIViewForKey:"
- "safeUnsignedIntForKey:"
- "safeValueForKey:"
- "safeValueForKeyPath:"
- "setAccessibilityActivationPointBlock:"
- "setAccessibilityIdentifier:"
- "setAccessibilityLabel:"
- "setAccessibilityLanguage:"
- "setAccessibilityRespondsToUserInteraction:"
- "setAccessibilityTraits:"
- "setAttribute:forKey:"
- "setIsAccessibilityElement:"
- "setNeedsLoadAccessibilityInformation"
- "setOverrideProcessName:"
- "setUserInteractionEnabled:"
- "setValidationTargetName:"
- "sharedInstance"
- "sortedArrayUsingSelector:"
- "stringByAppendingString:"
- "stringByTrimmingCharactersInSet:"
- "tableView:cellForRowAtIndexPath:"
- "tableView:heightForHeaderInSection:"
- "text"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v40@0:8@16@24@32"
- "v44@0:8@16B24@?28@?36"
- "validateClass:"
- "validateClass:hasClassMethod:withFullSignature:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:hasProperty:withType:"
- "validateClass:hasSwiftField:withSwiftType:"
- "validateClass:isKindOfClass:"
- "validateProtocol:hasMethod:isInstanceMethod:isRequired:"
- "value"
- "view"
- "viewDidAppear:"
- "viewDidLayoutSubviews"
- "viewDidLoad"
- "visibleViewController"
- "whitespaceAndNewlineCharacterSet"
- "{CGPoint=dd}16@0:8"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"

```
