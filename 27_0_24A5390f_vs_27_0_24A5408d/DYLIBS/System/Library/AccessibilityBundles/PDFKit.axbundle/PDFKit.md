## PDFKit

> `/System/Library/AccessibilityBundles/PDFKit.axbundle/PDFKit`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3045.0.0.0.0
-  __TEXT.__text: 0xa218
-  __TEXT.__objc_methlist: 0xcd0
+3048.0.0.0.0
+  __TEXT.__text: 0xa2e4
+  __TEXT.__objc_methlist: 0xce0
   __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0xc4
   __TEXT.__cstring: 0xec4

   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa20
+  __DATA_CONST.__objc_selrefs: 0xa30
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__got: 0x2f8
   __AUTH_CONST.__const: 0x180

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 246
-  Symbols:   912
+  Functions: 247
+  Symbols:   914
   CStrings:  195
 
Symbols:
+ -[PDFAnnotationAccessibilityElement accessibilityActivate]
+ GCC_except_table171
+ GCC_except_table199
+ GCC_except_table224
+ GCC_except_table66
+ GCC_except_table81
+ _objc_msgSend$addControl
- GCC_except_table170
- GCC_except_table198
- GCC_except_table223
- GCC_except_table65
- GCC_except_table80
Functions:
+ -[PDFAnnotationAccessibilityElement accessibilityActivate]
~ -[PDFPageViewAccessibility accessibilityElements] : 328 -> 312
```
