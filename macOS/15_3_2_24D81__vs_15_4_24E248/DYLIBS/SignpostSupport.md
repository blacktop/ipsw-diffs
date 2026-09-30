## SignpostSupport

> `/System/Library/PrivateFrameworks/SignpostSupport.framework/Versions/A/SignpostSupport`

```diff

-146.2.0.0.0
-  __TEXT.__text: 0x4cbe8
-  __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_methlist: 0x58e4
-  __TEXT.__const: 0x1c4
-  __TEXT.__cstring: 0x16962
-  __TEXT.__oslogstring: 0xda5
-  __TEXT.__gcc_except_tab: 0x258
+151.7.0.0.0
+  __TEXT.__text: 0x53424
+  __TEXT.__auth_stubs: 0x3a0
+  __TEXT.__objc_methlist: 0x6304
+  __TEXT.__const: 0x238
+  __TEXT.__cstring: 0x16d9f
+  __TEXT.__oslogstring: 0xed6
+  __TEXT.__gcc_except_tab: 0x2b0
   __TEXT.__ustring: 0x3e
-  __TEXT.__unwind_info: 0x10c0
-  __TEXT.__objc_classname: 0xcc0
-  __TEXT.__objc_methname: 0xdf7e
-  __TEXT.__objc_methtype: 0xfb9
-  __TEXT.__objc_stubs: 0x8300
-  __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0x298
-  __DATA_CONST.__objc_classlist: 0x2d8
+  __TEXT.__unwind_info: 0x1280
+  __TEXT.__objc_classname: 0xd5b
+  __TEXT.__objc_methname: 0xeeac
+  __TEXT.__objc_methtype: 0x1172
+  __TEXT.__objc_stubs: 0x8d40
+  __DATA_CONST.__got: 0x308
+  __DATA_CONST.__const: 0x318
+  __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x58
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26a8
-  __DATA_CONST.__objc_superrefs: 0x270
-  __DATA_CONST.__objc_arraydata: 0x4e68
-  __AUTH_CONST.__auth_got: 0x1c0
-  __AUTH_CONST.__const: 0x1030
-  __AUTH_CONST.__cfstring: 0x17b20
-  __AUTH_CONST.__objc_const: 0xd5e0
-  __AUTH_CONST.__objc_arrayobj: 0x2e8
+  __DATA_CONST.__objc_selrefs: 0x2a08
+  __DATA_CONST.__objc_superrefs: 0x288
+  __DATA_CONST.__objc_arraydata: 0x4ea8
+  __AUTH_CONST.__auth_got: 0x1e0
+  __AUTH_CONST.__const: 0x11c0
+  __AUTH_CONST.__cfstring: 0x17fa0
+  __AUTH_CONST.__objc_const: 0xd938
+  __AUTH_CONST.__objc_arrayobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH.__objc_data: 0x17c0
-  __DATA.__objc_ivar: 0x888
-  __DATA.__data: 0xa88
-  __DATA.__bss: 0x340
+  __AUTH_CONST.__objc_intobj: 0x1b0
+  __AUTH.__objc_data: 0x18b0
+  __DATA.__objc_ivar: 0x904
+  __DATA.__data: 0xb48
+  __DATA.__bss: 0x370
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6DF0D2B2-11C1-3E6B-8EF3-C33BDD5D2E11
-  Functions: 2152
-  Symbols:   5054
-  CStrings:  8698
+  UUID: B2DECA4C-050A-39DA-AEDF-9636332B014D
+  Functions: 2333
+  Symbols:   5422
+  CStrings:  8951
 
Symbols:
+ +[SignpostAnimationInterval effectiveGlitchTimeRatioAdjustedVersion].cold.2
+ +[SignpostAnimationInterval overrunIntervalForOverrunQuery:frameLifetimes:]
+ +[SignpostAnimationInterval timeRatioMSPerSForOverrunQuery:frameLifetimes:applyPerceptionAdjustments:]
+ +[SignpostAnimationOverrunQuery nonFirstFrameContributedGlitches:]
+ +[SignpostAnimationOverrunQuery nonFirstFrameGlitches]
+ +[SignpostEvent _baseMCTForEvent:]
+ +[SignpostEvent(Serialization) serializationTypeNumber].cold.1
+ +[SignpostStreamEvent(Serialization) serializationTypeNumber].cold.1
+ +[SignpostSupportLogMessage(Serialization) serializationTypeNumber].cold.1
+ -[SignpostAggregation _handleCountSegment:].cold.1
+ -[SignpostAnimationAccumulatedState _handleFrameLifetime:isLong:isConcise:pidToNameDict:]
+ -[SignpostAnimationAccumulatedState _handleUpdateInterval:]
+ -[SignpostAnimationAccumulatedState allUpateIntervals]
+ -[SignpostAnimationInterval allDisplayIDs]
+ -[SignpostAnimationInterval contributingPidsForProcessName:]
+ -[SignpostAnimationInterval initWithFrameLifetimes:]
+ -[SignpostAnimationInterval overrunIntervals:]
+ -[SignpostAnimationOverrunQuery .cxx_destruct]
+ -[SignpostAnimationOverrunQuery contributingPID]
+ -[SignpostAnimationOverrunQuery displayID]
+ -[SignpostAnimationOverrunQuery init]
+ -[SignpostAnimationOverrunQuery isEqual:]
+ -[SignpostAnimationOverrunQuery overrunClass]
+ -[SignpostAnimationOverrunQuery overrunType]
+ -[SignpostAnimationOverrunQuery setContributingPID:]
+ -[SignpostAnimationOverrunQuery setDisplayID:]
+ -[SignpostAnimationOverrunQuery setOverrunClass:]
+ -[SignpostAnimationOverrunQuery setOverrunType:]
+ -[SignpostAnimationSubInterval .cxx_destruct]
+ -[SignpostAnimationSubInterval beginEvent]
+ -[SignpostAnimationSubInterval endEvent]
+ -[SignpostAnimationSubInterval isGeneratedInterval]
+ -[SignpostCAInstrumentationProcessor _handleCommitInterval:]
+ -[SignpostCAInstrumentationProcessor _handleFrameLatencyInterval:].cold.2
+ -[SignpostCAInstrumentationProcessor _handleFrameLifetimeBegin:isLong:]
+ -[SignpostCAInstrumentationProcessor _handleFrameLifetimeBegin:isLong:].cold.1
+ -[SignpostCAInstrumentationProcessor _handleFrameLifetimeInterval:].cold.1
+ -[SignpostCAInstrumentationProcessor _handleHIDInterval:].cold.2
+ -[SignpostCAInstrumentationProcessor _handleUpdateSequenceInterval:]
+ -[SignpostCAInstrumentationProcessor _removeOrphansFromQueue:preceedingEvent:]
+ -[SignpostCAInstrumentationProcessor _updatesMatchingFrameLifetime:]
+ -[SignpostCAInstrumentationProcessor gpuBlock]
+ -[SignpostCAInstrumentationProcessor handleSignpostEvent:].cold.1
+ -[SignpostCAInstrumentationProcessor handleSignpostEvent:].cold.2
+ -[SignpostCAInstrumentationProcessor queueCommitIntervals]
+ -[SignpostCAInstrumentationProcessor queueUpdateIntervals]
+ -[SignpostCAInstrumentationProcessor setGpuBlock:]
+ -[SignpostCAInstrumentationProcessor setUpdateIntervalBlock:]
+ -[SignpostCAInstrumentationProcessor updateIntervalBlock]
+ -[SignpostContextInfo initWithContextInfoEvent:contributor:]
+ -[SignpostEvent _argumentObjectWithPrefix:]
+ -[SignpostEvent _argumentObjectWithPrefix:].cold.1
+ -[SignpostEvent _argumentObjectWithPrefix:expectedClass:]
+ -[SignpostEvent _dataArgumentWithPrefix:]
+ -[SignpostEvent _numberArgumentWithPrefix:]
+ -[SignpostEvent _stringArgumentWithPrefix:]
+ -[SignpostEvent copyWithType:machContinuousTime:]
+ -[SignpostEvent copy]
+ -[SignpostEvent isGenerated]
+ -[SignpostEvent oppositeEventForIntervalWithDeltaSeconds:]
+ -[SignpostEvent setIsGenerated:]
+ -[SignpostFrameLatencyInterval frameLifetime]
+ -[SignpostFrameLatencyInterval isPotentiallyLong]
+ -[SignpostFrameLatencyInterval setFrameLifetime:]
+ -[SignpostFrameLifetimeInterval gpuInterval]
+ -[SignpostFrameLifetimeInterval hasRenderServerUpdateOnly]
+ -[SignpostFrameLifetimeInterval initWithInterval:contextArray:hidLatencyInterval:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:]
+ -[SignpostFrameLifetimeInterval initWithInterval:contextArray:hidLatencyInterval:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:].cold.1
+ -[SignpostFrameLifetimeInterval initWithInterval:contextArray:hidLatencyInterval:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:].cold.2
+ -[SignpostFrameLifetimeInterval initWithInterval:contextArray:hidLatencyInterval:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:].cold.3
+ -[SignpostFrameLifetimeInterval initWithInterval:contextArray:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:]
+ -[SignpostFrameLifetimeInterval initWithInterval:contextArray:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:].cold.1
+ -[SignpostFrameLifetimeInterval initWithInterval:swapID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:renderInterval:gpuInterval:]
+ -[SignpostFrameLifetimeInterval initWithInterval:swapID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:renderInterval:gpuInterval:].cold.1
+ -[SignpostFrameLifetimeInterval initWithInterval:swapID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:renderInterval:gpuInterval:].cold.2
+ -[SignpostFrameLifetimeInterval initWithInterval:swapID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:renderInterval:gpuInterval:].cold.3
+ -[SignpostFrameLifetimeInterval initWithInterval:swapID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:renderInterval:gpuInterval:].cold.4
+ -[SignpostFrameLifetimeInterval isPotentiallyLong]
+ -[SignpostFrameLifetimeInterval processNameToPidsDict]
+ -[SignpostFrameLifetimeInterval setFrameLatencyInterval:]
+ -[SignpostFrameLifetimeInterval setProcessNameToPidsDict:]
+ -[SignpostFrameLifetimeInterval setUpdateIntervals:]
+ -[SignpostFrameLifetimeInterval updateIntervalsForPID:]
+ -[SignpostFrameLifetimeInterval updateIntervals]
+ -[SignpostFrameLifetimeInterval(Deprecated) commits]
+ -[SignpostFrameOverrunInterval .cxx_destruct]
+ -[SignpostFrameOverrunInterval frameLifetime]
+ -[SignpostFrameOverrunInterval initWithFrameLifetime:startMCT:endMCT:timebaseRatio:class:]
+ -[SignpostGPURenderInterval .cxx_destruct]
+ -[SignpostGPURenderInterval frameLifetime]
+ -[SignpostGPURenderInterval frameSeed]
+ -[SignpostGPURenderInterval initWithInterval:]
+ -[SignpostGPURenderInterval initWithInterval:frameSeed:]
+ -[SignpostGPURenderInterval isPotentiallyLong]
+ -[SignpostGPURenderInterval setFrameLifetime:]
+ -[SignpostIntervalBuilder collectPIDToProcessNameForEvent:]
+ -[SignpostIntervalBuilder doneProcessingWithIntervalBuilderSource:]
+ -[SignpostIntervalBuilder pidToProcessNameDictionary]
+ -[SignpostIntervalBuilder processBeginEvent:endEvent:intervalBuilderSource:isAnimation:]
+ -[SignpostIntervalBuilder processEndEvent:intervalBuilderSource:isAnimation:]
+ -[SignpostIntervalBuilder runSynchronized:]
+ -[SignpostObject copy]
+ -[SignpostRenderServerRenderInterval frameLifetime]
+ -[SignpostRenderServerRenderInterval initWithInterval:frameSeed:renderSkipReason:refreshInterval:displayID:passCount:compileCount:cacheMissCount:fallbackDrawCount:]
+ -[SignpostRenderServerRenderInterval isPotentiallyLong]
+ -[SignpostRenderServerRenderInterval setFrameLifetime:]
+ -[SignpostSupportMetadataSegment initWithArgumentObject:scalarType:typeNamespace:type:tokens:stringPrefix:privacy:]
+ -[SignpostSupportMetadataSegment scalarType]
+ -[SignpostSupportMetadataSegment(Serialization) _dictionaryRepresentationWithIsHumanReadable:shouldRedact:didRedactOut:].cold.1
+ -[SignpostSupportMetadataSegment(Serialization) _scalarTypeForArgumentObject:scalarTypeNumber:]
+ -[SignpostSupportObject copy]
+ -[SignpostSupportObjectExtractor _calculateRawFilterPredicate]
+ -[SignpostSupportObjectExtractor _checkProcessingConfiguration]
+ -[SignpostSupportObjectExtractor _hasNonPredicateFirstPassFilter]
+ -[SignpostSupportObjectExtractor _hasSupportedFilterConfiguration]
+ -[SignpostSupportObjectExtractor filterPredicateString]
+ -[SignpostSupportObjectExtractor filterPredicate]
+ -[SignpostSupportObjectExtractor intervalReconstructionProcessingBlock]
+ -[SignpostSupportObjectExtractor processInterval:isAnimation:]
+ -[SignpostSupportObjectExtractor rawFilterPredicate]
+ -[SignpostSupportObjectExtractor setFilterPredicate:]
+ -[SignpostSupportObjectExtractor setFilterPredicateString:]
+ -[SignpostSupportObjectExtractor setIntervalReconstructionProcessingBlock:]
+ -[SignpostSupportObjectExtractor setRawFilterPredicate:]
+ -[SignpostSupportObjectExtractor(Deserialization) _startDeserializationProcessing]
+ -[SignpostUpdateSequenceInterval .cxx_destruct]
+ -[SignpostUpdateSequenceInterval commits]
+ -[SignpostUpdateSequenceInterval frameLifetime]
+ -[SignpostUpdateSequenceInterval initWithInterval:isLong:]
+ -[SignpostUpdateSequenceInterval initWithStartMCT:endMCT:timebaseRatio:]
+ -[SignpostUpdateSequenceInterval isImplicit]
+ -[SignpostUpdateSequenceInterval isPotentiallyLong]
+ -[SignpostUpdateSequenceInterval pid]
+ -[SignpostUpdateSequenceInterval setCommits:]
+ -[SignpostUpdateSequenceInterval setFrameLifetime:]
+ -[SignpostUpdateSequenceInterval setPid:]
+ -[_GeneratedSignpostMetadata hasRelativeMcts]
+ -[_GeneratedSignpostMetadata setHasRelativeMcts:]
+ -[_SignpostAggregationValueSegmentParser processSegment:placeholderType:].cold.1
+ GCC_except_table1
+ GCC_except_table3
+ GCC_except_table35
+ GCC_except_table50
+ GCC_except_table75
+ GCC_except_table80
+ OBJC_IVAR_$_SignpostAnimationAccumulatedState._allUpateIntervals
+ OBJC_IVAR_$_SignpostAnimationOverrunQuery._contributingPID
+ OBJC_IVAR_$_SignpostAnimationOverrunQuery._displayID
+ OBJC_IVAR_$_SignpostAnimationOverrunQuery._overrunClass
+ OBJC_IVAR_$_SignpostAnimationOverrunQuery._overrunType
+ OBJC_IVAR_$_SignpostAnimationSubInterval._beginEvent
+ OBJC_IVAR_$_SignpostAnimationSubInterval._endEvent
+ OBJC_IVAR_$_SignpostCAInstrumentationProcessor._gpuBlock
+ OBJC_IVAR_$_SignpostCAInstrumentationProcessor._queueCommitIntervals
+ OBJC_IVAR_$_SignpostCAInstrumentationProcessor._queueUpdateIntervals
+ OBJC_IVAR_$_SignpostCAInstrumentationProcessor._updateIntervalBlock
+ OBJC_IVAR_$_SignpostEvent._isGenerated
+ OBJC_IVAR_$_SignpostFrameLatencyInterval._frameLifetime
+ OBJC_IVAR_$_SignpostFrameLifetimeInterval._displayID
+ OBJC_IVAR_$_SignpostFrameLifetimeInterval._gpuInterval
+ OBJC_IVAR_$_SignpostFrameLifetimeInterval._processNameToPidsDict
+ OBJC_IVAR_$_SignpostFrameLifetimeInterval._updateIntervals
+ OBJC_IVAR_$_SignpostFrameOverrunInterval._frameLifetime
+ OBJC_IVAR_$_SignpostGPURenderInterval._frameLifetime
+ OBJC_IVAR_$_SignpostGPURenderInterval._frameSeed
+ OBJC_IVAR_$_SignpostIntervalBuilder._pidToProcessNameDictionary
+ OBJC_IVAR_$_SignpostRenderServerRenderInterval._frameLifetime
+ OBJC_IVAR_$_SignpostSupportMetadataSegment._scalarType
+ OBJC_IVAR_$_SignpostSupportObjectExtractor._filterPredicate
+ OBJC_IVAR_$_SignpostSupportObjectExtractor._filterPredicateString
+ OBJC_IVAR_$_SignpostSupportObjectExtractor._intervalReconstructionProcessingBlock
+ OBJC_IVAR_$_SignpostSupportObjectExtractor._rawFilterPredicate
+ OBJC_IVAR_$_SignpostUpdateSequenceInterval._commits
+ OBJC_IVAR_$_SignpostUpdateSequenceInterval._frameLifetime
+ OBJC_IVAR_$_SignpostUpdateSequenceInterval._implicit
+ OBJC_IVAR_$_SignpostUpdateSequenceInterval._isLong
+ OBJC_IVAR_$_SignpostUpdateSequenceInterval._pid
+ OBJC_IVAR_$__GeneratedSignpostMetadata._hasRelativeMcts
+ PassesPerfLoggingAllowlist.cold.1
+ PassesPerfLoggingAllowlist.cold.2
+ SRStringFilter_debugLog.cold.1
+ SignpostReporterAllowlistedStringSet.cold.2
+ SignpostReporterAllowlistedStringSet.cold.3
+ SignpostReporterAllowlistedStringSet.cold.4
+ SignpostReporterAllowlistedStringSet.cold.5
+ SignpostReporterAllowlistedStringSet.cold.6
+ SignpostReporterAllowlistedStringSet.cold.7
+ SignpostReporterCrossPlatformAppleAccountAllowlist.cold.1
+ SignpostReporterCrossPlatformAppleIDAuthenticationAllowlist.cold.1
+ SignpostReporterCrossPlatformAuthKitAllowlist.cold.1
+ SignpostReporterCrossPlatformIntelligencePlatformAllowlist.cold.1
+ SignpostReporterCrossPlatformLowDiskConditionAllowlist.cold.1
+ SignpostReporterCrossPlatformPersonIdentificationTaskAllowlist.cold.1
+ SignpostReporterCrossPlatformPersonIdentificationTaskAllowlist.onceToken
+ SignpostReporterCrossPlatformPersonIdentificationTaskAllowlist.stringArray
+ SignpostReporterCrossPlatformSharedAllowlist.cold.1
+ SignpostReporterCrossPlatformSiriAudioStringPasslist.cold.1
+ SignpostReporterCrossPlatformSiriHomeAutomationStringPasslist.cold.1
+ SignpostReporterCrossPlatformSiriPersonalUpdateStringPasslist.cold.1
+ SignpostReporterCrossPlatformSiriPlaybackControlsStringPasslist.cold.1
+ SignpostReporterCrossPlatformSiriVideoUTSOperationRequestStringPasslist.cold.1
+ SignpostReporterCrossPlatformSiriVocabularyStringPasslist.cold.1
+ SignpostReporterCrossPlatformSpeechProfileAllowlist.cold.1
+ SignpostReporterCrossPlatformWidgetAllowlist.cold.1
+ SignpostReporterCrossPlatformZelkovaAllowlist.cold.1
+ SignpostReporterEmbeddedOSHangTracerAllowlist.cold.1
+ SignpostReporterEmbeddedOSMusicWaitTimeAllowlist.cold.1
+ SignpostReporterMacOsPerfLoggingOperationCategoryAllowlist.cold.1
+ SignpostReporterMacOsPerfLoggingOperationNameAllowlist.cold.1
+ SignpostReporteriOSPoirotAllowlist.cold.1
+ SignpostReporteriOSSystemEnvironmentsAllowlist.cold.1
+ SignpostScalarTypeFromNumber.cold.1
+ SignpostScalarTypeFromNumber.objCTypeToScalarType
+ SignpostScalarTypeFromNumber.onceToken
+ SignpostSystemTimebaseRatio.cold.1
+ _OBJC_CLASS_$_NSMutableIndexSet
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_CLASS_$_NSSortDescriptor
+ _OBJC_CLASS_$_SignpostAnimationOverrunQuery
+ _OBJC_CLASS_$_SignpostGPURenderInterval
+ _OBJC_CLASS_$_SignpostUpdateSequenceInterval
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_METACLASS_$_SignpostAnimationOverrunQuery
+ _OBJC_METACLASS_$_SignpostGPURenderInterval
+ _OBJC_METACLASS_$_SignpostUpdateSequenceInterval
+ _SSCAIsUCMetadataSubsystemCategory
+ _SignpostReporterCrossPlatformPersonIdentificationTaskAllowlist
+ _SignpostScalarTypeFromNumber
+ _SignpostScalarTypeIsIntegral
+ _SignpostScalarTypeIsSigned
+ _SignpostScalarTypeSizeOf
+ __46-[SignpostAnimationInterval overrunIntervals:]_block_invoke.707
+ __47-[SignpostIntervalBuilder dropAccumulatedState]_block_invoke.116
+ __47-[SignpostIntervalBuilder dropAccumulatedState]_block_invoke.120
+ __47-[SignpostIntervalBuilder dropAccumulatedState]_block_invoke.124
+ __47-[SignpostIntervalBuilder dropAccumulatedState]_block_invoke.128
+ __47-[SignpostIntervalBuilder dropAccumulatedState]_block_invoke.132
+ __47-[SignpostIntervalBuilder dropAccumulatedState]_block_invoke.136
+ __47-[SignpostIntervalBuilder dropAccumulatedState]_block_invoke.140
+ __60-[SignpostCAInstrumentationProcessor newConfiguredExtractor]_block_invoke.216
+ __60-[SignpostCAInstrumentationProcessor newConfiguredExtractor]_block_invoke.220
+ __68-[SignpostCAInstrumentationProcessor _updatesMatchingFrameLifetime:]_block_invoke.188
+ __68-[SignpostCAInstrumentationProcessor _updatesMatchingFrameLifetime:]_block_invoke.192
+ __68-[SignpostCAInstrumentationProcessor _updatesMatchingFrameLifetime:]_block_invoke.194
+ __68-[SignpostCAInstrumentationProcessor _updatesMatchingFrameLifetime:]_block_invoke_2.193
+ __OBJC_$_CLASS_METHODS_SignpostAnimationOverrunQuery
+ __OBJC_$_INSTANCE_METHODS_SignpostAnimationOverrunQuery
+ __OBJC_$_INSTANCE_METHODS_SignpostFrameLifetimeInterval(Deprecated)
+ __OBJC_$_INSTANCE_METHODS_SignpostGPURenderInterval
+ __OBJC_$_INSTANCE_METHODS_SignpostUpdateSequenceInterval
+ __OBJC_$_INSTANCE_VARIABLES_SignpostAnimationOverrunQuery
+ __OBJC_$_INSTANCE_VARIABLES_SignpostGPURenderInterval
+ __OBJC_$_INSTANCE_VARIABLES_SignpostUpdateSequenceInterval
+ __OBJC_$_PROP_LIST_SignpostAnimationOverrunQuery
+ __OBJC_$_PROP_LIST_SignpostGPURenderInterval
+ __OBJC_$_PROP_LIST_SignpostIntervalBuilderSource
+ __OBJC_$_PROP_LIST_SignpostOverrunChecking
+ __OBJC_$_PROP_LIST_SignpostUpdateSequenceInterval
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SignpostIntervalBuilderSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SignpostOverrunChecking
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SignpostIntervalBuilderSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SignpostOverrunChecking
+ __OBJC_$_PROTOCOL_REFS_SignpostIntervalBuilderSource
+ __OBJC_CLASS_PROTOCOLS_$_SignpostGPURenderInterval
+ __OBJC_CLASS_PROTOCOLS_$_SignpostRenderServerRenderInterval
+ __OBJC_CLASS_PROTOCOLS_$_SignpostSupportObjectExtractor
+ __OBJC_CLASS_PROTOCOLS_$_SignpostUpdateSequenceInterval
+ __OBJC_CLASS_RO_$_SignpostAnimationOverrunQuery
+ __OBJC_CLASS_RO_$_SignpostGPURenderInterval
+ __OBJC_CLASS_RO_$_SignpostUpdateSequenceInterval
+ __OBJC_LABEL_PROTOCOL_$_SignpostIntervalBuilderSource
+ __OBJC_LABEL_PROTOCOL_$_SignpostOverrunChecking
+ __OBJC_METACLASS_RO_$_SignpostAnimationOverrunQuery
+ __OBJC_METACLASS_RO_$_SignpostGPURenderInterval
+ __OBJC_METACLASS_RO_$_SignpostUpdateSequenceInterval
+ __OBJC_PROTOCOL_$_SignpostIntervalBuilderSource
+ __OBJC_PROTOCOL_$_SignpostOverrunChecking
+ __SignpostIntervalInTimeRange
+ __SignpostReporterAllowlistedStringSet_block_invoke.11.cold.10
+ __SignpostReporterAllowlistedStringSet_block_invoke.11.cold.2
+ __SignpostReporterAllowlistedStringSet_block_invoke.11.cold.3
+ __SignpostReporterAllowlistedStringSet_block_invoke.11.cold.4
+ __SignpostReporterAllowlistedStringSet_block_invoke.11.cold.5
+ __SignpostReporterAllowlistedStringSet_block_invoke.11.cold.6
+ __SignpostReporterAllowlistedStringSet_block_invoke.11.cold.7
+ __SignpostReporterAllowlistedStringSet_block_invoke.11.cold.8
+ __SignpostReporterAllowlistedStringSet_block_invoke.11.cold.9
+ __SignpostReporterAllowlistedStringSet_block_invoke.cold.2
+ __SignpostReporterAllowlistedStringSet_block_invoke.cold.3
+ ___43-[SignpostEvent _argumentObjectWithPrefix:]_block_invoke
+ ___46-[SignpostAnimationInterval overrunIntervals:]_block_invoke
+ ___52-[SignpostAnimationInterval initWithFrameLifetimes:]_block_invoke
+ ___55-[SignpostFrameLifetimeInterval updateIntervalsForPID:]_block_invoke
+ ___67-[SignpostIntervalBuilder doneProcessingWithIntervalBuilderSource:]_block_invoke
+ ___67-[SignpostIntervalBuilder doneProcessingWithIntervalBuilderSource:]_block_invoke_2
+ ___67-[SignpostIntervalBuilder doneProcessingWithIntervalBuilderSource:]_block_invoke_3
+ ___68-[SignpostCAInstrumentationProcessor _handleUpdateSequenceInterval:]_block_invoke
+ ___68-[SignpostCAInstrumentationProcessor _updatesMatchingFrameLifetime:]_block_invoke
+ ___68-[SignpostCAInstrumentationProcessor _updatesMatchingFrameLifetime:]_block_invoke_2
+ ___88-[SignpostIntervalBuilder processBeginEvent:endEvent:intervalBuilderSource:isAnimation:]_block_invoke
+ ___SignpostReporterCrossPlatformPersonIdentificationTaskAllowlist_block_invoke
+ ___SignpostScalarTypeFromNumber_block_invoke
+ ___block_descriptor_32_e56_B24?0"SignpostFrameLifetimeInterval"8"NSDictionary"16l
+ ___block_descriptor_32_e75_q24?0"SignpostUpdateSequenceInterval"8"SignpostUpdateSequenceInterval"16l
+ ___block_descriptor_36_e57_B24?0"SignpostUpdateSequenceInterval"8"NSDictionary"16l
+ ___block_descriptor_40_e8_32w_e40_v16?0"SignpostUpdateSequenceInterval"8l
+ ___block_descriptor_52_e39_B32?0"SignpostCommitInterval"8Q16^B24l
+ ___block_descriptor_56_e8_32s40s48s_e23_v24?0"NSIndexSet"8Q16l
+ ___block_descriptor_56_e8_32s40s48s_e30_v32?0"SignpostEvent"8Q16^B24l
+ ___block_descriptor_56_e8_32s_e39_B32?0"SignpostCommitInterval"8Q16^B24l
+ ___block_descriptor_56_e8_32s_e47_B32?0"SignpostUpdateSequenceInterval"8Q16^B24l
+ ___block_descriptor_80_e8_32s40s48r56r64r_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48r56r64r
+ ___destroy_helper_block_e8_32s40s48r56r64r
+ __block_literal_global.1020
+ __block_literal_global.484
+ __block_literal_global.533
+ __block_literal_global.571
+ __block_literal_global.605
+ __block_literal_global.702
+ __block_literal_global.800
+ __block_literal_global.944
+ _argumentObjectWithPrefix:.onceToken
+ _argumentObjectWithPrefix:.prefixRegex
+ _checkTokenString.cold.1
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_msgSend$_argumentObjectWithPrefix:
+ _objc_msgSend$_argumentObjectWithPrefix:expectedClass:
+ _objc_msgSend$_baseMCTForEvent:
+ _objc_msgSend$_calculateRawFilterPredicate
+ _objc_msgSend$_checkProcessingConfiguration
+ _objc_msgSend$_dataArgumentWithName:
+ _objc_msgSend$_handleCommitInterval:
+ _objc_msgSend$_handleFrameLifetime:isLong:isConcise:pidToNameDict:
+ _objc_msgSend$_handleFrameLifetimeBegin:isLong:
+ _objc_msgSend$_handleUpdateInterval:
+ _objc_msgSend$_handleUpdateSequenceInterval:
+ _objc_msgSend$_hasNonPredicateFirstPassFilter
+ _objc_msgSend$_hasSupportedFilterConfiguration
+ _objc_msgSend$_numberArgumentWithPrefix:
+ _objc_msgSend$_removeOrphansFromQueue:preceedingEvent:
+ _objc_msgSend$_scalarTypeForArgumentObject:scalarTypeNumber:
+ _objc_msgSend$_startDeserializationProcessing
+ _objc_msgSend$_updatesMatchingFrameLifetime:
+ _objc_msgSend$addIndex:
+ _objc_msgSend$allUpateIntervals
+ _objc_msgSend$bytes
+ _objc_msgSend$collectPIDToProcessNameForEvent:
+ _objc_msgSend$commits
+ _objc_msgSend$containsIndex:
+ _objc_msgSend$contributingPID
+ _objc_msgSend$copyWithType:machContinuousTime:
+ _objc_msgSend$displayIDNum
+ _objc_msgSend$doneProcessingWithIntervalBuilderSource:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$filterPredicate
+ _objc_msgSend$filterPredicateString
+ _objc_msgSend$firstIndex
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$frameLifetime
+ _objc_msgSend$gpuBlock
+ _objc_msgSend$hasRelativeMcts
+ _objc_msgSend$hasRenderServerUpdateOnly
+ _objc_msgSend$indexGreaterThanIndex:
+ _objc_msgSend$indexSet
+ _objc_msgSend$indexesOfObjectsPassingTest:
+ _objc_msgSend$initWithArgumentObject:scalarType:typeNamespace:type:tokens:stringPrefix:privacy:
+ _objc_msgSend$initWithContextInfoEvent:contributor:
+ _objc_msgSend$initWithFrameLifetime:startMCT:endMCT:timebaseRatio:class:
+ _objc_msgSend$initWithFrameLifetimes:
+ _objc_msgSend$initWithInterval:contextArray:hidLatencyInterval:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:
+ _objc_msgSend$initWithInterval:contextArray:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:
+ _objc_msgSend$initWithInterval:frameSeed:
+ _objc_msgSend$initWithInterval:frameSeed:renderSkipReason:refreshInterval:displayID:passCount:compileCount:cacheMissCount:fallbackDrawCount:
+ _objc_msgSend$initWithInterval:isLong:
+ _objc_msgSend$initWithInterval:swapID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:renderInterval:gpuInterval:
+ _objc_msgSend$initWithSubsystem:category:timebaseRatio:
+ _objc_msgSend$intervalReconstructionProcessingBlock
+ _objc_msgSend$isGenerated
+ _objc_msgSend$isGeneratedInterval
+ _objc_msgSend$isPotentiallyLong
+ _objc_msgSend$nonFirstFrameContributedGlitchTimeRatioAdjustedMsPerS
+ _objc_msgSend$numberOfRanges
+ _objc_msgSend$objCType
+ _objc_msgSend$objectsAtIndexes:
+ _objc_msgSend$overrunIntervals:
+ _objc_msgSend$overrunType
+ _objc_msgSend$pidToProcessNameDictionary
+ _objc_msgSend$processBeginEvent:endEvent:intervalBuilderSource:isAnimation:
+ _objc_msgSend$processEndEvent:intervalBuilderSource:isAnimation:
+ _objc_msgSend$processInterval:isAnimation:
+ _objc_msgSend$processNameToPidsDict
+ _objc_msgSend$queueCommitIntervals
+ _objc_msgSend$queueUpdateIntervals
+ _objc_msgSend$rangeAtIndex:
+ _objc_msgSend$rawFilterPredicate
+ _objc_msgSend$reason
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$removeObjectsAtIndexes:
+ _objc_msgSend$removeObjectsInRange:
+ _objc_msgSend$runSynchronized:
+ _objc_msgSend$scalarType
+ _objc_msgSend$setCommits:
+ _objc_msgSend$setContributingPID:
+ _objc_msgSend$setFrameLifetime:
+ _objc_msgSend$setHasRelativeMcts:
+ _objc_msgSend$setIsGenerated:
+ _objc_msgSend$setPid:
+ _objc_msgSend$setProcessNameToPidsDict:
+ _objc_msgSend$setRawFilterPredicate:
+ _objc_msgSend$setUpdateIntervalBlock:
+ _objc_msgSend$setUpdateIntervals:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$sortDescriptorWithKey:ascending:
+ _objc_msgSend$sortUsingDescriptors:
+ _objc_msgSend$sortWithOptions:usingComparator:
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$updateIntervalBlock
+ _objc_msgSend$updateIntervals
+ _objc_sync_enter
+ _objc_sync_exit
+ _signpost_debug_log.cold.1
+ _stringForDate.cold.1
+ _timeTranslatorDebugLog.cold.1
+ serializationTypeNumber.onceToken.481
+ serializationTypeNumber.serializationTypeNumber.482
- -[SignpostAnimationAccumulatedState _handleFrameLifetime:isLong:isConcise:]
- -[SignpostCAInstrumentationProcessor _handleFrameLifetimeBegin:]
- -[SignpostCAInstrumentationProcessor _handleFrameLifetimeBegin:].cold.1
- -[SignpostCAInstrumentationProcessor _handleLongFrameLifetimeBegin:]
- -[SignpostCAInstrumentationProcessor _handleLongFrameLifetimeBegin:].cold.1
- -[SignpostFrameLifetimeInterval initWithInterval:contextArray:hidLatencyInterval:renderInterval:frameLatencyInterval:frameSeedToSkippedRenderIntervals:]
- -[SignpostFrameLifetimeInterval initWithInterval:contextArray:hidLatencyInterval:renderInterval:frameLatencyInterval:frameSeedToSkippedRenderIntervals:].cold.1
- -[SignpostFrameLifetimeInterval initWithInterval:contextArray:hidLatencyInterval:renderInterval:frameLatencyInterval:frameSeedToSkippedRenderIntervals:].cold.2
- -[SignpostFrameLifetimeInterval initWithInterval:contextArray:hidLatencyInterval:renderInterval:frameLatencyInterval:frameSeedToSkippedRenderIntervals:].cold.3
- -[SignpostFrameLifetimeInterval initWithInterval:contextArray:hidLatencyInterval:renderInterval:frameLatencyInterval:frameSeedToSkippedRenderIntervals:].cold.4
- -[SignpostFrameLifetimeInterval initWithInterval:contextArray:hidLatencyInterval:renderInterval:frameLatencyInterval:frameSeedToSkippedRenderIntervals:].cold.5
- -[SignpostFrameLifetimeInterval initWithInterval:contextArray:hidLatencyInterval:renderInterval:frameLatencyInterval:frameSeedToSkippedRenderIntervals:].cold.6
- -[SignpostFrameLifetimeInterval initWithInterval:contextArray:hidLatencyInterval:renderInterval:frameLatencyInterval:frameSeedToSkippedRenderIntervals:].cold.7
- -[SignpostFrameLifetimeInterval initWithInterval:contextArray:renderInterval:frameSeedToSkippedRenderIntervals:]
- -[SignpostFrameLifetimeInterval initWithInterval:contextArray:renderInterval:frameSeedToSkippedRenderIntervals:].cold.1
- -[SignpostFrameLifetimeInterval initWithInterval:contextArray:renderInterval:frameSeedToSkippedRenderIntervals:].cold.2
- -[SignpostFrameLifetimeInterval setLifetimeIsLong:]
- -[SignpostFrameOverrunInterval initWithStartMCT:endMCT:timebaseRatio:class:]
- -[SignpostIntervalBuilder doneProcessing]
- -[SignpostIntervalBuilder processEndEvent:firstFrameGraceTimeController:isAnimation:]
- -[SignpostIntervalBuilder syncQueue]
- -[SignpostSupportMetadataSegment initWithArgumentObject:typeNamespace:type:tokens:stringPrefix:privacy:]
- -[SignpostSupportObjectExtractor _processingStarting]
- GCC_except_table0
- GCC_except_table33
- GCC_except_table45
- GCC_except_table62
- GCC_except_table70
- GCC_except_table74
- OBJC_IVAR_$_SSCAMetalLayerOnGlassDrawableInterval._instantaneousFramesPerSecond
- OBJC_IVAR_$_SignpostIntervalBuilder._syncQueue
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- __47-[SignpostIntervalBuilder dropAccumulatedState]_block_invoke.110
- __47-[SignpostIntervalBuilder dropAccumulatedState]_block_invoke.114
- __47-[SignpostIntervalBuilder dropAccumulatedState]_block_invoke.118
- __47-[SignpostIntervalBuilder dropAccumulatedState]_block_invoke.122
- __47-[SignpostIntervalBuilder dropAccumulatedState]_block_invoke.126
- __47-[SignpostIntervalBuilder dropAccumulatedState]_block_invoke.130
- __60-[SignpostCAInstrumentationProcessor newConfiguredExtractor]_block_invoke.153
- __60-[SignpostCAInstrumentationProcessor newConfiguredExtractor]_block_invoke.157
- __85-[SignpostIntervalBuilder processEndEvent:firstFrameGraceTimeController:isAnimation:]_block_invoke.cold.1
- __OBJC_$_INSTANCE_METHODS_SignpostFrameLifetimeInterval
- __OBJC_$_PROP_LIST_SignpostFrameLifetimeInterval
- ___41-[SignpostIntervalBuilder doneProcessing]_block_invoke
- ___41-[SignpostIntervalBuilder doneProcessing]_block_invoke_2
- ___74-[SignpostAnimationInterval overrunIntervalsOfType:class:contributingPID:]_block_invoke
- ___85-[SignpostIntervalBuilder processEndEvent:firstFrameGraceTimeController:isAnimation:]_block_invoke
- ___block_descriptor_72_e8_32s40s48s56r_e5_v8?0l
- __block_literal_global.1022
- __block_literal_global.481
- __block_literal_global.522
- __block_literal_global.595
- __block_literal_global.958
- _objc_msgSend$_handleFrameLifetime:isLong:isConcise:
- _objc_msgSend$_handleFrameLifetimeBegin:
- _objc_msgSend$_handleLongFrameLifetimeBegin:
- _objc_msgSend$_processingStarting
- _objc_msgSend$doneProcessing
- _objc_msgSend$frameLatency
- _objc_msgSend$initWithArgumentObject:typeNamespace:type:tokens:stringPrefix:privacy:
- _objc_msgSend$initWithInterval:contextArray:hidLatencyInterval:renderInterval:frameLatencyInterval:frameSeedToSkippedRenderIntervals:
- _objc_msgSend$initWithInterval:contextArray:renderInterval:frameSeedToSkippedRenderIntervals:
- _objc_msgSend$initWithStartMCT:endMCT:timebaseRatio:class:
- _objc_msgSend$processEndEvent:firstFrameGraceTimeController:isAnimation:
- _objc_msgSend$setLifetimeIsLong:
- serializationTypeNumber.onceToken.478
- serializationTypeNumber.serializationTypeNumber.479
CStrings:
+ "%.1fms/s"
+ "(?:^|\\s)([a-zA-Z0-9_]+)[:=]?$"
+ "-[SignpostFrameLifetimeInterval initWithInterval:contextArray:hidLatencyInterval:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:]"
+ "-[SignpostFrameLifetimeInterval initWithInterval:contextArray:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:]"
+ "@\"NSPredicate\""
+ "@\"SignpostGPURenderInterval\""
+ "@\"SignpostSupportAnimationGraceTimeController\"16@0:8"
+ "@20@0:8i16"
+ "@28@0:8@16I24"
+ "@32@0:8@16^{?=iiii}24"
+ "@48@0:8@16@24@32^B40"
+ "@56@0:8@16@24@32@40@48"
+ "@56@0:8@16Q24Q32d40Q48"
+ "@64@0:8@16I24@28Q36I44S48C52C56C60"
+ "@72@0:8@16Q24@32@40@48@56@64"
+ "@92@0:8@16I24I28I32B36C40Q44Q52Q60@68@76@84"
+ "@?<@\"SignpostEvent\"@?@\"SignpostEvent\">16@0:8"
+ "ArgumentScalarType"
+ "B24@?0@\"SignpostUpdateSequenceInterval\"8@\"NSDictionary\"16"
+ "B28@0:8@\"SignpostInterval\"16B24"
+ "B32@?0@\"SignpostCommitInterval\"8Q16^B24"
+ "B32@?0@\"SignpostUpdateSequenceInterval\"8Q16^B24"
+ "ConfigureVNCreateFaceprintRequest"
+ "ConfigureVNDetectFaceRectanglesRequest"
+ "D"
+ "Deprecated"
+ "DetectFace"
+ "Failed to create predicate for predicate string: '%@' due to reason '%@'. Please refer to the output of 'log help predicates' for more information on valid predicates."
+ "FrameGPUExecute"
+ "FrameGPUExecution"
+ "FrameLifetime has %ld commits unrelated to UpdateSequence"
+ "FrameLifetime with server side updates only has %u updates."
+ "FrameLifetimeInterval"
+ "FrameModifierTarget"
+ "FramePrevious"
+ "FrameRender"
+ "FrameUpdate"
+ "FrameUpdate %llx is long with no contributors"
+ "FrameUpdate contributor length not a multiple of contributor size"
+ "GenerateFaceprint"
+ "Glitch Ratio"
+ "LoadPixelBuffer"
+ "Missing name for pid %@"
+ "NFFCGTRAMsPerS"
+ "NoDetectedFaceCount"
+ "NoFaceprintResultCount"
+ "Processing requested after processing already completed"
+ "Q32@0:8@16@24"
+ "Requested to handle a generated hid interval"
+ "Requested to handle a generated latency interval"
+ "S"
+ "ScalarType"
+ "SignpostAnimationOverrunQuery"
+ "SignpostGPURenderInterval"
+ "SignpostIntervalBuilderSource"
+ "SignpostOverrunChecking"
+ "SignpostUpdateSequenceInterval"
+ "T@\"NSArray\",&,N,V_updateIntervals"
+ "T@\"NSDictionary\",&,N,V_processNameToPidsDict"
+ "T@\"NSIndexSet\",R,N"
+ "T@\"NSMutableArray\",R,N,V_allUpateIntervals"
+ "T@\"NSMutableArray\",R,N,V_queueCommitIntervals"
+ "T@\"NSMutableArray\",R,N,V_queueUpdateIntervals"
+ "T@\"NSMutableDictionary\",R,N,V_pidToProcessNameDictionary"
+ "T@\"NSNumber\",C,N,V_contributingPID"
+ "T@\"NSNumber\",C,N,V_displayID"
+ "T@\"NSPredicate\",&,N,V_filterPredicate"
+ "T@\"NSPredicate\",&,N,V_rawFilterPredicate"
+ "T@\"NSString\",&,N,V_filterPredicateString"
+ "T@\"SignpostEvent\",R,N,V_beginEvent"
+ "T@\"SignpostEvent\",R,N,V_endEvent"
+ "T@\"SignpostFrameLatencyInterval\",&,N,V_frameLatencyInterval"
+ "T@\"SignpostFrameLifetimeInterval\",R,N,V_frameLifetime"
+ "T@\"SignpostFrameLifetimeInterval\",W,N,V_frameLifetime"
+ "T@\"SignpostGPURenderInterval\",R,N,V_gpuInterval"
+ "T@\"SignpostSupportAnimationGraceTimeController\",R,N"
+ "T@?,C,N,V_gpuBlock"
+ "T@?,C,N,V_intervalReconstructionProcessingBlock"
+ "T@?,C,N,V_updateIntervalBlock"
+ "T@?,R,C,N"
+ "TB,N,V_hasRelativeMcts"
+ "TB,N,V_isGenerated"
+ "TB,R,N,GisImplicit,V_implicit"
+ "TB,R,N,GisPotentiallyLong"
+ "TB,R,N,V_lifetimeIsLong"
+ "TQ,R,N,V_scalarType"
+ "TemporaryAnimationInterval"
+ "The `filterPredicateString` property is not supported when reading this type of serialized data."
+ "The `filterPredicate` property is not supported when reading this type of serialized data."
+ "Ti,N,V_pid"
+ "Unsupported combination of predicate and non-predicate based filters"
+ "UpdateCycle"
+ "UpdateCycle.Stalls"
+ "UpdateSequence"
+ "_allUpateIntervals"
+ "_argumentObjectWithPrefix:"
+ "_argumentObjectWithPrefix:expectedClass:"
+ "_baseMCTForEvent:"
+ "_calculateRawFilterPredicate"
+ "_checkProcessingConfiguration"
+ "_contributingPID"
+ "_dataArgumentWithPrefix:"
+ "_filterPredicate"
+ "_filterPredicateString"
+ "_frameLifetime"
+ "_gpuBlock"
+ "_gpuInterval"
+ "_handleCommitInterval:"
+ "_handleFrameLifetime:isLong:isConcise:pidToNameDict:"
+ "_handleFrameLifetimeBegin:isLong:"
+ "_handleUpdateInterval:"
+ "_handleUpdateSequenceInterval:"
+ "_hasNonPredicateFirstPassFilter"
+ "_hasRelativeMcts"
+ "_hasSupportedFilterConfiguration"
+ "_implicit"
+ "_intervalReconstructionProcessingBlock"
+ "_isGenerated"
+ "_isLong"
+ "_numberArgumentWithPrefix:"
+ "_pidToProcessNameDictionary"
+ "_processNameToPidsDict"
+ "_queueCommitIntervals"
+ "_queueUpdateIntervals"
+ "_rawFilterPredicate"
+ "_removeOrphansFromQueue:preceedingEvent:"
+ "_scalarType"
+ "_scalarTypeForArgumentObject:scalarTypeNumber:"
+ "_startDeserializationProcessing"
+ "_stringArgumentWithPrefix:"
+ "_updateIntervalBlock"
+ "_updateIntervals"
+ "_updatesMatchingFrameLifetime:"
+ "addIndex:"
+ "allDisplayIDs"
+ "allUpateIntervals"
+ "args1"
+ "args2"
+ "bytes"
+ "c"
+ "collectPIDToProcessNameForEvent:"
+ "com.apple.AppKit"
+ "containsIndex:"
+ "contributingPID"
+ "contributingPidsForProcessName:"
+ "contributors"
+ "copyWithType:machContinuousTime:"
+ "d40@0:8@16@24Q32"
+ "doneProcessingWithIntervalBuilderSource:"
+ "enumerateObjectsUsingBlock:"
+ "filterPredicate"
+ "filterPredicateString"
+ "firstIndex"
+ "firstMatchInString:options:range:"
+ "frameLifetime"
+ "gpuBlock"
+ "gpuInterval"
+ "hasRelativeMcts"
+ "hasRenderServerUpdateOnly"
+ "implicit"
+ "indexGreaterThanIndex:"
+ "indexSet"
+ "indexesOfObjectsPassingTest:"
+ "initWithArgumentObject:scalarType:typeNamespace:type:tokens:stringPrefix:privacy:"
+ "initWithContextInfoEvent:contributor:"
+ "initWithFrameLifetime:startMCT:endMCT:timebaseRatio:class:"
+ "initWithFrameLifetimes:"
+ "initWithInterval:contextArray:hidLatencyInterval:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:"
+ "initWithInterval:contextArray:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:"
+ "initWithInterval:frameSeed:"
+ "initWithInterval:frameSeed:renderSkipReason:refreshInterval:displayID:passCount:compileCount:cacheMissCount:fallbackDrawCount:"
+ "initWithInterval:isLong:"
+ "initWithInterval:swapID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:renderInterval:gpuInterval:"
+ "intervalReconstructionProcessingBlock"
+ "isGenerated"
+ "isGeneratedInterval"
+ "isImplicit"
+ "isPotentiallyLong"
+ "nonFirstFrameContributedGlitches:"
+ "numberOfRanges"
+ "objCType"
+ "objectsAtIndexes:"
+ "oppositeEventForIntervalWithDeltaSeconds:"
+ "overrunIntervalForOverrunQuery:frameLifetimes:"
+ "overrunIntervals:"
+ "pidToProcessNameDictionary"
+ "potentiallyLong"
+ "processBeginEvent:endEvent:intervalBuilderSource:isAnimation:"
+ "processEndEvent:intervalBuilderSource:isAnimation:"
+ "processInterval:isAnimation:"
+ "processNameToPidsDict"
+ "q24@?0@\"SignpostUpdateSequenceInterval\"8@\"SignpostUpdateSequenceInterval\"16"
+ "queueCommitIntervals"
+ "queueUpdateIntervals"
+ "rangeAtIndex:"
+ "rawFilterPredicate"
+ "reason"
+ "regularExpressionWithPattern:options:error:"
+ "removeObjectsAtIndexes:"
+ "removeObjectsInRange:"
+ "runSynchronized:"
+ "s"
+ "scalarType"
+ "setContributingPID:"
+ "setDisplayID:"
+ "setFilterPredicate:"
+ "setFilterPredicateString:"
+ "setFrameLatencyInterval:"
+ "setFrameLifetime:"
+ "setGpuBlock:"
+ "setHasRelativeMcts:"
+ "setIntervalReconstructionProcessingBlock:"
+ "setIsGenerated:"
+ "setPid:"
+ "setProcessNameToPidsDict:"
+ "setRawFilterPredicate:"
+ "setUpdateIntervalBlock:"
+ "setUpdateIntervals:"
+ "setValue:forKey:"
+ "sortDescriptorWithKey:ascending:"
+ "sortUsingDescriptors:"
+ "sortWithOptions:usingComparator:"
+ "stringWithCString:encoding:"
+ "substringWithRange:"
+ "timeRatioMSPerSForOverrunQuery:frameLifetimes:applyPerceptionAdjustments:"
+ "updateIntervalBlock"
+ "updateIntervals"
+ "updateIntervalsForPID:"
+ "v16@?0@\"SignpostUpdateSequenceInterval\"8"
+ "v24@?0@\"NSIndexSet\"8Q16"
+ "v28@0:8@16B24"
+ "v32@?0@\"SignpostEvent\"8Q16^B24"
+ "v40@0:8@16B24B28@32"
+ "\xb1"
- "-[SignpostFrameLifetimeInterval initWithInterval:contextArray:hidLatencyInterval:renderInterval:frameLatencyInterval:frameSeedToSkippedRenderIntervals:]"
- "-[SignpostFrameLifetimeInterval initWithInterval:contextArray:renderInterval:frameSeedToSkippedRenderIntervals:]"
- "-[SignpostIntervalBuilder processEndEvent:firstFrameGraceTimeController:isAnimation:]_block_invoke"
- "@48@0:8Q16Q24d32Q40"
- "H"
- "HIDLatency frame seed mismatch: %#x vs %#x"
- "Processing requested after processing already completed."
- "SignpostIntervalBuilder sync queue"
- "T@\"SignpostFrameLatencyInterval\",R,N,V_frameLatencyInterval"
- "TB,N,V_lifetimeIsLong"
- "Td,R,N,V_instantaneousFramesPerSecond"
- "_handleFrameLifetime:isLong:isConcise:"
- "_handleFrameLifetimeBegin:"
- "_handleLongFrameLifetimeBegin:"
- "_instantaneousFramesPerSecond"
- "_processingStarting"
- "doneProcessing"
- "endEvent._resolvedEventType & SignpostResolvedEventType_IntervalEndEvent"
- "initWithArgumentObject:typeNamespace:type:tokens:stringPrefix:privacy:"
- "initWithInterval:contextArray:hidLatencyInterval:renderInterval:frameLatencyInterval:frameSeedToSkippedRenderIntervals:"
- "initWithInterval:contextArray:renderInterval:frameSeedToSkippedRenderIntervals:"
- "initWithStartMCT:endMCT:timebaseRatio:class:"
- "processEndEvent:firstFrameGraceTimeController:isAnimation:"
- "setLifetimeIsLong:"

```
