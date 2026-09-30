## SpringBoardUI

> `/System/Library/PrivateFrameworks/SpringBoardUI.framework/SpringBoardUI`

```diff

-4557.0.6.103.0
-  __TEXT.__text: 0x178e8
-  __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_methlist: 0x3094
-  __TEXT.__const: 0x360
-  __TEXT.__cstring: 0x1c64
+4557.0.9.100.0
+  __TEXT.__text: 0x18430
+  __TEXT.__auth_stubs: 0x690
+  __TEXT.__objc_methlist: 0x30e4
+  __TEXT.__const: 0x370
+  __TEXT.__cstring: 0x1d21
   __TEXT.__oslogstring: 0x9c5
   __TEXT.__gcc_except_tab: 0x138
-  __TEXT.__unwind_info: 0x910
-  __TEXT.__objc_classname: 0x804
-  __TEXT.__objc_methname: 0x8520
-  __TEXT.__objc_methtype: 0x14ef
-  __TEXT.__objc_stubs: 0x5760
-  __DATA_CONST.__got: 0x3d0
-  __DATA_CONST.__const: 0xc38
-  __DATA_CONST.__objc_classlist: 0x170
+  __TEXT.__unwind_info: 0x928
+  __TEXT.__objc_classname: 0x82f
+  __TEXT.__objc_methname: 0x86b9
+  __TEXT.__objc_methtype: 0x1504
+  __TEXT.__objc_stubs: 0x5960
+  __DATA_CONST.__got: 0x3f0
+  __DATA_CONST.__const: 0xcd8
+  __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_nlclslist: 0x8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2150
+  __DATA_CONST.__objc_selrefs: 0x21d8
   __DATA_CONST.__objc_superrefs: 0xf8
-  __AUTH_CONST.__auth_got: 0x350
+  __AUTH_CONST.__auth_got: 0x358
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x2460
-  __AUTH_CONST.__objc_const: 0x83f0
-  __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x870
-  __DATA.__objc_ivar: 0x3ac
+  __AUTH_CONST.__cfstring: 0x2540
+  __AUTH_CONST.__objc_const: 0x84d8
+  __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH.__objc_data: 0x8c0
+  __DATA.__objc_ivar: 0x3b4
   __DATA.__data: 0x9c8
   __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x5f0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4A34A3F1-6F59-3992-8892-80F17B61F51E
-  Functions: 990
-  Symbols:   3843
-  CStrings:  2415
+  UUID: 690405EC-4B36-3C93-87D9-61948A492E81
+  Functions: 1000
+  Symbols:   3897
+  CStrings:  2452
 
Symbols:
+ +[SBAlertPortalView layerClass]
+ -[SBAlertPortalView _shouldAnimatePropertyWithKey:]
+ -[UIView(SBAlertControllerHack) sb_recursivelyFindAlertControllerSubviewWithGlass]
+ -[_SBAlertController viewDidMoveToWindow:shouldAppearOrDisappear:]
+ -[_SBAlertController viewWillDisappear:]
+ _CGAffineTransformMakeScale
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$_SBAlertPortalView
+ _OBJC_CLASS_$__UIViewGlass
+ _OBJC_IVAR_$__SBAlertController._glassView
+ _OBJC_IVAR_$__SBAlertController._portalView
+ _OBJC_METACLASS_$_SBAlertPortalView
+ __OBJC_$_CATEGORY_UIView_$_SBAlertControllerHack
+ __OBJC_$_CLASS_METHODS_SBAlertPortalView
+ __OBJC_$_INSTANCE_METHODS_SBAlertPortalView
+ __OBJC_$_INSTANCE_METHODS_UIView(SBAlertControllerHack|SBUIAdditions)
+ __OBJC_$_PROP_LIST_SBAlertPortalView
+ __OBJC_CLASS_RO_$_SBAlertPortalView
+ __OBJC_METACLASS_RO_$_SBAlertPortalView
+ ___40-[_SBAlertController viewWillDisappear:]_block_invoke
+ ___40-[_SBAlertController viewWillDisappear:]_block_invoke_2
+ ___66-[_SBAlertController viewDidMoveToWindow:shouldAppearOrDisappear:]_block_invoke
+ ___66-[_SBAlertController viewDidMoveToWindow:shouldAppearOrDisappear:]_block_invoke.43
+ ___66-[_SBAlertController viewDidMoveToWindow:shouldAppearOrDisappear:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e56_v16?0"<UIViewControllerTransitionCoordinatorContext>"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e56_v16?0"<UIViewControllerTransitionCoordinatorContext>"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e56_v16?0"<UIViewControllerTransitionCoordinatorContext>"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___kCFBooleanFalse
+ _kCAFilterGaussianBlur
+ _objc_msgSend$_background
+ _objc_msgSend$_setBackground:
+ _objc_msgSend$animateAlongsideTransitionInView:animation:completion:
+ _objc_msgSend$filters
+ _objc_msgSend$initWithVariant:
+ _objc_msgSend$lastObject
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$sb_recursivelyFindAlertControllerSubviewWithGlass
+ _objc_msgSend$setFilters:
+ _objc_msgSend$setHidesSourceLayer:
+ _objc_msgSend$setMatchesOpacity:
+ _objc_msgSend$setMatchesPosition:
+ _objc_msgSend$setSourceLayer:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$setValue:forKeyPath:
+ _objc_msgSend$transitionCoordinator
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UIView_$_SBUIAdditions
- __OBJC_$_CATEGORY_UIView_$_SBUIAdditions
CStrings:
+ "@\"SBAlertPortalView\""
+ "SBAlertControllerHack"
+ "SBAlertPortalView"
+ "T@\"CAPortalLayer\",R,D,N"
+ "_background"
+ "_glassView"
+ "_setBackground:"
+ "animateAlongsideTransitionInView:animation:completion:"
+ "filters"
+ "filters.gaussianBlur.inputRadius"
+ "gaussianBlur"
+ "initWithVariant:"
+ "inputHardEdges"
+ "inputIntermediateBitDepth"
+ "inputNormalizeEdges"
+ "inputQuality"
+ "inputRadius"
+ "lastObject"
+ "mutableCopy"
+ "sb_recursivelyFindAlertControllerSubviewWithGlass"
+ "setFilters:"
+ "setHidesSourceLayer:"
+ "setMatchesOpacity:"
+ "setMatchesPosition:"
+ "setSourceLayer:"
+ "setValue:forKey:"
+ "setValue:forKeyPath:"
+ "transitionCoordinator"
+ "v16@?0@\"<UIViewControllerTransitionCoordinatorContext>\"8"
+ "viewDidMoveToWindow:shouldAppearOrDisappear:"

```
