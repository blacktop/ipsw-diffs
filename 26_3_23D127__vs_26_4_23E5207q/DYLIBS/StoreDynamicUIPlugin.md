## StoreDynamicUIPlugin

> `/System/Library/AccessibilityBundles/StoreDynamicUIPlugin.axbundle/StoreDynamicUIPlugin`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x950
-  __TEXT.__auth_stubs: 0x150
+3005.16.0.0.0
+  __TEXT.__text: 0x9e0
+  __TEXT.__auth_stubs: 0x140
   __TEXT.__objc_methlist: 0x1e8
   __TEXT.__cstring: 0x2e9
   __TEXT.__unwind_info: 0xc0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xb0
+  __AUTH_CONST.__auth_got: 0xa8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0x630

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 78C1AC3B-B3B2-30F2-B127-3641410CC115
+  UUID: AB5E7F96-3884-3E68-BCBC-415579445D73
   Functions: 35
-  Symbols:   182
+  Symbols:   181
   CStrings:  98
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[TextHeaderComponentAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[TextHeaderComponentAccessibility accessibilityLabel] : 244 -> 268
~ +[RecessedPlatterComponentAccessibility _accessibilityPerformValidations:] : 184 -> 192
~ -[RecessedPlatterComponentAccessibility accessibilityLabel] : 260 -> 292
~ +[OfferPlatterComponentAccessibility _accessibilityPerformValidations:] : 176 -> 184
~ -[OfferPlatterComponentAccessibility accessibilityLabel] : 280 -> 316
~ -[OfferPlatterComponentAccessibility accessibilityActivationPoint] : 80 -> 84
~ +[AXStoreDynamicUIPluginGlue accessibilityInitializeBundle] : 148 -> 152
~ ___59+[AXStoreDynamicUIPluginGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___59+[AXStoreDynamicUIPluginGlue accessibilityInitializeBundle]_block_invoke_3 : 112 -> 120
~ _accessibilityLocalizedString : 176 -> 184

```
