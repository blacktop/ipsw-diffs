## MetricMeasurement

> `/System/Library/PrivateFrameworks/MetricMeasurement.framework/MetricMeasurement`

```diff

-297.120.4.0.0
-  __TEXT.__text: 0x1e524
-  __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_methlist: 0x28bc
+353.0.0.0.0
+  __TEXT.__text: 0x1d41c
+  __TEXT.__objc_methlist: 0x28c4
   __TEXT.__const: 0x268
-  __TEXT.__cstring: 0x2645
-  __TEXT.__gcc_except_tab: 0x6f4
+  __TEXT.__cstring: 0x268f
+  __TEXT.__gcc_except_tab: 0x648
   __TEXT.__oslogstring: 0x9d5
   __TEXT.__ustring: 0x34
-  __TEXT.__unwind_info: 0x9c8
-  __TEXT.__objc_classname: 0x5c5
-  __TEXT.__objc_methname: 0x4b7a
-  __TEXT.__objc_methtype: 0x10f2
-  __TEXT.__objc_stubs: 0x4200
-  __DATA_CONST.__got: 0x288
-  __DATA_CONST.__const: 0x6a0
+  __TEXT.__unwind_info: 0x9a0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x6a8
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_nlclslist: 0x8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1550
+  __DATA_CONST.__objc_selrefs: 0x1558
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x108
-  __AUTH_CONST.__auth_got: 0x438
+  __DATA_CONST.__got: 0x288
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x27e0
+  __AUTH_CONST.__cfstring: 0x2800
   __AUTH_CONST.__objc_const: 0x59d8
   __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH_CONST.__auth_got: 0x478
   __AUTH.__objc_data: 0xe60
   __DATA.__objc_ivar: 0x170
   __DATA.__data: 0x7e0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpmsample.dylib
   - /usr/lib/libsysmon.dylib
-  UUID: 6DE27443-A30D-3136-9DB2-3B4434272BDB
-  Functions: 870
-  Symbols:   3257
-  CStrings:  1893
+  UUID: B1DEF6AB-9149-35E6-8D98-E926EDE8DF9D
+  Functions: 871
+  Symbols:   3268
+  CStrings:  713
 
Symbols:
+ +[MXMEnergySampleTag allEnergySampleTags]
+ _MXMAttributeNameOSSignpostEndEventProcessName
+ ___block_literal_global.277
+ _basename_r
+ _objc_claimAutoreleasedReturnValue
+ _objc_exception_rethrow
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_retain_x9
+ _proc_pidpath
- ___block_literal_global.278
- _proc_name
Functions:
~ +[MXMEnergyMetric currentProcess] : 204 -> 196
~ -[MXMEnergyMetric initWithProcessNames:] : 460 -> 444
~ -[MXMEnergyMetric processNames] : 124 -> 112
~ -[MXMEnergyMetric prepareWithOptions:error:] : 1192 -> 1148
~ ___44-[MXMEnergyMetric prepareWithOptions:error:]_block_invoke : 128 -> 112
~ -[MXMEnergyMetric willStartAtEstimatedTime:] : 168 -> 164
~ -[MXMEnergyMetric didStopAtContinuousTime:absoluteTime:stopDate:] : 260 -> 244
~ -[MXMEnergyMetric _convertMetricsToSampleData:] : 1596 -> 1512
~ -[MXMEnergyMetric appendMetricSample:name:tag:unit:conversionFactor:processName:pidNumber:toData:timestamp:] : 644 -> 596
~ -[MXMEnergyMetric harvestData:error:] : 728 -> 672
~ ___37-[MXMEnergyMetric harvestData:error:]_block_invoke : 128 -> 112
~ -[MXMMemoryMetric initWithProcessIdentifier:] : 268 -> 256
~ -[MXMMemoryMetric initWithProcessName:] : 252 -> 248
~ -[MXMMemoryMetric initWithBundleIdentifier:] : 80 -> 76
~ -[MXMMemoryMetric willStartAtEstimatedTime:] : 128 -> 124
~ -[MXMMemoryMetric processName] : 124 -> 112
~ -[MXMMemoryMetric processIdentifier] : 124 -> 112
~ -[MXMProxyProbe initWithCoder:] : 124 -> 120
~ -[MXMProxyProbe encodeWithCoder:] : 112 -> 108
~ -[MXMProxyProbe updateNowUntilStoppedWithUpdateHandler:stopHandler:] : 72 -> 68
~ -[MXMProxyProbe sampleWithTimeout:stopReason:] : 160 -> 148
~ +[MXMProxyServiceManager shared] : 84 -> 68
~ -[MXMProxyServiceManager initInternal] : 168 -> 164
~ -[MXMProxyServiceManager _proxyObject] : 92 -> 84
~ ___38-[MXMProxyServiceManager _proxyObject]_block_invoke : 176 -> 128
~ -[MXMProxyServiceManager wake] : 312 -> 304
~ ___30-[MXMProxyServiceManager wake]_block_invoke : 72 -> 16
~ ___68-[MXMProxyServiceManager _sampleWithProxyMetric:timeout:stopReason:]_block_invoke : 128 -> 96
~ -[MXMProxyServiceManager _setupMetricMonitorWithProxyMetric:processNames:response:] : 392 -> 396
~ ___83-[MXMProxyServiceManager _setupMetricMonitorWithProxyMetric:processNames:response:]_block_invoke : 96 -> 32
~ -[MXMProxyServiceManager _sampleFromMetricMonitorWithProxyMetric:timeout:stopReason:] : 740 -> 680
~ ___85-[MXMProxyServiceManager _sampleFromMetricMonitorWithProxyMetric:timeout:stopReason:]_block_invoke : 156 -> 160
~ -[MXMProxyServiceManager _teardownMetricMonitorWithProxyMetric:response:] : 196 -> 200
~ ___58-[MXMProxyServiceManager _startPerformanceTrace:response:]_block_invoke : 204 -> 216
~ -[MXMProxyServiceManager _stopPerformanceTrace:] : 988 -> 976
~ ___48-[MXMProxyServiceManager _stopPerformanceTrace:]_block_invoke : 300 -> 328
~ ___68-[MXMProxyServiceManager _startFunctionCoverageCollection:response:]_block_invoke : 92 -> 36
~ -[MXMProxyServiceManager _stopFunctionCoverageCollection:] : 384 -> 380
~ ___58-[MXMProxyServiceManager _stopFunctionCoverageCollection:]_block_invoke : 140 -> 136
~ -[MXMProxyServiceManager _quiesceBeforeIteration:timeout:response:] : 372 -> 368
~ ___67-[MXMProxyServiceManager _quiesceBeforeIteration:timeout:response:]_block_invoke : 96 -> 32
~ ___59-[MXMProxyServiceManager _uncacheBeforeIteration:response:]_block_invoke : 96 -> 32
~ ___70-[MXMProxyServiceManager _terminateProcessesBeforeIteration:response:]_block_invoke : 96 -> 32
~ -[MXMProxyServiceManager dealloc] : 92 -> 88
~ -[MXMProxyMetric initWithMetric:] : 132 -> 136
~ -[MXMProxyMetric metric] : 76 -> 72
~ -[MXMProxyMetric _remoteProbe] : 344 -> 272
~ -[MXMProxyMetric encodeWithCoder:] : 140 -> 136
~ -[MXMProxyMetric copyWithZone:] : 116 -> 112
~ -[MXMProxyMetric _sampleMode] : 128 -> 120
~ -[MXMProxyMetric prepareWithOptions:error:] : 156 -> 152
~ -[MXMProxyMetric willStartAtEstimatedTime:] : 104 -> 100
~ -[MXMProxyMetric didStartAtTime:startDate:] : 140 -> 136
~ -[MXMProxyMetric didStartAtContinuousTime:absoluteTime:startDate:] : 160 -> 156
~ -[MXMProxyMetric willStop] : 96 -> 92
~ -[MXMProxyMetric didStopAtTime:stopDate:] : 140 -> 136
~ -[MXMProxyMetric didStopAtContinuousTime:absoluteTime:stopDate:] : 160 -> 156
~ +[MXMResourceProbe _processIdentifierWithProcessName:error:] : 620 -> 684
~ ___48-[MXMResourceProbe _buildData:timestamp:rusage:]_block_invoke : 920 -> 828
~ -[MXMResourceProbe _buildData:timestamp:taskinfo:] : 260 -> 244
~ -[MXMResourceProbe _buildData:timestamp:mach_space_basicinfo:] : 232 -> 220
~ -[MXMResourceProbe _buildData:timestamp:pm_networking_stats:] : 740 -> 688
~ -[MXMResourceProbe _beginUpdates] : 300 -> 296
~ ___33-[MXMResourceProbe _beginUpdates]_block_invoke : 220 -> 208
~ -[MXMResourceProbe _stopUpdates] : 220 -> 208
~ -[MXMResourceProbe sampleWithTimeout:stopReason:] : 128 -> 116
~ -[MXMResourceProbe performPreIterationActions] : 884 -> 864
~ -[MXMResourceProbe _pollMainBody] : 1144 -> 1088
~ -[MXMResourceProbe _pollAllProcesses:] : 364 -> 316
~ -[MXMResourceProbe _pollProcessWithData:pid:] : 460 -> 440
~ -[MXMResourceProbe _pollProcessResourceUsageWithData:pid:] : 384 -> 380
~ -[MXMSampleSet(Stats) min] : 264 -> 252
~ -[MXMSampleSet(Stats) max] : 264 -> 252
~ -[MXMSampleSet(Stats) distance] : 276 -> 264
~ -[MXMSampleSet(Stats) range] : 360 -> 336
~ -[MXMSampleSet(Stats) geoMean] : 248 -> 236
~ -[MXMSampleSet(Stats) standardDeviation] : 248 -> 236
~ -[MXMSampleSet(Stats) relativeStandardDeviation] : 252 -> 240
~ -[MXMSampleSet(Stats) sum] : 236 -> 224
~ -[MXMDisplayDescriptor main] : 96 -> 92
~ -[MXMDisplayDescriptor initWithDisplay:] : 108 -> 116
~ ___25+[MXMMachUtils _timebase]_block_invoke : 84 -> 80
~ +[MXMMachUtils _processNameWithBundleIdentifier:] : 132 -> 120
~ -[MXMNetworkMetric initWithProcessIdentifier:] : 268 -> 256
~ -[MXMNetworkMetric initWithProcessName:] : 252 -> 248
~ -[MXMNetworkMetric initWithBundleIdentifier:] : 80 -> 76
~ -[MXMNetworkMetric processName] : 124 -> 112
~ -[MXMNetworkMetric processIdentifier] : 124 -> 112
~ -[MXMSampleSet samples] : 396 -> 372
~ -[MXMSampleSet attributes] : 128 -> 116
~ -[MXMSampleSet attributeWithName:] : 116 -> 108
~ -[MXMSampleSet initWithTag:unit:attributes:] : 140 -> 148
~ -[MXMSampleSet initWithTime:tag:unit:attributes:values:length:valueSize:] : 592 -> 608
~ -[MXMSampleSet countByEnumeratingWithState:objects:count:] : 92 -> 88
~ -[MXMSampleSet encodeWithCoder:] : 232 -> 228
~ -[MXMSampleSet initWithCoder:] : 596 -> 576
~ -[MXMSampleSet copyWithZone:] : 212 -> 196
~ -[MXMSampleSet mutableCopyWithZone:] : 212 -> 196
~ -[MXMSampleSet _prepareUnderlyingBufferSizeWithAdditionalBytes:] : 224 -> 216
~ -[MXMSampleSet _appendAttribute:] : 208 -> 192
~ -[MXMSampleSet _appendDoubleValue:timestamp:] : 188 -> 180
~ -[MXMSampleSet _appendSample:] : 172 -> 160
~ -[MXMSampleTimeSeries initWithAbsoluteTimeSeries:length:] : 308 -> 300
~ -[MXMSampleTimeSeries initWithContinuousTimeSeries:length:] : 332 -> 324
~ -[MXMSampleTimeSeries initWithTimeSeries:tag:unit:length:] : 220 -> 224
~ -[MXMSampleTimeSeries _appendAbsoluteTime:] : 196 -> 192
~ -[MXMMutableSampleSet appendSet:] : 188 -> 176
~ -[MXMMutableSampleSet appendSample:] : 188 -> 176
~ -[MXMCPUMetric initWithProcessIdentifier:] : 332 -> 316
~ -[MXMCPUMetric initWithProcessName:] : 324 -> 316
~ -[MXMCPUMetric initWithBundleIdentifier:] : 80 -> 76
~ -[MXMCPUMetric processName] : 124 -> 112
~ -[MXMCPUMetric processIdentifier] : 124 -> 112
~ -[MXMCPUMetric _shouldConstructProbe] : 56 -> 52
~ -[MXMCPUMetric harvestData:error:] : 704 -> 676
~ -[MXMClockMetric _unit] : 16 -> 20
~ +[MXMClockMetric allTime] : 100 -> 96
~ +[MXMClockMetric absoluteTime] : 100 -> 96
~ +[MXMClockMetric continuousTime] : 100 -> 96
~ -[MXMClockMetric harvestData:error:] : 544 -> 524
~ -[MXMClockMetric copyWithZone:] : 120 -> 128
~ -[MXMClockMetric encodeWithCoder:] : 124 -> 128
~ -[MXMMetric instrument] : 172 -> 164
~ -[MXMMetric identifier] : 56 -> 8
~ -[MXMMetric version] : 56 -> 8
~ -[MXMMetric build] : 56 -> 8
~ -[MXMMetric _shouldWrapInProxy] : 196 -> 188
~ -[MXMMetric _shouldConstructProbe] : 60 -> 56
~ -[MXMMetric _constructProbe] : 60 -> 56
~ -[MXMMetric _getProbe] : 184 -> 176
~ -[MXMMetric copyWithZone:] : 188 -> 180
~ -[MXMMetric encodeWithCoder:] : 276 -> 256
~ -[MXMMetric initWithCoder:] : 320 -> 304
~ -[MXMMetric initWithIdentifier:filter:] : 324 -> 304
~ -[MXMMetric willStartAtEstimatedTime:] : 524 -> 456
~ -[MXMMetric didStopAtTime:stopDate:] : 872 -> 776
~ -[MXMMetric didStopAtContinuousTime:absoluteTime:stopDate:] : 564 -> 496
~ -[MXMMetric harvestData:error:] : 236 -> 232
~ -[MXMMetric setFilter:] : 64 -> 12
~ +[MXMDisplayProbe_iphoneOS_Internal _displayIndexWithDescriptor:] : 124 -> 116
~ +[MXMDisplayProbe_iphoneOS_Internal _allDescriptors] : 372 -> 364
~ -[MXMDisplayProbe_iphoneOS_Internal initPrivateWithDescriptor:queue:] : 156 -> 164
~ -[MXMDisplayProbe_iphoneOS_Internal _stop] : 76 -> 72
~ +[MXMOSLogDeviceStore_Internal shared] : 84 -> 68
~ -[MXMOSLogDeviceStore_Internal init] : 248 -> 236
~ -[MXMOSLogDeviceStore_Internal activityStream:deviceUDID:deviceID:status:error:] : 192 -> 188
~ -[MXMOSLogDevice_Internal initWithOSLogDevice:] : 108 -> 116
~ -[MXMOSLogDevice_Internal initWithName:identifier:] : 144 -> 152
~ -[MXMOSLogDevice_Internal setName:] : 64 -> 12
~ -[MXMOSLogDevice_Internal setIdentifier:] : 64 -> 12
~ -[MXMOSLogDevice_Internal setRawDevice:] : 64 -> 12
~ -[MXMDiskMetric initWithProcessIdentifier:] : 268 -> 256
~ -[MXMDiskMetric initWithProcessName:] : 252 -> 248
~ -[MXMDiskMetric initWithBundleIdentifier:] : 80 -> 76
~ -[MXMDiskMetric processName] : 124 -> 112
~ -[MXMDiskMetric processIdentifier] : 124 -> 112
~ +[MXMOSLogProbe hostDevice] : 92 -> 84
~ +[MXMOSLogProbe connectedDevices] : 120 -> 108
~ +[MXMOSLogProbe probeHostOSLog] : 100 -> 96
~ -[MXMOSLogProbe initWithTargetDevice:] : 288 -> 280
~ -[MXMOSLogProbe _beginUpdates] : 16 -> 20
~ -[MXMOSLogProbe _stopUpdates] : 84 -> 88
~ -[MXMSampleAttributeFilter stringValue] : 140 -> 128
~ -[MXMSampleAttributeFilter numericValue] : 140 -> 128
~ -[MXMSampleAttributeFilter value] : 112 -> 104
~ -[MXMSampleAttributeFilter values] : 112 -> 104
~ -[MXMSampleAttributeFilter initWithAttribute:] : 184 -> 168
~ -[MXMSampleAttributeFilter initWithAttributeName:stringValue:] : 116 -> 112
~ -[MXMSampleAttributeFilter initWithAttributeName:numericValue:] : 116 -> 112
~ -[MXMSampleAttributeFilter _matchesSampleAttributeValueWithValue:] : 92 -> 88
~ -[MXMSampleAttributeFilter _matchesSampleAttributeNameWithName:] : 96 -> 92
~ -[MXMSampleAttributeFilter matchesSampleWithAttribute:] : 168 -> 156
~ -[MXMSampleAttributeFilter copyWithZone:] : 144 -> 136
~ -[MXMSampleAttributeFilter encodeWithCoder:] : 152 -> 160
~ -[MXMSampleAttributeFilter initWithCoder:] : 336 -> 328
~ -[MXMSampleTagFilter matchesSampleWithTag:] : 116 -> 120
~ -[MXMSampleTagFilter copyWithZone:] : 76 -> 80
~ -[MXMSampleTagFilter encodeWithCoder:] : 124 -> 128
~ -[MXMSampleTagFilter initWithCoder:] : 124 -> 128
~ -[MXMSampleTagFilter tagPermutations] : 16 -> 20
~ +[MXMSampleFilter filterWithAttributeFilter:tagFilter:] : 108 -> 112
~ -[MXMSampleFilter initWithTagFilter:] : 80 -> 76
~ -[MXMSampleFilter initWithAttributeFilter:] : 84 -> 80
~ -[MXMSampleFilter initWithAttributeFilter:tagFilter:] : 152 -> 144
~ -[MXMSampleFilter initWithAttributeFilters:tagFilters:] : 468 -> 464
~ -[MXMSampleFilter addAttributeFilters:] : 312 -> 308
~ -[MXMSampleFilter matchesSample:] : 144 -> 132
~ -[MXMSampleFilter matchesSampleSet:] : 144 -> 132
~ -[MXMSampleFilter matchesSamplesWithAttribute:] : 136 -> 124
~ -[MXMSampleFilter matchesSamplesWithTag:] : 276 -> 280
~ -[MXMSampleFilter copyWithZone:] : 152 -> 144
~ -[MXMSampleFilter encodeWithCoder:] : 116 -> 108
~ -[MXMSampleFilter initWithCoder:] : 412 -> 392
~ -[MXMSampleFilter setTagFilters:] : 64 -> 12
~ -[MXMSampleFilter setAttributeFilters:] : 64 -> 12
~ -[MXMSampleTag domainNameString] : 96 -> 88
~ -[MXMSampleTag initWithDNString:] : 88 -> 84
~ -[MXMSampleTag initWithComponents:] : 80 -> 76
~ -[MXMSampleTag initWithTaxonomy:] : 108 -> 116
~ -[MXMSampleTag initWithCoder:] : 208 -> 200
~ -[MXMSampleTag description] : 160 -> 148
~ +[MXMProbeDisplay mainDescriptor] : 304 -> 280
~ ___33+[MXMProbeDisplay mainDescriptor]_block_invoke : 116 -> 108
~ -[MXMProbeDisplay init] : 120 -> 116
~ -[MXMProbeDisplay _beginUpdates] : 84 -> 88
~ -[MXMProbeDisplay _stopUpdates] : 84 -> 88
~ -[MXMProbe updateQueue] : 88 -> 68
~ -[MXMProbe _handleIncomingData:] : 276 -> 264
~ -[MXMProbe _setupWaitSemaphore] : 132 -> 128
~ -[MXMProbe sampleWithTimeout:stopReason:] : 620 -> 612
~ ___41-[MXMProbe sampleWithTimeout:stopReason:]_block_invoke : 112 -> 100
~ -[MXMProbe setUpdateQueue:] : 64 -> 12
~ -[MXMSample asMeasurementValue] : 160 -> 152
~ -[MXMSample asNumberValue] : 192 -> 180
~ -[MXMSample shortDesc] : 172 -> 160
~ -[MXMSample unit] : 56 -> 8
~ -[MXMSample initWithTag:attributes:doubleValue:unit:timestamp:] : 252 -> 256
~ -[MXMSample encodeWithCoder:] : 148 -> 140
~ -[MXMSample initWithCoder:] : 284 -> 272
~ -[MXMSample description] : 220 -> 204
~ -[MXMSample convertToUnit:] : 268 -> 248
~ +[MXMOSSignpostProbe probeHostSystemLogArchiveWithRelativeTimeInterval:] : 160 -> 152
~ +[MXMOSSignpostProbe probeHostSystemLogArchiveWithStartDate:endDate:] : 116 -> 120
~ +[MXMOSSignpostProbe probeHostSystemLogArchiveWithStartDate:endDate:startMachTime:stopMachTime:] : 140 -> 144
~ +[MXMOSSignpostProbe probeWithLogArchivePath:startDate:endDate:] : 128 -> 136
~ +[MXMOSSignpostProbe probeWithLogArchivePath:startDate:endDate:startMachTime:stopMachTime:] : 152 -> 160
~ -[MXMOSSignpostProbe initWithMode:] : 152 -> 164
~ -[MXMOSSignpostProbe initWithMode:logArchive:startDate:endDate:] : 184 -> 192
~ -[MXMOSSignpostProbe initWithMode:logArchive:startDate:endDate:startMachTime:stopMachTime:] : 28 -> 36
~ -[MXMOSSignpostProbe _setupProcessingFilter] : 392 -> 364
~ -[MXMOSSignpostProbe _setupProcessingBlocks] : 712 -> 724
~ ___44-[MXMOSSignpostProbe _setupProcessingBlocks]_block_invoke : 256 -> 268
~ ___44-[MXMOSSignpostProbe _setupProcessingBlocks]_block_invoke_2 : 96 -> 100
~ ___44-[MXMOSSignpostProbe _setupProcessingBlocks]_block_invoke_3 : 164 -> 176
~ ___44-[MXMOSSignpostProbe _setupProcessingBlocks]_block_invoke_4 : 164 -> 176
~ ___44-[MXMOSSignpostProbe _setupProcessingBlocks]_block_invoke_5 : 516 -> 460
~ -[MXMOSSignpostProbe _buildSampleSetWithData:tag:unit:attributes:signpostObject:] : 1644 -> 1512
~ -[MXMOSSignpostProbe _buildData:attributes:signpostEvent:] : 436 -> 416
~ -[MXMOSSignpostProbe _buildData:signpostInterval:] : 344 -> 452
~ -[MXMOSSignpostProbe _buildData:signpostAnimationInterval:] : 196 -> 204
~ -[MXMOSSignpostProbe _addAnimationFrameRateToData:fromSignpostAnimationInterval:] : 260 -> 252
~ -[MXMOSSignpostProbe _addAnimationFrameCountToData:fromSignpostAnimationInterval:] : 260 -> 252
~ -[MXMOSSignpostProbe _addAnimationRenderStatsToData:fromSignpostAnimationInterval:] : 736 -> 680
~ ___83-[MXMOSSignpostProbe _addAnimationRenderStatsToData:fromSignpostAnimationInterval:]_block_invoke : 200 -> 188
~ -[MXMOSSignpostProbe _addAnimationGlitchTimeRatioToData:fromSignpostAnimationInterval:] : 780 -> 740
~ ___87-[MXMOSSignpostProbe _addAnimationGlitchTimeRatioToData:fromSignpostAnimationInterval:]_block_invoke : 128 -> 120
~ -[MXMOSSignpostProbe _addAnimationNumberOfGlitchesToData:fromSignpostAnimationInterval:] : 824 -> 772
~ ___88-[MXMOSSignpostProbe _addAnimationNumberOfGlitchesToData:fromSignpostAnimationInterval:]_block_invoke : 144 -> 136
~ -[MXMOSSignpostProbe _addAnimationGlitchesTotalDurationToData:fromSignpostAnimationInterval:] : 1148 -> 1104
~ ___93-[MXMOSSignpostProbe _addAnimationGlitchesTotalDurationToData:fromSignpostAnimationInterval:]_block_invoke : 312 -> 308
~ -[MXMOSSignpostProbe _beginUpdates] : 748 -> 732
~ -[MXMOSSignpostProbe _stopUpdates] : 104 -> 112
~ -[MXMOSSignpostProbe sampleWithTimeout:stopReason:] : 476 -> 428
~ -[MXMOSSignpostProbe dealloc] : 108 -> 112
~ -[MXMSystemProbe init] : 96 -> 100
~ -[MXMSystemProbe _buildData:timestamp:processorCount:] : 140 -> 132
~ -[MXMSystemProbe _buildData:timestamp:cpuLoad:] : 320 -> 300
~ -[MXMSystemProbe _buildData:timestamp:loadInfo:] : 208 -> 196
~ -[MXMSystemProbe _prepareData] : 600 -> 572
~ -[MXMSystemProbe _beginUpdates] : 136 -> 140
~ -[MXMSystemProbe _stopUpdates] : 96 -> 100
~ -[MXMSystemProbe _pollSystemLoop] : 200 -> 192
~ -[MXMSystemProbe _gatherConstantSystemProperties] : 104 -> 108
~ -[MXMSystemProbe _pollSystemMainBody] : 128 -> 132
~ -[MXMSystemProbe _pollSystemHostProcessorInfoWithData:] : 804 -> 772
~ -[MXMSystemProbe _pollSystemLoadInformationWithData:] : 136 -> 152
~ -[MXMSampleData tags] : 324 -> 320
~ -[MXMSampleData samples] : 484 -> 472
~ -[MXMSampleData numberOfSets] : 296 -> 292
~ -[MXMSampleData numberOfSamples] : 60 -> 56
~ -[MXMSampleData init] : 128 -> 124
~ -[MXMSampleData initWithSet:] : 168 -> 164
~ -[MXMSampleData initWithSets:] : 272 -> 284
~ -[MXMSampleData sampleSetWithTag:attribute:] : 140 -> 132
~ -[MXMSampleData sampleSetWithTag:attributes:] : 412 -> 400
~ -[MXMSampleData initWithCoder:] : 252 -> 244
~ -[MXMSampleData copyWithZone:] : 120 -> 112
~ -[MXMSampleData mutableCopyWithZone:] : 120 -> 112
~ -[MXMSampleData countByEnumeratingWithState:objects:count:] : 508 -> 496
~ -[MXMSampleData _appendAttribute:] : 288 -> 284
~ -[MXMSampleData _appendSet:] : 680 -> 640
~ -[MXMSampleData setTagsToSampleSets:] : 64 -> 12
~ -[MXMMutableSampleData appendSample:] : 584 -> 532
~ -[MXMMutableSampleData appendFloatValue:tag:timestamp:] : 160 -> 152
~ -[MXMMutableSampleData appendDoubleValue:tag:timestamp:] : 160 -> 152
~ -[MXMMutableSampleData appendUnsignedIntValue:tag:timestamp:] : 156 -> 148
~ -[MXMMutableSampleData appendIntValue:tag:timestamp:] : 156 -> 148
~ -[MXMMutableSampleData appendIntegerValue:tag:timestamp:] : 156 -> 148
~ -[MXMMutableSampleData appendUnsignedIntegerValue:tag:timestamp:] : 156 -> 148
~ -[MXMOSSignpostMetric subsystem] : 124 -> 112
~ -[MXMOSSignpostMetric category] : 124 -> 112
~ -[MXMOSSignpostMetric name] : 124 -> 112
~ -[MXMOSSignpostMetric _shouldConstructProbe] : 108 -> 116
~ -[MXMOSSignpostMetric _constructProbe] : 464 -> 440
~ -[MXMOSSignpostMetric initWithSubsystem:category:name:processName:] : 400 -> 408
~ -[MXMOSSignpostMetric copyWithZone:] : 188 -> 220
~ -[MXMOSSignpostMetric encodeWithCoder:] : 208 -> 224
~ -[MXMOSSignpostMetric initWithCoder:] : 276 -> 284
~ -[MXMOSSignpostMetric didStartAtTime:startDate:] : 160 -> 164
~ -[MXMOSSignpostMetric didStartAtContinuousTime:absoluteTime:startDate:] : 196 -> 204
~ -[MXMOSSignpostMetric didStopAtContinuousTime:absoluteTime:stopDate:] : 180 -> 184
~ -[MXMOSSignpostMetric processName] : 16 -> 20
+ +[MXMEnergySampleTag allEnergySampleTags]
~ -[MXMInstrument setActive:] : 308 -> 300
~ -[MXMInstrument initWithInstrumentals:] : 212 -> 208
~ -[MXMInstrument _prepareIteration:options:instrumentals:errors:] : 648 -> 656
~ ___64-[MXMInstrument _prepareIteration:options:instrumentals:errors:]_block_invoke : 120 -> 124
~ -[MXMInstrument _setupAndRunWithIteration:spawnThread:attrs:pthread:returnCode:] : 2640 -> 2584
~ _MXMRunBlockIteration : 1580 -> 1508
~ -[MXMInstrument _transitionWithState:iteration:instrumentals:] : 724 -> 728
~ ___62-[MXMInstrument _transitionWithState:iteration:instrumentals:]_block_invoke : 656 -> 640
~ -[MXMInstrument startWithError:] : 1076 -> 1028
~ -[MXMInstrument stopWithError:] : 1096 -> 1092
~ -[MXMInstrument measureAutomatically:options:block:] : 2828 -> 2760
~ -[MXMInstrument _makePerfDataFromMXMResults:testName:] : 928 -> 884
~ -[MXMInstrument _valueWithOption:userOptions:] : 164 -> 156
~ -[MXMInstrument _defaultValueWithOption:] : 408 -> 404
~ -[MXMInstrument _validOptionKeys] : 244 -> 240
~ ___MXMQuiesceBeforeIteration_block_invoke : 168 -> 148
~ ___MXMUncacheBeforeIteration_block_invoke : 116 -> 112
~ ___MXMTerminateBeforeIteration_block_invoke : 116 -> 112
~ ___MXMStartPerformanceTraceCollection_block_invoke : 380 -> 332
~ ___MXMStartFunctionCoverageCollection_block_invoke : 300 -> 252
~ ___MXMStopPerformanceTraceCollection_block_invoke : 644 -> 600
~ ___MXMStopFunctionCoverageCollection_block_invoke : 308 -> 264
~ +[MXMSampleAttribute attributeWithName:stringValue:] : 108 -> 112
~ +[MXMSampleAttribute attributeWithName:numericValue:] : 108 -> 112
~ +[MXMSampleAttribute attributeWithName:valueType:value:] : 116 -> 120
~ -[MXMSampleAttribute initWithAttributeName:valueType:value:] : 344 -> 348
~ -[MXMSampleAttribute copyWithZone:] : 140 -> 132
~ -[MXMSampleAttribute encodeWithCoder:] : 136 -> 128
~ -[MXMSampleAttribute initWithCoder:] : 268 -> 260
~ -[MXMSampleAttribute isEqualToAttribute:] : 480 -> 440
~ -[MXMSampleAttribute description] : 192 -> 176
~ -[MXMProxyMetric _sampleMode].cold.1 : 120 -> 116
~ -[MXMResourceProbe _stopUpdates].cold.1 : 88 -> 84
~ -[MXMResourceProbe _pollAllProcesses:].cold.1 : 112 -> 108
~ -[MXMResourceProbe _pollTaskMachPortInformation:task:].cold.1 : 100 -> 96
~ -[MXMResourceProbe _pollBasicTaskInformation:pid:].cold.1 : 100 -> 96
~ -[MXMSampleSet(Stats) distance].cold.1 : 120 -> 116
~ -[MXMSampleSet _appendAttribute:].cold.1 : 92 -> 88
~ -[MXMMutableSampleSet appendSet:].cold.1 : 92 -> 88
~ -[MXMMutableSampleSet appendSample:].cold.1 : 92 -> 88
~ -[MXMCPUMetric harvestData:error:].cold.1 : 92 -> 88
~ -[MXMCPUMetric harvestData:error:].cold.2 : 92 -> 88
~ -[MXMCPUMetric harvestData:error:].cold.3 : 92 -> 88
~ -[MXMCPUMetric harvestData:error:].cold.4 : 92 -> 88
~ -[MXMMetric willStartAtEstimatedTime:].cold.1 : 92 -> 88
~ -[MXMMetric didStopAtTime:stopDate:].cold.1 : 92 -> 88
~ -[MXMMetric didStopAtContinuousTime:absoluteTime:stopDate:].cold.1 : 92 -> 88
~ -[MXMMetric harvestData:error:].cold.1 : 92 -> 88
~ -[MXMMetric harvestData:error:].cold.2 : 92 -> 88
~ -[MXMMetric harvestData:error:].cold.3 : 92 -> 88
~ -[MXMMetric harvestData:error:].cold.4 : 92 -> 88
~ -[MXMMetric harvestData:error:].cold.5 : 148 -> 144
~ -[MXMSampleTag isEqualToTag:].cold.1 : 128 -> 124
~ -[MXMProbeDisplay initWithDescriptor:].cold.1 : 92 -> 88
~ -[MXMProbeDisplay initWithDescriptor:].cold.2 : 92 -> 88
~ -[MXMProbeDisplay initWithDescriptor:].cold.3 : 128 -> 124
~ ___60-[MXMProbe updateNowUntilTimeout:updateHandler:stopHandler:]_block_invoke.cold.1 : 116 -> 112
~ -[MXMOSSignpostProbe _beginUpdates].cold.1 : 144 -> 136
~ -[MXMSystemProbe _pollSystemHostProcessorInfoWithData:].cold.1 : 80 -> 76
~ -[MXMSystemProbe _pollProcessorLoadInformationWithData:].cold.1 : 80 -> 76
~ -[MXMSystemProbe _pollProcessorLoadInformationWithData:].cold.2 : 80 -> 76
~ -[MXMSystemProbe _pollSystemLoadInformationWithData:].cold.1 : 80 -> 76
~ -[MXMMutableSampleData appendFloatValue:tag:timestamp:].cold.1 : 84 -> 80
~ -[MXMMutableSampleData appendDoubleValue:tag:timestamp:].cold.1 : 84 -> 80
~ -[MXMMutableSampleData appendUnsignedIntValue:tag:timestamp:].cold.1 : 84 -> 80
~ -[MXMMutableSampleData appendIntValue:tag:timestamp:].cold.1 : 84 -> 80
~ -[MXMMutableSampleData appendIntegerValue:tag:timestamp:].cold.1 : 84 -> 80
~ -[MXMMutableSampleData appendUnsignedIntegerValue:tag:timestamp:].cold.1 : 84 -> 80
~ -[MXMOSSignpostMetric _constructProbe].cold.1 : 108 -> 104
~ -[MXMOSSignpostMetric _constructProbe].cold.2 : 132 -> 128
~ -[MXMInstrument initWithInstrumentals:].cold.1 : 80 -> 76
~ -[MXMInstrument _setupAndRunWithIteration:spawnThread:attrs:pthread:returnCode:].cold.1 : 92 -> 88
~ -[MXMInstrument _setupAndRunWithIteration:spawnThread:attrs:pthread:returnCode:].cold.2 : 120 -> 116
~ -[MXMInstrument _setupAndRunWithIteration:spawnThread:attrs:pthread:returnCode:].cold.3 : 96 -> 92
~ -[MXMInstrument _setupAndRunWithIteration:spawnThread:attrs:pthread:returnCode:].cold.4 : 92 -> 88
~ -[MXMInstrument _setupAndRunWithIteration:spawnThread:attrs:pthread:returnCode:].cold.5 : 80 -> 76
~ -[MXMInstrument _transitionWithState:iteration:instrumentals:].cold.1 : 92 -> 88
~ -[MXMInstrument _transitionWithState:iteration:instrumentals:].cold.2 : 92 -> 88
~ -[MXMInstrument _transitionWithState:iteration:instrumentals:].cold.3 : 96 -> 92
~ -[MXMInstrument _transitionWithState:iteration:instrumentals:].cold.4 : 96 -> 92
~ ___62-[MXMInstrument _transitionWithState:iteration:instrumentals:]_block_invoke.cold.1 : 96 -> 92
~ ___62-[MXMInstrument _transitionWithState:iteration:instrumentals:]_block_invoke.cold.2 : 96 -> 92
~ ___62-[MXMInstrument _transitionWithState:iteration:instrumentals:]_block_invoke.cold.3 : 96 -> 92
~ ___62-[MXMInstrument _transitionWithState:iteration:instrumentals:]_block_invoke.cold.4 : 96 -> 92
~ -[MXMInstrument startWithError:].cold.1 : 96 -> 92
~ -[MXMInstrument stopWithError:].cold.1 : 80 -> 76
~ -[MXMInstrument stopWithError:].cold.2 : 116 -> 108
~ -[MXMInstrument measureAutomatically:options:block:].cold.1 : 96 -> 92
~ -[MXMInstrument measureAutomatically:options:block:].cold.2 : 96 -> 92
~ -[MXMInstrument measureAutomatically:options:block:].cold.3 : 92 -> 88
~ -[MXMInstrument measureAutomatically:options:block:].cold.4 : 92 -> 88
~ -[MXMInstrument measureAutomatically:options:block:].cold.5 : 108 -> 104
~ -[MXMInstrument measureAutomatically:options:block:].cold.6 : 80 -> 76
~ -[MXMInstrument measureAutomatically:options:block:].cold.7 : 80 -> 76
~ -[MXMInstrument measureAutomatically:options:block:].cold.8 : 116 -> 108
~ -[MXMSampleAttribute initWithAttributeName:valueType:value:].cold.1 : 92 -> 88
~ -[MXMSampleAttribute initWithAttributeName:valueType:value:].cold.2 : 88 -> 84
~ -[MXMSampleAttribute initWithAttributeName:valueType:value:].cold.3 : 88 -> 84
~ -[MXMSampleAttribute isEqualToAttribute:].cold.1 : 96 -> 92
CStrings:
+ "os_signpost end event process name"
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"<MXMDisplayProbePlatform>\""
- "@\"<MXMDisplayProbePlatformDelegate>\""
- "@\"<MXMDisplayProbePlatformDelegate>\"16@0:8"
- "@\"<MXMProbeDelegate>\""
- "@\"<MXMProbeableDevice>\""
- "@\"CADisplay\""
- "@\"MXMDisplayDescriptor\""
- "@\"MXMMetric\""
- "@\"MXMMutableSampleData\""
- "@\"MXMProbe\""
- "@\"MXMProxyMetric\""
- "@\"MXMSampleData\""
- "@\"MXMSampleFilter\""
- "@\"MXMSampleTag\""
- "@\"MXMSampleTimeSeries\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSOrderedSet\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSThread\""
- "@\"NSURL\""
- "@\"NSUnit\""
- "@\"NSXPCConnection\""
- "@\"OSActivityStream\""
- "@\"OSLogDevice\""
- "@\"SignpostSupportObjectExtractor\""
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8d16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@\"MXMDisplayDescriptor\"16@\"NSObject<OS_dispatch_queue>\"24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16q24"
- "@32@0:8Q16@?24"
- "@32@0:8^Q16Q24"
- "@32@0:8d16^Q24"
- "@36@0:8I16@20Q28"
- "@36@0:8f16@20Q28"
- "@36@0:8i16@20Q28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24^{__CVBuffer=}32"
- "@40@0:8@16@24d32"
- "@40@0:8@16d24^Q32"
- "@40@0:8@16q24@32"
- "@40@0:8Q16@24@?32"
- "@40@0:8Q16@24Q32"
- "@40@0:8Q16r^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v@}24@32"
- "@40@0:8d16@24Q32"
- "@40@0:8q16@24Q32"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24Q32Q40"
- "@48@0:8@16@24d32@40"
- "@48@0:8Q16@24@32@40"
- "@48@0:8^d16@24@32Q40"
- "@56@0:8@16@24@32@40@48"
- "@56@0:8@16@24@32Q40Q48"
- "@56@0:8@16@24d32@40Q48"
- "@64@0:8@16@24@32@40^d48Q56"
- "@64@0:8Q16@24@32@40Q48Q56"
- "@72@0:8@16@24@32@40^v48Q56Q64"
- "@?"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B24@0:8d16"
- "B24@0:8q16"
- "B32@0:8@\"NSDictionary\"16^@24"
- "B32@0:8@\"OSActivityStream\"16@\"NSArray\"24"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B32@0:8^@16^@24"
- "B40@0:8@\"OSActivityStream\"16@\"NSArray\"24@\"NSError\"32"
- "B40@0:8@16@24@32"
- "B56@0:8@\"OSActivityStream\"16@\"NSString\"24@\"OSLogDevice\"32q40@\"NSError\"48"
- "B56@0:8@16@24@32q40@48"
- "CPU"
- "CPUCores"
- "CPUCoresLogical"
- "CPUCoresPhysical"
- "CPUCycles"
- "CPUInstructions"
- "CPULoad"
- "CPULoadTask"
- "CPULoadThread"
- "CPUQos"
- "CPUQosBackground"
- "CPUQosDefault"
- "CPUQosLegacy"
- "CPUQosMaintenance"
- "CPUQosUserInitiated"
- "CPUQosUserInteractive"
- "CPUQosUtility"
- "CPUTicks"
- "CPUTicksIdle"
- "CPUTicksNice"
- "CPUTicksSystem"
- "CPUTicksUser"
- "CPUTime"
- "CPUTimeSystem"
- "CPUTimeUser"
- "Concate"
- "Exa"
- "Exbi"
- "GBs"
- "Gbs"
- "Gibi"
- "Giga"
- "IO"
- "IOLogicalWrites"
- "IOReads"
- "IOWrites"
- "Kibi"
- "Kilo"
- "MBs"
- "MXMCPUMetric"
- "MXMClockMetric"
- "MXMClockSampleTag"
- "MXMDiskMetric"
- "MXMDisplayDescriptor"
- "MXMDisplayProbePlatform"
- "MXMDisplayProbePlatformDelegate"
- "MXMDisplayProbe_iphoneOS_Internal"
- "MXMEnergySampleTag"
- "MXMInstrumental"
- "MXMMachUtils"
- "MXMMemoryMetric"
- "MXMMetric"
- "MXMMutableSampleData"
- "MXMMutableSampleSet"
- "MXMNetworkMetric"
- "MXMOSLogDeviceStore_Internal"
- "MXMOSLogDevice_Internal"
- "MXMOSLogProbe"
- "MXMOSSignpostMetric"
- "MXMOSSignpostProbe"
- "MXMOSSignpostSampleTag"
- "MXMProbe"
- "MXMProbeDelegate"
- "MXMProbeDisplay"
- "MXMProbeableDevice"
- "MXMProxyMetric"
- "MXMProxyProbe"
- "MXMProxyServiceManager"
- "MXMResourceProbe"
- "MXMSMachUtilitiesProtocol_Internal"
- "MXMSProxyFunctionCoverage_Internal"
- "MXMSProxyPerformanceTrace_Internal"
- "MXMSProxyProbeProtocol_Internal"
- "MXMSProxyQuiesceBeforeIteration_Internal"
- "MXMSProxyTerminateProcessesBeforeIteration_Internal"
- "MXMSProxyUncacheBeforeIteration_Internal"
- "MXMSample"
- "MXMSampleAttribute"
- "MXMSampleAttributeFilter"
- "MXMSampleData"
- "MXMSampleFilter"
- "MXMSampleSet"
- "MXMSampleTag"
- "MXMSampleTagFilter"
- "MXMSampleTimeSeries"
- "MXMSystemProbe"
- "MXMSystemSampleTag"
- "MXMUnitCycle"
- "MXMUnitEnergy"
- "MXMUnitFrame"
- "MXMUnitHitch"
- "MXMUnitInstruction"
- "MXMUnitMemory"
- "MXMUnitPacket"
- "MXMUtilizationSampleTag"
- "MXMVirtualMachineProbe"
- "Mbs"
- "Mebi"
- "Mega"
- "MetricMeasurementHelperProtocol_Internal"
- "NSCoding"
- "NSCopying"
- "NSFastEnumeration"
- "NSMutableCopying"
- "NSObject"
- "NSSecureCoding"
- "OSActivityStreamDelegate"
- "OSDeviceDelegate"
- "Pebi"
- "Peta"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "Q24@0:8d16"
- "Q40@0:8^{?=Q^@^Q[5Q]}16^@24Q32"
- "SIExtended"
- "Stats"
- "T#,R"
- "T@\"<MXMDisplayProbePlatformDelegate>\",W,N"
- "T@\"<MXMDisplayProbePlatformDelegate>\",W,N,V_delegate"
- "T@\"<MXMProbeDelegate>\",W,N,V_delegate"
- "T@\"<MXMProbeableDevice>\",R,N"
- "T@\"<MXMProbeableDevice>\",R,N,V_hostDevice"
- "T@\"<MetricMeasurementHelperProtocol_Internal>\",R"
- "T@\"CADisplay\",R,N,V_display"
- "T@\"MXMCPUMetric\",R,C,N"
- "T@\"MXMClockMetric\",R,N"
- "T@\"MXMClockSampleTag\",R,D,N,Gancestery"
- "T@\"MXMClockSampleTag\",R,N"
- "T@\"MXMDiskMetric\",R,C,N"
- "T@\"MXMDisplayDescriptor\",R,N"
- "T@\"MXMEnergyMetric\",R,C,N"
- "T@\"MXMEnergySampleTag\",R,C,N"
- "T@\"MXMInstrument\",R,C,D,N"
- "T@\"MXMInstrument\",R,D,N"
- "T@\"MXMInstrument\",R,N"
- "T@\"MXMMemoryMetric\",R,C,N"
- "T@\"MXMMetric\",R,&,V__underlyingMetric"
- "T@\"MXMMetric\",R,C"
- "T@\"MXMNetworkMetric\",R,C,N"
- "T@\"MXMOSLogDeviceStore_Internal\",R,N"
- "T@\"MXMOSLogProbe\",R,N"
- "T@\"MXMOSSignpostSampleTag\",R,C,N"
- "T@\"MXMProbe\",R,C"
- "T@\"MXMProxyMetric\",R,V_proxyMetric"
- "T@\"MXMProxyServiceManager\",R"
- "T@\"MXMSample\",R,N"
- "T@\"MXMSampleFilter\",&,N,V_filter"
- "T@\"MXMSampleFilter\",C,N,V_filter"
- "T@\"MXMSampleSet\",R,N"
- "T@\"MXMSampleTag\",R,C,N,V_parent"
- "T@\"MXMSampleTag\",R,N,V_tag"
- "T@\"MXMSampleTag\",R,V_tag"
- "T@\"MXMSampleTimeSeries\",R,&,V_timeIndex"
- "T@\"MXMSystemSampleTag\",R,C,N"
- "T@\"MXMUnitCycle\",R,C"
- "T@\"MXMUnitEnergy\",R,C,D,N"
- "T@\"MXMUnitEnergy\",R,C,D,N,GbaseUnit"
- "T@\"MXMUnitEnergy\",R,C,D,N,Gjoules"
- "T@\"MXMUnitEnergy\",R,C,D,N,Gnanojoules"
- "T@\"MXMUnitFrame\",R"
- "T@\"MXMUnitHitch\",R"
- "T@\"MXMUnitInstruction\",R,C,N"
- "T@\"MXMUnitInstruction\",R,C,N,GbaseUnit"
- "T@\"MXMUnitInstruction\",R,C,N,GkiloInstructions"
- "T@\"MXMUnitInstruction\",R,C,N,GmegaInstructions"
- "T@\"MXMUnitMemory\",R"
- "T@\"MXMUnitMemory\",R,Gbytes"
- "T@\"MXMUnitMemory\",R,Ggigabits"
- "T@\"MXMUnitMemory\",R,Ggigabytes"
- "T@\"MXMUnitMemory\",R,Gkibibits"
- "T@\"MXMUnitMemory\",R,Gkibibytes"
- "T@\"MXMUnitMemory\",R,Gkilobits"
- "T@\"MXMUnitMemory\",R,Gkilobytes"
- "T@\"MXMUnitMemory\",R,Gmegabits"
- "T@\"MXMUnitMemory\",R,Gmegabytes"
- "T@\"MXMUnitMemory\",R,Gnibbles"
- "T@\"MXMUnitPacket\",R,N,GbaseUnit"
- "T@\"MXMUtilizationSampleTag\",R,C,N"
- "T@\"NSArray\",&,V_cachedSamples"
- "T@\"NSArray\",&,V_enumSet"
- "T@\"NSArray\",R,C"
- "T@\"NSArray\",R,C,N"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_instrumentals"
- "T@\"NSData\",R,N,V_date"
- "T@\"NSData\",R,V_perfMetricsPerfdata"
- "T@\"NSMeasurement\",R,C,N"
- "T@\"NSMutableDictionary\",&,N,V_attributeFilters"
- "T@\"NSMutableDictionary\",&,N,V_tagsToSampleSets"
- "T@\"NSMutableDictionary\",R,N,V_attributesMap"
- "T@\"NSMutableDictionary\",R,N,V_devices"
- "T@\"NSNumber\",R,C,N"
- "T@\"NSNumber\",R,N"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_updateQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,V_instrumentalsQueue"
- "T@\"NSSet\",&,N,V_tagFilters"
- "T@\"NSSet\",C,N,V_tagPermutations"
- "T@\"NSSet\",R,C"
- "T@\"NSSet\",R,C,D,N"
- "T@\"NSSet\",R,C,D,N,Gancestery"
- "T@\"NSSet\",R,C,N"
- "T@\"NSSet\",R,C,N,V_attributes"
- "T@\"NSSet\",R,N"
- "T@\"NSString\",&,N,V_identifier"
- "T@\"NSString\",&,N,V_name"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_name"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_processName"
- "T@\"NSString\",R,V_performanceTraceFileSandboxExtensionToken"
- "T@\"NSThread\",&,V_pollingThread"
- "T@\"NSURL\",R,V_functionCoverageFileURL"
- "T@\"NSURL\",R,V_performanceTraceFileURL"
- "T@\"NSUnit\",R,C,N"
- "T@\"NSUnit\",R,V_unit"
- "T@\"NSUnitDuration\",R,N"
- "T@\"NSXPCConnection\",R,V__serviceConnection"
- "T@\"OSLogDevice\",&,N,V_rawDevice"
- "T@,R,C,N"
- "T@,R,C,N,V_value"
- "TB,R"
- "TB,R,N"
- "TB,R,N,Gfinite"
- "TB,R,N,Gmain"
- "TB,R,V_didQuiesce"
- "TB,V__shouldStop"
- "TB,V__updating"
- "TQ,N,V_preferredSampleMode"
- "TQ,R"
- "TQ,R,N"
- "TQ,R,N,V_length"
- "TQ,R,N,V_timestamp"
- "TQ,R,N,V_valueType"
- "T^d,R"
- "T^v,N,V_underlyingBuffer"
- "T^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v@},V_currentIteration"
- "T^{?=QQ},N,V_index"
- "Td,R,N"
- "Tebi"
- "Tera"
- "Tq,N,V_underlyingBufferLength"
- "Tq,R,N"
- "Tq,R,N,V_valueType"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^d16@0:8"
- "^v"
- "^v16@0:8"
- "^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v@}"
- "^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v@}16@0:8"
- "^{?=QQ}"
- "^{?=QQ}16@0:8"
- "^{_NSZone=}16@0:8"
- "^{mach_timebase_info=II}16@0:8"
- "__serviceConnection"
- "__shouldStop"
- "__underlyingMetric"
- "__updating"
- "_absoluteTimeWithNanoseconds:"
- "_activityStream"
- "_addAnimationFrameCountToData:fromSignpostAnimationInterval:"
- "_addAnimationFrameRateToData:fromSignpostAnimationInterval:"
- "_addAnimationGlitchTimeRatioToData:fromSignpostAnimationInterval:"
- "_addAnimationGlitchesTotalDurationToData:fromSignpostAnimationInterval:"
- "_addAnimationNumberOfGlitchesToData:fromSignpostAnimationInterval:"
- "_addAnimationRenderStatsToData:fromSignpostAnimationInterval:"
- "_allDescriptors"
- "_appendAbsoluteTime:"
- "_appendAttribute:"
- "_appendData:"
- "_appendDoubleValue:timestamp:"
- "_appendSample:"
- "_appendSet:"
- "_attributes"
- "_beginUpdates"
- "_build"
- "_buildData:attributes:signpostEvent:"
- "_buildData:signpostAnimationInterval:"
- "_buildData:signpostInterval:"
- "_buildData:timestamp:cpuInfo:"
- "_buildData:timestamp:cpuLoad:"
- "_buildData:timestamp:hostInfo:"
- "_buildData:timestamp:loadInfo:"
- "_buildData:timestamp:mach_space_basicinfo:"
- "_buildData:timestamp:pm_networking_stats:"
- "_buildData:timestamp:processorCount:"
- "_buildData:timestamp:rusage:"
- "_buildData:timestamp:taskinfo:"
- "_buildSampleSetWithData:tag:unit:attributes:signpostObject:"
- "_cachedSamples"
- "_collectedData"
- "_constructProbe"
- "_convertMetricsToSampleData:"
- "_currentIteration"
- "_dataMatchingFilter:"
- "_date"
- "_defaultValueWithOption:"
- "_delegate"
- "_devices"
- "_didQuiesce"
- "_didRecieveData:"
- "_display"
- "_displayDescriptor"
- "_displayIndexWithDescriptor:"
- "_endDate"
- "_enumSet"
- "_extractor"
- "_filter"
- "_finishedProcessingSema"
- "_functionCoverageFileURL"
- "_gatherConstantSystemProperties"
- "_getProbe"
- "_handleIncomingData:"
- "_hostDevice"
- "_identifier"
- "_impl"
- "_instrumentals"
- "_instrumentalsQueue"
- "_lastSample"
- "_length"
- "_logArchivePath"
- "_loop"
- "_makeInstrumentalsForIteration:shouldCopy:"
- "_makePerfDataFromMXMResults:testName:"
- "_matchesSampleAttributeNameWithName:"
- "_matchesSampleAttributeValueTypeWithAttributeValueType:"
- "_matchesSampleAttributeValueWithValue:"
- "_matchingNumericAttributeValues"
- "_matchingStringAttributeValues"
- "_mode"
- "_name"
- "_nanosecondsWithAbsoluteTime:"
- "_nanosecondsWithContinuousTime:"
- "_parent"
- "_perfMetricsPerfdata"
- "_performanceTraceFileSandboxExtensionToken"
- "_performanceTraceFileURL"
- "_pollAllProcesses:"
- "_pollBasicTaskInformation:pid:"
- "_pollDisplayForSample"
- "_pollMain"
- "_pollMainBody"
- "_pollProcessNetworkingStatsWithData:pid:task:"
- "_pollProcessResourceUsageWithData:pid:"
- "_pollProcessWithData:pid:"
- "_pollProcessorLoadInformationWithData:"
- "_pollRate"
- "_pollSystemBatteryWithData:"
- "_pollSystemHostProcessorInfoWithData:"
- "_pollSystemLoadInformationWithData:"
- "_pollSystemLoop"
- "_pollSystemMainBody"
- "_pollSystemThermalsWithData:"
- "_pollTaskMachPortInformation:task:"
- "_pollingThread"
- "_preferredSampleMode"
- "_prepareData"
- "_prepareIteration:options:instrumentals:errors:"
- "_prepareUnderlyingBufferSizeWithAdditionalBytes:"
- "_probe"
- "_processIdentifierWithProcessName:error:"
- "_processName"
- "_processNameWithBundleIdentifier:"
- "_proxyMetric"
- "_proxyObject"
- "_queue"
- "_quiesceBeforeIteration:timeout:response:"
- "_quiesceBeforeIterationHelper:timeout:response:"
- "_rawDevice"
- "_remoteProbe"
- "_sampleFromMetricMonitorWithProxyMetric:timeout:response:"
- "_sampleFromMetricMonitorWithProxyMetric:timeout:stopReason:"
- "_sampleMode"
- "_sampleSetsWithTag:"
- "_sampleWithProxyMetric:timeout:response:"
- "_sampleWithProxyMetric:timeout:stopReason:"
- "_serviceConnection"
- "_setupAndRunWithIteration:spawnThread:attrs:pthread:returnCode:"
- "_setupMetricMonitorWithProxyMetric:processNames:response:"
- "_setupProcessingBlocks"
- "_setupProcessingFilter"
- "_setupWaitSemaphore"
- "_shouldAlwaysWrapInProxy"
- "_shouldConstructProbe"
- "_shouldNeverWrapInProxy"
- "_shouldStop"
- "_shouldWrapInProxy"
- "_start"
- "_startDate_semaphore"
- "_startFunctionCoverageCollection:response:"
- "_startFunctionCoverageCollectionHelper:response:"
- "_startPerformanceTrace:response:"
- "_startPerformanceTraceHelper:response:"
- "_stop"
- "_stopDate_semaphore"
- "_stopFunctionCoverageCollection:"
- "_stopFunctionCoverageCollectionHelper:"
- "_stopHandler"
- "_stopPerformanceTrace:"
- "_stopPerformanceTraceHelper:"
- "_stopUpdates"
- "_stopWaiter"
- "_stream"
- "_tagPermutations"
- "_tagsToSampleSets"
- "_teardownMetricMonitorWithProxyMetric:response:"
- "_terminateProcessesBeforeIteration:response:"
- "_terminateProcessesBeforeIterationHelper:response:"
- "_time"
- "_timebase"
- "_timestamp"
- "_transitionWithState:iteration:instrumentals:"
- "_uncacheBeforeIteration:response:"
- "_uncacheBeforeIterationHelper:response:"
- "_underlyingBufferLength"
- "_underlyingMetric"
- "_underlyingValue"
- "_underlyingValueLength"
- "_unitWithTag:"
- "_updateHandler"
- "_updateQueue"
- "_updateThread"
- "_updating"
- "_validOptionKeys"
- "_value"
- "_valueType"
- "_valueWithOption:userOptions:"
- "_version"
- "_wakeWithPhrase:response:"
- "absoluteString"
- "absoluteTime"
- "active"
- "activeInstrument"
- "activityStream:deviceUDID:deviceID:status:error:"
- "activityStream:results:"
- "activityStream:results:error:"
- "addAttributeFilters:"
- "addObject:"
- "addObjectsFromArray:"
- "allEnergyTags"
- "allKeys"
- "allObjects"
- "allTime"
- "allUtilization"
- "allValues"
- "ancestery"
- "aneEnergyProcess"
- "animationFrameCount"
- "animationFrameRate"
- "animationGPUTimeP90"
- "animationGlitchTimeRatio"
- "animationGlitchesTotalDuration"
- "animationNonFirstFrameGlitchTimeRatioAdjusted"
- "animationNonFirstFrameGlitchesTotalDuration"
- "animationNonFirstFrameNumberOfGlitches"
- "animationNumberOfGlitches"
- "animationNumberOfOffscreenPassesP90"
- "animationPerAppNonFirstFrameGlitchTimeRatioAdjusted"
- "animationPerAppNonFirstFrameGlitchesTotalDuration"
- "animationPerAppNonFirstFrameNumberOfGlitches"
- "animationRenderGPUTimeP90"
- "animationRenderTimeP90"
- "animationUpdateTimeP90"
- "anyObject"
- "appendAttribute:"
- "appendAttributes:"
- "appendData:"
- "appendDoubleValue:tag:timestamp:"
- "appendDoubleValue:timestamp:"
- "appendFloatValue:tag:timestamp:"
- "appendFloatValue:timestamp:"
- "appendIntValue:tag:timestamp:"
- "appendIntValue:timestamp:"
- "appendIntegerValue:tag:timestamp:"
- "appendIntegerValue:timestamp:"
- "appendMetricSample:name:tag:unit:conversionFactor:processName:pidNumber:toData:timestamp:"
- "appendSample:"
- "appendSet:"
- "appendUnsignedIntValue:tag:timestamp:"
- "appendUnsignedIntValue:timestamp:"
- "appendUnsignedIntegerValue:tag:timestamp:"
- "appendUnsignedIntegerValue:timestamp:"
- "array"
- "arrayWithCapacity:"
- "arrayWithObject:"
- "arrayWithObjects:count:"
- "asMeasurementValue"
- "asNumberValue"
- "attributeFilterWithName:"
- "attributeFilters"
- "attributeWithName:"
- "attributeWithName:numericValue:"
- "attributeWithName:stringValue:"
- "attributeWithName:valueType:"
- "attributeWithName:valueType:value:"
- "attributes"
- "attributesMap"
- "autorelease"
- "baseUnit"
- "beginEvent"
- "bits"
- "boolValue"
- "build"
- "bundleExecutable"
- "bundleForClass:"
- "bundleProxyForIdentifier:"
- "bytes"
- "bytesReadProcess"
- "bytesWrittenProcess"
- "cStringUsingEncoding:"
- "cachedSamples"
- "cancel"
- "category"
- "class"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "conformsToProtocol:"
- "connectedDevices"
- "containsObject:"
- "containsTag:"
- "containsValueForKey:"
- "continuousTime"
- "contributingPidsForProcessName:"
- "convertToUnit:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "cpuEnergyProcess"
- "cpuInstructionsProcess"
- "currentHandler"
- "currentIteration"
- "currentProcess"
- "currentThread"
- "cycles"
- "d"
- "d16@0:8"
- "d24@0:8Q16"
- "dataMatchingFilter:"
- "dataWithBytes:length:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "date"
- "dateByAddingTimeInterval:"
- "dateWithTimeIntervalSinceNow:"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeBytesForKey:returnedLength:"
- "decodeInt64ForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultCenter"
- "delegate"
- "description"
- "descriptors"
- "devices"
- "dictionary"
- "dictionaryWithCapacity:"
- "dictionaryWithObjects:forKeys:count:"
- "didQuiesce"
- "didStartAtContinuousTime:absoluteTime:startDate:"
- "didStartAtTime:startDate:"
- "didStopAtContinuousTime:absoluteTime:stopDate:"
- "didStopAtTime:stopDate:"
- "display"
- "displayId"
- "displays"
- "distance"
- "domainNameString"
- "doubleValue"
- "doubleValues"
- "duration"
- "durationMs"
- "durationNanoseconds"
- "encodeBool:forKey:"
- "encodeBytes:length:forKey:"
- "encodeInt64:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endEvent"
- "endMachContinuousTime"
- "enumSet"
- "enumerateIndexesUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "exabits"
- "exabytes"
- "exbibits"
- "exbibytes"
- "exceptionWithName:reason:userInfo:"
- "filter"
- "filterWithAttributeFilter:"
- "filterWithAttributeFilter:tagFilter:"
- "filterWithAttributeFilters:"
- "filterWithTagFilter:"
- "filterWithTagFilters:"
- "finite"
- "firstDoubleValue"
- "firstObject"
- "flattenArray"
- "floatValue"
- "frameCount"
- "frameRate"
- "frameStatisticsForDisplayID:"
- "framesPerSecond"
- "functionCoverageFileURL"
- "geoMean"
- "gibibits"
- "gibibytes"
- "gigaCycles"
- "gigaInstructions"
- "gigabits"
- "gigabytes"
- "glitchTimeRatioMsPerS"
- "glitches"
- "gpuEnergyProcess"
- "gpuTime"
- "halfbytes"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "harvestData:error:"
- "hash"
- "hostDevice"
- "i32@0:8r*16^@24"
- "identifier"
- "index"
- "indexOfObject:"
- "infoDictionary"
- "init"
- "initInternal"
- "initPrivateWithDescriptor:queue:"
- "initWithAbsoluteTimeSeries:length:"
- "initWithAttribute:"
- "initWithAttributeFilter:"
- "initWithAttributeFilter:tagFilter:"
- "initWithAttributeFilters:"
- "initWithAttributeFilters:tagFilters:"
- "initWithAttributeName:"
- "initWithAttributeName:numericValue:"
- "initWithAttributeName:numericValues:"
- "initWithAttributeName:stringValue:"
- "initWithAttributeName:stringValues:"
- "initWithAttributeName:valueType:"
- "initWithAttributeName:valueType:value:"
- "initWithBlock:"
- "initWithBundleIdentifier:"
- "initWithCoder:"
- "initWithCoefficient:"
- "initWithComponents:"
- "initWithContinuousTimeSeries:length:"
- "initWithDNString:"
- "initWithDescriptor:"
- "initWithDisplay:"
- "initWithDoubleValue:unit:"
- "initWithEntries:"
- "initWithIdentifier:"
- "initWithIdentifier:filter:"
- "initWithInstrumentals:"
- "initWithLogArchive:"
- "initWithLogArchive:startDate:endDate:"
- "initWithMetric:"
- "initWithMode:"
- "initWithMode:logArchive:startDate:endDate:"
- "initWithMode:logArchive:startDate:endDate:startMachTime:stopMachTime:"
- "initWithName:identifier:"
- "initWithOSLogDevice:"
- "initWithProcessIdentifier:"
- "initWithProcessName:"
- "initWithProcessNames:"
- "initWithProxyMetric:"
- "initWithServiceName:"
- "initWithSet:"
- "initWithSets:"
- "initWithSubsystem:"
- "initWithSubsystem:category:"
- "initWithSubsystem:category:name:"
- "initWithSubsystem:category:name:processName:"
- "initWithSymbol:"
- "initWithSymbol:converter:"
- "initWithTag:"
- "initWithTag:allowDescendents:"
- "initWithTag:attributes:doubleValue:"
- "initWithTag:attributes:doubleValue:unit:"
- "initWithTag:attributes:doubleValue:unit:timestamp:"
- "initWithTag:attributes:pixelBufferValue:"
- "initWithTag:unit:attributes:"
- "initWithTagFilter:"
- "initWithTagFilters:"
- "initWithTarget:selector:object:"
- "initWithTargetDevice:"
- "initWithTaxonomy:"
- "initWithTime:tag:unit:attributes:"
- "initWithTime:tag:unit:attributes:doubleValues:length:"
- "initWithTime:tag:unit:attributes:values:length:valueSize:"
- "initWithTimeSeries:tag:unit:length:"
- "instructions"
- "instrument"
- "instrumentThread"
- "instrumentWithInstrumentals:"
- "instrumentals"
- "instrumentalsQueue"
- "intValue"
- "integerValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isCancelled"
- "isEqual:"
- "isEqualTo:"
- "isEqualToAttribute:"
- "isEqualToNumber:"
- "isEqualToOrderedSet:"
- "isEqualToSet:"
- "isEqualToString:"
- "isEqualToTag:"
- "isFinished"
- "isFinite"
- "isKindOfClass:"
- "isMain"
- "isMemberOfClass:"
- "isProxy"
- "isSubsetOfOrderedSet:"
- "isSubsetOfSet:"
- "joules"
- "kBs"
- "kbs"
- "kibibits"
- "kibibytes"
- "kiloCycles"
- "kiloInstructions"
- "kilobits"
- "kilobytes"
- "lastDoubleValue"
- "lastObject"
- "lastPathComponent"
- "length"
- "load"
- "machPort"
- "main"
- "mainDescriptor"
- "mainDisplay"
- "matchesSample:"
- "matchesSampleSet:"
- "matchesSampleWithAttribute:"
- "matchesSampleWithTag:"
- "matchesSamplesWithAttribute:"
- "matchesSamplesWithAttributes:"
- "matchesSamplesWithTag:"
- "max"
- "measureAutomatically:block:"
- "measureAutomatically:options:block:"
- "measureBlock:"
- "measureWithOptions:block:"
- "measurementByConvertingToUnit:"
- "mebibits"
- "mebibytes"
- "megaCycles"
- "megaInstructions"
- "megabits"
- "megabytes"
- "memory"
- "memoryDirtied"
- "memoryLeak"
- "memoryPeakPhysicalInterval"
- "memoryPeakPhysicalLifetime"
- "memoryPhysical"
- "memoryResident"
- "memorySwapped"
- "memoryVirtual"
- "memoryWired"
- "microseconds"
- "milliseconds"
- "min"
- "mutableCopy"
- "mutableCopyWithZone:"
- "nanojoules"
- "nanoseconds"
- "network"
- "networkRecievedBytes"
- "networkRecievedPackets"
- "networkSentBytes"
- "networkSentPackets"
- "nibbles"
- "nonFirstFrameContributedGlitches:"
- "nonFirstFrameGlitchTimeRatioAdjustedMsPerS"
- "nonFirstFrameGlitches"
- "number1Name"
- "number1Value"
- "number2Name"
- "number2Value"
- "numberOfSamples"
- "numberOfSets"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "numericValue"
- "numericValues"
- "nybbles"
- "nybles"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "octets"
- "offscreenPassCount"
- "orderedSetWithArray:"
- "overrunIntervals:"
- "p90"
- "packets"
- "parent"
- "pebibits"
- "pebibytes"
- "perfMetricsPerfdata"
- "performPreIterationActions"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performanceTraceFileSandboxExtensionToken"
- "performanceTraceFileURL"
- "petabits"
- "petabytes"
- "pollingThread"
- "postNotificationName:object:"
- "preferredSampleMode"
- "prepareWithOptions:error:"
- "probeDidStartUpdating:"
- "probeDidStop:reason:"
- "probeDidUpdate:data:stop:"
- "probeHostLive"
- "probeHostOSLog"
- "probeHostSystemLogArchiveWithRelativeTimeInterval:"
- "probeHostSystemLogArchiveWithStartDate:endDate:"
- "probeHostSystemLogArchiveWithStartDate:endDate:startMachTime:stopMachTime:"
- "probeWithDescriptor:"
- "probeWithLogArchivePath:"
- "probeWithLogArchivePath:startDate:endDate:"
- "probeWithLogArchivePath:startDate:endDate:startMachTime:stopMachTime:"
- "processID"
- "processIdentifier"
- "processLogArchiveWithPath:startDate:endDate:errorOut:"
- "processMetrics"
- "processName"
- "processNames"
- "processNotificationsWithIntervalTimeoutInSeconds:shouldCalculateAnimationFramerate:targetQueue:errorOut:"
- "proxyMetric"
- "q"
- "q16@0:8"
- "range"
- "rawDevice"
- "refreshRate"
- "relativeStandardDeviation"
- "release"
- "renderAndGPUTime"
- "renderTime"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "root"
- "sampleSetWithTag:attribute:"
- "sampleSetWithTag:attributes:"
- "sampleSetsWithTag:"
- "sampleWithIndex:"
- "sampleWithTimeout:"
- "sampleWithTimeout:stopReason:"
- "samples"
- "self"
- "semioctets"
- "setActive:"
- "setAnimationIntervalCompletionProcessingBlock:"
- "setAttributeFilters:"
- "setByAddingObject:"
- "setByAddingObjectsFromArray:"
- "setByAddingObjectsFromSet:"
- "setCachedSamples:"
- "setCurrentIteration:"
- "setDelegate:"
- "setDevice:"
- "setDeviceDelegate:"
- "setEmitEventProcessingBlock:"
- "setEnumSet:"
- "setFilter:"
- "setIdentifier:"
- "setIndex:"
- "setIntervalCompletionProcessingBlock:"
- "setName:"
- "setObject:atIndexedSubscript:"
- "setObject:forKeyedSubscript:"
- "setPollingThread:"
- "setPreferredSampleMode:"
- "setProcessingCompletionBlock:"
- "setRawDevice:"
- "setRemoteObjectInterface:"
- "setSubsystemCategoryFilter:"
- "setTagFilters:"
- "setTagPermutations:"
- "setTagsToSampleSets:"
- "setUnderlyingBuffer:"
- "setUnderlyingBufferLength:"
- "setUpdateQueue:"
- "setWithArray:"
- "setWithObject:"
- "setWithObjects:"
- "set_shouldStop:"
- "set_updating:"
- "shared"
- "shortDesc"
- "signpostId"
- "standardDeviation"
- "start"
- "startMachContinuousTime"
- "startNanoseconds"
- "startWithError:"
- "stop"
- "stopProcessing"
- "stopUpdates"
- "stopWithError:"
- "streamDidFail:error:"
- "streamDidStart:"
- "streamDidStop:"
- "string1Name"
- "string1Value"
- "string2Name"
- "string2Value"
- "stringByAppendingString:"
- "stringValue"
- "stringValues"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "subsystem"
- "sum"
- "superclass"
- "supportsSecureCoding"
- "symbol"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "tagFilters"
- "tagPermutations"
- "tags"
- "tebibits"
- "tebibytes"
- "telemetryNumber1"
- "telemetryNumber2"
- "terabits"
- "terabytes"
- "tetrades"
- "timeIndex"
- "timeRatio"
- "timeRatioMSPerSForOverrunIntervals:applyPerceptionAdjustments:"
- "timestamp"
- "underlyingBuffer"
- "underlyingBufferLength"
- "unsignedIntegerValue"
- "unsignedValue"
- "updateNowUntilStopped"
- "updateNowUntilStoppedWithUpdateHandler:"
- "updateNowUntilStoppedWithUpdateHandler:stopHandler:"
- "updateNowUntilTimeout:"
- "updateNowUntilTimeout:updateHandler:"
- "updateNowUntilTimeout:updateHandler:stopHandler:"
- "updateQueue"
- "updateTime"
- "updating"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"<MXMDisplayProbePlatformDelegate>\"16"
- "v24@0:8@\"MXMProbe\"16"
- "v24@0:8@\"MXMSampleData\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"OSActivityStream\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSURL\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSURL\"@\"NSString\"@\"NSError\"@\"NSError\"@\"NSError\"@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8^v16"
- "v24@0:8^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v@}16"
- "v24@0:8^{?=QQ}16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@16I24"
- "v28@0:8@16i24"
- "v28@0:8I16Q20"
- "v28@0:8f16Q20"
- "v28@0:8i16Q20"
- "v32@0:8@\"MXMProbe\"16Q24"
- "v32@0:8@\"MXMProxyMetric\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\"@\"NSError\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\">24"
- "v32@0:8@\"OSActivityStream\"16@\"NSError\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8@16i24I28"
- "v32@0:8@?16@?24"
- "v32@0:8Q16@\"NSDate\"24"
- "v32@0:8Q16@24"
- "v32@0:8Q16Q24"
- "v32@0:8d16@?24"
- "v32@0:8d16Q24"
- "v32@0:8q16Q24"
- "v36@0:8@16Q24I32"
- "v40@0:8@\"MXMProbe\"16@\"MXMSampleData\"24^B32"
- "v40@0:8@\"MXMProxyMetric\"16@\"NSArray\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"MXMProxyMetric\"16d24@?<v@?@\"MXMSampleData\"Q@\"NSError\">32"
- "v40@0:8@\"MXMProxyMetric\"16d24@?<v@?@\"PPSMetricCollection\"Q@\"NSError\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@24^B32"
- "v40@0:8@16Q24^{?=iQQQQ}32"
- "v40@0:8@16Q24^{ipc_info_space_basic=IIII[2I]}32"
- "v40@0:8@16Q24^{proc_taskinfo=QQQQQQiiiiiiiiiiii}32"
- "v40@0:8@16Q24^{processor_basic_info=iiii(?=ii)}32"
- "v40@0:8@16Q24^{processor_cpu_load_info=[4I]}32"
- "v40@0:8@16Q24^{processor_set_load_info=iiii}32"
- "v40@0:8@16Q24^{rusage_info_v6=[16C]QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ[9Q]}32"
- "v40@0:8@16Q24^{vm_statistics64=IIIIQQQQQQQQQIIQQQQIIIIQQQQQQQQQQQQQ}32"
- "v40@0:8@16d24@?32"
- "v40@0:8Q16Q24@\"NSDate\"32"
- "v40@0:8Q16Q24@32"
- "v40@0:8d16@?24@?32"
- "v40@0:8d16d24@?32"
- "v40@0:8d16d24@?<v@?B@\"NSError\">32"
- "v48@0:8^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v@}16@24@32@40"
- "v52@0:8^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v@}16B24^{_opaque_pthread_attr_t=q[56c]}28^^{_opaque_pthread_t}36^Q44"
- "v88@0:8@16@24@32@40d48@56@64@72Q80"
- "valueForKey:"
- "values"
- "version"
- "waitForeverUntilStopped"
- "waitUntilStoppedWithTimeout:"
- "wake"
- "willStartAtEstimatedTime:"
- "willStop"
- "zone"
- "{?=\"timestamp\"d\"frameCount\"Q}"
- "{?=dQ}16@0:8"

```
