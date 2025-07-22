## GenerativeExperiencesRuntime

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime`

```diff

-205.1.0.0.0
-  __TEXT.__text: 0xbf200
-  __TEXT.__auth_stubs: 0x4680
+208.0.0.0.0
+  __TEXT.__text: 0xc0f24
+  __TEXT.__auth_stubs: 0x4710
   __TEXT.__objc_methlist: 0xacc
-  __TEXT.__const: 0x4e3c
-  __TEXT.__cstring: 0x4b45
-  __TEXT.__constg_swiftt: 0x1bc8
-  __TEXT.__swift5_typeref: 0x2b62
+  __TEXT.__const: 0x4e5c
+  __TEXT.__cstring: 0x4b95
+  __TEXT.__constg_swiftt: 0x1be4
+  __TEXT.__swift5_typeref: 0x2ba8
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_reflstr: 0xee6
-  __TEXT.__swift5_fieldmd: 0x1248
+  __TEXT.__swift5_fieldmd: 0x1258
   __TEXT.__swift5_assocty: 0x4b0
-  __TEXT.__oslogstring: 0x6b60
+  __TEXT.__oslogstring: 0x6d00
   __TEXT.__swift5_proto: 0x2fc
-  __TEXT.__swift5_types: 0x1e0
-  __TEXT.__swift_as_entry: 0x328
-  __TEXT.__swift_as_ret: 0x31c
+  __TEXT.__swift5_types: 0x1e4
+  __TEXT.__swift_as_entry: 0x320
+  __TEXT.__swift_as_ret: 0x314
   __TEXT.__swift5_capture: 0xfc8
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_protos: 0x48
-  __TEXT.__unwind_info: 0x2e70
-  __TEXT.__eh_frame: 0x8990
+  __TEXT.__unwind_info: 0x2eb8
+  __TEXT.__eh_frame: 0x8a38
   __TEXT.__objc_classname: 0x46
-  __TEXT.__objc_methname: 0x2245
+  __TEXT.__objc_methname: 0x2266
   __TEXT.__objc_methtype: 0xad
-  __DATA_CONST.__got: 0x11b8
+  __DATA_CONST.__got: 0x11f8
   __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x780
+  __DATA_CONST.__objc_selrefs: 0x790
   __DATA_CONST.__objc_protorefs: 0x90
-  __AUTH_CONST.__auth_got: 0x2340
-  __AUTH_CONST.__const: 0x3da8
+  __AUTH_CONST.__auth_got: 0x2388
+  __AUTH_CONST.__const: 0x3dc8
   __AUTH_CONST.__objc_const: 0x2f78
   __AUTH.__objc_data: 0x4e8
-  __AUTH.__data: 0xa50
-  __DATA.__data: 0xe28
+  __AUTH.__data: 0xb80
+  __DATA.__data: 0xe98
   __DATA.__bss: 0x3960
-  __DATA.__common: 0x98
+  __DATA.__common: 0xc8
   __DATA_DIRTY.__objc_data: 0x5a0
-  __DATA_DIRTY.__data: 0x2418
+  __DATA_DIRTY.__data: 0x22e8
   __DATA_DIRTY.__bss: 0x1a80
-  __DATA_DIRTY.__common: 0x228
+  __DATA_DIRTY.__common: 0x1f8
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog
   - /System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices
   - /System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport

   - /System/Library/PrivateFrameworks/TextComposer.framework/TextComposer
   - /System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration
   - /System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore
+  - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
   - /System/Library/PrivateFrameworks/VectorSearch.framework/VectorSearch
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A86832AF-D499-3178-8BC3-0621CB4684A7
-  Functions: 4124
-  Symbols:   241
-  CStrings:  993
+  UUID: 0E19328E-B341-32BF-B344-FA43A5B55D61
+  Functions: 4149
+  Symbols:   244
+  CStrings:  1005
 
Symbols:
+ _MKBDeviceUnlockedSinceBoot
+ _OBJC_CLASS_$_UAFAssetSetManager
+ _os_variant_has_internal_diagnostics
CStrings:
+ "%s: %s"
+ "Asset delivery not ready, applying strict readiness rules"
+ "AvailabilityStore.set(latestNotification): %s = %s"
+ "Can't encode latestNotification with error: %@"
+ "GenerativeModels"
+ "MKBDeviceUnlockedSinceBoot() -> %d"
+ "No change to availability or eligibility, not sending notification"
+ "No change to availability, ticket status, or eligibility change. Not invoking reportCurrentAvailabilityState"
+ "Skip updating use cases whose assets not ready or out of storage since it's not modelcatalog notification or boot task"
+ "Warning: readiness unable to fully update before first unlock"
+ "Warning: vmHostAvailable, skipping asset readiness checks"
+ "_TtCO28GenerativeExperiencesRuntime27AvailabilityBackgroundTasks26PostBootUpdateAvailability"
+ "_TtCO28GenerativeExperiencesRuntime27AvailabilityBackgroundTasks5Daily"
+ "assetDeliveryReady"
+ "assetDeliveryReady: %{bool}d"
+ "com.apple.GenerativeFunctions.PeriodicTasks.AvailabilityUpdateTask.Boot"
+ "externalIntelligenceIntegrations"
+ "sharedManager"
- "No availability cache change. Bail out sending notification"
- "No availability cache, ticket status, or eligibility change. Not invoking reportCurrentAvailabilityState"
- "Skip updating use cases whose assets not ready or out of storage since it's not modelcatalog notification"
- "_TtCO28GenerativeExperiencesRuntime27AvailabilityBackgroundTasks12Availability"
- "_TtCO28GenerativeExperiencesRuntime27AvailabilityBackgroundTasks26PostBootReportAvailability"
- "com.apple.GenerativeFunctions.PeriodicTasks.ReportAvailabilityTask.Boot"

```
