## Gif-QuickLook

> `/System/Library/AccessibilityBundles/Gif-QuickLook.axbundle/Gif-QuickLook`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x220
+3005.16.0.0.0
+  __TEXT.__text: 0x240
   __TEXT.__auth_stubs: 0xa0
   __TEXT.__objc_methlist: 0x5c
   __TEXT.__cstring: 0xd8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 790212B4-8F40-3B0B-93FA-4DFEB4624798
+  UUID: E1C28D66-EF8C-38E0-95D1-5D67D34E0DCD
   Functions: 8
   Symbols:   64
   CStrings:  42
Symbols:
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
Functions:
~ +[QLGIFDisplayBundleAccessibility _accessibilityPerformValidations:] : 132 -> 140
~ -[QLGIFDisplayBundleAccessibility viewDidAppear:] : 224 -> 244
~ +[AXGIFQuickLookGlue accessibilityInitializeBundle] : 96 -> 100

```
