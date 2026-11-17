## MetricKit

> `/System/Library/Frameworks/MetricKit.framework/MetricKit`

```diff

-369.60.4.0.0
-  __TEXT.__text: 0x83480
-  __TEXT.__objc_methlist: 0x293c
-  __TEXT.__const: 0x94e6
-  __TEXT.__cstring: 0x1f82
+369.60.5.0.0
+  __TEXT.__text: 0x89948
+  __TEXT.__objc_methlist: 0x2ac4
+  __TEXT.__const: 0x9556
+  __TEXT.__cstring: 0x1fc2
+  __TEXT.__oslogstring: 0x3c9
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__oslogstring: 0x349
-  __TEXT.__swift5_typeref: 0x1990
-  __TEXT.__swift5_reflstr: 0x1183
+  __TEXT.__swift5_typeref: 0x1a90
+  __TEXT.__swift5_reflstr: 0x1190
   __TEXT.__swift5_assocty: 0x4b0
   __TEXT.__constg_swiftt: 0x143c
-  __TEXT.__swift5_fieldmd: 0x1c30
+  __TEXT.__swift5_fieldmd: 0x1c3c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x94c
   __TEXT.__swift5_types: 0x218

   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x2f20
+  __TEXT.__unwind_info: 0x2f58
   __TEXT.__eh_frame: 0x27e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x170
+  __DATA_CONST.__const: 0x190
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1240
+  __DATA_CONST.__objc_selrefs: 0x1348
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x178
-  __DATA_CONST.__got: 0x498
-  __AUTH_CONST.__const: 0x4719
+  __DATA_CONST.__got: 0x4a0
+  __AUTH_CONST.__const: 0x4741
   __AUTH_CONST.__cfstring: 0x1c00
   __AUTH_CONST.__objc_const: 0x6820
-  __AUTH_CONST.__auth_got: 0xa58
+  __AUTH_CONST.__auth_got: 0xa90
   __AUTH.__objc_data: 0x188
   __AUTH.__data: 0x1c0
   __DATA.__objc_ivar: 0x440
-  __DATA.__data: 0x13d0
-  __DATA.__common: 0x40
+  __DATA.__data: 0x1430
+  __DATA.__common: 0x58
   __DATA_DIRTY.__objc_data: 0x11b0
   __DATA_DIRTY.__data: 0x1298
   __DATA_DIRTY.__bss: 0x390

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3509
-  Symbols:   2482
-  CStrings:  360
+  Functions: 3554
+  Symbols:   2533
+  CStrings:  365
 
Symbols:
+ -[MXAnimationMetric nullableHitchTimeRatio]
+ -[MXAppRunTimeMetric nullableCumulativeBackgroundAudioTime]
+ -[MXAppRunTimeMetric nullableCumulativeBackgroundLocationTime]
+ -[MXAppRunTimeMetric nullableCumulativeBackgroundTime]
+ -[MXAppRunTimeMetric nullableCumulativeForegroundTime]
+ -[MXAverage nullableAverageMeasurement]
+ -[MXCPUMetric nullableCumulativeCPUInstructions]
+ -[MXCPUMetric nullableCumulativeCPUTime]
+ -[MXDiskIOMetric nullableCumulativeLogicalWrites]
+ -[MXDiskSpaceUsageMetric nullableTotalBinaryFileSize]
+ -[MXDiskSpaceUsageMetric nullableTotalCacheFolderSize]
+ -[MXDiskSpaceUsageMetric nullableTotalCloneSize]
+ -[MXDiskSpaceUsageMetric nullableTotalDataFileSize]
+ -[MXDiskSpaceUsageMetric nullableTotalDiskSpaceCapacity]
+ -[MXDiskSpaceUsageMetric nullableTotalDiskSpaceUsedSize]
+ -[MXGPUMetric nullableCumulativeGPUTime]
+ -[MXHistogramBucket nullableBucketEnd]
+ -[MXHistogramBucket nullableBucketStart]
+ -[MXLocationActivityMetric nullableCumulativeBestAccuracyForNavigationTime]
+ -[MXLocationActivityMetric nullableCumulativeBestAccuracyTime]
+ -[MXLocationActivityMetric nullableCumulativeHundredMetersAccuracyTime]
+ -[MXLocationActivityMetric nullableCumulativeKilometerAccuracyTime]
+ -[MXLocationActivityMetric nullableCumulativeNearestTenMetersAccuracyTime]
+ -[MXLocationActivityMetric nullableCumulativeReducedAccuracyTime]
+ -[MXLocationActivityMetric nullableCumulativeThreeKilometersAccuracyTime]
+ -[MXMemoryMetric nullableAverageSuspendedMemory]
+ -[MXMemoryMetric nullablePeakMemoryUsage]
+ -[MXMetalFrameRateMetric nullableActiveDrawingDuration]
+ -[MXMetalFrameRateMetric nullableAverageFrameRate]
+ -[MXNetworkTransferMetric nullableCumulativeCellularDownload]
+ -[MXNetworkTransferMetric nullableCumulativeCellularUpload]
+ -[MXNetworkTransferMetric nullableCumulativeWifiDownload]
+ -[MXNetworkTransferMetric nullableCumulativeWifiUpload]
+ _MXNullableBridgedValue
+ _MXNullableBridgedValue.log
+ _MXNullableBridgedValue.onceToken
+ _NSStringFromClass
+ ___MXNullableBridgedValue_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ _swift_getMetatypeMetadata
+ _symbolic So14NSUnitDurationCm
+ _symbolic So15NSUnitFrequencyCm
+ _symbolic So24NSUnitInformationStorageCm
+ _symbolic _____ySo15NSUnitFrequencyCGSg 10Foundation11MeasurementV
+ _symbolic _____ySo16MXUnitSignalBarsCGSg 10Foundation11MeasurementV
+ _symbolic _____ySo27MXUnitAveragePixelLuminanceCGSg 10Foundation11MeasurementV
+ _symbolic _____y_____G 10Foundation11MeasurementV 9MetricKit10SignalBarsC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y_____GSg 10Foundation11MeasurementV 9MetricKit10SignalBarsC
+ _symbolic _____y_____GSg 10Foundation11MeasurementV 9MetricKit21AveragePixelLuminanceC
+ _symbolic _____y_____GSg 9MetricKit17AverageStatisticsV AA0C14PixelLuminanceC
CStrings:
+ "MetricReport"
+ "Nonnull declared measurement has unexpected unit: %s (expected %s)"
+ "Nonnull declared nil value encountered: %@.%s (nil)"
+ "averageFrameRate"
+ "averageMeasurement"
```
