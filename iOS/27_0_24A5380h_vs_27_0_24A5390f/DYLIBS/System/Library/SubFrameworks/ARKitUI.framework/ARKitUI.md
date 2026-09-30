## ARKitUI

> `/System/Library/SubFrameworks/ARKitUI.framework/ARKitUI`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-781.0.1.0.4
-  __TEXT.__text: 0x2a2f8
-  __TEXT.__objc_methlist: 0x2888
-  __TEXT.__const: 0x958
-  __TEXT.__oslogstring: 0x1917
-  __TEXT.__cstring: 0xdb6
-  __TEXT.__gcc_except_tab: 0xcf8
-  __TEXT.__unwind_info: 0xc08
+781.0.4.0.0
+  __TEXT.__text: 0x2b150
+  __TEXT.__objc_methlist: 0x2910
+  __TEXT.__const: 0x948
+  __TEXT.__oslogstring: 0x18d2
+  __TEXT.__cstring: 0xdb4
+  __TEXT.__gcc_except_tab: 0xcd8
+  __TEXT.__unwind_info: 0xc10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x380
+  __DATA_CONST.__const: 0x330
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2178
+  __DATA_CONST.__objc_selrefs: 0x2248
   __DATA_CONST.__objc_superrefs: 0x138
-  __DATA_CONST.__got: 0x570
-  __AUTH_CONST.__const: 0x3c0
-  __AUTH_CONST.__cfstring: 0xc00
-  __AUTH_CONST.__objc_const: 0x7410
+  __DATA_CONST.__got: 0x590
+  __AUTH_CONST.__const: 0x3a0
+  __AUTH_CONST.__cfstring: 0xc20
+  __AUTH_CONST.__objc_const: 0x75c8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x10e0
-  __DATA.__objc_ivar: 0x558
+  __DATA.__objc_ivar: 0x588
   __DATA.__data: 0x380
-  __DATA.__bss: 0x250
+  __DATA.__bss: 0x240
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 969
-  Symbols:   2991
-  CStrings:  235
+  Functions: 972
+  Symbols:   3032
+  CStrings:  234
 
