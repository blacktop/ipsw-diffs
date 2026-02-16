## Movie-QuickLook

> `/System/Library/AccessibilityBundles/Movie-QuickLook.axbundle/Movie-QuickLook`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x554
-  __TEXT.__auth_stubs: 0x100
+3005.16.0.0.0
+  __TEXT.__text: 0x594
+  __TEXT.__auth_stubs: 0xf0
   __TEXT.__objc_methlist: 0xb8
   __TEXT.__cstring: 0x138
   __TEXT.__unwind_info: 0x90

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x88
+  __AUTH_CONST.__auth_got: 0x80
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x1a0
   __AUTH_CONST.__objc_const: 0x2d0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 013F68FC-C150-3327-928C-413F9C1F3092
+  UUID: 2D687740-ACB5-3220-A670-ADCE602462F4
   Functions: 15
-  Symbols:   99
+  Symbols:   98
   CStrings:  55
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ _accessibilityLocalizedString : 176 -> 184
~ +[AXMovieQuickLookGlue accessibilityInitializeBundle] : 100 -> 104
~ ___53+[AXMovieQuickLookGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ +[QLAudioViewControllerAccessibility _accessibilityPerformValidations:] : 148 -> 156
~ -[QLAudioViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 240 -> 256
~ +[QLMovieViewControllerAccessibility _accessibilityPerformValidations:] : 148 -> 156
~ -[QLMovieViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 240 -> 256

```
