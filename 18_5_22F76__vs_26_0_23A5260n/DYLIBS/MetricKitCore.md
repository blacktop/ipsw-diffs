## MetricKitCore

> `/System/Library/PrivateFrameworks/MetricKitCore.framework/MetricKitCore`

```diff

-261.0.0.0.0
-  __TEXT.__text: 0x15a00
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x198c
+291.0.0.0.1
+  __TEXT.__text: 0x167c4
+  __TEXT.__auth_stubs: 0x590
+  __TEXT.__objc_methlist: 0x19f4
   __TEXT.__const: 0x158
-  __TEXT.__cstring: 0x7c7
-  __TEXT.__oslogstring: 0x1b3c
-  __TEXT.__gcc_except_tab: 0xcc
-  __TEXT.__unwind_info: 0x548
+  __TEXT.__cstring: 0x7e2
+  __TEXT.__oslogstring: 0x1c8e
+  __TEXT.__gcc_except_tab: 0x14
+  __TEXT.__unwind_info: 0x528
   __TEXT.__objc_classname: 0x2be
-  __TEXT.__objc_methname: 0x472b
-  __TEXT.__objc_methtype: 0x97a
-  __TEXT.__objc_stubs: 0x38c0
-  __DATA_CONST.__got: 0x398
-  __DATA_CONST.__const: 0x158
+  __TEXT.__objc_methname: 0x48bc
+  __TEXT.__objc_methtype: 0x98d
+  __TEXT.__objc_stubs: 0x3940
+  __DATA_CONST.__got: 0x3a8
+  __DATA_CONST.__const: 0x180
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1018
+  __DATA_CONST.__objc_selrefs: 0x1050
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x80
-  __DATA_CONST.__objc_arraydata: 0x3f8
-  __AUTH_CONST.__auth_got: 0x2e8
+  __DATA_CONST.__objc_superrefs: 0x88
+  __DATA_CONST.__objc_arraydata: 0x580
+  __AUTH_CONST.__auth_got: 0x2d8
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x740
-  __AUTH_CONST.__objc_const: 0x2ba8
-  __AUTH_CONST.__objc_arrayobj: 0x210
+  __AUTH_CONST.__objc_const: 0x2c18
+  __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_intobj: 0x78
-  __DATA.__objc_ivar: 0x138
+  __DATA.__objc_ivar: 0x140
   __DATA.__data: 0x660
   __DATA_DIRTY.__objc_data: 0x5a0
   __DATA_DIRTY.__bss: 0x30

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MetricKitServices.framework/MetricKitServices
   - /System/Library/PrivateFrameworks/MetricKitSource.framework/MetricKitSource
+  - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B04F25A3-2439-39E9-951A-7EADA1D028EA
-  Functions: 616
-  Symbols:   2293
-  CStrings:  1058
+  UUID: 155E48F1-3114-38C1-8F91-72DB12FAD045
+  Functions: 633
+  Symbols:   2345
+  CStrings:  1078
 
Symbols:
+ +[MXCorePayloadConstructor buildMetricPayloadForClient:fromClientMetricsDictionary:]
+ +[MXCorePayloadConstructor buildMetricPayloadForClient:fromClientMetricsDictionary:].cold.1
+ +[MXCorePayloadConstructor buildMetricPayloadForClient:fromClientMetricsDictionary:].cold.2
+ +[MXCorePayloadConstructor constructPayloadWithServiceString:withSourceData:withDateString:forClient:].cold.13
+ +[MXCorePayloadConstructor constructPayloadWithServiceString:withSourceData:withDateString:forClient:].cold.14
+ +[MXCorePayloadConstructor constructPayloadWithServiceString:withSourceData:withDateString:forClient:].cold.15
+ +[MXCorePayloadConstructor updatePayload:withServiceString:withSourceData:withDateString:forClient:].cold.1
+ +[MXCorePayloadConstructor updatePayload:withServiceString:withSourceData:withDateString:forClient:].cold.2
+ +[MXCorePayloadConstructor updatePayload:withServiceString:withSourceData:withDateString:forClient:].cold.3
+ +[MXCorePayloadConstructor updatePayload:withServiceString:withSourceData:withDateString:forClient:].cold.4
+ +[MXCorePayloadConstructor updatePayload:withServiceString:withSourceData:withDateString:forClient:].cold.5
+ +[MXCorePayloadConstructor updatePayload:withServiceString:withSourceData:withDateString:forClient:].cold.6
+ +[MXCorePayloadConstructor updatePayload:withServiceString:withSourceData:withDateString:forClient:].cold.7
+ +[MXCorePayloadConstructor updatePayload:withServiceString:withSourceData:withDateString:forClient:].cold.8
+ +[MXCorePayloadConstructor updatePayload:withServiceString:withSourceData:withDateString:forClient:].cold.9
+ -[MXCleanUtil _cleanClientlessSourceDirectoriesForStaleData]
+ -[MXCleanUtil _clientlessSourceDirectories]
+ -[MXCleanUtil _clientlessSourceDirectories].cold.1
+ -[MXCleanUtil dateUtil]
+ -[MXCleanUtil initWithClientUtil:andDeliveryPathUtil:andDateUtil:]
+ -[MXCleanUtil setDateUtil:]
+ -[MXDateUtil .cxx_destruct]
+ -[MXDateUtil dateFormatter]
+ -[MXDateUtil dateFromString:]
+ -[MXDateUtil init]
+ -[MXDateUtil setDateFormatter:]
+ -[MXPayloadValidator _validateSpaceAttributionData:]
+ -[MXPayloadValidator _validateSpaceAttributionData:].cold.1
+ GCC_except_table29
+ _OBJC_CLASS_$_MXDiskSpaceUsageMetric
+ _OBJC_CLASS_$_MXSpaceAttributionData
+ _OBJC_CLASS_$_MXSpaceAttributionService
+ _OBJC_IVAR_$_MXCleanUtil._dateUtil
+ _OBJC_IVAR_$_MXDateUtil._dateFormatter
+ __OBJC_$_INSTANCE_VARIABLES_MXDateUtil
+ __OBJC_$_PROP_LIST_MXDateUtil
+ ___29-[MXCore performDataActivity]_block_invoke
+ ___31-[MXCore _scheduleDataActivity]_block_invoke_2
+ ___40-[MXSource _setupHandlersForConnection:]_block_invoke.28
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32s40w_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8w40l8
+ _objc_copyWeak
+ _objc_initWeak
+ _objc_msgSend$_cleanClientlessSourceDirectoriesForStaleData
+ _objc_msgSend$_clientlessSourceDirectories
+ _objc_msgSend$_validateSpaceAttributionData:
+ _objc_msgSend$buildMetricPayloadForClient:fromClientMetricsDictionary:
+ _objc_msgSend$diskSpaceUsageMetrics
+ _objc_msgSend$exactBundleVersion
+ _objc_msgSend$initWithClientUtil:andDeliveryPathUtil:andDateUtil:
+ _objc_msgSend$initWithHitchTimeRatio:perceivedHitchTimeRatio:
+ _objc_msgSend$initWithTotalBinaryFileSize:totalBinaryFileCount:totalDataFileSize:totalDataFileCount:totalCacheFolderSize:totalCloneSize:totalDiskSpaceUsedSize:totalDiskSpaceCapacity:
+ _objc_msgSend$setDiskSpaceUsageMetrics:
+ _objc_msgSend$sharedSpaceAttributionService
- +[MXCorePayloadConstructor buildPayloadForClient:fromClientMetricsDictionary:]
- +[MXCorePayloadConstructor buildPayloadForClient:fromClientMetricsDictionary:].cold.1
- +[MXCorePayloadConstructor buildPayloadForClient:fromClientMetricsDictionary:].cold.2
- -[MXCleanUtil _cleanClientlessSourceDirectoryForStaleData]
- -[MXCleanUtil _clientlessSourceDirectory]
- -[MXCleanUtil _clientlessSourceDirectory].cold.1
- -[MXMetricServices _isMetricSourceDataAvailable].cold.1
- GCC_except_table16
- GCC_except_table20
- GCC_except_table24
- GCC_except_table3
- _OBJC_EHTYPE_$_NSException
- ___40-[MXSource _setupHandlersForConnection:]_block_invoke.27
- ___92-[MXCore metricIsAvailableFromSourceDirectoryForSavingToDeliveryDirectoryWithClientMetrics:]_block_invoke
- ___92-[MXCore metricIsAvailableFromSourceDirectoryForSavingToDeliveryDirectoryWithClientMetrics:]_block_invoke.cold.1
- ___block_descriptor_40_e8_32s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
- _dispatch_sync
- _objc_begin_catch
- _objc_end_catch
- _objc_msgSend$_cleanClientlessSourceDirectoryForStaleData
- _objc_msgSend$_clientlessSourceDirectory
- _objc_msgSend$buildPayloadForClient:fromClientMetricsDictionary:
- _objc_msgSend$initWithClientUtil:andDeliveryPathUtil:
- _objc_msgSend$initWithGlitchTimeRatio:
- _objc_msgSend$initWithRegionFormat:osVersion:deviceType:appBuildVersion:
- _objc_msgSend$reason
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "@\"NSDateFormatter\""
+ "Compatible service string not found. Received: %@"
+ "Construction Step: Metadata"
+ "Construction Step: Powerlog data"
+ "Construction Step: Space Attribution Data: %@"
+ "Construction Step: Space Attribution data"
+ "Error retrieving app record for %@: %@"
+ "Failed to retrieve space attribution data."
+ "Invalid Space Attribution Data"
+ "Meta Data: %@"
+ "Nil payload received in update path"
+ "Payload Constructor"
+ "Payload Updater"
+ "Service %@ returned YES for metrics check "
+ "SpaceAttribution"
+ "T@\"NSDateFormatter\",&,V_dateFormatter"
+ "Update Step: Date Data: %@, %@"
+ "Update Step: Powerlog Data: %@"
+ "Update Step: Powerlog data"
+ "Update Step: Space Attribution Data: %@"
+ "Update Step: Space Attribution data"
+ "_cleanClientlessSourceDirectoriesForStaleData"
+ "_clientlessSourceDirectories"
+ "_dateFormatter"
+ "_validateSpaceAttributionData:"
+ "buildMetricPayloadForClient:fromClientMetricsDictionary:"
+ "dateFormatter"
+ "diskSpaceUsageMetrics"
+ "exactBundleVersion"
+ "initWithClientUtil:andDeliveryPathUtil:andDateUtil:"
+ "initWithHitchTimeRatio:perceivedHitchTimeRatio:"
+ "initWithTotalBinaryFileSize:totalBinaryFileCount:totalDataFileSize:totalDataFileCount:totalCacheFolderSize:totalCloneSize:totalDiskSpaceUsedSize:totalDiskSpaceCapacity:"
+ "setDateFormatter:"
+ "setDiskSpaceUsageMetrics:"
+ "sharedSpaceAttributionService"
- "Compatible service string not found. Expected: %@, Received: %@"
- "Construction Step: Powerlog Data"
- "Error in payload constructor: %@"
- "Meta Data V1: %@"
- "Meta Data V2: %@"
- "Payload Meta Data:%@"
- "Source Directory: %@"
- "Starting payload delivery"
- "_cleanClientlessSourceDirectoryForStaleData"
- "_clientlessSourceDirectory"
- "buildPayloadForClient:fromClientMetricsDictionary:"
- "cumulativeCPUInstructions"
- "initWithGlitchTimeRatio:"
- "initWithRegionFormat:osVersion:deviceType:appBuildVersion:"
- "reason"

```
