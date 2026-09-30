## MotionSensorLogging

> `/System/Library/PrivateFrameworks/MotionSensorLogging.framework/MotionSensorLogging`

```diff

-3072.0.42.0.0
-  __TEXT.__text: 0x24b3b8
-  __TEXT.__auth_stubs: 0xa60
+3072.0.44.0.2
+  __TEXT.__text: 0x247318
+  __TEXT.__auth_stubs: 0xa50
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0x4523
-  __TEXT.__gcc_except_tab: 0x3b98
+  __TEXT.__gcc_except_tab: 0x3b90
   __TEXT.__oslogstring: 0x450
-  __TEXT.__cstring: 0x12856
-  __TEXT.__unwind_info: 0x63f0
+  __TEXT.__cstring: 0x1115a
+  __TEXT.__unwind_info: 0x63e0
   __TEXT.__eh_frame: 0x590
   __TEXT.__objc_classname: 0x10
   __TEXT.__objc_methname: 0x2cc

   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xf0
-  __AUTH_CONST.__auth_got: 0x540
+  __AUTH_CONST.__auth_got: 0x538
   __AUTH_CONST.__const: 0xa9c0
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x90

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 8FD3ECF7-F547-36C8-BD0D-0D1605147DC7
+  UUID: CEEB3E0D-059B-35D7-BB47-1111EA9B695A
   Functions: 9879
-  Symbols:   11239
-  CStrings:  3623
+  Symbols:   11238
+  CStrings:  3606
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ sub_266d057d0 -> sub_26450b7d0 : 4648 -> 4420
~ __ZN5CMMsl14ARKitWorldPose8readFromERN2PB6ReaderE : 1400 -> 1328
~ __ZN5CMMsl17AccelBiasEstimate8readFromERN2PB6ReaderE : 1776 -> 1652
~ __ZN5CMMsl13AccelTNBFrame8readFromERN2PB6ReaderE : 2120 -> 1944
~ __ZN5CMMsl19AccessoryBatchedPPG8readFromERN2PB6ReaderE : 2084 -> 2044
~ __ZN5CMMsl27AccessoryDeviceMotionConfig8readFromERN2PB6ReaderE : 1156 -> 1092
~ __ZN5CMMsl12AccessoryPPG8readFromERN2PB6ReaderE : 7364 -> 6900
~ __ZN5CMMsl23AccessoryProxSensorDrop8readFromERN2PB6ReaderE : 2876 -> 2728
~ __ZN5CMMsl13AccessoryWake8readFromERN2PB6ReaderE : 2012 -> 1940
~ __ZN5CMMsl18AccessoryWakeDebug8readFromERN2PB6ReaderE : 4064 -> 3732
~ __ZN5CMMsl26AudioAccessoryDeviceMotion8readFromERN2PB6ReaderE : 3476 -> 3360
~ __ZN5CMMsl21AuxiliaryDeviceMotion8readFromERN2PB6ReaderE : 3416 -> 3136
~ __ZN5CMMsl14BatchedPPGData8readFromERN2PB6ReaderE : 5600 -> 5360
~ __ZN5CMMsl15BioMotionAnchor8readFromERN2PB6ReaderE : 1240 -> 1176
~ __ZN5CMMsl32BioMotionLinkLengthFitParameters8readFromERN2PB6ReaderE : 2528 -> 2300
~ __ZN5CMMsl13BioMotionPose8readFromERN2PB6ReaderE : 3172 -> 2892
~ __ZN5CMMsl15BraveHeartAccel8readFromERN2PB6ReaderE : 772 -> 732
~ __ZN5CMMsl22BraveHeartDeviceMotion8readFromERN2PB6ReaderE : 772 -> 732
~ __ZN5CMMsl21BraveHeartVO2MaxInput8readFromERN2PB6ReaderE : 772 -> 732
~ __ZN5CMMsl17CV3DPredictedPose8readFromERN2PB6ReaderE : 1464 -> 1340
~ __ZN5CMMsl13CV3DSLAMState8readFromERN2PB6ReaderE : 1828 -> 1652
~ __ZN5CMMsl15ClefCalibration8readFromERN2PB6ReaderE : 2528 -> 2488
~ __ZN5CMMsl18CompassConstraints8readFromERN2PB6ReaderE : 2684 -> 2560
~ __ZN5CMMsl22DeviceMotionCorrection8readFromERN2PB6ReaderE : 3128 -> 2796
~ __ZN5CMMsl22DeviceMotionCovariance8readFromERN2PB6ReaderE : 1400 -> 1276
~ __ZN5CMMsl21DoTEstimatorHandSwing8readFromERN2PB6ReaderE : 3728 -> 3508
~ __ZN5CMMsl19DoTEstimatorWithTNB8readFromERN2PB6ReaderE : 4028 -> 3652
~ __ZN5CMMsl30EntityKitBoundingBoxCorrection8readFromERN2PB6ReaderE : 3908 -> 3680
~ __ZN5CMMsl28EntityKitBoundingBoxDataList8readFromERN2PB6ReaderE : 1016 -> 976
~ __ZN5CMMsl32FaceBlendShapeCoefficientsSample8readFromERN2PB6ReaderE : 928 -> 888
~ __ZN5CMMsl17FaceDownDetection8readFromERN2PB6ReaderE : 2064 -> 1940
~ __ZN5CMMsl29FallDetectionWristStateReplay8readFromERN2PB6ReaderE : 7840 -> 7352
~ __ZN5CMMsl17FrequencyResponse8readFromERN2PB6ReaderE : 1400 -> 1276
~ __ZN5CMMsl21GnssLeechLocationData8readFromERN2PB6ReaderE : 892 -> 772
~ __ZN5CMMsl19GyroBiasConstraints8readFromERN2PB6ReaderE : 2496 -> 2268
~ __ZN5CMMsl16GyroBiasEstimate8readFromERN2PB6ReaderE : 1776 -> 1652
~ __ZN5CMMsl21GyroBiasEstimateError8readFromERN2PB6ReaderE : 1900 -> 1724
~ __ZN5CMMsl11GyroBiasFit8readFromERN2PB6ReaderE : 1392 -> 1268
~ __ZN5CMMsl26GyroCalibrationDataFactory8readFromERN2PB6ReaderE : 772 -> 732
~ __ZN5CMMsl38GyroCalibrationDataNonlinearNonFactory8readFromERN2PB6ReaderE : 772 -> 732
~ __ZN5CMMsl17GyroScaleEstimate8readFromERN2PB6ReaderE : 1776 -> 1652
~ __ZN5CMMsl47HeadToHeadsetAttitudeEstimatorMeasurementUpdate8readFromERN2PB6ReaderE : 2872 -> 2644
~ __ZN5CMMsl35HeadToHeadsetTransformationEstimate8readFromERN2PB6ReaderE : 1528 -> 1404
~ __ZN5CMMsl20InEarAdditionalState8readFromERN2PB6ReaderE : 720 -> 680
~ __ZN5CMMsl13InEarBaseline8readFromERN2PB6ReaderE : 1344 -> 1312
~ __ZN5CMMsl12InEarOptical8readFromERN2PB6ReaderE : 2432 -> 2316
~ __ZN5CMMsl20InEarTransitionEntry8readFromERN2PB6ReaderE : 2596 -> 2392
~ __ZN5CMMsl37InitialHistoricalMeanSeaLevelPressure8readFromERN2PB6ReaderE : 1828 -> 1652
~ __ZN5CMMsl18KappaActivityPhone8readFromERN2PB6ReaderE : 3844 -> 3608
~ __ZN5CMMsl18KappaActivityWatch8readFromERN2PB6ReaderE : 3232 -> 3104
~ __ZN5CMMsl22KappaDirectionOfTravel8readFromERN2PB6ReaderE : 3396 -> 3272
~ __ZN5CMMsl26KappaPeakDetectorMapResult8readFromERN2PB6ReaderE : 4468 -> 4332
~ __ZN5CMMsl15KappaSpinResult8readFromERN2PB6ReaderE : 5472 -> 5152
~ __ZN5CMMsl12KappaTrigger8readFromERN2PB6ReaderE : 7076 -> 6888
~ __ZN5CMMsl17KappaTriggerDebug8readFromERN2PB6ReaderE : 3160 -> 2952
~ __ZN5CMMsl20LSLHeadingEstimation8readFromERN2PB6ReaderE : 3132 -> 2956
~ __ZN5CMMsl38MagnetometerCalibratorFilterParameters8readFromERN2PB6ReaderE : 2692 -> 2412
~ __ZN5CMMsl21MotionLoiAltitudeData8readFromERN2PB6ReaderE : 1332 -> 1208
~ __ZN5CMMsl30MovementStatsGravityProjection8readFromERN2PB6ReaderE : 1708 -> 1584
~ __ZN5CMMsl16NonlinearBiasFit8readFromERN2PB6ReaderE : 4984 -> 4584
~ __ZN5CMMsl7ODTPose8readFromERN2PB6ReaderE : 960 -> 888
~ __ZN5CMMsl30PDRDOTMeasurementSelectorState8readFromERN2PB6ReaderE : 1272 -> 1200
~ __ZN5CMMsl28PDRPedestrianClassifierState8readFromERN2PB6ReaderE : 1348 -> 1276
~ __ZN5CMMsl27PDRPlacementClassifierState8readFromERN2PB6ReaderE : 1272 -> 1200
~ __ZN5CMMsl16PdrMLModelOutput8readFromERN2PB6ReaderE : 960 -> 888
~ __ZN5CMMsl13PearlAttitude8readFromERN2PB6ReaderE : 2688 -> 2512
~ __ZN5CMMsl18PencilDeviceMotion8readFromERN2PB6ReaderE : 1248 -> 1184
~ __ZN5CMMsl24PencilFusionReplayResult8readFromERN2PB6ReaderE : 1792 -> 1728
~ __ZN5CMMsl4Pose8readFromERN2PB6ReaderE : 1392 -> 1268
~ __ZN5CMMsl9PoseState8readFromERN2PB6ReaderE : 1168 -> 1104
~ __ZN5CMMsl12PostureJoint8readFromERN2PB6ReaderE : 1564 -> 1440
~ __ZN5CMMsl15PostureSkeleton8readFromERN2PB6ReaderE : 788 -> 748
~ __ZN5CMMsl16PropagatedAnchor8readFromERN2PB6ReaderE : 1156 -> 1092
~ __ZN5CMMsl15ProxCalibration8readFromERN2PB6ReaderE : 1936 -> 1812
~ __ZN5CMMsl8RawAudio8readFromERN2PB6ReaderE : 1216 -> 1144
~ __ZN5CMMsl28RelativeDeviceMotionInternal8readFromERN2PB6ReaderE : 3864 -> 3740
~ __ZN5CMMsl10Skeleton2D8readFromERN2PB6ReaderE : 932 -> 892
~ __ZN5CMMsl15Skeleton2DJoint8readFromERN2PB6ReaderE : 1276 -> 1204
~ __ZN5CMMsl10Skeleton3D8readFromERN2PB6ReaderE : 472 -> 440
~ __ZN5CMMsl16Skeleton3DLifted8readFromERN2PB6ReaderE : 932 -> 892
~ __ZN5CMMsl21Skeleton3DLiftedJoint8readFromERN2PB6ReaderE : 1132 -> 1060
~ __ZN5CMMsl20Skeleton3DRetargeted8readFromERN2PB6ReaderE : 628 -> 588
~ __ZN5CMMsl13SkeletonJoint8readFromERN2PB6ReaderE : 1564 -> 1440
~ __ZN5CMMsl31TempestPoCAuxiliaryDeviceMotion8readFromERN2PB6ReaderE : 2052 -> 1988
~ __ZN5CMMsl29TempestPoCListenerOrientation8readFromERN2PB6ReaderE : 2048 -> 1924
~ __ZN5CMMsl13VIOEstimation8readFromERN2PB6ReaderE : 6128 -> 5484
~ __ZN5CMMsl7VIOPose8readFromERN2PB6ReaderE : 1488 -> 1416
~ __ZN5CMMsl13VIOReplayPose8readFromERN2PB6ReaderE : 1392 -> 1268
~ __ZN5CMMsl17VisionCompassBias8readFromERN2PB6ReaderE : 1784 -> 1712
~ __ZN5CMMsl18VisualLocalization8readFromERN2PB6ReaderE : 1816 -> 1680
~ __ZN5CMMsl37VisualLocalizationAttitudeConstraints8readFromERN2PB6ReaderE : 1228 -> 1156
~ __ZN5CMMsl22VisualStateMeasurement8readFromERN2PB6ReaderE : 2140 -> 1964
~ __ZN5CMMsl15WifiScanResults8readFromERN2PB6ReaderE : 772 -> 732
~ __ZN5CMMsl20WorkoutSessionPriors8readFromERN2PB6ReaderE : 772 -> 732
~ sub_266f423e4 -> sub_264744fd0 : 4604 -> 4584
~ sub_266f437ac -> sub_264746384 : 5044 -> 4808
~ sub_266f45668 -> sub_264748154 : 5704 -> 4676
~ sub_266f46e00 -> sub_2647494e8 : 1268 -> 900
~ sub_266f47e84 -> sub_26474a3fc : 204 -> 176
~ sub_266f4a194 -> sub_26474c6f0 : 508 -> 420
~ sub_266f4a390 -> sub_26474c894 : 3588 -> 3168
~ sub_266f4c0dc -> sub_26474e43c : 316 -> 268
~ sub_266f4c340 -> sub_26474e670 : 228 -> 140
~ sub_266f4c50c -> sub_26474e7e4 : 216 -> 188
~ sub_266f4ca60 -> sub_26474ed1c : 2132 -> 2036
~ sub_266f4e464 -> sub_2647506c0 : 136 -> 48
~ sub_266f4e5d4 -> sub_2647507d8 : 212 -> 56
~ sub_266f4e9b4 -> sub_264750b1c : 436 -> 164
~ sub_266f4ec78 -> sub_264750cd0 : 328 -> 80
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJIVugB_qVghDI8oqvuBaxFWHprWxJcF91nzmpg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugB_qVghDI8oqvuBaxFWHprWxJcF91nzmpg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugB_qVghDI8oqvuBaxFWHprWxJcF91nzmpg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugB_qVghDI8oqvuBaxFWHprWxJcF91nzmpg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugB_qVghDI8oqvuBaxFWHprWxJcF91nzmpg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugB_qVghDI8oqvuBaxFWHprWxJcF91nzmpg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugB_qVghDI8oqvuBaxFWHprWxJcF91nzmpg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugB_qVghDI8oqvuBaxFWHprWxJcF91nzmpg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugB_qVghDI8oqvuBaxFWHprWxJcF91nzmpg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugB_qVghDI8oqvuBaxFWHprWxJcF91nzmpg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugB_qVghDI8oqvuBaxFWHprWxJcF91nzmpg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugB_qVghDI8oqvuBaxFWHprWxJcF91nzmpg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugB_qVghDI8oqvuBaxFWHprWxJcF91nzmpg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugB_qVghDI8oqvuBaxFWHprWxJcF91nzmpg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugB_qVghDI8oqvuBaxFWHprWxJcF91nzmpg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugB_qVghDI8oqvuBaxFWHprWxJcF91nzmpg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugB_qVghDI8oqvuBaxFWHprWxJcF91nzmpg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"

```
