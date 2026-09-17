## QuickLookUI

> `/System/Library/Frameworks/QuickLookUI.framework/Versions/A/QuickLookUI`

```diff

-1114.0.0.0.0
-  __TEXT.__text: 0xc9d38
-  __TEXT.__objc_methlist: 0x10d60
-  __TEXT.__gcc_except_tab: 0x10c8
+1114.1.1.0.0
+  __TEXT.__text: 0xcb78c
+  __TEXT.__objc_methlist: 0x10f40
+  __TEXT.__gcc_except_tab: 0x10d4
   __TEXT.__const: 0xf24
-  __TEXT.__cstring: 0x7ac6
-  __TEXT.__oslogstring: 0x39da
+  __TEXT.__cstring: 0x7ae6
+  __TEXT.__oslogstring: 0x39b8
   __TEXT.__ustring: 0x26
   __TEXT.__swift5_typeref: 0x390
   __TEXT.__swift5_reflstr: 0xc9

   __TEXT.__swift_as_cont: 0x14
   __TEXT.__swift5_capture: 0x20
   __TEXT.__dof_QLSeamles: 0x8e7
-  __TEXT.__unwind_info: 0x4d58
+  __TEXT.__unwind_info: 0x4dc8
   __TEXT.__eh_frame: 0x2b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5d8
+  __DATA_CONST.__const: 0x5e0
   __DATA_CONST.__objc_classlist: 0x690
-  __DATA_CONST.__objc_catlist: 0x68
+  __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8660
+  __DATA_CONST.__objc_selrefs: 0x87b0
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x4b0
   __DATA_CONST.__objc_arraydata: 0x38
-  __DATA_CONST.__got: 0x10e8
-  __AUTH_CONST.__const: 0x21f8
-  __AUTH_CONST.__cfstring: 0x7ec0
-  __AUTH_CONST.__objc_const: 0x17950
+  __DATA_CONST.__got: 0x1100
+  __AUTH_CONST.__const: 0x21d8
+  __AUTH_CONST.__cfstring: 0x7ee0
+  __AUTH_CONST.__objc_const: 0x17b78
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x14a8
+  __AUTH_CONST.__auth_got: 0x14a0
   __AUTH.__objc_data: 0x3a90
   __AUTH.__data: 0x128
-  __DATA.__objc_ivar: 0x1028
+  __DATA.__objc_ivar: 0x1050
   __DATA.__data: 0x1b50
   __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0x748

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6000
-  Symbols:   13271
-  CStrings:  1563
+  Functions: 6039
+  Symbols:   13361
+  CStrings:  1562
 
Symbols:
+ -[NSScrollView(QLPanGestureUtilities) ql_updatePanTouchesForSwipeAvailable:]
+ -[NSView(QLScrollViewUtilities) ql_containsHorizontallyScrollableScrollView]
+ -[NSView(QLScrollViewUtilities) ql_containsMagnifiableScrollView]
+ -[NSView(QLScrollViewUtilities) ql_firstMagnificationGestureRecognizer]
+ -[NSView(QLScrollViewUtilities) ql_updateAllScrollViewPanTouchesForSwipeAvailable:]
+ -[QLDisplayBundle _updateScrollViewPanTouches]
+ -[QLDisplayBundle sidecarSwipeAvailableDidChange]
+ -[QLDisplayBundle sidecarSwipeAvailable]
+ -[QLFullscreenController setSidecarSwipeGestureRecognizer:]
+ -[QLFullscreenController sidecarSwipeGestureRecognizer]
+ -[QLOverlayGlassBackground initWithSize:expandedSize:isForVideo:]
+ -[QLOverlayGlassBackground isForVideo]
+ -[QLOverlayGlassBackground setIsForVideo:]
+ -[QLPanelPreviewDragPreviewPanGestureRecognizer acceptsFirstMouse:]
+ -[QLPreviewDocument sidecarSwipeAvailable]
+ -[QLPreviewOverlayController _setShowOverlay:dimmed:isForVideo:]
+ -[QLPreviewPanelController _sidecarSwipeMagnificationRecognizer]
+ -[QLPreviewPanelController _sidecarSwipeShouldYieldToMagnification]
+ -[QLPreviewPanelController forwardedSwipeLastPosition]
+ -[QLPreviewPanelController gestureRecognizer:shouldReceiveTouch:]
+ -[QLPreviewPanelController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:]
+ -[QLPreviewPanelController setForwardedSwipeLastPosition:]
+ -[QLPreviewPanelController sidecarSwipeAvailableForPreviewView:]
+ -[QLPreviewView sidecarSwipeAvailableDidChange]
+ -[QLPreviewView sidecarSwipeAvailable]
+ -[QLRemoteDisplayBundle sidecarSwipeAvailableDidChange]
+ -[QLSidecarSwipeGestureRecognizer .cxx_destruct]
+ -[QLSidecarSwipeGestureRecognizer ql_activeTouchCount]
+ -[QLSidecarSwipeGestureRecognizer ql_peakTouchCount]
+ -[QLSidecarSwipeGestureRecognizer ql_shouldRequireFailureOfRecognizer:forOneFingerSwipeInContentView:]
+ -[QLSidecarSwipeGestureRecognizer reset]
+ -[QLSidecarSwipeGestureRecognizer touchesBeganWithEvent:]
+ -[QLSidecarSwipeGestureRecognizer touchesCancelledWithEvent:]
+ -[QLSidecarSwipeGestureRecognizer touchesEndedWithEvent:]
+ -[QLUIServiceBaseViewController gestureRecognizer:shouldReceiveTouch:]
+ -[QLUIServiceBaseViewController setSidecarSwipeDidClassifyPinch:]
+ -[QLUIServiceBaseViewController setSidecarSwipeDidDisableMagnification:]
+ -[QLUIServiceBaseViewController setSidecarSwipeGestureRecognizer:]
+ -[QLUIServiceBaseViewController setSidecarSwipeHasScreenBaseline:]
+ -[QLUIServiceBaseViewController setSidecarSwipeHasStartSpread:]
+ -[QLUIServiceBaseViewController setSidecarSwipeLastTranslation:]
+ -[QLUIServiceBaseViewController setSidecarSwipeStartScreenCentroid:]
+ -[QLUIServiceBaseViewController setSidecarSwipeStartSpread:]
+ -[QLUIServiceBaseViewController sidecarSwipeDidClassifyPinch]
+ -[QLUIServiceBaseViewController sidecarSwipeDidDisableMagnification]
+ -[QLUIServiceBaseViewController sidecarSwipeGestureRecognizer]
+ -[QLUIServiceBaseViewController sidecarSwipeHasScreenBaseline]
+ -[QLUIServiceBaseViewController sidecarSwipeHasStartSpread]
+ -[QLUIServiceBaseViewController sidecarSwipeLastTranslation]
+ -[QLUIServiceBaseViewController sidecarSwipeMagnificationRecognizer]
+ -[QLUIServiceBaseViewController sidecarSwipeShouldYieldToMagnification]
+ -[QLUIServiceBaseViewController sidecarSwipeStartScreenCentroid]
+ -[QLUIServiceBaseViewController sidecarSwipeStartSpread]
+ GCC_except_table118
+ GCC_except_table155
+ GCC_except_table229
+ GCC_except_table271
+ OBJC_IVAR_$_QLFullscreenController._sidecarSwipeGestureRecognizer
+ OBJC_IVAR_$_QLOverlayGlassBackground._isForVideo
+ OBJC_IVAR_$_QLPreviewPanelController._forwardedSwipeLastPosition
+ OBJC_IVAR_$_QLPreviewPanelController._sidecarSwipeDidClassifyPinch
+ OBJC_IVAR_$_QLPreviewPanelController._sidecarSwipeDidDisableMagnification
+ OBJC_IVAR_$_QLPreviewPanelController._sidecarSwipeForwardingStarted
+ OBJC_IVAR_$_QLPreviewPanelController._sidecarSwipeHasStartSpread
+ OBJC_IVAR_$_QLPreviewPanelController._sidecarSwipeStartSpread
+ OBJC_IVAR_$_QLSidecarSwipeGestureRecognizer._activeTouchIdentities
+ OBJC_IVAR_$_QLSidecarSwipeGestureRecognizer._peakTouchCount
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeDidClassifyPinch
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeDidDisableMagnification
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeGestureRecognizer
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeHasScreenBaseline
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeHasStartSpread
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeLastTranslation
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeStartScreenCentroid
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeStartSpread
+ _OBJC_CLASS_$_NSScrollView
+ _OBJC_CLASS_$_NSSlider
+ _OBJC_CLASS_$_QLPanelPreviewDragPreviewPanGestureRecognizer
+ _OBJC_CLASS_$_QLSidecarSwipeGestureRecognizer
+ _OBJC_METACLASS_$_QLPanelPreviewDragPreviewPanGestureRecognizer
+ _OBJC_METACLASS_$_QLSidecarSwipeGestureRecognizer
+ _QLSidecarCurrentTouchSpread
+ _QLSidecarGestureLooksLikePinch
+ _QLSidecarSwipeTouchHitsScrubber
+ _QLUIServiceSwipeAvailablePropertyKey
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSScrollView_$_QLPanGestureUtilities
+ __OBJC_$_CATEGORY_NSScrollView_$_QLPanGestureUtilities
+ __OBJC_$_INSTANCE_METHODS_NSView(QLDisplayableAddition|QuickLookAdditions|QLScrollViewUtilities|QLWindowEffectsLibrary|QuickLookUI)
+ __OBJC_$_INSTANCE_METHODS_QLPanelPreviewDragPreviewPanGestureRecognizer
+ __OBJC_$_INSTANCE_METHODS_QLSidecarSwipeGestureRecognizer
+ __OBJC_$_INSTANCE_VARIABLES_QLSidecarSwipeGestureRecognizer
+ __OBJC_$_PROP_LIST_QLSidecarSwipeGestureRecognizer
+ __OBJC_CLASS_RO_$_QLPanelPreviewDragPreviewPanGestureRecognizer
+ __OBJC_CLASS_RO_$_QLSidecarSwipeGestureRecognizer
+ __OBJC_METACLASS_RO_$_QLPanelPreviewDragPreviewPanGestureRecognizer
+ __OBJC_METACLASS_RO_$_QLSidecarSwipeGestureRecognizer
+ _objc_msgSend$_setShowOverlay:dimmed:isForVideo:
+ _objc_msgSend$_sidecarSwipeMagnificationRecognizer
+ _objc_msgSend$_sidecarSwipeShouldYieldToMagnification
+ _objc_msgSend$_updateScrollViewPanTouches
+ _objc_msgSend$allowsMagnification
+ _objc_msgSend$convertPointToScreen:
+ _objc_msgSend$forwardedSwipeLastPosition
+ _objc_msgSend$gestureRecognizerForScrolling
+ _objc_msgSend$gestureRecognizers
+ _objc_msgSend$identity
+ _objc_msgSend$initWithSize:expandedSize:isForVideo:
+ _objc_msgSend$isForVideo
+ _objc_msgSend$numberOfTouchesRequired
+ _objc_msgSend$ql_activeTouchCount
+ _objc_msgSend$ql_containsHorizontallyScrollableScrollView
+ _objc_msgSend$ql_containsMagnifiableScrollView
+ _objc_msgSend$ql_firstMagnificationGestureRecognizer
+ _objc_msgSend$ql_peakTouchCount
+ _objc_msgSend$ql_shouldRequireFailureOfRecognizer:forOneFingerSwipeInContentView:
+ _objc_msgSend$ql_updateAllScrollViewPanTouchesForSwipeAvailable:
+ _objc_msgSend$ql_updatePanTouchesForSwipeAvailable:
+ _objc_msgSend$rangeOfString:options:
+ _objc_msgSend$setForwardedSwipeLastPosition:
+ _objc_msgSend$setMaximumNumberOfTouches:
+ _objc_msgSend$setMinimumNumberOfTouches:
+ _objc_msgSend$setNextState
+ _objc_msgSend$setSidecarSwipeDidClassifyPinch:
+ _objc_msgSend$setSidecarSwipeDidDisableMagnification:
+ _objc_msgSend$setSidecarSwipeHasScreenBaseline:
+ _objc_msgSend$setSidecarSwipeHasStartSpread:
+ _objc_msgSend$setSidecarSwipeLastTranslation:
+ _objc_msgSend$setSidecarSwipeStartScreenCentroid:
+ _objc_msgSend$setSidecarSwipeStartSpread:
+ _objc_msgSend$sidecarSwipeAvailable
+ _objc_msgSend$sidecarSwipeAvailableDidChange
+ _objc_msgSend$sidecarSwipeAvailableForPreviewView:
+ _objc_msgSend$sidecarSwipeDidClassifyPinch
+ _objc_msgSend$sidecarSwipeDidDisableMagnification
+ _objc_msgSend$sidecarSwipeGestureRecognizer
+ _objc_msgSend$sidecarSwipeHasScreenBaseline
+ _objc_msgSend$sidecarSwipeHasStartSpread
+ _objc_msgSend$sidecarSwipeLastTranslation
+ _objc_msgSend$sidecarSwipeMagnificationRecognizer
+ _objc_msgSend$sidecarSwipeShouldYieldToMagnification
+ _objc_msgSend$sidecarSwipeStartScreenCentroid
+ _objc_msgSend$sidecarSwipeStartSpread
+ _objc_msgSend$touchesMatchingPhase:inView:
- -[QLFullscreenController setSidecarSwipeRecognizer:]
- -[QLFullscreenController sidecarSwipeRecognizer]
- -[QLOverlayGlassBackground initWithSize:expandedSize:]
- -[QLPanelPreviewPanGestureRecognizer acceptsFirstMouse:]
- -[QLPreviewOverlayController _setShowOverlay:dimmed:]
- -[QLPreviewPanelController forwardedSwipeFilter]
- -[QLPreviewPanelController setForwardedSwipeFilter:]
- -[QLSidecarSwipeSampleFilter addSample:]
- -[QLSidecarSwipeSampleFilter initWithInitialPosition:]
- -[QLSidecarSwipeSampleFilter isEnabled]
- -[QLSidecarSwipeSampleFilter position]
- -[QLSidecarSwipeSampleFilter setEnabled:]
- -[QLUIServiceBaseViewController setSidecarSwipeRecognizer:]
- -[QLUIServiceBaseViewController sidecarSwipeRecognizer]
- GCC_except_table117
- GCC_except_table152
- GCC_except_table227
- GCC_except_table269
- OBJC_IVAR_$_QLFullscreenController._sidecarSwipeRecognizer
- OBJC_IVAR_$_QLPreviewPanelController._forwardedSwipeFilter
- OBJC_IVAR_$_QLSidecarSwipeSampleFilter._enabled
- OBJC_IVAR_$_QLSidecarSwipeSampleFilter._position
- OBJC_IVAR_$_QLSidecarSwipeSampleFilter._rawPrev1
- OBJC_IVAR_$_QLSidecarSwipeSampleFilter._rawPrev2
- OBJC_IVAR_$_QLSidecarSwipeSampleFilter._rejectionCount
- OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeRecognizer
- QLSidecarMultiItemSwipeEnabled
- QLSidecarMultiItemSwipeEnabled._sidecarMultiItemSwipeEnabled
- QLSidecarMultiItemSwipeEnabled.onceToken
- _NSStringFromPoint
- _OBJC_CLASS_$_QLPanelPreviewPanGestureRecognizer
- _OBJC_CLASS_$_QLSidecarSwipeSampleFilter
- _OBJC_METACLASS_$_QLPanelPreviewPanGestureRecognizer
- _OBJC_METACLASS_$_QLSidecarSwipeSampleFilter
- _QLSidecarMultiItemSwipeEnabled
- __OBJC_$_INSTANCE_METHODS_NSView(QLDisplayableAddition|QuickLookAdditions|QLWindowEffectsLibrary|QuickLookUI)
- __OBJC_$_INSTANCE_METHODS_QLPanelPreviewPanGestureRecognizer
- __OBJC_$_INSTANCE_METHODS_QLSidecarSwipeSampleFilter
- __OBJC_$_INSTANCE_VARIABLES_QLSidecarSwipeSampleFilter
- __OBJC_$_PROP_LIST_QLSidecarSwipeSampleFilter
- __OBJC_CLASS_RO_$_QLPanelPreviewPanGestureRecognizer
- __OBJC_CLASS_RO_$_QLSidecarSwipeSampleFilter
- __OBJC_METACLASS_RO_$_QLPanelPreviewPanGestureRecognizer
- __OBJC_METACLASS_RO_$_QLSidecarSwipeSampleFilter
- ___QLSidecarMultiItemSwipeEnabled_block_invoke
- _objc_msgSend$_setShowOverlay:dimmed:
- _objc_msgSend$addSample:
- _objc_msgSend$forwardedSwipeFilter
- _objc_msgSend$initWithInitialPosition:
- _objc_msgSend$initWithSize:expandedSize:
- _objc_msgSend$setForwardedSwipeFilter:
- _objc_msgSend$setSidecarSwipeRecognizer:
- _objc_msgSend$sidecarSwipeRecognizer
CStrings:
+ "%@ failed to forward sidecar swipe to host: %@"
+ "Scrubber"
+ "_NSScrollAxisAwareLeftMouseDragGestureRecognizer"
+ "swipeAvailable"
- "&"
- "------ shouldReceiveTouch: %@"
- "QLSidecarMultiItemSwipeEnabled"
- "QLSidecarSwipeFilterEnabled"
- "Received simulated swipe point %@"
```
