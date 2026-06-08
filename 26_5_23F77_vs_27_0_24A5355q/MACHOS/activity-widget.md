## activity-widget

> `/System/Library/AccessibilityBundles/activity-widget.axbundle/activity-widget`

```diff

-1001.19.0.0.0
-  __TEXT.__text: 0xaac
-  __TEXT.__auth_stubs: 0x170
+1029.0.0.0.0
+  __TEXT.__text: 0x9a8
+  __TEXT.__auth_stubs: 0x180
   __TEXT.__objc_stubs: 0x3c0
   __TEXT.__objc_methlist: 0x138
-  __TEXT.__cstring: 0x177
-  __TEXT.__objc_classname: 0xae
+  __TEXT.__cstring: 0x179
+  __TEXT.__objc_classname: 0xac
   __TEXT.__objc_methname: 0x462
   __TEXT.__objc_methtype: 0x38
-  __TEXT.__unwind_info: 0xb0
-  __DATA_CONST.__auth_got: 0xc0
-  __DATA_CONST.__got: 0x30
+  __TEXT.__unwind_info: 0xa0
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0xc8
+  __DATA_CONST.__got: 0x30
   __DATA.__objc_const: 0x2b0
   __DATA.__objc_selrefs: 0x140
   __DATA.__objc_ivar: 0x8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3267FE8F-015F-3589-8680-3C6805682F60
-  Functions: 29
+  UUID: 63569A31-4594-339D-8A57-D2243B6099AF
+  Functions: 28
   Symbols:   132
   CStrings:  95
 
Symbols:
+ __block_literal_global.352
+ __block_literal_global.354
+ __block_literal_global.360
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- +[AXActivityWidgetGlue accessibilityInitializeBundle].cold.1
- __block_literal_global.331
- __block_literal_global.333
- __block_literal_global.339
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[AXActivityWidgetGlue accessibilityInitializeBundle] : 44 -> 40
~ ___53+[AXActivityWidgetGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___53+[AXActivityWidgetGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 96
~ _accessibilityLocalizedString : 168 -> 160
~ -[AXActivityWidgetHeaderValueView accessibilityLabel] : 84 -> 76
~ -[AXActivityWidgetHeaderValueView accessibilityValue] : 84 -> 76
~ -[AXActivityWidgetHeaderValueView headerView] : 16 -> 20
~ -[AXActivityWidgetHeaderValueView setHeaderView:] : 80 -> 20
~ -[AXActivityWidgetHeaderValueView valueView] : 16 -> 20
~ -[AXActivityWidgetHeaderValueView setValueView:] : 80 -> 20
~ +[CHActivityTodayWidgetViewControllerAccessibility _accessibilityPerformValidations:] : 408 -> 400
~ -[CHActivityTodayWidgetViewControllerAccessibility _axUpdateViewAccessibilityElements] : 1076 -> 992

```
