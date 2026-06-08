## TelephonyUIFramework

> `/System/Library/AccessibilityBundles/TelephonyUIFramework.axbundle/TelephonyUIFramework`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x2540
-  __TEXT.__auth_stubs: 0x2b0
-  __TEXT.__objc_methlist: 0x59c
-  __TEXT.__cstring: 0x927
+3036.2.0.0.0
+  __TEXT.__text: 0x231c
+  __TEXT.__objc_methlist: 0x524
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__unwind_info: 0x180
-  __TEXT.__objc_classname: 0x427
-  __TEXT.__objc_methname: 0x8cc
-  __TEXT.__objc_methtype: 0x5a
-  __TEXT.__objc_stubs: 0x860
-  __DATA_CONST.__got: 0xd0
+  __TEXT.__cstring: 0x8ba
+  __TEXT.__unwind_info: 0x170
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x150
-  __DATA_CONST.__objc_classlist: 0x100
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c0
-  __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x168
+  __DATA_CONST.__objc_selrefs: 0x2b0
+  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__got: 0xd0
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0xee0
-  __AUTH_CONST.__objc_const: 0x1200
+  __AUTH_CONST.__cfstring: 0xe20
+  __AUTH_CONST.__objc_const: 0x10e0
   __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__bss: 0x8
-  __DATA_DIRTY.__objc_data: 0x9b0
+  __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EBC5FD69-FB70-3D8A-80AA-BAE94CA21BCC
-  Functions: 103
-  Symbols:   520
-  CStrings:  383
+  UUID: 4748D42B-230E-3A5C-BD39-EB1BE1B99666
+  Functions: 95
+  Symbols:   494
+  CStrings:  242
 
Symbols:
+ GCC_except_table42
+ GCC_except_table5
+ GCC_except_table62
+ ___block_literal_global.465
+ ___block_literal_global.471
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- +[TPSlidingButtonAccessibility _accessibilityPerformValidations:]
- +[TPSlidingButtonAccessibility(SafeCategory) safeCategoryBaseClass]
- +[TPSlidingButtonAccessibility(SafeCategory) safeCategoryTargetClassName]
- -[TPSlidingButtonAccessibility _accessibilitySupportsActivateAction]
- -[TPSlidingButtonAccessibility accessibilityActivate]
- -[TPSlidingButtonAccessibility accessibilityLabel]
- -[TPSlidingButtonAccessibility accessibilityTraits]
- -[TPSlidingButtonAccessibility isAccessibilityElement]
- GCC_except_table3
- GCC_except_table4
- GCC_except_table6
- _OBJC_CLASS_$_TPSlidingButtonAccessibility
- _OBJC_CLASS_$___TPSlidingButtonAccessibility_super
- _OBJC_METACLASS_$_TPSlidingButtonAccessibility
- _OBJC_METACLASS_$___TPSlidingButtonAccessibility_super
- __OBJC_$_CLASS_METHODS_TPSlidingButtonAccessibility(SafeCategory)
- __OBJC_$_INSTANCE_METHODS_TPSlidingButtonAccessibility
- __OBJC_CLASS_RO_$_TPSlidingButtonAccessibility
- __OBJC_CLASS_RO_$___TPSlidingButtonAccessibility_super
- __OBJC_METACLASS_RO_$_TPSlidingButtonAccessibility
- __OBJC_METACLASS_RO_$___TPSlidingButtonAccessibility_super
- ___block_literal_global.451
- ___block_literal_global.457
- _objc_msgSend$accessibilityActivate
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
- _objc_retain_x21
- _objc_retain_x24
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXTelephonyUIGlue"
- "B16@0:8"
- "Q16@0:8"
- "SafeCategory"
- "TPButtonAccessibilityElement"
- "TPSlidingButton"
- "TPSlidingButtonAccessibility"
- "_UIActionSlider"
- "__MessageIndicatorViewAccessibility_super"
- "__TPButtonAccessibility_super"
- "__TPDialerNumberPadAccessibility_super"
- "__TPLCDTextViewAccessibility_super"
- "__TPLCDViewAccessibility_super"
- "__TPNumberPadAccessibility_super"
- "__TPNumberPadButtonAccessibility_super"
- "__TPPasscodeViewAccessibility_super"
- "__TPPhonePadAccessibility_super"
- "__TPPillViewAccessibility_super"
- "__TPSetPINKeyPadButtonAccessibility_super"
- "__TPSetPINViewControllerAccessibility_super"
- "__TPSimpleNumberPadAccessibility_super"
- "__TPSlidingButtonAccessibility_super"
- "__UIButtonAccessibility__TelephonyUI__UIKit_super"
- "_acceptButton"
- "_accessibilityCirclePathBasedOnBoundsWidth"
- "_accessibilityIsBlankButton"
- "_accessibilityIsFKARunningForFocusItem"
- "_accessibilityIsScannerGroup"
- "_accessibilityIsSoftwareKeyboardMimic"
- "_accessibilityKeyboardKeyAllowsTouchTyping"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_accessibilityProvidesScannerGroupElements"
- "_accessibilityScannerGroupElements"
- "_accessibilityScannerGroupTraits"
- "_accessibilitySetRetainedValue:forKey:"
- "_accessibilitySupportsActivateAction"
- "_accessibilityValueForKey:"
- "_accessibilityViewIsVisible"
- "accessibilityActivate"
- "accessibilityElements"
- "accessibilityFrame"
- "accessibilityHint"
- "accessibilityIdentification"
- "accessibilityIdentifier"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityPath"
- "accessibilityTraits"
- "accessibilityUserDefinedLabel"
- "accessibilityValue"
- "addObject:"
- "alpha"
- "arrayByAddingObject:"
- "arrayWithCapacity:"
- "axAttributedStringWithString:"
- "bundleWithIdentifier:"
- "count"
- "currentImage"
- "currentTitle"
- "delegate"
- "dictionaryWithObjects:forKeys:count:"
- "init"
- "initWithAccessibilityContainer:"
- "installSafeCategory:canInteractWithTargetClass:"
- "intValue"
- "integerValue"
- "isAccessibilityElement"
- "isEqualToString:"
- "isHidden"
- "lastObject"
- "length"
- "localizedStringForKey:value:table:"
- "localizedStringWithFormat:"
- "lowercaseString"
- "mutableCopy"
- "objectForKey:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "phone.action.answer"
- "rectValue"
- "replaceObjectAtIndex:withObject:"
- "safeBoolForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeStringForKey:"
- "safeSwiftValueForKey:"
- "safeValueForKey:"
- "setAccessibilityFrameInContainerSpace:"
- "setAccessibilityHint:"
- "setAccessibilityIdentifierBlock:"
- "setAccessibilityLabel:"
- "setAccessibilityLabelBlock:"
- "setAccessibilityTraits:"
- "setAttribute:forKey:"
- "setObject:forKey:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "shouldGroupAccessibilityChildren"
- "sizeValue"
- "subarrayWithRange:"
- "type"
- "v16@0:8"
- "v24@0:8@16"
- "validateClass:"
- "validateClass:hasClassMethod:withFullSignature:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:hasProperty:withType:"
- "validateClass:hasSwiftField:withSwiftType:"
- "validateClass:isKindOfClass:"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"

```
