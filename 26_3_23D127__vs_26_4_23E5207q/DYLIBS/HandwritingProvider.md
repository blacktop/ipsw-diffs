## HandwritingProvider

> `/System/Library/AccessibilityBundles/HandwritingProvider.axbundle/HandwritingProvider`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xcf0
-  __TEXT.__auth_stubs: 0x1a0
+3005.16.0.0.0
+  __TEXT.__text: 0xd60
+  __TEXT.__auth_stubs: 0x190
   __TEXT.__objc_methlist: 0x1d4
   __TEXT.__cstring: 0x303
   __TEXT.__unwind_info: 0xb8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x178
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xd8
+  __AUTH_CONST.__auth_got: 0xd0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x400
   __AUTH_CONST.__objc_const: 0x3f0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D78DD036-4B42-37C1-BD11-69F743435415
+  UUID: 11AF464C-4BA5-3AE5-B4C1-E3E1FCC8F69F
   Functions: 37
-  Symbols:   185
+  Symbols:   184
   CStrings:  132
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXHandwritingBubbleProviderGlue accessibilityInitializeBundle] : 148 -> 152
~ ___64+[AXHandwritingBubbleProviderGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ ___64+[AXHandwritingBubbleProviderGlue accessibilityInitializeBundle]_block_invoke_3 : 112 -> 120
~ _accessibilityLocalizedString : 160 -> 168
~ +[HWHandwritingItemColectionViewCellAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[HWHandwritingItemColectionViewCellAccessibility accessibilityLabel] : 168 -> 180
~ -[HWHandwritingItemColectionViewCellAccessibility accessibilityHint] : 80 -> 84
~ -[HWHandwritingItemColectionViewCellAccessibility accessibilityCustomActions] : 204 -> 212
~ -[HWHandwritingItemColectionViewCellAccessibility _axDelete] : 72 -> 76
~ +[HWBrowserViewControllerAccessibility _accessibilityPerformValidations:] : 392 -> 400
~ -[HWBrowserViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 160 -> 168
~ -[HWBrowserViewControllerAccessibility _scrollPageToLeft:] : 204 -> 212
~ -[HWBrowserViewControllerAccessibility _scrollPageToRight:] : 204 -> 212
~ -[HWBrowserViewControllerAccessibility _axUpdateAndFocusCanvas] : 88 -> 92
~ -[HWBrowserViewControllerAccessibility _axAnnounceHandwritingViewScroll] : 260 -> 272

```
