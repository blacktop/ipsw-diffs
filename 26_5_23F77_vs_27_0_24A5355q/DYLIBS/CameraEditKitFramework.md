## CameraEditKitFramework

> `/System/Library/AccessibilityBundles/CameraEditKitFramework.axbundle/CameraEditKitFramework`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x39fc
-  __TEXT.__auth_stubs: 0x250
+3036.2.0.0.0
+  __TEXT.__text: 0x39a8
   __TEXT.__objc_methlist: 0x4c4
-  __TEXT.__cstring: 0x8c0
   __TEXT.__const: 0x28
   __TEXT.__gcc_except_tab: 0x28
+  __TEXT.__cstring: 0x8c0
   __TEXT.__unwind_info: 0x1c8
-  __TEXT.__objc_classname: 0x20c
-  __TEXT.__objc_methname: 0xa65
-  __TEXT.__objc_methtype: 0xc5
-  __TEXT.__objc_stubs: 0xaa0
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x200
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x340
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x138
+  __DATA_CONST.__got: 0xa0
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0xe40
   __AUTH_CONST.__objc_const: 0x870
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x4b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 98674DFB-E9DC-3B77-A97A-86E776A61F5A
+  UUID: 1144262A-C873-3220-9AFC-94B9810A9314
   Functions: 116
-  Symbols:   469
-  CStrings:  376
+  Symbols:   471
+  CStrings:  240
 
