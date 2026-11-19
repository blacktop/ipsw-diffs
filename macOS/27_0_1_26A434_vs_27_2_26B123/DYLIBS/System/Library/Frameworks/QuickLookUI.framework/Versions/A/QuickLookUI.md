## QuickLookUI

> `/System/Library/Frameworks/QuickLookUI.framework/Versions/A/QuickLookUI`

```diff

-1114.0.0.0.0
-  __TEXT.__text: 0xcfcd8
-  __TEXT.__objc_methlist: 0x10d60
-  __TEXT.__gcc_except_tab: 0x10c8
-  __TEXT.__const: 0xf24
-  __TEXT.__cstring: 0x7ac6
-  __TEXT.__oslogstring: 0x39da
+1114.1.11.0.0
+  __TEXT.__text: 0xd4c44
+  __TEXT.__objc_methlist: 0x11250
+  __TEXT.__gcc_except_tab: 0x10f4
+  __TEXT.__const: 0x1164
+  __TEXT.__cstring: 0x7bb6
+  __TEXT.__oslogstring: 0x3cb1
   __TEXT.__ustring: 0x26
-  __TEXT.__swift5_typeref: 0x390
-  __TEXT.__swift5_reflstr: 0xc9
-  __TEXT.__swift5_assocty: 0x108
-  __TEXT.__constg_swiftt: 0x148
-  __TEXT.__swift5_fieldmd: 0xcc
-  __TEXT.__swift5_proto: 0x84
-  __TEXT.__swift5_types: 0x18
-  __TEXT.__swift_as_entry: 0x24
+  __TEXT.__swift5_typeref: 0x470
+  __TEXT.__swift5_reflstr: 0xe9
+  __TEXT.__swift5_assocty: 0x128
+  __TEXT.__constg_swiftt: 0x18c
+  __TEXT.__swift5_fieldmd: 0xe8
+  __TEXT.__swift5_proto: 0x9c
+  __TEXT.__swift5_types: 0x1c
+  __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__swift_as_cont: 0x14
+  __TEXT.__swift_as_cont: 0x18
   __TEXT.__swift5_capture: 0x20
   __TEXT.__dof_QLSeamles: 0x8e7
-  __TEXT.__unwind_info: 0x3e18
+  __TEXT.__unwind_info: 0x3f80
   __TEXT.__eh_frame: 0x2b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5d8
-  __DATA_CONST.__objc_classlist: 0x690
-  __DATA_CONST.__objc_catlist: 0x68
+  __DATA_CONST.__const: 0x620
+  __DATA_CONST.__objc_classlist: 0x6a0
+  __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8660
+  __DATA_CONST.__objc_selrefs: 0x8948
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x4b0
   __DATA_CONST.__objc_arraydata: 0x38
-  __DATA_CONST.__got: 0x10e8
-  __AUTH_CONST.__const: 0x21f8
+  __DATA_CONST.__got: 0x1148
+  __AUTH_CONST.__const: 0x2370
   __AUTH_CONST.__cfstring: 0x7ec0
-  __AUTH_CONST.__objc_const: 0x17950
+  __AUTH_CONST.__objc_const: 0x17df0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x14a8
+  __AUTH_CONST.__auth_got: 0x1558
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x3a90
+  __AUTH.__objc_data: 0x3b30
   __AUTH.__data: 0x128
-  __DATA.__objc_ivar: 0x1028
-  __DATA.__data: 0x1b50
-  __DATA.__bss: 0x14a0
-  __DATA.__common: 0x1
+  __DATA.__objc_ivar: 0x1060
+  __DATA.__data: 0x1bd8
+  __DATA.__bss: 0x17b0
+  __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x748
   __DATA_DIRTY.__data: 0x28
   __DATA_DIRTY.__bss: 0x70

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6000
-  Symbols:   13271
-  CStrings:  1563
+  Functions: 6145
+  Symbols:   13535
+  CStrings:  1580
 
Symbols:
+ +[NSScrollView(QLPanGestureUtilities) ql_scrollViewOwningScrollPanGestureRecognizer:]
+ +[QLPreviewOverlayController temporaryControlsRevealDuration]
+ -[NSScrollView(QLPanGestureUtilities) ql_canScrollContent]
+ -[NSScrollView(QLPanGestureUtilities) ql_updatePanTouchesForSwipeAvailable:inMarkup:]
+ -[NSView(QLScrollViewUtilities) ql_containsHorizontallyScrollableScrollView]
+ -[NSView(QLScrollViewUtilities) ql_containsMagnifiableScrollView]
+ -[NSView(QLScrollViewUtilities) ql_firstMagnificationGestureRecognizer]
+ -[NSView(QLScrollViewUtilities) ql_updateAllScrollViewPanTouchesForSwipeAvailable:inMarkup:]
+ -[QLControlButton mouseMoved:]
+ -[QLControlSegmentedControl mouseMoved:]
+ -[QLDisplayBundle _updateScrollViewPanTouches]
+ -[QLDisplayBundle hideOverlayControls]
+ -[QLDisplayBundle showOverlayControlsMomentarily]
+ -[QLDisplayBundle sidecarSwipeAvailableDidChange]
+ -[QLDisplayBundle sidecarSwipeAvailable]
+ -[QLDisplayBundleViewController handlesOverlayControlsTaps]
+ -[QLDisplayBundleViewController hasRevealedOverlayControlAtPoint:]
+ -[QLDisplayBundleViewController hideOverlayControls]
+ -[QLDisplayBundleViewController overlayControlsTapAtPoint:]
+ -[QLDisplayBundleViewController revealsOverlayControlsWhenAttached]
+ -[QLDisplayBundleViewController setRevealsOverlayControlsWhenAttached:]
+ -[QLDisplayBundleViewController showOverlayControlsMomentarily]
+ -[QLFullscreenController _dragControlsPanelWithGesture:]
+ -[QLFullscreenController _ensureControlsPanelOrderedAboveContent]
+ -[QLFullscreenController _installControlsPanelDragDetection]
+ -[QLFullscreenController _orderControlsPanelAboveContent]
+ -[QLFullscreenController _performTouchDownControlsToggle]
+ -[QLFullscreenController _synchronizeControlsPanelPosition]
+ -[QLFullscreenController cancelPendingTouchDownControlsToggle]
+ -[QLFullscreenController controlsPanelDragRecognizer]
+ -[QLFullscreenController enteringFullscreen]
+ -[QLFullscreenController gestureRecognizerShouldBegin:]
+ -[QLFullscreenController lastControlsToggleTime]
+ -[QLFullscreenController setControlsPanelDragRecognizer:]
+ -[QLFullscreenController setEnteringFullscreen:]
+ -[QLFullscreenController setLastControlsToggleTime:]
+ -[QLFullscreenController setSidecarSwipeGestureRecognizer:]
+ -[QLFullscreenController setSwipeInProgress:]
+ -[QLFullscreenController sidecarSwipeGestureRecognizer]
+ -[QLFullscreenController swipeInProgress]
+ -[QLFullscreenHUDContentView acceptsFirstMouse:]
+ -[QLFullscreenHUDWindow _childWindowOrderingPriority]
+ -[QLFullscreenHUDWindow _doOrderWindow:]
+ -[QLInlinePreviewController _remoteDisplayBundleOwnsOverlay]
+ -[QLInlinePreviewController hideOverlay]
+ -[QLInlinePreviewController showOverlayMomentarily]
+ -[QLOverlayBaseButtonLayer pressAtPoint:]
+ -[QLOverlayGlassBackground initWithSize:expandedSize:isForVideo:]
+ -[QLOverlayGlassBackground isForVideo]
+ -[QLOverlayGlassBackground setIsForVideo:]
+ -[QLPanelPreviewDragPreviewPanGestureRecognizer acceptsFirstMouse:]
+ -[QLPreviewDocument sidecarSwipeAvailable]
+ -[QLPreviewDragController startDraggingWithGestureRecognizer:isTouchEvent:beganOrFailedHandler:]
+ -[QLPreviewOverlayController _cancelTemporaryControlsReveal]
+ -[QLPreviewOverlayController _setShowOverlay:dimmed:isForVideo:]
+ -[QLPreviewOverlayController controlsTemporarilyRevealed]
+ -[QLPreviewOverlayController hideOverlay]
+ -[QLPreviewOverlayController showOverlayMomentarily]
+ -[QLPreviewPanelController _isShowingShareSheet]
+ -[QLPreviewPanelController _isWindowResizeGestureRecognizer:]
+ -[QLPreviewPanelController _sidecarSwipeMagnificationRecognizer]
+ -[QLPreviewPanelController _sidecarSwipeShouldYieldToMagnification]
+ -[QLPreviewPanelController beginControlsInteraction]
+ -[QLPreviewPanelController endControlsInteraction]
+ -[QLPreviewPanelController forwardedSwipeLastPosition]
+ -[QLPreviewPanelController gestureRecognizer:shouldReceiveTouch:]
+ -[QLPreviewPanelController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:]
+ -[QLPreviewPanelController isShowingShareSheet]
+ -[QLPreviewPanelController setForwardedSwipeLastPosition:]
+ -[QLPreviewPanelController setSidecarSwipeDidReceiveChange:]
+ -[QLPreviewPanelController setSwipeControllerIsSidecarDriven:]
+ -[QLPreviewPanelController set_isShowingShareSheet:]
+ -[QLPreviewPanelController sidecarSwipeAvailableForPreviewView:]
+ -[QLPreviewPanelController sidecarSwipeDidReceiveChange]
+ -[QLPreviewPanelController swipeControllerIsSidecarDriven]
+ -[QLPreviewSwipeTransitionView hitTest:]
+ -[QLPreviewTitleBarView _isStoplightButtonHit:]
+ -[QLPreviewView dragTouchGestureRecognizer]
+ -[QLPreviewView receivedDragGesture:isTouchEvent:]
+ -[QLPreviewView receivedDragTouchGesture:]
+ -[QLPreviewView setDragTouchGestureRecognizer:]
+ -[QLPreviewView sidecarSwipeAvailableDidChange]
+ -[QLPreviewView sidecarSwipeAvailable]
+ -[QLPreviewView startDragFromGesture:isTouchEvent:beganOrFailedHandler:]
+ -[QLRemoteDisplayBundle hideOverlayControls]
+ -[QLRemoteDisplayBundle showOverlayControlsMomentarily]
+ -[QLRemoteDisplayBundle sidecarSwipeAvailableDidChange]
+ -[QLSidecarSwipeGestureRecognizer .cxx_destruct]
+ -[QLSidecarSwipeGestureRecognizer ql_activeTouchCount]
+ -[QLSidecarSwipeGestureRecognizer ql_peakTouchCount]
+ -[QLSidecarSwipeGestureRecognizer ql_shouldRequireFailureOfRecognizer:forOneFingerSwipeInContentView:]
+ -[QLSidecarSwipeGestureRecognizer reset]
+ -[QLSidecarSwipeGestureRecognizer touchesBeganWithEvent:]
+ -[QLSidecarSwipeGestureRecognizer touchesCancelledWithEvent:]
+ -[QLSidecarSwipeGestureRecognizer touchesEndedWithEvent:]
+ -[QLUIServiceBaseViewController dragTouchRecognizer]
+ -[QLUIServiceBaseViewController gestureRecognizer:shouldAttemptToRecognizeWithEvent:]
+ -[QLUIServiceBaseViewController gestureRecognizer:shouldReceiveTouch:]
+ -[QLUIServiceBaseViewController receivedDragGesture:isTouchEvent:]
+ -[QLUIServiceBaseViewController receivedDragTouchGesture:]
+ -[QLUIServiceBaseViewController setDragTouchRecognizer:]
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
+ GCC_except_table107
+ GCC_except_table120
+ GCC_except_table123
+ GCC_except_table157
+ GCC_except_table233
+ GCC_except_table271
+ GCC_except_table358
+ GCC_except_table40
+ GCC_except_table8
+ OBJC_IVAR_$_QLDisplayBundleViewController._revealsOverlayControlsWhenAttached
+ OBJC_IVAR_$_QLFullscreenController._controlsPanelDragRecognizer
+ OBJC_IVAR_$_QLFullscreenController._enteringFullscreen
+ OBJC_IVAR_$_QLFullscreenController._hudControlsPanel
+ OBJC_IVAR_$_QLFullscreenController._lastControlsToggleTime
+ OBJC_IVAR_$_QLFullscreenController._sidecarSwipeGestureRecognizer
+ OBJC_IVAR_$_QLFullscreenController._swipeInProgress
+ OBJC_IVAR_$_QLOverlayGlassBackground._isForVideo
+ OBJC_IVAR_$_QLPreviewBubble._touchEventMonitor
+ OBJC_IVAR_$_QLPreviewOverlayController._controlsTemporarilyRevealed
+ OBJC_IVAR_$_QLPreviewPanelController.__isShowingShareSheet
+ OBJC_IVAR_$_QLPreviewPanelController._forwardedSwipeLastPosition
+ OBJC_IVAR_$_QLPreviewPanelController._sidecarSwipeDidClassifyPinch
+ OBJC_IVAR_$_QLPreviewPanelController._sidecarSwipeDidDisableMagnification
+ OBJC_IVAR_$_QLPreviewPanelController._sidecarSwipeDidReceiveChange
+ OBJC_IVAR_$_QLPreviewPanelController._sidecarSwipeForwardingStarted
+ OBJC_IVAR_$_QLPreviewPanelController._sidecarSwipeHasStartSpread
+ OBJC_IVAR_$_QLPreviewPanelController._sidecarSwipeStartSpread
+ OBJC_IVAR_$_QLPreviewPanelController._swipeControllerIsSidecarDriven
+ OBJC_IVAR_$_QLPreviewSwipeController._transitionView
+ OBJC_IVAR_$_QLPreviewViewReserved.dragTouchGestureRecognizer
+ OBJC_IVAR_$_QLSidecarSwipeGestureRecognizer._activeTouchIdentities
+ OBJC_IVAR_$_QLSidecarSwipeGestureRecognizer._peakTouchCount
+ OBJC_IVAR_$_QLUIServiceBaseViewController._dragTouchRecognizer
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeDidClassifyPinch
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeDidDisableMagnification
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeGestureRecognizer
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeHasScreenBaseline
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeHasStartSpread
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeLastTranslation
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeStartScreenCentroid
+ OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeStartSpread
+ QLControlObservePointerInputMode.onceToken
+ _NSDraggingImageComponentIconKey
+ _OBJC_CLASS_$_NSDraggingImageComponent
+ _OBJC_CLASS_$_NSScrollView
+ _OBJC_CLASS_$_NSSlider
+ _OBJC_CLASS_$_QLFullscreenHUDContentView
+ _OBJC_CLASS_$_QLPanelPreviewDragPreviewPanGestureRecognizer
+ _OBJC_CLASS_$_QLPreviewSwipeTransitionView
+ _OBJC_CLASS_$_QLSidecarSwipeGestureRecognizer
+ _OBJC_METACLASS_$_QLFullscreenHUDContentView
+ _OBJC_METACLASS_$_QLPanelPreviewDragPreviewPanGestureRecognizer
+ _OBJC_METACLASS_$_QLPreviewSwipeTransitionView
+ _OBJC_METACLASS_$_QLSidecarSwipeGestureRecognizer
+ _QLSidecarCurrentTouchSpread
+ _QLSidecarGestureLooksLikePinch
+ _QLSidecarSwipeTouchHitsScrubber
+ _QLUIServiceSwipeAvailablePropertyKey
+ __66-[QLPreviewBubble setAutomaticallyCloseWithMask:filterMask:block:]_block_invoke
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSScrollView_$_QLPanGestureUtilities
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSScrollView_$_QLPanGestureUtilities
+ __OBJC_$_CATEGORY_NSScrollView_$_QLPanGestureUtilities
+ __OBJC_$_INSTANCE_METHODS_NSView(QLDisplayableAddition|QuickLookAdditions|QLScrollViewUtilities|QLWindowEffectsLibrary|QuickLookUI)
+ __OBJC_$_INSTANCE_METHODS_QLFullscreenHUDContentView
+ __OBJC_$_INSTANCE_METHODS_QLPanelPreviewDragPreviewPanGestureRecognizer
+ __OBJC_$_INSTANCE_METHODS_QLPreviewSwipeTransitionView
+ __OBJC_$_INSTANCE_METHODS_QLSidecarSwipeGestureRecognizer
+ __OBJC_$_INSTANCE_VARIABLES_QLSidecarSwipeGestureRecognizer
+ __OBJC_$_PROP_LIST_QLSidecarSwipeGestureRecognizer
+ __OBJC_CLASS_RO_$_QLFullscreenHUDContentView
+ __OBJC_CLASS_RO_$_QLPanelPreviewDragPreviewPanGestureRecognizer
+ __OBJC_CLASS_RO_$_QLPreviewSwipeTransitionView
+ __OBJC_CLASS_RO_$_QLSidecarSwipeGestureRecognizer
+ __OBJC_METACLASS_RO_$_QLFullscreenHUDContentView
+ __OBJC_METACLASS_RO_$_QLPanelPreviewDragPreviewPanGestureRecognizer
+ __OBJC_METACLASS_RO_$_QLPreviewSwipeTransitionView
+ __OBJC_METACLASS_RO_$_QLSidecarSwipeGestureRecognizer
+ ___44-[QLPreviewPanelController shareFromButton:]_block_invoke
+ ___50-[QLPreviewView receivedDragGesture:isTouchEvent:]_block_invoke
+ ___52-[QLPreviewSwipeController _swipeEndedAndCompleted:]_block_invoke
+ ___66-[QLUIServiceBaseViewController receivedDragGesture:isTouchEvent:]_block_invoke
+ ___72-[QLPreviewView startDragFromGesture:isTouchEvent:beganOrFailedHandler:]_block_invoke
+ ___83-[QLPreviewPanelController previewSwipeController:didEndWithDeltaIndex:isComplete:]_block_invoke
+ ___96-[QLPreviewDragController startDraggingWithGestureRecognizer:isTouchEvent:beganOrFailedHandler:]_block_invoke
+ ___96-[QLPreviewDragController startDraggingWithGestureRecognizer:isTouchEvent:beganOrFailedHandler:]_block_invoke_2
+ ___QLControlObservePointerInputMode_block_invoke
+ ___QLControlObservePointerInputMode_block_invoke_2
+ ___QLControlObservePointerInputMode_block_invoke_3
+ ___QLControlObservePointerInputMode_block_invoke_4
+ ___block_descriptor_32_e26_"NSEvent"16?0"NSEvent"8l
+ ___block_descriptor_32_e29_B24?0"NSTouch"8"NSEvent"16l
+ ___block_descriptor_40_e8_32bs_e26_"NSEvent"16?0"NSEvent"8l
+ ___block_descriptor_40_e8_32bs_e29_B24?0"NSTouch"8"NSEvent"16l
+ ___block_descriptor_40_e8_32w_e8_v16?08l
+ ___block_descriptor_49_e8_32s40s_e28_v16?0"NSAnimationContext"8l
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e51_v48?0"NSImage"8{CGRect={CGPoint=dd}{CGSize=dd}}16l
+ ___block_descriptor_73_e8_32s_e14_"NSArray"8?0l
+ ___swift_allocate_value_buffer
+ ___swift_project_value_buffer
+ __swiftEmptySetSingleton
+ _associated conformance 11QuickLookUI14DocumentEntityV10AppIntents015SystemFrameworkE0AaD0fE0
+ _associated conformance 11QuickLookUI14DocumentEntityV10AppIntents04FileE0AaD0fE0
+ _associated conformance 11QuickLookUI14DocumentEntityV5QueryV10AppIntents0eF16ValidationBypassAaF0eF0
+ _associated conformance 11QuickLookUI21ResolveDocumentIntentV10AppIntents0gF0AA13PerformResultAdEP_AD0fJ0
+ _associated conformance 11QuickLookUI21ResolveDocumentIntentV10AppIntents0gF0AA14SummaryContentAdEP_AD09ParameterI0
+ _associated conformance 11QuickLookUI21ResolveDocumentIntentV10AppIntents0gF0AaD09_SupportsG12Dependencies
+ _associated conformance 11QuickLookUI21ResolveDocumentIntentV10AppIntents0gF0AaD24PersistentlyIdentifiable
+ _objc_msgSend$_cancelTemporaryControlsReveal
+ _objc_msgSend$_dragWindowRelativeToMouseDown:
+ _objc_msgSend$_ensureControlsPanelOrderedAboveContent
+ _objc_msgSend$_glassWindowBackingGlassView
+ _objc_msgSend$_installControlsPanelDragDetection
+ _objc_msgSend$_isShowingShareSheet
+ _objc_msgSend$_isWindowResizeGestureRecognizer:
+ _objc_msgSend$_lastInteractionWasDirectTouch
+ _objc_msgSend$_orderControlsPanelAboveContent
+ _objc_msgSend$_remoteDisplayBundleOwnsOverlay
+ _objc_msgSend$_setCornerRadius:
+ _objc_msgSend$_setShowOverlay:dimmed:isForVideo:
+ _objc_msgSend$_sidecarSwipeMagnificationRecognizer
+ _objc_msgSend$_sidecarSwipeShouldYieldToMagnification
+ _objc_msgSend$_synchronizeControlsPanelPosition
+ _objc_msgSend$_updateScrollViewPanTouches
+ _objc_msgSend$addLocalMonitorForTouchBegan:
+ _objc_msgSend$allowsMagnification
+ _objc_msgSend$anchorRect
+ _objc_msgSend$cancelPendingTouchDownControlsToggle
+ _objc_msgSend$controlsPanelDragRecognizer
+ _objc_msgSend$controlsTemporarilyRevealed
+ _objc_msgSend$convertPointToScreen:
+ _objc_msgSend$dragTouchGestureRecognizer
+ _objc_msgSend$dragTouchRecognizer
+ _objc_msgSend$draggingImageComponentWithKey:
+ _objc_msgSend$enteringFullscreen
+ _objc_msgSend$forwardedSwipeLastPosition
+ _objc_msgSend$gestureRecognizerForScrolling
+ _objc_msgSend$gestureRecognizers
+ _objc_msgSend$hasRevealedOverlayControlAtPoint:
+ _objc_msgSend$hideOverlay
+ _objc_msgSend$hideOverlayControls
+ _objc_msgSend$identity
+ _objc_msgSend$initWithSize:expandedSize:isForVideo:
+ _objc_msgSend$isForVideo
+ _objc_msgSend$isShowingShareSheet
+ _objc_msgSend$lastControlsToggleTime
+ _objc_msgSend$mouseDownCanMoveWindow
+ _objc_msgSend$mouseEventWithType:location:modifierFlags:timestamp:windowNumber:context:eventNumber:clickCount:pressure:
+ _objc_msgSend$options
+ _objc_msgSend$pressAtPoint:
+ _objc_msgSend$ql_activeTouchCount
+ _objc_msgSend$ql_canScrollContent
+ _objc_msgSend$ql_containsHorizontallyScrollableScrollView
+ _objc_msgSend$ql_containsMagnifiableScrollView
+ _objc_msgSend$ql_firstMagnificationGestureRecognizer
+ _objc_msgSend$ql_peakTouchCount
+ _objc_msgSend$ql_scrollViewOwningScrollPanGestureRecognizer:
+ _objc_msgSend$ql_shouldRequireFailureOfRecognizer:forOneFingerSwipeInContentView:
+ _objc_msgSend$ql_updateAllScrollViewPanTouchesForSwipeAvailable:inMarkup:
+ _objc_msgSend$ql_updatePanTouchesForSwipeAvailable:inMarkup:
+ _objc_msgSend$rangeOfString:options:
+ _objc_msgSend$receivedDragGesture:isTouchEvent:
+ _objc_msgSend$revealsOverlayControlsWhenAttached
+ _objc_msgSend$setControlsPanelDragRecognizer:
+ _objc_msgSend$setDelaysPrimaryMouseButtonEvents:
+ _objc_msgSend$setDragTouchGestureRecognizer:
+ _objc_msgSend$setDragTouchRecognizer:
+ _objc_msgSend$setDraggingFrame:
+ _objc_msgSend$setEnteringFullscreen:
+ _objc_msgSend$setForwardedSwipeLastPosition:
+ _objc_msgSend$setImageComponentsProvider:
+ _objc_msgSend$setLastControlsToggleTime:
+ _objc_msgSend$setMaximumNumberOfTouches:
+ _objc_msgSend$setMinimumNumberOfTouches:
+ _objc_msgSend$setNextState
+ _objc_msgSend$setOptions:
+ _objc_msgSend$setRevealsOverlayControlsWhenAttached:
+ _objc_msgSend$setSidecarSwipeDidClassifyPinch:
+ _objc_msgSend$setSidecarSwipeDidDisableMagnification:
+ _objc_msgSend$setSidecarSwipeDidReceiveChange:
+ _objc_msgSend$setSidecarSwipeHasScreenBaseline:
+ _objc_msgSend$setSidecarSwipeHasStartSpread:
+ _objc_msgSend$setSidecarSwipeLastTranslation:
+ _objc_msgSend$setSidecarSwipeStartScreenCentroid:
+ _objc_msgSend$setSidecarSwipeStartSpread:
+ _objc_msgSend$setSwipeControllerIsSidecarDriven:
+ _objc_msgSend$setSwipeInProgress:
+ _objc_msgSend$set_isShowingShareSheet:
+ _objc_msgSend$sheetParent
+ _objc_msgSend$showOverlayControlsMomentarily
+ _objc_msgSend$showOverlayMomentarily
+ _objc_msgSend$sidecarSwipeAvailable
+ _objc_msgSend$sidecarSwipeAvailableDidChange
+ _objc_msgSend$sidecarSwipeAvailableForPreviewView:
+ _objc_msgSend$sidecarSwipeDidClassifyPinch
+ _objc_msgSend$sidecarSwipeDidDisableMagnification
+ _objc_msgSend$sidecarSwipeDidReceiveChange
+ _objc_msgSend$sidecarSwipeGestureRecognizer
+ _objc_msgSend$sidecarSwipeHasScreenBaseline
+ _objc_msgSend$sidecarSwipeHasStartSpread
+ _objc_msgSend$sidecarSwipeLastTranslation
+ _objc_msgSend$sidecarSwipeMagnificationRecognizer
+ _objc_msgSend$sidecarSwipeShouldYieldToMagnification
+ _objc_msgSend$sidecarSwipeStartScreenCentroid
+ _objc_msgSend$sidecarSwipeStartSpread
+ _objc_msgSend$startDragFromGesture:isTouchEvent:beganOrFailedHandler:
+ _objc_msgSend$startDraggingWithGestureRecognizer:isTouchEvent:beganOrFailedHandler:
+ _objc_msgSend$swipeControllerIsSidecarDriven
+ _objc_msgSend$temporaryControlsRevealDuration
+ _objc_msgSend$touchesMatchingPhase:inView:
+ _sLastDirectTouchTimestamp
+ _sPointerMovedSinceDirectTouch
+ _sTooltipOwner
+ _swift_once
+ _swift_slowAlloc
+ _symbolic $s10AppIntents0A6IntentP
+ _symbolic _____ 11QuickLookUI21ResolveDocumentIntentV
+ _symbolic _____Sg 10AppIntents12IntentDialogV
+ _symbolic _____Sg 10Foundation23LocalizedStringResourceV
+ _symbolic _____Sg 11QuickLookUI14DocumentEntityV
+ _symbolic _____y_____A3BG 10AppIntents21IntentResultContainerV s5NeverO
+ _symbolic _____y_____G s11_SetStorageC 10AppIntents22IntentExecutionTargetsV9ConditionV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10AppIntents22IntentExecutionTargetsV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10AppIntents22IntentExecutionTargetsV9ConditionV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 22UniformTypeIdentifiers6UTTypeV
+ _symbolic _____y_____SgG 10AppIntents15IntentParameterC 11QuickLookUI14DocumentEntityV
+ _symbolic _____y______Qo_ 10AppIntents0A6IntentPAAE16parameterSummaryQrvpZQO 11QuickLookUI015ResolveDocumentC0V
+ _type_layout_string 11QuickLookUI21ResolveDocumentIntentV
+ get_witness_table 10AppIntents21IntentResultContainerVys5NeverOA3EGAA0cD0HPyHC
- -[QLFullscreenController setSidecarSwipeRecognizer:]
- -[QLFullscreenController sidecarSwipeRecognizer]
- -[QLOverlayGlassBackground initWithSize:expandedSize:]
- -[QLPanelPreviewPanGestureRecognizer acceptsFirstMouse:]
- -[QLPreviewDragController startDraggingWithGestureRecognizer:beganOrFailedHandler:]
- -[QLPreviewOverlayController _setShowOverlay:dimmed:]
- -[QLPreviewPanelController forwardedSwipeFilter]
- -[QLPreviewPanelController setForwardedSwipeFilter:]
- -[QLPreviewTitleBarView gestureRecognizer:shouldReceiveTouch:]
- -[QLPreviewTitleBarView handleLongPress:]
- -[QLPreviewTitleBarView handleTap:]
- -[QLPreviewTitleBarView showStopLightZoomUI]
- -[QLPreviewView startDragFromGesture:beganOrFailedHandler:]
- -[QLSidecarSwipeSampleFilter addSample:]
- -[QLSidecarSwipeSampleFilter initWithInitialPosition:]
- -[QLSidecarSwipeSampleFilter isEnabled]
- -[QLSidecarSwipeSampleFilter position]
- -[QLSidecarSwipeSampleFilter setEnabled:]
- -[QLUIServiceBaseViewController setSidecarSwipeRecognizer:]
- -[QLUIServiceBaseViewController sidecarSwipeRecognizer]
- GCC_except_table105
- GCC_except_table108
- GCC_except_table119
- GCC_except_table152
- GCC_except_table227
- GCC_except_table269
- OBJC_IVAR_$_QLFullscreenController._controlsPanel
- OBJC_IVAR_$_QLFullscreenController._sidecarSwipeRecognizer
- OBJC_IVAR_$_QLPreviewPanelController._forwardedSwipeFilter
- OBJC_IVAR_$_QLPreviewPanelController._swipeContainerWindow
- OBJC_IVAR_$_QLPreviewSwipeController._cid
- OBJC_IVAR_$_QLPreviewSwipeController._fullscreenAndOnlyOneScreen
- OBJC_IVAR_$_QLPreviewSwipeController._previewFrame
- OBJC_IVAR_$_QLPreviewSwipeController._transitionWindow
- OBJC_IVAR_$_QLPreviewSwipeController._wid
- OBJC_IVAR_$_QLPreviewTitleBarView._clickRecognizer
- OBJC_IVAR_$_QLPreviewTitleBarView._longPressRecognizer
- OBJC_IVAR_$_QLPreviewTitleBarView._stoplightZoomUIController
- OBJC_IVAR_$_QLSidecarSwipeSampleFilter._enabled
- OBJC_IVAR_$_QLSidecarSwipeSampleFilter._position
- OBJC_IVAR_$_QLSidecarSwipeSampleFilter._rawPrev1
- OBJC_IVAR_$_QLSidecarSwipeSampleFilter._rawPrev2
- OBJC_IVAR_$_QLSidecarSwipeSampleFilter._rejectionCount
- OBJC_IVAR_$_QLUIServiceBaseViewController._sidecarSwipeRecognizer
- QLSidecarMultiItemSwipeEnabled
- QLSidecarMultiItemSwipeEnabled._sidecarMultiItemSwipeEnabled
- QLSidecarMultiItemSwipeEnabled.onceToken
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
- ___37-[QLPreviewView receivedDragGesture:]_block_invoke
- ___53-[QLUIServiceBaseViewController receivedDragGesture:]_block_invoke
- ___59-[QLPreviewView startDragFromGesture:beganOrFailedHandler:]_block_invoke
- ___83-[QLPreviewDragController startDraggingWithGestureRecognizer:beganOrFailedHandler:]_block_invoke
- ___QLSidecarMultiItemSwipeEnabled_block_invoke
- ___block_descriptor_72_e8_32s40s48s56s64bs_e51_v48?0"NSImage"8{CGRect={CGPoint=dd}{CGSize=dd}}16l
- _objc_msgSend$_setShowOverlay:dimmed:
- _objc_msgSend$addSample:
- _objc_msgSend$allTouches
- _objc_msgSend$forwardedSwipeFilter
- _objc_msgSend$initWithInitialPosition:
- _objc_msgSend$initWithSize:expandedSize:
- _objc_msgSend$setDraggingFrame:contents:
- _objc_msgSend$setForwardedSwipeFilter:
- _objc_msgSend$setSidecarSwipeRecognizer:
- _objc_msgSend$setWindowServerAware:
- _objc_msgSend$showMenu
- _objc_msgSend$showStopLightZoomUI
- _objc_msgSend$sidecarSwipeRecognizer
- _objc_msgSend$stage
- _objc_msgSend$startDragFromGesture:beganOrFailedHandler:
- _objc_msgSend$startDraggingWithGestureRecognizer:beganOrFailedHandler:
CStrings:
+ "%@ failed to forward sidecar swipe to host: %@"
+ "@\"NSArray\"8@?0"
+ "B24@?0@\"NSTouch\"8@\"NSEvent\"16"
+ "HUD toggle (recognizer: %p): visible: %d, fading out: %d, hide timer armed: %d"
+ "HUD toggle ignored: duplicate tap report %.3fs after the last toggle (recognizer: %p)"
+ "HUD toggle: hiding controls"
+ "HUD toggle: showing controls and scheduling auto-hide"
+ "NSWindowResizePanGestureRecognizer"
+ "QLFullscreenController.controlsPanelDragRecognizer"
+ "QLInlinePreviewTemporaryControlsRevealDuration"
+ "QLPreviewView.dragTouchGestureRecognizer"
+ "QLUIServiceBaseViewController.dragTouch"
+ "Resolve Document"
+ "Scrubber"
+ "[touch-debug] %p hideOverlay remoteOwns=%d"
+ "[touch-debug] %p showOverlayMomentarily remoteOwns=%d"
+ "[touch-debug] DBVC hideOverlayControls"
+ "[touch-debug] DBVC overlayControlsTapAtPoint %{public}@ controller=%p revealed=%d pressed=%d page=%lu/%lu"
+ "[touch-debug] DBVC showOverlayControlsMomentarily controller=%p"
+ "[touch-debug] overlay %p goToNextPage page=%lu/%lu"
+ "[touch-debug] overlay %p hit %{public}@ at %{public}@ dequeue=%d overlayLayerFrame=%{public}@"
+ "_NSGlassTrackingWindow"
+ "_NSScrollAxisAwareLeftMouseDragGestureRecognizer"
+ "com.apple.MobileSMS"
+ "com.apple.Preview"
+ "com.apple.QuickLookUIFramework"
+ "swipeAvailable"
+ "v16@?0@8"
+ "\xd2"
+ "\xf0\xf0\xc1"
- "%@ handleLongPress state is %lx"
- "%@ handleTap"
- "&"
- "------ shouldReceiveTouch: %@"
- "NSStoplightZoomUIController"
- "QLFullscreenController.m"
- "QLPreviewTitleBarView.clickGestureRecognizer"
- "QLPreviewTitleBarView.longPressGestureRecognizer"
- "QLSidecarMultiItemSwipeEnabled"
- "QLSidecarSwipeFilterEnabled"
- "Received simulated swipe point %@"
- "\xf0B"
- "\xf0\xf0\xb1"
```
