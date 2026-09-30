## AccessibilitySettingsLoader

> `/System/Library/AccessibilityBundles/AccessibilitySettingsLoader.bundle/AccessibilitySettingsLoader`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3234.5.0.0.0
-  __TEXT.__text: 0x125a0
-  __TEXT.__objc_methlist: 0x11bc
+3237.1.0.0.0
+  __TEXT.__text: 0x12b24
+  __TEXT.__objc_methlist: 0x11fc
   __TEXT.__dlopen_cstrs: 0x7e4
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x574
+  __TEXT.__gcc_except_tab: 0x598
   __TEXT.__cstring: 0x20cb
   __TEXT.__oslogstring: 0x6a4
-  __TEXT.__unwind_info: 0x750
+  __TEXT.__unwind_info: 0x770
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd90
+  __DATA_CONST.__objc_selrefs: 0xdc0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__got: 0x290
   __AUTH_CONST.__const: 0x620
   __AUTH_CONST.__cfstring: 0x14e0
-  __AUTH_CONST.__objc_const: 0x23c0
+  __AUTH_CONST.__objc_const: 0x2410
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xaf0
-  __DATA.__objc_ivar: 0x2c
+  __DATA.__objc_ivar: 0x30
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x290
+  __DATA.__bss: 0x2e8
   __DATA_DIRTY.__objc_data: 0x3c0
-  __DATA_DIRTY.__bss: 0x170
+  __DATA_DIRTY.__bss: 0x128
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 413
-  Symbols:   1293
+  Functions: 419
+  Symbols:   1302
   CStrings:  330
 
Symbols:
+ -[AccessibilityFloatingUIKeyboardHelper _mirrorToAssistiveTouchVisible:frame:]
+ -[AccessibilityFloatingUIKeyboardHelper astMessagingCenter]
+ -[AccessibilityFloatingUIKeyboardHelper setAstMessagingCenter:]
+ GCC_except_table323
+ GCC_except_table329
+ GCC_except_table336
+ GCC_except_table352
+ GCC_except_table357
+ GCC_except_table362
+ GCC_except_table373
+ GCC_except_table375
+ GCC_except_table383
+ GCC_except_table413
+ _OBJC_IVAR_$_AccessibilityFloatingUIKeyboardHelper._astMessagingCenter
+ ___78-[AccessibilityFloatingUIKeyboardHelper _mirrorToAssistiveTouchVisible:frame:]_block_invoke
+ _objc_msgSend$_mirrorToAssistiveTouchVisible:frame:
+ _objc_msgSend$astMessagingCenter
+ _objc_msgSend$dictionary
- GCC_except_table322
- GCC_except_table328
- GCC_except_table338
- GCC_except_table350
- GCC_except_table351
- GCC_except_table367
- GCC_except_table369
- GCC_except_table377
- GCC_except_table407
```
