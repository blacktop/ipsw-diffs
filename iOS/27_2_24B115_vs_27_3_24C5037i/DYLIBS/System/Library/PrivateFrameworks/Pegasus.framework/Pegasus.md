## Pegasus

> `/System/Library/PrivateFrameworks/Pegasus.framework/Pegasus`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-311.1.1.0.0
-  __TEXT.__text: 0x42b4c
-  __TEXT.__objc_methlist: 0x469c
-  __TEXT.__const: 0x264
+311.1.2.600.0
+  __TEXT.__text: 0x43d2c
+  __TEXT.__objc_methlist: 0x47f4
+  __TEXT.__const: 0x2e4
   __TEXT.__cstring: 0x47d8
   __TEXT.__oslogstring: 0x1acc
   __TEXT.__gcc_except_tab: 0x500

   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1968
+  __TEXT.__unwind_info: 0x19b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d50
+  __DATA_CONST.__objc_selrefs: 0x2de8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x70
-  __DATA_CONST.__got: 0x488
+  __DATA_CONST.__got: 0x4a8
   __AUTH_CONST.__const: 0x400
   __AUTH_CONST.__cfstring: 0x2f40
-  __AUTH_CONST.__objc_const: 0xae60
+  __AUTH_CONST.__objc_const: 0xb080
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x568
+  __AUTH_CONST.__auth_got: 0x578
   __AUTH.__objc_data: 0xcd0
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x5e8
+  __DATA.__objc_ivar: 0x61c
   __DATA.__data: 0x990
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x460

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1776
-  Symbols:   3187
-  CStrings:  666
+  Functions: 1806
+  Symbols:   3238
+  CStrings:  667
 
Symbols:
+ +[PGControlsViewLayoutMetrics defaultControlsBottomPadding]
+ +[PGControlsViewLayoutMetrics defaultControlsEdgePadding]
+ +[PGPictureInPictureViewController animateViewWithAnimationType:initialSpringVelocity:options:animations:completion:]
+ +[UIView(PGAdditions) PG_animateUsingDefaultDampedSpringWithInitialSpringVelocity:options:animations:completion:]
+ -[PGControlsContainerView _insertSubviewBelowBorder:]
+ -[PGControlsContainerView _newBorderView]
+ -[PGControlsContainerView _updateBorder]
+ -[PGControlsContainerView _updateInterruptionDimmingView]
+ -[PGControlsContainerView cornerRadii]
+ -[PGControlsContainerView gestureRecognizer:shouldReceiveTouch:]
+ -[PGControlsContainerView isControlsSuppressed]
+ -[PGControlsContainerView prefersUniformBorder]
+ -[PGControlsContainerView setControlsSuppressed:]
+ -[PGControlsContainerView setCornerRadii:]
+ -[PGControlsContainerView setPrefersUniformBorder:]
+ -[PGControlsContainerView setUsesVibrantBorder:]
+ -[PGControlsContainerView usesVibrantBorder]
+ -[PGControlsView cornerRadii]
+ -[PGControlsView setCornerRadii:]
+ -[PGPictureInPictureViewController isControlsSuppressed]
+ -[PGPictureInPictureViewController prefersUniformBorder]
+ -[PGPictureInPictureViewController setContentCornerRadii:animated:]
+ -[PGPictureInPictureViewController setControlsSuppressed:]
+ -[PGPictureInPictureViewController setPrefersUniformBorder:]
+ -[PGPictureInPictureViewController setUsesVibrantBorder:]
+ -[PGPictureInPictureViewController usesVibrantBorder]
+ -[PGStashedMaskView _applyResolvedTabCornerRadius]
+ -[PGStashedMaskView _easedMainBodyCornerRadius]
+ -[PGStashedMaskView _resolvedTabCornerRadius]
+ GCC_except_table28
+ GCC_except_table37
+ GCC_except_table43
+ _CACornerRadiiUnset
+ _CGAffineTransformConcat
+ _CGAffineTransformMakeTranslation
+ _OBJC_IVAR_$_PGControlsContainerView._controlsSuppressed
+ _OBJC_IVAR_$_PGControlsContainerView._cornerRadii
+ _OBJC_IVAR_$_PGControlsContainerView._prefersUniformBorder
+ _OBJC_IVAR_$_PGControlsContainerView._uniformBorderView
+ _OBJC_IVAR_$_PGControlsContainerView._usesVibrantBorder
+ _OBJC_IVAR_$_PGControlsContainerView._vibrantBorderView
+ _OBJC_IVAR_$_PGControlsContainerView._wantsInterruptionDimmingView
+ _OBJC_IVAR_$_PGControlsView._cornerRadii
+ _OBJC_IVAR_$_PGPictureInPictureViewController._contentCornerRadii
+ _OBJC_IVAR_$_PGPictureInPictureViewController._controlsSuppressed
+ _OBJC_IVAR_$_PGPictureInPictureViewController._prefersUniformBorder
+ _OBJC_IVAR_$_PGPictureInPictureViewController._usesVibrantBorder
+ _OBJC_IVAR_$_PGStashedMaskView._contentCornerRadius
+ _UIRectCornerRadiiZero
+ ___113+[UIView(PGAdditions) PG_animateUsingDefaultDampedSpringWithInitialSpringVelocity:options:animations:completion:]_block_invoke
+ ___117+[PGPictureInPictureViewController animateViewWithAnimationType:initialSpringVelocity:options:animations:completion:]_block_invoke
+ ___117+[PGPictureInPictureViewController animateViewWithAnimationType:initialSpringVelocity:options:animations:completion:]_block_invoke_2
+ ___40-[PGControlsContainerView _updateBorder]_block_invoke
+ ___67-[PGPictureInPictureViewController setContentCornerRadii:animated:]_block_invoke
+ _kCAFilterInputColorMatrix
+ _kCAFilterVibrantColorMatrix
- +[PGControlsViewLayoutMetrics concentricCornerRadiusForViewSize:]
- GCC_except_table33
- ___105+[UIView(PGAdditions) PG_animateUsingDefaultDampedSpringWithInitialSpringVelocity:animations:completion:]_block_invoke
- ___109+[PGPictureInPictureViewController animateViewWithAnimationType:initialSpringVelocity:animations:completion:]_block_invoke
- ___109+[PGPictureInPictureViewController animateViewWithAnimationType:initialSpringVelocity:animations:completion:]_block_invoke_2
CStrings:
+ "#\xf0\x91"
+ "("
+ "\xa1"
- "#\xd1"
- "\x91"
```
