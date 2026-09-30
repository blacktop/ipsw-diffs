## CoreNavigation

> `/System/Library/PrivateFrameworks/CoreNavigation.framework/CoreNavigation`

```diff

-364.0.1.0.0
-  __TEXT.__text: 0x302988
+364.0.2.0.0
+  __TEXT.__text: 0x303798
   __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__const: 0x4caef
-  __TEXT.__gcc_except_tab: 0x152fc
-  __TEXT.__cstring: 0x3192d
+  __TEXT.__const: 0x4cb2f
+  __TEXT.__gcc_except_tab: 0x15300
+  __TEXT.__cstring: 0x31c8f
   __TEXT.__oslogstring: 0xe
-  __TEXT.__unwind_info: 0xc868
+  __TEXT.__unwind_info: 0xc880
   __DATA_CONST.__got: 0x2e0
   __DATA_CONST.__const: 0x770
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 598B8B61-72F1-3B8F-AC55-AF87E5F226EB
-  Functions: 13634
-  Symbols:   11469
-  CStrings:  3459
+  UUID: D874E2DA-1812-33EE-BA9B-4B228EA1D26C
+  Functions: 13638
+  Symbols:   11471
+  CStrings:  3468
 
Symbols:
+ __ZN5raven15RavenSupervisor15RaiseEventsFromERKN14CoreNavigation3CLP8LogEntry11PrivateData19MotionStateMediatorE
+ __ZN5raven36ConvertProtobufToFitnessSessionEventERKN14CoreNavigation3CLP8LogEntry11PrivateData19MotionStateMediatorERNS_19FitnessSessionEventE
+ __ZN5raven44ConvertRavenFitnessSessionActivityToProtobufERKNS_27RavenFitnessSessionActivityE
- __ZN5raven40ConvertRavenFitnessSessionEnumToProtobufERKNS_19RavenFitnessSession23RavenFitnessSessionEnumE
CStrings:
+ "#rwo,integrity_estimator,event_time,%.6f,activity_type,%d,state,%d,source,%d,start_time,%.6f,applicability_time,%.6f,end_time,%.6f"
+ "#rwo,mediator,event_type,%d,workout_type,%d,event_time,%.6f,applicability_time,%.6f"
+ "#rwo,observer,activity_type,%d,start_time,%.6f,applicability_time,%.6f"
+ "/AppleInternal/Library/BuildRoots/4~B-qjugCNCPx5bOd3xswqP3T9claLgaAsDOzhOyw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/boost/geometry/algorithms/centroid.hpp"
+ "/AppleInternal/Library/BuildRoots/4~B-qjugCNCPx5bOd3xswqP3T9claLgaAsDOzhOyw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/boost/rational.hpp"
+ "/AppleInternal/Library/BuildRoots/4~B-qjugCNCPx5bOd3xswqP3T9claLgaAsDOzhOyw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/4~B-qjugCNCPx5bOd3xswqP3T9claLgaAsDOzhOyw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "debug_allow_motion_state_mediator_notifications"
+ "t,%.3lf,IntegrityEstimatorAO: Blocking MotionStateMediator-originated FitnessSessionEvent on Watch platform"
+ "t,%.3lf,IntegrityEstimatorAO: Caching remote FitnessSessionEvent while local active, event=%d"
+ "t,%.3lf,IntegrityEstimatorAO: Local ended but remote still active, blocking local end-event and sending cached remote FitnessSessionEvent"
+ "t,%.3lf,IntegrityEstimatorAO: Passing through remote FitnessSessionEvent (no active local), event=%d"
+ "t,%.3lf,IntegrityEstimatorAO: Processing MotionStateMediator FitnessSessionEvent, event=%d"
- "/AppleInternal/Library/BuildRoots/4~B9I6ugBCBEz96N9aNlMPp4ZJhTlNYqFI-wu8Pl4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/boost/geometry/algorithms/centroid.hpp"
- "/AppleInternal/Library/BuildRoots/4~B9I6ugBCBEz96N9aNlMPp4ZJhTlNYqFI-wu8Pl4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/boost/rational.hpp"
- "/AppleInternal/Library/BuildRoots/4~B9I6ugBCBEz96N9aNlMPp4ZJhTlNYqFI-wu8Pl4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/4~B9I6ugBCBEz96N9aNlMPp4ZJhTlNYqFI-wu8Pl4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"

```
