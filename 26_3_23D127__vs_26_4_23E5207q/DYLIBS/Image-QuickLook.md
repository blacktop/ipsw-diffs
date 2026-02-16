## Image-QuickLook

> `/System/Library/AccessibilityBundles/Image-QuickLook.axbundle/Image-QuickLook`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xa04
-  __TEXT.__auth_stubs: 0x220
+3005.16.0.0.0
+  __TEXT.__text: 0xa74
+  __TEXT.__auth_stubs: 0x230
   __TEXT.__objc_methlist: 0xd0
   __TEXT.__cstring: 0x231
   __TEXT.__const: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x120
+  __AUTH_CONST.__auth_got: 0x128
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0x2d0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 515E5451-88DC-3F0F-8C20-EB08BCC72DC3
+  UUID: 30F84322-5DB6-36FA-B86B-469C0594D6FB
   Functions: 20
-  Symbols:   140
+  Symbols:   141
   CStrings:  100
 
Symbols:
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x21
+ _objc_retain_x23
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ +[AXImageQuickLookGlue accessibilityInitializeBundle] : 104 -> 108
~ +[QLImageItemViewControllerAccessibility _accessibilityPerformValidations:] : 464 -> 472
~ -[QLImageItemViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 208 -> 224
~ -[QLImageItemViewControllerAccessibility _axPhotoDescriptionFromContents:context:] : 732 -> 764
~ ___82-[QLImageItemViewControllerAccessibility _axPhotoDescriptionFromContents:context:]_block_invoke : 80 -> 84
~ +[QLImageDisplayBundleAccessibility _accessibilityPerformValidations:] : 212 -> 220
~ -[QLImageDisplayBundleAccessibility loadWithHints:] : 200 -> 216
~ -[QLImageDisplayBundleAccessibility _axPhotoDescriptionFromItem:] : 268 -> 292

```
