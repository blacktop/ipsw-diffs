## CompanionCamera

> `/System/Library/PrivateFrameworks/CompanionCamera.framework/CompanionCamera`

```diff

-2022.300.12.0.0
-  __TEXT.__text: 0x8ec0
-  __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_methlist: 0xa4c
-  __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x6c
-  __TEXT.__cstring: 0x8c2
-  __TEXT.__oslogstring: 0x5c5
-  __TEXT.__unwind_info: 0x250
-  __TEXT.__objc_classname: 0xb3
-  __TEXT.__objc_methname: 0x1afe
-  __TEXT.__objc_methtype: 0x4c0
-  __TEXT.__objc_stubs: 0x17c0
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x388
-  __DATA_CONST.__objc_classlist: 0x10
+2023.100.17.0.0
+  __TEXT.__text: 0x8a00
+  __TEXT.__auth_stubs: 0x370
+  __TEXT.__objc_methlist: 0xa54
+  __TEXT.__const: 0xf0
+  __TEXT.__cstring: 0xaf3
+  __TEXT.__gcc_except_tab: 0x8c
+  __TEXT.__oslogstring: 0x53b
+  __TEXT.__unwind_info: 0x230
+  __TEXT.__objc_classname: 0x10a
+  __TEXT.__objc_methname: 0x18e8
+  __TEXT.__objc_methtype: 0x4b3
+  __TEXT.__objc_stubs: 0x15c0
+  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__const: 0x3f0
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7e0
+  __DATA_CONST.__objc_selrefs: 0x770
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1b0
-  __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x420
-  __AUTH_CONST.__objc_const: 0x828
+  __DATA_CONST.__objc_superrefs: 0x18
+  __AUTH_CONST.__auth_got: 0x1c8
+  __AUTH_CONST.__const: 0x3a0
+  __AUTH_CONST.__cfstring: 0x740
+  __AUTH_CONST.__objc_const: 0xa60
   __AUTH_CONST.__objc_intobj: 0x48
-  __DATA.__objc_ivar: 0x70
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x78
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__bss: 0x20
+  __DATA.__bss: 0x20
+  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 753A7770-2BB1-3678-9A2B-E9373C09DEAE
-  Functions: 253
-  Symbols:   925
-  CStrings:  504
+  UUID: 1906B869-BCE8-311E-BCD1-370AEAAE11B4
+  Functions: 241
+  Symbols:   914
+  CStrings:  545
 
Symbols:
+ +[CCCameraConnectionReliabilityMonitor sharedInstance]
+ +[ViewfinderErrorReporter _logError:]
+ +[ViewfinderErrorReporter _logError:].cold.1
+ +[ViewfinderErrorReporter _logError:].cold.2
+ +[ViewfinderErrorReporter report:status:]
+ -[CCCameraConnection _closePreview]
+ -[CCCameraConnection _openPreview]
+ -[CCCameraConnection cameraViewfinderSession:previewStreamDidCloseWithStatus:].cold.2
+ -[CCCameraConnection didUpdateStereoCaptureStatus:]
+ -[CCCameraConnectionReliabilityMonitor .cxx_destruct]
+ -[CCCameraConnectionReliabilityMonitor decrementInstanceCount]
+ -[CCCameraConnectionReliabilityMonitor didConnect]
+ -[CCCameraConnectionReliabilityMonitor didDisconnect]
+ -[CCCameraConnectionReliabilityMonitor incrementInstanceCount]
+ -[CCCameraConnectionReliabilityMonitor init]
+ -[ViewfinderErrorReport .cxx_destruct]
+ -[ViewfinderErrorReport _codeDescription]
+ -[ViewfinderErrorReport code]
+ -[ViewfinderErrorReport date]
+ -[ViewfinderErrorReport initWithCode:status:date:]
+ -[ViewfinderErrorReport loggingDescription]
+ -[ViewfinderErrorReport status]
+ -[ViewfinderErrorReport ttrDescriptionWithDateFormatter:]
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_CCCameraConnectionReliabilityMonitor
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_ViewfinderErrorReport
+ _OBJC_CLASS_$_ViewfinderErrorReporter
+ _OBJC_IVAR_$_CCCameraConnection._remoteViewfinderSessionState
+ _OBJC_IVAR_$_CCCameraConnection._stereoCaptureStatus
+ _OBJC_IVAR_$_CCCameraConnectionReliabilityMonitor._instanceCount
+ _OBJC_IVAR_$_CCCameraConnectionReliabilityMonitor._isConnected
+ _OBJC_IVAR_$_CCCameraConnectionReliabilityMonitor._lastConnectTime
+ _OBJC_IVAR_$_ViewfinderErrorReport._code
+ _OBJC_IVAR_$_ViewfinderErrorReport._date
+ _OBJC_IVAR_$_ViewfinderErrorReport._status
+ _OBJC_METACLASS_$_CCCameraConnectionReliabilityMonitor
+ _OBJC_METACLASS_$_ViewfinderErrorReport
+ _OBJC_METACLASS_$_ViewfinderErrorReporter
+ _ViewfinderErrorReportKey
+ _ViewfinderErrorReporterDidReportErrorNotification
+ __OBJC_$_CLASS_METHODS_CCCameraConnectionReliabilityMonitor
+ __OBJC_$_CLASS_METHODS_ViewfinderErrorReporter
+ __OBJC_$_INSTANCE_METHODS_CCCameraConnectionReliabilityMonitor
+ __OBJC_$_INSTANCE_METHODS_ViewfinderErrorReport
+ __OBJC_$_INSTANCE_VARIABLES_CCCameraConnectionReliabilityMonitor
+ __OBJC_$_INSTANCE_VARIABLES_ViewfinderErrorReport
+ __OBJC_$_PROP_LIST_ViewfinderErrorReport
+ __OBJC_CLASS_RO_$_CCCameraConnectionReliabilityMonitor
+ __OBJC_CLASS_RO_$_ViewfinderErrorReport
+ __OBJC_CLASS_RO_$_ViewfinderErrorReporter
+ __OBJC_METACLASS_RO_$_CCCameraConnectionReliabilityMonitor
+ __OBJC_METACLASS_RO_$_ViewfinderErrorReport
+ __OBJC_METACLASS_RO_$_ViewfinderErrorReporter
+ ___26-[CCCameraConnection init]_block_invoke.6
+ ___30-[CCCameraConnection _connect]_block_invoke.89
+ ___37+[ViewfinderErrorReporter _logError:]_block_invoke
+ ___41+[ViewfinderErrorReporter report:status:]_block_invoke
+ ___41+[ViewfinderErrorReporter report:status:]_block_invoke_2
+ ___51-[CCCameraConnection didUpdateStereoCaptureStatus:]_block_invoke
+ ___51-[CCCameraConnection didUpdateStereoCaptureStatus:]_block_invoke.cold.1
+ ___54+[CCCameraConnectionReliabilityMonitor sharedInstance]_block_invoke
+ ___62-[CCCameraConnectionReliabilityMonitor incrementInstanceCount]_block_invoke
+ ___63-[CCCameraConnection cameraViewfinder:viewfinderSessionDidEnd:]_block_invoke
+ ___63-[CCCameraConnection cameraViewfinder:viewfinderSessionDidEnd:]_block_invoke.cold.1
+ ___65-[CCCameraConnection cameraViewfinder:viewfinderSessionDidBegin:]_block_invoke
+ ___65-[CCCameraConnection cameraViewfinder:viewfinderSessionDidBegin:]_block_invoke.cold.1
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_44_e19_"NSDictionary"8?0l
+ ___block_descriptor_44_e5_v8?0l
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
+ __logError:.log
+ __logError:.onceToken
+ __ncStereoCaptureStatusFromCCStereoCaptureStatus
+ _dispatch_after
+ _dispatch_get_global_queue
+ _objc_msgSend$_closePreview
+ _objc_msgSend$_codeDescription
+ _objc_msgSend$_logError:
+ _objc_msgSend$_openPreview
+ _objc_msgSend$decrementInstanceCount
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$didConnect
+ _objc_msgSend$didDisconnect
+ _objc_msgSend$incrementInstanceCount
+ _objc_msgSend$initWithCode:status:date:
+ _objc_msgSend$loggingDescription
+ _objc_msgSend$now
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$postNotificationName:object:userInfo:
+ _objc_msgSend$report:status:
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$timeIntervalSinceNow
+ _objc_msgSend$xpc_didUpdateStereoCaptureStatus:
+ _objc_msgSend$xpc_viewfinderSessionStateDidChange:
+ _sharedInstance.instance
+ _sharedInstance.onceToken
- -[CCCameraConnection _captureButtonDown]
- -[CCCameraConnection _captureButtonUp]
- -[CCCameraConnection _connect].cold.1
- -[CCCameraConnection _currentCameraAppOrientation]
- -[CCCameraConnection _handleCaptureStartTimerFired:]
- -[CCCameraConnection _handleDockKitConnectedEvent:]
- -[CCCameraConnection _handleDockKitSystemEvent:]
- -[CCCameraConnection _handleInterruption].cold.1
- -[CCCameraConnection _handleInterruption].cold.2
- -[CCCameraConnection _isShowingLivePreview]
- -[CCCameraConnection _isSpatialCapture]
- -[CCCameraConnection _registerForDockKitButtonEvents]
- -[CCCameraConnection _reportToDockKitCameraModeChangedIfNeeded]
- -[CCCameraConnection _reportToDockKitCameraStartCaptureIfNeeded]
- -[CCCameraConnection _reportToDockKitCameraStopCaptureIfNeeded]
- -[CCCameraConnection _reportToDockKitPanoramaDirectionChangedIfNeeded:]
- -[CCCameraConnection _resetCurrentZoomMagnificationState]
- -[CCCameraConnection _scheduleStartCaptureIfNeeded]
- -[CCCameraConnection _startCaptureIfNeeded]
- -[CCCameraConnection _stopCaptureIfNeeded]
- -[CCCameraConnection _stopScheduledCaptureIfNeeded]
- -[CCCameraConnection _updateCurrentZoomMagnificationState]
- -[CCCameraConnection closePreview]
- -[CCCameraConnection openPreview]
- -[CCCameraConnection spatialModeDidChange]
- _OBJC_CLASS_$_DKSystemEventsAgent
- _OBJC_CLASS_$_NSTimer
- _OBJC_IVAR_$_CCCameraConnection._captureStartTimer
- _OBJC_IVAR_$_CCCameraConnection._connectedToDockKitDevice
- _OBJC_IVAR_$_CCCameraConnection._currentZoomMagnification
- _OBJC_IVAR_$_CCCameraConnection._dockKitAgent
- _OBJC_IVAR_$_CCCameraConnection._zoomInProgress
- _OBJC_IVAR_$_CCCameraConnection._zoomMagnificationChanged
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- ___26-[CCCameraConnection init]_block_invoke.5
- ___26-[CCCameraConnection init]_block_invoke.5.cold.1
- ___26-[CCCameraConnection init]_block_invoke_2.cold.1
- ___30-[CCCameraConnection _connect]_block_invoke.91
- ___30-[CCCameraConnection _connect]_block_invoke.cold.1
- ___30-[CCCameraConnection _connect]_block_invoke_2.cold.1
- ___38-[CCCameraConnection _captureButtonUp]_block_invoke
- ___42-[CCCameraConnection _stopCaptureIfNeeded]_block_invoke
- ___42-[CCCameraConnection spatialModeDidChange]_block_invoke
- ___42-[CCCameraConnection spatialModeDidChange]_block_invoke.cold.1
- ___43-[CCCameraConnection _startCaptureIfNeeded]_block_invoke
- ___48-[CCCameraConnection _handleDockKitSystemEvent:]_block_invoke
- ___48-[CCCameraConnection _handleDockKitSystemEvent:]_block_invoke.237
- ___48-[CCCameraConnection _handleDockKitSystemEvent:]_block_invoke.cold.1
- ___49-[CCCameraConnection showingLivePreviewDidChange]_block_invoke
- ___49-[CCCameraConnection showingLivePreviewDidChange]_block_invoke.cold.1
- ___51-[CCCameraConnection _scheduleStartCaptureIfNeeded]_block_invoke
- ___53-[CCCameraConnection _registerForDockKitButtonEvents]_block_invoke
- ___53-[CCCameraConnection _registerForDockKitButtonEvents]_block_invoke_2
- ___53-[CCCameraConnection _registerForDockKitButtonEvents]_block_invoke_3
- ___64-[CCCameraConnection _reportToDockKitCameraStartCaptureIfNeeded]_block_invoke
- ___block_descriptor_40_e8_32s_e23_v16?0"DKSystemEvent"8ls32l8
- ___block_descriptor_40_e8_32s_e8_v12?0B8ls32l8
- ___block_descriptor_40_e8_32s_e8_v12?0f8ls32l8
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
- ___block_literal_global.141
- ___block_literal_global.236
- ___block_literal_global.96
- ___block_literal_global.98
- _objc_msgSend$_captureButtonDown
- _objc_msgSend$_captureButtonUp
- _objc_msgSend$_currentCameraAppOrientation
- _objc_msgSend$_handleDockKitConnectedEvent:
- _objc_msgSend$_handleDockKitSystemEvent:
- _objc_msgSend$_isShowingLivePreview
- _objc_msgSend$_isSpatialCapture
- _objc_msgSend$_registerForDockKitButtonEvents
- _objc_msgSend$_reportToDockKitCameraModeChangedIfNeeded
- _objc_msgSend$_reportToDockKitCameraStartCaptureIfNeeded
- _objc_msgSend$_reportToDockKitCameraStopCaptureIfNeeded
- _objc_msgSend$_reportToDockKitPanoramaDirectionChangedIfNeeded:
- _objc_msgSend$_resetCurrentZoomMagnificationState
- _objc_msgSend$_scheduleStartCaptureIfNeeded
- _objc_msgSend$_startCaptureIfNeeded
- _objc_msgSend$_stopCaptureIfNeeded
- _objc_msgSend$_stopScheduledCaptureIfNeeded
- _objc_msgSend$_updateCurrentZoomMagnificationState
- _objc_msgSend$cameraConnectionIsShowingLivePreview:
- _objc_msgSend$cameraConnectionIsSpatialCapture:
- _objc_msgSend$cameraShutterModeChanged:
- _objc_msgSend$closePreview
- _objc_msgSend$deregisterForSystemEvents
- _objc_msgSend$doubleValue
- _objc_msgSend$intValue
- _objc_msgSend$isValid
- _objc_msgSend$openPreview
- _objc_msgSend$panoramaCaptureDirectionChanged:
- _objc_msgSend$registerForSystemEvents:forConnectedEvents:
- _objc_msgSend$scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:
- _objc_msgSend$startCaptureIfNeeded:orientation:finished:
- _objc_msgSend$stopCaptureIfNeeded:
- _objc_msgSend$type
- _objc_msgSend$value
- _objc_msgSend$xpc_showingLivePreviewDidChange:
- _objc_msgSend$xpc_spatialCaptureDidChange:
CStrings:
+ "!"
+ "%@, date: %@"
+ "-[CCCameraConnection _closePreview]"
+ "-[CCCameraConnection _openPreview]"
+ "-[CCCameraConnection init]"
+ "@\"NSDictionary\"8@?0"
+ "@24@0:8@16"
+ "@36@0:8q16i24@28"
+ "Active"
+ "AvailableAndNotSuggested"
+ "AvailableAndSuggested"
+ "C"
+ "CCCameraConnectionReliabilityMonitor"
+ "CC_Leaked"
+ "CC_RapidDisconnection"
+ "CC_SessionPreviewStreamDidClose"
+ "CC_UnpexpectedInstanceCount"
+ "Disabled"
+ "EnabledAndNotSuggested"
+ "EnabledAndSuggested"
+ "EnabledWideDualLowLightAvailable"
+ "ErrorReport"
+ "NC_FigNeroDisconnectionRetryAttempt"
+ "NC_FigNeroStartErr"
+ "NC_FigNeroStopErr"
+ "NotEnoughLightWideDualLowLightAvailable"
+ "PeakPowerExceeded"
+ "Reporting error %@"
+ "SpatialPhoto"
+ "SpatialVideo"
+ "T@\"NSDate\",R,N,V_date"
+ "Ti,R,N,V_status"
+ "Tq,R,N,V_code"
+ "ViewfinderErrorReport"
+ "ViewfinderErrorReporter"
+ "ViewfinderErrorReporterDidReportErrorNotification"
+ "Vv28@0:8B16@?<v@?@\"NSOrderedSet\"q@\"NSOrderedSet\"qB@\"NSDate\"B@\"NSDate\"qBBfBff@\"NSArray\"fqqqqqqqqBBQqq>20"
+ "_closePreview"
+ "_code"
+ "_codeDescription"
+ "_date"
+ "_instanceCount"
+ "_isConnected"
+ "_lastConnectTime"
+ "_logError:"
+ "_openPreview"
+ "_remoteViewfinderSessionState"
+ "_status"
+ "_stereoCaptureStatus"
+ "code"
+ "code=%@ status=%d"
+ "com.apple.NanoCamera.viewfinderError"
+ "decrementInstanceCount"
+ "defaultCenter"
+ "didConnect"
+ "didDisconnect"
+ "didUpdateStereoCaptureStatus:"
+ "i16@0:8"
+ "incrementInstanceCount"
+ "initWithCode:status:date:"
+ "loggingDescription"
+ "now"
+ "numberWithInt:"
+ "postNotificationName:object:userInfo:"
+ "previewStreamDidCloseWithStatus: %d"
+ "report:status:"
+ "sharedInstance"
+ "status"
+ "stringFromDate:"
+ "supportedCaptureDevices:%@ captureDevice:%@ supportedCaptureModes:%@ captureMode:%@ capturing:%d captureStartDate:%@ capturingPaused:%d capturePauseDate:%@ orientation:%@ toggleCameraDeviceSupport:%d zoomSupport:%d zoomAmount:%f zoomMagnificationSupport:%d minimumZoomMagnification:%f maximumZoomMagnification:%f significantZoomMagnifications:%@ currentZoomMagnification:%f flashSupport:%@ flashMode:%@ hdrSupport:%@ hdrMode:%@ irisSupport:%@ irisMode:%@ sharedLibrarySupport:%@ sharedLibraryMode:%@ supportsMomentCapture:%d burstSupport:%d viewfinderSessionState:%lu shallowDepthOfFieldStatus:%@ stereoCaptureStatus:%@"
+ "timeIntervalSinceNow"
+ "ttrDescriptionWithDateFormatter:"
+ "v28@0:8q16i24"
+ "xpc_didUpdateStereoCaptureStatus:"
+ "xpc_viewfinderSessionStateDidChange:"
+ "\xf0A"
- "-[CCCameraConnection closePreview]"
- "-[CCCameraConnection openPreview]"
- "@\"DKSystemEventsAgent\""
- "@\"NSTimer\""
- "C16@0:8"
- "Vv20@0:8B16"
- "Vv28@0:8B16@?<v@?@\"NSOrderedSet\"q@\"NSOrderedSet\"qB@\"NSDate\"B@\"NSDate\"qBBfBff@\"NSArray\"fqqqqqqqqBBBqB>20"
- "_captureButtonDown"
- "_captureButtonUp"
- "_captureStartTimer"
- "_connectedToDockKitDevice"
- "_currentCameraAppOrientation"
- "_dockKitAgent"
- "_handleCaptureStartTimerFired:"
- "_handleDockKitConnectedEvent:"
- "_handleDockKitSystemEvent:"
- "_isShowingLivePreview"
- "_isSpatialCapture"
- "_registerForDockKitButtonEvents"
- "_reportToDockKitCameraModeChangedIfNeeded"
- "_reportToDockKitCameraStartCaptureIfNeeded"
- "_reportToDockKitCameraStopCaptureIfNeeded"
- "_reportToDockKitPanoramaDirectionChangedIfNeeded:"
- "_resetCurrentZoomMagnificationState"
- "_scheduleStartCaptureIfNeeded"
- "_startCaptureIfNeeded"
- "_stopCaptureIfNeeded"
- "_stopScheduledCaptureIfNeeded"
- "_updateCurrentZoomMagnificationState"
- "_zoomInProgress"
- "_zoomMagnificationChanged"
- "cameraConnectionIsShowingLivePreview:"
- "cameraConnectionIsSpatialCapture:"
- "cameraShutterModeChanged:"
- "closePreview"
- "deregisterForSystemEvents"
- "dockkit capture failed."
- "doubleValue"
- "flip event triggered. Payload is %d"
- "intValue"
- "isValid"
- "openPreview"
- "panoramaCaptureDirectionChanged:"
- "registerForSystemEvents:forConnectedEvents:"
- "scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:"
- "shutter event triggered. Payload is %d"
- "spatialModeDidChange"
- "startCaptureIfNeeded:orientation:finished:"
- "status: %d"
- "stopCaptureIfNeeded:"
- "supportedCaptureDevices:%@ captureDevice:%@ supportedCaptureModes:%@ captureMode:%@ capturing:%d captureStartDate:%@ capturingPaused:%d capturePauseDate:%@ orientation:%@ toggleCameraDeviceSupport:%d zoomSupport:%d zoomAmount:%f zoomMagnificationSupport:%d minimumZoomMagnification:%f maximumZoomMagnification:%f significantZoomMagnifications:%@ currentZoomMagnification:%f flashSupport:%@ flashMode:%@ hdrSupport:%@ hdrMode:%@ irisSupport:%@ irisMode:%@ sharedLibrarySupport:%@ sharedLibraryMode:%@ supportsMomentCapture:%d burstSupport:%d showingLivePreview:%d shallowDepthOfFieldStatus:%@ isSpatialCapture:%d"
- "type"
- "unknown event triggered, ignoring"
- "v12@?0B8"
- "v12@?0f8"
- "v16@?0@\"DKSystemEvent\"8"
- "v20@0:8B16"
- "value"
- "xpc_showingLivePreviewDidChange:"
- "xpc_spatialCaptureDidChange:"
- "zoom event triggered. Payload is %0.2f"
- "zoom set to %0.2f"
- "\xf0Q"

```
