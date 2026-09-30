## AppleNeuralEngine

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`

```diff

-370.56.0.0.0
-  __TEXT.__text: 0x3a928
-  __TEXT.__auth_stubs: 0xb70
-  __TEXT.__objc_methlist: 0x24b4
-  __TEXT.__const: 0x268
-  __TEXT.__oslogstring: 0x6212
-  __TEXT.__cstring: 0x2b60
-  __TEXT.__gcc_except_tab: 0x3e88
-  __TEXT.__unwind_info: 0x1030
+380.7.0.0.0
+  __TEXT.__text: 0x44924
+  __TEXT.__auth_stubs: 0xbd0
+  __TEXT.__objc_methlist: 0x2614
+  __TEXT.__const: 0x288
+  __TEXT.__oslogstring: 0x80c0
+  __TEXT.__cstring: 0x2d9d
+  __TEXT.__gcc_except_tab: 0x5250
+  __TEXT.__unwind_info: 0x1128
   __TEXT.__objc_classname: 0x2ef
-  __TEXT.__objc_methname: 0x5977
-  __TEXT.__objc_methtype: 0x2359
-  __TEXT.__objc_stubs: 0x3e80
-  __DATA_CONST.__got: 0x278
-  __DATA_CONST.__const: 0x6c8
+  __TEXT.__objc_methname: 0x5fb2
+  __TEXT.__objc_methtype: 0x24a8
+  __TEXT.__objc_stubs: 0x4400
+  __DATA_CONST.__got: 0x298
+  __DATA_CONST.__const: 0x6f0
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14e8
+  __DATA_CONST.__objc_selrefs: 0x1658
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x118
-  __AUTH_CONST.__auth_got: 0x5d0
-  __AUTH_CONST.__const: 0x470
-  __AUTH_CONST.__cfstring: 0x33e0
-  __AUTH_CONST.__objc_const: 0x3628
+  __AUTH_CONST.__auth_got: 0x600
+  __AUTH_CONST.__const: 0x490
+  __AUTH_CONST.__cfstring: 0x3720
+  __AUTH_CONST.__objc_const: 0x3658
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0xc8
-  __DATA.__objc_ivar: 0x1fc
-  __DATA.__data: 0x398
-  __DATA.__bss: 0x148
-  __DATA_DIRTY.__objc_data: 0x9d8
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x200
+  __DATA.__data: 0x3c0
+  __DATA.__bss: 0x158
+  __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0xf8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: E5FA27BE-BA60-38A2-AB8D-5F9D82DD3FCC
-  Functions: 1280
-  Symbols:   4293
-  CStrings:  2397
+  UUID: D062BD17-E0CA-3E8C-AAB9-0CFB3B2DEB80
+  Functions: 1413
+  Symbols:   4632
+  CStrings:  2645
 
