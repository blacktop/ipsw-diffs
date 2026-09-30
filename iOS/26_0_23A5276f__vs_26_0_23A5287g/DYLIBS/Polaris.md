## Polaris

> `/System/Library/PrivateFrameworks/Polaris.framework/Polaris`

```diff

-220.0.13.0.0
-  __TEXT.__text: 0x12bbfc
-  __TEXT.__auth_stubs: 0x3990
-  __TEXT.__objc_methlist: 0x53b0
-  __TEXT.__const: 0x2ad2
-  __TEXT.__oslogstring: 0xcf84
-  __TEXT.__cstring: 0x140c1
-  __TEXT.__gcc_except_tab: 0x6098
+220.0.17.0.0
+  __TEXT.__text: 0x1310b4
+  __TEXT.__auth_stubs: 0x39b0
+  __TEXT.__objc_methlist: 0x5640
+  __TEXT.__const: 0x2ac2
+  __TEXT.__cstring: 0x143f1
+  __TEXT.__oslogstring: 0xd106
+  __TEXT.__gcc_except_tab: 0x6088
   __TEXT.__swift5_typeref: 0xd71
   __TEXT.__constg_swiftt: 0x590
   __TEXT.__swift5_fieldmd: 0x45c

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_capture: 0x1fc
-  __TEXT.__unwind_info: 0x4170
-  __TEXT.__eh_frame: 0xd80
-  __TEXT.__objc_classname: 0x8f4
-  __TEXT.__objc_methname: 0xda3c
-  __TEXT.__objc_methtype: 0x51b3
-  __TEXT.__objc_stubs: 0x8f20
+  __TEXT.__unwind_info: 0x4200
+  __TEXT.__eh_frame: 0xdb8
+  __TEXT.__objc_classname: 0x908
+  __TEXT.__objc_methname: 0xde44
+  __TEXT.__objc_methtype: 0x5253
+  __TEXT.__objc_stubs: 0x91e0
   __DATA_CONST.__got: 0x720
-  __DATA_CONST.__const: 0x1a90
+  __DATA_CONST.__const: 0x1ab0
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x30b8
+  __DATA_CONST.__objc_selrefs: 0x3158
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x178
+  __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x338
-  __AUTH_CONST.__auth_got: 0x1ce0
+  __AUTH_CONST.__auth_got: 0x1cf0
   __AUTH_CONST.__const: 0x3748
-  __AUTH_CONST.__cfstring: 0x4bc0
-  __AUTH_CONST.__objc_const: 0x8fc8
-  __AUTH_CONST.__objc_intobj: 0x11e8
+  __AUTH_CONST.__cfstring: 0x4be0
+  __AUTH_CONST.__objc_const: 0x92d0
+  __AUTH_CONST.__objc_intobj: 0x1218
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1a30
-  __AUTH.__data: 0x538
+  __AUTH.__data: 0x540
   __AUTH.__thread_vars: 0xc0
   __AUTH.__thread_bss: 0x1e8
-  __DATA.__objc_ivar: 0x670
-  __DATA.__data: 0x1918
-  __DATA.__bss: 0x1b7a0
+  __DATA.__objc_ivar: 0x6ac
+  __DATA.__data: 0x1908
+  __DATA.__bss: 0x1b790
   __DATA.__common: 0x1138
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B4748EDB-44C8-354F-9AD5-9B73A1D62023
-  Functions: 5611
-  Symbols:   14943
-  CStrings:  6602
+  UUID: 133E6F74-821E-3EAC-BBA5-AD5F0FC485BE
+  Functions: 5669
+  Symbols:   15082
+  CStrings:  6668
 
Symbols:
+ -[PSExecutionSession builder]
+ -[PSExecutionSession orchestrator]
+ -[PSExecutionSession setOrchestrator:]
+ -[PSExecutionSessionWorkarounds shouldForceCadencedGSTforDomain:forGraph:systemPulseRate:]
+ -[PSGSTManager initWithGSM:shouldUseOrchestratorV2:]
+ -[PSGSTManager setShouldUseOrchestratorV2:]
+ -[PSGSTManager shouldUseOrchestratorV2]
+ -[PSGraphCompiler3rdPartyReader dealloc]
+ -[PSGraphState domain]
+ -[PSGraphState lowerBoundStride]
+ -[PSGraphState setDomain:]
+ -[PSGraphState setLowerBoundStride:]
+ -[PSGraphState setUpperBoundStride:]
+ -[PSGraphState upperBoundStride]
+ -[PSGraphState_v2 description]
+ -[PSGraphState_v2 lowerBoundStride]
+ -[PSGraphState_v2 setLowerBoundStride:]
+ -[PSGraphState_v2 setUpperBoundStride:]
+ -[PSGraphState_v2 upperBoundStride]
+ -[PSOrchestrator setStatisticsDelegate:]
+ -[PSOrchestrator setSystemPulseRate:]
+ -[PSOrchestrator statisticsDelegate]
+ -[PSOrchestrator systemPulseRate]
+ -[PSOrchestrator(Listener) dumpStateToXPCDictionary:]
+ -[PSOrchestrator(Policy) applyPolicyConstraints:withDesiredStride:]
+ -[PSOrchestrator(Policy) updateGraphTargetState:fromPolicy:].cold.1
+ -[PSOrchestratorStatisticsDelegate .cxx_destruct]
+ -[PSOrchestratorStatisticsDelegate dealloc]
+ -[PSOrchestratorStatisticsDelegate didEndOrchestration]
+ -[PSOrchestratorStatisticsDelegate initWithHistoryCapacity:getTime:]
+ -[PSOrchestratorStatisticsDelegate init]
+ -[PSOrchestratorStatisticsDelegate log]
+ -[PSOrchestratorStatisticsDelegate setLog:]
+ -[PSOrchestratorStatisticsDelegate statistics]
+ -[PSOrchestratorStatisticsDelegate willStartOrchestration]
+ -[PSOrchestrator_v2 initWithQueue:withBuilder:withGSTManager:isSessionForLocalReplay:withSystemPulseRate:]
+ -[PSOrchestrator_v2 setStatisticsDelegate:]
+ -[PSOrchestrator_v2 statisticsDelegate]
+ -[PSOrchestrator_v2(Listener) dumpStateToXPCDictionary:]
+ -[PSOrchestrator_v2(Listener) flushAddedRemovedGraphs]
+ -[PSOrchestrator_v2(Listener) frameIdUpdate:frameId:]
+ -[PSOrchestrator_v2(Listener) frameIdUpdateWithVirtualStride:frameId:]
+ -[PSOrchestrator_v2(Listener) producibleStridesHaveChanged:]
+ -[PSOrchestrator_v2(Listener) resolvedDomainForGraphs:]
+ -[PSOrchestrator_v2(Listener) setupSupportedStridesForLocalReplay:]
+ -[PSOrchestrator_v2(Listener) transitionAddedGraphs:removedGraphs:]
+ -[PSOrchestrator_v2(Policy) applyPolicyConstraints:withDesiredStride:]
+ -[PSOrchestrator_v2(Policy) convertGraphStrideToFrequency:]
+ -[PSOrchestrator_v2(Policy) evaluateAllPolicies]
+ -[PSOrchestrator_v2(Policy) getDefaultResourceFrequency:]
+ -[PSOrchestrator_v2(Policy) setResourceStridesForGraph:]
+ -[PSOrchestrator_v2(Policy) updateGraphTargetState:fromPolicy:]
+ -[PSOrchestrator_v2(Policy) updateGraphTargetState:fromPolicy:].cold.1
+ -[PSSystemGraphListener handleOrchestratorDumpStateMessage:withSession:]
+ GCC_except_table112
+ GCC_except_table171
+ GCC_except_table173
+ GCC_except_table174
+ GCC_except_table237
+ _OBJC_CLASS_$_PSOrchestratorStatisticsDelegate
+ _OBJC_IVAR_$_PSGSTManager._shouldUseOrchestratorV2
+ _OBJC_IVAR_$_PSGraphState._domain
+ _OBJC_IVAR_$_PSGraphState._lowerBoundStride
+ _OBJC_IVAR_$_PSGraphState._upperBoundStride
+ _OBJC_IVAR_$_PSGraphState_v2._lowerBoundStride
+ _OBJC_IVAR_$_PSGraphState_v2._upperBoundStride
+ _OBJC_IVAR_$_PSOrchestrator._statisticsDelegate
+ _OBJC_IVAR_$_PSOrchestrator._systemPulseRate
+ _OBJC_IVAR_$_PSOrchestratorStatisticsDelegate._allTimeStatistics
+ _OBJC_IVAR_$_PSOrchestratorStatisticsDelegate._getTime
+ _OBJC_IVAR_$_PSOrchestratorStatisticsDelegate._log
+ _OBJC_IVAR_$_PSOrchestratorStatisticsDelegate._recentHistory
+ _OBJC_IVAR_$_PSOrchestratorStatisticsDelegate._recentHistoryBufferCapacity
+ _OBJC_IVAR_$_PSOrchestratorStatisticsDelegate._startTime
+ _OBJC_IVAR_$_PSOrchestrator_v2._statisticsDelegate
+ _OBJC_METACLASS_$_PSOrchestratorStatisticsDelegate
+ __OBJC_$_INSTANCE_METHODS_PSOrchestrator(Listener|Policy)
+ __OBJC_$_INSTANCE_METHODS_PSOrchestratorStatisticsDelegate
+ __OBJC_$_INSTANCE_METHODS_PSOrchestrator_v2(Listener|Policy)
+ __OBJC_$_INSTANCE_VARIABLES_PSOrchestratorStatisticsDelegate
+ __OBJC_$_PROP_LIST_PSExecutionSessionResourceAvailability.342
+ __OBJC_$_PROP_LIST_PSOrchestratorStatisticsDelegate
+ __OBJC_CLASS_PROTOCOLS_$_PSOrchestrator(Listener|Policy)
+ __OBJC_CLASS_PROTOCOLS_$_PSOrchestrator_v2(Listener|Policy)
+ __OBJC_CLASS_RO_$_PSOrchestratorStatisticsDelegate
+ __OBJC_METACLASS_RO_$_PSOrchestratorStatisticsDelegate
+ ___40-[PSOrchestratorStatisticsDelegate init]_block_invoke
+ ___67-[PSOrchestrator_v2(Listener) setupSupportedStridesForLocalReplay:]_block_invoke
+ ___67-[PSOrchestrator_v2(Listener) setupSupportedStridesForLocalReplay:]_block_invoke.cold.1
+ ___67-[PSOrchestrator_v2(Listener) setupSupportedStridesForLocalReplay:]_block_invoke_2
+ ___block_descriptor_32_e5_Q8?0l
+ ___block_literal_global.268
+ ___block_literal_global.270
+ ___block_literal_global.273
+ ___block_literal_global.286
+ ___block_literal_global.53
+ _objc_msgSend$applyPolicyConstraints:withDesiredStride:
+ _objc_msgSend$convertGraphStrideToFrequency:
+ _objc_msgSend$defaultFrequencies
+ _objc_msgSend$didEndOrchestration
+ _objc_msgSend$dumpStateToXPCDictionary:
+ _objc_msgSend$frameIdUpdateWithVirtualStride:frameId:
+ _objc_msgSend$getDefaultResourceFrequency:
+ _objc_msgSend$handleOrchestratorDumpStateMessage:withSession:
+ _objc_msgSend$initWithGSM:shouldUseOrchestratorV2:
+ _objc_msgSend$initWithHistoryCapacity:getTime:
+ _objc_msgSend$initWithQueue:withBuilder:withGSTManager:isSessionForLocalReplay:withSystemPulseRate:
+ _objc_msgSend$inputResourcesForGraph:
+ _objc_msgSend$lowerBoundStride
+ _objc_msgSend$orchestrator
+ _objc_msgSend$rootResourcesForGraph:
+ _objc_msgSend$setLowerBoundStride:
+ _objc_msgSend$setProducibleFrequencies:
+ _objc_msgSend$setShouldUseOrchestratorV2:
+ _objc_msgSend$setStatisticsDelegate:
+ _objc_msgSend$setUpperBoundStride:
+ _objc_msgSend$setupProducibleFrequencies:
+ _objc_msgSend$shouldForceCadencedGSTforDomain:forGraph:systemPulseRate:
+ _objc_msgSend$statistics
+ _objc_msgSend$statisticsDelegate
+ _objc_msgSend$upperBoundStride
+ _objc_msgSend$willStartOrchestration
+ _xpc_array_create
- +[PSMSGUtilities sharedInstance]
- +[PSMSGUtilities sharedInstance].cold.1
- -[PSExecutionSessionWorkarounds shouldForceCadencedGSTforDomain:forGraph:]
- -[PSGSTManager initWithGSM:]
- -[PSMSGUtilities currentDisplayFrequency]
- GCC_except_table108
- GCC_except_table132
- GCC_except_table138
- GCC_except_table68
- GCC_except_table83
- _OBJC_CLASS_$_PSMSGUtilities
- _OBJC_METACLASS_$_PSMSGUtilities
- _PSMSGGetCurrentDisplayFrequency
- __OBJC_$_CLASS_METHODS_PSMSGUtilities
- __OBJC_$_INSTANCE_METHODS_PSMSGUtilities
- __OBJC_$_INSTANCE_METHODS_PSOrchestrator(Policy|Listener)
- __OBJC_$_INSTANCE_METHODS_PSOrchestrator_v2
- __OBJC_$_PROP_LIST_PSExecutionSessionResourceAvailability.336
- __OBJC_$_PROP_LIST_PSOrchestrator_v2
- __OBJC_CLASS_PROTOCOLS_$_PSOrchestrator(Policy|Listener)
- __OBJC_CLASS_RO_$_PSMSGUtilities
- __OBJC_METACLASS_RO_$_PSMSGUtilities
- __ZZ32+[PSMSGUtilities sharedInstance]E10__appleMsg
- __ZZ32+[PSMSGUtilities sharedInstance]E9onceToken
- ___32+[PSMSGUtilities sharedInstance]_block_invoke
- ___70-[PSSystemGraphListener builderAddGraphs:execSessionName:addedGraphs:]_block_invoke.cold.1
- ___70-[PSSystemGraphListener builderAddGraphs:execSessionName:addedGraphs:]_block_invoke.cold.2
- ___block_descriptor_tmp.31
- ___block_literal_global.262
- ___block_literal_global.264
- ___block_literal_global.267
- ___block_literal_global.280
- ___block_literal_global.52
- _objc_msgSend$currentDisplayFrequency
- _objc_msgSend$initGlobalWithName:
- _objc_msgSend$initWithGSM:
- _objc_msgSend$shouldForceCadencedGSTforDomain:forGraph:
CStrings:
+ "%s:%d Failed to make resourceID (name: %s, session: %s, storageMode: %llu)"
+ "&"
+ "-[PSOrchestrator(Policy) updateGraphTargetState:fromPolicy:]"
+ "-[PSOrchestrator_v2(Listener) setupSupportedStridesForLocalReplay:]_block_invoke"
+ "-[PSOrchestrator_v2(Policy) updateGraphTargetState:fromPolicy:]"
+ "@\"PSOrchestratorStatisticsDelegate\""
+ "@28@0:8^{ps_gsm_s=C(?={ps_gsm_memory_handles_local_s=^v^v^v^vQQ}{ps_gsm_memory_handles_shared_s=^{PSSharedSerialDataWriter}^{PSSharedSerialDataWriter}^{PSSharedSerialDataWriter}^{PSSharedSerialDataWriter}^{PSSharedSemaphoreArray}^{PSSharedSemaphoreArray}}{ps_gsm_memory_handles_mapped_s=^{PSSharedSerialDataReader}^{PSSharedSerialDataReader}^v^{PSSharedSerialDataReader}^{PSSharedSerialDataReader}^{PSSharedSemaphoreArray}^{PSSharedSemaphoreArray}})^{ps_gsm_gst_meta_s}^{ps_gsm_gst_s}^{ps_gsm_source_meta_s}^{ps_gsm_source_s}^{ps_gsm_source_meta_s}^{ps_gsm_source_s}^{ps_gsm_shared_trigger_meta_s}^{ps_gsm_shared_trigger_s}BAQ@?^{__CFDictionary}^{__CFDictionary}[1024I][128I]B@}16B24"
+ "@32@0:8Q16@?24"
+ "@52@0:8@16@24@32B40@44"
+ "Adding orphaned graph %@ to sourceGraphToAffectedGraph"
+ "Command Queue Full: Request (command=%d, frameid=%lld)"
+ "Failed to add graph to builder: %s"
+ "Failed to make resourceID (name: %s, session: %s, storageMode: %llu)"
+ "OrchestratorStatistics: New max duration: %.1f ms, Seconds since boot: %.1f, Orchestration number: %llu"
+ "Orphaned graph %@ also in sourceGraphToAffectedGraph!"
+ "PSOrchestrator+Listener_v2.m"
+ "PSOrchestratorStatisticsDelegate"
+ "Q8@?0"
+ "Stride dependent graph count %ld does not match total graph count %ld"
+ "Strides current:%@ target:%@ requested:%@ Frequency current:%@ target:%@ Bounds lower:%@ upper:%@ domain:%@"
+ "T@\"NSNumber\",&,N,V_lowerBoundStride"
+ "T@\"NSNumber\",&,N,V_upperBoundStride"
+ "T@\"PSOrchestratorStatisticsDelegate\",&,N,V_statisticsDelegate"
+ "T@,&,N,V_orchestrator"
+ "TB,N,V_shouldUseOrchestratorV2"
+ "Two policies are trying to set target strides. This is an invalid configuration! Aborting!"
+ "^{historyEntry=QQ}"
+ "_allTimeStatistics"
+ "_getTime"
+ "_lowerBoundStride"
+ "_recentHistory"
+ "_recentHistoryBufferCapacity"
+ "_shouldUseOrchestratorV2"
+ "_startTime"
+ "_statisticsDelegate"
+ "_upperBoundStride"
+ "allTimeStatistics"
+ "applyPolicyConstraints:withDesiredStride:"
+ "convertGraphStrideToFrequency:"
+ "desired stride for %@ is %@"
+ "didEndOrchestration"
+ "dumpStateToXPCDictionary:"
+ "duration"
+ "frameIdUpdateWithVirtualStride:frameId:"
+ "getDefaultResourceFrequency:"
+ "getOrphanedGraphsWithSourceGraphToAffectedGraphs:"
+ "getStrideDependentGraphsCountWithStrideDependentGraphs:"
+ "handleOrchestratorDumpStateMessage:withSession:"
+ "history"
+ "historyCount"
+ "initWithGSM:shouldUseOrchestratorV2:"
+ "initWithHistoryCapacity:getTime:"
+ "initWithQueue:withBuilder:withGSTManager:isSessionForLocalReplay:withSystemPulseRate:"
+ "inputResourcesForGraph:"
+ "lowerBoundStride"
+ "numberOfOrchestrationsRecorded"
+ "orchestrationNumber"
+ "orchestrator_statistics"
+ "q24@0:8@16"
+ "root resource are from different MSGs for Graph %@, MSGIDs are %@"
+ "setLowerBoundStride:"
+ "setShouldUseOrchestratorV2:"
+ "setStatisticsDelegate:"
+ "setUpperBoundStride:"
+ "shouldForceCadencedGSTforDomain:forGraph:systemPulseRate:"
+ "sink-applecv3d/lux/oahu/CV3DLuxEstimationResultRef-resource-graph"
+ "startTimestamp"
+ "statistics"
+ "statisticsDelegate"
+ "total"
+ "upperBoundStride"
+ "willStartOrchestration"
+ "xpc_array_get_count(inputNamesArray) (%zd) != xpc_array_get_count(inputStorageModesArray) (%zd) @ %s:%d"
+ "xpc_array_get_count(inputNamesArray) (%zd) != xpc_array_get_count(inputTypesArray) (%zd) @ %s:%d"
+ "xpc_array_get_count(outputNamesArray) (%zd) != xpc_array_get_count(outputStorageModesArray) (%zd) @ %s:%d"
+ "{?=\"max\"{?=\"start\"Q\"duration\"Q\"orchestrationNumber\"Q}\"total\"Q\"numberOfOrchestrations\"Q}"
+ "\x82"
- "@\"PSOrchestrator\""
- "@24@0:8^{ps_gsm_s=C(?={ps_gsm_memory_handles_local_s=^v^v^v^vQQ}{ps_gsm_memory_handles_shared_s=^{PSSharedSerialDataWriter}^{PSSharedSerialDataWriter}^{PSSharedSerialDataWriter}^{PSSharedSerialDataWriter}^{PSSharedSemaphoreArray}^{PSSharedSemaphoreArray}}{ps_gsm_memory_handles_mapped_s=^{PSSharedSerialDataReader}^{PSSharedSerialDataReader}^v^{PSSharedSerialDataReader}^{PSSharedSerialDataReader}^{PSSharedSemaphoreArray}^{PSSharedSemaphoreArray}})^{ps_gsm_gst_meta_s}^{ps_gsm_gst_s}^{ps_gsm_source_meta_s}^{ps_gsm_source_s}^{ps_gsm_source_meta_s}^{ps_gsm_source_s}^{ps_gsm_shared_trigger_meta_s}^{ps_gsm_shared_trigger_s}BAQ@?^{__CFDictionary}^{__CFDictionary}[1024I][128I]B@}16"
- "Command Queue Full: Request (command=%d, frameid=%lld"
- "Error occured while adding graphs within builder %s"
- "Failed to make resourceID (name: %s, session: %s, storageMode: %llu)! This is very bad!"
- "PSMSGUtilities"
- "currentDisplayFrequency"
- "d16@0:8"
- "desired freq for %@ is %@, desired Stride is %@ , requested is %@"
- "initWithGSM:"
- "shouldForceCadencedGSTforDomain:forGraph:"
- "xpc_array_get_count(inputNamesArray) == xpc_array_get_count(inputStorageModesArray)"
- "xpc_array_get_count(inputNamesArray) == xpc_array_get_count(inputTypesArray)"

```
