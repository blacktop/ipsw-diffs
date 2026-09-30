## SignpostSupport

> `/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport`

```diff

-151.8.0.0.0
-  __TEXT.__text: 0x4a4d8
-  __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_methlist: 0x62dc
+170.0.0.0.0
+  __TEXT.__text: 0x47f24
+  __TEXT.__auth_stubs: 0x570
+  __TEXT.__objc_methlist: 0x6114
   __TEXT.__const: 0x228
-  __TEXT.__cstring: 0x16daf
-  __TEXT.__oslogstring: 0xed6
-  __TEXT.__gcc_except_tab: 0x2b0
+  __TEXT.__cstring: 0x16c29
+  __TEXT.__oslogstring: 0xe6a
+  __TEXT.__gcc_except_tab: 0x28c
   __TEXT.__ustring: 0x3e
-  __TEXT.__unwind_info: 0x1178
-  __TEXT.__objc_classname: 0xd5b
-  __TEXT.__objc_methname: 0xeea6
-  __TEXT.__objc_methtype: 0x1183
-  __TEXT.__objc_stubs: 0x8d40
-  __DATA_CONST.__got: 0x308
-  __DATA_CONST.__const: 0xa48
-  __DATA_CONST.__objc_classlist: 0x2f0
+  __TEXT.__unwind_info: 0x1100
+  __TEXT.__objc_classname: 0xd0e
+  __TEXT.__objc_methname: 0xe81f
+  __TEXT.__objc_methtype: 0x1111
+  __TEXT.__objc_stubs: 0x86e0
+  __DATA_CONST.__got: 0x2e8
+  __DATA_CONST.__const: 0xae8
+  __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a08
-  __DATA_CONST.__objc_superrefs: 0x288
-  __DATA_CONST.__objc_arraydata: 0x4ea8
-  __AUTH_CONST.__auth_got: 0x2d8
-  __AUTH_CONST.__const: 0x980
-  __AUTH_CONST.__cfstring: 0x17fc0
-  __AUTH_CONST.__objc_const: 0xd8f8
-  __AUTH_CONST.__objc_arrayobj: 0x300
+  __DATA_CONST.__objc_selrefs: 0x28f8
+  __DATA_CONST.__objc_superrefs: 0x260
+  __DATA_CONST.__objc_arraydata: 0x4fc8
+  __AUTH_CONST.__auth_got: 0x2c8
+  __AUTH_CONST.__const: 0x9e0
+  __AUTH_CONST.__cfstring: 0x181a0
+  __AUTH_CONST.__objc_const: 0xd628
+  __AUTH_CONST.__objc_arrayobj: 0x330
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x1b0
-  __AUTH.__objc_data: 0xc8
-  __DATA.__objc_ivar: 0x900
+  __AUTH.__objc_data: 0x118
+  __DATA.__objc_ivar: 0x8e8
   __DATA.__data: 0xb48
-  __DATA.__bss: 0x370
-  __DATA_DIRTY.__objc_data: 0x1c98
+  __DATA.__bss: 0x390
+  __DATA_DIRTY.__objc_data: 0x1ba8
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9059EC32-F2F6-31EF-859D-B02ED1735134
-  Functions: 2308
-  Symbols:   7682
-  CStrings:  8954
+  UUID: 257637F4-1F74-3225-BCB8-78AE0C841046
+  Functions: 2272
+  Symbols:   7573
+  CStrings:  8922
 
Symbols:
+ +[SignpostCAInstrumentationProcessor _hitchesSubsystemCategoryArrayForPlatform:]
+ +[SignpostCAInstrumentationProcessor addNeededSCToAllowlist:platform:]
+ +[SignpostCAInstrumentationProcessor filterPassesRequiredSCForCAInstrumentation:platform:]
+ +[SignpostCAInstrumentationProcessor hitchesAllowlistFilterForPlatform:]
+ +[SignpostIntervalBuilder _filterPassesRequiredSCForFramerate:includeMetal:platform:]
+ +[SignpostIntervalBuilder _framerateCalculationAllowlist:platform:]
+ +[SignpostSupportObjectExtractor _checkDateRange:endDate:]
+ -[SSCAMetalLayerOnGlassDrawableInterval includeTimelines]
+ -[SSCAMetalLayerSession _sessionFromFilteredResults:configurationTimeline:onGlassTimeline:errorOut:]
+ -[SignpostAnimationInterval initWithBeginEvent:endEvent:accumulatedState:]
+ -[SignpostAnimationInterval initWithBeginEvent:endEvent:accumulatedState:].cold.1
+ -[SignpostFrameLifetimeInterval initWithInterval:contextArray:isLong:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:]
+ -[SignpostFrameLifetimeInterval initWithInterval:contextArray:isLong:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:].cold.1
+ -[SignpostFrameLifetimeInterval initWithInterval:contextArray:isLong:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:].cold.2
+ -[SignpostFrameLifetimeInterval initWithInterval:contextArray:isLong:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:].cold.3
+ -[SignpostFrameLifetimeInterval initWithInterval:swapID:surfaceID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:isLong:renderInterval:gpuInterval:]
+ -[SignpostFrameLifetimeInterval initWithInterval:swapID:surfaceID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:isLong:renderInterval:gpuInterval:].cold.1
+ -[SignpostFrameLifetimeInterval initWithInterval:swapID:surfaceID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:isLong:renderInterval:gpuInterval:].cold.2
+ -[SignpostFrameLifetimeInterval initWithInterval:swapID:surfaceID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:isLong:renderInterval:gpuInterval:].cold.3
+ -[SignpostFrameLifetimeInterval initWithInterval:swapID:surfaceID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:isLong:renderInterval:gpuInterval:].cold.4
+ -[SignpostFrameLifetimeInterval surfaceID]
+ -[SignpostIntervalBuilder _animationWithBegin:endEvent:]
+ -[SignpostSupportObjectExtractor setTargetPlatform:]
+ -[SignpostSupportObjectExtractor targetPlatform]
+ GCC_except_table44
+ GCC_except_table58
+ GCC_except_table67
+ GCC_except_table70
+ _OBJC_IVAR_$_SignpostFrameLifetimeInterval._surfaceID
+ _OBJC_IVAR_$_SignpostSupportAnimationGraceTimeController._defaultGraceTimeMs
+ _OBJC_IVAR_$_SignpostSupportAnimationGraceTimeController._userInitiatedGraceTimeMs
+ _OBJC_IVAR_$_SignpostSupportAnimationGraceTimeController._userInteractiveGraceTimeMs
+ _OBJC_IVAR_$_SignpostSupportObjectExtractor._targetPlatform
+ _SignpostReporterCrossPlatformMediaAnalysisAllowlist
+ _SignpostReporterCrossPlatformMediaAnalysisAllowlist.cold.1
+ _SignpostReporterCrossPlatformMediaAnalysisAllowlist.onceToken
+ _SignpostReporterCrossPlatformMediaAnalysisAllowlist.stringArray
+ _SignpostReporterCrossPlatformPhotosPersistenceAllowlist
+ _SignpostReporterCrossPlatformPhotosPersistenceAllowlist.cold.1
+ _SignpostReporterCrossPlatformPhotosPersistenceAllowlist.onceToken
+ _SignpostReporterCrossPlatformPhotosPersistenceAllowlist.stringArray
+ _SignpostSupportIsDynamicDataAllowlistedForCurrentDevice
+ _SignpostSupportIsDynamicDataAllowlistedForCurrentDevice.cold.1
+ _SignpostSupportIsDynamicDataAllowlistedForCurrentDevice.curPlatform
+ _SignpostSupportIsDynamicDataAllowlistedForCurrentDevice.onceToken
+ __OBJC_$_CLASS_METHODS_SignpostSupportObjectExtractor
+ ___48-[SignpostAnimationInterval firstFrameLifetimes]_block_invoke
+ ___60-[SignpostContextInfo initWithContextInfoEvent:contributor:]_block_invoke
+ ___68-[SignpostCAInstrumentationProcessor _updatesMatchingFrameLifetime:]_block_invoke.73
+ ___SignpostReporterCrossPlatformMediaAnalysisAllowlist_block_invoke
+ ___SignpostReporterCrossPlatformPhotosPersistenceAllowlist_block_invoke
+ ___SignpostSupportIsDynamicDataAllowlistedForCurrentDevice_block_invoke
+ ___block_descriptor_40_e11_Q16?0i8B12l
+ ___block_literal_global.1013
+ ___block_literal_global.401
+ ___block_literal_global.480
+ ___block_literal_global.529
+ ___block_literal_global.599
+ ___block_literal_global.684
+ ___block_literal_global.688
+ ___block_literal_global.774
+ ___block_literal_global.937
+ ___block_literal_global.939
+ ___block_literal_global.941
+ ___block_literal_global.943
+ ___block_literal_global.945
+ ___block_literal_global.947
+ ___block_literal_global.949
+ _kSSAppKitSubsystem
+ _kSSCAContextInfoName
+ _kSSCAFrameInfoName
+ _kSSCAFrameInfoPresentationTimeArgumentName
+ _kSSCAFrameInfoRequestedPresentationArgumentName
+ _kSSCAFrameLatencyName
+ _kSSCAFrameLifetime
+ _kSSCAIOMFBInMemoryCategory
+ _kSSCAIOMFBStallCategory
+ _kSSCAImageQueueInMemoryCategory
+ _kSSCAImageQueueSampleName
+ _kSSCAImageQueueStallCategory
+ _kSSCAMetalLayerClientDrawableName
+ _kSSCAMetalLayerInMemoryCategory
+ _kSSCAMetalLayerStallCategory
+ _kSSCARenderIntervalName
+ _kSSCASubsystem
+ _kSSCATransactionCommitName
+ _kSSCATransactionInMemoryCategory
+ _kSSCATransactionStallCategory
+ _kSSCAWindowServerInMemoryCategory
+ _kSSCAWindowServerStallCategory
+ _kSSFrameUpdateArgs1Key
+ _kSSFrameUpdateArgs2Key
+ _kSSFrameUpdateContributorsDataKey
+ _kSSFrameUpdateFrameLifetimeIntervalKey
+ _kSSFrameUpdateGPURenderIntervalKey
+ _kSSFrameUpdateName
+ _kSSFrameUpdatePreviousModifierEventKey
+ _kSSFrameUpdatePreviousPresentationEventKey
+ _kSSFrameUpdateRenderServerRenderIntervalKey
+ _kSSSkyLightInMemoryCategory
+ _kSSSkyLightStallsCategory
+ _kSSSkyLightSubsystem
+ _kSSUCUpdateCycleCategory
+ _kSSUCUpdateCycleStallCategory
+ _kSSUCUpdateSequenceName
+ _kSSUIKitSubsystem
+ _objc_msgSend$_animationWithBegin:endEvent:
+ _objc_msgSend$_filterPassesRequiredSCForFramerate:includeMetal:platform:
+ _objc_msgSend$_framerateCalculationAllowlist:platform:
+ _objc_msgSend$_hitchesSubsystemCategoryArrayForPlatform:
+ _objc_msgSend$_sessionFromFilteredResults:configurationTimeline:onGlassTimeline:errorOut:
+ _objc_msgSend$addNeededSCToAllowlist:platform:
+ _objc_msgSend$filterPassesRequiredSCForCAInstrumentation:platform:
+ _objc_msgSend$initWithBeginEvent:endEvent:accumulatedState:
+ _objc_msgSend$initWithInterval:contextArray:isLong:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:
+ _objc_msgSend$initWithInterval:swapID:surfaceID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:isLong:renderInterval:gpuInterval:
+ _objc_msgSend$targetPlatform
+ _objc_msgSend$timeIntervalSinceReferenceDate
+ _serializationTypeNumber.onceToken.398
+ _serializationTypeNumber.onceToken.477
+ _serializationTypeNumber.serializationTypeNumber.399
+ _serializationTypeNumber.serializationTypeNumber.478
- +[SignpostIntervalBuilder _filterPassesRequiredSCForFramerate:includeMetal:]
- +[SignpostIntervalBuilder _framerateCalculationAllowlist:]
- -[SSCAMetalLayerSession _sessionFromFilteredResults:configurationTimeline:errorOut:]
- -[SignpostAnimationAccumulatedState _handleHIDLatency:isLong:isConcise:]
- -[SignpostAnimationAccumulatedState _handleTransactionLifetimeInterval:isLong:isConcise:]
- -[SignpostAnimationInterval firstFrameGraceTimeMCT]
- -[SignpostAnimationInterval firstFrameGraceTime]
- -[SignpostAnimationInterval firstFrameLifetimesWithGraceTimeMCT:]
- -[SignpostAnimationInterval initWithBeginEvent:endEvent:accumulatedState:firstFrameGraceTimeController:]
- -[SignpostAnimationInterval initWithBeginEvent:endEvent:accumulatedState:firstFrameGraceTimeController:].cold.1
- -[SignpostAnimationInterval isFramePossibleFirstFrameForAnimation:]
- -[SignpostAnimationInterval isFramePossibleFirstFrameForAnimation:withGraceTime:]
- -[SignpostAnimationTransactionLifetime initWithTransactionSeedInterval:]
- -[SignpostAnimationTransactionLifetime initWithTransactionSeedInterval:].cold.1
- -[SignpostCAInstrumentationProcessor _handleHIDInterval:]
- -[SignpostCAInstrumentationProcessor _handleHIDInterval:].cold.1
- -[SignpostCAInstrumentationProcessor _handleHIDInterval:].cold.2
- -[SignpostCAStallAggregationBuilder _handleLongTransactionLifetime:]
- -[SignpostEvent _argumentObjectWithPrefix:]
- -[SignpostEvent _argumentObjectWithPrefix:].cold.1
- -[SignpostEvent _argumentObjectWithPrefix:expectedClass:]
- -[SignpostEvent _dataArgumentWithPrefix:]
- -[SignpostEvent _numberArgumentWithPrefix:]
- -[SignpostEvent _stringArgumentWithPrefix:]
- -[SignpostEvent animationType]
- -[SignpostEvent setAnimationType:]
- -[SignpostEvent(Serialization) setAnimationTypeFromRawMetadata:]
- -[SignpostFrameLifetimeInterval initWithInterval:contextArray:hidLatencyInterval:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:]
- -[SignpostFrameLifetimeInterval initWithInterval:contextArray:hidLatencyInterval:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:].cold.1
- -[SignpostFrameLifetimeInterval initWithInterval:contextArray:hidLatencyInterval:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:].cold.2
- -[SignpostFrameLifetimeInterval initWithInterval:contextArray:hidLatencyInterval:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:].cold.3
- -[SignpostFrameLifetimeInterval initWithInterval:contextArray:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:]
- -[SignpostFrameLifetimeInterval initWithInterval:contextArray:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:].cold.1
- -[SignpostFrameLifetimeInterval initWithInterval:swapID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:renderInterval:gpuInterval:]
- -[SignpostFrameLifetimeInterval initWithInterval:swapID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:renderInterval:gpuInterval:].cold.1
- -[SignpostFrameLifetimeInterval initWithInterval:swapID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:renderInterval:gpuInterval:].cold.2
- -[SignpostFrameLifetimeInterval initWithInterval:swapID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:renderInterval:gpuInterval:].cold.3
- -[SignpostFrameLifetimeInterval initWithInterval:swapID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:renderInterval:gpuInterval:].cold.4
- -[SignpostHIDLatencyInterval initWithHIDLatencyInterval:]
- -[SignpostHIDLatencyInterval initWithHIDLatencyInterval:].cold.1
- -[SignpostHIDLatencyInterval initWithStartMCT:endMCT:timebaseRatio:swapID:frameSeed:]
- -[SignpostIntervalBuilder _animationWithBegin:endEvent:firstFrameGraceTimeController:]
- -[SignpostSupportAnimationGraceTime animationType]
- -[SignpostSupportAnimationGraceTime firstFrameGraceTimeMs]
- -[SignpostSupportAnimationGraceTime initWithAnimationType:firstFrameGraceTimeMs:]
- -[SignpostSupportAnimationGraceTime setFirstFrameGraceTimeMs:]
- -[SignpostSupportAnimationGraceTimeController .cxx_destruct]
- -[SignpostSupportAnimationGraceTimeController _setFirstFrameGraceTime:forSubsystem:category:name:]
- -[SignpostSupportAnimationGraceTimeController debugDescription]
- -[SignpostSupportAnimationGraceTimeController defaultGraceTime]
- -[SignpostSupportAnimationGraceTimeController gracetimeForSubsystem:category:name:]
- -[SignpostSupportAnimationGraceTimeController gracetimeMsForSubsystem:category:name:]
- -[SignpostSupportAnimationGraceTimeController setAnimationType:forSubsystem:category:name:]
- -[SignpostSupportAnimationGraceTimeController setFirstFrameGraceTimeMs:forSubsystem:category:name:]
- -[SignpostSupportAnimationGraceTimeController subsystemGraceTimesDictionary]
- -[SignpostSupportAnimationGraceTimeController userInitiatedGraceTime]
- -[SignpostSupportAnimationGraceTimeController userInteractiveGraceTime]
- -[SignpostSupportGraceTimeOverrideEntry .cxx_destruct]
- -[SignpostSupportGraceTimeOverrideEntry debugDescriptionWithWhitespacePrefix:]
- -[SignpostSupportGraceTimeOverrideEntry debugDescription]
- -[SignpostSupportGraceTimeOverrideEntry defaultGraceTime]
- -[SignpostSupportGraceTimeOverrideEntry entryLevel]
- -[SignpostSupportGraceTimeOverrideEntry initWithEntryLevel:]
- -[SignpostSupportGraceTimeOverrideEntry overrides]
- -[SignpostSupportGraceTimeOverrideEntry setDefaultGraceTime:]
- GCC_except_table37
- GCC_except_table48
- GCC_except_table63
- GCC_except_table71
- GCC_except_table74
- _OBJC_CLASS_$_NSRegularExpression
- _OBJC_CLASS_$_SignpostSupportAnimationGraceTime
- _OBJC_CLASS_$_SignpostSupportGraceTimeOverrideEntry
- _OBJC_IVAR_$_SignpostAnimationInterval._firstFrameGraceTime
- _OBJC_IVAR_$_SignpostEvent._animationType
- _OBJC_IVAR_$_SignpostSupportAnimationGraceTime._animationType
- _OBJC_IVAR_$_SignpostSupportAnimationGraceTime._firstFrameGraceTimeMs
- _OBJC_IVAR_$_SignpostSupportAnimationGraceTimeController._defaultGraceTime
- _OBJC_IVAR_$_SignpostSupportAnimationGraceTimeController._subsystemGraceTimesDictionary
- _OBJC_IVAR_$_SignpostSupportAnimationGraceTimeController._userInitiatedGraceTime
- _OBJC_IVAR_$_SignpostSupportAnimationGraceTimeController._userInteractiveGraceTime
- _OBJC_IVAR_$_SignpostSupportGraceTimeOverrideEntry._defaultGraceTime
- _OBJC_IVAR_$_SignpostSupportGraceTimeOverrideEntry._entryLevel
- _OBJC_IVAR_$_SignpostSupportGraceTimeOverrideEntry._overrides
- _OBJC_METACLASS_$_SignpostSupportAnimationGraceTime
- _OBJC_METACLASS_$_SignpostSupportGraceTimeOverrideEntry
- __OBJC_$_INSTANCE_METHODS_SignpostSupportAnimationGraceTime
- __OBJC_$_INSTANCE_METHODS_SignpostSupportGraceTimeOverrideEntry
- __OBJC_$_INSTANCE_VARIABLES_SignpostSupportAnimationGraceTime
- __OBJC_$_INSTANCE_VARIABLES_SignpostSupportGraceTimeOverrideEntry
- __OBJC_$_PROP_LIST_SignpostSupportAnimationGraceTime
- __OBJC_$_PROP_LIST_SignpostSupportGraceTimeOverrideEntry
- __OBJC_CLASS_PROTOCOLS_$_SignpostSupportSubsystemCategoryFilter
- __OBJC_CLASS_RO_$_SignpostSupportAnimationGraceTime
- __OBJC_CLASS_RO_$_SignpostSupportGraceTimeOverrideEntry
- __OBJC_METACLASS_RO_$_SignpostSupportAnimationGraceTime
- __OBJC_METACLASS_RO_$_SignpostSupportGraceTimeOverrideEntry
- ___43-[SignpostEvent _argumentObjectWithPrefix:]_block_invoke
- ___47-[SignpostIntervalBuilder dropAccumulatedState]_block_invoke_7
- ___47-[SignpostIntervalBuilder dropAccumulatedState]_block_invoke_8
- ___63-[SignpostSupportAnimationGraceTimeController debugDescription]_block_invoke
- ___68-[SignpostCAInstrumentationProcessor _updatesMatchingFrameLifetime:]_block_invoke.189
- ___74-[SignpostCAStallAggregationBuilder _initializeCAInstrumentationProcessor]_block_invoke_3
- ___78-[SignpostSupportGraceTimeOverrideEntry debugDescriptionWithWhitespacePrefix:]_block_invoke
- ___block_descriptor_40_e8_32s_e64_v32?0"NSString"8"SignpostSupportGraceTimeOverrideEntry"16^B24ls32l8
- ___block_descriptor_40_e8_32w_e39_v20?0"SignpostHIDLatencyInterval"8B16lw32l8
- ___block_descriptor_40_e8_32w_e49_v20?0"SignpostAnimationTransactionLifetime"8B16lw32l8
- ___block_descriptor_48_e8_32s40s_e64_v32?0"NSString"8"SignpostSupportGraceTimeOverrideEntry"16^B24ls32l8s40l8
- ___block_literal_global.1012
- ___block_literal_global.405
- ___block_literal_global.484
- ___block_literal_global.533
- ___block_literal_global.571
- ___block_literal_global.605
- ___block_literal_global.694
- ___block_literal_global.792
- ___block_literal_global.936
- ___block_literal_global.938
- ___block_literal_global.940
- ___block_literal_global.942
- ___block_literal_global.944
- ___block_literal_global.946
- ___block_literal_global.948
- __argumentObjectWithPrefix:.onceToken
- __argumentObjectWithPrefix:.prefixRegex
- _objc_getProperty
- _objc_msgSend$_animationWithBegin:endEvent:firstFrameGraceTimeController:
- _objc_msgSend$_argumentObjectWithPrefix:
- _objc_msgSend$_argumentObjectWithPrefix:expectedClass:
- _objc_msgSend$_filterPassesRequiredSCForFramerate:includeMetal:
- _objc_msgSend$_framerateCalculationAllowlist:
- _objc_msgSend$_handleHIDInterval:
- _objc_msgSend$_handleHIDLatency:isLong:isConcise:
- _objc_msgSend$_handleLongTransactionLifetime:
- _objc_msgSend$_handleTransactionLifetimeInterval:isLong:isConcise:
- _objc_msgSend$_numberArgumentWithPrefix:
- _objc_msgSend$_sessionFromFilteredResults:configurationTimeline:errorOut:
- _objc_msgSend$_setFirstFrameGraceTime:forSubsystem:category:name:
- _objc_msgSend$allHIDLatencies
- _objc_msgSend$allTransactionLifetimes
- _objc_msgSend$animationFirstFrameGraceTimeController
- _objc_msgSend$contextInfoForHIDInput
- _objc_msgSend$debugDescriptionWithWhitespacePrefix:
- _objc_msgSend$defaultGraceTime
- _objc_msgSend$defaultGraceTimeMs
- _objc_msgSend$entryLevel
- _objc_msgSend$filterPassesRequiredSCForCAInstrumentation:
- _objc_msgSend$firstFrameGraceTime
- _objc_msgSend$firstFrameGraceTimeMCT
- _objc_msgSend$firstFrameGraceTimeMs
- _objc_msgSend$firstFrameLifetimesWithGraceTimeMCT:
- _objc_msgSend$firstMatchInString:options:range:
- _objc_msgSend$gracetimeForSubsystem:category:name:
- _objc_msgSend$hidLatency
- _objc_msgSend$hidLatencyBlock
- _objc_msgSend$hidLatencyInterval
- _objc_msgSend$hidLatencyIsLong
- _objc_msgSend$initWithAnimationType:firstFrameGraceTimeMs:
- _objc_msgSend$initWithBeginEvent:endEvent:accumulatedState:firstFrameGraceTimeController:
- _objc_msgSend$initWithEntryLevel:
- _objc_msgSend$initWithHIDLatencyInterval:
- _objc_msgSend$initWithInterval:contextArray:hidLatencyInterval:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:
- _objc_msgSend$initWithInterval:contextArray:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:
- _objc_msgSend$initWithInterval:swapID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:renderInterval:gpuInterval:
- _objc_msgSend$initWithStartMCT:endMCT:timebaseRatio:swapID:frameSeed:
- _objc_msgSend$initWithTransactionSeedInterval:
- _objc_msgSend$isFramePossibleFirstFrameForAnimation:withGraceTime:
- _objc_msgSend$longHIDLatencies
- _objc_msgSend$longTransactionLifetimes
- _objc_msgSend$numberOfRanges
- _objc_msgSend$overrides
- _objc_msgSend$rangeAtIndex:
- _objc_msgSend$regularExpressionWithPattern:options:error:
- _objc_msgSend$setAnimationType:
- _objc_msgSend$setAnimationType:forSubsystem:category:name:
- _objc_msgSend$setAnimationTypeFromRawMetadata:
- _objc_msgSend$setDefaultGraceTime:
- _objc_msgSend$setFirstFrameGraceTimeMs:
- _objc_msgSend$setHidLatency:
- _objc_msgSend$setHidLatencyBlock:
- _objc_msgSend$setTransactionLifetimeBlock:
- _objc_msgSend$stringByAppendingString:
- _objc_msgSend$substringWithRange:
- _objc_msgSend$subsystemGraceTimesDictionary
- _objc_msgSend$transactionLifetimeBlock
- _objc_msgSend$userInitiatedGraceTime
- _objc_msgSend$userInitiatedGraceTimeMs
- _objc_msgSend$userInteractiveGraceTime
- _objc_msgSend$userInteractiveGraceTimeMs
- _serializationTypeNumber.onceToken.402
- _serializationTypeNumber.onceToken.481
- _serializationTypeNumber.serializationTypeNumber.403
- _serializationTypeNumber.serializationTypeNumber.482
- _strstr
CStrings:
+ "%@%@%@%@%@%@%@%@%@"
+ "-[SignpostFrameLifetimeInterval initWithInterval:contextArray:isLong:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:]"
+ "@100@0:8@16I24I28I32I36B40C44Q48Q56Q64@72B80@84@92"
+ "@48@0:8@16@24@32^@40"
+ "@60@0:8@16@24B32@36@44@52"
+ "Any"
+ "B36@0:8@16B24Q28"
+ "Background"
+ "EffectsAnalysis"
+ "ExecuteCalibration"
+ "ExecuteSafety"
+ "ExecuteTextEncoder"
+ "ExecuteThreshold"
+ "FaceAnalysis"
+ "FilesystemAnalysis"
+ "FilesystemVideoAnalysis"
+ "FrameInfo"
+ "FullImageAnalysis"
+ "LoadCalibration"
+ "LoadSafety"
+ "LoadTextEncoder"
+ "Long commits: %lu long commit(s) out of %lu\nSystemwide Long commits: %lu systemwide long commit(s) out of %lu\nLong client drawables: %lu long client drawable(s) out of %lu\nSystemwide Long client drawables: %lu systemwide long client drawables(s) out of %lu\nLong Frame Latency Count: %lu late frame(s) a total of %lu\nLong CA Render Server Render Count: %lu render(s) out of %lu\nLong Frame Lifetime Count: %lu frame lifetime(s) out of %lu\nLong Contributed Frame Lifetime Count: %lu frame(s) out of %lu\nGlitch Count: %lu glitches (%lu first frame, %lu non-first frame)\nContributed Glitch Count: %lu glitches (%lu first frame, %lu non-first frame)\nGlitch Time Ratio: %.2f ms/s (%.2f ms/s first frame, %.2f ms/s non-first frame)\n"
+ "MediaAnalysis"
+ "MovieHighlightProcessing"
+ "MultiWorkerAnalysis"
+ "OCRAnalysis"
+ "PECAnalysis"
+ "Presentation_time"
+ "Q16@?0i8B12"
+ "QuickFaceIdentification"
+ "Requested_presentation"
+ "SceneAnalysis"
+ "Sceneprint"
+ "SpotlightImageAnalysis"
+ "SpotlightMovieAnalysis"
+ "Start date (%@) >= end date (%@)"
+ "TQ,N,V_defaultGraceTimeMs"
+ "TQ,N,V_targetPlatform"
+ "TQ,N,V_userInitiatedGraceTimeMs"
+ "TQ,N,V_userInteractiveGraceTimeMs"
+ "UserInitiated"
+ "UserInteractive"
+ "Using string allowlist with %lu elements for Unknown/any platform"
+ "Utility"
+ "VideoCaptionAnalysis"
+ "VideoStabilization"
+ "VisualSearchAnalysis"
+ "_animationWithBegin:endEvent:"
+ "_checkDateRange:endDate:"
+ "_defaultGraceTimeMs"
+ "_filterPassesRequiredSCForFramerate:includeMetal:platform:"
+ "_framerateCalculationAllowlist:platform:"
+ "_hitchesSubsystemCategoryArrayForPlatform:"
+ "_sessionFromFilteredResults:configurationTimeline:onGlassTimeline:errorOut:"
+ "_targetPlatform"
+ "_userInitiatedGraceTimeMs"
+ "_userInteractiveGraceTimeMs"
+ "addNeededSCToAllowlist:platform:"
+ "filterPassesRequiredSCForCAInstrumentation:platform:"
+ "hitchesAllowlistFilterForPlatform:"
+ "initWithBeginEvent:endEvent:accumulatedState:"
+ "initWithInterval:contextArray:isLong:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:"
+ "initWithInterval:swapID:surfaceID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:isLong:renderInterval:gpuInterval:"
+ "setTargetPlatform:"
+ "surface_id"
+ "targetPlatform"
+ "timeIntervalSinceReferenceDate"
+ "v32@0:8@16Q24"
- "\n  %@: \n%@"
- "\n%@%@: \n%@"
- "\n%@}"
- "  "
- "    "
- "%@ \nuserInteractiveGraceTimeMs: %llu \nuserInitiatedGraceTimeMs: %llu \ndefaultGraceTimeMs: %llu \noverrides: {%@\n}"
- "%@%@%@%@%@%@%@%@%@%@%@"
- "%@Grace Time Ms: %llu \n%@%@ overrides : %@"
- "(?:^|\\s)([a-zA-Z0-9_]+)[:=]?$"
- "-[SignpostAnimationTransactionLifetime initWithTransactionSeedInterval:]"
- "-[SignpostFrameLifetimeInterval initWithInterval:contextArray:hidLatencyInterval:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:]"
- "-[SignpostFrameLifetimeInterval initWithInterval:contextArray:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:]"
- "-[SignpostHIDLatencyInterval initWithHIDLatencyInterval:]"
- "@\"SignpostSupportAnimationGraceTime\""
- "@\"SignpostSupportAnimationGraceTimeController\"16@0:8"
- "@48@0:8Q16Q24d32I40I44"
- "@56@0:8@16@24@32@40@48"
- "@64@0:8@16@24@32@40@48@56"
- "@92@0:8@16I24I28I32B36C40Q44Q52Q60@68@76@84"
- "Could not find swap_id in %s"
- "HID latencies"
- "HID latency seed mismatch: %#x v. %#x"
- "HIDLatency"
- "Long commits: %lu long commit(s) out of %lu\nSystemwide Long commits: %lu systemwide long commit(s) out of %lu\nLong client drawables: %lu long client drawable(s) out of %lu\nSystemwide Long client drawables: %lu systemwide long client drawables(s) out of %lu\nLong Transaction Lifetimes: %lu long transaction lifetime(s) out of %lu\nLong Frame Latency Count: %lu late frame(s) a total of %lu\nLong HID Latency Count: %lu long HID interval(s) out of %lu\nLong CA Render Server Render Count: %lu render(s) out of %lu\nLong Frame Lifetime Count: %lu frame lifetime(s) out of %lu\nLong Contributed Frame Lifetime Count: %lu frame(s) out of %lu\nGlitch Count: %lu glitches (%lu first frame, %lu non-first frame)\nContributed Glitch Count: %lu glitches (%lu first frame, %lu non-first frame)\nGlitch Time Ratio: %.2f ms/s (%.2f ms/s first frame, %.2f ms/s non-first frame)\n"
- "None"
- "Q40@0:8@16@24@32"
- "Requested to handle a generated hid interval"
- "ScrollView"
- "Scroll_Dragging"
- "Scroll_DraggingAndDeceleration"
- "SignpostSupportAnimationGraceTime"
- "SignpostSupportGraceTimeOverrideEntry"
- "T@\"NSMutableDictionary\",R,N,V_overrides"
- "T@\"NSMutableDictionary\",R,N,V_subsystemGraceTimesDictionary"
- "T@\"SignpostSupportAnimationGraceTime\",&,N,V_defaultGraceTime"
- "T@\"SignpostSupportAnimationGraceTime\",R,N,V_defaultGraceTime"
- "T@\"SignpostSupportAnimationGraceTime\",R,N,V_userInitiatedGraceTime"
- "T@\"SignpostSupportAnimationGraceTime\",R,N,V_userInteractiveGraceTime"
- "T@\"SignpostSupportAnimationGraceTime\",R,V_firstFrameGraceTime"
- "T@\"SignpostSupportAnimationGraceTimeController\",R,N"
- "TQ,N,V_animationType"
- "TQ,N,V_firstFrameGraceTimeMs"
- "TQ,R,N,V_animationType"
- "TQ,R,V_entryLevel"
- "TransactionLifetime"
- "Using string allowlist with %lu elements for Unknown platform"
- "_animationType"
- "_animationWithBegin:endEvent:firstFrameGraceTimeController:"
- "_argumentObjectWithPrefix:"
- "_argumentObjectWithPrefix:expectedClass:"
- "_dataArgumentWithPrefix:"
- "_defaultGraceTime"
- "_entryLevel"
- "_filterPassesRequiredSCForFramerate:includeMetal:"
- "_firstFrameGraceTime"
- "_firstFrameGraceTimeMs"
- "_framerateCalculationAllowlist:"
- "_handleHIDInterval:"
- "_handleHIDLatency:isLong:isConcise:"
- "_handleLongTransactionLifetime:"
- "_handleTransactionLifetimeInterval:isLong:isConcise:"
- "_numberArgumentWithPrefix:"
- "_overrides"
- "_sessionFromFilteredResults:configurationTimeline:errorOut:"
- "_setFirstFrameGraceTime:forSubsystem:category:name:"
- "_stringArgumentWithPrefix:"
- "_subsystemGraceTimesDictionary"
- "_userInitiatedGraceTime"
- "_userInteractiveGraceTime"
- "animation_type=1"
- "animation_type=2"
- "debugDescriptionWithWhitespacePrefix:"
- "defaultGraceTime"
- "entryLevel"
- "firstFrameGraceTime"
- "firstFrameGraceTimeMCT"
- "firstFrameLifetimesWithGraceTimeMCT:"
- "firstMatchInString:options:range:"
- "first_frame_grace_time_ms"
- "gracetimeForSubsystem:category:name:"
- "gracetimeMsForSubsystem:category:name:"
- "initWithAnimationType:firstFrameGraceTimeMs:"
- "initWithBeginEvent:endEvent:accumulatedState:firstFrameGraceTimeController:"
- "initWithEntryLevel:"
- "initWithHIDLatencyInterval:"
- "initWithInterval:contextArray:hidLatencyInterval:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:"
- "initWithInterval:contextArray:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:"
- "initWithInterval:swapID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:renderInterval:gpuInterval:"
- "initWithStartMCT:endMCT:timebaseRatio:swapID:frameSeed:"
- "initWithTransactionSeedInterval:"
- "input_time"
- "isFramePossibleFirstFrameForAnimation:"
- "isFramePossibleFirstFrameForAnimation:withGraceTime:"
- "numberOfRanges"
- "overrides"
- "rangeAtIndex:"
- "regularExpressionWithPattern:options:error:"
- "setAnimationType:"
- "setAnimationType:forSubsystem:category:name:"
- "setAnimationTypeFromRawMetadata:"
- "setDefaultGraceTime:"
- "setFirstFrameGraceTimeMs:"
- "setFirstFrameGraceTimeMs:forSubsystem:category:name:"
- "stringByAppendingString:"
- "substringWithRange:"
- "subsystemGraceTimesDictionary"
- "swap_id"
- "transaction lifetimes"
- "userInitiatedGraceTime"
- "userInteractiveGraceTime"
- "v20@?0@\"SignpostAnimationTransactionLifetime\"8B16"
- "v20@?0@\"SignpostHIDLatencyInterval\"8B16"
- "v32@?0@\"NSString\"8@\"SignpostSupportGraceTimeOverrideEntry\"16^B24"
- "v48@0:8Q16@24@32@40"
- "{"

```
