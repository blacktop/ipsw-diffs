## aned

> `/usr/libexec/aned`

```diff

-370.56.0.0.0
-  __TEXT.__text: 0x1be5c
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_stubs: 0x2800
-  __TEXT.__objc_methlist: 0xcac
-  __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x2dcc
-  __TEXT.__cstring: 0xd44
-  __TEXT.__oslogstring: 0x28be
+380.7.0.0.0
+  __TEXT.__text: 0x1e958
+  __TEXT.__auth_stubs: 0x7e0
+  __TEXT.__objc_stubs: 0x2780
+  __TEXT.__objc_methlist: 0xc9c
+  __TEXT.__const: 0x130
+  __TEXT.__gcc_except_tab: 0x3228
+  __TEXT.__cstring: 0x841
+  __TEXT.__oslogstring: 0x2ac9
   __TEXT.__objc_classname: 0x1a0
-  __TEXT.__objc_methname: 0x2eb9
-  __TEXT.__objc_methtype: 0xb97
-  __TEXT.__unwind_info: 0x5b8
-  __DATA_CONST.__auth_got: 0x400
-  __DATA_CONST.__got: 0x190
+  __TEXT.__objc_methname: 0x2e94
+  __TEXT.__objc_methtype: 0xb8a
+  __TEXT.__unwind_info: 0x590
+  __DATA_CONST.__auth_got: 0x408
+  __DATA_CONST.__got: 0x268
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x4b0
-  __DATA_CONST.__cfstring: 0xcc0
+  __DATA_CONST.__const: 0x440
+  __DATA_CONST.__cfstring: 0x720
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x40
-  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x1120
-  __DATA.__objc_selrefs: 0xc38
+  __DATA.__objc_selrefs: 0xc28
   __DATA.__objc_ivar: 0xa4
   __DATA.__objc_data: 0x370
-  __DATA.__data: 0x4f0
+  __DATA.__data: 0x380
   __DATA.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler
   - /System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine
-  - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FD1AC69C-116F-3912-AB9F-BA0A7A764696
-  Functions: 384
-  Symbols:   187
-  CStrings:  1054
+  UUID: C34EF2C7-71FB-3772-9351-FBEAC5FFB529
+  Functions: 375
+  Symbols:   215
+  CStrings:  979
 
Symbols:
+ __os_signpost_emit_with_name_impl
+ _kANEFAOTCacheUrlIdentifierKey
+ _kANEFBaseModelIdentifierKey
+ _kANEFCompilationInitiatedByE5MLKey
+ _kANEFEnableLateLatchKey
+ _kANEFEnablePowerSavingKey
+ _kANEFIntermediateBufferHandleKey
+ _kANEFKeepModelMemoryWiredKey
+ _kANEFMemoryPoolIDKey
+ _kANEFModelCacheIdentifierUsingSourceURLKey
+ _kANEFModelDescriptionKey
+ _kANEFModelHasCacheURLIdentifierKey
+ _kANEFModelIdentityStrKey
+ _kANEFModelInput16KAlignmentArrayKey
+ _kANEFModelInputSymbolIndexArrayKey
+ _kANEFModelInputSymbolsArrayKey
+ _kANEFModelOutput16KAlignmentArrayKey
+ _kANEFModelOutputSymbolIndexArrayKey
+ _kANEFModelOutputSymbolsArrayKey
+ _kANEFModelPreCompiledValue
+ _kANEFModelProcedureIDKey
+ _kANEFModelProcedureNameToIDMapKey
+ _kANEFModelProcedureNameToStatsSizeMapKey
+ _kANEFModelProceduresArrayKey
+ _kANEFModelTypeKey
+ _kANEFPerformanceStatsMaskKey
+ _kANEFSkipPreparePhaseKey
+ _kANEModelKeyAllSegmentsValue
+ _mach_continuous_time
+ _os_signpost_enabled
+ _os_signpost_id_generate
- _CacheDeleteRegisterInfoCallbacks
- _fcntl
- _objc_retain_x27
CStrings:
+ "%@: START : cachedModel.bytes=%p : cachedModel.length=%ld : qos=%d : isPreCompiled=%d : enablePowerSaving=%d : controller.device=%p : programInstance=%p : refcount=%lld : intermediateBufferHandle=%llu : statsMask=%u : memoryPoolId=%llu : enableLateLatch=%d : modelIdentityStr=%@ : cacheUrlIdentifier=%@ : aotCacheUrlIdentifier=%@ optOutOfModelMemoryUnwiring=%d"
+ "%u"
+ "%u %u model.string_id:%llu"
+ "%u, ok:%u, attemptedCount:%lu, removedCount:%lu"
+ "%{public, signpost.description:begin_time}llu "
+ "ANEServicesInitializePlatformServices"
+ "B112@0:8@16@24@32I40B44B48B52I56Q60B68@72i80@84@92B100^@104"
+ "_ANED_ADAPTER_LOAD"
+ "_ANED_COMPILED_MODEL_EXISTS"
+ "_ANED_MODELCACHE_GC"
+ "_ANED_MODEL_COMPILE"
+ "_ANED_MODEL_COMPILE_CONT"
+ "_ANED_MODEL_LOAD"
+ "_ANED_MODEL_PURGE_COMPILED"
+ "_ANED_MODEL_UNLOAD"
+ "_ANED_PREPARE_CHAINING"
+ "_ANED_PURGE_COMPILED_MODEL"
+ "createProgramInstanceForModel:modelToken:modelFilePath:qos:isPreCompiled:enablePowerSaving:skipPreparePhase:statsMask:memoryPoolID:enableLateLatch:modelIdentityStr:owningPid:cacheUrlIdentifier:aotCacheUrlIdentifier:optOutOfModelMemoryUnwiring:error:"
+ "model.string_id:%llu %u"
+ "model.string_id:%llu %u ok:%u"
+ "model.string_id:%llu status:%u"
+ "modelUnLoadingTime"
+ "qos:%u"
+ "qos:%u model.string_id:%llu cachedModel.length:%lu wiredMemory:%lu"
+ "qos:%u model.string_id:%llu numInputs:%u numOutputs:%u"
+ "qos:%u model.string_id:%llu status:%u"
+ "qos:%u model.string_id:%llu wiredMemory:%lu"
+ "qos:%u status:%u"
+ "reportTelemetryToCoreAnalytics:payload:"
+ "unload"
- "%@: CacheDelete dictionary=%@"
- "%@: CacheDelete, urgency: %d and purgeable: %d, purge: %d"
- "%@: START : cachedModel.bytes=%p : cachedModel.length=%ld : qos=%d : isPreCompiled=%d : enablePowerSaving=%d : controller.device=%p : programInstance=%p : refcount=%lld : intermediateBufferHandle=%llu : statsMask=%u : memoryPoolId=%llu : enableLateLatch=%d : modelIdentityStr=%@ : cacheUrlIdentifier=%@ : aotCacheUrlIdentifier=%@"
- "%@: fcntl(F_RDADVISE). errno=%d : %s"
- "@36@0:8@16@24i32"
- "ANEFModelDescription"
- "ANEFModelInput16KAlignmentArray"
- "ANEFModelInputSymbolIndexArray"
- "ANEFModelOutput16KAlignmentArray"
- "ANEFModelOutputSymbolIndexArray"
- "ANEFModelProcedureID"
- "ANEFModelProcedures"
- "B108@0:8@16@24@32I40B44B48B52I56Q60B68@72i80@84@92^@100"
- "CACHE_DELETE_AMOUNT"
- "CACHE_DELETE_ITEMIZED_NONPURGEABLE"
- "CACHE_DELETE_VOLUME"
- "COREML_NON_PURGEABLE_BY_APP"
- "CacheDeleteRegisterInfoCallbacks() returned %d"
- "H11InitializePlatformServices"
- "ModelCacheDeleted"
- "PERIODIC"
- "PURGE"
- "PURGEABLE"
- "^{__CFDictionary=}20@?0i8^{__CFDictionary=}12"
- "cacheDeleteServiceName"
- "com.apple.appleneuralengine._ANEModel.AllSegments"
- "createCacheDeleteDictionaryFrom:userInfo:"
- "createProgramInstanceForModel:modelToken:modelFilePath:qos:isPreCompiled:enablePowerSaving:skipPreparePhase:statsMask:memoryPoolID:enableLateLatch:modelIdentityStr:owningPid:cacheUrlIdentifier:aotCacheUrlIdentifier:error:"
- "handleCacheDeleteCall:userInfo:urgency:"
- "kANEFAOTCacheUrlIdentifierKey"
- "kANEFBaseModelIdentifierKey"
- "kANEFCompilationInitiatedByE5MLKey"
- "kANEFCompilerOptionsFilenameKey"
- "kANEFDisableIOFencesUseSharedEventsKey"
- "kANEFEnableFWToFWSignal"
- "kANEFEnableLateLatchKey"
- "kANEFEnablePowerSavingKey"
- "kANEFEspressoFileResourcesKey"
- "kANEFIntermediateBufferHandleKey"
- "kANEFMemoryPoolIDKey"
- "kANEFModelANECIR"
- "kANEFModelCacheIdentifierUsingSourceURLKey"
- "kANEFModelCoreML"
- "kANEFModelHasCacheURLIdentifierKey"
- "kANEFModelIdentityStrKey"
- "kANEFModelInputSymbolsArrayKey"
- "kANEFModelInstanceParameters"
- "kANEFModelIsEncryptedKey"
- "kANEFModelLoadPerformanceStats"
- "kANEFModelMIL"
- "kANEFModelOutputSymbolsArrayKey"
- "kANEFModelPreCompiled"
- "kANEFModelProcedureNameToIDMapKey"
- "kANEFModelProcedureNameToStatsSizeMapKey"
- "kANEFModelType"
- "kANEFNetPlistFilenameKey"
- "kANEFPerformanceStatsMask"
- "kANEFRetainModelsWithoutSourceURLKey"
- "kANEFSkipPreparePhaseKey"
- "kANEModelKeyEspressoTranslationOptions"

```
