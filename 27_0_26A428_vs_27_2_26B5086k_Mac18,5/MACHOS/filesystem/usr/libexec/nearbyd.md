## nearbyd

> `/usr/libexec/nearbyd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
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
+575.0.5.0.0
+  __TEXT.__text: 0x4d39d4
+  __TEXT.__auth_stubs: 0x27e0
+  __TEXT.__objc_stubs: 0x139a0
   __TEXT.__init_offsets: 0x2d8
-  __TEXT.__objc_methlist: 0xdeec
-  __TEXT.__gcc_except_tab: 0x4b944
-  __TEXT.__const: 0x3ee288
-  __TEXT.__cstring: 0x34d79
-  __TEXT.__objc_methname: 0x1f463
+  __TEXT.__objc_methlist: 0xdf04
+  __TEXT.__gcc_except_tab: 0x4ba48
+  __TEXT.__const: 0x3ee368
+  __TEXT.__cstring: 0x34e69
+  __TEXT.__objc_methname: 0x1f4e3
   __TEXT.__oslogstring: 0x55887
   __TEXT.__objc_classname: 0x1b5e
-  __TEXT.__objc_methtype: 0x2089a
+  __TEXT.__objc_methtype: 0x208aa
   __TEXT.__ustring: 0x60
   __TEXT.__swift5_typeref: 0x1e8
   __TEXT.__swift5_capture: 0x114

   __TEXT.__swift5_reflstr: 0x2b5
   __TEXT.__swift5_fieldmd: 0x22c
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x1e8b0
+  __TEXT.__unwind_info: 0x1e938
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__const: 0x1d8c8
-  __DATA_CONST.__cfstring: 0x15220
+  __DATA_CONST.__const: 0x1d990
+  __DATA_CONST.__cfstring: 0x153a0
   __DATA_CONST.__objc_classlist: 0x570
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x288

   __DATA_CONST.__objc_arrayobj: 0x1f8
   __DATA_CONST.__objc_intobj: 0x708
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA_CONST.__auth_got: 0x1400
-  __DATA_CONST.__got: 0x948
+  __DATA_CONST.__auth_got: 0x1408
+  __DATA_CONST.__got: 0x958
   __DATA_CONST.__auth_ptr: 0xe0
-  __DATA.__objc_const: 0x18248
-  __DATA.__objc_selrefs: 0x60e0
-  __DATA.__objc_ivar: 0x1790
+  __DATA.__objc_const: 0x18278
+  __DATA.__objc_selrefs: 0x60f0
+  __DATA.__objc_ivar: 0x1794
   __DATA.__objc_data: 0x3ae8
   __DATA.__data: 0x35c4
   __DATA.__common: 0xe08

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 21370
-  Symbols:   950
-  CStrings:  17450
+  Functions: 21392
+  Symbols:   953
+  CStrings:  17464
 
Symbols:
+ _CFPreferencesCopyValue
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
CStrings:
+ ", Suggested Nearby Threshold: %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "Tf,N,V_suggestedNearbyThreshold"
+ "_suggestedNearbyThreshold"
+ "filter"
+ "hysteresis_sample_constant"
+ "hysteresis_threshold_delta_in_dB"
+ "hysteresis_threshold_delta_out_dB"
+ "hysteresis_time_constant_seconds"
+ "max_of_mean"
+ "mean"
+ "measurement_buffer_size"
+ "median"
+ "setSuggestedNearbyThreshold:"
+ "suggestedNearbyThreshold"
+ "v464@0:8{Solution={ConvergenceState=iBBBB}{optional<nearby::algorithms::common::RangeResult>=(?=c{RangeResult=Qdfi{optional<nearby::algorithms::common::AngleMeasurement>=(?=c{AngleMeasurement=ffi})B}d{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}ii{optional<nearby::algorithms::common::MagneticFieldStrengthCheckParameter>=(?=c{MagneticFieldStrengthCheckParameter=idd})B}{optional<double>=(?=cd)B}{optional<unsigned short>=(?=cS)B}{optional<unsigned char>=(?=cC)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}})B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}i{optional<double>=(?=cd)B}{optional<float __attribute__((ext_vector_type(3)))>=(?=c)B}{optional<float __attribute__((ext_vector_type(3)))>=(?=c)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}{optional<bool>=(?=cB)B}{optional<nearby::algorithms::common::OdometryAvailabilityState>=(?=ci)B}{optional<nearby::algorithms::common::AlgorithmSource>=(?=ci)B}{optional<nearby::algorithms::common::PeerMotionState>=(?=ci)B}BB{optional<double>=(?=cd)B}}16"
+ "{BTCSItemFinderAlgorithmConfig=BBBdd{ParticleFilterConfig=BBqBBBdddddddddddddBBddddddBdddddddddddddddddddddddddddddddBBBBBdiddddiB{vector<nearby::algorithms::common::TLocationScaleParamsWithRange, std::allocator<nearby::algorithms::common::TLocationScaleParamsWithRange>>=^{TLocationScaleParamsWithRange}^{TLocationScaleParamsWithRange}{?=^{TLocationScaleParamsWithRange}}}{vector<nearby::algorithms::common::TLocationScaleParamsWithRange, std::allocator<nearby::algorithms::common::TLocationScaleParamsWithRange>>=^{TLocationScaleParamsWithRange}^{TLocationScaleParamsWithRange}{?=^{TLocationScaleParamsWithRange}}}}{SyntheticApertureConfig=BBBBBdd}B}16@0:8"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "v448@0:8{Solution={ConvergenceState=iBBBB}{optional<nearby::algorithms::common::RangeResult>=(?=c{RangeResult=Qdfi{optional<nearby::algorithms::common::AngleMeasurement>=(?=c{AngleMeasurement=ffi})B}d{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}ii{optional<nearby::algorithms::common::MagneticFieldStrengthCheckParameter>=(?=c{MagneticFieldStrengthCheckParameter=idd})B}{optional<double>=(?=cd)B}{optional<unsigned short>=(?=cS)B}{optional<unsigned char>=(?=cC)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}})B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}i{optional<double>=(?=cd)B}{optional<float __attribute__((ext_vector_type(3)))>=(?=c)B}{optional<float __attribute__((ext_vector_type(3)))>=(?=c)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}{optional<bool>=(?=cB)B}{optional<nearby::algorithms::common::OdometryAvailabilityState>=(?=ci)B}{optional<nearby::algorithms::common::AlgorithmSource>=(?=ci)B}{optional<nearby::algorithms::common::PeerMotionState>=(?=ci)B}BB}16"
- "{BTCSItemFinderAlgorithmConfig=BBB{ParticleFilterConfig=BBqBBBdddddddddddddBBddddddBdddddddddddddddddddddddddddddddBBBBBdiddddiB{vector<nearby::algorithms::common::TLocationScaleParamsWithRange, std::allocator<nearby::algorithms::common::TLocationScaleParamsWithRange>>=^{TLocationScaleParamsWithRange}^{TLocationScaleParamsWithRange}{?=^{TLocationScaleParamsWithRange}}}{vector<nearby::algorithms::common::TLocationScaleParamsWithRange, std::allocator<nearby::algorithms::common::TLocationScaleParamsWithRange>>=^{TLocationScaleParamsWithRange}^{TLocationScaleParamsWithRange}{?=^{TLocationScaleParamsWithRange}}}}{SyntheticApertureConfig=BBBBBdd}B}16@0:8"
```
