## MetricKit

> `/System/Library/Frameworks/MetricKit.framework/MetricKit`

```diff

-297.120.4.0.0
-  __TEXT.__text: 0x134d0
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_methlist: 0x1c08
-  __TEXT.__const: 0x198
-  __TEXT.__cstring: 0xf3e
-  __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__oslogstring: 0x21e
-  __TEXT.__swift5_typeref: 0x5f
-  __TEXT.__swift5_reflstr: 0x9
-  __TEXT.__swift5_assocty: 0x18
-  __TEXT.__constg_swiftt: 0x54
-  __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_proto: 0xc
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x558
-  __TEXT.__objc_classname: 0x360
-  __TEXT.__objc_methname: 0x53df
-  __TEXT.__objc_methtype: 0x654
-  __TEXT.__objc_stubs: 0x1120
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0x100
-  __DATA_CONST.__objc_classlist: 0x140
+353.0.0.0.0
+  __TEXT.__text: 0x7c7e0
+  __TEXT.__objc_methlist: 0x286c
+  __TEXT.__const: 0x8f06
+  __TEXT.__cstring: 0x1e92
+  __TEXT.__gcc_except_tab: 0x18
+  __TEXT.__oslogstring: 0x349
+  __TEXT.__swift5_typeref: 0x18b4
+  __TEXT.__swift5_reflstr: 0x11b1
+  __TEXT.__swift5_assocty: 0x4c8
+  __TEXT.__constg_swiftt: 0x145c
+  __TEXT.__swift5_fieldmd: 0x1c88
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_proto: 0x8dc
+  __TEXT.__swift5_types: 0x21c
+  __TEXT.__swift_as_entry: 0x4
+  __TEXT.__swift_as_ret: 0x4
+  __TEXT.__swift_as_cont: 0xc
+  __TEXT.__unwind_info: 0x23c0
+  __TEXT.__eh_frame: 0x2838
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x108
+  __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc38
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x128
-  __AUTH_CONST.__auth_got: 0x3a0
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x14a0
-  __AUTH_CONST.__objc_const: 0x44e8
-  __AUTH.__objc_data: 0x100
-  __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x2ac
-  __DATA.__data: 0x1d0
-  __DATA.__common: 0x18
-  __DATA.__bss: 0x1e0
-  __DATA_DIRTY.__objc_data: 0xbe0
+  __DATA_CONST.__objc_selrefs: 0x1220
+  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x178
+  __DATA_CONST.__got: 0x488
+  __AUTH_CONST.__const: 0x4779
+  __AUTH_CONST.__cfstring: 0x1b20
+  __AUTH_CONST.__objc_const: 0x66b8
+  __AUTH_CONST.__auth_got: 0x9e8
+  __AUTH.__objc_data: 0x3d8
+  __AUTH.__data: 0x13b0
+  __DATA.__objc_ivar: 0x428
+  __DATA.__data: 0x12d0
+  __DATA.__bss: 0x12dc0
+  __DATA.__common: 0x58
+  __DATA_DIRTY.__objc_data: 0xeb0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/StateReporting.framework/StateReporting
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/SignpostMetrics.framework/SignpostMetrics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libapp_launch_measurement.dylib

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: DB89FAE5-7250-30B2-9100-61FF7B88AF80
-  Functions: 597
-  Symbols:   1986
-  CStrings:  1177
+  UUID: E92D872D-D801-3251-816B-92521C199065
+  Functions: 3322
+  Symbols:   3727
+  CStrings:  566
 
Symbols:
+ +[MXCallStackArray supportsSecureCoding]
+ +[MXCrashDiagnostic _resolveTerminationCategoryWithSignal:terminationReason:]
+ +[MXDiagnosticEnvironment supportsSecureCoding]
+ +[MXFlatFrameData supportsSecureCoding]
+ +[MXIntervalMetricData intervalMetricDataWithDictionary:]
+ +[MXIntervalMetricData supportsSecureCoding]
+ +[MXMemoryExceptionDiagnosticContainer supportsSecureCoding]
+ +[MXMetalFrameRateMetric metricsFromDictionaryArray:]
+ +[MXMetalFrameRateMetric supportsSecureCoding]
+ +[MXMetricManager stateAwareSharedManager]
+ +[MXReportedState reportedStateWithDictionary:]
+ +[MXReportedState supportsSecureCoding]
+ +[MXStateMetricData stateMetricDataWithDictionary:]
+ +[MXStateMetricData supportsSecureCoding]
+ +[MXThreadMetadata supportsSecureCoding]
+ -[MXAnimationMetric initWithHitchTimeRatio:perceivedHitchTimeRatio:totalScrollHitchTime:totalScrollTime:totalHitchTime:totalAnimationTime:]
+ -[MXAnimationMetric totalAnimationTime]
+ -[MXAnimationMetric totalHitchTime]
+ -[MXAnimationMetric totalScrollHitchTime]
+ -[MXAnimationMetric totalScrollTime]
+ -[MXAppLaunchDiagnostic initWithMetaData:applicationVersion:signpostData:reportedStateData:pid:callStack:launchDuration:]
+ -[MXCPUExceptionDiagnostic initWithMetaData:applicationVersion:signpostData:reportedStateData:pid:callStack:totalCpuTime:totalSampledTime:]
+ -[MXCallStackArray .cxx_destruct]
+ -[MXCallStackArray callStackPerThread]
+ -[MXCallStackArray encodeWithCoder:]
+ -[MXCallStackArray flatFrames]
+ -[MXCallStackArray initWithCoder:]
+ -[MXCallStackArray initWithFlatFrames:threadMetadata:callStackPerThread:]
+ -[MXCallStackArray setCallStackPerThread:]
+ -[MXCallStackArray setFlatFrames:]
+ -[MXCallStackArray setThreadMetadata:]
+ -[MXCallStackArray threadMetadata]
+ -[MXCallStackArrayBuilder .cxx_destruct]
+ -[MXCallStackArrayBuilder addFrameWithBinaryName:binaryUUID:address:offsetIntoBinaryTextSegment:sampleCount:isRoot:]
+ -[MXCallStackArrayBuilder beginThreadWithThreadAttributed:]
+ -[MXCallStackArrayBuilder buildWithCallStackPerThread:]
+ -[MXCallStackArrayBuilder init]
+ -[MXCallStackArrayBuilder setParent:forChild:]
+ -[MXCrashDiagnostic initWithMetaData:applicationVersion:signpostData:reportedStateData:pid:terminationReason:applicationSpecificInfo:virtualMemoryRegionInfo:exceptionType:exceptionCode:exceptionReason:signal:stackTrace:]
+ -[MXCrashDiagnostic terminationCategory]
+ -[MXDiagnostic initWithMetaData:applicationVersion:signpostData:reportedStateData:andPID:]
+ -[MXDiagnostic reportedStateData]
+ -[MXDiagnostic setReportedStateData:]
+ -[MXDiagnosticEnvironment .cxx_destruct]
+ -[MXDiagnosticEnvironment applicationBuildVersion]
+ -[MXDiagnosticEnvironment applicationVersion]
+ -[MXDiagnosticEnvironment bundleIdentifier]
+ -[MXDiagnosticEnvironment deviceType]
+ -[MXDiagnosticEnvironment encodeWithCoder:]
+ -[MXDiagnosticEnvironment initWithBundleIdentifier:applicationVersion:applicationBuildVersion:pid:osVersion:deviceType:signpostData:regionFormat:platformArchitecture:lowPowerModeEnabled:isTestFlightApp:]
+ -[MXDiagnosticEnvironment initWithBundleIdentifier:applicationVersion:applicationBuildVersion:pid:osVersion:deviceType:signpostData:reportedStateData:regionFormat:platformArchitecture:lowPowerModeEnabled:isTestFlightApp:]
+ -[MXDiagnosticEnvironment initWithCoder:]
+ -[MXDiagnosticEnvironment isTestFlightApp]
+ -[MXDiagnosticEnvironment lowPowerModeEnabled]
+ -[MXDiagnosticEnvironment osBuildNumber]
+ -[MXDiagnosticEnvironment osPlatform]
+ -[MXDiagnosticEnvironment osVersionNumber]
+ -[MXDiagnosticEnvironment osVersion]
+ -[MXDiagnosticEnvironment pid]
+ -[MXDiagnosticEnvironment platformArchitecture]
+ -[MXDiagnosticEnvironment regionFormat]
+ -[MXDiagnosticEnvironment reportedStateData]
+ -[MXDiagnosticEnvironment setApplicationBuildVersion:]
+ -[MXDiagnosticEnvironment setApplicationVersion:]
+ -[MXDiagnosticEnvironment setBundleIdentifier:]
+ -[MXDiagnosticEnvironment setDeviceType:]
+ -[MXDiagnosticEnvironment setIsTestFlightApp:]
+ -[MXDiagnosticEnvironment setLowPowerModeEnabled:]
+ -[MXDiagnosticEnvironment setOsBuildNumber:]
+ -[MXDiagnosticEnvironment setOsPlatform:]
+ -[MXDiagnosticEnvironment setOsVersion:]
+ -[MXDiagnosticEnvironment setOsVersionNumber:]
+ -[MXDiagnosticEnvironment setPid:]
+ -[MXDiagnosticEnvironment setPlatformArchitecture:]
+ -[MXDiagnosticEnvironment setRegionFormat:]
+ -[MXDiagnosticEnvironment setReportedStateData:]
+ -[MXDiagnosticEnvironment setSignpostData:]
+ -[MXDiagnosticEnvironment signpostData]
+ -[MXDiagnosticPayload initWithStartDate:endDate:diagnosticContainers:]
+ -[MXDiagnosticPayload initWithStartDate:endDate:diagnostics:]
+ -[MXDiagnosticPayload initWithStartDate:endDate:diagnostics:diagnosticContainers:]
+ -[MXDiagnosticPayload memoryExceptionDiagnosticContainers]
+ -[MXDiagnosticPayload setMemoryExceptionDiagnosticContainers:]
+ -[MXDiskWriteExceptionDiagnostic initWithMetaData:applicationVersion:signpostData:reportedStateData:pid:totalWritesCaused:stackTrace:]
+ -[MXFlatFrameData .cxx_destruct]
+ -[MXFlatFrameData address]
+ -[MXFlatFrameData binaryName]
+ -[MXFlatFrameData binaryUUID]
+ -[MXFlatFrameData childIndices]
+ -[MXFlatFrameData encodeWithCoder:]
+ -[MXFlatFrameData initWithBinaryName:binaryUUID:address:offsetIntoBinaryTextSegment:sampleCount:parentIndex:childIndices:threadIndex:]
+ -[MXFlatFrameData initWithCoder:]
+ -[MXFlatFrameData offsetIntoBinaryTextSegment]
+ -[MXFlatFrameData parentIndex]
+ -[MXFlatFrameData sampleCount]
+ -[MXFlatFrameData setAddress:]
+ -[MXFlatFrameData setBinaryName:]
+ -[MXFlatFrameData setBinaryUUID:]
+ -[MXFlatFrameData setChildIndices:]
+ -[MXFlatFrameData setOffsetIntoBinaryTextSegment:]
+ -[MXFlatFrameData setParentIndex:]
+ -[MXFlatFrameData setSampleCount:]
+ -[MXFlatFrameData setThreadIndex:]
+ -[MXFlatFrameData threadIndex]
+ -[MXHangDiagnostic initWithMetaData:applicationVersion:signpostData:reportedStateData:pid:callStack:hangDuration:hangType:]
+ -[MXIntervalMetricData .cxx_destruct]
+ -[MXIntervalMetricData activeStates]
+ -[MXIntervalMetricData animationMetrics]
+ -[MXIntervalMetricData applicationExitMetrics]
+ -[MXIntervalMetricData applicationLaunchMetrics]
+ -[MXIntervalMetricData applicationResponsivenessMetrics]
+ -[MXIntervalMetricData applicationTimeMetrics]
+ -[MXIntervalMetricData cellularConditionMetrics]
+ -[MXIntervalMetricData copyWithZone:]
+ -[MXIntervalMetricData cpuMetrics]
+ -[MXIntervalMetricData diskIOMetrics]
+ -[MXIntervalMetricData displayMetrics]
+ -[MXIntervalMetricData durationSeconds]
+ -[MXIntervalMetricData encodeWithCoder:]
+ -[MXIntervalMetricData endTimestamp]
+ -[MXIntervalMetricData gpuMetrics]
+ -[MXIntervalMetricData initWithCoder:]
+ -[MXIntervalMetricData initWithStartTimestamp:endTimestamp:durationSeconds:cpuMetrics:gpuMetrics:applicationTimeMetrics:locationActivityMetrics:networkTransferMetrics:diskIOMetrics:memoryMetrics:displayMetrics:cellularConditionMetrics:applicationLaunchMetrics:applicationResponsivenessMetrics:animationMetrics:applicationExitMetrics:signpostMetrics:metalFrameRateMetrics:activeStates:]
+ -[MXIntervalMetricData locationActivityMetrics]
+ -[MXIntervalMetricData memoryMetrics]
+ -[MXIntervalMetricData metalFrameRateMetrics]
+ -[MXIntervalMetricData networkTransferMetrics]
+ -[MXIntervalMetricData signpostMetrics]
+ -[MXIntervalMetricData startTimestamp]
+ -[MXIntervalMetricData toDictionary]
+ -[MXMemoryExceptionDiagnosticContainer .cxx_destruct]
+ -[MXMemoryExceptionDiagnosticContainer callStackArray]
+ -[MXMemoryExceptionDiagnosticContainer encodeWithCoder:]
+ -[MXMemoryExceptionDiagnosticContainer environment]
+ -[MXMemoryExceptionDiagnosticContainer initWithCoder:]
+ -[MXMemoryExceptionDiagnosticContainer initWithEnvironment:callStackArray:timestamp:]
+ -[MXMemoryExceptionDiagnosticContainer setCallStackArray:]
+ -[MXMemoryExceptionDiagnosticContainer setEnvironment:]
+ -[MXMemoryExceptionDiagnosticContainer setTimestamp:]
+ -[MXMemoryExceptionDiagnosticContainer timestamp]
+ -[MXMetaData osBuildNumber]
+ -[MXMetaData osPlatform]
+ -[MXMetaData osVersionNumber]
+ -[MXMetaData setOsBuildNumber:]
+ -[MXMetaData setOsPlatform:]
+ -[MXMetaData setOsVersionNumber:]
+ -[MXMetalFrameRateMetric .cxx_destruct]
+ -[MXMetalFrameRateMetric activeDrawingDuration]
+ -[MXMetalFrameRateMetric averageFrameRate]
+ -[MXMetalFrameRateMetric encodeWithCoder:]
+ -[MXMetalFrameRateMetric frameCount]
+ -[MXMetalFrameRateMetric initWithCoder:]
+ -[MXMetalFrameRateMetric initWithLayerName:frameCount:activeDrawingDuration:averageFrameRate:]
+ -[MXMetalFrameRateMetric layerName]
+ -[MXMetalFrameRateMetric toDictionary]
+ -[MXMetricManager _updateStateReportingDomainsViaXPC:]
+ -[MXMetricManager _updateStateReportingDomainsViaXPC:].cold.1
+ -[MXMetricManager _updateStateReportingDomainsViaXPC:].cold.2
+ -[MXMetricManager addStateReportingDomains:]
+ -[MXMetricManager domainSubscriberCounts]
+ -[MXMetricManager initWithStateAware:]
+ -[MXMetricManager initWithStateAware:].cold.1
+ -[MXMetricManager initWithStateAware:].cold.2
+ -[MXMetricManager initWithStateAware:].cold.3
+ -[MXMetricManager initWithStateAware:].cold.4
+ -[MXMetricManager removeStateReportingDomains:]
+ -[MXMetricManager setDomainSubscriberCounts:]
+ -[MXMetricPayload intervalMetrics]
+ -[MXMetricPayload metalFrameRateMetrics]
+ -[MXMetricPayload setIntervalMetrics:]
+ -[MXMetricPayload setMetalFrameRateMetrics:]
+ -[MXMetricPayload setStateMetrics:]
+ -[MXMetricPayload stateMetrics]
+ -[MXReportedState .cxx_destruct]
+ -[MXReportedState copyWithZone:]
+ -[MXReportedState domain]
+ -[MXReportedState durationSeconds]
+ -[MXReportedState encodeWithCoder:]
+ -[MXReportedState initWithCoder:]
+ -[MXReportedState initWithDomain:label:stableContext:durationSeconds:]
+ -[MXReportedState label]
+ -[MXReportedState stableContext]
+ -[MXReportedState toDictionary]
+ -[MXStateMetricData .cxx_destruct]
+ -[MXStateMetricData animationMetrics]
+ -[MXStateMetricData applicationExitMetrics]
+ -[MXStateMetricData applicationLaunchMetrics]
+ -[MXStateMetricData applicationResponsivenessMetrics]
+ -[MXStateMetricData applicationTimeMetrics]
+ -[MXStateMetricData cellularConditionMetrics]
+ -[MXStateMetricData copyWithZone:]
+ -[MXStateMetricData cpuMetrics]
+ -[MXStateMetricData diskIOMetrics]
+ -[MXStateMetricData displayMetrics]
+ -[MXStateMetricData durationSeconds]
+ -[MXStateMetricData encodeWithCoder:]
+ -[MXStateMetricData gpuMetrics]
+ -[MXStateMetricData initWithCoder:]
+ -[MXStateMetricData initWithReportedState:durationSeconds:cpuMetrics:gpuMetrics:applicationTimeMetrics:locationActivityMetrics:networkTransferMetrics:diskIOMetrics:memoryMetrics:displayMetrics:cellularConditionMetrics:applicationLaunchMetrics:applicationResponsivenessMetrics:animationMetrics:applicationExitMetrics:signpostMetrics:metalFrameRateMetrics:]
+ -[MXStateMetricData locationActivityMetrics]
+ -[MXStateMetricData memoryMetrics]
+ -[MXStateMetricData metalFrameRateMetrics]
+ -[MXStateMetricData networkTransferMetrics]
+ -[MXStateMetricData reportedState]
+ -[MXStateMetricData signpostMetrics]
+ -[MXStateMetricData toDictionary]
+ -[MXThreadMetadata .cxx_destruct]
+ -[MXThreadMetadata encodeWithCoder:]
+ -[MXThreadMetadata initWithCoder:]
+ -[MXThreadMetadata initWithThreadAttributed:rootFrameIndices:]
+ -[MXThreadMetadata rootFrameIndices]
+ -[MXThreadMetadata setRootFrameIndices:]
+ -[MXThreadMetadata setThreadAttributed:]
+ -[MXThreadMetadata threadAttributed]
+ GCC_except_table1
+ _OBJC_CLASS_$_MXCallStackArray
+ _OBJC_CLASS_$_MXCallStackArrayBuilder
+ _OBJC_CLASS_$_MXDiagnosticEnvironment
+ _OBJC_CLASS_$_MXFlatFrameData
+ _OBJC_CLASS_$_MXIntervalMetricData
+ _OBJC_CLASS_$_MXMemoryExceptionDiagnosticContainer
+ _OBJC_CLASS_$_MXMetalFrameRateMetric
+ _OBJC_CLASS_$_MXReportedState
+ _OBJC_CLASS_$_MXStateMetricData
+ _OBJC_CLASS_$_MXThreadMetadata
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_CLASS_$_NSScanner
+ _OBJC_CLASS_$_NSUnitFrequency
+ _OBJC_CLASS_$__TtC9MetricKit10SignalBars
+ _OBJC_CLASS_$__TtC9MetricKit21AveragePixelLuminance
+ _OBJC_CLASS_$__TtC9MetricKit25MetricManagerSubscription
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_MXAnimationMetric._totalAnimationTime
+ _OBJC_IVAR_$_MXAnimationMetric._totalHitchTime
+ _OBJC_IVAR_$_MXAnimationMetric._totalScrollHitchTime
+ _OBJC_IVAR_$_MXAnimationMetric._totalScrollTime
+ _OBJC_IVAR_$_MXCallStackArray._callStackPerThread
+ _OBJC_IVAR_$_MXCallStackArray._flatFrames
+ _OBJC_IVAR_$_MXCallStackArray._threadMetadata
+ _OBJC_IVAR_$_MXCallStackArrayBuilder._currentThreadAttributed
+ _OBJC_IVAR_$_MXCallStackArrayBuilder._currentThreadIndex
+ _OBJC_IVAR_$_MXCallStackArrayBuilder._currentThreadRootIndices
+ _OBJC_IVAR_$_MXCallStackArrayBuilder._flatFrames
+ _OBJC_IVAR_$_MXCallStackArrayBuilder._hasStartedThread
+ _OBJC_IVAR_$_MXCallStackArrayBuilder._threadMetadata
+ _OBJC_IVAR_$_MXCrashDiagnostic._terminationCategory
+ _OBJC_IVAR_$_MXDiagnostic._reportedStateData
+ _OBJC_IVAR_$_MXDiagnosticEnvironment._applicationBuildVersion
+ _OBJC_IVAR_$_MXDiagnosticEnvironment._applicationVersion
+ _OBJC_IVAR_$_MXDiagnosticEnvironment._bundleIdentifier
+ _OBJC_IVAR_$_MXDiagnosticEnvironment._deviceType
+ _OBJC_IVAR_$_MXDiagnosticEnvironment._isTestFlightApp
+ _OBJC_IVAR_$_MXDiagnosticEnvironment._lowPowerModeEnabled
+ _OBJC_IVAR_$_MXDiagnosticEnvironment._osBuildNumber
+ _OBJC_IVAR_$_MXDiagnosticEnvironment._osPlatform
+ _OBJC_IVAR_$_MXDiagnosticEnvironment._osVersion
+ _OBJC_IVAR_$_MXDiagnosticEnvironment._osVersionNumber
+ _OBJC_IVAR_$_MXDiagnosticEnvironment._pid
+ _OBJC_IVAR_$_MXDiagnosticEnvironment._platformArchitecture
+ _OBJC_IVAR_$_MXDiagnosticEnvironment._regionFormat
+ _OBJC_IVAR_$_MXDiagnosticEnvironment._reportedStateData
+ _OBJC_IVAR_$_MXDiagnosticEnvironment._signpostData
+ _OBJC_IVAR_$_MXDiagnosticPayload._memoryExceptionDiagnosticContainers
+ _OBJC_IVAR_$_MXFlatFrameData._address
+ _OBJC_IVAR_$_MXFlatFrameData._binaryName
+ _OBJC_IVAR_$_MXFlatFrameData._binaryUUID
+ _OBJC_IVAR_$_MXFlatFrameData._childIndices
+ _OBJC_IVAR_$_MXFlatFrameData._offsetIntoBinaryTextSegment
+ _OBJC_IVAR_$_MXFlatFrameData._parentIndex
+ _OBJC_IVAR_$_MXFlatFrameData._sampleCount
+ _OBJC_IVAR_$_MXFlatFrameData._threadIndex
+ _OBJC_IVAR_$_MXIntervalMetricData._activeStates
+ _OBJC_IVAR_$_MXIntervalMetricData._animationMetrics
+ _OBJC_IVAR_$_MXIntervalMetricData._applicationExitMetrics
+ _OBJC_IVAR_$_MXIntervalMetricData._applicationLaunchMetrics
+ _OBJC_IVAR_$_MXIntervalMetricData._applicationResponsivenessMetrics
+ _OBJC_IVAR_$_MXIntervalMetricData._applicationTimeMetrics
+ _OBJC_IVAR_$_MXIntervalMetricData._cellularConditionMetrics
+ _OBJC_IVAR_$_MXIntervalMetricData._cpuMetrics
+ _OBJC_IVAR_$_MXIntervalMetricData._diskIOMetrics
+ _OBJC_IVAR_$_MXIntervalMetricData._displayMetrics
+ _OBJC_IVAR_$_MXIntervalMetricData._durationSeconds
+ _OBJC_IVAR_$_MXIntervalMetricData._endTimestamp
+ _OBJC_IVAR_$_MXIntervalMetricData._gpuMetrics
+ _OBJC_IVAR_$_MXIntervalMetricData._locationActivityMetrics
+ _OBJC_IVAR_$_MXIntervalMetricData._memoryMetrics
+ _OBJC_IVAR_$_MXIntervalMetricData._metalFrameRateMetrics
+ _OBJC_IVAR_$_MXIntervalMetricData._networkTransferMetrics
+ _OBJC_IVAR_$_MXIntervalMetricData._signpostMetrics
+ _OBJC_IVAR_$_MXIntervalMetricData._startTimestamp
+ _OBJC_IVAR_$_MXMemoryExceptionDiagnosticContainer._callStackArray
+ _OBJC_IVAR_$_MXMemoryExceptionDiagnosticContainer._environment
+ _OBJC_IVAR_$_MXMemoryExceptionDiagnosticContainer._timestamp
+ _OBJC_IVAR_$_MXMetaData._osBuildNumber
+ _OBJC_IVAR_$_MXMetaData._osPlatform
+ _OBJC_IVAR_$_MXMetaData._osVersionNumber
+ _OBJC_IVAR_$_MXMetalFrameRateMetric._activeDrawingDuration
+ _OBJC_IVAR_$_MXMetalFrameRateMetric._averageFrameRate
+ _OBJC_IVAR_$_MXMetalFrameRateMetric._frameCount
+ _OBJC_IVAR_$_MXMetalFrameRateMetric._layerName
+ _OBJC_IVAR_$_MXMetricManager._domainSubscriberCounts
+ _OBJC_IVAR_$_MXMetricPayload._intervalMetrics
+ _OBJC_IVAR_$_MXMetricPayload._metalFrameRateMetrics
+ _OBJC_IVAR_$_MXMetricPayload._stateMetrics
+ _OBJC_IVAR_$_MXReportedState._domain
+ _OBJC_IVAR_$_MXReportedState._durationSeconds
+ _OBJC_IVAR_$_MXReportedState._label
+ _OBJC_IVAR_$_MXReportedState._stableContext
+ _OBJC_IVAR_$_MXStateMetricData._animationMetrics
+ _OBJC_IVAR_$_MXStateMetricData._applicationExitMetrics
+ _OBJC_IVAR_$_MXStateMetricData._applicationLaunchMetrics
+ _OBJC_IVAR_$_MXStateMetricData._applicationResponsivenessMetrics
+ _OBJC_IVAR_$_MXStateMetricData._applicationTimeMetrics
+ _OBJC_IVAR_$_MXStateMetricData._cellularConditionMetrics
+ _OBJC_IVAR_$_MXStateMetricData._cpuMetrics
+ _OBJC_IVAR_$_MXStateMetricData._diskIOMetrics
+ _OBJC_IVAR_$_MXStateMetricData._displayMetrics
+ _OBJC_IVAR_$_MXStateMetricData._durationSeconds
+ _OBJC_IVAR_$_MXStateMetricData._gpuMetrics
+ _OBJC_IVAR_$_MXStateMetricData._locationActivityMetrics
+ _OBJC_IVAR_$_MXStateMetricData._memoryMetrics
+ _OBJC_IVAR_$_MXStateMetricData._metalFrameRateMetrics
+ _OBJC_IVAR_$_MXStateMetricData._networkTransferMetrics
+ _OBJC_IVAR_$_MXStateMetricData._reportedState
+ _OBJC_IVAR_$_MXStateMetricData._signpostMetrics
+ _OBJC_IVAR_$_MXThreadMetadata._rootFrameIndices
+ _OBJC_IVAR_$_MXThreadMetadata._threadAttributed
+ _OBJC_METACLASS_$_MXCallStackArray
+ _OBJC_METACLASS_$_MXCallStackArrayBuilder
+ _OBJC_METACLASS_$_MXDiagnosticEnvironment
+ _OBJC_METACLASS_$_MXFlatFrameData
+ _OBJC_METACLASS_$_MXIntervalMetricData
+ _OBJC_METACLASS_$_MXMemoryExceptionDiagnosticContainer
+ _OBJC_METACLASS_$_MXMetalFrameRateMetric
+ _OBJC_METACLASS_$_MXReportedState
+ _OBJC_METACLASS_$_MXStateMetricData
+ _OBJC_METACLASS_$_MXThreadMetadata
+ _OBJC_METACLASS_$__TtC9MetricKit10SignalBars
+ _OBJC_METACLASS_$__TtC9MetricKit21AveragePixelLuminance
+ _OBJC_METACLASS_$__TtC9MetricKit25MetricManagerSubscription
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _OUTLINED_FUNCTION_2
+ __CLASS_METHODS__TtC9MetricKit10SignalBars
+ __CLASS_METHODS__TtC9MetricKit21AveragePixelLuminance
+ __DATA__TtC9MetricKit10SignalBars
+ __DATA__TtC9MetricKit13MetricManager
+ __DATA__TtC9MetricKit21AveragePixelLuminance
+ __DATA__TtC9MetricKit25MetricManagerSubscription
+ __INSTANCE_METHODS__TtC9MetricKit10SignalBars
+ __INSTANCE_METHODS__TtC9MetricKit21AveragePixelLuminance
+ __INSTANCE_METHODS__TtC9MetricKit25MetricManagerSubscription
+ __IVARS__TtC9MetricKit13MetricManager
+ __IVARS__TtC9MetricKit25MetricManagerSubscription
+ __METACLASS_DATA__TtC9MetricKit10SignalBars
+ __METACLASS_DATA__TtC9MetricKit13MetricManager
+ __METACLASS_DATA__TtC9MetricKit21AveragePixelLuminance
+ __METACLASS_DATA__TtC9MetricKit25MetricManagerSubscription
+ __OBJC_$_CLASS_METHODS_MXCallStackArray
+ __OBJC_$_CLASS_METHODS_MXDiagnosticEnvironment
+ __OBJC_$_CLASS_METHODS_MXFlatFrameData
+ __OBJC_$_CLASS_METHODS_MXIntervalMetricData
+ __OBJC_$_CLASS_METHODS_MXMemoryExceptionDiagnosticContainer
+ __OBJC_$_CLASS_METHODS_MXMetalFrameRateMetric
+ __OBJC_$_CLASS_METHODS_MXReportedState
+ __OBJC_$_CLASS_METHODS_MXStateMetricData
+ __OBJC_$_CLASS_METHODS_MXThreadMetadata
+ __OBJC_$_CLASS_PROP_LIST_MXCallStackArray
+ __OBJC_$_CLASS_PROP_LIST_MXDiagnosticEnvironment
+ __OBJC_$_CLASS_PROP_LIST_MXFlatFrameData
+ __OBJC_$_CLASS_PROP_LIST_MXIntervalMetricData
+ __OBJC_$_CLASS_PROP_LIST_MXMemoryExceptionDiagnosticContainer
+ __OBJC_$_CLASS_PROP_LIST_MXReportedState
+ __OBJC_$_CLASS_PROP_LIST_MXStateMetricData
+ __OBJC_$_CLASS_PROP_LIST_MXThreadMetadata
+ __OBJC_$_INSTANCE_METHODS_MXCallStackArray
+ __OBJC_$_INSTANCE_METHODS_MXCallStackArrayBuilder
+ __OBJC_$_INSTANCE_METHODS_MXDiagnosticEnvironment
+ __OBJC_$_INSTANCE_METHODS_MXFlatFrameData
+ __OBJC_$_INSTANCE_METHODS_MXIntervalMetricData
+ __OBJC_$_INSTANCE_METHODS_MXMemoryExceptionDiagnosticContainer
+ __OBJC_$_INSTANCE_METHODS_MXMetalFrameRateMetric
+ __OBJC_$_INSTANCE_METHODS_MXReportedState
+ __OBJC_$_INSTANCE_METHODS_MXStateMetricData
+ __OBJC_$_INSTANCE_METHODS_MXThreadMetadata
+ __OBJC_$_INSTANCE_VARIABLES_MXCallStackArray
+ __OBJC_$_INSTANCE_VARIABLES_MXCallStackArrayBuilder
+ __OBJC_$_INSTANCE_VARIABLES_MXDiagnosticEnvironment
+ __OBJC_$_INSTANCE_VARIABLES_MXFlatFrameData
+ __OBJC_$_INSTANCE_VARIABLES_MXIntervalMetricData
+ __OBJC_$_INSTANCE_VARIABLES_MXMemoryExceptionDiagnosticContainer
+ __OBJC_$_INSTANCE_VARIABLES_MXMetalFrameRateMetric
+ __OBJC_$_INSTANCE_VARIABLES_MXReportedState
+ __OBJC_$_INSTANCE_VARIABLES_MXStateMetricData
+ __OBJC_$_INSTANCE_VARIABLES_MXThreadMetadata
+ __OBJC_$_PROP_LIST_MXCallStackArray
+ __OBJC_$_PROP_LIST_MXDiagnosticEnvironment
+ __OBJC_$_PROP_LIST_MXFlatFrameData
+ __OBJC_$_PROP_LIST_MXIntervalMetricData
+ __OBJC_$_PROP_LIST_MXMemoryExceptionDiagnosticContainer
+ __OBJC_$_PROP_LIST_MXMetalFrameRateMetric
+ __OBJC_$_PROP_LIST_MXReportedState
+ __OBJC_$_PROP_LIST_MXStateMetricData
+ __OBJC_$_PROP_LIST_MXThreadMetadata
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MXMetricManagerSubscriber
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MXMetricManagerSubscriber
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_MXDiagnosticContainerProtocol
+ __OBJC_$_PROTOCOL_REFS_MXMetricManagerSubscriber
+ __OBJC_CLASS_PROTOCOLS_$_MXCallStackArray
+ __OBJC_CLASS_PROTOCOLS_$_MXDiagnosticEnvironment
+ __OBJC_CLASS_PROTOCOLS_$_MXFlatFrameData
+ __OBJC_CLASS_PROTOCOLS_$_MXIntervalMetricData
+ __OBJC_CLASS_PROTOCOLS_$_MXMemoryExceptionDiagnosticContainer
+ __OBJC_CLASS_PROTOCOLS_$_MXReportedState
+ __OBJC_CLASS_PROTOCOLS_$_MXStateMetricData
+ __OBJC_CLASS_PROTOCOLS_$_MXThreadMetadata
+ __OBJC_CLASS_RO_$_MXCallStackArray
+ __OBJC_CLASS_RO_$_MXCallStackArrayBuilder
+ __OBJC_CLASS_RO_$_MXDiagnosticEnvironment
+ __OBJC_CLASS_RO_$_MXFlatFrameData
+ __OBJC_CLASS_RO_$_MXIntervalMetricData
+ __OBJC_CLASS_RO_$_MXMemoryExceptionDiagnosticContainer
+ __OBJC_CLASS_RO_$_MXMetalFrameRateMetric
+ __OBJC_CLASS_RO_$_MXReportedState
+ __OBJC_CLASS_RO_$_MXStateMetricData
+ __OBJC_CLASS_RO_$_MXThreadMetadata
+ __OBJC_LABEL_PROTOCOL_$_MXDiagnosticContainerProtocol
+ __OBJC_LABEL_PROTOCOL_$_MXMetricManagerSubscriber
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_MXCallStackArray
+ __OBJC_METACLASS_RO_$_MXCallStackArrayBuilder
+ __OBJC_METACLASS_RO_$_MXDiagnosticEnvironment
+ __OBJC_METACLASS_RO_$_MXFlatFrameData
+ __OBJC_METACLASS_RO_$_MXIntervalMetricData
+ __OBJC_METACLASS_RO_$_MXMemoryExceptionDiagnosticContainer
+ __OBJC_METACLASS_RO_$_MXMetalFrameRateMetric
+ __OBJC_METACLASS_RO_$_MXReportedState
+ __OBJC_METACLASS_RO_$_MXStateMetricData
+ __OBJC_METACLASS_RO_$_MXThreadMetadata
+ __OBJC_PROTOCOL_$_MXDiagnosticContainerProtocol
+ __OBJC_PROTOCOL_$_MXMetricManagerSubscriber
+ __OBJC_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$_NSObject
+ __PROTOCOLS__TtC9MetricKit25MetricManagerSubscription
+ __PROTOCOLS__TtC9MetricKit25MetricManagerSubscription.2
+ ___38-[MXMetricManager initWithStateAware:]_block_invoke
+ ___38-[MXMetricManager initWithStateAware:]_block_invoke.cold.1
+ ___42+[MXMetricManager stateAwareSharedManager]_block_invoke
+ ___44-[MXMetricManager addStateReportingDomains:]_block_invoke
+ ___47-[MXMetricManager removeStateReportingDomains:]_block_invoke
+ ___NSArray0__struct
+ ___block_literal_global.54
+ ___block_literal_global.59
+ ___swift_async_cont_functlets
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateGenericMetadata
+ ___swift_memcpy0_1
+ ___swift_memcpy154_8
+ ___swift_memcpy16_8
+ ___swift_memcpy176_8
+ ___swift_memcpy17_8
+ ___swift_memcpy1_1
+ ___swift_memcpy208_8
+ ___swift_memcpy24_8
+ ___swift_memcpy48_8
+ ___swift_memcpy4_4
+ ___swift_memcpy80_8
+ ___swift_memcpy88_8
+ ___swift_memcpy8_8
+ ___swift_memcpy9_8
+ ___swift_mutable_project_boxed_opaque_existential_1
+ ___swift_noop_void_return
+ ___unnamed_1
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_MetricKit
+ __swift_stdlib_malloc_size
+ __validatedMetricOfClass
+ _associated conformance 9MetricKit010PeakMemoryA0V10CodingKeys33_23FF6B91966BD0D6D0346FA0DD69FEA6LLOSHAASQ
+ _associated conformance 9MetricKit010PeakMemoryA0V10CodingKeys33_23FF6B91966BD0D6D0346FA0DD69FEA6LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit010PeakMemoryA0V10CodingKeys33_23FF6B91966BD0D6D0346FA0DD69FEA6LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit010PeakMemoryA0VSHAASQ
+ _associated conformance 9MetricKit013TotalFileSizeA0V10CodingKeys33_8D807C669B46F938E9ECF0E96439C9A3LLOSHAASQ
+ _associated conformance 9MetricKit013TotalFileSizeA0V10CodingKeys33_8D807C669B46F938E9ECF0E96439C9A3LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit013TotalFileSizeA0V10CodingKeys33_8D807C669B46F938E9ECF0E96439C9A3LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit013TotalFileSizeA0VSHAASQ
+ _associated conformance 9MetricKit014ExtendedLaunchA0V10CodingKeys33_B3F851CF624E9C41766BCA88C121D88CLLOSHAASQ
+ _associated conformance 9MetricKit014ExtendedLaunchA0V10CodingKeys33_B3F851CF624E9C41766BCA88C121D88CLLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit014ExtendedLaunchA0V10CodingKeys33_B3F851CF624E9C41766BCA88C121D88CLLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit014ExtendedLaunchA0VSHAASQ
+ _associated conformance 9MetricKit014MetalFrameRateA0V10CodingKeys33_99B455C6B4B40F0B5B5954E5EE5AC02ELLOSHAASQ
+ _associated conformance 9MetricKit014MetalFrameRateA0V10CodingKeys33_99B455C6B4B40F0B5B5954E5EE5AC02ELLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit014MetalFrameRateA0V10CodingKeys33_99B455C6B4B40F0B5B5954E5EE5AC02ELLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit014MetalFrameRateA0VSHAASQ
+ _associated conformance 9MetricKit014PixelLuminanceA0V10CodingKeys33_E88C25336A14479CD52CF84AAB23826FLLOSHAASQ
+ _associated conformance 9MetricKit014PixelLuminanceA0V10CodingKeys33_E88C25336A14479CD52CF84AAB23826FLLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit014PixelLuminanceA0V10CodingKeys33_E88C25336A14479CD52CF84AAB23826FLLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit014PixelLuminanceA0VSHAASQ
+ _associated conformance 9MetricKit014TotalFileCountA0V10CodingKeys33_3C80CF88C6B3EBEF2DD8E0DC88F70D96LLOSHAASQ
+ _associated conformance 9MetricKit014TotalFileCountA0V10CodingKeys33_3C80CF88C6B3EBEF2DD8E0DC88F70D96LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit014TotalFileCountA0V10CodingKeys33_3C80CF88C6B3EBEF2DD8E0DC88F70D96LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit014TotalFileCountA0VSHAASQ
+ _associated conformance 9MetricKit015ScrollHitchTimeA0V10CodingKeys33_03245610228668DEF28556E7C33FDCA3LLOSHAASQ
+ _associated conformance 9MetricKit015ScrollHitchTimeA0V10CodingKeys33_03245610228668DEF28556E7C33FDCA3LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit015ScrollHitchTimeA0V10CodingKeys33_03245610228668DEF28556E7C33FDCA3LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit015ScrollHitchTimeA0VSHAASQ
+ _associated conformance 9MetricKit015SuspendedMemoryA0V10CodingKeys33_FCBAE00CCA9D1CB3F9B28CA6502B2F90LLOSHAASQ
+ _associated conformance 9MetricKit015SuspendedMemoryA0V10CodingKeys33_FCBAE00CCA9D1CB3F9B28CA6502B2F90LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit015SuspendedMemoryA0V10CodingKeys33_FCBAE00CCA9D1CB3F9B28CA6502B2F90LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit015SuspendedMemoryA0VSHAASQ
+ _associated conformance 9MetricKit015TimeToFirstDrawA0V10CodingKeys33_3E5B1FD9E1A042D733106E6EC5DC0833LLOSHAASQ
+ _associated conformance 9MetricKit015TimeToFirstDrawA0V10CodingKeys33_3E5B1FD9E1A042D733106E6EC5DC0833LLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit015TimeToFirstDrawA0V10CodingKeys33_3E5B1FD9E1A042D733106E6EC5DC0833LLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit015TimeToFirstDrawA0VSHAASQ
+ _associated conformance 9MetricKit015TotalWiFiUploadA0V10CodingKeys33_9F0F23E401EBCD4A8D755EE82340ADFBLLOSHAASQ
+ _associated conformance 9MetricKit015TotalWiFiUploadA0V10CodingKeys33_9F0F23E401EBCD4A8D755EE82340ADFBLLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit015TotalWiFiUploadA0V10CodingKeys33_9F0F23E401EBCD4A8D755EE82340ADFBLLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit015TotalWiFiUploadA0VSHAASQ
+ _associated conformance 9MetricKit016SignpostIntervalA0V10CodingKeys33_1BBB850FD69063EC4449A298AC57971BLLOSHAASQ
+ _associated conformance 9MetricKit016SignpostIntervalA0V10CodingKeys33_1BBB850FD69063EC4449A298AC57971BLLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit016SignpostIntervalA0V10CodingKeys33_1BBB850FD69063EC4449A298AC57971BLLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit016SignpostIntervalA0VSHAASQ
+ _associated conformance 9MetricKit017LogicalDiskWritesA0V10CodingKeys33_30907B10E3E4D626899DDF05BEC7AEE6LLOSHAASQ
+ _associated conformance 9MetricKit017LogicalDiskWritesA0V10CodingKeys33_30907B10E3E4D626899DDF05BEC7AEE6LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit017LogicalDiskWritesA0V10CodingKeys33_30907B10E3E4D626899DDF05BEC7AEE6LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit017LogicalDiskWritesA0VSHAASQ
+ _associated conformance 9MetricKit017TotalWiFiDownloadA0V10CodingKeys33_A966F018041ED5938BCAC232008657ECLLOSHAASQ
+ _associated conformance 9MetricKit017TotalWiFiDownloadA0V10CodingKeys33_A966F018041ED5938BCAC232008657ECLLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit017TotalWiFiDownloadA0V10CodingKeys33_A966F018041ED5938BCAC232008657ECLLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit017TotalWiFiDownloadA0VSHAASQ
+ _associated conformance 9MetricKit019TotalBackgroundTimeA0V10CodingKeys021_F28B0DC7DEAC9F9EE620I10C4C490394FLLOSHAASQ
+ _associated conformance 9MetricKit019TotalBackgroundTimeA0V10CodingKeys021_F28B0DC7DEAC9F9EE620I10C4C490394FLLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit019TotalBackgroundTimeA0V10CodingKeys021_F28B0DC7DEAC9F9EE620I10C4C490394FLLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit019TotalBackgroundTimeA0VSHAASQ
+ _associated conformance 9MetricKit019TotalCellularUploadA0V10CodingKeys33_3B2E4DAC4FB8B7C28E5C7B8A8200A4C5LLOSHAASQ
+ _associated conformance 9MetricKit019TotalCellularUploadA0V10CodingKeys33_3B2E4DAC4FB8B7C28E5C7B8A8200A4C5LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit019TotalCellularUploadA0V10CodingKeys33_3B2E4DAC4FB8B7C28E5C7B8A8200A4C5LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit019TotalCellularUploadA0VSHAASQ
+ _associated conformance 9MetricKit019TotalForegroundTimeA0V10CodingKeys33_BE47AB2988BDEA265855E5BDC626F717LLOSHAASQ
+ _associated conformance 9MetricKit019TotalForegroundTimeA0V10CodingKeys33_BE47AB2988BDEA265855E5BDC626F717LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit019TotalForegroundTimeA0V10CodingKeys33_BE47AB2988BDEA265855E5BDC626F717LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit019TotalForegroundTimeA0VSHAASQ
+ _associated conformance 9MetricKit020CPUInstructionsCountA0V10CodingKeys33_5B71F41DC98A6271721F92C58E806B59LLOSHAASQ
+ _associated conformance 9MetricKit020CPUInstructionsCountA0V10CodingKeys33_5B71F41DC98A6271721F92C58E806B59LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit020CPUInstructionsCountA0V10CodingKeys33_5B71F41DC98A6271721F92C58E806B59LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit020CPUInstructionsCountA0VSHAASQ
+ _associated conformance 9MetricKit020LocationActivityTimeA0V10CodingKeys33_359D6681CBFE71952A7BBF42B9EE6227LLOSHAASQ
+ _associated conformance 9MetricKit020LocationActivityTimeA0V10CodingKeys33_359D6681CBFE71952A7BBF42B9EE6227LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit020LocationActivityTimeA0V10CodingKeys33_359D6681CBFE71952A7BBF42B9EE6227LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit020LocationActivityTimeA0VSHAASQ
+ _associated conformance 9MetricKit021ApplicationResumeTimeA0V10CodingKeys33_6065BAD8666BE30CCDD5AED2BA2E22C9LLOSHAASQ
+ _associated conformance 9MetricKit021ApplicationResumeTimeA0V10CodingKeys33_6065BAD8666BE30CCDD5AED2BA2E22C9LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit021ApplicationResumeTimeA0V10CodingKeys33_6065BAD8666BE30CCDD5AED2BA2E22C9LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit021ApplicationResumeTimeA0VSHAASQ
+ _associated conformance 9MetricKit021BackgroundTerminationA0V10CodingKeys33_F6A7528DDA68B933ADF5711AE45D1B5ELLOSHAASQ
+ _associated conformance 9MetricKit021BackgroundTerminationA0V10CodingKeys33_F6A7528DDA68B933ADF5711AE45D1B5ELLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit021BackgroundTerminationA0V10CodingKeys33_F6A7528DDA68B933ADF5711AE45D1B5ELLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit021BackgroundTerminationA0VSHAASQ
+ _associated conformance 9MetricKit021CellularConditionTimeA0V10CodingKeys33_0A4D20088FAA6A69417AFFED54D53CE0LLOSHAASQ
+ _associated conformance 9MetricKit021CellularConditionTimeA0V10CodingKeys33_0A4D20088FAA6A69417AFFED54D53CE0LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit021CellularConditionTimeA0V10CodingKeys33_0A4D20088FAA6A69417AFFED54D53CE0LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit021CellularConditionTimeA0VSHAASQ
+ _associated conformance 9MetricKit021ForegroundTerminationA0V10CodingKeys33_6335AE56C1A3DA4A6CE6FB467D896D79LLOSHAASQ
+ _associated conformance 9MetricKit021ForegroundTerminationA0V10CodingKeys33_6335AE56C1A3DA4A6CE6FB467D896D79LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit021ForegroundTerminationA0V10CodingKeys33_6335AE56C1A3DA4A6CE6FB467D896D79LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit021ForegroundTerminationA0VSHAASQ
+ _associated conformance 9MetricKit021TotalCellularDownloadA0V10CodingKeys33_C3F8179C0A8D9850A4672B75EFE898E0LLOSHAASQ
+ _associated conformance 9MetricKit021TotalCellularDownloadA0V10CodingKeys33_C3F8179C0A8D9850A4672B75EFE898E0LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit021TotalCellularDownloadA0V10CodingKeys33_C3F8179C0A8D9850A4672B75EFE898E0LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit021TotalCellularDownloadA0VSHAASQ
+ _associated conformance 9MetricKit022TotalDiskSpaceCapacityA0V10CodingKeys33_6732B9030449A82B94553EEDA33CA538LLOSHAASQ
+ _associated conformance 9MetricKit022TotalDiskSpaceCapacityA0V10CodingKeys33_6732B9030449A82B94553EEDA33CA538LLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit022TotalDiskSpaceCapacityA0V10CodingKeys33_6732B9030449A82B94553EEDA33CA538LLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit022TotalDiskSpaceCapacityA0VSHAASQ
+ _associated conformance 9MetricKit024OptimizedTimeToFirstDrawA0V10CodingKeys025_9720B8D26652F761B9D78A28J6CAC096LLOSHAASQ
+ _associated conformance 9MetricKit024OptimizedTimeToFirstDrawA0V10CodingKeys025_9720B8D26652F761B9D78A28J6CAC096LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit024OptimizedTimeToFirstDrawA0V10CodingKeys025_9720B8D26652F761B9D78A28J6CAC096LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit024OptimizedTimeToFirstDrawA0VSHAASQ
+ _associated conformance 9MetricKit024TotalBackgroundAudioTimeA0V10CodingKeys33_A81B65BC8208469D73F94D30535A43BFLLOSHAASQ
+ _associated conformance 9MetricKit024TotalBackgroundAudioTimeA0V10CodingKeys33_A81B65BC8208469D73F94D30535A43BFLLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit024TotalBackgroundAudioTimeA0V10CodingKeys33_A81B65BC8208469D73F94D30535A43BFLLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit024TotalBackgroundAudioTimeA0VSHAASQ
+ _associated conformance 9MetricKit027TotalBackgroundLocationTimeA0V10CodingKeys33_1A15AB88DD3AFD1EAC286D9FB0F76DBBLLOSHAASQ
+ _associated conformance 9MetricKit027TotalBackgroundLocationTimeA0V10CodingKeys33_1A15AB88DD3AFD1EAC286D9FB0F76DBBLLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit027TotalBackgroundLocationTimeA0V10CodingKeys33_1A15AB88DD3AFD1EAC286D9FB0F76DBBLLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit027TotalBackgroundLocationTimeA0VSHAASQ
+ _associated conformance 9MetricKit07CPUTimeA0V10CodingKeys33_C8E927E6AC5315CC5856EFFD49D6C1B5LLOSHAASQ
+ _associated conformance 9MetricKit07CPUTimeA0V10CodingKeys33_C8E927E6AC5315CC5856EFFD49D6C1B5LLOs0D3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit07CPUTimeA0V10CodingKeys33_C8E927E6AC5315CC5856EFFD49D6C1B5LLOs0D3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit07CPUTimeA0VSHAASQ
+ _associated conformance 9MetricKit07GPUTimeA0V10CodingKeys33_FED091B3587CADBAD2F3D4A502DEB70BLLOSHAASQ
+ _associated conformance 9MetricKit07GPUTimeA0V10CodingKeys33_FED091B3587CADBAD2F3D4A502DEB70BLLOs0D3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit07GPUTimeA0V10CodingKeys33_FED091B3587CADBAD2F3D4A502DEB70BLLOs0D3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit07GPUTimeA0VSHAASQ
+ _associated conformance 9MetricKit08HangTimeA0V10CodingKeys33_48885408AF7B71E97B38A7FBE249EF03LLOSHAASQ
+ _associated conformance 9MetricKit08HangTimeA0V10CodingKeys33_48885408AF7B71E97B38A7FBE249EF03LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit08HangTimeA0V10CodingKeys33_48885408AF7B71E97B38A7FBE249EF03LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit08HangTimeA0VSHAASQ
+ _associated conformance 9MetricKit09HitchTimeA0V10CodingKeys011_2B5C7FD179G20A6A18C2E25E0EB7EAAA5LLOSHAASQ
+ _associated conformance 9MetricKit09HitchTimeA0V10CodingKeys011_2B5C7FD179G20A6A18C2E25E0EB7EAAA5LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit09HitchTimeA0V10CodingKeys011_2B5C7FD179G20A6A18C2E25E0EB7EAAA5LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit09HitchTimeA0VSHAASQ
+ _associated conformance 9MetricKit0A5GroupVSHAASQ
+ _associated conformance 9MetricKit0A6ReportV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLOSHAASQ
+ _associated conformance 9MetricKit0A6ReportV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLOs0D3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit0A6ReportV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLOs0D3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit0A6ReportV10StateEntryV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLOSHAASQ
+ _associated conformance 9MetricKit0A6ReportV10StateEntryV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit0A6ReportV10StateEntryV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit0A6ReportV11EnvironmentV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLOSHAASQ
+ _associated conformance 9MetricKit0A6ReportV11EnvironmentV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit0A6ReportV11EnvironmentV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit0A6ReportV13IntervalEntryV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLOSHAASQ
+ _associated conformance 9MetricKit0A6ReportV13IntervalEntryV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit0A6ReportV13IntervalEntryV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit0A6ReportV14EncodingFormatOSHAASQ
+ _associated conformance 9MetricKit0A6ResultO10CodingKeys33_85E4DAA39F87A1627E572936E3D697BALLOSHAASQ
+ _associated conformance 9MetricKit0A6ResultO10CodingKeys33_85E4DAA39F87A1627E572936E3D697BALLOs0D3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit0A6ResultO10CodingKeys33_85E4DAA39F87A1627E572936E3D697BALLOs0D3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit0A7ManagerC13ReportedStateV10CodingKeys33_5E7E076324A3935404D34BC4802B50B6LLOSHAASQ
+ _associated conformance 9MetricKit0A7ManagerC13ReportedStateV10CodingKeys33_5E7E076324A3935404D34BC4802B50B6LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit0A7ManagerC13ReportedStateV10CodingKeys33_5E7E076324A3935404D34BC4802B50B6LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit0A7ManagerC13ReportedStateVSHAASQ
+ _associated conformance 9MetricKit0A7ManagerC15LaunchTaskErrorV6ReasonOSHAASQ
+ _associated conformance 9MetricKit0aB14LoggerCategoryOSHAASQ
+ _associated conformance 9MetricKit11FeatureFlagOSHAASQ
+ _associated conformance 9MetricKit12LaunchTaskIDVSHAASQ
+ _associated conformance 9MetricKit12LaunchTaskIDVs26ExpressibleByStringLiteralAA0hI4TypesADP_s01_fg7BuiltinhI0
+ _associated conformance 9MetricKit12LaunchTaskIDVs26ExpressibleByStringLiteralAAs0fg23ExtendedGraphemeClusterI0
+ _associated conformance 9MetricKit12LaunchTaskIDVs33ExpressibleByUnicodeScalarLiteralAA0hiJ4TypesADP_s01_fg7BuiltinhiJ0
+ _associated conformance 9MetricKit12LaunchTaskIDVs43ExpressibleByExtendedGraphemeClusterLiteralAA0hijK4TypesADP_s01_fg7BuiltinhijK0
+ _associated conformance 9MetricKit12LaunchTaskIDVs43ExpressibleByExtendedGraphemeClusterLiteralAAs0fg13UnicodeScalarK0
+ _associated conformance 9MetricKit13CallStackTreeV10BinaryInfoV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLOSHAASQ
+ _associated conformance 9MetricKit13CallStackTreeV10BinaryInfoV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit13CallStackTreeV10BinaryInfoV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit13CallStackTreeV10BinaryInfoVSHAASQ
+ _associated conformance 9MetricKit13CallStackTreeV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLOSHAASQ
+ _associated conformance 9MetricKit13CallStackTreeV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit13CallStackTreeV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit13CallStackTreeVSHAASQ
+ _associated conformance 9MetricKit14CallStackFrameV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLOSHAASQ
+ _associated conformance 9MetricKit14CallStackFrameV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit14CallStackFrameV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit14CallStackFrameVSHAASQ
+ _associated conformance 9MetricKit14HangDiagnosticV10CodingKeys33_D754F9606244B2052D94776CECDA492CLLOSHAASQ
+ _associated conformance 9MetricKit14HangDiagnosticV10CodingKeys33_D754F9606244B2052D94776CECDA492CLLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit14HangDiagnosticV10CodingKeys33_D754F9606244B2052D94776CECDA492CLLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit14SignpostRecordV10CodingKeys33_CFA734C2817824AF1AC1ECE1D3570FB2LLOSHAASQ
+ _associated conformance 9MetricKit14SignpostRecordV10CodingKeys33_CFA734C2817824AF1AC1ECE1D3570FB2LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit14SignpostRecordV10CodingKeys33_CFA734C2817824AF1AC1ECE1D3570FB2LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit15CallStackThreadV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLOSHAASQ
+ _associated conformance 9MetricKit15CallStackThreadV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit15CallStackThreadV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit15CallStackThreadVSHAASQ
+ _associated conformance 9MetricKit15CrashDiagnosticV10CodingKeys33_5164B9ABCAEFAB6F5E2B4457471C23A4LLOSHAASQ
+ _associated conformance 9MetricKit15CrashDiagnosticV10CodingKeys33_5164B9ABCAEFAB6F5E2B4457471C23A4LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit15CrashDiagnosticV10CodingKeys33_5164B9ABCAEFAB6F5E2B4457471C23A4LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit15CrashDiagnosticV17TerminationReasonVSHAASQ
+ _associated conformance 9MetricKit15CrashDiagnosticV19TerminationCategoryVSHAASQ
+ _associated conformance 9MetricKit15CrashDiagnosticV25ObjectiveCExceptionReasonV10CodingKeys33_5164B9ABCAEFAB6F5E2B4457471C23A4LLOSHAASQ
+ _associated conformance 9MetricKit15CrashDiagnosticV25ObjectiveCExceptionReasonV10CodingKeys33_5164B9ABCAEFAB6F5E2B4457471C23A4LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit15CrashDiagnosticV25ObjectiveCExceptionReasonV10CodingKeys33_5164B9ABCAEFAB6F5E2B4457471C23A4LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit16DiagnosticReportV10CodingKeys33_6D2ED6D54C08653A1DFA592E99B6EC7DLLOSHAASQ
+ _associated conformance 9MetricKit16DiagnosticReportV10CodingKeys33_6D2ED6D54C08653A1DFA592E99B6EC7DLLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit16DiagnosticReportV10CodingKeys33_6D2ED6D54C08653A1DFA592E99B6EC7DLLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit16DiagnosticReportV11EnvironmentV10CodingKeys33_6D2ED6D54C08653A1DFA592E99B6EC7DLLOSHAASQ
+ _associated conformance 9MetricKit16DiagnosticReportV11EnvironmentV10CodingKeys33_6D2ED6D54C08653A1DFA592E99B6EC7DLLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit16DiagnosticReportV11EnvironmentV10CodingKeys33_6D2ED6D54C08653A1DFA592E99B6EC7DLLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit16DiagnosticResultO10CodingKeys33_0DDD74F52EA265B7459F16A348CA9023LLOSHAASQ
+ _associated conformance 9MetricKit16DiagnosticResultO10CodingKeys33_0DDD74F52EA265B7459F16A348CA9023LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit16DiagnosticResultO10CodingKeys33_0DDD74F52EA265B7459F16A348CA9023LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit17AverageStatisticsV10CodingKeys33_DE2D9734B03ED6E5FD94F5D25658EB9CLLOyx_GSHAASQ
+ _associated conformance 9MetricKit17AverageStatisticsV10CodingKeys33_DE2D9734B03ED6E5FD94F5D25658EB9CLLOyx_Gs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit17AverageStatisticsV10CodingKeys33_DE2D9734B03ED6E5FD94F5D25658EB9CLLOyx_Gs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit17AverageStatisticsVyxGSHAASQ
+ _associated conformance 9MetricKit19AppLaunchDiagnosticV10CodingKeys33_5C4DA93322D4DEAA97B6BD025B39EB39LLOSHAASQ
+ _associated conformance 9MetricKit19AppLaunchDiagnosticV10CodingKeys33_5C4DA93322D4DEAA97B6BD025B39EB39LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit19AppLaunchDiagnosticV10CodingKeys33_5C4DA93322D4DEAA97B6BD025B39EB39LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit20SourceLoggerCategoryOSHAASQ
+ _associated conformance 9MetricKit20StateReportingDomainVSHAASQ
+ _associated conformance 9MetricKit20StateReportingDomainVs26ExpressibleByStringLiteralAA0hI4TypesADP_s01_fg7BuiltinhI0
+ _associated conformance 9MetricKit20StateReportingDomainVs26ExpressibleByStringLiteralAAs0fg23ExtendedGraphemeClusterI0
+ _associated conformance 9MetricKit20StateReportingDomainVs33ExpressibleByUnicodeScalarLiteralAA0hiJ4TypesADP_s01_fg7BuiltinhiJ0
+ _associated conformance 9MetricKit20StateReportingDomainVs43ExpressibleByExtendedGraphemeClusterLiteralAA0hijK4TypesADP_s01_fg7BuiltinhijK0
+ _associated conformance 9MetricKit20StateReportingDomainVs43ExpressibleByExtendedGraphemeClusterLiteralAAs0fg13UnicodeScalarK0
+ _associated conformance 9MetricKit21MeasurementCodingKeys33_E58E169AC6B3C82E3591BD903470FE3ALLOSHAASQ
+ _associated conformance 9MetricKit21MeasurementCodingKeys33_E58E169AC6B3C82E3591BD903470FE3ALLOs0D3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit21MeasurementCodingKeys33_E58E169AC6B3C82E3591BD903470FE3ALLOs0D3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit22CPUExceptionDiagnosticV10CodingKeys33_EA4CA5603DCE70AF83DA4271940FF47DLLOSHAASQ
+ _associated conformance 9MetricKit22CPUExceptionDiagnosticV10CodingKeys33_EA4CA5603DCE70AF83DA4271940FF47DLLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit22CPUExceptionDiagnosticV10CodingKeys33_EA4CA5603DCE70AF83DA4271940FF47DLLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit22DateIntervalCodingKeys33_E58E169AC6B3C82E3591BD903470FE3ALLOSHAASQ
+ _associated conformance 9MetricKit22DateIntervalCodingKeys33_E58E169AC6B3C82E3591BD903470FE3ALLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit22DateIntervalCodingKeys33_E58E169AC6B3C82E3591BD903470FE3ALLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit25MemoryExceptionDiagnosticV10CodingKeys33_C7ADAF7494F05F5888A10451DDE735EDLLOSHAASQ
+ _associated conformance 9MetricKit25MemoryExceptionDiagnosticV10CodingKeys33_C7ADAF7494F05F5888A10451DDE735EDLLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit25MemoryExceptionDiagnosticV10CodingKeys33_C7ADAF7494F05F5888A10451DDE735EDLLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit28DiskWriteExceptionDiagnosticV10CodingKeys33_0263926ED9650D63D957FED9469F9F83LLOSHAASQ
+ _associated conformance 9MetricKit28DiskWriteExceptionDiagnosticV10CodingKeys33_0263926ED9650D63D957FED9469F9F83LLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit28DiskWriteExceptionDiagnosticV10CodingKeys33_0263926ED9650D63D957FED9469F9F83LLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit29StateReportingDomainCodingKey33_9289E22D8F530C7874151738768EE6C5LLVs0fG0AAs23CustomStringConvertible
+ _associated conformance 9MetricKit29StateReportingDomainCodingKey33_9289E22D8F530C7874151738768EE6C5LLVs0fG0AAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit9HistogramV10CodingKeys33_122F627C7D7E4C5AC71DA7223F23D97DLLOyx_GSHAASQ
+ _associated conformance 9MetricKit9HistogramV10CodingKeys33_122F627C7D7E4C5AC71DA7223F23D97DLLOyx_Gs0D3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit9HistogramV10CodingKeys33_122F627C7D7E4C5AC71DA7223F23D97DLLOyx_Gs0D3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit9HistogramV6BucketV10CodingKeys33_122F627C7D7E4C5AC71DA7223F23D97DLLOyx__GSHAASQ
+ _associated conformance 9MetricKit9HistogramV6BucketV10CodingKeys33_122F627C7D7E4C5AC71DA7223F23D97DLLOyx__Gs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit9HistogramV6BucketV10CodingKeys33_122F627C7D7E4C5AC71DA7223F23D97DLLOyx__Gs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9MetricKit9HistogramV6BucketVyx_GSHAASQ
+ _associated conformance 9MetricKit9HistogramVyxGSHAASQ
+ _associated conformance 9MetricKit9OSVersionV10CodingKeys33_81B4729B13564F0357B3F62CE4B9404ELLOSHAASQ
+ _associated conformance 9MetricKit9OSVersionV10CodingKeys33_81B4729B13564F0357B3F62CE4B9404ELLOs0D3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit9OSVersionV10CodingKeys33_81B4729B13564F0357B3F62CE4B9404ELLOs0D3KeyAAs28CustomDebugStringConvertible
+ _bzero
+ _flat unique So29MXDiagnosticContainerProtocol_p
+ _free
+ _get_enum_tag_for_layout_string 9MetricKit15CrashDiagnosticV25ObjectiveCExceptionReasonVSg
+ _get_witness_table ScSy9MetricKit0A6ReportVGSciHPyHC.3
+ _get_witness_table ScSy9MetricKit16DiagnosticReportVGSciHPyHC.4
+ _malloc_size
+ _memcpy
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_resolveTerminationCategoryWithSignal:terminationReason:
+ _objc_msgSend$_updateStateReportingDomainsViaXPC:
+ _objc_msgSend$activeDrawingDuration
+ _objc_msgSend$activeStates
+ _objc_msgSend$addStateReportingDomains:
+ _objc_msgSend$addSubscriber:
+ _objc_msgSend$address
+ _objc_msgSend$allKeys
+ _objc_msgSend$animationMetrics
+ _objc_msgSend$applicationBuildVersion
+ _objc_msgSend$applicationExitMetrics
+ _objc_msgSend$applicationLaunchMetrics
+ _objc_msgSend$applicationResponsivenessMetrics
+ _objc_msgSend$applicationTimeMetrics
+ _objc_msgSend$applicationVersion
+ _objc_msgSend$arguments
+ _objc_msgSend$array
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$attributedThread
+ _objc_msgSend$averageFrameRate
+ _objc_msgSend$averageMemory
+ _objc_msgSend$averagePixelLuminance
+ _objc_msgSend$averageSuspendedMemory
+ _objc_msgSend$backgroundExitData
+ _objc_msgSend$baseUnit
+ _objc_msgSend$beginThreadWithThreadAttributed:
+ _objc_msgSend$beginTimeStamp
+ _objc_msgSend$binaryName
+ _objc_msgSend$binaryUUID
+ _objc_msgSend$bits
+ _objc_msgSend$bucketCount
+ _objc_msgSend$bucketEnd
+ _objc_msgSend$bucketEnumerator
+ _objc_msgSend$bucketStart
+ _objc_msgSend$bytes
+ _objc_msgSend$callStackArray
+ _objc_msgSend$callStackPerThread
+ _objc_msgSend$callStackThreads
+ _objc_msgSend$callStackTree
+ _objc_msgSend$category
+ _objc_msgSend$cellularConditionMetrics
+ _objc_msgSend$childIndices
+ _objc_msgSend$className
+ _objc_msgSend$code
+ _objc_msgSend$composedMessage
+ _objc_msgSend$converter
+ _objc_msgSend$cpuMetrics
+ _objc_msgSend$cumulativeAbnormalExitCount
+ _objc_msgSend$cumulativeAppWatchdogExitCount
+ _objc_msgSend$cumulativeBackgroundAudioTime
+ _objc_msgSend$cumulativeBackgroundLocationTime
+ _objc_msgSend$cumulativeBackgroundTaskAssertionTimeoutExitCount
+ _objc_msgSend$cumulativeBackgroundTime
+ _objc_msgSend$cumulativeBadAccessExitCount
+ _objc_msgSend$cumulativeBestAccuracyForNavigationTime
+ _objc_msgSend$cumulativeBestAccuracyTime
+ _objc_msgSend$cumulativeCPUInstructions
+ _objc_msgSend$cumulativeCPUResourceLimitExitCount
+ _objc_msgSend$cumulativeCPUTime
+ _objc_msgSend$cumulativeCellularDownload
+ _objc_msgSend$cumulativeCellularUpload
+ _objc_msgSend$cumulativeForegroundTime
+ _objc_msgSend$cumulativeGPUTime
+ _objc_msgSend$cumulativeHitchTimeRatio
+ _objc_msgSend$cumulativeHundredMetersAccuracyTime
+ _objc_msgSend$cumulativeIllegalInstructionExitCount
+ _objc_msgSend$cumulativeKilometerAccuracyTime
+ _objc_msgSend$cumulativeLogicalWrites
+ _objc_msgSend$cumulativeMemoryPressureExitCount
+ _objc_msgSend$cumulativeMemoryResourceLimitExitCount
+ _objc_msgSend$cumulativeNearestTenMetersAccuracyTime
+ _objc_msgSend$cumulativeNormalAppExitCount
+ _objc_msgSend$cumulativeSuspendedWithLockedFileExitCount
+ _objc_msgSend$cumulativeThreeKilometersAccuracyTime
+ _objc_msgSend$cumulativeWifiDownload
+ _objc_msgSend$cumulativeWifiUpload
+ _objc_msgSend$decodeInt32ForKey:
+ _objc_msgSend$deviceType
+ _objc_msgSend$diskIOMetrics
+ _objc_msgSend$diskSpaceUsageMetrics
+ _objc_msgSend$displayMetrics
+ _objc_msgSend$domain
+ _objc_msgSend$domainSubscriberCounts
+ _objc_msgSend$durationSeconds
+ _objc_msgSend$encodeInt32:forKey:
+ _objc_msgSend$endTimeStamp
+ _objc_msgSend$environment
+ _objc_msgSend$exabits
+ _objc_msgSend$exabytes
+ _objc_msgSend$exbibits
+ _objc_msgSend$exbibytes
+ _objc_msgSend$exceptionCode
+ _objc_msgSend$exceptionName
+ _objc_msgSend$exceptionReason
+ _objc_msgSend$exceptionType
+ _objc_msgSend$extendLaunchMeasurementForTaskID:error:
+ _objc_msgSend$finishExtendedLaunchMeasurementForTaskID:error:
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$flatFrames
+ _objc_msgSend$foregroundExitData
+ _objc_msgSend$formatString
+ _objc_msgSend$frameCount
+ _objc_msgSend$gibibits
+ _objc_msgSend$gibibytes
+ _objc_msgSend$gigabits
+ _objc_msgSend$gigabytes
+ _objc_msgSend$gigahertz
+ _objc_msgSend$gpuMetrics
+ _objc_msgSend$hangDuration
+ _objc_msgSend$hertz
+ _objc_msgSend$histogrammedApplicationHangTime
+ _objc_msgSend$histogrammedApplicationResumeTime
+ _objc_msgSend$histogrammedCellularConditionTime
+ _objc_msgSend$histogrammedExtendedLaunch
+ _objc_msgSend$histogrammedOptimizedTimeToFirstDraw
+ _objc_msgSend$histogrammedSignpostDuration
+ _objc_msgSend$histogrammedTimeToFirstDraw
+ _objc_msgSend$hitchTimeRatio
+ _objc_msgSend$hours
+ _objc_msgSend$includesMultipleApplicationVersions
+ _objc_msgSend$initWithBinaryName:binaryUUID:address:offsetIntoBinaryTextSegment:sampleCount:parentIndex:childIndices:threadIndex:
+ _objc_msgSend$initWithBundleIdentifier:applicationVersion:applicationBuildVersion:pid:osVersion:deviceType:signpostData:reportedStateData:regionFormat:platformArchitecture:lowPowerModeEnabled:isTestFlightApp:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithCoder:
+ _objc_msgSend$initWithDomain:label:stableContext:durationSeconds:
+ _objc_msgSend$initWithFlatFrames:threadMetadata:callStackPerThread:
+ _objc_msgSend$initWithLayerName:frameCount:activeDrawingDuration:averageFrameRate:
+ _objc_msgSend$initWithReportedState:durationSeconds:cpuMetrics:gpuMetrics:applicationTimeMetrics:locationActivityMetrics:networkTransferMetrics:diskIOMetrics:memoryMetrics:displayMetrics:cellularConditionMetrics:applicationLaunchMetrics:applicationResponsivenessMetrics:animationMetrics:applicationExitMetrics:signpostMetrics:metalFrameRateMetrics:
+ _objc_msgSend$initWithStartDate:endDate:diagnostics:
+ _objc_msgSend$initWithStartDate:endDate:diagnostics:diagnosticContainers:
+ _objc_msgSend$initWithStartTimestamp:endTimestamp:durationSeconds:cpuMetrics:gpuMetrics:applicationTimeMetrics:locationActivityMetrics:networkTransferMetrics:diskIOMetrics:memoryMetrics:displayMetrics:cellularConditionMetrics:applicationLaunchMetrics:applicationResponsivenessMetrics:animationMetrics:applicationExitMetrics:signpostMetrics:metalFrameRateMetrics:activeStates:
+ _objc_msgSend$initWithStateAware:
+ _objc_msgSend$initWithThreadAttributed:rootFrameIndices:
+ _objc_msgSend$integerValue
+ _objc_msgSend$intervalMetrics
+ _objc_msgSend$isTestFlightApp
+ _objc_msgSend$kibibits
+ _objc_msgSend$kibibytes
+ _objc_msgSend$kilobits
+ _objc_msgSend$kilohertz
+ _objc_msgSend$label
+ _objc_msgSend$latestApplicationVersion
+ _objc_msgSend$launchDuration
+ _objc_msgSend$layerName
+ _objc_msgSend$length
+ _objc_msgSend$locationActivityMetrics
+ _objc_msgSend$lowPowerModeEnabled
+ _objc_msgSend$makeLogHandleWithCategory:
+ _objc_msgSend$mebibits
+ _objc_msgSend$mebibytes
+ _objc_msgSend$megabits
+ _objc_msgSend$megabytes
+ _objc_msgSend$megahertz
+ _objc_msgSend$memoryExceptionDiagnosticContainers
+ _objc_msgSend$memoryMetrics
+ _objc_msgSend$metaData
+ _objc_msgSend$metalFrameRateMetrics
+ _objc_msgSend$microhertz
+ _objc_msgSend$microseconds
+ _objc_msgSend$millihertz
+ _objc_msgSend$minutes
+ _objc_msgSend$name
+ _objc_msgSend$nanohertz
+ _objc_msgSend$nanoseconds
+ _objc_msgSend$networkTransferMetrics
+ _objc_msgSend$nextObject
+ _objc_msgSend$nibbles
+ _objc_msgSend$numberOfRanges
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$offsetInBinary
+ _objc_msgSend$offsetIntoBinaryTextSegment
+ _objc_msgSend$osBuildNumber
+ _objc_msgSend$osPlatform
+ _objc_msgSend$osVersionNumber
+ _objc_msgSend$parentIndex
+ _objc_msgSend$peakMemoryUsage
+ _objc_msgSend$pebibits
+ _objc_msgSend$pebibytes
+ _objc_msgSend$petabits
+ _objc_msgSend$petabytes
+ _objc_msgSend$picoseconds
+ _objc_msgSend$pid
+ _objc_msgSend$platformArchitecture
+ _objc_msgSend$rangeAtIndex:
+ _objc_msgSend$regionFormat
+ _objc_msgSend$registerClientWithStateAwareDomains:
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeStateReportingDomains:
+ _objc_msgSend$removeSubscriber:
+ _objc_msgSend$reportedState
+ _objc_msgSend$reportedStateData
+ _objc_msgSend$reportedStateWithDictionary:
+ _objc_msgSend$rootFrameIndices
+ _objc_msgSend$sampleCount
+ _objc_msgSend$scanHexLongLong:
+ _objc_msgSend$scannerWithString:
+ _objc_msgSend$scrollHitchTimeRatio
+ _objc_msgSend$seconds
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$signal
+ _objc_msgSend$signpostCategory
+ _objc_msgSend$signpostData
+ _objc_msgSend$signpostIntervalData
+ _objc_msgSend$signpostMetrics
+ _objc_msgSend$signpostName
+ _objc_msgSend$stableContext
+ _objc_msgSend$standardDeviation
+ _objc_msgSend$stateAwareSharedManager
+ _objc_msgSend$stateMetrics
+ _objc_msgSend$subFrames
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$subsystem
+ _objc_msgSend$symbol
+ _objc_msgSend$tebibits
+ _objc_msgSend$tebibytes
+ _objc_msgSend$terabits
+ _objc_msgSend$terabytes
+ _objc_msgSend$terahertz
+ _objc_msgSend$terminationCategory
+ _objc_msgSend$terminationReason
+ _objc_msgSend$threadAttributed
+ _objc_msgSend$threadIndex
+ _objc_msgSend$threadMetadata
+ _objc_msgSend$topFrames
+ _objc_msgSend$totalAnimationTime
+ _objc_msgSend$totalBinaryFileCount
+ _objc_msgSend$totalBinaryFileSize
+ _objc_msgSend$totalCPUTime
+ _objc_msgSend$totalCacheFolderSize
+ _objc_msgSend$totalCloneSize
+ _objc_msgSend$totalCount
+ _objc_msgSend$totalDataFileCount
+ _objc_msgSend$totalDataFileSize
+ _objc_msgSend$totalDiskSpaceCapacity
+ _objc_msgSend$totalDiskSpaceUsedSize
+ _objc_msgSend$totalHitchTime
+ _objc_msgSend$totalSampledTime
+ _objc_msgSend$totalScrollHitchTime
+ _objc_msgSend$totalScrollTime
+ _objc_msgSend$totalWritesCaused
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$virtualMemoryRegionInfo
+ _objc_msgSend$yobibits
+ _objc_msgSend$yobibytes
+ _objc_msgSend$yottabits
+ _objc_msgSend$yottabytes
+ _objc_msgSend$zebibits
+ _objc_msgSend$zebibytes
+ _objc_msgSend$zettabits
+ _objc_msgSend$zettabytes
+ _objc_opt_isKindOfClass
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x6
+ _objc_retain_x7
+ _objc_retain_x8
+ _objc_setProperty_nonatomic_copy
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _stateAwareSharedManager.onceToken
+ _stateAwareSharedManager.stateAwareSharedManager
+ _swift_allocError
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_beginAccess
+ _swift_coroFrameAlloc
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_dynamicCast
+ _swift_dynamicCastObjCClass
+ _swift_dynamicCastUnknownClass
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_getEnumCaseMultiPayload
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getForeignTypeMetadata
+ _swift_getGenericMetadata
+ _swift_getObjCClassFromMetadata
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_lookUpClassMethod
+ _swift_makeBoxUnique
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain
+ _swift_retain_x20
+ _swift_retain_x23
+ _swift_retain_x27
+ _swift_retain_x9
+ _swift_slowDealloc
+ _swift_storeEnumTagMultiPayload
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_task_alloc
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_updateClassMetadata2
+ _swift_weakAssign
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
+ _swift_willThrow
+ _symbolic $ss26ExpressibleByStringLiteralP
+ _symbolic $ss33ExpressibleByUnicodeScalarLiteralP
+ _symbolic $ss43ExpressibleByExtendedGraphemeClusterLiteralP
+ _symbolic 7ElementSciQz
+ _symbolic 7FailureSciQz
+ _symbolic SDySS_____G 14StateReporting23ReportableMetadataValueO
+ _symbolic SDySSypG
+ _symbolic SDy_____Say_____GG 9MetricKit20StateReportingDomainV AA0A6ReportV0C5EntryV
+ _symbolic SDy_____Say_____GG 9MetricKit20StateReportingDomainV AA0A7ManagerC08ReportedC0V
+ _symbolic SDy__________G 10Foundation4UUIDV 9MetricKit13CallStackTreeV10BinaryInfoV
+ _symbolic SS
+ _symbolic SS3key______5valuet 14StateReporting23ReportableMetadataValueO
+ _symbolic SSSg
+ _symbolic SS______t 14StateReporting23ReportableMetadataValueO
+ _symbolic SaySSG
+ _symbolic Say_____G 9MetricKit0A6ReportV10StateEntryV
+ _symbolic Say_____G 9MetricKit0A6ReportV13IntervalEntryV
+ _symbolic Say_____G 9MetricKit0A6ResultO
+ _symbolic Say_____G 9MetricKit0A7ManagerC13ReportedStateV
+ _symbolic Say_____G 9MetricKit13CallStackTreeV10BinaryInfoV
+ _symbolic Say_____G 9MetricKit14SignpostRecordV
+ _symbolic Say_____yx_GG 9MetricKit9HistogramV6BucketV
+ _symbolic Sb
+ _symbolic SbSg
+ _symbolic ScSy_____G 9MetricKit0A6ReportV
+ _symbolic ScSy_____G 9MetricKit16DiagnosticReportV
+ _symbolic SdSg
+ _symbolic Shy_____G 9MetricKit20StateReportingDomainV
+ _symbolic SiSg
+ _symbolic Si______t 9MetricKit14CallStackFrameV
+ _symbolic So11NSDimensionC
+ _symbolic So15MXMetricManagerCSg
+ _symbolic So17MXHistogramBucketC
+ _symbolic _____ 10Foundation12DateIntervalV
+ _symbolic _____ 10Foundation4UUIDV
+ _symbolic _____ 9MetricKit010PeakMemoryA0V
+ _symbolic _____ 9MetricKit010PeakMemoryA0V10CodingKeys33_23FF6B91966BD0D6D0346FA0DD69FEA6LLO
+ _symbolic _____ 9MetricKit013TotalFileSizeA0V
+ _symbolic _____ 9MetricKit013TotalFileSizeA0V10CodingKeys33_8D807C669B46F938E9ECF0E96439C9A3LLO
+ _symbolic _____ 9MetricKit014ExtendedLaunchA0V
+ _symbolic _____ 9MetricKit014ExtendedLaunchA0V10CodingKeys33_B3F851CF624E9C41766BCA88C121D88CLLO
+ _symbolic _____ 9MetricKit014MetalFrameRateA0V
+ _symbolic _____ 9MetricKit014MetalFrameRateA0V10CodingKeys33_99B455C6B4B40F0B5B5954E5EE5AC02ELLO
+ _symbolic _____ 9MetricKit014PixelLuminanceA0V
+ _symbolic _____ 9MetricKit014PixelLuminanceA0V10CodingKeys33_E88C25336A14479CD52CF84AAB23826FLLO
+ _symbolic _____ 9MetricKit014TotalFileCountA0V
+ _symbolic _____ 9MetricKit014TotalFileCountA0V10CodingKeys33_3C80CF88C6B3EBEF2DD8E0DC88F70D96LLO
+ _symbolic _____ 9MetricKit015ScrollHitchTimeA0V
+ _symbolic _____ 9MetricKit015ScrollHitchTimeA0V10CodingKeys33_03245610228668DEF28556E7C33FDCA3LLO
+ _symbolic _____ 9MetricKit015SuspendedMemoryA0V
+ _symbolic _____ 9MetricKit015SuspendedMemoryA0V10CodingKeys33_FCBAE00CCA9D1CB3F9B28CA6502B2F90LLO
+ _symbolic _____ 9MetricKit015TimeToFirstDrawA0V
+ _symbolic _____ 9MetricKit015TimeToFirstDrawA0V10CodingKeys33_3E5B1FD9E1A042D733106E6EC5DC0833LLO
+ _symbolic _____ 9MetricKit015TotalWiFiUploadA0V
+ _symbolic _____ 9MetricKit015TotalWiFiUploadA0V10CodingKeys33_9F0F23E401EBCD4A8D755EE82340ADFBLLO
+ _symbolic _____ 9MetricKit016SignpostIntervalA0V
+ _symbolic _____ 9MetricKit016SignpostIntervalA0V10CodingKeys33_1BBB850FD69063EC4449A298AC57971BLLO
+ _symbolic _____ 9MetricKit017LogicalDiskWritesA0V
+ _symbolic _____ 9MetricKit017LogicalDiskWritesA0V10CodingKeys33_30907B10E3E4D626899DDF05BEC7AEE6LLO
+ _symbolic _____ 9MetricKit017TotalWiFiDownloadA0V
+ _symbolic _____ 9MetricKit017TotalWiFiDownloadA0V10CodingKeys33_A966F018041ED5938BCAC232008657ECLLO
+ _symbolic _____ 9MetricKit019TotalBackgroundTimeA0V
+ _symbolic _____ 9MetricKit019TotalBackgroundTimeA0V10CodingKeys021_F28B0DC7DEAC9F9EE620I10C4C490394FLLO
+ _symbolic _____ 9MetricKit019TotalCellularUploadA0V
+ _symbolic _____ 9MetricKit019TotalCellularUploadA0V10CodingKeys33_3B2E4DAC4FB8B7C28E5C7B8A8200A4C5LLO
+ _symbolic _____ 9MetricKit019TotalForegroundTimeA0V
+ _symbolic _____ 9MetricKit019TotalForegroundTimeA0V10CodingKeys33_BE47AB2988BDEA265855E5BDC626F717LLO
+ _symbolic _____ 9MetricKit020CPUInstructionsCountA0V
+ _symbolic _____ 9MetricKit020CPUInstructionsCountA0V10CodingKeys33_5B71F41DC98A6271721F92C58E806B59LLO
+ _symbolic _____ 9MetricKit020LocationActivityTimeA0V
+ _symbolic _____ 9MetricKit020LocationActivityTimeA0V10CodingKeys33_359D6681CBFE71952A7BBF42B9EE6227LLO
+ _symbolic _____ 9MetricKit021ApplicationResumeTimeA0V
+ _symbolic _____ 9MetricKit021ApplicationResumeTimeA0V10CodingKeys33_6065BAD8666BE30CCDD5AED2BA2E22C9LLO
+ _symbolic _____ 9MetricKit021BackgroundTerminationA0V
+ _symbolic _____ 9MetricKit021BackgroundTerminationA0V10CodingKeys33_F6A7528DDA68B933ADF5711AE45D1B5ELLO
+ _symbolic _____ 9MetricKit021CellularConditionTimeA0V
+ _symbolic _____ 9MetricKit021CellularConditionTimeA0V10CodingKeys33_0A4D20088FAA6A69417AFFED54D53CE0LLO
+ _symbolic _____ 9MetricKit021ForegroundTerminationA0V
+ _symbolic _____ 9MetricKit021ForegroundTerminationA0V10CodingKeys33_6335AE56C1A3DA4A6CE6FB467D896D79LLO
+ _symbolic _____ 9MetricKit021TotalCellularDownloadA0V
+ _symbolic _____ 9MetricKit021TotalCellularDownloadA0V10CodingKeys33_C3F8179C0A8D9850A4672B75EFE898E0LLO
+ _symbolic _____ 9MetricKit022TotalDiskSpaceCapacityA0V
+ _symbolic _____ 9MetricKit022TotalDiskSpaceCapacityA0V10CodingKeys33_6732B9030449A82B94553EEDA33CA538LLO
+ _symbolic _____ 9MetricKit024OptimizedTimeToFirstDrawA0V
+ _symbolic _____ 9MetricKit024OptimizedTimeToFirstDrawA0V10CodingKeys025_9720B8D26652F761B9D78A28J6CAC096LLO
+ _symbolic _____ 9MetricKit024TotalBackgroundAudioTimeA0V
+ _symbolic _____ 9MetricKit024TotalBackgroundAudioTimeA0V10CodingKeys33_A81B65BC8208469D73F94D30535A43BFLLO
+ _symbolic _____ 9MetricKit027TotalBackgroundLocationTimeA0V
+ _symbolic _____ 9MetricKit027TotalBackgroundLocationTimeA0V10CodingKeys33_1A15AB88DD3AFD1EAC286D9FB0F76DBBLLO
+ _symbolic _____ 9MetricKit07CPUTimeA0V
+ _symbolic _____ 9MetricKit07CPUTimeA0V10CodingKeys33_C8E927E6AC5315CC5856EFFD49D6C1B5LLO
+ _symbolic _____ 9MetricKit07GPUTimeA0V
+ _symbolic _____ 9MetricKit07GPUTimeA0V10CodingKeys33_FED091B3587CADBAD2F3D4A502DEB70BLLO
+ _symbolic _____ 9MetricKit08HangTimeA0V
+ _symbolic _____ 9MetricKit08HangTimeA0V10CodingKeys33_48885408AF7B71E97B38A7FBE249EF03LLO
+ _symbolic _____ 9MetricKit09HitchTimeA0V
+ _symbolic _____ 9MetricKit09HitchTimeA0V10CodingKeys011_2B5C7FD179G20A6A18C2E25E0EB7EAAA5LLO
+ _symbolic _____ 9MetricKit0A19ManagerSubscriptionC
+ _symbolic _____ 9MetricKit0A5GroupV
+ _symbolic _____ 9MetricKit0A6ReportV
+ _symbolic _____ 9MetricKit0A6ReportV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLO
+ _symbolic _____ 9MetricKit0A6ReportV10StateEntryV
+ _symbolic _____ 9MetricKit0A6ReportV10StateEntryV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLO
+ _symbolic _____ 9MetricKit0A6ReportV11EnvironmentV
+ _symbolic _____ 9MetricKit0A6ReportV11EnvironmentV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLO
+ _symbolic _____ 9MetricKit0A6ReportV13IntervalEntryV
+ _symbolic _____ 9MetricKit0A6ReportV13IntervalEntryV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLO
+ _symbolic _____ 9MetricKit0A6ReportV14EncodingFormatO
+ _symbolic _____ 9MetricKit0A6ResultO
+ _symbolic _____ 9MetricKit0A6ResultO10CodingKeys33_85E4DAA39F87A1627E572936E3D697BALLO
+ _symbolic _____ 9MetricKit0A7ManagerC
+ _symbolic _____ 9MetricKit0A7ManagerC13ReportedStateV
+ _symbolic _____ 9MetricKit0A7ManagerC13ReportedStateV10CodingKeys33_5E7E076324A3935404D34BC4802B50B6LLO
+ _symbolic _____ 9MetricKit0A7ManagerC15LaunchTaskErrorV
+ _symbolic _____ 9MetricKit0A7ManagerC15LaunchTaskErrorV6ReasonO
+ _symbolic _____ 9MetricKit0A7ManagerC9ConstantsO
+ _symbolic _____ 9MetricKit0aB14LoggerCategoryO
+ _symbolic _____ 9MetricKit10SignalBarsC
+ _symbolic _____ 9MetricKit11FeatureFlagO
+ _symbolic _____ 9MetricKit12LaunchTaskIDV
+ _symbolic _____ 9MetricKit12_FeatureFlagV
+ _symbolic _____ 9MetricKit13CallStackTreeV
+ _symbolic _____ 9MetricKit13CallStackTreeV10BinaryInfoV
+ _symbolic _____ 9MetricKit13CallStackTreeV10BinaryInfoV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLO
+ _symbolic _____ 9MetricKit13CallStackTreeV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLO
+ _symbolic _____ 9MetricKit14CallStackFrameV
+ _symbolic _____ 9MetricKit14CallStackFrameV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLO
+ _symbolic _____ 9MetricKit14HangDiagnosticV
+ _symbolic _____ 9MetricKit14HangDiagnosticV10CodingKeys33_D754F9606244B2052D94776CECDA492CLLO
+ _symbolic _____ 9MetricKit14SignpostRecordV
+ _symbolic _____ 9MetricKit14SignpostRecordV10CodingKeys33_CFA734C2817824AF1AC1ECE1D3570FB2LLO
+ _symbolic _____ 9MetricKit15CallStackThreadV
+ _symbolic _____ 9MetricKit15CallStackThreadV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLO
+ _symbolic _____ 9MetricKit15CrashDiagnosticV
+ _symbolic _____ 9MetricKit15CrashDiagnosticV10CodingKeys33_5164B9ABCAEFAB6F5E2B4457471C23A4LLO
+ _symbolic _____ 9MetricKit15CrashDiagnosticV17TerminationReasonV
+ _symbolic _____ 9MetricKit15CrashDiagnosticV19TerminationCategoryV
+ _symbolic _____ 9MetricKit15CrashDiagnosticV25ObjectiveCExceptionReasonV
+ _symbolic _____ 9MetricKit15CrashDiagnosticV25ObjectiveCExceptionReasonV10CodingKeys33_5164B9ABCAEFAB6F5E2B4457471C23A4LLO
+ _symbolic _____ 9MetricKit16DiagnosticReportV
+ _symbolic _____ 9MetricKit16DiagnosticReportV10CodingKeys33_6D2ED6D54C08653A1DFA592E99B6EC7DLLO
+ _symbolic _____ 9MetricKit16DiagnosticReportV11EnvironmentV
+ _symbolic _____ 9MetricKit16DiagnosticReportV11EnvironmentV10CodingKeys33_6D2ED6D54C08653A1DFA592E99B6EC7DLLO
+ _symbolic _____ 9MetricKit16DiagnosticResultO
+ _symbolic _____ 9MetricKit16DiagnosticResultO10CodingKeys33_0DDD74F52EA265B7459F16A348CA9023LLO
+ _symbolic _____ 9MetricKit17AverageStatisticsV
+ _symbolic _____ 9MetricKit17AverageStatisticsV10CodingKeys33_DE2D9734B03ED6E5FD94F5D25658EB9CLLO
+ _symbolic _____ 9MetricKit19AppLaunchDiagnosticV
+ _symbolic _____ 9MetricKit19AppLaunchDiagnosticV10CodingKeys33_5C4DA93322D4DEAA97B6BD025B39EB39LLO
+ _symbolic _____ 9MetricKit20SourceLoggerCategoryO
+ _symbolic _____ 9MetricKit20StateReportingDomainV
+ _symbolic _____ 9MetricKit21AveragePixelLuminanceC
+ _symbolic _____ 9MetricKit21MeasurementCodingKeys33_E58E169AC6B3C82E3591BD903470FE3ALLO
+ _symbolic _____ 9MetricKit22CPUExceptionDiagnosticV
+ _symbolic _____ 9MetricKit22CPUExceptionDiagnosticV10CodingKeys33_EA4CA5603DCE70AF83DA4271940FF47DLLO
+ _symbolic _____ 9MetricKit22DateIntervalCodingKeys33_E58E169AC6B3C82E3591BD903470FE3ALLO
+ _symbolic _____ 9MetricKit25MemoryExceptionDiagnosticV
+ _symbolic _____ 9MetricKit25MemoryExceptionDiagnosticV10CodingKeys33_C7ADAF7494F05F5888A10451DDE735EDLLO
+ _symbolic _____ 9MetricKit28DiskWriteExceptionDiagnosticV
+ _symbolic _____ 9MetricKit28DiskWriteExceptionDiagnosticV10CodingKeys33_0263926ED9650D63D957FED9469F9F83LLO
+ _symbolic _____ 9MetricKit29StateReportingDomainCodingKey33_9289E22D8F530C7874151738768EE6C5LLV
+ _symbolic _____ 9MetricKit9HistogramV
+ _symbolic _____ 9MetricKit9HistogramV10CodingKeys33_122F627C7D7E4C5AC71DA7223F23D97DLLO
+ _symbolic _____ 9MetricKit9HistogramV6BucketV
+ _symbolic _____ 9MetricKit9HistogramV6BucketV10CodingKeys33_122F627C7D7E4C5AC71DA7223F23D97DLLO
+ _symbolic _____ 9MetricKit9OSVersionV
+ _symbolic _____ 9MetricKit9OSVersionV10CodingKeys33_81B4729B13564F0357B3F62CE4B9404ELLO
+ _symbolic _____ So16os_unfair_lock_sV
+ _symbolic _____ s5NeverO
+ _symbolic _____ s6UInt32V
+ _symbolic _____3key______5valuet 10Foundation4UUIDV 9MetricKit13CallStackTreeV10BinaryInfoV
+ _symbolic _____3key_yp5valuet s11AnyHashableV
+ _symbolic _____Sg 10Foundation4UUIDV
+ _symbolic _____Sg 9MetricKit010PeakMemoryA0V
+ _symbolic _____Sg 9MetricKit013TotalFileSizeA0V
+ _symbolic _____Sg 9MetricKit014MetalFrameRateA0V
+ _symbolic _____Sg 9MetricKit014PixelLuminanceA0V
+ _symbolic _____Sg 9MetricKit015ScrollHitchTimeA0V
+ _symbolic _____Sg 9MetricKit015SuspendedMemoryA0V
+ _symbolic _____Sg 9MetricKit015TotalWiFiUploadA0V
+ _symbolic _____Sg 9MetricKit016SignpostIntervalA0V
+ _symbolic _____Sg 9MetricKit017LogicalDiskWritesA0V
+ _symbolic _____Sg 9MetricKit017TotalWiFiDownloadA0V
+ _symbolic _____Sg 9MetricKit019TotalBackgroundTimeA0V
+ _symbolic _____Sg 9MetricKit019TotalCellularUploadA0V
+ _symbolic _____Sg 9MetricKit019TotalForegroundTimeA0V
+ _symbolic _____Sg 9MetricKit020LocationActivityTimeA0V
+ _symbolic _____Sg 9MetricKit021TotalCellularDownloadA0V
+ _symbolic _____Sg 9MetricKit022TotalDiskSpaceCapacityA0V
+ _symbolic _____Sg 9MetricKit024TotalBackgroundAudioTimeA0V
+ _symbolic _____Sg 9MetricKit027TotalBackgroundLocationTimeA0V
+ _symbolic _____Sg 9MetricKit07CPUTimeA0V
+ _symbolic _____Sg 9MetricKit07GPUTimeA0V
+ _symbolic _____Sg 9MetricKit09HitchTimeA0V
+ _symbolic _____Sg 9MetricKit0A19ManagerSubscriptionC
+ _symbolic _____Sg 9MetricKit0A6ReportV11EnvironmentV
+ _symbolic _____Sg 9MetricKit13CallStackTreeV10BinaryInfoV
+ _symbolic _____Sg 9MetricKit14CallStackFrameV
+ _symbolic _____Sg 9MetricKit14HangDiagnosticV
+ _symbolic _____Sg 9MetricKit15CrashDiagnosticV17TerminationReasonV
+ _symbolic _____Sg 9MetricKit15CrashDiagnosticV19TerminationCategoryV
+ _symbolic _____Sg 9MetricKit15CrashDiagnosticV25ObjectiveCExceptionReasonV
+ _symbolic _____Sg 9MetricKit19AppLaunchDiagnosticV
+ _symbolic _____Sg 9MetricKit22CPUExceptionDiagnosticV
+ _symbolic _____Sg 9MetricKit28DiskWriteExceptionDiagnosticV
+ _symbolic _____Sg s17CodingUserInfoKeyV
+ _symbolic _____Sg s5Int32V
+ _symbolic _____Sg s6UInt64V
+ _symbolic _____SgXw 9MetricKit0A7ManagerC
+ _symbolic _____Sg_ABt 10Foundation4UUIDV
+ _symbolic ___________t 10Foundation4UUIDV 9MetricKit13CallStackTreeV10BinaryInfoV
+ _symbolic ______p So29MXDiagnosticContainerProtocolP
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____ySS_____G s18_DictionaryStorageC 14StateReporting23ReportableMetadataValueO
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic _____ySiG s11_SetStorageC
+ _symbolic _____ySiG s23_ContiguousArrayStorageC
+ _symbolic _____ySi_____G s18_DictionaryStorageC 9MetricKit14CallStackFrameV
+ _symbolic _____ySnySiGG s23_ContiguousArrayStorageC
+ _symbolic _____ySo14NSUnitDurationCG 10Foundation11MeasurementV
+ _symbolic _____ySo14NSUnitDurationCG 9MetricKit9HistogramV
+ _symbolic _____ySo14NSUnitDurationCGSg 10Foundation11MeasurementV
+ _symbolic _____ySo14NSUnitDurationCGSg_AEt 10Foundation11MeasurementV
+ _symbolic _____ySo15NSUnitFrequencyCG 10Foundation11MeasurementV
+ _symbolic _____ySo16MXUnitSignalBarsCG 10Foundation11MeasurementV
+ _symbolic _____ySo24NSUnitInformationStorageCG 10Foundation11MeasurementV
+ _symbolic _____ySo24NSUnitInformationStorageCG 9MetricKit17AverageStatisticsV
+ _symbolic _____ySo24NSUnitInformationStorageCGSg 10Foundation11MeasurementV
+ _symbolic _____ySo24NSUnitInformationStorageCGSg 9MetricKit17AverageStatisticsV
+ _symbolic _____ySo24NSUnitInformationStorageCGSg_AEt 10Foundation11MeasurementV
+ _symbolic _____ySo24NSUnitInformationStorageCGSg_AEt 9MetricKit17AverageStatisticsV
+ _symbolic _____ySo27MXUnitAveragePixelLuminanceCG 10Foundation11MeasurementV
+ _symbolic _____ySo6NSUnitCG 10Foundation11MeasurementV
+ _symbolic _____ySo6NSUnitCGSg 10Foundation11MeasurementV
+ _symbolic _____ySo6NSUnitCGSg_AEt 10Foundation11MeasurementV
+ _symbolic _____y_____G 10Foundation11MeasurementV 9MetricKit21AveragePixelLuminanceC
+ _symbolic _____y_____G 9MetricKit17AverageStatisticsV AA0C14PixelLuminanceC
+ _symbolic _____y_____G 9MetricKit9HistogramV AA10SignalBarsC
+ _symbolic _____y_____G s15ContiguousArrayV 9MetricKit14CallStackFrameV
+ _symbolic _____y_____G s15ContiguousArrayV 9MetricKit15CallStackThreadV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit010PeakMemoryD0V10CodingKeys33_23FF6B91966BD0D6D0346FA0DD69FEA6LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit013TotalFileSizeD0V10CodingKeys33_8D807C669B46F938E9ECF0E96439C9A3LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit014ExtendedLaunchD0V10CodingKeys33_B3F851CF624E9C41766BCA88C121D88CLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit014MetalFrameRateD0V10CodingKeys33_99B455C6B4B40F0B5B5954E5EE5AC02ELLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit014PixelLuminanceD0V10CodingKeys33_E88C25336A14479CD52CF84AAB23826FLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit014TotalFileCountD0V10CodingKeys33_3C80CF88C6B3EBEF2DD8E0DC88F70D96LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit015ScrollHitchTimeD0V10CodingKeys33_03245610228668DEF28556E7C33FDCA3LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit015SuspendedMemoryD0V10CodingKeys33_FCBAE00CCA9D1CB3F9B28CA6502B2F90LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit015TimeToFirstDrawD0V10CodingKeys33_3E5B1FD9E1A042D733106E6EC5DC0833LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit015TotalWiFiUploadD0V10CodingKeys33_9F0F23E401EBCD4A8D755EE82340ADFBLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit016SignpostIntervalD0V10CodingKeys33_1BBB850FD69063EC4449A298AC57971BLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit017LogicalDiskWritesD0V10CodingKeys33_30907B10E3E4D626899DDF05BEC7AEE6LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit017TotalWiFiDownloadD0V10CodingKeys33_A966F018041ED5938BCAC232008657ECLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit019TotalBackgroundTimeD0V10CodingKeys021_F28B0DC7DEAC9F9EE620L10C4C490394FLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit019TotalCellularUploadD0V10CodingKeys33_3B2E4DAC4FB8B7C28E5C7B8A8200A4C5LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit019TotalForegroundTimeD0V10CodingKeys33_BE47AB2988BDEA265855E5BDC626F717LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit020CPUInstructionsCountD0V10CodingKeys33_5B71F41DC98A6271721F92C58E806B59LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit020LocationActivityTimeD0V10CodingKeys33_359D6681CBFE71952A7BBF42B9EE6227LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit021ApplicationResumeTimeD0V10CodingKeys33_6065BAD8666BE30CCDD5AED2BA2E22C9LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit021BackgroundTerminationD0V10CodingKeys33_F6A7528DDA68B933ADF5711AE45D1B5ELLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit021CellularConditionTimeD0V10CodingKeys33_0A4D20088FAA6A69417AFFED54D53CE0LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit021ForegroundTerminationD0V10CodingKeys33_6335AE56C1A3DA4A6CE6FB467D896D79LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit021TotalCellularDownloadD0V10CodingKeys33_C3F8179C0A8D9850A4672B75EFE898E0LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit022TotalDiskSpaceCapacityD0V10CodingKeys33_6732B9030449A82B94553EEDA33CA538LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit024OptimizedTimeToFirstDrawD0V10CodingKeys025_9720B8D26652F761B9D78A28M6CAC096LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit024TotalBackgroundAudioTimeD0V10CodingKeys33_A81B65BC8208469D73F94D30535A43BFLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit027TotalBackgroundLocationTimeD0V10CodingKeys33_1A15AB88DD3AFD1EAC286D9FB0F76DBBLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit07CPUTimeD0V10CodingKeys33_C8E927E6AC5315CC5856EFFD49D6C1B5LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit07GPUTimeD0V10CodingKeys33_FED091B3587CADBAD2F3D4A502DEB70BLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit08HangTimeD0V10CodingKeys33_48885408AF7B71E97B38A7FBE249EF03LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit09HitchTimeD0V10CodingKeys011_2B5C7FD179J20A6A18C2E25E0EB7EAAA5LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit0D6ReportV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit0D6ReportV10StateEntryV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit0D6ReportV11EnvironmentV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit0D6ReportV13IntervalEntryV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit0D6ResultO10CodingKeys33_85E4DAA39F87A1627E572936E3D697BALLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit0D7ManagerC13ReportedStateV10CodingKeys33_5E7E076324A3935404D34BC4802B50B6LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit13CallStackTreeV10BinaryInfoV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit13CallStackTreeV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit14CallStackFrameV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit14HangDiagnosticV10CodingKeys33_D754F9606244B2052D94776CECDA492CLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit14SignpostRecordV10CodingKeys33_CFA734C2817824AF1AC1ECE1D3570FB2LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit15CallStackThreadV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit15CrashDiagnosticV10CodingKeys33_5164B9ABCAEFAB6F5E2B4457471C23A4LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit15CrashDiagnosticV25ObjectiveCExceptionReasonV10CodingKeys33_5164B9ABCAEFAB6F5E2B4457471C23A4LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit16DiagnosticReportV10CodingKeys33_6D2ED6D54C08653A1DFA592E99B6EC7DLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit16DiagnosticReportV11EnvironmentV10CodingKeys33_6D2ED6D54C08653A1DFA592E99B6EC7DLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit16DiagnosticResultO10CodingKeys33_0DDD74F52EA265B7459F16A348CA9023LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit19AppLaunchDiagnosticV10CodingKeys33_5C4DA93322D4DEAA97B6BD025B39EB39LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit21MeasurementCodingKeys33_E58E169AC6B3C82E3591BD903470FE3ALLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit22CPUExceptionDiagnosticV10CodingKeys33_EA4CA5603DCE70AF83DA4271940FF47DLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit22DateIntervalCodingKeys33_E58E169AC6B3C82E3591BD903470FE3ALLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit25MemoryExceptionDiagnosticV10CodingKeys33_C7ADAF7494F05F5888A10451DDE735EDLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit28DiskWriteExceptionDiagnosticV10CodingKeys33_0263926ED9650D63D957FED9469F9F83LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit9OSVersionV10CodingKeys33_81B4729B13564F0357B3F62CE4B9404ELLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit010PeakMemoryD0V10CodingKeys33_23FF6B91966BD0D6D0346FA0DD69FEA6LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit013TotalFileSizeD0V10CodingKeys33_8D807C669B46F938E9ECF0E96439C9A3LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit014ExtendedLaunchD0V10CodingKeys33_B3F851CF624E9C41766BCA88C121D88CLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit014MetalFrameRateD0V10CodingKeys33_99B455C6B4B40F0B5B5954E5EE5AC02ELLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit014PixelLuminanceD0V10CodingKeys33_E88C25336A14479CD52CF84AAB23826FLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit014TotalFileCountD0V10CodingKeys33_3C80CF88C6B3EBEF2DD8E0DC88F70D96LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit015ScrollHitchTimeD0V10CodingKeys33_03245610228668DEF28556E7C33FDCA3LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit015SuspendedMemoryD0V10CodingKeys33_FCBAE00CCA9D1CB3F9B28CA6502B2F90LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit015TimeToFirstDrawD0V10CodingKeys33_3E5B1FD9E1A042D733106E6EC5DC0833LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit015TotalWiFiUploadD0V10CodingKeys33_9F0F23E401EBCD4A8D755EE82340ADFBLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit016SignpostIntervalD0V10CodingKeys33_1BBB850FD69063EC4449A298AC57971BLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit017LogicalDiskWritesD0V10CodingKeys33_30907B10E3E4D626899DDF05BEC7AEE6LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit017TotalWiFiDownloadD0V10CodingKeys33_A966F018041ED5938BCAC232008657ECLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit019TotalBackgroundTimeD0V10CodingKeys021_F28B0DC7DEAC9F9EE620L10C4C490394FLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit019TotalCellularUploadD0V10CodingKeys33_3B2E4DAC4FB8B7C28E5C7B8A8200A4C5LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit019TotalForegroundTimeD0V10CodingKeys33_BE47AB2988BDEA265855E5BDC626F717LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit020CPUInstructionsCountD0V10CodingKeys33_5B71F41DC98A6271721F92C58E806B59LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit020LocationActivityTimeD0V10CodingKeys33_359D6681CBFE71952A7BBF42B9EE6227LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit021ApplicationResumeTimeD0V10CodingKeys33_6065BAD8666BE30CCDD5AED2BA2E22C9LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit021BackgroundTerminationD0V10CodingKeys33_F6A7528DDA68B933ADF5711AE45D1B5ELLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit021CellularConditionTimeD0V10CodingKeys33_0A4D20088FAA6A69417AFFED54D53CE0LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit021ForegroundTerminationD0V10CodingKeys33_6335AE56C1A3DA4A6CE6FB467D896D79LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit021TotalCellularDownloadD0V10CodingKeys33_C3F8179C0A8D9850A4672B75EFE898E0LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit022TotalDiskSpaceCapacityD0V10CodingKeys33_6732B9030449A82B94553EEDA33CA538LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit024OptimizedTimeToFirstDrawD0V10CodingKeys025_9720B8D26652F761B9D78A28M6CAC096LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit024TotalBackgroundAudioTimeD0V10CodingKeys33_A81B65BC8208469D73F94D30535A43BFLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit027TotalBackgroundLocationTimeD0V10CodingKeys33_1A15AB88DD3AFD1EAC286D9FB0F76DBBLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit07CPUTimeD0V10CodingKeys33_C8E927E6AC5315CC5856EFFD49D6C1B5LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit07GPUTimeD0V10CodingKeys33_FED091B3587CADBAD2F3D4A502DEB70BLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit08HangTimeD0V10CodingKeys33_48885408AF7B71E97B38A7FBE249EF03LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit09HitchTimeD0V10CodingKeys011_2B5C7FD179J20A6A18C2E25E0EB7EAAA5LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit0D6ReportV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit0D6ReportV10StateEntryV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit0D6ReportV11EnvironmentV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit0D6ReportV13IntervalEntryV10CodingKeys33_5982F6453949B66B162EC4AFA3502BB2LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit0D6ResultO10CodingKeys33_85E4DAA39F87A1627E572936E3D697BALLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit0D7ManagerC13ReportedStateV10CodingKeys33_5E7E076324A3935404D34BC4802B50B6LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit13CallStackTreeV10BinaryInfoV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit13CallStackTreeV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit14CallStackFrameV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit14HangDiagnosticV10CodingKeys33_D754F9606244B2052D94776CECDA492CLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit14SignpostRecordV10CodingKeys33_CFA734C2817824AF1AC1ECE1D3570FB2LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit15CallStackThreadV10CodingKeys33_33F473728CE5BBD307FD2F60B6B877F9LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit15CrashDiagnosticV10CodingKeys33_5164B9ABCAEFAB6F5E2B4457471C23A4LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit15CrashDiagnosticV25ObjectiveCExceptionReasonV10CodingKeys33_5164B9ABCAEFAB6F5E2B4457471C23A4LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit16DiagnosticReportV10CodingKeys33_6D2ED6D54C08653A1DFA592E99B6EC7DLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit16DiagnosticReportV11EnvironmentV10CodingKeys33_6D2ED6D54C08653A1DFA592E99B6EC7DLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit16DiagnosticResultO10CodingKeys33_0DDD74F52EA265B7459F16A348CA9023LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit19AppLaunchDiagnosticV10CodingKeys33_5C4DA93322D4DEAA97B6BD025B39EB39LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit21MeasurementCodingKeys33_E58E169AC6B3C82E3591BD903470FE3ALLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit22CPUExceptionDiagnosticV10CodingKeys33_EA4CA5603DCE70AF83DA4271940FF47DLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit22DateIntervalCodingKeys33_E58E169AC6B3C82E3591BD903470FE3ALLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit25MemoryExceptionDiagnosticV10CodingKeys33_C7ADAF7494F05F5888A10451DDE735EDLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit28DiskWriteExceptionDiagnosticV10CodingKeys33_0263926ED9650D63D957FED9469F9F83LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit9OSVersionV10CodingKeys33_81B4729B13564F0357B3F62CE4B9404ELLO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 9MetricKit0D6ReportV10StateEntryV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 9MetricKit0D6ReportV13IntervalEntryV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 9MetricKit0D6ResultO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 9MetricKit0D7ManagerC13ReportedStateV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 9MetricKit13CallStackTreeV10BinaryInfoV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 9MetricKit14CallStackFrameV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 9MetricKit14SignpostRecordV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 9MetricKit15CallStackThreadV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 9MetricKit16DiagnosticReportV
+ _symbolic _____y_____Say_____GG s18_DictionaryStorageC 9MetricKit20StateReportingDomainV AC0C6ReportV0E5EntryV
+ _symbolic _____y_____Say_____GG s18_DictionaryStorageC 9MetricKit20StateReportingDomainV AC0C7ManagerC08ReportedE0V
+ _symbolic _____y______G 9MetricKit9HistogramV6BucketV AA10SignalBarsC
+ _symbolic _____y______G ScS12ContinuationV 9MetricKit0B6ReportV
+ _symbolic _____y______G ScS12ContinuationV 9MetricKit16DiagnosticReportV
+ _symbolic _____y______GSg ScS12ContinuationV 9MetricKit0B6ReportV
+ _symbolic _____y______GSg ScS12ContinuationV 9MetricKit16DiagnosticReportV
+ _symbolic _____y_______G ScS12ContinuationV11YieldResultO 9MetricKit0D6ReportV
+ _symbolic _____y_______G ScS12ContinuationV11YieldResultO 9MetricKit16DiagnosticReportV
+ _symbolic _____y_______G ScS12ContinuationV15BufferingPolicyO 9MetricKit0D6ReportV
+ _symbolic _____y_______G ScS12ContinuationV15BufferingPolicyO 9MetricKit16DiagnosticReportV
+ _symbolic _____y__________G s18_DictionaryStorageC 10Foundation4UUIDV 9MetricKit13CallStackTreeV10BinaryInfoV
+ _symbolic _____y_____y______GG s23_ContiguousArrayStorageC 9MetricKit9HistogramV6BucketV AC10SignalBarsC
+ _symbolic _____yxG 10Foundation11MeasurementV
+ _symbolic _____yytG 2os21OSAllocatedUnfairLockV
+ _symbolic _____yyt_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
+ _symbolic x
+ _symbolic ypSg
+ _type_layout_string 9MetricKit014ExtendedLaunchA0V
+ _type_layout_string 9MetricKit014TotalFileCountA0V
+ _type_layout_string 9MetricKit015TimeToFirstDrawA0V
+ _type_layout_string 9MetricKit020CPUInstructionsCountA0V
+ _type_layout_string 9MetricKit021ApplicationResumeTimeA0V
+ _type_layout_string 9MetricKit021BackgroundTerminationA0V
+ _type_layout_string 9MetricKit021CellularConditionTimeA0V
+ _type_layout_string 9MetricKit021ForegroundTerminationA0V
+ _type_layout_string 9MetricKit024OptimizedTimeToFirstDrawA0V
+ _type_layout_string 9MetricKit08HangTimeA0V
+ _type_layout_string 9MetricKit0A5GroupV
+ _type_layout_string 9MetricKit0A6ReportV11EnvironmentV
+ _type_layout_string 9MetricKit0A7ManagerC15LaunchTaskErrorV
+ _type_layout_string 9MetricKit12LaunchTaskIDV
+ _type_layout_string 9MetricKit12_FeatureFlagV
+ _type_layout_string 9MetricKit13CallStackTreeV
+ _type_layout_string 9MetricKit15CallStackThreadV
+ _type_layout_string 9MetricKit15CrashDiagnosticV
+ _type_layout_string 9MetricKit15CrashDiagnosticV17TerminationReasonV
+ _type_layout_string 9MetricKit15CrashDiagnosticV25ObjectiveCExceptionReasonV
+ _type_layout_string 9MetricKit16DiagnosticReportV11EnvironmentV
+ _type_layout_string 9MetricKit20StateReportingDomainV
+ _type_layout_string 9MetricKit25MemoryExceptionDiagnosticV
+ _type_layout_string 9MetricKit9OSVersionV
+ _type_layout_string So11NSDimensionCRbzl9MetricKit9HistogramVyxG
+ _type_layout_string So16os_unfair_lock_sV
- -[MXDiagnosticPayload initWithTimeStampBegin:withTimeStampEnd:withDiagnostics:]
- GCC_except_table0
- ___23-[MXMetricManager init]_block_invoke
- ___23-[MXMetricManager init]_block_invoke.cold.1
- ___block_literal_global.45
- ___block_literal_global.50
- _objc_msgSend$initWithTimeStampBegin:withTimeStampEnd:withDiagnostics:
- _objc_msgSend$invalidate
CStrings:
+ "' for dimension "
+ ") must be >= 'begin' ("
+ "Calling registerClient (legacy)"
+ "Calling registerClientWithStateAwareDomains:@[]"
+ "Connection stored in ivar: %{public}@"
+ "ContextualizedData"
+ "DateInterval 'end' ("
+ "MXIntervalMetricData cannot be decoded by non-keyed archivers"
+ "MXIntervalMetricData cannot be encoded by non-keyed archivers"
+ "MXMetricManager initWithStateAware:%{bool}d"
+ "MXReportedState cannot be decoded by non-keyed archivers"
+ "MXReportedState cannot be encoded by non-keyed archivers"
+ "MXReportedState requires domain and label"
+ "MXStateMetricData cannot be decoded by non-keyed archivers"
+ "MXStateMetricData cannot be encoded by non-keyed archivers"
+ "MXStateMetricData requires reportedState"
+ "MetricManager"
+ "No valid diagnostic case found"
+ "No valid metric case found"
+ "Sending domains via XPC: %{public}@"
+ "SourceManager"
+ "Swift feature not active"
+ "Unknown unit symbol '"
+ "_updateStateReportingDomainsViaXPC called with %lu domains: %{public}@"
+ "abnormal"
+ "abnormalTerminationCount"
+ "activeDrawingDuration"
+ "activeDrawingDurationSeconds"
+ "activeStates"
+ "appLaunchDiagnostic"
+ "applicationResponsiveness"
+ "applicationResumeTimeMetric"
+ "average"
+ "averageFramePerSecond"
+ "backgroundTerminationMetric"
+ "badAccess"
+ "badAccessTerminationCount"
+ "begin"
+ "bestAccuracy"
+ "bestAccuracyForNavigation"
+ "binaryFileSize"
+ "binaryInfo"
+ "cacheFolderSize"
+ "callStackArray"
+ "capacity"
+ "cellularCondition"
+ "cellularConditionTimeMetric"
+ "childIndices"
+ "cloneSize"
+ "com.apple.MetricKitSource"
+ "com.apple.metrickit.encodingFormat"
+ "cpuExceptionDiagnostic"
+ "cpuInstructionsCountMetric"
+ "cpuTime"
+ "cpuTimeMetric"
+ "crashDiagnostic"
+ "dataFileSize"
+ "diskWriteExceptionDiagnostic"
+ "domain"
+ "domain:(\\d+)\\s+code:0x([0-9A-Fa-f]+)"
+ "durationSeconds"
+ "end"
+ "endTimestamp"
+ "environment"
+ "extendedLaunchMetric"
+ "fileLock"
+ "fileLockTerminationCount"
+ "flatFrames"
+ "foregroundTerminationMetric"
+ "frameCount"
+ "framesPerSecond"
+ "framework"
+ "gpuTimeMetric"
+ "hangDiagnostic"
+ "hangTimeMetric"
+ "hasExceededStateLimit"
+ "highCPUTerminationCount"
+ "hitchTimeMetric"
+ "illegalInstruction"
+ "illegalInstructionTerminationCount"
+ "interval"
+ "intervalEntries"
+ "intervalMetrics"
+ "label"
+ "layerName"
+ "locationActivity"
+ "locationActivityTimeMetric"
+ "logicalDiskWritesMetric"
+ "logicalWrites"
+ "lowerBound"
+ "memoryExceptionDiagnostic"
+ "memoryExceptionDiagnosticContainers"
+ "memoryLimitTerminationCount"
+ "metalFrameRate"
+ "metalFrameRateMetric"
+ "metalFrameRateMetrics"
+ "normalTerminationCount"
+ "oneHundredMeter"
+ "oneKilometer"
+ "optimizedTimeToFirstDrawMetric"
+ "osBuildNumber"
+ "osPlatform"
+ "osVersionNumber"
+ "parentIndex"
+ "peakMemoryMetric"
+ "pixelLuminanceMetric"
+ "ratio"
+ "reportedState"
+ "reportedStateData"
+ "rootFrameIndices"
+ "scrollHitchTimeMetric"
+ "signpostDuration"
+ "signpostIntervalMetric"
+ "spaceUsed"
+ "stableContext"
+ "stableMetadata"
+ "stableStateContext"
+ "startTimestamp"
+ "stateEntries"
+ "stateMetrics"
+ "states"
+ "suspendedMemoryMetric"
+ "systemPressureTerminationCount"
+ "taskTimeout"
+ "taskTimeoutTerminationCount"
+ "tenMeters"
+ "terminationCategory"
+ "threadIndex"
+ "threadMetadata"
+ "threeKilometers"
+ "timeRange"
+ "timeToFirstDrawMetric"
+ "timestamp"
+ "totalAnimationTime"
+ "totalBackgroundAudioTimeMetric"
+ "totalBackgroundLocationTimeMetric"
+ "totalBackgroundTimeMetric"
+ "totalBytesWritten"
+ "totalCellularDownloadMetric"
+ "totalCellularUploadMetric"
+ "totalDiskSpaceCapacityMetric"
+ "totalFileCountMetric"
+ "totalFileSizeMetric"
+ "totalForegroundTimeMetric"
+ "totalHitchTime"
+ "totalScrollHitchTime"
+ "totalScrollTime"
+ "totalWiFiDownloadMetric"
+ "totalWiFiUploadMetric"
+ "upperBound"
+ "value"
+ "values"
+ "watchdog"
+ "watchdogTerminationCount"
- ".cxx_destruct"
- "@\"MXAnimationMetric\""
- "@\"MXAppExitMetric\""
- "@\"MXAppLaunchMetric\""
- "@\"MXAppResponsivenessMetric\""
- "@\"MXAppRunTimeMetric\""
- "@\"MXAverage\""
- "@\"MXBackgroundExitData\""
- "@\"MXCPUMetric\""
- "@\"MXCallStackTree\""
- "@\"MXCellularConditionMetric\""
- "@\"MXCrashDiagnosticObjectiveCExceptionReason\""
- "@\"MXDiskIOMetric\""
- "@\"MXDiskSpaceUsageMetric\""
- "@\"MXDisplayMetric\""
- "@\"MXForegroundExitData\""
- "@\"MXGPUMetric\""
- "@\"MXHistogram\""
- "@\"MXLocationActivityMetric\""
- "@\"MXMemoryMetric\""
- "@\"MXMetaData\""
- "@\"MXNetworkTransferMetric\""
- "@\"MXSignpostIntervalData\""
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSHashTable\""
- "@\"NSMeasurement\""
- "@\"NSMeasurementFormatter\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSString\""
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@100@0:8@16@24@32i40@44@52@60@68@76@84@92"
- "@108@0:8@16@24@32i40@44@52@60@68@76@84@92@100"
- "@112@0:8Q16Q24Q32Q40Q48Q56Q64Q72Q80Q88Q96Q104"
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@32@0:8@16@24"
- "@32@0:8@16q24"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24Q32"
- "@40@0:8@16q24d32"
- "@44@0:8@16@24@32i40"
- "@44@0:8@16B24@28@36"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24Q32@40"
- "@48@0:8d16q24d32@40"
- "@56@0:8@16@24@32@40@48"
- "@60@0:8@16@24@32i40@44@52"
- "@60@0:8@16B24@28@36@44@52"
- "@64@0:8@16@24@32@40@48@56"
- "@68@0:8@16@24@32@40@48@56B64"
- "@68@0:8@16@24@32i40@44@52@60"
- "@68@0:8@16@24@32i40@44@52q60"
- "@72@0:8@16@24@32@40@48@56@64"
- "@72@0:8@16@24@32@40@48@56i64B68"
- "@72@0:8@16@24@32@40@48Q56@64"
- "@72@0:8Q16Q24Q32Q40Q48Q56Q64"
- "@80@0:8@16Q24@32Q40@48@56@64@72"
- "@88@0:8@16@24@32@40@48@56@64@72@80"
- "@96@0:8@16@24@32@40@48@56@64@72@80@88"
- "B"
- "B16@0:8"
- "B32@0:8@16^@24"
- "MXAnimationMetric"
- "MXAppExitMetric"
- "MXAppLaunchDiagnostic"
- "MXAppLaunchMetric"
- "MXAppResponsivenessMetric"
- "MXAppRunTimeMetric"
- "MXAverage"
- "MXBackgroundExitData"
- "MXCPUExceptionDiagnostic"
- "MXCPUMetric"
- "MXCallStackFrame"
- "MXCallStackThread"
- "MXCallStackTree"
- "MXCellularConditionMetric"
- "MXCrashDiagnostic"
- "MXCrashDiagnosticObjectiveCExceptionReason"
- "MXDiagnostic"
- "MXDiagnosticPayload"
- "MXDiskIOMetric"
- "MXDiskSpaceUsageMetric"
- "MXDiskWriteExceptionDiagnostic"
- "MXDisplayMetric"
- "MXForegroundExitData"
- "MXGPUMetric"
- "MXHangDiagnostic"
- "MXHistogram"
- "MXHistogramBucket"
- "MXLocationActivityMetric"
- "MXMemoryMetric"
- "MXMetaData"
- "MXMetric"
- "MXMetricManager"
- "MXMetricPayload"
- "MXNetworkTransferMetric"
- "MXSignpostIntervalData"
- "MXSignpostMetric"
- "MXSignpostRecord"
- "MXUnitAveragePixelLuminance"
- "MXUnitSignalBars"
- "MXXPCClient"
- "MXXPCServer"
- "MetricKit"
- "NSCoding"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T@\"MXAnimationMetric\",&,V_animationMetrics"
- "T@\"MXAppExitMetric\",&,V_applicationExitMetrics"
- "T@\"MXAppLaunchMetric\",&,V_applicationLaunchMetrics"
- "T@\"MXAppResponsivenessMetric\",&,V_applicationResponsivenessMetrics"
- "T@\"MXAppRunTimeMetric\",&,V_applicationTimeMetrics"
- "T@\"MXAverage\",R,V_averageMemory"
- "T@\"MXAverage\",R,V_averagePixelLuminance"
- "T@\"MXAverage\",R,V_averageSuspendedMemory"
- "T@\"MXBackgroundExitData\",R,V_backgroundExitData"
- "T@\"MXCPUMetric\",&,V_cpuMetrics"
- "T@\"MXCallStackTree\",R,V_callStackTree"
- "T@\"MXCellularConditionMetric\",&,V_cellularConditionMetrics"
- "T@\"MXCrashDiagnosticObjectiveCExceptionReason\",R,V_exceptionReason"
- "T@\"MXDiskIOMetric\",&,V_diskIOMetrics"
- "T@\"MXDiskSpaceUsageMetric\",&,V_diskSpaceUsageMetrics"
- "T@\"MXDisplayMetric\",&,V_displayMetrics"
- "T@\"MXForegroundExitData\",R,V_foregroundExitData"
- "T@\"MXGPUMetric\",&,V_gpuMetrics"
- "T@\"MXHistogram\",R,V_histogrammedApplicationHangTime"
- "T@\"MXHistogram\",R,V_histogrammedApplicationResumeTime"
- "T@\"MXHistogram\",R,V_histogrammedCellularConditionTime"
- "T@\"MXHistogram\",R,V_histogrammedExtendedLaunch"
- "T@\"MXHistogram\",R,V_histogrammedOptimizedTimeToFirstDraw"
- "T@\"MXHistogram\",R,V_histogrammedSignpostDuration"
- "T@\"MXHistogram\",R,V_histogrammedTimeToFirstDraw"
- "T@\"MXLocationActivityMetric\",&,V_locationActivityMetrics"
- "T@\"MXMemoryMetric\",&,V_memoryMetrics"
- "T@\"MXMetaData\",&,V_metaData"
- "T@\"MXMetricManager\",R"
- "T@\"MXNetworkTransferMetric\",&,V_networkTransferMetrics"
- "T@\"MXSignpostIntervalData\",R,V_signpostIntervalData"
- "T@\"MXUnitAveragePixelLuminance\",R,C"
- "T@\"MXUnitSignalBars\",R,C"
- "T@\"NSArray\",&,V_pastDiagnosticPayloads"
- "T@\"NSArray\",&,V_pastPayloads"
- "T@\"NSArray\",&,V_signpostData"
- "T@\"NSArray\",&,V_signpostMetrics"
- "T@\"NSArray\",&,V_subFrames"
- "T@\"NSArray\",C,V_arguments"
- "T@\"NSArray\",R,V_appLaunchDiagnostics"
- "T@\"NSArray\",R,V_callStackThreads"
- "T@\"NSArray\",R,V_cpuExceptionDiagnostics"
- "T@\"NSArray\",R,V_crashDiagnostics"
- "T@\"NSArray\",R,V_diskWriteExceptionDiagnostics"
- "T@\"NSArray\",R,V_hangDiagnostics"
- "T@\"NSArray\",R,V_histogramData"
- "T@\"NSArray\",R,V_topFrames"
- "T@\"NSDate\",C,V_beginTimeStamp"
- "T@\"NSDate\",C,V_endTimeStamp"
- "T@\"NSDate\",R,V_timeStampBegin"
- "T@\"NSDate\",R,V_timeStampEnd"
- "T@\"NSEnumerator\",R"
- "T@\"NSHashTable\",&,N,V_subscribers"
- "T@\"NSMeasurement\",C,V_duration"
- "T@\"NSMeasurement\",R,V_averageMeasurement"
- "T@\"NSMeasurement\",R,V_bucketEnd"
- "T@\"NSMeasurement\",R,V_bucketStart"
- "T@\"NSMeasurement\",R,V_cumulativeBackgroundAudioTime"
- "T@\"NSMeasurement\",R,V_cumulativeBackgroundLocationTime"
- "T@\"NSMeasurement\",R,V_cumulativeBackgroundTime"
- "T@\"NSMeasurement\",R,V_cumulativeBestAccuracyForNavigationTime"
- "T@\"NSMeasurement\",R,V_cumulativeBestAccuracyTime"
- "T@\"NSMeasurement\",R,V_cumulativeCPUInstructions"
- "T@\"NSMeasurement\",R,V_cumulativeCPUTime"
- "T@\"NSMeasurement\",R,V_cumulativeCellularDownload"
- "T@\"NSMeasurement\",R,V_cumulativeCellularUpload"
- "T@\"NSMeasurement\",R,V_cumulativeForegroundTime"
- "T@\"NSMeasurement\",R,V_cumulativeGPUTime"
- "T@\"NSMeasurement\",R,V_cumulativeHitchTimeRatio"
- "T@\"NSMeasurement\",R,V_cumulativeHundredMetersAccuracyTime"
- "T@\"NSMeasurement\",R,V_cumulativeKilometerAccuracyTime"
- "T@\"NSMeasurement\",R,V_cumulativeLogicalWrites"
- "T@\"NSMeasurement\",R,V_cumulativeNearestTenMetersAccuracyTime"
- "T@\"NSMeasurement\",R,V_cumulativeThreeKilometersAccuracyTime"
- "T@\"NSMeasurement\",R,V_cumulativeWifiDownload"
- "T@\"NSMeasurement\",R,V_cumulativeWifiUpload"
- "T@\"NSMeasurement\",R,V_hangDuration"
- "T@\"NSMeasurement\",R,V_hitchTimeRatio"
- "T@\"NSMeasurement\",R,V_launchDuration"
- "T@\"NSMeasurement\",R,V_peakMemoryUsage"
- "T@\"NSMeasurement\",R,V_scrollHitchTimeRatio"
- "T@\"NSMeasurement\",R,V_totalBinaryFileSize"
- "T@\"NSMeasurement\",R,V_totalCPUTime"
- "T@\"NSMeasurement\",R,V_totalCacheFolderSize"
- "T@\"NSMeasurement\",R,V_totalCloneSize"
- "T@\"NSMeasurement\",R,V_totalDataFileSize"
- "T@\"NSMeasurement\",R,V_totalDiskSpaceCapacity"
- "T@\"NSMeasurement\",R,V_totalDiskSpaceUsedSize"
- "T@\"NSMeasurement\",R,V_totalSampledTime"
- "T@\"NSMeasurement\",R,V_totalWritesCaused"
- "T@\"NSMeasurementFormatter\",&,V_measurementFormatter"
- "T@\"NSNumber\",R,V_address"
- "T@\"NSNumber\",R,V_exceptionCode"
- "T@\"NSNumber\",R,V_exceptionType"
- "T@\"NSNumber\",R,V_offsetInBinary"
- "T@\"NSNumber\",R,V_sampleCount"
- "T@\"NSNumber\",R,V_signal"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_iVarQueue"
- "T@\"NSObject<OS_os_log>\",&,N,V_managerLogHandle"
- "T@\"NSObject<OS_os_log>\",&,V_logHandle"
- "T@\"NSString\",&,V_applicationBuildVersion"
- "T@\"NSString\",&,V_bundleIdentifier"
- "T@\"NSString\",&,V_deviceType"
- "T@\"NSString\",&,V_osVersion"
- "T@\"NSString\",&,V_platformArchitecture"
- "T@\"NSString\",&,V_regionFormat"
- "T@\"NSString\",C,V_category"
- "T@\"NSString\",C,V_className"
- "T@\"NSString\",C,V_composedMessage"
- "T@\"NSString\",C,V_exceptionName"
- "T@\"NSString\",C,V_exceptionType"
- "T@\"NSString\",C,V_formatString"
- "T@\"NSString\",C,V_name"
- "T@\"NSString\",C,V_subsystem"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,V_applicationVersion"
- "T@\"NSString\",R,V_binaryName"
- "T@\"NSString\",R,V_latestApplicationVersion"
- "T@\"NSString\",R,V_signpostCategory"
- "T@\"NSString\",R,V_signpostName"
- "T@\"NSString\",R,V_terminationReason"
- "T@\"NSString\",R,V_virtualMemoryRegionInfo"
- "T@\"NSUUID\",R,V_binaryUUID"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "TB,R"
- "TB,R,V_attributedThread"
- "TB,R,V_callStackPerThread"
- "TB,R,V_includesMultipleApplicationVersions"
- "TB,V_checkedDiagnostics"
- "TB,V_checkedMetrics"
- "TB,V_errorRetrievingAppRecord"
- "TB,V_isInterval"
- "TB,V_isTestFlightApp"
- "TB,V_lowPowerModeEnabled"
- "TQ,R,V_bucketCount"
- "TQ,R,V_cumulativeAbnormalExitCount"
- "TQ,R,V_cumulativeAppWatchdogExitCount"
- "TQ,R,V_cumulativeBackgroundFetchCompletionTimeoutExitCount"
- "TQ,R,V_cumulativeBackgroundTaskAssertionTimeoutExitCount"
- "TQ,R,V_cumulativeBackgroundURLSessionCompletionTimeoutExitCount"
- "TQ,R,V_cumulativeBadAccessExitCount"
- "TQ,R,V_cumulativeCPUResourceLimitExitCount"
- "TQ,R,V_cumulativeIllegalInstructionExitCount"
- "TQ,R,V_cumulativeMemoryPressureExitCount"
- "TQ,R,V_cumulativeMemoryResourceLimitExitCount"
- "TQ,R,V_cumulativeNormalAppExitCount"
- "TQ,R,V_cumulativeSuspendedWithLockedFileExitCount"
- "TQ,R,V_totalBucketCount"
- "TQ,R,V_totalCount"
- "Td,N,R"
- "Td,R,V_standardDeviation"
- "Ti,N,V_metricToken"
- "Ti,V_pid"
- "Tq,R,N,V_hangType"
- "Tq,R,V_sampleCount"
- "Tq,R,V_totalBinaryFileCount"
- "Tq,R,V_totalDataFileCount"
- "UTF8String"
- "UUIDString"
- "_TtC9MetricKit15MXDateFormatter"
- "_address"
- "_animationMetrics"
- "_appLaunchDiagnostics"
- "_applicationBuildVersion"
- "_applicationExitMetrics"
- "_applicationLaunchMetrics"
- "_applicationResponsivenessMetrics"
- "_applicationTimeMetrics"
- "_applicationVersion"
- "_arguments"
- "_attributedThread"
- "_averageMeasurement"
- "_averageMeasurementFormatter"
- "_averageMemory"
- "_averagePixelLuminance"
- "_averageSuspendedMemory"
- "_backgroundExitData"
- "_beginTimeStamp"
- "_binaryName"
- "_binaryUUID"
- "_bucketCount"
- "_bucketEnd"
- "_bucketStart"
- "_bundleIdentifier"
- "_cachedPayloadAvailable"
- "_callStackPerThread"
- "_callStackThreads"
- "_callStackTree"
- "_category"
- "_cellularConditionMetrics"
- "_checkAndDeliverDiagnosticReports"
- "_checkAndDeliverMetricReports"
- "_checkedDiagnostics"
- "_checkedMetrics"
- "_className"
- "_composedMessage"
- "_connection"
- "_cpuExceptionDiagnostics"
- "_cpuMetrics"
- "_crashDiagnostics"
- "_createXPCConnection"
- "_cumulativeAbnormalExitCount"
- "_cumulativeAppWatchdogExitCount"
- "_cumulativeBackgroundAudioTime"
- "_cumulativeBackgroundFetchCompletionTimeoutExitCount"
- "_cumulativeBackgroundLocationTime"
- "_cumulativeBackgroundTaskAssertionTimeoutExitCount"
- "_cumulativeBackgroundTime"
- "_cumulativeBackgroundURLSessionCompletionTimeoutExitCount"
- "_cumulativeBadAccessExitCount"
- "_cumulativeBestAccuracyForNavigationTime"
- "_cumulativeBestAccuracyTime"
- "_cumulativeCPUInstructions"
- "_cumulativeCPUResourceLimitExitCount"
- "_cumulativeCPUTime"
- "_cumulativeCellularDownload"
- "_cumulativeCellularUpload"
- "_cumulativeForegroundTime"
- "_cumulativeGPUTime"
- "_cumulativeHitchTimeRatio"
- "_cumulativeHundredMetersAccuracyTime"
- "_cumulativeIllegalInstructionExitCount"
- "_cumulativeKilometerAccuracyTime"
- "_cumulativeLogicalWrites"
- "_cumulativeMemoryPressureExitCount"
- "_cumulativeMemoryResourceLimitExitCount"
- "_cumulativeNearestTenMetersAccuracyTime"
- "_cumulativeNormalAppExitCount"
- "_cumulativeSuspendedWithLockedFileExitCount"
- "_cumulativeThreeKilometersAccuracyTime"
- "_cumulativeWifiDownload"
- "_cumulativeWifiUpload"
- "_defaultDescriptionForMXErrorCode:"
- "_deviceType"
- "_diskIOMetrics"
- "_diskSpaceUsageMetrics"
- "_diskWriteExceptionDiagnostics"
- "_displayMetrics"
- "_duration"
- "_endTimeStamp"
- "_errorRetrievingAppRecord"
- "_exceptionCode"
- "_exceptionName"
- "_exceptionReason"
- "_exceptionType"
- "_foregroundExitData"
- "_formatString"
- "_gpuMetrics"
- "_hangDiagnostics"
- "_hangDuration"
- "_hangType"
- "_hangTypeForHangTypeString:"
- "_histogramBucketFormatter"
- "_histogramData"
- "_histogrammedApplicationHangTime"
- "_histogrammedApplicationResumeTime"
- "_histogrammedCellularConditionTime"
- "_histogrammedExtendedLaunch"
- "_histogrammedOptimizedTimeToFirstDraw"
- "_histogrammedSignpostDuration"
- "_histogrammedTimeToFirstDraw"
- "_hitchTimeRatio"
- "_iVarQueue"
- "_includesMultipleApplicationVersions"
- "_isInterval"
- "_isTestFlightApp"
- "_latestApplicationVersion"
- "_launchDuration"
- "_locationActivityMetrics"
- "_logHandle"
- "_lowPowerModeEnabled"
- "_managerLogHandle"
- "_measurementFormatter"
- "_memoryMetrics"
- "_metaData"
- "_metricToken"
- "_name"
- "_networkTransferMetrics"
- "_offsetInBinary"
- "_osVersion"
- "_pastDiagnosticPayloads"
- "_pastPayloads"
- "_peakMemoryUsage"
- "_pid"
- "_platformArchitecture"
- "_regionFormat"
- "_sampleCount"
- "_scrollHitchTimeRatio"
- "_signal"
- "_signpostCategory"
- "_signpostData"
- "_signpostIntervalData"
- "_signpostMetrics"
- "_signpostName"
- "_standardDeviation"
- "_subFrames"
- "_subscribers"
- "_subsystem"
- "_terminationReason"
- "_timeStampBegin"
- "_timeStampEnd"
- "_topFrames"
- "_totalBinaryFileCount"
- "_totalBinaryFileSize"
- "_totalBucketCount"
- "_totalCPUTime"
- "_totalCacheFolderSize"
- "_totalCloneSize"
- "_totalCount"
- "_totalDataFileCount"
- "_totalDataFileSize"
- "_totalDiskSpaceCapacity"
- "_totalDiskSpaceUsedSize"
- "_totalSampledTime"
- "_totalWritesCaused"
- "_virtualMemoryRegionInfo"
- "addEntriesFromDictionary:"
- "addObject:"
- "addObjectsFromArray:"
- "addSubscriber:"
- "allowsKeyedCoding"
- "arrayWithArray:"
- "attributedThread"
- "averageMeasurement"
- "baseUnit"
- "boolValue"
- "bucketEnumerator"
- "checkedDiagnostics"
- "checkedMetrics"
- "connection"
- "containsObject:"
- "contentsAtPath:"
- "contentsOfDirectoryAtPath:error:"
- "copy"
- "countByEnumeratingWithState:objects:count:"
- "cumulativeHitchTimeRatio"
- "d"
- "d16@0:8"
- "dataWithJSONObject:options:error:"
- "dateFromString:"
- "dateFromString:format:"
- "dateTruncatedToMinute:"
- "dealloc"
- "decodeBoolForKey:"
- "decodeDoubleForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultManager"
- "deliverDiagnosticPayload:"
- "deliverMetricPayload:"
- "descriptionWithLocale:"
- "dictionaryWithObjects:forKeys:count:"
- "didReceiveDiagnosticPayloads:"
- "didReceiveMetricPayloads:"
- "doubleValue"
- "earlierDate:"
- "encodeBool:forKey:"
- "encodeDouble:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorRetrievingAppRecord"
- "errorWithDomain:code:userInfo:"
- "errorWithMXErrorCode:"
- "exceptionReason"
- "exportedInterface"
- "extendLaunchMeasurementForTaskID:error:"
- "failWithError:"
- "finishExtendedLaunchMeasurementForTaskID:error:"
- "hangTypeString"
- "histogramData"
- "histogrammedApplicationHangTime"
- "histogrammedApplicationResumeTime"
- "histogrammedCellularConditionTime"
- "histogrammedOptimizedTimeToFirstDraw"
- "histogrammedSignpostDuration"
- "histogrammedTimeToFirstDraw"
- "i"
- "i16@0:8"
- "iVarQueue"
- "init"
- "initWithAppResponsivenessData:"
- "initWithAppResponsivenessHangData:spinData:"
- "initWithAppVersion:withMutipleAppVersions:withTimeStampBegin:withTimeStampEnd:"
- "initWithAveragePictureLevel:"
- "initWithBinaryName:binaryUUID:address:binaryOffset:sampleCount:withDepth:subFrameArray:"
- "initWithBucketStart:bucketEnd:bucketCount:"
- "initWithCellularConditionTime:"
- "initWithCoder:"
- "initWithCoefficient:"
- "initWithComposedMessage:formatString:arguments:type:className:exceptionName:"
- "initWithCumulativeBestAccuracyTimeMeasurement:cumulativeBestAccuracyForNavigationTimeMeasurement:nearestTenMetersAccuracyTimeMeasurement:hundredMetersAccuracyTimeMeasurement:kilometerAccuracyTimeMeasurement:threeKilometerAccuracyTimeMeasurement:"
- "initWithCumulativeCPUTimeMeasurement:"
- "initWithCumulativeCPUTimeMeasurement:withCumulativeCPUInstructions:"
- "initWithCumulativeCPUTimeMeasurement:withCumulativeCPUInstructions:withCumulativeForegroundCPUTimeMeasurement:withCumulativeBackgroundCPUTimeMeasurement:"
- "initWithCumulativeForegroundTimeMeasurement:cumulativeBackgroundTimeMeasurement:cumulativeBackgroundAudioTimeMeasurement:cumulativeBackgroundLocationTimeMeasurement:"
- "initWithCumulativeGPUTimeMeasurement:"
- "initWithCumulativeLogicalWritesMeasurement:"
- "initWithCumulativeWifiUploadMeasurement:cumulativeWifiDownloadMeasurement:cumulativeCellularUploadMeasurement:cumulativeCellularDownloadMeasurement:"
- "initWithDomain:code:userInfo:"
- "initWithDoubleValue:sampleCount:standardDeviation:unit:"
- "initWithDoubleValue:unit:"
- "initWithForegroundExitData:backgroundExitData:"
- "initWithGlitchTimeRatio:"
- "initWithHistogramBucketData:"
- "initWithHistogramDurationData:withCumulativeCPUTime:withAverageMemory:withCumulativeLogicalWrites:"
- "initWithHistogramDurationData:withCumulativeCPUTime:withAverageMemory:withCumulativeLogicalWrites:withCumulativeHitchTimeRatio:"
- "initWithHistogramDurationData:withCumulativeCPUTime:withPeakMemory:withAverageMemory:withCumulativeLogicalWrites:"
- "initWithHitchTimeRatio:perceivedHitchTimeRatio:"
- "initWithLaunchTimeData:withResumeTimeData:"
- "initWithLaunchTimeData:withResumeTimeData:withActivationTimeData:"
- "initWithLaunchTimeData:withResumeTimeData:withActivationTimeData:withExtendedLaunchTimeData:"
- "initWithLocaleIdentifier:"
- "initWithMachServiceName:options:"
- "initWithMeasurement:sampleCount:standardDeviation:"
- "initWithMetaData:applicationVersion:"
- "initWithMetaData:applicationVersion:callStack:hangDuration:"
- "initWithMetaData:applicationVersion:callStack:launchDuration:"
- "initWithMetaData:applicationVersion:callStack:totalCpuTime:totalSampledTime:"
- "initWithMetaData:applicationVersion:signpostData:andPID:"
- "initWithMetaData:applicationVersion:signpostData:pid:callStack:hangDuration:"
- "initWithMetaData:applicationVersion:signpostData:pid:callStack:hangDuration:hangType:"
- "initWithMetaData:applicationVersion:signpostData:pid:callStack:launchDuration:"
- "initWithMetaData:applicationVersion:signpostData:pid:callStack:totalCpuTime:totalSampledTime:"
- "initWithMetaData:applicationVersion:signpostData:pid:terminationReason:applicationSpecificInfo:virtualMemoryRegionInfo:exceptionType:exceptionCode:exceptionReason:signal:stackTrace:"
- "initWithMetaData:applicationVersion:signpostData:pid:terminationReason:applicationSpecificInfo:virtualMemoryRegionInfo:exceptionType:exceptionCode:signal:stackTrace:"
- "initWithMetaData:applicationVersion:signpostData:pid:totalWritesCaused:stackTrace:"
- "initWithMetaData:applicationVersion:terminationReason:applicationSpecificInfo:virtualMemoryRegionInfo:exceptionType:exceptionCode:signal:stackTrace:"
- "initWithMetaData:applicationVersion:totalWritesCaused:stackTrace:"
- "initWithNormalAppExitCount:memoryResourceLimitExitCount:cpuResourceLimitExitCount:badAccessExitCount:abnormalExitCount:illegalInstructionExitCount:appWatchDogExitCount:"
- "initWithNormalAppExitCount:memoryResourceLimitExitCount:cpuResourceLimitExitCount:badAccessExitCount:abnormalExitCount:illegalInstructionExitCount:appWatchDogExitCount:cumulativeSuspendedWithLockedFileExitCount:cumulativeBackgroundTaskAssertionTimeoutExitCount:"
- "initWithNormalAppExitCount:memoryResourceLimitExitCount:cpuResourceLimitExitCount:memoryPressureExitCount:badAccessExitCount:abnormalExitCount:illegalInstructionExitCount:appWatchDogExitCount:cumulativeSuspendedWithLockedFileExitCount:cumulativeBackgroundTaskAssertionTimeoutExitCount:"
- "initWithNormalAppExitCount:memoryResourceLimitExitCount:cpuResourceLimitExitCount:memoryPressureExitCount:badAccessExitCount:abnormalExitCount:illegalInstructionExitCount:appWatchDogExitCount:cumulativeSuspendedWithLockedFileExitCount:cumulativeBackgroundTaskAssertionTimeoutExitCount:cumulativeBackgroundURLSessionCompletionTimeoutExitCount:cumulativeBackgroundFetchCompletionTimeoutExitCount:"
- "initWithNormalAppExitCount:withMemoryResourceLimitExitCount:withCPUResourceLimitExitCount:withBadAccessExitCount:withAbnormalExitCount:withIllegalInstructionExitCount:withAppWatchDogExitCount:"
- "initWithPayloadData:withMutipleAppVersions:withTimeStampBegin:withTimeStampEnd:withMetaData:withMetrics:"
- "initWithPeakMemoryUsageMeasurement:averageMemoryUsageMeasurement:"
- "initWithRegionFormat:osVersion:deviceType:appBuildVersion:"
- "initWithRegionFormat:osVersion:deviceType:appBuildVersion:bundleID:"
- "initWithRegionFormat:osVersion:deviceType:appBuildVersion:platformArchitecture:"
- "initWithRegionFormat:osVersion:deviceType:appBuildVersion:platformArchitecture:bundleID:"
- "initWithRegionFormat:osVersion:deviceType:appBuildVersion:platformArchitecture:bundleID:pid:isTestFlightApp:"
- "initWithSignpostName:withSignpostCategory:withTotalCount:withSignpostIntervalData:"
- "initWithSubSystem:category:name:beginTimeStamp:endTimeStamp:duration:isInterval:"
- "initWithSymbol:"
- "initWithSymbol:converter:"
- "initWithThreadArray:aggregatedByProcess:"
- "initWithTimeStampBegin:withTimeStampEnd:withDiagnostics:"
- "initWithTopCallStackFrames:isAttributedThread:"
- "initWithTotalBinaryFileSize:totalBinaryFileCount:totalDataFileSize:totalDataFileCount:totalCacheFolderSize:totalCloneSize:totalDiskSpaceUsedSize:totalDiskSpaceCapacity:"
- "intValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqualToString:"
- "isLowPowerModeEnabled"
- "isValidJSONObject:"
- "kilobytes"
- "laterDate:"
- "localizedStringForKey:value:table:"
- "logHandle"
- "mainBundle"
- "makeLogHandleWithCategory:"
- "managerLogHandle"
- "measurementByConvertingToUnit:"
- "measurementFormatter"
- "mergeDiagnosticsAtLocation:"
- "metricToken"
- "milliseconds"
- "mutableCopy"
- "numberFormatter"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectEnumerator"
- "objectForKeyedSubscript:"
- "offsetInBinary"
- "oneDay"
- "pastDiagnosticPayloads"
- "pastPayloads"
- "processInfo"
- "q"
- "q16@0:8"
- "q24@0:8@16"
- "raise:format:"
- "registerClient"
- "registrationProcessed"
- "remoteObjectProxy"
- "removeObject:"
- "removeObjectForKey:"
- "removeSubscriber:"
- "resume"
- "retrieveDiagnostics"
- "retrieveMetrics"
- "setAnimationMetrics:"
- "setApplicationBuildVersion:"
- "setApplicationExitMetrics:"
- "setApplicationLaunchMetrics:"
- "setApplicationResponsivenessMetrics:"
- "setApplicationTimeMetrics:"
- "setArguments:"
- "setBeginTimeStamp:"
- "setBundleIdentifier:"
- "setCategory:"
- "setCellularConditionMetrics:"
- "setCheckedDiagnostics:"
- "setCheckedMetrics:"
- "setClassName:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setComposedMessage:"
- "setConnection:"
- "setCpuMetrics:"
- "setDateFormat:"
- "setDeviceType:"
- "setDiskIOMetrics:"
- "setDiskSpaceUsageMetrics:"
- "setDisplayMetrics:"
- "setDuration:"
- "setEndTimeStamp:"
- "setErrorRetrievingAppRecord:"
- "setExceptionName:"
- "setExceptionType:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFormatString:"
- "setGpuMetrics:"
- "setIVarQueue:"
- "setIsInterval:"
- "setIsTestFlightApp:"
- "setLocale:"
- "setLocationActivityMetrics:"
- "setLogHandle:"
- "setLowPowerModeEnabled:"
- "setManagerLogHandle:"
- "setMaximumFractionDigits:"
- "setMeasurementFormatter:"
- "setMemoryMetrics:"
- "setMetaData:"
- "setMetricToken:"
- "setName:"
- "setNetworkTransferMetrics:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOsVersion:"
- "setPastDiagnosticPayloads:"
- "setPastPayloads:"
- "setPid:"
- "setPlatformArchitecture:"
- "setRegionFormat:"
- "setRemoteObjectInterface:"
- "setSignpostData:"
- "setSignpostMetrics:"
- "setSubFrames:"
- "setSubscribers:"
- "setSubsystem:"
- "setTimeZone:"
- "setUnitOptions:"
- "setUnitStyle:"
- "setValue:forKey:"
- "setWithObjects:"
- "sharedManager"
- "stringByAppendingPathComponent:"
- "stringFromDate:"
- "stringFromDate:format:"
- "stringFromMeasurement:"
- "stringValue"
- "subscribers"
- "supportsSecureCoding"
- "toDictionary"
- "topFrames"
- "totalBucketCount"
- "totalWritesCaused"
- "unarchivedObjectOfClass:fromData:error:"
- "unsignedIntegerValue"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "valueForKey:"
- "weakObjectsHashTable"

```
