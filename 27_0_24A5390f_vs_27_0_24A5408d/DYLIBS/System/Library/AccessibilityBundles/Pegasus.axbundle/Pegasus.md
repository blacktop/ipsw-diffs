## Pegasus

> `/System/Library/AccessibilityBundles/Pegasus.axbundle/Pegasus`

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
-  __TEXT.__text: 0x1f80
+3048.0.0.0.0
+  __TEXT.__text: 0x1fa4
   __TEXT.__objc_methlist: 0x3f0
   __TEXT.__const: 0x8
   __TEXT.__gcc_except_tab: 0xc8
-  __TEXT.__cstring: 0x6d9
+  __TEXT.__cstring: 0x6de
   __TEXT.__unwind_info: 0x108
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x88
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d8
+  __DATA_CONST.__objc_selrefs: 0x1e0
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__got: 0x70
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x9e0
+  __AUTH_CONST.__cfstring: 0xa00
   __AUTH_CONST.__objc_const: 0xcf0
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 72
-  Symbols:   305
-  CStrings:  90
+  Symbols:   306
+  CStrings:  91
 
Symbols:
+ _objc_msgSend$setAccessibilityContainerType:
Functions:
~ -[PGPictureInPictureViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 100 -> 136
CStrings:
+ "view"
```
