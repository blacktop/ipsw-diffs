## SystemUIWindowingKit

> `/System/Library/AccessibilityBundles/SystemUIWindowingKit.axbundle/SystemUIWindowingKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__DATA_DIRTY.__objc_data`

```diff

-3045.0.0.0.0
-  __TEXT.__text: 0x7e8
+3048.0.0.0.0
+  __TEXT.__text: 0x82c
   __TEXT.__objc_methlist: 0x110
-  __TEXT.__cstring: 0x4b6
+  __TEXT.__cstring: 0x4f8
   __TEXT.__unwind_info: 0x90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe0
+  __DATA_CONST.__objc_selrefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__got: 0x38
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x5a0
+  __AUTH_CONST.__cfstring: 0x5c0
   __AUTH_CONST.__objc_const: 0x3f0
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 20
-  Symbols:   115
-  CStrings:  50
+  Symbols:   117
+  CStrings:  51
 
Symbols:
+ _objc_msgSend$accessibilityIdentifier
+ _objc_msgSend$length
Functions:
~ -[SystemUIWindowingKitUIContextMenuCellContentViewAccessibility accessibilityLabel] : 632 -> 700
CStrings:
+ "com.apple.springboardhome.application-shortcut-item.open-in-split"
```
