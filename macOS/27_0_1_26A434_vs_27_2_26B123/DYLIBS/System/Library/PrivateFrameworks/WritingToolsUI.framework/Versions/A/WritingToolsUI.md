## WritingToolsUI

> `/System/Library/PrivateFrameworks/WritingToolsUI.framework/Versions/A/WritingToolsUI`

```diff

-149.503.0.0.0
-  __TEXT.__text: 0x5b1c0
-  __TEXT.__objc_methlist: 0x3464
+151.1.11.500.0
+  __TEXT.__text: 0x5c6fc
+  __TEXT.__objc_methlist: 0x3544
   __TEXT.__const: 0x2cd4
-  __TEXT.__cstring: 0x2ae2
-  __TEXT.__gcc_except_tab: 0x86c
-  __TEXT.__oslogstring: 0x10a5
+  __TEXT.__cstring: 0x2bb2
+  __TEXT.__gcc_except_tab: 0x8d0
+  __TEXT.__oslogstring: 0x1345
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__swift5_typeref: 0x926e
-  __TEXT.__swift5_reflstr: 0x9ac
+  __TEXT.__swift5_reflstr: 0x9cc
   __TEXT.__swift5_assocty: 0x1e8
   __TEXT.__constg_swiftt: 0xae0
-  __TEXT.__swift5_fieldmd: 0x864
+  __TEXT.__swift5_fieldmd: 0x870
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_capture: 0x374
   __TEXT.__swift5_proto: 0x170

   __TEXT.__swift_as_entry: 0x48
   __TEXT.__swift_as_cont: 0x40
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__unwind_info: 0x1720
-  __TEXT.__eh_frame: 0xa68
+  __TEXT.__unwind_info: 0x17b0
+  __TEXT.__eh_frame: 0xac0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x248
+  __DATA_CONST.__const: 0x258
   __DATA_CONST.__objc_classlist: 0x150
-  __DATA_CONST.__objc_catlist: 0x38
+  __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2918
+  __DATA_CONST.__objc_selrefs: 0x29e8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x88
-  __DATA_CONST.__got: 0x970
-  __AUTH_CONST.__const: 0x2920
-  __AUTH_CONST.__cfstring: 0xfc0
-  __AUTH_CONST.__objc_const: 0x4de8
+  __DATA_CONST.__got: 0x9a0
+  __AUTH_CONST.__const: 0x2980
+  __AUTH_CONST.__cfstring: 0x1020
+  __AUTH_CONST.__objc_const: 0x4ef8
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__auth_got: 0xe58
+  __AUTH_CONST.__auth_got: 0xe70
   __AUTH_CONST.__auth_ptr: 0x818
   __AUTH.__objc_data: 0xd90
   __AUTH.__data: 0x808
-  __DATA.__objc_ivar: 0x2e8
-  __DATA.__data: 0x15d0
+  __DATA.__objc_ivar: 0x2f8
+  __DATA.__data: 0x1618
   __DATA.__bss: 0x30f0
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2174
-  Symbols:   3810
-  CStrings:  404
+  Functions: 2207
+  Symbols:   3879
+  CStrings:  418
 
Symbols:
+ +[WTFeedbackProxy sendComposeFeedback:range:finished:compositionSessionType:]
+ +[WTWritingToolsViewController _responderTargetForAction:inWindow:]
+ -[NSUndoManager(WTTurnTracking) wt_registerTurnWithHandler:]
+ -[NSUndoManager(WTTurnTracking) wt_registerUndoIfPossibleWithTarget:handler:]
+ -[WTWritingTools _updateUserInterfaceVisibilityIfNeeded]
+ -[WTWritingTools dealloc]
+ -[WTWritingTools isUserInterfaceVisible]
+ -[WTWritingTools lastKnownUserInterfaceVisible]
+ -[WTWritingTools noteUserInterfaceVisibilityMayHaveChanged]
+ -[WTWritingTools popoverVisibilityObservers]
+ -[WTWritingTools setLastKnownUserInterfaceVisible:]
+ -[WTWritingTools setPopoverVisibilityObservers:]
+ -[WTWritingToolsRemoteViewController _installUndoInterceptionKeyEventMonitorIfNeeded]
+ -[WTWritingToolsRemoteViewController _registerUndoTrackingTurnOnUndoManager:]
+ -[WTWritingToolsRemoteViewController dealloc]
+ -[WTWritingToolsRemoteViewController performRequestedTool:precomputedData:]
+ -[WTWritingToolsRemoteViewController setUndoInterceptionKeyEventMonitor:]
+ -[WTWritingToolsRemoteViewController undoInterceptionKeyEventMonitor]
+ -[WTWritingToolsViewController(WTWritingToolsPanel) isVisible]
+ -[_WTReplaceTextEffect clipsToDestinationRect]
+ -[_WTReplaceTextEffect setClipsToDestinationRect:]
+ -[_WTTextEffectView hasManagedFrame]
+ -[_WTTextEffectView replaceSourceEffect]
+ -[_WTTextEffectView setHasManagedFrame:]
+ -[_WTTextEffectView setReplaceSourceEffect:]
+ GCC_except_table100
+ GCC_except_table106
+ GCC_except_table119
+ GCC_except_table179
+ GCC_except_table193
+ GCC_except_table221
+ GCC_except_table4
+ GCC_except_table6
+ GCC_except_table89
+ GCC_except_table91
+ OBJC_IVAR_$_WTWritingTools._lastKnownUserInterfaceVisible
+ OBJC_IVAR_$_WTWritingTools._popoverVisibilityObservers
+ OBJC_IVAR_$_WTWritingToolsRemoteViewController._undoInterceptionKeyEventMonitor
+ OBJC_IVAR_$__WTReplaceTextEffect._clipsToDestinationRect
+ OBJC_IVAR_$__WTTextEffectView._hasManagedFrame
+ OBJC_IVAR_$__WTTextEffectView._replaceSourceEffect
+ _NSInternalInconsistencyException
+ _NSPopoverDidCloseNotification
+ _NSPopoverDidShowNotification
+ _NSPopoverWillCloseNotification
+ _OBJC_CLASS_$_NSUndoManager
+ _OBJC_CLASS_$_WTPrecomputedData
+ _WTWritingToolsUserInterfaceVisibilityDidChangeNotification
+ _WTWritingToolsViewControllerEnhancedSiriAvailabilityDidChangeNotification
+ __116-[WTWritingToolsRemoteViewController _showAlwaysOnProofreadingSuggestionsInProcess:selectedIndex:anchor:sourceView:]_block_invoke_2
+ __75-[WTWritingToolsRemoteViewController performRequestedTool:precomputedData:]_block_invoke
+ __77-[WTWritingToolsRemoteViewController _registerUndoTrackingTurnOnUndoManager:]_block_invoke
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSUndoManager_$_WTTurnTracking
+ __OBJC_$_CATEGORY_NSUndoManager_$_WTTurnTracking
+ ___29-[WTWritingTools setPopover:]_block_invoke
+ ___60-[NSUndoManager(WTTurnTracking) wt_registerTurnWithHandler:]_block_invoke
+ ___75-[WTWritingToolsRemoteViewController performRequestedTool:precomputedData:]_block_invoke
+ ___77-[WTWritingToolsRemoteViewController _registerUndoTrackingTurnOnUndoManager:]_block_invoke
+ ___85-[WTWritingToolsRemoteViewController _installUndoInterceptionKeyEventMonitorIfNeeded]_block_invoke
+ ___block_descriptor_40_e8_32bs_e23_v16?0"NSUndoManager"8l
+ ___block_descriptor_40_e8_32w_e26_"NSEvent"16?0"NSEvent"8l
+ _objc_exception_rethrow
+ _objc_msgSend$_installUndoInterceptionKeyEventMonitorIfNeeded
+ _objc_msgSend$_registerUndoTrackingTurnOnUndoManager:
+ _objc_msgSend$_responderTargetForAction:inWindow:
+ _objc_msgSend$_updateUserInterfaceVisibilityIfNeeded
+ _objc_msgSend$charactersIgnoringModifiers
+ _objc_msgSend$clipsToDestinationRect
+ _objc_msgSend$groupingLevel
+ _objc_msgSend$groupsByEvent
+ _objc_msgSend$hasManagedFrame
+ _objc_msgSend$initWithPrecomputedResultText:precomputedCitationsJSON:precomputedContentAdvisoriesJSON:precomputedResultReplacesExisting:
+ _objc_msgSend$isUndoing
+ _objc_msgSend$isUserInterfaceVisible
+ _objc_msgSend$isVisible
+ _objc_msgSend$lastKnownUserInterfaceVisible
+ _objc_msgSend$name
+ _objc_msgSend$noteUserInterfaceVisibilityMayHaveChanged
+ _objc_msgSend$performRequestedTool:precomputedData:
+ _objc_msgSend$popoverVisibilityObservers
+ _objc_msgSend$postNotificationName:object:
+ _objc_msgSend$registerUndoWithTarget:handler:
+ _objc_msgSend$replaceSourceEffect
+ _objc_msgSend$sendComposeFeedback:range:finished:compositionSessionType:
+ _objc_msgSend$setClipsToDestinationRect:
+ _objc_msgSend$setLastKnownUserInterfaceVisible:
+ _objc_msgSend$setMasksToBounds:
+ _objc_msgSend$setPopoverVisibilityObservers:
+ _objc_msgSend$setReplaceSourceEffect:
+ _objc_msgSend$setUndoInterceptionKeyEventMonitor:
+ _objc_msgSend$supplementalTargetForAction:sender:
+ _objc_msgSend$systemRedColor
+ _objc_msgSend$undoInterceptionKeyEventMonitor
+ _objc_msgSend$wt_registerTurnWithHandler:
+ _objc_msgSend$wt_registerUndoIfPossibleWithTarget:handler:
- +[WTFeedbackProxy sendComposeFeedback:range:finished:]
- +[WTFeedbackProxy sendRewriteFeedback:range:finished:]
- -[WTWritingToolsRemoteViewController performRequestedTool:]
- -[WTWritingToolsViewController redoObserver]
- -[WTWritingToolsViewController setRedoObserver:]
- -[WTWritingToolsViewController setUndoObserver:]
- -[WTWritingToolsViewController undoObserver]
- GCC_except_table111
- GCC_except_table172
- GCC_except_table186
- GCC_except_table217
- GCC_except_table92
- OBJC_IVAR_$_WTWritingToolsViewController._redoObserver
- OBJC_IVAR_$_WTWritingToolsViewController._undoObserver
- _NSUndoManagerDidRedoChangeNotification
- _NSUndoManagerDidUndoChangeNotification
- __43-[WTWritingToolsViewController viewDidLoad]_block_invoke
- __59-[WTWritingToolsRemoteViewController performRequestedTool:]_block_invoke
- ___43-[WTWritingToolsViewController viewDidLoad]_block_invoke_2
- ___59-[WTWritingToolsRemoteViewController performRequestedTool:]_block_invoke
- _objc_msgSend$performRequestedTool:
- _objc_msgSend$sendComposeFeedback:range:finished:
- _objc_msgSend$sendRewriteFeedback:range:finished:
- _objc_msgSend$setIgnoresMouseEvents:
- _objc_msgSend$setRedoObserver:
- _objc_msgSend$setUndoObserver:
CStrings:
+ "("
+ "1\x81"
+ "DebugForceUnsafeOutput"
+ "Error getting serviceViewControllerProxy to call `-performRequestedTool:precomputedData:` : %@"
+ "N"
+ "WTWritingToolsUserInterfaceVisibilityDidChangeNotification"
+ "WTWritingToolsViewControllerEnhancedSiriAvailabilityDidChangeNotification"
+ "Y"
+ "_registerUndoTrackingTurnOnUndoManager: %@"
+ "undo tracking turn fired: isUndo=%s remainingUndoCount=%lu remainingRedoCount=%lu"
+ "undo tracking turn reconciled: remainingUndoCount=%lu remainingRedoCount=%lu"
+ "undo tracking: last tracked turn undone, ending Writing Tools"
+ "undoInterceptionKeyEventMonitor: installing for session %@"
+ "undoInterceptionKeyEventMonitor: intercepted Cmd+Z during pending Proofread review — canceling review instead of forwarding to the real undo manager"
+ "undoInterceptionKeyEventMonitor: intercepted Cmd+Z while still generating — canceling instead of forwarding to the real undo manager"
+ "undoInterceptionKeyEventMonitor: tearing down"
+ "v16@?0@\"NSUndoManager\"8"
+ "z"
- "'"
- "1\xa1"
- "3"
- "Error getting serviceViewControllerProxy to call `-performRequestedTool:` : %@"
```
