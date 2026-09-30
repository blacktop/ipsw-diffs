## Shortcuts

> `/System/Library/AccessibilityBundles/Shortcuts.axbundle/Shortcuts`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xb00
-  __TEXT.__auth_stubs: 0x190
+3005.16.0.0.0
+  __TEXT.__text: 0xb60
+  __TEXT.__auth_stubs: 0x170
   __TEXT.__objc_methlist: 0xd4
   __TEXT.__cstring: 0x286
   __TEXT.__const: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xe8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xd0
+  __AUTH_CONST.__auth_got: 0xc0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x3c0
   __AUTH_CONST.__objc_const: 0x2d0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 78D684ED-439D-3E98-8696-FF1A19900EDA
+  UUID: 2E599B7B-38BB-3D3F-A1F3-9F62FF92D84B
   Functions: 23
-  Symbols:   138
+  Symbols:   136
   CStrings:  106
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ +[AXShortcutsGlue accessibilityInitializeBundle] : 148 -> 152
~ ___48+[AXShortcutsGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___48+[AXShortcutsGlue accessibilityInitializeBundle]_block_invoke_3 : 92 -> 100
~ _accessibilityLocalizedString : 176 -> 184
~ +[LibraryCellAccessibility _accessibilityPerformValidations:] : 416 -> 424
~ -[LibraryCellAccessibility accessibilityLabel] : 244 -> 272
~ -[LibraryCellAccessibility accessibilityCustomActions] : 704 -> 724
~ -[LibraryCellAccessibility _axLibraryViewController] : 92 -> 100
~ -[LibraryViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 132 -> 140

```
