## HomeEnergyDaemon

> `/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon`

```diff

-332.0.2.0.0
-  __TEXT.__text: 0x1df344
-  __TEXT.__auth_stubs: 0x3c70
+341.0.0.0.0
+  __TEXT.__text: 0x1df870
+  __TEXT.__auth_stubs: 0x3c60
   __TEXT.__objc_methlist: 0xb38
-  __TEXT.__const: 0x45b8
-  __TEXT.__cstring: 0x672f
+  __TEXT.__const: 0x45c8
+  __TEXT.__cstring: 0x686f
   __TEXT.__constg_swiftt: 0x2614
   __TEXT.__swift5_typeref: 0x17aa
-  __TEXT.__swift5_reflstr: 0x1874
-  __TEXT.__swift5_fieldmd: 0x1674
+  __TEXT.__swift5_reflstr: 0x18b4
+  __TEXT.__swift5_fieldmd: 0x168c
   __TEXT.__oslogstring: 0x999b
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_assocty: 0x1b0
   __TEXT.__swift5_proto: 0x190
   __TEXT.__swift5_types: 0x1a4
-  __TEXT.__swift_as_entry: 0x4f4
-  __TEXT.__swift_as_ret: 0x744
-  __TEXT.__swift5_capture: 0x1e90
+  __TEXT.__swift_as_entry: 0x4f0
+  __TEXT.__swift_as_ret: 0x740
+  __TEXT.__swift5_capture: 0x1ea0
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x5450
-  __TEXT.__eh_frame: 0x134e0
+  __TEXT.__unwind_info: 0x5448
+  __TEXT.__eh_frame: 0x13490
   __TEXT.__objc_classname: 0xbc
   __TEXT.__objc_methname: 0x3687
   __TEXT.__objc_methtype: 0x687
   __TEXT.__objc_stubs: 0xc0
   __DATA_CONST.__got: 0xac8
-  __DATA_CONST.__const: 0xd8
+  __DATA_CONST.__const: 0xb8
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xf48
   __DATA_CONST.__objc_protorefs: 0x50
-  __AUTH_CONST.__auth_got: 0x1e40
-  __AUTH_CONST.__const: 0x5d50
+  __AUTH_CONST.__auth_got: 0x1e38
+  __AUTH_CONST.__const: 0x5d80
   __AUTH_CONST.__objc_const: 0x51c0
   __AUTH.__objc_data: 0x220
   __AUTH.__data: 0x10b8
-  __DATA.__data: 0xb78
+  __DATA.__data: 0xb88
   __DATA.__common: 0xa0
   __DATA.__bss: 0x2800
   __DATA_DIRTY.__objc_data: 0x468
-  __DATA_DIRTY.__data: 0x32f0
+  __DATA_DIRTY.__data: 0x32e0
   __DATA_DIRTY.__bss: 0x780
   __DATA_DIRTY.__common: 0x190
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMapKit.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A6CF74E3-F6B0-3789-A01D-E5ADBF7E95DD
-  Functions: 4279
-  Symbols:   1752
-  CStrings:  1890
+  UUID: ED4D1E97-104E-34BA-8BB2-96638E4D557F
+  Functions: 4278
+  Symbols:   1744
+  CStrings:  1894
 
Symbols:
+ _block_copy_helper.108
+ _block_copy_helper.118
+ _block_copy_helper.125
+ _block_copy_helper.135
+ _block_descriptor.110
+ _block_descriptor.120
+ _block_descriptor.127
+ _block_descriptor.137
+ _block_destroy_helper.109
+ _block_destroy_helper.119
+ _block_destroy_helper.126
+ _block_destroy_helper.136
+ _symbolic _____Sg 12HomeServices18HSGuidanceForecastV
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_HomeEnergyDaemon
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_HomeEnergyDaemon
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_HomeEnergyDaemon
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_HomeEnergyDaemon
- _block_copy_helper.110
- _block_copy_helper.120
- _block_copy_helper.127
- _block_copy_helper.137
- _block_descriptor.112
- _block_descriptor.122
- _block_descriptor.129
- _block_descriptor.139
- _block_destroy_helper.111
- _block_destroy_helper.121
- _block_destroy_helper.128
- _block_destroy_helper.138
- _objectdestroy.108Tm
- _symbolic _____Sg 12HomeServices10HSGuidanceV
CStrings:
+ "Failed to share AMI token"
+ "HomeServices failed to fetch historical guidance"
+ "addEnergySite(siteID:metadata:zoneName:context:tokenUpdate:)"
+ "gridID = %@ AND guidanceType = %d AND ratePlan = %@ AND utilityID = %@ AND timeZone = %@ AND version = %d"
+ "gridID = %@ AND guidanceType = %d AND ratePlan = %@ AND utilityID = %@ AND timeZone = %@ AND version = 2"
- "addEnergySite(siteID:metadata:zoneName:context:)"

```
