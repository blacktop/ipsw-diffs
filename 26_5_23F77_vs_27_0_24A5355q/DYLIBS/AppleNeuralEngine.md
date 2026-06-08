## AppleNeuralEngine

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`

```diff

-380.601.0.0.0
-  __TEXT.__text: 0x46104
-  __TEXT.__auth_stubs: 0xb70
-  __TEXT.__objc_methlist: 0x264c
-  __TEXT.__const: 0x280
-  __TEXT.__oslogstring: 0x8375
-  __TEXT.__cstring: 0x2e26
-  __TEXT.__gcc_except_tab: 0x527c
-  __TEXT.__unwind_info: 0x1230
-  __TEXT.__objc_classname: 0x2ef
-  __TEXT.__objc_methname: 0x5fef
-  __TEXT.__objc_methtype: 0x24c8
-  __TEXT.__objc_stubs: 0x4460
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0x6a8
-  __DATA_CONST.__objc_classlist: 0x110
+382.7.4.0.0
+  __TEXT.__text: 0x545e8
+  __TEXT.__objc_methlist: 0x2aec
+  __TEXT.__const: 0x2b0
+  __TEXT.__oslogstring: 0xb365
+  __TEXT.__cstring: 0x36f0
+  __TEXT.__gcc_except_tab: 0x654c
+  __TEXT.__unwind_info: 0x13a8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x890
+  __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1670
+  __DATA_CONST.__weak_got: 0x10
+  __DATA_CONST.__objc_selrefs: 0x19c0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xc8
-  __DATA_CONST.__objc_arraydata: 0x118
-  __AUTH_CONST.__auth_got: 0x5d0
-  __AUTH_CONST.__const: 0x490
-  __AUTH_CONST.__cfstring: 0x3a80
-  __AUTH_CONST.__objc_const: 0x3658
+  __DATA_CONST.__objc_superrefs: 0xd8
+  __DATA_CONST.__objc_arraydata: 0x120
+  __DATA_CONST.__got: 0x2f0
+  __AUTH_CONST.__const: 0x4d0
+  __AUTH_CONST.__cfstring: 0x48a0
+  __AUTH_CONST.__objc_const: 0x3c48
+  __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x200
-  __DATA.__data: 0x3c0
-  __DATA.__bss: 0x160
+  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__auth_got: 0x658
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x234
+  __DATA.__data: 0x6e8
+  __DATA.__bss: 0x180
   __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0xf8

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: A5BF7AB7-F083-3561-BE49-41D624F80C4C
-  Functions: 1446
-  Symbols:   4752
-  CStrings:  2715
+  UUID: 9B6E1258-7C16-3394-808E-F0A72D5261D2
+  Functions: 1690
+  Symbols:   5661
+  CStrings:  1969
 
