## nearbyd

> `/usr/libexec/nearbyd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-568.0.0.0.0
-  __TEXT.__text: 0x4d2268
-  __TEXT.__auth_stubs: 0x27d0
-  __TEXT.__objc_stubs: 0x13960
-  __TEXT.__init_offsets: 0x2d8
-  __TEXT.__objc_methlist: 0xdeec
-  __TEXT.__gcc_except_tab: 0x4b944
-  __TEXT.__const: 0x3ee288
-  __TEXT.__cstring: 0x34d79
-  __TEXT.__objc_methname: 0x1f463
-  __TEXT.__oslogstring: 0x55887
+575.0.10.0.0
+  __TEXT.__text: 0x4df9bc
+  __TEXT.__auth_stubs: 0x27e0
+  __TEXT.__objc_stubs: 0x13ac0
+  __TEXT.__init_offsets: 0x2dc
+  __TEXT.__objc_methlist: 0xe02c
+  __TEXT.__gcc_except_tab: 0x4c3e8
+  __TEXT.__const: 0x3ee928
+  __TEXT.__cstring: 0x35557
+  __TEXT.__objc_methname: 0x1f693
+  __TEXT.__oslogstring: 0x56592
   __TEXT.__objc_classname: 0x1b5e
-  __TEXT.__objc_methtype: 0x2089a
+  __TEXT.__objc_methtype: 0x208da
   __TEXT.__ustring: 0x60
   __TEXT.__swift5_typeref: 0x1e8
   __TEXT.__swift5_capture: 0x114

   __TEXT.__swift5_reflstr: 0x2b5
   __TEXT.__swift5_fieldmd: 0x22c
   __TEXT.__swift5_types: 0xc
-  __TEXT.__info_plist: 0x3ac
-  __TEXT.__unwind_info: 0x1e8b0
+  __TEXT.__info_plist: 0x3b2
+  __TEXT.__unwind_info: 0x1ede8
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__const: 0x1d8c8
-  __DATA_CONST.__cfstring: 0x15220
+  __DATA_CONST.__const: 0x1de68
+  __DATA_CONST.__cfstring: 0x15540
   __DATA_CONST.__objc_classlist: 0x570
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x288
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x4f0
-  __DATA_CONST.__objc_arraydata: 0x438
+  __DATA_CONST.__objc_arraydata: 0x448
   __DATA_CONST.__objc_arrayobj: 0x1f8
   __DATA_CONST.__objc_intobj: 0x708
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA_CONST.__auth_got: 0x1400
-  __DATA_CONST.__got: 0x948
+  __DATA_CONST.__auth_got: 0x1408
+  __DATA_CONST.__got: 0x960
   __DATA_CONST.__auth_ptr: 0xe0
-  __DATA.__objc_const: 0x18248
-  __DATA.__objc_selrefs: 0x60e0
-  __DATA.__objc_ivar: 0x1790
+  __DATA.__objc_const: 0x182d0
+  __DATA.__objc_selrefs: 0x6140
+  __DATA.__objc_ivar: 0x179c
   __DATA.__objc_data: 0x3ae8
   __DATA.__data: 0x35c4
-  __DATA.__bss: 0xcd68
+  __DATA.__bss: 0xd4d0
   __DATA.__common: 0xe08
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 21370
-  Symbols:   950
-  CStrings:  17450
+  Functions: 21585
+  Symbols:   953
+  CStrings:  17553
 
Symbols:
+ _CFPreferencesCopyValue
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
CStrings:
+ "#ble,Activate. Supports UWB: [%d], Supports WiFi ToF: [%d], Supports Perception: [%d], TokenFlags: [0x%08x]. ControlFlags: [0x%08x]"
+ "#intentaggr,Deliver handoff intention: %d, from source: %s, beforeExecute: %d"
+ "#intentaggr,clear up: fSilenceTimer == nil: %s"
+ "#intentaggr,delivered handoff intention %d to client for device: %llu"
+ "#intentaggr,silence timer armed for: %.1fs"
+ "#jointEsti, NRBYRegionJointEstimator reset"
+ "#jointEsti, Not configure exit execute region, return even when motion pullback Detected"
+ "#jointEsti, Not support current technology: %d"
+ "#jointEsti, Not support joint estimator for tech: %d"
+ "#jointEsti, Pullback detected, sending NON-Execute region back to client to dismiss handoff, %.4fs since execute detected"
+ "#jointEsti, We are already in Execute withdrawn state, NOP"
+ "#jointEsti, We are not in Execute Region yet but detected motion pullback?"
+ "#jointEsti, [Motion] spatial gesture based user handoff intention detected."
+ "#jointEsti, _combine joint Region cached [tech: %d] Region win: %f , current received [tech: %d] region: %f  "
+ "#jointEsti, _combineRegionCallback NOT update region to clients since its same"
+ "#jointEsti, should send out new BT region trigger by CV."
+ "#jointEsti, should send out new BT region trigger by Motion."
+ "#jointEsti, should send out new BT region trigger by PureBT."
+ "#jointEsti, should send out new region: %s, from tech [BT: %@], [wifi: %@]"
+ "#jointEsti, ~NRBYRegionJointEstimator"
+ "#regionmon Force set KRSSIThresholdOffset before execute with default write: %.2f"
+ "#regionmon _combineBTRegionForJointEstimatorCallback no _deviceRegionJointEstimators for deviceIdentifier: %llu"
+ "#regionmon _jointPrewarmStateUpdate: currentDeviceAssociationState for %llu, motion state: %d, orientation state: %d, Prewarm(Desk) Region state: %d"
+ "#regionmon offsetCurrentHighestBT for deviceId: %llu did not find any devices that match"
+ "#ses-loc,DL-TDoA background runtime budget (%.0fs) elapsed; force-closing session."
+ "#ses-loc,DL-TDoA background session NOT supported"
+ "#ses-loc,DL-TDoA session started while Not Foreground: %d; will be force-closed after %.0fs."
+ "#ses-loc,Skipping client update: no valid DL-TDoA anchors in range while app is backgrounded"
+ "#spatialGesturesPredictor #probabilities Other = %f, Handoff = %f"
+ "#spatialGesturesPredictor GesturePredictorSecondary successfully created!"
+ "#threshold-detector, accepting sustained high rssi: %f, jump: %f dB from %f"
+ "#threshold-detector, bubble entry DELAY: %f s (held %f, estimate %f; estimate %f once confirmed by %f; border %f)"
+ "#threshold-detector, bubble entry DELAY: %f s, confirming sample dropped (held %f, estimate %f; estimate %f once confirmed by %f; border %f)"
+ "#threshold-detector, one-hot rssi outlier rejected: %f, first sample with nothing buffered (next sample %f after %f s did not confirm)"
+ "#threshold-detector, one-hot rssi outlier rejected: %f, jump: %f dB from %f, buffered: %zu (next sample %f after %f s did not confirm)"
+ "#threshold-detector, pending first-sample one-hot detected: %f, above border %f with nothing buffered"
+ "#threshold-detector, pending one-hot detected: %f, jump: %f dB from %f, buffered: %zu"
+ "#threshold-detector, reinstating confirmed rssi sample: %f (confirmed by %f after %f s)"
+ ", Suggested Nearby Threshold: %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "ATVRemote1,5"
+ "AudioAccessory11,1"
+ "AudioAccessory11,1,"
+ "CV"
+ "DL-TDoA background session NOT supported"
+ "DelegateProxy: updated cv distance: %.3f. Object: %{private}@"
+ "DelegateProxy: updated cv region %{private}@ (previous: %{private}@). Object: %{private}@"
+ "HomeAccessory"
+ "HomeAccessory17,1"
+ "HomeAccessory17,2"
+ "HomeKit Accessory Control Devices"
+ "HomeKit Accessory Control Devices | Known Devices"
+ "Motion"
+ "NIDLTDOABackgroundLaunchEnabled"
+ "NIPerceptionBubbleRSSIOffsetThreshold"
+ "NIPerceptionSignpost_HandoffGestureModelCreate"
+ "NIPerceptionSignpost_HandoffGestureModelDestroy"
+ "NRBYRegionJointEstimator.mm"
+ "Perception"
+ "PerceptionHandoffSessionEnableMonitorLog"
+ "Technology duplicated"
+ "Tf,N,V_suggestedNearbyThreshold"
+ "_appLaunchedFromBackground"
+ "_checkIsInternalToolProxtool"
+ "_computeRecencyWeight"
+ "_isClientBackgrounded"
+ "_sessionLaunchedFromBackground"
+ "_suggestedNearbyThreshold"
+ "com.apple.nearbyd.reg_monitor.intention"
+ "default_bluetooth_filter_rssi_gating"
+ "deviceModelHomeAccessory:"
+ "didUpdateDeviceAssociationStatus:"
+ "filter"
+ "hysteresis_sample_constant"
+ "hysteresis_threshold_delta_in_dB"
+ "hysteresis_threshold_delta_out_dB"
+ "hysteresis_time_constant_seconds"
+ "iPhone18,1"
+ "iPhone18,2"
+ "iPhone18,3"
+ "iPhone18,4"
+ "iPhone19,2"
+ "iPhone19,3"
+ "iPhone19,7"
+ "isBackgroundSession"
+ "max_of_mean"
+ "mean"
+ "measurement_buffer_size"
+ "median"
+ "object:didUpdateCVDistance:"
+ "object:didUpdateCVRegion:previousRegion:"
+ "outlier_suppression_enabled"
+ "session:didUpdateDeviceAssociationStatus:"
+ "session:object:didUpdateCVDistance:"
+ "session:object:didUpdateCVRegion:previousRegion:"
+ "sessionInvalidateWithReason:isLaunchedFromBackground:"
+ "setSuggestedNearbyThreshold:"
+ "suggestedNearbyThreshold"
+ "supportsDeviceCVPerception"
+ "timeGap >= 0"
+ "v16@?0B8i12"
+ "v20@?0Q8f16"
+ "v24@0:8C16B20"
+ "v28@?0d8Q16B24"
+ "v32@0:8@\"NINearbyObject\"16d24"
+ "v392@?0d8Q16i24{optional<nearby::algorithms::region_monitoring::Region>=(?=c{Region={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}fiiiBB})B}28{optional<nearby::algorithms::region_monitoring::Region>=(?=c{Region={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}fiiiBB})B}84{optional<nearby::algorithms::common::RangeResult>=(?=c{RangeResult=Qdfi{optional<nearby::algorithms::common::AngleMeasurement>=(?=c{AngleMeasurement=ffi})B}d{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}ii{optional<nearby::algorithms::common::MagneticFieldStrengthCheckParameter>=(?=c{MagneticFieldStrengthCheckParameter=idd})B}{optional<double>=(?=cd)B}{optional<unsigned short>=(?=cS)B}{optional<unsigned char>=(?=cC)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}})B}140{optional<float>=(?=cf)B}380B388"
+ "v464@0:8{Solution={ConvergenceState=iBBBB}{optional<nearby::algorithms::common::RangeResult>=(?=c{RangeResult=Qdfi{optional<nearby::algorithms::common::AngleMeasurement>=(?=c{AngleMeasurement=ffi})B}d{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}ii{optional<nearby::algorithms::common::MagneticFieldStrengthCheckParameter>=(?=c{MagneticFieldStrengthCheckParameter=idd})B}{optional<double>=(?=cd)B}{optional<unsigned short>=(?=cS)B}{optional<unsigned char>=(?=cC)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}})B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}i{optional<double>=(?=cd)B}{optional<float __attribute__((ext_vector_type(3)))>=(?=c)B}{optional<float __attribute__((ext_vector_type(3)))>=(?=c)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}{optional<bool>=(?=cB)B}{optional<nearby::algorithms::common::OdometryAvailabilityState>=(?=ci)B}{optional<nearby::algorithms::common::AlgorithmSource>=(?=ci)B}{optional<nearby::algorithms::common::PeerMotionState>=(?=ci)B}BB{optional<double>=(?=cd)B}}16"
+ "v55@0:8@\"<PRBLEDiscoveryConsuming>\"16@\"NSObject<OS_dispatch_queue>\"24@\"NSData\"32@\"NSData\"40{NIBluetoothDiscoveryControlFlags=BBB}48I51"
+ "v55@0:8@16@24@32@40{NIBluetoothDiscoveryControlFlags=BBB}48I51"
+ "{BTCSItemFinderAlgorithmConfig=BBBdd{ParticleFilterConfig=BBqBBBdddddddddddddBBddddddBdddddddddddddddddddddddddddddddBBBBBdiddddiB{vector<nearby::algorithms::common::TLocationScaleParamsWithRange, std::allocator<nearby::algorithms::common::TLocationScaleParamsWithRange>>=^{TLocationScaleParamsWithRange}^{TLocationScaleParamsWithRange}{?=^{TLocationScaleParamsWithRange}}}{vector<nearby::algorithms::common::TLocationScaleParamsWithRange, std::allocator<nearby::algorithms::common::TLocationScaleParamsWithRange>>=^{TLocationScaleParamsWithRange}^{TLocationScaleParamsWithRange}{?=^{TLocationScaleParamsWithRange}}}}{SyntheticApertureConfig=BBBBBdd}B}16@0:8"
- "#ble,Activate. Supports UWB: [%d], Supports WiFi ToF: [%d], TokenFlags: [0x%08x]. ControlFlags: [0x%08x]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "sessionInvalidateWithReason:"
- "v448@0:8{Solution={ConvergenceState=iBBBB}{optional<nearby::algorithms::common::RangeResult>=(?=c{RangeResult=Qdfi{optional<nearby::algorithms::common::AngleMeasurement>=(?=c{AngleMeasurement=ffi})B}d{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}ii{optional<nearby::algorithms::common::MagneticFieldStrengthCheckParameter>=(?=c{MagneticFieldStrengthCheckParameter=idd})B}{optional<double>=(?=cd)B}{optional<unsigned short>=(?=cS)B}{optional<unsigned char>=(?=cC)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}})B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}i{optional<double>=(?=cd)B}{optional<float __attribute__((ext_vector_type(3)))>=(?=c)B}{optional<float __attribute__((ext_vector_type(3)))>=(?=c)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}{optional<bool>=(?=cB)B}{optional<nearby::algorithms::common::OdometryAvailabilityState>=(?=ci)B}{optional<nearby::algorithms::common::AlgorithmSource>=(?=ci)B}{optional<nearby::algorithms::common::PeerMotionState>=(?=ci)B}BB}16"
- "v54@0:8@\"<PRBLEDiscoveryConsuming>\"16@\"NSObject<OS_dispatch_queue>\"24@\"NSData\"32@\"NSData\"40{NIBluetoothDiscoveryControlFlags=BB}48I50"
- "v54@0:8@16@24@32@40{NIBluetoothDiscoveryControlFlags=BB}48I50"
- "{BTCSItemFinderAlgorithmConfig=BBB{ParticleFilterConfig=BBqBBBdddddddddddddBBddddddBdddddddddddddddddddddddddddddddBBBBBdiddddiB{vector<nearby::algorithms::common::TLocationScaleParamsWithRange, std::allocator<nearby::algorithms::common::TLocationScaleParamsWithRange>>=^{TLocationScaleParamsWithRange}^{TLocationScaleParamsWithRange}{?=^{TLocationScaleParamsWithRange}}}{vector<nearby::algorithms::common::TLocationScaleParamsWithRange, std::allocator<nearby::algorithms::common::TLocationScaleParamsWithRange>>=^{TLocationScaleParamsWithRange}^{TLocationScaleParamsWithRange}{?=^{TLocationScaleParamsWithRange}}}}{SyntheticApertureConfig=BBBBBdd}B}16@0:8"
```
