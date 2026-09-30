## companioncamerad

> `/System/Library/PrivateFrameworks/CompanionCamera.framework/Support/companioncamerad`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__data`

```diff

 2024.100.18.0.0
-  __TEXT.__text: 0x24064
-  __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_stubs: 0x20c0
-  __TEXT.__objc_methlist: 0x30a4
+  __TEXT.__text: 0x27c68
+  __TEXT.__auth_stubs: 0x780
+  __TEXT.__objc_stubs: 0x2320
+  __TEXT.__objc_methlist: 0x3574
   __TEXT.__const: 0x120
-  __TEXT.__gcc_except_tab: 0xc4
-  __TEXT.__cstring: 0x14e8
-  __TEXT.__oslogstring: 0x7bd
-  __TEXT.__objc_methname: 0x3870
-  __TEXT.__objc_classname: 0x4c1
-  __TEXT.__objc_methtype: 0x1301
+  __TEXT.__gcc_except_tab: 0x164
+  __TEXT.__cstring: 0x1934
+  __TEXT.__oslogstring: 0x891
+  __TEXT.__objc_methname: 0x3ff2
+  __TEXT.__objc_classname: 0x57f
+  __TEXT.__objc_methtype: 0x13db
   __TEXT.__dlopen_cstrs: 0x4f
-  __TEXT.__unwind_info: 0x8f0
-  __DATA_CONST.__const: 0xc78
-  __DATA_CONST.__cfstring: 0x1020
-  __DATA_CONST.__objc_classlist: 0x170
+  __TEXT.__unwind_info: 0x9f8
+  __DATA_CONST.__const: 0xd28
+  __DATA_CONST.__cfstring: 0x13c0
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x150
-  __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x3b0
-  __DATA_CONST.__got: 0x138
-  __DATA.__objc_const: 0x4df8
-  __DATA.__objc_selrefs: 0xfd0
-  __DATA.__objc_ivar: 0x2a4
-  __DATA.__objc_data: 0xe60
+  __DATA_CONST.__objc_superrefs: 0x178
+  __DATA_CONST.__objc_intobj: 0xc0
+  __DATA_CONST.__auth_got: 0x3d0
+  __DATA_CONST.__got: 0x160
+  __DATA.__objc_const: 0x5550
+  __DATA.__objc_selrefs: 0x1160
+  __DATA.__objc_ivar: 0x2ec
+  __DATA.__objc_data: 0xff0
   __DATA.__data: 0x300
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1041
-  Symbols:   168
-  CStrings:  1095
+  Functions: 1146
+  Symbols:   176
+  CStrings:  1203
 
