## Settings-Assistant

> `/System/Library/AccessibilityBundles/Settings-Assistant.axbundle/Settings-Assistant`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x688
-  __TEXT.__auth_stubs: 0xb0
+3036.2.0.0.0
+  __TEXT.__text: 0x618
   __TEXT.__objc_methlist: 0xe0
-  __TEXT.__cstring: 0x1b1
   __TEXT.__const: 0x8
-  __TEXT.__unwind_info: 0xa8
-  __TEXT.__objc_classname: 0xb6
-  __TEXT.__objc_methname: 0x2c1
-  __TEXT.__objc_methtype: 0x3b
-  __TEXT.__objc_stubs: 0x260
-  __DATA_CONST.__got: 0x20
+  __TEXT.__cstring: 0x1b1
+  __TEXT.__unwind_info: 0xa0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xb8
-  __AUTH_CONST.__auth_got: 0x60
+  __DATA_CONST.__got: 0x20
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x280
   __AUTH_CONST.__objc_const: 0x2d0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4B7D2B73-1C6E-3FEB-A9A2-0899D12C2C0B
-  Functions: 22
-  Symbols:   118
-  CStrings:  79
+  UUID: 649AB0CE-016A-34AA-AB4B-9D076BC2F693
+  Functions: 21
+  Symbols:   117
+  CStrings:  44
 
Symbols:
+ ___block_literal_global.352
+ ___block_literal_global.383
+ ___block_literal_global.392
+ ___block_literal_global.397
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
- +[SiriSettingsGlue accessibilityInitializeBundle].cold.1
- ___block_literal_global.331
- ___block_literal_global.362
- ___block_literal_global.371
- ___block_literal_global.376
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ -[ACSettingsSliderViewAccessibility accessibilityLabel] : 188 -> 168
~ -[ACSettingsSliderViewAccessibility accessibilityValue] : 92 -> 84
~ -[ACSettingsSliderViewAccessibility accessibilityDecrement] : 76 -> 72
~ -[ACSettingsSliderViewAccessibility accessibilityIncrement] : 76 -> 72
~ -[ACSettingsSliderViewAccessibility accessibilityTraits] : 68 -> 64
~ -[ACSettingsSwitchViewAccessibility accessibilityLabel] : 92 -> 84
~ -[ACSettingsSwitchViewAccessibility accessibilityValue] : 156 -> 144
~ -[ACSettingsSwitchViewAccessibility accessibilityActivationPoint] : 84 -> 80
~ +[SiriSettingsGlue accessibilityInitializeBundle] : 44 -> 40
~ ___49+[SiriSettingsGlue accessibilityInitializeBundle]_block_invoke : 172 -> 164
~ ___49+[SiriSettingsGlue accessibilityInitializeBundle]_block_invoke_2 : 228 -> 224
~ ___49+[SiriSettingsGlue accessibilityInitializeBundle]_block_invoke_3 : 88 -> 84
~ _accessibilityLocalizedString : 184 -> 176
CStrings:
- "#16@0:8"
- "@16@0:8"
- "B16@0:8"
- "Q16@0:8"
- "SafeCategory"
- "SiriSettingsGlue"
- "__ACSettingsSliderViewAccessibility_super"
- "__ACSettingsSwitchViewAccessibility_super"
- "accessibilityActivationPoint"
- "accessibilityDecrement"
- "accessibilityIncrement"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityTraits"
- "accessibilityValue"
- "anyObject"
- "boolValue"
- "bundleForClass:"
- "installSafeCategories:afterDelay:validationTargetName:overrideProcessName:"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeValueForKey:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "{CGPoint=dd}16@0:8"

```
