## FocusUI

> `/System/Library/PrivateFrameworks/FocusUI.framework/FocusUI`

```diff

-  __TEXT.__text: 0x23e00
-  __TEXT.__objc_methlist: 0x305c
-  __TEXT.__const: 0x328
+  __TEXT.__text: 0x23db8
+  __TEXT.__objc_methlist: 0x2fbc
+  __TEXT.__const: 0x318
   __TEXT.__gcc_except_tab: 0x320
   __TEXT.__cstring: 0xde3
   __TEXT.__oslogstring: 0x208

   __DATA_CONST.__const: 0x928
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x148
+  __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c38
+  __DATA_CONST.__objc_selrefs: 0x1bc0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__got: 0x478
   __AUTH_CONST.__const: 0x3c8
   __AUTH_CONST.__cfstring: 0xca0
-  __AUTH_CONST.__objc_const: 0x9f28
+  __AUTH_CONST.__objc_const: 0x9ec8
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH_CONST.__auth_got: 0x5d0
+  __AUTH_CONST.__auth_got: 0x5c8
   __AUTH.__objc_data: 0x458
   __AUTH.__data: 0x58
-  __DATA.__objc_ivar: 0x2f4
-  __DATA.__data: 0xef0
-  __DATA.__bss: 0xa0
+  __DATA.__objc_ivar: 0x2f8
+  __DATA.__data: 0xe90
+  __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0x7d0
-  __DATA_DIRTY.__bss: 0x18
+  __DATA_DIRTY.__bss: 0x28
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 993
-  Symbols:   3885
+  Functions: 994
+  Symbols:   3880
   CStrings:  250
 
Sections:
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[FCUIActivityListView contentHorizontalMargin]
+ -[FCUIActivityListView setContentHorizontalMargin:]
+ GCC_except_table17
+ _OBJC_IVAR_$_FCUIActivityListView._contentHorizontalMargin
+ _objc_msgSend$setContentHorizontalMargin:
- -[FCUIFocusSelectionViewController scrollViewDidScroll:]
- _UIRectRoundToScale
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIScrollViewDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_UIScrollViewDelegate
- __OBJC_$_PROTOCOL_REFS_UIScrollViewDelegate
- __OBJC_LABEL_PROTOCOL_$_UIScrollViewDelegate
- __OBJC_PROTOCOL_$_UIScrollViewDelegate
- _objc_msgSend$_isInAnimationBlock
- _objc_msgSend$_setManualScrollEdgeAppearanceProgress:
- _objc_msgSend$adjustedContentInset
Functions:
~ -[FCUIFocusSelectionViewController viewDidLoad] : 536 -> 420
- -[FCUIFocusSelectionViewController scrollViewDidScroll:]
+ -[FCUIActivityListView setContentHorizontalMargin:]
~ -[FCUIActivityListView _recalculateContentSize] : 380 -> 540
+ -[FCUIActivityListView contentHorizontalMargin]

```
