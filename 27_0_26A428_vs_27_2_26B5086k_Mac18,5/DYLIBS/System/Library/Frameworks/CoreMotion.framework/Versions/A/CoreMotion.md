## CoreMotion

> `/System/Library/Frameworks/CoreMotion.framework/Versions/A/CoreMotion`

```diff

-3185.0.6.0.0
-  __TEXT.__text: 0x31e2e8
-  __TEXT.__objc_methlist: 0x9e54
-  __TEXT.__const: 0xa698
+3186.0.12.0.0
+  __TEXT.__text: 0x3206e8
+  __TEXT.__objc_methlist: 0x9f74
+  __TEXT.__const: 0xa738
   __TEXT.__swift5_typeref: 0x257
   __TEXT.__swift5_reflstr: 0x2e
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__constg_swiftt: 0xb8
   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__swift5_capture: 0x40
-  __TEXT.__oslogstring: 0x24186
-  __TEXT.__cstring: 0x3945f
+  __TEXT.__oslogstring: 0x24259
+  __TEXT.__cstring: 0x3971f
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x30
-  __TEXT.__gcc_except_tab: 0xa5bc
-  __TEXT.__unwind_info: 0xaa10
+  __TEXT.__gcc_except_tab: 0xa634
+  __TEXT.__unwind_info: 0xaad0
   __TEXT.__eh_frame: 0x150
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1ca8
-  __DATA_CONST.__objc_classlist: 0x6b8
+  __DATA_CONST.__objc_classlist: 0x6c0
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x4248
+  __DATA_CONST.__objc_selrefs: 0x42a0
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x5c8
+  __DATA_CONST.__objc_superrefs: 0x5d0
   __DATA_CONST.__objc_arraydata: 0xe0
-  __DATA_CONST.__got: 0x680
-  __AUTH_CONST.__const: 0x13e10
-  __AUTH_CONST.__cfstring: 0xf7c0
-  __AUTH_CONST.__objc_const: 0x15d20
+  __DATA_CONST.__got: 0x688
+  __AUTH_CONST.__const: 0x13ed8
+  __AUTH_CONST.__cfstring: 0xf8e0
+  __AUTH_CONST.__objc_const: 0x15f90
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x1270
-  __AUTH.__objc_data: 0x2fd0
+  __AUTH_CONST.__auth_got: 0x1268
+  __AUTH.__objc_data: 0x3020
   __AUTH.__data: 0x210
-  __DATA.__objc_ivar: 0x111c
+  __DATA.__objc_ivar: 0x1140
   __DATA.__data: 0xaf0
   __DATA.__common: 0xc0
   __DATA_DIRTY.__objc_ivar: 0x18c

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 10478
-  Symbols:   1593
-  CStrings:  9530
+  Functions: 10523
+  Symbols:   1595
+  CStrings:  9549
 
Symbols:
+ _CLCopyAuthorization
+ _OBJC_CLASS_$_CMVO2MaxClassificationThreshold
+ _OBJC_METACLASS_$_CMVO2MaxClassificationThreshold
- _IOHIDEventCreateVendorDefinedEvent
CStrings:
+ "#Spi, CLCopyAuthorization failed"
+ "%0"
+ "%@,<biologicalSex %ld, ageLowerBound %ld, ageUpperBound %ld, thresholdType %ld, slope %f, intercept %f>"
+ "-[CLLocationInternalClient_CoreMotion copyAuthorizationFromBundleID:toBundleID:]_block_invoke"
+ "Assertion failed: lambda2 != 0, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMOQuaternion.cpp, line 172,invalid weights."
+ "Assertion failed: t >= 0 && t <= 1, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMOQuaternion.cpp, line 320,Invalid time t for slerp."
+ "CL: CLCopyAuthorization"
+ "TempestDefaultLidAngleDeg"
+ "TempestForceDefaultLidAngle"
+ "[RelDMService][parseLidAngleDeg] checkedLidAngleDeg: %{public}.1f deg"
+ "distanceCalibratedPedometer"
+ "float CMRelDMService::parseLidAngleDeg(const float) const"
+ "inHandDoubleTapBaseDetectorReset"
+ "kCMVO2MaxClassificationThresholdCodingKeyAgeLowerBound"
+ "kCMVO2MaxClassificationThresholdCodingKeyAgeUpperBound"
+ "kCMVO2MaxClassificationThresholdCodingKeyBiologicalSex"
+ "kCMVO2MaxClassificationThresholdCodingKeyIntercept"
+ "kCMVO2MaxClassificationThresholdCodingKeySlope"
+ "kCMVO2MaxClassificationThresholdCodingKeyThresholdType"
+ "pencilState"
+ "{\"msg%{public}.0s\":\"CLCopyAuthorization\", \"event\":%{public, location:escape_only}s}"
- "Assertion failed: lambda2 != 0, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMOQuaternion.cpp, line 152,invalid weights."
- "Assertion failed: t >= 0 && t <= 1, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMOQuaternion.cpp, line 300,Invalid time t for slerp."
```