Symbols:
+ _CFPreferencesGetAppBooleanValue
+ _OBJC_CLASS_$_NSCountedSet
+ _OBJC_CLASS_$_NSMutableString
+ __dispatch_main_q
+ __dispatch_source_type_signal
+ _objc_sync_enter
+ _objc_sync_exit
+ _signal
CStrings:
+ "%@: %lu\n"
+ "-[NCCompanionCamera startPersonalPhotographerCapture:]"
+ "-[NCCompanionCamera stopPersonalPhotographerCapture:]"
+ "-[NCCompanionCamera xpc_didStopPersonalPhotographerCapture]"
+ "-[NCCompanionCamera xpc_willStartPersonalPhotographerCapture]"
+ "@\"NSCountedSet\""
+ "@\"NSObject<OS_os_log>\""
+ "CameraAppLaunch"
+ "CameraAppLaunchFailed"
+ "CameraAppLaunchhSucceeded"
+ "CameraPreviewIDSSocketCreationFailed"
+ "CloseCameraMessageReceived"
+ "Count of events:\n%@"
+ "DaemonXPCConnectionInterruption"
+ "DaemonXPCConnectionInvalidation"
+ "DaemonXPCConnectionReceived"
+ "DeviceLowStorageSpace"
+ "EndingSoon"
+ "FigCameraViewfinderCreation"
+ "FigCameraViewfinderSessionDidBegin"
+ "FigCameraViewfinderSessionDidEnd"
+ "FigCameraViewfinderSessionOpenPreviewStream"
+ "FigCameraViewfinderSessionPreviewStreamDidClose"
+ "FigCameraViewfinderSessionPreviewStreamDidOpen"
+ "FigCameraViewfinderStarted"
+ "NCStartPersonalPhotographerCaptureRequest"
+ "NCStartPersonalPhotographerCaptureResponse"
+ "NCStopPersonalPhotographerCaptureRequest"
+ "NCStopPersonalPhotographerCaptureResponse"
+ "NoSubjectDetected"
+ "Normal"
+ "OpenCameraMessageReceived"
+ "Repeated event: %@"
+ "Reset events."
+ "StringAsPersonalPhotographerMode:"
+ "StringAsPersonalPhotographerSessionTimerState:"
+ "StringAsPersonalPhotographerStatus:"
+ "StringAsPersonalPhotographerSupport:"
+ "SubjectDetected"
+ "TB,N,V_capturingPersonalPhotographer"
+ "Ti,N,V_personalPhotographerMode"
+ "Ti,N,V_personalPhotographerSessionTimerState"
+ "Ti,N,V_personalPhotographerStatus"
+ "Ti,N,V_personalPhotographerSupport"
+ "Unexpected event: %@"
+ "ViewfinderReliability"
+ "ViewfinderReliability_CheckRepeatedEvents"
+ "ViewfinderReliability_CheckUnexpectedEvents"
+ "Vv28@0:8B16@?<v@?@\"NSOrderedSet\"q@\"NSOrderedSet\"qB@\"NSDate\"B@\"NSDate\"qBBfBff@\"NSArray\"fqqqqqqqqBBQqqqqqqB>20"
+ "_capturingPersonalPhotographer"
+ "_checkForRepeatedEvent:"
+ "_checkForUnexpectedEvent:"
+ "_events"
+ "_log"
+ "_personalPhotographerMode"
+ "_personalPhotographerSessionTimerState"
+ "_personalPhotographerStatus"
+ "_personalPhotographerSupport"
+ "_print"
+ "_printSource"
+ "_registerSources"
+ "_reset"
+ "_resetSource"
+ "appendString:"
+ "capturingPersonalPhotographer"
+ "containsObject:"
+ "countForObject:"
+ "hasCapturingPersonalPhotographer"
+ "hasPersonalPhotographerMode"
+ "hasPersonalPhotographerSessionTimerState"
+ "hasPersonalPhotographerStatus"
+ "hasPersonalPhotographerSupport"
+ "logEvent:"
+ "personalPhotographerMode"
+ "personalPhotographerMode: %ld"
+ "personalPhotographerModeAsString:"
+ "personalPhotographerSessionTimerState"
+ "personalPhotographerSessionTimerState: %ld"
+ "personalPhotographerSessionTimerStateAsString:"
+ "personalPhotographerStatus"
+ "personalPhotographerStatus: %ld"
+ "personalPhotographerStatusAsString:"
+ "personalPhotographerSupport"
+ "personalPhotographerSupport: %ld"
+ "personalPhotographerSupportAsString:"
+ "set"
+ "setCapturingPersonalPhotographer:"
+ "setHasCapturingPersonalPhotographer:"
+ "setHasPersonalPhotographerMode:"
+ "setHasPersonalPhotographerSessionTimerState:"
+ "setHasPersonalPhotographerStatus:"
+ "setHasPersonalPhotographerSupport:"
+ "setPersonalPhotographerMode:"
+ "setPersonalPhotographerSessionTimerState:"
+ "setPersonalPhotographerStatus:"
+ "setPersonalPhotographerSupport:"
+ "sharedInstance"
+ "startPersonalPhotographerCapture:"
+ "stopPersonalPhotographerCapture:"
+ "string"
+ "v240@?0@\"NSOrderedSet\"8q16@\"NSOrderedSet\"24q32B40@\"NSDate\"44B52@\"NSDate\"56q64B72B76f80B84f88f92@\"NSArray\"96f104q108q116q124q132q140q148q156q164B172B176Q180q188q196q204q212q220q228B236"
+ "v24@0:8q16"
+ "xpc_didStopPersonalPhotographerCapture"
+ "xpc_personalPhotographerModeDidChange:"
+ "xpc_personalPhotographerSessionTimerStateDidChange:"
+ "xpc_personalPhotographerStatusDidChange:"
+ "xpc_personalPhotographerSupportDidChange:"
+ "xpc_startPersonalPhotographerSessionWithReply:"
+ "xpc_stopPersonalPhotographerSessionWithReply:"
+ "xpc_willStartPersonalPhotographerCapture"
+ "{?=\"capturePauseDate\"b1\"captureStartDate\"b1\"captureDevice\"b1\"captureMode\"b1\"currentZoomMagnification\"b1\"flashMode\"b1\"flashSupport\"b1\"hdrMode\"b1\"hdrSupport\"b1\"irisMode\"b1\"irisSupport\"b1\"maximumZoomMagnification\"b1\"minimumZoomMagnification\"b1\"orientation\"b1\"personalPhotographerMode\"b1\"personalPhotographerSessionTimerState\"b1\"personalPhotographerStatus\"b1\"personalPhotographerSupport\"b1\"shallowDepthOfFieldStatus\"b1\"sharedLibraryMode\"b1\"sharedLibrarySupport\"b1\"stereoCaptureStatus\"b1\"zoomAmount\"b1\"burstSupport\"b1\"capturing\"b1\"capturingPaused\"b1\"capturingPersonalPhotographer\"b1\"isSpatialCapture\"b1\"supportsMomentCapture\"b1\"toggleCameraDeviceSupport\"b1\"viewfinderSessionActive\"b1\"zoomMagnificationSupport\"b1\"zoomSupport\"b1}"
- "Vv28@0:8B16@?<v@?@\"NSOrderedSet\"q@\"NSOrderedSet\"qB@\"NSDate\"B@\"NSDate\"qBBfBff@\"NSArray\"fqqqqqqqqBBQqq>20"
- "v204@?0@\"NSOrderedSet\"8q16@\"NSOrderedSet\"24q32B40@\"NSDate\"44B52@\"NSDate\"56q64B72B76f80B84f88f92@\"NSArray\"96f104q108q116q124q132q140q148q156q164B172B176Q180q188q196"
- "{?=\"capturePauseDate\"b1\"captureStartDate\"b1\"captureDevice\"b1\"captureMode\"b1\"currentZoomMagnification\"b1\"flashMode\"b1\"flashSupport\"b1\"hdrMode\"b1\"hdrSupport\"b1\"irisMode\"b1\"irisSupport\"b1\"maximumZoomMagnification\"b1\"minimumZoomMagnification\"b1\"orientation\"b1\"shallowDepthOfFieldStatus\"b1\"sharedLibraryMode\"b1\"sharedLibrarySupport\"b1\"stereoCaptureStatus\"b1\"zoomAmount\"b1\"burstSupport\"b1\"capturing\"b1\"capturingPaused\"b1\"isSpatialCapture\"b1\"supportsMomentCapture\"b1\"toggleCameraDeviceSupport\"b1\"viewfinderSessionActive\"b1\"zoomMagnificationSupport\"b1\"zoomSupport\"b1}"
```
