## HIServices

> `/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/HIServices.framework/Versions/A/HIServices`

```diff

-834.0.0.0.0
-  __TEXT.__text: 0x59de0
+835.3.0.0.0
+  __TEXT.__text: 0x5a0b8
   __TEXT.__objc_methlist: 0x10c
-  __TEXT.__const: 0x1610
-  __TEXT.__cstring: 0x5fba
-  __TEXT.__oslogstring: 0x2309
+  __TEXT.__const: 0x1620
+  __TEXT.__cstring: 0x5e96
+  __TEXT.__oslogstring: 0x2458
   __TEXT.__dlopen_cstrs: 0xfc
   __TEXT.__ustring: 0xd2
   __TEXT.__gcc_except_tab: 0x344
   __TEXT.__dof_Accessibi: 0x90c
-  __TEXT.__unwind_info: 0x1ca0
+  __TEXT.__unwind_info: 0x1ce0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

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
-  Functions: 1883
-  Symbols:   3275
-  CStrings:  1255
+  Functions: 1899
+  Symbols:   3279
+  CStrings:  1254
 
Symbols:
+ CoreDragTerminateDragsForPID
+ CoreDragTerminateReceiver
+ CoreDragUpdateContents.sCoreDragUpdateContentsProc
+ DisposeReceiverState
+ PerformReceiverSourceDiedTeardown
+ SimulateReceiverMessage
+ _CFMessagePortIsValid
+ _CollectDragRefsForPID
+ _CoreDragIsDirectTouch
+ _CoreDragTerminateDragsForPID
+ _CoreDragTerminateReceiver
+ _CoreDragUpdateContents
+ _CoreDragWasCanceled
+ _DisposeReceiverState
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _PerformReceiverSourceDiedTeardown
+ _SimulateReceiverMessage
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
+ "%llx Handle message: %s (%d) [%s]"
+ "%llx SendDragIPCMessage %{public}s failed with error %d"
+ "%llx Skipping %{public}s; remote port invalid."
+ "%llx kDragIPCDrop - source died during drop"
+ "CoreDragUpdateContents"
+ "Failed to get connection for pid %d with error %d. Process may have terminated."
+ "GetRemoteDragPort: CFMessagePortCreatePerProcessRemote returned NULL for pid %d"
+ "IPC"
+ "Ignoring invalidation for stale remote port %p (current %p, %d)"
+ "Remote drag port for process %d was invalidated. Process may have terminated."
+ "Terminate drags for process %d"
+ "Unpacked drag reference does not match: %llx != %llx"
+ "__CoreDragUpdateContents"
+ "synthesized"
- "%llx Cannot track drag receiver. No pasteboard name."
- "%llx CoreDragTerminate"
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
```
