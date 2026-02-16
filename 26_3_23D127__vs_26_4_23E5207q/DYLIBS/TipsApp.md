## TipsApp

> `/System/Library/AccessibilityBundles/TipsApp.axbundle/TipsApp`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xfe8
-  __TEXT.__auth_stubs: 0x1b0
+3005.16.0.0.0
+  __TEXT.__text: 0x10c4
+  __TEXT.__auth_stubs: 0x190
   __TEXT.__objc_methlist: 0x1cc
   __TEXT.__cstring: 0x39d
   __TEXT.__unwind_info: 0xc0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1a0
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xe0
+  __AUTH_CONST.__auth_got: 0xd0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x6c0
   __AUTH_CONST.__objc_const: 0x630

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AB7C2E94-C1A2-3385-A1F5-3441B7F6999F
+  UUID: 0D255E74-EA73-3637-BFB4-44EDF856484B
   Functions: 32
-  Symbols:   215
+  Symbols:   213
   CStrings:  185
 
Symbols:
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXTipsGlue accessibilityInitializeBundle] : 148 -> 152
~ ___43+[AXTipsGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ ___43+[AXTipsGlue accessibilityInitializeBundle]_block_invoke_3 : 152 -> 160
~ _accessibilityLocalizedString : 176 -> 184
~ -[TPSPageControlAccessibility accessibilityValue] : 228 -> 240
~ +[TPSTipCollectionViewCellAccessibility _accessibilityPerformValidations:] : 308 -> 316
~ -[TPSTipCollectionViewCellAccessibility _accessibilityScannerGroupElements] : 336 -> 360
~ -[TPSTipCollectionViewCellAccessibility _accessibilityLoadAccessibilityInformation] : 644 -> 696
~ +[TPSUICollectionViewAccessibility _accessibilityPerformValidations:] : 264 -> 276
~ -[TPSUICollectionViewAccessibility _axIsTipsCollectionView] : 84 -> 88
~ -[TPSUICollectionViewAccessibility _accessibilityFirstVisibleItem] : 180 -> 196
~ -[TPSUICollectionViewAccessibility _accessibilityScrollStatus] : 404 -> 436
~ +[TPSViewControllerAccessibility _accessibilityPerformValidations:] : 132 -> 140
~ +[UIBarButtonItemAccessibility__Tips__UIKit _accessibilityPerformValidations:] : 160 -> 172
~ -[UIBarButtonItemAccessibility__Tips__UIKit accessibilityLabel] : 236 -> 252

```
