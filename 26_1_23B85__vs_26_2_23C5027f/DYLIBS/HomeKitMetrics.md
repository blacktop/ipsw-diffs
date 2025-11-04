## HomeKitMetrics

> `/System/Library/PrivateFrameworks/HomeKitMetrics.framework/HomeKitMetrics`

```diff

-1371.2.9.0.0
-  __TEXT.__text: 0x69050
-  __TEXT.__auth_stubs: 0x1c70
-  __TEXT.__objc_methlist: 0x1cc4
+1388.3.1.0.2
+  __TEXT.__text: 0x6f130
+  __TEXT.__auth_stubs: 0x1ce0
+  __TEXT.__objc_methlist: 0x1c0c
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__const: 0x3ed0
-  __TEXT.__cstring: 0x210f
-  __TEXT.__constg_swiftt: 0x209c
-  __TEXT.__swift5_typeref: 0x1a6a
-  __TEXT.__swift5_reflstr: 0x14dc
-  __TEXT.__swift5_fieldmd: 0x1560
+  __TEXT.__const: 0x4070
+  __TEXT.__cstring: 0x212f
+  __TEXT.__swift5_typeref: 0x1b46
+  __TEXT.__swift5_capture: 0x420
+  __TEXT.__oslogstring: 0x152c
+  __TEXT.__constg_swiftt: 0x2158
+  __TEXT.__swift5_reflstr: 0x1588
+  __TEXT.__swift5_fieldmd: 0x1634
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x4f8
-  __TEXT.__oslogstring: 0x14ae
-  __TEXT.__swift5_proto: 0x218
-  __TEXT.__swift5_types: 0x1a0
-  __TEXT.__swift5_protos: 0x4c
-  __TEXT.__swift5_capture: 0x3f8
-  __TEXT.__swift_as_entry: 0x7c
-  __TEXT.__swift_as_ret: 0x58
+  __TEXT.__swift5_proto: 0x21c
+  __TEXT.__swift5_types: 0x1b0
+  __TEXT.__swift_as_entry: 0x80
+  __TEXT.__swift_as_ret: 0x5c
+  __TEXT.__swift5_protos: 0x50
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x278
-  __TEXT.__unwind_info: 0x1cb8
-  __TEXT.__eh_frame: 0x28c0
-  __TEXT.__objc_classname: 0x5d0
-  __TEXT.__objc_methname: 0x38a2
-  __TEXT.__objc_methtype: 0xcbf
-  __TEXT.__objc_stubs: 0x22a0
-  __DATA_CONST.__got: 0x580
-  __DATA_CONST.__const: 0x418
-  __DATA_CONST.__objc_classlist: 0x250
+  __TEXT.__gcc_except_tab: 0x288
+  __TEXT.__unwind_info: 0x1dd8
+  __TEXT.__eh_frame: 0x2a68
+  __TEXT.__objc_classname: 0x5b2
+  __TEXT.__objc_methname: 0x384b
+  __TEXT.__objc_methtype: 0xc50
+  __TEXT.__objc_stubs: 0x2280
+  __DATA_CONST.__got: 0x5a0
+  __DATA_CONST.__const: 0x438
+  __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf68
+  __DATA_CONST.__objc_selrefs: 0xf40
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0xf0
-  __AUTH_CONST.__auth_got: 0xe48
-  __AUTH_CONST.__const: 0x2fc8
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __AUTH_CONST.__auth_got: 0xe80
+  __AUTH_CONST.__const: 0x3080
   __AUTH_CONST.__cfstring: 0x8a0
-  __AUTH_CONST.__objc_const: 0x5bb0
-  __AUTH_CONST.__objc_floatobj: 0x20
+  __AUTH_CONST.__objc_const: 0x5b60
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0xd38
-  __AUTH.__data: 0xab0
-  __DATA.__objc_ivar: 0x1cc
-  __DATA.__data: 0x18a0
-  __DATA.__bss: 0x2598
+  __AUTH_CONST.__objc_floatobj: 0x20
+  __AUTH.__objc_data: 0xd00
+  __AUTH.__data: 0xc90
+  __DATA.__objc_ivar: 0x1c8
+  __DATA.__data: 0x1978
+  __DATA.__bss: 0x25b8
   __DATA.__common: 0x40
-  __DATA_DIRTY.__objc_data: 0x1118
-  __DATA_DIRTY.__data: 0x1638
-  __DATA_DIRTY.__bss: 0x10d0
+  __DATA_DIRTY.__objc_data: 0x10c8
+  __DATA_DIRTY.__data: 0x1608
+  __DATA_DIRTY.__bss: 0x10a0
   __DATA_DIRTY.__common: 0x48
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/CloudTelemetry.framework/CloudTelemetry
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation
   - /System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AC1150BA-74D2-31E2-B8B4-805202432160
-  Functions: 2457
-  Symbols:   2931
-  CStrings:  1391
+  UUID: 5D93FB62-1DF5-3CDD-9EE6-56362A90150C
+  Functions: 2528
+  Symbols:   2936
+  CStrings:  1368
 
Symbols:
+ +[HMMDateProvider datesOfPreviousMonthForDate:]
+ +[HMMDateProvider datesOfPreviousWeeks:forDate:]
+ +[HMMDateProvider startOfCurrentMonthForDate:]
+ +[HMMDateProvider startOfPreviousMonthForDate:]
+ -[HMMDateProvider datesOfPreviousMonth]
+ -[HMMDateProvider startOfPreviousMonth]
+ GCC_except_table112
+ GCC_except_table115
+ GCC_except_table117
+ GCC_except_table120
+ GCC_except_table160
+ GCC_except_table164
+ GCC_except_table200
+ GCC_except_table201
+ GCC_except_table231
+ GCC_except_table26
+ GCC_except_table49
+ GCC_except_table51
+ GCC_except_table57
+ GCC_except_table63
+ GCC_except_table81
+ GCC_except_table91
+ GCC_except_table94
+ GCC_except_table95
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$__TtC14HomeKitMetrics23EphemeralContainerState
+ _OBJC_CLASS_$__TtC14HomeKitMetrics30CloudTelemetryLogEventObserver
+ _OBJC_METACLASS_$__TtC14HomeKitMetrics23EphemeralContainerState
+ _OBJC_METACLASS_$__TtC14HomeKitMetrics30CloudTelemetryLogEventObserver
+ __DATA__TtC14HomeKitMetrics22DailyPartitionProvider
+ __DATA__TtC14HomeKitMetrics23CloudTelemetryConnector
+ __DATA__TtC14HomeKitMetrics23EphemeralContainerState
+ __DATA__TtC14HomeKitMetrics30CloudTelemetryLogEventObserver
+ __INSTANCE_METHODS__TtC14HomeKitMetrics23EphemeralContainerState
+ __INSTANCE_METHODS__TtC14HomeKitMetrics30CloudTelemetryLogEventObserver
+ __IVARS__TtC14HomeKitMetrics22DailyPartitionProvider
+ __IVARS__TtC14HomeKitMetrics23CloudTelemetryConnector
+ __IVARS__TtC14HomeKitMetrics23EphemeralContainerState
+ __IVARS__TtC14HomeKitMetrics30CloudTelemetryLogEventObserver
+ __METACLASS_DATA__TtC14HomeKitMetrics22DailyPartitionProvider
+ __METACLASS_DATA__TtC14HomeKitMetrics23CloudTelemetryConnector
+ __METACLASS_DATA__TtC14HomeKitMetrics23EphemeralContainerState
+ __METACLASS_DATA__TtC14HomeKitMetrics30CloudTelemetryLogEventObserver
+ __OBJC_$_PROP_LIST_HMMCloudTelemetryObservable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMCloudTelemetryObservable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMCloudTelemetryObservable
+ __OBJC_LABEL_PROTOCOL_$_HMMCloudTelemetryObservable
+ __OBJC_PROTOCOL_$_HMMCloudTelemetryObservable
+ __PROTOCOLS__TtC14HomeKitMetrics30CloudTelemetryLogEventObserver
+ __PROTOCOLS__TtC14HomeKitMetrics30CloudTelemetryLogEventObserver.2
+ __PROTOCOLS__TtCC14HomeKitMetrics25BaseMetricsManagerGenericP33_3F9386BFD5EA682752F81B798AABFF3E25CountersSaveTimerDelegate.21
+ ___block_descriptor_48_e8_32r_e5_v8?0lr32l8
+ ___block_literal_global.11
+ ___block_literal_global.1373
+ ___block_literal_global.1660
+ ___block_literal_global.278
+ ___block_literal_global.28
+ ___block_literal_global.356
+ ___block_literal_global.415
+ ___block_literal_global.532
+ ___block_literal_global.607
+ ___block_literal_global.796
+ ___block_literal_global.913
+ ___swift_memcpy96_8
+ ___swift_mutable_project_boxed_opaque_existential_0
+ ___unnamed_5
+ _get_type_metadata 14HomeKitMetrics18RepeatingSchedulerRzs8SendableRzAA05DailyE8ProtocolR_sACR_r0_l15Synchronization5MutexVyAA04BaseC14ManagerGenericC5State33_3F9386BFD5EA682752F81B798AABFF3ELLVyxq__GG.20
+ _get_type_metadata 15Synchronization6AtomicVySbG.15
+ _logCategory._hmf_once_t1.912
+ _logCategory._hmf_once_t9.436
+ _logCategory._hmf_once_v10.437
+ _logCategory._hmf_once_v2.914
+ _objc_msgSend$datesOfPreviousMonthForDate:
+ _objc_msgSend$startOfCurrentMonthForDate:
+ _objc_msgSend$startOfPreviousMonthForDate:
+ _objectdestroy.74Tm
+ _sharedInstance._hmf_once_t0.1372
+ _sharedInstance._hmf_once_t0.27
+ _sharedInstance._hmf_once_t0.355
+ _sharedInstance._hmf_once_v1.1374
+ _sharedInstance._hmf_once_v1.29
+ _sharedInstance._hmf_once_v1.357
+ _symbolic $s14HomeKitMetrics28CounterDatePartitionProviderP
+ _symbolic SDyS2SG
+ _symbolic SDySSypG
+ _symbolic SS_Sdt
+ _symbolic SS_Sit
+ _symbolic SS______t 14HomeKitMetrics19CounterDistributionV
+ _symbolic SS_ypt
+ _symbolic SaySDySSypGG
+ _symbolic _____ 14HomeKitMetrics13CounterFilterV
+ _symbolic _____ 14HomeKitMetrics16CounterFormatterO
+ _symbolic _____ 14HomeKitMetrics22DailyPartitionProviderC
+ _symbolic _____ 14HomeKitMetrics23CloudTelemetryConnectorC
+ _symbolic _____ 14HomeKitMetrics30CloudTelemetryLogEventObserverC
+ _symbolic ______p 14HomeKitMetrics28CounterDatePartitionProviderP
+ _symbolic _____yS2SG s18_DictionaryStorageC
+ _symbolic _____ySDySSypGG s23_ContiguousArrayStorageC
+ _symbolic _____ySS_SdtG s23_ContiguousArrayStorageC
+ _symbolic _____ySS_SitG s23_ContiguousArrayStorageC
+ _symbolic _____ySS______tG s23_ContiguousArrayStorageC 14HomeKitMetrics19CounterDistributionV
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic _____ySbG 15Synchronization6AtomicV
- +[HMMDailyPartitionProvider sharedInstance]
- -[HMMDailyPartitionProvider .cxx_destruct]
- -[HMMDailyPartitionProvider currentDatePartition]
- -[HMMDailyPartitionProvider datePartitionContainingDate:]
- -[HMMDailyPartitionProvider datePartitionWithOffset:fromDatePartition:]
- -[HMMDailyPartitionProvider datePartitionWithOffsetFromNow:]
- -[HMMDailyPartitionProvider dateProvider]
- -[HMMDailyPartitionProvider initWithDateProvider:]
- GCC_except_table110
- GCC_except_table139
- GCC_except_table162
- GCC_except_table169
- GCC_except_table172
- GCC_except_table173
- GCC_except_table190
- GCC_except_table191
- GCC_except_table192
- GCC_except_table197
- GCC_except_table229
- GCC_except_table25
- GCC_except_table319
- GCC_except_table388
- GCC_except_table393
- GCC_except_table396
- GCC_except_table82
- _OBJC_CLASS_$_HMMCounterDistribution
- _OBJC_CLASS_$_HMMDailyPartitionProvider
- _OBJC_CLASS_$_HMMEphemeralContainerState
- _OBJC_IVAR_$_HMMDailyPartitionProvider._dateProvider
- _OBJC_METACLASS_$_HMMCounterDistribution
- _OBJC_METACLASS_$_HMMDailyPartitionProvider
- _OBJC_METACLASS_$_HMMEphemeralContainerState
- __DATA_HMMCounterDistribution
- __DATA_HMMEphemeralContainerState
- __INSTANCE_METHODS_HMMCounterDistribution
- __INSTANCE_METHODS_HMMEphemeralContainerState
- __IVARS_HMMCounterDistribution
- __IVARS_HMMEphemeralContainerState
- __METACLASS_DATA_HMMCounterDistribution
- __METACLASS_DATA_HMMEphemeralContainerState
- __OBJC_$_CLASS_METHODS_HMMDailyPartitionProvider
- __OBJC_$_INSTANCE_METHODS_HMMDailyPartitionProvider
- __OBJC_$_INSTANCE_VARIABLES_HMMDailyPartitionProvider
- __OBJC_$_PROP_LIST_HMMCounterDatePartitionProvider
- __OBJC_$_PROP_LIST_HMMDailyPartitionProvider
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMCounterDatePartitionProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_HMMCounterDatePartitionProvider
- __OBJC_$_PROTOCOL_REFS_HMMCounterDatePartitionProvider
- __OBJC_CLASS_PROTOCOLS_$_HMMDailyPartitionProvider
- __OBJC_CLASS_RO_$_HMMDailyPartitionProvider
- __OBJC_LABEL_PROTOCOL_$_HMMCounterDatePartitionProvider
- __OBJC_METACLASS_RO_$_HMMDailyPartitionProvider
- __OBJC_PROTOCOL_$_HMMCounterDatePartitionProvider
- __PROPERTIES_HMMCounterDistribution
- __PROPERTIES_HMMEphemeralContainerState
- __PROTOCOLS__TtCC14HomeKitMetrics25BaseMetricsManagerGenericP33_3F9386BFD5EA682752F81B798AABFF3E25CountersSaveTimerDelegate.27
- ___43+[HMMDailyPartitionProvider sharedInstance]_block_invoke
- ___block_literal_global.1023
- ___block_literal_global.1218
- ___block_literal_global.1415
- ___block_literal_global.1530
- ___block_literal_global.1749
- ___block_literal_global.188
- ___block_literal_global.307
- ___block_literal_global.521
- ___block_literal_global.591
- ___block_literal_global.764
- ___block_literal_global.91
- ___swift_memcpy64_8
- ___unnamed_6
- _block_copy_helper.16
- _block_copy_helper.19
- _block_descriptor.18
- _block_descriptor.21
- _block_destroy_helper.17
- _block_destroy_helper.20
- _flat unique So31HMMCounterDatePartitionProvider_p
- _get_type_metadata 14HomeKitMetrics18RepeatingSchedulerRzs8SendableRzAA05DailyE8ProtocolR_sACR_r0_l15Synchronization5MutexVyAA04BaseC14ManagerGenericC5State33_3F9386BFD5EA682752F81B798AABFF3ELLVyxq__GG.26
- _logCategory._hmf_once_t1.1414
- _logCategory._hmf_once_t9.763
- _logCategory._hmf_once_v10.765
- _logCategory._hmf_once_v2.1416
- _objc_msgSend$dateProvider
- _objc_msgSend$initWithDateProvider:
- _objc_msgSend$startOfCurrentDay
- _objc_msgSend$startOfDayByAddingDayCount:
- _objectdestroy.80Tm
- _sharedInstance._hmf_once_t0.1022
- _sharedInstance._hmf_once_t0.1529
- _sharedInstance._hmf_once_t0.1748
- _sharedInstance._hmf_once_t0.389
- _sharedInstance._hmf_once_v1.1024
- _sharedInstance._hmf_once_v1.1531
- _sharedInstance._hmf_once_v1.1750
- _sharedInstance._hmf_once_v1.390
- _symbolic _____ 14HomeKitMetrics22HMMCounterDistributionC
- _symbolic ______p So31HMMCounterDatePartitionProviderP
CStrings:
+ "Dropping event %s because CloudTelemetry not yet initialized"
+ "Failed to send Cloud Telemetry event %s: %@"
+ "HMMCloudTelemetryObservable"
+ "HomeKitMetrics.CloudTelemetryLogEventObserver"
+ "_TtC14HomeKitMetrics22DailyPartitionProvider"
+ "_TtC14HomeKitMetrics23CloudTelemetryConnector"
+ "_TtC14HomeKitMetrics23EphemeralContainerState"
+ "_TtC14HomeKitMetrics30CloudTelemetryLogEventObserver"
+ "cloudTelemetryEventData"
+ "cloudTelemetryEventType"
+ "connector"
+ "datesOfPreviousMonth"
+ "datesOfPreviousMonthForDate:"
+ "datesOfPreviousWeeks:forDate:"
+ "isInitialized"
+ "setDateFormat:"
+ "setLocale:"
+ "softlink:o:path:/AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit"
+ "startOfCurrentMonthForDate:"
+ "startOfPreviousMonth"
+ "startOfPreviousMonthForDate:"
+ "stringFromDate:"
+ "teamID"
- "@\"HMMDateProvider\""
- "@\"NSDate\"16@0:8"
- "@\"NSDate\"24@0:8@\"NSDate\"16"
- "@\"NSDate\"24@0:8q16"
- "@\"NSDate\"32@0:8q16@\"NSDate\"24"
- "HMMCounterDatePartitionProvider"
- "HMMDailyPartitionProvider"
- "HMMEphemeralContainerState"
- "HomeKitMetrics.HMMCounterDistribution"
- "T@\"HMMDateProvider\",R,N,V_dateProvider"
- "TB,N"
- "Td,N,R"
- "Tq,N,R"
- "_dateProvider"
- "activeDuration"
- "averageValue"
- "currentDatePartition"
- "datePartitionContainingDate:"
- "datePartitionWithOffset:fromDatePartition:"
- "datePartitionWithOffsetFromNow:"
- "distribution"
- "initWithDateProvider:"
- "maxValue"
- "minValue"
- "setIsActive:"
- "softlink:o:path:/System/Library/PrivateFrameworks/TapToRadarKit.framework/TapToRadarKit"
- "standardDeviation"
- "sumOfSquares"
- "sumOfValues"
- "valueCount"
- "variance"

```
