## PosterBoardUIServices

> `/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices`

```diff

-140.26.102.0.0
-  __TEXT.__text: 0x193d0
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0x13b4
+140.39.0.0.0
+  __TEXT.__text: 0x1a49c
+  __TEXT.__auth_stubs: 0x760
+  __TEXT.__objc_methlist: 0x1474
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x115e
+  __TEXT.__cstring: 0x11a0
   __TEXT.__gcc_except_tab: 0x1e0
-  __TEXT.__oslogstring: 0x111c
+  __TEXT.__oslogstring: 0x111b
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x650
-  __TEXT.__objc_classname: 0x545
-  __TEXT.__objc_methname: 0x5eb1
-  __TEXT.__objc_methtype: 0x1157
-  __TEXT.__objc_stubs: 0x43c0
+  __TEXT.__unwind_info: 0x684
+  __TEXT.__objc_classname: 0x575
+  __TEXT.__objc_methname: 0x61e3
+  __TEXT.__objc_methtype: 0x11f6
+  __TEXT.__objc_stubs: 0x4600
   __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x818
-  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__const: 0x800
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3eb8
-  __DATA_CONST.__objc_selrefs: 0x1500
-  __AUTH_CONST.__cfstring: 0xe60
-  __AUTH_CONST.__objc_const: 0xa00
+  __DATA_CONST.__objc_const: 0x40e0
+  __DATA_CONST.__objc_selrefs: 0x15b0
+  __AUTH_CONST.__cfstring: 0xe80
+  __AUTH_CONST.__objc_const: 0xa48
   __AUTH_CONST.__const: 0x2a0
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0x3a8
-  __AUTH.__objc_data: 0x780
+  __AUTH_CONST.__auth_got: 0x3c0
+  __AUTH.__objc_data: 0x7d0
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x308
+  __DATA.__objc_classrefs: 0x320
   __DATA.__objc_superrefs: 0x90
-  __DATA.__objc_ivar: 0x23c
+  __DATA.__objc_ivar: 0x268
   __DATA.__data: 0x6a8
   __DATA.__bss: 0x108
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 611
-  Symbols:   2562
-  CStrings:  1386
+  Functions: 627
+  Symbols:   2634
+  CStrings:  1424
 
Symbols:
+ -[PRUISPosterAppearanceObservingAttachmentProvider _currentAppearance]
+ -[PRUISPosterAppearanceObservingAttachmentProvider _currentAppearance].cold.1
+ -[PRUISPosterAppearanceObservingAttachmentProvider _currentAppearance].cold.2
+ -[PRUISPosterAppearanceObservingAttachmentProvider _currentAppearance].cold.3
+ -[PRUISPosterAppearanceObservingAttachmentProvider _updateContentStyleWithTitleStyleConfiguration:initialAppearance:]
+ -[PRUISPosterAppearanceObservingAttachmentProvider obscurableOverlayView]
+ -[PRUISPosterAppearanceObservingAttachmentProvider primaryContentTightFrame]
+ -[PRUISPosterAppearanceObservingAttachmentProvider setPrimaryContentTightFrame:]
+ -[PRUISPosterAppearanceObservingAttachmentProvider updateLayoutForChangedObscuredSubviewBounds]
+ -[PRUISPosterContentViewCoordinator .cxx_destruct]
+ -[PRUISPosterContentViewCoordinator obscurableContentView]
+ -[PRUISPosterContentViewCoordinator obscurableOverlayView]
+ -[PRUISPosterContentViewCoordinator overlayContentView]
+ -[PRUISPosterContentViewCoordinator primaryContentTightFrame]
+ -[PRUISPosterContentViewCoordinator setObscurableOverlayView:]
+ -[PRUISPosterContentViewCoordinator setPrimaryContentTightFrame:]
+ -[PRUISPosterContentViewCoordinator updateContentViewsWithContentStyle:initialAppearance:]
+ -[PRUISPosterContentViewCoordinator updateLayoutForChangedVibrantObscuredSubviewBounds]
+ -[PRUISPosterContentViewCoordinator vibrantObscurableContentView]
+ -[PRUISPosterRenderingViewController _currentAppearance]
+ -[PRUISPosterRenderingViewController _currentAppearance].cold.1
+ -[PRUISPosterRenderingViewController _currentAppearance].cold.2
+ -[PRUISPosterRenderingViewController _isSceneContentReady]
+ -[PRUISPosterRenderingViewController _obscurableContentView]
+ -[PRUISPosterRenderingViewController _serverPath]
+ -[PRUISPosterRenderingViewController _setContentHidden:animated:completion:]
+ -[PRUISPosterRenderingViewController _setContentHidden:animationSettings:completion:]
+ -[PRUISPosterRenderingViewController _updateContentStyleWithAppearance:]
+ -[PRUISPosterRenderingViewController contentViewCoordinator]
+ -[PRUISPosterRenderingViewController updateLayoutForChangedObscuredSubviewBounds]
+ -[PRUISPosterRenderingViewController(Deprecated) _beginExecutingSnapshotsIfNeeded]
+ -[PRUISPosterRenderingViewController(Deprecated) _cachedImageForRequest:]
+ -[PRUISPosterRenderingViewController(Deprecated) _cachedImageForRequest:].cold.1
+ -[PRUISPosterRenderingViewController(Deprecated) _levelSetForSnapshotOptions:]
+ -[PRUISPosterRenderingViewController(Deprecated) _processNextSnapshot]
+ -[PRUISPosterRenderingViewController(Deprecated) _snapshotRequestForOptions:screen:levelSet:]
+ -[PRUISPosterRenderingViewController(Deprecated) obscurableContentView]
+ -[PRUISPosterRenderingViewController(Deprecated) snapshotWithOptions:]
+ -[PRUISPosterRenderingViewController(Deprecated) snapshotWithOptions:forScreen:completionBlock:]
+ GCC_except_table38
+ _CGRectEqualToRect
+ _CGRectIsEmpty
+ _CGRectUnion
+ _OBJC_CLASS_$_NSLayoutConstraint
+ _OBJC_CLASS_$_PRPosterContentStyleVibrantContentRenderer
+ _OBJC_CLASS_$_PRUISPosterContentViewCoordinator
+ _OBJC_IVAR_$_PRUISPosterAppearanceObservingAttachmentProvider._currentAppearance
+ _OBJC_IVAR_$_PRUISPosterAppearanceObservingAttachmentProvider._obscurableOverlayView
+ _OBJC_IVAR_$_PRUISPosterAppearanceObservingAttachmentProvider._primaryContentTightFrame
+ _OBJC_IVAR_$_PRUISPosterAppearanceObservingAttachmentProvider._vibrantContentRenderer
+ _OBJC_IVAR_$_PRUISPosterContentViewCoordinator._currentStyle
+ _OBJC_IVAR_$_PRUISPosterContentViewCoordinator._obscurableContentContainerView
+ _OBJC_IVAR_$_PRUISPosterContentViewCoordinator._obscurableContentVibrancyView
+ _OBJC_IVAR_$_PRUISPosterContentViewCoordinator._obscurableOverlayView
+ _OBJC_IVAR_$_PRUISPosterContentViewCoordinator._overlayContentView
+ _OBJC_IVAR_$_PRUISPosterContentViewCoordinator._primaryContentTightFrame
+ _OBJC_IVAR_$_PRUISPosterContentViewCoordinator._vibrantContentStyleRenderer
+ _OBJC_IVAR_$_PRUISPosterRenderingViewController._contentStyleRenderer
+ _OBJC_IVAR_$_PRUISPosterRenderingViewController._contentViewCoordinator
+ _OBJC_METACLASS_$_PRUISPosterContentViewCoordinator
+ __OBJC_$_INSTANCE_METHODS_PRUISPosterContentViewCoordinator
+ __OBJC_$_INSTANCE_METHODS_PRUISPosterRenderingViewController(Deprecated)
+ __OBJC_$_INSTANCE_VARIABLES_PRUISPosterContentViewCoordinator
+ __OBJC_$_PROP_LIST_PRUISPosterContentViewCoordinator
+ __OBJC_CLASS_RO_$_PRUISPosterContentViewCoordinator
+ __OBJC_METACLASS_RO_$_PRUISPosterContentViewCoordinator
+ ___70-[PRUISPosterRenderingViewController(Deprecated) _processNextSnapshot]_block_invoke
+ ___70-[PRUISPosterRenderingViewController(Deprecated) _processNextSnapshot]_block_invoke_2
+ ___85-[PRUISPosterRenderingViewController _setContentHidden:animationSettings:completion:]_block_invoke
+ ___block_literal_global.79
+ _objc_msgSend$_currentAppearance
+ _objc_msgSend$_isSceneContentReady
+ _objc_msgSend$_obscurableContentView
+ _objc_msgSend$_serverPath
+ _objc_msgSend$_setContentHidden:animated:completion:
+ _objc_msgSend$_setContentHidden:animationSettings:completion:
+ _objc_msgSend$_updateContentStyleWithAppearance:
+ _objc_msgSend$_updateContentStyleWithTitleStyleConfiguration:initialAppearance:
+ _objc_msgSend$activateConstraints:
+ _objc_msgSend$applyStyleWithRenderer:
+ _objc_msgSend$centerXAnchor
+ _objc_msgSend$centerYAnchor
+ _objc_msgSend$clearAllStyles
+ _objc_msgSend$constraintEqualToAnchor:
+ _objc_msgSend$contentViewCoordinator
+ _objc_msgSend$currentAppearance
+ _objc_msgSend$effectiveTitleContentStyle
+ _objc_msgSend$frame
+ _objc_msgSend$heightAnchor
+ _objc_msgSend$initWithVibrancyView:contentView:contentBoundingRect:styleBoundingRect:initialAppearance:
+ _objc_msgSend$layoutIfNeeded
+ _objc_msgSend$setContentBoundingRect:
+ _objc_msgSend$setNeedsLayout
+ _objc_msgSend$setStyleBoundingRect:
+ _objc_msgSend$subviews
+ _objc_msgSend$updateContentViewsWithContentStyle:initialAppearance:
+ _objc_msgSend$updateLayoutForChangedVibrantObscuredSubviewBounds
+ _objc_msgSend$vibrantObscurableContentView
+ _objc_msgSend$widthAnchor
- -[PRUISPosterAppearanceObservingAttachmentProvider _updateVibrancyConfigurationWithTitleStyleConfiguration:]
- -[PRUISPosterAppearanceObservingAttachmentProvider applyPosterAppearanceToObserver:].cold.1
- -[PRUISPosterAppearanceObservingAttachmentProvider applyPosterAppearanceToObserver:].cold.2
- -[PRUISPosterAppearanceObservingAttachmentProvider applyPosterAppearanceToObserver:].cold.3
- -[PRUISPosterRenderingViewController _beginExecutingSnapshotsIfNeeded]
- -[PRUISPosterRenderingViewController _cachedImageForRequest:]
- -[PRUISPosterRenderingViewController _cachedImageForRequest:].cold.1
- -[PRUISPosterRenderingViewController _createContentViewsIfNeeded]
- -[PRUISPosterRenderingViewController _createVibrancyEffectViewIfNeeded]
- -[PRUISPosterRenderingViewController _levelSetForSnapshotOptions:]
- -[PRUISPosterRenderingViewController _processNextSnapshot]
- -[PRUISPosterRenderingViewController _snapshotRequestForOptions:screen:levelSet:]
- -[PRUISPosterRenderingViewController _updateVibrancyConfiguration]
- -[PRUISPosterRenderingViewController isSceneContentReady]
- -[PRUISPosterRenderingViewController obscurableContentView]
- -[PRUISPosterRenderingViewController registerPosterAppearanceObserver:].cold.1
- -[PRUISPosterRenderingViewController registerPosterAppearanceObserver:].cold.2
- -[PRUISPosterRenderingViewController rotateToInterfaceOrientation:duration:]
- -[PRUISPosterRenderingViewController serverPath]
- -[PRUISPosterRenderingViewController setContentHidden:animated:completion:]
- -[PRUISPosterRenderingViewController setContentHidden:animationSettings:completion:]
- -[PRUISPosterRenderingViewController snapshotWithOptions:]
- -[PRUISPosterRenderingViewController snapshotWithOptions:forScreen:completionBlock:]
- GCC_except_table29
- GCC_except_table47
- _OBJC_IVAR_$_PRUISPosterRenderingViewController._behindFloatingContentView
- _OBJC_IVAR_$_PRUISPosterRenderingViewController._vibrancyEffectView
- __OBJC_$_INSTANCE_METHODS_PRUISPosterRenderingViewController
- __OBJC_$_PROP_LIST_PRUISPosterRenderingViewController
- ___58-[PRUISPosterRenderingViewController _processNextSnapshot]_block_invoke
- ___58-[PRUISPosterRenderingViewController _processNextSnapshot]_block_invoke_2
- ___84-[PRUISPosterRenderingViewController setContentHidden:animationSettings:completion:]_block_invoke
- ___block_literal_global.93
- _objc_msgSend$_createContentViewsIfNeeded
- _objc_msgSend$_createVibrancyEffectViewIfNeeded
- _objc_msgSend$_updateVibrancyConfiguration
- _objc_msgSend$_updateVibrancyConfigurationWithTitleStyleConfiguration:
- _objc_msgSend$isSceneContentReady
- _objc_msgSend$serverPath
- _objc_msgSend$setConfiguration:
- _objc_msgSend$setContentHidden:animated:completion:
- _objc_msgSend$setContentHidden:animationSettings:completion:
- _objc_msgSend$setShouldAcquireRuntimeAssertions:
- _objc_msgSend$vibrancyConfiguration
CStrings:
+ "\x01'\x11\x11\x13\""
+ "\x06"
+ "\b"
+ "@\"<PRPosterContentStyle>\""
+ "@\"PRPosterAppearance\""
+ "@\"PRPosterContentStyleVibrantContentRenderer\""
+ "@\"PRUISPosterContentViewCoordinator\""
+ "DECAF000-0000-0000-0000-000000000002"
+ "DECAF000-0000-0000-0000-000000000003"
+ "Deprecated"
+ "Found precachable url %{public}@"
+ "PRUISPosterContentViewCoordinator"
+ "T@\"PRUISPosterContentViewCoordinator\",R,N"
+ "T@\"UIView\",&,N,V_obscurableOverlayView"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_primaryContentTightFrame"
+ "_contentStyleRenderer"
+ "_contentViewCoordinator"
+ "_currentAppearance"
+ "_currentStyle"
+ "_isSceneContentReady"
+ "_obscurableContentView"
+ "_obscurableOverlayView"
+ "_primaryContentTightFrame"
+ "_serverPath"
+ "_setContentHidden:animated:completion:"
+ "_setContentHidden:animationSettings:completion:"
+ "_updateContentStyleWithAppearance:"
+ "_updateContentStyleWithTitleStyleConfiguration:initialAppearance:"
+ "_vibrantContentRenderer"
+ "_vibrantContentStyleRenderer"
+ "activateConstraints:"
+ "applyStyleWithRenderer:"
+ "centerXAnchor"
+ "centerYAnchor"
+ "clearAllStyles"
+ "constraintEqualToAnchor:"
+ "contentViewCoordinator"
+ "currentAppearance"
+ "effectiveTitleContentStyle"
+ "frame"
+ "heightAnchor"
+ "initWithVibrancyView:contentView:contentBoundingRect:styleBoundingRect:initialAppearance:"
+ "layoutIfNeeded"
+ "obscurableOverlayView"
+ "primaryContentTightFrame"
+ "setContentBoundingRect:"
+ "setNeedsLayout"
+ "setObscurableOverlayView:"
+ "setPrimaryContentTightFrame:"
+ "setStyleBoundingRect:"
+ "subviews"
+ "updateContentViewsWithContentStyle:initialAppearance:"
+ "updateLayoutForChangedObscuredSubviewBounds"
+ "updateLayoutForChangedVibrantObscuredSubviewBounds"
+ "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "widthAnchor"
+ "\xf0A"
- "\x01'\x12\x13\""
- "\x05"
- "Found precachable url %@{public}@"
- "_behindFloatingContentView"
- "_createContentViewsIfNeeded"
- "_createVibrancyEffectViewIfNeeded"
- "_updateVibrancyConfiguration"
- "_updateVibrancyConfigurationWithTitleStyleConfiguration:"
- "_vibrancyEffectView"
- "isSceneContentReady"
- "rotateToInterfaceOrientation:duration:"
- "serverPath"
- "setConfiguration:"
- "setContentHidden:animated:completion:"
- "setContentHidden:animationSettings:completion:"
- "setShouldAcquireRuntimeAssertions:"
- "unknown"
- "v32@0:8q16d24"
- "\xf01"

```
