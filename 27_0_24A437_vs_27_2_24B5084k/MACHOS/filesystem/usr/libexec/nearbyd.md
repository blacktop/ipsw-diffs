## nearbyd

> `/usr/libexec/nearbyd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-569.0.0.0.0
-  __TEXT.__text: 0x54b4d0
-  __TEXT.__auth_stubs: 0x30d0
-  __TEXT.__objc_stubs: 0x17500
+575.0.5.0.0
+  __TEXT.__text: 0x54dbe4
+  __TEXT.__auth_stubs: 0x30f0
+  __TEXT.__objc_stubs: 0x17600
   __TEXT.__init_offsets: 0x6fc
-  __TEXT.__objc_methlist: 0xf85c
-  __TEXT.__gcc_except_tab: 0x55600
-  __TEXT.__const: 0x3fa9b0
-  __TEXT.__cstring: 0x38c82
-  __TEXT.__objc_methname: 0x23925
-  __TEXT.__oslogstring: 0x63a1a
+  __TEXT.__objc_methlist: 0xf8bc
+  __TEXT.__gcc_except_tab: 0x558ac
+  __TEXT.__const: 0x3faaa0
+  __TEXT.__cstring: 0x38e52
+  __TEXT.__objc_methname: 0x23aa5
+  __TEXT.__oslogstring: 0x63ada
   __TEXT.__objc_classname: 0x20be
-  __TEXT.__objc_methtype: 0x22ded
+  __TEXT.__objc_methtype: 0x22dfd
   __TEXT.__ustring: 0x60
   __TEXT.__swift5_typeref: 0x7ec
   __TEXT.__swift5_capture: 0x574

   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x2c
   __TEXT.__swift_as_cont: 0x80
-  __TEXT.__unwind_info: 0x22070
+  __TEXT.__unwind_info: 0x22138
   __TEXT.__eh_frame: 0x5a0
-  __DATA_CONST.__const: 0x1f4b8
-  __DATA_CONST.__cfstring: 0x17520
+  __DATA_CONST.__const: 0x1f5c0
+  __DATA_CONST.__cfstring: 0x177a0
   __DATA_CONST.__objc_classlist: 0x640
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x330

   __DATA_CONST.__objc_superrefs: 0x538
   __DATA_CONST.__objc_arraydata: 0x480
   __DATA_CONST.__objc_arrayobj: 0x228
-  __DATA_CONST.__objc_intobj: 0x990
+  __DATA_CONST.__objc_intobj: 0x978
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA_CONST.__auth_got: 0x1880
-  __DATA_CONST.__got: 0xe60
+  __DATA_CONST.__auth_got: 0x1890
+  __DATA_CONST.__got: 0xe68
   __DATA_CONST.__auth_ptr: 0x300
-  __DATA.__objc_const: 0x1b800
-  __DATA.__objc_selrefs: 0x7180
-  __DATA.__objc_ivar: 0x1a1c
+  __DATA.__objc_const: 0x1b900
+  __DATA.__objc_selrefs: 0x71c0
+  __DATA.__objc_ivar: 0x1a34
   __DATA.__objc_data: 0x4a18
   __DATA.__data: 0x42cc
   __DATA.__common: 0xe80

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 23573
-  Symbols:   1309
-  CStrings:  19939
+  Functions: 23613
+  Symbols:   1312
+  CStrings:  19977
 
Symbols:
+ _CFPreferencesCopyValue
+ _NSSelectorFromString
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
- _CBConnectPeripheralOptionConnectionUseCase
CStrings:
+ "#btcs,PHY debug: %lu slice(s) x %lu byte(s) for %lu IQ tone(s)"
+ "#ses-btcs,BTCS algo: OTA override -> %s (%ld)"
+ "#ses-btcs,BTCS algo: OTA value %ld unrecognized; falling back to default %s (%ld)"
+ "#ses-btcs,BTCS forceTqiZero: %@"
+ ", Suggested Nearby Threshold: %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "<unknown>"
+ "BTCSFusionConfig defaulting to: %ld (%s)"
+ "BTCSFusionConfig invalid value %ld, defaulting to MedianCalib"
+ "Fused"
+ "LE range: %.4f m (bwMode=%lu errorCode=%d)"
+ "NIForegroundAccessoryBlueToothChannelSoundingAlgorithmSelect"
+ "NIForegroundAccessoryBlueToothChannelSoundingForceTqiZero"
+ "NN"
+ "PHY_Debug_Data"
+ "T@\"NSData\",&,N,V_phyDebugData"
+ "TB,N,V_forceTqiZero"
+ "TQ,N,V_algorithmSelect"
+ "Tf,N,V_suggestedNearbyThreshold"
+ "_algorithmSelect"
+ "_forceTqiZero"
+ "_phyDebugData"
+ "_resolvedAlgorithmSelect"
+ "_resolvedForceTqiZero"
+ "_suggestedNearbyThreshold"
+ "algorithmSelect %s (%ld) unrecognized; using SuperResolution (SR) as fallback"
+ "algorithmSelect: %s (%ld)"
+ "bwMode detection: toneCount=%lu lower18Zero=%d upper20Zero=%d upper18Zero=%d → %s"
+ "fcff7ffcffffff070000"
+ "filter"
+ "forceTqiZero"
+ "hysteresis_sample_constant"
+ "hysteresis_threshold_delta_in_dB"
+ "hysteresis_threshold_delta_out_dB"
+ "hysteresis_time_constant_seconds"
+ "kCBCSPhyDebugData"
+ "kCBCSPhyDebugNumSteps"
+ "max_of_mean"
+ "mean"
+ "measurement_buffer_size"
+ "median"
+ "phyDebugData"
+ "phyDebugNumSteps"
+ "pre-cal reject: rssi0=%.1f dBm below min (%.1f dBm) at range=%.2f m"
+ "setAlgorithmSelect:"
+ "setForceTqiZero:"
+ "setPhyDebugData:"
+ "setSuggestedNearbyThreshold:"
+ "strong-signal: srRange=%.4f m exceeds %.1f m bound, fusedRange=leRange=%.4f m (maxRssi=%.1f dBm)"
+ "suggestedNearbyThreshold"
+ "v464@0:8{Solution={ConvergenceState=iBBBB}{optional<nearby::algorithms::common::RangeResult>=(?=c{RangeResult=Qdfi{optional<nearby::algorithms::common::AngleMeasurement>=(?=c{AngleMeasurement=ffi})B}d{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}ii{optional<nearby::algorithms::common::MagneticFieldStrengthCheckParameter>=(?=c{MagneticFieldStrengthCheckParameter=idd})B}{optional<double>=(?=cd)B}{optional<unsigned short>=(?=cS)B}{optional<unsigned char>=(?=cC)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}})B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}i{optional<double>=(?=cd)B}{optional<float __attribute__((ext_vector_type(3)))>=(?=c)B}{optional<float __attribute__((ext_vector_type(3)))>=(?=c)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}{optional<bool>=(?=cB)B}{optional<nearby::algorithms::common::OdometryAvailabilityState>=(?=ci)B}{optional<nearby::algorithms::common::AlgorithmSource>=(?=ci)B}{optional<nearby::algorithms::common::PeerMotionState>=(?=ci)B}BB{optional<double>=(?=cd)B}}16"
+ "{BTCSItemFinderAlgorithmConfig=BBBdd{ParticleFilterConfig=BBqBBBdddddddddddddBBddddddBdddddddddddddddddddddddddddddddBBBBBdiddddiB{vector<nearby::algorithms::common::TLocationScaleParamsWithRange, std::allocator<nearby::algorithms::common::TLocationScaleParamsWithRange>>=^{TLocationScaleParamsWithRange}^{TLocationScaleParamsWithRange}{?=^{TLocationScaleParamsWithRange}}}{vector<nearby::algorithms::common::TLocationScaleParamsWithRange, std::allocator<nearby::algorithms::common::TLocationScaleParamsWithRange>>=^{TLocationScaleParamsWithRange}^{TLocationScaleParamsWithRange}{?=^{TLocationScaleParamsWithRange}}}}{SyntheticApertureConfig=BBBBBdd}B}16@0:8"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "BTCSFusionConfig invalid value %ld, defaulting to SingleCalib"
- "BTCSRangeAlgorithmSelect"
- "BTCSRangeAlgorithmSelect defaulting to: 3 (Fused)"
- "BTCSRangeAlgorithmSelect initialized to: %ld (Fused)"
- "BTCSRangeAlgorithmSelect initialized to: %ld (Leading Edge)"
- "BTCSRangeAlgorithmSelect initialized to: %ld (Neural Network)"
- "BTCSRangeAlgorithmSelect initialized to: %ld (Super Resolution)"
- "LE GetRange: bwMode=%lu algoBWMode=%u expectedBins=%u paddedSize=%u"
- "LE engine range: %.4f m"
- "bwMode detection: toneCount=%lu lower18Zero=%d upper20Zero=%d upper19Zero=%d → %s"
- "fcff7ffcffffff030000"
- "v448@0:8{Solution={ConvergenceState=iBBBB}{optional<nearby::algorithms::common::RangeResult>=(?=c{RangeResult=Qdfi{optional<nearby::algorithms::common::AngleMeasurement>=(?=c{AngleMeasurement=ffi})B}d{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}ii{optional<nearby::algorithms::common::MagneticFieldStrengthCheckParameter>=(?=c{MagneticFieldStrengthCheckParameter=idd})B}{optional<double>=(?=cd)B}{optional<unsigned short>=(?=cS)B}{optional<unsigned char>=(?=cC)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}})B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}i{optional<double>=(?=cd)B}{optional<float __attribute__((ext_vector_type(3)))>=(?=c)B}{optional<float __attribute__((ext_vector_type(3)))>=(?=c)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}{optional<bool>=(?=cB)B}{optional<nearby::algorithms::common::OdometryAvailabilityState>=(?=ci)B}{optional<nearby::algorithms::common::AlgorithmSource>=(?=ci)B}{optional<nearby::algorithms::common::PeerMotionState>=(?=ci)B}BB}16"
- "{BTCSItemFinderAlgorithmConfig=BBB{ParticleFilterConfig=BBqBBBdddddddddddddBBddddddBdddddddddddddddddddddddddddddddBBBBBdiddddiB{vector<nearby::algorithms::common::TLocationScaleParamsWithRange, std::allocator<nearby::algorithms::common::TLocationScaleParamsWithRange>>=^{TLocationScaleParamsWithRange}^{TLocationScaleParamsWithRange}{?=^{TLocationScaleParamsWithRange}}}{vector<nearby::algorithms::common::TLocationScaleParamsWithRange, std::allocator<nearby::algorithms::common::TLocationScaleParamsWithRange>>=^{TLocationScaleParamsWithRange}^{TLocationScaleParamsWithRange}{?=^{TLocationScaleParamsWithRange}}}}{SyntheticApertureConfig=BBBBBdd}B}16@0:8"
```
