## motiontrackingd

> `/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Support/motiontrackingd`

```diff

-502.7.8.0.0
-  __TEXT.__text: 0x27910
+534.1.0.0.0
+  __TEXT.__text: 0x281dc
   __TEXT.__auth_stubs: 0x9d0
-  __TEXT.__objc_stubs: 0x6de0
-  __TEXT.__objc_methlist: 0x302c
-  __TEXT.__const: 0x3a8
-  __TEXT.__gcc_except_tab: 0xa18
-  __TEXT.__cstring: 0x20a1
-  __TEXT.__oslogstring: 0x2130
-  __TEXT.__objc_methname: 0x8fc2
+  __TEXT.__objc_stubs: 0x6ec0
+  __TEXT.__objc_methlist: 0x3084
+  __TEXT.__const: 0x3bc
+  __TEXT.__gcc_except_tab: 0xa48
+  __TEXT.__cstring: 0x2119
+  __TEXT.__oslogstring: 0x21b9
+  __TEXT.__objc_methname: 0x91a2
   __TEXT.__objc_classname: 0x5e5
-  __TEXT.__objc_methtype: 0x1ec0
-  __TEXT.__dlopen_cstrs: 0x285
-  __TEXT.__unwind_info: 0xb08
+  __TEXT.__objc_methtype: 0x1eb5
+  __TEXT.__dlopen_cstrs: 0x2ef
+  __TEXT.__unwind_info: 0xb38
   __DATA_CONST.__auth_got: 0x4f8
-  __DATA_CONST.__got: 0x3e0
-  __DATA_CONST.__const: 0x978
+  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__const: 0x9f0
   __DATA_CONST.__cfstring: 0x840
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA.__objc_const: 0x4d18
-  __DATA.__objc_selrefs: 0x2010
-  __DATA.__objc_ivar: 0x3d8
+  __DATA.__objc_const: 0x4d78
+  __DATA.__objc_selrefs: 0x2048
+  __DATA.__objc_ivar: 0x3e0
   __DATA.__objc_data: 0x9b0
   __DATA.__data: 0x850
-  __DATA.__bss: 0x320
+  __DATA.__bss: 0x370
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A1D48B46-FE22-3AEC-A6B3-D92EB026A03F
-  Functions: 1204
-  Symbols:   297
-  CStrings:  2234
+  UUID: 40D28D9B-7442-3690-8834-AB971F8C5A31
+  Functions: 1220
+  Symbols:   300
+  CStrings:  2250
 
Symbols:
+ _AXSSDeviceFrontCameraSensorRotation
+ _AXSSMotionTrackingDeviceOrientationOverrideDistributedNotificationName
+ _AXSSMotionTrackingDeviceOrientationOverridePreferenceKey
+ _OBJC_CLASS_$_NSDistributedNotificationCenter
- _AXSSDeviceFrontCameraPhysicallyMountedUpsideDown
CStrings:
+ "%s: cannot adjust pose, cameraSensorRotation %d is unsupported"
+ "%s: overriding device orientation to: %ld"
+ "-[AXMTFaceKitResult _rotatePose:forCameraSensorRotation:]"
+ "-[AXMTUtilities _updateForDeviceOrientationOverride:]"
+ "FaceID stole the camera for: %f"
+ "TB,N,V_ignoreAccelerometerUpdatesForAutomation"
+ "TQ,N,V__lastTimeFaceIDStoleCamera"
+ "__lastTimeFaceIDStoleCamera"
+ "_iOSReferenceFocalLengthFor3DPointProjection"
+ "_iOSReferencePrincipalPointFor3DPointProjection"
+ "_ignoreAccelerometerUpdatesForAutomation"
+ "_interfaceOrientedScreenPointForNormalizedDeviceOrientedPoint:"
+ "_lastTimeFaceIDStoleCamera"
+ "_projectZAxisVectorUsingRGBCameraDictionary:pose:useReferenceIntrinsics:"
+ "_rotatePose:forCameraSensorRotation:"
+ "_updateForDeviceOrientationOverride:"
+ "ignoreAccelerometerUpdatesForAutomation"
+ "setIgnoreAccelerometerUpdatesForAutomation:"
+ "set_lastTimeFaceIDStoleCamera:"
+ "targetIntrinsics"
+ "{?=[4]}84@0:8{?=[4]}16i80"
+ "{CGPoint=dd}92@0:8@16{?=[4]}24B88"
- "Adjusted"
- "_mirrorPoseVertically:"
- "_projectPoint:usingRGBCameraDictionary:pose:referenceDimensions:"
- "_screenCoordsForNormPoint:"
- "{?=[4]}80@0:8{?=[4]}16"
- "{CGPoint=dd}120@0:816@32{?=[4]}40{CGSize=dd}104"

```
