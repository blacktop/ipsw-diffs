## CompanionCamera

> `/System/Library/PrivateFrameworks/CompanionCamera.framework/CompanionCamera`

```diff

-2023.500.2.0.0
-  __TEXT.__text: 0x97e4
-  __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_methlist: 0xad4
-  __TEXT.__const: 0xf0
-  __TEXT.__gcc_except_tab: 0x14c
-  __TEXT.__oslogstring: 0x585
-  __TEXT.__cstring: 0xda3
-  __TEXT.__unwind_info: 0x288
-  __TEXT.__objc_classname: 0x122
-  __TEXT.__objc_methname: 0x19da
-  __TEXT.__objc_methtype: 0x4da
-  __TEXT.__objc_stubs: 0x1760
-  __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__const: 0x468
-  __DATA_CONST.__objc_classlist: 0x30
+2024.100.12.0.0
+  __TEXT.__text: 0x80c8
+  __TEXT.__objc_methlist: 0xa54
+  __TEXT.__const: 0x110
+  __TEXT.__gcc_except_tab: 0x78
+  __TEXT.__oslogstring: 0x53b
+  __TEXT.__cstring: 0xb61
+  __TEXT.__unwind_info: 0x238
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x400
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7d8
+  __DATA_CONST.__objc_selrefs: 0x770
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1e8
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__got: 0xb0
   __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x9c0
-  __AUTH_CONST.__objc_const: 0xb78
-  __AUTH_CONST.__objc_intobj: 0xf0
+  __AUTH_CONST.__cfstring: 0x780
+  __AUTH_CONST.__objc_const: 0xa60
+  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x88
+  __DATA.__objc_ivar: 0x78
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__bss: 0x40
+  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B669FEF0-503B-381C-9599-94EFAC6D2506
-  Functions: 263
-  Symbols:   997
-  CStrings:  609
+  UUID: ABA0273D-6241-391E-9E7A-3F445D26FC61
+  Functions: 233
+  Symbols:   936
+  CStrings:  195
 
Symbols:
+ _CCCaptureDeviceFromNCCaptureDevice
+ _CCCaptureModeFromNCCaptureMode
+ _CCFlashModeFromNCFlashMode
+ _CCHDRModeFromNCHDRMode
+ _CCIrisModeFromNCIrisMode
+ _CCSharedLibraryModeFromNCSharedLibraryMode
+ _NCCaptureDeviceFromCCCaptureDevice
+ _NCCaptureModeFromCCCaptureMode
+ _NCFlashModeFromCCFlashMode
+ _NCFlashSupportFromCCFlashSupport
+ _NCHDRModeFromCCHDRMode
+ _NCHDRSupportFromCCHDRSupport
+ _NCIrisModeFromCCIrisMode
+ _NCIrisSupportFromCCIrisSupport
+ _NCOrientationFromDeviceOrientation
+ _NCShallowDepthOfFieldStatusFromCCShallowDepthOfFieldStatus
+ _NCSharedLibraryModeFromCCSharedLibraryMode
+ _NCSharedLibrarySupportFromCCSharedLibrarySupport
+ _NCStereoCaptureStatusFromCCStereoCaptureStatus
+ ___30-[CCCameraConnection _connect]_block_invoke.89
+ ___block_literal_global.101
+ ___block_literal_global.103
+ ___block_literal_global.106
+ ___block_literal_global.108
+ ___block_literal_global.110
+ ___block_literal_global.112
+ ___block_literal_global.114
+ ___block_literal_global.116
+ ___block_literal_global.118
+ ___block_literal_global.120
+ ___block_literal_global.122
+ ___block_literal_global.124
+ ___block_literal_global.126
+ ___block_literal_global.128
+ ___block_literal_global.130
+ ___block_literal_global.132
+ ___block_literal_global.134
+ ___block_literal_global.136
+ ___block_literal_global.138
+ ___block_literal_global.227
+ ___block_literal_global.229
+ ___block_literal_global.95
+ ___block_literal_global.97
+ ___block_literal_global.99
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- +[ViewfinderReliability sharedInstance]
- -[ViewfinderReliability .cxx_destruct]
- -[ViewfinderReliability _checkForRepeatedEvent:]
- -[ViewfinderReliability _checkForRepeatedEvent:].cold.1
- -[ViewfinderReliability _checkForUnexpectedEvent:]
- -[ViewfinderReliability _checkForUnexpectedEvent:].cold.1
- -[ViewfinderReliability _print]
- -[ViewfinderReliability _registerSources]
- -[ViewfinderReliability _reset]
- -[ViewfinderReliability init]
- -[ViewfinderReliability logEvent:]
- GCC_except_table3
- GCC_except_table5
- GCC_except_table8
- GCC_except_table9
- _CFPreferencesGetAppBooleanValue
- _NSStringFromViewfinderReliabiliyEvent
- _OBJC_CLASS_$_NSCountedSet
- _OBJC_CLASS_$_NSMutableString
- _OBJC_CLASS_$_ViewfinderReliability
- _OBJC_IVAR_$_ViewfinderReliability._events
- _OBJC_IVAR_$_ViewfinderReliability._log
- _OBJC_IVAR_$_ViewfinderReliability._printSource
- _OBJC_IVAR_$_ViewfinderReliability._resetSource
- _OBJC_METACLASS_$_ViewfinderReliability
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- __OBJC_$_CLASS_METHODS_ViewfinderReliability
- __OBJC_$_INSTANCE_METHODS_ViewfinderReliability
- __OBJC_$_INSTANCE_VARIABLES_ViewfinderReliability
- __OBJC_CLASS_RO_$_ViewfinderReliability
- __OBJC_METACLASS_RO_$_ViewfinderReliability
- ___30-[CCCameraConnection _connect]_block_invoke.91
- ___39+[ViewfinderReliability sharedInstance]_block_invoke
- ___41-[ViewfinderReliability _registerSources]_block_invoke
- ___41-[ViewfinderReliability _registerSources]_block_invoke_2
- ___block_literal_global.100
- ___block_literal_global.102
- ___block_literal_global.104
- ___block_literal_global.107
- ___block_literal_global.109
- ___block_literal_global.111
- ___block_literal_global.113
- ___block_literal_global.115
- ___block_literal_global.117
- ___block_literal_global.119
- ___block_literal_global.121
- ___block_literal_global.123
- ___block_literal_global.125
- ___block_literal_global.127
- ___block_literal_global.129
- ___block_literal_global.131
- ___block_literal_global.133
- ___block_literal_global.135
- ___block_literal_global.137
- ___block_literal_global.139
- ___block_literal_global.228
- ___block_literal_global.230
- ___block_literal_global.96
- ___block_literal_global.98
- __ccCaptureDeviceFromNCCaptureDevice
- __ccCaptureModeFromNCCaptureMode
- __ccFlashModeFromNCFlashMode
- __ccHDRModeFromNCHDRMode
- __ccIrisModeFromNCIrisMode
- __ccSharedLibraryModeFromNCSharedLibraryMode
- __dispatch_source_type_signal
- __ncCaptureDeviceFromCCCaptureDevice
- __ncCaptureModeFromCCCaptureMode
- __ncFlashModeFromCCFlashMode
- __ncFlashSupportFromCCFlashSupport
- __ncHDRModeFromCCHDRMode
- __ncHDRSupportFromCCHDRSupport
- __ncIrisModeFromCCIrisMode
- __ncIrisSupportFromCCIrisSupport
- __ncOrientationFromDeviceOrientation
- __ncShallowDepthOfFieldStatusFromCCShallowDepthOfFieldStatus
- __ncSharedLibraryModeFromCCSharedLibraryMode
- __ncSharedLibrarySupportFromCCSharedLibrarySupport
- __ncStereoCaptureStatusFromCCStereoCaptureStatus
- __os_log_fault_impl
- _objc_enumerationMutation
- _objc_msgSend$_checkForRepeatedEvent:
- _objc_msgSend$_checkForUnexpectedEvent:
- _objc_msgSend$_print
- _objc_msgSend$_registerSources
- _objc_msgSend$_reset
- _objc_msgSend$addObject:
- _objc_msgSend$appendString:
- _objc_msgSend$countByEnumeratingWithState:objects:count:
- _objc_msgSend$countForObject:
- _objc_msgSend$logEvent:
- _objc_msgSend$removeAllObjects
- _objc_msgSend$set
- _objc_msgSend$string
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_sync_enter
- _objc_sync_exit
- _os_variant_has_internal_diagnostics
- _signal
CStrings:
+ "NotSupported"
+ "VisualIntelligence"
- "#16@0:8"
- "%@: %lu\n"
- ".cxx_destruct"
- "@"
- "@\"<CCCameraConnectionDelegate>\""
- "@\"CCCameraConnection\""
- "@\"CCCameraConnectionInternal\""
- "@\"FigCameraViewfinder\""
- "@\"FigCameraViewfinderSession\""
- "@\"NSCountedSet\""
- "@\"NSDate\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@36@0:8q16i24@28"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "C"
- "CCCameraConnection"
- "CCCameraConnectionInternal"
- "CCCameraConnectionProtocol"
- "CCCameraConnectionReliabilityMonitor"
- "CCCameraServerProtocol"
- "CameraAppLaunch"
- "CameraAppLaunchFailed"
- "CameraAppLaunchhSucceeded"
- "CameraPreviewIDSSocketCreationFailed"
- "CloseCameraMessageReceived"
- "Count of events:\n%@"
- "DaemonXPCConnectionInterruption"
- "DaemonXPCConnectionInvalidation"
- "DaemonXPCConnectionReceived"
- "FigCameraViewfinderCreation"
- "FigCameraViewfinderDelegate"
- "FigCameraViewfinderSessionDelegate"
- "FigCameraViewfinderSessionDidBegin"
- "FigCameraViewfinderSessionDidEnd"
- "FigCameraViewfinderSessionOpenPreviewStream"
- "FigCameraViewfinderSessionPreviewStreamDidClose"
- "FigCameraViewfinderSessionPreviewStreamDidOpen"
- "FigCameraViewfinderStarted"
- "NSObject"
- "OpenCameraMessageReceived"
- "Q"
- "Q16@0:8"
- "Repeated event: %@"
- "Reset events."
- "T#,R"
- "T@\"<CCCameraConnectionDelegate>\",W,N,V_delegate"
- "T@\"CCCameraConnection\",W,N,V_parent"
- "T@\"NSDate\",R,N,V_date"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Ti,R,N,V_status"
- "Tq,R,N,V_code"
- "Unexpected event: %@"
- "ViewfinderErrorReport"
- "ViewfinderReliability"
- "ViewfinderReliability_CheckRepeatedEvents"
- "ViewfinderReliability_CheckUnexpectedEvents"
- "Vv16@0:8"
- "Vv20@0:8f16"
- "Vv24@0:8@\"NSDate\"16"
- "Vv24@0:8@\"NSString\"16"
- "Vv24@0:8@\"NSValue\"16"
- "Vv24@0:8@16"
- "Vv24@0:8@?16"
- "Vv24@0:8@?<v@?B>16"
- "Vv24@0:8Q16"
- "Vv24@0:8q16"
- "Vv28@0:8B16@?20"
- "Vv28@0:8B16@?<v@?@\"NSOrderedSet\"q@\"NSOrderedSet\"qB@\"NSDate\"B@\"NSDate\"qBBfBff@\"NSArray\"fqqqqqqqqBBQqq>20"
- "Vv28@0:8f16@?20"
- "Vv28@0:8f16@?<v@?f>20"
- "Vv32@0:8@\"NSOrderedSet\"16@?<v@?>24"
- "Vv32@0:8@16@?24"
- "Vv32@0:8q16@?24"
- "Vv32@0:8q16@?<v@?B>24"
- "^{_NSZone=}16@0:8"
- "_burstInProgress"
- "_burstSupport"
- "_captureDevice"
- "_captureMode"
- "_capturePauseDate"
- "_captureStartDate"
- "_capturing"
- "_capturingPaused"
- "_checkForRepeatedEvent:"
- "_checkForUnexpectedEvent:"
- "_checkin"
- "_closePreview"
- "_code"
- "_codeDescription"
- "_connect"
- "_currentOrientation"
- "_currentPreviewState"
- "_currentZoomMagnification"
- "_date"
- "_delegate"
- "_desiredPreviewState"
- "_deviceConnectedNotificationToken"
- "_deviceDisconnectedNotificationToken"
- "_disconnect"
- "_events"
- "_flashMode"
- "_flashSupport"
- "_handleInterruption"
- "_handleInvalidation"
- "_hdrMode"
- "_hdrSupport"
- "_instanceCount"
- "_internal"
- "_interruptionCount"
- "_irisMode"
- "_irisSupport"
- "_isConnected"
- "_lastConnectTime"
- "_lastSentZoomAmount"
- "_log"
- "_logError:"
- "_maximumZoomMagnification"
- "_minimumZoomMagnification"
- "_openPreview"
- "_orientationChangeObserver"
- "_parent"
- "_pendingZoomAmount"
- "_performPreviewStateTransitionsIfNeeded"
- "_previewEndpoint"
- "_print"
- "_printSource"
- "_registerSources"
- "_remoteViewfinder"
- "_remoteViewfinderSession"
- "_remoteViewfinderSessionState"
- "_reset"
- "_resetSource"
- "_shallowDepthOfFieldStatus"
- "_sharedLibraryMode"
- "_sharedLibrarySupport"
- "_shouldReportEvent"
- "_significantZoomMagnifications"
- "_status"
- "_stereoCaptureStatus"
- "_supportedCaptureDevices"
- "_supportedCaptureModes"
- "_supportsMomentCapture"
- "_supportsZoomMagnification"
- "_toggleCameraDeviceSupport"
- "_xpc"
- "_zoomAmount"
- "_zoomSupport"
- "_zoomTimer"
- "_zoomTimerFired"
- "addObject:"
- "appendString:"
- "applicationState"
- "autorelease"
- "burstCaptureDidStop"
- "burstCaptureNumberOfPhotosDidChange:"
- "burstCaptureWillStart"
- "cameraConnection:setCaptureDevice:"
- "cameraConnection:setCaptureMode:"
- "cameraConnection:setFlashMode:"
- "cameraConnection:setFocusPoint:"
- "cameraConnection:setHDRMode:"
- "cameraConnection:setIrisMode:"
- "cameraConnection:setSharedLibraryMode:"
- "cameraConnection:setZoomAmount:"
- "cameraConnection:setZoomMagnificationAmount:"
- "cameraConnection:takePhotoWithCountdown:"
- "cameraConnectionBeginBurstCapture:"
- "cameraConnectionBurstSupport:"
- "cameraConnectionCancelCountdown:"
- "cameraConnectionCaptureDevice:"
- "cameraConnectionCaptureMode:"
- "cameraConnectionCurrentZoomMagnification:"
- "cameraConnectionEndBurstCapture:"
- "cameraConnectionFlashMode:"
- "cameraConnectionFlashSupport:"
- "cameraConnectionHDRMode:"
- "cameraConnectionHDRSupport:"
- "cameraConnectionIrisMode:"
- "cameraConnectionIrisSupport:"
- "cameraConnectionMaximumZoomMagnification:"
- "cameraConnectionMinimumZoomMagnification:"
- "cameraConnectionOrientation:"
- "cameraConnectionPauseCapture:"
- "cameraConnectionResumeCapture:"
- "cameraConnectionSharedLibraryMode:"
- "cameraConnectionSharedLibrarySupport:"
- "cameraConnectionSignificantZoomMagnifications:"
- "cameraConnectionStartCapture:"
- "cameraConnectionStopCapture:"
- "cameraConnectionSupportedCaptureDevices:"
- "cameraConnectionSupportedCaptureModes:"
- "cameraConnectionSupportsMomentCapture:"
- "cameraConnectionSuspend:"
- "cameraConnectionToggleCameraDevice:"
- "cameraConnectionToggleCameraDeviceSupport:"
- "cameraConnectionZoomAmount:"
- "cameraConnectionZoomMagnificationSupport:"
- "cameraConnectionZoomSupport:"
- "cameraViewfinder"
- "cameraViewfinder:viewfinderSessionDidBegin:"
- "cameraViewfinder:viewfinderSessionDidEnd:"
- "cameraViewfinder:viewfinderSessionWillBegin:"
- "cameraViewfinderSession:didCapturePhotoWithStatus:thumbnailData:timestamp:"
- "cameraViewfinderSession:previewStreamDidCloseWithStatus:"
- "cameraViewfinderSessionDidFinishMovieRecording:"
- "cameraViewfinderSessionDidStartMovieRecording:"
- "cameraViewfinderSessionPreviewStreamDidOpen:"
- "captureDeviceDidChange"
- "captureDeviceDidChange:"
- "checkin"
- "class"
- "close"
- "closePreviewStream"
- "conformsToProtocol:"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countForObject:"
- "countdownCanceled"
- "d16@0:8"
- "date"
- "dealloc"
- "debugDescription"
- "decrementInstanceCount"
- "defaultCenter"
- "delegate"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "didConnect"
- "didDisconnect"
- "didPauseCaptureTimerWithPauseTime:"
- "didResumeCaptureTimerWithNewStartTime:"
- "didStartCaptureTimer"
- "didStopCapture"
- "didUpdateShallowDepthOfFieldStatus:"
- "didUpdateStereoCaptureStatus:"
- "didUpdateThumbnailWithData:isVideo:"
- "f"
- "firstObject"
- "flashModeDidChange"
- "getValue:"
- "hash"
- "hdrModeDidChange"
- "i16@0:8"
- "incrementInstanceCount"
- "init"
- "initWithCode:status:date:"
- "initWithMachServiceName:options:"
- "integerValue"
- "interfaceWithProtocol:"
- "intersectOrderedSet:"
- "invalidate"
- "irisModeDidChange"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isOpen"
- "isPreviewConnected"
- "isProxy"
- "logEvent:"
- "loggingDescription"
- "modeSelected:"
- "mutableCopy"
- "now"
- "numberWithInt:"
- "numberWithInteger:"
- "objCType"
- "open"
- "openPreviewStreamWithOptions:"
- "orderedSetWithArray:"
- "orderedSetWithObject:"
- "orderedSetWithObjects:"
- "panoramaDirectionDidChange:"
- "parent"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "photoTaken:"
- "postNotificationName:object:userInfo:"
- "q16@0:8"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "report:status:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "set"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setDelegate:"
- "setDelegate:queue:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setParent:"
- "setRemoteObjectInterface:"
- "setWithObjects:"
- "sharedApplication"
- "sharedInstance"
- "sharedLibraryModeDidChange"
- "sharedLibrarySupportDidChange"
- "showingLivePreviewDidChange"
- "startWithOptions:"
- "string"
- "stringFromDate:"
- "stringWithFormat:"
- "superclass"
- "switchedOrientation:"
- "takePhotoWithCountdown:"
- "timeIntervalSinceNow"
- "ttrDescriptionWithDateFormatter:"
- "v16@0:8"
- "v24@0:8@\"FigCameraViewfinderSession\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@\"FigCameraViewfinderSession\"16i24"
- "v28@0:8@\"NSData\"16B24"
- "v28@0:8@16B24"
- "v28@0:8@16i24"
- "v28@0:8q16i24"
- "v32@0:8@\"FigCameraViewfinder\"16@\"FigCameraViewfinderSession\"24"
- "v32@0:8@16@24"
- "v60@0:8@\"FigCameraViewfinderSession\"16i24@\"NSData\"28{?=qiIq}36"
- "v60@0:8@16i24@28{?=qiIq}36"
- "willStartCapturing"
- "xpc_beginBurstCaptureWithReply:"
- "xpc_burstCaptureDidStop"
- "xpc_burstCaptureNumberOfPhotosDidChange:"
- "xpc_burstCaptureWillStart"
- "xpc_cancelCountdown"
- "xpc_captureDeviceDidChange"
- "xpc_captureDeviceDidChange:"
- "xpc_captureModeSelected:"
- "xpc_countdownCanceled"
- "xpc_didPauseCaptureTimerWithDate:"
- "xpc_didResumeCaptureTimerWithDate:"
- "xpc_didStartCaptureTimerWithDate:"
- "xpc_didStopCapture"
- "xpc_didUpdateShallowDepthOfFieldStatus:"
- "xpc_didUpdateStereoCaptureStatus:"
- "xpc_didUpdateThumbnailWithData:isVideo:"
- "xpc_endBurstCaptureWithReply:"
- "xpc_ensureSwitchedToOneOfSupportedCaptureModes:reply:"
- "xpc_fetchCurrentStateIncludingSupportedCaptureModes:reply:"
- "xpc_flashModeDidChange:"
- "xpc_hdrModeDidChange:"
- "xpc_irisModeDidChange:"
- "xpc_orientationChanged:"
- "xpc_pauseCaptureWithReply:"
- "xpc_resumeCaptureWithReply:"
- "xpc_setCaptureDevice:reply:"
- "xpc_setCaptureMode:reply:"
- "xpc_setFlashMode:"
- "xpc_setFocusPoint:"
- "xpc_setHDRMode:"
- "xpc_setIrisMode:"
- "xpc_setPreviewEndpoint:"
- "xpc_setSharedLibraryMode:"
- "xpc_setZoom:reply:"
- "xpc_setZoomMagnification:reply:"
- "xpc_sharedLibraryModeDidChange:"
- "xpc_sharedLibrarySupportDidChange:"
- "xpc_startCaptureWithMode:reply:"
- "xpc_stopCaptureWithReply:"
- "xpc_suspend"
- "xpc_toggleCameraDevice"
- "xpc_viewfinderSessionStateDidChange:"
- "xpc_willStartCapturing"
- "xpc_zoomChanged:"
- "zone"
- "zoomDidChange:"

```
