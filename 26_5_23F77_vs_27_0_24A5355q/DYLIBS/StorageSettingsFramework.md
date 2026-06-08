## StorageSettingsFramework

> `/System/Library/AccessibilityBundles/StorageSettingsFramework.axbundle/StorageSettingsFramework`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0xe2c
-  __TEXT.__auth_stubs: 0x150
+3036.2.0.0.0
+  __TEXT.__text: 0xd64
   __TEXT.__objc_methlist: 0x24c
   __TEXT.__cstring: 0x36c
   __TEXT.__unwind_info: 0xd0
-  __TEXT.__objc_classname: 0x1de
-  __TEXT.__objc_methname: 0x3ac
-  __TEXT.__objc_methtype: 0x46
-  __TEXT.__objc_stubs: 0x2c0
-  __DATA_CONST.__got: 0x40
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x80
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xb0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x480
   __AUTH_CONST.__objc_const: 0x750
+  __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 205329A5-0C81-3C55-B5B0-8D4A2BB2B4B9
-  Functions: 44
-  Symbols:   219
-  CStrings:  135
+  UUID: EC7B1C23-3D88-38F8-9AE0-B2054467134B
+  Functions: 43
+  Symbols:   218
+  CStrings:  82
 
Symbols:
+ ___block_literal_global.362
+ ___block_literal_global.364
+ ___block_literal_global.370
+ ___block_literal_global.92
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- +[AXStorageSettingsFrameworkGlue accessibilityInitializeBundle].cold.1
- ___block_literal_global.341
- ___block_literal_global.343
- ___block_literal_global.349
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ _accessibilityPreferencesFrameworkBundleLocalizedString : 200 -> 184
~ +[AXStorageSettingsFrameworkGlue accessibilityInitializeBundle] : 44 -> 40
~ ___63+[AXStorageSettingsFrameworkGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___63+[AXStorageSettingsFrameworkGlue accessibilityInitializeBundle]_block_invoke_3 : 88 -> 84
~ ___63+[AXStorageSettingsFrameworkGlue accessibilityInitializeBundle]_block_invoke_4 : 180 -> 172
~ +[STStorageAppCellAccessibility _accessibilityPerformValidations:] : 156 -> 148
~ +[STStorageAppHeaderCellAccessibility _accessibilityPerformValidations:] : 156 -> 148
~ +[STStorageItemCellAccessibility _accessibilityPerformValidations:] : 160 -> 152
~ -[STStorageItemCellAccessibility accessibilityLabel] : 200 -> 184
~ +[STStorageTipCellAccessibility _accessibilityPerformValidations:] : 244 -> 236
~ -[STStorageTipCellAccessibility _accessibilityLoadAccessibilityInformation] : 204 -> 196
~ -[STStorageTipCellAccessibility accessibilityValue] : 220 -> 212
~ -[STStorageTipCellAccessibility accessibilityHint] : 220 -> 212
~ -[STStorageTipCellAccessibility accessibilityTraits] : 140 -> 136
~ -[STStorageTipCellAccessibility automationElements] : 308 -> 280
~ ___51-[STStorageTipCellAccessibility automationElements]_block_invoke : 132 -> 128
~ -[STStorageTipCellAccessibility accessibilityActivationPoint] : 84 -> 80
~ -[STStorageTipInfoCellAccessibility accessibilityLabel] : 92 -> 84
~ +[STStorageTableCellAccessibility _accessibilityPerformValidations:] : 188 -> 180
~ -[STStorageTableCellAccessibility accessibilityLabel] : 204 -> 188
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXStorageSettingsFrameworkGlue"
- "B16@0:8"
- "Q16@0:8"
- "SafeCategory"
- "__STStorageAppCellAccessibility_super"
- "__STStorageAppHeaderCellAccessibility_super"
- "__STStorageItemCellAccessibility_super"
- "__STStorageTableCellAccessibility_super"
- "__STStorageTipCellAccessibility_super"
- "__STStorageTipInfoCellAccessibility_super"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_accessibilityStringForLabelKeyValues:"
- "_accessibilityViewIsVisible"
- "accessibilityActivationPoint"
- "accessibilityHint"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityTraits"
- "accessibilityValue"
- "automationElements"
- "axArrayByIgnoringNilElementsWithCount:"
- "axFilterObjectsUsingBlock:"
- "bundleWithPath:"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "isHidden"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeBoolForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeUIViewForKey:"
- "safeUnsignedIntegerForKey:"
- "safeValueForKey:"
- "setIsAccessibilityElement:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "stringByAppendingPathComponent:"
- "v16@0:8"
- "v24@0:8@16"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "{CGPoint=dd}16@0:8"

```
