## WorkflowUIServices

> `/System/Library/AccessibilityBundles/WorkflowUIServices.axbundle/WorkflowUIServices`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-3045.0.0.0.0
-  __TEXT.__text: 0x2f7c
-  __TEXT.__objc_methlist: 0x268
+3048.0.0.0.0
+  __TEXT.__text: 0x3144
+  __TEXT.__objc_methlist: 0x270
   __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x23c
-  __TEXT.__cstring: 0x714
-  __TEXT.__unwind_info: 0x1e8
+  __TEXT.__gcc_except_tab: 0x228
+  __TEXT.__cstring: 0x725
+  __TEXT.__unwind_info: 0x1f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x2b8
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x240
+  __DATA_CONST.__objc_selrefs: 0x250
   __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__got: 0xb0
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x8a0
+  __AUTH_CONST.__cfstring: 0x8c0
   __AUTH_CONST.__objc_const: 0x750
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__bss: 0x9

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 70
-  Symbols:   318
-  CStrings:  88
+  Functions: 71
+  Symbols:   321
+  CStrings:  89
 
Symbols:
+ -[WFIntelligencePromptFieldAccessibility accessibilityElements]
+ GCC_except_table59
+ _OBJC_CLASS_$_NSConstantArray
+ _objc_msgSend$_accessibilityViewIsVisible
+ _objc_msgSend$addObject:
- GCC_except_table57
- _objc_msgSend$_accessibilitySetSortPriority:
Functions:
~ +[WFIntelligencePromptFieldAccessibility _accessibilityPerformValidations:] : 236 -> 264
~ -[WFIntelligencePromptFieldAccessibility _accessibilityLoadAccessibilityInformation] : 1064 -> 1032
+ -[WFIntelligencePromptFieldAccessibility accessibilityElements]
CStrings:
+ "attachmentButton"
```
