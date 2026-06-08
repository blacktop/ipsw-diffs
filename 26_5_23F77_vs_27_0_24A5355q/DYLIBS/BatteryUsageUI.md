## BatteryUsageUI

> `/System/Library/AccessibilityBundles/BatteryUsageUI.axbundle/BatteryUsageUI`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x2228
-  __TEXT.__auth_stubs: 0x2d0
+3036.2.0.0.0
+  __TEXT.__text: 0x20b8
   __TEXT.__objc_methlist: 0x328
-  __TEXT.__cstring: 0x6c0
-  __TEXT.__ustring: 0x12
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x9c
-  __TEXT.__unwind_info: 0x158
-  __TEXT.__objc_classname: 0x33b
-  __TEXT.__objc_methname: 0x748
-  __TEXT.__objc_methtype: 0x8a
-  __TEXT.__objc_stubs: 0x760
-  __DATA_CONST.__got: 0xa8
+  __TEXT.__cstring: 0x6c2
+  __TEXT.__ustring: 0x12
+  __TEXT.__unwind_info: 0x150
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x148
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x258
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0xa8
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x820
   __AUTH_CONST.__objc_const: 0xa90
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x8
   __DATA_DIRTY.__objc_data: 0x410

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F7594809-3380-329E-A1DF-179703E4A576
-  Functions: 69
-  Symbols:   384
-  CStrings:  248
+  UUID: 8323B697-7E8F-3CA9-A4B8-1BCEA951A75D
+  Functions: 68
+  Symbols:   383
+  CStrings:  138
 