Symbols:
+ -[ARSCNCompositor setViewRotationAngle:]
+ -[ARSCNCompositor viewRotationAngle]
+ -[ARSCNView _applyPreviewRotationFromAngle:hasOldAngle:toAngle:]
+ -[ARSCNView _assignViewLayerToSessionOnMainThread]
+ -[ARSCNView _assignViewLayerToSession]
+ -[ARSCNView _drawAtTime:]
+ -[ARSCNView _installSnapshotIfNeeded]
+ -[ARSCNView _pollResumeAfterDrawableResize]
+ -[ARSCNView _publishOrientationSwapAtAngle:fromAngle:]
+ -[ARSCNView _renderCapturedPixelBuffer:withOrientation:]
+ -[ARSCNView _setupRenderSublayer]
+ -[ARSCNView _updateCamera:withViewRotationAngle:viewportSize:]
+ -[ARSCNView _viewRotationAngleDidChange:]
+ -[ARSCNView _windowWillRotate:]
+ -[ARSCNView safeAreaInsetsDidChange]
+ -[ARSCNView session:didChangeViewRotationAngle:]
+ -[ARSKView _setLayerOnMain]
+ -[ARSKView _updateNode:forAnchor:projectionMatrix:camera:viewRotationAngle:]
+ -[ARSKView session:didChangeViewRotationAngle:]
+ _ARCameraImageToViewTransformWithAngle
+ _ARCorrectedViewRotationAngleForRotation
+ _ARDisplayRotationFromViewRotationAngle
+ _ARInterfaceOrientationFromViewRotationAngle
+ _ARViewToCameraImageTransformWithAngle
+ _CATransform3DMakeRotation
+ _CGPointZero
+ _NSRunLoopCommonModes
+ _OBJC_CLASS_$_CABasicAnimation
+ _OBJC_CLASS_$_CAMediaTimingFunction
+ _OBJC_CLASS_$_NSThread
+ _OBJC_IVAR_$_ARSCNCompositor._viewRotationAngle
+ _OBJC_IVAR_$_ARSCNView._baselineBounds
+ _OBJC_IVAR_$_ARSCNView._hasBaselineBounds
+ _OBJC_IVAR_$_ARSCNView._pendingNewOrientation
+ _OBJC_IVAR_$_ARSCNView._pendingResumeDrawableSize
+ _OBJC_IVAR_$_ARSCNView._pendingResumeMetalLayer
+ _OBJC_IVAR_$_ARSCNView._pendingResumeStage
+ _OBJC_IVAR_$_ARSCNView._pendingResumeStage0TicksRemaining
+ _OBJC_IVAR_$_ARSCNView._pendingResumeStage1TicksRemaining
+ _OBJC_IVAR_$_ARSCNView._pendingRotationBaselineSize
+ _OBJC_IVAR_$_ARSCNView._renderTargetLock
+ _OBJC_IVAR_$_ARSCNView._renderTargetOrientation
+ _OBJC_IVAR_$_ARSCNView._renderTargetViewAngle
+ _OBJC_IVAR_$_ARSCNView._renderTicksAtSuspendClear
+ _OBJC_IVAR_$_ARSCNView._rendererFrameCounter
+ _OBJC_IVAR_$_ARSCNView._resumePoller
+ _OBJC_IVAR_$_ARSCNView._viewRotationAngle
+ ___27-[ARSKView _setLayerOnMain]_block_invoke
+ ___38-[ARSCNView _assignViewLayerToSession]_block_invoke
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ _kCAMediaTimingFunctionEaseInEaseOut
+ _objc_msgSend$_applyPreviewRotationFromAngle:hasOldAngle:toAngle:
+ _objc_msgSend$_assignViewLayerToSession
+ _objc_msgSend$_assignViewLayerToSessionOnMainThread
+ _objc_msgSend$_installSnapshotIfNeeded
+ _objc_msgSend$_publishOrientationSwapAtAngle:fromAngle:
+ _objc_msgSend$_renderCapturedPixelBuffer:withOrientation:
+ _objc_msgSend$_setLayerOnMain
+ _objc_msgSend$_setupRenderSublayer
+ _objc_msgSend$_updateCamera:withViewRotationAngle:viewportSize:
+ _objc_msgSend$_updateNode:forAnchor:projectionMatrix:camera:viewRotationAngle:
+ _objc_msgSend$_viewRotationAngleDidChange:
+ _objc_msgSend$addAnimation:forKey:
+ _objc_msgSend$animationWithKeyPath:
+ _objc_msgSend$begin
+ _objc_msgSend$colorspace
+ _objc_msgSend$constraintEqualToConstant:
+ _objc_msgSend$drawableSize
+ _objc_msgSend$flush
+ _objc_msgSend$framebufferOnly
+ _objc_msgSend$functionWithName:
+ _objc_msgSend$heightAnchor
+ _objc_msgSend$isMainThread
+ _objc_msgSend$maximumDrawableCount
+ _objc_msgSend$projectionMatrixForViewRotationAngle:viewportSize:zNear:zFar:
+ _objc_msgSend$scn_backingLayer
+ _objc_msgSend$scn_setBackingLayer:
+ _objc_msgSend$session:didChangeViewRotationAngle:
+ _objc_msgSend$setAnchorPoint:
+ _objc_msgSend$setColorspace:
+ _objc_msgSend$setFramebufferOnly:
+ _objc_msgSend$setFromValue:
+ _objc_msgSend$setMaximumDrawableCount:
+ _objc_msgSend$setTimingFunction:
+ _objc_msgSend$setToValue:
+ _objc_msgSend$setViewLayer:
+ _objc_msgSend$setViewRotationAngle:
+ _objc_msgSend$translatesAutoresizingMaskIntoConstraints
+ _objc_msgSend$unprojectPoint:ontoPlaneWithTransform:viewRotationAngle:viewportSize:
+ _objc_msgSend$valueWithCATransform3D:
+ _objc_msgSend$viewRotationAngle
+ _objc_msgSend$widthAnchor
+ _os_unfair_lock_assert_owner
- -[ARSCNCompositor currentOrientation]
- -[ARSCNCompositor setCurrentOrientation:]
- -[ARSCNView cleanupLingeringRotationState]
- -[ARSCNView frameToRemoveRotationSnapshotOn]
- -[ARSCNView setFrameToRemoveRotationSnapshotOn:]
- -[ARSCNView windowDidRotateNotification:]
- -[ARSCNView windowWillAnimateRotateNotification:]
- -[ARSCNView windowWillRotateNotification:]
- -[ARSKView _updateNode:forAnchor:projectionMatrix:camera:orientation:]
- GCC_except_table22
- _ARCameraImageToViewTransform
- _ARCameraToDisplayRotation
- _ARViewToCameraImageTransform
- _CGAffineTransformIdentity
- _CGAffineTransformIsIdentity
- _NSStringFromUIInterfaceOrientation
- _OBJC_CLASS_$_NSBundle
- _OBJC_IVAR_$_ARSCNCompositor._currentOrientation
- _OBJC_IVAR_$_ARSCNView._frameToRemoveRotationSnapshotOn
- _OBJC_IVAR_$_ARSCNView._interfaceOrientation
- _OBJC_IVAR_$_ARSCNView._lastInterfaceOrientation
- _OBJC_IVAR_$_ARSKView._interfaceOrientation
- ___28-[ARSCNView didMoveToWindow]_block_invoke
- ___36-[ARSCNView _renderer:updateAtTime:]_block_invoke
- ___42-[ARSCNView cleanupLingeringRotationState]_block_invoke
- ___42-[ARSCNView windowWillRotateNotification:]_block_invoke
- ___42-[ARSCNView windowWillRotateNotification:]_block_invoke_2
- ___49-[ARSCNView windowWillAnimateRotateNotification:]_block_invoke
- ___49-[ARSCNView windowWillAnimateRotateNotification:]_block_invoke_2
- ___block_descriptor_40_e8_32s_e8_v12?0B8ls32l8
- ___block_descriptor_48_ea8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_56_e8_32s_e5_v8?0ls32l8
- __alwaysRotateCounterclockwise
- _didMoveToWindow.onceToken
- _objc_msgSend$_renderCapturedPixelBuffer:
- _objc_msgSend$_updateBackingSize
- _objc_msgSend$_updateNode:forAnchor:projectionMatrix:camera:orientation:
- _objc_msgSend$animateWithDuration:delay:options:animations:completion:
- _objc_msgSend$boolValue
- _objc_msgSend$cleanupLingeringRotationState
- _objc_msgSend$compositor
- _objc_msgSend$frameToRemoveRotationSnapshotOn
- _objc_msgSend$mainBundle
- _objc_msgSend$object
- _objc_msgSend$objectForInfoDictionaryKey:
- _objc_msgSend$objectForKey:
- _objc_msgSend$performWithoutAnimation:
- _objc_msgSend$projectionMatrixForOrientation:viewportSize:zNear:zFar:
- _objc_msgSend$setCurrentOrientation:
- _objc_msgSend$setFrameToRemoveRotationSnapshotOn:
- _objc_msgSend$unprojectPoint:ontoPlaneWithTransform:orientation:viewportSize:
- _objc_msgSend$userInterfaceIdiom
CStrings:
+ "%{public}@ <%p>: Layout changed to %{public}@, %.2fx"
+ "%{public}@ <%p>: [ARSKView] Layout changed to %{public}@, viewRotationAngle=%g°"
+ "%{public}@ <%p>: viewRotationAngle updated to %.0f"
+ "counterRotation"
+ "transform"
+ "viewRotationAngle updated to %.0f"
- "%{public}@ <%p>: ARSCNViewRotationSnapshotStateSetUp"
- "%{public}@ <%p>: ARSCNViewRotationSnapshotStateSettingUp"
- "%{public}@ <%p>: Layout changed to %{public}@, %.2fx, %{public}@"
- "%{public}@ <%p>: Removing rotation snapshot"
- "%{public}@ <%p>: [ARSKView] Layout changed to %{public}@, %{public}@"
- "UIRequiresFullScreen"
- "v12@?0B8"
```
