## DigitalTouchBalloonProvider

> `/System/Library/AccessibilityBundles/DigitalTouchBalloonProvider.axbundle/DigitalTouchBalloonProvider`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x2ad0
-  __TEXT.__auth_stubs: 0x270
+3036.2.0.0.0
+  __TEXT.__text: 0x28c8
   __TEXT.__objc_methlist: 0x398
-  __TEXT.__cstring: 0x91f
   __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0x14
+  __TEXT.__cstring: 0x91f
   __TEXT.__unwind_info: 0x138
-  __TEXT.__objc_classname: 0x245
-  __TEXT.__objc_methname: 0x9dc
-  __TEXT.__objc_methtype: 0xc6
-  __TEXT.__objc_stubs: 0x780
-  __DATA_CONST.__got: 0xa8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2e8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x148
+  __DATA_CONST.__got: 0xa8
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0xb80
   __AUTH_CONST.__objc_const: 0x750
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x1
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__bss: 0x8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9BFD3C82-4FC9-34AE-BB26-5E2ABFF34F9A
-  Functions: 74
-  Symbols:   353
-  CStrings:  319
+  UUID: BDFACB88-C21F-3A58-A260-25461AC45D9D
+  Functions: 73
+  Symbols:   354
+  CStrings:  197
 
Symbols:
+ GCC_except_table33
+ ___block_literal_global.358
+ ___block_literal_global.360
+ ___block_literal_global.366
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
- +[AXDigitalTouchBalloonProviderSharedGlue accessibilityInitializeBundle].cold.1
- GCC_except_table3
- ___block_literal_global.337
- ___block_literal_global.339
- ___block_literal_global.345
- _objc_retainAutoreleasedReturnValue
Functions:
~ +[AXDigitalTouchBalloonProviderSharedGlue accessibilityInitializeBundle] : 44 -> 40
~ ___72+[AXDigitalTouchBalloonProviderSharedGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___72+[AXDigitalTouchBalloonProviderSharedGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 96
~ ___72+[AXDigitalTouchBalloonProviderSharedGlue accessibilityInitializeBundle]_block_invoke_4 : 180 -> 172
~ _accessibilityLocalizedString : 168 -> 160
~ +[ETHorizontalColorPickerAccessibility _accessibilityPerformValidations:] : 148 -> 140
~ -[ETHorizontalColorPickerAccessibility setDimmed:excludeSelectedColor:animated:] : 376 -> 384
~ +[ETTranscriptDetailCanvasViewControllerAccessibility _accessibilityPerformValidations:] : 1128 -> 1120
~ -[ETTranscriptDetailCanvasViewControllerAccessibility accessibilityPerformEscape] : 268 -> 264
~ ___81-[ETTranscriptDetailCanvasViewControllerAccessibility accessibilityPerformEscape]_block_invoke : 116 -> 112
~ -[ETTranscriptDetailCanvasViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 972 -> 888
~ -[ETTranscriptDetailCanvasViewControllerAccessibility _accessibilityCameraFlipButtonLabelForCurrentCamera] : 152 -> 140
~ -[ETTranscriptDetailCanvasViewControllerAccessibility _accessibilityStringForCurrentCameraPosition] : 260 -> 240
~ -[ETTranscriptDetailCanvasViewControllerAccessibility init] : 132 -> 128
~ -[ETTranscriptDetailCanvasViewControllerAccessibility dealloc] : 120 -> 116
~ -[ETTranscriptDetailCanvasViewControllerAccessibility updateVideoUI] : 288 -> 264
~ -[ETTranscriptDetailCanvasViewControllerAccessibility _cameraFlipButtonTapped] : 156 -> 148
~ -[ETTranscriptDetailCanvasViewControllerAccessibility _setShowingGestureInstructionView:] : 180 -> 172
~ -[ETTranscriptDetailCanvasViewControllerAccessibility _expandColorPickerButtonTapped] : 308 -> 288
~ -[ETTranscriptDetailCanvasViewControllerAccessibility expandUI] : 116 -> 112
~ -[ETTranscriptDetailCanvasViewControllerAccessibility _sendButtonTapped] : 116 -> 112
~ -[ETTranscriptDetailCanvasViewControllerAccessibility videoControllerDidStartPreview:] : 292 -> 268
~ -[ETTranscriptDetailCanvasViewControllerAccessibility videoControllerDidStopPreview:] : 128 -> 124
~ -[ETTranscriptDetailCanvasViewControllerAccessibility colorPicker:requestsPresentColorWheel:] : 164 -> 160
~ -[ETTranscriptDetailCanvasViewControllerAccessibility colorPicker:requestsDismissColorWheel:] : 172 -> 164
~ -[ETTranscriptDetailCanvasViewControllerAccessibility _startShowCompositionControlsTimer] : 388 -> 376
~ -[ETTranscriptDetailCanvasViewControllerAccessibility _axFocusChanged:] : 436 -> 404
~ +[GestureInstructionItemViewAccessibility _accessibilityPerformValidations:] : 132 -> 124
~ -[GestureInstructionItemViewAccessibility accessibilityLabel] : 200 -> 180
~ -[ETCompositionUIButtonAccessibility accessibilityValue] : 316 -> 280
~ -[ETCompositionUIButtonAccessibility accessibilityPath] : 216 -> 192
~ +[ETTranscriptColorWheelAccessibility _accessibilityPerformValidations:] : 412 -> 404
~ -[ETTranscriptColorWheelAccessibility _accessibilityLoadAccessibilityInformation] : 112 -> 108
~ -[ETTranscriptColorWheelAccessibility initWithFrame:] : 84 -> 80
~ -[ETTranscriptColorWheelAccessibility updatePickerPositionForPoint:] : 300 -> 292
~ -[ETTranscriptColorWheelAccessibility touchesBegan:withEvent:] : 132 -> 136
~ -[ETTranscriptColorWheelAccessibility _accessibilityAdjustColorPickerBy:] : 272 -> 268
~ -[ETTranscriptColorWheelAccessibility _accessibilitySpeakPickerColor] : 132 -> 120
~ -[ColorWheelPickerCircleViewAccessibility isAccessibilityElement] : 120 -> 116
~ -[ColorWheelPickerCircleViewAccessibility accessibilityTraits] : 144 -> 140
~ -[ColorWheelPickerCircleViewAccessibility accessibilityValue] : 200 -> 180
~ -[ColorWheelPickerCircleViewAccessibility accessibilityPath] : 160 -> 148
~ -[ColorWheelPickerCircleViewAccessibility accessibilityIncrement] : 188 -> 180
~ -[ColorWheelPickerCircleViewAccessibility accessibilityDecrement] : 188 -> 180
CStrings:
- "#16@0:8"
- "@16@0:8"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "AXDigitalTouchBalloonProviderSharedGlue"
- "B16@0:8"
- "CGRectValue"
- "Q16@0:8"
- "SafeCategory"
- "__ColorWheelPickerCircleViewAccessibility_super"
- "__ETCompositionUIButtonAccessibility_super"
- "__ETHorizontalColorPickerAccessibility_super"
- "__ETTranscriptColorWheelAccessibility_super"
- "__ETTranscriptDetailCanvasViewControllerAccessibility_super"
- "__GestureInstructionItemViewAccessibility_super"
- "_accessibilityAdjustColorPickerBy:"
- "_accessibilityBoolValueForKey:"
- "_accessibilityCameraFlipButtonLabelForCurrentCamera"
- "_accessibilityCirclePathBasedOnBoundsWidth"
- "_accessibilityDecrementColorPicker"
- "_accessibilityDifferenceBetweenAngle:andAngle:"
- "_accessibilityIncrementColorPicker"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityOriginalPickerRotation"
- "_accessibilityPerformValidations:"
- "_accessibilitySetOriginalPickerRotation:"
- "_accessibilitySetRetainedValue:forKey:"
- "_accessibilitySpeakPickerColor"
- "_accessibilityStringForCurrentCameraPosition"
- "_accessibilityValueForKey:"
- "_accessibilityViewIsVisible"
- "_axFocusChanged:"
- "accessibilityBundles"
- "accessibilityDecrement"
- "accessibilityIdentifier"
- "accessibilityIncrement"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityNavigationStyle"
- "accessibilityPath"
- "accessibilityPerformEscape"
- "accessibilityTraits"
- "accessibilityValue"
- "addObserver:selector:name:object:"
- "afterDelay:processBlock:"
- "axColorStringForSpeaking"
- "borderColor"
- "bundleForClass:"
- "cancel"
- "canvasViewController:requestsPresentationStyleExpanded:"
- "colorPicker:requestsDismissColorWheel:"
- "colorPicker:requestsPresentColorWheel:"
- "colorWithCGColor:"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d16@0:8"
- "d32@0:8d16d24"
- "dealloc"
- "defaultCenter"
- "init"
- "initWithTargetSerialQueue:"
- "installSafeCategory:canInteractWithTargetClass:"
- "integerValue"
- "invalidate"
- "isAccessibilityElement"
- "isEqualToString:"
- "layer"
- "localizedStringForKey:value:table:"
- "objectAtIndex:"
- "objectForKeyedSubscript:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "q16@0:8"
- "removeObserver:name:object:"
- "safeCGFloatForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeValueForKey:"
- "setAccessibilityHint:"
- "setAccessibilityIdentifier:"
- "setAccessibilityLabel:"
- "setDebugBuild:"
- "setIsAccessibilityElement:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "shouldGroupAccessibilityChildren"
- "touchesBegan:withEvent:"
- "touchesCancelled:withEvent:"
- "touchesEnded:withEvent:"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8d16"
- "v28@0:8B16B20B24"
- "v32@0:8@16@24"
- "v32@0:8{CGPoint=dd}16"
- "validateClass:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:hasProperty:withType:"
- "validateClass:isKindOfClass:"
- "validateProtocol:hasRequiredInstanceMethod:"

```
