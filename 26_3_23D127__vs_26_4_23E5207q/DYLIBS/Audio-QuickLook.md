## Audio-QuickLook

> `/System/Library/AccessibilityBundles/Audio-QuickLook.axbundle/Audio-QuickLook`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x36c
-  __TEXT.__auth_stubs: 0x100
+3005.16.0.0.0
+  __TEXT.__text: 0x394
+  __TEXT.__auth_stubs: 0xf0
   __TEXT.__objc_methlist: 0x68
   __TEXT.__cstring: 0x10e
   __TEXT.__unwind_info: 0x80

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x88
+  __AUTH_CONST.__auth_got: 0x80
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DE975A60-F567-3D0F-94F7-9D1BCBD8269A
+  UUID: 38090A9B-7FB1-3D3C-AB27-1B50E629CD83
   Functions: 10
-  Symbols:   79
+  Symbols:   78
   CStrings:  49
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ _accessibilityLocalizedString : 176 -> 184
~ +[AXAudioQuickLookGlue accessibilityInitializeBundle] : 100 -> 104
~ ___53+[AXAudioQuickLookGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ +[QLAudioViewControllerAccessibility _accessibilityPerformValidations:] : 148 -> 156
~ -[QLAudioViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 240 -> 256

```
