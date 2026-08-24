## UIKitMacHelper

> `/System/Library/PrivateFrameworks/UIKitMacHelper.framework/Versions/A/UIKitMacHelper`

```diff

-9127.0.79.0.0
-  __TEXT.__text: 0xb6a38
-  __TEXT.__objc_methlist: 0xe1d8
-  __TEXT.__const: 0x7d8
+9127.0.84.1.406
+  __TEXT.__text: 0xb93f0
+  __TEXT.__objc_methlist: 0xe5e0
+  __TEXT.__const: 0x7e8
   __TEXT.__dlopen_cstrs: 0x6a6
-  __TEXT.__cstring: 0xd27e
+  __TEXT.__cstring: 0xd4d1
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__oslogstring: 0x5777
-  __TEXT.__gcc_except_tab: 0x16b4
+  __TEXT.__oslogstring: 0x5ada
+  __TEXT.__gcc_except_tab: 0x16dc
   __TEXT.__ustring: 0x52
-  __TEXT.__unwind_info: 0x2d68
+  __TEXT.__unwind_info: 0x2de8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd38
-  __DATA_CONST.__objc_classlist: 0x648
+  __DATA_CONST.__const: 0xd20
+  __DATA_CONST.__objc_classlist: 0x658
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_nlcatlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x2b0
+  __DATA_CONST.__objc_protolist: 0x2b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8410
+  __DATA_CONST.__objc_selrefs: 0x85d0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x450
+  __DATA_CONST.__objc_superrefs: 0x458
   __DATA_CONST.__objc_arraydata: 0x158
-  __DATA_CONST.__got: 0xc38
-  __AUTH_CONST.__const: 0x2e10
-  __AUTH_CONST.__cfstring: 0x8a00
-  __AUTH_CONST.__objc_const: 0x173b0
+  __DATA_CONST.__got: 0xc40
+  __AUTH_CONST.__const: 0x2ea0
+  __AUTH_CONST.__cfstring: 0x8ac0
+  __AUTH_CONST.__objc_const: 0x17770
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x2940
+  __AUTH.__objc_data: 0x29e0
   __AUTH.__data: 0xa0
-  __DATA.__objc_ivar: 0xb7c
-  __DATA.__data: 0x2088
+  __DATA.__objc_ivar: 0xba4
+  __DATA.__data: 0x20e8
   __DATA.__bss: 0x1c0
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_ivar: 0x4b0
   __DATA_DIRTY.__objc_data: 0x1540
   __DATA_DIRTY.__data: 0x40
-  __DATA_DIRTY.__bss: 0x8d8
+  __DATA_DIRTY.__bss: 0x8e8
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4573
-  Symbols:   11583
-  CStrings:  1934
+  Functions: 4645
+  Symbols:   11740
+  CStrings:  1955
 
Symbols:
+ -[UINSAppKitTerminationController deferredTerminationNonCancelability]
+ -[UINSAppKitTerminationController markAppKitTerminationNonCancelableIfDeferred]
+ -[UINSAppKitTerminationController setDeferredTerminationNonCancelability:]
+ -[UINSAppLifecycleState closureConfirmationsApproved_InAction]
+ -[UINSAppLifecycleState closureConfirmationsCanceled_InAction]
+ -[UINSAppLifecycleState closureConfirmationsDidBegin_InAction]
+ -[UINSAppLifecycleStateAwaitingClosureConfirmation _transitionToRunningOrRunningNoOpenWindows]
+ -[UINSAppLifecycleStateAwaitingClosureConfirmation accelerateTerminationSchedule_InAction]
+ -[UINSAppLifecycleStateAwaitingClosureConfirmation allExpectedWindowsDidOpen_InAction]
+ -[UINSAppLifecycleStateAwaitingClosureConfirmation appKitDidActivate_InAction]
+ -[UINSAppLifecycleStateAwaitingClosureConfirmation appKitDidHide_InAction]
+ -[UINSAppLifecycleStateAwaitingClosureConfirmation backgroundTasksCompleted_InAction]
+ -[UINSAppLifecycleStateAwaitingClosureConfirmation closureConfirmationsApproved_InAction]
+ -[UINSAppLifecycleStateAwaitingClosureConfirmation closureConfirmationsCanceled_InAction]
+ -[UINSAppLifecycleStateAwaitingClosureConfirmation closureConfirmationsDidBegin_InAction]
+ -[UINSAppLifecycleStateAwaitingClosureConfirmation init]
+ -[UINSAppLifecycleStateAwaitingClosureConfirmation lastWindowDidClose_InAction]
+ -[UINSAppLifecycleStateAwaitingClosureConfirmation stateEntry_InAction]
+ -[UINSAppLifecycleStateAwaitingClosureConfirmation stateExit_InAction]
+ -[UINSAppLifecycleStateAwaitingClosureConfirmation uiAppDidForeground_InAction]
+ -[UINSAppLifecycleStateRunning closureConfirmationsDidBegin_InAction]
+ -[UINSApplicationLifecycleController anyOpenSceneHasClosureConfirmation]
+ -[UINSApplicationLifecycleController anyOpenSceneHasClosureConfirmation_OutQuery]
+ -[UINSApplicationLifecycleController beginPerWindowClosureConfirmationForScene:]
+ -[UINSApplicationLifecycleController beginTerminationClosureConfirmations_OutAction]
+ -[UINSApplicationLifecycleController closeOrHideWindowWithScene:]
+ -[UINSApplicationLifecycleController closureConfirmationController]
+ -[UINSApplicationLifecycleController closureConfirmationsApproved]
+ -[UINSApplicationLifecycleController closureConfirmationsCanceled]
+ -[UINSApplicationLifecycleController closureConfirmationsDidBegin]
+ -[UINSApplicationLifecycleController isApplicationTerminating]
+ -[UINSApplicationLifecycleController isApplicationTerminating_OutQuery]
+ -[UINSApplicationLifecycleController markAppKitTerminationNonCancelableIfDeferred_OutAction]
+ -[UINSApplicationLifecycleController markSceneClosureApproved:]
+ -[UINSApplicationLifecycleController openScenesWithClosureConfirmation]
+ -[UINSApplicationLifecycleController windowForScene:]
+ -[UINSBridgedSceneBehavior resizeContentAnchorForBridgedScene]
+ -[UINSBridgedSceneBehavior setResizeContentAnchorForBridgedScene:]
+ -[UINSClosureConfirmationController .cxx_destruct]
+ -[UINSClosureConfirmationController _addDialogForScene:]
+ -[UINSClosureConfirmationController _alertForClosureConfirmation:actions:]
+ -[UINSClosureConfirmationController _pendingSceneCount]
+ -[UINSClosureConfirmationController _presentClosureConfirmationForScene:completion:]
+ -[UINSClosureConfirmationController _presentSheetForConfirmation:onWindow:completion:]
+ -[UINSClosureConfirmationController _sceneDidResolve:withOutcome:]
+ -[UINSClosureConfirmationController beginPerWindowClosureConfirmationForScene:]
+ -[UINSClosureConfirmationController beginTerminationClosureConfirmations]
+ -[UINSClosureConfirmationController delegate]
+ -[UINSClosureConfirmationController isTerminationFlow]
+ -[UINSClosureConfirmationController pendingClosureConfirmationScenes]
+ -[UINSClosureConfirmationController setDelegate:]
+ -[UINSClosureConfirmationController setIsTerminationFlow:]
+ -[UINSClosureConfirmationController setPendingClosureConfirmationScenes:]
+ -[UINSLocalSceneHostingViewParentSceneConfiguration resizeContentAnchorHandler]
+ -[UINSLocalSceneHostingViewParentSceneConfiguration setResizeContentAnchorHandler:]
+ -[UINSUIKitBackgroundingController sceneStateTrackingSentinelArrived]
+ -[UINSUIKitBackgroundingController sceneStateTrackingUUID]
+ -[UINSUIKitBackgroundingController setSceneStateTrackingSentinelArrived:]
+ -[UINSUIKitBackgroundingController setSceneStateTrackingUUID:]
+ -[UINSWindowCreatedAction abortForUsageViolation:]
+ -[UINSWindowStateController anyOpenSceneHasClosureConfirmation]
+ -[UINSWindowStateController closeOrHideWindowWithScene:]
+ -[UINSWindowStateController markSceneClosureApproved:]
+ -[UINSWindowStateController openScenesWithClosureConfirmation]
+ -[UINSWindowStateController scenesWithApprovedClosure]
+ -[UINSWindowStateController setScenesWithApprovedClosure:]
+ -[UINSWindowStateController windowForScene:]
+ GCC_except_table101
+ GCC_except_table133
+ GCC_except_table136
+ GCC_except_table144
+ GCC_except_table165
+ GCC_except_table181
+ GCC_except_table194
+ GCC_except_table196
+ GCC_except_table205
+ GCC_except_table209
+ GCC_except_table222
+ GCC_except_table31
+ GCC_except_table40
+ GCC_except_table49
+ GCC_except_table55
+ GCC_except_table64
+ GCC_except_table72
+ GCC_except_table76
+ GCC_except_table78
+ GCC_except_table89
+ OBJC_IVAR_$_UINSAppKitTerminationController._deferredTerminationNonCancelability
+ OBJC_IVAR_$_UINSApplicationLifecycleController._closureConfirmationController
+ OBJC_IVAR_$_UINSBridgedSceneBehavior._resizeContentAnchorForBridgedScene
+ OBJC_IVAR_$_UINSClosureConfirmationController._delegate
+ OBJC_IVAR_$_UINSClosureConfirmationController._isTerminationFlow
+ OBJC_IVAR_$_UINSClosureConfirmationController._pendingClosureConfirmationScenes
+ OBJC_IVAR_$_UINSLocalSceneHostingViewParentSceneConfiguration._resizeContentAnchorHandler
+ OBJC_IVAR_$_UINSUIKitBackgroundingController._sceneStateTrackingSentinelArrived
+ OBJC_IVAR_$_UINSUIKitBackgroundingController._sceneStateTrackingUUID
+ OBJC_IVAR_$_UINSWindowStateController._scenesWithApprovedClosure
+ _OBJC_CLASS_$_BSActionResponder
+ _OBJC_CLASS_$_UINSAppLifecycleStateAwaitingClosureConfirmation
+ _OBJC_CLASS_$_UINSClosureConfirmationController
+ _OBJC_METACLASS_$_UINSAppLifecycleStateAwaitingClosureConfirmation
+ _OBJC_METACLASS_$_UINSClosureConfirmationController
+ __110-[UINSUIKitBackgroundingController _sendSceneStateChangeRequestForSceneIdentifier:newState:completionHandler:]_block_invoke
+ __OBJC_$_INSTANCE_METHODS_UINSAppLifecycleStateAwaitingClosureConfirmation
+ __OBJC_$_INSTANCE_METHODS_UINSClosureConfirmationController
+ __OBJC_$_INSTANCE_VARIABLES_UINSClosureConfirmationController
+ __OBJC_$_PROP_LIST_UINSClosureConfirmationController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UINSClosureConfirmationControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UINSClosureConfirmationControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_UINSClosureConfirmationControllerDelegate
+ __OBJC_CLASS_RO_$_UINSAppLifecycleStateAwaitingClosureConfirmation
+ __OBJC_CLASS_RO_$_UINSClosureConfirmationController
+ __OBJC_LABEL_PROTOCOL_$_UINSClosureConfirmationControllerDelegate
+ __OBJC_METACLASS_RO_$_UINSAppLifecycleStateAwaitingClosureConfirmation
+ __OBJC_METACLASS_RO_$_UINSClosureConfirmationController
+ __OBJC_PROTOCOL_$_UINSClosureConfirmationControllerDelegate
+ ___54-[UINSBridgedScene initWithSession:connectionOptions:]_block_invoke
+ ___56-[UINSClosureConfirmationController _addDialogForScene:]_block_invoke
+ ___84-[UINSClosureConfirmationController _presentClosureConfirmationForScene:completion:]_block_invoke
+ ___86-[UINSClosureConfirmationController _presentSheetForConfirmation:onWindow:completion:]_block_invoke
+ ___block_descriptor_40_e8_32w_e11_v20?0I8Q12l
+ ___block_descriptor_48_e8_32s_e69_v24?0"FBSMutableSceneClientSettings"8"FBSSceneTransitionContext"16l
+ ___block_descriptor_56_e8_32s40s48s_e26_v16?0"BSActionResponse"8l
+ ___block_descriptor_56_e8_32s40s48s_e63_v24?0"FBSMutableSceneSettings"8"FBSSceneTransitionContext"16l
+ _objc_msgSend$_addDialogForScene:
+ _objc_msgSend$_alertForClosureConfirmation:actions:
+ _objc_msgSend$_message
+ _objc_msgSend$_pendingSceneCount
+ _objc_msgSend$_presentClosureConfirmationForScene:completion:
+ _objc_msgSend$_presentSheetForConfirmation:onWindow:completion:
+ _objc_msgSend$_sceneClosureActions
+ _objc_msgSend$_sceneDidResolve:withOutcome:
+ _objc_msgSend$_setResizeContentAnchorContextID:renderID:
+ _objc_msgSend$_title
+ _objc_msgSend$_transitionToRunningOrRunningNoOpenWindows
+ _objc_msgSend$abort
+ _objc_msgSend$addAction:
+ _objc_msgSend$alertAction
+ _objc_msgSend$anyOpenSceneHasClosureConfirmation
+ _objc_msgSend$anyOpenSceneHasClosureConfirmation_OutQuery
+ _objc_msgSend$beginPerWindowClosureConfirmationForScene:
+ _objc_msgSend$beginTerminationClosureConfirmations
+ _objc_msgSend$beginTerminationClosureConfirmations_OutAction
+ _objc_msgSend$closeOrHideWindowWithScene:
+ _objc_msgSend$closureConfirmation
+ _objc_msgSend$closureConfirmationController
+ _objc_msgSend$closureConfirmationsApproved
+ _objc_msgSend$closureConfirmationsApproved_InAction
+ _objc_msgSend$closureConfirmationsCanceled
+ _objc_msgSend$closureConfirmationsCanceled_InAction
+ _objc_msgSend$closureConfirmationsDidBegin
+ _objc_msgSend$closureConfirmationsDidBegin_InAction
+ _objc_msgSend$deferredTerminationNonCancelability
+ _objc_msgSend$isApplicationTerminating
+ _objc_msgSend$isApplicationTerminating_OutQuery
+ _objc_msgSend$isTerminationFlow
+ _objc_msgSend$markAppKitTerminationNonCancelableIfDeferred
+ _objc_msgSend$markAppKitTerminationNonCancelableIfDeferred_OutAction
+ _objc_msgSend$markSceneClosureApproved:
+ _objc_msgSend$openScenesWithClosureConfirmation
+ _objc_msgSend$pendingClosureConfirmationScenes
+ _objc_msgSend$resizeContentAnchorForBridgedScene
+ _objc_msgSend$resizeContentAnchorHandler
+ _objc_msgSend$responderWithHandler:
+ _objc_msgSend$sceneStateTrackingSentinelArrived
+ _objc_msgSend$sceneStateTrackingUUID
+ _objc_msgSend$scenesWithApprovedClosure
+ _objc_msgSend$setCatalystBridgedScene:
+ _objc_msgSend$setDeferredTerminationNonCancelability:
+ _objc_msgSend$setIsTerminationFlow:
+ _objc_msgSend$setPendingClosureConfirmationScenes:
+ _objc_msgSend$setQueue:
+ _objc_msgSend$setResizeContentAnchorHandler:
+ _objc_msgSend$setSceneStateTrackingSentinelArrived:
+ _objc_msgSend$setSceneStateTrackingUUID:
+ _objc_msgSend$windowForScene:
- GCC_except_table100
- GCC_except_table132
- GCC_except_table135
- GCC_except_table143
- GCC_except_table164
- GCC_except_table180
- GCC_except_table193
- GCC_except_table195
- GCC_except_table204
- GCC_except_table208
- GCC_except_table221
- GCC_except_table24
- GCC_except_table54
- GCC_except_table71
- GCC_except_table77
- GCC_except_table81
- GCC_except_table84
- ___block_descriptor_40_e39_v16?0"FBSMutableSceneClientSettings"8l
- ___block_descriptor_48_e8_32s40s_e63_v24?0"FBSMutableSceneSettings"8"FBSSceneTransitionContext"16l
CStrings:
+ "\x1b"
+ "%s: called outside a termination flow"
+ "-[UINSAppKitTerminationController markAppKitTerminationNonCancelableIfDeferred]"
+ "-[UINSAppLifecycleStateAwaitingClosureConfirmation accelerateTerminationSchedule_InAction]"
+ "-[UINSClosureConfirmationController beginPerWindowClosureConfirmationForScene:]"
+ "-[UINSClosureConfirmationController beginTerminationClosureConfirmations]"
+ "Actions added to a closure confirmation must have a title"
+ "App termination is for system shutdown, but a scene has a closureConfirmation. Deferring non-cancelability until the dialog resolves."
+ "Applying shadow state %{public}@ to scene %{public}@"
+ "Approved"
+ "AwaitingClosureConfirmation"
+ "Canceled"
+ "Cannot present closure confirmation for %{public}@ (confirmation=%{public}@, window=%{public}@)"
+ "Closure confirmation approved. Marking termination non-cancelable to expedite."
+ "Closure confirmation resolved: %{public}s"
+ "Dequeuing paused until state change is complete. (%{public}@; %{public}@)"
+ "Explicit / expedited termination, but a scene has a closureConfirmation. Deferring non-cancelability until the dialog resolves."
+ "Ignorning tracking sentinel arrival for old UUID: %{public}@"
+ "No longer tracking scene state with target state: %{public}@ (%{public}@) UUID: %{public}@"
+ "Saving shadow state: %{public}@ (%{public}@)"
+ "Scene reached target state. (%{public}@) UUID: %{public}@"
+ "Skipping shadow state for disconnected scene %{public}@"
+ "Still waiting for tracking sentinel. Ignoring state change. (%{public}@) UUID: %{public}@"
+ "Termination in progress; ignoring per-window closure confirmation for %{public}@"
+ "Tracking scene state with target state: %{public}@ (%{public}@) UUID: %{public}@"
+ "Tracking sentinel arrived. (%{public}@) UUID: %{public}@"
+ "UINSAppLifecycleStateAwaitingClosureConfirmation.m"
+ "UINSClosureConfirmationController.m"
+ "v16@?0@\"BSActionResponse\"8"
+ "v20@?0I8Q12"
- "+"
- "Applying shadow state %@ to scene %@"
- "Dequeuing paused until state change is complete. (%@; %@)"
- "No longer tracking scene state with target state: %@ (%@)"
- "Saving shadow state: %@ (%@)"
- "Scene reached target state. (%@)"
- "Scene was already in requested state. Skipping."
- "Skipping shadow state for disconnected scene %@"
- "Tracking scene state with target state: %@ (%@)"
```
