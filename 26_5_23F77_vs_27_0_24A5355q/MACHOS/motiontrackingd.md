## motiontrackingd

> `/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Support/motiontrackingd`

```diff

-545.18.0.0.0
-  __TEXT.__text: 0x2a0e4
-  __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_stubs: 0x6f40
-  __TEXT.__objc_methlist: 0x30dc
-  __TEXT.__const: 0x3b8
-  __TEXT.__gcc_except_tab: 0xa00
-  __TEXT.__cstring: 0x214b
-  __TEXT.__oslogstring: 0x219c
-  __TEXT.__objc_methname: 0x931e
-  __TEXT.__objc_classname: 0x5e5
-  __TEXT.__objc_methtype: 0x1ec4
+576.1.0.0.0
+  __TEXT.__text: 0x29834
+  __TEXT.__auth_stubs: 0x9f0
+  __TEXT.__objc_stubs: 0x6ec0
+  __TEXT.__objc_methlist: 0x2ebc
+  __TEXT.__const: 0x30c
   __TEXT.__dlopen_cstrs: 0x2ef
-  __TEXT.__unwind_info: 0xdf0
-  __DATA_CONST.__auth_got: 0x4d0
-  __DATA_CONST.__got: 0x3f8
-  __DATA_CONST.__const: 0x9f0
-  __DATA_CONST.__cfstring: 0x840
-  __DATA_CONST.__objc_classlist: 0xf8
+  __TEXT.__gcc_except_tab: 0xa68
+  __TEXT.__cstring: 0x217a
+  __TEXT.__oslogstring: 0x21b9
+  __TEXT.__objc_methname: 0x9244
+  __TEXT.__objc_classname: 0x549
+  __TEXT.__objc_methtype: 0x1dd0
+  __TEXT.__unwind_info: 0x9c8
+  __DATA_CONST.__const: 0x978
+  __DATA_CONST.__cfstring: 0x800
+  __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xb0
+  __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xf8
+  __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA.__objc_const: 0x4e28
-  __DATA.__objc_selrefs: 0x2080
-  __DATA.__objc_ivar: 0x3f0
-  __DATA.__objc_data: 0x9b0
-  __DATA.__data: 0x850
+  __DATA_CONST.__auth_got: 0x508
+  __DATA_CONST.__got: 0x3f0
+  __DATA.__objc_const: 0x4aa0
+  __DATA.__objc_selrefs: 0x2050
+  __DATA.__objc_ivar: 0x3cc
+  __DATA.__objc_data: 0x910
+  __DATA.__data: 0x7f0
   __DATA.__bss: 0x370
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F8C3FE89-6284-3AB3-A9AF-CA6FF292EB44
-  Functions: 1245
-  Symbols:   295
-  CStrings:  2264
+  UUID: 4E14D4B5-B4C8-39A7-80EB-349A1C5D9677
+  Functions: 1037
+  Symbols:   299
+  CStrings:  2242
 
Symbols:
+ __os_signpost_emit_with_name_impl
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_retain_x9
+ _os_signpost_enabled
- _OBJC_CLASS_$_UIScreen
- _OBJC_CLASS_$__UIRootWindow
- _OBJC_METACLASS_$__UIRootWindow
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "AXMTCameraBasedLookAtPointTracker: Face gestures needed, creating FaceKit tracker for expression detection alongside eye tracking"
+ "AXMTCameraBasedLookAtPointTracker: Face gestures no longer needed, tearing down FaceKit tracker"
+ "AXMTCameraBasedLookAtPointTracker: Face gestures now needed, creating FaceKit tracker"
+ "Failed to register check for effective device orientation: %u"
+ "Failed to register check for orientation lock status: %u"
+ "GAZE_DIAG | frame_t: %.3f | raw_cm: (%.3f, %.3f) | norm: (%.4f, %.4f) | screen_pt: (%.1f, %.1f) | bbox: (%.3f, %.3f, %.3f, %.3f) | yaw: %.1f | pitch: %.1f | err: %ld"
+ "TB,N,V_faceTrackingEnabled"
+ "TQ,N,V__lastTimeGazeDiagnosticRecorded"
+ "VNDetectScreenGazeRequest"
+ "__lastTimeGazeDiagnosticRecorded"
+ "_faceTrackingEnabled"
+ "_lastTimeGazeDiagnosticRecorded"
+ "faceGesturesNeeded"
+ "faceTrackingEnabled"
+ "setFaceTrackingEnabled:"
+ "set_lastTimeGazeDiagnosticRecorded:"
- "@\"AXMTARKitCameraInputSource\""
- "@\"_AXMTARKitInvisibleWindow\""
- "AXMTARKitBasedLookAtPointTracker"
- "AXMTARKitBasedLookAtPointTracker: setDebugOverlayEnabled: %@"
- "AXMTARKitBasedLookAtPointTracker: startTracking: called"
- "AXMTARKitBasedLookAtPointTracker: startTracking: started running ARKitCameraInputSource"
- "AXMTARKitBasedLookAtPointTracker: stopTracking"
- "AXMTARKitCameraInputSourceDelegate"
- "T@\"AXMTARKitCameraInputSource\",&,N,V__arkitCameraInputSource"
- "T@\"_AXMTARKitInvisibleWindow\",&,N,V__arkitCameraInputSourceWindow"
- "_AXMTARKitInvisibleWindow"
- "__arkitCameraInputSource"
- "__arkitCameraInputSourceWindow"
- "_arkitCameraInputSource"
- "_arkitCameraInputSourceWindow"
- "_isSecure"
- "_updateWindowForDebugOverlay"
- "arKitCameraInputSource: didFailToTrackFaceWithError: %@"
- "arKitCameraInputSource: didReceiveExpressionStart: called for expression: %@"
- "arKitCameraInputSource: didReceivePoint: point is (%f, %f)"
- "arKitCameraInputSource:didReceiveExpressionEnd: called for expression: %@"
- "arKitCameraInputSourceInterruptionEnded"
- "arKitCameraInputSourceWasInterrupted"
- "arKitCameraInputSourceWasInterrupted:"
- "false"
- "initWithScreen:"
- "isEqualToMotionTrackingExpressionConfiguration:"
- "mainScreen"
- "makeKeyAndVisible"
- "set_arkitCameraInputSource:"
- "set_arkitCameraInputSourceWindow:"
- "true"
- "v24@0:8@\"AXMTARKitCameraInputSource\"16"
- "v32@0:8@\"AXMTARKitCameraInputSource\"16@\"NSError\"24"
- "v32@0:8@\"AXMTARKitCameraInputSource\"16Q24"
- "v40@0:8@\"AXMTARKitCameraInputSource\"16{CGPoint=dd}24"

```
