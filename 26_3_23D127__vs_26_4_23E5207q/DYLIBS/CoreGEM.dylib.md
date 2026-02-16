## CoreGEM.dylib

> `/System/Library/PrivateFrameworks/CoreGEM.framework/CoreGEM.dylib`

```diff

 30.0.0.0.0
-  __TEXT.__text: 0xf6324
-  __TEXT.__auth_stubs: 0xaf0
+  __TEXT.__text: 0xf610c
+  __TEXT.__auth_stubs: 0xb00
   __TEXT.__objc_methlist: 0x38
-  __TEXT.__const: 0xb9e0
-  __TEXT.__gcc_except_tab: 0x4610
-  __TEXT.__cstring: 0x6ca3
-  __TEXT.__oslogstring: 0x924b
-  __TEXT.__unwind_info: 0x4058
+  __TEXT.__const: 0xb808
+  __TEXT.__gcc_except_tab: 0x46cc
+  __TEXT.__cstring: 0x76bb
+  __TEXT.__oslogstring: 0x91de
+  __TEXT.__unwind_info: 0x40c8
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methname: 0xc6
   __TEXT.__objc_methtype: 0x34

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x588
+  __AUTH_CONST.__auth_got: 0x590
   __AUTH_CONST.__const: 0x9150
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x90

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 38715821-D522-3701-8805-FE8FF7758FA4
-  Functions: 4086
-  Symbols:   227
-  CStrings:  1441
+  UUID: EB03D72C-1CCE-34BC-BA9A-429E5032C250
+  Functions: 4098
+  Symbols:   228
+  CStrings:  1445
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _memchr
- _memset_pattern16
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHoMugBJAj4PPLd3pcebaW8500MrsJbLqiWQ7pk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoMugBJAj4PPLd3pcebaW8500MrsJbLqiWQ7pk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoMugBJAj4PPLd3pcebaW8500MrsJbLqiWQ7pk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoMugBJAj4PPLd3pcebaW8500MrsJbLqiWQ7pk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoMugBJAj4PPLd3pcebaW8500MrsJbLqiWQ7pk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/Library/Caches/com.apple.xbs/0EA3FE66-6EA5-4721-98E6-2E665A531617/TemporaryDirectory.wjwu1V/Sources/CoreGEM/Sources/Emergency/CplaneBridge.mm"
+ "/Library/Caches/com.apple.xbs/0EA3FE66-6EA5-4721-98E6-2E665A531617/TemporaryDirectory.wjwu1V/Sources/CoreGEM/Sources/Emergency/GnssConnectionManager.mm"
+ "/Library/Caches/com.apple.xbs/0EA3FE66-6EA5-4721-98E6-2E665A531617/TemporaryDirectory.wjwu1V/Sources/CoreGEM/Sources/Emergency/PosProtocol/cps/asn1/coder/bms/bms_small.c"
+ "/Library/Caches/com.apple.xbs/0EA3FE66-6EA5-4721-98E6-2E665A531617/TemporaryDirectory.wjwu1V/Sources/CoreGEM/Sources/Emergency/PosProtocol/cps/asn1/coder/er/per/per_base.c"
+ "/Library/Caches/com.apple.xbs/0EA3FE66-6EA5-4721-98E6-2E665A531617/TemporaryDirectory.wjwu1V/Sources/CoreGEM/Sources/Emergency/PosProtocol/cps/asn1/coder/er/per/per_content.c"
+ "/Library/Caches/com.apple.xbs/0EA3FE66-6EA5-4721-98E6-2E665A531617/TemporaryDirectory.wjwu1V/Sources/CoreGEM/Sources/Emergency/PosProtocol/cps/asn1/coder/mms/mms.c"
+ "/Library/Caches/com.apple.xbs/0EA3FE66-6EA5-4721-98E6-2E665A531617/TemporaryDirectory.wjwu1V/Sources/CoreGEM/Sources/Emergency/PosProtocol/cps/asn1/coder/vms/vms_base.c"
+ "/Library/Caches/com.apple.xbs/0EA3FE66-6EA5-4721-98E6-2E665A531617/TemporaryDirectory.wjwu1V/Sources/CoreGEM/Sources/Protobuf/Generated/CLPGemProtocolGpsd.pb.cc"
+ "/Library/Caches/com.apple.xbs/0EA3FE66-6EA5-4721-98E6-2E665A531617/TemporaryDirectory.wjwu1V/Sources/CoreGEM/Sources/Protobuf/Generated/CLPGnssEmergencyLppTypes.pb.cc"
+ "/Library/Caches/com.apple.xbs/0EA3FE66-6EA5-4721-98E6-2E665A531617/TemporaryDirectory.wjwu1V/Sources/CoreGEM/Sources/Protobuf/Generated/CLPGnssMeasApi.pb.cc"
+ "/Library/Caches/com.apple.xbs/0EA3FE66-6EA5-4721-98E6-2E665A531617/TemporaryDirectory.wjwu1V/Sources/CoreGEM/Sources/Protobuf/Generated/CLPGnssMeasAsyncTrackingInsight.pb.cc"
+ "/Library/Caches/com.apple.xbs/0EA3FE66-6EA5-4721-98E6-2E665A531617/TemporaryDirectory.wjwu1V/Sources/CoreGEM/Sources/Protobuf/Generated/CLPProactiveInertialOdometryData.pb.cc"
+ "/Library/Caches/com.apple.xbs/0EA3FE66-6EA5-4721-98E6-2E665A531617/TemporaryDirectory.wjwu1V/Sources/CoreGEM/Sources/Protobuf/Generated/GnssEmergencyTypes.pb.cc"
+ "/Library/Caches/com.apple.xbs/0EA3FE66-6EA5-4721-98E6-2E665A531617/TemporaryDirectory.wjwu1V/Sources/CoreGEM/Sources/Protobuf/Generated/GnssTypes.pb.cc"
+ "/Library/Caches/com.apple.xbs/0EA3FE66-6EA5-4721-98E6-2E665A531617/TemporaryDirectory.wjwu1V/Sources/CoreGEM/Sources/Protobuf/Generated/GpsdProtocol.pb.cc"
+ "/Library/Caches/com.apple.xbs/0EA3FE66-6EA5-4721-98E6-2E665A531617/TemporaryDirectory.wjwu1V/Sources/CoreGEM/Sources/Util/GpsdUtil.mm"
+ "\\/"
- "/AppleInternal/Library/BuildRoots/4~CG6XugDLSgv_x1gd8TtV8kzvDrJEZD_GMba-L8k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/Library/Caches/com.apple.xbs/Sources/CoreGEM/Sources/Emergency/CplaneBridge.mm"
- "/Library/Caches/com.apple.xbs/Sources/CoreGEM/Sources/Emergency/GnssConnectionManager.mm"
- "/Library/Caches/com.apple.xbs/Sources/CoreGEM/Sources/Emergency/PosProtocol/cps/asn1/coder/bms/bms_small.c"
- "/Library/Caches/com.apple.xbs/Sources/CoreGEM/Sources/Emergency/PosProtocol/cps/asn1/coder/er/per/per_base.c"
- "/Library/Caches/com.apple.xbs/Sources/CoreGEM/Sources/Emergency/PosProtocol/cps/asn1/coder/er/per/per_content.c"
- "/Library/Caches/com.apple.xbs/Sources/CoreGEM/Sources/Emergency/PosProtocol/cps/asn1/coder/mms/mms.c"
- "/Library/Caches/com.apple.xbs/Sources/CoreGEM/Sources/Emergency/PosProtocol/cps/asn1/coder/vms/vms_base.c"
- "/Library/Caches/com.apple.xbs/Sources/CoreGEM/Sources/Protobuf/Generated/CLPGemProtocolGpsd.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/CoreGEM/Sources/Protobuf/Generated/CLPGnssEmergencyLppTypes.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/CoreGEM/Sources/Protobuf/Generated/CLPGnssMeasApi.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/CoreGEM/Sources/Protobuf/Generated/CLPGnssMeasAsyncTrackingInsight.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/CoreGEM/Sources/Protobuf/Generated/CLPProactiveInertialOdometryData.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/CoreGEM/Sources/Protobuf/Generated/GnssEmergencyTypes.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/CoreGEM/Sources/Protobuf/Generated/GnssTypes.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/CoreGEM/Sources/Protobuf/Generated/GpsdProtocol.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/CoreGEM/Sources/Util/GpsdUtil.mm"
- "HeloEstimator, isGnssFixReadyForEarlyReturn,semiMajor,%hhu,semiMinor,%hhu,POS Error ellipse is too elongated"

```