Symbols:
+ GCC_except_table14
+ GCC_except_table80
+ ___block_literal_global.20
+ ___block_literal_global.561
+ ___block_literal_global.612
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- GCC_except_table15
- GCC_except_table6
- ___block_literal_global.519
- ___block_literal_global.528
- _objc_retainAutoreleasedReturnValue
Functions:
~ +[AXCameraEditKitFrameworkGlue accessibilityInitializeBundle] : 104 -> 100
~ ___61+[AXCameraEditKitFrameworkGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ ___61+[AXCameraEditKitFrameworkGlue accessibilityInitializeBundle]_block_invoke_3 : 200 -> 192
~ _accessibilityCameraEditKitD2xLocalizedString : 184 -> 176
~ _accessibilityCameraEditKitV2LocalizedString : 184 -> 176
~ _AXScaledSliderValues : 216 -> 220
~ +[CEKApertureSliderAccessibility _accessibilityPerformValidations:] : 440 -> 432
~ -[CEKApertureSliderAccessibility scrollViewDidScroll:] : 200 -> 192
~ -[CEKApertureSliderAccessibility _axAdjustValue:] : 512 -> 500
~ ___49-[CEKApertureSliderAccessibility _axAdjustValue:]_block_invoke : 100 -> 96
~ ___49-[CEKApertureSliderAccessibility _axAdjustValue:]_block_invoke_2 : 84 -> 80
~ ___49-[CEKApertureSliderAccessibility _axAdjustValue:]_block_invoke_3 : 88 -> 84
~ ___49-[CEKApertureSliderAccessibility _axAdjustValue:]_block_invoke_4 : 84 -> 80
~ ___49-[CEKApertureSliderAccessibility _axAdjustValue:]_block_invoke_5 : 88 -> 84
~ -[CEKApertureSliderAccessibility accessibilityLabel] : 92 -> 84
~ -[CEKApertureSliderAccessibility accessibilityValue] : 248 -> 232
~ +[CEKLightingControlAccessibility _accessibilityPerformValidations:] : 380 -> 372
~ -[CEKLightingControlAccessibility accessibilityValue] : 364 -> 340
~ -[CEKLightingControlAccessibility _axChangeToLightingEffectAtIndex:] : 328 -> 316
~ +[CEKExpandingSliderAccessibility _accessibilityPerformValidations:] : 444 -> 436
~ -[CEKExpandingSliderAccessibility accessibilityLabel] : 92 -> 84
~ -[CEKExpandingSliderAccessibility accessibilityFrame] : 300 -> 284
~ -[CEKExpandingSliderAccessibility _axChangeValueInDirection:withLargeStep:] : 364 -> 348
~ -[CEKExpandingSliderAccessibility _axCurrentSliderValue] : 84 -> 80
~ -[CEKExpandingSliderAccessibility _axMinimumValue] : 84 -> 80
~ -[CEKExpandingSliderAccessibility _axMaximumValue] : 84 -> 80
~ -[CEKExpandingSliderAccessibility _axSemanticStyle] : 132 -> 124
~ +[CEKSliderAccessibility _accessibilityPerformValidations:] : 432 -> 424
~ -[CEKSliderAccessibility _axNumberOfTickSegments] : 140 -> 136
~ -[CEKSliderAccessibility accessibilityLabel] : 712 -> 680
~ ___44-[CEKSliderAccessibility accessibilityLabel]_block_invoke : 156 -> 144
~ -[CEKSliderAccessibility accessibilityValue] : 244 -> 424
~ -[CEKSliderAccessibility _axAdjustValue:] : 612 -> 608
~ -[CEKSliderAccessibility scrollViewDidScroll:] : 768 -> 936
~ -[CEKSliderAccessibility accessibilityActivationPoint] : 84 -> 80
~ +[CEKWheelScrubberViewAccessibility _accessibilityPerformValidations:] : 292 -> 280
~ -[CEKWheelScrubberViewAccessibility _axIsFilterChooser] : 124 -> 120
~ -[CEKWheelScrubberViewAccessibility _axPhotoEffect] : 180 -> 172
~ -[CEKWheelScrubberViewAccessibility _axFilterAnnouncement] : 204 -> 192
~ -[CEKWheelScrubberViewAccessibility isPhotoStyleScrubber] : 88 -> 84
~ -[CEKWheelScrubberViewAccessibility accessibilityLabel] : 216 -> 200
~ -[CEKWheelScrubberViewAccessibility accessibilityValue] : 608 -> 556
~ -[CEKWheelScrubberViewAccessibility _axPhotoFilterName] : 464 -> 448
~ -[CEKWheelScrubberViewAccessibility accessibilityHint] : 248 -> 236
~ -[CEKWheelScrubberViewAccessibility accessibilityFrame] : 256 -> 248
~ -[CEKWheelScrubberViewAccessibility accessibilityPath] : 268 -> 256
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXCameraEditKitFrameworkGlue"
- "B16@0:8"
- "B24@0:8q16"
- "CIFilterName"
- "Q16@0:8"
- "Q24@0:8Q16"
- "SafeCategory"
- "__CEKApertureButtonAccessibility_super"
- "__CEKApertureSliderAccessibility_super"
- "__CEKBadgeTextViewAccessibility_super"
- "__CEKExpandingSliderAccessibility_super"
- "__CEKLightingControlAccessibility_super"
- "__CEKSliderAccessibility_super"
- "__CEKWheelScrubberViewAccessibility_super"
- "_accessibilityAncestorIsKindOf:"
- "_accessibilityExpandedStatus"
- "_accessibilityFindAncestor:startWithSelf:"
- "_accessibilityInTopLevelTabLoop"
- "_accessibilityIsVerticalAdjustableElement"
- "_accessibilityOverridesInstructionsHint"
- "_accessibilityPerformValidations:"
- "_accessibilityStringForLabelKeyValues:"
- "_accessibilityViewController"
- "_apertureSliderDidChangeApertureValue:"
- "_apertureSliderDidChangeValue:"
- "_axAdjustValue:"
- "_axChangeToLightingEffectAtIndex:"
- "_axChangeValueInDirection:withLargeStep:"
- "_axCurrentSliderValue"
- "_axFilterAnnouncement"
- "_axGetDeltaForCurrentValue:toIncrement:"
- "_axIsFilterChooser"
- "_axIsSliderExpanded"
- "_axMaximumValue"
- "_axMinimumValue"
- "_axNumberOfTickSegments"
- "_axPhotoEffect"
- "_axPhotoFilterName"
- "_axSemanticStyle"
- "_axValidApertureIndexForDiscreteIndex:"
- "_effectForIndex:"
- "_filterTypeForItemIndex:"
- "_handleContinuousSliderValueChanged:"
- "accessibilityActivate"
- "accessibilityActivationPoint"
- "accessibilityDecrement"
- "accessibilityFrame"
- "accessibilityHint"
- "accessibilityIncrement"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityPath"
- "accessibilityScroll:"
- "accessibilityTraits"
- "accessibilityValue"
- "axArrayByIgnoringNilElementsWithCount:"
- "axAttributedStringWithString:"
- "bezierPathWithRect:"
- "bundleForClass:"
- "convertRect:fromView:"
- "convertRect:toView:"
- "count"
- "d16@0:8"
- "d28@0:8d16B24"
- "floatValue"
- "infoForItemAtIndexPath:"
- "installSafeCategory:canInteractWithTargetClass:"
- "integerValue"
- "isAccessibilityElement"
- "isEqualToString:"
- "isPhotoStyleScrubber"
- "localizedLowercaseString"
- "localizedStringForKey:value:table:"
- "numberWithInteger:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "q16@0:8"
- "safeArrayForKey:"
- "safeBoolForKey:"
- "safeCGFloatForKey:"
- "safeCGSizeForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeDoubleForKey:"
- "safeIntegerForKey:"
- "safeStringForKey:"
- "safeSwiftCGFloatForKey:"
- "safeSwiftIntForKey:"
- "safeSwiftValueForKey:"
- "safeUIViewForKey:"
- "safeUnsignedIntegerForKey:"
- "safeValueForKey:"
- "safeValueForKeyPath:"
- "sendActionsForControlEvents:"
- "setAttribute:forKey:"
- "setDebugBuild:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "sliderDidEndScrolling:"
- "sliderDidScroll:"
- "sliderValueChanged:"
- "sliderWillBeginScrolling:"
- "stringWithFormat:"
- "text"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8q16"
- "v28@0:8q16B24"
- "validateClass:"
- "validateClass:hasClassMethod:withFullSignature:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasSwiftField:withSwiftType:"
- "validateClass:isKindOfClass:"
- "{CGPoint=dd}16@0:8"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"

```
