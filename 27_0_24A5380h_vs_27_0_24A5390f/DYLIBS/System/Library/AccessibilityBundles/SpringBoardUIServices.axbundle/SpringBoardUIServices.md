## SpringBoardUIServices

> `/System/Library/AccessibilityBundles/SpringBoardUIServices.axbundle/SpringBoardUIServices`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__DATA_DIRTY.__objc_data`

```diff

-3042.0.0.0.0
-  __TEXT.__text: 0x4a28
-  __TEXT.__objc_methlist: 0xb44
+3045.0.0.0.0
+  __TEXT.__text: 0x4ba4
+  __TEXT.__objc_methlist: 0xb4c
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x80
   __TEXT.__cstring: 0x116b
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x290
+  __TEXT.__unwind_info: 0x2a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x1c0
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4e0
-  __DATA_CONST.__objc_superrefs: 0x80
+  __DATA_CONST.__objc_selrefs: 0x4e8
+  __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__got: 0x150
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x1500

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 207
-  Symbols:   720
+  Functions: 208
+  Symbols:   722
   CStrings:  190
 
Symbols:
+ -[SBPasscodeNumberPadButtonAccessibility accessibilityHint]
+ GCC_except_table108
+ GCC_except_table124
+ GCC_except_table163
+ GCC_except_table42
+ _objc_msgSend$accessibilityValue
- GCC_except_table107
- GCC_except_table123
- GCC_except_table162
- GCC_except_table41
Functions:
~ +[SBPasscodeNumberPadButtonAccessibility _accessibilityPerformValidations:] : 4 -> 124
+ -[SBPasscodeNumberPadButtonAccessibility accessibilityHint]
~ -[SBUISimpleFixedDigitPasscodeEntryFieldAccessibility _deleteLastCharacter] : 112 -> 164
```
