## locationd

> `/usr/libexec/locationd`

```diff

-2964.0.4.0.0
-  __TEXT.__text: 0x1adbc50
+2964.0.7.0.0
+  __TEXT.__text: 0x1adbbc0
   __TEXT.__auth_stubs: 0x60a0
   __TEXT.__objc_stubs: 0x42960
   __TEXT.__init_offsets: 0xb30
   __TEXT.__objc_methlist: 0x2f058
   __TEXT.__const: 0x1503d9
-  __TEXT.__cstring: 0x1d9f24
+  __TEXT.__cstring: 0x1d9f04
   __TEXT.__gcc_except_tab: 0xdeba4
-  __TEXT.__objc_methname: 0x5ff8d
-  __TEXT.__oslogstring: 0x275dd9
+  __TEXT.__objc_methname: 0x5ffaf
+  __TEXT.__oslogstring: 0x275f09
   __TEXT.__objc_classname: 0x7b56
   __TEXT.__objc_methtype: 0x4063e
   __TEXT.__constg_swiftt: 0x204

   __TEXT.__swift5_reflstr: 0x29
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_capture: 0x40
-  __TEXT.__unwind_info: 0x6f798
+  __TEXT.__unwind_info: 0x6f790
   __TEXT.__eh_frame: 0x1370
   __DATA_CONST.__auth_got: 0x3070
   __DATA_CONST.__got: 0x2d00

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 4FF8C82B-2BA9-3B0D-A154-FD3E5BFCC8B5
+  UUID: D63A9FB1-EC32-3E05-9BE5-185887B0F7F7
   Functions: 100751
   Symbols:   3067
-  CStrings:  91638
+  CStrings:  91639
 
Functions:
~ sub_100161c1c : 1748 -> 1196
~ sub_10076b35c -> sub_10076b134 : 356 -> 712
~ sub_1008ebd0c -> sub_1008ebc48 : 52 -> 56
~ sub_1011008c4 -> sub_101100804 : 1036 -> 1076
~ sub_1011df2e0 -> sub_1011df248 : 96 -> 104
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B24sugATDcvbtXJu9cbYBmSVSZtR8xQbGWSGaDo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
+ "/AppleInternal/Library/BuildRoots/4~B24sugATDcvbtXJu9cbYBmSVSZtR8xQbGWSGaDo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
+ "/AppleInternal/Library/BuildRoots/4~B24sugATDcvbtXJu9cbYBmSVSZtR8xQbGWSGaDo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "/AppleInternal/Library/BuildRoots/4~B24sugATDcvbtXJu9cbYBmSVSZtR8xQbGWSGaDo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/4~B24sugATDcvbtXJu9cbYBmSVSZtR8xQbGWSGaDo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "21:49:53"
+ "22:09:17"
+ "Jun 11 2025"
+ "Jun 11 2025 21:52:36"
+ "checkLocationServicesStatusAndEnableExpensiveScansIfNecessary"
+ "{\"msg%{public}.0s\":\"Got a usable location\", \"location\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"location services was toggled on, and this service is authorized, doing an initial high-accuracy scan\", \"duration\":%{public}d}"
+ "{\"msg%{public}.0s\":\"location services was toggled on, but the service isn't authorized, so not scanning\", \"status\":%{public, location:CLAuthorizationStatus}lld}"
- "-[CLCountryTracker locationManager:didUpdateLocations:]"
- "/AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
- "/AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
- "/AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "/AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "19:03:16"
- "19:23:32"
- "Apr 27 2025"
- "Apr 27 2025 19:06:24"
- "Got a usable location <%{sensitive}+.8lf,%{sensitive}+.8lf>, acc %.2f, timestamp %.2f, lifespan %.2f, confidence %d"
- "checkLocationServicesStatus"

```
