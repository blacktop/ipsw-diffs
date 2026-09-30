## DocumentManagerExecutables

> `/System/iOSSupport/System/Library/AccessibilityBundles/DocumentManagerExecutables.axbundle/Contents/MacOS/DocumentManagerExecutables`

```diff

-2963.3.13.1.0
-  __TEXT.__text: 0xa54
+2963.10.10.0.0
+  __TEXT.__text: 0xa6c
   __TEXT.__auth_stubs: 0x130
   __TEXT.__objc_methlist: 0x1dc
   __TEXT.__cstring: 0x2ec
-  __TEXT.__unwind_info: 0xc8
+  __TEXT.__unwind_info: 0xb8
   __TEXT.__objc_classname: 0x1a4
   __TEXT.__objc_methname: 0x3f3
   __TEXT.__objc_methtype: 0x5d

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 92F66769-67C3-3578-B7E2-8977CF117F1A
+  UUID: 762342EA-E928-3A72-8534-820EF8F1D186
   Functions: 36
-  Symbols:   160
+  Symbols:   161
   CStrings:  126
 
Symbols:
+ +[AXDocumentManagerExecutablesGlue accessibilityInitializeBundle].cold.1
Functions:
~ +[AXDocumentManagerExecutablesGlue accessibilityInitializeBundle] : 40 -> 44
~ -[DOCTagCheckableDotViewAccessibility accessibilityLabel] : 296 -> 324
~ sub_262ca1dc4 -> -[DOCTagCheckableDotViewAccessibility accessibilityTraits] : 28 -> 76
~ -[DOCTagCheckableDotViewAccessibility accessibilityTraits] -> +[DOCAddTagViewAccessibility(SafeCategory) safeCategoryTargetClassName] : 76 -> 12
~ +[DOCAddTagViewAccessibility(SafeCategory) safeCategoryBaseClass] -> +[DOCAddTagViewAccessibility _accessibilityPerformValidations:] : 12 -> 136
~ +[DOCAddTagViewAccessibility _accessibilityPerformValidations:] -> -[DOCAddTagViewAccessibility initWithFrame:] : 136 -> 88
~ -[DOCAddTagViewAccessibility initWithFrame:] -> -[DOCAddTagViewAccessibility _accessibilityLoadAccessibilityInformation] : 88 -> 132
~ -[DOCAddTagViewAccessibility _accessibilityLoadAccessibilityInformation] -> +[AXDocumentManagerExecutablesGlue accessibilityInitializeBundle].cold.1 : 132 -> 20

```
