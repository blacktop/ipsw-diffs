## PhotosEditUI

> `/System/Library/AccessibilityBundles/PhotosEditUI.axbundle/PhotosEditUI`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x12f8
-  __TEXT.__auth_stubs: 0x190
+3036.2.0.0.0
+  __TEXT.__text: 0x125c
   __TEXT.__objc_methlist: 0x20c
-  __TEXT.__cstring: 0x354
-  __TEXT.__const: 0x30
+  __TEXT.__const: 0x28
   __TEXT.__gcc_except_tab: 0x18
+  __TEXT.__cstring: 0x354
   __TEXT.__unwind_info: 0x100
-  __TEXT.__objc_classname: 0x1c0
-  __TEXT.__objc_methname: 0x415
-  __TEXT.__objc_methtype: 0x78
-  __TEXT.__objc_stubs: 0x320
-  __DATA_CONST.__got: 0x70
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xb8
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x138
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xd8
+  __DATA_CONST.__got: 0x70
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x420
   __AUTH_CONST.__objc_const: 0x630
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x370
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5F9A4712-8325-355C-B801-72EDAE6FB62D
+  UUID: 336F505F-EE5B-3DE9-8FA6-078E14E519B2
   Functions: 43
-  Symbols:   222
-  CStrings:  136
+  Symbols:   223
+  CStrings:  75
 
Symbols:
+ GCC_except_table38
+ ___block_literal_global.561
+ ___block_literal_global.570
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- GCC_except_table3
- ___block_literal_global.519
- ___block_literal_global.528
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x20
Functions:
~ +[AXPhotosEditUIGlue accessibilityInitializeBundle] : 104 -> 100
~ ___51+[AXPhotosEditUIGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ ___51+[AXPhotosEditUIGlue accessibilityInitializeBundle]_block_invoke_3 : 160 -> 152
~ _accessibilityPhotosEditUILocalizedString : 184 -> 176
~ +[PUAdjustmentsModePickerCellAccessibility _accessibilityPerformValidations:] : 168 -> 160
~ -[PUAdjustmentsModePickerCellAccessibility _accessibilityLoadAccessibilityInformation] : 224 -> 212
~ +[PUCompactAdjustmentsModeBarAccessibility _accessibilityPerformValidations:] : 144 -> 136
~ -[PUCompactAdjustmentsModeBarAccessibility _accessibilityLoadAccessibilityInformation] : 192 -> 184
~ -[PUPhotoEditEffectCellAccessibility accessibilityLabel] : 140 -> 128
~ +[PUTiltWheelControlAccessibility _accessibilityPerformValidations:] : 232 -> 224
~ -[PUTiltWheelControlAccessibility accessibilityValue] : 216 -> 200
~ -[PUTiltWheelControlAccessibility accessibilityIncrement] : 208 -> 200
~ -[PUTiltWheelControlAccessibility accessibilityDecrement] : 208 -> 200
~ -[PUTiltWheelControlAccessibility accessibilityScroll:] : 464 -> 452
~ ___55-[PUTiltWheelControlAccessibility accessibilityScroll:]_block_invoke : 304 -> 296
~ ___55-[PUTiltWheelControlAccessibility accessibilityScroll:]_block_invoke_2 : 304 -> 296
~ -[PUTiltWheelControlAccessibility _transformForTiltAngle:] : 372 -> 360
~ -[PUTiltWheelControlAccessibility _axRadiansToDegrees:] : 28 -> 32
~ -[PUTiltWheelControlAccessibility _axDegreesToRadians:] : 28 -> 32
~ +[PUVideoEditViewControllerAccessibility _accessibilityPerformValidations:] : 168 -> 160
~ -[PUVideoEditViewControllerAccessibility _updateButtonsIfNeeded] : 324 -> 320
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXPhotosEditUIGlue"
- "B16@0:8"
- "B24@0:8q16"
- "Q16@0:8"
- "SafeCategory"
- "__PUAdjustmentsModePickerCellAccessibility_super"
- "__PUCompactAdjustmentsModeBarAccessibility_super"
- "__PUPhotoEditEffectCellAccessibility_super"
- "__PUTiltWheelControlAccessibility_super"
- "__PUVideoEditViewControllerAccessibility_super"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_axDegreesToRadians:"
- "_axRadiansToDegrees:"
- "accessibilityDecrement"
- "accessibilityIncrement"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityScroll:"
- "accessibilityTraits"
- "accessibilityValue"
- "axAttributedStringWithString:"
- "bundleForClass:"
- "d24@0:8d16"
- "floatValue"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeStringForKey:"
- "safeValueForKey:"
- "setAccessibilityLabel:"
- "setAccessibilityValue:"
- "setAttribute:forKey:"
- "setDebugBuild:"
- "setIsAccessibilityElement:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "stringWithFormat:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "{CGAffineTransform=dddddd}24@0:8d16"

```
