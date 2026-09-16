## CoreMotion

> `/System/Library/Frameworks/CoreMotion.framework/CoreMotion`

```diff

-3185.0.6.0.3
-  __TEXT.__text: 0x3c4c24
-  __TEXT.__objc_methlist: 0xd854
-  __TEXT.__const: 0xcc90
+3186.0.12.0.0
+  __TEXT.__text: 0x3c6268
+  __TEXT.__objc_methlist: 0xd964
+  __TEXT.__const: 0xcd60
   __TEXT.__swift5_typeref: 0x257
   __TEXT.__swift5_reflstr: 0x2e
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__constg_swiftt: 0xb8
   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__swift5_capture: 0x40
-  __TEXT.__oslogstring: 0x2f686
-  __TEXT.__cstring: 0x47503
+  __TEXT.__oslogstring: 0x2f779
+  __TEXT.__cstring: 0x477f3
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x30
-  __TEXT.__gcc_except_tab: 0xd458
-  __TEXT.__unwind_info: 0xd040
+  __TEXT.__gcc_except_tab: 0xd4d0
+  __TEXT.__unwind_info: 0xd0e0
   __TEXT.__eh_frame: 0x178
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3d60
-  __DATA_CONST.__objc_classlist: 0x8d8
+  __DATA_CONST.__const: 0x3d68
+  __DATA_CONST.__objc_classlist: 0x8e0
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x56a0
+  __DATA_CONST.__objc_selrefs: 0x56f8
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x7c0
+  __DATA_CONST.__objc_superrefs: 0x7c8
   __DATA_CONST.__objc_arraydata: 0x240
-  __DATA_CONST.__got: 0x818
-  __AUTH_CONST.__const: 0x15810
-  __AUTH_CONST.__cfstring: 0x13c00
-  __AUTH_CONST.__objc_const: 0x1db18
+  __DATA_CONST.__got: 0x828
+  __AUTH_CONST.__const: 0x158b8
+  __AUTH_CONST.__cfstring: 0x13d20
+  __AUTH_CONST.__objc_const: 0x1dd88
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__auth_got: 0x14c0
-  __AUTH.__objc_data: 0x4290
+  __AUTH.__objc_data: 0x42e0
   __AUTH.__data: 0x220
-  __DATA.__objc_ivar: 0x1798
+  __DATA.__objc_ivar: 0x17bc
   __DATA.__data: 0xe18
   __DATA.__common: 0x128
   __DATA_DIRTY.__objc_ivar: 0x1c0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 12678
-  Symbols:   1811
-  CStrings:  11393
+  Functions: 12714
+  Symbols:   1815
+  CStrings:  11413
 
Symbols:
+ _CLCopyAuthorization
+ _OBJC_CLASS_$_CMVO2MaxClassificationThreshold
+ _OBJC_METACLASS_$_CMVO2MaxClassificationThreshold
+ _kTCCServiceMotionSensors
CStrings:
+ "#Spi, CLCopyAuthorization failed"
+ "%@,<biologicalSex %ld, ageLowerBound %ld, ageUpperBound %ld, thresholdType %ld, slope %f, intercept %f>"
+ "+[CMWakeGestureManager toPropertyC:]"
+ "-[CLLocationInternalClient_CoreMotion copyAuthorizationFromBundleID:toBundleID:]_block_invoke"
+ "Assertion failed: lambda2 != 0, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMOQuaternion.cpp, line 172,invalid weights."
+ "Assertion failed: t >= 0 && t <= 1, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMOQuaternion.cpp, line 320,Invalid time t for slerp."
+ "CL: CLCopyAuthorization"
+ "Invalid PropertyA input."
+ "ParameterK"
+ "PropertyA Ambiguous for PropertyB Ambiguous, ParameterD & ParameterE."
+ "TempestDefaultLidAngleDeg"
+ "TempestForceDefaultLidAngle"
+ "[Gesture %{public}ld] Gesture%{public}s notification: %{public}d(%{public}@), Mode:%{public}@, Start:%{public}@, End:%{public}@, HostAwake, %{public}d, Inferred:%{public}u, IsSuppressionActive:%{public}d"
+ "[RelDMService][parseLidAngleDeg] checkedLidAngleDeg: %{public}.1f deg"
+ "distanceCalibratedPedometer"
+ "float CMRelDMService::parseLidAngleDeg(const float) const"
+ "inHandDoubleTapBaseDetectorReset"
+ "isSuppressionActive"
+ "kCMVO2MaxClassificationThresholdCodingKeyAgeLowerBound"
+ "kCMVO2MaxClassificationThresholdCodingKeyAgeUpperBound"
+ "kCMVO2MaxClassificationThresholdCodingKeyBiologicalSex"
+ "kCMVO2MaxClassificationThresholdCodingKeyIntercept"
+ "kCMVO2MaxClassificationThresholdCodingKeySlope"
+ "kCMVO2MaxClassificationThresholdCodingKeyThresholdType"
+ "pencilState"
+ "{\"msg%{public}.0s\":\"CLCopyAuthorization\", \"event\":%{public, location:escape_only}s}"
- "Assertion failed: lambda2 != 0, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMOQuaternion.cpp, line 152,invalid weights."
- "Assertion failed: t >= 0 && t <= 1, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMOQuaternion.cpp, line 300,Invalid time t for slerp."
- "Invalid propertyA input."
- "PropertyA ambiguous for PropertyB Ambiguous, ParameterD & ParameterE."
- "[Gesture %{public}ld] Gesture%{public}s notification: %{public}d(%{public}@), Mode:%{public}@, Start:%{public}@, End:%{public}@, HostAwake, %{public}d, Inferred:%{public}u"
- "sharedManager_%@"
```
