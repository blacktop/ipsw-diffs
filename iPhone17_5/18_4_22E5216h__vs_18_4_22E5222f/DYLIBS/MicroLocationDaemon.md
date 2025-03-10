## MicroLocationDaemon

> `/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`

```diff

-27.0.28.0.5
-  __TEXT.__text: 0x1b6938
+27.0.28.0.6
+  __TEXT.__text: 0x1b6f58
   __TEXT.__auth_stubs: 0x1a00
-  __TEXT.__objc_methlist: 0x4df0
-  __TEXT.__gcc_except_tab: 0x213b0
-  __TEXT.__cstring: 0xc01a
-  __TEXT.__const: 0x966e
-  __TEXT.__oslogstring: 0x2645e
+  __TEXT.__objc_methlist: 0x4df8
+  __TEXT.__gcc_except_tab: 0x21484
+  __TEXT.__cstring: 0xc05a
+  __TEXT.__const: 0x967e
+  __TEXT.__oslogstring: 0x2655e
   __TEXT.__constg_swiftt: 0xec
   __TEXT.__swift5_typeref: 0xad
   __TEXT.__swift5_fieldmd: 0x30
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0xa028
+  __TEXT.__unwind_info: 0xa058
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0xbed
-  __TEXT.__objc_methname: 0xc000
-  __TEXT.__objc_methtype: 0xaecf
-  __TEXT.__objc_stubs: 0x9f20
-  __DATA_CONST.__got: 0x600
+  __TEXT.__objc_methname: 0xc069
+  __TEXT.__objc_methtype: 0xaff0
+  __TEXT.__objc_stubs: 0x9fc0
+  __DATA_CONST.__got: 0x608
   __DATA_CONST.__const: 0x1478
   __DATA_CONST.__objc_classlist: 0x3a8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d00
+  __DATA_CONST.__objc_selrefs: 0x2d28
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x440
   __AUTH_CONST.__auth_got: 0xd18
   __AUTH_CONST.__auth_ptr: 0x70
   __AUTH_CONST.__const: 0x8c78
-  __AUTH_CONST.__cfstring: 0x4500
+  __AUTH_CONST.__cfstring: 0x4540
   __AUTH_CONST.__objc_const: 0x8c88
   __AUTH_CONST.__objc_doubleobj: 0x3d0
   __AUTH_CONST.__objc_intobj: 0x1350

   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
+  - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet
   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7503
-  Symbols:   9936
-  CStrings:  5718
+  Functions: 7508
+  Symbols:   9944
+  CStrings:  5728
 
Symbols:
+ _OBJC_CLASS_$_BMSQLDatabase
CStrings:
+ "/AppleInternal/Library/BuildRoots/fe0942ab-f69f-11ef-83ba-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
+ "/AppleInternal/Library/BuildRoots/fe0942ab-f69f-11ef-83ba-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "/AppleInternal/Library/BuildRoots/fe0942ab-f69f-11ef-83ba-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "3.0.46"
+ "Enabled state: microlocations defaults enabled: %{public}d; location services enabled: %{public}d; significant locations enabled: %{public}d; platform supported %{public}d; LowPowerMode %{public}d; AirplaneMode %{public}d; buddyComplete %{public}d; LimitedMiloActiveTime %{public}d; overall enabled: %{public}d"
+ "MiloLimitedUsageIndicators"
+ "SELECT * FROM \"HomeKit.Client.AccessoryControl\""
+ "executeQuery:"
+ "fetchRecordingLabelsForServiceUuid:limit:"
+ "initWithUseCase:"
+ "isLimitedMiloActiveTime: isLimitedMiloUsagePlatform: %{public}d; corriander: %{public}d; isHomeKitBeingUsed: %{public}d; hasFocusModeLabels: %{public}d;"
+ "isLimitedMiloUsagePlatform"
+ "next"
+ "{\"msg%{public}.0s\":\"#LOI Manager, got location update to enable custom geofence\", \"latitude\":\"%{sensitive}7f\", \"longitude\":\"%{sensitive}7f\"}"
+ "{\"msg%{public}.0s\":\"#LOI Manager, got location update\", \"latitude\":\"%{sensitive}7f\", \"longitude\":\"%{sensitive}7f\"}"
+ "{\"msg%{public}.0s\":\"LOI Bridge, requested geofence at location\", \"latitude\":\"%{sensitive}7f\", \"longitude\":\"%{sensitive}7f\"}"
+ "{\"msg%{public}.0s\":\"Warning: BM Query returned error\"}"
+ "{\"msg%{public}.0s\":\"fetchPlaceInferenceAtCurrentLocation, received Place Inference\", \"PI\":%{sensitive, location:escape_only}@}"
+ "{vector<CLMicroLocationRecordingLabelsTable::Entry, std::allocator<CLMicroLocationRecordingLabelsTable::Entry>>=^{Entry}^{Entry}{__compressed_pair<CLMicroLocationRecordingLabelsTable::Entry *, std::allocator<CLMicroLocationRecordingLabelsTable::Entry>>=^{Entry}}}28@0:8r^{uuid=[16C]}16I24"
- "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
- "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "3.0.45"
- "Enabled state: microlocations defaults enabled: %{public}d; location services enabled: %{public}d; significant locations enabled: %{public}d; platform supported %{public}d; LowPowerMode %{public}d; AirplaneMode %{public}d; buddyComplete %{public}d; overall enabled: %{public}d"
- "{\"msg%{public}.0s\":\"#LOI Manager, got location update to enable custom geofence\", \"latitude\":\"%{private}7f\", \"longitude\":\"%{private}7f\"}"
- "{\"msg%{public}.0s\":\"#LOI Manager, got location update\", \"latitude\":\"%{private}7f\", \"longitude\":\"%{private}7f\"}"
- "{\"msg%{public}.0s\":\"LOI Bridge, requested geofence at location\", \"latitude\":\"%{private}7f\", \"longitude\":\"%{private}7f\"}"
- "{\"msg%{public}.0s\":\"fetchPlaceInferenceAtCurrentLocation, received Place Inference\", \"PI\":%{private, location:escape_only}@}"

```
