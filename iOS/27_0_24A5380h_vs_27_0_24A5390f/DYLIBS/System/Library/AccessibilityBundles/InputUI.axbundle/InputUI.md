## InputUI

> `/System/Library/AccessibilityBundles/InputUI.axbundle/InputUI`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__DATA_DIRTY.__objc_data`

```diff

-3042.0.0.0.0
-  __TEXT.__text: 0x7c4
+3045.0.0.0.0
+  __TEXT.__text: 0x7e8
   __TEXT.__objc_methlist: 0x74
   __TEXT.__const: 0x10
   __TEXT.__cstring: 0x1d9

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 14
-  Symbols:   108
+  Symbols:   109
   CStrings:  31
 
Symbols:
+ ___UIAccessibilitySafeClass
Functions:
~ ___72-[InputUIWindowAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_3 : 224 -> 260
```
