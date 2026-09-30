## StocksFramework

> `/System/Library/AccessibilityBundles/StocksFramework.axbundle/StocksFramework`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xdf4
-  __TEXT.__auth_stubs: 0x1c0
+3005.16.0.0.0
+  __TEXT.__text: 0xeb4
+  __TEXT.__auth_stubs: 0x1b0
   __TEXT.__objc_methlist: 0x128
   __TEXT.__cstring: 0x1cc
   __TEXT.__unwind_info: 0xb8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x248
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xe8
+  __AUTH_CONST.__auth_got: 0xe0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x320
   __AUTH_CONST.__objc_const: 0x2d0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E6F2DD98-CE5A-3B19-969A-E9A7ECA8037D
+  UUID: B1D99E16-EDBE-3B68-ADF3-7F425EFCAC4C
   Functions: 24
-  Symbols:   189
+  Symbols:   188
   CStrings:  143
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x24
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ -[StockAccessibility _accessibilityLabelWithMarketCap:] : 1032 -> 1112
~ -[StockAccessibility _accessibilitySpeakThisString] : 288 -> 312
~ +[StockGraphViewAccessibility _accessibilityPerformValidations:] : 140 -> 148
~ -[StockGraphViewAccessibility accessibilityElementCount] : 120 -> 128
~ -[StockGraphViewAccessibility _accessibilityNanoChildren] : 132 -> 136
~ -[StockGraphViewAccessibility _accessibilityChildrenWithmaxChildrenCount:frame:] : 788 -> 820
~ -[StockGraphViewAccessibility indexOfAccessibilityElement:] : 88 -> 92
~ -[StockGraphViewAccessibility accessibilityElementAtIndex:] : 108 -> 116
~ _accessibilityLocalizedString : 156 -> 164
~ +[AXStocksFrameworkGlue accessibilityInitializeBundle] : 148 -> 152
~ ___54+[AXStocksFrameworkGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___54+[AXStocksFrameworkGlue accessibilityInitializeBundle]_block_invoke_3 : 92 -> 100

```
