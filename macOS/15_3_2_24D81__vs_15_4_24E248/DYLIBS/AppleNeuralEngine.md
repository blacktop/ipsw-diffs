## AppleNeuralEngine

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/Versions/A/AppleNeuralEngine`

```diff

-370.31.1.0.0
-  __TEXT.__text: 0x3d224
-  __TEXT.__auth_stubs: 0x990
-  __TEXT.__objc_methlist: 0x2324
-  __TEXT.__const: 0x260
-  __TEXT.__oslogstring: 0x5d24
-  __TEXT.__cstring: 0x2993
-  __TEXT.__gcc_except_tab: 0x3e8c
-  __TEXT.__unwind_info: 0xf70
-  __TEXT.__objc_classname: 0x2e7
-  __TEXT.__objc_methname: 0x578c
-  __TEXT.__objc_methtype: 0x22df
-  __TEXT.__objc_stubs: 0x3d80
-  __DATA_CONST.__got: 0x288
+370.56.0.0.0
+  __TEXT.__text: 0x408dc
+  __TEXT.__auth_stubs: 0x9b0
+  __TEXT.__objc_methlist: 0x24b4
+  __TEXT.__const: 0x270
+  __TEXT.__oslogstring: 0x62d8
+  __TEXT.__cstring: 0x2bb7
+  __TEXT.__gcc_except_tab: 0x3eb4
+  __TEXT.__unwind_info: 0x1008
+  __TEXT.__objc_classname: 0x2ef
+  __TEXT.__objc_methname: 0x5994
+  __TEXT.__objc_methtype: 0x2359
+  __TEXT.__objc_stubs: 0x3ee0
+  __DATA_CONST.__got: 0x280
   __DATA_CONST.__const: 0x1f0
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1478
+  __DATA_CONST.__objc_selrefs: 0x14f0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x118
-  __AUTH_CONST.__auth_got: 0x4e0
-  __AUTH_CONST.__const: 0x980
-  __AUTH_CONST.__cfstring: 0x3220
-  __AUTH_CONST.__objc_const: 0x37e8
+  __AUTH_CONST.__auth_got: 0x4f0
+  __AUTH_CONST.__const: 0x9b0
+  __AUTH_CONST.__cfstring: 0x3420
+  __AUTH_CONST.__objc_const: 0x3628
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x5a0
   __DATA.__objc_ivar: 0x1fc
-  __DATA.__data: 0x360
+  __DATA.__data: 0x3a0
   __DATA.__bss: 0x218
   __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: 78D2A338-F9EA-3334-8513-A2691C6FC438
-  Functions: 1242
-  Symbols:   2849
-  CStrings:  2323
+  UUID: 2E86F089-7880-3702-A4F2-627892C5CCA1
+  Functions: 1319
+  Symbols:   2952
+  CStrings:  2406
 
