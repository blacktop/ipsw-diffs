## TipsCore

> `/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore`

```diff

-813.0.0.0.0
-  __TEXT.__text: 0x9e014
-  __TEXT.__auth_stubs: 0x1ef0
-  __TEXT.__objc_methlist: 0x8360
-  __TEXT.__const: 0x1c08
-  __TEXT.__cstring: 0x5bc3
+816.0.0.0.0
+  __TEXT.__text: 0x9dfe0
+  __TEXT.__auth_stubs: 0x1ed0
+  __TEXT.__objc_methlist: 0x8368
+  __TEXT.__const: 0x1c18
+  __TEXT.__cstring: 0x5b93
   __TEXT.__oslogstring: 0x1222
-  __TEXT.__gcc_except_tab: 0x100c
+  __TEXT.__gcc_except_tab: 0xfe4
   __TEXT.__ustring: 0x118
-  __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__constg_swiftt: 0x1260
   __TEXT.__swift5_typeref: 0xd62
   __TEXT.__swift5_reflstr: 0xce2

   __TEXT.__swift5_assocty: 0x168
   __TEXT.__swift5_proto: 0xec
   __TEXT.__swift5_types: 0xc8
-  __TEXT.__swift5_capture: 0x5d0
+  __TEXT.__swift5_capture: 0x5e0
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift_as_entry: 0x5c
   __TEXT.__swift_as_ret: 0x4c
-  __TEXT.__unwind_info: 0x2f28
-  __TEXT.__eh_frame: 0x16d8
+  __TEXT.__unwind_info: 0x2f20
+  __TEXT.__eh_frame: 0x1700
   __TEXT.__objc_classname: 0xdbf
-  __TEXT.__objc_methname: 0xee9a
+  __TEXT.__objc_methname: 0xeeb7
   __TEXT.__objc_methtype: 0x189e
-  __TEXT.__objc_stubs: 0x9700
-  __DATA_CONST.__got: 0x8f0
-  __DATA_CONST.__const: 0x2058
+  __TEXT.__objc_stubs: 0x9720
+  __DATA_CONST.__got: 0x8f8
+  __DATA_CONST.__const: 0x2018
   __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a18
+  __DATA_CONST.__objc_selrefs: 0x3a28
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x318
   __DATA_CONST.__objc_arraydata: 0x118
-  __AUTH_CONST.__auth_got: 0xf88
-  __AUTH_CONST.__const: 0x2dd8
+  __AUTH_CONST.__auth_got: 0xf78
+  __AUTH_CONST.__const: 0x2e00
   __AUTH_CONST.__cfstring: 0x5340
   __AUTH_CONST.__objc_const: 0xda88
   __AUTH_CONST.__objc_intobj: 0x2b8

   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x2740
   __DATA_DIRTY.__data: 0x728
-  __DATA_DIRTY.__bss: 0x548
+  __DATA_DIRTY.__bss: 0x538
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /System/Library/PrivateFrameworks/PegasusAPI.framework/PegasusAPI
   - /System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 18F789BB-5857-33C7-8EFA-686ABF0E739B
-  Functions: 4757
-  Symbols:   9868
-  CStrings:  4961
+  UUID: 190A8F30-6C5D-3757-A086-F5A485421A35
+  Functions: 4756
+  Symbols:   9851
+  CStrings:  4959
 
Symbols:
+ +[NSLocale(TPSCoreAdditions) tps_userRegion]
+ _DMGetPreviousBuildVersion
+ _DMGetUserDataDisposition
+ _NSLocaleCountryCode
+ _objc_msgSend$currentLocale
- +[TPSUserTypeChecker _previousBuildVersion].cold.1
- +[TPSUserTypeChecker userTypeFromMigratorData].cold.1
- _DataMigrationLibrary
- _DataMigrationLibraryCore.frameworkLibrary
- ___DataMigrationLibraryCore_block_invoke
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___getDMGetPreviousBuildVersionSymbolLoc_block_invoke
- ___getDMGetUserDataDispositionSymbolLoc_block_invoke
- __sl_dlopen
- _abort_report_np
- _audit_stringDataMigration
- _dlerror
- _dlsym
- _getDMGetPreviousBuildVersionSymbolLoc.ptr
- _getDMGetUserDataDispositionSymbolLoc.ptr
CStrings:
+ "currentLocale"
+ "tps_userRegion"
- "DMGetPreviousBuildVersion"
- "DMGetUserDataDisposition"
- "softlink:r:path:/System/Library/PrivateFrameworks/DataMigration.framework/DataMigration"

```