Symbols:
+ +[_ANEDataReporter reportTelemetryToCoreAnalytics:payload:]
+ +[_ANEDeviceInfo isBootArgPresent:]
+ +[_ANEErrors badArgumentForMethod:]
+ +[_ANEErrors guestToHostInterfaceTooOld:]
+ +[_ANEErrors virtualizationDataError:]
+ +[_ANEErrors virtualizationHostError:]
+ +[_ANEErrors virtualizationHostError:error:]
+ +[_ANEErrors virtualizationKernelError:kernelErrorCode:]
+ +[_ANEModel modelAtURL:key:mpsConstants:]
+ +[_ANEModel modelAtURLWithSourceURL:sourceURL:key:identifierSource:cacheURLIdentifier:UUID:]
+ +[_ANEModel modelWithCacheURLIdentifier:UUID:]
+ +[_ANEPerformanceStats statsWithReconstructed:hardwareExecutionNS:aneStatsRawData:]
+ +[_ANEStrings binExtension]
+ +[_ANEStrings defaultLLIRBundleName]
+ +[_ANEStrings defaultMLIRFileName]
+ +[_ANEStrings hwxExtension]
+ +[_ANEStrings llirBundleExtension]
+ +[_ANEStrings memoryUnwireAccessEntitlement]
+ +[_ANEStrings testing_defaultMLIRModelName]
+ +[_ANEStrings testing_defaultMLIRModelName].cold.1
+ +[_ANEStrings vm_debugDumpBootArg]
+ +[_ANEVirtualClient copyLLIRBundleToIOSurface:writtenDataSize:]
+ +[_ANEVirtualClient copyLLIRBundleToIOSurface:writtenDataSize:].cold.1
+ +[_ANEVirtualClient copyLLIRBundleToIOSurface:writtenDataSize:].cold.2
+ +[_ANEVirtualClient copyLLIRBundleToIOSurface:writtenDataSize:].cold.3
+ +[_ANEVirtualClient copyLLIRBundleToIOSurface:writtenDataSize:].cold.4
+ +[_ANEVirtualClient copyLLIRBundleToIOSurface:writtenDataSize:].cold.5
+ +[_ANEVirtualClient copyLLIRBundleToIOSurface:writtenDataSize:].cold.6
+ +[_ANEVirtualClient copyLLIRBundleToIOSurface:writtenDataSize:].cold.7
+ +[_ANEVirtualClient copyLLIRBundleToIOSurface:writtenDataSize:].cold.8
+ +[_ANEVirtualClient getCodeSigningIdentity]
+ +[_ANEVirtualClient getCodeSigningIdentity].cold.1
+ +[_ANEVirtualClient getCodeSigningIdentity].cold.2
+ +[_ANEVirtualClient getDictionaryWithJSONEncodingFromIOSurface:withArchivedDataSize:]
+ +[_ANEVirtualClient getDictionaryWithJSONEncodingFromIOSurface:withArchivedDataSize:].cold.1
+ +[_ANEVirtualClient getDictionaryWithJSONEncodingFromIOSurface:withArchivedDataSize:].cold.2
+ +[_ANEVirtualClient getDictionaryWithJSONEncodingFromIOSurface:withArchivedDataSize:].cold.3
+ +[_ANEVirtualClient getObjectFromIOSurface:classType:length:]
+ +[_ANEVirtualClient getObjectFromIOSurface:classType:length:].cold.1
+ +[_ANEVirtualClient getObjectFromIOSurface:classType:length:].cold.2
+ +[_ANEVirtualClient getObjectFromIOSurface:classType:length:].cold.3
+ +[_ANEVirtualClient getObjectFromIOSurface:classType:length:].cold.4
+ +[_ANEVirtualClient getObjectFromIOSurface:classType:length:].cold.5
+ +[_ANEVirtualClient getObjectFromIOSurface:classType:length:].cold.6
+ +[_ANEVirtualClient shouldUsePrecompiledPath:options:shouldUseChunking:chunkingThreshold:]
+ +[_ANEVirtualClient shouldUsePrecompiledPath:options:shouldUseChunking:chunkingThreshold:].cold.1
+ +[_ANEVirtualClient shouldUsePrecompiledPath:options:shouldUseChunking:chunkingThreshold:].cold.2
+ +[_ANEVirtualClient shouldUsePrecompiledPath:options:shouldUseChunking:chunkingThreshold:].cold.3
+ +[_ANEVirtualClient shouldUsePrecompiledPath:options:shouldUseChunking:chunkingThreshold:].cold.4
+ +[_ANEVirtualClient shouldUsePrecompiledPath:options:shouldUseChunking:chunkingThreshold:].cold.5
+ +[_ANEVirtualClient shouldUsePrecompiledPath:options:shouldUseChunking:chunkingThreshold:].cold.6
+ +[_ANEVirtualClient updateError:errorLength:error:]
+ +[_ANEVirtualClient updateError:errorLength:error:].cold.1
+ +[_ANEVirtualClient updatePerformanceStats:performanceStatsLength:perfStatsRawIOSurfaceRef:performanceStatsRawLength:hwExecutionTime:]
+ +[_ANEVirtualClient updatePerformanceStats:performanceStatsLength:perfStatsRawIOSurfaceRef:performanceStatsRawLength:hwExecutionTime:].cold.1
+ +[_ANEVirtualClient updatePerformanceStats:performanceStatsLength:perfStatsRawIOSurfaceRef:performanceStatsRawLength:hwExecutionTime:].cold.2
+ +[_ANEVirtualClient updatePerformanceStats:performanceStatsLength:perfStatsRawIOSurfaceRef:performanceStatsRawLength:hwExecutionTime:].cold.3
+ +[_ANEVirtualClient updatePerformanceStats:performanceStatsLength:perfStatsRawIOSurfaceRef:performanceStatsRawLength:hwExecutionTime:].cold.4
+ +[_ANEVirtualClient updatePerformanceStats:performanceStatsLength:perfStatsRawIOSurfaceRef:performanceStatsRawLength:hwExecutionTime:].cold.5
+ +[_ANEVirtualClient updatePerformanceStats:performanceStatsLength:perfStatsRawIOSurfaceRef:performanceStatsRawLength:hwExecutionTime:].cold.6
+ -[_ANEClient sessionHintWithModel:hint:options:report:error:].cold.4
+ -[_ANEModel initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:mpsConstants:]
+ -[_ANEModel initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:mpsConstants:].cold.1
+ -[_ANEModel initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:mpsConstants:].cold.2
+ -[_ANEModel initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:mpsConstants:].cold.3
+ -[_ANEModel initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:mpsConstants:].cold.4
+ -[_ANEModel mpsConstants]
+ -[_ANEVirtualClient copyAllModelFiles:dictionary:ioSurfaceRefs:].cold.12
+ -[_ANEVirtualClient copyDictionaryToIOSurface:copiedDataSize:createdIOSID:]
+ -[_ANEVirtualClient copyDictionaryToIOSurface:copiedDataSize:createdIOSID:].cold.1
+ -[_ANEVirtualClient copyDictionaryToIOSurface:copiedDataSize:createdIOSID:].cold.2
+ -[_ANEVirtualClient copyDictionaryToIOSurface:copiedDataSize:createdIOSID:].cold.3
+ -[_ANEVirtualClient copyDictionaryToIOSurface:copiedDataSize:createdIOSID:].cold.4
+ -[_ANEVirtualClient copyDictionaryToIOSurface:copiedDataSize:createdIOSID:].cold.5
+ -[_ANEVirtualClient doEvaluateWithModel:options:request:qos:completionEvent:error:].cold.11
+ -[_ANEVirtualClient doEvaluateWithModel:options:request:qos:completionEvent:error:].cold.12
+ -[_ANEVirtualClient loadModel:options:qos:error:].cold.10
+ -[_ANEVirtualClient loadModel:options:qos:error:].cold.11
+ -[_ANEVirtualClient loadModel:options:qos:error:].cold.12
+ -[_ANEVirtualClient loadModelNewInstance:options:modelInstParams:qos:error:].cold.10
+ -[_ANEVirtualClient loadModelNewInstance:options:modelInstParams:qos:error:].cold.11
+ -[_ANEVirtualClient loadModelNewInstance:options:modelInstParams:qos:error:].cold.12
+ -[_ANEVirtualClient loadModelNewInstance:options:modelInstParams:qos:error:].cold.13
+ -[_ANEVirtualClient loadModelNewInstance:options:modelInstParams:qos:error:].cold.14
+ -[_ANEVirtualClient loadModelNewInstance:options:modelInstParams:qos:error:].cold.15
+ -[_ANEVirtualClient loadModelNewInstance:options:modelInstParams:qos:error:].cold.16
+ -[_ANEVirtualClient loadModelNewInstance:options:modelInstParams:qos:error:].cold.17
+ -[_ANEVirtualClient loadModelNewInstance:options:modelInstParams:qos:error:].cold.8
+ -[_ANEVirtualClient loadModelNewInstance:options:modelInstParams:qos:error:].cold.9
+ -[_ANEVirtualClient loadModelNewInstanceLegacy:options:modelInstParams:qos:error:]
+ -[_ANEVirtualClient loadModelNewInstanceLegacy:options:modelInstParams:qos:error:].cold.1
+ -[_ANEVirtualClient loadModelNewInstanceLegacy:options:modelInstParams:qos:error:].cold.2
+ -[_ANEVirtualClient loadModelNewInstanceLegacy:options:modelInstParams:qos:error:].cold.3
+ -[_ANEVirtualClient loadModelNewInstanceLegacy:options:modelInstParams:qos:error:].cold.4
+ -[_ANEVirtualClient loadModelNewInstanceLegacy:options:modelInstParams:qos:error:].cold.5
+ -[_ANEVirtualClient loadModelNewInstanceLegacy:options:modelInstParams:qos:error:].cold.6
+ -[_ANEVirtualClient loadModelNewInstanceLegacy:options:modelInstParams:qos:error:].cold.7
+ -[_ANEVirtualClient sessionHintWithModel:hint:options:report:error:]
+ -[_ANEVirtualClient sessionHintWithModel:hint:options:report:error:].cold.1
+ -[_ANEVirtualClient sessionHintWithModel:hint:options:report:error:].cold.2
+ -[_ANEVirtualClient sessionHintWithModel:hint:options:report:error:].cold.3
+ -[_ANEVirtualClient sessionHintWithModel:hint:options:report:error:].cold.4
+ -[_ANEVirtualClient sessionHintWithModel:hint:options:report:error:].cold.5
+ -[_ANEVirtualClient sessionHintWithModel:hint:options:report:error:].cold.6
+ -[_ANEVirtualClient sessionHintWithModel:hint:options:report:error:].cold.7
+ -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:]
+ -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.1
+ -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.10
+ -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.11
+ -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.12
+ -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.13
+ -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.14
+ -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.15
+ -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.2
+ -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.3
+ -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.4
+ -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.5
+ -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.6
+ -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.7
+ -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.8
+ -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.9
+ -[_ANEVirtualClient validateNetworkCreateMLIR:validation_params:]
+ -[_ANEVirtualClient validateNetworkCreateMLIR:validation_params:].cold.1
+ -[_ANEVirtualClient validateNetworkCreateMLIR:validation_params:].cold.2
+ -[_ANEVirtualClient validateNetworkCreateMLIR:validation_params:].cold.3
+ -[_ANEVirtualClient validateNetworkCreateMLIR:validation_params:].cold.4
+ -[_ANEVirtualClient validateNetworkCreateMLIR:validation_params:].cold.5
+ -[_ANEWeight setWeightURL:]
+ -[_ANEWeight updateWeightURL:]
+ GCC_except_table103
+ GCC_except_table105
+ GCC_except_table106
+ GCC_except_table110
+ GCC_except_table120
+ GCC_except_table121
+ GCC_except_table122
+ GCC_except_table126
+ GCC_except_table131
+ GCC_except_table134
+ GCC_except_table144
+ GCC_except_table18
+ GCC_except_table33
+ GCC_except_table35
+ GCC_except_table40
+ GCC_except_table68
+ GCC_except_table71
+ GCC_except_table72
+ GCC_except_table73
+ GCC_except_table74
+ GCC_except_table87
+ _ANEValidateMILNetworkOnHost
+ _ANEValidateMILNetworkOnHost.cold.1
+ _ANEValidateMLIRNetworkOnHost
+ _ANEValidateNetworkCreate.cold.6
+ _ANEValidateNetworkCreateGenerateFailedGlobalIdentifier
+ _CFDictionaryContainsKey
+ _NSFileSize
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_IVAR_$__ANEModel._mpsConstants
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ __ZN35ANEProgramRequestSharedEventsStructD2Ev
+ __ZNKSt9type_infoeqB8ne200100ERKS_
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne200100Ev
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ ___112-[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:]_block_invoke
+ ___43+[_ANEStrings testing_defaultMLIRModelName]_block_invoke
+ ___59+[_ANEDataReporter reportTelemetryToCoreAnalytics:payload:]_block_invoke
+ ___65-[_ANEVirtualClient evaluateWithModel:options:request:qos:error:]_block_invoke.82
+ ___65-[_ANEVirtualClient evaluateWithModel:options:request:qos:error:]_block_invoke.90
+ ___65-[_ANEVirtualClient validateNetworkCreateMLIR:validation_params:]_block_invoke
+ ___68-[_ANEVirtualClient sessionHintWithModel:hint:options:report:error:]_block_invoke
+ ___76-[_ANEVirtualClient loadModelNewInstance:options:modelInstParams:qos:error:]_block_invoke
+ ___Block_byref_object_copy_.120
+ ___Block_byref_object_copy_.129
+ ___Block_byref_object_copy_.47
+ ___Block_byref_object_copy_.91
+ ___Block_byref_object_dispose_.121
+ ___Block_byref_object_dispose_.130
+ ___Block_byref_object_dispose_.48
+ ___Block_byref_object_dispose_.92
+ ___block_descriptor_100_e8_32s40s48s56s64r72r_e5_v8?0ls32l8s40l8r64l8s48l8s56l8r72l8
+ ___block_descriptor_100_e8_32s40s48s56s64r72r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8r72l8
+ ___block_descriptor_125_ea8_32s40s48s56bs64r72r80r88r_e51_v72?0{ANENotificationMessageStruct=ii^v[4^v][4I]}8lr64l8r72l8s32l8s40l8r80l8s48l8s56l8r88l8
+ ___block_descriptor_48_e8_32s40s_e19_"NSDictionary"8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32r40r_e20_v20?0B8"NSError"12lr32l8r40l8
+ ___block_descriptor_72_e8_32s40r48r_e20_v20?0B8"NSError"12lr40l8r48l8s32l8
+ ___block_descriptor_72_e8_32s40r48r_e33_v28?0B8"NSString"12"NSError"20ls32l8r40l8r48l8
+ ___block_descriptor_76_e8_32s40r48r_e20_v20?0B8"NSError"12lr40l8r48l8s32l8
+ ___block_descriptor_76_e8_32s40r48r_e50_v36?0B8"NSDictionary"12"NSString"20"NSError"28lr40l8s32l8r48l8
+ ___block_descriptor_76_e8_32s40r48r_e59_v56?0B8"NSDictionary"12Q20Q28c36"NSString"40"NSError"48ls32l8r40l8r48l8
+ ___block_descriptor_92_e8_32s40s48s56r64r_e5_v8?0ls32l8r56l8s40l8s48l8r64l8
+ ___block_descriptor_92_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8r56l8s48l8r64l8
+ ___block_descriptor_92_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8s48l8r56l8r64l8
+ ___block_literal_global.228
+ ___block_literal_global.233
+ ___block_literal_global.244
+ ___block_literal_global.258
+ ___block_literal_global.263
+ __os_signpost_emit_with_name_impl
+ _emitEndTracepoint
+ _kANEFConstantSurfaceAlignmentKey
+ _kANEFConstantSurfaceIDKey
+ _kANEFKeepModelMemoryWiredKey
+ _kANEFModelLLIRBundleValue
+ _kANEFModelMLIRValue
+ _mach_continuous_time
+ _objc_alloc_init
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$appendBytes:length:
+ _objc_msgSend$appendData:
+ _objc_msgSend$badArgumentForMethod:
+ _objc_msgSend$binExtension
+ _objc_msgSend$copyDictionaryToIOSurface:copiedDataSize:createdIOSID:
+ _objc_msgSend$copyLLIRBundleToIOSurface:writtenDataSize:
+ _objc_msgSend$data
+ _objc_msgSend$dataNotFoundForMethod:
+ _objc_msgSend$dataWithContentsOfFile:
+ _objc_msgSend$date
+ _objc_msgSend$description
+ _objc_msgSend$fileHandleForReadingAtPath:
+ _objc_msgSend$fileSize
+ _objc_msgSend$getCString:maxLength:encoding:
+ _objc_msgSend$getCodeSigningIdentity
+ _objc_msgSend$getDictionaryWithJSONEncodingFromIOSurface:withArchivedDataSize:
+ _objc_msgSend$getObjectFromIOSurface:classType:length:
+ _objc_msgSend$guestToHostInterfaceTooOld:
+ _objc_msgSend$hwxExtension
+ _objc_msgSend$initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:mpsConstants:
+ _objc_msgSend$isBootArgPresent:
+ _objc_msgSend$lengthOfBytesUsingEncoding:
+ _objc_msgSend$llirBundleExtension
+ _objc_msgSend$loadModelNewInstanceLegacy:options:modelInstParams:qos:error:
+ _objc_msgSend$modelAtURLWithSourceURL:sourceURL:key:identifierSource:cacheURLIdentifier:UUID:
+ _objc_msgSend$mpsConstants
+ _objc_msgSend$rangeOfString:options:range:
+ _objc_msgSend$readDataOfLength:
+ _objc_msgSend$sessionHintWithModel:hint:options:report:error:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setWeightURL:
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$shouldUsePrecompiledPath:options:shouldUseChunking:chunkingThreshold:
+ _objc_msgSend$statsWithReconstructed:hardwareExecutionNS:aneStatsRawData:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:
+ _objc_msgSend$updateError:errorLength:error:
+ _objc_msgSend$updatePerformanceStats:performanceStatsLength:perfStatsRawIOSurfaceRef:performanceStatsRawLength:hwExecutionTime:
+ _objc_msgSend$validateNetworkCreateMLIR:validation_params:
+ _objc_msgSend$virtualizationDataError:
+ _objc_msgSend$virtualizationHostError:
+ _objc_msgSend$virtualizationHostError:error:
+ _objc_msgSend$virtualizationKernelError:kernelErrorCode:
+ _objc_msgSend$vm_debugDumpBootArg
+ _objc_msgSend$writeToFile:atomically:encoding:error:
+ _os_signpost_enabled
+ _os_signpost_id_generate
+ _strcpy
+ _testing_defaultMLIRModelName._ANETestDefaultMLIRModelName
+ _testing_defaultMLIRModelName.onceToken
- +[_ANEPerformanceStats statsWithReconstructed:hardwareExecutionNS:]
- +[_ANEStrings aneuserdCacheDeleteServiceName]
- +[_ANEStrings cacheDeleteServiceName]
- +[_ANEStrings privateANEAccessEntitlement]
- +[_ANEVirtualClient setCodeSigningIdentity:].cold.2
- +[_ANEVirtualClient updatePerformanceStats:performanceStatsLength:hwExecutionTime:]
- +[_ANEVirtualClient updatePerformanceStats:performanceStatsLength:hwExecutionTime:].cold.1
- +[_ANEVirtualClient updatePerformanceStats:performanceStatsLength:hwExecutionTime:].cold.2
- +[_ANEVirtualClient updatePerformanceStats:performanceStatsLength:hwExecutionTime:].cold.3
- +[_ANEVirtualClient updatePerformanceStats:performanceStatsLength:hwExecutionTime:].cold.4
- -[_ANEModel initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:].cold.1
- -[_ANEModel initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:].cold.2
- -[_ANEModel initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:].cold.3
- -[_ANEModel initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:].cold.4
- -[_ANEVirtualClient getObjectFromIOSurface:classType:length:]
- -[_ANEVirtualClient getObjectFromIOSurface:classType:length:].cold.1
- -[_ANEVirtualClient getObjectFromIOSurface:classType:length:].cold.2
- -[_ANEVirtualClient getObjectFromIOSurface:classType:length:].cold.3
- GCC_except_table115
- GCC_except_table130
- GCC_except_table132
- GCC_except_table143
- GCC_except_table23
- GCC_except_table39
- GCC_except_table47
- GCC_except_table54
- GCC_except_table58
- GCC_except_table61
- GCC_except_table62
- GCC_except_table63
- GCC_except_table64
- GCC_except_table88
- GCC_except_table89
- __ZL15LoadDeviceNamedPKcS0_PP15ANEDeviceStructP25ANEDeviceParametersStructPvPF9ANEReturnS6_S2_P24ANEProgramInstanceStruct28ANENotificationMessageStructE
- __ZN35ANEProgramRequestSharedEventsStructD1Ev
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt9type_infoeqB8ne190102ERKS_
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102EPKcm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __Znwm
- ___65-[_ANEVirtualClient evaluateWithModel:options:request:qos:error:]_block_invoke.61
- ___65-[_ANEVirtualClient evaluateWithModel:options:request:qos:error:]_block_invoke.70
- ___block_descriptor_117_ea8_32s40s48s56bs64r72r80r88r_e51_v72?0{ANENotificationMessageStruct=ii^v[4^v][4I]}8lr64l8r72l8s32l8s40l8r80l8s48l8s56l8r88l8
- ___block_descriptor_56_e8_32r40r_e20_v20?0B8"NSError"12lr32l8r40l8
- ___block_descriptor_64_e8_32s40r48r_e20_v20?0B8"NSError"12lr40l8r48l8s32l8
- ___block_descriptor_64_e8_32s40r48r_e33_v28?0B8"NSString"12"NSError"20ls32l8r40l8r48l8
- ___block_descriptor_68_e8_32s40r48r_e20_v20?0B8"NSError"12lr40l8r48l8s32l8
- ___block_descriptor_68_e8_32s40r48r_e50_v36?0B8"NSDictionary"12"NSString"20"NSError"28lr40l8s32l8r48l8
- ___block_descriptor_68_e8_32s40r48r_e59_v56?0B8"NSDictionary"12Q20Q28c36"NSString"40"NSError"48ls32l8r40l8r48l8
- ___block_descriptor_84_e8_32s40s48s56r64r_e5_v8?0ls32l8r56l8s40l8s48l8r64l8
- ___block_descriptor_84_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8r56l8s48l8r64l8
- ___block_descriptor_84_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8s48l8r56l8r64l8
- ___block_descriptor_92_e8_32s40s48s56s64r72r_e5_v8?0ls32l8s40l8r64l8s48l8s56l8r72l8
- ___block_descriptor_92_e8_32s40s48s56s64r72r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8r72l8
- ___block_literal_global.216
- ___block_literal_global.221
- ___block_literal_global.232
- ___block_literal_global.246
- _objc_msgSend$initWithReconstructedData:hardwareExecutionNS:
- _objc_msgSend$statsWithReconstructed:hardwareExecutionNS:
- _objc_msgSend$updatePerformanceStats:performanceStatsLength:hwExecutionTime:
CStrings:
+ " hintParams.hintType:%u hintParams.programHandle:%llu"
+ " r:%p packedQOSandQID:%llu modelStringID:%llu ok:%u"
+ "%@ ANEProgramProcessRequestDirect() for lModel.string_id:0x%08llx waitForResults is %d"
+ "%@: BEGIN loadModel model=%@"
+ "%@: BEGIN loadModelNewInstance model=%@"
+ "%@: Bad argument error"
+ "%@: Begin file transfer to host with fileSize=%llu chunkSize=%u at path=%@"
+ "%@: END loadModel updatedModel=%@"
+ "%@: END loadModelNewInstance success=%d updatedModel=%@"
+ "%@: ERROR : BAD_ARGUMENT : bundlePath is nil!"
+ "%@: ERROR : BAD_ARGUMENT : chunkSize is 0!"
+ "%@: ERROR : BAD_ARGUMENT : error object is nil!"
+ "%@: ERROR : BAD_ARGUMENT : hint object is nil!"
+ "%@: ERROR : BAD_ARGUMENT : input dictionary is nil!"
+ "%@: ERROR : BAD_ARGUMENT : ioSurfaceRef is nil!"
+ "%@: ERROR : BAD_ARGUMENT : length is 0!"
+ "%@: ERROR : BAD_ARGUMENT : passed in archivedDataSize is 0!"
+ "%@: ERROR : BAD_ARGUMENT : passed in file path is nil or empty!"
+ "%@: ERROR : BAD_ARGUMENT : passed in ioSurfaceRef is nil!"
+ "%@: ERROR : BAD_ARGUMENT : return object for writtenDataSize is nil!"
+ "%@: ERROR : BAD_ARGUMENT : return variable for copiedDataSize is nil!"
+ "%@: ERROR : BAD_ARGUMENT : return variable for createdIOSID is nil!"
+ "%@: ERROR : FAILED to copy input validation_params dictionary to IOSurface"
+ "%@: ERROR : FAILED to copy options dictionary to IOSurface"
+ "%@: ERROR : FAILED to create error IOSurface"
+ "%@: ERROR : FAILED to create report IOSurface"
+ "%@: ERROR : FAILED to create validation_result IOSurface"
+ "%@: ERROR : FAILED to get dataArchive for dictionary object"
+ "%@: ERROR : FAILED to get valid dataArchive for dictionary. Data archive length is 0!"
+ "%@: ERROR : Failed to get NSData object"
+ "%@: ERROR : Failed to get object from unarchiver"
+ "%@: ERROR : Failed to get unarchiver object with error=%@"
+ "%@: ERROR : Host reported success=0"
+ "%@: ERROR : INVALID_MODEL : model.programHandle object is nil!"
+ "%@: ERROR : Kernel call failed with error=0x%x"
+ "%@: ERROR : failed to extract archived dictionary with archivedDataSize=%llu err=%@!"
+ "%@: ERROR : failed to get dataBaseAddress for ioSurface!"
+ "%@: ERROR : report from host has no data!"
+ "%@: ERROR : reportDataSize=%llu report=%@"
+ "%@: ERROR : validationResult data size is 0!"
+ "%@: ERROR Failed to create perfStatsRawIOSurfaceRef"
+ "%@: ERROR bundleNameLength is 0! bundlePath=%@"
+ "%@: ERROR failed to extract modelAttributes dictionary!"
+ "%@: ERROR failed to get CSIdentity"
+ "%@: ERROR failed to get CSIdentity, auditToken kernel call failed with ret=0x%x"
+ "%@: ERROR failed to get base address for ioSurfaceRef"
+ "%@: ERROR failed to get fileName from filePathComplete=%@"
+ "%@: ERROR failed to get segment=%d for fileSize=%llu chunkSize=%u at path=%@"
+ "%@: ERROR failed to transfer ANE model file to host! Could not get csIdentity"
+ "%@: ERROR failed to transfer ANE model file to host! Could not read modelInputPath into NSData object"
+ "%@: ERROR failed to transfer ANE model file to host! Could not write csIdentity to struct csIdentityStringLength=%zu bufferLength=%u"
+ "%@: ERROR failed to transfer ANE model file to host! Could not write csIdentity to struct, data will overflow. csIdentityStringLength=%zu > bufferLength=%u"
+ "%@: ERROR failed to transfer ANE model file to host! Failed get attributes for file at path=%@"
+ "%@: ERROR failed to transfer ANE model file to host! Path=%@ is a directory not a file"
+ "%@: ERROR failed to transfer ANE model file to host! file not found at path=%@"
+ "%@: ERROR failed to transfer adapter metadata to host! Could not write uuidString to struct uuidStringLength=%zu bufferLength=%u"
+ "%@: ERROR failed to transfer adapter metadata to host! Could not write uuidString to struct, data will overflow. uuidStringLength=%zu > bufferLength=%u"
+ "%@: ERROR failed to transfer adapter metadata to host, unable to generate modelCacheURLIdentifierData object from cacheURLIdentifier!"
+ "%@: ERROR failed to transfer adapter metadata to host, unable to serialize modelInstParams to NSData!"
+ "%@: ERROR failed to transfer adapter metadata to host, unable to write modelCacheURLIdentifierData to IOSurface!"
+ "%@: ERROR failed to transfer adapter metadata to host, unable to write modelInstParamsIOSurfaceRef data to IOSurface!"
+ "%@: ERROR failed to transfer adapter metadata to host, unable to write options data to IOSurface!"
+ "%@: ERROR failed to transfer file to host! Could not write fileName to struct, data will overflow. fileNameLength=%zu > bufferLength=%u"
+ "%@: ERROR failed to transfer file to host! Could not write uuidString to struct fileNameLength=%zu bufferLength=%u"
+ "%@: ERROR failed to transfer file to host! Could not write uuidString to struct uuidStringLength=%zu bufferLength=%u"
+ "%@: ERROR failed to transfer file to host! Could not write uuidString to struct, data will overflow. uuidStringLength=%zu > bufferLength=%u"
+ "%@: ERROR failed to transfer file to host! Filetype is kVirtANEFileTypeBin but no uuidString provided"
+ "%@: ERROR failed to transfer segment=%d for fileSize=%llu chunkSize=%u chunkDataLength=%llu at path=%@"
+ "%@: ERROR failed to write segment=%d to IOSurface for fileSize=%llu chunkSize=%u chunkDataLength=%llu at path=%@"
+ "%@: ERROR kANEFModelPreCompiledValue not found in options dictionary"
+ "%@: ERROR kernel call failed with ret=0x%x"
+ "%@: ERROR loadModelNewInstance failed, could not UUID for model files!"
+ "%@: ERROR loadModelNewInstance failed, could not get complete name of .asset directory in path=%@!"
+ "%@: ERROR loadModelNewInstance failed, could not get fileSize for file at path=%@!"
+ "%@: ERROR loadModelNewInstance failed, could not transfer file at path=%@!"
+ "%@: ERROR loadModelNewInstance failed, error=%@ trying to get attributes of weight file at path=%@!"
+ "%@: ERROR loadModelNewInstance failed, get overWriteFileName from path=%@!"
+ "%@: ERROR loadModelNewInstance failed, model cacheURLIdentifier is nil!"
+ "%@: ERROR no file at path"
+ "%@: ERROR passed in model is nil"
+ "%@: ERROR passed in options dictionary is nil"
+ "%@: ERROR shouldUseChunking return param is nil!"
+ "%@: ERROR unable to loadModel. Chunking required for file transfer and guest-to-host interface is incompatible. Minimum dataInterfaceVersion=0x%x : Negotiated dataInterfaceVersion=0x%x"
+ "%@: FAILED to create dataBuffer object!"
+ "%@: FAILED to create fileManager object!"
+ "%@: FAILED to create ioSurface of size=%lu!"
+ "%@: FAILED to get attributes for file at path=%@ with error=%@"
+ "%@: FAILED to get data for file %@"
+ "%@: FAILED to get dataBaseAddress for perfStatsRawIOSurfaceRef"
+ "%@: FAILED to get perfStatsRawData object (dataLength=%llu)"
+ "%@: FAILED to write LLIR bundle to IOSurface"
+ "%@: For procedure=%u transferring weight=%u transferring weight file with size=%@ at path=%@"
+ "%@: For procedure=%u weight=%u weight file already transferred at path=%@"
+ "%@: Guest-to-Host interface too old, feature not supported"
+ "%@: Host too old to support sending sessionHint. NegotiatedDataInterfaceVersion=%u"
+ "%@: Host too old to support validateNetworkCreateMLIR. NegotiatedDataInterfaceVersion=%u"
+ "%@: Host too old, model load not supported, negotiatedDataInterfaceVersion=0x%x negotiatedCapabilityMask=0x%llx"
+ "%@: LLIR bundle not supported negotiatedInterfaceVersion=0x%x"
+ "%@: Missing hint"
+ "%@: Missing model"
+ "%@: Path points to a directory, not a file (should not use precompiled path)"
+ "%@: Procedures to load=%lu"
+ "%@: Transferring chunkSeq=%d to host with fileSize=%llu chunkSize=%u at path=%@"
+ "%@: Virtualization data error"
+ "%@: Virtualization host-side error=%@"
+ "%@: Virtualization kernel call failed with error 0x%x"
+ "%@: Virtualization unknown host-side error"
+ "%@: [model.modelURL path]=%@ does not contain a valid bundle path!"
+ "%@: loadModel failed, unable to transfer model files to host"
+ "%@: model and request data dumped to tmpDir=%@"
+ "%@: model is nil!"
+ "%@: modelInstParams is nil!"
+ "%@: using weightFile only, could not find .asset directory in path=%@!"
+ "%@_%@.txt"
+ "%s: Host returned nil validation_result object"
+ "%s: api_version=%llu validation_params=%@"
+ "%s: validation_params do not contain kANECValidateNetworkMILModel or kANECValidateNetworkMLIRModel key"
+ "%u"
+ "%u ok:%u"
+ "%u success:%u"
+ "%{public, signpost.description:begin_time}llu "
+ ".asset"
+ ".bin"
+ ".hwx"
+ ".llir.bundle"
+ "/AppleInternal/Tests/AppleNeuralEngine/AppleNeuralEngine_tests-Runner.app/PlugIns/AppleNeuralEngine_tests.xctest"
+ "@28@0:8@16i24"
+ "@32@0:8^{__IOSurface=}16Q24"
+ "@40@0:8@16Q24@32"
+ "@56@0:8^{__IOSurface=}16Q24^{__IOSurface=}32Q40Q48"
+ "@64@0:8@16@24@32q40@48@56"
+ "@96@0:8@16@24@32@40q48@56@64B72Q76B84@88"
+ "ANECheckPrivilegedVMAccess"
+ "ANEDriver"
+ "ANEServicesDeviceOpen"
+ "B40@0:8^{__IOSurface=}16Q24^@32"
+ "B48@0:8@16@24^B32Q40"
+ "B52@0:8@16I24@28@36@44"
+ "CFDictionaryRef ANEValidateMILNetworkOnHost(uint64_t, CFDictionaryRef)"
+ "MLIR"
+ "No valid model key found"
+ "T@\"NSDictionary\",R,N,V_mpsConstants"
+ "T@\"NSURL\",C,N,V_weightURL"
+ "T^{ANEDeviceStruct=^v^v^vCiQ},N,V_device"
+ "^{ANEDeviceStruct=^v^v^vCiQ}"
+ "^{ANEDeviceStruct=^v^v^vCiQ}16@0:8"
+ "^{__CFDictionary=}32@0:8Q16^{__CFDictionary=}24"
+ "^{__IOSurface=}32@0:8@16^Q24"
+ "^{__IOSurface=}40@0:8@16^Q24^I32"
+ "_ANEF_ADAPTER_LOAD"
+ "_ANEF_COMPILED_MODEL_EXISTS"
+ "_ANEF_ENQUEUE_OUTPUT_SET"
+ "_ANEF_INPUT_BUFFERS_READY"
+ "_ANEF_IOSURFACES_MAP"
+ "_ANEF_IOSURFACES_UNMAP"
+ "_ANEF_MODEL_COMPILE"
+ "_ANEF_MODEL_EVAL"
+ "_ANEF_MODEL_EVALUATE"
+ "_ANEF_MODEL_EVAL_DRIVER_REQUEST"
+ "_ANEF_MODEL_EVAL_PERFCOUNTER_SAMPLE"
+ "_ANEF_MODEL_LOAD"
+ "_ANEF_MODEL_UNLOAD"
+ "_ANEF_PREPARE_CHAINING"
+ "_ANEF_PURGE_COMPILED_MODEL"
+ "_ANEF_SEND_SESSION_HINT"
+ "_mpsConstants"
+ "addEntriesFromDictionary:"
+ "ane_vm_debugDumpBootArg"
+ "appendBytes:length:"
+ "appendData:"
+ "badArgumentForMethod:"
+ "binExtension"
+ "com.apple.ane.memoryUnwiringOptOutAccess.allow"
+ "constantSurfaceAlignment"
+ "copyDictionaryToIOSurface:copiedDataSize:createdIOSID:"
+ "copyLLIRBundleToIOSurface:writtenDataSize:"
+ "data"
+ "dataWithContentsOfFile:"
+ "date"
+ "defaultLLIRBundleName"
+ "defaultMLIRFileName"
+ "fileDataAlreadySent"
+ "fileHandleForReadingAtPath:"
+ "fileSize"
+ "genericFileName"
+ "getCString:maxLength:encoding:"
+ "getCodeSigningIdentity"
+ "getDictionaryWithJSONEncodingFromIOSurface:withArchivedDataSize:"
+ "guestToHostInterfaceTooOld:"
+ "hwxExtension"
+ "i:%lu, counters[i]:%llu, counters[i+1]:%llu, counters[i+2]:%llu"
+ "initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:mpsConstants:"
+ "ioSIDLLIRBundle"
+ "isBootArgPresent:"
+ "kANEFKeepModelMemoryWiredKey"
+ "kANEFModelLLIRBundle"
+ "kANEFModelMLIR"
+ "kANEFconstantSurfaceID"
+ "lengthOfBytesUsingEncoding:"
+ "llirBundleExtension"
+ "llirDataSize"
+ "loadModelNewInstanceLegacy:options:modelInstParams:qos:error:"
+ "memoryUnwireAccessEntitlement"
+ "mlir"
+ "model.bc.mlir"
+ "model.llir.bundle"
+ "model.string_id:%llu"
+ "model.string_id:%llu ok:%u"
+ "model.string_id:%llu success:%u"
+ "modelAtURL:key:mpsConstants:"
+ "modelAtURLWithSourceURL:sourceURL:key:identifierSource:cacheURLIdentifier:UUID:"
+ "modelStringID:%llu numCounters:%lu perfCounterDataVersion:%llu"
+ "modelWithCacheURLIdentifier:UUID:"
+ "model_dump.txt"
+ "mpsConstants"
+ "numWrittenCounters:%lu a1:%llu a2:%llu a3:%llu"
+ "ok:%u"
+ "ok:%u qos:%u model.string_id:%llu"
+ "programHandle=%llu : "
+ "qos:%u"
+ "qos:%u model.string_id:%llu"
+ "qos:%u model.string_id:%llu model.perfStatsMask:%u"
+ "qos:%u model.string_id:%llu model.programHandle:%llu"
+ "qos:%u ok:%u model.string_id:%llu"
+ "qos:%u r:%p modelStringID:%llu completion:%p"
+ "qos:%u r:%p modelStringID:%llu hwExecutionNS:%lu"
+ "rangeOfString:options:range:"
+ "readDataOfLength:"
+ "reportTelemetryToCoreAnalytics:payload:"
+ "request:%p packedQOSandQID:%llu model.string_id:%llu ok:%u"
+ "request:%p qos:%u packedOutputs01:%llu, packedOutputs23%llu"
+ "request_dump.txt"
+ "setDateFormat:"
+ "setWeightURL:"
+ "setWithObject:"
+ "shouldUsePrecompiledPath:options:shouldUseChunking:chunkingThreshold:"
+ "statsWithReconstructed:hardwareExecutionNS:aneStatsRawData:"
+ "stringFromDate:"
+ "substringFromIndex:"
+ "testing_defaultMLIRModelName"
+ "transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:"
+ "updateError:errorLength:error:"
+ "updatePerformanceStats:performanceStatsLength:perfStatsRawIOSurfaceRef:performanceStatsRawLength:hwExecutionTime:"
+ "updateWeightURL:"
+ "v24@0:8^{ANEDeviceStruct=^v^v^vCiQ}16"
+ "validateNetworkCreateMLIR:validation_params:"
+ "virtualizationDataError:"
+ "virtualizationHostError:"
+ "virtualizationHostError:error:"
+ "virtualizationKernelError:kernelErrorCode:"
+ "vm_debugDumpBootArg"
+ "writeToFile:atomically:encoding:error:"
+ "yyyyMMdd_HHmmss"
- "%@ ANEProgramProcessRequestDirect() for lModel %@ waitForResults is %d"
- "%@: ANEVirtualClient evaluateWithModel model=%@ options=%@ request=%@ qos=%d"
- "%@: Missing model or hint"
- "%@: VM currently not supported for ANE hint"
- "%@:ANEVirtualClient start Model=%@ options=%@\n"
- "%s: inValidationParams: %@"
- "%s: nil csIdentity"
- "%s:ANEVirtualClient cannot have nil data."
- "-[_ANEVirtualClient getObjectFromIOSurface:classType:length:]"
- "/AppleInternal/Tests/AppleNeuralEngine/AppleNeuralEngine_tests.xctest"
- "@40@0:8^{__IOSurface=}16Q24Q32"
- "ANEVirtualClient virtualANEModel.ioSIDModelNet=%u virtualANEModel.ioSIDModelShape=%u virtualANEModel.ioSIDModelWeight=%u virtualANEModel.ioSIDKey=%u virtualANEModel.string_id=%lld virtualANEModel.programHandle=%lld virtualANEModel.intermediateBufferHandle=%lld virtualANEModel.queueDepth=%d virtualANEModel.ioSIDModelAttributes=%u virtualANEModel.ModelAttributeLength=%llu virtualANEModel.perfStatsMask=%u virtualANEModel.qos=%u virtualANEModel.ioSIDOptions=%u virtualANEModel.ioSIDErrorValue=%u"
- "H11ANECheckPrivilegedVMAccess"
- "H11ANEDeviceOpen"
- "H1xANELoadBalancer"
- "T@\"NSURL\",R,C,N,V_weightURL"
- "T^{ANEDeviceStruct=^v^v^vCi},N,V_device"
- "UUID UUIDString=%@ : "
- "^{ANEDeviceStruct=^v^v^vCi}"
- "^{ANEDeviceStruct=^v^v^vCi}16@0:8"
- "_ANEVirtualClient calling dictionary loadModel method"
- "aneuserdCacheDeleteServiceName"
- "cacheDeleteServiceName"
- "com.apple.aned.CacheDelete"
- "com.apple.aned.private.ANEAccess.allow"
- "com.apple.aneuserd.CacheDelete"
- "privateANEAccessEntitlement"
- "programHandle=%llu :"
- "statsWithReconstructed:hardwareExecutionNS:"
- "string_id=%llu : "
- "updatePerformanceStats:performanceStatsLength:hwExecutionTime:"
- "v24@0:8^{ANEDeviceStruct=^v^v^vCi}16"

```
