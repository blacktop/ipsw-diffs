## nearbyd

> `/usr/libexec/nearbyd`

```diff

-458.0.1.0.0
-  __TEXT.__text: 0x42c7e4
-  __TEXT.__auth_stubs: 0x28f0
-  __TEXT.__objc_stubs: 0x10f20
+458.0.3.0.0
+  __TEXT.__text: 0x42dbac
+  __TEXT.__auth_stubs: 0x2900
+  __TEXT.__objc_stubs: 0x10f80
   __TEXT.__init_offsets: 0x5e8
-  __TEXT.__objc_methlist: 0x99dc
-  __TEXT.__gcc_except_tab: 0x46dbc
-  __TEXT.__const: 0x2d4db0
-  __TEXT.__cstring: 0x305b2
-  __TEXT.__objc_methname: 0x19c88
-  __TEXT.__oslogstring: 0x4c0cf
+  __TEXT.__objc_methlist: 0x9a0c
+  __TEXT.__gcc_except_tab: 0x46f9c
+  __TEXT.__const: 0x2d4de0
+  __TEXT.__cstring: 0x30862
+  __TEXT.__objc_methname: 0x19ed8
+  __TEXT.__oslogstring: 0x4c23f
   __TEXT.__objc_classname: 0x185b
-  __TEXT.__objc_methtype: 0x1b6b5
+  __TEXT.__objc_methtype: 0x1c185
   __TEXT.__swift5_typeref: 0x7d
   __TEXT.__swift5_capture: 0x20
   __TEXT.__constg_swiftt: 0x88

   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
   __TEXT.__info_plist: 0x3fc
-  __TEXT.__unwind_info: 0x17428
+  __TEXT.__unwind_info: 0x17430
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x1490
+  __DATA_CONST.__auth_got: 0x1498
   __DATA_CONST.__got: 0x970
   __DATA_CONST.__auth_ptr: 0x80
   __DATA_CONST.__const: 0x1f600
-  __DATA_CONST.__cfstring: 0x11520
+  __DATA_CONST.__cfstring: 0x117a0
   __DATA_CONST.__objc_classlist: 0x4a8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x258

   __DATA_CONST.__objc_arrayobj: 0x198
   __DATA_CONST.__objc_intobj: 0x510
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x17090
-  __DATA.__objc_selrefs: 0x4e20
-  __DATA.__objc_ivar: 0x1280
+  __DATA.__objc_const: 0x17310
+  __DATA.__objc_selrefs: 0x4e40
+  __DATA.__objc_ivar: 0x12d0
   __DATA.__objc_data: 0x2f48
   __DATA.__data: 0x302c
   __DATA.__bss: 0xc1c0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 18742
-  Symbols:   989
-  CStrings:  16439
+  Functions: 18747
+  Symbols:   990
+  CStrings:  16497
 
Symbols:
+ __ZNSt3__16__sortIRNS_6__lessIffEEPfEEvT0_S5_T_
CStrings:
+ "#ni-ca,DoT error, mean: %!f(MISSING), std: %!f(MISSING), median: %!f(MISSING), 95th: %!f(MISSING)"
+ "#ni-ca,delta dot errors mean: %!f(MISSING), std: %!f(MISSING), median: %!f(MISSING), 95th: %!f(MISSING), n: %!z(MISSING)u"
+ "#ni-ca,dot errors mean: %!f(MISSING), std: %!f(MISSING), median: %!f(MISSING), 95th: %!f(MISSING), n: %!z(MISSING)u"
+ "#ni-ca,odometry source ratio, VIO: %!f(MISSING), IO: %!f(MISSING), DeltaV: %!f(MISSING), None: %!f(MISSING)"
+ "#ni-ca,point errors mean: %!f(MISSING), std: %!f(MISSING), median: %!f(MISSING), 95th: %!f(MISSING), n: %!z(MISSING)u"
+ "#ni-ca,pose times, vio: %!f(MISSING), io: %!f(MISSING)"
+ "-[NIServerAnalyticsManager _calculateErrorStatsFromVector:]"
+ "/AppleInternal/Library/BuildRoots/0af4df6a-42a2-11ef-b9e2-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.0.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/0af4df6a-42a2-11ef-b9e2-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.0.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "IODirectionOfTravelErrorDegrees95th"
+ "IODirectionOfTravelErrorDegreesMean"
+ "IODirectionOfTravelErrorDegreesMedian"
+ "IODirectionOfTravelErrorDegreesN"
+ "IODirectionOfTravelErrorDegreesStd"
+ "IODirectionOfTravelErrorDeltaDegrees95th"
+ "IODirectionOfTravelErrorDeltaDegreesMean"
+ "IODirectionOfTravelErrorDeltaDegreesMedian"
+ "IODirectionOfTravelErrorDeltaDegreesN"
+ "IODirectionOfTravelErrorDeltaDegreesStd"
+ "OdometrySourceDeltaV"
+ "OdometrySourceIO"
+ "OdometrySourceNone"
+ "OdometrySourceVIO"
+ "PointToPointError95th"
+ "PointToPointErrorMean"
+ "PointToPointErrorMedian"
+ "PointToPointErrorN"
+ "PointToPointErrorStd"
+ "TimeToFirstIOPoseAfterFindButtonPressed"
+ "_angleErrorHistory"
+ "_calculateAndLogErrorsFromIODeltaP:vioDeltaP:vioPos:"
+ "_calculateErrorStatsFromVector:"
+ "_calculatePoseSplicingMetrics"
+ "_currentVIOOffsetPosition"
+ "_deltaAngleErrorHistory"
+ "_deltaVSourceTime"
+ "_integratedPDRVIOFrame"
+ "_ioSourceTime"
+ "_lastAngleError"
+ "_lastOdometryAvailabilityState"
+ "_lastSolutionHadDriftingVIO"
+ "_lastSolutionTime"
+ "_noOdometryAvailableTime"
+ "_pdrAligner"
+ "_pointToPointErrorHistory"
+ "_previousAdjustedRotatedVioPosition"
+ "_previousVioIsNotAvailable"
+ "_timeAtFirstIOPose"
+ "_timeOfLastPDRUpdate"
+ "_timeOfLastSplicedPoseErrorLogging"
+ "_updateAlignedPDRMetrics:"
+ "_vioAvailableTime"
+ "_vioPathLength"
+ "errorVector.size() > 0"
+ "v400@0:8{Solution={ConvergenceState=iBBBB}{optional<nearby::algorithms::common::RangeResult>=(?=c{RangeResult=Qdfi{optional<nearby::algorithms::common::AngleMeasurement>=(?=c{AngleMeasurement=ffi})B}d{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}ii{optional<nearby::algorithms::common::MagneticFieldStrengthCheckParameter>=(?=c{MagneticFieldStrengthCheckParameter=idd})B}{optional<double>=(?=cd)B}{optional<unsigned short>=(?=cS)B}{optional<unsigned char>=(?=cC)B}{optional<unsigned char>=(?=cC)B}})B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}i{optional<double>=(?=cd)B}{optional<float __attribute__((ext_vector_type(3)))>=(?=c)B}{optional<float __attribute__((ext_vector_type(3)))>=(?=c)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}{optional<bool>=(?=cB)B}{optional<nearby::algorithms::common::OdometryAvailabilityState>=(?=ci)B}{optional<nearby::algorithms::common::AlgorithmSource>=(?=ci)B}{optional<nearby::algorithms::common::PeerMotionState>=(?=ci)B}BB}16"
+ "v40@0:8r^16r^24r^32"
+ "{FinderInertialOdometryProcessor=\"_bodyToSplicedFrame\"{?=\"vector\"}\"_pdrWorldFrameToSplicedFrame\"{?=\"vector\"}\"_vioWorldFrameToSplicedFrame\"{?=\"vector\"}\"_poseHistory\"{deque<nearby::algorithms::common::Pose, std::allocator<nearby::algorithms::common::Pose>>=\"__map_\"{__split_buffer<nearby::algorithms::common::Pose *, std::allocator<nearby::algorithms::common::Pose *>>=\"__first_\"^^{Pose}\"__begin_\"^^{Pose}\"__end_\"^^{Pose}\"__end_cap_\"{__compressed_pair<nearby::algorithms::common::Pose **, std::allocator<nearby::algorithms::common::Pose *>>=\"__value_\"^^{Pose}}}\"__start_\"Q\"__size_\"{__compressed_pair<unsigned long, std::allocator<nearby::algorithms::common::Pose>>=\"__value_\"Q}}\"_rotatedVioPoseHistory\"{deque<nearby::algorithms::common::Pose, std::allocator<nearby::algorithms::common::Pose>>=\"__map_\"{__split_buffer<nearby::algorithms::common::Pose *, std::allocator<nearby::algorithms::common::Pose *>>=\"__first_\"^^{Pose}\"__begin_\"^^{Pose}\"__end_\"^^{Pose}\"__end_cap_\"{__compressed_pair<nearby::algorithms::common::Pose **, std::allocator<nearby::algorithms::common::Pose *>>=\"__value_\"^^{Pose}}}\"__start_\"Q\"__size_\"{__compressed_pair<unsigned long, std::allocator<nearby::algorithms::common::Pose>>=\"__value_\"Q}}\"pdrToVioRotation\"{optional<simd_quatf>=\"\"(?=\"__null_state_\"c\"__val_\"{?=\"vector\"})\"__engaged_\"B}\"_lastVIOTrackingState\"i\"lastPDRAvailable\"B\"_lastPDRInput\"{optional<nearby::algorithms::finding::PDRInput>=\"\"(?=\"__null_state_\"c\"__val_\"{PDRInput=\"machAbsoluteTime\"d\"machContinuousTime\"{optional<double>=\"\"(?=\"__null_state_\"c\"__val_\"d)\"__engaged_\"B}\"deltaPosX\"{optional<double>=\"\"(?=\"__null_state_\"c\"__val_\"d)\"__engaged_\"B}\"deltaPosY\"{optional<double>=\"\"(?=\"__null_state_\"c\"__val_\"d)\"__engaged_\"B}\"deltaPosZ\"{optional<double>=\"\"(?=\"__null_state_\"c\"__val_\"d)\"__engaged_\"B}\"deltaVx\"{optional<double>=\"\"(?=\"__null_state_\"c\"__val_\"d)\"__engaged_\"B}\"deltaVy\"{optional<double>=\"\"(?=\"__null_state_\"c\"__val_\"d)\"__engaged_\"B}\"deltaVz\"{optional<double>=\"\"(?=\"__null_state_\"c\"__val_\"d)\"__engaged_\"B}\"quaternion\"{optional<nearby::algorithms::finding::QuaternionInput>=\"\"(?=\"__null_state_\"c\"__val_\"{QuaternionInput=\"_quatW\"d\"_quatX\"d\"_quatY\"d\"_quatZ\"d})\"__engaged_\"B}})\"__engaged_\"B}\"_availabilityState\"i\"kInterpolationStalenessThresholdSeconds\"d}"
+ "{VectorAggregateErrors=ddddQ}40@0:8{vector<float, std::allocator<float>>=^f^f{__compressed_pair<float *, std::allocator<float>>=^f}}16"
+ "{optional<float __attribute__((ext_vector_type(3)))>=\"\"(?=\"__null_state_\"c\"__val_\")\"__engaged_\"B}"
+ "{optional<float>=\"\"(?=\"__null_state_\"c\"__val_\"f)\"__engaged_\"B}"
+ "{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__end_cap_\"{__compressed_pair<float *, std::allocator<float>>=\"__value_\"^f}}"
- "/AppleInternal/Library/BuildRoots/42c968eb-3952-11ef-b3d0-4a8302371c27/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.0.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/42c968eb-3952-11ef-b3d0-4a8302371c27/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.0.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "v400@0:8{Solution={ConvergenceState=iBBBB}{optional<nearby::algorithms::common::RangeResult>=(?=c{RangeResult=Qdfi{optional<nearby::algorithms::common::AngleMeasurement>=(?=c{AngleMeasurement=ffi})B}d{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}ii{optional<nearby::algorithms::common::MagneticFieldStrengthCheckParameter>=(?=c{MagneticFieldStrengthCheckParameter=idd})B}{optional<double>=(?=cd)B}{optional<unsigned short>=(?=cS)B}{optional<unsigned char>=(?=cC)B}{optional<unsigned char>=(?=cC)B}})B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}i{optional<double>=(?=cd)B}{optional<float __attribute__((ext_vector_type(3)))>=(?=c)B}{optional<float __attribute__((ext_vector_type(3)))>=(?=c)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}{optional<bool>=(?=cB)B}{optional<nearby::algorithms::common::AlgorithmSource>=(?=ci)B}{optional<nearby::algorithms::common::PeerMotionState>=(?=ci)B}BB}16"

```
