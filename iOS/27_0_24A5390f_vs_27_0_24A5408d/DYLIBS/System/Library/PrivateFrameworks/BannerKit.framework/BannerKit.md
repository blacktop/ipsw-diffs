## BannerKit

> `/System/Library/PrivateFrameworks/BannerKit.framework/BannerKit`

```diff

-168.0.0.0.0
-  __TEXT.__text: 0x2d8c8
-  __TEXT.__objc_methlist: 0x3d44
+169.0.1.0.0
+  __TEXT.__text: 0x2dc24
+  __TEXT.__objc_methlist: 0x3d8c
   __TEXT.__const: 0x150
   __TEXT.__cstring: 0x2546
   __TEXT.__oslogstring: 0x208b
   __TEXT.__gcc_except_tab: 0x1148
-  __TEXT.__unwind_info: 0xfb8
+  __TEXT.__unwind_info: 0xfb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f90
+  __DATA_CONST.__objc_selrefs: 0x1fa8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__got: 0x3e8
   __AUTH_CONST.__const: 0x220
   __AUTH_CONST.__cfstring: 0x1fc0
-  __AUTH_CONST.__objc_const: 0xd050
+  __AUTH_CONST.__objc_const: 0xd0b0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf50
-  __DATA.__objc_ivar: 0x2b8
+  __DATA.__objc_ivar: 0x2bc
   __DATA.__data: 0x1a50
   __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1142
-  Symbols:   3174
+  Functions: 1144
+  Symbols:   3184
   CStrings:  435
 
Symbols:
+ +[BNBannerLayoutManager _dismissedFrameForContentWithPreferredSize:inUseableContainerFrame:containerBounds:layoutInfo:alignment:overshoot:scale:]
+ +[BNBannerLayoutManager _presentedFrameForContentWithPreferredSize:inUseableContainerFrame:containerBounds:layoutInfo:alignment:scale:]
+ -[BNBannerLayoutManager alignment]
+ -[BNBannerLayoutManager idealContentWidth]
+ -[BNBannerLayoutManager setAlignment:]
+ GCC_except_table100
+ GCC_except_table24
+ GCC_except_table32
+ GCC_except_table81
+ _CGRectIsNull
+ _OBJC_IVAR_$_BNBannerLayoutManager._alignment
+ __OBJC_$_PROP_LIST_BNLayoutManagingPrivate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BNLayoutManagingPrivate
+ _objc_msgSend$_dismissedFrameForContentWithPreferredSize:inUseableContainerFrame:containerBounds:layoutInfo:alignment:overshoot:scale:
+ _objc_msgSend$_presentedFrameForContentWithPreferredSize:inUseableContainerFrame:containerBounds:layoutInfo:alignment:scale:
+ _objc_msgSend$bannerContainmentFrameForPresenter:idealWidth:
+ _objc_msgSend$idealContentWidth
+ _objc_msgSend$preferredBannerAlignmentForPresenter:
+ _objc_msgSend$setAlignment:
- +[BNBannerLayoutManager _dismissedFrameForContentWithPreferredSize:inUseableContainerFrame:containerBounds:layoutInfo:overshoot:scale:]
- +[BNBannerLayoutManager _presentedFrameForContentWithPreferredSize:inUseableContainerFrame:containerBounds:layoutInfo:scale:]
- -[BNContentViewController viewDidLayoutSubviews]
- GCC_except_table101
- GCC_except_table25
- GCC_except_table82
- _objc_msgSend$_dismissedFrameForContentWithPreferredSize:inUseableContainerFrame:containerBounds:layoutInfo:overshoot:scale:
- _objc_msgSend$_presentedFrameForContentWithPreferredSize:inUseableContainerFrame:containerBounds:layoutInfo:scale:
- _objc_msgSend$presenterContentViewDidLayoutSubviews:
```
