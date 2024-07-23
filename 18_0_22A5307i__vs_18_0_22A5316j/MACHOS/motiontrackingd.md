## motiontrackingd

> `/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Support/motiontrackingd`

```diff

-491.0.0.0.0
-  __TEXT.__text: 0x23844
-  __TEXT.__auth_stubs: 0x9a0
-  __TEXT.__objc_stubs: 0x66a0
-  __TEXT.__objc_methlist: 0x26b4
-  __TEXT.__const: 0x348
-  __TEXT.__gcc_except_tab: 0x838
-  __TEXT.__cstring: 0x19cd
-  __TEXT.__oslogstring: 0x1e4f
-  __TEXT.__objc_methname: 0x853a
+493.0.0.0.0
+  __TEXT.__text: 0x24df0
+  __TEXT.__auth_stubs: 0x9c0
+  __TEXT.__objc_stubs: 0x6b60
+  __TEXT.__objc_methlist: 0x283c
+  __TEXT.__const: 0x388
+  __TEXT.__gcc_except_tab: 0x8ac
+  __TEXT.__cstring: 0x1ac0
+  __TEXT.__oslogstring: 0x1f7b
+  __TEXT.__objc_methname: 0x8a97
   __TEXT.__objc_classname: 0x5b4
-  __TEXT.__objc_methtype: 0x1bd6
-  __TEXT.__dlopen_cstrs: 0x21b
+  __TEXT.__objc_methtype: 0x1d1f
+  __TEXT.__dlopen_cstrs: 0x285
   __TEXT.__info_plist: 0x61a
-  __TEXT.__unwind_info: 0xa20
-  __DATA_CONST.__auth_got: 0x4e0
+  __TEXT.__unwind_info: 0xa58
+  __DATA_CONST.__auth_got: 0x4f0
   __DATA_CONST.__got: 0x3c0
-  __DATA_CONST.__const: 0x8a8
+  __DATA_CONST.__const: 0x910
   __DATA_CONST.__cfstring: 0x7c0
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA.__objc_const: 0x53c0
-  __DATA.__objc_selrefs: 0x1d18
-  __DATA.__objc_ivar: 0x390
+  __DATA.__objc_const: 0x55a0
+  __DATA.__objc_selrefs: 0x1e48
+  __DATA.__objc_ivar: 0x3b0
   __DATA.__objc_data: 0x910
   __DATA.__data: 0x850
-  __DATA.__bss: 0x258
+  __DATA.__bss: 0x268
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1091
-  Symbols:   290
-  CStrings:  2016
+  Functions: 1130
+  Symbols:   292
+  CStrings:  2094
 
Symbols:
+ _NSStringFromRect
+ _objc_retain_x26
CStrings:
+ "!\x14\x12"
+ "#"
+ "%!s(MISSING): %!f(MISSING)"
+ "%!s(MISSING): error: %!@(MISSING)"
+ "%!s(MISSING): faceBounds is out of bounds! face bounds: %!@(MISSING), orientation: %!l(MISSING)d"
+ "%!s(MISSING): no face metadata found!"
+ "-[AXMTLookAtPointTrackerObserver lookAtPointTracker:trackedOnScreenPoint:error:]_block_invoke"
+ "-[AXMTVisionKitEyeTracker _detectCriticalErrorsForFace:]"
+ "-[AXMTVisionKitEyeTracker didUpdateFieldOfView:]"
+ "-[AXMTVisionKitEyeTracker recalibrateFace]"
+ "B40@0:8{?=ddd}16"
+ "B72@0:8{?=ddd}16{?=ddd}40d64"
+ "T@\"NSNumber\",&,N,V__baselinePitch"
+ "T@\"NSNumber\",&,N,V__baselineYaw"
+ "T@\"NSValue\",&,N,V__baselineFaceBounds"
+ "TQ,N,V__lastTimePoseRecorded"
+ "Tf,N,V_fieldOfView"
+ "T{?=ddd},N,V__currentAcceleration"
+ "T{?=ddd},N,V__lastAccelerationUpdate"
+ "__baselineFaceBounds"
+ "__baselinePitch"
+ "__baselineYaw"
+ "__currentAcceleration"
+ "__lastAccelerationUpdate"
+ "__lastTimePoseRecorded"
+ "_accelerationIsInvalid:"
+ "_accelerationsAreWithinThreshold:acceleration2:threshold:"
+ "_accelerometerDataUpdated:"
+ "_baselineFaceBounds"
+ "_baselinePitch"
+ "_baselineYaw"
+ "_calculateMaxBoundingAreaBoxForFOV:"
+ "_calculateMinBoundingAreaBoxForFOV:"
+ "_currentAcceleration"
+ "_detectCriticalErrorsForFace:"
+ "_detectNonCriticalErrorsForFace:"
+ "_fieldOfView"
+ "_lastAccelerationUpdate"
+ "_lastTimePoseRecorded"
+ "_minDistBetweenAngleA:angleB:"
+ "_notifyDelegateFaceLost"
+ "_signalTrackedUnboundedOnScreenPoint:boundPoint:error:"
+ "axmtUtilities_accelerometerDataUpdated:"
+ "bounding box: %!@(MISSING), yaw: %!f(MISSING), pitch: %!f(MISSING)"
+ "canPerformReactionEffects"
+ "d20@0:8f16"
+ "d32@0:8d16d24"
+ "didUpdateFieldOfView:"
+ "facePositionChangedSignificantly: %!@(MISSING), poseChangedSignificantly: %!@(MISSING)"
+ "fieldOfView"
+ "geometricDistortionCorrectedVideoFieldOfView"
+ "hasPitchAngle"
+ "hasYawAngle"
+ "isGeometricDistortionCorrectionEnabled"
+ "lookAtPointTracker:trackedOnScreenPoint:error:"
+ "pitchAngle"
+ "setFieldOfView:"
+ "setReactionEffectsEnabled:"
+ "set_baselineFaceBounds:"
+ "set_baselinePitch:"
+ "set_baselineYaw:"
+ "set_currentAcceleration:"
+ "set_lastAccelerationUpdate:"
+ "set_lastTimePoseRecorded:"
+ "using baseline bounding box: %!@(MISSING)"
+ "using baseline pitch: %!f(MISSING)"
+ "using baseline yaw: %!f(MISSING)"
+ "v24@0:8@\"CMAccelerometerData\"16"
+ "v28@0:8@\"AXMTVideoCapturer\"16f24"
+ "v28@0:8@16f24"
+ "v40@0:8{?=ddd}16"
+ "v44@0:8{CGPoint=dd}16B32@36"
+ "v48@0:8@\"<AXMTLookAtPointTracker>\"16{CGPoint=dd}24@\"NSError\"40"
+ "v48@0:8@\"AXMTVisionKitEyeTracker\"16{CGPoint=dd}24@\"NSError\"40"
+ "v48@0:8@16{CGPoint=dd}24@40"
+ "valueWithRect:"
+ "videoCapturer:didUpdateFieldOfView:"
+ "videoFieldOfView"
+ "visionKitEyeTracker:detectedGaze:withNonCriticalError:"
+ "yawAngle"
+ "{?=\"x\"d\"y\"d\"z\"d}"
+ "{?=ddd}16@0:8"
- "\x01"
- "\x11\x14\x12"
- "v40@0:8@\"AXMTVisionKitEyeTracker\"16{CGPoint=dd}24"
- "visionKitEyeTracker:detectedGaze:"

```
