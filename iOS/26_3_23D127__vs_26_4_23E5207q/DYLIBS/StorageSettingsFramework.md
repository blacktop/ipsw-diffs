## StorageSettingsFramework

> `/System/Library/AccessibilityBundles/StorageSettingsFramework.axbundle/StorageSettingsFramework`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xd6c
-  __TEXT.__auth_stubs: 0x160
+3005.16.0.0.0
+  __TEXT.__text: 0xe2c
+  __TEXT.__auth_stubs: 0x150
   __TEXT.__objc_methlist: 0x24c
   __TEXT.__cstring: 0x36c
   __TEXT.__unwind_info: 0xd0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xb8
+  __AUTH_CONST.__auth_got: 0xb0
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x480
   __AUTH_CONST.__objc_const: 0x750

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7987E15B-EB07-34BF-820E-60B4ADF0B013
+  UUID: BA4069A2-C1E8-3D95-9F92-C0983E9E641B
   Functions: 44
-  Symbols:   220
+  Symbols:   219
   CStrings:  135
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ _accessibilityPreferencesFrameworkBundleLocalizedString : 184 -> 200
~ ___63+[AXStorageSettingsFrameworkGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___63+[AXStorageSettingsFrameworkGlue accessibilityInitializeBundle]_block_invoke_3 : 84 -> 88
~ ___63+[AXStorageSettingsFrameworkGlue accessibilityInitializeBundle]_block_invoke_4 : 172 -> 180
~ +[STStorageAppCellAccessibility _accessibilityPerformValidations:] : 148 -> 156
~ +[STStorageAppHeaderCellAccessibility _accessibilityPerformValidations:] : 148 -> 156
~ +[STStorageItemCellAccessibility _accessibilityPerformValidations:] : 152 -> 160
~ -[STStorageItemCellAccessibility accessibilityLabel] : 184 -> 200
~ +[STStorageTipCellAccessibility _accessibilityPerformValidations:] : 236 -> 244
~ -[STStorageTipCellAccessibility _accessibilityLoadAccessibilityInformation] : 196 -> 204
~ -[STStorageTipCellAccessibility accessibilityValue] : 204 -> 220
~ -[STStorageTipCellAccessibility accessibilityHint] : 204 -> 220
~ -[STStorageTipCellAccessibility accessibilityTraits] : 136 -> 140
~ -[STStorageTipCellAccessibility automationElements] : 280 -> 308
~ ___51-[STStorageTipCellAccessibility automationElements]_block_invoke : 128 -> 132
~ -[STStorageTipCellAccessibility accessibilityActivationPoint] : 80 -> 84
~ -[STStorageTipInfoCellAccessibility accessibilityLabel] : 84 -> 92
~ +[STStorageTableCellAccessibility _accessibilityPerformValidations:] : 180 -> 188
~ -[STStorageTableCellAccessibility accessibilityLabel] : 188 -> 204

```
