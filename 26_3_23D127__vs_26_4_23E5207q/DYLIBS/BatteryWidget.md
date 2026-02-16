## BatteryWidget

> `/System/Library/AccessibilityBundles/BatteryWidget.axbundle/BatteryWidget`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x648
-  __TEXT.__auth_stubs: 0x150
+3005.16.0.0.0
+  __TEXT.__text: 0x698
+  __TEXT.__auth_stubs: 0x140
   __TEXT.__objc_methlist: 0xc4
   __TEXT.__cstring: 0x229
   __TEXT.__unwind_info: 0x98

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xb0
+  __AUTH_CONST.__auth_got: 0xa8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x280
   __AUTH_CONST.__objc_const: 0x2d0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 647B7396-A40C-3EA5-8E0C-AEAC1CC3AE9D
+  UUID: 8929C3F3-9F59-332D-9BD3-40E914E29E8A
   Functions: 16
-  Symbols:   112
+  Symbols:   111
   CStrings:  82
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXBatteryWidgetGlue accessibilityInitializeBundle] : 148 -> 152
~ ___52+[AXBatteryWidgetGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ ___52+[AXBatteryWidgetGlue accessibilityInitializeBundle]_block_invoke_3 : 92 -> 100
~ _accessibilityLocalizedString : 160 -> 168
~ +[BCBatteryWidgetViewControllerAccessibility _accessibilityPerformValidations:] : 148 -> 156
~ -[BCBatteryWidgetViewControllerAccessibility _updateRowView:withDevice:animated:] : 348 -> 356
~ +[BCBatteryWidgetRowViewAccessibility _accessibilityPerformValidations:] : 184 -> 196
~ -[BCBatteryWidgetRowViewAccessibility accessibilityLabel] : 164 -> 180
~ -[BCBatteryWidgetRowViewAccessibility accessibilityValue] : 208 -> 220

```
