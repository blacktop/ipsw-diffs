## locationd

> `/usr/libexec/locationd`

```diff

-2964.0.3.0.0
-  __TEXT.__text: 0x1adb95c
+2964.0.4.0.0
+  __TEXT.__text: 0x1adbc70
   __TEXT.__auth_stubs: 0x60a0
   __TEXT.__objc_stubs: 0x42960
   __TEXT.__init_offsets: 0xb30
   __TEXT.__objc_methlist: 0x2f058
   __TEXT.__const: 0x1503e9
-  __TEXT.__cstring: 0x1d9e14
-  __TEXT.__gcc_except_tab: 0xdeb70
+  __TEXT.__cstring: 0x1d9f24
+  __TEXT.__gcc_except_tab: 0xdeba4
   __TEXT.__objc_methname: 0x5ff8d
-  __TEXT.__oslogstring: 0x275d09
+  __TEXT.__oslogstring: 0x275dd9
   __TEXT.__objc_classname: 0x7b56
   __TEXT.__objc_methtype: 0x4063e
   __TEXT.__constg_swiftt: 0x204

   __TEXT.__swift5_reflstr: 0x29
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_capture: 0x40
-  __TEXT.__unwind_info: 0x6f788
+  __TEXT.__unwind_info: 0x6f798
   __TEXT.__eh_frame: 0x1370
   __DATA_CONST.__auth_got: 0x3070
   __DATA_CONST.__got: 0x2d00

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 100750
+  Functions: 100751
   Symbols:   3067
-  CStrings:  83178
+  CStrings:  83181
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/34f5057a-19fd-11f0-a005-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
+ "/AppleInternal/Library/BuildRoots/34f5057a-19fd-11f0-a005-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
+ "/AppleInternal/Library/BuildRoots/34f5057a-19fd-11f0-a005-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "/AppleInternal/Library/BuildRoots/34f5057a-19fd-11f0-a005-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/34f5057a-19fd-11f0-a005-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "21:59:18"
+ "22:09:27"
+ "Apr 15 2025"
+ "Apr 15 2025 22:02:03"
+ "CL: CLGnssOdometer::onSignalEnvironmentNotification"
+ "CLGnssOdometer::onSignalEnvironmentNotification"
+ "GPSODOM,Set signal environment,%{public}d,fidelity,%{public}d"
+ "bool CLGpsOdometryInterface::update(GNSS::PerEpochData &, const GNSS::PerEpochData &, const CLMotionActivity &, const CMWorkoutType &, const bool, const GNSS::PerEpochData &, const CLSignalEnvironmentProvider_Type::SignalEnvironmentType &, const CLSignalEnvironmentProvider_Type::SignalEnvironmentFidelityLevel &, const bool, const std::optional<CLPedometerPathStraightness> &)"
+ "void CLGnssOdometer::onSignalEnvironmentNotification(int, const CLSignalEnvironmentProvider_Type::Notification &, const CLSignalEnvironmentProvider_Type::NotificationData &)"
+ "void CLGpsOdometryInterface::switchContext(const CLMotionActivity &, const CLSignalEnvironmentProvider_Type::SignalEnvironmentType &, const CLSignalEnvironmentProvider_Type::SignalEnvironmentFidelityLevel &, const CMWorkoutType &)"
+ "{\"msg%{public}.0s\":\"CLGnssOdometer::onSignalEnvironmentNotification\", \"event\":%{public, location:escape_only}s, \"this\":\"%{public}p\"}"
- "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
- "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
- "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "22:15:57"
- "22:33:56"
- "Apr 10 2025"
- "Apr 10 2025 22:18:43"
- "GPSODOM,Set signal environment,%{public}d"
- "bool CLGpsOdometryInterface::update(GNSS::PerEpochData &, const GNSS::PerEpochData &, const CLMotionActivity &, const CMWorkoutType &, const bool, const GNSS::PerEpochData &, const CLSignalEnvironmentProvider_Type::SignalEnvironmentType &, const bool, const std::optional<CLPedometerPathStraightness> &)"
- "void CLGnssOdometer::setSignalEnvironment(CLSignalEnvironmentProvider_Type::SignalEnvironmentType)"
- "void CLGpsOdometryInterface::switchContext(const CLMotionActivity &, const CLSignalEnvironmentProvider_Type::SignalEnvironmentType &, const CMWorkoutType &)"

```
