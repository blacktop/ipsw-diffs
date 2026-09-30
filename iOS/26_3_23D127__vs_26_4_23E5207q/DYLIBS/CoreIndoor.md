## CoreIndoor

> `/System/Library/PrivateFrameworks/CoreIndoor.framework/CoreIndoor`

```diff

-798.0.0.0.0
-  __TEXT.__text: 0x600e4
-  __TEXT.__auth_stubs: 0xd70
+801.0.0.0.0
+  __TEXT.__text: 0x5ff4c
+  __TEXT.__auth_stubs: 0xd20
   __TEXT.__init_offsets: 0x44
   __TEXT.__objc_methlist: 0x14cc
-  __TEXT.__gcc_except_tab: 0x4790
-  __TEXT.__cstring: 0x2fae
+  __TEXT.__gcc_except_tab: 0x47a0
+  __TEXT.__cstring: 0x36e5
   __TEXT.__const: 0x46aa
   __TEXT.__oslogstring: 0x2dda
-  __TEXT.__unwind_info: 0x2310
+  __TEXT.__unwind_info: 0x23c0
   __TEXT.__objc_classname: 0x2ab
   __TEXT.__objc_methname: 0x3b16
   __TEXT.__objc_methtype: 0x23ee

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x6c8
+  __AUTH_CONST.__auth_got: 0x6a0
   __AUTH_CONST.__const: 0x3998
   __AUTH_CONST.__cfstring: 0x12e0
   __AUTH_CONST.__objc_const: 0x2548

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 4C50A7AD-FFAB-362A-AB41-30B940C729BC
-  Functions: 1668
-  Symbols:   350
-  CStrings:  1286
+  UUID: A5C2DBC0-9758-33A9-8A08-73CCFF549C00
+  Functions: 1697
+  Symbols:   345
+  CStrings:  1290
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x4
- _objc_retain_x8
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHnfugBQfFiUsKTOUfg69qHXhLEu9BfmOtFN7Ag/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHpcugDBRunHGqZJR3kwuzDRHvXceFIXJiGAKSs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHpcugDBRunHGqZJR3kwuzDRHvXceFIXJiGAKSs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CHpcugDBRunHGqZJR3kwuzDRHvXceFIXJiGAKSs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CHpcugDBRunHGqZJR3kwuzDRHvXceFIXJiGAKSs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/exception/detail/exception_ptr.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CHpcugDBRunHGqZJR3kwuzDRHvXceFIXJiGAKSs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
+ "/Library/Caches/com.apple.xbs/3A0E77E4-7166-4848-AB0B-6AC55C8BF48A/TemporaryDirectory.DqYScS/Sources/purpleslam/daemon/Framework/AvailabilityTile.mm"
+ "/Library/Caches/com.apple.xbs/3A0E77E4-7166-4848-AB0B-6AC55C8BF48A/TemporaryDirectory.DqYScS/Sources/purpleslam/daemon/Framework/CLAvailabilityTileParser.mm"
+ "/Library/Caches/com.apple.xbs/3A0E77E4-7166-4848-AB0B-6AC55C8BF48A/TemporaryDirectory.DqYScS/Sources/purpleslam/daemon/Framework/CLAvailableVenuesStateMachine.mm"
+ "/Library/Caches/com.apple.xbs/3A0E77E4-7166-4848-AB0B-6AC55C8BF48A/TemporaryDirectory.DqYScS/Sources/purpleslam/daemon/Framework/utils/avl_tile_utils.cpp"
+ "/Library/Caches/com.apple.xbs/3A0E77E4-7166-4848-AB0B-6AC55C8BF48A/TemporaryDirectory.DqYScS/Sources/purpleslam/protobuf/gen/coordinates.pb.cc"
+ "/Library/Caches/com.apple.xbs/3A0E77E4-7166-4848-AB0B-6AC55C8BF48A/TemporaryDirectory.DqYScS/Sources/purpleslam/protobuf/gen/indoor_availability.pb.cc"
+ "/Library/Caches/com.apple.xbs/3A0E77E4-7166-4848-AB0B-6AC55C8BF48A/TemporaryDirectory.DqYScS/Sources/purpleslam/protobuf/gen/locationd_parameters.pb.cc"
+ "/Library/Caches/com.apple.xbs/3A0E77E4-7166-4848-AB0B-6AC55C8BF48A/TemporaryDirectory.DqYScS/Sources/purpleslam/protobuf/gen/math.pb.cc"
+ "/Library/Caches/com.apple.xbs/3A0E77E4-7166-4848-AB0B-6AC55C8BF48A/TemporaryDirectory.DqYScS/Sources/purpleslam/protobuf/gen/parameters.pb.cc"
+ "/Library/Caches/com.apple.xbs/3A0E77E4-7166-4848-AB0B-6AC55C8BF48A/TemporaryDirectory.DqYScS/Sources/purpleslam/protobuf/gen/venue.pb.cc"
- "/AppleInternal/Library/BuildRoots/4~CG66ugCkQ4mv-ugmTxypZFCEIreh2pbqOT4wWJ8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/boost/exception/detail/exception_ptr.hpp"
- "/AppleInternal/Library/BuildRoots/4~CG66ugCkQ4mv-ugmTxypZFCEIreh2pbqOT4wWJ8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
- "/Library/Caches/com.apple.xbs/Sources/purpleslam/daemon/Framework/AvailabilityTile.mm"
- "/Library/Caches/com.apple.xbs/Sources/purpleslam/daemon/Framework/CLAvailabilityTileParser.mm"
- "/Library/Caches/com.apple.xbs/Sources/purpleslam/daemon/Framework/CLAvailableVenuesStateMachine.mm"
- "/Library/Caches/com.apple.xbs/Sources/purpleslam/daemon/Framework/utils/avl_tile_utils.cpp"
- "/Library/Caches/com.apple.xbs/Sources/purpleslam/protobuf/gen/coordinates.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/purpleslam/protobuf/gen/indoor_availability.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/purpleslam/protobuf/gen/locationd_parameters.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/purpleslam/protobuf/gen/math.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/purpleslam/protobuf/gen/parameters.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/purpleslam/protobuf/gen/venue.pb.cc"

```
