## Logging

> `/System/Library/Trace/Providers/Logging.bundle/Logging`

```diff

-84.100.20.0.0
-  __TEXT.__text: 0x51d0
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_methlist: 0x170
-  __TEXT.__const: 0x596
-  __TEXT.__cstring: 0x70c
-  __TEXT.__swift5_typeref: 0x1e7
+130.0.0.0.0
+  __TEXT.__text: 0x8b88
+  __TEXT.__auth_stubs: 0x930
+  __TEXT.__objc_methlist: 0x380
+  __TEXT.__const: 0x7ce
+  __TEXT.__cstring: 0xd3b
+  __TEXT.__swift5_typeref: 0x2a4
   __TEXT.__swift5_capture: 0x88
-  __TEXT.__objc_methname: 0x331
-  __TEXT.__constg_swiftt: 0xe0
+  __TEXT.__objc_methname: 0x3dd
+  __TEXT.__constg_swiftt: 0x268
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_reflstr: 0x1f5
-  __TEXT.__swift5_fieldmd: 0x14c
+  __TEXT.__swift5_reflstr: 0x280
+  __TEXT.__swift5_fieldmd: 0x264
   __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__swift5_proto: 0x30
-  __TEXT.__swift5_types: 0x14
-  __TEXT.__objc_classname: 0x20
-  __TEXT.__objc_methtype: 0x17a
-  __TEXT.__unwind_info: 0x1d0
-  __TEXT.__eh_frame: 0xe8
-  __DATA_CONST.__auth_got: 0x3b8
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__auth_ptr: 0x1b0
-  __DATA_CONST.__const: 0x488
-  __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x20
+  __TEXT.__swift5_proto: 0x50
+  __TEXT.__swift5_types: 0x2c
+  __TEXT.__objc_classname: 0x4a
+  __TEXT.__objc_methtype: 0x2ad
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__unwind_info: 0x2e8
+  __TEXT.__eh_frame: 0x188
+  __DATA_CONST.__auth_got: 0x498
+  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__auth_ptr: 0x1d8
+  __DATA_CONST.__const: 0x5a0
+  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA.__objc_const: 0x1f0
-  __DATA.__objc_selrefs: 0x130
-  __DATA.__objc_data: 0xf8
-  __DATA.__data: 0x218
-  __DATA.__bss: 0x650
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA.__objc_const: 0x648
+  __DATA.__objc_selrefs: 0x168
+  __DATA.__objc_data: 0x588
+  __DATA.__data: 0x3d0
+  __DATA.__common: 0x8
+  __DATA.__bss: 0x750
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport

   - /usr/lib/swift/libswiftSystem.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 2D1611AA-75E9-3F45-82ED-79AA8077FD8D
-  Functions: 160
-  Symbols:   108
-  CStrings:  106
+  UUID: 9DBC85E1-3CB4-31C7-BB04-ED2671C50DC3
+  Functions: 279
+  Symbols:   118
+  CStrings:  160
 
Symbols:
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_stdlib_reportUnimplementedInitializer
+ _bzero
+ _ktrace_machine_sw_platform
+ _malloc_size
+ _memmove
+ _objc_release_x26
+ _objc_release_x27
+ _objc_retain_x26
+ _objc_retain_x27
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_conformsToProtocol2
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_setDeallocating
+ _swift_unknownObjectRelease_n
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _swift_cvw_initStructMetadataWithLayoutString
- _swift_cvw_initWithTake
- _swift_getEnumTagSinglePayloadGeneric
- _swift_storeEnumTagSinglePayloadGeneric
CStrings:
+ "@\"NSDictionary\"24@0:8^{ktrace_machine=}16"
+ "@\"NSString\"16@0:8"
+ "@24@0:8^{ktrace_machine=}16"
+ "B16@0:8"
+ "B48@0:8^v16@24@32^@40"
+ "B48@0:8^{ktrace_file=}16@\"NSDate\"24@\"NSDate\"32^@40"
+ "B48@0:8^{ktrace_file=}16@24@32^@40"
+ "B56@0:8@\"<KTProviderLogger>\"16^{ktrace_machine=}24@\"NSDictionary\"32@\"NSArray\"40^@48"
+ "B56@0:8@16^v24@32@40^@48"
+ "B56@0:8@16^{ktrace_machine=}24@32@40^@48"
+ "Collection options conflict: "
+ "InteractionTracking"
+ "KTPassiveDataCategory"
+ "KTPassiveDataSource"
+ "Logging.AppLaunchDataCategory"
+ "Logging.HangsDataCategory"
+ "Logging.InteractionTrackingDataCategory"
+ "Logging.MetalFramePacingDataCategory"
+ "Logging.PerfPowerMetricsDataCategory"
+ "Logging.ScrollingDataCategory"
+ "MetalFramePacing"
+ "PerfPowerMetrics"
+ "Requested data categories require os_signpost but options disable os_signpost colection"
+ "Unexpected data category type: "
+ "_TtC7Logging17HangsDataCategory"
+ "_TtC7Logging21AppLaunchDataCategory"
+ "_TtC7Logging21ScrollingDataCategory"
+ "_TtC7Logging28MetalFramePacingDataCategory"
+ "_TtC7Logging28PerfPowerMetricsDataCategory"
+ "_TtC7Logging31InteractionTrackingDataCategory"
+ "availableDataCategories:"
+ "collectToFile:startDate:endDate:error:"
+ "com.apple.AppKit"
+ "com.apple.SkyLight"
+ "com.apple.coreanimation"
+ "configureWithLogger:machine:options:dataCategories:error:"
+ "dataCategoryName"
+ "dataSourceName"
+ "hitches"
+ "init()"
+ "init:"
+ "isAvailable"
+ "machine"
+ "performance_instrumentation"
+ "requiresSignpost"
+ "resolvedFilterPredicateString"
+ "subsystem == \"com.apple.AppKit\" AND category == \"ScrollView\""
+ "subsystem == \"com.apple.Foundation\" AND category == \"NSProcessInfoInteractionTracking\""
+ "subsystem == \"com.apple.FramePacing\""
+ "subsystem == \"com.apple.PerfPowerMetricMonitor\" AND category == \"PowerMetrics\""
+ "subsystem == \"com.apple.UIKit\" AND category == \"ScrollView\""
+ "subsystem == \"com.apple.app_launch_measurement\" AND category == \"ApplicationLaunch\""
+ "subsystem == \"com.apple.hangtracer\" AND category == \"always_on_hang\""

```
