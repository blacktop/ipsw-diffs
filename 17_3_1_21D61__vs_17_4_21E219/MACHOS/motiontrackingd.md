## motiontrackingd

> `/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Support/motiontrackingd`

```diff

-452.0.6.0.0
-  __TEXT.__text: 0x21904
-  __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_stubs: 0x5fa0
-  __TEXT.__objc_methlist: 0x2454
-  __TEXT.__const: 0x288
+452.10.0.0.0
+  __TEXT.__text: 0x21d3c
+  __TEXT.__auth_stubs: 0x9a0
+  __TEXT.__objc_stubs: 0x5fc0
+  __TEXT.__objc_methlist: 0x246c
+  __TEXT.__const: 0x2bc
   __TEXT.__gcc_except_tab: 0x580
   __TEXT.__cstring: 0x175d
   __TEXT.__oslogstring: 0x1cbf
-  __TEXT.__objc_methname: 0x7c73
+  __TEXT.__objc_methname: 0x7c5f
   __TEXT.__objc_classname: 0x508
-  __TEXT.__objc_methtype: 0x181b
+  __TEXT.__objc_methtype: 0x184a
   __TEXT.__dlopen_cstrs: 0x21b
-  __TEXT.__unwind_info: 0x988
-  __DATA_CONST.__auth_got: 0x4c8
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x878
+  __TEXT.__unwind_info: 0x9a0
+  __DATA_CONST.__auth_got: 0x4e0
+  __DATA_CONST.__got: 0x1c8
+  __DATA_CONST.__const: 0x898
   __DATA_CONST.__cfstring: 0x740
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x290
+  __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_intobj: 0x90
   __DATA.__objc_const: 0x4e78
-  __DATA.__objc_selrefs: 0x1b20
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x290
-  __DATA.__objc_superrefs: 0xe0
+  __DATA.__objc_selrefs: 0x1b30
   __DATA.__objc_ivar: 0x368
   __DATA.__objc_data: 0x8c0
   __DATA.__data: 0x6d0
-  __DATA.__bss: 0x248
+  __DATA.__bss: 0x258
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 28B083B6-1AA1-3838-8CB3-681F2EC7E23B
-  Functions: 1102
-  Symbols:   283
-  CStrings:  1938
+  UUID: C20CB45E-4BF4-3F2C-8311-17CA5F362587
+  Functions: 1107
+  Symbols:   287
+  CStrings:  1943
 
Symbols:
+ _AXSSDeviceFrontCameraPhysicallyMountedUpsideDown
+ ___sincosf_stret
+ _atan2f
+ _matrix_identity_float4x4
CStrings:
+ "T@\"NSString\",?,R,C"
+ "T{?=[4]},N,V_pose"
+ "_calculatePoseWithRotation:translation:"
+ "_handleDetectedFaceAbsoluteModeWithFaceBounds:pose:"
+ "_handleDetectedFaceAccelerationModeWithFaceBounds:noseCenter:pose:poseTranslation:imageSize:"
+ "_handleDetectedFaceJoystickModeWithPose:poseTranslation:"
+ "_handleDetectedFaceWithProjectedPoint:pose:poseTranslation:"
+ "_mirrorPoseVertically:"
+ "_pose"
+ "_projectPoint:usingFaceInfoDict:pose:"
+ "pose"
+ "setPose:"
+ "{?=[4]}32@0:8@16@24"
+ "{?=[4]}80@0:8{?=[4]}16"
+ "{CGPoint=dd}104@0:816@32{?=[4]}40"
- "T{?=[4]},N,V_poseRotation"
- "_handleDetectedFaceAbsoluteModeWithFaceBounds:poseRotation:"
- "_handleDetectedFaceAccelerationModeWithFaceBounds:noseCenter:poseRotation:poseTranslation:imageSize:"
- "_handleDetectedFaceJoystickModeWithPoseRotation:poseTranslation:"
- "_handleDetectedFaceWithProjectedPoint:poseRotation:poseTranslation:"
- "_poseRotation"
- "_projectPoint:usingFaceInfoDict:poseRotationMatrixArray:poseTranslationArray:"
- "poseRotation"
- "setPoseRotation:"
- "{CGPoint=dd}56@0:816@32@40@48"

```