Symbols:
+ GCC_except_table43
+ GCC_except_table47
+ GCC_except_table48
+ GCC_except_table49
+ ___block_literal_global.171
+ ___block_literal_global.360
+ ___block_literal_global.362
+ ___block_literal_global.371
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- +[AXBatteryUsageUIGlue accessibilityInitializeBundle].cold.1
- GCC_except_table10
- GCC_except_table13
- GCC_except_table3
- GCC_except_table8
- ___block_literal_global.339
- ___block_literal_global.341
- ___block_literal_global.350
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x24
Functions:
~ _accessibilityLocalizedString : 168 -> 160
~ +[AXBatteryUsageUIGlue accessibilityInitializeBundle] : 44 -> 40
~ ___53+[AXBatteryUsageUIGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___53+[AXBatteryUsageUIGlue accessibilityInitializeBundle]_block_invoke_3 : 88 -> 84
~ ___53+[AXBatteryUsageUIGlue accessibilityInitializeBundle]_block_invoke_4 : 220 -> 212
~ -[UIAccessibilityElementBatteryLevel batteryLevel] : 16 -> 20
~ -[UIAccessibilityElementBatteryLevel setBatteryLevel:] : 16 -> 20
~ -[UIAccessibilityElementBatteryLevel date] : 16 -> 20
~ -[UIAccessibilityElementBatteryLevel setDate:] : 80 -> 20
~ -[PLSegmentedLabelSliderCellAccessibility _accessibilityLoadAccessibilityInformation] : 108 -> 104
~ +[UITableViewAccessibility__BatteryUsageUI__UIKit _accessibilityPerformValidations:] : 112 -> 104
~ -[UITableViewAccessibility__BatteryUsageUI__UIKit _visibleBounds] : 276 -> 272
~ +[PLBatteryUIBatteryBreakDownHeaderCellAccessibility _accessibilityPerformValidations:] : 308 -> 300
~ -[PLBatteryUIBatteryBreakDownHeaderCellAccessibility _accessibilityLoadAccessibilityInformation] : 164 -> 156
~ -[PLBatteryUIBatteryBreakDownHeaderCellAccessibility accessibilityElements] : 220 -> 204
~ -[PLBatteryUIBatteryBreakDownHeaderCellAccessibility buttonAction:] : 208 -> 200
~ +[PLBatteryUIDisplayTableCellAccessibility _accessibilityPerformValidations:] : 156 -> 148
~ -[PLBatteryUIDisplayTableCellAccessibility _accessibilityLoadAccessibilityInformation] : 544 -> 508
~ -[PLBatteryUIDisplayTableCellAccessibility accessibilityLabel] : 192 -> 172
~ -[PLBatteryUIDisplayTableCellAccessibility accessibilityValue] : 252 -> 236
~ +[PLBatteryUIGraphLastChargeCellAccessibility _accessibilityPerformValidations:] : 216 -> 208
~ -[PLBatteryUIGraphLastChargeCellAccessibility _accessibilityLoadAccessibilityInformation] : 504 -> 464
~ +[BatteryChargingControllerAccessibility _accessibilityPerformValidations:] : 340 -> 332
~ -[BatteryChargingControllerAccessibility tableView:willDisplayCell:forRowAtIndexPath:] : 904 -> 916
~ ___86-[BatteryChargingControllerAccessibility tableView:willDisplayCell:forRowAtIndexPath:]_block_invoke : 96 -> 92
~ ___86-[BatteryChargingControllerAccessibility tableView:willDisplayCell:forRowAtIndexPath:]_block_invoke_3 : 372 -> 360
~ ___86-[BatteryChargingControllerAccessibility tableView:willDisplayCell:forRowAtIndexPath:]_block_invoke_5 : 388 -> 384
~ ___86-[BatteryChargingControllerAccessibility tableView:willDisplayCell:forRowAtIndexPath:]_block_invoke_8 : 388 -> 384
~ +[PLBatteryUITimeUsageCellAccessibility _accessibilityPerformValidations:] : 240 -> 232
~ -[PLBatteryUITimeUsageCellAccessibility _accessibilityLoadAccessibilityInformation] : 760 -> 700
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSDate\""
- "@16@0:8"
- "AXBatteryUsageUIGlue"
- "B16@0:8"
- "Q16@0:8"
- "SafeCategory"
- "T@\"NSDate\",&,N,V_date"
- "Td,N,V_batteryLevel"
- "UIAccessibilityElementBatteryLevel"
- "__BatteryChargingControllerAccessibility_super"
- "__PLBatteryUIBatteryBreakDownHeaderCellAccessibility_super"
- "__PLBatteryUIDisplayTableCellAccessibility_super"
- "__PLBatteryUIGraphLastChargeCellAccessibility_super"
- "__PLBatteryUISuggestionHeaderCellAccessibility_super"
- "__PLBatteryUITimeUsageCellAccessibility_super"
- "__PLSegmentedLabelSliderCellAccessibility_super"
- "__UITableViewAccessibility__BatteryUsageUI__UIKit_super"
- "_accessibilityBoundsOfCellsToLoad"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_accessibilityStringForLabelKeyValues:"
- "_batteryLevel"
- "_date"
- "accessibilityElements"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityTraits"
- "accessibilityValue"
- "accessoryView"
- "addObject:"
- "array"
- "axArrayByIgnoringNilElementsWithCount:"
- "batteryLevel"
- "bounds"
- "bundleForClass:"
- "contentView"
- "count"
- "currentCalendar"
- "d"
- "d16@0:8"
- "date"
- "dateWithTimeIntervalSince1970:"
- "detailTextLabel"
- "doubleValue"
- "identifier"
- "initWithAccessibilityContainer:representedElements:"
- "installSafeCategory:canInteractWithTargetClass:"
- "intValue"
- "isAccessibilityElement"
- "isAccessibilityOpaqueElementProvider"
- "isDate:inSameDayAsDate:"
- "isEqualToString:"
- "localizedStringForKey:value:table:"
- "localizedStringFromNumber:numberStyle:"
- "numberWithFloat:"
- "objectForKeyedSubscript:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "propertyForKey:"
- "representedElements"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeIntForKey:"
- "safeValueForKey:"
- "setAccessibilityDecrementBlock:"
- "setAccessibilityElements:"
- "setAccessibilityIncrementBlock:"
- "setAccessibilityLabel:"
- "setAccessibilityLabelBlock:"
- "setAccessibilityTraits:"
- "setAccessibilityValueBlock:"
- "setBatteryLevel:"
- "setCurrentValue:animated:"
- "setDate:"
- "setIsAccessibilityElement:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "specifier"
- "stringWithFormat:"
- "subviews"
- "tableView:willDisplayCell:forRowAtIndexPath:"
- "textLabel"
- "unsignedLongValue"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8d16"
- "v40@0:8@16@24@32"
- "validateClass:"
- "validateClass:conformsToProtocol:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:isKindOfClass:"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"

```
