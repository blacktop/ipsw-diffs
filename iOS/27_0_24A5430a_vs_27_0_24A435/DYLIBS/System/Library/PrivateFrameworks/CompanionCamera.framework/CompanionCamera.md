## CompanionCamera

> `/System/Library/PrivateFrameworks/CompanionCamera.framework/CompanionCamera`

```diff

 2024.100.18.0.0
-  __TEXT.__text: 0x80c8
-  __TEXT.__objc_methlist: 0xa54
+  __TEXT.__text: 0x9a14
+  __TEXT.__objc_methlist: 0xbdc
   __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x78
-  __TEXT.__oslogstring: 0x53b
-  __TEXT.__cstring: 0xb61
-  __TEXT.__unwind_info: 0x238
+  __TEXT.__gcc_except_tab: 0x118
+  __TEXT.__oslogstring: 0x60b
+  __TEXT.__cstring: 0xfc7
+  __TEXT.__unwind_info: 0x2b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x400
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__const: 0x478
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x770
+  __DATA_CONST.__objc_selrefs: 0x898
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__got: 0xb0
-  __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x780
-  __AUTH_CONST.__objc_const: 0xa60
-  __AUTH_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__got: 0xd0
+  __AUTH_CONST.__const: 0x460
+  __AUTH_CONST.__cfstring: 0xa00
+  __AUTH_CONST.__objc_const: 0xbd8
+  __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x78
+  __DATA.__objc_ivar: 0x8c
   __DATA.__data: 0x1e0
-  __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__bss: 0x30
+  __DATA_DIRTY.__objc_data: 0x140
+  __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 233
-  Symbols:   603
-  CStrings:  135
+  Functions: 272
+  Symbols:   698
+  CStrings:  167
 
Symbols:
+ +[ViewfinderReliability sharedInstance]
+ -[CCCameraConnection _personalPhotographerMode]
+ -[CCCameraConnection _personalPhotographerSessionTimerState]
+ -[CCCameraConnection _personalPhotographerStatus]
+ -[CCCameraConnection _personalPhotographerSupport]
+ -[CCCameraConnection didStopPersonalPhotographerCapture]
+ -[CCCameraConnection personalPhotographerModeDidChange:]
+ -[CCCameraConnection personalPhotographerSessionTimerStateDidChange:]
+ -[CCCameraConnection personalPhotographerStatusDidChange:]
+ -[CCCameraConnection personalPhotographerSupportDidChange:]
+ -[CCCameraConnection willStartPersonalPhotographerCapture]
+ -[CCCameraConnection xpc_startPersonalPhotographerSessionWithReply:]
+ -[CCCameraConnection xpc_stopPersonalPhotographerSessionWithReply:]
+ -[CCCameraConnectionInternal xpc_startPersonalPhotographerSessionWithReply:]
+ -[CCCameraConnectionInternal xpc_stopPersonalPhotographerSessionWithReply:]
+ -[ViewfinderReliability .cxx_destruct]
+ -[ViewfinderReliability _checkForRepeatedEvent:]
+ -[ViewfinderReliability _checkForUnexpectedEvent:]
+ -[ViewfinderReliability _print]
+ -[ViewfinderReliability _registerSources]
+ -[ViewfinderReliability _reset]
+ -[ViewfinderReliability init]
+ -[ViewfinderReliability logEvent:]
+ GCC_except_table3
+ GCC_except_table5
+ GCC_except_table8
+ GCC_except_table9
+ _CFPreferencesGetAppBooleanValue
+ _NCPersonalPhotographerModeFromCCPersonalPhotographerMode
+ _NCPersonalPhotographerSessionTimerStateFromCCPersonalPhotographerSessionTimerState
+ _NCPersonalPhotographerStatusFromCCPersonalPhotographerStatus
+ _NCPersonalPhotographerSupportFromCCPersonalPhotographerSupport
+ _NSStringFromViewfinderReliabiliyEvent
+ _OBJC_CLASS_$_NSCountedSet
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_ViewfinderReliability
+ _OBJC_IVAR_$_CCCameraConnection._capturingPersonalPhotographer
+ _OBJC_IVAR_$_ViewfinderReliability._events
+ _OBJC_IVAR_$_ViewfinderReliability._log
+ _OBJC_IVAR_$_ViewfinderReliability._printSource
+ _OBJC_IVAR_$_ViewfinderReliability._resetSource
+ _OBJC_METACLASS_$_ViewfinderReliability
+ __OBJC_$_CLASS_METHODS_ViewfinderReliability
+ __OBJC_$_INSTANCE_METHODS_ViewfinderReliability
+ __OBJC_$_INSTANCE_VARIABLES_ViewfinderReliability
+ __OBJC_CLASS_RO_$_ViewfinderReliability
+ __OBJC_METACLASS_RO_$_ViewfinderReliability
+ ___39+[ViewfinderReliability sharedInstance]_block_invoke
+ ___41-[ViewfinderReliability _registerSources]_block_invoke
+ ___41-[ViewfinderReliability _registerSources]_block_invoke_2
+ ___56-[CCCameraConnection didStopPersonalPhotographerCapture]_block_invoke
+ ___56-[CCCameraConnection personalPhotographerModeDidChange:]_block_invoke
+ ___58-[CCCameraConnection personalPhotographerStatusDidChange:]_block_invoke
+ ___58-[CCCameraConnection willStartPersonalPhotographerCapture]_block_invoke
+ ___59-[CCCameraConnection personalPhotographerSupportDidChange:]_block_invoke
+ ___67-[CCCameraConnection xpc_stopPersonalPhotographerSessionWithReply:]_block_invoke
+ ___68-[CCCameraConnection xpc_startPersonalPhotographerSessionWithReply:]_block_invoke
+ ___69-[CCCameraConnection personalPhotographerSessionTimerStateDidChange:]_block_invoke
+ __dispatch_source_type_signal
+ __os_log_fault_impl
+ _objc_enumerationMutation
+ _objc_msgSend$_checkForRepeatedEvent:
+ _objc_msgSend$_checkForUnexpectedEvent:
+ _objc_msgSend$_personalPhotographerMode
+ _objc_msgSend$_personalPhotographerSessionTimerState
+ _objc_msgSend$_personalPhotographerStatus
+ _objc_msgSend$_personalPhotographerSupport
+ _objc_msgSend$_print
+ _objc_msgSend$_registerSources
+ _objc_msgSend$_reset
+ _objc_msgSend$addObject:
+ _objc_msgSend$appendString:
+ _objc_msgSend$cameraConnectionPersonalPhotographerMode:
+ _objc_msgSend$cameraConnectionPersonalPhotographerSessionTimerState:
+ _objc_msgSend$cameraConnectionPersonalPhotographerStatus:
+ _objc_msgSend$cameraConnectionPersonalPhotographerSupport:
+ _objc_msgSend$cameraConnectionStartPersonalPhotographerSession:
+ _objc_msgSend$cameraConnectionStopPersonalPhotographerSession:
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$countForObject:
+ _objc_msgSend$logEvent:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$set
+ _objc_msgSend$string
+ _objc_msgSend$xpc_didStopPersonalPhotographerCapture
+ _objc_msgSend$xpc_personalPhotographerModeDidChange:
+ _objc_msgSend$xpc_personalPhotographerSessionTimerStateDidChange:
+ _objc_msgSend$xpc_personalPhotographerStatusDidChange:
+ _objc_msgSend$xpc_personalPhotographerSupportDidChange:
+ _objc_msgSend$xpc_startPersonalPhotographerSessionWithReply:
+ _objc_msgSend$xpc_stopPersonalPhotographerSessionWithReply:
+ _objc_msgSend$xpc_willStartPersonalPhotographerCapture
+ _objc_sync_enter
+ _objc_sync_exit
+ _os_variant_has_internal_diagnostics
+ _signal
- _objc_release_x24
CStrings:
+ "%@: %lu\n"
+ "-[CCCameraConnection didStopPersonalPhotographerCapture]"
+ "-[CCCameraConnection personalPhotographerModeDidChange:]"
+ "-[CCCameraConnection personalPhotographerSessionTimerStateDidChange:]"
+ "-[CCCameraConnection personalPhotographerStatusDidChange:]"
+ "-[CCCameraConnection personalPhotographerSupportDidChange:]"
+ "-[CCCameraConnection willStartPersonalPhotographerCapture]"
+ "-[CCCameraConnection xpc_startPersonalPhotographerSessionWithReply:]"
+ "-[CCCameraConnection xpc_stopPersonalPhotographerSessionWithReply:]"
+ "CameraAppLaunch"
+ "CameraAppLaunchFailed"
+ "CameraAppLaunchhSucceeded"
+ "CameraPreviewIDSSocketCreationFailed"
+ "CloseCameraMessageReceived"
+ "Count of events:\n%@"
+ "DaemonXPCConnectionInterruption"
+ "DaemonXPCConnectionInvalidation"
+ "DaemonXPCConnectionReceived"
+ "FigCameraViewfinderCreation"
+ "FigCameraViewfinderSessionDidBegin"
+ "FigCameraViewfinderSessionDidEnd"
+ "FigCameraViewfinderSessionOpenPreviewStream"
+ "FigCameraViewfinderSessionPreviewStreamDidClose"
+ "FigCameraViewfinderSessionPreviewStreamDidOpen"
+ "FigCameraViewfinderStarted"
+ "OpenCameraMessageReceived"
+ "Repeated event: %@"
+ "Reset events."
+ "Unexpected event: %@"
+ "ViewfinderReliability"
+ "ViewfinderReliability_CheckRepeatedEvents"
+ "ViewfinderReliability_CheckUnexpectedEvents"
+ "supportedCaptureDevices:%@ captureDevice:%@ supportedCaptureModes:%@ captureMode:%@ capturing:%d captureStartDate:%@ capturingPaused:%d capturePauseDate:%@ orientation:%@ toggleCameraDeviceSupport:%d zoomSupport:%d zoomAmount:%f zoomMagnificationSupport:%d minimumZoomMagnification:%f maximumZoomMagnification:%f significantZoomMagnifications:%@ currentZoomMagnification:%f flashSupport:%@ flashMode:%@ hdrSupport:%@ hdrMode:%@ irisSupport:%@ irisMode:%@ sharedLibrarySupport:%@ sharedLibraryMode:%@ supportsMomentCapture:%d burstSupport:%d viewfinderSessionState:%lu shallowDepthOfFieldStatus:%@ stereoCaptureStatus:%@ personalPhotographerSupport:%ld personalPhotographerMode:%ld personalPhotographerStatus:%ld personalPhotographerSessionTimerState:%ld"
+ "\xf0Q"
- "supportedCaptureDevices:%@ captureDevice:%@ supportedCaptureModes:%@ captureMode:%@ capturing:%d captureStartDate:%@ capturingPaused:%d capturePauseDate:%@ orientation:%@ toggleCameraDeviceSupport:%d zoomSupport:%d zoomAmount:%f zoomMagnificationSupport:%d minimumZoomMagnification:%f maximumZoomMagnification:%f significantZoomMagnifications:%@ currentZoomMagnification:%f flashSupport:%@ flashMode:%@ hdrSupport:%@ hdrMode:%@ irisSupport:%@ irisMode:%@ sharedLibrarySupport:%@ sharedLibraryMode:%@ supportsMomentCapture:%d burstSupport:%d viewfinderSessionState:%lu shallowDepthOfFieldStatus:%@ stereoCaptureStatus:%@"
- "\xf0A"
```
