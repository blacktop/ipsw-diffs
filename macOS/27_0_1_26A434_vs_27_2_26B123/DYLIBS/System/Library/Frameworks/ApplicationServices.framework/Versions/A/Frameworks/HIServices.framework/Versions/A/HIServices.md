## HIServices

> `/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/HIServices.framework/Versions/A/HIServices`

```diff

-834.0.0.0.0
-  __TEXT.__text: 0x5ad24
+835.6.0.0.0
+  __TEXT.__text: 0x5b5b0
   __TEXT.__objc_methlist: 0x10c
-  __TEXT.__const: 0x1610
-  __TEXT.__cstring: 0x5fba
-  __TEXT.__oslogstring: 0x2309
+  __TEXT.__const: 0x1620
+  __TEXT.__cstring: 0x6206
+  __TEXT.__oslogstring: 0x245f
   __TEXT.__dlopen_cstrs: 0xfc
   __TEXT.__ustring: 0xd2
   __TEXT.__gcc_except_tab: 0x344
   __TEXT.__dof_Accessibi: 0x90c
-  __TEXT.__unwind_info: 0x1688
+  __TEXT.__unwind_info: 0x16b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1280
+  __DATA_CONST.__const: 0x1490
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x220
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0x4f0
   __AUTH_CONST.__const: 0x1898
-  __AUTH_CONST.__cfstring: 0x5e40
+  __AUTH_CONST.__cfstring: 0x5e80
   __AUTH_CONST.__objc_const: 0x230
   __AUTH_CONST.__weak_auth_got: 0x20
-  __AUTH_CONST.__auth_got: 0x1968
+  __AUTH_CONST.__auth_got: 0x1970
   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__data: 0x138
+  __AUTH.__thread_vars: 0x18
+  __AUTH.__thread_bss: 0x400
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x420
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x9d0
+  __DATA.__bss: 0x9b0
   __DATA.__common: 0x44
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x114
-  __DATA_DIRTY.__bss: 0x9f8
+  __DATA_DIRTY.__bss: 0xa08
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/QD.framework/Versions/A/QD

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1884
-  Symbols:   3275
-  CStrings:  1255
+  Functions: 1905
+  Symbols:   3295
+  CStrings:  1292
 
Symbols:
+ CoreDragBeginSlideBackAnimationAsync.sCheckedForAsyncProc
+ CoreDragBeginSlideBackAnimationAsync.sCoreDragBeginSlideBackAnimationAsyncProc
+ CoreDragTerminateDragsForPID
+ CoreDragTerminateReceiver
+ CoreDragUpdateContents.sCoreDragUpdateContentsProc
+ DisposeReceiverState
+ PerformReceiverSourceDiedTeardown
+ SimulateReceiverMessage
+ StringFromDragInfo.dragFlagNames
+ StringFromDragInfo.flagsString
+ StringFromDragInfo.flagsString$tlv$init
+ StringFromDragState.dragStateNames
+ _CFMessagePortIsValid
+ _CallTrackingEndedProc
+ _CollectDragRefsForPID
+ _CoreDragBeginSlideBackAnimationAsync
+ _CoreDragIsDirectTouch
+ _CoreDragSetTrackingEndedProc
+ _CoreDragTerminateDragsForPID
+ _CoreDragTerminateReceiver
+ _CoreDragUpdateContents
+ _CoreDragWasCanceled
+ _DisposeReceiverState
+ _EndDraggingZoomBackDidComplete
+ _FinishEndDragging
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _PerformReceiverSourceDiedTeardown
+ _SimulateReceiverMessage
+ _ZoomBackAnimationDidComplete
+ __tlv_bootstrap
+ _gTrackingEndedProcUserData
+ _gTrackingEndedProcs
+ _hypot
- CoreDragAutoScaleSourceDragComponents.sCoreDragAutoScaleSourceDragComponentsProc
- CoreDragResetAutoScaleSourceDragComponents.sCoreDragResetAutoScaleSourceDragComponentsProc
- CoreDragUpdateDragLayerContent.sCoreDragUpdateDragLayerContentProc
- CoreDragUpdateFlockingFormation.sCoreDragUpdateFlockingFormationProc
- CoreDragUpdateLayerPositions.sCoreDragUpdateLayerPositionsProc
- _CGDisplayPixelsHigh
- _CoreDragAutoScaleSourceDragComponents
- _CoreDragResetAutoScaleSourceDragComponents
- _CoreDragUpdateDragLayerContent
- _CoreDragUpdateFlockingFormation
- _CoreDragUpdateLayerPositions
- _sPid
- _sPortDragRef
- _sRemotePort
CStrings:
+ "%llx CoreDragTerminate - cancel tracking"
+ "%llx CoreDragTerminate - terminate receiver"
+ "%llx Drag source died; synthesizing receiver teardown."
+ "%llx Dropped on connection %u: %s"
+ "%llx End drag loop. %s - %s"
+ "%llx Handle message: %s (%d) [%s]"
+ "%llx SendDragIPCMessage %{public}s failed with error %d"
+ "%llx Skipping %{public}s; remote port invalid."
+ "%llx kDragIPCDrop - source died during drop"
+ "0x%x"
+ "CDDragSignificantMovement"
+ "CDEnableAsynchronousSlideBackAnimation"
+ "CoreDragUpdateContents"
+ "Ended"
+ "Failed to get connection for pid %d with error %d. Process may have terminated."
+ "GetRemoteDragPort: CFMessagePortCreatePerProcessRemote returned NULL for pid %d"
+ "IPC"
+ "Ignoring invalidation for stale remote port %p (current %p, %d)"
+ "Remote drag port for process %d was invalidated. Process may have terminated."
+ "Terminate drags for process %d"
+ "Tracking"
+ "Unpacked drag reference does not match: %llx != %llx"
+ "WaitingForDropCompleted"
+ "WaitingForZoomBack"
+ "__CoreDragBeginSlideBackAnimationAsync"
+ "__CoreDragUpdateContents"
+ "kDragAcceptEvent"
+ "kDragCachedCursorInBackgroundValue"
+ "kDragCancelEvent"
+ "kDragChangedTarget"
+ "kDragDestinationClearDragImages"
+ "kDragDestinationHasDragImageUpdatesForIPC"
+ "kDragDestinationShouldSendImageUpdates"
+ "kDragDidSendPing"
+ "kDragDropIsAsync"
+ "kDragEndEvent"
+ "kDragFirstSample"
+ "kDragHasEnabledBackgroundCursor"
+ "kDragInProgress"
+ "kDragIsDirectTouch"
+ "kDragRgnAndImage"
+ "kDragScreenUpdatesDisabled"
+ "kDragShowWindowOnFirstSample"
+ "kDragSourceHasDragImageUpdatesForIPC"
+ "kDragStartedAtSignificantMovement"
+ "kDragStoleKeyFocus"
+ "kDragSuccess"
+ "kDragTracking"
+ "kDragTrashIconReset"
+ "kDragTrashLabelReset"
+ "kDragTrashLabelSet"
+ "kDragUpdateClippingArea"
+ "kDragUpdateFormation"
+ "kDragUpdateLayerPositions"
+ "kDragUpdateWindowContent"
+ "kDragZoomBackInProgress"
+ "kMouseButtonIsDown"
+ "synthesized"
+ "|"
- "%llx Cannot track drag receiver. No pasteboard name."
- "%llx CoreDragTerminate"
- "%llx Dropped on connection %u, %s."
- "%llx End drag loop."
- "%llx Handle message: %s (%d)"
- "%llx Send async drag ended: %d %p"
- "%llx SendDragIPCMessage failed with error %d"
- "CoreDragAutoScaleSourceDragComponents"
- "CoreDragResetAutoScaleSourceDragComponents"
- "CoreDragUpdateDragLayerContent"
- "CoreDragUpdateFlockingFormation"
- "CoreDragUpdateLayerPositions"
- "GetRemoteDragPort: CFMessagePortCreatePerProcessRemote returned NULL for pid %d (rdar://178647659)"
- "Invalidated remote port for process %d"
- "Unpacked drag reference does not match: %llx %llx"
- "__CoreDragAutoScaleSourceDragComponents"
- "__CoreDragResetAutoScaleSourceDragComponents"
- "__CoreDragUpdateDragLayerContent"
- "__CoreDragUpdateFlockingFormation"
- "__CoreDragUpdateLayerPositions"
- "async"
- "sync"
```
