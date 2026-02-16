## TipsNotificationExtension

> `/System/Library/AccessibilityBundles/TipsNotificationExtension.axbundle/TipsNotificationExtension`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x834
-  __TEXT.__auth_stubs: 0x170
+3005.16.0.0.0
+  __TEXT.__text: 0x89c
+  __TEXT.__auth_stubs: 0x160
   __TEXT.__objc_methlist: 0xb4
   __TEXT.__cstring: 0x1da
   __TEXT.__unwind_info: 0x98

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x120
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xc0
+  __AUTH_CONST.__auth_got: 0xb8
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x2c0
   __AUTH_CONST.__objc_const: 0x2d0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0FE1A6C3-4F24-3F99-9F05-B84385B82EF4
+  UUID: EF5D70A2-8045-31B8-BD31-6F33CC9125C2
   Functions: 16
-  Symbols:   132
+  Symbols:   131
   CStrings:  96
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXTipsNotificationExtensionGlue accessibilityInitializeBundle] : 148 -> 152
~ ___64+[AXTipsNotificationExtensionGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ ___64+[AXTipsNotificationExtensionGlue accessibilityInitializeBundle]_block_invoke_3 : 92 -> 100
~ _accessibilityTipsLocalizedString : 196 -> 212
~ -[TipsWidgetExtensionUIViewAccessibility _accessibilityUseAccessibilityFrameForHittest] : 124 -> 128
~ -[TipsWidgetExtensionUIViewAccessibility _accessibilityOverridesInvalidFrames] : 124 -> 128
~ -[TipsWidgetExtensionUIViewAccessibility accessibilityFrame] : 208 -> 216
~ +[TPSSingleTipViewControllerAccessibility _accessibilityPerformValidations:] : 300 -> 308
~ -[TPSSingleTipViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 600 -> 648

```
