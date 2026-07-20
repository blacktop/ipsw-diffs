## QuickLook

> `/System/Library/AccessibilityBundles/QuickLook.axbundle/QuickLook`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-3042.0.0.0.0
-  __TEXT.__text: 0x3054
-  __TEXT.__objc_methlist: 0x4ec
+3045.0.0.0.0
+  __TEXT.__text: 0x3120
+  __TEXT.__objc_methlist: 0x504
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0xa4
-  __TEXT.__cstring: 0xa83
+  __TEXT.__cstring: 0xa9c
   __TEXT.__oslogstring: 0x20
   __TEXT.__unwind_info: 0x1a8
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__const: 0x1a8
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e0
+  __DATA_CONST.__objc_selrefs: 0x2f0
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__got: 0xd8
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0xe00
+  __AUTH_CONST.__cfstring: 0xe40
   __AUTH_CONST.__objc_const: 0x1050
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 96
-  Symbols:   422
-  CStrings:  134
+  Functions: 98
+  Symbols:   425
+  CStrings:  136
 
Symbols:
+ -[QLOverlayPlayButtonAccessibility _accessibilityUpdatePlayButtonLabelForPlaying:]
+ -[QLOverlayPlayButtonAccessibility setPlaying:]
+ GCC_except_table81
+ _objc_msgSend$_accessibilityUpdatePlayButtonLabelForPlaying:
- GCC_except_table79
Functions:
~ +[QLOverlayPlayButtonAccessibility _accessibilityPerformValidations:] : 172 -> 212
~ -[QLOverlayPlayButtonAccessibility _accessibilityLoadAccessibilityInformation] : 132 -> 80
+ -[QLOverlayPlayButtonAccessibility _accessibilityUpdatePlayButtonLabelForPlaying:]
+ -[QLOverlayPlayButtonAccessibility setPlaying:]
CStrings:
+ "pause.button"
+ "setPlaying:"
```
