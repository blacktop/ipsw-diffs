## companioncamerad

> `/System/Library/PrivateFrameworks/CompanionCamera.framework/Support/companioncamerad`

```diff

-2022.300.12.0.0
-  __TEXT.__text: 0x20360
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_stubs: 0x1e00
-  __TEXT.__objc_methlist: 0x2fec
-  __TEXT.__cstring: 0x11cf
-  __TEXT.__objc_methname: 0x352c
-  __TEXT.__objc_classname: 0x4bb
-  __TEXT.__objc_methtype: 0x1183
-  __TEXT.__const: 0xf0
-  __TEXT.__gcc_except_tab: 0xe0
-  __TEXT.__oslogstring: 0x741
+2023.100.17.0.0
+  __TEXT.__text: 0x22b28
+  __TEXT.__auth_stubs: 0x740
+  __TEXT.__objc_stubs: 0x20c0
+  __TEXT.__objc_methlist: 0x302c
+  __TEXT.__const: 0x110
+  __TEXT.__gcc_except_tab: 0xe8
+  __TEXT.__cstring: 0x1436
+  __TEXT.__oslogstring: 0x767
+  __TEXT.__objc_methname: 0x37bd
+  __TEXT.__objc_classname: 0x4c9
+  __TEXT.__objc_methtype: 0x11c0
   __TEXT.__dlopen_cstrs: 0x4f
-  __TEXT.__unwind_info: 0x8b8
-  __DATA_CONST.__auth_got: 0x390
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0xad0
-  __DATA_CONST.__cfstring: 0xca0
-  __DATA_CONST.__objc_classlist: 0x168
+  __TEXT.__unwind_info: 0x8d0
+  __DATA_CONST.__auth_got: 0x3b0
+  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__const: 0xc18
+  __DATA_CONST.__cfstring: 0x1020
+  __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x4c98
-  __DATA.__objc_selrefs: 0xef8
-  __DATA.__objc_ivar: 0x298
-  __DATA.__objc_data: 0xe10
+  __DATA.__objc_const: 0x4d78
+  __DATA.__objc_selrefs: 0xfc0
+  __DATA.__objc_ivar: 0x2a4
+  __DATA.__objc_data: 0xe60
   __DATA.__data: 0x2a0
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
+  - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 08199D45-E0FF-3979-AF7E-8EEFD8AFB695
-  Functions: 1012
-  Symbols:   162
-  CStrings:  1158
+  UUID: 5248C426-04FB-39F5-86AE-B72A70A8EB1F
+  Functions: 1024
+  Symbols:   168
+  CStrings:  1253
 
Symbols:
+ _AnalyticsSendEventLazy
+ _CFPreferencesAppSynchronize
+ _CFPreferencesSetAppValue
+ _OBJC_CLASS_$_NPSManager
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSNotificationCenter
+ __os_log_fault_impl
+ _dispatch_get_global_queue
+ _kCFBooleanFalse
+ _kCFBooleanTrue
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _objc_retain_x25
CStrings:
+ "%@, date: %@"
+ "@\"NPSManager\""
+ "@\"NSDate\""
+ "@\"NSDictionary\"8@?0"
+ "@36@0:8q16i24@28"
+ "Active"
+ "AvailableAndNotSuggested"
+ "AvailableAndSuggested"
+ "CC_Leaked"
+ "CC_RapidDisconnection"
+ "CC_SessionPreviewStreamDidClose"
+ "CC_UnpexpectedInstanceCount"
+ "CompanionCameraApplicationLastOpenDate"
+ "CompanionCameraApplicationOpen"
+ "Completed setting NPS companion camera open state preference: %{BOOL}d"
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
+ "Remote side is inactive."
+ "Reporting error %@"
+ "Sending open state change."
+ "Setting NPS companion camera open state preference: %{BOOL}d"
+ "SpatialPhoto"
+ "SpatialVideo"
+ "StringAsStereoCaptureStatus:"
+ "T@\"NSDate\",R,N,V_date"
+ "TB,N,V_viewfinderSessionActive"
+ "Ti,N,V_stereoCaptureStatus"
+ "Ti,R,N,V_status"
+ "Tq,R,N,V_code"
+ "ViewfinderErrorReport"
+ "ViewfinderErrorReporter"
+ "ViewfinderErrorReporterDidReportErrorNotification"
+ "Vv28@0:8B16@?<v@?@\"NSOrderedSet\"q@\"NSOrderedSet\"qB@\"NSDate\"B@\"NSDate\"qBBfBff@\"NSArray\"fqqqqqqqqBBQqq>20"
+ "[lifecycle] _cameraPreviewIDSSocketCreationFailed"
+ "_cameraPreviewIDSSocketCreationFailed"
+ "_code"
+ "_codeDescription"
+ "_date"
+ "_logError:"
+ "_npsManager"
+ "_queue_setCompanionCameraOpenStatePreference:"
+ "_setCompanionCameraOpenStatePreference:"
+ "_setError"
+ "_status"
+ "_stereoCaptureStatus"
+ "_viewfinderSessionActive"
+ "arrayWithObjects:count:"
+ "code"
+ "code=%@ status=%d"
+ "com.apple.NanoCamera.viewfinderError"
+ "companioncamerad detected com.apple.fignero.CameraPreviewIDSSocketCreationFailed."
+ "date"
+ "defaultCenter"
+ "getBytes:range:"
+ "hasError"
+ "hasStereoCaptureStatus"
+ "hasViewfinderSessionActive"
+ "initWithCode:status:date:"
+ "loggingDescription"
+ "now"
+ "position"
+ "postNotificationName:object:userInfo:"
+ "q16@0:8"
+ "report:status:"
+ "setHasStereoCaptureStatus:"
+ "setHasViewfinderSessionActive:"
+ "setPosition:"
+ "setStereoCaptureStatus:"
+ "setViewfinderSessionActive:"
+ "setWithArray:"
+ "status"
+ "stereoCaptureStatus"
+ "stereoCaptureStatusAsString:"
+ "stringFromDate:"
+ "supportedCaptureDevice:%@ captureDevice:%@ supportedCaptureModes:%@ captureMode:%@ capturing:%d captureStartDate:%@ capturingPaused:%d capturePauseDate:%@ orientation:%@ toggleCameraDeviceSupport:%d zoomSupport:%d zoomAmount:%f flashSupport:%@ flashMode:%@ hdrSupport:%@ hdrMode:%@ irisSupport:%@ irisMode:%@ sharedLibrarySupport:%@ sharedLibraryMode:%@ supportsMomentCapture:%d burstSupport:%d viewfinderSessionState:%lu shallowDepthOfFieldStatus:%@ stereoCaptureStatus:%@"
+ "synchronizeUserDefaultsDomain:keys:"
+ "ttrDescriptionWithDateFormatter:"
+ "v204@?0@\"NSOrderedSet\"8q16@\"NSOrderedSet\"24q32B40@\"NSDate\"44B52@\"NSDate\"56q64B72B76f80B84f88f92@\"NSArray\"96f104q108q116q124q132q140q148q156q164B172B176Q180q188q196"
+ "v28@0:8q16i24"
+ "viewfinderSessionActive"
+ "xpc_didUpdateStereoCaptureStatus:"
+ "xpc_viewfinderSessionStateDidChange:"
+ "{?=\"capturePauseDate\"b1\"captureStartDate\"b1\"captureDevice\"b1\"captureMode\"b1\"currentZoomMagnification\"b1\"flashMode\"b1\"flashSupport\"b1\"hdrMode\"b1\"hdrSupport\"b1\"irisMode\"b1\"irisSupport\"b1\"maximumZoomMagnification\"b1\"minimumZoomMagnification\"b1\"orientation\"b1\"shallowDepthOfFieldStatus\"b1\"sharedLibraryMode\"b1\"sharedLibrarySupport\"b1\"stereoCaptureStatus\"b1\"zoomAmount\"b1\"burstSupport\"b1\"capturing\"b1\"capturingPaused\"b1\"isSpatialCapture\"b1\"supportsMomentCapture\"b1\"toggleCameraDeviceSupport\"b1\"viewfinderSessionActive\"b1\"zoomMagnificationSupport\"b1\"zoomSupport\"b1}"
- "Active camera reset, not starting preview endpoint or sending open message."
- "Camera completed setup. Enqueuing finalization after XPC connection settle interval."
- "Camera setup finalized. Sending open state change. (willStartPreviewEndpoint=%d)"
- "NCCameraOpenStateChangeResponse"
- "TB,N,V_acknowledge"
- "TB,N,V_showingLivePreview"
- "Vv20@0:8B16"
- "Vv28@0:8B16@?<v@?@\"NSOrderedSet\"q@\"NSOrderedSet\"qB@\"NSDate\"B@\"NSDate\"qBBfBff@\"NSArray\"fqqqqqqqqBBBqB>20"
- "[lifecycle] cameraPreviewIDSSocketCreationFailed"
- "_acknowledge"
- "_showingLivePreview"
- "acknowledge"
- "cameraPreviewIDSSocketCreationFailed"
- "connectionDidTearDown"
- "hasAcknowledge"
- "hasShowingLivePreview"
- "setAcknowledge:"
- "setHasAcknowledge:"
- "setHasShowingLivePreview:"
- "setShowingLivePreview:"
- "showingLivePreview"
- "supportedCaptureDevice:%@ captureDevice:%@ supportedCaptureModes:%@ captureMode:%@ capturing:%d captureStartDate:%@ capturingPaused:%d capturePauseDate:%@ orientation:%@ toggleCameraDeviceSupport:%d zoomSupport:%d zoomAmount:%f flashSupport:%@ flashMode:%@ hdrSupport:%@ hdrMode:%@ irisSupport:%@ irisMode:%@ sharedLibrarySupport:%@ sharedLibraryMode:%@ supportsMomentCapture:%d burstSupport:%d showingLivePreview:%d shallowDepthOfFieldStatus:%@, spatial:%d"
- "v16@?0@\"NCCameraOpenStateChangeResponse\"8"
- "v196@?0@\"NSOrderedSet\"8q16@\"NSOrderedSet\"24q32B40@\"NSDate\"44B52@\"NSDate\"56q64B72B76f80B84f88f92@\"NSArray\"96f104q108q116q124q132q140q148q156q164B172B176B180q184B192"
- "xpc_showingLivePreviewDidChange:"
- "xpc_spatialCaptureDidChange:"
- "{?=\"acknowledge\"b1}"
- "{?=\"capturePauseDate\"b1\"captureStartDate\"b1\"captureDevice\"b1\"captureMode\"b1\"currentZoomMagnification\"b1\"flashMode\"b1\"flashSupport\"b1\"hdrMode\"b1\"hdrSupport\"b1\"irisMode\"b1\"irisSupport\"b1\"maximumZoomMagnification\"b1\"minimumZoomMagnification\"b1\"orientation\"b1\"shallowDepthOfFieldStatus\"b1\"sharedLibraryMode\"b1\"sharedLibrarySupport\"b1\"zoomAmount\"b1\"burstSupport\"b1\"capturing\"b1\"capturingPaused\"b1\"isSpatialCapture\"b1\"showingLivePreview\"b1\"supportsMomentCapture\"b1\"toggleCameraDeviceSupport\"b1\"zoomMagnificationSupport\"b1\"zoomSupport\"b1}"

```
