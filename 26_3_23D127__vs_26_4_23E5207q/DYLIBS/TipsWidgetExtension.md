## TipsWidgetExtension

> `/System/Library/AccessibilityBundles/TipsWidgetExtension.axbundle/TipsWidgetExtension`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x510
-  __TEXT.__auth_stubs: 0x100
+3005.16.0.0.0
+  __TEXT.__text: 0x550
+  __TEXT.__auth_stubs: 0xf0
   __TEXT.__objc_methlist: 0xc4
   __TEXT.__cstring: 0x12e
   __TEXT.__unwind_info: 0x98

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x88
+  __AUTH_CONST.__auth_got: 0x80
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x1c0
   __AUTH_CONST.__objc_const: 0x2d0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A81EF0C1-1FF6-3780-B881-9BFBA2F56600
+  UUID: AE835363-B61B-348D-A05A-F7321C70AB13
   Functions: 16
-  Symbols:   104
+  Symbols:   103
   CStrings:  64
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXTipsWidgetExtensionGlue accessibilityInitializeBundle] : 148 -> 152
~ ___58+[AXTipsWidgetExtensionGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ ___58+[AXTipsWidgetExtensionGlue accessibilityInitializeBundle]_block_invoke_3 : 92 -> 100
~ _accessibilityTipsLocalizedString : 196 -> 212
~ +[TPSWidgetTipViewAccessibility _accessibilityPerformValidations:] : 152 -> 164
~ -[TPSWidgetTipViewAccessibility accessibilityFrame] : 96 -> 100
~ -[TipsWidgetExtensionUIViewAccessibility _accessibilityUseAccessibilityFrameForHittest] : 124 -> 128
~ -[TipsWidgetExtensionUIViewAccessibility _accessibilityOverridesInvalidFrames] : 124 -> 128
~ -[TipsWidgetExtensionUIViewAccessibility accessibilityFrame] : 208 -> 216

```
