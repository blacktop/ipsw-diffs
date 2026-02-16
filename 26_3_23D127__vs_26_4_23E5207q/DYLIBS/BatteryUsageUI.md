## BatteryUsageUI

> `/System/Library/AccessibilityBundles/BatteryUsageUI.axbundle/BatteryUsageUI`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x20c8
-  __TEXT.__auth_stubs: 0x2e0
+3005.16.0.0.0
+  __TEXT.__text: 0x2228
+  __TEXT.__auth_stubs: 0x2d0
   __TEXT.__objc_methlist: 0x328
   __TEXT.__cstring: 0x6c0
   __TEXT.__ustring: 0x12
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x9c
-  __TEXT.__unwind_info: 0x150
+  __TEXT.__unwind_info: 0x158
   __TEXT.__objc_classname: 0x33b
   __TEXT.__objc_methname: 0x748
   __TEXT.__objc_methtype: 0x8a

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x258
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x180
+  __AUTH_CONST.__auth_got: 0x178
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x820
   __AUTH_CONST.__objc_const: 0xa90

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D3795C5E-AF08-30E0-A178-4C04785B515E
+  UUID: BB8B2383-F533-3CDF-A2B0-DD82F0EDC82D
   Functions: 69
-  Symbols:   385
+  Symbols:   384
   CStrings:  248
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x24
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ _accessibilityLocalizedString : 160 -> 168
~ ___53+[AXBatteryUsageUIGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___53+[AXBatteryUsageUIGlue accessibilityInitializeBundle]_block_invoke_3 : 84 -> 88
~ ___53+[AXBatteryUsageUIGlue accessibilityInitializeBundle]_block_invoke_4 : 212 -> 220
~ -[UIAccessibilityElementBatteryLevel setDate:] : 20 -> 80
~ -[PLSegmentedLabelSliderCellAccessibility _accessibilityLoadAccessibilityInformation] : 104 -> 108
~ +[UITableViewAccessibility__BatteryUsageUI__UIKit _accessibilityPerformValidations:] : 104 -> 112
~ -[UITableViewAccessibility__BatteryUsageUI__UIKit _visibleBounds] : 272 -> 276
~ +[PLBatteryUIBatteryBreakDownHeaderCellAccessibility _accessibilityPerformValidations:] : 300 -> 308
~ -[PLBatteryUIBatteryBreakDownHeaderCellAccessibility _accessibilityLoadAccessibilityInformation] : 156 -> 164
~ -[PLBatteryUIBatteryBreakDownHeaderCellAccessibility accessibilityElements] : 204 -> 220
~ -[PLBatteryUIBatteryBreakDownHeaderCellAccessibility buttonAction:] : 200 -> 208
~ +[PLBatteryUIDisplayTableCellAccessibility _accessibilityPerformValidations:] : 148 -> 156
~ -[PLBatteryUIDisplayTableCellAccessibility _accessibilityLoadAccessibilityInformation] : 508 -> 544
~ -[PLBatteryUIDisplayTableCellAccessibility accessibilityLabel] : 172 -> 192
~ -[PLBatteryUIDisplayTableCellAccessibility accessibilityValue] : 236 -> 252
~ +[PLBatteryUIGraphLastChargeCellAccessibility _accessibilityPerformValidations:] : 208 -> 216
~ -[PLBatteryUIGraphLastChargeCellAccessibility _accessibilityLoadAccessibilityInformation] : 464 -> 504
~ +[BatteryChargingControllerAccessibility _accessibilityPerformValidations:] : 332 -> 340
~ -[BatteryChargingControllerAccessibility tableView:willDisplayCell:forRowAtIndexPath:] : 912 -> 904
~ ___86-[BatteryChargingControllerAccessibility tableView:willDisplayCell:forRowAtIndexPath:]_block_invoke : 92 -> 96
~ ___86-[BatteryChargingControllerAccessibility tableView:willDisplayCell:forRowAtIndexPath:]_block_invoke_3 : 360 -> 372
~ +[PLBatteryUITimeUsageCellAccessibility _accessibilityPerformValidations:] : 232 -> 240
~ -[PLBatteryUITimeUsageCellAccessibility _accessibilityLoadAccessibilityInformation] : 700 -> 760

```
