## activity-widget

> `/System/Library/AccessibilityBundles/activity-widget.axbundle/activity-widget`

```diff

-1001.4.8.0.0
-  __TEXT.__text: 0x9b8
-  __TEXT.__auth_stubs: 0x180
+1001.12.0.0.0
+  __TEXT.__text: 0xaac
+  __TEXT.__auth_stubs: 0x170
   __TEXT.__objc_stubs: 0x3c0
   __TEXT.__objc_methlist: 0x138
   __TEXT.__cstring: 0x177
   __TEXT.__objc_classname: 0xae
   __TEXT.__objc_methname: 0x462
   __TEXT.__objc_methtype: 0x38
-  __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0xc8
+  __TEXT.__unwind_info: 0xb0
+  __DATA_CONST.__auth_got: 0xc0
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__cfstring: 0x220

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 25F87EFD-AE25-36F0-806B-4D1B1F8EB45B
+  UUID: F7C868D3-524E-363D-8181-E0FA430FF454
   Functions: 29
-  Symbols:   133
+  Symbols:   132
   CStrings:  95
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ ___53+[AXActivityWidgetGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___53+[AXActivityWidgetGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ _accessibilityLocalizedString : 160 -> 168
~ -[AXActivityWidgetHeaderValueView accessibilityLabel] : 76 -> 84
~ -[AXActivityWidgetHeaderValueView accessibilityValue] : 76 -> 84
~ -[AXActivityWidgetHeaderValueView setHeaderView:] : 20 -> 80
~ -[AXActivityWidgetHeaderValueView setValueView:] : 20 -> 80
~ +[CHActivityTodayWidgetViewControllerAccessibility _accessibilityPerformValidations:] : 400 -> 408
~ -[CHActivityTodayWidgetViewControllerAccessibility _axUpdateViewAccessibilityElements] : 992 -> 1076

```
