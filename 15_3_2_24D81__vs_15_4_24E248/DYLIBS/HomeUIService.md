## HomeUIService

> `/System/iOSSupport/System/Library/AccessibilityBundles/HomeUIService.axbundle/Contents/MacOS/HomeUIService`

```diff

-2963.3.13.1.0
-  __TEXT.__text: 0xce4
+2963.10.10.0.0
+  __TEXT.__text: 0xd04
   __TEXT.__auth_stubs: 0x160
   __TEXT.__objc_methlist: 0x1a8
   __TEXT.__cstring: 0x301

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 481C01AA-2918-3D52-883E-4FD1E6D5E41F
-  Functions: 33
-  Symbols:   162
+  UUID: 42E47771-B79D-38C2-A70A-78A47029124F
+  Functions: 34
+  Symbols:   163
   CStrings:  133
 
Symbols:
+ +[AXHomeUIServiceGlue accessibilityInitializeBundle].cold.1
Functions:
~ +[AXHomeUIServiceGlue accessibilityInitializeBundle] : 40 -> 44
~ -[HSPCPasscodeEntryViewAccessibility accessibilityTraits] : 184 -> 188
~ -[HSPCPasscodeEntryViewAccessibility insertText:] : 336 -> 340

```
