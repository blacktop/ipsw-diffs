## replayd

> `/usr/libexec/replayd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`

```diff

-740.62.1.0.0
-  __TEXT.__text: 0xc530c
-  __TEXT.__auth_stubs: 0x1b10
-  __TEXT.__objc_stubs: 0xed00
-  __TEXT.__objc_methlist: 0x75ac
+765.15.2.5.1
+  __TEXT.__text: 0xcae38
+  __TEXT.__auth_stubs: 0x1d10
+  __TEXT.__objc_stubs: 0xf2e0
+  __TEXT.__objc_methlist: 0x78cc
   __TEXT.__const: 0x430
-  __TEXT.__oslogstring: 0x15545
-  __TEXT.__cstring: 0x17324
-  __TEXT.__objc_classname: 0xacb
-  __TEXT.__objc_methname: 0x1618d
-  __TEXT.__objc_methtype: 0x40dd
-  __TEXT.__gcc_except_tab: 0xfe4
+  __TEXT.__oslogstring: 0x16418
+  __TEXT.__cstring: 0x177e3
+  __TEXT.__objc_classname: 0xb35
+  __TEXT.__objc_methname: 0x1693a
+  __TEXT.__objc_methtype: 0x4234
+  __TEXT.__gcc_except_tab: 0x1004
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__info_plist: 0x49b
-  __TEXT.__unwind_info: 0x33e0
-  __DATA_CONST.__const: 0x2900
-  __DATA_CONST.__cfstring: 0x6380
-  __DATA_CONST.__objc_classlist: 0x2e0
+  __TEXT.__info_plist: 0x4a1
+  __TEXT.__unwind_info: 0x35a8
+  __DATA_CONST.__const: 0x29a0
+  __DATA_CONST.__cfstring: 0x6420
+  __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0xf0
+  __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x248
+  __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_intobj: 0x6d8
   __DATA_CONST.__objc_doubleobj: 0x50
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0xd98
-  __DATA_CONST.__got: 0xd08
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0x11180
-  __DATA.__objc_selrefs: 0x4668
-  __DATA.__objc_ivar: 0xde8
-  __DATA.__objc_data: 0x1cc0
-  __DATA.__data: 0xc98
-  __DATA.__bss: 0x290
+  __DATA_CONST.__auth_got: 0xe98
+  __DATA_CONST.__got: 0xd38
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA.__objc_const: 0x11cf8
+  __DATA.__objc_selrefs: 0x47f8
+  __DATA.__objc_ivar: 0xe84
+  __DATA.__objc_data: 0x1e00
+  __DATA.__data: 0xcf8
+  __DATA.__bss: 0x2a0
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CallKit.framework/Versions/A/CallKit
+  - /System/Library/Frameworks/ColorSync.framework/Versions/A/ColorSync
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3752
-  Symbols:   848
-  CStrings:  7410
+  Functions: 3871
+  Symbols:   884
+  CStrings:  7591
 
Symbols:
+ _CFMachPortCreateRunLoopSource
+ _CFMachPortCreateWithPort
+ _CFMachPortInvalidate
+ _CFRunLoopAddSource
+ _CFRunLoopGetMain
+ _CFRunLoopRemoveSource
+ _CFUUIDCreateString
+ _CGDisplayCreateUUIDFromDisplayID
+ _CGEventCopyIOHIDEvent
+ _CGEventGetIntegerValueField
+ _CGEventGetTimestamp
+ _CGEventTapCreate
+ _CGEventTapEnable
+ _CGRegionCreateEmptyRegion
+ _CGRegionCreateWithRect
+ _CGRegionRelease
+ _CGSCoalesceEventsInMask
+ _CGSNewConnection
+ _CGSOrderWindow
+ _CGSReleaseConnection
+ _CGSReleaseWindow
+ _CGSSetWindowLevel
+ _CGWindowLevelForKey
+ _IOHIDEventGetChildren
+ _IOHIDEventGetFloatValue
+ _IOHIDEventGetIntegerValue
+ _IOHIDEventSystemClientActivate
+ _IOHIDEventSystemClientCreateWithType
+ _IOHIDEventSystemClientSetDispatchQueue
+ _OBJC_CLASS_$_BKSTouchStream
+ _OBJC_CLASS_$_BKSTouchStreamPolicy
+ _OBJC_CLASS_$_STMediaStatusDomainMicrophoneDescriptor
+ _SLSNewWindowWithOpaqueShapeAndContext
+ __exit
+ _clock_gettime_nsec_np
+ _kCFRunLoopCommonModes
+ _objc_setProperty_atomic_copy
- _notify_register_check
CStrings:
+ " [DEBUG] %{public}s:%d SCTouchTracker: discarding contacts replayed at touch stream creation"
+ " [ERROR] %{public}s:%d Failed to create new function drawFilledCirclesBGRA"
+ " [ERROR] %{public}s:%d Failed to create new function drawFilledCirclesX420"
+ " [ERROR] %{public}s:%d RPConnectionManager: SIGTERM cleanup window elapsed, exiting cleanly"
+ " [ERROR] %{public}s:%d SCTouchTracker: BKSTouchStream init failed contextID=0x%x displayUUID=%@"
+ " [ERROR] %{public}s:%d SCTouchTracker: CFMachPortCreateRunLoopSource failed for display %u"
+ " [ERROR] %{public}s:%d SCTouchTracker: CFMachPortCreateRunLoopSource failed for touch stream"
+ " [ERROR] %{public}s:%d SCTouchTracker: CFMachPortCreateWithPort failed port=%p shouldFreeInfo=%d"
+ " [ERROR] %{public}s:%d SCTouchTracker: CGDisplayCreateUUIDFromDisplayID failed for display %u"
+ " [ERROR] %{public}s:%d SCTouchTracker: CGEventTapCreate failed for display %u"
+ " [ERROR] %{public}s:%d SCTouchTracker: CGSGetEventPort failed err=%d"
+ " [ERROR] %{public}s:%d SCTouchTracker: CGSNewConnection failed err=%d"
+ " [ERROR] %{public}s:%d SCTouchTracker: CGSOrderWindow failed err=%d"
+ " [ERROR] %{public}s:%d SCTouchTracker: SLSNewWindowWithOpaqueShapeAndContext failed err=%d"
+ " [ERROR] %{public}s:%d SCTouchTracker: contextWithCGSConnection failed"
+ " [ERROR] %{public}s:%d SCTouchTracker: event tap unavailable for display-bound-window capture on display %u"
+ " [ERROR] %{public}s:%d SCTouchTracker: failed to create anchor window regions"
+ " [ERROR] %{public}s:%d SCTouchTracker: touch stream unavailable for display capture on display %u; touch tracking not started"
+ " [ERROR] %{public}s:%d [SCTouchDrawing] IOHIDEventSystemClientCreateWithType FAILED"
+ " [ERROR] %{public}s:%d [SCTouchDrawing] event tap disabled by timeout; re-enabling"
+ " [ERROR] %{public}s:%d [SCTouchDrawing] event tap disabled by user input"
+ " [ERROR] %{public}s:%d failed to create SCPreviewSession for previewID=%@"
+ " [ERROR] %{public}s:%d failed to stop own session"
+ " [ERROR] %{public}s:%d invalid pid=%d"
+ " [ERROR] %{public}s:%d maximum preview count (%lu) reached for previewContent=%d"
+ " [ERROR] %{public}s:%d missing or malformed previewID in previewConfig (got %@)"
+ " [ERROR] %{public}s:%d no client found for %{public}@, nothing to stop"
+ " [ERROR] %{public}s:%d no preview found for previewID=%@ content=%d"
+ " [ERROR] %{public}s:%d pickerDidCancel rejected: caller lacks ScreenCaptureKit private entitlement"
+ " [ERROR] %{public}s:%d pickerDidDismiss rejected: caller lacks ScreenCaptureKit private entitlement"
+ " [ERROR] %{public}s:%d pickerDidEnd rejected: caller lacks ScreenCaptureKit private entitlement"
+ " [ERROR] %{public}s:%d pickerDidUpdate rejected: caller lacks ScreenCaptureKit private entitlement"
+ " [ERROR] %{public}s:%d previewID=%@ already exists for previewContent=%d"
+ " [ERROR] %{public}s:%d stopAllActiveClients rejected: unentitled caller pid %d claims to be Control Center"
+ " [ERROR] %{public}s:%d stopAllActiveClients: caller pid %d lacks system recording entitlement, scoping stop to its own sessions"
+ " [ERROR] %{public}s:%d unsupported previewContent=%d"
+ " [INFO] %{public}s:%d %p hasStarted=%d micDeviceUID=%@ micCaptureSessionCount=%ld"
+ " [INFO] %{public}s:%d SCTouchTracker: started event tap for display-bound-window capture on display %u"
+ " [INFO] %{public}s:%d SCTouchTracker: started touch stream for display %u"
+ " [INFO] %{public}s:%d SCTouchTracker: stopped"
+ " [INFO] %{public}s:%d SCTouchTracker: touchStream=%@ connectionID=%u windowID=%u contextID=0x%x displayUUID=%@"
+ " [INFO] %{public}s:%d Stopped recording due to display change, outputURL: %@ error: %@"
+ " [INFO] %{public}s:%d [SCTouchDrawing] client lacks SCK system recording entitlement; touch tracking disabled session=%p"
+ " [INFO] %{public}s:%d [SCTouchDrawing] not a display or display-bound-window capture; touch tracking not started"
+ " [INFO] %{public}s:%d didStart=%d pid=%d attributionSource=%ld micDeviceUID=%@"
+ " [INFO] %{public}s:%d skipping invalid pid=%@"
+ " [INFO] %{public}s:%d stop own session success"
+ "-[RPConnectionManager handleSIGTERMWithExitAfter:exitBlock:]"
+ "-[RPConnectionManager handleSIGTERMWithExitAfter:exitBlock:]_block_invoke"
+ "-[RPConnectionManager pickerDidCancel:forStream:]"
+ "-[RPConnectionManager pickerDidDismiss:forStream:isCancelled:]"
+ "-[RPConnectionManager pickerDidEnd:withFilter:forStream:]"
+ "-[RPConnectionManager pickerDidUpdate:withFilter:preservedFilter:forStream:completionHandler:]"
+ "-[RPConnectionManager stopAllActiveClients]"
+ "-[RPRecordingManager stopActiveSessionForClientWithBundleID:]"
+ "-[RPRecordingManager stopActiveSessionForClientWithBundleID:]_block_invoke"
+ "-[SCCaptureSession setupShowMouseClicksWithContentFilter:withStreamConfiguration:]"
+ "-[SCMediaAttributionManager postMicAttributionDidStart:attributedEntity:micDeviceUID:micCaptureSessionCount:]_block_invoke_2"
+ "-[SCMediaAttributionManager updateMicrophoneCaptureDidStart:withAuditToken:micDeviceUID:]"
+ "-[SCMediaAttributionManager updateMicrophoneCaptureDidStart:withPID:attributionSource:micDeviceUID:]"
+ "-[SCScreenActivityManager startInactivityTimerWithQueue:]_block_invoke"
+ "-[SCTouchStreamSystemBackend copyNextEvent]"
+ "-[SCTouchStreamSystemBackend startForDisplay:eventsPendingHandler:]"
+ "-[SCTouchStreamSystemBackend startForDisplay:eventsPendingHandler:]_block_invoke"
+ "-[SCTouchTracker handleTapEventOfType:event:]"
+ "-[SCTouchTracker startEventTap]"
+ "-[SCTouchTracker start]"
+ "-[SCTouchTracker stop]"
+ "@\"<SCTouchStreamBackend>\""
+ "@\"BKSTouchStream\""
+ "@\"CAContext\""
+ "@\"SCTouchTracker\""
+ "@\"SCTouchTrackerEventTapContext\""
+ "AB"
+ "AQ"
+ "B28@0:8I16@?20"
+ "B28@0:8I16@?<v@?>20"
+ "RPConnectionManager: stopAllActiveClients completed for the calling client only"
+ "RPConnectionManager: stopAllActiveClientsInternal"
+ "RPConnectionManager: stopAllActiveClientsInternal completed"
+ "RPEnableEdgeLightDev"
+ "SCTouchEvent"
+ "SCTouchStreamBackend"
+ "SCTouchStreamSystemBackend"
+ "SCTouchTracker"
+ "SCTouchTrackerEventTapContext"
+ "SCTouchTracker_SharedHIDSystemClient_block_invoke"
+ "T@\"NSUUID\",R,N,V_previewID"
+ "T@\"SCClipSession\",&,V_clipSession"
+ "T@\"SCTouchTracker\",W,V_tracker"
+ "T@?,C,V_eventsPendingHandler"
+ "TB,N,V_active"
+ "TouchEffectRenderCommand"
+ "Tq,N,V_identity"
+ "Tq,N,V_index"
+ "T{CGPoint=dd},N,V_globalPosition"
+ "^{__CFMachPort=}"
+ "^{__CFMachPort=}32@0:8^?16^v24"
+ "^{__CFRunLoopSource=}"
+ "^{__CGEvent=}16@0:8"
+ "^{__CGEvent=}28@0:8I16^{__CGEvent=}20"
+ "_active"
+ "_activeTouchStreamBackend"
+ "_activeTouches"
+ "_activeTouchesLock"
+ "_attachedWindowIDs"
+ "_attachedWindowIDsRefreshTime"
+ "_cameraPreviewSessions"
+ "_capturedWindowID"
+ "_computePipelineFilledBGRA"
+ "_computePipelineFilledX420"
+ "_connectionID"
+ "_context"
+ "_displayFrameOnCameraPreviewSessions:"
+ "_displayFrameOnScreenPreviewSessions:"
+ "_eventPort"
+ "_eventTap"
+ "_eventTapContext"
+ "_eventsPendingHandler"
+ "_globalPosition"
+ "_identity"
+ "_includedWindowIDs"
+ "_index"
+ "_isDisplayBoundWindow"
+ "_isRunning"
+ "_lifecycleLock"
+ "_micDeviceUID"
+ "_runLoopSource"
+ "_screenPreviewSessions"
+ "_screenStreamsLock"
+ "_stopAndRemoveAllPreviewSessions"
+ "_touchStream"
+ "_touchStreamAcceptEventsAfter"
+ "_touchStreamBackend"
+ "_touchStreamCancelled"
+ "_touchStreamLock"
+ "_touchStreamQueue"
+ "_touchTracker"
+ "_tracker"
+ "_transientTouches"
+ "applyActiveTouches:"
+ "clipSession"
+ "com.apple.replayd.SCTouchTracker.touchStream"
+ "com.screenCaptureKit.previewUpdateQueue.%@"
+ "contextId"
+ "copyNextEvent"
+ "createEventTapWithCallback:userInfo:"
+ "drawFilledCirclesBGRA"
+ "drawFilledCirclesX420"
+ "edgeLightDevOverrideActive"
+ "elapsedClipBufferingSeconds"
+ "eventsPendingHandler"
+ "getStreamWithStreamID:"
+ "getStreamsSnapshot"
+ "globalPosition"
+ "handleSIGTERM"
+ "handleSIGTERMWithExitAfter:exitBlock:"
+ "handleTapEventOfType:event:"
+ "handleTouchStreamEvents"
+ "identity"
+ "index"
+ "initWithContentFilter:"
+ "initWithContentFilter:touchStreamBackend:"
+ "initWithContextID:displayUUID:identifier:policy:"
+ "initWithMicrophoneDescriptor:activityAttribution:maximumHistoryAccessed:"
+ "initWithMicrophoneIdentifier:"
+ "initWithUUIDString:"
+ "isUsingTouchStream"
+ "isWindowInCapturedContent:"
+ "nextRenderTouches"
+ "postMicAttributionDidStart:attributedEntity:micDeviceUID:micCaptureSessionCount:"
+ "previewID"
+ "refreshAttachedWindowIDs"
+ "removeStreamWithStreamID:"
+ "setActive:"
+ "setClipSession:"
+ "setEventsPendingHandler:"
+ "setGlobalPosition:"
+ "setIdentity:"
+ "setIndex:"
+ "setStream:withStreamID:"
+ "setTracker:"
+ "setWithCapacity:"
+ "startEventTap"
+ "startForDisplay:eventsPendingHandler:"
+ "startTouchStream"
+ "stopActiveSessionForClientWithBundleID:"
+ "stopAllActiveClientsInternal"
+ "stopEventTap"
+ "stopTouchStream"
+ "tearDownAnchorWindow"
+ "tracker"
+ "updateMicrophoneCaptureDidStart:withAuditToken:micDeviceUID:"
+ "updateMicrophoneCaptureDidStart:withPID:attributionSource:micDeviceUID:"
+ "v24@?0@\"NSError\"8Q16"
+ "v32@0:8d16@?24"
+ "v32@0:8{CGPoint=dd}16"
+ "v40@0:8B16i20q24@32"
+ "v44@0:8B16@20@28q36"
+ "v60@0:8B16{?=[8I]}20@52"
+ "{CGPoint=\"x\"d\"y\"d}"
- " [ERROR] %{public}s:%d failed to start previewContent=%d alreadyStarted=%d"
- " [ERROR] %{public}s:%d failed to stop previewContent=%d alreadyStopped=%d"
- " [INFO] %{public}s:%d Stopped recording due to display change"
- " [INFO] %{public}s:%d didStart=%d pid=%d attributionSource=%ld"
- "-[SCMediaAttributionManager postMicAttributionDidStart:attributedEntity:micCaptureSessionCount:]_block_invoke_2"
- "-[SCMediaAttributionManager updateMicrophoneCaptureDidStart:withAuditToken:]"
- "-[SCMediaAttributionManager updateMicrophoneCaptureDidStart:withPID:attributionSource:]"
- "-[SCScreenActivityManager startInactivityTimerWithQueue:]_block_invoke_2"
- "@\"SCPreviewSession\""
- "RPConnectionManager: stopAllActiveClients completed"
- "RPDaemonRun_block_invoke"
- "_cameraPreviewSession"
- "_screenPreviewSession"
- "com.screenCaptureKit.previewUpdateQueue"
- "postMicAttributionDidStart:attributedEntity:micCaptureSessionCount:"
- "updateMicrophoneCaptureDidStart:withAuditToken:"
- "updateMicrophoneCaptureDidStart:withPID:attributionSource:"
- "v32@0:8B16i20q24"
- "v36@0:8B16@20q28"
- "valueForKey:"
```
