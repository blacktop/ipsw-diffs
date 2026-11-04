## SystemStatusUI

> `/System/Library/AccessibilityBundles/SystemStatusUI.axbundle/SystemStatusUI`

```diff

-3050.3.8.0.0
-  __TEXT.__text: 0x74c0
-  __TEXT.__objc_methlist: 0xa7c
+3050.3.12.0.0
+  __TEXT.__text: 0x8f9c
+  __TEXT.__objc_methlist: 0xb8c
   __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x10c
-  __TEXT.__cstring: 0x2404
-  __TEXT.__unwind_info: 0x358
+  __TEXT.__gcc_except_tab: 0x1d8
+  __TEXT.__cstring: 0x28a0
+  __TEXT.__unwind_info: 0x3b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x380
-  __DATA_CONST.__objc_classlist: 0x1a8
+  __DATA_CONST.__const: 0x3c0
+  __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x450
-  __DATA_CONST.__objc_superrefs: 0xc8
+  __DATA_CONST.__objc_selrefs: 0x4c0
+  __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0xe0
-  __DATA_CONST.__got: 0x260
+  __DATA_CONST.__got: 0x270
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x2920
-  __AUTH_CONST.__objc_const: 0x1dd0
+  __AUTH_CONST.__cfstring: 0x2ec0
+  __AUTH_CONST.__objc_const: 0x2130
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x1e0
   __DATA_DIRTY.__objc_data: 0x1090
-  __DATA_DIRTY.__bss: 0x28
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 206
-  Symbols:   668
-  CStrings:  347
+  Functions: 232
+  Symbols:   730
+  CStrings:  395
 
Symbols:
+ +[STUIStatusBarCombinedItemAccessibility _accessibilityPerformValidations:]
+ +[STUIStatusBarCombinedItemAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[STUIStatusBarCombinedItemAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[STUIStatusBarCombinedViewAccessibility _accessibilityPerformValidations:]
+ +[STUIStatusBarCombinedViewAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[STUIStatusBarCombinedViewAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[STUIStatusBarRoundBatteryViewAccessibility _accessibilityPerformValidations:]
+ +[STUIStatusBarRoundBatteryViewAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[STUIStatusBarRoundBatteryViewAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[STUIStatusBarCombinedItemAccessibility applyUpdate:toDisplayItem:]
+ -[STUIStatusBarCombinedViewAccessibility _accessibilityHitTest:withEvent:]
+ -[STUIStatusBarCombinedViewAccessibility _axCellularLabelForPrimary:hasDualSIM:]
+ -[STUIStatusBarCombinedViewAccessibility _axDecoratedIndicatorNodes]
+ -[STUIStatusBarCombinedViewAccessibility _axSignalStringForMode:activeBars:totalBars:]
+ -[STUIStatusBarCombinedViewAccessibility accessibilityElements]
+ -[STUIStatusBarCombinedViewAccessibility isAccessibilityElement]
+ -[STUIStatusBarRoundBatteryViewAccessibility _accessibilitySupplementaryFooterViews]
+ -[STUIStatusBarRoundBatteryViewAccessibility _accessibilitySupportsActivateAction]
+ -[STUIStatusBarRoundBatteryViewAccessibility accessibilityHint]
+ -[STUIStatusBarRoundBatteryViewAccessibility accessibilityTraits]
+ GCC_except_table178
+ GCC_except_table26
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_STUIStatusBarCombinedItemAccessibility
+ _OBJC_CLASS_$_STUIStatusBarCombinedViewAccessibility
+ _OBJC_CLASS_$_STUIStatusBarRoundBatteryViewAccessibility
+ _OBJC_CLASS_$___STUIStatusBarCombinedItemAccessibility_super
+ _OBJC_CLASS_$___STUIStatusBarCombinedViewAccessibility_super
+ _OBJC_CLASS_$___STUIStatusBarRoundBatteryViewAccessibility_super
+ _OBJC_METACLASS_$_STUIStatusBarCombinedItemAccessibility
+ _OBJC_METACLASS_$_STUIStatusBarCombinedViewAccessibility
+ _OBJC_METACLASS_$_STUIStatusBarRoundBatteryViewAccessibility
+ _OBJC_METACLASS_$___STUIStatusBarCombinedItemAccessibility_super
+ _OBJC_METACLASS_$___STUIStatusBarCombinedViewAccessibility_super
+ _OBJC_METACLASS_$___STUIStatusBarRoundBatteryViewAccessibility_super
+ _UIAccessibilityPointForPoint
+ __OBJC_$_CLASS_METHODS_STUIStatusBarCombinedItemAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_STUIStatusBarCombinedViewAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_STUIStatusBarRoundBatteryViewAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_STUIStatusBarCombinedItemAccessibility
+ __OBJC_$_INSTANCE_METHODS_STUIStatusBarCombinedViewAccessibility
+ __OBJC_$_INSTANCE_METHODS_STUIStatusBarRoundBatteryViewAccessibility
+ __OBJC_CLASS_RO_$_STUIStatusBarCombinedItemAccessibility
+ __OBJC_CLASS_RO_$_STUIStatusBarCombinedViewAccessibility
+ __OBJC_CLASS_RO_$_STUIStatusBarRoundBatteryViewAccessibility
+ __OBJC_CLASS_RO_$___STUIStatusBarCombinedItemAccessibility_super
+ __OBJC_CLASS_RO_$___STUIStatusBarCombinedViewAccessibility_super
+ __OBJC_CLASS_RO_$___STUIStatusBarRoundBatteryViewAccessibility_super
+ __OBJC_METACLASS_RO_$_STUIStatusBarCombinedItemAccessibility
+ __OBJC_METACLASS_RO_$_STUIStatusBarCombinedViewAccessibility
+ __OBJC_METACLASS_RO_$_STUIStatusBarRoundBatteryViewAccessibility
+ __OBJC_METACLASS_RO_$___STUIStatusBarCombinedItemAccessibility_super
+ __OBJC_METACLASS_RO_$___STUIStatusBarCombinedViewAccessibility_super
+ __OBJC_METACLASS_RO_$___STUIStatusBarRoundBatteryViewAccessibility_super
+ ___68-[STUIStatusBarCombinedViewAccessibility _axDecoratedIndicatorNodes]_block_invoke
+ ___70-[STUIStatusBarAccessibility _axHitTestCombinedViewAtPoint:withEvent:]_block_invoke
+ ___76-[STUIStatusBarCombinedViewAccessibility _axConfigureElement:forIdentifier:]_block_invoke
+ ___76-[STUIStatusBarCombinedViewAccessibility _axConfigureElement:forIdentifier:]_block_invoke_2
+ ___76-[STUIStatusBarCombinedViewAccessibility _axConfigureElement:forIdentifier:]_block_invoke_3
+ ___76-[STUIStatusBarCombinedViewAccessibility _axConfigureElement:forIdentifier:]_block_invoke_4
+ ___76-[STUIStatusBarCombinedViewAccessibility _axConfigureElement:forIdentifier:]_block_invoke_5
+ ___block_descriptor_32_e12_B24?08^B16l
+ ___block_descriptor_40_e16_B16?0"UIView"8lu32l8
+ _objc_alloc_init
+ _objc_retain_x27
- GCC_except_table27
- __AXSLoadAuxiliaryBundlesWithName
- ___53+[AXSystemStatusUIGlue accessibilityInitializeBundle]_block_invoke_4
- _accessibilityInitializeBundle.onceToken
CStrings:
+ "AXCombinedDecoratedNodes"
+ "AXStatusBarCombinedDataNetworkLabelKey"
+ "AXStatusBarCombinedPrimaryCellularServiceKey"
+ "AXStatusBarCombinedSecondaryCellularServiceKey"
+ "B16@?0@\"UIView\"8"
+ "B24@?0@8^B16"
+ "CCUIHeaderPocketView"
+ "STStatusBarItemUpdate"
+ "STUIStatusBarCombined."
+ "STUIStatusBarCombined.airplane"
+ "STUIStatusBarCombined.cellularPrimary"
+ "STUIStatusBarCombined.cellularSecondary"
+ "STUIStatusBarCombined.liquid"
+ "STUIStatusBarCombined.satellite"
+ "STUIStatusBarCombined.sos"
+ "STUIStatusBarCombined.wifi"
+ "STUIStatusBarCombinedItem"
+ "STUIStatusBarCombinedItemAccessibility"
+ "STUIStatusBarCombinedView"
+ "STUIStatusBarCombinedViewAccessibility"
+ "STUIStatusBarRoundBatteryView"
+ "STUIStatusBarRoundBatteryViewAccessibility"
+ "STUIStatusBarVisualProvider"
+ "_UIRoundBatteryView"
+ "`"
+ "bottomCellularEnabled"
+ "bottomCellularNumberOfActiveBars"
+ "bottomCellularSOSEnabled"
+ "bottomCellularSignalMode"
+ "cellularEntry"
+ "enabled"
+ "expanded"
+ "isBootstrapCellular"
+ "networkType"
+ "secondaryCellularEntry"
+ "secondaryStatusBar"
+ "status.cellular.sos"
+ "status.wifi.disabled"
+ "status.wifi.warning"
+ "status.wlan.disabled"
+ "status.wlan.warning"
+ "topCellularEnabled"
+ "topCellularNumberOfActiveBars"
+ "topCellularSOSEnabled"
+ "topCellularSignalMode"
+ "wifiMode"
+ "wifiNumberOfActiveBars"
+ "wifiSignalMode"
```
