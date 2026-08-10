## PrintKitUI

> `/System/Library/PrivateFrameworks/PrintKitUI.framework/PrintKitUI`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-94.0.0.0.0
-  __TEXT.__text: 0x6560c
-  __TEXT.__objc_methlist: 0x716c
+97.0.0.0.0
+  __TEXT.__text: 0x6590c
+  __TEXT.__objc_methlist: 0x7184
   __TEXT.__const: 0x310
-  __TEXT.__gcc_except_tab: 0x1c9c
-  __TEXT.__cstring: 0x2a85
+  __TEXT.__gcc_except_tab: 0x1ba8
+  __TEXT.__cstring: 0x2a97
   __TEXT.__ustring: 0x182
   __TEXT.__dlopen_cstrs: 0x95
   __TEXT.__unwind_info: 0x1718

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4970
+  __DATA_CONST.__objc_selrefs: 0x4988
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x358
   __DATA_CONST.__got: 0x918
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x3b60
-  __AUTH_CONST.__objc_const: 0xa720
+  __AUTH_CONST.__cfstring: 0x3b80
+  __AUTH_CONST.__objc_const: 0xa750
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1630
-  __DATA.__objc_ivar: 0x7cc
+  __DATA.__objc_ivar: 0x7d0
   __DATA.__data: 0xcd8
   __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x320

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2299
-  Symbols:   6205
-  CStrings:  559
+  Functions: 2303
+  Symbols:   6213
+  CStrings:  560
 
Symbols:
+ -[UIPrintPreviewViewController dealloc]
+ -[UIPrintPreviewViewController printPanelDismissed]
+ -[UIPrintPreviewViewController setPrintPanelDismissed:]
+ GCC_except_table77
+ _OBJC_IVAR_$_UIPrintPreviewViewController._printPanelDismissed
+ ___41-[UIPrintPanelViewController setPrinter:]_block_invoke_3
+ ___41-[UIPrintPanelViewController setPrinter:]_block_invoke_4
+ _objc_msgSend$coordinateSpace
+ _objc_msgSend$effectiveGeometry
+ _objc_msgSend$printPanelDismissed
+ _objc_msgSend$setPrintPanelDismissed:
- -[UIPrintPreviewViewController printPanelDidDismiss]
- GCC_except_table120
- _objc_msgSend$printPanelDidDismiss
CStrings:
+ "effectiveGeometry"
```
