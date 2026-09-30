## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

```diff

-665.80.6.0.0
-  __TEXT.__text: 0x847220
+665.80.7.0.1
+  __TEXT.__text: 0x8479d4
   __TEXT.__auth_stubs: 0x5430
   __TEXT.__objc_methlist: 0x34858
   __TEXT.__const: 0x151240
-  __TEXT.__cstring: 0xe5aff
-  __TEXT.__oslogstring: 0x13c8f5
+  __TEXT.__cstring: 0xe5b8e
+  __TEXT.__oslogstring: 0x13cca5
   __TEXT.__gcc_except_tab: 0x3dac
   __TEXT.__dlopen_cstrs: 0x701
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0xf650
+  __TEXT.__unwind_info: 0xf658
   __TEXT.__eh_frame: 0x68
   __TEXT.__objc_classname: 0x850d
-  __TEXT.__objc_methname: 0xa8fc8
+  __TEXT.__objc_methname: 0xa8ff9
   __TEXT.__objc_methtype: 0x16591
   __TEXT.__objc_stubs: 0x49700
   __DATA_CONST.__got: 0x6928

   __AUTH_CONST.__auth_got: 0x2a28
   __AUTH_CONST.__const: 0x4700
   __AUTH_CONST.__cfstring: 0x50be0
-  __AUTH_CONST.__objc_const: 0x95f10
+  __AUTH_CONST.__objc_const: 0x95f50
   __AUTH_CONST.__objc_intobj: 0x5c58
   __AUTH_CONST.__objc_arrayobj: 0x2928
   __AUTH_CONST.__objc_floatobj: 0x250
   __AUTH_CONST.__objc_dictobj: 0x1770
   __AUTH_CONST.__objc_doubleobj: 0xa90
   __AUTH.__objc_data: 0x3430
-  __DATA.__objc_ivar: 0xaae0
+  __DATA.__objc_ivar: 0xaae8
   __DATA.__data: 0x5520
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x1b20

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 621A0EA0-A596-3C4C-A8C1-F9F003BDDF73
-  Functions: 34379
-  Symbols:   115114
-  CStrings:  70604
+  UUID: AE928F20-0840-3B7B-BB61-B9C51CF2B48B
+  Functions: 34395
+  Symbols:   115150
+  CStrings:  70616
 
Symbols:
+ -[FigCaptureSourceStreamsContainer zoomFactorsForDepthWithMaxContinuousZoomForDepthDataDelivery:]
+ -[FigExternalSyncDeviceDiscoverySessionDelegateHandler externalSyncDeviceDiscoverySessionManager:connectedDevicesDidChange:].cold.2
+ -[FigExternalSyncDeviceDiscoverySessionDelegateHandler externalSyncDeviceDiscoverySessionManager:connectedDevicesDidChange:].cold.3
+ _.compoundliteral.100
+ _.compoundliteral.31
+ _.compoundliteral.32
+ _.compoundliteral.41
+ _.compoundliteral.42
+ _.compoundliteral.48
+ _.compoundliteral.49
+ _.compoundliteral.50
+ _.compoundliteral.52
+ _.compoundliteral.53
+ _.compoundliteral.54
+ _.compoundliteral.55
+ _.compoundliteral.62
+ _.compoundliteral.93
+ _.compoundliteral.94
+ _.compoundliteral.95
+ _.compoundliteral.96
+ _.compoundliteral.97
+ _.compoundliteral.98
+ _.compoundliteral.99
+ _FigExternalSyncDeviceDiscoverySessionCreate.cold.2
+ _OBJC_IVAR_$_BWGraph._deferredPrepareActiveNode
+ _OBJC_IVAR_$_BWGraph._deferredPrepareState
- -[FigCaptureSourceStreamsContainer zoomFactorsForDepth]
- _.compoundliteral.38
- _.compoundliteral.39
- _.compoundliteral.46
- _.compoundliteral.60
- _.compoundliteral.63
- _.compoundliteral.64
- _.compoundliteral.65
- _.compoundliteral.66
- _.compoundliteral.68
- _.compoundliteral.69
- _.compoundliteral.70
- _.compoundliteral.77
- _.compoundliteral.79
- _.compoundliteral.80
- _.compoundliteral.81
- _.compoundliteral.82
- _.compoundliteral.83
- _.compoundliteral.84
- _.compoundliteral.87
- _.compoundliteral.88
CStrings:
+ "!storage->invalid"
+ "21:25:13"
+ "<<<< BWGraph >>>> %s: <%p[%{public}d][%{public}@]> A node with pointer <0x%lx> was flagged as still executing deferred prepare but wasn't found in this graph's node list. This may be a BWGraph bug"
+ "<<<< BWGraph >>>> %s: <%p[%{public}d][%{public}@]> Deferred prepare is still active which prevents graph start, but no single actively preparing node was identified. The deferred prepare thread may be stuck on non-node work or transitioning between nodes."
+ "<<<< BWGraph >>>> %s: <%p[%{public}d][%{public}@]> Deferred prepare is still pending which prevents graph start but hasn't asynchronously started or canceled."
+ "<<<< BWGraph >>>> %s: <%p[%{public}d][%{public}@]> Graph timeout was not attributed to any individual nodes."
+ "<<<< BWGraph >>>> %s: <%p[%{public}d][%{public}@]> Node <%p, %@, %@, %{public}@> is still executing deferred prepare and may have caused a graph start timeout."
+ "<<<< BWGraph >>>> %s: <%p[%{public}d][%{public}@]> Sink node <%p, %@, %{public}@> is %{public}@ which prevents graph from %@, but is blocked from %@ due to the following input states:"
+ "<<<< FigExternalSyncDeviceDiscoverySession >>>> %s: NULL notification queue"
+ "<<<< FigExternalSyncDeviceDiscoverySession >>>> %s: Session already invalidated, skipping notification"
+ "Failed to create notification queue"
+ "FigExternalSyncDeviceDiscoverySessionCreate"
+ "Jan  4 2026"
+ "LastShownBuild:BWGraph.m:3269"
+ "LastShownBuild:BWGraph.m:3348"
+ "LastShownBuild:BWGraph.m:3362"
+ "LastShownBuild:BWGraph.m:3365"
+ "LastShownBuild:FigCaptureSession.m:16609"
+ "LastShownBuild:FigCaptureSession.m:18095"
+ "LastShownBuild:FigCaptureSession.m:18948"
+ "LastShownBuild:FigCaptureSession.m:22439"
+ "LastShownBuild:FigCaptureSession.m:22474"
+ "LastShownBuild:FigCaptureSession.m:24735"
+ "LastShownBuild:FigCaptureSourceBackingsProvider.m:2522"
+ "LastShownDate:BWGraph.m:3269"
+ "LastShownDate:BWGraph.m:3348"
+ "LastShownDate:BWGraph.m:3362"
+ "LastShownDate:BWGraph.m:3365"
+ "LastShownDate:FigCaptureSession.m:16609"
+ "LastShownDate:FigCaptureSession.m:18095"
+ "LastShownDate:FigCaptureSession.m:18948"
+ "LastShownDate:FigCaptureSession.m:22439"
+ "LastShownDate:FigCaptureSession.m:22474"
+ "LastShownDate:FigCaptureSession.m:24735"
+ "LastShownDate:FigCaptureSourceBackingsProvider.m:2522"
+ "_deferredPrepareActiveNode"
+ "_deferredPrepareState"
+ "description=CameraCapture-665.80.7.0.1"
+ "storage->notificationQueue != ((void*)0)"
- "01:27:57"
- "<<<< BWGraph >>>> %s: <%p[%{public}d][%{public}@]> Failed to attribute graph timeout to one or more offenders"
- "<<<< BWGraph >>>> %s: <%p[%{public}d][%{public}@]> Sink node <%p, %@, %{public}@> is %{public}@ which prevents graph from %@, but is blocked from stopping due to the following input states:"
- "Dec  6 2025"
- "LastShownBuild:BWGraph.m:3249"
- "LastShownBuild:BWGraph.m:3325"
- "LastShownBuild:BWGraph.m:3328"
- "LastShownBuild:BWGraph.m:3342"
- "LastShownBuild:FigCaptureSession.m:16606"
- "LastShownBuild:FigCaptureSession.m:18089"
- "LastShownBuild:FigCaptureSession.m:18945"
- "LastShownBuild:FigCaptureSession.m:22436"
- "LastShownBuild:FigCaptureSession.m:22471"
- "LastShownBuild:FigCaptureSession.m:24732"
- "LastShownBuild:FigCaptureSourceBackingsProvider.m:2519"
- "LastShownDate:BWGraph.m:3249"
- "LastShownDate:BWGraph.m:3325"
- "LastShownDate:BWGraph.m:3328"
- "LastShownDate:BWGraph.m:3342"
- "LastShownDate:FigCaptureSession.m:16606"
- "LastShownDate:FigCaptureSession.m:18089"
- "LastShownDate:FigCaptureSession.m:18945"
- "LastShownDate:FigCaptureSession.m:22436"
- "LastShownDate:FigCaptureSession.m:22471"
- "LastShownDate:FigCaptureSession.m:24732"
- "LastShownDate:FigCaptureSourceBackingsProvider.m:2519"
- "description=CameraCapture-665.80.6"

```
