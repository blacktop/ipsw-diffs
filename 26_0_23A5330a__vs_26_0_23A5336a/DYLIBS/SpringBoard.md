## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4557.0.10.111.0
-  __TEXT.__text: 0xa85708
+4557.0.10.113.0
+  __TEXT.__text: 0xa85c00
   __TEXT.__auth_stubs: 0x5530
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb7a48
+  __TEXT.__objc_methlist: 0xb7a80
   __TEXT.__const: 0x12cf0
   __TEXT.__oslogstring: 0x5e502
   __TEXT.__cstring: 0x7cdcb
   __TEXT.__gcc_except_tab: 0x17898
   __TEXT.__ustring: 0xcac
   __TEXT.__dlopen_cstrs: 0x313
-  __TEXT.__unwind_info: 0x2c0e8
+  __TEXT.__unwind_info: 0x2c0f0
   __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0x220c0
-  __TEXT.__objc_methname: 0x1ceda5
+  __TEXT.__objc_classname: 0x220ef
+  __TEXT.__objc_methname: 0x1cedf8
   __TEXT.__objc_methtype: 0x4c859
   __TEXT.__objc_stubs: 0xf38e0
-  __DATA_CONST.__got: 0xa120
+  __DATA_CONST.__got: 0xa128
   __DATA_CONST.__const: 0x1cca8
-  __DATA_CONST.__objc_classlist: 0x5238
+  __DATA_CONST.__objc_classlist: 0x5240
   __DATA_CONST.__objc_catlist: 0x348
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x2928
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a900
+  __DATA_CONST.__objc_selrefs: 0x4a908
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x3f70
   __DATA_CONST.__objc_arraydata: 0x1850
   __AUTH_CONST.__auth_got: 0x2ab0
   __AUTH_CONST.__const: 0x10978
   __AUTH_CONST.__cfstring: 0x6ee00
-  __AUTH_CONST.__objc_const: 0x269308
+  __AUTH_CONST.__objc_const: 0x2693c0
   __AUTH_CONST.__objc_arrayobj: 0x1770
   __AUTH_CONST.__objc_doubleobj: 0x680
   __AUTH_CONST.__objc_intobj: 0x2bc8
   __AUTH_CONST.__objc_dictobj: 0x320
-  __AUTH.__objc_data: 0x10400
-  __DATA.__objc_ivar: 0xf320
+  __AUTH.__objc_data: 0x10450
+  __DATA.__objc_ivar: 0xf324
   __DATA.__data: 0x1f8b8
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xaa0

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: 29240BCF-63FC-34A5-A4A3-F4DE3DF56786
-  Functions: 70029
-  Symbols:   236776
-  CStrings:  104062
+  UUID: 45B75882-35B2-3C32-9823-58572AE82CC3
+  Functions: 70032
+  Symbols:   236788
+  CStrings:  104065
 
Symbols:
+ +[SBMenuBarAppearanceTransitionBackdropLayerView layerClass]
+ -[SBLockScreenManager coverSheetViewControllerIsTransitioningToSecureApp:]
+ GCC_except_table251
+ GCC_except_table257
+ _OBJC_CLASS_$_SBMenuBarAppearanceTransitionBackdropLayerView
+ _OBJC_IVAR_$_SBLockScreenManager._performingWakeToAppTransition
+ _OBJC_METACLASS_$_SBMenuBarAppearanceTransitionBackdropLayerView
+ __OBJC_$_CLASS_METHODS_SBMenuBarAppearanceTransitionBackdropLayerView
+ __OBJC_CLASS_RO_$_SBMenuBarAppearanceTransitionBackdropLayerView
+ __OBJC_METACLASS_RO_$_SBMenuBarAppearanceTransitionBackdropLayerView
+ ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.85
+ ___74-[SBMenuBarViewController dismissAnimated:alongsideAnimations:completion:]_block_invoke_2
+ ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.81
- GCC_except_table173
- GCC_except_table323
- ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.82
- ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.78
Functions:
~ -[SBFlexibleWindowingHomeGestureSwitcherModifier cornerRadiiForLayoutRole:inAppLayout:withCornerRadii:] : 644 -> 672
+ +[SBMenuBarAppearanceTransitionBackdropLayerView layerClass]
~ -[SBMenuBarViewController dismissAnimated:alongsideAnimations:completion:] : 484 -> 1136
+ ___74-[SBMenuBarViewController dismissAnimated:alongsideAnimations:completion:]_block_invoke_2
~ -[SBMenuBarViewController viewIsAppearing:] : 2108 -> 2556
~ ___43-[SBMenuBarViewController viewIsAppearing:]_block_invoke_2 : 296 -> 304
~ -[SBContinuousExposeHomeGestureSwitcherModifier cornerRadiiForLayoutRole:inAppLayout:withCornerRadii:] : 644 -> 672
+ -[SBLockScreenManager coverSheetViewControllerIsTransitioningToSecureApp:]
~ -[SBLockScreenManager unlockUIFromSource:withOptions:] : 4388 -> 4404
CStrings:
+ "SBMenuBarAppearanceTransitionBackdropLayerView"
+ "_performingWakeToAppTransition"
+ "coverSheetViewControllerIsTransitioningToSecureApp:"

```