Symbols:
+ +[_ANEClient sharedConnection].cold.1
+ +[_ANEClient sharedPrivateConnection].cold.1
+ +[_ANEDataReporter reportTelemetryToPPS:playload:].cold.5
+ +[_ANEDeviceController initialize].cold.1
+ +[_ANEDeviceController sharedPrivilegedConnection].cold.1
+ +[_ANEDeviceInfo aneArchitectureType].cold.1
+ +[_ANEDeviceInfo aneBoardType].cold.1
+ +[_ANEDeviceInfo buildVersion].cold.1
+ +[_ANEDeviceInfo hasANE].cold.1
+ +[_ANEDeviceInfo hasANE].cold.2
+ +[_ANEDeviceInfo isInternalBuild].cold.1
+ +[_ANEDeviceInfo isVirtualMachine].cold.1
+ +[_ANEDeviceInfo productName].cold.1
+ +[_ANEErrors dataNotFoundForMethod:]
+ +[_ANEErrors notSupportedErrorForMethod:]
+ +[_ANELog common].cold.1
+ +[_ANELog compiler].cold.1
+ +[_ANELog daemon].cold.1
+ +[_ANELog framework].cold.1
+ +[_ANELog maintenance].cold.1
+ +[_ANELog tests].cold.1
+ +[_ANELog tool].cold.1
+ +[_ANEProgramIOSurfacesMapper initialize].cold.1
+ +[_ANEStrings privateANEAccessEntitlement]
+ +[_ANEStrings testing_ThreeSixtyModelName].cold.1
+ +[_ANEStrings testing_encryptedModelNames].cold.1
+ +[_ANEStrings testing_external_precompiledModelPath].cold.1
+ +[_ANEStrings testing_modelNames].cold.1
+ +[_ANEStrings testing_zeroModelName].cold.1
+ +[_ANEStrings vm_allowPrecompiledBinaryBootArg]
+ +[_ANEVirtualClient createIOSurface:ioSID:]
+ +[_ANEVirtualClient sharedConnection].cold.1
+ +[_ANEVirtualClient updateError:errorLength:errorCode:error:]
+ +[_ANEVirtualClient updateError:errorLength:errorCode:error:].cold.1
+ +[_ANEVirtualClient updateError:errorLength:errorCode:error:].cold.2
+ +[_ANEVirtualClient updateError:errorLength:errorCode:error:].cold.3
+ +[_ANEVirtualClient updateError:errorLength:errorCode:error:].cold.4
+ +[_ANEVirtualClient updateError:errorLength:errorCode:error:].cold.5
+ +[_ANEVirtualClient updateError:errorLength:errorCode:error:].cold.6
+ +[_ANEVirtualClient updatePerformanceStats:performanceStatsLength:hwExecutionTime:]
+ +[_ANEVirtualClient updatePerformanceStats:performanceStatsLength:hwExecutionTime:].cold.1
+ +[_ANEVirtualClient updatePerformanceStats:performanceStatsLength:hwExecutionTime:].cold.2
+ +[_ANEVirtualClient updatePerformanceStats:performanceStatsLength:hwExecutionTime:].cold.3
+ +[_ANEVirtualClient updatePerformanceStats:performanceStatsLength:hwExecutionTime:].cold.4
+ -[_ANEClient isAnetoolRootDaemonConnection]
+ -[_ANEClient sessionHintWithModel:hint:options:report:error:]
+ -[_ANEClient sessionHintWithModel:hint:options:report:error:].cold.1
+ -[_ANEClient sessionHintWithModel:hint:options:report:error:].cold.2
+ -[_ANEClient sessionHintWithModel:hint:options:report:error:].cold.3
+ -[_ANEProgramForEvaluation processSessionHint:options:report:error:]
+ -[_ANEProgramForEvaluation processSessionHint:options:report:error:].cold.1
+ -[_ANEProgramForEvaluation processSessionHint:options:report:error:].cold.2
+ -[_ANEVirtualClient validateEnvironmentForPrecompiledBinarySupport]
+ -[_ANEVirtualClient validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:milTextData:]
+ -[_ANEVirtualClient validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:milTextData:].cold.1
+ -[_ANEVirtualClient validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:milTextData:].cold.2
+ -[_ANEVirtualClient validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:milTextData:].cold.3
+ -[_ANEVirtualClient validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:milTextData:].cold.4
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:]
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.1
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.10
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.11
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.12
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.13
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.14
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.15
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.16
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.17
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.18
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.19
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.2
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.20
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.21
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.22
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.23
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.24
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.25
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.26
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.27
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.28
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.29
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.3
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.30
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.31
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.4
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.5
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.6
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.7
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.8
+ -[_ANEVirtualClient(Private) doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:].cold.9
+ ANEValidateNetworkCreateVMHost.cold.1
+ GCC_except_table115
+ GCC_except_table116
+ GCC_except_table117
+ GCC_except_table131
+ GCC_except_table132
+ GCC_except_table133
+ GCC_except_table138
+ GCC_except_table139
+ GCC_except_table140
+ GCC_except_table145
+ GCC_except_table147
+ GCC_except_table148
+ GCC_except_table158
+ GCC_except_table23
+ GCC_except_table36
+ GCC_except_table44
+ GCC_except_table45
+ GCC_except_table53
+ GCC_except_table57
+ GCC_except_table72
+ GCC_except_table74
+ GCC_except_table75
+ GCC_except_table76
+ GCC_except_table77
+ GCC_except_table86
+ GCC_except_table87
+ GCC_except_table88
+ GCC_except_table89
+ GCC_except_table91
+ GCC_except_table92
+ GCC_except_table93
+ GCC_except_table99
+ _OBJC_CLASS_$_NSProcessInfo
+ __73-[_ANEVirtualClient mapIOSurfacesWithModel:request:cacheInference:error:]_block_invoke.95
+ __OBJC_$_INSTANCE_METHODS__ANEVirtualClient(Private)
+ __ZN3MIL4Text12ParseProgramENSt3__110shared_ptrINS_10MILContextEEENS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS_13ParserOptionsE
+ __ZN3MIL4Text9SerializeERKNS_9IRProgramERKNS0_17SerializerOptionsE
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt9type_infoeqB8ne190102ERKS_
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE25__init_copy_ctor_externalEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102EPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ ___83-[_ANEVirtualClient doEvaluateWithModel:options:request:qos:completionEvent:error:]_block_invoke
+ ___block_descriptor_40_ea8_32r_e5_v8?0l
+ ___copy_helper_block_ea8_32r
+ ___destroy_helper_block_ea8_32r
+ __block_literal_global.219
+ __block_literal_global.224
+ __block_literal_global.235
+ __block_literal_global.249
+ _kANEFHintEnergyEfficientWorkloadKey
+ _kANEFHintReportResidentPagesKey
+ _kANEFHintReportSessionStatusKey
+ _kANEFHintReportTotalPagesKey
+ _kANEFHintSessionAbort
+ _kANEFHintSessionInfo
+ _kANEFHintSessionStart
+ _kANEFHintSessionStop
+ _objc_msgSend$arguments
+ _objc_msgSend$createIOSurface:ioSID:
+ _objc_msgSend$invalidModelErrorForMethod:
+ _objc_msgSend$isAnetoolRootDaemonConnection
+ _objc_msgSend$processInfo
+ _objc_msgSend$processName
+ _objc_msgSend$processSessionHint:options:report:error:
+ _objc_msgSend$updateError:errorLength:errorCode:error:
+ _objc_msgSend$updatePerformanceStats:performanceStatsLength:hwExecutionTime:
+ _objc_msgSend$validateEnvironmentForPrecompiledBinarySupport
+ _objc_msgSend$validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:milTextData:
+ _objc_msgSend$vm_allowPrecompiledBinaryBootArg
- -[_ANEVirtualClient doEvaluateWithModel:options:request:qos:completionEvent:error:].cold.11
- -[_ANEVirtualClient doEvaluateWithModel:options:request:qos:completionEvent:error:].cold.12
- -[_ANEVirtualClient doEvaluateWithModel:options:request:qos:completionEvent:error:].cold.13
- -[_ANEVirtualClient doEvaluateWithModel:options:request:qos:completionEvent:error:].cold.14
- -[_ANEVirtualClient doEvaluateWithModel:options:request:qos:completionEvent:error:].cold.15
- -[_ANEVirtualClient doEvaluateWithModel:options:request:qos:completionEvent:error:].cold.16
- -[_ANEVirtualClient doEvaluateWithModel:options:request:qos:completionEvent:error:].cold.17
- -[_ANEVirtualClient doEvaluateWithModel:options:request:qos:completionEvent:error:].cold.18
- -[_ANEVirtualClient doEvaluateWithModel:options:request:qos:completionEvent:error:].cold.19
- -[_ANEVirtualClient doEvaluateWithModel:options:request:qos:completionEvent:error:].cold.20
- -[_ANEVirtualClient doEvaluateWithModel:options:request:qos:completionEvent:error:].cold.21
- -[_ANEVirtualClient validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:]
- -[_ANEVirtualClient validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:].cold.1
- -[_ANEVirtualClient validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:].cold.2
- -[_ANEVirtualClient validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:].cold.3
- GCC_except_table102
- GCC_except_table103
- GCC_except_table126
- GCC_except_table127
- GCC_except_table128
- GCC_except_table129
- GCC_except_table135
- GCC_except_table136
- GCC_except_table141
- GCC_except_table142
- GCC_except_table144
- GCC_except_table154
- GCC_except_table24
- GCC_except_table25
- GCC_except_table26
- GCC_except_table27
- GCC_except_table41
- GCC_except_table48
- GCC_except_table54
- GCC_except_table55
- GCC_except_table58
- GCC_except_table63
- GCC_except_table81
- GCC_except_table82
- GCC_except_table83
- GCC_except_table84
- GCC_except_table96
- GCC_except_table97
- _OUTLINED_FUNCTION_22
- _OUTLINED_FUNCTION_23
- _OUTLINED_FUNCTION_24
- _OUTLINED_FUNCTION_25
- _OUTLINED_FUNCTION_26
- _OUTLINED_FUNCTION_27
- _OUTLINED_FUNCTION_28
- _OUTLINED_FUNCTION_29
- _OUTLINED_FUNCTION_30
- _OUTLINED_FUNCTION_31
- _OUTLINED_FUNCTION_32
- _OUTLINED_FUNCTION_33
- _OUTLINED_FUNCTION_34
- _OUTLINED_FUNCTION_35
- _OUTLINED_FUNCTION_36
- _OUTLINED_FUNCTION_37
- __73-[_ANEVirtualClient mapIOSurfacesWithModel:request:cacheInference:error:]_block_invoke.170
- __OBJC_$_INSTANCE_METHODS__ANEVirtualClient
- __ZN14aneserializers28anemodelnewinstanceparams_v149_ANEModelInstanceParametersSerializerDeserializer12addProcedureEPNS0_39_ANEProcedureDataSerializerDeserializerE
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt9type_infoeqB8ne180100ERKS_
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100ILi0EEEPKc
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne180100Ev
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __block_literal_global.213
- __block_literal_global.218
- __block_literal_global.229
- __block_literal_global.243
- _objc_msgSend$validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:
CStrings:
+ "%@: %@ - 0x%llx"
+ "%@: ANEVirtualClient evaluateWithModel model=%@ options=%@ request=%@ qos=%d"
+ "%@: BAD_ARGUMENT error object is nil"
+ "%@: BAD_ARGUMENT errorIOSurface is nil!"
+ "%@: BAD_ARGUMENT errorLength is 0!"
+ "%@: BAD_ARGUMENT perfStatsIOSurface is NULL!"
+ "%@: Data not found error"
+ "%@: ERROR %@"
+ "%@: ERROR : conditions for precompiled binary support not met! isGuestInternalBuild=%d isHostInternalBuild=%d minimumInterfaceRequirementsMet=%d minimumCapabilityRequirementsMet=%d isPrecompiledBinaryBootArgSet=%d"
+ "%@: ERROR Failed to create errorIOSurface, host-side error reporting will not work"
+ "%@: ERROR Failed to create perfStatsIOSurface"
+ "%@: ERROR Invalid number of completion events"
+ "%@: ERROR failed to get base address for errorIOSurface"
+ "%@: ERROR failed to get string from decoder"
+ "%@: ERROR failed unarchive data:%@"
+ "%@: ERROR optionsArchive length is 0"
+ "%@: FAILED to get dataBaseAddress for perfStatsIOSurfaceRef"
+ "%@: FAILED to get optionsArchive from options dictionary"
+ "%@: FAILED to get perfStatsData object (dataLength=%llu)"
+ "%@: Failed to set session hint %u ret=0x%x"
+ "%@: Missing model or hint"
+ "%@: Not supported"
+ "%@: Program not loaded"
+ "%@: Set session hint %u success"
+ "%@: Unknown hint %@"
+ "%@: VM currently not supported for ANE hint"
+ "%@: Yes"
+ "%@: ioSIDPerStats ioSID: %u statsType : %ld"
+ "%@: milTextData is nil! negotiated interface version 0x%x expects a valid milTextData object"
+ "%@: perfStatsLength=0 hwExecutionTime=0, no perfStats to report"
+ "%@: request.inputArray ioSID: %u"
+ "%@: request.inputIndexArray : %llu"
+ "%@: request.outputArray ioSID: %u"
+ "%@: request.outputIndexArray : %llu"
+ "%@: signal events port is %#x and value is %llu\n"
+ "%@: weightsBufferIOSID: %u"
+ "%s:%d Failed to parse MIL::IRProgram"
+ "-[_ANEVirtualClient validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:milTextData:]"
+ "-u"
+ "@40@0:8^{__IOSurface=}16Q24Q32"
+ "ANEClientEnergyEfficientWorkload"
+ "ANEClientResidentPages"
+ "ANEClientSessionStatus"
+ "ANEClientTotalPages"
+ "ANEHintClientSessionAbort"
+ "ANEHintClientSessionInfo"
+ "ANEHintClientSessionStart"
+ "ANEHintClientSessionStop"
+ "B48@0:8^{__IOSurface=}16Q24q32^@40"
+ "B56@0:8@16@24@32@40^@48"
+ "CFDictionaryRef ANEValidateNetworkCreateVMHost(uint64_t, CFStringRef _Nonnull, CFStringRef _Nonnull, CFStringRef _Nonnull, CFDataRef _Nonnull)"
+ "Inferences failed with unknown host error"
+ "Kernel call failed with error=0x%x"
+ "Private"
+ "^{__CFDictionary=}64@0:8Q16@24@32@40@48@56"
+ "^{__IOSurface=}32@0:8Q16^I24"
+ "ane_vm_allowPrecompiledBinary"
+ "arguments"
+ "com.apple.aned.private.ANEAccess.allow"
+ "createIOSurface:ioSID:"
+ "dataNotFoundForMethod:"
+ "doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:"
+ "isAnetoolRootDaemonConnection"
+ "notSupportedErrorForMethod:"
+ "privateANEAccessEntitlement"
+ "processInfo"
+ "processName"
+ "processSessionHint:options:report:error:"
+ "sessionHintWithModel:hint:options:report:error:"
+ "updateError:errorLength:errorCode:error:"
+ "updatePerformanceStats:performanceStatsLength:hwExecutionTime:"
+ "validateEnvironmentForPrecompiledBinarySupport"
+ "validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:milTextData:"
+ "vm_allowPrecompiledBinaryBootArg"
- "-[_ANEVirtualClient validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:]"
- "ANEVirtualClient evaluateWithModel model: %@\n"
- "ANEVirtualClient evaluateWithModel qos: %d\n"
- "ANEVirtualClient evaluateWithModel request: %@\n"
- "ANEVirtualClient evaluateWithmodel options: %@\n"
- "^{__CFDictionary=}56@0:8Q16@24@32@40@48"
- "validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:"

```
