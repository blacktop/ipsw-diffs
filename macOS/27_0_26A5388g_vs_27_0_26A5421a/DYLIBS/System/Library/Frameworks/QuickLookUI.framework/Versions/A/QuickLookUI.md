## QuickLookUI

> `/System/Library/Frameworks/QuickLookUI.framework/Versions/A/QuickLookUI`

```diff

-1113.0.0.0.0
-  __TEXT.__text: 0xcda70
-  __TEXT.__objc_methlist: 0x10850
-  __TEXT.__gcc_except_tab: 0x10a8
-  __TEXT.__const: 0xf04
-  __TEXT.__cstring: 0x7986
-  __TEXT.__oslogstring: 0x3981
+1114.0.0.0.0
+  __TEXT.__text: 0xcfcc8
+  __TEXT.__objc_methlist: 0x10d60
+  __TEXT.__gcc_except_tab: 0x10c8
+  __TEXT.__const: 0xf24
+  __TEXT.__cstring: 0x7ac6
+  __TEXT.__oslogstring: 0x39da
   __TEXT.__ustring: 0x26
   __TEXT.__swift5_typeref: 0x390
   __TEXT.__swift5_reflstr: 0xc9

   __TEXT.__swift_as_cont: 0x14
   __TEXT.__swift5_capture: 0x20
   __TEXT.__dof_QLSeamles: 0x8e7
-  __TEXT.__unwind_info: 0x3d70
+  __TEXT.__unwind_info: 0x3e18
   __TEXT.__eh_frame: 0x2b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x570
-  __DATA_CONST.__objc_classlist: 0x678
+  __DATA_CONST.__const: 0x5d8
+  __DATA_CONST.__objc_classlist: 0x690
   __DATA_CONST.__objc_catlist: 0x68
-  __DATA_CONST.__objc_protolist: 0x208
+  __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x83f0
+  __DATA_CONST.__objc_selrefs: 0x8660
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x4a8
+  __DATA_CONST.__objc_superrefs: 0x4b0
   __DATA_CONST.__objc_arraydata: 0x38
-  __DATA_CONST.__got: 0x10c8
-  __AUTH_CONST.__const: 0x2298
-  __AUTH_CONST.__cfstring: 0x7d80
-  __AUTH_CONST.__objc_const: 0x171b8
+  __DATA_CONST.__got: 0x10e8
+  __AUTH_CONST.__const: 0x21f8
+  __AUTH_CONST.__cfstring: 0x7ec0
+  __AUTH_CONST.__objc_const: 0x17950
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x1498
-  __AUTH.__objc_data: 0x39a0
+  __AUTH_CONST.__auth_got: 0x14a8
+  __AUTH.__objc_data: 0x3a90
   __AUTH.__data: 0x128
-  __DATA.__objc_ivar: 0xfa8
-  __DATA.__data: 0x1b78
-  __DATA.__bss: 0x1490
+  __DATA.__objc_ivar: 0x1028
+  __DATA.__data: 0x1b50
+  __DATA.__bss: 0x14a0
   __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0x748
   __DATA_DIRTY.__data: 0x28

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5909
-  Symbols:   13051
-  CStrings:  1553
+  Functions: 6002
+  Symbols:   13271
+  CStrings:  1563
 
Symbols:
+ +[QLSidecarSwipeAnimator elasticProgressFrom:to:initialVelocity:elapsedTime:]
+ +[QLSidecarSwipeAnimator normalizedInitialVelocity:viewWidth:forwardSwipe:]
+ +[QLSidecarSwipeAnimator swipeSucceededWithProgress:velocity:viewWidth:]
+ -[QLBackgroundGestureHostView acceptsFirstMouse:]
+ -[QLFullscreenController _controlsInteractionDidBegin]
+ -[QLFullscreenController _controlsInteractionDidEnd]
+ -[QLFullscreenController backgroundClickRecognizer]
+ -[QLFullscreenController backgroundSidecarSwipeRecognizer]
+ -[QLFullscreenController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:]
+ -[QLFullscreenController setBackgroundClickRecognizer:]
+ -[QLFullscreenController setBackgroundSidecarSwipeRecognizer:]
+ -[QLFullscreenController setSidecarSwipeRecognizer:]
+ -[QLFullscreenController sidecarSwipeRecognizer]
+ -[QLFullscreenWindow _isNonactivatingPanel]
+ -[QLPreviewDocument beginControlsInteraction]
+ -[QLPreviewDocument endControlsInteraction]
+ -[QLPreviewPanelController _canSwipe]
+ -[QLPreviewPanelController _containingView]
+ -[QLPreviewPanelController _continueForwardedSwipeWithEvent:]
+ -[QLPreviewPanelController _endForwardedSwipe]
+ -[QLPreviewPanelController _handleForwardedSwipeScrollEvent:]
+ -[QLPreviewPanelController _isSidecarSwipeGestureRecognizer:]
+ -[QLPreviewPanelController _runSidecarSwipeWithState:translation:velocity:]
+ -[QLPreviewPanelController _setupGestures]
+ -[QLPreviewPanelController _swipeBegin]
+ -[QLPreviewPanelController forwardedSwipeFilter]
+ -[QLPreviewPanelController forwardedSwipeInProgress]
+ -[QLPreviewPanelController forwardedSwipeMonitor]
+ -[QLPreviewPanelController gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:]
+ -[QLPreviewPanelController gestureRecognizer:shouldRequireFailureOfGestureRecognizer:]
+ -[QLPreviewPanelController gestureRecognizerShouldBegin:]
+ -[QLPreviewPanelController newSidecarSwipeGestureRecognizer]
+ -[QLPreviewPanelController panWithGesture:]
+ -[QLPreviewPanelController previewSwipeController:didEndWithDeltaIndex:isComplete:]
+ -[QLPreviewPanelController previewSwipeController:previewFrameWithPreviewView:]
+ -[QLPreviewPanelController previewSwipeController:previewItemWithDeltaIndex:shouldLoad:]
+ -[QLPreviewPanelController previewSwipeController:progress:]
+ -[QLPreviewPanelController setForwardedSwipeFilter:]
+ -[QLPreviewPanelController setForwardedSwipeInProgress:]
+ -[QLPreviewPanelController setForwardedSwipeMonitor:]
+ -[QLPreviewPanelController setSidecarSwipeGestureRecognizer:]
+ -[QLPreviewPanelController sidecarSwipeGestureRecognizer]
+ -[QLPreviewSwipeController _animateProgress]
+ -[QLPreviewSwipeController _fire]
+ -[QLPreviewSwipeController animateFromValue]
+ -[QLPreviewSwipeController animateInitialVelocity]
+ -[QLPreviewSwipeController animateToValue]
+ -[QLPreviewSwipeController animationDisplayLink]
+ -[QLPreviewSwipeController animationTimerStartDate]
+ -[QLPreviewSwipeController delegate]
+ -[QLPreviewSwipeController setAnimateFromValue:]
+ -[QLPreviewSwipeController setAnimateInitialVelocity:]
+ -[QLPreviewSwipeController setAnimateToValue:]
+ -[QLPreviewSwipeController setAnimationDisplayLink:]
+ -[QLPreviewSwipeController setAnimationTimerStartDate:]
+ -[QLPreviewSwipeController setDelegate:]
+ -[QLPreviewSwipeController swipeAnimateToEndWithState:velocity:viewWidth:progress:]
+ -[QLPreviewSwipeController swipeBeginWithScrollingDeltaX:containingView:swipeUseOpaqueWindow:]
+ -[QLPreviewSwipeController swipeWithEvent:containingView:options:]
+ -[QLPreviewSwipeController swipeWithPhase:progress:isComplete:]
+ -[QLRemoteViewController beginControlsInteraction]
+ -[QLRemoteViewController beginForwardedSidecarSwipe]
+ -[QLRemoteViewController endControlsInteraction]
+ -[QLRemoteViewController endForwardedSidecarSwipe]
+ -[QLSidecarSwipeSampleFilter addSample:]
+ -[QLSidecarSwipeSampleFilter initWithInitialPosition:]
+ -[QLSidecarSwipeSampleFilter isEnabled]
+ -[QLSidecarSwipeSampleFilter position]
+ -[QLSidecarSwipeSampleFilter setEnabled:]
+ -[QLUIServiceBaseDisplayBundle beginControlsInteraction]
+ -[QLUIServiceBaseDisplayBundle beginForwardedSidecarSwipe]
+ -[QLUIServiceBaseDisplayBundle endControlsInteraction]
+ -[QLUIServiceBaseDisplayBundle endForwardedSidecarSwipe]
+ -[QLUIServiceBaseDisplayBundle forwardedSidecarSwipeActive]
+ -[QLUIServiceBaseDisplayBundle setForwardedSidecarSwipeActive:]
+ -[QLUIServiceBaseViewController _forwardSidecarSwipeToHostWithState:translation:modifiers:]
+ -[QLUIServiceBaseViewController _pageContentForSidecarSwipeState:translation:]
+ -[QLUIServiceBaseViewController beginControlsInteraction]
+ -[QLUIServiceBaseViewController endControlsInteraction]
+ -[QLUIServiceBaseViewController gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:]
+ -[QLUIServiceBaseViewController receivedSidecarSwipeGesture:]
+ -[QLUIServiceBaseViewController setSidecarSwipeAxisLocked:]
+ -[QLUIServiceBaseViewController setSidecarSwipeDidPage:]
+ -[QLUIServiceBaseViewController setSidecarSwipeForwardingStarted:]
+ -[QLUIServiceBaseViewController setSidecarSwipeMessage:]
+ -[QLUIServiceBaseViewController setSidecarSwipePaging:]
+ -[QLUIServiceBaseViewController setSidecarSwipeRecognizer:]
+ -[QLUIServiceBaseViewController sidecarSwipeAxisLocked]
+ -[QLUIServiceBaseViewController sidecarSwipeContentCanPage]
+ -[QLUIServiceBaseViewController sidecarSwipeContentPageByDelta:]
+ -[QLUIServiceBaseViewController sidecarSwipeDidPage]
+ -[QLUIServiceBaseViewController sidecarSwipeForwardingStarted]
+ -[QLUIServiceBaseViewController sidecarSwipeMessage]
+ -[QLUIServiceBaseViewController sidecarSwipePaging]
+ -[QLUIServiceBaseViewController sidecarSwipeRecognizer]
+ GCC_except_table108
+ GCC_except_table269
+ OBJC_IVAR_$_QLFullscreenController._backgroundClickRecognizer
+ OBJC_IVAR_$_QLFullscreenController._backgroundSidecarSwipeRecognizer
+ OBJC_IVAR_$_QLFullscreenController._controlsInteractionCount
+ OBJC_IVAR_$_QLFullscreenController._sidecarSwipeRecognizer
+ OBJC_IVAR_$_QLPreviewPanelController._forwardedSwipeFilter
+ OBJC_IVAR_$_QLPreviewPanelController._forwardedSwipeInProgress
+ OBJC_IVAR_$_QLPreviewPanelController._forwardedSwipeMonitor
+ OBJC_IVAR_$_QLPreviewPanelController._sidecarSwipeGestureRecognizer
+ OBJC_IVAR_$_QLPreviewSwipeController._animateFromValue
+ OBJC_IVAR_$_QLPreviewSwipeController._animateInitialVelocity
+ OBJC_IVAR_$_QLPreviewSwipeController._animateToValue
+ OBJC_IVAR_$_QLPreviewSwipeController._animationDisplayLink
+ OBJC_IVAR_$_QLPreviewSwipeController._animationTimerStartDate
+ OBJC_IVAR_$_QLPreviewSwipeController._cid
+ OBJC_IVAR_$_QLPreviewSwipeController._contentView
+ OBJC_IVAR_$_QLPreviewSwipeController._delegate
+ OBJC_IVAR_$_QLPreviewSwipeController._finalFrame
+ OBJC_IVAR_$_QLPreviewSwipeController._fullscreenAndOnlyOneScreen
+ OBJC_IVAR_$_QLPreviewSwipeController._initialFrame
+ OBJC_IVAR_$_QLPreviewSwipeController._previewFrame
+ OBJC_IVAR_$_QLPreviewSwipeController._wid
+ OBJC_IVAR_$_QLSidecarSwipeSampleFilter._enabled
+ OBJC_IVAR_$_QLSidecarSwipeSampleFilter._position
+ OBJC_IVAR_$_QLSidecarSwipeSampleFilter._rawPrev1
+ OBJC_IVAR_$_QLSidecarSwipeSampleFilter._rawPrev2
+ OBJC_IVAR_$_QLSidecarSwipeSampleFilter._rejectionCount
+ OBJC_IVAR_$_QLUIServiceBaseDisplayBundle._forwardedSidecarSwipeActive
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeAxisLocked
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeDidPage
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeForwardingStarted
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeMessage
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipePaging
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeRecognizer
+ QLSidecarMultiItemSwipeEnabled
+ QLSidecarMultiItemSwipeEnabled._sidecarMultiItemSwipeEnabled
+ QLSidecarMultiItemSwipeEnabled.onceToken
+ _NSStringFromPoint
+ _OBJC_CLASS_$_CADisplayLink
+ _OBJC_CLASS_$_NSMagnificationGestureRecognizer
+ _OBJC_CLASS_$_NSServiceViewControllerScrollWheelEmulatorMessage
+ _OBJC_CLASS_$_QLBackgroundGestureHostView
+ _OBJC_CLASS_$_QLSidecarSwipeAnimator
+ _OBJC_CLASS_$_QLSidecarSwipeSampleFilter
+ _OBJC_METACLASS_$_QLBackgroundGestureHostView
+ _OBJC_METACLASS_$_QLSidecarSwipeAnimator
+ _OBJC_METACLASS_$_QLSidecarSwipeSampleFilter
+ _QLControlsInteractionDidBeginNotification
+ _QLControlsInteractionDidEndNotification
+ _QLSidecarMultiItemSwipeEnabled
+ __OBJC_$_CLASS_METHODS_QLSidecarSwipeAnimator
+ __OBJC_$_INSTANCE_METHODS_QLBackgroundGestureHostView
+ __OBJC_$_INSTANCE_METHODS_QLSidecarSwipeSampleFilter
+ __OBJC_$_INSTANCE_VARIABLES_QLSidecarSwipeSampleFilter
+ __OBJC_$_PROP_LIST_QLSidecarSwipeSampleFilter
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_QLPreviewSwipeControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_QLPreviewSwipeControllerDelegate
+ __OBJC_CLASS_RO_$_QLBackgroundGestureHostView
+ __OBJC_CLASS_RO_$_QLSidecarSwipeAnimator
+ __OBJC_CLASS_RO_$_QLSidecarSwipeSampleFilter
+ __OBJC_LABEL_PROTOCOL_$_QLPreviewSwipeControllerDelegate
+ __OBJC_METACLASS_RO_$_QLBackgroundGestureHostView
+ __OBJC_METACLASS_RO_$_QLSidecarSwipeAnimator
+ __OBJC_METACLASS_RO_$_QLSidecarSwipeSampleFilter
+ __OBJC_PROTOCOL_$_QLPreviewSwipeControllerDelegate
+ ___61-[QLPreviewPanelController _handleForwardedSwipeScrollEvent:]_block_invoke
+ ___66-[QLPreviewSwipeController swipeWithEvent:containingView:options:]_block_invoke
+ ___91-[QLUIServiceBaseViewController _forwardSidecarSwipeToHostWithState:translation:modifiers:]_block_invoke
+ ___QLSidecarMultiItemSwipeEnabled_block_invoke
+ ___block_descriptor_40_e8_32s_e18_v36?0d8Q16B24^B28l
+ _exp
+ _objc_msgSend$_animateProgress
+ _objc_msgSend$_canSwipe
+ _objc_msgSend$_containingView
+ _objc_msgSend$_continueForwardedSwipeWithEvent:
+ _objc_msgSend$_endForwardedSwipe
+ _objc_msgSend$_forwardSidecarSwipeToHostWithState:translation:modifiers:
+ _objc_msgSend$_handleForwardedSwipeScrollEvent:
+ _objc_msgSend$_isSidecarSwipeGestureRecognizer:
+ _objc_msgSend$_pageContentForSidecarSwipeState:translation:
+ _objc_msgSend$_runSidecarSwipeWithState:translation:velocity:
+ _objc_msgSend$_swipeBegin
+ _objc_msgSend$addSample:
+ _objc_msgSend$addToRunLoop:forMode:
+ _objc_msgSend$allTouches
+ _objc_msgSend$animateFromValue
+ _objc_msgSend$animateInitialVelocity
+ _objc_msgSend$animateToValue
+ _objc_msgSend$animationDisplayLink
+ _objc_msgSend$animationTimerStartDate
+ _objc_msgSend$backgroundClickRecognizer
+ _objc_msgSend$backgroundSidecarSwipeRecognizer
+ _objc_msgSend$beginControlsInteraction
+ _objc_msgSend$beginForwardedSidecarSwipe
+ _objc_msgSend$displayLinkWithTarget:selector:
+ _objc_msgSend$elasticProgressFrom:to:initialVelocity:elapsedTime:
+ _objc_msgSend$endControlsInteraction
+ _objc_msgSend$endForwardedSidecarSwipe
+ _objc_msgSend$forwardedSidecarSwipeActive
+ _objc_msgSend$forwardedSwipeFilter
+ _objc_msgSend$forwardedSwipeInProgress
+ _objc_msgSend$forwardedSwipeMonitor
+ _objc_msgSend$initWithInitialPosition:
+ _objc_msgSend$momentumPhase
+ _objc_msgSend$newSidecarSwipeGestureRecognizer
+ _objc_msgSend$normalizedInitialVelocity:viewWidth:forwardSwipe:
+ _objc_msgSend$previewSwipeController:didEndWithDeltaIndex:isComplete:
+ _objc_msgSend$previewSwipeController:previewFrameWithPreviewView:
+ _objc_msgSend$previewSwipeController:previewItemWithDeltaIndex:shouldLoad:
+ _objc_msgSend$previewSwipeController:progress:
+ _objc_msgSend$sendScrollWheelEmulatorMessage:completion:
+ _objc_msgSend$setAnimateFromValue:
+ _objc_msgSend$setAnimateInitialVelocity:
+ _objc_msgSend$setAnimateToValue:
+ _objc_msgSend$setAnimationDisplayLink:
+ _objc_msgSend$setAnimationTimerStartDate:
+ _objc_msgSend$setBackgroundClickRecognizer:
+ _objc_msgSend$setBackgroundSidecarSwipeRecognizer:
+ _objc_msgSend$setDelta:
+ _objc_msgSend$setForwardedSidecarSwipeActive:
+ _objc_msgSend$setForwardedSwipeFilter:
+ _objc_msgSend$setForwardedSwipeInProgress:
+ _objc_msgSend$setForwardedSwipeMonitor:
+ _objc_msgSend$setModifiers:
+ _objc_msgSend$setPhase:
+ _objc_msgSend$setSidecarSwipeAxisLocked:
+ _objc_msgSend$setSidecarSwipeDidPage:
+ _objc_msgSend$setSidecarSwipeForwardingStarted:
+ _objc_msgSend$setSidecarSwipeMessage:
+ _objc_msgSend$setSidecarSwipePaging:
+ _objc_msgSend$setSidecarSwipeRecognizer:
+ _objc_msgSend$setTimestamp:
+ _objc_msgSend$sidecarSwipeAxisLocked
+ _objc_msgSend$sidecarSwipeContentCanPage
+ _objc_msgSend$sidecarSwipeContentPageByDelta:
+ _objc_msgSend$sidecarSwipeDidPage
+ _objc_msgSend$sidecarSwipeForwardingStarted
+ _objc_msgSend$sidecarSwipeMessage
+ _objc_msgSend$sidecarSwipePaging
+ _objc_msgSend$sidecarSwipeRecognizer
+ _objc_msgSend$swipeAnimateToEndWithState:velocity:viewWidth:progress:
+ _objc_msgSend$swipeBeginWithScrollingDeltaX:containingView:swipeUseOpaqueWindow:
+ _objc_msgSend$swipeSucceededWithProgress:velocity:viewWidth:
+ _objc_msgSend$swipeWithEvent:containingView:options:
+ _objc_msgSend$swipeWithPhase:progress:isComplete:
- -[QLOverlayView hitTest:]
- -[QLPreviewSwipeController completionBlock]
- -[QLPreviewSwipeController setCompletionBlock:]
- -[QLPreviewSwipeController swipeWithEvent:containingView:options:beginBlock:previewFrameBlock:progressBlock:completionBlock:]
- OBJC_IVAR_$_QLPreviewSwipeController._completionBlock
- _QLPreviewControlAccessibilityDescriptionKey
- _QLPreviewControlIsToggleKey
- _QLPreviewControlLargeButtonPadding
- _QLPreviewControlLargeButtonWidthKey
- _QLPreviewControlLargeImageNameKey
- _QLPreviewControlSendActionOnMouseDownKey
- __125-[QLPreviewSwipeController swipeWithEvent:containingView:options:beginBlock:previewFrameBlock:progressBlock:completionBlock:]_block_invoke
- __48-[QLPreviewPanelController trackSwipeWithEvent:]_block_invoke
- ___125-[QLPreviewSwipeController swipeWithEvent:containingView:options:beginBlock:previewFrameBlock:progressBlock:completionBlock:]_block_invoke
- ___48-[QLPreviewPanelController trackSwipeWithEvent:]_block_invoke
- ___block_descriptor_169_e8_32s40s48s56bs_e18_v36?0d8Q16B24^B28l
- ___block_descriptor_40_e8_32s_e28_"<QLPreviewItem>"20?0q8B16l
- ___block_descriptor_40_e8_32s_e54_{CGRect={CGPoint=dd}{CGSize=dd}}16?0"QLPreviewView"8l
- ___block_descriptor_40_e8_32s_e8_v16?0d8l
- ___block_descriptor_48_e8_32s40s_e11_v20?0q8B16l
- _objc_msgSend$swipeWithEvent:containingView:options:beginBlock:previewFrameBlock:progressBlock:completionBlock:
CStrings:
+ "%@ failed to forward sidecar swipe to host: %@ #Remote"
+ "&"
+ "-[QLPreviewSwipeController swipeBeginWithScrollingDeltaX:containingView:swipeUseOpaqueWindow:]"
+ "QLControlsInteractionDidBeginNotification"
+ "QLControlsInteractionDidEndNotification"
+ "QLFullscreenController.backgroundClickGestureRecognizer"
+ "QLPreviewPanelController.sidecarSwipeGestureRecognizer"
+ "QLPreviewSwipeController.m"
+ "QLSidecarMultiItemSwipeEnabled"
+ "QLSidecarSwipeFilterEnabled"
+ "QLUIServiceBaseViewController.sidecarSwipe"
+ "Received simulated swipe point %@"
+ "_NSContextMenuPressGestureRecognizer"
+ "swipeWithEvent can not start without a QLPreviewSwipeControllerDelegate"
+ "window == [containingView window]"
+ "\xf0B"
+ "\xf0\xc1"
- "-[QLPreviewSwipeController swipeWithEvent:containingView:options:beginBlock:previewFrameBlock:progressBlock:completionBlock:]"
- "@\"<QLPreviewItem>\"20@?0q8B16"
- "v16@?0d8"
- "v20@?0q8B16"
- "window == [view window]"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@?0@\"QLPreviewView\"8"
- "\xf0\xa1"
```