Symbols:
+ +[NSFileManager(ANE) sizeOfDirectoryOrFileAtPath:]
+ +[NSFileManager(ANE) sizeOfDirectoryOrFileAtPath:].cold.1
+ +[_ANEDebugUtils applyDebugEnvToOptions:]
+ +[_ANEDebugUtils applyDebugEnvToOptions:].cold.1
+ +[_ANEDebugUtils applyDebugEnvToOptions:].cold.2
+ +[_ANEDebugUtils applyDebugEnvToOptions:].cold.3
+ +[_ANEDebugUtils parseDebugEnvVar]
+ +[_ANEDebugUtils parseDebugString:]
+ +[_ANEErrors mappingMutableWeightsBufferFailed:]
+ +[_ANEErrors programTooLargeErrorForMethod:]
+ +[_ANEErrors unmappingMutableWeightsBufferFailed:]
+ +[_ANEIntermediateTensor descriptorWithName:index:]
+ +[_ANEIntermediateTensor supportsSecureCoding]
+ +[_ANEModel modelAtURL:key:externConstants:]
+ +[_ANEModel uuidV5FromString:]
+ +[_ANEModel uuidV5FromURL:]
+ +[_ANEModelToken teamScopedCodeSigningIDFor:processIdentifier:]
+ +[_ANEModelToken teamScopedCodeSigningIDFor:processIdentifier:].cold.1
+ +[_ANEPerformanceStats decodeDescriptor:perTdPerfCounters:]
+ +[_ANEPerformanceStats decodePerformanceStats:withOptions:]
+ +[_ANEPerformanceStats decodePerformanceStats:withOptions:].cold.1
+ +[_ANEPerformanceStats decodePerformanceStats:withOptions:].cold.2
+ +[_ANEPerformanceStats decodePerformanceStats:withOptions:].cold.3
+ +[_ANEPerformanceStats decodePerformanceStats:withOptions:].cold.4
+ +[_ANEPerformanceStats decodeRawStatsData:]
+ +[_ANEPerformanceStats decodeRawStatsData:].cold.1
+ +[_ANEPerformanceStats decodeRawStatsData:].cold.2
+ +[_ANEPerformanceStats decodeRawStatsData:].cold.3
+ +[_ANEPerformanceStats dumpPerformanceStatsRawData:]
+ +[_ANEPerformanceStats stringForEventType:]
+ +[_ANEStrings mutableWeightsMappingAccessEntitlement]
+ +[_ANEStrings trimmedModelPath:trimmedPathOut:]
+ +[_ANETensorDebugHelper normalizeTensor:descriptor:error:]
+ +[_ANETensorDebugHelper normalizeTensor:descriptor:error:].cold.1
+ +[_ANETensorDebugHelper normalizeTensor:descriptor:error:].cold.2
+ +[_ANETensorDebugHelper queryTensorsFromDebugFile:error:]
+ +[_ANETensorDebugHelper queryTensorsFromDebugFile:error:].cold.1
+ +[_ANETensorDebugHelper queryTensorsFromModel:error:]
+ +[_ANETensorDebugHelper queryTensorsFromModel:error:].cold.1
+ +[_ANETensorDebugHelper queryTensorsFromModel:error:].cold.2
+ +[_ANETensorDebugHelper validateDebugInfoFile:error:]
+ +[_ANETensorDebugHelper validateDebugInfoFile:error:].cold.1
+ +[_ANETensorDebugHelper validateDebugInfoFile:error:].cold.2
+ +[_ANETensorDebugHelper validateDebugInfoFile:error:].cold.3
+ +[_ANETensorDebugHelper validateDebugInfoFile:error:].cold.4
+ +[_ANETensorDebugHelper validateDebugInfoFile:error:].cold.5
+ +[_ANEVirtualClient createCFDictionaryFromIOSurface:dataLength:]
+ +[_ANEVirtualClient createCFDictionaryFromIOSurface:dataLength:].cold.1
+ +[_ANEVirtualClient createCFDictionaryFromIOSurface:dataLength:].cold.2
+ +[_ANEVirtualClient createCFDictionaryFromIOSurface:dataLength:].cold.3
+ +[_ANEVirtualClient createCFDictionaryFromIOSurface:dataLength:].cold.4
+ +[_ANEVirtualClient createCFDictionaryFromIOSurface:dataLength:].cold.5
+ +[_ANEVirtualClient deserializeHostErrorFromData:]
+ +[_ANEVirtualClient deserializeHostErrorFromData:].cold.1
+ +[_ANEVirtualClient deserializeHostErrorFromData:].cold.2
+ +[_ANEVirtualClient doesPath:matchPattern:withFullPath:]
+ +[_ANEVirtualClient extractMpsConstantsIOSurfaceIDs:ioSIDArray:keysArray:]
+ +[_ANEVirtualClient extractMpsConstantsIOSurfaceIDs:ioSIDArray:keysArray:].cold.1
+ +[_ANEVirtualClient extractMpsConstantsIOSurfaceIDs:ioSIDArray:keysArray:].cold.2
+ +[_ANEVirtualClient extractMpsConstantsIOSurfaceIDs:ioSIDArray:keysArray:].cold.3
+ +[_ANEVirtualClient extractMpsConstantsIOSurfaceIDs:ioSIDArray:keysArray:].cold.4
+ +[_ANEVirtualClient findMatchingAssetPaths:inDirectory:]
+ +[_ANEVirtualClient findPathsMatchingPattern:inDirectory:]
+ +[_ANEVirtualClient getPatternsForModelType:]
+ +[_ANEVirtualClient getPatternsForModelType:].cold.1
+ +[_ANEVirtualClient populateCSIdentity:maxLength:]
+ +[_ANEVirtualClient populateNSString:toBuffer:maxLength:]
+ +[_ANEVirtualClient populateNSString:toBuffer:maxLength:].cold.1
+ +[_ANEVirtualClient populateUUID:maxLength:fromString:]
+ +[_ANEVirtualClient populateUUID:maxLength:fromString:].cold.1
+ +[_ANEWeight weightWithSymbol:]
+ -[_ANEClient mapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:]
+ -[_ANEClient mapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.1
+ -[_ANEClient mapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.2
+ -[_ANEClient mapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.3
+ -[_ANEClient mapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.4
+ -[_ANEClient mapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.5
+ -[_ANEClient mapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.6
+ -[_ANEClient mapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.7
+ -[_ANEClient mapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.8
+ -[_ANEClient mapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.9
+ -[_ANEClient syncMutableWeightsForModel:andProcedure:fromOffset:withSize:error:]
+ -[_ANEClient syncMutableWeightsForModel:andProcedure:fromOffset:withSize:error:].cold.1
+ -[_ANEClient unmapMutableWeightsForModel:andProcedure:]
+ -[_ANEClient unmapMutableWeightsForModel:andProcedure:].cold.1
+ -[_ANEClient unmapMutableWeightsForModel:andProcedure:].cold.2
+ -[_ANEClient unmapMutableWeightsForModel:andProcedure:].cold.3
+ -[_ANEClient unmapMutableWeightsForModel:andProcedure:].cold.4
+ -[_ANEClient unmapMutableWeightsForModel:andProcedure:].cold.5
+ -[_ANEClient unmapMutableWeightsForModel:andProcedure:].cold.6
+ -[_ANEClient updatePurgeabilityLevelForModelTrackedByHash:to:]
+ -[_ANEClient updateSourcePathForModelTrackedByHash:to:error:]
+ -[_ANEDaemonConnection updatePurgeabilityLevelForModelTrackedByHash:to:withReply:]
+ -[_ANEDaemonConnection updateSourcePathForModelTrackedByHash:to:withReply:]
+ -[_ANEIntermediateTensor .cxx_destruct]
+ -[_ANEIntermediateTensor copyWithZone:]
+ -[_ANEIntermediateTensor encodeWithCoder:]
+ -[_ANEIntermediateTensor initWithCoder:]
+ -[_ANEIntermediateTensor initWithName:index:]
+ -[_ANEIntermediateTensor tensorIndex]
+ -[_ANEIntermediateTensor tensorName]
+ -[_ANEModel externConstants]
+ -[_ANEModel initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:mpsConstants:externConstants:programHandle:intermediateBufferHandle:queueDepth:perfStatsMask:state:]
+ -[_ANEModel initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:mpsConstants:externConstants:programHandle:intermediateBufferHandle:queueDepth:perfStatsMask:state:].cold.1
+ -[_ANEModel initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:mpsConstants:externConstants:programHandle:intermediateBufferHandle:queueDepth:perfStatsMask:state:].cold.2
+ -[_ANEModel initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:mpsConstants:externConstants:programHandle:intermediateBufferHandle:queueDepth:perfStatsMask:state:].cold.3
+ -[_ANEModel initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:mpsConstants:externConstants:programHandle:intermediateBufferHandle:queueDepth:perfStatsMask:state:].cold.4
+ -[_ANEModel numInputs]
+ -[_ANEModel numOutputs]
+ -[_ANEModel proceduresCount]
+ -[_ANEModel procedures]
+ -[_ANEModel setExternConstants:]
+ -[_ANEModel setModelURL:]
+ -[_ANEModel setMpsConstants:]
+ -[_ANEModel setNumInputs:]
+ -[_ANEModel setNumOutputs:]
+ -[_ANEModel setProcedures:]
+ -[_ANEModel updateFromModel:shouldUpdateModelURL:shouldUpdateUUID:]
+ -[_ANEModel updateFromModel:shouldUpdateModelURL:shouldUpdateUUID:].cold.1
+ -[_ANEModel updateModelAttributes:state:programHandle:intermediateBufferHandle:queueDepth:numInputs:numOutputs:]
+ -[_ANEProcedureData mutableWeightsBufferID]
+ -[_ANEProcedureData mutableWeightsBufferSize]
+ -[_ANEProcedureData setMutableWeightsBufferID:]
+ -[_ANEProcedureData setMutableWeightsBufferSize:]
+ -[_ANEProgramForEvaluation .cxx_construct]
+ -[_ANEProgramForEvaluation deviceController]
+ -[_ANEProgramForEvaluation mapMutableWeightsBufferDirectForProcedure:bufferID:buffer:size:error:]
+ -[_ANEProgramForEvaluation mapMutableWeightsBufferDirectForProcedure:bufferID:buffer:size:error:].cold.1
+ -[_ANEProgramForEvaluation mapMutableWeightsBufferDirectForProcedure:bufferID:buffer:size:error:].cold.2
+ -[_ANEProgramForEvaluation mapMutableWeightsBufferDirectForProcedure:bufferID:buffer:size:error:].cold.3
+ -[_ANEProgramForEvaluation unmapMutableWeightsBufferDirectForProcedure:bufferID:]
+ -[_ANEProgramForEvaluation unmapMutableWeightsBufferDirectForProcedure:bufferID:].cold.1
+ -[_ANEProgramForEvaluation unmapMutableWeightsBufferDirectForProcedure:bufferID:].cold.2
+ -[_ANEProgramProcedurePriv .cxx_destruct]
+ -[_ANEProgramProcedurePriv dealloc]
+ -[_ANEProgramProcedurePriv dealloc].cold.1
+ -[_ANEProgramProcedurePriv initWithSymbolName:]
+ -[_ANEProgramProcedurePriv mutableWeightsBufferPtr]
+ -[_ANEProgramProcedurePriv mutableWeightsBuffer]
+ -[_ANEProgramProcedurePriv setMutableWeightsBuffer:]
+ -[_ANEProgramProcedurePriv setSymbolName:]
+ -[_ANEProgramProcedurePriv symbolName]
+ -[_ANEVirtualClient .cxx_construct]
+ -[_ANEVirtualClient assetExistsOnHost:]
+ -[_ANEVirtualClient assetExistsOnHost:].cold.1
+ -[_ANEVirtualClient assetExistsOnHost:].cold.2
+ -[_ANEVirtualClient assetExistsOnHost:].cold.3
+ -[_ANEVirtualClient assetExistsOnHost:].cold.4
+ -[_ANEVirtualClient assetExistsOnHost:].cold.5
+ -[_ANEVirtualClient compileModel:options:qos:error:].cold.10
+ -[_ANEVirtualClient compileModel:options:qos:error:].cold.11
+ -[_ANEVirtualClient compileModel:options:qos:error:].cold.12
+ -[_ANEVirtualClient compileModel:options:qos:error:].cold.13
+ -[_ANEVirtualClient compileModel:options:qos:error:].cold.7
+ -[_ANEVirtualClient compileModel:options:qos:error:].cold.8
+ -[_ANEVirtualClient compileModel:options:qos:error:].cold.9
+ -[_ANEVirtualClient compileModelLegacy:options:qos:error:]
+ -[_ANEVirtualClient compileModelLegacy:options:qos:error:].cold.1
+ -[_ANEVirtualClient compileModelLegacy:options:qos:error:].cold.2
+ -[_ANEVirtualClient compileModelLegacy:options:qos:error:].cold.3
+ -[_ANEVirtualClient compileModelLegacy:options:qos:error:].cold.4
+ -[_ANEVirtualClient compileModelLegacy:options:qos:error:].cold.5
+ -[_ANEVirtualClient compileModelLegacy:options:qos:error:].cold.6
+ -[_ANEVirtualClient compiledModelExistsFor:].cold.10
+ -[_ANEVirtualClient compiledModelExistsFor:].cold.6
+ -[_ANEVirtualClient compiledModelExistsFor:].cold.7
+ -[_ANEVirtualClient compiledModelExistsFor:].cold.8
+ -[_ANEVirtualClient compiledModelExistsFor:].cold.9
+ -[_ANEVirtualClient compiledModelExistsForLegacy:]
+ -[_ANEVirtualClient compiledModelExistsForLegacy:].cold.1
+ -[_ANEVirtualClient compiledModelExistsForLegacy:].cold.2
+ -[_ANEVirtualClient compiledModelExistsForLegacy:].cold.3
+ -[_ANEVirtualClient compiledModelExistsForLegacy:].cold.4
+ -[_ANEVirtualClient compiledModelExistsForLegacy:].cold.5
+ -[_ANEVirtualClient copyModelAttributesToDictionary:dictionary:vmData:]
+ -[_ANEVirtualClient copyModelMetaData:options:dictionary:vmData:shouldEncodeKey:]
+ -[_ANEVirtualClient copyModelMetaData:options:dictionary:vmData:shouldEncodeKey:].cold.1
+ -[_ANEVirtualClient copyModelMetaData:options:dictionary:vmData:shouldEncodeKey:].cold.2
+ -[_ANEVirtualClient copyModelMetaData:options:dictionary:vmData:shouldEncodeKey:].cold.3
+ -[_ANEVirtualClient createIOSurfaceWithData:length:ioSID:]
+ -[_ANEVirtualClient createIOSurfaceWithData:length:ioSID:].cold.1
+ -[_ANEVirtualClient createIOSurfaceWithData:length:ioSID:].cold.2
+ -[_ANEVirtualClient createIOSurfaceWithData:length:ioSID:].cold.3
+ -[_ANEVirtualClient createIOSurfaceWithData:size:ioSID:]
+ -[_ANEVirtualClient createIOSurfaceWithData:size:ioSID:].cold.1
+ -[_ANEVirtualClient createIOSurfaceWithData:size:ioSID:].cold.2
+ -[_ANEVirtualClient createIOSurfaceWithData:size:ioSID:].cold.3
+ -[_ANEVirtualClient createValidationResultForNetworkCreateMLIR:validation_params:]
+ -[_ANEVirtualClient createValidationResultForNetworkCreateMLIR:validation_params:].cold.1
+ -[_ANEVirtualClient createValidationResultForNetworkCreateMLIR:validation_params:].cold.2
+ -[_ANEVirtualClient createValidationResultForNetworkCreateMLIR:validation_params:].cold.3
+ -[_ANEVirtualClient createValidationResultForNetworkCreateMLIR:validation_params:].cold.4
+ -[_ANEVirtualClient createValidationResultForNetworkCreateMLIR:validation_params:].cold.5
+ -[_ANEVirtualClient doMapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:]
+ -[_ANEVirtualClient doMapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.1
+ -[_ANEVirtualClient doMapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.2
+ -[_ANEVirtualClient doMapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.3
+ -[_ANEVirtualClient doMapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.4
+ -[_ANEVirtualClient doMapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.5
+ -[_ANEVirtualClient doMapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.6
+ -[_ANEVirtualClient doMapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.7
+ -[_ANEVirtualClient doMapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.8
+ -[_ANEVirtualClient doMapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.9
+ -[_ANEVirtualClient doSyncMutableWeightsForModel:andProcedure:fromOffset:withSize:error:]
+ -[_ANEVirtualClient doSyncMutableWeightsForModel:andProcedure:fromOffset:withSize:error:].cold.1
+ -[_ANEVirtualClient doSyncMutableWeightsForModel:andProcedure:fromOffset:withSize:error:].cold.2
+ -[_ANEVirtualClient doSyncMutableWeightsForModel:andProcedure:fromOffset:withSize:error:].cold.3
+ -[_ANEVirtualClient doSyncMutableWeightsForModel:andProcedure:fromOffset:withSize:error:].cold.4
+ -[_ANEVirtualClient doSyncMutableWeightsForModel:andProcedure:fromOffset:withSize:error:].cold.5
+ -[_ANEVirtualClient doSyncMutableWeightsForModel:andProcedure:fromOffset:withSize:error:].cold.6
+ -[_ANEVirtualClient doSyncMutableWeightsForModel:andProcedure:fromOffset:withSize:error:].cold.7
+ -[_ANEVirtualClient doSyncMutableWeightsForModel:andProcedure:fromOffset:withSize:error:].cold.8
+ -[_ANEVirtualClient doUnmapMutableWeightsForModel:andProcedure:]
+ -[_ANEVirtualClient doUnmapMutableWeightsForModel:andProcedure:].cold.1
+ -[_ANEVirtualClient doUnmapMutableWeightsForModel:andProcedure:].cold.2
+ -[_ANEVirtualClient doUnmapMutableWeightsForModel:andProcedure:].cold.3
+ -[_ANEVirtualClient doUnmapMutableWeightsForModel:andProcedure:].cold.4
+ -[_ANEVirtualClient doUnmapMutableWeightsForModel:andProcedure:].cold.5
+ -[_ANEVirtualClient doUnmapMutableWeightsForModel:andProcedure:].cold.6
+ -[_ANEVirtualClient loadModel:options:qos:error:].cold.13
+ -[_ANEVirtualClient loadModelLegacy:options:qos:error:]
+ -[_ANEVirtualClient loadModelLegacy:options:qos:error:].cold.1
+ -[_ANEVirtualClient loadModelLegacy:options:qos:error:].cold.10
+ -[_ANEVirtualClient loadModelLegacy:options:qos:error:].cold.11
+ -[_ANEVirtualClient loadModelLegacy:options:qos:error:].cold.2
+ -[_ANEVirtualClient loadModelLegacy:options:qos:error:].cold.3
+ -[_ANEVirtualClient loadModelLegacy:options:qos:error:].cold.4
+ -[_ANEVirtualClient loadModelLegacy:options:qos:error:].cold.5
+ -[_ANEVirtualClient loadModelLegacy:options:qos:error:].cold.6
+ -[_ANEVirtualClient loadModelLegacy:options:qos:error:].cold.7
+ -[_ANEVirtualClient loadModelLegacy:options:qos:error:].cold.8
+ -[_ANEVirtualClient loadModelLegacy:options:qos:error:].cold.9
+ -[_ANEVirtualClient loadModelNewInstance:options:modelInstParams:qos:error:].cold.19
+ -[_ANEVirtualClient mapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:]
+ -[_ANEVirtualClient mapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.1
+ -[_ANEVirtualClient mapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.2
+ -[_ANEVirtualClient mapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.3
+ -[_ANEVirtualClient mapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:].cold.4
+ -[_ANEVirtualClient purgeCompiledModel:].cold.5
+ -[_ANEVirtualClient purgeCompiledModel:].cold.6
+ -[_ANEVirtualClient purgeCompiledModel:].cold.7
+ -[_ANEVirtualClient purgeCompiledModel:].cold.8
+ -[_ANEVirtualClient purgeCompiledModel:].cold.9
+ -[_ANEVirtualClient purgeCompiledModelLegacy:]
+ -[_ANEVirtualClient purgeCompiledModelLegacy:].cold.1
+ -[_ANEVirtualClient purgeCompiledModelLegacy:].cold.2
+ -[_ANEVirtualClient purgeCompiledModelLegacy:].cold.3
+ -[_ANEVirtualClient purgeCompiledModelLegacy:].cold.4
+ -[_ANEVirtualClient syncMutableWeightsForModel:andProcedure:fromOffset:withSize:error:]
+ -[_ANEVirtualClient syncMutableWeightsForModel:andProcedure:fromOffset:withSize:error:].cold.1
+ -[_ANEVirtualClient syncMutableWeightsForModel:andProcedure:fromOffset:withSize:error:].cold.2
+ -[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:]
+ -[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:].cold.1
+ -[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:].cold.10
+ -[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:].cold.2
+ -[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:].cold.3
+ -[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:].cold.4
+ -[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:].cold.5
+ -[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:].cold.6
+ -[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:].cold.7
+ -[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:].cold.8
+ -[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:].cold.9
+ -[_ANEVirtualClient transferDirectoryMetaDataToHost:withUUID:]
+ -[_ANEVirtualClient transferDirectoryMetaDataToHost:withUUID:].cold.1
+ -[_ANEVirtualClient transferDirectoryMetaDataToHost:withUUID:].cold.2
+ -[_ANEVirtualClient transferDirectoryMetaDataToHost:withUUID:].cold.3
+ -[_ANEVirtualClient transferDirectoryMetaDataToHost:withUUID:].cold.4
+ -[_ANEVirtualClient transferDirectoryMetaDataToHost:withUUID:].cold.5
+ -[_ANEVirtualClient transferDirectoryMetaDataToHost:withUUID:].cold.6
+ -[_ANEVirtualClient transferDirectoryMetaDataToHost:withUUID:].cold.7
+ -[_ANEVirtualClient transferDirectoryMetaDataToHost:withUUID:].cold.8
+ -[_ANEVirtualClient transferDirectoryMetaDataToHost:withUUID:].cold.9
+ -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:overWriteFileNameWith:]
+ -[_ANEVirtualClient transferFileToHostWithPath:withUUID:withModelInputPath:overWriteFileNameWith:chunkSizeBytes:withExistingIOSurface:]
+ -[_ANEVirtualClient transferFileToHostWithPath:withUUID:withModelInputPath:overWriteFileNameWith:chunkSizeBytes:withExistingIOSurface:].cold.1
+ -[_ANEVirtualClient transferFileToHostWithPath:withUUID:withModelInputPath:overWriteFileNameWith:chunkSizeBytes:withExistingIOSurface:].cold.10
+ -[_ANEVirtualClient transferFileToHostWithPath:withUUID:withModelInputPath:overWriteFileNameWith:chunkSizeBytes:withExistingIOSurface:].cold.11
+ -[_ANEVirtualClient transferFileToHostWithPath:withUUID:withModelInputPath:overWriteFileNameWith:chunkSizeBytes:withExistingIOSurface:].cold.12
+ -[_ANEVirtualClient transferFileToHostWithPath:withUUID:withModelInputPath:overWriteFileNameWith:chunkSizeBytes:withExistingIOSurface:].cold.2
+ -[_ANEVirtualClient transferFileToHostWithPath:withUUID:withModelInputPath:overWriteFileNameWith:chunkSizeBytes:withExistingIOSurface:].cold.3
+ -[_ANEVirtualClient transferFileToHostWithPath:withUUID:withModelInputPath:overWriteFileNameWith:chunkSizeBytes:withExistingIOSurface:].cold.4
+ -[_ANEVirtualClient transferFileToHostWithPath:withUUID:withModelInputPath:overWriteFileNameWith:chunkSizeBytes:withExistingIOSurface:].cold.5
+ -[_ANEVirtualClient transferFileToHostWithPath:withUUID:withModelInputPath:overWriteFileNameWith:chunkSizeBytes:withExistingIOSurface:].cold.6
+ -[_ANEVirtualClient transferFileToHostWithPath:withUUID:withModelInputPath:overWriteFileNameWith:chunkSizeBytes:withExistingIOSurface:].cold.7
+ -[_ANEVirtualClient transferFileToHostWithPath:withUUID:withModelInputPath:overWriteFileNameWith:chunkSizeBytes:withExistingIOSurface:].cold.8
+ -[_ANEVirtualClient transferFileToHostWithPath:withUUID:withModelInputPath:overWriteFileNameWith:chunkSizeBytes:withExistingIOSurface:].cold.9
+ -[_ANEVirtualClient transferFileToHostWithPath:withUUID:withModelInputPath:overWriteFileNameWith:withExistingIOSurface:]
+ -[_ANEVirtualClient unmapMutableWeightsForModel:andProcedure:]
+ -[_ANEVirtualClient unmapMutableWeightsForModel:andProcedure:].cold.1
+ -[_ANEVirtualClient unmapMutableWeightsForModel:andProcedure:].cold.2
+ -[_ANEWeight initWithWeightSymbol:]
+ GCC_except_table106
+ GCC_except_table109
+ GCC_except_table110
+ GCC_except_table115
+ GCC_except_table122
+ GCC_except_table127
+ GCC_except_table128
+ GCC_except_table129
+ GCC_except_table130
+ GCC_except_table132
+ GCC_except_table135
+ GCC_except_table136
+ GCC_except_table137
+ GCC_except_table139
+ GCC_except_table145
+ GCC_except_table146
+ GCC_except_table147
+ GCC_except_table148
+ GCC_except_table149
+ GCC_except_table150
+ GCC_except_table151
+ GCC_except_table152
+ GCC_except_table153
+ GCC_except_table154
+ GCC_except_table155
+ GCC_except_table156
+ GCC_except_table158
+ GCC_except_table159
+ GCC_except_table164
+ GCC_except_table171
+ GCC_except_table175
+ GCC_except_table176
+ GCC_except_table177
+ GCC_except_table185
+ GCC_except_table26
+ GCC_except_table43
+ GCC_except_table47
+ GCC_except_table48
+ GCC_except_table53
+ GCC_except_table56
+ GCC_except_table59
+ GCC_except_table62
+ GCC_except_table64
+ GCC_except_table65
+ _ANECreateValidationResultForMILNetworkOnHost
+ _ANECreateValidationResultForMILNetworkOnHost.cold.1
+ _ANECreateValidationResultForMLIRNetworkOnHost
+ _ANECreateValidationResultForNetworkCreateGenerateFailedGlobalIdentifier
+ _ANEValidateNetworkCreate.cold.7
+ _ANEWeightSymbolIdentifyingIFP
+ _APP_SANDBOX_READ_WRITE
+ _CC_SHA1_Final
+ _CC_SHA1_Init
+ _CC_SHA1_Update
+ _CFArrayRemoveAllValues
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFDictionaryRemoveValue
+ _IOSurfaceFlushProcessorCaches
+ _IOSurfaceGetHeight
+ _IOSurfaceGetWidth
+ _NSURLFileSizeKey
+ _NSURLIsDirectoryKey
+ _NSURLIsRegularFileKey
+ _NSURLIsSymbolicLinkKey
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_CLASS_$__ANEDebugUtils
+ _OBJC_CLASS_$__ANEIntermediateTensor
+ _OBJC_CLASS_$__ANEProgramProcedurePriv
+ _OBJC_CLASS_$__ANETensorDebugHelper
+ _OBJC_IVAR_$__ANEIntermediateTensor._tensorIndex
+ _OBJC_IVAR_$__ANEIntermediateTensor._tensorName
+ _OBJC_IVAR_$__ANEModel._externConstants
+ _OBJC_IVAR_$__ANEModel._numInputs
+ _OBJC_IVAR_$__ANEModel._numOutputs
+ _OBJC_IVAR_$__ANEModel._procedures
+ _OBJC_IVAR_$__ANEProcedureData._mutableWeightsBufferID
+ _OBJC_IVAR_$__ANEProcedureData._mutableWeightsBufferSize
+ _OBJC_IVAR_$__ANEProgramForEvaluation._mutableWeightsMap
+ _OBJC_IVAR_$__ANEProgramForEvaluation._mutableWeightsMapLock
+ _OBJC_IVAR_$__ANEProgramProcedurePriv._mutableWeightsBuffer
+ _OBJC_IVAR_$__ANEProgramProcedurePriv._symbolName
+ _OBJC_IVAR_$__ANEVirtualClient._mutableWeightsBufferMap
+ _OBJC_METACLASS_$__ANEDebugUtils
+ _OBJC_METACLASS_$__ANEIntermediateTensor
+ _OBJC_METACLASS_$__ANEProgramProcedurePriv
+ _OBJC_METACLASS_$__ANETensorDebugHelper
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
+ __OBJC_$_CLASS_METHODS__ANEDebugUtils
+ __OBJC_$_CLASS_METHODS__ANEIntermediateTensor
+ __OBJC_$_CLASS_METHODS__ANETensorDebugHelper
+ __OBJC_$_CLASS_PROP_LIST__ANEIntermediateTensor
+ __OBJC_$_INSTANCE_METHODS__ANEIntermediateTensor
+ __OBJC_$_INSTANCE_METHODS__ANEProgramProcedurePriv
+ __OBJC_$_INSTANCE_VARIABLES__ANEIntermediateTensor
+ __OBJC_$_INSTANCE_VARIABLES__ANEProgramProcedurePriv
+ __OBJC_$_PROP_LIST__ANEIntermediateTensor
+ __OBJC_$_PROP_LIST__ANEProgramProcedurePriv
+ __OBJC_CLASS_PROTOCOLS_$__ANEIntermediateTensor
+ __OBJC_CLASS_RO_$__ANEDebugUtils
+ __OBJC_CLASS_RO_$__ANEIntermediateTensor
+ __OBJC_CLASS_RO_$__ANEProgramProcedurePriv
+ __OBJC_CLASS_RO_$__ANETensorDebugHelper
+ __OBJC_METACLASS_RO_$__ANEDebugUtils
+ __OBJC_METACLASS_RO_$__ANEIntermediateTensor
+ __OBJC_METACLASS_RO_$__ANEProgramProcedurePriv
+ __OBJC_METACLASS_RO_$__ANETensorDebugHelper
+ __ZL15fDeviceCallbackPvP15ANEDeviceStructP24ANEProgramInstanceStruct22ANENotificationMessage
+ __ZL15fDeviceCallbackPvP15ANEDeviceStructP24ANEProgramInstanceStruct22ANENotificationMessage.cold.1
+ __ZL15fDeviceCallbackPvP15ANEDeviceStructP24ANEProgramInstanceStruct22ANENotificationMessage.cold.2
+ __ZL22getANEDevicePropertiesPK10__CFString
+ __ZN25MutableWeightsBufferEntryaSERKS_
+ __ZNKSt9type_infoeqB9fqe220100ERKS_
+ __ZNSt12length_errorC1B9fqe220100EPKc
+ __ZNSt20bad_array_new_lengthC1Ev
+ __ZNSt20bad_array_new_lengthD1Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIy25MutableWeightsBufferEntryEEPvEENS_22__hash_node_destructorINS_9allocatorIS6_EEEEED1B9fqe220100Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy19MutableWeightsEntryEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy19MutableWeightsEntryEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE4findIyEENS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy19MutableWeightsEntryEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS3_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy19MutableWeightsEntryEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS3_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy19MutableWeightsEntryEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy19MutableWeightsEntryEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEEC2EOSH_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy19MutableWeightsEntryEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy25MutableWeightsBufferEntryEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy25MutableWeightsBufferEntryEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE22__deallocate_node_listB9fqe220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS3_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy25MutableWeightsBufferEntryEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE4findIyEENS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy25MutableWeightsBufferEntryEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy25MutableWeightsBufferEntryEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS3_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy25MutableWeightsBufferEntryEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS3_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy25MutableWeightsBufferEntryEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy25MutableWeightsBufferEntryEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEED2Ev
+ __ZNSt3__112__next_primeEm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE22__init_internal_bufferB9fqe220100Em
+ __ZNSt3__119__shared_weak_count16__release_sharedB9fqe220100Ev
+ __ZNSt3__119piecewise_constructE
+ __ZNSt3__120__throw_length_errorB9fqe220100EPKc
+ __ZSt28__throw_bad_array_new_lengthB9fqe220100v
+ __ZTISt20bad_array_new_length
+ __ZZ45+[_ANEVirtualClient getPatternsForModelType:]E17modelTypePatterns
+ __ZZ45+[_ANEVirtualClient getPatternsForModelType:]E9onceToken
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIy19MutableWeightsEntryEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE16__emplace_uniqueB9fqe220100IJRKNS_21piecewise_construct_tENS_5tupleIJRS6_EEENSM_IJEEEEEENS5_INS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEEDpOT_ENKUlSN_SL_OSO_OSP_E_clESN_SL_S10_S11_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIy25MutableWeightsBufferEntryEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE16__emplace_uniqueB9fqe220100IJRKNS_21piecewise_construct_tENS_5tupleIJRS6_EEENSM_IJEEEEEENS5_INS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEEDpOT_ENKUlSN_SL_OSO_OSP_E_clESN_SL_S10_S11_
+ __ZdaPvSt19__type_descriptor_t
+ ___100-[_ANEProgramForEvaluation processRequest:model:qos:qIndex:modelStringID:options:returnValue:error:]_block_invoke.cold.2
+ ___135-[_ANEVirtualClient transferFileToHostWithPath:withUUID:withModelInputPath:overWriteFileNameWith:chunkSizeBytes:withExistingIOSurface:]_block_invoke
+ ___40-[_ANEVirtualClient purgeCompiledModel:]_block_invoke
+ ___41+[_ANEDebugUtils applyDebugEnvToOptions:]_block_invoke
+ ___44-[_ANEVirtualClient compiledModelExistsFor:]_block_invoke
+ ___45+[_ANEVirtualClient getPatternsForModelType:]_block_invoke
+ ___49-[_ANEVirtualClient loadModel:options:qos:error:]_block_invoke
+ ___52-[_ANEVirtualClient compileModel:options:qos:error:]_block_invoke
+ ___61-[_ANEClient updateSourcePathForModelTrackedByHash:to:error:]_block_invoke
+ ___61-[_ANEClient updateSourcePathForModelTrackedByHash:to:error:]_block_invoke.cold.1
+ ___61-[_ANEClient updateSourcePathForModelTrackedByHash:to:error:]_block_invoke_2
+ ___61-[_ANEClient updateSourcePathForModelTrackedByHash:to:error:]_block_invoke_2.cold.1
+ ___61-[_ANEClient updateSourcePathForModelTrackedByHash:to:error:]_block_invoke_2.cold.2
+ ___62-[_ANEClient updatePurgeabilityLevelForModelTrackedByHash:to:]_block_invoke
+ ___62-[_ANEClient updatePurgeabilityLevelForModelTrackedByHash:to:]_block_invoke.25
+ ___62-[_ANEClient updatePurgeabilityLevelForModelTrackedByHash:to:]_block_invoke.25.cold.1
+ ___62-[_ANEClient updatePurgeabilityLevelForModelTrackedByHash:to:]_block_invoke.25.cold.2
+ ___62-[_ANEVirtualClient transferDirectoryMetaDataToHost:withUUID:]_block_invoke
+ ___62-[_ANEVirtualClient unmapMutableWeightsForModel:andProcedure:]_block_invoke
+ ___65-[_ANEDaemonConnection purgeCompiledModelMatchingHash:withReply:]_block_invoke.24
+ ___65-[_ANEDaemonConnection purgeCompiledModelMatchingHash:withReply:]_block_invoke.24.cold.1
+ ___65-[_ANEVirtualClient evaluateWithModel:options:request:qos:error:]_block_invoke.115
+ ___65-[_ANEVirtualClient evaluateWithModel:options:request:qos:error:]_block_invoke.115.cold.1
+ ___65-[_ANEVirtualClient evaluateWithModel:options:request:qos:error:]_block_invoke.123
+ ___65-[_ANEVirtualClient evaluateWithModel:options:request:qos:error:]_block_invoke.cold.3
+ ___65-[_ANEVirtualClient evaluateWithModel:options:request:qos:error:]_block_invoke.cold.4
+ ___66-[_ANEDaemonConnection compiledModelExistsMatchingHash:withReply:]_block_invoke.23
+ ___66-[_ANEDaemonConnection compiledModelExistsMatchingHash:withReply:]_block_invoke.23.cold.1
+ ___67-[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:]_block_invoke
+ ___67-[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:]_block_invoke.55
+ ___67-[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:]_block_invoke.57
+ ___67-[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:]_block_invoke.57.cold.1
+ ___67-[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:]_block_invoke.57.cold.2
+ ___67-[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:]_block_invoke.57.cold.3
+ ___67-[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:]_block_invoke.57.cold.4
+ ___67-[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:]_block_invoke.57.cold.5
+ ___67-[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:]_block_invoke_2
+ ___67-[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:]_block_invoke_2.cold.1
+ ___71-[_ANEClient doLoadModelNewInstance:options:modelInstParams:qos:error:]_block_invoke.32
+ ___71-[_ANEClient doLoadModelNewInstance:options:modelInstParams:qos:error:]_block_invoke.32.cold.1
+ ___71-[_ANEClient doLoadModelNewInstance:options:modelInstParams:qos:error:]_block_invoke.32.cold.2
+ ___71-[_ANEClient doLoadModelNewInstance:options:modelInstParams:qos:error:]_block_invoke.32.cold.3
+ ___71-[_ANEClient doLoadModelNewInstance:options:modelInstParams:qos:error:]_block_invoke.32.cold.4
+ ___75-[_ANEDaemonConnection updateSourcePathForModelTrackedByHash:to:withReply:]_block_invoke
+ ___75-[_ANEDaemonConnection updateSourcePathForModelTrackedByHash:to:withReply:]_block_invoke.22
+ ___75-[_ANEDaemonConnection updateSourcePathForModelTrackedByHash:to:withReply:]_block_invoke.cold.1
+ ___82-[_ANEDaemonConnection updatePurgeabilityLevelForModelTrackedByHash:to:withReply:]_block_invoke
+ ___82-[_ANEDaemonConnection updatePurgeabilityLevelForModelTrackedByHash:to:withReply:]_block_invoke.21
+ ___82-[_ANEDaemonConnection updatePurgeabilityLevelForModelTrackedByHash:to:withReply:]_block_invoke.cold.1
+ ___82-[_ANEVirtualClient createValidationResultForNetworkCreateMLIR:validation_params:]_block_invoke
+ ___87-[_ANEVirtualClient syncMutableWeightsForModel:andProcedure:fromOffset:withSize:error:]_block_invoke
+ ___91-[_ANEVirtualClient mapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:]_block_invoke
+ ___Block_byref_object_copy_.124
+ ___Block_byref_object_copy_.147
+ ___Block_byref_object_copy_.150
+ ___Block_byref_object_copy_.159
+ ___Block_byref_object_copy_.168
+ ___Block_byref_object_copy_.45
+ ___Block_byref_object_copy_.50
+ ___Block_byref_object_copy_.59
+ ___Block_byref_object_copy_.78
+ ___Block_byref_object_dispose_.125
+ ___Block_byref_object_dispose_.148
+ ___Block_byref_object_dispose_.151
+ ___Block_byref_object_dispose_.160
+ ___Block_byref_object_dispose_.169
+ ___Block_byref_object_dispose_.46
+ ___Block_byref_object_dispose_.51
+ ___Block_byref_object_dispose_.60
+ ___Block_byref_object_dispose_.79
+ ___block_descriptor_148_ea8_32s40s48s56bs64r72r80r88r96r104r112r_e65_v280?0{ANENotificationMessage=ii^v[4^v][4I][4[4^v]][4[4I]]QBCC}8lr64l8r72l8s32l8s40l8r80l8r88l8r96l8s48l8s56l8r104l8r112l8
+ ___block_descriptor_40_e8_32bs_e65_v64?0B8"NSDictionary"12Q20Q28c36I40I44"NSString"48"NSError"56ls32l8
+ ___block_descriptor_48_ea8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_ea8_32s_e28_"NSString"16?0"NSString"8ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s48bs_e33_v24?0"IOSurfaceSharedEvent"8Q16ls48l8s32l8s40l8
+ ___block_descriptor_64_ea8_32s40s48s56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40r48r_e20_v20?0B8"NSError"12lr40l8s32l8r48l8
+ ___block_descriptor_72_ea8_32s40s48bs56bs_e18_B16?0"NSString"8ls48l8s56l8s32l8s40l8
+ ___block_descriptor_72_ea8_32s40s48bs56r_e18_B16?0"NSString"8ls48l8s32l8s40l8r56l8
+ ___block_descriptor_76_e8_32s40r48r_e65_v64?0B8"NSDictionary"12Q20Q28c36I40I44"NSString"48"NSError"56ls32l8r40l8r48l8
+ ___block_descriptor_80_e8_32s40s48r56r_e20_v20?0B8"NSError"12lr48l8s32l8s40l8r56l8
+ ___block_descriptor_84_e8_32s40s48r56r_e65_v64?0B8"NSDictionary"12Q20Q28c36I40I44"NSString"48"NSError"56ls32l8r48l8s40l8r56l8
+ ___block_descriptor_88_e8_32s40s48r56r_e5_v8?0ls32l8s40l8r48l8r56l8
+ ___block_descriptor_88_ea8_32s40s48s56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_96_e8_32s40s48s56r64r_e5_v8?0lr56l8s32l8s40l8s48l8r64l8
+ ___block_literal_global.234
+ ___block_literal_global.239
+ ___block_literal_global.250
+ ___block_literal_global.264
+ ___block_literal_global.269
+ ___block_literal_global.27
+ ___block_literal_global.8
+ _applyDebugEnvToOptions:.knownBoolKeys
+ _applyDebugEnvToOptions:.onceToken
+ _csops_audittoken
+ _getenv
+ _kANEFAneInstanceHint
+ _kANEFDebugCaptureBytecodeKey
+ _kANEFDebugCaptureElideResourcesKey
+ _kANEFDebugCaptureFolderKey
+ _kANEFDebugCaptureFolderSandboxExtensionKey
+ _kANEFDebugCaptureIncludeLocationsKey
+ _kANEFDebugOptionsKey
+ _kANEFIntermediateBufferSizeHint
+ _kANEFIntermediateTensorDescriptorKey
+ _kANEFModelMutableWeightBufferInfoKey
+ _kANEFProcedureVariantHint
+ _kANEFTargetArchitectureKey
+ _kANEPerfStatsAuxDataKey
+ _kANEPerfStatsCounterAFToKMData
+ _kANEPerfStatsCounterAFToL2Data
+ _kANEPerfStatsCounterDMAReadBytes
+ _kANEPerfStatsCounterDMAReadWriteBytes
+ _kANEPerfStatsCounterDPEEnergy
+ _kANEPerfStatsCounterFp16Cycles
+ _kANEPerfStatsCounterInt8Cycles
+ _kANEPerfStatsCounterKMStallCycles
+ _kANEPerfStatsCounterL2NominalCycles
+ _kANEPerfStatsCounterL2PEComputeCycles
+ _kANEPerfStatsCounterL2PEInputStallCycles
+ _kANEPerfStatsCounterL2PEOutputStallCycles
+ _kANEPerfStatsCounterL2ReadStallCycles
+ _kANEPerfStatsCounterL2ThrottleCycles
+ _kANEPerfStatsCounterL2ToAFData
+ _kANEPerfStatsCounterL2ToNEData
+ _kANEPerfStatsCounterL2WriteStallCycles
+ _kANEPerfStatsCounterNEComputeCycles
+ _kANEPerfStatsCounterNEInputStallCycles
+ _kANEPerfStatsCounterNEKernelStallCycles
+ _kANEPerfStatsCounterNENominalCycles
+ _kANEPerfStatsCounterNEOutputStallCycles
+ _kANEPerfStatsCounterNEThrottleCycles
+ _kANEPerfStatsCounterNEToL2Data
+ _kANEPerfStatsCounterUnknown
+ _kANEPerfStatsDescriptorsKey
+ _kANEPerfStatsEventTypeBaseAddressError
+ _kANEPerfStatsEventTypeChangeDestination
+ _kANEPerfStatsEventTypeChangeSource
+ _kANEPerfStatsEventTypeCommit
+ _kANEPerfStatsEventTypeContextSwitchOut
+ _kANEPerfStatsEventTypeDMAAXIError
+ _kANEPerfStatsEventTypeDelay
+ _kANEPerfStatsEventTypeFWEnqueueTM
+ _kANEPerfStatsEventTypeFetchDone
+ _kANEPerfStatsEventTypeFinishExecution
+ _kANEPerfStatsEventTypeFinishExecutionNEDMA
+ _kANEPerfStatsEventTypeKey
+ _kANEPerfStatsEventTypeMacInf
+ _kANEPerfStatsEventTypeMacNan
+ _kANEPerfStatsEventTypeNeNonLinearLut
+ _kANEPerfStatsEventTypeNeSrcInf
+ _kANEPerfStatsEventTypeNeSrcNan
+ _kANEPerfStatsEventTypeNoHighestPriority
+ _kANEPerfStatsEventTypeOutputToL2
+ _kANEPerfStatsEventTypePeGlobalReductInf
+ _kANEPerfStatsEventTypePeGlobalReductNan
+ _kANEPerfStatsEventTypePeOutputNan
+ _kANEPerfStatsEventTypePeSrc1Inf
+ _kANEPerfStatsEventTypePeSrc1Nan
+ _kANEPerfStatsEventTypePeSrc2Inf
+ _kANEPerfStatsEventTypePeSrc2Nan
+ _kANEPerfStatsEventTypePerfTracingCounter
+ _kANEPerfStatsEventTypePpInf
+ _kANEPerfStatsEventTypePrefetch
+ _kANEPerfStatsEventTypePrefetchFinish
+ _kANEPerfStatsEventTypePrefetchTerminate
+ _kANEPerfStatsEventTypeStartExecution
+ _kANEPerfStatsEventTypeTaskSwitch
+ _kANEPerfStatsEventTypeUnknown
+ _kANEPerfStatsEventTypeValueKey
+ _kANEPerfStatsEventTypeWinoInpTransInf
+ _kANEPerfStatsEventTypeWinoKernTransInf
+ _kANEPerfStatsEventsKey
+ _kANEPerfStatsExecutionTimeKey
+ _kANEPerfStatsFinishTimeKey
+ _kANEPerfStatsHWExecutionTimeKey
+ _kANEPerfStatsMetadataKey
+ _kANEPerfStatsNumDescriptorsKey
+ _kANEPerfStatsNumTDsKey
+ _kANEPerfStatsPerTdPerfCountersConfigKey
+ _kANEPerfStatsPerTdPerfCountersKey
+ _kANEPerfStatsPerformanceCountersKey
+ _kANEPerfStatsPriorityKey
+ _kANEPerfStatsProcedureIdKey
+ _kANEPerfStatsProcessIdKey
+ _kANEPerfStatsProgramIdKey
+ _kANEPerfStatsRawStatsKey
+ _kANEPerfStatsStartTimeKey
+ _kANEPerfStatsTdExecutionTimesKey
+ _kANEPerfStatsTidKey
+ _kANEPerfStatsTimeStampKey
+ _kANEPerfStatsTotalEventsReceivedKey
+ _kANEPerfStatsTotalEventsRecordedKey
+ _kANEPerfStatsTotalExecutionTimeKey
+ _kANEPerfStatsUuidKey
+ _kANEPerfStatsValueMSKey
+ _kANEPerfStatsValueNSKey
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$applyDebugEnvToOptions:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$assetExistsOnHost:
+ _objc_msgSend$charValue
+ _objc_msgSend$compileModelLegacy:options:qos:error:
+ _objc_msgSend$compiledModelExistsForLegacy:
+ _objc_msgSend$copyModelAttributesToDictionary:dictionary:vmData:
+ _objc_msgSend$copyModelMetaData:options:dictionary:vmData:shouldEncodeKey:
+ _objc_msgSend$createCFDictionaryFromIOSurface:dataLength:
+ _objc_msgSend$createIOSurfaceWithData:length:ioSID:
+ _objc_msgSend$createValidationResultForNetworkCreateMLIR:validation_params:
+ _objc_msgSend$currentDirectoryPath
+ _objc_msgSend$decodeDescriptor:perTdPerfCounters:
+ _objc_msgSend$decodeInt64ForKey:
+ _objc_msgSend$decodeRawStatsData:
+ _objc_msgSend$descriptorWithName:index:
+ _objc_msgSend$deserializeHostErrorFromData:
+ _objc_msgSend$doMapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:
+ _objc_msgSend$doSyncMutableWeightsForModel:andProcedure:fromOffset:withSize:error:
+ _objc_msgSend$doUnmapMutableWeightsForModel:andProcedure:
+ _objc_msgSend$doesPath:matchPattern:withFullPath:
+ _objc_msgSend$encodeInt64:forKey:
+ _objc_msgSend$enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:
+ _objc_msgSend$externConstants
+ _objc_msgSend$extractMpsConstantsIOSurfaceIDs:ioSIDArray:keysArray:
+ _objc_msgSend$findMatchingAssetPaths:inDirectory:
+ _objc_msgSend$findPathsMatchingPattern:inDirectory:
+ _objc_msgSend$getPatternsForModelType:
+ _objc_msgSend$getUUIDBytes:
+ _objc_msgSend$initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:mpsConstants:externConstants:programHandle:intermediateBufferHandle:queueDepth:perfStatsMask:state:
+ _objc_msgSend$initWithName:index:
+ _objc_msgSend$initWithSymbolName:
+ _objc_msgSend$initWithUUIDBytes:
+ _objc_msgSend$initWithUUIDString:
+ _objc_msgSend$initWithWeightSymbol:
+ _objc_msgSend$isAbsolutePath
+ _objc_msgSend$isReadableFileAtPath:
+ _objc_msgSend$loadModelLegacy:options:qos:error:
+ _objc_msgSend$mapMutableWeightsBufferDirectForProcedure:bufferID:buffer:size:error:
+ _objc_msgSend$mapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:
+ _objc_msgSend$mappingMutableWeightsBufferFailed:
+ _objc_msgSend$mutableWeightsBufferID
+ _objc_msgSend$mutableWeightsBufferPtr
+ _objc_msgSend$mutableWeightsBufferSize
+ _objc_msgSend$mutableWeightsMappingAccessEntitlement
+ _objc_msgSend$numInputs
+ _objc_msgSend$numOutputs
+ _objc_msgSend$numberWithChar:
+ _objc_msgSend$numberWithUnsignedShort:
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$objectWithIOSurface:
+ _objc_msgSend$pStatsRawData
+ _objc_msgSend$parseDebugEnvVar
+ _objc_msgSend$parseDebugString:
+ _objc_msgSend$pathExtension
+ _objc_msgSend$populateCSIdentity:maxLength:
+ _objc_msgSend$populateNSString:toBuffer:maxLength:
+ _objc_msgSend$populateUUID:maxLength:fromString:
+ _objc_msgSend$procedures
+ _objc_msgSend$proceduresCount
+ _objc_msgSend$purgeCompiledModelLegacy:
+ _objc_msgSend$queryTensorsFromDebugFile:error:
+ _objc_msgSend$rangeOfFirstMatchInString:options:range:
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$setMutableWeightsBuffer:
+ _objc_msgSend$setMutableWeightsBufferID:
+ _objc_msgSend$setMutableWeightsBufferSize:
+ _objc_msgSend$setNumInputs:
+ _objc_msgSend$setNumOutputs:
+ _objc_msgSend$setProcedures:
+ _objc_msgSend$stringByAppendingPathExtension:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringByDeletingPathExtension
+ _objc_msgSend$stringByResolvingSymlinksInPath
+ _objc_msgSend$stringByTrimmingCharactersInSet:
+ _objc_msgSend$stringForEventType:
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$symbolName
+ _objc_msgSend$syncMutableWeightsForModel:andProcedure:fromOffset:withSize:error:
+ _objc_msgSend$teamScopedCodeSigningIDFor:processIdentifier:
+ _objc_msgSend$tensorIndex
+ _objc_msgSend$tensorName
+ _objc_msgSend$transferAssetsToHostAtPath:withUUID:modelType:
+ _objc_msgSend$transferDirectoryMetaDataToHost:withUUID:
+ _objc_msgSend$transferFileToHostWithPath:withUUID:withModelInputPath:overWriteFileNameWith:chunkSizeBytes:withExistingIOSurface:
+ _objc_msgSend$transferFileToHostWithPath:withUUID:withModelInputPath:overWriteFileNameWith:withExistingIOSurface:
+ _objc_msgSend$trimmedModelPath:trimmedPathOut:
+ _objc_msgSend$unmapMutableWeightsBufferDirectForProcedure:bufferID:
+ _objc_msgSend$unmapMutableWeightsForModel:andProcedure:
+ _objc_msgSend$updateFromModel:shouldUpdateModelURL:shouldUpdateUUID:
+ _objc_msgSend$updateModelAttributes:state:programHandle:intermediateBufferHandle:queueDepth:numInputs:numOutputs:
+ _objc_msgSend$updatePurgeabilityLevelForModelTrackedByHash:to:withReply:
+ _objc_msgSend$updateSourcePathForModelTrackedByHash:to:withReply:
+ _objc_msgSend$uuidV5FromString:
+ _objc_msgSend$uuidV5FromURL:
+ _objc_msgSend$validateDebugInfoFile:error:
+ _objc_msgSend$whitespaceCharacterSet
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x7
+ _putchar
+ _puts
- +[_ANEIOSurfaceObject objectWithIOSurfaceNoRetain:startOffset:]
- +[_ANEStrings trimmedModelPath:trimmedPath:]
- +[_ANEVirtualClient freeModelFileIOSurfaces:]
- +[_ANEVirtualClient getCFDictionaryFromIOSurface:dataLength:]
- +[_ANEVirtualClient getCFDictionaryFromIOSurface:dataLength:].cold.1
- +[_ANEVirtualClient getCFDictionaryFromIOSurface:dataLength:].cold.2
- +[_ANEVirtualClient getCFDictionaryFromIOSurface:dataLength:].cold.3
- +[_ANEVirtualClient getCFDictionaryFromIOSurface:dataLength:].cold.4
- +[_ANEVirtualClient getCFDictionaryFromIOSurface:dataLength:].cold.5
- -[_ANEModel encodeWithCoder:].cold.1
- -[_ANEModel initWithCoder:].cold.1
- -[_ANEModel initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:mpsConstants:]
- -[_ANEModel initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:mpsConstants:].cold.1
- -[_ANEModel initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:mpsConstants:].cold.2
- -[_ANEModel initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:mpsConstants:].cold.3
- -[_ANEModel initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:mpsConstants:].cold.4
- -[_ANEModel updateModelAttributes:state:programHandle:intermediateBufferHandle:queueDepth:]
- -[_ANEVirtualClient copyModelMetaData:options:dictionary:vmData:].cold.1
- -[_ANEVirtualClient copyModelMetaData:options:dictionary:vmData:].cold.2
- -[_ANEVirtualClient copyModelMetaData:options:dictionary:vmData:].cold.3
- -[_ANEVirtualClient copyToIOSurface:length:ioSID:]
- -[_ANEVirtualClient copyToIOSurface:length:ioSID:].cold.1
- -[_ANEVirtualClient copyToIOSurface:length:ioSID:].cold.2
- -[_ANEVirtualClient copyToIOSurface:length:ioSID:].cold.3
- -[_ANEVirtualClient copyToIOSurface:size:ioSID:]
- -[_ANEVirtualClient copyToIOSurface:size:ioSID:].cold.1
- -[_ANEVirtualClient copyToIOSurface:size:ioSID:].cold.2
- -[_ANEVirtualClient copyToIOSurface:size:ioSID:].cold.3
- -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.1
- -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.10
- -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.11
- -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.12
- -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.13
- -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.14
- -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.15
- -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.2
- -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.3
- -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.4
- -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.5
- -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.6
- -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.7
- -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.8
- -[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:].cold.9
- -[_ANEVirtualClient validateNetworkCreateMLIR:validation_params:]
- -[_ANEVirtualClient validateNetworkCreateMLIR:validation_params:].cold.1
- -[_ANEVirtualClient validateNetworkCreateMLIR:validation_params:].cold.2
- -[_ANEVirtualClient validateNetworkCreateMLIR:validation_params:].cold.3
- -[_ANEVirtualClient validateNetworkCreateMLIR:validation_params:].cold.4
- -[_ANEVirtualClient validateNetworkCreateMLIR:validation_params:].cold.5
- GCC_except_table102
- GCC_except_table103
- GCC_except_table104
- GCC_except_table105
- GCC_except_table108
- GCC_except_table112
- GCC_except_table144
- GCC_except_table20
- GCC_except_table21
- GCC_except_table22
- GCC_except_table44
- GCC_except_table46
- GCC_except_table50
- GCC_except_table52
- GCC_except_table57
- GCC_except_table66
- GCC_except_table67
- GCC_except_table68
- GCC_except_table71
- GCC_except_table73
- GCC_except_table77
- GCC_except_table78
- GCC_except_table86
- GCC_except_table87
- GCC_except_table89
- GCC_except_table90
- GCC_except_table91
- GCC_except_table92
- GCC_except_table93
- GCC_except_table96
- GCC_except_table97
- GCC_except_table98
- _ANEValidateMILNetworkOnHost
- _ANEValidateMILNetworkOnHost.cold.1
- _ANEValidateMLIRNetworkOnHost
- _ANEValidateNetworkCreateGenerateFailedGlobalIdentifier
- _CFArrayGetCount
- _NSLog
- __ZL15fDeviceCallbackPvP15ANEDeviceStructP24ANEProgramInstanceStruct28ANENotificationMessageStruct
- __ZL15fDeviceCallbackPvP15ANEDeviceStructP24ANEProgramInstanceStruct28ANENotificationMessageStruct.cold.1
- __ZL15fDeviceCallbackPvP15ANEDeviceStructP24ANEProgramInstanceStruct28ANENotificationMessageStruct.cold.2
- __ZNKSt9type_infoeqB9nqe210106ERKS_
- __ZNSt12length_errorC1B9nqe210106EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106ILi0EEEPKc
- __ZNSt3__119__shared_weak_count16__release_sharedB9nqe210106Ev
- __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- ___112-[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:]_block_invoke
- ___65-[_ANEDaemonConnection purgeCompiledModelMatchingHash:withReply:]_block_invoke.22
- ___65-[_ANEDaemonConnection purgeCompiledModelMatchingHash:withReply:]_block_invoke.22.cold.1
- ___65-[_ANEVirtualClient evaluateWithModel:options:request:qos:error:]_block_invoke.82
- ___65-[_ANEVirtualClient evaluateWithModel:options:request:qos:error:]_block_invoke.90
- ___65-[_ANEVirtualClient validateNetworkCreateMLIR:validation_params:]_block_invoke
- ___66-[_ANEDaemonConnection compiledModelExistsMatchingHash:withReply:]_block_invoke.21
- ___66-[_ANEDaemonConnection compiledModelExistsMatchingHash:withReply:]_block_invoke.21.cold.1
- ___71-[_ANEClient doLoadModelNewInstance:options:modelInstParams:qos:error:]_block_invoke.29
- ___71-[_ANEClient doLoadModelNewInstance:options:modelInstParams:qos:error:]_block_invoke.29.cold.1
- ___71-[_ANEClient doLoadModelNewInstance:options:modelInstParams:qos:error:]_block_invoke.29.cold.2
- ___Block_byref_object_copy_.120
- ___Block_byref_object_copy_.129
- ___Block_byref_object_copy_.47
- ___Block_byref_object_copy_.91
- ___Block_byref_object_dispose_.121
- ___Block_byref_object_dispose_.130
- ___Block_byref_object_dispose_.48
- ___Block_byref_object_dispose_.92
- ___block_descriptor_125_ea8_32s40s48s56bs64r72r80r88r_e51_v72?0{ANENotificationMessageStruct=ii^v[4^v][4I]}8lr64l8r72l8s32l8s40l8r80l8s48l8s56l8r88l8
- ___block_descriptor_40_e8_32bs_e59_v56?0B8"NSDictionary"12Q20Q28c36"NSString"40"NSError"48ls32l8
- ___block_descriptor_48_ea8_32s40s_e33_v24?0"IOSurfaceSharedEvent"8Q16ls32l8s40l8
- ___block_descriptor_76_e8_32s40r48r_e59_v56?0B8"NSDictionary"12Q20Q28c36"NSString"40"NSError"48ls32l8r40l8r48l8
- ___block_literal_global.231
- ___block_literal_global.236
- ___block_literal_global.24
- ___block_literal_global.247
- ___block_literal_global.261
- ___block_literal_global.266
- _objc_msgSend$copyToIOSurface:length:ioSID:
- _objc_msgSend$freeModelFileIOSurfaces:
- _objc_msgSend$getCFDictionaryFromIOSurface:dataLength:
- _objc_msgSend$initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:mpsConstants:
- _objc_msgSend$trimmedModelPath:trimmedPath:
- _objc_msgSend$updateModelAttributes:state:programHandle:intermediateBufferHandle:queueDepth:
- _objc_msgSend$validateNetworkCreateMLIR:validation_params:
- _strcpy
CStrings:
+ "\""
+ "%02x "
+ "%@: ANEProgramMapMutableWeightsBuffer failed with result=%d"
+ "%@: ANEProgramUnmapMutableWeightsBuffer failed with result=%d"
+ "%@: ANE_DEBUG=%@"
+ "%@: Assets needed on host but not transferred already, transferring assets."
+ "%@: Attempting updatePurgeabilityLevelForModelTrackedByHash"
+ "%@: BAD_ARGUMENT ERROR failed to call compiledModelExistsFor model.modelURL is nil AND model.cacheURLIdentifier is nil! At least one required."
+ "%@: BAD_ARGUMENT ERROR failed to compileModel (file does not exist) with model.modelURL.path=%@"
+ "%@: BAD_ARGUMENT ERROR failed to compiledModelExistsFor (file does not exist) with model.modelURL.path=%@"
+ "%@: BAD_ARGUMENT ERROR failed to loadModel (file does not exist) with model.modelURL.path=%@"
+ "%@: BAD_ARGUMENT ERROR failed to purgeCompiledModel (file does not exist) with model.modelURL.path=%@"
+ "%@: BAD_ARGUMENT directoryPath is nil or empty-string"
+ "%@: BAD_ARGUMENT model.modelURL.path points to file with .hwx extension. Model is precompiled!"
+ "%@: BAD_ARGUMENT uuidString is nil or empty-string. Model UUID is required to transfer assets to host!"
+ "%@: BEGIN assetExistsOnHost assetTransferUUID=%@"
+ "%@: BEGIN compileModel model.modelURL.path=%@ model.string_id=0x%llx"
+ "%@: BEGIN compiledModelExistsFor model.modelURL=%@ model.cacheURLIdentifier=%@ model.string_id=0x%llx"
+ "%@: BEGIN loadModel model.cacheURLIdentifier=%@ model.string_id=0x%llx model.UUID=%@"
+ "%@: BEGIN purgeCompiledModel model.modelURL.path=%@ model.string_id=0x%llx model.cacheURLIdentifier=%@"
+ "%@: Calling ANEProgramMapMutableWeightsBuffer for procedure=%@ bufferID=%llu programHandle=0x%llx"
+ "%@: Can't request scheduling on a particular ane instance without request single ane procedure variant (proc variant: %u, ane instance %u)\n"
+ "%@: Created reusable IOSurface with ioSID=%u for chunked transfer"
+ "%@: Created shared IOSurface with ioSID=%u (size=%u) for all file transfers"
+ "%@: DEBUG extracted mpsConstantsCount=%u"
+ "%@: DEBUG model.mpsConstants=%@ (count=%lu)"
+ "%@: Debug file does not exist at path: %@"
+ "%@: Debug file is not readable at path: %@"
+ "%@: Debug file validation successful: %@"
+ "%@: Direct mapping failed: %@"
+ "%@: Direct mapping succeeded, buffer=%p size=%llu"
+ "%@: ERROR : BAD_ARGUMENT : Failed to loadModel, model.URL is nil and cacheURLIdentifier is nil!"
+ "%@: ERROR : BAD_ARGUMENT : directoryPaths URL list variable is nil!"
+ "%@: ERROR : BAD_ARGUMENT : uuidString is nil or empty-string!"
+ "%@: ERROR : BAD_ARGUMENT input string is nil or has length=0!"
+ "%@: ERROR : Failed to create unarchiver with error=%@"
+ "%@: ERROR : Failed to decode error description string from archived data"
+ "%@: ERROR Could not extract model from IOSurface with dataSize=%llu"
+ "%@: ERROR Failed to call assetExistsOnHost, could not write UUID to input buffer"
+ "%@: ERROR Failed to create dataBuffer object! Could not transfer directory metadata"
+ "%@: ERROR Failed to directory metadata to host"
+ "%@: ERROR Failed to transfer assets, could not get contents of directory at path %@ with error %@"
+ "%@: ERROR Failed to transfer assets, could not get resource values for URL %@ with error %@"
+ "%@: ERROR Failed to transfer file to host at path: %@"
+ "%@: ERROR Failed to write string to buffer, data will overflow! inputStringLength=%zu > bufferLength=%zu"
+ "%@: ERROR Missing mutableWeightsBufferInfo at index %lu! Cannot cache its size!"
+ "%@: ERROR ambiguous file metadata found. isDirectory=NO, isRegularFile=NO. Failed to transfer asset at path=%@"
+ "%@: ERROR compileModel failed, could not transfer assets to host model.modelURL.path=%@ modelFileParentDirectory=%@"
+ "%@: ERROR failed to create reusable IOSurface for chunked transfer with chunkSize=%u at path=%@"
+ "%@: ERROR failed to create shared IOSurface for asset transfers!"
+ "%@: ERROR failed to populate dataBuffer (length is 0!). Could not transfer directory metadata"
+ "%@: ERROR failed to transfer ANE compileModel metadata to host! Could not get csIdentity"
+ "%@: ERROR failed to transfer ANE compiledModelExistsFor metadata to host! Could not get csIdentity"
+ "%@: ERROR failed to transfer ANE purgeCompiledModel metadata to host! Could not get csIdentity"
+ "%@: ERROR failed to transfer adapter metadata to host! Failed to populate UUID"
+ "%@: ERROR failed to transfer compileModel metadata to host, unable to create IOSurface for return model object, ioSID is 0!"
+ "%@: ERROR failed to transfer compileModel metadata to host, unable to serialize model to NSData with error=%@!"
+ "%@: ERROR failed to transfer compileModel metadata to host, unable to write model data to IOSurface!"
+ "%@: ERROR failed to transfer compileModel metadata to host, unable to write options data to IOSurface!"
+ "%@: ERROR failed to transfer compiledModelExistsFor metadata to host, unable to create IOSurface for return model object, ioSID is 0!"
+ "%@: ERROR failed to transfer compiledModelExistsFor metadata to host, unable to serialize model to NSData with error=%@!"
+ "%@: ERROR failed to transfer compiledModelExistsFor metadata to host, unable to write model data to IOSurface!"
+ "%@: ERROR failed to transfer directory metadata, host reported an error"
+ "%@: ERROR failed to transfer file to host! Could not populate UUID"
+ "%@: ERROR failed to transfer file to host! Could not write uuidString to struct uuidStringLength=%zu bufferLength=%zu"
+ "%@: ERROR failed to transfer file to host! Could not write uuidString to struct, data will overflow. uuidStringLength=%zu > bufferLength=%zu"
+ "%@: ERROR failed to transfer file to host! No UUID string provided"
+ "%@: ERROR failed to transfer loadModel metadata to host, unable to create IOSurface for return model object, ioSID is 0!"
+ "%@: ERROR failed to transfer loadModel metadata to host, unable to serialize model to NSData with error=%@!"
+ "%@: ERROR failed to transfer loadModel metadata to host, unable to write model data to IOSurface!"
+ "%@: ERROR failed to transfer loadModel metadata to host, unable to write options data to IOSurface!"
+ "%@: ERROR failed to transfer purgeCompiledModel metadata to host, unable to create IOSurface for return model object, ioSID is 0!"
+ "%@: ERROR failed to transfer purgeCompiledModel metadata to host, unable to serialize model to NSData with error=%@!"
+ "%@: ERROR failed to transfer purgeCompiledModel metadata to host, unable to write model data to IOSurface!"
+ "%@: ERROR failed to transferAssetsForModel, asset not found at path=%@"
+ "%@: ERROR failed to transferAssetsForModel, could not transfer directory at path=%@"
+ "%@: ERROR failed to transferAssetsForModel, could not transfer file at path=%@"
+ "%@: ERROR failed to write csIdentity to struct inputStringLength=%zu bufferLength=%zu"
+ "%@: ERROR host returned outModelDataSize = 0! Could not extract model object."
+ "%@: ERROR host returned success=0"
+ "%@: ERROR loadModelNewInstance failed, could not create shared IOSurface for file transfers!"
+ "%@: ERROR model.modelURL points to a precompiled (.hwx) binary but kANEFModelPreCompiledValue not found in options dictionary"
+ "%@: ERROR mpsConstants key '%@' exceeds max length %d"
+ "%@: ERROR mpsConstants key=%@ has no valid IOSurface"
+ "%@: ERROR too many mpsConstants (%lu), max is %d"
+ "%@: ERROR: inputPath '%@' is not under parent directory '%@'"
+ "%@: Expected the residency to be set to ANE Instance %u based on the hint, but was set to %u instead. Please check whether the hint was received and applied by the scheduler\n"
+ "%@: Expected to be scheduled on single ANE, current residency = %u"
+ "%@: Failed to get numANECores, default to 2"
+ "%@: File does not have .anedebug extension: %@"
+ "%@: Found %lu inspectable tensors"
+ "%@: Found %lu matchingAssetPaths for modelType=%@"
+ "%@: Found %lu patterns for modelType=%@"
+ "%@: Host too old to support createValidationResultForNetworkCreateMLIR. NegotiatedDataInterfaceVersion=%u"
+ "%@: IFP model load rejected; caller missing entitlement %@."
+ "%@: Invalid arguments"
+ "%@: Invalid regex pattern '%@': %@"
+ "%@: Looking for debug file at: %@"
+ "%@: Looking for debug file for model: %@"
+ "%@: Mapping mutable weights via direct device access"
+ "%@: Model size exceeds device limit"
+ "%@: No device available"
+ "%@: Normalizing intermediate tensor '%@' (index: %lu) in-place"
+ "%@: Procedure %@ not found in model"
+ "%@: Properties not found, default to 2 cores"
+ "%@: Raw tensor - size: %zu bytes, dimensions: %zux%zu"
+ "%@: Raw tensor unchanged (client will receive un-normalized data)"
+ "%@: Released shared IOSurface after all file transfers"
+ "%@: Reusing existing IOSurface with ioSID=%u (size=%u) for chunked transfer"
+ "%@: STUB - ANELoader in-place normalization not yet implemented"
+ "%@: Searching for patterns for modelType=%@"
+ "%@: Stub implementation - returning sample tensor descriptors"
+ "%@: Successfully mapped buffer at address=%p size=%llu"
+ "%@: Successfully transferred assets at path=%@"
+ "%@: Taking queued request path, returning YES without perfStats update"
+ "%@: Transfer complete fileSize=%llu chunkSize=%u at path=%@"
+ "%@: Transferred all assets to host"
+ "%@: Transferring asset at path=%@"
+ "%@: Transferring assets to host at path=%@ with assetTransferUUID=%@ with modelType=%@"
+ "%@: Transferring directoryMetaData with directoryCount=%u"
+ "%@: Unmapping mutable weights buffer failed"
+ "%@: Using direct unmapping via program"
+ "%@: already unmapped for bufferID=%llu procedure=%@"
+ "%@: assetExistsOnHost result=%d"
+ "%@: assetTransferUUID is nil!"
+ "%@: buffer is nil"
+ "%@: compileModel SUCCESS : model.cacheURLIdentifier=%@ model.string_id=0x%llx"
+ "%@: compiledModelExistsFor SUCCESS : result=%d model.modelURL=%@ model.cacheURLIdentifier=%@ model.string_id=0x%llx"
+ "%@: csops_audittoken(%d) failed. %{darwin.errno}d"
+ "%@: debugInfoFileURL is nil"
+ "%@: debugInfoFileURL: %@"
+ "%@: descriptor is nil"
+ "%@: error getting attributes for file (%@): %@"
+ "%@: error getting size for file (%@): %@"
+ "%@: evaluateWithModelDataOut.success is false with ERROR %@"
+ "%@: extracted %u mpsConstants IOSurfaceIDs and keys"
+ "%@: failed to issue write sandbox extension for capture folder: %@"
+ "%@: failed to resolve CWD for relative capture_folder path; skipping capture_folder"
+ "%@: inputBuffer symbolIndex=%u >= model.numInputs=%u"
+ "%@: inputIndexArray[%u]=%u >= lModel.numInputs=%u"
+ "%@: leaking mapped buffer bufferID=%llu refCount=%u — unmapping now"
+ "%@: loadModel SUCCESS : model.programHandle=%llu model.cacheURLIdentifier=%@ model.string_id=0x%llx"
+ "%@: model is nil"
+ "%@: model.program is nil"
+ "%@: model.program is nil, cannot map mutable weights"
+ "%@: modelURL is nil"
+ "%@: mpsConstants[%u] key=%@ ioSID=%u"
+ "%@: negotiatedDataInterfaceVersion < kAppleVirtIONeuralEngineDeviceInterface_2_4_7, using legacy interface"
+ "%@: negotiatedDataInterfaceVersion < kAppleVirtIONeuralEngineDeviceInterface_2_5_0, mutable weights VM support not available"
+ "%@: outputBuffer symbolIndex=%u >= model.numOutputs=%u"
+ "%@: outputIndexArray[%u]=%u >= lModel.numOutputs=%u"
+ "%@: path does not exist (%@)"
+ "%@: procedureSymbolName is nil"
+ "%@: purgeCompiledModel SUCCESS : model.cacheURLIdentifier=%@ model.string_id=0x%llx"
+ "%@: rawTensor is NULL"
+ "%@: released one reference for bufferID=%llu procedure=%@, %u remaining"
+ "%@: released one reference for bufferID=%llu, %u remaining"
+ "%@: reusing existing IOSurface for bufferID=%llu success=%d"
+ "%@: reusing existing mapping for bufferID=%llu procedure=%@, refCount=%u"
+ "%@: size is nil"
+ "%@: sourceModel is nil"
+ "%@: unmapped bufferID=%llu procedure=%@"
+ "%@: { statsSurRef=%p ; outputBuffer=%@}"
+ "%@_%@"
+ "%@_0x%x"
+ "%@_adhoc"
+ "%@_platform"
+ "%@_unsigned"
+ "%s: caller provided architecture=%@, device=%@; honoring caller"
+ "%s: procedure %@ dealloc'd with buffer ID=%llu still in map"
+ "%{public}@: [_ANEDeviceInfo numANEs] No ANEs found on system"
+ "%{public}@: boot-args has %{public}@ - allow any path for Pre-compiled models"
+ "'"
+ "*"
+ "*.llir.bundle"
+ "+[_ANEVirtualClient createCFDictionaryFromIOSurface:dataLength:]"
+ "-[_ANEProgramProcedurePriv dealloc]"
+ "-[_ANEVirtualClient doMapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:]"
+ "-[_ANEVirtualClient doSyncMutableWeightsForModel:andProcedure:fromOffset:withSize:error:]"
+ "-[_ANEVirtualClient doUnmapMutableWeightsForModel:andProcedure:]"
+ ".*"
+ "0"
+ "0x%llx"
+ "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
+ ";"
+ "="
+ "@\"NSString\"16@?0@\"NSString\"8"
+ "ANEDevicePropertyNumANECores"
+ "ANEFModelMutableWeightBufferInfo"
+ "ANE_DEBUG"
+ "AppleNeuralEngineSubtype"
+ "B16@?0@\"NSString\"8"
+ "BaseAddressError"
+ "CFDictionaryRef ANECreateValidationResultForMILNetworkOnHost(uint64_t, CFDictionaryRef)"
+ "ChangeDestination"
+ "ChangeSource"
+ "Commit"
+ "ContextSwitchOut"
+ "DMAAXIError"
+ "Delay"
+ "ERROR: %s: Cannot lock IOSurface for procedure %@, kernResult=0x%x!\n"
+ "ERROR: %s: Did not find specified procedure symbol name: %@ in programInstance!\n"
+ "ERROR: %s: End of modified region (%llu) exceeds buffer size %llu!\n"
+ "ERROR: %s: Failed to create IOSurface for procedure %@!\n"
+ "ERROR: %s: Guest KMD map call failed for procedure %@, kernResult=0x%x success=%d!\n"
+ "ERROR: %s: Guest KMD sync call failed for procedure %@, kernResult=0x%x success=%d!\n"
+ "ERROR: %s: Guest KMD unmap call failed for procedure %@, kernResult=0x%x success=%d!\n"
+ "ERROR: %s: Modified region offset %llu exceeds buffer size %llu!\n"
+ "ERROR: %s: MutableWeightsBuffer is not mapped for progHandle=%llx, procedureSymbolName=%@.\n"
+ "ERROR: %s: Procedure %u name: %@\n"
+ "ERROR: %s: mutableWeightsBufferPtr = nil for procedure %i %@!\n"
+ "ERROR: %s: mutableWeightsBufferPtr at index %i = nil!\n"
+ "ERROR: %s: mutableWeightsBufferPtr->size == 0 for procedure %i %@!\n"
+ "ERROR: %s: procedurePriv = nil for procedure %i %@!\n"
+ "ERROR: %s: procedurePriv at index %i = nil!\n"
+ "Error: %@ encountered during _updateSourcePathForModelTrackedByHash:%@ to:%@"
+ "Error: %@ encountered during updatePurgeabilityLevelForModelTrackedByHash:%@ to:%llu"
+ "FW_EnqueueTM"
+ "FetchDone"
+ "FinishExecution"
+ "FinishExecutionNEDMA"
+ "HasAppleNeuralEngine"
+ "MacInf"
+ "MacNan"
+ "Mutable weights buffer info data block returned by ANE Daemon has different size (%lu) than expected (%lu)!"
+ "Mutable weights buffer sizes data block was not returned by ANE Daemon!"
+ "MutableWeightsBuffer is already unmapped for progHandle=%llx, procedureSymbolName=%@.\n"
+ "NeNonLinearLut"
+ "NeSrcInf"
+ "NeSrcNan"
+ "NoHighestPriority"
+ "OutputToL2"
+ "PeGlobalReductInf"
+ "PeGlobalReductNan"
+ "PeOutputNan"
+ "PeSrc1Inf"
+ "PeSrc1Nan"
+ "PeSrc2Inf"
+ "PeSrc2Nan"
+ "PerfTracingCounter"
+ "Performance Stats Raw Data (%lu bytes):\n"
+ "PpInf"
+ "Prefetch"
+ "PrefetchFinish"
+ "PrefetchTerminate"
+ "StartExecution"
+ "TD_%u_Counter_%u"
+ "TaskSwitch"
+ "Unknown"
+ "WinoInpTransInf"
+ "WinoKernTransInf"
+ "[proxy updatePurgeabilityLevelForModelTrackedByHash:%@ to:%@...] returned success = %d with error = %@"
+ "[proxy updateSourcePathForModelTrackedByHash:%@ to:%@...] returned success = %d with error = %@"
+ "^%@$"
+ "_ANED_MODELCACHE_GC"
+ "_ANEF_MUTABLE_WEIGHTS_BUFFER_MAP_END"
+ "_ANEF_MUTABLE_WEIGHTS_BUFFER_MAP_START"
+ "_ANEF_MUTABLE_WEIGHTS_BUFFER_UNMAP_END"
+ "_ANEF_MUTABLE_WEIGHTS_BUFFER_UNMAP_START"
+ "_ANEValidateNetworkArchitectureUsed"
+ "_ANEValidateNetworkReturnArchitectureUsed"
+ "_ANEValidateNetworkVMGuestOrigin"
+ "_ANEVirtualClient createCFDictionaryFromIOSurface : Couldn't create CFDictionaryRef object"
+ "_ANEVirtualClient createCFDictionaryFromIOSurface : DataBaseAddress null"
+ "_ANEVirtualClient createCFDictionaryFromIOSurface : couldn't create CFDataRef object"
+ "_ANEVirtualClient createCFDictionaryFromIOSurface : ioSurfaceRef null"
+ "__IFP"
+ "_updatePurgeabilityLevelForModelTrackedByHash:%@ to:%llu"
+ "_updateSourcePathForModelTrackedByHash:%@ to:%@"
+ "a"
+ "a!"
+ "anedebug"
+ "auxData"
+ "capture_bytecode"
+ "capture_elide_resources"
+ "capture_folder"
+ "capture_include_locations"
+ "capturedCompletionHandler is NULL in error block! request=%p"
+ "capturedCompletionHandler is NULL in success else! request=%p"
+ "capturedCompletionHandler is NULL! request=%p"
+ "com.apple.private.ane.mappingMutableWeightsBuffer.allow"
+ "decodePerformanceStats: Decoded %lu performance counters"
+ "decodePerformanceStats: Decoded raw stats with %@ descriptors"
+ "decodePerformanceStats: HW execution time = %.2f ms"
+ "decodePerformanceStats: Invalid arguments (perfStats=%p, options=%p)"
+ "decodePerformanceStats: Missing kANEFPerformanceStatsMaskKey in options"
+ "decodeRawStatsData: Decoded %u descriptors for program %u"
+ "decodeRawStatsData: Invalid data (length=%lu, expected>=%lu)"
+ "decodeRawStatsData: Invalid stats type %u (expected %u)"
+ "descriptors"
+ "dumpPerformanceStats: No pStatsRawData to dump"
+ "eventTypeValue"
+ "events"
+ "executionTime"
+ "externConstants"
+ "false"
+ "finishTime"
+ "kANEFAneInstanceHint"
+ "kANEFDebugCaptureBytecodeKey"
+ "kANEFDebugCaptureElideResourcesKey"
+ "kANEFDebugCaptureFolderKey"
+ "kANEFDebugCaptureFolderSandboxExtensionKey"
+ "kANEFDebugCaptureIncludeLocationsKey"
+ "kANEFDebugOptionsKey"
+ "kANEFIntermediateBufferSizeHint"
+ "kANEFIntermediateTensorDescriptorKey"
+ "kANEFProcedureVariantHint"
+ "kANEFTargetArchitectureKey"
+ "metadata"
+ "mutableWeightsBufferID"
+ "mutableWeightsBufferSize"
+ "numDescriptors"
+ "numTDs"
+ "perTdPerfCounters"
+ "perTdPerfCountersConfig"
+ "priority"
+ "procedureId"
+ "processId"
+ "programId"
+ "rawStats"
+ "startTime"
+ "tdExecutionTimes"
+ "tensorIndex"
+ "tensorName"
+ "tensor_1_intermediate"
+ "tensor_2_intermediate"
+ "tensor_3_intermediate"
+ "tid"
+ "timeStamp"
+ "totalEventsReceived"
+ "totalEventsRecorded"
+ "totalExecutionTime"
+ "v280@?0{ANENotificationMessage=ii^v[4^v][4I][4[4^v]][4[4I]]QBCC}8"
+ "v64@?0B8@\"NSDictionary\"12Q20Q28c36I40I44@\"NSString\"48@\"NSError\"56"
+ "value_ms"
+ "value_ns"
- "%@: BEGIN loadModel model=%@"
- "%@: Created reusable IOSurface with ioSID=%u (size=%u) for chunked transfer"
- "%@: ERROR failed to create IOSurface for chunked transfer with chunkSize=%u at path=%@"
- "%@: ERROR failed to transfer ANE model file to host! Could not write csIdentity to struct csIdentityStringLength=%zu bufferLength=%u"
- "%@: ERROR failed to transfer ANE model file to host! Could not write csIdentity to struct, data will overflow. csIdentityStringLength=%zu > bufferLength=%u"
- "%@: ERROR failed to transfer adapter metadata to host! Could not write uuidString to struct uuidStringLength=%zu bufferLength=%u"
- "%@: ERROR failed to transfer adapter metadata to host! Could not write uuidString to struct, data will overflow. uuidStringLength=%zu > bufferLength=%u"
- "%@: ERROR failed to transfer file to host! Could not write uuidString to struct uuidStringLength=%zu bufferLength=%u"
- "%@: ERROR failed to transfer file to host! Could not write uuidString to struct, data will overflow. uuidStringLength=%zu > bufferLength=%u"
- "%@: ERROR failed to transfer file to host! Filetype is kVirtANEFileTypeBin but no uuidString provided"
- "%@: Host too old to support validateNetworkCreateMLIR. NegotiatedDataInterfaceVersion=%u"
- "%@: Unknown aneSubType"
- "%@: [_ANEDeviceInfo numANEs] No ANEs found on system"
- "%@: boot-args has %@ - allow any path for Pre-compiled models"
- "%@: identifierSource=%u"
- "%@: inputBuffer[%u]=%@ symbolIndex=%lu exceeds kANERequestMaxSymbolIndex=%d"
- "%@: inputIndexArray[%u]=%@ length=%lu exceeds kANERequestMaxSymbolIndex=%d"
- "%@: outputIndexArray[%u]=%@ length=%lu exceeds kANERequestMaxSymbolIndex=%d"
- "%@: outputIndexArray[%u]=%@ symbolIndex=%lu exceeds kANERequestMaxSymbolIndex=%d"
- "%@: { statsSurRef=%@ ; outputBuffer=%@}"
- "+N9mZUAHooNvMiQnjeTJ8g"
- "+[_ANEVirtualClient getCFDictionaryFromIOSurface:dataLength:]"
- ".cxx_destruct"
- "@\"IOSurfaceSharedEvent\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSString\""
- "@\"NSURL\""
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@\"_ANEClient\""
- "@\"_ANEDaemonConnection\""
- "@\"_ANEDeviceController\""
- "@\"_ANEIOSurfaceObject\""
- "@\"_ANEInMemoryModelDescriptor\""
- "@\"_ANEModel\""
- "@\"_ANEPerformanceStats\""
- "@\"_ANEProgramForEvaluation\""
- "@\"_ANEProgramIOSurfacesMapper\""
- "@\"_ANESharedEvents\""
- "@\"_ANEVirtualClient\""
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8I16"
- "@20@0:8i16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^v16"
- "@24@0:8^{VMData=^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}[32^{__IOSurface}][32^{__IOSurface}]{VirtANEModel=IqIIIIQQQQ[32I][32Q][32I][32Q]QQQcCIQIIIQIIQIQ[64I][64I][64I][64I]IQQ[64I][64I]IIIIIIQqIIQIQIQIQIQIQIQ}{VirtANEModel=IqIIIIQQQQ[32I][32Q][32I][32Q]QQQcCIQIIIQIIQIQ[64I][64I][64I][64I]IQQ[64I][64I]IIIIIIQqIIQIQIQIQIQIQIQ}^{__IOSurface}^{__IOSurface}}16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8^{__IOSurface=}16"
- "@28@0:8@16B24"
- "@28@0:8@16i24"
- "@28@0:8I16@20"
- "@28@0:8Q16B24"
- "@32@0:8*16Q24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8@16^@24"
- "@32@0:8@16q24"
- "@32@0:8Q16@24"
- "@32@0:8^^v16^I24"
- "@32@0:8^{__CFDictionary=}16^{__CFString=}24"
- "@32@0:8^{__IOSurface=}16@24"
- "@32@0:8^{__IOSurface=}16Q24"
- "@32@0:8q16@24"
- "@36@0:8@16B24@28"
- "@36@0:8@16Q24c32"
- "@36@0:8Q16Q24c32"
- "@36@0:8^{__IOSurface=}16@24B32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24q32"
- "@40@0:8@16Q24@32"
- "@40@0:8I16I20Q24B32B36"
- "@40@0:8Q16@24@32"
- "@40@0:8Q16@24Q32"
- "@40@0:8^{ANENotificationMessageStruct=ii^v[4^v][4I]}16@24@32"
- "@40@0:8^{__IOSurface=}16#24Q32"
- "@44@0:8@16@24@32B40"
- "@44@0:8@16@24@32i40"
- "@44@0:8I16@20@28Q36"
- "@44@0:8Q16I24q28@36"
- "@48@0:8@16@24@32@40"
- "@52@0:8Q16I24q28@36Q44"
- "@52@0:8{?=[8I]}16i48"
- "@56@0:8@16@24@32@40@48"
- "@56@0:8@16@24@32q40@48"
- "@56@0:8^{__IOSurface=}16Q24^{__IOSurface=}32Q40Q48"
- "@60@0:8@16@24q32@40@48B56"
- "@60@0:8{?=[8I]}16@48i56"
- "@64@0:8@16@24@32@40@48@56"
- "@64@0:8@16@24@32q40@48@56"
- "@72@0:8@16@24@32@40@48@56@64"
- "@80@0:8@16@24@32@40@48@56@64@72"
- "@88@0:8@16@24@32@40@48@56@64@72@80"
- "@88@0:8@16@24@32@40q48@56@64B72Q76B84"
- "@96@0:8@16@24@32@40q48@56@64B72Q76B84@88"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8^{__CFDictionary=}16"
- "B28@0:8@16B24"
- "B28@0:8@16S24"
- "B28@0:8I16^@20"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B32@0:8@16^{__IOSurface=}24"
- "B32@0:8@16q24"
- "B32@0:8^{VMData=^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}[32^{__IOSurface}][32^{__IOSurface}]{VirtANEModel=IqIIIIQQQQ[32I][32Q][32I][32Q]QQQcCIQIIIQIIQIQ[64I][64I][64I][64I]IQQ[64I][64I]IIIIIIQqIIQIQIQIQIQIQIQ}{VirtANEModel=IqIIIIQQQQ[32I][32Q][32I][32Q]QQQcCIQIIIQIIQIQ[64I][64I][64I][64I]IQQ[64I][64I]IIIIIIQqIIQIQIQIQIQIQIQ}^{__IOSurface}^{__IOSurface}}16^@24"
- "B36@0:8@16B24^@28"
- "B36@0:8I16@20^@28"
- "B36@0:8I16^{VirtANEModel=IqIIIIQQQQ[32I][32Q][32I][32Q]QQQcCIQIIIQIIQIQ[64I][64I][64I][64I]IQQ[64I][64I]IIIIIIQqIIQIQIQIQIQIQIQ}20^{VirtANEModel=IqIIIIQQQQ[32I][32Q][32I][32Q]QQQcCIQIIIQIIQIQ[64I][64I][64I][64I]IQQ[64I][64I]IIIIIIQqIIQIQIQIQIQIQIQ}28"
- "B40@0:8@16@24^@32"
- "B40@0:8@16^{__CFDictionary=}24^{__CFArray=}32"
- "B40@0:8^{__IOSurface=}16Q24^@32"
- "B44@0:8@16@24B32^@36"
- "B44@0:8@16@24I32^@36"
- "B44@0:8I16@20@28^@36"
- "B48@0:8@16@24@32^@40"
- "B48@0:8@16@24^B32Q40"
- "B48@0:8@16^{__CFArray=}24@32@40"
- "B48@0:8^{__IOSurface=}16Q24q32^@40"
- "B52@0:8@16@24@32I40^@44"
- "B52@0:8@16I24@28@36@44"
- "B56@0:8@16@24@32@40^@48"
- "B60@0:8@16@24@32I40@44^@52"
- "B76@0:8@16@24I32Q36Q44@52^I60^@68"
- "CFDictionaryRef ANEValidateMILNetworkOnHost(uint64_t, CFDictionaryRef)"
- "I"
- "I16@0:8"
- "I20@0:8I16"
- "I20@0:8i16"
- "I28@0:8@16I24"
- "I32@0:8^{__CFDictionary=}16^{__CFString=}24"
- "JSONObjectWithData:options:error:"
- "NSCoding"
- "NSCopying"
- "NSSecureCoding"
- "Private"
- "Q"
- "Q16@0:8"
- "Q20@0:8I16"
- "Q32@0:8^{__CFDictionary=}16^{__CFString=}24"
- "T@\"IOSurfaceSharedEvent\",R,N,V_sharedEvent"
- "T@\"NSArray\",&,N,V_signalEvents"
- "T@\"NSArray\",&,N,V_waitEvents"
- "T@\"NSArray\",R,N,V_inputArray"
- "T@\"NSArray\",R,N,V_inputBuffer"
- "T@\"NSArray\",R,N,V_inputBufferInfoIndex"
- "T@\"NSArray\",R,N,V_inputFreeValue"
- "T@\"NSArray\",R,N,V_inputIndexArray"
- "T@\"NSArray\",R,N,V_loopbackInputSymbolIndex"
- "T@\"NSArray\",R,N,V_loopbackOutputSymbolIndex"
- "T@\"NSArray\",R,N,V_outputArray"
- "T@\"NSArray\",R,N,V_outputBuffer"
- "T@\"NSArray\",R,N,V_outputIndexArray"
- "T@\"NSArray\",R,N,V_outputSets"
- "T@\"NSArray\",R,N,V_perfStatsArray"
- "T@\"NSArray\",R,N,V_priorityQ"
- "T@\"NSArray\",R,N,V_procedureArray"
- "T@\"NSArray\",R,N,V_signalEvents"
- "T@\"NSArray\",R,N,V_weightArray"
- "T@\"NSData\",R,C,N,V_SHACode"
- "T@\"NSData\",R,C,N,V_networkText"
- "T@\"NSData\",R,N,V_optionsPlist"
- "T@\"NSData\",R,N,V_pStatsRawData"
- "T@\"NSData\",R,N,V_perfCounterData"
- "T@\"NSDictionary\",&,N,V_modelAttributes"
- "T@\"NSDictionary\",R,N,V_mpsConstants"
- "T@\"NSDictionary\",R,N,V_weights"
- "T@\"NSMutableDictionary\",R,N,V_connections"
- "T@\"NSMutableDictionary\",R,N,V_connectionsUsedForLoadingModels"
- "T@\"NSNumber\",C,N,V_transactionHandle"
- "T@\"NSNumber\",R,C,N,V_procedureIndex"
- "T@\"NSNumber\",R,N,V_fwEnqueueDelay"
- "T@\"NSNumber\",R,N,V_memoryPoolId"
- "T@\"NSNumber\",R,N,V_procedureIndex"
- "T@\"NSNumber\",R,N,V_startOffset"
- "T@\"NSNumber\",R,N,V_symbolIndex"
- "T@\"NSNumber\",R,N,V_transactionHandle"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "T@\"NSObject<OS_dispatch_semaphore>\",R,N,V_requestsInFlight"
- "T@\"NSString\",C,N,V_cacheURLIdentifier"
- "T@\"NSString\",C,N,V_compilerOptionsFileName"
- "T@\"NSString\",C,N,V_sandboxExtension"
- "T@\"NSString\",R,C,N,V_hexStringIdentifier"
- "T@\"NSString\",R,C,N,V_instanceName"
- "T@\"NSString\",R,C,N,V_key"
- "T@\"NSString\",R,C,N,V_networkTextHash"
- "T@\"NSString\",R,C,N,V_procedureSymbol"
- "T@\"NSString\",R,C,N,V_weightSymbol"
- "T@\"NSString\",R,C,N,V_weightsHash"
- "T@\"NSString\",R,N,V_csIdentity"
- "T@\"NSString\",R,N,V_modelIdentifier"
- "T@\"NSString\",R,N,V_optionsPlistHash"
- "T@\"NSString\",R,N,V_teamIdentity"
- "T@\"NSURL\",&,N,V_modelURL"
- "T@\"NSURL\",C,N,V_weightURL"
- "T@\"NSURL\",R,N,V_modelURL"
- "T@\"NSURL\",R,N,V_sourceURL"
- "T@\"NSUUID\",R,N,V_UUID"
- "T@\"NSXPCConnection\",R,N,V_daemonConnection"
- "T@\"_ANEClient\",R,N,V_sharedConnection"
- "T@\"_ANEDaemonConnection\",R,N"
- "T@\"_ANEDaemonConnection\",R,N,V_conn"
- "T@\"_ANEDeviceController\",R,N,V_controller"
- "T@\"_ANEDeviceController\",R,N,V_deviceController"
- "T@\"_ANEIOSurfaceObject\",R,N,V_ioSurfaceObject"
- "T@\"_ANEIOSurfaceObject\",R,N,V_stats"
- "T@\"_ANEIOSurfaceObject\",R,N,V_weightsBuffer"
- "T@\"_ANEInMemoryModelDescriptor\",&,N,V_descriptor"
- "T@\"_ANEModel\",&,N,V_model"
- "T@\"_ANEPerformanceStats\",&,N,V_perfStats"
- "T@\"_ANEProgramForEvaluation\",&,N,V_program"
- "T@\"_ANEProgramIOSurfacesMapper\",&,N,V_mapper"
- "T@\"_ANESharedEvents\",&,N,V_sharedEvents"
- "T@\"_ANEVirtualClient\",R,N,V_virtualClient"
- "T@?,C,V_completionHandler"
- "TB,R"
- "TB,R,N,V_allowRestrictedAccess"
- "TB,R,N,V_isMILModel"
- "TB,R,N,V_isOpenLoop"
- "TB,R,N,V_isPrivileged"
- "TB,R,N,V_isRootDaemon"
- "TB,R,N,V_restricted"
- "TB,R,N,V_signalNotRequired"
- "TI,N,V_perfStatsMask"
- "TI,R,N,V_connect"
- "TI,R,N,V_procedureIndex"
- "TI,R,N,V_setIndex"
- "TI,R,N,V_symbolIndex"
- "TQ,N,V_agentMask"
- "TQ,N,V_intermediateBufferHandle"
- "TQ,N,V_programHandle"
- "TQ,N,V_state"
- "TQ,N,V_string_id"
- "TQ,N,V_value"
- "TQ,R,N,V_eventType"
- "TQ,R,N,V_executionDelay"
- "TQ,R,N,V_hwExecutionTime"
- "TQ,R,N,V_programHandle"
- "TQ,R,N,V_signalValue"
- "TQ,R,N,V_string_id"
- "T^{ANEDeviceStruct=^v^v^vCiQ},N,V_device"
- "T^{__IOSurface=},R,N,V_ioSurface"
- "T^{__IOSurface=},R,N,V_statsSurRef"
- "Tc,N,V_queueDepth"
- "Tc,R,N,V_queueDepth"
- "Ti,R,N,V_processIdentifier"
- "Tq,N,V_usecount"
- "Tq,R,N,V_eventType"
- "Tq,R,N,V_identifierSource"
- "Tq,R,N,V_source"
- "Tq,R,N,V_statType"
- "Tq,V_currentAsyncRequestsInFlight"
- "T{os_unfair_lock_s=I},N,V_l"
- "URLByDeletingLastPathComponent"
- "URLByStandardizingPath"
- "UTF8String"
- "UUID"
- "UUIDString"
- "^{ANEDeviceStruct=^v^v^vCiQ}"
- "^{ANEDeviceStruct=^v^v^vCiQ}16@0:8"
- "^{__CFDictionary=}32@0:8Q16^{__CFDictionary=}24"
- "^{__CFDictionary=}32@0:8^{__IOSurface=}16Q24"
- "^{__CFDictionary=}36@0:8I16^{__CFDictionary=}20^@28"
- "^{__CFDictionary=}64@0:8Q16@24@32@40@48@56"
- "^{__IOSurface=}"
- "^{__IOSurface=}16@0:8"
- "^{__IOSurface=}28@0:8i16i20i24"
- "^{__IOSurface=}32@0:8@16^Q24"
- "^{__IOSurface=}32@0:8Q16^I24"
- "^{__IOSurface=}32@0:8i16i20i24i28"
- "^{__IOSurface=}40@0:8*16Q24^I32"
- "^{__IOSurface=}40@0:8@16Q24^I32"
- "^{__IOSurface=}40@0:8@16^Q24^I32"
- "_ANEBuffer"
- "_ANEChainingRequest"
- "_ANEClient"
- "_ANECloneHelper"
- "_ANEDaemonConnection"
- "_ANEDaemonProtocol"
- "_ANEDaemonProtocol_Private"
- "_ANEDataReporter"
- "_ANEDeviceController"
- "_ANEDeviceInfo"
- "_ANEErrors"
- "_ANEHashEncoding"
- "_ANEIOSurfaceObject"
- "_ANEIOSurfaceOutputSets"
- "_ANEInMemoryModel"
- "_ANEInMemoryModelDescriptor"
- "_ANEInputBuffersReady"
- "_ANELog"
- "_ANEModel"
- "_ANEModelInstanceParameters"
- "_ANEModelToken"
- "_ANEOutputSetEnqueue"
- "_ANEPerformanceStats"
- "_ANEPerformanceStatsIOSurface"
- "_ANEProcedureData"
- "_ANEProgramForEvaluation"
- "_ANEProgramIOSurfacesMapper"
- "_ANEQoSMapper"
- "_ANERequest"
- "_ANESandboxingHelper"
- "_ANESharedEvents"
- "_ANESharedSignalEvent"
- "_ANESharedWaitEvent"
- "_ANEStrings"
- "_ANEVirtualClient"
- "_ANEVirtualClient getCFDictionaryFromIOSurface : Couldn't create CFDictionaryRef object"
- "_ANEVirtualClient getCFDictionaryFromIOSurface : DataBaseAddress null"
- "_ANEVirtualClient getCFDictionaryFromIOSurface : couldn't create CFDataRef object"
- "_ANEVirtualClient getCFDictionaryFromIOSurface : ioSurfaceRef null"
- "_ANEWeight"
- "_SHACode"
- "_UUID"
- "_agentMask"
- "_allowRestrictedAccess"
- "_cacheURLIdentifier"
- "_compilerOptionsFileName"
- "_completionHandler"
- "_conn"
- "_connect"
- "_connections"
- "_connectionsUsedForLoadingModels"
- "_controller"
- "_csIdentity"
- "_currentAsyncRequestsInFlight"
- "_daemonConnection"
- "_descriptor"
- "_device"
- "_deviceController"
- "_eventType"
- "_executionDelay"
- "_fastConn"
- "_fwEnqueueDelay"
- "_hexStringIdentifier"
- "_hwExecutionTime"
- "_identifierSource"
- "_inputArray"
- "_inputBuffer"
- "_inputBufferInfoIndex"
- "_inputFreeValue"
- "_inputIndexArray"
- "_instanceName"
- "_intermediateBufferHandle"
- "_ioSurface"
- "_ioSurfaceObject"
- "_isMILModel"
- "_isOpenLoop"
- "_isPrivileged"
- "_isRootDaemon"
- "_key"
- "_l"
- "_lock"
- "_loopbackInputSymbolIndex"
- "_loopbackOutputSymbolIndex"
- "_mapper"
- "_memoryPoolId"
- "_model"
- "_modelAttributes"
- "_modelIdentifier"
- "_modelURL"
- "_mpsConstants"
- "_networkText"
- "_networkTextHash"
- "_optionsPlist"
- "_optionsPlistHash"
- "_outputArray"
- "_outputBuffer"
- "_outputIndexArray"
- "_outputSets"
- "_pStatsRawData"
- "_perfCounterData"
- "_perfStats"
- "_perfStatsArray"
- "_perfStatsMask"
- "_priorityQ"
- "_procedureArray"
- "_procedureIndex"
- "_procedureSymbol"
- "_processIdentifier"
- "_program"
- "_programHandle"
- "_queue"
- "_queueDepth"
- "_requestsInFlight"
- "_restricted"
- "_sandboxExtension"
- "_setIndex"
- "_sharedConnection"
- "_sharedEvent"
- "_sharedEvents"
- "_signalEvents"
- "_signalNotRequired"
- "_signalValue"
- "_source"
- "_sourceURL"
- "_startOffset"
- "_statType"
- "_state"
- "_stats"
- "_statsSurRef"
- "_string_id"
- "_symbolIndex"
- "_teamIdentity"
- "_transactionHandle"
- "_usecount"
- "_value"
- "_virtualClient"
- "_waitEvents"
- "_weightArray"
- "_weightSymbol"
- "_weightURL"
- "_weights"
- "_weightsBuffer"
- "_weightsHash"
- "adapterWeightsAccessEntitlement"
- "adapterWeightsAccessEntitlementBypassBootArg"
- "addEntriesFromDictionary:"
- "addIndex:"
- "addObject:"
- "addValue:forScalarKey:"
- "aggressivePowerSavingEntitlement"
- "allKeys"
- "allValues"
- "allowRestrictedAccess"
- "analyticsKey:"
- "aneArchitectureType"
- "aneArchitectureTypeStr"
- "aneBackgroundTaskQoS"
- "aneBoardType"
- "aneBoardtype"
- "aneDefaultTaskQoS"
- "aneRealTimeTaskQoS"
- "aneSubType"
- "aneSubTypeAndVariant"
- "aneSubTypeProductVariant"
- "aneSubTypeVariant"
- "aneUserInitiatedTaskQoS"
- "aneUserInteractiveTaskQoS"
- "aneUtilityTaskQoS"
- "ane_addWriteModeForPath:"
- "ane_addWriteModeIfMissing:originalMode:"
- "appendBytes:length:"
- "appendData:"
- "appendFormat:"
- "appendString:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "arguments"
- "array"
- "arrayWithObjects:count:"
- "attributesOfItemAtPath:error:"
- "badArgumentForMethod:"
- "baseModelIdentifierNotFoundForNewInstanceMethod:"
- "beginRealTimeTask"
- "beginRealTimeTaskWithReply:"
- "binExtension"
- "boolValue"
- "bootArgs"
- "bufferWithIOSurfaceObject:symbolIndex:source:"
- "buffersReadyWithModel:inputBuffers:options:qos:error:"
- "buildSpecificModelDataVaultDirectory"
- "buildSpecificUserModelDataVaultDirectory"
- "buildVersion"
- "bytes"
- "c"
- "c16@0:8"
- "c32@0:8^{__CFDictionary=}16^{__CFString=}24"
- "cStringUsingEncoding:"
- "cacheURLIdentifier"
- "callIOUserClient:inParams:outParams:"
- "callIOUserClientWithDictionary:inDictionary:error:"
- "canAccessPathAt:methodName:error:"
- "chainingRequestWithInputs:outputSets:lbInputSymbolId:lbOutputSymbolId:procedureIndex:signalEvents:transactionHandle:fwEnqueueDelay:memoryPoolId:"
- "checkKernReturnValue:selector:outParams:"
- "cloneDirectory"
- "cloneIfWritable:isEncryptedModel:cloneDirectory:"
- "codeSigningIDFor:processIdentifier:"
- "compare:"
- "compileModel:options:qos:error:"
- "compileModel:sandboxExtension:options:qos:withReply:"
- "compileWithQoS:options:error:"
- "compiledModelExists"
- "compiledModelExistsFor:"
- "compiledModelExistsFor:withReply:"
- "compiledModelExistsMatchingHash:"
- "compiledModelExistsMatchingHash:withReply:"
- "compilerOptionsFileName"
- "compilerOptionsWithOptions:isCompiledModelCached:"
- "compilerServiceAccessEntitlement"
- "completionHandler"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "conn"
- "connect"
- "connectionForLoadingModel:options:"
- "connectionUsedForLoadingModel:"
- "connections"
- "connectionsUsedForLoadingModels"
- "consumeSandboxExtension:forModel:error:"
- "consumeSandboxExtension:forPath:error:"
- "containsIndex:"
- "containsObject:"
- "containsString:"
- "contentsOfDirectoryAtPath:error:"
- "controller"
- "controllerWithPrivilegedVM:"
- "controllerWithProgramHandle:"
- "convertToHexString:length:"
- "copy"
- "copyAllModelFiles:dictionary:ioSurfaceRefs:"
- "copyData:toExistingIOSurfaceRef:"
- "copyDictionaryDataToStruct:dictionary:"
- "copyDictionaryToIOSurface:copiedDataSize:createdIOSID:"
- "copyErrorValue:"
- "copyErrorValue:vmData:"
- "copyFilesInDirectoryToIOSurfaces:ioSurfaceRefs:ioSurfaceSizes:fileNames:"
- "copyLLIRBundleToIOSurface:writtenDataSize:"
- "copyModel:options:vmData:"
- "copyModelMetaData:options:dictionary:vmData:"
- "copyModelOptionFiles:options:dictionary:vmData:"
- "copyModelOptionFiles:options:vmData:"
- "copyOptions:dictionary:vmData:"
- "copyOptions:vmData:"
- "copySHA256For:toBuffer:"
- "copyToIOSurface:length:ioSID:"
- "copyToIOSurface:size:ioSID:"
- "copyWithZone:"
- "coreAnalyticsANEUsageDefaultReportedClient"
- "coreAnalyticsANEUsageKeyGroup"
- "correctFileURLFormat:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createErrorWithCode:description:"
- "createIOSurface:ioSID:"
- "createIOSurfaceWithWidth:pixel_size:height:"
- "createIOSurfaceWithWidth:pixel_size:height:bytesPerElement:"
- "currentAsyncRequestsInFlight"
- "daemon"
- "daemonConnection"
- "daemonConnectionRestricted"
- "data"
- "dataNotFoundForMethod:"
- "dataUsingEncoding:"
- "dataVaultStorageClass"
- "dataWithBytes:length:"
- "dataWithContentsOfFile:"
- "dataWithLength:"
- "date"
- "dealloc"
- "debugDescription"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decodeXPCObjectForKey:"
- "defaultANECIRFileName"
- "defaultANECIROptionsFileName"
- "defaultCompilerOptionsFilename"
- "defaultLLIRBundleName"
- "defaultMILFileName"
- "defaultMLIRFileName"
- "defaultManager"
- "defaultWeightFileName"
- "description"
- "descriptor"
- "destinationOfSymbolicLinkAtPath:error:"
- "device"
- "deviceController"
- "dictionary"
- "dictionaryGetInt64ForKey:key:"
- "dictionaryGetInt8ForKey:key:"
- "dictionaryGetNSStringForKey:key:"
- "dictionaryGetUInt32ForKey:key:"
- "dictionaryGetUInt64ForKey:key:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "dispatchQueueArrayByMappingPrioritiesWithTag:"
- "doBuffersReadyWithModel:inputBuffers:options:qos:error:"
- "doEnqueueSetsWithModel:outputSet:options:qos:error:"
- "doEvaluateDirectWithModel:options:request:qos:error:"
- "doEvaluateWithModel:options:request:qos:completionEvent:error:"
- "doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:"
- "doJsonParsingMatchWeightName:"
- "doLoadModel:options:qos:error:"
- "doLoadModelNewInstance:options:modelInstParams:qos:error:"
- "doMapIOSurfacesWithModel:request:cacheInference:error:"
- "doPrepareChainingWithModel:options:chainingReq:qos:error:"
- "doUnloadModel:options:qos:error:"
- "driverMaskForANEFMask:"
- "eJGhnVvylF3dMOHBKJzeiw"
- "echo:"
- "echo:withReply:"
- "emitPerfcounterSignpostsWithModelStringID:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encodeXPCObject:forKey:"
- "endRealTimeTask"
- "endRealTimeTaskWithReply:"
- "enqueueSetsWithModel:outputSet:options:qos:error:"
- "entitlementErrorForMethod:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "enumeratorAtPath:"
- "errorDomainCompiler"
- "errorDomainEspresso"
- "errorDomainGeneric"
- "errorDomainVirtIO"
- "errorWithDomain:code:userInfo:"
- "evaluateRealTimeWithModel:options:request:error:"
- "evaluateWithModel:options:request:qos:error:"
- "evaluateWithQoS:options:request:error:"
- "eventPort"
- "exchangeBuildVersionInfo"
- "executionDelay"
- "fastConn"
- "fastConnWithoutLock"
- "fileAccessErrorForMethod:"
- "fileAttributes"
- "fileExistsAtPath:"
- "fileExistsAtPath:isDirectory:"
- "fileHandleForReadingAtPath:"
- "fileModificationDate"
- "fileNotFoundErrorForMethod:"
- "fileSize"
- "fileSystemRepresentation"
- "fileType"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "firstObject"
- "framework"
- "freeModelFileIOSurfaces:"
- "getCFDictionaryFromIOSurface:dataLength:"
- "getCString:maxLength:encoding:"
- "getCacheURLIdentifier"
- "getCodeSigningIdentity"
- "getDeviceInfo"
- "getDictionaryWithJSONEncodingFromIOSurface:withArchivedDataSize:"
- "getModelAttribute:"
- "getObjectFromIOSurface:classType:length:"
- "getResourceValue:forKey:error:"
- "getUUID"
- "getValidateNetworkVersion"
- "getValue:"
- "guestToHostInterfaceTooOld:"
- "hasANE"
- "hasDirectoryPath"
- "hasPrefix:"
- "hasSuffix:"
- "hash"
- "hashForString:seed:"
- "hexStringForBytes:length:"
- "hexStringForData:"
- "hexStringForDataArray:"
- "hexStringForString:"
- "hexStringIdentifier"
- "hostBuildVersionStr"
- "hostTooOld:"
- "hwxExtension"
- "i16@0:8"
- "i20@0:8I16"
- "inMemoryModelCacheName"
- "inMemoryModelWithDescriptor:"
- "indexSet"
- "init"
- "initForReadingFromData:error:"
- "initInputsProcedureIndex:inputBufferInfoIndex:inputFreeValue:executionDelay:"
- "initOutputSetWithProcedureIndex:setIndex:signalValue:signalNotRequired:isOpenLoop:"
- "initWithANEPrivilegedVM:"
- "initWithAuditToken:modelIdentifier:processIdentifier:"
- "initWithBytes:length:"
- "initWithCoder:"
- "initWithContentsOfFile:"
- "initWithContentsOfFile:options:error:"
- "initWithController:"
- "initWithController:intermediateBufferHandle:queueDepth:"
- "initWithCsIdentity:teamIdentity:modelIdentifier:processIdentifier:"
- "initWithDesctiptor:"
- "initWithDispatchQueue:"
- "initWithFormat:"
- "initWithHardwareExecution:perfCounterData:ANEStatsRawData:"
- "initWithIOSurface:startOffset:shouldRetain:"
- "initWithIOSurface:statType:"
- "initWithIOSurfaceObject:symbolIndex:source:"
- "initWithInputs:inputIndices:outputs:outputIndices:weightsBuffer:perfStats:procedureIndex:sharedEvents:transactionHandle:"
- "initWithInputs:outputs:lbInputSymbolId:lbOutputSymbolId:procedureIndex:signalEvents:transactionHandle:fwEnqueueDelay:memoryPoolId:"
- "initWithMachServiceName:options:"
- "initWithMachServiceName:restricted:"
- "initWithModelAtURL:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:"
- "initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:"
- "initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:mpsConstants:"
- "initWithModelIdentifier:"
- "initWithNetworkText:weights:optionsPlist:isMILModel:"
- "initWithProcedure:weightArray:"
- "initWithProcedureData:procedureArray:"
- "initWithProgramHandle:priviledged:"
- "initWithReconstructedData:hardwareExecutionNS:"
- "initWithRequestPerformanceBuffer:statsBufferSize:"
- "initWithRestrictedAccessAllowed:"
- "initWithSignalEvents:waitEvents:"
- "initWithSingletonAccess"
- "initWithValue:sharedEvent:eventType:"
- "initWithValue:symbolIndex:eventType:sharedEvent:agentMask:"
- "initWithVirtualModel:"
- "initWithWeightSymbolAndURL:weightURL:"
- "initWithWeightSymbolAndURLSHA:weightURL:SHACode:sandboxExtension:"
- "initWithstatsSurRef:outputBuffer:"
- "initialize"
- "inputArray"
- "inputBuffer"
- "inputBufferInfoIndex"
- "inputBuffersWithProcedureIndex:inputBufferInfoIndex:inputFreeValue:executionDelay:"
- "inputFreeValue"
- "inputIndexArray"
- "inputSymbolIndicesForProcedureIndex:"
- "integerValue"
- "interfaceWithProtocol:"
- "internalLibraryPath"
- "invalidModelErrorForMethod:"
- "invalidModelInstanceErrorForMethod:"
- "invalidModelKeyErrorForMethod:"
- "invalidate"
- "ioSurface"
- "ioSurfacesCount"
- "isAnetoolRootDaemonConnection"
- "isBoolBootArgSetTrue:"
- "isBootArgPresent:"
- "isEqual:"
- "isEqualToInMemoryModelDescriptor:"
- "isEqualToModel:"
- "isEqualToString:"
- "isExcessivePowerDrainWhenIdle"
- "isFileURL"
- "isInternalBuild"
- "isMILModel"
- "isOpenLoop"
- "isPrivileged"
- "isRootDaemon"
- "isVirtualClient"
- "isVirtualMachine"
- "issueSandboxExtensionForModel:error:"
- "issueSandboxExtensionForPath:error:"
- "l"
- "lastObject"
- "lastPathComponent"
- "launchIOKitEvent"
- "launchUserIOKitEvent"
- "length"
- "lengthOfBytesUsingEncoding:"
- "llirBundleExtension"
- "loadModel:options:qos:error:"
- "loadModel:sandboxExtension:options:qos:withReply:"
- "loadModelNewInstance:options:modelInstParams:qos:error:"
- "loadModelNewInstance:options:modelInstParams:qos:withReply:"
- "loadModelNewInstanceLegacy:options:modelInstParams:qos:error:"
- "loadRealTimeModel:options:qos:error:"
- "loadWithQoS:options:error:"
- "localModelPath"
- "longValue"
- "loopbackInputSymbolIndex"
- "loopbackOutputSymbolIndex"
- "machServiceName"
- "machServiceNamePrivate"
- "mapIOSurfacesWithModel:request:cacheInference:error:"
- "mapIOSurfacesWithRequest:cacheInference:error:"
- "mapper"
- "mapperWithController:"
- "mapperWithProgramHandle:"
- "memoryUnwireAccessEntitlement"
- "missingCodeSigningErrorForMethod:"
- "mlirExtension"
- "model"
- "modelAssetsCacheName"
- "modelAtURL:key:"
- "modelAtURL:key:modelAttributes:"
- "modelAtURL:key:mpsConstants:"
- "modelAtURLWithCacheURLIdentifier:key:cacheURLIdentifier:"
- "modelAtURLWithSourceURL:sourceURL:key:cacheURLIdentifier:"
- "modelAtURLWithSourceURL:sourceURL:key:identifierSource:cacheURLIdentifier:"
- "modelAtURLWithSourceURL:sourceURL:key:identifierSource:cacheURLIdentifier:UUID:"
- "modelBinaryName"
- "modelCacheRetainName"
- "modelDataVaultDirectory"
- "modelIdentifier"
- "modelIdentifierNotFoundForMethod:"
- "modelNewInstanceCacheIdentifierNotNilMethod:"
- "modelPurgeInAllPartitionsEntitlement"
- "modelSourceStoreName"
- "modelWithCacheURLIdentifier:"
- "modelWithCacheURLIdentifier:UUID:"
- "modelWithMILText:weights:optionsPlist:"
- "modelWithNetworkDescription:weights:optionsPlist:"
- "mutableBytes"
- "mutableCopy"
- "negotiatedCapabilityMask"
- "negotiatedDataInterfaceVersion"
- "networkText"
- "networkTextHash"
- "new"
- "nextObject"
- "noSandboxExtension"
- "notSupportedErrorForMethod:"
- "notifyListener:atValue:block:"
- "numANECores"
- "numANEs"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLong:"
- "numberWithLongLong:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLong:"
- "numberWithUnsignedLongLong:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectWithIOSurface:"
- "objectWithIOSurface:startOffset:"
- "objectWithIOSurface:statType:"
- "objectWithIOSurfaceNoRetain:startOffset:"
- "objectWithstatsSurRef:outputBuffer:"
- "optionsPlist"
- "optionsPlistHash"
- "outputArray"
- "outputBuffer"
- "outputDictIOSurfaceSize"
- "outputIndexArray"
- "outputSetWithProcedureIndex:setIndex:signalValue:signalNotRequired:isOpenLoop:"
- "outputSets"
- "outputSymbolIndicesForProcedureIndex:"
- "pStatsRawData"
- "parallelDecompressedData:"
- "path"
- "perfCounterData"
- "perfStats"
- "perfStatsArray"
- "ppsCategoryForANE"
- "ppsSubsystemForANE"
- "pps_applicationDir"
- "pps_catalogDir"
- "pps_defaultSystemPathDir"
- "pps_defaultUserPathPrefix"
- "pps_frameworkDir"
- "pps_internalDir"
- "pps_privateFrameworkDir"
- "pps_tmpDir"
- "pps_varDir"
- "precompiledModelChecksDisabled"
- "prepareANEMemoryMappingParams:request:"
- "prepareChainingWithModel:options:chainingReq:qos:error:"
- "prepareChainingWithModel:options:chainingReq:qos:withReply:"
- "printDictionary:"
- "printIOSurfaceDataInBytes:"
- "printStruct:"
- "priorityErrorForMethod:"
- "priorityQ"
- "procedureDataWithSymbol:weightArray:"
- "procedureInfoForProcedureIndex:"
- "processIdentifier"
- "processInfo"
- "processInputBuffers:model:options:error:"
- "processModelShareAccessEntitlement"
- "processName"
- "processNameFor:identifier:"
- "processOutputSet:model:options:error:"
- "processRequest:model:qos:qIndex:modelStringID:options:returnValue:error:"
- "processSessionHint:options:report:error:"
- "productName"
- "program"
- "programChainingPrepareErrorForMethod:"
- "programCreationErrorForMethod:"
- "programIOSurfacesMapErrorForMethod:code:"
- "programIOSurfacesUnmapErrorForMethod:code:"
- "programInferenceOtherErrorForMessage:model:methodName:"
- "programInferenceOtherErrorForMethod:"
- "programInferenceOverflowErrorForMethod:"
- "programInferenceProgramNotFoundForMethod:"
- "programLoadErrorForMethod:"
- "programLoadErrorForMethod:code:"
- "programLoadNewInstanceErrorForMethod:"
- "programLoadNewInstanceErrorForMethod:code:"
- "programPriorityForQoS:"
- "programWithController:intermediateBufferHandle:queueDepth:"
- "programWithHandle:intermediateBufferHandle:queueDepth:"
- "purgeCompiledModel"
- "purgeCompiledModel:"
- "purgeCompiledModel:withReply:"
- "purgeCompiledModelMatchingHash:"
- "purgeCompiledModelMatchingHash:withReply:"
- "q"
- "q16@0:8"
- "q32@0:8^{__CFDictionary=}16^{__CFString=}24"
- "q40@0:8@16@24^@32"
- "qosForProgramPriority:"
- "queue"
- "queueIndexForQoS:"
- "rangeOfString:"
- "rangeOfString:options:range:"
- "readDataOfLength:"
- "readWeightFilename:"
- "realTimeProgramPriority"
- "realTimeQueueIndex"
- "releaseIOSurfaces:"
- "releaseSandboxExtension:handle:"
- "removeItemAtPath:error:"
- "removeLastObject"
- "reportClient:modelName:"
- "reportErrorMsg:status:"
- "reportEvaluateFailure:failureReason:qIdx:"
- "reportTelemetryToCoreAnalytics:payload:"
- "reportTelemetryToPPS:playload:"
- "requestWithInputs:inputIndices:outputs:outputIndices:perfStats:procedureIndex:"
- "requestWithInputs:inputIndices:outputs:outputIndices:procedureIndex:"
- "requestWithInputs:inputIndices:outputs:outputIndices:weightsBuffer:perfStats:procedureIndex:"
- "requestWithInputs:inputIndices:outputs:outputIndices:weightsBuffer:perfStats:procedureIndex:sharedEvents:"
- "requestWithInputs:inputIndices:outputs:outputIndices:weightsBuffer:perfStats:procedureIndex:sharedEvents:transactionHandle:"
- "requestWithInputs:inputIndices:outputs:outputIndices:weightsBuffer:procedureIndex:"
- "requestsInFlight"
- "resetOnUnload"
- "restricted"
- "restrictedAccessEntitlement"
- "resume"
- "sandboxExtensionPathForModelURL:"
- "saveModelFiles"
- "scheme"
- "secondaryANECompilerServiceAccessEntitlement"
- "sendGuestBuildVersion"
- "sessionHintWithModel:hint:options:report:error:"
- "set"
- "setAgentMask:"
- "setCacheURLIdentifier:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCodeSigningIdentity:"
- "setCompilerOptionsFileName:"
- "setCompletionHandler:"
- "setCurrentAsyncRequestsInFlight:"
- "setDateFormat:"
- "setDescriptor:"
- "setDevice:"
- "setIndex"
- "setIntermediateBufferHandle:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setL:"
- "setMapper:"
- "setModel:"
- "setModelAttributes:"
- "setModelURL:"
- "setObject:atIndexedSubscript:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPerfStats:"
- "setPerfStatsMask:"
- "setProgram:"
- "setProgramHandle:"
- "setQueueDepth:"
- "setRemoteObjectInterface:"
- "setSandboxExtension:"
- "setSharedEvents:"
- "setSignalEvents:"
- "setState:"
- "setString_id:"
- "setTransactionHandle:"
- "setUsecount:"
- "setValue:"
- "setValue:forKey:"
- "setWaitEvents:"
- "setWeightURL:"
- "setWithArray:"
- "setWithObject:"
- "setWithObjects:"
- "shallowCopy"
- "sharedConnection"
- "sharedEvents"
- "sharedEventsWithSignalEvents:waitEvents:"
- "sharedPrivateConnection"
- "sharedPrivilegedConnection"
- "shouldSkipCloneFor:isEncryptedModel:"
- "shouldUsePrecompiledPath:options:shouldUseChunking:chunkingThreshold:"
- "signalEventWithValue:symbolIndex:eventType:sharedEvent:"
- "signalNotRequired"
- "signalValue"
- "signaledValue"
- "sortedArrayUsingComparator:"
- "sourceURL"
- "start"
- "statType"
- "stats"
- "statsWithHardwareExecutionNS:"
- "statsWithReconstructed:hardwareExecutionNS:aneStatsRawData:"
- "statsWithRequestPerformanceBuffer:statsBufferSize:"
- "stop"
- "storageMaintainerAccessEntitlement"
- "stringByAppendingFormat:"
- "stringByAppendingPathComponent:"
- "stringByDeletingLastPathComponent"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringForPerfCounter:"
- "stringFromDate:"
- "stringValue"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "substringFromIndex:"
- "substringToIndex:"
- "supportsSecureCoding"
- "symbolIndicesForProcedureIndex:indexArrayKey:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "systemLibraryPath"
- "systemModelPurgeNotAllowedForMethod:"
- "systemModelsCacheDirectory"
- "teamIDFor:processIdentifier:"
- "teamIdentity"
- "tempDirectory"
- "testing_ThreeSixtyModelName"
- "testing_cacheDirectory"
- "testing_cacheDirectoryWithSuffix:"
- "testing_cacheDirectoryWithSuffix:buildVersion:"
- "testing_cloneDirectory:"
- "testing_dataVaultStorageClass"
- "testing_defaultMLIRModelName"
- "testing_encryptedModelNames"
- "testing_external_modelPath"
- "testing_external_precompiledModelPath"
- "testing_inputDirectory"
- "testing_modelDirectory"
- "testing_modelDirectory:"
- "testing_modelNames"
- "testing_tempDirectory:"
- "testing_userCacheDirectory"
- "testing_userCacheDirectoryWithSuffix:"
- "testing_userCacheDirectoryWithSuffix:buildVersion:"
- "testing_userCloneDirectory:"
- "testing_userTempDirectory:"
- "testing_zeroModelName"
- "timeIntervalSince1970"
- "timeoutErrorForMethod:"
- "tokenWithAuditToken:modelIdentifier:processIdentifier:"
- "tokenWithCsIdentity:teamIdentity:modelIdentifier:processIdentifier:"
- "tool"
- "transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:"
- "trimmedModelPath:trimmedPath:"
- "unloadModel:options:qos:error:"
- "unloadModel:options:qos:withReply:"
- "unloadRealTimeModel:options:qos:error:"
- "unloadWithQoS:error:"
- "unmapIOSurfacesWithModel:request:"
- "unmapIOSurfacesWithModel:request:error:"
- "unmapIOSurfacesWithRequest:"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "unsignedShortValue"
- "updateError:error:"
- "updateError:errorLength:error:"
- "updateError:errorLength:errorCode:error:"
- "updateModelAttributes:state:"
- "updateModelAttributes:state:programHandle:intermediateBufferHandle:queueDepth:"
- "updatePerformanceStats:"
- "updatePerformanceStats:performanceStatsLength:perfStatsRawIOSurfaceRef:performanceStatsRawLength:hwExecutionTime:"
- "updateWeightURL:"
- "usecount"
- "userCloneDirectory"
- "userDaemonConnection"
- "userMachServiceName"
- "userModelDataVaultDirectory"
- "userTempDirectory"
- "v16@0:8"
- "v20@0:8I16"
- "v20@0:8c16"
- "v20@0:8{os_unfair_lock_s=I}16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8I16I20"
- "v24@0:8Q16"
- "v24@0:8^{ANEDeviceStruct=^v^v^vCiQ}16"
- "v24@0:8^{VMData=^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}[32^{__IOSurface}][32^{__IOSurface}]{VirtANEModel=IqIIIIQQQQ[32I][32Q][32I][32Q]QQQcCIQIIIQIIQIQ[64I][64I][64I][64I]IQQ[64I][64I]IIIIIIQqIIQIQIQIQIQIQIQ}{VirtANEModel=IqIIIIQQQQ[32I][32Q][32I][32Q]QQQcCIQIIIQIIQIQ[64I][64I][64I][64I]IQQ[64I][64I]IIIIIIQqIIQIQIQIQIQIQIQ}^{__IOSurface}^{__IOSurface}}16"
- "v24@0:8^{VirtANEModel=IqIIIIQQQQ[32I][32Q][32I][32Q]QQQcCIQIIIQIIQIQ[64I][64I][64I][64I]IQQ[64I][64I]IIIIIIQqIIQIQIQIQIQIQIQ}16"
- "v24@0:8^{__CFArray=}16"
- "v24@0:8^{__CFDictionary=}16"
- "v24@0:8^{__IOSurface=}16"
- "v24@0:8q16"
- "v32@0:8@\"NSString\"16@\"NSDictionary\"24"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"_ANEModel\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"_ANEModel\"16@?<v@?B@\"NSString\"@\"NSError\">24"
- "v32@0:8@16*24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8@16^{VMData=^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}[32^{__IOSurface}][32^{__IOSurface}]{VirtANEModel=IqIIIIQQQQ[32I][32Q][32I][32Q]QQQcCIQIIIQIIQIQ[64I][64I][64I][64I]IQQ[64I][64I]IIIIIIQqIIQIQIQIQIQIQIQ}{VirtANEModel=IqIIIIQQQQ[32I][32Q][32I][32Q]QQQcCIQIIIQIIQIQ[64I][64I][64I][64I]IQQ[64I][64I]IIIIIIQqIIQIQIQIQIQIQIQ}^{__IOSurface}^{__IOSurface}}24"
- "v32@0:8^{ANEMemoryMappingParamsStruct=[128{ANEBufferStruct=^{__IOSurface}IiiI}]QIIQ}16@24"
- "v32@0:8^{VirtANEModel=IqIIIIQQQQ[32I][32Q][32I][32Q]QQQcCIQIIIQIIQIQ[64I][64I][64I][64I]IQQ[64I][64I]IIIIIIQqIIQIQIQIQIQIQIQ}16^{__CFDictionary=}24"
- "v32@0:8^{__CFDictionary=}16^{VMData=^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}[32^{__IOSurface}][32^{__IOSurface}]{VirtANEModel=IqIIIIQQQQ[32I][32Q][32I][32Q]QQQcCIQIIIQIIQIQ[64I][64I][64I][64I]IQQ[64I][64I]IIIIIIQqIIQIQIQIQIQIQIQ}{VirtANEModel=IqIIIIQQQQ[32I][32Q][32I][32Q]QQQcCIQIIIQIIQIQ[64I][64I][64I][64I]IQQ[64I][64I]IIIIIIQqIIQIQIQIQIQIQIQ}^{__IOSurface}^{__IOSurface}}24"
- "v32@0:8i16I20^{VirtANEModel=IqIIIIQQQQ[32I][32Q][32I][32Q]QQQcCIQIIIQIIQIQ[64I][64I][64I][64I]IQQ[64I][64I]IIIIIIQqIIQIQIQIQIQIQIQ}24"
- "v32@0:8q16@24"
- "v36@0:8@16I24Q28"
- "v40@0:8@16@24^{VMData=^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}[32^{__IOSurface}][32^{__IOSurface}]{VirtANEModel=IqIIIIQQQQ[32I][32Q][32I][32Q]QQQcCIQIIIQIIQIQ[64I][64I][64I][64I]IQQ[64I][64I]IIIIIIQqIIQIQIQIQIQIQIQ}{VirtANEModel=IqIIIIQQQQ[32I][32Q][32I][32Q]QQQcCIQIIIQIIQIQ[64I][64I][64I][64I]IQQ[64I][64I]IIIIIIQqIIQIQIQIQIQIQIQ}^{__IOSurface}^{__IOSurface}}32"
- "v40@0:8@16^{__CFDictionary=}24^{VMData=^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}[32^{__IOSurface}][32^{__IOSurface}]{VirtANEModel=IqIIIIQQQQ[32I][32Q][32I][32Q]QQQcCIQIIIQIIQIQ[64I][64I][64I][64I]IQQ[64I][64I]IIIIIIQqIIQIQIQIQIQIQIQ}{VirtANEModel=IqIIIIQQQQ[32I][32Q][32I][32Q]QQQcCIQIIIQIIQIQ[64I][64I][64I][64I]IQQ[64I][64I]IIIIIIQqIIQIQIQIQIQIQIQ}^{__IOSurface}^{__IOSurface}}32"
- "v44@0:8@\"_ANEModel\"16@\"NSDictionary\"24I32@?<v@?B@\"NSError\">36"
- "v44@0:8@16@24I32@?36"
- "v48@0:8@16@24^{__CFDictionary=}32^{VMData=^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}^{__IOSurface}[32^{__IOSurface}][32^{__IOSurface}]{VirtANEModel=IqIIIIQQQQ[32I][32Q][32I][32Q]QQQcCIQIIIQIIQIQ[64I][64I][64I][64I]IQQ[64I][64I]IIIIIIQqIIQIQIQIQIQIQIQ}{VirtANEModel=IqIIIIQQQQ[32I][32Q][32I][32Q]QQQcCIQIIIQIIQIQ[64I][64I][64I][64I]IQQ[64I][64I]IIIIIIQqIIQIQIQIQIQIQIQ}^{__IOSurface}^{__IOSurface}}40"
- "v52@0:8@\"_ANEModel\"16@\"NSDictionary\"24@\"_ANEChainingRequest\"32I40@?<v@?B@\"NSError\">44"
- "v52@0:8@\"_ANEModel\"16@\"NSDictionary\"24@\"_ANEModelInstanceParameters\"32I40@?<v@?B@\"NSDictionary\"QQc@\"NSString\"@\"NSError\">44"
- "v52@0:8@\"_ANEModel\"16@\"NSString\"24@\"NSDictionary\"32I40@?<v@?B@\"NSDictionary\"@\"NSString\"@\"NSError\">44"
- "v52@0:8@\"_ANEModel\"16@\"NSString\"24@\"NSDictionary\"32I40@?<v@?B@\"NSDictionary\"QQc@\"NSString\"@\"NSError\">44"
- "v52@0:8@16@24@32I40@?44"
- "v52@0:8@16Q24Q32Q40c48"
- "v56@?0B8@\"NSDictionary\"12Q20Q28c36@\"NSString\"40@\"NSError\"48"
- "v72@?0{ANENotificationMessageStruct=ii^v[4^v][4I]}8"
- "validate"
- "validateEnvironmentForPrecompiledBinarySupport"
- "validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:milTextData:"
- "validateNetworkCreateMLIR:validation_params:"
- "validateRequest:model:"
- "value:withObjCType:"
- "virtualClient"
- "virtualizationDataError:"
- "virtualizationHostError:"
- "virtualizationHostError:error:"
- "virtualizationKernelError:kernelErrorCode:"
- "vm_allowPrecompiledBinaryBootArg"
- "vm_debugDumpBootArg"
- "vm_forceValidationOnGuestBootArg"
- "vm_tmpBaseDirectory"
- "waitEvent"
- "waitEventWithValue:sharedEvent:"
- "waitEventWithValue:sharedEvent:eventType:"
- "waitEvents"
- "weightURL"
- "weightWithSymbolAndURL:weightURL:"
- "weightWithSymbolAndURLSHA:weightURL:SHACode:"
- "weightsBuffer"
- "weightsHash"
- "withProcedureData:procedureArray:"
- "writeToFile:atomically:"
- "writeToFile:atomically:encoding:error:"
- "{BuildVersionInfo=IIQ[32C]CQQ[15Q]}16@0:8"
- "{DeviceExtendedInfo={DeviceInfo=IqqB}BII[32c][8c]}16@0:8"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{os_unfair_lock_s=I}16@0:8"

```
