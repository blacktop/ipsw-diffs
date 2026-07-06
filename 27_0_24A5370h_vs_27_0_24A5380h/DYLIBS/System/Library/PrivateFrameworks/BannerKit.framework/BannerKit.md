## BannerKit

> `/System/Library/PrivateFrameworks/BannerKit.framework/BannerKit`

```diff

-  __TEXT.__text: 0x2d4b4
-  __TEXT.__objc_methlist: 0x3d0c
+  __TEXT.__text: 0x2d77c
+  __TEXT.__objc_methlist: 0x3d2c
   __TEXT.__const: 0x150
   __TEXT.__cstring: 0x2546
-  __TEXT.__oslogstring: 0x2022
+  __TEXT.__oslogstring: 0x208b
   __TEXT.__gcc_except_tab: 0x1148
-  __TEXT.__unwind_info: 0xfb8
+  __TEXT.__unwind_info: 0xfb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f40
+  __DATA_CONST.__objc_selrefs: 0x1f68
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x120
-  __DATA_CONST.__got: 0x3e0
+  __DATA_CONST.__got: 0x3e8
   __AUTH_CONST.__const: 0x220
   __AUTH_CONST.__cfstring: 0x1fc0
-  __AUTH_CONST.__objc_const: 0xd048
+  __AUTH_CONST.__objc_const: 0xd050
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0x0

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1138
-  Symbols:   4772
-  CStrings:  687
+  Functions: 1140
+  Symbols:   4783
+  CStrings:  688
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__objc_ivar : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[BNContentViewController _updateFrameForChildContentContainer:minimumTopInsetUpdate:interactive:]
+ -[BNContentViewController preferredMinimumTopInsetDidInvalidateInteractive:]
+ -[BNContentViewController viewDidLayoutSubviews]
+ GCC_except_table101
+ GCC_except_table25
+ GCC_except_table82
+ _CGRectNull
+ _NSStringFromCGRect
+ ___98-[BNContentViewController _updateFrameForChildContentContainer:minimumTopInsetUpdate:interactive:]_block_invoke
+ _objc_msgSend$_updateFrameForChildContentContainer:minimumTopInsetUpdate:interactive:
+ _objc_msgSend$_windowInterfaceOrientation
+ _objc_msgSend$preferredMinimumTopInsetDidInvalidate
+ _objc_msgSend$preferredMinimumTopInsetDidInvalidateInteractive:
+ _objc_msgSend$presenter:minimumPreferredEdgeInsetsForBannerFrame:
+ _objc_msgSend$presenterContentViewDidLayoutSubviews:
- -[BNContentViewController _updateFrameForChildContentContainer:minimumTopInsetUpdate:]
- GCC_except_table24
- GCC_except_table32
- GCC_except_table80
- GCC_except_table99
- ___86-[BNContentViewController _updateFrameForChildContentContainer:minimumTopInsetUpdate:]_block_invoke
- _objc_msgSend$_updateFrameForChildContentContainer:minimumTopInsetUpdate:
CStrings:
+ "Banner frame: natural=%{public}@ minInsets=%{public}@ -> final=%{public}@ (presented=%d orientation=%ld)"

```
