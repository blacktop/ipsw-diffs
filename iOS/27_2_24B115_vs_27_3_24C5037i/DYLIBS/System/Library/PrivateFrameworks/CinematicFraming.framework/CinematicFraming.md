## CinematicFraming

> `/System/Library/PrivateFrameworks/CinematicFraming.framework/CinematicFraming`

```diff

-764.42.8.0.0
-  __TEXT.__text: 0x22de4
-  __TEXT.__objc_methlist: 0x247c
+764.60.7.0.2
+  __TEXT.__text: 0x232e4
+  __TEXT.__objc_methlist: 0x24fc
   __TEXT.__const: 0x690
-  __TEXT.__gcc_except_tab: 0xca8
-  __TEXT.__cstring: 0x1dff
+  __TEXT.__gcc_except_tab: 0xcb4
+  __TEXT.__cstring: 0x1eb9
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0xa70
+  __TEXT.__unwind_info: 0xa80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16a8
+  __DATA_CONST.__objc_selrefs: 0x16e8
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0xf0
   __DATA_CONST.__got: 0x1f8
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x1680
-  __AUTH_CONST.__objc_const: 0x4ea0
+  __AUTH_CONST.__cfstring: 0x1720
+  __AUTH_CONST.__objc_const: 0x4fb0
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x580
+  __DATA.__objc_ivar: 0x598
   __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__data: 0x3a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 845
-  Symbols:   1618
-  CStrings:  306
+  Functions: 856
+  Symbols:   1635
+  CStrings:  311
 
Symbols:
+ -[CinematicFramingSessionInputMetadata setStabilizationRotation:]
+ -[CinematicFramingSessionInputMetadata stabilizationRotation]
+ -[DeskCamRenderingSession realtimeStabilizationEnabled]
+ -[DeskCamRenderingSession registerVideoStabilizationOutputRotationVector:]
+ -[DeskCamRenderingSession setRealtimeStabilizationEnabled:]
+ -[DeskCamSession realtimeStabilizationEnabled]
+ -[DeskCamSession setRealtimeStabilizationEnabled:]
+ -[DeskCamSessionInputMetadata initWithDetectedObjectsInfo:cameraCalibrationData:cameraOrientation:timestamp:aspectRatio:sensorID:gravity:videoStabilizationOutputRotationVector:]
+ -[DeskCamSessionInputMetadata videoStabilizationOutputRotationVector]
+ -[VCProcessor applyStabilizationRotation]
+ -[VCProcessor setApplyStabilizationRotation:]
+ _FigGetCFPreferenceNumberWithDefault
+ _OBJC_IVAR_$_CinematicFramingSessionInputMetadata._stabilizationRotation
+ _OBJC_IVAR_$_DeskCamRenderingSession._maxVISAngleDeg
+ _OBJC_IVAR_$_DeskCamRenderingSession._realtimeStabilizationEnabled
+ _OBJC_IVAR_$_DeskCamRenderingSession._visTransformMatrix
+ _OBJC_IVAR_$_DeskCamSessionInputMetadata._videoStabilizationOutputRotationVector
+ _OBJC_IVAR_$_VCProcessor._applyStabilizationRotation
+ _quaternionFromRotationVector
- -[DeskCamSessionInputMetadata initWithDetectedObjectsInfo:cameraCalibrationData:cameraOrientation:timestamp:aspectRatio:sensorID:gravity:]
- GCC_except_table14
CStrings:
+ "applyStabilizationRotationToCinematicFraming"
+ "com.apple.coremedia"
+ "videoStabilizationOutputRotationVectorX"
+ "videoStabilizationOutputRotationVectorY"
+ "videoStabilizationOutputRotationVectorZ"
```
