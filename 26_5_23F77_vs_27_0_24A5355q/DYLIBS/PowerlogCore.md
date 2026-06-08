## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`

```diff

-3031.122.1.0.0
-  __TEXT.__text: 0xe6704
-  __TEXT.__auth_stubs: 0x1ac0
-  __TEXT.__objc_methlist: 0x8ad8
-  __TEXT.__const: 0x1b70
-  __TEXT.__cstring: 0x3d012
-  __TEXT.__oslogstring: 0x7ef8
-  __TEXT.__gcc_except_tab: 0x2944
-  __TEXT.__unwind_info: 0x3030
-  __TEXT.__objc_classname: 0x90f
-  __TEXT.__objc_methname: 0x1319e
-  __TEXT.__objc_methtype: 0x1917
-  __TEXT.__objc_stubs: 0xfb40
-  __DATA_CONST.__got: 0x7a8
-  __DATA_CONST.__const: 0x2598
-  __DATA_CONST.__objc_classlist: 0x350
+3468.0.0.502.1
+  __TEXT.__text: 0xe5320
+  __TEXT.__objc_methlist: 0x9698
+  __TEXT.__const: 0x1b68
+  __TEXT.__cstring: 0x3e989
+  __TEXT.__oslogstring: 0x880f
+  __TEXT.__gcc_except_tab: 0x297c
+  __TEXT.__unwind_info: 0x3090
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x2500
+  __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_nlclslist: 0x80
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x51c8
+  __DATA_CONST.__weak_got: 0x8
+  __DATA_CONST.__objc_selrefs: 0x58f0
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x2b0
-  __DATA_CONST.__objc_arraydata: 0x3f1d0
-  __AUTH_CONST.__auth_got: 0xd78
-  __AUTH_CONST.__const: 0x2440
-  __AUTH_CONST.__cfstring: 0x62820
-  __AUTH_CONST.__objc_const: 0x9470
-  __AUTH_CONST.__objc_intobj: 0x4968
-  __AUTH_CONST.__objc_doubleobj: 0x12d0
+  __DATA_CONST.__objc_superrefs: 0x2d0
+  __DATA_CONST.__objc_arraydata: 0x40178
+  __DATA_CONST.__got: 0x7e8
+  __AUTH_CONST.__const: 0x2460
+  __AUTH_CONST.__cfstring: 0x64e00
+  __AUTH_CONST.__objc_const: 0xa9a0
+  __AUTH_CONST.__weak_auth_got: 0x10
+  __AUTH_CONST.__objc_intobj: 0x4a58
+  __AUTH_CONST.__objc_doubleobj: 0x1390
   __AUTH_CONST.__objc_arrayobj: 0x1158
-  __AUTH_CONST.__objc_dictobj: 0xf190
-  __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x658
+  __AUTH_CONST.__objc_dictobj: 0xf438
+  __AUTH_CONST.__auth_got: 0xd98
+  __AUTH.__objc_data: 0x500
+  __DATA.__objc_ivar: 0x7c4
   __DATA.__data: 0x4a0
-  __DATA.__bss: 0x1621
+  __DATA.__bss: 0x1739
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x1cc0
+  __DATA_DIRTY.__objc_data: 0x1db0
   __DATA_DIRTY.__data: 0x28
-  __DATA_DIRTY.__bss: 0x1160
+  __DATA_DIRTY.__bss: 0x1138
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/PowerlogControl.framework/PowerlogControl
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
+  - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libIOAccessoryManager.dylib
   - /usr/lib/libIOReport.dylib

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D2548722-21FD-370A-86E1-EBF6CC3C4D45
-  Functions: 4633
-  Symbols:   16339
-  CStrings:  30265
+  UUID: D441FBB2-BC43-374A-BA2D-B5E35CB828A8
+  Functions: 4908
+  Symbols:   16975
+  CStrings:  27132
 
Symbols:
+ +[PLAppDeletion _appDeletionQueue]
+ +[PLAppDeletion _appDeletionQueue].cold.1
+ +[PLContextualizedMetricData fromDictionary:]
+ +[PLContextualizedMetricData supportsSecureCoding]
+ +[PLContextualizedMetrics fromDictionary:]
+ +[PLContextualizedMetrics supportsSecureCoding]
+ +[PLGestaltUtilities hasPencil]
+ +[PLGestaltUtilities hasPencil].cold.1
+ +[PLOperator dddOverrideDateInPayload:subsystem:category:]
+ +[PLStateInterval intervalFromDictionary:]
+ +[PLStorageCache bgsqlCacheLimit]
+ +[PLStorageCache isBGSQLEntryKey:]
+ +[PLSubmissionConfig taskingTableGroups]
+ +[PLTimeChunkInterval chunksForTimeRangeStart:end:chunkDuration:]
+ +[PLTimeChunkInterval defaultChunksForEndTime:]
+ +[PLTimeChunkInterval intervalWithStartTimestamp:endTimestamp:chunkIndex:]
+ +[PLTimeChunkInterval supportsSecureCoding]
+ +[SignpostReaderHelper extractStateIntervalsFromSignpostData:]
+ -[PLContextualizedMetricData .cxx_destruct]
+ -[PLContextualizedMetricData activationsOutput]
+ -[PLContextualizedMetricData activations]
+ -[PLContextualizedMetricData addActivationDuration:foreground:activationFlag:]
+ -[PLContextualizedMetricData addExitWithForeground:domain:code:]
+ -[PLContextualizedMetricData addExtendedLaunchDuration:foreground:]
+ -[PLContextualizedMetricData addGlitchWithDuration:scrollDuration:glitchCount:isScrollStart:glitchRatio:animationDuration:]
+ -[PLContextualizedMetricData addHangDuration:]
+ -[PLContextualizedMetricData addLaunchDuration:foreground:]
+ -[PLContextualizedMetricData addMetalFrameRateWithLayerName:frameCount:activeSeconds:]
+ -[PLContextualizedMetricData addResumeDuration:]
+ -[PLContextualizedMetricData addSignpostIntervalEntry:]
+ -[PLContextualizedMetricData averageMemoryBytes]
+ -[PLContextualizedMetricData averageMemoryCount]
+ -[PLContextualizedMetricData averageMemoryVariance]
+ -[PLContextualizedMetricData averagePixelLuminance]
+ -[PLContextualizedMetricData bestAccuracyForNavigationSeconds]
+ -[PLContextualizedMetricData bestAccuracySeconds]
+ -[PLContextualizedMetricData bgAudioTimeSeconds]
+ -[PLContextualizedMetricData bgLocationAudioTimeSeconds]
+ -[PLContextualizedMetricData bgLocationTimeSeconds]
+ -[PLContextualizedMetricData bgTotalTimeSeconds]
+ -[PLContextualizedMetricData cellularBytesIn]
+ -[PLContextualizedMetricData cellularBytesOut]
+ -[PLContextualizedMetricData cpuInstructionsRetired]
+ -[PLContextualizedMetricData cpuTimeSeconds]
+ -[PLContextualizedMetricData diskBytesWritten]
+ -[PLContextualizedMetricData encodeWithCoder:]
+ -[PLContextualizedMetricData exitsOutput]
+ -[PLContextualizedMetricData exits]
+ -[PLContextualizedMetricData extendedLaunchesOutput]
+ -[PLContextualizedMetricData extendedLaunches]
+ -[PLContextualizedMetricData fgTimeSeconds]
+ -[PLContextualizedMetricData glitchCount]
+ -[PLContextualizedMetricData glitchDurationMs]
+ -[PLContextualizedMetricData glitchesOutput]
+ -[PLContextualizedMetricData gpuTimeSeconds]
+ -[PLContextualizedMetricData hangsOutput]
+ -[PLContextualizedMetricData hangs]
+ -[PLContextualizedMetricData hasActivations]
+ -[PLContextualizedMetricData hasAnyMetrics]
+ -[PLContextualizedMetricData hasCPUMetrics]
+ -[PLContextualizedMetricData hasCellularMetrics]
+ -[PLContextualizedMetricData hasDiskIOMetrics]
+ -[PLContextualizedMetricData hasDisplayMetrics]
+ -[PLContextualizedMetricData hasExits]
+ -[PLContextualizedMetricData hasExtendedLaunches]
+ -[PLContextualizedMetricData hasGPUMetrics]
+ -[PLContextualizedMetricData hasGlitches]
+ -[PLContextualizedMetricData hasHangs]
+ -[PLContextualizedMetricData hasLaunches]
+ -[PLContextualizedMetricData hasLocationMetrics]
+ -[PLContextualizedMetricData hasMemoryMetrics]
+ -[PLContextualizedMetricData hasMetalFrameRates]
+ -[PLContextualizedMetricData hasNetworkMetrics]
+ -[PLContextualizedMetricData hasResumes]
+ -[PLContextualizedMetricData hasRuntimeMetrics]
+ -[PLContextualizedMetricData hasSignpostIntervals]
+ -[PLContextualizedMetricData hundredMetersAccuracySeconds]
+ -[PLContextualizedMetricData initWithCoder:]
+ -[PLContextualizedMetricData kilometerAccuracySeconds]
+ -[PLContextualizedMetricData launchesOutput]
+ -[PLContextualizedMetricData launches]
+ -[PLContextualizedMetricData metalFrameRatesOutput]
+ -[PLContextualizedMetricData metalFrameRates]
+ -[PLContextualizedMetricData nearestTenMetersAccuracySeconds]
+ -[PLContextualizedMetricData peakMemoryBytes]
+ -[PLContextualizedMetricData resumesOutput]
+ -[PLContextualizedMetricData resumes]
+ -[PLContextualizedMetricData scrollCount]
+ -[PLContextualizedMetricData scrollDurationMs]
+ -[PLContextualizedMetricData setActivations:]
+ -[PLContextualizedMetricData setAverageMemoryBytes:]
+ -[PLContextualizedMetricData setAverageMemoryCount:]
+ -[PLContextualizedMetricData setAverageMemoryVariance:]
+ -[PLContextualizedMetricData setAveragePixelLuminance:]
+ -[PLContextualizedMetricData setBestAccuracyForNavigationSeconds:]
+ -[PLContextualizedMetricData setBestAccuracySeconds:]
+ -[PLContextualizedMetricData setBgAudioTimeSeconds:]
+ -[PLContextualizedMetricData setBgLocationAudioTimeSeconds:]
+ -[PLContextualizedMetricData setBgLocationTimeSeconds:]
+ -[PLContextualizedMetricData setBgTotalTimeSeconds:]
+ -[PLContextualizedMetricData setCellularBytesIn:]
+ -[PLContextualizedMetricData setCellularBytesOut:]
+ -[PLContextualizedMetricData setCpuInstructionsRetired:]
+ -[PLContextualizedMetricData setCpuTimeSeconds:]
+ -[PLContextualizedMetricData setDBMetrics:forType:]
+ -[PLContextualizedMetricData setDiskBytesWritten:]
+ -[PLContextualizedMetricData setExits:]
+ -[PLContextualizedMetricData setExtendedLaunches:]
+ -[PLContextualizedMetricData setFgTimeSeconds:]
+ -[PLContextualizedMetricData setGlitchCount:]
+ -[PLContextualizedMetricData setGlitchDurationMs:]
+ -[PLContextualizedMetricData setGpuTimeSeconds:]
+ -[PLContextualizedMetricData setHangs:]
+ -[PLContextualizedMetricData setHasActivations:]
+ -[PLContextualizedMetricData setHasCPUMetrics:]
+ -[PLContextualizedMetricData setHasCellularMetrics:]
+ -[PLContextualizedMetricData setHasDiskIOMetrics:]
+ -[PLContextualizedMetricData setHasDisplayMetrics:]
+ -[PLContextualizedMetricData setHasExits:]
+ -[PLContextualizedMetricData setHasExtendedLaunches:]
+ -[PLContextualizedMetricData setHasGPUMetrics:]
+ -[PLContextualizedMetricData setHasGlitches:]
+ -[PLContextualizedMetricData setHasHangs:]
+ -[PLContextualizedMetricData setHasLaunches:]
+ -[PLContextualizedMetricData setHasLocationMetrics:]
+ -[PLContextualizedMetricData setHasMemoryMetrics:]
+ -[PLContextualizedMetricData setHasMetalFrameRates:]
+ -[PLContextualizedMetricData setHasNetworkMetrics:]
+ -[PLContextualizedMetricData setHasResumes:]
+ -[PLContextualizedMetricData setHasRuntimeMetrics:]
+ -[PLContextualizedMetricData setHasSignpostIntervals:]
+ -[PLContextualizedMetricData setHundredMetersAccuracySeconds:]
+ -[PLContextualizedMetricData setKilometerAccuracySeconds:]
+ -[PLContextualizedMetricData setLaunches:]
+ -[PLContextualizedMetricData setMetalFrameRates:]
+ -[PLContextualizedMetricData setNearestTenMetersAccuracySeconds:]
+ -[PLContextualizedMetricData setPeakMemoryBytes:]
+ -[PLContextualizedMetricData setResumes:]
+ -[PLContextualizedMetricData setScrollCount:]
+ -[PLContextualizedMetricData setScrollDurationMs:]
+ -[PLContextualizedMetricData setSignalBar0Seconds:]
+ -[PLContextualizedMetricData setSignalBar1Seconds:]
+ -[PLContextualizedMetricData setSignalBar2Seconds:]
+ -[PLContextualizedMetricData setSignalBar3Seconds:]
+ -[PLContextualizedMetricData setSignalBar4Seconds:]
+ -[PLContextualizedMetricData setSignpostIntervals:]
+ -[PLContextualizedMetricData setThreeKilometersAccuracySeconds:]
+ -[PLContextualizedMetricData setTotalAnimationDuration:]
+ -[PLContextualizedMetricData setTotalFrameCount:]
+ -[PLContextualizedMetricData setWeightedGlitchRatioSum:]
+ -[PLContextualizedMetricData setWifiBytesIn:]
+ -[PLContextualizedMetricData setWifiBytesOut:]
+ -[PLContextualizedMetricData signalBar0Seconds]
+ -[PLContextualizedMetricData signalBar1Seconds]
+ -[PLContextualizedMetricData signalBar2Seconds]
+ -[PLContextualizedMetricData signalBar3Seconds]
+ -[PLContextualizedMetricData signalBar4Seconds]
+ -[PLContextualizedMetricData signpostIntervalsOutput]
+ -[PLContextualizedMetricData signpostIntervals]
+ -[PLContextualizedMetricData threeKilometersAccuracySeconds]
+ -[PLContextualizedMetricData toDictionary]
+ -[PLContextualizedMetricData totalAnimationDuration]
+ -[PLContextualizedMetricData totalFrameCount]
+ -[PLContextualizedMetricData weightedGlitchRatioSum]
+ -[PLContextualizedMetricData wifiBytesIn]
+ -[PLContextualizedMetricData wifiBytesOut]
+ -[PLContextualizedMetrics .cxx_destruct]
+ -[PLContextualizedMetrics chunkMetrics]
+ -[PLContextualizedMetrics encodeWithCoder:]
+ -[PLContextualizedMetrics initWithCoder:]
+ -[PLContextualizedMetrics initWithStateMetrics:chunkMetrics:]
+ -[PLContextualizedMetrics stateMetrics]
+ -[PLContextualizedMetrics toDictionary]
+ -[PLStateInterval .cxx_destruct]
+ -[PLStateInterval aggregationKey]
+ -[PLStateInterval bundleIDResolved]
+ -[PLStateInterval bundleID]
+ -[PLStateInterval copyWithZone:]
+ -[PLStateInterval description]
+ -[PLStateInterval domain]
+ -[PLStateInterval durationMs]
+ -[PLStateInterval durationSeconds]
+ -[PLStateInterval endDate]
+ -[PLStateInterval initWithDomain:label:bundleID:bundleIDResolved:processName:durationMs:startDate:endDate:stableState:pid:processImageUUID:processImagePath:]
+ -[PLStateInterval intervalWithResolvedBundleID:]
+ -[PLStateInterval label]
+ -[PLStateInterval pid]
+ -[PLStateInterval processImagePath]
+ -[PLStateInterval processImageUUID]
+ -[PLStateInterval processName]
+ -[PLStateInterval stableState]
+ -[PLStateInterval startDate]
+ -[PLStateInterval toDictionary]
+ -[PLStorageCache addToBGSQLStagingCache:]
+ -[PLStorageCache addToBGSQLStagingCache:].cold.1
+ -[PLStorageCache bgsqlDedicatedCacheEnabled]
+ -[PLStorageCache bgsqlFlushCountThisWindow]
+ -[PLStorageCache bgsqlFlushWindowStart]
+ -[PLStorageCache bgsqlStagingCacheSize]
+ -[PLStorageCache bgsqlStagingCache]
+ -[PLStorageCache flushBGSQLStagingCacheToDatabase]
+ -[PLStorageCache logBGSQLCacheSizeWithInsertCount:updateCount:flushDate:]
+ -[PLStorageCache setBgsqlFlushCountThisWindow:]
+ -[PLStorageCache setBgsqlFlushWindowStart:]
+ -[PLStorageCache setBgsqlStagingCache:]
+ -[PLStorageCache trackBGSQLFlushFrequencyWithDate:]
+ -[PLStorageCache trackBGSQLFlushFrequencyWithDate:].cold.1
+ -[PLSubmissionConfig emitTrialsTaskingDecisionEvent:enrolledTrials:appliedPercentage:]
+ -[PLSubmissionConfig enrolledTrialNamespaces]
+ -[PLSubmissionConfig enrolledTrialsFromTaskingTrials]
+ -[PLSubmissionConfig enrolledTrialsFromTaskingTrials].cold.1
+ -[PLSubmissionConfig enrolledTrialsFromTaskingTrials].cold.2
+ -[PLSubmissionConfig lookupTableGroup:]
+ -[PLSubmissionConfig lookupTableGroup:].cold.1
+ -[PLSubmissionConfig perModelTrialsPercentages]
+ -[PLSubmissionConfig readTaskingPayloadOverride:].cold.1
+ -[PLSubmissionConfig resolveTaskingTables]
+ -[PLSubmissionConfig setEnrolledTrialNamespaces:]
+ -[PLSubmissionConfig setPerModelTrialsPercentages:]
+ -[PLSubmissionConfig setTaskingBaselinePercentage:]
+ -[PLSubmissionConfig setTaskingTableGroups:]
+ -[PLSubmissionConfig setTaskingTrials:]
+ -[PLSubmissionConfig setTaskingTrialsPercentage:]
+ -[PLSubmissionConfig shouldStartTrialsTaskingToday]
+ -[PLSubmissionConfig shouldStartTrialsTaskingToday].cold.1
+ -[PLSubmissionConfig shouldStartTrialsTaskingToday].cold.2
+ -[PLSubmissionConfig shouldStartTrialsTaskingToday].cold.3
+ -[PLSubmissionConfig shouldStartTrialsTaskingToday].cold.4
+ -[PLSubmissionConfig shouldStartTrialsTaskingToday].cold.5
+ -[PLSubmissionConfig shouldStartTrialsTaskingToday].cold.6
+ -[PLSubmissionConfig shouldStartTrialsTaskingToday].cold.7
+ -[PLSubmissionConfig shouldStartTrialsTaskingToday].cold.8
+ -[PLSubmissionConfig taskingBaselinePercentage]
+ -[PLSubmissionConfig taskingTableGroups]
+ -[PLSubmissionConfig taskingTrialsPercentage]
+ -[PLSubmissionConfig taskingTrials]
+ -[PLSubmissionFilePLL prepareDatabaseAtPath:].cold.1
+ -[PLSubmissionFilePLL prepareDatabaseAtPath:].cold.2
+ -[PLSubmissions taskingBlobHasTrialsConfiguration]
+ -[PLTaskingTrial .cxx_destruct]
+ -[PLTaskingTrial deploymentId]
+ -[PLTaskingTrial dictionaryRepresentation]
+ -[PLTaskingTrial experimentId]
+ -[PLTaskingTrial setDeploymentId:]
+ -[PLTaskingTrial setExperimentId:]
+ -[PLTimeChunkInterval aggregationKey]
+ -[PLTimeChunkInterval chunkDurationSeconds]
+ -[PLTimeChunkInterval chunkIndex]
+ -[PLTimeChunkInterval copyWithZone:]
+ -[PLTimeChunkInterval description]
+ -[PLTimeChunkInterval encodeWithCoder:]
+ -[PLTimeChunkInterval endTimestamp]
+ -[PLTimeChunkInterval hash]
+ -[PLTimeChunkInterval initWithCoder:]
+ -[PLTimeChunkInterval initWithStartTimestamp:endTimestamp:chunkIndex:]
+ -[PLTimeChunkInterval isEqual:]
+ -[PLTimeChunkInterval setChunkIndex:]
+ -[PLTimeChunkInterval setEndTimestamp:]
+ -[PLTimeChunkInterval setStartTimestamp:]
+ -[PLTimeChunkInterval startTimestamp]
+ -[PLTimeChunkInterval toDictionary]
+ -[PLTimeChunkInterval toFilterableDictionary]
+ -[PPSSQLStorage setupTableForEntryKey:withName:].cold.3
+ -[SignpostReaderHelper getSignpostMetricsWithStartDate:withEndDate:processMXSignpost:collectStateIntervals:chunkIntervals:stateAwareClientsAllowlist:]
+ GCC_except_table102
+ GCC_except_table112
+ GCC_except_table15
+ GCC_except_table38
+ GCC_except_table53
+ _ArrayReserved_block_invoke_4.classDebugEnabled.110
+ _ArrayReserved_block_invoke_4.defaultOnce.109
+ _OBJC_CLASS_$_NSOrderedSet
+ _OBJC_CLASS_$_PLContextualizedMetricData
+ _OBJC_CLASS_$_PLContextualizedMetrics
+ _OBJC_CLASS_$_PLStateInterval
+ _OBJC_CLASS_$_PLTaskingTrial
+ _OBJC_CLASS_$_PLTimeChunkInterval
+ _OBJC_CLASS_$_TRIAllocationStatus
+ _OBJC_CLASS_$_TRIClient
+ _OBJC_CLASS_$_TRIExperimentAllocationStatus
+ _OBJC_IVAR_$_PLContextualizedMetricData._activations
+ _OBJC_IVAR_$_PLContextualizedMetricData._averageMemoryBytes
+ _OBJC_IVAR_$_PLContextualizedMetricData._averageMemoryCount
+ _OBJC_IVAR_$_PLContextualizedMetricData._averageMemoryVariance
+ _OBJC_IVAR_$_PLContextualizedMetricData._averagePixelLuminance
+ _OBJC_IVAR_$_PLContextualizedMetricData._bestAccuracyForNavigationSeconds
+ _OBJC_IVAR_$_PLContextualizedMetricData._bestAccuracySeconds
+ _OBJC_IVAR_$_PLContextualizedMetricData._bgAudioTimeSeconds
+ _OBJC_IVAR_$_PLContextualizedMetricData._bgLocationAudioTimeSeconds
+ _OBJC_IVAR_$_PLContextualizedMetricData._bgLocationTimeSeconds
+ _OBJC_IVAR_$_PLContextualizedMetricData._bgTotalTimeSeconds
+ _OBJC_IVAR_$_PLContextualizedMetricData._cellularBytesIn
+ _OBJC_IVAR_$_PLContextualizedMetricData._cellularBytesOut
+ _OBJC_IVAR_$_PLContextualizedMetricData._cpuInstructionsRetired
+ _OBJC_IVAR_$_PLContextualizedMetricData._cpuTimeSeconds
+ _OBJC_IVAR_$_PLContextualizedMetricData._diskBytesWritten
+ _OBJC_IVAR_$_PLContextualizedMetricData._exits
+ _OBJC_IVAR_$_PLContextualizedMetricData._extendedLaunches
+ _OBJC_IVAR_$_PLContextualizedMetricData._fgTimeSeconds
+ _OBJC_IVAR_$_PLContextualizedMetricData._glitchCount
+ _OBJC_IVAR_$_PLContextualizedMetricData._glitchDurationMs
+ _OBJC_IVAR_$_PLContextualizedMetricData._gpuTimeSeconds
+ _OBJC_IVAR_$_PLContextualizedMetricData._hangs
+ _OBJC_IVAR_$_PLContextualizedMetricData._hasActivations
+ _OBJC_IVAR_$_PLContextualizedMetricData._hasCPUMetrics
+ _OBJC_IVAR_$_PLContextualizedMetricData._hasCellularMetrics
+ _OBJC_IVAR_$_PLContextualizedMetricData._hasDiskIOMetrics
+ _OBJC_IVAR_$_PLContextualizedMetricData._hasDisplayMetrics
+ _OBJC_IVAR_$_PLContextualizedMetricData._hasExits
+ _OBJC_IVAR_$_PLContextualizedMetricData._hasExtendedLaunches
+ _OBJC_IVAR_$_PLContextualizedMetricData._hasGPUMetrics
+ _OBJC_IVAR_$_PLContextualizedMetricData._hasGlitches
+ _OBJC_IVAR_$_PLContextualizedMetricData._hasHangs
+ _OBJC_IVAR_$_PLContextualizedMetricData._hasLaunches
+ _OBJC_IVAR_$_PLContextualizedMetricData._hasLocationMetrics
+ _OBJC_IVAR_$_PLContextualizedMetricData._hasMemoryMetrics
+ _OBJC_IVAR_$_PLContextualizedMetricData._hasMetalFrameRates
+ _OBJC_IVAR_$_PLContextualizedMetricData._hasNetworkMetrics
+ _OBJC_IVAR_$_PLContextualizedMetricData._hasResumes
+ _OBJC_IVAR_$_PLContextualizedMetricData._hasRuntimeMetrics
+ _OBJC_IVAR_$_PLContextualizedMetricData._hasSignpostIntervals
+ _OBJC_IVAR_$_PLContextualizedMetricData._hundredMetersAccuracySeconds
+ _OBJC_IVAR_$_PLContextualizedMetricData._kilometerAccuracySeconds
+ _OBJC_IVAR_$_PLContextualizedMetricData._launches
+ _OBJC_IVAR_$_PLContextualizedMetricData._metalFrameRates
+ _OBJC_IVAR_$_PLContextualizedMetricData._nearestTenMetersAccuracySeconds
+ _OBJC_IVAR_$_PLContextualizedMetricData._peakMemoryBytes
+ _OBJC_IVAR_$_PLContextualizedMetricData._resumes
+ _OBJC_IVAR_$_PLContextualizedMetricData._scrollCount
+ _OBJC_IVAR_$_PLContextualizedMetricData._scrollDurationMs
+ _OBJC_IVAR_$_PLContextualizedMetricData._signalBar0Seconds
+ _OBJC_IVAR_$_PLContextualizedMetricData._signalBar1Seconds
+ _OBJC_IVAR_$_PLContextualizedMetricData._signalBar2Seconds
+ _OBJC_IVAR_$_PLContextualizedMetricData._signalBar3Seconds
+ _OBJC_IVAR_$_PLContextualizedMetricData._signalBar4Seconds
+ _OBJC_IVAR_$_PLContextualizedMetricData._signpostIntervals
+ _OBJC_IVAR_$_PLContextualizedMetricData._threeKilometersAccuracySeconds
+ _OBJC_IVAR_$_PLContextualizedMetricData._totalAnimationDuration
+ _OBJC_IVAR_$_PLContextualizedMetricData._totalFrameCount
+ _OBJC_IVAR_$_PLContextualizedMetricData._weightedGlitchRatioSum
+ _OBJC_IVAR_$_PLContextualizedMetricData._wifiBytesIn
+ _OBJC_IVAR_$_PLContextualizedMetricData._wifiBytesOut
+ _OBJC_IVAR_$_PLContextualizedMetrics._chunkMetrics
+ _OBJC_IVAR_$_PLContextualizedMetrics._stateMetrics
+ _OBJC_IVAR_$_PLStateInterval._bundleID
+ _OBJC_IVAR_$_PLStateInterval._bundleIDResolved
+ _OBJC_IVAR_$_PLStateInterval._domain
+ _OBJC_IVAR_$_PLStateInterval._durationMs
+ _OBJC_IVAR_$_PLStateInterval._endDate
+ _OBJC_IVAR_$_PLStateInterval._label
+ _OBJC_IVAR_$_PLStateInterval._pid
+ _OBJC_IVAR_$_PLStateInterval._processImagePath
+ _OBJC_IVAR_$_PLStateInterval._processImageUUID
+ _OBJC_IVAR_$_PLStateInterval._processName
+ _OBJC_IVAR_$_PLStateInterval._stableState
+ _OBJC_IVAR_$_PLStateInterval._startDate
+ _OBJC_IVAR_$_PLStorageCache._bgsqlDedicatedCacheEnabled
+ _OBJC_IVAR_$_PLStorageCache._bgsqlFlushCountThisWindow
+ _OBJC_IVAR_$_PLStorageCache._bgsqlFlushWindowStart
+ _OBJC_IVAR_$_PLStorageCache._bgsqlStagingCache
+ _OBJC_IVAR_$_PLSubmissionConfig._enrolledTrialNamespaces
+ _OBJC_IVAR_$_PLSubmissionConfig._perModelTrialsPercentages
+ _OBJC_IVAR_$_PLSubmissionConfig._taskingBaselinePercentage
+ _OBJC_IVAR_$_PLSubmissionConfig._taskingTableGroups
+ _OBJC_IVAR_$_PLSubmissionConfig._taskingTrials
+ _OBJC_IVAR_$_PLSubmissionConfig._taskingTrialsPercentage
+ _OBJC_IVAR_$_PLTaskingTrial._deploymentId
+ _OBJC_IVAR_$_PLTaskingTrial._experimentId
+ _OBJC_IVAR_$_PLTimeChunkInterval._chunkIndex
+ _OBJC_IVAR_$_PLTimeChunkInterval._endTimestamp
+ _OBJC_IVAR_$_PLTimeChunkInterval._startTimestamp
+ _OBJC_METACLASS_$_PLContextualizedMetricData
+ _OBJC_METACLASS_$_PLContextualizedMetrics
+ _OBJC_METACLASS_$_PLStateInterval
+ _OBJC_METACLASS_$_PLTaskingTrial
+ _OBJC_METACLASS_$_PLTimeChunkInterval
+ _PLSafeDoubleValue
+ _PLSafeIntegerValue
+ _PLSafeUnsignedIntegerValue
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.72
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.71
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_2.classDebugEnabled.52
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_2.defaultOnce.51
+ __OBJC_$_CLASS_METHODS_PLContextualizedMetricData
+ __OBJC_$_CLASS_METHODS_PLContextualizedMetrics
+ __OBJC_$_CLASS_METHODS_PLStateInterval
+ __OBJC_$_CLASS_METHODS_PLTimeChunkInterval
+ __OBJC_$_CLASS_METHODS_SignpostReaderHelper
+ __OBJC_$_CLASS_PROP_LIST_PLContextualizedMetricData
+ __OBJC_$_CLASS_PROP_LIST_PLContextualizedMetrics
+ __OBJC_$_CLASS_PROP_LIST_PLTimeChunkInterval
+ __OBJC_$_INSTANCE_METHODS_PLContextualizedMetricData
+ __OBJC_$_INSTANCE_METHODS_PLContextualizedMetrics
+ __OBJC_$_INSTANCE_METHODS_PLStateInterval
+ __OBJC_$_INSTANCE_METHODS_PLTaskingTrial
+ __OBJC_$_INSTANCE_METHODS_PLTimeChunkInterval
+ __OBJC_$_INSTANCE_VARIABLES_PLContextualizedMetricData
+ __OBJC_$_INSTANCE_VARIABLES_PLContextualizedMetrics
+ __OBJC_$_INSTANCE_VARIABLES_PLStateInterval
+ __OBJC_$_INSTANCE_VARIABLES_PLTaskingTrial
+ __OBJC_$_INSTANCE_VARIABLES_PLTimeChunkInterval
+ __OBJC_$_PROP_LIST_PLContextualizedMetricData
+ __OBJC_$_PROP_LIST_PLContextualizedMetrics
+ __OBJC_$_PROP_LIST_PLStateInterval
+ __OBJC_$_PROP_LIST_PLTaskingTrial
+ __OBJC_$_PROP_LIST_PLTimeChunkInterval
+ __OBJC_CLASS_PROTOCOLS_$_PLContextualizedMetricData
+ __OBJC_CLASS_PROTOCOLS_$_PLContextualizedMetrics
+ __OBJC_CLASS_PROTOCOLS_$_PLStateInterval
+ __OBJC_CLASS_PROTOCOLS_$_PLTimeChunkInterval
+ __OBJC_CLASS_RO_$_PLContextualizedMetricData
+ __OBJC_CLASS_RO_$_PLContextualizedMetrics
+ __OBJC_CLASS_RO_$_PLStateInterval
+ __OBJC_CLASS_RO_$_PLTaskingTrial
+ __OBJC_CLASS_RO_$_PLTimeChunkInterval
+ __OBJC_METACLASS_RO_$_PLContextualizedMetricData
+ __OBJC_METACLASS_RO_$_PLContextualizedMetrics
+ __OBJC_METACLASS_RO_$_PLStateInterval
+ __OBJC_METACLASS_RO_$_PLTaskingTrial
+ __OBJC_METACLASS_RO_$_PLTimeChunkInterval
+ __ZNSt12length_errorC1B9fqe220100EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE22__init_internal_bufferB9fqe220100Em
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB9fqe220100Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B9fqe220100Ej
+ __ZNSt3__116__pad_and_outputB9fqe220100IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__119__allocate_at_leastB9fqe220100INS_9allocatorIlEENS_16allocator_traitsIS2_EEEENS_19__allocation_resultINT0_7pointerENS6_9size_typeEEERT_m
+ __ZNSt3__119__shared_weak_count16__release_sharedB9fqe220100Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9fqe220100Ev
+ __ZNSt3__120__throw_length_errorB9fqe220100EPKc
+ __ZNSt3__124__put_character_sequenceB9fqe220100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__16vectorIlNS_9allocatorIlEEE11__vallocateB9fqe220100Em
+ __ZNSt3__16vectorIlNS_9allocatorIlEEE16__init_with_sizeB9fqe220100IPKlS6_EEvT_T0_m
+ __ZNSt3__16vectorIlNS_9allocatorIlEEE20__throw_length_errorB9fqe220100Ev
+ __ZSt28__throw_bad_array_new_lengthB9fqe220100v
+ ___104-[PLCoreStorage entriesForKey:inTimeRange:withCountOfEntriesBefore:withCountOfEntriesAfter:withFilters:]_block_invoke.857
+ ___18-[PLOperator init]_block_invoke.42
+ ___18-[PLXPCRelay init]_block_invoke.23
+ ___21-[PLCoreStorage init]_block_invoke.115
+ ___21-[PLCoreStorage init]_block_invoke.67
+ ___21-[PLCoreStorage init]_block_invoke.72
+ ___21-[PLCoreStorage init]_block_invoke.77
+ ___21-[PLTimeManager init]_block_invoke.28
+ ___21-[PLTimeManager init]_block_invoke.28.cold.1
+ ___23-[PLKQueue setEnabled:]_block_invoke.19
+ ___23-[PLKQueue setEnabled:]_block_invoke.27
+ ___23-[PLKQueue setEnabled:]_block_invoke.34
+ ___24-[PLXPCRelay startRelay]_block_invoke.33
+ ___24-[PLXPCRelay startRelay]_block_invoke.33.cold.1
+ ___24-[PLXPCRelay startRelay]_block_invoke.33.cold.2
+ ___24-[PLXPCRelay startRelay]_block_invoke.39
+ ___24-[PLXPCRelay startRelay]_block_invoke.44
+ ___24-[PLXPCRelay startRelay]_block_invoke.44.cold.1
+ ___24-[PLXPCRelay startRelay]_block_invoke_2.45
+ ___25-[PLActivity runActivity]_block_invoke.20
+ ___25-[PLActivity runActivity]_block_invoke.21
+ ___25-[PLOperator flushBuffer]_block_invoke.66
+ ___26-[PLOperator logDMAEntry:]_block_invoke.228
+ ___26-[PLOperator postEntries:]_block_invoke.104
+ ___26-[PLOperator postEntries:]_block_invoke.104.cold.1
+ ___26-[PLOperator postEntries:]_block_invoke.104.cold.2
+ ___26-[PLOperator postEntries:]_block_invoke.111
+ ___26-[PLOperator postEntries:]_block_invoke_2.105
+ ___26-[PLTimer setTimerActive:]_block_invoke.26
+ ___26-[PLTimer setTimerActive:]_block_invoke.26.cold.1
+ ___26-[PLTimer setTimerActive:]_block_invoke_2.27
+ ___27-[PLArchiveManager migrate]_block_invoke.608
+ ___27-[PLMonotonicTimer _cancel]_block_invoke.45
+ ___27-[PLMonotonicTimer _cancel]_block_invoke.51
+ ___28-[PLMonotonicTimer schedule]_block_invoke.33
+ ___28-[PLMonotonicTimer schedule]_block_invoke.37
+ ___29+[PLUtilities deviceBootUUID]_block_invoke.163
+ ___29-[PLXPCRelay relayConnection]_block_invoke.136.cold.1
+ ___29-[PLXPCRelay relayConnection]_block_invoke.136.cold.2
+ ___29-[PLXPCRelay relayConnection]_block_invoke.136.cold.3
+ ___29-[PLXPCRelay relayConnection]_block_invoke.136.cold.4
+ ___29-[PLXPCRelay relayConnection]_block_invoke.139
+ ___29-[PLXPCRelay relayConnection]_block_invoke.146
+ ___29-[PLXPCRelay relayConnection]_block_invoke.152
+ ___29-[PLXPCRelay relayConnection]_block_invoke.158
+ ___29-[PLXPCRelay relayConnection]_block_invoke.164
+ ___30-[PLMonotonicTimer reschedule]_block_invoke.92
+ ___30-[PLMonotonicTimer reschedule]_block_invoke.98
+ ___31+[PLGestaltUtilities hasPencil]_block_invoke
+ ___32-[PLABMClient regMetricListener]_block_invoke.70
+ ___32-[PLABMClient regMetricListener]_block_invoke.70.cold.1
+ ___32-[PLABMClient regMetricListener]_block_invoke.70.cold.2
+ ___33-[PLSemaphore waitWithBlockSync:]_block_invoke.48
+ ___33-[PLSubmissions taskingModeSetup]_block_invoke.358
+ ___33-[PLSubmissions taskingModeSetup]_block_invoke.374
+ ___33-[PLSubmissions taskingModeSetup]_block_invoke.374.cold.1
+ ___33-[PLSubmissions taskingModeSetup]_block_invoke.376
+ ___33-[PLSubmissions taskingModeSetup]_block_invoke_2.368
+ ___34+[PLAppDeletion _appDeletionQueue]_block_invoke
+ ___34-[PLSQLiteConnection updateEntry:]_block_invoke.671
+ ___34-[PLSQLiteConnection updateEntry:]_block_invoke.677
+ ___34-[PLSQLiteConnection updateEntry:]_block_invoke.683
+ ___34-[PLSemaphore signalDoneByObject:]_block_invoke.29
+ ___34-[PLSemaphore signalDoneByObject:]_block_invoke.35
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.105
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.111
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.120
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.126
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.60
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.66
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.72
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.78
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.90
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.99
+ ___35-[PLArchiveManager migrateArchive:]_block_invoke.592
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke.430
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke.430.cold.1
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke.436
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke.441
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke.441.cold.1
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke_2.442
+ ___35-[PLSQLiteConnection runTrimQuery:]_block_invoke.328
+ ___35-[PLSQLiteConnection runTrimQuery:]_block_invoke.334
+ ___35-[PLSubmissions performSubmission:]_block_invoke.172
+ ___35-[PPSCoreStorage setupEntryObjects]_block_invoke.34
+ ___36-[PLTimeReferenceDynamic setOffset:]_block_invoke.53
+ ___36-[PPSSignpostServiceConnection init]_block_invoke.20
+ ___36-[PPSSignpostServiceConnection init]_block_invoke.20.cold.1
+ ___37+[PLUtilities exitWithReason:action:]_block_invoke.233
+ ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.760
+ ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.766
+ ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.773
+ ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.779
+ ___37-[PLStorageCache entryIDForNewEntry:]_block_invoke.108
+ ___37-[PLStorageCache entryIDForNewEntry:]_block_invoke.123
+ ___37-[PLSubmissions submitReasonForToday]_block_invoke.141
+ ___37-[PLSubmissions submitReasonForToday]_block_invoke.147
+ ___37-[PLSubmissions submitReasonForToday]_block_invoke.153
+ ___37-[PLSubmissions taskingModeSafeguard]_block_invoke.335
+ ___37-[PPSSignpostController _handleTask:]_block_invoke.109
+ ___38-[PLStorageCache addToLastEntryCache:]_block_invoke.95
+ ___38-[PLSubmissionFileBDC getBDCPlistFile]_block_invoke.53
+ ___38-[PLSubmissionFileBDC getBDCPlistFile]_block_invoke.53.cold.1
+ ___38-[PLTimeReference getHourBucketOffset]_block_invoke.26
+ ___38-[PLTimeReferenceBaseband currentTime]_block_invoke.32
+ ___38-[PLTimeReferenceBaseband currentTime]_block_invoke.32.cold.1
+ ___38-[PLTimeReferenceBaseband currentTime]_block_invoke.40
+ ___39+[PLAppDeletion constructUpdateQueries]_block_invoke.112
+ ___39-[PLCoreStorage flushCachesWithReason:]_block_invoke.673
+ ___39-[PLCoreStorage flushCachesWithReason:]_block_invoke.675
+ ___39-[PLStorageCache bgsqlStagingCacheSize]_block_invoke
+ ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.109
+ ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.113
+ ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.120
+ ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.124
+ ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.128
+ ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.132
+ ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.136
+ ___39-[PLSubmissionFileSP copyAndPrepareLog]_block_invoke.145
+ ___39-[PPSCoreStorage mergePreUnlockDBFiles]_block_invoke.53
+ ___39-[PPSCoreStorage mergePreUnlockDBFiles]_block_invoke.53.cold.1
+ ___39-[PPSCoreStorage mergePreUnlockDBFiles]_block_invoke.53.cold.2
+ ___40+[PLSubmissionConfig taskingTableGroups]_block_invoke
+ ___40+[PLSubmissionConfig taskingTableGroups]_block_invoke.cold.1
+ ___41+[PLNetworkUtilities getNetworkWakeInfo:]_block_invoke.132
+ ___41+[PLNetworkUtilities isESPPacket:offset:]_block_invoke.285
+ ___41+[PLNetworkUtilities isESPPacket:offset:]_block_invoke.291
+ ___41-[PLCoreStorage initOperatorDependancies]_block_invoke.333
+ ___41-[PLStorageCache addToBGSQLStagingCache:]_block_invoke
+ ___41-[PLStorageCache addToBGSQLStagingCache:]_block_invoke.313
+ ___41-[PLStorageCache addToBGSQLStagingCache:]_block_invoke.313.cold.1
+ ___41-[PLStorageCache addToBGSQLStagingCache:]_block_invoke.314
+ ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.136
+ ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.136.cold.1
+ ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.136.cold.2
+ ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.136.cold.3
+ ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.136.cold.4
+ ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.142
+ ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.149
+ ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.155
+ ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.443
+ ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.449
+ ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.455
+ ___42-[PLSQLiteConnection removeEmptyOldTables]_block_invoke.382
+ ___42-[PLSQLiteConnection writeDynamicEntries:]_block_invoke.632
+ ___42-[PLSubmissionConfig resolveTaskingTables]_block_invoke
+ ___42-[PLSubmissionConfig resolveTaskingTables]_block_invoke.647
+ ___42-[PLSubmissionConfig resolveTaskingTables]_block_invoke.647.cold.1
+ ___42-[PLSubmissionConfig resolveTaskingTables]_block_invoke.651
+ ___42-[PLSubmissionConfig resolveTaskingTables]_block_invoke_2
+ ___42-[RbdcConverterHelper createXPCConnection]_block_invoke.50
+ ___42-[RbdcConverterHelper createXPCConnection]_block_invoke.50.cold.1
+ ___43+[PLNetworkUtilities handlePowerWakeEvent:]_block_invoke.153
+ ___43-[SignpostReaderHelper createXPCConnection]_block_invoke.69
+ ___43-[SignpostReaderHelper createXPCConnection]_block_invoke.69.cold.1
+ ___43-[SignpostReaderHelper createXPCConnection]_block_invoke.72
+ ___43-[SignpostReaderHelper createXPCConnection]_block_invoke.72.cold.1
+ ___44-[PLSQLiteConnection scheduleIntegrityCheck]_block_invoke.80
+ ___44-[PLStorageCache lastEntryCachePruneToDate:]_block_invoke.72
+ ___44-[PLStorageCache lastEntryCachePruneToDate:]_block_invoke.77
+ ___44-[PLSubmissions handleDRConfigUpdate:error:]_block_invoke.122
+ ___45-[PLActivityCriterionTime didEnableActivity:]_block_invoke.28
+ ___45-[PLActivityCriterionTime didEnableActivity:]_block_invoke.33
+ ___45-[PLActivityCriterionTime didEnableActivity:]_block_invoke.33.cold.1
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.475
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.481
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.491
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.502
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.508
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.517
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.538
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.544
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.550
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.557
+ ___45-[PLSubmissionFilePLL prepareDatabaseAtPath:]_block_invoke.127
+ ___45-[PLSubmissionFilePLL prepareDatabaseAtPath:]_block_invoke.141
+ ___45-[PLSubmissionFilePLL prepareDatabaseAtPath:]_block_invoke.66
+ ___45-[PLSubmissionFilePLL prepareDatabaseAtPath:]_block_invoke.73
+ ___45-[PLSubmissionFilePLL prepareDatabaseAtPath:]_block_invoke.73.cold.1
+ ___45-[PLSubmissionFilePLL prepareDatabaseAtPath:]_block_invoke_2.152
+ ___45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke.282
+ ___45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke.297
+ ___45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke.316
+ ___45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke_2.309
+ ___46+[PLNetworkUtilities getUnattributedWakeInfo:]_block_invoke.141
+ ___46-[PLActivityCriterionEntry didEnableActivity:]_block_invoke.41
+ ___46-[PLArchiveManager trimExtendedPersistenceLog]_block_invoke.570
+ ___46-[PLOperator subscribeNotificationsForEntries]_block_invoke.160
+ ___46-[PLStorageCache insertIntoStagingEntryCache:]_block_invoke.168
+ ___46-[PPSSQLStorage handleSchemaMismatchForTable:]_block_invoke.173
+ ___46-[PPSSignpostController generateForTimeRange:]_block_invoke.58
+ ___47+[PLDefaults registerEPLNotificationWithQueue:]_block_invoke.107
+ ___47+[PLDefaults registerEPLNotificationWithQueue:]_block_invoke.99
+ ___47+[PLDefaults registerEPLNotificationWithQueue:]_block_invoke.99.cold.1
+ ___47+[PLNetworkUtilities getNormalizedIPV6Address:]_block_invoke.162
+ ___47-[PLArchiveManager trimBackgroundProcessingLog]_block_invoke.571
+ ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.250
+ ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.250.cold.1
+ ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.250.cold.2
+ ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.250.cold.3
+ ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.261
+ ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.271
+ ___48+[PLEntryKey setupEntryObjectsForOperatorClass:]_block_invoke.19
+ ___48-[PLCoreStorage writeEntry:withCompletionBlock:]_block_invoke.741
+ ___49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.711
+ ___49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.711.cold.1
+ ___49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.717
+ ___49-[PLStorageCache clearLastEntryCacheForEntryKey:]_block_invoke.63
+ ___49-[PPSCollectionOperator initOperatorDependancies]_block_invoke.34
+ ___49-[PPSCollectionOperator initOperatorDependancies]_block_invoke.41
+ ___49-[PPSCollectionOperator initOperatorDependancies]_block_invoke.56
+ ___50-[PLSQLiteConnection createTableName:withColumns:]_block_invoke.477
+ ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.265
+ ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.265.cold.1
+ ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.265.cold.2
+ ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.265.cold.3
+ ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.271
+ ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.278
+ ___50-[PLStorageCache flushBGSQLStagingCacheToDatabase]_block_invoke
+ ___50-[PLStorageCache flushBGSQLStagingCacheToDatabase]_block_invoke.cold.1
+ ___50-[PLStorageCache flushBGSQLStagingCacheToDatabase]_block_invoke.cold.2
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.187
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.193
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.199
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.209
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.209.cold.1
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.209.cold.2
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.209.cold.3
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.209.cold.4
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.209.cold.5
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.213
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.219
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.225
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.231
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.241
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke_2.210
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke_2.245
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke_3.249
+ ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.171
+ ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.180
+ ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.189
+ ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.195
+ ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.213
+ ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.219
+ ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.225
+ ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.234
+ ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.57
+ ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.63
+ ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.67
+ ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.67.cold.1
+ ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.67.cold.2
+ ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.73
+ ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.80
+ ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.86
+ ___51-[PLSQLiteConnection entriesForKey:withProperties:]_block_invoke.761
+ ___51-[PLSubmissionConfig shouldStartTrialsTaskingToday]_block_invoke
+ ___51-[PLSubmissionConfig shouldStartTrialsTaskingToday]_block_invoke.587
+ ___51-[PLSubmissionConfig shouldStartTrialsTaskingToday]_block_invoke.593
+ ___51-[PLSubmissionConfig shouldStartTrialsTaskingToday]_block_invoke.596
+ ___51-[PLSubmissionConfig shouldStartTrialsTaskingToday]_block_invoke.599
+ ___51-[PLSubmissionConfig shouldStartTrialsTaskingToday]_block_invoke.605
+ ___51-[PLSubmissionConfig shouldStartTrialsTaskingToday]_block_invoke.611
+ ___51-[RbdcConverterHelper processRbdc:withServiceType:]_block_invoke.19
+ ___51-[RbdcConverterHelper processRbdc:withServiceType:]_block_invoke.19.cold.1
+ ___53-[PLSubmissionConfig enrolledTrialsFromTaskingTrials]_block_invoke
+ ___54+[PLAppDeletion handleAppDeletionXPCActivityCallback:]_block_invoke
+ ___54+[PLAppDeletion handleAppDeletionXPCActivityCallback:]_block_invoke.cold.1
+ ___54+[PLAppDeletion handleAppDeletionXPCActivityCallback:]_block_invoke.cold.2
+ ___54+[PLAppDeletion handleAppDeletionXPCActivityCallback:]_block_invoke.cold.3
+ ___54+[PLAppDeletion handleAppDeletionXPCActivityCallback:]_block_invoke.cold.4
+ ___55-[PLCoreStorage blockingFlushCachesWithReason:timeout:]_block_invoke.697
+ ___57-[PLSubmissionFilePLL generateSubmissionTagForCurrentLog]_block_invoke.170
+ ___57-[PLSubmissionFilePLL generateSubmissionTagForCurrentLog]_block_invoke_2.171
+ ___58-[PLIOHIDOperatorComposition initWithOperator:forService:]_block_invoke.30
+ ___58-[PLIOHIDOperatorComposition initWithOperator:forService:]_block_invoke.39
+ ___58-[PLSubmissions(XPCScheduling) submitRecord:withActivity:]_block_invoke.110
+ ___58-[PLSubmissions(XPCScheduling) submitRecord:withActivity:]_block_invoke.110.cold.1
+ ___58-[PLSubmissions(XPCScheduling) submitRecord:withActivity:]_block_invoke.110.cold.2
+ ___58-[PLSubmissions(XPCScheduling) submitRecord:withActivity:]_block_invoke.111
+ ___58-[PLSubmissions(XPCScheduling) submitRecord:withActivity:]_block_invoke.112
+ ___59-[PLStorageCache flushStagingAggregateEntryCacheToDatabase]_block_invoke.258
+ ___61-[PLCoreStorage lastEntryForKey:withComparisons:isSingleton:]_block_invoke.903
+ ___61-[PLStorageCache updateStagingEntryCacheWithEntry:withBlock:]_block_invoke.174
+ ___61-[PLStorageCache updateStagingEntryCacheWithEntry:withBlock:]_block_invoke.177
+ ___61-[PLSubmissions submitRecordToDiagnosticPipeline:withConfig:]_block_invoke.204
+ ___62-[PLCoreStorage(XPCScheduling) registerDailyTasks_XPCActivity]_block_invoke.42
+ ___62-[PLCoreStorage(XPCScheduling) registerDailyTasks_XPCActivity]_block_invoke.44
+ ___63-[PLCoreStorage processEntriesForKey:withProperties:withBlock:]_block_invoke.802
+ ___64-[PLSubmissions(XPCScheduling) registerUploadSchedulingActivity]_block_invoke.17
+ ___66-[PLSubmissions generateOTASubmissionAndSendTaskingEndSubmission:]_block_invoke.158
+ ___66-[PLSubmissions generateOTASubmissionAndSendTaskingEndSubmission:]_block_invoke.162
+ ___66-[PLSubmissions generateOTASubmissionAndSendTaskingEndSubmission:]_block_invoke.163
+ ___66-[PLSubmissions generateOTASubmissionAndSendTaskingEndSubmission:]_block_invoke.164
+ ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.47
+ ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.47.cold.1
+ ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.48
+ ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.48.cold.1
+ ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.49
+ ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.49.cold.1
+ ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.50
+ ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.50.cold.1
+ ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.51
+ ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.51.cold.1
+ ___68-[PLIOKitOperatorComposition initWithOperator:forService:withBlock:]_block_invoke.37
+ ___68-[PLSQLiteConnection trimAllTablesFromDate:toDate:withTableFilters:]_block_invoke.292
+ ___68-[PLSQLiteConnection trimAllTablesFromDate:toDate:withTableFilters:]_block_invoke.312
+ ___73-[PLStorageCache logBGSQLCacheSizeWithInsertCount:updateCount:flushDate:]_block_invoke
+ ___73-[PLTimeReferenceDynamic unregisterForTimeChangedCallbackWithIdentifier:]_block_invoke.85
+ ___74+[PLUtilities getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:]_block_invoke.191
+ ___74-[PLCoreStorage handleSchemaMismatchForTable:expectedVersion:schemaMatch:]_block_invoke.567
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.128
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.128.cold.1
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.128.cold.2
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.128.cold.3
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.132
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.132.cold.1
+ ___76-[PLCoreStorage writeProportionateAggregateEntry:withStartDate:withEndDate:]_block_invoke.750
+ ___76-[PLCoreStorage writeProportionateAggregateEntry:withStartDate:withEndDate:]_block_invoke.756
+ ___77-[PLTimeManager bucketTimeStampForDate:withTimeReference:withBucketInterval:]_block_invoke.59
+ ___77-[PLTimeManager bucketTimeStampForDate:withTimeReference:withBucketInterval:]_block_invoke.65
+ ___77-[PLTimeManager bucketTimeStampForDate:withTimeReference:withBucketInterval:]_block_invoke.71
+ ___82-[PLTimeReferenceDynamic registerForTimeChangedCallbackWithIdentifier:usingBlock:]_block_invoke.79
+ ___86-[PLSubmissionConfig emitTrialsTaskingDecisionEvent:enrolledTrials:appliedPercentage:]_block_invoke
+ ___87-[PLSubmissionFile logSubmissionResultToCAWithErrorType:withFileType:withOverrideKeys:]_block_invoke.90
+ ___89-[PLOperator postFilteredNotificationForEntry:withFilteredDefition:withNotificationName:]_block_invoke.140
+ ___93-[PLEnhancedTaskingAgent logAggregatedDataFromSignpostWithPayload:withStartDate:withEndDate:]_block_invoke.123
+ ___Block_byref_object_copy_.175
+ ___Block_byref_object_copy_.736
+ ___Block_byref_object_dispose_.176
+ ___Block_byref_object_dispose_.737
+ ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_53_e8_32s40s_e19_"NSDictionary"8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e33_v24?0"TRIAllocationStatus"8^B16ls32l8s40l8s48l8
+ ___block_literal_global.103
+ ___block_literal_global.116
+ ___block_literal_global.117
+ ___block_literal_global.118
+ ___block_literal_global.128
+ ___block_literal_global.131
+ ___block_literal_global.133
+ ___block_literal_global.134
+ ___block_literal_global.138
+ ___block_literal_global.144
+ ___block_literal_global.146
+ ___block_literal_global.150
+ ___block_literal_global.156
+ ___block_literal_global.161
+ ___block_literal_global.166
+ ___block_literal_global.171
+ ___block_literal_global.176
+ ___block_literal_global.181
+ ___block_literal_global.186
+ ___block_literal_global.19
+ ___block_literal_global.191
+ ___block_literal_global.193
+ ___block_literal_global.196
+ ___block_literal_global.198
+ ___block_literal_global.203
+ ___block_literal_global.222
+ ___block_literal_global.227
+ ___block_literal_global.231
+ ___block_literal_global.235
+ ___block_literal_global.236
+ ___block_literal_global.241
+ ___block_literal_global.246
+ ___block_literal_global.251
+ ___block_literal_global.256
+ ___block_literal_global.261
+ ___block_literal_global.266
+ ___block_literal_global.267
+ ___block_literal_global.271
+ ___block_literal_global.273
+ ___block_literal_global.275
+ ___block_literal_global.279
+ ___block_literal_global.281
+ ___block_literal_global.283
+ ___block_literal_global.284
+ ___block_literal_global.288
+ ___block_literal_global.289
+ ___block_literal_global.290
+ ___block_literal_global.295
+ ___block_literal_global.297
+ ___block_literal_global.299
+ ___block_literal_global.301
+ ___block_literal_global.303
+ ___block_literal_global.305
+ ___block_literal_global.307
+ ___block_literal_global.311
+ ___block_literal_global.318
+ ___block_literal_global.325
+ ___block_literal_global.335
+ ___block_literal_global.337
+ ___block_literal_global.343
+ ___block_literal_global.344
+ ___block_literal_global.356
+ ___block_literal_global.36
+ ___block_literal_global.360
+ ___block_literal_global.361
+ ___block_literal_global.368
+ ___block_literal_global.37
+ ___block_literal_global.377
+ ___block_literal_global.379
+ ___block_literal_global.397
+ ___block_literal_global.398
+ ___block_literal_global.41
+ ___block_literal_global.441
+ ___block_literal_global.453
+ ___block_literal_global.47
+ ___block_literal_global.477
+ ___block_literal_global.483
+ ___block_literal_global.490
+ ___block_literal_global.495
+ ___block_literal_global.500
+ ___block_literal_global.505
+ ___block_literal_global.514
+ ___block_literal_global.517
+ ___block_literal_global.520
+ ___block_literal_global.523
+ ___block_literal_global.525
+ ___block_literal_global.530
+ ___block_literal_global.536
+ ___block_literal_global.544
+ ___block_literal_global.553
+ ___block_literal_global.559
+ ___block_literal_global.560
+ ___block_literal_global.568
+ ___block_literal_global.57
+ ___block_literal_global.606
+ ___block_literal_global.61
+ ___block_literal_global.617
+ ___block_literal_global.620
+ ___block_literal_global.625
+ ___block_literal_global.690
+ ___block_literal_global.71
+ ___block_literal_global.722
+ ___block_literal_global.724
+ ___block_literal_global.727
+ ___block_literal_global.731
+ ___block_literal_global.734
+ ___block_literal_global.737
+ ___block_literal_global.740
+ ___block_literal_global.78
+ ___block_literal_global.82
+ ___block_literal_global.83
+ ___block_literal_global.837
+ ___block_literal_global.860
+ ___block_literal_global.88
+ ___block_literal_global.880
+ ___block_literal_global.93
+ ___block_literal_global.943
+ ___block_literal_global.98
+ ___kQueueEvent_block_invoke.106
+ __appDeletionQueue.onceToken
+ __appDeletionQueue.queue
+ __cancel.classDebugEnabled.44
+ __cancel.classDebugEnabled.50
+ __cancel.defaultOnce.43
+ __cancel.defaultOnce.49
+ __categoryByEntryKey
+ __filterEntryLoggingByEntryKey
+ __storageByEntryKey
+ __subsystemByEntryKey
+ __timeToLiveByEntryKey
+ _addToBGSQLStagingCache:.classDebugEnabled
+ _addToBGSQLStagingCache:.defaultOnce
+ _blockingFlushCachesWithReason:timeout:.classDebugEnabled.696
+ _blockingFlushCachesWithReason:timeout:.defaultOnce.695
+ _blockingFlushQueues:withTimeout:.classDebugEnabled.706
+ _blockingFlushQueues:withTimeout:.classDebugEnabled.716
+ _blockingFlushQueues:withTimeout:.defaultOnce.705
+ _blockingFlushQueues:withTimeout:.defaultOnce.715
+ _bucketTimeStampForDate:withTimeReference:withBucketInterval:.classDebugEnabled.58
+ _bucketTimeStampForDate:withTimeReference:withBucketInterval:.classDebugEnabled.64
+ _bucketTimeStampForDate:withTimeReference:withBucketInterval:.classDebugEnabled.70
+ _bucketTimeStampForDate:withTimeReference:withBucketInterval:.defaultOnce.57
+ _bucketTimeStampForDate:withTimeReference:withBucketInterval:.defaultOnce.63
+ _bucketTimeStampForDate:withTimeReference:withBucketInterval:.defaultOnce.69
+ _checkTaskingCompletionStatus.classDebugEnabled.290
+ _checkTaskingCompletionStatus.classDebugEnabled.308
+ _checkTaskingCompletionStatus.defaultOnce.289
+ _checkTaskingCompletionStatus.defaultOnce.307
+ _clearLastEntryCacheForEntryKey:.classDebugEnabled.62
+ _clearLastEntryCacheForEntryKey:.defaultOnce.61
+ _clearTaskingDefaults.classDebugEnabled.442
+ _clearTaskingDefaults.classDebugEnabled.448
+ _clearTaskingDefaults.classDebugEnabled.454
+ _clearTaskingDefaults.defaultOnce.441
+ _clearTaskingDefaults.defaultOnce.447
+ _clearTaskingDefaults.defaultOnce.453
+ _createTableName:withColumns:.classDebugEnabled.476
+ _createTableName:withColumns:.defaultOnce.475
+ _currentTime.classDebugEnabled.39
+ _currentTime.defaultOnce.38
+ _decodeIPPacket:encryptedPath:.classDebugEnabled.170
+ _decodeIPPacket:encryptedPath:.classDebugEnabled.179
+ _decodeIPPacket:encryptedPath:.classDebugEnabled.188
+ _decodeIPPacket:encryptedPath:.classDebugEnabled.194
+ _decodeIPPacket:encryptedPath:.classDebugEnabled.212
+ _decodeIPPacket:encryptedPath:.classDebugEnabled.218
+ _decodeIPPacket:encryptedPath:.classDebugEnabled.224
+ _decodeIPPacket:encryptedPath:.classDebugEnabled.233
+ _decodeIPPacket:encryptedPath:.defaultOnce.169
+ _decodeIPPacket:encryptedPath:.defaultOnce.178
+ _decodeIPPacket:encryptedPath:.defaultOnce.187
+ _decodeIPPacket:encryptedPath:.defaultOnce.193
+ _decodeIPPacket:encryptedPath:.defaultOnce.211
+ _decodeIPPacket:encryptedPath:.defaultOnce.217
+ _decodeIPPacket:encryptedPath:.defaultOnce.223
+ _decodeIPPacket:encryptedPath:.defaultOnce.232
+ _decorateFileAtPath:.classDebugEnabled.108
+ _decorateFileAtPath:.classDebugEnabled.112
+ _decorateFileAtPath:.classDebugEnabled.119
+ _decorateFileAtPath:.classDebugEnabled.123
+ _decorateFileAtPath:.classDebugEnabled.127
+ _decorateFileAtPath:.classDebugEnabled.131
+ _decorateFileAtPath:.classDebugEnabled.135
+ _decorateFileAtPath:.defaultOnce.107
+ _decorateFileAtPath:.defaultOnce.111
+ _decorateFileAtPath:.defaultOnce.118
+ _decorateFileAtPath:.defaultOnce.122
+ _decorateFileAtPath:.defaultOnce.126
+ _decorateFileAtPath:.defaultOnce.130
+ _decorateFileAtPath:.defaultOnce.134
+ _deviceBootUUID.classDebugEnabled.162
+ _deviceBootUUID.defaultOnce.161
+ _didEnableActivity:.classDebugEnabled.27
+ _didEnableActivity:.classDebugEnabled.40
+ _didEnableActivity:.defaultOnce.26
+ _didEnableActivity:.defaultOnce.39
+ _entriesForKey:withProperties:.classDebugEnabled.760
+ _entriesForKey:withProperties:.defaultOnce.759
+ _entryIDForNewEntry:.classDebugEnabled.107
+ _entryIDForNewEntry:.classDebugEnabled.122
+ _entryIDForNewEntry:.defaultOnce.106
+ _entryIDForNewEntry:.defaultOnce.121
+ _flushCachesWithReason:.defaultOnce.674
+ _flushStagingAggregateEntryCacheToDatabase.classDebugEnabled.257
+ _flushStagingAggregateEntryCacheToDatabase.defaultOnce.256
+ _flushStagingEntryCacheToDatabase.classDebugEnabled.248
+ _flushStagingEntryCacheToDatabase.defaultOnce.186
+ _flushStagingEntryCacheToDatabase.defaultOnce.247
+ _getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:.classDebugEnabled.190
+ _getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:.defaultOnce.189
+ _getHourBucketOffset.classDebugEnabled.25
+ _getHourBucketOffset.defaultOnce.24
+ _getNetworkWakeInfo:.classDebugEnabled.131
+ _getNetworkWakeInfo:.defaultOnce.130
+ _getNormalizedIPV6Address:.classDebugEnabled.161
+ _getNormalizedIPV6Address:.defaultOnce.160
+ _getUnattributedWakeInfo:.classDebugEnabled.140
+ _getUnattributedWakeInfo:.defaultOnce.139
+ _handlePeer:forEvent:.classDebugEnabled.104
+ _handlePeer:forEvent:.classDebugEnabled.110
+ _handlePeer:forEvent:.classDebugEnabled.119
+ _handlePeer:forEvent:.classDebugEnabled.125
+ _handlePeer:forEvent:.classDebugEnabled.59
+ _handlePeer:forEvent:.classDebugEnabled.65
+ _handlePeer:forEvent:.classDebugEnabled.71
+ _handlePeer:forEvent:.classDebugEnabled.77
+ _handlePeer:forEvent:.classDebugEnabled.89
+ _handlePeer:forEvent:.classDebugEnabled.98
+ _handlePeer:forEvent:.defaultOnce.103
+ _handlePeer:forEvent:.defaultOnce.109
+ _handlePeer:forEvent:.defaultOnce.118
+ _handlePeer:forEvent:.defaultOnce.124
+ _handlePeer:forEvent:.defaultOnce.58
+ _handlePeer:forEvent:.defaultOnce.64
+ _handlePeer:forEvent:.defaultOnce.70
+ _handlePeer:forEvent:.defaultOnce.76
+ _handlePeer:forEvent:.defaultOnce.88
+ _handlePeer:forEvent:.defaultOnce.97
+ _handlePowerWakeEvent:.classDebugEnabled.152
+ _handlePowerWakeEvent:.defaultOnce.151
+ _handleSchemaMismatchForTable:expectedVersion:schemaMatch:.classDebugEnabled.566
+ _handleSchemaMismatchForTable:expectedVersion:schemaMatch:.defaultOnce.565
+ _hasPencil.onceToken
+ _hasPencil.ret
+ _init.classDebugEnabled.41
+ _init.defaultOnce.40
+ _initWithOperator:forService:.classDebugEnabled.38
+ _initWithOperator:forService:.defaultOnce.37
+ _initWithOperator:forService:withBlock:.classDebugEnabled.36
+ _initWithOperator:forService:withBlock:.defaultOnce.35
+ _insertIntoStagingEntryCache:.defaultOnce.167
+ _isESPPacket:offset:.classDebugEnabled.284
+ _isESPPacket:offset:.classDebugEnabled.290
+ _isESPPacket:offset:.defaultOnce.283
+ _isESPPacket:offset:.defaultOnce.289
+ _kBGSQLCacheLimitKey_block_invoke.classDebugEnabled
+ _kBGSQLCacheLimitKey_block_invoke.defaultOnce
+ _kBGSQLCacheLimitKey_block_invoke_2.classDebugEnabled
+ _kBGSQLCacheLimitKey_block_invoke_2.classDebugEnabled.94
+ _kBGSQLCacheLimitKey_block_invoke_2.defaultOnce
+ _kBGSQLCacheLimitKey_block_invoke_2.defaultOnce.93
+ _kBGSQLCacheLimitKey_block_invoke_3.classDebugEnabled
+ _kBGSQLCacheLimitKey_block_invoke_3.classDebugEnabled.141
+ _kBGSQLCacheLimitKey_block_invoke_3.classDebugEnabled.148
+ _kBGSQLCacheLimitKey_block_invoke_3.classDebugEnabled.154
+ _kBGSQLCacheLimitKey_block_invoke_3.defaultOnce
+ _kBGSQLCacheLimitKey_block_invoke_3.defaultOnce.140
+ _kBGSQLCacheLimitKey_block_invoke_3.defaultOnce.147
+ _kBGSQLCacheLimitKey_block_invoke_3.defaultOnce.153
+ _kBGSQLCacheLimitKey_block_invoke_4.classDebugEnabled
+ _kBGSQLCacheLimitKey_block_invoke_4.classDebugEnabled.192
+ _kBGSQLCacheLimitKey_block_invoke_4.classDebugEnabled.198
+ _kBGSQLCacheLimitKey_block_invoke_4.classDebugEnabled.204
+ _kBGSQLCacheLimitKey_block_invoke_4.classDebugEnabled.240
+ _kBGSQLCacheLimitKey_block_invoke_4.classDebugEnabled.244
+ _kBGSQLCacheLimitKey_block_invoke_4.defaultOnce
+ _kBGSQLCacheLimitKey_block_invoke_4.defaultOnce.191
+ _kBGSQLCacheLimitKey_block_invoke_4.defaultOnce.197
+ _kBGSQLCacheLimitKey_block_invoke_4.defaultOnce.203
+ _kBGSQLCacheLimitKey_block_invoke_4.defaultOnce.239
+ _kBGSQLCacheLimitKey_block_invoke_4.defaultOnce.243
+ _kBGSQLCacheLimitKey_block_invoke_5.classDebugEnabled
+ _kBGSQLCacheLimitKey_block_invoke_5.classDebugEnabled.212
+ _kBGSQLCacheLimitKey_block_invoke_5.classDebugEnabled.218
+ _kBGSQLCacheLimitKey_block_invoke_5.classDebugEnabled.224
+ _kBGSQLCacheLimitKey_block_invoke_5.classDebugEnabled.230
+ _kBGSQLCacheLimitKey_block_invoke_5.defaultOnce
+ _kBGSQLCacheLimitKey_block_invoke_5.defaultOnce.211
+ _kBGSQLCacheLimitKey_block_invoke_5.defaultOnce.217
+ _kBGSQLCacheLimitKey_block_invoke_5.defaultOnce.223
+ _kBGSQLCacheLimitKey_block_invoke_5.defaultOnce.229
+ _kBGSQLCacheLimitKey_block_invoke_6.classDebugEnabled
+ _kBGSQLCacheLimitKey_block_invoke_6.classDebugEnabled.270
+ _kBGSQLCacheLimitKey_block_invoke_6.classDebugEnabled.277
+ _kBGSQLCacheLimitKey_block_invoke_6.defaultOnce
+ _kBGSQLCacheLimitKey_block_invoke_6.defaultOnce.269
+ _kBGSQLCacheLimitKey_block_invoke_6.defaultOnce.276
+ _kBGSQLCacheLimitKey_block_invoke_7.classDebugEnabled
+ _kBGSQLCacheLimitKey_block_invoke_7.defaultOnce
+ _kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.765
+ _kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.772
+ _kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.778
+ _kPLTaskingEndNotification_block_invoke_6.defaultOnce.764
+ _kPLTaskingEndNotification_block_invoke_6.defaultOnce.771
+ _kPLTaskingEndNotification_block_invoke_6.defaultOnce.777
+ _lastEntryCachePruneToDate:.classDebugEnabled.71
+ _lastEntryCachePruneToDate:.defaultOnce.70
+ _lastEntryForKey:withComparisons:isSingleton:.classDebugEnabled.902
+ _lastEntryForKey:withComparisons:isSingleton:.defaultOnce.901
+ _logBGSQLCacheSizeWithInsertCount:updateCount:flushDate:.classDebugEnabled
+ _logBGSQLCacheSizeWithInsertCount:updateCount:flushDate:.defaultOnce
+ _logMessage:fromFile:fromFunction:fromLineNumber:.defaultOnce.952
+ _logMessage:fromFile:fromFunction:fromLineNumber:.objectForKey.953
+ _migrateArchive:.classDebugEnabled.591
+ _migrateArchive:.defaultOnce.590
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_appDeletionQueue
+ _objc_msgSend$activations
+ _objc_msgSend$addToBGSQLStagingCache:
+ _objc_msgSend$aggregationKey
+ _objc_msgSend$bgsqlCacheLimit
+ _objc_msgSend$bgsqlDedicatedCacheEnabled
+ _objc_msgSend$bgsqlFlushCountThisWindow
+ _objc_msgSend$bgsqlFlushWindowStart
+ _objc_msgSend$bgsqlStagingCache
+ _objc_msgSend$bgsqlStagingCacheSize
+ _objc_msgSend$chunkDurationSeconds
+ _objc_msgSend$chunkIndex
+ _objc_msgSend$chunksForTimeRangeStart:end:chunkDuration:
+ _objc_msgSend$client
+ _objc_msgSend$dddOverrideDateInPayload:subsystem:category:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$defaultProvider
+ _objc_msgSend$deploymentId
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$dictionaryWithContentsOfFile:
+ _objc_msgSend$emitTrialsTaskingDecisionEvent:enrolledTrials:appliedPercentage:
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$endTimestamp
+ _objc_msgSend$enrolledTrialNamespaces
+ _objc_msgSend$enrolledTrialsFromTaskingTrials
+ _objc_msgSend$enumerateExperimentStatusesForEnvironment:startingFromCursor:error:block:
+ _objc_msgSend$exits
+ _objc_msgSend$experimentId
+ _objc_msgSend$extendedLaunches
+ _objc_msgSend$flushBGSQLStagingCacheToDatabase
+ _objc_msgSend$fromDictionary:
+ _objc_msgSend$hangs
+ _objc_msgSend$indexKey
+ _objc_msgSend$initWithDomain:label:bundleID:bundleIDResolved:processName:durationMs:startDate:endDate:stableState:pid:processImageUUID:processImagePath:
+ _objc_msgSend$initWithStartTimestamp:endTimestamp:chunkIndex:
+ _objc_msgSend$initWithStateMetrics:chunkMetrics:
+ _objc_msgSend$intervalFromDictionary:
+ _objc_msgSend$intervalWithStartTimestamp:endTimestamp:chunkIndex:
+ _objc_msgSend$isBGSQLEntryKey:
+ _objc_msgSend$launches
+ _objc_msgSend$logBGSQLCacheSizeWithInsertCount:updateCount:flushDate:
+ _objc_msgSend$lookupTableGroup:
+ _objc_msgSend$metalFrameRates
+ _objc_msgSend$namespaces
+ _objc_msgSend$orderedSetWithArray:
+ _objc_msgSend$perModelTrialsPercentages
+ _objc_msgSend$remoteObjectInterface
+ _objc_msgSend$requestExperimentActivationForNamespaceName:completion:
+ _objc_msgSend$resolveTaskingTables
+ _objc_msgSend$resumes
+ _objc_msgSend$setBgsqlFlushCountThisWindow:
+ _objc_msgSend$setBgsqlFlushWindowStart:
+ _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setDeploymentId:
+ _objc_msgSend$setEnrolledTrialNamespaces:
+ _objc_msgSend$setExperimentId:
+ _objc_msgSend$setPerModelTrialsPercentages:
+ _objc_msgSend$setTaskingBaselinePercentage:
+ _objc_msgSend$setTaskingTableGroups:
+ _objc_msgSend$setTaskingTrials:
+ _objc_msgSend$setTaskingTrialsPercentage:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$shouldStartTrialsTaskingToday
+ _objc_msgSend$signpostIntervals
+ _objc_msgSend$startTimestamp
+ _objc_msgSend$taskingBaselinePercentage
+ _objc_msgSend$taskingBlobHasTrialsConfiguration
+ _objc_msgSend$taskingTableGroups
+ _objc_msgSend$taskingTrials
+ _objc_msgSend$taskingTrialsPercentage
+ _objc_msgSend$toDictionary
+ _objc_msgSend$trackBGSQLFlushFrequencyWithDate:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x7
+ _postFilteredNotificationForEntry:withFilteredDefition:withNotificationName:.classDebugEnabled.139
+ _postFilteredNotificationForEntry:withFilteredDefition:withNotificationName:.defaultOnce.138
+ _registerDailyTasks.classDebugEnabled.435
+ _registerDailyTasks.defaultOnce.434
+ _registerEPLNotificationWithQueue:.classDebugEnabled.106
+ _registerEPLNotificationWithQueue:.defaultOnce.105
+ _registerForTimeChangedCallbackWithIdentifier:usingBlock:.classDebugEnabled.78
+ _registerForTimeChangedCallbackWithIdentifier:usingBlock:.defaultOnce.77
+ _relayConnection.classDebugEnabled.157
+ _relayConnection.classDebugEnabled.163
+ _relayConnection.defaultOnce.156
+ _relayConnection.defaultOnce.162
+ _relayConnectionSync_block_invoke.classDebugEnabled.38
+ _relayConnectionSync_block_invoke.defaultOnce.37
+ _relayConnectionSync_block_invoke_3.classDebugEnabled.138
+ _relayConnectionSync_block_invoke_3.classDebugEnabled.145
+ _relayConnectionSync_block_invoke_3.classDebugEnabled.151
+ _relayConnectionSync_block_invoke_3.defaultOnce.137
+ _relayConnectionSync_block_invoke_3.defaultOnce.144
+ _relayConnectionSync_block_invoke_3.defaultOnce.150
+ _removeEmptyOldTables.classDebugEnabled.381
+ _removeEmptyOldTables.defaultOnce.380
+ _reschedule.classDebugEnabled.91
+ _reschedule.classDebugEnabled.97
+ _reschedule.defaultOnce.90
+ _reschedule.defaultOnce.96
+ _runTrimQuery:.classDebugEnabled.327
+ _runTrimQuery:.classDebugEnabled.333
+ _runTrimQuery:.defaultOnce.326
+ _runTrimQuery:.defaultOnce.332
+ _schedule.classDebugEnabled.32
+ _schedule.classDebugEnabled.39
+ _schedule.defaultOnce.31
+ _schedule.defaultOnce.38
+ _setEnabled:.classDebugEnabled.18
+ _setEnabled:.classDebugEnabled.26
+ _setEnabled:.classDebugEnabled.33
+ _setEnabled:.defaultOnce.17
+ _setEnabled:.defaultOnce.25
+ _setEnabled:.defaultOnce.32
+ _shouldStartTaskingToday.classDebugEnabled.474
+ _shouldStartTaskingToday.classDebugEnabled.480
+ _shouldStartTaskingToday.classDebugEnabled.501
+ _shouldStartTaskingToday.classDebugEnabled.507
+ _shouldStartTaskingToday.classDebugEnabled.516
+ _shouldStartTaskingToday.classDebugEnabled.537
+ _shouldStartTaskingToday.classDebugEnabled.543
+ _shouldStartTaskingToday.classDebugEnabled.549
+ _shouldStartTaskingToday.defaultOnce.473
+ _shouldStartTaskingToday.defaultOnce.479
+ _shouldStartTaskingToday.defaultOnce.500
+ _shouldStartTaskingToday.defaultOnce.506
+ _shouldStartTaskingToday.defaultOnce.515
+ _shouldStartTaskingToday.defaultOnce.536
+ _shouldStartTaskingToday.defaultOnce.542
+ _shouldStartTaskingToday.defaultOnce.548
+ _shouldStartTrialsTaskingToday.classDebugEnabled
+ _shouldStartTrialsTaskingToday.classDebugEnabled.586
+ _shouldStartTrialsTaskingToday.classDebugEnabled.592
+ _shouldStartTrialsTaskingToday.classDebugEnabled.595
+ _shouldStartTrialsTaskingToday.classDebugEnabled.598
+ _shouldStartTrialsTaskingToday.classDebugEnabled.604
+ _shouldStartTrialsTaskingToday.classDebugEnabled.610
+ _shouldStartTrialsTaskingToday.defaultOnce
+ _shouldStartTrialsTaskingToday.defaultOnce.585
+ _shouldStartTrialsTaskingToday.defaultOnce.591
+ _shouldStartTrialsTaskingToday.defaultOnce.594
+ _shouldStartTrialsTaskingToday.defaultOnce.597
+ _shouldStartTrialsTaskingToday.defaultOnce.603
+ _shouldStartTrialsTaskingToday.defaultOnce.609
+ _signalDoneByObject:.classDebugEnabled.28
+ _signalDoneByObject:.classDebugEnabled.34
+ _signalDoneByObject:.defaultOnce.27
+ _signalDoneByObject:.defaultOnce.33
+ _submitReasonForToday.classDebugEnabled.140
+ _submitReasonForToday.classDebugEnabled.146
+ _submitReasonForToday.classDebugEnabled.152
+ _submitReasonForToday.defaultOnce.139
+ _submitReasonForToday.defaultOnce.145
+ _submitReasonForToday.defaultOnce.151
+ _subscribeNotificationsForEntries.classDebugEnabled.159
+ _subscribeNotificationsForEntries.defaultOnce.158
+ _taskingModeSafeguard.classDebugEnabled.346
+ _taskingModeSafeguard.defaultOnce.345
+ _taskingTableGroups.groups
+ _taskingTableGroups.once
+ _timerFiredForMonotonicFireDate:.classDebugEnabled.56
+ _timerFiredForMonotonicFireDate:.classDebugEnabled.62
+ _timerFiredForMonotonicFireDate:.classDebugEnabled.79
+ _timerFiredForMonotonicFireDate:.classDebugEnabled.85
+ _timerFiredForMonotonicFireDate:.defaultOnce.55
+ _timerFiredForMonotonicFireDate:.defaultOnce.61
+ _timerFiredForMonotonicFireDate:.defaultOnce.78
+ _timerFiredForMonotonicFireDate:.defaultOnce.84
+ _trimAllTablesFromDate:toDate:withTableFilters:.classDebugEnabled.291
+ _trimAllTablesFromDate:toDate:withTableFilters:.classDebugEnabled.311
+ _trimAllTablesFromDate:toDate:withTableFilters:.defaultOnce.290
+ _trimAllTablesFromDate:toDate:withTableFilters:.defaultOnce.310
+ _unregisterForTimeChangedCallbackWithIdentifier:.classDebugEnabled.84
+ _unregisterForTimeChangedCallbackWithIdentifier:.defaultOnce.83
+ _updateEntry:.classDebugEnabled.670
+ _updateEntry:.classDebugEnabled.676
+ _updateEntry:.classDebugEnabled.682
+ _updateEntry:.defaultOnce.669
+ _updateEntry:.defaultOnce.675
+ _updateEntry:.defaultOnce.681
+ _updateStagingEntryCacheWithEntry:withBlock:.classDebugEnabled.173
+ _updateStagingEntryCacheWithEntry:withBlock:.defaultOnce.172
+ _waitWithBlockSync:.classDebugEnabled.47
+ _waitWithBlockSync:.defaultOnce.46
+ _writeDynamicEntries:.classDebugEnabled.631
+ _writeDynamicEntries:.defaultOnce.630
+ _writeEntry:.classDebugEnabled.574
+ _writeEntry:.defaultOnce.573
+ _writeProportionateAggregateEntry:withStartDate:withEndDate:.classDebugEnabled.749
+ _writeProportionateAggregateEntry:withStartDate:withEndDate:.classDebugEnabled.755
+ _writeProportionateAggregateEntry:withStartDate:withEndDate:.defaultOnce.748
+ _writeProportionateAggregateEntry:withStartDate:withEndDate:.defaultOnce.754
- +[PLAppDeletion handleAppDeletionXPCActivityCallback:].cold.1
- +[PLAppDeletion handleAppDeletionXPCActivityCallback:].cold.2
- +[PLAppDeletion handleAppDeletionXPCActivityCallback:].cold.3
- +[PLAppDeletion handleAppDeletionXPCActivityCallback:].cold.4
- +[PLPlatform isBasebandMavLeg]
- +[PLPlatform isBasebandMavLeg].cold.1
- -[SignpostReaderHelper getSignpostMetricsWithStartDate:withEndDate:processMXSignpost:]
- GCC_except_table36
- GCC_except_table88
- _ArrayReserved_block_invoke_2.classDebugEnabled.86
- _ArrayReserved_block_invoke_2.defaultOnce.85
- _ArrayReserved_block_invoke_3.classDebugEnabled.133
- _ArrayReserved_block_invoke_3.classDebugEnabled.140
- _ArrayReserved_block_invoke_3.classDebugEnabled.146
- _ArrayReserved_block_invoke_3.defaultOnce.132
- _ArrayReserved_block_invoke_3.defaultOnce.139
- _ArrayReserved_block_invoke_3.defaultOnce.145
- _ArrayReserved_block_invoke_4.classDebugEnabled.107
- _ArrayReserved_block_invoke_4.classDebugEnabled.184
- _ArrayReserved_block_invoke_4.classDebugEnabled.190
- _ArrayReserved_block_invoke_4.classDebugEnabled.196
- _ArrayReserved_block_invoke_4.classDebugEnabled.232
- _ArrayReserved_block_invoke_4.classDebugEnabled.236
- _ArrayReserved_block_invoke_4.defaultOnce.106
- _ArrayReserved_block_invoke_4.defaultOnce.183
- _ArrayReserved_block_invoke_4.defaultOnce.189
- _ArrayReserved_block_invoke_4.defaultOnce.195
- _ArrayReserved_block_invoke_4.defaultOnce.231
- _ArrayReserved_block_invoke_4.defaultOnce.235
- _ArrayReserved_block_invoke_5.classDebugEnabled.204
- _ArrayReserved_block_invoke_5.classDebugEnabled.210
- _ArrayReserved_block_invoke_5.classDebugEnabled.216
- _ArrayReserved_block_invoke_5.classDebugEnabled.222
- _ArrayReserved_block_invoke_5.defaultOnce.203
- _ArrayReserved_block_invoke_5.defaultOnce.209
- _ArrayReserved_block_invoke_5.defaultOnce.215
- _ArrayReserved_block_invoke_5.defaultOnce.221
- _ArrayReserved_block_invoke_6.classDebugEnabled.262
- _ArrayReserved_block_invoke_6.classDebugEnabled.269
- _ArrayReserved_block_invoke_6.defaultOnce.261
- _ArrayReserved_block_invoke_6.defaultOnce.268
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_18
- _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.69
- _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.68
- _PLSubmissionAnalyticsStateSuccess_block_invoke_2.classDebugEnabled.49
- _PLSubmissionAnalyticsStateSuccess_block_invoke_2.defaultOnce.48
- __ZNSt12length_errorC1B9nqe210106EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106ILi0EEEPKc
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB9nqe210106Ev
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B9nqe210106Ej
- __ZNSt3__116__pad_and_outputB9nqe210106IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIlEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__shared_weak_count16__release_sharedB9nqe210106Ev
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106Ev
- __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- __ZNSt3__124__put_character_sequenceB9nqe210106IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__16vectorIlNS_9allocatorIlEEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorIlNS_9allocatorIlEEE16__init_with_sizeB9nqe210106IPKlS6_EEvT_T0_m
- __ZNSt3__16vectorIlNS_9allocatorIlEEE20__throw_length_errorB9nqe210106Ev
- __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- ___104-[PLCoreStorage entriesForKey:inTimeRange:withCountOfEntriesBefore:withCountOfEntriesAfter:withFilters:]_block_invoke.853
- ___18-[PLOperator init]_block_invoke.39
- ___18-[PLXPCRelay init]_block_invoke.20
- ___21-[PLCoreStorage init]_block_invoke.112
- ___21-[PLCoreStorage init]_block_invoke.64
- ___21-[PLCoreStorage init]_block_invoke.69
- ___21-[PLCoreStorage init]_block_invoke.74
- ___21-[PLTimeManager init]_block_invoke.25
- ___21-[PLTimeManager init]_block_invoke.25.cold.1
- ___23-[PLKQueue setEnabled:]_block_invoke.16
- ___23-[PLKQueue setEnabled:]_block_invoke.24
- ___23-[PLKQueue setEnabled:]_block_invoke.31
- ___24-[PLXPCRelay startRelay]_block_invoke.30
- ___24-[PLXPCRelay startRelay]_block_invoke.30.cold.1
- ___24-[PLXPCRelay startRelay]_block_invoke.30.cold.2
- ___24-[PLXPCRelay startRelay]_block_invoke.36
- ___24-[PLXPCRelay startRelay]_block_invoke.41
- ___24-[PLXPCRelay startRelay]_block_invoke.41.cold.1
- ___24-[PLXPCRelay startRelay]_block_invoke_2.42
- ___25-[PLActivity runActivity]_block_invoke.17
- ___25-[PLActivity runActivity]_block_invoke.18
- ___25-[PLOperator flushBuffer]_block_invoke.63
- ___26-[PLOperator logDMAEntry:]_block_invoke.225
- ___26-[PLOperator postEntries:]_block_invoke.101
- ___26-[PLOperator postEntries:]_block_invoke.101.cold.1
- ___26-[PLOperator postEntries:]_block_invoke.101.cold.2
- ___26-[PLOperator postEntries:]_block_invoke.108
- ___26-[PLOperator postEntries:]_block_invoke_2.102
- ___26-[PLTimer setTimerActive:]_block_invoke.23
- ___26-[PLTimer setTimerActive:]_block_invoke.23.cold.1
- ___26-[PLTimer setTimerActive:]_block_invoke_2.24
- ___27-[PLArchiveManager migrate]_block_invoke.596
- ___27-[PLMonotonicTimer _cancel]_block_invoke.42
- ___27-[PLMonotonicTimer _cancel]_block_invoke.48
- ___28-[PLMonotonicTimer schedule]_block_invoke.30
- ___28-[PLMonotonicTimer schedule]_block_invoke.34
- ___29+[PLUtilities deviceBootUUID]_block_invoke.118
- ___29-[PLXPCRelay relayConnection]_block_invoke.133
- ___29-[PLXPCRelay relayConnection]_block_invoke.133.cold.1
- ___29-[PLXPCRelay relayConnection]_block_invoke.133.cold.2
- ___29-[PLXPCRelay relayConnection]_block_invoke.133.cold.3
- ___29-[PLXPCRelay relayConnection]_block_invoke.133.cold.4
- ___29-[PLXPCRelay relayConnection]_block_invoke.143
- ___29-[PLXPCRelay relayConnection]_block_invoke.149
- ___29-[PLXPCRelay relayConnection]_block_invoke.155
- ___29-[PLXPCRelay relayConnection]_block_invoke.161
- ___30+[PLPlatform isBasebandMavLeg]_block_invoke
- ___30-[PLMonotonicTimer reschedule]_block_invoke.89
- ___30-[PLMonotonicTimer reschedule]_block_invoke.95
- ___32-[PLABMClient regMetricListener]_block_invoke.68
- ___32-[PLABMClient regMetricListener]_block_invoke.68.cold.1
- ___32-[PLABMClient regMetricListener]_block_invoke.68.cold.2
- ___33-[PLSemaphore waitWithBlockSync:]_block_invoke.45
- ___33-[PLSubmissions taskingModeSetup]_block_invoke.350
- ___33-[PLSubmissions taskingModeSetup]_block_invoke.365
- ___33-[PLSubmissions taskingModeSetup]_block_invoke_2.360
- ___34-[PLSQLiteConnection updateEntry:]_block_invoke.668
- ___34-[PLSQLiteConnection updateEntry:]_block_invoke.674
- ___34-[PLSQLiteConnection updateEntry:]_block_invoke.680
- ___34-[PLSemaphore signalDoneByObject:]_block_invoke.26
- ___34-[PLSemaphore signalDoneByObject:]_block_invoke.32
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.102
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.108
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.117
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.123
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.57
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.63
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.69
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.75
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.87
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.96
- ___35-[PLArchiveManager migrateArchive:]_block_invoke.580
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke.427
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke.427.cold.1
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke.433
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke.438
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke.438.cold.1
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke_2.439
- ___35-[PLSQLiteConnection runTrimQuery:]_block_invoke.325
- ___35-[PLSQLiteConnection runTrimQuery:]_block_invoke.331
- ___35-[PLSubmissions performSubmission:]_block_invoke.164
- ___35-[PPSCoreStorage setupEntryObjects]_block_invoke.31
- ___36-[PLTimeReferenceDynamic setOffset:]_block_invoke.50
- ___36-[PPSSignpostServiceConnection init]_block_invoke.14
- ___36-[PPSSignpostServiceConnection init]_block_invoke.14.cold.1
- ___37+[PLUtilities exitWithReason:action:]_block_invoke.188
- ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.756
- ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.762
- ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.769
- ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.775
- ___37-[PLStorageCache entryIDForNewEntry:]_block_invoke.100
- ___37-[PLStorageCache entryIDForNewEntry:]_block_invoke.115
- ___37-[PLSubmissions submitReasonForToday]_block_invoke.133
- ___37-[PLSubmissions submitReasonForToday]_block_invoke.139
- ___37-[PLSubmissions submitReasonForToday]_block_invoke.145
- ___37-[PLSubmissions taskingModeSafeguard]_block_invoke.327
- ___37-[PPSSignpostController _handleTask:]_block_invoke.107
- ___38-[PLStorageCache addToLastEntryCache:]_block_invoke.87
- ___38-[PLSubmissionFileBDC getBDCPlistFile]_block_invoke.50
- ___38-[PLSubmissionFileBDC getBDCPlistFile]_block_invoke.50.cold.1
- ___38-[PLTimeReference getHourBucketOffset]_block_invoke.23
- ___38-[PLTimeReferenceBaseband currentTime]_block_invoke.29
- ___38-[PLTimeReferenceBaseband currentTime]_block_invoke.29.cold.1
- ___38-[PLTimeReferenceBaseband currentTime]_block_invoke.37
- ___39+[PLAppDeletion constructUpdateQueries]_block_invoke.109
- ___39-[PLCoreStorage flushCachesWithReason:]_block_invoke.670
- ___39-[PLCoreStorage flushCachesWithReason:]_block_invoke.672
- ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.106
- ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.110
- ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.117
- ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.121
- ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.125
- ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.129
- ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.133
- ___39-[PLSubmissionFileSP copyAndPrepareLog]_block_invoke.142
- ___39-[PPSCoreStorage mergePreUnlockDBFiles]_block_invoke.50
- ___39-[PPSCoreStorage mergePreUnlockDBFiles]_block_invoke.50.cold.1
- ___39-[PPSCoreStorage mergePreUnlockDBFiles]_block_invoke.50.cold.2
- ___41+[PLNetworkUtilities getNetworkWakeInfo:]_block_invoke.129
- ___41+[PLNetworkUtilities isESPPacket:offset:]_block_invoke.282
- ___41+[PLNetworkUtilities isESPPacket:offset:]_block_invoke.288
- ___41-[PLCoreStorage initOperatorDependancies]_block_invoke.330
- ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.128
- ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.128.cold.1
- ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.128.cold.2
- ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.128.cold.3
- ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.128.cold.4
- ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.134
- ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.141
- ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.147
- ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.390
- ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.396
- ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.402
- ___42-[PLSQLiteConnection removeEmptyOldTables]_block_invoke.379
- ___42-[PLSQLiteConnection writeDynamicEntries:]_block_invoke.629
- ___42-[RbdcConverterHelper createXPCConnection]_block_invoke.44
- ___42-[RbdcConverterHelper createXPCConnection]_block_invoke.44.cold.1
- ___43+[PLNetworkUtilities handlePowerWakeEvent:]_block_invoke.147
- ___43-[SignpostReaderHelper createXPCConnection]_block_invoke.53
- ___43-[SignpostReaderHelper createXPCConnection]_block_invoke.53.cold.1
- ___43-[SignpostReaderHelper createXPCConnection]_block_invoke.56
- ___43-[SignpostReaderHelper createXPCConnection]_block_invoke.56.cold.1
- ___44-[PLSQLiteConnection scheduleIntegrityCheck]_block_invoke.77
- ___44-[PLStorageCache lastEntryCachePruneToDate:]_block_invoke.64
- ___44-[PLStorageCache lastEntryCachePruneToDate:]_block_invoke.69
- ___44-[PLSubmissions handleDRConfigUpdate:error:]_block_invoke.114
- ___45-[PLActivityCriterionTime didEnableActivity:]_block_invoke.25
- ___45-[PLActivityCriterionTime didEnableActivity:]_block_invoke.30
- ___45-[PLActivityCriterionTime didEnableActivity:]_block_invoke.30.cold.1
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.422
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.428
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.438
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.449
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.455
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.464
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.486
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.492
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.498
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.505
- ___45-[PLSubmissionFilePLL prepareDatabaseAtPath:]_block_invoke.111
- ___45-[PLSubmissionFilePLL prepareDatabaseAtPath:]_block_invoke.125
- ___45-[PLSubmissionFilePLL prepareDatabaseAtPath:]_block_invoke.57
- ___45-[PLSubmissionFilePLL prepareDatabaseAtPath:]_block_invoke.57.cold.1
- ___45-[PLSubmissionFilePLL prepareDatabaseAtPath:]_block_invoke_2.136
- ___45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke.274
- ___45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke.289
- ___45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke.308
- ___45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke_2.301
- ___46+[PLNetworkUtilities getUnattributedWakeInfo:]_block_invoke.138
- ___46-[PLActivityCriterionEntry didEnableActivity:]_block_invoke.38
- ___46-[PLArchiveManager trimExtendedPersistenceLog]_block_invoke.558
- ___46-[PLOperator subscribeNotificationsForEntries]_block_invoke.157
- ___46-[PLStorageCache insertIntoStagingEntryCache:]_block_invoke.160
- ___46-[PPSSQLStorage handleSchemaMismatchForTable:]_block_invoke.170
- ___46-[PPSSignpostController generateForTimeRange:]_block_invoke.56
- ___47+[PLDefaults registerEPLNotificationWithQueue:]_block_invoke.104
- ___47+[PLDefaults registerEPLNotificationWithQueue:]_block_invoke.96
- ___47+[PLDefaults registerEPLNotificationWithQueue:]_block_invoke.96.cold.1
- ___47+[PLNetworkUtilities getNormalizedIPV6Address:]_block_invoke.159
- ___47-[PLArchiveManager trimBackgroundProcessingLog]_block_invoke.559
- ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.247
- ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.247.cold.1
- ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.247.cold.2
- ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.247.cold.3
- ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.258
- ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.268
- ___48+[PLEntryKey setupEntryObjectsForOperatorClass:]_block_invoke.16
- ___48-[PLCoreStorage writeEntry:withCompletionBlock:]_block_invoke.737
- ___49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.703
- ___49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.707.cold.1
- ___49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.713
- ___49-[PLStorageCache clearLastEntryCacheForEntryKey:]_block_invoke.55
- ___49-[PPSCollectionOperator initOperatorDependancies]_block_invoke.31
- ___49-[PPSCollectionOperator initOperatorDependancies]_block_invoke.38
- ___49-[PPSCollectionOperator initOperatorDependancies]_block_invoke.53
- ___50-[PLSQLiteConnection createTableName:withColumns:]_block_invoke.474
- ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.257
- ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.257.cold.1
- ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.257.cold.2
- ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.257.cold.3
- ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.263
- ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.270
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.179
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.185
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.191
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.197
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.201
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.201.cold.1
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.201.cold.2
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.201.cold.3
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.201.cold.4
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.201.cold.5
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.211
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.217
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.223
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.233
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke_2.202
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke_2.237
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke_3.241
- ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.168
- ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.177
- ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.186
- ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.192
- ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.210
- ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.216
- ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.222
- ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.231
- ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.54
- ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.60
- ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.64
- ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.64.cold.1
- ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.64.cold.2
- ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.70
- ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.77
- ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.83
- ___51-[PLSQLiteConnection entriesForKey:withProperties:]_block_invoke.758
- ___51-[RbdcConverterHelper processRbdc:withServiceType:]_block_invoke.16
- ___51-[RbdcConverterHelper processRbdc:withServiceType:]_block_invoke.16.cold.1
- ___55-[PLCoreStorage blockingFlushCachesWithReason:timeout:]_block_invoke.694
- ___57-[PLSubmissionFilePLL generateSubmissionTagForCurrentLog]_block_invoke.154
- ___57-[PLSubmissionFilePLL generateSubmissionTagForCurrentLog]_block_invoke_2.155
- ___58-[PLIOHIDOperatorComposition initWithOperator:forService:]_block_invoke.27
- ___58-[PLIOHIDOperatorComposition initWithOperator:forService:]_block_invoke.36
- ___58-[PLSubmissions(XPCScheduling) submitRecord:withActivity:]_block_invoke.107
- ___58-[PLSubmissions(XPCScheduling) submitRecord:withActivity:]_block_invoke.107.cold.1
- ___58-[PLSubmissions(XPCScheduling) submitRecord:withActivity:]_block_invoke.107.cold.2
- ___58-[PLSubmissions(XPCScheduling) submitRecord:withActivity:]_block_invoke.108
- ___58-[PLSubmissions(XPCScheduling) submitRecord:withActivity:]_block_invoke.109
- ___59-[PLStorageCache flushStagingAggregateEntryCacheToDatabase]_block_invoke.250
- ___61-[PLCoreStorage lastEntryForKey:withComparisons:isSingleton:]_block_invoke.899
- ___61-[PLStorageCache updateStagingEntryCacheWithEntry:withBlock:]_block_invoke.166
- ___61-[PLStorageCache updateStagingEntryCacheWithEntry:withBlock:]_block_invoke.169
- ___61-[PLSubmissions submitRecordToDiagnosticPipeline:withConfig:]_block_invoke.196
- ___62-[PLCoreStorage(XPCScheduling) registerDailyTasks_XPCActivity]_block_invoke.39
- ___62-[PLCoreStorage(XPCScheduling) registerDailyTasks_XPCActivity]_block_invoke.41
- ___63-[PLCoreStorage processEntriesForKey:withProperties:withBlock:]_block_invoke.798
- ___64-[PLSubmissions(XPCScheduling) registerUploadSchedulingActivity]_block_invoke.14
- ___66-[PLSubmissions generateOTASubmissionAndSendTaskingEndSubmission:]_block_invoke.150
- ___66-[PLSubmissions generateOTASubmissionAndSendTaskingEndSubmission:]_block_invoke.154
- ___66-[PLSubmissions generateOTASubmissionAndSendTaskingEndSubmission:]_block_invoke.155
- ___66-[PLSubmissions generateOTASubmissionAndSendTaskingEndSubmission:]_block_invoke.156
- ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.35
- ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.35.cold.1
- ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.36
- ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.36.cold.1
- ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.37
- ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.37.cold.1
- ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.38
- ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.38.cold.1
- ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.39
- ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.39.cold.1
- ___68-[PLIOKitOperatorComposition initWithOperator:forService:withBlock:]_block_invoke.34
- ___68-[PLSQLiteConnection trimAllTablesFromDate:toDate:withTableFilters:]_block_invoke.289
- ___68-[PLSQLiteConnection trimAllTablesFromDate:toDate:withTableFilters:]_block_invoke.309
- ___73-[PLTimeReferenceDynamic unregisterForTimeChangedCallbackWithIdentifier:]_block_invoke.82
- ___74+[PLUtilities getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:]_block_invoke.146
- ___74-[PLCoreStorage handleSchemaMismatchForTable:expectedVersion:schemaMatch:]_block_invoke.564
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.83
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.83.cold.1
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.83.cold.2
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.83.cold.3
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.87
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.87.cold.1
- ___76-[PLCoreStorage writeProportionateAggregateEntry:withStartDate:withEndDate:]_block_invoke.746
- ___76-[PLCoreStorage writeProportionateAggregateEntry:withStartDate:withEndDate:]_block_invoke.752
- ___77-[PLTimeManager bucketTimeStampForDate:withTimeReference:withBucketInterval:]_block_invoke.56
- ___77-[PLTimeManager bucketTimeStampForDate:withTimeReference:withBucketInterval:]_block_invoke.62
- ___77-[PLTimeManager bucketTimeStampForDate:withTimeReference:withBucketInterval:]_block_invoke.68
- ___82-[PLTimeReferenceDynamic registerForTimeChangedCallbackWithIdentifier:usingBlock:]_block_invoke.76
- ___87-[PLSubmissionFile logSubmissionResultToCAWithErrorType:withFileType:withOverrideKeys:]_block_invoke.87
- ___89-[PLOperator postFilteredNotificationForEntry:withFilteredDefition:withNotificationName:]_block_invoke.137
- ___93-[PLEnhancedTaskingAgent logAggregatedDataFromSignpostWithPayload:withStartDate:withEndDate:]_block_invoke.120
- ___Block_byref_object_copy_.167
- ___Block_byref_object_copy_.732
- ___Block_byref_object_dispose_.168
- ___Block_byref_object_dispose_.733
- ___block_literal_global.100
- ___block_literal_global.105
- ___block_literal_global.11
- ___block_literal_global.110
- ___block_literal_global.111
- ___block_literal_global.115
- ___block_literal_global.120
- ___block_literal_global.125
- ___block_literal_global.130
- ___block_literal_global.135
- ___block_literal_global.148
- ___block_literal_global.158
- ___block_literal_global.163
- ___block_literal_global.173
- ___block_literal_global.178
- ___block_literal_global.183
- ___block_literal_global.185
- ___block_literal_global.190
- ___block_literal_global.192
- ___block_literal_global.197
- ___block_literal_global.207
- ___block_literal_global.208
- ___block_literal_global.218
- ___block_literal_global.219
- ___block_literal_global.226
- ___block_literal_global.228
- ___block_literal_global.233
- ___block_literal_global.238
- ___block_literal_global.243
- ___block_literal_global.244
- ___block_literal_global.248
- ___block_literal_global.258
- ___block_literal_global.26
- ___block_literal_global.260
- ___block_literal_global.262
- ___block_literal_global.268
- ___block_literal_global.270
- ___block_literal_global.272
- ___block_literal_global.276
- ___block_literal_global.278
- ___block_literal_global.280
- ___block_literal_global.285
- ___block_literal_global.287
- ___block_literal_global.291
- ___block_literal_global.292
- ___block_literal_global.294
- ___block_literal_global.298
- ___block_literal_global.300
- ___block_literal_global.302
- ___block_literal_global.304
- ___block_literal_global.308
- ___block_literal_global.310
- ___block_literal_global.313
- ___block_literal_global.329
- ___block_literal_global.332
- ___block_literal_global.334
- ___block_literal_global.341
- ___block_literal_global.352
- ___block_literal_global.353
- ___block_literal_global.365
- ___block_literal_global.374
- ___block_literal_global.387
- ___block_literal_global.396
- ___block_literal_global.408
- ___block_literal_global.42
- ___block_literal_global.432
- ___block_literal_global.438
- ___block_literal_global.44
- ___block_literal_global.440
- ___block_literal_global.445
- ___block_literal_global.450
- ___block_literal_global.455
- ___block_literal_global.460
- ___block_literal_global.462
- ___block_literal_global.466
- ___block_literal_global.469
- ___block_literal_global.472
- ___block_literal_global.475
- ___block_literal_global.480
- ___block_literal_global.491
- ___block_literal_global.499
- ___block_literal_global.5
- ___block_literal_global.50
- ___block_literal_global.508
- ___block_literal_global.516
- ___block_literal_global.548
- ___block_literal_global.55
- ___block_literal_global.56
- ___block_literal_global.561
- ___block_literal_global.572
- ___block_literal_global.575
- ___block_literal_global.580
- ___block_literal_global.65
- ___block_literal_global.678
- ___block_literal_global.684
- ___block_literal_global.752
- ___block_literal_global.754
- ___block_literal_global.757
- ___block_literal_global.761
- ___block_literal_global.764
- ___block_literal_global.767
- ___block_literal_global.770
- ___block_literal_global.80
- ___block_literal_global.833
- ___block_literal_global.85
- ___block_literal_global.856
- ___block_literal_global.86
- ___block_literal_global.876
- ___block_literal_global.89
- ___block_literal_global.90
- ___block_literal_global.95
- ___block_literal_global.974
- ___block_literal_global.99
- ___kQueueEvent_block_invoke.104
- __cancel.classDebugEnabled.41
- __cancel.classDebugEnabled.47
- __cancel.defaultOnce.40
- __cancel.defaultOnce.46
- _blockingFlushCachesWithReason:timeout:.classDebugEnabled.693
- _blockingFlushCachesWithReason:timeout:.defaultOnce.692
- _blockingFlushQueues:withTimeout:.classDebugEnabled.702
- _blockingFlushQueues:withTimeout:.classDebugEnabled.712
- _blockingFlushQueues:withTimeout:.defaultOnce.701
- _blockingFlushQueues:withTimeout:.defaultOnce.711
- _bucketTimeStampForDate:withTimeReference:withBucketInterval:.classDebugEnabled.55
- _bucketTimeStampForDate:withTimeReference:withBucketInterval:.classDebugEnabled.61
- _bucketTimeStampForDate:withTimeReference:withBucketInterval:.classDebugEnabled.67
- _bucketTimeStampForDate:withTimeReference:withBucketInterval:.defaultOnce.54
- _bucketTimeStampForDate:withTimeReference:withBucketInterval:.defaultOnce.60
- _bucketTimeStampForDate:withTimeReference:withBucketInterval:.defaultOnce.66
- _checkTaskingCompletionStatus.classDebugEnabled.282
- _checkTaskingCompletionStatus.classDebugEnabled.300
- _checkTaskingCompletionStatus.defaultOnce.281
- _checkTaskingCompletionStatus.defaultOnce.299
- _clearLastEntryCacheForEntryKey:.classDebugEnabled.54
- _clearLastEntryCacheForEntryKey:.defaultOnce.53
- _clearTaskingDefaults.classDebugEnabled.389
- _clearTaskingDefaults.classDebugEnabled.395
- _clearTaskingDefaults.classDebugEnabled.401
- _clearTaskingDefaults.defaultOnce.388
- _clearTaskingDefaults.defaultOnce.394
- _clearTaskingDefaults.defaultOnce.400
- _createTableName:withColumns:.classDebugEnabled.473
- _createTableName:withColumns:.defaultOnce.472
- _currentTime.classDebugEnabled.36
- _currentTime.defaultOnce.35
- _decodeIPPacket:encryptedPath:.classDebugEnabled.167
- _decodeIPPacket:encryptedPath:.classDebugEnabled.176
- _decodeIPPacket:encryptedPath:.classDebugEnabled.185
- _decodeIPPacket:encryptedPath:.classDebugEnabled.191
- _decodeIPPacket:encryptedPath:.classDebugEnabled.209
- _decodeIPPacket:encryptedPath:.classDebugEnabled.215
- _decodeIPPacket:encryptedPath:.classDebugEnabled.221
- _decodeIPPacket:encryptedPath:.classDebugEnabled.230
- _decodeIPPacket:encryptedPath:.defaultOnce.166
- _decodeIPPacket:encryptedPath:.defaultOnce.175
- _decodeIPPacket:encryptedPath:.defaultOnce.184
- _decodeIPPacket:encryptedPath:.defaultOnce.190
- _decodeIPPacket:encryptedPath:.defaultOnce.208
- _decodeIPPacket:encryptedPath:.defaultOnce.214
- _decodeIPPacket:encryptedPath:.defaultOnce.220
- _decodeIPPacket:encryptedPath:.defaultOnce.229
- _decorateFileAtPath:.classDebugEnabled.105
- _decorateFileAtPath:.classDebugEnabled.109
- _decorateFileAtPath:.classDebugEnabled.116
- _decorateFileAtPath:.classDebugEnabled.120
- _decorateFileAtPath:.classDebugEnabled.124
- _decorateFileAtPath:.classDebugEnabled.128
- _decorateFileAtPath:.classDebugEnabled.132
- _decorateFileAtPath:.defaultOnce.104
- _decorateFileAtPath:.defaultOnce.108
- _decorateFileAtPath:.defaultOnce.115
- _decorateFileAtPath:.defaultOnce.119
- _decorateFileAtPath:.defaultOnce.123
- _decorateFileAtPath:.defaultOnce.127
- _decorateFileAtPath:.defaultOnce.131
- _deviceBootUUID.classDebugEnabled.117
- _deviceBootUUID.defaultOnce.116
- _didEnableActivity:.classDebugEnabled.24
- _didEnableActivity:.classDebugEnabled.37
- _didEnableActivity:.defaultOnce.23
- _didEnableActivity:.defaultOnce.36
- _entriesForKey:withProperties:.classDebugEnabled.757
- _entriesForKey:withProperties:.defaultOnce.756
- _entryIDForNewEntry:.classDebugEnabled.114
- _entryIDForNewEntry:.classDebugEnabled.99
- _entryIDForNewEntry:.defaultOnce.113
- _entryIDForNewEntry:.defaultOnce.98
- _flushCachesWithReason:.defaultOnce.671
- _flushStagingAggregateEntryCacheToDatabase.classDebugEnabled.249
- _flushStagingAggregateEntryCacheToDatabase.defaultOnce.248
- _flushStagingEntryCacheToDatabase.classDebugEnabled.240
- _flushStagingEntryCacheToDatabase.defaultOnce.178
- _flushStagingEntryCacheToDatabase.defaultOnce.239
- _getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:.classDebugEnabled.145
- _getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:.defaultOnce.144
- _getHourBucketOffset.classDebugEnabled.22
- _getHourBucketOffset.defaultOnce.21
- _getNetworkWakeInfo:.classDebugEnabled.128
- _getNetworkWakeInfo:.defaultOnce.127
- _getNormalizedIPV6Address:.classDebugEnabled.158
- _getNormalizedIPV6Address:.defaultOnce.157
- _getUnattributedWakeInfo:.classDebugEnabled.137
- _getUnattributedWakeInfo:.defaultOnce.136
- _handlePeer:forEvent:.classDebugEnabled.101
- _handlePeer:forEvent:.classDebugEnabled.107
- _handlePeer:forEvent:.classDebugEnabled.116
- _handlePeer:forEvent:.classDebugEnabled.122
- _handlePeer:forEvent:.classDebugEnabled.56
- _handlePeer:forEvent:.classDebugEnabled.62
- _handlePeer:forEvent:.classDebugEnabled.68
- _handlePeer:forEvent:.classDebugEnabled.74
- _handlePeer:forEvent:.classDebugEnabled.86
- _handlePeer:forEvent:.classDebugEnabled.95
- _handlePeer:forEvent:.defaultOnce.100
- _handlePeer:forEvent:.defaultOnce.106
- _handlePeer:forEvent:.defaultOnce.115
- _handlePeer:forEvent:.defaultOnce.121
- _handlePeer:forEvent:.defaultOnce.55
- _handlePeer:forEvent:.defaultOnce.61
- _handlePeer:forEvent:.defaultOnce.67
- _handlePeer:forEvent:.defaultOnce.73
- _handlePeer:forEvent:.defaultOnce.85
- _handlePeer:forEvent:.defaultOnce.94
- _handlePowerWakeEvent:.classDebugEnabled.146
- _handlePowerWakeEvent:.defaultOnce.145
- _handleSchemaMismatchForTable:expectedVersion:schemaMatch:.classDebugEnabled.563
- _handleSchemaMismatchForTable:expectedVersion:schemaMatch:.defaultOnce.562
- _init.classDebugEnabled.38
- _init.defaultOnce.37
- _initWithOperator:forService:.classDebugEnabled.35
- _initWithOperator:forService:.defaultOnce.34
- _initWithOperator:forService:withBlock:.classDebugEnabled.33
- _initWithOperator:forService:withBlock:.defaultOnce.32
- _insertIntoStagingEntryCache:.defaultOnce.159
- _isBasebandMavLeg.onceToken
- _isBasebandMavLeg.result
- _isESPPacket:offset:.classDebugEnabled.281
- _isESPPacket:offset:.classDebugEnabled.287
- _isESPPacket:offset:.defaultOnce.280
- _isESPPacket:offset:.defaultOnce.286
- _kPLBB16
- _kPLBB17
- _kPLIce
- _kPLJ2
- _kPLJ72
- _kPLJ72A
- _kPLJ81N
- _kPLJ86
- _kPLJ86A
- _kPLK94
- _kPLMav1
- _kPLMav10
- _kPLMav13
- _kPLMav16
- _kPLMav16B
- _kPLMav2
- _kPLMav4
- _kPLMav5
- _kPLMav7
- _kPLN48
- _kPLN61A
- _kPLN61B
- _kPLN94
- _kPLP102
- _kPLP105
- _kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.761
- _kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.768
- _kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.774
- _kPLTaskingEndNotification_block_invoke_6.defaultOnce.760
- _kPLTaskingEndNotification_block_invoke_6.defaultOnce.767
- _kPLTaskingEndNotification_block_invoke_6.defaultOnce.773
- _lastEntryCachePruneToDate:.classDebugEnabled.63
- _lastEntryCachePruneToDate:.defaultOnce.62
- _lastEntryForKey:withComparisons:isSingleton:.classDebugEnabled.898
- _lastEntryForKey:withComparisons:isSingleton:.defaultOnce.897
- _logMessage:fromFile:fromFunction:fromLineNumber:.defaultOnce.948
- _logMessage:fromFile:fromFunction:fromLineNumber:.objectForKey.949
- _migrateArchive:.classDebugEnabled.579
- _migrateArchive:.defaultOnce.578
- _postFilteredNotificationForEntry:withFilteredDefition:withNotificationName:.classDebugEnabled.136
- _postFilteredNotificationForEntry:withFilteredDefition:withNotificationName:.defaultOnce.135
- _registerDailyTasks.classDebugEnabled.432
- _registerDailyTasks.defaultOnce.431
- _registerEPLNotificationWithQueue:.classDebugEnabled.103
- _registerEPLNotificationWithQueue:.defaultOnce.102
- _registerForTimeChangedCallbackWithIdentifier:usingBlock:.classDebugEnabled.75
- _registerForTimeChangedCallbackWithIdentifier:usingBlock:.defaultOnce.74
- _relayConnection.classDebugEnabled.154
- _relayConnection.classDebugEnabled.160
- _relayConnection.defaultOnce.153
- _relayConnection.defaultOnce.159
- _relayConnectionSync_block_invoke.classDebugEnabled.35
- _relayConnectionSync_block_invoke.defaultOnce.34
- _relayConnectionSync_block_invoke_3.classDebugEnabled.135
- _relayConnectionSync_block_invoke_3.classDebugEnabled.142
- _relayConnectionSync_block_invoke_3.classDebugEnabled.148
- _relayConnectionSync_block_invoke_3.defaultOnce.134
- _relayConnectionSync_block_invoke_3.defaultOnce.141
- _relayConnectionSync_block_invoke_3.defaultOnce.147
- _removeEmptyOldTables.classDebugEnabled.378
- _removeEmptyOldTables.defaultOnce.377
- _reschedule.classDebugEnabled.88
- _reschedule.classDebugEnabled.94
- _reschedule.defaultOnce.87
- _reschedule.defaultOnce.93
- _runTrimQuery:.classDebugEnabled.324
- _runTrimQuery:.classDebugEnabled.330
- _runTrimQuery:.defaultOnce.323
- _runTrimQuery:.defaultOnce.329
- _schedule.classDebugEnabled.29
- _schedule.classDebugEnabled.36
- _schedule.defaultOnce.28
- _schedule.defaultOnce.35
- _setEnabled:.classDebugEnabled.15
- _setEnabled:.classDebugEnabled.23
- _setEnabled:.classDebugEnabled.30
- _setEnabled:.defaultOnce.14
- _setEnabled:.defaultOnce.22
- _setEnabled:.defaultOnce.29
- _shouldStartTaskingToday.classDebugEnabled.421
- _shouldStartTaskingToday.classDebugEnabled.427
- _shouldStartTaskingToday.classDebugEnabled.448
- _shouldStartTaskingToday.classDebugEnabled.454
- _shouldStartTaskingToday.classDebugEnabled.463
- _shouldStartTaskingToday.classDebugEnabled.485
- _shouldStartTaskingToday.classDebugEnabled.491
- _shouldStartTaskingToday.classDebugEnabled.497
- _shouldStartTaskingToday.defaultOnce.420
- _shouldStartTaskingToday.defaultOnce.426
- _shouldStartTaskingToday.defaultOnce.447
- _shouldStartTaskingToday.defaultOnce.453
- _shouldStartTaskingToday.defaultOnce.462
- _shouldStartTaskingToday.defaultOnce.484
- _shouldStartTaskingToday.defaultOnce.490
- _shouldStartTaskingToday.defaultOnce.496
- _signalDoneByObject:.classDebugEnabled.25
- _signalDoneByObject:.classDebugEnabled.31
- _signalDoneByObject:.defaultOnce.24
- _signalDoneByObject:.defaultOnce.30
- _submitReasonForToday.classDebugEnabled.132
- _submitReasonForToday.classDebugEnabled.138
- _submitReasonForToday.classDebugEnabled.144
- _submitReasonForToday.defaultOnce.131
- _submitReasonForToday.defaultOnce.137
- _submitReasonForToday.defaultOnce.143
- _subscribeNotificationsForEntries.classDebugEnabled.156
- _subscribeNotificationsForEntries.defaultOnce.155
- _taskingModeSafeguard.classDebugEnabled.338
- _taskingModeSafeguard.defaultOnce.337
- _timerFiredForMonotonicFireDate:.classDebugEnabled.53
- _timerFiredForMonotonicFireDate:.classDebugEnabled.59
- _timerFiredForMonotonicFireDate:.classDebugEnabled.76
- _timerFiredForMonotonicFireDate:.classDebugEnabled.82
- _timerFiredForMonotonicFireDate:.defaultOnce.52
- _timerFiredForMonotonicFireDate:.defaultOnce.58
- _timerFiredForMonotonicFireDate:.defaultOnce.75
- _timerFiredForMonotonicFireDate:.defaultOnce.81
- _trimAllTablesFromDate:toDate:withTableFilters:.classDebugEnabled.288
- _trimAllTablesFromDate:toDate:withTableFilters:.classDebugEnabled.308
- _trimAllTablesFromDate:toDate:withTableFilters:.defaultOnce.287
- _trimAllTablesFromDate:toDate:withTableFilters:.defaultOnce.307
- _unregisterForTimeChangedCallbackWithIdentifier:.classDebugEnabled.81
- _unregisterForTimeChangedCallbackWithIdentifier:.defaultOnce.80
- _updateEntry:.classDebugEnabled.667
- _updateEntry:.classDebugEnabled.673
- _updateEntry:.classDebugEnabled.679
- _updateEntry:.defaultOnce.666
- _updateEntry:.defaultOnce.672
- _updateEntry:.defaultOnce.678
- _updateStagingEntryCacheWithEntry:withBlock:.classDebugEnabled.165
- _updateStagingEntryCacheWithEntry:withBlock:.defaultOnce.164
- _waitWithBlockSync:.classDebugEnabled.44
- _waitWithBlockSync:.defaultOnce.43
- _writeDynamicEntries:.classDebugEnabled.628
- _writeDynamicEntries:.defaultOnce.627
- _writeEntry:.classDebugEnabled.571
- _writeEntry:.defaultOnce.570
- _writeProportionateAggregateEntry:withStartDate:withEndDate:.classDebugEnabled.745
- _writeProportionateAggregateEntry:withStartDate:withEndDate:.classDebugEnabled.751
- _writeProportionateAggregateEntry:withStartDate:withEndDate:.defaultOnce.744
- _writeProportionateAggregateEntry:withStartDate:withEndDate:.defaultOnce.750
CStrings:
+ "%@_%ld_%ld"
+ "%@__%@__%@__%@"
+ "%@__unattributed_0"
+ "-[PLStorageCache addToBGSQLStagingCache:]"
+ "-[PLStorageCache addToBGSQLStagingCache:]_block_invoke_2"
+ "-[PLSubmissionConfig shouldStartTrialsTaskingToday]"
+ "3PPAuthFailCount"
+ "3PPDPDelay"
+ "3PPDPFailCount"
+ "<%@: chunk %lu, %.0f-%.0f (%.0fs)>"
+ "<PLStateInterval: bundleID=%@, domain=%@, label=%@, duration=%.1fms, start=%@, end=%@>"
+ "AccSOC"
+ "Activating staged trial for namespace: %@"
+ "ActiveProcesses"
+ "AdapterLimited"
+ "Adding %lu chunk intervals to XPC payload"
+ "Adding MetricKit client domain allowlist with %lu bundleIDs to XPC payload"
+ "Applied table group '%@' with %lu subsystems"
+ "AppliedPercentage"
+ "Applying trials tasking table whitelist filter"
+ "AverageMemory"
+ "AverageMemoryCount"
+ "AverageMemoryVariance"
+ "AveragePictureLevel"
+ "BGSQL"
+ "BGSQL cache limit reached (%lu), flushing before add"
+ "BGSQL high flush rate detected: %lu flushes in last %.0f seconds (threshold: %lu)"
+ "BGSQL writeToDB=NO entry=%@"
+ "BGSQL: daemon_flush_end totalEntries=%lu inserts=%lu updates=%lu"
+ "BGSQL: daemon_flush_start totalEntries=%lu entryKeys=%lu"
+ "BGSQL: flush had %lu failed writes out of %lu attempted"
+ "BGSQLCacheLimit"
+ "BGSQL_DedicatedCache"
+ "BatteryIndex"
+ "Bds0"
+ "BestAccuracy"
+ "BestAccuracyForNavigation"
+ "Bfo0"
+ "Bfo1"
+ "BundleIDStringID"
+ "CPMSPowerBudget"
+ "CPUInstructions"
+ "ChargeFrequency"
+ "ChargeModeConfigured"
+ "Checking device enrollment for trials: %@"
+ "ClientNameStringID"
+ "CoexAggressorMask"
+ "CoexPowerBudget"
+ "ConfigUUID"
+ "ConfiguredPowerBudget"
+ "Constructed PLTaskingTables entry: %@"
+ "Constructed trials tasking table whitelist in PerfPowerServicesExtended: %@"
+ "CoreMotionActivityState"
+ "Creating index on index key column: %@ for table: %@"
+ "DPPowerSetting"
+ "DependencyIdentifiersStringID"
+ "Device is enrolled in trial: %@ deploymentId: %@ (%@), namespaces: %@"
+ "DeviceSupportsAlwaysListening"
+ "DeviceSupportsAlwaysOnTime"
+ "DeviceSupportsApplePencil"
+ "DeviceSupportsDCP"
+ "DeviceSupportsLowPowerWake"
+ "Dice roll failed: %f >= %d"
+ "DiceRoll"
+ "DiskVolumeStringID"
+ "Dropping table: %@"
+ "DutyCycleChargingEnabled"
+ "EfficiencyPercent"
+ "Emitting CoreAnalytics event %@ for enrolled trials: %@"
+ "Error enumerating trials: %@"
+ "ErrorFlags"
+ "ErrorReason"
+ "Evaluations"
+ "FG"
+ "FODetected"
+ "Failed to activate namespace %@: %@"
+ "Failed to get TRIAllocationStatus provider"
+ "Failed to load PLTaskingTableGroups.plist"
+ "Failed to query table list for trials tasking filtering"
+ "Fault"
+ "FileProtectionStringID"
+ "FreeAirMag"
+ "FreeAirSTDDev"
+ "FreezerLifecycle"
+ "GLPEmbedding"
+ "GLPIndexing"
+ "GLPMailAttachments"
+ "GPUTime"
+ "GroupNameStringID"
+ "HapticAudioRunningCount"
+ "HapticForceStop"
+ "HasAppleNeuralEngine"
+ "HasBattery"
+ "HasMesa"
+ "HostRequestedCloak"
+ "HundredMetersAccuracy"
+ "INSERT INTO %@ (timestamp, TaskEndTime, Reason) VALUES ('%@', '%@', '%@')"
+ "IdentifierStringID"
+ "IndexKey column '%@' not found in metrics for table %@"
+ "IntelligentConnectivity"
+ "Invalid PLTaskingTrials: max 2 trials, received %lu"
+ "Invalid percentage: %d"
+ "InvolvedProcessesStringID"
+ "IsEnrolled"
+ "KilometerAccuracy"
+ "LSSR5CarKeyData"
+ "LSSR5SmartReplies"
+ "LaunchReasonStringID"
+ "LimitID"
+ "LowPowerWalletMode"
+ "MemoryFootprint"
+ "Migration"
+ "MultiFreqMag1"
+ "MultiFreqMag2"
+ "MultiFreqMag3"
+ "MultiFreqMag4"
+ "MultiFreqMag5"
+ "MultiFreqMag6"
+ "NANDown"
+ "NANState"
+ "NandBudgetLeft"
+ "NearestTenMetersAccuracy"
+ "No BGSQL connection for flush, dropping %lu entries across %lu keys"
+ "Not a trials blob - missing trials configuration"
+ "ObjectType"
+ "PArc"
+ "PLAudioAgent_EventForward_HapticAudioRunningCount"
+ "PLAudioAgent_EventForward_HapticForceStop"
+ "PLAudioAgent_EventPoint_HapticForceStop"
+ "PLBatteryAgent_EventPoint_InductiveEspContinuousInfo"
+ "PLBatteryAgent_EventPoint_InductiveEspPowerPolicyInfo"
+ "PLBatteryAgent_EventPoint_InductiveEspSignpostInfo"
+ "PLDisplayAgent_EventBackward_APLStatsX"
+ "PLDisplayAgent_EventBackward_DCPAODstatsX"
+ "PLDisplayAgent_EventForward_DisplayX"
+ "PLDisplayAgent_EventPoint_DisplayX"
+ "PLIOReportAgent_EventBackward_DCPSECscanout"
+ "PLIOReportAgent_EventBackward_DCPSECscanoutstats"
+ "PLIOReportAgent_EventBackward_DCPSECswap"
+ "PLIOReportAgent_EventBackward_MesaMesaPowerState"
+ "PLIOReportAgent_EventBackward_Multitouch2Multitouchhighlevelstats"
+ "PLIOReportAgent_EventBackward_PPMStatsSystemStressSignal"
+ "PLTaskingBaselinePercentage"
+ "PLTaskingOnDemandTrials"
+ "PLTaskingPerModelTrialsPercentages"
+ "PLTaskingTableGroups"
+ "PLTaskingTrials"
+ "PLTaskingTrialsPercentage"
+ "PRxPowerReceived"
+ "PTxPower"
+ "Peak1Freq"
+ "Peak1Mag"
+ "Peak2Freq"
+ "Peak2Mag"
+ "Penalty"
+ "PlatinumCapability"
+ "PolicyStringID"
+ "PoutNotAllowedReason"
+ "Power State_FING-DET"
+ "Power State_FING-DET_Transitions"
+ "Power State_IDLE"
+ "Power State_IDLE_Transitions"
+ "Power State_IMAGING"
+ "Power State_IMAGING_Transitions"
+ "Power State_OFF"
+ "Power State_OFF_Transitions"
+ "PrimaryDomain"
+ "ProcessNameStringID"
+ "ProcessNames"
+ "ProducedResultIdentifiersStringID"
+ "Purpose"
+ "PushTopicLimit"
+ "QiPacketResult"
+ "QuickSwitch"
+ "Recreating index on index key column: %@ for table: %@"
+ "RelatedApplicationsStringID"
+ "Resolved PPSTaskingTables for subsystem '%@': %@"
+ "Resolved trials tasking tables: %@"
+ "RetryCount"
+ "RuntimeWarningMetrics"
+ "RuntimeWarningModelTypeID"
+ "RuntimeWarningPrediction"
+ "RuntimeWarningTriggered"
+ "RxID"
+ "SDTc"
+ "SELECT name FROM sqlite_master WHERE type='index' AND name='%@'"
+ "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite%' AND name NOT LIKE 'PLCoreStorage%'"
+ "SHAD"
+ "SecondaryDomains"
+ "ServiceNameStringID"
+ "SignalBar0"
+ "SignalBar1"
+ "SignalBar2"
+ "SignalBar3"
+ "SignalBar4"
+ "SkinTemperature"
+ "StringID"
+ "StringInterning"
+ "StringValue"
+ "SubCategoryStringID"
+ "Successfully requested activation for namespace: %@"
+ "SupportsLowPowerMode"
+ "SyStress_0"
+ "SyStress_0_Transitions"
+ "SyStress_1"
+ "SyStress_1_Transitions"
+ "SystemPowerBudget"
+ "TA2B"
+ "TA2I"
+ "TArc"
+ "TDBP"
+ "TSSP"
+ "TTBP"
+ "TVDL"
+ "TVDQ"
+ "TVFQ"
+ "TVXL"
+ "TVXM"
+ "TVXQ"
+ "Table group '%@' not found in predefined groups, options are: %@"
+ "Table row missing name field"
+ "TargetPowerBudget"
+ "TaskNameStringID"
+ "TaskingTrialsFromBlob"
+ "ThermalPowerBudget"
+ "ThreeKilometersAccuracy"
+ "TotalFrameCount"
+ "Trial enrollment check result: ENROLLED in trials: %@"
+ "Trial enrollment check result: NOT ENROLLED in any trials"
+ "TrialExperimentIDStringID"
+ "TrialIDs"
+ "TrialTreatmentIDStringID"
+ "Trials blob requires PLTaskingOnDemand='%@', got '%@'"
+ "Trials tasking approved: model=%@, enrolled=%@, percentage=%d, dice=%f"
+ "Trials tasking whitelist filter applied, %lu tables allowed"
+ "Trials tasking: model '%@' not in per-model rates, not tasking"
+ "Trials tasking: model=%@, enrolled=%@, enrolledTrials=%@, percentage=%d, dice=%f"
+ "Trials-based tasking configured"
+ "Unknown table group: %@"
+ "UptimeDuration"
+ "UseCaseList"
+ "ValleyFreq"
+ "ValleyMag"
+ "WakesCaused"
+ "WallClockDuration"
+ "WidgetBudgetIDStringID"
+ "WirelessChargingCapability"
+ "[Log] %@ value is %.0fs in the future for subsystem/category: %@/%@; ignoring override"
+ "[Log] %@ value is %.1f days old (max %.0f) for subsystem/category: %@/%@; ignoring override"
+ "[Log] %@ value must be NSDate, got %@ for subsystem/category: %@/%@"
+ "[TrialsDebug] prepareDatabaseAtPath: ondemand=%@, ppsTaskingTables=%@"
+ "__pps_timeSensitiveEntryDate"
+ "activations"
+ "activeDrawingDurationSeconds"
+ "activeSeconds"
+ "addToBGSQLStagingCache: entryKey=%@, entryID=%llu already exists in cache"
+ "advertisingServices"
+ "aggregationKey"
+ "animationDurationMs"
+ "assetloadedfromCacheKB"
+ "averageAPL"
+ "averageAPLDimming"
+ "averageFramePerSecond"
+ "averageMemoryKB"
+ "awdlDisabled"
+ "awdlInactivityEvent"
+ "bdq0"
+ "bdq1"
+ "bds1"
+ "begin trials-based tasking setup check"
+ "bet0"
+ "bet1"
+ "bgLocationAudioTime"
+ "bgTime_Audio"
+ "bgTime_Location"
+ "bgTime_Total"
+ "bgsql_dedicated_cache"
+ "browsingServices"
+ "bundleIDResolved"
+ "bytesCellularIn"
+ "bytesCellularOut"
+ "bytesWifiIn"
+ "bytesWifiOut"
+ "cellularMetrics"
+ "chunkIndex"
+ "chunkIntervals"
+ "chunkKey"
+ "chunkMetrics"
+ "chunk__%lu"
+ "collect_state_intervals"
+ "com.apple.perfpowerservices.tasking.trials"
+ "com.apple.powerlog.appDeletion"
+ "compactor_major_compactions_bailed"
+ "compactor_major_compactions_bytes_freed"
+ "compactor_major_compactions_bytes_moved"
+ "compactor_major_compactions_completed"
+ "compactor_major_compactions_considered"
+ "compactor_major_compactions_segments_freed"
+ "compactor_major_compactions_slots_moved"
+ "countInstances"
+ "cpuInstructionsKI"
+ "cpuMetrics"
+ "cpuTimeSec"
+ "deploymentId"
+ "dictionaryRepresentation"
+ "diskIOMetrics"
+ "diskLogicalWritesKB"
+ "displayMetrics"
+ "displayON"
+ "durationMs"
+ "durationSeconds"
+ "durations"
+ "endContinuousSeconds"
+ "endMachTime"
+ "endTimestamp"
+ "exits"
+ "experimentId"
+ "extendedLaunches"
+ "featureEnabled"
+ "fgTime_Total"
+ "flipbookLayoutProfile"
+ "flipbookRenderProfile"
+ "frameCount"
+ "front-depth-camera"
+ "glitchDurationMs"
+ "gpuMetrics"
+ "hangs"
+ "hasActivations"
+ "hasExits"
+ "hasExtendedLaunches"
+ "hasGlitches"
+ "hasHangs"
+ "hasLaunches"
+ "hasMetalFrameRates"
+ "hasResumes"
+ "hasSignpostIntervals"
+ "hitchDurationMs"
+ "idx_%@_%@"
+ "label"
+ "launches"
+ "layerName"
+ "locationMetrics"
+ "maxEMATau0"
+ "maxEMATau1"
+ "maxEMATau2"
+ "maxEMATau3"
+ "maximumAPL"
+ "maximumAPLDimming"
+ "memoryMetrics"
+ "metalFrameRates"
+ "metrickit_client_domain_allowlist"
+ "minimumAPL"
+ "minimumAPLDimming"
+ "networkMetrics"
+ "pageins"
+ "pages_grabbed"
+ "pages_grabbed_iopl"
+ "pages_grabbed_kern"
+ "pages_grabbed_upl"
+ "peakMemoryKB"
+ "peakPowerEnvelope"
+ "perceivedHitchDuration"
+ "plist"
+ "powerMetrics"
+ "processImagePath"
+ "processImageUUID"
+ "pwrMax"
+ "pwrMean"
+ "pwrVar"
+ "registeredClients"
+ "resumes"
+ "rxIdleSeconds"
+ "scrollDurationMs"
+ "serviceCount"
+ "settingsAndState"
+ "signpostIntervals"
+ "stableState"
+ "staged"
+ "startContinuousSeconds"
+ "startMachTime"
+ "startTimestamp"
+ "stateIntervals"
+ "stateMetrics"
+ "swapouts_under_300s"
+ "swapouts_under_30s"
+ "swapouts_under_60s"
+ "timestampMS"
+ "totalAnimationDuration"
+ "totalAnimationDurationMs"
+ "totalCPUInstructionsKI"
+ "totalCPUTimeSec"
+ "totalDiskWritesKB"
+ "totalExpertSwappedCount"
+ "totalExpertsLoadedFromCacheCount"
+ "totalHitchDurationMs"
+ "trial_tasking"
+ "txIdleSeconds"
+ "unattributed"
+ "userEnabled"
+ "v20@?0B8@\"NSError\"12"
+ "v24@?0@\"TRIAllocationStatus\"8^B16"
+ "wakeups_external_q_throttled"
+ "wakeups_fragmentation_detected"
+ "wakeups_free_below_reserved"
+ "wakeups_minor_compactions"
+ "wakeups_scavenger"
+ "wakeups_swap_threshold_exceeded"
+ "wakeups_target_age"
+ "wakeups_thrashing_detected"
+ "wakeups_total"
+ "weightedGlitchRatioSum"
+ "\xf0\xf05c"
- "#"
- "#16@0:8"
- "#24@0:8@16"
- "+N9mZUAHooNvMiQnjeTJ8g"
- ".cxx_construct"
- ".cxx_destruct"
- "1oMPwMsqxTa9BJxUs8v06w"
- "8S7ydMJ4DlCUF38/hI/fJA"
- ":24@0:8q16"
- "@"
- "@\"<PLABMClientMessageDelegate>\""
- "@\"<PLActivityCriterionDelegate>\""
- "@\"<PLArchiveJobManager>\""
- "@\"<PLTimeReferenceManager>\""
- "@\"<PPSSignpostServiceDelegate>\""
- "@\"DRConfigMonitor\""
- "@\"NSArray\""
- "@\"NSCondition\""
- "@\"NSDate\""
- "@\"NSDate\"16@0:8"
- "@\"NSDate\"32@0:8q16q24"
- "@\"NSDictionary\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSObject<OS_os_transaction>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@\"PLAccountingOperator\""
- "@\"PLActivityCriterion\""
- "@\"PLArchiveEntry\""
- "@\"PLCFNotificationOperatorComposition\""
- "@\"PLCoreAgent\""
- "@\"PLCoreService\""
- "@\"PLCoreStorage\""
- "@\"PLEntry\""
- "@\"PLEntryKey\""
- "@\"PLEntryNotificationOperatorComposition\""
- "@\"PLKQueue\""
- "@\"PLMonotonicTimer\""
- "@\"PLNSNotificationOperatorComposition\""
- "@\"PLOperator\""
- "@\"PLSQLStatement\""
- "@\"PLSQLiteConnection\""
- "@\"PLStorageOperator\""
- "@\"PLSubmissionConfig\""
- "@\"PLTimer\""
- "@\"PLXPCListenerOperatorComposition\""
- "@\"PLXPCResponderOperatorComposition\""
- "@\"PPSCollectionOperator\""
- "@\"PPSCoreStorage\""
- "@\"PPSFlatStorage\""
- "@\"PPSSQLStorage\""
- "@\"PPSSignpostServiceConnection\""
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8C16"
- "@20@0:8I16"
- "@20@0:8S16"
- "@20@0:8i16"
- "@20@0:8s16"
- "@24@0:8#16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8^{__CFString=}16"
- "@24@0:8^{kern_event_msg=IIIIII[1I]}16"
- "@24@0:8d16"
- "@24@0:8r*16"
- "@28@0:8@16B24"
- "@28@0:8@16i24"
- "@28@0:8I16@20"
- "@28@0:8Q16i24"
- "@28@0:8^(in_addr_4_6={in_addr=I}{in6_addr=(?=[16C][8S][4I])})16i24"
- "@28@0:8^{__CFData=}16C24"
- "@28@0:8i16@20"
- "@28@0:8s16@20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16Q24"
- "@32@0:8@16d24"
- "@32@0:8@16q24"
- "@32@0:8Q16@24"
- "@32@0:8d16@24"
- "@32@0:8q16q24"
- "@32@0:8{_PLTimeIntervalRange=dd}16"
- "@32@0:8{timeval=qi}16"
- "@36@0:8@16@24B32"
- "@36@0:8@16@24s32"
- "@36@0:8@16^i24B32"
- "@36@0:8Q16i24^B28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24@?32"
- "@40@0:8@16@24C32I36"
- "@40@0:8@16@24q32"
- "@40@0:8@16d24@?32"
- "@40@0:8@16d24d32"
- "@40@0:8@16q24@32"
- "@40@0:8@16q24q32"
- "@40@0:8@16{_PLTimeIntervalRange=dd}24"
- "@40@0:8Q16@24@32"
- "@44@0:8@16@24@32B40"
- "@44@0:8@16@24@32C40"
- "@44@0:8@16@24B32@?36"
- "@44@0:8@16@24s32@?36"
- "@44@0:8s16@20@28@36"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24@32@?40"
- "@48@0:8@16@24@32C40C44"
- "@48@0:8@16@24[128c]32@?40"
- "@48@0:8@16@24d32^@40"
- "@48@0:8@16Q24Q32@?40"
- "@48@0:8@16^{sqlite3=}24@32^i40"
- "@48@0:8@16d24@32@?40"
- "@48@0:8@16d24{_PLTimeIntervalRange=dd}32"
- "@48@0:8@16q24q32@40"
- "@48@0:8@16{_PLTimeIntervalRange=dd}24@40"
- "@48@0:8d16Q24@32^@40"
- "@52@0:8@16@24@32@40B48"
- "@52@0:8@16@24s32@36@?44"
- "@52@0:8@16B24d28q36@44"
- "@56@0:8@16@24@32C40C44I48C52"
- "@64@0:8@16@24@32@40@48@56"
- "@64@0:8@16@24@32@40@?48@?56"
- "@64@0:8@16{_PLTimeIntervalRange=dd}24q40q48@56"
- "@64@0:8{apfs_label_purgeable_request=QQQQQQ}16"
- "@68@0:8@16d24d32B40@44@52@?60"
- "@80@0:8@16d24d32d40d48d56d64@72"
- "@?"
- "@?16@0:8"
- "APFS"
- "AppDeletionEnabled"
- "B16@0:8"
- "B20@0:8B16"
- "B20@0:8i16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8@?16"
- "B24@0:8Q16"
- "B24@0:8^B16"
- "B24@0:8^{npi_if_info=III}16"
- "B24@0:8d16"
- "B24@0:8q16"
- "B28@0:8@16B24"
- "B28@0:8B16d20"
- "B28@0:8^{__CFData=}16C24"
- "B28@0:8s16@20"
- "B32@0:8#16@24"
- "B32@0:8@16@24"
- "B32@0:8@16^B24"
- "B32@0:8@16q24"
- "B32@0:8i16i20*24"
- "B32@0:8q16@24"
- "B36@0:8@16@24B32"
- "B36@0:8@16@24i32"
- "B40@0:8@16@24@32"
- "B40@0:8@16Q24@32"
- "B40@0:8@16d24d32"
- "B44@0:8@16@24@32B40"
- "B48@0:8@16@24@32@40"
- "B48@0:8@16@24@32^@40"
- "B52@0:8@16@24@32@40B48"
- "B60@0:8@16@24@32@40B48q52"
- "B72@0:8@16{apfs_label_purgeable_request=QQQQQQ}24"
- "BGSQLConnection"
- "BGSQLDBDuration"
- "Birtx7GxrxCCUzsE1JQO8Q"
- "CESQLConnection"
- "CESQLDBDuration"
- "DMACompliant"
- "DMAKeys"
- "DMAKeysForEntryDefinition:"
- "EPSQLConnection"
- "EPSQLDBDuration"
- "EPSQLVacuumInterval"
- "HV7WDiidgMf7lwAu++Lk5w"
- "I16@0:8"
- "INSERT INTO %@ (TaskEndTime, Reason) VALUES ('%@', '%@')"
- "IhNb6V2L1pt+hBlZMsm5FQ"
- "J2"
- "J72A"
- "J81N"
- "J86A"
- "JSONSanitizeDictionary:"
- "K94"
- "MavRevStringQuery"
- "Monotonic"
- "N48"
- "N61A"
- "N61B"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "OperatorTask"
- "OverrideAllowlistEnabled"
- "PLABMClient"
- "PLAccountingOperator"
- "PLActivity"
- "PLActivityCriterion"
- "PLActivityCriterionDelegate"
- "PLActivityCriterionEntry"
- "PLActivityCriterionTime"
- "PLActivityScheduler"
- "PLAgent"
- "PLAggregateEntry"
- "PLAppDeletion"
- "PLArchiveEntry"
- "PLArchiveJob"
- "PLArchiveJobManager"
- "PLArchiveManager"
- "PLCFNotificationOperatorComposition"
- "PLChargingState"
- "PLCopyItemsFromPath:toPath:"
- "PLCoreAgent"
- "PLCoreOperator"
- "PLCoreService"
- "PLDarkWakeState"
- "PLDefaults"
- "PLDisplayState"
- "PLEnhancedTaskingAgent"
- "PLEntry"
- "PLEntryAggregateKeysForOperator:"
- "PLEntryAggregateKeysForOperatorClass:"
- "PLEntryAggregateKeysForOperatorName:"
- "PLEntryDefinition"
- "PLEntryKey"
- "PLEntryKeyForEntryKey:"
- "PLEntryKeyForOperatorName:withType:withName:"
- "PLEntryKeyForOperatorName:withType:withName:withWildCardName:isDynamic:"
- "PLEntryKeyStringsForTasking"
- "PLEntryKeyStringsForTaskingReset"
- "PLEntryKeysForEntryType:"
- "PLEntryNotificationOperatorComposition"
- "PLFileStats"
- "PLGestaltUtilities"
- "PLHIDEventOperatorComposition"
- "PLIOHIDOperatorComposition"
- "PLIOKitOperatorComposition"
- "PLIOReportStats"
- "PLKQueue"
- "PLMetricdLifecycleManager"
- "PLModelingUtilities"
- "PLMonotonicTimer"
- "PLMultiKeyEntry"
- "PLNSNotificationOperatorComposition"
- "PLNetworkUtilities"
- "PLOSMetricsUtilities"
- "PLOperator"
- "PLPlatform"
- "PLPluggedState"
- "PLPowerNode"
- "PLProcessInfo"
- "PLQLDuetInMemoryCache"
- "PLRapidController"
- "PLSQLConnection"
- "PLSQLDBDuration"
- "PLSQLStatement"
- "PLSemaphore"
- "PLService"
- "PLSleepState"
- "PLState"
- "PLStateTrackingComposition"
- "PLStorageCache"
- "PLStorageOperator"
- "PLSubmissionFile"
- "PLSubmissionFileBDC"
- "PLSubmissionFileBG"
- "PLSubmissionFileCE"
- "PLSubmissionFileMSS"
- "PLSubmissionFilePLL"
- "PLSubmissionFileSP"
- "PLSubmissionFileXC"
- "PLSubmissionRecord"
- "PLSubmissions"
- "PLThreadInfo"
- "PLThreadStats"
- "PLTimeReference"
- "PLTimeReferenceDynamic"
- "PLTimeReferenceManager"
- "PLTimer"
- "PLUserIdleState"
- "PLUtilities"
- "PLValue"
- "PLValueComparison"
- "PLValueUtilties"
- "PLWakeState"
- "PLXPCListenerOperatorComposition"
- "PLXPCRelay"
- "PLXPCResponderOperatorComposition"
- "PPSCollectionOperator"
- "PPSCoreUtilities"
- "PPSEnabled:"
- "PPSEntryDefinition"
- "PPSEntryKey"
- "PPSFeatureFlagReaderProtocol"
- "PPSFileUtilities"
- "PPSFlatStorage"
- "PPSSafeguardController"
- "PPSSignpostServiceConnection"
- "PPSSignpostServiceDelegate"
- "PPSSignpostServiceRequest"
- "PPSStorage"
- "PPSSubmissionRecord"
- "PPSSubmissionUtilities"
- "PowerlogCore"
- "PowerlogExtensions"
- "PpmzzBVLpZVubmP0tCIymg"
- "PreUnlockEPSQLConnection"
- "PreUnlockTelemetryEnabled"
- "Q16@0:8"
- "Q20@0:8i16"
- "Q24@0:8@16"
- "Q24@0:8Q16"
- "Q24@0:8d16"
- "Q28@0:8@16i24"
- "RbdcConverterHelper"
- "SignpostReaderHelper"
- "SwitchToIncrementalVacuumEnabled"
- "T#,R"
- "T#,R,&,V_operatorClass"
- "T@\"<PLABMClientMessageDelegate>\",&,V_delegate"
- "T@\"<PLActivityCriterionDelegate>\",W,V_delegate"
- "T@\"<PLArchiveJobManager>\",&,V_manager"
- "T@\"<PLTimeReferenceManager>\",&,V_timeManager"
- "T@\"<PPSSignpostServiceDelegate>\",R,V_service"
- "T@\"DRConfigMonitor\",&,V_drConfigMonitor"
- "T@\"DRConfigMonitor\",&,V_taskingMonitor"
- "T@\"NSArray\",&,V_builds"
- "T@\"NSArray\",&,V_criteria"
- "T@\"NSArray\",&,V_otherAggregateKeys"
- "T@\"NSArray\",&,V_removeEntries"
- "T@\"NSArray\",&,V_rootNodeEnergyRows"
- "T@\"NSArray\",&,V_serviceClients"
- "T@\"NSArray\",&,V_taskingFiles"
- "T@\"NSArray\",&,V_trimmingQueries"
- "T@\"NSArray\",R"
- "T@\"NSArray\",R,C,V_notificationNames"
- "T@\"NSCondition\",&,V_pendingObjectsLock"
- "T@\"NSDate\",&"
- "T@\"NSDate\",&,N"
- "T@\"NSDate\",&,N,V_entryDate"
- "T@\"NSDate\",&,N,V_fireDate"
- "T@\"NSDate\",&,N,V_lastCacheFlushDate"
- "T@\"NSDate\",&,N,V_monotonicFireDate"
- "T@\"NSDate\",&,V_configDateApplied"
- "T@\"NSDate\",&,V_configDateReceived"
- "T@\"NSDate\",&,V_endDate"
- "T@\"NSDate\",&,V_lastBatteryTimestampSystem"
- "T@\"NSDate\",&,V_lastCompletedDate"
- "T@\"NSDate\",&,V_lastKernelTimeRecalibrated"
- "T@\"NSDate\",&,V_lastQueryTime"
- "T@\"NSDate\",&,V_lastSleepTime"
- "T@\"NSDate\",&,V_lastSystemTimeRecalibrated"
- "T@\"NSDate\",&,V_logCreationEndDate"
- "T@\"NSDate\",&,V_logCreationResumeDate"
- "T@\"NSDate\",&,V_logCreationStartDate"
- "T@\"NSDate\",&,V_sampleTime"
- "T@\"NSDate\",&,V_sampleTimePrevious"
- "T@\"NSDate\",&,V_startDate"
- "T@\"NSDate\",&,V_stateChangeTime"
- "T@\"NSDate\",&,V_systemStateChangeTime"
- "T@\"NSDate\",&,V_time"
- "T@\"NSDate\",R"
- "T@\"NSDate\",R,N,V_configDateApplied"
- "T@\"NSDate\",R,N,V_configDateReceived"
- "T@\"NSDate\",R,V_launchDate"
- "T@\"NSDictionary\",&,N,V_entryDefinition"
- "T@\"NSDictionary\",&,V_ckTagConfig"
- "T@\"NSDictionary\",&,V_connectionByStorage"
- "T@\"NSDictionary\",&,V_contextDictionary"
- "T@\"NSDictionary\",&,V_currentSnapshot"
- "T@\"NSDictionary\",&,V_defaultTaskingTypeParameters"
- "T@\"NSDictionary\",&,V_filter"
- "T@\"NSDictionary\",&,V_hashEntries"
- "T@\"NSDictionary\",&,V_ioReportSample"
- "T@\"NSDictionary\",&,V_notificationsToTimeReferences"
- "T@\"NSDictionary\",&,V_perModelTaskingTypeParameters"
- "T@\"NSDictionary\",&,V_plTaskingTables"
- "T@\"NSDictionary\",&,V_ppsTaskingTables"
- "T@\"NSDictionary\",&,V_previousIOReportSample"
- "T@\"NSDictionary\",&,V_processThreadMap"
- "T@\"NSDictionary\",&,V_signpostAllowlist"
- "T@\"NSDictionary\",&,V_startArgs"
- "T@\"NSDictionary\",&,V_stopArgs"
- "T@\"NSDictionary\",&,V_storageMap"
- "T@\"NSDictionary\",&,V_subscribedChannels"
- "T@\"NSDictionary\",&,V_tagConfig"
- "T@\"NSDictionary\",&,V_taskingPercentage"
- "T@\"NSDictionary\",&,V_threadNameToInfo"
- "T@\"NSDictionary\",&,V_timeReferences"
- "T@\"NSDictionary\",R,V_registration"
- "T@\"NSMutableArray\",&,V_archiveJobs"
- "T@\"NSMutableArray\",&,V_bufferedEntries"
- "T@\"NSMutableArray\",&,V_notificationBlocks"
- "T@\"NSMutableArray\",&,V_offsetHistory"
- "T@\"NSMutableArray\",&,V_stateChangeNotifications"
- "T@\"NSMutableArray\",&,V_submissionQueue"
- "T@\"NSMutableArray\",R"
- "T@\"NSMutableArray\",R,GallValues"
- "T@\"NSMutableDictionary\",&,N,V_matchingKeyToValue"
- "T@\"NSMutableDictionary\",&,V_activities"
- "T@\"NSMutableDictionary\",&,V_cacheContent"
- "T@\"NSMutableDictionary\",&,V_countSafetyDrop"
- "T@\"NSMutableDictionary\",&,V_countWarnings"
- "T@\"NSMutableDictionary\",&,V_dictionary"
- "T@\"NSMutableDictionary\",&,V_entryKeyToStateMap"
- "T@\"NSMutableDictionary\",&,V_executeBlockCache"
- "T@\"NSMutableDictionary\",&,V_filterDefinitions"
- "T@\"NSMutableDictionary\",&,V_filterDeltaLastEntryIDs"
- "T@\"NSMutableDictionary\",&,V_instancePrefsCache"
- "T@\"NSMutableDictionary\",&,V_lastEntryCache"
- "T@\"NSMutableDictionary\",&,V_lastLogDateForEntryKey"
- "T@\"NSMutableDictionary\",&,V_managedPrefsCache"
- "T@\"NSMutableDictionary\",&,V_multiKeys"
- "T@\"NSMutableDictionary\",&,V_operators"
- "T@\"NSMutableDictionary\",&,V_preparedDynamicStatements"
- "T@\"NSMutableDictionary\",&,V_preparedStatements"
- "T@\"NSMutableDictionary\",&,V_preparedUpdateStatements"
- "T@\"NSMutableDictionary\",&,V_ruleIDToPendingJobs"
- "T@\"NSMutableDictionary\",&,V_services"
- "T@\"NSMutableDictionary\",&,V_stagingAggregateEntryCache"
- "T@\"NSMutableDictionary\",&,V_stagingEntryCache"
- "T@\"NSMutableDictionary\",&,V_stateIDToStateMap"
- "T@\"NSMutableDictionary\",&,V_timeChangeBlocks"
- "T@\"NSMutableDictionary\",&,V_userPrefsCache"
- "T@\"NSMutableSet\",&,V_canceledFireDates"
- "T@\"NSMutableSet\",&,V_entryKeysToSetup"
- "T@\"NSMutableSet\",&,V_interestedObjects"
- "T@\"NSMutableSet\",&,V_pendingDoneObjects"
- "T@\"NSMutableSet\",&,V_safeCopyInProgress"
- "T@\"NSNumber\",&,V_cacheSize"
- "T@\"NSNumber\",&,V_capSize"
- "T@\"NSNumber\",&,V_capValue"
- "T@\"NSNumber\",&,V_mssCycleInterval"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_backgroundQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_crashMoverQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_dispatchQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_operatorQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_queue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_utilityQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_workQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R"
- "T@\"NSObject<OS_dispatch_queue>\",R,W"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_sem"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,V_dbSem"
- "T@\"NSObject<OS_dispatch_source>\",&,V_timer"
- "T@\"NSObject<OS_os_transaction>\",&,V_userRequestTransaction"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_relayConnection"
- "T@\"NSObject<OS_xpc_object>\",&,V_xpcConnection"
- "T@\"NSObject<OS_xpc_object>\",&,V_xpcCrashMoverConn"
- "T@\"NSSet\",&,N,V_rules"
- "T@\"NSString\",&,N,V_entryKey"
- "T@\"NSString\",&,V_aggregateKey"
- "T@\"NSString\",&,V_blobFailureReason"
- "T@\"NSString\",&,V_cachedClassName"
- "T@\"NSString\",&,V_ckFileDirPath"
- "T@\"NSString\",&,V_configUUID"
- "T@\"NSString\",&,V_daFileDirPath"
- "T@\"NSString\",&,V_deviceModel"
- "T@\"NSString\",&,V_directory"
- "T@\"NSString\",&,V_driverName"
- "T@\"NSString\",&,V_entryDefinitionKey"
- "T@\"NSString\",&,V_entryKey"
- "T@\"NSString\",&,V_failureReason"
- "T@\"NSString\",&,V_fileName"
- "T@\"NSString\",&,V_filePath"
- "T@\"NSString\",&,V_fileType"
- "T@\"NSString\",&,V_filterQuery"
- "T@\"NSString\",&,V_issueCategory"
- "T@\"NSString\",&,V_issueDescription"
- "T@\"NSString\",&,V_key"
- "T@\"NSString\",&,V_mdLogCompressedFilePath"
- "T@\"NSString\",&,V_mdLogFilePath"
- "T@\"NSString\",&,V_monitoredCategory"
- "T@\"NSString\",&,V_monitoredSubsystem"
- "T@\"NSString\",&,V_mssCompressedFilePath"
- "T@\"NSString\",&,V_mssFilePath"
- "T@\"NSString\",&,V_name"
- "T@\"NSString\",&,V_notificationName"
- "T@\"NSString\",&,V_onDemandTasking"
- "T@\"NSString\",&,V_ondemand"
- "T@\"NSString\",&,V_processName"
- "T@\"NSString\",&,V_recordType"
- "T@\"NSString\",&,V_request"
- "T@\"NSString\",&,V_serviceClassName"
- "T@\"NSString\",&,V_serviceName"
- "T@\"NSString\",&,V_tagUUID"
- "T@\"NSString\",&,V_targetContainer"
- "T@\"NSString\",&,V_taskingBuild"
- "T@\"NSString\",&,V_taskingDeviceModels"
- "T@\"NSString\",&,V_taskingPopulation"
- "T@\"NSString\",&,V_taskingRequestReason"
- "T@\"NSString\",&,V_taskingType"
- "T@\"NSString\",&,V_threadName"
- "T@\"NSString\",&,V_transactionLock"
- "T@\"NSString\",&,V_uuid"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_filePath"
- "T@\"NSString\",C,N,V_wildCardName"
- "T@\"NSString\",C,V_path"
- "T@\"NSString\",R"
- "T@\"NSString\",R,&,V_entryKey"
- "T@\"NSString\",R,&,V_entryName"
- "T@\"NSString\",R,&,V_entryType"
- "T@\"NSString\",R,&,V_operatorName"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_crPath"
- "T@\"NSString\",R,V_entryKey"
- "T@\"NSString\",R,V_identifier"
- "T@\"NSString\",R,V_key"
- "T@\"NSString\",R,W"
- "T@\"NSURL\",&,V_filePath"
- "T@\"NSURL\",&,V_sourceURL"
- "T@\"NSUUID\",&,V_configUUID"
- "T@\"NSUUID\",R,N,V_configUUID"
- "T@\"NSUUID\",R,V_uuid"
- "T@\"NSXPCConnection\",&,N,V_connectionToServer"
- "T@\"PLAccountingOperator\",R,V_accounting"
- "T@\"PLActivityCriterion\",&,V_mustRunCriterion"
- "T@\"PLArchiveEntry\",&,V_archiveEntry"
- "T@\"PLCFNotificationOperatorComposition\",&,V_blockingFlushCachesCFNotification"
- "T@\"PLCFNotificationOperatorComposition\",&,V_flushCachesCFNotification"
- "T@\"PLCFNotificationOperatorComposition\",&,V_keybagFirstUnlockNotification"
- "T@\"PLCFNotificationOperatorComposition\",&,V_keybagLockStatusNotification"
- "T@\"PLCFNotificationOperatorComposition\",&,V_startMonitor"
- "T@\"PLCFNotificationOperatorComposition\",&,V_stopMonitor"
- "T@\"PLCoreAgent\",R,V_agents"
- "T@\"PLCoreService\",R,V_services"
- "T@\"PLCoreStorage\",R,V_storage"
- "T@\"PLCoreStorage\",R,W"
- "T@\"PLEntry\",&,V_activityEntry"
- "T@\"PLEntryKey\",W,V_baseEntryKey"
- "T@\"PLEntryNotificationOperatorComposition\",&,V_entryListener"
- "T@\"PLEntryNotificationOperatorComposition\",&,V_sleepEntryNotification"
- "T@\"PLEntryNotificationOperatorComposition\",&,V_wakeEntryNotification"
- "T@\"PLKQueue\",&,V_profileDefaultsKQueue"
- "T@\"PLMonotonicTimer\",&,V_timer"
- "T@\"PLNSNotificationOperatorComposition\",&,V_basebandTimeNotification"
- "T@\"PLNSNotificationOperatorComposition\",&,V_dailyTaskNotification"
- "T@\"PLNSNotificationOperatorComposition\",&,V_dayChangedNotification"
- "T@\"PLOperator\",&,V_operator"
- "T@\"PLOperator\",W,V_operator"
- "T@\"PLSQLStatement\",&,V_metadataStmt"
- "T@\"PLSQLiteConnection\",&,V_connection"
- "T@\"PLSQLiteConnection\",W,V_connection"
- "T@\"PLStorageOperator\",&,V_storageOperator"
- "T@\"PLStorageOperator\",W,V_storageOperator"
- "T@\"PLSubmissionConfig\",&,V_taskingConfig"
- "T@\"PLTimer\",&,V_dailyTaskTimer"
- "T@\"PLTimer\",&,V_flushCachesTimer"
- "T@\"PLTimer\",&,V_periodicCurrentTime"
- "T@\"PLTimer\",&,V_triggerBufferFlush"
- "T@\"PLTimer\",&,V_watchdog"
- "T@\"PLXPCListenerOperatorComposition\",&,V_metricListener"
- "T@\"PLXPCResponderOperatorComposition\",&,V_XPCFlushCacheResponder"
- "T@\"PLXPCResponderOperatorComposition\",&,V_allowlistResponder"
- "T@\"PLXPCResponderOperatorComposition\",&,V_archivesResponder"
- "T@\"PLXPCResponderOperatorComposition\",&,V_batteryUIPlistsResponder"
- "T@\"PLXPCResponderOperatorComposition\",&,V_blPathResponder"
- "T@\"PLXPCResponderOperatorComposition\",&,V_quarantineCopyResponder"
- "T@\"PLXPCResponderOperatorComposition\",&,V_quarantineResponder"
- "T@\"PLXPCResponderOperatorComposition\",&,V_safeFileResponder"
- "T@\"PLXPCResponderOperatorComposition\",&,V_upgradeLogsResponder"
- "T@\"PPSCollectionOperator\",R,V_collection"
- "T@\"PPSCoreStorage\",R,V_coreStorage"
- "T@\"PPSFlatStorage\",&,V_flatStorage"
- "T@\"PPSSQLStorage\",&,V_sqlStorage"
- "T@\"PPSSignpostServiceConnection\",&,V_connection"
- "T@,&,V_currValue"
- "T@,&,V_lastValue"
- "T@,&,V_userInfo"
- "T@,R"
- "T@,R,V_value"
- "T@?,C,N,V_kQueueBlock"
- "T@?,C,N,V_matchBlock"
- "T@?,C,N,V_operatorBlock"
- "T@?,C,V_activityBlock"
- "T@?,C,V_block"
- "T@?,C,V_criterionBlock"
- "T@?,C,V_interruptBlock"
- "T@?,C,V_operatorBlock"
- "TB,N"
- "TB,N,V_enabled"
- "TB,N,V_interrupted"
- "TB,N,V_isDynamic"
- "TB,N,V_satisfied"
- "TB,N,V_storageLocked"
- "TB,R"
- "TB,R,N"
- "TB,R,V_isDelete"
- "TB,R,V_isInsert"
- "TB,R,V_systemTimeOffsetModified"
- "TB,R,V_taskingStarted"
- "TB,V_debugEnabled"
- "TB,V_enableDPUpload"
- "TB,V_enableRestartAtEPL"
- "TB,V_eplEnabled"
- "TB,V_existsInDB"
- "TB,V_followupCurrentTimeRunning"
- "TB,V_iCloudUploadEnabled"
- "TB,V_inSubmission"
- "TB,V_internal"
- "TB,V_isActive"
- "TB,V_isDRTasking"
- "TB,V_isEnergyTasking"
- "TB,V_isErrorEntry"
- "TB,V_isExpedited"
- "TB,V_isNamed"
- "TB,V_isStateRequired"
- "TB,V_listeningForNotifications"
- "TB,V_metadataStmtCreated"
- "TB,V_monitor"
- "TB,V_monotonicResetOccurred"
- "TB,V_rebootOccurred"
- "TB,V_relayActive"
- "TB,V_repeats"
- "TB,V_seed"
- "TB,V_signpostDisable"
- "TB,V_storageReady"
- "TB,V_storageStarted"
- "TB,V_writeToDB"
- "TB,V_xpcActivityStarted"
- "TI,V_conn"
- "TI,V_iterator"
- "TI,V_notificationRef"
- "TI,V_service"
- "TQ,N"
- "TQ,R"
- "TQ,R,V_stateId"
- "TQ,V_percentTimeFilter"
- "TQ,V_stateChangeMask"
- "TQ,V_threadID"
- "T^{IONotificationPort=},V_ioNotifyPort"
- "T^{__CFFileDescriptor=},V_kqueueDescriptorRef"
- "T^{__CFRunLoopSource=},V_kqueueDescriptorSource"
- "T^{__IOHIDEventSystemClient=},V_eventSystemClient"
- "T^{__IOReportSubscriptionCF=},V_subscription"
- "T^{sqlite3=},V_dbConnection"
- "T^{sqlite3_stmt=},V_statement"
- "Td,N"
- "Td,N,V_hourBucketOffset"
- "Td,N,V_offset"
- "Td,N,V_rescheduleDelay"
- "Td,V_BGSQLDBDuration"
- "Td,V_CESQLDBDuration"
- "Td,V_EPSQLDBDuration"
- "Td,V_EPSQLVacuumInterval"
- "Td,V_PLSQLDBDuration"
- "Td,V_XCSQLDBDuration"
- "Td,V_absoluteTimeFilter"
- "Td,V_aggregateValue"
- "Td,V_archiveRetention"
- "Td,V_bgAudioTime"
- "Td,V_bgEnergy"
- "Td,V_bgLocationTime"
- "Td,V_bgTime"
- "Td,V_cellIn"
- "Td,V_cellOut"
- "Td,V_dice"
- "Td,V_fgEnergy"
- "Td,V_fgTime"
- "Td,V_interval"
- "Td,V_lastXPCActivityTimestamp"
- "Td,V_latency"
- "Td,V_mustRunInterval"
- "Td,V_samplingPercentage"
- "Td,V_startTime"
- "Td,V_stopTime"
- "Td,V_systemTime"
- "Td,V_timeout"
- "Td,V_tolerance"
- "Td,V_tooFarInFutureDistance"
- "Td,V_tooFarInPastDistance"
- "Td,V_totalSystemTime"
- "Td,V_totalUserTime"
- "Td,V_userTime"
- "Td,V_wifiIn"
- "Td,V_wifiOut"
- "Td,V_xpcActivityDelay"
- "Ti,V_entryCacheStorageSize"
- "Ti,V_fileDescriptor"
- "Ti,V_kQueue"
- "Ti,V_offsetHistoryHead"
- "Ti,V_pid"
- "Ti,V_refCount"
- "Ti,V_stateToken"
- "Ti,V_transactionInProgress"
- "Ti,V_type"
- "TimeAndLatencyAbm"
- "Tq,N"
- "Tq,N,V_entryID"
- "Tq,N,V_state"
- "Tq,V_cacheSize"
- "Tq,V_lastEntryCacheSize"
- "Tq,V_stage"
- "Tq,V_stagingEntryCacheSize"
- "Tq,V_timeReferenceType"
- "Ts,R,V_comparisonOperation"
- "Ts,V_aggregateFunction"
- "Ts,V_submitReasonType"
- "T{_PLTimeIntervalRange=dd},N,V_timeIntervalRange"
- "U+73bmG4kBGj6kpreQXUTQ"
- "UMUserSwitchStakeholder"
- "URLByAppendingPathComponent:"
- "URLWithString:"
- "UTF8String"
- "UUIDString"
- "Vv16@0:8"
- "XCSQLConnection"
- "XCSQLDBDuration"
- "XPCScheduling"
- "XPCSignpostReaderProtocol"
- "^{IONotificationPort=}"
- "^{IONotificationPort=}16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__CFFileDescriptor=}"
- "^{__CFFileDescriptor=}16@0:8"
- "^{__CFRunLoopSource=}"
- "^{__CFRunLoopSource=}16@0:8"
- "^{__IOHIDEventSystemClient=}"
- "^{__IOHIDEventSystemClient=}16@0:8"
- "^{__IOReportSubscriptionCF=}"
- "^{__IOReportSubscriptionCF=}16@0:8"
- "^{dispatch_queue_s=}"
- "^{mach_timebase_info=II}16@0:8"
- "^{sqlite3=}"
- "^{sqlite3=}16@0:8"
- "^{sqlite3_stmt=}"
- "^{sqlite3_stmt=}16@0:8"
- "_BGSQLDBDuration"
- "_CESQLDBDuration"
- "_EPSQLDBDuration"
- "_EPSQLVacuumInterval"
- "_PLSQLDBDuration"
- "_XCSQLDBDuration"
- "_XPCFlushCacheResponder"
- "_absoluteTimeFilter"
- "_accounting"
- "_activities"
- "_activityBlock"
- "_activityEntry"
- "_addObserver:selector:name:object:options:"
- "_agents"
- "_aggregateFunction"
- "_aggregateKey"
- "_aggregateValue"
- "_allowlistResponder"
- "_archiveEntry"
- "_archiveJobs"
- "_archiveRetention"
- "_archivesResponder"
- "_backgroundQueue"
- "_baseEntryKey"
- "_basebandTimeNotification"
- "_batteryUIPlistsResponder"
- "_bgAudioTime"
- "_bgEnergy"
- "_bgLocationTime"
- "_bgTime"
- "_blPathResponder"
- "_blobFailureReason"
- "_block"
- "_blockingFlushCachesCFNotification"
- "_bufferedEntries"
- "_builds"
- "_cacheContent"
- "_cacheSize"
- "_cachedClassName"
- "_calculateDeltaFromPreviousStats:toCurrentStats:"
- "_cancel"
- "_canceledFireDates"
- "_capSize"
- "_capValue"
- "_cellIn"
- "_cellOut"
- "_ckFileDirPath"
- "_ckTagConfig"
- "_clearState"
- "_collection"
- "_comparisonOperation"
- "_configDateApplied"
- "_configDateReceived"
- "_configUUID"
- "_conn"
- "_connection"
- "_connectionByStorage"
- "_connectionToServer"
- "_contextDictionary"
- "_convertValue:toUnityScaleFromUnit:"
- "_coreStorage"
- "_countSafetyDrop"
- "_countWarnings"
- "_crPath"
- "_crashMoverQueue"
- "_criteria"
- "_criterionBlock"
- "_currValue"
- "_currentSnapshot"
- "_daFileDirPath"
- "_dailyTaskNotification"
- "_dailyTaskTimer"
- "_dayChangedNotification"
- "_dbConnection"
- "_dbSem"
- "_debugEnabled"
- "_debugStringForPurgeableLabel:"
- "_defaultTaskingTypeParameters"
- "_delegate"
- "_deviceModel"
- "_dice"
- "_dictionary"
- "_directory"
- "_dispatchQueue"
- "_drConfigMonitor"
- "_driverName"
- "_enableDPUpload"
- "_enableRestartAtEPL"
- "_enabled"
- "_endDate"
- "_entryCacheStorageSize"
- "_entryDate"
- "_entryDefinition"
- "_entryDefinitionKey"
- "_entryID"
- "_entryKey"
- "_entryKeyToStateMap"
- "_entryKeysToSetup"
- "_entryListener"
- "_entryName"
- "_entryType"
- "_eplEnabled"
- "_eventSystemClient"
- "_executeBlockCache"
- "_existsInDB"
- "_fVMPressureSource"
- "_failureReason"
- "_fgEnergy"
- "_fgTime"
- "_fileDescriptor"
- "_fileName"
- "_filePath"
- "_fileType"
- "_filter"
- "_filterDefinitions"
- "_filterDeltaLastEntryIDs"
- "_filterQuery"
- "_fireDate"
- "_flatStorage"
- "_flushCachesCFNotification"
- "_flushCachesTimer"
- "_followupCurrentTimeRunning"
- "_handleTask:"
- "_hashEntries"
- "_hourBucketOffset"
- "_iCloudUploadEnabled"
- "_identifier"
- "_inSubmission"
- "_init"
- "_instancePrefsCache"
- "_interestedObjects"
- "_internal"
- "_interruptBlock"
- "_interrupted"
- "_interval"
- "_ioNotifyPort"
- "_ioReportSample"
- "_isActive"
- "_isDRTasking"
- "_isDelete"
- "_isDynamic"
- "_isEnergyTasking"
- "_isErrorEntry"
- "_isExpedited"
- "_isInsert"
- "_isNamed"
- "_isStateRequired"
- "_issueCategory"
- "_issueDescription"
- "_iterator"
- "_kQueue"
- "_kQueueBlock"
- "_key"
- "_keybagFirstUnlockNotification"
- "_keybagLockStatusNotification"
- "_kqueueDescriptorRef"
- "_kqueueDescriptorSource"
- "_lastBatteryTimestampSystem"
- "_lastCacheFlushDate"
- "_lastCollectionDate"
- "_lastCompletedDate"
- "_lastEntryCache"
- "_lastEntryCacheSize"
- "_lastKernelTimeRecalibrated"
- "_lastLogDateForEntryKey"
- "_lastQueryTime"
- "_lastSleepTime"
- "_lastSystemTimeRecalibrated"
- "_lastValue"
- "_lastXPCActivityTimestamp"
- "_latency"
- "_launchDate"
- "_listeningForNotifications"
- "_lock"
- "_logCreationEndDate"
- "_logCreationResumeDate"
- "_logCreationStartDate"
- "_managedPrefsCache"
- "_manager"
- "_matchBlock"
- "_matchingKeyToValue"
- "_mdLogCompressedFilePath"
- "_mdLogFilePath"
- "_metadataStmt"
- "_metadataStmtCreated"
- "_metricListener"
- "_monitor"
- "_monitoredCategory"
- "_monitoredSubsystem"
- "_monotonicFireDate"
- "_monotonicResetOccurred"
- "_mssCompressedFilePath"
- "_mssCycleInterval"
- "_mssFilePath"
- "_multiKeys"
- "_mustRunCriterion"
- "_mustRunInterval"
- "_name"
- "_notificationBlocks"
- "_notificationName"
- "_notificationNames"
- "_notificationObservers"
- "_notificationRef"
- "_notificationsToTimeReferences"
- "_offset"
- "_offsetHistory"
- "_offsetHistoryHead"
- "_onDemandTasking"
- "_ondemand"
- "_operator"
- "_operatorBlock"
- "_operatorClass"
- "_operatorName"
- "_operatorQueue"
- "_operators"
- "_otherAggregateKeys"
- "_parseIOReportSampleFromStats:convertingUnitToUnityScale:"
- "_path"
- "_pendingDoneObjects"
- "_pendingObjectsLock"
- "_perModelTaskingTypeParameters"
- "_percentTimeFilter"
- "_performWithStartDate:endDate:"
- "_periodicCurrentTime"
- "_pid"
- "_plTaskingTables"
- "_ppsTaskingTables"
- "_preparedDynamicStatements"
- "_preparedStatements"
- "_preparedUpdateStatements"
- "_previousIOReportSample"
- "_processName"
- "_processThreadMap"
- "_profileDefaultsKQueue"
- "_purgeableLabelWithUrgency:startDate:"
- "_quarantineCopyResponder"
- "_quarantineResponder"
- "_queue"
- "_rebootOccurred"
- "_recordType"
- "_refCount"
- "_registration"
- "_relayActive"
- "_relayConnection"
- "_removeEntries"
- "_removeObserver:"
- "_repeats"
- "_request"
- "_rescheduleDelay"
- "_rootNodeEnergyRows"
- "_ruleIDToPendingJobs"
- "_rules"
- "_safeCopyInProgress"
- "_safeFileResponder"
- "_sampleTime"
- "_sampleTimePrevious"
- "_samplingPercentage"
- "_satisfied"
- "_seed"
- "_sem"
- "_service"
- "_serviceClassName"
- "_serviceClients"
- "_serviceName"
- "_services"
- "_setMonotonicFireDate:"
- "_signpostAllowlist"
- "_signpostDisable"
- "_sleepEntryNotification"
- "_sourceURL"
- "_sqlStorage"
- "_stage"
- "_stagingAggregateEntryCache"
- "_stagingEntryCache"
- "_stagingEntryCacheSize"
- "_startArgs"
- "_startDate"
- "_startMonitor"
- "_startTime"
- "_state"
- "_stateChangeMask"
- "_stateChangeNotifications"
- "_stateChangeTime"
- "_stateIDToStateMap"
- "_stateId"
- "_stateToken"
- "_statement"
- "_stopArgs"
- "_stopMonitor"
- "_stopTime"
- "_storage"
- "_storageLocked"
- "_storageMap"
- "_storageOperator"
- "_storageReady"
- "_storageStarted"
- "_submissionQueue"
- "_submitReasonType"
- "_submittedFilesMask"
- "_subscribedChannels"
- "_subscription"
- "_systemStateChangeTime"
- "_systemTime"
- "_systemTimeOffsetModified"
- "_tagConfig"
- "_tagUUID"
- "_targetContainer"
- "_taskingBuild"
- "_taskingConfig"
- "_taskingDeviceModels"
- "_taskingFiles"
- "_taskingMonitor"
- "_taskingPercentage"
- "_taskingPopulation"
- "_taskingRequestReason"
- "_taskingStarted"
- "_taskingType"
- "_threadID"
- "_threadName"
- "_threadNameToInfo"
- "_time"
- "_timeChangeBlocks"
- "_timeIntervalRange"
- "_timeManager"
- "_timeReferenceType"
- "_timeReferences"
- "_timeout"
- "_timer"
- "_tolerance"
- "_tooFarInFutureDistance"
- "_tooFarInPastDistance"
- "_totalSystemTime"
- "_totalUserTime"
- "_transactionInProgress"
- "_transactionLock"
- "_triggerBufferFlush"
- "_trimmingQueries"
- "_type"
- "_updateEntry:withBlock:"
- "_upgradeLogsResponder"
- "_userInfo"
- "_userPrefsCache"
- "_userRequestTransaction"
- "_userTime"
- "_utilityQueue"
- "_uuid"
- "_value"
- "_wakeEntryNotification"
- "_watchdog"
- "_wifiIn"
- "_wifiOut"
- "_wildCardName"
- "_workQueue"
- "_writeToDB"
- "_xpcActivityDelay"
- "_xpcActivityStarted"
- "_xpcConnection"
- "_xpcCrashMoverConn"
- "abmPLClnt"
- "absoluteTimeFilter"
- "accounting"
- "accountingGroupDefinitions"
- "activities"
- "activityBlock"
- "activityEntry"
- "activityEntryKey"
- "activityStatesEntryKey"
- "addAggdModeKeys"
- "addAuxiliaryType:withEntryKey:"
- "addCounter:withValue:"
- "addDaleDeviceConfig"
- "addDaleDeviceConfigDebug"
- "addDataWithCellIn:withCellOut:withWifiIn:withWifiOut:"
- "addDeviceConfigWith:andConfigExtension:"
- "addDimensions:withKey:withValue:"
- "addEntriesFromDictionary:"
- "addFilesToList:"
- "addICEDeviceConfig"
- "addICEDeviceConfigDebug"
- "addMDLogContext:"
- "addMSSContext:"
- "addMavDeviceConfig"
- "addMavDeviceConfigDebug"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:selector:name:object:"
- "addOperation:"
- "addPLEntryKey:"
- "addPLEntryKeyStringToTasking:"
- "addSinopeDeviceConfig"
- "addSinopeDeviceConfigDebug"
- "addStartEvent:withArgs:"
- "addStopEvent:withArgs:"
- "addTimeOffsetToMonotonicTime:"
- "addToLastEntryCache:"
- "addToLastEntryCacheSubKey:"
- "addToStagingAggregateEntryCache:"
- "addToStagingEntryCache:"
- "additionalTables"
- "agents"
- "aggregateBucketDefinitionsForEntryDefinition:"
- "aggregateBucketDefinitionsForEntryKey:"
- "aggregateEntriesForKey:withBucketLength:inTimeIntervalRange:"
- "aggregateFunction"
- "aggregateFunctionForEntryDefinition:forKey:"
- "aggregateKey"
- "aggregateOperationWithMatchingPairs:"
- "aggregateSignpostData:withReply:"
- "aggregateValue"
- "aggregatedSignpostDataWithEntryKey:withStartDate:withEndDate:withSignpostName:withProcess:withDataDict:"
- "allAggregateKeysForEntryDefinition:"
- "allAggregateKeysForEntryKey:"
- "allAggregatePrimaryKeysForEntryDefinition:"
- "allAggregatePrimaryKeysForEntryKey:"
- "allAppIdentiferKeysForEntryKey:"
- "allArchivePaths"
- "allArrayKeysForEntryKey:"
- "allBaseKeysForEntryKey:"
- "allCriteriaSatisfied"
- "allDMAKeysForEntryKey:"
- "allDefaultsEnabled"
- "allDynamicKeysForEntryDefinition:"
- "allDynamicKeysForEntryKey:"
- "allEntryKeys"
- "allEntryKeysForStorage:"
- "allIndexKeysForEntryDefinition:"
- "allIndexKeysForEntryKey:"
- "allKeys"
- "allKeysForEntryDefinition:"
- "allKeysForEntryKey:"
- "allMetricsForEntryKey:"
- "allObjects"
- "allOperatorTablesToTrimConditionsForTrimDate:"
- "allOperators"
- "allSubClassesForClass:"
- "allTablesInDB:"
- "allValues"
- "allocWithZone:"
- "allowQueryFromPeer:"
- "allowRun"
- "allowlistForSignpostAggregatedData"
- "allowlistResponder"
- "anyMetricsForEntryKey:"
- "appDeletionCriteria"
- "appIdentifier"
- "appendFormat:"
- "appendString:"
- "applicationID"
- "applyContainerPOSIXPermissions"
- "appsToKeep:"
- "archiveDirectoryAt:deleteOriginal:"
- "archiveEntriesFinished"
- "archiveEntriesUnfinished"
- "archiveEntriesWithComparisons:"
- "archiveEntry"
- "archiveForDate:"
- "archiveJobs"
- "archiveRetention"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "archivesResponder"
- "arm"
- "array"
- "arrayByAddingObjectsFromArray:"
- "arrayByRemovingObjectsFromArray:"
- "arrayKeyConfigsForEntryKey:"
- "arrayKeys"
- "arrayKeysForEntryDefinition:"
- "arrayKeysForEntryKey:"
- "arrayMetricsForEntryKey:"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObject:"
- "arrayWithObjects:"
- "arrayWithObjects:count:"
- "attachDB:withName:"
- "attemptToSendTaskingStartNotification"
- "attemptToUnregisterUploadSchedulingActivity"
- "attributesOfItemAtPath:error:"
- "audioOffCriterion"
- "autoUpdateEnabled"
- "automatedDeviceGroup"
- "autorelease"
- "auxiliaryType"
- "backgroundQueue"
- "baseCADictionary"
- "baseEntryKey"
- "baseEntryKeyForEntryKey:"
- "baseMetricsForEntryKey:"
- "basebandTimeNotification"
- "battPC0"
- "battPC1"
- "battPC2"
- "battPC3"
- "battPC4"
- "battPC5"
- "battPC6"
- "battPC7"
- "batteryUIPlistsResponder"
- "beginTransaction"
- "bgAudioTime"
- "bgEnergy"
- "bgLocationTime"
- "bgTime"
- "binaryPathForPid:"
- "bindEntry:toPreparedStatement:atBindPosition:"
- "bindValue:withFormater:atPosition:"
- "blPathResponder"
- "blobFailureReason"
- "block"
- "blockingFlushCachesCFNotification"
- "blockingFlushCachesWithReason:"
- "blockingFlushCachesWithReason:timeout:"
- "blockingFlushQueues:withTimeout:"
- "blockingUpdateEntry:withBlock:"
- "blockingWriteEntry:withCompletionBlock:"
- "boolForKey:"
- "boolForKey:ifNotSet:"
- "boolValue"
- "bootStateChange:"
- "brownoutRiskEngaged"
- "brownoutRiskPu"
- "brownoutRiskSysCap"
- "bucketForValue:forBucketSize:"
- "bucketNSDate:withBucketInterval:"
- "bucketTimeStampForDate:withTimeReference:withBucketInterval:"
- "bufferedEntries"
- "buildColumnInsert:andValueInsert:forEntry:"
- "buildDeviceMetadata"
- "buildVersion"
- "builds"
- "bundleForClass:"
- "bundleIDFromPid:"
- "bundleIDFromProcessName:"
- "bundleIDFromURL:"
- "bundleVersionFromURL:"
- "cacheContent"
- "cacheCountForEntryDefition:"
- "cacheCountForEntryKey:"
- "cacheSQLPrepareStatementForEntryDefinition:"
- "cacheSQLPrepareStatementForEntryKey:"
- "cachedClassName"
- "cachedEntryForEntryKey:withEntryID:"
- "cachedStatementForMetadataInsert"
- "calculateDeltaFromPreviousSamples"
- "calculateDeltaFromPreviousSamplesConvertingUnitToUnityScale:"
- "callStackSymbols"
- "canLogMode:fullMode:"
- "canSleepEntryNotificationWithOperator:withBlock:"
- "canSleepEntryNotificationWithWorkQueue:withBlock:"
- "cancel"
- "cancelActivityWithIdentifier:"
- "canceledFireDates"
- "capSize"
- "capValue"
- "carrierBuild"
- "caseInsensitiveCompare:"
- "categoryForEntryKey:"
- "cellIn"
- "cellOut"
- "changeClassProtection:"
- "changePermissionForDirectory:withProtectionLevel:"
- "changePermissionsForFilesInDirectory:withProtectionLevel:"
- "characterAtIndex:"
- "characterSetWithCharactersInString:"
- "checkCacheSizeForFlush"
- "checkEmptyMasterTable:"
- "checkForTimeChangeWithCurrentTime:"
- "checkOverridesEntryDateWithNowDate:"
- "checkTaskingCompletionStatus"
- "ckFileDirPath"
- "ckTagConfig"
- "class"
- "classForEntryKey:"
- "className"
- "cleanLaunchdApplicationMacOS:"
- "cleanLaunchdName:"
- "cleanup"
- "cleanupQuarantine"
- "cleanupTemporarySubmissionFilesForTag:"
- "cleanupTmp"
- "cleanupTmpDirectory"
- "clearLastEntryCacheForEntryKey:"
- "clearStop"
- "clearSubscription"
- "clearTableHasTimestampColumnCache"
- "clearTaskingDRConfig"
- "clearTaskingDefaults"
- "closeAllConnections"
- "closeConnection"
- "closeXPCConnection"
- "coalitionIDForPid:"
- "code"
- "collectMSS"
- "collection"
- "commonInitProcessWithFilePath:withCacheSize:"
- "commonTypeDict_BoolFormat"
- "commonTypeDict_DateFormat"
- "commonTypeDict_DateFormat_isCFAbsoluteTime"
- "commonTypeDict_IntegerFormat"
- "commonTypeDict_IntegerFormat_aggregateFunction_sum"
- "commonTypeDict_IntegerFormat_withUnit_W"
- "commonTypeDict_IntegerFormat_withUnit_mA"
- "commonTypeDict_IntegerFormat_withUnit_mAh"
- "commonTypeDict_IntegerFormat_withUnit_mJ"
- "commonTypeDict_IntegerFormat_withUnit_mV"
- "commonTypeDict_IntegerFormat_withUnit_ms"
- "commonTypeDict_IntegerFormat_withUnit_s"
- "commonTypeDict_IntegerFormat_withUnit_us"
- "commonTypeDict_RawDataFormat"
- "commonTypeDict_RealFormat"
- "commonTypeDict_RealFormat_aggregateFunction_sum"
- "commonTypeDict_RealFormat_withUnit_W"
- "commonTypeDict_RealFormat_withUnit_mJ"
- "commonTypeDict_RealFormat_withUnit_mW"
- "commonTypeDict_RealFormat_withUnit_mWhr"
- "commonTypeDict_RealFormat_withUnit_s"
- "commonTypeDict_StringFormat"
- "commonTypeDict_StringFormat_withAppName"
- "commonTypeDict_StringFormat_withBundleID"
- "commonTypeDict_StringFormat_withProcessName"
- "compare:"
- "compare:options:"
- "compare:with:"
- "compareFilesByKey:file1:file2:sortAscending:"
- "compareFloat:"
- "compareInt:"
- "comparisonOperation"
- "comparisonOperationString"
- "completeTaskingConfig:"
- "components:fromDate:"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "compressWithSource:withDestination:withLevel:"
- "compressWithSourceStream:withDestination:withLevel:"
- "compressedPath"
- "computeHourBucketOffset"
- "conditionCheckForAppIntents"
- "conditionCheckForEnergy"
- "conditionCheckForTaskingType:"
- "conditionCheckForXcodeUserActions"
- "configFromMonitor:"
- "configsForEntryDefinition:"
- "configsForEntryKey:"
- "configuration"
- "configureCacheFlush"
- "configureWithDefaultValues"
- "configureWithDictionary:"
- "conformsToProtocol:"
- "conn"
- "connection"
- "connectionByStorage"
- "connectionForKey:"
- "connectionToQuarantine:"
- "connectionToServer"
- "constructAppReferenceMapping"
- "constructAppReferenceTableList"
- "constructEntryDefinition:"
- "constructFileNames"
- "constructUpdateQueries"
- "containerPath"
- "containsAtleastOneOf:"
- "containsDate:"
- "containsObject:"
- "containsString:"
- "containsStringInArray:"
- "contentsOfDirectoryAtPath:error:"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "contextDictionary"
- "continuousTimeToAbsoluteNs:"
- "convertFromBasebandToMonotonic"
- "convertFromMonotonicToBaseband"
- "convertFromMonotonicToSystem"
- "convertFromSystemToMonotonic"
- "convertTime:fromTimeReference:toTimeReference:"
- "convertToBase10:fromBaseN:"
- "copy"
- "copyAndPrepareLog"
- "copyArchiveAtPath:to:"
- "copyDB"
- "copyDatabase:"
- "copyDatabaseToPath:"
- "copyDatabaseToPath:fromDate:toDate:"
- "copyDatabaseToPath:fromDate:toDate:withTableFilters:vacuumDB:"
- "copyDatabaseToPath:fromDate:toDate:withTableFilters:vacuumDB:withCacheSize:"
- "copyItemAtPath:toPath:error:"
- "copyItemAtURL:toURL:error:"
- "copyLastArchiveToPath:"
- "copyPowerlogToPath:"
- "copyPropertyForKey:"
- "copyRBDCLogsToPath:withServiceType:"
- "copyTable:fromConnection:withDBName:withProperties:andAttach:"
- "copyTable:fromDBName:withProperties:"
- "copyUpgradePowerlogToPath:"
- "copyUpgradePowerlogsAtPath:toPath:"
- "copyWithIsDynamic:"
- "copyWithTimeIntervalRange:"
- "copyWithWildCardName:"
- "copyWithZone:"
- "coreStorage"
- "countByEnumeratingWithState:objects:count:"
- "countOfEntriesForKey:"
- "countSafetyDrop"
- "countWarnings"
- "cpuTimeForProcess:"
- "crPath"
- "crashMoverQueue"
- "crashReporterKey"
- "createAndChownDirectory:"
- "createAndChownDirectoryIfDirectoryDoesNotExist:"
- "createCompositeIndexOnTable:forColumns:"
- "createCounter:withLabel:"
- "createCounter:withLabel:withDimensions:withFlags:"
- "createDimensions:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "createEntriesForMetrics:withData:withDate:"
- "createFileAtPath:contents:attributes:"
- "createGauge:withLabel:"
- "createGauge:withLabel:withDimensions:withLevel:withFlags:"
- "createHangTableInDB:"
- "createHistogram:withLabel:withBins:withInterval:"
- "createHistogram:withLabel:withDimensions:withLevel:withBins:withInterval:withFlags:"
- "createIndexOnTable:forColumn:"
- "createMetadataTable"
- "createMetricGroup:withDimensions:"
- "createTableName:withColumns:"
- "createTagFileWithPath:"
- "createTagFileWithPath:withInfo:"
- "createWatchdogForSubmissionActivity:"
- "createXPCConnection"
- "criteria"
- "criteriaString"
- "criterionBlock"
- "criticalBatteryLevel"
- "currValue"
- "currentCalendar"
- "currentConfigSnapshotWithErrorOut:"
- "currentDate"
- "currentLocale"
- "currentSnapshot"
- "currentTime"
- "currentTimeFromTimeReference:toTimeReference:"
- "currentValueForSimpleChannel:"
- "currentValueForStateChannel:atIndex:"
- "customGetNearestMidnight"
- "d"
- "d16@0:8"
- "d24@0:8@16"
- "d24@0:8Q16"
- "d24@0:8d16"
- "d24@0:8q16"
- "d28@0:8d16i24"
- "d28@0:8i16d20"
- "d32@0:8@16@24"
- "d32@0:8@16d24"
- "d32@0:8d16@24"
- "d32@0:8q16Q24"
- "d40@0:8@16@24@32"
- "daFileDirPath"
- "dailyTaskNotification"
- "dailyTaskTimer"
- "dailyTasks"
- "dataCollectionCriterion"
- "dataDuration"
- "dataFormatForMetric:auxiliaryMetrics:"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dataWithContentsOfFile:"
- "dataWithJSONObject:options:error:"
- "datatype"
- "dateByAddingTimeInterval:"
- "dateBySettingHour:minute:second:ofDate:options:"
- "dateFromComponents:"
- "dateFromString:"
- "dateFromTimeval:"
- "dateFromTimevalSystemTime:"
- "dateFromnSecEpoch:"
- "dateIsMidnightLocalTime:"
- "dateWithTimeInterval:sinceDate:"
- "dateWithTimeIntervalSince1970:"
- "dateWithTimeIntervalSinceNow:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "dayChangedNotification"
- "dayChangedNotificationReceived:"
- "dbConnection"
- "dbSem"
- "dealloc"
- "debugDescription"
- "debugInstance"
- "debugScheduledTimerWithMonotonicFireDate:withInterval:withQueue:withBlock:"
- "debug_forceEligibility"
- "debug_installDate"
- "debug_treatAsTestDevice"
- "decodeEtherType:"
- "decodeIPPacket:encryptedPath:"
- "decodeIntegerForKey:"
- "decodeObjectForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decompressWithSource:withDestination:withRemoveSrc:"
- "decompressWithSourceStream:withDestinationStream:"
- "decorateFile"
- "decorateFileAtPath:"
- "defaultBatteryEnergyCapacity"
- "defaultBoolForKey:"
- "defaultCStringEncoding"
- "defaultCenter"
- "defaultDateFormatter"
- "defaultDoubleForKey:"
- "defaultLongForKey:"
- "defaultManager"
- "defaultObjectForKey:"
- "defaultService"
- "defaultTaskingTypeParameters"
- "defaults"
- "defaultsKeyFromEntryDefinitionKey:"
- "deferActivity:"
- "deferXPCActivity:"
- "definedKeys"
- "definitionForEntryKey:"
- "definitionForKey:"
- "delegate"
- "deleteAllEntriesForKey:"
- "deleteAllEntriesForKey:beforeTimestamp:"
- "deleteAllEntriesForKey:beforeTimestamp:withFilters:"
- "deleteAllEntriesForKey:withFilters:"
- "deleteAppReferenceMapping"
- "deleteAppReferences:"
- "deleteAppReferencesFromCompressedFiles:"
- "deleteAppReferencesInCurrentPowerlog"
- "deleteArrayEntriesForKey:withRowID:"
- "deleteDynamicEntriesForKey:withRowID:"
- "deleteEntry:"
- "deleteEntryForKey:WithRowID:"
- "deleteEntryForKey:withRowID:"
- "deleteOldMetadataStore"
- "deltaValueForSimpleChannel:"
- "deltaValueForStateChannel:atIndex:"
- "deprecateOldFullMode"
- "deprecateTables"
- "deprecateTablesBGSQL"
- "deprecateTablesEPSQL"
- "deprecateTablesXCSQL"
- "deregisterTaskWithIdentifier:"
- "description"
- "descriptionRespectingAllowlist:"
- "descriptionSingleLine"
- "detachDB:"
- "deviceBootArgs"
- "deviceBootTime"
- "deviceBootUUID"
- "deviceCapability"
- "deviceCapabilityMapping"
- "deviceRebooted"
- "diagnosticLogSubmissionEnabled"
- "dice"
- "dictionary"
- "dictionaryForKey:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "dictionaryWithValuesForKeys:"
- "didChangeCriterion:"
- "didCompleteActivity:"
- "didDisableActivity:"
- "didEnableActivity:"
- "didInterruptActivity:"
- "didRecieveMemoryPressureWarning"
- "diffSinceBaseline:"
- "diffSinceLastSnapshot"
- "diffSnapshotWithNew:andOld:"
- "directionality"
- "directionalityForEntryKey:"
- "directory"
- "directorySize:"
- "disable"
- "disableHangtracer"
- "dispatchAsyncForEntryKey:withBlock:"
- "dispatchQueue"
- "dispatchSyncForEntryKey:withBlock:"
- "dispatchSyncIfNotCallerQueue:withBlock:"
- "dispatchTimeInSeconds:"
- "displayAODNotificationWithOperator:withBlock:"
- "displayOffCriterion"
- "displayOffNotificationWithOperator:withBlock:"
- "displayOffOrAODNotificationWithOperator:withBlock:"
- "displayOnNotificationWithOperator:withBlock:"
- "displayOnOrAODNotificationWithOperator:withBlock:"
- "displaySchema:"
- "displayStateChangeNotificationWithOperator:withBlock:"
- "distantFuture"
- "distantPast"
- "doubleForKey:"
- "doubleForKey:ifNotSet:"
- "doubleValue"
- "drConfigMonitor"
- "driverName"
- "droopCE"
- "dropAppVersions:"
- "dropDataFromDB:withConfig:"
- "dropDuplicateRows:"
- "dropTable:"
- "dropTables:"
- "dropTablesFromDB:withConfig:"
- "duetDiscretionaryBudget"
- "dumpEntryCache:"
- "dumpLastEntryCache"
- "dumpStagingEntryCache"
- "dynamicEntryKeyForEntryKey:"
- "dynamicKeyConfigsForEntryDefinition:"
- "dynamicKeyConfigsForEntryKey:"
- "dynamicKeys"
- "dynamicMetricsForEntryKey:"
- "dynamicTableNameForEntryKey:"
- "eligibilityDuration"
- "eligibilityRange"
- "eliglibleToVacuumEPSQLForDate:"
- "emitAttemptEvent"
- "emitBlobDetectedEvent:"
- "emitBlobVerifiedEvent:"
- "emitCollisionEvent:"
- "emitCopyResult:"
- "emitDecompressionResult:"
- "emitFileExists:"
- "emitPreparationResult:"
- "emitQueryEvent:"
- "emitSubmitEvent"
- "emitSuccessEvent"
- "emitTaskingTypeSpecifiedEvent"
- "enable"
- "enableBufferFlushTimer:"
- "enableDPUpload"
- "enableHangtracer"
- "enableRestartAtEPL"
- "enabledPopulation"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endTransaction"
- "enqueueFileForUpload:"
- "enqueueSubmissionRecord:"
- "entriesForKey:"
- "entriesForKey:before:timeInterval:count:withFilters:"
- "entriesForKey:inTimeRange:withCountOfEntriesBefore:withCountOfEntriesAfter:withFilters:"
- "entriesForKey:inTimeRange:withFilters:"
- "entriesForKey:startingFromRowID:count:withFilters:"
- "entriesForKey:withComparisons:"
- "entriesForKey:withProperties:"
- "entriesForKey:withQuery:"
- "entryAggregateDefinitionEnergy"
- "entryAggregateDefinitionQualificationEnergy"
- "entryAggregateDefinitions"
- "entryCacheStorageSize"
- "entryDefinition"
- "entryDefinitionKey"
- "entryDefinitionsForOperator:"
- "entryDefinitionsForOperatorClass:"
- "entryEventBackwardDefinitionDistributionEvents"
- "entryEventBackwardDefinitionPowerEvents"
- "entryEventBackwardDefinitionQualificationEvents"
- "entryEventBackwardDefinitions"
- "entryEventForwardDefinitionActivityStates"
- "entryEventForwardDefinitionConfiguration"
- "entryEventForwardDefinitionDistributionEvents"
- "entryEventForwardDefinitionPowerEvents"
- "entryEventForwardDefinitionQualificationEvents"
- "entryEventForwardDefinitionSchemaChange"
- "entryEventForwardDefinitionSubmissionTag"
- "entryEventForwardDefinitionTaskingMode"
- "entryEventForwardDefinitionTimeOffset"
- "entryEventForwardDefinitions"
- "entryEventIntervalDefinitionCacheSize"
- "entryEventIntervalDefinitionDebugEnergyEstimateEvents"
- "entryEventIntervalDefinitionDistributionEvents"
- "entryEventIntervalDefinitionEnergyEstimateEvents"
- "entryEventIntervalDefinitionInProcessAnimation"
- "entryEventIntervalDefinitionPowerEvents"
- "entryEventIntervalDefinitionQualificationEvents"
- "entryEventIntervalDefinitionScrollView"
- "entryEventIntervalDefinitionUINavigationController"
- "entryEventIntervalDefinitions"
- "entryEventNoneDefinitionActivity"
- "entryEventNoneDefinitionAdditionalTablesTurnedOn"
- "entryEventNoneDefinitionAppSwitchTrigger"
- "entryEventNoneDefinitionDistributionRules"
- "entryEventNoneDefinitionNodes"
- "entryEventNoneDefinitionQualificationRules"
- "entryEventNoneDefinitions"
- "entryEventPointDefinitionArchive"
- "entryEventPointDefinitionCacheFlush"
- "entryEventPointDefinitionDistributionEvents"
- "entryEventPointDefinitionOTA"
- "entryEventPointDefinitionPLLog"
- "entryEventPointDefinitionQualificationEvents"
- "entryEventPointDefinitionTimeCorrection"
- "entryEventPointDefinitions"
- "entryForKey:withID:"
- "entryIDForNewEntry:"
- "entryKey"
- "entryKeyForMetric:"
- "entryKeyForOperatorName:withType:withName:"
- "entryKeyForOperatorName:withType:withName:isDynamic:"
- "entryKeyForOperatorName:withType:withName:withWildCardName:"
- "entryKeyForOperatorName:withType:withName:withWildCardName:isDynamic:"
- "entryKeyForType:andName:"
- "entryKeyForType:andName:isDynamic:"
- "entryKeyFromSelector:"
- "entryKeyStringForOperatorName:withType:withName:"
- "entryKeyToStateMap"
- "entryKeys"
- "entryKeysForOperator:"
- "entryKeysForOperatorClass:"
- "entryKeysForOperatorName:"
- "entryKeysForOperatorNameCopy:"
- "entryKeysToSetup"
- "entryListener"
- "entryName"
- "entrySelectorForMetric:"
- "entryType"
- "entryWithEntryKey:withData:"
- "entryWithEntryKey:withRawData:"
- "enumerateAllTablesWithBlock:"
- "enumerateCriteriaWithBlock:"
- "enumerateEntryCache:withBlock:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "enumerateStagingEntryCacheForEntryKey:withBlock:"
- "enumerateStagingEntryCacheWithBlock:"
- "enumerateTablesWithBlock:"
- "enumeratorAtPath:"
- "eplEnabled"
- "errorWithDomain:code:userInfo:"
- "eventIntervalCacheSizeWithPayload:withEntryDate:"
- "eventPointCacheFlushWithPayload:"
- "eventSystemClient"
- "excludeTestDevices"
- "executeBlockCache"
- "existsInDB"
- "exitSafe:"
- "exitWithReason:"
- "exitWithReason:action:"
- "exitWithReason:connection:"
- "exitWithReasonSync:"
- "experimentGroup"
- "extractDateStringAndUUIDStringFromFilePath:"
- "f+PE44W6AO2UENJk3p2s5A"
- "fallbackDefaultBatteryEnergyCapacity"
- "fgEnergy"
- "fgTime"
- "fileCleanupWithRecord:"
- "fileDescriptor"
- "fileExistsAtPath:"
- "fileExistsAtPath:isDirectory:"
- "fileExtension"
- "fileModificationDate"
- "filePermissionCriteria"
- "filePosixPermissions"
- "fileSize"
- "fileSizeAtPath:"
- "fileSystemRepresentation"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "filenameDateStringWithStartDate:endDate:"
- "filter"
- "filterDefinitions"
- "filterDeltaLastEntryIDs"
- "filterDiff:"
- "filterEntryLogging"
- "filterEntryLoggingForEntryDefinition:"
- "filterEntryLoggingForEntryKey:"
- "filterQuery"
- "filteredArrayUsingPredicate:"
- "finalize"
- "finishActivity:withStatus:"
- "finishXPCActivity:"
- "fire"
- "fireDate"
- "firstEntryForKey:"
- "firstObject"
- "fixedArraySize"
- "flags"
- "flatStorage"
- "floatValue"
- "flush"
- "flushBuffer"
- "flushCachesCFNotification"
- "flushCachesIfRequiredForEntryKey:"
- "flushCachesTimer"
- "flushCachesWithReason:"
- "flushMicrostackshots"
- "flushStagingAggregateEntryCacheToDatabase"
- "flushStagingEntryCacheToDatabase"
- "followupCurrentTimeRunning"
- "formaterForKey:"
- "formattedStringForDate:"
- "formatterFromDataType:"
- "freeMetadataState"
- "fullModeDaemonName"
- "fullModeForClass:"
- "fullModeSubmissionBehavior"
- "fullPLLog"
- "fullProcessNameForPid:"
- "fullVacuum"
- "gasGaugeEnabled"
- "generalEntryCacheSizeLimit"
- "generateAndUpdateSaltValue:"
- "generateContextDictionary:"
- "generateDummyPayload"
- "generateForTimeRange:"
- "generateHashValue:withSalt:"
- "generateMSS"
- "generateMSSReportForRAPID:withReply:"
- "generateMSSReportForTasking:withReply:"
- "generateMSSSubmissionWithPayload:"
- "generateOTASubmissionAndSendTaskingEndSubmission:"
- "generatePLLSubmissionWithPayload:"
- "generateRapidMSSWithStartDate:endDate:atPath:"
- "generateRapidSignpostSummaryWithStartDate:endDate:"
- "generateSignpostSubmissionWithTagConfig:withAllowlist:withStartDate:withEndDate:includeSPFile:"
- "generateSubmissionTagForCurrentLog"
- "generateTaskingMSSWithStartDate:endDate:atPath:"
- "getAllSubsystem"
- "getAllowblocklist"
- "getAllowlist"
- "getArchivingCriteria"
- "getBDCPlistFile"
- "getBGSQLFile"
- "getBasebandBootState"
- "getBasebandChipset"
- "getBasebandFirmwareVersion"
- "getBasebandTimeAndLatency"
- "getBootSessionUUID"
- "getBuildVersion"
- "getCESQLFile"
- "getCKSubmissionDirPathForTag:"
- "getCacheSpillValue"
- "getCompanionLink:"
- "getCurrMachAbsTimeInSecs"
- "getCurrState:"
- "getCurrentDRConfig"
- "getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:"
- "getCurrentStats"
- "getDASubmissionDirPathForTag:"
- "getDateMarker"
- "getDateMarkerFromSystemDate:"
- "getDateMarkerLegacy"
- "getDefaultL0bThresholdForDeviceType"
- "getDeltaStats"
- "getDeviceClass"
- "getDisplayBlock"
- "getEPSQLFile"
- "getEntryFromDBForEntryKey:withMatchingKeyToValue:"
- "getFeatureFlags"
- "getFeatureFlags:"
- "getFileList"
- "getFirstBatteryTimestamp"
- "getHardwareModel"
- "getHardwarePerfLevels"
- "getHardwarePlatform"
- "getHeatmapData:withReply:"
- "getHourBucketOffset"
- "getIPAddress:withAddressFamily:"
- "getIdentifierFromEntry:"
- "getIntegrityCheckCriteria"
- "getInterfaceType:withPktIFName:withPktIFInfo:withPktPhyIFInfo:"
- "getInverseDeviceID"
- "getJetsamPriority:"
- "getKVPairsForCASubmissionFromEntry:"
- "getLTESleepManagerStats"
- "getLastBatteryTimestamp"
- "getLastBatteryTimestampSystem"
- "getLastState:"
- "getLastSystemTimeOffset"
- "getListOfRequiredBDCFiles"
- "getMachTimebase"
- "getMachbaseTimeRatio"
- "getMetadataByCategoryForSubsystem:"
- "getMetadataByNameForSubsystem:category:"
- "getMetadataForSubsystem:category:name:"
- "getNetworkWakeInfo:"
- "getNormalizedIPV6Address:"
- "getNumberOfDCPEXT"
- "getOverridableMonotonicNow"
- "getPerfStatsForProcess:"
- "getPrivacyAllowlist"
- "getProcessMemoryLimit:"
- "getProductType"
- "getProductTypeCode"
- "getProtectionLevel:"
- "getQueryForAggregateEntryKey:withMatchingKeyToValue:"
- "getRbdcData:withReply:"
- "getResourceValue:forKey:error:"
- "getSBCMaxTimeInterval"
- "getSBCMinTimeInterval"
- "getSampleDuration"
- "getSeqNoAndSPI:offset:"
- "getSessionsAllowlist"
- "getSignpostMetricsWithStartDate:withEndDate:processMXSignpost:"
- "getSignpostNameValueGroupTypeFor:"
- "getSignpostSummaryWithAllowlist:withStartDate:withEndDate:"
- "getState:beforeDate:"
- "getStateBeforeSystemStateChange:"
- "getStateChangeTime:"
- "getSubmitReasonTypeToCAFieldValue"
- "getSubmitReasonTypeToFlushReason"
- "getSubmitReasonTypeToReasonLog"
- "getSubmitReasonTypeToStorageEventOTAType"
- "getSystemStateChangeTime"
- "getTestAllowlist"
- "getThreadName:inProcess:isNamed:"
- "getTimebaseInfo"
- "getUnattributedWakeInfo:"
- "getUserAssignedDeviceName"
- "getWifiChipset"
- "getXCSQLFile"
- "grabSysctlValue:"
- "grabSysctlValueInt64:"
- "grant0"
- "grant1"
- "grant2"
- "handleAppDeletionXPCActivityCallback:"
- "handleCrashMoverConnection:"
- "handleDRConfigUpdate:error:"
- "handleEvent:"
- "handleFailure:forArchiveEntry:"
- "handleFilePermissionXPCActivityCallback:"
- "handleForIdentifier:error:"
- "handleMetadataVersionChange"
- "handlePeer:forEvent:"
- "handlePowerWakeEvent:"
- "handleSchemaMismatchForTable:"
- "handleSchemaMismatchForTable:expectedVersion:schemaMatch:"
- "handleStateChange:"
- "handleTask:"
- "handleTimerFire"
- "handleXPCActivityCallback:"
- "hangTypeFromStr:"
- "has5G"
- "hasAAPC"
- "hasANE"
- "hasAOD"
- "hasAOP"
- "hasAOP2"
- "hasAOT"
- "hasAlwaysListening"
- "hasAppIdentiferKeys:"
- "hasAppIdentifierKeys"
- "hasAppIdentifierKeysForEntryDefinition:"
- "hasArrayKeys"
- "hasArrayKeys:"
- "hasArrayKeysForEntryDefinition:"
- "hasArrayKeysForEntryKey:"
- "hasBaseband"
- "hasBattery"
- "hasBatteryModuleAuth"
- "hasCapability:"
- "hasDCP"
- "hasDMAKeys"
- "hasDMAKeys:"
- "hasDMAKeysForEntryDefinition:"
- "hasDMAKeysForEntryKey:"
- "hasDynamicChargingLimit"
- "hasDynamicKeys"
- "hasDynamicKeys:"
- "hasDynamicKeysForEntryDefinition:"
- "hasDynamicKeysForEntryKey:"
- "hasEqualComparisonComponent"
- "hasFileToSubmit"
- "hasFixedChargingLimit"
- "hasGasGauge"
- "hasGenerativeModelSystems"
- "hasGreaterThanComparisonComponent"
- "hasInductiveCharging"
- "hasInternalKey"
- "hasInternalKey:"
- "hasLPEM"
- "hasLPM"
- "hasLPW"
- "hasLessThanComparisonComponent"
- "hasMesa"
- "hasMessageOnDevice"
- "hasNFC"
- "hasNilComparisonComponent"
- "hasOLED"
- "hasOrb"
- "hasPearl"
- "hasPerseus"
- "hasPlatinum"
- "hasPrefix:"
- "hasProximitySensor"
- "hasRearALS"
- "hasSleepMedia"
- "hasSuffix:"
- "hasTaskModeKeyForEntryDefinition:"
- "hasTaskModeKeyInConfig:"
- "hasWirelessCharger"
- "hasWristTemperature"
- "hash"
- "hashBundleID:"
- "hashEntries"
- "hashEntryKeyKeys:"
- "hashString:"
- "hourBucketBaseSnapOffsetWithMonotonicTime:"
- "hourBucketBaseSnapOffsetWithMonotonicTimeNow:"
- "hourBucketOffset"
- "hourBucketOffsetKeyFromEntryDefinitionKey:"
- "i16@0:8"
- "i24@0:8@16"
- "i32@0:8@16@24"
- "i32@0:8@16s24i28"
- "i32@0:8^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}16^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}24"
- "i36@0:8@16@24i32"
- "i36@0:8@16q24i32"
- "i36@0:8^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}16^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}24i32"
- "i36@0:8i16@20@28"
- "i48@0:8*16*24^{npi_if_info=III}32^{npi_if_info=III}40"
- "iCloudUploadEnabled"
- "identity"
- "inBUIDemoMode"
- "inSubmission"
- "indexOfObject:"
- "init"
- "initEntryWithData:"
- "initEntryWithRawData:"
- "initFileURLWithPath:"
- "initForTest"
- "initNotificationTimerWithWorkQueue:withBlock:"
- "initNotificationTimerWithWorkQueue:withMaxInterval:withBlock:"
- "initOperatorDependancies"
- "initOperatorDependanciesWithBlock:"
- "initServices"
- "initSubmissionQueue"
- "initTagInfoForReasonType:withStartDate:withEndDate:"
- "initTaskOperatorDependancies"
- "initWithArray:"
- "initWithBytes:length:encoding:"
- "initWithCKFilePath:tagUUID:tagConfig:configUUID:configDateReceived:configDateApplied:"
- "initWithCalendarIdentifier:"
- "initWithCoder:"
- "initWithConfig:"
- "initWithContainerID:"
- "initWithContainerIdentifier:environment:"
- "initWithContentsOfFile:"
- "initWithContentsOfURL:error:"
- "initWithData:encoding:"
- "initWithDomain:code:userInfo:"
- "initWithDriverName:withGroup:"
- "initWithEntryDate:"
- "initWithEntryKey:"
- "initWithEntryKey:withCriterionBlock:"
- "initWithEntryKey:withData:"
- "initWithEntryKey:withDate:"
- "initWithEntryKey:withFilter:withCriterionBlock:"
- "initWithEntryKey:withRawData:"
- "initWithFilePath:"
- "initWithFilePath:withCacheSize:"
- "initWithFilePath:withCacheSize:withFlags:"
- "initWithFilePath:withFlags:"
- "initWithFileURL:"
- "initWithFireDate:withInterval:withTolerance:repeats:withUserInfo:withQueue:withBlock:"
- "initWithFormat:"
- "initWithGroup:andSubGroup:"
- "initWithGroup:andSubGroup:withChannelIDs:"
- "initWithGroup:andSubGroup:withChannelIDs:manualChannelOnly:"
- "initWithIdentifier:"
- "initWithIdentifier:withCriteria:withMustRunCriterion:withQueue:withInterruptBlock:withActivityBlock:"
- "initWithInterval:"
- "initWithKey:"
- "initWithKey:withValue:withComparisonOperation:"
- "initWithLocaleIdentifier:"
- "initWithManager:andArchiveEntry:"
- "initWithMetadata:"
- "initWithMonotonicFireDate:withInterval:withQueue:withBlock:"
- "initWithName:andID:"
- "initWithName:withFGEnergy:withBGEnergy:withFGTime:withBGTime:withBGAudioTime:withBGLocationTime:withRootNodeEnergyRows:"
- "initWithObjects:"
- "initWithObjectsAndKeys:"
- "initWithOperator:forDynamicServiceClass:forNotificationType:withMatchBlock:"
- "initWithOperator:forEntryKey:forUpdateOrInsert:withBlock:"
- "initWithOperator:forEntryKey:forUpdateOrInsert:withFilter:withBlock:"
- "initWithOperator:forEntryKey:withBlock:"
- "initWithOperator:forEntryKey:withFilter:withBlock:"
- "initWithOperator:forNotification:requireState:withBlock:"
- "initWithOperator:forNotification:withBlock:"
- "initWithOperator:forNotifications:withBlock:"
- "initWithOperator:forService:"
- "initWithOperator:forService:withBlock:"
- "initWithOperator:forServiceClass:"
- "initWithOperator:forServiceClass:withBlock:"
- "initWithOperator:forUsagePage:andUsage:withBlock:"
- "initWithOperator:withRegistration:withBlock:"
- "initWithOperatorName:withEntryType:withEntryName:"
- "initWithPath:withDispatchQueue:withBlock:"
- "initWithPayload:"
- "initWithProcessInfo:"
- "initWithQueue:withBlock:"
- "initWithReasonType:"
- "initWithReasonType:DRConfig:"
- "initWithRecordType:"
- "initWithRecordsToSave:recordIDsToDelete:"
- "initWithSQLQuery:forDatabase:withDBSem:result:"
- "initWithServiceName:"
- "initWithStartDate:endDate:"
- "initWithStartDate:endDate:andUUID:"
- "initWithStartTime:withStartargs:"
- "initWithStateId:entryKey:currValue:"
- "initWithString:"
- "initWithSuiteName:"
- "initWithTeamID:targetQueue:configProcessingBlock:"
- "initWithThread:inProcess:"
- "initWithTime:andLatency:"
- "initWithTimeFilter:withPercentFilter:withProcessThreadMapping:withError:"
- "initWithTimeManager:entryDefinitionKey:timeReferenceType:"
- "initWithUUIDBytes:"
- "initWithUUIDString:"
- "initWithWorkQueue:forEntryKey:forUpdateOrInsert:withBlock:"
- "initWithWorkQueue:forEntryKey:forUpdateOrInsert:withFilter:withBlock:"
- "initWithWorkQueue:forEntryKey:withBlock:"
- "initWithWorkQueue:forEntryKey:withFilter:withBlock:"
- "initWithWorkQueue:forNotification:requireState:withBlock:"
- "initWithWorkQueue:forNotification:withBlock:"
- "initWithWorkQueue:forNotifications:withBlock:"
- "initWithWorkQueue:withRegistration:withBlock:"
- "initialMonotonicTime"
- "initializeFilesToBeSubmitted"
- "initializeOffsetHistoryWithEntries:"
- "initializeOffsetWithEntries:"
- "initializeSamplingPercentage"
- "initializeState"
- "initializeTaskingParams"
- "initializeTimeOffsets"
- "insertIntoStagingEntryCache:"
- "insertObject:atIndex:"
- "installDate"
- "instancePrefsCache"
- "instancePrefsObjectForKey:"
- "intValue"
- "integerValue"
- "interestedObjects"
- "interfaceNameForIndex:"
- "interfaceWithProtocol:"
- "internalBuild"
- "internalKey"
- "internalSubmissionBehavior"
- "interruptActivity"
- "interruptBlock"
- "interrupted"
- "interval"
- "intervalPeakCADictionaryForLaunchdName:intervalMaxKB:"
- "invalidate"
- "ioNotifyPort"
- "ioReportSample"
- "is64Bit"
- "isALSCurveHigherThanDefault"
- "isARMMac"
- "isActive"
- "isAggregateForEntryDefinition:"
- "isAggregateForEntryKey:"
- "isAggregateWallClockBucket:"
- "isAggregateWallClockBucketForEntryDefinition:"
- "isAllowedMetric:"
- "isAllowedPopulation:"
- "isAllowedSubsystem:"
- "isAllowedSubsystem:category:"
- "isAppAnalyticsEnabled"
- "isAppleTV"
- "isAppleVision"
- "isArchARM"
- "isAtEnd"
- "isAudioClass:"
- "isBasebandClass:"
- "isBasebandDSDS"
- "isBasebandDale"
- "isBasebandIBIS"
- "isBasebandIce"
- "isBasebandMav"
- "isBasebandMavLeg"
- "isBasebandMavToAllowSysdiagnoseTrigger"
- "isBasebandProto"
- "isCameraClass:"
- "isClassDebugEnabled:"
- "isClassDebugEnabled:forKey:"
- "isClassNameDebugEnabled:"
- "isClassNameDebugEnabled:forKey:"
- "isComputeModule"
- "isDRTasking"
- "isDaemon"
- "isDaemonOrAppleXPCService:"
- "isDebugEnabled"
- "isDebugEnabledForKey:"
- "isDelete"
- "isDevBoard"
- "isDeviceClass:"
- "isDeviceClassName:"
- "isDisplayClass:"
- "isDynamic"
- "isESPPacket:offset:"
- "isEduMode"
- "isEligible"
- "isEnabled"
- "isEnergyTasking"
- "isEntryKeySetup:forOperatorName:"
- "isEqual:"
- "isEqualToDate:"
- "isEqualToProcessInfo:"
- "isEqualToString:"
- "isEqualToThreadInfo:"
- "isErrorEntry"
- "isExpedited"
- "isFormater:validForObject:"
- "isFullModeDaemon"
- "isGPSClass:"
- "isHealthDataSubmissionAllowed"
- "isHeySiriAlwaysOn"
- "isHeySiriEnabled"
- "isHomePod"
- "isImproveFitnessPlusEnabled"
- "isInMonotonicFuture"
- "isInMonotonicFutureWithDistance:"
- "isInMonotonicPastWithDistance:"
- "isIncrementalVacuumEnabled"
- "isInsert"
- "isInterrupted"
- "isKeyAggregateValue:"
- "isKeyDynamic:"
- "isKindOfClass:"
- "isLiteModeDaemon"
- "isLowPowerModeSupported"
- "isMac"
- "isMemberOfClass:"
- "isModelTrigger"
- "isModelingDebugEnabled"
- "isNamed"
- "isNarrowScreen"
- "isNil"
- "isNil:"
- "isNonEmptyDictionary:"
- "isOnDemandQueryableForEntryDefinition:"
- "isOnDemandQueryableForEntryKey:"
- "isPPSEnabled"
- "isPercentageSupported"
- "isPerfPowerMetricd"
- "isPingPongChargingWith:andBatteryLevelPercent:"
- "isPowerexceptionsd"
- "isPowerlogHelperd"
- "isPrivacySensitive:"
- "isProcessRbdcAllowed"
- "isProxy"
- "isSafetyDataSubmissionAllowed"
- "isSetupAllowedForMetric:"
- "isSiriEnabled"
- "isSoCClass:"
- "isStartPresent"
- "isStateRequired"
- "isStopPresent"
- "isSubclassOfClass:"
- "isSupersetOfSet:"
- "isTVOS"
- "isTaskFullEPLMode"
- "isTestDeviceForSafeguard"
- "isTorchClass:"
- "isTransactionInProgress"
- "isUploadSizeWithinLimit:"
- "isUsingAnOlderWifiChip"
- "isValid"
- "isValidJSONObject:"
- "isValidModeForMetric:"
- "isValidString:"
- "isValidSubmissionFilesMask"
- "isValidTaskingBlob"
- "isVirtualDevice"
- "isWatch"
- "isWiFiClass:"
- "isXPCService"
- "isiOS"
- "isiPad"
- "isiPhone"
- "isiPod"
- "issueCategory"
- "issueDescription"
- "iterateAgents"
- "iterateMetrics"
- "iterateServices"
- "iterator"
- "j8/Omm6s1lsmTDFsXjsBfA"
- "kPLAudioClassIsOneOf:"
- "kPLAudioClassOfDevice"
- "kPLBasebandClassIsOneOf:"
- "kPLBasebandClassOfDevice"
- "kPLCameraClassIsOneOf:"
- "kPLCameraClassOfDevice"
- "kPLDeviceClass"
- "kPLDeviceClassIsOneOf:"
- "kPLDeviceClassName"
- "kPLDeviceMap"
- "kPLDisplayClassIsOneOf:"
- "kPLDisplayClassOfDevice"
- "kPLGPSClassIsOneOf:"
- "kPLGPSClassOfDevice"
- "kPLPlatformAttributes"
- "kPLSoCClassIsOneOf:"
- "kPLSoCClassOfDevice"
- "kPLTorchClassIsOneOf:"
- "kPLTorchClassOfDevice"
- "kPLWiFiClassIsOneOf:"
- "kPLWiFiClassOfDevice"
- "kPLXIsOneOf:firstArg:restOfArgs:"
- "kQueue"
- "kQueueBlock"
- "kRetry"
- "kSuccess"
- "kTimeout"
- "keyConfigsForEntryDefinition:"
- "keyConfigsForEntryKey:"
- "keyValuePathForKey:"
- "keybagFirstUnlockNotification"
- "keybagLockStatusNotification"
- "keys"
- "keysForSubKey:ofSubKeyType:"
- "kqueueDescriptorRef"
- "kqueueDescriptorSource"
- "lastArchivePath"
- "lastBatteryTimestampSystem"
- "lastCacheFlushDate"
- "lastCompletedDate"
- "lastCompletedDateWithIdentifier:"
- "lastEPSQLVacuumDate"
- "lastEntriesForKey:count:withFilters:"
- "lastEntryCache"
- "lastEntryCacheForEntryKey:"
- "lastEntryCacheForEntryKey:withSubEntryKey:"
- "lastEntryCachePruneToDate:"
- "lastEntryCacheSize"
- "lastEntryForKey:"
- "lastEntryForKey:withFilters:"
- "lastEntryForKey:withIDLessThan:"
- "lastEntryForKey:withSubEntryKey:"
- "lastKernelTimeRecalibrated"
- "lastLogDateForEntryKey"
- "lastObject"
- "lastPathComponent"
- "lastQueryTime"
- "lastSleepTime"
- "lastSubmissionDate"
- "lastSystemTimeRecalibrated"
- "lastValue"
- "lastXPCActivityTimestamp"
- "latency"
- "laterDate:"
- "launchDate"
- "launchdNameToProcessName:"
- "limitOfType:forEntryDefinition:"
- "limitOfType:forEntryKey:"
- "listenForNotifications:"
- "listeningForNotifications"
- "liteModeDaemonName"
- "liveModeQuery"
- "load"
- "loadArrayValuesIntoEntry:"
- "loadDynamicKeys"
- "loadDynamicValuesIntoEntry:"
- "localizedDescription"
- "lock"
- "log"
- "logAggregatedDataFromSignpostWithPayload:withStartDate:withEndDate:"
- "logAggregatedDataFromSignpostWithStartDate:withEndDate:"
- "logCreationEndDate"
- "logCreationResumeDate"
- "logCreationStartDate"
- "logDMAEntry:"
- "logEndDate"
- "logEndDateFromTable:"
- "logEntries:withGroupID:"
- "logEntry:"
- "logEventForwardConfiguration:"
- "logEventForwardSchemaChange:"
- "logEventForwardTaskingMode:"
- "logEventForwardTimeOffset:"
- "logEventNoneAdditionalTablesTurnedOn:"
- "logEventPointArchive:"
- "logEventPointCacheFlush:"
- "logEventPointOTA:"
- "logEventPointPLLog:"
- "logEventPointPreUnlock:"
- "logEventPointTimeCorrection:"
- "logForSubsystem:category:data:"
- "logForSubsystem:category:data:date:"
- "logFromCFCallback:"
- "logFullLastEntryCacheForEntryKey:"
- "logGenerationStats"
- "logHangSignposts:toDB:"
- "logMessage:fromFile:fromFunction:fromLineNumber:"
- "logModeForEntryKey:withKey:andValue:"
- "logOTAStatus:"
- "logPreUnlockState:"
- "logProportionateAggregateEntry:withStartDate:withEndDate:"
- "logRequestNotification:"
- "logSelectorStringForEnteryKey:"
- "logSelectorStringForEntryDefinition:"
- "logSignpostDataToDB:"
- "logSizeOfEntryCache:"
- "logSizeOfLastEntryCache"
- "logSizeOfStagingEntryCache"
- "logStagingEntryCacheForEntryKey:"
- "logStartDate"
- "logStartDateFromTable:"
- "logSubmissionResultToCAWithErrorType:withFileType:withOverrideKeys:"
- "logSubmissionSizeToAnalytics:withUncompressedSize:"
- "logSubmissionStateToAnalytics:"
- "logTaskingStatus:withAction:"
- "logTaskingStatus:withAction:withTables:"
- "logTaskingTablesTurnedOn:"
- "logTimeEntry"
- "logToCADataUploadState:"
- "logToCALogGenerationStats:"
- "longForKey:"
- "longForKey:ifNotSet:"
- "longLongValue"
- "longValue"
- "luxEntryNotificationWithOperator:withBlock:"
- "machTimeFromSeconds:"
- "mainDBSizeAtStart"
- "managedPrefsCache"
- "managedPrefsObjectForKey:forApplicationID:synchronize:"
- "manager"
- "manualSortOrderForEntryDefinition:"
- "manualSortOrderForEntryKey:"
- "markAsPurgeable:label:"
- "markAsPurgeable:urgency:startDate:"
- "markCompletedConfigUUID:errorOut:"
- "maskAssociatedPlugins:withMaskedDictionary:"
- "maskProcessName:withMaskedDictionary:"
- "masterTableForTable:andType:"
- "matchBlock"
- "matchingKeyToValue"
- "matchingPairs"
- "matchingPairs:"
- "matchingStringInArray:"
- "maxProcessCount"
- "md5Hash:"
- "mdLogCompressedFilePath"
- "mdLogFilePath"
- "mergeDataFromOtherDBFile:"
- "mergeNestedDictionary:withDict:"
- "mergePreUnlockDBFiles"
- "messageRecievedForClientID:withProcessName:withKey:withPayload:"
- "metadataStmt"
- "metadataStmtCreated"
- "methodForSelector:"
- "metricListener"
- "metricMessage:"
- "metricsForEntryKey:"
- "metricsToAddForStorage:processedMetrics:"
- "metricsToUpdateForStorage:processedMetrics:"
- "migrate"
- "migrateArchive:"
- "minTimeInterval"
- "minimumLiveOnTime"
- "minusSet:"
- "mobileUserADG"
- "modeForEntryKey:withKeyName:"
- "monitor"
- "monitorMetricsForSubsystem:category:payload:"
- "monitoredCategory"
- "monitoredSubsystem"
- "monotonicDate"
- "monotonicDateWithTimeIntervalSinceNow:"
- "monotonicFireDate"
- "monotonicResetOccurred"
- "moveDatabaseToPath:"
- "moveItemAtPath:toPath:error:"
- "moveItemAtPath:toPath:withName:error:"
- "movePowerlogs"
- "mssCompressedFilePath"
- "mssCycleInterval"
- "mssFilePath"
- "mssTextFilePath"
- "multiKeys"
- "mustRunCriterion"
- "mustRunCriterionSatisfied"
- "mustRunCriterionString"
- "mustRunInterval"
- "mutableCopy"
- "nearestDistanceFromDate:toRegionWithStartDate:andEndDate:"
- "nearestMidnightAfterDate:"
- "nearestMidnightBeforeDate:"
- "networkingEnergyWithBytes:withDuration:"
- "newOffsetEntryWithCurrentTime"
- "nextDateAfterDate:matchingComponents:options:"
- "nextObject"
- "nonUIBuild"
- "notification:"
- "notificationBlocks"
- "notificationName"
- "notificationNameForEntryKey:withFilterDefintion:"
- "notificationNames"
- "notificationRef"
- "notificationsToTimeReferences"
- "notifyExpired"
- "notifyTimeChange:"
- "now"
- "nsFromMachTime:"
- "null"
- "numAttempts"
- "numFilesAtPath:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLong:"
- "numberWithLongLong:"
- "numberWithShort:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLong:"
- "numberWithUnsignedLongLong:"
- "numberWithUnsignedShort:"
- "obfuscateTimestampsForTable:connection:withOffset:"
- "objCType"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectEnumerator"
- "objectExistsForKey:"
- "objectForCFString:"
- "objectForKey:"
- "objectForKey:forApplicationID:synchronize:"
- "objectForKey:ifNotSet:"
- "objectForKey:synchronize:"
- "objectForKeyedSubscript:"
- "objectForNullMarkerForKey:"
- "objectOrNullMarkerForCFString:"
- "objectsForSubKey:ofSubKeyType:"
- "offsetHistory"
- "offsetHistoryHead"
- "offsetTimestampsInDB:withConfig:withBaseTimestamp:"
- "oldFullMode"
- "onDemandTasking"
- "ondemand"
- "openCurrentFile"
- "openCurrentFileWithCacheSize:"
- "openCurrentFileWithCacheSize:withFlags:"
- "operatorBlock"
- "operatorClass"
- "operatorClassForEntryKey:"
- "operatorName"
- "operatorNameForEntryKey:"
- "operatorQueue"
- "operators"
- "otherAggregateKeys"
- "overridesEntryDateForEntryDefinition:"
- "overridesEntryDateForEntryKey:"
- "pUUIDForPid:"
- "pX2TxZTxWKS7QSXZDC/Z6A"
- "packageAllLogs"
- "packageDB:"
- "packageDirectory:to:"
- "parseIOReportSample"
- "parseSimpleDeltaSample"
- "passesIntegrityCheck"
- "pathExtension"
- "pathForResource:ofType:"
- "payloadDictionaryRepresentation"
- "peakPowerPressureLevel"
- "pendingDoneObjects"
- "pendingObjectsLock"
- "perModelTaskingTypeParameters"
- "percentTimeFilter"
- "perform"
- "performCopyTablesToDB:"
- "performQuery:"
- "performQuery:returnValue:returnResult:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performStatement:"
- "performSubmission"
- "performSubmission:"
- "periodicCurrentTime"
- "periodicIntegrityCheckInterval"
- "persistActivityState"
- "persistMetadata"
- "persistSubmissionInfo:"
- "pidForProcessName:"
- "plCompare:"
- "plTaskingTables"
- "pluggedInCriterion"
- "pluginsForBundleID:"
- "populateCPUTime"
- "populateIdentifiers:"
- "postEntries:"
- "postEntries:withGroupID:"
- "postFilteredNotificationForEntry:withFilteredDefition:withNotificationName:"
- "postNotificationName:object:"
- "postNotificationName:object:userInfo:"
- "powerModelForOperatorName:"
- "powerlogDefaultForKey:"
- "ppsTaskingTables"
- "predicateWithFormat:"
- "prepareAndEnqueueSubmissionFilesWithConfig:"
- "prepareDatabaseAtPath:"
- "prepareMSSLog"
- "preparePerfPowerlog:shouldDefer:"
- "preparedDynamicStatements"
- "preparedStatements"
- "preparedUpdateStatements"
- "previousIOReportSample"
- "printDBStatusString"
- "privacyClassification"
- "process:withReply:"
- "processEntriesForKey:withProperties:withBlock:"
- "processIDEntryForPid:"
- "processIdentifier"
- "processInfo"
- "processNameForBundleID:"
- "processNameForPid:"
- "processRbdc:withServiceType:"
- "processSignpostWithConfig:withServiceType:"
- "processThreadMap"
- "properties"
- "propertiesForKey:"
- "propertiesForKeys:"
- "propertiesFromIOEntry:"
- "propertiesFromIOEntry:forKey:"
- "pruneDB:withConfig:"
- "publicCloudDatabase"
- "q16@0:8"
- "q24@0:8@16"
- "q24@0:8i16i20"
- "q28@0:8@16s24"
- "q28@0:8q16i24"
- "q32@0:8@16@24"
- "q32@0:8@16@?24"
- "q32@0:8@16q24"
- "q44@0:8@16@24@32B40"
- "quarantineCopyResponder"
- "quarantineResponder"
- "quarantineToPath:action:"
- "quarantineWithExitReason:"
- "queue"
- "railDefinitions"
- "randomBoolWithYesPercentage:"
- "randomizedBaseOffset"
- "rangeOfString:"
- "rangeOfString:options:"
- "rbdcConverterProtocol"
- "readRawSignpostData:withReply:"
- "readTaskingDefaults"
- "readTaskingPayloadOverride:"
- "rebootOccurred"
- "receivedDate"
- "recover"
- "recoverCompress"
- "recoverCopy"
- "recoverSelectorForStage:"
- "recoverTrim"
- "refCount"
- "refreshBUI"
- "regBBWakeListener"
- "regBootStateListener"
- "regMetricListener"
- "regTriggerListener"
- "registerAppDeletionActivity"
- "registerDailyTasks"
- "registerDailyTasks_XPCActivity"
- "registerDataCollectionActivity"
- "registerEPLNotificationWithQueue:"
- "registerEntry:"
- "registerFilePermissionActivity"
- "registerForArchivingNotificationUsingBlock:"
- "registerForClockSetNotification"
- "registerForDayChangedNotification"
- "registerForListeners"
- "registerForStates:withOperator:withBlock:"
- "registerForTaskWithIdentifier:usingQueue:launchHandler:"
- "registerForTimeChangedCallbackWithIdentifier:forTimeReference:usingBlock:"
- "registerForTimeChangedCallbackWithIdentifier:usingBlock:"
- "registerForTimeChangedNotification"
- "registerForTimeZoneChangedNotification"
- "registerOperator:"
- "registerState:"
- "registerUploadSchedulingActivity"
- "registerUserSwitchStakeHolder:"
- "registeredOperators"
- "registeredOperatorsOfSuperClassType:"
- "rejectConfigUUID:errorOut:"
- "rejectTaskingConfig:"
- "rejectTaskingDRConfig"
- "relayActive"
- "relayConnection"
- "release"
- "remCapCE0"
- "remCapCE1"
- "remCapCE2"
- "remCapCE3"
- "remCapCE4"
- "remCapCE5"
- "remove:oldestFilesFromDirectory:containingFileNameSubstring:"
- "removeAdditionalFiles:"
- "removeAllObjects"
- "removeDBAtFilePath:"
- "removeDeviceConfig"
- "removeEntries"
- "removeErroneousQualificationEntries"
- "removeFileAtPath:"
- "removeFileAtURL:"
- "removeFirstPartyBundleIDPrefix:"
- "removeIDIndexes"
- "removeItemAtPath:error:"
- "removeItemAtURL:error:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObjectsForKeys:"
- "removeObjectsInArray:"
- "removeObserver:"
- "removeOldPowerlogFiles"
- "removeStorageForEntryKey:"
- "removeTableNameFromMergeDB:"
- "removeTimeOffsetFromReferenceTime:"
- "removed"
- "removedDate"
- "repeats"
- "reportEventToCA:didUpload:"
- "reportPerfStats"
- "reportZlibResultToCA:forEvent:"
- "req0"
- "req1"
- "req2"
- "request"
- "requestEntry"
- "requestEntryForEntryKey:forOperator:withTimeout:error:"
- "reschedule"
- "rescheduleDelay"
- "reset"
- "resetActivity"
- "resetCounter:"
- "resetMetricsForEntryKey:"
- "resetRelayConnection"
- "resetStateVariables"
- "resetTimestampFormaterTimezone"
- "resetUserDefaultCacheForKey:"
- "resetUserDefaultCacheForKey:forApplicationID:"
- "resolution"
- "respondToRequestForClientID:withProcessName:withKey:withPayload:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "reverseObjectEnumerator"
- "rootNodeEnergyRows"
- "roundDataInDB:withConfig:"
- "roundToSigFig:withSigFig:"
- "roundToSigFigDouble:withSigFig:"
- "rowCountForTable:"
- "rowCountForTableName:"
- "ruleIDToPendingJobs"
- "rules"
- "run"
- "runActivity"
- "runActivityWithLastCompletedDate:"
- "runArchiveJobs"
- "runInitialActivity"
- "runSelectorForStage:"
- "runTrimQuery:"
- "runningAsMobileUser"
- "runningAsUser"
- "s16@0:8"
- "s24@0:8@16"
- "s28@0:8@16B24"
- "s32@0:8@16@24"
- "s32@0:8@16d24"
- "s40@0:8@16@24@32"
- "safeCopyInProgress"
- "safeFileResponder"
- "sampleTime"
- "sampleTimePrevious"
- "sanitizeCAPayload:"
- "satisfied"
- "scaledPowerBasedOnPoint:withPowerModel:"
- "scanLocation"
- "scanUpToString:intoString:"
- "scannerWithString:"
- "schedule"
- "scheduleActivityWithIdentifier:withCriteria:withMustRunCriterion:withQueue:withInterruptBlock:withActivityBlock:"
- "scheduleArchiveJobs"
- "scheduleEntryListener"
- "scheduleIntegrityCheck"
- "scheduleSubmission"
- "scheduledTimerWithMonotonicFireDate:withInterval:withQueue:withBlock:"
- "schemaVersionForEntryDefinition:"
- "schemaVersionForEntryKey:"
- "schemaVersionForTable:"
- "secondsFromGMT"
- "secondsFromMachTime:"
- "seedBuild"
- "select:from:where:"
- "self"
- "sem"
- "sendBootStateChangInfoToLoggerUsing:"
- "sendMetricToLoggerUsing:"
- "sendSubmissionIssueSignature:"
- "sendTriggerToLoggerUsing:"
- "sendWakeInfoToLoggerUsing:"
- "serialize"
- "serialized"
- "serializedForJSON"
- "serializedJSONString"
- "serviceClassName"
- "serviceClients"
- "services"
- "servoCE0"
- "servoCE1"
- "servoCE2"
- "servoCE3"
- "servoCE4"
- "servoCE5"
- "servoCE6"
- "set"
- "setAbsoluteTimeFilter:"
- "setActivities:"
- "setActivityBlock:"
- "setActivityEntry:"
- "setAggregateFunction:"
- "setAggregateKey:"
- "setAggregateValue:"
- "setAllNullValuesForEntryKey:forKey:toValue:withFilters:"
- "setAllowlistResponder:"
- "setAllowsCellularAccess:"
- "setArchiveEntry:"
- "setArchiveJobs:"
- "setArchiveRetention:"
- "setArchivesResponder:"
- "setAttributes:ofItemAtPath:error:"
- "setBGSQLDBDuration:"
- "setBackgroundQueue:"
- "setBaseEntryKey:"
- "setBasebandTimeNotification:"
- "setBatteryUIPlistsResponder:"
- "setBgAudioTime:"
- "setBgEnergy:"
- "setBgLocationTime:"
- "setBgTime:"
- "setBlPathResponder:"
- "setBlobFailureReason:"
- "setBlock:"
- "setBlockingFlushCachesCFNotification:"
- "setBufferedEntries:"
- "setBuilds:"
- "setCESQLDBDuration:"
- "setCacheContent:"
- "setCacheSize:"
- "setCachedClassName:"
- "setCalendar:"
- "setCanceledFireDates:"
- "setCapSize:"
- "setCapValue:"
- "setCellIn:"
- "setCellOut:"
- "setCkFileDirPath:"
- "setCkTagConfig:"
- "setClass:debugEnabled:"
- "setClass:debugEnabled:forKey:"
- "setClassName:debugEnabled:"
- "setClassName:debugEnabled:forKey:"
- "setConfigDateApplied:"
- "setConfigDateReceived:"
- "setConfigUUID:"
- "setConn:"
- "setConnection:"
- "setConnectionByStorage:"
- "setConnectionToServer:"
- "setContextDictionary:"
- "setCountSafetyDrop:"
- "setCountWarnings:"
- "setCrashMoverQueue:"
- "setCriteria:"
- "setCriterionBlock:"
- "setCurrValue:"
- "setCurrentSnapshot:"
- "setDaFileDirPath:"
- "setDailyTaskNotification:"
- "setDailyTaskTimer:"
- "setDateFormat:"
- "setDay:"
- "setDayChangedNotification:"
- "setDbConnection:"
- "setDbSem:"
- "setDebugEnabled:"
- "setDefaultTaskingTypeParameters:"
- "setDelegate:"
- "setDeviceModel:"
- "setDice:"
- "setDictionary:"
- "setDirectory:"
- "setDiscretionaryNetworkBehavior:"
- "setDispatchQueue:"
- "setDrConfigMonitor:"
- "setDriverName:"
- "setDynamicObjectsFromRawData:"
- "setEPSQLDBDuration:"
- "setEPSQLVacuumInterval:"
- "setEnableDPUpload:"
- "setEnableRestartAtEPL:"
- "setEnabled:"
- "setEndDate:"
- "setEntryCacheStorageSize:"
- "setEntryDate:"
- "setEntryDefinition:"
- "setEntryDefinitionKey:"
- "setEntryID:"
- "setEntryKey:"
- "setEntryKeyToStateMap:"
- "setEntryKeysToSetup:"
- "setEntryListener:"
- "setEplEnabled:"
- "setEventSystemClient:"
- "setExecuteBlockCache:"
- "setExistsInDB:"
- "setExpirationHandler:"
- "setFailureReason:"
- "setFgEnergy:"
- "setFgTime:"
- "setFileDescriptor:"
- "setFileName:"
- "setFileNameWithSubmissionType:withID:"
- "setFilePath:"
- "setFileProtectionForPath:withLevel:"
- "setFileType:"
- "setFilter:"
- "setFilterDefinitions:"
- "setFilterDeltaLastEntryIDs:"
- "setFilterQuery:"
- "setFireDate:"
- "setFlatStorage:"
- "setFlushCachesCFNotification:"
- "setFlushCachesTimer:"
- "setFollowupCurrentTimeRunning:"
- "setGauge:withValue:"
- "setHashEntries:"
- "setHistogram:withValue:"
- "setHour:"
- "setHourBucketOffset:"
- "setICloudUploadEnabled:"
- "setInSubmission:"
- "setInstancePrefsCache:"
- "setInterestedObjects:"
- "setInternal:"
- "setInterruptBlock:"
- "setInterrupted:"
- "setInterruptionHandler:"
- "setInterval:"
- "setInvalidationHandler:"
- "setIoNotifyPort:"
- "setIoReportSample:"
- "setIsActive:"
- "setIsDRTasking:"
- "setIsDynamic:"
- "setIsEnergyTasking:"
- "setIsErrorEntry:"
- "setIsExpedited:"
- "setIsNamed:"
- "setIsStateRequired:"
- "setIssueCategory:"
- "setIssueDescription:"
- "setIterator:"
- "setJournalMode:"
- "setKQueue:"
- "setKQueueBlock:"
- "setKey:"
- "setKeybagFirstUnlockNotification:"
- "setKeybagLockStatusNotification:"
- "setKqueueDescriptorRef:"
- "setKqueueDescriptorSource:"
- "setLastBatteryTimestampSystem:"
- "setLastCacheFlushDate:"
- "setLastCompletedDate:"
- "setLastEPSQLVacuumDate:"
- "setLastEntryCache:"
- "setLastEntryCacheSize:"
- "setLastKernelTimeRecalibrated:"
- "setLastLogDateForEntryKey:"
- "setLastQueryTime:"
- "setLastSleepTime:"
- "setLastSystemTimeRecalibrated:"
- "setLastValue:"
- "setLastXPCActivityTimestamp:"
- "setLatency:"
- "setListeningForNotifications:"
- "setLocale:"
- "setLogCreationEndDate:"
- "setLogCreationResumeDate:"
- "setLogCreationStartDate"
- "setLogCreationStartDate:"
- "setMDLogCompressedFilePath"
- "setMDLogFilePath"
- "setMSSCompressedFilePath"
- "setMSSFilePath"
- "setMainDBSizeAtStart:"
- "setManagedPrefsCache:"
- "setManager:"
- "setMatchBlock:"
- "setMatchingKeyToValue:"
- "setMdLogCompressedFilePath:"
- "setMdLogFilePath:"
- "setMetadataStmt:"
- "setMetadataStmtCreated:"
- "setMetricListener:"
- "setMinute:"
- "setMobileOwnerForFile:"
- "setModifyRecordsCompletionBlock:"
- "setMonitor:"
- "setMonitoredCategory:"
- "setMonitoredSubsystem:"
- "setMonotonicFireDate:"
- "setMonotonicResetOccurred:"
- "setMonth:"
- "setMssCompressedFilePath:"
- "setMssCycleInterval:"
- "setMssFilePath:"
- "setMultiKeys:"
- "setMustRunCriterion:"
- "setMustRunInterval:"
- "setName:"
- "setNetworkUploadSize:"
- "setNextEntryIDForEntryKey:toEntryID:"
- "setNotificationBlocks:"
- "setNotificationName:"
- "setNotificationRef:"
- "setNotificationsToTimeReferences:"
- "setNumAttempts:"
- "setObject:atIndexedSubscript:"
- "setObject:forKey:"
- "setObject:forKey:forApplicationID:saveToDisk:"
- "setObject:forKey:saveToDisk:"
- "setObject:forKeyedSubscript:"
- "setObjectsFromData:"
- "setObjectsFromRawData:"
- "setObjectsUsingMetricsFromData:"
- "setOffset:"
- "setOffsetHistory:"
- "setOffsetHistoryHead:"
- "setOnDemandTasking:"
- "setOndemand:"
- "setOperator:"
- "setOperatorBlock:"
- "setOperatorQueue:"
- "setOperators:"
- "setOtherAggregateKeys:"
- "setPLSQLDBDuration:"
- "setPath:"
- "setPendingDoneObjects:"
- "setPendingObjectsLock:"
- "setPerModelTaskingTypeParameters:"
- "setPerRecordCompletionBlock:"
- "setPercentTimeFilter:"
- "setPeriodicCurrentTime:"
- "setPermissionsForFile:toValue:"
- "setPid:"
- "setPlTaskingTables:"
- "setPpsTaskingTables:"
- "setPreferAnonymousRequests:"
- "setPreparedDynamicStatements:"
- "setPreparedStatements:"
- "setPreparedUpdateStatements:"
- "setPreviousIOReportSample:"
- "setPriority:"
- "setProcessName:"
- "setProcessThreadMap:"
- "setProfileDefaultsKQueue:"
- "setQuarantineCopyResponder:"
- "setQuarantineResponder:"
- "setQueue:"
- "setRebootOccurred:"
- "setRecordType:"
- "setRefCount:"
- "setRelayActive:"
- "setRelayConnection:"
- "setRemoteObjectInterface:"
- "setRemoveEntries:"
- "setRemovedDate:"
- "setRepeats:"
- "setRequest:"
- "setRequiresExternalPower:"
- "setRequiresInexpensiveNetworkConnectivity:"
- "setRequiresNetworkConnectivity:"
- "setRequiresSignificantUserInactivity:"
- "setRescheduleDelay:"
- "setResourceIntensive:"
- "setResourceValue:forKey:error:"
- "setResources:"
- "setRootNodeEnergyRows:"
- "setRuleIDToPendingJobs:"
- "setRules:"
- "setSafeCopyInProgress:"
- "setSafeFileResponder:"
- "setSampleTime:"
- "setSampleTimePrevious:"
- "setSamplingPercentage:"
- "setSatisfied:"
- "setScanLocation:"
- "setScheduleAfter:"
- "setSchemaVersion:forTableName:"
- "setSecond:"
- "setSeed:"
- "setSem:"
- "setService:"
- "setServiceClassName:"
- "setServiceClients:"
- "setServiceName:"
- "setServices:"
- "setSignpostAllowlist:"
- "setSignpostDisable:"
- "setSleepEntryNotification:"
- "setSourceURL:"
- "setSqlStorage:"
- "setStage:"
- "setStagingAggregateEntryCache:"
- "setStagingEntryCache:"
- "setStagingEntryCacheSize:"
- "setStartArgs:"
- "setStartDate:"
- "setStartMonitor:"
- "setStartTime:"
- "setState:"
- "setStateChangeMask:"
- "setStateChangeNotifications:"
- "setStateChangeTime:"
- "setStateIDToStateMap:"
- "setStateToken:"
- "setStatement:"
- "setStopArgs:"
- "setStopMonitor:"
- "setStopTime:"
- "setStorageLocked:"
- "setStorageMap:"
- "setStorageOperator:"
- "setStorageReady:"
- "setStorageStarted:"
- "setSubmissionQueue:"
- "setSubmitReasonType:"
- "setSubmittedFilesMask:"
- "setSubscribedChannels:"
- "setSubscription:"
- "setSyncedOffDate:"
- "setSystemReboot:"
- "setSystemStateChangeTime:"
- "setSystemTime:"
- "setSystemTimeOffset:"
- "setTagConfig:"
- "setTagUUID:"
- "setTargetContainer:"
- "setTaskCompleted"
- "setTaskExpiredWithRetryAfter:error:"
- "setTaskingBuild:"
- "setTaskingConfig:"
- "setTaskingDeviceModels:"
- "setTaskingFiles:"
- "setTaskingMonitor:"
- "setTaskingPercentage:"
- "setTaskingPopulation:"
- "setTaskingRequestReason:"
- "setTaskingType:"
- "setThreadID:"
- "setThreadName:"
- "setThreadNameToInfo:"
- "setTime:"
- "setTimeChangeBlocks:"
- "setTimeIntervalRange:"
- "setTimeManager:"
- "setTimeReferenceType:"
- "setTimeReferences:"
- "setTimeZone:"
- "setTimeout:"
- "setTimer:"
- "setTimerActive:"
- "setTolerance:"
- "setTooFarInFutureDistance:"
- "setTooFarInPastDistance:"
- "setTotalSystemTime:"
- "setTotalUserTime:"
- "setTransactionInProgress:"
- "setTransactionLock:"
- "setTriggerBufferFlush:"
- "setTrimmingQueries:"
- "setTrySchedulingBefore:"
- "setType:"
- "setUpgradeLogsResponder:"
- "setUserInfo:"
- "setUserPrefsCache:"
- "setUserRequestTransaction:"
- "setUserTime:"
- "setUtilityQueue:"
- "setUuid:"
- "setValuesForKeysWithDictionary:"
- "setVersionHash:forTableName:"
- "setWakeEntryNotification:"
- "setWatchdog:"
- "setWifiIn:"
- "setWifiOut:"
- "setWildCardName:"
- "setWithArray:"
- "setWorkQueue:"
- "setWriteToDB:"
- "setXCSQLDBDuration:"
- "setXPCFlushCacheResponder:"
- "setXpcActivity:"
- "setXpcActivityDelay:"
- "setXpcActivityStarted:"
- "setXpcConnection:"
- "setXpcCrashMoverConn:"
- "setYear:"
- "setup"
- "setupArrayForTableName:forColumnNamed:withValueType:withShouldIndexFKID:"
- "setupArrayTableForEntryKey:withName:withConnection:"
- "setupCompositeIndexOnTable:withColumns:"
- "setupConnection"
- "setupCore"
- "setupDBConnectionAtPath:"
- "setupDBConnections"
- "setupDRTasking"
- "setupDynamicTableForEntryKey:withName:withConnection:"
- "setupEntryKeyForMetric:"
- "setupEntryObjects"
- "setupEntryObjectsAndStorage:"
- "setupEntryObjectsForOperatorClass:"
- "setupFilterRequest:"
- "setupFolders"
- "setupForPreUnlockTelemetry"
- "setupMetadataStorage"
- "setupStorage"
- "setupStorageForEntryKey:"
- "setupStorageForOperator:"
- "setupStorageForOperatorClass:"
- "setupStorageForOperatorName:"
- "setupStorageVersions"
- "setupTableForEntryKey:"
- "setupTableForEntryKey:withName:"
- "setupTableName:withEntryKeyConfig:withKeyOrder:isDynamic:withShouldIndexFKID:"
- "sharedABMClient"
- "sharedConnection"
- "sharedCore"
- "sharedCoreStarted"
- "sharedDefaults"
- "sharedFlatStorage"
- "sharedInstance"
- "sharedManager"
- "sharedSQLStorage"
- "sharedSQLiteConnection"
- "sharedScheduler"
- "sharedSemaphoreForKey:"
- "sharedStorageCache"
- "shortUUIDString"
- "shortValue"
- "shouldConfigureAdditionalTable:withType:withName:"
- "shouldConfigureTable:withType:withName:withConfigs:"
- "shouldCreateQuarantine"
- "shouldDoRapidCollection"
- "shouldGatherStatsForProcessName:"
- "shouldIncludeThread:withTotalSystemTime:withTotalUserTime:"
- "shouldLogForEntryKey:"
- "shouldLogForEntryKey:withKey:andValue:"
- "shouldLogMetric:"
- "shouldLogPreUnlockTelemetry"
- "shouldOverrideAllowlist:"
- "shouldQueryCurrentTime"
- "shouldSetupMetric:"
- "shouldShowBatteryGraphs"
- "shouldStartTaskingToday"
- "shouldSubmitToday"
- "shouldWriteEntry:withDebug:"
- "signal"
- "signalActive"
- "signalDoneByObject:"
- "signalInactive"
- "signalInterestByObject:"
- "signalNonInterestByObject:"
- "signalStartListening"
- "signatureWithDomain:type:subType:subtypeContext:detectedProcess:triggerThresholdValues:"
- "significantBatteryChangeNotificationWithOperator:withBlock:"
- "significantBatteryChangeNotificationWithOperator:withMaxIntervalInSecs:withBlock:"
- "signpostAllowlist"
- "signpostDisable"
- "sleepEntryNotification"
- "sleepEntryNotificationWithOperator:withBlock:"
- "smcPowerAccumulatedNotificationWithOperator:withBlock:"
- "smcThermalInstantNotificationWithOperator:withBlock:"
- "snapshotFromIOEntry:"
- "snapshotFromIOEntry:forKey:"
- "snapshotFromIOEntry:forKeys:"
- "snapshotWithSignature:duration:events:payload:actions:reply:"
- "sockaddrToNSDictionary:"
- "sortUsingComparator:"
- "sortedArrayUsingComparator:"
- "sortedArrayUsingSelector:"
- "sortedKeysFromEntryDefinition:"
- "sortedSqlFormatedColumnNamesForTableInsert:"
- "splitBySubmissionType"
- "sqlFormatedColumnNamesForTableInsert:"
- "sqlFormatedColumnNamesForTableSelect:withSystemOffset:"
- "sqlPropertiesAsString:"
- "sqlStorage"
- "sqlWhereClause"
- "stage"
- "stageCompress"
- "stageCopy"
- "stageRemove"
- "stageStart"
- "stageTrim"
- "stagingAggregateEntryCache"
- "stagingEntryCache"
- "stagingEntryCacheForEntryKey:"
- "stagingEntryCacheForEntryKey:withComparisons:isSingleton:"
- "stagingEntryCacheForEntryKey:withID:"
- "stagingEntryCacheForEntryKey:withIDLessThan:"
- "stagingEntryCacheIDsForEntryKey:"
- "stagingEntryCacheSize"
- "stagingEntryCacheSizeForEntryKey:"
- "startAccounting"
- "startAgents"
- "startAllStorage"
- "startArgs"
- "startCollection"
- "startCore"
- "startCoreForTest"
- "startHour"
- "startListening"
- "startMonitor"
- "startMonitoring"
- "startOperatorsOfSuperClassType:"
- "startPreUnlockServices"
- "startRelay"
- "startServices"
- "startServicesForPreUnlockTelemetry"
- "startStorage"
- "startWatchdog"
- "stateChangeMask"
- "stateChangeNotifications"
- "stateChangeTime"
- "stateChanged:"
- "stateIDToStateMap"
- "stateId"
- "stateToken"
- "statement"
- "staticArraySizeForKey:"
- "statsForFile:"
- "stopAccounting"
- "stopAgents"
- "stopArgs"
- "stopCore"
- "stopDRTasking"
- "stopDate"
- "stopHour"
- "stopMetricd"
- "stopMonitor"
- "stopMonitoring"
- "stopRelay"
- "stopServices"
- "stopTime"
- "stopWatchdog"
- "stopWatchdogForSubmissionActivity:"
- "storageClassForKey:"
- "storageClassForType:"
- "storageForConnection:"
- "storageForEntryKey:"
- "storageLocked"
- "storageMap"
- "storageOperator"
- "storageQueue"
- "storageQueueName"
- "storageQueueNameForClass:"
- "storageQueueNameForEntryKey:"
- "storageReady"
- "storageStarted"
- "string"
- "stringByAppendingFormat:"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringByDeletingLastPathComponent"
- "stringByDeletingPathExtension"
- "stringByReplacingCharactersInRange:withString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringByReplacingOccurrencesOfStrings:withString:"
- "stringByTrimmingCharactersInSet:"
- "stringForKey:"
- "stringFromDate:"
- "stringFromTrafficClass:"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "strip"
- "subEntryKey"
- "subEntryKeyKeyForEntryDefinition:"
- "subEntryKeyKeyForEntryKey:"
- "subarrayWithRange:"
- "submissionCategory"
- "submissionMaskToString"
- "submissionQueue"
- "submit:"
- "submitBDC"
- "submitBG"
- "submitCE"
- "submitFileStatsToAnalytics"
- "submitLogToDAWithBugType:"
- "submitLogToiCloud:WithCompress:"
- "submitLogToiCloudWithCompress:"
- "submitMSS"
- "submitPLL"
- "submitPLLUpgrade"
- "submitReasonForToday"
- "submitReasonType"
- "submitRecord:withActivity:"
- "submitRecordToDiagnosticPipeline:withConfig:"
- "submitSP"
- "submitSignpostDataWithConfig:withReply:"
- "submitTaskRequest:error:"
- "submitTaskingDefaultsCheckStateToCA:"
- "submitWithTaskingConfig:"
- "submitXC"
- "subpathsOfDirectoryAtPath:error:"
- "subscribeNotificationsForEntries"
- "subscribeToGroup:andSubGroup:"
- "subscribeToGroup:andSubGroup:withChannelIDs:"
- "subscribeToGroup:andSubGroup:withChannelIDs:manualChannelOnly:"
- "subscribedChannels"
- "subscription"
- "substringFromIndex:"
- "substringToIndex:"
- "substringWithRange:"
- "subsystemForEntryKey:"
- "subtractCounter:withValue:"
- "summarizeAggregateEntries:"
- "summarizeAggregateEntries:withPrimaryKeys:"
- "summarizeSignpostMetrics:withReply:"
- "superclass"
- "supplementalBuildVersion"
- "supportsEnhancedAPFS"
- "supportsPhysicalSim"
- "supportsSecureCoding"
- "supportsSlowCharging"
- "syncAndDispatchForEntryCache:forEntryKey:withBlock:"
- "syncWithDB"
- "syncedOff"
- "syncedOffDate"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "sysCap0"
- "sysCap1"
- "sysCap2"
- "systemStateChangeTime"
- "systemTime"
- "systemTimeChangedByOffset:"
- "systemTimeOffsetModified"
- "systemTimeZone"
- "tableCounts"
- "tableExistsForTableName:"
- "tableHasTimestampColumn"
- "tableHasTimestampColumn:"
- "tableHasTimestampColumnSem"
- "tableInfo:"
- "tablesToMigrateForCE"
- "tablesToTrimConditionsForTrimDate:"
- "targetContainer"
- "taskRequestForIdentifier:"
- "taskingBlobDRExists"
- "taskingBlobExists"
- "taskingBlobLegacyExists"
- "taskingBuild"
- "taskingCleanup"
- "taskingConfig"
- "taskingDeviceModels"
- "taskingFiles"
- "taskingModeSafeguard"
- "taskingModeSetup"
- "taskingMonitor"
- "taskingPercentage"
- "taskingPopulation"
- "taskingRequestReason"
- "taskingStarted"
- "taskingTables"
- "taskingType"
- "taskingTypeSpecified"
- "tcpParse:offset:"
- "teamID"
- "threadID"
- "threadName"
- "threadNameToInfo"
- "timeChangeBlocks"
- "timeChangedNotificationReceived:"
- "timeChangedToMidnightLocalTime"
- "timeCriterionWithInterval:"
- "timeIntervalRange"
- "timeIntervalRangeForEntryKey:"
- "timeIntervalSince1970"
- "timeIntervalSinceDate:"
- "timeIntervalSinceLastLogForEntryKey:"
- "timeIntervalSinceMonitonicNow"
- "timeIntervalSinceNow"
- "timeManager"
- "timeOffsetForTimeReference:"
- "timeReferenceType"
- "timeReferences"
- "timeToLiveForEntryKey:"
- "timeZoneChangedNotificationReceived:"
- "timeZoneHourBucketShift:"
- "timeZoneWithAbbreviation:"
- "timeintervalRangeEntryKeyForEntryKey:withTimeIntervalRange:"
- "timer"
- "timerActive"
- "timerFiredForMonotonicFireDate:"
- "todayRange"
- "tokenizedByString:"
- "tokenizedByStrings:"
- "tolerance"
- "tooFarInFutureDistance"
- "tooFarInPastDistance"
- "topAppsRunTime"
- "torchTypeString"
- "totalLogDuration"
- "totalLogDurationFromTable:where:"
- "totalSystemTime"
- "totalUserTime"
- "transactionInProgress"
- "transactionLock"
- "transactionWorkQueue"
- "traverseVersionDirectory:withBlock:"
- "triggerBlocks"
- "triggerBufferFlush"
- "triggerMessage:"
- "triggerPeriodicMetrics:andprofileId:"
- "trimAllTablesFromDate:toDate:"
- "trimAllTablesFromDate:toDate:withTableFilters:"
- "trimAndFilterDB:withConfig:"
- "trimBackgroundProcessingLog"
- "trimCleanEnergyLog"
- "trimConditionsForBGSQLWithTrimDate:"
- "trimConditionsForCESQLWithTrimDate:"
- "trimConditionsForEPSQLWithTrimDate:"
- "trimConditionsForEntryKey:forTrimDate:"
- "trimConditionsForEntryKey:trimDate:currDate:"
- "trimConditionsForPLSQLWithTrimDate:"
- "trimConditionsForStorage:trimDate:"
- "trimConditionsForTables:trimDate:"
- "trimConditionsForXCSQLWithTrimDate:"
- "trimConditionsWithEntryKey:withTrimDate:withCount:withStartDateKey:"
- "trimConditionsWithEntryKey:withTrimDate:withDuration:withStartDateKey:"
- "trimExtendedPersistenceLog"
- "trimTable:fromDate:withFilter:withTrimLimit:"
- "trimXcodeOrganizerLog"
- "truncateDB"
- "udpParse:offset:"
- "unarchivedObjectOfClass:fromData:error:"
- "undroopCE"
- "unionSet:"
- "unitForKey:"
- "unlock"
- "unregisterDataCollectionActivity"
- "unregisterForTimeChangedCallbackWithIdentifier:"
- "unregisterForTimeChangedCallbackWithIdentifier:forTimeReference:"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "updateDataStats:"
- "updateEntry:"
- "updateEntry:withBlock:"
- "updateMetadata:updateMetrics:addMetrics:"
- "updateQuery:"
- "updateStagingEntryCacheWithEntry:withBlock:"
- "updateStats"
- "updateStatsWithBlock:"
- "updateSubmissionTagWithConnection:"
- "updateTable:transferDataForKeys:"
- "updateTaskRequest:error:"
- "updateWithEntry:"
- "updateWithLastEntry"
- "updateWithValue:"
- "upgradeLogsResponder"
- "upload:"
- "uploadLog:"
- "uploadRange"
- "userActionCountForConnection:"
- "userDefaultsObjectForKey:forApplicationID:synchronize:"
- "userInfo"
- "userPrefsCache"
- "userRequestTransaction"
- "userTime"
- "utilityQueue"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8i16"
- "v20@0:8s16"
- "v24@0:8#16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"PLActivityCriterion\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\">16"
- "v24@0:8Q16"
- "v24@0:8^{IONotificationPort=}16"
- "v24@0:8^{__CFFileDescriptor=}16"
- "v24@0:8^{__CFRunLoopSource=}16"
- "v24@0:8^{__IOHIDEvent=}16"
- "v24@0:8^{__IOHIDEventSystemClient=}16"
- "v24@0:8^{__IOReportSubscriptionCF=}16"
- "v24@0:8^{sqlite3=}16"
- "v24@0:8^{sqlite3_stmt=}16"
- "v24@0:8d16"
- "v24@0:8i16i20"
- "v24@0:8q16"
- "v24@0:8s16s20"
- "v28@0:8#16B24"
- "v28@0:8@16B24"
- "v28@0:8@16S24"
- "v28@0:8@16i24"
- "v28@0:8@16s24"
- "v28@0:8Q16B24"
- "v28@0:8i16@20"
- "v28@0:8s16@20"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@\"PPSSignpostServiceRequest\"16@?<v@?B@\"NSDate\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8@16d24"
- "v32@0:8@16q24"
- "v32@0:8Q16Q24"
- "v32@0:8d16@24"
- "v32@0:8i16i20@24"
- "v32@0:8q16@\"PLArchiveEntry\"24"
- "v32@0:8q16@24"
- "v32@0:8{_PLTimeIntervalRange=dd}16"
- "v36@0:8#16B24@28"
- "v36@0:8@16@24B32"
- "v36@0:8@16B24@28"
- "v36@0:8@16d24s32"
- "v36@0:8i16@20@28"
- "v36@0:8s16@20@28"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@24d32"
- "v40@0:8@16@24s32B36"
- "v40@0:8@16q24@?32"
- "v40@0:8Q16@24@?32"
- "v40@0:8^@16^@24@32"
- "v40@0:8^@16^Q24^Q32"
- "v44@0:8@16@24@32B40"
- "v44@0:8s16@20@28@36"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32B40B44"
- "v48@0:8@16@24@32q40"
- "v48@0:8d16d24d32d40"
- "v56@0:8@16@24@32@40d48"
- "v64@0:8@16@24@32@40@?48@?56"
- "vacuum"
- "value:withObjCType:"
- "valueForKey:"
- "valueForKeyPath:"
- "valueForMobileGestaltCapability:"
- "values"
- "verifySchemaVersionOfTable:matchesExpectedVersion:"
- "versionForTable:"
- "versionHashForTable:"
- "waitUntilDate:"
- "waitWithBlock:"
- "waitWithBlockSync:"
- "wakeEntryNotification"
- "wakeEntryNotificationWithOperator:withBlock:"
- "wakeEntryNotificationWithWorkQueue:withBlock:"
- "wakeMessage:"
- "watchdog"
- "whitespaceAndNewlineCharacterSet"
- "wifiIn"
- "wifiOut"
- "wildCardForEntryKey:"
- "wildCardName"
- "willSwitchUser"
- "workQueue"
- "workQueueForClass:"
- "workQueueForKey:"
- "wrapDeviceArgumentsInArray:"
- "writeAggregateEntry:"
- "writeArrayEntries:"
- "writeDynamicEntries:"
- "writeDynamicEntriesToPPS:"
- "writeEntries:withCompletionBlock:"
- "writeEntry:"
- "writeEntry:withCompletionBlock:"
- "writeMetadata:forFKID:build:name:version:"
- "writeOffsetToDefaults"
- "writeProportionateAggregateEntry:withStartDate:withEndDate:"
- "writeToDB"
- "writeToFile:atomically:"
- "writeToFile:atomically:encoding:error:"
- "writeToURL:error:"
- "xcodeVersionFromUserActions"
- "xpcActivityDelay"
- "xpcActivityStarted"
- "xpcConnection"
- "xpcCrashMoverConn"
- "xpcServiceIdentifier"
- "zeroSumCE"
- "{_PLTimeIntervalRange=\"location\"d\"length\"d}"
- "{_PLTimeIntervalRange=dd}16@0:8"
- "{_PLTimeIntervalRange=dd}24@0:8@16"
- "{apfs_label_purgeable_request=QQQQQQ}32@0:8Q16@24"
- "{jetsam_priority_info=iBq}20@0:8i16"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{process_memory_limit_info=iBBB}20@0:8i16"
- "{shared_ptr<abm::client::Manager>=\"__ptr_\"^{Manager}\"__cntrl_\"^{__shared_weak_count}}"

```
