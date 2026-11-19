## UIKitMacHelper

> `/System/Library/PrivateFrameworks/UIKitMacHelper.framework/Versions/A/UIKitMacHelper`

```diff

-9127.0.84.1.406
-  __TEXT.__text: 0xb93f0
-  __TEXT.__objc_methlist: 0xe5e0
-  __TEXT.__const: 0x7e8
-  __TEXT.__dlopen_cstrs: 0x6a6
-  __TEXT.__cstring: 0xd4d1
+9127.1.13.1.411
+  __TEXT.__text: 0xbc0e0
+  __TEXT.__objc_methlist: 0xe800
+  __TEXT.__const: 0x7d8
+  __TEXT.__dlopen_cstrs: 0x737
+  __TEXT.__cstring: 0xd9b6
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__oslogstring: 0x5ada
-  __TEXT.__gcc_except_tab: 0x16dc
+  __TEXT.__oslogstring: 0x5d12
+  __TEXT.__gcc_except_tab: 0x1804
   __TEXT.__ustring: 0x52
-  __TEXT.__unwind_info: 0x2de8
+  __TEXT.__unwind_info: 0x2ea8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd20
+  __DATA_CONST.__const: 0xd60
   __DATA_CONST.__objc_classlist: 0x658
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_nlcatlist: 0x10
   __DATA_CONST.__objc_protolist: 0x2b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x85d0
+  __DATA_CONST.__objc_selrefs: 0x8740
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x458
   __DATA_CONST.__objc_arraydata: 0x158
-  __DATA_CONST.__got: 0xc40
-  __AUTH_CONST.__const: 0x2ea0
-  __AUTH_CONST.__cfstring: 0x8ac0
-  __AUTH_CONST.__objc_const: 0x17770
+  __DATA_CONST.__got: 0xc48
+  __AUTH_CONST.__const: 0x2e80
+  __AUTH_CONST.__cfstring: 0x8ce0
+  __AUTH_CONST.__objc_const: 0x17a20
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x29e0
   __AUTH.__data: 0xa0
-  __DATA.__objc_ivar: 0xba4
+  __DATA.__objc_ivar: 0xbd0
   __DATA.__data: 0x20e8
-  __DATA.__bss: 0x1c0
+  __DATA.__bss: 0x1c8
   __DATA.__common: 0x48
-  __DATA_DIRTY.__objc_ivar: 0x4b0
+  __DATA_DIRTY.__objc_ivar: 0x4c0
   __DATA_DIRTY.__objc_data: 0x1540
   __DATA_DIRTY.__data: 0x40
-  __DATA_DIRTY.__bss: 0x8e8
+  __DATA_DIRTY.__bss: 0x938
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4645
-  Symbols:   11740
-  CStrings:  1955
+  Functions: 4704
+  Symbols:   11853
+  CStrings:  1996
 
Symbols:
+ -[UINSDragManager _beginDragInSceneView:withItems:event:orTouchIndex:andContextID:menu:handler:]
+ -[UINSDragManager _resumeTouchDraggingSessionWrapper:]
+ -[UINSDragManager _sessionWrapperForDraggingSession:]
+ -[UINSDragManager beginDragInSceneView:withItems:touchIndex:contextID:menu:handler:]
+ -[UINSDragManager dragContextMenuController:willDismissContextMenuToYield:]
+ -[UINSDragManager dragContextMenuControllerWillCancelDragToTrackContextMenu:]
+ -[UINSDragTrackingGestureRecognizer acceptsFirstTouch:event:]
+ -[UINSDropSession isSuspended]
+ -[UINSDropSession lastKnownDraggingInfo]
+ -[UINSDropSession reconstructDataProvidersFromResumedDraggingInfo:sceneView:]
+ -[UINSDropSession setLastKnownDraggingInfo:]
+ -[UINSDropSession setSuspended:]
+ -[UINSLocalSceneHostingView _destroyLocalSceneIfNecessary]
+ -[UINSLocalSceneHostingView _setWindowResizeAnchorContentLayerContextID:renderID:]
+ -[UINSLocalSceneHostingView _startObservingKVO]
+ -[UINSLocalSceneHostingView _stopObservingKVO]
+ -[UINSLocalSceneHostingView _updateResizeAnchorContentLayer]
+ -[UINSLocalSceneHostingView _windowContextDidChange:]
+ -[UINSLocalSceneHostingView _windowSceneResizeAnchorContentViewDidChange:]
+ -[UINSLocalSceneHostingView dealloc]
+ -[UINSLocalSceneHostingView observeValueForKeyPath:ofObject:change:context:]
+ -[UINSLocalSceneHostingView observedRunningApplication]
+ -[UINSLocalSceneHostingView parentSceneWillInvalidate:]
+ -[UINSLocalSceneHostingView safeToVendNotificationObserver]
+ -[UINSLocalSceneHostingView setObservedRunningApplication:]
+ -[UINSLocalSceneHostingView setSafeToVendNotificationObserver:]
+ -[UINSLocalSceneHostingViewFBSSceneObserver sceneWillInvalidate:]
+ -[UINSMenuController setUpContextMenuForPresentation:inWindow:atLocationInWindow:activityItemsConfiguration:]
+ -[UINSMenuController tearDownContextMenuAfterPresentation:]
+ -[UINSMouseEventTranslator cancelDirectTouchesWithEvent:]
+ -[UINSSceneView(Dropping) endSuspendedDropSessionWithSessionID:]
+ -[UINSSceneView(Dropping) suspendDropSessionWithSessionID:]
+ -[UINSTouchGestureRecognizer lastTouchEvent]
+ -[UINSTouchGestureRecognizer reset]
+ -[UINSWindowProxy _touchAtPointShouldDragWindow:]
+ -[UINSWindowProxy beginDragWithItems:touchIndex:contextID:menu:handler:]
+ -[_UINSSessionWrapper contextMenuController]
+ -[_UINSSessionWrapper dragItems]
+ -[_UINSSessionWrapper hasSuspendedDropSession]
+ -[_UINSSessionWrapper locationInSceneView]
+ -[_UINSSessionWrapper modifierFlags]
+ -[_UINSSessionWrapper sceneView]
+ -[_UINSSessionWrapper sessionID]
+ -[_UINSSessionWrapper setContextMenuController:]
+ -[_UINSSessionWrapper setDragItems:]
+ -[_UINSSessionWrapper setHasSuspendedDropSession:]
+ -[_UINSSessionWrapper setLocationInSceneView:]
+ -[_UINSSessionWrapper setModifierFlags:]
+ -[_UINSSessionWrapper setSceneView:]
+ -[_UINSSessionWrapper setSessionID:]
+ GCC_except_table104
+ GCC_except_table32
+ GCC_except_table35
+ GCC_except_table66
+ GCC_except_table74
+ GCC_except_table87
+ OBJC_IVAR_$_UINSDragManager._commandeeredTouchesDidEnd
+ OBJC_IVAR_$_UINSDragManager._didEndCommandeeringTouchNotificationObserver
+ OBJC_IVAR_$_UINSDragManager._suspendedSessionWrapper
+ OBJC_IVAR_$_UINSDropSession._isSuspended
+ OBJC_IVAR_$_UINSDropSession._lastKnownDraggingInfo
+ OBJC_IVAR_$_UINSSheetManager._sheetWindowPresentationObserver
+ OBJC_IVAR_$__UINSSessionWrapper._contextMenuController
+ OBJC_IVAR_$__UINSSessionWrapper._dragItems
+ OBJC_IVAR_$__UINSSessionWrapper._hasSuspendedDropSession
+ OBJC_IVAR_$__UINSSessionWrapper._locationInSceneView
+ OBJC_IVAR_$__UINSSessionWrapper._modifierFlags
+ OBJC_IVAR_$__UINSSessionWrapper._sceneView
+ OBJC_IVAR_$__UINSSessionWrapper._sessionID
+ _CALayerGetRenderId
+ _NSDefaultRunLoopMode
+ _UINSMenuControllerDidDismissContextMenuNotification
+ _UINSSceneRoleIsMenuBarHostedPresentation
+ _UINSWindowProxyDidAttachToWindow
+ __61-[UINSSheetManager sceneHostingViewControllerDidCreateScene:]_block_invoke
+ __OBJC_$_PROP_LIST_UINSTouchGestureRecognizer
+ __UINSDragSessionIDForDraggingInfo
+ __UINSDragSessionIDForSequenceAndContext
+ ___58-[UINSLocalSceneHostingView _destroyLocalSceneIfNecessary]_block_invoke
+ ___59-[UINSMenuController tearDownContextMenuAfterPresentation:]_block_invoke
+ ___77-[UINSDropSession reconstructDataProvidersFromResumedDraggingInfo:sceneView:]_block_invoke
+ ___96-[UINSDragManager _beginDragInSceneView:withItems:event:orTouchIndex:andContextID:menu:handler:]_block_invoke
+ ___UINSSceneRoleIsMenuBarHostedPresentation_block_invoke
+ ____NSDragContextMenuControllerClass_block_invoke
+ ____updateDragPreviewItems_block_invoke
+ ____updateDragPreviewItems_block_invoke_2
+ ___block_descriptor_40_e8_32s_e35_v16?0"FBSSceneTransitionContext"8l
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSEvent"8l
+ ___getNSWindowSheetDidPresentNotification_block_invoke
+ ___getUIDestroySceneActionClass_block_invoke
+ ___get_UIWindowDidAttachContextNotificationSymbolLoc_block_invoke
+ ___get_UIWindowDidDetachContextNotificationSymbolLoc_block_invoke
+ ___get_UIWindowFirstResponderUserInfoKeySymbolLoc_block_invoke
+ ___get_UIWindowSceneResizeAnchorContentViewDidChangeNotificationSymbolLoc_block_invoke
+ __nsDraggingItemsFromUINSDragItems
+ __updateDragPreviewItems
+ _draggingSequenceNumberMapping
+ _getNSWindowSheetDidPresentNotification
+ _objc_msgSend$_destroyLocalSceneIfNecessary
+ _objc_msgSend$_gestureStartLocation
+ _objc_msgSend$_resizeAnchorContentView
+ _objc_msgSend$_setGestureStartLocation:
+ _objc_msgSend$_setResizeAnchorContentLayerContextID:renderID:
+ _objc_msgSend$_setWindowResizeAnchorContentLayerContextID:renderID:
+ _objc_msgSend$_startObservingKVO
+ _objc_msgSend$_stopObservingKVO
+ _objc_msgSend$_touchAtPointShouldDragWindow:
+ _objc_msgSend$_updateResizeAnchorContentLayer
+ _objc_msgSend$beginDragInSceneView:withItems:touchIndex:contextID:menu:handler:
+ _objc_msgSend$beginTouchDraggingSessionWithItems:source:locationInView:modifierFlags:
+ _objc_msgSend$cancelDirectTouchesWithEvent:
+ _objc_msgSend$dragItems
+ _objc_msgSend$draggingSession
+ _objc_msgSend$draggingSession:endedAtPoint:operation:
+ _objc_msgSend$endSuspendedDropSessionWithSessionID:
+ _objc_msgSend$hasSuspendedDropSession
+ _objc_msgSend$initWithObjects:
+ _objc_msgSend$initWithPersistedIdentifiers:preferredAnimationType:callbackQueue:completion:
+ _objc_msgSend$invalidate:
+ _objc_msgSend$isSuspended
+ _objc_msgSend$isValid
+ _objc_msgSend$lastKnownDraggingInfo
+ _objc_msgSend$lastTouchEvent
+ _objc_msgSend$locationInSceneView
+ _objc_msgSend$observedRunningApplication
+ _objc_msgSend$parentSceneWillInvalidate:
+ _objc_msgSend$performSelector:withObject:afterDelay:inModes:
+ _objc_msgSend$reconstructDataProvidersFromResumedDraggingInfo:sceneView:
+ _objc_msgSend$setContextMenu:
+ _objc_msgSend$setContextMenuController:
+ _objc_msgSend$setDragItems:
+ _objc_msgSend$setHasSuspendedDropSession:
+ _objc_msgSend$setLastKnownDraggingInfo:
+ _objc_msgSend$setLocationInSceneView:
+ _objc_msgSend$setMenuReplaysTouchesAfterAutoDismissal:
+ _objc_msgSend$setModifierFlags:
+ _objc_msgSend$setObservedRunningApplication:
+ _objc_msgSend$setSessionID:
+ _objc_msgSend$setSuspended:
+ _objc_msgSend$setTitlebarHandlesDoubleClickWhenTransparent:
+ _objc_msgSend$setUpContextMenuForPresentation:inWindow:atLocationInWindow:activityItemsConfiguration:
+ _objc_msgSend$setWaitForCatalystGate:
+ _objc_msgSend$suspendDropSessionWithSessionID:
+ _objc_msgSend$tearDownContextMenuAfterPresentation:
- -[UINSDragManager _beginDragInSceneView:withItems:event:orTouchIndex:handler:]
- -[UINSDragManager _indexForDraggingSession:]
- -[UINSDragManager beginDragInSceneView:withItems:touchIndex:handler:]
- -[UINSEventTranslator directTouchesWithEvent:]
- -[UINSWindowProxy beginDragWithItems:touchIndex:handler:]
- -[UINSWindowStateController _isPodcasts]
- -[UINSWindowStateController sceneIDWeHidInsteadOfClosing]
- -[UINSWindowStateController setSceneIDWeHidInsteadOfClosing:]
- GCC_except_table28
- GCC_except_table65
- GCC_except_table76
- GCC_except_table89
- OBJC_IVAR_$_UINSTouchGestureRecognizer._outstandingEvents
- OBJC_IVAR_$_UINSWindowStateController._sceneIDWeHidInsteadOfClosing
- ___40-[UINSWindowStateController _isPodcasts]_block_invoke
- ___44-[UINSDragManager _indexForDraggingSession:]_block_invoke
- ___47-[UINSWindow _wantsFullScreenCleanupOnOrderOut]_block_invoke
- ___60-[UINSDropSession initWithDraggingInfo:sessionID:sceneView:]_block_invoke
- ___78-[UINSDragManager _beginDragInSceneView:withItems:event:orTouchIndex:handler:]_block_invoke
- ___78-[UINSDragManager _beginDragInSceneView:withItems:event:orTouchIndex:handler:]_block_invoke_2
- ___block_descriptor_40_e8_32s_e17_v16?0"NSEvent"8l
- ___block_descriptor_40_e8_32s_e36_B32?0"_UINSSessionWrapper"8Q16^B24l
- ___getIOSTranslatorClass_block_invoke
- ___getMacPlatformElementClass_block_invoke
- _objc_msgSend$_indexForDraggingSession:
- _objc_msgSend$_isPodcasts
- _objc_msgSend$_unhideWindowForScene:
- _objc_msgSend$beginDragInSceneView:withItems:touchIndex:handler:
- _objc_msgSend$sceneIDWeHidInsteadOfClosing
- _objc_msgSend$setSceneIDWeHidInsteadOfClosing:
- _objc_msgSend$touchesForView:
CStrings:
+ "\f"
+ "+"
+ "/System/Library/Frameworks/AppKit.framework/Versions/Current/AppKit"
+ "BOOL UINSSceneRoleIsMenuBarHostedPresentation(UIScene *__strong _Nonnull)"
+ "Cannot find session to unsuspend: %lld"
+ "Class getUIDestroySceneActionClass(void)_block_invoke"
+ "Context menu dismissed. Resuming drag. Suspended session wrapper: %@"
+ "Ending drag session. Session wrapper: %@"
+ "Existing drop session was suspended, so unsuspending it to resume tracking drop. %lld"
+ "Failed to resume session."
+ "Ignoring drop session ending because the session is suspended: %lld"
+ "Ignoring ended session %@"
+ "Manually ending suspended drop session: %lld"
+ "NSDidEndCommandeeringTouchNotification"
+ "NSDragContextMenuController"
+ "NSNotificationName get_UIWindowDidAttachContextNotification(void)"
+ "NSNotificationName get_UIWindowDidDetachContextNotification(void)"
+ "NSNotificationName get_UIWindowSceneResizeAnchorContentViewDidChangeNotification(void)"
+ "NSString *get_UIWindowFirstResponderUserInfoKey(void)"
+ "NSWindow.backgroundWindowDrag"
+ "NSWindowSheetDidPresentNotification"
+ "Not resuming session because touches have ended. Ending it instead."
+ "Resuming drag session. Session wrapper: %@"
+ "Session %lld is already suspended. Cannot suspend it again."
+ "Session %lld was not suspended. Cannot end it manually."
+ "Session does not have a dragging info since it was suspended: %lld"
+ "Suspended drag session was cancelled. Suspended session wrapper: %@"
+ "Suspending drag for context menu. Suspended session wrapper: %@"
+ "Suspending drop session: %lld"
+ "UIDestroySceneAction"
+ "UINSDragManager.m"
+ "UINSMenuControllerDidDismissContextMenuNotification"
+ "UINSSceneViewDropping.m"
+ "UINSWindowProxyDidAttachToWindow"
+ "_NSAccessibilitySafeToVendDidBecomeAvailable"
+ "_UINSLocalSceneHostingViewPolicyWatchingContext"
+ "_UIWindowDidAttachContextNotification"
+ "_UIWindowDidDetachContextNotification"
+ "_UIWindowFirstResponderUserInfoKey"
+ "_UIWindowSceneResizeAnchorContentViewDidChangeNotification"
+ "bannerFloating"
+ "integratedCompactLeading"
+ "integratedCompactTrailing"
+ "integratedExpanded"
+ "integratedMinimal"
+ "v16@?0@\"FBSSceneTransitionContext\"8"
- "%s: We have a previous hidden window!"
- "-[UINSWindowStateController _closeOrHideWindowWithScene:]"
- "B32@?0@\"_UINSSessionWrapper\"8Q16^B24"
- "Hiding last window, without termination"
- "com.apple.podcasts"
```
